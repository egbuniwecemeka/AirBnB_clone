import uuid
import datetime
from models import storage

class BaseModel:
    """A base class for all common attributes/methods for other classes"""
    def __init__(self, *args, **kwargs):
            """Initializes public instance attributes

            Args:
                 *args: Variable length list
                 *kwargs: keyword arguments for deserialization
            
            """
            if kwargs:
                 # To handle deserializtion, assign values from dictionary
                 for key,value in kwargs.items():
                      if key != '__class__':
                           setattr(self, key, value)
               # converts string dates back to datetime objects
                 self.created_at = datetime.datetime.strptime(self.created_at, "%Y-%m-%dT%H:%M:%S.%f")
                 self.updated_at = datetime.datetime.strptime(self.updated_at, "%Y-%m-%dT%H:%M:%S.%f")
            else:
               # Normal initialization
               self.id = str(uuid.uuid4())
               self.created_at = datetime.datetime.now()
               self.updated_at = self.created_at

               # Add this new instance to storage
               storage.new(self)

    def save(self):
         """Updates current datetime anytime an object is changed"""
         self.updated_at = datetime.datetime.now()
         storage.save()

    
    def __str__(self):
         """Returns a string representation of BaseModel instance"""
         return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"
    
    def to_dict(self):
         """Returns a dictionary containing all key, value pairs of __dict__ of the object's instance

         class name is added to dictionary and datetime object is converted to ISO string format for serialization
         """
         obj_instance_dict = self.__dict__.copy()
         # class name added to dictionary
         obj_instance_dict['__class__'] = self.__class__.__name__
         # datetime objects are converted to ISO strings
         obj_instance_dict['created_at'] = self.created_at.isoformat()
         obj_instance_dict['updated_at'] = self.updated_at.isoformat()
         return obj_instance_dict
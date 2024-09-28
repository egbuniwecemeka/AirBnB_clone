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
         return (f"[{self.__class__.__name__}] ({self.id}) "
                 f"{{'my_number': {self.my_number}, 'name': {self.name}, "
                 f"'updated_at': {repr(self.updated_at)}, 'id': '{self.id}', 'created_at': {repr(self.created_at)}}}"
          )
    
    def to_dict(self):
         """Returns a dictionary containing all key, value pairs of __dict__ of the object's instance

         class name is added to dictionary and datetime object is converted to ISO string format for serialization
         """
         return {'my_number': getattr(self, 'my_number', 0),
                 'name': getattr(self, 'name', ''),
                 '__class__': self.__class__.__name__,
                 'updated_at': self.updated_at.isoformat(),
                 'id': self.id,
                 'created_at': self.created_at.isoformat()
                 }
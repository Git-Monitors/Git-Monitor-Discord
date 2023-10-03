from pydantic import BaseModel

class Updates(BaseModel):
    EventType: str
    EventDescription: str 
    EventUrl : str
    EventReceipients : int
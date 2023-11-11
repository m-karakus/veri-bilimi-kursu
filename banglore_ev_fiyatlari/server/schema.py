
from pydantic import  BaseModel

class Input(BaseModel):
    total_sqft : float = 1000
    location : str = 'subramanyapura'
    bhk : int = 2
    bath : int = 2

class Output(BaseModel):
    estimated_price : float

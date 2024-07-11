from pydantic import BaseModel, Field

class PlaceSchema(BaseModel):
    title : str = Field(None, max_length=100)
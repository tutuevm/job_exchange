from pydantic import BaseModel, Field

class AttributeSchema(BaseModel):
    key : str = Field(None, max_length=50)
    value : str = Field(None, max_length=50)
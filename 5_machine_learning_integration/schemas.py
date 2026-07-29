from pydantic import BaseModel, Field, StrictInt


class InputSchema(BaseModel):
    avg_area_income: float = Field(..., description="Average area income")
    avg_area_house_age: float = Field(..., description="Average area house age")
    avg_area_number_of_rooms: float = Field(..., description="Average area number of rooms")
    avg_area_number_of_bedrooms: float = Field(..., description="Average area number of bedrooms")
    area_population: float = Field(..., description="Area population")
    price: float = Field(..., description="Price of the house")
   


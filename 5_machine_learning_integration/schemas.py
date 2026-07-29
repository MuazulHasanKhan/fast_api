from pydantic import BaseModel, Field, StrictInt


class InputSchema(BaseModel):
    avg_area_income: float = Field(..., description="Average area income", gt = 0)
    avg_area_house_age: float = Field(..., description="Average area house age", gt = 0)
    avg_area_number_of_rooms: float = Field(..., description="Average area number of rooms", gt = 0)
    avg_area_number_of_bedrooms: float = Field(..., description="Average area number of bedrooms", gt = 0)
    area_population: float = Field(..., description="Area population")



   

class OutputSchema(BaseModel):
    price: float = Field(..., description="Price of the house", gt = 0)

    
from pydantic import BaseModel

class HealthInput(BaseModel):
    height_cm: float
    weight_kg: float
    age: int

    physical_activity: int
    smoking_history: int

    alcohol_frequency: float
    fruit_consumption: float
    vegetable_consumption: float
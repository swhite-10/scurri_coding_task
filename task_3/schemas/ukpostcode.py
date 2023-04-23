from pydantic import BaseModel, Field
from typing import Optional


class UKPostcodeService(BaseModel):
    input_postcode: str = Field(
        min_length=6,
        max_length=9
    )
    formatted_postcode: Optional[str]
    outward_code: Optional[str]
    inward_code: Optional[str]
    valid_postcode: bool

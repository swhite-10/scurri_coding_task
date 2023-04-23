from fastapi import APIRouter, HTTPException
from pydantic import ValidationError
from task_3.schemas.ukpostcode import UKPostcodeService
from task_3.services.ukpostcode import UKPostcode

ukpostcode_router = APIRouter(tags=['ukpostcode'])


@ukpostcode_router.get('/', response_model=UKPostcodeService)
def endpoint(input_postcode: str = 'wc2n 4js') -> UKPostcodeService:
    """
    Endpoint for retrieving formatted UK postcode and validation check.
    """

    get_postcode = UKPostcode(input_postcode)

    formatted = get_postcode.postcode_formatter()
    valid_postcode = get_postcode.postcode_validator()

    try:
        if formatted is None:
            return UKPostcodeService(input_postcode=input_postcode,
                                     valid_postcode=valid_postcode)
        else:
            return UKPostcodeService(input_postcode=input_postcode,
                                     formatted_postcode=formatted['Postcode'],
                                     outward_code=formatted['Outward Code'],
                                     inward_code=formatted['Inward Code'],
                                     valid_postcode=valid_postcode)
    except ValidationError:
        raise HTTPException(status_code=400,
                            detail='Ensure input_postcode is between 6 and 9 characters including whitespace')

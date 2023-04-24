from fastapi import APIRouter, HTTPException
from pydantic import ValidationError
from task_3.schemas.ukpostcode import UKPostcodeSchema
from task_3.services.ukpostcode import UKPostcodeService

ukpostcode_router = APIRouter(tags=['UK Postcode Formatter and Validator'])


@ukpostcode_router.get('/', response_model=UKPostcodeSchema)
def endpoint(input_postcode: str = 'wc2n4js') -> UKPostcodeSchema:
    """
    Endpoint for retrieving formatted UK postcode and validation check.
    """

    postcode = UKPostcodeService(input_postcode)

    formatted_postcode = postcode.postcode_formatter()
    valid_postcode = postcode.postcode_validator()

    try:
        if formatted_postcode is None:
            return UKPostcodeSchema(input_postcode=input_postcode,
                                    valid_postcode=valid_postcode)
        else:
            return UKPostcodeSchema(input_postcode=input_postcode,
                                    formatted_postcode=formatted_postcode['Postcode'],
                                    outward_code=formatted_postcode['Outward Code'],
                                    inward_code=formatted_postcode['Inward Code'],
                                    valid_postcode=valid_postcode)
    except ValidationError:
        raise HTTPException(status_code=400,
                            detail='Ensure input_postcode is between 6 and 9 characters including whitespace')

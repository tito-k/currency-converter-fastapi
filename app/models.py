from typing import Dict
from pydantic import BaseModel


class ConversionResultResponse(BaseModel):
    """ Defines the structure of the response returned after a conversion """

    from_currency: str
    to_currency: str
    amount: float
    converted_amount: float


class HistoricalDataResponse(BaseModel):
    from_currency: str
    to_currency: str
    exchange_date: str
    rate_at_date: float
from datetime import date
from fastapi import FastAPI, Depends

from .enums import SupportedCurrencies
from .services import (
    supported_currencies_service,
    currency_converter_service,
    historical_data_service
)
from .models import (
    ConversionResultResponse,
    HistoricalDataResponse
)
from .config import Settings, get_settings


app = FastAPI()


@app.get(
    "/api/v1/currency-converter", 
    response_model=ConversionResultResponse
)
async def currency_converter(
    from_currency: SupportedCurrencies, 
    to_currency: SupportedCurrencies,
    amount: float,
    settings: Settings = Depends(get_settings)
) -> ConversionResultResponse:
    """ Currency conversion route """
    
    response = await currency_converter_service(
        from_currency.name, # Pass the currency's short code. E.g USD
        to_currency.name,
        amount,
        settings
    )
   
    return response


@app.get(
    "/api/v1/historical-data", 
    response_model=HistoricalDataResponse
)
async def historical_data(
    from_currency: SupportedCurrencies, 
    to_currency: SupportedCurrencies,
    date: str,
    settings: Settings = Depends(get_settings)
) -> HistoricalDataResponse:
    """ Returns the exchange rate at the given date """
   
    response = await historical_data_service(
        from_currency.name, # Pass the currency's short code. E.g USD
        to_currency.name,
        date,
        settings
    )

    return response


@app.get("/api/vi/supported-currencies")
def currencies() -> dict:
    """ All supported currencies route """

    currencies = supported_currencies_service()
    return currencies


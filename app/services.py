"""
Each service function here is mapped to a request handler function
in the api.py file. The goal with services is to foster single reponsibility:
    - Each request handler in the api.py file would only accept a request and 
    return a response, and that only.
    - The task of processing a request is moved to services. Our business logic
    lives in the services module
"""
import aiohttp

from .enums import SupportedCurrencies
from .config import Settings
from .utils import currency_api_caller


async def currency_converter_service(
    from_currency: str, 
    to: str, 
    amount: float,
    settings: Settings
):
    """ 
    service for use in the currency_converter route handler.
    Houses all the currency conversion logic.
    """

    URL = settings.EXCHANGE_URL
    query_params = {"from":from_currency, "to":to}

    conversion_rate = await currency_api_caller(settings, URL, query_params)
    converted_amount = amount * float(conversion_rate)

    response = {
        "from_currency": from_currency,
        "to_currency": to,
        "amount": amount,
        "converted_amount": converted_amount
    }
    return response


async def historical_data_service(
    from_currency: str, 
    to: str, 
    date: str,
    settings: Settings
):
    """ 
    service for use in the currency_converter route handler.
    Houses all the currency conversion logic.
    """

    URL = settings.HISTORICAL_URL.format(date)
    query_params = {"from":from_currency, "to":to}

    data = await currency_api_caller(settings, URL, query_params)
    rate = data['rates'][to]['rate']
                
    response = {
        "from_currency": from_currency,
        "to_currency": to,
        "exchange_date": date,
        "rate_at_date": rate
    }
    return response


def supported_currencies_service():
    """ 
    Service for use in the currencies route handler.
    Returns a list of currency shortcodes along with their associated full names
    as key-value pairs
    """
    return {currency.name:currency.value for currency in SupportedCurrencies}
    
"""
Each service function here is mapped to a request handler function
in the main.py file. The goal with services is to foster single reponsibility:
    - Each request handler in the main.py file would only accept a request and 
    return a response, and that only.
    - The task of processing a request is moved to services. Our business logic
    lives in the services module
"""
import aiohttp

from .enums import SupportedCurrencies
from .config import Settings


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
    
    headers = {
        'x-rapidapi-key': settings.API_KEY
    }
    URL = settings.EXCHANGE_URL
    query_params = {"from":from_currency, "to":to}

    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(URL, headers=headers, params=query_params) as response:
                conversion_rate = await response.text()
                
                converted_amount = amount * float(conversion_rate)

                response = {
                        "from_currency": from_currency,
                        "to_currency": to,
                        "amount": amount,
                        "converted_amount": converted_amount
                }
                return response
                
    except Exception as e:
        error = f"erro: {e}"
        response = {
                'error': error
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
    
    headers = {
        'x-rapidapi-key': settings.API_KEY
    }
    URL = settings.HISTORICAL_URL.format(date)
    query_params = {"from":from_currency, "to":to}

    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(URL, headers=headers, params=query_params) as response:
                data = await response.json()
                rate = data['rates'][to]['rate']
                
                response = {
                        "from_currency": from_currency,
                        "to_currency": to,
                        "exchange_date": date,
                        "rate_at_date": rate
                }
                return response
                
    except Exception as e:
        error = f"erro: {e}"
        response = {
                'error': error
        } 
        return response


def supported_currencies_service():
    """ 
    Service for use in the currencies route handler.
    Returns a list of currency shortcodes along with their associated full names
    as key-value pairs
    """
    return {currency.name:currency.value for currency in SupportedCurrencies}
    
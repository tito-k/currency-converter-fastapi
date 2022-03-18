import aiohttp

from .config import Settings


async def currency_api_caller(settings: Settings, url: str, params: dict=None):
    """ 
        A helper function for calling the external APIs
        Moved the api-calling code to this separate function to separate concerns
    """
    
    headers = {
        'x-rapidapi-key': settings.API_KEY
    }

    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(url, headers=headers, params=params) as response:
                if response.content_type == 'text/plain':
                    response = await response.text()
                else:
                    response = await response.json()
                return response
                
    except Exception as e:
        error = f"erro: {e}"
        response = {
                'error': error
        } 
        return response
from enum import Enum


class SupportedCurrencies(str, Enum):
    """
        predefined list of the currencies supported.
        This will also be used to show a more user friendly drop-down
        of all the supported currencies in the docs
    """
    USD = 'USD'
    EUR = 'EUR'
    BRL = 'BRL'
    HKD = 'HKD'
    ZAR = 'ZAR'
    GHS = 'GHS'
    NGN = 'NGN'
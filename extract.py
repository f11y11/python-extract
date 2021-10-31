from typing import Dict, Iterable, Optional, Tuple
from forbiddenfruit import curse, reverse


__all__ = {'extract', 'init', 'term'}

def extract(__items:Iterable, __from:Optional[Dict], __none=True) -> Tuple:
    """
    Extract multiple items from the given dict in the given order

    ## Arguments:
    __items: items (key names) to extract
    __from: the dict to extract __items from
    __none: whether to return None for items that are not found

    ## Returns:
    A tuple containing the extracted items
    >>> mydict = {'key1': 'value1', 'key2': 'value2'}
    >>> extract(('key1', 'key2', 'key3'), mydict)
    ... ('value1', 'value2')
    """

    if isinstance(__from, Dict):
        if not __none:
            items = tuple(value for key, value in __from.items() if key in __items)
        else:
            items = tuple()
            for item in __items:
                items = (*items, __from.get(item))

        return items

def dict_extract(_, __items:Iterable, __none=True) -> Tuple:
    if not __none:
        items = tuple(value for key, value in _.items() if key in __items)
    else:
        items = tuple()
        for item in __items:
            items = (*items, _.get(item))
    return items

def init():
    """
    Adds extract() to default dict class
    AttributeError will be raised if dict.extract() is used and is not initialized
    """
    curse(dict, 'extract', dict_extract)
    assert 'extract' in dir(dict)

def term():
    """
    Removes extract() from default dict class
    """
    reverse(dict, 'extract')
    assert 'extract' not in dir(dict)

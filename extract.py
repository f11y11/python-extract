from typing import Dict, Iterable

def extract(__items:Iterable, __from:Dict, __none=True):
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
    ('value1', 'value2')

    

    """
    if isinstance(__from, Dict):
        if not __none:
            items = tuple(value for key, value in __from.items() if key in __items)
        else:
            items = tuple()
            for item in __items:
                items = (*items, __from.get(item))

        return items

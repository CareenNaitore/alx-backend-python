#!/usr/bin/env python3

""" more involved type annotation"""
from typing import Union, Any, Sequence, Mapping, TypeVar


T = TypeVar('T')


def safely_get_value(dct: Mapping, Key: Any,
                   default:  Union[T, None] = None
                   ) -> Union[Any, T]:
    """Safe first element"""
    if dct:
        return dct[key]
    else:
        return default

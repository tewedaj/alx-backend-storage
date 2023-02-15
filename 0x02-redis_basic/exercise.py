#!/usr/bin/env python3
""" Redis module. """

from functools import wraps
import redis
import sys
from typing import Union, Optional, Callable
from uuid import uuid4

class Cache:
    """ Cache class. """

    def __init__(self):
        """ Init """
        self._redis = redis.Redis()
        self._redis.flushdb()

    @count_calls
    @call_history
    def store(self, data: Union[str, bytes, int, float]) -> str:
        """ Random to store """
        key = str(uuid4())
        self._redis.set(key, data)
        return key

    def get(self, key: str, fn: Optional[Callable] = None) -> Union[str,
                                                                    bytes,
                                                                    int,
                                                                    float]:
        """ Gets  """
        res = self._redis.get(key)
        return fn(res) if fn else res

    def get_str(self, data: bytes) -> str:
        """ Bytes to string """
        return data.decode('utf-8')

    def get_int(self, data: bytes) -> int:
        """ Bytes to integer """
        return int.from_bytes(data, sys.byteorder)
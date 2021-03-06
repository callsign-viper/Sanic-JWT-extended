# Stubs for blacklist (Python 3)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

import abc
from abc import ABC, abstractmethod
from typing import Any

from sanic_jwt_extended.tokens import Token

class BlacklistABC(ABC, metaclass=abc.ABCMeta):
    @abstractmethod
    async def register(self, token: Token) -> None: ...
    @abstractmethod
    async def is_blacklisted(self, token: Token) -> bool: ...

class InMemoryBlacklist(BlacklistABC):
    blacklist: Any = ...
    def __init__(self) -> None: ...
    async def register(self, token: Token) -> None: ...
    async def is_blacklisted(self, token: Token) -> bool: ...

class RedisBlacklist(BlacklistABC):
    def __init__(self):
        self.connection_info = ...
    async def register(self, token: Token) -> None: ...
    async def is_blacklisted(self, token: Token) -> bool: ...

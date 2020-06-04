from abc import ABCMeta, abstractmethod
from datetime import datetime

from base58 import b58decode, b58encode


class AttestationBase(metaclass=ABCMeta):

    @abstractmethod
    def _generate(self, raw: bytes) -> bytes:
        raise Exception("AttestationBase abstract method called")

    @abstractmethod
    def _verify(self, raw: bytes, quote: bytes):
        raise Exception("AttestationBase abstract method called")

    @staticmethod
    def _normalize(qq_number) -> bytes:
        no = int(qq_number)
        return int.to_bytes(no, 8, 'little')

    def generate(self, qq_number):
        qq_number = self._normalize(qq_number)

        ts = int(datetime.now().timestamp())
        timestamp = int.to_bytes(ts, 4, 'little')

        quote = self._generate(timestamp + qq_number)
        return b58encode(timestamp + quote).decode()

    def verify(self, qq_number, quote) -> datetime:
        qq_number = self._normalize(qq_number)

        if not isinstance(quote, bytes):
            quote = b58decode(quote)

        try:
            self._verify(quote[:4] + qq_number, quote[4:])
        except ValueError:
            return None

        ts = int.from_bytes(quote[:4], 'little')
        return datetime.fromtimestamp(ts)

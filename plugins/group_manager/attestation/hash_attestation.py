from Crypto.Hash import HMAC, SHA256

from plugins.group_manager.attestation.base import AttestationBase


class HashAttestation(AttestationBase):
    def __init__(self, secret: bytes, digestmod=SHA256):
        self._secret = secret
        self._mod = digestmod

    @staticmethod
    def load(path, *args, **kwargs):
        from pathlib import Path
        key = Path(path).read_bytes()
        return HashAttestation(key, *args, **kwargs)

    def _common(self, raw: bytes):
        return HMAC.new(self._secret, msg=raw, digestmod=self._mod)

    def _generate(self, raw: bytes) -> bytes:
        h = self._common(raw)
        return h.digest()

    def _verify(self, raw: bytes, quote: bytes):
        h = self._common(raw)
        h.verify(quote)


if __name__ == "__main__":
    from pathlib import Path
    from Crypto.Random import get_random_bytes

    secret = get_random_bytes(16)
    Path('hsecret.bin').write_bytes(secret)

    a = HashAttestation(secret)

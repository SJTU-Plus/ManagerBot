from Crypto.Cipher import AES
from Crypto.Hash import CMAC

from plugins.group_manager.attestation.base import AttestationBase


class CmacAttestation(AttestationBase):
    def __init__(self, secret: bytes, ciphermod=AES):
        self._secret = secret
        self._mod = ciphermod
        if isinstance(ciphermod.key_size, int):
            assert len(secret) == ciphermod.key_size
        else:
            assert len(secret) in ciphermod.key_size

    @staticmethod
    def load(path, *args, **kwargs):
        from pathlib import Path
        key = Path(path).read_bytes()
        return CmacAttestation(key, *args, **kwargs)

    def _common(self, raw: bytes):
        return CMAC.new(self._secret, msg=raw, ciphermod=self._mod)

    def _generate(self, raw: bytes) -> bytes:
        h = self._common(raw)
        return h.digest()

    def _verify(self, raw: bytes, quote: bytes):
        h = self._common(raw)
        h.verify(quote)


if __name__ == "__main__":
    from pathlib import Path
    from Crypto.Random import get_random_bytes

    secret = get_random_bytes(AES.key_size[-1])
    # Path('csecret.bin').write_bytes(secret)
    print(secret.hex())
    # a = CmacAttestation(secret)

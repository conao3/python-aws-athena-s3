import base64
from typing import Any


def encode_object(pya_obj: Any):
    """
    Encodes either a PyArrow Schema or set of Records to Base64.
    I'm not entirely sure why, but I had to cut off the first 4 characters
    of the `serialize()` output to be compatible with the Java SDK.
    """
    return base64.b64encode(pya_obj.serialize().slice(4)).decode("utf-8")

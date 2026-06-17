"""publickipbitan - show your public internet IP address."""

from .core import PublicIPError, get_public_ip, get_public_ip_json

__version__ = "1.0.0"
__author__ = "Bitan Bhattachirjee"
__email__ = "mr.bitanbhattachirjee@gmail.com"

__all__ = [
    "PublicIPError",
    "get_public_ip",
    "get_public_ip_json",
]

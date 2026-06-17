"""Core functions for publickipbitan."""

from __future__ import annotations

import ipaddress
from typing import Iterable
from urllib.error import HTTPError, URLError
from urllib.request import Request, urlopen


DEFAULT_SERVICES = (
    "https://api.ipify.org",
    "https://ifconfig.me/ip",
    "https://icanhazip.com",
)


class PublicIPError(RuntimeError):
    """Raised when public IP detection fails."""


def _read_url(url: str, timeout: float) -> str:
    request = Request(
        url,
        headers={
            "User-Agent": "publickipbitan/1.0.0",
        },
    )

    with urlopen(request, timeout=timeout) as response:
        return response.read(200).decode("utf-8", errors="replace").strip()


def _validate_ip(value: str) -> str:
    candidate = value.strip().split()[0] if value else ""

    try:
        ipaddress.ip_address(candidate)
    except ValueError as exc:
        raise ValueError(f"Invalid IP response: {value!r}") from exc

    return candidate


def get_public_ip(
    timeout: float = 5.0,
    services: Iterable[str] | None = None,
) -> str:
    """
    Return the current machine/network public internet IP address.

    Example
    -------
    >>> import publickipbitan
    >>> publickipbitan.get_public_ip()
    '203.0.113.10'
    """

    service_list = tuple(services) if services is not None else DEFAULT_SERVICES
    errors: list[str] = []

    for url in service_list:
        try:
            response_text = _read_url(url, timeout=timeout)
            return _validate_ip(response_text)
        except (HTTPError, URLError, TimeoutError, ValueError, OSError) as exc:
            errors.append(f"{url}: {exc}")

    raise PublicIPError(
        "Unable to detect public IP address. "
        "Please check your internet connection. "
        "Details: " + " | ".join(errors)
    )


def get_public_ip_json(timeout: float = 5.0) -> dict[str, str]:
    """Return public IP information as a dictionary."""

    ip = get_public_ip(timeout=timeout)
    return {
        "public_ip": ip,
        "ip_version": "IPv6" if ":" in ip else "IPv4",
    }

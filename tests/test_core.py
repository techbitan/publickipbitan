from publickipbitan.core import _validate_ip


def test_validate_ipv4():
    assert _validate_ip("8.8.8.8") == "8.8.8.8"


def test_validate_ipv6():
    assert _validate_ip("2001:4860:4860::8888") == "2001:4860:4860::8888"

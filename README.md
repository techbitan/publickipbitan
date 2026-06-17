# publickipbitan

**Developer:** Bitan Bhattachirjee  
**Email:** mr.bitanbhattachirjee@gmail.com

`publickipbitan` is a simple Python library and command-line tool that shows your public internet IP address.

## Installation

```bash
pip install publickipbitan
```

## Use as Python library

```python
import publickipbitan

ip = publickipbitan.get_public_ip()
print("My public IP is:", ip)
```

## Use as command-line tool

```bash
publickipbitan
```

## JSON output

```bash
publickipbitan --json
```

Example output:

```json
{
  "public_ip": "203.0.113.10",
  "ip_version": "IPv4"
}
```

## Features

- Shows public internet IP address
- Works from Python code
- Works from terminal / CMD
- Supports JSON output
- Uses Python standard library only
- Uses multiple public IP services as fallback
- Validates IPv4 and IPv6 output

## Developer

Created by **Bitan Bhattachirjee**  
Email: **mr.bitanbhattachirjee@gmail.com**

## License

MIT License

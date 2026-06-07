#  IPInfo

A command-line tool to get detailed information about any public IP address.
## Installation

```bash
git clone https://github.com/Mehdi23-bit/ipinfo
cd ipinfo
pip install -r requirements.txt
```

## Usage

```bash
python ipinfo.py <ip>
```

## Examples

```bash
python ipinfo.py 8.8.8.8
python ipinfo.py 1.1.1.1
```

## Error Handling

|    Input    |      Response     |
|-------------|-------------------|
| Private IP  |  private addr     |
| Loopback    |  loopback addr    |
| Invalid IP  |  not a valid IP   |
| No argument | Usage message     |
| No internet | Connection error  |

## Requirements
requests
colorama
## Author

**Mehdi** — [@Mehdi23-bit](https://github.com/Mehdi23-bit)

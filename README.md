# I2C Relay Python Library

A Python library for controlling I2C relay modules.

## Installation

1. Clone this repository
2. Create and activate a virtual environment:
   ```bash
   python -m venv venv
   venv\Scripts\activate  # On Windows
   source venv/bin/activate  # On Linux/macOS
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

```python
from i2c_relay import I2CRelay

# Initialize the relay controller
relay = I2CRelay()

# Control relays
relay.turn_on(1)  # Turn on relay 1
relay.turn_off(1)  # Turn off relay 1
```

## Development

- Follow PEP 8 style guide
- Use type hints for all functions
- Include docstrings for all public methods
- Write unit tests for new features

## License

MIT License
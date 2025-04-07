# I2C Relay Python Library

A Python library for controlling I2C relay modules. Compatible with Raspberry Pi 5 and Raspberry Pi OS 64-bit.

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

## Contributing

We welcome contributions to this project! Here's how you can help:

- Report bugs and suggest features by opening issues
- Submit pull requests with bug fixes and new features
- Improve documentation
- Share your experiences and use cases

### Development Setup
1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## Donations

If you find this library useful and would like to support its development, consider making a donation. Your support helps maintain and improve this project.

[![Donate](https://img.shields.io/badge/Donate-PayPal-green.svg)](https://www.paypal.com/donate/?hosted_button_id=YOUR_BUTTON_ID)

## License

MIT License

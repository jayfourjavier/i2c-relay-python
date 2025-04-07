"""
Basic example of controlling I2C relays using the i2c_relay library.
"""

from i2c_relay import I2CRelay
import time
from loguru import logger

def main():
    # Configure logging
    logger.add("relay_control.log", rotation="1 MB")
    
    # Initialize relay controller
    relay = I2CRelay(i2c_address=0x20)
    
    try:
        # Toggle relay 1 every second
        while True:
            logger.info("Turning relay 1 on")
            relay.turn_on(1)
            time.sleep(1)
            
            logger.info("Turning relay 1 off")
            relay.turn_off(1)
            time.sleep(1)
            
    except KeyboardInterrupt:
        logger.info("Program terminated by user")
    except Exception as e:
        logger.error(f"An error occurred: {str(e)}")

if __name__ == "__main__":
    main() 
from binance.exceptions import BinanceAPIException
from requests.exceptions import RequestException
from bot.client import client
import logging


def place_market_order(symbol, side, quantity):
    try:
        logging.info(
            f"Request | MARKET | Symbol={symbol} | Side={side} | Quantity={quantity}"
        )

        order = client.futures_create_order(
            symbol=symbol,
            side=side,
            type="MARKET",
            quantity=quantity
        )

        logging.info(f"Response | {order}")
        return order

    except BinanceAPIException as e:
        logging.error(f"Binance API Error: {e}")
        raise

    except RequestException as e:
        logging.error(f"Network Error: {e}")
        raise

    except Exception as e:
        logging.error(f"Unexpected Error: {e}")
        raise


def place_limit_order(symbol, side, quantity, price):
    try:
        logging.info(
            f"Request | LIMIT | Symbol={symbol} | Side={side} | Quantity={quantity} | Price={price}"
        )

        order = client.futures_create_order(
            symbol=symbol,
            side=side,
            type="LIMIT",
            quantity=quantity,
            price=price,
            timeInForce="GTC"
        )

        logging.info(f"Response | {order}")
        return order

    except BinanceAPIException as e:
        logging.error(f"Binance API Error: {e}")
        raise

    except RequestException as e:
        logging.error(f"Network Error: {e}")
        raise

    except Exception as e:
        logging.error(f"Unexpected Error: {e}")
        raise
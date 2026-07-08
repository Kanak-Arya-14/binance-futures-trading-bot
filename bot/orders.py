from binance.exceptions import BinanceAPIException
from bot.client import client
import logging


def place_market_order(symbol, side, quantity):
    try:
        order = client.futures_create_order(
            symbol=symbol,
            side=side,
            type="MARKET",
            quantity=quantity
        )

        logging.info(order)
        return order

    except BinanceAPIException as e:
        logging.error(e)
        raise


def place_limit_order(symbol, side, quantity, price):
    try:
        order = client.futures_create_order(
            symbol=symbol,
            side=side,
            type="LIMIT",
            quantity=quantity,
            price=price,
            timeInForce="GTC"
        )

        logging.info(order)
        return order

    except BinanceAPIException as e:
        logging.error(e)
        raise
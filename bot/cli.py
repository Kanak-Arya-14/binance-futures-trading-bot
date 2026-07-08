import argparse


def parse_args():
    parser = argparse.ArgumentParser(
        description="Binance Futures Trading Bot"
    )

    parser.add_argument(
        "--symbol",
        required=True,
        help="Trading Pair (Example: BTCUSDT)"
    )

    parser.add_argument(
        "--side",
        choices=["BUY", "SELL"],
        required=True,
        help="Order Side"
    )

    parser.add_argument(
        "--type",
        choices=["MARKET", "LIMIT"],
        required=True,
        help="Order Type"
    )

    parser.add_argument(
        "--quantity",
        type=float,
        required=True,
        help="Order Quantity"
    )

    parser.add_argument(
        "--price",
        type=float,
        help="Required only for LIMIT orders"
    )

    return parser.parse_args()
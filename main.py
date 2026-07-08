from bot.cli import parse_args
from bot.validators import validate_input
from bot.orders import place_market_order, place_limit_order
import bot.logging_config


def main():
    args = parse_args()

    try:
        validate_input(
            args.symbol,
            args.side,
            args.type,
            args.quantity,
            args.price
        )

        if args.type.upper() == "MARKET":
            order = place_market_order(
                args.symbol,
                args.side.upper(),
                args.quantity
            )

        else:
            order = place_limit_order(
                args.symbol,
                args.side.upper(),
                args.quantity,
                args.price
            )

        print("\n========== ORDER SUCCESS ==========")
        print(f"Order ID : {order['orderId']}")
        print(f"Status   : {order['status']}")
        print(f"Executed : {order['executedQty']}")

        if "avgPrice" in order:
            print(f"Avg Price: {order['avgPrice']}")

    except Exception as e:
        print(f"\nError : {e}")


if __name__ == "__main__":
    main()
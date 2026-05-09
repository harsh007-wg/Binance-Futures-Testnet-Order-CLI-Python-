import argparse

from app.client import BinanceFuturesClient
from app.validators import (
    validate_side,
    validate_order_type,
    validate_quantity
)

from app.logger import logger


def print_response(response):
    print("\n========== ORDER RESPONSE ==========")
    print(f"Order ID      : {response.get('orderId')}")
    print(f"Status        : {response.get('status')}")
    print(f"Executed Qty  : {response.get('executedQty')}")
    print(f"Avg Price     : {response.get('avgPrice')}")
    print("====================================\n")


def main():
    parser = argparse.ArgumentParser(
        description="Binance Futures Testnet Trading CLI"
    )

    parser.add_argument("--symbol", required=True)
    parser.add_argument("--side", required=True)
    parser.add_argument("--type", required=True)
    parser.add_argument("--quantity", required=True)
    parser.add_argument("--price")

    args = parser.parse_args()

    try:
        symbol = args.symbol.upper()
        side = validate_side(args.side)
        order_type = validate_order_type(args.type)
        quantity = validate_quantity(args.quantity)

        print("\n========== ORDER REQUEST ==========")
        print(f"Symbol   : {symbol}")
        print(f"Side     : {side}")
        print(f"Type     : {order_type}")
        print(f"Quantity : {quantity}")

        if order_type == "LIMIT":
            if not args.price:
                raise ValueError(
                    "Price is required for LIMIT orders"
                )

            price = float(args.price)
            print(f"Price    : {price}")

        print("===================================\n")

        client = BinanceFuturesClient()

        if order_type == "MARKET":
            response = client.place_market_order(
                symbol,
                side,
                quantity
            )

        else:
            response = client.place_limit_order(
                symbol,
                side,
                quantity,
                price
            )

        print_response(response)

        print("✅ Order placed successfully")

    except Exception as e:
        logger.error(str(e))
        print(f"❌ Error: {e}")


if __name__ == "__main__":
    main()

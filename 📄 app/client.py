from binance.client import Client
from binance.exceptions import BinanceAPIException
from app.config import API_KEY, API_SECRET
from app.logger import logger


class BinanceFuturesClient:
    def __init__(self):
        self.client = Client(API_KEY, API_SECRET)
        self.client.FUTURES_URL = "https://testnet.binancefuture.com/fapi"

    def place_market_order(self, symbol, side, quantity):
        try:
            logger.info(
                f"MARKET ORDER REQUEST | {symbol} {side} qty={quantity}"
            )

            response = self.client.futures_create_order(
                symbol=symbol,
                side=side,
                type="MARKET",
                quantity=quantity
            )

            logger.info(f"MARKET ORDER RESPONSE | {response}")

            return response

        except BinanceAPIException as e:
            logger.error(f"Binance API Error: {e}")
            raise

        except Exception as e:
            logger.error(f"Unexpected Error: {e}")
            raise

    def place_limit_order(self, symbol, side, quantity, price):
        try:
            logger.info(
                f"LIMIT ORDER REQUEST | {symbol} {side} qty={quantity} price={price}"
            )

            response = self.client.futures_create_order(
                symbol=symbol,
                side=side,
                type="LIMIT",
                quantity=quantity,
                price=price,
                timeInForce="GTC"
            )

            logger.info(f"LIMIT ORDER RESPONSE | {response}")

            return response

        except BinanceAPIException as e:
            logger.error(f"Binance API Error: {e}")
            raise

        except Exception as e:
            logger.error(f"Unexpected Error: {e}")
            raise

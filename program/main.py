from constants import ABORT_ALL_POSITIONS, FIND_COINTEGRATED
from func_connections import connect_dydx
from func_private import abort_all_positions
from func_public import construct_market_prices
from func_messaging import send_message

if __name__ == "__main__":
    
    # success = send_message("Wowzers another awesome message")
    # print(success)
    exit(1)

    # Connect to client
    try:
        print("Connecting to Client...")
        client = connect_dydx()
    except Exception as e:
        print("Error connecting to client: ", e)
        exit(1)

    # Abort all open positions
    if ABORT_ALL_POSITIONS:
        try:
            print("Closing all positions...")
            close_orders = abort_all_positions(client)
        except Exception as e:
            print("Error aborting all open positions: ", e)
            exit(1)

    # Find Cointegrated Pairs
    if FIND_COINTEGRATED:
        try:
            print("Fecthing market prices, please allow 3 mins...")
            df_market_prices = construct_market_prices(client)
        except Exception as e:
            print("Error constructing market prices: ", e)
            exit(1)

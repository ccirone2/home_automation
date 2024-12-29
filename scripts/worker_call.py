# scripts/worker.py
import os
import anvil.server


if __name__ == "__main__":
    """
    Connects to Anvil app using uplink and calls a server function
    """

    uplink_key = os.environ["ANVIL_UPLINK_KEY"]

    try:
        anvil.server.connect(uplink_key)
        anvil.server.call("collect_temperature_data")

    finally:
        anvil.server.disconnect()

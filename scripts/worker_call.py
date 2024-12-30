# scripts/worker_call.py
"""
This script is called on a schedule using github Actions.
The Action configuration .yml file is in .github/workflows/
The uplink key is stored in github Secrets.
"""

import os
import anvil.server

client_uplink_key = os.environ["ANVIL_UPLINK_KEY"]

if __name__ == "__main__":
    """Connect to Anvil server as client and run a callable server function."""
    try:
        anvil.server.connect(client_uplink_key)
        anvil.server.call("fetch_nest_temperature", save=True)
    finally:
        anvil.server.disconnect()

import requests
import argparse
import time

SOLSCAN_API_BASE = "https://public-api.solscan.io"

def get_wallet_tokens(address: str):
    url = f"{SOLSCAN_API_BASE}/account/tokens?account={address}"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        raise Exception(f"API error: {response.status_code} {response.text}")

def main():
    parser = argparse.ArgumentParser(description="Solscan Wallet Auto Check CLI")
    parser.add_argument("address", help="Solana wallet address to check")
    parser.add_argument("--interval", type=int, default=0, help="Auto-check interval in seconds (0 = no auto-check)")
    args = parser.parse_args()

    try:
        while True:
            tokens = get_wallet_tokens(args.address)
            print(f"Token balances for {args.address}:")
            for token in tokens:
                print(f"- {token.get('tokenName')} ({token.get('tokenSymbol')}): {token.get('tokenAmount')}")
            if args.interval <= 0:
                break
            print(f"Waiting {args.interval} seconds before next check...\n")
            time.sleep(args.interval)
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()

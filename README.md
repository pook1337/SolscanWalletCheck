
# SolscanWalletCheck

A Python tool to check and verify Solana wallet information using Solscan API or related blockchain data sources.

## Overview

**SolscanWalletCheck** is a lightweight Python script designed to interact with the Solana blockchain via Solscan or similar APIs to retrieve and verify wallet details. This tool can be used for wallet balance checks, transaction history retrieval, or general wallet status verification on the Solana network.

## Features

- Query Solana wallet information  
- Retrieve wallet balance and transaction history  
- Simple Python implementation (`sol.py`)  
- Easy to extend for additional Solana blockchain features

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/pook1337/SolscanWalletCheck.git
   cd SolscanWalletCheck
   ```
2. (Optional) It is recommended to use a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```
3. Install required dependencies (if any):
   ```bash
   pip install -r requirements.txt
   ```
   *(If `requirements.txt` is not present, you may need to install packages like `requests` manually.)*

## Usage

Run the script with Python:

```bash
python sol.py
```

Modify `sol.py` to input the wallet address you want to check or extend the functionality as needed.

## Contributing

Contributions and suggestions are welcome! Feel free to open issues or submit pull requests to improve the project.


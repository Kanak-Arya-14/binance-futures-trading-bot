# Binance Futures Trading Bot

A Python-based Command Line Interface (CLI) trading bot developed for the Binance Futures Testnet. The application allows users to place MARKET and LIMIT orders on Binance Futures (USDT-M) while maintaining a clean modular architecture, input validation, structured logging, and exception handling.

---

## Features

- Place MARKET Orders
- Place LIMIT Orders
- BUY and SELL Support
- Command Line Interface using argparse
- Input Validation
- Exception Handling
- API Request & Response Logging
- Modular Project Structure
- Easy Configuration using Environment Variables

---

## Project Structure

```
trading_bot/
│
├── bot/
│   ├── __init__.py
│   ├── client.py
│   ├── orders.py
│   ├── validators.py
│   ├── logging_config.py
│   └── cli.py
│
├── logs/
│   └── trading.log
│
├── .env
├── .gitignore
├── main.py
├── README.md
└── requirements.txt
```

---

## Technologies Used

- Python 3.x
- python-binance
- python-dotenv
- argparse
- logging

---

## Installation

### 1. Clone Repository

```bash
git clone https://github.com/Kanak-Arya-14/binance-futures-trading-bot.git
```

### 2. Move into the project

```bash
cd binance-futures-trading-bot
```

### 3. Create Virtual Environment

```bash
python -m venv venv
```

### 4. Activate Virtual Environment

Windows

```bash
venv\Scripts\activate
```

Linux / macOS

```bash
source venv/bin/activate
```

### 5. Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Environment Variables

Create a `.env` file in the project root.

```env
API_KEY=YOUR_API_KEY
API_SECRET=YOUR_API_SECRET
```

---

## Usage

### Place a MARKET Order

```bash
python main.py --symbol BTCUSDT --side BUY --type MARKET --quantity 0.001
```

---

### Place a LIMIT Order

```bash
python main.py --symbol BTCUSDT --side BUY --type LIMIT --quantity 0.001 --price 50000
```

---

## Input Parameters

| Parameter | Description |
|-----------|-------------|
| symbol | Trading Pair (Example: BTCUSDT) |
| side | BUY or SELL |
| type | MARKET or LIMIT |
| quantity | Order Quantity |
| price | Required only for LIMIT Orders |

---

## Validation

The application validates:

- Valid BUY / SELL side
- Valid MARKET / LIMIT order type
- Positive Quantity
- Price Required for LIMIT Orders
- Positive Price for LIMIT Orders

---

## Logging

All important events are logged to:

```
logs/trading.log
```

The log file includes:

- API Requests
- API Responses
- Binance API Errors
- Network Errors
- Unexpected Exceptions

---

## Error Handling

The application gracefully handles:

- Invalid User Input
- Binance API Exceptions
- Network Exceptions
- Unexpected Runtime Errors

---

## Example Output

```
========== ORDER SUMMARY ==========
Symbol        : BTCUSDT
Side          : BUY
Order Type    : MARKET
Order ID      : 123456789
Status        : FILLED
Executed Qty  : 0.001
Average Price : 108432.57
===================================
```

---

## Requirements

- Python 3.x
- Binance Futures Testnet Account
- Binance API Key
- Binance Secret Key
- Internet Connection

---

## Assumptions

- The application is designed for Binance Futures Testnet (USDT-M).
- Users must generate valid API credentials before running the application.
- API credentials should be stored securely inside a `.env` file.

---

## Future Improvements

- Stop-Limit Order Support
- OCO Order Support
- Grid Trading Strategy
- Interactive CLI Menu
- Web-based User Interface
- Unit Testing
- Docker Support

---

## Author

Developed as part of the Python Developer Internship Assignment for **Primetrade.ai**.
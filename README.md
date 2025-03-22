# DigitalOcean Invoice Cost Notifier

This project is a Python script that fetches the latest invoice and billing information from DigitalOcean and sends it to a specified Telegram chat or WhatsApp group using Twilio.

## Features
- Fetches the latest invoice details from DigitalOcean.
- Sends the invoice details to a Telegram chat.
- Optionally, sends the invoice details to a WhatsApp group using Twilio.

## Requirements
- Python 3.x
- `requests` library
- `python-telegram-bot` library
- `twilio` library (if sending to WhatsApp)

## Installation
1. Clone this repository:
   ```bash
   git clone <repository-url>
   cd <repository-directory>
   ```

2. Install the required libraries:
   ```bash
   pip install requests python-telegram-bot twilio
   ```

3. Set up your DigitalOcean personal access token and Twilio credentials in the script:
   - Replace `DO_TOKEN` with your DigitalOcean personal access token.
   - Replace `TWILIO_ACCOUNT_SID`, `TWILIO_AUTH_TOKEN`, and phone numbers with your Twilio credentials.

## Usage
1. Run the script:
   ```bash
   python3 digitalocean_invoice_cost.py
   ```

2. The script will fetch the latest invoice details and send them to the specified Telegram chat or WhatsApp group.

## License
This project is licensed under the MIT License.

## Author
Your Name

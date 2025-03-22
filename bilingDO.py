import requests
from telegram import Bot
import asyncio

# Initialize Telegram bot with the provided token
TELEGRAM_TOKEN = 'isikan telegrambot'
CHAT_ID = 'chatid'
bot = Bot(token=TELEGRAM_TOKEN)

# DigitalOcean personal access token
DO_TOKEN = 'token do4'

# Function to check the latest invoice
# Function to check the latest invoice
def check_latest_invoice():
    headers = {
        'Authorization': f'Bearer {DO_TOKEN}',
        'Content-Type': 'application/json'
    }
    response = requests.get('https://api.digitalocean.com/v2/customers/my/invoices', headers=headers)

    if response.status_code == 200:
        invoice_data = response.json()
        if 'invoice_preview' in invoice_data:
            invoice = invoice_data['invoice_preview']
            message = (f"*Billing Cloud : DigitalOcean*\n"  
                       f"================================\n"
                       f"#=======Latest Invoice Details:=======#\n"
                       f"================================\n\n"  
                       f"*Invoice ID:* {invoice['invoice_id']}\n"  
                       f"*Amount Due:* {invoice['amount']}\n"  
                       f"*Invoice Period:* {invoice['invoice_period']}\n================================")

            return message
    else:
        # Print debugging information
        print(f"Error: {response.status_code} - {response.text}")
        return "Error fetching latest invoice."

# Function to get cost estimation
def get_cost_estimation():
    headers = {
        'Authorization': f'Bearer {DO_TOKEN}'
    }
    response = requests.get('https://api.digitalocean.com/v2/customers/my/billing', headers=headers)

    if response.status_code == 200:
        billing_info = response.json()
        estimated_cost = billing_info.get('estimated_cost', 'No estimated cost available')
        message = f"Estimated Cost: {estimated_cost}"
        return message
    else:
        # Print debugging information
        print(f"Error: {response.status_code} - {response.text}")
        return "Error fetching cost estimation."

# Main function to execute the logic
async def main():
    invoice_message = check_latest_invoice()
    if invoice_message:
        await bot.send_message(chat_id=CHAT_ID, text=invoice_message)
    else:
        cost_message = get_cost_estimation()
        await bot.send_message(chat_id=CHAT_ID, text=cost_message)

if __name__ == "__main__":
    asyncio.run(main())

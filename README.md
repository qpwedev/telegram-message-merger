# Telegram Message Merger

Telegram Message Merger is a script that combines your last messages sent in a private chat within a 30-second interval into a single message, deletes the old messages, and edits the first message to include the content of the others.

## Getting Started

To run this script on your local machine, follow these steps:

## Prerequisites

- Python 3.7 or higher
- Telegram account

## Installation

1. Clone the repository:

```bash
git clone https://github.com/yourusername/telegram-message-merger.git
```

1. Change the working directory:

```bash
cd telegram-message-merger
```

1. Install the required packages:

```
pip install -r requirements.txt
```

1. Create a new .env file in the project directory and add your API_ID, API_HASH, and MY_ID from your Telegram account:
   makefile

```
API_ID="<YOUR_VALUE>"
API_HASH="<YOUR_VALUE>"
MY_ID="<YOUR_VALUE>"
```

1. Replace <YOUR_VALUE> with your actual API ID, API HASH, and MY_ID values.

## Obtaining API_ID and API_HASH

To get the `API_ID` and `API_HASH` for your Telegram application, follow these steps:

1. Go to the [Telegram API Portal](https://my.telegram.org/).
1. Login with your phone number.
1. Click on the API development tools link.
1. Click on the Create New Application button.
1. Fill in the required fields and click on the Create button.
1. Your `API_ID` and `API_HASH` will be displayed on the next page.

Make sure to add these values to your `.env` file as mentioned in the Installation section.

## Usage

Run the script:

```bash
python3 src/main.py
```

Start a private chat with yourself on Telegram and send messages. The script will automatically merge the messages sent within a 30-second interval.

## Contributing

Contributions are welcome! If you have any suggestions, feature requests, or bug reports, feel free to open an issue or submit a pull request.

## Contact

If you have any questions or need help, feel free to contact me on Telegram: [@qpwedev](https://t.me/qpwedev).


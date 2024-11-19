# Website Monitoring and Notification Script

This repository contains two scripts that monitor the availability of a website and send an email notification if the website is down:

- **Python Script (`website_monitor.py`)**: A Python script that checks if a website is up by making a GET request using the `requests` library. If the website is down, it sends an email using Gmail's SMTP server.
- **Bash Script (`website_monitor.sh`)**: A Bash script that checks a website’s HTTP status using `curl` and sends an email if the website is down using the `mail` command.

## Features
- **Website Monitoring**: Both scripts check the availability of a specified website.
- **Email Notification**: If the website is down, the script sends an email notification.
- **Customizable**: You can configure the recipient email and website URL.

## Prerequisites

### Python Script
To run the Python script, ensure you have the following:

- **Python 3** (you can check by running `python --version`).
- **Required Python libraries**:
  - `requests` for sending HTTP requests.
  - `python-dotenv` for loading environment variables from a `.env` file.

Install the necessary libraries with `pip`:

```bash
pip install requests python-dotenv

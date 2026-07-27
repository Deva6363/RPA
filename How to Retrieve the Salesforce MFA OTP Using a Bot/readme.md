# Salesforce MFA TOTP Generator

This repository contains a Python script that generates a Time-based One-Time Password (TOTP) from a Salesforce MFA secret key.

## Prerequisites

Install the required dependency:

```bash
pip install pyotp
```

## Obtaining the Salesforce MFA Secret Key

Before using the script, you must obtain the Salesforce MFA secret key associated with your Salesforce account.

Follow the Salesforce documentation for instructions:

https://help.salesforce.com/s/articleView?id=xcloud.mfa_automation_totp.htm&type=5

## Usage

The Python script accepts the Salesforce MFA secret key as a command-line parameter and returns the current OTP.

Example:

```bash
python salesforce_Totp_login.py
```


Output:

```text
123456
```

## Script Behavior

- Accepts a Salesforce MFA secret key as input.
- Uses the `pyotp` library to generate a TOTP.
- Prints the current OTP to standard output.

## Notes

- Keep your secret key secure and do not commit it to source control.
- The generated OTP is time-based and changes periodically.
- Ensure your system clock is synchronized to avoid invalid OTP generation.

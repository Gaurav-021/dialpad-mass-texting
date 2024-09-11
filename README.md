# Dialpad Script
This script is used to mass text message using Dialpad's API with Python.

## Development
Download the code on your local machine:
```git clone https://github.com/Gaurav-021/dialpad-mass-texting```

Install dependencies:
```pip install -r requirements.txt```

Please note that there are two empty files in this project that require attention in order for this script to run as expected, the files are as follows:
 * `phone.csv` - contains the phone numbers to which the message gets sent. As per [Dialpad's documentation](https://developers.dialpad.com/docs), phone numbers must be E.164 formatted.
 *  `data.yml` - contains [confidential data](https://developers.dialpad.com/docs/authentication-basics) (e.g., API key, sender group ID, and user ID). 
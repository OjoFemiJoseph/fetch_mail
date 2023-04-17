# FETCH MAILS FROM GMAIL INBOX

This is an application that fetches and parses email data from a Gmail account using IMAP protocol. It extracts sender, subject, date, and body information from the emails and stores them in a CSV file.

## How to Use

1. Set up Environment Variables
    - Set the following environment variables in a .env file, a sample env file has been provided:
        - EMAIL: Your email address
        - PASSWORD: Your app password
   

2. Install Dependencies
    - Run `pip install -r requirements.txt` to install the required Python packages.

3. Run the Application
    - Execute the script to run the email application.
    - The script will fetch 50 emails from the INBOX folder and store the extracted data in a CSV file named "email.csv" (edit line 61 if you need more than 50).

4. How to Generate App Password
    - If you are using a Gmail account and have enabled 2-Step Verification, you need to generate an app password to use with this application.
    - Follow the instructions in this link to generate an app password: [Create App Password](https://www.google.com/amp/s/tech.hindustantimes.com/amp/how-to/what-is-gmail-app-password-and-how-to-create-one-71672827876186.html)



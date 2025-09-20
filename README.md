# QR Code Web App

A web application to generate QR codes in your browser using **Flask** and **Python**.

---

## Features

- Enter text, URL, email, or phone number.
- Generate QR code instantly on the web page.
- Clean and responsive interface.
- Automated Selenium test available.

---

Automated Test (Selenium)

test_qr.py automatically tests QR code generation:

Opens the web app in a browser.

Enters a test URL in the input box.

Clicks the Generate QR button.

Waits for the QR code to appear.

Verifies that the QR code image is present on the page.

Closes the browser.

This ensures the main functionality of your QR code generator works correctly.

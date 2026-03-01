# Simple QR Code Generator
# This script asks for a URL/text input and saves the generated QR code as qrcode.png.

import qrcode

# Take URL/text from the user and remove surrounding spaces.
url = input("Enter the URL:").strip()

# Output file path for the generated QR code image.
file_path = "qrcode.png"

# Create QR code object.
qr = qrcode.QRCode()

# Add user input to QR code data.
qr.add_data(url)

# Generate image from QR code data.
img = qr.make_image()

# Save image to disk.
img.save(file_path)

# Confirm where the file was saved.
print(f"QR code saved to {file_path}")

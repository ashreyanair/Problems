import qrcode

upi_id = "ashreyanair2004@okhdfcbank"          # e.g., amoolya@okaxis
name = "A Shreya Nair"               # Your real name
amount = "100"                   # Optional: can be "0" or leave blank
currency = "INR"                 # Currency

# UPI payment URL
upi_url = f"upi://pay?pa={upi_id}&pn={name}&am={amount}&cu={currency}"

# Generate QR code
img = qrcode.make(upi_url)

# Save QR code image
img.save("gpay_qr.png")
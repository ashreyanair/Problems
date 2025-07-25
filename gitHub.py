import qrcode
url = "https://github.com/ashreyanair/Problems"
qrimg = qrcode.make(url)
qrimg.save("github.png")
print("QR code saved as githubqr.png")
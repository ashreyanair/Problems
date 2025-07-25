import qrcode
a=qrcode.QRCode()
def get_info():
    file=open("dog.txt", "r")
    x=file.read()
    return x
text_msg=get_info()
a.add_data(text_msg)
a.make(fit=True)
b=a.make_image(fill_color="black",back_color="white")
b.save("dog.png")
print("sucessful")
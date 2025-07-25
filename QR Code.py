import qrcode
a=qrcode.QRCode()
txt_msg="Hi Students, you are disciplined"
a.add_data(txt_msg)
a.make(fit=True)
b=a.make_image(fill_color="black",black_color="white")
b.save("hi.png")
print("Saved successfully")
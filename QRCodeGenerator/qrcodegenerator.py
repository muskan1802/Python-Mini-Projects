import qrcode
import image
import os

qr = qrcode.QRCode(
    version = 15, # version of qr code high the no bigger the code image and complicated picture
    box_size = 10, # where qr code will be displayed
    border = 5 # white part of image -- border in all 4 sides with white color
)

data = "https://github.com/muskan1802"
# copied the path which is to be converted into qrcode , instead of link you can also insert normal text by simply writing in data variable

qr.add_data(data)
qr.make(fit = True)
img = qr.make_image(fill="black",back_color="white")

img.save("test.png")
os.system("test.png")
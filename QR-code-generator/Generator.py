import qrcode
import image

qr = qrcode.QRCode(
    version=5,  # 15 means the version od the qrcode, higher the number bigger the code image and complicated picture.
    box_size=10,  # size of the box where qr code will be displayed.
    border=5  # it is the white part of the image -- border in all 4 sides with white color.
)
# Path of my quora account.
data = "https://www.quora.com/profile/Vishwajeet-Muthe"
# data = "https://www.youtube.com/@vishwajeetmuthe8452/playlists"
# data = "Hello World!"
# data = "https://www.youtube.com/channel/UCAYO6s81Sqtd7hQqwXORKtg/playlists"


qr.add_data(data)
qr.make(fit=True)
img = qr.make_image(fill="black", back_color="white")
img.save("MyQRCode.png")

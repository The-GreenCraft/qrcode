import qrcode

def generate(data, file_name):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=0,
    )
    qr.add_data(data)
    qr.make(fit=True)

    img = qr.make_image(fill_color="black", back_color="white")
    img.save(file_name)
    print("QR-Code generated!")



link = "https://www.youtube.com/watch?v=dQw4w9WgXcQ"
image = "cupo.jpg"

generate(link, image)
!pip install qrcode[pil]
import qrcode

# Data to be encoded in the QR code
data = "https://example.com"

# Creating an instance of QRCode
qr = qrcode.QRCode(
    version=1,  # Controls the size of the QR code, 1 is the smallest
    error_correction=qrcode.constants.ERROR_CORRECT_L,  # Error correction level (L, M, Q, H)
    box_size=10,  # Size of each box in pixels
    border=4,  # Thickness of the border (minimum is 4)
)

# Add data to the QR code instance
qr.add_data(data)
qr.make(fit=True)  # Generate the QR code

# Create an image from the QR Code instance
img = qr.make_image(fill_color="white", back_color="black")

# Save the image to a file
img.save("qrcode.png")

print("QR code generated and saved as 'qrcode.png'.")

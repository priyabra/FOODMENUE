import qrcode
import os

# URL of your menu page
menu_url = "https://yourdomain.com/menu.html"

# Get current script directory
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Create images folder inside FOODMENUE
images_dir = os.path.join(BASE_DIR, "images")
os.makedirs(images_dir, exist_ok=True)

# Full file path
file_path = os.path.join(images_dir, "food_menu_qr.png")

# Generate QR
qr = qrcode.make(menu_url)
qr.save(file_path)

print("QR Code generated at:", file_path)


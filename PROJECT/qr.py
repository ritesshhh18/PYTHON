import pyqrcode
from PIL import Image, ImageOps
import imageio
import os

# List of URLs to generate QR codes for
urls = [
    "https://www.eisystems.in/",
    "https://www.google.co.in/",
    "https://in.linkedin.com/",
    "https://www.youtube.com/"
]

# Function to generate QR codes with different customizations
def generate_custom_qrs(urls):
    for index, url in enumerate(urls):
        # Generate QR code
        qr = pyqrcode.create(url)
        temp_filename = f"myqr_{index + 1}.png"
        try:
            qr.png(temp_filename, scale=8)

            # Open the generated QR code
            img = Image.open(temp_filename)

            # Apply customizations based on index % 4
            if index % 4 == 0:
                # First QR code is simple
                img.save(f"simple_qr_{index + 1}.png")

            elif index % 4 == 1:
                # Second QR code is blue-colored
                img = img.convert('L')  # Convert to grayscale
                img = ImageOps.colorize(img, black="blue", white="white")
                img.save(f"blue_qr_{index + 1}.png")

            elif index % 4 == 2:
                # Third QR code is rotated
                img = img.rotate(45, expand=1)
                img.save(f"rotated_qr_{index + 1}.png")

            elif index % 4 == 3:
                # Fourth QR code is animated
                frames = []
                max_size = (img.width, img.height)

                for angle in range(0, 360, 15):
                    frame = img.rotate(angle, expand=1).convert("RGBA")
                    frame_size = (max(frame.width, max_size[0]), max(frame.height, max_size[1]))
                    max_size = frame_size

                for angle in range(0, 360, 15):
                    frame = img.rotate(angle, expand=1).convert("RGBA")
                    padded_frame = Image.new('RGBA', max_size, (255, 255, 255, 0))
                    padded_frame.paste(frame, ((max_size[0] - frame.width) // 2, (max_size[1] - frame.height) // 2))
                    frames.append(padded_frame)

                imageio.mimsave(f"animated_qr_{index + 1}.gif", frames, duration=0.1)

        finally:
            # Remove the initial temporary QR code file
            if os.path.exists(temp_filename):
                os.remove(temp_filename)

# Generate custom QR codes for the list of URLs
generate_custom_qrs(urls)
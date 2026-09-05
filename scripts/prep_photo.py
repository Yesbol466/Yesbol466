import sys
import cv2
import numpy as np
from PIL import Image
from rembg import remove

def prep_photo(input_path, output_path="source-prepped.png"):
    # Load image
    print(f"Loading {input_path}...")
    with open(input_path, "rb") as f:
        input_data = f.read()

    # Remove background
    print("Removing background...")
    output_data = remove(input_data)
    img = Image.open(__import__("io").BytesIO(output_data)).convert("RGBA")

    # Composite onto white background
    white_bg = Image.new("RGBA", img.size, (255, 255, 255, 255))
    white_bg.paste(img, mask=img.split()[3])
    img_rgb = white_bg.convert("RGB")

    # Convert to numpy for OpenCV processing
    img_cv = cv2.cvtColor(np.array(img_rgb), cv2.COLOR_RGB2GRAY)

    # Apply CLAHE for contrast enhancement
    print("Enhancing contrast...")
    clahe = cv2.createCLAHE(clipLimit=3.0, tileGridSize=(8, 8))
    img_enhanced = clahe.apply(img_cv)

    # Save
    cv2.imwrite(output_path, img_enhanced)
    print(f"Saved prepped photo to {output_path}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python scripts/prep_photo.py your_photo.jpg")
        sys.exit(1)
    prep_photo(sys.argv[1])
import numpy as np
from PIL import Image, ImageDraw, ImageFont
import os


def create_block_letter_s(height: int, width: int, letter: str = "S", font_size_ratio: float = 0.9) -> np.ndarray:
    """
    Creates a block letter image matching the given dimensions.
    Parameters:
        height: height of the output image in pixels
        width: width of the output image in pixels
        letter: the letter to draw (default "S")
        font_size_ratio: how much of the image height the letter should fill (default 0.9)
    Returns:
        2D numpy array (height x width) with values in [0, 1]
        Letter is black (0.0) on white background (1.0)
    """
    img = Image.new("L", (width, height), color=255)
    draw = ImageDraw.Draw(img)

    font_size = int(height * font_size_ratio)

    font = None
    font_paths = [
        "/System/Library/Fonts/Helvetica.ttc",
        "/System/Library/Fonts/Arial Bold.ttf",
        "/Library/Fonts/Arial Bold.ttf",
        "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf",
        "/usr/share/fonts/truetype/liberation/LiberationSans-Bold.ttf",
        "/Windows/Fonts/arialbd.ttf",
        "/Windows/Fonts/Arial.ttf",
    ]

    for path in font_paths:
        if os.path.exists(path):
            try:
                font = ImageFont.truetype(path, font_size)
                break
            except Exception:
                continue

    if font is None:
        font = ImageFont.load_default()

    bbox = draw.textbbox((0, 0), letter, font=font)
    text_width = bbox[2] - bbox[0]
    text_height = bbox[3] - bbox[1]

    x = (width - text_width) // 2 - bbox[0]
    y = (height - text_height) // 2 - bbox[1]

    draw.text((x, y), letter, fill=0, font=font)

    arr = np.array(img, dtype=np.float32) / 255.0
    return arr


if __name__ == "__main__":
    result = create_block_letter_s(375, 250)
    print(f"Shape: {result.shape}")
    print(f"Min value: {result.min():.2f}, Max value: {result.max():.2f}")
    print(f"Black pixels (letter): {np.sum(result < 0.5)}")
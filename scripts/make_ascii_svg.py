import cv2
import numpy as np

RAMP = " .`:-=+*cs#%@"

def make_ascii_svg(image_path="source-prepped.png", output_path="yesbol-ascii.svg", cols=80):
    # Load grayscale image
    img = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
    if img is None:
        raise FileNotFoundError(f"Cannot load {image_path}")

    # Resize to character grid
    h, w = img.shape
    rows = int(cols * h / w * 0.55)
    img = cv2.resize(img, (cols, rows))
    

    # Map pixels to ASCII chars
    lines = []
    for r in range(rows):
        row_chars = ""
        for c in range(cols):
            brightness = img[r, c]
            idx = int(brightness / 255 * (len(RAMP) - 1))
            row_chars += RAMP[idx]
        lines.append(row_chars)

    # SVG dimensions
    char_w = 7
    char_h = 13
    svg_w = cols * char_w
    svg_h = rows * char_h

    # Animation duration per row
    row_dur = 0.04  # seconds per row
    total_dur = rows * row_dur

    svg = []
    svg.append(f'<svg xmlns="http://www.w3.org/2000/svg" '
               f'width="{svg_w}" height="{svg_h}" '
               f'style="background:#0d1117">')

    svg.append('<style>')
    svg.append('text { font-family: "Courier New", monospace; font-size: 11px; fill: #58a6ff; }')
    svg.append('</style>')

    for i, line in enumerate(lines):
        y = (i + 1) * char_h
        begin = f"{i * row_dur:.2f}s"
        escaped = (line.replace('&', '&amp;')
                       .replace('<', '&lt;')
                       .replace('>', '&gt;'))

        svg.append(f'<text x="0" y="{y}" opacity="0">')
        svg.append(escaped)
        svg.append(f'<animate attributeName="opacity" '
                   f'from="0" to="1" '
                   f'begin="{begin}" dur="0.01s" '
                   f'fill="freeze" />')
        svg.append('</text>')

    svg.append('</svg>')

    with open(output_path, 'w', encoding='utf-8') as f:
        f.write('\n'.join(svg))

    print(f"ASCII SVG saved to {output_path}")

if __name__ == "__main__":
    make_ascii_svg()
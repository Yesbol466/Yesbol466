output_path = "info-card.svg"

lines = [
    ("", ""),
    ("user", "yesbol@github"),
    ("", "---------------"),
    ("OS", "Warsaw, Poland"),
    ("Role", "Data Engineer &amp; SWE"),
    ("", ""),
    ("Now", "M.Sc. Applied CS @ PW"),
    ("Prev", "B.Sc. CS @ WUT 2026"),
    ("", ""),
    ("Stack", "Python · SQL · dbt"),
    ("", "Kubernetes · Airflow"),
    ("", "FastAPI · React"),
    ("", "Docker · PostgreSQL"),
    ("", ""),
    ("ML", "TensorFlow · OpenCV"),
    ("", "Scikit-Learn"),
    ("", ""),
    ("Work", "Lionbridge · QA"),
    ("", "Huicai · ML Intern"),
    ("", "Zerde · ML Intern"),
    ("", ""),
    ("Project", "job-market-trends"),
    ("", "1.6M rows · live"),
    ("", ""),
    ("Languages", "EN · ZH · RU · KZ · TR"),
    ("", ""),
]

char_h = 18
padding = 20
svg_w = 490
svg_h = len(lines) * char_h + padding * 2

key_color = "#58a6ff"
val_color = "#e6edf3"
sep_color = "#30363d"
bg_color = "#0d1117"

row_dur = 0.05

svg = []
svg.append(f'<svg xmlns="http://www.w3.org/2000/svg" '
           f'width="{svg_w}" height="{svg_h}" '
           f'style="background:{bg_color}">')

svg.append('<style>')
svg.append('text { font-family: "Courier New", monospace; font-size: 13px; }')
svg.append('</style>')

# Border
svg.append(f'<rect x="1" y="1" width="{svg_w-2}" height="{svg_h-2}" '
           f'rx="6" fill="none" stroke="{sep_color}" stroke-width="1"/>')

for i, (key, val) in enumerate(lines):
    y = padding + (i + 1) * char_h
    begin = f"{i * row_dur:.2f}s"

    if key == "" and val == "---------------":
        svg.append(f'<line x1="{padding}" y1="{y-5}" '
                   f'x2="{svg_w - padding}" y2="{y-5}" '
                   f'stroke="{sep_color}" stroke-width="1" opacity="0">')
        svg.append(f'<animate attributeName="opacity" '
                   f'from="0" to="1" begin="{begin}" dur="0.01s" fill="freeze"/>')
        svg.append('</line>')
        continue

    if key:
        svg.append(f'<text x="{padding}" y="{y}" '
                   f'fill="{key_color}" opacity="0">{key}'
                   f'<animate attributeName="opacity" '
                   f'from="0" to="1" begin="{begin}" dur="0.01s" fill="freeze"/>'
                   f'</text>')
        svg.append(f'<text x="160" y="{y}" '
                   f'fill="{val_color}" opacity="0">{val}'
                   f'<animate attributeName="opacity" '
                   f'from="0" to="1" begin="{begin}" dur="0.01s" fill="freeze"/>'
                   f'</text>')
    else:
        svg.append(f'<text x="160" y="{y}" '
                   f'fill="{val_color}" opacity="0">{val}'
                   f'<animate attributeName="opacity" '
                   f'from="0" to="1" begin="{begin}" dur="0.01s" fill="freeze"/>'
                   f'</text>')

svg.append('</svg>')

with open(output_path, 'w', encoding='utf-8') as f:
    f.write('\n'.join(svg))

print(f"Info card saved to {output_path}")
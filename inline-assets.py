from pathlib import Path
import base64
import mimetypes
import re

root = Path(__file__).resolve().parent
html_path = root / "Wagent-Presentacion-Comercial.html"
html = html_path.read_text()

pattern = re.compile(r'src="(assets/[^"]+)"')
seen = set()


def repl(match):
    rel = match.group(1)
    if rel in seen:
        return match.group(0)
    seen.add(rel)
    file_path = root / rel
    if not file_path.exists():
        raise FileNotFoundError(file_path)
    mime = mimetypes.guess_type(file_path.name)[0] or "application/octet-stream"
    data = base64.b64encode(file_path.read_bytes()).decode("ascii")
    return f'src="data:{mime};base64,{data}"'


html = pattern.sub(repl, html)
html_path.write_text(html)
print(f"Imágenes embebidas: {len(seen)}")

from pathlib import Path
import base64
import re

root = Path(__file__).resolve().parent
html_path = root / "Wagent-Presentacion-Comercial.html"
html = html_path.read_text()

screen_by_title = {
    "Dashboard": ["dashboard.png"],
    "Conexiones": ["connections.png"],
    "Bandeja de atención": ["inbox.png"],
    "Automatizaciones": ["automations.png"],
    "Canvas del bot": ["bot-builder.png"],
    "Difusiones": ["broadcasts.png", "broadcast-dialog.png"],
    "Plantillas locales": ["local-templates.png"],
    "Departamentos": ["departments.png"],
    "Agentes y pesos": ["agents.png"],
    "Horarios": ["schedules.png"],
    "Consumo y métricas": ["usage.png"],
    "Integraciones": ["api-keys.png"],
}

counters = {key: 0 for key in screen_by_title}
replacements = 0


def repl(match):
    global replacements
    tag = match.group(0)
    start = match.start()
    section_start = html.rfind("<section", 0, start)
    title_match = re.search(r'data-title="([^"]+)"', html[section_start:start])
    if not title_match:
        return tag
    title = title_match.group(1)
    files = screen_by_title.get(title)
    if not files:
        return tag
    index = counters[title]
    counters[title] += 1
    if index >= len(files):
        return tag

    source = root / "assets" / "screens" / files[index]
    if not source.exists():
        raise FileNotFoundError(source)
    encoded = base64.b64encode(source.read_bytes()).decode("ascii")
    new_src = f'src="data:image/png;base64,{encoded}"'
    if re.search(r'src="[^"]*"', tag):
        new_tag = re.sub(r'src="[^"]*"', new_src, tag, count=1)
    else:
        new_tag = tag.replace("<img", f'<img {new_src}', 1)
    replacements += 1
    return new_tag


html = re.sub(r"<img\b[^>]*>", repl, html)
html_path.write_text(html)
print(f"Capturas reincrustadas: {replacements}")

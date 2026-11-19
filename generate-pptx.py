#!/usr/bin/env python3
"""Genera la presentación comercial de Wagent en PowerPoint."""

from pathlib import Path
from PIL import Image
from pptx import Presentation
from pptx.dml.color import RGBColor
from pptx.enum.shapes import MSO_SHAPE
from pptx.enum.text import PP_ALIGN, MSO_ANCHOR
from pptx.util import Inches, Pt

ROOT = Path(__file__).resolve().parent
ASSETS = ROOT / "assets"
SCREENS = ASSETS / "screens"
OUT = ROOT / "Wagent-Presentacion-Comercial.pptx"

# Paleta WhatsApp / Wagent
GREEN = RGBColor(0x00, 0xA8, 0x84)
GREEN_DARK = RGBColor(0x00, 0x80, 0x69)
GREEN_BRIGHT = RGBColor(0x25, 0xD3, 0x66)
GREEN_SOFT = RGBColor(0xD9, 0xFD, 0xD3)
INK = RGBColor(0x11, 0x1B, 0x21)
MUTED = RGBColor(0x66, 0x77, 0x81)
BG = RGBColor(0xF0, 0xF2, 0xF5)
WHITE = RGBColor(0xFF, 0xFF, 0xFF)
LINE = RGBColor(0xE9, 0xED, 0xEF)
DARK = RGBColor(0x0B, 0x14, 0x1A)
DARK_2 = RGBColor(0x11, 0x1B, 0x21)
DARK_3 = RGBColor(0x20, 0x2C, 0x33)
META = RGBColor(0x18, 0x77, 0xF2)
META_SOFT = RGBColor(0xE7, 0xF0, 0xFE)
AMBER = RGBColor(0xF5, 0x9E, 0x0B)
AMBER_SOFT = RGBColor(0xFE, 0xF3, 0xC7)
RED = RGBColor(0xEF, 0x44, 0x44)
RED_SOFT = RGBColor(0xFE, 0xE2, 0xE2)
BLUE = RGBColor(0x3B, 0x82, 0xF6)
BLUE_SOFT = RGBColor(0xDB, 0xEA, 0xFE)
VIOLET = RGBColor(0x8B, 0x5C, 0xF6)
VIOLET_SOFT = RGBColor(0xED, 0xE9, 0xFE)
SOFT_GREEN = RGBColor(0xEA, 0xFA, 0xF4)

FONT = "Arial"

prs = Presentation()
prs.slide_width = Inches(13.333)
prs.slide_height = Inches(7.5)

SW = 13.333
SH = 7.5
M = 0.55


def rgb_hex(value):
    return RGBColor.from_string(value)


def set_bg(slide, color):
    fill = slide.background.fill
    fill.solid()
    fill.fore_color.rgb = color


def add_text(
    slide,
    x,
    y,
    w,
    h,
    text,
    size=12,
    bold=False,
    color=INK,
    align=PP_ALIGN.LEFT,
    anchor=MSO_ANCHOR.TOP,
    font=FONT,
    line_spacing=1.05,
    space_after=0,
):
    box = slide.shapes.add_textbox(Inches(x), Inches(y), Inches(w), Inches(h))
    tf = box.text_frame
    tf.clear()
    tf.word_wrap = True
    tf.margin_left = 0
    tf.margin_right = 0
    tf.margin_top = 0
    tf.margin_bottom = 0
    tf.vertical_anchor = anchor
    lines = str(text).split("\n")
    for i, line in enumerate(lines):
        p = tf.paragraphs[0] if i == 0 else tf.add_paragraph()
        p.alignment = align
        p.line_spacing = line_spacing
        p.space_after = Pt(space_after)
        run = p.add_run()
        run.text = line
        run.font.name = font
        run.font.size = Pt(size)
        run.font.bold = bold
        run.font.color.rgb = color
    return box


def add_rect(slide, x, y, w, h, fill, line=None, radius=True, line_width=0.75):
    shape = slide.shapes.add_shape(
        MSO_SHAPE.ROUNDED_RECTANGLE if radius else MSO_SHAPE.RECTANGLE,
        Inches(x),
        Inches(y),
        Inches(w),
        Inches(h),
    )
    shape.fill.solid()
    shape.fill.fore_color.rgb = fill
    if line is None:
        shape.line.fill.background()
    else:
        shape.line.color.rgb = line
        shape.line.width = Pt(line_width)
    if radius:
        shape.adjustments[0] = 0.08
    return shape


def add_pill(slide, x, y, w, text, fill=GREEN_SOFT, color=GREEN_DARK, size=8.5):
    add_rect(slide, x, y, w, 0.24, fill, None, True)
    add_text(slide, x + 0.09, y + 0.045, w - 0.18, 0.15, text, size=size, bold=True, color=color)
    return w


def add_footer(slide, page, dark=False):
    color = RGBColor(0x7F, 0xA7, 0x9A) if dark else RGBColor(0x8A, 0x97, 0x9E)
    line_color = RGBColor(0x2A, 0x4A, 0x40) if dark else LINE
    add_text(slide, M, 7.10, 2.0, 0.20, "BPONET SAS", size=8, color=color)
    add_rect(slide, M + 1.15, 7.185, 7.9, 0.01, line_color, None, False)
    add_text(slide, 10.7, 7.10, 2.1, 0.20, f"Wagent · Presentación comercial · {page:02d}", size=8, color=color, align=PP_ALIGN.RIGHT)


def add_title(slide, kicker, title, subtitle, page, dark=False, kicker_color=GREEN_DARK, kicker_bg=RGBColor(0xE7, 0xF8, 0xF1)):
    box_w = max(1.75, 0.086 * len(kicker) + 0.34)
    add_rect(slide, M, 0.42, box_w, 0.24, kicker_bg, None, True)
    add_text(slide, M + 0.10, 0.465, box_w - 0.20, 0.16, kicker.upper(), size=7.8, bold=True, color=kicker_color)
    add_text(slide, M, 0.78, 11.6, 0.58, title, size=25, bold=True, color=WHITE if dark else INK, line_spacing=0.98)
    add_text(slide, M, 1.36, 11.2, 0.42, subtitle, size=10.5, color=RGBColor(0xB8, 0xD7, 0xCC) if dark else MUTED, line_spacing=1.15)
    add_text(slide, 11.9, 0.48, 0.9, 0.20, f"{page:02d} / 37", size=8.5, bold=True, color=RGBColor(0x7F, 0xA7, 0x9A) if dark else RGBColor(0x9A, 0xA8, 0xAF), align=PP_ALIGN.RIGHT)


def add_card(slide, x, y, w, h, title, body, fill=WHITE, line=LINE, title_color=INK, body_color=MUTED, title_size=11.5, body_size=9.5, icon=None):
    add_rect(slide, x, y, w, h, fill, line, True)
    top = y + 0.16
    if icon:
        add_text(slide, x + 0.18, top, 0.35, 0.35, icon, size=16, color=GREEN_DARK)
        top += 0.34
    add_text(slide, x + 0.18, top, w - 0.36, 0.28, title, size=title_size, bold=True, color=title_color)
    if body:
        add_text(slide, x + 0.18, top + 0.30, w - 0.36, h - (top - y) - 0.38, body, size=body_size, color=body_color, line_spacing=1.12)


def add_bullet_card(slide, x, y, w, h, title, bullets, fill=WHITE, line=LINE, title_color=INK, bullet_color=MUTED, title_size=11.5, body_size=9.2):
    body = "\n".join(f"•  {b}" for b in bullets)
    add_card(slide, x, y, w, h, title, body, fill, line, title_color, bullet_color, title_size, body_size)


def add_browser(slide, image_path, x, y, w, h, url):
    add_rect(slide, x, y, w, h, WHITE, RGBColor(0xDF, 0xE5, 0xE8), True)
    add_rect(slide, x, y, w, 0.20, RGBColor(0xEE, 0xF2, 0xF4), None, True)
    for i, c in enumerate([RGBColor(0xFC, 0xA5, 0xA5), RGBColor(0xFC, 0xD3, 0x4D), RGBColor(0x86, 0xEF, 0xAC)]):
        dot = slide.shapes.add_shape(MSO_SHAPE.OVAL, Inches(x + 0.11 + i * 0.12), Inches(y + 0.075), Inches(0.055), Inches(0.055))
        dot.fill.solid()
        dot.fill.fore_color.rgb = c
        dot.line.fill.background()
    add_rect(slide, x + 0.48, y + 0.045, w - 0.60, 0.11, WHITE, RGBColor(0xE2, 0xE8, 0xEC), True)
    add_text(slide, x + 0.54, y + 0.055, w - 0.70, 0.08, url, size=5.6, color=RGBColor(0x8A, 0x97, 0x9E))

    img = Image.open(image_path)
    ar = img.width / img.height
    max_w = w - 0.04
    max_h = h - 0.24
    if max_w / max_h > ar:
        ph = max_h
        pw = ph * ar
    else:
        pw = max_w
        ph = pw / ar
    left = x + (w - pw) / 2
    top = y + 0.22 + (max_h - ph) / 2
    slide.shapes.add_picture(str(image_path), Inches(left), Inches(top), Inches(pw), Inches(ph))


def add_dark_callout(slide, x, y, w, h, text, size=9.5):
    add_rect(slide, x, y, w, h, DARK, None, True)
    add_text(slide, x + 0.18, y + 0.13, w - 0.36, h - 0.26, text, size=size, color=RGBColor(0xB8, 0xD7, 0xCC), line_spacing=1.15)


def add_table(slide, x, y, w, h, headers, rows, col_widths=None, font_size=8.2):
    table_shape = slide.shapes.add_table(len(rows) + 1, len(headers), Inches(x), Inches(y), Inches(w), Inches(h))
    table = table_shape.table
    if col_widths:
        for i, cw in enumerate(col_widths):
            table.columns[i].width = Inches(cw)
    for c, header in enumerate(headers):
        cell = table.cell(0, c)
        cell.fill.solid()
        cell.fill.fore_color.rgb = RGBColor(0xF3, 0xF6, 0xF7)
        cell.margin_left = Inches(0.04)
        cell.margin_right = Inches(0.04)
        cell.margin_top = Inches(0.02)
        cell.margin_bottom = Inches(0.02)
        tf = cell.text_frame
        tf.clear()
        p = tf.paragraphs[0]
        r = p.add_run()
        r.text = header
        r.font.name = FONT
        r.font.size = Pt(font_size - 0.5)
        r.font.bold = True
        r.font.color.rgb = RGBColor(0x81, 0x90, 0x97)
    for r_idx, row in enumerate(rows, start=1):
        for c_idx, value in enumerate(row):
            cell = table.cell(r_idx, c_idx)
            cell.fill.solid()
            cell.fill.fore_color.rgb = WHITE
            cell.margin_left = Inches(0.04)
            cell.margin_right = Inches(0.04)
            cell.margin_top = Inches(0.02)
            cell.margin_bottom = Inches(0.02)
            tf = cell.text_frame
            tf.word_wrap = True
            tf.clear()
            p = tf.paragraphs[0]
            r = p.add_run()
            r.text = value
            r.font.name = FONT
            r.font.size = Pt(font_size)
            r.font.color.rgb = MUTED if c_idx else INK
            r.font.bold = c_idx == 0
    return table


def new_slide(bg=BG):
    slide = prs.slides.add_slide(prs.slide_layouts[6])
    set_bg(slide, bg)
    return slide


# ---------------------------------------------------------------- 01 PORTADA
slide = new_slide(DARK)
# Glow decorativo
for (x, y, w, h) in [(8.6, -1.2, 6.4, 6.4), (-1.6, 4.6, 5.6, 5.6)]:
    glow = slide.shapes.add_shape(MSO_SHAPE.OVAL, Inches(x), Inches(y), Inches(w), Inches(h))
    glow.fill.solid()
    glow.fill.fore_color.rgb = RGBColor(0x0E, 0x3B, 0x30)
    glow.line.fill.background()

slide.shapes.add_picture(str(ASSETS / "logo-bponet-white.png"), Inches(M), Inches(0.45), height=Inches(0.55))
slide.shapes.add_picture(str(ASSETS / "meta-app-icon.png"), Inches(10.55), Inches(0.42), Inches(0.92), Inches(0.92))
add_text(slide, 11.62, 0.52, 1.5, 0.30, "Wagent", size=18, bold=True, color=WHITE)
add_text(slide, 11.63, 0.83, 1.4, 0.18, "WHATSAPP BUSINESS PLATFORM", size=5.8, bold=True, color=RGBColor(0x7F, 0xA7, 0x9A))

add_pill(slide, M, 1.95, 2.1, "PRESENTACIÓN COMERCIAL · 2026", RGBColor(0x0E, 0x3B, 0x30), RGBColor(0x8F, 0xF2, 0xC8), 7.8)
add_text(slide, M, 2.28, 11.0, 0.78, "Todo tu WhatsApp", size=42, bold=True, color=WHITE, line_spacing=0.95)
add_text(slide, M, 3.00, 11.0, 0.78, "en una sola plataforma.", size=42, bold=True, color=GREEN_BRIGHT, line_spacing=0.95)
add_text(slide, M, 3.78, 8.9, 0.85, "Conecta números con la API oficial, atiende desde una bandeja colaborativa,\nautomatiza conversaciones y mide cada interacción. Sin cambiar de herramienta.", size=12.5, color=RGBColor(0xC8, 0xE3, 0xDA), line_spacing=1.25)

chips = ["Cloud API", "Embedded Signup", "Coexistencia", "Multiempresa", "Automatización"]
cx = M
for chip in chips:
    cw = 0.95 if len(chip) < 13 else 1.25
    add_rect(slide, cx, 5.35, cw, 0.24, RGBColor(0x10, 0x2B, 0x24), RGBColor(0x2A, 0x5A, 0x4B), True)
    add_text(slide, cx + 0.08, 5.40, cw - 0.16, 0.14, chip, size=6.8, bold=True, color=RGBColor(0xC7, 0xE5, 0xDB))
    cx += cw + 0.10

add_text(slide, M, 6.52, 5.0, 0.55, "BPO NET S.A.S. · NIT 901.620.548-2\nPalmira, Valle del Cauca · Colombia\nwagent.bponet.com.co", size=8.2, color=RGBColor(0x7F, 0xA7, 0x9A), line_spacing=1.3)

# ---------------------------------------------------------------- 02 AGENDA
slide = new_slide()
add_title(slide, "Agenda", "Dos recorridos, una sola plataforma", "Primero cómo conectar tu WhatsApp con BPONET. Después, todo lo que Wagent permite operar.", 2)
add_bullet_card(slide, M, 1.95, 5.9, 4.75, "01 · Conectar con BPONET", [
    "Tres caminos de conexión.",
    "Qué necesita cada camino.",
    "QR / WhatsApp Web.",
    "API manual.",
    "Embedded Signup + coexistencia.",
    "Quién gestiona qué.",
], SOFT_GREEN, RGBColor(0xC9, 0xF0, 0xE2), INK, MUTED, 13, 9.6)
add_bullet_card(slide, 6.85, 1.95, 5.9, 4.75, "02 · La plataforma", [
    "Conexiones multinúmero y multicanal.",
    "Bandeja compartida y atención en tiempo real.",
    "Automatización visual y bots por código.",
    "Campañas con plantillas y opt-in.",
    "Equipos, horarios, métricas y consumo.",
    "Cuotas y límites según el acuerdo.",
    "Integraciones, seguridad y cumplimiento.",
], WHITE, LINE, INK, MUTED, 13, 9.6)
add_footer(slide, 2)

# ---------------------------------------------------------------- 03 DIVIDER CONEXIÓN
slide = new_slide(DARK)
slide.shapes.add_picture(str(ASSETS / "logo-bponet-white.png"), Inches(M), Inches(0.45), height=Inches(0.55))
add_rect(slide, 9.95, 2.05, 1.85, 1.85, WHITE, None, True)
slide.shapes.add_picture(str(ASSETS / "meta-app-icon.png"), Inches(10.05), Inches(2.15), Inches(1.65), Inches(1.65))
add_text(slide, 11.3, 0.48, 1.5, 0.20, "PARTE 01", size=8, bold=True, color=RGBColor(0x74, 0xA9, 0x9A), align=PP_ALIGN.RIGHT)
add_pill(slide, M, 2.15, 2.55, "BPONET · TECH PROVIDER DE META", RGBColor(0x0E, 0x3B, 0x30), RGBColor(0x8F, 0xF2, 0xC8), 7.0)
add_text(slide, M, 2.50, 8.6, 0.74, "Conectar WhatsApp", size=44, bold=True, color=WHITE, line_spacing=0.95)
add_text(slide, M, 3.26, 8.8, 0.74, "sin gestionar Meta.", size=44, bold=True, color=GREEN_BRIGHT, line_spacing=0.95)
add_text(slide, M, 4.15, 8.2, 0.72, "BPONET ya tiene la app, la aprobación y la infraestructura. Tú solo autorizas tu cuenta y tu número.", size=13, color=RGBColor(0xB8, 0xD7, 0xCC), line_spacing=1.3)
add_footer(slide, 3, dark=True)

# ---------------------------------------------------------------- 04 TRES CAMINOS
slide = new_slide()
add_title(slide, "Conexión", "Tres caminos para conectar WhatsApp", "Cada camino tiene requisitos y responsables distintos. Elige según tu operación, tu WABA y tu equipo técnico.", 4)
add_bullet_card(slide, M, 1.95, 3.95, 2.95, "QR / WhatsApp Web", [
    "La forma más rápida de empezar.",
    "No requiere app de Meta ni WABA.",
    "Necesita: teléfono con WhatsApp o WhatsApp Business y escanear el QR.",
    "Ideal para pilotos y equipos pequeños.",
], AMBER_SOFT, RGBColor(0xF6, 0xD5, 0x8A), INK, MUTED, 11.2, 8.6)
add_bullet_card(slide, 4.65, 1.95, 3.95, 2.95, "API manual", [
    "Conexión oficial con WABA propia.",
    "Necesita: WABA, número en Cloud API, token, Phone Number ID y WABA ID.",
    "El cliente gestiona su app de Meta y webhooks.",
    "Ideal para empresas con WABA y equipo técnico.",
], WHITE, LINE, INK, MUTED, 11.2, 8.6)
add_bullet_card(slide, 8.75, 1.95, 3.95, 2.95, "Embedded + coexistencia", [
    "La vía recomendada.",
    "BPONET gestiona Meta y tú conservas la app Business.",
    "Necesita: cuenta Meta, app 2.24.17+ y número elegible.",
    "Ideal para API oficial sin gestionar la app de Meta.",
], SOFT_GREEN, RGBColor(0xC9, 0xF0, 0xE2), INK, MUTED, 11.2, 8.6)
add_dark_callout(slide, M, 5.12, 12.15, 0.85, "Regla simple: si no tienes WABA ni equipo técnico, usa Embedded + coexistencia. Si no necesitas API oficial, usa QR. Si ya tienes WABA y token, usa API manual.", 9.0)
add_footer(slide, 4)

# ---------------------------------------------------------------- 05 REQUISITOS POR CAMINO
slide = new_slide()
add_title(slide, "Comparación", "Qué necesita el cliente en cada camino", "Antes de elegir, revisa los requisitos y quién gestiona cada pieza.", 5)
headers = ["Requisito", "QR / WhatsApp Web", "API manual", "Embedded + coexistencia"]
rows = [
    ("Cuenta de Meta", "No", "Sí, para tu WABA", "Sí; puede crearse en el flujo"),
    ("WABA", "No", "Propio", "Se crea o convierte"),
    ("Número", "WhatsApp o Business", "Registrado en Cloud API", "Business 2.24.17+ elegible"),
    ("Token", "No", "System user token", "BPONET lo intercambia"),
    ("App de Meta / App Review", "No", "El cliente los gestiona", "BPONET los gestiona"),
    ("Webhooks", "No", "El cliente los configura", "BPONET los configura"),
    ("Plantillas oficiales", "No", "Sí", "Sí"),
    ("Ideal para", "Pilotos y equipos pequeños", "Empresas con WABA propio", "Coexistencia y onboarding simple"),
]
add_table(slide, M, 1.95, 12.2, 4.45, headers, rows, [3.2, 2.7, 3.2, 3.1], 7.7)
add_text(slide, M, 6.50, 12.2, 0.35, "Los requisitos de QR son mínimos; los de API manual recaen en el cliente; en Embedded/coexistencia BPONET asume la parte técnica de Meta.", size=8.2, color=MUTED)
add_footer(slide, 5)

# ---------------------------------------------------------------- 06 WABA
slide = new_slide()
add_title(slide, "Conceptos clave", "Qué es el WABA (solo API y Embedded)", "El WABA agrupa números, plantillas, webhooks y facturación. QR no usa WABA ni Graph API.", 6)
items = [
    ("WABA ID", "Identifica la cuenta de mensajería. En API manual lo aporta el cliente; en Embedded lo gestiona BPONET.", SOFT_GREEN),
    ("Phone Number ID", "Identifica cada número. Se usa para enviar mensajes y resolver webhooks.", WHITE),
    ("Token", "Credencial para Graph API. En API manual lo genera el cliente; en Embedded lo intercambia BPONET.", WHITE),
    ("Webhook", "En API manual lo configura el cliente; en Embedded lo configura y opera BPONET.", WHITE),
]
for i, (title, body, fill) in enumerate(items):
    add_card(slide, M + i * 3.10, 1.95, 2.85, 2.20, title, body, fill, RGBColor(0xC9, 0xF0, 0xE2) if i == 0 else LINE, INK, MUTED, 11.0, 8.4)
add_dark_callout(slide, M, 4.40, 12.15, 0.80, "QR no usa WABA. Si el cliente elige QR, no hay WABA, token, webhooks ni plantillas oficiales. Para eso debe migrar a API manual o Embedded.", 9.0)
add_text(slide, M, 5.45, 12.15, 0.50, "En Embedded/coexistencia, BPONET crea o convierte el WABA y deja la conexión lista; el cliente solo autoriza su cuenta y su número.", size=9.2, color=MUTED)
add_footer(slide, 6)

# ---------------------------------------------------------------- 07 QR
slide = new_slide()
add_title(slide, "Camino 1", "QR / WhatsApp Web", "La forma más rápida de empezar, sin app de Meta, sin WABA y sin App Review.", 7)
add_bullet_card(slide, M, 1.95, 5.95, 2.75, "Qué necesita el cliente", [
    "Un teléfono con WhatsApp o WhatsApp Business.",
    "Escanear el código QR desde Wagent.",
    "Mantener el teléfono conectado y con internet.",
    "No eliminar la sesión de WhatsApp Web.",
], AMBER_SOFT, RGBColor(0xF6, 0xD5, 0x8A), INK, MUTED, 11.0, 8.8)
add_bullet_card(slide, 6.75, 1.95, 5.95, 2.75, "Qué obtiene y qué límites tiene", [
    "Bandeja, bots, difusiones con texto libre y plantillas locales.",
    "Sin webhooks oficiales ni plantillas de Meta.",
    "Depende del teléfono y de la sesión abierta.",
    "Mayor riesgo operativo para volúmenes altos.",
], WHITE, LINE, INK, MUTED, 11.0, 8.8)
for i, step in enumerate(["Nueva conexión", "Tipo QR", "Escanear código", "Conectar"]):
    add_card(slide, M + i * 3.10, 4.95, 2.85, 0.85, f"Paso {i+1}", step, WHITE, LINE, INK, MUTED, 8.4, 7.8)
add_dark_callout(slide, M, 6.05, 12.15, 0.55, "No usa Cloud API. Si necesitas plantillas oficiales, webhooks, coexistencia o escala, elige API manual o Embedded.", 8.8)
add_footer(slide, 7)

# ---------------------------------------------------------------- 08 API MANUAL
slide = new_slide()
add_title(slide, "Camino 2", "Conexión por API manual", "Para empresas que ya tienen su propia WABA, número registrado y token de Meta.", 8)
add_bullet_card(slide, M, 1.95, 5.95, 3.15, "Qué necesita el cliente", [
    "WABA propia y número registrado en Cloud API.",
    "System user token con whatsapp_business_management y whatsapp_business_messaging.",
    "Phone Number ID y WABA ID.",
    "Gestionar su app de Meta, App Review y webhooks.",
], WHITE, LINE, INK, MUTED, 11.0, 8.8)
add_bullet_card(slide, 6.75, 1.95, 5.95, 3.15, "Qué hace Wagent", [
    "Conexión por API Token + Phone Number ID + WABA ID.",
    "Bandeja compartida, automatización y campañas.",
    "Plantillas oficiales, métricas e integraciones.",
    "Soporte de la plataforma; la gestión de Meta es del cliente.",
], SOFT_GREEN, RGBColor(0xC9, 0xF0, 0xE2), INK, MUTED, 11.0, 8.8)
add_dark_callout(slide, M, 5.35, 12.15, 0.75, "Si no tienes WABA ni token, no uses este camino. Usa Embedded Signup con coexistencia: BPONET gestiona Meta por ti.", 9.0)
add_footer(slide, 8)

# ---------------------------------------------------------------- 09 EMBEDDED
slide = new_slide()
add_title(slide, "Camino 3", "Embedded Signup + coexistencia", "La vía recomendada: BPONET gestiona Meta y tú conservas tu app WhatsApp Business.", 9)
add_bullet_card(slide, M, 1.95, 5.95, 2.35, "Qué necesita el cliente", [
    "Cuenta de Meta o Business Portfolio (puede crearse en el flujo).",
    "WhatsApp Business app 2.24.17 o superior.",
    "Número activo y elegible para coexistencia.",
    "Aceptar compartir el historial y mantener la app abierta.",
], SOFT_GREEN, RGBColor(0xC9, 0xF0, 0xE2), INK, MUTED, 11.0, 8.6)
add_bullet_card(slide, 6.75, 1.95, 5.95, 2.35, "Qué hace BPONET", [
    "App de Meta, configuración de Embedded Signup y App Review.",
    "Webhooks, tokens, suscripción al WABA y sincronización.",
    "Contactos, historial, echoes y account_update.",
    "Soporte técnico de la conexión.",
], WHITE, LINE, INK, MUTED, 11.0, 8.6)
steps = ["Entra a Wagent", "Conectar con Meta", "Autoriza cuenta", "Elige número", "Confirma código", "Sincroniza historial"]
for i, step in enumerate(steps):
    col = i % 3
    row = i // 3
    add_card(slide, M + col * 4.05, 4.55 + row * 0.95, 3.85, 0.78, f"Paso {i+1}", step, WHITE, LINE, INK, MUTED, 8.2, 7.6)
add_text(slide, M, 6.55, 12.15, 0.30, "No necesitas crear app, App Review, webhooks ni tokens. BPONET ya lo tiene resuelto.", size=8.8, bold=True, color=GREEN_DARK)
add_footer(slide, 9)

# ---------------------------------------------------------------- 10 COEXISTENCIA
slide = new_slide()
add_title(slide, "Camino 3b", "Coexistencia en detalle", "Solo aplica al camino Embedded: tú sigues usando la app WhatsApp Business y la API opera en paralelo.", 10)
add_bullet_card(slide, M, 1.95, 5.95, 3.05, "Qué se sincroniza", [
    "Contactos: smb_app_state_sync.",
    "Historial: history, hasta 180 días.",
    "Echo: smb_message_echoes.",
    "Ciclo de vida: account_update.",
    "No soportado: grupos, efímeros, view once, listas, llamadas.",
], WHITE, LINE, INK, MUTED, 11.0, 8.7)
add_bullet_card(slide, 6.75, 1.95, 5.95, 3.05, "Qué cambia para ti", [
    "Sigues respondiendo desde la app WhatsApp Business.",
    "Tus agentes también responden desde Wagent.",
    "Los mensajes de la app se reflejan en la bandeja.",
    "La sincronización debe iniciar dentro de las 24 h.",
    "BPONET procesa webhooks e historial.",
], SOFT_GREEN, RGBColor(0xC9, 0xF0, 0xE2), INK, MUTED, 11.0, 8.7)
add_dark_callout(slide, M, 5.30, 12.15, 0.75, "Ventana crítica: si la sincronización no se inicia en 24 h, el cliente debe offboardear y repetir el flujo. BPONET acompaña el proceso.", 9.0)
add_footer(slide, 10)

# ---------------------------------------------------------------- 11 WEBHOOKS
slide = new_slide()
add_title(slide, "Detrás de escena", "Webhooks y sincronización", "Aplica a API manual y Embedded. QR no usa webhooks. En Embedded, BPONET lo configura y opera por ti.", 11)
headers = ["Evento", "Qué entrega Meta", "Qué ves en Wagent"]
rows = [
    ("messages", "Mensajes y estados.", "Bandeja, bots y métricas."),
    ("history", "Historial en fases y chunks.", "Conversaciones anteriores."),
    ("smb_app_state_sync", "Contactos de la app Business.", "Contactos actualizados."),
    ("smb_message_echoes", "Mensajes enviados desde la app.", "Espejo en la bandeja."),
    ("account_update", "Offboarding / reconexión.", "Estado de la conexión."),
]
add_table(slide, M, 1.95, 12.2, 3.15, headers, rows, [3.5, 4.6, 4.1], 8.2)
add_bullet_card(slide, M, 5.30, 5.95, 0.95, "API manual", ["El cliente configura y mantiene sus webhooks."], SOFT_GREEN, RGBColor(0xC9, 0xF0, 0xE2), INK, MUTED, 9.5, 8.2)
add_bullet_card(slide, 6.75, 5.30, 5.95, 0.95, "Embedded", ["BPONET configura, verifica y procesa los webhooks."], WHITE, LINE, INK, MUTED, 9.5, 8.2)
add_text(slide, M, 6.45, 12.15, 0.30, "Cola BullMQ, verificación de token y procesamiento idempotente para no duplicar mensajes.", size=8.2, color=MUTED)
add_footer(slide, 11)

# ---------------------------------------------------------------- 12 QUIÉN GESTIONA QUÉ
slide = new_slide()
add_title(slide, "Responsabilidades", "Quién gestiona qué en cada camino", "La responsabilidad técnica cambia según el camino. BPONET siempre acompaña y da soporte.", 12)
headers = ["Actividad", "QR / WhatsApp Web", "API manual", "Embedded + coexistencia"]
rows = [
    ("App de Meta", "No aplica", "Cliente", "BPONET"),
    ("WABA", "No aplica", "Cliente", "BPONET lo crea o convierte"),
    ("Token", "No aplica", "Cliente", "BPONET lo intercambia y cifra"),
    ("App Review", "No aplica", "Cliente, si onboardea", "BPONET"),
    ("Webhooks", "No aplica", "Cliente", "BPONET"),
    ("Número", "WhatsApp o Business", "Registrado por el cliente", "Business elegible; BPONET conecta"),
    ("Sincronización", "No aplica", "Cliente + Wagent", "BPONET"),
    ("Soporte", "BPONET", "BPONET + cliente (Meta)", "BPONET"),
]
add_table(slide, M, 1.95, 12.2, 4.25, headers, rows, [3.1, 2.8, 3.2, 3.1], 7.6)
add_dark_callout(slide, M, 6.35, 12.15, 0.55, "En Embedded/coexistencia, el cliente solo autoriza. En API manual, el cliente es dueño de su app, WABA, token y webhooks. En QR no hay app de Meta.", 8.6)
add_footer(slide, 12)

# ---------------------------------------------------------------- 13 QUÉ CAMINO ELEGIR
slide = new_slide()
add_title(slide, "Decisión", "¿Qué camino elegir?", "Tres preguntas para decidir en menos de un minuto.", 13)
add_bullet_card(slide, M, 1.95, 5.95, 3.15, "Elige por situación", [
    "No tengo WABA ni equipo técnico → Embedded + coexistencia.",
    "Ya tengo WABA, número y token → API manual.",
    "Solo quiero probar rápido → QR.",
], SOFT_GREEN, RGBColor(0xC9, 0xF0, 0xE2), INK, MUTED, 11.0, 9.0)
add_bullet_card(slide, 6.75, 1.95, 5.95, 3.15, "Preguntas rápidas", [
    "¿QR usa WABA? No.",
    "¿API manual requiere App Review? Depende de tu app; si onboardeas clientes, sí.",
    "¿Embedded requiere App Review? No, BPONET ya lo tiene.",
    "¿Puedo migrar de QR a API? Sí, con una nueva conexión.",
    "¿Coexistencia con cualquier número? No, debe ser elegible.",
], WHITE, LINE, INK, MUTED, 11.0, 8.4)
add_dark_callout(slide, M, 5.35, 12.15, 0.72, "Checklist: cuenta de Meta (API/Embedded) · número (WhatsApp, Cloud API o Business elegible) · token/WABA (API manual) · app actualizada · aceptar historial (coexistencia).", 8.8)
add_footer(slide, 13)

# ---------------------------------------------------------------- 14 DIVIDER APP
slide = new_slide(DARK)
slide.shapes.add_picture(str(ASSETS / "logo-bponet-white.png"), Inches(M), Inches(0.45), height=Inches(0.55))
add_text(slide, 11.3, 0.48, 1.5, 0.20, "PARTE 02", size=8, bold=True, color=RGBColor(0x74, 0xA9, 0x9A), align=PP_ALIGN.RIGHT)
add_pill(slide, M, 2.15, 1.8, "LA PLATAFORMA", RGBColor(0x0E, 0x3B, 0x30), RGBColor(0x8F, 0xF2, 0xC8), 7.2)
add_text(slide, M, 2.50, 11.0, 0.82, "Wagent,", size=48, bold=True, color=WHITE, line_spacing=0.95)
add_text(slide, M, 3.32, 11.2, 0.82, "todo el ciclo de WhatsApp.", size=44, bold=True, color=GREEN_BRIGHT, line_spacing=0.95)
add_text(slide, M, 4.25, 8.9, 0.65, "Conectar, atender, automatizar, medir y cumplir. Una plataforma multiempresa construida sobre la API oficial.", size=13, color=RGBColor(0xB8, 0xD7, 0xCC), line_spacing=1.3)
add_footer(slide, 14, dark=True)

# ---------------------------------------------------------------- 15 WHAT IS WAGENT
slide = new_slide()
add_title(slide, "Producto", "Qué es Wagent", "Una plataforma multiempresa para conectar WhatsApp, atender con equipos, automatizar conversaciones y medir resultados.", 15)
cards = [
    ("Conexiones", "QR, API manual, Embedded Signup y coexistencia. Varios números por empresa."),
    ("Bandeja", "Conversaciones compartidas, asignación, prioridades, media y tiempo real."),
    ("Automatización", "Constructor visual, bots por código, APIs, bases de datos y plantillas."),
    ("Campañas", "Difusiones con plantillas aprobadas, opt-in, variables y logs de entrega."),
]
for i, (title, body) in enumerate(cards):
    add_card(slide, M + i * 3.05, 1.95, 2.85, 1.75, title, body, SOFT_GREEN if i in (0, 3) else WHITE, RGBColor(0xC9, 0xF0, 0xE2) if i in (0, 3) else LINE, INK, MUTED, 11.2, 8.8)
add_bullet_card(slide, M, 4.05, 5.9, 2.05, "Lo que la hace diferente", [
    "Multiempresa real: datos y políticas aisladas por tenant.",
    "Coexistencia: app Business y API en el mismo número.",
    "No-code + código: flujos visuales o scripts avanzados.",
    "Integraciones: CRM, ERP, bases de datos y APIs externas.",
], WHITE, LINE, INK, MUTED, 11.2, 8.8)
add_dark_callout(slide, 6.85, 4.05, 5.9, 2.05, "“No es un chat más. Es la capa operativa de WhatsApp para tu empresa.”", 13)
add_footer(slide, 15)

# ---------------------------------------------------------------- 16 ARCHITECTURE
slide = new_slide()
add_title(slide, "Arquitectura", "Diseñada para operar, no solo para demostrar", "Frontend Angular, API NestJS, auth independiente, PostgreSQL, MongoDB, Redis y colas. Todo aislado por empresa.", 16)
flow = ["Web Angular", "API NestJS", "PostgreSQL", "MongoDB", "Redis / BullMQ", "Meta Cloud API"]
x = 0.72
for i, text in enumerate(flow):
    w = 1.55 if i != 5 else 1.65
    add_rect(slide, x, 1.90, w, 0.34, SOFT_GREEN if i == 0 else META_SOFT if i == 5 else WHITE, RGBColor(0xC9, 0xF0, 0xE2) if i == 0 else RGBColor(0xD7, 0xE6, 0xFF) if i == 5 else LINE, True)
    add_text(slide, x + 0.07, 1.97, w - 0.14, 0.18, text, size=7.0, bold=True, color=GREEN_DARK if i == 0 else META if i == 5 else INK)
    if i < len(flow) - 1:
        add_text(slide, x + w + 0.04, 1.97, 0.18, 0.18, "→", size=9, bold=True, color=RGBColor(0x9F, 0xB0, 0xB6))
    x += w + 0.20
cards = [
    ("Multi-tenant", "Contexto de empresa en cada request, políticas por tenant y aislamiento de datos y credenciales."),
    ("Tiempo real", "WebSockets para mensajes, estados de sesión, QR y tickets. La UI se actualiza sin recargar."),
    ("Asíncrono", "Colas para mensajes entrantes, bots, difusiones e historial. Respuestas rápidas a Meta."),
    ("Auth separada", "Servicio independiente, JWT, roles, permisos y revalidación de sesión."),
    ("Seguridad", "Tokens cifrados con AES-256-GCM, HTTPS, guards por rol y auditoría."),
    ("Extensible", "Módulos de WhatsApp, tickets, chatbot, difusiones, contactos y reportes."),
]
for i, (title, body) in enumerate(cards):
    col = i % 3
    row = i // 3
    add_card(slide, M + col * 4.05, 2.55 + row * 1.85, 3.85, 1.65, title, body, WHITE, LINE, INK, MUTED, 10.5, 8.4)
add_footer(slide, 16)

# ---------------------------------------------------------------- 17 DASHBOARD
slide = new_slide()
add_title(slide, "Vista 01", "Panel de control", "La operación completa en una pantalla: tickets, chats, mensajes, tiempos de respuesta, agentes y sesiones.", 17)
add_browser(slide, SCREENS / "dashboard.png", M, 1.95, 7.55, 4.75, "wagent.bponet.com.co/pages/dashboard")
add_bullet_card(slide, 8.35, 1.95, 4.40, 1.35, "Decisiones con datos", ["KPIs, tendencia de volumen y distribución por estado, prioridad, departamento y tipo."], SOFT_GREEN, RGBColor(0xC9, 0xF0, 0xE2), INK, MUTED, 10.2, 8.2)
add_bullet_card(slide, 8.35, 3.45, 4.40, 1.35, "Equipo y capacidad", ["Agentes disponibles, carga, resueltos y tiempos de primera respuesta y resolución."], WHITE, LINE, INK, MUTED, 10.2, 8.2)
add_bullet_card(slide, 8.35, 4.95, 4.40, 1.35, "Sesiones y campañas", ["Estado de conexiones y desempeño de difusiones, sin salir del panel."], WHITE, LINE, INK, MUTED, 10.2, 8.2)
add_footer(slide, 17)

# ---------------------------------------------------------------- 18 CONNECTIONS
slide = new_slide()
add_title(slide, "Vista 02", "Conexiones multinúmero", "QR, API manual, Embedded Signup y coexistencia en un mismo panel. Estado, método, número y última actualización.", 18)
add_browser(slide, SCREENS / "connections.png", M, 1.95, 7.55, 4.75, "wagent.bponet.com.co/pages/whatsapp")
add_bullet_card(slide, 8.35, 1.95, 4.40, 1.55, "Un panel para todo", ["Varios números por empresa.", "QR, API, Embedded Signup y coexistencia.", "Estado en tiempo real y reconexión."], WHITE, LINE, INK, MUTED, 10.2, 8.2)
add_bullet_card(slide, 8.35, 3.65, 4.40, 1.85, "Nueva conexión", ["Nombre de la conexión.", "Tipo: QR o API.", "Método: token manual o Embedded Signup.", "Coexistencia opcional.", "PIN si el número ya lo tiene."], SOFT_GREEN, RGBColor(0xC9, 0xF0, 0xE2), INK, MUTED, 10.2, 8.2)
add_footer(slide, 18)

# ---------------------------------------------------------------- 19 INBOX
slide = new_slide()
add_title(slide, "Vista 03", "Bandeja de atención", "Una sola vista para conversaciones, agentes, prioridades, departamentos y bots. Menos pestañas, más contexto.", 19)
add_browser(slide, SCREENS / "inbox.png", M, 1.95, 7.55, 4.75, "wagent.bponet.com.co/pages/tickets")
add_bullet_card(slide, 8.35, 1.95, 4.40, 1.35, "Colaboración", ["Chats abiertos, pendientes, bots, resueltos y todos. Búsqueda y filtros."], SOFT_GREEN, RGBColor(0xC9, 0xF0, 0xE2), INK, MUTED, 10.2, 8.2)
add_bullet_card(slide, 8.35, 3.45, 4.40, 1.35, "Control del bot", ["Pausa y reanudación por conversación, ventana de bot y transferencia."], WHITE, LINE, INK, MUTED, 10.2, 8.2)
add_bullet_card(slide, 8.35, 4.95, 4.40, 1.35, "Multimedia y contexto", ["Texto, imágenes, documentos, audio, emojis y adjuntos. Historial completo."], WHITE, LINE, INK, MUTED, 10.2, 8.2)
add_footer(slide, 19)

# ---------------------------------------------------------------- 20 AUTOMATION
slide = new_slide()
add_title(slide, "Vista 04", "Automatizaciones: todos los flujos en un solo lugar", "Crea, publica y monitorea bots por conexión. Un bot puede operar en varias conexiones; cada número solo puede tener uno.", 20)
add_browser(slide, SCREENS / "automations.png", M, 1.95, 7.55, 4.75, "wagent.bponet.com.co/pages/chatbot")
add_bullet_card(slide, 8.35, 1.95, 4.40, 1.45, "Estados y control", ["Borrador o publicado, activo o inactivo. Autoguardado y validación antes de publicar."], WHITE, LINE, INK, MUTED, 10.2, 8.2)
add_bullet_card(slide, 8.35, 3.50, 4.40, 1.45, "Asignación por conexión", ["Un bot puede operar varias conexiones. Cada número de WhatsApp solo puede tener un bot."], WHITE, LINE, INK, MUTED, 10.2, 8.2)
add_bullet_card(slide, 8.35, 5.05, 4.40, 1.45, "Observabilidad", ["Logs por ejecución, fallbacks, transferencias y versiones para volver atrás."], SOFT_GREEN, RGBColor(0xC9, 0xF0, 0xE2), INK, MUTED, 10.2, 8.2)
add_footer(slide, 20)

# ---------------------------------------------------------------- 21 CANVAS
slide = new_slide()
add_title(slide, "Vista 05", "Canvas: así se construye un bot", "Arrastra nodos, conecta el recorrido y prueba antes de publicar. Todo queda versionado y asociado a tus conexiones.", 21)
add_browser(slide, SCREENS / "bot-builder.png", M, 1.95, 7.55, 4.75, "wagent.bponet.com.co/pages/chatbot/builder")
add_bullet_card(slide, 8.35, 1.95, 4.40, 1.45, "Dispara y conversa", ["Palabra clave, bienvenida, fuera de horario, evento o programación. Texto, archivos, botones, listas, enlaces, ubicación, contacto y plantillas."], WHITE, LINE, INK, MUTED, 10.2, 7.9)
add_bullet_card(slide, 8.35, 3.50, 4.40, 1.45, "Decide e integra", ["Condiciones, variables, esperas, horarios, aleatorio, bucles, etiquetas, saltos, APIs, bases de datos, data store, código y consentimiento."], WHITE, LINE, INK, MUTED, 10.2, 7.9)
add_bullet_card(slide, 8.35, 5.05, 4.40, 1.45, "Prueba y publica", ["Valida el esquema, prueba en el simulador, publica y conserva versiones. Los cambios se guardan automáticamente."], SOFT_GREEN, RGBColor(0xC9, 0xF0, 0xE2), INK, MUTED, 10.2, 7.9)
add_footer(slide, 21)

# ---------------------------------------------------------------- 22 CAPACIDADES
slide = new_slide()
add_title(slide, "Compatibilidad", "Qué puede hacer el bot según la conexión", "El mismo motor opera en API y QR. La diferencia está en los mensajes nativos de Meta y en los nodos que el constructor habilita.", 22)
headers = ["Capacidad", "API manual / Embedded", "QR / WhatsApp Web"]
rows = [
    ("Texto, archivos, ubicación y contacto", "Nativo.", "Nativo."),
    ("Botones, listas y enlace", "Nativo: hasta 3 botones y listas.", "Texto con opciones numeradas."),
    ("Plantilla Meta o local en el bot", "Sí, con el nodo Enviar plantilla.", "No: el nodo no se habilita."),
    ("Catálogo", "Nativo: producto, lista o carrusel.", "No disponible."),
    ("WhatsApp Flow", "Formulario nativo multi-pantalla.", "No disponible."),
    ("APIs, bases de datos, data store y código", "Sí.", "Sí."),
    ("Condiciones, variables, bucles y esperas", "Sí.", "Sí."),
    ("Transferencia, etiquetas y consentimiento", "Sí.", "Sí."),
    ("Disparadores y programación", "Sí.", "Sí."),
]
add_table(slide, M, 1.95, 12.25, 4.15, headers, rows, [4.55, 4.05, 3.65], 8.0)
add_dark_callout(slide, M, 6.28, 12.25, 0.60, "43 nodos en el canvas: 40 compartidos y 3 exclusivos de API (plantilla, catálogo y WhatsApp Flow). En QR, botones y listas se envían como texto para que el cliente responda escribiendo.", 8.2)
add_footer(slide, 22)

# ---------------------------------------------------------------- 23 BOTS POR CÓDIGO
slide = new_slide()
add_title(slide, "Avanzado", "Bots por código cuando el flujo necesita más", "JavaScript aislado, con recursos permitidos y los mismos controles de publicación, versiones y logs.", 23)
add_rect(slide, M, 1.95, 6.05, 4.75, DARK, None, True)
add_text(slide, M + 0.20, 2.10, 3.0, 0.20, "ONMESSAGE.JS", size=7.5, bold=True, color=RGBColor(0x8F, 0xF2, 0xC8))
code = (
    "export async function onMessage(ctx) {\n"
    "  const pedido = await ctx.http.get({\n"
    "    url: 'https://api.miempresa.com/pedido',\n"
    "    headers: { 'x-tel': ctx.contact.phone }\n"
    "  });\n\n"
    "  if (!pedido.ok) {\n"
    "    await ctx.reply.text('No pudimos consultar.');\n"
    "    return ctx.transfer({ departmentId: 'soporte' });\n"
    "  }\n\n"
    "  await ctx.reply.text(\n"
    "    `Pedido ${pedido.data.id}: ${pedido.data.estado}`\n"
    "  );\n"
    "  await ctx.tags.add(['pedido-consultado']);\n"
    "}"
)
add_text(slide, M + 0.20, 2.38, 5.65, 3.10, code, size=8.1, color=RGBColor(0xD9, 0xF2, 0xE8), line_spacing=1.22)
add_text(slide, M + 0.20, 5.70, 5.65, 0.70, "Se activa con features.codeNode. Cada llamada queda auditada y usa las mismas conexiones, logs y publicación que los flujos visuales.", size=8.4, color=RGBColor(0xB8, 0xD7, 0xCC), line_spacing=1.15)
add_bullet_card(slide, 6.85, 1.95, 5.95, 1.45, "Sandbox y límites", ["QuickJS aislado: sin npm, filesystem, process ni secretos. Timeout 500–5.000 ms, memoria 8–64 MB, 30 llamadas al host, 8 HTTP y 8 de BD."], SOFT_GREEN, RGBColor(0xC9, 0xF0, 0xE2), INK, MUTED, 10.2, 7.9)
add_bullet_card(slide, 6.85, 3.50, 5.95, 1.45, "Recursos permitidos", ["Credenciales API, conexiones de datos y políticas de consentimiento seleccionadas por alias. Nada fuera de la allowlist."], WHITE, LINE, INK, MUTED, 10.2, 7.9)
add_bullet_card(slide, 6.85, 5.05, 5.95, 1.45, "Funciones disponibles", ["Respuestas de texto, botones, listas, media, plantilla, ubicación, contacto, catálogo y flow; HTTP, BD, data store, etiquetas, agenda, consentimiento, transferencia, fin y log."], WHITE, LINE, INK, MUTED, 10.2, 7.6)
add_footer(slide, 23)

# ---------------------------------------------------------------- 24 OPERACIÓN DEL BOT
slide = new_slide()
add_title(slide, "Operación", "Del borrador a producción, con control", "Publica, prueba, versiona y observa cada ejecución. El modo de atención define si el bot se detiene al transferir.", 24)
add_bullet_card(slide, M, 1.95, 5.95, 2.15, "Ciclo de vida", ["Borrador y publicado; activo o inactivo.", "Autoguardado y validación de esquema.", "Versiones con restauración.", "Prueba en simulador antes de publicar."], WHITE, LINE, INK, MUTED, 10.8, 8.4)
add_bullet_card(slide, 6.85, 1.95, 5.95, 2.15, "Handoff a personas", ["Modo Bot + agentes o Solo bot.", "Transferencia a departamento o agente.", "Prioridad y mensaje de transferencia.", "El ticket conserva el contexto del chat."], SOFT_GREEN, RGBColor(0xC9, 0xF0, 0xE2), INK, MUTED, 10.8, 8.4)
add_bullet_card(slide, M, 4.25, 5.95, 2.15, "Ventana del bot", ["De 1 a 1.440 minutos.", "Se pausa al transferir y reanuda al vencer.", "Fallback y transferencia por conexión.", "Un número un bot; un bot varias conexiones."], WHITE, LINE, INK, MUTED, 10.8, 8.4)
add_bullet_card(slide, 6.85, 4.25, 5.95, 2.15, "Observabilidad", ["Logs por ejecución y por flujo.", "Fallbacks, transferencias y errores.", "Trazabilidad de nodos ejecutados.", "Reportes de rendimiento del bot."], WHITE, LINE, INK, MUTED, 10.8, 8.4)
add_footer(slide, 24)

# ---------------------------------------------------------------- 25 CAMPAIGNS
slide = new_slide()
add_title(slide, "Vista 06", "Campañas con plantillas", "Difusiones con plantillas aprobadas, variables, categorías, opt-in y trazabilidad de cada envío.", 25)
add_browser(slide, SCREENS / "broadcasts.png", M, 1.95, 5.9, 3.45, "wagent.bponet.com.co/pages/notifications")
add_browser(slide, SCREENS / "broadcast-dialog.png", 6.85, 1.95, 5.9, 3.45, "Nueva difusión · Plantilla")
add_card(slide, M, 5.65, 3.85, 1.05, "Plantillas", "Aprobadas por Meta, con variables y categoría.", WHITE, LINE, INK, MUTED, 9.2, 7.8)
add_card(slide, 4.65, 5.65, 3.85, 1.05, "Audiencia", "Números manuales o selector de contactos; opt-in.", WHITE, LINE, INK, MUTED, 9.2, 7.8)
add_card(slide, 8.50, 5.65, 4.25, 1.05, "Resultados", "Enviados, fallidos, estados y logs por campaña.", WHITE, LINE, INK, MUTED, 9.2, 7.8)
add_footer(slide, 25)

# ---------------------------------------------------------------- 26 LOCAL TEMPLATES
slide = new_slide()
add_title(slide, "Contenido", "Plantillas locales: texto reutilizable sin aprobación", "Para respuestas y campañas dentro de la conversación. No reemplazan a las plantillas aprobadas de Meta.", 26)
add_browser(slide, SCREENS / "local-templates.png", M, 1.95, 7.55, 4.75, "wagent.bponet.com.co/pages/local-templates")
add_bullet_card(slide, 8.35, 1.95, 4.40, 1.35, "Qué son", ["Nombre, cuerpo de texto y variables como {{nombre}}. Solo texto: sin encabezado, media, botones ni categoría de Meta."], WHITE, LINE, INK, MUTED, 10.2, 7.9)
add_bullet_card(slide, 8.35, 3.45, 4.40, 1.55, "Cuándo se pueden usar", ["En API, dentro de la ventana de 24 h desde la última respuesta. En QR se envían como texto de la sesión. Fuera de la ventana usa plantilla Meta."], SOFT_GREEN, RGBColor(0xC9, 0xF0, 0xE2), INK, MUTED, 10.2, 7.6)
add_bullet_card(slide, 8.35, 5.15, 4.40, 1.35, "Dónde se usan", ["Difusiones en modo Plantilla local y en el bot con Enviar plantilla → Plantilla local (conexiones API)."], WHITE, LINE, INK, MUTED, 10.2, 7.9)
add_footer(slide, 26)

# ---------------------------------------------------------------- 27 DEPARTMENTS
slide = new_slide()
add_title(slide, "Equipo", "Departamentos: ordenan el equipo y el enrutamiento", "Crea equipos, asigna agentes y define cómo se reparten las conversaciones de cada conexión.", 27)
add_browser(slide, SCREENS / "departments.png", M, 1.95, 7.55, 4.75, "wagent.bponet.com.co/pages/departments")
add_bullet_card(slide, 8.35, 1.95, 4.40, 1.35, "Crear", ["Nombre, descripción, regla de distribución y agentes. La vista muestra agentes activos, conversaciones y carga promedio."], WHITE, LINE, INK, MUTED, 10.2, 7.7)
add_bullet_card(slide, 8.35, 3.45, 4.40, 1.55, "Reglas", ["Round-robin: turnos.", "Menos ocupado: menor carga abierta.", "Ponderado: peso por agente.", "Manual: el equipo toma el ticket."], SOFT_GREEN, RGBColor(0xC9, 0xF0, 0xE2), INK, MUTED, 10.2, 8.2)
add_bullet_card(slide, 8.35, 5.15, 4.40, 1.35, "Conexión y transferencia", ["Asigna departamentos y uno predeterminado por conexión. El nodo Derivar agente elige departamento o agente, prioridad y mensaje. Hasta 50 agentes."], WHITE, LINE, INK, MUTED, 10.2, 7.4)
add_footer(slide, 27)

# ---------------------------------------------------------------- 28 AGENTS
slide = new_slide()
add_title(slide, "Equipo", "Agentes, carga y pesos de distribución", "Sincroniza el equipo, controla la carga y ajusta el reparto cuando usas ponderado aleatorio.", 28)
add_browser(slide, SCREENS / "agents.png", M, 1.95, 7.55, 4.75, "wagent.bponet.com.co/pages/departments/agents")
add_bullet_card(slide, 8.35, 1.95, 4.40, 1.35, "Sincronización", ["Los agentes se sincronizan desde el sistema de autenticación. Se controla su estado y pertenencia a cada departamento."], WHITE, LINE, INK, MUTED, 10.2, 7.7)
add_bullet_card(slide, 8.35, 3.45, 4.40, 1.55, "Pesos", ["Solo aplican a Ponderado Aleatorio. Cada agente tiene un peso de 1 a 100: mayor peso, más conversaciones asignadas."], SOFT_GREEN, RGBColor(0xC9, 0xF0, 0xE2), INK, MUTED, 10.2, 7.7)
add_bullet_card(slide, 8.35, 5.15, 4.40, 1.35, "Acceso y control", ["El agente ve las conversaciones de sus departamentos y conexiones asignadas. En asignación manual el sistema no elige."], WHITE, LINE, INK, MUTED, 10.2, 7.7)
add_footer(slide, 28)

# ---------------------------------------------------------------- 29 SCHEDULES
slide = new_slide()
add_title(slide, "Equipo", "Horarios: disponibilidad y mensajes fuera de horario", "Un horario general o uno por agente. La bandeja y el bot respetan la disponibilidad configurada.", 29)
add_browser(slide, SCREENS / "schedules.png", M, 1.95, 7.55, 4.75, "wagent.bponet.com.co/pages/schedules")
add_bullet_card(slide, 8.35, 1.95, 4.40, 1.35, "Horario general", ["Zona horaria, días y franjas de inicio y fin. Se aplica a todos los agentes cuando no hay horarios individuales."], WHITE, LINE, INK, MUTED, 10.2, 7.7)
add_bullet_card(slide, 8.35, 3.45, 4.40, 1.55, "Por agente", ["Activa horarios individuales. Sin horario configurado, el agente se considera disponible 24/7. La vista muestra En horario o Fuera de horario."], SOFT_GREEN, RGBColor(0xC9, 0xF0, 0xE2), INK, MUTED, 10.2, 7.6)
add_bullet_card(slide, 8.35, 5.15, 4.40, 1.35, "Fuera de horario y bot", ["Mensaje automático de hasta 500 caracteres. Los nodos Horario y Fuera de horario pueden usar el horario general y derivar o responder."], WHITE, LINE, INK, MUTED, 10.2, 7.5)
add_footer(slide, 29)

# ---------------------------------------------------------------- 30 USAGE
slide = new_slide()
add_title(slide, "Vista 07", "Consumo, límites y métricas", "Controla el uso por API y QR, las categorías de WhatsApp, los límites de la app y la capacidad del equipo.", 30)
add_browser(slide, SCREENS / "usage.png", M, 1.95, 7.55, 4.75, "wagent.bponet.com.co/pages/usage")
add_bullet_card(slide, 8.35, 1.95, 4.40, 1.35, "Consumo API", ["Mensajes, audio, entrantes y categorías. Disponible y porcentaje usado."], SOFT_GREEN, RGBColor(0xC9, 0xF0, 0xE2), INK, MUTED, 10.2, 8.2)
add_bullet_card(slide, 8.35, 3.45, 4.40, 1.35, "Consumo QR", ["Estadística separada: las conexiones QR no consumen cuota de API."], WHITE, LINE, INK, MUTED, 10.2, 8.2)
add_bullet_card(slide, 8.35, 4.95, 4.40, 1.35, "Límites y reportes", ["Agentes, flujos, conexiones y reportes de operación."], WHITE, LINE, INK, MUTED, 10.2, 8.2)
add_footer(slide, 30)

# ---------------------------------------------------------------- 24 CUOTAS
slide = new_slide()
add_title(slide, "Cuotas", "Cuotas y consumo: qué se mide", "Las cuotas se definen en el acuerdo con el cliente y se controlan por empresa, período y tipo de conexión.", 31)
add_bullet_card(slide, M, 1.95, 5.9, 1.85, "WhatsApp API: bolsa mensual", [
    "Mensajes salientes por API: texto, media y plantillas.",
    "Bolsa global mensual + bolsas por categoría.",
    "Entrantes: estadística; no consumen bolsa.",
    "QR no consume la bolsa de API.",
], SOFT_GREEN, RGBColor(0xC9, 0xF0, 0xE2), INK, MUTED, 11, 8.8)
add_bullet_card(slide, 6.85, 1.95, 5.9, 1.85, "Audio, conexiones y equipo", [
    "Bolsa mensual de audio para API.",
    "Canal de audio habilitado o deshabilitado.",
    "Límite de conexiones API, QR y Embedded.",
    "Límite de agentes y flujos de chatbot.",
], WHITE, LINE, INK, MUTED, 11, 8.8)
headers = ["Recurso", "Cómo se mide", "Aplica a"]
rows = [
    ("WhatsApp API", "Mensajes salientes por mes.", "API manual y Embedded."),
    ("Categorías", "Utilidad, marketing, autenticación y servicio.", "API manual y Embedded."),
    ("Audio", "Audios salientes por mes.", "API; QR solo estadística."),
    ("Conexiones", "Sesiones activas por tipo.", "API, QR y Embedded."),
    ("Equipo", "Agentes y flujos creados.", "Plataforma."),
]
add_table(slide, M, 3.95, 12.0, 2.05, headers, rows, [3.0, 4.8, 4.2], 8.2)
add_text(slide, M, 6.18, 12.0, 0.22, "El período es mensual y se calcula en la zona horaria del cliente. El histórico disponible es de 12 meses.", size=7.8, color=MUTED)
add_footer(slide, 31)

# ---------------------------------------------------------------- 25 CUOTAS ACUERDO
slide = new_slide()
add_title(slide, "Acuerdo", "Cuotas según el acuerdo y qué pasa al llegar al límite", "BPONET configura la política de cada empresa según el contrato; el cliente la consulta y solicita ampliación cuando la necesita.", 32)
add_bullet_card(slide, M, 1.95, 5.9, 3.50, "Cómo se gestiona", [
    "El acuerdo define bolsa mensual, categorías, audio, conexiones, agentes y flujos.",
    "BPONET configura los topes en la política de la empresa.",
    "Los cambios se aplican en la siguiente validación.",
    "El cliente consulta usado, disponible y % en Uso y consumo.",
    "Las ampliaciones se solicitan a BPONET.",
], SOFT_GREEN, RGBColor(0xC9, 0xF0, 0xE2), INK, MUTED, 11, 8.8)
add_bullet_card(slide, 6.85, 1.95, 5.9, 3.50, "Qué pasa al llegar al límite", [
    "Envío API: se bloquea con mensaje claro.",
    "Difusión: aviso si supera lo disponible; los mensajes que exceden fallan y quedan en el log.",
    "Audio: bloqueo si está deshabilitado o se alcanza la bolsa.",
    "Conexiones, agentes o flujos: no se crean más allá del tope.",
    "QR: no consume la bolsa de API; solo se contabiliza.",
], WHITE, LINE, INK, MUTED, 11, 8.8)
add_dark_callout(slide, M, 5.75, 12.0, 0.68, "Sin cobros sorpresa: la cuota se define en el acuerdo y se controla antes de enviar. El cliente ve su consumo y solicita ampliación cuando la necesita.", 8.8)
add_footer(slide, 32)


# ---------------------------------------------------------------- 24 INTEGRATIONS
slide = new_slide()
add_title(slide, "Ecosistema", "Integraciones y extensibilidad", "Wagent se conecta con tus sistemas: entrada por API keys, salida por credenciales, bases de datos y webhooks.", 33)
add_browser(slide, SCREENS / "api-keys.png", M, 1.95, 7.55, 4.75, "wagent.bponet.com.co/pages/api-keys")
mini = [
    ("API Keys", "Apps externas llaman a Wagent con scopes y rate limit."),
    ("Credenciales", "Wagent llama APIs externas con allowlist y cifrado."),
    ("Bases de datos", "PostgreSQL, MySQL, MongoDB y Redis para flujos."),
    ("WhatsApp Flows", "Formularios nativos y data exchange."),
    ("Webhooks", "Eventos de mensajes, tickets y sesiones."),
    ("Catálogo", "Productos y carruseles en la conversación."),
]
for i, (title, body) in enumerate(mini):
    col = i % 2
    row = i // 2
    add_card(slide, 8.35 + col * 2.25, 1.95 + row * 1.58, 2.10, 1.40, title, body, WHITE, LINE, INK, MUTED, 9.0, 7.4)
add_footer(slide, 33)

# ---------------------------------------------------------------- 25 SECURITY
slide = new_slide()
add_title(slide, "Confianza", "Seguridad y cumplimiento", "La conversación contiene datos personales. Wagent los trata con aislamiento, cifrado y trazabilidad.", 34)
sec = [
    ("Cifrado", "Tokens de acceso cifrados con AES-256-GCM. HTTPS/TLS en tránsito."),
    ("Aislamiento", "Contexto de empresa en cada request y consultas filtradas por tenant."),
    ("Roles", "JWT, permisos granulares, guards por rol y revalidación de sesión."),
    ("Consentimientos", "Políticas versionadas, evidencia de aceptación y opt-in."),
    ("Eliminación", "Purga por empresa, página pública y plazo de 15 días hábiles."),
    ("Auditoría", "Registro de operaciones sensibles, accesos y eventos de sesión."),
]
for i, (title, body) in enumerate(sec):
    col = i % 3
    row = i // 3
    add_card(slide, M + col * 4.05, 1.95 + row * 1.85, 3.85, 1.65, title, body, SOFT_GREEN if i in (0, 3) else WHITE, RGBColor(0xC9, 0xF0, 0xE2) if i in (0, 3) else LINE, INK, MUTED, 10.8, 8.6)
add_dark_callout(slide, M, 5.75, 12.0, 0.70, "Marco: Ley 1581 de 2012, Decreto 1377 de 2013, políticas de Meta y acuerdo de tratamiento de datos con subencargados.", 8.8)
add_footer(slide, 34)

# ---------------------------------------------------------------- 26 ADVANTAGES
slide = new_slide()
add_title(slide, "Por qué Wagent", "Ocho razones para centralizar WhatsApp", "Menos herramientas, más control. Una plataforma que crece con la operación.", 35)
adv = [
    ("Multiempresa", "Una instancia, muchas empresas, datos aislados."),
    ("Multinúmero", "Varios números y modalidades por empresa."),
    ("Coexistencia", "La app Business y la API en el mismo número."),
    ("Automatización", "Visual, por código, con APIs y bases de datos."),
    ("Equipo", "Bandeja compartida, roles y distribución."),
    ("Campañas", "Plantillas, opt-in y logs de entrega."),
    ("Integraciones", "CRM, ERP, DB, webhooks y Flows."),
    ("Cumplimiento", "Consentimiento, auditoría y eliminación."),
]
for i, (title, body) in enumerate(adv):
    col = i % 4
    row = i // 4
    add_card(slide, M + col * 3.05, 1.95 + row * 1.85, 2.85, 1.65, title, body, SOFT_GREEN if i < 4 else WHITE, RGBColor(0xC9, 0xF0, 0xE2) if i < 4 else LINE, INK, MUTED, 10.2, 8.0)
add_text(slide, M, 6.15, 12.0, 0.40, "“La forma más directa de convertir WhatsApp en una operación medible.”", size=13, bold=True, color=GREEN_DARK)
add_footer(slide, 35)

# ---------------------------------------------------------------- 27 USE CASES
slide = new_slide()
add_title(slide, "Aplicación", "Un producto, múltiples operaciones", "El mismo motor sirve para soporte, ventas, citas, notificaciones, cobranza y encuestas.", 36)
cases = [
    ("Soporte", "Bandeja compartida, prioridades, SLA, bots de triage y transferencia."),
    ("Ventas", "Calificación de leads, catálogo, seguimiento y recuperación de carrito."),
    ("Citas", "Agendamiento, confirmación, recordatorios y reprogramación."),
    ("Notificaciones", "Pedidos, pagos, entregas y alertas transaccionales."),
    ("Cobranza", "Recordatorios de pago, acuerdos y seguimiento de cartera."),
    ("Encuestas", "NPS, satisfacción post-venta y retroalimentación."),
]
for i, (title, body) in enumerate(cases):
    col = i % 3
    row = i // 3
    add_card(slide, M + col * 4.05, 1.95 + row * 1.80, 3.85, 1.60, title, body, WHITE, LINE, INK, MUTED, 10.8, 8.6)
add_dark_callout(slide, M, 5.70, 5.9, 0.80, "Mismo motor, distinto flujo: conexiones, bandeja, automatización y campañas se combinan.", 8.6)
add_bullet_card(slide, 6.85, 5.70, 5.9, 0.80, "Resultado", ["Menos tiempos de respuesta, más conversaciones resueltas y trazabilidad completa."], SOFT_GREEN, RGBColor(0xC9, 0xF0, 0xE2), INK, MUTED, 9.0, 7.8)
add_footer(slide, 36)

# ---------------------------------------------------------------- 28 CLOSING
slide = new_slide(DARK)
slide.shapes.add_picture(str(ASSETS / "logo-bponet-white.png"), Inches(M), Inches(0.45), height=Inches(0.55))
add_text(slide, 11.3, 0.48, 1.5, 0.20, "2026", size=8, bold=True, color=RGBColor(0x74, 0xA9, 0x9A), align=PP_ALIGN.RIGHT)
add_pill(slide, M, 2.05, 1.8, "SIGUIENTE PASO", RGBColor(0x0E, 0x3B, 0x30), RGBColor(0x8F, 0xF2, 0xC8), 7.2)
add_text(slide, M, 2.45, 11.0, 0.82, "Conversemos.", size=48, bold=True, color=WHITE, line_spacing=0.95)
add_text(slide, M, 3.27, 11.4, 0.82, "Tu WhatsApp puede operar mejor.", size=40, bold=True, color=GREEN_BRIGHT, line_spacing=0.95)
add_text(slide, M, 4.18, 8.9, 0.80, "Wagent conecta la API oficial, tu equipo y tus procesos en una sola plataforma.\nSin costos en esta presentación: solo el software y su operación.", size=12.5, color=RGBColor(0xB8, 0xD7, 0xCC), line_spacing=1.25)
contacts = [
    ("Correo", "gerencia@bponet.com.co"),
    ("Teléfonos", "602 2822990 · +57 313 788 5351"),
    ("Web", "wagent.bponet.com.co"),
]
x = M
for label, value in contacts:
    add_text(slide, x, 5.20, 3.7, 0.18, label.upper(), size=6.8, bold=True, color=RGBColor(0x7F, 0xA7, 0x9A))
    add_text(slide, x, 5.42, 3.8, 0.22, value, size=9.5, bold=True, color=RGBColor(0xE9, 0xF7, 0xF2))
    x += 4.05
add_footer(slide, 37, dark=True)

# Notas del presentador
notes = {
    1: "Abrir con la promesa: todo WhatsApp en una sola plataforma. Mencionar que la presentación no incluye costos.",
    2: "Recorrer la agenda: primero conexión con BPONET, después producto y operación.",
    3: "BPONET es Tech Provider. El cliente no gestiona la app de Meta para Embedded Signup/coexistencia.",
    4: "Tres caminos: QR, API manual y Embedded/coexistencia. Cada uno tiene requisitos distintos.",
    5: "Comparar requisitos: cuenta Meta, WABA, número, token, App Review, webhooks y plantillas.",
    6: "El WABA aplica a API y Embedded. QR no usa WABA ni Graph API.",
    7: "QR: rápido, sin Meta, pero depende del teléfono y no tiene webhooks oficiales.",
    8: "API manual: el cliente ya tiene WABA y token; gestiona su app de Meta y webhooks.",
    9: "Embedded/coexistencia: BPONET gestiona Meta; el cliente solo autoriza cuenta y número.",
    10: "Coexistencia: 24 h, 20 mps, límites y sincronización.",
    11: "Webhooks: el cliente los gestiona en API manual; BPONET en Embedded; QR no usa.",
    12: "Quién gestiona qué: tabla de responsabilidades por camino.",
    13: "Decisión rápida: sin WABA → Embedded; con WABA/token → API; prueba rápida → QR.",
    17: "Mostrar el dashboard como centro de control de la operación.",
    18: "Destacar multinúmero y coexistencia.",
    19: "Mostrar la bandeja como el lugar donde el equipo trabaja.",
    20: "Vista general de flujos: estados, asignación por conexión y logs.",
    21: "Canvas con un flujo creado: disparadores, mensajes, lógica, integración y publicación.",
    22: "Explicar qué cambia entre API y QR: nativos, plantillas, catálogo y Flows.",
    23: "Bots por código: sandbox, límites y recursos permitidos.",
    24: "Handoff, ventana del bot, versiones, logs y simulación.",
    25: "Difusiones con plantillas Meta, opt-in y logs.",
    26: "Plantillas locales: solo texto, variables y ventana de 24 h en API.",
    27: "Departamentos: crear, reglas, asignación a conexión y transferencia.",
    28: "Agentes y pesos: sincronización, carga y ponderado aleatorio.",
    29: "Horarios generales o por agente, mensaje fuera de horario y nodos del bot.",
    30: "Consumo y límites por API y QR.",
    31: "Cuotas: bolsa mensual, categorías, audio, conexiones y equipo.",
    32: "El acuerdo define los topes. BPONET los configura; el cliente solicita ampliación.",
    33: "Integraciones como ventaja competitiva.",
    34: "Cerrar con seguridad y cumplimiento.",
    35: "Resumir las ocho ventajas.",
    36: "Conectar con casos reales del cliente.",
    37: "Cerrar con contacto y siguiente paso.",
}
for idx, text in notes.items():
    prs.slides[idx - 1].notes_slide.notes_text_frame.text = text

prs.save(OUT)
print(f"OK: {OUT} ({len(prs.slides)} slides)")

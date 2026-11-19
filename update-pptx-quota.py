from pathlib import Path

path = Path(__file__).resolve().parent / "generate-pptx.py"
script = path.read_text()

# Total de diapositivas
script = script.replace('f"{page:02d} / 28"', 'f"{page:02d} / 30"')

# Renumerar bloques existentes 24-28 -> 26-30 (antes de insertar las nuevas)
def replace_block(start_marker, end_marker, replacements):
    global script
    start = script.index(start_marker)
    end = script.index(end_marker, start)
    block = script[start:end]
    for old, new in replacements:
        block = block.replace(old, new)
    script = script[:start] + block + script[end:]

replace_block(
    "# ---------------------------------------------------------------- 24 INTEGRATIONS",
    "# ---------------------------------------------------------------- 25 SECURITY",
    [
        ('add_title(slide, "Ecosistema", "Integraciones y extensibilidad", "Wagent se conecta con tus sistemas: entrada por API keys, salida por credenciales, bases de datos y webhooks.", 24)',
         'add_title(slide, "Ecosistema", "Integraciones y extensibilidad", "Wagent se conecta con tus sistemas: entrada por API keys, salida por credenciales, bases de datos y webhooks.", 26)'),
        ('add_footer(slide, 24)', 'add_footer(slide, 26)'),
    ],
)
replace_block(
    "# ---------------------------------------------------------------- 25 SECURITY",
    "# ---------------------------------------------------------------- 26 ADVANTAGES",
    [
        ('add_title(slide, "Confianza", "Seguridad y cumplimiento", "La conversación contiene datos personales. Wagent los trata con aislamiento, cifrado y trazabilidad.", 25)',
         'add_title(slide, "Confianza", "Seguridad y cumplimiento", "La conversación contiene datos personales. Wagent los trata con aislamiento, cifrado y trazabilidad.", 27)'),
        ('add_footer(slide, 25)', 'add_footer(slide, 27)'),
    ],
)
replace_block(
    "# ---------------------------------------------------------------- 26 ADVANTAGES",
    "# ---------------------------------------------------------------- 27 USE CASES",
    [
        ('add_title(slide, "Por qué Wagent", "Ocho razones para centralizar WhatsApp", "Menos herramientas, más control. Una plataforma que crece con la operación.", 26)',
         'add_title(slide, "Por qué Wagent", "Ocho razones para centralizar WhatsApp", "Menos herramientas, más control. Una plataforma que crece con la operación.", 28)'),
        ('add_footer(slide, 26)', 'add_footer(slide, 28)'),
    ],
)
replace_block(
    "# ---------------------------------------------------------------- 27 USE CASES",
    "# ---------------------------------------------------------------- 28 CLOSING",
    [
        ('add_title(slide, "Aplicación", "Un producto, múltiples operaciones", "El mismo motor sirve para soporte, ventas, citas, notificaciones, cobranza y encuestas.", 27)',
         'add_title(slide, "Aplicación", "Un producto, múltiples operaciones", "El mismo motor sirve para soporte, ventas, citas, notificaciones, cobranza y encuestas.", 29)'),
        ('add_footer(slide, 27)', 'add_footer(slide, 29)'),
    ],
)
# Cierre
script = script.replace('add_footer(slide, 28, dark=True)', 'add_footer(slide, 30, dark=True)')

quota_block = '''# ---------------------------------------------------------------- 24 CUOTAS
slide = new_slide()
add_title(slide, "Cuotas", "Cuotas y consumo: qué se mide", "Las cuotas se definen en el acuerdo con el cliente y se controlan por empresa, período y tipo de conexión.", 24)
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
add_footer(slide, 24)

# ---------------------------------------------------------------- 25 CUOTAS ACUERDO
slide = new_slide()
add_title(slide, "Acuerdo", "Cuotas según el acuerdo y qué pasa al llegar al límite", "BPONET configura la política de cada empresa según el contrato; el cliente la consulta y solicita ampliación cuando la necesita.", 25)
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
add_footer(slide, 25)

'''

anchor = "add_footer(slide, 23)\n"
if anchor not in script:
    raise SystemExit("No se encontró add_footer(slide, 23)")
script = script.replace(anchor, anchor + quota_block, 1)

# Notas completas
notes_block = '''notes = {
    1: "Abrir con la promesa: todo WhatsApp en una sola plataforma. Mencionar que la presentación no incluye costos.",
    2: "Recorrer la agenda en 30 segundos: primero conexión con BPONET, después producto.",
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
    20: "Explicar que la automatización combina no-code y código.",
    21: "Mostrar plantillas aprobadas y trazabilidad.",
    22: "Reglas de distribución y horarios.",
    23: "Control de consumo y límites.",
    24: "Cuotas: bolsa mensual, categorías, audio, conexiones y equipo. QR no consume API.",
    25: "El acuerdo define los topes. BPONET los configura; el cliente ve su consumo y solicita ampliación.",
    26: "Integraciones como ventaja competitiva.",
    27: "Cerrar con seguridad y cumplimiento.",
    28: "Resumir las ocho ventajas.",
    29: "Conectar con casos reales del cliente.",
    30: "Cerrar con contacto y siguiente paso.",
}'''
start = script.index("notes = {")
end = script.index("}\nfor idx, text in notes.items():", start) + 1
script = script[:start] + notes_block + script[end:]

path.write_text(script)
print("PPTX quota slides inserted and pages renumbered")

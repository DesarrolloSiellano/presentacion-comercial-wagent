from pathlib import Path

path = Path(__file__).resolve().parent / "generate-pptx.py"
script = path.read_text()

new_block = '''# ---------------------------------------------------------------- 04 TRES CAMINOS
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

'''

start_marker = "# ---------------------------------------------------------------- 04 DOS FORMAS\n"
end_marker = "# ---------------------------------------------------------------- 14 DIVIDER APP\n"
start = script.index(start_marker)
end = script.index(end_marker, start)
script = script[:start] + new_block + script[end:]

path.write_text(script)
print("Generador PPTX: primera parte sincronizada con los tres caminos")

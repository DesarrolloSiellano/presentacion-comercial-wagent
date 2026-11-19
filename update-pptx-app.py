from pathlib import Path

path = Path(__file__).resolve().parent / "generate-pptx.py"
script = path.read_text()

# Total de diapositivas
script = script.replace('f"{page:02d} / 30"', 'f"{page:02d} / 37"')

new_block = '''# ---------------------------------------------------------------- 20 AUTOMATION
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
    "export async function onMessage(ctx) {\\n"
    "  const pedido = await ctx.http.get({\\n"
    "    url: 'https://api.miempresa.com/pedido',\\n"
    "    headers: { 'x-tel': ctx.contact.phone }\\n"
    "  });\\n\\n"
    "  if (!pedido.ok) {\\n"
    "    await ctx.reply.text('No pudimos consultar.');\\n"
    "    return ctx.transfer({ departmentId: 'soporte' });\\n"
    "  }\\n\\n"
    "  await ctx.reply.text(\\n"
    "    `Pedido ${pedido.data.id}: ${pedido.data.estado}`\\n"
    "  );\\n"
    "  await ctx.tags.add(['pedido-consultado']);\\n"
    "}"
)
add_text(slide, M + 0.20, 2.38, 5.65, 4.10, code, size=8.1, color=RGBColor(0xD9, 0xF2, 0xE8), line_spacing=1.22)
add_bullet_card(slide, 6.85, 1.95, 5.95, 1.45, "Sandbox y límites", ["QuickJS aislado: sin npm, filesystem, process ni secretos. Timeout 500–5.000 ms, memoria 8–64 MB, 30 llamadas al host, 8 HTTP y 8 de BD."], SOFT_GREEN, RGBColor(0xC9, 0xF0, 0xE2), INK, MUTED, 10.2, 7.9)
add_bullet_card(slide, 6.85, 3.50, 5.95, 1.45, "Recursos permitidos", ["Credenciales API, conexiones de datos y políticas de consentimiento seleccionadas por alias. Nada fuera de la allowlist."], WHITE, LINE, INK, MUTED, 10.2, 7.9)
add_bullet_card(slide, 6.85, 5.05, 5.95, 1.45, "Funciones disponibles", ["Respuestas de texto, botones, listas, media, plantilla, ubicación, contacto, catálogo y flow; HTTP, BD, data store, etiquetas, agenda, consentimiento, transferencia, fin y log."], WHITE, LINE, INK, MUTED, 10.2, 7.6)
add_footer(slide, 23)

# ---------------------------------------------------------------- 24 OPERACIÓN DEL BOT
slide = new_slide()
add_title(slide, "Operación", "Del borrador a producción, con control", "Publica, prueba, versiona y observa cada ejecución. El bot se detiene cuando un agente toma la conversación.", 24)
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

'''

start_marker = "# ---------------------------------------------------------------- 20 AUTOMATION\n"
end_marker = "# ---------------------------------------------------------------- 24 CUOTAS\n"
start = script.index(start_marker)
end = script.index(end_marker, start)
script = script[:start] + new_block + script[end:]

# Renumerar solo los bloques existentes, sin tocar las diapositivas nuevas.
def renumber_block(start_marker, end_marker, old_page, new_page):
    global script
    start = script.index(start_marker)
    end = script.index(end_marker, start)
    block = script[start:end]
    block = block.replace(f"add_title(", "add_title(", 1)
    block = block.replace(f", {old_page})", f", {new_page})", 1)
    block = block.replace(f"add_footer(slide, {old_page})", f"add_footer(slide, {new_page})")
    script = script[:start] + block + script[end:]


renumber_block(
    "# ---------------------------------------------------------------- 24 CUOTAS",
    "# ---------------------------------------------------------------- 25 CUOTAS ACUERDO",
    24,
    31,
)
renumber_block(
    "# ---------------------------------------------------------------- 25 CUOTAS ACUERDO",
    "# ---------------------------------------------------------------- 24 INTEGRATIONS",
    25,
    32,
)
renumber_block(
    "# ---------------------------------------------------------------- 24 INTEGRATIONS",
    "# ---------------------------------------------------------------- 25 SECURITY",
    26,
    33,
)
renumber_block(
    "# ---------------------------------------------------------------- 25 SECURITY",
    "# ---------------------------------------------------------------- 26 ADVANTAGES",
    27,
    34,
)
renumber_block(
    "# ---------------------------------------------------------------- 26 ADVANTAGES",
    "# ---------------------------------------------------------------- 27 USE CASES",
    28,
    35,
)
renumber_block(
    "# ---------------------------------------------------------------- 27 USE CASES",
    "# ---------------------------------------------------------------- 28 CLOSING",
    29,
    36,
)
script = script.replace("add_footer(slide, 30, dark=True)", "add_footer(slide, 37, dark=True)")

# Integraciones: corregir tarjeta duplicada.
script = script.replace('''    add_card(slide, 8.35 + col * 2.25, 1.95 + row * 1.58, 2.10, 1.40, title, body, WHITE, LINE, INK, MUTED, 9.0, 7.4)
    add_card(slide, 8.35 + col * 2.25, 1.95 + row * 1.58, 2.10, 1.40, title, body, WHITE, LINE, INK, MUTED, 9.0, 7.4)''',
'''    add_card(slide, 8.35 + col * 2.25, 1.95 + row * 1.58, 2.10, 1.40, title, body, WHITE, LINE, INK, MUTED, 9.0, 7.4)''')

# Notas del presentador
notes_block = '''notes = {
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
}'''
start = script.index("notes = {")
end = script.index("}\nfor idx, text in notes.items():", start) + 1
script = script[:start] + notes_block + script[end:]

path.write_text(script)
print("Generador PPTX actualizado a 37 diapositivas")

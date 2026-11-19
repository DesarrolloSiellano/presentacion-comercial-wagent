from pathlib import Path
import re

root = Path(__file__).resolve().parent
html_path = root / "Wagent-Presentacion-Comercial.html"
html = html_path.read_text()


def replace_once(old, new, label):
    global html
    if old not in html:
        raise SystemExit(f"No se encontró: {label}")
    html = html.replace(old, new, 1)


# --- Ajustar la diapositiva de automatizaciones ---------------------------------
replace_once(
    '<h2 class="slide-title">Automatización visual y por código</h2>\n          <p class="slide-subtitle">Flujos que responden, clasifican, integran APIs, consultan bases de datos y transfieren al equipo correcto.</p>',
    '<h2 class="slide-title">Automatizaciones: todos los flujos en un solo lugar</h2>\n          <p class="slide-subtitle">Crea, publica y monitorea bots por conexión. Un bot puede operar en varias conexiones; cada número solo puede tener uno.</p>',
    "título automatizaciones",
)
replace_once(
    '''<div>
          <div class="card" style="margin-bottom:12px"><h3>Constructor visual</h3><p>Nodos de mensaje, botones, listas, condiciones, esperas, horarios, etiquetas y saltos de flujo.</p></div>
          <div class="card" style="margin-bottom:12px"><h3>Integraciones</h3><p>Llamadas a APIs, credenciales, PostgreSQL, MySQL, MongoDB, Redis y código aislado.</p></div>
          <div class="card"><h3>Control</h3><p>Validación, publicación, versiones, logs de ejecución, fallbacks y consentimientos.</p></div>
        </div>''',
    '''<div>
          <div class="card" style="margin-bottom:12px"><h3>Estados y control</h3><p>Borrador o publicado, activo o inactivo. Autoguardado y validación antes de publicar.</p></div>
          <div class="card" style="margin-bottom:12px"><h3>Asignación por conexión</h3><p>Un bot puede operar varias conexiones. Cada número de WhatsApp solo puede tener un bot.</p></div>
          <div class="card"><h3>Observabilidad</h3><p>Logs por ejecución, fallbacks, transferencias y versiones para volver atrás.</p></div>
        </div>''',
    "tarjetas automatizaciones",
)


bot_block = '''
    <!-- 21 CANVAS DEL BOT -->
    <section class="slide" data-title="Canvas del bot">
      <div class="slide-header">
        <div>
          <div class="kicker">Vista 05</div>
          <h2 class="slide-title">Canvas: así se construye un bot</h2>
          <p class="slide-subtitle">Arrastra nodos, conecta el recorrido y prueba antes de publicar. Todo queda versionado y asociado a tus conexiones.</p>
        </div>
        <div class="slide-number">21 / 37</div>
      </div>
      <div class="content grid-2-1">
        <div class="browser">
          <div class="browser-bar"><span class="browser-dot"></span><span class="browser-dot"></span><span class="browser-dot"></span><div class="browser-url">wagent.bponet.com.co/pages/chatbot/builder</div></div>
          <img src="assets/screens/bot-builder.png" alt="Canvas del constructor de bots con un flujo creado" />
        </div>
        <div>
          <div class="card" style="margin-bottom:12px"><h3>Dispara y conversa</h3><p>Palabra clave, bienvenida, fuera de horario, evento o programación. Mensajes de texto, archivos, botones, listas, enlaces, ubicación, contacto y plantillas.</p></div>
          <div class="card" style="margin-bottom:12px"><h3>Decide e integra</h3><p>Condiciones, variables, esperas, horarios, aleatorio, bucles, etiquetas, saltos de flujo, APIs, bases de datos, data store, código y consentimiento.</p></div>
          <div class="card"><h3>Prueba y publica</h3><p>Valida el esquema, prueba en el simulador, publica y conserva versiones. Los cambios se guardan automáticamente.</p></div>
        </div>
      </div>
      <div class="slide-footer"><span>BPONET SAS</span><div class="rule"></div><span>Wagent · Presentación comercial</span><span>21</span></div>
    </section>

    <!-- 22 CAPACIDADES POR CONEXIÓN -->
    <section class="slide" data-title="Capacidades del bot por conexión">
      <div class="slide-header">
        <div>
          <div class="kicker">Compatibilidad</div>
          <h2 class="slide-title">Qué puede hacer el bot según la conexión</h2>
          <p class="slide-subtitle">El mismo motor opera en API y QR. La diferencia está en los mensajes nativos de Meta y en los nodos que el constructor habilita.</p>
        </div>
        <div class="slide-number">22 / 37</div>
      </div>
      <div class="content">
        <div class="card flat" style="padding:4px 10px">
          <table class="table" style="font-size:9.0px">
            <thead><tr><th>Capacidad</th><th>API manual / Embedded</th><th>QR / WhatsApp Web</th></tr></thead>
            <tbody>
              <tr><td><strong>Texto, archivos, ubicación y contacto</strong></td><td>Nativo.</td><td>Nativo.</td></tr>
              <tr><td><strong>Botones, listas y enlace</strong></td><td>Nativo: hasta 3 botones y listas.</td><td>Se envía como texto con opciones numeradas.</td></tr>
              <tr><td><strong>Plantilla Meta o local en el bot</strong></td><td>Sí, con el nodo Enviar plantilla.</td><td>No: el nodo no se habilita.</td></tr>
              <tr><td><strong>Catálogo</strong></td><td>Nativo: producto, lista o carrusel.</td><td>No disponible.</td></tr>
              <tr><td><strong>WhatsApp Flow</strong></td><td>Formulario nativo multi-pantalla.</td><td>No disponible.</td></tr>
              <tr><td><strong>APIs, bases de datos, data store y código</strong></td><td>Sí.</td><td>Sí.</td></tr>
              <tr><td><strong>Condiciones, variables, bucles y esperas</strong></td><td>Sí.</td><td>Sí.</td></tr>
              <tr><td><strong>Transferencia, etiquetas y consentimiento</strong></td><td>Sí.</td><td>Sí.</td></tr>
              <tr><td><strong>Disparadores y programación</strong></td><td>Sí.</td><td>Sí.</td></tr>
            </tbody>
          </table>
        </div>
        <div class="card dark" style="margin-top:12px;padding:11px 16px">
          <p style="font-size:10.2px;color:#b8d7cc"><strong style="color:#fff">43 nodos en el canvas:</strong> 40 compartidos y 3 exclusivos de API (plantilla, catálogo y WhatsApp Flow). En QR, botones y listas se envían como texto para que el cliente responda escribiendo.</p>
        </div>
      </div>
      <div class="slide-footer"><span>BPONET SAS</span><div class="rule"></div><span>Wagent · Presentación comercial</span><span>22</span></div>
    </section>

    <!-- 23 BOTS POR CÓDIGO -->
    <section class="slide" data-title="Bots por código">
      <div class="slide-header">
        <div>
          <div class="kicker">Avanzado</div>
          <h2 class="slide-title">Bots por código cuando el flujo necesita más</h2>
          <p class="slide-subtitle">JavaScript aislado, con recursos permitidos y los mismos controles de publicación, versiones y logs.</p>
        </div>
        <div class="slide-number">23 / 37</div>
      </div>
      <div class="content grid-2">
        <div class="card dark" style="padding:14px 16px">
          <div class="kicker dark" style="margin-bottom:8px">onMessage.js</div>
          <pre style="margin:0;font-family:'DM Mono','SFMono-Regular',Consolas,monospace;font-size:8.6px;line-height:1.55;color:#d9f2e8;white-space:pre-wrap">export async function onMessage(ctx) {
  const pedido = await ctx.http.get({
    url: 'https://api.miempresa.com/pedido',
    headers: { 'x-tel': ctx.contact.phone }
  });

  if (!pedido.ok) {
    await ctx.reply.text('No pudimos consultar tu pedido.');
    return ctx.transfer({ departmentId: 'soporte' });
  }

  await ctx.reply.text(
    `Pedido ${pedido.data.id}: ${pedido.data.estado}`
  );
  await ctx.tags.add(['pedido-consultado']);
}</pre>
        </div>
        <div>
          <div class="card green" style="margin-bottom:12px"><h3>Sandbox y límites</h3><p>QuickJS aislado: sin npm, filesystem, process ni secretos. Timeout de 500 a 5.000 ms, memoria de 8 a 64 MB, hasta 30 llamadas al host, 8 HTTP y 8 de base de datos.</p></div>
          <div class="card" style="margin-bottom:12px"><h3>Recursos permitidos</h3><p>Credenciales API, conexiones de datos y políticas de consentimiento seleccionadas por alias. Nada fuera de la allowlist.</p></div>
          <div class="card"><h3>Funciones disponibles</h3><p>Respuestas de texto, botones, listas, media, plantilla, ubicación, contacto, catálogo y flow; HTTP, base de datos, data store, etiquetas, agenda, consentimiento, transferencia, fin y log.</p></div>
        </div>
      </div>
      <div class="slide-footer"><span>BPONET SAS</span><div class="rule"></div><span>Wagent · Presentación comercial</span><span>23</span></div>
    </section>

    <!-- 24 OPERACIÓN DEL BOT -->
    <section class="slide" data-title="Operación del bot">
      <div class="slide-header">
        <div>
          <div class="kicker">Operación</div>
          <h2 class="slide-title">Del borrador a producción, con control</h2>
          <p class="slide-subtitle">Publica, prueba, versiona y observa cada ejecución. El bot se detiene cuando un agente toma la conversación.</p>
        </div>
        <div class="slide-number">24 / 37</div>
      </div>
      <div class="content grid-2">
        <div class="card"><h3>Ciclo de vida</h3><ul class="list-clean" style="margin-top:8px"><li>Borrador y publicado; activo o inactivo.</li><li>Autoguardado y validación de esquema.</li><li>Versiones con restauración.</li><li>Prueba en simulador antes de publicar.</li></ul></div>
        <div class="card green"><h3>Handoff a personas</h3><ul class="list-clean" style="margin-top:8px"><li>Modo Bot + agentes o Solo bot.</li><li>Transferencia a departamento o agente.</li><li>Prioridad y mensaje de transferencia.</li><li>El ticket conserva el contexto del chat.</li></ul></div>
        <div class="card"><h3>Ventana del bot</h3><ul class="list-clean" style="margin-top:8px"><li>De 1 a 1.440 minutos.</li><li>Se pausa al transferir y reanuda al vencer.</li><li>Por conexión: mensaje de fallback y de transferencia.</li><li>Un número solo puede tener un bot; un bot puede tener varias conexiones.</li></ul></div>
        <div class="card"><h3>Observabilidad</h3><ul class="list-clean" style="margin-top:8px"><li>Logs por ejecución y por flujo.</li><li>Fallbacks, transferencias y errores.</li><li>Trazabilidad de nodos ejecutados.</li><li>Reportes de rendimiento del bot.</li></ul></div>
      </div>
      <div class="slide-footer"><span>BPONET SAS</span><div class="rule"></div><span>Wagent · Presentación comercial</span><span>24</span></div>
    </section>
'''

# Insertar el bloque de bots después de la diapositiva de automatizaciones.
marker = '<section class="slide" data-title="Automatización">'
start = html.index(marker)
end = html.index('</section>', start) + len('</section>')
html = html[:end] + '\n' + bot_block + html[end:]


app_block = '''
    <!-- 26 PLANTILLAS LOCALES -->
    <section class="slide" data-title="Plantillas locales">
      <div class="slide-header">
        <div>
          <div class="kicker">Contenido</div>
          <h2 class="slide-title">Plantillas locales: texto reutilizable sin aprobación</h2>
          <p class="slide-subtitle">Para respuestas y campañas dentro de la conversación. No reemplazan a las plantillas aprobadas de Meta.</p>
        </div>
        <div class="slide-number">26 / 37</div>
      </div>
      <div class="content grid-2-1">
        <div class="browser">
          <div class="browser-bar"><span class="browser-dot"></span><span class="browser-dot"></span><span class="browser-dot"></span><div class="browser-url">wagent.bponet.com.co/pages/local-templates</div></div>
          <img src="assets/screens/local-templates.png" alt="Plantillas locales de solo texto con variables" />
        </div>
        <div>
          <div class="card" style="margin-bottom:10px"><h3>Qué son</h3><p>Nombre, cuerpo de texto y variables como <span class="code">{{nombre}}</span>. Solo texto: sin encabezado, media, botones ni categoría de Meta.</p></div>
          <div class="card green" style="margin-bottom:10px"><h3>Cuándo se pueden usar</h3><p>En API, dentro de la ventana de 24 h desde la última respuesta del cliente. En QR se envían como texto de la sesión. Fuera de la ventana usa una plantilla Meta aprobada.</p></div>
          <div class="card"><h3>Dónde se usan</h3><p>Difusiones en modo Plantilla local y en el bot con Enviar plantilla → Plantilla local (conexiones API). Las variables se reemplazan por contacto o por el flujo.</p></div>
        </div>
      </div>
      <div class="slide-footer"><span>BPONET SAS</span><div class="rule"></div><span>Wagent · Presentación comercial</span><span>26</span></div>
    </section>

    <!-- 27 DEPARTAMENTOS -->
    <section class="slide" data-title="Departamentos">
      <div class="slide-header">
        <div>
          <div class="kicker">Equipo</div>
          <h2 class="slide-title">Departamentos: ordenan el equipo y el enrutamiento</h2>
          <p class="slide-subtitle">Crea equipos, asigna agentes y define cómo se reparten las conversaciones de cada conexión.</p>
        </div>
        <div class="slide-number">27 / 37</div>
      </div>
      <div class="content grid-2-1">
        <div class="browser">
          <div class="browser-bar"><span class="browser-dot"></span><span class="browser-dot"></span><span class="browser-dot"></span><div class="browser-url">wagent.bponet.com.co/pages/departments</div></div>
          <img src="assets/screens/departments.png" alt="Departamentos con reglas de distribución y agentes" />
        </div>
        <div>
          <div class="card" style="margin-bottom:10px"><h3>Crear</h3><p>Nombre, descripción, regla de distribución y agentes. La vista muestra agentes activos, conversaciones activas y carga promedio.</p></div>
          <div class="card green" style="margin-bottom:10px"><h3>Reglas</h3><ul class="list-clean" style="margin-top:5px"><li>Round-robin: turnos entre agentes.</li><li>Menos ocupado: menor carga abierta.</li><li>Ponderado: peso por agente.</li><li>Manual: el equipo toma el ticket.</li></ul></div>
          <div class="card"><h3>Conexión y transferencia</h3><p>Asigna departamentos y uno predeterminado en cada conexión. El nodo Derivar agente elige departamento o agente, prioridad y mensaje. Hasta 50 agentes por empresa.</p></div>
        </div>
      </div>
      <div class="slide-footer"><span>BPONET SAS</span><div class="rule"></div><span>Wagent · Presentación comercial</span><span>27</span></div>
    </section>

    <!-- 28 AGENTES -->
    <section class="slide" data-title="Agentes y pesos">
      <div class="slide-header">
        <div>
          <div class="kicker">Equipo</div>
          <h2 class="slide-title">Agentes, carga y pesos de distribución</h2>
          <p class="slide-subtitle">Sincroniza el equipo, controla la carga y ajusta el reparto cuando usas ponderado aleatorio.</p>
        </div>
        <div class="slide-number">28 / 37</div>
      </div>
      <div class="content grid-2-1">
        <div class="browser">
          <div class="browser-bar"><span class="browser-dot"></span><span class="browser-dot"></span><span class="browser-dot"></span><div class="browser-url">wagent.bponet.com.co/pages/departments/agents</div></div>
          <img src="assets/screens/agents.png" alt="Agentes por departamento y pesos de distribución" />
        </div>
        <div>
          <div class="card" style="margin-bottom:10px"><h3>Sincronización</h3><p>Los agentes se sincronizan desde el sistema de autenticación. Se controla su estado y pertenencia a cada departamento.</p></div>
          <div class="card green" style="margin-bottom:10px"><h3>Pesos</h3><p>Solo aplican a la regla Ponderado Aleatorio. Cada agente tiene un peso de 1 a 100: mayor peso, más conversaciones asignadas.</p></div>
          <div class="card"><h3>Acceso y control</h3><p>El agente ve las conversaciones de sus departamentos y de las conexiones asignadas. En asignación manual el sistema no elige: el ticket queda para toma del equipo.</p></div>
        </div>
      </div>
      <div class="slide-footer"><span>BPONET SAS</span><div class="rule"></div><span>Wagent · Presentación comercial</span><span>28</span></div>
    </section>

    <!-- 29 HORARIOS -->
    <section class="slide" data-title="Horarios">
      <div class="slide-header">
        <div>
          <div class="kicker">Equipo</div>
          <h2 class="slide-title">Horarios: disponibilidad y mensajes fuera de horario</h2>
          <p class="slide-subtitle">Un horario general o uno por agente. La bandeja y el bot respetan la disponibilidad configurada.</p>
        </div>
        <div class="slide-number">29 / 37</div>
      </div>
      <div class="content grid-2-1">
        <div class="browser">
          <div class="browser-bar"><span class="browser-dot"></span><span class="browser-dot"></span><span class="browser-dot"></span><div class="browser-url">wagent.bponet.com.co/pages/schedules</div></div>
          <img src="assets/screens/schedules.png" alt="Horarios generales y por agente con mensaje fuera de horario" />
        </div>
        <div>
          <div class="card" style="margin-bottom:10px"><h3>Horario general</h3><p>Zona horaria, días y franjas de inicio y fin. Se aplica a todos los agentes cuando no hay horarios individuales.</p></div>
          <div class="card green" style="margin-bottom:10px"><h3>Por agente</h3><p>Activa horarios individuales. Sin horario configurado, el agente se considera disponible 24/7. La vista muestra En horario o Fuera de horario.</p></div>
          <div class="card"><h3>Fuera de horario y bot</h3><p>Mensaje automático de hasta 500 caracteres. Los nodos Horario y Fuera de horario pueden usar el horario general y derivar o responder según disponibilidad.</p></div>
        </div>
      </div>
      <div class="slide-footer"><span>BPONET SAS</span><div class="rule"></div><span>Wagent · Presentación comercial</span><span>29</span></div>
    </section>
'''

# Insertar el bloque de la aplicación después de Difusiones.
marker = '<section class="slide" data-title="Difusiones">'
start = html.index(marker)
end = html.index('</section>', start) + len('</section>')
html = html[:end] + '\n' + app_block + html[end:]

# Eliminar la diapositiva antigua de Equipos y horarios (queda reemplazada por las tres nuevas).
marker = '<section class="slide" data-title="Equipos y horarios">'
start = html.index(marker)
start = html.rfind('<!--', 0, start) if html.rfind('<!--', 0, start) > html.rfind('</section>', 0, start) else start
end = html.index('</section>', start) + len('</section>')
html = html[:start] + html[end:]

# Renumerar encabezados y pies de diapositivas.
sections = re.split(r'(?=<section class="slide)', html)
new_sections = []
page = 0
total = sum(1 for s in sections if s.startswith('<section class="slide'))
for section in sections:
    if not section.startswith('<section class="slide'):
        new_sections.append(section)
        continue
    page += 1
    section = re.sub(r'<div class="slide-number">[^<]*</div>', f'<div class="slide-number">{page:02d} / {total}</div>', section)
    section = re.sub(
        r'(<div class="slide-footer">[\s\S]*?<span>)(\d+)(</span>\s*</div>)',
        lambda m: m.group(1) + f'{page:02d}' + m.group(3),
        section,
    )
    new_sections.append(section)

html = ''.join(new_sections)

# Agenda: reflejar la profundidad de la plataforma.
html = html.replace(
    '<li>Canvas, 43 nodos y bots por código.</li>' if '<li>Canvas, 43 nodos y bots por código.</li>' in html else '<li>Automatización visual y bots por código.</li>',
    '<li>Canvas, 43 nodos y bots por código.</li>',
)
html = html.replace(
    '<li>Equipos, horarios, métricas y consumo.</li>',
    '<li>Departamentos, agentes y horarios.</li>',
)
html = html.replace(
    '<li>Cuotas y límites según el acuerdo.</li>',
    '<li>Plantillas locales, cuotas y límites.</li>',
)

html_path.write_text(html)
print(f"Diapositivas de aplicación agregadas. Total: {total}")

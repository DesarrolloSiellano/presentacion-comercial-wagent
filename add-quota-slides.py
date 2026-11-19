from pathlib import Path
import re

root = Path(__file__).resolve().parent
html_path = root / "Wagent-Presentacion-Comercial.html"
html = html_path.read_text()

quota_block = '''
    <!-- 24 CUOTAS Y CONSUMO -->
    <section class="slide" data-title="Cuotas y consumo">
      <div class="slide-header">
        <div>
          <div class="kicker">Cuotas</div>
          <h2 class="slide-title">Cuotas y consumo: qué se mide</h2>
          <p class="slide-subtitle">Las cuotas se definen en el acuerdo con el cliente y se controlan por empresa, período y tipo de conexión.</p>
        </div>
        <div class="slide-number">24 / 30</div>
      </div>
      <div class="content">
        <div class="grid-2">
          <div class="card green">
            <h3>WhatsApp API: bolsa mensual</h3>
            <ul class="list-clean" style="margin-top:8px">
              <li>Mensajes salientes por API: texto, media y plantillas.</li>
              <li>Bolsa global mensual + bolsas por categoría: utilidad, marketing, autenticación y servicio.</li>
              <li>Los mensajes entrantes se registran como estadística; no consumen bolsa.</li>
              <li>QR no consume la bolsa de API; solo se contabiliza.</li>
            </ul>
          </div>
          <div class="card">
            <h3>Audio, conexiones y equipo</h3>
            <ul class="list-clean" style="margin-top:8px">
              <li>Bolsa mensual de audio para API.</li>
              <li>Canal de audio habilitado o deshabilitado por política.</li>
              <li>Límite de conexiones API, QR y Embedded Signup.</li>
              <li>Límite de agentes y flujos de chatbot.</li>
            </ul>
          </div>
        </div>
        <div class="card flat" style="margin-top:12px;padding:5px 10px">
          <table class="table" style="font-size:9.2px">
            <thead><tr><th>Recurso</th><th>Cómo se mide</th><th>Aplica a</th></tr></thead>
            <tbody>
              <tr><td><strong>WhatsApp API</strong></td><td>Mensajes salientes por mes.</td><td>API manual y Embedded/coexistencia.</td></tr>
              <tr><td><strong>Categorías</strong></td><td>Utilidad, marketing, autenticación y servicio.</td><td>API manual y Embedded/coexistencia.</td></tr>
              <tr><td><strong>Audio</strong></td><td>Audios salientes por mes.</td><td>API; QR solo se contabiliza.</td></tr>
              <tr><td><strong>Conexiones</strong></td><td>Sesiones activas por tipo.</td><td>API, QR y Embedded Signup.</td></tr>
              <tr><td><strong>Equipo</strong></td><td>Agentes y flujos creados.</td><td>Plataforma.</td></tr>
            </tbody>
          </table>
        </div>
        <div class="tiny" style="margin-top:8px">El período es mensual y se calcula en la zona horaria del cliente. El histórico disponible es de 12 meses.</div>
      </div>
      <div class="slide-footer"><span>BPONET SAS</span><div class="rule"></div><span>Wagent · Presentación comercial</span><span>24</span></div>
    </section>

    <!-- 25 CUOTAS SEGÚN ACUERDO -->
    <section class="slide" data-title="Cuotas según el acuerdo">
      <div class="slide-header">
        <div>
          <div class="kicker">Acuerdo</div>
          <h2 class="slide-title">Cuotas según el acuerdo y qué pasa al llegar al límite</h2>
          <p class="slide-subtitle">BPONET configura la política de cada empresa según el contrato; el cliente la consulta y solicita ampliación cuando la necesita.</p>
        </div>
        <div class="slide-number">25 / 30</div>
      </div>
      <div class="content grid-2">
        <div class="card green">
          <h3>Cómo se gestiona</h3>
          <ul class="list-clean" style="margin-top:8px">
            <li>El acuerdo define la bolsa mensual, su distribución por categoría, audio, conexiones, agentes y flujos.</li>
            <li>BPONET configura esos topes en la política de la empresa.</li>
            <li>Los cambios se aplican en la siguiente validación y la vista de uso los refleja.</li>
            <li>El cliente consulta usado, disponible, porcentaje e histórico en <strong>Uso y consumo</strong>.</li>
            <li>Las ampliaciones se solicitan a BPONET y se actualizan en el acuerdo.</li>
          </ul>
        </div>
        <div class="card">
          <h3>Qué pasa al llegar al límite</h3>
          <ul class="list-clean" style="margin-top:8px">
            <li><strong>Envío API:</strong> se bloquea con un mensaje claro de límite mensual o de categoría.</li>
            <li><strong>Difusión:</strong> se avisa si la campaña supera lo disponible; los mensajes que exceden fallan y quedan en el log.</li>
            <li><strong>Audio:</strong> se bloquea si el canal está deshabilitado o se alcanza la bolsa.</li>
            <li><strong>Conexiones, agentes o flujos:</strong> no se pueden crear más allá del tope.</li>
            <li><strong>QR:</strong> no consume la bolsa de API; solo se contabiliza.</li>
          </ul>
        </div>
      </div>
      <div class="card dark" style="margin-top:14px;padding:11px 16px">
        <p style="font-size:10.5px;color:#b8d7cc"><strong style="color:#fff">Sin cobros sorpresa:</strong> la cuota se define en el acuerdo y se controla antes de enviar. El cliente ve su consumo y solicita ampliación cuando la necesita.</p>
      </div>
      <div class="slide-footer"><span>BPONET SAS</span><div class="rule"></div><span>Wagent · Presentación comercial</span><span>25</span></div>
    </section>
'''

# Insertar después de la sección de Consumo y métricas
marker = '<section class="slide" data-title="Consumo y métricas">'
start = html.index(marker)
end = html.index('</section>', start) + len('</section>')
html = html[:end] + '\n' + quota_block + html[end:]

# Renumerar secciones: headers XX / 28 -> XX / 30 y footer de página
sections = re.split(r'(?=<section class="slide)', html)
new_sections = []
page = 0
for section in sections:
    if not section.startswith('<section class="slide'):
        new_sections.append(section)
        continue
    page += 1
    # Header: XX / 28 -> XX / 30
    section = re.sub(r'(\d+)\s*/\s*28', f'{page:02d} / 30', section)
    # Footer: último <span>NN</span> dentro de .slide-footer
    def repl_footer(m):
        return m.group(1) + f'{page:02d}' + m.group(3)
    section = re.sub(r'(<div class="slide-footer">[\s\S]*?<span>)(\d+)(</span>\s*</div>)', repl_footer, section)
    new_sections.append(section)

html = ''.join(new_sections)
html_path.write_text(html)
print(f'quota slides inserted; total sections: {page}')

from pathlib import Path

root = Path(__file__).resolve().parent
html_path = root / "Wagent-Presentacion-Comercial.html"
html = html_path.read_text()

new_block = '''    <!-- 03 DIVIDER CONEXIÓN -->
    <section class="slide divider" data-title="Parte 1 — Conexión">
      <div class="divider-top">
        <img src="assets/logo-bponet-white.png" alt="BPO NET" />
        <div class="divider-num">PARTE 01</div>
      </div>
      <img class="divider-icon" src="assets/meta-app-icon.png" alt="Wagent app icon" />
      <div class="divider-main">
        <div class="kicker dark">BPONET · Tech Provider de Meta</div>
        <h2>Conectar WhatsApp<br /><span>tres caminos.</span></h2>
        <p>QR, API manual o Embedded Signup con coexistencia. Tú eliges; BPONET te acompaña en la conexión.</p>
      </div>
      <div class="divider-bottom"><span>BPONET SAS · Wagent</span><div class="line"></div><span>01</span></div>
    </section>

    <!-- 04 TRES CAMINOS -->
    <section class="slide" data-title="Tres caminos de conexión">
      <div class="slide-header">
        <div>
          <div class="kicker">Conexión</div>
          <h2 class="slide-title">Tres caminos para conectar WhatsApp</h2>
          <p class="slide-subtitle">Cada camino tiene requisitos y responsables distintos. Elige según tu operación, tu WABA y tu equipo técnico.</p>
        </div>
        <div class="slide-number">04 / 28</div>
      </div>
      <div class="content grid-3">
        <div class="card amber">
          <div class="icon amber">QR</div>
          <h3>QR / WhatsApp Web</h3>
          <p>La forma más rápida de empezar. No requiere app de Meta ni WABA.</p>
          <p class="small" style="margin-top:8px"><strong>Qué necesita:</strong> un teléfono con WhatsApp o WhatsApp Business, escanear el QR y mantener el teléfono conectado.</p>
          <p class="small" style="margin-top:8px"><strong>Ideal para:</strong> pilotos, equipos pequeños y operación asistida.</p>
        </div>
        <div class="card">
          <div class="icon amber">API</div>
          <h3>API manual</h3>
          <p>Conexión oficial con tu propia WABA, número y token.</p>
          <p class="small" style="margin-top:8px"><strong>Qué necesita:</strong> WABA, número registrado en Cloud API, system user token, Phone Number ID y WABA ID.</p>
          <p class="small" style="margin-top:8px"><strong>Ideal para:</strong> empresas con WABA propio y equipo técnico.</p>
        </div>
        <div class="card green">
          <div class="icon">∞</div>
          <h3>Embedded Signup + coexistencia</h3>
          <p>La vía recomendada. BPONET gestiona Meta y tú conservas la app WhatsApp Business.</p>
          <p class="small" style="margin-top:8px"><strong>Qué necesita:</strong> cuenta de Meta, WhatsApp Business app 2.24.17+ y número elegible.</p>
          <p class="small" style="margin-top:8px"><strong>Ideal para:</strong> clientes que quieren API oficial sin gestionar la app de Meta.</p>
        </div>
      </div>
      <div class="card dark" style="margin-top:14px;padding:11px 16px">
        <p style="font-size:10.5px;color:#b8d7cc"><strong style="color:#fff">Regla simple:</strong> si no tienes WABA ni equipo técnico, usa Embedded Signup + coexistencia. Si no necesitas API oficial, usa QR. Si ya tienes WABA y token, usa API manual.</p>
      </div>
      <div class="slide-footer"><span>BPONET SAS</span><div class="rule"></div><span>Wagent · Presentación comercial</span><span>04</span></div>
    </section>

    <!-- 05 QUÉ NECESITA CADA CAMINO -->
    <section class="slide" data-title="Qué necesita cada camino">
      <div class="slide-header">
        <div>
          <div class="kicker">Comparación</div>
          <h2 class="slide-title">Qué necesita el cliente en cada camino</h2>
          <p class="slide-subtitle">Antes de elegir, revisa los requisitos y quién gestiona cada pieza.</p>
        </div>
        <div class="slide-number">05 / 28</div>
      </div>
      <div class="content">
        <div class="card flat" style="padding:4px 10px">
          <table class="table" style="font-size:9.1px">
            <thead><tr><th>Requisito</th><th>QR / WhatsApp Web</th><th>API manual</th><th>Embedded + coexistencia</th></tr></thead>
            <tbody>
              <tr><td><strong>Cuenta de Meta</strong></td><td>No</td><td>Sí, para tu WABA</td><td>Sí; puede crearse en el flujo</td></tr>
              <tr><td><strong>WABA</strong></td><td>No</td><td>Propio</td><td>Se crea o convierte en el flujo</td></tr>
              <tr><td><strong>Número</strong></td><td>WhatsApp o WhatsApp Business</td><td>Registrado en Cloud API</td><td>WhatsApp Business 2.24.17+ elegible</td></tr>
              <tr><td><strong>Token</strong></td><td>No</td><td>System user token</td><td>BPONET lo intercambia</td></tr>
              <tr><td><strong>App de Meta / App Review</strong></td><td>No</td><td>El cliente los gestiona</td><td>BPONET los gestiona</td></tr>
              <tr><td><strong>Webhooks</strong></td><td>No</td><td>El cliente los configura</td><td>BPONET los configura</td></tr>
              <tr><td><strong>Plantillas oficiales</strong></td><td>No</td><td>Sí</td><td>Sí</td></tr>
              <tr><td><strong>Ideal para</strong></td><td>Pilotos y equipos pequeños</td><td>Empresas con WABA propio</td><td>Coexistencia y onboarding simple</td></tr>
            </tbody>
          </table>
        </div>
      </div>
      <div class="slide-footer"><span>BPONET SAS</span><div class="rule"></div><span>Wagent · Presentación comercial</span><span>05</span></div>
    </section>

    <!-- 06 WABA -->
    <section class="slide" data-title="Qué es el WABA">
      <div class="slide-header">
        <div>
          <div class="kicker">Conceptos clave</div>
          <h2 class="slide-title">Qué es el WABA (solo API y Embedded)</h2>
          <p class="slide-subtitle">El WABA agrupa números, plantillas, webhooks y facturación. QR no usa WABA ni Graph API.</p>
        </div>
        <div class="slide-number">06 / 28</div>
      </div>
      <div class="content">
        <div class="flow" style="justify-content:center;margin:8px 0 20px">
          <div class="flow-node meta">Business Portfolio<br /><span class="tiny">Tu empresa en Meta</span></div>
          <div class="flow-arrow">→</div>
          <div class="flow-node green">WABA / Messaging account<br /><span class="tiny">Plantillas · webhooks · facturación</span></div>
          <div class="flow-arrow">→</div>
          <div class="flow-node">Números de teléfono<br /><span class="tiny">Phone Number ID</span></div>
          <div class="flow-arrow">→</div>
          <div class="flow-node">Webhooks<br /><span class="tiny">Mensajes · estados · historial</span></div>
        </div>
        <div class="grid-4">
          <div class="card flat">
            <div class="icon meta">ID</div>
            <h3>WABA ID</h3>
            <p>Identifica la cuenta de mensajería. En API manual lo aporta el cliente; en Embedded lo gestiona BPONET.</p>
          </div>
          <div class="card flat">
            <div class="icon">#</div>
            <h3>Phone Number ID</h3>
            <p>Identifica cada número. Se usa para enviar mensajes y resolver webhooks.</p>
          </div>
          <div class="card flat">
            <div class="icon amber">🔑</div>
            <h3>Token</h3>
            <p>Credencial para Graph API. En API manual lo genera el cliente; en Embedded lo intercambia BPONET.</p>
          </div>
          <div class="card flat">
            <div class="icon blue">↺</div>
            <h3>Webhook</h3>
            <p>En API manual lo configura el cliente; en Embedded lo configura y opera BPONET.</p>
          </div>
        </div>
        <div class="card dark" style="margin-top:16px;padding:12px 16px">
          <p style="font-size:10.5px;color:#b8d7cc"><strong style="color:#fff">QR no usa WABA.</strong> Si el cliente elige QR, no hay WABA, token, webhooks ni plantillas oficiales. Para eso debe migrar a API manual o Embedded.</p>
        </div>
      </div>
      <div class="slide-footer"><span>BPONET SAS</span><div class="rule"></div><span>Wagent · Presentación comercial</span><span>06</span></div>
    </section>

    <!-- 07 QR -->
    <section class="slide" data-title="Camino 1 — QR">
      <div class="slide-header">
        <div>
          <div class="kicker amber">Camino 1</div>
          <h2 class="slide-title">QR / WhatsApp Web</h2>
          <p class="slide-subtitle">La forma más rápida de empezar, sin app de Meta, sin WABA y sin App Review.</p>
        </div>
        <div class="slide-number">07 / 28</div>
      </div>
      <div class="content grid-2">
        <div class="card amber">
          <h3>Qué necesita el cliente</h3>
          <ul class="list-clean" style="margin-top:10px">
            <li>Un teléfono con WhatsApp o WhatsApp Business app.</li>
            <li>Escanear el código QR desde Wagent.</li>
            <li>Mantener el teléfono conectado y con internet.</li>
            <li>No eliminar la sesión de WhatsApp Web.</li>
          </ul>
        </div>
        <div class="card">
          <h3>Qué obtiene y qué límites tiene</h3>
          <ul class="list-clean" style="margin-top:10px">
            <li>Bandeja, bots, difusiones con texto libre y plantillas locales.</li>
            <li>Sin webhooks oficiales ni plantillas de Meta.</li>
            <li>Depende del teléfono y de la sesión abierta.</li>
            <li>Mayor riesgo operativo para volúmenes altos.</li>
          </ul>
        </div>
      </div>
      <div class="flow" style="margin-top:16px;justify-content:center">
        <div class="flow-node green">Nueva conexión</div><div class="flow-arrow">→</div>
        <div class="flow-node">Tipo QR</div><div class="flow-arrow">→</div>
        <div class="flow-node">Escanear código</div><div class="flow-arrow">→</div>
        <div class="flow-node green">Conectar</div>
      </div>
      <div class="card dark" style="margin-top:16px;padding:12px 16px">
        <p style="font-size:10.5px;color:#b8d7cc"><strong style="color:#fff">No usa Cloud API.</strong> Si el cliente necesita plantillas oficiales, webhooks, coexistencia o escala, debe elegir API manual o Embedded Signup.</p>
      </div>
      <div class="slide-footer"><span>BPONET SAS</span><div class="rule"></div><span>Wagent · Presentación comercial</span><span>07</span></div>
    </section>

    <!-- 08 API MANUAL -->
    <section class="slide" data-title="Camino 2 — API manual">
      <div class="slide-header">
        <div>
          <div class="kicker amber">Camino 2</div>
          <h2 class="slide-title">Conexión por API manual</h2>
          <p class="slide-subtitle">Para empresas que ya tienen su propia WABA, número registrado y token de Meta.</p>
        </div>
        <div class="slide-number">08 / 28</div>
      </div>
      <div class="content grid-2">
        <div class="card">
          <h3>Qué necesita el cliente</h3>
          <ul class="list-clean" style="margin-top:10px">
            <li>WABA propia y número registrado en Cloud API.</li>
            <li>System user token con whatsapp_business_management y whatsapp_business_messaging.</li>
            <li>Phone Number ID y WABA ID.</li>
            <li>Gestionar su app de Meta, App Review si onboardea clientes y webhooks.</li>
          </ul>
        </div>
        <div class="card green">
          <h3>Qué hace Wagent</h3>
          <ul class="list-clean" style="margin-top:10px">
            <li>Conexión por API Token + Phone Number ID + WABA ID.</li>
            <li>Bandeja compartida, automatización y campañas.</li>
            <li>Plantillas oficiales, métricas e integraciones.</li>
            <li>Soporte de la plataforma; la gestión de Meta es del cliente.</li>
          </ul>
        </div>
      </div>
      <div class="flow" style="margin-top:16px;justify-content:center">
        <div class="flow-node green">Nueva conexión</div><div class="flow-arrow">→</div>
        <div class="flow-node">Tipo API</div><div class="flow-arrow">→</div>
        <div class="flow-node">Token manual</div><div class="flow-arrow">→</div>
        <div class="flow-node">API Token + Phone ID + WABA ID</div><div class="flow-arrow">→</div>
        <div class="flow-node green">Crear</div>
      </div>
      <div class="card dark" style="margin-top:16px;padding:12px 16px">
        <p style="font-size:10.5px;color:#b8d7cc"><strong style="color:#fff">Si no tienes WABA/token,</strong> no uses este camino. Usa Embedded Signup con coexistencia: BPONET gestiona Meta por ti.</p>
      </div>
      <div class="slide-footer"><span>BPONET SAS</span><div class="rule"></div><span>Wagent · Presentación comercial</span><span>08</span></div>
    </section>

    <!-- 09 EMBEDDED -->
    <section class="slide" data-title="Camino 3 — Embedded + coexistencia">
      <div class="slide-header">
        <div>
          <div class="kicker">Camino 3</div>
          <h2 class="slide-title">Embedded Signup + coexistencia</h2>
          <p class="slide-subtitle">La vía recomendada: BPONET gestiona Meta y tú conservas tu app WhatsApp Business.</p>
        </div>
        <div class="slide-number">09 / 28</div>
      </div>
      <div class="content grid-2">
        <div class="card green">
          <h3>Qué necesita el cliente</h3>
          <ul class="list-clean" style="margin-top:10px">
            <li>Cuenta de Meta o Business Portfolio (puede crearse en el flujo).</li>
            <li>WhatsApp Business app 2.24.17 o superior.</li>
            <li>Número activo y elegible para coexistencia.</li>
            <li>Aceptar compartir el historial y mantener la app abierta.</li>
          </ul>
        </div>
        <div class="card">
          <h3>Qué hace BPONET</h3>
          <ul class="list-clean" style="margin-top:10px">
            <li>App de Meta, configuración de Embedded Signup y App Review.</li>
            <li>Webhooks, tokens, suscripción al WABA y sincronización.</li>
            <li>Procesamiento de contactos, historial, echoes y account_update.</li>
            <li>Soporte técnico de la conexión.</li>
          </ul>
        </div>
      </div>
      <div class="grid-3" style="margin-top:12px">
        <div class="card flat" style="padding:10px 12px"><div class="pill">1</div><p style="margin-top:6px;font-size:9.5px"><strong>Entra a Wagent</strong><br />Conexiones → Nueva conexión.</p></div>
        <div class="card flat" style="padding:10px 12px"><div class="pill">2</div><p style="margin-top:6px;font-size:9.5px"><strong>Conectar con Meta</strong><br />Marca coexistencia.</p></div>
        <div class="card flat" style="padding:10px 12px"><div class="pill">3</div><p style="margin-top:6px;font-size:9.5px"><strong>Autoriza</strong><br />Cuenta Meta y negocio.</p></div>
        <div class="card flat" style="padding:10px 12px"><div class="pill">4</div><p style="margin-top:6px;font-size:9.5px"><strong>Número</strong><br />Selecciona tu WhatsApp Business.</p></div>
        <div class="card flat" style="padding:10px 12px"><div class="pill">5</div><p style="margin-top:6px;font-size:9.5px"><strong>Código</strong><br />Confirma en la app Business.</p></div>
        <div class="card flat" style="padding:10px 12px"><div class="pill">6</div><p style="margin-top:6px;font-size:9.5px"><strong>Sincroniza</strong><br />Acepta historial y espera.</p></div>
      </div>
      <div class="card dark" style="margin-top:10px;padding:10px 16px">
        <p style="font-size:10px;color:#b8d7cc"><strong style="color:#fff">No necesitas crear app, App Review, webhooks ni tokens.</strong> BPONET ya lo tiene resuelto.</p>
      </div>
      <div class="slide-footer"><span>BPONET SAS</span><div class="rule"></div><span>Wagent · Presentación comercial</span><span>09</span></div>
    </section>

    <!-- 10 COEXISTENCIA -->
    <section class="slide" data-title="Coexistencia">
      <div class="slide-header">
        <div>
          <div class="kicker">Camino 3b</div>
          <h2 class="slide-title">Coexistencia en detalle</h2>
          <p class="slide-subtitle">Solo aplica al camino Embedded: tú sigues usando la app WhatsApp Business y la API opera en paralelo.</p>
        </div>
        <div class="slide-number">10 / 28</div>
      </div>
      <div class="content grid-2">
        <div class="card">
          <h3>Qué se sincroniza</h3>
          <ul class="list-clean" style="margin-top:10px">
            <li><strong>Contactos:</strong> smb_app_state_sync.</li>
            <li><strong>Historial:</strong> history, hasta 180 días.</li>
            <li><strong>Echo:</strong> smb_message_echoes.</li>
            <li><strong>Ciclo de vida:</strong> account_update.</li>
            <li><strong>No soportado:</strong> grupos, efímeros, view once, listas, llamadas.</li>
          </ul>
          <div class="badge-row"><span class="pill">20 mps</span><span class="pill amber">Companion unlink</span><span class="pill blue">Webhooks</span></div>
        </div>
        <div class="card green">
          <h3>Qué cambia para ti</h3>
          <ul class="list-clean" style="margin-top:10px">
            <li>Sigues respondiendo desde la app WhatsApp Business.</li>
            <li>Tus agentes también responden desde Wagent.</li>
            <li>Los mensajes de la app se reflejan en la bandeja.</li>
            <li>La sincronización debe iniciar dentro de las 24 h.</li>
            <li>BPONET procesa webhooks e historial.</li>
          </ul>
        </div>
      </div>
      <div class="card dark" style="margin-top:16px;padding:12px 16px">
        <p style="font-size:10.5px;color:#b8d7cc"><strong style="color:#fff">Ventana crítica:</strong> si la sincronización no se inicia en 24 h, el cliente debe offboardear y repetir el flujo. BPONET acompaña el proceso.</p>
      </div>
      <div class="slide-footer"><span>BPONET SAS</span><div class="rule"></div><span>Wagent · Presentación comercial</span><span>10</span></div>
    </section>

    <!-- 11 WEBHOOKS -->
    <section class="slide" data-title="Webhooks y sincronización">
      <div class="slide-header">
        <div>
          <div class="kicker">Detrás de escena</div>
          <h2 class="slide-title">Webhooks y sincronización</h2>
          <p class="slide-subtitle">Aplica a API manual y Embedded. QR no usa webhooks. En Embedded, BPONET lo configura y opera por ti.</p>
        </div>
        <div class="slide-number">11 / 28</div>
      </div>
      <div class="content">
        <div class="flow" style="justify-content:center;margin-bottom:16px">
          <div class="flow-node meta">Meta Cloud API</div><div class="flow-arrow">→</div>
          <div class="flow-node">Webhook</div><div class="flow-arrow">→</div>
          <div class="flow-node">Verify token</div><div class="flow-arrow">→</div>
          <div class="flow-node green">Cola BullMQ</div><div class="flow-arrow">→</div>
          <div class="flow-node">Procesamiento</div><div class="flow-arrow">→</div>
          <div class="flow-node">Wagent UI</div>
        </div>
        <div class="card flat" style="padding:8px 12px">
          <table class="table">
            <thead><tr><th>Evento</th><th>Qué entrega Meta</th><th>Qué ves en Wagent</th></tr></thead>
            <tbody>
              <tr><td><span class="code">messages</span></td><td>Mensajes y estados.</td><td>Bandeja, bots y métricas.</td></tr>
              <tr><td><span class="code">history</span></td><td>Historial en fases y chunks.</td><td>Conversaciones anteriores sincronizadas.</td></tr>
              <tr><td><span class="code">smb_app_state_sync</span></td><td>Contactos de la app Business.</td><td>Contactos actualizados.</td></tr>
              <tr><td><span class="code">smb_message_echoes</span></td><td>Mensajes enviados desde la app.</td><td>Espejo en la bandeja.</td></tr>
              <tr><td><span class="code">account_update</span></td><td>Offboarding / reconexión.</td><td>Estado de la conexión actualizado.</td></tr>
            </tbody>
          </table>
        </div>
        <div class="grid-2" style="margin-top:12px">
          <div class="card green" style="padding:12px 15px"><p><strong>API manual:</strong> el cliente configura y mantiene sus webhooks.</p></div>
          <div class="card" style="padding:12px 15px"><p><strong>Embedded:</strong> BPONET configura, verifica y procesa los webhooks.</p></div>
        </div>
      </div>
      <div class="slide-footer"><span>BPONET SAS</span><div class="rule"></div><span>Wagent · Presentación comercial</span><span>11</span></div>
    </section>

    <!-- 12 QUIÉN GESTIONA QUÉ -->
    <section class="slide" data-title="Quién gestiona qué">
      <div class="slide-header">
        <div>
          <div class="kicker">Responsabilidades</div>
          <h2 class="slide-title">Quién gestiona qué en cada camino</h2>
          <p class="slide-subtitle">La responsabilidad técnica cambia según el camino. BPONET siempre acompaña y da soporte.</p>
        </div>
        <div class="slide-number">12 / 28</div>
      </div>
      <div class="content">
        <div class="card flat" style="padding:4px 10px">
          <table class="table" style="font-size:9.3px">
            <thead><tr><th>Actividad</th><th>QR / WhatsApp Web</th><th>API manual</th><th>Embedded + coexistencia</th></tr></thead>
            <tbody>
              <tr><td><strong>App de Meta</strong></td><td>No aplica</td><td>Cliente</td><td>BPONET</td></tr>
              <tr><td><strong>WABA</strong></td><td>No aplica</td><td>Cliente</td><td>BPONET lo crea o convierte</td></tr>
              <tr><td><strong>Token</strong></td><td>No aplica</td><td>Cliente</td><td>BPONET lo intercambia y cifra</td></tr>
              <tr><td><strong>App Review</strong></td><td>No aplica</td><td>Cliente, si onboardea clientes</td><td>BPONET</td></tr>
              <tr><td><strong>Webhooks</strong></td><td>No aplica</td><td>Cliente</td><td>BPONET</td></tr>
              <tr><td><strong>Número</strong></td><td>WhatsApp / WhatsApp Business</td><td>Registrado en Cloud API por el cliente</td><td>WhatsApp Business elegible; BPONET lo conecta</td></tr>
              <tr><td><strong>Sincronización</strong></td><td>No aplica</td><td>Cliente + Wagent</td><td>BPONET</td></tr>
              <tr><td><strong>Soporte</strong></td><td>BPONET</td><td>BPONET (plataforma) + cliente (Meta)</td><td>BPONET</td></tr>
            </tbody>
          </table>
        </div>
        <div class="card dark" style="margin-top:12px;padding:10px 16px">
          <p style="font-size:10px;color:#b8d7cc"><strong style="color:#fff">En Embedded/coexistencia, el cliente solo autoriza.</strong> En API manual, el cliente es dueño de su app, WABA, token y webhooks. En QR no hay app de Meta.</p>
        </div>
      </div>
      <div class="slide-footer"><span>BPONET SAS</span><div class="rule"></div><span>Wagent · Presentación comercial</span><span>12</span></div>
    </section>

    <!-- 13 QUÉ CAMINO ELEGIR -->
    <section class="slide" data-title="Qué camino elegir">
      <div class="slide-header">
        <div>
          <div class="kicker">Decisión</div>
          <h2 class="slide-title">¿Qué camino elegir?</h2>
          <p class="slide-subtitle">Tres preguntas para decidir en menos de un minuto.</p>
        </div>
        <div class="slide-number">13 / 28</div>
      </div>
      <div class="content grid-2">
        <div class="grid-3" style="grid-template-columns:1fr;gap:10px">
          <div class="card flat" style="padding:12px 14px"><strong>No tengo WABA ni equipo técnico</strong><p style="margin-top:4px">Usa Embedded Signup + coexistencia. BPONET gestiona Meta.</p></div>
          <div class="card flat" style="padding:12px 14px"><strong>Ya tengo WABA, número y token</strong><p style="margin-top:4px">Usa API manual. Tú gestionas tu app de Meta y tus webhooks.</p></div>
          <div class="card flat" style="padding:12px 14px"><strong>Solo quiero probar rápido</strong><p style="margin-top:4px">Usa QR. No requiere WABA, app de Meta ni App Review.</p></div>
        </div>
        <div class="card green">
          <h3>Preguntas rápidas</h3>
          <ul class="list-clean" style="margin-top:8px">
            <li>¿QR usa WABA? No.</li>
            <li>¿API manual requiere App Review? Depende de tu app; si onboardeas clientes, sí.</li>
            <li>¿Embedded requiere App Review? No, BPONET ya lo tiene.</li>
            <li>¿Puedo migrar de QR a API? Sí, creando una nueva conexión API o Embedded.</li>
            <li>¿Puedo usar coexistencia con cualquier número? No, debe ser elegible.</li>
          </ul>
        </div>
      </div>
      <div class="card dark" style="margin-top:14px;padding:11px 16px">
        <p style="font-size:10.5px;color:#b8d7cc"><strong style="color:#fff">Checklist:</strong> cuenta de Meta (API/Embedded) · número (WhatsApp, Cloud API o Business elegible) · token/WABA (API manual) · app actualizada · aceptar historial (coexistencia).</p>
      </div>
      <div class="slide-footer"><span>BPONET SAS</span><div class="rule"></div><span>Wagent · Presentación comercial</span><span>13</span></div>
    </section>

'''

start = html.index("    <!-- 03 DIVIDER META -->") if "    <!-- 03 DIVIDER META -->" in html else html.index("    <!-- 03 DIVIDER CONEXIÓN -->")
end = html.index("    <!-- 14 DIVIDER APP -->")
html = html[:start] + new_block + html[end:]

# Agenda
html = html.replace(
    "<li>Dos formas de conectar.</li>\n            <li>Qué gestiona BPONET por ti.</li>\n            <li>Qué necesitas tú.</li>\n            <li>Embedded Signup + coexistencia.</li>\n            <li>Requisitos del número.</li>\n            <li>Segunda vía: API manual.</li>",
    "<li>Tres caminos de conexión.</li>\n            <li>Qué necesita cada camino.</li>\n            <li>QR / WhatsApp Web.</li>\n            <li>API manual.</li>\n            <li>Embedded Signup + coexistencia.</li>\n            <li>Quién gestiona qué.</li>",
)
html = html.replace(
    "<h3>Conectar con BPONET</h3>\n          <p>La vía recomendada y la segunda vía.</p>",
    "<h3>Conectar con BPONET</h3>\n          <p>QR, API manual o Embedded/coexistencia.</p>",
)

html_path.write_text(html)
print("tres caminos actualizados")

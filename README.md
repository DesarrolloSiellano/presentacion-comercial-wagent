# Presentación comercial Wagent

Carpeta con la presentación comercial del software Wagent, sus vistas reales y la guía de configuración de Meta/WhatsApp.

## Archivos

| Archivo | Descripción |
| --- | --- |
| `Wagent-Presentacion-Comercial.html` | Presentación navegable en HTML, 16:9, 37 diapositivas. |
| `Wagent-Presentacion-Comercial.pptx` | Presentación editable en PowerPoint, 37 diapositivas. |
| `Wagent-Presentacion-Comercial.pdf` | Exportación lista para compartir o imprimir, 37 páginas. |
| `GUIA-META-WHATSAPP.md` | Guía detallada de verificación, WABA, Embedded Signup, coexistencia y App Review. |
| `assets/logo-bponet.png` | Logo de BPONET. |
| `assets/logo-bponet-white.png` | Logo para fondos oscuros. |
| `assets/meta-app-icon.png` | Ícono de la app para Meta. |
| `assets/screens/` | Capturas reales de la aplicación con datos demo. |
| `capture-screenshots.mjs` | Script de Playwright para regenerar capturas. |
| `generate-pptx.py` | Script de Python para regenerar el PPTX. |

## Cómo abrir la presentación HTML

Abre `Wagent-Presentacion-Comercial.html` en Chrome, Edge o Safari. No requiere servidor.

- Avanzar: `→`, espacio o `Page Down`.
- Retroceder: `←` o `Page Up`.
- Inicio: `Home`.
- Final: `End`.
- También puedes usar los botones inferiores.

Para imprimir o guardar como PDF: `Cmd/Ctrl + P` y elige “Guardar como PDF”. Cada diapositiva se imprime en una página 16:9.

## Cómo abrir el PowerPoint

Abre `Wagent-Presentacion-Comercial.pptx` con Microsoft PowerPoint, Keynote o Google Slides. Las diapositivas son editables y usan formas, textos e imágenes nativos.

## Cómo regenerar las capturas

Con la app web corriendo en `http://localhost:4200` (o ajusta `BASE` en el script):

```bash
node presentacion-comercial-wagent/capture-screenshots.mjs
```

El script usa Playwright, intercepta la API con datos demo y guarda las imágenes en `assets/screens/`.

## Cómo regenerar el PPTX

```bash
python3 presentacion-comercial-wagent/generate-pptx.py
```

Requiere `python-pptx` y `Pillow`.

## Contenido de la presentación

1. Portada.
2. Agenda.
3. Conexión con BPONET.
4. Tres caminos de conexión: QR, API manual y Embedded/coexistencia.
5. Qué necesita cada camino.
6. Qué es el WABA (solo API y Embedded).
7. Camino 1: QR / WhatsApp Web.
8. Camino 2: conexión por API manual.
9. Camino 3: Embedded Signup + coexistencia.
10. Coexistencia en detalle.
11. Webhooks y sincronización.
12. Quién gestiona qué en cada camino.
13. Qué camino elegir.
14. La plataforma.
15. Qué es Wagent.
16. Arquitectura.
17. Dashboard.
18. Conexiones.
19. Bandeja de atención.
20. Automatizaciones: todos los flujos en un solo lugar.
21. Canvas: así se construye un bot (captura con flujo creado).
22. Qué puede hacer el bot según la conexión (API vs QR).
23. Bots por código: sandbox, límites y funciones.
24. Operación del bot: handoff, ventana, versiones y logs.
25. Campañas con plantillas.
26. Plantillas locales: texto reutilizable sin aprobación.
27. Departamentos: creación, reglas y enrutamiento.
28. Agentes, carga y pesos de distribución.
29. Horarios: disponibilidad y mensajes fuera de horario.
30. Consumo y métricas.
31. Cuotas y consumo: qué se mide.
32. Cuotas según el acuerdo y qué pasa al llegar al límite.
33. Integraciones.
34. Seguridad y cumplimiento.
35. Ventajas.
36. Casos de uso.
37. Cierre y contacto.

## Automatizaciones y bots

- **Canvas visual:** 43 nodos entre disparadores, mensajes, lógica, integraciones, datos y código. Incluye palabra clave, bienvenida, fuera de horario, evento, programación, condiciones, variables, esperas, bucles, etiquetas, salto de flujo, APIs, bases de datos, data store, consentimiento y transferencia.
- **Por conexión:** un bot puede operar en varias conexiones; cada número solo puede tener un bot. El constructor habilita los nodos según los tipos de conexión asignados.
- **API vs QR:** texto, archivos, ubicación, contacto, APIs, bases de datos, condiciones y transferencia funcionan en ambos. Plantilla, catálogo y WhatsApp Flow son exclusivos de API. En QR, botones, listas y enlace se envían como texto numerado.
- **Bots por código:** JavaScript aislado con QuickJS, sin npm, filesystem, process ni secretos. Timeout de 500 a 5.000 ms, memoria de 8 a 64 MB, hasta 30 llamadas al host, 8 HTTP y 8 de base de datos. Recursos por allowlist (credenciales, bases de datos y consentimientos).
- **Operación:** borrador/publicado, activo/inactivo, autoguardado, validación, simulador, versiones, logs, fallbacks y transferencias. Modos Bot + agentes o Solo bot, con ventana de 1 a 1.440 minutos.

## Plantillas locales

- Solo texto: nombre, cuerpo y variables como `{{nombre}}`; sin encabezado, media, botones ni categoría de Meta.
- No requieren aprobación de Meta.
- En API solo se entregan dentro de la ventana de 24 h desde la última respuesta del cliente. En QR se envían como texto de la sesión.
- Se usan en Difusiones (modo Plantilla local) y en el nodo Enviar plantilla → Plantilla local de los bots (conexiones API).
- Fuera de la ventana de 24 h se debe usar una plantilla Meta aprobada.

## Departamentos, agentes y horarios

- **Departamentos:** nombre, descripción, regla de distribución y agentes. Reglas: round-robin, menos ocupado, ponderado aleatorio y asignación manual.
- **Conexiones:** cada conexión puede tener departamentos asignados y uno predeterminado. Los agentes de esos departamentos acceden a las conversaciones.
- **Transferencia:** el nodo Derivar agente elige departamento o agente, prioridad y mensaje. Si no define departamento, se usa el predeterminado de la conexión.
- **Agentes:** sincronización desde autenticación, estado, carga y pertenencia a departamentos. Límite de 50 agentes por empresa.
- **Pesos:** solo para ponderado aleatorio; peso de 1 a 100 por agente.
- **Horarios:** general o por agente, zona horaria y franjas por día. Sin horario configurado se considera 24/7. Mensaje automático de fuera de horario de hasta 500 caracteres. Los nodos Horario y Fuera de horario pueden usar el horario general.

## Cuotas

Las cuotas se definen en el acuerdo con cada cliente y se configuran por empresa en la política del tenant:

- Bolsa mensual de WhatsApp API y distribución por categorías: utilidad, marketing, autenticación y servicio.
- Bolsa mensual de audio.
- Límite de conexiones API, QR y Embedded Signup.
- Límite de agentes y flujos de chatbot.
- Período mensual según la zona horaria del cliente; histórico de 12 meses.
- QR no consume la bolsa de API; los entrantes se registran como estadística.

La vista **Uso y consumo** muestra usado, disponible, porcentaje e histórico. BPONET configura los topes y gestiona las ampliaciones solicitadas por el cliente. Al alcanzar un límite, el sistema bloquea el envío o la creación correspondiente con un mensaje claro.

## Responsabilidades

- **BPONET (Tech Provider):** app de Meta, configuración de Embedded Signup, App Review, webhooks, tokens, sincronización y soporte técnico.
- **Cliente final (Embedded Signup/coexistencia):** cuenta de Meta, número de WhatsApp Business elegible, autorización del flujo y aceptación del historial.
- **Cliente con API manual (segunda vía):** gestiona su propia WABA, app de Meta, token, registro del número y webhooks; Wagent se conecta por API Token + Phone Number ID + WABA ID.
- **Cliente con QR:** solo necesita un teléfono con WhatsApp o WhatsApp Business y escanear el código; no usa WABA ni app de Meta.

## Nota

La presentación no incluye costos ni propuestas económicas. Está enfocada en el software, sus capacidades, la ruta de conexión con Meta y las vistas de la aplicación.

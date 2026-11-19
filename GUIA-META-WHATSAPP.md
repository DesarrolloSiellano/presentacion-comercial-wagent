# Guía de conexión WhatsApp + Wagent

Documento de apoyo para la presentación comercial y para el equipo de implementación.

## 1. Idea clave

**BPONET es Tech Provider de Meta.** La app de Meta, la configuración de Embedded Signup, los permisos avanzados, el App Review y los webhooks ya están gestionados por BPONET.

El cliente **no** tiene que crear una app en Meta, pedir permisos, pasar App Review ni configurar webhooks. Solo autoriza su cuenta y su número mediante Embedded Signup.

Hay dos vías:

| Vía | Quién gestiona Meta | Para quién |
| --- | --- | --- |
| **Embedded Signup + coexistencia** (recomendada) | BPONET | Clientes que quieren conservar su app WhatsApp Business y sumar la API. |
| **API manual** (segunda vía) | El cliente | Empresas que ya tienen su propia WABA, número y token. |

## 2. Cliente final: Embedded Signup + coexistencia

### 2.1 Qué necesita el cliente

- Cuenta de Meta o Business Portfolio (puede crearlo durante el flujo).
- WhatsApp Business app **2.24.17 o superior**.
- Número activo y elegible para coexistencia.
- Aceptar compartir el historial.
- Mantener la app abierta durante la sincronización.

### 2.2 Qué NO necesita

- Crear una app en Meta.
- Ser Tech Provider.
- Pasar App Review.
- Configurar webhooks.
- Generar tokens o servidores.

### 2.3 Pasos de conexión

1. Entrar a Wagent.
2. Ir a **WhatsApp → Conexiones → Nueva conexión**.
3. Elegir **Conectar con Meta (Embedded Signup)**.
4. Marcar **Mi número ya usa la app WhatsApp Business (coexistencia)**.
5. Iniciar sesión con la cuenta de Meta y seleccionar el negocio.
6. Seleccionar el número de WhatsApp Business.
7. Ingresar en la app WhatsApp Business el código que muestra Meta.
8. Aceptar compartir el historial.
9. Esperar la sincronización. La conexión queda activa.

### 2.4 Requisitos del número

- WhatsApp Business app 2.24.17+.
- Número activo y país soportado por Meta.
- No registrado en Cloud API con otra app.
- No bloqueado ni restringido.
- No deregistrar ni registrar manualmente antes del flujo.
- Si el número no está en WhatsApp, usar el flujo de número nuevo (Wagent lo registra con PIN).

### 2.5 Qué se sincroniza

- Contactos: `smb_app_state_sync`.
- Historial: `history`, hasta 180 días.
- Mensajes enviados desde la app: `smb_message_echoes`.
- Ciclo de vida: `account_update`.
- No soportado: grupos, efímeros, “ver una vez”, listas de difusión, llamadas.

### 2.6 Ventana de 24 horas

La sincronización de contactos e historial debe iniciar dentro de las **24 horas** posteriores al onboarding. Si no se completa, el cliente debe offboardear y repetir el flujo.

### 2.7 Preguntas frecuentes del cliente

| Situación | Causa | Qué hacer |
| --- | --- | --- |
| No veo la opción de coexistencia | Número no elegible, app vieja o ya está en Cloud API. | Revisar requisitos o usar número nuevo. |
| No llega el código | El mensaje llega a la app WhatsApp Business, no por SMS. | Revisar la app y la cuenta oficial de Facebook Business. |
| La sincronización no termina | Historial grande o app cerrada. | Mantener la app abierta y esperar; soporte BPONET. |
| ¿Tengo que hacer App Review? | No para Embedded Signup/coexistencia. | BPONET ya lo tiene. |
| Quiero mi propia WABA | Necesitas la segunda vía. | API manual: tú gestionas Meta; Wagent se conecta por token. |
| El número ya está en Cloud API | Registrado con otra app. | Offboardear o usar otro número. |

## 3. BPONET: gestión de la app de Meta

Esta sección es interna o aplica a la segunda vía. El cliente final no la ejecuta.

### 3.1 Requisitos

- Negocio verificado.
- Dominio verificado.
- App tipo Business.
- Producto WhatsApp.
- Tech Provider + Access Verification.
- Facebook Login for Business.
- Embedded Signup configurado.
- Webhook verificado.
- App Review para permisos avanzados.
- App Live.

### 3.2 Verificación de negocio

1. Meta Business Suite → Configuración → Centro de seguridad → Verificar negocio.
2. Cargar RUT, Cámara de Comercio y documentos solicitados.
3. Esperar aprobación.

### 3.3 Verificación de dominio

1. Business Settings → Brand Safety → Dominios.
2. Agregar `wagent.bponet.com.co`.
3. Verificar por DNS TXT o meta-tag.

### 3.4 App y datos básicos

- App tipo Business.
- Ícono 1024×1024 sin transparencia.
- Política de privacidad.
- Términos y condiciones.
- Instrucciones de eliminación de datos.
- Dominio `wagent.bponet.com.co`.
- URL `https://wagent.bponet.com.co/`.

### 3.5 Facebook Login for Business

Activar:

- Client OAuth Login.
- Web OAuth Login.
- Enforce HTTPS.
- Embedded Browser OAuth Login.
- Use Strict Mode for redirect URIs.
- Login with the JavaScript SDK.

Agregar dominio y redirect URI.

### 3.6 Embedded Signup

1. Crear configuración de Facebook Login for Business.
2. Variación WhatsApp Embedded Signup.
3. Producto WhatsApp Cloud API.
4. Activos WhatsApp accounts.
5. Permisos `whatsapp_business_management` y `whatsapp_business_messaging`.
6. Copiar Configuration ID a `META_ES_CONFIG_ID`.

#### v4 y v5

| Versión | Coexistencia | Extras |
| --- | --- | --- |
| v4 | Se activa con `featureType` | `featureType: 'whatsapp_business_app_onboarding'`, `sessionInfoVersion: '3'` |
| v5 | Activa por defecto | `version: 'v5'`; opt-out con `features` |

Wagent soporta ambas y normaliza `waba_id` / `messaging_account_ids`.

### 3.7 Webhooks

- Callback URL: `https://wagent.bponet.com.co/api/whatsapp/webhooks`
- Verify token: `META_VERIFY_TOKEN`.
- Campos: `messages`, `account_update`, `history`, `smb_app_state_sync`, `smb_message_echoes`.
- Suscripción por WABA: `POST /{waba_id}/subscribed_apps`.

### 3.8 App Review

Permisos:

- `whatsapp_business_messaging`
- `whatsapp_business_management`

Dos videos separados:

1. **Messaging:** la app envía un mensaje, el WhatsApp lo recibe y la respuesta vuelve.
2. **Management:** plantilla creada en WhatsApp Manager y mostrada en la app.

Además: tratamiento de datos, instrucciones para el revisor y app publicada.

### 3.9 Live

- Publicar la app.
- Data Use Checkup.
- Probar con una cuenta que no sea admin/developer/tester.
- Método de pago del cliente en WhatsApp Manager.

## 4. Segunda vía: API manual

Para empresas que ya tienen su propia WABA, número y token.

### 4.1 El cliente gestiona

- Su app de Meta y su WABA.
- App Review / Advanced Access si onboardea clientes.
- Token de usuario del sistema.
- Registro del número y webhooks.
- Acceso a los activos de su negocio.

### 4.2 Wagent le da

- Conexión por **API Token + Phone Number ID + WABA ID**.
- Bandeja compartida, automatización, campañas y métricas.
- Integraciones y seguridad multiempresa.

### 4.3 Pasos en Wagent

1. WhatsApp → Conexiones → Nueva conexión.
2. Tipo: API.
3. Método: Token manual.
4. Ingresar API Token, Phone Number ID y WABA ID.
5. Crear.

> Si el cliente no tiene WABA propio, debe usar Embedded Signup con coexistencia.

## 5. Variables de entorno

```env
META_GRAPH_VERSION=v22.0
META_VERIFY_TOKEN=...
META_APP_ID=...
META_APP_SECRET=...
META_ES_CONFIG_ID=...
META_ES_VERSION=v5
```

## 6. Checklists

### 6.1 Cliente final

- [ ] Cuenta de Meta / Business Portfolio.
- [ ] WhatsApp Business app 2.24.17+.
- [ ] Número elegible para coexistencia.
- [ ] Aceptar compartir historial.
- [ ] Mantener la app abierta durante la sincronización.

### 6.2 BPONET

- [ ] Negocio verificado.
- [ ] Dominio verificado.
- [ ] App Business + producto WhatsApp.
- [ ] Tech Provider + Access Verification.
- [ ] Facebook Login for Business.
- [ ] SDK de JavaScript activado.
- [ ] Configuration ID en `META_ES_CONFIG_ID`.
- [ ] Webhook verificado y campos suscritos.
- [ ] `META_APP_SECRET` en producción.
- [ ] App Review aprobado.
- [ ] App Live.

## 7. Errores comunes

### 7.1 Cliente

| Situación | Causa | Solución |
| --- | --- | --- |
| No aparece coexistencia | Número no elegible / app vieja / ya en Cloud API. | Revisar requisitos. |
| No llega el código | El código llega a la app Business. | Revisar la app. |
| Sincronización lenta | Historial grande. | Mantener la app abierta. |
| Número ya en Cloud API | Otra app lo registró. | Offboardear o usar otro. |

### 7.2 BPONET / segunda vía

| Error | Causa | Solución |
| --- | --- | --- |
| `META_ES_NOT_CONFIGURED` | Faltan env. | Configurar y reiniciar. |
| `META_ES_ASSETS_NOT_RESOLVED` | No se capturó WABA/número. | Esperar FINISH; revisar v4/v5. |
| `META_CODE_EXCHANGE_FAILED` | Code vencido. | Repetir el flujo. |
| `META_WABA_SUBSCRIBE_FAILED` | Token/activos. | Revisar permisos. |
| `META_TEMPLATES_UNAVAILABLE` | Token/WABA/sesión. | Revisar la sesión API y el WABA. |

## 8. Enlaces oficiales

- Embedded Signup: https://developers.facebook.com/documentation/business-messaging/whatsapp/embedded-signup/
- Coexistencia: https://developers.facebook.com/documentation/business-messaging/whatsapp/embedded-signup/onboarding-business-app-users/
- App Review: https://developers.facebook.com/docs/whatsapp/embedded-signup/app-review/
- Access Tokens: https://developers.facebook.com/documentation/business-messaging/whatsapp/access-tokens/
- Webhooks: https://developers.facebook.com/documentation/business-messaging/whatsapp/webhooks/

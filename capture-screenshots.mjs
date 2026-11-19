import { chromium } from 'playwright';
import { mkdir } from 'node:fs/promises';

const BASE = 'http://localhost:4200';
const OUT = 'presentacion-comercial-wagent/assets/screens';

const tenantConfig = {
  tenantId: 'tenant-demo',
  company: 'BPO NET Demo',
  version: 1,
  updatedAt: '2026-11-19T12:00:00.000Z',
  features: {
    whatsappIntegration: true,
    atencionSalidaMensajes: true,
    qr: true,
    coexistenceHistoryImport: true,
    codeNode: true,
    chatbotPublish: true,
    embeddedSignup: true,
  },
  channels: { whatsapp: { enabled: true, embeddedSignup: { enabled: true } } },
  limits: {
    maxWhatsappApiConnections: 5,
    maxWhatsappQrConnections: 2,
    maxWhatsappEmbeddedSignupConnections: 5,
    maxAgents: 20,
    maxChatbotFlows: 20,
  },
};

const dashboardStats = {
  kpis: {
    ticketsTotal: 128,
    ticketsOpen: 14,
    ticketsPending: 9,
    ticketsResolved: 105,
    chatsTotal: 342,
    chatsToday: 47,
    messagesTotal: 2840,
    messagesInbound: 1620,
    messagesOutbound: 1220,
    messagesBot: 640,
    agentsTotal: 8,
    agentsAvailableNow: 5,
    sessionsConnected: 3,
    sessionsTotal: 3,
    botExecutions: 890,
    botTransfers: 112,
    botFallbacks: 34,
    broadcastsTotal: 12,
    broadcastsSuccessRate: 98.4,
  },
  global: {
    ticketsTotal: 128,
    ticketsOpen: 14,
    ticketsPending: 9,
    ticketsResolved: 105,
    chatsTotal: 342,
    chatsToday: 47,
  },
  agentsPerformance: [
    { agentId: 'a1', name: 'Ana', lastName: 'Torres', availableNow: true, load: 4, resolved: 28, totalInPeriod: 32, avgFirstResponseMs: 42000, avgResolutionMs: 780000 },
    { agentId: 'a2', name: 'Carlos', lastName: 'Ríos', availableNow: true, load: 6, resolved: 24, totalInPeriod: 30, avgFirstResponseMs: 51000, avgResolutionMs: 840000 },
    { agentId: 'a3', name: 'Laura', lastName: 'Méndez', availableNow: true, load: 3, resolved: 31, totalInPeriod: 34, avgFirstResponseMs: 38000, avgResolutionMs: 720000 },
    { agentId: 'a4', name: 'Diego', lastName: 'Salazar', availableNow: false, load: 0, resolved: 22, totalInPeriod: 32, avgFirstResponseMs: 46000, avgResolutionMs: 810000 },
  ],
  volumeTrend: [
    { date: '2026-11-13', tickets: 12, messages: 180 },
    { date: '2026-11-14', tickets: 18, messages: 220 },
    { date: '2026-11-15', tickets: 15, messages: 205 },
    { date: '2026-11-16', tickets: 22, messages: 260 },
    { date: '2026-11-17', tickets: 19, messages: 240 },
    { date: '2026-11-18', tickets: 26, messages: 310 },
    { date: '2026-11-19', tickets: 24, messages: 295 },
  ],
  distribution: {
    byStatus: [
      { label: 'Abiertos', value: 14 },
      { label: 'Pendientes', value: 9 },
      { label: 'Resueltos', value: 105 },
    ],
    byPriority: [
      { label: 'Alta', value: 18 },
      { label: 'Media', value: 42 },
      { label: 'Baja', value: 68 },
    ],
    byDepartment: [
      { label: 'Ventas', value: 38 },
      { label: 'Soporte', value: 54 },
      { label: 'Cobranza', value: 22 },
      { label: 'Agendamiento', value: 14 },
    ],
    byType: [
      { label: 'Texto', value: 1800 },
      { label: 'Imagen', value: 420 },
      { label: 'Documento', value: 310 },
      { label: 'Audio', value: 210 },
      { label: 'Plantilla', value: 100 },
    ],
  },
  bot: {
    fallbackRate: 3.8,
    transferRate: 12.6,
    byFlow: [
      { flowId: 'f1', name: 'Atención al cliente', executions: 520, fallbacks: 18, transfers: 64 },
      { flowId: 'f2', name: 'Agendamiento', executions: 250, fallbacks: 8, transfers: 32 },
      { flowId: 'f3', name: 'Recuperación de carrito', executions: 120, fallbacks: 8, transfers: 16 },
    ],
  },
  sessions: [
    { id: 's1', name: 'Ventas Colombia', status: 'CONNECTED', connectionType: 'API' },
    { id: 's2', name: 'Soporte Norte', status: 'CONNECTED', connectionType: 'API' },
    { id: 's3', name: 'Recepción', status: 'CONNECTED', connectionType: 'QR' },
  ],
  broadcasts: [
    { id: 'b1', name: 'Recordatorio de citas', status: 'COMPLETED', totalMessages: 120, successfulMessages: 118, failedMessages: 2, createdAt: '2026-11-18T09:00:00.000Z' },
    { id: 'b2', name: 'Promoción Black Friday', status: 'RUNNING', totalMessages: 850, successfulMessages: 620, failedMessages: 4, createdAt: '2026-11-19T08:00:00.000Z' },
  ],
  avgFirstResponseMs: 42000,
  avgResolutionMs: 780000,
};

const sessions = [
  {
    id: 's1', name: 'Ventas Colombia', connectionType: 'API', status: 'CONNECTED', qrCode: null,
    phoneNumber: '+57 300 123 4567', apiToken: null, phoneNumberId: '109876543210',
    businessAccountId: '987654321098', onboardingType: 'EMBEDDED_SIGNUP', isCoexistence: true,
    updatedAt: '2026-11-19T14:20:00.000Z',
  },
  {
    id: 's2', name: 'Soporte Norte', connectionType: 'API', status: 'CONNECTED', qrCode: null,
    phoneNumber: '+57 601 555 0101', apiToken: null, phoneNumberId: '109876543211',
    businessAccountId: '987654321098', onboardingType: 'EMBEDDED_SIGNUP', isCoexistence: false,
    updatedAt: '2026-11-19T13:10:00.000Z',
  },
  {
    id: 's3', name: 'Recepción WhatsApp Web', connectionType: 'QR', status: 'CONNECTED', qrCode: null,
    phoneNumber: '+57 315 555 0199', apiToken: null, phoneNumberId: null, businessAccountId: null,
    onboardingType: 'MANUAL', isCoexistence: false, updatedAt: '2026-11-19T12:45:00.000Z',
  },
  {
    id: 's4', name: 'Cobranza', connectionType: 'API', status: 'CONNECTING', qrCode: null,
    phoneNumber: '+57 604 555 0202', apiToken: null, phoneNumberId: '109876543212',
    businessAccountId: '987654321098', onboardingType: 'MANUAL', isCoexistence: false,
    updatedAt: '2026-11-19T11:30:00.000Z',
  },
];

const templates = [
  { name: 'confirmacion_pedido', language: 'es_CO', category: 'UTILITY', status: 'APPROVED', bodyText: 'Hola {{1}}, tu pedido {{2}} fue confirmado y está en camino.', variableCount: 2, components: [] },
  { name: 'recordatorio_cita', language: 'es_CO', category: 'UTILITY', status: 'APPROVED', bodyText: 'Hola {{1}}, te recordamos tu cita del {{2}} a las {{3}}.', variableCount: 3, components: [] },
  { name: 'bienvenida_wagent', language: 'es_CO', category: 'MARKETING', status: 'APPROVED', bodyText: 'Hola {{1}}, bienvenido a Wagent. Estamos aquí para ayudarte.', variableCount: 1, components: [] },
  { name: 'encuesta_satisfaccion', language: 'es_CO', category: 'UTILITY', status: 'APPROVED', bodyText: 'Hola {{1}}, ¿cómo calificas la atención que recibiste hoy?', variableCount: 1, components: [] },
];

const departments = [
  { id: 'd1', name: 'Ventas', description: 'Consultas comerciales, cotizaciones y seguimiento de oportunidades.', distributionRule: 'round-robin', agents: [{ agentId: 'a1' }, { agentId: 'a2' }], currentLoad: 4, activeTicketsCount: 12 },
  { id: 'd2', name: 'Soporte', description: 'Incidentes, dudas técnicas y acompañamiento postventa.', distributionRule: 'least-busy', agents: [{ agentId: 'a3' }, { agentId: 'a4' }], currentLoad: 6, activeTicketsCount: 18 },
  { id: 'd3', name: 'Cobranza', description: 'Recordatorios de pago y acuerdos de cartera.', distributionRule: 'random-weighted', agents: [{ agentId: 'a2' }], currentLoad: 2, activeTicketsCount: 7 },
  { id: 'd4', name: 'Agendamiento', description: 'Reserva y confirmación de citas.', distributionRule: 'round-robin', agents: [{ agentId: 'a1' }, { agentId: 'a3' }], currentLoad: 3, activeTicketsCount: 9 },
];

const agents = [
  { _id: 'a1', name: 'Ana', lastName: 'Torres', email: 'ana.torres@bponet.com.co', roles: ['ADMIN'] },
  { _id: 'a2', name: 'Carlos', lastName: 'Ríos', email: 'carlos.rios@bponet.com.co', roles: ['AGENT'] },
  { _id: 'a3', name: 'Laura', lastName: 'Méndez', email: 'laura.mendez@bponet.com.co', roles: ['AGENT'] },
  { _id: 'a4', name: 'Diego', lastName: 'Salazar', email: 'diego.salazar@bponet.com.co', roles: ['AGENT'] },
];

const chats = [
  {
    id: 'c1', whatsappSessionId: 's1', contactNumber: '573001112233', contactName: 'María Gómez',
    lastMessageAt: '2026-11-19T14:32:00.000Z', botState: null,
    activeTicket: { id: 't1', chatId: 'c1', agentId: 'a1', departmentId: 'd1', status: 'OPEN', priority: 'HIGH', createdAt: '2026-11-19T14:20:00.000Z', resolvedAt: null, chat: { id: 'c1', contactName: 'María Gómez', contactNumber: '573001112233' }, department: { id: 'd1', name: 'Ventas' } },
    botMode: 'AGENT_HANDOFF', assignedFlowId: 'f1', assignedFlowName: 'Atención al cliente', botPausedAt: null, botResumeAt: null, botWindowMinutes: 30,
  },
  {
    id: 'c2', whatsappSessionId: 's2', contactNumber: '573104445566', contactName: 'Andrés Felipe Mora',
    lastMessageAt: '2026-11-19T14:18:00.000Z', botState: null,
    activeTicket: { id: 't2', chatId: 'c2', agentId: 'a3', departmentId: 'd2', status: 'PENDING', priority: 'MEDIUM', createdAt: '2026-11-19T13:50:00.000Z', resolvedAt: null, chat: { id: 'c2', contactName: 'Andrés Felipe Mora', contactNumber: '573104445566' }, department: { id: 'd2', name: 'Soporte' } },
    botMode: 'AGENT_HANDOFF', assignedFlowId: 'f1', assignedFlowName: 'Atención al cliente', botPausedAt: null, botResumeAt: null, botWindowMinutes: 30,
  },
  {
    id: 'c3', whatsappSessionId: 's1', contactNumber: '573205556677', contactName: 'Paula Restrepo',
    lastMessageAt: '2026-11-19T13:58:00.000Z', botState: null,
    activeTicket: { id: 't3', chatId: 'c3', agentId: 'a2', departmentId: 'd3', status: 'OPEN', priority: 'LOW', createdAt: '2026-11-19T13:30:00.000Z', resolvedAt: null, chat: { id: 'c3', contactName: 'Paula Restrepo', contactNumber: '573205556677' }, department: { id: 'd3', name: 'Cobranza' } },
    botMode: 'BOT_ONLY', assignedFlowId: 'f2', assignedFlowName: 'Agendamiento de citas', botPausedAt: null, botResumeAt: null, botWindowMinutes: 30,
  },
  {
    id: 'c4', whatsappSessionId: 's2', contactNumber: '573157778899', contactName: 'Jorge Iván Cárdenas',
    lastMessageAt: '2026-11-19T13:40:00.000Z', botState: null,
    activeTicket: { id: 't4', chatId: 'c4', agentId: 'a1', departmentId: 'd4', status: 'OPEN', priority: 'MEDIUM', createdAt: '2026-11-19T13:10:00.000Z', resolvedAt: null, chat: { id: 'c4', contactName: 'Jorge Iván Cárdenas', contactNumber: '573157778899' }, department: { id: 'd4', name: 'Agendamiento' } },
    botMode: 'AGENT_HANDOFF', assignedFlowId: 'f2', assignedFlowName: 'Agendamiento de citas', botPausedAt: null, botResumeAt: null, botWindowMinutes: 30,
  },
];

const messages = [
  { id: 'm1', chatId: 'c1', ticketId: 't1', sender: 'CONTACT', senderId: null, type: 'TEXT', body: 'Hola, necesito ayuda con mi pedido.', mediaUrl: null, mimeType: null, timestamp: '2026-11-19T14:28:00.000Z' },
  { id: 'm2', chatId: 'c1', ticketId: 't1', sender: 'BOT', senderId: null, type: 'TEXT', body: '¡Hola, María! Soy el asistente de Wagent. ¿En qué puedo ayudarte?', mediaUrl: null, mimeType: null, timestamp: '2026-11-19T14:28:10.000Z' },
  { id: 'm3', chatId: 'c1', ticketId: 't1', sender: 'CONTACT', senderId: null, type: 'TEXT', body: 'Quiero saber el estado de mi pedido #4582.', mediaUrl: null, mimeType: null, timestamp: '2026-11-19T14:29:00.000Z' },
  { id: 'm4', chatId: 'c1', ticketId: 't1', sender: 'AGENT', senderId: 'a1', type: 'TEXT', body: 'Claro, María. Estoy revisando el pedido #4582. Un momento, por favor.', mediaUrl: null, mimeType: null, timestamp: '2026-11-19T14:31:00.000Z' },
  { id: 'm5', chatId: 'c1', ticketId: 't1', sender: 'AGENT', senderId: 'a1', type: 'TEXT', body: 'Tu pedido ya salió del centro de distribución y llega mañana antes de las 6 p.m.', mediaUrl: null, mimeType: null, timestamp: '2026-11-19T14:32:00.000Z' },
  { id: 'm6', chatId: 'c1', ticketId: 't1', sender: 'CONTACT', senderId: null, type: 'TEXT', body: 'Perfecto, muchas gracias.', mediaUrl: null, mimeType: null, timestamp: '2026-11-19T14:32:30.000Z' },
];

const flows = [
  { id: 'f1', name: 'Atención al cliente', description: 'Clasifica la solicitud, responde preguntas frecuentes y transfiere a un agente.', isActive: true, status: 'PUBLISHED', handoffMode: 'AGENT_HANDOFF', botWindowMinutes: 30, executionMode: 'NODES', whatsappSessionIds: ['s1', 's2'], triggerKeywords: ['ayuda', 'soporte', 'pedido'], updatedAt: '2026-11-18T16:00:00.000Z', createdAt: '2026-10-01T10:00:00.000Z' },
  { id: 'f2', name: 'Agendamiento de citas', description: 'Reserva, confirma y reprograma citas sin intervención humana.', isActive: true, status: 'PUBLISHED', handoffMode: 'AGENT_HANDOFF', botWindowMinutes: 30, executionMode: 'NODES', whatsappSessionIds: ['s1'], triggerKeywords: ['cita', 'agenda', 'horario'], updatedAt: '2026-11-17T11:30:00.000Z', createdAt: '2026-10-05T09:00:00.000Z' },
  { id: 'f3', name: 'Recuperación de carrito', description: 'Contacta al cliente, resuelve dudas y comparte un enlace de pago.', isActive: true, status: 'DRAFT', handoffMode: 'BOT_ONLY', botWindowMinutes: 30, executionMode: 'NODES', whatsappSessionIds: ['s1', 's2'], triggerKeywords: ['carrito', 'compra', 'pago'], updatedAt: '2026-11-16T15:10:00.000Z', createdAt: '2026-10-20T12:00:00.000Z' },
  { id: 'f4', name: 'Encuesta de satisfacción', description: 'Mide la experiencia del cliente después de cada atención.', isActive: false, status: 'PUBLISHED', handoffMode: 'BOT_ONLY', botWindowMinutes: 30, executionMode: 'NODES', whatsappSessionIds: ['s1', 's2'], triggerKeywords: ['encuesta', 'satisfacción'], updatedAt: '2026-11-10T10:00:00.000Z', createdAt: '2026-10-25T10:00:00.000Z' },
];

const flowDetails = {
  f1: {
    ...flows[0],
    nodes: [
      { id: 'node_keyword', type: 'keyword', title: 'Palabras clave', x: 80, y: 210, data: { keywords: ['ayuda', 'soporte', 'pedido'] } },
      { id: 'node_message', type: 'send_message', title: 'Saludo', x: 380, y: 80, data: { messageText: 'Hola {{contact_name}}, soy el asistente de Wagent. ¿En qué te puedo ayudar?' } },
      { id: 'node_buttons', type: 'send_buttons', title: 'Opciones', x: 700, y: 80, data: { messageText: 'Elige una opción:', buttons: [{ id: 'btn_1', title: 'Estado de pedido' }, { id: 'btn_2', title: 'Hablar con asesor' }, { id: 'btn_3', title: 'Otro tema' }] } },
      { id: 'node_condition', type: 'condition', title: '¿Pide asesor?', x: 1010, y: 80, data: { conditionField: 'last_input', conditionValue: 'asesor' } },
      { id: 'node_transfer', type: 'transfer', title: 'Transferir a Soporte', x: 1010, y: 300, data: { departmentId: 'd2', priority: 'HIGH', transferMessage: 'Te estoy comunicando con un asesor de Soporte.' } },
      { id: 'node_end', type: 'end', title: 'Fin', x: 1310, y: 80, data: {} },
    ],
    edges: [
      { id: 'e1', sourceNodeId: 'node_keyword', targetNodeId: 'node_message' },
      { id: 'e2', sourceNodeId: 'node_message', targetNodeId: 'node_buttons' },
      { id: 'e3', sourceNodeId: 'node_buttons', targetNodeId: 'node_condition' },
      { id: 'e4', sourceNodeId: 'node_condition', targetNodeId: 'node_transfer', sourceHandle: 'false' },
      { id: 'e5', sourceNodeId: 'node_condition', targetNodeId: 'node_end', sourceHandle: 'true' },
    ],
  },
};

const agentAssignments = {
  d1: [{ agentId: 'a1', weight: 2 }, { agentId: 'a2', weight: 1 }],
  d2: [{ agentId: 'a3', weight: 1 }, { agentId: 'a4', weight: 1 }],
  d3: [{ agentId: 'a2', weight: 3 }],
  d4: [{ agentId: 'a1', weight: 1 }, { agentId: 'a3', weight: 2 }],
};

const weekSchedule = [
  { dayOfWeek: 1, startTime: '08:00', endTime: '18:00', isEnabled: true },
  { dayOfWeek: 2, startTime: '08:00', endTime: '18:00', isEnabled: true },
  { dayOfWeek: 3, startTime: '08:00', endTime: '18:00', isEnabled: true },
  { dayOfWeek: 4, startTime: '08:00', endTime: '18:00', isEnabled: true },
  { dayOfWeek: 5, startTime: '08:00', endTime: '17:00', isEnabled: true },
  { dayOfWeek: 6, startTime: '09:00', endTime: '13:00', isEnabled: true },
  { dayOfWeek: 0, startTime: '00:00', endTime: '00:00', isEnabled: false },
];

const generalSchedule = { id: 'gs1', timezone: 'America/Bogota', schedule: weekSchedule };

const agentSchedules = [
  { id: 'as1', agentId: 'a1', timezone: 'America/Bogota', schedule: weekSchedule },
  { id: 'as2', agentId: 'a2', timezone: 'America/Bogota', schedule: weekSchedule },
  { id: 'as3', agentId: 'a3', timezone: 'America/Bogota', schedule: weekSchedule },
];

const appConfiguration = {
  isOutOfOfficeEnabled: true,
  outOfOfficeMessage: 'Gracias por escribirnos. Nuestro horario es de lunes a viernes de 8:00 a 18:00. Te respondemos al abrir.',
  agentSchedulesEnabled: true,
};

const executionLogs = [
  { id: 'l1', flowId: 'f1', flowName: 'Atención al cliente', chatId: 'c1', contactNumber: '573001112233', status: 'COMPLETED', fallbackUsed: false, fallbackType: null, createdAt: '2026-11-19T14:28:00.000Z' },
  { id: 'l2', flowId: 'f2', flowName: 'Agendamiento de citas', chatId: 'c4', contactNumber: '573157778899', status: 'TRANSFERRED', fallbackUsed: false, fallbackType: null, createdAt: '2026-11-19T13:10:00.000Z' },
];

const broadcasts = [
  { id: 'b1', name: 'Recordatorio de citas - Noviembre', whatsappSessionId: 's1', message: '', category: 'utilidad', status: 'COMPLETED', totalMessages: 120, successfulMessages: 118, failedMessages: 2, createdAt: '2026-11-18T09:00:00.000Z', updatedAt: '2026-11-18T09:20:00.000Z' },
  { id: 'b2', name: 'Promoción Black Friday', whatsappSessionId: 's1', message: '', category: 'marketingComercial', status: 'RUNNING', totalMessages: 850, successfulMessages: 620, failedMessages: 4, createdAt: '2026-11-19T08:00:00.000Z', updatedAt: '2026-11-19T14:00:00.000Z' },
  { id: 'b3', name: 'Encuesta post-venta', whatsappSessionId: 's2', message: '', category: 'utilidad', status: 'DRAFT', totalMessages: 0, successfulMessages: 0, failedMessages: 0, createdAt: '2026-11-17T15:30:00.000Z', updatedAt: '2026-11-17T15:30:00.000Z' },
];

const usage = {
  period: '2026-11', tenantId: 'tenant-demo', company: 'BPO NET Demo',
  availablePeriods: ['2026-11', '2026-10'],
  whatsapp: { limit: 5000, used: 2840, remaining: 2160, percent: 56.8, unlimited: false, enabled: true },
  audio: { limit: 500, used: 120, remaining: 380, percent: 24, unlimited: false, enabled: true },
  providers: { tenant: { whatsapp: 2200, audio: 100, inbound: 1620 }, qr: { whatsapp: 640, audio: 20, inbound: 0 } },
  whatsappCategories: [
    { key: 'utilidad', limit: 3000, used: 1800, remaining: 1200, percent: 60, unlimited: false },
    { key: 'marketingComercial', limit: 1500, used: 800, remaining: 700, percent: 53.3, unlimited: false },
    { key: 'autenticacion', limit: 500, used: 240, remaining: 260, percent: 48, unlimited: false },
  ],
  embeddedSignup: { enabled: true },
  limits: {
    agents: { limit: 20, used: 8, remaining: 12, percent: 40, unlimited: false },
    chatbotFlows: { limit: 20, used: 6, remaining: 14, percent: 30, unlimited: false },
    whatsappApiConnections: { limit: 5, used: 2, remaining: 3, percent: 40, unlimited: false },
    whatsappQrConnections: { limit: 2, used: 1, remaining: 1, percent: 50, unlimited: false },
    whatsappEmbeddedSignupConnections: { limit: 5, used: 2, remaining: 3, percent: 40, unlimited: false },
  },
  features: [
    { key: 'features.codeNode', enabled: true },
    { key: 'features.coexistenceHistoryImport', enabled: true },
  ],
  general: { timezone: 'America/Bogota', locale: 'es-CO' },
  trial: { isTrial: false, trialStartedAt: null, trialEndsAt: null, daysRemaining: null, expired: false },
  history: [
    { period: '2026-10', whatsapp: 2200, audio: 90, inbound: 1400 },
    { period: '2026-09', whatsapp: 1900, audio: 80, inbound: 1250 },
  ],
};

const apiKeys = [
  { id: 'k1', name: 'Integración CRM', prefix: 'wgt_live_', scopes: ['broadcasts:write', 'flows:resume'], status: 'ACTIVE', createdAt: '2026-10-01T10:00:00.000Z', lastUsedAt: '2026-11-19T13:50:00.000Z', expiresAt: null },
  { id: 'k2', name: 'Portal de pedidos', prefix: 'wgt_live_', scopes: ['flows:resume'], status: 'ACTIVE', createdAt: '2026-10-15T09:00:00.000Z', lastUsedAt: '2026-11-18T18:20:00.000Z', expiresAt: null },
];

const dbConnections = [
  { id: 'db1', name: 'Pedidos (PostgreSQL)', engine: 'postgres', host: 'db.pedidos.internal', database: 'pedidos', status: 'CONNECTED', updatedAt: '2026-11-19T09:00:00.000Z' },
  { id: 'db2', name: 'Clientes (MongoDB)', engine: 'mongodb', host: 'mongo.clientes.internal', database: 'clientes', status: 'CONNECTED', updatedAt: '2026-11-18T16:00:00.000Z' },
];

const integrationCredentials = [
  { id: 'ic1', name: 'CRM Ventas', type: 'API_KEY', domain: 'crm.bponet.com.co', status: 'ACTIVE', updatedAt: '2026-11-15T10:00:00.000Z' },
  { id: 'ic2', name: 'ERP Facturación', type: 'BEARER', domain: 'erp.bponet.com.co', status: 'ACTIVE', updatedAt: '2026-11-12T11:00:00.000Z' },
];

const consentPolicies = [
  { id: 'cp1', name: 'Tratamiento de datos personales', key: 'privacy', version: '2026-10', status: 'ACTIVE', updatedAt: '2026-10-01T10:00:00.000Z' },
  { id: 'cp2', name: 'Comunicaciones comerciales', key: 'marketing', version: '2026-10', status: 'ACTIVE', updatedAt: '2026-10-01T10:00:00.000Z' },
];

const localTemplates = [
  { id: 'lt1', name: 'Saludo inicial', bodyText: 'Hola {{nombre}}, gracias por escribirnos. ¿En qué podemos ayudarte?', variables: ['nombre'], createdAt: '2026-10-10T10:00:00.000Z', updatedAt: '2026-11-01T10:00:00.000Z' },
  { id: 'lt2', name: 'Cierre de conversación', bodyText: 'Gracias por contactarnos, {{nombre}}. Si necesitas algo más, escríbenos nuevamente.', variables: ['nombre'], createdAt: '2026-10-12T10:00:00.000Z', updatedAt: '2026-11-02T10:00:00.000Z' },
  { id: 'lt3', name: 'Recordatorio de cita', bodyText: 'Hola {{nombre}}, te recordamos tu cita del {{fecha}} a las {{hora}}.', variables: ['nombre', 'fecha', 'hora'], createdAt: '2026-10-20T10:00:00.000Z', updatedAt: '2026-11-10T10:00:00.000Z' },
];

const contacts = [
  { id: 'ct1', name: 'María Gómez', phoneNumber: '573001112233', tags: ['cliente', 'pedido'] },
  { id: 'ct2', name: 'Andrés Felipe Mora', phoneNumber: '573104445566', tags: ['soporte'] },
  { id: 'ct3', name: 'Paula Restrepo', phoneNumber: '573205556677', tags: ['cartera'] },
];

function ok(data, extra = {}) {
  return { success: true, data, ...extra };
}

function corsHeaders(origin = 'http://localhost:4200') {
  return {
    'access-control-allow-origin': origin,
    'access-control-allow-methods': 'GET,POST,PUT,PATCH,DELETE,OPTIONS',
    'access-control-allow-headers': 'authorization,content-type',
    'access-control-max-age': '600',
  };
}

async function installMocks(page) {
  await page.route('https://app.bponet.com.co/**', async (route) => {
    const origin = route.request().headers()['origin'] || 'http://localhost:4200';
    if (route.request().method() === 'OPTIONS') {
      await route.fulfill({ status: 204, headers: corsHeaders(origin) });
      return;
    }
    await route.fulfill({ status: 200, contentType: 'application/json', body: JSON.stringify(ok(tenantConfig)) });
  });

  await page.route('http://localhost:3000/api/**', async (route) => {
    const request = route.request();
    const origin = request.headers()['origin'] || 'http://localhost:4200';
    if (request.method() === 'OPTIONS') {
      await route.fulfill({ status: 204, headers: corsHeaders(origin) });
      return;
    }

    const path = new URL(request.url()).pathname;
    let body = ok([]);

    const deptAgentsMatch = path.match(/\/departments\/([^/]+)\/agents$/);

    if (path.endsWith('/dashboard/stats')) body = ok(dashboardStats);
    else if (path.endsWith('/usage')) body = ok(usage);
    else if (path.endsWith('/agents/general-schedule')) body = ok(generalSchedule);
    else if (path.endsWith('/agents/schedules')) body = ok(agentSchedules);
    else if (path.endsWith('/configurations')) body = ok(appConfiguration);
    else if (path.endsWith('/chatbot/flows/f1')) body = ok(flowDetails.f1);
    else if (deptAgentsMatch) body = ok(agentAssignments[deptAgentsMatch[1]] || []);
    else if (path.endsWith('/whatsapp/sessions/templates')) body = ok(templates);
    else if (path.endsWith('/whatsapp/sessions/embedded-signup/config')) {
      body = ok({ appId: '1234567890', configId: '9876543210', graphVersion: 'v26.0', version: 'v5' });
    } else if (path.endsWith('/whatsapp/sessions')) body = ok(sessions);
    else if (/\/tickets\/chats\/[^/]+\/messages/.test(path)) body = ok(messages);
    else if (path.endsWith('/tickets/chats')) body = ok(chats);
    else if (path.endsWith('/departments/agents/all')) body = ok(agents);
    else if (path.endsWith('/departments/me')) body = ok(departments);
    else if (path.endsWith('/departments')) body = ok(departments);
    else if (path.endsWith('/chatbot/flows/logs')) {
      body = { success: true, data: executionLogs, total: executionLogs.length, page: 1, limit: 20 };
    } else if (path.endsWith('/chatbot/flows')) {
      body = { success: true, data: flows, total: flows.length, page: 1, limit: 20, totalPages: 1 };
    } else if (path.endsWith('/chatbot/local-templates')) body = ok(localTemplates);
    else if (path.endsWith('/chatbot/database-connections')) body = ok(dbConnections);
    else if (path.endsWith('/chatbot/integration-credentials')) body = ok(integrationCredentials);
    else if (path.endsWith('/broadcasts')) body = { success: true, data: broadcasts, total: broadcasts.length };
    else if (path.endsWith('/external-api-keys')) body = ok(apiKeys);
    else if (path.endsWith('/consents')) body = ok(consentPolicies);
    else if (path.endsWith('/legal/acceptances/status')) body = ok({ accepted: true, acceptance: null });
    else if (path.endsWith('/agents')) body = ok(agents);
    else if (path.endsWith('/contacts')) body = ok(contacts);

    await route.fulfill({ status: 200, contentType: 'application/json', headers: corsHeaders(origin), body: JSON.stringify(body) });
  });
}

async function newPage(browser) {
  const context = await browser.newContext({
    viewport: { width: 1440, height: 900 },
    deviceScaleFactor: 2,
    locale: 'es-CO',
  });

  await context.addInitScript(
    ({ config }) => {
      const state = {
        accessToken: 'demo-access-token',
        isAdmin: 'true',
        isSuperAdmin: 'false',
        tenantId: 'tenant-demo',
        company: 'BPO NET Demo',
        userName: 'Ana Torres',
        mustChangePassword: 'false',
        isNewUser: 'false',
        isTrial: 'false',
        emailVerified: 'true',
        'app-language': 'es',
      };
      for (const [key, value] of Object.entries(state)) localStorage.setItem(key, value);
      localStorage.setItem('tenantConfig', JSON.stringify(config));
      sessionStorage.setItem('selectedTenantId', 'tenant-demo');
      sessionStorage.setItem('selectedCompany', 'BPO NET Demo');
    },
    { config: tenantConfig },
  );

  const page = await context.newPage();
  await installMocks(page);
  return { context, page };
}

async function capture(page, name, url, readySelector, action) {
  await page.goto(`${BASE}${url}`, { waitUntil: 'domcontentloaded' });
  if (readySelector) {
    await page.locator(readySelector).first().waitFor({ state: 'visible', timeout: 20000 });
  }
  await page.waitForTimeout(1200);
  if (action) {
    await action(page);
    await page.waitForTimeout(800);
  }
  await page.screenshot({ path: `${OUT}/${name}.png`, fullPage: false });
  console.log(`captured ${name}`);
}

await mkdir(OUT, { recursive: true });

const browser = await chromium.launch({ headless: true });

try {
  {
    const { context, page } = await newPage(browser);
    await capture(page, 'dashboard', '/pages/dashboard', '.kpi-card');
    await context.close();
  }

  {
    const { context, page } = await newPage(browser);
    await capture(page, 'connections', '/pages/whatsapp', '.session-card');
    await page.getByRole('button', { name: 'Nueva Conexión' }).click();
    await page.locator('.p-dialog').waitFor({ state: 'visible', timeout: 10000 });
    await page.waitForTimeout(600);
    await page.screenshot({ path: `${OUT}/connection-dialog.png`, fullPage: false });
    console.log('captured connection-dialog');
    await context.close();
  }

  {
    const { context, page } = await newPage(browser);
    await capture(page, 'inbox', '/pages/tickets', '.chat-card', async (p) => {
      await p.locator('.chat-card').first().click();
      await p.locator('.message-bubble').first().waitFor({ state: 'visible', timeout: 10000 });
    });
    await context.close();
  }

  {
    const { context, page } = await newPage(browser);
    await capture(page, 'automations', '/pages/chatbot', '.flow-card');
    await context.close();
  }

  {
    const { context, page } = await newPage(browser);
    await capture(page, 'broadcasts', '/pages/notifications', 'tbody tr');
    await page.getByRole('button', { name: 'Nueva Difusión' }).click();
    await page.locator('.p-dialog').waitFor({ state: 'visible', timeout: 10000 });
    await page.locator('#name').fill('Recordatorio de citas - Noviembre');
    await page.getByRole('button', { name: 'Plantilla', exact: true }).click();
    await page.locator('.template-preview').waitFor({ state: 'visible', timeout: 10000 });
    await page.waitForTimeout(1000);
    await page.screenshot({ path: `${OUT}/broadcast-dialog.png`, fullPage: false });
    console.log('captured broadcast-dialog');
    await context.close();
  }

  {
    const { context, page } = await newPage(browser);
    await capture(page, 'departments', '/pages/departments', '.dept-card');
    await context.close();
  }

  {
    const { context, page } = await newPage(browser);
    await capture(page, 'usage', '/pages/usage', '.usage-page');
    await context.close();
  }

  {
    const { context, page } = await newPage(browser);
    await capture(page, 'api-keys', '/pages/api-keys', 'tbody tr');
    await context.close();
  }

  {
    const { context, page } = await newPage(browser);
    await capture(page, 'local-templates', '/pages/local-templates', 'tbody tr');
    await context.close();
  }

  {
    const { context, page } = await newPage(browser);
    await capture(page, 'agents', '/pages/departments/agents', '.dept-group-card');
    await context.close();
  }

  {
    const { context, page } = await newPage(browser);
    await capture(page, 'schedules-config', '/pages/schedules', '.table-card tbody tr');
    await page.locator('.table-card').scrollIntoViewIfNeeded();
    await page.waitForTimeout(600);
    await page.screenshot({ path: `${OUT}/schedules.png`, fullPage: false });
    console.log('captured schedules');
    await context.close();
  }

  {
    const { context, page } = await newPage(browser);
    await capture(page, 'bot-builder', '/pages/chatbot/builder/f1', '.canvas-board');
    await page.waitForTimeout(1000);
    await page.screenshot({ path: `${OUT}/bot-builder.png`, fullPage: false });
    console.log('captured bot-builder');
    await context.close();
  }
} finally {
  await browser.close();
}

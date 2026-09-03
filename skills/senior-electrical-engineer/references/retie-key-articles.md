# RETIE 2024 Key Articles Quick Reference (Colombia)

## Overview
RETIE = Reglamento Técnico de Instalaciones Eléctricas
**Governing resolution: Resolución MINMINAS 40117 de 2024** (Ministerio de Minas y Energía, Colombia)
Supersedes: Resolución 90708 de 2013 and Resolución 40117 de 2016 (derogadas)

> **IMPORTANTE**: La versión vigente es RETIE 2024. No citar la Resolución 90708 de 2013 como normativa vigente — fue derogada. Verificar siempre la resolución más reciente en vigor antes de diseñar o inspeccionar.

## Key Chapters and Articles

### Capítulo 1 — Generalidades
- **Art. 1**: Scope and purpose — applies to all electrical installations ≥25V AC or 60V DC
- **Art. 3**: Definitions (updated 2024 to include BESS, EVSE, microgrids, hydrogen systems)
- **Art. 4**: Safety objectives — life safety, property, continuity of service, environment

### Capítulo 2 — Requisitos para Productos
- **Art. 7**: Product certification requirements — all electrical equipment must have ONAC certification or equivalent (RETILAB-accredited lab required)
- **Art. 8**: Testing laboratories and certification bodies — ISO/IEC 17025 accreditation mandatory

### Capítulo 3 — Instalaciones Eléctricas (Core Installation Requirements)
- **Art. 11**: Grounding and bonding — SPT (sistema de puesta a tierra) design, equipotential bonding, electrode systems
- **Art. 13**: Protection against electric shock (direct and indirect contact)
- **Art. 14**: Protection against thermal effects
- **Art. 15**: Protection against overcurrents
- **Art. 16**: Low-voltage installations (<1 kV)
  - 16.1: Wiring methods
  - 16.2: Panelboards and distribution
  - 16.3: Residential installations (120/208 V; 220 V configurations)
- **Art. 17**: Medium-voltage installations (1 kV–57.5 kV)
  - 17.1: Substations — clearances, switching equipment
  - 17.2: Safety clearances (updated 2024)
  - 17.3: Protection systems — coordination, relaying

### Capítulo 4 — Protecciones
- **Art. 20**: Overcurrent protection coordination
- **Art. 21**: Ground fault protection
- **Art. 22**: Surge protection (lightning and transients) — lightning protection zones per IEC 62305
- **Art. 23**: Arc fault protection

### Capítulo 5 — Instalaciones Especiales
- **Art. 19**: Photovoltaic systems (Sistemas Fotovoltaicos y Generación Distribuida)
  - 19.1: System components and RETILAB certification
  - 19.2: Grid-tied interconnection (STR/SDL) — CREG 030/2018 net metering
  - 19.3: Off-grid and hybrid systems
  - 19.4: Safety and protection requirements — rapid shutdown, arc fault protection
- **Art. 25**: Emergency systems and backup power (UPS, gensets)
- **Art. 26**: Hazardous locations (classified areas — Zones 1/2 per IEC 60079)
- **Art. 27**: Healthcare facilities
- **Art. 28**: Data centers and critical facilities
- **Art. 38** *(RETIE 2024 addition)*: Electric vehicles and EVSE infrastructure
  - Level 2 and DCFC charger requirements
  - Bidirectional meter for V2G
  - OCPP 2.0.1 compliance for smart charging networks
- **Art. 40** *(RETIE 2024 addition)*: Battery Energy Storage Systems (BESS)
  - Fire protection and ventilation requirements
  - Disconnecting means, maintenance isolation
  - Communication protocols and monitoring

### Capítulo 6 — Inspección y Certificación
- **Art. 30**: Mandatory inspection — all installations inspected by ONAC-accredited inspector before energization
- **Art. 31**: Inspector qualifications — Ingeniero Electricista matriculado (COPNIA registration required)
- **Art. 32**: Certificate of conformity (Certificado de Conformidad de Instalación)
- **Art. 33**: Periodic inspection intervals (updated 2024)

### Anexo General (RETIE 2024)
- Updated conductor sizing tables for Colombian voltage levels
- Correction factors for altitude (Bogotá 2,600 m; Medellín 1,495 m; Cali 995 m)
- Safety clearance tables for overhead lines (updated 2024)
- Grounding electrode requirements by soil resistivity

---

## Key Colombian Regulatory Bodies & Standards

| Entity/Standard | Role |
|---|---|
| **CREG** (Comisión de Regulación de Energía y Gas) | Energy market regulation, grid connection rules |
| **UPME** (Unidad de Planeación Minero Energética) | Energy planning and self-generation registry |
| **ONAC** (Organismo Nacional de Acreditación) | Accreditation of inspection/certification bodies (ISO/IEC 17025) |
| **COPNIA** | Professional engineers registry — Matrícula Profesional required for signing plans |
| **NTC 2050** | Colombian national standard (adapted from NEC) — complementary to RETIE |
| **NTC 4552** | Photovoltaic systems — performance and safety |
| **RETILAP** | Technical regulation for lighting (indoor and public) |
| **RETILAB** | Technical regulation for testing laboratories |
| **Resolución CREG 030/2018** | Net metering for small self-generators (<100 kW) |
| **Ley 1715/2014** | Renewable energy framework and tax incentives |
| **Decreto 829/2020** | Implements Ley 1715 benefits (VAT exemption, income deduction, accelerated depreciation) |

---

## Ley 1715 Incentives (Critical for Solar/Renewable Projects in Colombia)
- **VAT Exemption**: 0% IVA on renewable energy equipment import
- **Income Tax Deduction**: 50% of investment deductible from income tax (up to 50% of annual taxable income)
- **Accelerated Depreciation**: Assets depreciated over 5 years instead of standard 20 years
- **Customs Exemption**: Import duties waived on qualifying equipment
- **Eligibility**: Self-generators and small-scale generators registered with UPME (required before claiming benefits)

---

## NEC vs. RETIE 2024 — Key Differences

| Topic | NEC (USA) | RETIE 2024 (Colombia) |
|---|---|---|
| Voltage levels | 120/240V residential; 480V industrial | 120/208V, 220V residential; 440V industrial |
| Grounding electrode | Ground rods, plates, concrete-encased (Art. 250) | SPT per Art. 11 — resistivity-based design mandatory |
| PV interconnection | IEEE 1547-2018, NEC Art. 690 | CREG 030/2018, RETIE 2024 Art. 19 |
| BESS requirements | NEC Art. 706 | RETIE 2024 Art. 40 (new) |
| EVSE requirements | NEC Art. 625 | RETIE 2024 Art. 38 (new) |
| Inspection authority | AHJ (local authority having jurisdiction) | ONAC-accredited inspector mandatory (Art. 30) |
| Product marking | UL listing preferred | RETIE certification + ONAC mark mandatory (Art. 7) |
| Documentation | Plans stamped by licensed PE | Planos firmados por Ingeniero Matriculado (COPNIA) |
| Altitude derating | Not addressed (sea-level baseline) | Explicit derating tables in Anexo General |

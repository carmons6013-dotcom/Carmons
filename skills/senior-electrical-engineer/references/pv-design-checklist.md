# Solar PV System Design Checklist

## Phase 1: Site Assessment & Data Collection
- [ ] Monthly utility bills (12 months) — kWh consumption and demand (kW)
- [ ] Utility tariff structure (flat, TOU, demand charges)
- [ ] Roof or ground area survey (tilt, azimuth, shading analysis)
- [ ] Solar irradiance data (NREL PVWatts for US; IDEAM for Colombia)
- [ ] Structural assessment (roof load capacity, ground conditions)
- [ ] Utility interconnection requirements (local utility + ISO/RTO)
- [ ] Available incentives (ITC 30% for US; Ley 1715 for Colombia)

## Phase 2: System Sizing

### Load Analysis
- Annual kWh consumption: _______ kWh/yr
- Peak demand: _______ kW
- Target offset: _______ % (100% = net zero)

### PV Array Sizing Formula
```
Array kWp = Annual kWh / (365 days × Peak Sun Hours × System Efficiency)
System Efficiency: ~78–82% (accounts for temperature, wiring, inverter losses)

US Reference PSH (avg): 4.0–6.0 hours/day (varies by location)
Colombia Reference PSH (avg): 4.5–5.5 hours/day (depends on region/altitude)
```

### Equipment Selection
- [ ] Module type: Monocrystalline / Polycrystalline / Bifacial / Thin-film
- [ ] Inverter type: String / Microinverter / Power optimizer + string / Central
- [ ] Racking system: Roof-mount / Ground-mount / Carport / BIPV
- [ ] Monitoring system: Module-level / System-level
- [ ] Battery storage: Yes / No — if yes, size per backup load and duration

## Phase 3: Electrical Design

### US — NEC Compliance Checklist (Art. 690)
- [ ] **690.7**: Max system voltage calculated per temperature coefficient (1,500V max commercial)
- [ ] **690.8**: Conductor sizing at 125% of Isc; overcurrent at 156% of Isc
- [ ] **690.11**: DC arc fault protection required for systems >80V
- [ ] **690.12**: Rapid shutdown (RSD) required for roof-mounted residential and commercial
- [ ] **690.13**: Disconnecting means — accessible and marked "PV System Disconnect"
- [ ] **690.31**: Wiring methods — USE-2 or PV wire in exposed outdoor DC wiring
- [ ] **690.47**: Grounding — comply with Art. 250; equipment grounding conductor sizing
- [ ] **Art. 706**: If BESS included — ESS compliance, ventilation, disconnect
- [ ] **Art. 710**: Stand-alone systems — if off-grid
- [ ] **UL 1741-SA**: Inverter certification for grid-tied + advanced grid support
- [ ] **IEEE 1547-2018**: Interconnection standard — anti-islanding, ride-through

### Colombia — RETIE Compliance Checklist (Art. 19)
- [ ] **RETIE Art. 19.1**: All components ONAC-certified or carry valid certification
- [ ] **RETIE Art. 19.2**: CREG 030/2018 net metering application filed with utility (autogeneradores <100kW)
- [ ] **RETIE Art. 19.3**: Off-grid systems — comply with isolation and safety requirements
- [ ] **RETIE Art. 11**: SPT (sistema de puesta a tierra) design and verification
- [ ] **NTC 4552**: Colombian PV standard compliance
- [ ] **UPME Registry**: Self-generator registration completed
- [ ] Planos firmados por Ingeniero Electricista Matriculado
- [ ] ONAC inspection scheduled before energization

## Phase 4: Interconnection & Utility Coordination

### US
- Interconnection application submitted to utility
- Anti-islanding protection verified
- Revenue-grade production meter specified
- Net Energy Metering (NEM) agreement signed

### Colombia
- Solicitud de conexión submitted to operator (OR — Operador de Red)
- Net metering (CREG 030/2018) agreement
- Medidor bidireccional installed and approved
- Contrato de uso de redes executed

## Phase 5: Economic Analysis

### US Financial Model
- Installed cost: $X/Wp (typical range: $2.50–$3.50/Wp commercial, $3.00–$4.50/Wp residential)
- Federal ITC: 30% of installed cost (per IRA 2022 through 2032)
- State incentives: Varies by state (DSIRE database)
- SREC value: Varies by state
- Simple payback: 6–10 years (commercial), 8–12 years (residential)
- 25-year NPV calculation at cost of capital

### Colombia Financial Model
- Installed cost: USD $1.20–$1.80/Wp (lower due to labor rates)
- Ley 1715 incentives: 50% income deduction, 0% IVA, accelerated depreciation
- Effective payback with Ley 1715: 4–7 years
- Electricity tariff escalation assumption: 5–8% annual (historically)
- 20-year NPV calculation

## Phase 6: Documentation Package
- [ ] Electrical single-line diagram (SLD)
- [ ] Structural/mechanical drawings
- [ ] Site plan with array layout
- [ ] String sizing calculations
- [ ] Voltage drop calculations (DC and AC)
- [ ] Short circuit current calculations
- [ ] Load calculation worksheet
- [ ] Equipment cut sheets and certifications
- [ ] Financial pro forma (TCO, ROI, NPV, IRR)
- [ ] Permit application package (US: AHJ; Colombia: municipio + ONAC inspector)

# Hydrogen Safety Reference — NFPA 2, LCOH Calculator, Fuel Cell Comparison

## Hydrogen Physical Properties (Critical for Safety Design)

| Property | Value | Comparison to Natural Gas |
|---|---|---|
| Flammability range | 4–75% vol/vol in air | NG: 5–15% — H₂ is far wider |
| Detonation range | 18–59% in air | NG: ~6–13% — H₂ detonation range much wider |
| Minimum ignition energy | 0.017 mJ | NG: 0.28 mJ — H₂ ignites with static electricity |
| Autoignition temperature | 500–571°C | NG: 482–632°C — similar |
| Flame temperature | 2,045°C (air) | NG: 1,960°C — similar |
| Diffusivity in air | 6.1 × 10⁻⁵ m²/s | NG: 1.6 × 10⁻⁵ m²/s — H₂ disperses 4× faster |
| Density (STP) | 0.090 kg/Nm³ | NG: ~0.72 kg/Nm³ — H₂ rises rapidly, key for ventilation |
| Lower heating value (LHV) | 119.9 MJ/kg / 3.0 kWh/Nm³ | NG: 50 MJ/kg — H₂ has highest gravimetric energy density |
| Higher heating value (HHV) | 141.8 MJ/kg / 3.54 kWh/Nm³ | Use HHV when comparing electrolyzer specs |

---

## NFPA 2 Separation Distances (USA)

### Hydrogen Storage (Compressed Gas)
| Quantity | From Buildings | From Property Lines | From Air Intakes |
|---|---|---|---|
| <400 scf (11 Nm³) | 5 ft (1.5 m) | 5 ft | 5 ft |
| 400–3,000 scf | 10 ft (3 m) | 10 ft | 10 ft |
| 3,000–15,000 scf | 15 ft (4.6 m) | 15 ft | 15 ft |
| >15,000 scf | 25 ft (7.6 m) | 25 ft | 25 ft |

### Hydrogen Dispensers / Fueling Stations
| Item | Separation |
|---|---|
| Dispenser to building opening | 10 ft (3 m) |
| Dispenser to property line | 5 ft (1.5 m) |
| Dispenser to combustibles | 10 ft |
| Electrolyzer to occupied building | 10 ft |

---

## Area Classification — IEC 60079 / NFPA 2

| Zone | Definition | Typical H₂ Location |
|---|---|---|
| Zone 0 | Explosive atmosphere continuously present | Inside electrolyzer cell stack, storage vessel interior |
| Zone 1 | Explosive atmosphere likely in normal operation | Within 3 m of vents, fill connections, relief valves |
| Zone 2 | Explosive atmosphere not likely, but possible if fault | Within 3–8 m of Zone 1 boundary; enclosed equipment rooms |
| Unclassified | No hazardous atmosphere expected | Beyond Zone 2, with adequate ventilation |

**Electrical equipment in classified zones must be:**
- Zone 0: Category 1G (ia intrinsic safety or equivalent)
- Zone 1: Category 2G (d, e, ia, ib certified)
- Zone 2: Category 3G (n-type, or Category 2G acceptable)

---

## Hydrogen Detection Protocol

| Detector Type | Technology | Set Points | Location |
|---|---|---|---|
| Catalytic bead (pellistor) | Oxidation on bead | 10% LEL alarm, 25% LEL emergency shutdown | Ceiling (H₂ rises) — 6 in. from ceiling |
| Electrochemical | Oxidation reaction | Low-level ppm detection | Backup confirmation sensor |
| Thermal conductivity | TC difference | Bulk concentration detection | Not for trace detection |

**Sensor placement rules:**
- H₂ rises: sensors must be at ceiling level or highest point in room
- Maximum 3 m sensor spacing (or per room — whichever is smaller)
- Auto-test required every 6 months; replace catalytic beads every 2–3 years
- Calibration gas: certified H₂/N₂ mixture at 25% LEL (1% H₂ vol/vol)

---

## LCOH Calculator Template

### Inputs
```
Electrolyzer capacity:    _____ kW (AC input)
Annual operating hours:   _____ hrs/yr (base case: 4,000 for solar; 8,000 for grid)
Stack efficiency (LHV):   _____ % (PEM: 65–70%; AEL: 63–71%)
Electricity cost:         _____ $/kWh or COP/kWh
Stack replacement cost:   _____ $ (PEM: ~$250/kW every 80,000 hrs; AEL: ~$100/kW every 120,000 hrs)
System installed cost:    _____ $/kW (PEM 2026: $800–$1,500/kW; AEL: $500–$900/kW)
WACC / discount rate:     _____ %
Project lifetime:         _____ years (typically 20 years)
```

### Calculation
```
Annual H₂ production (kg/yr) = Capacity (kW) × Hours (hrs/yr) × Efficiency_LHV / 39.4 (kWh/kg LHV)

Annual electricity cost ($) = Capacity (kW) × Hours (hrs/yr) × Electricity cost ($/kWh)

Annualized CapEx ($) = Total CapEx × [WACC × (1+WACC)^n] / [(1+WACC)^n - 1]
  where n = project lifetime years

Annual O&M ($) = 2–5% of system CapEx (electrolysis systems)

Annual stack replacement ($) = Stack cost / stack lifetime in years (interpolated)

LCOH ($/kg) = (Annualized CapEx + Annual O&M + Electricity cost + Stack replacement) / Annual H₂ production
```

### Benchmark LCOH (2026)
| Scenario | LCOH (USD/kg) |
|---|---|
| PEM + US grid (avg. $0.07/kWh) | $4.50–$6.50 |
| PEM + dedicated solar (LCOE $0.03/kWh, 25% CF) | $5.50–$8.00 |
| PEM + curtailed RE ($0.01/kWh, 20% CF) | $3.50–$5.50 |
| AEL + industrial power ($0.05/kWh) | $3.50–$5.50 |
| PEM + Colombia solar (Ley 1715, $0.025/kWh LCOE) | $3.50–$5.50 |
| DOE Hydrogen Shot target (2031) | <$1.00 |

*Note: IRA 2022 Clean Hydrogen Production Tax Credit (45V) provides $0.60–$3.00/kg depending on carbon intensity — dramatically improves US project economics*

---

## IRA 2022 — Section 45V Clean Hydrogen Production Tax Credit

| Carbon Intensity (kg CO₂e/kg H₂) | PTC ($/kg H₂) |
|---|---|
| <0.45 (near-zero) | $3.00 |
| 0.45–1.5 | $1.00 |
| 1.5–2.5 | $0.75 |
| 2.5–4.0 | $0.60 |
| >4.0 | $0.00 |

**Key requirements for 45V:**
- Must use lifecycle assessment (LCA) per DOE's GREET model to verify CI
- If using grid electricity: "3 pillars" required — additionality, deliverability, and time-matching
- Green H₂ from dedicated new solar/wind with annual matching: typically <1.0 kg CO₂e/kg H₂
- Must meet PWA (prevailing wage and apprenticeship) for full credit rate

---

## Fuel Cell Comparison — Stationary Power Generation

| Parameter | PEMFC | PAFC | MCFC | SOFC |
|---|---|---|---|---|
| Operating temperature | 60–80°C | 150–200°C | 650°C | 700–1,000°C |
| Fuel (H₂ purity) | >99.97% H₂ | Reformate (CO <1%) | Reformate (CO OK) | Reformate, NG, biogas |
| Electrical efficiency (net AC) | 40–60% | 40–45% | 45–55% | 50–65% |
| CHP total efficiency | 60–75% | 75–85% | 80–90% | 80–90% |
| Start-up time | <5 min (warm); <30 min (cold) | 2–4 hours | 5–8 hours | 4–12 hours |
| Load following | Excellent (fast) | Moderate | Slow | Slow–Moderate |
| Stack life | 40,000–80,000 hrs | 80,000–100,000 hrs | 40,000–60,000 hrs | 40,000–80,000 hrs |
| Power range | 1 kW–250 kW (modular) | 400 kW–1 MW | 300 kW–2 MW | 1 kW–250 kW (modular) |
| Best application | Backup power, mobility, small CHP | Medium commercial CHP | Industrial CHP, baseload | Industrial CHP, premium efficiency |
| Key vendor examples | Plug Power, Ballard, Hydrogenics | UTC/Doosan | Fuel Cell Energy (FuelCell) | Bloom Energy, Ceres |

### Fuel Cell Grid Interconnection
- All stationary fuel cells >1 kW grid-tied: IEEE 1547-2018 (US) anti-islanding, ride-through
- UL 1741-SA certification required for fuel cell inverters (US)
- CREG 030/2018 applies to fuel cells as distributed generation in Colombia
- NFPA 853 (Standard for Installation of Stationary Fuel Cell Power Systems) governs installation

---

## Hydrogen Piping Material Selection (ASME B31.12)

| Pressure Range | Acceptable Materials | Avoid |
|---|---|---|
| <1 bar (low pressure) | Stainless steel 316L, carbon steel, HDPE | Copper (H₂ embrittlement) |
| 1–100 bar | SS 316L, duplex stainless, carbon steel (dehydrated H₂ only) | Copper, zinc-plated fittings |
| 100–700 bar | SS 316L, Inconel, carbon steel ASME SA-106 (Grade B or C) | Standard carbon steel (HIC risk) |
| Cryogenic (LH₂) | Austenitic SS (304L, 316L), aluminum alloys | Carbon steel (brittle at -253°C) |

**Hydrogen embrittlement note:** High-strength steels (>690 MPa yield) are susceptible to hydrogen embrittlement under pressure — always verify ASME B31.12 material compatibility before specifying.

---

## Hydrogen Project Permitting — Key Agencies

### USA
- **NFPA 2**: Fire code adopted by local AHJ — primary design standard
- **EPA**: Emissions permits if electrolysis uses grid power; TA Luft equivalent
- **DOT PHMSA**: If H₂ is transported via pipeline interstate — 49 CFR Part 193
- **OSHA**: 29 CFR 1910.103 — flammable liquids/gases in workplace
- **Local fire department**: Often requires pre-permit meeting for H₂ facilities

### Colombia
- **RETIE 2024 Art. 3**: Hydrogen referenced as energy carrier — follow emerging MMES guidance
- **Ministerio de Minas y Energía (MMES)**: National hydrogen strategy "Colombia Hidrógeno" (2021)
- **ANLA**: Licencia Ambiental if generation >1 MW or significant land disturbance
- **Bomberos / IDIGER (Bogotá)**: Fire safety approval for H₂ storage
- **CREG**: If exporting electricity from fuel cell to grid — standard generator connection rules apply

# FAT/SAT Detailed Checklists — Pass/Fail Criteria

## Instrument Calibration Requirements (All FAT/SAT)
All test instruments must have valid calibration certificates traceable to NIST (USA) or ONAC (Colombia), with calibration date within 12 months.

| Instrument | Test | Calibration Required |
|---|---|---|
| Digital Megohmmeter | Insulation resistance | Yes — within 12 months |
| High-voltage AC/DC test set | Dielectric withstand | Yes — within 12 months |
| Micro-ohmmeter / DLRO | Contact/winding resistance | Yes — within 12 months |
| Power analyzer (Class A) | Power quality, losses | Yes — IEC 61000-4-30 |
| Doble M4100 / Megger BITE | Insulation power factor | Yes — within 6 months |
| Relay test set (OMICRON CMC) | Protection relay testing | Yes — within 12 months |
| Calibrated load bank | Generator load test | Yes — within 12 months |
| Calibrated luxmeter | Lighting verification | Yes — within 12 months |

---

## MV/LV Switchgear — Acceptance Criteria

| Test | Acceptance Criterion | Failure Action |
|---|---|---|
| Insulation resistance (IR) | ≥1,000 MΩ at 5 kV (new equipment) | Dry or investigate moisture — do not energize |
| High-potential (AC) | Withstand per IEC 62271-200; no flashover | Replace insulation — return to manufacturer |
| Contact resistance | ≤100 µΩ per pole (typical); compare to manufacturer baseline ±20% | Re-torque or replace contact |
| Relay trip test — 50 (instantaneous) | Trips within 1 cycle at 2× pickup | Recalibrate relay; verify CT ratios |
| Relay trip test — 51 (TOC) | TCC curve within ±10% of characteristic | Recalibrate; verify time dial setting |
| Mechanical operations | 5 close-open cycles without binding | Lubricate per manufacturer; replace mechanism if recurring |
| Racking mechanism | Smooth operation in all positions (connected, test, withdrawn) | Adjust cam/racking drive |
| Partial discharge (PD) | ≤10 pC at 1.1× operating voltage | Investigate corona source; reject if >10 pC |
| Interlock verification | ALL interlocks prevent unauthorized operation | Rework wiring/mechanical interlock before energizing |

---

## Power Transformer — Acceptance Criteria

| Test | Acceptance Criterion | Failure Action |
|---|---|---|
| Turns ratio (TTR) | All taps within ±0.5% of design ratio | Reject or investigate winding shorts |
| Winding resistance | Within ±3% of factory baseline (same temperature) | Investigate loose connection or shorted turns |
| Impedance (%Z) | Nameplate ±7.5% | Flag for relay coordination re-check |
| No-load losses | Within ±10% of nameplate | Core damage suspected — thermal imaging |
| Insulation power factor (tan-δ) | <0.5% (mineral oil, new); flag if >1% | Investigate oil contamination or insulation aging |
| Oil dielectric strength | ≥30 kV (IEC 60156) for new oil | Filter or replace oil |
| DGA (dissolved gas analysis) | H₂ <100 ppm; C₂H₂ = 0 (no arcing); CO/CO₂ ratio <4 | Investigate thermal fault or arcing if exceeded |
| OLTC drive test | Completes 3 full cycles without mechanical fault | Service OLTC; replace drive motor if required |

---

## UPS System — Acceptance Criteria

| Test | Acceptance Criterion | Failure Action |
|---|---|---|
| Static bypass transfer | ≤4 ms (online double-conversion) or per spec | Adjust static switch timing; replace thyristors if needed |
| Output voltage regulation | Rated voltage ±2% at 0%, 50%, 100% load | Adjust output transformer or feedback loop |
| Output frequency (inverter mode) | 60 Hz ±0.1% (USA); 60 Hz (Colombia, varies by region) | Recalibrate frequency control |
| Output THD (linear load) | ≤3% VTHD | Tune output filter or replace PWM IGBT driver |
| Battery autonomy at rated load | ≥specified minutes to 1.67 V/cell EOD | Inspect battery capacity; replace weak strings |
| Overload protection | 125% for 1 min — alarm; 150% for 10 s — bypass | Verify current limit settings in DSP controller |
| EPO (Emergency Power Off) | Shuts down within 100 ms on activation | Rewire EPO circuit; test all EPO stations |

---

## Generator / Genset — Acceptance Criteria (Per NFPA 110)

| Test | Acceptance Criterion | Failure Action |
|---|---|---|
| No-load voltage | Rated ±2% | Adjust AVR (automatic voltage regulator) |
| No-load frequency | Rated ±2% | Adjust governor speed droop |
| Overspeed shutdown | Trips at 115% rated speed | Adjust overspeed relay setpoint |
| Block load — 100% step | Voltage dip ≤15%; recovery ≤10 s | Adjust AVR transient gain; verify engine governor |
| Frequency dip — 100% block load | ≤5 Hz dip from rated; recovery ≤5 s | Adjust governor droop setting |
| 2-hour full-load run | Stable temperature, no faults, oil pressure within limits | Investigate if temperature continuously rises |
| Emergency start time | ≤10 s to rated voltage/frequency (NFPA 110 Level 1) | Adjust pre-heater or battery start system |
| ATS transfer time | ≤10 s from utility loss to generator at load (Level 1) | Adjust ATS timing relay |
| Fuel consumption | Within ±5% of rated BSFC at 100% load | Tune fuel injection; check injectors |

---

## SAT Final Sign-Off Checklist

Before issuing SAT completion certificate:
- [ ] All FAT punch list items closed (or formally accepted with waiver)
- [ ] Ground resistance measured and documented (<5 Ω system; <1 Ω equipment)
- [ ] Phase rotation confirmed on all 3-phase equipment
- [ ] All protective relay settings verified against approved relay coordination study
- [ ] SCADA/DCS point-to-point check 100% complete (sign off each loop)
- [ ] ATS transfer test passed under actual site conditions
- [ ] O&M manuals and as-built drawings delivered to client
- [ ] Operator training completed (sign-off sheet from qualified instructor)
- [ ] Spare parts list agreed and initial spares delivered
- [ ] Warranty start date recorded (typically begins at SAT completion)

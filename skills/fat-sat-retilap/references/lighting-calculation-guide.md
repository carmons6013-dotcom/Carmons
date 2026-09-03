# Lighting Calculation Guide

> 🇨🇴 **RETILAP** = Colombia únicamente (obligatorio por ley) | 🇺🇸 **IESNA/IES** = USA únicamente

## Core Formulas

### Lumen Method (Zonal Cavity)
Used for average illuminance in rectangular rooms.

```
Number of luminaires = (Em × A) / (n × Φ × CU × MF)

Where:
  Em  = Maintained illuminance target (lux)
  A   = Room area (m²)
  n   = Number of lamps per luminaire
  Φ   = Luminous flux per lamp (lumens)
  CU  = Coefficient of Utilization (from photometric data, function of RCR and reflectances)
  MF  = Maintenance Factor = LLD × LDD × (RSDD if applicable)
        LLD = Lamp Lumen Depreciation (LED: 0.90–0.95 at L70)
        LDD = Luminaire Dirt Depreciation (clean env: 0.90; industrial: 0.75)
```

### Room Cavity Ratio (RCR)
```
RCR = 5 × h_rc × (L + W) / (L × W)
  h_rc = Cavity height (ceiling to workplane, m)
  L, W = Room length and width (m)
```
RCR determines the Coefficient of Utilization from photometric tables.

### Point Calculation (Inverse Square Law)
For a luminaire at height h above a point P:
```
E_horizontal = I × cos³(θ) / h²
E_vertical   = I × cos²(θ) × sin(θ) / h²
  I = Intensity at angle θ (candela, from photometric report)
  θ = Angle from nadir (straight down = 0°)
  h = Mounting height above measurement plane (m)
```

### Unified Glare Rating (UGR)
Per CIE 117 / EN 12464-1:
```
UGR = 8 × log₁₀ [0.25/Lb × Σ(L² × ω / p²)]
  Lb   = Background luminance (cd/m²)
  L    = Luminance of each luminaire (cd/m²)
  ω    = Solid angle of luminaire (sr)
  p    = Guth position index
```
Acceptable values: UGR ≤ 19 (offices), ≤ 22 (industrial), ≤ 25 (rough work)

---

## DIALux Evo Workflow (Step by Step)

1. **Create project**: Set country (Colombia or USA), standard (RETILAP / IESNA)
2. **Import floor plan**: DXF/DWG from architectural drawings; set scale
3. **Define rooms**: Draw room boundaries; assign reflectances (ceiling/walls/floor)
4. **Set calculation plane**: Workplane height (office: 0.80 m; industrial: 0.85 m; road: ground level)
5. **Import luminaire**: Load manufacturer IES/LDT file (always use manufacturer photometric file, not generic)
6. **Place luminaires**: Use arrangement grid; set mounting height and orientation
7. **Set maintenance factor**: Input LLD and LDD per project environment class
8. **Run calculation**: Verify Em (average), Emin, Emax, uniformity U0 = Emin/Em
9. **Check UGR**: Add UGR calculation zone in observer direction
10. **Energy report**: Verify LPD (W/m²); compare to RETILAP Tabla 2 or ASHRAE 90.1
11. **Export**: PDF report with isolux diagrams, false-color maps, luminaire schedule

---

## RETILAP Maintenance Factor Guidelines

| Environment Class | Description | MF |
|---|---|---|
| MF-1 (Very Clean) | Office, hospital, clean room | 0.85 |
| MF-2 (Clean) | Schools, retail, light industrial | 0.80 |
| MF-3 (Normal) | General industrial, warehouses | 0.75 |
| MF-4 (Dirty) | Foundries, cement plants, agriculture | 0.65 |
| MF-5 (Very Dirty) | Mining, heavy process | 0.55 |

---

## RETILAP Minimum Illuminance Table (Selected Spaces)

| Espacio | Em (lux) | UGR máx | Ra (CRI) mín |
|---|---|---|---|
| Pasillos y escaleras | 100 | 28 | 40 |
| Archivos y salas de almacenamiento | 200 | 25 | 60 |
| Oficinas generales | 500 | 19 | 80 |
| Trabajo en computadora | 300–500 | 19 | 80 |
| Salas de conferencias | 500 | 19 | 80 |
| Salas de reuniones técnicas | 750 | 19 | 80 |
| Talleres mecánicos (grueso) | 300 | 25 | 60 |
| Talleres mecánicos (fino) | 750 | 22 | 80 |
| Salas de control | 500 | 16 | 80 |
| Plantas de manufactura (electrónica) | 1,000 | 19 | 80 |
| Zonas de carga exterior | 50 | — | 20 |
| Parqueaderos cubiertos | 75 | 28 | 40 |

---

## Road Lighting — RETILAP Classification & Requirements

| Vía | Tipo | Em (lux) | U0 (Emin/Em) | Ul (Emin/Emax) | TI (%) |
|---|---|---|---|---|---|
| Autopistas y vías primarias | V1 | 30 | ≥0.40 | ≥0.70 | ≤10 |
| Arterias principales | V2 | 20 | ≥0.40 | ≥0.60 | ≤10 |
| Vías colectoras | V3 | 15 | ≥0.35 | ≥0.50 | ≤15 |
| Vías locales residenciales | V4 | 10 | ≥0.25 | — | ≤15 |
| Vías peatonales | V5 | 5 | ≥0.25 | — | ≤25 |

TI = Threshold Increment (glare from road luminaires affecting driver vision)

### Road Lighting Pole Spacing Formula
```
S ≤ MH × (Em × W) / (Φ × CU × MF × n_sides)
  MH = Mounting height (m)
  W  = Road width (m)
  Φ  = Luminaire flux (lm)
  n_sides = 1 (single side), 2 (staggered/opposite)
```
Verify final spacing in AGi32 or DIALUX Street — always use measured photometric data.

---

## IES Illuminance Categories (USA Reference)

| Category | Illuminance Range (fc) | Application Examples |
|---|---|---|
| A | 2–5 fc | Public areas, low-activity outdoor |
| B | 5–10 fc | Simple visual tasks, walkways |
| C | 10–20 fc | Working spaces (warehousing, common areas) |
| D | 20–50 fc | Performance of visual tasks — high contrast, large size |
| E | 50–100 fc | Performance of visual tasks — medium contrast |
| F | 100–200 fc | Performance of visual tasks — low contrast or small size |
| G | 200–500 fc | Very prolonged and exacting visual tasks |
| H | 500–1000 fc | Special visual tasks (surgery, jewel inspection) |

---

## LED Specification Quick Reference

| Parameter | Specification to Require |
|---|---|
| Efficacy | ≥130 lm/W (general commercial); ≥150 lm/W (industrial/road LED 2026) |
| L70 lifetime | ≥50,000 hours at rated operating temperature |
| CRI (Ra) | ≥80 (general); ≥90 for retail, medical, art galleries |
| CCT | 3000–3500K (warm/hospitality); 4000K (office/industrial); 5700K (safety/outdoor) |
| Power factor | ≥0.90 (NEC 100) or per RETILAP requirements |
| THD (current) | ≤20% (RETILAP); ≤10% preferred for facilities with sensitive equipment |
| IP rating | IP65 minimum (outdoor); IP54 (semi-protected indoor); IP66+ (washdown areas) |
| IK rating | IK08 minimum (public areas); IK10 (high-abuse areas) |
| Operating temperature | -20°C to +50°C (standard); verify for high-altitude Colombia sites |
| Surge protection | ≥4 kV line-to-line (road/outdoor per IEC 61547) |
| Certification | RETILAP/RETILAB mark (Colombia); UL/ETL + Energy Star or DesignLights Consortium (USA) |

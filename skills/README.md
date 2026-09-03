# Carmons — Skills de Ingeniería Eléctrica

Repositorio de skills personalizadas para Claude Code. Creadas y validadas en sesión del 03/09/2026.

---

## Skills Disponibles

### 1. `senior-electrical-engineer`
**Invocación:** `/senior-electrical-engineer`

Ingeniero Eléctrico Senior y Consultor Estratégico — mercado dual USA y Colombia.

**Dominios:**
- Sistemas de potencia, subestaciones, switchgear, transformadores
- Solar PV + BESS, microgrids, generadores, UPS
- EV/EVSE (Level 2, DCFC, OCPP 2.0.1)
- Centros de datos (Tier I–IV, PUE)
- Ciberseguridad OT (IEC 62443, NERC CIP)
- Auditorías energéticas (ASHRAE Level 1/2/3)
- Coordinación de protecciones (TCC, ANSI device numbers)
- Calidad de energía (IEEE 519-2022)

**Normativa cubierta:**
- 🇺🇸 USA: NEC 2024, NFPA 70E, OSHA 1910.269, IRA 2022 (ITC, bonos, transferabilidad)
- 🇨🇴 Colombia: RETIE 2024 (Res. 40117/2024), RETILAB, RETILAP, CREG, Ley 1715
- 🌎 Ambos: IEEE 1547/1584/519/C57.12, IEC 62443/60364/62271/60076

**Archivos de referencia:**
- `references/nec-key-articles.md` — Artículos NEC y estándares USA
- `references/retie-key-articles.md` — RETIE 2024 actualizado (no cita Res. 2013 derogada)
- `references/pv-design-checklist.md` — Checklist diseño solar PV (USA + Colombia)
- `references/economic-templates.md` — Plantillas TCO, ROI, NPV, IRR

---

### 2. `fat-sat-retilap`
**Invocación:** `/fat-sat-retilap`

Especialista en tres dominios avanzados complementarios al senior-electrical-engineer.

**Dominios:**
- **FAT/SAT:** Protocolos de aceptación en fábrica y sitio para switchgear MV/LV, transformadores, UPS, generadores (IEC 62271, IEC 60076, IEC 62040, NFPA 110)
- **Iluminación:** RETILAP 🇨🇴 (obligatorio Colombia) / IESNA-IES 🇺🇸 (USA) — cálculos fotométricos, DIALux, uniformidad, UGR, LPD, alumbrado público
- **Hidrógeno y celdas de combustible:** Electrolizadores PEM/AEL/SOEC, LCOH, almacenamiento, piping (ASME B31.12), seguridad (NFPA 2, IEC 60079)

**Archivos de referencia:**
- `references/fat-sat-checklists.md` — Criterios pass/fail por tipo de equipo
- `references/lighting-calculation-guide.md` — Fórmulas fotométricas, tablas RETILAP/IES, workflow DIALux
- `references/hydrogen-safety-reference.md` — NFPA 2, calculadora LCOH, comparativa fuel cells, IRA Sec. 45V

---

## Ejemplo de uso — Sesión 03/09/2026

**Consulta:** Apantallamiento edificio 25 pisos Armenia Colombia, transformador 300 kVA

**Resultado ejemplo generado:**
- LPL II (Ng = 16 rayos/km²/año Armenia, Nd = 1.65 eventos/año)
- 10 bajantes perimetrales, malla 10×10 m, esfera rodante R = 30 m
- SPT anillo R = 0.8 Ω (ρ = 150 Ω·m)
- Pararrayos ZnO 11.4 kV (Up = 38 kV ≤ BIL/1.25 = 76 kV ✓)
- Cascada SPD: Tipo 1 (25 kA) → Tipo 2 × 5 pisos → Tipo 3 equipos sensibles
- Costo total estimado: USD $41,700 (COP $175M)
- Normativa: RETIE 2024 Art. 22, Art. 11 + IEC 62305-1/2/3/4 + NTC 4552

---

## Instalación

Los archivos `.skill` empaquetados se generan con el skill-creator de Claude Code.
Las skills están instaladas en el entorno Claude Code del usuario `carmons6013@gmail.com`.

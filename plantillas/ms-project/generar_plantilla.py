#!/usr/bin/env python3
"""Genera la plantilla de cronograma para licitaciones eléctricas.

Salidas (en la misma carpeta):
  - plantilla_licitacion_electrica.xml   -> abrir en MS Project (formato MSPDI)
  - plantilla_licitacion_electrica.xlsx  -> cronograma con fechas por fórmula

Para adaptar: edite FECHA_INICIO, TAREAS o RECURSOS y vuelva a ejecutar.
"""
import datetime as dt
from pathlib import Path
from xml.sax.saxutils import escape

from openpyxl import Workbook
from openpyxl.styles import Alignment, Border, Font, PatternFill, Side
from openpyxl.worksheet.datavalidation import DataValidation

AQUI = Path(__file__).resolve().parent
NOMBRE = "Plantilla - Licitación obra eléctrica"
FECHA_INICIO = dt.date(2027, 1, 4)  # lunes; se cambia en Project o en Excel

RECURSOS = [
    ("DIR", "Director de proyecto"),
    ("DIS", "Ingeniero diseñador"),
    ("RES", "Ingeniero residente"),
    ("SUP", "Supervisor / tecnólogo"),
    ("ELE", "Cuadrilla electricistas"),
    ("CIV", "Cuadrilla obra civil"),
    ("ADM", "Administrador / compras"),
    ("SST", "Profesional SST"),
    ("INS", "Organismo de inspección RETIE"),
]

# (clave, nivel, nombre, duración en días hábiles | None si es resumen,
#  predecesoras [claves], recursos [códigos])
TAREAS = [
    ("F1", 1, "1. INICIO Y CONTRATACIÓN", None, [], []),
    ("ADJ", 2, "Adjudicación / firma del contrato", 0, [], ["DIR"]),
    ("POL", 2, "Expedición de pólizas y garantías", 5, ["ADJ"], ["ADM"]),
    ("ACT", 2, "Acta de inicio", 0, ["POL"], ["DIR"]),
    ("ARR", 2, "Reunión de arranque, plan de calidad y plan SST", 2, ["ACT"], ["DIR", "RES", "SST"]),

    ("F2", 1, "2. INGENIERÍA Y DISEÑO", None, [], []),
    ("LEV", 2, "Visita técnica y levantamiento en sitio", 3, ["ACT"], ["DIS", "RES"]),
    ("CAR", 2, "Estudio y cuadro de cargas", 5, ["LEV"], ["DIS"]),
    ("CAL", 2, "Cálculos: regulación, cortocircuito y coordinación de protecciones", 8, ["CAR"], ["DIS"]),
    ("SPTD", 2, "Diseño SPT y SIPRA (análisis de riesgo NTC 4552)", 5, ["CAR"], ["DIS"]),
    ("ILUD", 2, "Diseño de iluminación (RETILAP)", 5, ["LEV"], ["DIS"]),
    ("PLA", 2, "Planos y memorias de cálculo", 8, ["CAL", "SPTD", "ILUD"], ["DIS"]),
    ("REV", 2, "Revisión y aprobación del diseño (cliente / interventoría)", 5, ["PLA"], ["DIR"]),
    ("DAP", 2, "HITO: Diseño aprobado", 0, ["REV"], []),

    ("F3", 1, "3. TRÁMITES ANTE OPERADOR DE RED", None, [], []),
    ("FAC", 2, "Solicitud de factibilidad / disponibilidad de punto de conexión", 15, ["LEV"], ["DIS"]),
    ("ROR", 2, "Radicación y aprobación del proyecto ante el OR", 20, ["DAP", "FAC"], ["DIS"]),
    ("OROK", 2, "HITO: Proyecto aprobado por el OR", 0, ["ROR"], []),

    ("F4", 1, "4. SUMINISTROS", None, [], []),
    ("COM", 2, "Cotización y orden de compra de materiales y equipos", 5, ["DAP"], ["ADM"]),
    ("TAB", 2, "Fabricación de tableros", 20, ["COM"], ["ADM"]),
    ("TRA", 2, "Suministro de transformador y equipos de MT", 40, ["COM"], ["ADM"]),
    ("MAT", 2, "Entrega de cable y materiales en obra", 10, ["COM"], ["ADM"]),
    ("EQOK", 2, "HITO: Equipos y materiales en obra", 0, ["TAB", "TRA", "MAT"], []),

    ("F5", 1, "5. CONSTRUCCIÓN Y MONTAJE", None, [], []),
    ("CAM", 2, "Instalación de campamento, cerramiento y señalización", 3, ["ARR"], ["SUP", "CIV"]),
    ("CIVO", 2, "Obra civil: excavación, ductos y cajas de inspección", 15, ["DAP", "CAM"], ["CIV", "SUP"]),
    ("SPT", 2, "Construcción del sistema de puesta a tierra", 5, ["CIVO"], ["ELE"]),
    ("CAN", 2, "Canalización interna (tubería, bandejas)", 15, ["DAP", "CAM"], ["ELE", "SUP"]),
    ("CAB", 2, "Tendido y conexionado de cables", 12, ["CAN", "MAT", "CIVO"], ["ELE", "SUP"]),
    ("MTAB", 2, "Montaje de tableros", 5, ["TAB", "CAN"], ["ELE"]),
    ("MSUB", 2, "Montaje de subestación / transformador", 8, ["TRA", "SPT", "OROK"], ["ELE", "RES"]),
    ("LUM", 2, "Instalación de luminarias, tomas y salidas", 10, ["CAB"], ["ELE"]),
    ("SIP", 2, "Instalación SIPRA (puntas captoras y bajantes)", 5, ["SPT"], ["ELE"]),

    ("F6", 1, "6. PRUEBAS Y PUESTA EN SERVICIO", None, [], []),
    ("PBT", 2, "Pruebas BT: aislamiento, continuidad, polaridad y SPT", 4, ["CAB", "MTAB", "SIP", "LUM"], ["RES", "ELE"]),
    ("PMT", 2, "Pruebas de equipos de MT", 3, ["MSUB"], ["RES"]),
    ("ENE", 2, "Solicitud y visita de energización del OR", 10, ["PBT", "PMT"], ["RES"]),
    ("ENOK", 2, "HITO: Energización", 0, ["ENE"], []),

    ("F7", 1, "7. CERTIFICACIÓN", None, [], []),
    ("ASB", 2, "Planos récord (as built)", 5, ["ENOK"], ["DIS"]),
    ("IRE", 2, "Inspección RETIE por organismo acreditado", 10, ["ENOK"], ["INS", "RES"]),
    ("IRL", 2, "Inspección RETILAP (si aplica)", 5, ["ENOK"], ["INS", "RES"]),
    ("CERT", 2, "HITO: Dictámenes de conformidad RETIE / RETILAP", 0, ["IRE", "IRL"], []),

    ("F8", 1, "8. ENTREGA Y CIERRE", None, [], []),
    ("CAP", 2, "Capacitación al cliente y manuales de operación y mantenimiento", 2, ["ENOK"], ["RES"]),
    ("DOS", 2, "Entrega de dossier: planos, certificados, garantías", 3, ["ASB", "CERT", "CAP"], ["DIR", "RES"]),
    ("FIN", 2, "HITO: Acta de recibo final y liquidación", 0, ["DOS"], ["DIR"]),
]


# ---------- calendario lunes-viernes ----------
def es_habil(d):
    return d.weekday() < 5


def siguiente_habil(d):
    d += dt.timedelta(days=1)
    while not es_habil(d):
        d += dt.timedelta(days=1)
    return d


def sumar_habiles(d, n):
    """Fin de una tarea de n días que empieza el día hábil d."""
    for _ in range(n - 1):
        d = siguiente_habil(d)
    return d


def primer_habil(d):
    while not es_habil(d):
        d += dt.timedelta(days=1)
    return d


def calcular_fechas():
    fechas = {}
    for clave, nivel, _n, dur, preds, _r in TAREAS:
        if dur is None:
            continue
        if preds:
            fin_max = max(fechas[p][1] for p in preds)
            if dur == 0:
                ini = fin = fin_max
            else:
                ini = siguiente_habil(fin_max)
                fin = sumar_habiles(ini, dur)
        else:
            ini = primer_habil(FECHA_INICIO)
            fin = ini if dur == 0 else sumar_habiles(ini, dur)
        fechas[clave] = (ini, fin)
    # resúmenes
    actual = None
    hijos = {}
    for clave, nivel, *_ in TAREAS:
        if nivel == 1:
            actual = clave
            hijos[clave] = []
        else:
            hijos[actual].append(clave)
    for f, hs in hijos.items():
        fechas[f] = (min(fechas[h][0] for h in hs), max(fechas[h][1] for h in hs))
    return fechas, hijos


def habiles_entre(a, b):
    n, d = 1, a
    while d < b:
        d = siguiente_habil(d)
        n += 1
    return n


# ---------- XML MSPDI ----------
def generar_xml(fechas, hijos):
    uid = {t[0]: i + 1 for i, t in enumerate(TAREAS)}
    ruid = {c: i + 1 for i, (c, _) in enumerate(RECURSOS)}
    ini_p, fin_p = fechas["F1"][0], max(v[1] for v in fechas.values())

    def ts(d, h):
        return f"{d.isoformat()}T{h}"

    def dur(dias):
        return f"PT{dias * 8}H0M0S"

    x = ['<?xml version="1.0" encoding="UTF-8" standalone="yes"?>',
         '<Project xmlns="http://schemas.microsoft.com/project">',
         "<SaveVersion>14</SaveVersion>",
         f"<Name>{escape(NOMBRE)}.xml</Name>",
         f"<Title>{escape(NOMBRE)}</Title>",
         "<ScheduleFromStart>1</ScheduleFromStart>",
         f"<StartDate>{ts(ini_p, '08:00:00')}</StartDate>",
         f"<FinishDate>{ts(fin_p, '17:00:00')}</FinishDate>",
         "<CalendarUID>1</CalendarUID>",
         "<DefaultStartTime>08:00:00</DefaultStartTime>",
         "<DefaultFinishTime>17:00:00</DefaultFinishTime>",
         "<MinutesPerDay>480</MinutesPerDay><MinutesPerWeek>2400</MinutesPerWeek>",
         "<DaysPerMonth>20</DaysPerMonth>",
         "<DurationFormat>7</DurationFormat>",
         "<NewTasksAreManual>0</NewTasksAreManual>",
         "<CurrencySymbol>$</CurrencySymbol><CurrencyCode>COP</CurrencyCode>",
         "<Calendars><Calendar><UID>1</UID><Name>Estándar (L-V 8:00-17:00)</Name>",
         "<IsBaseCalendar>1</IsBaseCalendar><WeekDays>"]
    for d in range(1, 8):
        if d in (1, 7):
            x.append(f"<WeekDay><DayType>{d}</DayType><DayWorking>0</DayWorking></WeekDay>")
        else:
            x.append(f"<WeekDay><DayType>{d}</DayType><DayWorking>1</DayWorking><WorkingTimes>"
                     "<WorkingTime><FromTime>08:00:00</FromTime><ToTime>12:00:00</ToTime></WorkingTime>"
                     "<WorkingTime><FromTime>13:00:00</FromTime><ToTime>17:00:00</ToTime></WorkingTime>"
                     "</WorkingTimes></WeekDay>")
    x.append("</WeekDays></Calendar></Calendars><Tasks>")

    # tarea 0 = resumen del proyecto
    x.append(f"<Task><UID>0</UID><ID>0</ID><Name>{escape(NOMBRE)}</Name><Type>1</Type>"
             f"<OutlineNumber>0</OutlineNumber><OutlineLevel>0</OutlineLevel><Summary>1</Summary>"
             f"<Start>{ts(ini_p, '08:00:00')}</Start><Finish>{ts(fin_p, '17:00:00')}</Finish>"
             f"<Duration>{dur(habiles_entre(ini_p, fin_p))}</Duration><DurationFormat>7</DurationFormat></Task>")
    fase = hito_n = 0
    for clave, nivel, nombre, d, preds, _r in TAREAS:
        ini, fin = fechas[clave]
        resumen = d is None
        if nivel == 1:
            fase += 1
            hito_n = 0
            wbs = str(fase)
        else:
            hito_n += 1
            wbs = f"{fase}.{hito_n}"
        hito = d == 0
        dias = habiles_entre(ini, fin) if resumen else d
        h_ini = "17:00:00" if (hito and preds) else "08:00:00"
        x.append("<Task>"
                 f"<UID>{uid[clave]}</UID><ID>{uid[clave]}</ID><Name>{escape(nombre)}</Name>"
                 f"<Type>{1 if resumen else 0}</Type><IsNull>0</IsNull>"
                 f"<WBS>{wbs}</WBS><OutlineNumber>{wbs}</OutlineNumber><OutlineLevel>{nivel}</OutlineLevel>"
                 f"<Start>{ts(ini, h_ini)}</Start><Finish>{ts(fin, '17:00:00' if not hito or preds else '08:00:00')}</Finish>"
                 f"<Duration>{dur(dias)}</Duration><DurationFormat>7</DurationFormat>"
                 f"<Manual>0</Manual><Milestone>{1 if hito else 0}</Milestone>"
                 f"<Summary>{1 if resumen else 0}</Summary><Critical>0</Critical>"
                 "<ConstraintType>0</ConstraintType><CalendarUID>-1</CalendarUID>"
                 f"<Notes>Código plantilla: {clave}</Notes>")
        for p in preds:
            x.append(f"<PredecessorLink><PredecessorUID>{uid[p]}</PredecessorUID><Type>1</Type>"
                     "<CrossProject>0</CrossProject><LinkLag>0</LinkLag><LagFormat>7</LagFormat></PredecessorLink>")
        x.append("</Task>")
    x.append("</Tasks><Resources>")
    x.append("<Resource><UID>0</UID><ID>0</ID><Type>1</Type><IsNull>0</IsNull></Resource>")
    for c, nombre in RECURSOS:
        x.append(f"<Resource><UID>{ruid[c]}</UID><ID>{ruid[c]}</ID><Name>{escape(nombre)}</Name>"
                 f"<Type>1</Type><IsNull>0</IsNull><Initials>{c}</Initials><MaxUnits>1.00</MaxUnits>"
                 "<CalendarUID>1</CalendarUID></Resource>")
    x.append("</Resources><Assignments>")
    a = 0
    for clave, _n, _nm, d, _p, recs in TAREAS:
        for r in recs:
            a += 1
            x.append(f"<Assignment><UID>{a}</UID><TaskUID>{uid[clave]}</TaskUID>"
                     f"<ResourceUID>{ruid[r]}</ResourceUID><Units>1</Units>"
                     f"<Work>{dur(d or 0)}</Work></Assignment>")
    x.append("</Assignments></Project>")
    (AQUI / "plantilla_licitacion_electrica.xml").write_text("\n".join(x), encoding="utf-8")


# ---------- Excel ----------
def generar_xlsx(hijos):
    wb = Workbook()
    ws = wb.active
    ws.title = "Cronograma"
    azul = PatternFill("solid", fgColor="1F3864")
    gris = PatternFill("solid", fgColor="D9E1F2")
    amar = PatternFill("solid", fgColor="FFF2CC")
    borde = Border(*(Side(style="thin", color="BFBFBF"),) * 4)

    ws["A1"] = NOMBRE
    ws["A1"].font = Font(bold=True, size=14, color="1F3864")
    ws["A2"] = "Fecha de inicio del proyecto:"
    ws["D2"] = FECHA_INICIO
    ws["D2"].number_format = "dd/mm/yyyy"
    ws["D2"].fill = amar
    ws["D2"].font = Font(bold=True)
    ws["E2"] = "← cambie esta fecha y todo se recalcula (celdas amarillas = editables)"
    ws["E2"].font = Font(italic=True, color="7F7F7F")

    enc = ["ID", "EDT", "Nivel", "Nombre de la tarea", "Duración (días)", "Inicio", "Fin",
           "Predecesoras (ID)", "Recursos", "Hito"]
    fila0 = 4
    for c, t in enumerate(enc, 1):
        cel = ws.cell(fila0, c, t)
        cel.font = Font(bold=True, color="FFFFFF")
        cel.fill = azul
        cel.alignment = Alignment(horizontal="center", vertical="center", wrap_text=True)
    nombre_rec = dict(RECURSOS)
    filas = {t[0]: fila0 + 1 + i for i, t in enumerate(TAREAS)}
    ids = {t[0]: i + 1 for i, t in enumerate(TAREAS)}
    fase = n = 0
    for clave, nivel, nombre, d, preds, recs in TAREAS:
        r = filas[clave]
        if nivel == 1:
            fase += 1; n = 0; wbs = str(fase)
        else:
            n += 1; wbs = f"{fase}.{n}"
        ws.cell(r, 1, ids[clave])
        ws.cell(r, 2, wbs)
        ws.cell(r, 3, nivel)
        ws.cell(r, 4, ("    " if nivel == 2 else "") + nombre)
        ws.cell(r, 8, ";".join(str(ids[p]) for p in preds))
        ws.cell(r, 9, ", ".join(nombre_rec[x] for x in recs))
        if d is None:
            hs = hijos[clave]
            a, b = filas[hs[0]], filas[hs[-1]]
            ws.cell(r, 6, f"=MIN(F{a}:F{b})")
            ws.cell(r, 7, f"=MAX(G{a}:G{b})")
            ws.cell(r, 5, f"=NETWORKDAYS(F{r},G{r},Festivos!$A$2:$A$60)")
            ws.cell(r, 10, "")
            for c in range(1, 11):
                ws.cell(r, c).fill = gris
                ws.cell(r, c).font = Font(bold=True)
        else:
            ws.cell(r, 5, d).fill = amar
            if preds:
                mx = "MAX(" + ",".join(f"G{filas[p]}" for p in preds) + ")"
                ws.cell(r, 6, f"=IF(E{r}=0,{mx},WORKDAY({mx},1,Festivos!$A$2:$A$60))")
            else:
                ws.cell(r, 6, f"=WORKDAY($D$2-1,1,Festivos!$A$2:$A$60)")
            ws.cell(r, 7, f"=IF(E{r}=0,F{r},WORKDAY(F{r},E{r}-1,Festivos!$A$2:$A$60))")
            ws.cell(r, 10, f'=IF(E{r}=0,"◆","")')
            if d == 0:
                ws.cell(r, 4).font = Font(bold=True, color="C00000")
        for c in range(1, 11):
            ws.cell(r, c).border = borde
        ws.cell(r, 6).number_format = ws.cell(r, 7).number_format = "dd/mm/yyyy"
        for c in (1, 2, 3, 5, 6, 7, 8, 10):
            ws.cell(r, c).alignment = Alignment(horizontal="center")
    ult = fila0 + len(TAREAS)
    tot = ult + 2
    ws.cell(tot, 4, "DURACIÓN TOTAL (días hábiles)").font = Font(bold=True)
    ws.cell(tot, 5, f"=NETWORKDAYS(MIN(F{fila0+1}:F{ult}),MAX(G{fila0+1}:G{ult}),Festivos!$A$2:$A$60)").font = Font(bold=True)
    ws.cell(tot + 1, 4, "Fecha de terminación").font = Font(bold=True)
    c = ws.cell(tot + 1, 5, f"=MAX(G{fila0+1}:G{ult})")
    c.font = Font(bold=True); c.number_format = "dd/mm/yyyy"
    for col, w in zip("ABCDEFGHIJ", [5, 6, 6, 62, 10, 12, 12, 14, 42, 6]):
        ws.column_dimensions[col].width = w
    ws.freeze_panes = ws.cell(fila0 + 1, 5)
    dv = DataValidation(type="whole", operator="greaterThanOrEqual", formula1="0",
                        error="La duración debe ser un número entero de días ≥ 0")
    ws.add_data_validation(dv)
    dv.add(f"E{fila0+1}:E{ult}")

    # Festivos
    wf = wb.create_sheet("Festivos")
    wf["A1"] = "Festivos (no laborables)"; wf["A1"].font = Font(bold=True)
    wf["B1"] = "Descripción"; wf["B1"].font = Font(bold=True)
    wf["D1"] = ("Escriba aquí los festivos de Colombia del año del proyecto (A2:A60). "
                "El cronograma de Excel los salta automáticamente. "
                "En Project, agréguelos en Proyecto → Cambiar tiempo de trabajo.")
    wf["D1"].alignment = Alignment(wrap_text=True)
    wf.column_dimensions["A"].width = 14; wf.column_dimensions["B"].width = 30
    wf.column_dimensions["D"].width = 60
    for r in range(2, 61):
        wf.cell(r, 1).number_format = "dd/mm/yyyy"
        wf.cell(r, 1).fill = amar

    # Recursos
    wr = wb.create_sheet("Recursos")
    for c, t in enumerate(["Código", "Recurso", "Tipo"], 1):
        cel = wr.cell(1, c, t); cel.font = Font(bold=True, color="FFFFFF"); cel.fill = azul
    for i, (c, nm) in enumerate(RECURSOS, 2):
        wr.cell(i, 1, c); wr.cell(i, 2, nm); wr.cell(i, 3, "Trabajo")
    wr.column_dimensions["B"].width = 36

    # Instrucciones
    wi = wb.create_sheet("Instrucciones")
    txt = [
        "CÓMO USAR ESTA PLANTILLA",
        "",
        "En Excel:",
        "1. Cambie la fecha de inicio (Cronograma!D2). Todas las fechas se recalculan.",
        "2. Ajuste las duraciones (columna E, amarilla). Use 0 para hitos.",
        "3. Agregue los festivos en la hoja Festivos.",
        "",
        "En Microsoft Project (recomendado):",
        "1. Abra plantilla_licitacion_electrica.xml (Archivo → Abrir → tipo XML).",
        "2. Proyecto → Información del proyecto → cambie la fecha de comienzo.",
        "3. Agregue festivos en Proyecto → Cambiar tiempo de trabajo.",
        "4. Elimine las tareas que no apliquen (p. ej. subestación, RETILAP, SIPRA).",
        "5. Guarde como .mpp y fije la línea base antes de presentar la oferta.",
        "",
        "Supuestos: jornada L-V 8:00-17:00, vínculos fin-comienzo, sin retardos.",
        "Las duraciones son referenciales; ajústelas al alcance de cada licitación.",
    ]
    for i, t in enumerate(txt, 1):
        wi.cell(i, 1, t)
    wi["A1"].font = Font(bold=True, size=13)
    wi.column_dimensions["A"].width = 95
    wb.move_sheet("Instrucciones", offset=-3)
    wb.active = 1
    wb.save(AQUI / "plantilla_licitacion_electrica.xlsx")


if __name__ == "__main__":
    fechas, hijos = calcular_fechas()
    generar_xml(fechas, hijos)
    generar_xlsx(hijos)
    print("Inicio:", fechas["F1"][0], " Fin:", max(v[1] for v in fechas.values()))

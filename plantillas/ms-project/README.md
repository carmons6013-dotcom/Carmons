# Plantilla de cronograma: licitación de obra eléctrica

Plantilla que se puede reutilizar en ofertas de obras eléctricas en Colombia.
Tiene 8 fases, 48 tareas, 10 hitos y 9 recursos.

| Archivo | Uso |
|---|---|
| `plantilla_licitacion_electrica.xml` | Se abre en **MS Project** (Archivo → Abrir → tipo *XML*). Trae la EDT, las duraciones, las predecesoras, los hitos, los recursos y sus asignaciones. |
| `plantilla_licitacion_electrica.xlsx` | Cronograma en **Excel** con las fechas calculadas por fórmula. Si cambia la fecha de inicio o una duración, todo se recalcula. Los festivos se agregan en la hoja *Festivos*. |
| `generar_plantilla.py` | Script que genera los dos archivos. Para cambiar tareas o recursos, edite las listas `TAREAS` y `RECURSOS` y ejecute `python3 generar_plantilla.py` (requiere `openpyxl`). |

## Fases

1. Inicio y contratación (pólizas, acta de inicio, plan SST)
2. Ingeniería y diseño (cargas, cálculos, SPT/SIPRA NTC 4552, RETILAP, planos)
3. Trámites ante el operador de red (factibilidad, aprobación del proyecto)
4. Suministros (tableros, transformador/MT, cable)
5. Construcción y montaje
6. Pruebas y energización
7. Certificación RETIE / RETILAP
8. Entrega y cierre

## Supuestos

- Jornada de lunes a viernes, de 8:00 a 17:00. Fecha de inicio de ejemplo: 04/01/2027.
- Todos los vínculos son fin-comienzo y no tienen retardos.
- Con estos datos el plazo es de **114 días hábiles** (unos 5,3 meses). La ruta crítica pasa por el suministro del transformador.
- Las duraciones son de referencia. Ajústelas al alcance de cada licitación y quite las tareas que no apliquen.
- Los festivos de Colombia **no** vienen cargados. Agréguelos en Project (*Proyecto → Cambiar tiempo de trabajo*) o en la hoja *Festivos* del Excel.

## Pasos en Project

1. Abra el `.xml`.
2. Vaya a *Proyecto → Información del proyecto* y ponga la fecha de inicio real.
3. Agregue los festivos.
4. Ajuste duraciones y recursos.
5. Guarde como `.mpp`.
6. Fije la línea base antes de presentar la oferta.

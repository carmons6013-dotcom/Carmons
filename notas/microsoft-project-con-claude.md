# Microsoft Project con Claude — Nota de consulta

**Fecha:** 2026-11-10
**Pregunta:** ¿Microsoft Project se puede usar con Claude como Word o Excel?

## Respuesta corta

Sí se puede usar, pero no igual que Word o Excel. Hasta donde se sabe, Claude
no tiene un complemento oficial que funcione dentro de Microsoft Project, como
sí lo tiene en Excel o PowerPoint. Tampoco puede abrir un archivo `.mpp`
directamente porque es un formato binario cerrado. Aun así, puede trabajar con
Project usando formatos intermedios.

## Formas de usarlo

| Método | Cómo funciona | Para qué sirve |
|---|---|---|
| **1. XML de Project (MSPDI)** ⭐ Recomendado | En Project: *Archivo → Guardar como → XML*. Claude lee o genera ese XML, y luego usted lo abre en Project. | Es el más completo: conserva tareas, duraciones, predecesoras (FC, CC, FF), recursos, costos, calendarios, hitos y EDT/WBS. |
| **2. Excel / CSV** | Claude genera un `.xlsx` con el cronograma. En Project: *Archivo → Abrir → Excel* y el asistente de importación asigna las columnas. | Es más sencillo, pero se pierde parte de la lógica, como calendarios y algunos tipos de vínculo. |
| **3. Leer un `.mpp` existente** | Se puede convertir a XML o Excel con la librería de código abierto MPXJ, o exportarlo desde Project. | Para revisar ruta crítica, holguras, sobreasignación de recursos o retrasos. |
| **4. Project para la web / Planner** | Depende de los conectores de Microsoft 365 activos. No es seguro que den acceso completo a los planes. | Es limitado: conviene verificarlo en la cuenta. |

## Qué puede hacer Claude en la práctica

- **Crear un cronograma desde cero.** Por ejemplo, una obra eléctrica, un
  proyecto solar FV o una subestación, con EDT, duraciones, dependencias, hitos
  (RETIE, energización, recibo de obra) y recursos. El resultado es un `.xml`
  que Project abre listo, con el diagrama de Gantt.
- **Analizar un cronograma existente.** Ruta crítica, tareas sin predecesoras,
  holguras negativas, recursos sobreasignados y fechas poco realistas.
- **Convertir una propuesta o licitación en cronograma.** Pasar un alcance en
  Word o PDF, o un presupuesto en Excel, a un plan de trabajo en Project.
- **Hacer informes.** Curva S, avance contra línea base y reportes ejecutivos en
  Word, Excel o PowerPoint a partir de los datos exportados.

## Limitación

Claude no edita el archivo "en vivo" dentro de Project. El flujo siempre es:

**Exportar → Claude procesa → Importar**

## Próximos pasos sugeridos

- Pedir a Claude un cronograma de ejemplo en XML (MSPDI) para un proyecto
  eléctrico o solar.
- Si ya existe un cronograma, exportarlo a XML o Excel y pedir una revisión.

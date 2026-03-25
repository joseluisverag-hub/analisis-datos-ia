# Prompt estándar para GitHub Copilot en VS Code

Este prompt está pensado para usarlo en **GitHub Copilot Chat dentro de VS Code** y dejar cualquier notebook Jupyter compatible con el framework automático de extracción de reportes.

---

## Objetivo

Formatear un notebook para que el framework pueda extraer automáticamente:

- título
- insights
- conclusión
- gráficos

Sin cambiar el análisis ni los resultados.

---

## Prompt para usar en Copilot

```text
Quiero que reformatees este notebook Jupyter para que sea compatible con un framework automático que extrae:
1) título
2) insights
3) conclusión
4) gráficos embebidos en outputs

Objetivo:
No cambies el análisis ni los resultados.
Solo reorganiza y mejora la estructura del notebook para que pueda ser procesado automáticamente.

Aplica estas reglas en TODO el notebook:

### 1. Título
- La primera celda markdown debe ser un H1 con el título principal del análisis.
- Si ya existe un título, reutilízalo.
- Si no existe, crea uno claro y profesional.
- Formato exacto:
  # Título del análisis

### 2. Insights
- Después de cada gráfico o bloque analítico importante, debe existir una celda markdown separada con encabezado:
  ## Insight
- En esa celda, redacta un insight breve, claro y profesional, basado solo en lo que ya muestra el análisis.
- No inventes datos.
- Si ya hay texto equivalente, conviértelo a este formato.
- Si hay varios insights juntos, sepáralos en distintas celdas markdown cuando corresponda.

### 3. Conclusión
- Al final del notebook debe existir una celda markdown con encabezado:
  ## Conclusión
- Debe resumir los hallazgos principales en tono ejecutivo.
- Si ya existe una conclusión, reformátala con ese encabezado exacto.

### 4. Gráficos
- No elimines gráficos existentes.
- Mantén cada gráfico en una celda de código independiente cuando sea posible.
- Si hay varias visualizaciones mezcladas en una sola celda, sepáralas si eso mejora claridad.
- Asegúrate de que cada gráfico importante tenga un insight markdown inmediatamente después.

### 5. Orden del notebook
Reorganiza el notebook para que siga esta estructura lógica:
1. Título
2. Objetivo o contexto
3. Preparación de datos
4. Gráfico o análisis
5. Insight
6. Gráfico o análisis
7. Insight
8. Hallazgos ejecutivos (si aplica)
9. Conclusión

### 6. Estilo markdown
- Usa encabezados markdown consistentes:
  - # para el título principal
  - ## para secciones e insights
- No uses texto largo innecesario.
- Mantén tono profesional, claro y reutilizable.

### 7. Compatibilidad con extracción automática
Quiero que el notebook quede preparado para que un script detecte:
- el título como el primer H1
- los insights como celdas markdown con encabezado exacto ## Insight
- la conclusión como una celda markdown con encabezado exacto ## Conclusión
- los gráficos como outputs de celdas de código

### 8. Restricciones
- No cambies los cálculos, métricas ni resultados.
- No modifiques la lógica del análisis salvo que sea necesario para separar visualizaciones o mejorar estructura.
- No elimines contenido útil.
- Conserva el notebook funcional.

### 9. Entrega esperada
Haz directamente las modificaciones en el notebook actual.
Si detectas secciones ambiguas, elige la opción más compatible con la extracción automática.
```

---

## Prompt adicional para tags

Si quieres una versión más robusta del estándar, puedes pedir además esto:

```text
Además del formateo actual, prepara el notebook para extracción automática con tags de celda cuando sea posible.

Convención deseada:
- celda del título: tag "title"
- celdas de insights: tag "insight"
- celda final de conclusión: tag "conclusion"
- celdas de código con gráficos principales: tag "chart"

No cambies el contenido analítico; solo agrega la metadata necesaria y mantén el notebook válido.
Si no puedes agregar tags de forma segura desde la interfaz actual, deja el contenido estructurado con markdown exacto:
- # Título
- ## Insight
- ## Conclusión
```

---

## Uso recomendado

1. Abre el notebook en VS Code.
2. Abre GitHub Copilot Chat.
3. Pega el prompt.
4. Revisa los cambios propuestos.
5. Ejecuta el notebook nuevamente para guardar outputs de gráficos.
6. Luego corre el framework de extracción.

---

## Resultado esperado

El notebook quedará preparado para que el framework detecte automáticamente:

- título
- insights
- conclusión
- gráficos

y pueda alimentar la generación de PDF y PPTX sin trabajo manual adicional.

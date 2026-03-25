# Titanic: análisis exploratorio y factores asociados a la supervivencia

## Insights

1. Insight Los datos muestran que la proporción general de supervivencia fue menor al 50 %, por lo que la mayoría de los pasajeros no sobrevivió. Esto sugiere un desenlace ampliamente adverso y refuerza la conveniencia de analizar variables como sexo, clase y edad para entender qué factores podrían estar asociados a diferencias en el resultado.

2. Insight Los datos muestran que las mujeres registran una tasa de supervivencia considerablemente superior a la de los hombres. Esto sugiere que el sexo podría estar asociado de forma relevante con la probabilidad de supervivencia y que esta variable puede aportar valor explicativo en análisis posteriores.

3. Insight Los datos muestran que los pasajeros de primera clase registran la mayor tasa de supervivencia, seguidos por los de segunda clase, mientras que la tercera clase presenta la más baja. Esto sugiere que la clase del pasajero podría estar asociada de manera importante con el resultado, por lo que Pclass aparece como una variable relevante para explicar diferencias en la supervivencia.

4. Insight Los datos muestran que las mujeres presentan tasas de supervivencia superiores a las de los hombres en todas las clases, y que la clase modula con claridad este patrón. Esto sugiere que la combinación entre Sex y Pclass podría estar asociada de forma especialmente fuerte con la supervivencia. En esta lectura, las mujeres de primera clase concentran los resultados más favorables, mientras que los hombres de tercera clase muestran los más desfavorables.

5. Insight Los datos muestran que los niños presentan la mayor tasa de supervivencia entre los grupos etarios observados, mientras que los adultos mayores registran los valores más bajos. Los adultos se ubican en un nivel intermedio. Esto sugiere que la edad podría estar asociada a diferencias relevantes en la probabilidad de supervivencia y que Age, o variables derivadas como grupo_edad, podrían aportar valor explicativo en un modelo posterior.

6. Insight Los datos muestran un patrón no lineal entre el tamaño de la familia y la supervivencia: los grupos pequeños o medianos registran mejores tasas que quienes viajaban solos o en familias muy grandes. Esto sugiere que el tamaño del núcleo familiar podría estar asociado al resultado final. Una posible explicación es que ciertos tamaños de grupo hayan facilitado o dificultado la capacidad de respuesta durante la evacuación, aunque los datos no permiten afirmarlo como causa probada. En términos analíticos, tamano_familia parece ser una variable útil para complementar la lectura demográfica y socioeconómica de la supervivencia.

7. Insight Los datos muestran que la distribución de edades difiere entre quienes sobrevivieron y quienes no sobrevivieron. En particular, los pasajeros de menor edad parecen tener una presencia relativamente mayor entre los sobrevivientes, mientras que en edades más altas la frecuencia se concentra más en quienes no sobrevivieron. Esto sugiere que la edad podría estar asociada al resultado final, aunque el gráfico por sí solo no prueba una relación causal. Una posible explicación es que la vulnerabilidad o las condiciones de evacuación hayan afectado de forma distinta a los grupos etarios. En términos analíticos, esta visualización refuerza que Age no solo aporta valor como variable individual, sino también como dimensión útil para segmentar el riesgo y complementar la lectura de supervivencia por grupo etario.

8. Hallazgos ejecutivos 1. Los datos muestran que la mayoría de los pasajeros no sobrevivió, lo que sugiere un evento con desenlace ampliamente adverso. 2. El sexo aparece como una de las variables más asociadas a la supervivencia, con mejores resultados observados en mujeres que en hombres. 3. La clase del pasajero también muestra una asociación clara con el resultado, con patrones más favorables en primera clase y menos favorables en tercera. 4. La combinación entre sexo y clase permite distinguir perfiles con comportamientos de supervivencia claramente diferentes. 5. La edad parece aportar capacidad explicativa adicional, ya que los grupos más jóvenes muestran mejores resultados relativos que los de mayor edad. 6. El tamaño de la familia presenta un patrón no lineal, por lo que podría ser una variable complementaria relevante en análisis posteriores.

## Conclusión

Conclusión Los datos muestran que la supervivencia en el Titanic no se distribuyó de manera homogénea entre los pasajeros. Esto sugiere que variables demográficas y socioeconómicas como sexo, clase, edad y tamaño de familia podrían estar asociadas a diferencias relevantes en el resultado final. En conjunto, el análisis permite construir una narrativa clara para portafolio y ofrece una base consistente para un modelo predictivo posterior.

## Gráficos extraídos

- chart_01.png (celda 5) — Supervivencia general

- chart_02.png (celda 8) — Supervivencia por sexo

- chart_03.png (celda 11) — Supervivencia por clase

- chart_04.png (celda 14) — Supervivencia por sexo + clase

- chart_05.png (celda 17) — Supervivencia por grupo etario

- chart_06.png (celda 20) — Supervivencia por tamaño de familia

- chart_07.png (celda 23) — Distribución de edad por resultado

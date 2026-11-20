# Laboratorios y evaluación

Todos los datasets y soluciones abajo son **entregas planificadas**. Usar datos ficticios en los materiales públicos; los datos operativos quedan en el proyecto de aplicación con controles propios.

| Laboratorio | Material a producir | Ejercicio | Evidencia de conclusión |
|---|---|---|---|
| L1 — formular | 12 situaciones cotidianas | Elegir regla, Choice, Noul, Score o generación | Respuesta justificada y solución comentada |
| L2 — hotel | 6 políticas ficticias de cancelación | Separar dinero, crédito, conflicto y omisión | Ninguna ausencia tratada automáticamente como “no” |
| L3 — atención | 30 tickets ficticios en portugués | Etiquetar cola y suficiencia | Matriz manual con divergencias explicadas |
| L4 — evidencias | 8 pares de afirmación/pasaje y 4 cláusulas ficticias | Marcar apoyo y pendiente de revisión | Fragmento de evidencia y límite de la conclusión |
| L5 — rutas | 12 tareas con catálogo de modelos/agentes abstractos | Elegir camino y tope de intentos | Diagrama sin loops ilimitados ni permisos implícitos |
| L6 — DOM | 5 listas textuales de elementos | Elegir candidato o abstenerse | Distinguir selección semántica de ejecución del clic |
| L7 — economía | Hoja de cálculo editable y escenarios | Calcular API, fallback y revisión | Cuenta corregida y análisis de sensibilidad |
| L8 — evaluación | Predicciones simuladas con error de alta confianza | Medir error y cobertura al variar el umbral | Informe rotulado como simulación, sin alegar benchmark |

## Proyecto final

Problema: un equipo recibe tickets y necesita sugerir colas. Entregar taxonomía; cinco ejemplos difíciles; preguntas atómicas; política de revisión; diagrama del flujo; plan de datos y evaluación; presupuesto; criterios de operación y retorno.

Recorrido sin código entrega hoja de cálculo y especificación. Recorrido técnico agrega ejecución en el laboratorio del repositorio de la aplicación cuando se implemente, logs anonimizados y un informe reproducible. Si no hay acceso real, la ejecución usa fixture rotulada; no inventar llamadas exitosas.

## Rúbrica de 100 puntos

| Criterio | Puntos | Evidencia |
|---|---:|---|
| Formulación y opciones | 20 | Preguntas específicas, sin solapamiento indebido, datos insuficientes tratados |
| Política de decisión | 20 | Consecuencias, revisión, acciones permitidas y límites de repetición |
| Evidencia y calidad | 25 | Referencia revisada, separación de datos y errores por clase |
| Economía y latencia | 15 | Cálculo correcto y costos del flujo completo |
| Reproducibilidad y comunicación | 20 | Versiones, fuentes, procedimiento y distinción entre simulación y resultado real |

Aprobación propuesta: 75 puntos y corrección de las fallas esenciales. Alegar que la confianza garantiza la verdad, presentar la simulación como benchmark o permitir una acción fuera de la política exige revisión del proyecto, independientemente de la suma.

## Preguntas de salida y respuesta esperada

1. “Si solo hay dos opciones, ¿el modelo no puede errar?” Puede elegir la alternativa equivocada.
2. “Noul 0,05 significa poca confianza?” Significa baja probabilidad de sim, no un campo confidence.
3. “La falta de confirmación significa que no hubo agendamiento?” No necesariamente; preservar insuficiencia.
4. “10 mil tokens cuestan US$ 0,0042 en esta tarifa?” No; US$ 0,00042.
5. “¿El benchmark externo valida atención en portugués?” No; necesitamos evaluación en el dominio.
6. “¿Puedo enviar un screenshot directamente?” La modalidad documentada es texto; requiere una etapa anterior.
7. “Elegí el agente financiero: ¿puede pagar?” Elegir una ruta no concede permiso.
8. “Si el piloto no economiza, ¿el proyecto fracasó?” Una decisión fundamentada de no adoptar es un resultado útil.

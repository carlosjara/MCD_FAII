Rules
OJO: El trabajo es en parejas (parejas de a dos!).
Es completamente válido buscar en internet soluciones a preguntas de código, no hay problema en eso. Sin embargo, en varios semestres anteriores, ha pasado, y ojalá no vuelva a pasar, que se copien pedazos de códigos entre grupos, siendo esto bastante evidente. Todo siempre comienza cuando varios grupos se reunen a desarrollar el taller "por separado", pero siempre termina en utilización del mismo pedazo de código, ya sea porque lo encuentran juntos en la web o porque un grupo le muestra al otro.
Evitemos problemas; que cada grupo trabaje de manera totalmente independiente. Es bastante incómodo (para todos) tener que tomar acciones punitivas como tener que repetir la materia.

OJO: no olviden aplicar buenas prácticas en cuanto a metodología, pues problemas como el data leakage deben ser evitados a toda costa e influiran en la calificación.

Description
Contexto de negocio.
Una empresa aseguradora en salud está presentando altos costos dados por complicaciones de pacientes que anteriormente habían sido marcados con ciertas enfermedades, cuya complicación puede aumentar tanto el costo, como la preocupación del paciente. Una de las enfermedades que han decidido estudiar estratégicamente es el Cáncer de Mama. Dado esto, la empresa requiere mantener un control de estos pacientes, haciendo demanda inducida, seguimiento periódico, adopción de estrategias médicas, entre otras, que permitan evitar que se llegue a alguna complicación. Es necesario priorizar estos pacientes tratando de predecir quienes que llegarán a presentar alguna complicación en los siguientes 6 meses.

Problema de negocio
La empresa ha decidido contratarlos para que construyan un modelo predictivo que permita estimar la probabilidad de que un paciente diagnosticado con Cáncer de Mama presente una complicación en los próximos 6 meses.

Contexto analítico
Se espera que entrene diferentes familias de modelos predictivos de clasificación (SVC con diferentes kernels, Redes Neuronales poco profundas), precedidos por diferentes procesos de transformación (normalizaciones, imputación, feature engineering, dummificación, PCA, selección de features).

La evaluación de la calidad de los flujos de modelos predictivos se debe estimar utilizando la métrica de F1-Score.

Expliquen sus ideas, el por qué realizan las acciones, y comenten los resultados obtenidos; se espera mucho más que unos bloques de código.
La toma de decisiones sobre los datos se debe hacer considerando el contexto del problema y de los datos, no se puede ver todo solamente desde los ojos de los datos, sino también considerar el negocio.
Un Científico de Datos debe poder comunicar los puntos importantes de su trabajo en un lenguaje universal para todos los públicos.
Todo esto se considerará en la nota.
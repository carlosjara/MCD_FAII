## Integrantes :
#### Yasmin Garcia
#### Carlos Enrique Jaramillo

#### Desarrollo
La actividad fue desarrollada en cuatro fases las cuales serán descritas de manera superficial (no técnica) en esta sección.

Con el fin de usar de manera centralizada las configuraciones de esta actividad, se utilizó un archivo *yaml* en el que guardan configuraciones como rutas de archvios origenes y destino o hiperparametros de modelos a optimizar usados en la seccion 4, para la lectura de este archivo, se realiza inicialmente una configuracion de ruta de ubiciacion del archvio (Taller_Practico)
  
  1. Data Understanding
  : *Archivo:*
  [data_understanding_cancer.ipynb](https://github.com/carlosjara/MCD_FAII/blob/main/FAII/Talleres/Taller_Practico/1_data_understanding/data_understanding_cancer.ipynb)

En este archivo se describen las variables desde un punto de vista analitico del conjunto de datos, utilizando visualziaciones de barras, cajas y bigotes, se generaron nuevas columnas derivadas de las columnas actuales, al igual que se analizaron posibles estrategias de imputación de datos faltantes o outlier para la fase de procesamiento de datos.

2. Data Preparation
   : *Archivo:*
   [data_preparation_cancer.ipynb](https://github.com/carlosjara/MCD_FAII/blob/main/FAII/Talleres/Taller_Practico/2_data_preparation/data_preparation_cancer.ipynb)

En este archivo, se prepara la informacion para minimizar el impacto en el entrenamiento de los modelos y generacion de predicciones, entre otro procesamiento de datos se realizó elimiacion de variables, imputación de valores nulos, reemplazo de valores outlies utilizando el metodo de tukey (modificado para reemplazo y no solo para encontrarlos) dispuesto en el archivo **TukeysOutlierReplacer.py**, una vez realizada el procesamiento, se guarda el archivo preparado en la ruta especificada en el archivo *yaml*
**Nota:** En este archivo se encuentra el primer acercamiento al entrenamiento de un modelo, como una **[ Prueba Inicial ]** de entrenamiento y envío al [kaggle](https://www.kaggle.com/competitions/fa-ii-2024-i-flujos-de-modelos-tradicionales) 

3. Modeling [ Carpetas : 3_Modeling y YASMIN_TEST ]
   :*Archivo:*
   [modeling_cancer.ipynb](https://github.com/carlosjara/MCD_FAII/blob/main/FAII/Talleres/Taller_Practico/3_modeling/modeling_cancer.ipynb)
Se manejaron dos archivos (dispuestos en cada carpeta) uno para mantener el codigo limpio y otro para ejecucion y pruebas), dado los tiempos de ejecucion de los procesos, se decidio conservar ambas versiones.

En estos archivos se leyó la data preaparada en la fase anterior (dispuesta en la ruta del archivo yaml) para realizar pasar por diferentes pipelines de los modelos a ejeuctar y se corrieron diferentes modelos con diferente configuracion de hiperparametros o parametros para encontrar mejores resultados con los datos de prueba y en kaggle.
Los modelos desarrollados fueron:
- Regresion Logistica con PCA (Encontrando el mejor PCA para estos datos preparados)
- Regresion Logistica
- Naive Bayes
- XGBOOST (Se selcciono para realiza optimizacion en la siguiente fase, por sus buenos resultados en kaggle)
- Supportt Vector Classifier Lineal usando  Grid Search (usando PCA) - Dado su alto tiempo en ejecucion **se recomienda no ejecutar**
- Supportt Vector Classifier (Lineal) usando LDA y una primera fase de optimizacion Bayesiana
- Supportt Vector Classifier (RBF) usando LDA y una primera fase de optimizacion Bayesiana
- Red Neuronal de Poca profundida *model_hidden_layer_size_exp ¬ max = 4 *

4. Optimziation
  : *Archivo:*
  Optimizacion modelo : [SVC_Optimization.ipynb](https://github.com/carlosjara/MCD_FAII/blob/main/FAII/Talleres/Taller_Practico/4_optimization/SVC_Optimization.ipynb) y Optmizacion modelo : 
  [xgboost_Optimization.ipynb](https://github.com/carlosjara/MCD_FAII/blob/main/FAII/Talleres/Taller_Practico/4_optimization/xgboost_Optimization.ipynb)

Se tomaron los dos modelos con mejores resutlados en kaggle para ejecutar realizar optimziacion.

Para el caso de SupportVectorClassifier, se adiciona configuracion de parametro para Scaler (agregando la robusta) y se ejecuta con diferentes pruebas, conservando en codigo la mas optima, pero almacenando modelos archivos .pkl con los modelos que iban mejorando sus resultados en kaggle.

Para el caso de XGBOOST, se decidio realizar numero de iteraciones alta (**se recomienda no ejecutar** +120 minutos

Adicionalmente en la carpeta raiz, se conservan los modelos *.pck y *.svc cargados a kaggle y en la carpeta data se almacenan los parquet entregados en la actividad.


---


## Rules
OJO: El trabajo es en parejas (parejas de a dos!).
Es completamente válido buscar en internet soluciones a preguntas de código, no hay problema en eso. Sin embargo, en varios semestres anteriores, ha pasado, y ojalá no vuelva a pasar, que se copien pedazos de códigos entre grupos, siendo esto bastante evidente. Todo siempre comienza cuando varios grupos se reunen a desarrollar el taller "por separado", pero siempre termina en utilización del mismo pedazo de código, ya sea porque lo encuentran juntos en la web o porque un grupo le muestra al otro.
Evitemos problemas; que cada grupo trabaje de manera totalmente independiente. Es bastante incómodo (para todos) tener que tomar acciones punitivas como tener que repetir la materia.

OJO: no olviden aplicar buenas prácticas en cuanto a metodología, pues problemas como el data leakage deben ser evitados a toda costa e influiran en la calificación.

## Description
### Contexto de negocio.
Una empresa aseguradora en salud está presentando altos costos dados por complicaciones de pacientes que anteriormente habían sido marcados con ciertas enfermedades, cuya complicación puede aumentar tanto el costo, como la preocupación del paciente. Una de las enfermedades que han decidido estudiar estratégicamente es el Cáncer de Mama. Dado esto, la empresa requiere mantener un control de estos pacientes, haciendo demanda inducida, seguimiento periódico, adopción de estrategias médicas, entre otras, que permitan evitar que se llegue a alguna complicación. Es necesario priorizar estos pacientes tratando de predecir quienes que llegarán a presentar alguna complicación en los siguientes 6 meses.

### Problema de negocio
La empresa ha decidido contratarlos para que construyan un modelo predictivo que permita estimar la probabilidad de que un paciente diagnosticado con Cáncer de Mama presente una complicación en los próximos 6 meses.

### Contexto analítico
Se espera que entrene diferentes familias de modelos predictivos de clasificación (SVC con diferentes kernels, Redes Neuronales poco profundas), precedidos por diferentes procesos de transformación (normalizaciones, imputación, feature engineering, dummificación, PCA, selección de features).

La evaluación de la calidad de los flujos de modelos predictivos se debe estimar utilizando la métrica de F1-Score.

Expliquen sus ideas, el por qué realizan las acciones, y comenten los resultados obtenidos; se espera mucho más que unos bloques de código.
La toma de decisiones sobre los datos se debe hacer considerando el contexto del problema y de los datos, no se puede ver todo solamente desde los ojos de los datos, sino también considerar el negocio.
Un Científico de Datos debe poder comunicar los puntos importantes de su trabajo en un lenguaje universal para todos los públicos.
Todo esto se considerará en la nota.


### Integrantes
Yasmin Garcia
Carlos Jaramillo

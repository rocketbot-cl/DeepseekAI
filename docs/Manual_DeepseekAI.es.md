



# DeepseekAI
  
Módulo para interactuar con los modelos de DeepseekAI desde Rocketbot.  

*Read this in other languages: [English](Manual_DeepseekAI.md), [Português](Manual_DeepseekAI.pr.md), [Español](Manual_DeepseekAI.es.md)*
  
![banner](imgs/Banner_DeepseekAI.png o jpg)
## Como instalar este módulo
  
Para instalar el módulo en Rocketbot Studio, se puede hacer de dos formas:
1. Manual: __Descargar__ el archivo .zip y descomprimirlo en la carpeta modules. El nombre de la carpeta debe ser el mismo al del módulo y dentro debe tener los siguientes archivos y carpetas: \__init__.py, package.json, docs, example y libs. Si tiene abierta la aplicación, refresca el navegador para poder utilizar el nuevo modulo.
2. Automática: Al ingresar a Rocketbot Studio sobre el margen derecho encontrara la sección de **Addons**, seleccionar **Install Mods**, buscar el modulo deseado y presionar install.  

## Cómo usar este módulo

Para usar este módulo, necesitamos obtener una clave API de DeepSeek y tener créditos disponibles. Sigue estos pasos:

### Obtener la API Key

1. Para comenzar, cree una cuenta o inicie sesión en [platform.deepseek.com/api_keys](https://platform.deepseek.com/api_keys).

2. Una vez en la página de claves API, podrá generar una nueva clave API.

3. La clave API comenzará con "sk-".

**Importante**: Asegúrese de guardar la clave en un lugar seguro, ya que no podrá verla nuevamente después de cerrar esta ventana.

### Comprar Créditos

Para poder usar la API de DeepSeek, es necesario tener créditos disponibles:

1. Visite la plataforma de DeepSeek y configure su método de pago
2. Los servicios de DeepSeek son de pago, asegúrese de tener saldo disponible

**Nota**: Sin créditos disponibles, no podrá usar la API aunque tenga una clave API válida.

### Uso del Módulo

Una vez que tenga su clave API y créditos disponibles, puede usar el módulo de la siguiente manera:


1. **Conectar con DeepSeek AI**:
   - Use el comando "Connect to DeepSeek AI"
   - Ingrese su clave API en el campo correspondiente
   - El módulo verificará la conexión y mostrará los modelos disponibles

2. **Generar Texto**:
   - Use el comando "Generate Text"
   - Ingrese su prompt o pregunta
   - Seleccione el modelo a usar. Los modelos disponibles son:
     - `deepseek-chat`: Modelo optimizado para conversaciones y generación de texto
     - `deepseek-reasoner`: Modelo especializado en razonamiento y resolución de problemas
   - Configure los parámetros opcionales si lo desea:
     - Temperature (0-1): controla la creatividad de las respuestas
     - Max Tokens: límite de tokens para la respuesta
     - Stop Sequence: texto que detendrá la generación

3. **Consultar Modelos Disponibles**:
   - Use el comando "Get Available Models"
   - Verá la lista de modelos que puede usar con su cuenta

### Recomendaciones

- Mantenga su clave API segura y no la comparta
- Monitoree su uso 
de créditos regularmente
- Use el modelo más apropiado para su caso de uso:
  - `deepseek-chat`: Para interacciones conversacionales generales y generación de texto
  - `deepseek-reasoner`: Para tareas que requieren análisis lógico y razonamiento detallado
- Ajuste la temperatura según necesite respuestas más precisas (0) o creativas (1)
- El valor predeterminado de temperatura es 1.0
- El límite predeterminado de tokens es 2048
## Descripción de los comandos

### Conectar con DeepseekAI
  
Establece conexión con DeepseekAI
|Parámetros|Descripción|ejemplo|
| --- | --- | --- |
|API Key|Clave API de tu cuenta de DeepseekAI|sk-ant...|
|Asignar a variable|Nombre de la variable donde se guardará la conexión|resultadoDeepseekAI|

### Obtener Modelos
  
Recupera los modelos disponibles de DeepseekAI
|Parámetros|Descripción|ejemplo|
| --- | --- | --- |
|Asignar a variable|Nombre de la variable donde se guardará la lista de modelos|resultadoModelos|

### Generar Texto
  
Genera texto utilizando DeepseekAI
|Parámetros|Descripción|ejemplo|
| --- | --- | --- |
|Prompt|Texto de entrada para generar texto|Qué es Rocketbot?|
|Modelo|ID del modelo a utilizar|deepseek-chat|
|Temperatura (opcional)|Controla la aleatoriedad de la generación de texto (0.0 a 2)|0.8|
|Máximo de tokens (opcional)|Número máximo de tokens a generar|100|
|Secuencia de parada (opcional)|Secuencia opcional para detener la generación de texto|herramienta RPA|
|Asignar a variable|Nombre de la variable donde se guardará el texto generado|resultadoTexto|

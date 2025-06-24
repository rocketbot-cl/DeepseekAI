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
- Monitoree su uso de créditos regularmente
- Use el modelo más apropiado para su caso de uso:
  - `deepseek-chat`: Para interacciones conversacionales generales y generación de texto
  - `deepseek-reasoner`: Para tareas que requieren análisis lógico y razonamiento detallado
- Ajuste la temperatura según necesite respuestas más precisas (0) o creativas (1)
- El valor predeterminado de temperatura es 1.0
- El límite predeterminado de tokens es 2048
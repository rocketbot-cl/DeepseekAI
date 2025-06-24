## Como usar este módulo

Para usar este módulo, precisamos obter uma chave API do DeepSeek e ter créditos disponíveis. Siga estes passos:

### Obtendo a Chave API

1. Primeiro, crie uma conta ou faça login em [platform.deepseek.com/api_keys](https://platform.deepseek.com/api_keys).

2. Uma vez na página de chaves API, você poderá gerar uma nova chave API.

3. A chave API começará com "sk-".

**Importante**: Certifique-se de salvar a chave em um local seguro, pois você não poderá vê-la novamente depois de fechar esta janela.

### Comprando Créditos

Para usar a API do DeepSeek, você precisa ter créditos disponíveis:

1. Visite a plataforma DeepSeek e configure seu método de pagamento
2. Os serviços do DeepSeek são pagos, certifique-se de ter saldo disponível

**Nota**: Sem créditos disponíveis, você não poderá usar a API mesmo que tenha uma chave API válida.

### Usando o Módulo

Uma vez que você tenha sua chave API e créditos disponíveis, você pode usar o módulo da seguinte forma:

1. **Conectar ao DeepSeek AI**:
   - Use o comando "Connect to DeepSeek AI"
   - Insira sua chave API no campo correspondente
   - O módulo verificará a conexão e exibirá os modelos disponíveis

2. **Gerar Texto**:
   - Use o comando "Generate Text"
   - Insira seu prompt ou pergunta
   - Selecione o modelo a ser usado. Os modelos disponíveis são:
     - `deepseek-chat`: Modelo otimizado para conversas e geração de texto
     - `deepseek-reasoner`: Modelo especializado em raciocínio e resolução de problemas
   - Configure os parâmetros opcionais se desejar:
     - Temperature (0-1): controla a criatividade das respostas
     - Max Tokens: limite de tokens para a resposta
     - Stop Sequence: texto que irá parar a geração

3. **Consultar Modelos Disponíveis**:
   - Use o comando "Get Available Models"
   - Você verá a lista de modelos que pode usar com sua conta

### Recomendações

- Mantenha sua chave API segura e não a compartilhe
- Monitore seu uso de créditos regularmente
- Use o modelo mais apropriado para seu caso de uso:
  - `deepseek-chat`: Para interações conversacionais gerais e geração de texto
  - `deepseek-reasoner`: Para tarefas que requerem análise lógica e raciocínio detalhado
- Ajuste a temperatura com base na necessidade de respostas mais precisas (0) ou criativas (1)
- O valor padrão de temperatura é 1.0
- O limite padrão de tokens é 2048
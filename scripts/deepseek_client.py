# Variable global para almacenar la conexión
deepseek_client = None

def set_deepseek_client(client):
    """
    Establece el cliente global de DeepseekAI.
    
    Args:
        client: Cliente de DeepseekAI inicializado (instancia de DeepSeekAPI)
    """
    global deepseek_client
    deepseek_client = client

def get_deepseek_client():
    """
    Obtiene el cliente global de DeepseekAI.
    
    Returns:
        El cliente de DeepseekAI o None si no está inicializado
    """
    global deepseek_client
    return deepseek_client
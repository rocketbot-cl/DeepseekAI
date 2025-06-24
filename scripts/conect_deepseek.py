from deepseek.api import DeepSeekAPI
import traceback
from deepseek_client import set_deepseek_client

def connect_to_deepseek(api_key, result_var, SetVar, PrintException):
    """
    Conectar a DeepseekAI usando el SDK oficial.

    Args:
        api_key: API key para autenticar con DeepseekAI
        result_var: Nombre de la variable para almacenar el resultado
        SetVar: Función para establecer variables en Rocketbot
        PrintException: Función para imprimir excepciones en Rocketbot
    """
    try:
        # Establecer el resultado como False por defecto
        SetVar(result_var, False)
        
        print("Starting connection with DeepSeek AI...")
        print(f"API Key (masked): {'*' * (len(api_key)-4) + api_key[-4:] if api_key else 'Not provided'}")
        
        # Validaciones básicas
        if not api_key or not isinstance(api_key, str):
            raise ValueError("API key must be a valid string")
            
        if not api_key.startswith("sk-"):
            raise ValueError("API key must start with 'sk-'")
        
        # Intentar crear el cliente y listar modelos
        client = DeepSeekAPI(api_key=api_key)
        set_deepseek_client(client)
        models = client.get_models()
        
        # Mostrar modelos disponibles
        print("Available models:", models)
        SetVar(result_var, True)
        print("✓ Connection established successfully!")
        
    except Exception as e:
        print(f"Error during connection: {str(e)}")
        print(traceback.format_exc())
        SetVar(result_var, False)
        if PrintException:
            PrintException()
        raise
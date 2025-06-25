from deepseek_client import get_deepseek_client
import traceback
from typing import Optional, Union


def generate_text(
    prompt: str,
    model: str,
    result_var: str,
    temperature: Optional[Union[float, str]] = None,
    max_tokens: Optional[Union[int, str]] = None,
    stop_sequence: Optional[str] = None,
    SetVar=None,
    PrintException=None
):
    """
    Genera texto usando el cliente de DeepseekAI y asigna el resultado a la variable especificada.

    Args:
        prompt: El prompt de entrada para la generación de texto.
        model: El modelo a usar para la generación de texto.
        result_var: Nombre de la variable para almacenar el texto generado.
        temperature: Temperatura para la generación (entre 0 y 1).
        max_tokens: Número máximo de tokens a generar.
        stop_sequence: Secuencia opcional para detener la generación.
        SetVar: Función para establecer variables en Rocketbot.
        PrintException: Función para imprimir excepciones en Rocketbot.
    """
    try:
        print("\n=== Generating text with DeepseekAI ===")
        
        # Establecer resultado por defecto
        SetVar(result_var, None)
        
        # Obtener el cliente
        client = get_deepseek_client()
        if not client:
            error_msg = "ERROR: You must connect to DeepseekAI before using this command. Please run the connection module first."
            print(error_msg)
            raise Exception(error_msg)

        # Validar parámetros requeridos
        if not prompt:
            error_msg = "ERROR: Prompt is required."
            print(error_msg)
            raise Exception(error_msg)
            
        if not model:
            error_msg = "ERROR: Model is required."
            print(error_msg)
            raise Exception(error_msg)

        # Convertir parámetros a sus tipos correctos
        try:
            temp = float(temperature) if temperature else 0.5
            if not (0 <= temp <= 1):
                print(f"WARNING: Temperature {temp} is outside recommended range [0-1]. Clamping to range.")
                temp = max(0, min(temp, 1))
                
            max_tok = int(max_tokens) if max_tokens else 400
            stop_sequences = [stop_sequence] if stop_sequence else None
            
        except ValueError as e:
            error_msg = f"ERROR: Error converting parameters: {str(e)}"
            print(error_msg)
            raise Exception(error_msg)

        print("\nGeneration parameters:")
        print(f"- Model: {model}")
        print(f"- Temperature: {temp}")
        print(f"- Maximum tokens: {max_tok}")
        print(f"- Stop sequences: {stop_sequences}")
        
        print("\nGenerating response...")
        try:
            # Usar el método de chat_completion de la API de DeepSeek
            response = client.chat_completion(
                prompt=prompt,
                model=model,
                temperature=temp,
                max_tokens=max_tok,
                stop=stop_sequences
            )
            
            # El resultado viene directamente como texto
            generated_text = response
            
            print("\n✓ Text generated successfully!")
            
            # Guardar el resultado
            SetVar(result_var, generated_text)

        except Exception as e:
            error_str = str(e)
            if "404" in error_str:
                error_msg = f"ERROR: Model '{model}' not found. This could mean:\n" \
                          f"1. The model name is incorrect\n" \
                          f"2. The model is not available in your region\n" \
                          f"3. The model requires special access\n\n" \
                          f"To see available models you can:\n" \
                          f"1. Run the 'Get available models' command from the module\n" \
                          f"2. Check the official DeepSeek documentation"
                print(error_msg)
                raise Exception(error_msg)
            elif "429" in error_str:
                error_msg = "ERROR: Rate limit exceeded. Please wait a moment before trying again."
                print(error_msg)
                raise Exception(error_msg)
            else:
                error_msg = f"ERROR: An API error occurred: {error_str}\n" \
                          f"This could be due to:\n" \
                          f"1. Network connectivity issues\n" \
                          f"2. Server-side problems\n" \
                          f"3. Invalid API key or authentication issues\n\n" \
                          f"Please try again in a few moments. If the problem persists, verify your connection and API key."
                print(error_msg)
                raise Exception(error_msg)

    except Exception as e:
        error_msg = f"Error generating text: {str(e)}"
        print(error_msg)
        print("\nError details:")
        print(traceback.format_exc())
        if PrintException:
            PrintException()
        raise Exception(error_msg)

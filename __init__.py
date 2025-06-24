# coding: utf-8
"""
Módulo Rocketbot para conectarse con DeepseekAI usando su SDK oficial.

Para obtener el módulo/función que se está llamando:
    GetParams("module")

Para obtener variables desde Rocketbot:
    var = GetParams("nombre_variable")

Para modificar variables en Rocketbot:
    SetVar("nombre_variable", valor)

Para instalar el SDK:
    pip install deepseek -t libs
"""

import os
import sys

base_path = tmp_global_obj["basepath"]  # type: ignore
cur_path = base_path + 'modules' + os.sep + 'DeepseekAI' + os.sep + 'scripts' + os.sep
libs_path = base_path + 'modules' + os.sep + 'DeepseekAI' + os.sep + 'libs' + os.sep
GetParams = GetParams  # type: ignore
SetVar = SetVar  # type: ignore
PrintException = PrintException  # type: ignore

if cur_path not in sys.path:
    sys.path.append(cur_path)

# Agregar la carpeta 'libs' al path si no está ya
if libs_path not in sys.path:
    sys.path.append(libs_path)

module = GetParams("module")

from conect_deepseek import connect_to_deepseek  # type: ignore
from get_models import get_models  # type: ignore
from generate_text import generate_text  # type: ignore

try:
    if module == "connect":
        api_key = GetParams("api_key")
        result_var = GetParams("result_var")
        connect_to_deepseek(api_key, result_var, SetVar, PrintException)

    elif module == "get_models":
        result_var = GetParams("result_var")
        get_models(result_var, SetVar, PrintException)

    elif module == "generate_text":
        prompt = GetParams("prompt")
        model = GetParams("model")
        result_var = GetParams("result_var")
        temperature = GetParams("temperature")
        max_completion_tokens = GetParams("max_tokens")
        stop_sequence = GetParams("stop_sequence")

        generate_text(
            prompt=prompt,
            model=model,
            result_var=result_var,
            temperature=temperature,
            max_tokens=max_completion_tokens,
            stop_sequence=stop_sequence,
            SetVar=SetVar,
            PrintException=PrintException
        )

    else:
        raise Exception(f"El módulo '{module}' no está implementado.")
except Exception as e:
    PrintException()
    raise e

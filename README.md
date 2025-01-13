# Chatbot con Gemini AI o OpenAI

Este proyecto implementa un chatbot simple utilizando la API de Google Gemini AI con capacidad de almacenamiento en base de datos SQLite.

## Características

- Integración con Google Gemini AI para generar respuestas
- Almacenamiento de conversaciones en base de datos SQLite
- Interfaz de menú por consola
- Historial de conversaciones consultable

## Requisitos Previos

- Python 3.7 o superior
- Una API key de Google Gemini (obtener en https://makersuite.google.com/app/apikey)

## Instalación

1. Clona el repositorio o descarga los archivos

2. Instala las dependencias necesarias:

```bash
pip install -r requirements.txt
```

3. Configura tu API key de Google Gemini o OpenAI en el archivo `config.py`

## Uso

1. Ejecuta el programa principal:

```bash
python main.py
```

2. El menú te mostrará tres opciones:
   - 1: Hacer una pregunta
   - 2: Ver historial
   - 3: Salir

3. Para hacer una pregunta:
   - Selecciona la opción 1
   - Escribe tu pregunta
   - La respuesta se mostrará y se guardará automáticamente

4. Para ver el historial:
   - Selecciona la opción 2
   - Se mostrarán todas las conversaciones previas ordenadas por fecha

## Base de Datos

La base de datos `chat_history.db` se crea automáticamente con la siguiente estructura:

- Tabla: `conversaciones`
  - `id`: Identificador único (autoincremental)
  - `pregunta`: Texto de la pregunta
  - `respuesta`: Texto de la respuesta
  - `fecha`: Fecha y hora de la conversación

## Herramientas Recomendadas

Para visualizar la base de datos, puedes usar:
- DB Browser for SQLite (https://sqlitebrowser.org/)
- SQLite Studio (https://sqlitestudio.pl/)

## Solución de Problemas

Si encuentras algún error:
1. Verifica que tu API key sea válida
2. Asegúrate de tener todas las dependencias instaladas
3. Comprueba que tienes permisos de escritura en la carpeta para crear la base de datos

## Contribuir

Siéntete libre de:
- Reportar bugs
- Sugerir nuevas características
- Enviar pull requests

## Licencia

Este proyecto está bajo la Licencia MIT.
# chat-bot-AI

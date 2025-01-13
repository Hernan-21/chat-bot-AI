import google.generativeai as genai
import sqlite3
from datetime import datetime

# Configuración de Gemini
GOOGLE_API_KEY = "tu_clave_api_aqui"
genai.configure(api_key=GOOGLE_API_KEY)

def inicializar_db():
    """Crear la base de datos y la tabla si no existen"""
    conn = sqlite3.connect('chat_history.db')
    cursor = conn.cursor()
    
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS conversaciones (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        pregunta TEXT NOT NULL,
        respuesta TEXT NOT NULL,
        fecha TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    )
    ''')
    
    conn.commit()
    conn.close()

def guardar_conversacion(pregunta, respuesta):
    """Guardar la conversación en la base de datos"""
    conn = sqlite3.connect('chat_history.db')
    cursor = conn.cursor()
    
    cursor.execute('''
    INSERT INTO conversaciones (pregunta, respuesta, fecha)
    VALUES (?, ?, ?)
    ''', (pregunta, respuesta, datetime.now()))
    
    conn.commit()
    conn.close()

def obtener_historial():
    """Obtener todas las conversaciones guardadas"""
    conn = sqlite3.connect('chat_history.db')
    cursor = conn.cursor()
    
    cursor.execute('SELECT * FROM conversaciones ORDER BY fecha DESC')
    conversaciones = cursor.fetchall()
    
    conn.close()
    return conversaciones

def hacer_pregunta(pregunta):
    try:
        modelo = genai.GenerativeModel('gemini-pro')
        respuesta = modelo.generate_content(pregunta)
        return respuesta.text
    except Exception as e:
        return f"Ocurrió un error: {str(e)}"

def mostrar_menu():
    print("\n=== MENÚ ===")
    print("1. Hacer una pregunta")
    print("2. Ver historial")
    print("3. Salir")
    return input("Selecciona una opción: ")

if __name__ == "__main__":
    inicializar_db()
    
    while True:
        opcion = mostrar_menu()
        
        if opcion == "1":
            pregunta = input("\nEscribe tu pregunta: ")
            respuesta = hacer_pregunta(pregunta)
            print(f"\nRespuesta: {respuesta}")
            guardar_conversacion(pregunta, respuesta)
            
        elif opcion == "2":
            print("\n=== HISTORIAL DE CONVERSACIONES ===")
            for conv in obtener_historial():
                print(f"\nID: {conv[0]}")
                print(f"Fecha: {conv[3]}")
                print(f"Pregunta: {conv[1]}")
                print(f"Respuesta: {conv[2]}")
                print("-" * 50)
                
        elif opcion == "3":
            print("¡Hasta luego!")
            break
            
        else:
            print("Opción no válida. Por favor, intenta de nuevo.") 
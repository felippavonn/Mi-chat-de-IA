
import streamlit as st  # Importa la librería Streamlit para crear la app web
from groq import Groq

st.set_page_config(page_title="Mi chat de IA", page_icon="🎉")  # Configura el título y el ícono de la página

st.title("Hola, esta es mi primera aplicación con streamlit")  # Muestra un título grande en la página

nombre = st.text_input("¿Cuál es tu nombre?")  # Crea una caja de texto donde el usuario escribe su nombre

if st.button("Saludar"): #Crea un botón que dice "Saludar"
    st.write(f"¡Hola, {nombre}! me caes mal")  # Muestra un mensaje personalizado cuando aprieta el botón

MODELOS = ['llama-3.1-8b-instant', 'llama-3.3-70b-versatile', 'deepseek-r1-distill-llama-70b']

def configurar_pagina():  # Define una función llamada configurar_pagina
    st.title("Mi chat de IA")  # Muestra un título dentro de la función
    st.sidebar.title("Configuración de la IA")  # Crea un título en la barra lateral
    elegirModelo = st.sidebar.selectbox('Elegí un Modelo', options=MODELOS, index=0)  # Crea un menú desplegable para elegir un modelo
    return elegirModelo  # Devuelve el modelo que el usuario eligió


modelo = configurar_pagina()  # Llama a la función y guarda el modelo elegido en la variable "modelo"

def crear_usuario_groq():
    clave_secreta = st.secrets["CLAVE_API"]
    return Groq(api_key=clave_secreta)

def configurar_modelo(cliente, modelo, mensajeDeEntrada):
    return cliente.chat.completions.create(
        model=modelo,
        messages=[{"role": "user", "content": mensajeDeEntrada}],
        stream=True
    )

def inicializar_estado():
    if "mensajes" not in st.session_state:
        st.session_state.mensajes = []

clienteUsuario = crear_usuario_groq()
inicializar_estado()

# Tomamos el mensaje del usuario por el input.
mensaje = st.chat_input("Escribí tu mensaje:")

# Verificamos que el mensaje no esté vacío antes de configurar el modelo
if mensaje:
    configurar_modelo(clienteUsuario, modelo, mensaje)
    print(mensaje)  # Mostramos el mensaje en la terminal para ver cómo se muestra
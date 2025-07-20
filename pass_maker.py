import customtkinter as ctk
from tkinter import messagebox

import string
import random

# --- 1.- Lógica de 'Genenración de contraseñas'

def generar_contraseña(longitud=12):
    caracteres = string.ascii_letters + string.digits + string.punctuation

    contraseña = ''.join(random.choice(caracteres) for i in range (longitud))
    return contraseña


# --- 2.- Funcion para la interacción de la GUI.
def mostrar_contraseña_en_gui():
    try:
        longitud_str = entrada_longitud.get()
        longitud = int(longitud_str)

        if longitud <= 0:
            messagebox.showerror("Error", "La longitud debe ser un número positivo.")
            return

        contraseña_generada = generar_contraseña(longitud)
        etiqueta_resultado.configure(text=contraseña_generada) # Usamos .configure() para CTkLabel

    except ValueError:
        messagebox.showerror("Error", "Por favor, introduce un número válido para la longitud.")
    except Exception as e:
        messagebox.showerror("Error Inesperado", f"Ocurrió un error: {e}")


# --- 3. Configuración de la Ventana Principal de CustomTkinter ---
# Configura el tema y el color de los widgets
ctk.set_appearance_mode("System")  # Modes: "System" (standard), "Dark", "Light"
ctk.set_default_color_theme("green")  # Themes: "blue" (standard), "green", "dark-blue"

ventana = ctk.CTk() # Crea la ventana principal de CustomTkinter
ventana.title("Generador de Contraseñas Seguras")
ventana.geometry("480x280") # Un poco más grande para el estilo moderno
ventana.resizable(False, False)

# --- 4. Creación de Elementos (Widgets) de CustomTkinter ---

# Frame para agrupar los elementos y dar un mejor diseño
frame_principal = ctk.CTkFrame(ventana, corner_radius=10)
frame_principal.pack(pady=20, padx=20, fill="both", expand=True)

# Etiqueta para indicar al usuario qué hacer
etiqueta_instruccion = ctk.CTkLabel(frame_principal, text="Introduce la longitud deseada:", font=ctk.CTkFont(size=16, weight="bold"))
etiqueta_instruccion.pack(pady=(10, 5)) # Un poco más de padding arriba

# Campo de entrada de texto (Entry) para la longitud de la contraseña
entrada_longitud = ctk.CTkEntry(frame_principal, width=200, height=30, placeholder_text="Ej: 12", font=ctk.CTkFont(size=14))
entrada_longitud.insert(0, "12") # Valor inicial por defecto en el campo de entrada
entrada_longitud.pack(pady=5)

# Botón para generar la contraseña
boton_generar = ctk.CTkButton(frame_principal, text="Generar Contraseña", command=mostrar_contraseña_en_gui, font=ctk.CTkFont(size=15, weight="bold"), height=40)
boton_generar.pack(pady=15)

# Etiqueta para mostrar la contraseña generada
etiqueta_resultado = ctk.CTkLabel(frame_principal, text="Contraseña Generada Aquí", font=ctk.CTkFont(family="monospace", size=16, weight="bold"), text_color="green")
etiqueta_resultado.pack(pady=10)

# --- 5. Iniciar el Bucle Principal de la Aplicación ---
ventana.mainloop()

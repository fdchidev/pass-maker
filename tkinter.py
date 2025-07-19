import tkinter as tk
from tkinter import messagebox
import random
import string

def generar_contrasena(longitud=12):
    caracteres = string.ascii_letters + string.digits + string.punctuation
    contrasena = ''.join(random.choice(caracteres) for i in range(longitud))
    return contrasena

def mostrar_contrasena():
    try:
        longitud = int(entrada_longitud.get())
        if longitud <= 0:
            messagebox.showerror("Error", "La longitud debe ser un número positivo.")
            return
        contrasena_generada = generar_contrasena(longitud)
        etiqueta_resultado.config(text=contrasena_generada)
    except ValueError:
        messagebox.showerror("Error", "Por favor, introduce un número válido para la longitud.")

# Configuración de la ventana principal
ventana = tk.Tk()
ventana.title("Generador de Contraseñas")
ventana.geometry("400x200") # Ancho x Alto

# Etiqueta para la longitud
etiqueta_longitud = tk.Label(ventana, text="Longitud de la contraseña:")
etiqueta_longitud.pack(pady=5)

# Campo de entrada para la longitud
entrada_longitud = tk.Entry(ventana)
entrada_longitud.insert(0, "12") # Valor por defecto
entrada_longitud.pack(pady=5)

# Botón para generar
boton_generar = tk.Button(ventana, text="Generar Contraseña", command=mostrar_contrasena)
boton_generar.pack(pady=10)



# Etiqueta para mostrar el resultado
etiqueta_resultado = tk.Label(ventana, text="", font=("Helvetica", 14, "bold"))
etiqueta_resultado.pack(pady=10)

# Iniciar el bucle principal de la aplicación
ventana.mainloop()
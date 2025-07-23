import customtkinter as ctk
from tkinter import messagebox
import string
import random

__version__ = "1.0.0" 

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
            messagebox.showerror("Error", "La longitud debe ser mayor a 4.")
            return

        contraseña_generada = generar_contraseña(longitud)
        etiqueta_resultado.configure(text=contraseña_generada) # Usamos .configure() para CTkLabel
        
        boton_copiar.configure(state="normal") # Esto debería ejecutarse después de que etiqueta_resultado se actualiza con una contraseña válida.

    except ValueError:
        messagebox.showerror("Error", "Por favor, introduce un número válido para la longitud.")
    except Exception as e:
        messagebox.showerror("Error Inesperado", f"Ocurrió un error: {e}")


# --- 3.- NUEVA: Función para Copiar la Contraseña al Portapapeles ---- 

def copiar_al_portapapeles():
    contrasena_a_copiar = etiqueta_resultado.cget("text") # Obtiene el texto actual de la etiqueta
    if contrasena_a_copiar and contrasena_a_copiar != "Contraseña Generada:": # Asegura que haya algo que copiar
        try:
            ventana.clipboard_clear()  # Limpia el portapapeles
            ventana.clipboard_append(contrasena_a_copiar) # Añade la contraseña
            # Opcional: mostrar un mensaje temporal de confirmación
            #CODE COMENTADO messagebox.showinfo("Copiado", "¡Contraseña copiada al portapapeles!")
            # Si quieres una retroalimentación más sutil y temporal:
            etiqueta_estado.configure(text="¡Copiado!", text_color="white")
            ventana.after(2000, lambda: etiqueta_estado.configure(text="")) # Desaparece después de 2 segundos
        except Exception as e:
            messagebox.showerror("Error al Copiar", f"No se pudo copiar al portapapeles: {e}")
    else:
        messagebox.showwarning("Advertencia", "No hay contraseña para copiar.")




# --- 4. Configuración de la Ventana Principal de CustomTkinter ---
# Configura el tema y el color de los widgets
ctk.set_appearance_mode("System")  # Modes: "System" (standard), "Dark", "Light"
ctk.set_default_color_theme("dark-blue")  # Themes: "blue" (standard), "green", "dark-blue"

ventana = ctk.CTk() # Crea la ventana principal de CustomTkinter
ventana.title("Generador de Contraseñas")
ventana.geometry("480x325") # Un poco más grande para el estilo moderno
ventana.resizable(False, False)

# --- 5. Creación de Elementos (Widgets) de CustomTkinter ---

# Frame para agrupar los elementos y dar un mejor diseño
frame_principal = ctk.CTkFrame(ventana, corner_radius=10)
frame_principal.pack(pady=20, padx=20, fill="both", expand=True)

# Etiqueta para indicar al usuario qué hacer
etiqueta_instruccion = ctk.CTkLabel(frame_principal, text="Introduce la longitud deseada:", font=ctk.CTkFont(size=16, weight="bold"), text_color='white')
etiqueta_instruccion.pack(pady=(10, 5)) # Un poco más de padding arriba

# Campo de entrada de texto (Entry) para la longitud de la contraseña
entrada_longitud = ctk.CTkEntry(frame_principal, width=200, height=30, placeholder_text="Ej: 12", font=ctk.CTkFont(size=14))
entrada_longitud.insert(0, "12") # Valor inicial por defecto en el campo de entrada
entrada_longitud.pack(pady=5)

# Botón para generar la contraseña
boton_generar = ctk.CTkButton(frame_principal, text="Generar Contraseña", command=mostrar_contraseña_en_gui, font=ctk.CTkFont(size=16, weight="bold"), height=40)
boton_generar.pack(pady=15)

# Etiqueta para mostrar la contraseña generada
etiqueta_resultado = ctk.CTkLabel(frame_principal, text="Contraseña Generada:", font=ctk.CTkFont(family="monospace", size=16, weight="bold"), text_color="white")
etiqueta_resultado.pack(pady=10)



# --- NUEVO: Botón para Copiar al Portapapeles ---
boton_copiar = ctk.CTkButton(frame_principal, text="Copiar Contraseña", command=copiar_al_portapapeles, font=ctk.CTkFont(size=16, weight="bold"),  height=40, state="disabled") # Inicialmente deshabilitado disabled
boton_copiar.pack(pady=(5))

# Opcional: Etiqueta de estado para mensajes temporales (si no usas messagebox para "Copiado!")
etiqueta_estado = ctk.CTkLabel(frame_principal, text="", font=ctk.CTkFont(size=16))
etiqueta_estado.pack(pady=(0,10))



# --- 6. Iniciar el Bucle Principal de la Aplicación ---
ventana.mainloop()


import tkinter as tk
from tkinter import messagebox

# Variables globales para el estado de usuario
logged_in_user = None

# Función para verificar si el usuario ha hecho log out
def verify_user_login():
    if logged_in_user:
        main_window()
    else:
        login_window()

# Función para limpiar la ventana actual
def clear_window():
    for widget in root.winfo_children():
        widget.destroy()

# Función para cambiar tema claro/oscuro
def toggle_theme(theme):
    if theme == "dark":
        root.tk_setPalette(background="#333", foreground="#fff")
    else:
        root.tk_setPalette(background="#fff", foreground="#000")

# Función para mostrar el contenido de login
def login_window():
    clear_window()

    def login():
        global logged_in_user
        username = entry_user.get()
        password = entry_pass.get()
        
        # Validar login con base de datos
        if username == "admin" and password == "password":
            logged_in_user = username
            main_window()
        else:
            messagebox.showerror("Error", "Credenciales incorrectas")

    tk.Label(root, text="Usuario").pack(pady=10)
    entry_user = tk.Entry(root)
    entry_user.pack()

    tk.Label(root, text="Contraseña").pack(pady=10)
    entry_pass = tk.Entry(root, show='*')
    entry_pass.pack()

    tk.Button(root, text="Login", command=login).pack(pady=20)
    tk.Button(root, text="Registrarse", command=register_window).pack()

# Función para mostrar el contenido de registro
def register_window():
    clear_window()

    def register():
        email = entry_email.get()
        username = entry_user.get()
        password = entry_pass.get()
        password2 = entry_pass2.get()
        # Validar registro e enviarlo a la base de datos (hay que encriptar las contraseñas)
        if password == password2:
            messagebox.showinfo("Registro", "Usuario registrado exitosamente")
            login_window()
        else:
            messagebox.showerror("Error", "Las contraseñas no coinciden")

    tk.Label(root, text="Email").pack(pady=10)
    entry_email = tk.Entry(root)
    entry_email.pack()

    tk.Label(root, text="Usuario").pack(pady=10)
    entry_user = tk.Entry(root)
    entry_user.pack()

    tk.Label(root, text="Contraseña").pack(pady=10)
    entry_pass = tk.Entry(root, show='*')
    entry_pass.pack()

    tk.Label(root, text="Confirmar Contraseña").pack(pady=10)
    entry_pass2 = tk.Entry(root, show='*')
    entry_pass2.pack()

    tk.Button(root, text="Registrarse", command=register).pack(pady=20)



# Función para mostrar la ventana de ayuda
def help_window():
    clear_window()
    tk.Label(root, text="Texto explicativo aquí.\nContacto: contacto@soporte.com").pack(pady=20)
    tk.Button(root, text="Volver", command=main_window).pack(pady=20)

# Función para mostrar la ventana de configuración
def settings_window():
    clear_window()

    def toggle_fullscreen():
        root.attributes('-fullscreen', not root.attributes('-fullscreen'))

    tk.Label(root, text="Modo de Tema").pack(pady=10)
    theme_var = tk.StringVar(value="light")
    tk.Radiobutton(root, text="Claro", variable=theme_var, value="light", command=lambda: toggle_theme("light")).pack()
    tk.Radiobutton(root, text="Oscuro", variable=theme_var, value="dark", command=lambda: toggle_theme("dark")).pack()

    tk.Button(root, text="Pantalla Completa", command=toggle_fullscreen).pack(pady=20)
    tk.Button(root, text="Volver", command=main_window).pack(pady=20)

# Función para mostrar la ventana de usuario
def user_window():
    clear_window()

    def change_username():
        new_user = entry_new_user.get()
        if new_user:
            global logged_in_user
            logged_in_user = new_user
            messagebox.showinfo("Éxito", "Nombre de usuario actualizado")
            main_window()

    tk.Label(root, text=f"Usuario actual: {logged_in_user}").pack(pady=10)
    tk.Label(root, text="Nuevo nombre de usuario:").pack(pady=10)
    entry_new_user = tk.Entry(root)
    entry_new_user.pack()

    tk.Button(root, text="Cambiar nombre", command=change_username).pack(pady=10)
    tk.Button(root, text="Cerrar sesión", command=logout).pack(pady=10)
    tk.Button(root, text="Volver", command=main_window).pack(pady=20)

# Función para cerrar sesión
def logout():
    global logged_in_user
    logged_in_user = None
    messagebox.showinfo("Sesión", "Has cerrado sesión")
    login_window()

# Ventana principal con opciones de gramática, etc.
def main_window():
    clear_window()

    def open_grammar():
        messagebox.showinfo("Grammar", "Ventana de Gramática")

    def open_speaking():
        messagebox.showinfo("Speaking", "Ventana de Speaking")

    def open_writing():
        messagebox.showinfo("Writing", "Ventana de Writing")

    def open_reading():
        messagebox.showinfo("Reading", "Ventana de Reading")

    def open_listening():
        messagebox.showinfo("Listening", "Ventana de Listening")

    # Crear menú desplegable
    menu_bar = tk.Menu(root)
    user_menu = tk.Menu(menu_bar, tearoff=0)
    user_menu.add_command(label="Ayuda", command=help_window)
    user_menu.add_command(label="Usuario", command=user_window)
    user_menu.add_command(label="Configuración", command=settings_window)
    menu_bar.add_cascade(label="Opciones", menu=user_menu)
    root.config(menu=menu_bar)

    tk.Label(root, text="Bienvenido a la Aplicación de Idiomas", font=("Arial", 16)).pack(pady=20)

    # Opciones de aprendizaje
    tk.Button(root, text="Grammar", command=open_grammar).pack(pady=10)
    tk.Button(root, text="Speaking", command=open_speaking).pack(pady=10)
    tk.Button(root, text="Writing", command=open_writing).pack(pady=10)
    tk.Button(root, text="Reading", command=open_reading).pack(pady=10)
    tk.Button(root, text="Listening", command=open_listening).pack(pady=10)



# Inicializar la aplicación
root = tk.Tk()
root.title("Traitor Translator")
verify_user_login()

root.mainloop()
import tkinter as tk
from tkinter import messagebox
import random
import pygame
import os
from connect import validate_user, register_user, save_user_data, load_user_data, delete_user_data, get_connection

pygame.mixer.init()

# Variables globales para el estado de usuario y +
logged_in_user = None
high_scores = {"facil": 0, "medio": 0, "dificil": 0}
difficulty_mapping = {"facil": 1, "medio": 2, "dificil": 3}
AUDIO_FOLDER = os.path.join(os.path.dirname(__file__), "audio")
# Mapeo de niveles del listening
LEVELS = {
    "facil": "nivel_1",
    "medio": "nivel_2",
    "dificil": "nivel_3"
}

# Variables globales listening
current_word = ""
current_audio = ""
current_level = ""
score = 0
attempts = 0

# Función para verificar si el usuario ha hecho log out
def verify_user_login():
    user_data = load_user_data()
    if user_data and validate_user(user_data["username"], user_data.get("password", "")):
        global logged_in_user
        logged_in_user = user_data["username"]
        main_window()
    else:
        login_window()


def create_centered_window(root, title, width, height):
    root.title(title)
    root.geometry(f"{width}x{height}")
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    x = (screen_width // 2) - (width // 2)
    y = (screen_height // 2) - (height // 2)
    root.geometry(f"{width}x{height}+{x}+{y}")

# Función para limpiar la ventana actual
def clear_window():
    for widget in root.winfo_children():
        widget.destroy()
    
def create_centered_window(root, title, width, height):
    root.title(title)
    root.geometry(f"{width}x{height}")
    root.resizable(False, False)
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    x = (screen_width // 2) - (width // 2)
    y = (screen_height // 2) - (height // 2)
    root.geometry(f"{width}x{height}+{x}+{y}")
    root.configure(bg="#2C3E50")


# Función para mostrar el contenido de login
def login_window():
    clear_window()
    tk.Label(root, text="Iniciar Sesión", font=("Arial", 16, "bold"), bg="#2C3E50", fg="white").pack(pady=20)

    def login():
        global logged_in_user
        username = entry_user.get()
        password = entry_pass.get()

        # Validar login con base de datos
        if validate_user(username, password):
            logged_in_user = username
            save_user_data(username, password)
            main_window()
        else:
            messagebox.showerror("Error", "Credenciales incorrectas")

    tk.Label(root, text="Usuario", bg="#2C3E50", fg="white").pack()
    entry_user = tk.Entry(root)
    entry_user.pack()

    tk.Label(root, text="Contraseña", bg="#2C3E50", fg="white").pack()
    entry_pass = tk.Entry(root, show='*')
    entry_pass.pack()

<<<<<<< HEAD
    
    tk.Button(root, text="Login", command=login, font=("Arial", 12), 
          bg="#3498DB", fg="white", bd=0, padx=10, pady=5, width=20, 
          highlightthickness=2, highlightbackground="white").pack(pady=20)
    tk.Button(root, text="Registrarse", command=register_window, font=("Arial", 12), 
          bg="#3498DB", fg="white", bd=0, padx=10, pady=5, width=20, 
          highlightthickness=2, highlightbackground="white").pack(pady=0)
    
    
=======
    tk.Button(root, text="Login", command=login, font=("Arial", 12), bg="#3498DB", 
          fg="white", bd=0, padx=10, pady=5, width=20, 
          highlightthickness=2, highlightbackground="white").pack(pady=5)

    tk.Button(root, text="Registrarse", command=register_window, font=("Arial", 12), 
          bg="#3498DB", fg="white", bd=0, padx=10, pady=5, width=20, 
          highlightthickness=2, highlightbackground="white").pack(pady=5)



>>>>>>> 7f12b97b83037688d663b9c9b4f35ff45eeb94db

# Función para mostrar el contenido de registro
def register_window():
    clear_window()
    tk.Label(root, text="Crear Cuenta", font=("Arial", 16, "bold"), bg="#2C3E50", fg="white").pack(pady=20)     
    def register():
        username = entry_user.get()
        password = entry_pass.get()
        password2 = entry_pass2.get()
        email = entry_email.get()

        # Validar registro e enviarlo a la base de datos
        if password == password2:
            if register_user(9, username, password, email):
                messagebox.showinfo("Registro", "Usuario registrado exitosamente")
                logged_in_user = username
                save_user_data(username, password)
                main_window()
            else:
                messagebox.showerror("Error", "No se pudo registrar el usuario")
        else:
            messagebox.showerror("Error", "Las contraseñas no coinciden")

    tk.Label(root, text="Email", bg="#2C3E50", fg="white").pack()
    entry_email = tk.Entry(root)
    entry_email.pack()

    tk.Label(root, text="Usuario", bg="#2C3E50", fg="white").pack()
    entry_user = tk.Entry(root)
    entry_user.pack()

    tk.Label(root, text="Contraseña", bg="#2C3E50", fg="white").pack()
    entry_pass = tk.Entry(root, show='*')
    entry_pass.pack()

    tk.Label(root, text="Confirmar Contraseña", bg="#2C3E50", fg="white").pack()
    entry_pass2 = tk.Entry(root, show='*')
    entry_pass2.pack()
<<<<<<< HEAD

    tk.Button(root, text="Registrarse", command=register, font=("Arial", 12), 
          bg="#3498DB", fg="white", bd=0, padx=10, pady=5, width=20, 
          highlightthickness=2, highlightbackground="white").pack(pady=20)
=======
    
    tk.Button(root, text="Registrarse", command=register, font=("Arial", 12), 
          bg="#3498DB", fg="white", bd=0, padx=10, pady=5, width=20, 
          highlightthickness=2, highlightbackground="white").pack(pady=5)
>>>>>>> 7f12b97b83037688d663b9c9b4f35ff45eeb94db

# Función para cerrar sesión
def logout():
    global logged_in_user
    logged_in_user = None
    delete_user_data()
    messagebox.showinfo("Sesión", "Has cerrado sesión")
    login_window()

# Función para mostrar la ventana de ayuda
def help_window():
    clear_window()
    tk.Label(root, text="Texto explicativo aquí.\nContacto: contacto@soporte.com").pack(pady=20)
    
    tk.Button(root, text="Volver", command=main_window, font=("Arial", 12), 
          bg="#3498DB", fg="white", bd=0, padx=10, pady=5, width=20, 
          highlightthickness=2, highlightbackground="white").pack(pady=20)
    
def toggle_theme(theme):
    if theme == "dark":
        root.tk_setPalette(background="#333", foreground="#fff")
    else:
        root.tk_setPalette(background="#fff", foreground="#000")

# Función para mostrar la ventana de configuración
def settings_window():
    clear_window()

    def toggle_fullscreen():
        root.attributes('-fullscreen', not root.attributes('-fullscreen'))

    tk.Label(root, text="Modo de Tema").pack(pady=10)
    theme_var = tk.StringVar(value="light")
    tk.Radiobutton(root, text="Claro", variable=theme_var, value="light", command=lambda: toggle_theme("light")).pack()
    tk.Radiobutton(root, text="Oscuro", variable=theme_var, value="dark", command=lambda: toggle_theme("dark")).pack()
    
    tk.Button(root, text="Pantalla Completa", command=toggle_fullscreen, font=("Arial", 12), 
          bg="#3498DB", fg="white", bd=0, padx=10, pady=5, width=20, 
          highlightthickness=2, highlightbackground="white").pack(pady=10)
    tk.Button(root, text="Volver", command=main_window, font=("Arial", 12), 
          bg="#3498DB", fg="white", bd=0, padx=10, pady=5, width=20, 
          highlightthickness=2, highlightbackground="white").pack(pady=10)

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
    
    tk.Button(root, text="Cambiar nombre", command=change_username, font=("Arial", 12), 
          bg="#3498DB", fg="white", bd=0, padx=10, pady=5, width=20, 
          highlightthickness=2, highlightbackground="white").pack(pady=10)
    tk.Button(root, text="Cerrar sesión", command=logout, font=("Arial", 12), 
          bg="#3498DB", fg="white", bd=0, padx=10, pady=5, width=20, 
          highlightthickness=2, highlightbackground="white").pack(pady=10)
    tk.Button(root, text="Volver", command=main_window, font=("Arial", 12), 
          bg="#3498DB", fg="white", bd=0, padx=10, pady=5, width=20, 
          highlightthickness=2, highlightbackground="white").pack(pady=20)

# Ventana principal con opciones de gramática, etc.
def main_window():
    clear_window()
    # Crear menú desplegable
    menu_bar = tk.Menu(root)
    user_menu = tk.Menu(menu_bar, tearoff=0)
    user_menu.add_command(label="Ayuda", command=help_window)
    user_menu.add_command(label="Usuario", command=user_window)
    user_menu.add_command(label="Configuración", command=settings_window)
    menu_bar.add_cascade(label="Opciones", menu=user_menu)
    root.config(menu=menu_bar)

    tk.Label(root, text="Traitor Translator", font=("Arial", 16)).pack(pady=20)
    

    
    tk.Button(root, text="Vocabulary", command=words_game, font=("Arial", 12), 
          bg="#3498DB", fg="white", bd=0, padx=10, pady=5, width=20, 
          highlightthickness=2, highlightbackground="white").pack(pady=5)
    tk.Button(root, text="Phrases", command=phrases_game, font=("Arial", 12), 
          bg="#3498DB", fg="white", bd=0, padx=10, pady=5, width=20, 
          highlightthickness=2, highlightbackground="white").pack(pady=5)
    tk.Button(root, text="Reading", command=reading, font=("Arial", 12), 
          bg="#3498DB", fg="white", bd=0, padx=10, pady=5, width=20, 
          highlightthickness=2, highlightbackground="white").pack(pady=5)
    tk.Button(root, text="Listening", command=listening, font=("Arial", 12), 
          bg="#3498DB", fg="white", bd=0, padx=10, pady=5, width=20, 
          highlightthickness=2, highlightbackground="white").pack(pady=5)
    
    
def fetch_word(difficulty):
    conn = get_connection()
    cursor = conn.cursor()
    table = random.choice(["parEng", "parEsp"])
    opposite_table = "parEsp" if table == "parEng" else "parEng"
    query = f"""
        SELECT TOP 1 e.id_paraula, e.paraula, s.paraula FROM {table} e
        JOIN {opposite_table} s ON e.id_paraula = s.id_paraula
        WHERE e.id_nivel = ? ORDER BY NEWID()
    """
    cursor.execute(query, (difficulty_mapping[difficulty],))
    word = cursor.fetchone()
    conn.close()
    return word, table, opposite_table

def fetch_options_words(correct_word, correct_id, table, opposite_table, difficulty):
    conn = get_connection()
    cursor = conn.cursor()
    num_options = 3 if difficulty == "facil" else 5
    query = f"""
        SELECT paraula FROM {opposite_table} WHERE id_paraula <> ?
        ORDER BY ABS(id_paraula - ?) ASC OFFSET 0 ROWS FETCH NEXT {num_options - 1} ROWS ONLY
    """
    cursor.execute(query, (correct_id, correct_id))
    options = [row[0] for row in cursor.fetchall()]
    conn.close()
    options.append(correct_word)
    random.shuffle(options)
    return options

def words_game():
    clear_window()
    
    def start_game(difficulty):
        clear_window()
        score = 0
        rounds = 5

        def next_round(round_num):
            if round_num > rounds:
                messagebox.showinfo("Juego terminado", f"Puntuación final: {score}")
                if score > high_scores[difficulty]:
                    high_scores[difficulty] = score
                main_window()
                return
            
            clear_window()
            word_data, table, opposite_table = fetch_word(difficulty)
            if not word_data:
                messagebox.showerror("Error", "No se pudo obtener una palabra")
                main_window()
                return

            word_id, word, correct_word = word_data
            tk.Label(root, text=f"Traduce: {word}", font=("Arial", 14)).pack(pady=10)
            
            def check_answer(user_answer):
                nonlocal score
                if user_answer == correct_word:
                    score += 5
                    messagebox.showinfo("Resultado", "¡Correcto!")
                else:
                    if difficulty == "medio":
                        score -= 1
                    elif difficulty == "dificil":
                        score -= 3
                    messagebox.showerror("Resultado", f"Incorrecto. La respuesta correcta era: {correct_word}")
                root.after(2000, lambda: next_round(round_num + 1))
            
            if difficulty in ["facil", "medio"]:
                options = fetch_options_words(correct_word, word_id, table, opposite_table, difficulty)
                for option in options:
                    tk.Button(root, text=option, command=lambda opt=option: check_answer(opt), font=("Arial", 12), 
                    bg="#003366", fg="white", bd=0, padx=10, pady=5,  
                    highlightthickness=2, highlightbackground="white").pack(pady=5)
                    
                tk.Button(root, text="Volver", command=confirm_exit, font=("Arial", 12), 
                    bg="#3498DB", fg="white", bd=0, padx=10, pady=5, width=20, 
                    highlightthickness=2, highlightbackground="white").pack(pady=20)
            else:
                entry = tk.Entry(root)
                entry.pack(pady=5)
               
                
                tk.Button(root, text="Confirmar",command=lambda: check_answer(entry.get()), font=("Arial", 12), 
                    bg="#3498DB", fg="white", bd=0, padx=10, pady=5, width=20, 
                    highlightthickness=2, highlightbackground="white").pack(pady=5)
                
                tk.Button(root, text="Volver",command= confirm_exit, font=("Arial", 12), 
                    bg="#3498DB", fg="white", bd=0, padx=10, pady=5, width=20, 
                    highlightthickness=2, highlightbackground="white").pack(pady=20)

        next_round(1)
        
    tk.Label(root, text="Selecciona la dificultad", font=("Arial", 14)).pack(pady=10)
    
    tk.Button(root, text="Fácil",command=lambda: start_game("facil"), font=("Arial", 12), 
                    bg="#3498DB", fg="white", bd=0, padx=10, pady=5, width=20, 
                    highlightthickness=2, highlightbackground="white").pack(pady=5)
    tk.Button(root, text="Medio", command=lambda: start_game("medio"), font=("Arial", 12), 
                    bg="#3498DB", fg="white", bd=0, padx=10, pady=5, width=20, 
                    highlightthickness=2, highlightbackground="white").pack(pady=5)
    tk.Button(root, text="Difícil", command=lambda: start_game("dificil"), font=("Arial", 12), 
                    bg="#3498DB", fg="white", bd=0, padx=10, pady=5, width=20, 
                    highlightthickness=2, highlightbackground="white").pack(pady=5)
    def confirm_exit():
        if messagebox.askyesno("Confirmar", "¿Seguro que quieres salir al menú principal?"):
            main_window()
    
    tk.Button(root, text="Volver", command=confirm_exit, font=("Arial", 12), 
                    bg="#3498DB", fg="white", bd=0, padx=10, pady=5, width=20, 
                    highlightthickness=2, highlightbackground="white").pack(pady=20)
    
    

def fetch_phrase(difficulty):
    conn = get_connection()
    cursor = conn.cursor()
    table = random.choice(["frsEng", "frsEsp"])
    opposite_table = "frsEsp" if table == "frsEng" else "frsEng"
    query = f"""
        SELECT TOP 1 e.id_frase, e.frase, s.frase FROM {table} e
        JOIN {opposite_table} s ON e.id_frase = s.id_frase
        WHERE e.id_nivel = ? ORDER BY NEWID()
    """
    cursor.execute(query, (difficulty_mapping[difficulty],))
    phrase = cursor.fetchone()
    conn.close()
    return phrase, table, opposite_table

def fetch_phrase_options(correct_phrase, correct_id, table, opposite_table, difficulty):
    conn = get_connection()
    cursor = conn.cursor()
    num_options = {"facil": 3, "medio": 4, "dificil": 5}[difficulty]
    query = f"""
        SELECT frase FROM {opposite_table} WHERE id_frase <> ?
        ORDER BY ABS(id_frase - ?) ASC OFFSET 0 ROWS FETCH NEXT {num_options - 1} ROWS ONLY
    """
    cursor.execute(query, (correct_id, correct_id))
    options = [row[0] for row in cursor.fetchall()]
    conn.close()
    options.append(correct_phrase)
    random.shuffle(options)
    return options

def phrases_game():
    clear_window()
    
    def start_game(difficulty):
        clear_window()
        score = 0
        rounds = 5

        def next_round(round_num):
            if round_num > rounds:
                messagebox.showinfo("Juego terminado", f"Puntuación final: {score}")
                if score > high_scores[difficulty]:
                    high_scores[difficulty] = score
                main_window()
                return
            
            clear_window()
            phrase_data, table, opposite_table = fetch_phrase(difficulty)
            if not phrase_data:
                messagebox.showerror("Error", "No se pudo obtener una frase")
                main_window()
                return

            phrase_id, phrase, correct_phrase = phrase_data
            tk.Label(root, text=f"Traduce: {phrase}", font=("Arial", 14)).pack(pady=10)
            
            def check_answer(user_answer):
                nonlocal score
                if user_answer == correct_phrase:
                    score += 5
                    messagebox.showinfo("Resultado", "¡Correcto!")
                else:
                    if difficulty == "medio":
                        score -= 1
                    elif difficulty == "dificil":
                        score -= 3
                    messagebox.showerror("Resultado", f"Incorrecto. La respuesta correcta era: {correct_phrase}")
                root.after(2000, lambda: next_round(round_num + 1))
            
            if difficulty in ["facil", "medio", "dificil"]:
                options = fetch_phrase_options(correct_phrase, phrase_id, table, opposite_table, difficulty)
                for option in options:
                    tk.Button(root, text=option, command=lambda opt=option: check_answer(opt), font=("Arial", 12), 
                    bg="#003366", fg="white", bd=0, padx=10, pady=5, 
                    highlightthickness=2, highlightbackground="white").pack(pady=5)
                    
                tk.Button(root, text="Volver", command=confirm_exit, font=("Arial", 12), 
                    bg="#3498DB", fg="white", bd=0, padx=10, pady=5, width=20, 
                    highlightthickness=2, highlightbackground="white").pack(pady=20)
                

        next_round(1)
        
    tk.Label(root, text="Selecciona la dificultad", font=("Arial", 14)).pack(pady=10)
    
    tk.Button(root, text="Fácil", command=lambda: start_game("facil"), font=("Arial", 12), 
                    bg="#3498DB", fg="white", bd=0, padx=10, pady=5, width=20, 
                    highlightthickness=2, highlightbackground="white").pack(pady=5)
    tk.Button(root, text="Medio", command=lambda: start_game("medio"), font=("Arial", 12), 
                    bg="#3498DB", fg="white", bd=0, padx=10, pady=5, width=20, 
                    highlightthickness=2, highlightbackground="white").pack(pady=5)
    tk.Button(root, text="Difícil", command=lambda: start_game("dificil"), font=("Arial", 12), 
                    bg="#3498DB", fg="white", bd=0, padx=10, pady=5, width=20, 
                    highlightthickness=2, highlightbackground="white").pack(pady=5)
    
    def confirm_exit():
        if messagebox.askyesno("Confirmar", "¿Seguro que quieres salir al menú principal?"):
            main_window()

    tk.Button(root, text="Volver", command=confirm_exit, font=("Arial", 12), 
                    bg="#3498DB", fg="white", bd=0, padx=10, pady=5, width=20, 
                    highlightthickness=2, highlightbackground="white").pack(pady=20)

def load_reading_text(difficulty):
    file_number = random.choice([1, 2, 3])
    file_path = f"texts/{difficulty}/texto{file_number}.txt"
    try:
        with open(file_path, "r", encoding="utf-8") as file:
            content = file.read().strip().split("\n\n")
        if len(content) < 2:
            raise ValueError("Formato de archivo incorrecto")
        text = content[0]
        questions = []
        for q in content[1:]:
            lines = q.strip().split("\n")
            if len(lines) < 5:
                continue  # Ignorar preguntas mal formateadas
            question_text = lines[0]
            options = lines[1:4]
            correct_line = lines[4].split(": ")
            if len(correct_line) < 2:
                continue  # Ignorar preguntas sin respuesta correcta válida
            correct_answer = correct_line[1]
            questions.append((question_text, options, correct_answer))
        if not questions:
            raise ValueError("No hay preguntas válidas en el archivo")
        return text, questions
    except (FileNotFoundError, ValueError) as e:
        messagebox.showerror("Error", f"Error al cargar el archivo: {e}")
        return None, None


def reading():
    clear_window()
    
    def start_reading(difficulty):
        clear_window()
        text, questions = load_reading_text(difficulty)
        if not text or not questions:
            main_window()
            return
        
        tk.Label(root, text=text, wraplength=500, justify="left", font=("Arial", 12)).pack(pady=10)
        responses = []
        
        def check_answers():
            for i, (question_label, var, correct_answer, option_buttons) in enumerate(responses):
                selected = var.get()
                if selected == correct_answer:
                    question_label.config(fg="green")
                else:
                    question_label.config(fg="red")
                    for btn in option_buttons:
                        if btn.cget("text") == correct_answer:
                            btn.config(fg="green")
            messagebox.showinfo("Resultados", "Revisión completa. Respuestas correctas en verde, incorrectas en rojo.")
        
        for q_text, options, correct in questions:
            frame = tk.Frame(root)
            frame.pack(pady=5)
            question_label = tk.Label(frame, text=q_text, font=("Arial", 10))
            question_label.pack(anchor="w")
            var = tk.StringVar(value="None")
            option_buttons = []
            for option in options:
                rb = tk.Radiobutton(frame, text=option, variable=var, value=option)
                rb.pack(anchor="w")
                option_buttons.append(rb)
            responses.append((question_label, var, correct, option_buttons))
        
        tk.Button(root, text="Verificar respuestas", command=check_answers, font=("Arial", 12), 
                    bg="#3498DB", fg="white", bd=0, padx=10, pady=5, width=20, 
                    highlightthickness=2, highlightbackground="white").pack(pady=10)
        tk.Button(root, text="Volver", command=confirm_exit, font=("Arial", 12), 
                    bg="#3498DB", fg="white", bd=0, padx=10, pady=5, width=20, 
                    highlightthickness=2, highlightbackground="white").pack(pady=10)
        
        
    tk.Label(root, text="Selecciona la dificultad", font=("Arial", 14)).pack(pady=10)
    
    tk.Button(root, text="Fácil",  command=lambda: start_reading("facil"), font=("Arial", 12), 
                    bg="#3498DB", fg="white", bd=0, padx=10, pady=5, width=20, 
                    highlightthickness=2, highlightbackground="white").pack(pady=5)
    tk.Button(root, text="Medio", command=lambda: start_reading("medio"), font=("Arial", 12), 
                    bg="#3498DB", fg="white", bd=0, padx=10, pady=5, width=20, 
                    highlightthickness=2, highlightbackground="white").pack(pady=5)
    tk.Button(root, text="Difícil", command=lambda: start_reading("dificil"), font=("Arial", 12), 
                    bg="#3498DB", fg="white", bd=0, padx=10, pady=5, width=20, 
                    highlightthickness=2, highlightbackground="white").pack(pady=5)
    
    
    
    def confirm_exit():
        if messagebox.askyesno("Confirmar", "¿Seguro que quieres salir al menú principal?"):
            main_window()
    
    
    tk.Button(root, text="Volver", command=confirm_exit, font=("Arial", 12), 
        bg="#3498DB", fg="white", bd=0, padx=10, pady=5, width=20, 
        highlightthickness=2, highlightbackground="white").pack(pady=20)


def listening():
    clear_window()
    tk.Label(root, text="Selecciona un nivel de dificultad", font=("Arial", 14)).pack(pady=10)


    
    tk.Button(root, text="Fácil", command=lambda: start_listening("facil"), font=("Arial", 12), 
          bg="#3498DB", fg="white", bd=0, padx=10, pady=5, width=20, 
          highlightthickness=2, highlightbackground="white").pack(pady=5)
    tk.Button(root, text="Medio", command=lambda: start_listening("medio"), font=("Arial", 12), 
          bg="#3498DB", fg="white", bd=0, padx=10, pady=5, width=20, 
          highlightthickness=2, highlightbackground="white").pack(pady=5)
    tk.Button(root, text="Dificil", command=lambda: start_listening("dificil"), font=("Arial", 12), 
          bg="#3498DB", fg="white", bd=0, padx=10, pady=5, width=20, 
          highlightthickness=2, highlightbackground="white").pack(pady=5)
    tk.Button(root, text="Volver", command=main_window, font=("Arial", 12), 
          bg="#3498DB", fg="white", bd=0, padx=10, pady=5, width=20, 
          highlightthickness=2, highlightbackground="white").pack(pady=20)

# Función para iniciar el juego de escucha
def start_listening(level):
    global current_level, score, attempts
    current_level = level
    score = 0
    attempts = 0
    play_round()

# Función para reproducir un audio y mostrar la interfaz de respuesta
def play_round():
    clear_window()
    level_folder = LEVELS[current_level]
    audio_path = os.path.join(AUDIO_FOLDER, level_folder)

    if not os.path.exists(audio_path):
        messagebox.showerror("Error", "Carpeta de audios no encontrada")
        listening()
        return
    
    audio_files = os.listdir(audio_path)
    if not audio_files:
        messagebox.showerror("Error", "No hay audios disponibles")
        listening()
        return

    global current_audio, current_word
    current_audio = random.choice(audio_files)
    current_word = current_audio.split("_")[0]  # Extraer palabra del nombre del archivo

    pygame.mixer.music.load(os.path.join(audio_path, current_audio))
    pygame.mixer.music.play()

    tk.Label(root, text="Escucha y escribe la palabra:").pack(pady=10)
    entry = tk.Entry(root)
    entry.pack(pady=5)
    
    tk.Button(root, text="Comprobar",  command=lambda: check_answer(entry), font=("Arial", 12), 
          bg="#3498DB", fg="white", bd=0, padx=10, pady=5, width=20, 
          highlightthickness=2, highlightbackground="white").pack(pady=10)
    tk.Button(root, text="Reproducir de nuevo", command=play_audio, font=("Arial", 12), 
          bg="#3498DB", fg="white", bd=0, padx=10, pady=5, width=20, 
          highlightthickness=2, highlightbackground="white").pack(pady=5)
    tk.Button(root, text="Volver", command=confirm_exit, font=("Arial", 12), 
          bg="#3498DB", fg="white", bd=0, padx=10, pady=5, width=20, 
          highlightthickness=2, highlightbackground="white").pack(pady=20)

# Función para volver a reproducir el audio
def play_audio():
    level_folder = LEVELS[current_level]  # Obtener la carpeta del nivel actual
    audio_path = os.path.join(AUDIO_FOLDER, level_folder, current_audio)  # Construir ruta completa
    
    if os.path.exists(audio_path):  # Verificar si el archivo existe
        pygame.mixer.music.load(audio_path)
        pygame.mixer.music.play()
    else:
        messagebox.showerror("Error", f"No se encontró el archivo de audio: {audio_path}")


# Función para verificar la respuesta
def check_answer(entry):
    global score, attempts
    user_input = entry.get().strip().lower()
    
    if user_input == current_word:
        score += 5
        result_text = "¡Correcto!"
        color = "green"
    else:
        penalty = 1 if current_level == "medio" else 3 if current_level == "dificil" else 0
        score -= penalty
        result_text = f"Incorrecto. La palabra era '{current_word}'"
        color = "red"

    attempts += 1
    clear_window()
    tk.Label(root, text=result_text, fg=color, font=("Arial", 12)).pack(pady=10)
    root.after(2000, next_round)

# Función para manejar las rondas
def next_round():
    if attempts < 5:
        play_round()
    else:
        show_results()

# Función para mostrar los resultados finales
def show_results():
    clear_window()
    tk.Label(root, text=f"Puntuación final: {score}", font=("Arial", 14)).pack(pady=10)
    
    tk.Button(root, text="Jugar de nuevo", command=start_listening, font=("Arial", 12), 
          bg="#3498DB", fg="white", bd=0, padx=10, pady=5, width=20, 
          highlightthickness=2, highlightbackground="white").pack(pady=10)
    tk.Button(root, text="Volver al menu", command=listening, font=("Arial", 12), 
          bg="#3498DB", fg="white", bd=0, padx=10, pady=5, width=20, 
          highlightthickness=2, highlightbackground="white").pack(pady=20)

# Función para confirmar salida al menú principal
def confirm_exit():
    if messagebox.askyesno("Confirmar", "¿Seguro que quieres salir? Se perderá el progreso."):
        listening() 


# Inicializar la aplicación
root = tk.Tk()
create_centered_window(root, "Traitor Translator", 400, 500)
verify_user_login()
root.mainloop()







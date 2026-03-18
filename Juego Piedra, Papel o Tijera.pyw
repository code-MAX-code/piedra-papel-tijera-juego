# uso tkinder que es la libreria estandar de python
import tkinter as tk
from tkinter import messagebox
# uso random para escoger una respuesta aleatoria
import random

# variables globales para el marcador 
# definimos las variables fuera de las funciones para que su valor 
# persista durante toda la sesion
puntos_usuario = 0 
puntos_rival = 0

def jugar(eleccion_usuario):
    global puntos_usuario, puntos_rival
    
    opciones = ["Piedra", "Papel", "Tijera"]
    # la computadora elige un elemento aleatorio de la lista anterior
    eleccion_rival = random.choice(opciones)
    
    # verificamos el empate es la condicion mas simple
    if eleccion_usuario == eleccion_rival:
        resultado = f"Empate Ambos eligieron {eleccion_rival}."
        
    # aqui evaluamos todas las formas en las que el usuario puede ganar.
    # el operador '\' permite continuar la linea de codigo abajo para que sea legible
    elif (eleccion_usuario == "Piedra" and eleccion_rival == "Tijera") or \
         (eleccion_usuario == "Papel" and eleccion_rival == "Piedra") or \
         (eleccion_usuario == "Tijera" and eleccion_rival == "Papel"):
        puntos_usuario += 1
        resultado = f"¡Ganaste! \nRival eligió: {eleccion_rival}"
    else:
        puntos_rival += 1
        resultado = f"Perdiste... \nRival eligió: {eleccion_rival}"
    
    # utilizo .config() permite cambiar el texto de un Label
    # sin tener que destruir y recrear el elemento grafico
    label_marcador.config(text=f"Tú: {puntos_usuario}  |  Rival: {puntos_rival}")
    
    # mostramos una ventana emergente con el resultado de la ronda
    messagebox.showinfo("Resultado", resultado)

# funcion para reiniciar el marcador
def reiniciar_juego():
    global puntos_usuario, puntos_rival
    puntos_usuario = 0
    puntos_rival = 0
    label_marcador.config(text="Tú: 0  |  Rival: 0")
    messagebox.showinfo("Reinicio", "El marcador ha vuelto a cero.")

# ventana principal
ventana = tk.Tk()
ventana.title("El clásico juego piedra, papel o tijera")
ventana.geometry("400x400")
ventana.configure(bg="#2c3e50")

# interfaz
label_marcador = tk.Label(ventana, text="Tú: 0  |  Rival: 0", 
                          font=("Helvetica", 18, "bold"), 
                          bg="#2c3e50", fg="#ecf0f1")
label_marcador.pack(pady=30)

frame_botones = tk.Frame(ventana, bg="#2c3e50")
frame_botones.pack(pady=10)


# botones de juego
# command=lambda: es importante. Sin el lambda, la función jugar() se 
# ejecutaria sola al abrir el programa. Lambda congela la funcion hasta el clic.
tk.Button(frame_botones, text="PIEDRA", width=12, height=2, bg="#e74c3c", fg="white", 
          font=("Arial", 9, "bold"), command=lambda: jugar("Piedra")).grid(row=0, column=0, padx=5)

tk.Button(frame_botones, text="PAPEL", width=12, height=2, bg="#f1c40f", fg="black", 
          font=("Arial", 9, "bold"), command=lambda: jugar("Papel")).grid(row=0, column=1, padx=5)

tk.Button(frame_botones, text="TIJERA", width=12, height=2, bg="#3498db", fg="white", 
          font=("Arial", 9, "bold"), command=lambda: jugar("Tijera")).grid(row=0, column=2, padx=5)

# boton para reiniciar
btn_reiniciar = tk.Button(ventana, text="REINICIAR MARCADOR", width=20, 
                          bg="#95a5a6", fg="white", font=("Arial", 10, "bold"),
                          command=reiniciar_juego)
btn_reiniciar.pack(pady=40)

# el mainloop es un bucle infinito que espera que se haga clic.
ventana.mainloop()
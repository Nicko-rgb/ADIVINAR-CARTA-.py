import tkinter as tk
import random

# Variables globales
intentos = 0
carta_ganador = None
juego_terminado = False

# Función para voltear la carta al hacer clic
def voltear_carta(event):
    global intentos, carta_ganador, juego_terminado
    if not juego_terminado:
        carta_seleccionada = event.widget
        if carta_seleccionada["text"] == "":
            if intentos < 2:
                if carta_seleccionada == carta_ganador:
                    carta_seleccionada["text"] = "GANASTE"
                    carta_seleccionada["bg"] = "green"
                    label2["text"] = "¡GANASTE EL JUEGO!"
                    label2["fg"] = "green"
                    print("¡GANASTE EL JUEGO!")
                    juego_terminado = True
                else:
                    carta_seleccionada["text"] = "No es el objeto"
                    carta_seleccionada["bg"] = "red"
                    intentos += 1
                    labelIn["text"] = f"Intentos restantes: {2 - intentos}"
            else:
                juego_terminado = True
                label2["text"] = "¡PERDISTE EL JUEGO!"
                label2["fg"] = "red"
                print("¡Juego terminado! Has agotado tus intentos.")
        else:
            carta_seleccionada["text"] = ""

# Función para reiniciar el juego
def reiniciar_juego():
    global intentos, carta_ganador, juego_terminado
    intentos = 0
    juego_terminado = False
    labelIn["text"] = "Intentos restantes: 2"
    label2["text"] = ""
    label2["fg"] = "black"
    for carta in cartas:
        carta["text"] = ""
        carta["bg"] = "white"
    carta_ganador = random.choice(cartas)

# Crear la ventana
ventana = tk.Tk()
ventana.title("Juego de adivinar carta")
ventana.geometry("700x550")
ventana.resizable(False, False)

# Crear etiquetas y panel
label0 = tk.Label(ventana, text="ADIVINA LA CARTA GANADORA", font=("Arial", 12, "underline"))
label0.place(relx=0.5, rely=0.1, anchor="center")

labelRegla = tk.Label(ventana, text="REGLAS: Encuentra la carta con el objeto ganador. ¡Tienes 2 intentos!")
labelRegla.place(relx=0.5, rely=0.18, anchor="center")

label1 = tk.Label(ventana, text="Haz clic en una carta para descubrir el objeto ganador", font=("Arial", 10))
label1.place(relx=0.5, rely=0.26, anchor="center")

panel = tk.Frame(ventana, background="grey", width=600, height=350, bd=1, relief="solid")
panel.place(relx=0.5, rely=0.5, anchor="center")

# Etiqueta de Intento
labelIn = tk.Label(ventana, text="Intentos restantes: 2")
labelIn.place(relx=0.3, rely=0.75, anchor="e")

# Etiqueta de mensajes
label2 = tk.Label(ventana, text="")
label2.place(relx=0.5, rely=0.75, anchor="center")

# Botón para reiniciar el juego
boton_reiniciar = tk.Button(ventana, text="Reiniciar Juego", command=reiniciar_juego)
boton_reiniciar.place(relx=0.5, rely=0.9, anchor="center")

# Crear cartas sin texto inicial
cartas = []
for i in range(6):
    carta = tk.Label(panel, text="", width=13, height=13, bd=1, relief="solid")
    carta.grid(row=0, column=i, padx=8, pady=10)
    carta.bind("<Button-1>", voltear_carta)
    cartas.append(carta)

# Asignar un objeto aleatorio a una carta
carta_ganador = random.choice(cartas)

ventana.mainloop()
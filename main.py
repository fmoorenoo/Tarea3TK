import tkinter as tk
from tkinter import ttk
from tkinter.font import Font
from PIL import Image, ImageTk
import os
import random

aciertos = 0
indice = 0
imagenes_notas = ["suspenso.png", "suficiente.png", "bien.png", "notable.png", "sobresaliente.png"]

def texto_ingresado():
    global aciertos, indice, imagenes_notas, fuente

    # Almacena lo que ingresa el usuario, lo convierte en minúsculas y elimina los espacios al principio y al final
    texto = entrada.get().lower().strip()
    correcta = nueva_lista[indice]
    if texto == correcta:
        aciertos += 1
        print("¡Correcto!")
        info.config(text=f"Aciertos: {aciertos}")  # Actualiza el texto de aciertos

    indice += 1
    if indice < len(diez_imagenes):
        actualizar_imagen()
    else:
        ventana_final()


def actualizar_imagen():
    global photo, label_img
    nueva_imagen = Image.open("imagenes_hiragana/" + diez_imagenes[indice]).resize((200, 200))
    photo = ImageTk.PhotoImage(nueva_imagen)
    label_img.config(image=photo)

    # Ver respuesta correcta por terminal
    print(f"La respuesta correcta es: {nueva_lista[indice]}")

def ventana_final():
    fallos = 10 - aciertos
    root.destroy()
    v2 = tk.Tk()
    v2.title("Resultados del examen")
    v2.configure(background='#7a7a7a')
    v2.geometry('450x450')

    res = ttk.Label(v2, text=f"Examen terminado. Has tenido {fallos} fallos", padding=10, font=fuente)
    res.pack()

    nota = ""
    i = 0
    if aciertos == 5:
        nota = "Suficiente.\nPor los pelos."
        i = 1
    elif aciertos == 6:
        nota = "Bien.\nNo está mal."
        i = 2
    elif aciertos in [7, 8]:
        nota = "Notable.\nOkayyy."
        i = 3
    elif aciertos in [9, 10]:
        nota = "Sobresaliente.\nGod."
        i = 4
    else:
        nota = "Has suspendido.\nEres un desastre."
        i = 0

    resultado = ttk.Label(v2, text=f"Tienes un {aciertos}. {nota}", padding=10, font=fuente)
    resultado.pack()

    nueva_imagen = Image.open("imagenes_nota/" + imagenes_notas[i]).resize((300, 300))
    photo = ImageTk.PhotoImage(nueva_imagen)

    label_img_v2 = tk.Label(v2, image=photo)
    label_img_v2.image = photo
    label_img_v2.pack(pady=20)

# Pantalla principal
root = tk.Tk()
root.title("Examen")
color_purple = '#eecbff'
root.configure(background=color_purple)
root.geometry('330x450')
fuente = Font(family="Futuristic", size=15)

# Imagenes guardadas en una lista y 10 de ellas escogidas al azar
lista_imagenes = os.listdir('imagenes_hiragana')
diez_imagenes = random.sample(lista_imagenes, 10)

# Lista sin el tipo de archivo al final
nueva_lista = []
for x in diez_imagenes:
    if x.endswith('.png') or x.endswith('.jpg'):
        nueva_lista.append(x[:-4])

# Primera imagen
image = Image.open("imagenes_hiragana/" + diez_imagenes[indice]).resize((200, 200))
photo = ImageTk.PhotoImage(image)
label_img = tk.Label(root, image=photo, bg=color_purple)
label_img.pack(pady=20)

# Título y campo de entrada para la respuesta
label_texto = ttk.Label(root, text="Introduce tu respuesta:", background=color_purple, padding=10, font=fuente)
label_texto.pack()

entrada = ttk.Entry(root, width=25, font=fuente)
entrada.pack(pady=10)

# Botón para confirmar la respuesta
boton_confirmar = ttk.Button(root, text="Confirmar", command=texto_ingresado)
boton_confirmar.pack(pady=10)

info = ttk.Label(root, text=f"Aciertos: {aciertos}", background=color_purple, padding=10, font=fuente)
info.pack()

# Ver respuesta correcta por terminal
print(f"La respuesta correcta es: {nueva_lista[indice]}")

root.mainloop()

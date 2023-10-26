# Prototipo buscador de imagenes
# Aksel Villela
# 2023

import tkinter as tk

# Lista de palabras de ejemplo
lista_palabras = ["chango", "chango riendo", "chango con paleta", "chango al chile que bueno",
                  "chango cierra el hocico papi"
    , "chango mamado", "Gato saludando", "gato explotando", "gato orejas", "joder claro que si",
                  "chango riendo con lentes", "chango riendo sin lentes"]


# Funciones
def buscar_palabra():
    entrada = entrada_texto.get().lower()
    resultado.delete(0, tk.END)

    # Busca coincidencias en la lista de palabras
    for palabra in lista_palabras:
        if entrada in palabra.lower():
            resultado.insert(tk.END, palabra)


# Crear la ventana principal
ventana = tk.Tk()
ventana.title("My fesAPPragon")
ventana.geometry("1280x720")
ventana.configure(bg="white")

# Barra de búsqueda y botones
barra_superior = tk.Frame(ventana, width=1280, height=80, bg="black")  # "#D7D7D7"
barra_superior.pack(side=tk.TOP, fill=tk.X)

entrada_texto = tk.Entry(barra_superior)
entrada_texto.pack(side=tk.LEFT, padx=10)

boton_buscar = tk.Button(barra_superior, text="Buscar", bg="white", fg="black", command=buscar_palabra)
boton_eliminar = tk.Button(barra_superior, text="Eliminar", bg="white", fg="black")
boton_favorito = tk.Button(barra_superior, text="Favorito", bg="white", fg="black")

boton_buscar.pack(side=tk.LEFT, padx=10, pady=10)
boton_eliminar.pack(side=tk.RIGHT, padx=10, pady=10)
boton_favorito.pack(padx=10, pady=10)

# Área azul
area_azul = tk.Frame(ventana, bg="#AFA9FF", width=1000, height=720)
area_azul.pack(side=tk.LEFT, fill=tk.X)

# Rectangulos
area_rectangulos = tk.Frame(area_azul, bg="black", width=1000, height=720)
area_rectangulos.pack(side=tk.LEFT, fill=tk.X, padx=300,pady=185)
for i in range(9):
    rectangulo = tk.Label(area_rectangulos, text=f"Imagen {i + 1}", bg="white", width=20, height=5)
    rectangulo.grid(row=i // 3, column=i % 3, padx=10, pady=10)

# Área blanca y etiquetas de texto
area_blanca = tk.Frame(ventana, bg="white", width=1280, height=720)
rectangulo = tk.Label(area_azul, text=f"Imagen", bg="white", width=20, height=5)

# ListBox de resultados
resultado = tk.Listbox(area_blanca)
resultado.pack()
area_blanca.pack(side=tk.RIGHT, fill=tk.X)

etiqueta_agregado = tk.Label(area_blanca, text="Agregado", font=("Arial", 20))
etiqueta_historial = tk.Label(area_blanca, text="Historial", font=("Arial", 20))
etiqueta_favoritos = tk.Label(area_blanca, text="Favoritos", font=("Arial", 20))

etiqueta_agregado.pack(side=tk.TOP, pady=50, )
etiqueta_historial.pack(side=tk.TOP, pady=50)
etiqueta_favoritos.pack(side=tk.TOP, pady=50)

# Iniciar la aplicación
ventana.mainloop()

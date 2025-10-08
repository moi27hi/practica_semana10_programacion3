from PIL import Image
imagen = Image.open("Imagenes/descarga.png")
#imagen.show()
#imagen.save("imagenes/logo1.webp")

print(f"Extension de la imagen: {imagen.png}")
print(f"La imagen tiene este tamaño: {imagen.size}")
print(f"Colores: {imagen.mode}")

#cambiada = imagen.thumbnail((200,100))
imagen.thumbnail((200,100))
imagen.show()
#cambiada.show()
from PIL import Image,ImageFilter

Imagen = Image.open("Imagenes/paisajehermoso.webp")
Imagen.show()


#Rotaciones
rotacion = Imagen.rotate(90)
rotacion.show()
rotacion2 = Imagen.rotate(180)
rotacion2.show()
rotacion3 = Imagen.rotate(270)
rotacion3.show()

Imagen.transpose(Image.FLIP_LEFT_RIGHT).show()
Imagen.transpose(Image.FLIP_TOP_BOTTOM).show()


#Filtros

img_contor = Imagen.filter(ImageFilter.CONTOUR).show()
img_detail = Imagen.filter(ImageFilter.DETAIL).show()
#img_edge = imagen.filter(ImageFilter.EDGE_ENHANCE).show()
#img_edgem = imagen.filter(ImageFilter.EDGE_ENHANCE_MORE).show()
#img_emboss = imagen.filter(ImageFilter.EMBOSS).show()
#img_findedg = imagen.filter(ImageFilter.FIND_EDGES).show()
#img_smooth = imagen.filter(ImageFilter.SMOOTH).show()
#img_smoothm = imagen.filter(ImageFilter.SMOOTH_MORE).show()

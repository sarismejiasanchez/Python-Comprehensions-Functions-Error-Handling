# Escribir en un archivo
# https://www.w3schools.com/python/python_file_write.asp
# https://platzi.com/blog/administracion-usuarios-servidores-linux/
# https://platzi.com/blog/cosas-que-nos-sabias-sobre-el-sistema-de-permisos-de-linux-realmente-es-octal/

'''
r+ da permisos tanto de lectura como de escritura, respetando el contenido original del archivo, es decir agregando nuevas lineas.
w+ da permisos tanto de lectura como de escritura, sin embargo este sobreescribe el contenido del archivo.
''' 

with open("./text.txt", "w+") as file:
  print(file.read())
  file.write("Nuevas cosas en este archivo\n")
  file.write("Otra linea\n")
  file.write("Una mas\n")
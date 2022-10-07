import PySimpleGUI as Ps
from rembg import remove
from PIL import Image


input_path = input("Coloque o caminho para o arquivo aqui: ")
output_path = input("Onde deve ser salvo")
input = Image.open(input_path)
output = remove(input)
output.save(output_path)
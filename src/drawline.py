# Plugin de desenhar uma linha
# Autor: Artur O. R. Franco
# 11/10/2017

# importar biblioteca
from gimpfu import *

# metodo da logica do plugin
def drawline():
	# gimp # variavel GIMP, tem acesso a imagem e as camadas
	# pdb # ele tem acesso as ferramentos e aos filtros
	img = gimp.image_list();
	img = img[0];
	
	width = img.layers[0].width;
	height = img.layers[0].height;
	
	# pdb.gimp_paintbrush_default(camada, numero de valores, [x0,y0,x1,y1])
	pdb.gimp_paintbrush_default(img.layers[0], 4, [0,0,width,height])

# funcao que personaliza a interface (GUI, Graphical User Interface)
register(
	"desenha_linha_veia",
	"drawline",
	"Desenha uma linha de uma ponta a outra",
	"Eu mesmo",
	"Irene",
	"2017 em diante",
	"Desenha Linha",
	"",
	[],
	[],
	drawline,
	menu="<Image>/Aula"
)

# funcao principal, NAO MEXA NELA!!!
main()
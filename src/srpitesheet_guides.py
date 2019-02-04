# Author: Artur "Tushin" de Oliveira da Rocha Franco
# C:\Program Files\GIMP 2\lib\gimp\2.0\plug-ins\spritesheet_guides.py
from gimpfu import *
import random

def spritesheet_guides(option):
	img = gimp.image_list()[0]
	height = img.height
	width = img.width
	
	if(option == "12x8"):
		h = height/8
		w = width/12
		for i in range(1,12):
			guide = pdb.gimp_image_add_vguide(img, w*i)
		for i in range(1,8):
			guide = pdb.gimp_image_add_hguide(img, h*i)
	else:
		h = height/4
		w = width/3
		for i in range(1,3):
			guide = pdb.gimp_image_add_vguide(img, w*i)
		for i in range(1,4):
			guide = pdb.gimp_image_add_hguide(img, h*i)


register(
    "spritesheet_guides",
    "spritesheet_guides",
    "Adiciona guidelines",
    "Artur O. R. Franco",
    "Artur O. R. Franco",
    "2019",
    "Add guidelines for RPG MakerMV Spritesheet (Py)...",
    "",      # Create a new image, don't work on an existing one
    [
	(PF_RADIO, "option", "Choose application: ", "12x8", (("12x8","12x8"),("3x4","3x4")))
	],
    [],
    spritesheet_guides,
	menu="<Image>/Aula"
)

main()
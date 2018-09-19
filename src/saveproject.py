#!/usr/bin/env python

# Save a directory with all XCF was opened
# Author: Artur O. R. Franco
# 11/10/2017

# importar biblioteca
from gimpfu import *
import os
# metodo da logica do plugin
#~ def save_project(dirname, path):

def saveproject(dirname, path):
    imgs = gimp.image_list();
    num = 0;

    for img in imgs:
        for layer in img.layers:
            fullpath = os.path.join(path, dirname+str(num)+'.xcf');
            pdb.gimp_xcf_save(0, img, layer, fullpath, fullpath);
            num += 1;

# funcao que personaliza a interface (GUI, Graphical User Interface)
register(
    "save_project",
    "saveproject",
    "Save a directory with all xcf is opened",
    "Artur O. R. Franco",
    "Artur O. R. Franco",
    "2018",
    "Save project",
    "RGB*, GRAY*",
    [
        #~ (PF_STRING, "dirname", "Directory name", _("Untitled project")),
        (PF_STRING, "dirname", "Project name", "Untitled project"),
        #~ (PF_DIRNAME, "dirname", _("_Project name"), os.getcwd()),
        (PF_DIRNAME, "path", "Path name", os.getcwd())    ],
    [],
    saveproject,
    menu="<Image>/Save Project"
)

main()

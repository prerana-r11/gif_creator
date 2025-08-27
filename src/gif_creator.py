import imageio.v3 as io
import os

def create(files,res="output.gif",duration=500,loop=0,fps=None):
    images=[]
    for i in files:
        images.append(io.imread(i))
    
    a=[".jpg",".png",".jpeg",".bmp"]

    for i in files:
        if not i.lower.endswith() (a):
            raise ValueError(f"unsupportes file format")
         
    io.imwrite("output.gif",images,duration=500,loop=0)
    print(f"GIF saved at: {os.path.abspath(res)}")

    

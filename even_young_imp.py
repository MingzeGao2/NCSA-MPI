import gdal
import numpy as np
from gdalconst import *
import matplotlib.pyplot as plt
import matplotlib as ml
import matplotlib.cm as cm


dataset = gdal.Open("output.tif", GA_ReadOnly)
band = dataset.GetRasterBand(1)
geotransform = dataset.GetGeoTransform()
originX = geotransform[0]
originY = geotransform[3]
pixelWidth = geotransform[1]
pixelHeight = geotransform[5]

cols = dataset.RasterXSize
rows = dataset.RasterYSize
p = pixelWidth
data = band.ReadAsArray(0,0, cols, rows)

def isOutOfBound(x,y):
    if x !=0 and x != rows - 1 and y != 0 and y != cols - 1:
        return False
    else:
        return True
    
def getG(x,y):
    if(isOutOfBound(x,y)):
        return None
    else:
        z3 = data[x+1, y-1]
        z6 = data[x+1, y]
        z9 = data[x+1, y+1]
        z1 = data[x-1, y-1]
        z4 = data[x-1, y]
        z7 = data[x-1, y+1]
        return (z3 + z6 + z9 - z1 - z4 - z7)/(6*p)
    
def getH(x,y):
    if (isOutOfBound(x,y)):
        return None
    else:
        z3 = data[x+1, y-1]
        z6 = data[x+1, y]
        z9 = data[x+1, y+1]
        z1 = data[x-1, y-1]
        z4 = data[x-1, y]
        z7 = data[x-1, y+1]
        z2 = data[x, y-1]
        z8 = data[x, y+1]
        return(z1 + z2 + z3 - z7 - z8 -z9)/(6*p)
def getD(x,y):
    if(isOutOfBound(x,y)):
        return None
    else:
        z3 = data[x+1, y-1]
        z6 = data[x+1, y]
        z9 = data[x+1, y+1]
        z1 = data[x-1, y-1]
        z4 = data[x-1, y]
        z7 = data[x-1, y+1]
        z2 = data[x, y-1]
        z5 = data[x,y]
        z8 = data[x, y+1]
        return (z1 + z3 + z4 - z6 - z7 - z9 - 2*(z2 + z5 + z8))/float(3*p**2)

def getE(x,y):
    if(isOutOfBound(x,y)):
        return None
    else:
        z3 = data[x+1, y-1]
        z6 = data[x+1, y]
        z9 = data[x+1, y+1]
        z1 = data[x-1, y-1]
        z4 = data[x-1, y]
        z7 = data[x-1, y+1]
        z2 = data[x, y-1]
        z5 = data[x,y]
        z8 = data[x, y+1]
        return (z1 + z3 + z4 - z6 - z7 - z9 -2 * (z4 + z5 + z6))/float(3*p**2)
def getF(x,y):
    if (isOutOfBound(x,y)):
        return None
    else:
        z3 = data[x+1, y-1]
        z6 = data[x+1, y]
        z9 = data[x+1, y+1]
        z1 = data[x-1, y-1]
        z4 = data[x-1, y]
        z7 = data[x-1, y+1]
        z2 = data[x, y-1]
        z5 = data[x,y]
        z8 = data[x, y+1]
        return (z3 + z7 -z1 -z9)/(4*p**2)

def plot(data):
    fig = plt.figure()
    plt.imshow(data)
    plt.colorbar(orientation='vertical')
    plt.show()


def main():
    G = H = D = E = F = np.zeros((rows, cols))
    for i in range(data.shape[0]):
        for j in range(data.shape[1]):
            D[i,j] = getD(i,j)
    plot(D)

main()

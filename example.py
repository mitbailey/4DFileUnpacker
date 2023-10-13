import numpy as np
import matplotlib.pyplot as plt

from unpack4d import unpacker as u4d
# import unpack4d as u4d

if __name__ == '__main__':
    surfaces, metadata = u4d.unpack('example.4d')

    FIG_W = 9
    FIG_H = 9
    figscale = 0.75

    fig, ax = plt.subplots(1, 1, figsize=(FIG_W*figscale, FIG_H*figscale))
    im = ax.imshow(surfaces['SurfaceInNanometers'], cmap=plt.get_cmap('turbo'), interpolation='none')
    plt.colorbar(im,ax=ax,fraction=0.046, pad=0.04, orientation='vertical')

    fig.suptitle('Surface')

    plt.show()
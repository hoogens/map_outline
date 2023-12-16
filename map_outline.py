"""
Script to create an outline of a land 'The Netherlands' and river 'Rhine'
@author: Sarah H
"""
import geopandas as gpd
import matplotlib.pyplot as plt
import numpy
import os

def load_netherlands_map():
    """
    Function to load the map of the Netherlands
    """
    netherlands = gpd.read_file('gadm36_NLD.gpkg') #'provinces.geojson'
    return netherlands

def load_rhine_map():
    """"
    Function to load the river Rhine
    """
    rivers_path = gpd.datasets.get_path("naturalearth_lowres")
    rivers = gpd.read_file(rivers_path)
    rhine = rivers[(rivers['name'] == 'Rhein') & (rivers['iso_a3'] == 'NLD')]
    return rhine

def align_land_and_river():
    """
    Function to align landmap and river
    """
    netherlands = load_netherlands_map()
    rhine = load_rhine_map()

    ax = netherlands.plot(color='lightgray', edgecolor='black')

    # rhine.plot(ax=ax, color='blue', linewidth=2)

    ax.set_aspect('equal')

    plt.savefig('map_and_river_align.png')

    plt.show()

if __name__ == '__main__':
    align_land_and_river()

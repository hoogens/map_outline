"""
Script to create an outline of a land 'The Netherlands' and river 'Rhine'
@author: Sarah H
"""
import geopandas as gpd
import matplotlib as plt

def load_netherlands_map():
    """
    Function to load the map of the Netherlands
    """
    world = gpd.read_file(gpd.datasets.get_path('naturalearth_lowres'))
    nl = world[world['name'] == 'Netherlands']
    return nl

def load_rhine_map():
    """"
    Function to load the river Rhine
    """
    rivers = gpd.read_file(gpd.datasets.get_path("naturalearth_lowres"))
    rhine = rivers[rivers['name'] == 'Rhein']
    return rhine




# if __name__ == '__main__':

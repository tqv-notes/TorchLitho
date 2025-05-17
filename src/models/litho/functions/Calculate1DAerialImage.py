# dummy file for testing purpose 

import torch
import sys, os

dir_path = os.path.dirname(__file__)
sys.path.append(dir_path+"/../..")

from CalculateCharacteristicMatrix import CalculateCharacteristicMatrix
from litho.Numerics import Numerics
from litho.Source import Source
from litho.Receipe import Receipe
from litho.Mask import Mask
from litho.ProjectionObjective import ProjectionObjective
from litho.ImageData import ImageData

def Calculate1DAerialImage(source, mask, projector, lithoImage, receipe, numerics):
    lithoImage.ImageType = '1d'
    lithoImage.SimulatinType = 'aerial'
    lithoImage.Intensity = []
    lithoImage.ImageX = []
    lithoImage.ImageY = []
    lithoImage.ImageZ = []

    return lithoImage

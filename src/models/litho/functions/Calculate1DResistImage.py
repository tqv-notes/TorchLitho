# dummy file for testing purpose

import torch
import sys, os

dir_path = os.path.dirname(__file__)
sys.path.append(dir_path+"/../..")

from CalculateTransferMatrix import CalculateTransferMatrix
from litho.Numerics import Numerics
from litho.Source import Source
from litho.Receipe import Receipe
from litho.Mask import Mask
from litho.ProjectionObjective import ProjectionObjective
from litho.ImageData import ImageData
from litho.FilmStack import FilmStack

def Calculate1DResistImage(source, mask, projector, filmStack, resistLithoImage, receipe, numerics):
  
    resistLithoImage.ImageType = '1d'
    resistLithoImage.SimulationType = 'resist'
    resistLithoImage.Intensity = []
    resistLithoImage.ImageX = []
    resistLithoImage.ImageY = []
    resistLithoImage.ImageZ = []
    
    return resistLithoImage


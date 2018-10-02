import random as random
from scipy.spatial import distance
import numpy as numpy
import matplotlib.pyplot as plt

class gas:
  
  def __init__(self,position,nodeID,dist,error,neighbors):
    self.position=position
    self.nodeId=nodeID
    self.dist=dist
    self.error=error
    self.neighbors=neighbors
  
  getPosition(self):
    reuturn(self.Position)
  getNodeID(self):
    reuturn(self.nodeID)
  getError(self):
    reuturn(self.error)
  getNeighbors(self):
    reuturn(self.neighbors)
  
  setPosition(self,position):
    self.position=position
  setNodeID(self,nodeID):
    self.nodeID=nodeID
  setError(self,error):
    self.error=error
  setNeighbors(self,neighbor):
    self.neighbor=neighbor

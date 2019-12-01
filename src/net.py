import math
import numpy as np

import layer
from distance import euclidean

class Net:
    def __init__(self, lr, radius, inputSize, width, height):
        self.learningRate = lr
        self.radius = radius
        self.decayConstant = 1 #??
        self.t = 1
        self.map = layer.SquareMap(inputSize, width, height)


    def decay(self):
        self.radius = self.radius * math.exp(-self.t / self.decayConstant)
        self.learningRate = self.learningRate * math.exp(-self.t / self.decayConstant)

    def findBMU(self, sample):
        minDistance = -1
        bmu = (-1, -1)
        for row in self.map.neurons:
            for n in row:
                distance = euclidean(n.value, sample)
                if minDistance == -1 or distance < minDistance:
                    minDistance = dstance
                    bmu = n.pos
        return bmu

    def neighbourhood(self, target, bmu):
        d = euclidean(target.value, bmu.value)
        return math.exp(-(d ** 2) / (2 * (self.radius ** 2)))

    def updateWeight(self, sample, targetPos, bmuPos):
        targetRow, targetCol = targetPos
        bmuRow, bmuCol = bmuPos
        target = self.map.neurons[targetRow][targetCol]
        bmu = self.map.neurons[bmuRow][bmuCol]
        diff = np.subtract(sample, target.value)
        updated = np.add(target.value, np.multiply(diff, self.learningRate * self.neighbourhood(target, bmu)))
        self.map.neurons[targetRow][targetCol].value = updated

import math
import numpy as np

import layer
from distance import euclidean

class Net:
    def __init__(self, lr, radius, inputSize, width, height):
        self.inputSize = inputSize
        self.initialLearningRate = lr
        self.learningRate = lr
        self.initialRadius = radius
        self.radius = radius
        self.timeConstant = 1000
        self.map = layer.SquareMap(inputSize, width, height)


    def decay(self, iteration):
        self.radius = self.initialRadius * math.exp(-iteration / self.timeConstant)
        self.learningRate = self.initialLearningRate * math.exp(-iteration / self.timeConstant)

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

    def getNeighbours(self, pos):
        #TODO: implement

    def neighbourhood(self, targetPos, bmuPos):
        targetX, targetY = targetPos
        bmuX, bmuY = bmuPos
        distance = 0
        if (targetX == bmuX):
            distance = abs(bmuY - targetY)
        elif (targetY == bmuY):
            distance = abs(bmuX - targetX)
        else:
            dx = abs(bmuX - targetX)
            dy = abs(bmuY - targetY)
            if targetY < bmuY:
                distance = dx + dy - int(math.ceil(dx / 2.0))
        else:
            distance = dx + dy - int(math.floor(dx / 2.0))

        return math.exp(-(distance ** 2) / (2 * (self.radius ** 2)))

    def updateWeight(self, sample, targetPos, bmuPos):
        targetRow, targetCol = targetPos
        target = self.map.neurons[targetRow][targetCol]
        diff = np.subtract(sample, target.value)
        updated = np.add(target.value, np.multiply(diff, self.learningRate * self.neighbourhood(targetPos, bmuPos)))
        self.map.neurons[targetRow][targetCol].value = updated

    def train(self):
        for i in range(self.timeConstant):
            sample = np.empty(self.inputSize)
            bmuPos = self.findBMU(sample)
            neighbours = self.getNeighbours(bmuPos)
            for n in neighbours:
                self.updateWeight(sample, n, bmuPos)
            self.decay(i)

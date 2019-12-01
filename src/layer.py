
class SquareMap:
    def __init__(self, inputSize, width, height):
        self.width = width
        self.height = height
        self.neurons = [
            [ Neuron(inputSize, (i, j)) for j in range(width) ]
            for i in range(height)
            ]
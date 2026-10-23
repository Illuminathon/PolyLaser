class DecorationObject(object):
    def draw(self, window, height, width):
        raise NotImplementedError("Subclasses must implement this method.")
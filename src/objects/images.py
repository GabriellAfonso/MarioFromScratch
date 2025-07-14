class ImageObject:
    def __init__(self, surface, x=0, y=0, depth=0):
        self.surface = surface
        self.x = x
        self.y = y
        self.depth = depth
        self.scene_index = 0


class plates :
    def __init__(self,breadth,length,dist_from_screen):
        super().__init__()
        self.breadth = breadth
        self.length = length
        self.dist_from_screen = dist_from_screen 

    def adjust_dimensions(self,breadth_factor,length_factor, dist_from_screen_factor):
        new_breadth = self.breadth + breadth_factor
        new_length = self.length + length_factor
        new_dist_from_screen = self.dist_from_screen + dist_from_screen_factor

        return new_breadth, new_length, new_dist_from_screen


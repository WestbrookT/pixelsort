
class Selector:
    """
    A selector will take a grid of pixels in the form of [[x1y1, x2y1, x3y1, ...], # Row 1
                                                          [x1y2, x2y2, x3y3, ...], # Row 2
                                                          ]
    Once it has this grid it will return a list of Points that are allowed to be changed.
    """

    def __init__(self, selection_algo):
        self.selection_algo = selection_algo

    def select(self, img_data):

        return self.selection_algo(img_data)
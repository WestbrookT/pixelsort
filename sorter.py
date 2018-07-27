
class Sorter:
    '''
    A Sorter will take in a list of pixels irrespective of their location and
    will return another list of pixels in a sorted order determined by the sorter.

    These pixels will be matched with the Points returned by the Placer object.
    '''

    def __init__(self, sort_algo):
        self.sort_algo = sort_algo

    def sort(self, pixels):

        for pix in pixels:
            pix.set_compare(self.sort_algo)

        return sorted(pixels)
        #do the sorting
    
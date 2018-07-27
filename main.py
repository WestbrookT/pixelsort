from pixel import Pixel
from point import Point
import math

import selector, sorter, pixler

def pixel_sorter(first, second):

    return True

    f_total = first.r + first.g + first.b
    s_total = second.r + second.g + second.b

    return f_total < s_total

def location_sorter(first, second):

    if first.y == second.y:
        return first.x < second.x
    else:
        return first.y < second.y

def center_point(first, second):

    dist1 = math.sqrt((512 - first.x)**2 + (440 - first.y)**2)
    dist2 = math.sqrt((512 - second.x)**2 + (440 - second.y)**2)

    return dist1 < dist2

def diag(first, second):

    angle = math.radians(-90)

    if first.x * math.cos(angle) + first.y * math.sin(angle) == second.x * math.cos(angle) + second.y * math.sin(angle):
        return first.x < second.x
    else:
        return first.x * math.cos(angle) + first.y * math.sin(angle) < second.x * math.cos(angle) + second.y * math.sin(angle)

def selection_algo(img_data):

    pixels = []
    locations = []

    for y, row in enumerate(img_data):
        for x, pix in enumerate(row):
            if (pix.r > 150 or  pix.g > 150 or pix.b > 150):
                pixels.append(pix)
                locations.append(Point(x, y))

    return pixels, locations

def select2(img_data):
    pixels = []
    locations = []

    for y, row in enumerate(img_data):
        for x, pix in enumerate(row):
        
            pixels.append(pix)
            locations.append(Point(x, y))

    return pixels, locations


sel = selector.Selector(selection_algo)
sorting = sorter.Sorter(pixel_sorter)
locations_placer = sorter.Sorter(diag)

creator = pixler.Pixler('orchid.jpg')

creator.generate_sorted_image(sel, sorting, locations_placer).show()


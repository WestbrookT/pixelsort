from PIL import Image
from pixel import Pixel

class Pixler:

    def __init__(self, pil_image):
        self.origin = Image.open(pil_image)

    def place_color(self, point, pixel):
        pass

    def get_image_data(self):
        tuples = self.origin.getdata()
        width = self.origin.width

        raw_data = self.origin.getdata()
        
        img_data = []
        for y in range(self.origin.height):

            row = [Pixel(tup=raw_data[tup]) for tup in range(y*width, y*width+width)]
            img_data.append(row)
        return img_data


    def generate_sorted_image(self, selector, sorter, placer):
        
        img_data = self.get_image_data()

        pixels, locations = selector.select(img_data)

        final_locations = placer.sort(locations)
        final_pixels = sorter.sort(pixels)

        out_img = self.origin.copy()

        for point, pix in zip(final_locations, final_pixels):
            # out_img[point.x, point.y] = (pix.r, pix.g, pix.b)
            out_img.putpixel((point.x, point.y), (pix.r, pix.g, pix.b))
        
        return out_img

if __name__ == '__main__':

    a = Pixler('moe.png')
    a.get_image_data()
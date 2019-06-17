from PIL import Image, ImageQt
 
def make_sepia_palette(color):
    palette = []
    r, g, b = color
    for i in range(255):
        palette.extend((int(r*i/255), int(g*i/255), int(b*i/255)))
 
    return palette
 
def create_sepia(input_img):
    whitish = (255, 240, 192)
    sepia = make_sepia_palette(whitish)
 
    color_image = Image.open(input_img)
 
    # convert our image to gray scale
    black_white = color_image.convert('L')
 
    # add the sepia toning
    black_white.putpalette(sepia)
 
    # convert to RGB for easier saving
    sepia_image =black_white.convert('RGB')
    qt_img = ImageQt.ImageQt(sepia_image)
#    sepia_image.save(output_image_path)
#    sepia_image.show()
    return qt_img


if __name__ == '__main__':
    create_sepia('photo.jpg')

from PIL import Image
 
def resize_image(input_image_path,
                 output_image_path):
    original_image = Image.open(input_image_path)
    width, height = original_image.size
    print('The original image size is {wide} wide x {height} '
          'high'.format(wide=width, height=height))
    k = float(input("How many times the image should be resized? "))
    w = k*width
    h = k*height
    width = int(w)
    height = int(h)
    size = (width, height)
    resized_image = original_image.resize(size)
    width, height = resized_image.size
    print('The resized image size is {wide} wide x {height} '
          'high'.format(wide=width, height=height))
    resized_image.show()
    resized_image.save(output_image_path)
 

input_image_path = str(input("Enter a file to be resized: "))
resize_image(input_image_path,
            output_image_path='output.jpg')

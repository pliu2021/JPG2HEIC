from PIL import Image
import pyheif

def convert_jpg_to_heic(input_path, output_path):
    img = Image.open(input_path)
    
    heif_file = pyheif.from_pillow(img)
    
    with open(output_path, "wb") as f:
        f.write(heif_file.data)


input_path = "path_to_your_input_file.jpg" 
output_path = "output_file.heic"  
convert_jpg_to_heic(input_path, output_path)

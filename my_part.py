!pip install bing_image_downloader
!pip install Pillow

from bing_image_downloader import downloader
from PIL import Image
print ("Enter the request: ")
query_string = input()
#query_string = 'cat'
downloader.download(query_string, limit=3,  output_dir='dataset',  # изменить limit для большего числа фоток
adult_filter_off=True, force_replace=False, timeout=60)

im = Image.open(r"dataset/Hogwarts/Image_1.jpg") 
im
# Указываем желаемое разрешение и приводим к нему
size = 128, 128
im.thumbnail(size, Image.ANTIALIAS)
im.save('dataset/Hogwarts/Image_1_scaled.jpg', "JPEG")

from PIL import Image
im = Image.open(r"dataset/Hogwarts/Image_1.jpg") 
im

# Указываем желаемое разрешение и приводим к нему
size = 128, 128
im.thumbnail(size, Image.ANTIALIAS)
im.save('dataset/mipt/Image_1_scaled.jpg', "JPEG")
im = Image.open(r"dataset/mipt/Image_1_scaled.jpg") 
im
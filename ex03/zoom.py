from load_image import display_image_info
from load_image import ft_load

def ft_zoom(img_array) -> int:
    zoomed_img = img_array[100:500, 400:800, :]
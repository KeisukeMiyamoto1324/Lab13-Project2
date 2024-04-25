from PIL import Image
import os

class ImageEditer:
    def open(self, path: str) -> Image:
        """
        Method to open image file
        
        :param path: where the image is
        
        :return: opened image
        
        :raise e: error happenned during processing
        """
        try:
            results = Image.open(path)
            return results
        except Exception as e:
            raise e
    
    def save(self, image: Image, path: str) -> None:
        """
        Method to save image
        
        :param image: image you'd like to save
        :param path: where to save
        """
        image.save(path)
    
    def remove(self, path: str) -> None:
        """
        Method to delete image
        
        :param path: path to the image to be removed
        
        :raise e: error happenned during processing
        """
        try:
            os.remove(path)
        except Exception as e:
            raise e
        
    def resizeByWidth(self, image: Image.Image, width: int) -> Image.Image:
        """
        Method to resize an image to a specified width while preserving the aspect ratio
        
        :param image: image to be resized
        :param width: width after resized
        
        :return: resized images
        """
        original_width, original_height = image.size
        new_width = width
        new_height = int(original_height * (new_width / original_width))
        resized_image = image.resize((new_width, new_height))

        return resized_image
    
    def resizeByHeight(self, image: Image.Image, height: int) ->Image.Image:
        """
        Method to resize an image to a specified height while preserving the aspect ratio
        
        :param image: image to be resized
        :param height: height after resized
        
        :return: resized images
        """
        original_width, original_height = image.size
        new_height = height
        new_width = int(original_width * (new_height / original_height))
        resized_image = image.resize((new_width, new_height))

        return resized_image

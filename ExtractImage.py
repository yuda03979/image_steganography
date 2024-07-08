import cv2
from Functions import check_path_already_exist


class ExtractImage:

    def __init__(self, path:str):
        self.path = path
        check_path_already_exist(self.path)
        self.image = cv2.imread(self.path)
        self.bin_text = self.extract_png()


    def check_path(self):
        # raise exeption
        pass

    def extract_png(self):
        """
        extract the first "length" LSB in the image and return it as a string
        :return: the requierd text without the begining (the length)
        """
        length = self.extract_length() + (4 * 8)
        text = ""
        counter = 0
        for i in range(self.image.shape[0]):
            for j in range(self.image.shape[1]):
                for k in range(3):
                    #print(counter, i, j, k)
                    if counter < length:
                        text += "0" if self.image[i, j, k] % 2 == 0 else "1"
                        counter += 1
                    else:
                        return text[(4 * 8):]


    def extract_length(self):
        binary_length = ""
        counter = 0
        for i in range(self.image.shape[0]):
            for j in range(self.image.shape[1]):
                for k in range(3):
                    if counter < (4 * 8):
                        binary_length += "0" if self.image[i, j, k] % 2 == 0 else "1"
                        counter += 1
                    else:
                        length = int(binary_length, 2)
                        return length

    def get_bin_text(self):
        return self.bin_text
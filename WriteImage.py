
import cv2, re, os
from Functions import check_path_not_exist, check_path_already_exist

class WriteImage:

    def __init__(self, path:str, bin_text:str, output_path:str):
        self.path = path
        self.bin_text = bin_text
        self.output_path = output_path
        # checking if the file exist
        check_path_already_exist(self.path)
        self.original_image = cv2.imread(self.path) # this line needed for the next line

        self.check_text()
        self.check_output_path()
        # starting operations
        self.result_image = self.original_image.copy()
        self.write_png()
        self.save_png()


    def check_text(self):
        pass

    def check_output_path(self):
        # make sure the file ends with .png
        # make sure that the path is correct
        if not re.search(".png$", self.output_path):
            raise ValueError("Output path must end with .png")
        check_path_not_exist(self.output_path)


    def get_max_text_length(self):
        return self.original_image.shape[0] * self.original_image.shape[1] * 3

    def write_png(self):
        counter = 0
        for i in range(self.result_image.shape[0]):
            for j in range(self.result_image.shape[1]):
                for k in range(3):
                    if self.bin_text[counter] == "0":
                        self.result_image[i, j, k] = self.original_image[i, j, k] & 254
                    else:
                        self.result_image[i, j, k] = self.original_image[i, j, k] | 1
                    counter += 1
                    if len(self.bin_text) <= counter:
                        return

    def save_png(self):
        os.makedirs(self.output_path[:str(reversed(self.output_path)).find('/')], exist_ok=True)
        cv2.imwrite(self.output_path[str(reversed(self.output_path)).find('/') + 1:], self.result_image)

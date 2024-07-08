from HuffmanCode import *
from WriteImage import *
from ExtractImage import *
from ReadFile import *
from Functions import *


class MyMain:
    def __init__(self):
        self.huffmanCode = None
        self.writeImage = None
        self.extractImage = None
        self.readImage = None

    def hide_text_in_image(self, image_path, text_path, output_image_path):
        self.readFile = ReadFile(text_path)
        self.huffmanCode = HuffmanCode(self.readFile.get_message())
        bin_text = calculate_text_length(self.huffmanCode.get_bin_text())
        bin_text += self.huffmanCode.get_bin_text()
        self.WriteImage = WriteImage(image_path, bin_text, output_image_path)

    def extract_text_from_image(self, image_path):
        if self.huffmanCode == None:
            raise Exception("Huffman Code Not Found")
        self.extractImage = ExtractImage(image_path)
        messege = translate_bin_to_ascii(self.extractImage.get_bin_text(), self.huffmanCode.get_dict_bin_ascii())
        return messege

    def find_text_matches(self, text, regex_pattern):
        """

        :param text: the all text in the image that we need to search in
        :param regex_pattern:
        :return: list of indexes where text matches inside bin_text
        """
        # check_text(text)
        # check_regex(regex_pattern)
        text_matches, _ = find_all_regex_in_text(text, regex_pattern)
        print(text_matches, _)
        # text_matches = [text_matches[i] for i in range(len(text_matches))]
        if len(text_matches) == None:
            raise Exception("No Matches Found")
        for i in range(len(text_matches)):
            text_matches[i] = translate_ascii_to_bin(text_matches[i], self.huffmanCode.get_dict_ascii_bin())
        print(text_matches)
        matches_indexes_in_bin = find_string_in_text(self.huffmanCode.get_bin_text(), text_matches)
        print(self.huffmanCode.get_bin_text())
        print(matches_indexes_in_bin)
        indexes = calculate_place(matches_indexes_in_bin, self.extractImage.image.shape)
        return indexes

    def extract_and_crop(self, image_path, text, regex_pattern, output_image_path):
        indexes = self.find_text_matches(text, regex_pattern)
        for i in range(len(indexes)):
            img_name = f'Hi_{i}'
            print(indexes[i])
            crop_image(image_path, output_image_path, img_name, indexes[i][0], indexes[i][1])

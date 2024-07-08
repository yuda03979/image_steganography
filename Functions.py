
import re
import os
import platform

import cv2
import numpy as np


def calculate_text_length(text):
    max_length = (2 ** (8 * 4)) - (8 * 4) - 1
    text_length = len(text)
    if (text_length < 1 or text_length > max_length): # the size of max png is (2 ** 32) - 1
        raise ValueError("Text length must be between 1 and " + str(max_length))
    bin_length = bin(text_length)[2:]
    return bin_length.zfill(8 * 4)


def translate_bin_to_ascii(bin_text:str, dict_bin_ascii:dict):
    text = ""
    var = ""
    for i in bin_text:
        var += i
        if var in dict_bin_ascii:
            text += dict_bin_ascii[var]
            var = ''
    return text


def translate_ascii_to_bin(text:str, dict_ascii_bin:dict):
    bin_text = ""
    for letter in text:
        bin_text += dict_ascii_bin[letter]
    return bin_text

def find_all_regex_in_text(text:str, regex:str):
    """

    :param text:
    :param regex:
    :return: 2 lists containing all matches in text, and their indexes
    """
    pattern = re.compile(regex)
    iter_matches = pattern.finditer(text)
    text_matches = []
    index_matches = []
    for match in iter_matches:
        text_matches.append(match.group())
        index_matches.append(list(match.span()))
    return text_matches, index_matches


def find_string_in_text(text: str, list_sub_text: list):
    """
    :param text:
    :param sub_text:
    :return: list of tuples with all indexes e.g.(0 , 4) found or None if not found
    note: handle the case where sub_text is inside text multiple times
    """
    list_matches = []
    list_indexes_matches = []
    j = 0
    for i in list_sub_text:
        var = re.search(i, text[j:])
        if var:
            list_matches.append(var)
            list_indexes_matches.append([list_matches[-1].span()[0] + j, list_matches[-1].span()[1] + j])
            j = list_matches[-1].span()[-1] + j

    if len(list_indexes_matches) == 0:
        raise ValueError("No matches found in bin_text [Functions.py, find_all_regex_in_text()]")
    return list_indexes_matches


def calculate_indexes(i: int, png_size: tuple):
    """

    :param index_matches:
    :param png_size: (y, x) y its the y axis (the rows) and x is the x axis (the columns)
    :return:
    """
    print(png_size)
    indexes_list = [0, 0]
    indexes_list[0] = i // (png_size[1] * 3)
    indexes_list[1] = i - (indexes_list[0] * png_size[1] * 3)
    return indexes_list


def calculate_place(indexes_matches:list, png_size:tuple):
    """

    :param indexes_matches:
    :param png_size: (y, x) y its the y axis (the rows) and x is the x axis (the columns)
    :return:
    """
    final_indexes = []
    print(indexes_matches)
    for i in indexes_matches:
        final_indexes.append([[],[]])
        final_indexes[-1][0] = calculate_indexes(i[0], png_size)
        final_indexes[-1][1] = calculate_indexes(i[1], png_size)
    print(final_indexes)
    return final_indexes


def check_path_already_exist(path:str):
    if not os.path.exists(path):
        raise Exception(f'Path does not exist: {path}')


def check_path_not_exist(path:str):
    invalid_chars = {
        'Windows': r'<>:"/\|?*',
        'Linux': '/',
        'Darwin': '/'
    }

    system = platform.system()
    if system not in invalid_chars:
        raise ValueError(f"Unsupported operating system: {system}")

    invalid_char_set = set(invalid_chars[system])
    if not any(char in invalid_char_set for char in path):
        raise Exception(f"Invalid path to create: {path}")

#
# def crop_image(image_path, output_path, img_name, top_left, bottom_right):
#     image = cv2.imread(image_path)
#     output_path = os.path.join(output_path, img_name)
#     x_start, y_start = top_left[0], top_left[1]  # Starting point (x, y)
#     x_end, y_end = bottom_right[0], bottom_right[1] # Ending point (x, y)
#     cv2.imwrite(output_path, image[y_start:y_end, x_start:x_end])
import cv2
import os

def crop_image(image_path, output_path, img_name, top_left, bottom_right):
    """
    Crop a portion of an image and save it to a new file.

    :param image_path: Path to the input image file.
    :param output_path: Directory to save the cropped image.
    :param img_name: Name for the cropped image file.
    :param top_left: Tuple (x, y) for the top-left corner of the crop rectangle.
    :param bottom_right: Tuple (x, y) for the bottom-right corner of the crop rectangle.
    """
    # Read the image
    image = cv2.imread(image_path)
    if image is None:
        raise FileNotFoundError(f"The image at path {image_path} could not be found or opened.")
    top_left = [20, 20]
    bottom_right = [40, 40]
    # Ensure output path exists
    os.makedirs(output_path, exist_ok=True)
    output_file = os.path.join(output_path, img_name)

    # Get the coordinates
    x_start, y_start = top_left
    x_end, y_end = bottom_right
    x_end += 1
    y_end += 1
    print(x_start, x_end, y_start, y_end)
    # Check if coordinates are within image bounds
    height, width = image.shape[:2]
    if not (0 <= x_start < x_end <= width and 0 <= y_start < y_end <= height):
        raise ValueError("The provided coordinates are out of image bounds.")

    # Crop the image and save it
    cropped_image = image[y_start:y_end, x_start:x_end]
    cv2.imwrite(img=cropped_image, filename=output_file)









from HuffmanCode import HuffmanCode
from Functions import *
from MyMain import MyMain
import os


def main():
    my_main = MyMain()
    png_file = "/Users/yuda/My_Documents/programing/projects/mefathim/python_course/day_9/ElevatorChallenge_Python/brakes_wall.jpeg"
    messege_file = "messege.txt"
    output_png_file = "/Users/yuda/My_Documents/programing/projects/mefathim/python_course/day_9/ElevatorChallenge_Python/car1.png"
    my_main.hide_text_in_image(png_file, messege_file, output_png_file)
    print(my_main.extract_text_from_image(output_png_file))
    # my_main.extract_and_crop(output_png_file, "hello! you fucking stupid; you want to check me, hu? try this: חחח לא תצליח!! אין לי מושג איך גם עברית עובד אבל לא מתלוננים... :) "
    # "יאללה סתום", "hello", "/Users/yuda/My_Documents/programing/projects/mefathim/python_course/day_9/ElevatorChallenge_Python/")
    my_main.find_text_matches(text="hello! you fucking stupid; you want to check me, hu? try this:", regex_pattern=r"h")
    my_main.extract_and_crop(output_png_file, text="hello! you fucking stupid; you want to check me, hu? try this:", regex_pattern=r"h", output_image_path=)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

import math
def paint(height,width,cover):
    area= height*width
    number_of_cans = math.ceil(area/cover)
    print(f"You will need {number_of_cans} cans.")



test_h = int(input("Height: "))
test_w = int(input("Width: "))
coverage=5



paint(height=test_h,width=test_w,cover=coverage)
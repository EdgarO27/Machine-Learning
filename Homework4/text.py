import os



for filename in os.listdir("\\Projects\\MachineLearning\\Machine-Learning\\Homework4\\digit_dataset\\test"
):
    label = filename.split('_')[0]
    print(label)
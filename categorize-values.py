myMixedTypeList = [45, 290578, 1.02, True, "My dog is on the bed.", "45"]
for item in myMixedTypeList:
    # print(str(item) + " is of the data type " + str(type(item)))
    # print("{} is of the data type {}".format(item,type(item)))
    print(f"{item} is of data type {type(item)}")
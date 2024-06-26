import re

f = open("preproinsulin-seq.txt" , 'r')
data = f.read().replace('\n', "").replace("[0-9]","")

new_data = re.sub("ORIGIN", "", data)
# remove // characters
data_without_slash = re.sub("//", "", new_data)
# remove any numbers
# data_without_nums = re.sub("[0-9]", "", data_without_slash)
# remove any white spaces
cleaned_content = re.sub("\s", "", data_without_slash)

print(cleaned_content)
num_characters = len(cleaned_content)
print(f"The cleaned sequence has {num_characters} characters.")
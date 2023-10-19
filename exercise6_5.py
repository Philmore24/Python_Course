text = "X-DSPAM-Confidence:    0.8475"

int_postion = text.find(':')
print(int_postion)
part_string = text[int_postion+1:]
print(part_string)
num_value = float(part_string)
print(num_value)

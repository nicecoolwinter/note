


def bit_count(int_type):
    count = 0
    while(int_type):
        int_type &= (int_type - 1)
        count += 1
        print('hi')
    return(count)

print(bit_count(0b100))
print(bit_count(0b110))
print(bit_count(0b101100))
print(bit_count(0b111100))
# print(bit_count(-1)) # �L�k�B�z
# �Y���D�n��X��bit�A�h�i�H

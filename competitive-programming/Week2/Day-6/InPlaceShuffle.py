import random 

def random_number(floor,ceiling):
    return random.randint(floor,ceiling)

def shuffle(the_list):

    # Shuffle the input in place
    length = len(the_list)
    for i in range(0,length-1):
        j = random_number(0,length-1)
        the_list[i],the_list[j] =  the_list[j],the_list[i]     


sample_list = [1, 2, 3, 4, 5]
print 'Sample list:', sample_list

print 'Shuffling sample list...'
shuffle(sample_list)
print sample_list

"""
CMPS 2200  Assignment 1.
See assignment-01.pdf for details.
"""
# no imports needed.

def foo(x):
    ### TODO
    if x<=1:
        return x
    else:
        ra = (foo(x-1))
        rb = (foo(x-2))

        return ra+rb


def longest_run(mylist, key):
    ### TODO
    prev = None
    size = 0
    max_size = 0
    total_size = 0
    listlen = len(mylist)
    print("List Length: ", listlen)

    for i in range(listlen):
        print(prev, "prev b4 if")
        print(total_size)
        print(i)
        if key == prev:
            print("----------")
           ## print("key == prev")
            print(key, "KEY == ", prev, "PREV" )
            size += 1
            print("Size: ", size)
            print("----------")
            if size > max_size:
                max_size = size
                   ## print(size, "size on run")
                print(max_size, "max size")
        else:

            size = 0
        if i < listlen-2:
            prev = mylist[i+1]
        total_size += 1

    return max_size

    pass


class Result:
    """ done """
    def __init__(self, left_size, right_size, longest_size, is_entire_range):
        self.left_size = left_size               # run on left side of input
        self.right_size = right_size             # run on right side of input
        self.longest_size = longest_size         # longest run in input
        self.is_entire_range = is_entire_range   # True if the entire input matches the key
        
    def __repr__(self):
        return('longest_size=%d left_size=%d right_size=%d is_entire_range=%s' %
              (self.longest_size, self.left_size, self.right_size, self.is_entire_range))
    
    
def longest_run_recursive(mylist, key):
    ### TODO
    pass

## Feel free to add your own tests here.
def test_longest_run():
    ##if longest_run([2,12,12,8,12,12,12,0,12,1], 12) == 3:
        ##print("Test one complete")
    if longest_run([12, 12, 12, 8, 12, 12, 0, 12, 12, 12, 12], 12) == 4:
        print("Test two complete")
    ##assert longest_run([2,12,12,8,12,12,12,0,12,1], 12) == 3
    ##assert longest_run([12, 12, 12, 8, 12, 12, 0, 12, 12, 12, 12], 12) == 4


test_longest_run()


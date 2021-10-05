def linear_search(list,target):
    for users in range(0,len(list)):
        if list[users] == target:
            return users  
    return None

def verify(index):
    if index is not None:
        print('the target is at index: ', index)
    else:
        print('Target is not in list')

numbers = [1,2,3,4,5,6,7,8]

result =linear_search(numbers, 2)
verify(result)  





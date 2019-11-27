def is_member(list1:list,list2:list):
    for data1 in list1:
        if list2.__contains__(data1):
            return True
        return False
print(is_member([12,5],[34,5]))
def segregate(head):
    #code here
    count = [0,0,0]
    temp = head
    while temp:
        count[temp.data] += 1
        temp = temp.next
    i = 0
    temp = head
    while temp:
        if count[i] == 0:
            i += 1
        else:
            temp.data = i
            count[i] -= 1
            temp = temp.next
    return head
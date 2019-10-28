# import copy
#
# # initializing list 1
# li1 = [1, 2, [3,5], 4]
#
# # using deepcopy to deep copy
# li2 = copy.deepcopy(li1)
#
# # original elements of list
# print ("The original elements before deep copying")
# for i in range(0,len(li1)):
#     print (li1[i],end=" ")
#
# print("\r")
#
# # adding and element to new list
# li2[2][0] = 7
#
# # Change is reflected in l2
# print ("The new list of elements after deep copying ")
# for i in range(0,len( li1)):
#     print (li2[i],end=" ")
#
# print("\r")
#
# # Change is NOT reflected in original list
# # as it is a deep copy
# print ("The original elements after deep copying")
# for i in range(0,len( li1)):
#     print (li1[i],end=" ")

# colors = ["red", "green", "blue", "purple"]
# for i in range(len(colors)):
#     print(colors[i])

# presidents = ["Washington", "Adams", "Jefferson", "Madison", "Monroe", "Adams", "Jackson"]
# for i in range(len(presidents)):
#     print("President {}: {}".format(i + 1, presidents[i]))

presidents = ["Washington", "Adams", "Jefferson", "Madison", "Monroe", "Adams", "Jackson"]
for num, name in enumerate(presidents, start=1):
    print("President {}: {}".format(num, name))

colors = ["red", "green", "blue", "purple"]
ratios = [0.2, 0.3, 0.1, 0.4]
for i, color in enumerate(colors):
    ratio = ratios[i]
    print("{}% {}".format(ratio * 100, color))

#Our real goal is to loop over two lists at once. This need is common enough that there’s a special built-in function just for this.
# Python’s zip function allows us to loop over multiple lists at the same time:

colors = ["red", "green", "blue", "purple"]
ratios = [0.2, 0.3, 0.1, 0.4]
for color, ratio in zip(colors, ratios):
    print("{}% {}".format(ratio * 100, color))

#If you need to loop over multiple lists at the same time, use zip
#If you only need to loop over a single list just use a for-in loop
#If you need to loop over a list and you need item indexes, use enumerate
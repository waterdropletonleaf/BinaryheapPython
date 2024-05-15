heap_list = []
class heap:
    #insert
    def insert(a):
        global root
        global count
        
        # print(len(heap_list))
        # print("A is ", a)
        # print(heap_list)
        if(len(heap_list) == 0):
            root = a
            heap_list.insert(0, a)
            # print("before count reassignment:", count)
            count = 1
        elif(root > a):
            # the number here gets reassigned to another place in the list
            root = a
            heap_list.insert(0, root)
            
            count = count + 1

        else: #a is less than(or equal to)  root
            if((count % 2) == 0):
                
                heap_list.insert(2*count + 2, a)
                #heap_list.append(a)
                for x in range(count):
                    if(heap_list[count] < heap_list[(count - 1)%2]): #soon to be X
                        temp = heap_list[(count - 1)%2]
                        heap_list[(count - 1)%2] =  heap_list[count]
                        heap_list[count] = temp
                count = count + 1
                
                
            else:
                
                heap_list.insert(2*count + 1, a)
                #heap_list.append(a)
                for x in range(count):
                    if(heap_list[count] < heap_list[(count - 1)%2]): #soon to be X
                        temp = heap_list[(count - 1)%2]
                        heap_list[(count - 1)%2] =  heap_list[count]
                        heap_list[count] = temp
                count = count + 1
                #if the new is greater than the previous
                # I NEED TO LOOK AT THE SUBTREES INSTEAD OF THE LIST AS A WHOLE
                    
                    
                    
    def little_display():
        print(heap_list)
        
    def extract_min():
        print("EXTRACT MIN",heap_list[0])
        heap_list[0] = heap_list[count - 1] # zero is gone
        heap_list.pop(count -1)
        for x in range(len(heap_list) - 1):
            if(heap_list[0] > heap_list[x] ):
                temp = heap_list[0]
                heap_list[0] = heap_list[x]
                heap_list[x] = temp
                print("apple")
            elif(heap_list[x -1] > heap_list[x]):
                temp = heap_list[ x -1 ]
                heap_list[x -1 ] = heap_list[x]
                heap_list[x] = temp
                
    def proper_display():
        level = 0
        #traverse through array, starting from the rightmost portion of the 
        #tree
        #might just make a function for that, if not
        for x in range(len(heap_list)):
            for y in range(level + 1):
                print(end= " ")
                level = level + 1
            print(heap_list[x])
            
            
        # display spaces based on the level of the item 
        # print item 
        # do it again with the next item 
        #
        
        
#     def display():
# #you print the amount of spaces for the root which would be the length of the list divided by 2
#         for x in range(len(heap_list) // 2):
#             print(end = " ")
#             print(heap_list[0])
# # if it is left, then you print 1 less space than it's parent
#         for x in range(len(heap_list)):
            
# if it is right, the you print 1 more space than it's parent\
        
        
        
        
        
        
        
    # def display_help():
    #     for x in range(len(heap_list) // 2):
    #         for y in range(x):
    #             print(" ", end=" ")
    #         print(heap_list[x])
    #     for a in range((len(heap_list) // 2) + 1, len(heap_list) ):
    #         for b in range(len(heap_list) -1):
    #              print(" ", end=" ")
    #         print(heap_list[a])
                
        
        

# take the middle of list
# print numbers until middle 
# take what is left(lenght of heap_list/2 -> end of heap list)


    # def display_help():
    #     for x in range(len(heap_list)):
    #         for y in range(x):
    #             print(" ", end=" ")
    #         print(heap_list[x])
                #if count is even: 2i +1
                #if count is odd 2i +2
                #use mod/2 to determine count is even or odd
            
            #insert number into list
            #figure out where number needs to go

    #extract min
    # pop the root(index 0)
    #will have to decrease count by 1

    
    # }

    # // display recursive helper
#     def display_recursive(level):
#         if(root != None):
#             display_recursive(level+1)
#             for x in range(level):
#                 x = x + 1
#                 print("     ")
#             print(heap_list[2*i +2])
#             display_recursive(level + 1)
#             i = i + 1
#     def big_display():
#     #     // display()
#     # public void display(){
#         display_recursive(0)
#     #         for(int i=0; i < level; i++){
#     #             System.out.print("     ");
#     #         }
#     #         System.out.println(stroot.get_num());
#     #         display_recursive(stroot.get_left(), level+1);
#     #     }
#     #     //else{
#     #         // if you hit the null do nothing
#     #     //}
#     # }

        
#         # for x in range(len(heap_list)):
#         #     if x is 0 :
#         #         print("                 ", end= ' ')
#         #         print(heap_list[x])
#         #         print("                 ", end= ' ')
#     #print tabs/spaces for each position the number is at? 
        

#     #visualize

# #idea: counting variable?
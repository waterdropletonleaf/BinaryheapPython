import binary_heap
bh = binary_heap.heap
# numbers are 1, 2,3, 17, 19, 36, 7, 25 100
#subtrees should be
#SBT1:0; 1; 2; 5;
#SBT2:0; 3; 4;

bh.insert(2)
bh.insert(3)
bh.insert(1)
bh.insert(17)
bh.insert(19)
bh.insert(36)
bh.insert(7)
bh.insert(25)
bh.insert(100)
bh.little_display()
bh.extract_min() #extract min needs more work, it is swapping but it is not going down
bh.little_display()
bh.proper_display()
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
    
class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        temp_list=ListNode(0)
        changing = temp_list
        temp = Heap(lists)
        while temp.heap:
            changing.next=temp.remove()
            changing=changing.next
        return temp_list.next
            

class Heap:
    def __init__(self,data):
        self.heap = list(filter(lambda x:x,data))
        self.max_index = len(self.heap)-1
        self.heapify()
    
    def leftchild(self,index):
        return index*2+1
    def rightchild(self,index):
        return index*2+2
        
    def heapify(self):
        before_leaf= (self.max_index-1)//2
        while before_leaf>=0:
            self.shift_down(before_leaf)
            before_leaf-=1
    def shift_up(self,index):
        parent = (index-1)//2
        if parent>=0 and self.heap[index].val<self.heap[parent].val:
            self.heap[parent],self.heap[index]=self.heap[index],self.heap[parent]
            self.shift_up(parent)
    def insert(self,node):
        self.heap.append(node)
        self.max_index+=1
        self.shift_up(self.max_index)
    def shift_down(self,index):
        if self.leftchild(index)<=self.max_index:
            ch_l,ch_r = self.leftchild(index) ,self.rightchild(index)
            if ch_r <=self.max_index and self.heap[ch_l].val > self.heap[ch_r].val:
                candidate_index = ch_r
            else:
                candidate_index = ch_l
            if self.heap[index].val>self.heap[candidate_index].val:
                self.heap[index],self.heap[candidate_index]=self.heap[candidate_index],self.heap[index]
                self.shift_down(candidate_index)
                    
    def remove(self):
        self.heap[0],self.heap[self.max_index]=self.heap[self.max_index],self.heap[0]
        new_data = self.heap.pop()
        self.max_index-=1
        self.shift_down(0)
        if new_data:
            if new_data.next:
                self.insert(new_data.next)
        return new_data
                
        
        
        
        
            
            
        

class MinHeap:
    def __init__(self):
        self.heap_list = [0]
        self.size = 0

    def sift_up(self, i):
        while i // 2 > 0:
            if self.heap_list[i] < self.heap_list[i//2]:
                self.heap_list[i], self.heap_list[i//2] = self.heap_list[i//2], self.heap_list[i]
                i = i // 2
    def sift_down(self, i):
        while (i*2) <= self.size:
            mc = self.min_child(i)
            if self.heap_list > self.heap_list[mc]:
                self.heap_list[i], self.heap_list[mc] = self.heap_list[mc], self.heap_list[i]
            i = mc

    def min_child(self, i):
        if (i * 2)+1 > self.size:
            return i * 2
        else:
            pass
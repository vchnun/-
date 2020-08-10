class List(list):
    def __getindex(self, low, high):
        tmp = self[high]
        while(low < high):
            while(low < high and self[low] <= tmp):
                low += 1
            else:
                self[high] = self[low]
            while(low < high and self[high] >= tmp):
                high -= 1
            else:
                self[low] = self[high]
        else:
            self[high] = tmp
            return high

    def __quick_sort(self, low, high):
        if low < high:
            i = self.__getindex(low, high)
            self.__quick_sort(low, i-1)
            self.__quick_sort(i+1, high)
            # print(self)


    def quick_sort(self,):
        self.__quick_sort(0, self.__len__()-1)
        
import random
if __name__ == "__main__":
    # a = List([random.randint(10,99) for i in range(10)])
    a = List([1,2,5,7,4,3,6])
    b = a.copy()
    print(a)
    a.quick_sort()
    print(a)
    b.sort()
    print(b)
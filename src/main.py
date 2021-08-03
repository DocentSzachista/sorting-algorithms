

class Sorts(object):

    @staticmethod
    def bubble_sort(array) ->None:
        """ Sorts the array using bubble sort algorithm

            Description 
            -----------

            Sorts the array by compairing two neightbouring array elements and is swapping them if the order is disturbed
            The average performance of this algorithm is  O(n^2)
        """
        try:
            for i in range(len(array)):
                for j in range(len(array)-1):
                    if array[i] < array[j]:
                        array[i], array[j] = array[j], array[i]
        except TypeError:
            print("Your input array can't be a null value")

    @staticmethod
    def insert_sort(array) ->None:
        try:
            leng = len(array)
            for i in range(1 ,leng):
                j = i
                while array[j] < array[j-1] and j>0:
                    array[j-1] , array[j] = array[j] , array[j-1]
                    j-=1
        except TypeError:
            print("Your input array can't be a null value")

    @staticmethod
    def quick_sort(arr, start_index, end_index) -> None:
        try:
            if start_index < end_index:
                index =Sorts.__partition(arr, start_index, end_index)
                Sorts.quick_sort(arr, start_index, index)
                Sorts.quick_sort(arr, index+1, end_index)
        except TypeError:
            print("Your input array can't be a null value")

    @staticmethod
    def __partition( arr, start_index, end_index) -> None:
        pivot = arr[end_index]
        l = start_index
        r = end_index
        while True:
            while arr[l] < pivot: l+=1
            while arr[r] > pivot: r-=1
            if l<r:
                arr[l], arr[r] = arr[r], arr[l]
                l+=1
                r-=1
            else:
                if r == end_index: r-=1
                return r



    @staticmethod
    def merge_sort( array, left, right) -> None:
        if right > left:
            middle = int(left+(right-1)/2)
            Sorts.merge_sort(array,left, middle )
            Sorts.merge_sort(array,middle+1, right)
            Sorts.__merge(array, left, middle, right)

    @staticmethod
    def __merge(array, left, middle, right) -> None:
        sub_arr1=[]
        sub_arr2=[]
        for iterator in range(middle-left+1):
            sub_arr1.append(array[iterator + left])
        for iterator in range(right-middle):
            sub_arr2.append(array[iterator+1+middle])
        index1=index2=0
        merged = left
        while index1 < middle-left+1 and index2 < right-middle :
            if sub_arr1[index1] <= sub_arr2[index2]:
                array[merged] = sub_arr1[index1]
                index1+=1
            else:
                array[merged] = sub_arr2[index2]
                index2+=1
            merged+=1
            
    #A - tablica z liczbami do posortowania
    #B - posortowana tablica
    #C - helper tab 
    #K - maksymalny przedzial liczb
    @staticmethod
    def counting_sort( array, num_range=0) -> None:
        """ Sorts the array by using counting sort algorithm

            Description
            -----------
            Counting sort is an algorithm which counts the number of given number occurences in an array
            and after some arithmetics it calculates the position of each number in the output sequence
            
            Steps
            -----
            
            1. Initialize array to hold each unique number occurence in main array
            2. Modify this array to hold at each index sum of previous index counts
            3. Output each number from the input sequence decreasing its count by 1

        """
        try:
            if num_range ==0:
                num_range = max(array)

            sorted_array = [0]*(len(array))
            count_array = [0]*(num_range+1)

            for iterator in range(len(array)):
                count_array[array[iterator]] +=1
            
            for iterator in range(1 ,num_range+1):
                count_array[iterator] += count_array[iterator -1]  
            
            for iterator in range(len(array)-1, -1, -1):
                sorted_array[count_array[array[iterator]] -1 ] = array[iterator]
                count_array[array[iterator]]-=1
            
            for iterator in range(len(array)):
                array[iterator] = sorted_array[iterator]
        except (TypeError, ValueError):
            print("Your array cannot be a null")

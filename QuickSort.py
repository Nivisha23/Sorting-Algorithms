arr = [34, 23, 76, 56, 98, 34, 20, 10, 36]
print(arr)

def quick_sort(arr):
    
    less, equal, greater = [], [], []

    if len(arr) <= 1:
        return arr

    else:
        for i in arr:
            
            if i > arr[-1]:
                greater.append(i)
            
            elif i == arr[-1]:
                equal.append(i)
                
            else:
                less.append(i)
           
            # print('less = ',less, 'equal = ',equal, 'greater = ', greater)
        
        return quick_sort(less)+ equal+ quick_sort(greater)
    

def main():
    print(quick_sort(arr))

main()

# 假设子树已经调节好，调节的目的是把当前树根放到合适的位置，也就是下沉

def HeapAdjust(arr,start,end):
    k = start
    sd = arr[k]
    i = 2*k+1
    while i<=end:
        if i<end and arr[i]<arr[i+1]:
            i+=1
        if sd < arr[i]:
            arr[k]=arr[i]
            k=i
        else:
            break
        i=2*i+1
    arr[k] = sd

def HeapBuild(arr,len):
    for i in range((len-1)//2,-1,-1):
        HeapAdjust(arr,i,len-1)

def HeapSort(arr,len):
    HeapBuild(arr,len)
    # 交换堆顶和堆底，这样，大根堆得出从小到大，小根堆得出从大到小，先得出最后的
    for i in range(0,len-1):
        tmp =  arr[0]
        arr[0] = arr[len-i-1]
        arr[len-i-1] = tmp
        HeapAdjust(arr,0,len-2-i)

a = [9,4,6,0,8]
HeapSort(a,5)
print(a)


    
#Hackerank Python Find The Runner Up!
n = int(input())
arr = list(set(map(int,input().split())))
arr.sort(reverse=True)
print(arr[1])

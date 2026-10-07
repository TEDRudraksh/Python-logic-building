# 28. P is one-dimensional array of integers. Write a Java program search for a data VAL from P. If VAL is present in the array then “element found ” otherwise “element not found” should be displayed. 



arr = [1,2,9,5,6,7,4]
k=5
for i in arr:
    if i==k:
        print("element found")
        break
else:
    print("not found")
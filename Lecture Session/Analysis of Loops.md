# Analysis of Loops

## 1
```python
# Here c is a constant   
for i in range(c):
    # some O(1) expressions
    print(i)
```
## 2
```python
# Here c is a positive integer constant
for i in range(0, n, c):
    # some O(1) expressions
    print(i)


for i in range(n - 1, -1, -c):
    # some O(1) expressions
    print(i)
```
## 3
```python
for i in range(0, n, c):
    for j in range(0, n, c):
        # some O(1) expressions


for i in range(0, n, c):
    for j in range(0, n, c):
        for k in range(0, n, 2 * c):
            # some O(1) expressions
```
## 4
```python
i = 0

while i < n:
    # some O(1) expressions
    i *= c # Here c is a positive integer constant


j = n

while j > 0:
    # some O(1) expressions
    j /= c # Here c is a positive integer constant
```
## 5
```python
i = 2

while i < n:
    # some O(1) expressions
    i = i ** c
```
## 6
```python
i, j = 0, 1

while i < n:
    i += j
    j += 1
```
## 7
```python
i = n
count = 0

while i > 0:
    for j in range(i):
        count += 1

    i /= 2

print(count)
```
## 8
```python
i = n

while i > 0:
    for j in range(i, 0, -1):
        count += 1

    i -= 1
```
## 9
```python
# Here arr is a list of integer  
i, j = 0, 0

for i in range(n):
    while j < n and arr[i] < arr[j]:
        j += 1
```
## 10
```python
def fun_1(n):
    if n < 1:
        return

    fun_1(n - 1)
    print(n)
```
## 11
```python
def fun_1(n):
    if n <= 1:
        return n

    return 2 * fun_1(n - 1)


def fun_2(n):
    if n < 1:
        return 1

    return fun_2(n - 1) + fun_2(n - 1)
```
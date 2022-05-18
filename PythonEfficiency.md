# Python Efficiency

## Split up multiple rules

```python
if n == 0:
        return None
if W == 0:
        return None
if n != len(values):
        return None
```

is ~2x as fast as making all of the stipulations on one line

```python
if n == 0 or W == 0 or n != len(values):
        return None
```

 

Results

----



<img src="/home/sayf/.config/Typora/typora-user-images/image-20220505100431056.png" alt="image-20220505100431056" style="zoom: 67%;" align="left" />



## Making a pandas dataframe is expensive

![image-20220505101143960](/home/sayf/.config/Typora/typora-user-images/image-20220505101143960.png)



## range and enumerate are pretty even

![image-20220507102842131](/home/sayf/.config/Typora/typora-user-images/image-20220507102842131.png)

## Use 'in' instead of regex when possible

![image-20220507124500479](/home/sayf/.config/Typora/typora-user-images/image-20220507124500479.png)

![image-20220507124512197](/home/sayf/.config/Typora/typora-user-images/image-20220507124512197.png)

## List comps vs for-loops

### List comps are significantly faster for making lists

![image-20220508093806985](/home/sayf/.config/Typora/typora-user-images/image-20220508093806985.png)

### For-loops are faster for only iteration

- This is because the list comp will still store the data as a list

<img src="/home/sayf/.config/Typora/typora-user-images/image-20220508095544557.png" alt="image-20220508095544557" style="zoom:67%" align="left"/>

### List comp is faster for operations within the loop

<img src="/home/sayf/.config/Typora/typora-user-images/image-20220508095031729.png" alt="image-20220508095031729" style="zoom:67%;" align="left" />
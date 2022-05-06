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
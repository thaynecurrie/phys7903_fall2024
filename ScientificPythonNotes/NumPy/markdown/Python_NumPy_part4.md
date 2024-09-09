# _Python for Scientific Data Analysis_

# NumPy/SciPy

## Section 4: More Array Operations: Concatenating, Stacking and Splitting, Repeating, and Meshgrid; Array Broadcasting

### Concatenation 

#### _concatenating vectors and matrices_ 

NumPy allows a fairly straightforward way to concatenate arrays with the ``np.concatenate`` function.   The function accepts a list of arrays (i.e. enclosed by [ ]). Here's an example:


```python
import numpy as np


arr = np.random.randn(5, 4)
print(arr)
print('')
arr2=arr+np.random.randn(arr.shape[0],arr.shape[1])*0.1  #create another array that is just slightly different from the first one

print(arr2)

print('')
arr3=np.concatenate([arr,arr2])

print(arr3)

print(arr2.shape, arr3.shape)
```

    [[-0.60420594  0.77760138 -0.34556717  0.10818886]
     [ 0.5676424   1.04884126  0.92071367 -0.33600685]
     [-0.6102725   0.22099141 -0.28742492  1.53369688]
     [-1.16337195 -1.03147184 -0.02566285  0.12433982]
     [ 0.59715548 -0.05129267  0.12684328  0.65785089]]
    
    [[-0.55855696  0.69580998 -0.17453603 -0.05199762]
     [ 0.49821526  0.93997613  0.97315659 -0.09388734]
     [-0.7265761   0.21241606 -0.1572816   1.48832164]
     [-1.15668786 -1.16209237 -0.08928653  0.01128033]
     [ 0.74298213 -0.23702775 -0.08153408  0.62265544]]
    
    [[-0.60420594  0.77760138 -0.34556717  0.10818886]
     [ 0.5676424   1.04884126  0.92071367 -0.33600685]
     [-0.6102725   0.22099141 -0.28742492  1.53369688]
     [-1.16337195 -1.03147184 -0.02566285  0.12433982]
     [ 0.59715548 -0.05129267  0.12684328  0.65785089]
     [-0.55855696  0.69580998 -0.17453603 -0.05199762]
     [ 0.49821526  0.93997613  0.97315659 -0.09388734]
     [-0.7265761   0.21241606 -0.1572816   1.48832164]
     [-1.15668786 -1.16209237 -0.08928653  0.01128033]
     [ 0.74298213 -0.23702775 -0.08153408  0.62265544]]
    (5, 4) (10, 4)


Note that the ``shape`` of the two input arrays  -- ``arr`` and ``arr2`` -- are each (5,4).   And the shape of the concatenated array is (10,4) (ten rows and four columns).  Now we can invoke the ``axis`` keyword to control _how_ these arrays are concatenated.  I.e. 


```python

arr4=np.concatenate([arr,arr2],axis=1)

print(arr4)

print(arr4.shape)
```

    [[-0.60420594  0.77760138 -0.34556717  0.10818886 -0.55855696  0.69580998
      -0.17453603 -0.05199762]
     [ 0.5676424   1.04884126  0.92071367 -0.33600685  0.49821526  0.93997613
       0.97315659 -0.09388734]
     [-0.6102725   0.22099141 -0.28742492  1.53369688 -0.7265761   0.21241606
      -0.1572816   1.48832164]
     [-1.16337195 -1.03147184 -0.02566285  0.12433982 -1.15668786 -1.16209237
      -0.08928653  0.01128033]
     [ 0.59715548 -0.05129267  0.12684328  0.65785089  0.74298213 -0.23702775
      -0.08153408  0.62265544]]
    (5, 8)


This yields an array ``arr4`` with a shape of (5,8) (i.e now we have five rows and eight columns).

### Stacking and Splitting

#### _array stacking_

In the previous sections you found how you can create NumPy arrays as 1-D vectors and then reshape these 1-D vectors into 2-D arrays (matrices).   And you also saw how to combine arrays together via concatenation.   Now if, for whatever reason, you just are philsophically opposed to concatenation never fear: there is another NumPy operation at your disposal: _stacking_.   There are a couple of ways to stack arrays.

* _hstack_ - stacks arrays horizontally
* _vstack_ - stacks arrays vertically
* _columnstack_ stacks vectors in columns

A simple example:


```python
newarr=np.array([1,2,3,4,5])
newarr2=np.array([6,7,8,9,10])
```


```python
np.vstack([newarr,newarr2])
```




    array([[ 1,  2,  3,  4,  5],
           [ 6,  7,  8,  9, 10]])




```python
np.hstack([newarr,newarr2])
```




    array([ 1,  2,  3,  4,  5,  6,  7,  8,  9, 10])




```python
np.column_stack([newarr,newarr2])
```




    array([[ 1,  6],
           [ 2,  7],
           [ 3,  8],
           [ 4,  9],
           [ 5, 10]])



A slightly more involved example with a matrix instead of a 1-D vector.


```python
arr5=np.vstack([arr,arr2])
arr5
```




    array([[-0.60420594,  0.77760138, -0.34556717,  0.10818886],
           [ 0.5676424 ,  1.04884126,  0.92071367, -0.33600685],
           [-0.6102725 ,  0.22099141, -0.28742492,  1.53369688],
           [-1.16337195, -1.03147184, -0.02566285,  0.12433982],
           [ 0.59715548, -0.05129267,  0.12684328,  0.65785089],
           [-0.55855696,  0.69580998, -0.17453603, -0.05199762],
           [ 0.49821526,  0.93997613,  0.97315659, -0.09388734],
           [-0.7265761 ,  0.21241606, -0.1572816 ,  1.48832164],
           [-1.15668786, -1.16209237, -0.08928653,  0.01128033],
           [ 0.74298213, -0.23702775, -0.08153408,  0.62265544]])




```python
      
arr6=np.hstack([arr,arr2])
arr6
```

    [[0. 0. 0. 0. 0. 0. 0. 0.]
     [0. 0. 0. 0. 0. 0. 0. 0.]
     [0. 0. 0. 0. 0. 0. 0. 0.]
     [0. 0. 0. 0. 0. 0. 0. 0.]
     [0. 0. 0. 0. 0. 0. 0. 0.]]



You'll notice that in these cases the resulting arrays ``arr5`` and ``arr6`` are identical to ``arr3`` and ``arr4``, respectively.


```python
print(arr5-arr3)
print(arr6-arr4)
```

    [[0. 0. 0. 0.]
     [0. 0. 0. 0.]
     [0. 0. 0. 0.]
     [0. 0. 0. 0.]
     [0. 0. 0. 0.]
     [0. 0. 0. 0.]
     [0. 0. 0. 0.]
     [0. 0. 0. 0.]
     [0. 0. 0. 0.]
     [0. 0. 0. 0.]]
    [[0. 0. 0. 0. 0. 0. 0. 0.]
     [0. 0. 0. 0. 0. 0. 0. 0.]
     [0. 0. 0. 0. 0. 0. 0. 0.]
     [0. 0. 0. 0. 0. 0. 0. 0.]
     [0. 0. 0. 0. 0. 0. 0. 0.]]


#### _array splitting_

``split``  slices apart an array into multiple arrays along an axis .  For example, starting with ``arr3`` from before


```python

print(arr3)
       
print('')
first,second=np.split(arr3,[1])

print(first)

print('')
print(second)

      
```

    [[-0.60420594  0.77760138 -0.34556717  0.10818886]
     [ 0.5676424   1.04884126  0.92071367 -0.33600685]
     [-0.6102725   0.22099141 -0.28742492  1.53369688]
     [-1.16337195 -1.03147184 -0.02566285  0.12433982]
     [ 0.59715548 -0.05129267  0.12684328  0.65785089]
     [-0.55855696  0.69580998 -0.17453603 -0.05199762]
     [ 0.49821526  0.93997613  0.97315659 -0.09388734]
     [-0.7265761   0.21241606 -0.1572816   1.48832164]
     [-1.15668786 -1.16209237 -0.08928653  0.01128033]
     [ 0.74298213 -0.23702775 -0.08153408  0.62265544]]
    
    [[-0.60420594  0.77760138 -0.34556717  0.10818886]]
    
    [[ 0.5676424   1.04884126  0.92071367 -0.33600685]
     [-0.6102725   0.22099141 -0.28742492  1.53369688]
     [-1.16337195 -1.03147184 -0.02566285  0.12433982]
     [ 0.59715548 -0.05129267  0.12684328  0.65785089]
     [-0.55855696  0.69580998 -0.17453603 -0.05199762]
     [ 0.49821526  0.93997613  0.97315659 -0.09388734]
     [-0.7265761   0.21241606 -0.1572816   1.48832164]
     [-1.15668786 -1.16209237 -0.08928653  0.01128033]
     [ 0.74298213 -0.23702775 -0.08153408  0.62265544]]



```python
print(arr3)
print('')
first,second,third=np.split(arr3,[2,4])

print(first)
print('')
print(second)
print('')
print(third)
print('')
       
first,second=np.split(arr3,[1],axis=1)

print(first)

print(second)
```

    [[-0.60420594  0.77760138 -0.34556717  0.10818886]
     [ 0.5676424   1.04884126  0.92071367 -0.33600685]
     [-0.6102725   0.22099141 -0.28742492  1.53369688]
     [-1.16337195 -1.03147184 -0.02566285  0.12433982]
     [ 0.59715548 -0.05129267  0.12684328  0.65785089]
     [-0.55855696  0.69580998 -0.17453603 -0.05199762]
     [ 0.49821526  0.93997613  0.97315659 -0.09388734]
     [-0.7265761   0.21241606 -0.1572816   1.48832164]
     [-1.15668786 -1.16209237 -0.08928653  0.01128033]
     [ 0.74298213 -0.23702775 -0.08153408  0.62265544]]
    
    [[-0.60420594  0.77760138 -0.34556717  0.10818886]
     [ 0.5676424   1.04884126  0.92071367 -0.33600685]]
    
    [[-0.6102725   0.22099141 -0.28742492  1.53369688]
     [-1.16337195 -1.03147184 -0.02566285  0.12433982]]
    
    [[ 0.59715548 -0.05129267  0.12684328  0.65785089]
     [-0.55855696  0.69580998 -0.17453603 -0.05199762]
     [ 0.49821526  0.93997613  0.97315659 -0.09388734]
     [-0.7265761   0.21241606 -0.1572816   1.48832164]
     [-1.15668786 -1.16209237 -0.08928653  0.01128033]
     [ 0.74298213 -0.23702775 -0.08153408  0.62265544]]
    
    [[-0.60420594]
     [ 0.5676424 ]
     [-0.6102725 ]
     [-1.16337195]
     [ 0.59715548]
     [-0.55855696]
     [ 0.49821526]
     [-0.7265761 ]
     [-1.15668786]
     [ 0.74298213]]
    [[ 0.77760138 -0.34556717  0.10818886]
     [ 1.04884126  0.92071367 -0.33600685]
     [ 0.22099141 -0.28742492  1.53369688]
     [-1.03147184 -0.02566285  0.12433982]
     [-0.05129267  0.12684328  0.65785089]
     [ 0.69580998 -0.17453603 -0.05199762]
     [ 0.93997613  0.97315659 -0.09388734]
     [ 0.21241606 -0.1572816   1.48832164]
     [-1.16209237 -0.08928653  0.01128033]
     [-0.23702775 -0.08153408  0.62265544]]


### Repeating Array Elements

It's often useful to create an array that is a repeat or replication of another array some number of times.   E.g. IDL's replicate function does this for scalars: with some trickery you can make it work for vectors and arrays.   Python has stand-alone functions for exactly this purpose.

Two useful tools for repeating or replicating arrays to produce larger arrays are the
``repeat`` and ``tile`` functions. 

``repeat`` replicates each element in an array some number
of times, producing a larger array.  E.g.


```python
a=np.arange(3)
#array([0,1,2])
a
```




    array([0, 1, 2])




```python
a.repeat(3)
#array([0, 0, 0, 1, 1, 1, 2, 2, 2])
```




    array([0, 0, 0, 1, 1, 1, 2, 2, 2])



By default, if you pass an integer, each element will be repeated that number of times.
If you pass an array of integers, each element can be repeated a different number of
times:


```python

a.repeat([2,3,4])
#array([0, 0, 1, 1, 1, 2, 2, 2, 2])

```




    array([0, 0, 1, 1, 1, 2, 2, 2, 2])



Multidimensional arrays can have their elements repeated along a particular axis.


```python
arr = np.random.randn(2, 2)
arr
```




    array([[-0.77364227,  1.18296869],
           [-0.45712094,  0.94071693]])




```python
arr.repeat(2,axis=0)

  
```




    array([[-0.77364227,  1.18296869],
           [-0.77364227,  1.18296869],
           [-0.45712094,  0.94071693],
           [-0.45712094,  0.94071693]])




```python
     
arr.repeat(2,axis=1)
```




    array([[-0.77364227, -0.77364227,  1.18296869,  1.18296869],
           [-0.45712094, -0.45712094,  0.94071693,  0.94071693]])



Note that if no axis is passed, the array will be flattened first, which is likely not what
you want. Similarly, you can pass an array of integers when repeating a multidimensional
array to repeat a given slice a different number of times:


```python
arr.repeat([3,2], axis=0)
```




    array([[-0.77364227,  1.18296869],
           [-0.77364227,  1.18296869],
           [-0.77364227,  1.18296869],
           [-0.45712094,  0.94071693],
           [-0.45712094,  0.94071693]])



``tile`` is different. tile, on the other hand, is a shortcut for stacking copies of an array along an axis.
Visually you can think of it as being akin to “laying down tiles”:


```python

print(arr)
       
np.tile(arr,2)

```

    [[-0.77364227  1.18296869]
     [-0.45712094  0.94071693]]





    array([[-0.77364227,  1.18296869, -0.77364227,  1.18296869],
           [-0.45712094,  0.94071693, -0.45712094,  0.94071693]])



The second argument is the number of tiles; with a scalar, the tiling is made row by
row, rather than column by column. The second argument to tile can be a tuple
indicating the layout of the “tiling”:


```python

print(np.tile(arr,(2,1)))

print('')

       
print(np.tile(arr,(1,2)))

print('')
print(np.tile(arr,(3,2)))


```

    [[-0.77364227  1.18296869]
     [-0.45712094  0.94071693]
     [-0.77364227  1.18296869]
     [-0.45712094  0.94071693]]
    
    [[-0.77364227  1.18296869 -0.77364227  1.18296869]
     [-0.45712094  0.94071693 -0.45712094  0.94071693]]
    
    [[-0.77364227  1.18296869 -0.77364227  1.18296869]
     [-0.45712094  0.94071693 -0.45712094  0.94071693]
     [-0.77364227  1.18296869 -0.77364227  1.18296869]
     [-0.45712094  0.94071693 -0.45712094  0.94071693]
     [-0.77364227  1.18296869 -0.77364227  1.18296869]
     [-0.45712094  0.94071693 -0.45712094  0.94071693]]


### Meshgrid

NumPy arrays allow you to vectorize array expressions that might otherwise require writing loops (which Python is a lot slower at than C, Fortran, and Julia).   

One example of this is the ``np.meshgrid`` function, which takes two one-dimensional arrays and produces two two-dimensional matrices corresponding to all pairs of (x,y) in the two arrays.  

E.g.


```python

points=np.arange(-5,5,0.01)
xs,ys= np.meshgrid(points,points) #returns a two-element list of NumPy arrays

print(len(points),xs.shape,ys.shape)
```

    1000 (1000, 1000) (1000, 1000)


Here, both xs and ys are arrays of dimension(1000,1000).

The use of ``meshgrid`` is that it allows an easy evaluation of functions of x and y (i.e. f(x,y)).

### Array Broadcasting

Broadcasting refers to how arithmetic works between NumPy arrays of different shapes.  E.g. a vector array and a scalar.  


```python
arr=np.arange(5)

arr*4

```




    array([ 0,  4,  8, 12, 16])



Here, the array ``arr`` is not repeated four times but instead each element of the array is multiplied by a scalar value of 4.   We say that four is _broadcast_ to all of the array elements.   

For example, we can demean each column of an array by subtracting the column
means. In this case, it is very simple:


```python

arr = np.random.randn(4, 3)
print(arr)
print('')
print(arr.mean(0))
print('other way')
print(np.mean(arr,axis=0))
print('')
demeaned = arr - arr.mean(0)
print(demeaned)
print('')
print(demeaned.mean(0))
#array([-0., 0., -0.])

```

    [[-0.02130007 -1.0373789   2.4572157 ]
     [-0.59071767 -0.21009829  0.5146266 ]
     [-1.0156085  -0.37829766  0.87956382]
     [-0.90302399  0.77699065  1.3842623 ]]
    
    [-0.63266256 -0.21219605  1.3089171 ]
    other way
    [-0.63266256 -0.21219605  1.3089171 ]
    
    [[ 0.61136248 -0.82518285  1.1482986 ]
     [ 0.04194489  0.00209776 -0.79429051]
     [-0.38294594 -0.16610161 -0.42935328]
     [-0.27036143  0.9891867   0.07534519]]
    
    [2.77555756e-17 0.00000000e+00 2.77555756e-17]


Improper array broadcasting (or miscasting) is the source of many Python coding errors.   Which brings us to the broadcasting "rule":

_**Two arrays are compatible for broadcasting if for each trailing dimension (i.e., starting
from the end) the axis lengths match or if either of the lengths is 1. Broadcasting is
then performed over the missing or length 1 dimensions.**_

For example, for a (4,3) NumPy array and a (3,) array, the result is a (4,3) array where the (3,) array operates on each row of the first array.   For a (4,3) array and a (4,1) array, the result is a (4,3) array where the (4,1) array operates on every column.

Note that if you ask Python to do an impossible broadcast, you will get an error that looks something like this:

```
row_means=arr.mean(1)
arr-row_means
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ValueError: operands could not be broadcast together with shapes (4,3) (4,) 
```

However, reshaping the array can avoid a broadcasting error:


```python
#row_means=arr.mean(1)
row_means=np.mean(arr,axis=1)
print(row_means.shape)
arr-row_means.reshape(4,1)
```

    (4,)





    array([[-0.48747898, -1.50355781,  1.99103679],
           [-0.49532121, -0.11470184,  0.61002305],
           [-0.84416105, -0.20685021,  1.05101127],
           [-1.32243364,  0.357581  ,  0.96485264]])



A common problem, therefore, is needing to add a new axis with length 1 specifically
for broadcasting purposes. Using reshape is one option, but inserting an axis
requires constructing a tuple indicating the new shape. This can often be a tedious
exercise. Thus, NumPy arrays offer a special syntax for inserting new axes by indexing.
We use the special np.newaxis attribute along with “full” slices to insert the new
axis:


```python

arr=np.zeros((4,4))

arr_3d=arr[:,np.newaxis,:]
arr_3d.shape
#(4,1,4)

```




    (4, 1, 4)



Another example:


```python
arr_1d=np.random.normal(size=3)
print(arr_1d)
```

    [-1.11071556  1.76809613 -0.24458615]



```python
arr_1d[:,np.newaxis] #a column vector
```




    array([[-1.11071556],
           [ 1.76809613],
           [-0.24458615]])




```python
        
arr_1d[np.newaxis,:] #a row vector
```




    array([[-1.11071556,  1.76809613, -0.24458615]])



The same broadcasting rule governing arithmetic operations also applies to setting
values via array indexing. In a simple case, we can do things like:


```python

arr = np.zeros((4, 3))
arr[:] = 5
print(arr)


```

    [[5. 5. 5.]
     [5. 5. 5.]
     [5. 5. 5.]
     [5. 5. 5.]]


However, if we had a one-dimensional array of values we wanted to set into the columns
of the array, we can do that as long as the shape is compatible:


```python
 col = np.array([1.28, -0.42, 0.44, 1.6])
 print(col)
 arr[:] = col[:, np.newaxis]
 arr
 
```

    [ 1.28 -0.42  0.44  1.6 ]





    array([[ 1.28,  1.28,  1.28],
           [-0.42, -0.42, -0.42],
           [ 0.44,  0.44,  0.44],
           [ 1.6 ,  1.6 ,  1.6 ]])




```python
 arr[:2] = [[-1.37], [0.509]]
 arr
 
```




    array([[-1.37 , -1.37 , -1.37 ],
           [ 0.509,  0.509,  0.509],
           [ 0.44 ,  0.44 ,  0.44 ],
           [ 1.6  ,  1.6  ,  1.6  ]])



 Note, though that ``arr[:2] = [[-1.37, 0.509]]`` triggers a broadcasting error.
 

```
 Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ValueError: could not broadcast input array from shape (1,2) into shape (2,3)
```

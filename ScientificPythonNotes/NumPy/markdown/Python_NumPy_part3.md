# _Python for Scientific Data Analysis_

# NumPy/SciPy

## Section 3: Array Slicing and Reshaping

### Array Slicing

#### _Basic Slicing and Caveats_

We already covered array slicing in the **Data Structures** section.  But because this is so important, we will review what we said before.  We will also describe in more detail "boolean slicing".

Let's start with a NumPy array created from one of the functions described in the previous section: 


```python
import numpy as np

a = np.arange(10)

a
```




    array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])



This equals ``array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])``.  

And do some slicing.  


```python
print(a[4])
#a[4]=4 
print(a[3:7] )
```

    4
    [3 4 5 6]


We can also _redefine_ array elements from slicing.  

E.g.


```python
a[2:5]=12 
print(a)
```

    [ 0  1 12 12 12  5  6  7  8  9]


After that operation, ``a= array([ 0,  1, 12, 12, 12,  5,  6,  7,  8,  9])``.  As you can see, if you assign a scalar value to a slice, as in arr[2:5] = 12, the value is
propagated (or broadcasted henceforth) to the entire selection. An important first distinction
from Python’s built-in lists is that array slices are views on the original array.
This means that the data is not copied, and any modifications to the view will be
reflected in the source array.

To give an example of this, I first create a slice of arr:


```python
arr_slice=a[2:5]

#which equals ``array([12,12,12])
```

Now, when I change values in arr_slice, the mutations are reflected in the original
array arr: 


```python
arr_slice[1] = 12345
```

then ``a=array([    0,     1,    12, 12345,    12,     5,     6,     7,  8, 9])``.


```python
print(a)
```

    [    0     1    12 12345    12     5     6     7     8     9]


**CAUTION !!!** Now, this is a bit different than the form in other languages (e.g. IDL).   If you want a copy of a slice of an ndarray instead of a view, you will need to explicitly copy the array—for example, ``arr[2:5].copy()``.

#### _Higher Dimensional Slicing_

With higher dimensional arrays, you have many more options. In a two-dimensional
array, the elements at each index are no longer scalars but rather one-dimensional
arrays:


```python

arr2d = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
arr2d[2]


```




    array([7, 8, 9])



Thus, individual elements can be accessed recursively. But that is a bit too much
work, so you can pass a comma-separated list of indices to select individual elements.
So these are equivalent:


```python
#equivalent statements

print(arr2d[0][2])
print(arr2d[0,2])
#both equal 3


```

    3
    3


#### _Indexing with Slicing_

Another example shows how indexing is treated with slicing for NumPy arrays.


```python

arr2d = np.array([[1, 2, 3],[4, 5, 6],[7, 8, 9]])
#array([[1, 2, 3],
#[4, 5, 6]])
print(arr2d[0:2,:]) #select the first two rows of arr2d
print(arr2d[:2]) #same thing
```

    [[1 2 3]
     [4 5 6]]
    [[1 2 3]
     [4 5 6]]


As you can see, it has sliced along axis 0, the first axis. A slice, therefore, selects a
range of elements along an axis. It can be helpful to read the expression arr2d[:2] as
“select the first two rows of arr2d.”

You can pass multiple slices just like you can pass multiple indexes:

``arr2d[:2, 1:]`` equals ``array([[2, 3],
[5, 6]])``.  

When slicing like this, you always obtain array views of the same number of dimensions.
By mixing integer indexes and slices, you get lower dimensional slices.
For example, I can select the second row but only the first two columns like so:
``arr2d[1, :2]`` equals ``array([4, 5])``.  

Similarly, I can select the third column but only the first two rows like so:
``arr2d[:2, 2]`` equals ``array([3, 6])``.  

Note that a colon by itself means to take the entire
axis, so you can slice just the higher dimensional axes (i.e. slice on columns) as shown below


```python
arr2d[:,:1] #all rows, first column

```




    array([[1],
           [4],
           [7]])



assigning to a slice expression assigns to the whole selection:

e.g. ``arr2d[:2, 1:] = 0``


```python
arr2d[:2,1:] = 0

arr2d
```




    array([[1, 0, 0],
           [4, 0, 0],
           [7, 8, 9]])



#### _Slicing with Boolean Indexing_

##### _One Way_

Let’s consider an example where we have some data in a NumPy array and an array of names
with duplicates. We use the randn function in ``numpy.random`` to generate
some random normally distributed data:


```python

names = np.array(['Bob', 'Joe', 'Will', 'Bob', 'Will', 'Joe', 'Joe'])
data = np.random.randn(7,4)

print(data)
```

    [[-0.95490244 -0.1914647  -0.95327315  0.92027643]
     [-0.17037324 -0.68519543  1.0956573  -0.65449562]
     [ 0.77865508  1.12470135  1.74984846 -0.86348672]
     [ 0.45095936 -0.27173829  0.74643123  1.08588898]
     [ 0.97830604  0.11268757 -0.14456917 -1.28356505]
     [-0.13735323 -0.40996842  1.22489976  0.51266261]
     [ 0.90775459  1.55065173 -0.980306   -1.4167332 ]]


Suppose each name corresponds to a row in the data array and we wanted to select
all the rows with corresponding name 'Bob'. Like arithmetic operations, comparisons
(such as ==) with arrays are also vectorized. Thus, comparing names with the
string 'Bob' yields a boolean array:


```python
#``names == 'Bob'; array([ True, False, False,  True, False, False, False])``

names == 'Bob'
#nn=np.where(names == 'Bob')
```




    array([ True, False, False,  True, False, False, False])



This boolean array can be passed when indexing the array:


```python
data[names == 'Bob']
```




    array([[-0.95490244, -0.1914647 , -0.95327315,  0.92027643],
           [ 0.45095936, -0.27173829,  0.74643123,  1.08588898]])



Note: the boolean array must be of the same length as the array axis it’s indexing. 

In these examples, I select from the rows where names == 'Bob' and index the columns,
too:


```python

print(data[names == 'Bob', 2:])

       
print(data[names == 'Bob', 3])



```

    [[-0.95327315  0.92027643]
     [ 0.74643123  1.08588898]]
    [0.92027643 1.08588898]


To select everything but 'Bob' for column 2, you can either use != or negate the condition using ``~``: e.g. ``data[names != 'Bob', 2:]`` or ``data[~(names == 'Bob'),2:]``.


```python
noBob=data[names != 'Bob',2:]
goawayBob = data[~(names == 'Bob'),2:]

print(noBob)
print(goawayBob)
```

    [[ 1.0956573  -0.65449562]
     [ 1.74984846 -0.86348672]
     [-0.14456917 -1.28356505]
     [ 1.22489976  0.51266261]
     [-0.980306   -1.4167332 ]]
    [[ 1.0956573  -0.65449562]
     [ 1.74984846 -0.86348672]
     [-0.14456917 -1.28356505]
     [ 1.22489976  0.51266261]
     [-0.980306   -1.4167332 ]]


Selecting two of the three names to combine multiple boolean conditions, use
boolean arithmetic operators like ``&`` (and) and ``|`` (or):


```python
mask = (names == 'Bob') | (names == 'Will')
#data[mask]

data[mask]
#mask
```




    array([[-0.95490244, -0.1914647 , -0.95327315,  0.92027643],
           [ 0.77865508,  1.12470135,  1.74984846, -0.86348672],
           [ 0.45095936, -0.27173829,  0.74643123,  1.08588898],
           [ 0.97830604,  0.11268757, -0.14456917, -1.28356505]])



Setting values with boolean arrays works in a common-sense way. To set all of the
negative values in data to 0 we need only do:


```python
print(data)
data2=data.copy()
data2[data<0]=0
print('')
print(data2)
```

    [[-0.95490244 -0.1914647  -0.95327315  0.92027643]
     [-0.17037324 -0.68519543  1.0956573  -0.65449562]
     [ 0.77865508  1.12470135  1.74984846 -0.86348672]
     [ 0.45095936 -0.27173829  0.74643123  1.08588898]
     [ 0.97830604  0.11268757 -0.14456917 -1.28356505]
     [-0.13735323 -0.40996842  1.22489976  0.51266261]
     [ 0.90775459  1.55065173 -0.980306   -1.4167332 ]]
    
    [[0.         0.         0.         0.92027643]
     [0.         0.         1.0956573  0.        ]
     [0.77865508 1.12470135 1.74984846 0.        ]
     [0.45095936 0.         0.74643123 1.08588898]
     [0.97830604 0.11268757 0.         0.        ]
     [0.         0.         1.22489976 0.51266261]
     [0.90775459 1.55065173 0.         0.        ]]


Setting whole rows or columns using a one-dimensional boolean array is also easy:


```python
data[names != 'Joe']
```




    array([[-0.95490244, -0.1914647 , -0.95327315,  0.92027643],
           [ 0.77865508,  1.12470135,  1.74984846, -0.86348672],
           [ 0.45095936, -0.27173829,  0.74643123,  1.08588898],
           [ 0.97830604,  0.11268757, -0.14456917, -1.28356505]])



##### _Boolean Slicing with np.where_

Another way to do very complex slicing is with the ``where`` function (e.g. ``np.where[set of boolean conditions]``).   E.g. you can write the previous slicing as:


```python
#let's go back to our original data array...
data3=data.copy()
print(data)
bad=np.where(names != 'Joe')
data3[bad]=7
data3
```

    [[-0.95490244 -0.1914647  -0.95327315  0.92027643]
     [-0.17037324 -0.68519543  1.0956573  -0.65449562]
     [ 0.77865508  1.12470135  1.74984846 -0.86348672]
     [ 0.45095936 -0.27173829  0.74643123  1.08588898]
     [ 0.97830604  0.11268757 -0.14456917 -1.28356505]
     [-0.13735323 -0.40996842  1.22489976  0.51266261]
     [ 0.90775459  1.55065173 -0.980306   -1.4167332 ]]





    array([[ 7.        ,  7.        ,  7.        ,  7.        ],
           [-0.17037324, -0.68519543,  1.0956573 , -0.65449562],
           [ 7.        ,  7.        ,  7.        ,  7.        ],
           [ 7.        ,  7.        ,  7.        ,  7.        ],
           [ 7.        ,  7.        ,  7.        ,  7.        ],
           [-0.13735323, -0.40996842,  1.22489976,  0.51266261],
           [ 0.90775459,  1.55065173, -0.980306  , -1.4167332 ]])



The ``where`` function allows for highly complex slicing.   E.g.


```python
data4=data.copy()
data4
```




    array([[-0.95490244, -0.1914647 , -0.95327315,  0.92027643],
           [-0.17037324, -0.68519543,  1.0956573 , -0.65449562],
           [ 0.77865508,  1.12470135,  1.74984846, -0.86348672],
           [ 0.45095936, -0.27173829,  0.74643123,  1.08588898],
           [ 0.97830604,  0.11268757, -0.14456917, -1.28356505],
           [-0.13735323, -0.40996842,  1.22489976,  0.51266261],
           [ 0.90775459,  1.55065173, -0.980306  , -1.4167332 ]])




```python
bad=np.where( (names == 'Will') | ( (data4[:,0] > 0) & (names == 'Bob')))
data4[bad]=9
data4
print(data[:,0])
print(data4[:,0])
```

    [-0.95490244 -0.17037324  0.77865508  0.45095936  0.97830604 -0.13735323
      0.90775459]
    [-0.95490244 -0.17037324  9.          9.          9.         -0.13735323
      0.90775459]


##### _Expressing Conditional Logic as Array Operations with np.where_

Where can do even more complex operations.  Essentially it is a vectorized version of the ternary expression ``x if condition else y``.   Before, we were just using it as ``x if condition`` just to find indexes of an array.   Now we can use it to do more complex operations.

E.g. say we have two arrays of values and a boolean array:


```python

xarr = np.array([1.1, 1.2, 1.3, 1.4, 1.5])
yarr = np.array([2.1, 2.2, 2.3, 2.4, 2.5])
cond = np.array([True, False, True, True, False])


```

Suppose we wanted to take a value from xarr whenever the corresponding value in
cond is True, and otherwise take the value from yarr. A list comprehension doing
this might look like:

```
result = [(x if c else y)
 for x, y, c in zip(xarr, yarr, cond)]

```

For our simple example, this is fine but it is slow for large arrays and hard to pull off for multi-dimensional arrays.  ``np.where`` is the solution:


```python
result = np.where(cond, xarr, yarr)
#array([ 1.1, 2.2, 1.3, 1.4, 2.5])
result
```




    array([1.1, 2.2, 1.3, 1.4, 2.5])



Another example:


```python
data3=data.copy()
good=data3 > 0
data3c=np.where(good,data3,-1*data3)
print(data3)
print('')
print(data3c)
print('')


```

    [[-0.95490244 -0.1914647  -0.95327315  0.92027643]
     [-0.17037324 -0.68519543  1.0956573  -0.65449562]
     [ 0.77865508  1.12470135  1.74984846 -0.86348672]
     [ 0.45095936 -0.27173829  0.74643123  1.08588898]
     [ 0.97830604  0.11268757 -0.14456917 -1.28356505]
     [-0.13735323 -0.40996842  1.22489976  0.51266261]
     [ 0.90775459  1.55065173 -0.980306   -1.4167332 ]]
    
    [[0.95490244 0.1914647  0.95327315 0.92027643]
     [0.17037324 0.68519543 1.0956573  0.65449562]
     [0.77865508 1.12470135 1.74984846 0.86348672]
     [0.45095936 0.27173829 0.74643123 1.08588898]
     [0.97830604 0.11268757 0.14456917 1.28356505]
     [0.13735323 0.40996842 1.22489976 0.51266261]
     [0.90775459 1.55065173 0.980306   1.4167332 ]]
    
    [[0.95490244 0.1914647  0.95327315 0.92027643]
     [0.17037324 0.68519543 1.0956573  0.65449562]
     [0.77865508 1.12470135 1.74984846 0.86348672]
     [0.45095936 0.27173829 0.74643123 1.08588898]
     [0.97830604 0.11268757 0.14456917 1.28356505]
     [0.13735323 0.40996842 1.22489976 0.51266261]
     [0.90775459 1.55065173 0.980306   1.4167332 ]]


### Array Shapes and Reshaping

NumPy arrays have given dimensions: the ``shape`` of a NumPy array distinguishes vectors or matrices of different sizes.   The attribute ``.shape`` for a NumPy array returns its dimensionality in the form of a tuple of its dimensions.   

E.g. for the matrix ``a=np.array([[3,4,5],[6,7,8]])`` the shape can be returned from ``a.shape #yields (2,3)``. 


```python
a=np.array([[3,4,5],[6,7,8]])

print(a.shape)

print(a.shape[0]) #how many rows?
print(a.shape[1]) #how many columns?

```

    (2, 3)
    2
    3


A vector returns ``([number],)``: e.g. ``a=np.array([3,4,5,6,7,8])`` returns as ``a.shape #(6,)``.


```python
a=np.array([3,4,5,6,7,8])
print(a.shape)

```

    (6,)


#### _reshape_

We can give a view of the array where we change the dimensions of the array while keeping the same number of elements with the ``.reshape`` function.

E.g. for ``arr=np.array([8,6,7,5,3,0])`` we can reshape it as ``arr.reshape(2,3)``, which returns ``array([[8, 6, 7],[5, 3, 0]])``.  
       


```python
arr=np.array([8,6,7,5,3,0]) # a vector
arr.reshape(2,3) #reshaped into a 2D array
```




    array([[8, 6, 7],
           [5, 3, 0]])



       Figure 4.2 in Fuhrer gives a nice overview of what happens when you ``reshape`` an array different ways.   E.g. for ``arr`` in the above example, we get the following results from different reshapings:
       


```python
arr=np.array([8,6,7,5,3,0])

arr.reshape(1,6)
#yields array([[8, 6, 7, 5, 3, 0]]) ... i.e. the same as before
```




    array([[8, 6, 7, 5, 3, 0]])




```python
arr.reshape(6,1)
#yields a column matrix
#array([[8],
#       [6],
#       [7],
#       [5],
#       [3],
#       [0]])
```




    array([[8],
           [6],
           [7],
           [5],
           [3],
           [0]])




```python
arr.reshape(2,3)
#yields 
#array([[8, 6, 7],
#       [5, 3, 0]])
```




    array([[8, 6, 7],
           [5, 3, 0]])




```python
arr.reshape(3,2)
#yields
#array([[8, 6],
#       [7, 5],
#       [3, 0]])    
```




    array([[8, 6],
           [7, 5],
           [3, 0]])



Now say you have an array of some dimensions and you want to reshape it so it has, say, two columns and "some" number of rows but that you don't know the number of rows beforehand, or vice versa.   I.e. you specify one shape but want Python to specify (er, _compute_) the other one.  You can let Python determine this by setting the second parameter to ``-1``.   E.g. 


```python
v=np.array([1,2,3,4,5,6,7,8])
M=v.reshape(2,-1)
M.shape
#returns (2,4)
```




    (2, 4)




```python
M=v.reshape(-1,2)
M.shape
#returns (4,2)
```




    (4, 2)



#### _Transpose_

A special form of reshaping used often in linear algebra is _**transposing**_, which shwithces the two shape elements of the matrix (e.g. columns--> rows; rows--> columns).    The transpose of a matrix _**A**_ is a matrix _**B**_ such that:
_B <sub>ij</sub>_ = _B <sub>ji</sub>_ .

The simplest to do a transpose with a NumPy array is ...  ``array.T``, e.g. for a matrix A, the transpose B is ``B= A.T``.   An alternative way is with the ``np.transpose()`` operation: e.g. ``B=np.transpose(A)``.

Note that transposing just returns a view of the array: it does not copy.

Array transposing becomes very useful later when we try to do matrix operations.   E.g. when computing the inner matrix product using ``np.dot``:


```python
a=np.array([[1,2,3],[4,5,6],[7,8,9],[10,11,12]])
print(a.shape)
```

    (4, 3)



```python
result1=np.dot(a,a.T)
print(result1)

result1.shape
#(4,4)
```

    [[ 14  32  50  68]
     [ 32  77 122 167]
     [ 50 122 194 266]
     [ 68 167 266 365]]





    (4, 4)




```python
result2=np.dot(a.T,a)
print(result2)

result2.shape
#(3, 3)

 
```

    [[166 188 210]
     [188 214 240]
     [210 240 270]]





    (3, 3)



#### _flatten_ and _ravel_

With ``reshape`` we have found a way to convert a 1-D vector into 2-D matrix: i.e. reshape-ing an array to a higher dimension.  We can also do the opposite -- converting a 2+D array into a 1-D vector -- using the ``flatten`` or ``ravel`` function.   These two functions largely do the same thing (as described above).  

There are some key differences between these two, mainly on that ``flatten`` returns a copy of an array while ``ravel`` returns a view: these are described in more detail [here](https://www.naukri.com/code360/library/difference-between-flatten-and-ravel-functions-in-numpy) [what's the difference between a copy and a view? see [here](https://www.w3schools.com/python/numpy/numpy_copy_vs_view.asp) .

Here are examples of ``flatten`` and ``ravel`` in action:


```python

arr = np.arange(15).reshape((5, 3))
arr
#array([[ 0, 1, 2],
#[ 3, 4, 5],
#[ 6, 7, 8],
#[ 9, 10, 11],
#[12, 13, 14]])

print(arr.flatten())
#array([ 0,  1,  2,  3,  4,  5,  6,  7,  8,  9, 10, 11, 12, 13, 14])
print(arr)
print(arr.ravel())
#array([ 0,  1,  2,  3,  4,  5,  6,  7,  8,  9, 10, 11, 12, 13, 14])

print(arr)
```

    [ 0  1  2  3  4  5  6  7  8  9 10 11 12 13 14]
    [[ 0  1  2]
     [ 3  4  5]
     [ 6  7  8]
     [ 9 10 11]
     [12 13 14]]
    [ 0  1  2  3  4  5  6  7  8  9 10 11 12 13 14]
    [[ 0  1  2]
     [ 3  4  5]
     [ 6  7  8]
     [ 9 10 11]
     [12 13 14]]


A short caveat ... Note that data can be reshaped or raveled in different orders.   One order is "row-major" order, where values within each row of data are stored in adjacent memory locations (you traverse higher dimensions first).  The alternative to row major ordering is column major
order, which means that values within each column of data are stored in adjacent
memory locations (you traverse higher dimensions last).   "Row major" order is traditionally known as "C order" and "column major" order is traditionally known as "Fortran order".  

By default, NumPy arrays are created in _row major_ order.  But both ``ravel`` and ``flatten`` have an order keyword that allows you to switch to _column major_ order.   E.g.


```python

arr = np.arange(12).reshape((3, 4))
arr
#array([[ 0, 1, 2, 3],
#[ 4, 5, 6, 7],
#[ 8, 9, 10, 11]])
```




    array([[ 0,  1,  2,  3],
           [ 4,  5,  6,  7],
           [ 8,  9, 10, 11]])




```python
print(arr.ravel()) #default ordering
#array([ 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11])

print(arr.ravel('F'))
#array([ 0, 4, 8, 1, 5, 9, 2, 6, 10, 3, 7, 11])

```

    [ 0  1  2  3  4  5  6  7  8  9 10 11]
    [ 0  4  8  1  5  9  2  6 10  3  7 11]


### The Axis Keyword

Before proceeding to the next section, it's worth highlighting a particularly important keyword for many NumPy functions, since it crops up everwhere: ``axis``.   Usually this is invoked as ``np.[functionname](array,axis=[some number])``.   Basically it means "apply the vectorized NumPy function only along a given axis instead of for the array as a whole"

You will immediately see that this is extremely powerful.   

For example...


```python

arr = np.random.randn(5, 4)
print(arr)
print('the shape is ',arr.shape)
print('')
arr2=np.sum(arr)
print('')
print(arr2)
print('')
arr2=np.sum(arr,axis=0)
print(arr2)

print('')
arr2=np.sum(arr,axis=1)
print(arr2)


```

    [[ 0.49814033  0.40455304  1.19489358  0.73568257]
     [ 0.02384146  0.46080824  0.76953115 -0.03552168]
     [ 1.13934394  1.28586223  1.62328899 -1.09341034]
     [ 0.40183207  1.92525277  0.82317276  1.62423224]
     [-1.6883183  -1.234848    0.08197712 -0.58906142]]
    the shape is  (5, 4)
    
    
    8.351252736350375
    
    [0.37483949 2.84162828 4.4928636  0.64192136]
    
    [ 2.83326951  1.21865916  2.95508482  4.77448984 -3.4302506 ]


In this case, for "axis=0", NumPy performs a sum over _each row in a column_.  Since there are 4 columns, the shape and len of the resulting array ``arr2`` is (4,) and 4, respectively.   For "axis=1", NumPy performs a sum over _each column in a row_.   

Here's another example with the same array


```python

arr = np.random.randn(5, 4)
print(arr)

arr2=np.median(arr)
print(arr2)

arr2=np.median(arr,axis=0)
print(arr2)

arr2=np.median(arr,axis=1)
print(arr2)


```

    [[ 0.29552596  0.38818689  0.35051761  0.10367164]
     [ 1.90169647  0.74523103  0.71771212 -1.65561412]
     [-0.29832033 -0.7672148  -1.91305586 -0.47338039]
     [-1.41963564  1.07743676  0.45743791  0.49610772]
     [-0.60517634  0.28312329 -1.17911145  0.39466925]]
    0.28932462756285043
    [-0.29832033  0.38818689  0.35051761  0.10367164]
    [ 0.32302178  0.73147157 -0.6202976   0.47677282 -0.16102652]


You can also call combinations of axes: e.g. ``np.median(array,axis=[0,1])``.


```python

```

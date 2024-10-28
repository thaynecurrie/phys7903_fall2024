# _Python for Scientific Data Analysis_

## Homework - Week 10 (Due Nov 1)


### 1. Simple Matplotlib Plotting

* read in ``file.txt``
* use SciPy's ``curve_fit`` function
* plot the best-fit function as an orange dash-dotted line
* overplot the original data with green cross symbols
* Label ``X`` and ``Y`` in size 14 font.

### 2. Customized Matplotlib Plotting

* read in ``compilation.txt`` 
* reproduce the following plot


 ![](./cmd.png)
 
 * note: the array slicing is a little bit tricky (ideally you want a vectorized string operation with wildcards).  Here's a simple version:

```
lowg=np.where( ( flag == 'lowg') | (flag == 'young') | (flag == 'lowg,young') | (flag == 'ABDor,lowg,young')
              | (flag == 'Argus,lowg,young') | (flag == 'Columba,lowg,young') | (flag == 'TWA,lowg,young')
              | (flag == 'ScoCen,young')                                 
              | (flag == 'TucHor,young') | (flag=='Tuc-Hor,lowg,young') | (flag == 'plx-discrep,lowg') )
```

* note: the problem will require you to inspect the file to see the column headers.

* note: to convert from apparent to absolute magnitude ...
 $abs_{\rm mag}$ = $app_{\rm mag}$-5*log$_{\rm 10}$(distance/10 $pc$).    And the distance is related to the parallax as:
 $distance (pc) = 1 /parallax$. 
 
 i.e. To go from apparent magnitude to absolute magnitude (e.g. J to $M_{\rm J}$) do:
 
 $M_{\rm J}$ = J - 5*np.log10(1e2/parallax)
 
 **Hint** -  The column notation is tricky.  The columns for J, error in J, H, and error in H are:
 
 J = column 27
 eJ = column 28
 H = column 30
 eH = column 31
 
### 3. Multi-Panel Plots

From the same data as above, produce the following plot (you will have to read in J, H, K and L photometry and errors).

**Hint** -  the convention for the columns is the same as in problem 2:

  (i.e. K and L are columns 33 and 36, respectively)

**EXTRA CREDIT (one point)** -- instead of individually indexing values for the plotted variables and labels, do this in a for-loop with the x,y data points and labels all saved to variables outside of the loop.

![](./prob4.png)


### 4. Formatted Error Bar Plots

Start with the file ``test3.csv`` similar to (but not exactly the same as!) that from the Week 4 homework.  As a reminder, the first row in this table is a list of column headers.   

* Plot the radius (in Jupiter radii) vs semimajor axis for all planets detected by the transit method, including errors in the radius and and semimajor axis (examine the file headers to see which one to use).

* use a log scale for the y axis ``plt.yscale('log')``

Reproduce the output as follows:

![](./transit_plot.png)



### 5. Project Update

* Please give me a (**short**) update on the progress of your class project.  In particular, I would like to see ...

- A finalized short summary of what you are doing
- A list of code packages you plan to use or type of code you plan to write
- A description of the current status of your project
- Items where you are getting stuck (if any)/questions you may have
- Any plots or graphics you have produced.
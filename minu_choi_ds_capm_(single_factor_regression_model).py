# -*- coding: utf-8 -*-
"""Minu Choi DS - CAPM (single-factor regression model)

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1-xifbw9Pf3GcPuWXYsPcbPKgert5qhJB

### Background

In finance, CAPM is a single-factor regression model used for analyzing (and predicting) excess stock returns. There are better, more accurate models, but it has its uses. For example, the *market beta* is a useful output which has something to do with the risk of particular investments.

The main formula will look like this:

\begin{aligned}
E(R_A) = R_f + \beta_A (E(R_{SP}) - R_f)
\end{aligned}

Some notes on the symbols in this formula:
- The formula is used to estimate $E(R_A)$.  The $E$ here stands for the expected value, and $R_A$ is the rate of return of the investment $A$.
- To use this formula, you therefore need to know the values of the other variables.
- The variable $R_f$ is the "risk-free rate," which is the amount of return you can get on an investment that has zero risk, like say a bank account.
This quantity changes over time but for our purposes we can treat it as a constant.  It is hard-coded into the code below.  Make sure you see where this variable occurs in the formula above.
- In this assignment the variable $R_{SP}$ is a measure of the rate of return of the overall market.  (The $E$ on the right side also means expected value.)
- The variable $\beta_A$ measures something about the relative risk of the investment A, relative to the overall market.  The technical objective of this assignment will be to compute $\beta_A$ below, and then to examine how sensitive it is to the specific data.
- The value you get for $\beta_A$ will be a number.  If it is greater than 1, it means (*very roughly*) that the investment A is more volatile than the overall market.  If it is less than 1, it means that the investment is less volatile than the overall market.  But **do not take this too seriously!** In particular see all the caveats at the wikipedia page.
- The A investment in our example is an individual stock (Apple).

2.  Load the packages and data.  (Note that the following code chunk also hard-codes the constant $R_f$.)  
The data lives in the file `capm_market_data` in the `data` folder on the `GitHub` site.
"""

# load numpy and pandas packages
import numpy as np
import pandas as pd

# get data
data = pd.read_csv("capm_market_data.csv")
print(data)

# risk-free Treasury rate
R_f = 0.0175 / 252

"""3.  Look at some records.  
SPY is something that mirrors the S&P 500 ("the market").  
AAPL is the code for Apple stock.  
The values are closing prices, adjusted for splits and dividends.
"""

data.info()
data.describe()

"""4.  Drop the date column"""

data = data.drop(columns='date')

"""5.  Compute daily returns (percentage changes in price) for both SPY and AAPL.
(Be sure to drop the first row of NaN.)  
Hint: pandas has functions to easily do this.  
Print the first 5 rows of returns.

"""

daily_returns = data.pct_change().dropna() * 100

daily_returns.head(n=5)

"""6.  Save the SPY and AAPL returns into separate numpy arrays.  
Print the first five values from each of the two arrays.

"""

spy_array = daily_returns['spy_adj_close'].to_numpy()
aapl_array = daily_returns['aapl_adj_close'].to_numpy()

print(f"First five values of spy_returns array: {spy_array[:5]}")
print(f"First five values of aapl_returns array: {aapl_array[:5]}")

"""7.  Make arrays (one for SPY, one for AAPL) containing the *excess* returns by subtracting the constant $R_f$ from the returns.  
(Recall that $R_f$ is the "risk-free rate" meaning essentially that you could earn this much in interest if you didn't invest in anything.)  
Print the LAST five excess returns from both SPY and AAPL numpy arrays.
"""

# Given at the introduction of this assignemnt
R_f = 0.0175 / 252

spy_excess_array = spy_array - R_f
aapl_excess_array = aapl_array - R_f

spy_last_five_excess = spy_excess_array[-5:]
aapl_last_five_excess = aapl_excess_array[-5:]

print(spy_last_five_excess, aapl_last_five_excess)

"""8. Make a scatterplot with SPY excess returns on the $x$-axis and AAPL excess returns on the $y$-axis.  
If you need it, here is the [Matplotlib documentation]( https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.scatter.html).
"""

import matplotlib.pyplot as plt

plt.figure(figsize=(10, 5))
plt.scatter(spy_excess_array, aapl_excess_array, color='green')
plt.title('SPY Excess Returns vs AAPL Excess Returns')
plt.xlabel('SPY Excess Returns')
plt.ylabel('AAPL Excess Returns')
plt.show()

"""The value of $\beta_A$ is computed from the arrays you built in problem 7, via a formula that uses some statistical functions called the "variance" and the "covariance."

Any individual 1-d array of numbers has a variance, which you can compute using `numpy`'s function `var()` (documented [here](https://numpy.org/doc/stable/reference/generated/numpy.var.html)).  This is a number.

If you have two 1-d arrays of the same length, they collectively have something called a covariance which `numpy` also can compute using `cov()` (documented [here](https://numpy.org/doc/stable/reference/generated/numpy.cov.html)).

The covariance is also a number, but look at what happens when you send two 1-d arrays to `cov()`: it returns a $2\times 2$ matrix.  (Try it!)  The covariance we are looking for is the number that lives in both the top right and the bottom left of this matrix.  (Those two numbers should be the same.)  The top left and bottom right entries of the covariance matrix also have meaning, but we don't need them.

9. Use `numpy` functions as described above to compute the estimate of $\beta_A$, using the following formula:  
\begin{aligned} \beta_A= \frac{ \text{cov}(A,SP) }{ \text{var}(SP) } \end{aligned}
In our context, A will be the 1-d array you made in problem 7 for AAPL, and SP will be the 1-d array you made for SPY.
"""

cov_a_sp = np.cov(aapl_excess_array, spy_excess_array)

var_sp = np.var(spy_excess_array)

beta_a = cov_a_sp / var_sp

print(beta_a) # 1.09561726 is the output that we are interested in.

# As it is explained above in question 9, this returns a 2 x 2 matrix.
# However, given that the number in both the top right and the bottom left is
# the covariance we desire, the top left and bottom right entries are not needed.

"""You should have found that the beta estimate is greater than one.  
This means that the volatility of AAPL stock, given the data, and according to this particular (flawed) model,
is higher than the volatility of the S&P 500.

Bonus:  Is this something you can see on the plot you made?


"""

# BONUS QUESTION RESPONSE
# In terms of the plot I made, the beta_a depicts the slope of the best-fit line
# through the scatterplot of the excess returns. A beta greater than one indicates
# that the volatility of AAPL stock is higher than the volataility of the S&P 500.

"""Finally, let's look at how sensitive the beta is to each data point.   
We want to drop each data point (one at a time), compute \\(\hat\beta_i\\) using our formula from above, and save each measurement.

This is called *jackknifing*.

10. Write a function called `beta_sensitivity()` with these specs:

- take numpy arrays `x` and `y` as inputs
- outputs a list of tuples, so that each tuple contains (observation row dropped, beta estimate)

Hint: **np.delete(x, i).reshape(-1,1)** will delete observation i from array x, and make it a column vector
"""

def beta_sensitivity(x, y):
  beta = []
  for i in range(len(x)):
    x_beta = np.delete(x, i).reshape(-1, 1)
    y_beta = np.delete(y, i).reshape(-1, 1)
    var_x = np.var(x_beta)
    cov_xy = np.cov(y_beta.T, x_beta.T)[0, 1]
    # .T is used to converts columns into rows. This was to consistently adhere to the 2D format.
    beta_sample = cov_xy / var_x
    beta.append((i, beta_sample))
  return beta

"""11. Call `beta_sensitivity()` on the arrays A and SP from earlier and print the first ten tuples of output."""

beta_tuples = beta_sensitivity(spy_excess_array, aapl_excess_array)
print(beta_tuples[:10])
#CS/ML

# Losses, Regularizers, and Optimizers

[toc]

[Wiki](https://en.wikipedia.org/wiki/Loss_function): *In mathematical optimization and decision theory, a loss function or a cost function is a function that maps an event or values of one or more variables onto a real number intuitively representing some "cost" associated with the event.*

* In a regression(optimization) problem, we try to describe the event with a family of (multidimensional) surfaces, and the optimal surface is the one has least loss.
* In a classification(decision) problem, our target is minimizing the prediction inaccuracy or minimizing the cost of mis-identification. See also [wiki: Loss functions for classification](https://en.wikipedia.org/wiki/Loss_functions_for_classification)

## Some suggestions from PRML

# Losses

## For regression problem

How to choose a model? In most cast we follow AIC or BIC.

### Minkovski loss

As given by [wiki: Norm](https://en.wikipedia.org/wiki/Norm_(mathematics))

#### L2 norm

* Also known as *linear regression*, *Mean-Square Error(MSE)*
* The optimal point is the mean(平均數).

#### L1 norm

* Also known as *Mean-Absolute Error(MAE)*.
* The optimal point is the median(中位數).
* To save RAM: [稀疏化](https://developers.google.com/machine-learning/crash-course/regularization-for-sparsity/l1-regularization)

#### L0 norm

* Not really 0, but approach to 0.
* Optimal point is the mode(眾數)

## For classification problem

The inaccuracy of 

### Minkovski loss

Similar to the case for regression problem. But geometrically, it describes *how exact the discriminant distinguish classes*, when we take L0 norm, there no room for ambiguous event. 

### Logistic Regression: softmax

#### Special case: Binary logistic equation
#### Special case: log softmax

### Hinge loss

### Entropy-based loss

#### Special case: binary cross entropy

[A simple derivation of the formula](https://www.youtube.com/watch?v=hSXFuypLukA)

* Q: Why don't we take just square error?  
    A: When the target parameter is away from the optimal point, the calculated gradient is way larger with cross entropy than that with L2

# Regularizers

Key idea is **a trade off between performance in training and performance in
generalization.** 

* **It can be derived intuitively in Bayesian view from prior.** The L2 regulator comes from to the orthonormal Gaussian fluctuation assumption of each parameters as the prior. This is explicitly shown in *PRML 2/e* `Eqn.(1.65)`~`Eqn.(1.67)`

## For classification problem

### Entropy-based regularization

Used in semi-supervised training.

## For regression problem

# Optimizers

Optimizers describes how we update parameters for loss function. Techniques are used to prevent from falling into local minimum, improve learning procedure, etc.. 

An introduction can be found in [this lecture](https://www.youtube.com/watch?v=xki61j7z-30)

* Training: ReLU, Max-out, RMSProp + Momentum = Adam.
* Testing: Early stopping, Regularization, Dropout.

## Boosting

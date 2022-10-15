#CS/DSA/ML 

# ScikitLearn

* https://scikit-learn.org/stable/user_guide.html
This note is based on [PRML/2e by Bishop](https://dl.acm.org/doi/book/10.5555/1162264).

# Regression problem

# Classification problem

* https://en.wikipedia.org/wiki/Model_selection

## Inference and decision making

A classification could be separated into two stages: *Inference stage* and *Decision stage*, but this is not always followed. We could also achieve the classification goal in a single step.

The target problem of interest can be expressed in the form $$p(\mathcal{C}_k| x) = \frac{p(x|\mathcal{C}_k)p(\mathcal{C}_k)}{p(x)}$$ where $\mathcal{C}_{k}$ is the class and $x$ is the data.

#CS/ML 

Preprocessing can be useful to reduce correlations among the variables, to transform their shapes into more appropriate forms, or to accelerate the response time of a method (event sorting).

## Normalization

Linearly scale the minimum to maximum values for the variable to $[-1, 1]$.

* Pros
    * Useful to allow direct comparison between the MVA weights assigned to the variables, where a large weight may indicate strong separation power.

* Use case

## De-correlation

Consider the real symmetric correlation matrix $C$, it can be diagonalised to be $C = SDS^{T}$, where $D$ is diagonal.
With the help of $S$, the variables are decorrelated.

* Pros:
    * Less performance loss in some classification algorithm which ignores correlations among the discriminating input variables. 
      In most realistic use case this is not an accurate conjecture.
* Remark:
    * For highly nonlinear problems the performance may even become worse. Nonlinear methods without prior variable decorrelation should be used in such cases.

## Principle component decomposition
Nothing more than dropping information along least data-describing eigenvector.

## [Feature scaling](https://en.wikipedia.org/wiki/Feature_scaling)

This process includes not just scaling but also *standarization* to $\mu=0$ and $\sigma = 1$. If the scale of individual input values in raw data varies widely, then in some algorithms, loss functions will not work properly. For example, in gradient descent method, the parameters of interest will be dominated by input value with way larger scale than others.

## Uniform-ization

## Gaussian-ization

## Data Augmentation 資料增強

When there is no sufficient input data, we generate more data from existing data. This is usually useful for automatic feature engineering, such as convolutional NN for graphics.

Example could be seen/produced with [`imgaug`](https://github.com/aleju/imgaug) module.

----
# Technical issues

## General

* For sequential reading, a good randomness could be achieved take reasonable buffer size and shuffle in such buffer. See [discussion on `tensorflow.data.Dataset.shuffle`](https://stackoverflow.com/questions/46444018/meaning-of-buffer-size-in-dataset-map-dataset-prefetch-and-dataset-shuffle)

## Scikit-learn

See `sklearn.preprocessing` in [scikit-learn](mweblib://15835468465195)

----
# Reference

* [TMVA Users Guide](https://github.com/root-project/root/blob/master/documentation/tmva/UsersGuide/TMVAUsersGuide.pdf)
* https://scikit-learn.org/stable/modules/preprocessing.html



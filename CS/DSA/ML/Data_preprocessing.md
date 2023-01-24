#CS/DSA/ML 

Preprocessing can be useful to reduce correlations among the variables, to transform their shapes into more appropriate forms, or to accelerate the response time of a method (event sorting).

# Transformations

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
# Performance issues

* [如何在pandas中有效節省記憶體，把資料縮小90%. | by Yung-Hui Hsu | Medium](https://medium.com/@YungHui_Med/%E8%BC%95%E9%AC%86%E9%A7%95%E9%A6%AD%E5%B7%A8%E9%87%8F%E7%B4%9Adataframes-%E8%87%B3%E5%B0%91%E5%9C%A8%E8%A8%98%E6%86%B6%E9%AB%94%E6%96%B9%E9%9D%A2-2d8cc8a3e26e)
* * For sequential reading, a good randomness could be achieved take reasonable buffer size and shuffle in such buffer. See [discussion on `tensorflow.data.Dataset.shuffle`](https://stackoverflow.com/questions/46444018/meaning-of-buffer-size-in-dataset-map-dataset-prefetch-and-dataset-shuffle)
* See [`sklearn.preprocessing`](https://scikit-learn.org/stable/modules/preprocessing.html) 
*  Efficient tensor operation with [arogozhnikov/einops](https://github.com/arogozhnikov/einops)

----
# Reference

* [TMVA Users Guide](https://github.com/root-project/root/blob/master/documentation/tmva/UsersGuide/TMVAUsersGuide.pdf)
* https://scikit-learn.org/stable/modules/preprocessing.html



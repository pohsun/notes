#ZZZ/index #CS/DSA/ML

## Overview
    
[Wiki: Artificial Intelligence](https://en.wikipedia.org/wiki/Artificial_intelligence)
[ML cheatsheet](https://ml-cheatsheet.readthedocs.io/en/latest/)

----

Quote from the textbook "Machine Learning" by T. Mitchell(1997): *"A computer program is said to learn from experience `E` with respect to some class of tasks `T` and performance measure `P`, if its performance at tasks in `T`, as measured by `P`, improves with experience `E`."*

* [Overview and Theoretical Basis](/Math/InformationTheory.md)
* `E`: [Data preprocessing](Data_preprocessing.md)
* `T`: Tasks (i.e. the algorithms)
   * [`ANN`](NeuralNetwork.md)
        * `CNN`, `RNN`, `GNN`, `GAN`
    * `DT`, `SVM`, etc..
* `P`: Performance measure
    * Supervised, semi-supervised, and unsupervised.
    * [Losses_Regularizers_and_Optimizers](Losses_Regularizers_and_Optimizers.md)
    * Activation functions: Provide non-linear feature in `ANN`.

----

Here is a list of some special topics for AI/ML

* [Visualization](Visualization.md)
* [Jupyter + Colab](/CS/JupyterLab_and_Colab.md)
* [Computer Vision](ComputerVision.md)
* [Natural Language Processing](NaturalLanguageProcessing.md)
* [ML compiling課程](https://mlc.ai/summer22-zh/)
* Generative models
    * [[Diffusion_model]]
            
## Tools

* [Jupyter notebook][/CS/JupyterLab_and_Colab]
* [Scikit-learn](https://scikit-learn.org/stable/user_guide.html)
* NN frameworks
    * [`tensorflow2`](Tensorflow2.md)
    * [`PyTorch`](PyTorch.md)
* [Visualization](Visualization.md)- `matplotlib`, `plotly`, `dash`, etc..

## Reference

### News

[Lil'Log (lilianweng.github.io)](https://lilianweng.github.io/)
[colah's blog](https://colah.github.io/)
[Papers With Code](https://paperswithcode.com/)

### Theoretical references

* [PRML by Bishop](https://github.com/it-ebooks/it-ebooks-2017-04to06/blob/master/%E6%A8%A1%E5%BC%8F%E8%AF%86%E5%88%AB%E4%B8%8E%E6%9C%BA%E5%99%A8%E5%AD%A6%E4%B9%A0%E4%B8%AD%E6%96%87%E7%89%88%EF%BC%88%E9%A9%AC%E6%98%A5%E9%B9%8F%EF%BC%89.pdf)
* [Deep Learning by I. Goodfellow](https://github.com/exacity/deeplearningbook-chinese), 最好先讀過PRML
* The Elements of Statistical Learning by Hastie, 中文版是屎翻
* Understanding machine learning - From theory to algorithms, 在書庫有
* [InformationTheory](/Math/InformationTheory.md)
* [Hung-yi Lee (李宏毅) (ntu.edu.tw)](https://speech.ee.ntu.edu.tw/~hylee/index.php))
        * [某人的2020 ML上課筆記](https://hackmd.io/@shaoeChen/B1CoXxvmm/)
        * [逐字稿](https://miblue119.github.io/hungyi_lectures/index.html)
    * [Next step of ML](https://www.youtube.com/watch?v=XnyM3-xtxHs&list=PLJV_el3uVTsOK_ZK5L0Iv_EQoL1JefRL4)
    * [MLDS 2018 Spring (ntu.edu.tw)](https://speech.ee.ntu.edu.tw/~hylee/mlds/2018-spring.php)
* 吳恩達
    * [ML筆記 in Python](https://github.com/fengdu78/Coursera-ML-AndrewNg-Notes)
    * [DL筆記 in Python](https://github.com/fengdu78/deeplearning_ai_books)

### Technical references

* [Dive into Deep Learning (d2l.ai)](https://d2l.ai/)
* 動手深度學習
    * [動手深度學習 - PyTorch版](https://tangshusen.me/Dive-into-DL-PyTorch/)
    * [動手深度學習 - TF2.0版](https://trickygo.github.io/Dive-into-DL-TensorFlow2.0/)
* [ML From Scratch - 無框架基礎實作](https://github.com/eriklindernoren/ML-From-Scratch)
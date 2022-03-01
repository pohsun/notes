#CS/ML 

# Artificial Neural Network

https://www.asimovinstitute.org/neural-network-zoo/

## Calculation techniques

* [**Computational graphs and back propagation**](https://colah.github.io/posts/2015-08-Backprop/)
* [Computational graphs in PyTorch and TensorFlow](https://towardsdatascience.com/computational-graphs-in-pytorch-and-tensorflow-c25cc40bdcd1) [中譯本](https://zhuanlan.zhihu.com/p/346995454)

## Layers

### Dense

The simplest structure, which is also called *fully connected layer*.

#### Output

### Convolution
* $\text{kernel size}=\text{input size}\times\text{n channels}$
* Activation function introduces non-linearity for the importance of each feature.
* Kernel is learnable.
* $\text{rock}$

#### 1x1 Convolution
[1x1卷積計算在做什麼？](https://medium.com/@chih.sheng.huang821/%E5%8D%B7%E7%A9%8D%E7%A5%9E%E7%B6%93%E7%B6%B2%E8%B7%AF-convolutional-neural-network-cnn-1-1%E5%8D%B7%E7%A9%8D%E8%A8%88%E7%AE%97%E5%9C%A8%E5%81%9A%E4%BB%80%E9%BA%BC-7d7ebfe34b8): 
相當於將前一層的輸出結果做線性疊加，每種線性疊加即為一個維度，故也同時做output tensor的作昇、降維。

### Pooling

### Max-out

### Recursive

# Convolutional Neural Network

See also [A Beginner's Guide To Understanding Convolutional Neural Networks](https://adeshpande3.github.io/adeshpande3.github.io/A-Beginner's-Guide-To-Understanding-Convolutional-Neural-Networks/)

## Models

* [CNN演化史](https://medium.com/%E9%9B%9E%E9%9B%9E%E8%88%87%E5%85%94%E5%85%94%E7%9A%84%E5%B7%A5%E7%A8%8B%E4%B8%96%E7%95%8C/%E6%A9%9F%E5%99%A8%E5%AD%B8%E7%BF%92-ml-note-cnn%E6%BC%94%E5%8C%96%E5%8F%B2-alexnet-vgg-inception-resnet-keras-coding-668f74879306)
* [Implementations in `PyTorch`](https://github.com/pytorch/vision/tree/master/torchvision/models)
* [Implementations in `Keras`](https://github.com/tensorflow/tensorflow/tree/master/tensorflow/python/keras/applications)

### 1998 LeNet
* Basic CNN + Pooling + `softmax`/`tanh`

### 2012 AlexNet
* Non-linear Rectified linear unit(`Relu`)
* Data augmentation
* Dropout

### 2014 Vgg 
* Padding
* small stepping(less parameters) -> keyword: receptive field

### 2014 Inception(GoogLeNet)
* Replace CNN with `inception` structure to significantly reduce the number of parameters without losing accuracy. The core idea of `inception` is similar with replacing dense layers with CNN - drop the computation between uncorrelated neurons.
    * Make use of $1\times{}1$ convolution to reduce 
    * The kernel sizes are optimized using the inception structure.
    * In V2 and V3, larger kernels are factorized into smaller ones, such as  $5\times{}5\to{}3\times{}3\circ{}3\times{}3$ and $7\times{}7\to{}7\times{}1\circ{}1\times{}7$, to further reduce parameters.
    * In V4, ResNet is combined with inception.
* [Review: GoogLeNet](https://medium.com/@chensheep1005/googlenet-ac609d13e3f1)
* [知乎: 讲解GoogleNet的Inception从v1到v4的演变](https://zhuanlan.zhihu.com/p/104671625)

### 2015 [Deep residual network(ResNet)](https://zhuanlan.zhihu.com/p/31852747)
* Residual, feature at different scale won't be dropped during convolution. Meanwhile, as the resolution gets worse, more feature map is introduced to maintain the complexity.
* [直觀理解ResNet](https://medium.com/@rossleecooloh/%E7%9B%B4%E8%A7%80%E7%90%86%E8%A7%A3resnet-%E7%B0%A1%E4%BB%8B-%E8%A7%80%E5%BF%B5%E5%8F%8A%E5%AF%A6%E4%BD%9C-python-keras-8d1e2e057de2)

### 2017 DenseNet
* [知乎講解DenseNet](https://zhuanlan.zhihu.com/p/37189203)

### [理解Spatial Transformer Networks](https://zhuanlan.zhihu.com/p/41738716)

# Recurrent^1 /Recusive^2 Neural Network

* What's the difference between **Recurrent^1** and **Recurrsive^2** NN?
    * Wiki:
        * *Recurrent neural networks are recursive artificial neural networks with a certain structure: that of a linear chain.*
         * *Recursive neural networks operate on any hierarchical structure, combining child representations into parent representations*
         * *Recurrent neural networks operate on the linear progression of time, combining the previous time step and a hidden representation into the representation for the current time step.*
    * To make it clear
        * `RNN`^1 for Recurrent NN.
        * `RNN`^2 for Recursive NN.
        *  `RNN`^2 is a generalization of `RNN`^1 , which operates on any hierarchical structure.
* How and why it work?  
    [遞歸神經網路 Recurrent Neural Network Back-propagation Through Time](https://chih-sheng-huang821.medium.com/%E9%81%9E%E6%AD%B8%E7%A5%9E%E7%B6%93%E7%B6%B2%E8%B7%AF-recurrent-neural-network-back-propagation-through-time-8d49ebf04b77)


## Models

[歷史整理/模型比較](https://github.com/gopala-kr/language-models)
[A list of `xxx2vec` models](https://github.com/MaxwellRebo/awesome-2vec)

### LSTM

### Attention-based model

## Further reading
* [Understanding LSTM Networks](https://colah.github.io/posts/2015-08-Understanding-LSTMs/), [中譯本](https://www.jianshu.com/p/9dc9f41f0b29)
* [The Unreasonable Effectiveness of Recurrent Neural Networks](http://karpathy.github.io/2015/05/21/rnn-effectiveness/)

# Graph Neural Network
* [知乎](https://zhuanlan.zhihu.com/p/43972372)




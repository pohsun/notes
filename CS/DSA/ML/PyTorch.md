---
---

#CS/DSA/ML #CS/Lang/Python 

* [Official API](https://pytorch.org/docs/stable/index.html), [official tutorials](https://pytorch.org/tutorials/)
    *  [Advanced topics: The incredible PyTorch](https://github.com/ritchieng/the-incredible-pytorch)
    * 
* Supportive packages
    * [`pytorch-lightning`: High-level lib to help training and evaluating](https://github.com/PyTorchLightning/pytorch-lightning)
    * [`torchsummary`: Better way showing the figure](https://github.com/sksq96/pytorch-summary)
* [CheatSheat](https://hackmd.io/@rh0jTfFDTO6SteMDq91tgg/HkDRHKLrU)

## Tutorials

* General
    * [動手學深度學習+PyTorch](https://tangshusen.me/Dive-into-DL-PyTorch/)
    * https://github.com/jcjohnson/pytorch-examples
    * https://github.com/hunkim/PyTorchZeroToAll
    * https://github.com/yunjey/pytorch-tutorial
    * [PyTorch handbook中文](https://github.com/zergtant/pytorch-handbook)
* Visualization
    * https://github.com/szagoruyko/pytorchviz
* Performance
    * [Optimize PyTorch Performance for Speed and Memory Efficiency (2022) | by Jack Chih-Hsu Lin | Towards Data Science](https://towardsdatascience.com/optimize-pytorch-performance-for-speed-and-memory-efficiency-2022-84f453916ea6)
* Internals
    * [How Computational Graphs are Constructed in PyTorch](https://pytorch.org/blog/computational-graphs-constructed-in-pytorch/)

## Workflow

### Preprocessing: `DataLoader`

[Official tutorial](https://pytorch.org/tutorials/recipes/recipes/custom_dataset_transforms_loader.html)

Read: [`torch.utils.data`](https://pytorch.org/docs/stable/data.html)
Processing: [`torchvision.transforms`](https://pytorch.org/docs/stable/torchvision/transforms.html)

#### Customization

`torch.utils.data.Dataset` is an abstract class representing a dataset. Your custom dataset should inherit Dataset and override the following methods:

```python
import torch

class CustomizedDataset(tourch.utils.data.Dataset):
    def __init__(self):
        # Load some data here.
        pass
        
    def __len__(self):
        """ Returns the size of the dataset. """
        
        pass
        
    def __getitem__(self, idx):
        """ support indexing such that dataset[i] can be used to get i-th sample. """
        pass
```

Or, alternatively, we could use `generator` style dataset

### Training

* [How does pytorch handle the mini-batch training?](https://discuss.pytorch.org/t/how-does-pytorch-handle-the-mini-batch-training/9707)

----

# Lightning

Similar to `keras` for `tensorflow`, there is `pytorch-lightning` for `PyTorch`.
#ZZZ/index #CS/CoreSkills #CS/Lang/Haskell #CS/Lang/Python 

* [Why Structure and Interpretation of Computer Programs matters](https://people.eecs.berkeley.edu/~bh/sicp.html)
    * [译文：为何 SICP 意义重大 - Paradigm X (soulhacker.me)](https://soulhacker.me/posts/why-sicp-matters/)

``` zsh
cd ~/GoogleDrive/My\ Drive/Obsidian/CS/CoreSkills/SICP
```

Ref: 
* [課程錄影 中英雙字幕](https://youtube.com/playlist?list=PLkEwH_Z2WOlppy8oUfrGwFVlOuKyo3RO_)
    * [SICP 解题集](https://sicp.readthedocs.io/en/latest/)
* [Berkeley CS61A, Spring 2012 Online Textbook (SICP in Python)](https://inst.eecs.berkeley.edu//~cs61a/sp12/book/)
    * [SICP Python 描述 中文版](https://wizardforcel.gitbooks.io/sicp-py/content/)

## Concepts

## Exercises

盡可能用haskell跟python兩種語法構成

### 1.1

![ex_1_1](exercise/ex_1_1.hs)

```haskell
main :: IO ()
main = do
    let result = show 10
    putStrLn result

    let result = show (sum [5, 3, 4])
    putStrLn result
```

### 1.2 
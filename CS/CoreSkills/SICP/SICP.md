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

### Chapter 1
* (p6) 樹形累積: 對任意組合式(function)求值過程，可以一再被展開為回傳值作為節點、單一operator及一個以上arguments（不考慮currying）作為子節點的樹形表示。展開到最後，整個計算過程可以被表示為基於硬體的、對記憶體中的數值的深度優先遍歷操作(DFS)。
* (p10) 應用序求值*applicative order evaluation*與正則序求值*normal order evaluation*
    * 應用序
        * 先對參數求值再進行應用。
        * 可以避免重複求值，一般來說比較有效率，且替換處理的複雜度會降低很多。
    * 正則序
        * 先代換參數完全展開再進行求值。
        * 有時候可以成為有價值的工具。
            * 可跳過沒必要的求值，見[習題1.5](exercise/chap_1.md)
    * 兩者可以被證明會得到相同的結果。
    * 更多討論在Chapter 3, 4
* (p22) 遞迴(*Recursion*)與迭代(*Iteration*)
    * 遞迴
    * 迭代
## Exercises

* 作答原則
    * 盡可能同時用`Haskell`跟`python`兩種語法作答
    * `Haskell`
        *  盡可能使用前綴形式(prefix form), 例如 `((+) 5 3 4)`
    * `Python`
        * 用`functool.reduce`及`operator `製造出前綴形式
        * 用`toolz`生出`curry`
        * 用[`pyrsistent`](https://pyrsistent.readthedocs.io/en/master/)做出invariant
        * 參考[Mastering Monad Design Patterns](https://dev.to/hamzzak/mastering-monad-design-patterns-simplify-your-python-code-and-boost-efficiency-kal)自定義[Monad](https://en.wikipedia.org/wiki/Monad_(functional_programming))
* 各章節解答
    * [Chap 1](exercise/chap_1.md)
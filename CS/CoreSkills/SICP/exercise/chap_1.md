# 1.1

```include haskell
exercise_1_1.hs
```

```include python
exercise_1_1.py
```

# 1.2

```include haskell
exercise_1_2.hs
```

```include python
exercise_1_2.py
```

# 1.3

```include haskell
exercise_1_3.hs
```

```include python
exercise_1_3.py
```
# 1.4

```include haskell
exercise_1_4.hs
```

```include python
exercise_1_4.py
```
# 1.5

```scheme
(define (p) (p))

(define (test x y)
  (if (= x 0)
      0
      y))
(test 0 (p))
```

* 正則序求值
    * **先展開表達**再求值
    * `(p)` in `(test 0 (p))`先塞入`test`，但沒有被用到，不會進入`(p)`的無限遞迴。
    * Haskell應該是正則序
* 應用序求值
    * **先對參數求值**再處理表達
    * `(p)` in `(test 0 (p))`被求值再塞入`test`，會陷入`(p)`的無限遞迴。
    * Python應該是應用序

----

```include haskell
exercise_1_5.hs
```

```include python
exercise_1_5.py
```
# TODO 1.6
* [What's the explanation for Exercise 1.6 in SICP? - Stack Overflow](https://stackoverflow.com/questions/1171252/whats-the-explanation-for-exercise-1-6-in-sicp)

```include haskell
exercise_1_6.hs
```

```include python
exercise_1_6.py
```

# 1.7

```include haskell
exercise_1_7.hs
```

```include python
exercise_1_7.py
```
# 1.8

```include haskell
exercise_1_8.hs
```

```include python
exercise_1_8.py
```





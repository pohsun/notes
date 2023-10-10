```scheme
(define (p) (p))

(define (test x y)
  (if (= x 0)
      0
      y))
(test 0 (p))
```

* 正則序求值
    * 先展開表達再求值
    * `(p)` in `(test 0 (p))`先塞入`test`，但沒有被用到，不會進入`(p)`的無限遞迴。
    * Haskell應該是正則序
* 應用序求值
    * 先對參數求值
    * `(p)` in `(test 0 (p))`被求值再塞入`test`，會陷入`(p)`的無限遞迴。
    * Python應該是應用序

----

```include haskell
exercise_1_5.hs
```

```include python
exercise_1_5.py
```

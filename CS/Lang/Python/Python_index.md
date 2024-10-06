---

---

#ZZZ/index #CS/Lang/Python 

```dataview
TABLE file.tags AS "Tags", file.mday AS "Last Modified"
FROM #CS/Lang/Python
```

# Basics

## Introduction

* [Python 3: Deep Dive (Part 1 - Functional)](https://www.udemy.com/course/python-3-deep-dive-part-1/)
* [Python 3: Deep Dive (Part 2 - Iteration, Generators)](https://www.udemy.com/course/python-3-deep-dive-part-2/)
* [Python 3: Deep Dive (Part 3 - Hash Maps)](https://www.udemy.com/course/python-3-deep-dive-part-3/)
* [Python 3: Deep Dive (Part 4 - OOP)](https://www.udemy.com/course/python-3-deep-dive-part-4/)

## Features

* [PEP 0: Index of PEP](https://www.python.org/dev/peps/)
* [PEP 8 – Style Guide for Python Code](https://peps.python.org/pep-0008/) - 每個開發者都應該從基礎學起
* [PEP 328 – Imports: Multi-Line and Absolute/Relative](https://peps.python.org/pep-0328/)
* [PEP 484 – Type Hints](https://peps.python.org/pep-0484/)
* [PEP 517 – A build-system independent format for source trees](https://peps.python.org/pep-0517/)
* [PEP 3143 – Standard daemon process library](https://peps.python.org/pep-3143/)
* [PEP 684 – A Per-Interpreter GIL](https://peps.python.org/pep-0684/)
* `GIL` and `Concurrency` issues
    * GIL
        * [Python的GIL是什么鬼，多线程性能究竟如何](http://cenalulu.github.io/python/gil-in-python/)
        * [天使还是魔鬼？GIL的前世今生。一期视频全面了解GIL！](https://www.youtube.com/watch?v=XjBsk8JGHhQ)
    * [Concurrent Execution](https://docs.python.org/3/library/concurrency.html)
        * [PEP 492: Coroutines with async and await syntax](https://www.python.org/dev/peps/pep-0492/)
        * [Build Your Own Async (youtube.com)](https://www.youtube.com/watch?v=Y4Gt3Xjd7G8)
        * [await机制详解。再来个硬核内容，把并行和依赖背后的原理全给你讲明白](https://www.youtube.com/watch?v=K0BjgYZbgfE)
        * [asyncio從不會到上路](https://myapollo.com.tw/zh-tw/begin-to-asyncio/)
        * [asyncio: We Did It Wrong – roguelynn](https://www.roguelynn.com/words/asyncio-we-did-it-wrong/)
* [Python module and packaging](Python_Packaging.md)
	* [PEP 420: Implicit Namespace Packages](https://www.python.org/dev/peps/pep-0420/)  - 實用的namespace打包方法
	* [PEP518: `pyproject.toml`]()
	* [利用 pkgutil & importlib 打造可擴充式模組](https://myapollo.com.tw/blog/python-pkgutil-importlib/)
* [WTF Python - 一些鮮為人知的特性](https://github.com/satwikkansal/wtfpython)
* 奇技
	* [Make SUID function on scripts](https://stackoverflow.com/questions/5523279/semantics-of-suid-set-user-id) [一些中文解釋](https://blog.csdn.net/dmjz_lk/article/details/97259258)
	* [Redirecting all kinds of stdout in Python](https://eli.thegreenplace.net/2015/redirecting-all-kinds-of-stdout-in-python/)
        * [Python bytecode explained](https://github.com/MoserMichael/pyasmtool/blob/master/bytecode_disasm.md)

## Advanced topics

* Internals
    * [Exploring the internals (python.org)](https://devguide.python.org/internals/exploring/)
    * [Your Guide to the CPython Source Code – Real Python](https://realpython.com/cpython-source-code-guide/)
    * [码农高天 - YouTube](https://www.youtube.com/@minkoder/videos)
# Useful Modules (Except for DevTools)

* Data analysis
    * Data structures for data analysis with Python:  
        含`numpy`, `pandas`/`vaex`/`modin`, `dask`, `scikit-hep/awkward-array`, ~~`uproot`~~ etc..
    * [`scikit-learn`](https://scikit-learn.org/stable/user_guide.html)
    * [`statmodels`](https://www.statsmodels.org/stable/index.html)
    * [PyTorch](DSA/ML/PyTorch.md)
    * [Tensorflow2](DSA/ML/Tensorflow2.md)
* Patterns 
    * [Awesome Functional Python](https://github.com/sfermigier/awesome-functional-python)
        * [Does Python optimize tail recursion? - Stack Overflow](https://stackoverflow.com/questions/13591970/does-python-optimize-tail-recursion)
* Interface
    * Web: [Django](WebDev/Django.md), `Flask`, `fastAPI`
    * Interface: [`attrs`](https://www.attrs.org/en/stable/)
    * GUI: `pyQt`, [`kivy`](https://kivy.org/)
* Automator
    * [網路爬蟲大全](WebDev/WebScraper.md)  
* Utilities
* Others
	* [`ast`](https://sadh.life/post/ast/), [`lark`](https://github.com/lark-parser/lark) for [wiki: LanguageParsing](https://wiki.python.org/moin/LanguageParsing)
	* python-daemon
	  And corresponding [benchmark](https://github.com/goodmami/python-parsing-benchmarks).
	* Socket programming with [pyzmq](https://pyzmq.readthedocs.io/en/latest/index.html), See also [ZeroMQ](Patterns/ZeroMQ.md)

# DevTools

## Environment setup

* [Introduction to `pyenv`](https://realpython.com/intro-to-pyenv/)
    * [Tip: Use `Python` from `homebrew` in `pyenv`](https://stackoverflow.com/questions/30499795/how-can-i-make-homebrews-python-and-pyenv-live-together).  
        `ln -s $(brew --cellar python)/* ~/.pyenv/versions/`
* [Difference between `venv`, `pyvenv`, `pyenv`, `virtualenv`, `virtualenvwrapper`, `pipenv`](https://stackoverflow.com/questions/41573587/what-is-the-difference-between-venv-pyvenv-pyenv-virtualenv-virtualenvwrappe)
    * After PEP517, we use `Poetry` [Poetry 完全入門指南](https://blog.kyomind.tw/python-poetry/) - 取代venv + pip
    * `venv` or `virtualenv` for modules is good enough for most use case.
* [IPython notebook](https://ipython-books.github.io/)
* 原始碼保護
	* [訂製Python interpreter](https://zhuanlan.zhihu.com/p/54297880)
	* [python编译后的pyd爆破](https://zhuanlan.zhihu.com/p/357372838)

## Profilers

* [A Guide to Analyzing Python Performance](https://everyhue.me/posts/python-performance-analysis/)

### Tools

* line_profiler
* memory_profiler
* cProfile
* [py_spy](https://github.com/benfred/py-spy)
## Debugger

* [`pdb`](https://docs.python.org/3/library/pdb.html) [`pudb`](https://documen.tician.de/pudb/) -> [`breakpoint()`](https://docs.python.org/3/library/functions.html#breakpoint))
* [`objgraph`](https://pypi.org/project/objgraph/)
## Unittest

* [Effective Python Testing With `Pytest`](https://realpython.com/pytest-python-testing/)
### Tools

# Performance issues

## Solution - Concurrency

* A short(?) intro to the python async core implementations: 
    * [Build Your Own Async](https://www.youtube.com/watch?v=Y4Gt3Xjd7G8)
    * [The Other Async (Threads + Async = ❤️)](https://www.youtube.com/watch?v=x1ndXuw7S0s)

Be careful about the definition of the jargons:
* `concurrency`: Multiple tasks make progress **together** in a period of time. The tasks may(`parallelism`) or may not(`non-blocking`) run on multiple threads.
* `parallelism`: Surely another thread is spawned to take care of a task.
    * Implementations: `concurrency.future.ProcessPoolExecutor`, `multiprocessing`, `subprocess`
* `non-blocking`: Also know as `async`, (in most case) an IO bound task starts competing `GIL`. Sometimes, e.g. networking tasks, it is not a good idea to spin up an comsuming thread to handle a low impact task. 
    * Implementations: `concurrency.future.ThreadPoolExecutor`, `asyncio`, `threading`

Some auxiliary modules are provides to support the concurrency, such as
* `queue`: 
* `sched`: Event schedular.

### Tools

*  [Concurrent execution](https://docs.python.org/3/library/concurrency.html)
*  [`asynio`](https://docs.python.org/3/library/asyncio.html)
### See also

* [Python Parallel Programming Cookbook 中文版](https://python-parallel-programmning-cookbook.readthedocs.io/)

## Solution - JIT/AOT

* [scikit-learn: How to optimize for speed](https://scikit-learn.org/stable/developers/performance.html)

### Tools

* `Numba`: The most pythonic solution
   * [Manual](http://numba.pydata.org/numba-doc/latest/user/index.html)
   * JIT for quick development. However, it's embarrassing for deploying.
   * Use `pyyaml` to globally switch on/off JIT.
   * More [constraints](http://numba.pydata.org/numba-doc/dev/reference/pysupported.html).
* [`Cython`](https://cython.readthedocs.io/en/stable/index.html): Slightly `C`-like solution.
   * Compile for static lib. Less constraints.  
        Suitable for deploying well developed package. 
   * A widely adopted solution for mature projects in python community.
   * Offers guides for improving performance.
* [`pybind11`](https://pybind11.readthedocs.io/en/stable/index.html): Pure `C` solution to create a python API.
    * Wrap `C++11` (and beyond) to `Python` module, quite easy to learn and use.
    * Support for `CUDA` and etc..
    * Could be 2x slower than `Numba`.
* (Optional) [Python C API](https://docs.python.org/3/c-api/index.html) 

## Solution - subinterpreter

* 
* [Python 3.12 Preview: Subinterpreters – Real Python](https://realpython.com/python312-subinterpreters/)

## Solution - GPGPU

Please refer to [INDEX: GPGPU]().

# Embedding python in other language

If you insist, see [official doc](https://docs.python.org/3/extending/embedding.html). But, it is suggested to take advantage of socket programming such as using [ZeroMQ](Patterns/ZeroMQ.md).
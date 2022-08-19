#index #CS/ProgLang/Python 

真正的基礎王者課程
[Python 3: Deep Dive (Part 1 - Functional)](https://www.udemy.com/course/python-3-deep-dive-part-1/)
[Python 3: Deep Dive (Part 2 - Iteration, Generators)](https://www.udemy.com/course/python-3-deep-dive-part-2/)
[Python 3: Deep Dive (Part 3 - Hash Maps)](https://www.udemy.com/course/python-3-deep-dive-part-3/)
[Python 3: Deep Dive (Part 4 - OOP)](https://www.udemy.com/course/python-3-deep-dive-part-4/)

# Features

* [PEP 0: Index of PEP](https://www.python.org/dev/peps/)
* [PEP 8: Style Guide](https://www.python.org/dev/peps/pep-0008/) - 每個開發者都應該從基礎學起
* [PEP 328: Imports](python.org/dev/peps/pep-0328/)
* [PEP 484: Type Hints](https://www.python.org/dev/peps/pep-0484/)
* `GIL` and `Concurrency` issues
    * [Concurrent Execution](https://docs.python.org/3/library/concurrency.html)
    * [Python的GIL是什么鬼，多线程性能究竟如何](http://cenalulu.github.io/python/gil-in-python/)
    * [PEP 492: Coroutines with async and await syntax](https://www.python.org/dev/peps/pep-0492/)
* [Python module and packaging](Python_Packaging.md)
	* [PEP 420: Implicit Namespace Packages](https://www.python.org/dev/peps/pep-0420/)  - 實用的namespace打包方法
	* [PEP518: `pyproject.toml`]()
* [WTF Python - 一些鮮為人知的特性](https://github.com/satwikkansal/wtfpython)
* 奇技
	* [Make SUID function on scripts](https://stackoverflow.com/questions/5523279/semantics-of-suid-set-user-id) [一些中文解釋](https://blog.csdn.net/dmjz_lk/article/details/97259258)


# Useful Modules (Except for DevTools)

* Data analysis
    * Data structures in data analysis with Python:  
        含`numpy`, `pandas`, `modin`, `dask`, `scikit-hep/awkward-array`, ~~`uproot`~~ etc..
    * [`scikit-learn`](https://scikit-learn.org/stable/user_guide.html)
    * [`Tensorflow2`](ML/Tensorflow2.md)
    * [`PyTorch`](ML/PyTorch.md)
    * [`statmodels`](https://www.statsmodels.org/stable/index.html)
* Interface
    * Web: [Django](WebDev/Django.md), `Flask`, `fastAPI`
    * GUI: `pyQt`
* Automator

    * ETL
        * [一段 `Airflow` 與資料工程的故事：談如何用 Python 追漫畫連載](https://leemeng.tw/a-story-about-airflow-and-data-engineering-using-how-to-use-python-to-catch-up-with-latest-comics-as-an-example.html)
        * dagster
        * pyperunner
        * lightflow
    * [網路爬蟲大全](WebDev/WebScraper.md)  
* Utilities
* Others
	* [`ast`](https://sadh.life/post/ast/), [`lark`](https://github.com/lark-parser/lark) for  [wiki: LanguageParsing](https://wiki.python.org/moin/LanguageParsing)
	  And corresponding [benchmark](https://github.com/goodmami/python-parsing-benchmarks).

# DevTools

## Environment

* [Introduction to `pyenv`](https://realpython.com/intro-to-pyenv/)
    * [Tip: Use `Python` from `homebrew` in `pyenv`](https://stackoverflow.com/questions/30499795/how-can-i-make-homebrews-python-and-pyenv-live-together).  
        `ln -s $(brew --cellar python)/* ~/.pyenv/versions/`
* [`virtualenv` manual](https://virtualenv.pypa.io/en/latest/index.html)
* [Difference between `venv`, `pyvenv`, `pyenv`, `virtualenv`, `virtualenvwrapper`, `pipenv`](https://stackoverflow.com/questions/41573587/what-is-the-difference-between-venv-pyvenv-pyenv-virtualenv-virtualenvwrappe)
    * `pyenv`(for `Python`) and `venv`(for modules) is good enough for most use case.
    * After PEP517, we use `Poetry`.
        * https://github.com/python-poetry/poetry/issues/1783
* [IPython notebook](https://ipython-books.github.io/)
* [訂製Python interpreter](https://zhuanlan.zhihu.com/p/54297880)

## Profilers

* [A Guide to Analyzing Python Performance](https://everyhue.me/posts/python-performance-analysis/)

### Tools

* line_profiler
* memory_profiler
* cProfile
* [py_spy](https://github.com/benfred/py-spy)

## Debugger

* [`pdb`](https://docs.python.org/3/library/pdb.html) [`pudb`](https://documen.tician.de/pudb/)
* [`objgraph`](https://pypi.org/project/objgraph/)

## Unittest

* [Effective Python Testing With `Pytest`](https://realpython.com/pytest-python-testing/)

### Tools

# Performance issues

## Solution - Concurrency

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

* `Numba`: Most pythonic solution
   * [Manual](http://numba.pydata.org/numba-doc/latest/user/index.html)
   * JIT for quick development. However, it's embarrassing for deploying.
   * Use `pyyaml` to globally switch on/off JIT.
   * More [constraints](http://numba.pydata.org/numba-doc/dev/reference/pysupported.html).
* [`Cython`](https://cython.readthedocs.io/en/stable/index.html): Slightly `C`-like solution.
   * Compile for static lib. Less constraints.  
        Suitable for deploying well developed package.
* [`pybind11`](https://pybind11.readthedocs.io/en/stable/index.html): Pure `C` solution.
    * Wrap `C++11` (and beyond) to `Python` module, quite easy to learn and use.
    * Support for `CUDA` and etc..
    * Could be 2x slower than `Numba`.
* (Optional) [Python C API](https://docs.python.org/3/c-api/index.html)

## Solution - GPGPU

Please refer to [INDEX: GPGPU]().
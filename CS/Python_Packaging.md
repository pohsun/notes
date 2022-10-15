#CS/Lang/Python 

# Module and Packaging

* [Python Packaging(PyPA) User Guide](https://packaging.python.org/)
    * [Quickstart](https://packaging.python.org/tutorials/packaging-projects/)
    * Details of [`setuptools`](https://packaging.python.org/guides/distributing-packages-using-setuptools/)

# Overview

The structure of a project/module could be found as in [the sample namespace project](https://github.com/pypa/sample-namespace-packages) provided officially by PyPA. 

```
root
├── setup.py
├── pyproject.toml
├── LICENSE
├── README.md
├── src
│   └── namespace
│       ├── __init__.py: Consult `PEP420`
│       ├── module.py
│       └── subpackageA
│           ├── __init__.py
│           └── pkgA_module.py
├── docs: Consult `Sphinx` module
└── tests: Consult `pytests`, `coverage` module
    └── test_XXX.py
```

* Jump into legacy [`setup.py`](https://packaging.python.org/guides/distributing-packages-using-setuptools/)
* Jump into [`pyproject.toml`](https://python-poetry.org/docs/pyproject/)
# Dependency management
* [`pip freeze` vs `pip list`?](https://stackoverflow.com/questions/18966564/pip-freeze-vs-pip-list)
	* 總之用 `pip3 freeze > requirements.txt`

# FAQ
* [`install_reqires` v.s. `Requirements.txt`?](https://packaging.python.org/discussions/install-requires-vs-requirements/) [原文](https://pyzh.readthedocs.io/en/latest/python-setup-dot-py-vs-requirements-dot-txt.html)

* [如何發布python package](https://www.jiqizhixin.com/articles/19060901) [原文](https://www.freecodecamp.org/news/from-a-python-project-to-an-open-source-package-an-a-to-z-guide-c34cb7139a22)
* [How to choose an open source license?](https://choosealicense.com/)

# Recommended reading

* [PEP420: Implicit Namespace Packages](https://www.python.org/dev/peps/pep-0420/)
	* 非常實用的個人工具集打包概念，只需要改動`src/namespace/__init__.py`
* [import 概念(及一些測試)](https://blog.hochun836.com/2020/10/03/python/import-concept.html)
* PyPA sample projects
	* [sample project](https://github.com/pypa/sampleproject)
	* [sample namespace project](https://github.com/pypa/sample-namespace-packages)
* [給新手的Poetry的使用說明書](https://blog.kyomind.tw/python-poetry/)
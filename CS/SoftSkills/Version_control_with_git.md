tags: #CS/SoftSkills 

# Reference 

* [Github official help](https://help.github.com/en)
* [Pro Git](https://git-scm.com/book)
* [Git魔法書](http://www-cs-students.stanford.edu/~blynn/gitmagic/intl/zh_tw/)
* [快速上手](https://zlargon.gitbooks.io/git-tutorial/content/)
* [為你自己學git](https://gitbook.tw/)
    * [練習場](https://gitbook.tw/playground)
* [700道git練習題](https://hackmd.io/6cgdNTXCS4O9COMTCGW5jA?view)
* [Git visualized](https://dev.to/lydiahallie/cs-visualized-useful-git-commands-37p1)
* [知乎: 一文講透git底層數據結構和原理](https://zhuanlan.zhihu.com/p/296780372)

# Basics usage

* Configuration
    ```bash
    git config --global user.name "Po-Hsun Chen"
    git config --global user.email pohsun.chen.hep@gmail.com
    git config --global core.editor vim
    ```
* Clone
    `git clone https://github.com/ntuhep/bprimeKit.git`
* Branch/tag operations
    * Create
        ```bash
        git branch newBrName srcBrName
        git tag -a [-m <message>] tagName
        ```
    * Switch to branch/tag
        ```bash
        # In newer git versions
        git switch branchname
        git checkout tagname
        
        # There is no 'switch' in old versions, use checkout is fine.
        git checkout branchname
        ```
* Check status/log/fetch
    ```bash
    git status
    git log
    git fetch --dry-run
    ```
* Reset to 
    ```bash
    git reset --hard HEAD 回復到最新提交版本
    git reset --hard HEAD~ // 等於 ~1 回復到上一個提交版本
    git reset --hard HEAD~n // n 等於往上第幾個提交版本 回復之前指定的提交版本
    ```
    * [`--hard` 的意義請見此文](https://gitbook.tw/chapters/using-git/reset-commit.html)
* Commit all new/changes
   ```bash
    # Register which file to to commited.
    git add filename
    
    # Book a commit.
    git commit -m "Comments to the commit"
    
    # Push commits to remote.
    git push
    
    # If you want to specify a branch
    git push <origin> <branchname>
    
    # If you want to push tags
    git push --tags
    ```
*   Create a new repo and do first upload to github  
    First of all, create a new repository on github, and then...
    ```bash
    cd yourworkspace
    git init
    git add --all
    git commit -a
    git remote add origin https://github.com/username/projname.git
    git pull --rebase origin master
    git push -u origin master
    ```

# Advanced usage

## Conflict handling  
    
* See [Use vimdiff as git mergetool](https://www.rosipov.com/blog/use-vimdiff-as-git-mergetool/)
    * `git config --global merge.tool vimdiff`

```
+--------------------------------+
| LOCAL  |     BASE     | REMOTE |
+--------------------------------+
|             MERGED             |
+--------------------------------+

----

:diffg LO  " Get from LOCAL
:diffg BA  " Get from BASE
:diffg RE  " Get from REMOTE
]c         " Move to the next conflict
[c         " Move to the previous conflict
:wqa       " Save and close all open panes
```
    
## Submodule, subtree
    
* Submodule & subtree: [1](https://blog.puckwang.com/post/2020/git-submodule-vs-subtree/) [2](https://whchi.github.io/posts/difference-between-subtree-and-submodule/)
    * SubTree: 把整個外部 repo 以及 commit log 拷貝到新的 repo 中, 如同名稱一樣, 就是「子樹」的概念, 可把它視為完全獨立於 master repo 底下的 repo. 另需注意subtree並非預設功能, 如果找不到subtree子命令的話就[自己build](https://github.com/git/git/tree/master/contrib/subtree)吧.
    * SubModule: 建立與外部 repo 的 HEAD commit 連結, 但由於僅是連結, 要進行 push 的話會比較複雜, 因此較適合使用的 repo 本身僅需維持在某特定版本的情境.
    * 總之, 只是要**固定在某版本**使用沒有要開新功能的話, 用submodule會比較單純, subtree比較用於**將大project分切為小專案**時使用.
* [Git SubTree 共編 Library](http://yutin.logdown.com/posts/188306-git-subtree-total-addendum-library)

## Bare repo

Create a bare repo with `git init --bare`, then just work as if there is a server.... Nothing differet is found so far. See [this note](https://hackmd.io/@hbdoy/BJz0V5tv8) if you want to understand deeper.

# FAQ

* [About repository transfers](https://help.github.com/articles/about-repository-transfers/)
* What are `HEAD` / `master` / `origin`?  
    `HEAD` is the only official notion in git, `HEAD` always has a well defined meaning. master and origin are common names *usually* used in git but they don't have to be.
    * `HEAD`:
        The current commit your repo is on.  
        Most of the time `HEAD` points to the latest commit in your branch, but that doesn't have to be the case. `HEAD` really just means "what is my repo currently pointing at". In the event that the commit `HEAD` refers to is not the tip of any branch, this is called a "detached head".
    * `base` : The upsteam repo of a fork. Sometimes it is just marked as `upstream`.
    * `master`: The name of the default branch that git creates for you when first creating a repo.  
        In most cases, `master` means "the main branch". Most shops have everyone pushing to `master`, and `master` is considered the definitive view of the repo. But it's also common for release branches to be made off of `master` for releasing. Your local repo has its own `master` branch, that almost always follows the `master` of a remote repo.
    * `origin`: The default name that git gives to your main REMOTE repo.  
        Your box has its own repo, and you most likely push out to some remote repo that you and all your coworkers push to. That remote repo is almost always called origin, but it doesn't have to be.
* Get a single file from repository
    ```bash
    wget --no-check-certificate https://github.com/cms-sw/cmssw/tree/CMSSW_5_3_X/GeneratorInterface/ExternalDecays/data/Bd_Kstarmumu_Kpi.dec
    wget https://raw.githubusercontent.com/<user>/<repo>/<branch>/<tagname/><filename>
    git checkout <branch> -- filename
    ```
* [How to compare two versions](https://help.github.com/articles/comparing-commits-across-time/)
*   Compare local master to current:  
    `git diff HEAD:snippets/tex.snippets snippets/tex.snippets` or  
    `git diff -- snippets/tex.snippets`
* How to sync changes you make in a fork?  
    See [Github help: Syncing a fork](https://help.github.com/articles/syncing-a-fork/)
    ```bash
    # Configure upstream
    git remote -v
    git remote add upstream https://github.com/ORIGINAL_OWNER/ORIGINAL_REPO.git
    git remote -v 
    # sync
    git fetch upstream
    git checkout master
    git merge upstream/master
    git push --tags
    git push origin master
    ```
* How to change origin/master?
    ```bash
    git remote rename origin other
    git remote add origin newRepo
    vim .git/config
    # modify the master section
    ```
* Handle `error: The requested URL returned error: 403 Forbidden while accessing https://github.com/REPO/USER/info/refs`  
    In `.git/config`, replace all `https://` in url with `ssh://git@` and copy public key to git.   
   
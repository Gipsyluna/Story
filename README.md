# Git Github 问题汇总

> 作者：桂明露
>
> 日期：2024/03/18



## 本地仓库

一般流程：初始化，添加到暂存区，提交到本地仓库

```zsh
git init

git add filename
or
git add .

git commit -m "message"
```

其他命令：

```zsh
git status

git log

git checkout filename

git diff filename
```



## 远程仓库

首先在Github上创建好仓库，注意：主流用SSH而不是HTTPS，后者有403问题

```zsh
git remote add <remote name> <url>
git remote add origin git@github.com:Gipsyluna/Story.git

git push -u <remote name> <branch name>
git push -u origin main
```



## 关于SSH Key



### 第一步：检查本地主机是否已经存在ssh key

```zsh
cd ~/.ssh
ls
//看是否存在 id_rsa 和 id_rsa.pub文件，如果存在，说明已经有SSH Key
```

如果存在，直接跳到第三步



### 第二步：生成ssh key

如果不存在ssh key，使用如下命令生成

```zsh
ssh-keygen -t rsa -C "xxx@xxx.com"
//"xxx@xxx.com"为邮箱地址
```

生成完以后再用第二步命令，查看ssh key



### 第三步：获取ssh key公钥内容（id_rsa.pub）

```zsh
cd ~/.ssh
cat id_rsa.pub
```

复制id_rsa.pub内容



### 第四步：在Github账号上添加公钥



### 第五步：验证是否设置成功

```zsh
ssh -T git@github.com
```

对另一个账户则使用`ssh -T git@gipsyluna.github.com `，后续有更详细的说明。



## 关于在一台电脑上配置多个SSH Key

开发人员通常只会生成一个SSH Key，名字叫**id_rsa**，然后提交到多个不同的网站（如：GitHub、CodeArts或Gitee）。

但是也存在另一种需要，在同一个网站上，注册了两个用户名，通常网站不会允许为这两个用户名，配置同一个SSH Key，这时候就会有些麻烦。



### 第一步：在本地Git仓库生成另一个不同的SSH Key

```zsh
ssh-keygen -t rsa -C "xxx@xxx.com"
//"xxx@xxx.com"为邮箱地址

Generating public/private rsa key pair.
Enter file in which to save the key (~/.ssh/id_rsa):<不要直接回车，填写自己定义的名字>
Enter passphrase(empty for no passphrase):
```



### 第二步：在另一个Github账号上添加公钥



### 第三步：编辑**~/.ssh/config**文件

如下是我已经创建好的。

HostName统一为 github.com

Host根据需要取名，例如我的gipsyfine账户用的是github.com，而第二个账户gipsyluna用的是gipsyluna.github.com，在后续远程操作会用到

```
Host github.com
HostName github.com
User git
IdentityFile ~/.ssh/id_rsa
PreferredAuthentications publickey

Host gipsyluna.github.com
HostName github.com
User git
IdentityFile ~/.ssh/gipsyluna
PreferredAuthentications publickey
```



### 第四步：根据需要进行远程操作

对于多个账号使用方式略有不同，仔细看命令。



```zsh
git remote add origin git@github.com:XXX.git
// gipsyfine账户

git remote add origin git@gipsyluna.github.com:XXX.git
// gipsyluna账户
```



## 问题汇总



> 为什么有的人的电脑commit默认就是main，而我的就是master?

这可能是由于你的 Git 版本或配置设置不同造成的。较新版本的 Git 已经将默认分支名称从 `master` 更改为 `main`，以避免与语言和文化上的含义有关的一些问题，并更好地反映代码仓库的含义。

如果你希望在新的 Git 仓库中使用 `main` 作为默认分支名称，可以按照以下步骤进行设置：

1. **创建新的仓库：** 在创建新的 Git 仓库时，在 GitHub 或其他 Git 托管服务中选择 `main` 作为默认分支名称。

2. **本地设置：** 在本地仓库中使用以下命令将默认分支更改为 `main`：

   ```zsh
   git init
   git branch -M main
   ```

3. **全局配置（可选）：** 如果你希望所有新的仓库都默认使用 `main` 作为主分支名称，可以设置 Git 的全局配置：

   ```zsh
   git config --global init.defaultBranch main
   ```

这样，在你初始化新的 Git 仓库时，默认分支就会是 `main` 而不是 `master` 了。

对于已经存在的仓库，你可以手动将主分支从 `master` 更改为 `main`。你可以使用以下命令：

```zsh
git branch -m master main
```

然后将新的主分支推送到远程仓库：

```zsh
git push -u origin main
```

这样就完成了将默认分支从 `master` 更改为 `main`。
# ktools

<p align="center">
  <img      src="https://img.shields.io/github/stars/kenyon-wong/ktools"/>  
  <img      src="https://img.shields.io/github/forks/kenyon-wong/ktools"/> 
  <img      src="https://img.shields.io/github/issues/kenyon-wong/ktools"/> 
<!--   <img      src="https://img.shields.io/github/license/kenyon-wong/ktools"/>  -->
</p>
<p align="center">
<img      src="https://img.shields.io/github/commit-activity/m/kenyon-wong/ktools"/>
<img      src="https://img.shields.io/github/last-commit/kenyon-wong/ktools"/>
<img      src="https://img.shields.io/github/repo-size/kenyon-wong/ktools"/>
</p>

## 项目说明

ktools 是一个 scoop 的 bucket 扩展库，主要 Fork 自以下项目，按照个人习惯对部分软件包进行了适当增删

- https://github.com/ViCrack/scoop-bucket.git
- https://github.com/arch3rPro/PST-Bucket.git

## 食用指南

```powershell
scoop bucket add ktools https://github.com/kenyon-wong/ktools
scoop update
```

## 软件自动更新

> 来自 ViCrack 的 scoop-bucket

这个仓库已经添加 github ci 自动化，每隔几个小时会自动更新所有软件到最新版本

使用者可以自行在系统中加个定时任务，这样就能自动更新 scoop 软件了，当然也可以手工更新

```powershell
scoop update *
```

单个软件的更新可以使用下列命令，大多数情况下软件名不重复的话，可以省略 `vi/`，只需要执行类似 `scoop update xray` 的命令

```powershell
scoop update vi/xray
scoop update vi/windterm
scoop update vi/screentogif
.......
```

## 引用

> 来自 ViCrack 的 scoop-bucket

加了一些我平常可能会用到的一些程序，大部分 json 是我自己写的，还有一部分参考或者定制化改写了以下仓库，表示感谢

-   [ScoopInstaller/Main: 📦 The default bucket for Scoop](https://github.com/ScoopInstaller/Main)
-   [ScoopInstaller/Extras: 📦 The Extras bucket for Scoop](https://github.com/ScoopInstaller/Extras)
-   [chawyehsu/dorado: 🐟 Yet Another bucket for lovely Scoop](https://github.com/chawyehsu/dorado)
-   [kkzzhizhou/scoop-apps 📦](https://github.com/kkzzhizhou/scoop-apps)


# ktools

<p align="center">
  <img src="https://img.shields.io/github/stars/kenyon-wong/ktools" alt="GitHub stars"/>
  <img src="https://img.shields.io/github/forks/kenyon-wong/ktools" alt="GitHub forks"/>
  <img src="https://img.shields.io/github/issues/kenyon-wong/ktools" alt="GitHub issues"/>
  <img src="https://img.shields.io/github/commit-activity/m/kenyon-wong/ktools" alt="Commit activity"/>
  <img src="https://img.shields.io/github/last-commit/kenyon-wong/ktools" alt="Last commit"/>
  <img src="https://img.shields.io/github/repo-size/kenyon-wong/ktools" alt="Repo size"/>
</p>

## 📖 项目说明

ktools 是一个 Scoop 的 bucket 扩展库，主要 Fork 自以下项目，并根据个人需求对部分软件包进行了适当调整：

- [ViCrack/scoop-bucket](https://github.com/ViCrack/scoop-bucket.git)
- [arch3rPro/PST-Bucket](https://github.com/arch3rPro/PST-Bucket.git)

## 🚀 快速开始

### 添加 bucket

在 PowerShell 中运行以下命令：

```powershell
scoop bucket add ktools https://github.com/kenyon-wong/ktools
scoop update
```

## 🔄 软件自动更新

> 此功能来自 ViCrack 的 scoop-bucket

本仓库已添加 GitHub Actions 自动化流程，每隔几个小时会自动将所有软件更新到最新版本。

### 自动更新

建议在系统中添加定时任务，实现 Scoop 软件的自动更新。

### 手动更新

也可以手动更新所有软件：

```powershell
scoop update *
```

更新单个软件（大多数情况下可以省略 `vi/` 前缀）：

```powershell
scoop update vi/xray
scoop update vi/windterm
scoop update vi/screentogif
# 或者
scoop update xray
scoop update windterm
scoop update screentogif
```

## 🙏 致谢

> 部分内容来自 ViCrack 的 scoop-bucket

本项目中的大部分 JSON 配置文件是由项目维护者编写，同时也参考和定制化改写了以下仓库的内容。在此表示感谢：

- [ScoopInstaller/Main](https://github.com/ScoopInstaller/Main): 📦 Scoop 的默认 bucket
- [ScoopInstaller/Extras](https://github.com/ScoopInstaller/Extras): 📦 Scoop 的 Extras bucket
- [chawyehsu/dorado](https://github.com/chawyehsu/dorado): 🐟 又一个 Scoop bucket
- [kkzzhizhou/scoop-apps](https://github.com/kkzzhizhou/scoop-apps): 📦 Scoop 应用集合

## 🤝 贡献

欢迎提交 Issues 或 Pull Requests 来帮助改进这个项目。

## 📄 许可证

本项目采用 [MIT 许可证](LICENSE)。

---

⭐ 如果您觉得这个项目有用，请给它一个 star！

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

### 安装工具

```powershell
# 安装单个工具
scoop install nuclei

# 批量安装推荐工具组合
scoop install nuclei httpx subfinder katana naabu dnsx
```

## 📦 工具列表

### ProjectDiscovery 工具套件

```powershell
# 漏洞扫描
scoop install nuclei          # 快速可定制的漏洞扫描器

# HTTP 工具
scoop install httpx           # 多功能 HTTP 工具包
scoop install katana          # 下一代爬虫框架

# 子域名发现
scoop install subfinder       # 被动子域名枚举
scoop install alterx          # 子域名字典生成器
scoop install shuffledns      # DNS 暴力破解

# 端口和网络扫描
scoop install naabu           # 快速端口扫描器
scoop install dnsx            # DNS 工具包
scoop install mapcidr         # CIDR 范围操作

# 资产发现
scoop install uncover         # 资产发现工具
scoop install cloudlist       # 云资产枚举
scoop install asnmap          # ASN 枚举

# 辅助工具
scoop install notify          # 通知推送
scoop install proxify         # 代理工具
scoop install interactsh      # OOB 交互收集
scoop install cdncheck        # CDN 检测
scoop install tlsx            # TLS 数据提取
scoop install urlfinder       # URL 发现
scoop install tldfinder       # TLD 发现
scoop install tunnelx         # 隧道工具
scoop install simplehttpserver # HTTP 服务器
scoop install chaos-client    # Chaos 数据集客户端
scoop install aix             # AI 驱动的安全工具
scoop install pdtm            # ProjectDiscovery 工具管理器
```

### ChainReactors 工具

```powershell
scoop install gogo            # 自动化引擎
scoop install spray           # HTTP 模糊测试
scoop install zombie          # 僵尸网络工具
scoop install neutron         # 日志分析工具
```

### 其他安全工具

```powershell
scoop install ksubdomain      # 子域名枚举
scoop install feroxbuster     # 内容发现
scoop install crawlergo       # 浏览器爬虫
scoop install fscan           # 内网综合扫描
scoop install xray            # Web 安全评估
scoop install yakit           # 安全测试平台
scoop install ffuf            # Web 模糊测试
scoop install goby            # 资产收集和漏洞扫描
```

## 🔥 推荐工具组合

### 信息收集套件
```powershell
scoop install subfinder httpx naabu dnsx katana
```

### 漏洞扫描套件
```powershell
scoop install nuclei xray fscan
```

### 内网渗透套件
```powershell
scoop install fscan gogo spray
```

### 完整 ProjectDiscovery 套件
```powershell
scoop install nuclei httpx subfinder katana naabu dnsx mapcidr alterx asnmap uncover notify proxify
```

## 📖 使用示例

### Nuclei 漏洞扫描
```powershell
# 更新模板
nuclei -update-templates

# 扫描单个目标
nuclei -u https://example.com

# 使用特定模板
nuclei -u https://example.com -t cves/

# 按严重程度过滤
nuclei -u https://example.com -severity critical,high
```

### 子域名枚举工作流
```powershell
# 1. 被动收集子域名
subfinder -d example.com -o subdomains.txt

# 2. 验证存活
httpx -l subdomains.txt -o alive.txt

# 3. 端口扫描
naabu -list alive.txt -o ports.txt

# 4. 漏洞扫描
nuclei -list alive.txt -o vulnerabilities.txt
```

### HTTP 探测和爬虫
```powershell
# 1. HTTP 探测
httpx -l domains.txt -title -status-code -tech-detect -o http_info.txt

# 2. 爬虫收集 URL
katana -list alive.txt -d 3 -o urls.txt

# 3. 模糊测试
ffuf -w wordlist.txt -u https://example.com/FUZZ
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

## ✨ 特色功能

- 🔄 **自动更新**: GitHub Actions 自动更新所有工具到最新版本
- 🔐 **安全可靠**: 所有配置文件包含 SHA256 哈希校验
- 📚 **详细文档**: 重要工具包含详细的使用说明和示例
- 🎯 **精选工具**: 专注于安全测试和渗透测试领域的优质工具
- 🚀 **开箱即用**: 一键安装，无需复杂配置

## 🙏 致谢

> 部分内容来自 ViCrack 的 scoop-bucket

本项目中的大部分 JSON 配置文件是由项目维护者编写，同时也参考和定制化改写了以下仓库的内容。在此表示感谢：

- [ScoopInstaller/Main](https://github.com/ScoopInstaller/Main): 📦 Scoop 的默认 bucket
- [ScoopInstaller/Extras](https://github.com/ScoopInstaller/Extras): 📦 Scoop 的 Extras bucket
- [chawyehsu/dorado](https://github.com/chawyehsu/dorado): 🐟 又一个 Scoop bucket
- [kkzzhizhou/scoop-apps](https://github.com/kkzzhizhou/scoop-apps): 📦 Scoop 应用集合
- [ProjectDiscovery](https://projectdiscovery.io/): 🔍 优秀的开源安全工具
- [ChainReactors](https://github.com/chainreactors): ⚡ 红队工具开发

## 🤝 贡献

欢迎提交 Issues 或 Pull Requests 来帮助改进这个项目。

## 📄 许可证

本项目采用 [MIT 许可证](LICENSE)。

---

⭐ 如果您觉得这个项目有用，请给它一个 star！

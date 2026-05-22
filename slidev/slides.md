---
theme: seriph
background: https://cover.sli.dev
title: 小红书自动搜索评论工具 (MCP Server 2.0)
info: |
  ## 小红书MCP工具介绍
  从部署环境到登录使用的完整流程演示

  基于Playwright的小红书自动化工具
class: text-center
transition: slide-left
---

# 小红书自动搜索评论工具

## 从部署环境到登录使用的一站式流程

<div class="text-2xl mt-8">
基于 Playwright 和 fastmcp 的小红书自动化服务
</div>

<div class="text-lg mt-4 opacity-80">
包含部署、MCP配置、登录与搜索使用流程
</div>

---
layout: center
---

# 项目简介

- **核心功能**：自动登录、搜索笔记、抓取内容、获取评论、生成评论并发布
- **技术栈**：Python、Playwright、FastMCP、MCP Client
- **目标场景**：通过小红书自动化实现内容采集与智能评论交互
- **关键文件**：`xiaohongshu_mcp.py`、`login_script.py`、`search_script.py`

---
layout: two-cols
---

# 核心模块

::left::

## MCP Server 主入口
- `xiaohongshu_mcp.py`
- 提供登录、搜索、获取内容、获取评论、分析和发布评论功能

## 登录验证
- `login()` 方法实现扫码登录
- 使用持久化浏览器上下文保存登录状态

::right::

## 搜索流程
- `search_notes(keywords, limit)`
- 加载搜索结果页面并解析笔记卡片

## 内容获取
- `get_note_content(url)`
- 分析笔记标题、作者、发布时间和正文内容

---
layout: center
---

# 部署环境准备

## 环境要求

- Python 3.8 或更高版本
- 安装 `playwright` 和 `fastmcp`
- 支持 Windows / macOS / Linux
- 推荐使用虚拟环境

---
layout: two-cols
---

# 安装与环境搭建

::left::

## 1. 获取项目
```bash
git clone <repo-url>
cd Redbook-Search-Comment-MCP2.0-main
```

## 2. 创建虚拟环境
```bash
python -m venv venv
# Windows
venv\Scripts\activate
# macOS/Linux
source venv/bin/activate
```

::right::

## 3. 安装依赖
```bash
pip install -r requirements.txt
pip install fastmcp
```

## 4. 安装Playwright浏览器
```bash
playwright install
```

---
layout: center
---

# 关键目录与文件

- `xiaohongshu_mcp.py`：MCP Server 核心逻辑
- `login_script.py`：登录流程验证脚本
- `search_script.py`：搜索流程验证脚本
- `browser_data/`：持久化浏览器上下文，保存登录状态
- `requirements.txt`：依赖包列表

---
layout: center
---

# MCP 客户端配置

## 配置示例

```json
{
  "mcpServers": {
    "xiaohongshu MCP": {
      "command": "<绝对路径>/venv/bin/python",
      "args": ["<绝对路径>/xiaohongshu_mcp.py", "--stdio"]
    }
  }
}
```

---
layout: two-cols
---

# 配置要点

::left::

- 使用虚拟环境中的 Python 解释器
- `xiaohongshu_mcp.py` 必须使用绝对路径
- Windows 路径中反斜杠需转义

::right::

- 确保已执行 `playwright install`
- `browser_data` 目录需要可写权限
- `--stdio` 是 MCP 常用通信方式

---
layout: center
---

# 启动 MCP Server

## 方式一：直接运行

```bash
# 激活虚拟环境
venv\Scripts\activate  # Windows
source venv/bin/activate  # macOS/Linux

python xiaohongshu_mcp.py
```

## 方式二：通过 MCP 客户端启动

- 在客户端中选择已配置 Server
- 启动后保持连接状态

---
layout: center
---

# 登录流程概览

## 自动登录机制

1. 启动持久化浏览器上下文
2. 访问 `https://www.xiaohongshu.com`
3. 查找页面中的“登录”按钮
4. 用户手动扫码登录
5. 登录成功后保存状态

---
layout: two-cols
---

# 登录实现细节

::left::

## `login()` 方法
- 检查是否已初始化浏览器
- 访问小红书首页
- 点击登录按钮
- 轮询检测是否完成登录

::right::

## 登录状态管理
- 将登录状态保存到 `browser_data`
- `ensure_browser()` 每次调用时自动检测登录状态
- 已登录后，后续功能可直接使用

---
layout: center
---

# 登录使用示例

## MCP 客户端示例

```
帮我登录小红书账号
```

## 脚本测试示例

```bash
python login_script.py
```

---
layout: center
---

# 搜索笔记流程

## `search_notes(keywords, limit=5)`

- 登录检查
- 访问搜索页
- 多次等待页面加载
- 使用备用选择器找到笔记卡片
- 提取标题与链接
- 返回结构化结果

---
layout: two-cols
---

# 搜索使用示例

::left::

### MCP 客户端
```
帮我搜索小红书笔记，关键词为：旅游
```

::right::

### 脚本测试
```bash
python search_script.py
```

---
layout: center
---

# 获取笔记内容流程

## `get_note_content(url)`

- 登录检查
- 标准化 URL
- 加载笔记页面
- 滚动并等待页面渲染
- 检测错误页面
- 尝试多种选择器获取标题、作者、发布时间
- 过滤评论区，提取笔记正文

---
layout: center
---

# 从登录到使用的完整链路

1. 登录小红书
2. 搜索关键词，获取笔记链接
3. 获取笔记详情内容
4. 分析笔记内容
5. 生成评论并发布

---
layout: two-cols
---

# 数据分析与评论生成

::left::

## `analyze_note(url)`
- 调用 `get_note_content`
- 解析标题、作者、发布时间、正文
- 判断笔记所属领域
- 返回结构化结果给 AI 生成评论

::right::

## `post_smart_comment(url, comment_type)`
- 支持评论类型：引流、点赞、咨询、专业
- 生成评论策略说明
- 返回分析结果与目标评论指南
- 由客户端生成文本并调用 `post_comment`

---
layout: center
---

# 发布评论流程

## `post_comment(url, comment)`

- 登录检查
- 加载帖子页面
- 定位评论输入框
- 输入评论内容并发送
- 尝试多种发送方式

---
layout: center
---

# 运行检查与调试

- `login_script.py`：验证登录功能
- `search_script.py`：验证搜索功能
- `xiaohongshu_mcp.py`：MCP Server 主入口
- `browser_data/`：保存登录状态

---
layout: center
---

# 关键注意事项

- 首次登录需要手动扫码
- `browser_data` 保存登录状态，避免重复登录
- 如果页面结构变化，可能需要更新选择器
- 确保 `playwright` 浏览器安装正常
- 保持 MCP 客户端与服务器配置一致

---
layout: center
---

# 总结

- 本项目涵盖从部署环境到小红书登录的完整流程
- `xiaohongshu_mcp.py` 是流程核心，负责浏览器自动化与 MCP 通信
- 登录后即可进行搜索、内容抓取与评论发布
- 建议先完成环境配置，再逐步验证登录与搜索功能

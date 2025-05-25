# 抖音无水印视频文本提取 MCP 服务器

[![PyPI version](https://badge.fury.io/py/douyin-mcp-server.svg)](https://badge.fury.io/py/douyin-mcp-server)
[![Python version](https://img.shields.io/pypi/pyversions/douyin-mcp-server.svg)](https://pypi.org/project/douyin-mcp-server/)

一个基于 Model Context Protocol (MCP) 的服务器，可以从抖音分享链接下载无水印视频，提取音频并转换为文本。

## 功能特性

- 🎵 从抖音分享链接获取无水印视频
- 🎧 自动提取视频音频
- 📝 使用AI语音识别提取文本内容
- 🧹 自动清理中间临时文件
- 🔧 支持自定义API配置

## 安装

### 使用 uvx 安装（推荐）

```bash
uvx douyin-mcp-server
```

### 使用 pip 安装

```bash
pip install douyin-mcp-server
```

## 使用方法

### 1. 启动服务器

```bash
douyin-mcp-server
```

### 2. 在Claude Desktop中配置

在你的 `claude_desktop_config.json` 中添加：

```json
{
  "mcpServers": {
    "douyin-mcp": {
      "command": "uvx",
      "args": ["douyin-mcp-server"],
      "env": {
        "DOUYIN_API_KEY": "your-api-key-here"
      }
    }
  }
}
```

### 3. 使用MCP工具

#### 获取无水印下载链接

使用 `get_douyin_download_link` 工具：

```python
# 在Claude中使用，无需API密钥
get_douyin_download_link("https://v.douyin.com/xxx")
```

#### 提取视频文本

使用 `extract_douyin_text` 工具（需要设置环境变量 DOUYIN_API_KEY）：

```python
# 在Claude中使用
extract_douyin_text("https://v.douyin.com/xxx")
```

#### 解析视频信息

使用 `parse_douyin_video_info` 工具：

```python
parse_douyin_video_info("https://v.douyin.com/xxx")
```

## API 配置

### 默认配置

服务器默认使用 [SiliconFlow API](https://cloud.siliconflow.cn/i/TxUlXG3u)：
- API URL: `https://api.siliconflow.cn/v1/audio/transcriptions`
- 模型: `FunAudioLLM/SenseVoiceSmall`

### 自定义配置

你可以自定义API配置：

```python
extract_douyin_text(
    share_link="your-douyin-link",
    api_base_url="https://your-custom-api.com/transcriptions",
    model="your-custom-model"
)
```

## 环境变量配置

在Claude Desktop的配置文件中设置环境变量：

```json
{
  "mcpServers": {
    "douyin-mcp": {
      "command": "uvx",
      "args": ["douyin-mcp-server"],
      "env": {
        "DOUYIN_API_KEY": "sk-your-api-key-here"
      }
    }
  }
}
```

## 工具说明

### `get_douyin_download_link`

获取抖音视频的无水印下载链接，无需API密钥。

**参数：**
- `share_link`: 抖音分享链接或包含链接的文本

**返回：**
- 包含下载链接和视频信息的JSON格式数据

### `extract_douyin_text`

完整的文本提取工具，执行以下步骤：
1. 解析抖音分享链接
2. 下载无水印视频
3. 提取音频
4. 转换音频为文本
5. 清理临时文件

**参数：**
- `share_link`: 抖音分享链接或包含链接的文本
- `api_base_url`: API基础URL（可选）
- `model`: 语音识别模型（可选）

**环境变量：**
- `DOUYIN_API_KEY`: 语音识别API密钥（必需）

### `parse_douyin_video_info`

仅解析视频基本信息，不下载视频。

**参数：**
- `share_link`: 抖音分享链接

### 资源访问

- `douyin://video/{video_id}`: 通过视频ID获取详细信息

## 依赖要求

- Python 3.8+
- ffmpeg（系统需要安装ffmpeg）
- requests
- ffmpeg-python
- tqdm
- mcp

## 安装 ffmpeg

### macOS
```bash
brew install ffmpeg
```

### Ubuntu/Debian
```bash
sudo apt update
sudo apt install ffmpeg
```

### Windows
下载并安装 [ffmpeg](https://ffmpeg.org/download.html)

## 开发

### 本地开发

```bash
git clone https://github.com/yzfly/douyin-mcp-server.git
cd douyin-mcp-server
pip install -e .
```

### 运行测试

```bash
python -m douyin_mcp_server.server
```

## 注意事项

- 确保系统已安装 ffmpeg
- 需要在环境变量中设置有效的语音识别API密钥 `DOUYIN_API_KEY`
- 获取下载链接功能无需API密钥
- 中间文件会自动清理，不会占用磁盘空间
- 支持大部分抖音视频格式

## 许可证

MIT License

## 作者

- **yzfly** - [yz.liu.me@gmail.com](mailto:yz.liu.me@gmail.com)
- GitHub: [https://github.com/yzfly](https://github.com/yzfly)

## 贡献

欢迎提交 Issue 和 Pull Request！

## 更新日志

### v1.0.0
- 初始版本
- 支持抖音视频文本提取
- 支持获取无水印视频下载链接
- 从环境变量读取API密钥
- 自动清理临时文件
- 支持自定义API配置
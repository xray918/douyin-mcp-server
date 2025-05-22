# Douyin MCP Server

抖音无水印链接提取 MCP 服务器

## 安装

使用 uvx 安装（推荐）：

```bash
uvx douyin-mcp-server
```

或使用 pip 安装：

```bash
pip install douyin-mcp-server
```

## 使用方法

### 1. 在 Claude Desktop 中使用

配置文件 `claude_desktop_config.json`：

```json
{
  "mcpServers": {
    "douyin": {
      "command": "uvx",
      "args": ["douyin-mcp-server"]
    }
  }
}
```

重启 Claude Desktop 后，直接发送抖音分享链接：

```
帮我提取这个抖音视频的无水印链接：
复制此链接，打开Dou音搜索，直接观看视频！ https://v.douyin.com/iFhBEj2t/
```

### 2. 直接运行

```bash
douyin-mcp-server
```

### 3. 使用 MCP Inspector 测试

```bash
uvx mcp dev douyin-mcp-server
```

## 功能

- **工具名称**: `get_douyin_video_url`
- **参数**: `share_text` - 包含抖音分享链接的文本
- **返回**: 无水印视频下载链接

## 支持的链接格式

- `https://v.douyin.com/xxx/`
- `https://www.douyin.com/video/xxx`
- 包含上述链接的分享文本

## 许可证

MIT License

## 作者

- **yzfly** - [GitHub](https://github.com/yzfly)
- **Email**: yz.liu.me@gmail.com
#!/usr/bin/env python3
"""
抖音无水印链接提取 MCP 服务器
"""

import json
import re
import requests
from mcp.server.fastmcp import FastMCP

# 创建 MCP 服务器
mcp = FastMCP("Douyin Link Extractor")

# 请求头
headers = {
    'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 17_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) EdgiOS/121.0.2277.107 Version/17.0 Mobile/15E148 Safari/604.1'
}


def parse_share_url(share_text: str):
    """从分享文本中提取无水印视频链接"""
    # 提取分享链接
    share_url = re.findall('http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', share_text)[0]
    share_response = requests.get(share_url, headers=headers)
    video_id = share_response.url.split("?")[0].strip("/").split("/")[-1]
    share_url = f'https://www.iesdouyin.com/share/video/{video_id}'
    
    # 获取视频页面内容
    response = requests.get(share_url, headers=headers)
    response.raise_for_status()
    pattern = re.compile(
        pattern=r"window\._ROUTER_DATA\s*=\s*(.*?)</script>",
        flags=re.DOTALL,
    )
    
    find_res = pattern.search(response.text)
    
    if not find_res or not find_res.group(1):
        raise ValueError("从HTML中解析视频信息失败")
    
    # 解析JSON数据
    json_data = json.loads(find_res.group(1).strip())
    VIDEO_ID_PAGE_KEY = "video_(id)/page"
    NOTE_ID_PAGE_KEY = "note_(id)/page"
    
    if VIDEO_ID_PAGE_KEY in json_data["loaderData"]:
        original_video_info = json_data["loaderData"][VIDEO_ID_PAGE_KEY]["videoInfoRes"]
    elif NOTE_ID_PAGE_KEY in json_data["loaderData"]:
        original_video_info = json_data["loaderData"][NOTE_ID_PAGE_KEY]["videoInfoRes"]
    else:
        raise Exception("无法从JSON中解析视频或图集信息")
    
    data = original_video_info["item_list"][0]
    
    # 获取视频信息
    video_url = data["video"]["play_addr"]["url_list"][0].replace("playwm", "play")
    desc = data.get("desc", "").strip() or f"douyin_{video_id}"
    
    # 替换文件名中的非法字符
    desc = re.sub(r'[\\/:*?"<>|]', '_', desc)
    
    return {
        "url": video_url,
        "title": desc,
        "video_id": video_id
    }


@mcp.tool()
def get_douyin_video_url(share_text: str) -> str:
    """
    从抖音分享文本中提取无水印视频链接
    
    Args:
        share_text: 包含抖音分享链接的文本
        
    Returns:
        无水印视频下载链接
    """
    try:
        result = parse_share_url(share_text)
        return result["url"]
    except Exception as e:
        return f"错误：{str(e)}"


def main():
    """主函数"""
    mcp.run()


if __name__ == "__main__":
    main()
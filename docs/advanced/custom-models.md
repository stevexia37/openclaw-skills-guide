# 配置自定义模型

## OpenAI 兼容 API

支持任何 OpenAI 兼容的 API：

```json
{
  "provider": "openai-compatible",
  "api_base": "https://your-api-endpoint.com/v1",
  "api_key": "your-api-key",
  "model": "your-model-name"
}
```

## 本地模型 (Ollama)

1. 安装 Ollama: https://ollama.ai
2. 下载模型: `ollama pull llama3`
3. 在 OpenClaw 中配置本地模型

## 国内模型

支持配置国内大模型：

- 文心一言
- 通义千问
- 智谱 AI
- 月之暗面

配置方法参见官方文档。

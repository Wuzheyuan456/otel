# 配置 Claude Code

通过 ADVibe MaaS 平台 API 配置 Claude Code 开发工具。

## 使用场景

当用户需要以下操作时使用此 skill：
- 在 macOS 上安装并配置 Claude Code
- 使用 ADVibe MaaS 平台的 API Key 设置 Claude Code
- 配置 Claude Code 模型参数

## 前置条件

- macOS 系统
- 公司内网环境需设置代理才能访问外部网络
- 用户必须拥有 ADVibe MaaS 平台的 API Key
  - API Key 申请指南：https://nio.feishu.cn/wiki/PldIwKQgEibbLGkLJ5UcV1B4nlf

## 执行步骤

### 第1步：获取用户的 API Key

在执行任何操作之前，必须先向用户索取 ADVibe MaaS 平台的 API Key。

向用户提示：
```
请提供你在 ADVibe MaaS 平台申请的 API Key。
如果还没有申请，请前往此链接申请：https://nio.feishu.cn/wiki/PldIwKQgEibbLGkLJ5UcV1B4nlf
```

在用户提供有效的 API Key（非空字符串）之前，不得继续执行后续步骤。

### 第2步：安装 Claude Code

先检查是否已安装及当前版本：
```bash
claude -v
```

如果未安装，先设置代理，再通过官方脚本安装 Claude Code：
```bash
export HTTPS_PROXY="http://proxy.nioint.com:8080"
curl -fsSL https://claude.ai/install.sh | bash
```

如果已安装则跳过此步骤。

注意：如需更新到新版本，执行以下命令：
```bash
claude update
```

### 第3步：创建配置目录

```bash
mkdir -p ~/.claude
```

### 第4步：写入配置文件

将以下内容写入 `~/.claude/settings.json`，将 `{{API_KEY}}` 替换为用户提供的实际 API Key：

```json
{
  "env": {
    "ANTHROPIC_AUTH_TOKEN": "{{API_KEY}}",
    "ANTHROPIC_API_KEY": "",
    "CLAUDE_CODE_DISABLE_FEEDBACK_SURVEY": 1,
    "DISABLE_TELEMETRY": 1,
    "CLAUDE_CODE_ENABLE_GATEWAY_MODEL_DISCOVERY": "1",
    "ANTHROPIC_BASE_URL": "https://api-ad-ops-prod-advibe.nioint.com",
    "CLAUDE_CODE_MAX_OUTPUT_TOKENS": "32000",
    "ANTHROPIC_DEFAULT_OPUS_MODEL": "claude-opus-4-7",
    "ANTHROPIC_DEFAULT_SONNET_MODEL": "claude-sonnet-4-6",
    "ANTHROPIC_DEFAULT_HAIKU_MODEL": "claude-haiku-4-5",
    "ANTHROPIC_MODEL": "opusplan"
  }
}
```

### 第5步：验证配置

```bash
cat ~/.claude/settings.json
```

确认 API Key 已正确写入，且 JSON 格式有效。

### 第6步：启动 Claude Code

```bash
claude
```

告知用户 Claude Code 已配置完成，可以开始使用。

## 重要注意事项

- 绝对不能将 API Key 硬编码或存储在 `~/.claude/settings.json` 以外的任何地方
- 必须要求用户提供自己的 API Key，不得在最终配置中使用占位符
- 如果用户的 `~/.claude/settings.json` 已存在，必须先警告用户并确认是否覆盖
- `ANTHROPIC_BASE_URL` 必须指向 `https://api-ad-ops-prod-advibe.nioint.com`，这是 ADVibe 代理端点

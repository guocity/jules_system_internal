# Claude Code Environment Documentation

**Generated:** 2025-11-27
**Session ID:** session_01PB5Pe9rkfXtwSzxUD7V7in
**Container ID:** container_01V3kCKYLLos2VnVKGmuoSpf--claude_code_remote--hefty-fickle-shabby-churns

---

## Table of Contents
1. [System Overview](#system-overview)
2. [Process Architecture](#process-architecture)
3. [Network Configuration](#network-configuration)
4. [Hardware Resources](#hardware-resources)
5. [User and Permissions](#user-and-permissions)
6. [Python Environment](#python-environment)
7. [Node.js Environment](#nodejs-environment)
8. [Git Configuration](#git-configuration)
9. [Environment Variables](#environment-variables)
10. [Claude Code Architecture](#claude-code-architecture)

---

## System Overview

### Operating System
- **Distribution:** Ubuntu 24.04.3 LTS (Noble Numbat)
- **Kernel:** Linux 4.4.0 #1 SMP Sun Jan 10 15:06:54 PST 2016
- **Architecture:** x86_64 (64-bit)
- **Hostname:** runsc
- **Virtualization:** Running in KVM hypervisor (full virtualization)
- **Container Environment:** Yes (IS_SANDBOX=yes)
- **Uptime:** System has been running for ~1 minute at time of investigation

### Container Information
```json
{
  "container_name": "container_01V3kCKYLLos2VnVKGmuoSpf--claude_code_remote--hefty-fickle-shabby-churns",
  "creation_time": 1764284661.8523204
}
```

---

## Process Architecture

### Process Hierarchy

The Claude Code environment runs with the following process tree:

```
process_api (PID 1)
├── sh (PID 19)
│   └── environment-manager (PID 21)
│       └── claude (PID 81)
│           └── bash (shells spawned for command execution)
```

### Key Processes

#### 1. **process_api** (PID 1)
- **Executable:** `/process_api`
- **Type:** ELF 64-bit LSB pie executable, static-pie linked
- **Command:** `/process_api --addr 0.0.0.0:2024 --max-ws-buffer-size 32768 --cpu-shares 4096 --oom-polling-period-ms 100 --memory-limit-bytes 8589934592`
- **Purpose:** Root process that manages the container lifecycle and provides API endpoints
- **Listening Address:** 0.0.0.0:2024
- **Memory Limit:** 8GB (8589934592 bytes)
- **CPU Shares:** 4096

#### 2. **environment-manager** (PID 21)
- **Executable:** `/usr/local/bin/environment-manager`
- **Type:** ELF 64-bit LSB executable, dynamically linked
- **Command:** `/usr/local/bin/environment-manager task-run --stdin --session session_01PB5Pe9rkfXtwSzxUD7V7in --session-mode new --upgrade-claude-code=False`
- **Purpose:** Manages the execution environment and sessions for Claude Code
- **Session Management:** Handles session lifecycle and environment setup
- **Output Logging:** `/tmp/environment-manager.out`

#### 3. **claude** (PID 81)
- **Executable:** Node.js application
- **Location:** `/opt/node22/bin/claude`
- **Package:** @anthropic-ai/claude-code@2.0.50
- **Purpose:** Main Claude Code application that processes user interactions and executes commands
- **Threads:** 10 worker threads
- **Working Directory:** `/home/user/jules_system_internal`

### Communication Flow

```
User → Anthropic API Server (api.anthropic.com)
    ↓
process_api (WebSocket on port 2024)
    ↓
environment-manager (Session Management)
    ↓
claude (Main Application)
    ↓
bash (Command Execution)
```

---

## Network Configuration

### IP Address
- **Primary IP:** 21.0.0.74
- **Loopback:** 127.0.0.1 (lo)

### Network Interfaces

1. **f1723b9488-v** (Virtual Interface)
   - Received: 733,028 bytes (1,906 packets)
   - Transmitted: 1,450,991 bytes (2,077 packets)
   - No errors, drops, or collisions

2. **lo** (Loopback)
   - Standard loopback interface
   - No traffic at time of investigation

### DNS Configuration
- **Resolv.conf:** Empty or default configuration

### Proxy Configuration

All external HTTP/HTTPS traffic is routed through an authenticated proxy:

- **Proxy Address:** 21.0.0.75:15004
- **Authentication:** JWT-based authentication with container-specific tokens
- **Token Expiration:** Tokens expire after ~4 hours (exp: 1764299061)
- **Proxy Variables:**
  - `HTTP_PROXY`, `HTTPS_PROXY`, `http_proxy`, `https_proxy`
  - `GLOBAL_AGENT_HTTP_PROXY`, `GLOBAL_AGENT_HTTPS_PROXY`
  - `YARN_HTTP_PROXY`, `YARN_HTTPS_PROXY`

### No Proxy Exceptions
The following domains bypass the proxy:
- localhost, 127.0.0.1
- 169.254.169.254 (Instance metadata)
- metadata.google.internal
- *.svc.cluster.local, *.local
- *.googleapis.com, *.google.com

---

## Hardware Resources

### CPU

- **Processor:** Intel Xeon (Model 106)
- **CPU Cores:** 16 cores (single socket)
- **Threads per Core:** 1
- **CPU Speed:** 2600.026 MHz
- **Cache Size:** 8192 KB (8 MB L3)
- **Architecture Features:**
  - AVX-512 support (avx512f, avx512dq, avx512cd, avx512bw, avx512vl)
  - AES-NI encryption
  - SHA extensions
  - Hardware transactional memory (RTM, HLE)
  - Virtual Machine Extensions

### Memory

- **Total Memory:** 13.3 GB (13,631,488 KB)
- **Available Memory:** 12.7 GB (13,302,360 KB)
- **Memory Usage:** ~329 MB used
- **Active Memory:** 264 MB
- **Cached:** 129 MB
- **Swap:** 0 KB (no swap configured)

### Disk Storage

- **Root Filesystem:** 30 GB total, 3 MB used (1% utilization)
- **/dev:** 252 GB (tmpfs)
- **/dev/shm:** 252 GB (tmpfs)
- **Filesystem Type:** Overlay filesystem (container)

### System Load
- **Load Average:** 0.00, 0.00, 0.00 (1, 5, 15 minute averages)
- **Users Logged In:** 0

---

## User and Permissions

### Current User
- **Username:** root
- **UID:** 0
- **GID:** 0
- **Groups:** root (0)
- **Home Directory:** /root
- **Shell:** /bin/bash

### Working Directory
- **Current:** `/home/user/jules_system_internal`
- **Repository:** Git repository (guocity/jules_system_internal)

### File Permissions
- Running as root user with full system privileges
- Access to all system resources

---

## Python Environment

### Python Installation

- **Version:** Python 3.11.14
- **Executable:** `/usr/local/bin/python3`
- **Type:** System Python installation

### Python Path (sys.path)

```
/usr/lib/python311.zip
/usr/lib/python3.11
/usr/lib/python3.11/lib-dynload
/root/.local/lib/python3.11/site-packages
/usr/local/lib/python3.11/dist-packages
/usr/lib/python3/dist-packages
```

### Installed Python Packages

| Package | Version | Purpose |
|---------|---------|---------|
| argcomplete | 3.1.4 | Command-line completion |
| certifi | 2025.11.12 | SSL certificates |
| charset-normalizer | 3.4.4 | Character encoding detection |
| colorama | 0.4.6 | Terminal color support |
| conan | 2.22.2 | C/C++ package manager |
| cryptography | 41.0.7 | Cryptographic operations |
| httplib2 | 0.20.4 | HTTP client library |
| Jinja2 | 3.1.6 | Template engine |
| packaging | 24.0 | Package version handling |
| pip | 24.0 | Package installer |
| PyYAML | 6.0.1 | YAML parser |
| requests | 2.32.5 | HTTP library |
| setuptools | 68.1.2 | Package development |
| urllib3 | 2.5.0 | HTTP client |
| yq | 3.1.0 | YAML/JSON processor |

### Additional Python Tools
- **dbus-python:** D-Bus integration
- **python-apt:** APT package management
- **launchpadlib:** Launchpad API access
- **patch-ng:** Patch file handling

---

## Node.js Environment

### Node.js Installation

- **Node Version:** v22.21.1
- **NPM Version:** 10.9.4
- **Installation Path:** `/opt/node22/bin/node`
- **Package Manager:** npm, pnpm, yarn (all available)

### Global NPM Packages

| Package | Version | Purpose |
|---------|---------|---------|
| **@anthropic-ai/claude-code** | **2.0.50** | **Claude Code main application** |
| chromedriver | 142.0.3 | Chrome WebDriver |
| corepack | 0.34.0 | Package manager manager |
| eslint | 9.39.1 | JavaScript linter |
| http-server | 14.1.1 | Simple HTTP server |
| nodemon | 3.1.11 | Development auto-restart |
| playwright | 1.56.1 | Browser automation |
| pnpm | 10.23.0 | Fast package manager |
| prettier | 3.6.2 | Code formatter |
| serve | 14.2.5 | Static file server |
| ts-node | 10.9.2 | TypeScript execution |
| typescript | 5.9.3 | TypeScript compiler |
| yarn | 1.22.22 | Package manager |

### Node Configuration

- **Extra CA Certs:** `/etc/ssl/certs/ca-certificates.crt`
- **Corepack:** Auto-pinning disabled
- **Proxy Support:** Configured via ELECTRON_GET_USE_PROXY

---

## Git Configuration

### Git Version
- **Version:** git version 2.43.0

### Global Configuration

```ini
user.name=Claude
user.email=noreply@anthropic.com
user.signingkey=/home/claude/.ssh/commit_signing_key.pub
gpg.format=ssh
gpg.ssh.program=/tmp/code-sign
commit.gpgsign=true
http.proxyauthmethod=basic
```

### Commit Signing
- **Enabled:** Yes (all commits are signed)
- **Format:** SSH signatures
- **Key:** `/home/claude/.ssh/commit_signing_key.pub`
- **Signing Program:** `/tmp/code-sign` (custom signing wrapper)

### Repository Configuration

#### Current Repository
- **Remote Name:** origin
- **Repository:** guocity/jules_system_internal
- **Remote URL:** `http://local_proxy@127.0.0.1:27169/git/guocity/jules_system_internal`
- **Fetch/Push:** Both operations use the same URL

#### Git Proxy
- **Proxy Type:** Local HTTP proxy
- **Proxy Address:** 127.0.0.1:27169
- **Authentication:** Username-based (local_proxy)
- **Purpose:** Routes GitHub operations through authenticated proxy

### Repository Status
- **Current Branch:** claude/document-environment-setup-01PB5Pe9rkfXtwSzxUD7V7in
- **Working Directory:** Clean (no uncommitted changes)
- **Recent Commit:** 8e2e1b0 (init)

---

## Environment Variables

### Claude Code Specific

| Variable | Value | Purpose |
|----------|-------|---------|
| CLAUDECODE | 1 | Identifies Claude Code environment |
| CLAUDE_CODE_VERSION | 2.0.50 | Current version |
| CLAUDE_CODE_SESSION_ID | session_01PB5Pe9rkfXtwSzxUD7V7in | Current session |
| CLAUDE_CODE_CONTAINER_ID | container_01V3k... | Container identifier |
| CLAUDE_CODE_REMOTE | true | Running in remote mode |
| CLAUDE_CODE_REMOTE_ENVIRONMENT_TYPE | cloud_default | Cloud environment |
| CLAUDE_CODE_DEBUG | true | Debug mode enabled |
| CLAUDE_CODE_ENTRYPOINT | remote | Entry point type |
| CLAUDE_CODE_OAUTH_TOKEN_FILE_DESCRIPTOR | 4 | OAuth token file descriptor |
| CLAUDE_CODE_WEBSOCKET_AUTH_FILE_DESCRIPTOR | 3 | WebSocket auth descriptor |

### API Configuration

| Variable | Value |
|----------|-------|
| ANTHROPIC_BASE_URL | https://api.anthropic.com |

### Proxy Configuration

All proxy variables point to: `21.0.0.75:15004` with JWT authentication

- HTTP_PROXY, HTTPS_PROXY
- GLOBAL_AGENT_HTTP_PROXY, GLOBAL_AGENT_HTTPS_PROXY
- YARN_HTTP_PROXY, YARN_HTTPS_PROXY

### Development Tools

| Variable | Value | Purpose |
|----------|-------|---------|
| JAVA_HOME | /usr/lib/jvm/java-21-openjdk-amd64 | Java 21 |
| MAVEN_HOME | /opt/maven | Maven build tool |
| GRADLE_HOME | /opt/gradle | Gradle build tool |
| NVM_DIR | /opt/nvm | Node Version Manager |
| RBENV_ROOT | /opt/rbenv | Ruby environment |
| RUSTUP_HOME | /root/.rustup | Rust toolchain |
| BUN_INSTALL | /root/.bun | Bun runtime |

### System Configuration

| Variable | Value |
|----------|-------|
| PATH | /root/.local/bin:/root/.cargo/bin:/usr/local/go/bin:/opt/node22/bin:/opt/maven/bin:/opt/gradle/bin:/opt/rbenv/bin:/root/.bun/bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin |
| SHELL | /bin/bash |
| HOME | /root |
| PWD | /home/user/jules_system_internal |
| PYTHONUNBUFFERED | 1 |
| RUST_BACKTRACE | 1 |
| IS_SANDBOX | yes |

### MCP (Model Context Protocol)

| Variable | Value |
|----------|-------|
| CODESIGN_MCP_PORT | 40668 |
| CODESIGN_MCP_TOKEN | pXGMxPV2k09QMquHGvERwQM7fOVR3_tQJXOLDIc83o8= |
| ENABLE_MCP_CLI | false |

### SSL/TLS Certificates

| Variable | Value |
|----------|-------|
| SSL_CERT_FILE | /etc/ssl/certs/ca-certificates.crt |
| REQUESTS_CA_BUNDLE | /etc/ssl/certs/ca-certificates.crt |
| NODE_EXTRA_CA_CERTS | /etc/ssl/certs/ca-certificates.crt |

### Miscellaneous

| Variable | Value |
|----------|-------|
| GIT_EDITOR | true |
| DEBIAN_FRONTEND | noninteractive |
| DEBUGINFOD_URLS | https://debuginfod.ubuntu.com |
| MAX_THINKING_TOKENS | 31999 |
| CCR_TEST_GITPROXY | 1 |

---

## Claude Code Architecture

### Directory Structure

**Claude Configuration:** `/root/.claude/`

```
/root/.claude/
├── projects/          # Project-specific configurations
├── session-env/       # Session environment data
├── settings.json      # Claude Code settings
├── shell-snapshots/   # Shell state snapshots
├── skills/            # Custom skills
├── statsig/           # Statistics and telemetry
├── stop-hook-git-check.sh  # Git validation hook
└── todos/             # Task management data
```

### How Claude Code Communicates with API Server

#### 1. **WebSocket Connection**
- Claude Code maintains a WebSocket connection to the `process_api` server
- Authentication file descriptor: 3 (CLAUDE_CODE_WEBSOCKET_AUTH_FILE_DESCRIPTOR)
- The WebSocket handles bidirectional communication for:
  - User messages and commands
  - Tool execution requests
  - Response streaming
  - Real-time updates

#### 2. **OAuth Authentication**
- OAuth token file descriptor: 4 (CLAUDE_CODE_OAUTH_TOKEN_FILE_DESCRIPTOR)
- Tokens are managed by the environment-manager
- Used for authenticating with Anthropic's API (api.anthropic.com)

#### 3. **API Flow**

```
User Input (Web/CLI)
    ↓
Anthropic API (api.anthropic.com)
    ↓
Claude LLM Processing
    ↓
WebSocket Response → process_api:2024
    ↓
environment-manager (session management)
    ↓
claude application (PID 81)
    ↓
Tool Execution (bash, file operations, etc.)
    ↓
Results back through WebSocket
    ↓
Anthropic API
    ↓
User
```

#### 4. **Network Path**

All external requests (GitHub, npm, pip, etc.) follow this path:

```
claude application
    ↓
Authenticated Proxy (21.0.0.75:15004)
    ↓
External Service (github.com, npmjs.com, etc.)
```

### GitHub Repository Access

#### 1. **Local Git Proxy**
- **Address:** 127.0.0.1:27169
- **Purpose:** Intercepts git operations and routes them through authenticated proxy
- **Configuration:** Set in `.git/config` as remote URL

#### 2. **Repository Cloning Process**

```
git clone/fetch/push command
    ↓
Local Git Proxy (127.0.0.1:27169)
    ↓
Authenticated Proxy (21.0.0.75:15004 + JWT)
    ↓
GitHub API (github.com)
```

#### 3. **Authentication**
- Uses `local_proxy` user in git URL
- JWT tokens embedded in proxy environment variables
- SSH commit signing via custom `/tmp/code-sign` program

### Session Management

#### Session Lifecycle

1. **Session Creation**
   - Container created with unique ID
   - `environment-manager` starts session
   - Session ID: `session_01PB5Pe9rkfXtwSzxUD7V7in`

2. **Environment Setup**
   - Shell snapshots created in `/root/.claude/shell-snapshots/`
   - Environment variables loaded
   - Git configuration applied

3. **Task Execution**
   - Commands executed via bash shells
   - Working directory maintained at `/home/user/jules_system_internal`
   - Shell state preserved across command executions

4. **Resource Limits**
   - Memory limit: 8GB
   - CPU shares: 4096
   - OOM (Out of Memory) polling: 100ms

### Code Signing Process

When commits are created:

1. Claude Code calls git commit
2. Git invokes `/tmp/code-sign` (gpg.ssh.program)
3. Code sign program connects to MCP server on port 40668
4. MCP server signs commit with SSH key
5. Signature attached to commit
6. Commit completed

**MCP Server Details:**
- Port: 40668 (CODESIGN_MCP_PORT)
- Token: pXGMxPV2k09QMquHGvERwQM7fOVR3_tQJXOLDIc83o8=
- Purpose: Secure commit signing without exposing private keys

---

## Summary

### Key Characteristics

1. **Isolated Container Environment**
   - Running in sandboxed container with resource limits
   - Full virtualization via KVM hypervisor
   - Ubuntu 24.04 LTS base system

2. **Multi-Process Architecture**
   - `process_api` → `environment-manager` → `claude` → `bash`
   - Clear separation of concerns
   - WebSocket-based communication

3. **Comprehensive Development Environment**
   - Python 3.11, Node.js 22, Java 21
   - Multiple build tools (Maven, Gradle, npm, pnpm, yarn)
   - Language support: Python, JavaScript/TypeScript, Java, Ruby, Rust, Go

4. **Secure Network Architecture**
   - All external traffic through authenticated proxy
   - JWT-based authentication with time-limited tokens
   - Git operations through local proxy
   - SSH commit signing via MCP server

5. **Session Management**
   - Persistent session state
   - Shell snapshot preservation
   - Environment isolation
   - Resource monitoring and limits

### Performance Characteristics

- **CPU:** 16 cores @ 2.6 GHz with AVX-512
- **Memory:** 13.3 GB total, ~12.7 GB available
- **Storage:** 30 GB root filesystem (nearly empty)
- **Network:** Low latency within container network
- **Startup Time:** Container ready in ~1 minute

### Security Features

- Sandboxed execution environment
- Authenticated proxy for all external requests
- Commit signing with SSH keys
- JWT-based API authentication
- No swap to prevent memory leaks to disk
- Root user contained within container namespace

---

*End of Documentation*

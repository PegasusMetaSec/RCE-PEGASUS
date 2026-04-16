<div align="center">

# 🦅 PEGASUS RCE

### *WordPress Backup Backup Plugin - Remote Code Execution Exploit*

[![Version](https://img.shields.io/badge/version-1.0-blue.svg)](https://github.com/yourusername/pegasus-rce)
[![Python](https://img.shields.io/badge/python-3.7+-green.svg)](https://www.python.org/downloads/)
[![License](https://img.shields.io/badge/license-MIT-red.svg)](LICENSE)
[![Status](https://img.shields.io/badge/status-stable-brightgreen.svg)]()

</div>

---

## 📋 Table of Contents

- [Overview](#-overview)
- [Features](#-features)
- [Prerequisites](#-prerequisites)
- [Installation](#-installation)
- [Usage](#-usage)
- [How It Works](#-how-it-works)
- [Technical Details](#-technical-details)
- [Configuration](#-configuration)
- [Disclaimer](#-disclaimer)
- [License](#-license)
- [Contributing](#-contributing)

---

## 🎯 Overview

**PEGASUS RCE** is a sophisticated penetration testing tool that exploits a Remote Code Execution vulnerability in the **WordPress Backup Backup plugin**. The tool leverages advanced PHP filter chain techniques to achieve arbitrary code execution on vulnerable WordPress installations.

> ⚠️ **IMPORTANT**: This tool is intended for authorized security testing and educational purposes only. Always obtain proper permission before testing any system.

---

## ✨ Features

| Feature | Description |
|---------|-------------|
| 🚀 **Multi-threading** | Concurrent scanning with up to 75 threads |
| 🔧 **PHP Filter Chains** | Advanced encoding bypass techniques |
| 🎲 **Randomized Payloads** | Dynamic filename generation to avoid detection |
| 🌈 **Colored Output** | Real-time visual feedback with colorama |
| 📁 **Results Export** | Automatic saving of successful shells |
| 🔄 **User-Agent Rotation** | Bypass basic WAF rules |
| 🛡️ **SSL Bypass** | Ignore SSL certificate validation |
| ⏱️ **Timeout Handling** | Prevent hanging requests |

---

## 📦 Prerequisites

Before using PEGASUS RCE, ensure you have the following installed:

```bash
# Python 3.7 or higher
python --version

# Required Python packages
pip install requests
pip install colorama
pip install urllib3

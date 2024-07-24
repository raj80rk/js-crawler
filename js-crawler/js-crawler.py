
#!/usr/bin/env python3

import requests
from bs4 import BeautifulSoup
import os
import urllib.parse
import argparse
import threading
import time
import sys
import pyfiglet
import termcolor

visited_urls = set()
lock = threading.Lock()

def print_banner():
    banner = pyfiglet.figlet_format("js-crawler", font="slant")
    print(termcolor.colored(banner, 'green'))
    sub_banner = "Powered by eagle_rock"
    print(termcolor.colored(sub_banner, 'yellow') + "\n")

def log_output(url, output_file=None):
    if output_file:
        with open(output_file, 'a') as file:
            file.write(url + '\n')
    else:
        print(url)

def crawl(site_url, timeout, output_file, verbose):
    with lock:
        if site_url in visited_urls:
            return
        visited_urls.add(site_url)
    
    try:
        response = requests.get(site_url, timeout=timeout)
        response.raise_for_status()
        html = response.text
        soup = BeautifulSoup(html, 'html.parser')

        # Extract JS and JSON files
        js_files = []
        json_files = []
        
        for script in soup.find_all('script', src=True):
            src = script['src']
            if src.endswith('.js'):
                js_file = urllib.parse.urljoin(site_url, src)
                js_files.append(js_file)

        for link in soup.find_all('a', href=True):
            href = link['href']
            if href.endswith('.json'):
                json_file = urllib.parse.urljoin(site_url, href)
                json_files.append(json_file)

        # Log JS files
        for js_file in js_files:
            try:
                js_response = requests.get(js_file, timeout=timeout)
                js_response.raise_for_status()
                log_output(js_file, output_file)
                if verbose:
                    print(js_file)
            except requests.RequestException as e:
                if verbose:
                    print(f"Error downloading {js_file}: {e}")

        # Log JSON files
        for json_file in json_files:
            try:
                json_response = requests.get(json_file, timeout=timeout)
                json_response.raise_for_status()
                log_output(json_file, output_file)
                if verbose:
                    print(json_file)
            except requests.RequestException as e:
                if verbose:
                    print(f"Error downloading {json_file}: {e}")

        # Follow links to continue crawling
        for link in soup.find_all('a', href=True):
            next_url = urllib.parse.urljoin(site_url, link['href'])
            if next_url.startswith(site_url):
                crawl(next_url, timeout, output_file, verbose)

    except requests.RequestException as e:
        if verbose:
            print(f"Error crawling {site_url}: {e}")

def start_crawling(urls, threads, timeout, output_file, verbose):
    if output_file and os.path.exists(output_file):
        os.remove(output_file)

    threads_list = []
    for url in urls:
        t = threading.Thread(target=crawl, args=(url, timeout, output_file, verbose))
        t.start()
        threads_list.append(t)
        while threading.active_count() > threads:
            time.sleep(1)

    for t in threads_list:
        t.join()

def read_input_file(file_path):
    with open(file_path, 'r') as file:
        return [line.strip() for line in file]

def main():
    print_banner()
    
    parser = argparse.ArgumentParser(description="JS and JSON files crawler")
    parser.add_argument('-u', '--url', help="URL to crawl", nargs='+')
    parser.add_argument('-il', '--input', help="File containing URLs to crawl")
    parser.add_argument('-o', '--output', help="File to save the output")
    parser.add_argument('-t', '--threads', type=int, help="Number of threads to use", default=2)
    parser.add_argument('--timeout', type=int, help="Request timeout in seconds", default=5, choices=range(5, 16))
    parser.add_argument('-v', '--verbose', action='store_true', help="Enable verbose output")
    
    args = parser.parse_args()

    if args.url:
        urls = args.url
    elif args.input:
        urls = read_input_file(args.input)
    else:
        print("Please provide a URL with -u or an input file with -il")
        sys.exit(1)

    start_crawling(urls, args.threads, args.timeout, args.output, args.verbose)

if __name__ == "__main__":
    main()


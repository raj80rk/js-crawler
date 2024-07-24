# js-crawler
js-crawler
js-crawler is a versatile tool designed for extracting JavaScript sources from URLs and web pages. It provides both a command-line interface (CLI) for straightforward URL processing and a package interface for custom integrations, making it an essential tool for pentesters, bug bounty hunters, and developers who need to extract JavaScript sources efficiently.

Features
Efficient JavaScript Extraction: Extracts JavaScript (.js) and JSON (.json) files from web pages and HTTP responses.
Command-Line Interface (CLI): Offers a user-friendly CLI for quick and easy URL processing and output management.
Custom Integration: Can be integrated into custom workflows or scripts via its package interface.
Multi-Threaded Crawling: Speeds up the extraction process with multi-threaded support.
Verbose Logging: Optionally enable verbose output for detailed logging of the crawling process.
Output Options: Save results to a file or print them to the console.
Use Cases
Pentesters: Quickly gather JavaScript files from a target website to analyze for vulnerabilities.
Bug Bounty Hunters: Extract and review JavaScript sources to identify potential security issues.
Developers: Integrate into custom tools or scripts for automated extraction of JavaScript and JSON resources.

**Install Dependencies**

    Install the required Python packages using `pip`:

    ```bash
    pip install -r requirements.txt
    ```

 **Run the Script**

    You can now use `js-crawler` by running the script:

    ```bash
    python3 js-crawler.py --help
    ```

    This will display the available command-line options and usage instructions.

## Usage

### Command-Line Arguments

- `-u`, `--url` : URL(s) to crawl. Specify multiple URLs separated by spaces.
- `-il`, `--input` : Path to a file containing URLs to crawl. Each URL should be on a new line.
- `-o`, `--output` : Path to a file where results will be saved. If not specified, results are printed to the console.
- `-t`, `--threads` : Number of threads for crawling. Default is 2.
- `--timeout` : Request timeout in seconds. Default is 5, with a range of 5-15.
- `-v`, `--verbose` : Enable verbose output for detailed logging.

### Examples

1. **Extract JavaScript from a single URL and print results:**

    ```bash
    js-crawler -u https://example.com
    ```

2. **Extract from multiple URLs and save to a file:**

    ```bash
    js-crawler -u https://example.com https://anotherexample.com -o results.txt
    ```

3. **Crawl URLs from a file with verbose output:**

    ```bash
    js-crawler -il urls.txt -v
    ```

4. **Customize the number of threads and timeout:**

    ```bash
    js-crawler -u https://example.com -t 5 --timeout 10
    ```

## Contributing

Contributions are welcome! Please submit issues or pull requests to help improve the tool. For major changes, open an issue first to discuss potential updates.

## License

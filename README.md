# EmailURLExtractor
 EmailURLExtractor is a script designed to extract URLs from email logs and provide a list of fully qualified domain names (FQDNs) for further analysis. This tool can be useful for various purposes, such as investigating email communications, analyzing website links, or identifying potentially malicious URLs.
 
## Features

- URL Extraction: EmailURLExtractor utilizes regular expressions to extract URLs from email logs, capturing the links present in the email content.

- FQDN Retrieval: The script processes the extracted URLs to obtain the corresponding fully qualified domain names (FQDNs).

- Customizable Functionality: EmailURLExtractor provides a flexible code structure that allows you to modify and extend the script to fit your specific requirements or integrate with additional functionalities.

## Installation

1. Clone the repository:

```
   git clone [https://github.com/HassanNasrMohamed/EmailURLExtractor.git]
```

2. Install the required dependencies:

```
		pip install -r requirements.txt
```
## Usage

1. Prepare your email logs: Ensure you have the email logs in a suitable format (csv) for processing. Each log entry should be a string containing email URL.
2. Modify the script (optional): Customize the script according to your needs. You can add additional processing steps, implement URL filtering, or incorporate further analysis based on your specific requirements.
3. Run the script: Execute the script to extract URLs from email logs and retrieve the associated FQDNs.
```
	python email_url_extractor.py
```
4. Analyze the results: Review the list of FQDNs obtained from the email logs. Use this information for further analysis, investigation, or any other relevant tasks.

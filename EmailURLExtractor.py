import csv
from urllib.parse import unquote
from urllib.parse import urlparse


## Def URL Decoder Function:

def decode_url(url):
    # Decode URL
    decoded_url = unquote(url)
    return decoded_url
## Def Extract FQDN Function:

def extract_domains(url):
    # Extract domains from URL segments
    domains = []
    segments = url.split('http')
    for segment in segments:
        if segment.startswith('s://'):
            parsed_url = urlparse('http' + segment)
            domains.append(parsed_url.netloc)

    return domains


## Read Encoded URLs Function:
 
def decode_and_extract_domains(csv_file):
    decoded_domains = []

    with open(Input_File, 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            if len(row) > 0:
                url = row[0]
                decoded_url = decode_url(url)
                domains = extract_domains(decoded_url)
                decoded_domains.extend(domains)

    return decoded_domains

# Input & Output Files

Input_File = 'Urls.csv'
Output_File = 'FQDN.csv'
decoded_domains = decode_and_extract_domains(Input_File)

## Unique Domains Function:

unique_domains = list(set(decoded_domains))

## Output File Function:

with open(Output_File, "a", newline="") as outfile:
    writer = csv.writer(outfile)
    for domain in unique_domains:
       row = [domain]
       writer.writerow(row)
       print(domain)

print("Decoding & Extracting FQDN Completed Successfully !! \n You Can Find The Output in FQDN.csv")
print("By: Hassan Nasr !!")
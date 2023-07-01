## WhoIs Python Script

This is a simple Python script that can be used from the command line to quickly check the registration status of multiple domains listed in a text file.

## Installation

1. Clone the repository

```bash
git clone https://github.com/suspiciousRaccoon/WhoIs-python-script
```

2. Install dependencies

```bash
pip install -r requirements.txt
```

## Usage

1.Run the script with the following command:

```bash
python whois_script.py -i input_file.txt
```

Replace `input_file.txt` with the path to your input text file containing domains to check. The path must contain the text file itself. Ensure that each domain is listed on a separate line, with no additional content or formatting.

2.The script will create two output files:

- 'registered.txt' - Contains registered domains.
- 'not_registered.txt' - Contains unregistered domains.

By default, these output files will be created in the same directory as the script file. You can also specify custom output file paths using the optional -r and -n arguments.

```bash
python whois_script.py -i input_file.txt -r your/path/registered_output/ -n your/path/not_registered_output/
```

Replace `your/path/registered_output/` and `your/path/not_registered_output/` with your desired output paths

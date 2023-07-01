from pathlib import Path
import argparse
import whois


def parse_args():
    """
    Parses the command line arguments.

    Returns:
        Tuple[str, str, str]: A tuple containing the input file path, the output file path for registered domains, and the output file path for unregistered domains.
    """
    parser = argparse.ArgumentParser(
        description='Check domain registration status')
    parser.add_argument('-i', '--input_file', type=str, required=True,
                        help='Filepath to the input text file containing domains to check (must include the actual text file)')
    parser.add_argument("-r", "--registered", default=Path(__file__).parent, type=str,
                        help="Filepath to the output text file for registered domains (optional, default: script file's directory)")
    parser.add_argument("-n", "--not-registered", default=Path(__file__).parent, type=str,
                        help="Filepath to the output text file for unregistered domains (optional, default: script file's directory)")
    args = parser.parse_args()

    return args


def check_domain_registration(domain):
    """
    Checks the registration status of a domain.

    Args:
        domain (str): The domain to check.

    Returns:
        bool: True if the domain is registered, False otherwise.
    """
    try:
        w = whois.whois(domain)
        return bool(w.domain_name)
    except whois.parser.PywhoisError as e:
        # print(f'Error checking domain {domain}: {}')
        return False


def get_domains(input_file, output_registered, output_not_registered):
    """
    Retrieves the domain registration status for each domain in the input file and writes the results to the respective output files.

    Args:
        input_file (str): Filepath to the input text file containing domains to check.
        output_registered (str): Filepath to the output text file for registered domains.
        output_not_registered (str): Filepath to the output text file for unregistered domains.

    Returns:
        None
    """
    with open(input_file, 'r', encoding='utf-8') as f, \
            open(Path(output_registered, 'registered.txt'), 'w') as registered, \
            open(Path(output_not_registered, 'not_registered.txt'), 'w') as not_registered:
        registered.write('Starting registered\n')
        not_registered.write('Starting not registered\n')
        lines = f.readlines()
        for line in lines:
            domain = line.strip()  # Remove leading/trailing whitespace
            if check_domain_registration(domain):
                registered.write(domain + '\n')
                # print(f'Registered: {domain}')
            else:
                not_registered.write(domain + '\n')
                # print(f'Not registered: {domain}')


if __name__ == "__main__":
    args = parse_args()
    input_file = args.input_file
    registered_path = args.registered
    not_registered_path = args.not_registered
    print('Starting Script')
    get_domains(input_file, registered_path, not_registered_path)
    print('Script Finished')

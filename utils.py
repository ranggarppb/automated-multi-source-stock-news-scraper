from collections import defaultdict
from configparser import ConfigParser

# Function for reading configuration
def config_reader(config, section):
    """
    Reading configuration file
    Input :
        - config (str) : path to the configuration file
        - section (str) : section to be read
    Output :
        - config_dict (dictionary) : configuration dictionary
    """
    # Create parser
    parser = ConfigParser()
    # Read config file
    parser.read(config)
    # Get database section
    config_dict = {}
    params = parser.items(section)
    for param in params:
        config_dict[param[0]] = param[1]
    return config_dict

def list_duplicates(seq):
    tally = defaultdict(list)
    for i,item in enumerate(seq):
        tally[item].append(i)
    return list(((key,locs) for key,locs in tally.items() if len(locs)>1))
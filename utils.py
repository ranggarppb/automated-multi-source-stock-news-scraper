from collections import defaultdict
from configparser import ConfigParser
import re
import simplejson

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



FLAGS = re.VERBOSE | re.MULTILINE | re.DOTALL
WHITESPACE = re.compile(r'[ \t\n\r]*', FLAGS)

def grab_json(s):
    """Takes the largest bite of JSON from the string.
       Returns (object_parsed, remaining_string)
    """
    decoder = simplejson.JSONDecoder()
    obj, end = decoder.raw_decode(s)
    end = WHITESPACE.match(s, end).end()
    return obj, s[end:]


def list_duplicates(seq):
    tally = defaultdict(list)
    for i,item in enumerate(seq):
        tally[item].append(i)
    return list(((key,locs) for key,locs in tally.items() if len(locs)>1))
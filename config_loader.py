import json
import sys

def load_config(config_file="config.json"):
    """Load the configuration from Json file.
    
    Parameters:
    config_file (str): Path to config file.
    
    Returns:
    dict: Configuration dictionary

    """
    try:
        with open(config_file, 'r') as f:
            config = json.load(f)
            
        #Validate required keys
        required_keys = ['files', 'cleaning_options']
        
        for key in required_keys:
            if key not in config:
                raise KeyError(f"Missing required config key: {key}")
            
        #Validate files section
        if 'input_files' not in config['files']:
            raise ValueError("Missing 'input_files' in 'files' section of config") 
        if 'output_file' not in config['files']:
            raise ValueError("Missing 'output_file' in 'files' section of config")
        
        
        #Validate cleaning options
        if 'duplicate_column' not in config['cleaning_options']:
            raise ValueError("Missing 'duplicate_column' in 'cleaning_options' config")
        
        return config
    
    except FileNotFoundError:
        print(f"❌ ERROR: Configuration file '{config_file}' not found.")
        print()
        print("Creating default config.json...")
        create_default_config(config_file)
        print(f"✅ Default configuration file created at '{config_file}'.")
        print("Please edit it in your system and run the program again.")
        sys.exit(1)
    
    except json.JSONDecodeError as e:
        print(f"❌  ERROR: Invalid JSON format in config file: ")
        print(f"    {e}")
        print()
        print("Check your config.json for syntax errors. ")
        print("   - Missing commas")
        print("   - Mismatched braces")
        print("   - Incorrect quotations")
        sys.exit(1)
        
    except ValueError as e:
        print(f"❌ ERROR: Configuration error: ")
        print(f"   {e}")
        sys.exit(1)
          
def create_default_config(config_file):
    """Create a default configuration file.
    
    Parameters:
    config_file (str): Path to config file.
    
    Returns:
    None (creates file in place)
    
    """
    default_config = {
        "files": {
            "input_files": [
                "data_files/loyalty_file_1.xlsx",
                "data_files/loyalty_file_2.xlsx",
                "data_files/loyalty_file_3.xlsx"
            ],
            "output_file": "data_files/cleaned_loyalty_data.xlsx"
        },
        "cleaning_options": {
            "duplicate_column": "Email",
            "date_columns": ["Birthday", "JoinDate"],
            "phone_columns": ["Phone"]
        }
    }
    
    with open(config_file, 'w') as f:
        json.dump(default_config, f, indent=4)
    
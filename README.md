# InfluxDB-Matplotlib-Tutorial
The project outlines how you can use influxdb to store time series data, retrieve it and create visualizations using matplotlib.


## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install packages.

```bash
pip install matplotlib
```

## Usage
```bash
# Create a directory
mkdir influxDB-Tutorial

# Navigate into the folder
cd influxDB-Tutorial

# To create a virtual environment
pip install venv

# Activate virtual environment
source venv/Scripts/activate

# Install influxDB client
pip install influxdb-client

# Create a file known as named __init__.py
touch __init__.py

# Create a file known as named .env to store credentials
touch .env

# Create .gitignore file to prevent .env going public
touch .gitignore
# Install python-dotenv to allow access to the .env file
pip install python-dotenv

# Create folders for storing data and img

mkdir data
mkdir img
# Install yfinance to Collect data
pip install yfinance

# Install matplotlib
pip install matplotlib

# when done deactivate the virtual environment 

deactivate

```
## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License
[MIT](https://choosealicense.com/licenses/mit/)
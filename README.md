# COVID-19 Data Scraper

This Python script scrapes COVID-19 data from the Worldometers website and generates a JSON file containing daily cases and deaths data for various countries. The script utilizes web scraping techniques to extract relevant data from the website's HTML content.

## Table of Contents

- [Getting Started](#getting-started)
- [Prerequisites](#prerequisites)
- [Usage](#usage)
- [Output](#output)
- [Contributing](#contributing)
- [License](#license)

## Getting Started

To get started with this script, follow the steps outlined below.

### Prerequisites

Before running the script, make sure you have the following prerequisites:

- Python 3.x
- Required Python packages: numpy, pandas, requests, BeautifulSoup (bs4)

You can install the required packages using the following command:

```bash
pip install numpy pandas requests beautifulsoup4
```

### Usage

1. Clone this repository to your local machine:

```bash
git clone https://github.com/supun156/covid_19_data_scrapping.git
```

2. Navigate to the repository directory:

```bash
cd covid19-data-scraper
```

3. Run the script:

```bash
python scraper.py
```

The script will extract COVID-19 data for various countries from the Worldometers website and generate a JSON file named \`covid19.json\` containing the data.

## Output

The generated JSON file \`covid19.json\` will contain a dictionary with country names as keys and their corresponding COVID-19 data as values. Each country's data includes daily cases and deaths information.

Here's an example structure of the JSON file:

```json
{
  "usa": {
    "cases_daily": [
      {"date": "2020-01-22", "count": "0"},
      {"date": "2020-01-23", "count": "0"},
      ...
    ],
    "deaths_daily": [
      {"date": "2020-01-22", "count": "0"},
      {"date": "2020-01-23", "count": "0"},
      ...
    ]
  },
  "canada": {
    ...
  },
  ...
}
```

## Contributing

Contributions are welcome! If you have any ideas, suggestions, or bug reports, please create an issue or submit a pull request.

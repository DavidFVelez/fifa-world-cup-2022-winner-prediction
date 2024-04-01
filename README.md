# World Cup Winner Prediction Project

This project aimed to predict the winner and runner-up of the 2022 FIFA World Cup in Qatar using data analysis techniques. The prediction was made by considering the historical goal-scoring strengths of teams across previous World Cup tournaments and employing a Poisson model for analysis.

## Data Collection

The data collection process involved web scraping techniques to gather relevant information from various sources:

1. **beautifulsoup_scraping.py**: This script was used for exploratory web scraping and generated the `cups_history.csv` file.
2. **selenium_scraping.py**: This script utilized the Selenium library to scrape data from websites, resulting in the `fifa_cups.csv` file containing match data from the World Cup tournaments.

## Data Preprocessing

The collected data underwent cleaning and preprocessing steps:

1. **data_cleaning_preparation.ipynb**: This Jupyter Notebook was used for data cleaning, preparation, and transformation tasks, generating the `clean_data.csv` file.

## Model Development and Prediction

1. **requirements.txt**: This file lists the Python package dependencies required for running the project.
2. **winner_prediction.ipynb**: This Jupyter Notebook contains the code for developing the Poisson model, performing analysis, and generating predictions for the winner and runner-up of the 2022 FIFA World Cup in Qatar.

## Usage

To run this project, follow these steps:

1. Clone the repository to your local machine.
2. Install the required Python packages listed in `requirements.txt`.
3. Execute the scripts and notebooks in the following order:
   - `beautifulsoup_scraping.py`
   - `selenium_scraping.py`
   - `data_cleaning_preparation.ipynb`
   - `winner_prediction.ipynb`

## Contributing

Contributions to this project are welcome. If you find any issues or have suggestions for improvements, please open an issue or submit a pull request.

## Acknowledgments

- [Beautiful Soup](https://www.crummy.com/software/BeautifulSoup/) for web scraping
- [Selenium](https://www.selenium.dev/) for web scraping
- [Pandas](https://pandas.pydata.org/) for data manipulation and analysis
- [NumPy](https://numpy.org/) for numerical computing
- [Scikit-learn](https://scikit-learn.org/) for machine learning models

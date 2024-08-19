# Registro Civil Costa Rica Data Mining

## Overview

This project involves the analysis and data mining of records from the Registro Civil of Costa Rica. The goal is to extract valuable insights and trends from civil registration data, including births, marriages, and deaths. The analysis aims to uncover patterns and correlations that can be useful for demographic studies, public policy formulation, and historical research.

## Features

- **Data Collection**: Aggregation of civil registry data from official sources, covering key events such as births, marriages, and deaths.
- **Data Cleaning**: Preprocessing the data to handle missing values, inconsistencies, and errors commonly found in large datasets.
- **Exploratory Data Analysis (EDA)**: Initial analysis to explore the dataset, identify trends, and generate hypotheses.
- **Pattern Recognition**: Use of data mining techniques to discover patterns and correlations in the data, such as seasonality in births or trends in marriage rates.
- **Visualization**: Creation of visual representations of the data to make findings more accessible and understandable.

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/Gaboelc/Registro-civil-costa-rica-data-mining.git
    cd Registro-civil-costa-rica-data-mining
    ```

2. Create and activate a virtual environment:
    ```bash
    python3 -m venv venv
    source venv/bin/activate
    ```

3. Install the required packages:
    ```bash
    pip install -r requirements.txt
    ```

## Usage

1. **Data Preparation**: Start by running the `data_preparation.ipynb` notebook to clean and preprocess the raw data.

2. **Exploratory Data Analysis**: Use the `EDA.ipynb` notebook to explore the data, generate descriptive statistics, and create initial visualizations.

3. **Data Mining**: Run the `data_mining.ipynb` notebook to apply various data mining techniques, such as clustering, association rule mining, and time-series analysis.

4. **Visualization and Reporting**: Use the `visualization.ipynb` notebook to generate detailed visualizations of the mined data, and compile a report summarizing the findings.

## Datasets

The datasets analyzed in this project are stored in the `data/` directory. These include records from the Registro Civil de Costa Rica, detailing key civil events across different regions and time periods.

## Results

- The data mining process revealed significant trends in civil registrations, including seasonality in birth rates and shifts in marriage patterns over time.
- Detailed results and visualizations are included in the notebooks and final report.

## Contributing

Contributions are welcome! Please follow these steps:
1. Fork the repository.
2. Create a new branch (`git checkout -b feature-branch`).
3. Commit your changes (`git commit -am 'Add new feature'`).
4. Push to the branch (`git push origin feature-branch`).
5. Create a new Pull Request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- Data sourced from the Registro Civil de Costa Rica.
- Special thanks to the open-source community for the data analysis tools and libraries used in this project.

## Contact

For any questions or inquiries, please reach out via the repository's issue tracker.

# Credit Score Prediction DSO17/2024-25 MUHAMMAD NOMAN BAIG

## Overview

This project utilizes machine learning to predict credit scores based on user-provided information. It's designed to evaluate the potential risk posed by lending money to consumers and to mitigate losses due to bad debt. The application is built using [Streamlit](https://www.streamlit.io/) and includes features such as profile selection, input sliders, and radio buttons to simulate user input.

Project Deployed on Streamlit:

## Installation and Usage

### Prerequisites

- Python 3.6 or later
- Streamlit
- pandas
- seaborn
- matplotlib
- joblib
- scikit-learn

### Setup

1. Clone the repository to your local machine:

    ```bash
    git clone https://github.com/nomanbaig98/CreditScorePrediction
    ```



2.Install the required dependencies:

    ```bash
    pip install -r requirements.txt
    ```

### Run the Application

1. Execute the following command in the terminal:

    ```bash
    streamlit run Apps/newapp.py
    ```

2. Open your web browser and go to the provided URL (typically http://localhost:8501).

3. Use the application to select a profile and input various parameters to predict and analyze credit scores.

## Project Structure

- **Apps/newapp.py**: Streamlit application script containing the main functionality.
- **src/transform_resp.py**: Module for transforming user inputs.
- **model.pkl**: Pre-trained machine learning model (serialized using joblib).
- **requirements.txt**: List of project dependencies.


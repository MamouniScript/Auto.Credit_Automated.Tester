# Automated Web Interaction Script

## Introduction

This script automates interactions with a specific website, Crédit_Auto. It is designed to test sign-in functionality, simulate interest rates for a car loan while respecting specific conditions, and perform a log-out action.

The script includes two scenarios:

1. **Positive Scenario:** Successfully fills out a form with correct values and handles the success alert. This scenario is followed by a page refresh.

2. **Negative Scenario:** Attempts to submit the form with incorrect values, triggers an error alert, and prints the error message. This scenario is followed by a page refresh.

## Prerequisites

Before running the script, ensure you have the following:

- **Access to the Website:** If you have access to the Crédit_Auto website, please update the following parameters in the script:
  - `url`: The URL of the Crédit_Auto website.
  - `username`: Your username for logging in.
  - `password`: Your password for logging in.

- **Edge Browser:** The script uses the Edge browser. If you don't have it installed, download and install it from the official [Microsoft Edge website](https://www.microsoft.com/en-us/edge).

- **EdgeDriver Path:** Specify the path to the EdgeDriver executable (`edgedriver_path`) in the script. Make sure it matches the version of your Edge browser.

- **Edge Options Binary Location:** Update `edge_options.binary_location` in the script with the correct path to your Edge browser executable.

## Usage

1. Ensure you have Selenium installed. If not, install it using:

    pip install selenium

2. Update the script with your credentials and paths as mentioned in the Prerequisites section.
3. Run the script using a Python interpreter.

    python auto.py

4. Observe the automated interactions with the Crédit_Auto website.

## Notes

- The script may require adjustments based on changes to the Crédit_Auto website structure or elements.

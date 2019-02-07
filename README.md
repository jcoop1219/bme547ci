# Unit Testing & Continuous Integration Assignment
Developed by Jason Cooper

## Usage Instructions
1. Gain access this repository. You can either do this by:
   * Downloading the latest release from the [releases page](https://github.com/jcoop1219/bme547ci/releases) and navigating to it in your Git Bash terminal
   * Cloning this repository onto your local machine and navigating to it in your Git Bash terminal.
     Copy/Paste: `https://github.com/jcoop1219/bme547ci.git`
1. Create a virtual environment with the required packages in the `envRequirements.txt` file.
   * **Important:** `tachycardia.py` relies on Levenshtein distance calculation functionality from the [python-Levenshtein package](https://pypi.org/project/python-Levenshtein/), so installing this package is required.
1. Activate your virtual environment.
1. Enter the following command into the command line of the terminal: `python tachycardia.py`
1. Enter a string which you would like to check against the string `tachycardic`.
1. The module will return whether or not the entered string matches on `tachycardic`. Close enough representations of the word (1-2 letters added, missing, or substituted) still count as matching.

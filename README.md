# model-training-cookie

![CI](https://github.com/remla23-team10/model-training/actions/workflows/continous-integration.yaml/badge.svg)

Repo for training the model

<p><small>Project based on the <a target="_blank" href="https://drivendata.github.io/cookiecutter-data-science/">cookiecutter data science project template</a>.</small></p>

## Usage

Clone the repo and `cd` into it.

### Training
1. Activate the virtual environment

    ```bash
    source venv/bin/activate
    ```
2. Install the requirements

    ```bash
    pip install -r requirements.txt
    ```
3. Reproduce the training. This will download the data, preprocess it, train the model and save it in the `models` folder as `Classifier_Sentiment_Model.joblib`

    ```bash
    dvc repro
    ```

### Backing up artifacts to Google Drive

1. Activate the virtual environment
2. Attain access to the Google Drive folder
3. Run `dvc pull` to initiate the authorization process. This will open a browser window where you can authorize the app to access your Google Drive folder.
4. Run `dvc repro` and `dvc push` to push the artifacts to the Google Drive folder. 

### Running tests
To run the unit tests for this project, run `pytest` in the root folder.


## Project Organization

    ├── .dvc               <- DVC files
    |
    ├── .github            <- Github actions
    |   └── workflows      <- Github workflow that add pylint and dslinter checks
    |
    ├── .venv              <- Virtual environment for the project
    |
    ├── data
    │   ├── external       <- Dataset from online third party source.
    │   ├── interim        <- Intermediate data that has been transformed.
    │   ├── processed      <- The dataset after preprocessing.
    │   └── raw            <- The original, immutable data dump.
    │
    ├── docs               <- A default Sphinx project; 
    │
    ├── models             <- Trained models
    │   └── metrics        <- Metrics for model evaluation
    │
    ├── notebooks          <- Jupyter notebooks. 
    │
    ├── references         <- Data dictionaries, manuals, and all other explanatory materials.
    │
    ├── reports            <- Generated analysis as HTML, PDF, LaTeX, etc.
    │   └── figures        <- Generated graphics and figures to be used in reporting
    │
    ├── src                <- Source code for use in this project.
    │   │
    │   ├── data           <- Scripts to download dataset from externals ource
    │   │
    │   ├── features       <- Script to preprocess the data
    │   │
    │   ├── models         <- Scripts to train models and then use trained models to make
    │   │                     predictions
    │   │
    │   └── visualization  <- Scripts to create exploratory and results oriented visualizations


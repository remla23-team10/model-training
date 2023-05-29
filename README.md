# model-training-cookie

Repo for training the model

## Usage

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
4. Return to the terminal. Run `dvc push` after `dvc repro` to push the artifacts to the Google Drive folder. 

## Project Organization

    ├── LICENSE
    ├── Makefile           <- Makefile with commands like `make data` or `make train`
    ├── README.md          <- The top-level README for developers using this project.
    ├── data
    │   ├── external       <- Dataset from online third party source.
    │   ├── interim        <- Intermediate data that has been transformed.
    │   ├── processed      <- The dataset after preprocessing.
    │   └── raw            <- The original, immutable data dump.
    │
    ├── docs               <- A default Sphinx project; see sphinx-doc.org for details
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
    ├── requirements.txt   <- The requirements file for reproducing the analysis environment, e.g.
    │                         generated with `pip freeze > requirements.txt`
    │
    ├── setup.py           <- makes project pip installable (pip install -e .) so src can be imported
    ├── src                <- Source code for use in this project.
    │   ├── __init__.py    <- Makes src a Python module
    │   │
    │   ├── data           <- Scripts to download or generate data
    │   │   └── make_dataset.py
    │   │
    │   ├── features       <- Scripts to turn raw data into features for modeling
    │   │   └── build_features.py
    │   │
    │   ├── models         <- Scripts to train models and then use trained models to make
    │   │   │                 predictions
    │   │   ├── predict_model.py
    │   │   └── train_model.py
    │   │
    │   └── visualization  <- Scripts to create exploratory and results oriented visualizations
    │       └── visualize.py
    │
    ├── tox.ini            <- tox file with settings for running tox; see tox.readthedocs.io
    |
    └── venv               <- Virtual environment for the project


--------

<p><small>Project based on the <a target="_blank" href="https://drivendata.github.io/cookiecutter-data-science/">cookiecutter data science project template</a>. #cookiecutterdatascience</small></p>

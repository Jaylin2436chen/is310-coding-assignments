# National Park Visits EDA

This folder contains a Jupyter notebook that explores the U.S. National Park visit dataset from [Responsible Datasets in Context](https://www.responsible-datasets-in-context.com/posts/np-data/). It checks the dataset's rows, columns, data types, summary statistics, and number of records per park. It also creates an interactive Altair line chart comparing yearly recreation visit counts for the five parks with the highest counts in 2024.

## Run the notebook

1. Open a terminal in this folder.
2. Install the listed packages in the Python environment you plan to use for the notebook:

   ```bash
   python3 -m pip install -r requirements.txt
   ```

3. Start Jupyter with `jupyter notebook` or `jupyter lab`.
4. Open `national_park_visits_eda.ipynb`, select the same Python environment as its kernel, and run the cells from top to bottom.

The notebook reads the CSV directly from its public source, so an internet connection is needed when running it.
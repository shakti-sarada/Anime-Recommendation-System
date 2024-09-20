# Anime Recommendation System

This project is an Anime Recommendation System that uses data from a Kaggle dataset and presents a user-friendly interface through Streamlit. Follow the instructions below to set up the project and get it running on your local machine.

## Prerequisites

- Python 3.8+ installed on your system.
- A Kaggle account to download the dataset.

## Steps to Set Up and Run the Anime Recommendation System

### 1. Download the Anime Dataset
You will first need to download the anime dataset from Kaggle.

- Visit [Kaggle Anime Dataset 2024](https://www.kaggle.com/datasets/junaidk0012/anime-dataset-2024).
- Download the dataset as a `.csv` file.
- Create a folder named `data` inside your project directory.
- Move the downloaded dataset into the `data` folder.

### 2. Preprocess the Data and Generate Artifacts
Next, you need to preprocess the dataset to create the necessary pickle files for the recommendation system. The code for this is provided in a Jupyter notebook.

- Open the `.ipynb` file provided in the project.
- Run all cells to preprocess the dataset.
- The preprocessing will generate `.pkl` files (serialized objects).
- Create an `artifacts` folder inside your project directory.
- Save all generated `.pkl` files in the `artifacts` folder.

### 3. Install Required Libraries
Before running the application, ensure you have all the required dependencies.

- Open a terminal or command prompt.
- Navigate to your project directory.
- Run the following command to install all required libraries:

  ```bash
  pip install -r requirements.txt
  ```

### 4. Run the Application
Now that you have the dataset and necessary files ready, you can start the Streamlit app.

- In your terminal or command prompt, navigate to your project directory.
- Run the following command to launch the app:

  ```bash
  streamlit run app.py
  ```

### 5. Access the Application
After running the above command, Streamlit will launch a web server. Open your browser and visit the URL (usually `http://localhost:8501`) provided in the terminal to access the Anime Recommendation System interface.

---

## Project Structure
```
Anime-Recommendation-System/
│
├── data/
│   └── anime_dataset.csv         # Downloaded dataset
│
├── artifacts/
│   └── *.pkl                     # Preprocessed artifacts (generated after running the notebook)
│
├── app.py                        # Main Streamlit app
├── requirements.txt              # Required Python libraries
└── preprocess.ipynb              # Notebook to preprocess data and create artifacts
```

## Troubleshooting
- Ensure you have the correct version of Python and all required libraries installed.
- Make sure the paths to the `data` and `artifacts` folders are correct and files are in the right location.

## License
This project is licensed under the MIT License.

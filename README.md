# ML Project: House Price Prediction

This project aims to build a machine learning pipeline to predict house prices based on various features such as area, number of bedrooms, bathrooms, stories, and more. The pipeline includes data ingestion, data transformation, model training, and prediction components.

## Project Structure
```
.github/
    workflows/
.gitignore
application.py
artifacts/
    data.csv
    model.pkl
    preprocessor.pkl
    test.csv
    train.csv
catboost_info/
    catboost_training.json
    learn/
    learn_error.tsv
    time_left.tsv
    tmp/
Dockerfile
logs/
    ...
MLproject.egg-info/
    ...
README.md
requirements.txt
setup.py
src/
    components/
        data_ingestion.py
        data_transformation.py
        model_trainer.py
        predict_pipeline.py
    ...
templates/
    ...
venv/
```


## Components

### Data Ingestion

The data ingestion component reads the dataset, splits it into training and testing sets, and saves them as CSV files.

- **File:** file://MLproject/src/components/data_ingestion.py
- **Class:** [`DataIngestion`](command:_github.copilot.openSymbolInFile?%5B%7B%22scheme%22%3A%22file%22%2C%22authority%22%3A%22%22%2C%22path%22%3A%22%2FC%3A%2FUsers%2FAsus%2FDocuments%2FAcademic%2FMachine%20Learning%2FMLproject%2Fsrc%2Fcomponents%2Fdata_ingestion.py%22%2C%22query%22%3A%22%22%2C%22fragment%22%3A%22%22%7D%2C%22DataIngestion%22%2C%2204faac14-55bf-4525-b521-22bc821329e9%22%5D "c:\Users\Asus\Documents\Academic\Machine Learning\MLproject\src\components\data_ingestion.py")
- **Method:** [`initiate_data_ingestion`](command:_github.copilot.openSymbolFromReferences?%5B%22%22%2C%5B%7B%22uri%22%3A%7B%22scheme%22%3A%22file%22%2C%22authority%22%3A%22%22%2C%22path%22%3A%22%2FC%3A%2FUsers%2FAsus%2FDocuments%2FAcademic%2FMachine%20Learning%2FMLproject%2Fsrc%2Fcomponents%2Fdata_ingestion.py%22%2C%22query%22%3A%22%22%2C%22fragment%22%3A%22%22%7D%2C%22pos%22%3A%7B%22line%22%3A24%2C%22character%22%3A8%7D%7D%5D%2C%2204faac14-55bf-4525-b521-22bc821329e9%22%5D "Go to definition")

### Data Transformation

The data transformation component preprocesses the data, including handling missing values, scaling numerical features, and encoding categorical features.

- **File:** file://MLproject/src/components/data_transformation.py
- **Class:** [`DataTransformation`](command:_github.copilot.openSymbolInFile?%5B%7B%22scheme%22%3A%22file%22%2C%22authority%22%3A%22%22%2C%22path%22%3A%22%2FC%3A%2FUsers%2FAsus%2FDocuments%2FAcademic%2FMachine%20Learning%2FMLproject%2Fsrc%2Fcomponents%2Fdata_transformation.py%22%2C%22query%22%3A%22%22%2C%22fragment%22%3A%22%22%7D%2C%22DataTransformation%22%2C%2204faac14-55bf-4525-b521-22bc821329e9%22%5D "c:\Users\Asus\Documents\Academic\Machine Learning\MLproject\src\components\data_transformation.py")
- **Method:** [`initiate_data_transformation`](command:_github.copilot.openSymbolFromReferences?%5B%22%22%2C%5B%7B%22uri%22%3A%7B%22scheme%22%3A%22file%22%2C%22authority%22%3A%22%22%2C%22path%22%3A%22%2FC%3A%2FUsers%2FAsus%2FDocuments%2FAcademic%2FMachine%20Learning%2FMLproject%2Fsrc%2Fcomponents%2Fdata_ingestion.py%22%2C%22query%22%3A%22%22%2C%22fragment%22%3A%22%22%7D%2C%22pos%22%3A%7B%22line%22%3A56%2C%22character%22%3A45%7D%7D%2C%7B%22uri%22%3A%7B%22scheme%22%3A%22file%22%2C%22authority%22%3A%22%22%2C%22path%22%3A%22%2Fc%3A%2FUsers%2FAsus%2FDocuments%2FAcademic%2FMachine%20Learning%2FMLproject%2Fsrc%2Fcomponents%2Fdata_transformation.py%22%2C%22query%22%3A%22%22%2C%22fragment%22%3A%22%22%7D%2C%22pos%22%3A%7B%22line%22%3A66%2C%22character%22%3A8%7D%7D%5D%2C%2204faac14-55bf-4525-b521-22bc821329e9%22%5D "Go to definition")

### Model Training

The model training component trains multiple regression models and selects the best one based on performance metrics.

- **File:** file://MLproject/src/components/model_trainer.py
- **Class:** [`ModelTrainer`](command:_github.copilot.openSymbolInFile?%5B%7B%22scheme%22%3A%22file%22%2C%22authority%22%3A%22%22%2C%22path%22%3A%22%2FC%3A%2FUsers%2FAsus%2FDocuments%2FAcademic%2FMachine%20Learning%2FMLproject%2Fsrc%2Fcomponents%2Fmodel_trainer.py%22%2C%22query%22%3A%22%22%2C%22fragment%22%3A%22%22%7D%2C%22ModelTrainer%22%2C%2204faac14-55bf-4525-b521-22bc821329e9%22%5D "c:\Users\Asus\Documents\Academic\Machine Learning\MLproject\src\components\model_trainer.py")
- **Method:** [`initiate_model_trainer`](command:_github.copilot.openSymbolFromReferences?%5B%22%22%2C%5B%7B%22uri%22%3A%7B%22scheme%22%3A%22file%22%2C%22authority%22%3A%22%22%2C%22path%22%3A%22%2FC%3A%2FUsers%2FAsus%2FDocuments%2FAcademic%2FMachine%20Learning%2FMLproject%2Fsrc%2Fcomponents%2Fdata_ingestion.py%22%2C%22query%22%3A%22%22%2C%22fragment%22%3A%22%22%7D%2C%22pos%22%3A%7B%22line%22%3A59%2C%22character%22%3A23%7D%7D%2C%7B%22uri%22%3A%7B%22scheme%22%3A%22file%22%2C%22authority%22%3A%22%22%2C%22path%22%3A%22%2Fc%3A%2FUsers%2FAsus%2FDocuments%2FAcademic%2FMachine%20Learning%2FMLproject%2Fsrc%2Fcomponents%2Fmodel_trainer.py%22%2C%22query%22%3A%22%22%2C%22fragment%22%3A%22%22%7D%2C%22pos%22%3A%7B%22line%22%3A30%2C%22character%22%3A8%7D%7D%5D%2C%2204faac14-55bf-4525-b521-22bc821329e9%22%5D "Go to definition")

### Prediction Pipeline

The prediction pipeline component loads the trained model and preprocessor to make predictions on new data.

- **File:** file://MLproject/src/pipeline/predict_pipeline.py
- **Class:** [`PredictPipeline`](command:_github.copilot.openSymbolInFile?%5B%7B%22scheme%22%3A%22file%22%2C%22authority%22%3A%22%22%2C%22path%22%3A%22%2FC%3A%2FUsers%2FAsus%2FDocuments%2FAcademic%2FMachine%20Learning%2FMLproject%2Fsrc%2Fpipeline%2Fpredict_pipeline.py%22%2C%22query%22%3A%22%22%2C%22fragment%22%3A%22%22%7D%2C%22PredictPipeline%22%2C%2204faac14-55bf-4525-b521-22bc821329e9%22%5D "c:\Users\Asus\Documents\Academic\Machine Learning\MLproject\src\pipeline\predict_pipeline.py")
- **Method:** [`predict`](command:_github.copilot.openSymbolFromReferences?%5B%22%22%2C%5B%7B%22uri%22%3A%7B%22scheme%22%3A%22file%22%2C%22authority%22%3A%22%22%2C%22path%22%3A%22%2Fc%3A%2FUsers%2FAsus%2FDocuments%2FAcademic%2FMachine%20Learning%2FMLproject%2Fsrc%2Fpipeline%2Fpredict_pipeline.py%22%2C%22query%22%3A%22%22%2C%22fragment%22%3A%22%22%7D%2C%22pos%22%3A%7B%22line%22%3A11%2C%22character%22%3A8%7D%7D%2C%7B%22uri%22%3A%7B%22scheme%22%3A%22file%22%2C%22authority%22%3A%22%22%2C%22path%22%3A%22%2Fc%3A%2FUsers%2FAsus%2FDocuments%2FAcademic%2FMachine%20Learning%2FMLproject%2Fsrc%2Fcomponents%2Fmodel_trainer.py%22%2C%22query%22%3A%22%22%2C%22fragment%22%3A%22%22%7D%2C%22pos%22%3A%7B%22line%22%3A108%2C%22character%22%3A33%7D%7D%5D%2C%2204faac14-55bf-4525-b521-22bc821329e9%22%5D "Go to definition")

## How to Run

1. **Install Dependencies:**
   ```sh
   pip install -r requirements.txt
2. **Run the Application:**
   ```sh
   python application.py

## Logging

Logs are stored in the file://MLproject/logs/ directory, capturing various stages of the pipeline execution.

## Configuration

Configuration settings for data paths and model parameters are defined using dataclasses in the respective components.

## Deployment

To deploy the house price prediction model, follow these steps:

1. **Build the Docker Image:**
   Ensure you have Docker installed. Navigate to the project directory and build the Docker image using the provided Dockerfile.
   ```sh
   docker build -t house-price-prediction:latest .

2. **Run the Docker Container:**
   Once the image is built, run the container.
   ```sh
   docker run -p 5000:5000 house-price-prediction:latest

3. **Access the Application:**
   The application will be accessible at `http://localhost:5000`. You can use this endpoint to make predictions by sending a POST request with the required features.

4. **Environment Variables:**
   Ensure to set any necessary environment variables for configuration, such as database connections or API keys, if applicable.

5. **Logging and Monitoring:**
   Logs are stored in the `logs/` directory within the container. You can mount this directory to your host machine for easier access and monitoring.

6. **Scaling:**
   For scaling the application, consider using orchestration tools like Kubernetes or Docker Swarm. Define the necessary deployment configurations and services to manage multiple instances of the application.

7. **CI/CD Pipeline:**
   Set up a CI/CD pipeline using GitHub Actions or any other CI/CD tool to automate the build, test, and deployment process. Ensure to include steps for running unit tests, building the Docker image, and deploying to your chosen environment.

By following these steps, you can deploy the house price prediction model and make it accessible for real-time predictions..


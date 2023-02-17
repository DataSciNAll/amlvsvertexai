# Azure-ML-vs-GCP Vertex AI

## Overview
In this tutorial, you will go through various ways of importing, transforming, analyzing, and exporting data with Vertex AI. This tutorial will walk you through the Vertex AI Console. 

This Compete collection includes the following:
- AutoML tutorial
- Custom model training and deployment tutorial


<!-- HACK #1 -->
## Hack #1: Training a classification model with Vertex AI AutoML

### Step 0: Before You Start 
* GCP Account - Sign up for a free GCP account here

### Step 1: Create a project and enable the Needed API's 
* Create a new project (Manage Resources -> Create Project)
* Enable the following API's Vertex API (APIs & Services -> +Enable APIs and Services -> Search)

 * Vertex AI API
 * Cloud Storage API

### Setup the rest of the environment
* Follow Step 5 - Step 7 -> https://cloud.google.com/vertex-ai/docs/tutorials/tabular-automl/setup 

### Step 2: Upload Dataset + Analyze 
* Navigate to Vertex AI within the GoogleCloud platform. (Click on the Navigation Menu -> Artificial Intelligence -> Vertex AI)
* Go to Datasets -> Create -> Tabular -> Regression/Classification -> Upload CSV file from computer -> Select a Cloud Storage Path -> Create.
* View dataset and what values may be missing.

### Step 3: Training 
* Training -> Train new model -> AutoML -> Choose Target Col -> Select Compute and pricing -> Start Training

### Step 4: Deploy + Test
* Model Registry -> Model -> Version -> Deploy & Test -> Deploy to endpoint
* Test your model -> Enter values -> Predict


<!-- HACK #2 -->
## Hack #2: Training a classification model with Vertex AI Custom Training
This tutorial borrows from [Vertex AI: Custom training job and prediction using managed datasets](https://codelabs.developers.google.com/codelabs/vertex-ai-custom-code-training#0) with some changes made. It uses prebuilt scikit-learn containers to train and deploy a custom model based on Titanic survival data.

We recommend following the steps in that tutorial and referencing the notes listed here for the respective steps.

Following this tutorial will cost less than $5 to run, provided that you delete resources afterwards.

**Step 1: Overview**
- Ensure the following services are enabled, using [the Console UI or gcloud shell](https://cloud.google.com/endpoints/docs/openapi/enable-api#console):
  - Vertex AI API
  - Cloud Storage API
  - Compute Engine API
  - Artifact Registry API

**Step 2: Setup your environment**:
- The tutorial's written instructions can be skipped since we will be uploading data into Google Cloud Storage instead of BigQuery.
- Instead do the following:
  - Download `titanic.csv` in this repository and [upload into a Google Cloud Storage Bucket](https://cloud.google.com/storage/docs/uploading-objects#:~:text=Uploading%20Files%20to%20Google%20Cloud%201%20Open%20the,you%20are%20using%20the%20Chrome%20...%20See%20More.).
  - Create a folder, `model` nested under `artifacts` in the Notebook's Terminal:

      ```
      mkdir titanic/trainer/artifacts/model
      ```

**Step 3: Create a dataset**
- Select datasource: Choose `Select CSV files from Cloud Storage`.


**Step 4: Custom training package using Notebooks**
- Create a **user-managed notebook** in Vertex AI Workbench. The region does not matter.
- Copy the code provided in this repository under `custom-model/trainer/task.py`
- Paste code into your `task.py` file in your Notebook environment.
- Test the program locally before building your package. Here is an example of user input. Replace the `model_dir`, `training_data_uri`, and `test_data_uri` arguments with your own paths.

  ```
  python -m trainer.task -v \
      --model_param_kernel=linear \
      --model_dir="gs://my-bucket/titanic/trial" \
      --data_format=csv\
      --training_data_uri="gs://my-bucket/titanic/titanic.csv" \
      --test_data_uri="gs://my-bucket/titanic/titanic.csv"" \
      --validation_data_uri="gs://my-bucket/titanic/titanic.csv""
  ```

**Step 5: Model Training**:
- Step 0: Training region does not matter.
- Step 3:
  - **BigQuery project for exporting data** can be the Cloud Storage Bucket hosting your training data
  - **Model output directory**: select the directory `artifacts` if your folder structure is the same as defined in earlier steps. 
  
    The training job will automatically look within that directory for a `model` folder that stores your `model.pkl` and `report.txt` files. 
  - Copy and paste these arguments into the UI, replacing the text with your respective paths. The training job will pass these to `task.py` as you tested locally in the previous step.
  
    Notice how the `--model_dir` argument specifies that the outputs are saved in `artifacts/model` folder.

    ```
    --model_param_kernel=linear
    --model_dir="gs://my-bucket/titanic/artifacts/model"
    --data_format=csv
    --training_data_uri="gs://my-bucket/titanic/titanic.csv"
    --test_data_uri="gs://my-bucket/titanic/titanic.csv"
    --validation_data_uri="gs://my-bucket/titanic/titanic.csv"
    ```
- Training should take about 5-7 minutes.

**Steps 6-9**: Same as tutorial.


## Appendix
### Authors
- Devanshi Thakar, Cloud Solution Architect
- Amanda Wong, Cloud Solution Architect

### Related Compete Hacks
[Azure ML vs AWS Sagemaker](https://github.com/DataSciNAll/Azure-ML-vs-AWS-SageMaker-)

### Reference material

- [Data Engineering Decision Tree](https://towardsdatascience.com/how-to-choose-the-right-google-cloud-platform-database-a223f4d7482f)

- [GCP Machine Learning Best Practices](https://cloud.google.com/architecture/ml-on-gcp-best-practices)

- [Data Transfer Service to BQ](https://cloud.google.com/bigquery/docs/loading-data-cloud-storage-csv)

- [Big Query One-minute](https://cloud.google.com/bigquery/docs/introduction)

- [Intro to Vertex AI](https://cloud.google.com/vertex-ai/docs/beginner/beginners-guide)

- [Intro to AutoML](https://cloud.google.com/vertex-ai/docs/beginner/beginners-guide)

- [Vertex AI + BigQuery](https://cloud.google.com/vertex-ai/docs/beginner/bqml)

- [BigQuery ML](https://cloud.google.com/bigquery-ml/docs/introduction)

- [Feature Store](https://cloud.google.com/vertex-ai/docs/featurestore/overview)

![Ref Arch](https://cloud.google.com/static/vertex-ai/docs/beginner/images/mlops_bq2.png)

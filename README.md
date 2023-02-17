# Azure-ML-vs-GCP Vertex AI

## Overview
---
In this tutorial, you will go through various ways of importing, transforming, analyzing, and exporting data with Vertex AI. This tutorial will walk you through the Vertex AI Console. 

This Compete collection includes the following:
- AutoML tutorial
- Custom model training and deployment tutorial


<!-- HACK #1 -->
## Hack #1: Training a classification model with Vertex AI AutoML
---

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
---
This tutorial borrows from [Vertex AI: Custom training job and prediction using managed datasets](https://codelabs.developers.google.com/codelabs/vertex-ai-custom-code-training#0) with some changes made.

We recommend following the steps in that tutorial and referencing the notes listed here for the respective steps.

Following this tutorial will cost less than $5 to run, provided that you delete resources afterwards.

**Step 1**: Same as tutorial.

**Step 2**: 
- Download `titanic.csv` in this repository and follow ===THESE STEPS=== to upload into a Google Cloud Storage Bucket.
 - Create a folder, `model` nested under `artifacts` in the Terminal: `mkdir titanic/trainer/artifacts/model`.
 
**Step 3**: Same as tutorial.

**Step 4**: 
- Copy and paste the code provided in this repository under `custom-model/trainer/task.py` and paste into your respective task.py file.

**Step 5**:
- Copy and paste these arguments into the UI, replacing the text with your respective arguments.
- Training should take about 5-7 minutes.

**Steps 6-9**: Same as tutorial.


## Related Compete Hacks
---
[Azure ML vs AWS Sagemaker](https://github.com/DataSciNAll/Azure-ML-vs-AWS-SageMaker-)


### Resources

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

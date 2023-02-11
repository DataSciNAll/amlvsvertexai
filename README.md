
# Azure-ML-vs-GCP Vertex AI

## Overview
In this tutorial, you will go through various ways of importing, transforming, analyzing, and exporting data with Vertex AI. This tutorial will walk you through BigQuery and Vertex AI Consoles. Here is a good cheatsheet that outlines the options for data engineering and machine learning options in GCP.


### Research Articles

[Data Engineering Decision Tree](https://towardsdatascience.com/how-to-choose-the-right-google-cloud-platform-database-a223f4d7482f)

[GCP Machine Learning Best Practices](https://cloud.google.com/architecture/ml-on-gcp-best-practices)

[Data Transfer Service to BQ](https://cloud.google.com/bigquery/docs/loading-data-cloud-storage-csv)

[Big Query One-minute](https://cloud.google.com/bigquery/docs/introduction)

[Intro to Vertex AI](https://cloud.google.com/vertex-ai/docs/beginner/beginners-guide)

[Intro to AutoML](https://cloud.google.com/vertex-ai/docs/beginner/beginners-guide)

[Vertex AI + BigQuery](https://cloud.google.com/vertex-ai/docs/beginner/bqml)

[BigQuery ML](https://cloud.google.com/bigquery-ml/docs/introduction)

[Feature Store](https://cloud.google.com/vertex-ai/docs/featurestore/overview)

![Ref Arch](https://cloud.google.com/static/vertex-ai/docs/beginner/images/mlops_bq2.png)

### Data Science Lifecycle from past hacks
1. Storage Tabular Data
2. Feature Engineering
3. Model training -- Respond to a offer for a Fixed Term Deposit from a banking institution (Binary Classification)
4. AutoML -- Quick Build
5. Feature Importance
6. Model Evaluation
7. Model Deployment -- Test use case

### GCP Service in Scope
1. Cloud Storage
1. BQ Data Transfer Service
1. BigQuery
1. BigQuery ML -- AutoML
1. Vertex AI -- AutoML
1. Vertex AI -- Custom Models


<!-- HACK #1 -->
## Training a classification model with Vertex AI AutoML  

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

# Acknowledgements
This code repo has been forked from https://github.com/DataSciNAll/Azure-ML-vs-AWS-SageMaker- Special thanks to Devanshi Thakar and team for sharing their code set and workflows with us.  We hope this gives a good guide to the different features across each platform.


<!-- HACK #2 -->
## Training a classification model with Vertex AI Custom Training 


<!-- DEMO -->
## BigQuery

### Step 0: Before You Start 
* GCP Account - Sign up for a free GCP account here 

### Step 1: Download Dataset and Upload to GCP Storage Account 
* Download Titanic Dataset from the Github page - Grab the .CSV file
* Navigate to GCP portal and type Storage in the Search Bar 
  *  Hit Create a bucket:  Name your bucket and leave all other settings as default.

<!-- ![p1](https://user-images.githubusercontent.com/33441411/164117324-657bf0ce-5a65-4418-b653-0271424d61f2.png) -->

  *  Upload .csv file into the created bucket using the Upload button

### Step 2: Set up Vertex AI
* Navigate to GCP portal and type in Vertex AI
* Create a Vertex AI workbench

<!-- ![p2](https://user-images.githubusercontent.com/33441411/164118649-8be00282-58d8-4edd-9c88-4b32ee6db4ea.png)
![p3](https://user-images.githubusercontent.com/33441411/164118664-d9344532-092b-445b-b422-b143f94b097f.png)
 -->
### Step 3: Get Started with BigQuery
* Hit Launch App -> Studio 

* Create a Data Wrangler Flow by going to File -> New -> Data Wrangler Flow
<!-- ![p5](https://user-images.githubusercontent.com/33441411/164119824-00eb5c9b-5176-4b6b-842e-b4cb557cbead.png)
 -->
* Import S3 Data 
  * Choose your S3 bucket and Click on the .CSV file that you uploaded. You should be able to see a Preview version of your data on the very bottom. Then click Import at the very top.
<!-- ![p6](https://user-images.githubusercontent.com/33441411/164120598-5607027e-9e82-4a5b-b681-9c56907ab660.png)
![p7](https://user-images.githubusercontent.com/33441411/164120605-5c99301a-fd1e-41b9-9a27-a4f0b68674dc.png)
 -->
### Step 4: Begin adding to the Flow
* In the Data Flow, you should just see 2 steps - the data from S3 and the data types. Data Wrangler has inferred the data types for you already.
* Analyze: Now let's start analyzing the data. To get a feel of the data, we can do + Add Analysis. For Analysis Type, click on "Table Summary" from the Drop Down. As you can see from the output, there are many missing values in the columns: cabin, embarked, and home.dest. In addition, there are outliers as well. You can play around with other pre-built Analysis features like creating a Histogram. 
<!-- ![p8](https://user-images.githubusercontent.com/33441411/164122242-d4e9da00-4cfc-4b0c-b17f-a09d64bd0d46.png)
![p9](https://user-images.githubusercontent.com/33441411/164122250-9e468961-b2d9-41f5-b423-b00163fb0bea.png)
 -->
* Transform: Now let's transform the data. This is where you can manipulate the data by cleaning it up. Click on + Add Transform. Then + Add Step on the top right of the screen. 
   * Drop Columns: Now here, we want to select the built in option to drop the columns that are unnecessary. In Transform, we are going to select the Drop column option. And for column's to drop, we will select: cabin, ticket, name, sibsp, parch, home.dest, boat, and body. Then hit preview. And finally, click Add.
<!--    ![p10](https://user-images.githubusercontent.com/33441411/164125305-881e8c1c-f4d6-44bd-8669-f85f1181105b.png)
 -->
   * Missing Data: + Add Step again. Click on the Handle Missing built in option. Under Transform, click on Drop missing. Then for Input columns, select age. Then hit preview. Lastly, click Add.  Repeat this step for the column, fare.

   <!-- ![p11](https://user-images.githubusercontent.com/33441411/164125333-0dd3f095-b68f-4871-a2e9-b82d290691af.png) -->
   
   * Let's take a look at the Custom Tranform option. Select Python(Pandas). Enter this query: df.info(). You will see 1045 entries that are remaining after all the transformations. We do not have to save this. Let's click on Custom transform again. Select Python(Pandas). 
 
 Insert this code:
```
import pandas as pd

dummies = []
cols = ['pclass','sex','embarked']
for col in cols:
    dummies.append(pd.get_dummies(df[col]))
    
encoded = pd.concat(dummies, axis=1)

df = pd.concat((df, encoded),axis=1)

```
Hit preview and click Add. You should see some new columns on the right.

 
  * SQL: Hit Custom Transform again. Click on SQL(PySpark SQL). Here we want to select the columns we want to keep.
    
     Insert this code: 
     ```
     SELECT survived, age, fare, 1, 2, 3, female, male, C, Q, S FROM df;
     ```


* You're done with the Data Flow! Now we want to Export. Let's explore different options by going to +Export. 

### Step 5: Clean up!
* Make sure all and any S3 buckets are deleted!
* In the Studio: On the left, click on Running Terminals and Kernals. Next to Running Apps click on the X. This will close out all your application sessions. I also close all my notebooks.
* Delete all Domain's open for the Studio and Canvas (Part 2)

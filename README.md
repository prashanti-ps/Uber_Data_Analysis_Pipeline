# Uber Data Analysis

The pipeline extracts, transforms and analyzes the TLC Trip Record Data, which includes yellow and green taxi trip records in New York City. The analysis aims to provide insights into the Uber data for informed decision-making and data-driven strategies.

## Data Source  
The primary data source for this project is the TLC Trip Record Data. It includes detailed information about yellow and green taxi trips in New York City. The data comprises fields such as pick-up and drop-off dates/times, locations, trip distances, fares, rate types, payment types, and passenger counts.

The data can be obtained from the NYC TLC (Taxi and Limousine Commission) website - https://www.nyc.gov/site/tlc/about/tlc-trip-record-data.page                    
The data dictionary is available for reference - https://www.nyc.gov/assets/tlc/downloads/pdf/data_dictionary_trip_records_yellow.pdf


## Architechture
The Uber Data Analysis Pipeline follows a modular architecture using various technologies and components:

1. Google Cloud Storage (Datalake): This component serves as the storage layer for storing both raw and processed data.

2. Google Compute Engine (MAGE AI): MAGE, a "Data Transformation and Integration Tool," is utilized for data transformation and integration within the pipeline. It helps streamline the data flow and ensures data consistency and quality.

3. BigQuery (data warehouse): BigQuery is the chosen data warehouse for this project. It stores the processed and transformed data from the pipeline, enabling fast querying and analysis of large datasets.

4. Looker Studio (Visualization): Looker Studio is the visualization tool integrated with the pipeline. It facilitates the creation of interactive dashboards and visualizations based on the data stored in BigQuery. These visualizations aid in better understanding the Uber data and extracting valuable insights.


![244839012-f35f3531-d096-4f86-9261-0c4fac9716b4](https://github.com/prashanti-ps/Uber_Data_Analysis_Pipeline/assets/78148121/be712c3f-ddcd-4500-9157-a90aed20bb9e)



## Dimensional Model
To facilitate efficient querying and analysis, a dimensional model is employed in the data warehouse. The dimensional model includes dimensions like time, location, and passenger, along with fact tables like trips. This model provides a structured framework for organizing and analyzing the Uber data effectively.


![image](https://github.com/prashanti-ps/Uber_Data_Analysis_Pipeline/assets/78148121/7cfa21ed-f376-4000-ae6e-67e1d0ade068)


## Visualization
The project employs Looker Studio as the visualization tool. Looker Studio allows the creation of visually appealing and interactive dashboards based on the data stored in BigQuery. These dashboards provide data engineers with a comprehensive view of the Uber data, enabling them to gain insights, identify patterns, and make informed decisions.

![image](https://github.com/prashanti-ps/Uber_Data_Analysis_Pipeline/assets/78148121/aaf606c1-759f-4a53-87d8-a48a5bd3c511)


## Key Features
The key features of the project are:  

- Data Extraction: The pipeline extracts data from the TLC Trip Record Data, which includes yellow and green taxi trip records in New York City. This ensures a reliable and up-to-date data source for analysis.

- Data Transformation and Integration: The project utilizes MAGE to perform necessary transformations on the raw data. This ensures data consistency, quality, and compatibility with the data warehouse.

- Data Storage and Management: Google Cloud Storage serves as the data lake for storing both raw and processed data. BigQuery, the chosen data warehouse, provides efficient storage and management capabilities for large datasets.

- Data Warehouse Dimensional Model: A dimensional model is implemented in the data warehouse to organize Uber data effectively. This model includes dimensions like time, location, and passenger, along with fact tables like trips. It enables optimized querying and analysis of the data.

- Powerful Analytics: Leveraging big query capabilities, the project enables fast querying and analysis of Uber data. Data engineers can perform complex analytical tasks, generate insights, and identify trends and patterns within the data.

- Visualization and Dashboards: Looker Studio is integrated into the pipeline to create interactive dashboards and visualizations based on the data stored in BigQuery. These visualizations provide a user-friendly and intuitive way to explore and understand Uber data, making it easier to communicate findings and insights.

- Scalability and Performance: The chosen technologies, such as Google Cloud Storage, Google Compute Engine, BigQuery, and Looker Studio, offer scalability and high-performance capabilities, allowing for efficient processing and analysis of large volumes of data.

- Data-driven Decision Making: The Uber Data Analysis project empowers data engineers to make data-driven decisions by providing them with accurate and relevant insights. They can identify trends, optimize operations, and discover opportunities for improvement based on the analysis of Uber data.

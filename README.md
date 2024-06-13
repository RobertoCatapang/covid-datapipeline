# covid-datapipeline

## Overview

A complete data pipeline that ingests, loads and transforms covid reports CSV files into a database. Uses modern data tools (MageAI, dbt, and DuckDB) and data sourced from COVID-19 Data Repository by Hopkins University.

## Architecture

<screenshot of architecture>

MageAI
dbt
DuckDB

1. Data Ingestion: Write a script to ingest data from the provided source into a database. You should account for potential inconsistencies and errors in the data.
2. Data Processing: Implement a process to clean and transform the data. This could involve handling missing values, deduplicating records, or transforming data formats.
3. Data Storage: Store the processed data in a relational or NoSQL database. Design the schema in a way that supports efficient querying and analysis.
4. Data Analysis: Write queries or scripts to answer three specific questions about the dataset. These questions should demonstrate your ability to perform complex data analysis. Examples include:
a. What are the top 5 most common values in a particular column, and what is their frequency?
b. How does a particular metric change over time within the dataset?
c. Is there a correlation between two specific columns? Explain your findings.
5. Documentation: Provide a README.md file that includes:
a. Instructions on how to set up and run your solution.
b. A brief explanation of your design decisions and the technologies used.
c. Answers to the data analysis questions, including any assumptions you made.

Evaluation Criteria
● Correctness and efficiency of data ingestion and processing.
● Database schema design and the efficiency of queries.
● Quality of the analysis and insights provided.
● Code quality, including readability, organization, and documentation.

## 

## Requirements

- Python 3.8+
- Docker

## Installion

Before initial run, enter the command in the terminal:
```bash
cp dev.env .env && rm dev.env
```

Running the app:
```bash 
docker compose up
```


## Discussion

### Answers

1. What are the top 5 most common values in a particular column, and what is their frequency?
2. How does a particular metric change over time within the dataset?
3. Is there a correlation between two specific columns? Explain your findings.

### Assumptions


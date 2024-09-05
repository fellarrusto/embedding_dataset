
# Embedding Dataset Creator

## Overview

Embedding Dataset Creator is a web-based application designed to facilitate the creation of a dataset from book pages in PDF format. Users can load a random page from a PDF, create questions and answers based on the content, and save the results into a MySQL database. The application also allows users to download the dataset as a `.jsonl` file for further use.

## Features

- Load a random page from a PDF file.
- Create and submit question-answer pairs.
- Store the data in a MySQL database.
- Download the dataset in JSONL format (`id`, `anchor`, `positive`).

## File Structure

```
embedding_dataset
├── .gitignore
├── database
│   ├── docker-compose.yaml        # Docker Compose for MySQL setup
│   └── init.sql                   # SQL script to initialize the MySQL table
└── datasetapp
    ├── css
    │   └── style.css              # Custom styles for the web app
    ├── docker-compose.yaml        # Docker Compose for the PHP app
    ├── Dockerfile                 # Dockerfile for PHP and Apache setup
    ├── index.html                 # Main HTML file for the app interface
    ├── js
    │   ├── jquery-3.7.1.min.js    # jQuery library
    │   └── script.js              # JavaScript for handling user interactions
    ├── pdfs                       # Folder to store PDFs (place your PDFs here)
    └── php
        ├── composer.json          # Composer file for dependencies
        ├── composer.lock          # Composer lock file
        ├── generate_jsonl.php     # Script to generate and download JSONL
        ├── getRandomPdf.php       # Script to load random PDF pages
        ├── submit.php             # Script to submit data to the MySQL database
        └── vendor                 # Dependencies installed via Composer
```

## How It Works

1. **Load a Random PDF Page**: The user clicks the "New Page" button, and a random page from one of the PDFs stored in the `/pdfs` folder is displayed.
2. **Create a Dataset Entry**: The user can enter a question and answer based on the loaded PDF page.
3. **Submit the Data**: Once the user clicks "Submit", the data (`anchor`, `question`, `answer`) is saved into the MySQL database.
4. **Download Dataset**: The user can download the entire dataset in JSONL format by clicking the "Download JSONL" button, which will generate a `.jsonl` file containing the dataset entries.

## Prerequisites

- Docker
- Docker Compose

## Installation and Setup

1. **Clone the Repository**:
   ```bash
   git clone <repository-url>
   cd embedding_dataset
   ```

2. **Setting up shared network**
    Create a shared network
    ```
    docker network create app_network
    ```

3. **Database Setup**:
   Navigate to the `database` folder and run the following command to start the MySQL container:
   ```bash
   docker-compose up -d
   ```

   This will start a MySQL container and automatically initialize the database and table using the `init.sql` script.

4. **Web Application Setup**:
   Navigate to the `datasetapp` folder and run the following command to start the PHP container:
   ```bash
   docker-compose up -d
   ```

5. **Add PDFs**:
   Place your PDF files in the `datasetapp/pdfs` folder. The application will load random pages from these PDFs.

6. **Access the Application**:
   Open your browser and go to `http://localhost:8081` to access the web interface.

## Download Dataset as JSONL

To download the dataset in JSONL format, simply click the "Download JSONL" button. This will trigger the download of a `dataset.jsonl` file that contains all the entries in the database.

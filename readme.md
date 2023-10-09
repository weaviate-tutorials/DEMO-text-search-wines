# Semantic search of wines

In this repository, you'll find the practical essence of the article [Hackernoon article: "Semantic Search Queries Return More Informed Results"](https://hackernoon.com/semantic-search-queries-return-more-informed-results-nr5335nw) distilled into code (albeit updated). The author points out a common hurdle: the struggle with searching through our own unstructured data. Weaviate, an open-source vector search engine, is introduced as a sturdy bridge over this hurdle. Following the narrative, this codebase sets up Weaviate, harnesses the open transformer model [`sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2`](https://huggingface.co/sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2) for vectorization through the [vectorization module](https://www.semi.technology/developers/weaviate/current/modules/text2vec-transformers.html), and dives into a dataset of wine reviews. This repository demonstrates how to set up Weaviate with your data and get straight to firing up search queries. 

(TODO: Add demo video)

## Prerequisites
Before you can run the project, you need to have Docker, Docker Compose, and Python installed on your machine. Follow the instructions below to install the prerequisites:

### 1. Install Docker:
   - **For Windows and Mac**:
      - Download and install Docker Desktop from [Docker's official website](https://www.docker.com/products/docker-desktop).
   - **For Linux**:
      - Run the following commands in your terminal:
        ```bash
        sudo apt-get update
        sudo apt-get install docker-ce docker-ce-cli containerd.io
        ```

### 2. Install Docker Compose:
   - **For Windows and Mac**:
      - Docker Compose is included with Docker Desktop.
   - **For Linux**:
      - Run the following command in your terminal:
        ```bash
        sudo apt install docker-compose
        ```

### 3. Install Python:
   - Download and install the latest version of Python from [Python's official website](https://www.python.org/downloads/).
   - Verify the installation by running the following command in your terminal:
     ```bash
     python --version
     ```

## Setup instructions
1. **Install virtualenv** (if not already installed):
   ```bash
   pip install virtualenv
   ```
2. **Create a Virtual Environment:** 
   Navigate to the directory where you want to create your virtual environment, then run:
   ```bash
   virtualenv <name_of_virtualenv>
   ```
3. **Activate the Virtual Environment:** 
   On Windows, run:
   ```bash
   .\<name_of_virtualenv>\Scripts\activate
   ```
   On macOS and Linux, run:
   ```bash
   source <name_of_virtualenv>/bin/activate
   ```
4. **Install Python requirements:**
   ```bash
   pip install -r requirements.txt
   ```

## Usage instructions
1. Start up Weaviate: `docker-compose up -d`. Once completed, Weaviate is running on [`http://localhost:8080`]().
2. Run `python import.py` to import 2500 wines to Weaviate.
3. The data is now stored in the Weaviate instance. You can experiment with it using a python notebook or a python file.

## Dataset license
This folder contains Wine review data, retrieved from [Kaggle (from WineEnthusiast)](https://www.kaggle.com/zynicide/wine-reviews).

## Notes:
This project's origin is [here](https://github.com/weaviate/weaviate-examples/tree/main/semanticsearch-transformers-wines) and the [Hackernoon article: "Semantic Search Queries Return More Informed Results"](https://hackernoon.com/semantic-search-queries-return-more-informed-results-nr5335nw).

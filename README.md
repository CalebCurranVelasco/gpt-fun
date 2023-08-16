# gpt-fun
Caleb Curran-Velasco

gpt-fun is an innovative project that explores the capabilities of large language models and the OpenAI API for semantic search and question answering. This project aims to provide a seamless and intuitive experience for users to extract insights from various sources of information such as PDFs, YouTube videos, and URLs. By leveraging the power of large language models such as gpt-3.5, and libraries such as langchain, gpt-fun enables users to pose questions and receive accurate answers based on the contextual understanding of the provided text.

## Project Overview

This project consists of multiple sub-projects, each contributing to the overall goal of enhancing information retrieval and comprehension. The key features of this project include:

- **Medical Diagnosis Prediction**: One of gpt-fun's unique features is its ability to predict diagnoses based on user-input symptoms. Users can input their symptoms, and the model employs its contextual understanding to provide a predicted diagnosis.

- **Text Embedding**: gpt-fun utilizes the OpenAI API to embed the text content from diverse sources, including PDF documents, YouTube videos, and URLs, into a vector store. This allows for efficient storage and retrieval of semantic representations of the input data.

- **Semantic Search**: The heart of some of these projects's functionality lies in its semantic search capabilities. When a user submits a question, the system embeds the question and performs semantic search across the stored vectors of text content. This enables the identification of relevant passages and contextually similar information, enhancing the accuracy of the provided answers.

- **Question Answering**: gpt-fun's language model processes the user's question and compares it to the embedded text vectors using advanced semantic analysis techniques. By understanding the context and meaning behind the question, the model selects the most appropriate answer from the available sources.

- **User-Friendly Interface**: To ensure easy interaction and accessibility, gpt-fun's graphical user interface (GUI) is developed using Streamlit. The Streamlit app allows users to effortlessly input questions, view answers, and explore the retrieved content in a visually appealing and intuitive manner.

## Getting Started

Try out the gpt-fun app and explore its features at: [https://gpt-fun.streamlit.app](https://gpt-fun.streamlit.app)

Discover more about gpt-fun and its development on the GitHub repository: [https://github.com/CalebCurranVelasco/gpt-fun](https://github.com/CalebCurranVelasco/gpt-fun)

## To Use Locally

To experience the capabilities of gpt-fun, follow these steps:

1. Clone the gpt-fun repository to your local machine:
2. Install the required dependencies. You may need to set up a virtual environment for this purpose: pip install -r requirements.txt
3. Obtain an API key from OpenAI by signing up for access to their API services.
4. Place your actual OpenAI API key in an env file.
5. Launch the Streamlit app by running the following command in your terminal: streamlit run Homepage.py

---

*Disclaimer: gpt-fun is a project for experimental purposes and may not provide accurate or reliable information in all cases. Use the information provided by the model at your own discretion.*

# Real-Time Sentiment Analysis Dashboard

This project is a real-time sentiment analysis system built using Streamlit and powered by the Gemma 1B parameter language model for high-accuracy sentiment classification. It processes live or uploaded tweet/text data, performs preprocessing, sentiment detection, clusters negative messages, and notifies the user about critical clusters.

---

## Features

- **Real-time Analysis**: Performs text preprocessing and sentiment classification on live data.
- **Advanced Model**: Utilizes the Gemma 1B model for advanced language understanding and high-accuracy sentiment detection.
- **Interactive Dashboard**: Built with Streamlit for an intuitive and responsive user interface.
- **Negative Message Clustering**: Groups similar negative messages to identify common themes and critical concerns.
- **Real-time Notifications**: Sends alerts with key representative phrases from critical clusters.
- **Flexible Data Input**: Supports uploading custom CSV files or connecting to a Twitter scraper for live analysis.

---

## Model Used

- **Model**: Gemma-1B (Google’s open-source language model).
- **Implementation**: Loaded using a custom wrapper in `sentiment_model.py`.
- **Task**: Prompted for 3-class sentiment classification: **Positive**, **Neutral**, and **Negative**.

---

## Installation and Usage

### 1. Prerequisites

Ensure you have Python 3.x installed.

### 2. Clone the Repository

```bash
git clone <your-repository-url>
cd Real-Time-Sentiment-Dashboard

# Real-Time Sentiment Analysis Dashboard

This project is a real-time sentiment analysis system built using Streamlit and powered by the Gemma 1B parameter language model for high-accuracy sentiment classification. It processes live or uploaded tweet/text data, performs preprocessing, sentiment detection, clusters negative messages, and notifies the user about critical clusters.

---

## Features

- Real-time text preprocessing and sentiment classification  
- Utilizes Gemma 1B model for advanced language understanding  
- Interactive dashboard built with Streamlit  
- Clustering of negative messages to detect common concerns  
- Real-time notifications for key representative phrases  
- Upload custom CSVs or connect to a Twitter scraper for live analysis

---

## Model Used

- Gemma-1B (Google’s open-source language model)  
- Loaded using a custom wrapper in `sentiment_model.py`  
- Prompted for 3-class sentiment classification: Positive, Neutral, Negative

---

## Project Structure

Real-Time-Sentiment-Dashboard/
├── app.py # Main Streamlit app
├── sample_sentiment_dataset.csv # Sample input
├── sentiment_model.py # Gemma 1B based sentiment logic
├── prepocess.py # Text preprocessing logic
├── csv_deleter.py # Removes previous output CSVs
├── emotion_detection.py # (Optional) Emotion classifier
├── phrase_extractor.py # Extracts representative phrases
├── SentenceClustering.py # Clusters similar negative messages
├── ntfy.py # Sends real-time alerts via ntfy
├── runner.py # Pipeline runner
├── run_twitter_scraper.py # Twitter scraping (HT parameterized)
├── requirements.txt # Python dependencies

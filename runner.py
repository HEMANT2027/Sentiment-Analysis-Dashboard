import streamlit as st
import pandas as pd
from sentiment_model import TextProcessor
from prepocess import preprocess
from SentenceClustering import SentenceClustering
from ntfy import notification
from phrase_extractor import extract_joined_phrase

def process_sentiment(df):
    st.info("📊 Analyzing sentiment...")
    df = preprocess(df)

    analyser = TextProcessor()
    df['sentiment'] = df['Content'].apply(lambda x: analyser.analyze_sentiment(x))
    return df

def cluster_and_notify(df):
    st.info("🔍 Clustering negative tweets...")

    negative_sentences = df[df['sentiment'] == 'Negative']['Content'].tolist()

    if not negative_sentences:
        st.warning("No negative tweets to cluster.")
        return []

    clustering = SentenceClustering()
    clustering.encode_sentences(negative_sentences)
    clustering.cluster_sentences()
    representatives = clustering.get_representative_sentences()

    for sentence in representatives:
        text = extract_joined_phrase(sentence)
        notification(text)
    st.success("✅ Alerts sent.")
    return representatives

# Streamlit UI
st.set_page_config(page_title="Tweet Sentiment Processor", layout="centered")
st.title("📥 Upload Tweets CSV for Sentiment & Clustering")

uploaded_file = st.file_uploader("Upload CSV file with tweets", type="csv")

if uploaded_file is not None:
    try:
        # ✅ Correct way to read uploaded file
        df = pd.read_csv(uploaded_file)

        # ✅ Ensure proper column check
        if 'Content' not in df.columns:
            st.error("❌ The uploaded CSV must have a 'Content' column.")
        else:
            st.success("✅ File uploaded successfully!")

            if st.button("Run Sentiment & Clustering Pipeline"):
                with st.spinner("Running..."):
                    df = process_sentiment(df)

                    st.subheader("📈 Sentiment Distribution")
                    st.bar_chart(df['sentiment'].value_counts())

                    alerts = cluster_and_notify(df)
                    if alerts:
                        st.subheader("🚨 Alerts Sent for Negative Clusters")
                        for alert in alerts:
                            st.write(f"• {alert}")

                    st.subheader("🔎 Sample Output")
                    st.dataframe(df[['Content', 'sentiment']].head(10))

    except Exception as e:
        st.error(f"❌ Error reading file: {e}")

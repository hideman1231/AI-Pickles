from transformers import pipeline

sentiment_pipeline = pipeline('sentiment-analysis')

SENTIMENT_MAPPING = {
    'POSITIVE': 1,
    'NEGATIVE': 2,
    'NEUTRAL': 3,
}


def get_sentiment_answer(prompt):
    return SENTIMENT_MAPPING[sentiment_pipeline(prompt)[0]['label']]

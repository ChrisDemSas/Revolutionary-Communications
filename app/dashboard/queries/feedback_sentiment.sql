SELECT COUNT(sentiment) AS sentiment_counter, sentiment 
FROM feedbacks 
GROUP BY sentiment
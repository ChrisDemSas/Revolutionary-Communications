SELECT AVG(sentiment) AS average_sentiment, category 
FROM feedbacks 
GROUP BY category
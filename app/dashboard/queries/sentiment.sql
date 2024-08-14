SELECT AVG(sentiment) AS average_sentiment, time 
FROM feedbacks 
GROUP BY time
SELECT feedback
FROM feedbacks
WHERE time > DATE('now' , '-7 days')
ORDER BY time DESC
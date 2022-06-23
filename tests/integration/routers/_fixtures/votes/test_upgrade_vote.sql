INSERT INTO `candidates` (id, name, description, category)
VALUES
(1, 'Kanye West', 'Born in Atlanta and raised in Chicago, West was first known as a producer for Roc-A-Fella Records in the early 2000s, producing singles for several mainstream artists.', 'ENTERTAINMENT'),
(2, 'Mark Zuckerberg', 'Born in White Plains, New York, Zuckerberg attended Harvard University, where he launched the Facebook social networking service from his dormitory room on February 4, 2004.', 'BUSINESS');

INSERT INTO `users` (id, email, name, family_name, password, enabled)
VALUES
(1, 'oscar@gmail.com', 'Oscar', 'Orellana', null, 1),
(2, 'raquel@gmail.com', 'Raquel', 'Godina', null, 1);

INSERT INTO `votes` (user_id, candidate_id, veredict, historical_veredicts)
VALUES
(1, 1, 0, '[{"veredict": 1, "datetime": "2022-03-10 16:49:34"}, {"veredict": 0, "datetime": "2022-03-11 18:49:34"}]'),
(1, 2, 1, '[{"veredict": 1, "datetime": "2022-03-14 16:49:34"}]'),
(2, 1, null, '[{"veredict": 0, "datetime": "2022-03-18 16:49:34"}, {"veredict": null, "datetime": "2022-03-20 16:49:34"}]');
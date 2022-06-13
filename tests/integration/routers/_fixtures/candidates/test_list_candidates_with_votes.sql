INSERT INTO `candidates` (id, name, description, category, picture)
VALUES
(1, 'Kanye West', 'Born in Atlanta and raised in Chicago, West was first known as a producer for Roc-A-Fella Records in the early 2000s, producing singles for several mainstream artists.', 'ENTERTAINMENT', null),
(2, 'Mark Zuckerberg', 'Born in White Plains, New York, Zuckerberg attended Harvard University, where he launched the Facebook social networking service from his dormitory room on February 4, 2004.', 'BUSINESS', null),
(3, 'Cristina Fernández de Kirchner', 'Her first term of office started with a conflict with the agricultural sector, and her proposed taxation system was rejected.', 'POLITICS', null),
(4, 'Malala Yousafzai', 'The daughter of educational activist Ziauddin, Yousafzai was born to a Pashtun family in Mingora, Khyber Pakhtunkhwa, Pakistan. Her family came to run a chain of schools in the region.', 'POLITICS', null),
(5, 'Elon Musk', 'In 2002, Musk founded SpaceX, an aerospace manufacturer and space transport services company, of which he is CEO, CTO, and lead designer.', 'BUSINESS', null),
(6, 'Greta Thumberg', 'Thunberg''s activism started after convincing her parents to adopt several lifestyle choices to reduce their own carbon footprint.', 'ENVIRONMENT', null);

INSERT INTO `users` (id, email, name, family_name, password, enabled)
VALUES
(1, 'oscar@gmail.com', 'Oscar', 'Orellana', null, 1),
(2, 'raquel@gmail.com', 'Raquel', 'Godina', null, 1),
(3, 'robert@gmail.com', 'Robert', 'Tzeker', null, 0);

INSERT INTO `votes` (user_id, candidate_id, veredict, historical_veredicts)
VALUES
(1, 1, 0, '[{"veredict": 1, "datetime": "2022-03-10 16:49:34"}, {"veredict": 0, "datetime": "2022-03-11 18:49:34"}]'),
(1, 2, 1, '[{"veredict": 1, "datetime": "2022-03-14 16:49:34"}]'),
(1, 3, 0, '[{"veredict": 0, "datetime": "2022-03-18 16:49:34"}]'),
(1, 4, null, '[{"veredict": 0, "datetime": "2022-03-18 16:49:34"}, {"veredict": null, "datetime": "2022-03-20 16:49:34"}]'),
(1, 6, 1, '[{"veredict": 1, "datetime": "2022-03-14 16:49:34"}]'),
(2, 1, 0, '[{"veredict": 1, "datetime": "2022-03-10 16:49:34"}, {"veredict": 0, "datetime": "2022-03-11 18:49:34"}]'),
(2, 2, 0, '[{"veredict": 0, "datetime": "2022-03-14 16:49:34"}]'),
(2, 3, 0, '[{"veredict": 0, "datetime": "2022-03-18 16:49:34"}]'),
(2, 4, null, '[{"veredict": 0, "datetime": "2022-03-18 16:49:34"}, {"veredict": null, "datetime": "2022-03-20 16:49:34"}]'),
(2, 6, 0, '[{"veredict": 0, "datetime": "2022-03-14 16:49:34"}]'),
(3, 1, 0, '[{"veredict": 1, "datetime": "2022-03-10 16:49:34"}, {"veredict": 0, "datetime": "2022-03-11 18:49:34"}]'),
(3, 2, 0, '[{"veredict": 0, "datetime": "2022-03-14 16:49:34"}]'),
(3, 3, 0, '[{"veredict": 0, "datetime": "2022-03-18 16:49:34"}]'),
(3, 4, 1, '[{"veredict": 1, "datetime": "2022-03-18 16:49:34"}]'),
(3, 6, 0, '[{"veredict": 0, "datetime": "2022-03-14 16:49:34"}]');
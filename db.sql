--
-- Create database from scratch
--

DROP DATABASE rule_of_thumb_mysql;
CREATE DATABASE rule_of_thumb_mysql;
USE rule_of_thumb_mysql;

--
-- Table structure for table `candidates`
--

CREATE TABLE `candidates` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(100) NOT NULL,
  `description` varchar(255) NOT NULL,
  `category` enum('ENTERTAINMENT','BUSINESS','POLITICS','ENVIRONMENT') NOT NULL,
  `created_at` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `last_updated` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Inserts for table `candidates`
--

INSERT INTO `candidates` (id, name, description, category)
VALUES
(1, 'Kanye West', 'Born in Atlanta and raised in Chicago, West was first known as a producer for Roc-A-Fella Records in the early 2000s, producing singles for several mainstream artists.', 'ENTERTAINMENT'),
(2, 'Mark Zuckerberg', 'Born in White Plains, New York, Zuckerberg attended Harvard University, where he launched the Facebook social networking service from his dormitory room on February 4, 2004.', 'BUSINESS'),
(3, 'Cristina Fernández de Kirchner', 'Her first term of office started with a conflict with the agricultural sector, and her proposed taxation system was rejected.', 'POLITICS'),
(4, 'Malala Yousafzai', 'The daughter of educational activist Ziauddin, Yousafzai was born to a Pashtun family in Mingora, Khyber Pakhtunkhwa, Pakistan. Her family came to run a chain of schools in the region.', 'POLITICS'),
(5, 'Elon Musk', 'In 2002, Musk founded SpaceX, an aerospace manufacturer and space transport services company, of which he is CEO, CTO, and lead designer.', 'BUSINESS'),
(6, 'Greta Thumberg', 'Thunberg''s activism started after convincing her parents to adopt several lifestyle choices to reduce their own carbon footprint.', 'ENVIRONMENT');

--
-- Table structure for table `users`
--

CREATE TABLE `users` (
  `id` int NOT NULL AUTO_INCREMENT,
  `email` varchar(50) NOT NULL,
  `name` varchar(50) NOT NULL,
  `family_name` varchar(50) DEFAULT NULL,
  `password` text,
  `enabled` tinyint(1) DEFAULT 1,
  `created_at` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `updated_at` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`),
  UNIQUE KEY `email` (`email`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Inserts for table `users`
--

INSERT INTO `users` (id, email, name, family_name, password, enabled)
VALUES
(1, 'oscar@gmail.com', 'Oscar', 'Orellana', null, 1),
(2, 'raquel@gmail.com', 'Raquel', 'Godina', null, 1),
(3, 'robert@gmail.com', 'Robert', 'Tzeker', null, 0),
(4, 'viviana@gmail.com', 'Viviana', 'Merlo', null, 1),
(5, 'lizeth@gmail.com', 'Lizeth', 'Echevarri', null, 1);

--
-- Table structure for table `votes`
--

CREATE TABLE `votes` (
  `user_id` int NOT NULL,
  `candidate_id` int NOT NULL,
  `veredict` tinyint(1) DEFAULT NULL,
  `historical_veredicts` json DEFAULT NULL,
  `updated_at` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`user_id`,`candidate_id`),
  KEY `candidate_id` (`candidate_id`),
  CONSTRAINT `votes_ibfk_1` FOREIGN KEY (`user_id`) REFERENCES `users` (`id`),
  CONSTRAINT `votes_ibfk_2` FOREIGN KEY (`candidate_id`) REFERENCES `candidates` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Inserts for table `votes`
--

INSERT INTO `votes` (user_id, candidate_id, veredict, historical_veredicts)
VALUES
(1, 1, 0, '[{"veredict": 1, "datetime": "2022-03-10 16:49:34"}, {"veredict": 0, "datetime": "2022-03-11 18:49:34"}]'),
(1, 2, 1, '[{"veredict": 1, "datetime": "2022-03-14 16:49:34"}]'),
(1, 3, 0, '[{"veredict": 0, "datetime": "2022-03-18 16:49:34"}]'),
(1, 4, null, '[{"veredict": 0, "datetime": "2022-03-18 16:49:34"}, {"veredict": null, "datetime": "2022-03-20 16:49:34"}]'),
(1, 5, 1, '[{"veredict": 1, "datetime": "2022-03-14 16:49:34"}]'),
(1, 6, 1, '[{"veredict": 1, "datetime": "2022-03-14 16:49:34"}]'),
(2, 1, 0, '[{"veredict": 1, "datetime": "2022-03-10 16:49:34"}, {"veredict": 0, "datetime": "2022-03-11 18:49:34"}]'),
(2, 2, 0, '[{"veredict": 0, "datetime": "2022-03-14 16:49:34"}]'),
(2, 3, 0, '[{"veredict": 0, "datetime": "2022-03-18 16:49:34"}]'),
(2, 4, null, '[{"veredict": 0, "datetime": "2022-03-18 16:49:34"}, {"veredict": null, "datetime": "2022-03-20 16:49:34"}]'),
(2, 5, 0, '[{"veredict": 0, "datetime": "2022-03-14 16:49:34"}]'),
(2, 6, 0, '[{"veredict": 0, "datetime": "2022-03-14 16:49:34"}]'),
(3, 1, 0, '[{"veredict": 1, "datetime": "2022-03-10 16:49:34"}, {"veredict": 0, "datetime": "2022-03-11 18:49:34"}]'),
(3, 2, 0, '[{"veredict": 0, "datetime": "2022-03-14 16:49:34"}]'),
(3, 3, 0, '[{"veredict": 0, "datetime": "2022-03-18 16:49:34"}]'),
(3, 4, 1, '[{"veredict": 1, "datetime": "2022-03-18 16:49:34"}]'),
(3, 5, 0, '[{"veredict": 0, "datetime": "2022-03-14 16:49:34"}]'),
(3, 6, 0, '[{"veredict": 0, "datetime": "2022-03-14 16:49:34"}]'),
(4, 1, 0, '[{"veredict": 1, "datetime": "2022-03-10 16:49:34"}, {"veredict": 0, "datetime": "2022-03-11 18:49:34"}]'),
(4, 2, 1, '[{"veredict": 1, "datetime": "2022-03-14 16:49:34"}]'),
(4, 3, 0, '[{"veredict": 0, "datetime": "2022-03-18 16:49:34"}]'),
(4, 4, 1, '[{"veredict": 1, "datetime": "2022-03-18 16:49:34"}]'),
(4, 5, 1, '[{"veredict": 1, "datetime": "2022-03-14 16:49:34"}]'),
(4, 6, 1, '[{"veredict": 1, "datetime": "2022-03-14 16:49:34"}]'),
(5, 1, 0, '[{"veredict": 1, "datetime": "2022-03-10 16:49:34"}, {"veredict": 0, "datetime": "2022-03-11 18:49:34"}]'),
(5, 2, 1, '[{"veredict": 1, "datetime": "2022-03-14 16:49:34"}]'),
(5, 3, 0, '[{"veredict": 0, "datetime": "2022-03-18 16:49:34"}]'),
(5, 4, 1, '[{"veredict": 1, "datetime": "2022-03-14 16:49:34"}]'),
(5, 5, 1, '[{"veredict": 1, "datetime": "2022-03-14 16:49:34"}]'),
(5, 6, null, '[{"veredict": 0, "datetime": "2022-03-18 16:49:34"}, {"veredict": null, "datetime": "2022-03-20 16:49:34"}]');
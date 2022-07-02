SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;

CREATE TABLE IF NOT EXISTS movies (
    movie_id INT PRIMARY KEY,
    movie_name VARCHAR(100) NOT NULL,
    movie_rank INT UNIQUE,
    movie_score FLOAT NOT NULL,
    movie_picture VARCHAR(200) NOT NULL,
    movie_year INT NOT NULL
)ENGINE=InnoDB DEFAULT CHARSET=utf8;

CREATE TABLE IF NOT EXISTS users (
    user_id INT PRIMARY KEY AUTO_INCREMENT,
    user_name VARCHAR(20) NOT NULL,
    user_email VARCHAR(20) NOT NULL,
    user_password INT NOT NULL
)ENGINE=InnoDB DEFAULT CHARSET=utf8;

CREATE TABLE IF NOT EXISTS user_premovies (
    user_id INT NOT NULL,
    movie_id INT NOT NULL,
    PRIMARY KEY(user_id, movie_id),
    CONSTRAINT fk_um_1 FOREIGN KEY (user_id) REFERENCES users(user_id),
    CONSTRAINT fk_um_2 FOREIGN KEY (movie_id) REFERENCES movies(movie_id)
)ENGINE=InnoDB DEFAULT CHARSET=utf8;

CREATE TABLE IF NOT EXISTS directors (
    director_id INT PRIMARY KEY,
    director_name VARCHAR(50) NOT NULL
)ENGINE=InnoDB DEFAULT CHARSET=utf8;

CREATE TABLE IF NOT EXISTS writers (
    writer_id INT PRIMARY KEY,
    writer_name VARCHAR(50) NOT NULL
)ENGINE=InnoDB DEFAULT CHARSET=utf8;

CREATE TABLE IF NOT EXISTS actors (
    actor_id INT PRIMARY KEY,
    actor_name VARCHAR(50) NOT NULL
)ENGINE=InnoDB DEFAULT CHARSET=utf8;


CREATE TABLE IF NOT EXISTS areas (
    area_id INT PRIMARY KEY,
    area_name VARCHAR(20) NOT NULL
)ENGINE=InnoDB DEFAULT CHARSET=utf8;

CREATE TABLE IF NOT EXISTS types (
    type_id INT PRIMARY KEY,
    type_name VARCHAR(20) NOT NULL
)ENGINE=InnoDB DEFAULT CHARSET=utf8;

CREATE TABLE IF NOT EXISTS movie_director (
    movie_id INT  NOT NULL,
    director_id INT  NOT NULL,
    PRIMARY KEY(movie_id,director_id),
    CONSTRAINT fk_md_1 FOREIGN KEY (movie_id) REFERENCES movies(movie_id),
    CONSTRAINT fk_md_2 FOREIGN KEY (director_id) REFERENCES directors(director_id)
)ENGINE=InnoDB DEFAULT CHARSET=utf8;

CREATE TABLE IF NOT EXISTS movie_writer (
    movie_id INT  NOT NULL,
    writer_id INT  NOT NULL,
    PRIMARY KEY(movie_id,writer_id),
    CONSTRAINT fk_mw_1 FOREIGN KEY (movie_id) REFERENCES movies(movie_id),
    CONSTRAINT fk_mw_2 FOREIGN KEY (writer_id) REFERENCES writers(writer_id)
)ENGINE=InnoDB DEFAULT CHARSET=utf8;

CREATE TABLE IF NOT EXISTS movie_actor (
    movie_id INT  NOT NULL,
    actor_id INT  NOT NULL,
    PRIMARY KEY(movie_id,actor_id),
    CONSTRAINT fk_mac_1 FOREIGN KEY (movie_id) REFERENCES movies(movie_id),
    CONSTRAINT fk_mac_2 FOREIGN KEY (actor_id) REFERENCES actors(actor_id)
)ENGINE=InnoDB DEFAULT CHARSET=utf8;

CREATE TABLE IF NOT EXISTS movie_type (
    movie_id INT  NOT NULL,
    type_id INT  NOT NULL,
    PRIMARY KEY(movie_id,type_id),
    CONSTRAINT fk_mt_1 FOREIGN KEY (movie_id) REFERENCES movies(movie_id),
    CONSTRAINT fk_mt_2 FOREIGN KEY (type_id) REFERENCES types(type_id)
)ENGINE=InnoDB DEFAULT CHARSET=utf8;

CREATE TABLE IF NOT EXISTS movie_area (
    movie_id INT  NOT NULL,
    area_id INT  NOT NULL,
    PRIMARY KEY(movie_id,area_id),
    CONSTRAINT fk_mar_1 FOREIGN KEY (movie_id) REFERENCES movies(movie_id),
    CONSTRAINT fk_mar_2 FOREIGN KEY (area_id) REFERENCES areas(area_id)
)ENGINE=InnoDB DEFAULT CHARSET=utf8;

CREATE TABLE IF NOT EXISTS admin_users (
    admin_id INT PRIMARY KEY AUTO_INCREMENT,
    admin_name VARCHAR(20) NOT NULL,
    admin_password VARCHAR(20) NOT NULL
)ENGINE=InnoDB DEFAULT CHARSET=utf8;



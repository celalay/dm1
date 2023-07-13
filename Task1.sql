CREATE TABLE blogs (
    id INT PRIMARY KEY,
    title VARCHAR(255),
    content TEXT,
    author VARCHAR(255),
    publication_date DATE
);

CREATE TABLE comments (
    id INT PRIMARY KEY,
    content TEXT,
    author VARCHAR(255),
    publication_date DATE,
    blog_id INT,
    FOREIGN KEY (blog_id) REFERENCES blogs(id)
);

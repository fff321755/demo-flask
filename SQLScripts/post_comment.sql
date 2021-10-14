CREATE TABLE users(
    uni CHAR(8),
    firstName VARCHAR(100),
    lastName VARCHAR(40),
    PRIMARY KEY(uni)
);

CREATE TABLE posts(
    pid INT,
    parent_pid INT,
    uni CHAR(8),
    title VARCHAR(100),
    text VARCHAR(500) NOT NULL,
    time TIMESTAMP NOT NULL,
    PRIMARY KEY(pid),
    FOREIGN KEY (uni) REFERENCES users(uni)
        ON DELETE SET NULL,
    FOREIGN KEY (parent_pid) REFERENCES posts(pid)
        ON DELETE CASCADE
);

DROP TABLE posts;
DROP TABLE users;

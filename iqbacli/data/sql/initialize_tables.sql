BEGIN TRANSACTION;

CREATE TABLE IF NOT EXISTS query (
    id INT PRIMARY KEY,
    keywords_raw VARCHAR(500) NOT NULL,
    keywords_pattern VARCHAR(1500) NOT NULL,
    directory VARCHAR(500) NOT NULL,
    output_dir VARCHAR(500),
    cache BOOLEAN NOT NULL,
    flat BOOLEAN NOT NULL,
    regex BOOLEAN NOT NULL, 
    only_ext VARCHAR(500),
    only_filename VARCHAR(500),
    only_dirname VARCHAR(500),
    ignore_ext VARCHAR(500),
    ignore_filename VARCHAR(500),
    ignore_dirname VARCHAR(500)
);

CREATE TABLE IF NOT EXISTS result (
    id INT PRIMARY KEY,
    query_id INT NOT NULL,
    search_count INT NOT NULL,
    match_count INT NOT NULL,
    unsupported_count INT NOT NULL,
    fail_to_parse_count INT NOT NULL,
    fail_to_copy_count INT NOT NULL,
    cache_dir_size INT,
    cache_dir VARCHAR(500),
    FOREIGN KEY (query_id) REFERENCES query(id) ON DELETE CASCADE
);

COMMIT;
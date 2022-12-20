CREATE TABLE IF NOT EXISTS result {
    id INT UNIQUE NOT NULL IDENTITY(1, 1) PRIMARY KEY,
    query_id INT NOT NULL,
    search_count INT NOT NULL,
    match_count INT NOT NULL,
    unsupported_count INT NOT NULL,
    fail_to_parse_count INT NOT NULL,
    fail_to_copy_count INT NOT NULL,
    cache_dir_size INT,
    cache_dir VARCHAR(500)
}
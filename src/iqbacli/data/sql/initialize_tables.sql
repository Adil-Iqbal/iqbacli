BEGIN TRANSACTION;

CREATE TABLE IF NOT EXISTS query (
    id INTEGER PRIMARY KEY,
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
    id INTEGER PRIMARY KEY,
    query_id INTEGER NOT NULL,
    search_count INTEGER NOT NULL,
    match_count INTEGER NOT NULL,
    unsupported_count INTEGER NOT NULL,
    fail_to_parse_count INTEGER NOT NULL,
    fail_to_copy_count INTEGER NOT NULL,
    cache_dir_size INTEGER,
    cache_dir VARCHAR(500),
    FOREIGN KEY (query_id) REFERENCES query (id) ON DELETE CASCADE
);

COMMIT;
CREATE TABLE IF NOT EXISTS queries (
    qid INTEGER PRIMARY KEY,
    keywords_raw TEXT NOT NULL,
    keywords_pattern TEXT NOT NULL,
    directory TEXT NOT NULL,
    output_dir TEXT,
    cache BOOLEAN NOT NULL,
    flat BOOLEAN NOT NULL,
    regex BOOLEAN NOT NULL, 
    only_ext TEXT,
    only_filename TEXT,
    only_dirname TEXT,
    ignore_ext TEXT,
    ignore_filename TEXT,
    ignore_dirname TEXT
);

CREATE TABLE IF NOT EXISTS results (
    rid INTEGER PRIMARY KEY,
    qid INTEGER NOT NULL,
    search_count INTEGER NOT NULL,
    match_count INTEGER NOT NULL,
    unsupported_count INTEGER NOT NULL,
    fail_to_parse_count INTEGER NOT NULL,
    fail_to_copy_count INTEGER NOT NULL,
    cache_dir_size INTEGER NOT NULL,
    cache_dir TEXT,
    FOREIGN KEY (qid) REFERENCES query (qid) ON DELETE CASCADE
);
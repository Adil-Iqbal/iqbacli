CREATE TABLE IF NOT EXISTS query {
    id INT UNIQUE NOT NULL IDENTITY(1, 1) PRIMARY KEY,
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
    ignore_dirname VARCHAR(500),
}
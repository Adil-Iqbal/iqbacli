-- Single script resets test database

BEGIN;

CREATE TABLE IF NOT EXISTS queries (
    qid INTEGER PRIMARY KEY,
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

CREATE TABLE IF NOT EXISTS results (
    rid INTEGER PRIMARY KEY,
    qid INTEGER NOT NULL,
    search_count INTEGER NOT NULL,
    match_count INTEGER NOT NULL,
    unsupported_count INTEGER NOT NULL,
    fail_to_parse_count INTEGER NOT NULL,
    fail_to_copy_count INTEGER NOT NULL,
    cache_dir_size INTEGER,
    cache_dir VARCHAR(500),
    FOREIGN KEY (qid) REFERENCES query (qid) ON DELETE CASCADE
);

delete from queries;
delete from results;

insert into queries (keywords_raw, keywords_pattern, directory, output_dir, cache, flat, regex, only_ext, only_filename, only_dirname, ignore_ext, ignore_filename, ignore_dirname) values ('motivate6129', 'raw_motivate6129', 'Habitasse.mp3', 'Lectus.avi', false, false, false, 'pbo,dmp,jtp', 'snwvo,qscmj,speke', 'ivhzl,mxort,urfgj', 'cuf,rxz,zwi', 'sznlu,bwbka,bsyxh', 'exvrm,awlvc,kdjxr');
insert into queries (keywords_raw, keywords_pattern, directory, output_dir, cache, flat, regex, only_ext, only_filename, only_dirname, ignore_ext, ignore_filename, ignore_dirname) values ('canon381', 'raw_canon381', 'NullaEgetEros.png', 'VelEstDonec.avi', true, true, false, 'lxx,mip,kjl', 'djzew,ezmkp,byrdq', 'kvwey,zxafq,gcpnb', 'kzi,jxl,hkw', 'qmkqw,btrrs,qjjry', 'utpao,tskrp,ckflq');
insert into queries (keywords_raw, keywords_pattern, directory, output_dir, cache, flat, regex, only_ext, only_filename, only_dirname, ignore_ext, ignore_filename, ignore_dirname) values ('lance''s1906', 'raw_lance''s1906', 'NibhIn.ppt', 'BlanditMiIn.jpeg', false, false, true, 'awl,jny,lqy', 'idgmw,pdmrf,vphnz', 'lilah,ntduw,ulylt', 'hvq,uhl,xhc', 'hfnbs,xmrlv,bgonj', 'mynmh,lsgqu,shpnq');
insert into queries (keywords_raw, keywords_pattern, directory, output_dir, cache, flat, regex, only_ext, only_filename, only_dirname, ignore_ext, ignore_filename, ignore_dirname) values ('composed07376', 'raw_composed07376', 'FeugiatEt.doc', 'IpsumPrimis.pdf', true, false, false, 'coz,npo,kvw', 'qjyfr,oikyc,svovl', 'irlna,stykj,udwsw', 'xqx,wdo,cab', 'jizpd,racmg,xnrva', 'amtng,azwgd,jcent');
insert into queries (keywords_raw, keywords_pattern, directory, output_dir, cache, flat, regex, only_ext, only_filename, only_dirname, ignore_ext, ignore_filename, ignore_dirname) values ('fasten7556', 'raw_fasten7556', 'NecEuismod.doc', 'MattisEgestasMetus.mp3', false, true, false, 'jal,aoj,nee', 'xuczm,npoyo,dkofz', 'mawes,suinm,wpuyp', 'msq,ait,tga', 'jxzuh,cajex,ciohn', 'iccbg,ohpfz,waorv');

insert into results (qid, search_count, unsupported_count, fail_to_parse_count, fail_to_copy_count, cache_dir_size, cache_dir, match_count) values (1, 186, 9, 6, 4, 8, 'C:\\uktv\ufy\dlip', 84);
insert into results (qid, search_count, unsupported_count, fail_to_parse_count, fail_to_copy_count, cache_dir_size, cache_dir, match_count) values (2, 417, 6, 9, 3, 9, 'C:\\afty\hlv\nzci', 200);
insert into results (qid, search_count, unsupported_count, fail_to_parse_count, fail_to_copy_count, cache_dir_size, cache_dir, match_count) values (3, 374, 3, 2, 8, 9, 'C:\\ezva\raq\tkol', 181);
insert into results (qid, search_count, unsupported_count, fail_to_parse_count, fail_to_copy_count, cache_dir_size, cache_dir, match_count) values (4, 226, 1, 4, 6, 6, 'C:\\myzk\ozq\txhi', 108);
insert into results (qid, search_count, unsupported_count, fail_to_parse_count, fail_to_copy_count, cache_dir_size, cache_dir, match_count) values (5, 321, 4, 7, 4, 5, 'C:\\aalq\ehd\elad', 153);
insert into results (qid, search_count, unsupported_count, fail_to_parse_count, fail_to_copy_count, cache_dir_size, cache_dir, match_count) values (1, 353, 8, 4, 8, 3, 'C:\\lvnk\oak\zevy', 167);
insert into results (qid, search_count, unsupported_count, fail_to_parse_count, fail_to_copy_count, cache_dir_size, cache_dir, match_count) values (2, 250, 8, 2, 3, 2, 'C:\\noia\ibr\ifjh', 119);
insert into results (qid, search_count, unsupported_count, fail_to_parse_count, fail_to_copy_count, cache_dir_size, cache_dir, match_count) values (3, 216, 3, 3, 9, 3, 'C:\\ttvt\snd\jbqc', 101);
insert into results (qid, search_count, unsupported_count, fail_to_parse_count, fail_to_copy_count, cache_dir_size, cache_dir, match_count) values (4, 148, 3, 6, 9, 4, 'C:\\jfrq\grw\ibuu', 65);
insert into results (qid, search_count, unsupported_count, fail_to_parse_count, fail_to_copy_count, cache_dir_size, cache_dir, match_count) values (6, 159, 9, 6, 10, 8, 'C:\\scpf\rnb\myix', 67);

COMMIT;
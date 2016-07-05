ALTER TABLE wp_posts
    CHANGE COLUMN post_date post_date datetime NOT NULL DEFAULT CURRENT_TIMESTAMP,
    CHANGE COLUMN post_date_gmt post_date_gmt datetime NOT NULL DEFAULT CURRENT_TIMESTAMP,
    CHANGE COLUMN post_modified post_modified datetime NOT NULL DEFAULT CURRENT_TIMESTAMP,
    CHANGE COLUMN post_modified_gmt post_modified_gmt datetime NOT NULL DEFAULT CURRENT_TIMESTAMP;

-- DROP INDEX ft_content ON wp_posts;
-- DROP INDEX ft_excerpt ON wp_posts;
-- DROP INDEX ft_title ON wp_posts;

ALTER TABLE wp_posts
    ADD FULLTEXT(post_content);
ALTER TABLE wp_posts
    ADD FULLTEXT(post_excerpt);
ALTER TABLE wp_posts
    ADD FULLTEXT(post_title);

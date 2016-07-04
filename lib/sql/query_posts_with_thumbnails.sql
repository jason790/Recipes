SELECT ID,post_title, post_status , thumbnail.meta_key, thumbnail.meta_value FROM wp_posts
INNER JOIN 
    (
        SELECT m.post_id,m.meta_id,t.meta_key,t.meta_value FROM wp_postmeta AS m
            INNER JOIN wp_postmeta AS t
            ON t.post_id = m.meta_value
        WHERE t.meta_key = "_wp_attached_file"
        AND m.meta_key = "_thumbnail_id"
    ) AS thumbnail
    ON thumbnail.post_id = wp_posts.id
WHERE wp_posts.post_type = "post"
AND wp_posts.post_status = "publish"
LIMIT 12

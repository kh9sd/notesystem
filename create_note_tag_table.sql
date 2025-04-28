CREATE TABLE note_tags (
   note_id BIGINT REFERENCES notes,
   tag_id BIGINT REFERENCES tags,
   UNIQUE (note_id, tag_id)
)

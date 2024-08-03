CREATE TYPE release_type AS ENUM ('album', 'ep', 'single', 'live');

CREATE TABLE IF NOT EXISTS Release (
  id SERIAL PRIMARY KEY,
  title VARCHAR(255) NOT NULL,
  release_date DATE NOT NULL,
  release_type release_type NOT NULL
);

CREATE TABLE IF NOT EXISTS Track (
  id SERIAL PRIMARY KEY,
  title VARCHAR(255) NOT NULL
);

CREATE TABLE IF NOT EXISTS ReleaseTrack (
  release_id INTEGER NOT NULL REFERENCES Release(id) ON DELETE CASCADE,
  track_id INTEGER NOT NULL REFERENCES Track(id) ON DELETE CASCADE,
  track_index INTEGER NOT NULL,
  PRIMARY KEY (release_id, track_id)
);

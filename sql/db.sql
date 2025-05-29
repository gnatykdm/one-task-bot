-- DataBase for OneTaskBitBot --

-- Enums --
CREATE TYPE language_enum AS ENUM('ENGLISH', 'RUSSIAN'); 
CREATE TYPE task_status AS ENUM('DONE', 'PROCESSING');
CREATE TYPE routine_type AS ENUM('MORNING', 'EVENING');

-- Tables --
CREATE TABLE IF NOT EXISTS users (
    t_id BIGINT PRIMARY KEY,
    t_name VARCHAR(255) UNIQUE NOT NULL,
    language language_enum NOT NULL DEFAULT 'ENGLISH',
    created_at TIMESTAMP NOT NULL,
    wake_up_time TIMESTAMP,
    sleep_time TIMESTAMP
);

CREATE TABLE IF NOT EXISTS tasks (
    t_id BIGSERIAL PRIMARY KEY,
    u_id BIGINT NOT NULL REFERENCES users(t_id) ON DELETE CASCADE,
    t_name VARCHAR(255) NOT NULL,
    t_deadline TIMESTAMP,
    t_status task_status NOT NULL DEFAULT 'PROCESSING',
    t_created_at TIMESTAMP NOT NULL DEFAULT NOW()
);

CREATE TABLE IF NOT EXISTS notes (
    n_id BIGSERIAL PRIMARY KEY,
    u_id BIGINT NOT NULL REFERENCES users(t_id) ON DELETE CASCADE,
    n_context TEXT NOT NULL,
    created_at TIMESTAMP NOT NULL DEFAULT NOW()
);

CREATE TABLE IF NOT EXISTS daily_routines (
    r_id BIGSERIAL PRIMARY KEY,
    u_id BIGINT NOT NULL REFERENCES users(t_id) ON DELETE CASCADE,
    r_name VARCHAR(255) NOT NULL,
    r_type routine_type NOT NULL
);

CREATE TABLE IF NOT EXISTS daily_statistics (
    d_id BIGSERIAL PRIMARY KEY,
    u_id BIGINT NOT NULL REFERENCES users(t_id) ON DELETE CASCADE,
    performed INT NOT NULL DEFAULT 0,
    focus_counter INT NOT NULL DEFAULT 0,
    break_counter INT NOT NULL DEFAULT 0,
    notes_counter INT NOT NULL DEFAULT 0,
    streak INT NOT NULL DEFAULT 0,
    best_streak INT NOT NULL DEFAULT 0,
    energy_level INT CHECK (energy_level BETWEEN 1 AND 10)
);

CREATE TABLE IF NOT EXISTS habits (
    h_id BIGSERIAL PRIMARY KEY,
    u_id BIGINT NOT NULL REFERENCES users(t_id) ON DELETE CASCADE,
    h_name VARCHAR(255) NOT NULL,
    h_status task_status NOT NULL DEFAULT 'PROCESSING',
    start_h_time TIMESTAMP NOT NULL,
    finish_h_time TIMESTAMP NOT NULL,
    h_created_at TIMESTAMP NOT NULL DEFAULT NOW()
);

CREATE TABLE IF NOT EXISTS focuses (
    f_id BIGSERIAL PRIMARY KEY,
    u_id BIGINT NOT NULL REFERENCES users(t_id) ON DELETE CASCADE,
    t_id BIGINT REFERENCES tasks(t_id) ON DELETE SET NULL,
    start_time TIMESTAMP NOT NULL,
    stop_time TIMESTAMP NOT NULL,
    breaks_counter INT NOT NULL DEFAULT 0
);

CREATE TABLE IF NOT EXISTS reminders (
    id BIGSERIAL PRIMARY KEY,
    u_id BIGINT NOT NULL REFERENCES users(t_id) ON DELETE CASCADE,
    task_id BIGINT REFERENCES tasks(t_id) ON DELETE CASCADE,
    reminder_time TIMESTAMP NOT NULL,
    repeat_interval INTERVAL,
    is_active BOOLEAN DEFAULT TRUE,
    created_at TIMESTAMP DEFAULT NOW()
);

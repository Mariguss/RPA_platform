# tasks:      id, payload (jsonb), status, result (jsonb), error_type, error_message, created_at, updated_at
# outbox:     id, task_id, topic, payload (jsonb), created_at, sent_at
# robot_runs: id, task_id, attempt, status, duration_ms, error, created_at   -- UNIQUE(task_id, attempt)
from tortoise import BaseDBAsyncClient


async def upgrade(db: BaseDBAsyncClient) -> str:
    return """
        CREATE TABLE IF NOT EXISTS "aerich" (
    "id" SERIAL NOT NULL PRIMARY KEY,
    "version" VARCHAR(255) NOT NULL,
    "app" VARCHAR(100) NOT NULL,
    "content" JSONB NOT NULL
);
CREATE TABLE IF NOT EXISTS "sources" (
    "id" BIGSERIAL NOT NULL PRIMARY KEY,
    "type" VARCHAR(255) NOT NULL,
    "active" BOOL NOT NULL  DEFAULT True,
    "name" VARCHAR(255) NOT NULL,
    "reference" VARCHAR(255) NOT NULL,
    "extra" VARCHAR(300),
    "status" VARCHAR(255) NOT NULL,
    "older_date" DATE,
    "updated_at" TIMESTAMPTZ NOT NULL  DEFAULT CURRENT_TIMESTAMP,
    "created_at" TIMESTAMPTZ NOT NULL  DEFAULT CURRENT_TIMESTAMP
);
CREATE TABLE IF NOT EXISTS "metricdata" (
    "id" BIGSERIAL NOT NULL PRIMARY KEY,
    "date" DATE NOT NULL,
    "metric" VARCHAR(255) NOT NULL,
    "value" DOUBLE PRECISION NOT NULL,
    "source_id" BIGINT NOT NULL REFERENCES "sources" ("id") ON DELETE CASCADE
);
CREATE TABLE IF NOT EXISTS "source_fetches" (
    "id" BIGSERIAL NOT NULL PRIMARY KEY,
    "error" VARCHAR(10000),
    "page" VARCHAR(5000),
    "tag" VARCHAR(255),
    "from_date" DATE NOT NULL,
    "to_date" DATE NOT NULL,
    "rows_count" BIGINT,
    "finished_at" TIMESTAMPTZ,
    "failed_at" TIMESTAMPTZ,
    "retried_at" TIMESTAMPTZ,
    "created_at" TIMESTAMPTZ NOT NULL  DEFAULT CURRENT_TIMESTAMP,
    "source_id" BIGINT NOT NULL REFERENCES "sources" ("id") ON DELETE CASCADE
);"""


async def downgrade(db: BaseDBAsyncClient) -> str:
    return """
        """

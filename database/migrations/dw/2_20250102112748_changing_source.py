from tortoise import BaseDBAsyncClient


async def upgrade(db: BaseDBAsyncClient) -> str:
    return """
        ALTER TABLE "sources" DROP COLUMN "reference";
        ALTER TABLE "sources" DROP COLUMN "extra";"""


async def downgrade(db: BaseDBAsyncClient) -> str:
    return """
        ALTER TABLE "sources" ADD "reference" VARCHAR(255) NOT NULL;
        ALTER TABLE "sources" ADD "extra" VARCHAR(300);"""

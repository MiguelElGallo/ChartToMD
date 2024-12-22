import asyncio

import typer
from azure.identity.aio import DefaultAzureCredential
from mediadescriber import ContentUnderstandingDescriber
from pydantic import Field
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    cu_secret: str = Field(..., env="CU_SECRET")

    class Config:
        env_file = ".env"


app = typer.Typer()


@app.command()
def run_cli(image_path: str, endpoint: str):
    async def _run():
        # ...class definitions from the provided code snippet...
        # ...existing code...
        credential = DefaultAzureCredential()
        describer = ContentUnderstandingDescriber(endpoint, credential)
        await describer.create_analyzer()
        with open(image_path, "rb") as f:
            image_bytes = f.read()
        description = await describer.describe_image(image_bytes)
        print(description)

    asyncio.run(_run())


if __name__ == "__main__":
    app()

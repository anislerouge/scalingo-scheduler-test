import uvicorn
from loguru import logger
from os import environ


PORT = int(environ.get("PORT", '8000'))

def serve():
    """Run function for Scalingo, see `Procfile`"""
    logger.info(f"Running uvicorn on {PORT}")
    uvicorn.run("api.app:app", host="0.0.0.0", port=PORT, workers=1)


if __name__ == '__main__':
    serve()

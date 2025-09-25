import dotenv

dotenv.load_dotenv()

from app import app


if __name__ == "__main__":
    import multiprocessing
    import uvicorn
    multiprocessing.freeze_support()
    uvicorn.run(app, host="0.0.0.0", port=8000)

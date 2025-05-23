import uvicorn

from contextlib import asynccontextmanager
from fastapi import FastAPI

from core.database import recreate_db
from src.api.dependencies import err_handlers
from src.api.v1.progress import progress_router
from src.api.v1.task import task_router


@asynccontextmanager
async def lifespan(app: FastAPI):
    recreate_db()
    yield


app = FastAPI(debug=True, lifespan=lifespan)

for exception, handler in err_handlers.items():
    app.add_exception_handler(exception, handler)

app.include_router(task_router, prefix="/api/v1", tags=["Tasks"])
app.include_router(progress_router, prefix="/api/v1", tags=["Progress"])


if __name__ == "__main__":
    recreate_db()
    uvicorn.run("main:app", host="127.0.0.1", port=5000, reload=True)

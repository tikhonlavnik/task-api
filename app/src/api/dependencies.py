from starlette.requests import Request
from starlette.responses import JSONResponse

from core.exceptions import AppError


async def app_error_handler(request: Request, exc: AppError):
    return JSONResponse(
        status_code=exc.status_code,
        content={"error": exc.detail, "type": exc.__class__.__name__},
    )


err_handlers = {
    AppError: app_error_handler,
    # other errs
}

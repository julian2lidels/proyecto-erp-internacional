from fastapi import Request
from fastapi.responses import JSONResponse
import logging

async def global_exception_handler(request: Request, exc: Exception):
    logging.error(f"Error en {request.url.path}: {str(exc)}")
    return JSONResponse(
        status_code=500,
        content={"error": "Error interno del servidor", "detalle": str(exc)}
    )
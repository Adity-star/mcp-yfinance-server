import asyncio
from source.yf_server import mcp
import uvicorn


def main():
    from starlette.middleware import Middleware
    from starlette.middleware.cors import CORSMiddleware

    # Build the ASGI app
    asyncio.run(mcp.run_stdio_async())
    # http_app = mcp.streamable_http_app(
    #     path="/mcp",  # default mount point for HTTP transport
    # )

    # uvicorn.run(http_app, host="0.0.0.0", port=8000)


if __name__ == "__main__":
    main()

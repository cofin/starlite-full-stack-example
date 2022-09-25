import logging

import anyio
from app.config import paths
from starlite import MediaType, NotFoundException, Response, get

logger = logging.getLogger()


@get(path=paths.urls.INDEX, media_type=MediaType.HTML, cache=False, tags=["Index"], include_in_schema=False)
async def site_index() -> Response:
    """Site index"""
    exists = await anyio.Path(paths.PUBLIC_DIR / "index.html").exists()
    if exists:
        async with await anyio.open_file(anyio.Path(paths.PUBLIC_DIR / "index.html")) as file:
            content = await file.read()
            return Response(content=content, status_code=200, media_type=MediaType.HTML)
    raise NotFoundException("Site index was not found")


@get(path="/test", media_type=MediaType.HTML, cache=False, tags=["Index"], include_in_schema=False)
async def authenticated_test() -> Response:
    """Site index"""
    exists = await anyio.Path(paths.PUBLIC_DIR / "index.html").exists()
    if exists:
        async with await anyio.open_file(anyio.Path(paths.PUBLIC_DIR / "index.html")) as file:
            content = await file.read()
            return Response(content=content, status_code=200, media_type=MediaType.HTML)
    raise NotFoundException("Site index was not found")

from ssl import SSLContext
from typing import Any, Iterable, Mapping, Optional, Union

from aiohttp import ClientTimeout
from aiohttp.helpers import BasicAuth
from aiohttp.typedefs import LooseCookies, LooseHeaders, StrOrURL
from multidict import CIMultiDict


class Request:
    def __init__(
        self,
        method: str,
        url: str,
        *,
        params: Optional[Mapping[str, str]] = None,
        data: Any = None,
        json: Any = None,
        cookies: Optional[LooseCookies] = None,
        headers: Optional[LooseHeaders] = None,
        skip_auto_headers: Optional[Iterable[str]] = None,
        auth: Optional[BasicAuth] = None,
        allow_redirects: bool = True,
        max_redirects: int = 10,
        compress: Optional[str] = None,
        chunked: Optional[bool] = None,
        expect100: bool = False,
        read_until_eof: bool = True,
        proxy: Optional[StrOrURL] = None,
        proxy_auth: Optional[BasicAuth] = None,
        proxy_headers: Optional[LooseHeaders] = None,
        timeout: Union[ClientTimeout, object] = None,
        verify_ssl: Optional[bool] = None,
        read_bufsize: Optional[int] = None,
        trace_request_ctx=None,
        ssl_context: Optional[SSLContext] = None,
    ):
        self.method = method
        self.url = url
        self.params = params
        self.data = data
        self.json = json
        self.cookies = cookies
        self.headers = self.prepare_headers(headers)
        self.skip_auto_headers = skip_auto_headers
        self.auth = auth
        self.allow_redirects = allow_redirects
        self.max_redirects = max_redirects
        self.compress = compress
        self.chunked = chunked
        self.expect100 = expect100

        self.read_until_eof = read_until_eof
        self.proxy = proxy
        self.proxy_headers = proxy_headers
        self.proxy_auth = proxy_auth
        self.timeout = timeout
        self.verify_ssl = verify_ssl
        self.read_bufsize = read_bufsize
        self.trace_request_ctx = trace_request_ctx
        self.ssl_context = ssl_context

    def prepare_headers(self, headers):
        if not headers:
            return CIMultiDict()

        new_headers = CIMultiDict(headers)
        for header, value in headers.items():
            new_headers[header.lower()] = value
        return new_headers

    @property
    def request_kwargs(self):
        return {key: value for key, value in self.__dict__.items() if value is not None}

meandmymonkey/simpleproxy
=========================

Publish linked containers as name-based hosts.

This container provides a basic HTTP reverse proxy for
simple use cases and experiments. It makes the single
assumption that connected containers publish their
services on internal port 80.


Usage
-----

Hosts are configured by setting the environment variable 
```PROXY_MAP``` to a JSON formatted string mapping linked
container names to host names:

```
docker run -d -p 80:80 \
    -e PROXY_MAP='{"app1": "foo.com", "app2": "bar.net"}' \
    --link somecontainer:app1 --link anothercontainer:app2 \
    meandmymonkey/simpleproxy
```
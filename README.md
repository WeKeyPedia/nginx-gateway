## mechanism

When container is started:

- it reads the `etcd` http API and looks for enabled subdomains within the CoreOS space
- it creates subsequents nginx config files
- start a simple nginx

The intent is to make every apps contained in a CoreOS host available as separed subdomains instead of the localhost + random ports logic.

### example

```
[api container:3000] ---> api.localhost:80
[front container:3000] ---> front.localhost:80

+ dev mode:

[neo4j container:7474] ---> neo4j.localhost:80
```


## usage

```shell
$ docker run -d -p 80:80 wekeypedia/nginx-localhost
```

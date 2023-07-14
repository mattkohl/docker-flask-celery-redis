# Docker Flask Celery Redis

A basic [Docker Compose](https://docs.docker.com/compose/) template for orchestrating a [Flask](http://flask.pocoo.org/) application & a [Celery](http://www.celeryproject.org/) queue with [Redis](https://redis.io/)

### Installation

```bash
git clone https://github.com/mattkohl/docker-flask-celery-redis
```

### Build & Launch

```bash
docker-compose up -d --build
```

### Enable hot code reload

```
docker-compose -f docker-compose.yml -f docker-compose.development.yml up --build
```

This will expose the Flask application's endpoints on port `5001` as well as a [Flower](https://github.com/mher/flower) server for monitoring workers on port `5555`

To add more workers:
```bash
docker-compose up -d --scale worker=5 --no-recreate
```

To shut down:

```bash
docker-compose down
```


To change the endpoints, update the code in [api/app.py](api/app.py)

Task changes should happen in [celery-queue/tasks.py](celery-queue/tasks.py) 


### Setup considerations

From: [Redis administration](https://redis.io/docs/management/admin/)

```
Make sure to set Linux kernel overcommit memory setting to 1.

This can be done by adding vm.overcommit_memory=1 to /etc/sysctl.conf. Then, reboot or run the command sysctl vm.overcommit_memory=1 to activate the setting.
```

---

adapted from [https://github.com/itsrifat/flask-celery-docker-scale](https://github.com/itsrifat/flask-celery-docker-scale)

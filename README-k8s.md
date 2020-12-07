### Installation

```bash
git clone https://github.com/mattkohl/docker-flask-celery-redis

```

### OPTIONAL: To build your own image

```bash
docker login
./build [YOUR_DOCKER_HUB_ID]

```

### to run using kubectl using my image
```bash
kubectl apply -f k8s/

```

### to use your own replace it with your own docker hub id
```bash
$ grep -in "image: teochenglim" k8s/*
k8s/monitor.yml:29:        image: teochenglim/celery-monitor
k8s/web.yml:16:      - image: teochenglim/celery-api
k8s/worker.yml:16:      - image: teochenglim/celery-worker

$ grep -in "image: teochenglim" k8s/*
k8s/monitor.yml:29:        image: [YOUR_DOCKER_HUB_ID]/celery-monitor
k8s/web.yml:16:      - image: [YOUR_DOCKER_HUB_ID]/celery-api
k8s/worker.yml:16:      - image: [YOUR_DOCKER_HUB_ID]/celery-worker

```

### Open this using browser to see it in action

```bash
$ open http://localhost:30010

```

### To play with it, assume you also using minikube and using local NodePort

```bash
$ curl -s http://localhost:30011/add/4/3

```

### To test k8s HPA, please use below to generate traffic

```bash
$ yes 'curl -s http://localhost:30011/add/4/3' | sh

```

### To monitor HPA

```bash
$ kubectl get hpa -w

```

### To shut down:

```bash
kubectl delete -f k8s/

```

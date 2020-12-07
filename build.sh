docker_hub_account=${1:-teochenglim}
docker build -f api/Dockerfile                  -t ${docker_hub_account}/celery-api     api/
docker build -f celery-queue/Dockerfile         -t ${docker_hub_account}/celery-worker  celery-queue/
docker build -f celery-queue/Dockerfile.monitor -t ${docker_hub_account}/celery-monitor celery-queue/
docker push ${docker_hub_account}/celery-api:latest
docker push ${docker_hub_account}/celery-worker:latest
docker push ${docker_hub_account}/celery-monitor:latest

VER=0.0.1
build:
	docker build . -t ticktick-exporter -t pawelflajszer/ticktick-exporter:${VER} -t pawelflajszer/ticktick-exporter:latest -f deployment/Dockerfile
run:
	docker run --env-file=${TICKTICK_EXPORTER_DOTENV_FILEPATH} --mount type=bind,source=${TICKTICK_EXPORTER_BACKUP_DIRPATH},target=/app/db/ticktick pawelflajszer/ticktick-exporter:latest
cleanup:
	docker image rm pawelflajszer/ticktick-exporter:latest -f
	docker image rm pawelflajszer/ticktick-exporter:${VER} -f
pull:
	docker pull pawelflajszer/ticktick-exporter:latest
push:
	docker push pawelflajszer/ticktick-exporter:${VER}
	docker push pawelflajszer/ticktick-exporter:latest
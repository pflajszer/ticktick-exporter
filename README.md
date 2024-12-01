# Overview

TickTick Exporter enables you to safely backup your TickTick **Tasks** and **Habits** locally.

# Quickstart

1. save `.env.example` & `Makefile` files from this repo on your host machine, or clone this repo
    - replace the values to your details
    - rename to `.env`
    - note down the path to that file 
2. add the below variables to `.bashrc` file (replace the values). Remember to run `source ~/.bashrc` after the update or reboot:
```bash
# ticktick-exporter
export TICKTICK_EXPORTER_DOTENV_FILEPATH=/home/user/repos/ticktick-export/.env # .env file path. you can download `.env.example` file from this repo and fill in the variables
export TICKTICK_EXPORTER_BACKUP_DIRPATH=/home/user/db/ticktick # a directory that will get mounted and where the script will download your backups. ensure this directory exists.
```
3. navigate to the folder where you downloaded `Makefile` to using the terminal
4. run `make run`
5. that's it! your `TICKTICK_EXPORTER_BACKUP_DIRPATH` directory should now be populated with todays backup of TickTick Tasks and Habits


# Deployment

1. Update `VER` variable in `Makefile` (optional)
2. Run:
```bash
make build && make push
```

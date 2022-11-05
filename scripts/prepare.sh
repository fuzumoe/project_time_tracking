#!/bin/sh

dir=$(pwd)/backend_plentific/data

sudo rm -r "${dir}/db/test_backup.sql"
sudo apt-get -y install rar
unrar e "${dir}/db/test_backup.part01.rar"
mv test_backup.sql  "${dir}/db/test_backup.sql"

sudo rm -r "${dir}/pp-data"
sudo rm -r *.csv
mkdir -p "${dir}/pp-data"

sudo apt-get -y install rar
unrar e "${dir}/pp-data.rar"

 mv *.csv  "${dir}/pp-data/"

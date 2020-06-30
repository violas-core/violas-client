#!/bin/sh

cd ..

cp canoser/ violas_client/ -rf
cp crypto/ violas_client/ -rf
cp error/ violas_client/ -rf
cp json_rpc/ violas_client/ -rf
cp lbrtypes/ violas_client/ -rf
cp libra_client/ violas_client/ -rf
cp move_core_types/ violas_client/ -rf

git mv exchange_client/ violas_client/
git mv extypes/ violas_client/

git mv canoser/ libra_client/
git mv crypto/ libra_client/
git mv error/ libra_client/
git mv json_rpc/ libra_client/
git mv lbrtypes/ libra_client/
git mv move_core_types/ libra_client/
git mv test/ libra_client/

git add violas_client/

cd ./script
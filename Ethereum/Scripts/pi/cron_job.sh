#!/bin/bash
if ps -ef | grep -v grep | grep geth ; then
	exit 0
else
	geth --datadir "/home/ubuntu/Desktop/private/blockchain/" --networkid 3141592 --nat extip:52.34.24.43 --port 30303 console
fi
#!/bin/sh
echo "Waiting for signal..."
echo "pid=$$"

# Sleeping in the background seems to do the job
sleep infinity &
wait $!

# ADD YOUR CODE HERE
echo "Received arbitrary signal"

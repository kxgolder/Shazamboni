#!/bin/bash

sudo mv car_controller.service /lib/systemd/system/
sudo systemd enable car_controller.service
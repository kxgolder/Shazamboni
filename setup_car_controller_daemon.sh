#!/bin/bash

mv car_controller.service /lib/systemd/system/
systemd enable car_controller.service
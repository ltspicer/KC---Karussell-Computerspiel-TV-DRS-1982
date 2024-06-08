#!/bin/sh

HOME="$(getent passwd $USER | awk -F ':' '{print $6}')"
cd ${HOME}/kc.linux ; ./kc # Hier ggf. Pfad innerhalb des home Verzeichnisses anpassen !!!


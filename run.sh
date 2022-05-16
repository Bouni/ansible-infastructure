#!/bin/sh

ansible-playbook --extra-vars '@vault.yml' --diff $@

#!/usr/bin/env bash

main() {
    python -m pytest "$@"
}

main "$@"

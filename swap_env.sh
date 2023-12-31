#!/bin/bash

# Check if both files exist
if [ -e .env ] && [ -e local.env ]; then
  # Generate temporary file names
  temp_env=".env.temp"
  temp_local_env="local.env.temp"

  # Rename the files
  mv .env "$temp_env"
  mv local.env "$temp_local_env"

  # Swap the temporary names
  mv "$temp_env" local.env
  mv "$temp_local_env" .env

  env_type=$(cat .env | grep "ENV_TYPE" | cut -d '=' -f 2)
  echo "ENV_TYPE was set to: $env_type"
else
  echo "Something went wrong. Check your .env and local.env files"
fi
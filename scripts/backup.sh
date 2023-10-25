#!/bin/bash

DATE=$(date +%Y-%m-%d_%H%M%S)
BACKUP_FILE="/backup/files_$DATE.sql"
docker exec postgres pg_dump -U postgres -d mydb > $BACKUP_FILE
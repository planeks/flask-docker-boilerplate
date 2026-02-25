## Backups

### Automated backups (provisioned servers)

If you provisioned the server with Ansible, a weekly cron job is already set up. It runs `scripts/backup.sh` which:
- Creates a database dump inside the postgres container
- Cleans up backups older than 28 days

The backup role configures this automatically for production environments.

### Manual backup

Run the backup script directly on the server:

```bash
cd ~/projects/flask_app
./scripts/backup.sh compose.prod.yml ~/projects/flask_app
```

Or via SSH:

```bash
ssh -i <your-key> <user>@<server_ip> "cd ~/projects/flask_app && ./scripts/backup.sh"
```

### Listing backups

```bash
docker compose -f compose.prod.yml exec -T postgres backups
```

## Restore from backup

Stop the app containers that use the database:

```bash
docker compose -f compose.prod.yml stop flask celeryworker
```

Restore the database from a specific dump:

```bash
docker compose -f compose.prod.yml exec -T postgres restore <dump_name>
```

Start the containers again:

```bash
docker compose -f compose.prod.yml up -d flask celeryworker
```

## Cleaning Docker data

Optionally set up a cron job to prune unused Docker data:

```bash
sudo crontab -e
```

Add:

```bash
0 2 * * *       docker system prune -f >> /home/appuser/docker_prune.log 2>&1
```

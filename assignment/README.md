# FastAPI Docker Compose Assignment

This project containerizes Lab 1 and Lab 2 FastAPI applications using Docker Compose.

## Project Structure

```
assignment/
├── docker-compose.yml    # Docker Compose configuration
├── requirements.txt      # Python dependencies
├── lab1/
│   ├── Dockerfile
│   └── main.py          # In-memory FastAPI (Lab 1)
└── lab2/
    ├── Dockerfile
    └── main.py          # Database-integrated FastAPI (Lab 2)
```

## Prerequisites

- Docker
- Docker Compose

## Quick Start

1. **Build and start all services:**
   ```bash
   docker compose up -d
   ```

2. **Verify containers are running:**
   ```bash
   docker compose ps
   ```

3. **Test the endpoints:**

   ### Lab 1 (In-Memory) - Port 8001
   ```bash
   # Swagger UI
   http://localhost:8001/docs
   
   # GET all items
   curl http://localhost:8001/items
   
   # POST create item
   curl -X POST http://localhost:8001/items \
     -H "Content-Type: application/json" \
     -d '{"name":"Test Item","description":"Test"}'
   
   # DELETE item
   curl -X DELETE http://localhost:8001/items/1
   ```

   ### Lab 2 (Database) - Port 8002
   ```bash
   # Swagger UI
   http://localhost:8002/docs
   
   # GET all items
   curl http://localhost:8002/items
   
   # POST create item (stored in persistent volume)
   curl -X POST http://localhost:8002/items \
     -H "Content-Type: application/json" \
     -d '{"name":"Database Item","description":"Persistent"}'
   
   # DELETE item
   curl -X DELETE http://localhost:8002/items/1
   ```

## Key Features

- **Lab 1 (Port 8001)**: In-memory storage - data is reset on container restart
- **Lab 2 (Port 8002)**: SQLite database with persistent Docker volume
  - Database stored at `/app/data/items.db` inside the container
  - Volume: `db-volume` - persists data across container restarts
- **Networking**: Both services communicate through a custom Docker network

## Database Persistence

The Lab 2 database is stored in a Docker volume named `db-volume`. This ensures:
- Data survives container restarts
- Data is independent of the container lifecycle

To verify the volume:
```bash
docker volume ls
docker volume inspect assignment_db-volume
```

## Stop Services

```bash
docker compose down
```

## Stop Services and Remove Volume (Clean Reset)

```bash
docker compose down -v
```

This will delete the database volume and reset all data.

## Troubleshooting

### Services won't start
```bash
docker compose logs lab1
docker compose logs lab2
```

### Port already in use
- Lab 1 uses port 8001
- Lab 2 uses port 8002
- Check if these ports are available: `netstat -ano | findstr :8001` (Windows)

### Need to rebuild after code changes
```bash
docker compose up -d --build
```

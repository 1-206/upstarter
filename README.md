# Upstarter

A startup finder application. Find a project to particate or to invest in.

## Development

To start the development process clone the repository with the latest changes.
In the project's root directory execute the following command:

```
echo "DOCKER_USER=$UID" > .env && ln -s docker-compose.dev.yml docker-compose.yml
```

This will set your user as a default user for the docker containers and set
development docker compose file as a main compose file.

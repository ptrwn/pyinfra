#### Homework 4 steps
----------------------------
##### stateful set with persistent volume
##### use init container instead of configmap init script -- nope, does not work, leaving configmap init
##### helm chart for psql



```bash
The error indicates that the psql command in the init container is trying to connect to a PostgreSQL server on the same container, but the server is not running because it's part of the main postgres container, which hasn't started yet. Init containers run before the main container, so the psql command won't find the database server.

that's strange - previously, before I added the command, I saw in init container logs that it has successfully create database records

---------------------

You're right—it may seem contradictory. This discrepancy can happen due to differences in how the PostgreSQL image handles initialization when the init container runs and how it's set up to execute SQL files.

Let's break this down:

1. Why Did the Init Container Previously Succeed?
Default PostgreSQL Behavior: The official PostgreSQL image automatically initializes the database from .sql files placed in /docker-entrypoint-initdb.d/ if the database is being created for the first time.
If the database already exists, the PostgreSQL container skips initialization during startup, and any additional .sql scripts executed by the init container might succeed because the database server was ready.
2. Why Does the psql Command Now Fail?
When you explicitly added the command to the init container, it began running the psql command independently.
However, the main postgres container (and the database server) doesn't start until after the init container finishes. Therefore, the psql command in the init container cannot connect to the database.

```
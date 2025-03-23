#### Homework 5 steps
----------------------------

##### helm chart for psql


start:
```bash
 helm upgrade --install my-fastapi-db . \
  --set image.repository=fastapi-local \
  --set image.pullPolicy=IfNotPresent --debug
```
stop:
```bash
 helm uninstall my-fastapi-db
```

pvc does not get removed upon helm uninstall:

```bash
 kubectl get pvc
 kubectl delete pvc --all
```

all events:
```bash
kubectl get events --sort-by=.metadata.creationTimestamp
```

troubleshooting:

```bash
 kubectl describe statefulset postgres


Events:
  Type     Reason        Age                    From                    Message
  ----     ------        ----                   ----                    -------
  Warning  FailedCreate  100s (x16 over 4m17s)  statefulset-controller  create Pod postgres-0 in StatefulSet postgres failed error: Pod "postgres-0" is invalid: spec.initContainers[0].volumeMounts[0].name: Not found: "db-init-scripts"

 kubectl logs postgres-0
```


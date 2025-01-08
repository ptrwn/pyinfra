#### Homework 3 steps
----------------------------

1. Write yamls, or get ChatGPT to do that for you.

2. Run docker desktop, then run minikube:

```bash
 $  minikube status
 $  minikube start
```

3. Run deployments, then services:

```bash
 $  kubectl apply -f k8s/db-deployment.yaml
 $  kubectl apply -f k8s/db-service.yaml
 $  kubectl apply -f k8s/fastapi-deployment.yaml
 $  kubectl apply -f k8s/fastapi-service.yaml
```

4. Unhappy path, troubleshooting:
```bash
 $ kubectl describe pods db-deployment
 $ kubectl logs  db-deployment-59bc7c4b87-4tj86
```

5. Found error in log:
```bash
Events:
  Type     Reason       Age                 From               Message
  ----     ------       ----                ----               -------
  Normal   Scheduled    15m                 default-scheduler  Successfully assigned default/db-deployment-59bc7c4b87-4tj86 to minikube
  Warning  FailedMount  21s (x15 over 15m)  kubelet            MountVolume.SetUp failed for volume "init-scripts" : configmap "db-init-scripts" not found
```

6. Access the app:
```bash
$ kubectl get svc fastapi-service # get port
$ minikube ip # get IP
```

If this does not work, do:
```bash
$ minikube service fastapi-service
```
This will create a tunnel for the service and make it available in browser.
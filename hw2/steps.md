#### Homework 2 steps
----------------------------

1. Build Docker image using the minimal FastAPI app from homework 1:

```bash
$ docker build -t myfastapi .
```

2. Check locally that it works:

```bash
$ docker run -it -p 8008:8008 ptrwn/myfastapi:latest
```

3. Add dockerhub repo name to image tag and push the image to dockerhub repo:

```bash
$ docker tag myfastapi:latest ptrwn/myfastapi:latest
$ docker login
$ docker push ptrwn/myfastapi:latest
```

4. Create and run a pod in local minikube:
```bash
$ kubectl run hello --image=ptrwn/myfastapi:latest
```

5. Forward port to expose it:
```bash
$ kubectl port-forward hello 5555:8008
```
Check that `http://127.0.0.1:5555/health` opens in browser.

6. Delete the pod:
```bash
$ kubectl delete pod hello
```

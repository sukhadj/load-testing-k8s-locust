#!/bin/bash

# docker build -t add-event-agg .
# docker tag add-event-agg sukhadj/add-event-agg-k8s:latest
# docker push sukhadj/add-event-agg-k8s:latest

kubectl apply -f flask-app.yml
POD=$(kubectl get pod -l app=flask -o jsonpath="{.items[0].metadata.name}")
kubectl logs $POD

kubectl autoscale deployment ad-events-agg --cpu-percent=50 --min=1 --max=10  
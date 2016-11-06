#!/bin/bash

curl -H "Content-Type: application/json" --data @create_budget.json localhost:5000/api/budget/create

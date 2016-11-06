#!/bin/bash

curl -H "Content-Type: application/json" --data @add_budget_item.json localhost:5000/api/budget/add

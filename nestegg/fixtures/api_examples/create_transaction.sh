#!/bin/bash

curl -H "Content-Type: application/json" --data @create_transaction.json localhost:5000/api/transaction/create

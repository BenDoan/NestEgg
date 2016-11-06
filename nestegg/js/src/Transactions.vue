<template>
    <div id="app">
        <h2>Transactions</h2>
        <h3>Add entry</h3>
        <div class="form-inline">
            <div class="form-group">
                <input v-model="newTran.title" type="text" placeholder="Title" class="form-control" >
            </div>

            <div class="form-group">
                <div class="input-group">
                    <div class="input-group-addon">$</div>
                    <input v-model="newTran.amount" type="number" min="0.01" step="0.01" max="2500" placeholder="Amount" class="form-control">
                </div>
            </div>

            <div class="form-group">
                <input v-model="newTran.date" type="date" placeholder="Date" class="form-control">
            </div>

            <div class="form-group">
                <select v-model="newTran.category" class="form-control">
                    <option v-for="(subcat, i) in budget_subcategories">{{ subcat[0] }}/{{ subcat[1] }}</option>
                </select>
            </div>
            <button v-on:click="addNewTransaction()" class="btn">Add</button>
        </div>
        <br>
        <table class="table table-hover">
            <tr>
                <th></th>
                <th>Title</th>
                <th>Amount</th>
                <th>Date</th>
                <th>Category</th>
            </tr>
            <tr v-for="(transaction, i) in transactions">
                <td></td>
                <td>{{ transaction['title'] }}</td>
                <td>{{ transaction['amount'] }}</td>
                <td>{{ transaction['date'] }}</td>
                <td>{{ transaction['budget_item'].join('/') }}</td>
            </tr>
        </table>

    </div>
</template>

<script>
import global from './global'

export default {
    name: "transactions",
    data () {
       return {
        global: global,
        transactions: {},
        newTran: {},
        budget_subcategories: []
       }
    },
    created: function(){
        this.axios.get("/api/transaction/get/all").then((response) => {
            this.transactions = response.data
        })
        this.axios.get("/api/subcategory/all/get").then((response) => {
            this.budget_subcategories = response.data
        })
    },
    methods: {
        addNewTransaction: function (event){
            let newTran = this.newTran
            newTran['budget_item'] = newTran['category'].split("/")

            this.transactions.push(newTran)
            this.newTran = {}

            this.axios.post("/api/transaction/create", newTran).then((response) => {
            })
        }
    }
}
</script>

<style lang="stylus">
select, button, input
    color: #000
</style>

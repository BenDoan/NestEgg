<template>
    <div id="app">
        <h2>Transactions</h2>
        <table class="table table-hover">
            <tr>
                <th></th>
                <th>Title</th>
                <th>Amount</th>
                <th>Date</th>
                <th>Category</th>
            </tr>
            <tr v-for="(transaction, i) in transactions">
                <td>{{ transaction['title'] }}</td>
                <td>{{ transaction['amount'] }}</td>
                <td>{{ transaction['date'] }}</td>
                <td>{{ transaction['budget_item'].join('/') }}</td>
            </tr>
        </table>

        <input type="text" placeholder="Title">
        <input type="text" placeholder="Amount">
        <input type="text" placeholder="Date">
        <select>
            <option>utilities/gas</option>
        </select>
        <button v-on:click="transactions.push({})">Add row</button>
    </div>
</template>
<script>
import global from './global'
import Table from './Table.vue'
export default {
    name: "transactions",
    components: {
        'edi-table': Table
    },
    data () {
       return {
        global: global,
        keys: {
            "date": "date",
            "amount": "money",
            "desc": "text"
        },
        rows: [],
        transactions: {}
       }
    },
    created: function(){
        this.axios.get("/api/transaction/get/all").then((response) => {
            this.transactions = response.data
        })
    }
}
</script>

<style lang="stylus">
select, button, input
    color: #000
</style>

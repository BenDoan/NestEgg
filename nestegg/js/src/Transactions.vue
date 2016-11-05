<template>
    <div id="app">
        <h1>Transactions for {{ global.budget }}</h1>
        <edi-table v-bind:keys="keys" v-bind:rows="rows"></edi-table>
        <pre>
            {{ transactions['total_budgeted'] }}
        </pre>
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
        this.axios.get("/api/homeinfo/get").then((response) => {
            this.transactions = response.data
        })
    }
}
</script>

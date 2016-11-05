<template>
    <div id="app">
    <h1>Transactions</h1>
        <edi-table v-bind:keys="keys" v-bind:rows="rows" v-bind:notify="save"></edi-table>
    </div>
</template>
<script>
import Table from './Table.vue'
export default {
    components: {
        'edi-table': Table
    },
    data () {
       return {
        keys: {
            "date": "date",
            "amount": "money",
            "desc": "text"
        },
        rows: []
       }
    },
    name: "transactions"
}
</script>

<template>
    <div id="app">
        <h1>Transactions for {{ global.budget }}</h1>
        <edi-table v-bind:keys="keys" v-bind:rows="rows"></edi-table>
    </div>
</template>
<script>
import global from './global'
import Table from './Table.vue'
export default {
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
        rows: []
       }
    },
    name: "transactions"
}
</script>

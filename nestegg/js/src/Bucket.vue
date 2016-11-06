<template>
    <div id="app">
        <h2>Buckets</h2>
        <h3>Add entry</h3>
        <div class="form-inline">
            <div class="form-group">
                <input @keyup.enter="addNewBucket()" v-model="newBucket.name" type="text" placeholder="Name" class="form-control" >
                <div class="input-group">
                    <div class="input-group-addon">$</div>
                    <input @keyup.enter="addNewBucket()" v-model="newBucket.monthly_amount" placeholder="Amount" class="form-control" type="number" min="0.01" step="0.01" max="2500">
                </div>
            </div>
            <button v-on:click="addNewBucket()" class="btn">Add</button>
        </div>
        <br>
        <table class="table table-hover">
            <tr>
                <th></th>
                <th>Bucket</th>
                <th>Amount</th>
                <th>Monthly amount</th>
            </tr>
            <tr v-for="(bucket, i) in buckets">
                <td></td>
                <td>{{ bucket['name'] }}</td>
                <td>${{ bucket['amount'] }}</td>
                <td>${{ bucket['monthly_amount'] }}</td>
            </tr>
        </table>

    </div>
</template>

<script>
import global from './global'

export default {
    name: "buckets",
    data () {
       return {
        global: global,
        buckets: {},
           newBucket: {}
       }
    },
    created: function(){
        this.axios.get("/api/bucket/get/all").then((response) => {
            this.buckets = response.data
        })
    },
    methods: {
        addNewBucket: function (event){
            let newBucket = this.newBucket
            this.buckets.push(newBucket)
            this.newBucket = {}

            this.axios.post("/api/bucket/add", newBucket).then((response) => {
            })
        }
    }
}
</script>

<style lang="stylus">
select, button, input
    color: #000
</style>

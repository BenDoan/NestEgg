<template>
    <div id="app">
        <h2>Buckets</h2>
        <h3>Add entry</h3>
        <div class="form-inline">
            <div class="form-group">
                <input v-model="newBucket" type="text" placeholder="Title" class="form-control" >
            </div>
            <button v-on:click="addNewBucket()" class="btn">Add</button>
        </div>
        <br>
        <table class="table table-hover">
            <tr>
                <th></th>
                <th>Bucket</th>
                <th>Amount</th>
            </tr>
            <tr v-for="(bucket, i) in buckets">
                <td></td>
                <td>{{ bucket[0] }}</td>
                <td>{{ bucket[1] }}</td>
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
        newBucket: ""
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
            this.buckets.push([newBucket, 0])
            this.newBucket = ""

            this.axios.post("/api/bucket/add/"+newBucket).then((response) => {
            })
        }
    }
}
</script>

<style lang="stylus">
select, button, input
    color: #000
</style>

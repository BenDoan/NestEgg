<template>
<div id="app">
	<div class="holding"><h1 class="main_head">Accounts Overview</h1><div class="line"></div></div>
	<h2>Checking</h2>
	<p>$349.05</p>
	<h2>Savings</h2>
	<p>$1039.05</p>
	<h2>Transactions</h2>
    <table class="table table-hover">
        <thead>
            <tr>
                <th>Title</th>
                <th>Amount</th>
                <th>Date</th>
                <th>Category</th>
            </tr>
        </thead>
        <tbody>
            <tr v-for="(transaction, i) in transactions">
                <td>{{ transaction['title'] }}</td>
                <td>{{ transaction['amount'] }}</td>
                <td>{{ transaction['date'] }}</td>
                <td>{{ transaction['budget_item'].join('/') }}</td>
            </tr>
        </tbody>
    </table>
	<h2 class="head">Budget</h2>
	<div class="budget">
		{{ data["total_spent"] }}	{{ data["total_budgeted"] }}
	</div>
	<h2>Buckets</h2>
	<div class="row">
		<div v-for="(bucket,i) in data['buckets']" class="col-sm-3 bucket-pod">
			<h2>{{ bucket[name] }}</h2>
			<p>Amount Total: ${{ bucket[amount] }}</p>
		</div>
	</div>
</div>
</template>

<style lang="stylus" scoped>

.bar_holder
	background-color:black!important;
	height:20px!important;
	width:100%!important;

.progress-bar
	height:20px!important;
	background-color:greent;

.row
	margin-top:60px!important;
	padding-left:80px;

.bucket-pod
	padding-left:80px;
	margin-right:60px;
	border: 1px solid #ccc !important;
	padding:40px;
	border-radius:10px;

.bucket-pod > h2
	margin-top:10px;

.bucket-pod:hover
	background-color:#DDD;

</style>

<script>
export default {
name: "home",
    data () {
       return {
        global: global,
        transactions: {},
        data: {}
       }
    },
    created: function(){
        this.axios.get("/api/homeinfo/get").then((response) => {
            this.data = response.data
        })
        this.axios.get("/api/transaction/get/all").then((response) => {
            this.transactions = response.data
        })
    }
}
</script>

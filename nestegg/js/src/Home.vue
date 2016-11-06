<template>
<div id="app">
	<div class="holding"><h1 class="main_head">Accounts Overview</h1><div class="line"></div></div>
	<h2>Checking</h2>
	<div class="row">
		<div v-for="(bucket,i) in buckets"class="col-sm-3 bucket-pod">
			<h2>{{ bucket[name] }}</h2>
			<p>Amount Total: ${{ bucket[amount] }}</p>
		</div>
		<div class="col-sm-3 bucket-pod">
			<h2>Bucket Name</h2>
			<p>Amount Total: $100</p>
		</div>
		<div class="col-sm-3 bucket-pod">
			<h2>Bucket Name</h2>
			<p>Amount Total: $100</p>
		</div>
	</div>
	<h2>Savings</h2>
	<div class="row">
		<div class="col-sm-3 bucket-pod">
			<h2>Bucket Name</h2>
			<p>Amount Total: $100</p>
		</div>
		<div class="col-sm-3 bucket-pod">
			<h2>Bucket Name</h2>
			<p>Amount Total: $100</p>
		</div>
		<div class="col-sm-3 bucket-pod">
			<h2>Bucket Name</h2>
			<p>Amount Total: $100</p>
		</div>
	</div>
	<h2 class="head">Transactions</h2>
	<table class="table table-hover">
		<thead>
			<tr>
				<th>#</th>
				<th>Name</th>
				<th>Type</th>
				<th>Amount</th>
			</tr>
		</thead>
		<tbody>
		<tr>
			<td>1</td>
			<td>Transaction Name</td>
			<td>Type</td>
			<td>$Amount</td>
		</tr>
		<tr>
			<td>2</td>
			<td>Transaction Name</td>
			<td>Type</td>
			<td>$Amount</td>
		</tr>
		<tr>
			<td>3</td>
			<td>Transaction Name</td>
			<td>Type</td>
			<td>$Amount</td>
		</tr>
		<tr>
			<td>4</td>
			<td>Transaction Name</td>
			<td>Type</td>
			<td>$Amount</td>
		</tr>
		<tr>
			<td>5</td>
			<td>Transaction Name</td>
			<td>Type</td>
			<td>$Amount</td>
		</tr>
		</tbody>
	</table>
	<h2 class="head">Budget</h2>
	<table class="table table-hover">
		<thead>
			<tr>
				<th>#</th>
				<th>Name</th>
				<th>Type</th>
				<th>Amount</th>
			</tr>
		</thead>
		<tbody>
		<tr>
			<td>1</td>
			<td>Transaction Name</td>
			<td>Type</td>
			<td>$Amount</td>
		</tr>
		<tr>
			<td>2</td>
			<td>Transaction Name</td>
			<td>Type</td>
			<td>$Amount</td>
		</tr>
		<tr>
			<td>3</td>
			<td>Transaction Name</td>
			<td>Type</td>
			<td>$Amount</td>
		</tr>
		<tr>
			<td>4</td>
			<td>Transaction Name</td>
			<td>Type</td>
			<td>$Amount</td>
		</tr>
		<tr>
			<td>5</td>
			<td>Transaction Name</td>
			<td>Type</td>
			<td>$Amount</td>
		</tr>
		</tbody>
	</table>
</div>
</template>

<style lang="stylus" scoped>

/*
.bar_holder
background-color:black!important;
height:20px!important;
width:100%!important;

.progress-bar
height:20px!important;
background-color:greent;
 */

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
        buckets: {},
        newBucket: ""
       }
    },
    created: function(){
        this.axios.get("/api/homeinfo/get").then((response) => {
            this.buckets = response.data
        })
    }
}
</script>

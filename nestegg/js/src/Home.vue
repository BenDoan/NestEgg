<template>
<div id="app">
	<div class="holding"><h1 class="main_head">Accounts Overview</h1><div class="line"></div></div>
	<h2>Checking</h2>
	<p>349.05</p>
	<h2>Savings</h2>
	<p>1039.05</p>
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
			<td>105</td>
			<td>Scooter's Coffee House</td>
			<td>Food</td>
			<td>$6.10</td>
		</tr>
		<tr>
			<td>104</td>
			<td>BP</td>
			<td>Car</td>
			<td>$23.47</td>
		</tr>
		<tr>
			<td>103</td>
			<td>Scheel's</td>
			<td>Clothing</td>
			<td>$43.08</td>
		</tr>
		<tr>
			<td>102</td>
			<td>Runza</td>
			<td>Food</td>
			<td>$10.42</td>
		</tr>
		<tr>
			<td>101</td>
			<td>Famous Footwear</td>
			<td>Clothing</td>
			<td>$103.28</td>
		</tr>
		</tbody>
	</table>
	<h2 class="head">Budget</h2>
	<div class="budget">
		<div class="progress">
			<div class="progress-bar progress-bar-success" v-bind:style="{width: percent(data.total_spent/data.total_budgeted)}">
			</div>
		</div>
			{{Math.round((data.total_spent/data.total_budgeted * 100) * 100)/100}}%
			<br />
			${{data.total_spent}} / ${{data.total_budgeted}}
	</div>
	<h2>Buckets</h2>
	<div class="row">
		<router-link to = "/bucket">
		<div v-for="(amount,name,index) in data.buckets" class="col-sm-3 bucket-pod">
			<h2>{{ name}}</h2>
			<p>Amount Total: ${{amount }}</p>
		</div>
		</router-link>
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
					return { global: global,
						data: {}
					}
				},
created: function(){
					 this.axios.get("/api/homeinfo/get").then((response) => {
							 this.data= response.data
							 })
				 },
methods: {
					 percent(v){
						 return (v*100)+"%";
					 }
				 }
}
</script>

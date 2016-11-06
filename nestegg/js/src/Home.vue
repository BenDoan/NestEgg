<template>
    <div id="app">
				<div class="holding"><h1 class="main_head">Accounts Overview</h1><div class="line"></div></div>
				<h2>Checking</h2>
				<table class="table table-hover">
					<thead>
						<tr>
							<th>Bucket</th>
							<th>% Used</th>
						</tr>
					</thead>
					<tbody>
					<tr>
						<td>Gas</td>
						<td>20%</td>
					</tr>
					<tr>
						<td>Rent</td>
						<td>100%</td>
					</tr>
					<tr>
						<td>Gas</td>
						<td>20%</td>
					</tr>
					</tbody>

				</table>
				<h2>Savings</h2>
				<table class="table table-hover">
					<thead>
						<tr>
							<th>Bucket</th>
							<th>% Used</th>
						</tr>
					</thead>
					<tbody>
					<tr>
						<td>Gas</td>
						<td>20%</td>
					</tr>
					<tr>
						<td>Rent</td>
						<td>100%</td>
					</tr>
					</tbody>

				</table>
				<h2 class="head">Transactions</h2><!--<div class="line"></div>-->
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

<div class=".col-xs-6 .col-sm-4 bucket-pod">
	<h2>Bucket Name</h2>
	<p>Amount Total: 100$</p>
	<p>80%</p>

</div>
<div class=".col-xs-6 .col-sm-4 bucket-pod">
	<h2>Bucket Name</h2>
	<p>Amount Total: 100$</p>
	<p>80%</p>

</div>
<div class=".col-xs-6 .col-sm-4 bucket-pod">
	<h2>Bucket Name</h2>
	<p>Amount Total: 100$</p>
	<p>80%</p>

</div>

<script>
export default {
    name: "home"
}
</script>

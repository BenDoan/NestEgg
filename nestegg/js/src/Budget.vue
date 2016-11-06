<template>
    <div id="app">
        <h1>
            <button class="unbutton" v-on:click="jumpmonths(-1)"><span class="glyphicon glyphicon-chevron-left"></span></button>
            Budget for {{budget_year}}-{{budget_month+1}}
            <button class="unbutton" v-on:click="jumpmonths(1)"><span class="glyphicon glyphicon-chevron-right"></span></button>
        </h1>
        <template v-if="budget_exists">
            <div class="form-inline">
                Income:
                <div class="form-group">
                    <div class="input-group">
                        <div class="input-group-addon">$</div>
                        <input v-model="budget_income" type="number" min="0.01" step="0.01" max="2500" placeholder="Expected Income" class="form-control">
                    </div>
                </div>
                - ${{ bucket_amount }} = ${{ budget_income - bucket_amount }}
            </div>
            </br>
            <div class="alert alert-success">
                <p>You have allocated ${{ sum_all() }} of ${{ budget_income - bucket_amount }}</p>
                <div class="progress">
                    <div class="progress-bar progress-bar-success" v-bind:style="{width: percent(sum_all()/budget_income)}">
                    </div>
                </div>
            </div>
            <template v-for="(cat, i) in budget">
                <h2>
                    <template v-if="!cat.edit">
                        {{ cat.name }}
                        <button class="unbutton" v-on:click="cat.edit=true"><small><span class="glyphicon glyphicon-edit edit-button"></span></small></button>
                    </template>
                    <template v-if="cat.edit">
                        <div class="form-inline">
                            <div class="form-group">
                                <input type="text" v-model="cat.name" class="form-control" @keyup.enter="cat.edit=false; save_budget()"></input>
                            </div>
                            <div class="form-group">
                                <button class="unbutton" v-on:click="cat.edit=false; save_budget()"><span class="glyphicon glyphicon-ok edit-button"></span></button>
                            </div>
                            <div class="form-group">
                                <button class="unbutton" v-on:click="budget.splice(i, 1)"><span class="glyphicon glyphicon-remove edit-button"></span></button>
                            </div>
                        </div>
                    </template>
                </h2>
                <div class="gridbox" v-for="(item, j) in cat.items">
                    <template v-if="!item.edit">
                        <span>{{ item.name }}: ${{ item.amount }} (spent: ${{item.used}})</span>
                        <button class="unbutton" v-on:click="item.edit=true"><small><span class="glyphicon glyphicon-edit edit-button"></span></small></button>
                    </template>
                    <template v-if="item.edit">
                        <div class="form-inline">
                            <div class="form-group">
                                <input type="text" v-model="item.name" class="form-control" @keyup.enter="item.edit=false; save_budget()"></input>
                            </div>
                            <div class="form-group">
                                <input type="numeric" v-model="item.amount" class="form-control" @keyup.enter="item.edit=false; save_budget()"></input>
                            </div>
                            <div class="form-group">
                                <button class="unbutton" v-on:click="item.edit=false; save_budget()"><span class="glyphicon glyphicon-ok"></span></button>
                            </div>
                            <div class="form-group">
                                <button class="unbutton" v-on:click="cat.items.splice(j, 1)"><span class="glyphicon glyphicon-remove"></span></button>
                            </div>
                        </div>
                    </template>
                </div>
                <div class="gridbox">
                    <span class="unvisible">-</span>
                    <button class="unbutton" v-on:click="cat.items.push({name:'',edit:true,amount:100,used:0})"><span class="glyphicon glyphicon-plus"></span></button>
                </div>
            </template>
            <h2>
                <button class="unbutton" v-on:click="budget.push({name:'',edit:true,items:[]})"><span class="glyphicon glyphicon-plus"></span></button>
            </h2>
        </template>
        <template v-if="!budget_exists">
            <p>budget does not exist</p>
            <button v-on:click="create_budget()" class="btn btn-primary">Create a budget</button>
        </template>
    </div>
</template>
<script>
    export default {
        name: "budget",
        data () {
            return {
                shunt: {
                    name: "",
                    rows: []
                },
                edit_data: {
                    cat: null,
                    prev_key: "",
                    key: "",
                    type: "",
                    max: 0
                },
                edit: null,
                budget: [],
                structure: {},
                budget_year: 0,
                budget_month: 0,
                budget_list: [],
                budget_exists: true,
                budget_income: 0,
                bucket_amount: 200,
            };
        },
        created () {
            var now = new Date();
            this.budget_year = now.getFullYear();
            this.budget_month = now.getMonth();
            this.axios.get("/api/budgetmonths/get/all").then((response) => {
                if(response.data.length == 0){
                    this.axios.post("/api/budget/create",{
                        year: now.getFullYear(),
                        month: now.getMonth(),
                        income: 0,
                        items: {}
                    }).then((response) => {
                        console.log(response);
                        this.structure = {};
                    });
                } else {
                    response.data.sort((a,b) => {
                        return a[0]*100+a[1] - (b[0]*100+b[1]);
                    });
                    this.budget_list = response.data;
                }
            }, (error) => {
                console.log(error);
            });
            this.axios.get("/api/bucket/get/all").then((response) => {
                this.bucket_amount = 0;
                response.data.forEach((bucket) => {
                    this.bucket_amount += bucket.monthly_amount;
                });
            });
        },
        watch: {
            budget_year: "update_budget",
            budget_month: "update_budget",
            budget_income () {
                this.axios.post("/api/budget/setincome/"+this.budget_year+"/"+this.budget_month, {"income" : this.budget_income});
            }
        },
        methods: {
            sum_all (){
                var acc = 0;
                this.budget.forEach((cat) => {
                    cat.items.forEach((item) => {
                        acc += parseInt(item.amount);
                    });
                });
                return acc;
            },
            percent (v) {
                return (v*100)+"%";
            },
            create_budget () {
                var b = this.budget_list[this.budget_list.length-1];
                this.axios.get("/api/budget/get/"+b[0]+"/"+b[1]).then((response) => {
                    response.data.year = this.budget_year;
                    response.data.month = this.budget_month;
                    this.axios.post("/api/budget/create",response.data).then((response) => {
                        this.update_budget();
                    });
                });
            },
            save_budget () {
                console.log("BEGIN SAVE");
                this.axios.get("/api/budget/get/"+this.budget_year+"/"+this.budget_month).then((response) => {
                    var old = response.data.items;
                    var targ = this.client_to_server(this.budget);
                    Object.keys(old).forEach((cat) => {
                        Object.keys(old[cat]).forEach((subcat) => {
                            if(!(cat in targ) || !(subcat in targ[cat]) ||
                                    targ[cat][subcat].max != old[cat][subcat].max) {
                                this.axios.get("/api/budget/get/"+this.budget_year+"/"+this.budget_month+"/"+cat+"/"+subcat);
                            }
                        });
                    });
                    Object.keys(targ).forEach((cat) => {
                        Object.keys(targ[cat]).forEach((subcat) => {
                            if(!(cat in old) || !(subcat in old[cat]) ||
                                    targ[cat][subcat].max != old[cat][subcat].max) {
                                this.axios.post("/api/budget/add", {
                                    year: this.budget_year,
                                    month: this.budget_month,
                                    category: cat,
                                    sub_category: subcat,
                                    max: targ[cat][subcat].max
                                });
                            }
                        });
                    });
                });
                console.log(this.budget_income);
            },
            server_to_client(obj) {
                var out = [];
                Object.keys(obj).sort().forEach((key) => {
                    var lst = [];
                    Object.keys(obj[key]).sort().forEach((subkey) => {
                        lst.push({
                            name: subkey,
                            amount: obj[key][subkey].max,
                            used: 0,
                            edit: false
                        });
                    });
                    out.push({
                        name: key,
                        edit: false,
                        used: 0,
                        items: lst
                    });
                });
                return out;
            },
            client_to_server(lst) {
                var out = {};
                lst.forEach((cat) => {
                    var obj = {};
                    cat.items.forEach((item) => {
                        obj[item.name] = {
                            max: item.amount
                        };
                    });
                    out[cat.name] = obj;
                });
                return out;
            },
            update_budget () {
                this.axios.get("/api/transaction/get/all").then((response) => {
                    var transactions = response.data;
                    this.axios.get("/api/budget/get/"+this.budget_year+"/"+this.budget_month).then((response) => {
                        this.budget = this.server_to_client(response.data.items);
                        this.budget_income = response.data.income;
                        this.budget_exists = true;
                        
                        transactions.forEach((transaction) => {
                            var dt = transaction.date.split("-");
                            var cnam = transaction.budget_item[0];
                            var scnam = transaction.budget_item[1];
                            if(this.budget_month+1 == dt[1] && this.budget_year == dt[0]) {
                                this.budget.forEach((cat) => {
                                    if(cat.name == cnam){
                                        cat.used += transaction.amount;
                                        cat.items.forEach((item) => {
                                            console.log(item);
                                            if(item.name== scnam) {
                                                item.used += transaction.amount;
                                            }
                                        });
                                    }
                                });
                            }
                        });
                    }, (error) => {
                        this.budget_exists = false;
                        console.log(error);
                    });
                });
            },
            setedit (cat, subcat) {
                if(this.edit_data.cat) {
                    if(this.edit_data.prev_key){
                        delete this.structure[this.edit_data.cat][this.edit_data.prev_key];
                    }
                    if(this.edit_data.key) {
                        this.structure[this.edit_data.cat][this.edit_data.key] = {
                            type: this.edit_data.type,
                            max: this.edit_data.max
                        };
                    }
                }
                this.edit_data.cat = cat;
                this.edit_data.prev_key = subcat;
                this.edit_data.key = subcat;
                if(subcat) {
                    this.edit_data.type = this.structure[cat][subcat].type;
                    this.edit_data.max = this.structure[cat][subcat].max;
                } else {
                    this.edit_data.type = "monthly";
                    this.edit_data.max = 100;
                }
            },
            isedit (cat, subcat) {
                return this.edit_data.cat == cat && this.edit_data.prev_key == subcat;
            },
            hasnewsub (cat) {
                return this.edit_data.cat == cat && !this.edit_data.prev_key;
            },
            addsub (cat) {
                this.setedit (cat, null);
                this.edit_data.key = "new subcategory";
            },
            do_shunt (name) {
                if(this.edit) {
                    this.un_shunt(this.edit);
                }
                this.edit = name;
                var lst = [];
                var str = this.structure;
                Object.keys(this.structure[name]).sort().forEach(function(key){
                    lst.push({
                        key: key,
                        type: str[name][key].type,
                        max: str[name][key].max
                    });
                });
                this.shunt.name = name;
                this.shunt.rows = lst;
            },
            un_shunt (name) {
                var vals = {};
                this.shunt.rows.forEach(function(row){
                    vals[row.key] = {
                        type: row.type,
                        max: row.max
                    }
                });
                this.structure[this.edit] = {};
                delete this.structure[this.edit];
                this.structure[this.shunt.name] = vals;
                this.edit = null;
            },
            remove (idx) {
                this.shunt.rows.splice(idx, 1);
            },
            add () {
                this.shunt.rows.push({ key: "new subcategory", max: 100, type: "monthly" });
            },
            addcat () {
                this.structure[1] = {};
                this.do_shunt(1);
                this.shunt.name = "new category";
            },
            jumpmonths (n) {
                this.budget_month += n;
                while(this.budget_month >= 12) {
                    this.budget_year += 1;
                    this.budget_month -= 12;
                }
                while(this.budget_month < 0) {
                    this.budget_year -= 1;
                    this.budget_month += 12;
                }
            }
        }
    }
</script>

<style>
.form-inline {
    color: black;
}
h1 .glyphicon, h2 .glyphicon {
    color:gray;
}
.gridbox {
    color: #000;
    display: inline-block;
    margin: 10px;

	border: 1px solid #ccc;
	padding:10px;
	border-radius:10px;

    font-size: 14pt;
}

.gridbox button {
    float:left;
}

.edit-button {
    font-size:13px;
}

.unbutton {
    appearance: none;
    -webkit-appearance: none;
    -moz-appearance: none;
    outline: none;
    border: 0;
    background: transparent;
}
</style>

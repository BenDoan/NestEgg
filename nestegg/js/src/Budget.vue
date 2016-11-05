<template>
    <div id="app">
        <h1>Budget</h1>
        <button class="btn btn-primary" v-on:click="addcat()"><span class="glyphicon gliphicon-add" aria-hidden="true"></span>Add category</button>
        <div v-for="nam in Object.keys(structure).sort()">
            <template v-if="edit == nam">
                <div class="input-group">
                <span class="input-group-btn"><button class="btn btn-secondary" v-on:click="un_shunt(nam)"><span class="glyphicon glyphicon-ok" aria-hidden="true"></span></button></span><input type="text" class="form-control" v-model="shunt.name"></input>
                </div>
                    <div class="form-inline" v-for="(row, i) in shunt.rows">
                            <div class="input-group">
                                <span class="input-group-btn"><button class="btn btn-secondary" v-on:click="remove(i)"><span class="glyphicon glyphicon-remove" aria-hidden="true"></span></button></span>
                                <input type="text" class="form-control" v-model="row.key"></input>
                            </div>
                            <input type="text" class="form-control" v-model="row.type"></input>
                            <input type="numeric" class="form-control" v-model="row.max"></input>
                    </div>
                    <button class="btn btn-secondary" v-on:click="add()"><span class="glyphicon glyphicon-plus" aria-hidden="true"></span></button>
            </template>
            <template v-if="edit != nam">
                <h2><button v-on:click="do_shunt(nam)" class="btn btn-primary"><span class="glyphicon glyphicon-edit" aria-hidden="true"></span></button> {{nam}}</h2>
                <table class="table table-hover">
                    <tbody>
                        <template v-for="subnam in Object.keys(structure[nam]).sort()">
                            <tr>
                                <td>{{ subnam }}</td>
                                <td>{{ structure[nam][subnam].type }}</td>
                                <td>${{structure[nam][subnam].max}}</td>
                            </tr>
                        </template>
                    </tbody>
                </table>
            </template>
        </div>
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
                structure: {
                    utilities: {
                        gas: {
                            "max": 30,
                            "type": "monthly"
                        },
                        electricity: {
                            max: 100,
                            type: "monthly"
                        },
                        rent: {
                            max: 700,
                            type: "monthly"
                        }
                    }
                }
            };
        },
        methods: {
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
            }
        }
    }
    </script>

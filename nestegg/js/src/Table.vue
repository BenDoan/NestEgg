<template>
    <div id="app">
        <h1>{{ title }}</h1>
        <table>
            <tr><th></th><th v-for="(type, key) in keys">{{ key }}</th></tr>
            <tr v-for="(row, i) in rows">
                <td><button v-on:click="edit = i==edit ? null : i">{{ edit == i ? "done" : "edit" }}</button></td>
                <td v-if="i != edit" v-for="(type, key) in keys">{{ row[key] }}</td>
                <td v-if="i == edit" v-for="(type, key) in keys">
                    <input type="text" v-if="type=='text'" v-model="row[key]"></input>
                    <input type="month" v-if="type=='month'" v-model="row[key]"></input>
                    <input type="date" v-if="type=='date'" v-model="row[key]"></input>
                    <input type="number" step="0.01" v-if="type=='money'" v-model="row[key]"></input>
                </td>
            </tr>
        </table>
        <button v-on:click="rows.push({}); edit=rows.length-1;">Add row</button>
    </div>
</template>

<script>
export default {
    name: 'table',
    props: ["keys", "rows", "notify"],
    data () {
        return {
            title: "HELLO WORLD",
//            keys: {"a":"text", "b":"month", "day":"day"},
//            rows: [],
            edit: null
        }
    },
    watch: {
        edit: function () {
            console.log("edit has changed");
            if(this.notify){
                this.notify();
            }
        }
    }
}
</script>

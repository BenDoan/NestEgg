import Vue from 'vue'
import VueResource from 'vue-resource'
import VueRouter from 'vue-router'
//import App from './App.vue'
import Table from './Table.vue'
import Home from './Home.vue'
import Budget from './Budget.vue'
import Transactions from './Transactions.vue'

Vue.use(VueResource);
Vue.use(VueRouter);

const router = new VueRouter({
    mode: "hash",
    base: __dirname,
    routes: [
        { path:"/", component: Home },
        { path:"/budget", component: Budget },
        { path:"/transactions", component: Transactions }
    ]
});

new Vue({
  el: '#app',
    router,
    components: {
        'edi-table': Table
    },
    data: {
        keys: {
            "date": "date",
            "amount": "money",
            "desc": "text"
        },
        rows: []
    },
    methods: {
        save: function () {
            console.log("saving...");
            this.$http.get("/").then((response) => {
                console.log(response);
            });
        }
    },
 // render: h => h(Table)
})

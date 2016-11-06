import Vue from 'vue'
import VueRouter from 'vue-router'
import axios from 'axios'
import VueAxios from 'vue-axios'

//import App from './App.vue'
import Table from './Table.vue'
import Home from './Home.vue'
import Budget from './Budget.vue'
import Bucket from './Bucket.vue'
import Transactions from './Transactions.vue'

import global from './global'

Vue.use(VueRouter);
Vue.use(VueAxios, axios)

const router = new VueRouter({
    mode: "hash",
    base: __dirname,
    routes: [
        { path:"/", component: Home },
        { path:"/budget", component: Budget },
        { path:"/bucket", component: Bucket },
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
        rows: [],
        global: global
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

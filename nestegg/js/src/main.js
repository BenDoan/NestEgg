import Vue from 'vue'
import VueResource from 'vue-resource'
import VueRouter from 'vue-router'
//import App from './App.vue'
import Table from './Table.vue'

Vue.use(VueResource);
Vue.use(VueRouter);

const Home = { template: '<div><router-link to="/test">asdf</router-link></div>' };
const Test = { template: '<div><router-link to="/">fdsa</router-link></div>' };

const router = new VueRouter({
    mode: "hash",
    base: __dirname,
    routes: [
        { path:"/", component: Home },
        { path:"/test", component: Test }
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

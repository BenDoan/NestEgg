const webpack = require('webpack')
const path = require('path')

module.exports = {
    devtool: 'inline-source-map',
    entry: "./main/main.js",
    output: {
        path: path.join(__dirname, '__build__'),
        filename: "[name].js",
        chunkFilename: '[id].chunk.js',
        publicPath: '/__build__/'
    },
    module: {
        loaders: [
            { test: /\.js$/, exclude: /node_modules/, loader: 'babel' },
            { test: /\.vue$/, loader: 'vue' }
        ]
    },
    node: {
        __dirname: true
    },
    context: __dirname,
    plugins: [
        new webpack.optimize.CommonsChunkPlugin('shared.js'),
        new webpack.DefinePlugin({
            'process.env.NODE_ENV': JSON.stringify(process.env.NODE_ENV || 'development')
        })
    ],
    resolve: {
        alias: {
            'vue': 'vue/dist/vue.js',
        }
    },
};

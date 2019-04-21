var redis = require('redis');
var createAccount = require('./create_account.js')
var createProject = require('./create_project.js')
var getContractAd = require('./get_contract_ad.js')
var zerorpc = require("zerorpc");
var sub = redis.createClient();
var server = new zerorpc.Server({
	keypair: function(reply){
		let keypair = createAccount.CreateAccount();
		keypair.then(result=>{
			console.log(result);
			reply(null, result.address +  result.pbkey + result.prkey);	
		});
	},
	createproject: function(user, coins, prkey, reply){
		let hash = createProject.CreateProject(user, coins, prkey);
		hash.then(result=>{
			console.log(result);
			reply(null, result);
		});
	},
    getcontractad: function(hash, reply){
    	let address = getContractAd.getContractAd(hash);
    	address.then(result=>{
			console.log(result);
			reply(null, result);
		});

    },
    createproject: function(user, coins, prkey, reply){
		let hash = createProject.CreateProject(user, coins, prkey);
		hash.then(result=>{
			console.log(result);
			reply(null, result);
		});
	},
	hello: function(hash, reply){
       reply("hello");
    },


});
server.bind("tcp://127.0.0.1:4343")


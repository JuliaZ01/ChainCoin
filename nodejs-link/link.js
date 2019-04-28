var redis = require('redis');
var createAccount = require('./create_account.js')
var createProject = require('./create_project.js')
var getContractAd = require('./get_contract_ad.js')
var settleWeight = require('./settle_weight.js')
var investContract = require('./invest_contract.js')
var settleContract = require('./settle_contract.js')
var addVolunteer = require('./add_volunteer.js')
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
	settleweight: function(ad, pr,reply){
		let info = settleWeight.settleWeight(ad,pr);
		info.then(result=>{
			console.log(result);
			reply(null, result.result.hash);
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
	investproject: function(user, pr, cad, coin, reply){
		let hash = investContract.investContract(user, pr, cad, coin);
		hash.then(result=>{
			console.log(result);
			reply(null, result.result.hash);
		});
	},
	settleContract: function(cad, reply){
		let hash = settleContract.settleContract(cad);
		hash.then(result=>{
			console.log(result);
			reply(null, result);
		});
	},
	addVolunteer: function(ad, pr, name, key, reply){
		let hash = addVolunteer.settlemetadata(ad, pr, name, key);
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


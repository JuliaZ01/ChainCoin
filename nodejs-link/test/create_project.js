const BumoSDK = require('bumo-sdk');
const encryption = require('bumo-encryption');
const BigNumber = require('bignumber.js');

const options = {
  host: '127.0.0.1:36002',
};
const sdk = new BumoSDK(options);
const genesisaddress = 'buQf5VAcYgWhJTp9Fywpu7W9KWfnUTK55MHt'
const genesispk = 'privbyrGtc3YaTLf4iWPU68Dwx83j8jjLvsoqAS3zbjVX5BcDvP7uYhE'
const CreateProject = async function(){
//获取Nonce
	const nonceInfo = await sdk.account.getNonce(genesisaddress)
	if(nonceInfo.errorCode != 0){
		console.log(nonceInfo);
		return;
	}
	let nonce = nonceInfo.result.nonce;
	nonce = new BigNumber(nonce).plus(1).toString(10);
//构建操作
   const operationInfo = await sdk.operation.contractCreateOperation({
   	   initBalance: '10000000',
   	   payload : "'use strict';function init(){storageStore('init','Initialized successful.I can r and write');return;}function main(input_str){let input_obj=JSON.parse(input_str);log('The sender:('+sender+') calls the function ('+input_obj.method+').');if(input_obj.method==='hello'){storageStore('main','called hello successful, I can read and write');}return;}function query(input_str){let input_obj=JSON.parse(input_str);if(input_obj.method==='hello'){return'Query and read only.Block hash:'+getBlockHash(0);}}",
   });
   if(operationInfo.errorCode != 0){
    	console.log(operationInfo);
    	return;
    }
    const operation = operationInfo.result.operation;
 //序列化交易
   const buildInfo = await sdk.transaction.buildBlob({
   	   sourceAddress : genesisaddress,
   	   gasPrice : '1000',
   	   feeLimit : '1004723000',
   	   nonce : nonce,
   	   operations : [ operation ],
   });
   if(buildInfo.errorCode !=0){
   	    console.log(buildInfo);
   	    return;
   }
   const blob = buildInfo.result.transactionBlob;
//用私钥进行签名
    const signatureInfo = sdk.transaction.sign({
    privateKeys : [ genesispk ],
    blob : blob,
  });
   if (signatureInfo.errorCode != 0){
   	console.log(signatureInfo);
   	return;
   }
   let signature = signatureInfo.result.signatures; 
//广播
   const submitInfo = await sdk.transaction.submit({
   	blob,
   	signature,
   });
   return submitInfo;
};



CreateProject().then(result =>{
  console.log(result);
  return result;
})
.catch(err =>{
  console.log(err);
});

module.exports.CreateProject = CreateProject;
const BumoSDK = require('bumo-sdk');
const encryption = require('bumo-encryption');
const BigNumber = require('bignumber.js');

const options = {
  host: '127.0.0.1:36002',
};
const sdk = new BumoSDK(options);
// const user = 'buQYhiGqsUawbz47FW3vtN5zKtMYcgMZcCDn';
// const prkey = 'privbwj3dpQfkCdCq539prht19JPLpGHs9Er4gK1b5QqTJAaz7X1Jdqy';
// const coins = 4;
const CreateProject = async function(user, coins, prkey){
//获取Nonce
	const nonceInfo = await sdk.account.getNonce(user)
	if(nonceInfo.errorCode != 0){
		console.log(nonceInfo);
		return;
	}
	let nonce = nonceInfo.result.nonce;
	nonce = new BigNumber(nonce).plus(1).toString(10);
//构建操作
   const params = {
       user : user,
       coins: coins,
   }
   const initInput = {
        params : params,
   }
   const operationInfo = await sdk.operation.contractCreateOperation({
       initInput: JSON.stringify(initInput),
   	   initBalance: '10000000',
       payload: "'use strict';let globalAttribute={};const globalAttributeKey='global_attribute';let helperList={};const helperListKey='helper_list';function transfer(to,value){assert(addressCheck(to)===true,'Arg-to is not a valid address.');assert(stoI64Check(value)===true,'Arg-value must be alphanumeric.');assert(int64Compare(value,'0')>0,'Arg-value must be greater than 0.');let sender=JSON.parse(storageLoad(globalAttributeKey)).user;let senderValue=storageLoad(JSON.parse(storageLoad(globalAttributeKey)).user);assert(senderValue!==false,'Failed to get the balance of '+sender+' from metadata.');assert(int64Compare(senderValue,value)>=0,'more than goal');let toValue=storageLoad(to);if(toValue===false){helperList=JSON.parse(storageLoad(helperListKey));helperList.result.push(to);storageStore(helperListKey,JSON.stringify(helperList));}toValue=(toValue===false)?value:int64Add(toValue,value);storageStore(to,toValue);senderValue=int64Sub(senderValue,value);storageStore(sender,senderValue);return true;}function settle(){globalAttribute=JSON.parse(storageLoad(globalAttributeKey));if(int64Compare(storageLoad(globalAttribute.user),'0')===0){let amount=globalAttribute.goal*100000000;Chain.payCoin(globalAttribute.user,amount.toString());globalAttribute.now=false;storageStore(globalAttributeKey,JSON.stringify(globalAttribute));return true;}else{helperList=JSON.parse(storageLoad(helperListKey));let i=0;while(helperList.result.length!==0){let value=parseInt(storageLoad(helperList.result[i]))*100000000;Chain.payCoin(helperList.result[i],value.toString());storageDel(helperList.result[i]);helperList.result.shift();}globalAttribute.now=false;storageStore(globalAttributeKey,JSON.stringify(globalAttribute));storageLoad(helperListKey,JSON.stringify(helperList));return true;}}function init(input_str){let params=JSON.parse(input_str).params;assert(addressCheck(params.user)===true&&params.coins>0,'Failed to check args');globalAttribute.user=params.user;globalAttribute.coins=params.coins;globalAttribute.now=true;globalAttribute.goal=params.coins;helperList.result=[];storageStore(helperListKey,JSON.stringify(helperList));storageStore(globalAttributeKey,JSON.stringify(globalAttribute));storageStore(sender,globalAttribute.coins.toString());}function main(input_str){let input=JSON.parse(input_str);if(input.method==='transfer'){transfer(input.params.to,input.params.value);}else if(input.method==='settle'){settle();}else{throw'<Main interface passes an invalid operation type>';}}function query(input_str){let result={};let input=JSON.parse(input_str);if(input.method==='GetInfo'){globalAttribute=JSON.parse(storageLoad(globalAttributeKey));result.ProInfo=globalAttribute;}else{throw'<Query interface passes an invalid operation type>';}return JSON.stringify(result);}",
     });
   if(operationInfo.errorCode != 0){
    	console.log(operationInfo);
    	return;
    }
    const operation = operationInfo.result.operation;
 //序列化交易
   const buildInfo = await sdk.transaction.buildBlob({
   	   sourceAddress : user,
   	   gasPrice : '1000',
   	   feeLimit : '2001030000',
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
    privateKeys : [ prkey ],
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
    return submitInfo.result.hash;
};

// CreateProject(user,coins,prkey).then(result =>{
//   console.log(result);
//   return result;
// })
// .catch(err =>{
//   console.log(err);
// });

module.exports.CreateProject = CreateProject;
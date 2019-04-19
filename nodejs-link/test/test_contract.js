const BumoSDK = require('bumo-sdk');
const encryption = require('bumo-encryption');
const BigNumber = require('bignumber.js');
const options = {
  host: '127.0.0.1:36002',
};
const sdk = new BumoSDK(options);

const hash = '2b1af217a4540f0441bc01118b4c14925dc0c10d9b613317acbd384a6a5b1fa2';
const caddress = 'buQjPgvddwvtpFYf76hZHW6kWk1xaMvSG6UB';
const testaddress = 'buQosfewhBYa5xxY4vLQSEZiLoNnXeiXkT1y';
const gaddress = 'buQf5VAcYgWhJTp9Fywpu7W9KWfnUTK55MHt';

const TestProject = async function(){
    const getInfo = await sdk.contract.getAddress(hash);
    if(getInfo.errorCode !=0){
    	console(errorCode);
    	return;
        }
    return getInfo.result.contractAddressList[0].contract_address;
    const input = {
      method: 'settle',
    };
    const testInfo = sdk.contract.call({
      sourceAddress: gaddress,
    	contractAddress: caddress,
    	optType :1,
    	feeLimit : '100000000000',
    	gasPrice : '1000',
      input: JSON.stringify(input),
    });
    return testInfo;
};

TestProject().then(result =>{
  console.log(result);
  console.log(result.result.txs[0].transaction_env.transaction.operations);
  console.log(result.result.txs[1].transaction_env.transaction.operations);
  console.log(result.result.txs[2].transaction_env.transaction.operations);
  console.log(result.result.txs[3].transaction_env.transaction.operations);
  return result;
})
.catch(err =>{
  console.log(err);
});
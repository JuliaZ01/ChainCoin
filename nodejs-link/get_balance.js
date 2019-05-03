const BumoSDK = require('bumo-sdk');
const encryption = require('bumo-encryption');
const BigNumber = require('bignumber.js');
const options = {
  host: '127.0.0.1:36002',
};
const sdk = new BumoSDK(options);
const getABalance = async function(ad){
    const getInfo = await sdk.account.getBalance(ad);
    if(getInfo.errorCode !=0){
        console(errorCode);
        return;
        }
    return getInfo.result.balance;
 };   
// getABalance('buQYhiGqsUawbz47FW3vtN5zKtMYcgMZcCDn').then(result =>{
//   console.log(result);
//   return result;
// })
// .catch(err =>{
//   console.log(err);
// });
module.exports.getABalance = getABalance;
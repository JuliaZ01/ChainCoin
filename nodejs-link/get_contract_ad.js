const BumoSDK = require('bumo-sdk');
const encryption = require('bumo-encryption');
const BigNumber = require('bignumber.js');
const options = {
  host: '127.0.0.1:36002',
};
const sdk = new BumoSDK(options);
const getContractAd = async function(hash){
    const getInfo = await sdk.contract.getAddress(hash);
    if(getInfo.errorCode !=0){
        console(errorCode);
        return;
        }
    return getInfo.result.contractAddressList;
};
// getContractAd('cb55e4f35012845ed6da1468bdecb4b0374f0cf74289b61c2eed8b0b25078603').then(result =>{
//   console.log(result);
//   return result;
// })
// .catch(err =>{
//   console.log(err);
// });
module.exports.getContractAd = getContractAd;
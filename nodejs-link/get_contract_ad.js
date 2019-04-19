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
module.exports.getContractAd = getContractAd;
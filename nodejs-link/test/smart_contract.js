'use strict';
function init(){
    storageStore('init','Initialized successful.I can r and write');
    return;
}
function main(input_str){
    let input_obj = JSON.parse(input_str);
    log('The sender:(' +sender+ ') calls the function (' +input_obj. method+ ').');
    if(input_obj . method === 'hello'){
    	storageStore('main','called hello successful, I can read and write');
    }
    return;
}
function query(input_str){
    let input_obj = JSON.parse(input_str);
    if(input_obj.method === 'hello'){
    	return 'Query and read only.Block hash:'  + getBlockHash(0);
    }
}

    // let params = JSON.parse(input_str);
    // let globalAttribute = {};
    // let globalAttributeKey = 'global_attribute';
    // assert(addressCheck(params.destaddress) === true && params.targetcoins > 0 &&
    //        typeof params.time === 'string' && params.nowcoins === 0 &&
    //        params.now === true,'Failed to check args');
    // globalAttribute.destaddress = params.destaddress;
    // globalAttribute.targetcoins = params.targetcoins;
    // globalAttribute.time = params.time;
    // globalAttribute.nowcoins = 0;
    // globalAttribute.now = true;
    // storageStore(globalAttributeKey, JSON.stringify(globalAttribute));
    // return;
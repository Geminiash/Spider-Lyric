const cryptoJS = require('crypto-js')

const key = cryptoJS.enc.Utf8.parse('suiyu'.padEnd(16, '0'))
const iv = cryptoJS.enc.Utf8.parse('suiyu'.padEnd(16, '0'))

// 加密
function cryptoData(data){
    const encry = cryptoJS.AES.encrypt(data,key,{
        iv:iv,
        mode : cryptoJS.mode.CBC,
        padding:cryptoJS.pad.Pkcs7
    })
    return encry.toString()
}

// 解密
function Datatocryp(data){
    const decry = cryptoJS.AES.decrypt(data,key,{
        iv:iv,
        mode:cryptoJS.mode.CBC,
        padding:cryptoJS.pad.Pkcs7
    })
    return decry.toString(cryptoJS.enc.Utf8)
}

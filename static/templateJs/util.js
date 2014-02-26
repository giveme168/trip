function isIP(value){
  var reg_ip = new RegExp('^[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}$');
  if ( ! reg_ip.exec(value) ) {
      return false; 
  }
  var strs = value.split(".");
  if( strs.length != 4) {
    return false; 
  }
  for (var i=0;i<strs.length ;i++ ) {
    if (strs[i].indexOf("0") == 0 && strs[i].length > 1) {
      return false;
    }
    else if (parseInt(strs[i])>255 || parseInt(strs[i])<0) {
      return false;
    }
  }
    /*if (value.search(/^192\.168\./) != -1 || value.search(/^172/) != -1 || value.search(/^127\.0/) != -1 ) {
        return false;
    }*/
  return true; 
};
function trim(str){
  return str.replace(/(^\s*)|(\s*$)/g, "");
};
function isNumber(obj){
  var isNumFlag = true;
  var ex = /^\d+$/;
  if (!ex.test(obj)) {
     isNumFlag = false;
  } 
  return isNumFlag;
  
}

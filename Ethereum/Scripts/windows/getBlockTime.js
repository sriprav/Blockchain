var Web3 = require('web3');
var web3 = new Web3();
var http = require('http');
web3.setProvider(new web3.providers.HttpProvider('http://localhost:8545'));

var Workbook = require('xlsx-populate');
 
// Load the input workbook from file. 
var workbook = Workbook.fromFileSync("./sample.xlsx");
 
// Access the first worksheet
var sheet = workbook.getSheet(0);

function getBlockTime() {
lastBlock = web3.eth.blockNumber; //Getting the latest mined block in the blockchain
firstBlock = 1; //First block
block_time = 0;
	for (var i = firstBlock, rowNum = 1; i<=lastBlock; i++, rowNum++) 
    { 
    	block_time = web3.eth.getBlock(i).timestamp - web3.eth.getBlock(i-1).timestamp;
        //console.log(block_time);
        var row = sheet.getRow(rowNum);
        colNum = 1;
        var cell = row.getCell(colNum);
        cell.setValue(block_time);
        workbook.toFileSync("./sample.xlsx");
  	} 
// Write to file. 
//workbook.toFileSync("./sample.xlsx");
}

getBlockTime();

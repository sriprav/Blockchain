var Web3 = require('web3');
var web3 = new Web3();
var http = require('http');
web3.setProvider(new web3.providers.HttpProvider('http://localhost:8545'));

var Workbook = require('xlsx-populate');
 
// Load the input workbook from file. 
var workbook = Workbook.fromFileSync("./difficulty.xlsx");
 
// Access the first worksheet
var sheet = workbook.getSheet(0);

function difficulty() {
lastBlock = web3.eth.blockNumber; //Getting the latest mined block in the blockchain
firstBlock = 0; //First block
block_time = 0;
	for (var i = firstBlock, rowNum = 1; i<=lastBlock; i++, rowNum++) 
    { 
    	diff = parseInt(web3.eth.getBlock(i).difficulty);
        var row = sheet.getRow(rowNum);
        colNum = 1;
        var cell = row.getCell(colNum);
        cell.setValue(diff);
        workbook.toFileSync("./difficulty.xlsx");
  	} 
}

difficulty();



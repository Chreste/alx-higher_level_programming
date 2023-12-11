#!/usr/bin/node
const s = Math.floor(Number(process.argv[2]));
if (isNaN(s)){
	console.log('Missing size')
} else {
	for (let y = 0; y < s; y++ ){
		let row = '';
		for (let c = 0; c < s; c++) row += 'X';
		console.log(row)
	}
}

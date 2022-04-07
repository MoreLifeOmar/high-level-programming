#!/usr/bin/node

if (isNaN(process.argv[2])) {
	  console.log('Missing size');
} else {
	  const x = parseInt(process.argv[2]);
	  for (let i = 0; i < x; i++) {
		      for (let j = 0; j < x; j++) { process.stdout.write('X'); }
		      console.log();
		    }
}

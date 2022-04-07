#!/usr/bin/node
const fs = require('fs');
const fileA = process.argv[2];
const fileB = process.argv[3];
const fileC = process.argv[4];
const fA = fs.readFileSync(fileA, 'utf-8');
const fB = fs.readFileSync(fileB, 'utf-8');
fs.writeFileSync(fileC, fA + fB);

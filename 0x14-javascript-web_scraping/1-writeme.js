#!/usr/bin/node
let fs = require('fs');
let file = process.argv[2];
let content = process.argv[3];

function writeMe (file, content) {
  fs.writeFile(file, content, function (error) {
    if (error) {
      console.log(error);
    }
  });
}
writeMe(file, content);

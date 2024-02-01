#!/usr/bin/node
/*
 * script that computes the number of tasks completed by user id.
 * The first argument is the API URL: https://jsonplaceholder.typicode.com/todos
 * Only print users with completed task
 */
const req = require('request');
const url = process.argv[2];
req(url, (error, response, body) => {
  if (error) console.log(error);
  else {
    const data = {};
    const tasks = JSON.parse(body);
    for (const index in tasks) {
      if (tasks[index].completed === true) {
        if (tasks[index].userId in data) data[tasks[index].userId]++;
        else data[tasks[index].userId] = 1;
      }
    }
    console.log(data);
  }
});

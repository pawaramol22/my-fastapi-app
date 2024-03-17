/* global use, db */
// MongoDB Playground
// To disable this template go to Settings | MongoDB | Use Default Template For Playground.
// Make sure you are connected to enable completions and to be able to run a playground.
// Use Ctrl+Space inside a snippet or a string literal to trigger completions.
// The result of the last command run in a playground is shown on the results panel.
// By default the first 20 documents will be returned with a cursor.
// Use 'console.log()' to print to the debug output.
// For more documentation on playgrounds please refer to
// https://www.mongodb.com/docs/mongodb-vscode/playgrounds/

// Select the database to use.
use('myproducts');

// Insert a few documents into the sales collection.
db.getCollection('products').insertMany([
  { 'name': 'abc', 'price': 10, 'description': 'This is test' },
  { 'name': 'jkl', 'price': 20, 'description': 'This is test' },
  { 'name': 'xyz', 'price': 5, 'description': 'This is test' },
  { 'name': 'xyz', 'price': 5, 'description': 'This is test' },
  { 'name': 'abc', 'price': 10, 'description': 'This is test' },
]);

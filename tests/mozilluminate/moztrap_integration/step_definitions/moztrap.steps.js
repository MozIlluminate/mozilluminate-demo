'use strict';

module.exports = function (){
/*
this.When(/^I add (.*) to the list$/, function (itemName, callback) { // Write code here that turns the phrase above into concrete actions
  //callback.pending();
  //
  console.log(itemName)
  //callback.pending();
  callback();
});

this.Then(/^The grocery list contains (.*)$/, function (itemName, callback) {
  // Write code here that turns the phrase above into concrete actions
  //callback.pending();
  //
});
*/
this.When(/^(.*)$/, function (text, callback) {
  // Write code here that turns the phrase above into concrete actions
  console.log("WHEN " + text)
  callback();
});

this.Then(/^(.*)$/, function (text, callback, keyword) {
  // Write code here that turns the phrase above into concrete actions
  console.log(keyword.toUpperCase() + " " + text)
  callback();
});

this.Before(function(scenario, callback){
  console.log("TEST THAT " + scenario.getName())
  console.log(scenario.getDescription())
  //console.log("\n=====\n")
  callback();
})
this.After(function(scenario, callback){
  console.log("\n=====\n")
  callback();
})
/*
this.When(/^(.*)$/, function (text, callback) {
  // Write code here that turns the phrase above into concrete actions
  console.log(text)
  //callback.pending();
  callback();
});
*/


};

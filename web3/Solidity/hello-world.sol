// Here's a code snippet in Solidity to print "Hello, World!" on the console:


// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

contract HelloWorld {
    function sayHello() public pure returns (string memory) {
        return "Hello, World!";
    }
}


// In this Solidity code snippet, we define a contract called `HelloWorld` that contains a function `sayHello`.
// The `sayHello` function is declared as `public` and `pure`, which means it can be called externally and does not modify the contract's state.

// Inside the `sayHello` function, we simply return the string `"Hello, World!"`. This value will be returned when the function is called.

// To execute and see the result of this contract, you would need to deploy it on a blockchain network like Ethereum.
// After deployment, you can call the `sayHello` function and retrieve the returned string value, which will be "Hello, World!".

// Solidity is primarily used for creating smart contracts that run on blockchain networks,
//  and printing output to the console is not a typical use case within smart contracts.
//  However, this simple example demonstrates the concept of returning a string from a Solidity function.
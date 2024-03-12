#!/usr/bin/node
// check for Rectangle parameters

modules.exports = class Rectangle {
    constructor (width,height) {
        if (typeof width === 'number' && typeof height === 'number' && width > 0 && height > 0) {
            this.width = width;
            this.height = height;}
    }
};
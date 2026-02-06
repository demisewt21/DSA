Array.prototype.last = function() {
  // 'this' refers to the current array
  if (this.length === 0) {
    return -1;
  }
  return this[this.length - 1];
};

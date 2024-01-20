/**
 * @param {Promise} promise1
 * @param {Promise} promise2
 * @return {Promise}
 */
var addTwoPromises = async function(promise1, promise2) {
  // Use Promise.all to wait for both promises to resolve
  const [result1, result2] = await Promise.all([promise1, promise2]);
  
  // Return a new promise with the sum of the resolved values
  return result1 + result2;
};

// Example usage:
addTwoPromises(Promise.resolve(2), Promise.resolve(2))
  .then(console.log); // Output: 4

export default function appendToEachArrayValue(array, appendString) {
  /* eslint-disable no-param-reassign */
  for (const [idx, value] of array.entries()) {
    array[idx] = appendString + value;
  }

  return array;
}

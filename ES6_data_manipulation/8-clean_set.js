function cleanSet(set, startString) {
  // Check if startString is a string and not empty
  if (typeof startString !== 'string' || startString === '') {
    return '';
  }

  const result = [];
  for (const item of set) {
    // Check if item is a string before calling startsWith
    if (typeof item === 'string' && item.startsWith(startString)) {
      // Only add the rest of the string if it's not empty
      const restOfString = item.slice(startString.length);
      if (restOfString !== '') {
        result.push(restOfString);
      }
    }
  }

  return result.join('-');
}

export default cleanSet;

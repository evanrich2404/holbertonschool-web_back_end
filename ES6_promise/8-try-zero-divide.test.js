import divideFunction from './8-try';

test("divideFunction throw an error", () => {
  expect(() => {
    divideFunction(10, 0);
  }).toThrowError('cannot divide by 0');
});

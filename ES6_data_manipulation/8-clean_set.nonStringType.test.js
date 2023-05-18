import cleanSet from "./8-clean_set.js";

test("returns an empty string when a non string type is passed in", () => {
  const set = new Set(['id-test', 'id-chicken', 'id-user', , 'id-id-']);
  expect(cleanSet(set, [])).toBe('');
});

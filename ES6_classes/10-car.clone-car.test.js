import Car from "./10-car.js";

class TestCar extends Car {}

test("Car cloneCar check for species", () => {
  const opel = new TestCar();
  const newCar = opel.cloneCar();

  expect(newCar instanceof TestCar).toBe(true);
});

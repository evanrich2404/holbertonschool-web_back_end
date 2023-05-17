export default class Car {
  constructor(brand, motor, color) {
    this.brand = brand;
    this.motor = motor;
    this.color = color;
  }

  cloneCar() {
    return new Car(this._brand, this._motor, this._color);
  }
}

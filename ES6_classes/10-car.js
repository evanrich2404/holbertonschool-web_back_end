const _class = Symbol('class');

export default class Car {
  constructor(brand, motor, color) {
    this._brand = brand;
    this._motor = motor;
    this._color = color;
    this[_class] = this.constructor;
  }

  cloneCar() {
    return new this[_class]();
  }
}

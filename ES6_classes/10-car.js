export default class Car {
  constructor(brand, motor, color) {
    this._brand = brand;
    this._motor = motor;
    this._color = color;
  }
  
    // Symbol.species vasitəsilə obyektin hansı konstruktorla yaradılacağını müəyyən edirik
  static get [Symbol.species]() {
    return this;
  }
  
    // Cari obyektin sinfinə uygun yeni instansiya qaytarır
  cloneCar() {
    const Species = this.constructor[Symbol.species];
    return new Species();
  }
}

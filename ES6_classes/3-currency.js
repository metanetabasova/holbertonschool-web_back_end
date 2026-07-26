export default class Currency {
  constructor(code, name) {
    this.code = code;
    this.name = name;
  }
  
    // Code getter və setter
  get code() {
    return this._code;
  }
  
  set code(val) {
    if (typeof val !== 'string') {
      throw new TypeError('Code must be a string');
    }
    this._code = val;
  }
  
    // Name getter və setter
  get name() {
    return this._name;
  }
  
  set name(val) {
    if (typeof val !== 'string') {
      throw new TypeError('Name must be a string');
    }
    this._name = val;
  }
  
    // Tam valyuta məlumatını qaytaran metod
  displayFullCurrency() {
    return `${this._name} (${this._code})`;
  }
}

export default class Airport {
  constructor(name, code) {
    this._name = name;
    this._code = code;
  }
  
    // Symbol.toStringTag vasitəsilə obyekti string-ə çevirərkən görünən mətni dəyişirik
  get [Symbol.toStringTag]() {
    return this._code;
  }
}

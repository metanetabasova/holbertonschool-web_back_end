import Building from './5-building.js';

export default class SkyHighBuilding extends Building {
  constructor(sqft, floors) {
    super(sqft);
    this._floors = floors;
  }

  // Floors getter
  get floors() {
    return this._floors;
  }

  // evacuationWarningMessage metodunun təkrar təyin edilməsi (override)
  evacuationWarningMessage() {
    return `Evacuate slowly the ${this._floors} floors`;
  }
}

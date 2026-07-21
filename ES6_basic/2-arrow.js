export default function getNeighborhoodsList () {
  this.sanFranciscoNeighborhoods = ['SOMA', 'Unionn Square'];

  this.addNeighborhood = (newNeighborhood) => {
    this.sanFranciscoNeighborhoods.push(newNeighborhood);
    return this.sanFranciscoNeighborhoods;
  };
}

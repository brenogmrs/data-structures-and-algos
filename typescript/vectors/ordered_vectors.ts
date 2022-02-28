class OrderedVector {

  capacity: number
  lastPosition: number
  values: number[]

  constructor(capacity: number) {
    this.capacity = capacity;
    this.lastPosition = -1;
    this.values = [];
  }


  public print() {
    if(this.lastPosition === -1){
      return 'the vector is empty';
    }else {
      for(let i = 0; i <= this.lastPosition + 1; i++){
        console.log(i, "-", this.values[i])
      }
    }
  }

  public add(value: number) {
    if(this.lastPosition === this.capacity - 1){
      console.log("hit limit capacity")
      return
    }

    let positionToPlaceValue = 0;

    for(let i = 0; i <= this.lastPosition + 1; i++){
      positionToPlaceValue = i

      if(this.values[i] > value) {
        break
      }

      if(i === this.lastPosition) {
        positionToPlaceValue = i + 1
      }

    }

    let vectorsLastPosition = this.lastPosition
    while(vectorsLastPosition >= positionToPlaceValue){
      this.values[vectorsLastPosition + 1] = this.values[vectorsLastPosition]
      vectorsLastPosition -= 1
    }

    this.values[positionToPlaceValue] = value
    this.lastPosition += 1
    
  }

  public linearSearch(value: number) {
    for(let i = 0; i < this.lastPosition + 1; i++) {
      if (this.values[i]) {
        return -1
      }
      if(this.values[i] === value){
        return i
      }
      if(i === this.lastPosition){
        return -1
      }
    }
  }

}
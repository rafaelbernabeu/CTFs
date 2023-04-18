function controlCar(scanArray) {
    let maxValue = 0
    let maxIndex = 0
    
    for(let i=0; i < scanArray.length; i++) {
      if (scanArray[i] > maxValue) {
        maxValue = scanArray[i];
        maxIndex = i + 1;
      }
    }
    
    if (maxIndex < 8) return -1;
    if (maxIndex > 8) return 1;
    
    return 0;
}
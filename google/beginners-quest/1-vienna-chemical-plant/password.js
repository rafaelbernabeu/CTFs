function checkPassword() {
    let p = []

    p[0] = String.fromCharCode(52037 - 0xCafe);
    p[6] = String.fromCharCode(52081 - 0xCafe);
    p[5] = String.fromCharCode(52063 - 0xCafe);
    p[1] = String.fromCharCode(52077 - 0xCafe);
    p[9] = String.fromCharCode(52077 - 0xCafe);
    p[10] = String.fromCharCode(52080 - 0xCafe);
    p[4] = String.fromCharCode(52046 - 0xCafe);
    p[3] = String.fromCharCode(52066 - 0xCafe);
    p[8] = String.fromCharCode(52085 - 0xCafe);
    p[7] = String.fromCharCode(52081 - 0xCafe);
    p[2] = String.fromCharCode(52077 - 0xCafe);
    p[11] = String.fromCharCode(52066 - 0xCafe);
      
    console.log(p.join(""))
}
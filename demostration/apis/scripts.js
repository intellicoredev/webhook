def leer_reles():
    var
    sum = 0;
    if (payload.data.Boton1 == 1){
    sum=sum+1;
    }
    if (payload.data.Boton2 == 1){
    sum=sum+2
    }
    if (payload.data.Boton3 == 1){
    sum=sum+4;
    }
    if (payload.data.Boton4 == 1){
    sum=sum+8;
    }
    if (payload.data.Boton5 == 1){
    sum=sum+16;
    }
    if (payload.data.Boton6 == 1){
    sum=sum+32;
    }
    if (payload.data.Boton7 == 1){
    sum=sum+64;
    }
    if (payload.data.Boton8 == 1){
    sum=sum+128;
    }
    nvar
    sum2 = 0;
    if (payload.data.Boton9 == 1){
    sum2=sum2+1;
    }
    if (payload.data.Boton10 == 1){
    sum2=sum2+2;
    }
    if (payload.data.Boton11 == 1){
    sum2=sum2+4;
    }
    if (payload.data.Boton12 == 1){
    sum2=sum2+8;
    }
    payload.data.Cuenta1 = sum;
    payload.data.Cuenta2 = sum2;


def script2():
    var
    a = 0;
    var
    suma = 0;

    for (a=0;a < 4;a++){
    if (parseInt(payload.data.body.b2, 10) & (1 << a)){
    suma += (1 << a);
    }
    }


payload.data.relb2 = suma;


def script3():
    var
    a = 0;
    var
    relState = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0];
    var
    eneState = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0];

    for (a=0;a < 8;a++){
    if (parseInt(payload.data.body.b1, 10) & (1 << a)){
    relState[a]=1;
    } else {
    relState[a]=0;
    }
    }


for (a=0;a < 4;a++){
if (parseInt(payload.data.body.b2, 10) & (1 << a)){
relState[a+8]=1;
}
else {
relState[a+8]=0;
}
}

for (a=4;a < 8;a++){
if (parseInt(payload.data.body.b2, 10) & (1 << a)){
eneState[a-4]=1;
}
else {
eneState[a-4]=0;
}
}

for (a=0;a < 8;a++){
if (parseInt(payload.data.body.b3, 10) & (1 << a)){
eneState[a+4]=1;
}
else {
eneState[a+4]=0;
}
}
payload.data.relState = relState;
payload.data.eneState = eneState;


def script5():
    var
    a = 0;
    var
    plaState = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0];
    for (a=0;a < 8;a++){
    if (parseInt(payload.data.Platb1.value, 10) & (1 << a)){
    plaState[a]=1;
    }
    else {
    plaState[a]=0;
    }
    }
    for (a=0;a < 4;a++){
    if (parseInt(payload.data.Platb2.value, 10) & (1 << a)){
    plaState[a+8]=1;
    }
    else {
    plaState[a+8]=0;
    }
    }
    payload.data.plaState = plaState;


def script6():
    var
    a = 0;
    var
    chgNumber = 0;
    var
    chgArray = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0];
    var
    errorNumber = 0;
    var
    errorArray = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0];
    var
    outArray = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0];
    var
    suma = 0;

    for (a=0;a < 12;a++){
    if (payload.data.relState[a] != payload.data.plaState[a]){
    chgNumber++;
    chgArray[a]=1;
    if (payload.data.relState[a] == 0 & & payload.data.eneState[a] == 1){
    errorNumber++;
    errorArray[a]=1;
    }
    }
    }
    if (chgNumber == 0){
    // Out=0 If chgNumber == 0 Send Null
    payload.data.CambioPlataforma.value=0;
    payload.data.OutputValue=0;
    }
    else if (chgNumber > 0 & & errorNumber == 0){
    // Out=1 if chgNumber > 0 & & errorNumber == 0 send chg Normal
    payload.data.OutputValue=1;
    }
    else if (chgNumber > 0 & & errorNumber > 0){
    // Out=2 If chgNumber > 0 & & errorNumber > 0 & & CambioPlataforma == 1 make payloads change (Rel=Open & Ener=1) chg=0 & save ErrorNumber
    // Out=2 ** If chgNumber > 0 & & errorNumber > 0 & & CambioPlataforma == 0 & & ErrorNumber != SavedErrorNumber make payloads change & save ErrorNumber // Out=0 If chgNumber > 0 & & errorNumber > 0 & & CambioPlataforma == 0 & & ErrorNumber == SavedErrorNumber send NULL
    payload.data.CambioPlataforma.value = 0;
    if (payload.lastErrorNumber.value != errorNumber){
    payload.data.OutputValue=2;
    for (a=0;a < 12;a++){
    if (payload.data.relState[a] != payload.data.plaState[a]){
    if (payload.data.relState[a] == 0 & & payload.data.eneState[a] == 1){
    outArray[a]=0;
    }
    else {
    outArray[a]=payload.data.plaState[a];
    }
    }
    else {
    outArray[a]=payload.data.plaState[a];
    }
    }
    } else {
    payload.data.OutputValue=0;
    }
    }

    if (payload.data.OutputValue == 2){
    for (a=0;a < 8;a++){
    if (outArray[a] == 1){
    suma += (1 << a);
    }
    }
    payload.data.newOutb1=suma;
    suma=0;
    for (a=8;a < 12;a++){
    if (outArray[a] == 1){
    suma += (1 << (a-8));
    }
    }
    payload.data.newOutb2=suma;
    }

    payload.data.chgNumber = chgNumber;
    payload.data.chgArray = chgArray;
    payload.data.errorNumber = errorNumber;
    payload.data.errorArray = errorArray;
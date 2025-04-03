// var is set globally no new variable is created 
// let creates a new binding variable every time loop iterates 

// the function with the enclosing lexical scope is called closure 

for(var i  = 0; i < 3; i++){
    
    const log = () => {
        console.log(i);
    }

    log();
}
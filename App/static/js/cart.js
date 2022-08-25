function getCookie(name){
    //Split cookie string and get all individual name=value pairs in an array
    var cookieArr = document.cookie.split(",");
    console.log('ca: ', cookieArr);

    //Loop through the array elements
    for(var i = 0; i < cookieArr.length; i++){
        var cookiePair = cookieArr[i].split("=");
        console.log('cp: ', cookiePair);
        /* Removing whitespace at the beginning of the cookie name
        and compare it with the given string */
        if(name == cookiePair[0].trim()){
            //Decode the cookie value and return
            return decodeURIComponent(cookiePair[1]);
        }
    }

    // Return null if not found
    return {};
}

var cart = getCookie('cart')

if (cart == undefined ){
    cart = {}
    console.log('cart created!');
    document.cookie = 'cart=' + JSON.stringify(cart) + ";domain=;path=/"
}

function addCookieItem(bookId, action){  

    if (action == 'add'){
        if (cart[bookId] == undefined){
            console.log('undefined: ', cart[bookId]);
            cart[bookId] = {'quantity': 1}
        }else{
            cart[bookId]['quantity'] += 1
            console.log('defined: ', cart[bookId]);
        }
    }
    console.log('Cart: ', cart);

    if (action == 'remove'){
        cart[bookId]['quantity'] -= 1

        if (cart[bookId]['quantity'] <= 0){
            console.log('Item should be deleted');
            delete cart[bookId]
        }
    }

    document.cookie = 'cart=' + JSON.stringify(cart) + ";domain=;path=/"
    // location.reload()
}

let idProduct = document.getElementById('id_product_1');
let id = idProduct.textContent;

const btn = document.getElementById('input_1');

function postFormData(url, data){
    // we send the content of the form to the server.
    console.log(data)
    console.log(typeof data)
    return fetch(url, {
        method: "POST",
        body: data
    })
    .then(response => response.json())
    .catch(error => console.log(error));
}

btn.addEventListener('click', function(event) {
    event.preventDefault();
    postFormData('proposed_products/', id)
});

const agencias = {

    "Pichincha": [
        "Quito Norte",
        "Quito Sur",
        "Sangolquí",
        "Cayambe"
    ],

    "Guayas": [
        "Guayaquil Centro",
        "Durán",
        "Milagro"
    ]

};


const provinciaSelect =
    document.getElementById("provincia");

const agenciaSelect =
    document.getElementById("agencia");


provinciaSelect.addEventListener("change", function(){

    const provincia =
        this.value;

    agenciaSelect.innerHTML = "";

    const opcionInicial =
        document.createElement("option");

    opcionInicial.value = "";

    opcionInicial.textContent =
        "Seleccione una agencia";

    agenciaSelect.appendChild(opcionInicial);

    if(agencias[provincia]){

        agencias[provincia].forEach(function(agencia){

            const option =
                document.createElement("option");

            option.value = agencia;

            option.textContent = agencia;

            agenciaSelect.appendChild(option);

        });

    }

});



const tecnicos = {

    "Diego Lema": "1312316811",
    "Juan Perez": "9999999999"

};


const tecnicoSelect =
    document.getElementById("tecnico");

const cedulaInput =
    document.getElementById("cedula");


tecnicoSelect.addEventListener("change", function(){

    const tecnico =
        this.value;

    cedulaInput.value =
        tecnicos[tecnico] || "";

});

const botonAgregarSerie =
    document.getElementById("agregar-serie");

const contenedorSeries =
    document.getElementById("contenedor-series");


botonAgregarSerie.addEventListener("click", function(){

    const input =
        document.createElement("input");

    input.type = "text";

    input.name = "series[]";

    input.placeholder = "Ingrese serie";

    input.required = true;

    contenedorSeries.appendChild(input);

});
const agencias = {

    "Ibarra": [
        "Tulcan",
        "San Gabriel",
        "El Angel",
        "Mira",
        "Ibarra",
        "Atuntaqui",
        "Pimampiro",
        "Otavalo",
        "Cotacachi",
        "Lago Agrio",
        "Putumayo",
        "Lumbaqui",
        "Tarapoa",
        "Esmeraldas",
        "Atacames",
        "Limones",
        "San Lorenzo",
        "Muisne",
        "Quininde",
        "Shushufindi",
        "Puerto Pesquero Esmeraldas(Cac)"
    ],

    "Quito": [
        "Guayaquil Centro",
        "Durán",
        "Milagro"
    ],


     "Riobamba": [
        "Guayaquil Centro",
        "Durán",
        "Milagro"
    ],

     "Portoviejo": [
        "Guayaquil Centro",
        "Durán",
        "Milagro"
    ],

     "Guayaquil": [
        "Guayaquil Centro",
        "Durán",
        "Milagro"
    ],

     "Cuenca": [
        "Guayaquil Centro",
        "Durán",
        "Milagro"
    ],

     "Loja": [
        "Guayaquil Centro",
        "Durán",
        "Milagro"
    ]

};


const zonalSelect =
    document.getElementById("zonal");

const agenciaSelect =
    document.getElementById("agencia");


zonalSelect.addEventListener("change", function(){

    const zonal =
        this.value;

    agenciaSelect.innerHTML = "";

    const opcionInicial =
        document.createElement("option");

    opcionInicial.value = "";

    opcionInicial.textContent =
        "Seleccione una agencia";

    agenciaSelect.appendChild(opcionInicial);

    if(agencias[zonal]){

        agencias[zonal].forEach(function(agencia){

            const option =
                document.createElement("option");

            option.value = agencia;

            option.textContent = agencia;

            agenciaSelect.appendChild(option);

        });

    }

});



const tecnicos = {

    "Jorgue Quijije": "1317604039",
    "Luis Llivisaca": "1400825673",
    "Jefferson Reyes": "1311208068",
    "Jaime Gonzalez": "1104055346",
    "Daniel Yuquilema": "0919137315",
    "Cristian Tene": "1105041675",
    "Leonardo Quijije": "1312316811",
    "Jorge Morocho Jimenez": "0104922869",
    "Jesus Quijije": "1316415643",
    "Cristian Silva": "2000072831",
    "Jorge Morocho Buele": "1400854251",
    "Ronald Paute": "0106409402",
    "Jefferson Pillco": "2100725494",
    "Jean Cordova": "1313617753",
    "Victor Nieves": "0103174017",
    "Ricardo Moreira": "1722253992",

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
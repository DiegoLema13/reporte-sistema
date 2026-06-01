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
        "Quito",
        "Ventanilla ext.Chiriyacu 1(Quito)",
        "Sangolqui",
        "Baeza",
        "El Chaco oficina ext.Baeza",
        "Cayambe",
        "Machachi",
        "S.M de los Bancos",
        "Dayuma",
        "Loreto",
        "Joya de los Sachas",
        "El Tena",
        "Fco.de Orellana",
        "Plataforma Norte (Quito)"
    ],


     "Riobamba": [
        "Alausi",
        "Ambato",
        "Baños",
        "Cevallos",
        "Chunchi",
        "Cumanda",
        "El Corazon",
        "El Puyo",
        "Guano",
        "La Mana",
        "Latacunga",
        "Mcdo. Mayorista de Ambato",
        "Mcdo. Mayorista de Riobamba",
        "Pallatanga",
        "Pillaro",
        "Quero",
        "Riobamba",
        "Sigchos",
        "Zumbahua"
    ],

     "Portoviejo": [
        "Portoviejo",
        "Rocafuerte",
        "Pichincha",
        "Manta",
        "Montecristi",
        "Jipijapa",
        "Pajan",
        "Chone",
        "Flavio Alfaro",
        "Bahia",
        "Calceta",
        "Pedernales",
        "El Carmen",
        "Santo Domingo",
        "La Concordia",
        "Jaramijo",
        "Nuevo Tarqui Manta"
    ],

     "Guayaquil": [
        "Guayaquil",
        "Playas",
        "Duran",
        "Chongon",
        "Tarqui",
        "Guasmo",
        "Atarazana",
        "Salitre",
        "Samborondon",
        "Pedro Carbo",
        "Daule",
        "Palestina",
        "Santa Lucia",
        "Balzar",
        "Colimes",
        "Santa Elena",
        "Salinas",
        "Pto.Baquerizo Moreno",
        "Pto.Ayora",
        "Pto.Villamil",
        "Milagro",
        "El Triunfo",
        "El Empalme",
        "Naranjal",
        "Anconcito",
        "Guaranda",
        "Chillanes",
        "Caluma",
        "Echeandia",
        "S.M.Bolivar",
        "Las Naves",
        "Quevedo",
        "Valencia",
        "Babahoyo",
        "Baba",
        "Ventanas",
        "Quinsaloma",
        "Vinces",
        "Palenque",
        "Catarama",
        "Mocache"
    ],

     "Cuenca": [
        "Cuenca",
        "Cañar",
        "Azogues",
        "Biblian",
        "Giron",
        "Santa Isabel",
        "Camilo Ponce E.",
        "Paute",
        "Gualaceo",
        "La Troncal",
        "Palora",
        "Macas",
        "Pablo Sexto",
        "Taisha",
        "Sucua",
        "Mendez",
        "Tiwintza",
        "Gualaquiza",
        "Limon Indanza"
    ],

     "Loja": [
        "Loja",
        "Catamayo",
        "Saraguro",
        "Gonzanama",
        "Cariamanga",
        "Catacocha",
        "Chaguarpamba",
        "Olmedo",
        "Zamora",
        "Nangaritza",
        "Yantzaza",
        "El Pangui",
        "Zumba",
        "Palanda",
        "Macara",
        "Sozoranga",
        "Zapotillo",
        "Alamor",
        "Celica",
        "Pindal",
        "Machala",
        "Santa Rosa",
        "Arenillas",
        "Huaquillas",
        "Piñas",
        "Marcabeli",
        "Zaruma"
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
function agregarContacto() {
  var nombre = document.getElementById("nombre").value;
  var email = document.getElementById("email").value;
  var celular = document.getElementById("celular").value;

  if (nombre === "" || email === "" || celular === "") {
    alert("Por favor, complete todos los campos.");
    return;
  }

  var contactosExistentes = document.getElementsByClassName("contacto");
  for (var i = 0; i < contactosExistentes.length; i++) {
    var contacto = contactosExistentes[i];
    var infoExistente = contacto.getElementsByTagName("p")[0].innerText;

    if (
      infoExistente.toLowerCase() ===
      (nombre + " - " + email + " - " + celular).toLowerCase()
    ) {
      alert("El contacto ya existe.");
      return;
    }
  }

  var listaContactos = document.getElementById("listaContactos");

  var nuevoContacto = document.createElement("div");
  nuevoContacto.classList.add("contacto");

  var info = document.createElement("p");
  info.textContent = nombre + " - " + email + " - " + celular;
  nuevoContacto.appendChild(info);

  var editarBoton = document.createElement("button");
  editarBoton.textContent = "Editar";
  editarBoton.classList.add("editar-button");
  editarBoton.onclick = function () {
    editarContacto(nuevoContacto);
  };
  nuevoContacto.appendChild(editarBoton);

  var borrarBoton = document.createElement("button");
  borrarBoton.textContent = "Borrar";
  borrarBoton.classList.add("borrar-button");
  borrarBoton.onclick = function () {
    nuevoContacto.remove();
  };
  nuevoContacto.appendChild(borrarBoton);

  listaContactos.appendChild(nuevoContacto);

  document.getElementById("nombre").value = "";
  document.getElementById("email").value = "";
  document.getElementById("celular").value = "";
}

function editarContacto(contacto) {
  var infoContacto = contacto.getElementsByTagName("p")[0].innerText;
  var datosContacto = infoContacto.split(" - ");

  document.getElementById("nombre").value = datosContacto[0];
  document.getElementById("email").value = datosContacto[1];
  document.getElementById("celular").value = datosContacto[2];

  var guardarBoton = document.createElement("button");
  guardarBoton.textContent = "Guardar";
  guardarBoton.classList.add("guardar-button");
  guardarBoton.onclick = function () {
    // Actualizar la información del contacto
    var nuevoNombre = document.getElementById("nombre").value;
    var nuevoEmail = document.getElementById("email").value;
    var nuevoCelular = document.getElementById("celular").value;

    var nuevaInfo = nuevoNombre + " - " + nuevoEmail + " - " + nuevoCelular;
    contacto.getElementsByTagName("p")[0].innerText = nuevaInfo;

    // Limpiar el formulario
    document.getElementById("nombre").value = "";
    document.getElementById("email").value = "";
    document.getElementById("celular").value = "";

    // Eliminar el botón de guardar y restablecer el de editar
    contacto.removeChild(guardarBoton);
    var editarBoton = document.createElement("button");
    editarBoton.textContent = "Editar";
    editarBoton.classList.add("editar-button");
    editarBoton.onclick = function () {
      editarContacto(contacto);
    };
    contacto.replaceChild(editarBoton, guardarBoton);
  };

  // Reemplazar el botón de editar por el de guardar
  contacto.replaceChild(guardarBoton, contacto.getElementsByClassName("editar-button")[0]);
}

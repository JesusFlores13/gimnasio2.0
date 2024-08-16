<template>
  <form @submit.prevent="submitForm" enctype="multipart/form-data">
    <div class="grid gap-12 mb-12 sm:grid-cols-2 mt-8">
      <div>
        <label class="px-1 block text-sm uppercase text-gray-500 mb-2 font-extrabold">Nombre</label>
        <input type="text" v-model="form.nombre"
          class="font-bold hover:bg-blue-100 focus:bg-blue-100 rounded-sm shadow-sm  focus:ring-0 w-full px-3 py-2 mb-5 border border-gray-300 rounded-xl placeholder-gray-400"
          placeholder="Nombre">
      </div>
      <div>
        <label class="px-1 block text-sm uppercase text-gray-500 mb-2 font-extrabold">Primer Apellido</label>
        <input type="text" v-model="form.primer_apellido"
          class="font-bold hover:bg-blue-100 focus:bg-blue-100 rounded-sm shadow-sm  focus:ring-0 w-full px-3 py-2 mb-5 border border-gray-300 rounded-xl placeholder-gray-400"
          placeholder="Primer apellido ">
      </div>
      <div>
        <label class="px-1 block text-sm uppercase text-gray-500 mb-2 font-extrabold">Segundo Apellido</label>
        <input type="text" v-model="form.segundo_apellido"
          class="font-bold hover:bg-blue-100 focus:bg-blue-100 rounded-sm shadow-sm  focus:ring-0 w-full px-3 py-2 mb-5 border border-gray-300 rounded-xl placeholder-gray-400"
          placeholder="Segundo Apellido">
      </div>
      <div>
        <label class="px-1 block text-sm uppercase text-gray-500 mb-2 font-extrabold">Titulo de cortesía</label>
        <input type="text" v-model="form.titulo_cortesia"
          class="font-bold hover:bg-blue-100 focus:bg-blue-100 rounded-sm shadow-sm  focus:ring-0 w-full px-3 py-2 mb-5 border border-gray-300 rounded-xl placeholder-gray-400"
          placeholder="Mr.">
      </div>
      <div>
        <label class="px-1 block text-sm uppercase text-gray-500 mb-2 font-extrabold">Fecha de nacimiento</label>
        <input type="date" v-model="form.fecha_nacimiento"
          class="font-bold hover:bg-blue-100 focus:bg-blue-100 rounded-sm shadow-sm  focus:ring-0 w-full px-3 py-2 mb-5 border border-gray-300 rounded-mxl placeholder-gray-400">
      </div>
      <div>
        <label class="px-1 block text-sm uppercase text-gray-500 mb-2 font-extrabold">Foto</label>
        <input type="file" @change="handleFileUpload"
          class="font-bold hover:bg-blue-100 focus:bg-blue-100 rounded-sm shadow-sm  focus:ring-0 w-full px-3 py-2 mb-5 border border-gray-300 rounded-xl placeholder-gray-400">
      </div>
      <div>
        <label class="px-1 block text-sm uppercase text-gray-500 mb-2 font-extrabold">Selecciona el genero</label>
        <select v-model="form.genero"
          class="font-bold hover:bg-blue-100 focus:bg-blue-100 rounded-sm shadow-sm  focus:ring-0 w-full px-3 py-2 mb-5 border border-gray-300 rounded-xl placeholder-gray-400">
          <option>-- Selecciona genero --</option>
          <option>Hombre</option>
          <option>Mujer</option>
          <option>Otro</option>
        </select>
      </div>
      <div>
        <label class="px-1 block text-sm uppercase text-gray-500 mb-2 font-extrabold">Selecciona tipo de sangre</label>
        <select v-model="form.tipo_sangre"
          class="font-bold hover:bg-blue-100 focus:bg-blue-100 rounded-sm shadow-sm  focus:ring-0 w-full px-3 py-2 mb-5 border border-gray-300 rounded-xl placeholder-gray-400">
          <option>-- Selecciona tipo de sangre --</option>
          <option>A+</option>
          <option>A-</option>
          <option>B+</option>
          <option>B-</option>
          <option>AB+</option>
          <option>AB-</option>
          <option>O+</option>
          <option>O-</option>
        </select>
      </div>
    </div>
    <button type="submit" class="bg-blue-500 text-white px-4 py-2 rounded-lg">Enviar</button>
  </form>
</template>

<script>
import axios from 'axios';

export default {
  data() {
    return {
      form: {
        nombre: '',
        primer_apellido: '',
        segundo_apellido: '',
        titulo_cortesia: '',
        fecha_nacimiento: '',
        foto: '',
        genero: '',
        tipo_sangre: ''
      }
    };
  },
  methods: {
    handleFileUpload(event) {
      this.form.foto = event.target.files[0];
    },
    async submitForm() {
      const formData = new FormData();
      formData.append('nombre', this.form.nombre);
      formData.append('primer_apellido', this.form.primer_apellido);
      formData.append('segundo_apellido', this.form.segundo_apellido);
      formData.append('titulo_cortesia', this.form.titulo_cortesia);
      formData.append('fecha_nacimiento', this.form.fecha_nacimiento);
      formData.append('foto', this.form.foto);
      formData.append('genero', this.form.genero);
      formData.append('tipo_sangre', this.form.tipo_sangre);

      try {
        const response = await axios.post('http://localhost:8000/submit-form/', formData, {
          headers: {
            'Content-Type': 'multipart/form-data'
          }
        });
        console.log('Formulario enviado:', response.data);
      } catch (error) {
        console.error('Error al enviar el formulario:', error);
      }
    }
  }
};
</script>

<style>
/* Puedes agregar estilos personalizados aquí */
</style>

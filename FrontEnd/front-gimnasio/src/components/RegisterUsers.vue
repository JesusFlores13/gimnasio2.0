<template>
    <div class=" py-10 flex-col bg-gray-100 items-center sm:justify-center min-h-screen ">
        <div class="mt-8 mx-auto  max-w-4xl">
            <div class="bg-white  py-8 px-4 shadow-lg rounded-xl  ">
                <h1 class="text-2xl xl:text-2xl text-center font-bold">Registrate</h1>

                <Persona></Persona>
                <h1 class="text-2xl xl:text-2xl text-center font-bold mt-8">Datos de acceso</h1>

                <Usuraio></Usuraio>

                <input
                    class="w-full bg-blue-600 hover:bg-blue-700 text-white font-extrabold py-3 cursor-pointer transition duration-500 ease-in-out  transform hover:-translate-x hover:scale-105 rounded-xl"
                    type="submit" value="Registrarse" href='/'>

                <div class="mt-7">
                    <div class=" flex justify-center items-center">
                        <label class="mr-2 ">¿Ya tienes una cuenta?</label>
                        <a href='/'
                            class=" text-blue-500 transition duration-500 ease-in-out  transform hover:-translate-x hover:scale-105">
                            Iniciar sesio
                        </a>
                    </div>
                </div>
                <div class="mt-7">
                    <div class=" flex justify-center items-center">
                        <label class="mr-2 ">¿Olvidaste tu contraseña?</label>
                        <a href='/'
                            class=" text-blue-500 transition duration-500 ease-in-out  transform hover:-translate-x hover:scale-105">
                            Recupar Contraseña
                        </a>
                    </div>
                </div>

            </div>
        </div>
    </div>
</template>

<script>
import Persona from './Persona.vue'
import Usuraio from './Usuario.vue'
export default {
    components: {
        Persona,
        Usuraio
    }, components: { Usuraio, Persona }

}
</script>
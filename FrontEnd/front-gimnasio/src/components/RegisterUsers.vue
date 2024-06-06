<template>
    <div class=" py-10 flex-col bg-gray-100 items-center sm:justify-center min-h-screen ">
        <div class="mt-8 mx-auto  max-w-4xl">
            <div class="bg-white  py-8 px-4 shadow-lg rounded-xl  ">
                <form>
                    <h1 class="text-2xl xl:text-2xl text-center font-bold">Registrate</h1>

                <div class="grid gap-12 mb-12 sm:grid-cols-2 mt-8 ">
                    <div>
                        <label class="px-1 block text-sm uppercase text-gray-500 mb-2 font-extrabold">Nombre</label>
                        <input type="text"
                            class="font-bold hover:bg-blue-100 focus:bg-blue-100 rounded-sm shadow-sm  focus:ring-0 w-full px-3 py-2 mb-5 border border-gray-300 rounded-xl placeholder-gray-400"
                            placeholder="Nombre">

                    </div>
                    <div>
                        <label class="px-1 block text-sm uppercase text-gray-500 mb-2 font-extrabold">Primer
                            Apellido</label>
                        <input type="text"
                            class="font-bold hover:bg-blue-100 focus:bg-blue-100 rounded-sm shadow-sm  focus:ring-0 w-full px-3 py-2 mb-5 border border-gray-300 rounded-xl placeholder-gray-400"
                            placeholder="Primer apellido ">
                    </div>
                    <div>
                        <label class="px-1 block text-sm uppercase text-gray-500 mb-2 font-extrabold">Segundo Apellido
                        </label>
                        <input type="text"
                            class="font-bold hover:bg-blue-100 focus:bg-blue-100 rounded-sm shadow-sm  focus:ring-0 w-full px-3 py-2 mb-5 border border-gray-300 rounded-xl placeholder-gray-400"
                            placeholder="Segundo Apellido">
                    </div>
                    <div>
                        <label class="px-1 block text-sm uppercase text-gray-500 mb-2 font-extrabold">Titulo de cortesia
                        </label>
                        <input type="text"
                            class="font-bold hover:bg-blue-100 focus:bg-blue-100 rounded-sm shadow-sm  focus:ring-0 w-full px-3 py-2 mb-5 border border-gray-300 rounded-xl placeholder-gray-400"
                            placeholder="Mr.">
                    </div>
                    <div>
                        <label class="px-1 block text-sm uppercase text-gray-500 mb-2 font-extrabold">Fecha de
                            nacimiento</label>
                        <input type="date"
                            class="font-bold hover:bg-blue-100 focus:bg-blue-100 rounded-sm shadow-sm  focus:ring-0 w-full px-3 py-2 mb-5 border border-gray-300 rounded-mxl placeholder-gray-400"
                            >
                    </div>
                    <div>
                        <label class="px-1 block text-sm uppercase text-gray-500 mb-2 font-extrabold">Foto</label>
                        <input type="file"
                            class="font-bold hover:bg-blue-100 focus:bg-blue-100 rounded-sm shadow-sm  focus:ring-0 w-full px-3 py-2 mb-5 border border-gray-300 rounded-xl placeholder-gray-400"
                            >
                    </div>
                    <div>
                        <label class="px-1 block text-sm uppercase text-gray-500 mb-2 font-extrabold">Selecciona el
                            genero</label>
                        <select
                            class="font-bold hover:bg-blue-100 focus:bg-blue-100 rounded-sm shadow-sm  focus:ring-0 w-full px-3 py-2 mb-5 border border-gray-300 rounded-xl placeholder-gray-400"
                            >
                            <option>-- Selecciona genero --</option>
                            <option>Hombre</option>
                            <option>Mujer</option>
                            <option>Otro</option>
                        </select>
                    </div>
                    <div>
                        <label class="px-1 block text-sm uppercase text-gray-500 mb-2 font-extrabold">Selecciona tipo de
                            sangre</label>
                        <select
                            class="font-bold hover:bg-blue-100 focus:bg-blue-100 rounded-sm shadow-sm  focus:ring-0 w-full px-3 py-2 mb-5 border border-gray-300 rounded-xl placeholder-gray-400"
                            >
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
                    
                <h1 class="text-2xl xl:text-2xl text-center font-bold mt-8">Datos de acceso</h1>
                <br>
                <div class="grid gap-12 mb-12 sm:grid-cols-3">
                <div>
                    <label class="px-1 block text-sm uppercase text-gray-500 mb-2 font-extrabold">Usuario</label>
                    <input type="text"
                        class="font-bold hover:bg-blue-100 focus:bg-blue-100 rounded-sm shadow-sm  focus:ring-0 w-full px-3 py-2 mb-5 border border-gray-300 rounded-xl placeholder-gray-400"
                        placeholder="Genera un nombre de     usuario">
                </div>
                <div>
                    <label class="px-1 block text-sm uppercase text-gray-500 mb-2 font-extrabold">Contraseña</label>
                    <input type="password"
                        class="font-bold hover:bg-blue-100 focus:bg-blue-100 rounded-sm shadow-sm  focus:ring-0 w-full px-3 py-2 mb-5 border border-gray-300 rounded-xl placeholder-gray-400"
                        placeholder="Crear contraseña">
                </div>
                <div>
                    <label class="px-1 block text-sm uppercase text-gray-500 mb-2 font-extrabold">Repetir
                        contraseña</label>
                    <input type="password"
                        class="font-bold hover:bg-blue-100 focus:bg-blue-100 rounded-sm shadow-sm  focus:ring-0 w-full px-3 py-2 mb-5 border border-gray-300 rounded-xl placeholder-gray-400"
                        placeholder="Confirma tu contraseña">
                </div>
            </div>

                <input
                    class="w-full bg-blue-600 hover:bg-blue-700 text-white font-extrabold py-3 cursor-pointer transition duration-500 ease-in-out  transform hover:-translate-x hover:scale-105 rounded-xl"
                    type="submit" value="Crear Cuenta" href='/'>

                    <div class="mt-7">
                        <div class=" flex justify-center items-center">
                            <label class="mr-2 " >¿Ya tienes una cuenta?</label>
                            <a href='/' class=" text-blue-500 transition duration-500 ease-in-out  transform hover:-translate-x hover:scale-105">
                                Iniciar sesion
                            </a>
                        </div>
                    </div>
                    <div class="mt-7">
                        <div class=" flex justify-center items-center">
                            <label class="mr-2 " >¿Olvidaste tu contraseña?</label>
                            <a href='/' class=" text-blue-500 transition duration-500 ease-in-out  transform hover:-translate-x hover:scale-105">
                                Recupar Contraseña
                            </a>
                        </div>
                    </div>
                    
            </form>

        </div>
    </div>
</div>
</template>
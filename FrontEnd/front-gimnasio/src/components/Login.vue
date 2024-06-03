<template>
    <div class="py-10 flex-col bg-gray-100 items-center sm:justify-center min-h-screen">
        <div class="mt-8 mx-auto  max-w-lg ">
            <div class="bg-white  py-8 px-4 shadow-lg rounded-xl ">
                <form >
                    <label for="" class="block mt-3 text-xl text-gray-700 text-center font-extrabold">
                    Iniciar sesion 
                </label>
                
                
                    <div>
                        <label class="px-1 block text-sm uppercase text-gray-500 mb-2 font-extrabold">Usuario</label>
                        <input type="text" class="font-bold hover:bg-blue-100 focus:bg-blue-100 rounded-sm shadow-sm  focus:ring-0 w-full px-3 py-2 mb-5 border border-gray-300 rounded-md placeholder-gray-400" placeholder="Ingresar correo o nombre de usuario">

                    </div>
                    <div>
                       <label class="px-1 block text-sm uppercase text-gray-500 mb-2 font-extrabold">Contraseña</label>
                        <input type="text" class="font-bold hover:bg-blue-100 focus:bg-blue-100 rounded-sm shadow-sm  focus:ring-0 w-full px-3 py-2 mb-5 border border-gray-300 rounded-md placeholder-gray-400" placeholder="Ingresar contraseña">
                    </div>
                    
                    <input class="w-full bg-blue-600 hover:bg-blue-700 text-white font-extrabold py-3 cursor-pointer transition duration-500 ease-in-out  transform hover:-translate-x hover:scale-105 rounded-xl" type="submit" value="Crear Cuenta">
                    <div class="mt-7">
                        <div class="flex justify-center items-center">
                            <label class="mr-2" >¿No tienes una cuenta?</label>
                            <a href='/registe' class=" text-blue-500 transition duration-500 ease-in-out  transform hover:-translate-x hover:scale-105">
                                Crear cuenta
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
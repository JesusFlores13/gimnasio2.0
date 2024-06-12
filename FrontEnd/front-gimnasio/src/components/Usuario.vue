<template>
    <form>

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

       
    </form>
</template>
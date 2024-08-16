<template>
    <label for="" class="block mt-3 text-xl text-gray-700 text-center font-extrabold p-6">
        instalaciones
    </label>

    <div class="bg-white  py-8 px-4 shadow-lg rounded-xl ">
        <form>

            <div class="grid gap-12 mb-12 sm:grid-cols-2 mt-8 ">
                <div>
                    <label class="px-1 block text-sm uppercase text-gray-500 mb-2 font-extrabold">Servicio</label>
                    <input type="text"
                        class="font-bold hover:bg-blue-100 focus:bg-blue-100 rounded-sm shadow-sm  focus:ring-0 w-full px-3 py-2 mb-5 border border-gray-300 rounded-xl placeholder-gray-400"
                        placeholder="Servicio">

                </div>
                <div>
                    <label class="px-1 block text-sm uppercase text-gray-500 mb-2 font-extrabold">Descripcion</label>
                    <input type="text"
                        class="font-bold hover:bg-blue-100 focus:bg-blue-100 rounded-sm shadow-sm  focus:ring-0 w-full px-3 py-2 mb-5 border border-gray-300 rounded-xl placeholder-gray-400"
                        placeholder="Descripcion ">
                </div>
                <div>
                    <label class="px-1 block text-sm uppercase text-gray-500 mb-2 font-extrabold">Tipo
                    </label>
                    <input type="text"
                        class="font-bold hover:bg-blue-100 focus:bg-blue-100 rounded-sm shadow-sm  focus:ring-0 w-full px-3 py-2 mb-5 border border-gray-300 rounded-xl placeholder-gray-400"
                        placeholder="Tipo">
                </div>
                <div>
                    <label class="px-1 block text-sm uppercase text-gray-500 mb-2 font-extrabold">Observaciones
                    </label>
                    <input type="text"
                        class="font-bold hover:bg-blue-100 focus:bg-blue-100 rounded-sm shadow-sm  focus:ring-0 w-full px-3 py-2 mb-5 border border-gray-300 rounded-xl placeholder-gray-400"
                        placeholder="Observaciones">
                </div>
                <div>
                    <label class="px-1 block text-sm uppercase text-gray-500 mb-2 font-extrabold">Calificaciones</label>
                    <input type="text"
                        class="font-bold hover:bg-blue-100 focus:bg-blue-100 rounded-sm shadow-sm  focus:ring-0 w-full px-3 py-2 mb-5 border border-gray-300 rounded-mxl placeholder-gray-400">
                </div>
                <div>
                    <label class="px-1 block text-sm uppercase text-gray-500 mb-2 font-extrabold">Sucursal</label>
                    <input type="text"
                        class="font-bold hover:bg-blue-100 focus:bg-blue-100 rounded-sm shadow-sm  focus:ring-0 w-full px-3 py-2 mb-5 border border-gray-300 rounded-mxl placeholder-gray-400">
                </div>
                <div>
                    <label class="px-1 block text-sm uppercase text-gray-500 mb-2 font-extrabold">Horario disponible</label>
                    <input type="text"
                        class="font-bold hover:bg-blue-100 focus:bg-blue-100 rounded-sm shadow-sm  focus:ring-0 w-full px-3 py-2 mb-5 border border-gray-300 rounded-mxl placeholder-gray-400">
                </div>
                <!-- <div>
        <label class="px-1 block text-sm uppercase text-gray-500 mb-2 font-extrabold">Total empleados</label>
        <input type="text"
            class="font-bold hover:bg-blue-100 focus:bg-blue-100 rounded-sm shadow-sm  focus:ring-0 w-full px-3 py-2 mb-5 border border-gray-300 rounded-mxl placeholder-gray-400">
    </div> -->
                <!-- <div>
        <label class="px-1 block text-sm uppercase text-gray-500 mb-2 font-extrabold">Foto</label>
        <input type="file"
            class="font-bold hover:bg-blue-100 focus:bg-blue-100 rounded-sm shadow-sm  focus:ring-0 w-full px-3 py-2 mb-5 border border-gray-300 rounded-xl placeholder-gray-400">
    </div> -->
                <!-- <div>
        <label class="px-1 block text-sm uppercase text-gray-500 mb-2 font-extrabold">Selecciona el
            genero</label>
        <select
            class="font-bold hover:bg-blue-100 focus:bg-blue-100 rounded-sm shadow-sm  focus:ring-0 w-full px-3 py-2 mb-5 border border-gray-300 rounded-xl placeholder-gray-400">
            <option>-- Selecciona genero --</option>
            <option>Hombre</option>
            <option>Mujer</option>
            <option>Otro</option>
        </select>
    </div> -->
                <!-- <div>
        <label class="px-1 block text-sm uppercase text-gray-500 mb-2 font-extrabold">Selecciona tipo de
            sangre</label>
        <select
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
    </div> -->
            </div>
        </form>

        <!-- <div class="relative overflow-x-auto">
    <table class="w-full text-sm text-left rtl:text-right text-gray-500 dark:text-gray-400">
        <thead class="text-xs text-gray-700 uppercase bg-gray-50 dark:bg-gray-700 dark:text-gray-400">
            <tr>
                <th scope="col" class="px-6 py-3">
                    Product name
                </th>
                <th scope="col" class="px-6 py-3">
                    Color
                </th>
                <th scope="col" class="px-6 py-3">
                    Category
                </th>
                <th scope="col" class="px-6 py-3">
                    Price
                </th>
            </tr>
        </thead>
        <tbody>
            <tr class="bg-white border-b dark:bg-gray-800 dark:border-gray-700">
                <th scope="row" class="px-6 py-4 font-medium text-gray-900 whitespace-nowrap dark:text-white">
                    Apple MacBook Pro 17"
                </th>
                <td class="px-6 py-4">
                    Silver
                </td>
                <td class="px-6 py-4">
                    Laptop
                </td>
                <td class="px-6 py-4">
                    $2999
                </td>
            </tr>
            <tr class="bg-white border-b dark:bg-gray-800 dark:border-gray-700">
                <th scope="row" class="px-6 py-4 font-medium text-gray-900 whitespace-nowrap dark:text-white">
                    Microsoft Surface Pro
                </th>
                <td class="px-6 py-4">
                    White
                </td>
                <td class="px-6 py-4">
                    Laptop PC
                </td>
                <td class="px-6 py-4">
                    $1999
                </td>
            </tr>
            <tr class="bg-white dark:bg-gray-800">
                <th scope="row" class="px-6 py-4 font-medium text-gray-900 whitespace-nowrap dark:text-white">
                    Magic Mouse 2
                </th>
                <td class="px-6 py-4">
                    Black
                </td>
                <td class="px-6 py-4">
                    Accessories
                </td>
                <td class="px-6 py-4">
                    $99
                </td>
            </tr>
        </tbody>
    </table>
</div> -->
    </div>
</template>
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Matriz de Proveedores ProServices</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            margin: 20px;
        }
        .container {
            max-width: 1200px;
            margin: 0 auto;
        }
        h1 {
            color: #2c3e50;
            text-align: center;
        }
        .search-box {
            margin: 20px 0;
            padding: 15px;
            background: #f8f9fa;
            border-radius: 5px;
        }
        table {
            width: 100%;
            border-collapse: collapse;
            margin-top: 20px;
        }
        th, td {
            border: 1px solid #ddd;
            padding: 8px;
            text-align: left;
        }
        th {
            background-color: #3498db;
            color: white;
        }
        tr:nth-child(even) {
            background-color: #f2f2f2;
        }
        .filter-section {
            margin-bottom: 15px;
        }
        .hidden {
            display: none;
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>Matriz de Proveedores ProServices</h1>
        
        <div class="search-box">
            <div class="filter-section">
                <label for="proveedor">Filtrar por Proveedor:</label>
                <select id="proveedor">
                    <option value="">Todos</option>
                    <option value="PGIC">PGIC</option>
                    <option value="KOSLAN">KOSLAN</option>
                    <option value="KSB">KSB</option>
                    <option value="COSMOPLAS">COSMOPLAS</option>
                    <option value="FRANKLIN">FRANKLIN</option>
                    <option value="HCP">HCP</option>
                </select>
            </div>
            
            <div class="filter-section">
                <label for="categoria">Filtrar por Categoría:</label>
                <select id="categoria">
                    <option value="">Todas</option>
                    <!-- Las opciones se llenarán con JavaScript -->
                </select>
            </div>
            
            <div class="filter-section">
                <label for="busqueda">Buscar producto:</label>
                <input type="text" id="busqueda" placeholder="Ingrese modelo o descripción">
                <button onclick="filtrarDatos()">Buscar</button>
            </div>
        </div>
        
        <table id="tablaProveedores">
            <thead>
                <tr>
                    <th>Proveedor</th>
                    <th>Marca</th>
                    <th>Línea de Producto</th>
                    <th>Modelo</th>
                    <th>Categoría</th>
                    <th>Procedencia</th>
                    <th>% Desc.</th>
                    <th>Pago</th>
                    <th>Garantía</th>
                    <th>Contacto</th>
                    <th>Acciones</th>
                </tr>
            </thead>
            <tbody>
                <!-- Los datos se llenarán con JavaScript -->
            </tbody>
        </table>
        
        <div id="detalleProducto" class="hidden">
            <h2>Detalle del Producto</h2>
            <div id="detalleContenido"></div>
            <button onclick="cerrarDetalle()">Volver</button>
        </div>
    </div>

    <script>
        // Datos de proveedores (simplificados para el ejemplo)
        const proveedores = [
            {
                proveedor: "PGIC",
                marca: "STAIRS",
                linea: "Bombas multietapas horizontales inox AISI 304",
                modelo: "MXHM / MXH",
                categoria: "Bomba Superficie Inox",
                procedencia: "China",
                descuento: 0.4,
                pago: "Cheques 60 días",
                condicionPago: "sobre 1MM / 2 cheques/ sobre 2MM 3 cheques",
                garantia: "1 año",
                precioApp: "App PGIC",
                descuentoExtra: "Sí",
                montoActivacion: 1500000,
                entrega: "1 día hábil",
                contacto: "Valeska Canales / +56 9 6206 0189",
                email: "vcanales@pgic.cl",
                web: "https://b2b.pgic.cl",
                telefono: "+56 2 1234 5678",
                datosApp: "Usuario: Kimberly / Clave: Operaciones24"
            },
            // ... (agregar todos los demás productos de la misma forma)
        ];

        // Llenar la tabla al cargar la página
        document.addEventListener('DOMContentLoaded', function() {
            llenarTabla(proveedores);
            llenarCategorias();
        });

        function llenarTabla(datos) {
            const tbody = document.querySelector('#tablaProveedores tbody');
            tbody.innerHTML = '';
            
            datos.forEach(item => {
                const tr = document.createElement('tr');
                tr.innerHTML = `
                    <td>${item.proveedor}</td>
                    <td>${item.marca}</td>
                    <td>${item.linea}</td>
                    <td>${item.modelo}</td>
                    <td>${item.categoria}</td>
                    <td>${item.procedencia}</td>
                    <td>${item.descuento * 100}%</td>
                    <td>${item.pago}</td>
                    <td>${item.garantia}</td>
                    <td>${item.contacto.split('/')[0].trim()}</td>
                    <td><button onclick="verDetalle('${item.proveedor}', '${item.marca}', '${item.linea}')">Detalle</button></td>
                `;
                tbody.appendChild(tr);
            });
        }

        function llenarCategorias() {
            const categorias = [...new Set(proveedores.map(item => item.categoria))];
            const select = document.getElementById('categoria');
            
            categorias.forEach(cat => {
                const option = document.createElement('option');
                option.value = cat;
                option.textContent = cat;
                select.appendChild(option);
            });
        }

        function filtrarDatos() {
            const proveedor = document.getElementById('proveedor').value;
            const categoria = document.getElementById('categoria').value;
            const busqueda = document.getElementById('busqueda').value.toLowerCase();
            
            let filtrados = proveedores;
            
            if (proveedor) {
                filtrados = filtrados.filter(item => item.proveedor === proveedor);
            }
            
            if (categoria) {
                filtrados = filtrados.filter(item => item.categoria === categoria);
            }
            
            if (busqueda) {
                filtrados = filtrados.filter(item => 
                    item.linea.toLowerCase().includes(busqueda) || 
                    item.modelo.toLowerCase().includes(busqueda)
                );
            }
            
            llenarTabla(filtrados);
        }

        function verDetalle(proveedor, marca, linea) {
            const producto = proveedores.find(item => 
                item.proveedor === proveedor && 
                item.marca === marca && 
                item.linea === linea
            );
            
            if (producto) {
                document.getElementById('tablaProveedores').classList.add('hidden');
                document.getElementById('detalleProducto').classList.remove('hidden');
                
                const detalle = document.getElementById('detalleContenido');
                detalle.innerHTML = `
                    <h3>${producto.marca} - ${producto.linea}</h3>
                    <p><strong>Proveedor:</strong> ${producto.proveedor}</p>
                    <p><strong>Modelo:</strong> ${producto.modelo}</p>
                    <p><strong>Categoría:</strong> ${producto.categoria}</p>
                    <p><strong>Procedencia:</strong> ${producto.procedencia}</p>
                    <p><strong>Descuento:</strong> ${producto.descuento * 100}%</p>
                    <p><strong>Condiciones de pago:</strong> ${producto.condicionPago}</p>
                    <p><strong>Garantía:</strong> ${producto.garantia}</p>
                    <p><strong>Entrega:</strong> ${producto.entrega}</p>
                    <p><strong>Contacto:</strong> ${producto.contacto}</p>
                    <p><strong>Email:</strong> ${producto.email}</p>
                    <p><strong>Web:</strong> <a href="${producto.web}" target="_blank">${producto.web}</a></p>
                    <p><strong>Teléfono:</strong> ${producto.telefono}</p>
                    <p><strong>Datos App:</strong> ${producto.datosApp}</p>
                `;
            }
        }

        function cerrarDetalle() {
            document.getElementById('tablaProveedores').classList.remove('hidden');
            document.getElementById('detalleProducto').classList.add('hidden');
        }
    </script>
</body>
</html>

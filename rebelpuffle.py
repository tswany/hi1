var Discord = require('discord.io');

var bot = new Discord.Client({
    token: "MzAwNjQyNTQzOTU0Mjk2ODMy.C8wHyw.ck1UJG9d_TWAdl5XMk5-1s0b3A4",
    autorun: true
});

bot.on('ready', function() {
    console.log('Logged in as %s - %s\n', bot.username, bot.id);
});

bot.on('message', function(user, userID, channelID, message, event) {
    if (message === ";ping") {
        bot.sendMessage({
            to: channelID,
            message: "Pong."
        });
    }
});

bot.on('message', function(user, userID, channelID, message, event) {
    if (message === ";opinion") {
        bot.sendMessage({
            to: channelID,
            message: "I hate pookies."
        });
    }
});

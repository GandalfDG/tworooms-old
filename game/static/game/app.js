/*
 *  1. send a POST with a player name to create a new game
 *  2. receive a response with the newly created game
 *  3. switch to the lobby and poll for players being added
 *  4. player 1 will start the game with a POST 
 *  5. all players will be switched to the game screen
 */

var page = "home"

var app = new Vue({
    // Remove clashing delimiter to work with Django templates
    delimiters: ['[[',']]'],
    el: '#app',
    data: {
        message: 'Hello Vue!',
        current_page: page,
    }
})


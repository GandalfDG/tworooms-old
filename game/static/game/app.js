var page = "home"

var app = new Vue({
    // Remove clashing delimiter to work with Django templates
    delimiters: ['[[',']]'],
    el: '#app',
    data: {
        message: 'Hello Vue!',
        current_page: page,
    }
    computed: {
        current_time: 
    }
})


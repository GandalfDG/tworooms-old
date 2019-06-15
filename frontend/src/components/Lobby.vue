<template>
    <div>
        <h1>Access Code: {{accessCode}}</h1>
        <ul v-if="players">
            <li v-for="player in players">{{player}}</li>
        </ul>
    </div>
</template>

<script>
import axios from 'axios'
export default {
    data() {
      return {
        players: ['bob', 'joe', 'steve'],
      }
    },
    props: ['accessCode'],
    created() {
        let self = this
        setInterval(() => {
            axios.get('http://localhost:8000/game?access_code=' + self.accessCode)
                .then((response) => {
                    self.players = response.data.players
                }
            )
        }, 5000)
    }
}
</script>

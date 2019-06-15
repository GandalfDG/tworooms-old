<template>
  <form>
    <div class="form-group">
      <label for="playerName">Enter Your Name</label>
      <input
        v-model="name"
        type="text"
        class="form-control"
        id="playerName"
        placeholder="John Smith"
      >
    </div>
    <button @click="createGame" type="button" class="btn btn-primary">Create Game</button>
  </form>
</template>

<script>
import axios from 'axios'
export default {
  data () {
    return {
      name: ''
    }
  },
  methods: {
    createGame () {
      axios.post('http://localhost:8000/newgame/', {'player_name': this.name}).then(function (response) {
        console.log(response)
      })
    }
  }
}
</script>

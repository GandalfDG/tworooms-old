<template>
  <div>
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
    <h1 v-if="accessCode">{{accessCode}}</h1>
  </div>
</template>

<script>
import axios from 'axios'
export default {
  data () {
    return {
      name: '',
      accessCode: ''
    }
  },
  methods: {
    createGame () {
      let self = this
      axios
        .post('http://localhost:8000/newgame/', { player_name: this.name })
        .then((response) => self.accessCode = response.data.access_code)
    },
    updateAccessCode (response) {
      this.accessCode = response.data.access_code
    }
  }
}
</script>

<template>
  <div id="register">
    <div class="forms">
      <h2>在室登録</h2>
      <div class="form-name">
        <p>名前</p>
        <input type="text" name="name" placeholder="名前" v-model="name" />
      </div>
      <div class="form-name">
        <p>入室時刻</p>
        <input type="date" name="intime" placeholder="入室時刻" v-model="intime" />
      </div>
      <div class="form-name">
        <p>退室時刻</p>
        <input type="date" name="outtime" placeholder="退室時刻" v-model="outtime" />
      </div>
      <div class="form-name">
        <p>コメント</p>
        <input type="text" name="comment" placeholder="コメント" v-model="comment" />
      </div>
      <div class="form-pass">
        <p>パスワード</p>
        <input type="text" name="pass" placeholder="パスワード" v-model="pass" />
      </div>
      <div>
        <button @click="Register">登録する</button>
      </div>
    </div>
  </div>
</template>

<style scoped>
#register {
  text-align: center;
}

.forms {
  margin: 0 auto;
  background-color: white;
  border: 1px solid #d1d1d1;
  border-radius: 10px;
}

h2 {
  margin: 40px;
}

h2,
p {
  color: #375a7f;
}

button {
  width: 20%;
  background-color: #375a7f;
  color: white;
  padding: 10px 0;
  border: none;
  border-radius: 10px;
  cursor: pointer;
  margin-bottom: 50px;
}

@media screen and (max-width: 599px) {
  .forms {
    width: 100%;
  }
  h2 {
    margin-bottom: 20px;
  }
  .form-name {
    padding-top: 15px 0;
    margin-bottom: 20px;
  }

  .form-pass {
    padding-top: 15px 0;
    margin-bottom: 40px;
  }
  input {
  padding: 5px 10px;
  min-width: 70%;
  }
}

@media screen and (min-width: 600px) and (max-width: 959px) {
  .forms {
    width: 90%;
  }
  h2 {
    margin-bottom: 30px;
  }
  .form-name {
    padding-top: 15px 0;
    margin-bottom: 60px;
  }

  .form-pass {
    padding-top: 15px 0;
    margin-bottom: 50px;
  }
  input {
  padding: 5px 10px;
  min-width: 60%;
  }
}

@media screen and (min-width: 960px){
  .forms {
    width: 50%;
  }
  h2 {
    margin-bottom: 50px;
  }
  .form-name {
    padding-top: 15px 0;
    margin-bottom: 20px;
  }

  .form-pass {
    padding-top: 15px 0;
    margin-bottom: 70px;
  }
  input {
  padding: 5px 10px;
  min-width: 40%;
  }
}

</style>

<script>

</script>
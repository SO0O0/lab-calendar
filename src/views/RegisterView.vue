<template>
  <div id="register">
    <div class="form">
    <!-- 名前フォーム -->
            <div class="form-name">
                <p>名前</p>
                <input type="text" name="name" placeholder="名前" v-model="name">
            </div>
        <div>
          <button disabled>送信する</button>
        </div>
    </div>
  </div>
</template>

<style scoped>
#register{
    text-align:center;
}

.form{
  margin:0 auto;
  width:40%;
  background-color:whitesmoke;
}

.form-name{
    padding:15px 0;
    margin-bottom:30px;
}

input{
    padding:5px 10px;
    min-width:250px;
}

button{
    width:20%;
    background-color: #375a7f;
    color:white;
    padding:10px 0;
    border:none;
    border-radius:10px;
    cursor:pointer;
    margin-bottom: 50px;
}
</style>

<script></script>
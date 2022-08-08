<template>
  <div id="register">
    <div class="forms">
      <h2>在室登録</h2>
            <div class="form-name">
                <p>名前</p>
                <input type="text" name="name" placeholder="名前" v-model="name">
            </div>
            <div class="form-name">
                <p>入室時刻</p>
                <input type="date" name="intime" placeholder="入室時刻" v-model="name">
            </div>
            <div class="form-name">
                <p>退室時刻</p>
                <input type="date" name="outtime" placeholder="退室時刻" v-model="name">
            </div>
            <div class="form-name">
                <p>コメント</p>
                <input type="text" name="comment" placeholder="コメント" v-model="name">
            </div>
            <div class="form-pass">
                <p>パスワード</p>
                <input type="text" name="pass" placeholder="パスワード" v-model="name">
            </div>
        <div>
          <button disabled>登録する</button>
        </div>
    </div>
  </div>
</template>

<style scoped>
#register{
    text-align:center;
}

.forms{
  margin:0 auto;
  width:40%;
  background-color:whitesmoke;
  border-radius:10px;
}

.forms h2{
  padding-top:40px;
}

.form-name{
    padding-top:15px 0;
    margin-bottom:50px
}

.form-pass{
    padding-top:15px 0;
    margin-bottom:70px;
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
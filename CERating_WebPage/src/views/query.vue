<template>
  <div class="con-background">
    <el-header>
      <!-- 菜单栏 -->
      <div class="menu">
        <!-- <div class="menu-item" :key="0">
          <a href="/" @click="activeURL = 0">Logo</a>
          <div
              class="menu-underline"
              :class="{ activedPage: activeURL == 0 }"
          ></div>
        </div> -->
        <div class="menu-item" :key="1">
          <a href="/" @click="activeURL = 1">首页</a>
          <div
              class="menu-underline"
              :class="{ activedPage: activeURL == 1 }"
          ></div>
        </div>
        <div class="menu-item" :key="2">
          <a href="/bulletin" @click="activeURL = 2">公告</a>
          <div
              class="menu-underline"
              :class="{ activedPage: activeURL == 2 }"
          ></div>
        </div>
        <div class="menu-item" :key="3">
          <a href="/announcement" @click="activeURL = 3">帮助</a>
          <div
              class="menu-underline"
              :class="{ activedPage: activeURL == 3 }"
          ></div>
        </div>
        <div class="menu-item" :key="4">
          <a href="/query" @click="activeURL = 4">查询</a>
          <div
              class="menu-underline"
              :class="{ activedPage: activeURL == 4 }"
          ></div>
        </div>
      </div>
      <!-- 个人 -->
      <div class="person">
        <a href="/Login" @click="activeURL = 0" style="text-decoration:none;color:black;">登录</a>
        <div class="person-img">
          <a href="/Login" @click="activeURL = 0"><img src="../assets/person.png" alt="" /></a>
        </div>
        <!-- TODO 点击头像下拉框 -->
      </div>
    </el-header>
  </div>
  <!-- 个人 -->
  <div class="person">
    <a href="/Login" @click="activeURL = 0" style="text-decoration:none;color:black;">登录</a>
    <div class="person-img">
      <a href="/Login" @click="activeURL = 0"><img src="../assets/person.png" alt="" /></a>
    </div>
  </div>
  <div class="left-container">
    <div class="logo-box">
      <img src="../assets/logo.png" alt="" />
      <span>CERating</span>
    </div>
    <div class="text-box">
      <h3>让标准</h3>
      <p>成为人与自然之间的桥梁</p>
    </div>
    <div class="footer-box">
        <span class="footer-list">
          <a class="footer-about" target="_blank" href="/about">关于</a>
          <span class="footer-line"></span>
          <a class="footer-help" target="_blank" href="">帮助</a>
        </span>
      <span class="footer-copyright"> 2022 ©CERating </span>
    </div>
  </div>
    <div>
        查询
    </div>
  <div class="login">
    <div class="loginPart">
      <h2>模拟评级</h2>
      <h3>碳排放评级详情查询</h3>
      <el-form>
        <a style="color:whitesmoke">选择企业</a>
        <select v-model="goodsId" style="width:200px;height: 30px;margin-top: 5px;margin-bottom: 5px;margin-left: 10px">
          <option value="">选择企业</option>
          <!--                <option v-for="item in kindList" v-bind:value="item.id" v-text="item.name" ></option>-->
        </select>
        <div class="inputElement">
          <el-input placeholder="请输入指标X "></el-input>
        </div>
        <div class="inputElement">
          <el-input placeholder="请输入指标X "></el-input>
        </div>
        <div class="inputElement">
          <el-input placeholder="请输入指标X "></el-input>
        </div>
        <div class="inputElement">
          <el-input placeholder="请输入指标X "></el-input>
        </div>
        <div class="inputElement">
          <el-input placeholder="请输入指标X "></el-input>
        </div>
        <div>
          <el-button type="primary" >确认</el-button>
        </div>
        <div style="text-align: right;color: white;">
        </div>
      </el-form>
    </div>
  </div>
</template>

<script>
import Footer from "../components/Home/Footer.vue"
export default {
    name: "Query",
    props: {

    },
    data() {
        return {
          activeURL: 1,
        };
    },
    watch: {

    },
    methods: {

    },
    components: {

    },
};
</script>

<style scoped>
.con-background {
  position: fixed;
  left: 0;
  right: 0;
  top: 0;
  bottom: 0;
  background: url("../assets/login_background.jpg") no-repeat;
  background-size: cover;
}
.text-box {
  position: fixed;
  left: 10%;
  top: 45%;
  color: #fff;
  display: block;
  text-align: left;
}
.text-box h3 {
  font-size: 54px;
  letter-spacing: 0;
  font-weight: 700;
  color: #fff;
}
.text-box p {
  font-size: 32px;
  letter-spacing: 3.81px;
  font-weight: 300;
}
.logo-box {
  position: fixed;
  left: 6%;
  top: 9%;
  color: #fff;
  text-align: left;
  display: flex;
  flex-direction: row;
  justify-content: center;
  align-items: center;
}
.logo-box span {
  margin-left: 10px;
  font-size: 30px;
  font-family: Times;
}
.logo-box img {
  height: 50px;
  width: 50px;
}
.footer-box {
  position: fixed;
  opacity: 0.78;
  left: 6%;
  bottom: 8%;
  font-size: 14px;
  color: #fff;
}
.footer-box a {
  color: #fff;
  text-decoration: none;
}
.footer-box a:hover {
  color: rgb(75, 105, 254);
  opacity: 1;
}
.footer-about .footer-help {
  opacity: 0.8;
  text-decoration: none;
  color: #fff;
  cursor: pointer;
}
.footer-line {
  display: inline-block;
  width: 2px;
  height: 12px;
  filter: alpha(opacity=78);
  opacity: 0.78;
  margin: 0 12px 0 13px;
  background: #fff;
  position: relative;
  top: 1px;
}
.footer-copyright {
  opacity: 0.54;
  font-size: 12px;
  color: #fff;
  display: inline-block;
  padding-left: 30px;
}
.right-container {
  top: 50%;
  margin-top: -215px;
  position: absolute;
  display: flex;
  flex-direction: column;
  justify-content: space-around;
  right: 170px;
  width: 420px;
  height: 350px; /* login的高度 */
  padding: 28px 35px 20px 35px;
  background: rgba(255, 255, 255, 0.9);
  border-radius: 12px;
  overflow: hidden;
  transition: all 0.5s;
}
.right-footer-box {
  text-align: center;
}
.right-footer-box a {
  color: rgb(100, 100, 100);
  text-decoration: none;
  cursor: pointer; /* 光标变小手 */
}
.right-footer-box a:hover {
  color: rgb(75, 105, 254);
  opacity: 1;
}
.loginPart{
  position:absolute;
  /*定位方式绝对定位absolute*/
  top:50%;
  left:50%;
  /*顶和高同时设置50%实现的是同时水平垂直居中效果*/
  transform:translate(-50%,-50%);
  /*实现块元素百分比下居中*/
  width:650px;
  height:450px;
  padding:50px;
  background: rgba(226, 236, 236, 0.5);
  /*背景颜色为黑色，透明度为0.8*/
  box-sizing:border-box;
  /*box-sizing设置盒子模型的解析模式为怪异盒模型，
  将border和padding划归到width范围内*/
  box-shadow: 0px 15px 25px rgba(0,0,0,.5);
  /*边框阴影  水平阴影0 垂直阴影15px 模糊25px 颜色黑色透明度0.5*/
  border-radius:15px;
  /*边框圆角，四个角均为15px*/
}
.loginPart h2{
  margin:0 0 30px;
  padding:0;
  color: #1f4be8;
  text-align:center;
  /*文字居中*/
}
.loginPart h3{
  margin:0 0 30px;
  padding:0;
  color: #1f4be8;
  text-align:center;
  /*文字居中*/
}

/*.loginPart.inputElement{*/
/*  height: 45px;*/
/*  width: 100px;*/
/*  left: 3000px;*/
/*  bottom:15px;*/

/*}*/
/*输入框style*/
.loginPart .inputElement .el-input{
  /*position:absolute;*/
  /*height: 40px;*/
  left: 30px;
  /*right: 3000px;*/
  bottom:5px;
  /*float:right;*/
  width: 70%;
  /*padding:10px 0;*/
  /*font-size:16px;*/
  /*color:#fff;*/
  /*letter-spacing: 1px;*/
  /*!*字符间的间距1px*!*/
  /*margin-bottom: 30px;*/
  /*border:none;*/
  /*border-bottom: 1px solid #fff;*/
  /*outline:none;*/
  /*!*outline用于绘制元素周围的线*/
  /*outline：none在这里用途是将输入框的边框的线条使其消失*!*/
  /*background: transparent;*/
  /*背景颜色为透明*/
}

.login{
  width:100%;
  height:100%;
}
.el-button{
  position:absolute;
  height: 45px;
  width: 120px;
  /*left:600px;*/
  right:155px;
  bottom:15px;
  /*border-radius:5px;*/
}
.el-form-item {
  width: 50%;
  display:inline-block;
}
.home-background {
  position: fixed;
  left: 0;
  right: 0;
  top: 0;
  bottom: 0;
  background: url("../assets/home_background.jpg") no-repeat;
  background-size: cover;
  z-index: -1;
}
.el-header .logo {
  height: 35px;
}
.el-header .logo img {
  height: 100%;
}
.el-header .menu {
  width: 30%;
  height: 35px;
  left: 35%;
  position: absolute;
  display: flex;
  justify-content: space-between;
  line-height: 35px; /* 垂直居中 */
}
.el-header .menu-item {
  width: 32px;
}
.el-header .menu-item .menu-underline {
  width: 10px;
  height: 5px;
  background-color: #ffffffcc;
  border-radius: 5px;
  margin-left: calc(50% - 5px); /* 注意空格，否则无效！ */
  transform: scaleX(0);
  transition: transform 0.3s ease;
}
.el-header .menu-underline.activedPage {
  transform: scaleX(1);
}
.el-header .menu-item a {
  color: #ffffffcc;
  text-decoration: none;
}
.el-header .menu-item a:hover {
  color: #fff;
}

.person {
  display: flex;
  justify-content: right;
}
.person .person-img {
  width: 30px;
  height: 30px;
  border-radius: 50%;
  /* border: 4px solid rgba(255, 255, 255, 0.3); */
  overflow: hidden;
}
.person .person-img img {
  width: 100%;
  height: 100%;
  border-radius: 50%;
  object-fit: cover;
}
.person .settings {
  padding: 0;
}
.login_container {
  background-image: linear-gradient(-180deg, #1a1454 0%, #0e81a5 100%);
  /*background-image: url("../images/bg_login.png");*/
  background-repeat: no-repeat;
  background-size: cover;
  height: 100%;
}
.login_box {
  width: 390px;
  height: 350px;
  /* background-color: #fff; */
  background-color: #2e527bb3;
  border-radius: 5px;

  position: absolute;
  left: 50%;
  top: 40%;
  transform: translate(-50%, -50%);
}
.el-form {
  padding: 64px;
  position: absolute;
  bottom: 0;
  width: 100%;
  box-sizing: border-box;
}

.code {
  width: 45%;
}
.el-footer {
  width: 100%;
  display: flex;
  justify-content: center;
  position: absolute;
  bottom: 0;
  padding-bottom: 12px;
  height: inherit;
}
</style>

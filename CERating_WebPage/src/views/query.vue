<template>
  <div class="home">
    <el-container>
      <!-- 背景图片 -->
      <div class="home-background"></div>
      <!-- 头部导航 -->
      <el-header>
        <!-- LOGO -->
        <div class="logo">
          <a href="/" @click="activeURL = 0"
          ><img src="../assets/logo.png" alt="logo"
          /></a>
        </div>

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
      <!-- 主体部分 -->
      <el-main>
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
        <vue-particles
            color="#fff"
            :particleOpacity="0.7"
            :particlesNumber="60"
            shapeType="circle"
            :particleSize="4"
            linesColor="#fff"
            :linesWidth="1"
            :lineLinked="true"
            :lineOpacity="0.4"
            :linesDistance="150"
            :moveSpeed="2"
            :hoverEffect="true"
            hoverMode="grab"
            :clickEffect="true"
            clickMode="push"
            class="lizi"
            style="height:80%"
        >
        </vue-particles>




        <!-- 时间 -->
        <div class="time-box">

        </div>
        <!-- 主题内容 -->
        <router-view />
      </el-main>
      <!-- 底部信息 -->
      <el-footer>
        <Footer></Footer>
      </el-footer>
    </el-container>
  </div>
</template>

<script>
import Footer from "../components/Home/Footer.vue"

export default {
  name: "Home",
  components: { Footer },
  data() {
    return {
      activeURL: 1,
    };

  },
  data1(){
    return{
      kindList:[{name:"小可爱",id:1},{name:"小仙女",id:2},{name:"小宝龙",id:3}]
    }
  },
};

</script>

<style scoped>
.home {
  display: flex;
  justify-content: center;
}
.main .login-box .el-form-item {
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
.el-header {
 width: 100%;
 height: 50px;
 padding: 15px 20px 0 20px;
 display: flex;
 justify-content: space-between;
 text-align: center;
 /* opacity: 0; */
 transition: all 0.5s ease;
}
/*.el-header:hover {*/
/*  padding-top: 15px;*/
/*  opacity: 1;*/
/*}*/
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
.el-main .el-button {
  color: #ffccee;
  left: 50%;
  right: 30%;
  top: 40%;
  bottom: 60%;
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
.el-button {
  width: 100%;
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

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
          <div class="menu-item" :key="0">
            <a href="/" @click="activeURL = 0">Logo</a>
            <div
                class="menu-underline"
                :class="{ activedPage: activeURL == 0 }"
            ></div>
          </div>
          <div class="menu-item" :key="1">
            <a href="/" @click="activeURL = 0">首页</a>
            <div
                class="menu-underline"
                :class="{ activedPage: activeURL == 0 }"
            ></div>
          </div>
          <div class="menu-item" :key="2">
            <a href="/" @click="activeURL = 0">公告</a>
            <div
                class="menu-underline"
                :class="{ activedPage: activeURL == 0 }"
            ></div>
          </div>
          <div class="menu-item" :key="3">
            <a href="/" @click="activeURL = 0">帮助</a>
            <div
                class="menu-underline"
                :class="{ activedPage: activeURL == 0 }"
            ></div>
          </div>
          <div class="menu-item" :key="3">
            <a href="/" @click="activeURL = 0">查询</a>
            <div
                class="menu-underline"
                :class="{ activedPage: activeURL == 0 }"
            ></div>
          </div>
        </div>
        <!-- 个人 -->
        <div class="person">
          <div class="person-img">
            <img src="../assets/person.png" alt="" />
          </div>
          <!-- TODO 点击头像下拉框 -->
        </div>
      </el-header>
      <!-- 主体部分 -->
      <el-main>
        <div class="login_box">
          <!-- 登录表单区域 -->
          <el-form size="mini">
            <!-- 用户名 -->
            <el-form-item>
              <a style="color:whitesmoke">选择企业</a>
              <select v-model="goodsId" style="width:200px;height: 30px;margin-top: 5px;margin-bottom: 5px;margin-left: 10px">
                <option value="">选择企业</option>
<!--                <option v-for="item in kindList" v-bind:value="item.id" v-text="item.name" ></option>-->
              </select>
            </el-form-item>
            <!-- 密码 -->
            <el-form-item>
              <a style="color:whitesmoke">选择年份</a>
              <select v-model="goodsId" style="width:200px;height: 30px;margin-top: 5px;margin-bottom: 5px;margin-left: 10px">
                <option value="">选择年份</option>

              </select>
            </el-form-item>
            <!-- 登录按钮 -->
            <el-form-item>
              <el-button type="primary">查询</el-button>
            </el-form-item>
          </el-form>
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
      activeURL: 0,
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
.el-header {
  width: 100%;
  height: 50px;
  padding: 0 20px 0 20px;
  display: flex;
  justify-content: space-between;
  text-align: center;
  opacity: 0;
  transition: all 0.5s ease;
}
.el-header:hover {
  padding-top: 15px;
  opacity: 1;
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

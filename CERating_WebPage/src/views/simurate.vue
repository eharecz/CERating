<template>
  <div class="home">
    <el-container>
      <NavigationBar/>
      <!-- 主体部分 -->
      <el-main style="overflow-y: hidden;">
        <div class="login" v-if="true">
          <div class="loginPart">
            <h2>模拟评级</h2>
            <h3>碳排放评级详情查询</h3>
<!--            <el-form>
              <a style="color:whitesmoke">选择企业</a>
              <select v-model="goodsId" style="width:200px;height: 30px;margin-top: 5px;margin-bottom: 5px;margin-left: 10px">
                <option value="">选择企业</option>
                &lt;!&ndash;                <option v-for="item in kindList" v-bind:value="item.id" v-text="item.name" ></option>&ndash;&gt;
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
            </el-form>-->

            <el-form :model="ruleForm" :rules="rules" ref="ruleForm" :label-position="'top'" label-width="100px" class="demo-ruleForm" style="width: 100%;">
              <el-form-item label="选择企业" prop="region">
                <el-select v-model="ruleForm.goodsName" placeholder="请选择" style="width: 100%;">
                  <el-option v-for="item in result.enterprise" :key="item" :value="item">{{item}}</el-option>
                  <!-- <el-option v-for="(item, index) in kindList" :label="item.name" :value="item.id" :key="index"></el-option> -->
                </el-select>
              </el-form-item>
              <el-form-item label="是否采取节能减排措施" prop="name1">
                <el-input v-model="ruleForm.name1" placeholder="请输入指标X"></el-input>
              </el-form-item>
              <el-form-item label="公开信息中对环保政策的关注程度" prop="name2">
                <el-input v-model="ruleForm.name2" placeholder="请输入指标X"></el-input>
              </el-form-item>
              <el-form-item label="二氧化碳排放（吨）" prop="name3">
                <el-input v-model="ruleForm.name3" placeholder="请输入指标X"></el-input>
              </el-form-item>
              <el-form-item label="废弃物排放（吨）" prop="name4">
                <el-input v-model="ruleForm.name4" placeholder="请输入指标X"></el-input>
              </el-form-item>
              <el-form-item label="排废水量（吨）" prop="name5">
                <el-input v-model="ruleForm.name5" placeholder="请输入指标X"></el-input>
              </el-form-item>
              <el-form-item label="COD排放（吨）" prop="name6">
                <el-input v-model="ruleForm.name6" placeholder="请输入指标X"></el-input>
              </el-form-item>
              <el-form-item label="综合能耗（吨标煤）" prop="name7">
                <el-input v-model="ruleForm.name7" placeholder="请输入指标X"></el-input>
              </el-form-item>
              <el-form-item label="研发投入(亿元)" prop="name8">
                <el-input v-model="ruleForm.name8" placeholder="请输入指标X"></el-input>
              </el-form-item>
              <el-form-item label="环保投入（万元）" prop="name9">
                <el-input v-model="ruleForm.name9" placeholder="请输入指标X"></el-input>
              </el-form-item>
              <el-form-item>
                <el-button type="primary" @click="submitForm('ruleForm')">立即提交</el-button>
              </el-form-item>
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
        <router-view/>
      </el-main>
      <!-- 底部信息 -->
      <el-footer>
        <!-- <Footer></Footer> -->
      </el-footer>
    </el-container>
  </div>
</template>

<script>
import Global from "../components/Global.vue"
import NavigationBar from "../components/NavigationBar.vue";
import axios from "axios";

export default {
  name: "Home",
  components: {NavigationBar},
  data() {
    return {
      activeURL: 4,
      result: {},
      ruleForm: {
        goodsName: '',
      },
      rules: {
        goodsName: [
          { required: true, message: '请选择', trigger: 'change' }
        ],
      }
    }
  },
  created() {
    axios
        .post(Global.address + '/api/getEnterpriseData/')
        .then( response => {
          this.result = response
        })
        .catch(error=>{
          console.log(error);
          alert('数据获取失败,请刷新重试');
        })
  },
  methods: {
    submitForm(formName) {
      this.$refs[formName].validate((valid) => {
        if (valid) {
          // alert('submit!');
          this.$alert('是否消耗一次模拟评级机会', '', {
            confirmButtonText: '确定',
            callback: action => {
              console.log(action)
              console.log(this.ruleForm)
              // axios
              //   .post(Global.address + '/api/simurate', this.$refs[formName])
              //   .then( response => {
              //     console.log(response)
              //   })
            }
          });
        } else {
          console.log('请填写全部信息！');
          return false;
        }
      });
    },
    resetForm(formName) {
      this.$refs[formName].resetFields();
    }
  }
};

</script>

<style scoped>
.home {
  display: flex;
  justify-content: center;
}

.main .login-box .el-form-item {
  width: 50%;
  display: inline-block;
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
  margin: 20px auto 00px;
  /*position:absolute;*/
  /*定位方式绝对定位absolute*/
  /*top:50%;*/
  /*left:50%;*/
  /*顶和高同时设置50%实现的是同时水平垂直居中效果*/
  /*transform:translate(-50%,-50%);*/
  /*实现块元素百分比下居中*/
  width: 650px;
  /*height:450px;*/
  padding:30px;
  background: rgba(226, 236, 236, 0.5);
  /*背景颜色为黑色，透明度为0.8*/
  box-sizing: border-box;
  /*box-sizing设置盒子模型的解析模式为怪异盒模型，
  将border和padding划归到width范围内*/
  box-shadow: 0px 15px 25px rgba(0, 0, 0, .5);
  /*边框阴影  水平阴影0 垂直阴影15px 模糊25px 颜色黑色透明度0.5*/
  border-radius: 15px;
  /*边框圆角，四个角均为15px*/
}
.loginPart h2{
  margin:0 0 10px;
  padding:0;
  color: #1f4be8;
  text-align: center;
  /*文字居中*/
}
.loginPart h3{
  margin:0 0 10px;
  padding:0;
  color: #1f4be8;
  text-align: center;
  /*文字居中*/
}

/*.loginPart.inputElement{*/
/*  height: 45px;*/
/*  width: 100px;*/
/*  left: 3000px;*/
/*  bottom:15px;*/

/*}*/
/*输入框style*/
.loginPart .inputElement .el-input {
  /*position:absolute;*/
  /*height: 40px;*/
  left: 30px;
  /*right: 3000px;*/
  bottom: 5px;
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

.login {
  width: 100%;
  height: 100%;
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
  /*position: absolute;*/
  bottom: 0;
  width: 100%;
  box-sizing: border-box;
}

.el-button {
  /* position:absolute; */
  margin-top: 10px;
  margin-left: 300px;
  height: 45px;
  width: 120px;
  /*left:600px;*/
  /*border-radius:5px;*/
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

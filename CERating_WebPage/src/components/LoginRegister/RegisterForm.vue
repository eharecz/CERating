<template>
  <div>
    <el-form
      class="register-form"
      ref="ref-registerform"
      :model="registerForm"
      :rules="registerRules"
    >
      <h3>注册</h3>
      <el-form-item prop="businessName">
        <input type="text" v-model="registerForm.name" required />
        <div class="input-underline"></div>
        <label class="input-label">企业名称</label>
      </el-form-item>
      <el-form-item prop="businessType1">
        <div class="businessType1-box">
          <label>企业类型</label>
          <div class="dropdown">
            <input
              type="text"
              class="dropdown-textbox"
              placeholder="请选择"
              @click="dropdown_list()"
              readonly
            />
            <div class="dropdown-option">
              <div @click="dropdown_selected('工业')">工业</div>
              <div @click="dropdown_selected('农业')">农业</div>
              <div @click="dropdown_selected('商业')">商业</div>
              <div @click="dropdown_selected('旅行业')">旅行业</div>
            </div>
          </div>
        </div>
      </el-form-item>
      <el-form-item prop="type">
        <div class="businessType2-box">
          <div>
            <input
              type="radio"
              name="businessType2"
              id="type2-center"
              value="0"
              @click="radio_selected(0)"
            />
            <label for="type2-center">总公司</label>
          </div>
          <div>
            <input
              type="radio"
              name="businessType2"
              id="type2-brach"
              value="1"
              @click="radio_selected(1)"
            />
            <label for="type2-brach">分公司</label>
          </div>
          <div>
            <input
              type="radio"
              name="businessType2"
              id="type2-other"
              value="2"
              @click="radio_selected(2)"
            />
            <label for="type2-other">其他</label>
          </div>
        </div>
      </el-form-item>
      <el-form-item prop="email">
        <input type="text" v-model="registerForm.email" required />
        <div class="input-underline"></div>
        <label class="input-label">邮箱</label>
      </el-form-item>
      <el-form-item prop="password">
        <input type="password" v-model="registerForm.password" required />
        <div class="input-underline"></div>
        <label class="input-label">密码</label>
      </el-form-item>
      <el-form-item prop="securityCode" inline="true" class="security-code-box">
        <input
          type="text"
          autocomplete="false"
          v-model="registerForm.captcha"
          style="width: 58%"
          required
        />
        <div class="input-underline"></div>
        <label class="input-label">验证码</label>
        <el-button
          class="security-code-button"
          type="primary"
          @click="getSecurityCode"
          >获取验证码</el-button
        >
      </el-form-item>
      <el-form-item>
        <el-button type="primary" @click="submitRegister">注册</el-button>
      </el-form-item>
    </el-form>
  </div>
</template>

<script>
import { postRequest } from "@/utils/api";
import qs from 'qs'

export default {
  name: "RegisterForm",
  data() {
    return {
      securityCodeUrl: "",
      registerForm: {
        name: "",
        type: "",
        relation: "",
        email: "",
        password: "",
        captcha: "",
      },
    };
  },
  methods: {
    getSecurityCode() {
      postRequest("http://127.0.0.1:8000/email_request/", qs.stringify(this.registerForm)).then(response => {
        console.log(this.registerForm)
        console.log(response)
      });
    },
    submitRegister() {
      postRequest("http://127.0.0.1:8000/enterprise_register/", qs.stringify(this.registerForm)).then(response => {
        console.log("form")
        console.log(this.registerForm)
        console.log(response)
        if(response.code === 1){
          alert("邮箱已存在")
        }else if(response.code === 2){
          alert("验证码错误")
        }else if(response.code === 0){
          this.$router.replace('/login');
        }
      });
    },
    dropdown_selected(selectName) {
      document.querySelector('.dropdown-textbox').value = selectName;
      document.querySelector('.dropdown').classList.toggle('active');
      this.registerForm.type = selectName;
    },
    dropdown_list() {
      document.querySelector('.dropdown').classList.toggle('active');
    },
    radio_selected(value) {
      this.registerForm.relation = value;
    }
  },
};
</script>

<style scoped>
.register-form {
  margin: 0 0.6rem;
}
.register-form h3 {
  text-align: center;
  font-size: 2.3rem;
  padding-bottom: 15px;
  width: 100%;
  /* 大写 */
  text-transform: uppercase;
}
.register-form input {
  font-size: 1rem;
  background: rgba(39, 39, 41, 0.025);
  /* background: rgba(255, 255, 255, 0); */
  border-radius: 0.5rem;
  padding-left: 1rem;
  /* border: 1px solid transparent; */
  border: none;
  height: 46px;
  width: 100%;
  line-height: 150%;
  color: #25262b;
}
.register-form input:focus {
  /* border: rgb(180, 193, 255) solid 1px; */
  outline: none;
  background: rgba(255, 255, 255, 0.04);
}
.register-form label {
  font-size: 1rem;
  position: absolute;
  bottom: 10px;
  left: 1rem;
  color: rgba(65, 65, 65, 0.6);
  pointer-events: none;
  transition: all 0.3s ease;
}
.businessType1-box {
  position: relative;
  display: flex;
  justify-content: space-around;
  width: 100%;
  height: 35px;
  line-height: 30px;
}
.businessType1-box label {
  position: relative;
  left: 0;
  bottom: 0;
  top: 0.4rem;
}
.businessType1-box input{
  text-align: center;
  padding: 0 0.5rem;
  width: 120%;
  margin-left: -30px;
}
.businessType1-box .dropdown::before {
  content: '';
  position: absolute;
  right: 2.2rem;
  top: 1rem;
  z-index: 100;
  width: 8px;
  height: 8px;
  border: 1.2px solid rgba(65, 65, 65, 0.7);
  border-top: 0;
  border-right: 0;
  transform: rotate(-45deg);
  transition: 0.4s;
  pointer-events: none;
}
.businessType1-box .active::before{
  top: 1.2rem;
  transform: rotate(-225deg);
}
.businessType1-box .dropdown-option {
  position: absolute;
  top: 50px;
  width: 58%;
  right: 18px;
  height: 120px;
  background: rgba(248, 248, 248, 0.877);
  box-shadow: 0 10px 10px rgba(180, 180, 180, 0.3);
  border-radius: 5px;
  overflow-y: scroll;
  z-index: 100;
  display: none;
}
.businessType1-box .active .dropdown-option {
  display: flex;
  flex-direction: column;
}
/* 隐藏滚动条 */
.businessType1-box .active .dropdown-option::-webkit-scrollbar{
  display: none;
}
.businessType1-box .dropdown-option div{
  padding: 0.3rem;
  text-align: center;
  cursor: pointer;
  color: rgba(65, 65, 65, 0.7);
}
.businessType1-box .dropdown-option div:hover{
  background: rgba(133, 171, 247, 0.65);
}
.businessType2-box {
  display: flex;
  width: 100%;
  height: 30px;
  flex-direction: row;
  justify-content: space-around;
  align-content: center;
  align-items: center;
}
.businessType2-box label {
  position: relative;
  pointer-events: fill;
  bottom: 0;
  font-size: 1rem;
  margin-left: 0;
  bottom: 2px;
}
.businessType2-box input {
  height: 1rem;
  width: 1rem;
}
.businessType2-box span {
  font-size: 1rem;
  line-height: 1rem;
}
/* 关联input与label  input的focus触发会改变label的属性  */
.register-form input:focus ~ .input-label,
.register-form input:valid ~ .input-label {
  /* :valid选择器是如果合法触发，所以输入框记得加required属性 */
  transform: translateY(-1.8rem) translateX(-0.5rem);
  font-size: 0.85rem;
  letter-spacing: 0.05rem;
  /* color: rgba(75, 105, 254, 0.7); */
}
.register-form .input-underline {
  position: absolute;
  bottom: 0px;
  height: 1.4px;
  width: 95%;
  left: 2.5%;
}
.register-form .security-code-box .input-underline {
  width: 55%;
}
/* 不理解这里加before选择器是为了什么 */
.register-form .input-underline:before {
  position: absolute;
  content: "";
  height: 100%;
  width: 100%;
  /* background: rgba(75, 105, 254, 0.7); */
  background: rgba(129, 129, 129, 0.3);
  transform: scaleX(0);
  transition: transform 0.3s ease;
}
.register-form input:focus ~ .input-underline:before {
  transform: scaleX(1);
}
.register-form button {
  width: 100%;
  background-image: linear-gradient(
    130deg,
    rgb(75, 105, 254) 0%,
    rgba(150, 152, 253, 0.75) 100%
  );
  border-radius: 10px;
  backdrop-filter: blur(24px);
  border: none;
  cursor: pointer;
  height: 48px;
  font-size: 16px;
}
.register-form .security-code-box >>> div {
  display: flex;
  justify-content: space-between;
}
.register-form .security-code-button {
  background-image: linear-gradient(
    130deg,
    #93a8f1b6 0%,
    rgba(152, 171, 255, 0.6) 100%
  );
  font-size: 0.9rem;
  width: 35%;
}
</style>

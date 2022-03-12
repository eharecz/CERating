<template>
  <div>
    <div class="mb-background" @click="closeCom"></div>
    <div class="message-box">
      <div class="mb-title">
        <div><img src="../assets/topimg-earth.jpg" alt="leaf" /></div>
        <div class="mb-title-text">
          <h3>{{ this.fTitle }}</h3>
        </div>
      </div>
      <div class="mb-text">
        <label>{{ this.fMessage }}</label>
      </div>
      <div class="mb-button">
        <el-button type="primary" @click="goFun">{{ this.fGoName }}</el-button>
      </div>
      <div class="mb-footer"></div>
    </div>
  </div>
</template>

<script>
export default {
  name: "LoginForm",
  props: ["fTitle", "fMessage", "fGoURL", "fGoName"],
  data() {
    return {
      show: true,
    };
  },
  
  methods: {

    goFun() {
      this.$router.push(this.fGoURL);
    },
    closeCom() {
      this.show=false
      this.$emit("changeMB", this.show);
    }
  },
};
</script>

<style scoped>
.mb-background {
  position: fixed;
  left: 0;
  right: 0;
  top: 0;
  bottom: 0;
  background: rgba(204,204,204, 0.5);
  background-size: cover;
  z-index: 0;
}
.message-box {
  position: absolute;
  left: calc(50% - 250px);
  width: 500px;
  border-radius: 10px;
  display: flex;
  flex-direction: column;
  justify-content: space-between;
  /* height: 350px; login的高度 */
  background: rgba(255, 255, 255, 0.9);
  border-radius: 12px;
  box-shadow: rgb(0 0 0 / 20%) 0 0 10px;
  overflow: hidden;
  transition: all 0.5s;
}
.mb-title {
  display: flex;
  justify-content: left;
  width: 100%;
  height: 50px;
  padding: 15px 0 0 10px;
  background-image: linear-gradient(
    130deg,
    rgb(255, 204, 102) 0%,
    rgb(250, 206, 129) 100%
  );
}
.mb-title img {
  height: 35px;
}
.mb-title h3 {
  padding-left: 10px;
  text-align: center;
  font-size: 1.3rem;
  color: rgb(42, 177, 170);
  width: 100%;
  /* 大写 */
  text-transform: uppercase;
}
.message-box .mb-text {
  margin: 40px;
}
.message-box label {
  font-size: 1.2rem;
  font-weight: bold;
  transition: all 0.3s ease;
}
.mb-button {
  display: flex;
  justify-content: right;
}
.message-box button {
  margin: 20px;
  width: 40%;
  background-image: linear-gradient(
    130deg,
    rgb(252, 178, 47) 0%,
    rgb(250, 206, 129) 100%
  );
  border-radius: 10px;
  backdrop-filter: blur(24px);
  border: none;
  cursor: pointer;
  height: 48px;
  font-size: 16px;
}
.mb-footer {
  width: 100%;
  height: 20px;
  background-image: linear-gradient(
    130deg,
    rgb(255, 204, 102) 0%,
    rgb(250, 206, 129) 100%
  );
}
</style>

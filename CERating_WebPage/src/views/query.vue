<template>
  <div>
    <NavigationBar />
    查询
    <button @click="mbfun">message box</button>
    <MessageBox
      v-show="this.mbShow"
      :fTitle="'温馨提示'"
      :fMessage="'是否已经了解上述内容？如有疑问请先查看模拟评级导航'"
      :fGoName="'进入模拟评级'"
      :fGoURL="'/'"
      @changeMB="changeMBVal"
    />
  </div>
</template>

<script>
import NavigationBar from "../components/NavigationBar.vue";
import MessageBox from "../components/MessageBox.vue";

export default {
  name: "Query",
  props: {},
  components: {
    NavigationBar,
    MessageBox,
  },
  data() {
    return {
      mbShow : true,
    };
  },
  methods: {
    mbfun() {
      this.mbShow=!this.mbShow;
    },
    changeMBVal(val){
      this.mbShow=val
    }
  },
};
</script>

<style scoped></style>

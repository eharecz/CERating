<template>
  <div>
    <NavigationBar />
    查询
    <MessageBox :fTitle="'温馨提示'" :fMessage="'是否已经了解上述内容？如有疑问请先查看模拟评级导航'" :fGoName="'进入模拟评级'" :fGoURL="'/'"/>
  </div>
</template>

<script>
import NavigationBar from "../components/NavigationBar.vue";
import MessageBox from "../components/MessageBox.vue"


export default {
  name: "Query",
  props: {},
  data() {
    return {};
  },
  watch: {},
  methods: {},
  components: {
    NavigationBar,
    MessageBox
  },
};
</script>

<style scoped></style>

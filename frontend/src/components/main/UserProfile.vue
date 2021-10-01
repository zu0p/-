<template>
  <v-card>
    <v-card-title>
      <span class="text-h5">Create New Diary</span>
    </v-card-title>
    <v-card-text>
      gdgd
    </v-card-text>
    <v-card-actions>
      <v-spacer></v-spacer>
      <v-btn color="blue darken-1" text @click="closeClick">
        Close
      </v-btn>
    </v-card-actions>
  </v-card>
</template>

<script>
export default {
  data() {
    return {
      userInfo: {
        userEmail: "",
        userId: "",
        userImage: "",
        userName: "",
        userNick: "",
        userPhone: "",
      },
    };
  },
  mounted: {},
  methods: {
    closeClick() {
      this.$emit("closeUserInfoDialog");
    },
  },
};
</script>

<style></style>

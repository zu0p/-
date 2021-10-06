<template>
  <v-card>
    <v-card-title>
      <span v-if="isAdd" class="text-h5">Create New Diary</span>
      <span v-else class="text-h5">Update Diary</span>
    </v-card-title>
    <v-card-text>
      <v-container>
        <v-row>
          <v-col>
            <v-text-field label="Title*" required v-model="diary.diaryName"></v-text-field>
          </v-col>
        </v-row>

        <v-row>
          <v-col>
            <v-text-field
              :disabled="!isAdd"
              label="Description*"
              hint="간단한 설명을 적어보세요"
              persistent-hint
              required
              v-model="diary.diaryDesc"
            ></v-text-field>
          </v-col>
        </v-row>
        <v-row>
          <v-col>
            <v-checkbox :disabled="!isAdd" v-model="diary.diaryShare" label="Share Diary"></v-checkbox>
          </v-col>
          <v-col>
            <v-file-input
              :disabled="!isAdd"
              accept="image/*"
              label="Diary Cover Image*(세로 사진을 사용해주세요)"
              v-model="diary.diaryImage"
            ></v-file-input>
          </v-col>
        </v-row>
      </v-container>
      <small>*indicates required field</small>
    </v-card-text>
    <v-card-actions>
      <v-spacer></v-spacer>
      <v-btn color="blue darken-1" text @click="closeClick">
        Close
      </v-btn>
      <v-btn color="blue darken-1" text @click="createClick">
        {{ isAdd ? "Create" : "Update" }}
      </v-btn>
    </v-card-actions>
  </v-card>
</template>

<script>
import { mapActions } from "vuex";
const diaryStore = "diaryStore";

export default {
  props: ["isAdd", "id"],
  data() {
    return {
      diary: {
        diaryName: "",
        diaryImage: {},
        diaryDesc: "",
        diaryShare: false,
      },
    };
  },
  updated() {
    // console.log(this.diary.diaryImage)
  },
  mounted() {
    // console.log(this.isAdd)
    if (!this.isAdd) {
      // 수정일 때
      // 기존 정보 불러와서 값 채우기
      // console.log(this.id)
      this.requestDiaryInfo(this.id).then((res) => {
        console.log(res);
        this.diary.diaryName = res.data.diaryName;
        this.diary.diaryDesc = res.data.diaryDesc;
        this.diary.diaryImage = res.data.diaryImage;
        this.diary.diaryShare = res.data.diaryShare;
      });
    }
  },
  methods: {
    ...mapActions(diaryStore, ["createDiary", "addDiary", "requestUpdateDiary", "updateDiary", "requestDiaryInfo"]),
    closeClick() {
      this.$emit("closeAddDialog");
    },
    createClick() {
      // console.log(this.diary)

      if (this.isAdd) {
        //생성
        //actions 불러서 새로 생성
        const form = new FormData();
        form.append("diaryName", this.diary.diaryName);
        form.append("diaryImage", this.diary.diaryImage);
        form.append("diaryDesc", this.diary.diaryDesc);
        form.append("diaryShare", this.diary.diaryShare);

        this.createDiary(form).then((res) => {
          // console.log(res)
          this.addDiary(res.data);
          this.diary.diaryName = "";
          this.diary.diaryImage = {};
          this.diary.diaryDesc = "";
          this.diary.diaryShare = false;

          this.$emit("closeAddDialog");
        });
      } else {
        //update
        console.log("update");
        const param = {
          diaryId: this.id,
          modifyName: this.diary.diaryName,
        };
        this.requestUpdateDiary(param).then((res) => {
          // console.log(res)
          this.updateDiary(param);
          this.$emit("closeAddDialog");
        });
      }
    },
  },
};
</script>

<style></style>

<template>
  <div id="cal">
    <!-- カレンダーヘッダ -->
    <div id="cal-header">
      <span
        class="header-arrow"
        v-on:touchstart.prevent="setLastMonth"
        v-on:mousedown.prevent="setLastMonth"
      >＜</span>
      <span id="month" class="selected-month">
        <p>{{year}}-{{month}}</p>
      </span>
      <span
        class="header-arrow"
        v-on:touchstart.prevent="setNextMonth"
        v-on:mousedown.prevent="setNextMonth"
      >＞</span>
    </div>

    <!-- カレンダーメイン -->
    <table id="cal-main">
      <!-- 曜日を表示させる（テーブルヘッダ） -->
      <thead>
        <th v-for="(dayname,index) in weekdays" :key="index">{{dayname}}</th>
      </thead>
      <!-- 日付を表示させる（テーブルボディ） -->
      <tbody>
        <tr v-for="(weekData,index) in calData" :key="index">
          <td
            class="cal-day"
            v-for="(dayNum,index) in weekData"
            :key="index"
            v-on:touchstart.prevent="dateClick(dayNum)"
            v-on:mousedown.prevent="dateClick(dayNum)"
            :class="{'cal-today': isToday(dayNum), active: day === dayNum}"
          >
            <span v-if="isToday(dayNum)">{{dayNum}}</span>
            <span v-else>{{dayNum}}</span>
          </td>
        </tr>
      </tbody>
    </table>
  </div>
</template>

<script>
export default {
  data() {
    return {
      weekdays: ["日", "月", "火", "水", "木", "金", "土"],
      year: 2000,
      month: 1,
      day: -1,
      today: ""
    };
  },
  mounted() {
    var date = new Date();
    var y = date.getFullYear();
    var m = ("0" + (date.getMonth() + 1)).slice(-2);
    var d = ("0" + date.getDate()).slice(-2);
    // yearとmonthを設定
    this.year = y;
    this.month = Number(m);
    // 今日の日付を設定
    this.today = y + "-" + m + "-" + d;
  },
  methods: {
    /**
     * カレンダー日付クリック時の処理
     */
    dateClick: function(dayNum) {
      if (dayNum !== "") {
        this.day = dayNum;
      }
    },
    /**
     * 今日かどうかの判定
     * 年、月は現在選択しているページ
     * 日は引数
     */
    isToday: function(day) {
      var date = this.year + "-" + ("0" + this.month).slice(-2) + "-" + day;
      if (this.today === date) {
        return true;
      }
      return false;
    },
    /**
     * 先月のカレンダーを取得
     */
    setLastMonth: function() {
      if (this.month === 1) {
        this.year--;
        this.month = 12;
      } else {
        this.month--;
      }
      this.day = -1;
    },
    /**
     * 翌月のカレンダーを取得
     */
    setNextMonth: function() {
      if (this.month === 12) {
        this.year++;
        this.month = 1;
      } else {
        this.month++;
      }
      this.day = -1;
    }
  },
  computed: {
    calData: function() {
      console.log(this.year + "-" + this.month + "のデータ作成");
      var calData = [];
      // 初日の曜日を取得
      var firstWeekDay = new Date(this.year, this.month - 1, 1).getDay();
      // 月の日数
      var lastDay = new Date(this.year, this.month, 0).getDate();
      // 日数カウント用
      var dayNum = 1;
      // 週ごとのデータを作成して、calDateにpush
      while (dayNum <= lastDay) {
        var weekData = [];
        // 日曜～土曜の日付データを配列で作成
        for (var i = 0; i <= 6; i++) {
          if (calData.length === 0 && i < firstWeekDay) {
            // 初週の1日以前の曜日は空文字
            weekData[i] = "";
          } else if (lastDay < dayNum) {
            // 最終日以降の曜日は空文字
            weekData[i] = "";
          } else {
            // 通常の日付入力
            weekData[i] = dayNum;
            dayNum++;
          }
        }
        calData.push(weekData);
      }
      return calData;
    }
  }
};
</script>

<style scoped>
/*---------------------------------------
ヘッダのcss
---------------------------------------*/
#cal-header {
  font-size: 18px;
  text-align: center;
}
#cal-header span {
  padding: 15px 20px;
  color: #375a7f;
  display: inline-block;
}
#cal-header p {
  font-size: 24px;
}
/*---------------------------------------
カレンダーのcss
---------------------------------------*/
#cal-main {
  font-size: 20px;
  table-layout: fixed;
  margin: auto;
  margin-bottom: 1rem;
  color: #212529;
}
#cal-main th {
  padding: 0;
  text-align: center;
  vertical-align: middle;
  font-weight: normal;
  border: 1px solid #ddd;
  color: #999;
}
#cal-main td {
  padding: 8px;
  vertical-align: middle;
  border: 1px solid #ddd;
  border-top: 1px solid #ddd;
}
.cal-today {
  background-color: #fcf8e3;
}
.cal-day.active {
  background-color: #375a7f;
}

@media screen and (max-width: 959px){
  #cal-main {
    line-height: 60px;
    width: 100%;
  }
}

@media screen and (min-width: 960px){
  #cal-main {
    line-height: 70px;
    width: 70%;
  }
}

</style>
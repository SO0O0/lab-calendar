<template>
  <div class="home">
    <Calendar />
  </div>
</template>

<script>
// @ is an alias to /src
import Calendar from '@/components/LabCalendar.vue'
export default {
  name: 'LabCalendar',
  components: {
    Calendar
  }
}
</script>


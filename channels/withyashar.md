<div dir="rtl" align="right">

<style>
.tg-channel-box {
  max-width: 800px;
  margin: 0 auto;
  padding: 16px;
  font-family: system-ui, -apple-system, 'Segoe UI', 'Vazirmatn', Tahoma, sans-serif;
  background: #fafafa;
  border-radius: 20px;
  line-height: 1.7;
}

/* حالت دارک برای کسانی که تم دارک دارن */
@media (prefers-color-scheme: dark) {
  .tg-channel-box {
    background: #1a1a2e;
    color: #eee;
  }
  .tg-post {
    background: #16213e;
    border-color: #0f3460;
  }
  .tg-post-header {
    background: #0f3460;
  }
  .tg-footer {
    color: #aaa;
  }
  .tg-text a {
    color: #7eb6ff;
  }
}

/* کارت پست */
.tg-post {
  background: white;
  border-radius: 20px;
  padding: 18px 22px;
  margin: 20px 0;
  box-shadow: 0 2px 8px rgba(0,0,0,0.08);
  border: 1px solid #e5e7eb;
  transition: box-shadow 0.2s;
}
.tg-post:hover {
  box-shadow: 0 8px 20px rgba(0,0,0,0.1);
}
.tg-post-header {
  background: #f3f4f6;
  margin: -18px -22px 16px -22px;
  padding: 10px 22px;
  border-radius: 20px 20px 0 0;
  font-size: 13px;
  color: #4b5563;
  border-bottom: 1px solid #e5e7eb;
}

/* نقل قول / فوروارد */
.tg-forward {
  background: #eef2ff;
  border-right: 4px solid #3b82f6;
  padding: 8px 14px;
  border-radius: 12px;
  margin: 12px 0;
  font-size: 13px;
  color: #1e40af;
}

/* متن */
.tg-text {
  font-size: 16px;
  margin: 14px 0;
}
.tg-text a {
  color: #2563eb;
  text-decoration: none;
}
.tg-text a:hover {
  text-decoration: underline;
}

/* تصاویر */
.tg-photo {
  margin: 12px 0;
  text-align: center;
}
.tg-photo img {
  max-width: 100%;
  border-radius: 16px;
  box-shadow: 0 2px 8px rgba(0,0,0,0.1);
}

/* آلبوم */
.tg-album {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(150px, 1fr));
  gap: 8px;
  margin: 12px 0;
}
.tg-album-item {
  overflow: hidden;
  border-radius: 12px;
}
.tg-album-item img {
  width: 100%;
  height: 150px;
  object-fit: cover;
  transition: transform 0.2s;
}
.tg-album-item img:hover {
  transform: scale(1.02);
}

/* ویدیو */
.tg-video {
  margin: 12px 0;
}
.tg-video video {
  width: 100%;
  border-radius: 16px;
  background: black;
}
.tg-dl-btn {
  display: inline-block;
  background: #3b82f6;
  color: white;
  padding: 6px 14px;
  border-radius: 24px;
  font-size: 13px;
  text-decoration: none;
  margin-top: 6px;
}
.tg-dl-btn:hover {
  background: #2563eb;
}

/* فایل */
.tg-doc {
  background: #f9fafb;
  border: 1px solid #e5e7eb;
  border-radius: 16px;
  padding: 12px 16px;
  margin: 12px 0;
  display: flex;
  align-items: center;
  gap: 12px;
}
.tg-doc-icon {
  font-size: 32px;
}
.tg-doc-info {
  flex: 1;
}
.tg-doc-title {
  font-weight: 600;
}
.tg-doc-extra {
  font-size: 12px;
  color: #6b7280;
}
.tg-doc-link {
  background: #3b82f6;
  color: white;
  padding: 6px 12px;
  border-radius: 20px;
  font-size: 12px;
  text-decoration: none;
}

/* نظرسنجی */
.tg-poll {
  background: #fef9e3;
  border: 1px solid #fde047;
  border-radius: 20px;
  padding: 12px 18px;
  margin: 12px 0;
}
.tg-poll h4 {
  margin: 0 0 10px 0;
  color: #854d0e;
}
.tg-poll ul {
  margin: 0;
  padding-right: 20px;
}
.tg-poll li {
  margin: 6px 0;
  color: #a16207;
}

/* فوتر پست (تاریخ و بازدید) */
.tg-footer {
  font-size: 12px;
  color: #9ca3af;
  margin-top: 12px;
  padding-top: 8px;
  border-top: 1px solid #e5e7eb;
  display: flex;
  gap: 12px;
  justify-content: flex-end;
}
.tg-footer a {
  color: #6b7280;
  text-decoration: none;
}
.tg-footer a:hover {
  color: #3b82f6;
}

/* هدر کانال */
.tg-channel-header {
  text-align: center;
  padding: 20px;
  background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
  border-radius: 28px;
  color: white;
  margin-bottom: 24px;
}
.tg-avatar {
  width: 80px;
  height: 80px;
  border-radius: 50%;
  border: 4px solid white;
  margin-bottom: 12px;
}
.tg-channel-header h1 {
  margin: 8px 0 4px;
  font-size: 24px;
}
.tg-channel-header p {
  margin: 4px 0;
  opacity: 0.9;
}
.tg-channel-desc {
  background: #f3f4f6;
  padding: 14px 20px;
  border-radius: 20px;
  margin: 16px 0;
  font-size: 14px;
  color: #374151;
}
.tg-last-update {
  text-align: center;
  font-size: 12px;
  color: #9ca3af;
  margin: 16px 0;
}
.tg-telegram-btn {
  display: inline-block;
  background: #1e88e5;
  color: white;
  padding: 8px 18px;
  border-radius: 30px;
  text-decoration: none;
  margin: 12px 0;
  font-weight: 500;
}
.tg-telegram-btn:hover {
  background: #0b5e8a;
}
@media (prefers-color-scheme: dark) {
  .tg-channel-desc {
    background: #1f2937;
    color: #d1d5db;
  }
  .tg-post {
    background: #1e1e2f;
    border-color: #2d2d44;
  }
  .tg-post-header {
    background: #2a2a3b;
    color: #bbb;
    border-color: #3a3a52;
  }
  .tg-doc {
    background: #252535;
    border-color: #3a3a52;
  }
  .tg-forward {
    background: #1f2a3a;
    color: #90cdf4;
  }
}
</style>

<div class="tg-channel-box">

<div class="tg-channel-header">
<img src="https://cdn4.telesco.pe/file/sjqaU07aHJT9aIsxjjxmbgbBhJdB-Z006c3Zp3ZZgNKvtpaZhAokryx4QHvxAa6PRAPcD8PmnMjyf1ilKG1CyIt5n4Ky8eD3QmoIcswgBypGEgLczJv3vCdYJmv6vhCaBQIfprnkBq0rAoCxtvLyZvDQt2yek-xybhzhNWxbPHchMk3_Vj485bh5RD9g0U4f5VLpTrDwQeLW0fixQYCDUhDiWJ-gxUeVOpaPp56QgvCIYxcZtWUQ9QrHZV7fm8niKkqsHUWUfhFhr1da2dPzsAxGaC7eVh1mtc4X1zWihxlO8w7J7L-uESNrSgMnqOXeVfWtVRJ53mGtbmUTCXlvIA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 WarRoom with YASHAR</h1>
<p>@withyashar • 👥 338K عضو</p>
<a href="https://t.me/withyashar" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 چنل رسمی«اتاق جنگ با یاشار»اخبار لحظه ای و فوری از‌ جنگ با تحلیلinstagram.com/yasharhttps://X.com/yasharrapfa</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-15 15:51:24</div>
<hr>

<div class="tg-post" id="msg-16569">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LwuoRGQ8XfDkuN1d18gpw_DS8HnHachji7PD10S8iPVpPPS1Wvp3ZI1AlU_7b0b8Qd0U2Cg8LwLJc_mtDt6MiiNpbiIJzmacEVtXj-q9OD1eWYVkRHlBul1BkYrzHPXqrilzrs7SMXn_nSg08WOmDx45_QkPw2xN25_AFtQGYHcbDVfbfTPa9lC8eVngXs3SQyH9D3vgGvQLTJWF55jAkO7PkinjRdwkZUh2pu-VykblquACTyhTP5khd2r-Xa85tvgOoft_alzEoIecwRKyHW-x5m5-DdTmWFAvYci28OYr1EFTOIloshI7PZWlqyhRYG5r43AelrEJmnTzfiLO_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حضور میم معروف این روزها در مراسم @withyashar</div>
<div class="tg-footer">👁️ 3.7K · <a href="https://t.me/withyashar/16569" target="_blank">📅 15:49 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16568">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">روزنامه الاخبار خبر داد: پرواز دومین هواپیمای ایرانی به صنعا در ساعات آینده
@withyashar</div>
<div class="tg-footer">👁️ 31.9K · <a href="https://t.me/withyashar/16568" target="_blank">📅 14:47 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16567">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/92eb08c456.mp4?token=pTz_kp5xZaN-RhHwj0ppJ1JwmyN34TbiFcQG99hsmzLLXPnNii3-bZIHtn2jW8sxaZzsJ-GrB_Ji7vyLcwRPMToYqK0kdaz6YqRRV0FebicOpKuXP2wUGykj5aA-qoOfQWtPFPcGcar-FLlPF3I1mP3k_F6mlHJGN3LLPSbYOL-caIU5YQ-pDq-ETHw-JiU7VANUnIli63wu3rLhLH2TzCSNwZVsEB3MCB8xHP3wNM7nWy0U5OuG7Gm2WB_N5QWOF5fOdkv9IgeNzSmvNs6uJ9baQoLu4-sf9tHp86ZS-XA2BJexJtoPkycVrdLRgaqdpdbq0d9n_AIY1hcQnxtwfg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/92eb08c456.mp4?token=pTz_kp5xZaN-RhHwj0ppJ1JwmyN34TbiFcQG99hsmzLLXPnNii3-bZIHtn2jW8sxaZzsJ-GrB_Ji7vyLcwRPMToYqK0kdaz6YqRRV0FebicOpKuXP2wUGykj5aA-qoOfQWtPFPcGcar-FLlPF3I1mP3k_F6mlHJGN3LLPSbYOL-caIU5YQ-pDq-ETHw-JiU7VANUnIli63wu3rLhLH2TzCSNwZVsEB3MCB8xHP3wNM7nWy0U5OuG7Gm2WB_N5QWOF5fOdkv9IgeNzSmvNs6uJ9baQoLu4-sf9tHp86ZS-XA2BJexJtoPkycVrdLRgaqdpdbq0d9n_AIY1hcQnxtwfg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترکیه در مسیر تبدیل شدن به جمهوری اسلامی تخت گاز پیش میرود
: ویدیو تعداد زیادی از مردم ترکیه در یک تجمع اعتراضی که هدف آن، وارد کردن یک ضربه به کیسه بوکس با تصویر نتانیاهو برای نشان همبستگی با ساکنان غزه  است
@withyashar</div>
<div class="tg-footer">👁️ 33.7K · <a href="https://t.me/withyashar/16567" target="_blank">📅 14:45 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16566">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">گزارش هایی از حمله و درگیری بسیجی ها با قالیباف در میدان آزادی
@withyashar</div>
<div class="tg-footer">👁️ 38.1K · <a href="https://t.me/withyashar/16566" target="_blank">📅 14:36 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16564">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Hh48so0K2zxAF92UvjML3Lm_sbCCZX08Jh7k2inLmnga1p2Fz3Zln1sptFsnKPE5ofTDpSiI89mEAsKOJrnkcHnMjtwqeNXW2-UdLSjv_d5qLGw2pspAkb1ZLFZhRp3U-ouePyRsfmlKV219X-fyWc7dXZk9Q8pxXMbeHEA2XWxT4KygYNRIKBsBMHVSG-Zz3g5dosWmjHYwFM3-RwCQymUGHNIvo3-30u4r6jwKMJ1Uy1FTQIjG8RlopZ7XIPeNCsrU3Z-jsGUfPrQFO6wvK6QnbS1aPrvlDcp5TMg7MpHQW_qehFXUniP1FN5W_fcmkY_0Mik7ifya0mGoSD-LWw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5278196c6e.mp4?token=ET8mNNLNjC9IENJS4XskEtpl3g4MFtivP3HPUza3qKW4BGpRMiIrFhMee3OU43_Jzrmym29Av0cpW80Zl6JL5ZfCPFQLUjIkA_hgSM5cQ_aoQWovBpoAJUQ7VDKuewHo7V8TWsTTfcW61AvO7-bDjMGNxbjDuoH7wsTr5NaM4C9uGcNOyaIaKO2SMfjn4Z9yIotuSs-99aO1aH-xiuTu0y6WdjUyh0JgQnRTD_rKG_L3QmUZmrCVIJOYWnkVkuRP1oBecZc1J3laks4DgxhFfa-4vi4ahu_WUzy9kWPIAji0UTlbnOBEyZ5H6lFRl0dt4x94HwuGZcLm9lEHgavOTnd4W-n4QfZSbYZMswOL2815O-C4N3dRBRa3gT-ZhfP6f_7rTGqDoo90IFYJxj_SDdMNefdvr0kUGXDfIjPN1uOmo7nJnsjLSXWe9wfq7FFpBySOYa-hlPMZXETBZs9Vi01Kf0R3s1KX4yq82f3XDjraLMgltVtz7R3kiNqssV82wdHd6vGZkOtLBa2qjlAK6ghtOp2QGiszzmmjEr3FiVUOUpeJF0MroI5n2Z7K_gMcin3bxcQI5yxMfONCtl5-c1V9Oa-dZl4WRovl2TQcIGzK3uiTBH0VL3SUgtr0cciQ7bQLMoVu12MMh7jXeUoFd-XFBrlC0KPD4oHle5a_al0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5278196c6e.mp4?token=ET8mNNLNjC9IENJS4XskEtpl3g4MFtivP3HPUza3qKW4BGpRMiIrFhMee3OU43_Jzrmym29Av0cpW80Zl6JL5ZfCPFQLUjIkA_hgSM5cQ_aoQWovBpoAJUQ7VDKuewHo7V8TWsTTfcW61AvO7-bDjMGNxbjDuoH7wsTr5NaM4C9uGcNOyaIaKO2SMfjn4Z9yIotuSs-99aO1aH-xiuTu0y6WdjUyh0JgQnRTD_rKG_L3QmUZmrCVIJOYWnkVkuRP1oBecZc1J3laks4DgxhFfa-4vi4ahu_WUzy9kWPIAji0UTlbnOBEyZ5H6lFRl0dt4x94HwuGZcLm9lEHgavOTnd4W-n4QfZSbYZMswOL2815O-C4N3dRBRa3gT-ZhfP6f_7rTGqDoo90IFYJxj_SDdMNefdvr0kUGXDfIjPN1uOmo7nJnsjLSXWe9wfq7FFpBySOYa-hlPMZXETBZs9Vi01Kf0R3s1KX4yq82f3XDjraLMgltVtz7R3kiNqssV82wdHd6vGZkOtLBa2qjlAK6ghtOp2QGiszzmmjEr3FiVUOUpeJF0MroI5n2Z7K_gMcin3bxcQI5yxMfONCtl5-c1V9Oa-dZl4WRovl2TQcIGzK3uiTBH0VL3SUgtr0cciQ7bQLMoVu12MMh7jXeUoFd-XFBrlC0KPD4oHle5a_al0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">برخی رسانه های رژیم از حضور جمعیت ۱۵ الی ۲۰ میلیونی در مراسم تشییع صحبت میکنن ولی اگه مراسم حج امسال در عربستان که فقط ۱ میلیون ۷۰۰ هزار نفر توش شرکت کرده بودن رو نگاه کنیم میبینم جمعیت چند میلیونی خیلی خیلی بیشتر تر از چیزیه که فکر میکنیم.
@withyashar</div>
<div class="tg-footer">👁️ 37.8K · <a href="https://t.me/withyashar/16564" target="_blank">📅 14:35 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16563">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">پاکستان آبزرور : احتمالم میرود برگزاری دور سوم مذاکرات ایران و آمریکا در اسلام‌آباد در روزهای ۱۴ و ۱۵ ژوئیه (۲۴ و ۲۵ تیر) شروع شود
@withyashar</div>
<div class="tg-footer">👁️ 38K · <a href="https://t.me/withyashar/16563" target="_blank">📅 14:32 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16562">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">توافق اوپک پلاس برای افزایش محدود تولید همزمان با بازگشت قیمت نفت به سطح قبل از جنگ
هفت کشور عضو ائتلاف اوپک پلاس توافق کردند تولید مجموع نفت خود را در ماه اوت به طور محدود و روزانه ۱۸۸ هزار بشکه افزایش دهند، همزمان که قیمت نفت خام به سطح پیش از جنگ ایران سقوط کرده است.
@withyashar</div>
<div class="tg-footer">👁️ 39.5K · <a href="https://t.me/withyashar/16562" target="_blank">📅 14:25 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16561">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Q2U-riMSKWoIlRspRuPqV8_nuLGmqgOE3VoK_PUdX5IDaT2o7XPbMHtWfHTz5PMILZz10Swzdmf57_kU8OSLoeZwgqmZEmygzw4_BqPU-aSKgSxX4pHqs36MHcgifAjRYPMzLkD6eqMu95_N04Es-fUspf0-lfPTk0ADvL3RDL-oHQc1Iqpcj-8ewgGB245_ABNtdh9DEVS6mgzOCh9TWsYmTEpJ7I_9NqfuVGyyl7fXyI6bhSx8AKK-R_JkGqtAl3-rDYyrfp4B5HxLWID9L7JtZ94WTzFojENpAiNINs2qrmcXihP9G7arICo_fLb7nGDySFPvxQ83D9hGMj1KKw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بلومبرگ: جمهوری اسلامی همچنان با مشکل فروش نفت روبه رو است
@withyashar
طبق این گزارش ایران ۵۸ میلیون بشکه نفت روی دریا دارد که ۹۰ درصدش رو هنوز نتوانسته بفروشد
از دلایل مهم این موضوع کاهش واردات چین است. از دیگر دلایل هند نفت ایران را یا روسیه جایگزین کرده است
اروپا هم در شرایط فعلی باتوجه به نگرانی از فعال شدن مجدد تحریم‌های نفتی از خرید نفت ایران خودداری می‌کند</div>
<div class="tg-footer">👁️ 47.8K · <a href="https://t.me/withyashar/16561" target="_blank">📅 13:53 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16560">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">کره‌ جنوبی:ایران برای مراسم وداع با رهبرش از ما دعوت کرد ولی زمانی که میخواستیم هیئتی برای مراسم بفرستیم به ما پیام داد و دعوتشو پس گرفت و اعلام کرد حق حضور تو مراسمو نداریم
@withyashar</div>
<div class="tg-footer">👁️ 46.7K · <a href="https://t.me/withyashar/16560" target="_blank">📅 13:49 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16559">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vpgapNDk4n1WjNxr1ivqpRwQBetlG9VzsWg6bkcrM9cgsX4nFZClwYx_FrW3tEKQvDPTPj3Cte2nHh4UJAfIQ5g_WOhQtL8iFkDvEPDQ9UkPw9bC79RXuR38CWZARTulLUsgWSffu6M-pUR0gJfn4Iw1odAqHbC5ajANhx4b5c4_4vf6H673ZukEq451iNhaB4gsSnE9RG-R0NH4KZp1h1t538dM0FyPIQZUxGQ5bie9jSi6l7OSA2xI6defsTV9Ls-SWGOrsTe7ICaWpKC56DEezK-5Zn_RdDiDv42Prh3h12UmJShGlULLHGA0qckCYMqVwsihySly8iFZp-wuLw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حضور میم معروف این روزها در مراسم
@withyashar</div>
<div class="tg-footer">👁️ 48.8K · <a href="https://t.me/withyashar/16559" target="_blank">📅 13:42 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16558">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">دفتر رسانه‌ای دولتی غزه(تحت مدیریت و کنترل حماس): تمامی آمادگی‌ها و ترتیبات قانونی برای فرآیند تحویل و تسلیم سیستم دولتی، انجام شده است. @withyashar</div>
<div class="tg-footer">👁️ 51.8K · <a href="https://t.me/withyashar/16558" target="_blank">📅 13:25 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16557">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">دفتر رسانه‌ای دولتی غزه(تحت مدیریت و کنترل حماس): تمامی آمادگی‌ها و ترتیبات قانونی برای فرآیند تحویل و تسلیم سیستم دولتی، انجام شده است.
@withyashar</div>
<div class="tg-footer">👁️ 51.3K · <a href="https://t.me/withyashar/16557" target="_blank">📅 13:23 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16556">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JyyS4o7qKc4ylwLjniCk2y1CqoQQqNkap_SI-pdwCdqNyeAysYXRtT_dkEJyEq39KKbk0lO0WpKQMdmzTIKrlOhPYSRsoRtAMB_J2R5EFN8Ee1ivimSgXlFaKfPJ6Hmks4devIjN8jcEUTA-P-1MNxZUY9E32zclV6BdagikTliS20b0_ujpm6oYa7R6HYYTkm0IWB0bTC1nsWrXOYVl8azIuMh8lD8zrR77bJbOZT5w9fBTQAQLxxPnRdzT01rkDlcChVJn1wZeI4JvBKQIMAbkWi1S-7xiCbGN0cnWjxgUc7eLAY3jy3y_Mlc6NT9cT6ng1mb4sBywRZAkPOrP_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دو حمله پهپادی هدفمند اسرائیل در جنوب لبنان.
@withyashar</div>
<div class="tg-footer">👁️ 53K · <a href="https://t.me/withyashar/16556" target="_blank">📅 13:14 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16555">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/59bbec746d.mp4?token=fCM8z1mxUVhkhL6YQf2K7J9OfrHA7cQk3l2TYEGhd-6wbF4bT-711AqSnItR5-OZrVl1GEVYChzSVdq1Y2KgClwzftRTp51eWSHgKvyLJpdOKAJo8EAJg3VgqoJJ_P0DMXarASSV25Yxbvy4O5Q-WWdE5Z1Xt-5EycyjCDYm9FjPhJeKDDtrjZ1JCy7CYV_8-tksMHXaqn-px10jzDAc8lhkhQXQJTTstyA4cic4jcYmaulbim0Ev2a1ytO95h4h9EMzRBSjtfmkSrxhBXpP_5htkV7XAZVcv-ejDB1cE_R1geDYOVhA6Lrqot4GJUwHXIoaKTVGqoHbnpv6NOHFPg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/59bbec746d.mp4?token=fCM8z1mxUVhkhL6YQf2K7J9OfrHA7cQk3l2TYEGhd-6wbF4bT-711AqSnItR5-OZrVl1GEVYChzSVdq1Y2KgClwzftRTp51eWSHgKvyLJpdOKAJo8EAJg3VgqoJJ_P0DMXarASSV25Yxbvy4O5Q-WWdE5Z1Xt-5EycyjCDYm9FjPhJeKDDtrjZ1JCy7CYV_8-tksMHXaqn-px10jzDAc8lhkhQXQJTTstyA4cic4jcYmaulbim0Ev2a1ytO95h4h9EMzRBSjtfmkSrxhBXpP_5htkV7XAZVcv-ejDB1cE_R1geDYOVhA6Lrqot4GJUwHXIoaKTVGqoHbnpv6NOHFPg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تصویر ماهواره‌ای انبار مهمات پایگاه هشتم شکاری اصفهان که توسط BBC منتشر شده است، انهدام کامل ۴۶ انبار مهمات و سازه این پایگاه را نشان می‌دهد.
@withyashar</div>
<div class="tg-footer">👁️ 52.4K · <a href="https://t.me/withyashar/16555" target="_blank">📅 13:13 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16554">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">خبرگزاری مهر: پزشکیان، قالیباف و فرزند رهبر انقلاب فردا در مراسم تشییع عراق شرکت می‌کنند
@withyashar</div>
<div class="tg-footer">👁️ 52.6K · <a href="https://t.me/withyashar/16554" target="_blank">📅 13:08 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16553">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">کاتز وزیر جنگ اسرائیل:
خامنه‌ای که مراسم تشییع جنازه‌اش اکنون درحال برگزاری است توسط ما کشته شده زیرا او طرحی را با هدف نابودی اسرائیل آغاز و رهبری کرده ، اگر رهبر جدید هم از عاقبت پدر خود عبرت نگیرد به سرنوشت آن دچار خواهد شد
﻿﻿﻿﻿
@withyashar</div>
<div class="tg-footer">👁️ 53.6K · <a href="https://t.me/withyashar/16553" target="_blank">📅 13:03 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16552">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c0de6a03c0.mp4?token=mlPjf8VlEV7wxPpuxA5aZw9RA7CJHjrXBmr_CdcQQoDWInqjYEQq_mPL9t_1VEevjLRceIHvR9mCabbYCLGrkU8qpToEskv7jpESnV7Owrly-ZwTR0gLzFtYziRM_Vbnj0V9S-OyYrxpUEgz5b_Ejy_lb-GjipvfZ01K1BjyplNKXePV1CB8crNIKAa3Rygox9ehuG9qja0GnLtK1bFac4EsajzP5Ve-QElZv7RV0uNBwwBrhbAsamQsp5aa5gH_U32jSJ6yg92EiqzlnfRriv2LGtcCvFFA7Htycmw-5caXmbGBel7cWzzCdvw0r0O6L55dSAEA86YKlLAL52NnRw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c0de6a03c0.mp4?token=mlPjf8VlEV7wxPpuxA5aZw9RA7CJHjrXBmr_CdcQQoDWInqjYEQq_mPL9t_1VEevjLRceIHvR9mCabbYCLGrkU8qpToEskv7jpESnV7Owrly-ZwTR0gLzFtYziRM_Vbnj0V9S-OyYrxpUEgz5b_Ejy_lb-GjipvfZ01K1BjyplNKXePV1CB8crNIKAa3Rygox9ehuG9qja0GnLtK1bFac4EsajzP5Ve-QElZv7RV0uNBwwBrhbAsamQsp5aa5gH_U32jSJ6yg92EiqzlnfRriv2LGtcCvFFA7Htycmw-5caXmbGBel7cWzzCdvw0r0O6L55dSAEA86YKlLAL52NnRw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اتاق جنگ با شما : یاشار جان سلام امروز تو مصلی بعد از پایان نماز ، بلندگو ورود مجتبی رو اعلام کرد اما بلافاصله هم صدای مجری قطع شد و بلافاصله آنتن ها برای مدتی قطع شد... @withyashar</div>
<div class="tg-footer">👁️ 59K · <a href="https://t.me/withyashar/16552" target="_blank">📅 12:43 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16551">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jah-1cPQMBAmvA5PfxhZS7K8dOke__8MyYDsW017rUdRzDsi1eHz0NgnX-23RWohpLmPAMAQXCdodYMwQ0aG-McQ7G21bENwtWHNf2Bcw2jGxL7z9hBbcdaDJRyN6JqpKA7fHX9kwvv0lVqvTF3HxEfP3UXUnEn28XTBvKVFg5PXDGp9QPWxRQJdYGzMBliQJue9C_ZjE7vkpi47vy1Qji2UM2O9pfiMt5pLPtmUGkwnYrUPZ0dnhGdbJPotqM0PPuYC_dKxI86-6Y9Ono-Jwo1zmG23YE8EEJH_XvU37yV-lxNDDd65OxxVfEmKrFZxj1qhP-_cacelus40LRIVVw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ارتش اسرائیل به حملات خود در جنوب لبنان ادامه می‌دهد.
انفجاری در پی فعالیت ارتش اسرائیل در منطقه بنت جبیل رخ داده است.
@withyashar</div>
<div class="tg-footer">👁️ 56.7K · <a href="https://t.me/withyashar/16551" target="_blank">📅 12:38 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16550">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/061472f621.mp4?token=A7-yu_uWrDr2EX2O5RK1okboDpGdU4gH0MgHgPzLkhL3YW_zx1LgYWbVn2Laqyvc6GpZxFGesvCoZRo3ROP-IEc6Dn-_aD80PwY9lF_7K_AJoQ7xkM-8qbh1H3EScg41sKsoVZ8aokE0e5t55_rFyTQAOHfL8k1fAIObP9RJM4UtJuKi4DgOlN8WoLSlCzvV9XCrVqiJskjWGoS9Bl7AJQC0-XqPkdOGk40hWy4wmwnGFs7vWGaQmffyTXtMl-8NU6CrstxmGpAqCu0rgKFtF-DNwTyRa91lMJEiKM1mJ7UySDEMyYarReDVMltk6Ij4BYIwYHuuwo741yZeGGt6ew" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/061472f621.mp4?token=A7-yu_uWrDr2EX2O5RK1okboDpGdU4gH0MgHgPzLkhL3YW_zx1LgYWbVn2Laqyvc6GpZxFGesvCoZRo3ROP-IEc6Dn-_aD80PwY9lF_7K_AJoQ7xkM-8qbh1H3EScg41sKsoVZ8aokE0e5t55_rFyTQAOHfL8k1fAIObP9RJM4UtJuKi4DgOlN8WoLSlCzvV9XCrVqiJskjWGoS9Bl7AJQC0-XqPkdOGk40hWy4wmwnGFs7vWGaQmffyTXtMl-8NU6CrstxmGpAqCu0rgKFtF-DNwTyRa91lMJEiKM1mJ7UySDEMyYarReDVMltk6Ij4BYIwYHuuwo741yZeGGt6ew" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حضور دایناسور جنتی
@withyashar
انگار دارن به ۱۸ چرخ فرمون میدن
😂</div>
<div class="tg-footer">👁️ 62.6K · <a href="https://t.me/withyashar/16550" target="_blank">📅 12:11 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16549">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/19ab53f55a.mp4?token=na5zg8u8kkHa7NEQBy1prPt7vgcJ0Z9WJyxa5gSLhBzikfFjBVoQspiUf2eq-xkPoAphRYQ2yD8CJAenAitZifNLqT2LszQUXR0G69UmyNB9-awOaEukW4i5upGW0J9YKpGyisgrQm8FWlyesphK4hX6Iv430rdjOgMimOr_Yvm7sYJXNldfgGZ6L2dMV1qIadQSDyE2YwrUdIXcNEM15WJBEH8yMn4mWVqI-84ORRgnLOGdIw4B5OhEMDDVbnf1_d_3oOmy2K15W491x7mCoHcXACd96kqzKjjeGEer3j9H9EqFdPQ_rIusW66IbXq6oH-UWiAANexSaAi3C-yWaQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/19ab53f55a.mp4?token=na5zg8u8kkHa7NEQBy1prPt7vgcJ0Z9WJyxa5gSLhBzikfFjBVoQspiUf2eq-xkPoAphRYQ2yD8CJAenAitZifNLqT2LszQUXR0G69UmyNB9-awOaEukW4i5upGW0J9YKpGyisgrQm8FWlyesphK4hX6Iv430rdjOgMimOr_Yvm7sYJXNldfgGZ6L2dMV1qIadQSDyE2YwrUdIXcNEM15WJBEH8yMn4mWVqI-84ORRgnLOGdIw4B5OhEMDDVbnf1_d_3oOmy2K15W491x7mCoHcXACd96kqzKjjeGEer3j9H9EqFdPQ_rIusW66IbXq6oH-UWiAANexSaAi3C-yWaQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اولین ویدیو از احمدی نژاد
@withyashar
یاشار: من چیکار کنم کاپشن پوشیده ! روانی ها
🤦🏻‍♂️
😂</div>
<div class="tg-footer">👁️ 66.1K · <a href="https://t.me/withyashar/16549" target="_blank">📅 11:32 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16548">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c911eae2a5.mp4?token=TVCsUOpAhhpInQaVfZZ_BmU3860xf9JFNSN6_3naEQuL12fxTHsk_pzt6K4iwRJ8VPjvNREcCSFXSabXh6TRlluaKyp1tGBfRcEpw4GRhsGfe8GLVLy3FlQqEj7bpSW19RhFw05U_McZHAoZ7bCzd9h_Dh15j6O3Px3Z9d_Qr6FBDDq0-Fh8dPxtLTPWpU8mx835dHZU0B51a3qtaoiHhQyHa4ZKpifBAV5bsSfEREwjIFFr_RiUj_KJAkXoLmWmBIpJPbuxdbDZSt3WQZEKu5Z0uaxKx8y3mZbL2OyRxtL9emQ3nCo2btumyDFl673m6HWzuZQHHbNy4NyMlrGWwQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c911eae2a5.mp4?token=TVCsUOpAhhpInQaVfZZ_BmU3860xf9JFNSN6_3naEQuL12fxTHsk_pzt6K4iwRJ8VPjvNREcCSFXSabXh6TRlluaKyp1tGBfRcEpw4GRhsGfe8GLVLy3FlQqEj7bpSW19RhFw05U_McZHAoZ7bCzd9h_Dh15j6O3Px3Z9d_Qr6FBDDq0-Fh8dPxtLTPWpU8mx835dHZU0B51a3qtaoiHhQyHa4ZKpifBAV5bsSfEREwjIFFr_RiUj_KJAkXoLmWmBIpJPbuxdbDZSt3WQZEKu5Z0uaxKx8y3mZbL2OyRxtL9emQ3nCo2btumyDFl673m6HWzuZQHHbNy4NyMlrGWwQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خودرو ضریحی عظما
@withyashar</div>
<div class="tg-footer">👁️ 66.4K · <a href="https://t.me/withyashar/16548" target="_blank">📅 11:14 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16547">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ddbc5efdc9.mp4?token=ZA9ajhrEox7bZEb4rCnp2cM0YeT73gKspDq9nfmhNZt98g7lYMOTpID30gbEnvtrNjDgwayPz7CmaQI9DI-8YYZwuOpdqDLfsRbTHNbisQuh2v2S2K9QHRPTNYmPRnBo6upVI9o7wWLrVz0ABbp4tIvxy1rbFgvyXLgNOH8BA-Ij9_6dUYH6mskFHNsN_YOZE3QzRgIYvWeYgW240fthE-_FGIgz6HQmqkCSGALRwTtDiPwARPkj-HSKJEEU_djEfJcUn2M8d3pO9F9pWH9av53BVfxwyF_JNCB8uqaBp4un-pt15F8NMH1HwDTCwnhg0h9-E5EQ_EH8znP2anbo9g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ddbc5efdc9.mp4?token=ZA9ajhrEox7bZEb4rCnp2cM0YeT73gKspDq9nfmhNZt98g7lYMOTpID30gbEnvtrNjDgwayPz7CmaQI9DI-8YYZwuOpdqDLfsRbTHNbisQuh2v2S2K9QHRPTNYmPRnBo6upVI9o7wWLrVz0ABbp4tIvxy1rbFgvyXLgNOH8BA-Ij9_6dUYH6mskFHNsN_YOZE3QzRgIYvWeYgW240fthE-_FGIgz6HQmqkCSGALRwTtDiPwARPkj-HSKJEEU_djEfJcUn2M8d3pO9F9pWH9av53BVfxwyF_JNCB8uqaBp4un-pt15F8NMH1HwDTCwnhg0h9-E5EQ_EH8znP2anbo9g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ورود وحیدی‌ با موتور
😂
@withyashar</div>
<div class="tg-footer">👁️ 66.9K · <a href="https://t.me/withyashar/16547" target="_blank">📅 11:11 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16546">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">الاخبار لبنان: یمن در حال بررسی بستن تنگه باب‌المندب به روی کشتی‌های سعودی جهت فشار به این کشور است
@withyashar</div>
<div class="tg-footer">👁️ 66.2K · <a href="https://t.me/withyashar/16546" target="_blank">📅 10:58 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16545">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PQzQGnop9GX1qdTIWkKXxxQCIWPwxN1-va-cHPac1htjzqoSFR8WzAQ756AkhBoJvGcBDZ_avdwbJAv6XwAU3EXzJF_gqTJPLeu2GuZTrBY5AQI8BC4dxuHWIbAqOYkndryKYZ0hCjILIddb_H1082I6xXSb-9QRHbHgU4dmqGXV9QaPD8qBCKKog1-jq5wLf0zTlM_Z2SA7SDLPiF8YLUcrsrowXmPP-8ND36brcsxyZYXN8i-A_892V2x9rG2CSZrP1kwMCozUiphsu_mpYyQghLl9zkwVVLFYJiu-VbiNHPUB-sL5ox871cD3-zA-DhGGT9Fq3zMEBpsTFYT-DA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پس از انتشار گزارش‌هایی مبنی بر اینکه اسرائیل و آمریکا قصد داشتند او را در طول جنگ، به قدرت اول ایران برسانند : محمود احمدی‌نژاد، رئیس‌جمهور سابق ایران، در مراسم تشییع جنازه علی خامنه‌ای شرکت کرد.
@withyashar</div>
<div class="tg-footer">👁️ 70K · <a href="https://t.me/withyashar/16545" target="_blank">📅 10:51 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16543">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jZbRt2l4wrv16uBvYpA7lsz-yhU4k36b7GfIacvb52HuDQZmTQ-2qudGtIpjoumLkTrtG5m3BWo0G5Vxy792Oa_Kkb1W0zzw0KhfmYbIvURHgL5o-FZWIT0GN32GVjd4cYkMdvvd2lJ-Ys3IoVcW4vra3NI2x6_G8Zyp17ajUodix_j0tNdPzBN7D54gdIE97FWJ80qKQQ0wkUSQkXNpHh3-eXcqB5sSS8bWdnz44ugje_sIFWO40Q-ejtZRbh3eK4w0m9TovG9ZQbAshOATF5WLuW_XB8bUNd3ooYhyyZ3Y83tO8nH406gPRuQyGiXxrnKrbzzxv0G5UAIpnPEwpw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/BqhQu3CUW8C0iUQLu-skWjyLHdNKg7coRdwpl9aRyA13pXhOcbabp9aUkGBOSZJoZak07JX2tun10LTYHx1XT38O1dwupS5NvUClimDZEm4RiFdRZfhnvczJN2s-dBMPiJNY5v3VZRmflCHFNC0_FcE8P5qsNEboPA_5XgrE9cRW81bNsiEx46xHhgCijCZ2csXc94v3ZoOiAEGoPCNix0fd3LVrUpYcfi3hOinUIHYNzp5krympWnUBjbVOGgbEvMlzSa2WupYq6c1MgChjYK5wheV9b1vCG9qAE0yY3R_VtOkMWO1aKj1Dju0HBUrclSGBEDePFR_U9UFQgNHlqw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">نمایش قدرت در برابر اردوغان: ارتش اسرائیل در تمرین مشترک با ارتش یونان.
در طول این تمرین، هواپیمای تانکر اسرائیلی در حال سوخت‌رسانی به هواپیمای F16 یونانی بر فراز دریای اژه فیلم‌برداری شد. ارتش اسرائیل گفت : "این همکاری بخشی از یک برنامه استراتژیک گسترده است، در دوره‌ای که ترکیه تلاش می‌کند قدرت بازدارندگی خود را تقویت کند."
@withyashar</div>
<div class="tg-footer">👁️ 75.3K · <a href="https://t.me/withyashar/16543" target="_blank">📅 10:10 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16542">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">این آخرین تلاشمه …
@withyashar
⚠️
یاشار : عرزشی ها اومدن ریکشن فیک زدن رو این پست ، اتفاقاً این کار ارزش این ویدیو رو بیشتر می‌کنه و نشون میده چقدر سوختن</div>
<div class="tg-footer">👁️ 351K · <a href="https://t.me/withyashar/16542" target="_blank">📅 02:46 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16541">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NT8JaqUohsnl4cMC54Zb7bR68dgjsTFmNbMJNFTsELEswqWYaZVTGdQSJ2Tj_fB2TF3bUo7ZnVw6OBvPQiqAvHH3lXaxc4KiZhS08tiOE2f3rs6e7hMzvXNCULOQsCIhPCxnRHTBxE-U70RM9G7Y86mKGZ8L2fyLOST7QUhD1nmNQffH1us7P-0qw7QTaWMBKLVS9d1qKswLzBOOHqQ8_nCWKqnOkib4n1ijiAn5gQlrfi9B74Swo9MzRYpcoo4Eoogv5egoGJbi8Szp2FHVn7C-dkPxbxn-L74Yr3GO4x5Wo27uDfqd6OpTgSBMQ4pEqWMMnvNPT-WIDlG06R2mDw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سوگواری شبانه روزی نیرو هوایی آمریکا در‌ تکیه تنگه هرمز در غم عظما
@withyashar</div>
<div class="tg-footer">👁️ 100K · <a href="https://t.me/withyashar/16541" target="_blank">📅 01:58 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16540">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/b4s_nfyC49l-PdEmi31ORWN_H206gh3I_WIq8rCnNtE7dp3a8Mj5BpynxgvQF3Tu5816gyKU8bYJteLJsMEhRdkpbfpnXwoRQ1T6WZap6E5AYyaSOWR_m2clModO8EHfuHNPhre3a9kFopHv1DopZAJlmklPgr9BUypm-OvFhGS9jlvrxwOZj96Kj8rB88U9wioUBeXRaOpYjqUbzbOyl8aFS8CG8Nu76O16Ku7rA0EtGBZjM1cDDX5q5lnXWn6Al93cd3A2p-grjyCNHVgjxSWsw0C2EoCeNuubJet4CQqO0jtW4qxIBApisOyiCWSXq34xNzwwWuuY-o4NI6sVrQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قفلی جدید
😁
@withyashar</div>
<div class="tg-footer">👁️ 100K · <a href="https://t.me/withyashar/16540" target="_blank">📅 01:51 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16538">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">گزارش ها از آغاز درگیری شدید میان حوثی ها و ارتش یمن تحت حمایت عربستان در جنوب یمن،ده ها کشته از هر دو طرف تا کنون مخابره شده است.
@withyashar</div>
<div class="tg-footer">👁️ 100K · <a href="https://t.me/withyashar/16538" target="_blank">📅 01:19 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16537">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vBipYKfDPqmOklbyvviicWxuY1nbWKrXwyS27GkhX7JGBP_1t5DdMIrlxoXDHC71yawirHanGkpofFXTBpFpByhepH0q0ZURg3kuYNKnpZ5DlJnwc2HQpfjsJZhCPCIJD_AF8BxPhsA6hxAxUeLs6xa34a9drmL-05NqOf8nhh0rufkDIJAWZNUGEnT3pnxKZcrx-3oFjXtCxtDKPERyIu2XXXhG2dhWz6je4_LO9y0mSOt7R4DkKc_fXBSOBN2-nU46caoCOG-_j_WpgvKUaSBtnJ9dHDlH0dmjuxicEiy_HFLiUKJvmbf6PIDLRCt26ApP_ciTzqzFs31Gqz9_Vg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ پستی از خانواده خودش در سال ۱۹۱۵ (۱۲۹۴) منتشر کرد و نوشت : پدرم، پدربزرگ و مادربزرگم، عمو و عمه‌ام!
@withyashar
یاشار : میخواد بگه ما از قدیم پولدار و با اصل و نسب هستیم</div>
<div class="tg-footer">👁️ 103K · <a href="https://t.me/withyashar/16537" target="_blank">📅 00:49 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16536">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fhgusyX1GsfRZfYOTXhWJuEofw7UBsEEBM-imYskrWfbhXNbIPL1G5uFzU7sev9tOpYjSA18y1Hf6Y0AVmpTkWJnrHffm5JFqiYr3i7JDJzIGYAm446PteLVrM-qUa3PxY0kPz32mgtPp3YJetficfj5nvxQZaD59Ts1iZRwqsRxXX0WSpnowfESg_EhYoKrdUVPRXwdK7FUGJuKVbsnH33dAihAgjFgwxiEEDw-BULFA7aJPaRpnKhkjUo_qUu_pyHcZ51Q_8bK7bmmqVFkxGgASYsJj3CJJxKb0QtV7GNU7m2aqUk1TIpjTtHMRZAYBohkGQq6AKgppmhrRhwKKA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تهیه غذای «هانی» اسپانسر تشیع موشلی , دسر هم حتما با «میهن» بوده!
@withyashar</div>
<div class="tg-footer">👁️ 93.3K · <a href="https://t.me/withyashar/16536" target="_blank">📅 00:33 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16535">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Rd2TKAoHNnH4UKt-OjOWblIY8xKNzyhygzAJOnJBj43DH5-bshBQc00UBgrvzNf307Jmf1JzlLCT3M_bDtu_FZ-mC0AiZL2lnaslbLXVofrh6-60d9lBQzwKJxEuyrU-GsPwSywY2wwrum9XRjh0oBjUU8lM6bwl3LxykvizuLkE8IORCtVdCew6dlBZw-zeeiEaZq7Xi7T2WrzhCVtlqwx23iehSlgOIUyM_F2G6fxPQaNlVnQzt30zqT0Mae8JJBkeCnqZKx6Cg0JGZk64kNe4gRf7zUycW1x0_sFhElrbhenWJwL_aWRE5POFxTReu53cZpfMB-TjR_aYL9CEIw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سپاه پستانداران انقلاب اسلامی
وضعیت بدنی نیروهای محافظتی امروز در مصلای تهران
@withyashar</div>
<div class="tg-footer">👁️ 93.8K · <a href="https://t.me/withyashar/16535" target="_blank">📅 00:21 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16534">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">در پی گزارش‌های منتشر شده از عربستان سعودی، منابعی در نوار غزه که از جزئیات ماجرا اطلاع دارند، به کانال۱۲ تأیید می‌کنند: حماس احتمالاً فردا اعلام خواهد کرد که کمیته‌های اضطراری دولتی منحل شده و یک جانشین برای مدیریت این کمیته منصوب خواهد شد. این موضوع تا زمانی که کمیته متخصصان وارد نوار غزه شود و اختیارات مربوط به اداره ادارات دولتی را به دست گیرد، ادامه خواهد داشت.
@withyashar</div>
<div class="tg-footer">👁️ 90K · <a href="https://t.me/withyashar/16534" target="_blank">📅 00:15 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16533">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">خاستگاری‌جنجالی نوک برج امپایر استیت دو شهروند روس پس از بالا رفتن از نوک آسمان‌خراش «امپایر استیت» در نیویورک، در همان محل مراسم خواستگاری برگزار کردند، اما پس از پایین آمدن از ساختمان توسط پلیس دستگیر شدند @withyashar</div>
<div class="tg-footer">👁️ 90.1K · <a href="https://t.me/withyashar/16533" target="_blank">📅 00:10 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16532">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OR968o0VnO9HNFN2MQSBH1bJGfr-A_qDEOK2u8Fff4KYU-M93yuQFl4y5S66Q5hIDGgHnXe5rtrAd2zpHdRx0z60jJ-Ic92TTRnSvLZOKY72kJdWWWyMGJv2duW23WtOgXP9iNBQ9g-BQ6FlwdXeo9efehsdounXOxNb5AJi-5pm1qM-7pQ9ZmJbO5tT3HwlfhCV52egVmfHO2BH7U18mXgS4inSTsH2XlJ6or1p6Sej9cJrafGU7Z7yu14IhElw2LGFyptr3vJpzppcXYT35xt5WPedHZJvgCEYzwatewZTJ149DGg6nkLSlq6LcrDVeU-hyBbA-XP4xvPUtSOveg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بعد از حدود ۲۴ تا ۳۳ هزار سال از انقراض آخرین نئاندرتال‌‌هایی که در منطقهٔ جبل الطارق دوام آوردند ، امروز یک نمونه در
تشیع جنازهٔ آقای موش علی دیده شد.
@withyashar</div>
<div class="tg-footer">👁️ 90.2K · <a href="https://t.me/withyashar/16532" target="_blank">📅 00:02 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16531">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DaN_xqDCmooTW2D5IKvjgHMr1ODswm67u_b4yZgX1-7x5T9gb9-oGlQN317rHd-UsSbKsrtN6qwKFiNHeDq8ylXeL45Un89WjHJHNMW2M61sMbDjaTSfb_G_fCUrC-s6f7amHSRlLa-Y-YSYCFda_ZPgMG2lRhOy_0KedgZm6ez6IZNY6b-5xcsEoPJvIyAd5HZsU7uG2lDKw8XbByCGbyOpgoFNYyc2E0e8JsfGI9EtS0rA8eHAxAU2GPglqGlip1HA4wbvDZVG8mU3O0SKj_HkvjmH4fo4GtXdi6moqgii_GVRioVXc_7PJl5cqEYHD5Jw7Uh-3kCdoIJXks-b5w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">Voice message</div>
<div class="tg-footer">👁️ 86K · <a href="https://t.me/withyashar/16531" target="_blank">📅 23:47 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16529">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LAC-GWJwNLmhqSu8aXdABQesyEeHNVd1zGgmx8-D6FlqqnD58EeHcQBJvOx69ncujvkyNjgdmfffB51ukw0F69D6PvNNZy2CGuGoI6YzJFvf6rCYZ-Q-AI-UIbicO1lqvXirT4KROGgAix-r_iT8uWZ_jkdz7QbUSQlNsAqp7tkI8lsz-rlJLkbJPcPd8yyP0pLMBQ-29X26b0sMbV5crUH4_DSeUOb3dpfNiqo4GFVbvl7qzzH7nMaxYf4RPOkPGvILgK1gDVKWyn9Hza4cZVMevNE9xhD9xAwaXp_LJJ_U2T8Gp06VKHOnG4NznUIGElWWq3qL1_4g-m8OieoX_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏شرکت هواپیمایی سعودی اعلام کرد که هواپیماهای بوئینگ 777-200ER از رده خارج شده خود را مستقیماً به ایران نفروخته است.
‏این شرکت در بیانیه‌ای توضیح داده که این هواپیماها در تاریخ ٧ ژوئن ٢٠٢٣ به شرکتی واسطه خارج از عربستان سعودی فروخته شده‌اند. پس از اتمام این معامله این شرکت دیگر هیچ ارتباط عملیاتی یا تجاری با این هواپیماها ندارد و برایشان اهمیتی هم ندارد آن واسطه این هواپیماهارا به که فروخته‌اند.
@withyashar</div>
<div class="tg-footer">👁️ 87K · <a href="https://t.me/withyashar/16529" target="_blank">📅 23:40 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16528">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DKqm39QA8r1k0pqAXTmvj_VHqprFBX59y-idWKUCTqZtixRnElu-vJzgoqJHU6MeqLFf61sIVrLTSWCvJfCaLLW0CJxnTjltBcjIwrOBSXCu5pmzyb9Fn8GHl1oebav77EZpdre4RoJwnk_NQaVmMqk0ozdifsfx3_TR5n-U-TyFHkot2VlpypzSiugYDl8HfqvdaC3d0yMb9gh-LRUbpHj8meVvBWQCiyGQYKt-pNZ_shY67L9T-Nrd2AoI3JQxANVB7AohDI0ObjDhi1uMpdPsmxU20oogDUoFVMGYkOr5rtngJA62wWXL_i22IGM6fFWDPsuOJqU570Qc3IkqlQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ته مانده جمهوری اسلامی …
🗑️
@withyashar</div>
<div class="tg-footer">👁️ 86.7K · <a href="https://t.me/withyashar/16528" target="_blank">📅 23:34 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16527">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">صابرین نیوز: محمود احمدی‌نژاد، حسن روحانی، محمد خاتمی، محمدجواد ظریف و اسحاق جهانگیری در مراسم وداع رهبر شهید انقلاب شرکت نکردن
@withyashar</div>
<div class="tg-footer">👁️ 88.7K · <a href="https://t.me/withyashar/16527" target="_blank">📅 23:27 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16526">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">کریستیانو رونالدو به گمانه‌زنی‌ها پیرامون آینده‌اش با تیم ملی پرتغال پایان داد و به طور واضح اعلام کرد که جام جهانی ۲۰۲۶ آخرین جام جهانی او خواهد بود. این بازیکن ۴۱ ساله فوتبال در کنفرانس مطبوعاتی پیش از این مسابقات گفت که قصد شرکت در جام جهانی بعدی را ندارد، اما تأکید کرد که هنوز قصد بازنشستگی از فوتبال را ندارد.
@withyashar</div>
<div class="tg-footer">👁️ 90.7K · <a href="https://t.me/withyashar/16526" target="_blank">📅 22:59 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16525">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">یک مقام ارشد کاخ سفید گفت که دونالد ترامپ، رئیس جمهور آمریکا، در دیدارهای خود با رهبران در اجلاس ناتو در ترکیه، موضوع حفاظت از ترافیک دریایی در تنگه هرمز را مطرح خواهد کرد و خاطرنشان کرد که متحدان پیش از این تمایل خود را برای شرکت در این تلاش ابراز کرده‌اند. با این حال، وی گفت که بسیاری از آنها کشتی‌ها یا منابع لازم برای مشارکت در یک تلاش دریایی قابل توجه را ندارند. وی افزود که واشنگتن همچنان به متحدان خود فشار می‌آورد تا قابلیت‌های خود را تقویت کرده و در دفاع از خود سرمایه‌گذاری بیشتری کنند.
@withyashar</div>
<div class="tg-footer">👁️ 92.1K · <a href="https://t.me/withyashar/16525" target="_blank">📅 22:26 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16524">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">⚠️
ادمین کانال تلگرامی به نام کیان ملی در تاریخ ۵ خرداد(۲۶ می) دستگیر شد و  از تاریخ ۱۷ خرداد(۷ ژوئن) این چنل توسط افراد اطلاعات سپاه کنترل میشود و مطالبی ضد انقلاب شیر و خورشید منتشر میکند. به هیچ وجه به این چنل دایرکتی نفرستید و از آن خارج شوید.
⚠️
@withyashar</div>
<div class="tg-footer">👁️ 92.1K · <a href="https://t.me/withyashar/16524" target="_blank">📅 21:51 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16523">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/62ca634efc.mp4?token=IYjszd6mCMPwpbLWcpMYJCeSd56fJjN_SawSZ0DNqlqhrNFgIZYEZ6N4q56JELr55H0CQheSIJKZXsfMqyQiCRk9iTn2ygVrxBzzuSbcxsR2uhYP_Rls2u2lUVfXgaVORO3VUqsNiwxsaW3QNYoGSoN1SWvm835pLmpfn22-rbktDIK0i2CpVigYw-JfyGM2qpU4SXQMEdO0pjWe7rFanciJ9HrVhVKv0pCBJfgR0nE9hN_vd7DrJDeZMV9Q9dNTdsJmHIrN9R31pfNJSXwpzTsAXpjWJtCK8N1vbr3emui8rVUk4wgrWrN7N5MxIjPiR-wyKYG8CPJYCucKim-cfU2aY7i6S5LQ7eJMRA6UCJ2zJp1YuZndMjgCtMoOH-IJN8W8VLMj99pOAKSVxcui67DCH5j4qk_PrXAVAS8V4AU0ykWX0OUAm6GUm8d0OzDDsR_M52KNcAcHSqxhpZpaQ27Y0us6UWIR693jPtZIivW0AqREjqQTa6p03OzX9quxi2OxvFsE26KiymuupEdWOoZj64UdWem2877HmFYCuqWhirPNrXd4Zp8fDSjISjmK_daC1fTZZllkVz1zEmqm7bUP2VU-iQjcueyKfPbq7xgdAwZpgETgB0Sw_3sVrs83blAaBQr4HMbEbiy0imPR5v8qUlL6jbMSuP-hhePLBRs" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/62ca634efc.mp4?token=IYjszd6mCMPwpbLWcpMYJCeSd56fJjN_SawSZ0DNqlqhrNFgIZYEZ6N4q56JELr55H0CQheSIJKZXsfMqyQiCRk9iTn2ygVrxBzzuSbcxsR2uhYP_Rls2u2lUVfXgaVORO3VUqsNiwxsaW3QNYoGSoN1SWvm835pLmpfn22-rbktDIK0i2CpVigYw-JfyGM2qpU4SXQMEdO0pjWe7rFanciJ9HrVhVKv0pCBJfgR0nE9hN_vd7DrJDeZMV9Q9dNTdsJmHIrN9R31pfNJSXwpzTsAXpjWJtCK8N1vbr3emui8rVUk4wgrWrN7N5MxIjPiR-wyKYG8CPJYCucKim-cfU2aY7i6S5LQ7eJMRA6UCJ2zJp1YuZndMjgCtMoOH-IJN8W8VLMj99pOAKSVxcui67DCH5j4qk_PrXAVAS8V4AU0ykWX0OUAm6GUm8d0OzDDsR_M52KNcAcHSqxhpZpaQ27Y0us6UWIR693jPtZIivW0AqREjqQTa6p03OzX9quxi2OxvFsE26KiymuupEdWOoZj64UdWem2877HmFYCuqWhirPNrXd4Zp8fDSjISjmK_daC1fTZZllkVz1zEmqm7bUP2VU-iQjcueyKfPbq7xgdAwZpgETgB0Sw_3sVrs83blAaBQr4HMbEbiy0imPR5v8qUlL6jbMSuP-hhePLBRs" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">صداوسیما : انتقام رهبر شهیدمون رو توی بازی ماینکرفت از آمریکا و اسرائیل بگیرین و فیلم و عکساشو برامون بفرستین @withyashar
😂</div>
<div class="tg-footer">👁️ 94.5K · <a href="https://t.me/withyashar/16523" target="_blank">📅 21:45 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16521">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">⚠️
ادمین کانال تلگرامی به نام
کیان ملی
در تاریخ ۵ خرداد(۲۶ می) دستگیر شد و  از تاریخ ۱۷ خرداد(۷ ژوئن) این چنل توسط افراد اطلاعات سپاه کنترل میشود و مطالبی ضد انقلاب شیر و خورشید منتشر میکند. به هیچ وجه به این چنل دایرکتی نفرستید و از آن خارج شوید.
⚠️
@withyashar</div>
<div class="tg-footer">👁️ 100K · <a href="https://t.me/withyashar/16521" target="_blank">📅 21:10 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16520">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">ترامپ در تروث : از فیفا به خاطر انجام کار درست و لغو یک بی‌عدالتی بزرگ متشکرم! @withyadhar</div>
<div class="tg-footer">👁️ 95.1K · <a href="https://t.me/withyashar/16520" target="_blank">📅 20:57 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16519">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GBJKPWHBR4YfVyvd-MDeIBVxiywAd6BZxjZXBKUcWTeYv9tNzpr7QkFpIqT1qDpBsWreYRnrOuI0fdcgBIsnr3h1NaGn90ngZs_eDpBXa9WmeFC8OpBQzpFcicEXNuji8-dGevTAgF6Il5sfheX5vRFPSNYj2MXtxNZogR-7vm4xPvRK2UKWbMTPb-eB4ESeJnLxg7UsznAhiZ5r9uBZO_hnxX0G-E9V2Auzvgmr3yRn6FLpl3CttcivT1j8iOyC7DYoHyQRNlpKLcbZJ6vLMm1WPslMsASItJ5q_UWdN3T7qQ-10pE1N30i300NWMf8tA7gXe4U3Z0rbnYh2QlhAw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ در تروث : از فیفا به خاطر انجام کار درست و لغو یک بی‌عدالتی بزرگ متشکرم!
@withyadhar</div>
<div class="tg-footer">👁️ 93K · <a href="https://t.me/withyashar/16519" target="_blank">📅 20:54 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16518">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">کاخ سفید : ترامپ قراره تو اجلاس ناتو با جولانی دیداری داشته باشه
@withyashar</div>
<div class="tg-footer">👁️ 90.3K · <a href="https://t.me/withyashar/16518" target="_blank">📅 20:52 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16517">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">گزارشهایی از مشاهده یک شیع‌ ناشناس  نورانی با سرعت بالا در‌ آسمان تهران
@withyashar</div>
<div class="tg-footer">👁️ 90.6K · <a href="https://t.me/withyashar/16517" target="_blank">📅 20:51 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16516">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IGnjOAIveHzAIxe7oZt2jnwqcv1cUICkB9n6v3e45Lwv5wf55GSpUQQhycHYyQr3lJvSqp-88_6GIaCyMcpj0IdJ9U7heCJd1hfqJWlB1JBpepJzldqMluqrRKwphpVm7b077-_-sft9WZE2geE41S5Hhb_IHbDGlJlapKcn9fm0O7Hw-W188S52Zvx7Z-iS90SpijdW5xz9DInkDITt1OxY33DiWOt6ylaNRqS2IngPUuNG2V4bIWC3x-DKFuLwiUzALhTMn3zTTPgB3oeZRLXW_49VeugVkCjhkoL9xdT2PJmCSRP-uZ-OLZUPw7Uxs8H5dvJBM0NocF-_Natq_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">صداوسیما : انتقام رهبر شهیدمون رو
توی بازی ماینکرفت
از آمریکا و اسرائیل بگیرین و فیلم و عکساشو برامون بفرستین
@withyashar
😂</div>
<div class="tg-footer">👁️ 98.5K · <a href="https://t.me/withyashar/16516" target="_blank">📅 20:02 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16515">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">تنگه دعوا شد
🚨
🚨
🚨
🚨
🚨
گزارش انفجار سیریک
🚨
🚨
🚨
🚨
@withyashar</div>
<div class="tg-footer">👁️ 92.4K · <a href="https://t.me/withyashar/16515" target="_blank">📅 19:56 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16514">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">هرجاى اين كشور بگى نور به قبرش بباره همه ميفهمن كيو ميگى؛ هرجا هم بگى ريدم به قبرش، باز همه ميفهمن کيو ميگى.
@withyashar</div>
<div class="tg-footer">👁️ 91.4K · <a href="https://t.me/withyashar/16514" target="_blank">📅 19:45 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16513">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GoVR5TkspQxqzMAcC200gGNoaVKyGsD40OXZd0jQqrm_dAsU_eElTzfi7AcBbeo_4fV46ySeo33NVjtJwlfdCJRuc-aSNOjIBuoaVKy8HIbT2pu5vmhjGPv2m3Wt2Q_pacBXpGMpgLye97oxH_MliBX2G1n2vuP769bVQcAVgeyD2d5wCWtUxJMtI9gtuqIrbuLPdFuOyvU909Fpf485APnUMJbFbVTtkkju2up23COlclHKgUUKOn_iDE4UV9YhtLR3E4WtZUZS4GoCQIxLz6WDeU8HWHnLMJk4HtZ7S3YNYHF-9puJ0_TLL-5lJ6cYbiKOpTsQKWQak7vvIJ37AA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">محسن امير اصلانى سال ٩٣بخاطر اين نقاشى و توهين به حضرت يونس اعدام شد.
@withyashar</div>
<div class="tg-footer">👁️ 93.3K · <a href="https://t.me/withyashar/16513" target="_blank">📅 19:41 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16512">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PR3FVK2UcR7P15ts5cpL-hp20jHV6KNcz72PFV-4r06FTVFe3tn3d68fOvhTisFhhssJkCn45ETk6co0BuXoL1aWjS3ZI5sDBWKXGgYw_RC0X9qyjNtt9JeuCMW5PvyECN1t9MtZeh1oGr70M7u3dNh_a0hVEPhs087_tZZ4QY7TEtvvIB3tIB-tuWrjevEaySAW_4OYIpxauahc5PuJG5HjcyeWLGBYCs4zMzpNyr2GrnkOA32z9bn5Ne2YaDe2gJbcYOGz31UgoUM9ZlRuYSN4RYhlXA09bzoHPzh1sOWaMdML2a-KFqJEw4m18jqsnmybbE3xqDAAgpSFYupuUQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یک حادثه در فاصله ۳۰ مایل دریایی جنوب غربی الحدیده، یمن. یک کشتی باری، درخواست کمک ارسال کرد و اعلام کرد که مورد حمله مهاجمان مسلح ناشناس قرار گرفته است. @withyashar</div>
<div class="tg-footer">👁️ 86K · <a href="https://t.me/withyashar/16512" target="_blank">📅 19:10 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16511">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/l9zJ-1JKoBzQNtVT9kYIs19GuzRFwCvca0QfuKPMSDcUMFpoFmkQ8NAth5TjM1EZ-TYsUUa2oSes6W6bMGr0yTRDy-TPAk2mF3hKEqLLuilLHtl9Mptbv7MzZas4kuF0h9NY_UyQz3h-j6HlARds4yQdoejQ1Fs9OSEeI2JahQRAzIx6Pb9OtkN65ILoFu462r-aORDo7S17Zc-K0NEqxTnTcIhsW1upQ-yTzsx-ff-RdWgxjobdszQwud79F0xXQnEfSB6AOSx_TxsaCaxPwLdFbOFQTj5f37hAbSLgSXlK3i2KUJNdXSiCerd8D1eG1NVpeTLg-C0AdZey3H1TJg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مجتبی با صدور حکمی، غلامحسین محسنی اژه‌ای را بار دیگر به عنوان رئیس قوه قضائیه منصوب کرد.
@withyashar</div>
<div class="tg-footer">👁️ 86.4K · <a href="https://t.me/withyashar/16511" target="_blank">📅 19:08 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16510">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">نیروی دریایی آمریکا: عملیات جستجو برای یافتن سرنشین مفقودشده در پی سقوط بالگرد در دریای عرب در یکم ژوئیه متوقف شد.
@withyashar
یاشار : خبر‌ سقوط بالگرد دوم الان فیک نیوز است</div>
<div class="tg-footer">👁️ 85.1K · <a href="https://t.me/withyashar/16510" target="_blank">📅 18:57 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16509">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">نتانیاهو به شبکه خبری فاکس نیوز:
ایران، چه با توافق و چه بدون آن، هرگز به سلاح هسته‌ای دست نخواهد یافت.
@withyashar</div>
<div class="tg-footer">👁️ 89.5K · <a href="https://t.me/withyashar/16509" target="_blank">📅 18:45 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16508">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ctgokfy520xbjVvWaMYtprlIbyC0pbBaCVtY1iCHln_cABPBD8UjZL2pq8Liy4Ijo4Z81WR7JPmHE8cMnqM38z6Gc5NxzQWm9lOEK2AQCzA20yEABBPap8F5lNEqTfVycfQfQZ9DKPSxWJ2hyDZSbEdPAh6NC-EQc8Zs_icIdEbotC3rYNMwt-F0mzhLVlJl4AHdHIWQlqQ3DDCao68QgFHflGLacp7DAuMiWcWg8RkcgFN-1EImCbJCgdAkiFAgEc9gDUa-pIlfVtiEfY5OdkLeX2z-7CN2rNmwgfzch5TEfy9Mo2OK94eC1MGMzwhAAhe0j3qhXre9MYxMlqTDdA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ناو هواپیمابر آبراهام لینکولن امروز مشاهده شد  به‌همراه یک نفت‌کش پشتیبانی (که در تصویر دیده نمی‌شود) و یک ناوشکن، در مختصات:
22.2521, 60.8321
حدود ۱۰۰ کیلومتر دورتر از سواحل عمان ، در دریای عرب؛ که احتمالاً نشان می‌دهد توافق برای کاهش تنش در عبور از تنگه هرمز با ایران  همچنان پابرجاست.
@withyashar</div>
<div class="tg-footer">👁️ 94.6K · <a href="https://t.me/withyashar/16508" target="_blank">📅 17:51 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16507">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">خبرگزاری های اسرائیل :امروز ثابت شد که این فرد به اسم ابراهیم ذوالفقاری وجود خارجی نداره و با هوش مصنوعی ساخته شده. چون حتی احمد وحیدی فرمانده سپاه هم توی مراسم حضور داشت ولی خبری از این نبود
@withyashar</div>
<div class="tg-footer">👁️ 88.8K · <a href="https://t.me/withyashar/16507" target="_blank">📅 17:36 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16506">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">اتاق جنگ با شما : یاشار جان سلام
امروز تو مصلی بعد از پایان نماز ، بلندگو ورود مجتبی رو اعلام کرد اما بلافاصله هم صدای مجری قطع شد و بلافاصله آنتن ها برای مدتی قطع شد...
@withyashar</div>
<div class="tg-footer">👁️ 89.4K · <a href="https://t.me/withyashar/16506" target="_blank">📅 17:35 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16505">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">کانال ۱۴ اسرائیل : اطلاعات جدید نشان می‌دهد که نیروی قدس ایران واحد جدیدی به نام «
مختار
» تشکیل داده است که با کارتل‌های مکزیکی و ایرانیان خارج از کشور برای توطئه ترور رئیس جمهور ترامپ و دیگر مقامات آمریکایی همکاری می‌کند.
@withyashar
🚨
😂</div>
<div class="tg-footer">👁️ 92.6K · <a href="https://t.me/withyashar/16505" target="_blank">📅 16:43 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16504">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">فرودگاه بین‌المللی بندرعباس عصر امروز با فرود نخستین پرواز مسافری از مبدأ مشهد، پس از چهار ماه وقفه، رسماً فعالیت دوباره خود را آغاز کرد.
@withyashar</div>
<div class="tg-footer">👁️ 90.9K · <a href="https://t.me/withyashar/16504" target="_blank">📅 16:33 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16503">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5d4a6d9f34.mp4?token=Akx_MaDcTEgTL39Uy01zBtFjFe18N0z0GuFiEDxichxU6pmrBGR-bjwd9sm_fEqocRGkRnXN1g9zs4VwAsi13yf4W9K8L_ATtOuDbgyjh1EhjlGJ4bhtXbEs7cAOBb2dHr1VEESW1sUMIXDH-MG1h3m_RbAsLoJkVThdFbGK8HZXmqpg9sk0qW2bO4PMAAmbS1tir6KvzDxpti9yBqFSb_WaH15XKtPM5A7KAQj8DK_fe5Nevg6wN3PIssQuCNyrWehoA_zCANuVWVm16_fhQ1uIVWxDnRdrE0cdr4NSy_eBMCQ3Q2o6e8HavBtzGj5R79VrXZuf336OgFGDgkto4w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5d4a6d9f34.mp4?token=Akx_MaDcTEgTL39Uy01zBtFjFe18N0z0GuFiEDxichxU6pmrBGR-bjwd9sm_fEqocRGkRnXN1g9zs4VwAsi13yf4W9K8L_ATtOuDbgyjh1EhjlGJ4bhtXbEs7cAOBb2dHr1VEESW1sUMIXDH-MG1h3m_RbAsLoJkVThdFbGK8HZXmqpg9sk0qW2bO4PMAAmbS1tir6KvzDxpti9yBqFSb_WaH15XKtPM5A7KAQj8DK_fe5Nevg6wN3PIssQuCNyrWehoA_zCANuVWVm16_fhQ1uIVWxDnRdrE0cdr4NSy_eBMCQ3Q2o6e8HavBtzGj5R79VrXZuf336OgFGDgkto4w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">همچنان حملات سنگین اسرائیل در جنوب لبنان
@withyashar</div>
<div class="tg-footer">👁️ 90.2K · <a href="https://t.me/withyashar/16503" target="_blank">📅 16:04 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16502">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6f20cf4d81.mp4?token=sdcjghkmhpE7uzmpQZB44MgA36le3ql4su_SPh6Ad0ZHS2VzQ2DJ7Q3Bxo4bEAwjJdgEsNWxFAMBvBSP-xcd7i8j81JF5sKec-QDsusfqN-2G35mla_bVbhRnsQ4oNP6dM36WNVVaBv0BNUuOkyE0n-Xg6wtlSfMaSKbyTZcfKhIfu_Jf9vCdmVoOT9F1O4TRtihUYHTSBvz1m_fLuTXj9vXql0G8MEy5erJPUERXq0txPjvjCj6WOmt_yiZSNVPngLzrfjBISLqFG1lknjQ1JF9V_rF1Labs2xBEcQz4zw51OWUA9w0SFu0Nyhm7Ojg5favYf4tI7GhvV8MSNKG2w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6f20cf4d81.mp4?token=sdcjghkmhpE7uzmpQZB44MgA36le3ql4su_SPh6Ad0ZHS2VzQ2DJ7Q3Bxo4bEAwjJdgEsNWxFAMBvBSP-xcd7i8j81JF5sKec-QDsusfqN-2G35mla_bVbhRnsQ4oNP6dM36WNVVaBv0BNUuOkyE0n-Xg6wtlSfMaSKbyTZcfKhIfu_Jf9vCdmVoOT9F1O4TRtihUYHTSBvz1m_fLuTXj9vXql0G8MEy5erJPUERXq0txPjvjCj6WOmt_yiZSNVPngLzrfjBISLqFG1lknjQ1JF9V_rF1Labs2xBEcQz4zw51OWUA9w0SFu0Nyhm7Ojg5favYf4tI7GhvV8MSNKG2w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حملات اسرائیل به جنوب لبنان
@withyashar</div>
<div class="tg-footer">👁️ 87.2K · <a href="https://t.me/withyashar/16502" target="_blank">📅 15:43 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16501">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hWLYHXSPH_LEPUS4gxiil5yCWTRuLYMtHGBGDM5v7T1upkn0KOqu4pwX5YBwuErXQivLhUXFvujuJdrjAPQo5uDacU1i0B79zpfiiG6COsNqd0ZprjCJl4b0TlVth3tos02tD6_gBCsE_EtQhob9XKuudYhzJA58yeT6GyDA7kLuQ9x-anzsy9bZLrmX7bBd5pS83Di50GHaD6zHC8lZeUpiqEk9Tw1I7THLg_fuJOYAtk-RsQerDp2F7zpkEuXW10k7PYD7cZCiffh6LyGukR2PIff5N5t-yw-Q7Cp11d9NKrs-uNAWztQcQ6HGsavl4H8m3tYlWlLfHJB0CNb9Pg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پست وزارت خارجه اسرائیل به مراسم تشییع علی‌ خامنه‌ای
@withyashar</div>
<div class="tg-footer">👁️ 86.7K · <a href="https://t.me/withyashar/16501" target="_blank">📅 15:42 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16500">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KeMLZk6JP2yblaZ6cOnEMfjsgXY8VJ_QOpYds5zzVnSSbpgsWjYPylZS6RejlDUjxfKgAwLukNn_i5qD_jbP-xpKjjjb-kkX7cIAWBZTRkbWFrBdGQekEgoLKVZ34ZcefOS0pGdTZcg4026zI-buGGhtxd1UmGHDcM43df5tqRl2Sbk60tL5mpYV8u-oc1_iXJiK3SjI2Y_ihoji8k_wkn7g_7nGs7d2PmJ_J8M-eH_QtINKPasB3HhC2CBRExJsbVYxcYTUJvLgT7RMoOw-3qeIyLzmGScWGrhbvIgZisgI0lhmclIA7OtEtAc0_4y9WK-tH_Db4f5HYmm_iVaCDw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ در تروث : از زمان آغاز جنگ در ایران، بیش از 273 آمریکایی در شیکاگو هدف گلوله قرار گرفته‌اند
😳
@withyashar</div>
<div class="tg-footer">👁️ 84K · <a href="https://t.me/withyashar/16500" target="_blank">📅 15:39 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16499">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b892031853.mp4?token=UmFMFtYeZ-dj-Njg0IIp2ddmVRX7cKr_fFzL4Ty11yVM2_iAzqGuefR_W5oSEOvFWWXT1x4ZQJcNQRHPmGP8uq84ytvzVUmQAfJkqTAdbBpX4WINkx-teD0-_11qjCFEUY_vOCenB0JRNxrJM8DSXqJ0-vuWyGkPLDcgK_eXeqtBXLsz72naAXEEt7C3EeJKk8cK3uudAwq25hQ2wm-fkfZV0nNNaU4dWSPIXKehwZs5rQmTStoWdS0lLRVz81OPESbZEr_erfKIfpbaB985w2q3BFhs0Afg0cmDCJdRpKfEjbpQMHpvWEvXYly9GcNvwX3s6g0ufPEx3wloSBlI8g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b892031853.mp4?token=UmFMFtYeZ-dj-Njg0IIp2ddmVRX7cKr_fFzL4Ty11yVM2_iAzqGuefR_W5oSEOvFWWXT1x4ZQJcNQRHPmGP8uq84ytvzVUmQAfJkqTAdbBpX4WINkx-teD0-_11qjCFEUY_vOCenB0JRNxrJM8DSXqJ0-vuWyGkPLDcgK_eXeqtBXLsz72naAXEEt7C3EeJKk8cK3uudAwq25hQ2wm-fkfZV0nNNaU4dWSPIXKehwZs5rQmTStoWdS0lLRVz81OPESbZEr_erfKIfpbaB985w2q3BFhs0Afg0cmDCJdRpKfEjbpQMHpvWEvXYly9GcNvwX3s6g0ufPEx3wloSBlI8g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خنده های زننده و گرم گرفتن ملعون وحید خزائی با یکی از عوامل مهم کشته شدن ۴۲،۰۰۰ جاوید نام ،  فرمانده کل انتظامی جمهوری اسلامی احمدرضا رادان
@withyashar</div>
<div class="tg-footer">👁️ 86.7K · <a href="https://t.me/withyashar/16499" target="_blank">📅 15:11 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16498">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">نتانیاهو : حرف‌هایی که درباره درخواست ترامپ برای حمله نکردن به تونل‌های لبنان پخش شده
کاملاً دروغه، ترامپ اصلاً چیزی رو به من نگفته
منم چنین درخواستی ازش نکردم و ما تصمیم‌هامون رو بر اساس ملاحظات خودمون می‌گیریم
@withyashar</div>
<div class="tg-footer">👁️ 83.4K · <a href="https://t.me/withyashar/16498" target="_blank">📅 14:44 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16497">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XC1o49bysAqSS0U2d_plsWHAO2Oal2Ahv4_3wz1OwPbH8pHRLE7gQDzF4e1xrkxYwGqQWZ14b2PbyvfODcBK1XHOg8PHnqioTRULRc1dwYlfhPtenvQXVPEJeRSpfGu-yJcV36jnYXq6zLhamFDid8uVSPj7qdekyK47Zwc2SBJpPurdVEAbYqiJOgph85wC1wHL0bOBSew3qI-ZPjsS2TxF0VBCMEMtVryMk4ymreQCApJIRKnIHLyD6xxNyI3k-pTj0659grNBVZqA5DYki7CC9c_FUpI1_4ePD7auSaN9NI5h-KeOhwTOy3CDpsobogmYHdq43XS5fP1S0Mqesg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یک جت دولتی ایران از مسکو برگشت و هم اکنون بر روی باند فرودگاه مهر آباد تهران به زمین نشست
@withyashar</div>
<div class="tg-footer">👁️ 86K · <a href="https://t.me/withyashar/16497" target="_blank">📅 14:32 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16496">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jJFLD4p_QzM5Hvw4AMl3fu9brx2NBjRmeE45_3IOY-vOLAZaexKBT1NXhIb8ux-96M1BjMKvrvxThC5h1axLNzjQkgyX6z9K3mZ74lTZpHiCPnK1Ie39kt26B_-OV1aI56tC3jUrm_vuclAb7PMCSf2kkcKFPbt7-87pBcMtF3r3EiqRD1Ng4K9FHS5jHgFjbWfU5koXodD_-UabdS9vd3jYg0xVeSJ2ZKhaqgjBKnQxKaaH44Y2T7PUndS26r4_RORW8puNsvIc3A_5Xw50M5tWHgH3F8oKF25oLGfixBctJUszQj39KHbQEGNiuEi2P9daskLUyRFnqWaM0kYSZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">همونطور که در ویس دیشب اشاره کردم که منارههای مصلی یکسان نیستند، در این تصویر هوایی هم کاملا مشخص است که ایده طراحی این بنا کاملا از سنگ توالت برداشت شده.
@withyashar</div>
<div class="tg-footer">👁️ 88.6K · <a href="https://t.me/withyashar/16496" target="_blank">📅 14:16 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16495">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">کانال ۱۴ اسرائیل : احمد وحیدی، فرمانده کل سپاه پاسداران، که تحت تعقیب اینترپل، تحریم‌شده توسط ایالات متحده و در فهرست اهداف اسرائیل است، دوباره در روز دوم تشییع جنازه خامنه‌ای دیده شد.
@withyashar
اتاق جنگ با یاشار : موساد این روزا حسابی سرش شلوغه و لیست جدید ترور‌ رو داره آماده میکنه تا هفته دیگه بی بی برای تایید پیش ترامپ ببره</div>
<div class="tg-footer">👁️ 85.4K · <a href="https://t.me/withyashar/16495" target="_blank">📅 14:11 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16494">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">شاهزاده رضا پهلوی : ‏تلویزیون بی‌بی‌سی فارسی در صفحات رسمی خود، با انتشار بخش‌هایی تقطیع‌شده از گفت‌وگوی هایم، تصویری نادرست و گمراه‌کننده ارائه کرده است.
@withyashar</div>
<div class="tg-footer">👁️ 87.3K · <a href="https://t.me/withyashar/16494" target="_blank">📅 14:08 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16493">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">کان نیوز : در اسرائیل معتقدند وقوع یک درگیری نظامی مجدد با ایران در آینده نزدیک وجود دارد.
@withyashar</div>
<div class="tg-footer">👁️ 87.7K · <a href="https://t.me/withyashar/16493" target="_blank">📅 13:49 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16492">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SNIugWSaB7EasyckQvKu-7DWYHPTSHQetXCbN7yEKPLkLBCF_9JbXzjBNDbrg_wTUgAxIpDl8TLn1lLpknlmA5MhCCM8QPoo3C5V2jf6QY8DxN2CPaRUb5sFtgFyC7_6AVrsB7ui1jIJbiQTJ_EEzzhSztUhj3HzflJpHcYdd8Wm6GJpiFrFyyxzbB-Gud9Zw_Z2ZWZPHLh3peHccOBY9c4KZzM56ecKVYbWfQOn8Gi4d6xmUL7imj1fbdeHJUhnFkLoKvCML4h-MKd6cKEiFbm4Gt5FXA4tZH_823vQn5QGsyWUJ-m7_1-9nnnCZnpIMXWKHb_M6Or7J4JcUDNr7w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هشت هواپیمای تهاجمی A-10C Thunderbolt II که در خدمت وینگ ۲۳ ارتش آمریکا هستند، از پایگاه هوایی RAF Lakenheath به پایگاه هوایی موفق سلتی در اردن اعزام شده‌اند @withyashar</div>
<div class="tg-footer">👁️ 90.2K · <a href="https://t.me/withyashar/16492" target="_blank">📅 13:34 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16491">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">ارتش اسرائیل : دو فرمانده حماس در حملات  هوایی به غزه کشته شدن   ارتش اسرائیل به عملیات خود برای رفع هرگونه تهدید فوری ادامه خواهد داد @withyashar</div>
<div class="tg-footer">👁️ 85.8K · <a href="https://t.me/withyashar/16491" target="_blank">📅 12:55 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16490">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/m6A--0gqclq2kfSaF9MtEa7eyljlTnppY-awwjOFxj3qdVg3yT1FUzkM5sdHNO_XMx3MfOA_1SvnEqGxxb8mUBIik6fDJ2U0TTZnz8TKyHDdDJWu8U1zorbhjO_0QVi9oc4j0qlJLPummsjZRhFS2XsNO5MgsxqAw7I5vrtWKUcPEffo7T1VoF6r1dnAamW68a084m1z6SWcMu5NQx2VhMbqHwIsN-arCMi00uOz4nJaBhKvE5xOCBvQiMQK6tEv_YXZ85VHDxTE7oCJ4lAO2tdijKUYhrTjLfG4vVEvD-dLSzESz1F5YzabtsG3VMKJELyQJ7Jj5ckDkMUOgutExA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یک حادثه در فاصله ۳۰ مایل دریایی جنوب غربی الحدیده، یمن. یک کشتی باری، درخواست کمک ارسال کرد و اعلام کرد که مورد حمله مهاجمان مسلح ناشناس قرار گرفته است.
@withyashar</div>
<div class="tg-footer">👁️ 86.9K · <a href="https://t.me/withyashar/16490" target="_blank">📅 12:44 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16489">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">کانال 15 اسرائیلی: جلسه فوق‌العاده کابینه سیاسی-امنیتی به روز سه‌شنبه موکول شد. انتظار می‌رود جلسه کوچکتر کابینه امشب برگزار شود.
@withyashar</div>
<div class="tg-footer">👁️ 82.7K · <a href="https://t.me/withyashar/16489" target="_blank">📅 12:42 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16488">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d92ffd63b9.mp4?token=TP_tX9oS7Okl_g-RVyxe87ijiHgtAGe-e3DLm3KwpKvIdEg4mKp_k6-U2aRGGKXMnHkj_2BSZCl3FWQYvRp8Kup3ZDlil9HA97gSKQLp1_S-7hSmKx7SvvfV__bpPO5aP4Fz6vhEQ-mwmU8lkbAR80SnZFbwtBbYuCnMU7J2l2DgHaqAlkBr4tPc9LeOb--aAPJuAaQ8mnyUQlW-KY864KrGLDg_oSaquvY6iy9u4ze3DvWiGZ3ItAqvJZHDTE_x_16uOPHvJBxTQU8g8E2aKKu92lLD1OQ-32coxmnUCX5OBid-SGam51BKG-5AjybQVbA0LOAPpeNXCDk2oYxz7Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d92ffd63b9.mp4?token=TP_tX9oS7Okl_g-RVyxe87ijiHgtAGe-e3DLm3KwpKvIdEg4mKp_k6-U2aRGGKXMnHkj_2BSZCl3FWQYvRp8Kup3ZDlil9HA97gSKQLp1_S-7hSmKx7SvvfV__bpPO5aP4Fz6vhEQ-mwmU8lkbAR80SnZFbwtBbYuCnMU7J2l2DgHaqAlkBr4tPc9LeOb--aAPJuAaQ8mnyUQlW-KY864KrGLDg_oSaquvY6iy9u4ze3DvWiGZ3ItAqvJZHDTE_x_16uOPHvJBxTQU8g8E2aKKu92lLD1OQ-32coxmnUCX5OBid-SGam51BKG-5AjybQVbA0LOAPpeNXCDk2oYxz7Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">رسانه های رژیم ویدیویی از حضور احمد وحیدی در تشییع جنازه نشان دادن. به نظر میرسد در صحنه ای که کات میخورد بر‌اثر هجوم و درگیری‌ بادیگارد ها  کلاهش می افتد.
@withyashar</div>
<div class="tg-footer">👁️ 88K · <a href="https://t.me/withyashar/16488" target="_blank">📅 12:20 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16487">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">گزارشی درباره یک حادثه تیراندازی در آمریکا
: طبق گزارش شبکه خبری ABC، حداقل هشت نفر، از جمله چهار کودک، در کونی آیلند، ایالت نیویورک، در جریان جشن‌های روز استقلال آمریکا مورد اصابت گلوله قرار گرفتند.
@withyashar</div>
<div class="tg-footer">👁️ 81.8K · <a href="https://t.me/withyashar/16487" target="_blank">📅 12:12 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16486">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">زمین لرزه شدیدی شهرستان بستک در غرب هرمزگان را لرزاند
@withyashar</div>
<div class="tg-footer">👁️ 83.5K · <a href="https://t.me/withyashar/16486" target="_blank">📅 11:57 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16485">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/37255614f1.mp4?token=iaZS-eHG2y1MTtH6fzjmsp06bH63iolG3J4ifGnxpkTc_7CPa6dmXIgZtEW0TLYCXKXK_k_nyBizp5FqpSZGahJt9pqz_jvsz_lZ5WfhyjUoF7MGUsBzRJv4Mk_CXGfYn3zh2o8CZM2IWJ3yzSYEnoWA5pjgffICFW0sFFcPE2BUksaDLjv0tWt49hP9_7gO3brfOnIAQ1mejS8zn0yB8_0i-bnGRT-iAPSXsi4VD8qxUnzcquAN0QWvyH_0N2lv_e_QOBBOdDk9soQoBVJCw2VJk7r0yUKfSVfu483VVNvr1ry4X8wGkvN7sXv-GofdKWHCy4aL-ts0lENoVixyKg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/37255614f1.mp4?token=iaZS-eHG2y1MTtH6fzjmsp06bH63iolG3J4ifGnxpkTc_7CPa6dmXIgZtEW0TLYCXKXK_k_nyBizp5FqpSZGahJt9pqz_jvsz_lZ5WfhyjUoF7MGUsBzRJv4Mk_CXGfYn3zh2o8CZM2IWJ3yzSYEnoWA5pjgffICFW0sFFcPE2BUksaDLjv0tWt49hP9_7gO3brfOnIAQ1mejS8zn0yB8_0i-bnGRT-iAPSXsi4VD8qxUnzcquAN0QWvyH_0N2lv_e_QOBBOdDk9soQoBVJCw2VJk7r0yUKfSVfu483VVNvr1ry4X8wGkvN7sXv-GofdKWHCy4aL-ts0lENoVixyKg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ارتش اسرائیل : دو فرمانده حماس در حملات  هوایی به غزه کشته شدن
ارتش اسرائیل به عملیات خود برای رفع هرگونه تهدید فوری ادامه خواهد داد
@withyashar</div>
<div class="tg-footer">👁️ 84.5K · <a href="https://t.me/withyashar/16485" target="_blank">📅 11:56 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16484">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UQtIv7mofuQLcbtjv5qUIi0-y76Qv4Deyz6nYLdQQ2d7c0cYDIrS4dW9ZGC4l3oYNk0g0rZwxx4ulrr6WV4HNSzAtm5-sPm74nXs8Fn_QSYXzV2F9mx5oW-GmKCAE7ElstSZNsOd5zFGMOtZRMYHA4TWHJHeWGNRVq-OQHkP1DKu1nMvgmGci2aIEK7r-6K64QDr7fu7egIMlJkCse2Nn1FVNbDkutIRl-GHTQ9d1JPTJdp0lZggg_Yo10LMgaRo66bbU2XpMihTGK7xrEvJegRtPnv_Ipv5_u1tJYwtRHltbR4oTYy-rb-qucHUQH65GSq2AKdyp2MhZGNyfz_vmQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هم‌اکنون با پوشش هوایی و اسکورت سنگین، ارتش ایالات متحده یک کشتی باری (با AIS روشن) را از مسیر عمانی عبور می‌دهد!
این اولین عبور امروز خواهد بود اگر موفقیت آمیز باشد.
@withyashar</div>
<div class="tg-footer">👁️ 84.5K · <a href="https://t.me/withyashar/16484" target="_blank">📅 11:37 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16483">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">قایق‌های تندرو سپاه، مسیر عمانی را بستند
هرمزلتر: نیروی دریایی سپاه با استفاده از قایق‌های تندرو، کریدور مورد حمایت آمریکا در تنگه هرمز را به طور کامل متوقف کرده و در نیم روز هیچ شناوری از این مسیر عبور نکرده.
سپاه صبح امروز از طریق بی‌سیم به تمامی کشتی‌ها هشدار داد و همزمان قایق‌های گشتی نیروهای ویژه را برای اعمال کنترل ایران بر تنگه هرمز مستقر کرد.
@withyashar</div>
<div class="tg-footer">👁️ 83.7K · <a href="https://t.me/withyashar/16483" target="_blank">📅 11:33 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16482">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">کامیونت یخچالداری که جنازه علی خامنه ای را حمل میکرد، گویا خیلی عجله داشته. ۲،۳۰۰ هم جریمه شده. @withyashar</div>
<div class="tg-footer">👁️ 84.9K · <a href="https://t.me/withyashar/16482" target="_blank">📅 11:27 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16481">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">فرمانده نیروی قدس، اسماعیل قاآنی، و فرمانده سپاه پاسداران انقلاب اسلامی، احمد وحیدی، هم امروز در مراسم تشییع جنازه خامنه‌ای حضور داشتند.
@withyashar</div>
<div class="tg-footer">👁️ 83.7K · <a href="https://t.me/withyashar/16481" target="_blank">📅 11:22 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16480">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">سخنگوی ارتش ایران: از فرصت آتش‌بس برای تقویت توانایی‌های نظامی خود استفاده می‌کنیم و لحظه‌ای را برای این کار از دست نمی‌دهیم.
@withyashar</div>
<div class="tg-footer">👁️ 83.6K · <a href="https://t.me/withyashar/16480" target="_blank">📅 11:19 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16479">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">قطر: فعالیت‌های کشتیرانی به‌طور کامل و فوری از سر گرفته شد.
@withyashar</div>
<div class="tg-footer">👁️ 82.9K · <a href="https://t.me/withyashar/16479" target="_blank">📅 11:17 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16478">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">وال استریت ژورنال: ایران، روسیه و کره شمالی، در نحوه تعامل با بازار ارز‌های دیجیتال، ایجاد رمزارز‌های اختصاصی خود و پلتفرم‌های معاملاتی برای دور زدن تحریم‌ها، بسیار پیشرفته‌تر شده‌اند
تهران و مسکو از ارز‌های دیجیتال برای خرید پهپاد و قطعات یدکی تسلیحات استفاده می‌کنند
@withyashar</div>
<div class="tg-footer">👁️ 84.5K · <a href="https://t.me/withyashar/16478" target="_blank">📅 11:01 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16477">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">گریه های پسران خامنه ای بجز مجتبی @withyashar</div>
<div class="tg-footer">👁️ 82.9K · <a href="https://t.me/withyashar/16477" target="_blank">📅 10:58 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16476">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">نیویورک تایمز: مجتبی خامنه‌ای همچنان در تلاش است تا در تشییع پدرش شرکت کند اما مقامات امنیتی مانع هستند
@withyashar</div>
<div class="tg-footer">👁️ 81.2K · <a href="https://t.me/withyashar/16476" target="_blank">📅 10:56 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16475">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/G18rmSgDHbIZW87AbB4EyYUSzt3AlNpHOQ8rC3OnEBOTtJEyMkzOlb2Fs3ZbQIm5ta7c-8Vj1fEe9AM2LKp1FAD3T5kRc2fQP3tGl3kGBbQJL6DI9EM9BleWo2rW9TVGfrFF4Ye4fCIcdqbpM6YgdhyioL5VpEGKGQUCaEPNmbtkla3aDaYaSyg51dpMeURxAF6RSvh5pIW-ISlkov7_HKgyj_PaPL5oEbzMETSzCoEy_ZazW74aH-JD98zPLqdfrHhx5cZSgx-LBWbGoMjNmKHt1lbtSNY2ryRo3CmB_4kQzwQUrLrLgKBJOMKGwHcrG-mK5Meq3z3rW_jnj5xmrw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شباهت امام جمعه پاوه ( ماموستا قادری ) با ( هاشمی رفسنجانی ) که دایرکت منو منفجر کرد
@withyashar</div>
<div class="tg-footer">👁️ 83.8K · <a href="https://t.me/withyashar/16475" target="_blank">📅 10:54 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16474">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jauzC9se1Z0eYV3GB9fTXhDBuTYxC3bETQYwkr8nCwbTwDyu6eWy_tnD27CwwDiB3N3G9emjKN2neCHqszSAS7k2SfuVJS0UhOBIGKptaw2GVgkn7-vxMn4TBbyVMNKT8AK_yIUBcXlGmdjRBoSt9fGuq0q-48MrlwIY1Qgtw5PRhG14IdF6gwt8vBQdGjwK5M8IjjUaILnLsy60L__ur_F0NBNuVy4Bq4Jn-nKKtD7yLBYwhozqFAyirRSkQDQBvFWQgMJ0xPpb_h5tD5TdlbzXvmQ4V9bs5-J6aUa8due4IzxMpA2_QRqWMOXVUkTRWJfZD1Mbp2jo81G0COgRuA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حضور مصطفی،میثم و مسعود خامنه‌ای ، فرزندان موشعلی ، پس از ماه‌ها دوری از رسانه‌ها  در جلوی دوربین. مجتبی خامنه‌ای دیگر فرزند رهبر پیشین و هم اینک ،  رهبر کنونی جمهوری اسلامی ایران همچنان در رسانه‌ها دیده نشده است! @withyashar</div>
<div class="tg-footer">👁️ 83.7K · <a href="https://t.me/withyashar/16474" target="_blank">📅 10:44 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16473">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2866a3ad1b.mp4?token=CYEaF05yNRsjkq6H6z1bSg3gwWi-Jbu2BUXQm-K66u-ZsJm5iX4u_xDxACSidalTWmD7WfaUZPHtMVhdXrCLZjoNjYnAuaDA4Hw0UiLUFUpqlZ0vhH_q3q9thUXNe6mmWQeR2MN434NJpLyob4AWw1VjmHmWVUwz93p4T97VMpxe-ccQbyppjwqfdmJxG6Xr45Rhj4iz5RJLXhIpseETP8FGcV7rsErAZgADkKpI2PqW4lejiK3Mg4ycaN-PJ_0s54RorUHMoZoG2izV6CQpLmLp5_eCglyDOXRsWT6SzviYlfQjDyVNyHgZByeDtvZmH7m3p2t1BzxMg7jMtOBuiA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2866a3ad1b.mp4?token=CYEaF05yNRsjkq6H6z1bSg3gwWi-Jbu2BUXQm-K66u-ZsJm5iX4u_xDxACSidalTWmD7WfaUZPHtMVhdXrCLZjoNjYnAuaDA4Hw0UiLUFUpqlZ0vhH_q3q9thUXNe6mmWQeR2MN434NJpLyob4AWw1VjmHmWVUwz93p4T97VMpxe-ccQbyppjwqfdmJxG6Xr45Rhj4iz5RJLXhIpseETP8FGcV7rsErAZgADkKpI2PqW4lejiK3Mg4ycaN-PJ_0s54RorUHMoZoG2izV6CQpLmLp5_eCglyDOXRsWT6SzviYlfQjDyVNyHgZByeDtvZmH7m3p2t1BzxMg7jMtOBuiA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گریه های پسران خامنه ای بجز مجتبی
@withyashar</div>
<div class="tg-footer">👁️ 88.6K · <a href="https://t.me/withyashar/16473" target="_blank">📅 10:40 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16472">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">حضور مصطفی،میثم و مسعود خامنه‌ای ، فرزندان موشعلی ، پس از ماه‌ها دوری از رسانه‌ها  در جلوی دوربین. مجتبی خامنه‌ای دیگر فرزند رهبر پیشین و هم اینک ،  رهبر کنونی جمهوری اسلامی ایران همچنان در رسانه‌ها دیده نشده است! @withyashar</div>
<div class="tg-footer">👁️ 91.8K · <a href="https://t.me/withyashar/16472" target="_blank">📅 10:39 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16471">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5a4c290e0d.mp4?token=jQwl6SB_COfgHediUTaAMsbD2-QRWc9Y9Ms0ck3xigJVRkYdPI-WI1cvCjdrvS6OXjZrS3Nh3jcqbVwOwyOD3tubyTLJ6V23L37nNwOu7-m8eKYmPi2d7m_AVsSxi_ojQhyCuQakyWKLWKksE4Ox9au6PJ1bcnwyVCWHyCv1gYkB_FfJUQOqqYnYYR1-tE1c6kBz8uPi2a7UcIcZQHTBRVeNP7-t4NX7JDwifazflE9J_Y-kNN6tvixJ3ZOk9zdxHeou2Qkz5dKPwN1xqdISUBTQ_dhrim_nQmz6lv29Hn0TXxHDMfpE-8qDfSUaNW4hEs5uezrGMJtrepOid-ucBg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5a4c290e0d.mp4?token=jQwl6SB_COfgHediUTaAMsbD2-QRWc9Y9Ms0ck3xigJVRkYdPI-WI1cvCjdrvS6OXjZrS3Nh3jcqbVwOwyOD3tubyTLJ6V23L37nNwOu7-m8eKYmPi2d7m_AVsSxi_ojQhyCuQakyWKLWKksE4Ox9au6PJ1bcnwyVCWHyCv1gYkB_FfJUQOqqYnYYR1-tE1c6kBz8uPi2a7UcIcZQHTBRVeNP7-t4NX7JDwifazflE9J_Y-kNN6tvixJ3ZOk9zdxHeou2Qkz5dKPwN1xqdISUBTQ_dhrim_nQmz6lv29Hn0TXxHDMfpE-8qDfSUaNW4hEs5uezrGMJtrepOid-ucBg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حضور مصطفی،میثم و مسعود خامنه‌ای ، فرزندان موشعلی ، پس از ماه‌ها دوری از رسانه‌ها  در جلوی دوربین.
مجتبی خامنه‌ای دیگر فرزند رهبر پیشین و هم اینک ،  رهبر کنونی جمهوری اسلامی ایران همچنان در رسانه‌ها دیده نشده است!
@withyashar</div>
<div class="tg-footer">👁️ 95.1K · <a href="https://t.me/withyashar/16471" target="_blank">📅 10:07 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16468">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/KcC_Os8zqnCbJzRHa5evUON8MfpLZjLA03HfUQ81r3_gJSBpxqy77qeAkok0Jw9OwLsrQrfHnyPq6S33fcFP5BcJs996L-fwLsKyv8l-XGmfKGeEk794eUZnNYa-7Eero8b-ILu32i0szu6GDYuxi3psBvT0Tq26GX3eQqHVkhYFOWctq1y_EXKEfOCOPJHjQ3heIrKbQdXTzRjP2MCCNGQdo0S-__UR_yYaHuUi5EorlXdbTOzti3w9a9-lMojPSU-2PCP7dA6sGpkmTW1KkV9fNTKCz2kYgL5jO1g1ZpRhUbp18JO7BnsIuopW-lajHCh7jgZn2Y9QiZ_FUatbVw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/gFOTdG5pAegMrXgZiKY-JHnUihJ7-xhoAxpgWuF_pFWUylJes-4fxhyYW45fRpFmCO7E5geNJWFHmuyxMYUZddMb0EewQ3HBYcKzYGRrxubzo-rkk9EE5_4MNW7HHm4dWBUcOsLvpntno4f6sZGxUaVRu2mg3V6Jo277Y09sIwSLBybR8lYaOp-iE5j3lCniTEtvuEX7j9v7eZUUf0Pu6wkzfopTaDUwrmdExY_tvoMr0fYbHzvPSUK2KkCwz_UbtertJplS57q4guFlAGjdhW_nBWUdAdvwSikbo9M_A8ZjLVV1HGkicwJ7dXpC2WX2QGCeKY10smEbJ7-gN2NzSw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/BJUrTla5lNwgn8F2EdRHnFi4MIU23yINK5stnwWDg0hURVdrBLtAmTtzlZw5Y6aju_s-3yfGtuw2k8YJE5bfmcMi5MK7AQWUPbRVSDlKs5F-hwIMTxujm0EWYFKe-Qy6O4bOyJYOzP7-EQ2AM-sjnLQT_QXLvPz9IER5Y0br_I0oTXT2Fd_p8PrzE0xLSfanxeNQEttKPSELrbl2mWiYaeCfYOaXIAvEovJXH3uJTzEkSdgjOdCLrP4XGF9Z0CEDeRUEWiCl5i83qwXKAGWq1hvYbomlv2I53-1T7yKyI1sZXZPftbqlFhZr5yfWbQvJxIczsi2JOG3iL2chPmpo3A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">شهستان پهلوی (ویس قبل رو گوش کنید)
@withyashar</div>
<div class="tg-footer">👁️ 101K · <a href="https://t.me/withyashar/16468" target="_blank">📅 00:43 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16467">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">شَهِستان پهلوی، نام یک مجموعه بزرگ شهری در زمین‌های منطقه عباس‌آباد تهران بود که اجرای آن در سال ۱۳۵۴ در زمان محمدرضا پهلوی شروع شد ولی در طرح آمایش سرزمین ۱۳۵۴ ستیران آرمان‌گرایانه اما ناپایدار و مخاطره‌آمیز برای توسعه کشور و شهر تهران قلمداد شد و با وقوع انقلاب ۱۳۵۷ ایران هیچ‌گاه بطور کامل اجرایی نشد. بخشی از این طرح احداث یک برج مخابراتی مانند برج میلاد امروزی بود
@withyashar</div>
<div class="tg-footer">👁️ 104K · <a href="https://t.me/withyashar/16467" target="_blank">📅 00:40 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16466">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">گزارشهایی از فعالیت پدافند پرند
@withyashar
🚨</div>
<div class="tg-footer">👁️ 104K · <a href="https://t.me/withyashar/16466" target="_blank">📅 00:26 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16465">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">کانال 15 تلویزیون اسرائیل: در‌تماس‌ امروز دونالد ترامپ از بنیامین نتانیاهو خواست اوضاع لبنان را متشنج نکند.
@withyashar</div>
<div class="tg-footer">👁️ 104K · <a href="https://t.me/withyashar/16465" target="_blank">📅 00:25 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16464">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">ارسالی : یاشار جان درود
داداش همین الان از اطراف مصلا برگشتم ، تمام حجم ترافیک و شلوغی برای صف های ایستگاه صلواتی ها و مفت خوری ها بود
یجا مردم بخاطر یدونه تخم مرغ آبپز و یدونه لواش داشتن همدیگرو میزدن همشونم طرفدار اینا
@withyashar</div>
<div class="tg-footer">👁️ 108K · <a href="https://t.me/withyashar/16464" target="_blank">📅 23:07 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16463">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">اکونومیست: جنگ بعدی خاورمیانه بین اسرائیل و ترکیه است
@withyashar</div>
<div class="tg-footer">👁️ 107K · <a href="https://t.me/withyashar/16463" target="_blank">📅 22:55 · 13 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>

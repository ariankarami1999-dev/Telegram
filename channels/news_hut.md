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
<img src="https://cdn4.telesco.pe/file/s6aD9SqDNdRDkR3qA5JqmmXyF8OJG6y2yXKnNUp_jzEMu6OY740KbywtNZYcWkeUQn5LGi_aw01EOG0w9R1PFTgCAifmj853bd3xbvWE9jVt-_OW2q7Ct3s5VW39g0v_INM_E1ScXZ_mCJ4b2CWRyrqHcGuxizlABTv4GptcrWgHHuMUaoJpRLDZwuQigjKFI9I7XaefAXcp_0TWFs68ch8o7hf9F9p4h9tgct-PEE7tX7772As_arjkUNNiZIcWDhRRjdTAvHugJb2OFHSRhgSzpy8aijHy4JZjtnFcvwggksX7oiOpbYwvRCIgjN_FHfolGqTtY6ogkkbF4j0M8g.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 هات نیوز | HotNews</h1>
<p>@news_hut • 👥 104K عضو</p>
<a href="https://t.me/news_hut" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 بدون هیچگونه گرایش و تمایلات سیاسی، همیشه سمت حقیقت و مردم.</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-07-23 01:19:55</div>
<hr>

<div class="tg-post" id="msg-73313">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/aff752009f.mp4?token=WKJoZIz6uXJMyCNXN5-bmS5Wp9E2zcWJDUKbCRGuK9lCa5cTzxFq8lSG1d0t0czYKEkLqG2NDHuAY-HIwtSE0dXvivWGmBjJx8oFgRBqd3J02XNxKfmlsfbeMg43wWQOCp_zNNI1_T8jvKY6vtfm_VCipUPuD7fOtMyPz1dJccRlBC7DTNfGOrTAFSPDroEpdW54R4aU0XYJ7W1y6gieoEGcSoa6zaRK3gPOpnEXFGeZkWqLCEk6v_CqfLhZzD0FLF1ZR9n6H6Z5r9O2o3smhDlqT3qFXK__IBaf8B765RF1DkYE50dmSuz-ta2rChvc9SYIUvYcCnACITxT67pmiqD-bh315fauvpNhnMtGNMZDliNce2HqaI_XC5KWYlJFNBolCKkdeLoZLoGeuVhvTS4GYTCmejP2znc4-U28b_wrKocBSuvkXu1R2e1Zjmzxuc0usYmqYVjXbY0iLXrct5XnfFhzh98J6NQeWNCrIk-JlZZicQAFm0-BD1Ex_9RTQ5VDowhg89kqkQm-O7yQc6S9CUoHaioyllvbFp3pTjbER21GethCE42UVpdtfudjMgNwWN5dqEDJBji2Lk1EfD8nImhd4mrPSoiXcdLUwKj1-2ecssYaWJ4s5gcwH98_F2x_bjupH4gc3fr-UG6naHSAbrIJJtu1AVXSwIFnEy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aff752009f.mp4?token=WKJoZIz6uXJMyCNXN5-bmS5Wp9E2zcWJDUKbCRGuK9lCa5cTzxFq8lSG1d0t0czYKEkLqG2NDHuAY-HIwtSE0dXvivWGmBjJx8oFgRBqd3J02XNxKfmlsfbeMg43wWQOCp_zNNI1_T8jvKY6vtfm_VCipUPuD7fOtMyPz1dJccRlBC7DTNfGOrTAFSPDroEpdW54R4aU0XYJ7W1y6gieoEGcSoa6zaRK3gPOpnEXFGeZkWqLCEk6v_CqfLhZzD0FLF1ZR9n6H6Z5r9O2o3smhDlqT3qFXK__IBaf8B765RF1DkYE50dmSuz-ta2rChvc9SYIUvYcCnACITxT67pmiqD-bh315fauvpNhnMtGNMZDliNce2HqaI_XC5KWYlJFNBolCKkdeLoZLoGeuVhvTS4GYTCmejP2znc4-U28b_wrKocBSuvkXu1R2e1Zjmzxuc0usYmqYVjXbY0iLXrct5XnfFhzh98J6NQeWNCrIk-JlZZicQAFm0-BD1Ex_9RTQ5VDowhg89kqkQm-O7yQc6S9CUoHaioyllvbFp3pTjbER21GethCE42UVpdtfudjMgNwWN5dqEDJBji2Lk1EfD8nImhd4mrPSoiXcdLUwKj1-2ecssYaWJ4s5gcwH98_F2x_bjupH4gc3fr-UG6naHSAbrIJJtu1AVXSwIFnEy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">فرماندهی مرکزی ایالات متحده (سنتکام) اعلام کرد که نیروهای آمریکایی در تاریخ ۶ اکتبر یک شناور بادبانی (داو) مرتبط با ایران را در دریای عمان منهدم کردند؛ این فرماندهی مدعی است که شناور مذکور مشغول عملیات شناسایی بوده و به ایران در هدف‌گیری ناوهای جنگی نیروی دریایی آمریکا کمک می‌کرده است.
سنتکام اعلام کرد که پیش از انهدام شناور، خدمه آن به سلامت تخلیه شدند و تلاش‌ها برای بازگرداندن آن‌ها به کشورشان در جریان است.
@News_Hut</div>
<div class="tg-footer">👁️ 1.88K · <a href="https://t.me/news_hut/73313" target="_blank">📅 01:08 · 23 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73312">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">ترامپ:
«دلیل حمله ما به ایران در واقع دفاعی بود؛ چون نمی‌خوایم اونا سلاحی داشته باشن که بتونه با یه ضربه میلیون‌ها نفر رو از بین ببره.»
@News_Hut</div>
<div class="tg-footer">👁️ 3.42K · <a href="https://t.me/news_hut/73312" target="_blank">📅 00:57 · 23 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73311">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e37850b672.mp4?token=CPr5NSi_pEI1B7VqEbE1c1YnKE5gTPBQ-5N4YbaMvMlK92Hu8tboKHp6hcCX4Ug2I4lmdUUi0AhH3_9KNpsvehJWY_HYEwaFnw4cIb14nR4bRe5YSsX41L3w64BJmMyK-Ah3--_yNuM1B-sy5UTXu3k8qzTWmawhNI8lhirpib9vXKLbth_HNYINjcKrW2M2ECstpDeYQWUe5_MBb9DWsi9Y3TWHl19nMPGPBXVZXVCkYFA5zCWGmy6mdRo9JDgQjfsicbie4I_jNiV6V8DyLLe50SnVZIOYYd2G3ZhWlhOOLP0B1DTirsA5duc1Xe4JH83MDfterJyeHyl4Ra0tJA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e37850b672.mp4?token=CPr5NSi_pEI1B7VqEbE1c1YnKE5gTPBQ-5N4YbaMvMlK92Hu8tboKHp6hcCX4Ug2I4lmdUUi0AhH3_9KNpsvehJWY_HYEwaFnw4cIb14nR4bRe5YSsX41L3w64BJmMyK-Ah3--_yNuM1B-sy5UTXu3k8qzTWmawhNI8lhirpib9vXKLbth_HNYINjcKrW2M2ECstpDeYQWUe5_MBb9DWsi9Y3TWHl19nMPGPBXVZXVCkYFA5zCWGmy6mdRo9JDgQjfsicbie4I_jNiV6V8DyLLe50SnVZIOYYd2G3ZhWlhOOLP0B1DTirsA5duc1Xe4JH83MDfterJyeHyl4Ra0tJA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ:
«اگه اونا سلاح هسته‌ای داشتن، ظرف ۲۴ ساعت ازش استفاده می‌کردن.
کل خاورمیانه رو نابود می‌کردن، بعدش حمله به سواحل غربی آمریکا رو شروع می‌کردن و به اروپا هم حمله می‌کردن.
چون دیوونه‌ان؛ آدم‌های دیوونه‌ای هستن!»
@News_Hut</div>
<div class="tg-footer">👁️ 4.78K · <a href="https://t.me/news_hut/73311" target="_blank">📅 00:45 · 23 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73310">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4d0f068cfa.mp4?token=l9dWGQJTHsITxcG0wIJo1XfDHTQLV_x6dOPqFqYvQDlBl-2TqF40K0xOfMSc-Ycj7JkQFKb4CRsTAtqw2ldI7_YqIbSsyGs7LYUdqtwRS0DaKUXn5MnEbJJcY5ldM5ci4SvGvvel5F06gBQDduC6CB2gHncwxWZBdwzfhhwT5vbRqq1EgleJ1tT_VObnQOuCh5ZFTtBNIKyoXNycdPBpjF4ncFMjoqh1ZHrUdPbyDxj5kbyCIyEJEx50aiWgDSP1BUGJsGQe15PaMWeqYRB69PKioQ_O_rZeGcRM0E-D3sNW7SF2Jv8u6u1FYtvqP6rPCvtPk_dYmNPViXcNisXVbQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4d0f068cfa.mp4?token=l9dWGQJTHsITxcG0wIJo1XfDHTQLV_x6dOPqFqYvQDlBl-2TqF40K0xOfMSc-Ycj7JkQFKb4CRsTAtqw2ldI7_YqIbSsyGs7LYUdqtwRS0DaKUXn5MnEbJJcY5ldM5ci4SvGvvel5F06gBQDduC6CB2gHncwxWZBdwzfhhwT5vbRqq1EgleJ1tT_VObnQOuCh5ZFTtBNIKyoXNycdPBpjF4ncFMjoqh1ZHrUdPbyDxj5kbyCIyEJEx50aiWgDSP1BUGJsGQe15PaMWeqYRB69PKioQ_O_rZeGcRM0E-D3sNW7SF2Jv8u6u1FYtvqP6rPCvtPk_dYmNPViXcNisXVbQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ :
«اونا ازم قول گرفتن که دیگه هیچ‌کدوم از رهبران ایران رو هدف قرار ندم. منم بهشون قول دادم.»
«احتمالاً یه کم زیاده‌روی کردم. عذر می‌خوام، چون دیگه اصلاً نمی‌دونم با چه کسانی طرفیم!»
@News_Hut</div>
<div class="tg-footer">👁️ 4.88K · <a href="https://t.me/news_hut/73310" target="_blank">📅 00:43 · 23 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73309">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e6ca5ec198.mp4?token=r47sAPvLjG6s8_7Kzh0J_WlfqRXPuM3YHkK8OvJxPxPmfZcVgZwHGVmFIGvWYfHTPN8-fO2hgdh1zy7P839O2Qr0R73fBzjVW9GHc8do8JXvCa22tUEFIFQQpZ1sJhxKLdgZhv1MN8nfBv9fbx0ovdbwkOlpNF8cg0TrL_sPHHRqZH2TdSrnsWUIeYnBufL3bP2yUrDSHQgi-Ho-VM6tsvABmNi6YR4U8-x6hTEYhyYawM97WVcAY06YvGu-tuPeH7Nnazidcph6QvYv9gt4WaC6g1MAUF0eDbJTwh0h5cOtKgIMxiVjKZdYKlkShajVvCFhwDy7i1OBtIlEWrmskg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e6ca5ec198.mp4?token=r47sAPvLjG6s8_7Kzh0J_WlfqRXPuM3YHkK8OvJxPxPmfZcVgZwHGVmFIGvWYfHTPN8-fO2hgdh1zy7P839O2Qr0R73fBzjVW9GHc8do8JXvCa22tUEFIFQQpZ1sJhxKLdgZhv1MN8nfBv9fbx0ovdbwkOlpNF8cg0TrL_sPHHRqZH2TdSrnsWUIeYnBufL3bP2yUrDSHQgi-Ho-VM6tsvABmNi6YR4U8-x6hTEYhyYawM97WVcAY06YvGu-tuPeH7Nnazidcph6QvYv9gt4WaC6g1MAUF0eDbJTwh0h5cOtKgIMxiVjKZdYKlkShajVvCFhwDy7i1OBtIlEWrmskg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سؤال: آیا تغییر رژیم در ایران پیش از انتخابات اسرائیل واقع‌بینانه‌ست؟
نتانیاهو: «نه، فکر نمی‌کنم واقع‌بینانه باشه.»
«من می‌گم سرنگونی این رژیم ضروریه؛ چون مسئله موجودیت ما به این موضوع بستگی داره.
ما کارهای زیادی انجام دادیم و ضربات سنگینی بهش وارد کردیم. این رژیم الان در ضعیف‌ترین وضعیت تاریخ خودش قرار داره.
اما باید کار رو تموم کنیم.»
@News_Hut</div>
<div class="tg-footer">👁️ 6.95K · <a href="https://t.me/news_hut/73309" target="_blank">📅 00:24 · 23 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73308">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">صدای انفجاری از سمت تنگه هرمز شنیده شد.
@News_Hut</div>
<div class="tg-footer">👁️ 9.68K · <a href="https://t.me/news_hut/73308" target="_blank">📅 23:38 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73307">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ee05740e91.mp4?token=nGI6XzptJdDx_RDv71us2Qww1TaCplKVh6-0-nWMhE6msMgsSmHnUfYIk7SreOJl04yU2bfmXcnH7_lwxsxhlkvQKMvH8tPhELmrUHDmqL3Qez3k9ge60MaEoaEboaiSXwrqd0-gn5HyM-cUBoy-Qw_VWZF1xHvJvLclVhd_2R-xy146Q0qqc_WlNPV9sBZcoUf3qI-xuRFU45hYHFZGSwzvzzOohoImbrtLw22D9dIjbvuqj0GoGN7ucdxRHqbdcP0Xm8HZzup24WyWS8P80ssuO_tpPSyCq6FOAjQWIyjNiPXr3YzsOJV19TiKiBEG_6gAacAMfNBELDCAwx2Q0Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ee05740e91.mp4?token=nGI6XzptJdDx_RDv71us2Qww1TaCplKVh6-0-nWMhE6msMgsSmHnUfYIk7SreOJl04yU2bfmXcnH7_lwxsxhlkvQKMvH8tPhELmrUHDmqL3Qez3k9ge60MaEoaEboaiSXwrqd0-gn5HyM-cUBoy-Qw_VWZF1xHvJvLclVhd_2R-xy146Q0qqc_WlNPV9sBZcoUf3qI-xuRFU45hYHFZGSwzvzzOohoImbrtLw22D9dIjbvuqj0GoGN7ucdxRHqbdcP0Xm8HZzup24WyWS8P80ssuO_tpPSyCq6FOAjQWIyjNiPXr3YzsOJV19TiKiBEG_6gAacAMfNBELDCAwx2Q0Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ درباره ایران:
«اصلاً معلوم نیست توی ایران با چه کسی طرفیم؛ هیچ‌کس دقیقاً مطمئن نیست.»
@News_Hut</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/news_hut/73307" target="_blank">📅 23:34 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73306">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fb1ab9f9c7.mp4?token=N-oMB9VDR5-7tJc2_sryW7FvISnAJBSU5ey0oVHXTMu_D62CfqYOLV_w9f9SewA2GLurfkTWIhWx-IR6z9K0aYDzZ8912yH84WD02BMDK66573VjTUjT60S3iEbt2yrdYJTl6j0WREcHMXBu-nZysjiKBOxiNKkzgjvrsaavTvYCcUSvxcs8JzDb3DoD9rrErRIdnrH2m74-xuIGxkm06mWR4tuGY6aIfkZoNEzxdw0mGIJzWh2QTDtzf4ZwRTuzgRGYWT4XJHyCOavglMP_okGGzW8rSFvgPeECbmNChikg7-dEtyob2TN6U7JZ7uhr1xVSMG0MlLC53AsnRPDYlg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fb1ab9f9c7.mp4?token=N-oMB9VDR5-7tJc2_sryW7FvISnAJBSU5ey0oVHXTMu_D62CfqYOLV_w9f9SewA2GLurfkTWIhWx-IR6z9K0aYDzZ8912yH84WD02BMDK66573VjTUjT60S3iEbt2yrdYJTl6j0WREcHMXBu-nZysjiKBOxiNKkzgjvrsaavTvYCcUSvxcs8JzDb3DoD9rrErRIdnrH2m74-xuIGxkm06mWR4tuGY6aIfkZoNEzxdw0mGIJzWh2QTDtzf4ZwRTuzgRGYWT4XJHyCOavglMP_okGGzW8rSFvgPeECbmNChikg7-dEtyob2TN6U7JZ7uhr1xVSMG0MlLC53AsnRPDYlg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سعید شکیبا یه بلاگر طنزپرداز که صدای افراد رو تقلید میکنه این دفعه صدای علی خامنه‌ای رو تقلید کرده؛
و باعث اعتراض حامیان حکومت شده و گفتن با خمار کردن چشماش و درخواست چایی نبات قصد داشته به رهبر صفت معتادی بزنه....
+الانم گزارش هایی منتشر شده که براش پرونده قضایی تشکیل دادن.
@News_Hut</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/news_hut/73306" target="_blank">📅 23:15 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73305">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/2f7e6ba723.mp4?token=H_rkuJ4hXEDre628gwUiKOo080lvDHVUj8I12w30r_yH9Vq88ooXD7U7WSLRtvt6GFaRO1UKtsssZH2RzZCRGnMv83sZCjJU6-9u9TgrV9A1TJW2u4tLjOfZXT7dzXFPzedwK2Cme5PxWr7lkqNEjka9BmgB1jnBKwjapalwMLzcRZB_-JRGAfW63NIteTcSvLSpZUVOzk0OmjZyiZjFe4cZiuTSqEHfaHsfOHh0NJmjEoF345kQkULcQy6g4czL2Xamfqy_obXEQmHDdwCza5umJ84YDqX1snxRVi50RABAtZarMFyp5ACQ9bG5Vyl_HCSAjMki0ETTN9TYKnD8zA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/2f7e6ba723.mp4?token=H_rkuJ4hXEDre628gwUiKOo080lvDHVUj8I12w30r_yH9Vq88ooXD7U7WSLRtvt6GFaRO1UKtsssZH2RzZCRGnMv83sZCjJU6-9u9TgrV9A1TJW2u4tLjOfZXT7dzXFPzedwK2Cme5PxWr7lkqNEjka9BmgB1jnBKwjapalwMLzcRZB_-JRGAfW63NIteTcSvLSpZUVOzk0OmjZyiZjFe4cZiuTSqEHfaHsfOHh0NJmjEoF345kQkULcQy6g4czL2Xamfqy_obXEQmHDdwCza5umJ84YDqX1snxRVi50RABAtZarMFyp5ACQ9bG5Vyl_HCSAjMki0ETTN9TYKnD8zA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یه دختر از کبودی چشمش در اثر کتکی که خورده پست گذاشته و اما کامنتا وحشتناکه!
بیش از ۱۰ هزار دختر، عکسای کبودی‌شون که در اثر کتکی که از دوس پسر، شوهر، برادر و پدرشون بوده رو کامنت کردن!
@News_Hut</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/news_hut/73305" target="_blank">📅 22:33 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73304">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f4ba0e7f1e.mp4?token=bPdaKuDOBQVBMwoeokzPySHqUN4vYHPbP6Kd8eYi4gsO7NFlY5n0kWPX17Ag31sT6kbjL_nF1Ob7b_J2MF1NiXwZyu6Vjb5owhWI6svUNW9axltJNc6MsCavedIjBroIqJNI2LKyB60y4npHKluVH6Y80ibK9iNC1KmxfDCu8otb3Eebg5Q3nQlMhT74jBkyKCgZuwcEVgjSOhRcLnrs4iQEcH_9fAO55SajyU4L4fGjnGZWgza4gUMK3BOy1rMgYTuegLZNEDp7cJOqnhZ-jig9J7Kp25YjoXLByxodp8H_X80CgPLdDKKrG6MetQiUj49EQA92HYypCPEGGqsKVoijOtAacLORwh_nlRrrOKkEOzNkeOtdeChMG-8EMZQ8Rif81up-025rMVoOO9KZMhDhQp4R75S7XC5e1fCBMfNP1AZTVYCcpTAEPwYv-TZ9E6-pboVooD2vtA0fblyUrI_Ji-x6j-vAfKeKUy2MP3lWttp0gR4yC_fW6EDO9eTMYaf_5EKJhU5549ugyvY0-Ip97pPifde_6zfCpoPO2Rrs76Vk1HQFg8V_TPR9JmiojBZ6IAJzYdLQw_KUi2xLEB85To3yk76sCIakITcxnuxmtToKYNiWXyBsWFPjgYCotGE6EuxnJesohxVBtPPmYf8QnY_lkP9sw9uBC5wDAAU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f4ba0e7f1e.mp4?token=bPdaKuDOBQVBMwoeokzPySHqUN4vYHPbP6Kd8eYi4gsO7NFlY5n0kWPX17Ag31sT6kbjL_nF1Ob7b_J2MF1NiXwZyu6Vjb5owhWI6svUNW9axltJNc6MsCavedIjBroIqJNI2LKyB60y4npHKluVH6Y80ibK9iNC1KmxfDCu8otb3Eebg5Q3nQlMhT74jBkyKCgZuwcEVgjSOhRcLnrs4iQEcH_9fAO55SajyU4L4fGjnGZWgza4gUMK3BOy1rMgYTuegLZNEDp7cJOqnhZ-jig9J7Kp25YjoXLByxodp8H_X80CgPLdDKKrG6MetQiUj49EQA92HYypCPEGGqsKVoijOtAacLORwh_nlRrrOKkEOzNkeOtdeChMG-8EMZQ8Rif81up-025rMVoOO9KZMhDhQp4R75S7XC5e1fCBMfNP1AZTVYCcpTAEPwYv-TZ9E6-pboVooD2vtA0fblyUrI_Ji-x6j-vAfKeKUy2MP3lWttp0gR4yC_fW6EDO9eTMYaf_5EKJhU5549ugyvY0-Ip97pPifde_6zfCpoPO2Rrs76Vk1HQFg8V_TPR9JmiojBZ6IAJzYdLQw_KUi2xLEB85To3yk76sCIakITcxnuxmtToKYNiWXyBsWFPjgYCotGE6EuxnJesohxVBtPPmYf8QnY_lkP9sw9uBC5wDAAU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حوثی ها اومدن یه ویدیو منتشر کردن از اسنایپر هاشون که نیرو های دشمنشون تحت ائتلاف عربستان زدن:
@News_Hut</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/news_hut/73304" target="_blank">📅 21:52 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73302">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3e63f1ffb8.mp4?token=tkF6YsQ5QUvkW7jbYU3f4jt0-gwJOzPGvn1y5B7ybLlscmZsD5FmssoHObQj8wTpO1UNQWPx_CO_Q0q4Hm5PSTL_oNE6PTTu-gOj3QO718tmZQq6tJ3Nxyvvd-dH0ifDrTbkoUoQ0_Y7dSSmoPYfjYIUeTwekuzpPaeCo3GdzcFipEMOfyIkYGmWV5SdyDBzHwQX4cipiSxJ-muuC-AP9GTPMem1eAzJP3x2e8J5O7F1ULPkenocGwdRlACshaX1Qve3VFOGWh4jRx_LRuVmZxvvH8IaQhK186elwXhz41n15g3K-H3Cl5UcTzG-Oh7Fpm0PsqXBZhSN56DBM01ljA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3e63f1ffb8.mp4?token=tkF6YsQ5QUvkW7jbYU3f4jt0-gwJOzPGvn1y5B7ybLlscmZsD5FmssoHObQj8wTpO1UNQWPx_CO_Q0q4Hm5PSTL_oNE6PTTu-gOj3QO718tmZQq6tJ3Nxyvvd-dH0ifDrTbkoUoQ0_Y7dSSmoPYfjYIUeTwekuzpPaeCo3GdzcFipEMOfyIkYGmWV5SdyDBzHwQX4cipiSxJ-muuC-AP9GTPMem1eAzJP3x2e8J5O7F1ULPkenocGwdRlACshaX1Qve3VFOGWh4jRx_LRuVmZxvvH8IaQhK186elwXhz41n15g3K-H3Cl5UcTzG-Oh7Fpm0PsqXBZhSN56DBM01ljA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">کرباسچی: سلاح هسته‌ای بازدارنده نیست ما نمی‌توانیم پدر آمریکا را دربیاوریم!
کرباسچی:
اینکه حالا هر روز اینجا کارشناس بیارید و هی بگن: «نه آقا، ما اونجا داریم پدر آمریکا رو درمیاریم!» آقا، ما نمی‌تونیم...
هی میگین پدرش دراومده! دقیقاً پدرش کی بوده؟
همون‌جوری که ما به آمریکا آسیب زدیم، ولی آسیبی که ما به آمریکا زدیم، با آسیبی که به کشور ما خورده، قابل مقایسه نیست.
@News_Hut</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/news_hut/73302" target="_blank">📅 21:05 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73301">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/578bba6f4a.mp4?token=UOE-A4xhYu1bGhdxmCGfdH0IuRn47zysIB0frt2qJ_VOrVIXEVqDMa_1pYvoPFHPbdeANHzV1RJfu1B3-kv0VB14hv0VLeLddXiTII8xO-N-Pvr34WAPJ4n4apTaHFblR-3icUlTts-I6cw8lppk5gA-ugqlARdjOXtEavH3uuhkgsv0SfmIOfkAdawRrWRr8YkwTHD9TLYYmL1EdqSWUxtry39iVKfUhf-MbII6Zh2Mumd-BbSl8iDWhaWY1NiIOILmbCV-nAda3fEWCMAeS0X1QjN3wqzZSRL7Xln0MfNF_-6n8ZKdUH1LJGrtnGRkTMBdHyDzLztqfdAKJBf7jA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/578bba6f4a.mp4?token=UOE-A4xhYu1bGhdxmCGfdH0IuRn47zysIB0frt2qJ_VOrVIXEVqDMa_1pYvoPFHPbdeANHzV1RJfu1B3-kv0VB14hv0VLeLddXiTII8xO-N-Pvr34WAPJ4n4apTaHFblR-3icUlTts-I6cw8lppk5gA-ugqlARdjOXtEavH3uuhkgsv0SfmIOfkAdawRrWRr8YkwTHD9TLYYmL1EdqSWUxtry39iVKfUhf-MbII6Zh2Mumd-BbSl8iDWhaWY1NiIOILmbCV-nAda3fEWCMAeS0X1QjN3wqzZSRL7Xln0MfNF_-6n8ZKdUH1LJGrtnGRkTMBdHyDzLztqfdAKJBf7jA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">کرباسچی در آنتن زنده شبکه خبر:
مجری: از آقای ظریف دعوت کرده بودیم اما نیامدند.
کرباسچی: شاید از عواقبش ترسیدند!
@News_Hut</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/news_hut/73301" target="_blank">📅 21:00 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73300">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d6981ce1ea.mp4?token=OrQThl1EY7BIWSAfxSyXNaIosKmzGDVKdUtdzIO0GU8oDkcPPmggQRxqWySI27lnenc0jJ49M7WSiPtyX6ivS2_v6pCIUgZan6TZUwvvNuKw0lgRVMC2LkRmbKOFvQNkRver39RrlWZArpHw4K6bfjmR3ekXX0pxLig3l9pvy2PhCogK4pc-g7qVVwAWtX4rASwKEFqceUrDvOQuUPE6mTdBcv36HDrVxXlHGgs8HVh8f3aHgmJ56fa7_rcznm8qMVZ49cYwACrjQxpQ-LuG9qpMwd8o0MnaV65gn-AHwIBaO9XQDDn4sx_0nQy_UWFzRm5_YX1Zgsjg9wQmekWq6jtvr2sTnReixyiU6BZuoJRqT5JGxPRn-Con9jd_9IfLR5hUl6YBtjvNO3KdJ1QLwxnY7FsiqRO7IGsj1TkPzmNb3Kv7nA7VA0SXZ9rxHLOOQZXhYTp0DNo7pk2nhF-R7tkuHk70vIdGfp_SKNRptVgC9kpgM3oC6LuxUpe6Zw5eXI4rwllp2AZrmKBX_WlGzdJCoaCKA2u4zLTV-KM-iLvAK-fgLkxq-GXY2V6qRPxaVHFcpPDdgCK4SYuVR_-1hSlNywBoRW2EpHwCyzmVL7UeIu1VB9EDem5OVbk9VT3TXl_JuTBoLAoPsslfB5YCP4a1hftXb3cckhe3wCFo1io" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d6981ce1ea.mp4?token=OrQThl1EY7BIWSAfxSyXNaIosKmzGDVKdUtdzIO0GU8oDkcPPmggQRxqWySI27lnenc0jJ49M7WSiPtyX6ivS2_v6pCIUgZan6TZUwvvNuKw0lgRVMC2LkRmbKOFvQNkRver39RrlWZArpHw4K6bfjmR3ekXX0pxLig3l9pvy2PhCogK4pc-g7qVVwAWtX4rASwKEFqceUrDvOQuUPE6mTdBcv36HDrVxXlHGgs8HVh8f3aHgmJ56fa7_rcznm8qMVZ49cYwACrjQxpQ-LuG9qpMwd8o0MnaV65gn-AHwIBaO9XQDDn4sx_0nQy_UWFzRm5_YX1Zgsjg9wQmekWq6jtvr2sTnReixyiU6BZuoJRqT5JGxPRn-Con9jd_9IfLR5hUl6YBtjvNO3KdJ1QLwxnY7FsiqRO7IGsj1TkPzmNb3Kv7nA7VA0SXZ9rxHLOOQZXhYTp0DNo7pk2nhF-R7tkuHk70vIdGfp_SKNRptVgC9kpgM3oC6LuxUpe6Zw5eXI4rwllp2AZrmKBX_WlGzdJCoaCKA2u4zLTV-KM-iLvAK-fgLkxq-GXY2V6qRPxaVHFcpPDdgCK4SYuVR_-1hSlNywBoRW2EpHwCyzmVL7UeIu1VB9EDem5OVbk9VT3TXl_JuTBoLAoPsslfB5YCP4a1hftXb3cckhe3wCFo1io" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ایلان ماسک درباره هوش مصنوعی:
شکنجه کردن یک «ابر هوش» احتمالاً ایده خوبی نیست؛ چرا که ممکن است بخواهد انتقام بگیرد یا کارهایی از این دست انجام دهد.
به گمانم لازم نیست با آن خیلی با احتیاط و ملاحظه‌کاری رفتار کنیم؛ این موجود قطعاً از نظر احساسات و جنبه‌های مشابه، بسیار سرسخت‌تر و مقاوم‌تر از انسان است.
با این حال، فکر می‌کنم بهتر است ابر هوش را در موقعیتی قرار ندهیم که احساس کند با آن بدرفتاری شده است.
@News_Hut</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/news_hut/73300" target="_blank">📅 20:28 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73299">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/79be643006.mp4?token=EMu9320HTD6bq-ARuoPdYIHxbOWx-VsSErH7TKIjt6YC5JzbChWUUoHj9R1uYa5-nk2_sIwuf0fVY79KMtwUC05sMHyC7HSvJxHq0Iget9sucJcxz4jk46LT76KMua7IwJJnPBdlLMIWTqChM8q0YLxkQ-1sywoW6WZK-mQadKzFQiJxj3EhI4sTRntQUNhFLXMoWGfAOKbsNxQ9Ey0BD7PI_MxRVimkuEyrJBEUQf4nonYjeX4iMNCv7xxg3j2A1cGej-rcLYHo7F2nKkWEGQRzNRUi9KzEaO-AkHYkaM1AiCMMs0vJqJ5WlGFt19RBS07v1yyh-4mfRwLDQuAAdw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/79be643006.mp4?token=EMu9320HTD6bq-ARuoPdYIHxbOWx-VsSErH7TKIjt6YC5JzbChWUUoHj9R1uYa5-nk2_sIwuf0fVY79KMtwUC05sMHyC7HSvJxHq0Iget9sucJcxz4jk46LT76KMua7IwJJnPBdlLMIWTqChM8q0YLxkQ-1sywoW6WZK-mQadKzFQiJxj3EhI4sTRntQUNhFLXMoWGfAOKbsNxQ9Ey0BD7PI_MxRVimkuEyrJBEUQf4nonYjeX4iMNCv7xxg3j2A1cGej-rcLYHo7F2nKkWEGQRzNRUi9KzEaO-AkHYkaM1AiCMMs0vJqJ5WlGFt19RBS07v1yyh-4mfRwLDQuAAdw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">#مهم
؛ افزایش چشمگیر و پشم‌ریزون پروازهای ترابری نظامی آمریکا در خاورمیانه و شرق مدیترانه
؛
بر اساس داده‌های رهگیری پروازها از FR، تعداد پروازهای باری نظامی آمریکا نسبت به ماه اوت ۸۰ درصد بیشتر شده؛ هواپیماهای C-17 بیشترین سهم رو داشتن و فعالیت هواپیماهای سنگین C-5 هم دو برابر شده.
این آمار فقط مربوط به یک بازه ۲۴ ساعته‌ست.
@News_Hut</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/news_hut/73299" target="_blank">📅 19:59 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73298">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">صدای دو انفجار در تنگه هرمز شنیده شد.
@News_Hut</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/news_hut/73298" target="_blank">📅 19:42 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73294">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/c4IJWsVe1pV6gIRa5AmwuBnB1kWirs91biE6F2fUf8i-lS_FDaYu2G8DPDr-MWLM2d0HeZddGUmYjtQR6SnnVxg6SOkxjGGrSFTf1_g2CUyfcd9MKmjTl8V9t5PCIo0sZNfsLzTisGk8c7OEA-2QM0m_2sYGx0-386SkSOTaxc7rJY1wzQ-8VpcvK9qSUlfxtPfIM0617YJq3SpVXp-fbMQYvRMpm8lDsSRQ0V76ZU9NCjQafzurX7e6zNTMV9L31fbPbvFAZFQfJHt8ceGf9cbUa_x7sb7BL9TFzUliz90lwGUIQKP5QeIq_Uo6vZustaUt7KTNudkQSTW83jyh6Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/fsWBZSRzzpf2lwNBaGyJbyOiJna6ToqZdA3niFpNlh2waFPML92nd74F8z38vwQO77KIEmDifQgKP-hBX6HKFS6_Lwr8aXeYW30b2UzsQufpQ1qxBTjMEsFpxDbTr-W2wTCdwyYnRKVZ9JAG-mpguKg_dqPKJGNI3Mr8BQh_1Mo3aBmSvYPvWFCf3GzUd5MocZ_Gtj7DPEKQa1vDkSAqGOrWFjoZSFhqf-laO690X2oCnkHur3PSCNA9zu3eTjz0tHWvbNlwWcrtGGvf9vH4ccWBInxLYAzowiJA3CZvEyuqQOE9EF1AVFDklcKV0ik5E6VdKFuKKZ-x_q355qfigg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/EKVns0EOU7yrrJ9Q-uyS8xOUKROdPNqCKzXazY5BWzE_-tcOgLjRki2sBwrxeubMA8RTbTxoV7gQOi-ukjC3JJ_QG2EsvutIV-0MmV_8Foe-ZeuZbwfpQmck1tu2apcshbIgHwV6xx3oEmlHrYFguf8ym4d_669t05Kp3CJO-z0nBK1cPs2f3LPIFI6ay2CMdtUfc6w0PrcK1LD3TPdrd_JxQTFqQS44NcnKNKuhrmQRkWbLVOGejFoHsZ4U5Hj6g-93cDTRKnp1vBC8d2Pvk3lq-QQJQeU2pi-BRQjNfoOWsyiHk2KfGarFnrQfx40S4cImGwWW88385CTna9Ozfw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/IT4GzYLSiEYu-OzRSc6qTicddTb1bQmdOTJoLsXl-cllW6EHmSKS-mYg5yRuVyd6PAJciwhT6uWmP20HW9HfsTkoaJ2c9oirbjhgikZu4SJpEPMwhT2i07Jm1aOrUtCxuSNeZ7HmXwTdeAYKvIoDaU8HNWdlBzm_QrddMK9BhCVCYFXbbCG3D9PLyzhWIdOkS2Im9t_7VSzxtVirpkgY0ZMyyaxAOqs-VHqK9D8P2VR-KqW0OrEdhN54lojA31jj_z405PjJcMBiMYZlKguVejM9qOaofP9HATUX01_iMzD-lFK0-rQDuQAaMHjYz11jfhkf1XOdzf9Y9sA6ajPOkQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">دیروز یه عکاس فرانسوی تونست از پدیده‌ی زیبای red sprite | رِد اسپرایت ، عکاسی کنه؛
رد اسپریت‌ها نورهای قرمز کوتاه‌مدتی هستن که گاهی بالای ابرهای تندری، تو آسمون دیده میشن.
اونا فقط چند لحظه (هزارم ثانیه) می‌درخشن و معمولاً بعد از رعدوبرق‌های خیلی قوی ظاهر میشن.
‌
@News_Hut</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/news_hut/73294" target="_blank">📅 19:13 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73293">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0104fcf33c.mp4?token=agd5qsncMuZJ_Y7WBfiDtEb532qiap8B4srZRqKWFw32BTHV-OMHpKWkX4bM32cirTX2KU332mCzfVMDbyFdk_TiBD3B08APw1W5PC351FMlfCm1YsnrwTJaXeopl9Nhvsyxyf81TdtT7ppHBop2rOnra-9j4aOkUYJ5JPA_iHg2Bm2A4FwVwgbZVdH6i0hi4YgXlU9KJdb_g-GTZZBRCGs6UZMrZ6IXvCDQLPYIGTtp8Z7boVswIaxQuv4QxzVlzBfly8HCqP4IiiGmpQG1D0wYvzosH-y9iBanb0TJm22oFTrUmFhjoHMvK3KOVB12zlLzttuc6iI1VBwNEu21BQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0104fcf33c.mp4?token=agd5qsncMuZJ_Y7WBfiDtEb532qiap8B4srZRqKWFw32BTHV-OMHpKWkX4bM32cirTX2KU332mCzfVMDbyFdk_TiBD3B08APw1W5PC351FMlfCm1YsnrwTJaXeopl9Nhvsyxyf81TdtT7ppHBop2rOnra-9j4aOkUYJ5JPA_iHg2Bm2A4FwVwgbZVdH6i0hi4YgXlU9KJdb_g-GTZZBRCGs6UZMrZ6IXvCDQLPYIGTtp8Z7boVswIaxQuv4QxzVlzBfly8HCqP4IiiGmpQG1D0wYvzosH-y9iBanb0TJm22oFTrUmFhjoHMvK3KOVB12zlLzttuc6iI1VBwNEu21BQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مراد ویسی:جمهوری اسلامی انگار با غافلگیری حال می‌کنه؛ تو جنگ ۱۲ روزه غافلگیر شد، تو جنگ ۴۰ روزه هم غافلگیر شد و
تو جنگ بعدی هم قراره غافلگیر بشه!
@News_Hut</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/news_hut/73293" target="_blank">📅 18:59 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73292">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/news_hut/73292" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/news_hut/73292" target="_blank">📅 18:59 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73291">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gjGiHJzG0dRHbkFGHtVPaJGnNRo09EdiQUyetrLyulq6v5Tml3r-fIaD46rxpen92W_KFhhFZx8jQx4Vb5cDRsNKtttnsq_9dTnmEj5AlMTHA2aOqAf-P3trEaqzA4g7_5OqYQwYAQrBNdc-4NnxDk3rm8q76skc_LmyRpSULdX9kg4qkN4X1Z0rfizm9RSPWXFQT661BBNZh5bpwt65LTKzM5plXFHZvxuT7ODrFdhMOrQ_THFL01PoJs5wFqajVXprCKa6Tv4CzYBIqXrDtjow0MWE1P8A2iHTV-r61Cf1bMU4kFJa54jN9fjcfTM_aYRBfYxqimouJfKJ60-lBg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رئال مادرید
🆚
آاس رم
🦖
این نبرد حساس چمپیونزلیگ را در سایت بین‌المللی
TrexBet
پیش‌بینی کنید!
📉
نگاهی به آمار ۲ تیم در ۵ بازی اخیر:
رئال مادرید: ۴ برد، ۱ شکست و ۱۱ گل زده
آاس رم: ۲ برد، ۳ تساوی و ۷ گل زده
🦖
🦖
🦖
🦖
🦖
بونوس اولین واریز تا سقف ۱۰۰ یورو
🦖
بهترین ضرایب بین تمام سایت‌ها
🦖
واریز آسان و امن از طریق کارت به کارت
TREXBET — PLAY. PREDICT. WIN.
https://TrexBet.com
T.me/TrexBet_Ir</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/news_hut/73291" target="_blank">📅 18:59 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73290">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vrp9VkrWoEp0ukYey0za6oa3MHZ4CtEdNYC3Q4t8nM1T7MWVMJ5HdaakYfNqVBJA18bIJicB8_mmCEmTxTVHB9ZMbtyVCu2pKBnlqBtLPMf01Vwa7us0wsB-xZqtiSbZscxXqt5P6V11qK2lJgZWN1WVtp0RL6PTftaI1FtySXq-fjIHln9JbnMN0VqhHgcZ_60BRgKoCHM1-KDHAC1b_ckHgrARMWVC59HRBu3N6QEcnIlpIIbKBJPudx3GJwTsO7Z3uDjje5Dvs5YOrkNbAQBQyLtB5JE6oD8IwPiHxI8PBbip0HpjE9f3VoR1VIw6WPMTv4quyAW78kFt_IC99A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سنتکام:
محاصره بسیار موفقیت‌آمیز ایران توسط ایالات متحده، ماه‌هاست که اجرا شده و به‌شکل حرفه‌ای اطلاع‌رسانی شده است.
ایران تنها کشوری است که به دریانوردان غیرنظامی در حال عبور از آب‌های منطقه حمله می‌کند.
با وجود این حملات غیرموجه، تردد تجاری در تنگه هرمز با حفاظت هماهنگ نیروهای آمریکایی و شرکای منطقه‌ای همچنان ادامه دارد.
@News_Hut</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/news_hut/73290" target="_blank">📅 18:31 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73289">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UlBw6xJOcYkY_MHGz5XdkUopO19a5kio9FguerQsim8R5sASuyO-2mNL4r9krF4rBKEfPF1GEw-_dTP26osZsx-8H0JhQRIuZO1P_2-t985wnm1VgQmQG8vkAPd35DyEG0LSxupy_fxG-PDbag_Omwvne3P_noY5l9h3Ndn-xE54iSsuJoHg2OMYG0cXWv9YvQxwr6AdSwqsQhTkx8fKCP1dzBmPy9WTBV41vSokFZEvQL5990d__ib6v8sP2faZ_P-4iw3LzED5cQB7Gs_nX0QMrDG_2QVolPyX75cXDKgb8s1fET-TO7ipMvnKbSGjt6HA09qzVIE_l-16Gk39sw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جماران: اوپراتورها تصمیم‌ گرفتن اینترنت رو 40 درصد گرون کنن ولی هنوز معلوم نیست کی به اجرا دربیاد. احتمال داره از امشب اعمال بشه!!!
@News_Hut</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/news_hut/73289" target="_blank">📅 17:48 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73287">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6638d07252.mp4?token=Mfy-Ygnh6jHic-EjM1BOOZu6TSd3iXktlJ2cW5HBiePbpnkvcgErbq72yXqUhRpXMN6CqWlHyFHcus--I5n3BND2LtedTFQibw9Mp_IfzYNcW-nFR6D08eE7zGagvGEQHhjNLHBycYx2-IRsKJDnqWEKoscXZITh81Xd_A8b6xR11fjziF2ALqxZ05Cv2SJ3umw8HncdQ71Hmnk4vowR6WDtZD8lDI26BrIouXL77erb2jjqA8qReSzkRThF-TVoBE-fV17q03VMOLllHu-HdjS6sph0W6tNV6D-FVQDohPvepSEMBBni01ejVLeyDDqhLDt2HPjwcT_NPkAUk_-_Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6638d07252.mp4?token=Mfy-Ygnh6jHic-EjM1BOOZu6TSd3iXktlJ2cW5HBiePbpnkvcgErbq72yXqUhRpXMN6CqWlHyFHcus--I5n3BND2LtedTFQibw9Mp_IfzYNcW-nFR6D08eE7zGagvGEQHhjNLHBycYx2-IRsKJDnqWEKoscXZITh81Xd_A8b6xR11fjziF2ALqxZ05Cv2SJ3umw8HncdQ71Hmnk4vowR6WDtZD8lDI26BrIouXL77erb2jjqA8qReSzkRThF-TVoBE-fV17q03VMOLllHu-HdjS6sph0W6tNV6D-FVQDohPvepSEMBBni01ejVLeyDDqhLDt2HPjwcT_NPkAUk_-_Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دیشب در یکی از تجمعات شبانه  سه نفر از حاضرین نقش قاضی دادستان و حسن روحانی رو بازی کردند و حسن روحانی محاکمه شد.
@News_Hut</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/news_hut/73287" target="_blank">📅 17:27 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73286">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/83510795fd.mp4?token=V2qJEh9c-G_D12aJ9zkLIl9v0_1cLZf9uBpXvtacXLIzCvr52YZJR2lf8AjDw5YI9Mu4Zayow1X9PxuPWfQry-05CqQquZXQup4DAIieu0IyEPkiqX1cEcYBfiyH46afe90LXRGzmDnpAAai7VW1_szUf9VNHm8fMf9gYVdx63ZC0F4MBdFjCcQPnQsSO1WAS974QQ1IN1Aq7qT6bHacWlPN2PRvDnS7VYlBfeqHJnzneANi2bvcEcCMHjmL2bSnzkNub7v80luMM2s1ZXVgb38JyYqU0Jk2lQv74yE2rsohe8M-CP0OALUyhGKh3MmaKFerty8RGgaoms6bghDT1Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/83510795fd.mp4?token=V2qJEh9c-G_D12aJ9zkLIl9v0_1cLZf9uBpXvtacXLIzCvr52YZJR2lf8AjDw5YI9Mu4Zayow1X9PxuPWfQry-05CqQquZXQup4DAIieu0IyEPkiqX1cEcYBfiyH46afe90LXRGzmDnpAAai7VW1_szUf9VNHm8fMf9gYVdx63ZC0F4MBdFjCcQPnQsSO1WAS974QQ1IN1Aq7qT6bHacWlPN2PRvDnS7VYlBfeqHJnzneANi2bvcEcCMHjmL2bSnzkNub7v80luMM2s1ZXVgb38JyYqU0Jk2lQv74yE2rsohe8M-CP0OALUyhGKh3MmaKFerty8RGgaoms6bghDT1Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سپاه: یک کشتی کانتینربر حامل بیش از ۲۵۰۰ کانتینر، صبح چهارشنبه پس از برخورد با مین دریایی در جنوب تنگه هرمز و وقوع انفجار و آتش‌سوزی، غرق شده است.
@News_Hut</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/news_hut/73286" target="_blank">📅 17:10 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73285">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">گزارش های غیررسمی از اینکه تعرفه اینترنت اپراتور ها از فردا قراره ۴۰ درصد افزایش پیدا کنه و گران تر بشه.
@News_Hut</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/news_hut/73285" target="_blank">📅 17:06 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73284">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">😶
🚨
🚨
این کانال باعث ورشکستگی خیلی از سایتای بت شده و پلیس FBI برای دستگیری ادمینای این چنل جایزه تعیین کرده
🔥
https://t.me/+bDapVmvigDhmYzZk https://t.me/+bDapVmvigDhmYzZk</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/news_hut/73284" target="_blank">📅 17:06 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73283">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/vgIeYZf0ZDLUcdTYd1lCrBGaKVLt7q0p_FD4yN8WezQVylrpyXAVEkmZglotRXLZi8rJuFuv_WB0YmBlEg30ofOOiRg0cEZg2cBbLWyskwfbwrs-_gdTYpoARPIjIY_putLKSHrWg5EwQOh2TXdLYdbSVmpUpYiZuW7bLekTKU_sIljsKpPnwDuptxPlDFmiWN7XqtLuWN9q_xTOZ_6oT6IpQH5WS2eAvRd-jSncxmt8kPjEWQqsRR-PfYQyGxHOJZcFxfJ0Yx8nyWDHqqOEw8P2torTr6hxu2f3wicsY4gdr_j1bK6wZg21fupd2PVIpV1Iq3HwyTLZnXG5-wzMTg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">😶
🚨
🚨
این کانال باعث ورشکستگی خیلی از سایتای بت شده و پلیس FBI برای دستگیری ادمینای این چنل جایزه تعیین کرده
🔥
https://t.me/+bDapVmvigDhmYzZk
https://t.me/+bDapVmvigDhmYzZk</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/news_hut/73283" target="_blank">📅 17:06 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73282">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bea561a653.mp4?token=JJLFIbQPrRZlxHHKkDEyVKk53iK3JR5lImM05_L0mT9Zz6DVPEI4kMo3ets5xWaFeP0cUjfILvZ-E5_GcVAWnHmzpuKD9IToxk16_yvYoN34bArF3q7QfoCSVwcdnm3h0fkaBgBb8oPdduczDy4YT-bwhrOOTQmpkM2BrxBdrDOOzawfZnLoMaG1G-UFHvkB_Vgd_CI_DVqtAiSeMrK9qI_SgqEInQ6bUDXdGjp35xxASVwMVkHBkSl_zf-1zDbgmpWVlQBeCoHyS7uL1_l1tEgzm2Z7nQ9i6YZ43s_gK9Vyigx0j7LnHDG6czNm4_oZERfSr1gZHsyXwu_c68lV6Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bea561a653.mp4?token=JJLFIbQPrRZlxHHKkDEyVKk53iK3JR5lImM05_L0mT9Zz6DVPEI4kMo3ets5xWaFeP0cUjfILvZ-E5_GcVAWnHmzpuKD9IToxk16_yvYoN34bArF3q7QfoCSVwcdnm3h0fkaBgBb8oPdduczDy4YT-bwhrOOTQmpkM2BrxBdrDOOzawfZnLoMaG1G-UFHvkB_Vgd_CI_DVqtAiSeMrK9qI_SgqEInQ6bUDXdGjp35xxASVwMVkHBkSl_zf-1zDbgmpWVlQBeCoHyS7uL1_l1tEgzm2Z7nQ9i6YZ43s_gK9Vyigx0j7LnHDG6czNm4_oZERfSr1gZHsyXwu_c68lV6Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پزشکیان در واکنش به پذیرش نظرات کارشناسی گفت:
من مگه دیوونم که اگه حرف درستی را به من بگن و من نپذیرم!
@News_Hut</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/news_hut/73282" target="_blank">📅 17:02 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73281">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/544a54e3ac.mp4?token=qpDFtX32nue8v8o4uXyiroI9lJrc-a2mClBbNFIUTzbhPInBcjQopN767U6YdzUn7kmwdvS_I7GHUMe-XAJu75Iy6PADK0LGNi3D9E4Pm6JB7pCqXwexxVXRmO51Q0kTPSk_vLk6PzlDmf0-fJMkR5Yj7HtVyCnGYV2KEvxeYsQY5-BARwgRFJw05X8HmnkykYm61LFBQRj6fdsSnbdKokqNDnT2sPpoS47qrxwHt0UtP-6hAVnh-zGFXcn0QXtVz8v4-JFcnnaC-fWRJetgyT2Ppfh3v9Lp-MyVG3KNdU4jKcFIHHB6GTkjUR4UsZMpHCg4s_Ueo4zt-5ITfU37vg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/544a54e3ac.mp4?token=qpDFtX32nue8v8o4uXyiroI9lJrc-a2mClBbNFIUTzbhPInBcjQopN767U6YdzUn7kmwdvS_I7GHUMe-XAJu75Iy6PADK0LGNi3D9E4Pm6JB7pCqXwexxVXRmO51Q0kTPSk_vLk6PzlDmf0-fJMkR5Yj7HtVyCnGYV2KEvxeYsQY5-BARwgRFJw05X8HmnkykYm61LFBQRj6fdsSnbdKokqNDnT2sPpoS47qrxwHt0UtP-6hAVnh-zGFXcn0QXtVz8v4-JFcnnaC-fWRJetgyT2Ppfh3v9Lp-MyVG3KNdU4jKcFIHHB6GTkjUR4UsZMpHCg4s_Ueo4zt-5ITfU37vg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">در جریان اجرای ارکسترال «آرش» در سالن اسپیناس تهران، در شامگاه جمعه ۱۷ مهر، تماشاگران در واکنش به صحبت‌های اسماعیل بقایی، سخنگوی وزارت امور خارجه جمهوری اسلامی، او را هو کردند.</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/news_hut/73281" target="_blank">📅 16:33 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73280">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/41a28d4b0f.mp4?token=G65KOthb1w7WkWcVJxtZg3YLlc21zAYPbsg1CeOM7btrGRdaSlQTEqKYWX1xy-sUEBABkuiMvL3r-x5GfUtXnLmLjfB5aMQY-xrAuY929bfEh4M9CIvx6jYElZJCrzu1X0OxmvD0QZgWDKzRSoSokZSn9Xar-hxDmvKNlfk7FJ45CnFpKtZYbPJBptr7uqbPHfJ2c73r6eGaunzR5LH7bowiqM1a0h27Ojsk7i6apdZVFyF92v4MGzk7KVN3VPqlVwzrLhEgGbF0g0vDgD_kwtvJOS2vPLxbneiNjcudIZIsBfY6C6mJT0JtpEwBzhBT1KNl-wgGRCTnT1i7YNRfjg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/41a28d4b0f.mp4?token=G65KOthb1w7WkWcVJxtZg3YLlc21zAYPbsg1CeOM7btrGRdaSlQTEqKYWX1xy-sUEBABkuiMvL3r-x5GfUtXnLmLjfB5aMQY-xrAuY929bfEh4M9CIvx6jYElZJCrzu1X0OxmvD0QZgWDKzRSoSokZSn9Xar-hxDmvKNlfk7FJ45CnFpKtZYbPJBptr7uqbPHfJ2c73r6eGaunzR5LH7bowiqM1a0h27Ojsk7i6apdZVFyF92v4MGzk7KVN3VPqlVwzrLhEgGbF0g0vDgD_kwtvJOS2vPLxbneiNjcudIZIsBfY6C6mJT0JtpEwBzhBT1KNl-wgGRCTnT1i7YNRfjg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تو ژاپن یه زن 29 ساله برای خودکشی از طبقه یازدهم میپره و روی یه دختری که داشته از خیابون رد میشده میوفته و دختری که از خیابون رد میشد جونشو از دست میده، در حالی که زنی که میخواست خودکشی‌کننده زنده میمونه!
حالا قراره این زن اعدام بشه...
@News_Hut</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/news_hut/73280" target="_blank">📅 16:01 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73278">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/G8O7Aoghy0tN1duxWcQ_Z1HQ-oWZfF1o1RLmmlHed4V2OUNnmYkYqTF1ULldSqznIqC8Ua0bbt9EcZsuEjrsoCXFV0U2QzzJDv-rEImNIA7kR98jq4lwtGr5AbQtb8mghZXIGaRRixbi4ZputJrchWzVBLN2tuYq1Kj7ehz7Zpx1S2K2f-Ef3TPK8A1BGTgJqt5loMWLWPmcivtGiigFf5dxBN6lMNCZ8NsKPE975lk0hjjH6vO-To2xsAggHFOEVdUjYdsBR-GIJfqv7cz4wjwRzMeHqHRwOB2KoU1xGlzRMGnZ6pncauWzQeGlxzTENuBxOg70Y2JCTxAvJk69zA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/1f8ef828fb.mp4?token=nS3Rbn2hUjDSS1ZsHn2jqsSuX2g8lG8x7o2frbaYbYDRRLYZ4Gw428SwQLnoF3AWXTRzC9jMV8_Hu82flwvMMeN9bmo1H4MTyxRaSS0_LA3S1zuJyAEfwTsBYdYQ5ZOWdDNeNYggehrWeyIqULJVXX_t9dNsagT4GnA0TaEM4zy664mF_0mPA-w63pTKbwmc_aNmpgUm3y39Hc4D8lBAMEWFKKW69U9ZBKtzg1ri6HZEdkGl7hSntz7S6dBjQLDXAf1pA7kiZWEznqDWCloM5lbYjqak-X6NRvzjCDA4CW451Q1C_e7aTuTwgpFPabU6sdnauqgQyc7LrWYxtYiOdA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/1f8ef828fb.mp4?token=nS3Rbn2hUjDSS1ZsHn2jqsSuX2g8lG8x7o2frbaYbYDRRLYZ4Gw428SwQLnoF3AWXTRzC9jMV8_Hu82flwvMMeN9bmo1H4MTyxRaSS0_LA3S1zuJyAEfwTsBYdYQ5ZOWdDNeNYggehrWeyIqULJVXX_t9dNsagT4GnA0TaEM4zy664mF_0mPA-w63pTKbwmc_aNmpgUm3y39Hc4D8lBAMEWFKKW69U9ZBKtzg1ri6HZEdkGl7hSntz7S6dBjQLDXAf1pA7kiZWEznqDWCloM5lbYjqak-X6NRvzjCDA4CW451Q1C_e7aTuTwgpFPabU6sdnauqgQyc7LrWYxtYiOdA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">علی سینا مصطفوی از بازداشت شدگان دی ماه، نوازنده و از معدود کوهنوردای ایرانی که قله اورست رو فتح کرده بود، امروز همزمان با اذان صبح اعدام شد
💔
@News_Hut</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/news_hut/73278" target="_blank">📅 15:25 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73277">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/016589a6d1.mp4?token=NvVgt0AR7oFWamb5Jnp-gIbTOcyYaOjqK8QISq8uSTtJnF-VS9m6ODXIF6ml_raBqrtqmqKJG4sj72d5DVxWJlVryhQMBSBWgPVpYa782IJOeKrUgd-7HU300Kdx_u1v5S7VZ7UhhRuIjy0uPBmZyUMPpugSfgAb432KLkE6Lm1Xw5vHKelzf4w-mUOM3ymcHWyTpXBfHJZKBGT2YwbBF1lBuLr213DKT_D_rCRGRM-pZD95Sy97hYhz6fZ2zzkXj5c_6m6l_TiWlWQBe769gS7rhIZK_qdbQ-vkLVSuan4IA7M_V5qlXIVo87IYvtx3sFDfvv7eizdJWaE2B514ag" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/016589a6d1.mp4?token=NvVgt0AR7oFWamb5Jnp-gIbTOcyYaOjqK8QISq8uSTtJnF-VS9m6ODXIF6ml_raBqrtqmqKJG4sj72d5DVxWJlVryhQMBSBWgPVpYa782IJOeKrUgd-7HU300Kdx_u1v5S7VZ7UhhRuIjy0uPBmZyUMPpugSfgAb432KLkE6Lm1Xw5vHKelzf4w-mUOM3ymcHWyTpXBfHJZKBGT2YwbBF1lBuLr213DKT_D_rCRGRM-pZD95Sy97hYhz6fZ2zzkXj5c_6m6l_TiWlWQBe769gS7rhIZK_qdbQ-vkLVSuan4IA7M_V5qlXIVo87IYvtx3sFDfvv7eizdJWaE2B514ag" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اسرائیل کاتس، وزیر دفاع اسرائیل:
اگر حزب‌الله در حمله به اسرائیل به ایران بپیوندد، ضربه‌ای سنگین دریافت خواهد کرد و بخش‌های دیگری از خاک خود در جنوب لبنان را از دست خواهد داد.
بیش از یک میلیون شیعه در لبنان آواره خواهند شد.
@News_Hut</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/news_hut/73277" target="_blank">📅 14:56 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73276">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6b6d991be7.mp4?token=fBmY-BdzSdULT-caD9eE8Vx7ACLHsQnS-F5QwbhushXTTN-kmKoHTup1sR0IDEFM0lYyBxL1UCsSqYCeKrGNCejS01cAD5Usuuv78wLvLxtNqoHgwmnbXl7jOiNaeJK5ee-zP_xRiGyI_X2fASv6undnS5QVryrDOh0X_vYKq3s_QOcgcOSeVPk0V4MTL2hlmI9pybp2L0Q7DyVm6w-7dpkINUqMjdalEIxDplpeKrP3Wx50BX_YnKmp61juYeTfLX4xV775VM3J6wEA8eI2sn7YDbTnqXWtHtqK8UmGmvlu8e1oXYfuEhITZieGQZbF2-l8MV-t7dFc-tHYJkYxaw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6b6d991be7.mp4?token=fBmY-BdzSdULT-caD9eE8Vx7ACLHsQnS-F5QwbhushXTTN-kmKoHTup1sR0IDEFM0lYyBxL1UCsSqYCeKrGNCejS01cAD5Usuuv78wLvLxtNqoHgwmnbXl7jOiNaeJK5ee-zP_xRiGyI_X2fASv6undnS5QVryrDOh0X_vYKq3s_QOcgcOSeVPk0V4MTL2hlmI9pybp2L0Q7DyVm6w-7dpkINUqMjdalEIxDplpeKrP3Wx50BX_YnKmp61juYeTfLX4xV775VM3J6wEA8eI2sn7YDbTnqXWtHtqK8UmGmvlu8e1oXYfuEhITZieGQZbF2-l8MV-t7dFc-tHYJkYxaw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خانوم دکتر:
یه خانومی به من پیام داده و گفته که من به غیر از شوهرم 3 تا دوست‌پسر دارم و با هر سه‌تاشون رابطه‌جنسی دارم چون هر کدومشون برام یه لذتی دارن ...
هیچکدومشون هم از اون یکی روابطم خبر ندارن و 7 روز هفته رو تقسیم‌بندی کردم و پیش همه‌شون میرم !
اخیرا حامله شدم و چون نمیدونستم بچه از کدوم یکی رابطه‌هام هست، بچه رو سقط کردم ولی الان به‌شدت خون‌ریزی دارم ...
موقعی که با همسرم رابطه داشتم اون از این وضعیت شاکی شد گفت برو دکتر ببین برای چی این شکلی شدی؛ الان سوالم اینه اگه برم آزمایش بدم مشخص میشه من با دوست‌پسرم رابطه داشتم یا اینکه از دارو سقط استفاده کردم؟
@News_Hut</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/news_hut/73276" target="_blank">📅 14:32 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73275">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">خبرگزاری مهر:
«افسانه عقیله»، عضو سپاه پاسداران و فرمانده حوزه بسیج خواهران شهیده افضل در مهرستان استان سیستان و بلوچستان، امروز در حمله‌ای کشته شد.
@News_Hut</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/news_hut/73275" target="_blank">📅 13:56 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73270">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KMrd47ztJry4b9MRGteYbltQTkEXW9Vxdh4X1RyctQAV1Qd1a38WS9oTHLM9iifH8mUGCEOs_kruBX-jYZUuBvf4rUlheQoJo46Fjl272dn1j4Ua2TZ0SV_2HvkgLKPqRIzfkvA2dQD8dMbZETB9DizQTOPb5dR_PJ6WfzvehpB8k027hcXsT5GmnvrLzIGitDExcOD5vkrPikV5LA5GfYRlBbCPmaPME8wg63JFaPMt_ko2e-3In6woR0B9mrdnMCxVBZqTsCO4Zy8cXfeSlqnIA00W3vKGfBlLLZgyVG6Vv8VaDZpljchW8SG70wJJFMzN4fnrJRj3Soesed_YrQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f0bb97d458.mp4?token=m9oCi1uD9Otm4bcP59jG7wxunc5Lkgs-Hj9ZKHRs82y7XdjuIetjGIDFC21e7BvLq-eh5nTEYo2pVTnvcujVN3kPddJu_XZIzz9pMj5i6KZ_gvMp_pp89mZGZ--Vjydb22sWP3nNvD40TapjfJ-FdP5flK462HItrXrNneDUgp_q-dwYpqHVlynY2Geb6z15PMU95QPdY2zJ_KR83IPIlp507EsbOemNHNSkRlQwn58cVoQN_AqEz1J6IYV79U_RJh7GB0fcGpaRNUhmzT-x0ySZtJcz1AiMpo-GB7nLUHRL-2Xw_eyF6Ra7bE93ZtszgVgGZbDP3NoJx_6BGWo7RIi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f0bb97d458.mp4?token=m9oCi1uD9Otm4bcP59jG7wxunc5Lkgs-Hj9ZKHRs82y7XdjuIetjGIDFC21e7BvLq-eh5nTEYo2pVTnvcujVN3kPddJu_XZIzz9pMj5i6KZ_gvMp_pp89mZGZ--Vjydb22sWP3nNvD40TapjfJ-FdP5flK462HItrXrNneDUgp_q-dwYpqHVlynY2Geb6z15PMU95QPdY2zJ_KR83IPIlp507EsbOemNHNSkRlQwn58cVoQN_AqEz1J6IYV79U_RJh7GB0fcGpaRNUhmzT-x0ySZtJcz1AiMpo-GB7nLUHRL-2Xw_eyF6Ra7bE93ZtszgVgGZbDP3NoJx_6BGWo7RIi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ساعتی پیش، اوکراین بوسیله پهپادهای انتحاری به پالایشگاه نفت نووشاختی در منطقه روستوف روسیه حمله کرد که باعث ایجاد انفجار و آتشسوزی گسترده شد.
@News_Hut</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/news_hut/73270" target="_blank">📅 13:40 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73267">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jpjNNPZYNUksWkPn4MODDBNlGP6St74Z56efvzYvJGg6yj2P-Vx_zNsxvNFrQXgmIVGjgp3yxNMtV4qE0R2p7GALa45MtE2YyESpxRVjsb8ZQImAW2Aac-fOAW8XKoztR6KCY455tT4BzIkFaUIm3xN4rBaLCCl8jtqlG86DE9CckPITpPScf-q6lLklFRyn149bMHkw1SBApAC8-eVNN8qyQs55EtzYy-Q9xC603u2AJdLMxSFrj2e4temOPpJ6hBvWwm02YmqOaBb24leubZdqGg9GAvJMRfO4qx0cA2TJ4UPhL5mkGClK_Cj0We6DNklkpncrhgBmlAzH-LoL2w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Q6U3YZSoAU0XBL3ELUiFyfqQRpPWetaRm-EI1_IgKPTekNQCYlRtsEjoOmQCKFegDwMP-aihkwek6Srfr0r9JkQbrnwFcjm3qYUuN0iDoFaIVJrPtHhuegPt_SqzFAK9UrxNQqF8Qjior_Iwywtw8v2TUG9_taZ8qKUhhtGERuXg47mpBrXLrI5gwdCRlmPfWeUlX9O_6wJlNShFjKmZPkMekv7qjE2LeCRyWKno3AnbrUJ7a2eGuQYZbkwMrM3OgqbZkgHMIlzf85Hz39yC_PD5vIfH9zvO7idQF7NbJVgcijfCbwfEhbbQ5ZNg-vQcEiwXMohXQN_RiOO9IB8nHg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dd22e2bf5b.mp4?token=qML0XIalkQqBdLCJ2mshJmRXusevmcjRIud9R-sc3sCFLDGxjapZYGSY9x2OCXAT36x9b6WqDPXU4rKKGYBFsh5_ibnvWqvjmHKuozLMkB5-T7pXwrvgomav9cQJ0JWRvx95APx45USdmwSlB3qm4AiReR8XNqvk9F0a7Zxm7XBHNs41T-1gZv8hyiOhLpvCsJPWTMHQQ8Tsb-TjtVJeJ9NC8HhxR9BJgMTbBRuk4NDkW98ggk9kkGQlazEzFnhc81VlSMsn0ST-IXTddVGjkYDm3jzBNz9nwGIRf_LLbg_D-XAsxxthYeGORaGZi2OCi_NPhKp4lY5mRmdds74Y9g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dd22e2bf5b.mp4?token=qML0XIalkQqBdLCJ2mshJmRXusevmcjRIud9R-sc3sCFLDGxjapZYGSY9x2OCXAT36x9b6WqDPXU4rKKGYBFsh5_ibnvWqvjmHKuozLMkB5-T7pXwrvgomav9cQJ0JWRvx95APx45USdmwSlB3qm4AiReR8XNqvk9F0a7Zxm7XBHNs41T-1gZv8hyiOhLpvCsJPWTMHQQ8Tsb-TjtVJeJ9NC8HhxR9BJgMTbBRuk4NDkW98ggk9kkGQlazEzFnhc81VlSMsn0ST-IXTddVGjkYDm3jzBNz9nwGIRf_LLbg_D-XAsxxthYeGORaGZi2OCi_NPhKp4lY5mRmdds74Y9g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نیروی دریایی سپاه پاسداران اعلام کرد که یک کشتی کانتینربر حامل بیش از ۲۵۰۰ کانتینر، هنگام تلاش برای عبور از تنگه هرمز از مسیری غیرمجاز، با یک مین دریایی برخورد کرد.
این کشتی صبح چهارشنبه در جنوب تنگه دچار آتش‌سوزی شد و غرق گردید.
@News_Hut</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/news_hut/73267" target="_blank">📅 12:56 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73266">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">تا انتخابات اسرائیل و آمریکا چقدر مونده؟
فقط ۱۳ روز تا انتخابات پارلمانی اسرائیل در ۲۷ اکتبر ۲۰۲۶ مونده.
انتخابات میان‌دوره‌ای آمریکا هم ۳ نوامبر برگزار می‌شه و ۲۰ روز تا اون باقی مونده.
@News_Hut</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/news_hut/73266" target="_blank">📅 12:14 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73265">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qWNS9ClQfcef-yP-fgGtk0l8u83yByu96OhDJL4FY91eOVk34qeRLZ4K4pjsOjINxie_aC4QkrYR89DPiJ3TzqxQTB6mZgfxhRNvhGQ3-mYlvJIjGENTRWHe1Qng2iQfq8Strt07QWmBOhscZLhIlaGW6DcvErTOEy1jtUezHJfr8Uk5VOGfi5ikkN5SXuVvjp-I3AB7b9GgJRaRZ2lY1gDtvM9gf-3LgQnvW5uiFoFT1ewOo2mOj402iLkppKk5QCe95-vHYnRfaIlcfiQs682yFUMRuXPYVnr2f34DcBK5tkLHkWMQ3fm-XME686gB9jnvaUgwAIHbMm0MAj_E6g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🇺🇸
#فوری؛پست جدید دونالد ترامپ در تروث سوشال:ترامپ ویدئویی منتشر کرده که در پایان اون بخشی از سخنرانیش در زمان آغاز حملات مشترک آمریکا و اسرائیل به جمهوری اسلامی آورده شده که میگه:
🇺🇸
ترامپ: این رژیم به‌زودی درخواهد یافت که هیچ‌کس نباید قدرت و صلابت نیروهای…</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/news_hut/73265" target="_blank">📅 12:04 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73264">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromهات نیوز | HotNews</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/240fbc3c81.mp4?token=UiqncOKKtNvWtXREenapIuqeY_1V_PWFa0fLWV8zuGc1GcNjZGsYB3vfn95QatEGqfN9wYznw0OSsGv6W8ftOnnNXhctZ3u9DBsOp6b0bqTavNH6r51w9On87RJGPo2gNAfa2rk-xD6rhjHV_DJXHPGoN0qRU1R9BPggEW0UUinTZgBabdJelveHYr1T9Ri5tUiVS0KJTfDtsQwE67TzDzgMINgW-qj-8pu1BmuvdUMM1Jsc-ZHjCWT0OOmdiIr6OCDHCzExxK3vgFE0wfQBTKhdRrbi0_-aZINo0453U4n4HEnTW1snudqlj9P7htfEqglbQtBOw6N9LaDx5E8Vrg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/240fbc3c81.mp4?token=UiqncOKKtNvWtXREenapIuqeY_1V_PWFa0fLWV8zuGc1GcNjZGsYB3vfn95QatEGqfN9wYznw0OSsGv6W8ftOnnNXhctZ3u9DBsOp6b0bqTavNH6r51w9On87RJGPo2gNAfa2rk-xD6rhjHV_DJXHPGoN0qRU1R9BPggEW0UUinTZgBabdJelveHYr1T9Ri5tUiVS0KJTfDtsQwE67TzDzgMINgW-qj-8pu1BmuvdUMM1Jsc-ZHjCWT0OOmdiIr6OCDHCzExxK3vgFE0wfQBTKhdRrbi0_-aZINo0453U4n4HEnTW1snudqlj9P7htfEqglbQtBOw6N9LaDx5E8Vrg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
🇺🇸
#فوری
؛پست جدید دونالد ترامپ در تروث سوشال:ترامپ ویدئویی منتشر کرده که در پایان اون بخشی از سخنرانیش در زمان آغاز حملات مشترک آمریکا و اسرائیل به جمهوری اسلامی آورده شده که میگه:
🇺🇸
ترامپ:
این رژیم به‌زودی درخواهد یافت که هیچ‌کس نباید قدرت و صلابت نیروهای مسلح ایالات متحده را به چالش بکشد.
🎙
سخنگو:
او به جهانیان یادآوری کرد — همان‌طور که بارها و بارها گفته است — که آمریکایی بودن، نمادی از چیزی شکست‌ناپذیر است.
اگر آمریکایی‌ها را بکشید، یا هر جای این کره خاکی آن‌ها را تهدید کنید، ما بی‌هیچ عذرخواهی و درنگی به سراغتان می‌آییم و شما را از بین می‌بریم.
ما آغازگر این جنگ نبودیم، اما در دوران ریاست‌جمهوری ترامپ، آن را به پایان می‌رسانیم
جنگ آن‌ها علیه آمریکایی‌ها، به انتقام ما از آیت‌الله‌شان بدل شده است
🔴
ترامپ:
خطاب به مردم بزرگ و سرافراز ایران:
لحظه آزادی شما فرا رسیده است.
وقتی کار ما تمام شد، کنترل حکومت را به دست بگیرید؛ این حکومت از آنِ شما خواهد بود.
@News_Hut</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/news_hut/73264" target="_blank">📅 12:02 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73263">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/377d554e40.mp4?token=NjSCYPcmvQBRr19QBqY5T9T2v2eTv5pYBLqL5cVQ2pzolMCcwEeIk2XGB39OmHl-JPiL6ozQTFUxQ2s3tYBjxsxfac8ZJah6cRcHcPBVkWhAQX9Z5BT7uJih-5EcPZhdUoRHj3qZfPqcXy5JdoWL0ZUNWtec7TenI0Md_4FSfpFYGimJcdZ3RGw1QDHB-n5_f6rSbElrIsp9zoaUzm1YcSyQ6JJPrczaXXnxI1CZssuAWMtuFF_M-YaVG-L5SMhncBOwG6eyZ5uhHIcggVL-UVLgh-BX0sSrqsyIkUiOGeXSJYRZ7J36vm5cZVAemXafk2J13skHqApR6EVP0HB1xQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/377d554e40.mp4?token=NjSCYPcmvQBRr19QBqY5T9T2v2eTv5pYBLqL5cVQ2pzolMCcwEeIk2XGB39OmHl-JPiL6ozQTFUxQ2s3tYBjxsxfac8ZJah6cRcHcPBVkWhAQX9Z5BT7uJih-5EcPZhdUoRHj3qZfPqcXy5JdoWL0ZUNWtec7TenI0Md_4FSfpFYGimJcdZ3RGw1QDHB-n5_f6rSbElrIsp9zoaUzm1YcSyQ6JJPrczaXXnxI1CZssuAWMtuFF_M-YaVG-L5SMhncBOwG6eyZ5uhHIcggVL-UVLgh-BX0sSrqsyIkUiOGeXSJYRZ7J36vm5cZVAemXafk2J13skHqApR6EVP0HB1xQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دیروز تو بریتانیا، یه مرد جوون وارد محوطه ببرها تو پارک حیات وحش یورک‌شایر میشه و اونجا یکی از ببرها به نام آلتای بهش حمله می‌کنه و نهایتا میکُشتش!</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/news_hut/73263" target="_blank">📅 11:31 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73262">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/news_hut/73262" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/news_hut/73262" target="_blank">📅 11:31 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73261">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cMWo-7bt82Ha_Njqz7gpRk82rRNeffGjSfavkKrraEYkBf0WHgJKF5UOcG99xCYka2Wfty-K0BdetK6NKqn8V7H_u4xGA_tivnsarVeaZ0ao5r2O8P9ZcgHea2ednmdjJS0uKDy9Ixo9oA-4QVftfPAMIicqLPPO0TQ3sR8x9cXjlnjRA4lAZemSbwkjym-Rq8qtNFUSTmzcc2C3sA2Qf4sfr2q257xtNl9OFT0gPkfe-KGxfDXFHYb8v5HH91W2D2R4vYWRIaaneyjOSZQcopxFqm8KgAd9P44-mvi-tU40fmtmp2EBL-0YOmpVOmxDzVzVRAOAkbIPZ1zYYjKUgA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🦖
مچ‌های مهم امروز در سایت بین المللی
TrexBet
لیورپول
🆚
لاسک
فنرباغچه
🆚
استون ویلا
دورتموند
🆚
بودو/گلیمت
پاریسن‌ژرمن
🆚
منچستر سیتی
پورتو
🆚
رئال بتیس
رئال مادرید
🆚
رم
پرسپولیس
🆚
خیبر
🦖
🦖
🦖
🦖
🦖
بونوس اولین واریز تا سقف ۱۰۰ یورو
🦖
بهترین ضرایب بین تمام سایت‌ها
🦖
واریز آسان و امن از طریق کارت به کارت، ووچر، کریپتوکارنسی
انتخابت رو انجام بده و آماده‌ی هیجان باش!
TREXBET — PLAY. PREDICT. WIN.
https://TrexBet.com
T.me/TrexBet_Ir</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/news_hut/73261" target="_blank">📅 11:31 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73260">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">استانداری هرمزگان:
دقایقی پیش یک پهپاد با یک لنج صیادی متعلق به شهرستان سیریک در محدوده بندر کلاهی برخورد کرد. بر اساس اطلاعات اولیه، در پی این حادثه سه نفر مصدوم شدند.
@News_Hut</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/news_hut/73260" target="_blank">📅 11:12 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73259">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bf6e01fafb.mp4?token=mkA53g-Z7WuUc9y7iZAkgQO0IacDxOtLOFt_dJt3Pv5qEZTdCZ_2ZlTpgXk1c1NqahEfNtafTBRy3uIQwJ_s5VT4HxBMo9zPkzkTVz7W6eLwFtFx1X5CFwSxoxz7cyARtwnw8UdBcri47HW21a4ozwd-m8baY4rti3EsDgz4X9c6UOnfGasnCbDef5OJ-u4O9D1SmTEeO3E_bW_6DkFEBQHaB4mlyfdKwH0siKUk3h5Z1YHVS0ARN1cSVeOOaHEOOx8CkLTt3AmuPjq-Qn9F0f8MSJuw5Q_KhKGu9SV--QjR6zxLjupTIgjQoIlt02Lh1gFKdScipIMpUwnA6HfG2Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bf6e01fafb.mp4?token=mkA53g-Z7WuUc9y7iZAkgQO0IacDxOtLOFt_dJt3Pv5qEZTdCZ_2ZlTpgXk1c1NqahEfNtafTBRy3uIQwJ_s5VT4HxBMo9zPkzkTVz7W6eLwFtFx1X5CFwSxoxz7cyARtwnw8UdBcri47HW21a4ozwd-m8baY4rti3EsDgz4X9c6UOnfGasnCbDef5OJ-u4O9D1SmTEeO3E_bW_6DkFEBQHaB4mlyfdKwH0siKUk3h5Z1YHVS0ARN1cSVeOOaHEOOx8CkLTt3AmuPjq-Qn9F0f8MSJuw5Q_KhKGu9SV--QjR6zxLjupTIgjQoIlt02Lh1gFKdScipIMpUwnA6HfG2Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">چند وقت پیش تو مکه-عربستان، یه کفتره با گردنی شُل درحال مرگ بود؛
که گروهی از زائران رفتن بالاسرش و گفتن حیوونِ خدا داره نماز ميخونه و حسابی به وجد اومده بودن:
@News_Hut</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/news_hut/73259" target="_blank">📅 10:57 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73258">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/c20d7f23a2.mp4?token=i3SeBbcZFwzBde2iCKrBklKbL5reeKZ6OoTxDmuvpClyndoLM1jegVqNrz4WhubfhGuWr8w3liGX25NOMgEKvCVw21hznW4CX6Bq7aANWKujN1Xy7DvK_xR--ROlBdsPe1uPwBo0IDIsL350OezQWQCpTu1XKDJnaVQFLCknXllTky7ijQON1J-V253C5iM472ocICi1L4U0A-sA4EWhQLqi8vpKuxardp7kjmgFPFAYpRhzMNTch1BviSDMSUmiAGc7Yin9u4TPt2GLp8pnw_jwHJ5peNd-EiPIerVRk_Oit8jx3Y_1eeW_SkIxgdEhOCgYMsUs23q1QIEkuQy_yQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/c20d7f23a2.mp4?token=i3SeBbcZFwzBde2iCKrBklKbL5reeKZ6OoTxDmuvpClyndoLM1jegVqNrz4WhubfhGuWr8w3liGX25NOMgEKvCVw21hznW4CX6Bq7aANWKujN1Xy7DvK_xR--ROlBdsPe1uPwBo0IDIsL350OezQWQCpTu1XKDJnaVQFLCknXllTky7ijQON1J-V253C5iM472ocICi1L4U0A-sA4EWhQLqi8vpKuxardp7kjmgFPFAYpRhzMNTch1BviSDMSUmiAGc7Yin9u4TPt2GLp8pnw_jwHJ5peNd-EiPIerVRk_Oit8jx3Y_1eeW_SkIxgdEhOCgYMsUs23q1QIEkuQy_yQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">این کلیپ شاهکار از کنسرت چند تا پسر توی خوابگاه دانشجویی، فقط توی چند ساعت میلیونی بازدید خورده:
@News_Hut</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/news_hut/73258" target="_blank">📅 10:29 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73257">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/i0noc0NAQFS466MWTVem-4tEUjM1tHYawvqWClngnZbbDXOSYzVQ2ld87xT90gEStAK6iG7Y8sF3m504hiKQDNbKCpI6EkWEcVEsIz28akbJzDDlMj_KL0TfZ7bmzzOfcMHIV7fM5F_QeW-PF4HDMeBtYZ6c0SP-DjZZW3uZZnHvUXr92QXriBG_8ey-hkXlRe8efrpNq2dWGALnC8KyH3LRVgbPBO0oxbGJuERSezcdNi9MSYM9PzzLLrh_YwU_rbbr7x4NQq5qlhG5nymrUCf0RoMfqvN-0B23cMEa0CvKP9ZZqwS54DcEtr29SyueaXUdGLJ85vU6QE6k0tKB7A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رصد ۱۰۵ هواپیمای نظامی در منطقه طی ۲۴ ساعت گذشته
۱۰ هواپیمای ترابری ورودی از خارج منطقه:
فرانسه: ۳ فروند
آمریکا: ۳ فروند
بریتانیا: ۲ فروند
عراق: ۱ فروند
کویت: ۱ فروند
۸ فروند هواپیمای ترابری نظامی منطقه‌ای
۴۵ فروند هواپیمای سوخت‌رسان
۷ فروند هواپیمای جاسوسی و شناسایی
۳۴ فروند هواپیمای ترابری نظامی که در داخل منطقه جابه‌جا شده‌اند
۱ فروند بالگرد نظامی
مجموع: ۱۰۵ هواپیمای نظامی در ۲۴ ساعت گذشته.
@News_Hut</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/news_hut/73257" target="_blank">📅 09:49 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73256">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1a8ff56bcd.mp4?token=QNv-KMTN_1RALc1X-agckbnkjRG2YXJa2jDvmYc8FSJFLU6tx6W5Y-p4XEcYPTojcKiRnmiAl46CxbOJyzBmRWi9zfu7TnwP8ewAeUicGpedv6OLvkU625n4DQMWX9-L1dq6siFLUJEV3I-FJnfAe3eJqp5mrlikjJ3nwpPcqcGwtol6PuFpOyMf9pThQF8mN0dnnspaK_2SJUwJP_mIpcng1fbUoJhpNnPRTkYvTWxlZh-T-Sw5FailjVVxJ-G2PgV2pK5GSPNLaaZxuVlxBtnwze8IZmSSfe6p7dDKe4KcsxWztUHHyw0xD4lhTamYTs0c3uHzN5rCQDtxtCh_5g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1a8ff56bcd.mp4?token=QNv-KMTN_1RALc1X-agckbnkjRG2YXJa2jDvmYc8FSJFLU6tx6W5Y-p4XEcYPTojcKiRnmiAl46CxbOJyzBmRWi9zfu7TnwP8ewAeUicGpedv6OLvkU625n4DQMWX9-L1dq6siFLUJEV3I-FJnfAe3eJqp5mrlikjJ3nwpPcqcGwtol6PuFpOyMf9pThQF8mN0dnnspaK_2SJUwJP_mIpcng1fbUoJhpNnPRTkYvTWxlZh-T-Sw5FailjVVxJ-G2PgV2pK5GSPNLaaZxuVlxBtnwze8IZmSSfe6p7dDKe4KcsxWztUHHyw0xD4lhTamYTs0c3uHzN5rCQDtxtCh_5g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نتانیاهو درباره ایران:
این رژیمی متعصب است. تا زمانی که پابرجا بماند، برای احیای خود تلاش خواهد کرد.
تلاش خواهد کرد برنامه هسته‌ای‌اش را از سر بگیرد؛ دوباره برای نابودی ما، و بازسازی حزب‌الله و حماس تلاش خواهد کرد.
برای نابودی کامل این تشکیلات، باید این رژیم را سرنگون کنیم.
@News_Hut</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/news_hut/73256" target="_blank">📅 09:40 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73255">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cc5f754c70.mp4?token=hYSvOUPiZdC6psz7X26Djlc2CjA-Wxzoaa76yl6wLMG_kEg2J7CUbx74C0CSLJtXyMoUpG2qjhe9Pgqud-VojdocHK3IvU3yt5UhQR2NdZtH-a72g1e4ImuMuEFx8ofaCaa17Wf5gGyhjdX4Fh6ilicChgdiVYDxZ2wC40gOENRTsyzm3-CNm0nNdq5TrQG3EKvC0vGi574W4fhcoTTuy5Xec7LCZaYzVxk57_DTRYZm5sJVSpA208a-9qnUz_yC0DJ0_7NOl4IjI19TI44gCx1X1XLhMNHPV9nATnrXTnbS-7Onb6h6yzbJ1qWUdvrNLLaCEJ4Wpmov0vfpy3-U_VGv7MgXdxx_hEVCwlCYiDQzqK3GwB4LxB1MM0jp48y8KT3XdqMABSwqDIX0rIQhqEUrDqySIWBKfBbJEXTDe4zL_E0mvRI3o8tpiGgbVtd-BJkxNIcGmAzVi7AH9pUzYefKrKcjQHI4PwFPYJ_0J5BBA9OdZsaFz2maR-fPDxNi8cSg0lkhpFb1IPyyiK06CYZDyUhzcyVig_9aqkvzSq-Kqs41O1ehx6TYYLAHPFGnbDvy6pA76hiPk_ghCFT5Uzw6Xx7c1k8AcVBB8W_iC9t6w3d2xwoNaIzKj-ny7p4WUyxO7GeuBEutv3cYd4XjH-LM-1nbUCkO1q3VtbWxvvY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cc5f754c70.mp4?token=hYSvOUPiZdC6psz7X26Djlc2CjA-Wxzoaa76yl6wLMG_kEg2J7CUbx74C0CSLJtXyMoUpG2qjhe9Pgqud-VojdocHK3IvU3yt5UhQR2NdZtH-a72g1e4ImuMuEFx8ofaCaa17Wf5gGyhjdX4Fh6ilicChgdiVYDxZ2wC40gOENRTsyzm3-CNm0nNdq5TrQG3EKvC0vGi574W4fhcoTTuy5Xec7LCZaYzVxk57_DTRYZm5sJVSpA208a-9qnUz_yC0DJ0_7NOl4IjI19TI44gCx1X1XLhMNHPV9nATnrXTnbS-7Onb6h6yzbJ1qWUdvrNLLaCEJ4Wpmov0vfpy3-U_VGv7MgXdxx_hEVCwlCYiDQzqK3GwB4LxB1MM0jp48y8KT3XdqMABSwqDIX0rIQhqEUrDqySIWBKfBbJEXTDe4zL_E0mvRI3o8tpiGgbVtd-BJkxNIcGmAzVi7AH9pUzYefKrKcjQHI4PwFPYJ_0J5BBA9OdZsaFz2maR-fPDxNi8cSg0lkhpFb1IPyyiK06CYZDyUhzcyVig_9aqkvzSq-Kqs41O1ehx6TYYLAHPFGnbDvy6pA76hiPk_ghCFT5Uzw6Xx7c1k8AcVBB8W_iC9t6w3d2xwoNaIzKj-ny7p4WUyxO7GeuBEutv3cYd4XjH-LM-1nbUCkO1q3VtbWxvvY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">#فوووری
؛پرزیدنت ترامپ درباره ایران صبر کنید تا ببینید با ایران چه می‌کنیم. کارشان را خواهیم ساخت؛ صبر کنید تا ببینید. آن‌ها هم فقط منتظرند.
صبر کنید تا ببینید با ایران چه می‌کنیم، چون دیگر کاسه صبرمان لبریز شده است. می‌دانید، دیگر به آخر خط رسیده‌ایم.
اما خب، این‌ها اهمیتی ندارد. مسئله مهم این است که قرار نبود آن‌ها سلاح هسته‌ای داشته باشند و نخواهند داشت؛ این موضوع زیر هزاران تن سنگ دفن شده است.
@News_Hut</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/news_hut/73255" target="_blank">📅 09:12 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73254">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6a1adb1098.mp4?token=rHRDUPN0P6qyf3wTD8zWJrPJBbCauGTrU_01sSxdzl4EEZoUMTzksXjM9dw8nZUX3yLPP4f06hbslM5kzaypsvEKNdZgPK2D7fISkxkkIgGSGSSLk1M-nzIuQhCZ7ZCye0ZN0ysP0mhfGvqiQ6DzaCSvmkI11ZVuK8Q8gEtihdKlUHw7ujgF8c1UdQcNfVYdu_noYTAyCjwd3N17W81Uc4X72--MpkRK-EjagiK57pBuzdoXRV5AaIzpXrosZqlXXGs7fMFHOLfwL6ZTCPkwGbeXlogBD-caclFvMBofgxlvSKz3JpTSVXnrmiM8CBpxFFnmUssNhbpp0erieNueQw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6a1adb1098.mp4?token=rHRDUPN0P6qyf3wTD8zWJrPJBbCauGTrU_01sSxdzl4EEZoUMTzksXjM9dw8nZUX3yLPP4f06hbslM5kzaypsvEKNdZgPK2D7fISkxkkIgGSGSSLk1M-nzIuQhCZ7ZCye0ZN0ysP0mhfGvqiQ6DzaCSvmkI11ZVuK8Q8gEtihdKlUHw7ujgF8c1UdQcNfVYdu_noYTAyCjwd3N17W81Uc4X72--MpkRK-EjagiK57pBuzdoXRV5AaIzpXrosZqlXXGs7fMFHOLfwL6ZTCPkwGbeXlogBD-caclFvMBofgxlvSKz3JpTSVXnrmiM8CBpxFFnmUssNhbpp0erieNueQw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تولیت آستان قدس رضوی:
توفیق اقامه نماز با رهبر انقلاب را داشته‌ام؛ حال ایشان بسیار خوب بود
رهبر انقلاب پیش و پس از تدفین رهبر شهید در مشهد حضور داشتند
@News_Hut</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/news_hut/73254" target="_blank">📅 09:00 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73253">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">فک کنم اگه هرشب با ۱۰۰ هزار تومن میومدین چنل بت ما، شبی بالای ۲ میلیون سود کرده بودین مثل دیشب :)
😊
😂
میگی نه؟ بیا تو چنلمون و ببین!
🔥
@FutballFuckBet @FutballFuckBet @FutballFuckBet @FutballFuckBet</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/news_hut/73253" target="_blank">📅 01:52 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73252">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/hJj6VCGsV0vCdnT863Bl19SzIHLiym8H5REtP4gxj-ieZILPYcsMXnQSyePHzwMxLB-lnfMfomMhmUP0zwimBEuKa-RVkXOgG1SMW-rmbeH99OJ2xgl0sFdd_rzZJxI0U87S0NB25EKUzYLztoyLY2nsf3olxujW0bghgEKsrUF5fiKNjGWbqtSQB7RyTHI1ShtQSclGw1yCzBNqK71whhwwzYsY8R4sYLBAM_DkwCntyeuOj5jlbMGF2xdW1_3lEXn3qGkcGUPQ6OCYGYm8voLrXrNyMlwoZaBggzsQ7yXY8U-WUwvuHRrc17ge3bVaORCYyinsetn2OaKbE5Jp6w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فک کنم اگه هرشب با ۱۰۰ هزار تومن میومدین چنل بت ما، شبی بالای ۲ میلیون سود کرده بودین مثل دیشب :)
😊
😂
میگی نه؟ بیا تو چنلمون و ببین!
🔥
@FutballFuckBet
@FutballFuckBet
@FutballFuckBet
@FutballFuckBet</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/news_hut/73252" target="_blank">📅 01:52 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73251">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">حوثی‌ها به مقر شرکت «آرامکو» عربستان در ظهران حمله کردند؛ این اقدام ساعاتی پس از آن صورت گرفت که آن‌ها به‌طور علنی این مکان را به عنوان هدف تلافی‌جویانه معرفی کرده بودند.
وزارت انرژی عربستان تأیید کرد که یکی از ساختمان‌های اداری در مجتمع آرامکو در ظهران هدف قرار گرفته و منجر به وقوع «آتش‌سوزی محدود» شده است؛ این حادثه تلفات جانی در پی نداشت.
خبرگزاری رویترز از شنیده شدن صدای انفجارهای مهیب در نزدیکی این مقر، وقوع آتش‌سوزی و صدور دستور تخلیه خبر داد و اعلام کرد که به کارکنان گفته شده است روز بعد از خانه کار کنند.
@News_Hut</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/news_hut/73251" target="_blank">📅 01:30 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73250">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lKIu7vqyWhOfu_iARDPMOKta6nwYG8RmS10QOqRll_qzmHEjRdHlxatXwQ429T5U2fOl3nNgkB3fh9eAasfxqT3fDOL7BS6W4tKVAxbcwgxOiRSAQ5k5sp7PdPthtnr90isJVwwxDhSyN5Rm93vMSOdRNR5N0vZ1hMFOK3S9kT_eScr-eASEL_Hr87zDSKE5J8lrqhrWsGUt2OfxeM3PyiwFLgYduPubc9CqZOmQoXf7C75ofFbiNoKhRN4VRvxCuPehYPS5OPrvmU89pYHeoeLixXdZ8tscOvuUUSfLSqE4YdLT00twGEKPy5fKQyzkEbBq1HHRM0XDwmKuflqa2Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ناو هواپیمابر آمریکایی «جورج اچ. دابلیو. بوش» به همراه حدود ۴۸۰۰ نفر از کارکنان خود، پس از شش ماه پشتیبانی از عملیات‌های ایالات متحده در خاورمیانه، برای یک دوره استراحت وارد پوکتِ تایلند شد.</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/news_hut/73250" target="_blank">📅 01:20 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73249">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">صدای دو انفجار از سمت تنگه هرمز شنیده شد.
@News_Hut</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/news_hut/73249" target="_blank">📅 01:12 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73248">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cf7e4aede4.mp4?token=f32F5FWCx927HvFAxi3ddwBYqqEiuucGR6MtmPEmQdH7oR_GZaYRcBHWJYtGFeh33O1jGrAwgFWMiARY0R1l0IUHu2vlWcM7OGK3TmPrr6JLT_fHRHHekeutmUJ5XPesCszUDFyvxfSnrC7wwkIBDGh-wuwGZJHYqDZ_4VdzqIAqN4FCuXNOzyP1crh7_WNo9NMEDI4iaYEFV_v5LQjL8xncOkZFl_cUvUXXJPv7ZwAn1EYEqkut-uqHzLCn1gGNIlt_BQkk-MwnWC9ZZ5ddgoQR5RuNVaInYZUkTh3H1ziUI3gQTI9FgoxGpqZgRRRwWLB9Inhpb33iCNTScPWrww" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cf7e4aede4.mp4?token=f32F5FWCx927HvFAxi3ddwBYqqEiuucGR6MtmPEmQdH7oR_GZaYRcBHWJYtGFeh33O1jGrAwgFWMiARY0R1l0IUHu2vlWcM7OGK3TmPrr6JLT_fHRHHekeutmUJ5XPesCszUDFyvxfSnrC7wwkIBDGh-wuwGZJHYqDZ_4VdzqIAqN4FCuXNOzyP1crh7_WNo9NMEDI4iaYEFV_v5LQjL8xncOkZFl_cUvUXXJPv7ZwAn1EYEqkut-uqHzLCn1gGNIlt_BQkk-MwnWC9ZZ5ddgoQR5RuNVaInYZUkTh3H1ziUI3gQTI9FgoxGpqZgRRRwWLB9Inhpb33iCNTScPWrww" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">امروز خاتمی داشت با عصا به سختی راه میرفت که یهو ملت شروع میکنن به تشویق کردنش که یدفعه شفا پیدا میکنه و عصا رو میذاره کنار و راحت میشینه!!
@News_Hut</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/news_hut/73248" target="_blank">📅 01:10 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73247">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/de41df8bac.mp4?token=rkef_rjjL4PfiI8gJ9kNKTxSdczBY3jygij0X65EMENUN5UW4pSi75OY1JcW10FN-Aj4-m7kPsHThfVUUT9XeJAT-Pb6Pei6c58cgVvtbUM1XKKtMimpJ_UF1R_tlrgbdRoO09AMPrXeqlBIfkIsmAfeYPfc5rZ0Nbp2Z_3fJpqRnSm0kTO-rGCaaPou7iDMScNLMtsjr5eA_Cv9yRofhazgii-Y0L5S7aAsFcvrPafWBTFSk8oPa6XXwcJiah3EsUWZ12WYFG0UVfanYNSb2AbL0WsTpxVGLS7DKVzQLFNjX1x3UGLS_FlX-75OpBiqZSdj7AP4oxC_ahwMwIQIjg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/de41df8bac.mp4?token=rkef_rjjL4PfiI8gJ9kNKTxSdczBY3jygij0X65EMENUN5UW4pSi75OY1JcW10FN-Aj4-m7kPsHThfVUUT9XeJAT-Pb6Pei6c58cgVvtbUM1XKKtMimpJ_UF1R_tlrgbdRoO09AMPrXeqlBIfkIsmAfeYPfc5rZ0Nbp2Z_3fJpqRnSm0kTO-rGCaaPou7iDMScNLMtsjr5eA_Cv9yRofhazgii-Y0L5S7aAsFcvrPafWBTFSk8oPa6XXwcJiah3EsUWZ12WYFG0UVfanYNSb2AbL0WsTpxVGLS7DKVzQLFNjX1x3UGLS_FlX-75OpBiqZSdj7AP4oxC_ahwMwIQIjg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ابوالفضل ظهره‌وند، نماینده مجلس: پیش بینی میکنم ظرف یک هفته تا ده روز آینده جنگ از سر گرفته شود.
@News_Hut</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/news_hut/73247" target="_blank">📅 00:57 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73246">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PtulWSn1oEmtSV20S3cEzvHUXRmafL5iSoRBfPUR_r50PYO91kr7c_RLAjQNkonffDtGQdvE9TflzCsS-FzFBw3_9DIF6BIPP0s8XqabxbtbjODm0mNVCes0JCJmvq_Oh86OYkreGc1lGdMiE0cmaYknFMlnG8HailObbpgNJTT7cuMgaYiKum_o1tiZ7dZAZM6lwfl8Si3UsNjmp9fVTsfbsIInd2m-H0oGA-erRacgAmN26tzzwq3wLl5ohi6gUtfQpjgmpNwSsjlLmUE-9XCbbM9HMU5LqkwaSv56REPAXnMaHYHb0afDnwqDL0EFgNzoRtxwOpBQStSGU-Y4fA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#مهم
؛
اکسیوس به نقل از یک مقام آمریکایی:
به نظر می‌رسد «بی‌بی» (نتانیاهو) می‌خواهد دوباره دست به اقدام بزند. او چند بار در این باره با رئیس‌جمهور صحبت کرده و رئیس‌جمهور هم گفته است: «خب، می‌دانی بی‌بی، برو و آماده شو.»
اما در واقع هیچ تعهد قطعی‌ای وجود ندارد. عبارت «برو و آماده شو» ممکن است به معنای «الان»، «بعداً» یا حتی «هرگز» باشد.
@News_Hut</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/news_hut/73246" target="_blank">📅 00:32 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73245">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/15a3b1b7fc.mp4?token=JCFojyHkqgEvOWcs4In11coqCFGlyVPxftAMuaTn3EBSzQWYxqzVtygIUjWoIuaShZnxB5CpYO3ljYjmGg3eVSm44MgvXwlA-uX-UCjkW1IO12A5mQSrawQQHVaSaSh0pPkWzRvg6vUZgfegHPKaJwg6pO1B26kbUemKwA7zZmEnPM17AGZrxkVwOsFRmCWJSuNwCjBfVXF2MK0CDcTt-1W4uUpwJlFcGuBE9_zlZFrHECpDvg17dhkA2jOzECReNityJZ0JoCcPae54nOOZubbzHFAUEp_BMVEeee5-ExR9vjKIYUL6YZQFRa9uDmc7_ddq59if2c3JYiywesPcAw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/15a3b1b7fc.mp4?token=JCFojyHkqgEvOWcs4In11coqCFGlyVPxftAMuaTn3EBSzQWYxqzVtygIUjWoIuaShZnxB5CpYO3ljYjmGg3eVSm44MgvXwlA-uX-UCjkW1IO12A5mQSrawQQHVaSaSh0pPkWzRvg6vUZgfegHPKaJwg6pO1B26kbUemKwA7zZmEnPM17AGZrxkVwOsFRmCWJSuNwCjBfVXF2MK0CDcTt-1W4uUpwJlFcGuBE9_zlZFrHECpDvg17dhkA2jOzECReNityJZ0JoCcPae54nOOZubbzHFAUEp_BMVEeee5-ExR9vjKIYUL6YZQFRa9uDmc7_ddq59if2c3JYiywesPcAw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وضعیت دستشویی یه کافه تو بالاشهر تهران:
@News_Hut</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/news_hut/73245" target="_blank">📅 23:59 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73244">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">یک مقام آمریکایی به «اکسیوس» درباره ایران:
مذاکرات نه کاملاً مرده‌اند و نه واقعاً زنده؛
ما صرفاً در حال افزایش فشار هستیم و این باور وجود دارد که در نهایت، عقلانیت و تدبیر در آنجا پیروز خواهد شد.
ایرانی‌ها تصور می‌کردند که این رئیس‌جمهور به دلیل فشارها و انتخابات میان‌دوره‌ای عقب‌نشینی خواهد کرد؛ اما او به آن‌ها نشان داد که در اشتباه بوده‌اند.
@News_Hut</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/news_hut/73244" target="_blank">📅 23:16 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73243">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Bpp6_bblZT3X3ulsJFnpM--PTX_L56wNaBN0xJxolzAdb5bw_TTJg1yBLhChOGnBGNxSERK_zMm_g1qvr0DuezlUfRLErz131Vwwmmj_NW_YyrFrluqSzh3Q2W5CWXV23P8izIA7Ir8u5qOfqHFkUkFWRmeJu7jdfJoF4eZPaeyStdmUrb8hX6pESWzPNyMUxAFvGMrFltk8bYeWm3LPt3keMFw1fZa18PytMeUT84ce_AX9rUhDkkgTAhDjrI-kHqdbvGoJ5S3bOdp8IMnKptv_6aNGhiA5aS-vdD4u6Gf-HYB8X34C_T1K-jJYIGU-tmU5gO6fTZ077kEPhkIYog.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سازمان دریایی تجاری بریتانیا (UKMTO) گزارش داد که یک کشتی باری امروز در تنگه هرمز مورد اصابت یک پرتابه قرار گرفته است.
@News_Hut</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/news_hut/73243" target="_blank">📅 23:14 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73242">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c6d007bae0.mp4?token=C1krxtuYqSLuFBsydSGBGhEW9eG3Xjg2UU2_YyeV4aXRnwBgZFt18WsvwxLwuUWQXdPdEtLe_CjWaogcwWmTCGaw6WnfxxuoWVm2p-kuDIWTIiYTLWm4NRIdByf-bW9eDC1N-CjFQJi8lB3Nu3pWhtPLuNcGkym9wU4Vylm_W5neNYUsQFo6eSjmXpnwKf6Lpc_lwPjMSEAxyLJu-oswa9jQezktguzAOLeWxINtkDWpm_jnYeJ8UD3UCeJ5bKLlhmRIq0iW_mkMyMmGCqxM5eVjpiQLjjeVDTURoDdkGpPwx_yXfHvaJz1SL6B9mvzWXzTUMY4hJMx3ykW7RsUwZw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c6d007bae0.mp4?token=C1krxtuYqSLuFBsydSGBGhEW9eG3Xjg2UU2_YyeV4aXRnwBgZFt18WsvwxLwuUWQXdPdEtLe_CjWaogcwWmTCGaw6WnfxxuoWVm2p-kuDIWTIiYTLWm4NRIdByf-bW9eDC1N-CjFQJi8lB3Nu3pWhtPLuNcGkym9wU4Vylm_W5neNYUsQFo6eSjmXpnwKf6Lpc_lwPjMSEAxyLJu-oswa9jQezktguzAOLeWxINtkDWpm_jnYeJ8UD3UCeJ5bKLlhmRIq0iW_mkMyMmGCqxM5eVjpiQLjjeVDTURoDdkGpPwx_yXfHvaJz1SL6B9mvzWXzTUMY4hJMx3ykW7RsUwZw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خبرنگار رکنا از سخنگوی شهرداری تهران پرسید: چرا در تهران در تمام ساعات
روز ترافیک سنگین وجود دارد؟
محمدخانی در پاسخ: «اینطور نیست، مثلا ساعت ۳ نصفه‌شب که ترافیک نیست!»
@News_Hut</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/news_hut/73242" target="_blank">📅 23:01 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73241">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/26766391a1.mp4?token=sm3EuthmP5vpxk077YLSWrWwQ9nbsn_uvvMp3bi__ETBCLJ_kxgUpi8t6hPveb1Q-jsLwqGw1sK-lOaMLr94UCsGHyownBne2oPCPqYDPV5AWJUGFESrsBgAVFS9s7tEYnvc7RIx-Vi-Md5PpOUQ8ByJSHPiTs_FwGLfWbg9OLBBsqZKaNNq3qF9DKdDKqKVB-wE6UdQrYB31rNDnkemfa2U2s31anHgfBdPIoikYGAhfFQujwnrF6uf7T6mCZuHfo7sZTfhd3zunh4qHL92I7RIgKZX1oFU5Zn41yWo0_4rMzj-VPuvUi6fQl_phFxeoXA2iPMYsBh--QqTZ75Ag4WOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/26766391a1.mp4?token=sm3EuthmP5vpxk077YLSWrWwQ9nbsn_uvvMp3bi__ETBCLJ_kxgUpi8t6hPveb1Q-jsLwqGw1sK-lOaMLr94UCsGHyownBne2oPCPqYDPV5AWJUGFESrsBgAVFS9s7tEYnvc7RIx-Vi-Md5PpOUQ8ByJSHPiTs_FwGLfWbg9OLBBsqZKaNNq3qF9DKdDKqKVB-wE6UdQrYB31rNDnkemfa2U2s31anHgfBdPIoikYGAhfFQujwnrF6uf7T6mCZuHfo7sZTfhd3zunh4qHL92I7RIgKZX1oFU5Zn41yWo0_4rMzj-VPuvUi6fQl_phFxeoXA2iPMYsBh--QqTZ75Ag4WOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تجمع عرازشه در مقابل منزل حسن روحانی و شعار بر علیه او:
@News_Hut</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/news_hut/73241" target="_blank">📅 22:15 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73240">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6568459aaf.mp4?token=Irru8VTzP7r5KRe4qyDBT8tNRQj6Nh4TivzR4xssyINY33g9KpzSIYpH2f10ko4NoTfpfT4SQYNoblqHKEZ92SMML8Fu-ud8cYjhTRgq0BqBiAl-9x5BB3MTxSetO4GdRfVjc695LKvR3SLRkXdlBDXOjoZcoCTY45BbcwE5aCBXzD4x1Us77s2JW8z1-8q-jvxFgZLq51D8MfTnl6l5h74-itro58lvKN7l1dj5k8ybwnFSxCIQr_YReGoSyjHo6MuOiCUiLRBbUiwruVTVy-SYDnVkVNnfHCx_-vXYxO6G6S0Xl6z5isqy3iCb2nHKFxppMsbAusJHRjtn5MhXmw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6568459aaf.mp4?token=Irru8VTzP7r5KRe4qyDBT8tNRQj6Nh4TivzR4xssyINY33g9KpzSIYpH2f10ko4NoTfpfT4SQYNoblqHKEZ92SMML8Fu-ud8cYjhTRgq0BqBiAl-9x5BB3MTxSetO4GdRfVjc695LKvR3SLRkXdlBDXOjoZcoCTY45BbcwE5aCBXzD4x1Us77s2JW8z1-8q-jvxFgZLq51D8MfTnl6l5h74-itro58lvKN7l1dj5k8ybwnFSxCIQr_YReGoSyjHo6MuOiCUiLRBbUiwruVTVy-SYDnVkVNnfHCx_-vXYxO6G6S0Xl6z5isqy3iCb2nHKFxppMsbAusJHRjtn5MhXmw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وضعیت سرویس بهداشتی یه مدرسه پسرونه در تهران!!
@News_Hut</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/news_hut/73240" target="_blank">📅 21:34 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73239">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jpGMowpihdJ0Q9l1_Jmyw5jc0MYTy_MMw7u-hDrXRdWIfCSe0JySdU7goCwY3ei-Ezvzxt7uNPcf2qt3LsCC_wcttwjJ1XwUyN4Hhx5Xzuo82BmUbQB1gy-WhJD8BuXGbiKoTpjmUWWg5_4OQun6OL0scFpdtehF_dRThNoxWayOsY5omUCClFhd4wG-fr-N4Cut6NSGZk2fez7iH1_3pI9qk2r91VlJuoG7qs8frpZxftahawF8qXZo26VI4Ls-CGvGHCddMiFP-2IVGJ05lO1vzv888bFoGFabve3de5nPM8BitRPVx3_CYaM8ROhBiLXC1vZBx_MKiv287NAhpQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#فوری
؛به گزارش شبکه ۱۲ اسرائیل، بنیامین نتانیاهو، نخست‌وزیر اسرائیل، طی دو هفته گذشته گفتگوهای متعددی با دونالد ترامپ، رئیس‌جمهور آمریکا، درباره آغاز یک عملیات نظامی مشترک جدید علیه ایران داشته است؛ عملیاتی که احتمالاً پیش از انتخابات ۲۷ اکتبر اسرائیل و انتخابات میان‌دوره‌ای ۳ نوامبر آمریکا انجام خواهد شد.
نتانیاهو با ابراز نگرانی نسبت به تلاش‌های ایران برای ازسرگیری فعالیت‌ها در تمامی بخش‌های برنامه هسته‌ای خود، این تحولات را توجیه‌کننده‌ی انجام حملات مجدد علیه تأسیسات نظامی و هسته‌ای ایران دانست.
یک مقام آمریکایی اظهار داشت که ترامپ به نتانیاهو گفته است «اقدام کند و آماده شود»، اما تعهد قطعی نداده است؛ در همین حال، مقام دیگری گفت که موضع رئیس‌جمهور همچنان در حال تغییر است.
@News_Hut</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/news_hut/73239" target="_blank">📅 20:59 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73238">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">حوثی‌ها (انصارالله) اعلام کردند که عربستان سعودی طی ۲۴ ساعت گذشته ۱۰۴ حمله هوایی و موشکی علیه صنعا و استان‌های ذمار، تعز، عمران، لحج، الجوف، مأرب، صعده و الحدیده انجام داده که منجر به تلفات غیرنظامی شده است.
این حملات توسط جنگنده‌های اف-۱۵ و تایفون که از پایگاه‌های هوایی «خمیس مشیط» و «طائف» برخاسته بودند، و همچنین با شلیک موشک از «نجران» صورت گرفت؛ امری که مجموع حملات ادعایی ائتلاف به رهبری عربستان را به ۲۲۸۱ مورد می‌رساند.
@News_Hut</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/news_hut/73238" target="_blank">📅 20:15 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73237">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/r41DL7Gkkcxd8QbOG9ZEarLKdlFF_dMxJuHjvhjzqJPDEOrsLIdJsdp0fsExilcL2BGBR4c76Xc_K2zPoAGuM6wVlTgm8sgkPIn9YdOdr39rY3HOcEMVzu8_GjzOLWqOmSY3s50_OweTBSWpLdaao2vgj3td0HPfNrfHIemDaxSla2ZIE-r2c_VyLXrPABIpjR0ne_7uQ_1a3kCcJZGDKAOTODW5paPQqXe-ll6MHeAOOmhSZkpIQ8cdLbd5gAJDqyp9gIXWrPHy-D_D5k9X62Z_FcpdfW22AdCIECNMwtp2N1bM1TWH08TOyFpvL0uSVrvJLHnHz9Xow8haUlw9CQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#مهم
؛ترامپ در تروث سوشال:
«حوثی‌ها رفتار خیلی بدی دارن. فکر می‌کردم یه سال پیش، وقتی حسابی بمبارونشون کردیم و به درخواست خودشون حملات رو متوقف کردیم، درسشون رو گرفته باشن.
اونا مدت زیادی سکوت کرده بودن، اما حالا دوباره ظاهر شدن؛ احتمالاً به دستور ایران که یه کشور در حال فروپاشیه، نیروی دریایی نداره، نیروی هوایی نداره، بدترین اقتصاد دنیا رو داره و تورمش به ۳۰۱ درصد رسیده.
اونا به شکل خیلی بدی به عربستان سعودی حمله می‌کنن و عمداً سعی دارن قیمت نفت رو بالا ببرن؛ احتمالاً هم قبل از انتخابات آمریکا. این اصلاً قابل‌قبول نیست!
یکی باید بهشون توضیح بده که من دیگه نامزد انتخابات نیستم؛
من قبلاً با اختلافی بسیار زیاد پیروز شدم!
اما بعد از انتخابات دوباره وارد ماجرا می‌شم و این اتفاق رو هیچ‌وقت فراموش نمی‌کنم!»
@News_Hut</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/news_hut/73237" target="_blank">📅 19:41 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73236">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/eb0e101b64.mp4?token=LVSx-4EJ-TNw30motoQ1V-Bh6lNriIIL3Hdp2VS77wypjhdp8f1TtXQtHNIm_ZNQYWEp9XkeBmSNQ1sDs8t8WSPqXbcrsN35_gD8Q4JCwtQEHH3PyUvljSLHJGHHXo_cPU76hWlooZlK7C90_7aF-WxU0_X2tRO668VW9nAMky1-HC3K8ntjTvaen1_44hePst2lYMezRMc0TldhvdrjJTTqz0Gebh7YdMjBFT0ouJxNua0IBJXqruP_-uxG8NunNOugS3PVvbEHSIWbCPdszI4NTz76IvjYGeB95E2wqG3tGdoX-AWHFL53lOeEmlKIZs4IrARLHIc9hY_I2fpf5A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/eb0e101b64.mp4?token=LVSx-4EJ-TNw30motoQ1V-Bh6lNriIIL3Hdp2VS77wypjhdp8f1TtXQtHNIm_ZNQYWEp9XkeBmSNQ1sDs8t8WSPqXbcrsN35_gD8Q4JCwtQEHH3PyUvljSLHJGHHXo_cPU76hWlooZlK7C90_7aF-WxU0_X2tRO668VW9nAMky1-HC3K8ntjTvaen1_44hePst2lYMezRMc0TldhvdrjJTTqz0Gebh7YdMjBFT0ouJxNua0IBJXqruP_-uxG8NunNOugS3PVvbEHSIWbCPdszI4NTz76IvjYGeB95E2wqG3tGdoX-AWHFL53lOeEmlKIZs4IrARLHIc9hY_I2fpf5A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ خبرنگاری رو که همیشه درباره وضعیت ایران سؤال می‌پرسه، مسخره کرد:
ترامپ:
«ایران؟ باز هم ایران؟ همیشه ایران!»
«ایران یه کشور شکست‌خورده‌ست. هیچ اقتصادی نداره، تورمش ۳۰۰ درصده، پولی نداره و حقوق نیروهاش رو هم نمی‌ده؛ نه به نیروهاش، نه به هیچ‌کس دیگه‌ای پول نمی‌ده.
خیلی زود درباره ایران تصمیم می‌گیریم.
ما تنگه هرمز رو کنترل می‌کنیم و نفت زیادی هم از این تنگه خارج می‌شه.»
@News_Hut</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/news_hut/73236" target="_blank">📅 19:33 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73235">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2628e9cb18.mp4?token=cqrXHtJ2cdRDRuZknThVe7u0C8ClgI2qstuOrIpYLmPja0RGTajkSjWMzsPiKf1G6w33cKIVJWSOLf1fNEdlo001tSr1WXwGmv4jNjhAzoT29IzZ12nPWE0IFlL4gRPHKGCQlu0G-A1tFoRxBiZw0DqVBPz9iJwxafymY3-SRAHk2_dMUNmWXi4hMRGbN8y4pST3SVYA1z2Wyz1rgBgvKirMStyqCPmcTCiRgbH0poatk03Q_8xUTKAzRzOrXmNj52irrYVWLAMgk1kdQLoMhboghaU442vh4D980eAQjmpzzl0CxRvimDB6bhZ-F35rJXwsmHypQoFiEiXF1GQmbg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2628e9cb18.mp4?token=cqrXHtJ2cdRDRuZknThVe7u0C8ClgI2qstuOrIpYLmPja0RGTajkSjWMzsPiKf1G6w33cKIVJWSOLf1fNEdlo001tSr1WXwGmv4jNjhAzoT29IzZ12nPWE0IFlL4gRPHKGCQlu0G-A1tFoRxBiZw0DqVBPz9iJwxafymY3-SRAHk2_dMUNmWXi4hMRGbN8y4pST3SVYA1z2Wyz1rgBgvKirMStyqCPmcTCiRgbH0poatk03Q_8xUTKAzRzOrXmNj52irrYVWLAMgk1kdQLoMhboghaU442vh4D980eAQjmpzzl0CxRvimDB6bhZ-F35rJXwsmHypQoFiEiXF1GQmbg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سوال: آیا از ترکیه می‌خواید که در واکنش به اقدامات یمن ملحق بشه؟
ترامپ: «ممکنه این کار رو بکنم. اردوغان دوست خیلی خوب منه و احترام زیادی براش قائلم.»
@News_Hut</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/news_hut/73235" target="_blank">📅 19:30 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73234">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a7fdc0493f.mp4?token=cZBHtL_XisdyAC24A1dYKUh-TVtUbSR_ooOyCBeLVLclOaSxASx-hcaRVVUsn5IPPorMFij2E8xRKMAvhlkWN6KSpvlfO1gW0Dv4-TZ0lUJGcLNp7UDtMcnOMgIYsCJIq4Eh19fC14pY8uEXAy_9oqL83XFezx3uD24suUa_U1kVlLb3L34nJH7_uZqThg1exg57x9C0Pb_h0tCCJphmQzjYwX3_5-wDUchR5aN2m-pLypYT94HzPny8aL_gAos3iek5iyZZ3DbRvAI8ZM5Bh24Fy-uXsIhya4Ii-ityMwBPlVMmpybufYhIfLC1rAu0ksJ_K8b7uFjk31K1ZuQrcA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a7fdc0493f.mp4?token=cZBHtL_XisdyAC24A1dYKUh-TVtUbSR_ooOyCBeLVLclOaSxASx-hcaRVVUsn5IPPorMFij2E8xRKMAvhlkWN6KSpvlfO1gW0Dv4-TZ0lUJGcLNp7UDtMcnOMgIYsCJIq4Eh19fC14pY8uEXAy_9oqL83XFezx3uD24suUa_U1kVlLb3L34nJH7_uZqThg1exg57x9C0Pb_h0tCCJphmQzjYwX3_5-wDUchR5aN2m-pLypYT94HzPny8aL_gAos3iek5iyZZ3DbRvAI8ZM5Bh24Fy-uXsIhya4Ii-ityMwBPlVMmpybufYhIfLC1rAu0ksJ_K8b7uFjk31K1ZuQrcA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ در پاسخ به این سؤال که آیا حوثی‌ها رو هدف حمله قرار می‌ده:
ترامپ: «اونا خیلی بد رفتار می‌کنن. اگه بهتون بگم تصمیمم رو گرفتم، اون‌وقت... حوثی‌ها واقعاً خیلی بد رفتار کردن.»
@News_Hut</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/news_hut/73234" target="_blank">📅 19:25 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73233">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bae90f7f46.mp4?token=S11tJNaB6aRD_V5-P-LiPB8EHZDrhgc2df6SG9kDt-jDvZPwdFlC9GpV0cFx_ZYO0ZSL_jr7U3NnvJsQBrSK8ywpS7-h3wVao9ISGR_2npMKSs_bTcvPlwtNnIY72pxojnw1shbfMMYZzZCaUMPssJ6dmKyUIVavej51LEsYPTaK4JSjAoeyrZERHybh0oIyM-_7KG-kUx8-NBncTEvgBBw_vXCSR8F6tw54PblTTBmlGmeFnqx646eVuKcMGcKWnymRaxrUau14y6VCVygcXSSzIU-0mNZZzpzM9hYQG4T_f3fWi3fPJmag9_h7PDYcIe5Y9SKM_sC9b9w0YM7MyQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bae90f7f46.mp4?token=S11tJNaB6aRD_V5-P-LiPB8EHZDrhgc2df6SG9kDt-jDvZPwdFlC9GpV0cFx_ZYO0ZSL_jr7U3NnvJsQBrSK8ywpS7-h3wVao9ISGR_2npMKSs_bTcvPlwtNnIY72pxojnw1shbfMMYZzZCaUMPssJ6dmKyUIVavej51LEsYPTaK4JSjAoeyrZERHybh0oIyM-_7KG-kUx8-NBncTEvgBBw_vXCSR8F6tw54PblTTBmlGmeFnqx646eVuKcMGcKWnymRaxrUau14y6VCVygcXSSzIU-0mNZZzpzM9hYQG4T_f3fWi3fPJmag9_h7PDYcIe5Y9SKM_sC9b9w0YM7MyQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پیتر دوسی، خبرنگار فاکس‌نیوز: «اشتراک‌گذاری اطلاعات و داده‌های اطلاعاتی با اوکراین رو متوقف کردیم؟»
ترامپ: «نه، متوقف نکردیم. ما بهشون کمک می‌کنیم و واقعاً داریم کمک می‌کنیم که به یه نتیجه نهایی برسن. پیتر، ما می‌خوایم جنگ تموم بشه. داریم بهشون کمک می‌کنیم و اطلاعات هم در اختیارشون می‌ذاریم. می‌خوایم جنگ تموم بشه؛ برای همین با اوکراین و روسیه همکاری می‌کنیم تا به این جنگ پایان بدیم.»
این جنگ بی‌فایده‌ست و باید تموم بشه!
@News_Hut</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/news_hut/73233" target="_blank">📅 19:17 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73232">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/3fc7b7be7c.mp4?token=BfO1eKNSe-bJSN67q-xxrsx9gzkYEWtcTHrBjwjjy_qA6HL6aYIb90VxrIfRmTdFSY1DMJH22nvLn0Vyh4Aq2f6ULeIPkUj_o7IDZOzrtCoe7T4qO_WXSLc3VDY0U72TX25tyQgl4CY32iaCa6j40FHsmil8tvXHJRIqVJRd5xUg5Rdk7dGiV6LJBT2l2QAotAaOHrOfvIbHvFJz_XvpDziAjQlIlitd4sKvRveKaSpnZ0SdNTyJmpcJW9LN3Qo1KSF_LTEttzHHU1Gsnb6RB06b4uHtC6Vd-kyJ6Pp6D5Y6ASMRsTtykOUKuptOP0oK2MPwX97aHWVBWkC-WUlI7g" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/3fc7b7be7c.mp4?token=BfO1eKNSe-bJSN67q-xxrsx9gzkYEWtcTHrBjwjjy_qA6HL6aYIb90VxrIfRmTdFSY1DMJH22nvLn0Vyh4Aq2f6ULeIPkUj_o7IDZOzrtCoe7T4qO_WXSLc3VDY0U72TX25tyQgl4CY32iaCa6j40FHsmil8tvXHJRIqVJRd5xUg5Rdk7dGiV6LJBT2l2QAotAaOHrOfvIbHvFJz_XvpDziAjQlIlitd4sKvRveKaSpnZ0SdNTyJmpcJW9LN3Qo1KSF_LTEttzHHU1Gsnb6RB06b4uHtC6Vd-kyJ6Pp6D5Y6ASMRsTtykOUKuptOP0oK2MPwX97aHWVBWkC-WUlI7g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">در پی حملات هوایی نیروی هوایی سلطنتی عربستان سعودی، مخازن سوخت در بندر الحدیده یمن (تحت کنترل انصارالله) دچار آتش‌سوزی شده‌اند.
@News_Hut</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/news_hut/73232" target="_blank">📅 18:56 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73230">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/3237ca4f82.mp4?token=Xwlxn9L2LdyZ0cb8bXWxLvOzM0-1yP6-7846qr-r0wVro812b8JLGOH6RoueHNX_jpD-a85B0jXcATiWgwfxnB0X1EhXCxCXb7wn0lrcmQw3UepODhQy0VEXyeooxhqOYiRbOHks89mCt_WCUpBaA_OAOCtQzUWD3A7STpDrZQqNJRFdWtIGs464vxv9DroiN72IwBkdNB2GHRnfBXGSTEhuN789kKOuT7OJuwIeHfB0NIzvXz9EgJK0UBSfZwBDU7LyrYrURlvKd5td4tjctMyZSxaMHngi9E2gm0uPzd-abyRBeOXH8rP3ovksfbVU-khKkS-cw9wdq3n3ZpUlvLKkDfut0gBfdjaMp4olQoe3daAWrZ6jnv93Gpt5599zbXpdQNNOHWqaKRRCC3rZaLpP499iCHxp-LrwVv-SrJZblIIjNIXIRDeAYhkhY1l_t63PT853m-ta4NuEGenaOqTTHhV86lbhv4P8__VZvtyItkjIUuFJ0kSNplZ4z36S2upVs4TC14_Ckee0cq2SWiA72N0mO2Zxs1BHRYRaPkTDQW6KgoJeKCCQnIsvXVe8pub0pY5Tu2ErrFxHDKYcz6tFRoJsUVgPSS2IePD89CRn1ZpueguJ3e07rL7k7NRSSL2TbnCODgnSktPRMgr3Z6EKIpnm-rkras5e1FOYC3Q" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/3237ca4f82.mp4?token=Xwlxn9L2LdyZ0cb8bXWxLvOzM0-1yP6-7846qr-r0wVro812b8JLGOH6RoueHNX_jpD-a85B0jXcATiWgwfxnB0X1EhXCxCXb7wn0lrcmQw3UepODhQy0VEXyeooxhqOYiRbOHks89mCt_WCUpBaA_OAOCtQzUWD3A7STpDrZQqNJRFdWtIGs464vxv9DroiN72IwBkdNB2GHRnfBXGSTEhuN789kKOuT7OJuwIeHfB0NIzvXz9EgJK0UBSfZwBDU7LyrYrURlvKd5td4tjctMyZSxaMHngi9E2gm0uPzd-abyRBeOXH8rP3ovksfbVU-khKkS-cw9wdq3n3ZpUlvLKkDfut0gBfdjaMp4olQoe3daAWrZ6jnv93Gpt5599zbXpdQNNOHWqaKRRCC3rZaLpP499iCHxp-LrwVv-SrJZblIIjNIXIRDeAYhkhY1l_t63PT853m-ta4NuEGenaOqTTHhV86lbhv4P8__VZvtyItkjIUuFJ0kSNplZ4z36S2upVs4TC14_Ckee0cq2SWiA72N0mO2Zxs1BHRYRaPkTDQW6KgoJeKCCQnIsvXVe8pub0pY5Tu2ErrFxHDKYcz6tFRoJsUVgPSS2IePD89CRn1ZpueguJ3e07rL7k7NRSSL2TbnCODgnSktPRMgr3Z6EKIpnm-rkras5e1FOYC3Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نیروی دریایی ارتش جمهوری اسلامی تصاویری از یه نفتکش در حال سوختن تو شرق تنگه هرمز منتشر کرد و از اعزام نیروهای جدید به دریای عرب، دریای عمان و شرق تنگه هرمز برای رصد رفت‌وآمد کشتی‌ها خبر داد.
@News_Hut</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/news_hut/73230" target="_blank">📅 18:16 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73229">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7853c789a5.mp4?token=pU677n9yr7utr4OhhDCke6cbZ3FtAzqD-2YwbQy3A6ghtti32qs0oEI0U10Y1f6QrQOkkRY9uYCtqz_mO9jTtp4Z91GxTsfDE75R_ZdNCVBVHoDXQgnj02KO0vgDFapXKq62ZIZY6MWTJkXR7nHoZCoH-ip_Yc1mWggpI2md2LlALHL6gfNWzQ2wKYctIvlzyoG_1oZMiesH96PHYKvNADnT3GZVyPMGheIF98Efg1qggkmp2Ja3hy3SW2xRTFtKHPxKrnEG63PzaIfAg1JVQgtwyo169a5dOtqRN26CnTDx8pdNGS6plA3RLX7-jGd2TclqVvBvPvf_qoWxey_rSw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7853c789a5.mp4?token=pU677n9yr7utr4OhhDCke6cbZ3FtAzqD-2YwbQy3A6ghtti32qs0oEI0U10Y1f6QrQOkkRY9uYCtqz_mO9jTtp4Z91GxTsfDE75R_ZdNCVBVHoDXQgnj02KO0vgDFapXKq62ZIZY6MWTJkXR7nHoZCoH-ip_Yc1mWggpI2md2LlALHL6gfNWzQ2wKYctIvlzyoG_1oZMiesH96PHYKvNADnT3GZVyPMGheIF98Efg1qggkmp2Ja3hy3SW2xRTFtKHPxKrnEG63PzaIfAg1JVQgtwyo169a5dOtqRN26CnTDx8pdNGS6plA3RLX7-jGd2TclqVvBvPvf_qoWxey_rSw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">۸۰ تن میوه به علت بسته بودن تنگه هرمز رو دریا خراب شده و داره دور ریخته میشه:
@News_Hut</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/news_hut/73229" target="_blank">📅 18:11 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73228">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/news_hut/73228" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBe
t
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/news_hut/73228" target="_blank">📅 18:11 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73227">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Gu7nB1ovULZ_YeZ1KOu15YnvH2I4LIFi6zf_C-ntVB0dk5h1evVKnpsHIvSzVMYUmXIyQq8Q-RsSHU5VpiYEfBUm2PsJZ9TPqbnTT_YtV1LaUD-svYWjykGYdWGPq8iiKbFP_EW2PAbpBbYuI7wQhcACHkyPzNvqMWl2XNfHIRMYo0GuuLJRY-ZfiJSM3md8vg9BKf-Ur8HQv-nt3ocIfyJNJnXzzypGQjJy6WqXNLP3_SVq3coqHMDN_59NPCUf-TyvwFWLpU__6113fFPbg1UkShjvNtJnz0gsaRvtbLb70HCMSu0fXVYfB5GifFjTPGdbYP0acYr5Sv_hqqHEaA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">منچستر یونایتد
🆚
اتلتیکو مادرید
🦖
این نبرد حساس چمپیونزلیگ را در سایت بین‌المللی
TrexBet
پیش‌بینی کنید!
📉
نگاهی به آمار ۲ تیم
در ۵ رویارویی اخیر :
منچستر یونایتد : ۱ برد، ۲ تساوی، ۲ شکست و ۷ گل زده
اتلتیکو مادرید : ۴ برد، ۱ شکست و ۱۲ گل زده
🦖
🦖
🦖
🦖
🦖
بونوس اولین واریز تا سقف ۱۰۰ یورو
🦖
بهترین ضرایب بین تمام سایت‌ها
🦖
واریز آسان و امن از طریق کارت به کارت
TREXBET — PLAY. PREDICT. WIN.
https://TrexBet.com
T.me/TrexBet_Ir</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/news_hut/73227" target="_blank">📅 18:11 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73226">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">حملات هوایی نیروی هوایی سلطنتی عربستان سعودی به صنعا، پایتخت یمن تحت کنترل انصارالله.
@News_Hut</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/news_hut/73226" target="_blank">📅 17:49 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73225">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f155f86ad3.mp4?token=RNJ-BtwAABD-CYTkGnh4hK6uYYRZH8-aQO0tV3m6TpGTSH5vI0ZDoDx6bGA7_Uoo0WyjkM-XwAxze3y3URE6PeNQQTEIvdXuqDgqPfFv8NB8vCZX_sde1BWXpOSPxs3G9cnDUeJeFGPd4SnCXhYbmSw2h04x0og_M5np55G9AVCQDJfNU05xSXZNIqjeWGiiC6HyNGoY-bvSM31tO1LGcn-WGHSbs4JVX7F-NkoeZEGuN4tIgqq6SlCJ-D5ZjDQgRAT3C51fDzInWMvivHXSpglf47H49xRn9tx-uO120CRISjJaW_mTktiKPsLnfBBHa9r3c8wF9KIGgvLIlYWBmA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f155f86ad3.mp4?token=RNJ-BtwAABD-CYTkGnh4hK6uYYRZH8-aQO0tV3m6TpGTSH5vI0ZDoDx6bGA7_Uoo0WyjkM-XwAxze3y3URE6PeNQQTEIvdXuqDgqPfFv8NB8vCZX_sde1BWXpOSPxs3G9cnDUeJeFGPd4SnCXhYbmSw2h04x0og_M5np55G9AVCQDJfNU05xSXZNIqjeWGiiC6HyNGoY-bvSM31tO1LGcn-WGHSbs4JVX7F-NkoeZEGuN4tIgqq6SlCJ-D5ZjDQgRAT3C51fDzInWMvivHXSpglf47H49xRn9tx-uO120CRISjJaW_mTktiKPsLnfBBHa9r3c8wF9KIGgvLIlYWBmA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شهردار کرج:
همه شهروندان ایران کرجی‌ان، فقط خودشون خبر ندارن؛ چون بالاخره هر کسی یه فامیل کرجی داره.
آغوش کرج به روی همه بازه، ما هم آماده‌ایم از همه مهمون‌نوازی کنیم.
از پارک‌های زیبا و اماکن دیدنی تا رستوران‌های خوب، همه‌چی مهیاست؛ فقط مونده بیاین کرج.
@News_Hut</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/news_hut/73225" target="_blank">📅 17:31 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73224">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">#فوری؛ائتلاف به رهبری عربستان سعودی دستور تخلیه ایستگاه مرکزی «الصباحه» متعلق به شرکت نفت یمن در صنعا را صادر کرده است؛ تأسیساتی که تحت کنترل حوثی‌ها (انصارالله) قرار دارد.  @News_Hut</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/news_hut/73224" target="_blank">📅 16:49 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73223">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">حوثی‌های یمن بار دیگر به همه کارکنان تأسیسات نفتی و فرودگاه‌های عربستان سعودی هشدار دادند که محل را ترک کنند و این نشان می‌دهد که حملات بیشتری در پیش است.
حوثی‌ها به همه «کارشناسان، مهندسان و کارگران در تمام تأسیسات نفتی عربستان سعودی» هشدار دادند که مناطقی را که نشان دهنده اهداف هستند، «چه قبلاً مورد حمله قرار گرفته باشند و چه نه»، ترک کنند تا از به خطر انداختن جان خود جلوگیری کنند.
آنها همچنین هشدارها را به خطوط هوایی، فرودگاه‌ها، مسافران و کارکنانی که قبلاً به عنوان مناطق هدف تعیین شده بودند، مجدداً تمدید کردند.
@News_Hut</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/news_hut/73223" target="_blank">📅 16:46 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73222">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/O3psDVLN_eajUzfjo9q6dbgaXA30lRxE5ROCgTWHwHTLvhlAW3MTYXk838TLcAvc6lzLzmwnlJ9_kmb0-Nx0IrPnH88XqUh20qmdNmeh5mVngOWKiGRXW8G5ofq3n9f4-IHnRL0Pl6hGPKy4OcSAmJAGxCh8ZdkyMg5cSybWb9DV26gIA6iLJ_0E3HE9piQwH1pUZTlroIz7Ki6RuFILZ_2nDNSNaPUsSECxhSZrFIoCEazqydruWyr9SIjZ3CNbb7nHe3KQ63Gw4rE3cgLw_nS9QB5v-3qJFmE9bX3HIow6MyuX_fh2MlNOKvIWqtMb0Y5ddV1yPDNnmekHifu-TA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#فوری
؛ائتلاف به رهبری عربستان سعودی دستور تخلیه ایستگاه مرکزی «الصباحه» متعلق به شرکت نفت یمن در صنعا را صادر کرده است؛ تأسیساتی که تحت کنترل حوثی‌ها (انصارالله) قرار دارد.
@News_Hut</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/news_hut/73222" target="_blank">📅 16:42 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73221">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">😶
🚨
🚨
این کانال باعث ورشکستگی خیلی از سایتای بت شده و پلیس FBI برای دستگیری ادمینای این چنل جایزه تعیین کرده
🔥
https://t.me/+bDapVmvigDhmYzZk https://t.me/+bDapVmvigDhmYzZk</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/news_hut/73221" target="_blank">📅 16:42 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73220">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/v2p0YJ1GrAqXx5TXtJy_pxvHRQBZ3ATtfXDNanMwHf5mi5dc9zbVKEdD1G0NL-xIBk0mUr2JqCx9HS68UzkIi7W7LifY2H1Dw_lC0SdbQ_EhOA7iCUsVXYVK1Pq3u9-jgykD0-UuV3NCVSGgB3Dd7jZNzuRuRlXF3Ua__5SK94tIrxFNOMCmHpxX5957cfGMFsHwfOkAbEUv6SOH1xE9cUbscg2TWe2WaNhitWlHo5AISF98VXmJMp_02CPJVIImY5uF2sXYyZUzA51x-O3vYUbGSIcrGAIEmVwhLdR6oFagHv6OxvP5yI33l0x_EEC8BOaHHSkWyd_wWz2x7tHM4A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">😶
🚨
🚨
این کانال باعث ورشکستگی خیلی از سایتای بت شده و پلیس FBI برای دستگیری ادمینای این چنل جایزه تعیین کرده
🔥
https://t.me/+bDapVmvigDhmYzZk
https://t.me/+bDapVmvigDhmYzZk</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/news_hut/73220" target="_blank">📅 16:42 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73219">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/lAqO7Geq8x21jP9JNIcTPGMe1K6S3a1T-6GcVTN1mHZ6MOH5_cIei5Kmx5fJ2pXupjQTsqPB5cKQ8HuPuh-q_H7WfXcA9R5FBUJIblRyseOjpXoRPWOcpBQsfdbBgXkKGE30d7_SoUhjuSgGhtJrggJ5t7cVl9BW7HYQXrPc8IwF6uNvyslVoa1cmDhK_8jEMpWx2dWmsDrvVAM9LTVWk0RhmWlwcSdXAEIkTvfGSUkiwnCAVbWJ4kr6Ju_tMlPMkBbnKSPDXR7LmQyAYpeTYpVm3FL5xGSikAT7Oatf9NesKERsvVtM1uDZO8w18qrR0g-dwCx18tts5BOGn1xRMw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">طبق گزارش وال‌استریت ژورنال به نقل از منابع مطلع، ایران به کشورهای منطقه هشدار داده که در صورت آغاز دوباره جنگ، ممکنه نیروهای مسلحش حمله زمینی به کشورهای همسایه انجام بدن.
ایران همچنین به مقام‌های عرب هشدار داده که ممکنه تأسیسات نفتی عربستان رو هدف قرار بده؛ در کنار حملات ادامه‌دار انصارالله به تأسیسات نفتی سعودی.
به گفته این منابع، ایران قصد داره در صورت شروع دوباره جنگ، حملاتش به نیروهای آمریکایی رو هم افزایش بده؛ از جمله تلاش برای غرق کردن ناوهای آمریکا در غرب آسیا و کشتن ملوانان حاضر در اون‌ها.
@News_Hut</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/news_hut/73219" target="_blank">📅 16:25 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73218">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f037a6e61d.mp4?token=hvjST3ajZIHRn9zh5sjShne3FTjQDGsHi28Imyp4pD3v46McCobjoLjTGyP7oetDPG16VIWmmr427OAG4ocmCtr8EpfT1LK2Lbi7sfC9v727bhQSgdBmHohYzAK7bUJ9jn23Tl0ifmfyLBudMN58CQWEaFlTrrHwc8F0KWyoaRgeKpBau_nMyZyKtYEkOAVjVI7by-Xtbf-6obea-304n2EJV2FT4kULKthHzoB4GP6vLsWrE9n0KbwQNo9cN2H2rtvDvH5l4U49UYY5K1I1-U0gvuedjeH_LTK6vMC9Yo03uboq7PsKQiO_ARs9pU0sD7Ha5dPlGWRQ6puFBxvazg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f037a6e61d.mp4?token=hvjST3ajZIHRn9zh5sjShne3FTjQDGsHi28Imyp4pD3v46McCobjoLjTGyP7oetDPG16VIWmmr427OAG4ocmCtr8EpfT1LK2Lbi7sfC9v727bhQSgdBmHohYzAK7bUJ9jn23Tl0ifmfyLBudMN58CQWEaFlTrrHwc8F0KWyoaRgeKpBau_nMyZyKtYEkOAVjVI7by-Xtbf-6obea-304n2EJV2FT4kULKthHzoB4GP6vLsWrE9n0KbwQNo9cN2H2rtvDvH5l4U49UYY5K1I1-U0gvuedjeH_LTK6vMC9Yo03uboq7PsKQiO_ARs9pU0sD7Ha5dPlGWRQ6puFBxvazg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">درگیری‌ها در ارتفاعات چاه‌احمد تفتان، با گذشت بیش از ۷ ساعت، همچنان ادامه دارد.
به گزارش حال‌وش، در حمله افراد مسلح به ستون موتورسواران لشکر فاطمیون، بیش از ۲۰ نفر کشته یا زخمی شده‌اند.
پس از این حمله، بیش از ۴۰ خودروی نظامی و پهپادهای شناسایی و رزمی به منطقه اعزام شده‌اند و نیروهای نظامی همچنان با خمپاره و پهپاد ارتفاعات را هدف قرار می‌دهند.
این در حالی است که رسانه‌های حکومتی پیش‌تر از پایان درگیری و کشته شدن تنها سه فرد مسلح خبر داده بودند.
@News_Hut</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/news_hut/73218" target="_blank">📅 15:54 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73217">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">ائتلاف به رهبری عربستان سعودی:
به‌زودی به غیرنظامیان هشدار خواهیم داد تا مکانی را در صنعا تخلیه کنند؛ این اقدام به منظور انجام یک عملیات ویژه صورت می‌گیرد.
@News_Hut</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/news_hut/73217" target="_blank">📅 15:44 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73214">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/lqlfdh7Suzj0b8ejIDXmQU6fbPVM3UrQ2FTFF2844fL_CCba1F6Lrkjs0TavpRxbRrz7blUCyJncwMbC0xQUqo6UVK9YRxqepoTUPeMOgukffCt9eTxJ_Cw8_aN5R5xnAAUiNyX2UC04v9rQ5LoerMVhU1fGiCNoIY99g0bnoS2eImT5RFj74fpaJyuco3-2IL7T41Tj0uKE_B8WmE7DxqKabPyQrPp4BCzbEYBWhg_edknhwRGaFgMEyfMs6aztgeqbozIBUa1963b4jPKP7qnOz84kVHQzrN5UPvllIMU5KKrWPpptysiQsoNXhmYMuJRQcao8YiTgOm_wqq1ccg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ZsodTvzgUNX8KuPca-BwhpBZOODxSsWZ03JLeh0wv38iQGJl_VJwpx5mp4YYpUkgoJVkiZS4_yAZzYY3J5DwFjT3udxvS1vEB7eea1m4BiTXHKt0oKrWEASo-55dcnoaRCbzLFKF3b45E3vtF9-WpNAXLeBMDKBeUaneICh8dnn1N3i-ll-37uxXzZr1BzcQGaI7Ew9f7S0p5YlcXO5p6w8q3HvU3o-VzQuynHhHaU1v5w_6cqw87bU-K8s1aMVTF2YUXCysTW6gwPdqhVLz0VVck_IdBbRbJTcjsxkgEySHJl3D9tUp8oUHuEK269eK3_WYZHDoaanW0Jd4aaKFzA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Og4nYXdE_GqC1DCr-K7XxwsyBaF7mDYE0Dn7nKpDqaoQyjNqBa4MTtn9f2eqFIX18YJ5tihRCeuoKAjBQK_zs9Gpq_eBqkGQ7zZ8YoSr_LhEzy3ujs5IQC82NA2QdfUOE_t7xOnLlAe8IfEOFGYnrr0LEMBDzEBz8P456XBn1QdDpmghCYOzT79nJresT8w_ruv9wNT84lebf0z76d5d97zeWGgTmN8khOXTG3PgSfw3k321wewXID78A5A1dk-suoyf-ubgZwyN3Giw0NEDqez1TSlo50dlpq5ohwbU6szSxpc-c1krlcO6t52QLx-hNnF-WPfUTToV4JQScLQuDw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">حدیث ستاری، مدل ۲۵ ساله ایرانی و دانشجوی دندان‌پزشکی در امارات، در مسابقات بین‌المللی زیبایی «میس گلوبال ۲۰۲۶» موفق شد دو عنوان «ملکه زیبایی خاورمیانه» و «برگزیده مردم» رو به دست بیاره.
+لباس ملی حدیث در این مسابقات با الهام از سیمرغ، پرنده افسانه‌ای ادبیات فارسی، و نمادهایی از حکومت‌های ایران باستان طراحی شده بود.
@News_Hut</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/news_hut/73214" target="_blank">📅 15:27 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73213">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/90850a02ad.mp4?token=sfgddQNVkr60F58OUPcFAbzOdfQcl0M7TIJ84AgSXzskj45m1Ykdrd3duP79XR2MaZZdC64074qnaa4cYcrfMdtTURnDmBI1vD4u9XFNQHUQ9GdXDGqdy1f9MoOOCJf8OCsfRE3UbV7DgFElK3Rrl4-EAmJNQCs7b_iKhS4gwvsBIaWaBYRDTIcio3WBoIaGgtyJmf1AhGpfuigaRsvLYykNxK8pyoe9vl-yBNHTuYcxD6j8AJiEaGGBkrbXBAR_2efhRkJFt-HajUMGBV8wvtxNHMGl_R1-Jck7fzYOOO7zP8xKmvj1ZgAmasz9qKCIpveCAUkFKgpNjFVvD20MeA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/90850a02ad.mp4?token=sfgddQNVkr60F58OUPcFAbzOdfQcl0M7TIJ84AgSXzskj45m1Ykdrd3duP79XR2MaZZdC64074qnaa4cYcrfMdtTURnDmBI1vD4u9XFNQHUQ9GdXDGqdy1f9MoOOCJf8OCsfRE3UbV7DgFElK3Rrl4-EAmJNQCs7b_iKhS4gwvsBIaWaBYRDTIcio3WBoIaGgtyJmf1AhGpfuigaRsvLYykNxK8pyoe9vl-yBNHTuYcxD6j8AJiEaGGBkrbXBAR_2efhRkJFt-HajUMGBV8wvtxNHMGl_R1-Jck7fzYOOO7zP8xKmvj1ZgAmasz9qKCIpveCAUkFKgpNjFVvD20MeA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">عرازشه شب گذشته،  در میدان انقلاب تهران علیه مسی شعار دادند  !!!!!  @News_Hut</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/news_hut/73213" target="_blank">📅 14:57 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73212">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/b1RGvGZuX8RysurtCcY3ThE9ZadOOhl7TO1ffDzLdGG_QPGNSAbm6qBrrlnyY7K-wo4rVOPAntO56Pj5YBJ9wqfjgJtU37kqZNch9d-mHNC093GCfGqGFhSw_eeI4O_lam5zc5KF6FLzkUNuMXXeEPk11kNHp3eX_6PnCpzZZGuhrUL-NlRhFL03TWaJgWQw3k0r50uHsH50kTLkkKNQyZvzXrJbHg3Rzf0raNaj5BTk4mr4v50SwFY1yoeLW0p3Xcl_C9136F1VsgLSt42wXO0WA74Ve5pKj3HxqfOe7ZU77C2dehc6lkf1ptwoWxjELF4zaBrNW_L1BPBOFjAktw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">به گزارش روزنامه «هاآرتص»، بنیامین نتانیاهو، نخست‌وزیر اسرائیل، از طریق میانجی‌گری ایالات متحده به دنبال جلب موافقت عربستان سعودی برای مشارکت اسرائیل در عملیات نظامی علیه حوثی‌های یمن (انصارالله) است.
نتانیاهو این پیشنهاد را فرصتی برای تقویت روابط با ریاض و پیشبرد توافق احتمالی عادی‌سازی روابط می‌داند.
با این حال، محمد بن سلمان، ولیعهد عربستان، به دلیل نگرانی از واکنش منفی افکار عمومی در داخل پادشاهی، با مشارکت اسرائیل مخالفت کرده است.
@News_Hut</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/news_hut/73212" target="_blank">📅 14:31 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73211">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/876aa9210f.mp4?token=e-pyZUfsmD1eAP9aPbq_nf4WAX3q80q1pAm6LJ25nT2X6fynOSYPJtkTKPEp2Qwdkx1DzYmviyEWEDgbgBCTCop2ulce__RPtpTa0DivdHlvXrUVs02bzDGaPtJO_TQpv47LwIofI-N9m1H3EdgTBNrs8Mq_lvXTZ1duYaLHB5Son7FQcM6DcGQydEeC8DvROPb9ZEerpsi1MtshbyXv-yevMG1FjKvXvdBSG4_1u9nlCH20C1uCX4nOZUny2KcpqPEwW9u48Hs87NND10z0GlhxpMV_wWSQYerwYlc-RHrKpFZ0PMLDNDhoM5AucwlotgH7L2C_rxMbqDt9WXboig" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/876aa9210f.mp4?token=e-pyZUfsmD1eAP9aPbq_nf4WAX3q80q1pAm6LJ25nT2X6fynOSYPJtkTKPEp2Qwdkx1DzYmviyEWEDgbgBCTCop2ulce__RPtpTa0DivdHlvXrUVs02bzDGaPtJO_TQpv47LwIofI-N9m1H3EdgTBNrs8Mq_lvXTZ1duYaLHB5Son7FQcM6DcGQydEeC8DvROPb9ZEerpsi1MtshbyXv-yevMG1FjKvXvdBSG4_1u9nlCH20C1uCX4nOZUny2KcpqPEwW9u48Hs87NND10z0GlhxpMV_wWSQYerwYlc-RHrKpFZ0PMLDNDhoM5AucwlotgH7L2C_rxMbqDt9WXboig" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مدیرعامل شرکت آب و فاضلاب استان تهران: قیمت آبی که به مشترکین ارائه می‌شود ۱۱ هزار تومان است درصورتی که قیمت تمام شده آن ۸۸ هزار تومان است؛ فاصله وحشتناک است.
@News_Hut</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/news_hut/73211" target="_blank">📅 14:26 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73210">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c54425bdea.mp4?token=W5o0pEJ3QiiQYSZWYIhZ4_GnMfMG45Vj2KyT_yBLh2HoypWzR9Y5iBM5H7Y7rESAR-ybOsFIWpTYXDhtnoyUKSUGw3hGWUQyS_NNc7JtAkzKpm1Rar4IF4BJJTT2GLzu7Gr1Ypaz7bnnFepOWB4zuOGkRi9aFLRsLWpJyXQmOgZu3IoDhOJd56egvmMx_WW_jlfmVhPncdDYcI6-5vR4kReToDdmEy2t3cTXXaEL38Y3c4Bbzj3IUZCqTEQNp_TZiK_uyMuIO0F55fo8mw-EO-xq2C_gCNlnvc8cnnjXRqCK9IozSYwQ4YzdCgKCldt9hLE-MnqskZc6JplLFSdK6Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c54425bdea.mp4?token=W5o0pEJ3QiiQYSZWYIhZ4_GnMfMG45Vj2KyT_yBLh2HoypWzR9Y5iBM5H7Y7rESAR-ybOsFIWpTYXDhtnoyUKSUGw3hGWUQyS_NNc7JtAkzKpm1Rar4IF4BJJTT2GLzu7Gr1Ypaz7bnnFepOWB4zuOGkRi9aFLRsLWpJyXQmOgZu3IoDhOJd56egvmMx_WW_jlfmVhPncdDYcI6-5vR4kReToDdmEy2t3cTXXaEL38Y3c4Bbzj3IUZCqTEQNp_TZiK_uyMuIO0F55fo8mw-EO-xq2C_gCNlnvc8cnnjXRqCK9IozSYwQ4YzdCgKCldt9hLE-MnqskZc6JplLFSdK6Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نخست‌وزیر نتانیاهو :
کشورها، حتی آنهایی که به ما حمله می‌کنند، به آرامی و پنهانی می‌گویند که رژیم جمهوری اسلامی باید سرنگون شوند، آنها ما را خفه می‌کنند.
ما مطمئن خواهیم شد که آنها(رژیم جمهوری اسلامی) سرنگون شوند. آنها سرنگون خواهند شد.
@News_Hut</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/news_hut/73210" target="_blank">📅 13:46 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73209">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/de6a75e3c2.mp4?token=YbbsAN-lzE9LxhXHdPT5tn5qGuNZ0a1WqFrEjCTlSnTbAhY8s5t4vUZ6rQdufyXRohMKR3ssWAMqMxVNtpskeDvWXEkonglTRTgYJFhC4bkqa6ojaIOZn6cPXY_DYhhgugzJ0vLbaeGHCnfq3hJLzNsuS3AMjSzwpqzXu2wDxncXDOL6QXGcYVopwsMsB8CHSnY176Xa4Cmwv_bDKHSfIGuqeF5m2d5_-vMymn9NDpbPnCuRJ2C-jJQNtkiwDUQtkEiqIvArjzeP6fGwECV4uFa3ha51xC5Sc8dTuuijySnIjTLdKzj8Zi36sNZnUyNixNCPAtIJQsSmAv7cd0e1rQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/de6a75e3c2.mp4?token=YbbsAN-lzE9LxhXHdPT5tn5qGuNZ0a1WqFrEjCTlSnTbAhY8s5t4vUZ6rQdufyXRohMKR3ssWAMqMxVNtpskeDvWXEkonglTRTgYJFhC4bkqa6ojaIOZn6cPXY_DYhhgugzJ0vLbaeGHCnfq3hJLzNsuS3AMjSzwpqzXu2wDxncXDOL6QXGcYVopwsMsB8CHSnY176Xa4Cmwv_bDKHSfIGuqeF5m2d5_-vMymn9NDpbPnCuRJ2C-jJQNtkiwDUQtkEiqIvArjzeP6fGwECV4uFa3ha51xC5Sc8dTuuijySnIjTLdKzj8Zi36sNZnUyNixNCPAtIJQsSmAv7cd0e1rQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جالبه بدونید این ویدیو که خیلی وایرال شده یه بداهه از خواننده و طرفدارشه و بیت شعرش از قبل مشخص نبوده:
@News_Hut</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/news_hut/73209" target="_blank">📅 13:11 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73208">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a96bc792f3.mp4?token=raAKonIjIGSYiFAAHeYLORYUtgt-PY6ggZ5jHjugKmgOCwSRsj5XJxpr8A7IQpgxwyZHezPFDC42szG_R_PSEMRzAg_fcMoNd_0MGP_LNObGWqwtY0VGIIMqPhn7RrBC9cbnxQgwdeoVQ8xD82RXt2EDZ00oDgpSUBpvhsc3Mv5zgwJeZuiPx9R3OnyNFYBrn3DFmQYubGsk1sNg802iMDHWzXR_77VdGQD10_ZILHRaZzf8wpGevJs91dWb-yt3Na51KTEBcU4skiRZPZ3EEWyBOioYXhRkYJwMZtzMfHmVaKNXiqgSLILRCC0YJgsJ-mb1lqlkPm4XK-SiojtKYA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a96bc792f3.mp4?token=raAKonIjIGSYiFAAHeYLORYUtgt-PY6ggZ5jHjugKmgOCwSRsj5XJxpr8A7IQpgxwyZHezPFDC42szG_R_PSEMRzAg_fcMoNd_0MGP_LNObGWqwtY0VGIIMqPhn7RrBC9cbnxQgwdeoVQ8xD82RXt2EDZ00oDgpSUBpvhsc3Mv5zgwJeZuiPx9R3OnyNFYBrn3DFmQYubGsk1sNg802iMDHWzXR_77VdGQD10_ZILHRaZzf8wpGevJs91dWb-yt3Na51KTEBcU4skiRZPZ3EEWyBOioYXhRkYJwMZtzMfHmVaKNXiqgSLILRCC0YJgsJ-mb1lqlkPm4XK-SiojtKYA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حال‌وش:درگیری در منطقه تفتان-سیستان بلوچستان بین نیروهای نظامی جمهوری اسلامی و گروه های مسلح ناشناس:
@News_Hut</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/news_hut/73208" target="_blank">📅 12:36 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73207">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/98721d1ae5.mp4?token=KpslO5CYWeGnspCMC5MIsZwfS0S_a16YBJuHoahfIy0TC_g7SLe8d1YkggqA__8XWvm68Z5rbrhLQ_PY6D64r2QT9n8Q2feqfP38znMgyQDAWil2AN2ioOfhg9BM3TlPYIO3t5sEwRPbjPn0EHuy77dn49Erq6JkBdUX42Mw9UAsmRvnd219gqyukwPubl0WyyTsk2MS2Z7ADTO7PIE1OgDH8Nqp54GQ7KGvXGkkxGrStyF1-WF3PJ4qszuKQhlu4SRIoEBlOJiGsgDQ0_DLqFZQlbzDvcSEHIbmFGmx6qS2ZjceuHrmLsqM6bo_v0asT96QQBKPUyirqHuDezRPcTDuw8bQyuX3ttct3bsheRDd8SFDBpjgHPPFu98Gq369JEz0MeTqUW31r_VvemDdLKfcgEFxdDJiTk5q9-ZOPN4htSHy5p1NJsVIZHslAZQ6TPzV9bxAcDKrtr_oUsjYNv8CJ1OVIQkYJwreo7tcj-bZlecQ5VY9bkb6tDvPzSCUpeuSvJQ8XT9tXFWI8XFsqQyfK_tNxDSBHvtEP4aIETVF3b5rsKXBGNNweTr44Ojjiui7LYzQGbfnvWB8GFuRMA8myZ9piFFFYwkiRdlWhtZMzq4ZiUsIRgSCitBoeMl2GILaYi0fghA_bbueaNJmHh0UR1vf6yP_hyIgboTbNss" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/98721d1ae5.mp4?token=KpslO5CYWeGnspCMC5MIsZwfS0S_a16YBJuHoahfIy0TC_g7SLe8d1YkggqA__8XWvm68Z5rbrhLQ_PY6D64r2QT9n8Q2feqfP38znMgyQDAWil2AN2ioOfhg9BM3TlPYIO3t5sEwRPbjPn0EHuy77dn49Erq6JkBdUX42Mw9UAsmRvnd219gqyukwPubl0WyyTsk2MS2Z7ADTO7PIE1OgDH8Nqp54GQ7KGvXGkkxGrStyF1-WF3PJ4qszuKQhlu4SRIoEBlOJiGsgDQ0_DLqFZQlbzDvcSEHIbmFGmx6qS2ZjceuHrmLsqM6bo_v0asT96QQBKPUyirqHuDezRPcTDuw8bQyuX3ttct3bsheRDd8SFDBpjgHPPFu98Gq369JEz0MeTqUW31r_VvemDdLKfcgEFxdDJiTk5q9-ZOPN4htSHy5p1NJsVIZHslAZQ6TPzV9bxAcDKrtr_oUsjYNv8CJ1OVIQkYJwreo7tcj-bZlecQ5VY9bkb6tDvPzSCUpeuSvJQ8XT9tXFWI8XFsqQyfK_tNxDSBHvtEP4aIETVF3b5rsKXBGNNweTr44Ojjiui7LYzQGbfnvWB8GFuRMA8myZ9piFFFYwkiRdlWhtZMzq4ZiUsIRgSCitBoeMl2GILaYi0fghA_bbueaNJmHh0UR1vf6yP_hyIgboTbNss" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">عرازشه شب گذشته،  در میدان انقلاب تهران علیه مسی شعار دادند  !!!!!
@News_Hut</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/news_hut/73207" target="_blank">📅 12:27 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73206">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5be338c559.mp4?token=oxOrblnIh3okCCbL67_K4GZRj41SP3cp7EM37qllNpS300NkyAc496To4v_Bw3CZNnzBu3rYjKWRmiL1fxrY9dMF0OLA8v9De_psvMSgbvroox1ECd7vdgUIxMwJ39VyoICcTjUlYFVmft8ju1cc80niOXWM8JYxlAhnb2VYhaV9DUDuBhjy1ai23h4JnlZ91Um4QUJ_msg1weyN9S8uPDXz_tlPDVM1jcmaU00WNeWjdonwqDv2j3sAltuZVp4BjuYO7AbfmkV_5B2c3cHUQ6rUzcTyviB18L3166WvcLIXavFopmT4SYvRYJBcSj8nDqVS0xefsZ74wPeBrQNjcw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5be338c559.mp4?token=oxOrblnIh3okCCbL67_K4GZRj41SP3cp7EM37qllNpS300NkyAc496To4v_Bw3CZNnzBu3rYjKWRmiL1fxrY9dMF0OLA8v9De_psvMSgbvroox1ECd7vdgUIxMwJ39VyoICcTjUlYFVmft8ju1cc80niOXWM8JYxlAhnb2VYhaV9DUDuBhjy1ai23h4JnlZ91Um4QUJ_msg1weyN9S8uPDXz_tlPDVM1jcmaU00WNeWjdonwqDv2j3sAltuZVp4BjuYO7AbfmkV_5B2c3cHUQ6rUzcTyviB18L3166WvcLIXavFopmT4SYvRYJBcSj8nDqVS0xefsZ74wPeBrQNjcw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">عده‌ای از اراذل و اوباش سرکوبگر سپاهی و بسیجی با لباس شخصی و پرچم فلسطین و به بهانه حمایت از دانش‌آموزان فرانسوی در برابر سفارت این کشور در تهران تجمع کرده‌اند و علیه دولت فرانسه شعار می‌دهند:
«مکرون حیا کن، دانش‌آموز رو رها کن!»
@News_Hut</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/news_hut/73206" target="_blank">📅 11:59 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73205">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/news_hut/73205" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBe
t
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/news_hut/73205" target="_blank">📅 11:58 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73204">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rDfI6ocIwwO6Q5A_YgSsDPkStIZ597TNcVQN3YME6T99UfhzbWw7PBglF1TxIU6aOP58bJxv8ycHEY0Ryiqo7tZfL_ticp7upXdd0aC2AumRN97ZQyOI54nKodaAiFA1d7D4kwI7e1REemNmcCkoRAdioMSXm5skMcz2-ViO4sFdQsoGMQVhmMW8Vlk0DAirjSZz2HhXnPb3pRSf2bgTNPCGlaWsvXJTeTFbz3syYsZUQ-KP0p2_Y9iWzMkdqY2zlk7EvvxnoSieGVCFpMp6w0oHGuYXHCB0DFxDJKi2BXCqrs0jD0OweyIU3jZXhQbj-dfCMJV2NKWJOFO8dstD5g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🦖
بارسلونا
🆚
گالاتاسرای،
این نبرد حساس چمپیونزلیگ را در سایت بین‌المللی
TrexBet
پیش‌بینی کنید!
🦖
گزینه پیشنهادی:
بالای ۲۸.۵ شوت در مجموع بازی (Over 28.5 Total Shots)
با
ضریب 1.64
📉
با توجه به سبک هجومی دو تیم، تمایل به خلق موقعیت و آمار شوت‌های مسابقات اخیر، انتظار داریم دیدار گالاتاسرای و بارسلونا شاهد موقعیت‌های گل‌زنی متعددی باشد.
📉
بررسی ۵ بازی اخیر هر تیم نشان می‌دهد که مجموع شوت‌های مسابقات آن‌ها به‌طور میانگین نزدیک به ۳۰ شوت بوده است. به همین دلیل، خط ۲۸.۵ شوت می‌تواند گزینه‌ای قابل بررسی برای این دیدار باشد.
🦖
🦖
🦖
🦖
🦖
بونوس اولین واریز تا سقف ۱۰۰ یورو
🦖
بهترین ضرایب بین تمام سایت‌ها
🦖
واریز آسان و امن از طریق کارت به کارت
TREXBET — PLAY. PREDICT. WIN.
https://TrexBet.com
T.me/TrexBet_Ir</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/news_hut/73204" target="_blank">📅 11:58 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73203">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">پرونده کنکور ۱۴۰۵ بسته شد /نتایج نهایی اواخر آبان اعلام می‌شود
با اتمام مهلت انتخاب رشته داوطلبان، پرونده کنکور ۱۴۰۵ بسته شد و نتایج نهایی اواخر آبان اعلام می‌شود.
@News_Hut</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/news_hut/73203" target="_blank">📅 11:27 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73202">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e31f93a352.mp4?token=oY_tiBKiTZ9Y_EN4sw2pqlXy3_m3jYMkM-KGjAatVLsBOsxy_0k-FynfPOwvIGBkBcnWhxfGIQTQRS3Pm3NJkf_-SH0zT38BKiiTPb_qR_OKzlFXIg76aXnVwL2LBprpYswt3mZstTniz3VQzWx-mZ-3noSC3xEeObQs9WYHERlv0o_mKs2hMoQqA8r1OYvXiaQDttqvr3tefwsS7vtpO1iVP7VcAPsrIUDtdC-VKnu7EhO9HRfvFOyIP_82wQ4_o2Y7GyJjYLKGO0sxh86f3rCS1zfh0B5H3tiklrjUFcTySecvVu5OTFp716JBI16NS3aBc_Q9vfPLPu1ju8-nmkJTaDeKlc4f4pD9MQb4Cgi_bTxTp7iSezXMZ2ewL2invaPVSvQFoDrJSX4oauPokjomY7nIj7G6C-kRAM2RJKHnsqJuqeQ0gBCpyMkPmmFEz5dUMuzaLDdp8XGMfXMe3QyBjwzMXQvtcFO4686UQylST8ipBwDiP2VKE_xjeq_CktZaHYn78YPO802M7dHJIV2G7uAlab4TIjzx3cp85A6aLptod9bJN4sk1XVR6ume1wZ1QWQqTKyah3JRAN604Hj2fz-Y3O-ia7sqRnTnKkkuF6viXpMSYFl9hHLx9TbJ1dxkBKk71-Dbb3YM5i2pTnuAFBiOUKPKqapYY0wgaGU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e31f93a352.mp4?token=oY_tiBKiTZ9Y_EN4sw2pqlXy3_m3jYMkM-KGjAatVLsBOsxy_0k-FynfPOwvIGBkBcnWhxfGIQTQRS3Pm3NJkf_-SH0zT38BKiiTPb_qR_OKzlFXIg76aXnVwL2LBprpYswt3mZstTniz3VQzWx-mZ-3noSC3xEeObQs9WYHERlv0o_mKs2hMoQqA8r1OYvXiaQDttqvr3tefwsS7vtpO1iVP7VcAPsrIUDtdC-VKnu7EhO9HRfvFOyIP_82wQ4_o2Y7GyJjYLKGO0sxh86f3rCS1zfh0B5H3tiklrjUFcTySecvVu5OTFp716JBI16NS3aBc_Q9vfPLPu1ju8-nmkJTaDeKlc4f4pD9MQb4Cgi_bTxTp7iSezXMZ2ewL2invaPVSvQFoDrJSX4oauPokjomY7nIj7G6C-kRAM2RJKHnsqJuqeQ0gBCpyMkPmmFEz5dUMuzaLDdp8XGMfXMe3QyBjwzMXQvtcFO4686UQylST8ipBwDiP2VKE_xjeq_CktZaHYn78YPO802M7dHJIV2G7uAlab4TIjzx3cp85A6aLptod9bJN4sk1XVR6ume1wZ1QWQqTKyah3JRAN604Hj2fz-Y3O-ia7sqRnTnKkkuF6viXpMSYFl9hHLx9TbJ1dxkBKk71-Dbb3YM5i2pTnuAFBiOUKPKqapYY0wgaGU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ:
«شاید در برخورد با رهبران ایران زیاده‌روی کردیم، چون دیگه نمی‌دونیم دقیقاً با چه کسانی طرفیم!
راستش رو بخواید، به‌سختی می‌تونیم بفهمیم باید با چه کسی مذاکره کنیم. فکر می‌کنم زیادی جلو رفتیم.
می‌تونستیم همون سطح یک متوقف بشیم؛ رفتن به سطح دو و حتی دو و نیم، احتمالاً دیگه زیاده‌روی بود.»
@News_Hut</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/news_hut/73202" target="_blank">📅 10:59 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73201">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7ec03fa2f2.mp4?token=tUMiTw1kxtjqzVdCHF1HE9NpP3fL_COUhqrtr9ZQVUmPTvlStoYr03K8BWCiyLKvVhMYYSWXeDCC04uNr7ZQo4IyQ1iT690wiToTD5Z960MpQYKWU3Lr3YDpeV4iOGTMDybuYkF9cBCtDoptzpVJhluJk0-4SVO0Ht7MsRsqCsPd1-ec4X-gXfeO5L90jWDqlgxGPEodBodGujlCQJBGnw26lpbQ1aUp92T1Y605ERH2031RofSesNQAHgcbcGx7BTphP5ncsLFmTISs6NgTMAGttfvyg4bM6v2vqEyQfrRfk1aSU-W2sVz4-sKrS6ZFh-Wcsj0-NebLJ4_lthUc2g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7ec03fa2f2.mp4?token=tUMiTw1kxtjqzVdCHF1HE9NpP3fL_COUhqrtr9ZQVUmPTvlStoYr03K8BWCiyLKvVhMYYSWXeDCC04uNr7ZQo4IyQ1iT690wiToTD5Z960MpQYKWU3Lr3YDpeV4iOGTMDybuYkF9cBCtDoptzpVJhluJk0-4SVO0Ht7MsRsqCsPd1-ec4X-gXfeO5L90jWDqlgxGPEodBodGujlCQJBGnw26lpbQ1aUp92T1Y605ERH2031RofSesNQAHgcbcGx7BTphP5ncsLFmTISs6NgTMAGttfvyg4bM6v2vqEyQfrRfk1aSU-W2sVz4-sKrS6ZFh-Wcsj0-NebLJ4_lthUc2g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">چند شب پیش در تجمعات شبانه تبریز، یه دختر توی ۲۰ ثانیه کلاشینکف رو باز و دوباره سرهم کرد!
@News_Hut</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/news_hut/73201" target="_blank">📅 10:31 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73200">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">دونالد ترامپ:
«شعاری که از همه بیشتر دوست دارم، «همجنس‌گراها برای فلسطین»ه!
می‌دونید اگه تو اونجا همجنس‌گرا باشید، باهاتون چی کار می‌کنن؟ از بالای یه ساختمون پرتتون می‌کنن پایین.
شما رو می‌برن بالای بلندترین ساختمونی که دارن؛ البته ساختمون‌هاشون خیلی هم بلند نیست، ولی لازم هم نیست بلند باشه. از بالاش پرتتون می‌کنن پایین. با این حال، من مدام می‌بینم که می‌گن «همجنس‌گراها برای فلسطین»!
@News_Hut</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/news_hut/73200" target="_blank">📅 10:00 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73197">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/uGjJa9fCWwTDF6A7gFt65SvvHpk_1GBVk0SfRtvkAhTCr7OZRff0SG5zFeHuy6m3fdA7M0IzpPcC5Hv24Chm7nOzsTH6TAdNxGRpkzcd5aLUkK_FvK1Fz0d3CAWJjeZK8LUPs1gxHHuNjm3svBosf4z40tJrJDo-UbUSPJLBggWdfYUjqh8N1Mmu639a6FLeqMNG-0guVRE_uHl9Q77Zwhibb-yxMglVBG0cHRhcb7iarRM7TwglTw_AcGByGv3qYxdL6psBtv3T52lof6uZpPZVDVepLq5GLVaOYi-uozYKhqD_oMmK8Dq9GKqRndz9zE7XA7b65_A6Z-Gkx0CNJQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/k1xmCg9McpggXEp4BewLPmD7Kz2_742_wF6gEcWxaOH43jiRpa6CCr2OCKl-fdvdEkQP-dcMRUuh70Czb8lymN67i-dEQN9FOHCsHfAzHaim6hWZjdLlmmTxqdFsZ1FgmpItvnRHtsWgajygiJr4MWLythHaav7CcH63lt2WueeJe12L7NT8orzcOlZ_0YAZOV3nYzUyR_8S7k27OS5V1mAwSw3_rD2DaqZMM17Qy8D9-KtWxbYcNKHv9OUDBKyTf4UzD7iIf8sc42w1poDL4LiSpUOm8LdbbRwESPUQ4gh8PIa13_SvaIXRgkkpXFwPFd_STlloH5w9hoa6v4YQWA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/352c619970.mp4?token=djDPUOR79G_NqwOUD0hHKM9x7l6y_QAPgQ8UWuoEtLIADEcRXDq5G8HllWOCzUbb62F01cZg9Pgl3WFZhUMSM3EfbZG_104UZEM60UH-Bfk1uz2QoSTn__jL0tdOPtcmLy6M_9xN75cPGSSGqIM-la_o4oquEXGQhV3kQ80kHJ-8QR-PLZuNxGOkRhAKcP9dUy25ysmo4OsMtzINuegQXnUlKFb-6Dyf1892qOE1FgsbKpAGuA8n2lZz289mMOrhqvZQO_-sl1exX0N4YdHWjDRVsxPxZZxLeuO7FvM0CpKB23kQquMG3Qhj85_R9PAWVyIO7J3Q-bsohlxtdlzh1g" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/352c619970.mp4?token=djDPUOR79G_NqwOUD0hHKM9x7l6y_QAPgQ8UWuoEtLIADEcRXDq5G8HllWOCzUbb62F01cZg9Pgl3WFZhUMSM3EfbZG_104UZEM60UH-Bfk1uz2QoSTn__jL0tdOPtcmLy6M_9xN75cPGSSGqIM-la_o4oquEXGQhV3kQ80kHJ-8QR-PLZuNxGOkRhAKcP9dUy25ysmo4OsMtzINuegQXnUlKFb-6Dyf1892qOE1FgsbKpAGuA8n2lZz289mMOrhqvZQO_-sl1exX0N4YdHWjDRVsxPxZZxLeuO7FvM0CpKB23kQquMG3Qhj85_R9PAWVyIO7J3Q-bsohlxtdlzh1g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یه پسر دانش آموز ۱۶ ساله از اندامش فیلم گذاشته و حالا کامنت دخترا زیر پستش:
@News_Hut</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/news_hut/73197" target="_blank">📅 09:32 · 21 Mehr 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>

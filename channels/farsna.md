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
<img src="https://cdn4.telesco.pe/file/jnf4tpVuUsnUQFVu6JShczmXpIGXudOhGoAhkuqF7oTInQ43GtsEtKoKHZPZxMQiU_JYqxc4pWISiWx4s16Gy_h3RbtMz3hnXwxyj2CTu_XX7Jj8dgMmSdp46Zpl2vP1URq_lJzY4yz9LqVBKU0fuPmkQPBrltDvOY_uc1LGLzjTLrh9Xpzn_wDH9gzwjkTzMtehrY8w5sNXim2OqPuSimwjB98t6LBwOxW5vfDXP2TmryZ--4P7rgbW_wyTJxHGsGDAWjPmeZEVyaGHCmaAHkhC8HwcEc8bcVdQ3aDtJfM5adjT1wBwLgcoxJ8EMnxR2CwYRekp4mOn7eeePZ1BzQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرگزاری فارس</h1>
<p>@farsna • 👥 1.85M عضو</p>
<a href="https://t.me/farsna" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 حقیقت روشن می‌شود‌‌تبلیغات@Farsnews_adsارتباط@FarsNewsفارس‌پلاس@Fars_Plus‌ورزش@SportFarsجهان@FarsNewsIntعکس@FarsImagesپیام‌رسان‌ها@Farsnaاینستاگرامinstagram.com/farsnews.agencyتوییترtwitter.com/FarsNews_Agency</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-07-17 18:54:21</div>
<hr>

<div class="tg-post" id="msg-467332">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/My5odSG3P9rHSe9IiurguTPIkxYM8v8462qXeYj8Lo7TTLLJuBzkjyiJLUKmmzWmbCINhdN8zVeT0_WqYkbBEZgKV1XyUh0nbG8jq4PXdH5z21rIRhVAMjud3lHJALu2yjACYOEH1cZoCVv7oxDpewo_v9s6V0g8Jrr-TPFNj6fPstE9i8LP34rntBpZvoIHRQqK2otESjRVuQXfuK9Yy6ZliYT4jIjTVPAk3n8klxeX0QvWOj5ht52bqktendB_mfUuSa6CFBhgBFhpB13mdr9MFLt5Gbb4Z3QKkDuiVowCGmrt997vqlGSTfI1JG6p0fnanCi9UhtD6yHNPo6-aw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎥
وزیر آموزش‌وپرورش: قطعاً مدارس حضوری خواهد بود
🔹
ما تمام برنامه‌ریزی‌های لازم را برای حضوری‌شدن کامل مدارس انجام داده‌ایم.
🔹
اگر اتفاقی در نقاطی از کشور رخ بدهد، اختیاراتی به استانداران می‌دهیم و استانداران متناسب با آن شرایط، به‌صورت نقطه‌ای تصمیم‌گیری می‌کنند.…</div>
<div class="tg-footer">👁️ 945 · <a href="https://t.me/farsna/467332" target="_blank">📅 18:52 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467331">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/af2934295f.mp4?token=fJbGajBqbnvTf4Kn5N9PIL50HQl9fWXISjA7PkuVsaX1UmxgGn93hD5pD5klsCcoyqqIuZWK9tK7GGEVokbHIrYcoJZ2w7T8bSb-qGT2CQ94kIGzT6dw9Uk0KrAmbOZV6auCzXLWcivrsOG5HuUpZqWsvULMC3UZLvSwgI7q2aQLgz4Oi-SHL3WvK2zWtJX0KSJbTM1RakmXKB0vpydX5Fkoc9gClLmyUgTKhHWlOnBUx17uv4CN57wcdhVLvkuUzXv34pRKCkhZ_TMr8Sl9jDTUtoMBX5VKotl45pP84qlciKtREyoUrqCsOtHASo2zRVL85amM4JucsQazt0oxDQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/af2934295f.mp4?token=fJbGajBqbnvTf4Kn5N9PIL50HQl9fWXISjA7PkuVsaX1UmxgGn93hD5pD5klsCcoyqqIuZWK9tK7GGEVokbHIrYcoJZ2w7T8bSb-qGT2CQ94kIGzT6dw9Uk0KrAmbOZV6auCzXLWcivrsOG5HuUpZqWsvULMC3UZLvSwgI7q2aQLgz4Oi-SHL3WvK2zWtJX0KSJbTM1RakmXKB0vpydX5Fkoc9gClLmyUgTKhHWlOnBUx17uv4CN57wcdhVLvkuUzXv34pRKCkhZ_TMr8Sl9jDTUtoMBX5VKotl45pP84qlciKtREyoUrqCsOtHASo2zRVL85amM4JucsQazt0oxDQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سلطان، نام پلنگ جوان شناسایی‌ شده در رودافشان دماوند
🔹
مدیرکل محیط‌زیست استان تهران: یک پلنگ نر که پیش‌تر توسط اهالی روستا مشاهده شده بود، با تلاش محیط‌بانان و نصب دوربین تله‌ای شناسایی و نام سلطان برای آن انتخاب شد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 1.92K · <a href="https://t.me/farsna/467331" target="_blank">📅 18:44 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467330">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/577177c5a9.mp4?token=dPye-wFQIvqwguT_hijxjblkBE471MKtgyepwSU-39JK6izGB41lOT8LMiuW3DxexGYDNkI2js_NJiuMlC3YDnq0jOv9DEa1FuL71gbneWUeHdLgKZjpa7dRuP8CrYkOL2dw3w7gtzzztFqVA7v4w3s_4HeK7xAIqupsNtvT6Rm5yFEGj6-EdXvpDtpHQ9Rxy5UTeigvbwy3BR2du8y1DqrMFwYRKT19U-L7RgoPbrmRPtgt7i06uXDV-2ikOS-CTJi9kKEeoDce4iwnSgu5XZg0Fo6yxgReHXSDkrj_fXsor-j6mUReDKxBNxFM0ZfVSGCiVOetPLe-EH80RyiuLQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/577177c5a9.mp4?token=dPye-wFQIvqwguT_hijxjblkBE471MKtgyepwSU-39JK6izGB41lOT8LMiuW3DxexGYDNkI2js_NJiuMlC3YDnq0jOv9DEa1FuL71gbneWUeHdLgKZjpa7dRuP8CrYkOL2dw3w7gtzzztFqVA7v4w3s_4HeK7xAIqupsNtvT6Rm5yFEGj6-EdXvpDtpHQ9Rxy5UTeigvbwy3BR2du8y1DqrMFwYRKT19U-L7RgoPbrmRPtgt7i06uXDV-2ikOS-CTJi9kKEeoDce4iwnSgu5XZg0Fo6yxgReHXSDkrj_fXsor-j6mUReDKxBNxFM0ZfVSGCiVOetPLe-EH80RyiuLQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
گل اول پرسپولیس توسط بیفوما در دقیقه ۴
⚽️
پرسپولیس ۱ - ۰ صنعت نفت @Farsna</div>
<div class="tg-footer">👁️ 2.9K · <a href="https://t.me/farsna/467330" target="_blank">📅 18:37 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467329">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/v9sGTXnrCdVGp4ytbSlS5pk_G2L69P7RtEKpXGheTaE9PAR1ugcLhrvf5unNe-8R-Z8NoRrnzNxWWcQz5hpQqD0MUZ4tDW37Yjdmf3ANQ_ANFo80qVIZd0fXKNsU05gy6dRBb0sFtUJpScGsle-GYOh9EJYlUB3LGa_MzHpbizjNtW1TYmSGmuUKrfROhSQjpHe8CYMtgr37kBSYAa5eFJThwqdsa_CYqGn_KM2PxJM4SjDkYHfgcsZfzqyvZ0J6pdbi9_58pygEaEeWwfi6wMjAfvjEDIpdcjO8XSoagiRtSIm5SgSyF3juCF_YVpPjurt8oqcw7c8L3oHM2FGDbw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‌  یمن: مانع حرکت مزدوران سعودی به‌سوی باب‌المندب شدیم
🔹
سخنگوی نیروهای مسلح یمن: تحرکات مزدوران سعودی برای پیش‌روی به‌سوی باب‌المندب با مقاومت رزمندگان ناکام ماند و حملات موشکی موجب تخریب تجیهزات و کشته و زخمی شدن ده‌ها نیروی دشمن شد. @Farsna</div>
<div class="tg-footer">👁️ 3.57K · <a href="https://t.me/farsna/467329" target="_blank">📅 18:31 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467327">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/A3cdYsJYbS6YqSfX0NaNXqA5llkvQ1sNX_5EBHourj6tbBF42Vlf6bROGhCBOdcXod5U_-MPuJytHYKqLOL5ioiSw0el-bnrlOpnmrdkP2rfqgICiG_R2WIjgTKBS08f7mGZAUCJMOK9MLWGfHlgqw0Okj_67ntEaDBYlVXkco6sXtH3Sysf4dl-62JAoqWv5Iv2r2ZCo1PChSif_ILkq3WdlsLBR9ldoWM6OUdGb8OKFYzJP5uU0SfsrVPQ2bqqDqNTl-uXUzdbm9VgfD7WIxTOkZIwBD24CFD4NjqJzuJx6kC6pidLjUX-IzspcCxA7Fc22FbUse7P8kRQ8H7tAA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
یکی از ستون‌های مستحکم امنیّت کشور
@Farsna</div>
<div class="tg-footer">👁️ 3.9K · <a href="https://t.me/farsna/467327" target="_blank">📅 18:21 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467326">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2bbad3ed44.mp4?token=AkjoVcwfxeqeocoa1d1_neAfCJPbzq_NMF-moiP3PD8hofFFtkqZdIewEUVBYugPKrkO7V8kMN9gpV8qH0u8X0yHB1477fj86DLmhwJzRHg7oZXj4VYwS4s8qADdE2k6iFD2C2QsCCr-l9eLI7F76RKATQgrsAfy8o1E3RxwSbo8McIDlClksnQVoZDGNZCabFk1KT7u2JnMRuelOqQ_sYHlckTq_usvHTo57WkwPAMrL8NsROmNjoKyGo0KKMQA9jyH0CeXRQvGYDw8jYzx3k-ZRQMdaAd62aSG3fBqYbyCtdoswpxp2nYo3f3yh00_kVJZkk7wETgdHH4Dk1DFJWvouFF7EmFEJHABJFnoEfOdF-_PI9y6HH9modsxE9J3oyAu65hbjW6JDPJ8UyQZKDpbqSr5fcL1maXuNrCNlXu7jcOvNiq7c4dLXqYYoGUs70HfQUsmeL0HSvf_AGvrMlWcWFDho9E9oaDIa6Y_rzz8DBB9b0Eg9_S_n2b3FGZCL1Lv5o1xsZDJ9XF-xwQ0NE1dgcmv2kmjl5Vg5xcHtk_AMGDjar0Z36XON8l5HWVQqbUSYSzKxGSaDPmFREaYCwQXhRuzTlqzCeDzeBS9sEerg8MW5Mj2URwF62Y1fEMOhdZrMe97tVP882EvdLI_WxPrkPjCdNw-S1TlVkwV_TA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2bbad3ed44.mp4?token=AkjoVcwfxeqeocoa1d1_neAfCJPbzq_NMF-moiP3PD8hofFFtkqZdIewEUVBYugPKrkO7V8kMN9gpV8qH0u8X0yHB1477fj86DLmhwJzRHg7oZXj4VYwS4s8qADdE2k6iFD2C2QsCCr-l9eLI7F76RKATQgrsAfy8o1E3RxwSbo8McIDlClksnQVoZDGNZCabFk1KT7u2JnMRuelOqQ_sYHlckTq_usvHTo57WkwPAMrL8NsROmNjoKyGo0KKMQA9jyH0CeXRQvGYDw8jYzx3k-ZRQMdaAd62aSG3fBqYbyCtdoswpxp2nYo3f3yh00_kVJZkk7wETgdHH4Dk1DFJWvouFF7EmFEJHABJFnoEfOdF-_PI9y6HH9modsxE9J3oyAu65hbjW6JDPJ8UyQZKDpbqSr5fcL1maXuNrCNlXu7jcOvNiq7c4dLXqYYoGUs70HfQUsmeL0HSvf_AGvrMlWcWFDho9E9oaDIa6Y_rzz8DBB9b0Eg9_S_n2b3FGZCL1Lv5o1xsZDJ9XF-xwQ0NE1dgcmv2kmjl5Vg5xcHtk_AMGDjar0Z36XON8l5HWVQqbUSYSzKxGSaDPmFREaYCwQXhRuzTlqzCeDzeBS9sEerg8MW5Mj2URwF62Y1fEMOhdZrMe97tVP882EvdLI_WxPrkPjCdNw-S1TlVkwV_TA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
پشت‌صحنهٔ خبر بازگشت گلشیفته فراهانی
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 4.71K · <a href="https://t.me/farsna/467326" target="_blank">📅 18:12 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467325">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">🎥
نمایش دستاورد علمی ایران در درمان فلج مغزی کودکان برای اولین بار؛ سل‌تک فارمد نور امید را روشن کرد
🔹
همزمان با روز کودک، حدود ۲۰ خانواده از کودکان فلجِ تحت درمان سلول‌درمانی، در جشن «رویش امید» گرد هم آمدند تا روایتگر تغییرات و امیدهای تازه در مسیر درمان فرزندانشان باشند.
🔹
سلول‌درمانی، فناوری نوین پزشکی در لبه دانش جهانی است؛ عرصه‌ای که ایران با تولید ۲۰ محصول از حدود ۱۵۰ محصول سلول‌درمانی جهان، سهمی قابل‌توجه در آن دارد.
🔹
سل‌تک فارمد تنها سازنده داروی فلج مغزی کودکان در ایران است و ۳ محصول دیگر در زمینه درمان‌های پوستی و مفاصل دارد.
@Farsna</div>
<div class="tg-footer">👁️ 4.27K · <a href="https://t.me/farsna/467325" target="_blank">📅 18:11 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467324">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NpuzuAyofTSxBEa-wg83-2iLNMCcjmHcfF56VS6wcbmuoQmYwK8DRv8P3keJX59N5-ViuRlnyX-H72ZVK_OZdR5IQi5WCMFTMnJP2aA1pFcYIxJpyeFnwbuXPPRH5us_ZmIY1myc8tfqJsZ-tKN-ODtiALvXycP66A83qcYMXC8l5rP5V-HPhob3tTfYyVg4pLHZwRWMW_3Mji7_xTTTHrJA7QI5dd-duPChWMY5fKfy1qq9pCaKadP68tbBsqZcRBT5hzI0qlalzCXyGkp9uTGLrovpDghD3hZi2V9zeY4ObZi3Qlsjhf-t4iBui6x2MhOaSFhhYUsXbTUCqgDweA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یار دبستانی اُپارک شروع شد!
🎒
💦
شروع مدرسه رو با یه خاطره هیجان‌انگیز برای کوچولوها همراه کنید!
🥳
اُپارک به نوآموزان متولد سال‌های ۱۳۹۸، ۱۳۹۹ و ۱۴۰۰ یک بلیت هدیه می‌ده.
🎁
📅
۴ تا ۳۰ مهر
🎟️
کافیه هنگام مراجعه، کارت شناسایی معتبر کودک رو همراه داشته باشید تا بلیت هدیه‌تون رو دریافت کنید.
👇
برای مشاهده شرایط کامل و اطلاعات بیشتر، همین حالا وارد لینک زیر شوید:
🔗
لینک</div>
<div class="tg-footer">👁️ 3.92K · <a href="https://t.me/farsna/467324" target="_blank">📅 18:10 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467323">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-footer">👁️ 3.65K · <a href="https://t.me/farsna/467323" target="_blank">📅 18:09 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467322">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/opAbzu2Dye8yTUWjNYBMbMWJ2DymGScJTkRjBgvARkyzVk2MWou4r2L0H8-q8e0EFG9T5nwI8bS1pgJsXoW8qwzb2M-drGNHhz0lAFEt_Kq5omPRfmPmlK5k11VyZ0W6PQ7y6z-3_tQNfdfh_QKDCJqkAK1Iy1gtpqMT0AFIyKqk7XCmJDzHIeXr2US_wwXCP9MUSIHdcDLjIGAlBOGiHUU3rWeMK82ehMYpdo4dHYytonDlX0TnCAo5oAUoASepfBbeUH0l6r_DYosrzEj7MWjfuVf7z1cjzmlpI-IIYWWzEcO695E5y9MBK1k3b7p5WrbKRjXQYtdadN_stnhbCQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هشدار مدیریت بحران به ۶ استان کشور دربارهٔ بارش شدید باران
🔹
مرکز مدیریت بحران کشور در پی صدور هشدار نارنجی هواشناسی برای روزهای ۱۸ و ۱۹ مهر، از استان‌های گیلان، مازندران، گلستان، خراسان شمالی، خراسان رضوی و سمنان خواست با تشکیل جلسات ستاد بحران، اقدامات پیشگیرانه را اجرا کنند و دستگاه‌های اجرایی و امدادی را برای مقابله با رگبار باران، رعدوبرق، وزش باد شدید و گردوخاک به آماده‌باش کامل درآورند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 4.51K · <a href="https://t.me/farsna/467322" target="_blank">📅 17:59 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467321">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/r7qoKyfDccEwbvNtS5TqtZR_8MIAp8nOSLSrOdgOWfuezsDhITXaZZVP1cvmoJEtIbnVL1O6FAsBwjAIGlSblT00VFrpDyypN7XUtURI07j2twy_L2b8AeJOomjZ2Pr605ov0ZKb-XJuiVX8AVkN5qWvYR-mBmEX6vpiQc_7wZdXHEJShi8wJuG2qIldEZEMZulkTssIrpVIilNQlYpc6Y7NyeJoJHUQOMipYPxFsAyqe8r03eqMOE4hNdcjX-jaq_yJbFE3SXWXbsyWB3Dhq9nyWwg7ipvNB1_GI4a2cpqtKywTFAgSmy7isRX0W1cGNh5AxQiDK2OIJsjWaEYOZg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">واکنش سخنگوی وزارت خارجه به مواضع متناقض فرانسه دربارهٔ موضوع تسلیحات هسته‌ای
🔹
امانوئل ماکرون رئیس‌جمهور فرانسه به هنگام آزمایش یک موشک بالستیک دارای قابلیت حمل کلاهک هسته‌ای می‌گوید: «برای آزاد بودن باید ترسناک بود؛ و برای ترسناک بودن، باید قدرتمند بود.»
🔹
اما همین امانوئل ماکرون درباره ایران که از اساس دنبال سلاح هسته‌ای نبوده است، گفته: «ایران هرگز نباید صاحب سلاح هسته‌ای شود؛ نه امروز، نه پنج سال دیگر، نه ده سال دیگر؛ هرگز.»
🔹
مسئله این نیست که فرانسه چرا بازدارندگی هسته‌ای دارد؛ مسئله این است که چرا منطقی که برای فرانسه ضامن امنیت و آزادی است، درباره ایران، حتی در بحث از برنامه هسته‌ای صلح‌آمیز و تحت نظارت بین‌المللی، ناگهان به «تهدید» تبدیل می‌شود؟
🔹
واقعیت تلخ این است: آنها صلح را برای همه نمی‌خواهند؛ انحصارِ ترسناک بودن و مشروعیتِ ترساندن را می‌خواهند. خودشان باید قدرتمند و هسته‌ای و البته ترسناک بمانند و دیگران را حتی کشورهایی را که صرفا به دنبال انرژی صلح آمیز هسته‌ای هستند، با تصویر دروغین «تهدید هسته‌ای» محدود کنند.
🔹
صلحی که در آن قدرت‌های هسته‌ای، سلاح خود را ضامن آزادی و امنیت می‌دانند، اما همان منطق را برای دیگران تهدید می‌خوانند، نه صلح، که انحصار قدرت بر مبنای خودبرترپنداری است.
🔹
نظمی که برخورداری از امنیت و صلح را حق همگان نمی‌داند، بیش از آنکه حافظ صلح باشد، مشوق سیطره‌طلبی یک جمع خاص است.
@Farsna</div>
<div class="tg-footer">👁️ 4.28K · <a href="https://t.me/farsna/467321" target="_blank">📅 17:57 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467320">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6a3b26fd38.mp4?token=Z5356hTGDEr1o_aOsv0Yev9PFAe0GS6Zlfaf2HLgjtlxMDGQ5wJtn01nUQNVF41QuxsiZnMBcB5ZRc8GZ6t_pgoKIc5sKZTULXWfBGR8wO1WnVxODMEW5chP7bwGA_sDXD4n8cIXA2W517nxq4wtgsa3QaUPAsqOhEJvhOpj8US8D6TL4BBvu4ca0uBi_QpiePEDWKLAwl_vDDLzVR54LIciXhLOLjGinW7aInThoNxdmt_muD7wV6K8BoqAlxUhWMJLe3huuhKjCPWd6YNOKUHOwXzbNtXDeDNcSEgAIjIaRY1RdrYuIPZwhpn7X4a-nb_Xdqaq3j4_t6bGEd-mOA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6a3b26fd38.mp4?token=Z5356hTGDEr1o_aOsv0Yev9PFAe0GS6Zlfaf2HLgjtlxMDGQ5wJtn01nUQNVF41QuxsiZnMBcB5ZRc8GZ6t_pgoKIc5sKZTULXWfBGR8wO1WnVxODMEW5chP7bwGA_sDXD4n8cIXA2W517nxq4wtgsa3QaUPAsqOhEJvhOpj8US8D6TL4BBvu4ca0uBi_QpiePEDWKLAwl_vDDLzVR54LIciXhLOLjGinW7aInThoNxdmt_muD7wV6K8BoqAlxUhWMJLe3huuhKjCPWd6YNOKUHOwXzbNtXDeDNcSEgAIjIaRY1RdrYuIPZwhpn7X4a-nb_Xdqaq3j4_t6bGEd-mOA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
پزشکیان پس از شرکت و سخنرانی در ۲ اجلاس سران کشورهای مشترک المنافع و اجلاس محیط‌زیستی خزر، ترکمن باشی را به مقصد تهران ترک کرد.
@Farsna</div>
<div class="tg-footer">👁️ 4.46K · <a href="https://t.me/farsna/467320" target="_blank">📅 17:51 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467319">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Af5WWh_l5Q8GitdfzK0EslFOUxJQqZdH43vHbUH_gMm8xDBFkj5pqXPkyKaGAyoe-NYXeVYOjPj46-E0Fb93Nsr7YqxPgmzIRzw4ADtTPBA9Rk8DuFT33_QYYMggSgsQHmYfuEhdvh7MVq71a5O7EDTNtIGW20dBHprWw_SA4U36_33Xi0waxa8uSOKL1_T_r9V-fTBLSrD6G02HaayadlR2nEouyfMpUHsPw7OdshEcZAP--yW0kubI608KrjJIAVzGlB-IekFXEE2v0Xa4HDehnZ4Bjnf-AgRnw1w67gRicnXAbbHNbkVGswW4lh6brZgtUOw-7aIkqKh7ENHupg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
انفجار در مسیر خودروی پلیس در زاهدان
🔹
دقایقی پیش یک بمب کنار جاده‌ای در مسیر حرکت یک دستگاه خودروی پلیس در چشمه زیارت زاهدان منفجر شد.
🔹
اخبار اولیه از جراحت چند نیروی پلیس در این حادثه حکایت دارد.
📝
اخبار تکمیلی متعاقبا منتشر میشود. @Farsna</div>
<div class="tg-footer">👁️ 5.4K · <a href="https://t.me/farsna/467319" target="_blank">📅 17:44 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467317">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/080ffd578f.mp4?token=CQOKx6FKELaCxnzM60SCg6myjZ13KqEpzKwOrP7BjeBcM6B1d7IT8BidfU2ORmKcrBHLuGnVZs3O2EWZdQLbYkgDaB47PsIKZUN-T-581xlQKNqo66oZ1IO_mtaGA2lSp6O0po7gISynKR5Tn-uU6ipi563IucR_j8gXM76hrHC2ZrZsdfFRx4ej4OdfYdmHEQRXxgp1b5gMx9uVs0Piljq3fdUIwrnk5DK4o69_-Ugsm-dVOGr6qEIN_CGkAFHIEOIqZlmFhWvnzzHcauFw5Tb7elL7F0aq9ivlM_vr-YjlU0ouKAl7oQ-Iw1GCpazEnhaMwYvmzvsNnTh4VTGtcQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/080ffd578f.mp4?token=CQOKx6FKELaCxnzM60SCg6myjZ13KqEpzKwOrP7BjeBcM6B1d7IT8BidfU2ORmKcrBHLuGnVZs3O2EWZdQLbYkgDaB47PsIKZUN-T-581xlQKNqo66oZ1IO_mtaGA2lSp6O0po7gISynKR5Tn-uU6ipi563IucR_j8gXM76hrHC2ZrZsdfFRx4ej4OdfYdmHEQRXxgp1b5gMx9uVs0Piljq3fdUIwrnk5DK4o69_-Ugsm-dVOGr6qEIN_CGkAFHIEOIqZlmFhWvnzzHcauFw5Tb7elL7F0aq9ivlM_vr-YjlU0ouKAl7oQ-Iw1GCpazEnhaMwYvmzvsNnTh4VTGtcQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
طوفان سهمگین در راه سواحل آمریکا؛ هشدار تخلیه در سه ایالت
🔹
مرکز ملی طوفان آمریکا اعلام کرد طوفان «ایسایاس»، قرار است شامگاه جمعه به وقت محلی در نزدیکی مرز ایالت‌های فلوریدا و آلاباما به سواحل آمریکا برسد، به یک طوفان بزرگ رده ۳ تبدیل شده و سرعت بادهای پایدار آن به حدود ۱۹۳ کیلومتر بر ساعت رسیده است.
🔹
بر اساس هشدارهای هواشناسی، وقوع قطعی گسترده برق، بالا آمدن سطح آب دریا تا حدود ۲.۷ متر و بارندگی تا ۳۸ سانتی‌متر در مناطق ساحلی محتمل است. همچنین احتمال شکل‌گیری گردبادهای ناگهانی وجود دارد که می‌تواند فرصت کمی برای واکنش و پناه‌گرفتن به ساکنان مناطق آسیب‌پذیر بدهد.
🔹
در پی نزدیک‌شدن این طوفان، در بخش‌هایی از ایالت‌های آلاباما، فلوریدا و جورجیا وضعیت اضطراری اعلام شده و دستور تخلیه برخی مناطق ساحلی در آلاباما و فلوریدا صادر شده است. مقام‌های محلی از ساکنان مناطق در معرض خطر خواسته‌اند هشدارها و دستورالعمل‌های ایمنی را جدی بگیرند.
@FarsNewsInt</div>
<div class="tg-footer">👁️ 4.97K · <a href="https://t.me/farsna/467317" target="_blank">📅 17:41 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467316">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qUb1SpiAXAYCrZtebekwzb8Stnrz_aCcSByaEXKG_Crxuy2qU_mv9_q35QG1HiFyLlhpEy3BFN4NUzN0o1yae-ExnhUjux9tLEkMYs9-4I1Xj_GthnXrOUAi4lDuWpbfWaz_Uki3FeiEwJ6E3F7LYNjtYNcKrPGfne92IR9z9049I8Y18Eo2FZvS1CFooHJrNvhLNeP_Gf-bp5LnScS7GpajINLgCxaAgCh1NTgEmNyCTyK6Z-bCsoyBNn7uOyK7QW05WhkAvq34z7gVmY6o5MSsPjl5tzjNM37Xya9Bi2UrbotRj9SWT6s2mwdmRgpzC9SDyt1kXmIZrgXczm0WUA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بورس آمریکا اسیر هرمز
🔹
ریزش ارزش سهام شرکت‌های آمریکایی در سایهٔ تنش با ایران ادامه دارد.
🔹
مطابق آخرین داده‌ها، حدود ۷۰ درصد شرکت‌های بزرگ آمریکایی در ماه گذشته میلادی بازدهی منفی داشته‌اند.
🔹
افزایش تورم در اثر ادامهٔ تنش‌ها در منطقه و کاهش عرضهٔ نفت، شرکت‌های آمریکایی را با بحران مواجه کرده است و پیش‌بینی می‌شود این بحران به زودی دامن‌گیر شرکت‌های پیشرو بورس نیز بشود.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 5.74K · <a href="https://t.me/farsna/467316" target="_blank">📅 17:26 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467315">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">ترکمنستان چه می‌خواهد و گلستان چه دارد؟
🔹
ترکمنستان سالانه میلیاردها دلار کالا وارد می‌کند؛ و سوال اینجاست سهم گلستان به عنوان همسایه اصلی مرزی از این بازار چقدر است؟
🔹
ترکمنستان در سال ۲۰۲۵ بیش از ۵.۱ میلیارد دلار واردات داشته، در حالی که گلستان در همین سال ۴۸۱.۷ میلیون دلار کالا به ۲۸ کشور صادر کرده است. لوله و محصولات فولادی، فرآورده‌های پلیمری و محصولات غذایی، بخشی از ظرفیت صادراتی استان برای حضور در بازار همسایه شمالی است.
🔹
اما نکته اینجاست که ظرفیت به‌تنهایی کافی نیست؛ رقابت قیمتی، کیفیت، بسته‌بندی و حرکت از خام‌فروشی به سمت محصولات فرآوری‌شده، شرط ماندگاری در این بازار است. کارشناسان نیز بر ضرورت شناخت دقیق کالا، خریدار، قیمت و مسیر صادرات تأکید دارد که اینچه‌برون می‌تواند دروازه ورود کالاهای گلستان به بازار آسیای مرکزی باشد.
🔸
اکنون سفر پزشکیان به عشق‌آباد و اکسپو ۲۰۲۶ گرگان فرصتی است تا دیپلماسی اقتصادی از تفاهم‌نامه عبور کند و به قراردادهای واقعی، سرمایه‌گذاری و اشتغال برسد.
🔸
مسئله گلستان کمبود ظرفیت نیست؛ مسئله، تبدیل این ظرفیت‌ها به سهمی واقعی از بازار ترکمنستان است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 6.06K · <a href="https://t.me/farsna/467315" target="_blank">📅 17:15 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467314">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">🔴
تداوم حملات هوایی عربستان به پایتخت یمن
🔹
شبکهٔ خبری المیادین از ۱۰ حملهٔ هوایی عربستان به جنوب صنعا پایخت یمن گزارش داد.
🔹
المیادین گفت که در این حملات، شبکهٔ مخابرات هدف قرار گرفته است. @Farsna</div>
<div class="tg-footer">👁️ 5.76K · <a href="https://t.me/farsna/467314" target="_blank">📅 17:13 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467313">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1104e3f811.mp4?token=ti8bss-axaTxHSUhClOeQiZGzxrA_XquTBZg9euC_1XLhGJGm7t_5a8EpUCqSX_wunrpUVyAhTk6a6gzt01te2ClBtw9hXhFBCmmmnF3a5FBTwB5PVycVrvKZf-N353hPIUzFweVChefD3TodFbFsalhr7bG42KQrXQ2yO8ijPqyua2E_aj7s0xLckX7q5Zv8g2JFvEpKNCjkVr40JLVEKXe9dUj9ESQEujvWdTjW1GNuhmpU46r4guJCMfdWHWXS5kXlLbaOO02R8TPnEFE3SIkzLKUEQ37CZC0_wqwn41waHyywzyeO_NMRGWGbaZ6umvkXXZiVkENTUndwqvNRA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1104e3f811.mp4?token=ti8bss-axaTxHSUhClOeQiZGzxrA_XquTBZg9euC_1XLhGJGm7t_5a8EpUCqSX_wunrpUVyAhTk6a6gzt01te2ClBtw9hXhFBCmmmnF3a5FBTwB5PVycVrvKZf-N353hPIUzFweVChefD3TodFbFsalhr7bG42KQrXQ2yO8ijPqyua2E_aj7s0xLckX7q5Zv8g2JFvEpKNCjkVr40JLVEKXe9dUj9ESQEujvWdTjW1GNuhmpU46r4guJCMfdWHWXS5kXlLbaOO02R8TPnEFE3SIkzLKUEQ37CZC0_wqwn41waHyywzyeO_NMRGWGbaZ6umvkXXZiVkENTUndwqvNRA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
گل اول پرسپولیس توسط بیفوما در دقیقه ۴
⚽️
پرسپولیس ۱ - ۰ صنعت نفت
@Farsna</div>
<div class="tg-footer">👁️ 5.91K · <a href="https://t.me/farsna/467313" target="_blank">📅 17:09 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467312">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YwXopFHhK0t_xhd3Pz2e9vobjU75MCvp9HBxWp_zux3M-egBvtJpDKD_sGER06Wojki9j2wDc6rGTeJmGCUKO9xfksJFLb6n669k_TE0IYhcWp_LhoT7TN0VE4DJ-xNRirOS2R6Oq-MLcgblW1jQK6r5n88FJS_NVBIRwcgEPYX7xPJa6iwJLFNVX0Ccu1KyundnAIhGKRUlIbUM1C8pVN0ED9kaeoxrSUWXCGxYFoTncmPIIDzAFDC7_hsXGI_ieyafVYk0Xz2P_ji3vmxpbgUa3nU3ESDDO2RKhOCkFuYqXvGQWhvhgo2WTDtv0nq1I5plvBohgUdg8tjEou7pbw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آیا پزشکیان در عشق‌آباد برگ برنده را رو می‌کند؟
🔹
سفر رئیس‌جمهور ایران به ترکمنستان، فراتر از دیدارهای دیپلماتیک و گفت‌وگوهای معمول، می‌تواند فرصتی برای بازتعریف روابط دو همسایه باشد؛ فرصتی که اگر با تصمیم‌های عملی همراه شود، معادلات منطقه و به ویژه شمال کشور را تحت تأثیر قرار می‌دهد. اما سؤال اصلی اینجاست: آیا این سفر می‌تواند به نقطه عطفی در همکاری‌های اقتصادی ایران و ترکمنستان تبدیل شود؟
🔹
استان گلستان به واسطه موقعیت جغرافیایی، مرز مشترک با ترکمنستان و پیوندهای تاریخی و فرهنگی و قومی ظرفیت‌هایی دارد که هنوز تمام ابعاد آن در مناسبات دوجانبه ایران و ترکمنستان به کار گرفته نشده است. در این میان، نسبت میان ظرفیت‌های موجود و آنچه تاکنون در میدان عمل محقق شده، پرسشی جدی پیش روی سیاست‌گذاران قرار می‌دهد.
🔹
تجربه همکاری‌های منطقه‌ای نشان می‌دهد که همسایگی به‌تنهایی مزیت اقتصادی نمی‌سازد؛ آنچه اهمیت دارد، تبدیل ظرفیت‌های جغرافیایی به سازوکارهای پایدار برای همکاری‌های مشترک است. از همین منظر، دیدگاه کارشناسان درباره آینده روابط دو کشور و الزامات عبور از توافق‌های روی کاغذ، اهمیت ویژه‌ای پیدا می‌کند.
🔹
ایده منطقهٔ آزاد تجاری اینچه برون _ آلتین‌عصر همان نقطهٔ عطفی است که می‌تواند پایه گذار روابط نوین این ۲ کشور همسایه و تحقق اتصال واقعی ایران به بازار ۲۲۰ میلیونی آسیای میانه باشد.
🔸
اکنون نگاه‌ها به نتایج این سفر و تصمیم‌هایی دوخته شده که می‌تواند مسیر آینده همکاری‌های تهران و عشق‌آباد را مشخص کند؛ تصمیم‌هایی که آثار آن، در صورت تحقق، محدود به روابط دیپلماتیک نخواهد ماند.
🖼
سوال اصلی همچنان این است: آیا این بار پزشکیان برگ‌برنده را رو می‌کند؟
اینجا
بخوانید.
@Farsna</div>
<div class="tg-footer">👁️ 6.88K · <a href="https://t.me/farsna/467312" target="_blank">📅 16:56 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467311">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4c2f4c6813.mp4?token=HFVWAzVII86HxM7Uqc0Py3Suu2g-HJaPiQy7cWzxzyHutGylEV9IQjIDQM4LsZrHA99qzk-ElE_B4LkEjj9GYtyAZdwy_yZBbFy8ZRA025PVB0k6RbxxVTb-TXj-ztbjBlQdt0MV54fVqPDLM3Nv9o9xmTVjJa2YGZsQLNm-dwhYVtmfNyuG4vJbnsWVYuDAAPlDlHEYP7A4PtMiGiW07DKHujix6SYpWkeh3hcF1QAGeP1zP-OgdBmesEF8Sz7rSdT0hjwxr4dBloO2wCqJeS9NEEEJ496WRQVCoatiRwqEmGSvIaLV0AjV8HLD79Gcf7NRvFNopO_56oLMnlUZTDKvTcWcdsNHBAn6shIa74H_XtE6x46N6Vr0iSBApZgD_rQ7K5Is-tyVAyYy0wjoUx6JmyFcFTAghCzXuddIdODvNiLhe9qGc7CrFcorypNuQ5fnCgYamqaY34dNf4tzeguSNmLoi-nPcy-l7hnQ3mmXrP0hIGc3bf2LTnz9Ez5N3EEJBWs5AB0-s_zAJX3IWsLH-elrtOExEaz3hoBQx60NWYzx6YIRevi0I_ihTeHxm4rimSAnQCMqIPhzfcZ8EpCG15ULCy_9IXmhyRKJqwtEBH0kvAkqyYc3H-zcZvTgpKn6iV1NOuTQlEqhG2UjkQMtezEo8zhaRtsmuEIdL2o" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4c2f4c6813.mp4?token=HFVWAzVII86HxM7Uqc0Py3Suu2g-HJaPiQy7cWzxzyHutGylEV9IQjIDQM4LsZrHA99qzk-ElE_B4LkEjj9GYtyAZdwy_yZBbFy8ZRA025PVB0k6RbxxVTb-TXj-ztbjBlQdt0MV54fVqPDLM3Nv9o9xmTVjJa2YGZsQLNm-dwhYVtmfNyuG4vJbnsWVYuDAAPlDlHEYP7A4PtMiGiW07DKHujix6SYpWkeh3hcF1QAGeP1zP-OgdBmesEF8Sz7rSdT0hjwxr4dBloO2wCqJeS9NEEEJ496WRQVCoatiRwqEmGSvIaLV0AjV8HLD79Gcf7NRvFNopO_56oLMnlUZTDKvTcWcdsNHBAn6shIa74H_XtE6x46N6Vr0iSBApZgD_rQ7K5Is-tyVAyYy0wjoUx6JmyFcFTAghCzXuddIdODvNiLhe9qGc7CrFcorypNuQ5fnCgYamqaY34dNf4tzeguSNmLoi-nPcy-l7hnQ3mmXrP0hIGc3bf2LTnz9Ez5N3EEJBWs5AB0-s_zAJX3IWsLH-elrtOExEaz3hoBQx60NWYzx6YIRevi0I_ihTeHxm4rimSAnQCMqIPhzfcZ8EpCG15ULCy_9IXmhyRKJqwtEBH0kvAkqyYc3H-zcZvTgpKn6iV1NOuTQlEqhG2UjkQMtezEo8zhaRtsmuEIdL2o" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
پزشکیان: گفتگو زمانی کاربرد دارد که در سایهٔ زور نباشد  @Farsna</div>
<div class="tg-footer">👁️ 5.39K · <a href="https://t.me/farsna/467311" target="_blank">📅 16:55 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467310">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">🔴
تداوم حملات هوایی عربستان به پایتخت یمن
🔹
شبکهٔ خبری المیادین از ۱۰ حملهٔ هوایی عربستان به جنوب صنعا پایخت یمن گزارش داد.
🔹
المیادین گفت که در این حملات، شبکهٔ مخابرات هدف قرار گرفته است.
@Farsna</div>
<div class="tg-footer">👁️ 6.14K · <a href="https://t.me/farsna/467310" target="_blank">📅 16:44 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467309">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">🔴
انفجار در مسیر خودروی پلیس در زاهدان
🔹
دقایقی پیش یک بمب کنار جاده‌ای در مسیر حرکت یک دستگاه خودروی پلیس در چشمه زیارت زاهدان منفجر شد.
🔹
اخبار اولیه از جراحت چند نیروی پلیس در این حادثه حکایت دارد.
📝
اخبار تکمیلی متعاقبا منتشر میشود.
@Farsna</div>
<div class="tg-footer">👁️ 6.4K · <a href="https://t.me/farsna/467309" target="_blank">📅 16:42 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467308">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Gqr448du8Ll0E7aQApBo83cPlBh6bbKg9vCvTXqf7pS0swunF8LAKAt8DWQfUybREOQm5CoUwxG_qjR1PVmcdKVej-F3kitSVMSTrEYX-ECXtHTKeuoK0P22wRz68v22-zWOLp9lzJ3mwDLVmoJcoaKxchv7gtsYrJSrcwHoktkq1Km2RB56e4gztu-UMuUjjlRC842Mx5wtbMe3VahLeqHCBBcgf0UsrW361W22Fzhy2bUDumPHZdVDFmg-K52hthXD9QrD46xWILQze1GTNXdJ-dgo-ZNrtvpQ3_1IAUmmywlUUNzQPxP5GLd-O-GfP_kI1r7U09ze1J9kQ6jR3w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
گزارش حمله به یک کشتی در خلیج فارس
🔹
سازمان عملیات تجارت دریایی انگلیس (UKMTO) از وقوع یک حادثه‌ امنیتی برای یک کشتی در فاصله ۱۳ مایل دریایی غرب منطقه الجزیره امارات خبر داد.
🔹
این سازمان اعلام کرد که بر اساس گزارش‌های دریافتی از چند منبع، این شناور در حال عبور از مسیر خروجی، هدف اصابت یک پرتابه ناشناس قرار گرفته که در پی آن آتش‌سوزی رخ داده است.
🔹
به ادعای این نهاد، آتش‌سوزی مهار شده اما وضعیت خدمه، میزان خسارات وارده به شناور و پیامدهای احتمالی زیست‌محیطی این حادثه همچنان مشخص نیست.
@Farsna</div>
<div class="tg-footer">👁️ 6.13K · <a href="https://t.me/farsna/467308" target="_blank">📅 16:41 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467301">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/NgXFGHW13unDH2Dds_3CCf6kpvIKbwhnL5Q4DVbSQG_X90Ul_lkk6VTGlHFc5qllab42zIufZX2u-oJ4nFssUdf12TnGRJqc-U3dXatKfktbf9znWPlLReC93tUZPmIUDD67eLqBUidCFFDFSDkVCw3TCW5OQr0wBGLGJ4PYrltqFbuudXtLPVxlKywGykaIlJtHowNWh8GGluk2uT2FRGW4mUXqSpK_OXdpDo6w0sf5UXPo_BsE2Y-hYZDudnGib3mxXgxr-4jPC3i9zVl3SN9wiQwwTqM_5FCJapKA3-bIIRs4eq8UF6GEd_fzKoWyBy_h3ixodX_YF70YlEXzZw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qqTfc8-8w0CVynehHQzxr3yrQDEsYBXgFElD8uW9JDep2NumpQfdoUFcjO-mcrk1vyjx0UhQ22m6uqWksSF14mu4yPmOs_fS44R2cFbow-0aVD7Kzk28zBi6ZzxQ2HSBggOPGI4y7xIoWinm4LuPQg_b0wSPAx0SfSuI84N0JRVmVBTvLJZbnDaJW4ITEI4EwVXMOZMqeneLMr19NY4_ndJtYcBacdBAXoJjhlroVNSClsP9cQQ5vupB5K7jFHgpN9uTGZ1P4FBczrRIQTfpqg3q1DbxbMj9hGJFmcV_uUixgZbE8qdghzGoE8Inm4MYgXFcQaWcX859xv-yoMJo5g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/PrT4XrVecjBxbe1zu6Yu4RGh_RwpoeKpz6zUUt48ZwZTbLJP4MgzGAhHNtWrODvHPho35pDIYJQa15La1JTVpjg252aEAxfjtDbvX8IpdNgr2Z--j_WDtRnA86Y2XWQCEkfpGRkrYPMfvI9CTOrU6k18YEEOXzh_zx5FUdQyqw70xbVgIrHhgMGnTp7a6EePlZRCn-UrYYdpb92-kG1xnYMEnk5Xf0A3i3ZGzRFM1WVqaMGZjKNY6sTEw5PV5XQ7W7sclpk-hFSc2ggwfTAvOhwUJRTAlTrYgaZof8fBmic8-Gb-KIaUi8sNh0YoRjeIFLe4ZHe3e4F-CkLPEQIkKA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/lUuLR5Wdbdn4lOBAYKIRW_KYPUogB6xwHVnuQb-LakxQdN68yY2eKCkqKongiW91N6Yf8IqrN47Ywbep3ZG0KZdS96XMVyyyhiSTuHYiqLTwNxPBAw4qvm6S3yOcq2D6dwSkPLSn8-UOu5sGeDyAMKRc-FspS_Aw0zOxDADxf2JOPpj5WOGl_EalqMIC3mG6_S5f0yx1-KN4TepXfTLQQT86k0Y3IXArnZVNErHBxb2NqUlLH5vjN5Z0bO6UwpayGn0ypapDMMv8ioEnOXn-TN4AifhwzHtt63pMY14soWhQg5R7A3wM_fDx_c7houbkqADzhoj4ECEO3TX48yHqfg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/FXx-LY-tWppxxzWWCBnl-aRXoHGRl-Bvi5iG-SGLAMVPai_NRgiWbwYLiZdVvfFCvRyA7PgPktTNuJ9k1C_qWbgItxFlpfXm8uui3-GuZmU-M-waE2UtHSxjyN3tjg4vYmwp-4NODGJEOoBPiF7chyRwXavhSPVGdLrlKU3jUllcLtZKxiUQHybFrDTrriGmdSMGGBt_kw1IZ4FsYFRtWlHZyaHXwKO4V5g4wzwAww9nUKSqvgRGw1PExI-tuFztpMOrRhEYPJfTUQWGZJ-_AEgcjm7lPIv3OsHpQuPROy2Ygpa080HXXlBY7PNBOWiF6mH63kDVY-nyGxLAO3CJig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/oUx30wr8x-UeBBS_SHWHHXIRhRucVjZsb0F7KZuAwz_fWtjKA4hNfRkdgVlvKBvU9X_riZ1nZcpOAC0-_z_3ze-8QgBz3-EcDeGQ-P5u4ACw-soFRETPxd3I8hbSrwlTc9U1vWawNsDbUFoRn898sFOD6VeD5UGgbfn2QfPaY2EmBwWjgkm7NxzFm_LbOGWj_FC2ggIbpU6cOXceoN7BvtqMYRrkSWsrWXQkQbogObStsgBRew7Dv1ZLrwmESz2NUFrjGMtUqj5qdkcdHU2FlN23fSg4GZsRygSJsP7q6RUTfWpOkVsK-HNgi2Ok4f5JHDX2TE-ORKDbmuoNFSoU-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/kyUxNX_nodrV_jNaVWhqbQ56MVFguuJq-YnU--22Z23uU6xFjWUzpr6W9qEYkVHtWx09soNIvlLjBm-lrpWvbDZMppiyZEJhW4hE7-tAgpfVZFw9PFkX-CDVyZ2YdGeXhfk_cih32DSDkBwBVFoE-Fn8F6pQFgLWiEz6hlugcSNZcP26h9ZaoAaLv5M-GQUqLEnLYnindLPxl5r0ww-RKMAyOC5aDoX6PjJM0zRG7CiWAfoGM0N0e9bzOOokOYqGGwCrsLKiZPqagt2tOjdzhtJHcDeQdXPxYeQdBMETSTIqX7KsWH5lapJZLlDR2TW-6yZj4l6cFjVJyEzHUrlZAw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">‌ خطیب جمعهٔ تهران: تنگهٔ هرمز تا تحقق کامل شروط ایران باز نخواهد شد
🔹
حجت‌الاسلام والمسلمین حاج علی‌اکبری: ایران شروط هفت‌گانهٔ خود را اعلام کرده و پس از تحقق آن‌ها درباره اقدامات بعدی تصمیم خواهد گرفت. وی افزود تنگهٔ هرمز تا زمان تحقق شروط ایران باز نخواهد…</div>
<div class="tg-footer">👁️ 5.94K · <a href="https://t.me/farsna/467301" target="_blank">📅 16:34 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467300">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WmJm3wc9IXVAwYKhSVpea3k_GxrAOoWCfjsxsP3dxWXtpF0V3NNPccQye2PBhAq0Gfy4WxLHOVSkGY1k35HWPXQ8XQYFXgHI21L5SYlzW9oe7mTByKv5n1oLtd37JfgQYo8_HjRJrO1vXTOiS3VilgwYQ6W49Z4Xw7vo8HaNqCcJSjs5ZCmC_yjr5AfbI1Dq8eJd7nC62-coSGjx7wHurDdVVPbb_WeDGotj8p5TBCpu02ahitU-tgNtiQC8-RQdvWq1-DSSGZ19_IOEGUbJVkoWuElWdcKr16MV4c2CGebIVdYSwPL8cSfT6fmntJp1jVwWTqZVhoY4gldRvUS4_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
شرط یمن برای پروازهای فرودگاه ریاض
🔹
یحیی سریع سخنگوی نیروهای مسلح یمن امروز گفت فقط پروازهای بشردوستانه‌ای می‌تواند به فرودگاه ریاض صورت گیرد که مجوز پرواز را از مرکز هماهنگی عملیات بشردوستانه در صنعا دریافت کرده باشند.
@Farsna</div>
<div class="tg-footer">👁️ 6.09K · <a href="https://t.me/farsna/467300" target="_blank">📅 16:28 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467299">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pjQNRzHNRTTQZJV-yiyJx0wQfYSvuPi79Qv42bu2yPzPhPKbMggbrx8d6gNaidq8wbwl2gk7_zD4aPfIB7Sq1um0xPiKGllV-acIamKgrAqvn8-tueL6tn-wqgZJqhIBvXJvu6aEdWOzEEAV8yPUoXtpsPHbqHffAWk99fNm3UtHiKxSOgE512-3TOTmCraVvYO6PtYejOtb0kuEIv7zGNSxhYHcKzrc3sTzenneZ6bji2a2S37Kzxg2jE1MPCtwe87mQrSf1iV9IAGQ0q3ERJScO9YO7JkILaHALP8nDX0IJvSGh59QB7FaoxYGgAlYIU64BIXOD4P6X9BdHw3McQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
تصویر حکم تنفیذ دورهٔ اول ریاست‌جمهوری حضرت آیت‌الله شهید خامنه‌ای از سوی حضرت امام خمینی(ره)؛ ۱۷ مهر ۱۳۶۰
@Farsna</div>
<div class="tg-footer">👁️ 6.01K · <a href="https://t.me/farsna/467299" target="_blank">📅 16:26 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467298">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">🔴
وقوع چند انفجار در اربیل
🔹
منابع خبری امروز از شنیده شدن صدای چندین انفجار در اربیل خبر دادند.
🔹
هنوز علت انفجارها مشخص نیست.
@Farsna</div>
<div class="tg-footer">👁️ 6.18K · <a href="https://t.me/farsna/467298" target="_blank">📅 16:20 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467297">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CdTQ7T_gpt3a_yJ-A3B_ZY00vmYqVU4DXBLMnl4142O8yIT6YyFxUlZUJE-3BnIPjBJFw7IbP3Fjy5byMIWh1NlS1lO31-_4r0FuH2pLZHYnFoBs1S2jmS3l0lkQ5CppDV3nHsNlaGXouBkWUKFX2cmC50r2yvpGdC4wW1IEE1IdoT8rDDGNeNWaT54uLzWwHLH9QFg2gMyQunW4U-IQ-lTcUFA2LtZ0sXPc9KTmhpUUl0SMNHbJ0bou9H8ldLdQ6Te_U7GrGxb5jDucTn6bybDn2djrke_IbFKszloOwWy9IoJmm-ZrfVlH-WoqorUAOpOP1uqqfvIQfWQ9hOYiZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سپاه: کشتی غول پیکر حامل گاز ال پی جی مورد اصابت قرار گرفت و دچار آتش سوزی شد/ مسئولیت تنش افزایی در حمل و نقل دریایی منطقه بر عهده ارتش متجاوز آمریکاست
🔹
نیروی دریایی سپاه: ۲۲۰ شب حماسه حضور میلیونی و ایستادگی و پایمردی شما در دفاع از حق و عدالت دنیا را به شگفتی واداشته، ملت ها را به نقش آفرینی در اصلاح وضعیت جهان فرا می خواند و مهم‌ترین پشتوانه الهی و موجب دلگرمی رزمندگان اسلام است.
🔹
دریادلان نیروی دریایی سپاه در تحقق فرمانِ فرماندهی معظم کل قوا و خواست عموم مردم ایران مبنی بر اعمال حاکمیت بر تنگهٔ هرمز، اداره تنگه را در اختیار دارند و اجازهٔ حضور ارتش‌های متجاوز را در این منطقه نداده و نخواهند داد و با شیطنت‌های دشمن برای اخلال در این مدیریت با قاطعیت برخورد می‌نمایند.
🔹
در اجرای این ماموریت، ساعاتی پیش کشتی غول پیکر حامل گاز ال پی جی به نام اِن‌وی‌ سان‌شاین متعلق به شرکت نات‌ویت که قصد عبور از مسیر غیرقانونی جنوب تنگه هرمز را داشت مورد اصابت قرار گرفت و دچار آتش‌سوزی گسترده‌ در قسمت موتورخانه و سامانه رانش گردید.
نیروی دریایی سپاه اعلام می‌دارد:
🔸
همگان بدانند مسئولیت مستقیم این حوادث و تنش افزایی در حمل و نقل دریایی منطقه بر عهده ارتش متجاوز آمریکاست که با دخالت و فریب مدیریت شرکت‌های کشتیرانی و شرکت‌های بیمه گذار و پرداخت رشوه‌های کلان، مسبب چنین حوادثی می‌شود و با ادامه این مداخلات، حوادث تلخ روز به روز افزایش خواهد یافت.
🔸
شرکت‌هایی که فریب متجاوزان آمریکایی را بخورند، تحریم می‌شوند و اقدامات تنبیهی لازم در مورد کلیه شناورهای شرکت‌های متخلف اعمال خواهد شد.
🔸
من‌بعد برخورد با شناورهای متخلف محدود به تنگهٔ هرمز نخواهد بود و هر شناوری از معبر غیر مجاز عبور کند در سراسر منطقه تحت تعقیب قرار می‌گیرد و تنبیه آن قطعی خواهد بود.
@Farsna</div>
<div class="tg-footer">👁️ 7.91K · <a href="https://t.me/farsna/467297" target="_blank">📅 16:05 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467296">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mEJj1mLztdRrDuwAnw3XFt_IEZbO6A2DqPkCmhJlAvH0F3setNsMzbD5jbKdvxMvuuZ0wGzl9Ic4AEgfZiyIB8usvPvOBnznKRC_ncy3Ubi03rMxSaUZa8-qCHsy4idsOdjuTdEAHTqdjb4JpnSjNxmW36iMuHQKbRhhbmRqMTT8k0Thgq0f0oU7i0tbkE3--_3bq43QBQVzWwok-6kkz7iD9U5tlavKn9rciqmhrIvVwvZjGtxX3h5Rq53apodb1T9t7Z1kKTbqEB6lP_pRlHLuzcOq8recSnm7FrxoPB53I62_yt6wVL7WgWPd8HnOOYGMraJTpdI_WMlZK8MAEg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اردوغان: بدون محاکمهٔ عاملان نسل‌کشی در غزه، نمی‌توان از عدالت بین‌الملل سخن گفت
🔹
رئیس جمهور ترکیه: ساختاری که در آن اراده بیش از ۱۹۰ کشور عضو سازمان ملل متحد تابع تصمیم‌های پنج عضو دارای حق وتو باشد، نه عادلانه است و نه صحیح.
🔹
تا زمانی که عاملان نسل‌کشی در غزه پاسخگو نشوند، هیچ‌کس نمی‌تواند مدعی عادلانه بودن نظام بین‌الملل باشد.
🔹
توافق‌نامه‌های بین‌المللی کارایی خود را از دست داده‌اند و دیگر امکان اجرای احکام صادرشده از سوی دادگاه‌های بین‌المللی وجود ندارد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.4K · <a href="https://t.me/farsna/467296" target="_blank">📅 15:55 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467293">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/TWZHHVYHuVB29MtEuILDepyO7czObjZqoD-JCabNGHYK_FQBzQ-zl3Ps-mg671-Tudz1lxVKFNIU6X9Yd6h578CqgRHiKJp6P5s1pds-mdapdKk_YCvq1e0jqaH1DxgXpzQn5XsTbbRgaFduiIpXCbkzKgY7cRSP1GL93OcwoAVgDX7q-rZZJgWKIR2h_8YFJ4abVKvQMB1sOwJRqoNlHDA6Gn0K8J7ITLTeAs_jiGd1xO1l6R8vYabsRnaH9wbYJ7YGsaszCxJcINHSrK5_B_RDWKgl8fUXYFc5VZ9WIML82Rz1opmTHirulmBF3luRf5v6GIva5al1wCE4NM9fMw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/VVtaF8pQ9454yw2tNm0BKHNMK9jDGut9MIxn2QgvJ7usViQitOO0SykCExm9dqvJCBi_N6lEIoWHNYohfM_WF7H06uGJulrr4hkqmw8vXuOp3bvknMfmzoUX1CmNgS6-nGsjVXVPFqIbowb-tJ3ffvdwpN0tXiNB9Ii7jV1QiMEujh4F0byAse57Rh-ea2DhFj2LvINVZNPwwYxn7Rn2n6rcibZcYOvdLN3icR-N1xDMxe2jR-lUmjcvcC4dTk5H1YZtWdFSGPR2KIi6VIw0zxvAtfctA7yoAPZ48Y3-vti23oicurotFLe6wMdhoShLJepYwaAWk3Bes2d94eAE6A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/l2DYT_KjtI9YKWDxnMFwe25UBZxd9PRONhh8JF3AFskvC-v-KHt1eJeEOZ5rsZ9T4UQ2ZQgMXBmNKfP_9ETb4GPjl566yoTLJchwJCIiKkvpzCkhxIin9y9CpKnxkVdr3nioRe_vsabghqw4SaVW01Qg8m-PIXNrbc16u13dEoJzLTHh0s3iUpc1jza7o3kvBwv86I-vJBf4xuKrZ0NrT5LGYL4qdXzesnmctyqK1VPB9vVIb1ZZIqCH2xcHHwbVrXIimPAfqf6_IB_ZlIHYKYbhEXAggr9QwnpLfLsMfpgSaxwxgjeD4Sq7U-sinFWCEtPDueFTs_S9bjoiXAAf3g.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">پزشکیان به دبیرکل سازمان همکاری شانگهای: تاثیرپذیری از آمریکا و عدم استقلال در تصمیم‌گیری، منجر به از دست رفتن قدرت و انسجام شانگهای و بریکس خواهد شد.  @Farsna</div>
<div class="tg-footer">👁️ 7.1K · <a href="https://t.me/farsna/467293" target="_blank">📅 15:42 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467292">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eg2IW4ZNmCjoorOX-BpFIMpQ4ayD1MAWvuOvLzJS6mXnP4WZgaNbfeYKGweTBRrlaogWy4XzE8JhTMqacnZ1lHyai2SWGsrlxQaAlyHPwlUhsVuPtCDRzfiziPz7eq4y6qp4eEQSNqMiF7kKdjztjo8Te7nGL5l3JxRm4Wg_UcB3A78e4M55r6O6hpFvqiT60AfExjsag8xJS6eGIG3rJLUTGDsj3ssL8eSU8_l6FYT7FJwaMWzusCqXfICeorb_TRiLBGK-CodHLovrDVb9dg0Pvw0VS8BBW5XtrkldDOG2YcVy0H6KMzGjiOrZPImL4YKHtRE06g8yRdfTamyEOg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📷
دیدار پزشکیان و رئیس‌جمهور ترکمنستان  @Farsna</div>
<div class="tg-footer">👁️ 6.87K · <a href="https://t.me/farsna/467292" target="_blank">📅 15:40 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467291">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ddfnh4A1rwYSFAj5ZzsO2WbfM7dhDDYUHA1lDnyEWpigX_lxBepN4bkX8QSgg3JaHRs7A4z88a9Iu0GB0buDriBq1ceTgYIomrEi13WHzacoLuR2ocCOOX6Z_7_Bjb-vDBuqdA8sxHvzvikta5IHcC-nstizj33YGCJGebeZWRITlxs4_skUhku-fzfAQx4MCVJZCt6v7jFCU0TvWHrneK_HDt6VNLLTmBhkyGM07I9X7DXDR1XaXuTFK3ketl5mamg4mARYwiSg3AJj40s5mZ7JplJX6rfESP4y6aqJNhDc_h72dZBl2m5QxXDVatvjjVz9MvhJLjd95Z0oBDsTJA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هزینهٔ سنگین اعزام کشتی‌گیران به جهانی لاس‌وگاس
🔹
فدراسیون کشتی برای تیم‌های ملی کشتی آزاد و فرنگی کشورمان جهت حضور در رقابت‌های امیدهای جهان ۲۱ میلیارد تومان برای بلیت هواپیما هزینه کرده است.
🔹
علاوه براین فدراسیون باید برای ثبت‌نام در مسابقات و هتل نزدیک ۱۱۰ هزار دلار هم پرداخت کند. تیم کشتی فرنگی امروز در لاس‌وگاس مستقر شده و تیم آزاد نیز فردا راهی آمریکا خواهد شد.
🔹
فدراسیون کشتی توانسته با رایزنی تمامی ویزای تیم‌های اعزامی را بگیرد و حتی تنها مربی جامانده به دلیل نقص مدارک نیز با برطرف شدن مشکل، ویزایش صادر شده و با تیم آزاد به لاس‌وگاس خواهد رفت.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 6.93K · <a href="https://t.me/farsna/467291" target="_blank">📅 15:38 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467288">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vLD1QD3H9e63YEXtbemBqYPPal2_B04q7TFg0Y94gSIIiIPo7XObreg_XRwmjEOWJMZGvjWubw6Pyfe8ugjx2cgrvkR2nlBghbProt5nvwCD7_mfC43LTtEgiaGxerLrLsfrh8Ba3EJTamFieQm99R2mCStZ7XXOutNEY27eebFbjCh5Zm3IuF7G0M00f_ZimvegUuJLNeFT_IHcQTOMKJXsJcuymjZD5imvdNyDwGox2m_X8lByhOQcH4B5sy_FiR1qKtCdCsSsWQ303A8g9XJEh5Gr_kqUocx8zh9rrRZ_R4NgD-vT-7pvbczue7-eXBHHb5K9ID2LG9G_GujH0g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/DggUV5leLZsF4XZVz4UJx-Ajpxi5aFh4WXiujqpKz0r46toTzgmzZSe0vdGyc75dfxwUU47W9Tbsgq4FQdi6nB01uOFsuwr7kiKHjd5gVddo8FYxscmjttrjlC1gX9Vr-LWfJgrnxxHXOe74TvjLixtzzVbRUmxuy-jTb_0U3k6kltVWurQP3emMskdebuJ2SYAVpX5tnXsTWR47VoStH6hMnpyzMwiDOhZgopbM2Y0Tzv_MMjquTEn8z_L-534jKh-dWxvPX1f-707KF6wjbGEFDo2QUPZBCqj2jhdvTrDZyqth7bgYSZjVQPalInD477Q69BnjFHTmwfLV7RGcDQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/EOZFIunmz7RFWUd9GGdrCkRBPj7Dw57Q0PRL3kMGHHr426C8RfhsoHpbbUiL-xCtXDE87kUO0GjW3FgdNBp-xQa2eS9JKkYL0v53trcH0XB86CemXhPhqIEBp0PMLwut0buNM4cDGuebfahAo3uOuSCdY7VRz7P01v0ayNCPaPa7WxSBNL-EjMQ6JN59Tk3Mwd4M5Lelhy7EbclNiNBEUG54sXM9MyXPEw4jbIKktkemhBhD6wkHVy5cIdUk-4_lBenOeL3QiNa42Dvlnjwl8fwejxxo6UH6ddW6jYabAklShfayi3IpjDqXL-qnIlo7uSgHQahEpI4nbNenTDA1pQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🎥
در نشست سران کشورهای مشترک‌المنافع چه گذشت؟  @Farsna</div>
<div class="tg-footer">👁️ 7.23K · <a href="https://t.me/farsna/467288" target="_blank">📅 15:32 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467287">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/S2HUCKq0UAx9mmrFPFYGjFKkeVEgj_5z1Y0P5nlwdsgf_3MbBrtvsT1kvsodxFfj6vOIuOadLMKNkuhjzEXx5idAGTRc69aU25hn9RJGAP0rCc1RemD1cQ0nqWKVvZL0FEHK5Aw7iXntjFbJlQGiZzYdrmbq-P8PJIiad2wUZJKM7NIpwlceHi3uruwYozPSY1wUxWQF2tS6OT76v2BGsYGqDMJ6dsvkFmdj9jWzZIm5JAdnI27woFizZYqeQ23f8dwkWA6TqmOubWKPiPEU66QUovKeqJZQ0evQ8LKH58oZtkFiTrBDu2pH_MUZTt3IOaYsYxPojx9Wii9xY7htpA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">برنامۀ تلویزیونی «ثریا» فعلا پخش نمی‌شود
🔹
برنامۀ تلویزیونی «ثریا» که با اجرای محسن مقصودی تا امروز به صورت زنده پخش می‌شد،‌ در صفحه مجازی خود اعلام کرد که امشب روی آنتن نخواهد رفت. و تا اطلاع ثانوی پخش زنده نخواهد داشت.
🔹
صفحۀ مجازی این برنامه نوشت: «امیدواریم…</div>
<div class="tg-footer">👁️ 7.21K · <a href="https://t.me/farsna/467287" target="_blank">📅 15:23 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467286">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f99ad6ee08.mp4?token=eanXURcB7Xd8ZJnGY78plZ6NCjlsN_dHAVvontUQn5P63do87yrl-BlpfG-lbbDu6OlJnEa9xqpw-snK_3MnnJBiplsDWk39iBiv0gfaKwBLLr4uHWE3dRi2PBCyaCBsLEudIy3wEyZemQ4DA4FwHAkdrnE_3reWfm2w2VsAABSlU9ZTE2bnNAYUOekyatrfRbYG4pm6LpHO-iXnla_FV3VINx8y506snHVp-fXSqp9DupmeE9NdhBOLAbiv2xaZLCG8Lih18U-VWlTkQSk5GrMTAe1g4pGrQ7UX-XWeBDqRraBtvkO1TTAU4thayv1hJq-Ubx-CmBQ0zy5c3xxRkQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f99ad6ee08.mp4?token=eanXURcB7Xd8ZJnGY78plZ6NCjlsN_dHAVvontUQn5P63do87yrl-BlpfG-lbbDu6OlJnEa9xqpw-snK_3MnnJBiplsDWk39iBiv0gfaKwBLLr4uHWE3dRi2PBCyaCBsLEudIy3wEyZemQ4DA4FwHAkdrnE_3reWfm2w2VsAABSlU9ZTE2bnNAYUOekyatrfRbYG4pm6LpHO-iXnla_FV3VINx8y506snHVp-fXSqp9DupmeE9NdhBOLAbiv2xaZLCG8Lih18U-VWlTkQSk5GrMTAe1g4pGrQ7UX-XWeBDqRraBtvkO1TTAU4thayv1hJq-Ubx-CmBQ0zy5c3xxRkQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
ادای احترام نظامی به فرزندان شهدای فراجا؛ قاب ماندگار یک جشن کودکانه
🔸
در مراسم روز ملی کودک و هم‌زمان با هفتهٔ نیروی انتظامی در باغ کتاب تهران، حاضران به احترام ۳ فرزند ۲ تن شهیدان احمد حرآبادی و جواد انصاری، از شهدای نیروی انتظامی در جنگ با آمریکا، احترام نظامی گذاشتند.
@Farsna</div>
<div class="tg-footer">👁️ 7.92K · <a href="https://t.me/farsna/467286" target="_blank">📅 15:13 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467285">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d3defd3519.mp4?token=tKVYQfOP-Gv1qflPyqLW__AbVzxHkkuFMCT2G8ocK1BU5NYXoVI8HaE0izJO323DW_05PdN04NDNt0t0qXlp67Pry20MYujXBQkbd7PwUw3_7M1ym0Xufk4Rfz9vYQTtXlRGB5HS7buRtcQLf7bjH3RoVBXvHGuLLAEMjoLc2cof4yhzhg_IT0mNP2UJD8wZp3KC5OjW3zj-DRkb4FilBOg8SZ_U8nNWtd-xuzmqt3B5eofoWsN-BZr1lPWDrkan1t38oZoTdNLSMUhLOsDRgUkKkWIQ6z2VQ1M14YE8xgBZO2AI0MzfQyvyaSNkbp4-Lbgs2UQwa5fsPUwsifoKSA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d3defd3519.mp4?token=tKVYQfOP-Gv1qflPyqLW__AbVzxHkkuFMCT2G8ocK1BU5NYXoVI8HaE0izJO323DW_05PdN04NDNt0t0qXlp67Pry20MYujXBQkbd7PwUw3_7M1ym0Xufk4Rfz9vYQTtXlRGB5HS7buRtcQLf7bjH3RoVBXvHGuLLAEMjoLc2cof4yhzhg_IT0mNP2UJD8wZp3KC5OjW3zj-DRkb4FilBOg8SZ_U8nNWtd-xuzmqt3B5eofoWsN-BZr1lPWDrkan1t38oZoTdNLSMUhLOsDRgUkKkWIQ6z2VQ1M14YE8xgBZO2AI0MzfQyvyaSNkbp4-Lbgs2UQwa5fsPUwsifoKSA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
کاروان دوچرخه‌سواران ترکیه‌ای «مقاومت شهدای میناب» وارد ایران شد  @Farsna - Link</div>
<div class="tg-footer">👁️ 8.65K · <a href="https://t.me/farsna/467285" target="_blank">📅 15:00 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467284">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/264f5e51d8.mp4?token=q4SC8_qYypoMP2J-7J_n18D0FW3F0hExP4Fk6yZcj1CiSmUdM7XhWo3TvWgfrZGkPVDvn3erLEb3XLLVrJLcoxSlgPTZGsfDql7poOQ2iQmUeVVjCvnlJbLPVPqhXtqzJYTsT6G6z0kfJQw8cwe7icag1gbi-OMYYPaiPMX1maitdvXNxKnPtd9cb7BTcitFcX4TeTacehfU3u0akHmp1yAX6H1ooiT5Fwjy5z2dFlsaJicXIJ9Xqxwo8A7RA1oAGcRbl4RcZ3E2tz562GPVFM1SBUuCFnQ2JxubXXVQGuXoNqAQ0KV-r1E3fzNuNHmXsgJRXRtnpDcdxVmgL8UScg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/264f5e51d8.mp4?token=q4SC8_qYypoMP2J-7J_n18D0FW3F0hExP4Fk6yZcj1CiSmUdM7XhWo3TvWgfrZGkPVDvn3erLEb3XLLVrJLcoxSlgPTZGsfDql7poOQ2iQmUeVVjCvnlJbLPVPqhXtqzJYTsT6G6z0kfJQw8cwe7icag1gbi-OMYYPaiPMX1maitdvXNxKnPtd9cb7BTcitFcX4TeTacehfU3u0akHmp1yAX6H1ooiT5Fwjy5z2dFlsaJicXIJ9Xqxwo8A7RA1oAGcRbl4RcZ3E2tz562GPVFM1SBUuCFnQ2JxubXXVQGuXoNqAQ0KV-r1E3fzNuNHmXsgJRXRtnpDcdxVmgL8UScg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">چراغ سبز دولت به ارزانی سیب زمینی
🔹
معاون توسعه بازرگانی وزارت جهاد اعلام کرد: صادرات سیب‌زمینی تا پایان سال ممنوع است.
🔹
قیمت سیب زمینی به کیلویی ۱۰۰ هزار تومان رسیده بود یعنی نسبت به قیمت یک‌ماه اخیر ۳ برابر شده بود، فاصلهٔ بین تولید مناطق گرم و سرد عاملی…</div>
<div class="tg-footer">👁️ 8.99K · <a href="https://t.me/farsna/467284" target="_blank">📅 14:52 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467283">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d1423c4aa4.mp4?token=fOxQRzISaWooG7UNjd8menUH6ZCricSxnaoWAF2lXsmDNL6mkL4RSVziDcbZLOsp2SwRymf83FdzJ_wMfd5rwbnWkYsT19jlmP9t0Z3TyDuctjrlRrwOnOniw-kMsh7oQy2vv1CDuHFS9EaKdysnEZNA8YCu1-yLoxpWnxuexpoX2Yfs5J4hqUfhuhpdCnGGmH7XACLIQZ0kxHV1V8G4HN5TW2VlmEDIM7mkebNxC1hfeINRWCuKJkAKOnQ2o0SSLuAVNv7FuWM1aWQgCxRrAuk1OaWeyxOdhWuDckCzwiVRgwjlSP8snBFohKXGsIIpJoKDv1_0Nhdd8hnljAR6hweCrjWO6ebAFYF0bw3U4RJt5wlhRjyrtfNybcpVcnKZGJP7-9FMNr5RYkEVcORO7e6vxieTnU6UUkshKlOblpcr0BCBm9eyWWdu9x0eJKuh_D-bZlb7TWvgCI1PgvPiSqtPde5apUpuqAtMJeeq2m0Z9FgjWi0T6DwQVUj9EcG7V0Nwlk1lGl1AynPNO5XaJzXaPl37fgK9lmAUSqb9UrhAVDD_vQWy4KG5Sin8tHjDrA1WTP73Uv-q_IqLz7w7tQ-jo5k7YDoeuMxWiUmwlm8mnk-hz9jlWfLbx-BoTPm2t0v64aCTgZGSqLEsMImuEVME9Gz98mlblnC6iWOKum0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d1423c4aa4.mp4?token=fOxQRzISaWooG7UNjd8menUH6ZCricSxnaoWAF2lXsmDNL6mkL4RSVziDcbZLOsp2SwRymf83FdzJ_wMfd5rwbnWkYsT19jlmP9t0Z3TyDuctjrlRrwOnOniw-kMsh7oQy2vv1CDuHFS9EaKdysnEZNA8YCu1-yLoxpWnxuexpoX2Yfs5J4hqUfhuhpdCnGGmH7XACLIQZ0kxHV1V8G4HN5TW2VlmEDIM7mkebNxC1hfeINRWCuKJkAKOnQ2o0SSLuAVNv7FuWM1aWQgCxRrAuk1OaWeyxOdhWuDckCzwiVRgwjlSP8snBFohKXGsIIpJoKDv1_0Nhdd8hnljAR6hweCrjWO6ebAFYF0bw3U4RJt5wlhRjyrtfNybcpVcnKZGJP7-9FMNr5RYkEVcORO7e6vxieTnU6UUkshKlOblpcr0BCBm9eyWWdu9x0eJKuh_D-bZlb7TWvgCI1PgvPiSqtPde5apUpuqAtMJeeq2m0Z9FgjWi0T6DwQVUj9EcG7V0Nwlk1lGl1AynPNO5XaJzXaPl37fgK9lmAUSqb9UrhAVDD_vQWy4KG5Sin8tHjDrA1WTP73Uv-q_IqLz7w7tQ-jo5k7YDoeuMxWiUmwlm8mnk-hz9jlWfLbx-BoTPm2t0v64aCTgZGSqLEsMImuEVME9Gz98mlblnC6iWOKum0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
آمریکا به خیال شکار آمد، اما خودش پرپر شد
@Farsna</div>
<div class="tg-footer">👁️ 8.54K · <a href="https://t.me/farsna/467283" target="_blank">📅 14:49 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467282">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">جنجال واگذاری اراضی چابهار به افغانستان؛ اصل ماجرا چیست؟
🔹
اظهارات اخیر محسن زنگنه، نمایندهٔ مجلس و رئیس کمیسیون ویژه اصل ۴۴، دربارهٔ واگذاری اراضی چابهار به افغانستان، با واژه‌ای همراه شد که موجی از نگرانی و انتقاد را در فضای عمومی ایران برانگیخت.
🔹
او در…</div>
<div class="tg-footer">👁️ 8.41K · <a href="https://t.me/farsna/467282" target="_blank">📅 14:44 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467281">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6a8b0e0034.mp4?token=ILrIQ-8IKGXPXWsjf0xQBWXXZ36Y0VvIwjgA_FiIwa9V0u5J4dViy1xN957FdnM5GV-bN-sh263wl--UiJcbuTa5nGPbnP6Z93vTnQ1ntuCqWd8ej9I-fv6r1ymaeoprNKzKH026nahxP2n_IY9yutohVeFXYAqdaR_RlH9V5Mp8UhlUSlePFvMEL2l7ZwN8jSO5tS2Ika7T8Qgizn7187TgZW5T10pj2blQH65cq0n4Ap2FoONsPXMArKHjZ-KhxSukAwSeIwxB3E9h0pqQjG2ZNYgwZodBHBfuzHE3tDwRwMy_3O32b_w4eYhvTaXZ3VbDN0Fm0kxUCAfvcYI3MIi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6a8b0e0034.mp4?token=ILrIQ-8IKGXPXWsjf0xQBWXXZ36Y0VvIwjgA_FiIwa9V0u5J4dViy1xN957FdnM5GV-bN-sh263wl--UiJcbuTa5nGPbnP6Z93vTnQ1ntuCqWd8ej9I-fv6r1ymaeoprNKzKH026nahxP2n_IY9yutohVeFXYAqdaR_RlH9V5Mp8UhlUSlePFvMEL2l7ZwN8jSO5tS2Ika7T8Qgizn7187TgZW5T10pj2blQH65cq0n4Ap2FoONsPXMArKHjZ-KhxSukAwSeIwxB3E9h0pqQjG2ZNYgwZodBHBfuzHE3tDwRwMy_3O32b_w4eYhvTaXZ3VbDN0Fm0kxUCAfvcYI3MIi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
پزشکیان: گفتگو زمانی کاربرد دارد که در سایهٔ زور نباشد  @Farsna</div>
<div class="tg-footer">👁️ 8.13K · <a href="https://t.me/farsna/467281" target="_blank">📅 14:34 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467280">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">🔴
هشدار امنیتی آمریکا در اردن
🔹
سفارت آمریکا در امان، پایتخت اردن، از شهروندان آمریکایی حاضر در خاورمیانه خواست با توجه به «شرایط پیچیده امنیتی منطقه»، هوشیاری بیشتری به خرج دهند و آگاه باشند که احتمال لغو پروازها، بسته‌شدن حریم‌های هوایی و اختلال در سفرها…</div>
<div class="tg-footer">👁️ 8.49K · <a href="https://t.me/farsna/467280" target="_blank">📅 14:24 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467274">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jhql3kbOpeKuWkQ03tBgAwhuiDNR0zoUL7jWWua_BWdrbusZk2FYgzQKzrB6iC7RcILJ3elTbRw_v4C9ayB621VOlovUgXaXp8A4I793_GU0r60pmAbib3li9IgIK1n0PuCQFxabq6-KLanbYzN0n8ZTD-Y2_a3H7VZD5Mxe6qdmMlCIcqRn2L5ixB077-1UwfL8VxEatz-urNindE-KwNGGAVrv2laOU7gYXBcqgG6-OAuEbV3fLjUXO3FnzTa1hwsj0kA6e8yTUZ5RzvCAKgxUrTcMNNmkk9DgC6zPQvDebM-8tAAQ9F7DEWCO7MY3WGLeINp5fDSuJreUxBB9Uw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/cdR-M3zQLMJO-b75o3Iouq23RlRuI_ckGYy89hLYEHeDttsExEydVhgMyNemwyWYEVpND3XixYsRehe3O5I1Zbl5ZqYN4A6dmqfm3jHgP2kflm8IYdwWw8uWvZs_bUmSkqUDcxBPfNF0GJvkCIZFisvwhT33vho1SNtJpZmCIV3obdoUceNtr-xxbbckVRA0PJz3Pn0EpAMQVaFdH6Ehi7CW5svX-ox4SdOcwgR2iGyit2kwFWZNYxGLoGPcxHlvFzxavwQl61YcAtqIywXpWACNBT0eLylXKYI6ksq2e2x2XxA7NGdrsODa3VILVIxMEiyYwqGz_I8F87TMbPkD5A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/U9FUtB5pNpduH2xqO8X5G_rzI0yYqn3ukbVtjWdfRmnICBJGJ_AoQTI3w--8zyk7c-3xkp4IpkEiR12HY_HydUbfg1A6eph7R8N8s_a6KBv7h12Y2Xp_3cxS5MgFYkg3ls7j5jrOHHDR4D_2OjbJ13z1U1a5IzXOJToALORfi2oT59LxarA2MmhgMgq1n-N7ZUBJrmRazinaG59tHL0gU63kIdMnnZ__CQDZ_tGQXqP0EQQ4Dy_qH3Rx9wqqSfzXt5zv-ZkTgvTmpdVQFwNCDerB_5dcS5CN6_8Qpvv4CYMWMxl5PTQgAwvABLuOGr8DtTNxaes9IA6j4BuyDk-KSQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/e_NuXAETkLd31PrnEuLc15mQ3L0BB9v2vPkg55RsOvb8GPPSR4YmsdoeKOQmvNBZYiZzYV-nZbW4fcU7J5CoAF7MXJxguMG2Gj0fjsIeOW4siVU7hKCt38zwjie-0vsG4YoYP_k52-jNc0AGmWqzP9XVaEDVqlIZaxoQ6zEFbQJHXjm63B-pjKiCTu1jzpe-7-LuTTkZ9U2vKzNR2ip0vIzzmGvfVEYQh4JY3wIO5pXsM7yaGb0XVOAMfw2xfdy-9NV1pUbfr3tK6jSshUGWKUOav-UffaUXs8zfkzZsuTN-_F4uuhBtpF606VKbyH7FjXE_d1ZS6nLhzWfsZHHu_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/FCrNtCdrmSAIO8PyVNl8ew88pQ-i9u-eNsQkuZLPWDvFTZw13X4fYA3vdX5Zl8CDdyvAKf07BHPT3ibGnj0EXCn2oNP5Y05GQIr2o3c19TYf2geJSjNYEFiuoGON-DnpgF5eegbXd2ENp-nS7Q1rp2Jkr8o5sDACBcW6GOYnntbvuarwPLEIcKJpRgSYUCnHHjXzJU4xubMv1yoGUoP4lTB31RMJBdtEWBerBAVa9YXUUH6nnRK3F2Go-54807CiZEKD-XR37ByAd8AvjdPnM-dBbW9bG2hTvYRBJtW9uALTekryRiuhOGpD9yh-Bhfs1DPcNeJi2pvWg49YEVlR5g.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🎥
پزشکیان: گفتگو زمانی کاربرد دارد که در سایهٔ زور نباشد  @Farsna</div>
<div class="tg-footer">👁️ 8.15K · <a href="https://t.me/farsna/467274" target="_blank">📅 14:20 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467273">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/64b1af67f1.mp4?token=Pjgr1AM4MApx7av94BOLn4zjng3Ztlg-ncfwo_70WPfKpFc8MU_z1ndG3vjLT_CUvGmvRJx15LB5FGmFITU8pij9VqkdEwv-4r4BoG_kgkrphQBN84P84O6KAU9JdK53tVoKVMt_FMIDgO48icmINmPQ-2d6lsKbHkYel-FOVKr_CjykrAQ617blG8Cys9ArljXJvDDQzj5g_szYt-lRjie24EJfhWnj3VgpX79V8xUsLD-VI3AH0C1Ct4TXaX2XEL5BlDkn2Qk-K2zmcceG3u7haqQZ_0h97TKSkwZR4aZg9ISvTcczTiTo6VbdXGgiCUeQVC93SsFiApwaB9Z4Ew" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/64b1af67f1.mp4?token=Pjgr1AM4MApx7av94BOLn4zjng3Ztlg-ncfwo_70WPfKpFc8MU_z1ndG3vjLT_CUvGmvRJx15LB5FGmFITU8pij9VqkdEwv-4r4BoG_kgkrphQBN84P84O6KAU9JdK53tVoKVMt_FMIDgO48icmINmPQ-2d6lsKbHkYel-FOVKr_CjykrAQ617blG8Cys9ArljXJvDDQzj5g_szYt-lRjie24EJfhWnj3VgpX79V8xUsLD-VI3AH0C1Ct4TXaX2XEL5BlDkn2Qk-K2zmcceG3u7haqQZ_0h97TKSkwZR4aZg9ISvTcczTiTo6VbdXGgiCUeQVC93SsFiApwaB9Z4Ew" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
پزشکیان: حضور ایران در نشست سران کشورهای مستقل مشترک‌المنافع فرصتی برای گشودن فصل جدید همکاری‌هاست  @Farsna</div>
<div class="tg-footer">👁️ 7.09K · <a href="https://t.me/farsna/467273" target="_blank">📅 14:17 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467272">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5dcfef82ee.mp4?token=ue0DfEfEy8dW1Py0_u3K2d_adCzsMjj8weNzVRSeMuu-989iRCu15GSnAc6UHaT_i0COBYAqZf7LK5R4_aq36DIUbwpM1fNT7iwqhA41OTEKEKNV-yyO6y9vxa2V7f2mwmh6xjh6fCbV3ZICQ4CKpFUhj_KOpIMSfrn2x_yFvCBhqbFZhx3cq6lev_uNmNp02mZcCkdiKtcVym0vlqqInBuiTXZivV0gswrlAXrhm5elqEzJqIYtu_OUFTHEHCwDL2Hrpaps1hjTGIGh8RZnQAYAf3JOMjdS-W-E9OVhhfgHciGE1WMgLgM_eD5vd_CE3vZwWA1DsY2FTOHkuoIUEw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5dcfef82ee.mp4?token=ue0DfEfEy8dW1Py0_u3K2d_adCzsMjj8weNzVRSeMuu-989iRCu15GSnAc6UHaT_i0COBYAqZf7LK5R4_aq36DIUbwpM1fNT7iwqhA41OTEKEKNV-yyO6y9vxa2V7f2mwmh6xjh6fCbV3ZICQ4CKpFUhj_KOpIMSfrn2x_yFvCBhqbFZhx3cq6lev_uNmNp02mZcCkdiKtcVym0vlqqInBuiTXZivV0gswrlAXrhm5elqEzJqIYtu_OUFTHEHCwDL2Hrpaps1hjTGIGh8RZnQAYAf3JOMjdS-W-E9OVhhfgHciGE1WMgLgM_eD5vd_CE3vZwWA1DsY2FTOHkuoIUEw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📷
دیدار دبیرکل سازمان همکاری‌های شانگهای با پزشکیان  @Farsna</div>
<div class="tg-footer">👁️ 7.13K · <a href="https://t.me/farsna/467272" target="_blank">📅 14:12 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467271">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rZP7gSs9g5G7NHgzWA-hZR-bJrQNOFRuYrENHgDURIIIEFc7WM9hN9uuoAdJTx-LLPfJXJixSo9slKCmFKJXn9-RFMJwFSbD6WX1eDGFhhI6g_agvso19ng15HmNKIHLobPzUg4h2vng_nFOzdLYp3Si4vfJBhvg7mrPNDc85n73_9cZW2QXRgOX0ManDHcXYqns0k0qCryNybKmtnZQevmI3gRKtPe2CifJr2m9ElKZqqw5DYzjHh0mhTn_sQy-ZKnlvnS9BWfJ0-63EVsdhFnlcyincVDHBoeC5TmxSpc9Dz4_f9JbWVjUqLjQXrdczewcXx2PnsesGrR04pOdUQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ماجرای ناگفتهٔ اخراج پژوهشگران در اپن‌ای‌آی
🔹
انگجت: ۳ پژوهشگر حوزهٔ ایمنی هوش مصنوعی که به‌تازگی از اپن‌ای‌آی اخراج شده‌اند، در نامه‌ای سرگشاده به تصمیم این شرکت اعتراض کردند و هشدار دادند نحوهٔ برخورد با اخراج آن‌ها ممکن است دیگر کارکنان را از بیان نگرانی‌های ایمنی و همکاری با کارشناسان مستقل بترساند.
🔹
جاسمین وانگ، میکیتا بالِسنی و تومک کورباک در این نامه اعلام کردند که پیش‌تر می‌توانستند آزادانه دربارهٔ خطرات هوش مصنوعی بحث کنند و با سازمان‌های مستقل ایمنی همکاری داشته باشند.
🔹
به گفته آن‌ها، اخراج ناگهانی‌شان این نگرانی را ایجاد کرده که قواعد همکاری در اپن‌ای‌آی تغییر کرده و کارکنان دیگر نمی‌دانند چه رفتاری ممکن است به اخراج منجر شود.
🔹
این ۳ پژوهشگر همچنین اتهام نقض رویه‌های مربوط به اطلاعات محرمانه را رد کردند و گفتند ارتباطاتشان با کارشناسان بیرونی در چارچوب مسئولیت‌های کاری و با اطلاع مدیران ارشد انجام شده است.
🔹
آن‌ها همچنین هرگونه نقش داشتن در افشای اطلاعات مربوط به معماری مدل‌های جدید اپن‌ای‌آی را انکار کردند.
🔹
پژوهشگران در پایان نامه خواستار تقویت نظارت مستقل بر مدل‌های پیشرفته هوش مصنوعی، حفظ امکان ارزیابی رفتار این مدل‌ها و حمایت از گفت‌وگوی شفاف میان پژوهشگران داخلی و متخصصان بیرونی شدند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.13K · <a href="https://t.me/farsna/467271" target="_blank">📅 14:04 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467270">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/df44a64bc6.mp4?token=nyp_rIw426TL1AT2CK-I-TEMzd_HrBtTSTOZUPrfcWl1kfL4aknPL3VWxK9ZzatlIZgnc5q5gxKEvW-2dG8cHqPYafw0rlUaU_moXjdKUJ5kGQ44W8HQnzfcRAcjXFOf2JiCGGhlzWWazMc5KWYMf-WPAHDP4w6gbPoOZr1lxrBRFRV8cT0An2Ey96-AC5lxcmgsZYy-kdNcyFM1C-DVcfGQK6-AMdIgpVpGrUX37stHhgCKShKt-OBp0GEDcC4z2-PEerhj4CzHAPB71BwV9G-VQOjAgmTPoo7CHTxEG0lOpo9lxNbbMOV-Kr9b9aZi9MC9IR2hm6Qp_TcTIFeXuw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/df44a64bc6.mp4?token=nyp_rIw426TL1AT2CK-I-TEMzd_HrBtTSTOZUPrfcWl1kfL4aknPL3VWxK9ZzatlIZgnc5q5gxKEvW-2dG8cHqPYafw0rlUaU_moXjdKUJ5kGQ44W8HQnzfcRAcjXFOf2JiCGGhlzWWazMc5KWYMf-WPAHDP4w6gbPoOZr1lxrBRFRV8cT0An2Ey96-AC5lxcmgsZYy-kdNcyFM1C-DVcfGQK6-AMdIgpVpGrUX37stHhgCKShKt-OBp0GEDcC4z2-PEerhj4CzHAPB71BwV9G-VQOjAgmTPoo7CHTxEG0lOpo9lxNbbMOV-Kr9b9aZi9MC9IR2hm6Qp_TcTIFeXuw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📺
«رخصت»؛ صبح رو با یه یاعلی و رسم پهلوونی شروع کنیم!
🔹
برنامه صبحگاهی «رخصت» با محوریت ورزش زورخانه‌ای و فرهنگ پهلوانی از راه رسید؛ برنامه‌ای پرانرژی که قراره صبح‌هامون رو با ورزش، نشاط و آمادگی جسمانی آغاز کنیم.
🔹
«رخصت» فقط برای تماشا کردن نیست! شما هم به گود رخصت بیاین تا با هم ورزش کنیم و روزمون رو پرانرژی شروع کنیم.
🗓
از شنبه ۱۸ مهرماه
⏰
هر روز ساعت ۷ صبح
📺
از شبکه افق</div>
<div class="tg-footer">👁️ 6.48K · <a href="https://t.me/farsna/467270" target="_blank">📅 14:01 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467269">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromبیمه البرز</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Lo1v6okFfLZJahLSIyGXxlCF46woDHgfSGlMriCVAen4UfMZtPRP4JDg_aEotbxiIUX-J82qhjCrx7cfjjqh8fsHGQ_cqS5rRf6JHo8nPnjG2pVBoiVnjnC2vZRy3PWNG0OPYOuPTgNVqFGSkgPmtPq2K951YuDoZFK8qel2eK3FFH8CuJujC30gfOptsDWyw_HP-5iYFcq_02r_ybaLP20Qsfq8r_i236F_0G65hfgtIbwy8Sj4vJRwSGp7RXC7xl_shL1C95sXjfOsniDz5KjFPpl7U2HHOSvRWo2U4TB_YDJ4BatfuYNhpG5b-LBm6Tn3Aoh0PHxIrJ1iKhQaxg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رونمایی
#بیمه_البرز
از نخستین برات الکترونیک در صنعت بیمه
در گردهمایی مدیران و رؤسای شعب بیمه البرز، از نخستین برات الکترونیک صنعت بیمه به همت بیمه البرز و بانک تجارت رونمایی شد.
مشروح خبر:
https://www.alborzinsurance.ir/PublicBlogDetail/5111</div>
<div class="tg-footer">👁️ 6.41K · <a href="https://t.me/farsna/467269" target="_blank">📅 14:00 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467268">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-footer">👁️ 6.44K · <a href="https://t.me/farsna/467268" target="_blank">📅 13:59 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467267">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">لوفت‌هانزا و پاکستان پروازهای ریاض را لغو کردند
🔹
با انفجارهای روز گذشته در ریاض و توقف موقت فعالیت فرودگاه بین‌المللی این شهر، شرکت‌های هواپیمایی لوفت‌هانزا و پاکستان از تعلیق پروازهای خود به عربستان خبر دادند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.41K · <a href="https://t.me/farsna/467267" target="_blank">📅 13:51 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467266">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/K9e6jJsBtONQUcm3QfXhTazLXib8NvdoUzDyrC_az3NGl6cPMOUoUadxz0EFH24iRwv1Q13hKJ54bI4d0DIB4jQVe_lwI-bVPKSn_GGmnjR3-asp_eri9_47IA9MA5hTrC4F1Y2QMIuwK2Y-vArKmyrtPX5-jfSQiYCZmyJsrJkADBAwa7-eQnjkZtPyqUZZtuVbb5HwOabYppJhmbb7tUJ1_vUxOR_OTP6N8ZjG0Wg_dJ-LQ9kiNytwPu8qAM0s6MPKW-fdkPFyDdmU92Kv_SrOtyLY97YanaKR-zMLEuXpVEAF-7w9Ibqok5EbW8ysAQdUFmB_I9mGhtiGJjX6Yw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حاج علی‌اکبری: صیانت از خانواده به یک نهضت ملی فراگیر نیاز دارد
🔹
خطیب جمعهٔ تهران: امروز جامعه ما برای حفاظت از خانواده و تقویت بنیان آن به یک نهضت ملی فراگیر نیاز دارد و مراقبت از سلامت روابط زن و مرد در جامعه باید به‌عنوان یکی از راهبردهای اصلی در این مسیر…</div>
<div class="tg-footer">👁️ 8.59K · <a href="https://t.me/farsna/467266" target="_blank">📅 13:42 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467261">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/pfpUFtoBoRruZE5dkb3XTh7Hx3uLGZJIzN4qDmTpN5QfDfm1DfJ4Sy_RN0ZmUhF0_zyUbHa_SIIxjfOngyj9PNhhRyPX51Awjya0iuD0fr85_2AVZ63YZxCI5Gklg_ADyb4m9mTXrI_ygqKfz6CpNvWeEu1WPrwEUtsJhZCF0RaIVxF0KIAuc9miRqUK5JOpdV3qLKpgKnm6mVAiFFGyVVHbewVQr_Kv99Oiq571v6N3HXFqDKIYdbkVsLl7zXkAjgPXhtU9l8Ko4p6TsSxSgKIbgIc9X4lYC-QjeUTZq5Z-kisEgW2o6QbyrbpoDM-Vr9ENCILNtoAHjlYbXCU90w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/G7IGNNESyVatHRNetYFgjKaRHLUH_JdYoeMiCxmKxSe8s2W5_tLWL9Nbrnn6y9vSoIQMWfN_EuTyJ_UBqHD5YYVxM7BVC3on_sYSQvpnvgZyv3FE0arSjjtkmCZWxl1ad2ekpS7XQ12yTcByH2t3QFFMd1zCnt5kgS-BMUBuPHUK3YRL2XreF7jn4lNWzZGFvBgfUu-CB9syXS_e9a_h46OjSx27A7p4GSsZjRREIedo0sU0Nm7TZxY1WFUFDpOB70cp7W648PMHl2XsZleqp_kFWl13AjZQ4RqyVnLrGvGRmMv0geb0Bi_y0K8_tx0cp_215ootAnAhErJUeGey6A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/suAlWXjbZVm5Q3zsa07GJgRtWT40_jBAAs5R_IpdRXq_XfcA6DJVqGh1fWXutpR8jUMrirFTysezAf5eH4_qiWc4FOov6-QzGgV5uhPL5HbAtCgA2LSwjseU01JlMAhA3xh7FF7ucZQ5Ak1Gj-NnB43xbG-YoFFG_JgNvURz70s4Yo719fPyMHFkM5L_PIoD33D7VfQ5cTkg1aAMZpj1kv7y0wbgGdVcdEIGENqwlwEgplJQysvd2icz0BG9D2_zp_p86tMsA14RFQ5HCUFMhx5UK5XFNKaRFCUfIL8y67zxl7_7uNQxn_Z2kkSI3eFE6mASGSJWC6CqXi6LPSxsCA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/GJ43sF2SEsMoJ5qp7l1dwkTg8zd1OMWykln3YYATUKlz9TCcmNDSTAvdCDhAmm9WGzLNvxO9GboNmSwBNlfSRimUkZUqPs1YXxJj1jYFCdOjwbcNTJEY_8LNjbUROJ77lKn49lcVggCFqieIVkevtetcyxcgetwsKSamBMchfQHHldP6_yHZ56Zsr2iJw0F_31mroxURzxUF8KZQFim7y7YEht24W1zp67kKOfhw99MdvacPZQMH_5SDiHrnazAC0vuH05Mp5eRNFNq-4aGMMnbe3UXP7nnqlnGR3GjDRUBpqykX8MltbXKFth16Srv6qcS3sZdogWRUpaurcdRmeg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/bEdWuD8_iixz38m3Kxc9lo0ggbB_qBNky595v6HkasaAXHQXufwLpKB7-CH5FYmDle0NO2Tx8ffncXz33ATzGpeBMT9L7ZiPfCeT-CUSNV0pQNPaw6UlaNXKrwnNuGblUoYSrLvNZ4IIiwaKk6XoVcQGwTX0rD8oJPZ6p6w4dsbE0CcOPoRS3MlA4wjABxlFrXNDxHkbiWSpaMxmY0OJ6OSM4RPttpVNuNPdE4VN8Y_nRXE04tBZangx75RlA12z771qhjnKAhnYNfEQFovqKg1fpjnsc8pkJW04skAMGNdYvXxL6w9TbyM_Dof8r11uWyeY4Ti6KKWvyZqH27mfjQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
تصاویری از اجلاس سران کشورهای مشترک‌المنافع
@Farsna</div>
<div class="tg-footer">👁️ 7.78K · <a href="https://t.me/farsna/467261" target="_blank">📅 13:36 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467260">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">صدای انفجار در مسجدسلیمانِ خوزستان تا ساعاتی دیگر
🔹
فرمانداری مسجدسلیمان:  تا ساعاتی دیگر صدای انفجار در سطح شهرستان مسجدسلیمان شنیده خواهد شد که این صدا ناشی از عملیات انفجار و امحای مهمات عمل‌نکرده باقی‌مانده از جنگ اخیر است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.92K · <a href="https://t.me/farsna/467260" target="_blank">📅 13:33 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467259">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GAQWturE-GpRf0Qu0phmIUQGGrF8gKokqbhTdV1iHcu9AcTXXwd9815Dr4bO-8OnIk67s3PyBtM7i_lJ_sRpI1-XqLfOsBfnbVb-AH1s9sqmShEY2guwPHB1ndp86gzErAQVm7xY9K0AS9S5fn-g29ezDhnWd6_q5-uNfxH2dUs2NikusSCfKLzDH5HxBjDgTujUlrdFYFSCgEwBO7sCHbFvhFCrPqJTZnjniMxVkEqK1QLhkwpHkR8g6kN51V6pkJmrw86MvuBtE-ECdSj--z6-lPiXtxd1tuUx443NlCWo6CKjN5gMUHxAIstYoa8EWOqYwIF2OEXd1djAtccQ1Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
هشدار امنیتی آمریکا در اردن
🔹
سفارت آمریکا در امان، پایتخت اردن، از شهروندان آمریکایی حاضر در خاورمیانه خواست با توجه به «شرایط پیچیده امنیتی منطقه»، هوشیاری بیشتری به خرج دهند و آگاه باشند که احتمال لغو پروازها، بسته‌شدن حریم‌های هوایی و اختلال در سفرها وجود دارد.
@FarsNewsInt</div>
<div class="tg-footer">👁️ 8.69K · <a href="https://t.me/farsna/467259" target="_blank">📅 13:07 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467255">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/mtTaIm8HixdJ56TcCvE7KzPoG_yWzzR8Sh30oG9EsLi0UJIiPzvj6CYqkkacRj8MfYWbKfS7oqeBCDbQUCfzzIkfeiLAGhCJvydHlm9LPQUnJmB3WO6-ccc35aiBj97GDt6niy2fd1syZdmdAL5PTF3e17pVOYlGBp5JqwSifkzKSmldslZukr8rdmfeh5vmSiailKwH22B7QpVsMIe8tAMOSicSPEpk7yXMKq-aV_1w_ScXkJhkuc3PGRx1sJGfxZ2ZgIl_kedWW_q_unr_2atVOyRYMzgfHx0uxyAcjAugyqm11Lc3ZZy6JRKL3ZU8Xl0PkBxRMcW52GL4EyMy7Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/IBNaDRdpXRN2xz4Y3Wva4-WU_8Mt4ZbHpoL3tdNHMbw-sTEnLA6WEBn1t6OYsZwDvf7FMKrN_j97Am00maq37Ox0SQ0qv2zJqRrmlotnDmi3-dUv0ha5vs-rMQ8jUMsYJO3-9rg7XJon3AApZUqQAdH8iAe6gxb2_BxXY4vLmw8iNQTaa_Q6loTLXdVXGBTHWQsHyHzW_aR39cPLAR_62hszaK3J77ZEjdzc4GkajMkdkiaYMF_Nua8ryZ9z2CMBWWWjj-Cs4WxqhQhDSgZOavfd27dKQ1k3yNKfeDhyW6sg6jCR4eDlT-odBUlDhY65U407udbzigXVgcFIog3vlw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ONkD15xq67Z6B1fMEa9QRSglgFzfy_fmqFhj658X8Gip4cOdcZUivI_zJ7hKCeGUuYjhQWLGwnsTfkMZz-tkWPFZvlmNOxKuIX1MKlby0a2JXWSMntlA3QW3BLWx1z2qqhtiK1cErGs9TORjFJBU3GkwcgAR5Rl3LaA98keswmanLHkC5e_5uoJvWwuDEL0i1BUla3rOuVx7OHNtykCDxnpHynvK3TKnvLf9psHjUs4UOE5mIFqNScjr6qmMWQ9GQjwXl-MUHI-SBD0XtceEjU0ThUkl-905z1N1t_swQ2VYW3_ppJr4NzSSB9N-8_ERaZzRDmKv0bKuIjds_NT5bQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/OJVrSyv78absXTxNNFdBZCvMYsYqd0qJJgbhmB9iTzGS6krkC9T7GejwUj5IQ3f8PPooG9B6NjyN6m02mfKsoP8TVLx_DpIyiN7PmJ7Km_kAvGDGzDTmtNNuhDJUT0v1R3pjyT56QcFbTIPrTdh54cg5gufmoTXz4CXdv0TfJdbhwfKDix3EBxMMHESF5hJIoeP05sBbhZzCrBwKYnHIFk9Bcf-YxHeqKfr090OoDoRykJGekg4jaQEb0ZqYdpY9GKI-6LYvH-zv9bX8hltfUMzBhLQ1MZF6h44WTT0Bm6cMuVdcJBaEGjqFUmuuBM9vv5KTbPfeSQfU5bYuEWoC3Q.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">پزشکیان: امروز بیش از هر زمان دیگری نیازمند چندجانبه‌گرایی واقعی در منطقه هستیم
🔹
رئیس‌جمهور: منطقهٔ ما می‌تواند به‌جای رقابت برای حذف یکدیگر از بازار انرژی، به شبکه‌ای از تولید، انتقال و تبادل انرژی تبدیل شود؛ شبکه‌ای که نفت، گاز، برق و انرژی‌های تجدیدپذیر…</div>
<div class="tg-footer">👁️ 8.65K · <a href="https://t.me/farsna/467255" target="_blank">📅 12:58 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467254">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sl53NEe7XW04UojlH1GYkGaPfsbvwaDFj-SB1NEWDKLmSEJlpAbcgkaSv5y7EPJA77siPntMX5eR6OQYyqksGaRYuZMOou1vSEzudfTXbsxKROd9UOhyhxUQK_L7HGr64dRdiMsQPwSWlyvDnY2n2XJL2TYCHUZ_XyoXh-f40Gen9nOm0H-ShZRJSQBu5tg1LxvR-w6zR7yydQJAITdTDKUM06KGxeiaUyJCgWcGa5P31BuqwakhjGUxG0AjVLNfhABzqPIxgrc6y40NrGw0O5pfUq-160HpZyLpFSB48jaj04LXw7Pf0WKLqMpap5aEVuAlVxAOITW3o-H3dP86Vw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حاج علی‌اکبری: صیانت از خانواده به یک نهضت ملی فراگیر نیاز دارد
🔹
خطیب جمعهٔ تهران: امروز جامعه ما برای حفاظت از خانواده و تقویت بنیان آن به یک نهضت ملی فراگیر نیاز دارد و مراقبت از سلامت روابط زن و مرد در جامعه باید به‌عنوان یکی از راهبردهای اصلی در این مسیر مورد توجه قرار گیرد.
🔹
چراغ خانواده در غرب رو به خاموشی گذاشته و این روند، هشداری جدی برای سیاستمداران، نخبگان و خانواده‌هاست؛ هشداری که جوامع دیگر نیز باید از آن درس بگیرند.
🔹
ملت ایران به برکت انقلاب اسلامی، پرچم ارزش‌های اخلاقی و خانوادگی را در سطح جهان برافراشته و زمینه توجه بسیاری از ملت‌ها به این ارزش‌ها را فراهم کرده است. ازاین‌رو، چشم امید بسیاری از مردم جهان به ایران است تا در پاسداری از این ارزش‌ها پیشگام باشد.
🔹
امروز به یک نهضت ملی فراگیر برای صیانت از خانواده نیاز داریم؛ نهضتی که حفاظت از بنیان خانواده، تقویت روابط سالم اجتماعی و فراهم‌کردن زمینه رشد و تعالی خانواده را در اولویت قرار دهد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.3K · <a href="https://t.me/farsna/467254" target="_blank">📅 12:55 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467253">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IK9gEnUcO64dbm_rMeGb7zM8CMrxkQ2rhxIRQJnfyOhDfyXFrvD3cnyjNd7s91R-S1jceQETNyKH13VxxNHdA1eYpcZorGhiOrJfZsOZ-wLIaaGuvlRYfFVGKGQ8B1pWYnDF4p77Cixi29r7vZXRIyMll2-FC5sEa3emP57Q1jWKZQ1o1QZpfy8d2Vd00zTC3nGl3JFUppL9rDVQobzCD6mQa_CqL6nPB1w1mcRNF0vMP8HwtyqMGHOcVYYCr63apnTq8GXiU0GqjjXxRzzzAlVtNhXHKSEH_KeeSqYo7MzoyNSW9QD-sS3mP8vEKc6br82Zh8k5gFDBKc5p7spHuw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎥
حضور رئیس‌جمهور به عنوان «مهمان ویژه» در مراسم عکس یادگاری نشست سران کشورهای مشترک‌المنافع  @Farsna</div>
<div class="tg-footer">👁️ 8.15K · <a href="https://t.me/farsna/467253" target="_blank">📅 12:42 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467252">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/psgvJSnV76BJXpY7gT2I6K8YYJVFNf1VtYf8nNOnByZd-FXywF08WvbNlfd5o3s5nRs9sbQvqwuRBlbxGilk_XLms4FH9WIYttbxNZ2aPvklNPg3y_mwBRi1FfMgdd0AnwiDnfsKbhZiAGEkMMjvtF4_EvqW3U7q0tI2cqPF63wkPchPs1BRWA5FCY0XhOeqIy9ckcZfkvs_6cQHyOS4O2JBhQGPevUDSEBYqZIu5U428NUZ-cbppXwk8zNUo5OT7hTuJv84kPfvbBZL5EnMWlKTiEZpUwPeVUgv-1BxPgnm9IizslW_0a_-d7ytjBCpru83Rg5xcoYRW4T2fghUFg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جنجال واگذاری اراضی چابهار به افغانستان؛ اصل ماجرا چیست؟
🔹
اظهارات اخیر محسن زنگنه، نمایندهٔ مجلس و رئیس کمیسیون ویژه اصل ۴۴، دربارهٔ واگذاری اراضی چابهار به افغانستان، با واژه‌ای همراه شد که موجی از نگرانی و انتقاد را در فضای عمومی ایران برانگیخت.
🔹
او در گفت‌وگو با شبکهٔ سحر افغانستان اعلام کرد که «افغانستان بتواند در بندر چابهار در منطقه آزاد، یک سرزمین متعلق به خودش داشته باشد».
🔹
زنگنه خود نیز بعدها به تحریف اظهاراتش واکنش نشان داد و تأکید کرد: «موضوع، اختصاص زمین برای سرمایه‌گذاری افغانستان در بندر چابهار است و به هیچ عنوان به معنای واگذاری خاک یا حاکمیت جمهوری اسلامی ایران نیست».
🔹
در شرایطی که منطقهٔ شرق کشور با تهدیدات تروریستی مستمر روبه‌روست و هرگونه تنش رسانه‌ای می‌تواند به سوءاستفاده سرویس‌های امنیتی رقیب منجر شود، انتخاب واژگان نادرست از سوی یک نمایندهٔ مجلس آن هم در گفت‌وگو با رسانه افغانستانی می‌تواند سریعا به یک اقدامی ضد توسعه بدل شود.
🔹
آنچه در چابهار در حال وقوع است، اجارهٔ بلندمدت زمین برای سرمایه‌گذاری است؛ الگویی که در ده‌ها بندر جهان، از اروپا تا آسیا و از آمریکا تا آفریقا، امری روزمره و پذیرفته‌شده است.
🖼
اما آنچه در چابهار با افغانستان می‌گذرد، دقیقاً چیست؟
اینجا
بخوانید.
@Farsna</div>
<div class="tg-footer">👁️ 8.09K · <a href="https://t.me/farsna/467252" target="_blank">📅 12:38 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467251">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/i8TS0V4ylpH6NaSomDttCINsm38wqJzIDI04wCrJ8BEdCYfBfTIlCLtlTZuQ6bkeTPEvEKyPsW-6mxhX9sUe-9k55eRL9g9tmV4MQkOq_7v4lwsb3xRrsiYZ-5GMcY3pgQOU5KjCw5un1vVS_Y6ciQ5xS9EhCT9GlyGCYsjlT1-mKCS2CvYZ5nNgQbwV1nhHaVaM_AjbTF14LjMP9us3VkmteRHUG5E1d8Nb6IVdl-IUz8fDTPBz1kUTXRr2jsEFnLlFtLj6axgcXEpwICK26Mt3p6fwshwKydYCf_tx0zUdRWG6QxDhG19a29tQxpyapeVZ7AsonwGUiiHGXyOdoQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
بیرانوند در پاسخ به مدیرعامل تراکتور: اعتبار حرفه‌ای من برایم ارزشمند است؛ دفاع از آن را از مسیر قانون دنبال خواهم کرد
🔸
مدیرعامل تراکتور علاوه‌بر انتقاد از بیرانوند برای «خسته‌نباشید به استقلالی‌ها»، گفته بود او در بازی مقابل استقلال عملکرد خوبی نداشته…</div>
<div class="tg-footer">👁️ 8.3K · <a href="https://t.me/farsna/467251" target="_blank">📅 12:30 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467250">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">یحیی سریع: به فرودگاه‌های عربستان حمله کردیم
🔹
سرتیپ یحیی سریع، سخنگوی نیروهای مسلح یمن اعلام کرد شامگاه امروز پنجشنبه فرودگاه ملک خالد در ریاض با دو موشک کروز و فرودگاه نجران و پایگاه هوایی خمیس مشیط هم با موشک‌های بالستیک مورد اصابت دقیق و مستقیم قرار گرفت.…</div>
<div class="tg-footer">👁️ 8.78K · <a href="https://t.me/farsna/467250" target="_blank">📅 12:15 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467249">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TMxOBVMg5iufqupwUrqxn8yVyrJ5Ab9rUR5Ainh9jRW8WybOL1dUia8VIE4pICiVTkLQm_Vhxez_aU3fKjK8Hm-2cyPObitxxM3ocgk9vx0HH4Alo2CERj23lMocjWAXgeahww1rtSSOCUwH0KEJN8IrEnM6XM-9TfZyG-TtqnOJY-ygRDhtXo1pruAzJuozWx_SK0wkAM63OGRoniRsk74KQRAeOV0enhjb_bH4J4MZ0ex106EfrUP_QU_zxjj6fhcF75mA22uhkx0vSsIjzcQ30Hz1gxCtlhTsqg8nJr87GXmHp2rNHTU3siRCEfew2ue2aezn1r3h5czarDpdvA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مقر قدیمی سیا به پایگاه نظامی چین تبدیل شد
🔹
سی‌ان‌ان: ارتش چین یک مرکز مشترک پشتیبانی و آموزش نظامی را در شمال‌غرب لائوس، در محل یک فرودگاه متعلق به دوران جنگ ویتنام که پیش‌تر سازمان سیا از آن استفاده می‌کرد، راه‌اندازی کرده است.
🔹
این مرکز در فرودگاه بان کئون، حدود ۶۴ کیلومتری شمال وینتیان، پایتخت لائوس، و در فاصله حدود ۴۰ کیلومتری نزدیک‌ترین مرز تایلند قرار دارد.
🔹
فرودگاه بان کئون در لائوس نیز در دوران جنگ ویتنام به‌عنوان یکی از مراکز پشتیبانی و تدارکاتی شرکت ایر آمریکا، وابسته به سازمان سیا، برای عملیات مخفیانه در منطقه مورد استفاده قرار می‌گرفت.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.53K · <a href="https://t.me/farsna/467249" target="_blank">📅 12:01 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467248">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/npdTbDtSV8T4n1N1loQWNP6JK4FXCTnG2HbTVrJVIWb-IrpjmZ68UUS7l72yYlVcpIM_pcwnJEPe6MptSWqcB5t_3OTWRBjSA8wu7rBchLYNzBvqBdsGKYnWf051SRyPFIxNc370eVWmGumeIGD3iAEIAW3OrYH8dGrH4IiHuiYwfCGfA50chpMx8h4zzvMIrHKBgV_xaIkl5x_WYWz5dsZQBaJ0hhHTG0VrktewHEEkl9IEZ8SQXrq9acbozD5je4LXYq3lUN4XDMcbsM6dQAooLY-TuYHoR4A5M-x5q3Lv0IxJg7pHeWomHGh3rj6cTfQZ8OiWdo1R-ZrGe6S8kw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بازار خودرو خارجی زیر سایهٔ جنگ
🔹
رویترز: قیمت بنزین در فیلیپین از زمان حملات آمریکا و اسرائیل به ایران در اواخر فوریه، ۶۸.۳ درصد افزایش یافته است.
🔹
این کشور تقریباً تمام سوخت موردنیاز خود را وارد می‌کند و یارانه سوخت نیز ندارد، آنها مجبور شدند به سمت خودروهای برقی روی بیاورند.
🔹
تنگهٔ هرمز، به‌عنوان یکی از مسیرهای مهم انتقال نفت و فرآورده‌های انرژی، در این بحران به نقطه‌ای تعیین‌کننده تبدیل شده است.
🔹
اختلال در عبورومرور انرژی یا افزایش نگرانی از تداوم عرضه، هزینه سوخت را در کشورهای وابسته به واردات بالا می‌برد و فشار آن به حمل‌ونقل و هزینه زندگی مردم منتقل می‌شود.
🔹
حال فیلیپین به ثبت‌نام خودروهای برقی و هیبریدی روی آورده است، افزایش تقاضا برای خودروهای برقی در شرایطی رخ می‌دهد که جنگ ایران و آمریکا و اسرائیل، بازار جهانی انرژی را با شوک تازه‌ای مواجه کرده است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.89K · <a href="https://t.me/farsna/467248" target="_blank">📅 11:50 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467247">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3c877e1ef2.mp4?token=oCOWmRW4LhqRjF7dHyNa-X-oCFyFkIEgMtcbPVlD1usPxU1p9WwPNCXA6ihu1Vf-_O-vaNoUA70E46ut1SqIf1XUAmbYugnhDRFdb8K8ORRBUtWmQ7eJi7TZtVQNQ3JeI3i049TZIFIrWsJvuJIIiG6cLouvLMrJyKqLXS__-CVyqgE2h0zFTI-p-BIKoWOsf6ITDRXD1P9rjxp5HoQ8HHCTYG1FObO9W9P2rsnnh5HLXz1seEzRXg7caccBPL5weodLty0A0F4YcT39PbUZ9tKIO4sqzu5Xm1nGwuVs2O7yFqZuLwr3vqSnWa47oUKdfx2FW5FNGJWVBGbBCFVRoQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3c877e1ef2.mp4?token=oCOWmRW4LhqRjF7dHyNa-X-oCFyFkIEgMtcbPVlD1usPxU1p9WwPNCXA6ihu1Vf-_O-vaNoUA70E46ut1SqIf1XUAmbYugnhDRFdb8K8ORRBUtWmQ7eJi7TZtVQNQ3JeI3i049TZIFIrWsJvuJIIiG6cLouvLMrJyKqLXS__-CVyqgE2h0zFTI-p-BIKoWOsf6ITDRXD1P9rjxp5HoQ8HHCTYG1FObO9W9P2rsnnh5HLXz1seEzRXg7caccBPL5weodLty0A0F4YcT39PbUZ9tKIO4sqzu5Xm1nGwuVs2O7yFqZuLwr3vqSnWa47oUKdfx2FW5FNGJWVBGbBCFVRoQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
کاروان دوچرخه‌سواران ترکیه‌ای «مقاومت شهدای میناب» وارد ایران شد
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.71K · <a href="https://t.me/farsna/467247" target="_blank">📅 11:48 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467246">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس ورزشی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gBHz4A4fN0LpcgugVTVaoE9bSj9w_G3SEtlUVyAvu9Kc_0tOUL3ug_IJHg6mgrXLUTZvE0YHYILMCszjm6Mashri0aI9GGHmUQ2XwScP895NUegOwIPrxGnIbyLiw6u609wx_GHbXn975JG-k_Y23SZ_rIT7L8PX3HZNTzyMVSMSLAZUill0kq8BszOkOqcAZ6tFHu4j2nhNIfp67jaVhQUiLgPPKq5QG741KhFqJlAKxJ6Ce10LOI8wS0DQycxwPyKt_boUgrg8acPhF-sFqL8huAjRTpYFnXJdhj0W5auqtYf4L_XADwmcsjvKGy1bQ4bn1mN6-PhDgmigAJZKZg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دوومیدانی‌کاران ناشنوای ایران نایب قهرمان آسیا شدند
🔹
تیم ملی دوومیدانی ناشنوایان کشورمان موفق به کسب پنج مدال طلا،‌ ۳ نقره و چهار برنز شد و با ۱۲ مدال به کار خود در این مسابقات پایان داد.
🔹
براین اساس تیم ملی دوومیدانی ناشنوایان کشورمان در رده‌بندی نهایی مسابقات بعد از ژاپن و بالاتر از هند به رتبه دوم رسید.
@Sportfars</div>
<div class="tg-footer">👁️ 7.92K · <a href="https://t.me/farsna/467246" target="_blank">📅 11:41 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467244">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/44855256e8.mp4?token=jZZwAWpe2tBMrbw2Wg3M7UiKLB33M338xm9HEWT-VjKeEUL2KqXnOH_5SJMUdD56plmCW3Ll3VyTuUMOB5cre8f8Q3Bmh5owUcphgS9RAMwOMzsRef4iJoRlZCaNy_NY63xhAokI418gae-0deIr__6dmfd1qYDdQ-niZb-alJRHc0svQzb5I6mdBnaiDwNTJCad9nciOwh72wLpxA7tzENHZIu69_xYvPabFk6NfC4HTvzLduxtgbJxVocS3PHSrZaaERE-hN8TwtpyB5G_9mkmxmADYvslMOOB8NC3I1DKbExghxnm-CXPuCp2WsaJGr6IkPC3yQuuP8xZIKM48g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/44855256e8.mp4?token=jZZwAWpe2tBMrbw2Wg3M7UiKLB33M338xm9HEWT-VjKeEUL2KqXnOH_5SJMUdD56plmCW3Ll3VyTuUMOB5cre8f8Q3Bmh5owUcphgS9RAMwOMzsRef4iJoRlZCaNy_NY63xhAokI418gae-0deIr__6dmfd1qYDdQ-niZb-alJRHc0svQzb5I6mdBnaiDwNTJCad9nciOwh72wLpxA7tzENHZIu69_xYvPabFk6NfC4HTvzLduxtgbJxVocS3PHSrZaaERE-hN8TwtpyB5G_9mkmxmADYvslMOOB8NC3I1DKbExghxnm-CXPuCp2WsaJGr6IkPC3yQuuP8xZIKM48g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
آنچه در سفر وزیر نیرو به کابل گذشت
@Farsna</div>
<div class="tg-footer">👁️ 7.83K · <a href="https://t.me/farsna/467244" target="_blank">📅 11:34 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467243">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">🎥
از هامبورگ تا دارالذکر
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.18K · <a href="https://t.me/farsna/467243" target="_blank">📅 11:28 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467242">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1ba130634c.mp4?token=TzpL-6MfkwEXkX7cl_GOgTwy_qmMD6koOwMsg19ARCq7rMrsDFi4YxDob4jUcmBICn3xdabYrGScs9gASKak1HfkVM_vyFU0wDYALFNuUbU5AcSlF6qtKhhnanHBkfWtDlJhZtuyZtCMe9_l_Gs6zmQ0CpOG5War96Y6oKRYk5QcNSxZaJq7MGpvCeKUlqV8WIYUwrVuZdgcA4VWqciVHH0ehS3QArw1G8WGXlYOvIzp27tRBqiubRHYIGm-KsThcZomgii-ByvA-O-j6MsK0ab3wxWovuE3pLw0YZSB8TDpUg9LWdKw1ggNwdrOODVM6gDrTdI19qMTSs5ol8Vjmg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1ba130634c.mp4?token=TzpL-6MfkwEXkX7cl_GOgTwy_qmMD6koOwMsg19ARCq7rMrsDFi4YxDob4jUcmBICn3xdabYrGScs9gASKak1HfkVM_vyFU0wDYALFNuUbU5AcSlF6qtKhhnanHBkfWtDlJhZtuyZtCMe9_l_Gs6zmQ0CpOG5War96Y6oKRYk5QcNSxZaJq7MGpvCeKUlqV8WIYUwrVuZdgcA4VWqciVHH0ehS3QArw1G8WGXlYOvIzp27tRBqiubRHYIGm-KsThcZomgii-ByvA-O-j6MsK0ab3wxWovuE3pLw0YZSB8TDpUg9LWdKw1ggNwdrOODVM6gDrTdI19qMTSs5ol8Vjmg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
نمایندگان مجلس برای حل مشکلات مردم خارگ قول مساعد دادند
@Farsna</div>
<div class="tg-footer">👁️ 8.74K · <a href="https://t.me/farsna/467242" target="_blank">📅 11:11 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467241">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/95e8b2b99a.mp4?token=KkRQCb8Uvd4fsWFE4FtTz6cmWCQk8TlzsJWMl3T1jQcJBli-KQOySObnSj0nXHBYIGhyVJn8He8JQLgpNs5fIXZqJMnUMp8UY1g1lJwDrKgLirBQh0A1wYYIUlge_hI148ytUzLcqR0FJFqRpU8fcEt67M4oN2sH0yZ-sImOj5RIYQC_NZ0IQpOf6gtorgftpou7pYqo6WcWBQyW7JoGmxXQ0n6bjxCUXxGHOH7t6WrF1hkEp2_QOouoyNKAksk98p27Aul7EQcjqLQs5YY1VsAerl5ycwhXCfNK4sDYQwh33CM0Tp7qenPZ-FcW2x7ats8SOrmmT9IFdxVUSwrYTw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/95e8b2b99a.mp4?token=KkRQCb8Uvd4fsWFE4FtTz6cmWCQk8TlzsJWMl3T1jQcJBli-KQOySObnSj0nXHBYIGhyVJn8He8JQLgpNs5fIXZqJMnUMp8UY1g1lJwDrKgLirBQh0A1wYYIUlge_hI148ytUzLcqR0FJFqRpU8fcEt67M4oN2sH0yZ-sImOj5RIYQC_NZ0IQpOf6gtorgftpou7pYqo6WcWBQyW7JoGmxXQ0n6bjxCUXxGHOH7t6WrF1hkEp2_QOouoyNKAksk98p27Aul7EQcjqLQs5YY1VsAerl5ycwhXCfNK4sDYQwh33CM0Tp7qenPZ-FcW2x7ats8SOrmmT9IFdxVUSwrYTw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
رئیس پلیس فتای فراجا: تجارت وام در فضای مجازی ممنوع است؛ به وعده‌های وامی در این فضا اعتماد نکنید
@Farsna</div>
<div class="tg-footer">👁️ 9.3K · <a href="https://t.me/farsna/467241" target="_blank">📅 11:01 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467239">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a86db71c63.mp4?token=WuB7GcGD2tEwYhTtcmtz77CD-nM-0ANo4hIEaZ_8w7_ty9SU_qlOPZhEqV8kQyoODmG-fzCYJLMXMgFHa61y2qLK7eohjuqsBbOmEk78w_4Mv-IURoyWV_Fj2tY4EY1-lSuldlnRstMssSvsg_9Cjp7DTBpeq5PQoU0Cd79BQJ8tXUCh_EtTBAc_3fkAJhc-WmTWWBe0oTeQPdmo2UOp2UWhfRvXXagEP01a6kNdIdJo2FNan0T_U-c9WMXd2Q86pzD1ky-snJM58je89W2-Qis9ReJyvymBALbEnLluZHH3dG99NGjJuvxHGK19QihyH_Pfe2oGu7sXiZWMjnRRFw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a86db71c63.mp4?token=WuB7GcGD2tEwYhTtcmtz77CD-nM-0ANo4hIEaZ_8w7_ty9SU_qlOPZhEqV8kQyoODmG-fzCYJLMXMgFHa61y2qLK7eohjuqsBbOmEk78w_4Mv-IURoyWV_Fj2tY4EY1-lSuldlnRstMssSvsg_9Cjp7DTBpeq5PQoU0Cd79BQJ8tXUCh_EtTBAc_3fkAJhc-WmTWWBe0oTeQPdmo2UOp2UWhfRvXXagEP01a6kNdIdJo2FNan0T_U-c9WMXd2Q86pzD1ky-snJM58je89W2-Qis9ReJyvymBALbEnLluZHH3dG99NGjJuvxHGK19QihyH_Pfe2oGu7sXiZWMjnRRFw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مأموران مهاجرت آمریکا باز هم به یک نفر تیراندازی کردند
🔹
یک مأمور ادارهٔ مهاجرت و گمرک آمریکا در جریان عملیات بازداشت در شهر نیویورک به سوی مردی تیراندازی کرد و او را زخمی کرد.
🔹
این حادثه‌ در پی چندین مورد تیراندازی مأموران مهاجرت به افراد در ماه‌های اخیر، بار دیگر شیوهٔ برخورد این نیروها با شهروندان و مهاجران را در کانون توجه قرار داده است.
🔸
زهران ممدانی، شهردار نیویورک در واکنش به این حادثه گفت: «دولت ترامپ فضای رعب و وحشت ایجاد کرده است» و خواستار توقف عملیات این نهاد فدرال در نیویورک شد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.26K · <a href="https://t.me/farsna/467239" target="_blank">📅 10:54 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467238">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">🎥
گلباران مردم توسط هوانیروز
🔸
مهمان نوازی هوانیروز کرمان در روز افتتاحیه بزرگترین پل جنوب شرق ایران که مزین شده به نام شهدای خلبان  @Farsna</div>
<div class="tg-footer">👁️ 8.87K · <a href="https://t.me/farsna/467238" target="_blank">📅 10:42 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467237">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cI8JVH7WJtcAtjWWH6BmA-vwlZhdb5-y6ByJIXsGDt2TPtUBXMcABER78nhDL5y9r0MCSOkJ6hQFyCUT_bx5Qjp6wUjOtijHurCy4ZhtjEL76vYB_kqMW23VL8vSJhhrhhQhtnHbAbAvrmoflTvc0F4koI1WChclRf7NGvy7cBa81ITRkAygCwYFEQ1yV1Wlps0pNnn6Kh4AOGj-1F4ZQ-iEbgC0uCMgV7X_8z_C3BxMbjxD2sCAMR0NLpPuWAPkVXDcfVk5KL-Nl4JVU_Chk2IzyscYvXN-jXbN80fifF4_G9OGunUmd2OAbGOb5e5snLvkj2SBenQF3T9MvuwNyw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نامزد سنا: اسرائیل قوانین جنگ و حقوق بین‌الملل را نقض کرده است
🔹
جان اوساف، سناتور دموکرات ایالت جورجیا، اعلام کرد نیروهای اسرائیلی در نوار غزه قوانین مخاصمات مسلحانه و حقوق بین‌الملل بشردوستانه را نقض کرده‌اند.
🔹
اوساف که برای انتخاب مجدد به سنای آمریکا رقابت می‌کند، روز پنجشنبه در جریان مناظره انتخاباتی درباره احتمال ارتکاب نسل‌کشی در غزه گفت که این موضوع باید از سوی دیوان کیفری بین‌المللی بررسی شود.
🔹
این سناتور دموکرات در ادامه، از مایک کالینز، رقیب جمهوری‌خواه خود و نماینده کنگره، به دلیل حمایت از اعمال تحریم علیه دیوان کیفری بین‌المللی و قطع بودجه آن انتقاد کرد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.24K · <a href="https://t.me/farsna/467237" target="_blank">📅 10:34 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467236">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BE8ILNbmvnhAECtYB1ra0czeCdcmxc5Ed6C1CXZOxcfW3PZ9Wi2UfhrjS_kYL_LVDo13rkUsFtIrsriG-Xw6IrOckvprSaYRz-WII5amKMD-2S4wgSnAtn5p_A0dQ54--hBJJMzfoqBAjJROx89JMOXVblZzmu7ahBbrBxSuQF-8YiHjxJ7wFxuKgaCY2SPXaIt5V9ucY_s9_JzkTjCTnqp-McKpS3hTBpF-MH1mWCDKqL2H1GZrifWLx2MjjP-6IEozf6F4d42jSzJZuciakhT_hHlX_1peNeixmARtmOpcIH_C-C55xCoGh7szgBfbsB7sh_piqjlvNovUSXEmFQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">۲۱ میلیارد دلار ارزی که از جیب اقتصاد کشور خارج شد
🔹
در یک سال و نیم گذشته، معادل ۲۱ میلیارد دلار از ارزهای حاصل از صادرات به چرخه اقتصاد بازنگشته است؛  رقمی که ۸ میلیارد دلار آن مستقیماً به معضل استفاده از کارت‌های بازرگانی اجاره‌ای گره خورده است.
🔹
باتوجه به حجم کل صادرات غیرنفتی که حدود ۵۰ میلیارد دلار برآورد می‌شود، عدم بازگشت این رقم نشان می‌دهد نزدیک به ۴۰ درصد از کل منابع ارزی حاصل از صادرات وارد چرخهٔ رسمی کشور نشده است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.67K · <a href="https://t.me/farsna/467236" target="_blank">📅 10:15 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467235">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">تلاش ناتو برای آرام‌کردن روسیه پیش از رزمایش اتمی در ایتالیا
🔹
پالتیکو: ناتو به دنبال اطمینان دادن به روسیه است مبنی بر اینکه رزمایش‌های نیروهای هسته‌ای در ایتالیا هیچ تهدیدی برای این کشور ایجاد نمی‌کند.
🔹
مدیر سیاست هسته‌ای ناتو ادعا می‌کند که هیچ دلیلی برای نگرانی روسیه و سایر کشورها درباره رزمایش اتمی در ایتالیا وجود ندارد.
🔸
رزمایش سالیانه «روز استوار» از ۱۳ تا ۲۳ اکتبر در ایتالیا برگزار می‌شود که برای حفظ آمادگی نیروهای هسته‌ای و تمرین رویه‌های لازم برای بازدارندگی و دفاع ناتو طراحی شده است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.37K · <a href="https://t.me/farsna/467235" target="_blank">📅 10:02 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467234">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b74322aaf3.mp4?token=uQI1_T0WQZjGI4jaXeXzRl_9NgzuYM6i8sT64Sedo-PMi3OBYm1HArUA8qne8TCobcCELm-bvuNAjPxbTtUPaFSxnm1k1w356_cnz62JCMLJmsj0VkA0C4SM8jU76Wdb_Rn7Wkff0Vb825-feJpGSeraC5v15LDLyOysP2a7TLDLW33wzLi54qnGeS-EWp1vPFwAvX2ljTmbTZk2mWLWpcS70ckfPGl46i0tJfUfIvjUh63GCQZ3rEDI26NtvN_4dI2F6BZV9i41lqJQNym44-0pV-C8Ci0eI0o0Z_VP5CFp2NhB-tisNnP8sUMZgYhCjjO7pBX2TW_lCzbLpxm4Gg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b74322aaf3.mp4?token=uQI1_T0WQZjGI4jaXeXzRl_9NgzuYM6i8sT64Sedo-PMi3OBYm1HArUA8qne8TCobcCELm-bvuNAjPxbTtUPaFSxnm1k1w356_cnz62JCMLJmsj0VkA0C4SM8jU76Wdb_Rn7Wkff0Vb825-feJpGSeraC5v15LDLyOysP2a7TLDLW33wzLi54qnGeS-EWp1vPFwAvX2ljTmbTZk2mWLWpcS70ckfPGl46i0tJfUfIvjUh63GCQZ3rEDI26NtvN_4dI2F6BZV9i41lqJQNym44-0pV-C8Ci0eI0o0Z_VP5CFp2NhB-tisNnP8sUMZgYhCjjO7pBX2TW_lCzbLpxm4Gg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
حضور ۲۳۰ هزار نفری در پیاده‌رویِ خانوادگی کرمان  @Farsna - Link</div>
<div class="tg-footer">👁️ 9.88K · <a href="https://t.me/farsna/467234" target="_blank">📅 09:50 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467233">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/23e4c1d123.mov?token=tg1o4QD8x-qHrZj8Tq0WcxHPpFFVTFO5zu1z6WcOtFh2aS3jeEr2UclMLURQe-GWRI0CYwpU-O35lHiJH6iEHXItiTepbJnfKQJNcoGFC-xzzHzOSqGcRIFa1Q-tnzPwVQUIJIvSmcSnkZ6bFOq1s6DwCdF8NNPa4RD3LnnetggxhpEbpmbwL03i-W7MflM3bzlabp2yKFExAEvF_bdEzyVKXc2QJL4_ZlEiC_VTIuVhV3npWTw8KiZ5sZSxUNGFRhwgPDusuufDiCZrtbRPeME3cwhZTtgbGLvOPJiNbcxxCoUjn05caK4popGIVQRgCfDlW2xVmXZGCCvw_aOPaw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/23e4c1d123.mov?token=tg1o4QD8x-qHrZj8Tq0WcxHPpFFVTFO5zu1z6WcOtFh2aS3jeEr2UclMLURQe-GWRI0CYwpU-O35lHiJH6iEHXItiTepbJnfKQJNcoGFC-xzzHzOSqGcRIFa1Q-tnzPwVQUIJIvSmcSnkZ6bFOq1s6DwCdF8NNPa4RD3LnnetggxhpEbpmbwL03i-W7MflM3bzlabp2yKFExAEvF_bdEzyVKXc2QJL4_ZlEiC_VTIuVhV3npWTw8KiZ5sZSxUNGFRhwgPDusuufDiCZrtbRPeME3cwhZTtgbGLvOPJiNbcxxCoUjn05caK4popGIVQRgCfDlW2xVmXZGCCvw_aOPaw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
حضور رئیس‌جمهور به عنوان «مهمان ویژه» در مراسم عکس یادگاری نشست سران کشورهای مشترک‌المنافع  @Farsna</div>
<div class="tg-footer">👁️ 9.15K · <a href="https://t.me/farsna/467233" target="_blank">📅 09:40 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467232">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">۶ کشته و زخمی در حملات پهپادی اوکراین به روسیه
🔹
وزارت دفاع روسیه: ارتش اوکراین در شب گذشته با ۵۰۵ پهپاد به مناطق مختلف روسیه حمله کرد که در پی این حملات پهپادی به منطقه بلگورود، ۲ نفر کشته و ۴ نفر زخمی شدند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.56K · <a href="https://t.me/farsna/467232" target="_blank">📅 09:35 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467231">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromدانشکده خبرگزاری فارس</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tQpVj8rW4G0Rnj2wKTrTL0ecLrBVKHyWgQHLVpfJk0fS291YnZlZgjZ0nbjSCmrbGiRxIY7fOL9nIyzKVAJbBTokLd6H6K1FDTKP8f8FW1_ap3nQdk7dWHMuqJ2BvKrUcyF9_KANqRhnpKCyY56HetBiAHhz08ue_5VPi_189-17uMAltbBj9Q2aaxN1c1rwG9iYofTuyjx8GwcoODT5liNZjtoESuTDIrC1C-mwuI-yYgQzdcTB9EQuk0DDTXWZzee4XzThOmWdBCNpxjochIOJlWNcWriv3XNNXrAFsKVHUvKLJnL3srhVrXaQVH2oSyTzvDnnI1YPeGCzu-e2qA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔰
مهلت ثبت‌نام و انتخاب رشته در پذیرش دوره های کاردانی و کارشناسی ناپیوسته دانشکده خبرگزاری فارس تا ۱۵ مهرماه تمدید شد.
🏷
براساس اعلام سازمان سنجش آموزش کشور، مهلت ثبت‌نام و انتخاب رشته در پذیرش دوره کاردانی و کارشناسی ناپیوسته دانشگاه جامع علمی کاربردی
از امروز تا۱۵ مهرماه تمدید شد.
📚
رشته‌های تحصیلی:
🎙
خبرنگاری
📸
عکاسی خبری
🎞
سینما‑تدوین فیلم
🤝
روابط‌عمومی
🎤
گویندگی و دوبله
ارسال  عدد ۱۴ را به شماره ۵۰۰۰۱۰۱۴
🌐
لینک سایت ثبت‌نام
🔗
futurix.ir/go/rxDxXO
☄️
☄️
این فرصت رو از دست ندهید
🎓
مرکز آموزش علمی کاربردی خبرگزاری فارس
🎓</div>
<div class="tg-footer">👁️ 3.66K · <a href="https://t.me/farsna/467231" target="_blank">📅 09:30 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467230">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/175419dd2b.mp4?token=Rui9g0q8PUvckRcPSMBG_eT5HL2z7xJ89b-Gq97MbC_ml_hO9ZLZu4YFDbqC_dhEvEwLQNgDRL-JZCI_Op6o-1esCmfyrRgsh9RxE70tcy80cSc7tqQpCV9lAGpE81gktkMBBosYK1wOU8s5ZRcEFwo4e3B3OUQ1QywZz7SqZqRPh6hfmkCs75DAcxw5A_HDRT5EevLB_oJufv_hcySxnKxm6vNnJRXh8icQvPrieAnfkHZyZjLJ0KH3AEliAsZZTjpZZ1xc-lU4nFY6goSSp-4zCVXF6Ixm5MWhZG6GHXiSzLLd0H31_EkVO44Uj-o5lw4lVGff5C_yktVP-VFZfA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/175419dd2b.mp4?token=Rui9g0q8PUvckRcPSMBG_eT5HL2z7xJ89b-Gq97MbC_ml_hO9ZLZu4YFDbqC_dhEvEwLQNgDRL-JZCI_Op6o-1esCmfyrRgsh9RxE70tcy80cSc7tqQpCV9lAGpE81gktkMBBosYK1wOU8s5ZRcEFwo4e3B3OUQ1QywZz7SqZqRPh6hfmkCs75DAcxw5A_HDRT5EevLB_oJufv_hcySxnKxm6vNnJRXh8icQvPrieAnfkHZyZjLJ0KH3AEliAsZZTjpZZ1xc-lU4nFY6goSSp-4zCVXF6Ixm5MWhZG6GHXiSzLLd0H31_EkVO44Uj-o5lw4lVGff5C_yktVP-VFZfA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
حضور ۲۳۰ هزار نفری در پیاده‌رویِ خانوادگی کرمان
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.81K · <a href="https://t.me/farsna/467230" target="_blank">📅 09:23 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467229">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b7eb764da2.mp4?token=qzILZebz_95Rk9JyM0YOP9viU7G_Ol5qrO6n3HGCvl1D0KA88r1SFAzUkWUkur29cLD4YFanIRNkqrIG1444qVp56ZKtL8xWRffBD1O3kuOV_bdVRIKoy8wZBBoKrtdFgdd8ARwjv04puRL2FGdrwAUZFZDDPmSIc-t95Thy3W2fqaZ0W6lF2oMDN4QcUi8bxMQRWuYlusG6SWNsh4l3YpH0RQnEuXM-Hiaj6hdbQua-8TSZb1eBx46Lia3kaw5i-KFXpmc8yzj1QD-chmVb6JjmJsE7tCaTskHVPQG13oY8GcJ-Snu6jhgjmwZgIiiGsJMisCEEXLFlbQwjAJhDLQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b7eb764da2.mp4?token=qzILZebz_95Rk9JyM0YOP9viU7G_Ol5qrO6n3HGCvl1D0KA88r1SFAzUkWUkur29cLD4YFanIRNkqrIG1444qVp56ZKtL8xWRffBD1O3kuOV_bdVRIKoy8wZBBoKrtdFgdd8ARwjv04puRL2FGdrwAUZFZDDPmSIc-t95Thy3W2fqaZ0W6lF2oMDN4QcUi8bxMQRWuYlusG6SWNsh4l3YpH0RQnEuXM-Hiaj6hdbQua-8TSZb1eBx46Lia3kaw5i-KFXpmc8yzj1QD-chmVb6JjmJsE7tCaTskHVPQG13oY8GcJ-Snu6jhgjmwZgIiiGsJMisCEEXLFlbQwjAJhDLQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
پزشکیان برای شرکت در نشست سران کشورهای مشترک‌المنافع وارد سالن اجلاس شد  @Farsna</div>
<div class="tg-footer">👁️ 9.39K · <a href="https://t.me/farsna/467229" target="_blank">📅 09:10 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467228">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/efdbdbe8b0.mp4?token=qJXUDbv4HpzVTxMU39uB59NbvULdGoWS4zsSuISIa-I1bEjfZphyd0miRvo49HiiXS77sP2u5Sm7iy_k59M2ajGCWVnhzR_bkRbSTwRa6UUXbSMm4A0uglv5O35w8s5ByE0dyQ6DQWSk2n4hcq6EuUXWLNVwWXRnFfD6BMhhi5Ny7ih-Uc4wPcrK-MfAXiK9MRPb5y-1aHbeMz73ntcMounVxgVhfKaphXIv8Tfm22fKDPxLSo28lhSzJw_1Osi61lE_ifnnwTIFtNv_EZBWF5ixiDH29J05gxYAEuDg62y48NDJ1As7u0KBdITN89AXAWhgGBgN001-SoM9b3wbEg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/efdbdbe8b0.mp4?token=qJXUDbv4HpzVTxMU39uB59NbvULdGoWS4zsSuISIa-I1bEjfZphyd0miRvo49HiiXS77sP2u5Sm7iy_k59M2ajGCWVnhzR_bkRbSTwRa6UUXbSMm4A0uglv5O35w8s5ByE0dyQ6DQWSk2n4hcq6EuUXWLNVwWXRnFfD6BMhhi5Ny7ih-Uc4wPcrK-MfAXiK9MRPb5y-1aHbeMz73ntcMounVxgVhfKaphXIv8Tfm22fKDPxLSo28lhSzJw_1Osi61lE_ifnnwTIFtNv_EZBWF5ixiDH29J05gxYAEuDg62y48NDJ1As7u0KBdITN89AXAWhgGBgN001-SoM9b3wbEg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
پزشکیان برای شرکت در نشست سران کشورهای مشترک‌المنافع وارد سالن اجلاس شد
@Farsna</div>
<div class="tg-footer">👁️ 9.75K · <a href="https://t.me/farsna/467228" target="_blank">📅 09:08 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467227">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/h_I0onw3ExHixRRHVR4gkaY-JaE9BAo2dyXEQ77--CuME_UFqFVAl7oTA01lJVRr-b78vBaOL_8w1wkRPXqTweyPabEsXx5JBD0xvUCdMmpZFmyvDAXoBSsghXAQKyXOtwwtpttY6OGY4V6ar3rck0H8hTDReyFaEVLLkQugxaHlQfa0OVaGVEb6H2ASOmqElc5NhUokd0dSMx0LcHl5Jayljs4EuJK_MIct5KjmYnhIkgrf15UHkNgMFt0RSEzNdXHBvi1rKzo7Q35N3tA113PVPqyuHgFfqZ3J0yp07we2ymeXqRSixJlntwsJTW4K853o5piVBTYjJ_t_M_gevw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فعالیت‌های دریایی در دریای مازندران موقتاً متوقف شد
🔹
هواشناسی مازندران از وزش بادهای شدید و مواج شدن دریا خبر داد و با تأکید بر خطر غرق‌شدگی، فعالیت‌های شنا، قایقرانی و صیادی را در سواحل استان محدود کرد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.48K · <a href="https://t.me/farsna/467227" target="_blank">📅 09:06 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467226">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">🎥
ماجرای اولین سفر با کشتی از تهران تا بندرعباس
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.36K · <a href="https://t.me/farsna/467226" target="_blank">📅 08:37 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467225">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/50a90f4363.mp4?token=MoAUKnIk9Ppy7UPwN1-VPM9hruekC4dtSfJOY3aLJDjxr6yzDoGsAGiP3CDlucQuihPh_SI1WfWVtO_Ug58KtWzl1fHnmTnlNp_4cA9hbVhLRgBMzVSPup5739U0W0n0ZcRFbNQ1qgPB4yXFy-JX13wYxyTTju6gY-8AetNuhllgXIa_U58dDa1_Np1xD8gh1ubehP1sLFGGe-3M8UlMMz4qFX0LKgYBhEUNNHqrp5negOycJta19LtU8PAPo0Rneefo_sDMgCgAotTRydoXkZDXkkjJ2fL6xycuZJ2Q6mVlRDG-SZpS5Hu34ccLJp8l8tc2pKnNw8utWf9DEh5jsg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/50a90f4363.mp4?token=MoAUKnIk9Ppy7UPwN1-VPM9hruekC4dtSfJOY3aLJDjxr6yzDoGsAGiP3CDlucQuihPh_SI1WfWVtO_Ug58KtWzl1fHnmTnlNp_4cA9hbVhLRgBMzVSPup5739U0W0n0ZcRFbNQ1qgPB4yXFy-JX13wYxyTTju6gY-8AetNuhllgXIa_U58dDa1_Np1xD8gh1ubehP1sLFGGe-3M8UlMMz4qFX0LKgYBhEUNNHqrp5negOycJta19LtU8PAPo0Rneefo_sDMgCgAotTRydoXkZDXkkjJ2fL6xycuZJ2Q6mVlRDG-SZpS5Hu34ccLJp8l8tc2pKnNw8utWf9DEh5jsg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
هواشناسی: در ساعات بعدازظهر، بارش پراکنده و ضعیف همراه با رگبار و رعدوبرق در مناطقی از البرز، قزوین و تهران رخ می‌دهد
@Farsna</div>
<div class="tg-footer">👁️ 9.47K · <a href="https://t.me/farsna/467225" target="_blank">📅 08:33 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467224">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EQJDU6OvSdMp9hGF-47DwrIf2jtqd9lxm5pSZTjj7Vae_a_et1Z2Rjd0HrHWQLMXDZIXviad-wbICTduUTseApxZcj_74rHdjPEASgwQSKkBnEhEjcSuywJixGD2t4i3rkl1vfWKMDlmNP49xH_f4WMEseeFHAzyfiiZKOBA9mWccbWdQW88kd-U4w6sAxAZudl4hC6efOW1mvdcUNJ1M83GbCNU0IarJKv0QJlg1cARopY4BCo1raeHk02ROewoVUILCuE2HVPm-zbhSrbKT_BTQ69ysngkwJZ4PzlHJ0k1Ml8fGe1H5vZ0IAOI3sxbxj4YAUCqvMpv8Mv1KX31RQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پزشکیان در حاشیهٔ اجلاس سران کشورهای مستقل مشترک‌المنافع و اجلاس محیط زیستی دریای خزر در ترکمنستان، با نخست‌وزیر ارمنستان، دیدار و گفت‌وگو کرد.
@Farsna</div>
<div class="tg-footer">👁️ 9.71K · <a href="https://t.me/farsna/467224" target="_blank">📅 08:23 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467223">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">🎥
سلام بر تو ای وعدهٔ تخلف‌ناپذیر خداوند
!
@Farsna</div>
<div class="tg-footer">👁️ 9.12K · <a href="https://t.me/farsna/467223" target="_blank">📅 08:15 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467222">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">هوای تهران «قابل‌قبول» است
🔸
شاخص امروز کیفیت هوای پایتخت روی عدد ۷۷، و در وضعیت قابل‌قبول قرار دارد.
@Farsna</div>
<div class="tg-footer">👁️ 9.76K · <a href="https://t.me/farsna/467222" target="_blank">📅 07:46 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467216">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ZRYjaKiyiUsBchbTmhBuig8X69gDwWTnCgcnf6E2u7sAlOY4j-g-9V3veMF2B3UXiNXaVGRTENT4_xnfHhNHBH-TnA9A28JielCAXOQ-2Wsc5KFIVdkrW8nMP-GyrefHbF4LTyZiULWWHO4wyppgsE8bLRUW58CWDAc-8wsi-ad9WDZBjCPDVwrANro_l3wPjx8V1yWDOLXWMklQt1A-BquwDbhCyuidV8PNQfIXSmfS2PrU5qLlNm1i971gfREM-CJCR7Gwev78E7yNpzLwDL5h9Nhox8b2HOxe8vNyeem_3ZqDza5ZJKAQl4lpDUgUQ-kG3pa7Ss7Qxh4ZeTienQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/D7qneZVLNwtTFcQTrfEEeBzmfHTDA-dGyFXnNUDEpPLQv5LGOYKfOHrf7wMd048uAPglWlxcqh6W7nblIbrN7ZP_ANztUrowqxt4YjFJ-OHILcraQ8e3oEpN9C1bSq7mt-QDO5c_I_e1ayTiq1SD1bBQWaFCdxyUxOEbvtoWhAvl7jQPrOA10StlcRnL8_O1yTt2MZI0hbLsHC2u_u4n_qHD6ghTzB4__Qdt7VnxY42WPsNjTYUt7aumWo5sct0_08_bApKTvAWM8jnsFlvO_J0cEGi0hiZe3ClTUZUJnOIqtyd_Y_8RblPLSq3pW48sI5OWt737J1t7jhazRd54OA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ZJMjrCFsaDZkiGsacmPewb09g_xIp6XPtSw85A0VA902EJCkqv8jmXOGAuiUsq6ijBwcdyy4s7xJz-BbVAHsF26YGx7uLuG0NHjWGnyQ9mme_jqQwXb9zIEQSUBjhA1j0QyHuO2V1d8FeVC6JccSn8TqY3l4dTe-f4AQaYvxE-4HZHSHkaCCB5KXME7sMrBRxIaChN0PR9X3N47ReetXwmMskkIk_nWbNakxIVu-6SUkVO2nHkg4KBKgf_2R2XdrxP7FYTvAAYbdoNVg-RHB7mt1bfYLtv344IgM7BqlYg4v4TYWUDPURnGiXQQViZIz6g75Kc-GTWxy56kROjTWJA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/FZ97aO8vEKBAao2pdpb3qGNxHffCeRgJPMnJyYo_S5ZZ9UiYspgRM7eP0zZdjpxtNjwc3wshac94F3neIAV6dzyOrs4ZcY0TQEXtu9mq4QzzzSvWWd6YBk4FFjy5ABdC6SrmPkJsy8wz0vkw_gsu3UwjkzYrOKBHwFzRdKkMtedbKH2d86zIJ2Y4M3W5bZf_HKKcn33ueIWnzD8EtBB8XKlaA1RzocTv0sMq4wvFS4cDeM8U71yYkoI_E4wlJ1jrIhE2Pj7hOJDXV8Pl6CAoNMnbzGVkrjdtUIGKxDqQnHIfqL60sqqIxbZHDN_fnuHEglJhrh85tpXim8111LswLg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/mhZa0dHlnxKxSToY4AxYKV20dsGrnrqDLkjJ_c4LMJeXhukRNjHmLJupIw3oeV5xQJ313IzmR8qjw4X11j4-C5dJt_bTdw_i-3c-fJgAtzDvSyZy_ieM_31BHR5lMm3lJMr00EVQe__6p13ERkn8yeOxGzTxmHzd9_fRjFSHiTFhudExHLDRV_kJQ1DOz9xoEBS9jpU6X2GjNVxwOjNcyOF68FmD4TCjIWH1d4o_LYcyxU_suW5L2F68lYgC6t6MxktcFwWzDq6ObSHVMxcsMqZUbWzRwGNiY5JIqD-71nar9d8EmHqvzdPzKdLwYOBd4ehxApgTuyfoYePlsy_HPA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
جشن روز ملی کودک در ساحل بندرعباس
عکس:
معصومه کمالی
@Farsna</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/farsna/467216" target="_blank">📅 07:36 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467206">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">بازداشت دو نفر در انگلیس بعد از ورود به یک پایگاه آمریکا
🔹
پلیس انگلیس اعلام کرد دو مرد اهل لتونی پس از ورود به یک پایگاه هوایی مورد استفادهٔ نیروهای آمریکایی در شرق انگلیس بازداشت شده‌اند و تحقیقات دربارهٔ این حادثه ادامه دارد.
🔹
بازداشت این دو نفر چند هفته بعد از آن صورت می‌گیرد که پلیس انگلیس مدعی شد طرحی برای حمله به یکی دیگر از پایگاه‌های آمریکا در آن کشور را خنثی کرده است.
🔹
پلیس اعلام کرد تاکنون هیچ مدرکی به دست نیامده است که نشان دهد حادثهٔ پایگاه هوایی «مولزورث» در شرق انگلیس با طرح مشکوک علیه پایگاه «فررفورد» در غرب این کشور ارتباط دارد.
🔹
پایگاه هوایی مولزورث مورد استفاده نیروهای آمریکایی است و محل استقرار واحدهای تحلیل اطلاعاتی، مراکز فرماندهی و یک مرکز اطلاعاتی ناتو به شمار می‌رود. این پایگاه برای عملیات پروازی استفاده نمی‌شود.
🔹
ماه گذشته نیز انگلیس مدعی شد چند مرد را در ارتباط با طرحی مشکوک برای حمله به پایگاه هوایی فرفورد بازداشت کرده است. این پایگاه در حدود ۱۴۵ کیلومتری غرب لندن قرار دارد.
🔹
این حادثه نگرانی‌ها دربارهٔ امنیت پایگاه‌های نظامی بریتانیا، به‌ویژه تأسیساتی را که نیروهای آمریکایی از آنها استفاده می‌کنند، افزایش داد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.35K · <a href="https://t.me/farsna/467206" target="_blank">📅 07:19 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467205">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">🎥
شعرخوانی محمد رسولی در رواق دارالذکر، مزار رهبر شهید انقلاب
◾️
کسی که کُشت امام مارا، چرا نکُشیم؟!
◾️
که ننگ ماست، اگر قاتل تو را نکُشیم
@Farsna</div>
<div class="tg-footer">👁️ 8.89K · <a href="https://t.me/farsna/467205" target="_blank">📅 07:08 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467204">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">طوفان تهران ۱۰ پایتخت‌نشین را مصدوم کرد
🔹
اورژانس تهران: در پی حوادث جوی عصر روز گذشته ۱۰ نفر مصدوم شدند  پنج نفر به صورت سرپایی در محل درمان شدند، و پنج نفر دیگر برای ادامهٔ روند درمان به بیمارستان منتقل شدند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.36K · <a href="https://t.me/farsna/467204" target="_blank">📅 06:57 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467203">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dc21dfb31b.mp4?token=FdkVC_XDxCDwcpvBtifujkTZmrfrGVlf2JNa35DkwQDSU1qqef0v7O8FV7IoSbPtMJRFVKTEYcojt6c4O26-yqYM658dJiaUPgiTmxV_e8euU8QTrF__dpdwKbMvSfciePOEdtrA34tSYm5mcbR0WdvDlek8NmvVfLDHvmPI-Q4X754d9t5QLr1gLPx6bLCAnTVoXjna8MkDV7-flqKV6aorW352VbIvpPz5sAj6AwMP6KqUE1ICYGth0chhAjUpzD6S86Lk6srshHwJvQY0nV9rEWOKqBZGA6UC5vFebkyF-zrdafCPRplDBRrVim0lVVV5UEK-Q_dQmzCYFCoUrnCk7soMw8rOjvO3SV9DvJeWsrLNNrIH5Y0pmpZUQGBPquNpCTTJcXtsAzp5SgHc6-8VQsvNUTzQ10vbdeev91fw9w0ilodQ3T12KC0jAnCQB-oQBDyrC2XtfGUeQMXsqS4jOrAqpELyHFTcik9dpg0ho10242gRHebg0qREQHVDTIO1bBsnQPPRKk7MCLyT77kBCxpR7ozmyIc4Bxz_VUoos1qFZ63KCzVbWsDSxTqMqcAzD7RSKsb156U6RjTsh6lHU9roQ8pSwvXlSWp5-tIN373z4d7V5tWN-r932lahqfgI9kSdjkxggU4EWIJiR_aH9b62iwpLQYhnY97o5Zk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dc21dfb31b.mp4?token=FdkVC_XDxCDwcpvBtifujkTZmrfrGVlf2JNa35DkwQDSU1qqef0v7O8FV7IoSbPtMJRFVKTEYcojt6c4O26-yqYM658dJiaUPgiTmxV_e8euU8QTrF__dpdwKbMvSfciePOEdtrA34tSYm5mcbR0WdvDlek8NmvVfLDHvmPI-Q4X754d9t5QLr1gLPx6bLCAnTVoXjna8MkDV7-flqKV6aorW352VbIvpPz5sAj6AwMP6KqUE1ICYGth0chhAjUpzD6S86Lk6srshHwJvQY0nV9rEWOKqBZGA6UC5vFebkyF-zrdafCPRplDBRrVim0lVVV5UEK-Q_dQmzCYFCoUrnCk7soMw8rOjvO3SV9DvJeWsrLNNrIH5Y0pmpZUQGBPquNpCTTJcXtsAzp5SgHc6-8VQsvNUTzQ10vbdeev91fw9w0ilodQ3T12KC0jAnCQB-oQBDyrC2XtfGUeQMXsqS4jOrAqpELyHFTcik9dpg0ho10242gRHebg0qREQHVDTIO1bBsnQPPRKk7MCLyT77kBCxpR7ozmyIc4Bxz_VUoos1qFZ63KCzVbWsDSxTqMqcAzD7RSKsb156U6RjTsh6lHU9roQ8pSwvXlSWp5-tIN373z4d7V5tWN-r932lahqfgI9kSdjkxggU4EWIJiR_aH9b62iwpLQYhnY97o5Zk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
معاون نیروی دریایی سپاه: شناورهای متخلف در تنگهٔ هرمز هر شب تنبیه می‌شوند
🔹
نیروی دریایی سپاه از شب نخست جنگ تاکنون با اشراف کامل بر تنگهٔ هرمز، برای حفظ منافع ملت ایران عملیات انجام داده و این روند ادامه خواهد داشت.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.57K · <a href="https://t.me/farsna/467203" target="_blank">📅 06:48 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467197">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/liIPQBKiFiKT1-j-tV86jwmM4-05gnsYqfR49QqDW6Oi4otIJRIH9wN4awSAT3NUrrDFGeKMDmRDFyO2iB4a9AVcUurLonYIgpnE9bqvBTQVrjAwckHJjk_0RnBhLpdS8PhJOy1L5phbqkDdIYNDFCfPX26pNxLOIOLfywopowV_0zpQzb3vDQpruc-WtY8JgwE-EhFCg1dwPHelFZ7Rg73RoTb7tjVuvTqLgCSRgxKLOutat0REYFr4rjcVbgG6e6ovBQSBtlIvaqNXmfU2Jktn6JtMVCHM1_qWVlc_rRiHF5YLLZEavqcjrEdYvYHmTQ9b4YoP49GdaWw5mV5Y_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/JmAebVG21zlnZYqSWVqnjrhWpkO_RZTxlZEEQjyvk2-vd8TkF-Xr8N7f-nW-_81jukP6GAkLmDBv4vp90SgDxe5JfGhM2pro1rTM2Sz3TtcPnQHmNSGkm_wyObUKK1sKM84xdISJO4Ho-RwQlQfv_Gf4NpeIzN7ogS1jj5hFSz3SnL1dxkvgpJ0GRnoOH7C3RxTAP7xt_AIh5wP_SBPxLsDX2DrGvuXNM1_3PwexVRzNEP0JzM5vEMrBU4YeDaQzhW_ppTzUaCPro_oCOLuxF7qsY1KqT2b2eHIw-icSwyDGZNKbDwcRNXZLSLJANk-yzmCEFtmQ2N9QrP8X5bd-XA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/NONF3lbNDnT82gHGJLxg2xP79d7ql3dc2U4cpmnPPTzcCWJdagpZdl6IA1pNANtMTEmMgnfh2rRAbOrp5UNRuw-4slItifmjAZrG_PoBeAmve0R2TNKSQqkE2IW4uq_Iee6iwwvOHIBGwEzcCd5ieuK3aT1oWcJtG6h2jgE-kK4bJsPXBIbhiZpydTDQG7WeYJTZzFe6cz9VfeYw0RZT9jd0pxcqJA-D_7BlfbgTzuuCV89TZszC0TC326gJeUaIIW8SoN5XKbXoDfjhRQDXO79pRfnCjqGPJLUbyTMq-fkx4PH4LMLYFCSmV7KEhV2_jxaqb0WQdW3HbsLYDa0T_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/acXSbetXoVRVPB92EMYqlfA5eY0u56An_uw8or1p_tDNachaYSp_H9mzgCDBCtQt8S5kP-WJzldDKRxoecHDyqkSB18UmhRCEC-po4g9a_QG0P8GJ0ljx6gU8QxjLHEvpIFuopj_4ARd8shWfbRmpSp5sIHnvmXOgJZ8b7kLDE7xE3lMOYbs4hBfe26kS_6Ego0J6awW2ndBNFRIid5NV4k1vSAa7pmMYM3KvqM4FcU2w-X2IhYFvN9YKxlmUwditJg-6wZXemTfgSniWUGJR3jOs3wrx_Dky2qn_o3yzjddRl3c2DjWACbvtwThX9Wtps6khYPqNT-eU3l1m5PBJg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/nmyx7Lxo0OsLqLpz22QDi-7wsaNpZuIQGU9VNURowjt1UAC3bknItcf3jsPI9384qJ3uvzhP-wvxvvketldp0EBpLaycxignHFCyPe_YAFlYqzXbASQIeaIktCei5JOpHyNQyPY8jYcGYyLerGD2t9Prp7MnhbzvloqrHhSeGkkNayeIIUtqeHaWXykoCzDJjcNJ0XMTxIy68ppRPjRBW4UXW0p32ztO-z14riUvKgYMWypoHwMVYn5uGScg6tYu0raWGSs6T3Tl764pLb68Y_4fb2OzohjyT6_YnZsFZ9TCXLfpeUI9Cx20eWd5ohAeqv15dDkhy1G01woGoUGUUQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jIaRcDDAl6NN74C_Qcf-fkcQk4Bf6eJXR1Y_ZWjyDl9qe0I3898cWagFjBiNr4-la3nBlFIQUhTRqWtubMSMT-Avzmv0omeV8neUjk6P-x1dDbzFD4-SqP0_qLkcDE5bf0wruLLS0qfp75KXGN02svUifksEUDZmTgtZEoQ9qGfCXNdzZ10_lRZ7lzQ76VLfzkBpnQ0N39bCaFL10fuh2aKBAnsOAAQ5tefvWYxaj5Y6_lFbMNBzI3zI2MuRDbUpH1JnwsiFqRGFZ25Sezfc08GcR0su-DZL1vF8JikJLP6ocgZpgOwefd4zzd4bRZ_oAIOu-bCl3fxUJVudKjqJ7Q.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
جشن شکوفه‌های میناب در گلزار شهدای این شهر برگزار شد
عکاس:
عماد یگانه‌دوست
@Farsna</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/farsna/467197" target="_blank">📅 06:38 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467196">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">آموزش‌وپرورش برگزاری آزمون‌های «ماز» را تعلیق کرد
🔹
رئیس سازمان مدارس و مراکز غیردولتی: داشتن مجوز به معنای فعالیت بدون قید و شرط نیست و اگر تخلف مؤسسه «ماز» ادامه داشته باشد، پروندهٔ آن در شورای نظارت بررسی، و تصمیم نهایی دربارهٔ ادامهٔ فعالیتش اعلام خواهد شد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/farsna/467196" target="_blank">📅 06:08 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467195">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">🖼
تصاویری از هواپیمای منهدم‌شده عربستان در حملات یمن
🔹
درحالی‌که عربستان مدعی رهگیری موشک‌های یمنی است، تصاویر جدید انهدام یک فروند هواپیما در فرودگاه ملک‌خالد ریاض را نشان می‌دهد.
🔹
رویترز می‌گوید که این هوایپما در حملهٔ موشکی نیروهای مسلح یمن به فرودگاه…</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/farsna/467195" target="_blank">📅 05:47 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467194">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">هشدار استرالیا به شهروندانش در عربستان: از تأسیسات انرژی دور بمانید
🔹
استرالیا از شهروندان خود در عربستان سعودی خواست از پایگاه‌های نظامی و تأسیسات انرژی این کشور دور بمانند، و به آن‌ها دربارهٔ احتمال بسته شدن حریم هوایی و لغو پروازها هشدار داد.
@Farsna</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/farsna/467194" target="_blank">📅 04:38 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467193">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lwQyD-dWbDwB6uWwIz-PiSnhjz4EbMVW9BqqUifpsJEqDvEcpvGiSxjNEXqNunOtWhGcl0qlxV_RJTJ06nTCQEBfbMyBpCPB64w-zo4ijgwFjBxqvE6R-C9eG55eQfdtYfgVJB6FHzm_Z4MxbVI9IUOzNSibwunmunNX_wPFcG1nhWVNOU0py6mG_a6jEVB0SjWrM9S83D5a2kX8ljFABi3lQJ1nNW6eLyefUHwCNmFfUIoaHGstjvsCAawOW_IUiz99UbdaGESrMoUj4_CH-sMdPAhajDdVk_ZWi2HuUc63L_wwODHCG9hSY2Z7Ihs-a6VMSw-Tb4V8qKODAhcryA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تهرانی‌ها برای خرید از طرح «تورم صفر»، در سامانهٔ شهرزاد احراز هویت کنند
🔹
شهرداری تهران: شهروندان پس از ثبت‌نام و احراز هویت در سامانهٔ شهرزاد می‌توانند خرید و پرداخت خود را انجام دهند و کد رهگیری دریافت کنند. خریدها با پیک یا به‌صورت حضوری از میادین منتخب تحویل می‌شود.
🔹
همچنین امکان خرید حضوری از غرفه‌های متصل به شهرزاد با کد ملی سرپرست خانوار وجود دارد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/farsna/467193" target="_blank">📅 03:58 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467192">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس معارف</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e0567dd374.mp4?token=lf0OANGaeqbbTnTeIrNRNh7oNWRolxYmwsakA-wgBnzkyZzkVkwjRnr7IbZ-wA4naWM9hYHU2am5Kl5WcM3hSHcfstblhw_x4N6mtJtW713nzcEVfMwbiPIpen4FqLBqBxvFd3BfhPudRGwX7Wdrx_T79DycyvCtHAMJTTgsO90cFB4qNr3UMnb2EToiAuuC8vnUQzm88YwOEGP-2RVLp_n5mp104aLPJckxMO5eC8IGcXUXRFknYYDetu--b4juwt-k8Sxn0ZjIsC39Cxng7VWZbvLeEIYav8h9KaYAkMVEyL4TdY2MMSsJSRPivW2EnuD1WNRRwiABX4FRUKBlCA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e0567dd374.mp4?token=lf0OANGaeqbbTnTeIrNRNh7oNWRolxYmwsakA-wgBnzkyZzkVkwjRnr7IbZ-wA4naWM9hYHU2am5Kl5WcM3hSHcfstblhw_x4N6mtJtW713nzcEVfMwbiPIpen4FqLBqBxvFd3BfhPudRGwX7Wdrx_T79DycyvCtHAMJTTgsO90cFB4qNr3UMnb2EToiAuuC8vnUQzm88YwOEGP-2RVLp_n5mp104aLPJckxMO5eC8IGcXUXRFknYYDetu--b4juwt-k8Sxn0ZjIsC39Cxng7VWZbvLeEIYav8h9KaYAkMVEyL4TdY2MMSsJSRPivW2EnuD1WNRRwiABX4FRUKBlCA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
این‌طور به فرزندت نماز را بیاموز
🎙
آیت‌الله مجتبی تهرانی
@FarsMaaref
💠</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/farsna/467192" target="_blank">📅 03:31 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467191">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">حملات هوایی عربستان به دو کارخانه در صنعا
🔹
شبکهٔ المیادین به‌نقل از منابع یمنی از حملات هوایی عربستان سعودی به دو کارخانه در شمال و شمال‌غرب صنعا، پایتخت یمن، خبر داد.
🔹
به گزارش رسانه‌های یمنی، یکی از حملات کارخانهٔ تولید اسفنج در شمال‌غرب صنعا را هدف قرار داد.
🔹
حملهٔ دیگری نیز یک کارخانهٔ فعال در زمینهٔ تولید مصالح ساختمانی و تجهیزات برق در شمال صنعا را هدف قرار داد.
@Farsna</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/farsna/467191" target="_blank">📅 03:12 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467190">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YhjNwJ7m-v9K2s0zECZmCOfBvJkD96fAj2gZgJW_odEinsjnJe_wLIIn0-YXYruPBx4Y3xC1Mjc-qohDd7ug1A6KP6Dn4uX_WXJFmxMcU3nf0ZTJ1D8LyxnxpsgGX0uhzZWkDTpBs3p3EnOR-OuKjsbBVMV8FxYqLQwOJcx9wL0wrtG7tDxMnNUMHmaKupoppdsIlUkgAVmoKExdS2oW6ndtDtqB5VsyPkAx5bk76w7b-NZ0AY2kQlmtAwesKVAf6EsxLPdurfFsC537nmWR33QnzeJ0W8Q3-qUP01j12dUn-HWQQuBE8PqlHbL7B00qZcEAVooGZEnJessuH_A6KA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پنهان‌کاری جنگی آمریکا؛ وزارت جنگ آمریکا کریس مورفی را به العدید راه نداد
🔹
کریس مورفی، سناتور دموکرات آمریکایی گفت وزارت دفاع آمریکا در جریان سفرش به خاورمیانه مانع دسترسی او به یکی از پایگاه‌های مهم نظامی آمریکا در قطر شده است.
🔹
او این اقدام را بخشی از…</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/farsna/467190" target="_blank">📅 02:57 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467189">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Sip44mWBuXlFwGJkTbC05UrJFcrJw1EbF_fxDgQDXl1qStWoKU6IIY41picJuThenzIl9DX8cuXzvPjXesudvvYVe0-qblfi9tjlBzrrS0TahAEroIXAz9ybjoaf6_VRbEEUDnDvxLfgK427I_YQnjnOnUcsUGm3b51yEqGBzY4xA7P5Ro7veHWZA4nqG7M-Hm4BXP8PEalDC_TrDBv9wjKQxQhMGFvq4dkSmGLhQxTbAliCNin_UiH-aIsznI7DlOSBE5BXas5SSINMTLPffRIX68_jkxUzmyKOU0LJ1HJ10sRcsGVVxM-HT5iqGL7zBbRv4qA7y6URuU-vmFRQbg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یحیی سریع: به فرودگاه‌های عربستان حمله کردیم
🔹
سرتیپ یحیی سریع، سخنگوی نیروهای مسلح یمن اعلام کرد شامگاه امروز پنجشنبه فرودگاه ملک خالد در ریاض با دو موشک کروز و فرودگاه نجران و پایگاه هوایی خمیس مشیط هم با موشک‌های بالستیک مورد اصابت دقیق و مستقیم قرار گرفت.…</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/farsna/467189" target="_blank">📅 02:42 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467188">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/830f231c18.mp4?token=F3LPXmqAX2f0n0G79iO1ChZv9KCmc6Gg2hY9VSlQtg-JFLzL_7cmAkoCMqeZ8cghfbIHB4d9Jg16sWssv1I_Y6PMLe9Pk-ScFwZSGa2G3cscXsuWqYdseASOMOiDZHXOcfmL7BiNssNkmREGn8WKZ6QMClz0l6MSrmMJkRZhH9qUCdz3Qi9oP4QWpOnE3AL0aSPHVQ6AqSyAwkjDW75ZPdyVpXTOtgwTI9_573HkmdRZt78ylCXzCA4c9W3dLzCuPkSnnXzlL_1O24r4ltqqpSPbtjBzWwayp40OiT1eJlVpIDzgXaKzABhh_gj4_A_5XAN3FWG7qg2ftcQ7AkMjq7KwB1DpH_GPJGRYZPbMtyhFcvXwP5oAkszOf44nCIBGsNPAx2bSUg6z0pStFqLbmEkubqgkl17tP2rjPaGFFTe0TKQT84Kr3kxmZEYCm0EolFZtPJcUPxDkztpJDyBsFeg_VG0oZ-EkCaHMjEsRP7V3_gO4nndzIt5SGNk2PFRLbBzafhPPLV0rN_wBCZs1wyHrRRiUWSgzolKxnp7hBWak8lTu15BYt8FWYu-FPr9feDOHRABhiqSpD8txXml11cU2Bjpq-yeOQZEzgjUc8fz_ciXbZ5XypRhjvuuT-Wh2oA7qAiDrWjlQ6LxFER1ZbYS3kF7SeA0N1RsoqfDl8cg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/830f231c18.mp4?token=F3LPXmqAX2f0n0G79iO1ChZv9KCmc6Gg2hY9VSlQtg-JFLzL_7cmAkoCMqeZ8cghfbIHB4d9Jg16sWssv1I_Y6PMLe9Pk-ScFwZSGa2G3cscXsuWqYdseASOMOiDZHXOcfmL7BiNssNkmREGn8WKZ6QMClz0l6MSrmMJkRZhH9qUCdz3Qi9oP4QWpOnE3AL0aSPHVQ6AqSyAwkjDW75ZPdyVpXTOtgwTI9_573HkmdRZt78ylCXzCA4c9W3dLzCuPkSnnXzlL_1O24r4ltqqpSPbtjBzWwayp40OiT1eJlVpIDzgXaKzABhh_gj4_A_5XAN3FWG7qg2ftcQ7AkMjq7KwB1DpH_GPJGRYZPbMtyhFcvXwP5oAkszOf44nCIBGsNPAx2bSUg6z0pStFqLbmEkubqgkl17tP2rjPaGFFTe0TKQT84Kr3kxmZEYCm0EolFZtPJcUPxDkztpJDyBsFeg_VG0oZ-EkCaHMjEsRP7V3_gO4nndzIt5SGNk2PFRLbBzafhPPLV0rN_wBCZs1wyHrRRiUWSgzolKxnp7hBWak8lTu15BYt8FWYu-FPr9feDOHRABhiqSpD8txXml11cU2Bjpq-yeOQZEzgjUc8fz_ciXbZ5XypRhjvuuT-Wh2oA7qAiDrWjlQ6LxFER1ZbYS3kF7SeA0N1RsoqfDl8cg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
عربستان برای جبران شکست‌های خود، به دروغ‌های رسانه‌ای رو آورد
🔹
سلطان سدح، خبرنگار جبههٔ مقاومت در یمن: عربستان برای جبران شکست‌های خود در برابر انصارالله، به‌دنبال رسیدن به پیروزی در رسانه‌هاست.
🔹
العربیه و الجزیره به‌طور گسترده دروغ‌های عربستان را پوشش…</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/farsna/467188" target="_blank">📅 02:28 · 17 Mehr 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>

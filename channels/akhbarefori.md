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
<img src="https://cdn4.telesco.pe/file/t_r6O36fvFxyDz1cSWQQxM_R963RZymQu0Y3nFYBC1MGGWfwTroQzz9pkWk54W8-us6MEe7uNk_jdvNKj9sbMlswZYFQk6McxvosjumEPRuXpL2y7_awoYQGVfzkGxolqzCqHwPcLFMhsZGtH8Erh8jW0Ji3wx2bCFlk8_BhEnaondz4Aqfa3tsZlkhwslWzCq-HUX0RjTjV0wOidraFWH1DvfzsInd9KBvxK9P9DUJFG908oSlXjTL7phDeJ4uJT0TjRDnIn12qWX-ZG09JA95LwQRjC9gtlxfcNxp_6Shm2RyLh3zCIA_JIV-k_RNk3B9C3s6zHY7pfFe0l3clnQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرفوری</h1>
<p>@akhbarefori • 👥 4.24M عضو</p>
<a href="https://t.me/akhbarefori" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ﷽تبلیغ درکانال خبرفوری@ads_foriارتباط مستقیم با ادمین تبلیغ@newsadminجهت رزرو تبلیغ تماس بگیرید. 09018373801؛ارتباط با ما@Ertebat_baforiiتبلیغ در ۳۰۰کانال تلگرام@Maino_marketer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-06 21:36:08</div>
<hr>

<div class="tg-post" id="msg-664015">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KXymGruTvu9XBv0tw3SnjJLBiEmRKeaSu8xh9gtLi1Qd6X_X_yLKTFpYNX_8r7O2-26KaPtZJOKZYFeoDAq9BTWCpKo0Nq5Vu6miwKGeI7UqA67n_RCFxMYTRUlskihvtgIfyNhtBjMG_LnYJRngZBgz7jUPsRmkE43GYa6-7kgquO1mNligNMYoPfx9wRMpjtz7H3xyMp8Bs8f-PWRa2hpeS788KfuAlKLvFJvhcsUQ-Xwrw4ymzcCw3P2QMGTAk-3oS5Ni7sJ45bbPFhZk77y9u9J4oJwhS4wxm4Mrd3sbBWeF4Pr_6c4SQ7jF5GtqitENwS85xbANjZYT3Kltqg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
نتانیاهو در سایه سکوت خفت بار مقامات لبنانی، رسماً اشغال خاک لبنان را کلید زد
🔹
نخست‌وزیر رژیم صهیونیستی در یک کنفرانس خبری با نمایش نقشه‌ای از مناطق جنوب لبنان، مدعی شد با مقامات دولت لبنان درباره حضور و اشغال بخش‌هایی از خاک این کشور به توافق رسیده است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 5.36K · <a href="https://t.me/akhbarefori/664015" target="_blank">📅 21:31 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664014">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">♦️
ونس مدعی شد: مذاکرات با ایران موفقیت‌آمیز بوده است
ادعای معاون رئیس‌جمهور آمریکا:
🔹
اگر با ایران به توافق نهایی برسیم، عالی می‌شود.
🔹
افزایش جریان نفت از طریق تنگه هرمز نشانه‌ای از وقوع یک اتفاق واقعی است، اما توافق آتش‌بس با ایران همیشه کمی آشفته خواهد بود.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/akhbarefori/664014" target="_blank">📅 21:27 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664013">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">♦️
انفجار و تیراندازی نزدیک یک مرکز امنیتی در کراچی پاکستان
🔹
رسانه ها از وقوع انفجار و تیراندازی نزدیک یک مرکز امنیتی در کراچی پاکستان خبر داده و اعلام کردند که درگیری‌ها ادامه دارد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/akhbarefori/664013" target="_blank">📅 21:24 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664012">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bc606f8ae6.mp4?token=HeS1oXgg6dlZwDy8OZ-KHdcaDWc5tSMpHvsk0_N1OVqBYeh67QBPTOrioeqXQOR5AD5iLr3amFwge7CROIqCrTqF1DCFDhHYIRIKmoRPw0ecCpP-zMqjpPqhswf2xfNkU3HzEDmFr-NtWqhw7bUs1YuHdr9AzXARSvRyK5ZrlPH17M8zcQt87nRhMf-qmCKGvfY_qWlzWO8WH613uDLPzyiSvS9kKWGd9OmoE9Fxg0d0ol-scZCC8nb_0RivwBMJfYM3jI7wDVK9VnPijLvyUoMuV9FmVuSxDavpGegLY136dMLWyMAMy4jC3FRCttgNNjp0Ya9TzgaX25vGjHmin79VvmJ3gkmi0t87hMc57EYlKQb6QX8SHz6cZvA5Z90GyOSW4iJwL70c0WUZtYH7mKevgafFLnyVS3WRwROh5nRxDuXpfvqcITVyC-dANFLsK4Zm-uxmyA846atsRpBDv7puPvXc0eN0jUJCVURmQ9bFRLgaLylM7YGjbdyETs-LOnDJV0Ok4FcnW5FZ3cZuVNQqwRY7HE5Wam-JYk8Ae3-5CTqKvvZ4zokaYu9LzEdF_XCRp68HkjkttQjGgCqoDTPSG4vkns7MsODhdqccJjrBMArbo-KOB6Y0N4H_Tj8BR32MhLqHewtTxlrZL-VU4eIOvezEP2DV8e4M3v3FlcA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bc606f8ae6.mp4?token=HeS1oXgg6dlZwDy8OZ-KHdcaDWc5tSMpHvsk0_N1OVqBYeh67QBPTOrioeqXQOR5AD5iLr3amFwge7CROIqCrTqF1DCFDhHYIRIKmoRPw0ecCpP-zMqjpPqhswf2xfNkU3HzEDmFr-NtWqhw7bUs1YuHdr9AzXARSvRyK5ZrlPH17M8zcQt87nRhMf-qmCKGvfY_qWlzWO8WH613uDLPzyiSvS9kKWGd9OmoE9Fxg0d0ol-scZCC8nb_0RivwBMJfYM3jI7wDVK9VnPijLvyUoMuV9FmVuSxDavpGegLY136dMLWyMAMy4jC3FRCttgNNjp0Ya9TzgaX25vGjHmin79VvmJ3gkmi0t87hMc57EYlKQb6QX8SHz6cZvA5Z90GyOSW4iJwL70c0WUZtYH7mKevgafFLnyVS3WRwROh5nRxDuXpfvqcITVyC-dANFLsK4Zm-uxmyA846atsRpBDv7puPvXc0eN0jUJCVURmQ9bFRLgaLylM7YGjbdyETs-LOnDJV0Ok4FcnW5FZ3cZuVNQqwRY7HE5Wam-JYk8Ae3-5CTqKvvZ4zokaYu9LzEdF_XCRp68HkjkttQjGgCqoDTPSG4vkns7MsODhdqccJjrBMArbo-KOB6Y0N4H_Tj8BR32MhLqHewtTxlrZL-VU4eIOvezEP2DV8e4M3v3FlcA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">💢
حفظ یکساله و دوساله قرآن کریم به صورت رایگان
✅
ویژه دختران و پسران۱۴ تا ۲۲
🔹
اعتکاف با قرآن در جوار حرم مطهر امام رضا علیه السلام
🔹
اطلاعات بیشتر در
👇
http://Samenoon.com
https://eitaa.com/samenalhojajj</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/akhbarefori/664012" target="_blank">📅 21:23 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664010">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">♦️
ایرنا بررسی کرد؛ عدم پرداخت حق عائله‌مندی به همسران بازمانده تک‌نفره، ناشی از قانون است
🔹
عدم پرداخت حق عائله‌مندی به برخی همسران بازمانده تک‌نفره مستمری‌بگیر، این روزها به یکی از مطالبات مطرح‌شده از سوی این گروه تبدیل شده است.
بر اساس گزارش ایرنا، عدم پرداخت حق عائله‌مندی به همسران بازمانده تک‌نفره ناشی از چارچوب قانونی موجود است.
🔹
طبق اعلام سازمان تأمین اجتماعی، این سازمان صرفاً مجری قوانین است و تنها می‌تواند مزایایی را پرداخت کند که در قانون برای آن پیش‌بینی شده باشد. در قوانین فعلی، برای همسران بازمانده تک‌نفره تنها مستمری بازماندگان در نظر گرفته شده و کمک‌هزینه عائله‌مندی جزو این مزایا نیست.
🔹
بنابراین، در صورت طرح و تصویب اصلاحات قانونی، امکان بازنگری در این موضوع وجود خواهد داشت.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/akhbarefori/664010" target="_blank">📅 21:20 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664009">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e32efcfdfc.mp4?token=kbD-khz2CxUMXkVaFqCeGDl10KYWGwC32tuBedT_HBogUUcHmCQKuwH66-cPZ7s95MXYQ2LVoGYn0SEHrFveriAZUTO62DlryZrml5xP4WcKII7_WEGo1J4f0eMaNv_KIG0pp75eaR35c_y5HMoLqgz2Xnn0VSit_AGEVD-gVMftK2BjmoMV6CUGRGhQuXBY_nwvnjqLAvFVM73rUGnioLXsLN6Q3dt5hYinvT9YT1Brb1ZosW5qXegA7nSIK5fZ4YRWGx2XT6GwWKQTpEqk2vjtcd0rk_rudCMNCTQc2cQJ62RB5OaSu4Cjyu8tY2weKOD65osKRoQt-rYfhUjc4A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e32efcfdfc.mp4?token=kbD-khz2CxUMXkVaFqCeGDl10KYWGwC32tuBedT_HBogUUcHmCQKuwH66-cPZ7s95MXYQ2LVoGYn0SEHrFveriAZUTO62DlryZrml5xP4WcKII7_WEGo1J4f0eMaNv_KIG0pp75eaR35c_y5HMoLqgz2Xnn0VSit_AGEVD-gVMftK2BjmoMV6CUGRGhQuXBY_nwvnjqLAvFVM73rUGnioLXsLN6Q3dt5hYinvT9YT1Brb1ZosW5qXegA7nSIK5fZ4YRWGx2XT6GwWKQTpEqk2vjtcd0rk_rudCMNCTQc2cQJ62RB5OaSu4Cjyu8tY2weKOD65osKRoQt-rYfhUjc4A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تاکر کارلسون: هیچ گزارش اطلاعاتی از نزدیک بودن ایران به ساخت سلاح هسته‌ای وجود نداشت و این ادعا از سوی رژیم صهیونیستی مطرح شده بود
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/akhbarefori/664009" target="_blank">📅 21:14 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664008">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AtJp1jnohHmIswdUJ9N6PEOkKMmzUbeJb--d5yMNSX6GI7OVb7858DwaJ1tZnvmQ5pvSqyuB4xkjTuk5VshjdNIf-jyc_mZaRj8kWjpCaNKMphHT32XfXeZywgzVYZL1MNbNwkaMHTtc3WlQNa7-7tRwtxXMjuXy3Hfy-2MGPJmpOEoKMp6xGq5b3UU0jtKQxzjlRf89uve-RGt5th2FQ5xMZp22W3zxZJ4-P5citlR6yI0Qks18Jy2CZBEJsTQiqeScTyu2IUaPdbcxZZLCIAtPKQb_ziJoJq3vBv1L8kqqpbIcqgWm70gm3jJYOe3tXCHyMrctes39bllHFqC-vg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
خیز مرد شیعه برای شکست ترامپ و دار و دسته اش/ ممدانی، آماده جنگ با مرد مو زرد
🔹
جرات و شجاعت جمهوری خواهان در انتخابات 2016 سبب شد که ترامپ به قدرت برسد و حزب جمهوری خواه یک پوست اندازی مناسب کند. دموکرات ها از این پوست اندازی ترسیدند و به همین دلیل، انتخابات 2024 را هم علی رغم تمایل کمرنگ هریس به سوسیالیسم، باختند.
در خبرفوری بخوانید
👇
khabarfoori.com/fa/tiny/news-3226025</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/akhbarefori/664008" target="_blank">📅 21:09 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664007">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/c05CjH-u72dD8XGPrlfYrOfsP_mLyA9_eGk9NqKSUUYtUnyWQcQcEljOY18-wSNzuo7nt_Y0unx5K2IdGxV7x6B67ibU5HR6PI5FBXqIScwWXIN9gcI3hNd-OzivNUN_SPta-MuomyYeP50N2hJ2uVC8QXhKxQxOhWgYBd5ddqvJQG01f4ULLxDwzRXxJ5bf2XkU7YWAzZTOfJWUdrVPbX5rSrb-7-XDn7L2w4i3zcy3vWBTLCxO9lDeo1b81PSvVHFDFeISXsb-68-BWXgfV1ZTzUYzgG3x1AcrSzHxwdMYeJNJjLoMcwuQsLIaB43e9-v4L8c-GEZJnRv1GkT0Aw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
رونمایی از استوک‌های جدید نایکی کریستیانو رونالدو
#جام_تایم۲۶
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/akhbarefori/664007" target="_blank">📅 21:09 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664006">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">♦️
۱۰۰۰ مدرسه تهران آماده اسکان زائران رهبر شهید  وزارت آموزش‌وپرورش:
🔹
بیش از هزار مدرسه در تهران برای اسکان زائران آماده شده است.
🔹
زائران بر اساس تقسیم‌بندی ستاد برگزاری مراسم به مراکز اسکان هدایت می‌شوند. #بدرقه_یار   #اخبار_تهران در فضای مجازی
👇
@akhbartehran</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/akhbarefori/664006" target="_blank">📅 21:07 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664005">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KOf1asrHyrOBTn6Ovc26_MxpYxQ0Z88VT0f1IgN6RDwrGhoIjm9kYuDKQ-my877iXj4-zQgItMJsvoTUliQKxI_C5GbwGxFa48ESk3CI9xLcWR9FubU4cPHtjRSa0XkCTK26Qkf126SkLjJaKi-QHzB4PDwJk2Ko-Z8sYzpDIZXz_zI8E5_EYvpPnJbbhHVb4DSEYS7SElGAjmTyLvtqIsEFzNpUuOP9olgxTe_URcSrvRjB8NArHJXUqjokDN6uJh7v6o-wp0dYBdDWE_cX-bDNt4gvyHunCc7vNRCYNFmG0S02ocdL9-pcnQC1MRZApkF3WtfC0CHaM4r77A7OGQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
معرفی سریال: سوپرانز ۱۹۹۹ـ۲۰۰۷| ( The  Sopranos)
🔹
ژانر: کمدی سیاه، درام مافیایی
🔹
امتیاز (IMDb): ۹.۲
🔹
خلاصه: رئیس قدرتمند مافیا، کسی که همه از او حساب می‌برند، ناگهان خودش را روی مبل یک روان‌درمانگر می‌بیند. سوپرانوز از همین نقطه شروع می‌شود؛ جایی که قدرت، خانواده، خشونت و روان انسان در هم گره می‌خورند و سریالی می‌سازند که به عقیده بسیاری همچنان بهترین سریال تاریخ است.
🔹
۶ فصلی
#فوری_فیلم
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/akhbarefori/664005" target="_blank">📅 21:04 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664004">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromآمارفکت</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/W_i-wRWQCSttOXGZ9HYTjoQsPL7AVHXhAQBFbaY7qkxEUN1gN1czXeEvKVC7QewDlEzmtAE1KKi8LddQWXvGJ4qd07h0W-PYfpAyVQ8h7dSYJWTh0omy9NblDN4qfc37bkP-iiLMTDegvl1RFJ3zrPY-WtEPIXustE63ANrMl7QtR_E34j1rPIvzQYerlh37-l4V_FIrAoEx7ei1IGC6J-FxtplYTV7PcELF7AVe4uzsoUF1oUWptQmuGt7L4jWkGQFxJ-7gfN6iMOxteTOoayFPBIknr07Ms7RCX9ZASLLw3BCRX34AE4_53wAOts9g3OUH0Le5zZxv2KAXDAQKjA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هیئت‌های محلی در صدر انتخاب‌های عزاداری محرم
🔸
در این نظرسنجی بیش از ۳۸ هزار نفر شرکت کردند که سهم روبیکا ۵۴٪، بله حدود ۳۳٪ و تلگرام ۱۳٪ بوده است.
🔸
حدود ۸۳٪ شرکت‌کنندگان در عزاداری محرم شرکت می‌کنند و ۱۷٪ هم شرکت نمی‌کنند.
🔸
بیش از نیمی از شرکت‌کنندگان برای شرکت در عزاداری محرم، هیئت‌های محلی و حدود ۱۸٪ هم تلویزیون را ترجیح می‌دهند.
@amarfact</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/akhbarefori/664004" target="_blank">📅 21:02 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664003">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">♦️
برخی خبرگزاری‌ها از قطعی برق بیشتر منطقه پیروزی تهران اطلاع می‌دهند
🔹
مشکل فنی در یکی از پست‌های ۲۳٠ شرق تهران علت قطعی برق است
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/akhbarefori/664003" target="_blank">📅 20:57 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664002">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/82f64a18e0.mp4?token=G3XXLWfea5mxquD3nlfSnRuqxxCkebDZ2zf4LO7AuFxGctNLYa0MLEWtosoGYcPE_D90ZvmaM9nVPjI0y2ogFcBPRk_3PXJySFOrHEkhjXN4J2B0E2Pt9sKUyiH4sx8LIyYU-59GDJc80D31sAshG1r50DhSjl0JVMtHt-R69Xtp4b9r2nnmIvN6Qklp7WCBMl3BvMUtfnLS2oRrmXqQag0H8rCKUG1N8m4cwnnAjGChqe1_scv5ge7lbMYwclH5ZUI4sTWnHWELd-sYadqMZ0wWsyHLK6qD-aSwYzAVeOZMdeS0NmMDyKKgNi5por3f_GczJ7GP1oyxrjOKyo1vwgWJYXbX5KqVZhj-qjL8kemoTd3TA8mkgPLxZWn5XCpemcfN-4QQNg6XQMSOFMHIRSrLLe-WphOdLHeHj09iZc3JcWWjWox3l-FdLhDatlxnLXbNF7dl5rGaMadeGA0rQzG135pB-Z9oTtn1bF19waMmCvW8wT8_q4BQJSejC4YHlnvncmN6bi9A8Fic_TyJeTbzJDDU0-5bl1r3lozgB9vBpmpeyq-wY7LjISY8Nsdg3bpMClO6IUGaZr9rDoiDgFuKxCq2pzEvqyOeUunurrfxb7w-tXbcOIOUhe2odN8PxXLSsFcP5qyl9b8UBPXnykOsd_Od6KdH0F6m-mFqpFQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/82f64a18e0.mp4?token=G3XXLWfea5mxquD3nlfSnRuqxxCkebDZ2zf4LO7AuFxGctNLYa0MLEWtosoGYcPE_D90ZvmaM9nVPjI0y2ogFcBPRk_3PXJySFOrHEkhjXN4J2B0E2Pt9sKUyiH4sx8LIyYU-59GDJc80D31sAshG1r50DhSjl0JVMtHt-R69Xtp4b9r2nnmIvN6Qklp7WCBMl3BvMUtfnLS2oRrmXqQag0H8rCKUG1N8m4cwnnAjGChqe1_scv5ge7lbMYwclH5ZUI4sTWnHWELd-sYadqMZ0wWsyHLK6qD-aSwYzAVeOZMdeS0NmMDyKKgNi5por3f_GczJ7GP1oyxrjOKyo1vwgWJYXbX5KqVZhj-qjL8kemoTd3TA8mkgPLxZWn5XCpemcfN-4QQNg6XQMSOFMHIRSrLLe-WphOdLHeHj09iZc3JcWWjWox3l-FdLhDatlxnLXbNF7dl5rGaMadeGA0rQzG135pB-Z9oTtn1bF19waMmCvW8wT8_q4BQJSejC4YHlnvncmN6bi9A8Fic_TyJeTbzJDDU0-5bl1r3lozgB9vBpmpeyq-wY7LjISY8Nsdg3bpMClO6IUGaZr9rDoiDgFuKxCq2pzEvqyOeUunurrfxb7w-tXbcOIOUhe2odN8PxXLSsFcP5qyl9b8UBPXnykOsd_Od6KdH0F6m-mFqpFQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
آخرین اخبار و حواشی جام جهانی ۲۰۲۶
#جام_تایم۲۶
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/akhbarefori/664002" target="_blank">📅 20:54 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664001">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">♦️
فرانسه: ما آماده‌ایم تا در اجرای توافق‌نامه چارچوب بین لبنان و اسرائیل مشارکت کنیم؛ این توافق باید عقب‌نشینی نیروهای صهیونیستی منجر شد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/akhbarefori/664001" target="_blank">📅 20:51 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664000">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">♦️
مردم نگران پیامدهای اختلال‌ اخیر بانکی نباشند   بانک مرکزی:
🔹
در پی اختلال‌ ایجادشده در بخشی از خدمات بانکی، بانک مرکزی از نخستین ساعات وقوع این شرایط، موضوع آثار ناشی از این اختلال‌ در امور جاری مردم و فعالان اقتصادی را در دست بررسی قرار داده است و حمایت…</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/akhbarefori/664000" target="_blank">📅 20:42 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663999">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gUbnSg-HapVr_Uru3ulYxx1MN39L5uLQHHTzqakVCRUUB7Fu_1iz-kRz6sJqwl8DNCUHcNmJfw_GHMgHYHgYgd8F7EsbvFX5vMLMiCgFELomMAlIxVf3HHXvaITPP_bfybN_al9PZvt9Z4af2QtY0EORufTK45HRuXANbCHq7ZMg8RFcCbbq1LKB_vP1BbtOp0QcTvNYTIYg2-tymN0T0NV6kHcUlUOfhXTb5fnQ1fQNpxNY0L4Ay0cou5BAwO4ih6igfECF5ydoHKi4QSf8hYDCEEFUBu_RQXA_n_UdaZ4VzY3WU7dl1ULWLDTdtBsiEwuf9UFg4nMcPmMoxivAAg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
مصر مادر دنیاست و ایران غرور دنیا
🔹
نوشته امروز یک شهروند مصری در سیاتل
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/akhbarefori/663999" target="_blank">📅 20:34 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663998">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">♦️
روایت تکان‌دهنده یک تجربه نزدیک به مرگ؛ ادعای سفر تا آسمان پنجم و بازگشت به زندگی
🔹
00:05:30 رنگ آسمان دگرگون شد و آوای آشنا خبر از مرگ داد
🔹
00:23:20 دعوت شدن به آسمان هفتم برای ملاقات با پروردگار
🔹
00:30:50 جوان ظاهر شدن روح پیرمرد در عالم برزخ بعد از مرگ
🔹
00:41:45 خبررسانی از درگذشت فرد آشنا در بازگشت از کما و صحت‌سنجی آن توسط خانواده
🔹
00:45:35 متوسل شدن به حضرت ابالفضل در زمین و آسمان
🔹
00:57:00 عدم اجازه ورود جبرئیل به آسمان هفتم
🔹
01:03:00 محدودیت‌های دنیایی انسان در مقایسه با عالم برزخ
🔹
قسمت بیست‌وسوم (وقت رفتن)، فصل چهارم
🔹
#تجربه‌گر
: حسن‌رضا هادی‌زاده
#زندگی_پس_از_زندگی
#فصل_چهارم
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/akhbarefori/663998" target="_blank">📅 20:34 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663997">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e70efb8d7c.mp4?token=sFUNz33jC-VCyxvi1BK5qDXzblp8dzk1Aq6UT2rhUOGNULdkRX80MEpjHeHrc33DVYDKPX_Yr5BvduRCdl4oKp8Anl6LaxOdkeNDefUqdJxKSmdnDTQEgW4VYMG2UaBeVvKHkSTDjN_T85CvErfLd1fiZPTFFiqtAZANx1F_3Lr5jIdhBHOpgJe4PqCw77fqqXnDl7M5MeVfQZMrY5d1J93fesMyjC-cXxEql3MWVJs6dT4cByCNNNVns7g5MNdJHWqf1wntBiqYjM1z1QkBPCwNOFXS7d0vkmYXPVh6c4ygH2JDeaS7QIlmfFyoeOYiLZz2HbaHwnFyAxCnxdZ7aA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e70efb8d7c.mp4?token=sFUNz33jC-VCyxvi1BK5qDXzblp8dzk1Aq6UT2rhUOGNULdkRX80MEpjHeHrc33DVYDKPX_Yr5BvduRCdl4oKp8Anl6LaxOdkeNDefUqdJxKSmdnDTQEgW4VYMG2UaBeVvKHkSTDjN_T85CvErfLd1fiZPTFFiqtAZANx1F_3Lr5jIdhBHOpgJe4PqCw77fqqXnDl7M5MeVfQZMrY5d1J93fesMyjC-cXxEql3MWVJs6dT4cByCNNNVns7g5MNdJHWqf1wntBiqYjM1z1QkBPCwNOFXS7d0vkmYXPVh6c4ygH2JDeaS7QIlmfFyoeOYiLZz2HbaHwnFyAxCnxdZ7aA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
سفیدپوشی سبلان در نخستین روزهای تابستان
🔹
در ششمین روز از فصل تابستان بارش برف سنگینی قله مرتفع سبلان را در استان اردبیل سفیدپوش کرد
#اخبار_اردبیل
در فضای مجازی
👇
@Akhbarardebill</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/akhbarefori/663997" target="_blank">📅 20:32 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663996">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromهیئت قرار</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qmGAszWCzBgUrdhrXWn3EZd0yH2Nzf6_FTeU03QkZsh_6LYGzPHModWQzYQTmk7y4QgI1DF8R1C5NOH_775l0J--11X2umyX89ga1pLiJ5V2EKQgiURVhOR-We2-DJF4Il9qxuTrYGxy7wjYLgVzrdyqfJRUwDvoN_lqUGQHdti-5mXu9rz4uyL3mfNmFOhkzujytxP00Kuq5worLZhftBz98_aCC3QxC5iUYCtK8SygOcNWX_7JQjJYqAUz-CgJDz6T-z_3JDrfZs4X-jEAs_oxOijF1MOq5TAnHNGGBZXrQR8NYV5uSuFqVH-s89dbjhg27hE6WFjcdGqd70xqPg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✨
به تو از دور سلام
چله زیارت عاشورا تا اربعین حسینی
#روز_سوم
▫️
امروز با خواندن زیارت عاشورا به نیت شهید بزرگوار
آوینا برزگر
، دل‌هایمان را به سوی امام حسین (ع) میبریم. امیدواریم که ایشان ما را پیش اربابمان شفاعت کنند
@Heyate_gharar</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/akhbarefori/663996" target="_blank">📅 20:32 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663994">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/IJd939om1OERzrCe5Pd4B-awHSLIIGaTRx9mwyzlHZuv_SZ7EAbDLyJ4HTb1ZlIWbLWQmcT-WiVtYxXj0ox58ugs2KKoxKjelSikaQ_ZVoKh0C0E4GzbM-WLx1VHlj5RA-FQqOyMs0YLWqfSTrP9XaL0buGbQoPI8AtFRbLtz0lexZ8O1DlEOwNp9KXdI1PLAZLWWvl7NileOaR0lE5pcbJkaIHIFDl4_siXGnYA6jJ6nvlupkKxhlS1i6knGeU5zF8KAyf39lee0sginBwHsDFQE_xWLw5coM0aMQDaEhMRicRDF3-kYF6NzSX_3tgn3fcLqevSqhHu0XgmrUkycg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jjgGLunDCkbI8hS9jADUlABs3CcfoOCvGzFI8Mkz_MoCvhvRfcWS5WRtbiys1A6A-NzXa6OQh5zMHc5LdPfMBlWU8ZuIo6BbezPFzbLVSr-liBPP5g3rh_xAu-tshtApPmu4Zg8hkp1nPwYKBFXwr-3Ye16cf3TLBuTii-vulng_yhjfbmb8Pff9BBqXOosFs6bVAhC_dggRbGmje5Czi_IBW6Fdt9gJxmy0lxQWYK26L3LPNQlzxROBEO_2h0thMzfdYP0pCpCaLVk313U-YYyoMNQHBWMH85rxDudyeuK7F8PbWyapO_-oaVRc0LodllW-zlWI_nTn1DuMwZ-ZYQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
پیراهن‌هایی که هیچ‌وقت از تنِ فوتبال درنمی‌آیند
🔹
«پیراهن‌های همیشه» با قلم جذاب حمیدرضا صدر، سفریه بین اسطوره‌های فوتبال؛ از پله و کرایف تا مسی و رونالدو، با نگاهی احساسی، نوستالژیک و پرشور. کتابی برای عاشقان مستطیل سبز که قصه مردان ماندگار فوتبال را طوری روایت می‌کند که هم هیجان‌زده‌ات می‌کند، هم دلتنگ.
#فوری_کتاب
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/akhbarefori/663994" target="_blank">📅 20:29 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663993">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c6f5c83348.mp4?token=MyJTyTSDKCF9EJDkMh_TCwPwIAfrkaZYPJz2jQ4dU91nK_JbvOfFrZ0udxiabsqHJYdZtGTPoHmLiNCLyxtRIHRYV6SDNt0947MxGpQJMCwYvxo-kh9lk_i04PKob2m4Hf4O00G7nPSvPC0uVsZuPdfmRCSW6Jw9NW-y5nZ5RzNtkv0GRwiftRSPNWSLoirYgb6RexPUeGDQYxGm1DxBYc_vBtGTI1-n6j6t6lcxUGxYwYbNyeDWTTi_ztGU1FZoFrFlb04LTJe6UPC7dJboJ-ABtm-JtlIVK06gInuOevgtzC6WRJu9Q6uRnrU8EzJVoLuk0JfRmq3nV33h4zvqBowYW09dCZxv9yIuHUxko0NKxXdRTWpaaXC53SldpWcfA39ixSHh04fH2NzF-qjGtStvkXJ4Mx7fjbVau9zXuTvk-j4G7IYSkeA9nFtaoxtAMIHhjwRQDS7agWOVnYtTJ-K2_qkVRpppsQkUThLLtxLXe-D93kTawnK1wp8jFz4QV9I_cCbAkl_UuO8OppcHweXZQLKf8P-Bi-C7P0q4AtSQ2ezk4_zllDjpM9WCZswdHTvm5JRIXnWThGVQe7LMzaW_21FJiZ6GJBk6xtUeR7v4J43bMXixL5sTkCTub_ixDFKjsh_G7kiBNEEbft6EofaowrJv3YtYmqUy98sjVxk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c6f5c83348.mp4?token=MyJTyTSDKCF9EJDkMh_TCwPwIAfrkaZYPJz2jQ4dU91nK_JbvOfFrZ0udxiabsqHJYdZtGTPoHmLiNCLyxtRIHRYV6SDNt0947MxGpQJMCwYvxo-kh9lk_i04PKob2m4Hf4O00G7nPSvPC0uVsZuPdfmRCSW6Jw9NW-y5nZ5RzNtkv0GRwiftRSPNWSLoirYgb6RexPUeGDQYxGm1DxBYc_vBtGTI1-n6j6t6lcxUGxYwYbNyeDWTTi_ztGU1FZoFrFlb04LTJe6UPC7dJboJ-ABtm-JtlIVK06gInuOevgtzC6WRJu9Q6uRnrU8EzJVoLuk0JfRmq3nV33h4zvqBowYW09dCZxv9yIuHUxko0NKxXdRTWpaaXC53SldpWcfA39ixSHh04fH2NzF-qjGtStvkXJ4Mx7fjbVau9zXuTvk-j4G7IYSkeA9nFtaoxtAMIHhjwRQDS7agWOVnYtTJ-K2_qkVRpppsQkUThLLtxLXe-D93kTawnK1wp8jFz4QV9I_cCbAkl_UuO8OppcHweXZQLKf8P-Bi-C7P0q4AtSQ2ezk4_zllDjpM9WCZswdHTvm5JRIXnWThGVQe7LMzaW_21FJiZ6GJBk6xtUeR7v4J43bMXixL5sTkCTub_ixDFKjsh_G7kiBNEEbft6EofaowrJv3YtYmqUy98sjVxk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ماجرای عجیب شفا گرفتن دختر «شهین تسلیمی» در کانادا
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/akhbarefori/663993" target="_blank">📅 20:28 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663992">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SlV0DdRiKLiBp7zlEEYk7ZM2zCb18mj31Ddb00yMrM7foRUxhNT-aORYTNYFRnlBwj_HJN4MKgxKaVLL0fWysiJxxiY_KsOE1ew2r0sszIP8lupPrwLBfKtB4ECIhZdDuq-X0K1VDOltRCUX9O-0WPtqdtvnmg-VlVdfY_5qj3GD-nGLk_prsjPX-oOIzf5rbeZdEv4iKDk0fML3mnWZi83HQtCc8N8I1QVt1FUyVRmhkMJqz3Nbn1ESitJlKIsQynpVD0HMp7Adq-m7CLtwdOc_xsjw6BMoPl13tayWdQ6AIsgagsnrCjOHfvsN6IfQ-ky-4S2OvEsTFZJPQ9ZAPA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚘
بازار خرید و فروش ماشین از نگاه شما
در یک نظرسنجی کوتاه  شرکت کنید و دیدگاه خود را درباره بازار خرید و فروش خودرو با ما به اشتراک بگذارید.
🙏🏼
🎁
به پاس همراهی شما، یک هدیه 3 میلیون تومانی به قید قرعه به یکی از شرکت‌کنندگان اهدا می‌شود.
🔹
بدون نیاز به ثبت‌نام یا اطلاعات شخصی.
برای شرکت در نظرسنجی وارد لینک زیر بشوید
👇
👇
https://survey.porsline.ir/s/sJ9hb8Dc</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/akhbarefori/663992" target="_blank">📅 20:20 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663991">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b02331900f.mp4?token=sCLiq64yPhVMx6qR-AtXeCO4KLZ6Nl4f-cSOSTonLGTPChC3QTEImNjl__avSQSri1z5ZUwYjIPL4fd_idGJ-YI_Vlm5Joo8KK1Gi6JxuYcppT5omyngmcz3qDDIiaFpVI0hBcomqcnumtBvMBu_b6N2QGhmBJxQPd9fMN5lP6SMtkoniOvVTXSD2BDrAhSkYD4hF70WBt7fUFQ7v-6k-NxoAbm3ty0o5REA_GSb9oVICjB1sB-HCxRbafGe8mL_lOOmOlwEdOF8rgvHOr10G1LuRGgP3SJ3M9YqJroDgCWUiBvIAJfUiC-REGiO-jQDLmIuBZiOa81_jKMv9MbUcQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b02331900f.mp4?token=sCLiq64yPhVMx6qR-AtXeCO4KLZ6Nl4f-cSOSTonLGTPChC3QTEImNjl__avSQSri1z5ZUwYjIPL4fd_idGJ-YI_Vlm5Joo8KK1Gi6JxuYcppT5omyngmcz3qDDIiaFpVI0hBcomqcnumtBvMBu_b6N2QGhmBJxQPd9fMN5lP6SMtkoniOvVTXSD2BDrAhSkYD4hF70WBt7fUFQ7v-6k-NxoAbm3ty0o5REA_GSb9oVICjB1sB-HCxRbafGe8mL_lOOmOlwEdOF8rgvHOr10G1LuRGgP3SJ3M9YqJroDgCWUiBvIAJfUiC-REGiO-jQDLmIuBZiOa81_jKMv9MbUcQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
نمایی زیبا از دسته فلامینگوهای مهاجر در تالاب میانکاله
#اخبار_گلستان
در فضای مجازی
👇
@AkhbareGolestan</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/akhbarefori/663991" target="_blank">📅 20:11 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663989">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/C2LyNP4_eShenD8PWp6qUtIhOxCkr1qhclfwrOEk_Yec2GVkhYr5i7aZnEXAf6TYmH4IPUCWB6BIZuc9s2Kh1RS67b9KfzWHxtiPnwilJqhJqWfQdKVM76f1qnXyDDgGfUkVHfvoS5SgPkrR1AmemSR1YCY_LgStLH-_hoSVC3GS_PbVqe3tXjUQ3y9QQiJJTuf1INfc9lWM74AyHfLeCHvsDWhh7pka01HubJn6OnH89ujA6vCaMKxTyBKI2030SVrZuKeznAFNzEoRbPEbx8ZEK3QIKEN25WvaYe_pwVVLb42wAQsLzF_Kyvo7JqzifkegbXXShJ0X5tlpaq0s0Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
وقوع گسترده  انفجارات در رفح
🔹
منابع محلی گزارش دادند ارتش رژیم صهیونیستی عملیات انفجار گسترده‌ای را در شمال شهر رفح در جنوب نوار غزه اجرا کرده است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/akhbarefori/663989" target="_blank">📅 20:09 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663988">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Be9fyRS3Z8HOnfHu7NNn2ITeoLv4Ms_6u8PmK99yVJQAdyuIp4a6Ryk0lG1t0Py1zhuaRAPiFX6qoxmHI-lHrZQAH0VKKaecNri59oPRiovSuvAoONTxJa6vIBwEWBVX7HN5Icv1HA-ziakIt9uifft9av5lWqYkHx_AfUd5n9P96aikhniko5YoouCX8TlW4vL8YUNEFTtH1-_8XcUwjAvsJhGYA30pABsHrSJUG8mklO1B0hU6dTt6VJVdVVMpdpg-9WCgZfMUZviVfVpJ8Pp7bTAh4ROqftyhP8ZLvnM9ycXAVG2JMQh0kxlWJpaL_dE3oIszyl0QgVCz2n4TlA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🤖
آخر ترمه و پروژه‌هایی که عقب انداختی، همه روی هم تلنبار شدن؟
حل تمرین و آماده‌کردن ارائه می‌تونه ساعت‌ها وقتت رو بگیره؛ اما ابزارهای هوش مصنوعی مثل
ChatGPT
و
Claude
کمکت می‌کنن تو چند دقیقه انجامشون بدی.
🚀
اشتراک پرمیوم ابزارهای هوش مصنوعی موردنیازت رو با
قیمت مناسب و پشتیبانی فعال
از پارس پرمیوم تهیه کن.
💚
🎁
دست‌خالی نرو!
کد تخفیف اختصاصی مخاطبان کانال
خبر
فوری به تعداد محدود
👇🏼
FORI405
مشاهده محصولات و خرید
راهنمای خرید و کدهای تخفیف بعدی داخل کانال پارس پرمیوم
👇🏼
@ParsPremium</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/akhbarefori/663988" target="_blank">📅 20:04 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663987">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">♦️
آمادگی ایران برای کمک و مشارکت در عملیات امداد و نجات در ونزوئلا
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/akhbarefori/663987" target="_blank">📅 20:02 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663986">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fSlHFJy9c_LJQe3FD0zI0vBmdywWtSsO2PR2meQsbzW9fOsQpLeExqa5weqNZTIdOFrvJx2kkhXZTKCmxM2UD8Droz5bkuyG2MYzwZmqvbt8SGVJOAJbfDPEmf7eFqHqPx4BTCq5keBJ15KWwsQvN9SsuTFwckplKSDBej3whYrfZPT7vUrg2CQsWfnhEai4fxRDDDbPr9W4MOisTV7h5Yv44f6juRUboskJPCdcYslP9xYETxo8GdRYvOvZi9YZVkPsfx-WLHYS94oKA2YOZ1SnjdYC25wNGusLQwIK54LiymirAxUtpYuLgwHZaCr6zeHGGOwd881g_AXcJIyw0A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
کرواسی را ببرید تا ما صعود کنیم
🔹
درخواست جالب سفارت ایران در غنا از تیم ملی این کشور
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/akhbarefori/663986" target="_blank">📅 19:59 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663985">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TyLyTNUtfDJrjAsPTYu0jsNw68shTpXCj0GvdYlQYtoUp4664RaL7mn8Mmy6jttnoxUKZgG4NssoDOjeYd1N1t1feQjVVYY3YmJfQj1OG18j8FgOiRsBi4TOco6M0eRSIo8mhGlyh6BbukR17iK76Lu5Z6PqpJUYX7fgiuW1Ud1u1nk82IN-aRA5q2FERE9dwnTNH7vXM92yylC1KgqzxcvUIqPK3SK5n_SWmQ8BZO2JH5hF4_dBgY8MVHUBHJPnrz3m2Q1hsD3frK3lUsiOwglU20w9RUYcrK6gLgV9cJMCvC6aMpgR3Mi2FNlseWnvrPgvcW79o_1slfzG5ja4iA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
بز کوهی ماقبل تاریخی که در حال انقراض است
🔹
سایگا یک نوع بز کوهی است که در مناطقی که پوشش استپ دارند در اوراسیا زندگی می‌کند
🔹
این حیوان در چین و‌ مغولستان تقریباً به کلی منقرض شده که یکی از دلایل اصلی آن، کاربرد دارویی شاخ "کَل سَکایی" در طب چینی است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/akhbarefori/663985" target="_blank">📅 19:56 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663984">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a77dcd6e7b.mp4?token=Xmzq_KjCNPLKIjNDqkzgULDzbU9Rb8NXTyDv7ESZXDKlZh0x9YURyJAQQfDw7yQSQcbAxcTOFPjJx6w_JUbM2nSZ3KVGr5VzGrKpoxm2uQh2bQNFyyZNUefWb6b1rNu_RnQvBlAzYszLG5C288acFiSf_FbPEeYEUTtdLq9zv8nhBT3-jRMmyQjoCMe9Mnda3Kva_OytUEJIyUfp--4EUstm1GG_nuRwAYTk7E0Mq18-my69T1Mm1-Lv_Fx89yKw7GGGl8xMx2bOWVRCOa41UckUD8NSMHsYiIs8pLrD5KSLM45WaUMLAoBR1zUQP3fG7HgpNQDYdiztD3WXsi9Aog" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a77dcd6e7b.mp4?token=Xmzq_KjCNPLKIjNDqkzgULDzbU9Rb8NXTyDv7ESZXDKlZh0x9YURyJAQQfDw7yQSQcbAxcTOFPjJx6w_JUbM2nSZ3KVGr5VzGrKpoxm2uQh2bQNFyyZNUefWb6b1rNu_RnQvBlAzYszLG5C288acFiSf_FbPEeYEUTtdLq9zv8nhBT3-jRMmyQjoCMe9Mnda3Kva_OytUEJIyUfp--4EUstm1GG_nuRwAYTk7E0Mq18-my69T1Mm1-Lv_Fx89yKw7GGGl8xMx2bOWVRCOa41UckUD8NSMHsYiIs8pLrD5KSLM45WaUMLAoBR1zUQP3fG7HgpNQDYdiztD3WXsi9Aog" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
مسکو: پالایشگاه نفت اوکراین در زاپوریژیا را هدف قرار دادیم
🔹
وزارت دفاع روسیه اعلام کرد نیروهای مسلح این کشور یکی از تاسیسات مجتمع سوخت و انرژی را که در خدمت نیروهای مسلح اوکراین در منطقه زاپوریژیا قرار داشت، هدف قرار دادند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/akhbarefori/663984" target="_blank">📅 19:50 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663983">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">♦️
اداره هوانوردی آمریکا: در حال بررسی ماجرای نزدیک شدن یک پهپاد به هواپیمای مسافربری هستیم
سی‌ان‌ان:
🔹
خلبان هواپیمای مسافربری شرکت یونایتد ایرلاینز اعلام کرد که  هنگام فرود در نیوجرسی نزدیک بود با این پهپاد برخورد کند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/akhbarefori/663983" target="_blank">📅 19:46 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663982">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">♦️
کاتس: اسرائیل از جنوب لبنان عقب‌نشینی نخواهد کرد و به استقرار در منطقه امنیتی، از جمله در شقیف، ادامه خواهد داد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/akhbarefori/663982" target="_blank">📅 19:44 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663981">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">♦️
سی‌ان‌ان مدعی شد که اعلام افزایش سطح تهدید در تنگه هرمز توسط نیروی دریایی آمریکا
🔹
مرکز اطلاعات مشترک نیروی دریایی آمریکا سطح تهدید در تنگه هرمز را به طور قابل توجهی افزایش داد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 28K · <a href="https://t.me/akhbarefori/663981" target="_blank">📅 19:42 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663980">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">♦️
عراقچی: از هیچ تلاشی برای پیگیری فاجعه بمباران سردشت در مجامع بین‌المللی دریغ نمی‌کنیم
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 28K · <a href="https://t.me/akhbarefori/663980" target="_blank">📅 19:39 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663979">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">♦️
هزینه جنگ با ایران برای آمریکا فاش شد؛ ۷ میلیارد دلار فقط برای دو نوع موشک
پایگاه خبری UNN:
🔹
طبق گزارش مرکز مطالعات استراتژیک و بین‌المللی (CSIS)، بیش از هزار موشک تاماهاک استفاده شده، بیش از ۲ میلیارد دلار هزینه داشته و هزینه‌های موشک‌های پاتریوت به حدود ۵ میلیارد دلار رسیده است.
🔹
با نرخ تولید فعلی، ذخایر پاتریوت ممکن است تنها تا اواسط سال ۲۰۲۹ به سطح قبل از جنگ بازگردد و ذخایر تاماهاک زودتر از پایان سال ۲۰۳۰ به دست نخواهد آمد./ خبرفوری
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 29K · <a href="https://t.me/akhbarefori/663979" target="_blank">📅 19:35 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663978">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفوری گرافی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/C-x6c1E-d_iKotRLPy6NTq4tiibMM2Om6pcx4AOpbAN0M15e0rN5mfK7R215X7OZd0aKPe6rPkRd5slvH7P2yYHIRwsVetpVgnpg69CLHJQwC5yUOm6EFE248zoOVgDkBuRp7-ww3K64QLp420HxbYs1EtytaLdYju0kT7dFU2DCQggtid8I3FXbyKljshNyq9rCPsVaRKnGmE-cUk0Ffd26pb940xM8q7Mm2qDkNi8eEep7qeZq1kBaYdlL7XPtDVZlM9g8o9WzCgm6hrJilinIGvdfQyouhZPOT1RMcb7zVd0S3nSItlenjgJqKIdhy-9GGiPCG6XhNnmIzbs2Vg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
استان‌هایی با بیشترین تردد وسایل نقلیه/ یک چهارم ترددها در تهران انجام می‌شود
#اینفوگرافی
@Fori_Graphi</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/akhbarefori/663978" target="_blank">📅 19:32 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663977">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">♦️
شهادت و جراحت ۳ لبنانی در حملات صهیونیست‌ها
🔹
رسانه‌های لبنانی اعلام کردند در حملات هوایی رژیم صهیونیستی به منطقه النبطیه‌ الفوقا‌ یک نفر شهید و ۲ نفر زخمی شدند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 28K · <a href="https://t.me/akhbarefori/663977" target="_blank">📅 19:32 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663976">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">♦️
هم‌اکنون دود غلیظ ناشی از آتش‌سوزی لندینگ‌کرافت حامل خودرو از مقابل پارک آفتاب ۲ قشم به‌وضوح قابل مشاهده است
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 29K · <a href="https://t.me/akhbarefori/663976" target="_blank">📅 19:28 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663975">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/t-TIqNXzlmY5qTq4iLkRk71mqpLHSMJxLJgqTlq2nCOe4OATeIb0x-w5QcyX7cb8ZSM37Q9Ui_vasZs5cgKboFc13fjlQMqkvZDl6hltv9s6MrukTIh4VEQtRzj-ECpj32Y6sNmN16cy5unne6zLhmHeYjRUm73qTl7SpZiLUaaqmOAzmJlN9jd9R1GYRnOoMrJdrVOFbLYDMWRQjpnuHCxOcKu4CalLVWyD5sjM62LsTHdTJgJEgTkE1Ptpahs9PNv2Jps2yF20KXCe9K1n7xaebTq4MMX3mDhWxDxNKk2PXLtZTPz-1Ap0c9KzZP11tqUgas-G4BsPh36Ug3FpSA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
اینفانتینو: بازی ایران و مصر تمام چیزی بود که فوتبال نیاز داشت
🔹
رئیس فیفا پس از تساوی یک بر یک ایران و مصر در گروه G جام جهانی ۲۰۲۶، از این دیدار به عنوان «بازی‌ای عالی و سرشار از احساسات» یاد کرد و گفت: «از دقیقه اول تا آخر، تمام آن چیزی که فوتبال نیاز داشت، در این بازی بود.»
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 31.3K · <a href="https://t.me/akhbarefori/663975" target="_blank">📅 19:20 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663974">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e4150f04d6.mp4?token=u8x6OkefGPJE31-brbVvCgVlhW8Qw9N7sPE6sbdUoP5nYPEOjvyMfKQY1b5Wsnuv9oEWhEzFjelYxc6qhFZ53DNMwuPbf_TQGhMZVDTagd9o8PRRs7Wdbd6Qbl8caZ0Uv-gL4zbJf8wibRdjqC24w9FFzZfdJwGQGvSXiIwlCzv-jO5YEt_iwFjQGyswKUT9WKf4KAMCsY96mHMqzgLhAYnrQDu1icIqhuvGxz2jnA3BWwL2BFdm6eMbJ_Vu6R3mo4Je_CheQ3w0HrvjbHUY5FC--yysjQzXuNI3jEpOcWYAhlbgYWV5qme77E3n0g8cNDzQRx_9knhdiltcHcTEIw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e4150f04d6.mp4?token=u8x6OkefGPJE31-brbVvCgVlhW8Qw9N7sPE6sbdUoP5nYPEOjvyMfKQY1b5Wsnuv9oEWhEzFjelYxc6qhFZ53DNMwuPbf_TQGhMZVDTagd9o8PRRs7Wdbd6Qbl8caZ0Uv-gL4zbJf8wibRdjqC24w9FFzZfdJwGQGvSXiIwlCzv-jO5YEt_iwFjQGyswKUT9WKf4KAMCsY96mHMqzgLhAYnrQDu1icIqhuvGxz2jnA3BWwL2BFdm6eMbJ_Vu6R3mo4Je_CheQ3w0HrvjbHUY5FC--yysjQzXuNI3jEpOcWYAhlbgYWV5qme77E3n0g8cNDzQRx_9knhdiltcHcTEIw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
وضعیتِ امروز صبح در سراسر ایران
🇮🇷
🔹
وقتی پای تیم ملی در میان باشد، ایران یکدل می‌شود؛ ۹۰ دقیقه هیجان، امید و همدلی
❤️
🤍
💚
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 31.3K · <a href="https://t.me/akhbarefori/663974" target="_blank">📅 19:17 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663973">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">♦️
پاسخ صریح و تند نماینده ایران در اجلاس بین‌المجالس اسلامی در باکو به ادعاهای نماینده امارات: شما شریک خون بیش از ۳۵۰۰ شهید و ۳۰ هزار مجروح ایرانی هستید
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 32.3K · <a href="https://t.me/akhbarefori/663973" target="_blank">📅 19:12 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663972">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8117fb79ce.mp4?token=WfOrED-710fyaDmfHFgxULyGuEEML3H5PKOPrqa4zDfdcWH1JiLq0ZRqTOelWnv8vC8h2gbpy-KwXbGdK9MtoWzbkYWbxZJG4XbvWx6kwz7KZ0-hRR_hRLmWJ5kL1fgqFAn7u6h8vkOKsNQVpcmttgH-J-hkkbtPbzaR_mHCrHKyHNdILu4YHLFLbx8qvf_n6AVAp3KxjMC7YB54ymYXAtjiciJKA8S9bmIC779QgGgKlcQNF9OgKkZ0rERHsfluH_H0GawVIXeb_2m4x5pdq6l8jVmnGh56LSnZ1PHZJSLzawaFUIz31o7IZKdE9VbFER5QcxX_rqgKLILZ4z-NIQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8117fb79ce.mp4?token=WfOrED-710fyaDmfHFgxULyGuEEML3H5PKOPrqa4zDfdcWH1JiLq0ZRqTOelWnv8vC8h2gbpy-KwXbGdK9MtoWzbkYWbxZJG4XbvWx6kwz7KZ0-hRR_hRLmWJ5kL1fgqFAn7u6h8vkOKsNQVpcmttgH-J-hkkbtPbzaR_mHCrHKyHNdILu4YHLFLbx8qvf_n6AVAp3KxjMC7YB54ymYXAtjiciJKA8S9bmIC779QgGgKlcQNF9OgKkZ0rERHsfluH_H0GawVIXeb_2m4x5pdq6l8jVmnGh56LSnZ1PHZJSLzawaFUIz31o7IZKdE9VbFER5QcxX_rqgKLILZ4z-NIQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
شهروندان ونزوئلایی در حال جستجو در میان آوار خانه‌هایشان
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 34.7K · <a href="https://t.me/akhbarefori/663972" target="_blank">📅 19:06 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663971">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">♦️
انصارالله یمن: توافق لبنان و رژیم صهیونیستی، ائتلاف برای نابودی مقاومت است
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 31.6K · <a href="https://t.me/akhbarefori/663971" target="_blank">📅 19:04 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663970">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ckvxGU0ZOUEMXoU4tSvfLXB7I1x_qX4sJ-WuRjqcVQwQtt3tad3f4D9pzeUR-jOqAZok2ACvDULHcRWrtvT2xR5nQKN_1kcScEgY9oeGJRyDmvA1L2XMxKubGMuP0yjzoh2nXWpdwo_WxL2ETIVHJUXRCnxDBqGYzN6E0hyYJF8NRQ9yFjV99pSsy40Ga7OI-Xsa0t9OGRALDfATbRPPIK_fMiPWGdzR091uIN1pvI3grEaWAFMILUKN00af62mYQrbK-s2Dkw2pupkHBZglkT0wOdoaVVBRu-A28cmnAwklgUdxchWDC9IYjuHBMk87W-O-WxIPn3Gcu8XeNIxO1A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
خبرفوری رو در سایر پیام‌رسان‌ها هم دنبال کنید
🔹
خبرفوری در ویراستی
👇
https://virasty.com/akhbarefori
🔹
خبرفوری در روبیکا
👇
rubika.ir/AkhbareFori
🔹
خبرفوری در ایتا
👇
eitaa.com/AkhbareFori
🔹
خبرفوری در بله
👇
ble.ir/akhbarefori
🔹
خبرفوری در سروش
👇
Splus.ir/AkhbareFori
🔹
خبرفوری در روبینو
👇
https://rubika.ir/akhbarefori
🔹
خبرفوری در گپ
👇
gap.im/AkhbareFori
🔹
خبرفوری در ای‌گپ
👇
iGap.net/AkhbareFori
🔹
خبرفوری در واتساپ
👇
https://whatsapp.com/channel/0029Vb1RfOdJkK71F9wpxh3F
🔹
خبرفوری در اینستاگرام
👇
http://instagram.com/_u/akhbare.fori
🔹
سایت خبرفوری
👇
http://khabarfoori.com/</div>
<div class="tg-footer">👁️ 34.3K · <a href="https://t.me/akhbarefori/663970" target="_blank">📅 19:04 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663965">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Uynzi_7SIcCFUOi_GDkIOobF7LAW2aiUR6A-VGwDyAqj3XnYLkrW2q76qYYb13Y_ZN6qjbH-x54EbkdZvXvmMssJSsiJkIMsepE8-yOU-R5TiYDwY8eXyYaDgqwP1YqSm6qHM2t7KBOEVbB4sgT6su6McAo5gFYNMaKPD7tct4W88nay_8Nu666Zx3nFdhh6jpTYd4BN3D4TvEoTEW8K8NjSE-fvdWaG_WPSNfswRUkCr3Ego-zsFgFc8eukmTkRVdc5A9TWOdE0k__v339iDAhIveC_Bv2KmEne21To6lCCFvxYvcOsv9Z46UeB9GSqP5O_aVNsAVdZ_Z1BXegZzw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/cd-ldb3fcvdONnew3AHD6q5XSxas8pji5P2xNoFFs2Qb6veF_PmCXcoQvz-sNt-MPtmTgTRAjpfrsCyYZAu1ro4O8eKg-61NQkYLXcUEh6ZraucWJY8v4US_EFiDF6hZi6PQZcCizuKZy6QqwwF-W6jM_LkwBo1uFQZNxs50TYAsi9_EA5lCtusf-dnI8ZCo0NQv8-1usW4RgBrQp3vdxl3ZU534NTHC7xJ8OxSz6uLEX9StIQQUwo5I3pMCNWo5GqyDK-ncyNGSO8EkrywOkkZhmJmzhDasl8j3p_ztaUM9iar_tZz1c-2Ch62tKL70p63PlK3uj_PTIX5hFZJ9kg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vCDgHiIboUzREqkTc4t6GsEPt5rkJl9ieDlpPF_VfNH-w7LILMYrSDbl_lHrtcnlb7DuodQ6pUh-usrxnx3AQG7oOVNcrPK14fz2MOChGUqA1GFQPEaDXZPGvm25fnbOt340tb-T4BNx0EgYPUP9hBhM4NRq414Ro1TrqnJxdyMrTXRTGc6ZcI75HqTBdm6rbKo3-tTb7uZLR_vcsnxt3gXcG24jRP3JjHXyiSnQqlqa8f2g5NmfpPUI1fITItXSLVCD2h3j5n8d9HEZWPOg2SQLjRdoMir_dzUD75uOVYrEQ-CIm-kwHSqg_Laby50RlX9tWk0eXnlL_zOHxsyqrA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/aBW283dfhY9eOJ1yU6ohqxumCPmV--tNcdWuPraPTdwlHJTOkdv6TSelcSkwlmpe-7uiQ6GeG1woRyZrxNXo78BuPTaqgWmI924BeFbJEeJdu1NLcpK0NfJtVXIkOhPrz_ONp42NVyODdCy0G8Qg6hRlq69Zo88AddY5pr5UR-232DZAIeNFGWSqk-jY92wcasoBAu-YZKNi8xZEp7cKuODww02-We8aKiz4rrfTv2HfU8eIOUJnjQsuYVOfrEVovlS9Yd8x-hchjwwqKe5-VaVvvWutdn5x5hXV4V0wA3mkDDB1m6rFcGhNeZbiAIqCZBcr7PpMocU8Pm-e17Utcw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hATrglia8YNnQndlkWmgdNKwAzxggpTI0QKuutsag1HNZuH74sF024D74aw-f8vsxWxQ7Z-GRkEZLyi6taAfw51wcgYwsw987JbEba1HKNNXeIfq_OzBNCGCsB2YcMmvfQFPyn_6hMsJVGaQG18DE5WO4Y00S9H7Qy0qspbBlbGtcVJE9nlFYUMYtRMk3j2CfHIX3wP7TNUMU282tCwBpIKiTtteO3SCXOXXADoqL66YvI3lI5aKGOa49WFCyubIaVMipQx5Va8b_Ce-nRgPVzQN3JslX6qp6rXu4GSeWBx06Bmia6WVvyxUTVI2F2S09MjivOPUS4MyDwAxaPjAvw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
دسر مورد علاقه‌ات رو به انگلیسی بلدی؟
🍰
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 32.9K · <a href="https://t.me/akhbarefori/663965" target="_blank">📅 18:59 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663964">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">♦️
تماس فوری اسلام‌آباد با تهران
ایندیاتودی:
🔹
وزیر خارجه پاکستان، پس از حملات جدید آمریکا و ایران که تنش‌ها را در منطقه خلیج‌فارس افزایش داد، تلفنی با عباس عراقچی صحبت کرد. این تماس پس از آن صورت گرفت که تلاش اخیر برای برقراری صلح در غرب آسیا با شکست مواجه شد.
🔹
اسلام‌آباد اعلام کرد که در جریان این تماس تلفنی، اسحاق‌دار بر تعهد اسلام‌آباد برای ایفای «نقش سازنده» خود در دستیابی به صلح و ثبات پایدار در منطقه تأکید کرد./ خبرفوری
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 39K · <a href="https://t.me/akhbarefori/663964" target="_blank">📅 18:50 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663963">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8e3f53f3c9.mp4?token=omNKSGGnHFnRktVi7RFPGG6nR4Y6OO-0S3ueV3PDudgu-2Z47AGOsYyZu7yvaU1OcSQiqL48X1gbRzPSvdoZeEMC6jHQnH49Mov3f2wmvUquGFwT_AgbF-Wt2ny1vOVlAKIBc7nVlxbvIhdt6po-uKXU2Do1yvC2eQOIFWildYyATAVSLXjodpdL_HT2i_22RLQLyL1cROsVsAIIJkwHu-8BJuN4mIYMtOSCl9jP6rYuGQZE-mN20eEPc_TmfzCuWQB8JREj2Yg-Xu8_aTN75B-YeVSYj6YyJW0Vdv0BeXLiFiy8V1SBHHbJtPfZFAZUevLhBvCM8oAKUIGY7XGP21tdhVePYfG258FN95QWmlL3zG_GcftNP5VZHe8Z9tmG1n6bCFUfyRnofo9mXb7iPxjL480KQo6FHiJIfQoblZtRIT7FR5Q3ORdIuKCYj7dw0gaLP-xtI52X-Hw-KOjFepq10dicj1N8l0s-ENbZIzijIFFf2d0XOnQgzwky_-RyeYTt4yriyjPLPARdwcUJq4xgx_TNS2cos4wKHpIHpy6fZw9ULDJL9EDL2wqQolc1GXKXxCyU-ZiThvjR_dI3zOrlcZHmpYwPXvScIls8hGRcKUdWUQLycS00sR_ZA42UoD0icc17OH9_a-0QFq90O_BQ5zbLzn4OsQUC4gI_oeo" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8e3f53f3c9.mp4?token=omNKSGGnHFnRktVi7RFPGG6nR4Y6OO-0S3ueV3PDudgu-2Z47AGOsYyZu7yvaU1OcSQiqL48X1gbRzPSvdoZeEMC6jHQnH49Mov3f2wmvUquGFwT_AgbF-Wt2ny1vOVlAKIBc7nVlxbvIhdt6po-uKXU2Do1yvC2eQOIFWildYyATAVSLXjodpdL_HT2i_22RLQLyL1cROsVsAIIJkwHu-8BJuN4mIYMtOSCl9jP6rYuGQZE-mN20eEPc_TmfzCuWQB8JREj2Yg-Xu8_aTN75B-YeVSYj6YyJW0Vdv0BeXLiFiy8V1SBHHbJtPfZFAZUevLhBvCM8oAKUIGY7XGP21tdhVePYfG258FN95QWmlL3zG_GcftNP5VZHe8Z9tmG1n6bCFUfyRnofo9mXb7iPxjL480KQo6FHiJIfQoblZtRIT7FR5Q3ORdIuKCYj7dw0gaLP-xtI52X-Hw-KOjFepq10dicj1N8l0s-ENbZIzijIFFf2d0XOnQgzwky_-RyeYTt4yriyjPLPARdwcUJq4xgx_TNS2cos4wKHpIHpy6fZw9ULDJL9EDL2wqQolc1GXKXxCyU-ZiThvjR_dI3zOrlcZHmpYwPXvScIls8hGRcKUdWUQLycS00sR_ZA42UoD0icc17OH9_a-0QFq90O_BQ5zbLzn4OsQUC4gI_oeo" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
پنالتی لحظه آخری ایران مقابل مصر دزدیده شد
حیدر سلیمانی، کارشناس داوری:
🔹
گل دوم ایران هرچند آفساید بود، اما در آغاز همان حمله، برخورد دروازه‌بان مصر با سر سعید عزت‌اللهی در محوطه جریمه باید به سود ایران پنالتی اعلام می‌شد.
#جام_تایم۲۶
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 40K · <a href="https://t.me/akhbarefori/663963" target="_blank">📅 18:45 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663962">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">♦️
رئیس سازمان بازرسی: گرانی خودرو فقط تقصیر خودروسازان نبود
🔹
بخشی از گرانی‌ها ناشی از افزایش هزینه خدمات دولتی و تصمیمات برخی دستگاه‌های اجرایی بوده است.
🔹
بخش دیگری از افزایش قیمت‌ها نیز به تخلفات برخی خودروسازان و واردکنندگان مربوط می‌شود.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 40.3K · <a href="https://t.me/akhbarefori/663962" target="_blank">📅 18:40 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663961">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/08a6be612c.mp4?token=e14bbxcAyI-71TXEns5EGQHzed0plV4JLr9iWwSnshjigDeFh70v9fwWlyMg9WMXPAQIajLSNIn9CxSbwQrUukG4c_uOmsDGIVyG8BDmD7FKYAMoqzObKJOux4bMRlI2gPpUg7lGFUt4lcCZ_UA1XerlXM9aORi6KNoov23IJeDq2DctJlBNMRMiev5VCtaGNtjgIsAhiFBKQGClry4h3mCGyC3bXe_Fz6S7i5sRL_FHzdcTyvZD7-KFz00PUPg8dmPQD3oOh223jGiVIPtqlTu46sqESFbYaxrxKBEosVvGX5vU8GpKz-phTp7Kmq7I-CxzCWD4WRC1Yig05nnbXQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/08a6be612c.mp4?token=e14bbxcAyI-71TXEns5EGQHzed0plV4JLr9iWwSnshjigDeFh70v9fwWlyMg9WMXPAQIajLSNIn9CxSbwQrUukG4c_uOmsDGIVyG8BDmD7FKYAMoqzObKJOux4bMRlI2gPpUg7lGFUt4lcCZ_UA1XerlXM9aORi6KNoov23IJeDq2DctJlBNMRMiev5VCtaGNtjgIsAhiFBKQGClry4h3mCGyC3bXe_Fz6S7i5sRL_FHzdcTyvZD7-KFz00PUPg8dmPQD3oOh223jGiVIPtqlTu46sqESFbYaxrxKBEosVvGX5vU8GpKz-phTp7Kmq7I-CxzCWD4WRC1Yig05nnbXQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
عصبانیت بلاگر ترکیه‌ای از تصمیم داور بازی
ایران و مصر
بلاگر ترکیه‌ای در واکنش به تصمیم داور:
🔹
قسم می‌خورم آن صحنه آفساید نبود. من ایرانی نیستم، اما معتقدم سیاست نباید وارد ورزش شود. ایران شایسته نتیجه بهتری بود، باید فیفا رو تحریم کنیم چقدر شما بی آبرو هستید.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 40.6K · <a href="https://t.me/akhbarefori/663961" target="_blank">📅 18:36 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663960">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
جعفری‌آذر: باید مقرر شود حتما زنان موتورسوار از شلوار استفاده کنند
علی جعفری‌آذر، عضو کمیسیون اجتماعی مجلس در گفتگو با
#خبرفوری
:
🔹
تاکنون لایحه‌ای از طرف دولت یا طرحی از طرف نمایندگان مجلس درباره گواهینامه موتورسواری زنان به کمیسیون اجتماعی ارائه نشده است.
🔹
درباره اصل موضوع، یعنی صدور گواهینامه موتورسواری برای بانوان از نظرم محل ایراد نیست و بحث این است که باید شرایطی درباره ضوابط شرعی، مسائل عرفی و اجتماعی و رعایت سلامت بانوان پیش‌بینی شود و بانوان در هنگام رانندگی پوشش لازم را رعایت کنند؛ مثلاً مقرر شود حتما از شلوار یا از کلاه ایمنی استفاده کنند.
@TV_Fori</div>
<div class="tg-footer">👁️ 28.2K · <a href="https://t.me/akhbarefori/663960" target="_blank">📅 18:32 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663959">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Vzda1XxrC7XIHrYljLGesRdUDJ8E6h_9Dlg25jCRnyvcvMWW9P_SvBX3KwgCgXn_Wnh7Dfuo9QKQqOODdKsF4XjlzgwXIpI_SjAZGJIX80maWVuahLIyeKOPejdq39f9Is4Soip_pJYc_Gvu-pOBp-ULee57si6JulAoEPqvssL3uXc2MWoYpQBJStx5NX-XR8vzOJWwh531ivZHjrULfedQE5J0-wfLloWEkRyrGl2a1FWPyu04D5FqhuJep5Lb8Ak_h5zmqpb2hj7irQxW8L88j_rVrKv4JFPSQt9UK0bB118wzdRRbAYRZ55y5VB2mMikFO4qTQD7v_nsEV666w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
اسکوچیچ سرمربی پرسپولیس شد
/ایسنا
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 32.8K · <a href="https://t.me/akhbarefori/663959" target="_blank">📅 18:29 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663958">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">♦️
ثبت‌نام زائران و میزبانان مراسم تشییع رهبر شهید در پیام رسان‌های داخلی  دبیر ستاد اسکان شهرداری تهران:
🔹
ثبت‌نام زائران و میزبانان مراسم تشییع رهبر شهید از طریق بات «باید برخاست» در پیام‌رسان‌های «بله»، «ایتا» و «سروش پلاس» آغاز شد.
🔹
زائران می‌توانند برای…</div>
<div class="tg-footer">👁️ 32.8K · <a href="https://t.me/akhbarefori/663958" target="_blank">📅 18:23 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663957">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">♦️
#چند_خبر_کوتاه
🔹
سخنگوی دولت: ایران و عمان درباره چارچوب اداره تنگه هرمز و خدمات دریایی رایزنی می‌کنند.
🔹
عراقچی: ایران بزرگ‌ترین قربانی سلاح‌های شیمیایی است
🔹
حزب‌الله: دولت لبنان به دنبال سرپوش گذاشتن بر اشغالگری اسرائیل است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 32.8K · <a href="https://t.me/akhbarefori/663957" target="_blank">📅 18:21 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663956">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6fe8d3874a.mp4?token=jjpdxPaCKaFGnPWpTmRZ4IynaexVblKSNqiGnZ-9fByvc-bfGspwq0lD-XOWs0zv-_W1yWAcqdwGsNzL6165lCyc5qkWyNUFN0DXggQUalGDMU_fgwBZOi_DAZ7KvyZ7iJ1wXThPmjH9MiTs8WkHCSLkpCnEHiqfNgfL13zpl1XDDx0IRq50DzeoUclW957GnjDFBEmurN5PBfxK854KkyUp0UnGkKRXRFvJIOC2WbyTddqy65C1Aro7gnQGEqi4lXD8d2KCqmSho-dZWRdiRIXZzvl3xVUR3--jBuZDCfZxiC7i5lTxI75e1UWzQYFEDJqDIrYYqlt5byHYZbyvsA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6fe8d3874a.mp4?token=jjpdxPaCKaFGnPWpTmRZ4IynaexVblKSNqiGnZ-9fByvc-bfGspwq0lD-XOWs0zv-_W1yWAcqdwGsNzL6165lCyc5qkWyNUFN0DXggQUalGDMU_fgwBZOi_DAZ7KvyZ7iJ1wXThPmjH9MiTs8WkHCSLkpCnEHiqfNgfL13zpl1XDDx0IRq50DzeoUclW957GnjDFBEmurN5PBfxK854KkyUp0UnGkKRXRFvJIOC2WbyTddqy65C1Aro7gnQGEqi4lXD8d2KCqmSho-dZWRdiRIXZzvl3xVUR3--jBuZDCfZxiC7i5lTxI75e1UWzQYFEDJqDIrYYqlt5byHYZbyvsA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
هم‌اکنون دود غلیظ ناشی از آتش‌سوزی لندینگ‌کرافت حامل خودرو از مقابل پارک آفتاب ۲ قشم به‌وضوح قابل مشاهده است
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 32.8K · <a href="https://t.me/akhbarefori/663956" target="_blank">📅 18:15 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663955">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">♦️
خانه‌های دلاری در مشهد!
رستمی، رئیس اتحادیه مشاورین املاک:
🔹
وجود معاملات خرید و فروش املاک با ارزهایی مانند طلا، دلار، یورو و ارزهای دیجیتال در برخی نقاط مشهد قابل انکار نیست.
🔹
افرادی که چنین شیوه‌ای از معامله را پیشنهاد می‌کنند، معمولاً خود در حوزه طلا، دلار و یا دیگر موارد فعالیت دارند؛ با تکنیک‌های این بازار آشنا هستند و می‌خواهند مسیرشان با موانع کمتری مواجه شود.
🔹
با توجه به نوسانات لحظه‌ای قیمت ارز و طلا، توصیه می‌شود از انجام چنین معاملاتی خودداری شود؛ زیرا در نهایت ممکن است متحمل ضرر شوند.
🔹
هرگونه معامله ملکی با ارزهایی غیر از ریال با مشکلات قانونی همراه است و در صورت مشاهده، برخورد جدی با آن انجام خواهد شد./ اخبارمشهد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 33.8K · <a href="https://t.me/akhbarefori/663955" target="_blank">📅 18:11 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663954">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Qo4xq9ihJWJuRx_ZDjukajc32BViMhGkG-nH1Xb776xmdyOwwHLVByMnTYoo7Q1jwnciGRKolIsxVoMmAXpYjsMBcu7Ht04ErKEekQtdIpkY0ryU82JhxZhY7lxgdpLFUqK1klG1uLqw3sTM9Z6Sddm0z0Q_RUb21amUZbOuQvDu6NUx9_fAkPK6YLKY_uVzVB-kMe5Imm5aX5PfQ7Lrgne2IY7Q1MrhptGVwWLQbNTpAHPOj3gcEb4PV9XGamPjr93MRFq7DeAQwlM6vm5pJnd0tsEODwkNQVYG2SRFBArUnQZxsKfo5EEHv5te1hU_L_5AxDN5538YZqlO0FnsyA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
فریب دود ملایم سیگار الکترونیکی را نخورید
متخصص طب ایرانی:
🔹
تصور بی‌ضرر بودن سیگار الکترونیکی به‌دلیل نداشتن احتراق، یک باور اشتباه است و این محصول می‌تواند آسیب‌های جدی به ریه وارد کند.
🔹
ویپ حاوی ترکیبات خطرناکی مانند فرمالدهید، آکرولئین، فلزات سنگین و مواد شیمیایی طعم‌دهنده است که باعث التهاب و تخریب بافت ریه می‌شوند و حتی وابستگی بیشتری ایجاد می‌کند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 31.8K · <a href="https://t.me/akhbarefori/663954" target="_blank">📅 18:09 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663953">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">♦️
امتحانات نهایی در زمان‌های اعلام‌ شده برگزار می‌شود
وزیر آموزش‌وپرورش:
🔹
جزئیات دقیق زمان‌بندی و اطلاعیه‌های تکمیلی از سوی وزارت آموزش‌وپرورش اعلام می‌شود.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 32.8K · <a href="https://t.me/akhbarefori/663953" target="_blank">📅 18:01 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663952">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/B5WxpicLtESzGWpa5Cryv8aRW8lZAGtabD0tEA_SRxVwp16w_hLNPNbXqtpO8xU8UOdN5euJVL7wFJWN57oMQ2HvEOmtgzl7L1hTTatlt1s9_vdC4s2DAAt6T1D9XlsXCDr9uVcbcNXuqtHQFlmvhJH3yJvLBJFMxg-mBrxSosPKIKUgOBkGw5fp-eafzbeDFaXGMIN9wxPsz554_LTvZdX6dZrkUieq8chg5o1uQXiftOV0x_m-vnG9pzbnv0ipljURDL0My_8LIq9zi9V-zpIgZ-oMulLDQlaCAkCQDeQhzTLaulNVquZWzapcbW1yP5BboSoec90awVy_4TJdyw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
نامش ام‌وهب بود؛ بانویی که در کربلا، کنار پیکر همسرش، عاشقانه به شهادت رسید!
🔹
شاید اکثر ما داستان عاشقانه شهادت تنها بانوی شهید عاشورا را ندانیم. زنی که پس از شهادت همسرش بر بالین او آمد، خون از چهره‌اش پاک کرد و او را به بهشت بشارت داد. شمر که این صحنه…</div>
<div class="tg-footer">👁️ 33.1K · <a href="https://t.me/akhbarefori/663952" target="_blank">📅 18:00 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663946">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/pyyGgu3pxlV_nnTcfBCtzRkRlgV8g341iJZpi0tK7fkL2zonw-34S1SJx6am7B_dluTdZZmQugtqQrSRqRqJQ6Sqs0WtgdqRN-Leew3Ib9bDV1j5rgOthiiAj_gBn-lgyuEMbdp23ladoaubWMhg6Moknd51wvBSrYOs7IZFp8-PCFspzqtKqI5I5yav5lKeo-OdPxcL_xfKpkAqSedxLPRQeF7RJgp64MwOBGbAToPMYu3JdvBtFbK7Hp9Hy0kIGuEdXcbt6e7GYUM__lorhi7LpkSLcZJ9plPNlSiJDo6vA6hghyMSqMx-AQH05fJhH49I51__5rOiboouunEdiQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ZahvFVwQg8X68xXm1RjdQiOiA3xVoNKqtbmE8EOjbCt-QjZjA2xb9OEdh6rkRWptH9VMApCFtpB27yjtLfBXIWsc4xDwZ8LSSqEo35vy7mMHAsUCMOii9M2bI80n15hjyC4GlHuneJ07RmKRQrIdz6UzWmaEK26KimfSDJa90w_sBnJA9yvl9qOcYhEnSjUaNIOA8kSAGqTAlhubBvaJtyex-3giRvwFWI3KHrfQGDAW9ZYZdJ98MtAjJfWvTrwBQdJ6tPcAODjHVhWFQqnP2P_JzkgD57SVyKN_dEghYebwRZMui-iaz1wPsP3Y6CXhJncfgGuQE3-XCbCjx0Vfhg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/mu6roRT3am1DzJBgshyLHqEeAx45J-6oWDVcwJbjtYyABUs9Vnk2IuF4WLBHPXKmL6XrY3pECeHLV1HhZ3vdP0_zShVCM3Xagv61z9XWd8z-UG8rUFXntqRjjSmnPrs53LB_Lk2f_K6YtvKmiBhvXQEUQ4zODnBB5VKe6OuuEn3R976qMZDbWCOAvvnGVanwiyoUU5lBc4Ob8dLZkuRzIsoLFIqI0Be0LznX2lbeJiUo4PPAOsgq-xTs-MxRukSvmyEy696G2BmVKN5ENh3zuQ4wXZaN6G1qS7sVks6OOQj_xAPXgQ9Ol0eCPbalhXrVtfmLp5gbPeKF56qhqd5TKw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/DCgQlfS17mbxO6Mm9rFzA-c-A9P3F5-FuCWHWmOHrVgaqqqe2fv026IuClcr3YO5FvT8YsVBvUdyydcPkxXM7KNSYipw9gr1Mk0OPm-MZEdCSpsH7e7an9U5-XLzaKQMKe9E6Mr1NwNsw5yjv-Dp2n8U0BEBz8i01gmhudVy9UJkvI7wARNzq4jtwPhrTo94m6PJTaF8PoLg82eW_utEn5vzLPX4jJ2YOAfvImTQ5-Nn0h-u_UAg_4DZfHHnwMvdWwJGHVfEEK3YB7LVxjDKSNEQ-zqnHbu9XHrCOnTOdmqtjkXxXy9NG-ajsE4UiE_0JGEydY2JC1dmWu6yJGO9Vg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/FrDtrFhe8T-GQ-rzvd87DRT21Zlt5HzTM-Q2aN1mrzKbk2BRs05TUawMFwTviIJTlv9ELCi8fo-QfEYQQN7svFMRJOhWJJ3z98OyboHfPpUGfOoleLRuWs6iLus4By-CEJxBjvKZNVwT6_KW4Znd1EplSmOcaWldPc-ZEKP5UHiZ7inCZIwalpv-frpu3J4q0Cp7gXDgTgARpsxt0nzjW6trhoaEOyP6PD1xpUFc2qaz_xTxIHU1lojxoJEuKt19KCAgE6KWNqrcXvc5iiS9zgQBWw8nMkjwi9bcdKSEEDWeJv3idJKKhEXuSM0xOoFyVCQUIoDUKssEUXGW163vEQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/nK0e_ZfqFTWY-fJfjXGT4xBQO8WBqUgFPvKpgOnHV2N7AmDhUw4NVjs_nPFYIkMfbJZrbtMkuIx5kLXv13wkdJ7cRNixTIwPNAZjvFQwre2Oyif_HRpKtRN4v8W5XXLJqfshNT7-A1EcwwcEx680xWYwiRy7yiSO2FazoPk9ElAy8QRKiJFD3JWC23kY6V695Kv12TLKPllDOZ-alW3iXaXQ8B1t0vRW9fmnP8R-BlnyyUWLPveEhw6sBPzQEPvuqi_ZD0NU3kuV7FNwp9c7QOYNirXdHymjws1OhLOogVAOWcKM_mIoAukjSEmARnlyCGpAhF8U-PuTxBs1noGsOw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
۵ باور غلط درباره قهوه که هنوز خیلی‌ها باور دارند!
☕️
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 31.1K · <a href="https://t.me/akhbarefori/663946" target="_blank">📅 17:56 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663945">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d38ff0718d.mp4?token=HF4WSUmNe37cAEuP1mGBIitJu8Ym2w3-Ub3VV92VZo8KRDoYff8SjNc7r28uTrMRTKRLROFMa9LZqxC3YbTAgNfYhscnO7som8yA-tGE5hW4i8-pn-ItqjP7SKTdRacql2zvQYMfwLczrqyvF99_AfU3uV6RoAYN2BGTuNAQSPJiTitFUxo9KnWF3ZYqXMZc80Rk-IDmt0NGVvhHZHumnsmcAQjuS8R3gmJve3oYYRQ99h1avCByY9mg1L4DYIkzhvb5QooHBnPrlWihncLQYp__-HvE7RcWLpk6X3mSk0YPzc2iUjCEoU98nEDlRltoFW-XjLd12nD0VRnlrMgjfg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d38ff0718d.mp4?token=HF4WSUmNe37cAEuP1mGBIitJu8Ym2w3-Ub3VV92VZo8KRDoYff8SjNc7r28uTrMRTKRLROFMa9LZqxC3YbTAgNfYhscnO7som8yA-tGE5hW4i8-pn-ItqjP7SKTdRacql2zvQYMfwLczrqyvF99_AfU3uV6RoAYN2BGTuNAQSPJiTitFUxo9KnWF3ZYqXMZc80Rk-IDmt0NGVvhHZHumnsmcAQjuS8R3gmJve3oYYRQ99h1avCByY9mg1L4DYIkzhvb5QooHBnPrlWihncLQYp__-HvE7RcWLpk6X3mSk0YPzc2iUjCEoU98nEDlRltoFW-XjLd12nD0VRnlrMgjfg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ثبت تصویر سیاه‌گوش در جنگل‌های ارسباران
🔹
سیاه‌گوش، گربه‌سانی وحشی و کمیاب با گوش‌های نوک‌تیز و دسته‌موهای سیاه است که از گونه‌های ارزشمند حیات‌وحش ایران محسوب می‌شود.
#اخبار_آذربایجان_شرقی
در فضای مجازی
👇🏻
@azarbaijan_sharghi</div>
<div class="tg-footer">👁️ 35.5K · <a href="https://t.me/akhbarefori/663945" target="_blank">📅 17:52 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663944">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">♦️
#چند_خبر_کوتاه
🔹
روابط عمومی سازمان سینمایی:
در صورت صعود، بازی ایران با سوییس در سینماها پخش می‌شود
🔹
استاندار البرز: احتمال تعطیلی استان البرز در ایام تشییع رهبر شهید وجود دارد.
🔹
بانک مرکزی: ذخایر ارزی بانک مرکزی ۴.۵ میلیارد دلار افزایش یافت.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 33.4K · <a href="https://t.me/akhbarefori/663944" target="_blank">📅 17:50 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663943">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a1fbc6e319.mp4?token=bPgDZqGIpbkPTU5B0a9jN7ny-nduvJiOlv_Qtn9zTlTMNPY1UdIKWooHB9LIGdjZP6tVbGM_WMdbSDYSoZ9Xj0n9Ve7aDnPE_MCpWQRGywa02eJLHXksGfIvqh_gycR1U65MPB5ajaZeqnomzdexIFX22-1IjnpE4b2ObZELzMpZB5SlAtXf5KuV7sWHINsJ8wJCO1I-zp-QeymtZGejfPNi48-EcoN3EvUNvVfoCGZkCXL1vn5fKKeJakojE37ARdzMdITLN_PtLpm12j-IV7FmSCarAvjtDL8YUF8xVeP5Wzsl2MSxA4L4oUxUrGnTSSSCykGEuK5GRxweK0C9pw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a1fbc6e319.mp4?token=bPgDZqGIpbkPTU5B0a9jN7ny-nduvJiOlv_Qtn9zTlTMNPY1UdIKWooHB9LIGdjZP6tVbGM_WMdbSDYSoZ9Xj0n9Ve7aDnPE_MCpWQRGywa02eJLHXksGfIvqh_gycR1U65MPB5ajaZeqnomzdexIFX22-1IjnpE4b2ObZELzMpZB5SlAtXf5KuV7sWHINsJ8wJCO1I-zp-QeymtZGejfPNi48-EcoN3EvUNvVfoCGZkCXL1vn5fKKeJakojE37ARdzMdITLN_PtLpm12j-IV7FmSCarAvjtDL8YUF8xVeP5Wzsl2MSxA4L4oUxUrGnTSSSCykGEuK5GRxweK0C9pw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
آتش‌سوزی‌ یوتا ایالات متحده آمریکا را درنوردید و ساکنان را مجبور به فرار کرد
🔹
به دلیل شرایط بسیار خشک و بادخیز، در این منطقه «وضعیت بسیار خطرناک» و وضعیت اضطراری اعلام شده است. آتش‌سوزی‌ها تاکنون ۱۴۴۷٠٠ هکتار زمین را سوزانده‌اند.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 35.4K · <a href="https://t.me/akhbarefori/663943" target="_blank">📅 17:43 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663942">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">♦️
منابع خبری از وقوع زلزله ۶ ریشتری در منطقه هندوکش در افغانستان خبر دادند
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 31.4K · <a href="https://t.me/akhbarefori/663942" target="_blank">📅 17:39 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663941">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">♦️
سفیر روسیه در ایران: همکاری تجاری مسکو و تهران همچنان رو به رشد است
🔹
آلکسی ددوف، سفیر روسیه در ایران در گفتگو با تهران تایمز اعلام کرد که رشد همکاری‌های تجاری و اقتصادی میان روسیه و ایران حتی در زمان درگیری میان ایران و آمریکا نیز ادامه یافته و همچنان در حال افزایش است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 32.4K · <a href="https://t.me/akhbarefori/663941" target="_blank">📅 17:37 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663940">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/C95R69uslpHW_uOmdoGBiyFYM41Yn1D1frJxKO9zYxLRS9wdG9y7EOMSZ-cm0HIfGUXJPH9Qm2ZB21u_pkvnOEuKWOtxYR0Fbez5fLWLR6eHSTDKjp-ULfsoZYa1_epVhmxJ03RF5FckcHReS8Yeqjo9JmFOa-oFSDTl_ZFQxye0hSZg8LWU_KKjeeqUEFtZ2zuqya3f3y9z2D1zqKwNSSqSF8jE-FzAlAvzBGl1aoiROChjvuoAjompvgdgKlVV3daymkknqCjA0TdeFu580mug1P3jptLHN8Tlcy1e0T695gFn2nNrSpiXmuyPYf_lBvsmhtwVmwXJ4Vhh9HBHxQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
غول هوش مصنوعی آنتروپیک در آستانۀ بازگشت
آکسیوس:
🔹
دولت ترامپ احتمالاً این هفته محدودیت مدل Fable 5 را برمی‌دارد؛ این مدل ۱۵ روز پیش به‌دلیل نگرانی‌های امنیتی متوقف شده بود.
اما چرا این مدل قدرتمند است؟
🔹
شرکت Stripe با آن یک پایگاه کد ۵۰ میلیون‌خطی را در یک روز بازنویسی کرد؛ کاری که برای مهندسان بیش از ۲ ماه زمان می‌برد.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 31.4K · <a href="https://t.me/akhbarefori/663940" target="_blank">📅 17:37 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663939">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1622775009.mp4?token=VmOh6kk8WI5lhj2ABgdq1L_VTXtRPNWJXBPiO8jWujW-Sb-vXUaM7UCnT0JdF4tikEw0FLzsnyIwawZ9tx5AZTIZwBvKJN7_CA8bF6Oj6Ox7xJWCQ6fkxWGNgDxDgRqO8hQ7p9oEgvUoUSjMY_RnIJSXCFWSBUrOu7vZoGTAotpf7VFPgPXAIo7BjV6x6D_DJvY348sZyr4wBUJiQ0tZRrR5W8AujhPzc1Ai0bZOe1LeRv93iEFrn8he2Srh3BuK7soL__hmhlE772nGCa67h3eG9xSiS73bLXUtaCZj9bijIxPqlqSHDbzc7WgMRvWzT3uvXug55-j5UU4MnoNShQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1622775009.mp4?token=VmOh6kk8WI5lhj2ABgdq1L_VTXtRPNWJXBPiO8jWujW-Sb-vXUaM7UCnT0JdF4tikEw0FLzsnyIwawZ9tx5AZTIZwBvKJN7_CA8bF6Oj6Ox7xJWCQ6fkxWGNgDxDgRqO8hQ7p9oEgvUoUSjMY_RnIJSXCFWSBUrOu7vZoGTAotpf7VFPgPXAIo7BjV6x6D_DJvY348sZyr4wBUJiQ0tZRrR5W8AujhPzc1Ai0bZOe1LeRv93iEFrn8he2Srh3BuK7soL__hmhlE772nGCa67h3eG9xSiS73bLXUtaCZj9bijIxPqlqSHDbzc7WgMRvWzT3uvXug55-j5UU4MnoNShQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔹
برخورد هواپیما به آسمان‌خراش ۵۱۸ متری در پکن
🔹
یک هواپیما با آسمان‌خراشی به ارتفاع ۱۷۰۰ فوت در پکن برخورد کرد و سپس به زمین سقوط کرد که منجر به تخلیه ساختمان شد.
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 30.7K · <a href="https://t.me/akhbarefori/663939" target="_blank">📅 17:36 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663938">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromروزنامه دیجیتال خبرفوری</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iGTze18quMXScpIYSVX1IKIcTOmS2P01Y3cFSZsiyqtJ9ZlnRelRWjqLwWBJXLWJ2dVVRtXDVCy5y_IOKx354sqAxVCEkXm3KX5xIEe7HUCxQypaMY_MNAlwwGwMxsdpqYAXlRpMR418tdaYmKIujSFCxKfQovgPUh_oUhU55x8bisedeYzek5jJ5EFCmG7tqEQ7BOlITaGJjp-ffLHIIV9OV-Fi2JrXLtppF8jldi4Lrn-bD1lXpxdAoZBMDNjb1qRmegFcMFu89TTpVgi_2f784dVx03R5VYe9QwQjZ0IDUqgcyjuqTGtCFcOrQB1Pn_GgMM10SiVqhBVy1SFIkg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
+۹۰
🔹
در سومین دیدار تیم ملی فوتبال ایران در رقابت‌های جام جهانی، شاگردان امیرقلعه‌نویی برابر مصر به میدان رفتند و در دیداری پرهیجان به تساوی یک بر یک رضایت دادند. ملی‌پوشان ایران که نمایش قابل قبولی ارائه کردند، در دقیقه ۹۳ موفق شدند برای دومین بار دروازه مصر را باز کنند، اما پس از بازبینی صحنه توسط کمک‌داور ویدئویی،این گل مردود اعلام شد تا فرصت کسب سه امتیاز از دست برود. با وجود این نتیجه، عملکرد شایسته تیم ملی امیدها را برای صعود زنده نگه داشته است. بر اساس پیش‌بینی‌ها و محاسبات جدول، ایران همچنان از شانس بالایی برای حضور در مرحله بعد برخوردار است و احتمال صعود این تیم به دور حذفی بیش از ۹۰ درصد برآورد می‌شود. این موضوع امیدواری هواداران را افزایش داده است.
🔹
هفتصدوهشتادوچهارمین شماره جلد یک خبرفوری
#تیتر_یک
@rozname_fori</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/akhbarefori/663938" target="_blank">📅 17:33 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663937">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c129e52657.mp4?token=XUOfZL1GFBzlrZiiYVN7UdkG4P2hxjhIg4LQCdm0S85qVbb3RGtb4CxOZx_PHDSIJjvde2a2Yn8QBjzO-WpxT5KiuDs3SLnC8iW_VXZUtTVFqKfNyqIHWYdNsHRHKWF38nTL9SiKMP6sZeB9P-0mYIqkB8JwL9FF5gpWpzYi36zVa0_qEMHUPeuTKVgJ5jHzBrodriA9iuASeOfz9a5srlR0gFkkXoEz_6PtuF3w-R2qrWGlnowx46aifPFtLrR2qlfVkN9ljnSeh6cZT5oHmAs9auZ7gPPSqpYHJ34IbADX1lkDu42SoG0edXyImngP7KUlJgR2wDDO4ifCU0nwoIi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c129e52657.mp4?token=XUOfZL1GFBzlrZiiYVN7UdkG4P2hxjhIg4LQCdm0S85qVbb3RGtb4CxOZx_PHDSIJjvde2a2Yn8QBjzO-WpxT5KiuDs3SLnC8iW_VXZUtTVFqKfNyqIHWYdNsHRHKWF38nTL9SiKMP6sZeB9P-0mYIqkB8JwL9FF5gpWpzYi36zVa0_qEMHUPeuTKVgJ5jHzBrodriA9iuASeOfz9a5srlR0gFkkXoEz_6PtuF3w-R2qrWGlnowx46aifPFtLrR2qlfVkN9ljnSeh6cZT5oHmAs9auZ7gPPSqpYHJ34IbADX1lkDu42SoG0edXyImngP7KUlJgR2wDDO4ifCU0nwoIi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ابتکار جالب هلندی‌ها در به نمایش کشیدن رنج مردم فلسطین
🔹
در جریان یک تجمع اعتراضی در شهر اوترخت هلند، شرکت‌کنندگان با اجرای یک صحنه نمایشی، شکنجه اسرای فلسطینی در زندان‌های رژیم صهیونیستی را بازسازی کردند.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 30.7K · <a href="https://t.me/akhbarefori/663937" target="_blank">📅 17:32 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663936">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">♦️
رئیس سازمان ثبت اسناد: اموال وطن‌فروشان با دستور مقام قضایی، بلافاصله شناسایی و توقیف می‌شود
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 31.7K · <a href="https://t.me/akhbarefori/663936" target="_blank">📅 17:28 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663935">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6b4dfca4db.mp4?token=Fv9-Chmk65YiQSOG-qk3lQikKgOa-FAnUtQHk417IHdTyO4d_Bg0VVzKnjfMkTiFAGtfktBGR6LQ8ncZ8o5taxngKkttUkG6EG-levHttB7HxdHibzXSVdnag5SdT4mGwj73eZokXf5B6zgklkeHJdj1JddPAtgxEwQm1Y92MG7KR5D3jW3TYKD2H682Fc9Wm4vN7S6UJd1Ctp1yL9hJ8v6pRqQlv8WQYLZysLVwgalAImNaPRphMS8crazqRT7XHNeQ8yIqZ32O0_GC_e8GPIJdlyzfPpYD7a8I_JjKArYUzE7d8DYJT73ZjyEh41MZHeXlss8zqB2aJC23rVv1fzzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6b4dfca4db.mp4?token=Fv9-Chmk65YiQSOG-qk3lQikKgOa-FAnUtQHk417IHdTyO4d_Bg0VVzKnjfMkTiFAGtfktBGR6LQ8ncZ8o5taxngKkttUkG6EG-levHttB7HxdHibzXSVdnag5SdT4mGwj73eZokXf5B6zgklkeHJdj1JddPAtgxEwQm1Y92MG7KR5D3jW3TYKD2H682Fc9Wm4vN7S6UJd1Ctp1yL9hJ8v6pRqQlv8WQYLZysLVwgalAImNaPRphMS8crazqRT7XHNeQ8yIqZ32O0_GC_e8GPIJdlyzfPpYD7a8I_JjKArYUzE7d8DYJT73ZjyEh41MZHeXlss8zqB2aJC23rVv1fzzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
اقتصاد و اتمام ذخایر استراتژیک نفت علت اصلی پایان جنگ بود نه حمله به کشورهای خلیج فارس
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 32.4K · <a href="https://t.me/akhbarefori/663935" target="_blank">📅 17:27 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663933">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NeT3GIb-e3I_HHFirWOIxCuegKWTs8OMQ2tag7t8BX9-w8SximpKTMjWc8kDt9h4ezNnqAtVFtkOxyw2Qcv6uSRt6NkQ6EJabJ92X2Q7RwSG2hYNn9yhoJcQTLiHwkV6tQYMFJs0yW9KFI4V5Ur0TblosgF1xpe4PUcCqoTAS0b6ZhVgNZCoCwPmElo0R1XJ2bMbEb10UKNPsEkHbCnnHWaWv7relVYP02zbu0bJj4DtNarQoGbrcWjKy77a3opwsL0YGVu_bmvq_4_UagTJM9BgL8iLw0VVIkFvrNUlUxhcvFDbDNxT8EYaBGYnbL4AfrHN4fVCHhXplzMNZS0LnA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
سی‌ان‌ان: تشدید دوباره تنش ایران و آمریکا؛ نفتکش در تنگه هرمز هدف قرار گرفت
🔹
آژانس امنیت دریایی بریتانیا اعلام کرد یک نفتکش در تنگه هرمز بر اثر اصابت پرتابه آسیب دیده، اما تمامی خدمه آن در سلامت هستند.
🔹
این حادثه پس از حمله به یک کشتی باری در روز پنج‌شنبه رخ داد. ایران و آمریکا هر یک حملات اخیر خود را واکنشی به اقدامات طرف مقابل دانسته و یکدیگر را به نقض توافق آتش‌بس متهم کرده‌اند. در پی این تحولات، سطح هشدار امنیتی برای کشتیرانی در منطقه افزایش یافته و نگرانی‌ها درباره تردد کشتی‌ها و ثبات بازار انرژی بار دیگر شدت گرفته است./ خبرفوری
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 37.8K · <a href="https://t.me/akhbarefori/663933" target="_blank">📅 17:18 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663932">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">♦️
پایان مهلت ثبت معافیت چند فرزندی
تا
۳۱ شهریور
🔹
سازمان وظیفۀ عمومی فراجا اعلام کرد مشمولان واجد شرایط معافیت با ۳ فرزند و بیشتر که تا پایان اسفند ۱۴۰۴ شرایط دریافت این معافیت را داشته‌اند، اما هنوز درخواست خود را ثبت نکرده‌اند، فقط تا پایان شهریور ۱۴۰۵ فرصت دارند.
🔹
این افراد باید برای ثبت درخواست معافیت خود به دفاتر پلیس +۱۰ مراجعه کنند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 35.7K · <a href="https://t.me/akhbarefori/663932" target="_blank">📅 17:16 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663931">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e8ac09a84e.mp4?token=GJXUzRh7PWKubvQhW3gNfiDjxb-RA3HzOvAlvgeMk4F2NNIfCGUX8mnCARMhe1FxfbtP9y71Et5j8UCl6Gq_Xj29P9bEB2ZVe06g9AM1rX65p9gnMlQ8TohuS51I2Ufksxv06Qbxelt2XXcDc0zbETRVLfvoxMQx9UcPbo377Q5UZOBoqIUDgwvFB-zM91gi_4RlB9BklSri0WVGwh9-TwPxFNc3pz0iMAiTcDg-MusZqYczrLHXfqEI3tO-FTHuOoWWTEk3LwihKFR9sdqtkLOIl6EwTpD3tCTYLkuQhtasNFS6LsGWEqi9egh28LF-5GILYNXQfGj_baFBpuzfwUm_BQOKSoo2NBtIgN0DuwvspKD9J0wmBZVbUbeGDaEsJQGDe5T1ZaUfUbSwLyuFXr5dmDUPEposG9Sjl3y9uTCuhYOvn2cUrHU7hHdve3BlhvE4eiWfBCbh9ciyoBV0bGP85GNrYYE2Qv5WmPmaqdwh62kunM7HPdSBogLc9zWROXc-dnpHMVvzC3tSXtxVvCuRTQDPOib5crgrhe8dqTj0xjfPTdqAFPIOsmN0pbkBcJeW76I5gU_aVlsIaC7yCLl4x8Wz3dxZe22_JuvxM2lNCPN1wdOIv-WhlWZpERWZ6YgbwCM4Vk2mtW79jXPfGCuq05QYj3lflBoN-zpPTq4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e8ac09a84e.mp4?token=GJXUzRh7PWKubvQhW3gNfiDjxb-RA3HzOvAlvgeMk4F2NNIfCGUX8mnCARMhe1FxfbtP9y71Et5j8UCl6Gq_Xj29P9bEB2ZVe06g9AM1rX65p9gnMlQ8TohuS51I2Ufksxv06Qbxelt2XXcDc0zbETRVLfvoxMQx9UcPbo377Q5UZOBoqIUDgwvFB-zM91gi_4RlB9BklSri0WVGwh9-TwPxFNc3pz0iMAiTcDg-MusZqYczrLHXfqEI3tO-FTHuOoWWTEk3LwihKFR9sdqtkLOIl6EwTpD3tCTYLkuQhtasNFS6LsGWEqi9egh28LF-5GILYNXQfGj_baFBpuzfwUm_BQOKSoo2NBtIgN0DuwvspKD9J0wmBZVbUbeGDaEsJQGDe5T1ZaUfUbSwLyuFXr5dmDUPEposG9Sjl3y9uTCuhYOvn2cUrHU7hHdve3BlhvE4eiWfBCbh9ciyoBV0bGP85GNrYYE2Qv5WmPmaqdwh62kunM7HPdSBogLc9zWROXc-dnpHMVvzC3tSXtxVvCuRTQDPOib5crgrhe8dqTj0xjfPTdqAFPIOsmN0pbkBcJeW76I5gU_aVlsIaC7yCLl4x8Wz3dxZe22_JuvxM2lNCPN1wdOIv-WhlWZpERWZ6YgbwCM4Vk2mtW79jXPfGCuq05QYj3lflBoN-zpPTq4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
پست پیج ارتش نروژ در حمایت از تیم ملی‌شون
#جام_تایم۲۶
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 37.8K · <a href="https://t.me/akhbarefori/663931" target="_blank">📅 17:14 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663930">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LRRJJQeJEcnkPVXT0YJptT54g5-vvUeJ2C1wqL5tOk3Ljo1O-Pt0fvFXM8IDvalBaR3l0MjgZhgfmpDdf650dLnoanRuzLKHQmGKahL_K1f_gDPjmFNRB4UkvUMl3lkaSaT8QTq2E3V2isRiBC7LVfYvXOxf_Ngk2TfD-uggpcv4McMTPrYCxFkq_26doe7tABQzHFkEJju6hmEgOseW4aSJM_0gf91vvvLlvJMFfndcFAEu8qUnmTYGp02BGoq4swgKvcMn0-ZfsyYYaHWSqa8qOTneO_3OlFKSiLJFGW_NkJAJ9nFt8WLclmf3ezRWDCIbd-c6KWFXnzpQDNn_GQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
تسنیم: مخالفت بورس و عضو هیات مدیره با تغییرات در هلدینگ خلیج فارس/ تصویر نامه به وزیر نفت منتشر شد
تسنیم:
🔹
براساس نامه‌ای که در تاریخ ۲۶ خرداد توسط حسین زاده عضو هیئت مدیره هلدینگ خلیج فارس خطاب به پاک‌نژاد وزیر نفت ارسال شده است، وی رسما روند غیرقانونی تغییرات در هلدینگ را به وزیر نفت اعلام کرده بود.
🔹
اخیرا هم سازمان بورس به عنوان نهاد ناظر بازار سرمایه بدلیل طی نشدن روند قانونی، با انتصاب اعضای جدید مخالفت کرد و کماکان هیئت مدیره پیش از انتصابات به عنوان اعضای قانونی هلدینگ خلیج فارس شناخته شده و تصمیماتی که با امضای اعضای جدید گرفته شده غیرقانونی اعلام شد.
🔹
حال سوال این است که مقصر جبران ضرر وارد شده به هلدینگ از لحاظ حقوقی و اقتصادی چه کسی است و آیا وزیر نفت پاسخگوی سهامداران خواهد بود؟
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 38.1K · <a href="https://t.me/akhbarefori/663930" target="_blank">📅 17:10 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663929">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">گزارش رسانه تلگراف: حمله به بانک‌های ایرانی کار گروه هکری «گنجشک درنده» است
🔹
رسانه تلگراف در گزارش ۲۳ ژوئن خود مدعی شد حمله سایبری به چهار بانک ایرانی از سوی اسرائیل انجام شده باشد.
🔹
طبق اعلام این گزارش، این حمله بلافاصله پس از اعلام دونالد ترامپ درباره دسترسی ایران به بخش اولیه ۶ میلیارد دلار دارایی نفتی مسدودشده در قطر انجام شده است.
🔹
کارشناسان امنیتی در اسرائیل به تلگراف گفته‌اند گروه هکری «گنجشک درنده» که یک گروه منتسب به عملیات سایبری اسرائیل است، احتمالا مسئول این حمله باشد..
🔹
یک منبع امنیتی دیگر نیز به تلگراف گفته زمان‌بندی عملیات نشان می‌دهد هدف احتمالی، خرابکاری در توافق بوده است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 38K · <a href="https://t.me/akhbarefori/663929" target="_blank">📅 17:08 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663928">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Wbrq96HyQMK-FUaiJaXND0xGaQuFRQsyI1WEFp53WLNVSw4wmCY3cZx3S6Uy0YZr1OkHXalziVfK38Em8ky8pAPj7lwkjOGtiIh4v2300URoKqZyknlKBmwkPfT7IvzOamyF7vMK2cQsiqTDMIGKfX4V4wy5R8ttM8cqxGhGZFayHz2DMxJbh55-pSaAT5SYoJJUWVbNP9pN7zoE02A8wVwEqHbjFm1Z_6dqThqTqapnBdxXRK50KiPXbx5R2KNwKY0GWzXLoGerjwVpOqzQ6Lp9YBcykVcpwJtg9XAPkFc8LKX6o0r7lnd0C6h3mUVb9noHDV3WmMpQtJyKFjbDtQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
تورم نقطه به نقطه در ۱۱ استان کشور از مرز ۱۰۰ درصد عبور کرده است/ ایلام، کردستان و لرستان صدرنشین تورم
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 40.4K · <a href="https://t.me/akhbarefori/663928" target="_blank">📅 17:06 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663927">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/96f85367bb.mp4?token=VV9o0uBok5VJMtVK_8ZaWVPfHJ74of6Cwpwp4MVYpCUqboIK9FSHyB5kp90Bd1oazzKhy5j1qmRqaIjqGU_qVFY6DwvROcRK8P9w4NgZ1sTstyA8xq5nMfvb2RHVtDVfJcFdWh6XjAFkvTkQFPc1-d-BjGdo_v_PFpiDejJV4uHUc7f33sgonneLwdSkCY0twGUr4N5psYoxRJSxk5A3QQBwnWS9qbXzW3XzD2bXPgWciK5Np8NspW2NxOxNZBm9dpWdEY5uABYB4W12XRviYBBS5WKkXnabez0DCbRKLonITCEmKFpPNRcKs80IV_XIzC-SadJ3KiuTc__xKg1JGoi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/96f85367bb.mp4?token=VV9o0uBok5VJMtVK_8ZaWVPfHJ74of6Cwpwp4MVYpCUqboIK9FSHyB5kp90Bd1oazzKhy5j1qmRqaIjqGU_qVFY6DwvROcRK8P9w4NgZ1sTstyA8xq5nMfvb2RHVtDVfJcFdWh6XjAFkvTkQFPc1-d-BjGdo_v_PFpiDejJV4uHUc7f33sgonneLwdSkCY0twGUr4N5psYoxRJSxk5A3QQBwnWS9qbXzW3XzD2bXPgWciK5Np8NspW2NxOxNZBm9dpWdEY5uABYB4W12XRviYBBS5WKkXnabez0DCbRKLonITCEmKFpPNRcKs80IV_XIzC-SadJ3KiuTc__xKg1JGoi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
اعتراض سحر قریشی به برنامه عشق ابدی: چرا همه لباس‌هاتون بازه؟ گفته بودم لباس باز نمیپوشم!
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 32.6K · <a href="https://t.me/akhbarefori/663927" target="_blank">📅 16:58 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663925">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XBo1GH4Lf8gXA9ew3l8KFbhdsPEPtZaOBlW-RDS4SmPCKHFCy3dsgJHjGzt04weD45dTAHwOrT_D_kf1Kr5TZdrxAqWgmvlU2digp2_wFvxnTexooS3AbdjCWAfZoKHfse38zhEv0QP-JK_At6KtG0KhDvAlQS5Od1WtwNuYK5qhbl__uT1pnSiaBHu0fpwdRchyTv11DxpPbH4OYXUIIjPtVWHQXl_IoNR6utgzsxznS0HQVXVmdZOmb7hROmn8GRZPJxvfColZ8z_NXoCw4lPYk99K-RuPzIMOxA1epUNuZ4VP9WqSslrjDDNtttyFJ7GUuE1TdOX2zhEbRRacag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
یک کاربر خارجی نوشته بود؛ وقتی VAR آمریکا می‌خواد گل ایران رو بررسی کنه
🙄
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 32.7K · <a href="https://t.me/akhbarefori/663925" target="_blank">📅 16:55 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663921">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/XpcWKNjYVZWh2jv6Ypj-uThUp4MaUp8gQT9UozByzgS8CFTgOzk0vJUnDl8E0arkqYg5tseuyXOhLa8PcvYk3cXJ1mLP-qhM0SJF6n1AqPByFgaCXBT7V5scI2TUwoUyyl8Z7v4vp53oWK4M8s5mlPkQKvSjmErjTA6roYt8izINyuDVXUlDDe15PPtNF497_es1_HYh-_oKuZXdT0FzuqorUjehMfeCQLkoRsrqWr28BCMWJefg6RRUtxBQ5zGZZoUj69N6iVK80g9GpSYk0ITPiuCTHJiAuVeR9s8b-eirSlgGm3-LrLRDBvkfPBYx2c4jTH51kZ_HhziXVel8lQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/n8NLqMTyhQ8QgKoBKbladK3p74QuhXypbfUGE7MR6eFVjr6uae5uhh5m1YFCjj5xtCLvKwfk1KGlxNYBrzncweE0oAMlRN1p0J-AYJCZYO_-mwTR3_qnuTBdlxHVBIskTcXCge4bHV3QFlFHXqOAGMr4nEYJ2u-7UeKrsh4I3HqcoeM1XiBCaiuOgEpb2QIC-gg2QeOCuqhQQjgP8oFdHeg6BSinFCi25L8FoRriredQTSG0ejx5cf-XhL9DiBXL1fj28Ut6mcQ4bktnHAvTlUBcpwl1GNA7YYQ281bbqgtvYbSwCiJoQnlwxEe5XL4lsLY40faoVXVbuITt9DMJ9Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/L04vOQOV_5B-iLhuQ5dsnuE-xzLPDPhA_w9UU1oKZhuDxYrp2WLt6micoi2hhcXu4k_FygcgbEFD41Dx0QirMHn0oZBKrXyKG6vzj71MCe7Dixu5HfKw7Sy3YIO8Qlb7NveX1Pc1rYx1Hr1rSOTws6Zsye35MuPyYqW40Swq1Vx3cFtogQJ7CwLLI-cIkXlC4zwY3ahhJgCX3HRONq31NADthul0gi8Jtep9eDxiJi0vZLlc4TiEgyPDqqazRifHM9vy2NRIxpncjnJ9uSvhZaBOJpn5vXxJnHvytth_JZ3k0dfirZYy22hlRoNrH6HyfTgBQnN4iwsC-ZdJ8U9GtQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
نشست مشترک سران قوا برگزار شد
🔹
نشست مشترک سران قوای مجریه، مقننه و قضائیه به میزبانی مسعود پزشکیان رئیس‌جمهوری در نهاد ریاست جمهوری برگزار شد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 32.4K · <a href="https://t.me/akhbarefori/663921" target="_blank">📅 16:52 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663920">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">♦️
تکذیب خبر ممنوعیت ورود خودرو‌ها به تهران از روز جمعه
🔹
به دنبال انتشار مطلبی در فضای مجازی مبنی بر بسته‌شدن کامل تمامی ورودی‌های تهران از روز جمعه و ممنوعیت ورود خودرو‌های شهرستانی به پایتخت، پیگیری‌ها از پلیس راهور تهران بزرگ نشان می‌دهد این خبر صحت ندارد.
#اخبار_تهران
در فضای مجازی
👇
@akhbartehran</div>
<div class="tg-footer">👁️ 32.3K · <a href="https://t.me/akhbarefori/663920" target="_blank">📅 16:49 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663919">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">♦️
دبیرکل حزب‌الله: توافق دولت لبنان با رژیم صهیونیستی ذلت‌بار، ننگین و به معنای چشم‌پوشی از حاکمیت ملی است
🔹
ما در سخت‌ترین شرایط میدان نبرد را ترک نکرده‌ایم و هرگز نیز آن را ترک نخواهیم کرد.
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 31.7K · <a href="https://t.me/akhbarefori/663919" target="_blank">📅 16:47 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663918">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/s2fIs4IU6sv8_HK23_vlgt9eAOT0xp2dz5cR87U5eS8GBr5AHZxkSI2UxvGUZjOE3AjxZwtO3vMJr3QjzR5Al66CVcX5vg48Iw8m_e_7rMQK0pihV_PomasXdP8CKeXiRclDWiU6xMAfsgeDuqZjlTXAPbnCI3SvtOvQyTWuSLX9fKdAD1wzj9IIiPB4BMckjRcNcUjqf_MrM5Sgf-T3w4khUdrUUA2Asl2-Q4PdwWpTDKv9s8BlW_5ZbaW7uMdKm20N0-8V2G_fjgt7D-178ERciZtcO88gTyhur1Osy4PejH8c0p8M3Dh2ixb1aofgUf6ZEjP-MiCgFriJMyKqWQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
مذاکره با آمریکا در آستانه تعلیق
عباس اصلانی، خبرنگار نزدیک به وزارت خارجه:
🔹
مذاکره‌کنندگان ایرانی پس از حمله بامداد امروز آمریکا به سیریک، در جنوب ایران، در حال بررسی تعلیق مذاکرات فنی با آمریکا در سوئیس هستند
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 32.1K · <a href="https://t.me/akhbarefori/663918" target="_blank">📅 16:45 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663917">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d0e48422d0.mp4?token=SA3fEiJYaPVjyMsT2dm0-4PGoKuaPVYee6_5-4ytXG6A70AezBfhhyluftwmAJmY_AF8c5J2dX_O3hA9z-lBJ8QcxuU-l5YOSd58R7VqWGwBfo1i9FN6O5NPpI0Hu50teBP8G_VceBeHZ4nYDFPrKzsIQ7qFwdXHmjmVjn2rdfchrW7YL0YU5Ts-Psr-Nw4xHmYPmoKbqkWp6pmFCMxEcSmYep0wNK8TMCInlLeyryEcC--w7VFFq3qDIcGT7TjwriXHkqAryeGfHqr7r4GbuAzZmyKxBk-Pr26ZNLS2Ql2VZENss1eUj6sF_6cF6ykgKVAL1ErVXu7DT7E2ksDZSzppCtgWsvqQzHJppcVgA3rz29L_M9MCx-3AkviEGVnNSMAgqeQ6iRERYF8XaOEXn93qvYxFCfQLAK4LQ-eZkjY0p9INYhYz05QnWzJpzsxWGXykvd3DXbsNZhDWZcRyVP4yCUyBF1NbTIubUXmUz_OaLoHJAVCgRY8Kga2KNAk9FAvRSKuZywdwzo1Pqu7JQp53GcxM7nyO6yrVySVyEF9r6kJ_5rVciAQoVMsm9Vf9KhwF0efJIXFkU9opnqtzVM7hE4K-uTv6giqQc8ivdVFeclIgtIMRNAG7F1vnG7NOSQhzkAlSa0W76JoWJ0CsUMqyxzFfkug0PleYEx7DGlQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d0e48422d0.mp4?token=SA3fEiJYaPVjyMsT2dm0-4PGoKuaPVYee6_5-4ytXG6A70AezBfhhyluftwmAJmY_AF8c5J2dX_O3hA9z-lBJ8QcxuU-l5YOSd58R7VqWGwBfo1i9FN6O5NPpI0Hu50teBP8G_VceBeHZ4nYDFPrKzsIQ7qFwdXHmjmVjn2rdfchrW7YL0YU5Ts-Psr-Nw4xHmYPmoKbqkWp6pmFCMxEcSmYep0wNK8TMCInlLeyryEcC--w7VFFq3qDIcGT7TjwriXHkqAryeGfHqr7r4GbuAzZmyKxBk-Pr26ZNLS2Ql2VZENss1eUj6sF_6cF6ykgKVAL1ErVXu7DT7E2ksDZSzppCtgWsvqQzHJppcVgA3rz29L_M9MCx-3AkviEGVnNSMAgqeQ6iRERYF8XaOEXn93qvYxFCfQLAK4LQ-eZkjY0p9INYhYz05QnWzJpzsxWGXykvd3DXbsNZhDWZcRyVP4yCUyBF1NbTIubUXmUz_OaLoHJAVCgRY8Kga2KNAk9FAvRSKuZywdwzo1Pqu7JQp53GcxM7nyO6yrVySVyEF9r6kJ_5rVciAQoVMsm9Vf9KhwF0efJIXFkU9opnqtzVM7hE4K-uTv6giqQc8ivdVFeclIgtIMRNAG7F1vnG7NOSQhzkAlSa0W76JoWJ0CsUMqyxzFfkug0PleYEx7DGlQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔹
خلبان اف۱۵ سقوط کرده آمریکایی در کهگیلویه گفته پهپادهای سپاه با آرایشی شبیه عروس دریایی در آسمان و مثل یک میدان مین در حرکت بودن...!
🔹
اکنون شبکه‌های اجتماعی غربی‌ها از این فیلم‌ها پر شده است
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 31.6K · <a href="https://t.me/akhbarefori/663917" target="_blank">📅 16:44 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663916">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/83fe6cc5e9.mp4?token=LqDavPFAt4nOJaRx-oC7KUv3T87PoAIHZcYcAbitOcmLYIARSYd_IzqQgVWcGHFCbMavq9H1m02Puuo2ULqjL4kZIvR6TE3cAtNTdqbYoJPasem5LQ8YHg4ypApaJWyTIuLazv_y-Um0NWnO1hLDDhXFqfvhzBtxGkX577bgyEll3h5SGZCATICa2UQmQ1KqZOZ1g4wZbi2-quqsI3OJR6McC8yN7p4RLy_6JG_EtgkumtjLnBsu6ETAaQvgxr3HDEx7nUMHRl4MpHhR1X7-DviOPAIVPIA7oI0-w_Hsxii0XJKqS2ldyWv8soRhjmllH1zKaS_HIguKuNAOWSdvSA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/83fe6cc5e9.mp4?token=LqDavPFAt4nOJaRx-oC7KUv3T87PoAIHZcYcAbitOcmLYIARSYd_IzqQgVWcGHFCbMavq9H1m02Puuo2ULqjL4kZIvR6TE3cAtNTdqbYoJPasem5LQ8YHg4ypApaJWyTIuLazv_y-Um0NWnO1hLDDhXFqfvhzBtxGkX577bgyEll3h5SGZCATICa2UQmQ1KqZOZ1g4wZbi2-quqsI3OJR6McC8yN7p4RLy_6JG_EtgkumtjLnBsu6ETAaQvgxr3HDEx7nUMHRl4MpHhR1X7-DviOPAIVPIA7oI0-w_Hsxii0XJKqS2ldyWv8soRhjmllH1zKaS_HIguKuNAOWSdvSA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
هنر خیره‌کننده ساخت رگه‌های مرمر روی دیوار گچی
😍
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 30.9K · <a href="https://t.me/akhbarefori/663916" target="_blank">📅 16:38 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663915">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/R6I2d7L7SCrkK9pX9jFWRuHnZCZx0eMgArUp2SGVamuI-rd2mDSZ4dUYOgmQh2EnNbw11xZh3tEgGJ0BjTos9fXxm5XWE3OUiygx7oaHSPDhkfg75g7qwKoqjy5K8PrMJPkHgJebQuGKzKBYqPTDPGSxUFtq4QSJEra8h8LMsZdXoSiJXW68l6RWZvPE8cigc--3Jajt9HjooYjXDIOgHRsh7BFnn49bNcObvLmL3zb4DarC93CSL73ouKheHJslD7j8qIOQt4xTCPudo4Tkx2kPqTFytitF1BAXcS6nNfp0vzr8lKNK4-IJoDf8jV3VhcnkjyVz6mOE7FnzPsHo4g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
دبیرکل حزب‌الله: توافق دولت لبنان با رژیم صهیونیستی ذلت‌بار، ننگین و به معنای چشم‌پوشی از حاکمیت ملی است
🔹
ما در سخت‌ترین شرایط میدان نبرد را ترک نکرده‌ایم و هرگز نیز آن را ترک نخواهیم کرد.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 30.6K · <a href="https://t.me/akhbarefori/663915" target="_blank">📅 16:35 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663914">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ff3df40d49.mp4?token=dx6cnatKlkzDlyAhqqc8W4JaQ5UHUr_X-dtYgG1lIBWn9CEEQdzp6dD_55dWdPvCErzjKGHklHmXIqabWNUNzoD6DjGeBIPUdLwUfOhbXQwiVHMi_BOA5aouDaefUuFliOnZuR51Mni2Lf597CXV5MOGCLGXCcnU4iz8F9N3P_mX7IRKRPOgSWeXUX7glar-2GpElsr6AFDvH1l-evO3W07iJJBgg7kA_RNvoL4t5kaz78GCOkzUI-xfWjQ69G0c5PMEjh-RFjGZ6R4cXUo1eqwtagvMXvA2SXy6ZQNKGdf7NONXAngdrqaUTUYBe3WS-eFkUyhSBjgM7r3B3nKNsBREu0slMXLmO76xiblizsXC0rKcjXOnU9BlEIoLbfg6_0KHD_SlIzcyWam_tES8LFeHEsQQ6Ycnf4pEwKA-KLyGMYB9lHBkzrfBBgIbioXR62yESLyKumvbCPND6xK1hyjQWh-ZbpZIn7XqU_5_UJ3frVbAyygkIWeKjUuWwKwKg0SvIYha9Uv1x7KFCUGarR6h53NOK2eLJrIcH0VRbfvdyF7QDBtcUlE1Q2bcvLAT2gvwvlX4T60AvUEfvsTJPjOIpHYZ5oUBj4S7alXh-DuarbcU3upCWbOJosQOXzk05ahlOJkyeYi9PGRjcX0xKKvFxJ8LfNVWc-5PkScv9oM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ff3df40d49.mp4?token=dx6cnatKlkzDlyAhqqc8W4JaQ5UHUr_X-dtYgG1lIBWn9CEEQdzp6dD_55dWdPvCErzjKGHklHmXIqabWNUNzoD6DjGeBIPUdLwUfOhbXQwiVHMi_BOA5aouDaefUuFliOnZuR51Mni2Lf597CXV5MOGCLGXCcnU4iz8F9N3P_mX7IRKRPOgSWeXUX7glar-2GpElsr6AFDvH1l-evO3W07iJJBgg7kA_RNvoL4t5kaz78GCOkzUI-xfWjQ69G0c5PMEjh-RFjGZ6R4cXUo1eqwtagvMXvA2SXy6ZQNKGdf7NONXAngdrqaUTUYBe3WS-eFkUyhSBjgM7r3B3nKNsBREu0slMXLmO76xiblizsXC0rKcjXOnU9BlEIoLbfg6_0KHD_SlIzcyWam_tES8LFeHEsQQ6Ycnf4pEwKA-KLyGMYB9lHBkzrfBBgIbioXR62yESLyKumvbCPND6xK1hyjQWh-ZbpZIn7XqU_5_UJ3frVbAyygkIWeKjUuWwKwKg0SvIYha9Uv1x7KFCUGarR6h53NOK2eLJrIcH0VRbfvdyF7QDBtcUlE1Q2bcvLAT2gvwvlX4T60AvUEfvsTJPjOIpHYZ5oUBj4S7alXh-DuarbcU3upCWbOJosQOXzk05ahlOJkyeYi9PGRjcX0xKKvFxJ8LfNVWc-5PkScv9oM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ما هم خیلی دوستتون داریم
❤️
🔹
دمتون گرم که با وجود برخی بی‌مهری‌ها، آبروداری کردید
🇮🇷
🫡
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 32K · <a href="https://t.me/akhbarefori/663914" target="_blank">📅 16:33 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663913">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fc13100ba3.mp4?token=QqrMwI9PA95ReLuKS8wBFa2E1JAJXvLmSIlCfXWu4zkOGk6SxGblLaYGUnmkK5Bo9Y2j9Att8IjQbXocnH19IBjctsXq_D-KKbH9nLlteft8BEbvTerLuXecemtAZWq02PljDH0fiMoHMAcmicskrzNy9yidmsCL1h0Dg9oXDgTJ4uf1SyuZ5MfK91N79bG8gKb673RG-Levb3__WvfU-L-qpx1Gam5nKhX-NgVhygCjZKBwSoS6P8f9AoJ0m46G1kWRrgkYHiZlDRsTZYXzYahJursPeRLKdLxMUqpBgS9pb2WzSMjwQU9Re03EhZxzqHdMMVTmn90QmQrW-QkowbmvWnRQZJwkWLKYYm7FLdiJgZGwnC21FVu2UNH5pdOhxziqbDMVFo02SOo4WsNBFMNKirbHvs-tXxHN7_3WuCiRty23KPuIWeaCcXapNPNqYsAraY0ElTBQonmhx7wrecfDuLof7Bv2oYn6GvaTGatZGFDMrPMXZrHxyN5q2KbCNrpaJZ_msDp5hOrMsOOVyvi8EJ0dvYWL8I5_mWHPdPIoNu0Qj3LDhChElBMKj-v-odYvIYhoCH9RHlOQLNj7tMhX6JRD7Ss6hNSZIuT2s5dfidtHdQexXs8GkWOwCCinFcDyR81IVXqDjet1sdLbeTVdcx4nBCV505F8Os7Gg60" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fc13100ba3.mp4?token=QqrMwI9PA95ReLuKS8wBFa2E1JAJXvLmSIlCfXWu4zkOGk6SxGblLaYGUnmkK5Bo9Y2j9Att8IjQbXocnH19IBjctsXq_D-KKbH9nLlteft8BEbvTerLuXecemtAZWq02PljDH0fiMoHMAcmicskrzNy9yidmsCL1h0Dg9oXDgTJ4uf1SyuZ5MfK91N79bG8gKb673RG-Levb3__WvfU-L-qpx1Gam5nKhX-NgVhygCjZKBwSoS6P8f9AoJ0m46G1kWRrgkYHiZlDRsTZYXzYahJursPeRLKdLxMUqpBgS9pb2WzSMjwQU9Re03EhZxzqHdMMVTmn90QmQrW-QkowbmvWnRQZJwkWLKYYm7FLdiJgZGwnC21FVu2UNH5pdOhxziqbDMVFo02SOo4WsNBFMNKirbHvs-tXxHN7_3WuCiRty23KPuIWeaCcXapNPNqYsAraY0ElTBQonmhx7wrecfDuLof7Bv2oYn6GvaTGatZGFDMrPMXZrHxyN5q2KbCNrpaJZ_msDp5hOrMsOOVyvi8EJ0dvYWL8I5_mWHPdPIoNu0Qj3LDhChElBMKj-v-odYvIYhoCH9RHlOQLNj7tMhX6JRD7Ss6hNSZIuT2s5dfidtHdQexXs8GkWOwCCinFcDyR81IVXqDjet1sdLbeTVdcx4nBCV505F8Os7Gg60" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
طلا برمی‌گردد یا همچنان قیمتش سقوط می‌کند؟
@TV_Fori</div>
<div class="tg-footer">👁️ 31.6K · <a href="https://t.me/akhbarefori/663913" target="_blank">📅 16:28 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663912">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">♦️
ادعای سنتکام: حملات ایران به کشتی‌های تجاری را نادیده نخواهیم گرفت
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 38.3K · <a href="https://t.me/akhbarefori/663912" target="_blank">📅 16:23 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663911">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">♦️
العربیه به نقل از منابع آگاه: دور جدید مذاکرات در ماه ژوئیه در قطر برگزار می‌شود
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 35.4K · <a href="https://t.me/akhbarefori/663911" target="_blank">📅 16:15 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663910">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">♦️
ثبت‌نام زائران و میزبانان مراسم تشییع رهبر شهید در پیام رسان‌های داخلی
دبیر ستاد اسکان شهرداری تهران:
🔹
ثبت‌نام زائران و میزبانان مراسم تشییع رهبر شهید از طریق بات «باید برخاست» در پیام‌رسان‌های «بله»، «ایتا» و «سروش پلاس» آغاز شد.
🔹
زائران می‌توانند برای حضور در مراسم ثبت‌نام کنند و میزبانان نیز آمادگی خود را برای ارائه خدماتی مانند محل استراحت، پارکینگ، سرویس بهداشتی، آب آشامیدنی و سایر امکانات رفاهی اعلام کنند.
#بدرقه_یار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 37.4K · <a href="https://t.me/akhbarefori/663910" target="_blank">📅 16:15 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663909">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">♦️
منابع محلی در سوریه: ارتش رژیم صهیونیستی طی ماه ژوئن جاری میلادی، بیش از ۶۰ یورش زمینی به سوریه انجام داده است
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 35.2K · <a href="https://t.me/akhbarefori/663909" target="_blank">📅 16:11 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663908">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">♦️
هشدار نبیه بری درباره فتنه جدید علیه لبنان
🔹
رئیس پارلمان لبنان طی پیامی خطاب به مردم لبنان گفت: ای اهل لبنان، این فتنه است!
🔹
نبیه بری با بهره‌گیری از کلام مولا امیرالمومنین در نهج‌البلاغه تأکید کرد: در فتنه همچون "ابن اللبون" (شتر دو ساله) باشید؛ نه پشتی…</div>
<div class="tg-footer">👁️ 28.5K · <a href="https://t.me/akhbarefori/663908" target="_blank">📅 16:08 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663907">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7953310c8f.mp4?token=obS4xYefIQjB6Rtl0B9g30R5PNcOu71CQMDrir9JAeFIEp9UY85SSZS3hhUyvzxxpGWrp1sGsJzkJNfZxe04LupwA63Rg8MgIcXBUUqupOF92O6IyI9hO-oykJU5W1F-eCPSsFz9JN6wao2YLhDkBZ0q9zKgWZdb8Noo-kpiDYP7czU7y0VYidFQKczL5FOYl_RyG8lSV9eiDYX1beWMpYDshoLEjFZJGUuAzc8RbUJJkUn5So_XiUDWX4nRwefqULuiISXyJkvLKQO84aaSUS0TEYpVD15fF3SkggL-L0g5IGmPbdLOYGBpaIfAzh7-KPhc-LVGuQKtiDl85ZSaLw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7953310c8f.mp4?token=obS4xYefIQjB6Rtl0B9g30R5PNcOu71CQMDrir9JAeFIEp9UY85SSZS3hhUyvzxxpGWrp1sGsJzkJNfZxe04LupwA63Rg8MgIcXBUUqupOF92O6IyI9hO-oykJU5W1F-eCPSsFz9JN6wao2YLhDkBZ0q9zKgWZdb8Noo-kpiDYP7czU7y0VYidFQKczL5FOYl_RyG8lSV9eiDYX1beWMpYDshoLEjFZJGUuAzc8RbUJJkUn5So_XiUDWX4nRwefqULuiISXyJkvLKQO84aaSUS0TEYpVD15fF3SkggL-L0g5IGmPbdLOYGBpaIfAzh7-KPhc-LVGuQKtiDl85ZSaLw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
آبی که آتش را در آغوش می‌گیرد؛ اما خاموش نمی‌کند
🔹
چشمه آب و آتش شگفتی طبیعت در روستای اردشیر محله در نزدیکی ساری
#اخبار_مازندران
در فضای مجازی
👇
@akhbarmazandara</div>
<div class="tg-footer">👁️ 28.5K · <a href="https://t.me/akhbarefori/663907" target="_blank">📅 16:06 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663906">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ba81c97e2f.mp4?token=s3NzbfqLBxXRPOxBVA57xRHvzBi2NbjhlEYrfjfiPPS39SOj4JnpIIbO4_rc7YvTsaAku_cThwzXaonMh1bDhYx6zgkQG0ohDOb_TKLHREJbW-AVAw0iordFsPKg9ZOCPtffU-vks3jujGk_AAIVXRTF9OFJsQ-orO31dSIAqrFRJII98ZcmY1KRnBTSupTwUEmB42aKj1wi75dwkhCjlN8aqu9QPH404RKvUB2y-et3SVpxPdfoQQ9b-td9hBuMPFBvx9ZdrBSnI8lOL1geTPXQBm5IvLiHg5r0xYAFQCBuJXuOgHiIWbb-50XWzl0WvPLoRgzMVIfjf7a82X1aBw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ba81c97e2f.mp4?token=s3NzbfqLBxXRPOxBVA57xRHvzBi2NbjhlEYrfjfiPPS39SOj4JnpIIbO4_rc7YvTsaAku_cThwzXaonMh1bDhYx6zgkQG0ohDOb_TKLHREJbW-AVAw0iordFsPKg9ZOCPtffU-vks3jujGk_AAIVXRTF9OFJsQ-orO31dSIAqrFRJII98ZcmY1KRnBTSupTwUEmB42aKj1wi75dwkhCjlN8aqu9QPH404RKvUB2y-et3SVpxPdfoQQ9b-td9hBuMPFBvx9ZdrBSnI8lOL1geTPXQBm5IvLiHg5r0xYAFQCBuJXuOgHiIWbb-50XWzl0WvPLoRgzMVIfjf7a82X1aBw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
با این ۳ قانون، پول و دارایی‌هات رو مدیریت کن #دارایی_هوشمند
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 28.9K · <a href="https://t.me/akhbarefori/663906" target="_blank">📅 16:00 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663905">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GRMBZ0LrlE7RjxHgAp0yw2tZeZj2UoEfi3DXGKsUxOtB-cVFhZOSSgvdPnUjstF9LVS5sSbPK3NLRr-8CBDY2YG7QVff1Bny_JFxcwzhw21rSMnuzCBOOS-dTu3afIkJv8tWR0udCEO9ferSZxxxmeEg7K0WgDsolJiRGajzJ0xAC9K-9Paq5cVnFv0dLzoj-b1YusLtcsQuGp-V5fa4Wn2Xek61v6-N4pVrPwS4cBtAhA43X7VltJKDnxnxiwf_0BUrj2658gKGojmySg2eX1cgpQLaEdG2Ntrs4hH3b5s9RQGjN4clcg-wimSQeRerN1VWu6cNRWVBE6N3ftbvFQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
منفجر کردن خانه‌های مسکونی در جنوب لبنان توسط صهیونیست‌های جنایتکار
🔹
منابع خبری لبنان از منفجر کردن و تخریب خانه‌های مسکونی توسط نظامیان رژیم صهیونیستی در شهرک «الطیری» در جنوب لبنان خبر دادند.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 30.5K · <a href="https://t.me/akhbarefori/663905" target="_blank">📅 15:56 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663904">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e49d6ecf91.mp4?token=KAt6W9H-diYOdVoUGsgtGXsXoptw25xePTrqLQiDq_OPP1Y9DRJAtSHiNo0a9OiVgrkDNFPE0n_b_s3ABqTKadfko8ZVie2qP5RT2d2oiIZmdFxqegv4ZDq1B1lCSzx_IY4cYhZ3Kw5bQbC4tL4T8ju6Hd4Do8SEOp_-EYKWnzPhHaQd47VO0He5m2ZCrb9ziIXJatwgFRySKhwWmmV01Pu7d3lC7CaUL8jL8Z45cQmZaEdVukaSreQRFRx9ddbAz9fxkGEmX4GbX2mq1Y-134ZY6aZ0Ghqre_tOvXnmlWNlQQoSMMAJGshskspjiWmmHRTNpMgpng7TQi5YaxpI3A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e49d6ecf91.mp4?token=KAt6W9H-diYOdVoUGsgtGXsXoptw25xePTrqLQiDq_OPP1Y9DRJAtSHiNo0a9OiVgrkDNFPE0n_b_s3ABqTKadfko8ZVie2qP5RT2d2oiIZmdFxqegv4ZDq1B1lCSzx_IY4cYhZ3Kw5bQbC4tL4T8ju6Hd4Do8SEOp_-EYKWnzPhHaQd47VO0He5m2ZCrb9ziIXJatwgFRySKhwWmmV01Pu7d3lC7CaUL8jL8Z45cQmZaEdVukaSreQRFRx9ddbAz9fxkGEmX4GbX2mq1Y-134ZY6aZ0Ghqre_tOvXnmlWNlQQoSMMAJGshskspjiWmmHRTNpMgpng7TQi5YaxpI3A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
انهدام پست فرماندهی پهپاد اوکراین توسط روسیه
🔹
خدمه سامانه موشکی پرتاب چندگانه «اوراگان» ارتش روسیه، یک پست فرماندهی پهپاد اوکراینی را در نزدیکی شهر اورخوفو در منطقه زاپاروژیه منهدم کردند.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 29.8K · <a href="https://t.me/akhbarefori/663904" target="_blank">📅 15:52 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663903">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/c0cHTVBgV3HRe9skY7WJeX5Zwf0w8Swdtn6aI2RJr4WmIEP52Y6I6F8oucNzaoHkeWOgMGvvRpeBy2vFsPzVs7eNCGxhLsq0RqX073IyJI2px6NdGfazJfhXQccIarVJDWBON7SNwfsg6qr9LvjiVZ1j7rMIHmGi07QoKJRTqEvnQpVSZf82HIuyS3i7UwE2LT93reNoWtxtuRlp3chI09c1mzf80pa1Di3bYEjMrh3OLilk1nM2q6WiVluAkGXsdsilZZ7IGZHpCMWZO6Qa3xAaD_RnET1ehOBLivseIkYjAp6pQNBKduegWfndQs_2qHFAgUwXckSJIltuJmbEyQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
۸ کشور بازی جی‌تی‌ای۶ را ممنوع کردند
🔹
تاکنون کشورهای بحرین، چین، کویت، لبنان، عمان، قطر، روسیه و تایوان این بازی را ممنوع اعلام کرده‌اند.
🔹
نسخه‌های قبلی این بازی نیز به دلیل محتوای خشونت‌آمیز، مواد مخدر، قمار و محتوای جنسی در کشورهایی مانند تایلند، عربستان، امارات و استرالیا با محدودیت روبرو بودند.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 32K · <a href="https://t.me/akhbarefori/663903" target="_blank">📅 15:44 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663902">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">♦️
یورش نظامیان صهیونیست به رام‌الله
🔹
نظامیان رژیم صهیونیستی به شهر رام الله مقر تشکیلات خودگردان در کرانه باختری یورش بردند.
🔹
این یورش در حالی است که تشکیلات خودگردان همچنان به هماهنگی و همکاری خفت بار خود با اشغالگران ادامه می‌دهند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 32.3K · <a href="https://t.me/akhbarefori/663902" target="_blank">📅 15:37 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663901">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
زنگ خطر نیروی کار، کشور بیش از یک میلیون نفر نیروی اتباع بیگانه نیاز دارد
کامران پولادی، عضو کمیسیون امور داخلی کشور و شوراها در
#گفتگو
با خبرفوری:
🔹
وزارت کار قرار شد به مدیر کل استان‌ها ابلاغ کنند که به چه تعداد از نیروهای غیر ایرانی یا اتباع خارجی نیاز دارند و این‌ها صرفا باید برای مشاغل سخت باشد که ایرانی‌ها کمتر به آن تمایل دارند.
🔹
برآورد ما این است که به یک میلیون و ۱۵۰ هزار نفر نیروی اتباع بیگانه نیاز داریم تا زمینه عودت مابقی آن‌ها به کشورشان فراهم شود.
@TV_Fori</div>
<div class="tg-footer">👁️ 31.3K · <a href="https://t.me/akhbarefori/663901" target="_blank">📅 15:32 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663900">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0daa995301.mp4?token=WwkLqiWZ5N39WDd0lSE5WJMAxNSjWaCpOft12vURp45C5v3gHM2-euRQyVOgWInkdUD_u5N7L_yu563dUH4XzovMaBmxV-bW9UIq-PYNwE2gQ4756z39n5ZyMh9SUO-nhiD77PJmdxxgd91KEk4Xe5tsCuFHgJoyROmBhmOb8-stsSFGaawThiBGfJqMMuABcd2RB7ZzV0aW9g2qQsbXy7Hl8noioA15RlUB-kJynqg0AW-oS0_5htoBAC3ZVl4y0zd_RYRNJTC115ZTT6t4DXQ8pl_jG1nn7wmwxp_DNCvhYWXrWHcWhnDANQN1Fc1WkmUV6Y9WfKzy0JyZGfS-5g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0daa995301.mp4?token=WwkLqiWZ5N39WDd0lSE5WJMAxNSjWaCpOft12vURp45C5v3gHM2-euRQyVOgWInkdUD_u5N7L_yu563dUH4XzovMaBmxV-bW9UIq-PYNwE2gQ4756z39n5ZyMh9SUO-nhiD77PJmdxxgd91KEk4Xe5tsCuFHgJoyROmBhmOb8-stsSFGaawThiBGfJqMMuABcd2RB7ZzV0aW9g2qQsbXy7Hl8noioA15RlUB-kJynqg0AW-oS0_5htoBAC3ZVl4y0zd_RYRNJTC115ZTT6t4DXQ8pl_jG1nn7wmwxp_DNCvhYWXrWHcWhnDANQN1Fc1WkmUV6Y9WfKzy0JyZGfS-5g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
آخرین وضعیت سد امیرکبیر کرج
#اخبار_البرز
در فضای مجازی
👇
@akhbare_Alborz</div>
<div class="tg-footer">👁️ 41.4K · <a href="https://t.me/akhbarefori/663900" target="_blank">📅 15:28 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663899">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/972c49c3d1.mp4?token=aZ6kIDCT-mpczEYS0hZo1blVVDFqCI4b3aaX2EpEaRNLQjvREHAcyXCT2IfkOBwGj7HOHVIt_Txk6br9uF1a0oLm-fwUQun8tYtYVP0iUMaJLTKeh5bUyvuWV5yt--X3aY7R0uo_VPu_PGari1_gBHU9kRbQ7eRBXGZZGxvkm3FsQ9N7xYJ1g3FzzsBC1bPXojVMgIXWGUbWPWUf181U8TRzLkIOPWqW4Uywgp1mt2O908hUKpKlAFP8AyZeFmOfIemM5IPl3h421d2yyQkrLzmadSTu7Gt6AVf6pT2P3zKM8Kp58cxWt1b_YXnCxuId0oWurjJh5PLDmejIho9yBw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/972c49c3d1.mp4?token=aZ6kIDCT-mpczEYS0hZo1blVVDFqCI4b3aaX2EpEaRNLQjvREHAcyXCT2IfkOBwGj7HOHVIt_Txk6br9uF1a0oLm-fwUQun8tYtYVP0iUMaJLTKeh5bUyvuWV5yt--X3aY7R0uo_VPu_PGari1_gBHU9kRbQ7eRBXGZZGxvkm3FsQ9N7xYJ1g3FzzsBC1bPXojVMgIXWGUbWPWUf181U8TRzLkIOPWqW4Uywgp1mt2O908hUKpKlAFP8AyZeFmOfIemM5IPl3h421d2yyQkrLzmadSTu7Gt6AVf6pT2P3zKM8Kp58cxWt1b_YXnCxuId0oWurjJh5PLDmejIho9yBw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
رئیس پلیس راهور فراجا: هموطنان در تهران، قم و مشهد در روز وداع و تشییع پیکر رهبر شهید، خودروهای شخصی خودشان را از منازل بیرون نیاورند؛ شرایط ترافیکی منحصربه‌فرد است
#بدرقه_یار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 41.5K · <a href="https://t.me/akhbarefori/663899" target="_blank">📅 15:23 · 06 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>

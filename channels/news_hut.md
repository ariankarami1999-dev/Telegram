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
<img src="https://cdn4.telesco.pe/file/PH5jacSICzZKzBiPDv2r0mlDQ_Y_904WdWPvpCREQnv073_t-ocS4bMwqbqjvecaYtxToqbU5usJHXP3Le0nythdvwkQUwdFrH5k2UvsRq-mqaDWiDL-CdOq3CWVkJ2kSdqBrJe9NGc_wsky-GA_B3yq-RiSpjYcrOkxZM-AMzg5ZVVgi-ulG_MKjD1RP7veQen3JNrPN-0PN_piGvxa8TzXwA8_ZcbSAr8ZJa0ryjr_P6Jjtt7aXXN76_z5jEwysvnRF4cb56DHh0Dno61WrA4c79PzW21OaYu5vJLFsXCyKg1aPw_G01hpgVV5hzo2ZwmWz6uHaNrpBKNP9hyAxA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 هات نیوز | HotNews</h1>
<p>@news_hut • 👥 112K عضو</p>
<a href="https://t.me/news_hut" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 بدون هیچگونه گرایش و تمایلات سیاسی، همیشه سمت حقیقت و مردم.</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-13 12:42:35</div>
<hr>

<div class="tg-post" id="msg-71084">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/IQ6y9Co5kf_pkFfLMf4KyGoOs3JGbh0YGo1vR3IRHG1w8X8cRXvXtkcQQITt-vjDYwLMYZjuLHgQ90Z6Aea3_OghsZWGeFIYoWt_o1jSNVTncfBturrfabeUKhVCtdH6kA3u3rFFI5uS9rdk4o3zco4IEz0R6GODRqnM5bIxLAYYbIDpwCIXvwLDipn2tjFya9TwNIJYUD7mJjfnYy2Sr0MunHzCnq1wuMgrC0BmNYfUvzfsH9aJgteZ4cAycqq_nebOnuXuvtWGxorA8qfiY1G6_LEkLKUb0oe49sFfh0WHMLPDM0opPpQ_dZGxmMpd2SxCFa29LfCoAoanM1yY-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عرزشی با این پست به شدت میسوزه
😃
@News_Hut</div>
<div class="tg-footer">👁️ 4.04K · <a href="https://t.me/news_hut/71084" target="_blank">📅 12:12 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71083">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d0edd50344.mp4?token=n4IQYkMJFhjFZmo5TQP8lhyqnxA_k3tWVihR46gJX-6hVWwJJ6RJ-yT_V8m8XwB1vDLty_vjDtGYkcS3XcpRCcJR_EjtS8CrsZa6PQV93CNCnKmn-XzUdxjXkKxb0HknpSjwN89kprOFt654jwdGd5yB8TWmHuevbJ57NRSeVlNJid1fPnqUTyracfOP2vGjsB7sBz2886bnqAGWy3Ao6PnkjwZut29fqc-qiHIcxFWmHl06Or2PhgK3Py8-pUb90rW6UIEGhGB2AIsOZyJG5UjzdDE6K3d68rfhngepVMnlGrhr_yIie5jDoEoRDDnsLUxKhVgRyU62usw-Qo4XNw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d0edd50344.mp4?token=n4IQYkMJFhjFZmo5TQP8lhyqnxA_k3tWVihR46gJX-6hVWwJJ6RJ-yT_V8m8XwB1vDLty_vjDtGYkcS3XcpRCcJR_EjtS8CrsZa6PQV93CNCnKmn-XzUdxjXkKxb0HknpSjwN89kprOFt654jwdGd5yB8TWmHuevbJ57NRSeVlNJid1fPnqUTyracfOP2vGjsB7sBz2886bnqAGWy3Ao6PnkjwZut29fqc-qiHIcxFWmHl06Or2PhgK3Py8-pUb90rW6UIEGhGB2AIsOZyJG5UjzdDE6K3d68rfhngepVMnlGrhr_yIie5jDoEoRDDnsLUxKhVgRyU62usw-Qo4XNw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
ویدیو وایرال شده از طرفدار حکومت
🎙
خبرنگار:
از قیمت دلار خبر داری ؟
🇮🇷
طرفدار حکومت:
بله شده 200 و خورده ای
🎙
خبرنگار:
با این قیمت پس چرا اومدی اجتماعات ؟
🇮🇷
طرفدار حکومت:
دیگه باید قدرت تفکیک داشته باشید تو ذهنتون و قیمت دلار یه چیزه و بیرون اومدن یه چیز
اصلا اگه امنیت ما نباشه شما میتونید راجب قیمت دلار فکر بکنید؟ نه نمیتونید!
@News_Hut</div>
<div class="tg-footer">👁️ 5.15K · <a href="https://t.me/news_hut/71083" target="_blank">📅 12:01 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71082">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">⏺
ویدیو وایرال شده از اعتراض یه زن کارتون خواب:
به عنوان یک کارتون خواب که 20 ساله دارم این زندگی تجربه میکنم!
شما مسئولین که مردان خدا هستید شما دیگه چرا؟
تو دانشگاه رشته حقوق خوندم
@News_Hut</div>
<div class="tg-footer">👁️ 7.03K · <a href="https://t.me/news_hut/71082" target="_blank">📅 11:34 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71081">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d18ffbfe89.mp4?token=FaaPxyaAk3FRBRUI2o3kXWTYxiDrqwXV1UJMuzLxXXrfqpazC31wm1CLUHI2Mhn3gnpgDTqx0SMriF5I0t18AXb7pQltpuZAU1MxNmWzooTpNTSbMigkOMCvzaydg8TqbsKz9urgx_6sxAF8bS7uaonoIWX2IfSt7ZUFvNd-wAmrkFh12JqHtZNRCPOu-U1bK86wlfA8IByF-G6RxUWijxR-MWRrJEV-yycdSauzDi9hW1eRoYkOpZ27zM77NfqH1HZrSXXd9R3VukiD3LHriCvcM2_oSnOnQhpQuT_58HtwE6bpcmwKf4odOfgs58tS9Evk_KJRHpCpuGLlDt1N5Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d18ffbfe89.mp4?token=FaaPxyaAk3FRBRUI2o3kXWTYxiDrqwXV1UJMuzLxXXrfqpazC31wm1CLUHI2Mhn3gnpgDTqx0SMriF5I0t18AXb7pQltpuZAU1MxNmWzooTpNTSbMigkOMCvzaydg8TqbsKz9urgx_6sxAF8bS7uaonoIWX2IfSt7ZUFvNd-wAmrkFh12JqHtZNRCPOu-U1bK86wlfA8IByF-G6RxUWijxR-MWRrJEV-yycdSauzDi9hW1eRoYkOpZ27zM77NfqH1HZrSXXd9R3VukiD3LHriCvcM2_oSnOnQhpQuT_58HtwE6bpcmwKf4odOfgs58tS9Evk_KJRHpCpuGLlDt1N5Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
یه پسره دوست دخترشو برده تو کوچه پس کوچه ها بهش رانندگی یاد بده
آخرش هردو غافلگیر شدن
😂
@News_Hut</div>
<div class="tg-footer">👁️ 9.24K · <a href="https://t.me/news_hut/71081" target="_blank">📅 11:01 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71078">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8bc34fe3de.mp4?token=YyoVO1P2GtH24jESJVaaIy_eP9tnr3CWrCOWCDK9PuzaZebUFpInYS5VGe6PgAe6IbySFK4eFRYDP2hd4q-vOf3QKMM-JD9sBBpP_GTYphCLsB9cctUv7Hm2sRW3wzS_kiqyeIudzFBXVKXn7H2Kzzk7LzLURewQe6p5CjwrVxP5V1qPsk4zeTO7UH0KY-CHYtKuXD-o-ufQx0rjQeHXRSBvmQ-8qZSROzvVGC0CuVCmhKRlHpeAKTAIo-ekGCcGYJkU8WaF2K72ul00gdYpZLqxVhvV7xkfuBZjbN5YJhlDm-_e2YsFt8SUAZ5wH5CXxj2T820Wxs3o50m5tK_N-Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8bc34fe3de.mp4?token=YyoVO1P2GtH24jESJVaaIy_eP9tnr3CWrCOWCDK9PuzaZebUFpInYS5VGe6PgAe6IbySFK4eFRYDP2hd4q-vOf3QKMM-JD9sBBpP_GTYphCLsB9cctUv7Hm2sRW3wzS_kiqyeIudzFBXVKXn7H2Kzzk7LzLURewQe6p5CjwrVxP5V1qPsk4zeTO7UH0KY-CHYtKuXD-o-ufQx0rjQeHXRSBvmQ-8qZSROzvVGC0CuVCmhKRlHpeAKTAIo-ekGCcGYJkU8WaF2K72ul00gdYpZLqxVhvV7xkfuBZjbN5YJhlDm-_e2YsFt8SUAZ5wH5CXxj2T820Wxs3o50m5tK_N-Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
توی دزفول چند تا دزد میرن توی یه خونه مجهز به وسایل ضد سرقت و 3 کیلو طلایی که توی اون خونه بوده و قاحب‌خونه قصد داشته باهاش طلا فروشی بزنه رو میدزدن!
صاحب خونه شب قبلش توی اینستاگرام گفته بوده که میخواد طلا فروشی راه بندازه که این حرفا رسیده به گوش دزدا ؛
فردای همون روزی که این حرف رو زده وقتی صاحب خونه خانومش که باردار بوده رو وقتی میبره بیرون یه هوایی بخوره دزدا میریزن تو خونه و طلا ها رو میبرن.
حالا صاحب خونه گفته که هرکسی هر سرنخی از این دزدا داشته باشه و بهم بده ، 10 میلیارد تومن بهش پاداش میدم.
@News_Hut</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/news_hut/71078" target="_blank">📅 10:33 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71077">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0def551e36.mp4?token=V6RnHP5wpked8QWEnvRCkCkkA8FBcHianBdLu53zX3gZS5woaP0WQmAsEPRyN_zvLiAupQMctJAO6vYTAVCKBD6r_EXsRoEUJolCpa4hBvp7ksiPC3BpvJuXLHdGRybJv8_ksSVuxI8Btp46jKUjKDb1iKCqKkaiNuN3Wz8IzTp9KcMaMshkAJGjDs7JC6I4fu4OTFleG1MCoG3le5EbasPNKUmyphcrkBw0YlN_-ktaMcvvPpxPg2f4dSqWimRaO3FQ5feWkiJj4ZkJLtaBVToul3xU22ApOvnrD5wbIdgNLU5KDhyIe2Gg3c4GaD8SrZgfe0OSio7OoGjFq5BhHQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0def551e36.mp4?token=V6RnHP5wpked8QWEnvRCkCkkA8FBcHianBdLu53zX3gZS5woaP0WQmAsEPRyN_zvLiAupQMctJAO6vYTAVCKBD6r_EXsRoEUJolCpa4hBvp7ksiPC3BpvJuXLHdGRybJv8_ksSVuxI8Btp46jKUjKDb1iKCqKkaiNuN3Wz8IzTp9KcMaMshkAJGjDs7JC6I4fu4OTFleG1MCoG3le5EbasPNKUmyphcrkBw0YlN_-ktaMcvvPpxPg2f4dSqWimRaO3FQ5feWkiJj4ZkJLtaBVToul3xU22ApOvnrD5wbIdgNLU5KDhyIe2Gg3c4GaD8SrZgfe0OSio7OoGjFq5BhHQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
امروز یه دختره داشت تو قزوين واسه خودش قدم میزد؛
که یهو یه پیرمرده خواست مزاحمش بشه ولی بعد که فهمید طرف پسر نیست، عذرخواهی کرد و رفت
😳
@News_Hut</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/news_hut/71077" target="_blank">📅 10:02 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71076">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/4ba13b0e17.mp4?token=CByrzygJ4u5E7SiR6f-o36EE0OqYiK2wwHfwif7aXmG-O4J2EXTiCl1D4SCuO3bHm3669w4oxBhxxKvN8HwOKYEn3sCnbKr3EPEfHUyEccXqmZSDEFlFexA9NhqlgXC2EhnxMH8WiNF5i1LfF2wn5pCuI7OSCrwCSBEz7pOagz0rH7_CIN_kN6IGNuBAFt_iu1hGqqs7bDP3TRQwDOm_aLS1dpzaSyKMby8DVnwUBYJUYSB9owuTVdI3FJbgU8wuUVHVNwAc8YaDxOOGWN3hqGN2HKi7PA3bOo6X41R4LoqoZqHt84z5dSMUsFhNwy72-dFZVjfoJeplFi11S9xykA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/4ba13b0e17.mp4?token=CByrzygJ4u5E7SiR6f-o36EE0OqYiK2wwHfwif7aXmG-O4J2EXTiCl1D4SCuO3bHm3669w4oxBhxxKvN8HwOKYEn3sCnbKr3EPEfHUyEccXqmZSDEFlFexA9NhqlgXC2EhnxMH8WiNF5i1LfF2wn5pCuI7OSCrwCSBEz7pOagz0rH7_CIN_kN6IGNuBAFt_iu1hGqqs7bDP3TRQwDOm_aLS1dpzaSyKMby8DVnwUBYJUYSB9owuTVdI3FJbgU8wuUVHVNwAc8YaDxOOGWN3hqGN2HKi7PA3bOo6X41R4LoqoZqHt84z5dSMUsFhNwy72-dFZVjfoJeplFi11S9xykA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
لحظه دستگیری یه قاتل فراری در ایرانه
:
قاتل با چاقو مامورا رو میزنه و داشت فرار میکرد که یکی از مامورا عین راموس تکل زد و طرف افتاد.
بعدش یکی دیگه از مامورا ویلچر برداشت و میکوبید تو سر و بدن قاتل تا بیفته زمین، هر لحظه این فیلم عجیب‌تر میشه.
@News_Hut</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/news_hut/71076" target="_blank">📅 09:32 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71075">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/L229KRy5cpPbotHr68bBeJhKkdJbdTUq4uO4EiPuU21HrKC1Qgae9C1Nrj3J5tbt8_Nh34dO_JVx_g9LD-doX8GzfkA5EJuBuQqsoW6U-ukMRWic5gZx-Trby7NtagwhwSH2D4L60a0y0iYAcZf4O3FCt0vhJyNskQic1zRpUHLpXpREGuNrl6nYSeekaIC-RA-dzFUIwJulHH4b2RfWjok9-iIwvELHsa6xtOdV78hJVeunvJorAu2QpHt9IBWgOuxnb2VSNWZ0rZktBLLrF843uYEXqBadNQVOG6IJE883jC1fu9HO41qnTv4zFrvns9EAqh4IO4sUjA4pFplROg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
⭕️
🇺🇸
⭕️
#فوری
؛اسکات بسنت وزیر خزانه‌داری آمریکا:
اتحادیه اروپا رسماً به «عملیات طرد اقتصادی» (Operation Economic Outcast) پیوسته است و ما از موضع قاطع و زودهنگام آن‌ها قدردانی می‌کنیم.
ایالات متحده در کنار متحدان خود قاطعانه ایستاده است تا اطمینان حاصل کند که رژیم جنایتکار ایران نمی‌تواند از سیستم مالی جهانی برای تأمین مالی جاه‌طلبی‌های هسته‌ای، برنامه‌های تسلیحاتی و نیروهای نیابتی تروریستی خود بهره‌برداری کند.
جهان پیام روشنی به رژیم ایران می‌فرستد: ما تا زمانی که آخرین شریان حیاتی مالی باقی‌مانده قطع نشود، از تلاش دست نخواهیم کشید.
@News_Hut</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/news_hut/71075" target="_blank">📅 09:03 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71074">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/news_hut/71074" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/news_hut/71074" target="_blank">📅 01:26 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71073">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fuGU0xv4iee-utA3CjLyCILacar9pXg4B-rTPLdwq-41eU7JvhcyrhRv6GI52IkeD3NBzN3JnMqXMPvbZXBS4J1-pP4TCOslgSTnoLGv6TdopciNdP545fGfh4SjAer176mwTMwh1rBrPVjA1neRp4ZSfnqkhRLhQ1Z7INkRmzw0mHV-FyKVBTdgepgi4vBG99LDwZTbNssuU5awj75_J7PoIUCrTQx4dJtRihbru3F5kKHV7ebmKDH3pBC35SPz7iyPoLNTvjA3NKwbe_4Cd8WVgRgqxhCOZd-3yPpi0A-OEF7NGtpm9aSwKHrWxmQFhlHCuFxeXm7v7oh81eM2zA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🦖
فقط یک بازی از میکس‌ت لوز شده؟
پولت برمی‌گرده!
میکس می‌بندی، هیجان بالا میره، اما یکی از انتخاب‌هات خراب می‌شه؟
با پیشنهاد ویژه
TrexBet
، در صورت رعایت شرایط، می‌تونی
۱۰۰٪ مبلغ شرطت رو پس بگیری
.
همین الان وارد سایت شو و شرایط آسان‌ش رو مطالعه کن!
💰
🦖
🦖
🦖
🦖
🦖
بونوس صدرصدی اولین واریز
🦖
واریز آسان، برداشت سریع
🦖
سرعت بالا، طراحی حرفه ای و تجربه ای متفاوت
https://TrexBet.com
T.me/TrexBet_Ir</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/news_hut/71073" target="_blank">📅 01:26 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71072">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">🚨
🇮🇷
نایا:ایران چندین موشک به سمت کشتی ها در تنگه هرمز شلیک کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/news_hut/71072" target="_blank">📅 01:14 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71071">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c46c090035.mp4?token=LSJero3CKIeNm5fA_N95-6dvX4d9GkbTeIS-DU45VBdtXTHBOiXH04KLF9gYb6yoeAjPlZvXNJpx-jFZeGUWiiIV7j3NXaAh9CwDNDJV-ILLmXS6mmU1DP9dPE_cOAv25iORShAFGqZBbZgolyIaMY_HkhTJA2RSKxhbeBN7Fw2-13olhog70FQi123YEmIP51dd-5cE5SaUVqjdctCE5ywpI_IisIQzfsO9tmqrEvPg4pF9xgahIL4YCb4xb99GdoRQZ5DcL6chTDeC8BzOFHY-qdj2Tr-vDWT6nr5LH6iEHuN4Sy8DkB9-xujvHhmSLjDIkIN7Teik_BCGhrpKKg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c46c090035.mp4?token=LSJero3CKIeNm5fA_N95-6dvX4d9GkbTeIS-DU45VBdtXTHBOiXH04KLF9gYb6yoeAjPlZvXNJpx-jFZeGUWiiIV7j3NXaAh9CwDNDJV-ILLmXS6mmU1DP9dPE_cOAv25iORShAFGqZBbZgolyIaMY_HkhTJA2RSKxhbeBN7Fw2-13olhog70FQi123YEmIP51dd-5cE5SaUVqjdctCE5ywpI_IisIQzfsO9tmqrEvPg4pF9xgahIL4YCb4xb99GdoRQZ5DcL6chTDeC8BzOFHY-qdj2Tr-vDWT6nr5LH6iEHuN4Sy8DkB9-xujvHhmSLjDIkIN7Teik_BCGhrpKKg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
پورمحمدی:
انسداد تنگه هرمز، برنامه‌ریزی شهید پاکپور بود.
شهید پاکپور پیش‌بینی کرده بود که جنگ با ترور او شروع می‌شود.
شهید پاکپور برنامه‌ریزی کرده بود که اگر جنگ آغاز شد و او دستوری صادر نکرد، فرماندهان ۲۰ دقیقه بعد شلیک کنند.
@News_Hut</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/news_hut/71071" target="_blank">📅 00:22 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71070">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/46300e7107.mp4?token=cZm6DIdrnwEiiQttWi5390cFNTMjU7hUVnblRHwTqK7xph8FKd8kbtwi4nRjYaPzPjMFnIFqghYQqWq6647re4dwJuXt8uyxEtllUuBdprWxmiEbFzdIReJ_ejkXWNz_sTqRjAKhfMOfnt-R8PzEJstoNe_5imwnDv-mdQL9990j3rBYFxYAvAhpsHwoY1XkXqVe0rMaNXBBJ41X39zv62ZaMEXyq03uHFbsiorGHNjFulLjTthiu7B-OXiGOzT6CpeibgGG0-R3hw_SEbTaDWnlctgpRjrUpLJbv_hDWhPLDBP5yEqOznK2bE1Lxwkt08CpVtwiNiWatDWISCjvNQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/46300e7107.mp4?token=cZm6DIdrnwEiiQttWi5390cFNTMjU7hUVnblRHwTqK7xph8FKd8kbtwi4nRjYaPzPjMFnIFqghYQqWq6647re4dwJuXt8uyxEtllUuBdprWxmiEbFzdIReJ_ejkXWNz_sTqRjAKhfMOfnt-R8PzEJstoNe_5imwnDv-mdQL9990j3rBYFxYAvAhpsHwoY1XkXqVe0rMaNXBBJ41X39zv62ZaMEXyq03uHFbsiorGHNjFulLjTthiu7B-OXiGOzT6CpeibgGG0-R3hw_SEbTaDWnlctgpRjrUpLJbv_hDWhPLDBP5yEqOznK2bE1Lxwkt08CpVtwiNiWatDWISCjvNQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
چندشب پیش تو شیراز یه دعوای عجیب رخ داد؛
دوتا دختر با ماشین میزنن به ماشینِ دوتا پسر؛ بعد گفتن ما مقصر نيستيم و داشتن فرار میکردن!
پسرها هم گفتن چون بی‌ادبی کردی، باید بمونی خسارت بدی، بخاطر همین پریدن رو کاپوت ماشینِ دختره که فرار نکنه!
این وسط یه پیرمرده هم خیلی بی‌دلیل از دختره کتک خورد...
تهشم دختره گفت دیگه این موضوع واسم مهم نیست چون زنگ زدم شوهرم سروان شهریزی، الان میاد کون همه‌تون رو پاره میکنه.
@News_Hut</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/news_hut/71070" target="_blank">📅 23:31 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71069">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/876466a913.mp4?token=ZT8ApHwRyvtfU29pJoW3FuZGmHWHMKrxR0ufYqlq3T2Kx3hUBFVstJF3nwwR5QVZHOtHkKjoc9R_IEkpdkWtvkxsVP-b9WiVnbgfgqCf9ZqzT4GjQdGL05Y72pWgArZJEgipV5t5VrDkHX7tzxHDd-NCkPKBNWTSQasdOCYrIhUi4uFoe0u-nzkH6M6Vkje7wFqpo081u67IjJiEonUuSRA3I4YiBoZ3sSU0B1g7sw8DepWqWkVjEfKkOvCwk4vxzBPqJa3LUJzei1MLlRDTGSahQTlwGxjmLIuMSz-zbqdIrHsLRiyhD2KmvGhtRtkTgTY6crS07xOjW6L7Hl4hvQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/876466a913.mp4?token=ZT8ApHwRyvtfU29pJoW3FuZGmHWHMKrxR0ufYqlq3T2Kx3hUBFVstJF3nwwR5QVZHOtHkKjoc9R_IEkpdkWtvkxsVP-b9WiVnbgfgqCf9ZqzT4GjQdGL05Y72pWgArZJEgipV5t5VrDkHX7tzxHDd-NCkPKBNWTSQasdOCYrIhUi4uFoe0u-nzkH6M6Vkje7wFqpo081u67IjJiEonUuSRA3I4YiBoZ3sSU0B1g7sw8DepWqWkVjEfKkOvCwk4vxzBPqJa3LUJzei1MLlRDTGSahQTlwGxjmLIuMSz-zbqdIrHsLRiyhD2KmvGhtRtkTgTY6crS07xOjW6L7Hl4hvQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
طبق گفته خانم دکتر؛ دیگه خوردن واژن خانم‌ها نه تنها دیگه نباید باعث خجالت شما بشه بلکه پر ازخاصیت و فواید زیادیه که تاحالا درجریان نبودیم!
@News_Hut</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/news_hut/71069" target="_blank">📅 23:02 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71068">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EYJSeRUVM7xx6lwcnNceBB6ma-suY0s9-ZAlPMfTnnBRf51XG0gAwSAysjgEkEAIDRtbgpGFN-BfTchmkCloVKhuUEQz4y2qWa9Xay6dJl-6aVNcOjMKNXAGxuWlPHyPywUA-q-c6Ixy1jTBgYgCerYzUH8S2qAodrfx_wp63VN_zXj_aqsGtaasX2HPbtp_pqA0TJEU-3EP8kGVmdc4Q1mlX9nmflw6I0eOLfRibOXxPhxhFrBKHS-b7rxmhGqbpWrdAVTbF3IMw6PHvIBpQRlch40fuYttFNsNDV-M6nFuKlqj3KG2VcnRgV7hatY10G3BMqy-sr8FWGKJwjNKGA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
قالیبافِ:
قهرمان، محکم‌تر «شورت» (Short) کن؛ طوری که انگار آینده‌ی شغلی‌ات به آن بستگی دارد (چون واقعاً هم همین‌طور است).
یا اینکه سطح ذخایر را به زیر «منطقه خطر» برسان و فرو ریختنِ آن حفره‌های عظیم (و البته نابودیِ شغل خودت) را تماشا کن.
یا هم به درگاه خدایانِ نمکِ «برایان ماوند» (Bryan Mound) دعا کن.
دنیا که از همین حالا بساط پاپ‌کورنش را آماده کرده است :)
@News_Hut</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/news_hut/71068" target="_blank">📅 22:20 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71067">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8f701b5944.mp4?token=PpOSKbTYi3Y-vbvE9AwqpYnXsB3uTyOBasQ0J8z0SL8gUYIdPyJXhF2E0OwzI8V70h48B3OPV0M4Wqr6nADQLtfD_bCXA3IKleewEahHW12dyS0lamf-cFY268XSxONYkQyIVNXf4zh8i1xIvkGdXiMutp7t8fsh3H-QVKFAYM4tln9QnLN9QSKFf6VwxP-RVfVDdG5GrL1iJclBfk0gm8XJM2luLIoHq0bYeQnI0BzKdk-1zggr-h1U2K2gW6cXCWUNkp0pHXHwuJtqdNyNz3peD_GtzrTueWYU4yra3okGG_vJiwuUXaE8NJ0thRpcogFFY7u_ltWI3Rxi9wY8aw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8f701b5944.mp4?token=PpOSKbTYi3Y-vbvE9AwqpYnXsB3uTyOBasQ0J8z0SL8gUYIdPyJXhF2E0OwzI8V70h48B3OPV0M4Wqr6nADQLtfD_bCXA3IKleewEahHW12dyS0lamf-cFY268XSxONYkQyIVNXf4zh8i1xIvkGdXiMutp7t8fsh3H-QVKFAYM4tln9QnLN9QSKFf6VwxP-RVfVDdG5GrL1iJclBfk0gm8XJM2luLIoHq0bYeQnI0BzKdk-1zggr-h1U2K2gW6cXCWUNkp0pHXHwuJtqdNyNz3peD_GtzrTueWYU4yra3okGG_vJiwuUXaE8NJ0thRpcogFFY7u_ltWI3Rxi9wY8aw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
⭕️
ارتش اسرائیل تپه علی طاهر در جنوب لبنان را فتح کرد و کنترل آن را در دست گرفت.
ارتش اسرائیل پاکسازی دو مسیر تونل زیرزمینی حزب‌الله در رشته‌کوه علی طاهر در جنوب لبنان را به پایان رسانده و در تلاش برای خنثی‌سازی آنهاست.
لشکر ۳۶ کنترل عملیاتی رشته‌کوه را در بالا و پایین زمین به دست گرفت و آن را از وجود شبه‌نظامیان پاکسازی کرد. برخی کشته و برخی دیگر فرار کردند. خنثی‌سازی زیرساخت‌های پاکسازی‌شده در حال انجام است.
در داخل، نیروها مراکز فرماندهی، اتاق‌های تسلیحات، اتاق‌های ژنراتور، محل‌های زندگی، دوش‌ها و یک آشپزخانه را یافتند -- که به شبه‌نظامیان اجازه می‌داد عملیات جنگی را انجام دهند و برای مدت طولانی در زیر زمین بمانند.
@News_Hut</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/news_hut/71067" target="_blank">📅 22:13 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71066">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GWKrALVaXLGcJ82N5Ca4MeGhx9bfxSLsBJCt3Y-EVilINnYmahIZxN3PSpPiHHPo2AgdUD00XPawXSFn-FPux8d_ufbexh6T5JvEtLeRrmvj3mCUxAUU3yDSQKnQsnl78xr9_bZgWDuVVZqkzSYdQ1Zj5uuJZbbcGhUjlRreYQZ6m8SnBeuOVXEmsa1yHqlkJxuQA7SkCdzV5qdQz0LUIdaC8jpgwMH0WFDzbxT2eRzBFSHLpJzknHzur8cdzLqu7BKYopAEv0DG3CX1ug1NXxvDMYpEAD4lT4yN1tmKEoNFQ7u6FLCTdFb9te_yYeaBQdb2-SrjKR3fPqYkfTHA6g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خرید حضوری با اسنپ‌پی، یه خرید معمولی نیست؛ شانس بردن BMW داره!
😎
🚗
با اسنپ‌پی می‌تونی از بیش از ۲۰ هزار فروشگاه حضوری خرید کنی و هزینه‌اش رو ۴ قسطه و بدون سود و کارمزد پرداخت کنی.
🎉
🥳
همه‌اش همین نیست؛
۵ هفته، ۵ برنده، ۵ جایزه در هر هفته هم در انتظارته:
🏆
۵ گرم طلا
📱
گوشی Galaxy S25FE
📱
گوشی iPhone 17
💻
لپ‌تاپ MacBook Air M4
🎮
کنسول PS5
این شهریور، حضوری خرید کن و شانس بردنت رو بیشتر کن:
👇
👇
👇
https://l.snpy.ir/iozfb
https://l.snpy.ir/iozfb
https://l.snpy.ir/iozfb</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/news_hut/71066" target="_blank">📅 22:13 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71065">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/af33ae7319.mp4?token=thHqyNxX_uioUg1bhj7SVTmKdWpO59zuHeiqf0_ecM2nAyYf5EdHCi-cjbB_6brs90Ax9l1utU83tObUUVpKTBMuFv2NvKwDpOp1A_A1xOE4xZ8PZT_efct4Ed3BRyBTyWnci1EQSrEtk9d2bKuwE19l7DmNINYQZw5X9kz8_4CHY7Y2zlS7mVdkkHw6RJjLwGAyqX5wuk_diyziQcqxM9eCEJt-DP7J7iYUWnQBBRP6M3utcMdIchtbWSdyVBDrPAI2GidLoPrAlbdHUdpjBpS3NXyrDFoKJ2Ui5fKxD8fEiWy4q56soT6znSCDS61NcAi32-r0NUVrnagYxme4LJABt9C9zrrhWjmdqI22WwBHG6Ul2BKwC-gGz6sQAA6iYdL3EwlfDpwEzOHpHApoPGQdgEJUw1Ox8yPNlTO3HPKrKL-kQG8RMEwpKhp1tttHW1rMDgknBpIOsvJzci7hM6KNfSlyuggCtD2qIQYiEfv9yWdU5PdXM_JJTG0Rtfza81mbTqnJh2rgMLAkr1s_VQ98mYRaAME00JaBcV6HFlcj-rEJht1de1oP1uYYsdX_tX7jO8VvtCG_Jzs3u2IO4jWaFNMDAwHkfxFoi9gLcv2AJ0YRPOvFx7odMr_Z65v0aSiNBycLU8PGDpFnu5xh6Yk9rNVjnnml1qe8mfMjHis" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/af33ae7319.mp4?token=thHqyNxX_uioUg1bhj7SVTmKdWpO59zuHeiqf0_ecM2nAyYf5EdHCi-cjbB_6brs90Ax9l1utU83tObUUVpKTBMuFv2NvKwDpOp1A_A1xOE4xZ8PZT_efct4Ed3BRyBTyWnci1EQSrEtk9d2bKuwE19l7DmNINYQZw5X9kz8_4CHY7Y2zlS7mVdkkHw6RJjLwGAyqX5wuk_diyziQcqxM9eCEJt-DP7J7iYUWnQBBRP6M3utcMdIchtbWSdyVBDrPAI2GidLoPrAlbdHUdpjBpS3NXyrDFoKJ2Ui5fKxD8fEiWy4q56soT6znSCDS61NcAi32-r0NUVrnagYxme4LJABt9C9zrrhWjmdqI22WwBHG6Ul2BKwC-gGz6sQAA6iYdL3EwlfDpwEzOHpHApoPGQdgEJUw1Ox8yPNlTO3HPKrKL-kQG8RMEwpKhp1tttHW1rMDgknBpIOsvJzci7hM6KNfSlyuggCtD2qIQYiEfv9yWdU5PdXM_JJTG0Rtfza81mbTqnJh2rgMLAkr1s_VQ98mYRaAME00JaBcV6HFlcj-rEJht1de1oP1uYYsdX_tX7jO8VvtCG_Jzs3u2IO4jWaFNMDAwHkfxFoi9gLcv2AJ0YRPOvFx7odMr_Z65v0aSiNBycLU8PGDpFnu5xh6Yk9rNVjnnml1qe8mfMjHis" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شیر ترامپ هم اومد به بازار
😳
@News_Hut</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/news_hut/71065" target="_blank">📅 21:30 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71064">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/40c15e0881.mp4?token=bySGzUU-aQ9ANWaRchy0RIuWWkYVqYRfTwL9d0icxI14gwLDyTIns5xIviDFOdcMpGlHKfPx3WKNpfjWFyqvKX96uU0Ii8d93bsu4UJolDzpLLd4KKY4xRvfB3007nM1PjcML1-4CPo_oXntD4cAJCFqUZqN_8vrDG1M3U9xGWhkCJkFh0rF32xcC3HUBcZjjZVrau_JokJJUHlebRcpNU95hZBTILvTUj9d-y_THI4hjZG4mXEzS2h4G1R9LUfnXheeNV8SVA6EhGqOhu6IhIMhHtCTblXAdUncAc7hY9RCpQl7jaLHbI4XjbdgBkLBtcH5a9nIi7VXW9pCUmnZfg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/40c15e0881.mp4?token=bySGzUU-aQ9ANWaRchy0RIuWWkYVqYRfTwL9d0icxI14gwLDyTIns5xIviDFOdcMpGlHKfPx3WKNpfjWFyqvKX96uU0Ii8d93bsu4UJolDzpLLd4KKY4xRvfB3007nM1PjcML1-4CPo_oXntD4cAJCFqUZqN_8vrDG1M3U9xGWhkCJkFh0rF32xcC3HUBcZjjZVrau_JokJJUHlebRcpNU95hZBTILvTUj9d-y_THI4hjZG4mXEzS2h4G1R9LUfnXheeNV8SVA6EhGqOhu6IhIMhHtCTblXAdUncAc7hY9RCpQl7jaLHbI4XjbdgBkLBtcH5a9nIi7VXW9pCUmnZfg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚠️
رقص عجیب «حسن حسین خانی» مداح نزدیک به حکومت  در حالی عجیب  و  با شلوارک! تو یک  ویلا با آهنگ شماعی زاده
@News_Hut</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/news_hut/71064" target="_blank">📅 20:46 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71063">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0392122fc9.mp4?token=XXaRxiB0kADk10ZUznd7JqUc4yIm2YUzc0jCb9lmFItHkuKgaswafUKkjQJudFbzXuIxLoZ9NWq2f_D-8CaAL6zV2sSvpWj3c-C3I1gybeE69LE3RVqg2wLbsh-m_Pcldarv0tkc340LjfBkC7LX3IHTm88_dTYZd0vKw9kKaK3RmIeJ9C2nbuZEjbgB9ECbpN3XWcLIkJsGGZ25wkjNfTmdWWu_RmGj_dGpziEEwGTAeoNFiTrBR8tMBQRocCGh_hKfBCtHXW4WzyRXS9H4I4KlEorCdbXuDynVyFd_sw6m2ncDtpev9N8AR5iZaQYlwQzU3oe-xIUJeZSbqLcD8Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0392122fc9.mp4?token=XXaRxiB0kADk10ZUznd7JqUc4yIm2YUzc0jCb9lmFItHkuKgaswafUKkjQJudFbzXuIxLoZ9NWq2f_D-8CaAL6zV2sSvpWj3c-C3I1gybeE69LE3RVqg2wLbsh-m_Pcldarv0tkc340LjfBkC7LX3IHTm88_dTYZd0vKw9kKaK3RmIeJ9C2nbuZEjbgB9ECbpN3XWcLIkJsGGZ25wkjNfTmdWWu_RmGj_dGpziEEwGTAeoNFiTrBR8tMBQRocCGh_hKfBCtHXW4WzyRXS9H4I4KlEorCdbXuDynVyFd_sw6m2ncDtpev9N8AR5iZaQYlwQzU3oe-xIUJeZSbqLcD8Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🇮🇱
#فوری
؛نخست‌وزیر نتانیاهو درباره ایران:
من به توانایی‌مان برای از میان برداشتنِ یک‌بار برای همیشهٔ این تهدید ــ یعنی سرنگونی این رژیم ــ اطمینان کامل دارم.
این همان مأموریت اصلی است که همچنان پیشِ رو داریم، اما به تحقق آن نزدیک شده‌ایم. این کار غیرممکن نیست؛ بلکه کاملاً دست‌یافتنی است.
آن‌ها بی‌دلیل از حمله به ما پرهیز نمی‌کنند؛ آن‌ها به همه حمله می‌کنند، جز ما. آن‌ها از قدرت ما، توان بازوی ما و عزم راسخ ما آگاهند.
من خطاب به دشمنانمان به‌طور کلی می‌گویم: با ما درنیفتید. اگر درسی گرفته‌اید، بدانید که نباید با ما دربیفتید.
@News_Hut</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/news_hut/71063" target="_blank">📅 19:55 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71062">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">🚨
شلیک موشک/پهباد از سیریک به سمت کشتی ها در تنگه هرمز
@News_Hut</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/news_hut/71062" target="_blank">📅 19:31 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71061">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/X6xAI2GzfLzlWJy7RHSJvxPBUPRpaCxrD7VBjhwQofDAlAmr81MBRcjcoDKh7K3hge8OEphhQQh_SmPyUFppg8hh1YDUwvOxZU8qZuCe0pcrS4sK2gEsf-AQS2eeZIRXXjYulLEmRdZawZDpvcNhkXtgWEfJjId6Zpz-ehGveqDConplQAF8Nqgh_RoFfM3UTwie9YlqwiqJTjeslMVHrts6RRRf3COwbYIpP6pSOJrSQnoeVuRkWQPh56-RHBW7iUAf7lKtX3BEL-hzUeiBauDw_zepBfGOOKEtmxutvkx0qvPC6RW8Tw2KkKt9pCpaqGzj1-xXuOgq-OCY7pgi3w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
🇺🇸
ترامپ در تروث:
برای آن مشتی خائنِ پست‌فطرت که از گزارش دقیق عملیات نظامی ما در ایران خودداری می‌کنند، باید بگویم که ما ذخایر تقریباً نامحدودی از مهمات با کیفیت متوسط تا عالی در اختیار داریم؛ بسیار فراتر از آنچه ممکن است برای این عملیات یا هر جنگ احتمالی دیگری (که وقوع آن بسیار بعید است!) نیاز داشته باشیم.
علاوه بر این، ما در حال تولید مهمات با حجمی بی‌سابقه هستیم. ما در حال انباشت و آماده‌سازی برای مقابله با هرگونه وضعیت پیش‌بینی‌نشده‌ای هستیم که ممکن است رخ دهد.
ما این مهمات را برای خودمان — یعنی ایالات متحده — نگه می‌داریم و فعلاً به دیگران نمی‌فروشیم، هرچند فروش به متحدان به‌زودی از سر گرفته خواهد شد.
همچنین، لازم است بدانید که دولت بایدن حجم بسیار بیشتری از مهمات را — بدون دریافت هیچ‌گونه هزینه‌ای — به اوکراین واگذار کرد، که این مقدار بسیار فراتر از مهماتی است که ما در ایران به کار گرفته‌ایم.
صدها میلیارد دلار کمک رایگان به اوکراین و ناتو اعطا شد؛ هزینه‌هایی که اگر از اروپایی‌ها خواسته می‌شد، خودشان آن را می‌پرداختند.
با این حال، ما آن پول را مطالبه خواهیم کرد، هرچند با کمی تأخیر!
@News_Hut</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/news_hut/71061" target="_blank">📅 18:52 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71060">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d21cce2e5e.mp4?token=RrVx6eYDM55RBPVrBG_TaB89Ehlh3xTjhNBaQDSDukZspShnLHCMNvtBKG6H5KE-osbdxj8tfDkFBEwUzZbTy4nLyDPb5AetDcnxI4UtVV3X8I32Gt0SWzvuzjb-dj4mjsQm5POmNNL9IuhsINm4H2xW8zOXQ_sCEwr_ROwvVLmPumMA3RXklhWbidYFeyqgWR5yAwWyfa8AV_wsNyOKJJ4-QbOSXr8KSKBSEpfyJhzEX2Z-5FAKr95HIdNSzadXoyulHIzgR_DbI00N81K3xmHM2SiS2toi1jmxbrZ4idP_PH6FBvxZEm05xG3wAi5Zv6Phw7vjMEP-40eYJewlwA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d21cce2e5e.mp4?token=RrVx6eYDM55RBPVrBG_TaB89Ehlh3xTjhNBaQDSDukZspShnLHCMNvtBKG6H5KE-osbdxj8tfDkFBEwUzZbTy4nLyDPb5AetDcnxI4UtVV3X8I32Gt0SWzvuzjb-dj4mjsQm5POmNNL9IuhsINm4H2xW8zOXQ_sCEwr_ROwvVLmPumMA3RXklhWbidYFeyqgWR5yAwWyfa8AV_wsNyOKJJ4-QbOSXr8KSKBSEpfyJhzEX2Z-5FAKr95HIdNSzadXoyulHIzgR_DbI00N81K3xmHM2SiS2toi1jmxbrZ4idP_PH6FBvxZEm05xG3wAi5Zv6Phw7vjMEP-40eYJewlwA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
مجری:
کسانی که دوستتان دارند، شما را فردی خوش‌برخورد، شوخ‌طبع، سخاوتمند و بذله‌گو می‌دانند؛ اما دیگران می‌گویند که شما سخت‌گیر، متکبر، مغرور و حتی بی‌رحم هستید. به نظر شما، کدام‌یک از این توصیفات درست است و کدام نادرست؟
❤️
شاهنشاه آریامهر:
بی‌رحم؟ گمان نمی‌کنم.
متکبر؟ قطعاً نه.
مغرور؟ شاید کمی. اما در مورد کشورم—و آنچه به دست آمده است
نمی‌توانم شخصاً دچار غرور شوم، چرا که انسانی مؤمن هستم. من عمیقاً به خدا ایمان دارم و اهل عرفانم؛ پس چگونه ممکن است مغرور باشم؟
انسان در پیشگاه ذات ازلی، هیچ است؛ مطلقاً هیچ؛ گویی اصلاً وجود ندارد.
البته با نگاهی به دستاوردهای این کشور، قطعاً دلیلی برای احساس غرور و سربلندی وجود دارد.
اما بی‌رحمی؟ این ویژگی من نیست؛ این نهادهای حکومتی هستند که باید عمل کنند.
وظیفه آن‌هاست که کسانی را که قصد آسیب رساندن به این کشور را دارند شناسایی و خنثی کنند. اگر نام این کار بی‌رحمی است... خب، در آن صورت باید بپذیریم که در این مورد با هم اختلاف‌نظر داریم.
@News_Hut</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/news_hut/71060" target="_blank">📅 18:26 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71059">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/259e330a05.mp4?token=aVMExSXhPKqxLWa7gtHfFkRFsKUKnmCpiTVipPykT4W9KOA_eMg8gTrdKNuSb-WJQj83YkdrfDy42lQzShzNVXBEZz9KF0IHyQ_NH74qb2I8I-61V-FZQzB7UDfRMX2EvZe3nJSY2m1MzTKj5vsrsTdrdxS3fd-BdS2begsztrZAGSZ_Fpa1_EpoNukgq6dFKAqk52GNT7x8L1fhulTklTYYukg1WBiXkSGPipSfcgUO0s9dxOPLIdORlrLs5SsXs0Sdez1iGZUFoCrVguCnQQqA6QjKlPl9VlTkm2hoFw-XrwW3XqtByBRxss6nVSGLOi8bZioSlnfADUQylb6DUw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/259e330a05.mp4?token=aVMExSXhPKqxLWa7gtHfFkRFsKUKnmCpiTVipPykT4W9KOA_eMg8gTrdKNuSb-WJQj83YkdrfDy42lQzShzNVXBEZz9KF0IHyQ_NH74qb2I8I-61V-FZQzB7UDfRMX2EvZe3nJSY2m1MzTKj5vsrsTdrdxS3fd-BdS2begsztrZAGSZ_Fpa1_EpoNukgq6dFKAqk52GNT7x8L1fhulTklTYYukg1WBiXkSGPipSfcgUO0s9dxOPLIdORlrLs5SsXs0Sdez1iGZUFoCrVguCnQQqA6QjKlPl9VlTkm2hoFw-XrwW3XqtByBRxss6nVSGLOi8bZioSlnfADUQylb6DUw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🎙
صحبت‌های این پسر درباره‌ی اونایی که میگن کسایی که ریش ندارن کونی هستن رو با هم ببینیم:
کدوم مادرجنده‌ای اینو باب کرده که هر کی که ریش‌وسیبیل نمیذاره، کونه؟
شما برو فیلم سوپرا رو نگاه کن، عمو جانی کونش هم یدونه مو نداره، چه برسه به صورتش.
ریشو کسایی میذارن که ترس از کون‌شون دارن، اونایی که عقده دارن و بچگی کون‌شون گذاشن، ریش میذارن.
خیلیا ریش دارن ولی صد مرتبه از کونیا بدتر هستن
@News_Hut</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/news_hut/71059" target="_blank">📅 18:16 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71058">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/news_hut/71058" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/news_hut/71058" target="_blank">📅 18:16 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71057">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VJHDJrvM0uY_OAfvdv8zSG47LgSFiVg2_-rAISf22_mgZXBm3r0lMU5D1Ft6n1Gg1K-HbDAzjmVfPeqvKWZ0ajGjvFaF9I-MfOIEmRNgcxHos_uU-zVW5PMxNniCGV6Elbglv7nlMy8kR7SklDpVlBY7GIs4VzZbpV4yPTUmF4BBSVthVVpuNkWNJRQnUuWnvNOwWGtTGUaSasOOyypYoTY_cC4GV5vmTcKHjDbL_NCovCBs6g9WsonNGDidJE1TquLvsNis7zPa6BLmLw1sUkInGJVhRIwgDOFkFv_2_4y8XfS3WY--0_cb7q7j1Zb1wEH_hA6lsj8Ibkwo8ZS01Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تیرکس‌ بت می‌بردت وسط هیجان
US Open!
🎾
🔥
🦖
رقابت‌های نفس‌گیر، امتیازهای سرنوشت‌ساز و هیجانی که تا آخرین ضربه ادامه داره!
🦖
بونوس اولین واریز تا سقف ۱۰۰ یورو
🦖
بهترین ضرایب بین تمام سایت‌ها
TREXBET — PLAY. PREDICT. WIN.
https://TrexBet.com
T.me/TrexBet_Ir</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/news_hut/71057" target="_blank">📅 18:16 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71055">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TAsZnDtw0R0NDTTpXT6hrPcI97ul6ugfHoLAnxOwrO1Zq_WKuuCFWtof1riZzTw1Mow37tUjwKVr96NoB9Y4NmoZD9IvL45LiJBCqq5KSwuuPSaopwGCPFOBTQL_1H0luYHAkqce_4UUrPdk4LggEHeVQGJDuxDDE7JMk_7rnMBffQinqZ_deOy_gyvbxTlRhaTKdYcK6_paX0uLQNGETlnZXexo9YJxzxtlf17-3gB4WZRlPbMUT0uDRwKmYhXKDIS1ukICTyU2R0ATgyKLvsUyPJIcETYHwzsSY73PHAHx7jvz4rLXvW-_fzWYHv2oWgLpAYfD8ldb50P5Wmrcgg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">〰️
💬
🙂
پست جدید تلگرام در پلتفرم ایکس:
حس و حال بامزه‌ای دارم، شاید بعداً عکس‌های نودم رو منتشر کنم!
@News_Hut</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/news_hut/71055" target="_blank">📅 17:32 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71054">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LLAfpojiBjs7iJM4ks3rgtjXHGGFAeARNU7rds10ZQMelphYrRCC0QZYnzkPGL_-76eLTYeNJ5LsBx1jACsjAfOAuW0EO1KjPpv3V-qK_WkuwA74dRKhAmyp7QUzRq3_IRBYtkjPufLeRP5fVe8GcP4XZnHybATb0WX_52q1AbbKaFR0yGxV3Ojbi2X3J4KeDGUN61K0a6fc7L1q7NrGWrWJxCnGE7qEJ6K4FcaVlWHD47XRllJcOOTwmSAGpIqJEQMxB5KV5dccOpg4yT3Abfrxe9cCrheMp7t2a3UcCSnLBJzlgwQ5x2Wk-rDaNc-VhKWAGyZNP4jd9XAYXwORWg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
جمهوری اسلامی کشته شدن سه خلبان نظامی در حملات آمریکا در دو شب گذشته را تأیید کرد.
اسامی: مجتبی باقری و حامد اوکاتی (خلبانان هوانیروز/هواپیمایی نیروی دریایی) و حسین مهدویان (خلبان نیروی هوایی).
@News_Hut</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/news_hut/71054" target="_blank">📅 16:41 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71053">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/03924aeb44.mp4?token=SHO0WlWDXb074odm41a3_4VsWK0rqm4Dwd0oBhmAbvMmMf-6xm9pM95h-pMblNhwbXhDquBr52DtrakAs1esyrBz7RB53M1071x0HaKSbubnwBu965nHiq0E88HZDdnQrlNOD9hgn0Bnlt-gx-dmxWjAqeW5xklh18jGf_cb__YvDNi5k2IrsvwJ857DqBc-1t9e1caUk3U6WfuqrjF84B-wA9D-5acyLZOxpSj77NpBMlHvqMvnrB4BAkKJr-fj-214w9uXL04N19z7xDy6JirMuYGNRYMBKBWOMEHQ8-NBmmNOvTLAjR2IbsJmRDsrwAD5HvzUzHM0PYCwLQXEbw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/03924aeb44.mp4?token=SHO0WlWDXb074odm41a3_4VsWK0rqm4Dwd0oBhmAbvMmMf-6xm9pM95h-pMblNhwbXhDquBr52DtrakAs1esyrBz7RB53M1071x0HaKSbubnwBu965nHiq0E88HZDdnQrlNOD9hgn0Bnlt-gx-dmxWjAqeW5xklh18jGf_cb__YvDNi5k2IrsvwJ857DqBc-1t9e1caUk3U6WfuqrjF84B-wA9D-5acyLZOxpSj77NpBMlHvqMvnrB4BAkKJr-fj-214w9uXL04N19z7xDy6JirMuYGNRYMBKBWOMEHQ8-NBmmNOvTLAjR2IbsJmRDsrwAD5HvzUzHM0PYCwLQXEbw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
تو ایتا و روبیکا با انتشار این فیلم نوشتن سامانه پدافند لیزری جدید اومده و همه موشکا و پهپادای آمریکا رو با لیزر زده.
@News_Hut</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/news_hut/71053" target="_blank">📅 16:32 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71051">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/94edb900f7.mp4?token=meln53nV3zFAWRjvnF0EyabOxLGm3CGf5fxmskxQU9LFIWdNgLfC7Ox-JJoDeoCt_2sFIeiRFL3GNxcpAA-q8QUTYDEjjV8rTx4wUa0FqRhHMxAe84j6FL_nDRZ_22wEcGUapDZkTAVuBGuff_UwkwRclrjH_Mqoi7gW3vJj1GmAJ7ypi9TFTfgj4laEhsPJV3ym9bflgF3JJ9ZHJ41MzvOE5eZwUVkw_pgh8LxKhbebY-U6MNMGVBLmc3dUBHwtDNT1xeN1rSCpacbNFGTwhzTvfvLvFebQ9h8GDXlY3hIxhnyB0MIrJAurOhiP3BciVYcOio4B_KIvN4qJctkrEg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/94edb900f7.mp4?token=meln53nV3zFAWRjvnF0EyabOxLGm3CGf5fxmskxQU9LFIWdNgLfC7Ox-JJoDeoCt_2sFIeiRFL3GNxcpAA-q8QUTYDEjjV8rTx4wUa0FqRhHMxAe84j6FL_nDRZ_22wEcGUapDZkTAVuBGuff_UwkwRclrjH_Mqoi7gW3vJj1GmAJ7ypi9TFTfgj4laEhsPJV3ym9bflgF3JJ9ZHJ41MzvOE5eZwUVkw_pgh8LxKhbebY-U6MNMGVBLmc3dUBHwtDNT1xeN1rSCpacbNFGTwhzTvfvLvFebQ9h8GDXlY3hIxhnyB0MIrJAurOhiP3BciVYcOio4B_KIvN4qJctkrEg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
این کلیپ از یه دختره که سر سفره عقد، آقای داماد رو سورپرایز کرد و گفت من مهریه نمی‌خوام و فقط 14 شاخه گل بنویسید
؛
هیچی دیگه پسره دیروز طلاقش داد و اونم با 14 شاخه گل رز طبیعی قرمز  یک جلد قرآن برگشت خونه باباش...
@News_Hut</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/news_hut/71051" target="_blank">📅 16:04 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71049">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/01429c982d.mp4?token=EbinAKrZA_sk7XSW6uf4ZuZdp8BLhxgycTXg-F7BieE8fIHsvmc18nf65XVHtp2h9o3uxtq4ar9cGqniAXSSCQ82r3LZt9YR_p3vNTM6LhkwwV9V45XYwWJHwCZ54VKzhw6GngFWYgJCrV9NOJXRUrtvtd2B3PFQpRRh00O0V160RdHSHI0SQbFShLLXx9POlqKQRnRxhr8dbyobNTynromeOyL3aVto9KZBUkJFMA9sDAGo8IPju9Yn2dWUUpD0oR8pZNKqLYc05s2cB9ESlqjQt0trp07mXZ0gVPZueGiHpR5UgJW9tVfoaPJPsUT1XUt6xoNwhzeSy942x-F9vg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/01429c982d.mp4?token=EbinAKrZA_sk7XSW6uf4ZuZdp8BLhxgycTXg-F7BieE8fIHsvmc18nf65XVHtp2h9o3uxtq4ar9cGqniAXSSCQ82r3LZt9YR_p3vNTM6LhkwwV9V45XYwWJHwCZ54VKzhw6GngFWYgJCrV9NOJXRUrtvtd2B3PFQpRRh00O0V160RdHSHI0SQbFShLLXx9POlqKQRnRxhr8dbyobNTynromeOyL3aVto9KZBUkJFMA9sDAGo8IPju9Yn2dWUUpD0oR8pZNKqLYc05s2cB9ESlqjQt0trp07mXZ0gVPZueGiHpR5UgJW9tVfoaPJPsUT1XUt6xoNwhzeSy942x-F9vg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
دیروز، اولین ایونت مد و فشن توی تبریز برگزار شد و حسابی غوغا کرده.
@News_Hut</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/news_hut/71049" target="_blank">📅 15:34 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71048">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/7913d873f1.mp4?token=aLXOFbwWVKRX6lr6uszpRFDaX6MNQ9AyXzZnO3oCIKh-b2ClRRCTIvosGfWxA4drfi82VEZK7wkrGJ4mDNSYfoGuZHaOWS6Jky_Jd9mUvT3NYemiLEcqff_toihuXMtEJq_Daj6J1o-6fYCJbgYhx6PlVQ9O1fw4AmS1W5dHpqheUFExdWnwhROvF5t3hMI0aB8Yn3P5Le7x4OroBvATi56GFO0Tu43BE8o3cRzkGAU99sJSKosuZUcgjvtUhV9ONP6nV3Q24MqA_Sqm-mt5p5QA9VEK3LBI3VJuBdGWM-k0k5XmmiDPUa8wsRg3xmGp7lej8fvMlke-HaMZhSXBeg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/7913d873f1.mp4?token=aLXOFbwWVKRX6lr6uszpRFDaX6MNQ9AyXzZnO3oCIKh-b2ClRRCTIvosGfWxA4drfi82VEZK7wkrGJ4mDNSYfoGuZHaOWS6Jky_Jd9mUvT3NYemiLEcqff_toihuXMtEJq_Daj6J1o-6fYCJbgYhx6PlVQ9O1fw4AmS1W5dHpqheUFExdWnwhROvF5t3hMI0aB8Yn3P5Le7x4OroBvATi56GFO0Tu43BE8o3cRzkGAU99sJSKosuZUcgjvtUhV9ONP6nV3Q24MqA_Sqm-mt5p5QA9VEK3LBI3VJuBdGWM-k0k5XmmiDPUa8wsRg3xmGp7lej8fvMlke-HaMZhSXBeg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
این کلیپ در مورد پسرای زیر ۳۵ سال که موهاشون سفید شده، در حال وایرال شدنه
@News_Hut</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/news_hut/71048" target="_blank">📅 15:01 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71047">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aIJc4Qq26UnaDoWpQynHwpHK2MblW9IPJaaA1oX_eI_A-C9Fj58QQe135j1mfeLbUrGfFYU20wIdA4ftXuyffFQ_9ovMYab2UQMENbRps67P5oX-mYT1vHkP6q5Cmv7mbTn0ya8WO-gmhPguzhW9oziY1zeIAYzu_BUCkOJeTJYD71H5_r-ybu20Rd8PnUwf25frVEgXJoDfWqyHWKygECBYvOpwcrtRbD5XZpK2lKAw8hkRr6UK9OyG2jWSHkJhUllArL8CfsT7GMO4zbKIxyN4GJoaR5wUwV9t7ZD3v3Sl_h_xO-ebiDywDeva_GSGW4-DG3UvTjvFXtlxykLcsQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
خبرگزاری میزان وابسته به قوه قضاییه، روز پنجشنبه ۱۲ شهریور ماه اعلام کرد حکم پرونده صادق ساعدی‌نیا، فرزند محمدعلی ساعدی‌نیا، در دیوان عالی کشور تایید شده و او به ۱۲ سال و ۶ ماه و یک روز حبس تعزیری، مصادره کلیه اموال منقول و غیرمنقول و محرومیت از اشتغال به شغل کافه‌داری محکوم شده است.
مرکز رسانه قوه قضاییه این پرونده را مرتبط با اعتراضات سراسری ۱۸ و ۱۹ دی سال گذشته دانسته و مدعی شده است که متهم در «تحریک اعتراضات و ورود خسارت به اماکن و اموال عمومی در استان قم» نقش داشته است.
صادق ساعدی‌نیا، فرزند محمدعلی ساعدی‌نیا، کارآفرین و نیکوکار ایرانی است. محمدعلی و صادق ساعدی‌نیا در جریان انقلاب ملی ایرانیان در دی ماه گذشته دستگیر و اموال هزاران میلیاردی آنان مصادره شد.
@News_Hut</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/news_hut/71047" target="_blank">📅 14:30 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71046">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">🚨
🇮🇱
اسرائیل کاتس، وزیر دفاع اسرائیل:  اگر ایران به دولت اسرائیل حمله کند، این اقدام اسرائیل را از هرگونه محدودیتِ موجود برای حمله به ایران رها خواهد ساخت. ما به تمامی زیرساخت‌های ملی، نظامی و غیرنظامی ایران - از جمله زیرساخت‌های انرژی - حمله خواهیم کرد و ایران…</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/news_hut/71046" target="_blank">📅 13:58 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71045">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7750e2ea67.mp4?token=cPjbLPvHX9tPeBwQ8L3tnT5s4gMSCYuTp_j6TgYJHP3pdkVtaznfRZvtNkWAGc5KdhqYmNoXw7r2UUlLWCQ2D_SOWqTyw6HazeIH-t959z9O7csho5AI48eSTktrM8KoTbRY7P2pzoK5LrgmJ06iuYMmSk7w2o1KgVlCm_FhPHvNrB5Pv2bhApspOAAMswRFEQYQX3WWV_dGAc_fkWPbxyBEaNJmB46_h-Y695C_1JqLl7uZDHhK4wRPQZoQ98qU8hMvhvu2mvadDv7q-XyhE_gM5JH7MYpLLBFGSZSz_gIWTeXdEIQmgjA_JH4ZuWEC-5rf1ieVmg16vJrTc2DJIQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7750e2ea67.mp4?token=cPjbLPvHX9tPeBwQ8L3tnT5s4gMSCYuTp_j6TgYJHP3pdkVtaznfRZvtNkWAGc5KdhqYmNoXw7r2UUlLWCQ2D_SOWqTyw6HazeIH-t959z9O7csho5AI48eSTktrM8KoTbRY7P2pzoK5LrgmJ06iuYMmSk7w2o1KgVlCm_FhPHvNrB5Pv2bhApspOAAMswRFEQYQX3WWV_dGAc_fkWPbxyBEaNJmB46_h-Y695C_1JqLl7uZDHhK4wRPQZoQ98qU8hMvhvu2mvadDv7q-XyhE_gM5JH7MYpLLBFGSZSz_gIWTeXdEIQmgjA_JH4ZuWEC-5rf1ieVmg16vJrTc2DJIQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇮🇱
اسرائیل کاتس، وزیر دفاع اسرائیل:
اگر ایران به دولت اسرائیل حمله کند، این اقدام اسرائیل را از هرگونه محدودیتِ موجود برای حمله به ایران رها خواهد ساخت.
ما به تمامی زیرساخت‌های ملی، نظامی و غیرنظامی ایران - از جمله زیرساخت‌های انرژی - حمله خواهیم کرد و ایران را به اعماق دوران حجر و تاریکی بازخواهیم گرداند.
﻿
@News_Hut</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/news_hut/71045" target="_blank">📅 13:51 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71044">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/80b05262cb.mp4?token=gP4dez5ZLS2Dvn0bB35IITMH6p4UML1o9namrznt7O2wv4i9bs6GGj0AIqY7s_JU762YjM-4oAVsmqWt3IyHY7c7ta_aoJQxAn77UEiePrBJf4-2P3pMEt1plV4F062GiH249yPYTrmK-xepB49fOgKxfODkmiptw8NVKFDXxyfRB0zR7GPnGBa1xrRVYvhrArSNNkgQGuoYdj7QarY5jHcTBBCOY5W_PBjTb3SIh2VFexaRvb09AK5JzMqQXCxChr-eVolW2KVErwZpH3y3-WDOLjVVdAREIjWULPQp_bdDn5hUBp8ut--LjMZRis3jBaYQPITJW-e0y5TLNktujw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/80b05262cb.mp4?token=gP4dez5ZLS2Dvn0bB35IITMH6p4UML1o9namrznt7O2wv4i9bs6GGj0AIqY7s_JU762YjM-4oAVsmqWt3IyHY7c7ta_aoJQxAn77UEiePrBJf4-2P3pMEt1plV4F062GiH249yPYTrmK-xepB49fOgKxfODkmiptw8NVKFDXxyfRB0zR7GPnGBa1xrRVYvhrArSNNkgQGuoYdj7QarY5jHcTBBCOY5W_PBjTb3SIh2VFexaRvb09AK5JzMqQXCxChr-eVolW2KVErwZpH3y3-WDOLjVVdAREIjWULPQp_bdDn5hUBp8ut--LjMZRis3jBaYQPITJW-e0y5TLNktujw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇦
جنگنده میگ-۲۹ام‌یو۱ اوکراینی یک موشک اس۸۰۰۰ «باندرول» روسی را در ارتفاع پایین با یک موشک آر-۶۰ منهدم کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/news_hut/71044" target="_blank">📅 13:21 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71043">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/162568634d.mp4?token=bDulJXWWcs0-p-H0py8se4Ei2zMejmquFH9_kYpY1b5QN8gTu80e_oBiJfiXgyo3LTr_ltnP7adUaI6C0A3bHwzPfioko5HuDRm7t-wg7tzGxXhfGGi2h6q5IoKdRBFeXuWjYJrCp3lKBGo7ZGzeNWFoU4DEXAxOtv66q78eyCUITnMEeTxoJtLWa47A5LhHy5jhgJOa-TI27ohC95PlgCCQQaX7ZWY30zHA1FDdx1RkIU0le04GjH7DVXniI8qDJre9FzF_kmEGR2-C0aby4OvgTDb5jUJ_1TEBmergY4zXlEhyZy1pt5E3IX0V0ufULhXP1tQe-Sn80eQrQ_5L5g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/162568634d.mp4?token=bDulJXWWcs0-p-H0py8se4Ei2zMejmquFH9_kYpY1b5QN8gTu80e_oBiJfiXgyo3LTr_ltnP7adUaI6C0A3bHwzPfioko5HuDRm7t-wg7tzGxXhfGGi2h6q5IoKdRBFeXuWjYJrCp3lKBGo7ZGzeNWFoU4DEXAxOtv66q78eyCUITnMEeTxoJtLWa47A5LhHy5jhgJOa-TI27ohC95PlgCCQQaX7ZWY30zHA1FDdx1RkIU0le04GjH7DVXniI8qDJre9FzF_kmEGR2-C0aby4OvgTDb5jUJ_1TEBmergY4zXlEhyZy1pt5E3IX0V0ufULhXP1tQe-Sn80eQrQ_5L5g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
🇮🇷
روابط عمومی ارتش:
در ادامه سلسله عملیات‌های صاعقه و در مرحله سی و یکم،  در انتقام خون پاک مردم بی‌گناه و دلاورمردان نیروهای مسلح، بامداد امروز، ارتش جمهوری اسلامی ایران، «سامانه‌های ارتباطات ماهواره‌ای»، «انبارهای تجهیزات» و «آشیانه هواپیماهای جنگنده» ارتش تروریستی آمریکا در پایگاه احمد الجابر کویت را با موشک‌ها‌ و پهپادهای انهدامی، مورد اصابت قرار داد.
@News_Hut</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/news_hut/71043" target="_blank">📅 13:20 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71042">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/news_hut/71042" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/news_hut/71042" target="_blank">📅 13:19 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71041">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aYRrzw3IDK_mKg8wZWwTGRzBrBTqQQCOZ3EV-5vO1rO1fKqvkCJ_JZyB0YvoHAWmSJByD7c1z6q8ramTYq1AOtUfCpc3pUBQXDJbI2qCT9Klk2ZIhxspXkNoqTkQRmdqAjUO5fKhM_acXIS8PZiLEbxTrDLIfNEVV8CzrCOCqUEhyucPro0eqS5OZ7NNe31NfHRfgjjkI8n2ri1z5xgwNu5lfQipkeF8odyZwjDit0u8wrHCilDW-IohCLAaHW1p3fzLDJyqgdcS3Yn7ul8gGJ1Cjn5S7GCQ-w2YJjXrE8csoQ-fTPrLUp8x0Hu7DK9T8OarKtdQJtqnVINuMyXNTA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🦖
با اولین واریز، بیشتر دریافت کن!  فقط در سایت جهانی
TrexBet
🦖
بسته خوش‌آمدگویی ویژه
TrexBet
تا ۱۰۰٪ بونوس واریز
🦖
تا ۱۵۰ چرخش رایگان در ۴ واریز اول
🥇
واریز اول:
۱۰۰٪ بونوس + ۳۰ چرخش رایگان
🥈
واریز دوم:
۵۰٪ بونوس + ۳۵ چرخش رایگان
🥉
واریز سوم:
۲۵٪ بونوس + ۴۰ چرخش رایگان
🏅
واریز چهارم:
۲۵٪ بونوس + ۴۵ چرخش رایگان
🦖
🦖
🦖
🦖
🦖
🦖
TREXBET — PLAY. PREDICT. WIN.
https://TrexBet.com
T.me/TrexBet_Ir</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/news_hut/71041" target="_blank">📅 13:19 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71040">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2218c2694e.mp4?token=CV_sxf_xR_TH7YLdHi3lhkmz7hQyihA9AM8wkwuaJerWDwLSuEagr_vmmfh5Bn8FCsj_ivoNuoWrt-2k6U5SF5QISPotKtt7dIV22hUbUjv_ve7T0nEV8gb7nv1Zl0BbSoGP2hPoncM_0B4nSEGllhNYE1TzyGl2qXU7XIbdz8AEStYxi-iA0FRLWmXWHp6zhh-y7G_k42FKmxMGYQqJ_aMoPBImmFydplyayQbb0kWzcVe8GE8yzuM0h3DqI829LhKhPDsjbnJQfOFsy_qMMwSnVasQTKPbMGSg1ccM84CqM1IFSs35ckNCczo77tb6VFBow3NUxyK7s4ma0Kq5LQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2218c2694e.mp4?token=CV_sxf_xR_TH7YLdHi3lhkmz7hQyihA9AM8wkwuaJerWDwLSuEagr_vmmfh5Bn8FCsj_ivoNuoWrt-2k6U5SF5QISPotKtt7dIV22hUbUjv_ve7T0nEV8gb7nv1Zl0BbSoGP2hPoncM_0B4nSEGllhNYE1TzyGl2qXU7XIbdz8AEStYxi-iA0FRLWmXWHp6zhh-y7G_k42FKmxMGYQqJ_aMoPBImmFydplyayQbb0kWzcVe8GE8yzuM0h3DqI829LhKhPDsjbnJQfOFsy_qMMwSnVasQTKPbMGSg1ccM84CqM1IFSs35ckNCczo77tb6VFBow3NUxyK7s4ma0Kq5LQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
تو میدون تایمز نیویورکِ آمریکا، یه خانمِ چاقو بدست بعد از اینکه یه مرد و یه زن رو از ناحیه شکم زخمی کرد، بعد از اخطارِ پلیس‌ها به سمتشون حمله‌ور شد و به این شکل بهش شلیک کردن و کشتنش.
@News_Hut</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/news_hut/71040" target="_blank">📅 12:33 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71039">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/17f52d28bc.mp4?token=fFNrpk3GCNe-I_s5m_dhQ9xYKfd1zlvx86rqPEVTT6CzawTT7KwMcJ1bu2FNfIsvAZkbzP71ovFz0XG05-VxXMv7z9LqLsOSITSp3NJdHrCZF1GdHOtSGeA3qACcqAwZLZsAIs5N7Kk5IDv_D55_Zz1eUdO-Uxww9ZW16JciL3hHIIlcK_fz9XC4m0YVThjg_7TRJOYJiHqdRT9UVQnTFvLtNs0VnXQo5-BypedwxPCmbQcrCa2kQpxyhx2rYjodguuNWMAvhKj3tRhfw3h5cwOlw6coxZFLekJZ2HJ6KPd6Aq0ywldFVX_c6RJMABdBDRTpzAxUHtffha9Kp269hg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/17f52d28bc.mp4?token=fFNrpk3GCNe-I_s5m_dhQ9xYKfd1zlvx86rqPEVTT6CzawTT7KwMcJ1bu2FNfIsvAZkbzP71ovFz0XG05-VxXMv7z9LqLsOSITSp3NJdHrCZF1GdHOtSGeA3qACcqAwZLZsAIs5N7Kk5IDv_D55_Zz1eUdO-Uxww9ZW16JciL3hHIIlcK_fz9XC4m0YVThjg_7TRJOYJiHqdRT9UVQnTFvLtNs0VnXQo5-BypedwxPCmbQcrCa2kQpxyhx2rYjodguuNWMAvhKj3tRhfw3h5cwOlw6coxZFLekJZ2HJ6KPd6Aq0ywldFVX_c6RJMABdBDRTpzAxUHtffha9Kp269hg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
سایپا تو ماشینی جدیدی که زده ماشین با اینکه راه نمیره ولی براش کیلومتر حساب میکنه
@News_Hut</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/news_hut/71039" target="_blank">📅 12:01 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71038">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rTDecJNySuAW8LzENNc_4yiBBBjM8GdVSr3Exti-drYy_p__bxiHL301to4xsQhX0N1mx5nnB-p3JYZ_gYmsns3RBEGDA8gFejI-39DNdxnEFE7h-Xc4zWt2yS6PtnJZlXKxDywchKhXPQG9AXZWVOuB-VgY_MYLp-xrthFhevcqHkkmEV-_EHJFMD0Biu1gPlG836wp_bOiIh4QsSnEtx48j_-8jDqZPS8UKTc5ITLyfEOmFsvXuvwMrh3KOET-5udbOBjDLzSGVj4438r0DcrI2qKhDYJ6N9gR9EGSKdcRA5dgWffUw31AfUbaehMGzcTX9xLAc0EuLsr1IUK7nQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
📰
اکسیوس:استیو ویتکاف، فرستاده کاخ سفید، آخر هفته گذشته در ساردینیا با شیخ طحنون بن زاید آل نهیان، مشاور امنیت ملی امارات متحده عربی، درباره ایران دیدار و گفتگو کرد.
این دو مقام درباره گام‌های احتمالی آتی بحث و تبادل نظر کردند؛ چرا که دولت ترامپ در پی بازگشایی تنگه هرمز و هم‌زمان افزایش فشار اقتصادی بر تهران است.
امارات نقش کلیدی در تلاش‌های تحت رهبری آمریکا برای عبور نفت‌کش‌ها از این تنگه ایفا کرده و در راهبرد تحریمی واشنگتن، کشوری مهم محسوب می‌شود.
مقامات اماراتی به دولت آمریکا اعلام کرده‌اند که هرگونه کارزار مؤثر فشار اقتصادی باید شامل تمامی کشورهای عمده‌ای باشد که همچنان به تجارت با ایران ادامه می‌دهند.
@News_Hut</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/news_hut/71038" target="_blank">📅 11:30 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71037">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">🇺🇦
❌
🇷🇺
پهپادهای اوکراینی به بندر سوچی در روسیه حمله کردند.
@News_Hut</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/news_hut/71037" target="_blank">📅 10:57 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71036">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ef77017317.mp4?token=Zj2WsJDw0Dc0EM8YBZepd-dtGczwR0RwV5gGdDS71Jx2DsvFhrPP_NyIMW8XEhRVw5DSw_m2k_DyKcPAABoT_vrQPYNg0ZYwGmrFIK98_FWlru6CyCJKhbhzJ9eRvVD_SlAGzjAZuuJrxoaoNBYn9VoskeBJzkLmjkoEb2_2hCY-wR24WuGbq3l2tmKwPcB1f6Ws0w4VsgeTcgH4-oZ-6dJ6aUeCgxVhtTWG-QjLjYs2ZDbD4hYoKBRRH6sFoX-c9RGJLSF1_URJ24isvEf3WnktEGrAHBQQW2NBbZY4LUrBc8DPzzYJ798eOMrPCqmrec8EvnR6XKwZ4BYcf6-50w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ef77017317.mp4?token=Zj2WsJDw0Dc0EM8YBZepd-dtGczwR0RwV5gGdDS71Jx2DsvFhrPP_NyIMW8XEhRVw5DSw_m2k_DyKcPAABoT_vrQPYNg0ZYwGmrFIK98_FWlru6CyCJKhbhzJ9eRvVD_SlAGzjAZuuJrxoaoNBYn9VoskeBJzkLmjkoEb2_2hCY-wR24WuGbq3l2tmKwPcB1f6Ws0w4VsgeTcgH4-oZ-6dJ6aUeCgxVhtTWG-QjLjYs2ZDbD4hYoKBRRH6sFoX-c9RGJLSF1_URJ24isvEf3WnktEGrAHBQQW2NBbZY4LUrBc8DPzzYJ798eOMrPCqmrec8EvnR6XKwZ4BYcf6-50w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
ویدیویی وایرال شده از پسری که چالش گرفت که تو خیابونای شهر از مردم درخواست پول کنه(نفری ۱۰۰تومن) و اکثرا قبول کردن و در آخر هم پولی که جمع شد رو رفت به نیازمندا کمک کرد
@News_Hut</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/news_hut/71036" target="_blank">📅 10:34 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71035">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7de7f7edfa.mp4?token=HKVjeosqZx5evTZtc1JPfTxuhHcSFmYZYI7dHeo0CZA2FnU29-0ycqcZVCfKlbUKL7JuS7cQnBG4g9mA6ndcMYpM1shVAmw6dtSOsn9-hj5E0welz-P_tjNuy0jHHcPtn5dPMWKxeZz8GNSetcskjMiFfyS_MDmoOaJYbk0s9VsRCBwEFdNjno83BYUkS68GoYX2guPYf8Pwk5B4hFnAOQwMcKmVq76ixAHtHrd-tHRMao2C5F65wklM3lilaGFXLXSvcUZn6lUvG1XCwlocm-qT5viFG1xwW5p_zR7B_DGaWRatmx0d8ejfNKxC9KmEn3R9pZVujGNrQHyQtwySyg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7de7f7edfa.mp4?token=HKVjeosqZx5evTZtc1JPfTxuhHcSFmYZYI7dHeo0CZA2FnU29-0ycqcZVCfKlbUKL7JuS7cQnBG4g9mA6ndcMYpM1shVAmw6dtSOsn9-hj5E0welz-P_tjNuy0jHHcPtn5dPMWKxeZz8GNSetcskjMiFfyS_MDmoOaJYbk0s9VsRCBwEFdNjno83BYUkS68GoYX2guPYf8Pwk5B4hFnAOQwMcKmVq76ixAHtHrd-tHRMao2C5F65wklM3lilaGFXLXSvcUZn6lUvG1XCwlocm-qT5viFG1xwW5p_zR7B_DGaWRatmx0d8ejfNKxC9KmEn3R9pZVujGNrQHyQtwySyg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
🇮🇷
ویدئو جدید از پرواز هواپیمای HC-130 Combat King II آمریکا در ارتفاع پایین در عمق کشور به دنبال خلبان آمریکایی جنگنده F-15E
@News_Hut</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/news_hut/71035" target="_blank">📅 10:03 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71034">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cad58d044a.mp4?token=HGZ4EQnidUa-IPRaosj18KkrQmR0RwwGDdK8k2o6A7-OMjbRypiXVdVwtZsEB6oA-LLlUgaRyy07oDqstfqkKimdt_FqlJd2lDXXjliNQ7_4szxVk8jDWvnaH2XueuPkTRjLeSPqVZF_QgQGinkGlLjm8rJA6OQ5WgRX24fTmOtwQAdnhuLENmfp3nnJG-Kz7on2RCQ65k765G6gPgJCrt5k88ttguz_KXjT-U_QmK_as6IkZuLXq9iVaQ27Laut9QSoHREkv3QQOgC-MhLXB3sjCcMXLler1OmxjD9za8NmFbf9vhdyz2jQc5z5umCsnouWs3riAs7HKXK5tfyiVw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cad58d044a.mp4?token=HGZ4EQnidUa-IPRaosj18KkrQmR0RwwGDdK8k2o6A7-OMjbRypiXVdVwtZsEB6oA-LLlUgaRyy07oDqstfqkKimdt_FqlJd2lDXXjliNQ7_4szxVk8jDWvnaH2XueuPkTRjLeSPqVZF_QgQGinkGlLjm8rJA6OQ5WgRX24fTmOtwQAdnhuLENmfp3nnJG-Kz7on2RCQ65k765G6gPgJCrt5k88ttguz_KXjT-U_QmK_as6IkZuLXq9iVaQ27Laut9QSoHREkv3QQOgC-MhLXB3sjCcMXLler1OmxjD9za8NmFbf9vhdyz2jQc5z5umCsnouWs3riAs7HKXK5tfyiVw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇷🇺
تو یه فروشگاه تکنولوژی تو روسیه، یه ربات بعد از اینکه مشتری هلش داد، شروع به دعوا با مشتری کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/news_hut/71034" target="_blank">📅 09:31 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71033">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e73b2179fb.mp4?token=MX7Bc0S-LybSu5ey1II6YbM3s0IEewCPfO3qbVxOElRzh0ksPCWDZ6qsBtdTmQd6KsB5OwAyHxCqkKmRN5tmIGaKZIyrIiV5CtMbosReLN5iFa_MzUAfK-T5kY1_fDXSlmPAKJOFatpfaq5g93Ty5I9CZlFnyNf0ivKXHAOPv_XG2fURrcepdEBiIyvWW2nNWIHZatfFnQLYG5tsBxlTLYZf7MIl_HVdJiDz05doRW_0nmaVlzGt5h6Tk9t3_Ap8eDVEQZ-8QU2tczfPLUGBjRPP9nupI8_aPgrXPN1cZUMPTjkRBc6f1SF0-PUGwrXBe3jkofX2MjnzTexNYKfZGw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e73b2179fb.mp4?token=MX7Bc0S-LybSu5ey1II6YbM3s0IEewCPfO3qbVxOElRzh0ksPCWDZ6qsBtdTmQd6KsB5OwAyHxCqkKmRN5tmIGaKZIyrIiV5CtMbosReLN5iFa_MzUAfK-T5kY1_fDXSlmPAKJOFatpfaq5g93Ty5I9CZlFnyNf0ivKXHAOPv_XG2fURrcepdEBiIyvWW2nNWIHZatfFnQLYG5tsBxlTLYZf7MIl_HVdJiDz05doRW_0nmaVlzGt5h6Tk9t3_Ap8eDVEQZ-8QU2tczfPLUGBjRPP9nupI8_aPgrXPN1cZUMPTjkRBc6f1SF0-PUGwrXBe3jkofX2MjnzTexNYKfZGw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
توضیح عباس حیدرزاده مداح درباره‌ی وضعیت مجتبی خامنه‌ای :
تولیت آستان قدس رضوی گفت که شب دفن رهبر؛ مجتبی خامنه ای ساعت ۱۲ شب اومد حرم برای دفن پدرش و تا ۷ صبح اونجا بوده.
وضعیت جسمانی ایشون هم عالیه، هم از لحاظ ظاهری و هم از لحاظ جسمی؛ حتی مسئولین هم پشت سر ایشون نماز خوندن.
همچنین ایشون نیم ساعت کنار قبر پدرش دو زانو نشسته بودن و گریه میکردن.
@News_Hut</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/news_hut/71033" target="_blank">📅 09:03 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71032">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/news_hut/71032" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/news_hut/71032" target="_blank">📅 01:24 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71031">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CARDswdKciFnbrSgRkk9cF7E_vJ0mMr4X11yC8V093ub7t9wERCvysLu_mY4OVIi3t9VeAjyGtox-NeBPJhPiTBBzidba2FZH-rZBYA0ae9IQak7gFOmofeHNxoUL7wpX8k-VeaYkpRFNtruIxysqPVNziyMMsNHZZJD1Dkn36NT0Yyyt2hd56lit9ieBM9Ifa9XuB6q5fNC6_0YfmqlJf8AblP9v6xqHecO0GrbqTvmjivrdhbdHSvCztTVb6SwBiiNiN6ees4thZ0cVmLvCoRX-LRID8aGettxmsWCaUOqjDMa-6ztXLpAvHD9Eslr1e1oIU4NT8ffL2mN55e-TQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🦖
فقط یک بازی از میکس‌ت لوز شده؟
پولت برمی‌گرده!
میکس می‌بندی، هیجان بالا میره، اما یکی از انتخاب‌هات خراب می‌شه؟
با پیشنهاد ویژه
TrexBet
، در صورت رعایت شرایط، می‌تونی
۱۰۰٪ مبلغ شرطت رو پس بگیری
.
همین الان وارد سایت شو و شرایط آسان‌ش رو مطالعه کن!
💰
🦖
🦖
🦖
🦖
🦖
بونوس صدرصدی اولین واریز
🦖
واریز آسان، برداشت سریع
🦖
سرعت بالا، طراحی حرفه ای و تجربه ای متفاوت
https://TrexBet.com
T.me/TrexBet_Ir</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/news_hut/71031" target="_blank">📅 01:23 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71030">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">🔴
⭕️
فوووووری/ همین الان با شروع مجدد جنگ دلار و ارز منفجر شد
😳
‼️
همین حالا چک کنید
👇
https://t.me/+S5Mn2k3LOf0wNjJk
https://t.me/+S5Mn2k3LOf0wNjJk
فوری برید ببینید
☝️
☝️
☝️</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/news_hut/71030" target="_blank">📅 00:04 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71029">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/aa78544f7d.mp4?token=FYrjVXn3R8n1bPzpnHPbTgJFeTwnUOCHBnA6LgXPqF4kMa8Grl3XPU12BnTiBp4knM6oTvvS7A5gPE400jgxyiM7GM9pgWHlUAQC_7-yzGK7ZEIb9FEltCO87LQ9BZMVmxqvcqVz-mK7YHLje_CPp__qeWvt7sIPxh4PHTwaRg678_O-8M8_4kTfYa1sAmlqS_ST04yW-rgsFeGH3x2HqQBl662X4NB8_YEjFh3ofhKbGnUG1dQ27E0yT3QTD7aGlR1VVzflflESJQRrJbN5F0tWl-EgoK7IdEFqAU6x95Bp9aX-vwbD69L0Ap2aHp6DDHZiaSdw-SjI9jlz_wVQiA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aa78544f7d.mp4?token=FYrjVXn3R8n1bPzpnHPbTgJFeTwnUOCHBnA6LgXPqF4kMa8Grl3XPU12BnTiBp4knM6oTvvS7A5gPE400jgxyiM7GM9pgWHlUAQC_7-yzGK7ZEIb9FEltCO87LQ9BZMVmxqvcqVz-mK7YHLje_CPp__qeWvt7sIPxh4PHTwaRg678_O-8M8_4kTfYa1sAmlqS_ST04yW-rgsFeGH3x2HqQBl662X4NB8_YEjFh3ofhKbGnUG1dQ27E0yT3QTD7aGlR1VVzflflESJQRrJbN5F0tWl-EgoK7IdEFqAU6x95Bp9aX-vwbD69L0Ap2aHp6DDHZiaSdw-SjI9jlz_wVQiA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
🇹🇭
ناو آبراهام لینکلن تو پاتایا - تایلند پهلو گرفت و ملوانان و اعضای این ناو برای یه استراحت  کوتاه مدت پیاده شدن
@News_Hut</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/news_hut/71029" target="_blank">📅 23:32 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71028">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/14a1d4faa9.mp4?token=oNgfYj5XD0yCjH6XhdjuMLdSY2InIk3LmZTfr-_M8XGIsj5MOiazGj4ydjhVloK_NypBTgtMdkVhT6P7M5QWnLz-U-fBKRfH65IGdPqddd-BahgvfPlcmS4e6Lilxs6EGJDZPQTbDW297XRA63Nw7Tn7-dwO06yIG2JIvjuNkWgg-T8abe-CIjGIvrG1M9QCMqbfBTP7cZoAlqeoPGYQQgH-3RbsBKok07VdkIGdan4eBoxMjIR3qDjRDlVLIebQVueQDIdVyJVqUzLbnm7R4AsvZTrc5cQoSfhd59Rhem1zQWfo9ZyDf0OGkFl57joUm2x5Sd8vu9zVzkTktzd0bQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/14a1d4faa9.mp4?token=oNgfYj5XD0yCjH6XhdjuMLdSY2InIk3LmZTfr-_M8XGIsj5MOiazGj4ydjhVloK_NypBTgtMdkVhT6P7M5QWnLz-U-fBKRfH65IGdPqddd-BahgvfPlcmS4e6Lilxs6EGJDZPQTbDW297XRA63Nw7Tn7-dwO06yIG2JIvjuNkWgg-T8abe-CIjGIvrG1M9QCMqbfBTP7cZoAlqeoPGYQQgH-3RbsBKok07VdkIGdan4eBoxMjIR3qDjRDlVLIebQVueQDIdVyJVqUzLbnm7R4AsvZTrc5cQoSfhd59Rhem1zQWfo9ZyDf0OGkFl57joUm2x5Sd8vu9zVzkTktzd0bQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
پزشکیان خطاب به پوتین :
قدرت‌های بزرگ صرفاً چون زور و قدرت دارن، حق ندارن بدون توجه به چارچوب‌ها و قوانین بین‌المللی به بقیه کشورها حمله کنن.
حمله‌ای که آمریکا علیه ایران انجام داد، نه مبنای قانونی داشت، نه مبنای علمی و نه حتی توجیه منطقی.
ملت ما با قدرت جلوشون ایستاد و اگه بخوان این مسیر رو ادامه بدن، بازم با قدرت مقابلشون می‌ایسته.
ما تو اون تفاهم‌نامه چیزی بیشتر از حقوق کشورمون نخواستیم و الان هم فقط دنبال همون حقوق هستیم.
ما همچنان به تفاهم‌نامه‌ای که امضا کردیم پایبندیم. اگه آمریکا هم به همون تفاهم‌نامه برگرده، ما هم طبق همون عمل می‌کنیم.
@News_Hut</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/news_hut/71028" target="_blank">📅 23:03 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71027">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/180c2bccea.mp4?token=TTdz66gcCRTIcHadIIQ0kCHVQmO4ZstMXE7rbsWkaq5Aqhzfil7XraOnppSkpW8Fl_vO8mO64PUHlfVkZuwkEK8JPWxrzRmI9VjT3mQOEYdHQ9Kmn_oUndMtePdra8M-rWok9lZdgTqbh-bH4V1pCn18E__W2Z1q8VZQpafHlbkZTZJn9sOl3rVK3eGvbAKyx3-aNbg2GzwxG3hXQm59sGGeqBOVEtOqSkaWln6rKz25E1P3GMMnM-rntFjjWFbMNSbb_CxbdQvcbAVtV_4K8IbnoR_4lhVGUL4dSjHk3vp-zLhct5Yf_g6QOBDmidqnC31rw4x_WU2ZJh5ynaXkog" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/180c2bccea.mp4?token=TTdz66gcCRTIcHadIIQ0kCHVQmO4ZstMXE7rbsWkaq5Aqhzfil7XraOnppSkpW8Fl_vO8mO64PUHlfVkZuwkEK8JPWxrzRmI9VjT3mQOEYdHQ9Kmn_oUndMtePdra8M-rWok9lZdgTqbh-bH4V1pCn18E__W2Z1q8VZQpafHlbkZTZJn9sOl3rVK3eGvbAKyx3-aNbg2GzwxG3hXQm59sGGeqBOVEtOqSkaWln6rKz25E1P3GMMnM-rntFjjWFbMNSbb_CxbdQvcbAVtV_4K8IbnoR_4lhVGUL4dSjHk3vp-zLhct5Yf_g6QOBDmidqnC31rw4x_WU2ZJh5ynaXkog" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
🇺🇸
ترامپ درباره انتخابات:
من تحت تأثیر انتخابات نیستم. خودم نامزد انتخابات نیستم؛ حزب من در انتخابات حضور دارد.
به گمانم حزبم به این واقعیت احترام می‌گذارد که ما اجازه نمی‌دهیم ایران به سلاح هسته‌ای دست یابد.
@News_Hut</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/news_hut/71027" target="_blank">📅 22:27 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71026">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/53f1ce3ca7.mp4?token=R6_KwVx3lZQ_4bVwK_D68u0HU2OYZpMTcdKBgXohYAGLfe9TpGOiE8ZRpU9K6Rad8bQJ5UTNg7yHW7JMEFmGPyE2EmnkuZbnx1VOzkiWOXISJRNSsWXWVSLO1xAXlVZwkSoMhER4S_9FkHoLNCK2KoCafTuWMIMSi8BO6OC9AR4O3-9uw81GZg5x1jP8iWEmhu4FeN3uz0qGyfkmn_HaZ82edcN7fxIkBXlW8EeC7bCxOw6Pl2baSmkWIY3UhcyYJ3XSqEMM9g4LPA892xGH9rPx09dEAXOdxElSO81BjEHZMEM920CSTyfTdMtCt2D7tNWAPvXy2HnRuBtbd6Hiew" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/53f1ce3ca7.mp4?token=R6_KwVx3lZQ_4bVwK_D68u0HU2OYZpMTcdKBgXohYAGLfe9TpGOiE8ZRpU9K6Rad8bQJ5UTNg7yHW7JMEFmGPyE2EmnkuZbnx1VOzkiWOXISJRNSsWXWVSLO1xAXlVZwkSoMhER4S_9FkHoLNCK2KoCafTuWMIMSi8BO6OC9AR4O3-9uw81GZg5x1jP8iWEmhu4FeN3uz0qGyfkmn_HaZ82edcN7fxIkBXlW8EeC7bCxOw6Pl2baSmkWIY3UhcyYJ3XSqEMM9g4LPA892xGH9rPx09dEAXOdxElSO81BjEHZMEM920CSTyfTdMtCt2D7tNWAPvXy2HnRuBtbd6Hiew" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
🇺🇸
ترامپ درباره ایران:
دیشب حمله بسیار سنگینی صورت گرفت و ما آماده‌ایم هر زمان که بخواهیم، حمله دیگری انجام دهیم.
@News_Hut</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/news_hut/71026" target="_blank">📅 22:25 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71025">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a230c24bdf.mp4?token=YXHk5w4pKwWQS7bhhw9U7efe2APLNq1IYj3ybRLvIHxVsqNHEVEWlQvTVFwlhi3h_gwr08FYfnudIvKuw1aLop1lz_V68Xa_03Io0MYl9UYxIYueP8xUFepPanP7aouEo6gmYZ3nPecBclWxNpr-hvNgh6rJ1xKGuSSuQuwbNXsn00v7a6LpkCgsB7oxkrGpF-FTR_cbEl9nQvJX2lO51YkVFmtEt1vMtxUkZzoOgX2X87vUSlorTDttrMr4NDRW1xZfsrl6oLEtCpBqlL8LGlRwXI5yyV4ppCljOGlV4TB0gser2xBfumRTXyNoj8P-ScBueyL-vSr9GnpCj3Y8Ug" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a230c24bdf.mp4?token=YXHk5w4pKwWQS7bhhw9U7efe2APLNq1IYj3ybRLvIHxVsqNHEVEWlQvTVFwlhi3h_gwr08FYfnudIvKuw1aLop1lz_V68Xa_03Io0MYl9UYxIYueP8xUFepPanP7aouEo6gmYZ3nPecBclWxNpr-hvNgh6rJ1xKGuSSuQuwbNXsn00v7a6LpkCgsB7oxkrGpF-FTR_cbEl9nQvJX2lO51YkVFmtEt1vMtxUkZzoOgX2X87vUSlorTDttrMr4NDRW1xZfsrl6oLEtCpBqlL8LGlRwXI5yyV4ppCljOGlV4TB0gser2xBfumRTXyNoj8P-ScBueyL-vSr9GnpCj3Y8Ug" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
🇺🇸
ترامپ درباره ایران:
یک ضربه کوچک بود، اما دیشب ضربه بسیار سختی به آن‌ها زدیم.
ما تمام تجهیزات جدیدی را که سعی داشتند در امتداد تنگه هرمز مستقر کنند، از بین بردیم؛ تجهیزاتی که برخی جنبه تدافعی و برخی جنبه تهاجمی داشتند.
آن‌ها تلاش می‌کردند موقعیت کشتی‌ها را رصد کنند — چون همان‌طور که می‌دانید، قادر به دیدن کشتی‌ها نیستند؛
ما تعداد زیادی از کشتی‌هایشان را نابود کرده‌ایم
آن‌ها نمی‌توانند کشتی‌ها را ببینند چون راداری در اختیار ندارند؛ چرا که ما رادارهایشان را منهدم کرده‌ایم.
@News_Hut</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/news_hut/71025" target="_blank">📅 22:04 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71024">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/991fb05c67.mp4?token=ZAdW5JFtQ650RKHlvON0DuQzFK09jjapJyo22EfUgX0zv71wqZiWxp1t3z3l0UH9igzKzqGvYj2JNe89oieGeKBWurIU-V3il4LbrYenF8g_ukOIyVi61mdqEtRsdFk_4CZf6LY_tN3u-0xdHGQmKNEJ7ZWY2jgIUW1LeT8juH4pvd4K_5U-k-MqQJCnJlrkl8NPCgDYZI_KTNQ62tO4lQWkX_koocQde4GwVW5rViAu8gHEtjgR5YqzwniKmN7x-dNXt1glX-Fk033bAm-VIKsw65oagrd0aHy2BHdMtTHmQsZr6TW4xYHxAQIBqHY6DRPh4oSQSexHREkfCteTUA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/991fb05c67.mp4?token=ZAdW5JFtQ650RKHlvON0DuQzFK09jjapJyo22EfUgX0zv71wqZiWxp1t3z3l0UH9igzKzqGvYj2JNe89oieGeKBWurIU-V3il4LbrYenF8g_ukOIyVi61mdqEtRsdFk_4CZf6LY_tN3u-0xdHGQmKNEJ7ZWY2jgIUW1LeT8juH4pvd4K_5U-k-MqQJCnJlrkl8NPCgDYZI_KTNQ62tO4lQWkX_koocQde4GwVW5rViAu8gHEtjgR5YqzwniKmN7x-dNXt1glX-Fk033bAm-VIKsw65oagrd0aHy2BHdMtTHmQsZr6TW4xYHxAQIBqHY6DRPh4oSQSexHREkfCteTUA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
🇺🇸
پرزیدنت ترامپ:
ما هر کاری که آن‌ها انجام می‌دهند را می‌بینیم.
آن‌ها حتی نمی‌توانند به دستشویی بروند بدون اینکه ما متوجه شویم.
@News_Hut</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/news_hut/71024" target="_blank">📅 21:57 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71023">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/504db2064f.mp4?token=nx1PasgjmrOjqu2ANVxkcYRhtE9pLe_lmx7Ro_y6S6K351p9ke7IU8SzXAJlktwg9-W67AL7VHmkkKdZmWk4tJN_4meppDmHJVxqC6NriLZNXbv_5LaQs0sdF4125a0gu0skyLYywa8MYdmXXpWJPyaqszPWwmFAmthOtvhTpS3JC8g-RVudmvgX89E5SQNcoFzcNq7VazUrqetu1qGguFpStKfVCPFTHTJ4c4DV3PA29LK-M4SmWpp9cpq2KaXX_A0I4sUnQyVxfPCkAnapMmVGjvfhW5tCxGXwaBSDHXYDqfEG-urJ07nf4YYi38WJDPFJkuDDuGCFawgYaSQjJQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/504db2064f.mp4?token=nx1PasgjmrOjqu2ANVxkcYRhtE9pLe_lmx7Ro_y6S6K351p9ke7IU8SzXAJlktwg9-W67AL7VHmkkKdZmWk4tJN_4meppDmHJVxqC6NriLZNXbv_5LaQs0sdF4125a0gu0skyLYywa8MYdmXXpWJPyaqszPWwmFAmthOtvhTpS3JC8g-RVudmvgX89E5SQNcoFzcNq7VazUrqetu1qGguFpStKfVCPFTHTJ4c4DV3PA29LK-M4SmWpp9cpq2KaXX_A0I4sUnQyVxfPCkAnapMmVGjvfhW5tCxGXwaBSDHXYDqfEG-urJ07nf4YYi38WJDPFJkuDDuGCFawgYaSQjJQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
🇺🇸
پرزیدنت ترامپ:
بیشتر مردم نمی‌توانند به این شکل آدم‌های خودشان را بکشند.
بیشتر مردم سعی می‌کنند منطقی رفتار کنند، گفتگو می‌کنند و بعد شاید کار به سرنگونی بکشد.
اما در ایران، آن‌ها مردم را می‌کشند.
وقتی مردم برای اعتراض بیرون می‌آیند، آن‌ها را می‌کشند؛ درست وسط پیشانی‌شان شلیک می‌کنند.
@News_Hut</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/news_hut/71023" target="_blank">📅 21:54 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71022">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c319507bcf.mp4?token=maYjLwpcJhqKaREcxVZjNbr5EhYjCF9Kh42iYGhoB5E5DTdf9lN0rsmIL8EVaM91eDuh_a6i8wYpq7qy8fU7vZ7hGVMAEtxFyQiUxW8svo60-8-4edr5LzFEUAX10XPVmi2aYn9pFXhDgM60Dy5Wfzv1vGZ2N0M-3d4kEg0mt-_EVTdC1n76zHE-a9DevqnyiYTG74VZRXXsSE0Qfny7AkaDCQmzzDMXsRnCQqRKPGgt--0HD8krMYEH6oebXZ1_ZyIlw3K0KRIbKqyiM93Dc0xL9qGFpIKgHP13GTiYNhlkIvCB5YPOjyGPuCLFZhx9xJAxwuaejZqhCkOUvMIYLg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c319507bcf.mp4?token=maYjLwpcJhqKaREcxVZjNbr5EhYjCF9Kh42iYGhoB5E5DTdf9lN0rsmIL8EVaM91eDuh_a6i8wYpq7qy8fU7vZ7hGVMAEtxFyQiUxW8svo60-8-4edr5LzFEUAX10XPVmi2aYn9pFXhDgM60Dy5Wfzv1vGZ2N0M-3d4kEg0mt-_EVTdC1n76zHE-a9DevqnyiYTG74VZRXXsSE0Qfny7AkaDCQmzzDMXsRnCQqRKPGgt--0HD8krMYEH6oebXZ1_ZyIlw3K0KRIbKqyiM93Dc0xL9qGFpIKgHP13GTiYNhlkIvCB5YPOjyGPuCLFZhx9xJAxwuaejZqhCkOUvMIYLg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
🇺🇸
پرزیدنت ترامپ:
تا سه ماه پیش، پنجاه‌ودو هزار نفر از معترضان کشته شده بودند؛ می‌توانید چنین چیزی را تصور کنید؟
و حالا شنیده‌ام که احتمالاً بیست تا بیست‌وپنج هزار نفر دیگر هم به این آمار اضافه شده است؛
یعنی شمار معترضان کشته‌شده به حدود شصت‌وپنج هزار نفر رسیده است.
@News_Hut</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/news_hut/71022" target="_blank">📅 21:52 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71021">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/78e478b4b0.mp4?token=aU8UTpmPMEZyuxQCndvEmL7fAd0XYibIBa6wMZ8tSXci2flxyv2MXlELdUGv79mkrD7eYkCKybsTm16tUteeGN1vaYX4brHlUsMW-7ELvJqXNjb6X7uRf3Ro2FRNwgNc24oiGaoaQfaYP2k0QnX1cOXdrrnbMto2Dimy0ra672wf18YskWL7vY8EMIimaAVesszEXsFELVU3PKYPYA0VznOLM9yWU-t6XR3cZ_eiE_Cb5b9RJCO0_Z70wQbELGeo6lSwcE_IJrmdnxCUhcsi4QZ3nQPY1fA9yExhBvm9sQzassK1pAl2cI9wtOLcnzob1Xz5P2kAWybnIaqOPwIVvg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/78e478b4b0.mp4?token=aU8UTpmPMEZyuxQCndvEmL7fAd0XYibIBa6wMZ8tSXci2flxyv2MXlELdUGv79mkrD7eYkCKybsTm16tUteeGN1vaYX4brHlUsMW-7ELvJqXNjb6X7uRf3Ro2FRNwgNc24oiGaoaQfaYP2k0QnX1cOXdrrnbMto2Dimy0ra672wf18YskWL7vY8EMIimaAVesszEXsFELVU3PKYPYA0VznOLM9yWU-t6XR3cZ_eiE_Cb5b9RJCO0_Z70wQbELGeo6lSwcE_IJrmdnxCUhcsi4QZ3nQPY1fA9yExhBvm9sQzassK1pAl2cI9wtOLcnzob1Xz5P2kAWybnIaqOPwIVvg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
خبرنگار:
شما امروز در «تروث سوشال» (Truth Social) نوشتید: «مردم ایران چه زمانی قرار است قیام کنند و بجنگند؟» خب... اگر... اگر این چیزی است که شما می‌خواهید، آیا سیا (CIA) را برای مسلح کردن ایرانی‌ها اعزام خواهید کرد؟
⏺
🇺🇸
ترامپ:
خب، پیتر، من نمی‌خواهم چنین چیزی به شما بگویم. خیلی دوست دارم این را به شما بگویم، اما... اما گفتنش مناسب نیست.
ولی... منظورم این است که من وضعیت دشوار آن‌ها را درک می‌کنم؛ آن‌ها هدف شلیک گلوله قرار می‌گیرند.
@News_Hut</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/news_hut/71021" target="_blank">📅 21:47 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71020">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">🚨
سازمان عملیات تجارت دریایی بریتانیا (UKMTO):   گزارش تأییدشده‌ای مبنی بر درگیری یک نفتکش در یک حادثه امنیتی دریافت کرده که منجر به دو مورد تلفات انسانی شده است.   @News_Hut</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/news_hut/71020" target="_blank">📅 21:32 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71019">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8edb01b99f.mp4?token=EYKT2kQP2ro_56DCPIihXshjl1KvjoEG5AfW0lrpZheGNeuj1JsWwPHYquh4aDbK8FXUV0Gazigs_8jzz2UkWxsNy3JNxUG_0ouE0Y0OQa7pkaWRim2ZFYWEJp4xi5_y8cxWf_A3lQ92sW1_zr35-8V4BGk12CDASc63AKWdTuX9k_F2Rm3AZiu4wluqlgLKp9vcCglqqoeO6MNy7r3przaLRpQ6pokH5D8Hhv_6FpHpN4mz1qQj53y9EqnixzLppkTVPmioIxRe2s-8QmRtu4DCVDO2afk3mu2mI-a1ZWlaKalPhKgFvtTzg-nTJ7rf5KhESd_rz9ovOBBFGaT79bEgvjxWIr553_UToiRwPaXldp45I9Ihe6OJ4nmlr-_uqL3JzivGQkT3QvVl0t1DrzOx3WafyJDs2yK_lnwo3kMI3EdT5J94wS2XzTCGTUAUFUMSKhEp8gpkmTe2dNu4UyqiaerWTUmoBPxG8demPJV4AZIIUdTyxJu203yooW6NaVNM4d9sf_fII7-E7tzj55Xwksc3HMsGZtEGDdHEBjy54b_7J53kqxKY_qBx734X86vOAGWm1gLOucphc4qmt7muqIQ7uhP1hKAszQbhyahdsCCvBkEGwyUrfYw5HG_XXYV8nbt9KSMEAZLG4NmbSCfZHH7vUMcy18qE4U-WWf8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8edb01b99f.mp4?token=EYKT2kQP2ro_56DCPIihXshjl1KvjoEG5AfW0lrpZheGNeuj1JsWwPHYquh4aDbK8FXUV0Gazigs_8jzz2UkWxsNy3JNxUG_0ouE0Y0OQa7pkaWRim2ZFYWEJp4xi5_y8cxWf_A3lQ92sW1_zr35-8V4BGk12CDASc63AKWdTuX9k_F2Rm3AZiu4wluqlgLKp9vcCglqqoeO6MNy7r3przaLRpQ6pokH5D8Hhv_6FpHpN4mz1qQj53y9EqnixzLppkTVPmioIxRe2s-8QmRtu4DCVDO2afk3mu2mI-a1ZWlaKalPhKgFvtTzg-nTJ7rf5KhESd_rz9ovOBBFGaT79bEgvjxWIr553_UToiRwPaXldp45I9Ihe6OJ4nmlr-_uqL3JzivGQkT3QvVl0t1DrzOx3WafyJDs2yK_lnwo3kMI3EdT5J94wS2XzTCGTUAUFUMSKhEp8gpkmTe2dNu4UyqiaerWTUmoBPxG8demPJV4AZIIUdTyxJu203yooW6NaVNM4d9sf_fII7-E7tzj55Xwksc3HMsGZtEGDdHEBjy54b_7J53kqxKY_qBx734X86vOAGWm1gLOucphc4qmt7muqIQ7uhP1hKAszQbhyahdsCCvBkEGwyUrfYw5HG_XXYV8nbt9KSMEAZLG4NmbSCfZHH7vUMcy18qE4U-WWf8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
🇮🇱
#فوری
؛نتانیاهو درباره ایران:ما رژیم ایران را سرنگون خواهیم کرد.
ما این رژیم را شکست خواهیم داد.
🎙
مجری؛
«شکست» چه معنایی دارد؟ آیا سقوط خواهد کرد؟
🇮🇱
نتانیاهو:
سقوط خواهد کرد. ما آن را سرنگون خواهیم کرد. این رژیم به هر حال در آستانه فروپاشی است.
🎙
مجری:
آیا رئیس موساد، رون گوفمن، برای سرنگونی رژیم ایران تلاش می‌کند؟
🇮🇱
نتانیاهو:
تمام نهادهای ما، تحت هدایت من، برای سرنگونی این رژیم و شکست دادن آن تلاش می‌کنند.
@News_Hut</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/news_hut/71019" target="_blank">📅 20:54 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71018">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7c5723b906.mp4?token=DqUV5NmS8AahmjutXr7YeOq6bCQiUk1xd0UFPMFHDky9muMgE82uPe6YRZNxXZSbKA8dkFOWSmlau-NnUhQh54to6UvohHUfNr5vv7Mqf6YAezVhLLI5N3H2Vhe3riyQ_aKA0DZDeyJQq8boK1uFznr-HES5PNXrZ-xg8wz02eqqQSKUEUPxOMqf-NgT0XKzD8JUf6q9fWWQhUOmCCTftAXnsvao1fDwFLdzPmKTyuEmCyHG4C06vgmax22sXN-CkrbxUnk9vpz18iC6J66eu-5x7nBDd-x3-24z-BauZ0k2AHbS6WaHulCyA-da4tpFchhFj4Kyn56jqXfMj92Kgw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7c5723b906.mp4?token=DqUV5NmS8AahmjutXr7YeOq6bCQiUk1xd0UFPMFHDky9muMgE82uPe6YRZNxXZSbKA8dkFOWSmlau-NnUhQh54to6UvohHUfNr5vv7Mqf6YAezVhLLI5N3H2Vhe3riyQ_aKA0DZDeyJQq8boK1uFznr-HES5PNXrZ-xg8wz02eqqQSKUEUPxOMqf-NgT0XKzD8JUf6q9fWWQhUOmCCTftAXnsvao1fDwFLdzPmKTyuEmCyHG4C06vgmax22sXN-CkrbxUnk9vpz18iC6J66eu-5x7nBDd-x3-24z-BauZ0k2AHbS6WaHulCyA-da4tpFchhFj4Kyn56jqXfMj92Kgw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
ویدیویی از دیدار محسن نامجو با مجتبی خامنه‌ای
😂
@News_Hut</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/news_hut/71018" target="_blank">📅 20:22 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71013">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ib3LBrbvR81GyAqOxhVYQdU8v7_uNUQ0wPZn8xLdD919EGm3BosvZeDh27hki8DfdVgfcJRij6NMArovkkTkxPVN0KyXmtWl7xGH8vJzkAhwWMRYD2gec5S6w5PAcXV9f_zTePYAPOeJN1stu5HqL9sZgg69oj9b1FU2qKfZOxA-fSRtiarU8z9wu1ZOEjT-Qu0EK47OS_Yhc-Crak6u4xm5l3ofyQOgByJ8spxA1dnIUK0cUkKwT95GthdvRfDiUay6n1_Q3Yquj5mAsQ53qtLyF81KF3WMdOHJCDqNwmEinWCCU2hz_JtnFujmE8mKnY0y9f-54cEBvIVILAidaw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/QRuP7rvOLG6IAyprVJpe_PHR5c7hCLlv8W-dJBUiSWapVRY197sq-g8E1ZkaccuTkn4Ur-Yt9DU5ROwTL_Hz29Je37ltfCeVO9aJf_X4jKI2_1k18rT92FsgNiQcMjBgKqsxJ-ITOR7v-uIvSvFhDRm07Blhj2i9tndRwSFzUp-bD-PURCzwbQqdsLQKqVZCPDOY-MMM4pnePVcgULka37U3ms8HzCqcGrMglvLr1-Ox8C1qpNxcaQUqPSGOIFFS9EMWty2L4C2BGZ7URLZ9uouYmsy5hx5V31pf8BRaqovp1fl_yKfilBqvfiOZtxVv-XlzeA4aLwGhHuFxL1KZcw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/21e8023466.mp4?token=URKDQUnhPxKG-XNSdbM9HjlagSnxAgrqNTKqAcL7QTuGfDq06XdMcI9cTDqBvR7-XYeqeaxiQ7eMD4QIdXPyZtV5-VLfV87-33OAJ_xze03ePeF9nXcQSua00bMzAE722KxI85T3LK1vcf7iiTgANTC1SExPsPrfXBgGydfL6lpVrTIH6HclPAobmIzrMCkCesBDcbpH1JVTnz5kOeLgCDeFGk83zAgtZMCR0K0RZR7LEwNSQ5z-kxD1HKoRcRD2VznXN1DYRPEEMYzs1X7hT9Q1cLPYmyv59OrC41tCQV6ORLzq1-Uzb8nbY4IjofcCTT67KAPaTx93DvjPmPhVKQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/21e8023466.mp4?token=URKDQUnhPxKG-XNSdbM9HjlagSnxAgrqNTKqAcL7QTuGfDq06XdMcI9cTDqBvR7-XYeqeaxiQ7eMD4QIdXPyZtV5-VLfV87-33OAJ_xze03ePeF9nXcQSua00bMzAE722KxI85T3LK1vcf7iiTgANTC1SExPsPrfXBgGydfL6lpVrTIH6HclPAobmIzrMCkCesBDcbpH1JVTnz5kOeLgCDeFGk83zAgtZMCR0K0RZR7LEwNSQ5z-kxD1HKoRcRD2VznXN1DYRPEEMYzs1X7hT9Q1cLPYmyv59OrC41tCQV6ORLzq1-Uzb8nbY4IjofcCTT67KAPaTx93DvjPmPhVKQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇱
حملات جنگنده های اسرائیلی به جنوب لبنان
@News_Hut</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/news_hut/71013" target="_blank">📅 20:01 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71012">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/600c9063c3.mp4?token=AlEUeCIdhUaxlcV-lG3jIdfZu2mVTHGRg0njmqBDoRqV_uYV1RVT1B6rNxwSBA4bp4mzwdmpF5wtunkwsi9_DYVyNTQHbjFR1ULAHeXanaU-o3L0jx4SCWEiDzk-OUJwn7WWonj3TIk8h41hrHjzj5m4AieLDfv_VcR0pFC7H_jAvf60VFjvMXltWctZau7XTvli2cLuwVtPn9BDc2o1Tefe5dsvatpi67B29lASWh5sAcw264xbQkJDJHKhwz7CU4LWQBQVKNLIhqoSQyU_pWW07XotDbafPdQ3H2u3xQQJND78xwBY_k_trqGzuq7XWz_Kgdkbm5dO1bBJ-wcnig" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/600c9063c3.mp4?token=AlEUeCIdhUaxlcV-lG3jIdfZu2mVTHGRg0njmqBDoRqV_uYV1RVT1B6rNxwSBA4bp4mzwdmpF5wtunkwsi9_DYVyNTQHbjFR1ULAHeXanaU-o3L0jx4SCWEiDzk-OUJwn7WWonj3TIk8h41hrHjzj5m4AieLDfv_VcR0pFC7H_jAvf60VFjvMXltWctZau7XTvli2cLuwVtPn9BDc2o1Tefe5dsvatpi67B29lASWh5sAcw264xbQkJDJHKhwz7CU4LWQBQVKNLIhqoSQyU_pWW07XotDbafPdQ3H2u3xQQJND78xwBY_k_trqGzuq7XWz_Kgdkbm5dO1bBJ-wcnig" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
مردی در نیویورک آمریکا پس از برخورد مستقیم صاعقه به پایش جان سالم به در برد
@News_Hut</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/news_hut/71012" target="_blank">📅 19:30 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71011">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AC21_nq4_HpIpsf6diN-_1U9ViQvO_NXN3826DFpWf-F-CaJ2XFrCyi0siGcJe6J4ixPM69DzWtO9cbI3ZEkADdL-D_0ggBGeYJMOA5t_5wyAMnDHQfQkFYZmplQ2s99WQc6v8ZS4RHY7-KiIC-VSsb5P7rvvGTaz_b4vvp33paPGwYsj9zvW50pBFxrR2EV9ngzDmfXUJR5jHxOD5WLjFAid2gOpw9VcX5LoTepc4TT17-HMgncMEZ8OT4RMmQWkjlKwXshhQrA8QOFww5ABpnWghJ4s4_uEl4lMqqq9KfBMrAlvAOebuop-8tE8Ug4WKXqCrhDgrj_sfzp0teN4Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
ترامپ در تروث سوشال:
حالا که تنگه هرمز تحت کنترل ایالات متحده است، آیا باید نام آن را به «تنگه ترامپ» تغییر دهیم؟ این تنگه هم درست مثل خودِ آمریکا، «داغ‌تر» از هر زمان دیگری خواهد شد.
@News_Hut</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/news_hut/71011" target="_blank">📅 18:58 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71010">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">اسپویل:
سپاه دوباره موشک می‌زنه و ترامپ هیچ گوهی نمی‌خوره
#hjAly‌</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/news_hut/71010" target="_blank">📅 18:55 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71009">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/27f635b0ff.mp4?token=hEW3ohw2wBLJOsMpDEbpeMh6oBXpVeJBv07Oq2tV7f0Y6PpliQsiUtr7rfv6jfky08dNzhpyJrHhxAgdF8oOYj7qIIhmeNvgR66aATKjE_-kbpIFYrldDgDyaYWT_VcXoucU6KNjL2RRguVHwMA6yf1ivn8RRST-H4dbapZ9b069UVjAyeFErPMBOAFpeb4pZRFz1P9Chyslc4lY7crq8NT9A2KBoK2fuHAEB0SijW0CCClRL0wze82sl3K97nKCm6mUFIrWKiRsjzbjRPNZpdNBb6oE_4b27n6mMb7qedV3nKAljVmm9J1l9_Gh64vnptQgOGMuzIB2-0YLDQkSnw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/27f635b0ff.mp4?token=hEW3ohw2wBLJOsMpDEbpeMh6oBXpVeJBv07Oq2tV7f0Y6PpliQsiUtr7rfv6jfky08dNzhpyJrHhxAgdF8oOYj7qIIhmeNvgR66aATKjE_-kbpIFYrldDgDyaYWT_VcXoucU6KNjL2RRguVHwMA6yf1ivn8RRST-H4dbapZ9b069UVjAyeFErPMBOAFpeb4pZRFz1P9Chyslc4lY7crq8NT9A2KBoK2fuHAEB0SijW0CCClRL0wze82sl3K97nKCm6mUFIrWKiRsjzbjRPNZpdNBb6oE_4b27n6mMb7qedV3nKAljVmm9J1l9_Gh64vnptQgOGMuzIB2-0YLDQkSnw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇺🇸
ترامپ درباره ایران:
ما اکنون کنترل تنگه هرمز را در دست داریم. ما آن را کنترل می‌کنیم.
دیشب ۲۸ قایق و کشتی را از کار انداختیم. ما کنترل آن را در اختیار داریم، آن‌ها هیچ‌چیز به دست نمی‌آورند و ما آن کشتی‌ها را نابود کردیم.
@News_Hut</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/news_hut/71009" target="_blank">📅 18:51 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71008">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/116dfeb2e5.mp4?token=ao8RwlTt2Jua-qfCMdXN7vqi9gU3-ENFtwpxM0mfql9BmEMOMwra7PnXxnmA4UXHXNUUe3Aj34uw0ATQOS_mdQyoquL0m2OHkERmbgUsb1pWCl8CSOgKUgPqcfT5BapJGPNNwBtRTlWsoLn-RDbbYtlT_RvmRIQRIdfc4glP5ctrgkJZ_dv6amyYp6oyDpGNdhw0juGDi1lvOtYJCLyqLUoL5Ok0JIkxvfJbiJIzp9ufNTgPx7b2zZptKynsMWt54oC0W3W_hEIbtmOi1KwWnEfxIB5G5gFS-ag1lnHCFDtvSQ8uGjGAGrVufn5iZP93aEEO-VAdgdh9pvru0yTvsg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/116dfeb2e5.mp4?token=ao8RwlTt2Jua-qfCMdXN7vqi9gU3-ENFtwpxM0mfql9BmEMOMwra7PnXxnmA4UXHXNUUe3Aj34uw0ATQOS_mdQyoquL0m2OHkERmbgUsb1pWCl8CSOgKUgPqcfT5BapJGPNNwBtRTlWsoLn-RDbbYtlT_RvmRIQRIdfc4glP5ctrgkJZ_dv6amyYp6oyDpGNdhw0juGDi1lvOtYJCLyqLUoL5Ok0JIkxvfJbiJIzp9ufNTgPx7b2zZptKynsMWt54oC0W3W_hEIbtmOi1KwWnEfxIB5G5gFS-ag1lnHCFDtvSQ8uGjGAGrVufn5iZP93aEEO-VAdgdh9pvru0yTvsg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
🇺🇸
🇧🇭
لحظه اصابت پهپاد شاهد-۱۳۶  به مقر ناوگان پنجم نیروی دریایی آمریکا در منامه، بحرین، صبح امروز
@News_Hut</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/news_hut/71008" target="_blank">📅 18:40 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71007">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VnOCGHokFMkvFtxPSIHqUujDbU4tUSQD-InaGNUpcu9szo07jfh-x0YD1CpJYMypadgm4fBaMJgB6BDEyM1LWhpVFcrFy-lzHvKFIEpS4f9e_7E3g2iaCiBbEMjgrU4JdbyBlwOQxBLJa6XF9Dio0fX12po7VCHhjznvpXp2MfGT1NdqhVCxnKOi9Cgu9v5Is0CYFMHqeDCTpD3onRpsazcPmMq8B1Grn-30XAiMhnJgdOQxelfpS7Z0ybSITSEd3IdaX38EJP22GIWfCGn3BnPpor0WiFFYYRZnrz3c4CS6damVIqejiUIochW7IgYaBuhRfB45KN-bXdN31U5wmA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇺🇸
مارکو روبیو، وزیر امور خارجه:
ایالات متحده به هدف قرار دادن ایران به دلیل حملات به کشتی‌ها ادامه خواهد داد.
@News_Hut</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/news_hut/71007" target="_blank">📅 18:32 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71006">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/news_hut/71006" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/news_hut/71006" target="_blank">📅 18:32 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71005">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Dc46TLpeuFwIMO8BAd2pcUhq-4PbQrzSSSAFAOd49IFkOVI2yuQ7SwyxEw9lYiLQNxHYecUZfXBHPqgMK5KsdJpqU3JpKZpOpFvnVHJ7AIvA0aDgti0aUbIGBcMRDkqQSqs91mvj4rIayURuGfGfvxvbEsjqgqiKXWKQCw9gMOcD8iVUpuonm2muGIt2609Zp9v9h9gzg11z90qC25ADYUxWEUD5EMafsY8fJRm7YWEC_XCVKnP2L1KHwDr3Tlz9ALllEfB27HGUn5TzbzMhlCROZzaeERUR9YeDDsza1ACXg9eqzhrXChjYGTUebb5EnFudtl0ZcigCTfqyWmQ8lw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
استقلال
🆚
پرسپولیس
⚽️
پیش‌بینی دربی رو در
TrexBet
از دست نده!
📉
نگاهی به 5 دربی اخیر:
2 برد پرسپولیس | 0 برد استقلال | 3 مساوی
4 گل پرسپولیس | 2 گل استقلال
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
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/news_hut/71005" target="_blank">📅 18:32 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71004">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/26734edca1.mp4?token=Rt4LBTY_FTiD1VA7d3Z7P6FFIxzge67Jk11gsb-hNsUG-ekyK-2XA5xazmwMyN1O_kflVF9z5g1mbVTzfnGPTYa4u8E5rgeCazvkW-FWSMTXQf3eNzxItQiL-RExlerDYL-tL8wutgQ5pxEPt1emL3DNuUtfgSuKGIrF4_lPBqg-myypisMtO8iodRGb22KJG841GOUBp0yZB6-HQUh-oL3nl8R0q_Bq5nr_y2Bah_am0V9Anwfuh6J0iOd2rZmPlwyqnsSSCTK2DfqjNspYinwJtaK2AsCAQOAv5aiPTfMxqZnA3EI4mvpdaKf--kizpJDpPbz12tjFvEltgMHepQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/26734edca1.mp4?token=Rt4LBTY_FTiD1VA7d3Z7P6FFIxzge67Jk11gsb-hNsUG-ekyK-2XA5xazmwMyN1O_kflVF9z5g1mbVTzfnGPTYa4u8E5rgeCazvkW-FWSMTXQf3eNzxItQiL-RExlerDYL-tL8wutgQ5pxEPt1emL3DNuUtfgSuKGIrF4_lPBqg-myypisMtO8iodRGb22KJG841GOUBp0yZB6-HQUh-oL3nl8R0q_Bq5nr_y2Bah_am0V9Anwfuh6J0iOd2rZmPlwyqnsSSCTK2DfqjNspYinwJtaK2AsCAQOAv5aiPTfMxqZnA3EI4mvpdaKf--kizpJDpPbz12tjFvEltgMHepQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
📰
اینترنشنال:
⁉️
🇺🇸
🇮🇱
از شهروندان پرسیدیم پاسخ شما به پرسش ترامپ درباره زمان قیام مردم ایران چیست؟
یک شهروند با ارسال پیام صوتی به ایران‌اینترنشنال خطاب به دونالد ترامپ می‌گوید: «چه تضمینی وجود دارد که ما بیرون بیاییم و تو بعدش مذاکره نکنی؟ ترامپ، کار را به نتانیاهو بسپار که او بلد است.»
@News_Hut</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/news_hut/71004" target="_blank">📅 18:04 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71003">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c4349c8ad3.mp4?token=g8CPHcuFG6v4gtOFOtuUxQcXOAtoFgMErnGCTFZaz-um0lz22XuRfizpRxDy6jy5rKlrxUaGnK9Ye9mYfj1lCwUDPRh6bnjcpeD4VwK2JpmLasqVNTSP5tYJ2SRp0Qc_o2S6VLtCX38W1HCpJXawiaSirY7UBC1IuVouEokarcEfuVC9a9glXt33h_mWUIUHd7JovBRTmFhrGcTF3Mc_0nqDRl79t04pyiyC5_0N-jvsPsa3vItunN-IaVSXz90nSTgCu8ACV370Tut0NAFihg_SWVNga1Ir02fFJeLXNpkj5QdNxfStocIwa88yMrmqPNrOs4iLElsv68u5hTn4sw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c4349c8ad3.mp4?token=g8CPHcuFG6v4gtOFOtuUxQcXOAtoFgMErnGCTFZaz-um0lz22XuRfizpRxDy6jy5rKlrxUaGnK9Ye9mYfj1lCwUDPRh6bnjcpeD4VwK2JpmLasqVNTSP5tYJ2SRp0Qc_o2S6VLtCX38W1HCpJXawiaSirY7UBC1IuVouEokarcEfuVC9a9glXt33h_mWUIUHd7JovBRTmFhrGcTF3Mc_0nqDRl79t04pyiyC5_0N-jvsPsa3vItunN-IaVSXz90nSTgCu8ACV370Tut0NAFihg_SWVNga1Ir02fFJeLXNpkj5QdNxfStocIwa88yMrmqPNrOs4iLElsv68u5hTn4sw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🎙
فردوسی پور:تاج و دوستاش نزدیک ۲۰ میلیارد از پول بیت المال رو گذاشتن تو جیبشون.
چند وقت پیش تیم ملی جوانان ایران واسه برگزاری یه اردو قبل بازی‌های آسیایی، به ترکیه سفر می‌کنه.
تو آنکارا، هزینه هتل‌شون طبق سند خودِ فدراسیون، 116,160 یورو شده.
بعد برنامه ۳۶۰ زنگ زده به همون هتل گفتن که قیمت‌ها اصلا این نیست و انگار مسئولین فدراسیون قیمت‌ها رو الکی بالا بردن! و هزینه ای که کردن چیزی حدود ۳۶ هزار یورو بوده.
خلاصه تاج شیرین نزدیک ۷۰ هزار یورو کرده تو جیب خودش و دوستاش
@News_Hut</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/news_hut/71003" target="_blank">📅 17:34 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71002">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b1896637f6.mp4?token=d9dRnJMrtQWhp8GUj3BapxLEK3MFBkQjuo1iKaeS-PxUMB6bw5HsxbbNORyJVGIJ7kyffQp6DCh6z5GF0BEHOhzLF4Hxi1GJX59C9lqK_7AG-2x0atOPdFB6Z-39HgwJHSEVo482WLr1IhltE4rVfYhZo3hyUnVKlZnEtZMBy4ai7AElGr257f2dn_2N4WPpRMl-BtpBcpvQZoMp-P9qHbHL_lA27KiTRn-esFyNecaLbQ_l2oGjobZKiBpEhLS5qhTJjo7GRVuHktn3jp12YJoSf14AGrufjpEcdPjhnMouOKBCaYhlLuELWMWrzNtkrOrMaIe68b5aoLFMy7fdfQD97ptllZbxbNKwojg7VsMqv_ZKAn9Gg1FdUda92ljtWpEGYlqp_9WwPWY18tL_q4CVWT7Hm01NI1736CZ7qD6UMIbtr2mxMaOrhh0cDqFjhoA2ZMjvTmCGLnzi7lqY7GKGA0dzh3daazaX7a4MHEnBaxAezQojHZBIaOLVX6umNj8RqcKFTwxdTA2dcwJbTZtGgbcshGt_R6htMoxohhMcharj3KA3lcsa5pMi8hEaPvquOFMJFJPuuq7w7peBS2HYf2O37-LC-BjjQQPNOtWUYhsUmkGWKTivjhMLpYRDhgr7-yBKoYuvnqramtk7wPTOxN9XKSmymzp_RbRDvx0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b1896637f6.mp4?token=d9dRnJMrtQWhp8GUj3BapxLEK3MFBkQjuo1iKaeS-PxUMB6bw5HsxbbNORyJVGIJ7kyffQp6DCh6z5GF0BEHOhzLF4Hxi1GJX59C9lqK_7AG-2x0atOPdFB6Z-39HgwJHSEVo482WLr1IhltE4rVfYhZo3hyUnVKlZnEtZMBy4ai7AElGr257f2dn_2N4WPpRMl-BtpBcpvQZoMp-P9qHbHL_lA27KiTRn-esFyNecaLbQ_l2oGjobZKiBpEhLS5qhTJjo7GRVuHktn3jp12YJoSf14AGrufjpEcdPjhnMouOKBCaYhlLuELWMWrzNtkrOrMaIe68b5aoLFMy7fdfQD97ptllZbxbNKwojg7VsMqv_ZKAn9Gg1FdUda92ljtWpEGYlqp_9WwPWY18tL_q4CVWT7Hm01NI1736CZ7qD6UMIbtr2mxMaOrhh0cDqFjhoA2ZMjvTmCGLnzi7lqY7GKGA0dzh3daazaX7a4MHEnBaxAezQojHZBIaOLVX6umNj8RqcKFTwxdTA2dcwJbTZtGgbcshGt_R6htMoxohhMcharj3KA3lcsa5pMi8hEaPvquOFMJFJPuuq7w7peBS2HYf2O37-LC-BjjQQPNOtWUYhsUmkGWKTivjhMLpYRDhgr7-yBKoYuvnqramtk7wPTOxN9XKSmymzp_RbRDvx0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
طراح ارشد موتور (بمب‌افکنB1-Lancer) متولد سیرجانه!
@News_Hut</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/news_hut/71002" target="_blank">📅 17:03 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71001">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/618f407212.mp4?token=dUaebrg_U3mgKRO8HLNw9bmxLlyRYcIkhDT9xjSItW7xCV30Bwlb9RQN59UMohcQ5j_hBgQ9UOLoUpyLbJCLRdu3RVjplCad2zIDNN-e8sz533Zys7rK05OFG50LWOgmJdsj0rz3RXhW8_Q1ryPg7j39psZtAu0UBR63slOSjdIOWckyl3JcO6DHKsquhYF2uf00WzqGxx7YOElTGDAZVbmPcF-t_ln3ChRd591mhskyktM_GyCtqzQ_0AMoMEa7V8tRF8WR9q95DcIf0Z0X8jbAluXpiNn4hatsHUjmtGUpSiesohLasm3GnQ1UhGu4vE34Py8Z2KH7xS1cRci_Nw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/618f407212.mp4?token=dUaebrg_U3mgKRO8HLNw9bmxLlyRYcIkhDT9xjSItW7xCV30Bwlb9RQN59UMohcQ5j_hBgQ9UOLoUpyLbJCLRdu3RVjplCad2zIDNN-e8sz533Zys7rK05OFG50LWOgmJdsj0rz3RXhW8_Q1ryPg7j39psZtAu0UBR63slOSjdIOWckyl3JcO6DHKsquhYF2uf00WzqGxx7YOElTGDAZVbmPcF-t_ln3ChRd591mhskyktM_GyCtqzQ_0AMoMEa7V8tRF8WR9q95DcIf0Z0X8jbAluXpiNn4hatsHUjmtGUpSiesohLasm3GnQ1UhGu4vE34Py8Z2KH7xS1cRci_Nw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
بررسی قیمت چند داروی پرمصرف از شهریور ۱۴۰۴ تا شهریور ۱۴۰۵:
@News_Hut</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/news_hut/71001" target="_blank">📅 16:31 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71000">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/df28769cb3.mp4?token=Myv5-sp8ecN4NILAK53N5JLiWSXyT8naRcX1YPfnC1vqAej6Mr1EcUGXqLF2eWkTKaSu2movRqqldeSk3LtRdc7CKiiekCmV7muljJk3ztajENjjbv_Qf-o0_I3BpAQOYM8LaUbCnS85_4bYsVdodqHEuivV9hyGSJu2OKpkdQEx4iJLdRaEqfdMaA2apS5TJTWADO3p3BuZy8xZ8Syv-ImHdS5NG5r2wE6B3C-PuD3WDGbnV8nOERczsMxv5qC_G3G46mT2XnnZANjAJHdno-_eIIIY5FBK29h_WlJ20HJjtyUSenzZu168azvZ0uokVVIc4ZFX3xJLuBEG4TAZfw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/df28769cb3.mp4?token=Myv5-sp8ecN4NILAK53N5JLiWSXyT8naRcX1YPfnC1vqAej6Mr1EcUGXqLF2eWkTKaSu2movRqqldeSk3LtRdc7CKiiekCmV7muljJk3ztajENjjbv_Qf-o0_I3BpAQOYM8LaUbCnS85_4bYsVdodqHEuivV9hyGSJu2OKpkdQEx4iJLdRaEqfdMaA2apS5TJTWADO3p3BuZy8xZ8Syv-ImHdS5NG5r2wE6B3C-PuD3WDGbnV8nOERczsMxv5qC_G3G46mT2XnnZANjAJHdno-_eIIIY5FBK29h_WlJ20HJjtyUSenzZu168azvZ0uokVVIc4ZFX3xJLuBEG4TAZfw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">چرت زدن وزیر ورزش و معاون وزیر خارجه و تمیز کردن دندان توسط وزیر خارجه هنگام سخنرانی پزشکیان
😃
@News_Hut</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/news_hut/71000" target="_blank">📅 15:59 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70999">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JN9yxE_JzrmbITUs4nCSxlhxdjQIQxOviAKPhKpM2zKQeyby8DCFXJD8bQSUtZu2Cb-XwfbdHO1yXOSi9L2jlMJhTIe5t5sUkpVXmZkX5wHRodXQ5qB7Thn_FkQBR7ORXnNXwtLQ4QrZ2N5H5idLUyi4aF48N8Lkg8KNVhUNa1JdIeKxFPwr3TJT18dIUJjCwZKSMkNX3oVZPCrXbVdpII6J4fRKXak49i4yxagxeHzrOwgswK5gJH9hZAt0B8RAW9Y7TNA5ihHFekcKivJv1XJSSQ8jijaimFbuD6NahRzBrWRbJOrXu49dLefBknXXug5gtXdtTMfT-j8qxHqWNg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
سازمان عملیات تجارت دریایی بریتانیا (UKMTO):
گزارش تأییدشده‌ای مبنی بر درگیری یک نفتکش در یک حادثه امنیتی دریافت کرده که منجر به دو مورد تلفات انسانی شده است.
@News_Hut</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/news_hut/70999" target="_blank">📅 15:25 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70998">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DM-kXnwDlYYI_DcQPbzJuMq18eo5gFZleO2syICQWpmIEVHpMdeStO5eUDYzZW1szQEC95xB1Rax875UVilOeDT5Pe3w_8wvl9VZSYQrXmTr9fLWeImGn3FEnBKDZlqdWa9b-YJPLnj6pvrN3rczsGpuihLIwi3CiPr155vE3npHRCxV4sjowO6TDmpQmAzL3W7c6-NDc-SB8667J9wwKGc-jG2Wyq5p_-OntrGG5wVJsfcFkp1zMWSz53ZvVb2-fVykOC2L5zaQ18J8B60RonIXzSRnUnrt-hgPxrQ4kzYDxXESwCPeX5d3pg2vpbenPKwSbJapxOHRlcFAW3SLSg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
🇮🇷
فیلد مارشال محسن رضایی:
با این دست‌وپازدن‌ها، نه تنها در بیرون آمدن از آن ورطه هولناکی که برای خود رقم زده‌اید ناکام خواهید ماند، بلکه به‌زودی خواهید دید که راهبرد جدید ایران در میدان نبرد، دیپلماسی و مقابله با محاصره اقتصادی، بنیان‌های شما را درهم خواهد کوبید.
@News_Hut</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/news_hut/70998" target="_blank">📅 14:57 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70997">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/13235e9918.mp4?token=FngCKgc4rStWn8VtJKtlT1-_LKEF_FO3pNUPNmpVICw3H2a6UI3m_J-4Cajv1JhSJc9qjymH_7m8F57qEf7qvYX1fiKGusp20SMwQ1LMQkQs4i5z0LZ8qVHEtEPYI_2jkqU_Ga7WI8mskg-J5fg231Pmc0euQG0sWlztS8NU3w2gU56f62zK5VtvykgN9XmxwJ7qSD6qyXqXStxjbP2s5hjpUpORZcF_rTd-GvuYN-13xPtrxYgvwyRjTVhJJCtVnGV6eICdYP25Zc35AHo32i-XuQKNUEy_6_PtCTaiB43VZhAhBImArj8Vng0rESWqbgkoBS6xoRO5bWNx_3OOOw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/13235e9918.mp4?token=FngCKgc4rStWn8VtJKtlT1-_LKEF_FO3pNUPNmpVICw3H2a6UI3m_J-4Cajv1JhSJc9qjymH_7m8F57qEf7qvYX1fiKGusp20SMwQ1LMQkQs4i5z0LZ8qVHEtEPYI_2jkqU_Ga7WI8mskg-J5fg231Pmc0euQG0sWlztS8NU3w2gU56f62zK5VtvykgN9XmxwJ7qSD6qyXqXStxjbP2s5hjpUpORZcF_rTd-GvuYN-13xPtrxYgvwyRjTVhJJCtVnGV6eICdYP25Zc35AHo32i-XuQKNUEy_6_PtCTaiB43VZhAhBImArj8Vng0rESWqbgkoBS6xoRO5bWNx_3OOOw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇷🇺
پوتین خطاب به پزشکیان:
تو این شرایط سخت، داریم سعی می‌کنیم هر کمکی که لازم دارید، بهتون برسونیم
.
قبلاً هم دربارش با هم صحبت کردیم و داریم کالاها و اقلام موردنیازتون رو تأمین می‌کنیم.
با وجود شرایط نظامی و سیاسی فعلی، همکاری‌های تجاری و اقتصادی‌مون رو با همون روند و قدرت سال گذشته ادامه می‌دیم.
همون‌طور که بارها گفتم، ما تو روسیه کنار مردم ایران هستیم و باهاشون اعلام همبستگی می‌کنیم. شجاعت و مقاومت شما واسه دفاع از منافع ملی‌تون واقعاً قابل تحسینه.
لطفاً سلام من و حمایت صمیمانه‌ام رو هم به رهبر جمهوری اسلامی، مجتبی خامنه‌ای برسونید.
@News_Hut</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/news_hut/70997" target="_blank">📅 14:30 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70996">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">1
💵
= 200.000
💸
🔼
یک دلار آمریکا=دویست هزارتومان   @News_Hut</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/news_hut/70996" target="_blank">📅 14:02 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70994">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d2a6a11bf6.mp4?token=q007YrA0tV7C7cqaghZjWlJoe4se-fDBkWVCTVNT8IFOqc6234p1vjj3mmquHPiis8J-ayJJfVL2O-mqTyFZ8iw3prPcyLYrqhAbwQdqivjXvnf17HzRhCWpXrr2lQYkPDbrshJ0a6wXc65U-FZpFxFE1PIOqfXJ5zTo5wiVs9Q0mUuv_FQJcT5Xb5Q5w6K5GniCcEXwf-wD-T4Wn4lxQtzrVBTyypnfEv_SHi0-miFxx3ZI_eQ0_TTi9Rog88Kt4GbqCtR3MQEK0CsYCY5LWlVla0_7ISLc5FSYHb90YHAYp0qqXqdBBly2fcweTsO04KtCsWHzecqc0q_ph4ky9g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d2a6a11bf6.mp4?token=q007YrA0tV7C7cqaghZjWlJoe4se-fDBkWVCTVNT8IFOqc6234p1vjj3mmquHPiis8J-ayJJfVL2O-mqTyFZ8iw3prPcyLYrqhAbwQdqivjXvnf17HzRhCWpXrr2lQYkPDbrshJ0a6wXc65U-FZpFxFE1PIOqfXJ5zTo5wiVs9Q0mUuv_FQJcT5Xb5Q5w6K5GniCcEXwf-wD-T4Wn4lxQtzrVBTyypnfEv_SHi0-miFxx3ZI_eQ0_TTi9Rog88Kt4GbqCtR3MQEK0CsYCY5LWlVla0_7ISLc5FSYHb90YHAYp0qqXqdBBly2fcweTsO04KtCsWHzecqc0q_ph4ky9g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
〰️
ناو «یو‌اس‌اس آبراهام لینکلن» در تاریخ ۲ سپتامبر و پس از ۲۸۶ روز حضور بی‌وقفه در دریا — که رکوردی مدرن برای نیروی دریایی ایالات متحده محسوب می‌شود — وارد بندر «لائم چابانگ» تایلند شد.
@News_Hut</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/news_hut/70994" target="_blank">📅 13:46 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70993">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">🚨
🇮🇱
یسرائیل کاتز وزیر دفاع اسرائیل درباره ایران:
هم‌زمان با افزایش فشارها بر آن‌ها، تشدید تنش‌ها و تنگ‌تر شدن حلقه محاصره — آن فشار اقتصادی خفقان‌آوری که رژیم افراطی بر مردم خود تحمیل کرده است — احتمال دارد که آن‌ها واقعاً دست به حمله بزنند.
چرا؟ زیرا ممکن است برای رهایی از دوراهیِ میان «خفقان» و «جنگ»، گزینه دوم را انتخاب کنند. ما از نظر دفاعی برای چنین وضعیتی آمادگی داریم.
اکنون در ایام تعطیلات هستیم و آن‌ها معمولاً در تعطیلات یهودیان دست به حمله می‌زنند؛ هرچه باشد، آن‌ها از یهودیان بیزارند.
اما ما — هم در حوزه دفاعی و هم تهاجمی — و با هماهنگی ایالات متحده در این جبهه آماده‌ایم. بله، در همین جبهه.
با این وجود، سناریوهایی وجود دارد — مانند حمله به اسرائیل — که ما به هیچ وجه آن‌ را تحمل نخواهیم کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/news_hut/70993" target="_blank">📅 13:16 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70992">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/0dd8120289.mp4?token=BxmS9TJLDt07lIW6OSWs_et_6gDtGeYbUjteGQxwbF6Xh91oa28hUEmrhIwCD5lEpJ-VutFK0WNzxKg0WWmgkeXGT121ZAuR6_siCVjy8rKleZIEtDjbIHs0IX05zoj9xYPLrdepuyOjziTycX6Iid1yBFMGRNeZ9RX3hSZSDrubqoLb_djFvDqfKkxwc19g5mIxO7BXCvyhSJLF_hvvLjbCacRp_800IV3dgm1fZ8SnChGiewqTyx5RdZHaQAiCkOeoMaOD6Gvn-_CW3VjrxQ4GjJSSxj_YZgH4IcF5e-ySOCB44MVZe4e554qKytgNDrL7Qe4Sn-W3mxpF054xXw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/0dd8120289.mp4?token=BxmS9TJLDt07lIW6OSWs_et_6gDtGeYbUjteGQxwbF6Xh91oa28hUEmrhIwCD5lEpJ-VutFK0WNzxKg0WWmgkeXGT121ZAuR6_siCVjy8rKleZIEtDjbIHs0IX05zoj9xYPLrdepuyOjziTycX6Iid1yBFMGRNeZ9RX3hSZSDrubqoLb_djFvDqfKkxwc19g5mIxO7BXCvyhSJLF_hvvLjbCacRp_800IV3dgm1fZ8SnChGiewqTyx5RdZHaQAiCkOeoMaOD6Gvn-_CW3VjrxQ4GjJSSxj_YZgH4IcF5e-ySOCB44MVZe4e554qKytgNDrL7Qe4Sn-W3mxpF054xXw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
این ویدیو از فروش طلا، به دلایل کاملا نامعلومی بیش از 5 میلیون بازدید داشته!
@News_Hut</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/news_hut/70992" target="_blank">📅 13:15 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70991">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/news_hut/70991" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/news_hut/70991" target="_blank">📅 13:14 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70990">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cueqwX5btFlz5WVbHlQiA2wUgiPKvOQZQqhe0lDdcB3OpmIFx_ILx7g1e3CbNOShZjU3h-jGrfr4ABwkPge9bO4zTAoeaAauCw6t4FNjvIJ8hKLvnh7AFBr78CYiLfkJu65CgkowYQGGF4S3Vqo7np6fLUiikPkCQr0MT7F8L3YuPCTyeTvV3MaLyP7meE1RDe48YtRDRGQSZQaY0ATMbg-P19m5UZVSafJS49WywggY204XK4GCP4NI6yKZecmZAfoPuZZouJYWTTkeaoCIhvU5RNoBeE3W4wUdGIn763pnexL0bSVM3URgyYq_ohcIEqZiVDcqECrd-qepcqMIyw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🦖
با اولین واریز، بیشتر دریافت کن!  فقط در سایت جهانی
TrexBet
🦖
بسته خوش‌آمدگویی ویژه
TrexBet
تا ۱۰۰٪ بونوس واریز
🦖
تا ۱۵۰ چرخش رایگان در ۴ واریز اول
🥇
واریز اول:
۱۰۰٪ بونوس + ۳۰ چرخش رایگان
🥈
واریز دوم:
۵۰٪ بونوس + ۳۵ چرخش رایگان
🥉
واریز سوم:
۲۵٪ بونوس + ۴۰ چرخش رایگان
🏅
واریز چهارم:
۲۵٪ بونوس + ۴۵ چرخش رایگان
🦖
🦖
🦖
🦖
🦖
🦖
TREXBET — PLAY. PREDICT. WIN.
https://TrexBet.com
T.me/TrexBet_Ir</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/news_hut/70990" target="_blank">📅 13:14 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70989">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1829295007.mp4?token=gg6u7_1tflk0mr3IsdH6kdBjMym1GgVwO3ua95eAvVbhQrGr7OQU49tBWXbv96fa6Vmwsozc5nuHGL_Wlrs9Lyv5E8ORetrW9Ss-Ltz4V4MECHxRgltEWyKqM2qVmUEAWgZ1n0P1IridZ4Z6xxDTS9BY_XLWBQDS3bntTgK3yIIAyqrog5iH30FdErJqduKOT_mTlBTh1ugb0PObp923S6Bg9AblqxOje8Wtsz1lgM1oJqaqVVTbeh-NjeePFb6fh8yN6wHzABa2A0DhEu1Xs9M1hGiukmtjwuupFPUpjS0WMJBF7qCjniJIcdnKMTrDeEseaxj6ukqJyh6pj1Jhgg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1829295007.mp4?token=gg6u7_1tflk0mr3IsdH6kdBjMym1GgVwO3ua95eAvVbhQrGr7OQU49tBWXbv96fa6Vmwsozc5nuHGL_Wlrs9Lyv5E8ORetrW9Ss-Ltz4V4MECHxRgltEWyKqM2qVmUEAWgZ1n0P1IridZ4Z6xxDTS9BY_XLWBQDS3bntTgK3yIIAyqrog5iH30FdErJqduKOT_mTlBTh1ugb0PObp923S6Bg9AblqxOje8Wtsz1lgM1oJqaqVVTbeh-NjeePFb6fh8yN6wHzABa2A0DhEu1Xs9M1hGiukmtjwuupFPUpjS0WMJBF7qCjniJIcdnKMTrDeEseaxj6ukqJyh6pj1Jhgg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
🇨🇳
⭕️
حسین مرعشی دبیرکل حزب کارگزاران:
🍆
چین سفر قالیباف به چین (و گسترش روابط تهران-پکن) را مشروط به موارد زیر کرده است:
۱- باز کردن تنگه توسط ایران
۲- دریافت نکردن هیچ‌گونه عوارضی
۳- پایان دادن به اختلافات خود با عربستان
۴- پایان دادن به اختلافات خود با آمریکا!
@News_Hut</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/news_hut/70989" target="_blank">📅 12:34 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70988">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">🚨
🇮🇷
روابط عمومی سپاه پاسداران:
ساعاتی پیش دو فروند کشتی نفتکش که با تحریک ارتش آمریکا خدمۀ خود را پیاده کرده و برای گذر از مسیر غیرقانونی در اختیار عوامل آمریکا قرار گرفته بودند، با رفتن روی مین منفجر و متوقف شدند و در آتش می سوزند.
@News_Hut</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/news_hut/70988" target="_blank">📅 11:51 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70987">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/P0gD3_rxSpVI454rERUki8mb6YnuOwjpE9hSEM-m1XpulabgosHo0wf5MKFm7limm0zdkQxaOw4jMcu8oKl3zp839QbsVG9zyAYK4D802dbtfADkvKfLdAjkRc_m1q5lV7OXPrAyunC6rYAbn2iwLOh6fAZyauAEYJ0AGitiGHD6WuSdQtwhbApjcbtD1Jl0M6A8TNGu7SwHgxeCYiJfk0Ke2d84v41JwefEVyQ0r8r7sGLQmUbSS95D6UxdpzeXSLZi1Ixdz3UGQogAt9b14eYbx6b8ZnnAOyh9-Wj7bCBi4gASHCFqXtD9rY0rBigIoXL4iCwVelDEn6V5RU2PwA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
⭕️
🇺🇸
پرزیدنت ترامپ:
من برخلاف گزارش «ای‌بی‌سی نیوز» (که اخبار جعلی منتشر می‌کند)، سعی ندارم ایران را به پای میز مذاکره بکشانم. برایم کوچک‌ترین اهمیتی ندارد که آن‌ها توافقی را امضا کنند که از نظر خودشان بی‌ارزش است.
وضعیت فعلی ما را بسیار بیشتر می‌پسندم؛ چرا که تقریباً کنترل کامل تنگه هرمز را در دست داریم و اقتصاد آن‌ها نیز در حال فروپاشی کامل است. آن‌ها صرفاً دارند زمان را سپری می‌کنند تا با سرنوشت اجتناب‌ناپذیر خود روبرو شوند.
مردم ایران چه زمانی قرار است قیام کنند و بجنگند؟
@News_Hut</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/news_hut/70987" target="_blank">📅 11:27 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70986">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/43dc462e7e.mp4?token=XgnWHwX2WS4ElNVLLCFP050FOEvpEXzJmLOYsf-WTsO_EXreWnrm9P75ZnhaNbsLBi6zeLzrCaU-PXkQ4iNhfLoRTsVVWn4ydlA2IiQQyw7N-oKr70HwL2bSsmRBqt5FJY9mzR017wRdEWdmCNjC1R9aLn3_if7Nw0J6KJkuRFiwQ4zVDivPSieMDQd8kes9iv5i6iwUxKA6LeFpecjjfiaqrXkJdLWtsS2vDukal7ggu2HDAbp16RMJYnTtddjyLc2eoU337gwfw0Y3mW29oOKECznHlLBYQBhrwW7d_ffca-jIilKdF_TkbNdHdDqXp8I1lbC4WLxj_8zczS2_2w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/43dc462e7e.mp4?token=XgnWHwX2WS4ElNVLLCFP050FOEvpEXzJmLOYsf-WTsO_EXreWnrm9P75ZnhaNbsLBi6zeLzrCaU-PXkQ4iNhfLoRTsVVWn4ydlA2IiQQyw7N-oKr70HwL2bSsmRBqt5FJY9mzR017wRdEWdmCNjC1R9aLn3_if7Nw0J6KJkuRFiwQ4zVDivPSieMDQd8kes9iv5i6iwUxKA6LeFpecjjfiaqrXkJdLWtsS2vDukal7ggu2HDAbp16RMJYnTtddjyLc2eoU337gwfw0Y3mW29oOKECznHlLBYQBhrwW7d_ffca-jIilKdF_TkbNdHdDqXp8I1lbC4WLxj_8zczS2_2w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
عطریانفر، عضو شورای اطلاع‌رسانی دولت:
پزشکیان اول توسط شورای نگهبان برای شرکت تو انتخابات ریاست‌جمهوری رد صلاحیت شد ولی شخص علی خامنه‌ای صلاحیتش رو تایید کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/news_hut/70986" target="_blank">📅 11:01 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70984">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ITERjCuC55Ge25_ba2jVcN_2MRec5UMI5hLd-pwTq7QxC5CW8S62a7JST2zANKrzPkP00GdRMLIp32pdPobld2j1zWNIPTKDqGLcBH16X_Bx3qE1St05NFNLM6bcDy8AJmmLnQdmi2CcIlD7I7b-LTFr08_68peEe1T05eGdmAcGGIW84F5LRscyVwxGHyAOahjeODWbfXvh-iQBiEe9yDD3skBj3zPqIw-9tqVLvDjd84z4XrrfP2l_zGsLZFgTjfM7qIXKOiZZFhpgG0t5VHTCd-MdrxF_TGDbCTxp-jkbz8Pb6PZqcm5e0Ej6SSY3fquNTnc0ntBHNsa-lZ2lZg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/00f0caae86.mp4?token=GJ-OQnEoHjQZxDhEH6seLnYAFIb9UKB2hitoIZ7OliH2imqi_wYYfDwKvEHRLIiaE5LBsBDdZaAIluDGGCXi3PUNHMWN97rgy7mAHJWd2gZ_QYKH49chkxDk5OKbvaGXnLQp2N2bc3Muehn1lBvM8uHKaiYdsyb4SlFkNnrkv5jL6qJK-2RoMosHIZ4dBwK__X-qELmESHufhflFO2zWBqmGIj88NJhMBMs6TXIh9jeE67evaJBNz-XCWknqkH_saZO-xuJNBvlq_FF_PdjtW7ADvW5JgdzU6PU9g-EkXYLbj2dbnNanpPK_IaLJi_eehrdde-r-K-vSB0lbAta60w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/00f0caae86.mp4?token=GJ-OQnEoHjQZxDhEH6seLnYAFIb9UKB2hitoIZ7OliH2imqi_wYYfDwKvEHRLIiaE5LBsBDdZaAIluDGGCXi3PUNHMWN97rgy7mAHJWd2gZ_QYKH49chkxDk5OKbvaGXnLQp2N2bc3Muehn1lBvM8uHKaiYdsyb4SlFkNnrkv5jL6qJK-2RoMosHIZ4dBwK__X-qELmESHufhflFO2zWBqmGIj88NJhMBMs6TXIh9jeE67evaJBNz-XCWknqkH_saZO-xuJNBvlq_FF_PdjtW7ADvW5JgdzU6PU9g-EkXYLbj2dbnNanpPK_IaLJi_eehrdde-r-K-vSB0lbAta60w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇷🇺
🇮🇷
🇮🇷
پوتین در دیدار با پزشکیان:
خواهش میکنم سلام گرم من رو به آیت الله سید مجتبی خامنه ای برسونید
@News_Hut</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/news_hut/70984" target="_blank">📅 10:30 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70983">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/48458cadfa.mp4?token=bPWBy_qZ8-l1ez07oChW-mkFI-0WPAil-aQyK-Z_JiIGeo4OSspomfHav2xHBczgBtWZfMjC1DDDP2wJ5h64F5cE00SZa-ohKY9wRwhNVIqKO8DLUZjbkKJqlyly8gRnAh-sFD3G1N7hNyGOeAGX_U6II0OCV1Fxw29U-pRnhnscmONsslGChVHEmrChiiU6t9MD2VET1vv_BhJG0u51ILXD7fST02gMdmcDVGTEp2l3VQ5ftD2PgNNGPDCNUGepEK_qONOSl9PZr8rvG_kgFp1w2keChJ18nm9cb5DJ2zUnfy38oVCb3-TxVhutz56r2gYFHQuFKAqb3UZUhKLSSA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/48458cadfa.mp4?token=bPWBy_qZ8-l1ez07oChW-mkFI-0WPAil-aQyK-Z_JiIGeo4OSspomfHav2xHBczgBtWZfMjC1DDDP2wJ5h64F5cE00SZa-ohKY9wRwhNVIqKO8DLUZjbkKJqlyly8gRnAh-sFD3G1N7hNyGOeAGX_U6II0OCV1Fxw29U-pRnhnscmONsslGChVHEmrChiiU6t9MD2VET1vv_BhJG0u51ILXD7fST02gMdmcDVGTEp2l3VQ5ftD2PgNNGPDCNUGepEK_qONOSl9PZr8rvG_kgFp1w2keChJ18nm9cb5DJ2zUnfy38oVCb3-TxVhutz56r2gYFHQuFKAqb3UZUhKLSSA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
ایشون رکورد دار عمل زیبایی بین آقایونه و تا حالا بیش از 300 عمل زیبایی انجام داده!
پسری که عمل زیبایی نکنه اسکله، تا حالا 200 میلیون خرج ابروم کردم، 150 میلیون خرج لبام شده
😶
استایلم فقط 400 میلیونه، 500 میلیون دادم که خط سینه بندازم. پسر باید به خودش برسه.
هزینه روزمره‌ام روزی 100-150 میلیونه.
@News_Hut</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/news_hut/70983" target="_blank">📅 10:03 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70982">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">⏺
🇮🇱
نخست‌وزیر نتانیاهو:
آیت‌الله‌ها می‌خواهند من در انتخابات شکست بخورم؛ حزب‌الله و حماس هم همین‌طور؛ و البته ترکیه نیز خواهان شکست من است. آن‌ها این را آشکارا بیان می‌کنند.
صادقانه از خود بپرسید: دشمنان اسرائیل می‌خواهند چه کسی در این انتخابات پیروز شود؟ به شما می‌گویم: آن‌ها نمی‌خواهند من پیروز شوم.
ما برای کل جهان آزاد می‌جنگیم. آن‌ها این را می‌دانند و به همین دلیل است که می‌خواهند ما شکست بخوریم.
ما اجازه نخواهیم داد آن‌ها پیروز شوند.
@News_Hut</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/news_hut/70982" target="_blank">📅 09:32 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70981">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/ec549d5483.mp4?token=ZAUbJvbM4008JTTw6etDg8m0ov7yJWd0NkVBRZE1d0VSXsXxFeheyLZitvOunHEua52WElTY4cyeJwWP1jXmMeHIVyeM1Bu854IW06pjODtqsrKxILMDVjSp_DWdj5IZAeuN0yVsGONYW3GwJc4CG9pOE4IN_1dtjD1MW-tmtnALkDFrACRpIfCGgtwsx90tXLN7hkyCaj09z4ouBrhCDximHWL4vwpTAiWY7HLt3AMFye5_9rcNJyptVf_SsCWGQatNgLbYIAY2FG7ziVunkCDV3oATZTMo2Vfpt6ENtUVjeZGJCyAaF02nlUUTSqir9F_MS90G7ONB-nqWY3-QbA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/ec549d5483.mp4?token=ZAUbJvbM4008JTTw6etDg8m0ov7yJWd0NkVBRZE1d0VSXsXxFeheyLZitvOunHEua52WElTY4cyeJwWP1jXmMeHIVyeM1Bu854IW06pjODtqsrKxILMDVjSp_DWdj5IZAeuN0yVsGONYW3GwJc4CG9pOE4IN_1dtjD1MW-tmtnALkDFrACRpIfCGgtwsx90tXLN7hkyCaj09z4ouBrhCDximHWL4vwpTAiWY7HLt3AMFye5_9rcNJyptVf_SsCWGQatNgLbYIAY2FG7ziVunkCDV3oATZTMo2Vfpt6ENtUVjeZGJCyAaF02nlUUTSqir9F_MS90G7ONB-nqWY3-QbA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
〰️
سنتکام ویدیویی را از حملات به ایران منتشر کرد؛
سنت‌کام، فرماندهی مرکزی آمریکا اعلام کرد نیروهای آمریکایی در روز اول سپتامبر، موجی از حملات علیه اهداف نظامی ایران را با موفقیت به پایان رساندند.
بر اساس این بیانیه، مواضع پدافند هوایی، سامانه‌های راداری، تجهیزات و تأسیسات دریایی، زیرساخت‌های مرتبط با مین‌گذاری و مراکز ارتباطی سپاه پاسداران هدف قرار گرفتند.
﻿
@News_Hut</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/news_hut/70981" target="_blank">📅 09:01 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70980">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/news_hut/70980" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/news_hut/70980" target="_blank">📅 02:00 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70979">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JnytfefmyzJVF2eW5VUarvHAKM88XVXPhDb49jEKWiFCxfzEWcvGUrAsz9MKJ2t5f2OXYEzLdd6_Cx5wAnuHxKf1PieLl1TeoLGGggmYFFyLGV-8znIUzC4AcsTnkNkZfSkNHGVLIsPxckwCGbqKF30qWQOlZ5TbSFkD1_ampnu8rCkysfh3Q67xs6fHXpHc4F1MQlEZndT5iYSRdWvr-SxJsLZ7uI1T5_0gsDYV43phA0oAXC35BOAYvcID0mc-uEPVbHPpMUc4HQMC52rRGdzyqIMb_t1bAmB8T1ECDHXU7rxlYc7xwKKA1YOsauQZhWiWtFPsycLzJlQYBNKlDA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🦖
سایت جهانی
TrexBet
می‌برتت وسط
جنگ
بزرگ!
⚽️
استقلال
🆚
پرسپولیس
⚽️
اینجا فقط فوتبال نیست… دربی‌ـه!
۹۰ دقیقه جنگ، کری‌خونی و هیجان تا آخرین سوت!
🦖
🦖
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
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/news_hut/70979" target="_blank">📅 02:00 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70978">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">🚨
منابع عربی:چندین انفجار در کویت و بحرین رخ داد.
@News_Hut</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/news_hut/70978" target="_blank">📅 01:44 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70977">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EwHKkHZ77jQJ-Hxi9i8ZOJ51Wmj_LzNviqiePlom9w3v1hVnJL9ppQRunr1Jvs_UAysXYcZ5aEZhZiF8Uiow9PneD__bGlptbsM-Q9LO-fUNBQlsKXRP9M2_7aU8mjGPSAL-sAE6g6Glrj072y1QIA3DSKZQffLPVIsA5okcqYR_6KwvLvqp8yZCegj-JCfVGZLrsdVs17LxKLJrtj3GRTyMl2DwT4x5YTCFoNgNNgMkjk3RB4qkFW6dQEU6GeuBiXoAzV10Fjht4EIDyktwet8ztdYtdnr-dpAU-BTc5VZ01lKS7S1Bltw0cdPHxgOPQhjwf15O206ws1piQ3bgqg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
کویت اعلام کرد پدافند این کشور در حال مقابله با پهباد هاست.
@News_Hut</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/news_hut/70977" target="_blank">📅 01:40 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70974">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">⏺
🇯🇴
نیروهای مسلح اردن:
پدافند هوایی کشور ۱۳ موشک بالستیک را که وارد حریم هوایی پادشاهی شده بودند، رهگیری کرده است.
به گفته ارتش، ۱۰ موشک رهگیری و منهدم شدند و سه موشک دیگر در مناطقی دور از مراکز جمعیتی سقوط کردند.
در این حمله هیچ‌گونه تلفات جانی یا مجروحی گزارش نشده است.
@News_Hut</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/news_hut/70974" target="_blank">📅 01:29 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70970">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/IYLwd0xW6cuDyeBnLr0ENs8BObH3lX6s1zmvQWx74ec0SuoPmts-URnqqObGzGoopt3CHq58IEgOsaCH9QXbJPl9pMmmJBW0nXmzn7so_F7Pgnw58tOK_l0pXVLq8tridWBq_YPIcGWr-47TY3E0UoTnCh-uCtIkUh2VWY3d12Kd6Y9i99P8eTlSYXthxBJGTf3DemALqZ7roeAso8Ek6BQ2G5XssCfSachr6V0zCNcXdMkaEs1-GXe9imPDacxIFpsGq3cyqCCfI_wiJjBsIdUkxL2nvugV2N-r7lI5sMt92FkYIfN2YG736w6XXsWWoxjpEWbsFiyAlfnQee5LAQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/703c34050b.mp4?token=avGaQTnSE_xwn1xPIPrE_yZjnj_DDzEUO-w_OlqSYbeg3H9bTJg5SId97B5FnfBHYxt0KnBN7c_ZVk1JBp9LjioI_uvKBjq26eHC-s_TJuFk0yO3U5bP2BmgRGIootqcSh8bOzcTRlAvfxLHbMAI8Alm59nozXlRSP2ZGLu8dSTc6kjdMxSX0541KUAxvB6id10Q5rLevdp5WhD9N5hkYgqFnYBExC3ThnuINvlIe5k4EFY8kVXNuhFxDFlco9m89rkLYURr7fe9nGY2vI-P-TCQA-q4f5rtCAXOkf3Gf4iChr-bMbpdz-9nOe8LJBz-5EK58Qyk4syEUu5R_mY-kw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/703c34050b.mp4?token=avGaQTnSE_xwn1xPIPrE_yZjnj_DDzEUO-w_OlqSYbeg3H9bTJg5SId97B5FnfBHYxt0KnBN7c_ZVk1JBp9LjioI_uvKBjq26eHC-s_TJuFk0yO3U5bP2BmgRGIootqcSh8bOzcTRlAvfxLHbMAI8Alm59nozXlRSP2ZGLu8dSTc6kjdMxSX0541KUAxvB6id10Q5rLevdp5WhD9N5hkYgqFnYBExC3ThnuINvlIe5k4EFY8kVXNuhFxDFlco9m89rkLYURr7fe9nGY2vI-P-TCQA-q4f5rtCAXOkf3Gf4iChr-bMbpdz-9nOe8LJBz-5EK58Qyk4syEUu5R_mY-kw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇮🇷
امشب از نقاط مختلف کشور به سمت مواضع آمریکا موشک شلیک شده؛
🤩
تسنیم:
امشب یکی از گسترده‌ترین شلیک‌های موشکی ایران (به نسبت درگیری‌های اخیر) به سمت پایگاه‌ها و مناطق آمریکایی انجام شده است
ایران هشدار داده بود که حمله دشمن آمریکایی با پاسخ چند برابری مواجه می‌شود.
@News_Hut</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/news_hut/70970" target="_blank">📅 00:25 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70969">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">🚨
🇮🇷
سپاه پاسداران: پادگان تفنگداران آمریکایی در اردن موسوم به کمپ تبتین هدف موشک های بالستیک قرار گرفت. تعداد زیادی از نیروهای آمریکایی به درک واصل شدند
⏺
روابط عمومی سپاه پاسداران انقلاب اسلامی:
در پاسخ به این شرارت سبعانه، رزمندگان دلیر نیروی هوافضای سپاه در موج دوم عملیات تنبیه متجاوز "با رمز مقدس یا رسول الله (ص)" با حمله سنگین موشک های بالستیک به پادگان تفنگداران آمریکایی در اردن موسوم به کمپ تیتین، واقع در سواحل خلیج عقبه، تعداد زیادی از نیروهای آمریکایی را به درک واصل کرده و چند تاسیسات مهم و بالگردهای هجومی دشمن را منهدم نمودند.
عملیات انتقامی نیروهای اسلام ادامه دارد.
@News_Hut</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/news_hut/70969" target="_blank">📅 00:14 · 11 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>

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
<img src="https://cdn4.telesco.pe/file/djxZJL032Xjs2Lwb5RTCxPXPPL9rgtkBICFLTe8nQTjXAN0fsk6XzLiJTv_vtJ66LGnY_ea-F5X4WnygEeZ1pjUhuNBCsu7v72T98y4-pot-s3HbCuY00GEQHW4ZgIJBoqHchyUP5lyu8ie7vVrai4dH996zWAp5scvna0PpVMSCsq_ebPmgbgXvAo9nn08P-ta8lJyOxLi6yofK0zxGSMrZ3-s5YVqPsYfNCFVqm0LyqX_3TFcKgtJwgzuY3uXHhNPcjRPAzjIlVkO6P_xg_05sfco92W4OYKMt5W4PizUfX9MppfT0eQLrBZPhVqkH1_QWxVtWB1q60gQRfH3FBw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرگزاری فارس</h1>
<p>@farsna • 👥 1.81M عضو</p>
<a href="https://t.me/farsna" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 حقیقت روشن می‌شود‌‌تبلیغات@Farsnews_adsارتباط@FarsNewsفارس‌پلاس@Fars_Plus‌ورزش@SportFarsجهان@FarsNewsIntعکس@FarsImagesپیام‌رسان‌ها@Farsnaاینستاگرامinstagram.com/fars_newsتوییترtwitter.com/FarsNews_Agency</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-16 21:55:52</div>
<hr>

<div class="tg-post" id="msg-448008">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f38ca023e8.mp4?token=BOaX8QuebBsiWk6sO5EGsiSQI4wDN3pRbOdV3bqrVtVdwm8ky9rCp6aYIv22rwFdEoK2XqfqCJ4CdnRrLaUJrOwY7eag_fFFdEHPiDanBfSQiOQsFMB0QpgcFB59jO8jXz1zMYZrGwtlTRolaoxWmL1lqScdTCvbTL1K3V57TZooEP301KeQbzRoGs_NpGJkif4Dmp_4A7pWCbioLXnHzju1lHv7JdeRifOsi7bNid3M4D70GtPlqgFnej_kC5koTt22KB7tyaI71YuYjF-fWVbYJmTBh9qNpBHxrOogakKU2Is70liVO5lQ6kjlJ3SwPDkhq3ZPSjZqbCQWFxKoKw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f38ca023e8.mp4?token=BOaX8QuebBsiWk6sO5EGsiSQI4wDN3pRbOdV3bqrVtVdwm8ky9rCp6aYIv22rwFdEoK2XqfqCJ4CdnRrLaUJrOwY7eag_fFFdEHPiDanBfSQiOQsFMB0QpgcFB59jO8jXz1zMYZrGwtlTRolaoxWmL1lqScdTCvbTL1K3V57TZooEP301KeQbzRoGs_NpGJkif4Dmp_4A7pWCbioLXnHzju1lHv7JdeRifOsi7bNid3M4D70GtPlqgFnej_kC5koTt22KB7tyaI71YuYjF-fWVbYJmTBh9qNpBHxrOogakKU2Is70liVO5lQ6kjlJ3SwPDkhq3ZPSjZqbCQWFxKoKw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
یزلۀ عراقی‌ها در صحن حرم امیرالمؤمنین(ع) در سوگ رهبر شهید انقلاب
🔹
مردم شعار می‌دهند «یا حیف تموت العیاله»؛ یعنی افسوس که عزیزان از دست بروند.
@Farsna</div>
<div class="tg-footer">👁️ 686 · <a href="https://t.me/farsna/448008" target="_blank">📅 21:55 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448007">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b8107af020.mp4?token=emXmCyXVFYVF-Yvmprgyz5b4EgBDo8Hg5Uq6oOWISfXa7543xoX9cIfVikVvEKj4zhR2HTFujEFhNxW_5E7rE2_ZjlpTH8UyKwfps8pf-6HqyE8BBdjiHWvq3nKE2kxEU8jvgG1zsiNDQJ9X2Kv27m9oORMsX-2lU1gDuLLvZyI5UBIjtG0vg1Yy93x3YLlEhPfQQ6xQKoLC2YGPv2r9r0EyP4H7ps6uN9uak23llvX96WfoXXnJ0NKW1KDZUNxZmuWdwVW5E4-urf5CCsHczZvxpeKSADuYGzSn3dme9klAiVD3w15LBd7U2sc3Nc9T6T-Nig9-ZA8tpmYvjW5J66nmm-89p5E6q-pR4X8UtWB7Sy_-ebo3nnXKQsz_NBvHafe2CSOoXjrxeLLLR5QymhYAik9I-qXqVzFbyMYeMk-sKyUuwAD_E6Mowalm22D0ky0R8WP6M88M_DjvratoY-5Jb7wsaASJY7L4-t5bsLrZPyUimrjYwOsZjeyx3l1lGkhaWR_HecPNqKKeEYs7fUWqcYsecEM98wfPqy5NEtSihiVRWsBrG61QI5rwl4-5GbVKPdGgfBzH6VjN8hz4_xcf3FEOd7zZjH_hCi2FgeMZVfxa77RWMLpAQUDZ5aAFAUhA-cTAPfMThqNZVQEme0_-x2sL7lL2Spyhf4HEva0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b8107af020.mp4?token=emXmCyXVFYVF-Yvmprgyz5b4EgBDo8Hg5Uq6oOWISfXa7543xoX9cIfVikVvEKj4zhR2HTFujEFhNxW_5E7rE2_ZjlpTH8UyKwfps8pf-6HqyE8BBdjiHWvq3nKE2kxEU8jvgG1zsiNDQJ9X2Kv27m9oORMsX-2lU1gDuLLvZyI5UBIjtG0vg1Yy93x3YLlEhPfQQ6xQKoLC2YGPv2r9r0EyP4H7ps6uN9uak23llvX96WfoXXnJ0NKW1KDZUNxZmuWdwVW5E4-urf5CCsHczZvxpeKSADuYGzSn3dme9klAiVD3w15LBd7U2sc3Nc9T6T-Nig9-ZA8tpmYvjW5J66nmm-89p5E6q-pR4X8UtWB7Sy_-ebo3nnXKQsz_NBvHafe2CSOoXjrxeLLLR5QymhYAik9I-qXqVzFbyMYeMk-sKyUuwAD_E6Mowalm22D0ky0R8WP6M88M_DjvratoY-5Jb7wsaASJY7L4-t5bsLrZPyUimrjYwOsZjeyx3l1lGkhaWR_HecPNqKKeEYs7fUWqcYsecEM98wfPqy5NEtSihiVRWsBrG61QI5rwl4-5GbVKPdGgfBzH6VjN8hz4_xcf3FEOd7zZjH_hCi2FgeMZVfxa77RWMLpAQUDZ5aAFAUhA-cTAPfMThqNZVQEme0_-x2sL7lL2Spyhf4HEva0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
پنجره‌ای به آخرین وداع با رهبر شهید در شهرِ بانوی کرامت
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 1.02K · <a href="https://t.me/farsna/448007" target="_blank">📅 21:55 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448006">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Cazt-CzlIZHAqlBSs6oHw9gDeS10VW7eKyK60JsCMaYdjGFmnQWx4PkvDaBD0MH9Y8u8zKTnN_HmgfpdTKKIsDTA1stHxtfNd5Bc9cerZe62zHN3EZQvCvefjYH8CoseuE7GzkCml1PxLnpuvS6LGzu_on3fUKiqioUeJ4NZ1pjnjsImlbfe5XryH8EZOAhP4VQI6xy_dF2ToMojT9TkBH6pBeb0bSVwJiaouARS4b73teZ13j--yXFtm1L_sCwIIi3OWC48tg8PyRDReyFSBAPgiNb1WQweDouzg2R_iALOEqocKrCEsXMb6lPljqgDlvdvLpAeWiURQPOWhCcPjA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📷
محل قرار گرفتن پیکر امام مجاهد شهید در فرودگاه نجف برای ادای احترام
@Farsna</div>
<div class="tg-footer">👁️ 1.02K · <a href="https://t.me/farsna/448006" target="_blank">📅 21:54 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448005">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aw0KgF0YyoVvs3b2-7C5Q3Yq5NHonlA9NPrLvCeGK13kYDPRMi41KAnzX255fPxPM36ZyLO47yYiC9qRObXBq1dt-eD7-XGh1IdcG4t1bEZV0w8XJbyTJyumyiF6m3cV3r55MzIcHpbAWG-kton9V6HmJ0N07R2_SUMKTB6MYqhrBCJUxp4WKWRJa-WNesu74IBJKUvCyaPyWVRM-P9lykTSktUlV46cXIQEKH7NxBM2RU2feYxIYb861jrBx_nqmBxc1a9zSlCcDEhlVYWS7r0vsjnd3GwbqMOdBkt2GHgNdxJrKvgRXnq0_2rQXbMOwICGyK_HmBTwSp6W-XVdPA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ولایتی: موضع ایران در حمایت از مقاومت تغییرناپذیر است
🔹
مشاور مقام معظم رهبری در دیدار با هیئتی از انصارالله یمن: محاصره یمن باید فوراً پایان یابد و ادامه آن غیرقابل قبول است یمن امروز یکی از ارکان مهم جبهه مقاومت است.
🔹
پس از جنگ ۴۰ روزه، آمریکا دیگر جایی در منطقه غرب آسیا ندارد و موازنه قدرت به سود ملت‌های مقاوم تغییر کرده است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 2.71K · <a href="https://t.me/farsna/448005" target="_blank">📅 21:47 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448004">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d084af3bf0.mp4?token=oRjxxqAIoRAnmpB4tmb6tMpxAlRx3zFRIubXASpOCZImygz6aXwrpJC2jE7KogEsiASO9Lkgazm4opa6NhTSqJE-KOBr0SoPyukD1SrblRoZcFXFxsrXMfx1TKS7xVodmHTL6wA2l3NUlxf7U5BNlZWc76uVfL87I9JLA8lg13H0VTDyMh7gnxQQiu-dd8f2JpbUSGPYB5Oy4WTS1koakaSqd3SOoCSpJ3mmTu6as6vtZyz_tVPOCAQxko0hmOUq7bgoeFK4iJ_iBKdJpXwiRbQDURfemutLhuxURjQaL5vyZZRd42Dlse--9JB0sra8KG9DzNWY37i3Ks727YxsQQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d084af3bf0.mp4?token=oRjxxqAIoRAnmpB4tmb6tMpxAlRx3zFRIubXASpOCZImygz6aXwrpJC2jE7KogEsiASO9Lkgazm4opa6NhTSqJE-KOBr0SoPyukD1SrblRoZcFXFxsrXMfx1TKS7xVodmHTL6wA2l3NUlxf7U5BNlZWc76uVfL87I9JLA8lg13H0VTDyMh7gnxQQiu-dd8f2JpbUSGPYB5Oy4WTS1koakaSqd3SOoCSpJ3mmTu6as6vtZyz_tVPOCAQxko0hmOUq7bgoeFK4iJ_iBKdJpXwiRbQDURfemutLhuxURjQaL5vyZZRd42Dlse--9JB0sra8KG9DzNWY37i3Ks727YxsQQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📷
استقبال نخست‌وزیر عراق از پزشکیان در نجف  @Farsna</div>
<div class="tg-footer">👁️ 4.35K · <a href="https://t.me/farsna/448004" target="_blank">📅 21:41 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448000">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/OzPc-IKSTj4fltMCaApzDqsoXWNAXb8mMhhlLPhZmCpfpJSHu06aNKBtxniD-OYT7NCTgcXnN5sBwawa4-4-xo5UbCrmj_0Ewi3wUnU7fkwfMzfprRACfTKdu-LkXQMJwbmB8r-cRFj_HhcHU35eW1Wu3eflHPF2k5p5bp1ZQmlncQEzLzfxBdfrUl34HGL9nDwfBwY1VRL0Amnpt6zbBeC597_UoUUzNoVvHFwSx1Li9zTGmbXy4-BpccgnJOLoPSPvUMS4uzZK0VusqTVrGnd9yM4Z2FDeohy-kd0k1Rs2Kkqy_aTHbVARL42Exy0QJhNC-uvDChMAxQM206_xbg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/RKu3rSHCAKs0k4iWqvGXdn26vy7qdhDG5xIrUyf5EeMfQVueNTuETdyWaCmlyse3PAzuA4Clz9II5nxKKNAIKzmPeKCy26UHSYLFi-Af8vcEOQziiK9jVsSCozx3tTt0nurm8v2F-XzXyxahrW5XTg9pth6zFkmMCcnGusWnFORdpU6WiGL6iV_zp754xnlm7hZESQ6hfCKxs3i7i3w6vX0H9LXskAp1S_HuOd4bLZYDVc7lsKO6v8jG5yWmsGUZSrkRoY0X97HRouUIfzEyJbIEbG1n8Wx_Yo6WIZ3L9T3B_Nja2aJpgn_U56Z7zYFh8kVXYnxXVgbo8cZ357JO-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qXekt2SItnqzRXCAyDqQ36g3DqMvfcY72KXX1xov-6MLDIMD0HV9Zp-f9zAiG6Le-FXHYzB_rTp3-WlemqeRSZxAbsNPxUqcoiSsT37uuTq2UJHHCM0jF5x1wz_7onfK0XphBDPxjh33wNFIj2oYQ4Igd_costNYhuJ4lVB4tmXWNtPVddXCJO3cmdhviW0f9gEvI6RYdSK07rmkV86IH6cImBEPvLPbJGhYgE23r_0G9IbEG5lUuuQfCRvk4UX2UombZLW_hxK0WjADK1FF5xphQowUKmsn7Lf0OWX-59sUNGwFtXp5kLkM7NGDZqwOYbdmSqmOWbF2Adzzu4b2mg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/YXZiSU2pRqcy-FFHzr-MszVZQZwlK6Numox2AoPQrYHJdbCr3C_9MMahrST0GsfdGlgQqZUEmiXNfOdO0c96zXczf1IpKsnd8gEHoH4rjMDr7C2A4VkAZKRax-NiJBdS0RwX-PXp__-0IxWpGV9DBldsN6D5yjxTB__cN1TMBiVW_qF1N7z5tkE3vr4H3Wis2AR_ZZmpqM9rqamGbZ17qsY-8iJ2xV10t9I8JJIdv2Gw-js6sUfR7N1_4HW7QlsGOCxsj9DfqRbHM2WbR27UFiF12D--_j_kpN9fPxqdsebF-opYmyb0oxezm6VQJi-npiC2bGQXmkZpJsFYyeo4KQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
استقبال نخست‌وزیر عراق از پزشکیان در نجف
@Farsna</div>
<div class="tg-footer">👁️ 4.37K · <a href="https://t.me/farsna/448000" target="_blank">📅 21:39 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447999">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/r18plKdfha5Y2POrDdLpEF5NNijuuBEtT3e6mUwHcx2MtBefBmgLKb6F9k69qPrZnY33k_DRQ1QVnw9XAAe_AyOf8lqaKVLHprcOyBUdtLVqt3BTLoP0oS_MUY4QnH9aJ-_w58mx1eCgSKFXF0IuwlsDyCm0TjVjzbqSkhIRXaelQz_dZE2zRnf86UjX3YuaqCAQkl4tA6N3r8ABaX3lxN735Uf_2JHXO5a8WVXWlyAjlUAJon23iuD5XSDdi5sgvg8eEbuJxfoFs4TjTjviwjIl7cYweMIGTXgODZj2slShyq73BMcN43rX6vEihwjK1ieyBuFunngNsB_di15qnA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎥
آرژانتین گل سوم را هم زد
⚽️
آرژانتین ۳ - ۲ مصر @Farsna</div>
<div class="tg-footer">👁️ 4.72K · <a href="https://t.me/farsna/447999" target="_blank">📅 21:35 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447998">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cef9fb8bb1.mp4?token=ttKkEbYyz22UCHEOgPvjhjSaIOlh74BzFDvnye-IHXbgbDhtGlldQmrxeoBSYCgyaX6CgrnPublESP6qEg_7Q3jNfrFATEmhVA3mY254_9jTSglUUBDNUceVT-xEa0OM8siIYvDeBpCvf8uWXjkNRCEj2dVzUfjSt9JPocEeNiPrCbUxvh25oiyk1m5wiI-qrEWhch3xaCaP2JCJ4Pmh03ELsnI9r1IJzD33sxZNbbe-JKpzzoXBAJmpC2-x1sDm_bRrzkEXN4QQg9MazMgvN1sSlg58ZUuW2QMOh-cq00cWk428urzb0PWijYCkPJyNELa7fupYPzMrdpTzCH7ypQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cef9fb8bb1.mp4?token=ttKkEbYyz22UCHEOgPvjhjSaIOlh74BzFDvnye-IHXbgbDhtGlldQmrxeoBSYCgyaX6CgrnPublESP6qEg_7Q3jNfrFATEmhVA3mY254_9jTSglUUBDNUceVT-xEa0OM8siIYvDeBpCvf8uWXjkNRCEj2dVzUfjSt9JPocEeNiPrCbUxvh25oiyk1m5wiI-qrEWhch3xaCaP2JCJ4Pmh03ELsnI9r1IJzD33sxZNbbe-JKpzzoXBAJmpC2-x1sDm_bRrzkEXN4QQg9MazMgvN1sSlg58ZUuW2QMOh-cq00cWk428urzb0PWijYCkPJyNELa7fupYPzMrdpTzCH7ypQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
ای مظلوم تنها خداحافظ؛ آه ای تهمت‌ها خداحافظ
@Farsna</div>
<div class="tg-footer">👁️ 4.4K · <a href="https://t.me/farsna/447998" target="_blank">📅 21:34 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447997">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8857572e4b.mp4?token=sNubdeDapJXNPHeElK5v7tx40NwkvYEeXwyoOoC4xpS2jKuiMmQ7vqJkrxhj30qQoMlzBIfM3gH5U3kPJFO_KDEPjN0cp-W7A1ZztisQAtKGmASR9CcBom0AD8KcqLlsr-zvUAVhT0tbVkD2TIFder8dn0NkCnj_bT5F3Ce3vwfaWcpL4OFvuLKa5UtcjE9GF-ObeFGU7prnRcRXvtD4WcrkFHZHvKTgSYPrNlXWlPO4nUn4B36ySYaZZqGPvK_kKwRbQDwQHGvN1Vv8li1q-_w8JzxQf-int7Rz19RAia9rOsDG9V6uUMYqD7fLNS3TRH_obVipZkqvJLwAPYbjUQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8857572e4b.mp4?token=sNubdeDapJXNPHeElK5v7tx40NwkvYEeXwyoOoC4xpS2jKuiMmQ7vqJkrxhj30qQoMlzBIfM3gH5U3kPJFO_KDEPjN0cp-W7A1ZztisQAtKGmASR9CcBom0AD8KcqLlsr-zvUAVhT0tbVkD2TIFder8dn0NkCnj_bT5F3Ce3vwfaWcpL4OFvuLKa5UtcjE9GF-ObeFGU7prnRcRXvtD4WcrkFHZHvKTgSYPrNlXWlPO4nUn4B36ySYaZZqGPvK_kKwRbQDwQHGvN1Vv8li1q-_w8JzxQf-int7Rz19RAia9rOsDG9V6uUMYqD7fLNS3TRH_obVipZkqvJLwAPYbjUQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
مسی آرژانتین را به بازی برگرداند
🔹
گل مساوی آرژانتین به مصر توسط مسی در دقیقۀ ۸۴
⚽️
آرژانتین ۲ - ۲ مصر @Farsna</div>
<div class="tg-footer">👁️ 5.11K · <a href="https://t.me/farsna/447997" target="_blank">📅 21:27 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447996">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/faef8f323c.mp4?token=WecsnWxMvjMflmss_seDQry1iyj-8c6lDHwr__4BwdtYI9XcejVkviU3Z7DDSv1NbZBhK1_dtLL02oT2461VQ1FUFh22um1taQwxlU7IOHz118j0n65lc0fuDXqPdY9RlKYUhSdqRHKAnhh8UY2T9PdKinT0JMioKaEPWnWXR6cK2foTAaqV1G3yHUFEKyKIMy_Ns573CFDT2U6P63PxzFxiBtG-Vr7XEZt69jWbDZ96CD9TXt_e_aVoFRMwE_YA7R5pN3tXxBpwFqXPnQFWpMwCj6TMCz-JzjOAnSo63R_WqWqhSEuyH5bcaEdR-p24t_x82GkFoZkjk_1RzXpIxw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/faef8f323c.mp4?token=WecsnWxMvjMflmss_seDQry1iyj-8c6lDHwr__4BwdtYI9XcejVkviU3Z7DDSv1NbZBhK1_dtLL02oT2461VQ1FUFh22um1taQwxlU7IOHz118j0n65lc0fuDXqPdY9RlKYUhSdqRHKAnhh8UY2T9PdKinT0JMioKaEPWnWXR6cK2foTAaqV1G3yHUFEKyKIMy_Ns573CFDT2U6P63PxzFxiBtG-Vr7XEZt69jWbDZ96CD9TXt_e_aVoFRMwE_YA7R5pN3tXxBpwFqXPnQFWpMwCj6TMCz-JzjOAnSo63R_WqWqhSEuyH5bcaEdR-p24t_x82GkFoZkjk_1RzXpIxw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
صحبت‌های زائر نروژی-کشمیری رهبر شهید
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 5.07K · <a href="https://t.me/farsna/447996" target="_blank">📅 21:24 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447995">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ae1c24d01e.mp4?token=qbw22V0X2CEIVr99Pwbmvh4PB5qfCHJNFTZPWl5VVaDYjK4UvH7-_IG7DcJkk49HNMTnYaT7f9vAYaUEqOQK8rfVgbqKUFsskD6Mt5_sn9MwueSrrDeCBMM3Ywh4rihHwznq7Ua-ed3ZXVgTOod001-sc4sQZQKSj8hLvkLGYY9zjzS4p99dZu1fFQPWCjj4UOFgr9HVWtf05zX3SxzTzLRp50lMJs5x303-Yec3g4dnyjEez1mOlvexH8doLpVOqdqTjz5IyIZjl_ssxjS58ge63lZapztnJO7g92V1zDGOGBWhA9YXzGtY9EwSHcIoKobJMwljXcgX8F-vg_LGvQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ae1c24d01e.mp4?token=qbw22V0X2CEIVr99Pwbmvh4PB5qfCHJNFTZPWl5VVaDYjK4UvH7-_IG7DcJkk49HNMTnYaT7f9vAYaUEqOQK8rfVgbqKUFsskD6Mt5_sn9MwueSrrDeCBMM3Ywh4rihHwznq7Ua-ed3ZXVgTOod001-sc4sQZQKSj8hLvkLGYY9zjzS4p99dZu1fFQPWCjj4UOFgr9HVWtf05zX3SxzTzLRp50lMJs5x303-Yec3g4dnyjEez1mOlvexH8doLpVOqdqTjz5IyIZjl_ssxjS58ge63lZapztnJO7g92V1zDGOGBWhA9YXzGtY9EwSHcIoKobJMwljXcgX8F-vg_LGvQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
گل اول آرژانتین به مصر در دقیقۀ ۷۹
⚽️
آرژانتین ۱ - ۲ مصر @Farsna</div>
<div class="tg-footer">👁️ 5.74K · <a href="https://t.me/farsna/447995" target="_blank">📅 21:18 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447994">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f63256cf94.mp4?token=qJ23PZEdaQ5BOS9kC123k27x9F-liWWr0K-saHxQirJzw1DedCe0t89NlN7pIvWwmPgqMzrrt7JrDaOts9MTHqCpjKKHNOats15EoBHzJe8vZl9uEuwmP6Vf8RCUGtWggZA8QF_ELI_BZthgTdc9IhQRPAAzcoCf5ISjvjs1ecYz_1acXylqTd_R9ZXrxYCYTPFjzBHt25oekfpdmrMTx1PVaR89QhzuEUC16MmCl6-wu_8EUeGnffgvpkeVsROtLszOsZd7W51Q16nx36od4XVL9ZVqoy99C53gJikKCoyyJkArOwbM5AV5uSR2xQjS4HFCs3g9FW9aMDhcapaAdw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f63256cf94.mp4?token=qJ23PZEdaQ5BOS9kC123k27x9F-liWWr0K-saHxQirJzw1DedCe0t89NlN7pIvWwmPgqMzrrt7JrDaOts9MTHqCpjKKHNOats15EoBHzJe8vZl9uEuwmP6Vf8RCUGtWggZA8QF_ELI_BZthgTdc9IhQRPAAzcoCf5ISjvjs1ecYz_1acXylqTd_R9ZXrxYCYTPFjzBHt25oekfpdmrMTx1PVaR89QhzuEUC16MmCl6-wu_8EUeGnffgvpkeVsROtLszOsZd7W51Q16nx36od4XVL9ZVqoy99C53gJikKCoyyJkArOwbM5AV5uSR2xQjS4HFCs3g9FW9aMDhcapaAdw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
مصر گل دوم را به آرژانتین زد
⚽️
آرژانتین ۰ - ۲ مصر @Farsna</div>
<div class="tg-footer">👁️ 5.76K · <a href="https://t.me/farsna/447994" target="_blank">📅 21:14 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447993">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f09c78366a.mp4?token=lcgS1nc792Mik7XTJkWbrG_KTNx49C9EbC0gv6TH5iEiEhD4snlV9da8qr2hbCQutS3W3GQF-f7pGChIHc-5nx9l84ACUozkUaNZx8k-5CI5KWvi2dEYLwvsNsug1B-JRwWd7nQgd1rV_Hvx69Nod3gWjzs7_BRXIRNcSCuvSUFBdFtKI0729s7mY2GvB3fvhJjztDS7cr4870J4H5-In9ijFvi7Ddiw3h-TYgeFUbUuYrA4s3xHwd_Qn0Q90QkrvKb8y_3r1UXVF3aNINDjHJff1v79pT9g3-mTtRm0wznY0YQgBd7ip1HoyJsIPcU3Rci3gOzRPrYsFxIW9cfIKA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f09c78366a.mp4?token=lcgS1nc792Mik7XTJkWbrG_KTNx49C9EbC0gv6TH5iEiEhD4snlV9da8qr2hbCQutS3W3GQF-f7pGChIHc-5nx9l84ACUozkUaNZx8k-5CI5KWvi2dEYLwvsNsug1B-JRwWd7nQgd1rV_Hvx69Nod3gWjzs7_BRXIRNcSCuvSUFBdFtKI0729s7mY2GvB3fvhJjztDS7cr4870J4H5-In9ijFvi7Ddiw3h-TYgeFUbUuYrA4s3xHwd_Qn0Q90QkrvKb8y_3r1UXVF3aNINDjHJff1v79pT9g3-mTtRm0wznY0YQgBd7ip1HoyJsIPcU3Rci3gOzRPrYsFxIW9cfIKA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
اشتیاق مردم عراق برای آخرین بدرقهٔ رهبر شهید
@Farsna</div>
<div class="tg-footer">👁️ 5.43K · <a href="https://t.me/farsna/447993" target="_blank">📅 21:12 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447992">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5686de84ab.mp4?token=nlVVXNR5-dbPCdh8_tdku5nCXf8AYq-Nw2ZuLVCnfCOLWtJJiEB8lkVIofBCQ99RgbOaUzNVjImHBMp502i0VkMzF7r5C4JLC6NsGFc7p8eHvdNJ8OHtEUEIp4YGu3uUMpv0Z0DyBVh6o1yXwRQ3wgJpSUy3eMWpU0VhxNNAaL8zRGpGI1Wu6A38NsfyZknmf93mFkcJflY91VaZqG4OwDlSq8fRIroZqrJQDO9BqIYuGG9C1foH4BcUirb1TToAcH52m-1WSB5Cu6Si9nx8P-FsUU_CHaO_DRgIeBhJ5ESAr2oq1lMv-96fKOtY5zIh2jzoeDIGUaD7HQNmNjfgGA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5686de84ab.mp4?token=nlVVXNR5-dbPCdh8_tdku5nCXf8AYq-Nw2ZuLVCnfCOLWtJJiEB8lkVIofBCQ99RgbOaUzNVjImHBMp502i0VkMzF7r5C4JLC6NsGFc7p8eHvdNJ8OHtEUEIp4YGu3uUMpv0Z0DyBVh6o1yXwRQ3wgJpSUy3eMWpU0VhxNNAaL8zRGpGI1Wu6A38NsfyZknmf93mFkcJflY91VaZqG4OwDlSq8fRIroZqrJQDO9BqIYuGG9C1foH4BcUirb1TToAcH52m-1WSB5Cu6Si9nx8P-FsUU_CHaO_DRgIeBhJ5ESAr2oq1lMv-96fKOtY5zIh2jzoeDIGUaD7HQNmNjfgGA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
آقا از تهران رفت؛ دلتنگی ماند
@Farsna</div>
<div class="tg-footer">👁️ 5.75K · <a href="https://t.me/farsna/447992" target="_blank">📅 21:09 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447991">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fc2bb01bbe.mp4?token=SgZR0Z-w2p7JpZNty7Tz7u3f5vFpF7LUEsVTx5jfdBoYbpaZx1zTLyjawKH_jslDG3tzp04BHlrpJzl9SHCl4sowzjVoXugglP8gmO5H_uFcyMVebhU06AXH1vQbiiBv6XEKBAJ04n0fmOE8-7oPlH5D8JQ1KVaVynOZYacmZ94fBpkSAzYzIwLqOU-hAEbrFQA6Q_VyS3J9xkBnrIcSwjsJbl93dZmp6jhNpANpPNWyiY4NLpApGxJ_f0nxs6d94AzkWhSd2e9braGR9gTIvGpZTmtHYQ89NXP-12VAwV3GimcrxJaG2c70tfO0OSUYGuc_7iFHdAPJ867YbY5YrA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fc2bb01bbe.mp4?token=SgZR0Z-w2p7JpZNty7Tz7u3f5vFpF7LUEsVTx5jfdBoYbpaZx1zTLyjawKH_jslDG3tzp04BHlrpJzl9SHCl4sowzjVoXugglP8gmO5H_uFcyMVebhU06AXH1vQbiiBv6XEKBAJ04n0fmOE8-7oPlH5D8JQ1KVaVynOZYacmZ94fBpkSAzYzIwLqOU-hAEbrFQA6Q_VyS3J9xkBnrIcSwjsJbl93dZmp6jhNpANpPNWyiY4NLpApGxJ_f0nxs6d94AzkWhSd2e9braGR9gTIvGpZTmtHYQ89NXP-12VAwV3GimcrxJaG2c70tfO0OSUYGuc_7iFHdAPJ867YbY5YrA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
هواپیمای حامل پیکر مطهر رهبر شهید و خانواده ایشان، وارد فرودگاه نجف شد
@Farsna</div>
<div class="tg-footer">👁️ 6.04K · <a href="https://t.me/farsna/447991" target="_blank">📅 21:04 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447990">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a92aa8d628.mp4?token=akS3wJxdQ89xQfy9UMGCaL6hw3Skw8323YsKgYOkPO3TSl7F_Aa3epeWo5OpJ-GLZcyVYGGRHVZp4WvarBDBWXhdFsLjV83_-m2a2ICRnJkwUUVE7bLiWEvb19ihPfM4zj3Twts3r9iwkxOvSoUU8pfeQ89xXFU_Pvx29rHtARsAHtCw-Wm1D_GTSXQTzvxaPf6X1lPN7O9Leh4u2xln6doZYPmCRAeVh-PXMG1f8cHbUxOE7c0ZWpTizp5jZ8l8_gQHHgDLuLE-YF4jEplONT0-yYDpbs9CPCJ0N-iee1tHDDPbVl0FxgCzRd8kYOgKDNWSwLEn0_YDsCJzEnLhyw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a92aa8d628.mp4?token=akS3wJxdQ89xQfy9UMGCaL6hw3Skw8323YsKgYOkPO3TSl7F_Aa3epeWo5OpJ-GLZcyVYGGRHVZp4WvarBDBWXhdFsLjV83_-m2a2ICRnJkwUUVE7bLiWEvb19ihPfM4zj3Twts3r9iwkxOvSoUU8pfeQ89xXFU_Pvx29rHtARsAHtCw-Wm1D_GTSXQTzvxaPf6X1lPN7O9Leh4u2xln6doZYPmCRAeVh-PXMG1f8cHbUxOE7c0ZWpTizp5jZ8l8_gQHHgDLuLE-YF4jEplONT0-yYDpbs9CPCJ0N-iee1tHDDPbVl0FxgCzRd8kYOgKDNWSwLEn0_YDsCJzEnLhyw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
آستان قدس رضوی: در خصوص موضوع محل تدفین پیکر قائد شهید، آستان تمامی تمهیدات لازم را اندیشیده و پس از تصمیم‌گیری نهایی توسط بیت شریف ایشان، جزئیات آن به استحضار ملت عزیزمان خواهد رسید.‌  @Farsna</div>
<div class="tg-footer">👁️ 5.68K · <a href="https://t.me/farsna/447990" target="_blank">📅 21:03 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447989">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/76f00a1bf2.mp4?token=Cvx-vBhlzwTyjJr7CTvqCfHYK3z2UKDRT-bMRdu84RE1xO4RGjwtWkMM-eu5bCIhH7uZk7QFs8ZjtTuX0GcsMX6ddfaVW3JsrzN2k_xBSyrFizCSYnH1NTb2EWltJKrE-ggZm3qG7bAXbrekJ25nUNNH5dWd-4FLHS935Kmq13JsLEHvPBiLHjblwQZiVJ1c0b7Zq-61K3krY5XF_vkG82ANQo7ZYgp0uhN-q1Jobz0BSVmlvpNsVbl-s4lagtWtgckD9Yzp71G9PRQX_r0e9EsG2MdrG6qTHwDTAu7BJ2wLbwFDrEt-a7ZiCKUQFzj01jXAxKZRhCh8ItNbDobgrQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/76f00a1bf2.mp4?token=Cvx-vBhlzwTyjJr7CTvqCfHYK3z2UKDRT-bMRdu84RE1xO4RGjwtWkMM-eu5bCIhH7uZk7QFs8ZjtTuX0GcsMX6ddfaVW3JsrzN2k_xBSyrFizCSYnH1NTb2EWltJKrE-ggZm3qG7bAXbrekJ25nUNNH5dWd-4FLHS935Kmq13JsLEHvPBiLHjblwQZiVJ1c0b7Zq-61K3krY5XF_vkG82ANQo7ZYgp0uhN-q1Jobz0BSVmlvpNsVbl-s4lagtWtgckD9Yzp71G9PRQX_r0e9EsG2MdrG6qTHwDTAu7BJ2wLbwFDrEt-a7ZiCKUQFzj01jXAxKZRhCh8ItNbDobgrQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
گل دوم مصر به آرژانتین با کمک VAR رد شد  @Farsna</div>
<div class="tg-footer">👁️ 5.37K · <a href="https://t.me/farsna/447989" target="_blank">📅 21:02 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447988">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b58ed26b37.mp4?token=dRKDb7SKmjw_8xpIaews64Fq9uGrvj1wmIQtX9GEP45TNOnPqJGBVKE0b7eWn0TrS2FAO6uL7s-ni0OpGSkErQKa_3gBIDIhd6UjkrqgPLR_QrDLRDylC5XPKJhUbeqmqRjSKH_3xeqB-THrWI7QPXAKohamfcQqfWhMoV_PDbysmRx13htdcFgrtpWvBjRW_ak7piWj59xD50s403FqO80Omuok0YWC74A5yBvR-3BkSfND45fEixa-L8TJEudFm0KrWrZYhokJ8qNGdRjCzyCuwQkdCO_jGozjEo0hZsyA9cBOqogDtA2Abb8Y6n-EN_NRct1_WJSupXb0UHSUGQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b58ed26b37.mp4?token=dRKDb7SKmjw_8xpIaews64Fq9uGrvj1wmIQtX9GEP45TNOnPqJGBVKE0b7eWn0TrS2FAO6uL7s-ni0OpGSkErQKa_3gBIDIhd6UjkrqgPLR_QrDLRDylC5XPKJhUbeqmqRjSKH_3xeqB-THrWI7QPXAKohamfcQqfWhMoV_PDbysmRx13htdcFgrtpWvBjRW_ak7piWj59xD50s403FqO80Omuok0YWC74A5yBvR-3BkSfND45fEixa-L8TJEudFm0KrWrZYhokJ8qNGdRjCzyCuwQkdCO_jGozjEo0hZsyA9cBOqogDtA2Abb8Y6n-EN_NRct1_WJSupXb0UHSUGQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
امروز دل‌های عاشق از سراسر جهان راهی قم شدند
@Farsna</div>
<div class="tg-footer">👁️ 5.02K · <a href="https://t.me/farsna/447988" target="_blank">📅 21:02 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447987">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8d4f9113c2.mp4?token=JrIW0zibhDeDQrFHEwmf88TWGCYv1QuF-jkgS7fY9Jw3vmkUcF55zUBoGVC-CJIq0HaCem_UAmEH7na5hieuyh6GfcQerZwU530-9Q6CMDBdNMahgWpvFcpOEF4xlq7ozhlek5qMESjai5I9l2PnvoQp5nTv40FcKMM9T0MpcfVQrts_IvJubVLeH1yJ_c3DU3WA2IM3F_-tXDH3xI380I4v542ZZSSAuwKBmSJvIz9fD0XqeGwFR_Ka5rPSnoTjNMqr7UmnOrKIQImCGxd-reEjnj2LT7ptp2F5DUcbHd6N1ekbHq1cJdsJ-oQ0VkJKO_3IzqsVZcWKrGDVRzXFHA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8d4f9113c2.mp4?token=JrIW0zibhDeDQrFHEwmf88TWGCYv1QuF-jkgS7fY9Jw3vmkUcF55zUBoGVC-CJIq0HaCem_UAmEH7na5hieuyh6GfcQerZwU530-9Q6CMDBdNMahgWpvFcpOEF4xlq7ozhlek5qMESjai5I9l2PnvoQp5nTv40FcKMM9T0MpcfVQrts_IvJubVLeH1yJ_c3DU3WA2IM3F_-tXDH3xI380I4v542ZZSSAuwKBmSJvIz9fD0XqeGwFR_Ka5rPSnoTjNMqr7UmnOrKIQImCGxd-reEjnj2LT7ptp2F5DUcbHd6N1ekbHq1cJdsJ-oQ0VkJKO_3IzqsVZcWKrGDVRzXFHA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
این نماز در حافظهٔ تاریخ ماندگار شد
@Farsna</div>
<div class="tg-footer">👁️ 4.68K · <a href="https://t.me/farsna/447987" target="_blank">📅 21:01 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447986">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cbc3fd34b6.mp4?token=CV5w1pId1lrIcsfRgv18hLra1YV2AcyC-2KTX-l1q3UBmK6tBS1s6taH3JlaylAT1dIn_Mg-N8jYM2OEsVu3QD7rySlGpi4LNuD29_YZZ0mWrRzrEHQ1T8J2vsjR0HxXU5BHWjKyP_B43zw3vR4SotBs7qYkVuuQW1iS790ToiGSK_OIoHPcS5T30x62d_2XjTCRkXVDZsz6FlWtuZmcNCVBovI3FBORcKTsXb2qxh3J1Wv69_GllnbTp7vI92y8uz6qtfdTVka2dHGnaOqYhS_6-mAp5eu97khnC5mjSckRYuYhrHvoSA2IkzbQPvl1z3jtqC7hiXqIiTbWgMI5VUY9C1F_XGbS0zipJjdhEsBuuRTLzrnk27_15_xbpSp2b2vS4PNsY6sU-q1H4E8RWTdpzf_o-Wt9FQuzzt5q_PEm24OIG4FOZh886jniHzV5T0g4GzlvbaCTZk8wnYXaTJ6LOCJ5O0OBI7s8ZiVB0-yxybzaqb6d-nuRueOhKJNz6WH454qtDoqtaAKFeBDpx7_CCYwANP1YfMrOhq90QX0Zu8hZnrWcBA-0VYjSOAAcND3ZQrRI7HGoxgWgiEVDR1Urhn2S5PDdDAA5permrzRsFRSprCWycmFqCig-DHam0zVzVsX31rZdjB1nS4BFomGqCIcyVXspGd52HieYxtA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cbc3fd34b6.mp4?token=CV5w1pId1lrIcsfRgv18hLra1YV2AcyC-2KTX-l1q3UBmK6tBS1s6taH3JlaylAT1dIn_Mg-N8jYM2OEsVu3QD7rySlGpi4LNuD29_YZZ0mWrRzrEHQ1T8J2vsjR0HxXU5BHWjKyP_B43zw3vR4SotBs7qYkVuuQW1iS790ToiGSK_OIoHPcS5T30x62d_2XjTCRkXVDZsz6FlWtuZmcNCVBovI3FBORcKTsXb2qxh3J1Wv69_GllnbTp7vI92y8uz6qtfdTVka2dHGnaOqYhS_6-mAp5eu97khnC5mjSckRYuYhrHvoSA2IkzbQPvl1z3jtqC7hiXqIiTbWgMI5VUY9C1F_XGbS0zipJjdhEsBuuRTLzrnk27_15_xbpSp2b2vS4PNsY6sU-q1H4E8RWTdpzf_o-Wt9FQuzzt5q_PEm24OIG4FOZh886jniHzV5T0g4GzlvbaCTZk8wnYXaTJ6LOCJ5O0OBI7s8ZiVB0-yxybzaqb6d-nuRueOhKJNz6WH454qtDoqtaAKFeBDpx7_CCYwANP1YfMrOhq90QX0Zu8hZnrWcBA-0VYjSOAAcND3ZQrRI7HGoxgWgiEVDR1Urhn2S5PDdDAA5permrzRsFRSprCWycmFqCig-DHam0zVzVsX31rZdjB1nS4BFomGqCIcyVXspGd52HieYxtA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
تلاش بی‌وقفه جوانان عشایر عراقی در دل شب برای استقبال هرچه باشکوه‌تر از رهبر شهید امت
@Farsna</div>
<div class="tg-footer">👁️ 4.38K · <a href="https://t.me/farsna/447986" target="_blank">📅 21:01 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447985">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/X2f0s3vqRIVEGJRxRQbHnegaUbXX1l5h-uQrp0UcQPAJd98zf2wnFwJDx45T10aRLJdm2VBKIWWNv1q82wHzhMRzrReT608ipNYo2u0IdzfFwGfUrz3TJ1Aptgp_5pPxvbnOVzOP1SYgTYKq8P4cUUUoi-25Dhhik9SFsSpJQxlgVRsEY2UkJwsI8Kx06-KDnm8WUiX_jn5y76deWmwysOxTG6eSc1o3reJRuCq5kDs-FFVebYRjqNL_jYIQVxL65jY778jMN4Aiid_kCGDlmH6jgBI1K5Ga2AUMRPCk_IiRdB_pWzMh0r5pKjROVvxlP820kceqEImIHey0B3Rj7A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎥
ترامپ: به فروش اف-۳۵ به ترکیه فکر می‌کنیم
🔹
رابطهٔ ما با ترکیه بهتر شده و ترکیه از خیلی جهات، بسیار وفادارتر از کشورهای دیگری بوده که فکر می‌کردیم به ما وفادار بمانند. @Farsna</div>
<div class="tg-footer">👁️ 4.75K · <a href="https://t.me/farsna/447985" target="_blank">📅 20:59 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447984">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b92c2e88cb.mp4?token=tE5bjerELOP2xa53TOPN_Lt51ZHETWLoXoT3jruzpMX9Pv4BWLyicwZ4OrdQPOyrcM7GfN2ntjD3MNoldIgUNHpng55vvyBTEBum1OnLhBvhgXdVQYmUiYZKUfkfR4cpWkDFfrIo3c4V4WwNVrO-JFabncPGZaYvq6gJrxqX6lFqw1Gf2c7HyZ4rMMED-nUQSOcN38_0ysU_721gA74uk2lChKb6-D2wENzHUq4-jNyvboZ-niKTSEzUNfc5ntcsaI2M3qn6GWDGfuylIUeYgwtciyvi-UZQ2wlBhi5qNJVNo4eilrYqxRP7gsvIIOXkJvl-umPhkUF_M6O8pa8bDQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b92c2e88cb.mp4?token=tE5bjerELOP2xa53TOPN_Lt51ZHETWLoXoT3jruzpMX9Pv4BWLyicwZ4OrdQPOyrcM7GfN2ntjD3MNoldIgUNHpng55vvyBTEBum1OnLhBvhgXdVQYmUiYZKUfkfR4cpWkDFfrIo3c4V4WwNVrO-JFabncPGZaYvq6gJrxqX6lFqw1Gf2c7HyZ4rMMED-nUQSOcN38_0ysU_721gA74uk2lChKb6-D2wENzHUq4-jNyvboZ-niKTSEzUNfc5ntcsaI2M3qn6GWDGfuylIUeYgwtciyvi-UZQ2wlBhi5qNJVNo4eilrYqxRP7gsvIIOXkJvl-umPhkUF_M6O8pa8bDQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
گل اول مصر به آرژانتین در دقیقۀ ۱۵
⚽️
آرژانتین ۰ - ۱ مصر @Farsna</div>
<div class="tg-footer">👁️ 5.08K · <a href="https://t.me/farsna/447984" target="_blank">📅 20:56 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447983">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cbb4602b4c.mp4?token=bjiQK51iJYQS6kevfzASvarOSKJcCZPHwYLvXnk97R2oVESyoitRPe3UMioFTtZAVNZotVdd10wCR7FdjP1FlEGOSpHbNTnWkaAScHhp3tL96eD9aPyjS0XeYK9ktN7EKmpPtgtoXbdwKj3d2XHquR3JbovKmFL6rN4YXXaQYIL9svzhIDuIP3mZRCxpUVhzHZK0rMrUE3Wj3pLgBh4YuuVTIcPfsJBBo93Sj2YmRTIhf7D0VJFKiVWjTCCfawRxfN0TT5fpWaO6rzTTwX6CS78VjhU6wuFBL0Tj9GqqW0ltkFlDQRMCyXxtKW-Lx-aj-l9PyQJgzt0WcMseOM4BGA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cbb4602b4c.mp4?token=bjiQK51iJYQS6kevfzASvarOSKJcCZPHwYLvXnk97R2oVESyoitRPe3UMioFTtZAVNZotVdd10wCR7FdjP1FlEGOSpHbNTnWkaAScHhp3tL96eD9aPyjS0XeYK9ktN7EKmpPtgtoXbdwKj3d2XHquR3JbovKmFL6rN4YXXaQYIL9svzhIDuIP3mZRCxpUVhzHZK0rMrUE3Wj3pLgBh4YuuVTIcPfsJBBo93Sj2YmRTIhf7D0VJFKiVWjTCCfawRxfN0TT5fpWaO6rzTTwX6CS78VjhU6wuFBL0Tj9GqqW0ltkFlDQRMCyXxtKW-Lx-aj-l9PyQJgzt0WcMseOM4BGA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
حماسه‌ای که رسانه‌های خارجی نتوانستند انکار کنند
@Farsna</div>
<div class="tg-footer">👁️ 4.72K · <a href="https://t.me/farsna/447983" target="_blank">📅 20:56 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447981">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2e75b8ebc9.mp4?token=YBjN_9YufsBec-mA4BTAfDU1h3hGtejEtYSUstjzoWA89DOWjZc1iMUTpnX9fNk3SiPe6SQ83EXYcW2ZMXZxhMutzvSW2uBsxxKIx6RJkYpnsRcnpZkJQEb3Mt4O42XvT9IQmMIEJ_nHSAQhnKr83_jKfxkst0s2lDYpFgzKYcdpmwtO8Z74VI_-wN6CCgp_PsctkRVUkHrK1SItj8k9yHQyTYUjT95YhQGpaa4tT3Xt7tY815Vfh25yCd54ymHcqKyZYL2qLxg_rQfF67Xg5yeOgBzfsL08zP3zGK8TYJ1dLvijH2nJ5aSktekaAam5WTKATG7hERoK6It89Quc8xw8b3uD3Zy2xhkljudkr92gNEpWpTT9ifnatndl5fq2Sx6fSeGucElO5AaLdhuUd8FuE7oCr81a6JPzBtU-v6sNMeklhcN-tFMRvpLnZD4gqc0oRS9zibBNMAyPEngUTK9_zYY-aiypKvcCdz1zJAF29nFqpPxbofBGvEA8I6UjOA1MH_NHIYr5IsEkdN6iQNjVD1jMPx5Tco-4xdTABDcIxnrtr4Kv-qw1Li2K65DCzwwkk7SCwtRtqa4_Kui376P5XlJOPSPxyagNxhYCKyn3DximdYXtoEYbi4Tzqq2FUG6x9utzPRs6KTQil-OaH0u9rt507fTRsLYnalYqYyA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2e75b8ebc9.mp4?token=YBjN_9YufsBec-mA4BTAfDU1h3hGtejEtYSUstjzoWA89DOWjZc1iMUTpnX9fNk3SiPe6SQ83EXYcW2ZMXZxhMutzvSW2uBsxxKIx6RJkYpnsRcnpZkJQEb3Mt4O42XvT9IQmMIEJ_nHSAQhnKr83_jKfxkst0s2lDYpFgzKYcdpmwtO8Z74VI_-wN6CCgp_PsctkRVUkHrK1SItj8k9yHQyTYUjT95YhQGpaa4tT3Xt7tY815Vfh25yCd54ymHcqKyZYL2qLxg_rQfF67Xg5yeOgBzfsL08zP3zGK8TYJ1dLvijH2nJ5aSktekaAam5WTKATG7hERoK6It89Quc8xw8b3uD3Zy2xhkljudkr92gNEpWpTT9ifnatndl5fq2Sx6fSeGucElO5AaLdhuUd8FuE7oCr81a6JPzBtU-v6sNMeklhcN-tFMRvpLnZD4gqc0oRS9zibBNMAyPEngUTK9_zYY-aiypKvcCdz1zJAF29nFqpPxbofBGvEA8I6UjOA1MH_NHIYr5IsEkdN6iQNjVD1jMPx5Tco-4xdTABDcIxnrtr4Kv-qw1Li2K65DCzwwkk7SCwtRtqa4_Kui376P5XlJOPSPxyagNxhYCKyn3DximdYXtoEYbi4Tzqq2FUG6x9utzPRs6KTQil-OaH0u9rt507fTRsLYnalYqYyA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
امروز مردم قم آخرین دیدار را با آقای شهید داشتند
@Farsna</div>
<div class="tg-footer">👁️ 4.4K · <a href="https://t.me/farsna/447981" target="_blank">📅 20:53 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447980">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fd17f74433.mp4?token=ejspwi2sPgBMrITTfAo6ys4dsofZ2gOqj-fJwa4v7L4O1i0LYVK4GXwSQ0T9AQTVDEQO3sQ5pUllAZ0dpuHm4BDjIKLThi8HAHSsVh9P3Sjl2LM9PyaYCskrivzG1WRFW0I7kpJGY-EQyz7JkscVfgSc2uqbj76l4OH48b9tzdbpkm32B75L-X6UwpojAo-rWcAHitQH9J1FTBNRfi2bJRPu-Y0TEpFsEDAQyh6pAgS_6EXuTJEBR-5NnaiJ5VzYVbUegGBFSabhwzO6dYY3a7wxknN6zGmSi0wXn49C4BIhSvICWCtRDOp3lKgZahAGa3qpFNXv9Y3ln2MT-VmqoIWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fd17f74433.mp4?token=ejspwi2sPgBMrITTfAo6ys4dsofZ2gOqj-fJwa4v7L4O1i0LYVK4GXwSQ0T9AQTVDEQO3sQ5pUllAZ0dpuHm4BDjIKLThi8HAHSsVh9P3Sjl2LM9PyaYCskrivzG1WRFW0I7kpJGY-EQyz7JkscVfgSc2uqbj76l4OH48b9tzdbpkm32B75L-X6UwpojAo-rWcAHitQH9J1FTBNRfi2bJRPu-Y0TEpFsEDAQyh6pAgS_6EXuTJEBR-5NnaiJ5VzYVbUegGBFSabhwzO6dYY3a7wxknN6zGmSi0wXn49C4BIhSvICWCtRDOp3lKgZahAGa3qpFNXv9Y3ln2MT-VmqoIWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
موکب‌‌داران در مشهد آمادۀ پذیرایی از زائران رهبر شهید
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 4.75K · <a href="https://t.me/farsna/447980" target="_blank">📅 20:49 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447979">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/15dd3f7562.mp4?token=rcKdpis9lv5HiY4w1_TKrg-jYpFsf_LkYlXfttMq4MgDlAOKATI3sOG0tpinQ0tmne9PBck14PzJeamPyN8sl6Llp8rpDKzBVPlygn2qzOiAlAp6UUhGkQXJy7fUtQNgnsZbX5Ds6SMPyrHLThqjWC9gBHaQk7KGTv4CbRadATU8_umPwzYvtbdyliZOmvwxIlS0PqB0M_Gsorbw4l-N7LkWtHIBiD8WOcJY7rPihvS9T4WBUt-lSOjlsJrkVZ-wyRVqYNe4TCRzws-YNTdA1d-aoRnQdnaHODNY4KYZlA6ITDsduxL7Dh50osWIWr1b3tbbtNix-7hoYOYf7gjQTw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/15dd3f7562.mp4?token=rcKdpis9lv5HiY4w1_TKrg-jYpFsf_LkYlXfttMq4MgDlAOKATI3sOG0tpinQ0tmne9PBck14PzJeamPyN8sl6Llp8rpDKzBVPlygn2qzOiAlAp6UUhGkQXJy7fUtQNgnsZbX5Ds6SMPyrHLThqjWC9gBHaQk7KGTv4CbRadATU8_umPwzYvtbdyliZOmvwxIlS0PqB0M_Gsorbw4l-N7LkWtHIBiD8WOcJY7rPihvS9T4WBUt-lSOjlsJrkVZ-wyRVqYNe4TCRzws-YNTdA1d-aoRnQdnaHODNY4KYZlA6ITDsduxL7Dh50osWIWr1b3tbbtNix-7hoYOYf7gjQTw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
ترامپ: به فروش اف-۳۵ به ترکیه فکر می‌کنیم
🔹
رابطهٔ ما با ترکیه بهتر شده و ترکیه از خیلی جهات، بسیار وفادارتر از کشورهای دیگری بوده که فکر می‌کردیم به ما وفادار بمانند. @Farsna</div>
<div class="tg-footer">👁️ 5.41K · <a href="https://t.me/farsna/447979" target="_blank">📅 20:44 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447978">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e70aeb849f.mp4?token=Zn1D7i-04fHBOvH3G4hHB0WW0l_c30aHSs1If-8wF0Qz5R1XFLdqXMPSwm_cIbVc_FhKD2athC5LIW1TXBUVtYC6DYU0ZCyQ4HlVVeuUSAB2Y6muPMPXJ4ysQJO9CQHxFjg-VKHJfSLLWbr4PUt1LnQdOwnJuaILy8iHIVDAgTKg1cpjHy5SdOxagXZ78ueJi5YjMlPt2X3s0b2sQ51jkk6CnPtGqIOWKQao9pnnFQ7lYoWuM2op_c3q2btQL9Grns52nMsqwXni5XgTeCImVDivUH5IkvBepNBXmQoKXoOU1NvrcgL-hmpWs1kV6X_Bz-ZpKNL34tGdN4gwHHkFMA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e70aeb849f.mp4?token=Zn1D7i-04fHBOvH3G4hHB0WW0l_c30aHSs1If-8wF0Qz5R1XFLdqXMPSwm_cIbVc_FhKD2athC5LIW1TXBUVtYC6DYU0ZCyQ4HlVVeuUSAB2Y6muPMPXJ4ysQJO9CQHxFjg-VKHJfSLLWbr4PUt1LnQdOwnJuaILy8iHIVDAgTKg1cpjHy5SdOxagXZ78ueJi5YjMlPt2X3s0b2sQ51jkk6CnPtGqIOWKQao9pnnFQ7lYoWuM2op_c3q2btQL9Grns52nMsqwXni5XgTeCImVDivUH5IkvBepNBXmQoKXoOU1NvrcgL-hmpWs1kV6X_Bz-ZpKNL34tGdN4gwHHkFMA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
یحیی قاسم، عضو شورای فرهنگی انصارالله یمن: یکی از مهم‌ترین اهداف رهبر شهید ایران در موضوع یمن، شکستن محاصرۀ یمن بود
🔹
مردم یمن به برادر خود، ایران، تکیه کرده‌اند تا این محاصره را بشکنند. @Farsna</div>
<div class="tg-footer">👁️ 4.77K · <a href="https://t.me/farsna/447978" target="_blank">📅 20:43 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447977">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/18d5597dad.mp4?token=tp17VZQ0CA-M7JMP2om31nYzU2yKHXfHvV9hIUDNXyEholjHFnOJHQkGYQSm5Wi96X6i9qAvgJl46aNKG2NwjFBwyzFnBRgLXdT6aSpFNqxz4EidD0GFJNfG-KyxbOs-kfW8XFS2ofyKk4Py0sFdNZlWueSntQbkz69PAeUGVeh_U5mkmvnb_Kk1Sp15GtOGhAKm3n8updvbV0Q4EYgb1KHEttOJNV6AYD5qdHDYqNCHK-re5pgV_dLgCXXsKTBUjQgjaeXIdwITHfnuAM2nxRUxCSFJL3A0bQhH3r2yysluIBwZS1yHtJFwNFkJnqiCp1N7TZZncd7OErg4pQdR1A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/18d5597dad.mp4?token=tp17VZQ0CA-M7JMP2om31nYzU2yKHXfHvV9hIUDNXyEholjHFnOJHQkGYQSm5Wi96X6i9qAvgJl46aNKG2NwjFBwyzFnBRgLXdT6aSpFNqxz4EidD0GFJNfG-KyxbOs-kfW8XFS2ofyKk4Py0sFdNZlWueSntQbkz69PAeUGVeh_U5mkmvnb_Kk1Sp15GtOGhAKm3n8updvbV0Q4EYgb1KHEttOJNV6AYD5qdHDYqNCHK-re5pgV_dLgCXXsKTBUjQgjaeXIdwITHfnuAM2nxRUxCSFJL3A0bQhH3r2yysluIBwZS1yHtJFwNFkJnqiCp1N7TZZncd7OErg4pQdR1A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
دختر عراقی ۴ روز قبل از تشییع برای خدمت‌رسانی به تشییع‌کنندگان خودش را از ناصریه به موکب‌های نجف رسانده و رو به پدر مادرها می‌گوید فرزندانتان را برای تشییع بیاورید.
@Farsna</div>
<div class="tg-footer">👁️ 5.41K · <a href="https://t.me/farsna/447977" target="_blank">📅 20:40 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447976">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fc2a4596c0.mp4?token=E-5F_qCgz-dO1FbRfOyeSLhlav_J7qXZWegD1F6S73LN412W_vy2qsQwXsDFmQfhb5rWoyKmApr_pOp7rYNw2_hdXzpzSDaNZ-_Q9cIF7QxVE2FBvhKqSiVk_a04Rp5RnmAMiShYXoUeky-G-VnSMKu6TDBuYIpsu35zZzgCTYHsbpyq_IXnSKwHMfyBKdhAEBL37eeUJm5KIylQ14BhK3ti9EvTsh88XsdBHKH5gUrHsW0zzmjNeLGld-14QeKLV5Hd5N9V8sbD5iwJSKd9_W2ElI7IV0MxOF0VdXzwzrwbAwuqaDwyqR38-NAS5FB3Z5eiEeChTUzKyIVSGvwmRA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fc2a4596c0.mp4?token=E-5F_qCgz-dO1FbRfOyeSLhlav_J7qXZWegD1F6S73LN412W_vy2qsQwXsDFmQfhb5rWoyKmApr_pOp7rYNw2_hdXzpzSDaNZ-_Q9cIF7QxVE2FBvhKqSiVk_a04Rp5RnmAMiShYXoUeky-G-VnSMKu6TDBuYIpsu35zZzgCTYHsbpyq_IXnSKwHMfyBKdhAEBL37eeUJm5KIylQ14BhK3ti9EvTsh88XsdBHKH5gUrHsW0zzmjNeLGld-14QeKLV5Hd5N9V8sbD5iwJSKd9_W2ElI7IV0MxOF0VdXzwzrwbAwuqaDwyqR38-NAS5FB3Z5eiEeChTUzKyIVSGvwmRA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
خودرویی که قرار است در عراق حامل پیکر مطهر رهبر شهید باشد
@Farsna</div>
<div class="tg-footer">👁️ 5.78K · <a href="https://t.me/farsna/447976" target="_blank">📅 20:34 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447975">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/26e0d8feab.mp4?token=j960xYbJ1T4a6CeO80Vjnri2Rbu64wMdqO7JyFgSbA49RjRwJpiOkzebRxMsLTIlgx2Gsm3Z210CO4ETBIFyCrlwjPN1T3x062wkxDo6aIa95O9xbwmhVGATbTBDS7xdzngAea2d0aXVRlxoYNyn-KSJ37FdmyyI_PDrMapF32oB7gDsae7dimq7KH94bPd-w0M1Mi-oPWtHzmh-EkQTESbhCDU0YDdLAMWadJObwVaYa8sWaL_pnf_190qU37TCFjdQW4eLA9tGbOfFkvRmYrCsgX_HP11wP0nNs4ByR8WzLYwWK5yPpsJAPC9TyIPy-nwqvGSOzruazMWoqfBzXA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/26e0d8feab.mp4?token=j960xYbJ1T4a6CeO80Vjnri2Rbu64wMdqO7JyFgSbA49RjRwJpiOkzebRxMsLTIlgx2Gsm3Z210CO4ETBIFyCrlwjPN1T3x062wkxDo6aIa95O9xbwmhVGATbTBDS7xdzngAea2d0aXVRlxoYNyn-KSJ37FdmyyI_PDrMapF32oB7gDsae7dimq7KH94bPd-w0M1Mi-oPWtHzmh-EkQTESbhCDU0YDdLAMWadJObwVaYa8sWaL_pnf_190qU37TCFjdQW4eLA9tGbOfFkvRmYrCsgX_HP11wP0nNs4ByR8WzLYwWK5yPpsJAPC9TyIPy-nwqvGSOzruazMWoqfBzXA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
سخنگوی نیروهای مسلح یمن: اگر عربستان یک‌بار دیگر حریم هوایی یمن را نقض کند پاسخ همه‌جانبه می‌دهیم
🔹
صبح امروز (جمعه) ساعت ۵:۲۰، چند فروند جنگندۀ ائتلاف سعودی با نقض حریم هوایی یمن تلاش کردند مانع فرود یک فروند هواپیمای غیرنظامی ایرانی در فرودگاه بین‌المللی…</div>
<div class="tg-footer">👁️ 6.08K · <a href="https://t.me/farsna/447975" target="_blank">📅 20:32 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447974">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/09a5827943.mp4?token=bm3LhHdMGqhH4ouA0otYZv15POJemjSDgcO1xELR4DzDud_D9X7kHBHYNHgiIScl1JhIpnq4QfTCWl93janCFl5KCTeyMPD3Li_E6IZaW84MXjlTC0ZIBMFeVGn1Q671xBEdKtXfBXEiIGDFfCEZelseAEOgj9yFUNgv0wwzcaimmVpWvTVx3HJUEIYHLkd_IoKN3JnAqip4NKEkAKZD3z0zZH9QdkNPLRnFWJ_KDa0or15AEGu3IQFe0p8XQ2inyvXSLddncXq-t3Wnyo5BAUHuIj8Bbk8xHNNT9KkEuW3RQxwCKmRPEkaO5WYLJuaeeg_MQ-h0HQGRlYwK0mRm4A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/09a5827943.mp4?token=bm3LhHdMGqhH4ouA0otYZv15POJemjSDgcO1xELR4DzDud_D9X7kHBHYNHgiIScl1JhIpnq4QfTCWl93janCFl5KCTeyMPD3Li_E6IZaW84MXjlTC0ZIBMFeVGn1Q671xBEdKtXfBXEiIGDFfCEZelseAEOgj9yFUNgv0wwzcaimmVpWvTVx3HJUEIYHLkd_IoKN3JnAqip4NKEkAKZD3z0zZH9QdkNPLRnFWJ_KDa0or15AEGu3IQFe0p8XQ2inyvXSLddncXq-t3Wnyo5BAUHuIj8Bbk8xHNNT9KkEuW3RQxwCKmRPEkaO5WYLJuaeeg_MQ-h0HQGRlYwK0mRm4A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
مراحل آماده سازی صندوقچه شیشه ای حامل تابوت رهبر شهید در عراق
@Farsna</div>
<div class="tg-footer">👁️ 6.42K · <a href="https://t.me/farsna/447974" target="_blank">📅 20:30 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447973">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a00947cfef.mp4?token=bTys1SHMFZp0mLtzuHmA4Ofz0Xv2bwehZUM2XXjAjT2o4V3eur1jsr9w-x92ZZIcFfm1N8AgV6Jh28ysX-yWOVEtyr8ibJxewx3PJHWZll_-Okpcp8gTczmP1Z-ru_ClFzDjnkeELYrjXE6kBPLLaVK7u8mlvDIS5yMY6sC88okQorY13moVDue-az8xN86oBaBuDtbBi9nz7HkCkK0oDnHeYI8VUJM-HkQQxy_mjNPiIIZj3NylNU9iArpdjx8LyXDz824av2yIBO-YUKiH4-BMzgNZ1HYxXIrOal5hSDQyT2IrCSJ5JmqTOtv1QnTklGtLBfMAsr8DT3_PLr_vLw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a00947cfef.mp4?token=bTys1SHMFZp0mLtzuHmA4Ofz0Xv2bwehZUM2XXjAjT2o4V3eur1jsr9w-x92ZZIcFfm1N8AgV6Jh28ysX-yWOVEtyr8ibJxewx3PJHWZll_-Okpcp8gTczmP1Z-ru_ClFzDjnkeELYrjXE6kBPLLaVK7u8mlvDIS5yMY6sC88okQorY13moVDue-az8xN86oBaBuDtbBi9nz7HkCkK0oDnHeYI8VUJM-HkQQxy_mjNPiIIZj3NylNU9iArpdjx8LyXDz824av2yIBO-YUKiH4-BMzgNZ1HYxXIrOal5hSDQyT2IrCSJ5JmqTOtv1QnTklGtLBfMAsr8DT3_PLr_vLw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سعید حدادیان: مردم با پرچم سرخ حاضر می‌شوند تا به همه نشان دهند که خون‌خواه رهبر خود هستند.  @Farsna</div>
<div class="tg-footer">👁️ 8.04K · <a href="https://t.me/farsna/447973" target="_blank">📅 20:17 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447972">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3198a22e34.mp4?token=WilEX5NI9mfFSLXPAgmFE-t8C59A5r7ada8t2roziO9Mbt18ITA8JhL5nmn895R72ruf0XOJ2AmpubJpm4bfmQxUu9iNopFqH5KIxp9jahHVyfvFF7HxJ9RNA4hUWY-qZqFnUCh0Rhmn0XvCKvG_NyjWrJO9ts04UYRPTO8BtpyjlZaZWPQPZGWjaTqt_-5CjwiBhzl2rs0-of500Ko8j6I5_0sHQ74f5DDz3QwaYODuYEh85PkEl6lZxZ99VW7CsxagJ11Q9POR7lwTgNpErYN0Q8BEyH8qsr5NH7QdKo0MbEzftyQuHnbc9YHhLAbNgiN1XB3bm9JR0Y_syxARQw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3198a22e34.mp4?token=WilEX5NI9mfFSLXPAgmFE-t8C59A5r7ada8t2roziO9Mbt18ITA8JhL5nmn895R72ruf0XOJ2AmpubJpm4bfmQxUu9iNopFqH5KIxp9jahHVyfvFF7HxJ9RNA4hUWY-qZqFnUCh0Rhmn0XvCKvG_NyjWrJO9ts04UYRPTO8BtpyjlZaZWPQPZGWjaTqt_-5CjwiBhzl2rs0-of500Ko8j6I5_0sHQ74f5DDz3QwaYODuYEh85PkEl6lZxZ99VW7CsxagJ11Q9POR7lwTgNpErYN0Q8BEyH8qsr5NH7QdKo0MbEzftyQuHnbc9YHhLAbNgiN1XB3bm9JR0Y_syxARQw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سعید حدادیان: مردم با پرچم سرخ حاضر می‌شوند تا به همه نشان دهند که خون‌خواه رهبر خود هستند.
@Farsna</div>
<div class="tg-footer">👁️ 7.69K · <a href="https://t.me/farsna/447972" target="_blank">📅 20:14 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447971">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b592877158.mp4?token=OL2YJcSFrAuDGLFudvSm2_nklOH0Q42agNCLRWYA8A2j6BXlgK5ISjAUk2YOQyJ0HpNfVCBYwBnNmnk9qn4k8ODe2XdAPqoM2SBqOMKcwLSfU-NGDsVqP4bsgq82khi2_k66yDCnmzXD7_CsyMUH8TUz-z5SBeGvrFF3LyGATDnc2vVBHMHW2p8eKlDMrLvgGir-ugdo8ftZZoWmm40VURDEXtzuJsXDFVKavGYVVQm2nKv3rVSj_I8Q1RpvkUC_JG2JlK5MZGmmfIZmvgK5odwh27PtYVOFykwRQFMYg3A08aUiphTdBLViynG44Sb23wKzGfdYKV-wv_JpIKXYZA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b592877158.mp4?token=OL2YJcSFrAuDGLFudvSm2_nklOH0Q42agNCLRWYA8A2j6BXlgK5ISjAUk2YOQyJ0HpNfVCBYwBnNmnk9qn4k8ODe2XdAPqoM2SBqOMKcwLSfU-NGDsVqP4bsgq82khi2_k66yDCnmzXD7_CsyMUH8TUz-z5SBeGvrFF3LyGATDnc2vVBHMHW2p8eKlDMrLvgGir-ugdo8ftZZoWmm40VURDEXtzuJsXDFVKavGYVVQm2nKv3rVSj_I8Q1RpvkUC_JG2JlK5MZGmmfIZmvgK5odwh27PtYVOFykwRQFMYg3A08aUiphTdBLViynG44Sb23wKzGfdYKV-wv_JpIKXYZA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
آماده‌سازی ورودی حرم امام حسین(ع) برای تشییع پیکر رهبر شهید  @Farsna - Link</div>
<div class="tg-footer">👁️ 7.37K · <a href="https://t.me/farsna/447971" target="_blank">📅 20:12 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447970">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e687be21dc.mp4?token=j3NIBngAU5S3twxoKGzOTsRMUwiLIvyOPv0B7Ug89jPUf3GmtjY0aLgbd5AdEGayN8v1SdboaPXXGy6wstQZAAl-BGShv8_JpVRg84DqUW_iZts793RsyVMuxPk7kOzzVcCsW_t7ozGmqBx0xz_JVyPMGqW8GuriSavUXMy2l0UvAOkuBLjjNKDeqW9PqTEK42x-InRXKt9HHLEd-_bn9He3BctN356JDIg7xvJNYjVEic_oUkDpqjf9PIpcL4taD1bMe2AzhtvAuQbLLpyi5STrr3wrbln2X5olQOPnF3vkXvW44Jn9bHf2ijuKXj0ACEg2a8xDMPtouUI3BYqz_Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e687be21dc.mp4?token=j3NIBngAU5S3twxoKGzOTsRMUwiLIvyOPv0B7Ug89jPUf3GmtjY0aLgbd5AdEGayN8v1SdboaPXXGy6wstQZAAl-BGShv8_JpVRg84DqUW_iZts793RsyVMuxPk7kOzzVcCsW_t7ozGmqBx0xz_JVyPMGqW8GuriSavUXMy2l0UvAOkuBLjjNKDeqW9PqTEK42x-InRXKt9HHLEd-_bn9He3BctN356JDIg7xvJNYjVEic_oUkDpqjf9PIpcL4taD1bMe2AzhtvAuQbLLpyi5STrr3wrbln2X5olQOPnF3vkXvW44Jn9bHf2ijuKXj0ACEg2a8xDMPtouUI3BYqz_Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
هر قاب، نشانی از یک شهر و یک روایت از انتظار مردم عراق برای رهبر شهید امت اسلام
@Farsna</div>
<div class="tg-footer">👁️ 7.04K · <a href="https://t.me/farsna/447970" target="_blank">📅 20:10 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447965">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/XPCZoOrnMieTqv9c2Bn2SZEqf_dWl4QYnLbFr1hRwdrm0bnlQE_erDW0CGmH2Elr-6u5S38fwTUfSt9opxrydHeIzyqQXRr7lxk2ECVCGitTd8vkR8u3a15wFexTWFoRWzgYI_Ypv15OEnTEnIcQxc9fRQ-RWVfMKE0_TQRaUsdkypJXdpcdtbDhAFoFyn6oMnb9NXxg66_2rbXdTl-QJJIJB32xzM4o-WAkWd0JCZ3I1Yl_Bv5ni78nHsDQpu9Rn6GgzfZ9E3_8f-cAJnT4QONKVQCzAU2h4A6c4DkR3-ONMmgCHI2RJnixCvMqiKZtrNrFA8fBAG_SJkvcfw7Cww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qfk5OWUdFPfOuxuZRlI-Cxe4gZJyWRcuAEsCFzfah1jeP4D34cfuGLjFvI-NG_EUYtbQjFC9It6aDFWh1wyXnZP-KCVX9wLpo2LXgGKSYIvvNgIuYDL_3DQJJbTrJwz9P_JgN7CSWRrTlePZHw2UjJqsjBnZYr1ZOpENURp4GB7qrXJE9mmrYjVaWYUX2xeQ2ZFf-4a5pasvAGDZ8XhLPrblleNAMnr0wXQ8i-_FM0f6lEdcHsTEzPT2qAFPUS91q8X0E4ShPrsm0bJ4loz3cE6HuG07J9fojBvlwEYoglkSp5NF3nM11of6seuwqoK1wGI_qcwX6G-utMmU3YFt-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/MxhnEwSLYITdfyNQMsnEYribmZPtmLMmAU6P3r_vtzfBQpQ26QfatR7O6cK5tUFWaGqKf9QbnJ75CiQCLaQcKclApxmsd4IV-ejd4bQSUbN79f_6FhYm8RSMEtfHDkGEHieov0qDW2s-5yTkopKvqpfVEp69GX6_MZ2RE-ujVivLf7wNUrAcyM1B2vFENC1XXwzIwV7BpZexCpU_hiGyGF6gRfOPOznCZZIzFbiPl6ux_aPGHnthrNwfSq9KOIRVigW1HF6Eh8eGGZxYhcfr6vKB9W3WZPjT4P5WvBBlqpUEYZbcabxV5B6oJvwZwIocyw8hWQamgMcPo5E6CrnyvA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/AbZtULvNl8DZKw89CUkAcWgPjVKZYj9JRGZeJo-3SBwm4CM02yp6uJJkW1_F49K0MN4JVkE8hdvJPuuKelYXkWWH0n-0_OCyFMausLbf4o1QaYNZpGXgnpQ9cSifrAE2yQkYmq0k-0tEIaHgYapEjWsJqaoR6bkWMOSdTDBXHWt6_ZxpqwzO3j3vsPhDrXj33qqrM5NnHpJjyZJ9U9XkKFEWKGfabDjGK-dn_7gMBWcvK_ZWqYE5hEHriYBEo1Ra-n-ELHE30JrdCWU92ijJwbGag1V26fbM42JVtxON3CN6LB-30B1KuQjQRqtAmIRVQHNy3vUhWq-Nz9hZVCN6BA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/adsNI3t2gUCRdA5_9hy6TL4_NpwClglLOqMZKf7sQFtGJFCSZnujTShdgU2rlth_m1W0HxUGGR27AkE0VlXd0mP4wO-OdLamjuR-U9SXcv8iDLmCCOV0xQZCY1M5s-FrkVFA42HPIcRmV4aLIcf3uXhZIdF7msz5DEa6uikIEGMLcJRPISG0ZspW69cLeojhk30XC4os-lo8Npj1Wdx8i-sj37HSihnnMqOy7YldQGymxznRxhMt2Dg7vO0AV9pS34-h7asmDLd5i3hTtmz9GbgFzolLPx7aWdd6vRBt-GZ_jGaVIsfWqlDVjYQYuS0ouZv20SVKsBfAK9Xo2p7Lmg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
پرچم ایران در دستان عراقی‌ها در بین‌الحرمین
@Farsna</div>
<div class="tg-footer">👁️ 7.04K · <a href="https://t.me/farsna/447965" target="_blank">📅 20:09 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447964">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">حادثه برای یک نفتکش در سواحل عمان
🔹
سازمان تجارت دریایی انگلیس اعلام کرد یک نفتکش هنگام عبور از تنگۀ هرمز، در سواحل عمان، هدف پرتابه‌های ناشناس قرار گرفته است. @Farsna</div>
<div class="tg-footer">👁️ 7.03K · <a href="https://t.me/farsna/447964" target="_blank">📅 20:06 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447962">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/273a807c5b.mp4?token=dNwilEr3LqgQEZXkh16C5kXktWoRzdzliD8D22R9sTqUlcP8cZqQcMgf2fLtoPn_v-Ql5e_QBw2zZEvw5t3TlyTjjLogeEi4WwTtRGR3eP2KXrN2fTRpK2gsFXPjpsfIbXw3aHXWyYxUXSfmQlYJEiej8ot8bxyO1_4OKy7aLCGpvMcuA5KBrYNw2fc8r31i7lur8TsjzNh-CfODB11cI4Fpt0foGf9JKjgohPaZFCtSRTrLXhMWza5XpdmtwvFJB2yjwK_KA8F-JLJWsQvCOvqB1J8xnJTP69p6nkPtusOPAiQ8YRfsGcY19o6P-YAibMeQRxWUGQcUHlbPVyKArA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/273a807c5b.mp4?token=dNwilEr3LqgQEZXkh16C5kXktWoRzdzliD8D22R9sTqUlcP8cZqQcMgf2fLtoPn_v-Ql5e_QBw2zZEvw5t3TlyTjjLogeEi4WwTtRGR3eP2KXrN2fTRpK2gsFXPjpsfIbXw3aHXWyYxUXSfmQlYJEiej8ot8bxyO1_4OKy7aLCGpvMcuA5KBrYNw2fc8r31i7lur8TsjzNh-CfODB11cI4Fpt0foGf9JKjgohPaZFCtSRTrLXhMWza5XpdmtwvFJB2yjwK_KA8F-JLJWsQvCOvqB1J8xnJTP69p6nkPtusOPAiQ8YRfsGcY19o6P-YAibMeQRxWUGQcUHlbPVyKArA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
از طلبه‌ای که در نظافت خیابان کمک می‌کرد تا کودکی که با پخش سربند خادم تشییع آقای شهیدش شده بود
@Farsna</div>
<div class="tg-footer">👁️ 7.7K · <a href="https://t.me/farsna/447962" target="_blank">📅 20:02 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447961">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/efadf61825.mp4?token=lJLnRKamqiZQyTnBdvGpM_vCad8DmXx10N-xPzKmYwBLylmyBlDP64JecL05wrVPahApNfMcF0dKcGLvC7aHpC0EzoJDmGsnfGbUk2Ten9wPuMxo-b1wFqfTpZjmXF2zUmmUa0vCRieahySbfBmg1j7LfO1ctJtmEc4hVU0q2mMGJuuQkGNLeRBZLS7Aqho9UOIb4AUAbHZUv-YWMxOzO6oJ1NAdNnzHM8tge_ppOR14zMsV4jnz-ji6-cwSeVbDLJuLCi-4uYp4akDLNSdAOAdV0d-Zboh4LZksQ3qBART_LLebWWzOErKbM0_ijqtWX2wJT1Y_HRVuOWeKHwbMhw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/efadf61825.mp4?token=lJLnRKamqiZQyTnBdvGpM_vCad8DmXx10N-xPzKmYwBLylmyBlDP64JecL05wrVPahApNfMcF0dKcGLvC7aHpC0EzoJDmGsnfGbUk2Ten9wPuMxo-b1wFqfTpZjmXF2zUmmUa0vCRieahySbfBmg1j7LfO1ctJtmEc4hVU0q2mMGJuuQkGNLeRBZLS7Aqho9UOIb4AUAbHZUv-YWMxOzO6oJ1NAdNnzHM8tge_ppOR14zMsV4jnz-ji6-cwSeVbDLJuLCi-4uYp4akDLNSdAOAdV0d-Zboh4LZksQ3qBART_LLebWWzOErKbM0_ijqtWX2wJT1Y_HRVuOWeKHwbMhw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
گل اول مصر به آرژانتین در دقیقۀ ۱۵
⚽️
آرژانتین ۰ - ۱ مصر @Farsna</div>
<div class="tg-footer">👁️ 7.74K · <a href="https://t.me/farsna/447961" target="_blank">📅 19:53 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447960">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8c2759e33f.mp4?token=BnD4b9TknoDZ7oGAT40498y2IA11Fboy4c2pl08uRtPyeUAGtQeOHhYkjGmgSvfGUOMT5Vy_hmhLqx1EbIN_2COezUiZ4i-lRA0Bn1WWdqGVaxjdPdBjn7FzO1uILUNw_S54U-bOX6Tzu_tnzPM6AJyImwJT1CXKVe6d0P5xWtykmDqHBraGQePzgzBOT0axMzFcUBegQLe3RhnGijPYDDzWmtQKDn8LZgsBmzoPsV2fLv7a9LSUOyS8OcaYAT8MQ6EI6BSyL_VT2K5ykgItsoFi1XltaDqDMVBEt1rzZ6d4ue4ILCN5TnSJ6gBrpGoUmFZJdQ0n24GIOT8r-I3W-A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8c2759e33f.mp4?token=BnD4b9TknoDZ7oGAT40498y2IA11Fboy4c2pl08uRtPyeUAGtQeOHhYkjGmgSvfGUOMT5Vy_hmhLqx1EbIN_2COezUiZ4i-lRA0Bn1WWdqGVaxjdPdBjn7FzO1uILUNw_S54U-bOX6Tzu_tnzPM6AJyImwJT1CXKVe6d0P5xWtykmDqHBraGQePzgzBOT0axMzFcUBegQLe3RhnGijPYDDzWmtQKDn8LZgsBmzoPsV2fLv7a9LSUOyS8OcaYAT8MQ6EI6BSyL_VT2K5ykgItsoFi1XltaDqDMVBEt1rzZ6d4ue4ILCN5TnSJ6gBrpGoUmFZJdQ0n24GIOT8r-I3W-A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
گل اول مصر به آرژانتین در دقیقۀ ۱۵
⚽️
آرژانتین ۰ - ۱ مصر
@Farsna</div>
<div class="tg-footer">👁️ 8.45K · <a href="https://t.me/farsna/447960" target="_blank">📅 19:48 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447959">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7c7988fbbe.mp4?token=co6UMCIrcQxE0QYQt3ONCLYTkPuETLl73ySWCvxwqmUsGxmCOiXpvRl_ypM5yMugiw9NWbUr__w0EafIO5M8cf0tAYYtMwnHTYPSwN_F1jqw3DcvVL4mo2zqJlvSqau0yRDkZdDA7b3PCCu1xyjdZJr4CyHH-IqfhHmTs-UZ1iL4GQIwKgMuZjzVFhKXc42ZSCa08t2-2HGSbAHxRj1aSZQvrkipLywhYz0xJ1iu26NG987o37RGjndoNMhYzoG2a3jFh-47d2Tw3xb_8KJv3PlBQ8yrlWcq5upiPMMxfrV1hh_COFfrpQqyjsQWRk1MLwPu-a1SE3VIm-7JEy4bYQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7c7988fbbe.mp4?token=co6UMCIrcQxE0QYQt3ONCLYTkPuETLl73ySWCvxwqmUsGxmCOiXpvRl_ypM5yMugiw9NWbUr__w0EafIO5M8cf0tAYYtMwnHTYPSwN_F1jqw3DcvVL4mo2zqJlvSqau0yRDkZdDA7b3PCCu1xyjdZJr4CyHH-IqfhHmTs-UZ1iL4GQIwKgMuZjzVFhKXc42ZSCa08t2-2HGSbAHxRj1aSZQvrkipLywhYz0xJ1iu26NG987o37RGjndoNMhYzoG2a3jFh-47d2Tw3xb_8KJv3PlBQ8yrlWcq5upiPMMxfrV1hh_COFfrpQqyjsQWRk1MLwPu-a1SE3VIm-7JEy4bYQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
استاندار خراسان‌رضوی: درهای حرم امام رضا(ع) در مدت برگزاری مراسم تشییع و تدفین رهبر شهید باز خواهد بود
🔹
البته رواق‌ها و بخش مرکزی حرم برای مراسم طواف و تدفین بسته خواهد بود. @Farsna</div>
<div class="tg-footer">👁️ 8.37K · <a href="https://t.me/farsna/447959" target="_blank">📅 19:40 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447958">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0f0274261a.mp4?token=E3OXtBPZEhHWVF1LBLsgLjbOJ1WPqV1i0w11lLhJbAotrHhlEP5T4T8dAlT2L9eX2ziMoRVCp6_DAJvGhQuheuJVVgPjZq-nbdxs29_gINH6Wnw0rUHrrBuAv961BBbJuIMMW9h2D6GXfvkPQ_n3e0PlX8OyR5-Fix-WW2jTErY78AxqRUvq9VMo4ypNGojsn0CHtHugNQL8wBSf5ZTHxwRaoCMXh1gcY71NXUQl3ScmOecWEEFFnBpwjriGxiWcIvkhIedaQYCa0P08QV2Z85qo81BQP1QF1H-70fg8dxOLzAtqpuKJ9kVU9e3dsjVp7Soew4I9tnxnuGJauDNWgw0CRZe5PqD2p55cL6JnSV4L9R9EtH3Zo53rBl_gPt_r-r7-lejZtffHJb9cAY698iW1XVI8vsr-iQWvQuM2gK0g0sBEh1t5ldKTQMt46ENO16Z1tD0HMTLdtVPzcyuvRzhN7IxVPaFEDxoBwCCrF44THkLcrjFAH8fkt7Qj9YJz450vfO3vwU4sV1AVuuSofEKGnxxcnnFSWvsxFEx5Z6Z9PmpDqm6BQImdzFHncqiJ0jPA74N_J2yKpzJ3PqfRzzn4RIN5t0dl9_r6BEfLkdisrnxqUpbi-A9raLxz0YTpA_Ld-0uGdxn3NTsgnIGkLG0vaiD582H5qmNZpZ5V9Ow" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0f0274261a.mp4?token=E3OXtBPZEhHWVF1LBLsgLjbOJ1WPqV1i0w11lLhJbAotrHhlEP5T4T8dAlT2L9eX2ziMoRVCp6_DAJvGhQuheuJVVgPjZq-nbdxs29_gINH6Wnw0rUHrrBuAv961BBbJuIMMW9h2D6GXfvkPQ_n3e0PlX8OyR5-Fix-WW2jTErY78AxqRUvq9VMo4ypNGojsn0CHtHugNQL8wBSf5ZTHxwRaoCMXh1gcY71NXUQl3ScmOecWEEFFnBpwjriGxiWcIvkhIedaQYCa0P08QV2Z85qo81BQP1QF1H-70fg8dxOLzAtqpuKJ9kVU9e3dsjVp7Soew4I9tnxnuGJauDNWgw0CRZe5PqD2p55cL6JnSV4L9R9EtH3Zo53rBl_gPt_r-r7-lejZtffHJb9cAY698iW1XVI8vsr-iQWvQuM2gK0g0sBEh1t5ldKTQMt46ENO16Z1tD0HMTLdtVPzcyuvRzhN7IxVPaFEDxoBwCCrF44THkLcrjFAH8fkt7Qj9YJz450vfO3vwU4sV1AVuuSofEKGnxxcnnFSWvsxFEx5Z6Z9PmpDqm6BQImdzFHncqiJ0jPA74N_J2yKpzJ3PqfRzzn4RIN5t0dl9_r6BEfLkdisrnxqUpbi-A9raLxz0YTpA_Ld-0uGdxn3NTsgnIGkLG0vaiD582H5qmNZpZ5V9Ow" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
مردم عراق در تدارک مراسمی باشکوه
🔹
آماده‌سازی‌ها برای استقبال از پیکر رهبر شهید امت اسلام ادامه دارد.
@Farsna</div>
<div class="tg-footer">👁️ 7.41K · <a href="https://t.me/farsna/447958" target="_blank">📅 19:39 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447957">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0736ea3351.mp4?token=MpH9V8m6fh6-A3O1U07OIy4oleUCGqJx3b4cS79dCATCgBqvWYlkDAYY-FbfZ9BJCFAuWszzDIjHuQzqM2P0KHfxUKfoYK6Mf_WU8oBQAewrs1quneqHfvMxj0qys_U5fxV55MWXoiRQ_Al3g7pGZz30yixdFFuLUdlAx2eoy4S4fWCM9qdzSka9JbE3fw2gX6nRg-Ivy7ldnq4UYSkXlcORPAw0E_6Cu37RRoYvrGjzp7gU450Po3dLMHvpify_4ytnJ2OcstPUs6km6-lVf5XuX5l_koIiI7nFYW-yKutq-HUeD13J9Gi6QVr5fJMRaauvXZCg1paGkseQS6pQmw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0736ea3351.mp4?token=MpH9V8m6fh6-A3O1U07OIy4oleUCGqJx3b4cS79dCATCgBqvWYlkDAYY-FbfZ9BJCFAuWszzDIjHuQzqM2P0KHfxUKfoYK6Mf_WU8oBQAewrs1quneqHfvMxj0qys_U5fxV55MWXoiRQ_Al3g7pGZz30yixdFFuLUdlAx2eoy4S4fWCM9qdzSka9JbE3fw2gX6nRg-Ivy7ldnq4UYSkXlcORPAw0E_6Cu37RRoYvrGjzp7gU450Po3dLMHvpify_4ytnJ2OcstPUs6km6-lVf5XuX5l_koIiI7nFYW-yKutq-HUeD13J9Gi6QVr5fJMRaauvXZCg1paGkseQS6pQmw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
استاندار خراسان‌رضوی: حوالی ساعت ۶ صبح پنجشنبه مراسم تشییع رهبر شهید در خیابان امام رضای مشهد آغاز می‌شود
🔹
پیش‌بینی شده که تشییع ۵ تا ۶ ساعت طول بکشد و غروب پنجشنبه هم مراسم تدفین انجام می‌شود. @Farsna</div>
<div class="tg-footer">👁️ 7.02K · <a href="https://t.me/farsna/447957" target="_blank">📅 19:38 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447956">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c63f377383.mp4?token=KXX28f0GAVa-hCXZxSwQCDJJt5XsPC9EFicAyyLfBZGIX-pRiA8twYGa7747taEvo440Yexp4higPmZywSbBgpN7ec5I7Nn6Avpmlcw3mqenN1q9uh4wmn0gkWWLcwezpPJOoOYdkGleldWbuxInFiN5rcmQBQQ7b3E-Bdw0XPK7y6fqAo-ba5Aoy8EjtGMEnHZDUTC-W8-HV8JjH-RBxT9qOEaQ0vDSqDoQEJ-8B_YA4zKyJjTfiqTSXdrEk-Pp4DInlF9ZtfNNVEKTFXatfwiXJhKIUmcqARPBbONehXQT2rnYEaK_FGFQo93BZlVeUx-B5edyBg5cSH9w3miILQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c63f377383.mp4?token=KXX28f0GAVa-hCXZxSwQCDJJt5XsPC9EFicAyyLfBZGIX-pRiA8twYGa7747taEvo440Yexp4higPmZywSbBgpN7ec5I7Nn6Avpmlcw3mqenN1q9uh4wmn0gkWWLcwezpPJOoOYdkGleldWbuxInFiN5rcmQBQQ7b3E-Bdw0XPK7y6fqAo-ba5Aoy8EjtGMEnHZDUTC-W8-HV8JjH-RBxT9qOEaQ0vDSqDoQEJ-8B_YA4zKyJjTfiqTSXdrEk-Pp4DInlF9ZtfNNVEKTFXatfwiXJhKIUmcqARPBbONehXQT2rnYEaK_FGFQo93BZlVeUx-B5edyBg5cSH9w3miILQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
استاندار خراسان‌رضوی: حوالی ساعت ۶ صبح پنجشنبه مراسم تشییع رهبر شهید در خیابان امام رضای مشهد آغاز می‌شود
🔹
پیش‌بینی شده که تشییع ۵ تا ۶ ساعت طول بکشد و غروب پنجشنبه هم مراسم تدفین انجام می‌شود.
@Farsna</div>
<div class="tg-footer">👁️ 6.71K · <a href="https://t.me/farsna/447956" target="_blank">📅 19:35 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447953">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/JYpGxySQJqlvhfazLSqELmY9xuIxYSa_Ghi_nguhYgRZHnZ0HvX3IEVMcXx7OSILaDFdzO9MOgZt2mnuutrEjJNU9PC80hUM9g-x7CnSbUzMC4sxGmi21uC-2oP9TpIlsMarUSYSRBIN-0XVW_ZyLOMBvOby0kC8uqNOblRqMmbxJy3Cu8KzsdqznLP1YdCm2be_VAej4X5uxUt8pIhjg3bBq2yNX-VNvBkXkzCt4IpPQQGpBCeQzLkZu0T5MNfm3xX7SqVWyuZYEmnWk87oDYTi1jWyn8tP34AQWdA7HiQWLyi1cHEh1SpEaswFIU9bYzjvODIZ3B3tqVcXL113ng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/F3uNI1aEKaEMMmd4A3qi-21wUcDQ6qCcaRKV4b8qvF6Iy1UPl4OvXMwBytgvboMxtMvXYKKlVjgCedg_ZcG4iDEApObQOyXXUIyALTwNBLvLJ4rxBJzZQ05Ig8PVrM-T-wEme0hKWv1HtNx_BYcWwQjXtN-8S-JEBKMc94WlDFMd7cFuq5uRD1DCZnG5EROYZx5Olcd5qv_3EnyeH_9ja9ruLhiEKgsjwm1YdXre0HIgAKVoAe6NsfXgeGaD-QZHG6YgkAdzTnY2Ip2eZk4DjY6rPR4B96gK4R7lwmOHPIrpqKEoARSmIiivGVGkeUDNb7Aba2LppoHlYzO3Qde49A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/QUhD21dTS54CpSqgxemD8eNAvOVieoUiblQqbDpYMs6cZPilX_y_6ngRafmU5Ep9rsgniUtWRXBUUBD1M1aCejmoRQtDbUYq0FwDPycyUCFn3ZZ2kwUs4TBqnWQlfcklt6l-tfhbrjHDCjlrjtwNZDZI3oeyxWPKj8ceaErQ3veITuyPJcD9H8E8rA60JBzIV7AFyS5AyowDwydkYLI0tcz4OTIbA62xMma-eq_kHuuIlHVfZc1BlV6AqgTkHJIYukaD7_9DBv2xV_V2tkBJwzV5cVGs1ZJsv4UAQlM8dCu6GkDqKVKIgEgFDwGLVTZ4Y5RtwV0Z3SThVmA0u-_ZCQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">استقرار نیروهای الحشد الشعبی در مسیر فرودگاه نجف اشرف
@FarsNewsInt</div>
<div class="tg-footer">👁️ 6.71K · <a href="https://t.me/farsna/447953" target="_blank">📅 19:34 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447952">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">پزشکیان راهی نجف شد
🔹
رئیس‌جمهور، به‌منظور شرکت در مراسم استقبال از پیکر مطهر رهبر شهید انقلاب، دقایقی پیش تهران را به مقصد نجف اشرف ترک کرد.
@Farsna</div>
<div class="tg-footer">👁️ 6.72K · <a href="https://t.me/farsna/447952" target="_blank">📅 19:32 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447951">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/199cb5464d.mp4?token=RdxOl80Z7B8XBsw5oan_KswUyUPmxDg9axV7W6bFj-63vriyorq8dC7VPAwqakSHsxzJLzn8DithDKgz-kNf6vsBPn3lfitgc-68QQreWyM6tv7AcIx8AMuT1HPMUkMlmYkfffVTCcVRpn4p7CwuncpFR4VGlhACydnyauuuxHoCSX_mXPMuae5YLbGhq_9SBdnzunjnP9OC6QwYgCZrmc1ACP41wZz3QuUQKvbnMY_cHYf1ICPyPOceZtPRVIl-bfxK-TGJHgrIXBbzyJ7FuGEksIxq1YwyJ1X6_iJyEcbWKaIKHHhJXgrD0-vj0Zop8MVWReda-IQL3d_Eprn10GY93DO_rLHY7_uA9UURZhdx6ifBl6DhnQVrGtUgjXat6XUivnFpO4Z2JPxXUXjgVP0i8XtKXYskAnPhm2TL_YR5KshGMyud01MOSOvWb1ClT3rw3c-xuKVcQLANtWZ4a5pidysmTnlg5RW1mhLnffFYtY7FzviEgPGnvvA-KLuUNbPE-L6H-p1wDEKlCFOri3lukGb20Q2cYq3-Ir_S-Ew-rNp0idbRrtjCOQHR3usxOAEekJWgJLwG3YkFOtgRIK1YV2ytM_47sbYHYxKT8rXe-g0W-3sYH6MqM-ajMHZboTczBBjddTXWSQ7rciW_KwP2Djhj8R1jNPJYnvIkGzY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/199cb5464d.mp4?token=RdxOl80Z7B8XBsw5oan_KswUyUPmxDg9axV7W6bFj-63vriyorq8dC7VPAwqakSHsxzJLzn8DithDKgz-kNf6vsBPn3lfitgc-68QQreWyM6tv7AcIx8AMuT1HPMUkMlmYkfffVTCcVRpn4p7CwuncpFR4VGlhACydnyauuuxHoCSX_mXPMuae5YLbGhq_9SBdnzunjnP9OC6QwYgCZrmc1ACP41wZz3QuUQKvbnMY_cHYf1ICPyPOceZtPRVIl-bfxK-TGJHgrIXBbzyJ7FuGEksIxq1YwyJ1X6_iJyEcbWKaIKHHhJXgrD0-vj0Zop8MVWReda-IQL3d_Eprn10GY93DO_rLHY7_uA9UURZhdx6ifBl6DhnQVrGtUgjXat6XUivnFpO4Z2JPxXUXjgVP0i8XtKXYskAnPhm2TL_YR5KshGMyud01MOSOvWb1ClT3rw3c-xuKVcQLANtWZ4a5pidysmTnlg5RW1mhLnffFYtY7FzviEgPGnvvA-KLuUNbPE-L6H-p1wDEKlCFOri3lukGb20Q2cYq3-Ir_S-Ew-rNp0idbRrtjCOQHR3usxOAEekJWgJLwG3YkFOtgRIK1YV2ytM_47sbYHYxKT8rXe-g0W-3sYH6MqM-ajMHZboTczBBjddTXWSQ7rciW_KwP2Djhj8R1jNPJYnvIkGzY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
معاون اجرایی رئیس‌جمهور: رهبر شهید، جمهوری اسلامی را به گونه‌ای ساخت که در برابر تمام قدرت‌های جهان ایستاد.
@Farsna</div>
<div class="tg-footer">👁️ 7.31K · <a href="https://t.me/farsna/447951" target="_blank">📅 19:28 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447950">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">🎥
جزئیات مراسم تشییع رهبر شهید در نجف از زبان سرکنسول ایران در کربلا
@Farsna</div>
<div class="tg-footer">👁️ 8.42K · <a href="https://t.me/farsna/447950" target="_blank">📅 18:59 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447949">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">هواشناسی با صدور هشدار نارنجی، از احتمال وقوع طوفان و گردوخاک شدید تا پنجشنبه در استان تهران خبر داد.
@Farsna</div>
<div class="tg-footer">👁️ 9.1K · <a href="https://t.me/farsna/447949" target="_blank">📅 18:51 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447948">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/588ed1bb1e.mp4?token=Rro29_c0NbWfrW-1q5DYdlx1y87JFT6uUiTQSqOaUJVWSXb1d9QQFoYCCNbEDqvuNNtGV0s4Wr-iZMVZBlsX_v4teLbaZ7P5Xs9p74f7PZSiKdAkb8M-aR_k0RgElsz26_cg9XXMa0HC68dV0qzyQJDTMWtc8XDZoZw3NhWbYaWhN6Z3JUqzq1fQGjtMZVnbcN0cxUvA25FS2G_-OkCkW7nIz4MMCpOTV_ZU6qMogRV1vD1n9XD459NLJpzR6s7egjKEr-UOu342P95kdkFLCnqlrDcSZaka3n9gG_O4H9ZMnIGA18Brpq84oMVXFGEw3sAzdwoPUT2AuPzO7vMMdQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/588ed1bb1e.mp4?token=Rro29_c0NbWfrW-1q5DYdlx1y87JFT6uUiTQSqOaUJVWSXb1d9QQFoYCCNbEDqvuNNtGV0s4Wr-iZMVZBlsX_v4teLbaZ7P5Xs9p74f7PZSiKdAkb8M-aR_k0RgElsz26_cg9XXMa0HC68dV0qzyQJDTMWtc8XDZoZw3NhWbYaWhN6Z3JUqzq1fQGjtMZVnbcN0cxUvA25FS2G_-OkCkW7nIz4MMCpOTV_ZU6qMogRV1vD1n9XD459NLJpzR6s7egjKEr-UOu342P95kdkFLCnqlrDcSZaka3n9gG_O4H9ZMnIGA18Brpq84oMVXFGEw3sAzdwoPUT2AuPzO7vMMdQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
کهنسال عراقی: با شهادت سید علی خامنه‌ای من ۳ شبانه‌روز نه سحری خوردم و نه افطار.
@Farsna</div>
<div class="tg-footer">👁️ 9.31K · <a href="https://t.me/farsna/447948" target="_blank">📅 18:45 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447947">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">حرم رضوی مهیای میزبانی از زائران و عزاداران تشییع و تدفین رهبر شهید
🔹
قائم‌مقام تولیت آستان قدس رضوی: محدودسازی تردد صرفاً در صحن‌های مرکزی حرم رضوی از ظهر روز قبل از مراسم آغاز می‌شود و تا پایان مراسم تدفین ادامه خواهد داشت.
🔹
تردد در صحن‌های پیرامونی تا زمانی که شرایط ایمنی و مدیریت جمعیت اجازه دهد، برقرار خواهد بود.
🔹
در تلاش هستیم که شرایطی فراهم شود تا حتی زائرانی که امکان حضور در صحن انقلاب را ندارند، بتوانند در نماز مشارکت داشته باشند.
@Farsna</div>
<div class="tg-footer">👁️ 8.31K · <a href="https://t.me/farsna/447947" target="_blank">📅 18:40 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447946">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d824fcad1c.mp4?token=apZR_N_xlkQdCD6kPcDNxTaSsDhfacFRndh5wmrOKvcX8n8VVZRBwHY7g_jMHh-V-Lb2XnUTf7QGPnM8GeLfTlWB-8B_Dt_yXt8P3J3URJvHv_emNIuOJcP2ZCouBhnjgz1ULeCHg1IQ2V0t4BoQriryrcz_CGEUMO-Ixcb_u3SgbnI93LjcE_C2hXYPQcgykBddZ6CmSIbBD5j0jY0qxpoXuLLvSeWbs5_uTcCCUmGYEL_N3P3S73KATNi34V86Jsn3Qj-INo7n_gUgz_0BkjGknHdcdpaenmz5A0zfyLaMTpOn70J9-uozYX4z5Qji8mIsCFhs_eEjIv20jDO2pg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d824fcad1c.mp4?token=apZR_N_xlkQdCD6kPcDNxTaSsDhfacFRndh5wmrOKvcX8n8VVZRBwHY7g_jMHh-V-Lb2XnUTf7QGPnM8GeLfTlWB-8B_Dt_yXt8P3J3URJvHv_emNIuOJcP2ZCouBhnjgz1ULeCHg1IQ2V0t4BoQriryrcz_CGEUMO-Ixcb_u3SgbnI93LjcE_C2hXYPQcgykBddZ6CmSIbBD5j0jY0qxpoXuLLvSeWbs5_uTcCCUmGYEL_N3P3S73KATNi34V86Jsn3Qj-INo7n_gUgz_0BkjGknHdcdpaenmz5A0zfyLaMTpOn70J9-uozYX4z5Qji8mIsCFhs_eEjIv20jDO2pg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
عهد و پیمان اهالی عراق با آقای شهید
@Farsna</div>
<div class="tg-footer">👁️ 8.28K · <a href="https://t.me/farsna/447946" target="_blank">📅 18:40 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447945">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CxInX5H4YsqSRd1Kt1FCz2tRgYXq1eoX_IyjPzmlPbHDup-c6HjCD5d0sPkuOIWXhaoUXC0onfZ5OwkI79DL6fEUmtSVRYkmaymBbzG8Nsw9oYw4Bz6boLWU-ck8jZ0vIHqIVByGj01xKXrMdO90TtkqBDablH31vKgVSIiXtx9KQTRVzJDnoCcpjDJviuwYSLou23lzIXmLOMgwCpDxDPIeSXNwBtQ0ofsKOPSTwqizh71SvwuCAX4bWcI65jO547kBVeDn6FeHHY3bjZeXJxuKEO5Iam-vHJZ3BMoRPZcsWrX6PlCD6IcdxsUqpb4x7qbCj65u50p5w8WUHPC2aw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سخنگوی وزارت دفاع: ایران در برابر هر تجاوزی پاسخ قاطع و متناسب خواهد داد
🔹
سردار طلایی‌نیک: دشمن تصور می‌کرد با ترور رهبر انقلاب، فرماندهان نظامی، دانشمندان و حمله به مراکز مسکونی، می‌تواند نظام جمهوری اسلامی را دچار فروپاشی کند، اما نتیجه کاملاً برعکس شد و انسجام ملی، حمایت مردمی و اقتدار نظام بیش از گذشته تقویت شد.
🔹
جمهوری اسلامی ایران مسیر دیپلماسی را با اقتدار دنبال می‌کند، اما در برابر هرگونه تجاوز یا عبور از خطوط قرمز، پاسخ قاطع، مؤثر و متناسب خواهد داد و تجربه‌های گذشته نیز این واقعیت را برای دشمنان اثبات کرده است.
🔹
امروز جمهوری اسلامی ایران با اتکا به مردم، توان داخلی، تجربه‌های ارزشمند دفاعی و هدایت‌های رهبر معظم انقلاب اسلامی، حضرت آیت‌الله سیدمجتبی حسینی خامنه‌ای، مسیر تقویت قدرت ملی، توسعه بازدارندگی و حفظ امنیت پایدار را با قدرت ادامه خواهد داد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.03K · <a href="https://t.me/farsna/447945" target="_blank">📅 18:29 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447944">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/22dd375f85.mp4?token=CkS_T_0CnYQwOwISVZltpNV_kWRBz3wSTrInOrq7OsVpAmskFTirf-DvEI4Wr4TWhPwYFPq2MHlin_SpHjVweOZmfoMgLM0gs2DIOy--s4GEg4CdI8kc6aBdHcFVThgTCaRyJQ0hOFLsr59ZyW5SI2H-9caTjGmjwgdkYLYwXp3jqhn0wNRfzwwUQ2fs78GY5TAHnDx6kfpKYw1YH89MEGVWLd8toLfa9Ea84CDook_nZPtTGK5oAm8zvQeOR-qP1ZqeDH55jZvOpROjdmVIO-O1L3kaJUlkCSL8ajAKBkMhMZpMcQapZKQwaPk4wvdVSS1twdIL4ny8c35dDJA74g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/22dd375f85.mp4?token=CkS_T_0CnYQwOwISVZltpNV_kWRBz3wSTrInOrq7OsVpAmskFTirf-DvEI4Wr4TWhPwYFPq2MHlin_SpHjVweOZmfoMgLM0gs2DIOy--s4GEg4CdI8kc6aBdHcFVThgTCaRyJQ0hOFLsr59ZyW5SI2H-9caTjGmjwgdkYLYwXp3jqhn0wNRfzwwUQ2fs78GY5TAHnDx6kfpKYw1YH89MEGVWLd8toLfa9Ea84CDook_nZPtTGK5oAm8zvQeOR-qP1ZqeDH55jZvOpROjdmVIO-O1L3kaJUlkCSL8ajAKBkMhMZpMcQapZKQwaPk4wvdVSS1twdIL4ny8c35dDJA74g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
خودنمایی پرچم ایران و عراق در خیابان‌های عراق در استقبال از تشییع رهبر شهید
@Farsna</div>
<div class="tg-footer">👁️ 7.96K · <a href="https://t.me/farsna/447944" target="_blank">📅 18:26 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447943">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9f7789ff06.mp4?token=S-0xAAnWaBJ3iFtDeeTob6IrtpI4WJkL5OumqPSiCkn97wNVXrfnUGBUn09NZD78DtTYImNdPxLl3hPsTMMRGqZLOKhp4x23JQlQGipTzdjU4B18Bjg85oKr-RfjZAIYJxZti6MlO_w6bEPzMMLEzYWSZaycRW-3gyt9cxi1yeB8pGoao3rwAXl-RZwWFov_hGdUjYkLNmyYuLtDhiW4Ti00Ozu5WSSVRzFDyhnQanqgZJKVgzMrIC5NWU5t08zD5lDBFygf0jLscHE4RzuRhTJi9a54JQf8lu8s04RxrA5HIZa1h8fM2v2WdtNJtXWs7LjLyRrKy6erVlzJ87rROA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9f7789ff06.mp4?token=S-0xAAnWaBJ3iFtDeeTob6IrtpI4WJkL5OumqPSiCkn97wNVXrfnUGBUn09NZD78DtTYImNdPxLl3hPsTMMRGqZLOKhp4x23JQlQGipTzdjU4B18Bjg85oKr-RfjZAIYJxZti6MlO_w6bEPzMMLEzYWSZaycRW-3gyt9cxi1yeB8pGoao3rwAXl-RZwWFov_hGdUjYkLNmyYuLtDhiW4Ti00Ozu5WSSVRzFDyhnQanqgZJKVgzMrIC5NWU5t08zD5lDBFygf0jLscHE4RzuRhTJi9a54JQf8lu8s04RxrA5HIZa1h8fM2v2WdtNJtXWs7LjLyRrKy6erVlzJ87rROA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
فرزندی که مهمان‌ خانهٔ پدر شد
🔸
روایتی از پیوند عاطفی عمیق مردم عراق با قائد شهید امت
@Farsna</div>
<div class="tg-footer">👁️ 7.81K · <a href="https://t.me/farsna/447943" target="_blank">📅 18:25 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447942">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/476d11a9c0.mp4?token=fJjUKuthmEVQSknqJXEE1-D2MzLqtgIaj_derbHbnk_HhcbDk9JGl_9UxENM0FLlKAEXVHFmaHkNpWYj2l_TN6kUcwyRaDokF1DPp-nHTFqRaTSFtTh_IJ1usGiatEPUa2dF8k9Y7afKLUiQUWk_K9rKZoNr2WMTOp3zOZDXwN5DKPYxrxfsjL65FGtaxLxzHbg2fubqtjaFDh_S2imw0k_xBvT_LcOWy7wDiC-O-P76BJK4Te4SuzX5ECnT5OZtIpuD0uQrGNntm9Pg4Ghs-wd4c0pLnpF48W5l8G8Ys7fXbqV17knOS0geNdv_ckpmwC9YRdDEkipPopJtYX_66Yi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/476d11a9c0.mp4?token=fJjUKuthmEVQSknqJXEE1-D2MzLqtgIaj_derbHbnk_HhcbDk9JGl_9UxENM0FLlKAEXVHFmaHkNpWYj2l_TN6kUcwyRaDokF1DPp-nHTFqRaTSFtTh_IJ1usGiatEPUa2dF8k9Y7afKLUiQUWk_K9rKZoNr2WMTOp3zOZDXwN5DKPYxrxfsjL65FGtaxLxzHbg2fubqtjaFDh_S2imw0k_xBvT_LcOWy7wDiC-O-P76BJK4Te4SuzX5ECnT5OZtIpuD0uQrGNntm9Pg4Ghs-wd4c0pLnpF48W5l8G8Ys7fXbqV17knOS0geNdv_ckpmwC9YRdDEkipPopJtYX_66Yi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📷
نشست رسانه‌ای مهمانان خارجی تشییع رهبر شهید  عکس: زینب حمزه‌لویی @Farsna</div>
<div class="tg-footer">👁️ 8.9K · <a href="https://t.me/farsna/447942" target="_blank">📅 18:18 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447941">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/305328c444.mp4?token=CmiRN1_BoUmi-JoNvzMMfHK9eZqYgelqdMkMay00wRvDfxk3qtnkboRgpUW_M_kAHHKqDcj05eY0ZIPzF5H5nceevZVWP2XPB5uBoU8bHx0TQ6r2Coko_nznTKbo7QtPNHyKDmUKCJad_DbsU4PYNQDxsZkQbKcxCRQkusHk41vYx9IGZ7m9dtal01fs2wlJHLgEi4Ba2Ad6IlZjCFY9juyi--3UEKJIv886eRQxfVArrg_8j1oLzCapBvunjBTr8LdSkVGnIPuVBej1maeF0w1Rkos05ivZPcqgSqEzJMs8hUT9RjqDcHTQ6IqYT60cWP5K9S_HqE_qSQOwPiwnzg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/305328c444.mp4?token=CmiRN1_BoUmi-JoNvzMMfHK9eZqYgelqdMkMay00wRvDfxk3qtnkboRgpUW_M_kAHHKqDcj05eY0ZIPzF5H5nceevZVWP2XPB5uBoU8bHx0TQ6r2Coko_nznTKbo7QtPNHyKDmUKCJad_DbsU4PYNQDxsZkQbKcxCRQkusHk41vYx9IGZ7m9dtal01fs2wlJHLgEi4Ba2Ad6IlZjCFY9juyi--3UEKJIv886eRQxfVArrg_8j1oLzCapBvunjBTr8LdSkVGnIPuVBej1maeF0w1Rkos05ivZPcqgSqEzJMs8hUT9RjqDcHTQ6IqYT60cWP5K9S_HqE_qSQOwPiwnzg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
تصویری دیده‌نشده از رهبر شهید؛ آخرین هدیهٔ مردم تهران، به آقای شهید…
🔸
در آستانهٔ تشییع رهبر شهید، مردم آخرین هدیه‌شان را با دست‌های خود ساختند. هر کس بومی را رنگ کرد و از پیوند آن‌ها روی دیوار شهر، تصویری خاص و دیده‌نشده از رهبر شهید خلق شد؛ یادگاریِ ماندگاری که تار و پودش از عشق و مشارکت مردم بود.
@Farsna</div>
<div class="tg-footer">👁️ 7.93K · <a href="https://t.me/farsna/447941" target="_blank">📅 18:13 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447940">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f49b6b30c1.mp4?token=OvaRxV6lCVyCDgnZMa4ZZq0HYoMT9StaNt1OQ6FXGgOR-dIjvFffpJgloFb7lk5AdMAYt1_ppBGBvsrIFU8cNxeRK72QhCs5U2gouF1bWUz3Px3FVzS86d8pNVHGhrjLlpBlDyXGuGHRoKihWah3pLbQrXwykqTvLvrnRUigNnWJ1PHlnOMtM1D9nsibW-LVgMfX9PL685iPnmqpZFNaSSd2u21VGmdFyUFfkMz462P88794UVLBmc1KFlwaEnU_KQnw-rwYTVc6-6LT6ue9nDO4-atU-stHE5rg9y00ymj8jPUz5i4dxbB5GPiyRZ6fFSLX4q_top5bo1FsIfMoug" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f49b6b30c1.mp4?token=OvaRxV6lCVyCDgnZMa4ZZq0HYoMT9StaNt1OQ6FXGgOR-dIjvFffpJgloFb7lk5AdMAYt1_ppBGBvsrIFU8cNxeRK72QhCs5U2gouF1bWUz3Px3FVzS86d8pNVHGhrjLlpBlDyXGuGHRoKihWah3pLbQrXwykqTvLvrnRUigNnWJ1PHlnOMtM1D9nsibW-LVgMfX9PL685iPnmqpZFNaSSd2u21VGmdFyUFfkMz462P88794UVLBmc1KFlwaEnU_KQnw-rwYTVc6-6LT6ue9nDO4-atU-stHE5rg9y00ymj8jPUz5i4dxbB5GPiyRZ6fFSLX4q_top5bo1FsIfMoug" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
ترامپ: من از ناتو خیلی ناامید شده‌ام، ناتو [در رابطه با ایران] با ما رفتار خوبی نداشت
🔹
اگر نشست ناتو در ترکیه برگزار نمی‌شد احتمال داشت که اصلاً در آن شرکت نکنم.
🔹
قبل از اینکه اصلاً از ناتو درخواستی کنم، آن‌ها گفتند که برای مقابله با ایران پشت ما نخواهند…</div>
<div class="tg-footer">👁️ 8.27K · <a href="https://t.me/farsna/447940" target="_blank">📅 18:10 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447939">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/abc858c595.mp4?token=PcfEtSOTYNHuArRae_7eOfn65hvcIMr-8BczCUf20q1H3wP47xir0p5lSheZChbKEs_RLdmQ1BB_9JOSdECK0VUkBsLB7B4tyGjcZpbm2o_9jf5E211I7_hPXTwSNhcVXngYlDIC0u-hUSYt7GT5oMJajZbSZ3O7bWdTsbBpOLA4RPHkNpxO02eSxVhE0xrGm7l8Yih0baxwOZEXl4x9bi_7CPcMUmJC2WyPm7AmJVM0kMfHzlgQ6w-56wqVGTyNcaXb21n2Cw7qYpnTygy4NGu9hb3b7h1syEATGd-VAxyuz41eom4vYxgSMhA0HzquL0jdLlHjuC0taNn3UzVJMg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/abc858c595.mp4?token=PcfEtSOTYNHuArRae_7eOfn65hvcIMr-8BczCUf20q1H3wP47xir0p5lSheZChbKEs_RLdmQ1BB_9JOSdECK0VUkBsLB7B4tyGjcZpbm2o_9jf5E211I7_hPXTwSNhcVXngYlDIC0u-hUSYt7GT5oMJajZbSZ3O7bWdTsbBpOLA4RPHkNpxO02eSxVhE0xrGm7l8Yih0baxwOZEXl4x9bi_7CPcMUmJC2WyPm7AmJVM0kMfHzlgQ6w-56wqVGTyNcaXb21n2Cw7qYpnTygy4NGu9hb3b7h1syEATGd-VAxyuz41eom4vYxgSMhA0HzquL0jdLlHjuC0taNn3UzVJMg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
چشم عراق روشن؛ گفت‌وگوی بی‌پرده با مردم عراق که چشم‌انتظار بزرگ‌ترین رویداد تاریخ عراق هستند
🔸
به زودی مراسم تشییع پیکر رهبر شهید انقلاب در عراق برگزار می‌شود.
@Farsna</div>
<div class="tg-footer">👁️ 7.95K · <a href="https://t.me/farsna/447939" target="_blank">📅 18:10 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447938">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/667eab7dcb.mp4?token=DBv4TDjYNRIHJB0Uvw08AukFjB73zo9k0AwPn0F2RfyBAfN54pEhoqTSoT67CF-c3-gYnAy4HBEVuakVqP4EFZwiWNU9whNVDx0RBHwp0wCl-4ftjWu84VCQ14nOGtFR2GZ8I7bsEedpUNMaTfLMsYxO6NPFy-dFGoLsC9ok_5Kv44zs6hJ3tt1AP1zlcSAMDF5yhgULq_lgjozUcC1VTSDJ0vpp1jGQV2cBwPWotP83tuyDrDUmcR5NK26LMz2ZbGJSBmjDOYhbtDg9w4Gs5igejCEEu215tldRfoF3IwAE9yu42pGHv5J4BTqvVwYhAjBfMiat8d08JHvByQHaiA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/667eab7dcb.mp4?token=DBv4TDjYNRIHJB0Uvw08AukFjB73zo9k0AwPn0F2RfyBAfN54pEhoqTSoT67CF-c3-gYnAy4HBEVuakVqP4EFZwiWNU9whNVDx0RBHwp0wCl-4ftjWu84VCQ14nOGtFR2GZ8I7bsEedpUNMaTfLMsYxO6NPFy-dFGoLsC9ok_5Kv44zs6hJ3tt1AP1zlcSAMDF5yhgULq_lgjozUcC1VTSDJ0vpp1jGQV2cBwPWotP83tuyDrDUmcR5NK26LMz2ZbGJSBmjDOYhbtDg9w4Gs5igejCEEu215tldRfoF3IwAE9yu42pGHv5J4BTqvVwYhAjBfMiat8d08JHvByQHaiA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
لقب حضرت آقا تا همیشه همین می‌ماند
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.06K · <a href="https://t.me/farsna/447938" target="_blank">📅 18:04 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447937">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DCndxyiB_J3PeioNON0w5oTOOBy6Gda7G9PjqgJf3acDci1xfl5DGbTjVyHKVq6qGFpXf8DL2QHO5t04bpIztBqXztfsf1dCFmGoFHasGpuIWmdeLV_MXja1TyezvFoz19lIrcE20UeOzK_q7Cg8b8ntZDQIfKDT7ZXrreFxULc15ZfINIg8cucgvTIpMdpwgjjt6N10FK-anMI6IOGd9Owjb9mnVf1JTslUXv3NxxUg_IGwDGH1ma9T8Y-V2JF8TP8VAQ1UGfyKLS_pJ3SrLuiSJl35cGnMlhwgzoZXliP9SUSoFuZEaPhDs4alFd4J2cOemVUVaomaFYgrkoR5Sw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چه کسی گفته حساب بازاری‌ها از رهبر و انقلاب جداست؟
🔹
کرکره آن‌قدر بالا نیست که بشود راحت چشم انداخت و داخل مغازه را دید، اما در میانهٔ در و کمی پایین‌تر از انتهای کرکره، دو چشم تیله‌ای زل‌زده به آدم‌های بیرون؛ لباس سیاه تن کرده و در دستش پرچمی دارد دوبرابر قد خودش.
🔹
دنبال پدر از این‌ور به آن‌ور می‌رود. پدری که عحیب متعهد  است. «حتی در روزهای جنگ که همه بستند و رفتند؛ ما در قلب شهر ماندیم و هیچ‌وقت خیابان را خالی نکردیم. اصلاً چه کسی گفته...»
🔗
دو کلام حرف‌ حساب کاسبی از کاسب‌های شهر را
اینجا
را بخوانید.
@Farsna</div>
<div class="tg-footer">👁️ 8.22K · <a href="https://t.me/farsna/447937" target="_blank">📅 17:55 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447936">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4413e158b8.mp4?token=nh2ANI9AvFQojGUO7QwRbee9ttBmfEjTMgtTVUUbCzMt4CaRu9YCuCJe9ys-GWwjEUExBJ0LqT1DI8PZriQB5iCoal4YAPNdiZh60daGCi7nBQctx2iTtWXdBiND8WKnhmsW6ZgA1dvpKW7smiPlYHpqS7VIt0HqTwduLHdVR9Qt3YJ3ELK7kaJE5pm5XjA2vZxVwsCxBk1RDLUyjWoWIIBKuigEzh08I2SJd7N0GN-ORyFIcdp-JIM8jhtmfDePZ-0Bg6UA7y1AJcYAZo8UmMsHVuGHxQhg738j6_J4rwCfqTvsVshaoX-1ogyXdBW9J3UDDpsCOV9aFAEN3pmoYw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4413e158b8.mp4?token=nh2ANI9AvFQojGUO7QwRbee9ttBmfEjTMgtTVUUbCzMt4CaRu9YCuCJe9ys-GWwjEUExBJ0LqT1DI8PZriQB5iCoal4YAPNdiZh60daGCi7nBQctx2iTtWXdBiND8WKnhmsW6ZgA1dvpKW7smiPlYHpqS7VIt0HqTwduLHdVR9Qt3YJ3ELK7kaJE5pm5XjA2vZxVwsCxBk1RDLUyjWoWIIBKuigEzh08I2SJd7N0GN-ORyFIcdp-JIM8jhtmfDePZ-0Bg6UA7y1AJcYAZo8UmMsHVuGHxQhg738j6_J4rwCfqTvsVshaoX-1ogyXdBW9J3UDDpsCOV9aFAEN3pmoYw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
تصاویری از دلتنگی ایرانیان ساکن عراق برای آقای شهید ایران
🔸
آن‌ها در انتظار تشییع پیکر رهبر شهید در عراق هستند
@Farsna</div>
<div class="tg-footer">👁️ 7.72K · <a href="https://t.me/farsna/447936" target="_blank">📅 17:55 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447935">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">ایلام چهارشنبه تعطیل شد
🔹
استانداری ایلام: تمام دستگاه‌های اجرایی، بانک‌ها، دانشگاه‌ها، مراکز آموزشی و سایر ادارات دولتی استان روز چهارشنبه ۱۷ تیرماه تعطیل است.
🔹
این تصمیم با هدف تسهیل حضور مردم در آیین وداع با پیکر مطهر رهبر شهید انقلاب در کربلا و با توجه به افزایش تردد در جاده‌های ایلام گرفته شده است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.98K · <a href="https://t.me/farsna/447935" target="_blank">📅 17:53 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447934">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b353fba9ba.mp4?token=pKImUad7etThdhRylVeVzrT7kUrr9pBDd9pHqkTXMCZ_eGzfvuQIiqPbOmuJBwI1VEmD5rjmlKvesbfIM9sbacgYE2OLA0hRoW45J-nhF3qFaf0k6G42SmjrTODH5CQO7RFhN7conYYEqdE8Cx6cYZxbPQFTcRqgKGo5WMceH8kfHjJeJ_-bnYluRmeK29SETxdwvmDXBi5EC7lmKrV-o9oGbeZhr-c6a1aKfzpiNCBcIzU493W6gvtEJmzRzBAaP0-LbGieMPyBFWv5DIFQ2GOfy1ReW_QK-PU0T8Ce5SkkB7gYdkWhy9NF3LDQjLU7ymRCjbKemEVDd3ApMRldfA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b353fba9ba.mp4?token=pKImUad7etThdhRylVeVzrT7kUrr9pBDd9pHqkTXMCZ_eGzfvuQIiqPbOmuJBwI1VEmD5rjmlKvesbfIM9sbacgYE2OLA0hRoW45J-nhF3qFaf0k6G42SmjrTODH5CQO7RFhN7conYYEqdE8Cx6cYZxbPQFTcRqgKGo5WMceH8kfHjJeJ_-bnYluRmeK29SETxdwvmDXBi5EC7lmKrV-o9oGbeZhr-c6a1aKfzpiNCBcIzU493W6gvtEJmzRzBAaP0-LbGieMPyBFWv5DIFQ2GOfy1ReW_QK-PU0T8Ce5SkkB7gYdkWhy9NF3LDQjLU7ymRCjbKemEVDd3ApMRldfA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
تنبیه متقلب‌ها در مستطیل سبز!
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.66K · <a href="https://t.me/farsna/447934" target="_blank">📅 17:43 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447933">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WO7llEq4hjx4Ma2JhUps6GXPTF40CcpCjs6daxu8fhnxgy-UpCfRxkXaj7rahoFZdTC1dw8edDOOcLrXF6fU-wxxl5H8X0scX6fXptF-v-06TjxG2TrwqihMxFknD_LvtEoqa-PJU34Klmd5m0VsyQIsO2do3yPc1vD4ugLmfayaR6U-8TvEc5578zhEnTTfbhLFdFO63SyXUc-WvE8OgJs6ql_qVBDTVfVoJmJzwqTkoFke6OFb2xgkYmuW2JHqDEuh2IaRoRZ0NM78SFC9ZLZnbUp4we3hhGLrOqNxTTlZdVBTeOJiJEnWiYg-C74JSRzRTkCbfTrA0RuS_M7Rhw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آرزویی که دختر عکاس را از بندرعباس به قم کشاند
🔹
در میان همهمهٔ خانهٔ میزبان، گوشه‌ای نشسته و دوربینش را محکم در آغوش گرفته؛ هنوز سؤال اول را نپرسیده‌، اشک روی گونه‌هایش سرازیر می‌شود.
🔹
آرزویی دارد که به‌خاطر آن دست خانواده‌اش را گرفته و از بندرعباس راهی قم شده؛ سفری طولانی فقط برای اینکه شاید بتواند.‌‌..
🔗
ماجرای سفر این دختر عکاس برای برآورده‌شدن آرزویش را
اینجا
بخوانید.
@Farsna</div>
<div class="tg-footer">👁️ 8.89K · <a href="https://t.me/farsna/447933" target="_blank">📅 17:36 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447932">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/df726c7c93.mp4?token=U29vokrpj80h_JB8v05hDNzdCltyGXQLtHOb174MdaOEskmcHx0qh50ZJkwkXXeYBHCYOxBUoJy6Wr8x1aTv2-U__v1yub7ynJfYDzUAFyUXf9xlt3JfaeZNgnBh1HE0_gKERPBCT1bM7kXiJkHIthITQJTYfUSTmU2j5B5qAhtTl2Ms6wYbo-Q1_W2zldhoBXwQXkwTbzXFnvRu2-6V2ed-4yfGbrjptQbnFP0-Z0TPkJxGREvIZv7n9p_J9C3shbuUSv68mzYaudDYvTNZcGrry1C9ef3JH_3NZvV6NO8wSIbl4jARsC4_vJQ4w2bqUE7f2ZX1vd8hYqJQ4WVOgA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/df726c7c93.mp4?token=U29vokrpj80h_JB8v05hDNzdCltyGXQLtHOb174MdaOEskmcHx0qh50ZJkwkXXeYBHCYOxBUoJy6Wr8x1aTv2-U__v1yub7ynJfYDzUAFyUXf9xlt3JfaeZNgnBh1HE0_gKERPBCT1bM7kXiJkHIthITQJTYfUSTmU2j5B5qAhtTl2Ms6wYbo-Q1_W2zldhoBXwQXkwTbzXFnvRu2-6V2ed-4yfGbrjptQbnFP0-Z0TPkJxGREvIZv7n9p_J9C3shbuUSv68mzYaudDYvTNZcGrry1C9ef3JH_3NZvV6NO8wSIbl4jARsC4_vJQ4w2bqUE7f2ZX1vd8hYqJQ4WVOgA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
تلاش بی‌وقفهٔ جوانان عشایر عراقی در دل شب برای استقبال هرچه باشکوه‌تر از رهبر شهید امت
@Farsna</div>
<div class="tg-footer">👁️ 8.65K · <a href="https://t.me/farsna/447932" target="_blank">📅 17:33 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447931">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ba9e6e1784.mp4?token=KQvd5S-ap9xlLeLKQcSzLTcrgMqdHDvruPQ68A78L-8KxcmH1kzqR2YZKEuLxhELoAvjn3LqbnCtaXVjtMOrzSLqFSLDrJp4o7060FBtn-MR5aV4aI7fBc5DMA-pyQWcEBwphpvXwLpEtLRJb8kgO-3oEhFZ_ZAri5Wh6hANhTBgrlbzQ8DMFuYF1orL3kRppqded-0oW_wYeyjOJeULGyKdS6Hf1wUmYbG-W-uQSSAVULRD3dItrofkgq7UrKXNjcdNi07rbMFsIOnCQtyC4464iZPllFfuNst4jydpIzgRM4aQYzd9H11TjiSEB62CTR_RYlHxwJLFE4QcRN-bKw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ba9e6e1784.mp4?token=KQvd5S-ap9xlLeLKQcSzLTcrgMqdHDvruPQ68A78L-8KxcmH1kzqR2YZKEuLxhELoAvjn3LqbnCtaXVjtMOrzSLqFSLDrJp4o7060FBtn-MR5aV4aI7fBc5DMA-pyQWcEBwphpvXwLpEtLRJb8kgO-3oEhFZ_ZAri5Wh6hANhTBgrlbzQ8DMFuYF1orL3kRppqded-0oW_wYeyjOJeULGyKdS6Hf1wUmYbG-W-uQSSAVULRD3dItrofkgq7UrKXNjcdNi07rbMFsIOnCQtyC4464iZPllFfuNst4jydpIzgRM4aQYzd9H11TjiSEB62CTR_RYlHxwJLFE4QcRN-bKw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
آماده‌سازی ورودی حرم امام حسین(ع) برای تشییع پیکر رهبر شهید
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.82K · <a href="https://t.me/farsna/447931" target="_blank">📅 17:21 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447930">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ce8c696d52.mp4?token=PG3mfnXUzpusrE4cg3PayepEqtIhLTMIoOTQ5xTrv_8mObOVZtgcKeDTUwZozaDEdXJT9BkaqapAoXGzVo50Bch2WuJs-o03h1lnik-TcLv4s57JopHtQ8QtTT8RPDNAdQ4sx5K790E9n_ql0xs9kiqKdYepasg98ffxVWkc5V-Rra7UgO-Y756xdcc58OGywXpVEjMGWFUVRZiNThT_2DsdOl84_l3S15wVQFPPSF5v9ZJWtECRUHgWj2k5I9U8rDHuvzSit6SVFtUjBlqS1DXm1_Mr3uZEisfyohDcbrbQzL4c_0Rj4lQ91DLV0kpUfWE6uClMIlhkCGpOlU-Z2A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ce8c696d52.mp4?token=PG3mfnXUzpusrE4cg3PayepEqtIhLTMIoOTQ5xTrv_8mObOVZtgcKeDTUwZozaDEdXJT9BkaqapAoXGzVo50Bch2WuJs-o03h1lnik-TcLv4s57JopHtQ8QtTT8RPDNAdQ4sx5K790E9n_ql0xs9kiqKdYepasg98ffxVWkc5V-Rra7UgO-Y756xdcc58OGywXpVEjMGWFUVRZiNThT_2DsdOl84_l3S15wVQFPPSF5v9ZJWtECRUHgWj2k5I9U8rDHuvzSit6SVFtUjBlqS1DXm1_Mr3uZEisfyohDcbrbQzL4c_0Rj4lQ91DLV0kpUfWE6uClMIlhkCGpOlU-Z2A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
به عراق خوش آمدید آقای شهید...
🔸
چند قاب از اشتیاق مردم عراق برای ملاقات با قائد شهید امت
@Farsna</div>
<div class="tg-footer">👁️ 9.13K · <a href="https://t.me/farsna/447930" target="_blank">📅 17:20 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447924">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس ورزشی</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/YSbHnEqNCeJfnmyXrYmckdjyLG4_dkfgN1S0nlua1iQaXk60C1GoFUm5HM-SqMuJbx3SeGQf9jEWzWBpOtbkW2f3_lFFdtWEjTiNNia8-yl0f6vPFGV6dsxHwpdDlWA4ybXciZ18wWnYOIdHvD4CW_XKO2j1qz0WpgpgNNv1GgQc30Pz4NRKVVXLPhWwr6jnOr2kIelQDAisXOn8TOADNl7jtbPRA4k_wVgEJU6_srY2_2lRrgQmnZYzncnpRgC1GbRjXl7RJwkikFm7H7Nyu9x0eVFg3qWZ4t1U9NXQ9rRdPlP0yy4nNAvCjGChA2EXhpsTuUTn1lKinAz7BI4pfg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/MwbkgxwQ_uOnfxdmtLSJLcMPSJ45Qukd40QvKTz2p-su-a5eI7vKVN-e5V-XoqQSI5NO2Q1jA6snttrt5-dVDcnJBShKkRNPU73C-CdIl7yGhCCgeo2KVmyusTMZW25f5e0ms3ZNiIFCegyaP3mK18qNk4-F49mFYOtZY5CM3e15387bBnrLqAFwSGDEjsSHViyva2we1NX8T0remFinVwE1CrhbMbO5uHV-CgdXczDohB53GrkYPx7PnBAlJE-VdWUSOOaxlnohhqL2NeuB27cSpx2MwxK8AwBvE-xKF-K10rjFERgVWhBAgIb91PO2ZL4lJv0Oy6aySB5RLmKt2g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Y7hXRNyHIBvGzKIpG7t80Y4Te6L8UTIoClRaHZ4-ItOvoPLgCxmgpJ5Lrh-nUw5ZaM2l67wfdDaBrgq_I6bt3czIgXw3irpm-hssxORFKFWsp2ybagWlXdcpcASOGOrCIuakr1n8iVPRU9BdGvJNCvWgyDeHqntHN94qIXQtYGkC-VYnCjeP6tm0YXOZiMDUf702KAMvd9Yi8EkuNj1zITeY5LWenqJOCHPJhN3qD60glvXYdY-94MRtF84Y-37EMtVkJTUUMoidjpS3IB8Z4h9fcjd0B7P5h8Dd7d6mRVSHH3P1LhH0TvQgeRwQtKIhpM7iqcuE5GN66HzaWE7BFg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/nQWf41h_5Cf9c2eRmvzht5WIRxOi_2i9bI88QxMOiHar2_pdh2JfjJR9tg5AOI5GXifqlzi9CkZoKbZTHfViq2JXZByHlGgFp7VbecOZXb2oa8S0vo9oKJcO6NMssZYt2DhPAGh1zeaTmGMBbwzJWmPPjDspPcRMTm-WvEmr5Xi4jYXUOqnZ5L_mCDLgHzC2kZDu_1Z-E-UzbXQZkie_dUL7phSimSDlSwSheh4gAcNJzmlQMlE4GeOjTC5mbQoguyfRR6i_T5l362VjplKrdZIsL-sEl5bzgnHi_rbo2c0kfnl9FjNxihz0RpD3qCa4yYz-U_uercOTcz0j4HceaA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/u-L8Ks9RSnUuSI1lxNyYNPjjv1VzU4U2fHFODDLa5f9ti5lJs6XpOyslCkDvy4SowbCqn7ZsHThK4h9V4C6GpU4Oz0rfS-8f72u6qOmeSC-5kEDeHBf7HoJihfvqkwjmAA0LQuQ-08WUiICBzpkYqG65tHf8O8R43EIf5ybVCO7CpQTVvNG1QAI3Im5mhjsEk_Er2OWsVX7KeCqrCODnDVxjZEgSZmn1LHMO2nyqZ1-o1JziuZRKbWXkpXMCJin38CHEHOuclKJrEf7hMF9GyrE1Z72EB3ecCFruyDqjbTzXmlELYI14y6h7D8OUsGrppZW8gxwVCMWI4UKKWbekew.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">⚽️
⚽️
آدیداس از توپ مراحل نیمه‌نهایی و فینال جام‌جهانی ۲۰۲۶ رونمایی کرد
@Sportfars</div>
<div class="tg-footer">👁️ 9.26K · <a href="https://t.me/farsna/447924" target="_blank">📅 17:17 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447923">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">حادثه برای یک نفتکش در سواحل عمان
🔹
سازمان تجارت دریایی انگلیس اعلام کرد یک نفتکش هنگام عبور از تنگۀ هرمز، در سواحل عمان، هدف پرتابه‌های ناشناس قرار گرفته است.
@Farsna</div>
<div class="tg-footer">👁️ 9.46K · <a href="https://t.me/farsna/447923" target="_blank">📅 17:05 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447922">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Vp4g5zaLLFmA6Zs5nJ1b2vCpIhAMoLLrATUhCRQd0YvvZMf0Q04h8wk2iRGuzuTVbuwjGiRNBldr9Pr8Pu_9uCp8lOpFR9J1IlJp8cqKYuMKTwK5rQ2LNYar9vkoNXfUbm45a8ABDRDzErCQ2NgFRWiuwA3r7iI7XbwJbJovJ1Cs7KMQ7JXCbFL75O6W7YXhRFO_9NojErP8XSdb8Ut2YyXbf8SZy7ci3yXyM1qrH6e8W4ti0aN1wXfgS61wjlxNDP4xoxyxrMCw6mD_S96iG4TKILXvDqcdRXBCua8BSNMrOw4uE5VyhtCQIo1Gp-bsfMnT4MmgS1QM90xKEbSyug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📷
آسمان قم میزبان طواف پیکر پاک رهبر شهید انقلاب، بر گرد مضجع شریف حضرت معصومه(س)
@Farsna</div>
<div class="tg-footer">👁️ 9.94K · <a href="https://t.me/farsna/447922" target="_blank">📅 16:59 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447921">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a4c8b46e0f.mp4?token=CdQZYBgAmbzRpb_RORHP26w5ZGhiJZ09akliPkfc2po6K21SNM6Q7s20P0C8DO5QasU6Y0A_gavcvusT7iKCnErJsuFnLOC14fgIJDNkUhPEfU76Bds5KIDatNLEZZRLHL7_OY5LDRB_vOCDS5OMG1q66jgOQuM2FutNBIv116W0SYur-8HfnmYlh1hmRsUG8RG8u7FJydepVf4kKkyOmNWMqO3gu2tWMthTblPqCVB3uQlGkwtQiqi9caCLfzjdrBKgDR38IiQ6Pt-ZCjWJwx-UDXubw3XfxJGfz9vINem1Pp4zl8AVYDxx1KM3MUlZMfPqhBQF6X2LX_VGtkgrHQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a4c8b46e0f.mp4?token=CdQZYBgAmbzRpb_RORHP26w5ZGhiJZ09akliPkfc2po6K21SNM6Q7s20P0C8DO5QasU6Y0A_gavcvusT7iKCnErJsuFnLOC14fgIJDNkUhPEfU76Bds5KIDatNLEZZRLHL7_OY5LDRB_vOCDS5OMG1q66jgOQuM2FutNBIv116W0SYur-8HfnmYlh1hmRsUG8RG8u7FJydepVf4kKkyOmNWMqO3gu2tWMthTblPqCVB3uQlGkwtQiqi9caCLfzjdrBKgDR38IiQ6Pt-ZCjWJwx-UDXubw3XfxJGfz9vINem1Pp4zl8AVYDxx1KM3MUlZMfPqhBQF6X2LX_VGtkgrHQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
ترامپ: به فروش اف-۳۵ به ترکیه فکر می‌کنیم
🔹
رابطهٔ ما با ترکیه بهتر شده و ترکیه از خیلی جهات، بسیار وفادارتر از کشورهای دیگری بوده که فکر می‌کردیم به ما وفادار بمانند. @Farsna</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/farsna/447921" target="_blank">📅 16:47 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447920">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b3b8ae83e9.mp4?token=cR1LYyNflSRBdon7aKhBDmu4EGGwlhpr7LGSz36_mUYiVvlu6VddN0pK0ow8DPtSSgPJ-LFG7_MLZgYsUNQ8SmnUdOK7S65z99pMjaFWNHg-PyR9_LIFKn7ykq5WBK3jZ7oS0RSHWA00tj20AaWwvZzmcikrJ6SbcyPkyl182kgj9_Du-iYEt5J423Uy-7eaLhjhYBZiExDu0oMr-bt-gxxDprrfUWmWmOQkumMdA61g_E03fGioEsYqkn7s5sZ8Mvwa6iVoJh4pSzHO5WRVwTyu9XChPntgJmA1ce7vYhk4f2XIEjN7mguKe3BCsB0jan0Fzu4MgHCYrXtTvfA9cA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b3b8ae83e9.mp4?token=cR1LYyNflSRBdon7aKhBDmu4EGGwlhpr7LGSz36_mUYiVvlu6VddN0pK0ow8DPtSSgPJ-LFG7_MLZgYsUNQ8SmnUdOK7S65z99pMjaFWNHg-PyR9_LIFKn7ykq5WBK3jZ7oS0RSHWA00tj20AaWwvZzmcikrJ6SbcyPkyl182kgj9_Du-iYEt5J423Uy-7eaLhjhYBZiExDu0oMr-bt-gxxDprrfUWmWmOQkumMdA61g_E03fGioEsYqkn7s5sZ8Mvwa6iVoJh4pSzHO5WRVwTyu9XChPntgJmA1ce7vYhk4f2XIEjN7mguKe3BCsB0jan0Fzu4MgHCYrXtTvfA9cA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">درخواست نتانیاهو از ترامپ: ترکیه نباید به اف-۳۵ دست پیدا کند
🔹
نتانیاهو در گفت‌وگو با شبکهٔ فاکس نیوز، ترکیه را «رژیمی آلوده به اخوان‌المسلمین» خواند و گفت به‌نظر من نباید اف‑۳۵ یا موتور برای جنگنده‌هایشان در اختیار آن‌ها گذاشت.
🔹
ترامپ ماه پیش تلویحا موافقت…</div>
<div class="tg-footer">👁️ 10K · <a href="https://t.me/farsna/447920" target="_blank">📅 16:40 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447914">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jDCmyxAW34lwEqVWuD4jJ4Aix3TcETbDh35hqTjh8gTWtOESkws6lLLtGz6Fi28lpbrRRY3YhPAzpoOwPYMLxcwZXtLjZ5Jjd4fNREG3oW2d-oObxzzYOs_UOPJl9qT1IlGM3fsGbSEHUs1Npsn8K9s3Kdru_R37135CS2BitZXlogKPeyIVj7eFHmSOFOkmGCR6fCS3J69SdOLWipj-hyOJZws-sDxTZ9rGzdFupBuZRo-4iEBhfB8jFYM-9h4XLrRW9kGbVgqTPVEjw3N-h7vDd3m3dBd2Wq0K3hKYxWljHgKw0rSlzuYgf-R2YCco_6_GfXhXnWk5AHNFX5847g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Ax9iXKOJVkDOZ0nkGhIvi7X2iSb7QB0P4vfkHc4fHc74MOalXCyooGW0DSP0HOYVKL4rOPcU1-S0ktE15Gog-hKJZ5bVqG4_K22jTfxrqlE-bjn4v9sTr1xLxDZk3FGPfUHwShlckUYqCxkn-fGhjqWf37c1vRqid-VwAeuI38VYpL70HiLxzbewMjkKxspcO025TlC7hJ6TfwJQbEGWLEWSloQz2AQlYTIarxGoFuV5lkvxDtWtaS-oUiw0-4ajLE7xbhkNDop0piwvXkua9aHFkqNeniX47SIqpyYvTPBEZ4_Gpr1XmuGtqo3jeRMfihMDPKWzIgwjgNy994-a1Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/cTo0uh6XeaQwSFQvse2Xz85g_wvxO02E1O1g84kLOtBBiJvKXyoQMuwRWhnydkXqLdq418kLhzcuEpoxesy_jwGxxnYrhUEhXDv0xj5tyhzMfxIYyvMKlxyXX_nYkXYsTjB6JGNeIj3gZ4kxrvJPL1th5hHjcjMJmOagnf7W6hzwi9PBnVrlDsj2MDNyonj-jcW9ehPDS5OKhAQir65dGMJL-i04wVxiVtvJ5lKjW0JMpwiQUO40tzp44amNMGwjk4ZJupLzTyyz_B0t7_Em0Hv8m-qEP6fVk9P2Zk4uWXDsCWyF7eCQSJylsq52lo6U6dqBslnukTGIIF5wQyXRtw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jU8UDqUzSg6_-xXoGo6WJp9LMq3lZSifMdo4zEyPRq6sE5PVablPXYaGbMhWhewwKdPHaIYmRu7e3UlWGW_CywKtteHVKr28UiznAqa9xKJGq3vqTJTIV4ua7DQbs_Q__-l92G95ysp4iLIEKD5soW1gSftsNXrONfN8vium83ohXK6npL0BqRcWe9vVb_1FY3sgnQG_4nT3qwqKiXQAmtFy-fPUwqkxRqbEme7pks-2le9eoYw_pk5NvZgj2Ld5cTtQTwi1yvMBwgrOx-4R2Ahm9qFZd4WyCpYqkt7GFI9sR8FS6QrWa2qBYaz2oAQ1b9N56FhN1trr1zKrwBG68A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/FOTGzsefftBvXn6xZEZvj5yMWypTXsfIq-EFVQRyC26UMKCW_WiYG_wMV-DY1ZPa9Ro-RO-5kVZLtUd_ZxThuDt3f_iK5N1639dhfZxOh0hVhTf5wzeVL_r38SFUfVBm75f9HClP-mjstG86NS-kPMOZl7rGa3rZPCAIS_7moXIWaWWcvk1B45kKLqQm4c3JtjMlM3i-Fh5wdDOWBzkNLRde7izavsYrOfVRaKlT63rMy-jx0OiQ6hAL6RihSMy5z69nnKpNyzsbMVKlRC12mXZxr37MTiSslXo9dPEU2FE2Hg-Jgf4CP5KyZg2zDGx9Wh_9hM5MS01KjLd_OumbPg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hQFFKfHk53uOqN1nXZFWb1AoAvYe9KrtGwTSODYZMkK3fsPDkeN3ZeIGNnbL38ohFfc5kpS-j8baYdZPkz3_wdAbCyZ_sp7hcf7ABZW4XelHzh0W2dxgcC4Wf4ik2kwG4sY5w7ffZdNOymr_wVxRuHX4cX6w85OLI9uNdWl6oRCJP4Q_aQj0jdhhEqrRUA8_6AhxGvNwe9YV1zquYVlvxHmQ2mXHn_l6YgJnVqiIbefH9SPFXOjxcVvpoGEaEjiB3gPFEn7Q3UTI-D-lMyHV7t2-0cWOfCZprFFCEpCULzFI7j88LfBb04g0909_mxmHpWH__NAeellqAmZS3adrpg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
اقامهٔ نماز بر پیکر مطهر رهبر شهید انقلاب اسلامی در جمکران
عکاس:
عادل عزیزی
@Farsna</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/farsna/447914" target="_blank">📅 16:40 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447913">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-text">🔴
چهارشنبه در عراق، تعطیلی رسمی اعلام شد
🔹
علی فالح الزیدی نخست وزیر عراق دستور داد به خاطر برگزاری مراسم تشییع رهبر شهید انقلاب، روز چهارشنبه تعطیلی رسمی اعلام شود.
@FarsNewsInt</div>
<div class="tg-footer">👁️ 8.71K · <a href="https://t.me/farsna/447913" target="_blank">📅 16:29 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447912">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/201cd87687.mp4?token=V46rB2oaIZORByP2XmhINaZ2dawLVWk4NxsnNlwYifjDhQfhkw-8150kbmXkXMxmS1LcrcXVKiRcheEBLfP85yEPwBgbOiviU9l_tYwgTq-DZ1N1qczggj4wE30UVaMR4tNaMc7Vr4zYQYpwTGLQMytRvBf7MGGdxtVJe1VOteP2YIXiN4HZ3UEl6VV6OfE5obVNTi0NU8bCAxGFpuW8p1UBxraNjxkhd6Ewf7hCuth4s_cdXHcLYSLNURoNKoG4Qd0f_tVqAwua38uHYF9IoiNKBbGHgqA9v1wvRCi0Sk6--YC6OeWuCRJEge5DOJz5-8g5UYbF557_AsgmrLXSrIi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/201cd87687.mp4?token=V46rB2oaIZORByP2XmhINaZ2dawLVWk4NxsnNlwYifjDhQfhkw-8150kbmXkXMxmS1LcrcXVKiRcheEBLfP85yEPwBgbOiviU9l_tYwgTq-DZ1N1qczggj4wE30UVaMR4tNaMc7Vr4zYQYpwTGLQMytRvBf7MGGdxtVJe1VOteP2YIXiN4HZ3UEl6VV6OfE5obVNTi0NU8bCAxGFpuW8p1UBxraNjxkhd6Ewf7hCuth4s_cdXHcLYSLNURoNKoG4Qd0f_tVqAwua38uHYF9IoiNKBbGHgqA9v1wvRCi0Sk6--YC6OeWuCRJEge5DOJz5-8g5UYbF557_AsgmrLXSrIi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یه نفر رو مثل آقای خامنه‌ای پیدا نمی‌کنید...
🎥
یه نفر رو مثل آقای خامنه‌ای پیدا نمی‌کنید...
🎥
امام خمینی(ره) بهمن ۱۳۶۱: اگر گمان بکنید که در تمام دنیا، رئیس جمهورها و سلاطین و امثال اینها، یک نفر را مثل آقای خامنه‌ای پیدا بکنید که متعهد به اسلام باشد و خدمتگزار، و بنای قلبی‌اش بر این باشد که به این ملت خدمت کند، پیدا نمی‌کنید. یک نعمت خدا به ما، این است که داده./کانال سلام آخر
@Farsna</div>
<div class="tg-footer">👁️ 8.86K · <a href="https://t.me/farsna/447912" target="_blank">📅 16:29 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447911">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromبانک ملی ایران</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/diq5-jv-NGm1xLA6FzHXK7OUeVOSzLPmLHdmytdNf14LouioAWdnnxvYcUI3xiiLgg3jd3F_S7Qb0c3VolIhatDVOvNVHZEfeINBhKoZl2kppLuiF02mcAuy-rozZGfg5EY7iX1_ICh7K8cDmHen_6K-_ZTH9__N78HeXtuMNX-QzM7NpnEHYgunktz_nbmuYq4r5r_pLk3rTd9PLrUbQTMUUcy38x66ahkjfnTHc3NhQUmg4FYsb15hpNZh01Th6vairFOKCxAs4XI4VowutwXTXHvHSbQR5IlE2DqF4nFcNO2g4e6nOQJKrgZJ7LsD3L3OOEu0Hs-EGQ34DOLAww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔺
اینفوگرافیک:
🔝
برای اطلاع از روش‌های فعلی انتقال وجه، این اینفوگرافیک را ببینید.
جزئیات هر خدمت به‌صورت خلاصه در تصویر آمده است.
@bankmelli_ir
| بانک‌ ملی ‌ایران
🌟</div>
<div class="tg-footer">👁️ 8.27K · <a href="https://t.me/farsna/447911" target="_blank">📅 16:28 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447910">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-footer">👁️ 8.09K · <a href="https://t.me/farsna/447910" target="_blank">📅 16:28 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447909">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f489625ab0.mp4?token=g0EFew3XnYkwcq5TsgcQCBEWcFpgAsl9sDMxC-Sq0gdI4zMkGJ1qUuDDF7u3Jl4jooo0hY0tMs_AKYYhYfc8x5V0oWx_tscKAC43kBYqntsaF_GCG7r956ofyMeslNLF28ekuOTTVhEE0FC2hfA-s1au6vY3fTqJ9B13gYbzggm8suUx3pNX0_AlOJyZJ8tIqCQHpx76_w3CLLB2wANp1Z1K4dQQ41g6QmyGWZ3PvY2klmY0ulcy2lx-fuZLZ386ON41nIOVe4t2hxZRAEO1QUwO9SCGYpswJt6ShUCVtDaW32kz2Zs6JkW8xpSaJaBjT_8lhpE_9KhD6kYAJY0eTgEEYyWBJasyzvzEc5VjOZFgTOcgjU1fBuQ3ZeGsgg0WPkHpW-QT-Rt1RzbSO5CFRr9G8Aix2DQotEpHg0B0zTV51noJSdVdlkTQZLh2xANE4qaqkH-0H9_K8L8OcjFjnB6Q499upLFugHpA1ycrFDAQH21ZU3HTbN7VfXe6G4HMNnTakBXS3Wpmu2d9wQGwdo2quscAkMVRmJeoO5eWgqzfUPVCa6Q30vM--AW7P0Shs0xtoXMSd1qjVom161Dl-gX9NCtJPfkcI4S6CzY7mAqHgJyMSLbNvL_u8B-dDAc3YZTRT25cwFQuUQ6_0KBxiLp9eHCOm2Uka1DRRlMuRsk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f489625ab0.mp4?token=g0EFew3XnYkwcq5TsgcQCBEWcFpgAsl9sDMxC-Sq0gdI4zMkGJ1qUuDDF7u3Jl4jooo0hY0tMs_AKYYhYfc8x5V0oWx_tscKAC43kBYqntsaF_GCG7r956ofyMeslNLF28ekuOTTVhEE0FC2hfA-s1au6vY3fTqJ9B13gYbzggm8suUx3pNX0_AlOJyZJ8tIqCQHpx76_w3CLLB2wANp1Z1K4dQQ41g6QmyGWZ3PvY2klmY0ulcy2lx-fuZLZ386ON41nIOVe4t2hxZRAEO1QUwO9SCGYpswJt6ShUCVtDaW32kz2Zs6JkW8xpSaJaBjT_8lhpE_9KhD6kYAJY0eTgEEYyWBJasyzvzEc5VjOZFgTOcgjU1fBuQ3ZeGsgg0WPkHpW-QT-Rt1RzbSO5CFRr9G8Aix2DQotEpHg0B0zTV51noJSdVdlkTQZLh2xANE4qaqkH-0H9_K8L8OcjFjnB6Q499upLFugHpA1ycrFDAQH21ZU3HTbN7VfXe6G4HMNnTakBXS3Wpmu2d9wQGwdo2quscAkMVRmJeoO5eWgqzfUPVCa6Q30vM--AW7P0Shs0xtoXMSd1qjVom161Dl-gX9NCtJPfkcI4S6CzY7mAqHgJyMSLbNvL_u8B-dDAc3YZTRT25cwFQuUQ6_0KBxiLp9eHCOm2Uka1DRRlMuRsk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
شعار لبیک یاحسین (ع) مردم عزادار قم در کنار خودروی حامل پیکر مطهر رهبر شهید
@Farsna</div>
<div class="tg-footer">👁️ 9.21K · <a href="https://t.me/farsna/447909" target="_blank">📅 16:20 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447908">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b16b182af5.mp4?token=cD1o3iuhcgWodVHSiI7gqFFzf2Dp0Ou5Y4s7ewLzJJzVfpi_mK2RWShAwWl2cbYVPOq1bcLIURwxGux2ar_TV7TX-TMmdk710V6Z6RUeVDvSYJsnxBuOu8Iw9YumGV6SYSvBBBtk0e71GK89LxJTROw1uXHYL2KZcqaojWRg-eKn8DLbalOBhsHioEJVdoNbx5rp0vMhO32rH53Z3tL40Il4NDCw0nbUG8bxcIPFHd2-CBHch0IhF-dpOtvwYqtpywXRUcVJPE-yayOBNsfcNG4Mx4_pcvaQ4LP9u8hhJMsDG0L32BXxHg12lJ6OISq_5_vjLfglACI4V5U_JSLv7jzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b16b182af5.mp4?token=cD1o3iuhcgWodVHSiI7gqFFzf2Dp0Ou5Y4s7ewLzJJzVfpi_mK2RWShAwWl2cbYVPOq1bcLIURwxGux2ar_TV7TX-TMmdk710V6Z6RUeVDvSYJsnxBuOu8Iw9YumGV6SYSvBBBtk0e71GK89LxJTROw1uXHYL2KZcqaojWRg-eKn8DLbalOBhsHioEJVdoNbx5rp0vMhO32rH53Z3tL40Il4NDCw0nbUG8bxcIPFHd2-CBHch0IhF-dpOtvwYqtpywXRUcVJPE-yayOBNsfcNG4Mx4_pcvaQ4LP9u8hhJMsDG0L32BXxHg12lJ6OISq_5_vjLfglACI4V5U_JSLv7jzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سفری که در حافظهٔ ایلام ماندگار شد
@Farsna</div>
<div class="tg-footer">👁️ 8.98K · <a href="https://t.me/farsna/447908" target="_blank">📅 16:15 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447907">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0d5a8cdbd6.mp4?token=Bv6XX1EKyQx64LGdAc_FErnF5044Chv6j6rpsq6GNJUuzZZ_v5Bj6_pic_WiVeScaoW9kM-1ZiB_Z6O7xW9Sy-DH8Va0u76zq8NOdAbENjFFIlfysqSgmURY8m1gdhLwJRbf9pVstMQvw31M2q71icSOKozbC6ZRUojs7apGHiA63dyEMk8w8cjIKsyY_AUzGV_XyJMVtW7ZIBRbOaogUNmjt_A33WP8La1EUMS-Iyrk4ferkKQl4QOhCh1rzFmkgXtwud0XVV6abmFZInLNXS_yLryP4F_pOqHNlSABFS6gRRgFicMSGGWuZy8Ee3H7U-xst3UoIilLKKFqyR9gUQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0d5a8cdbd6.mp4?token=Bv6XX1EKyQx64LGdAc_FErnF5044Chv6j6rpsq6GNJUuzZZ_v5Bj6_pic_WiVeScaoW9kM-1ZiB_Z6O7xW9Sy-DH8Va0u76zq8NOdAbENjFFIlfysqSgmURY8m1gdhLwJRbf9pVstMQvw31M2q71icSOKozbC6ZRUojs7apGHiA63dyEMk8w8cjIKsyY_AUzGV_XyJMVtW7ZIBRbOaogUNmjt_A33WP8La1EUMS-Iyrk4ferkKQl4QOhCh1rzFmkgXtwud0XVV6abmFZInLNXS_yLryP4F_pOqHNlSABFS6gRRgFicMSGGWuZy8Ee3H7U-xst3UoIilLKKFqyR9gUQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
وقتی اینترنشنال کلاس احکام می‌گذارد!
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.82K · <a href="https://t.me/farsna/447907" target="_blank">📅 16:09 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447906">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tf1Euv4yV2-mD1Hzf6NgZq5jSkcPdRqJtXg2XLgp9Lneuks5wcR6nQ2lotvEmNKBoWBNWOu2E6pFrQMH5dV-gMUhDxBz23Ms9k9-786ARmwcpRoHt8kwO6xeLg2qrrISYMswTP4Br4q4gT59iwQDkQuaQD2kgOJY_zbuv5p7Q2EPq0w4AdKWI_xBHlSUVW9vTdpxMAbR2L2SMCko9I0LY3akrtYKV_ywUkRwwlyain2Qj-oyzWj4z2f0GbVrEKBvXRMszeMCHf7kRpVpq--qu_J-3LVRnh13pKC67aJfF_WffA6TCjmk2w-Zdm5LXEKk7uqpSd0lcTzpeQH87LMPGw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آستان قدس حسینی: شیخ عبدالمهدی کربلایی، نمایندهٔ آیت‌الله سیستانی و متولی شرعی حرم حسینی، فردا در حرم امام حسین(ع) بر پیکر رهبر شهید انقلاب نماز می‌خواند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/farsna/447906" target="_blank">📅 16:00 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447905">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/30bd08b26e.mp4?token=oE6LXTLoFbt8OCLr8a5EutjOn9EjYd9iM6f-NtisgYzdO-k5ZH20Ex8qOnrh0L5mEU1g0CgReBMKue6iDHl5vmI-jgnqJcE2CWThpL4vWB8IoxYVGmnAfbnRkvmvCT5LxgMOBvH-6U5octk1QT6y0rILJOfGb3I5NFCcmcenrLMd6mVfEFc2b1B-lcZFsVGgcwLuQzf6AbARQxOZTqPi54ZDp-rYRwc3ck6oYOsBoaISvCB_L_Gnm9ldeRRpm7g9nYyoTgp7_oEjlj3gLacIOnMjkdtFNIdmWfD7tJWS3ZpoCVY8z9Bo0XhFVT6osZqhHkHpYAM_8T6eJ_oX_SsMTQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/30bd08b26e.mp4?token=oE6LXTLoFbt8OCLr8a5EutjOn9EjYd9iM6f-NtisgYzdO-k5ZH20Ex8qOnrh0L5mEU1g0CgReBMKue6iDHl5vmI-jgnqJcE2CWThpL4vWB8IoxYVGmnAfbnRkvmvCT5LxgMOBvH-6U5octk1QT6y0rILJOfGb3I5NFCcmcenrLMd6mVfEFc2b1B-lcZFsVGgcwLuQzf6AbARQxOZTqPi54ZDp-rYRwc3ck6oYOsBoaISvCB_L_Gnm9ldeRRpm7g9nYyoTgp7_oEjlj3gLacIOnMjkdtFNIdmWfD7tJWS3ZpoCVY8z9Bo0XhFVT6osZqhHkHpYAM_8T6eJ_oX_SsMTQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سخنگوی وزارت خارجه: مراسم تشییع رهبر شهید، نماد اقتدار و عزت ایران است
🔹
هم‌زمان که همهٔ ما سوگواریم، با تمام وجود به روش و منش رهبرمان افتخار می‌کنیم.
🔹
ایران امروز مقتدرتر و سربلندتر از هر زمان دیگری ایستاده است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.57K · <a href="https://t.me/farsna/447905" target="_blank">📅 15:52 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447897">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/MTo_UDiCOBcNWfhZO1ktKN0e8BC0cwWMZxMKHQwqSq2IDzYr_aUaukiniA_8CAKkzUS2I6UZNtFiJJdF2gqVMi2Mc5fXEHW5U9GZ-9coYmCz10QxcKr9OqSf35wzqT3p4elBcMkh3_bUvJxdQtbIEB4A3riKHCsAJ5JVtSLUeZnnO2xLuisBNvYnB473Bx1BRiZEvSh5U2Y9q04oGrEEfg-EP-kqenqbEjk16jFz558hssuuQyDC_hasJRncsJqB4Xx6FWhP_i5LlVt2guS2gl9bYV0MGYLO0Ae08r7aGUYavMpG83Lki8pzGyoALTOILh4icP9BDmVoVQpopJnVWA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/eAY4XDsoElcIY-OJOF6-Dzqx-cBI7uhpI8aGEW3AfptnPxQpcrzueGOqlOfoVrWCyGimDTv-axa_JlYrJXE1-ldNdz22MzWaKJxe4IkisSN0Pky-Zmo18Tk6jIweL17mWVj_j1Azf-NmwOgNP_uumhGpnzeEqZpf9vty__v9bFivQr2yRGfiOZw1p1vbDi1dMw8CA1X0VFrC0LU0XpBjmwA4Ggy2vkNfX4nOQhFAqGkOpXk8XaTahnBP0o9eXwzxNBArKOF_HCy5UGdW_6te6XW2pn-NkcNZuRwP-Biw7hbH_LPjAlMfdauvJTB2ZzUGOUuPh5u1KLy6h3OeS1XJ4Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/CFLtJW6J_HuSLpWUwlcO7DnHDYRBvXCDqWbiSFeQno_r441j9ReT_BLJ6PmEG3DnM_AD6x3RpOkp-_t1rJXF_yv5IYIndtMZL2QLApC-SOc5jtwxGGvn7dItF5AyORdfNM_FIcBERJNzxIfVWfGJCZvlTD3GF4K5whYUcOfiCwh0Vovw3KzZr7ozM5Avp5wUkQ7Iv7eP5Rf4QmGSQEP0IZg8idnqoSZzl_E3xOnu7FYWvJBqP2VUcs3zDSZS1wo-qC392vpdN3U1XVpxm-AhD1UXzCj2g5fM4GeFPDwVDfM3FtiCKJdWmFqeJh-KSo_JBDwxXSESxWgJC0AGVQa2Uw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ddJnK1DFtpOyQckwwETv5HOyXaGomj6W7uK_yW7ApJPSWfvTHNmZWGC3hYTM8SGDCWGyiqx9xrLGBaho1XnRh0FE28QY7nBRVhRpGYjk99sRwOgGsThYG-gv94FiTfT10yaZzOHjTMmb5uFFaK7YAVKs0iU6zw7epKYtrzmHi5L2m7JtNWiYZok5PpWqBa0YrlvKaLsHcx72AdBxF4jYP0VhAXOGHHjKBWsHHgRvTh6hbGz8XxpX_LsaBTSJ8jzKFRvAiikR1_VnX3x5svKFm-aNc_Bl1yRojhusxb_ysWhXvZvkfyr6pTvTTzVcI0IUGKD5K8pHEk4pXuj6tNrR0Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/RnY0DuJHDa6S2RDQwfnK9u2zpHthGaQeyWt6jNyvTL_WN5tstI269wsZsctGTMkIG5q1bmbRZIL34yiswY6g02jz0ZcY65ddxjcaoBhVq1ALqh_p40HTEBLcqmUa5801okmmW0ozpzRQnHH3wahrIb44ZRWfslqZnoC6EToGv3-YgJaa_JGOGMZWuBeKtkqupGuYRD7iRDPXAY7yMEuYX4NWjgvYneGhQ4fWXCZ3JVoEOG9K6yj8jlozlXxY6sTFjdw3CHAjPlVw7jaO5_4Z0VwoynYqvFG7VdeAPizSw14IRCkqmWrs_pwBF4W4FrO0PHP_HW0J2crUbqfkNe0sZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/RLSGAlB9BdnVfRMEJtYFe8fFfTsymmQlkDVVu4iX4kGKeXkc4EMSPKXmM10IaSKqVMLGVpEWQMs-Q3TUTeyurcLHyItsQ8wwgcC1tM3zHYgDkTH1Q4sjX4KjXpmORNRoNXw1kLAvVZygCciPtGiXvhq9Mo_2ieyEYFi1a8WIrX7Bkh1Q5pQ0fz1MQDWzsobBJhmGQIZxD5kvymmBYobbjhAoNGKI1VXUmuI4w1BCXdixWwJxMRyzTLzfAXCxAqJg6GeQrP7di4LqySln2_H8I5c_ggyQySjK-GjKRYjYajAt79ax6h6P6zh6fXJDs5lwG5G-tw7fz5FGKlg7vO8fng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ClYcVcNOjsHL-0EEsRUMY_6VnwR-WIDuGXyLf4w0bELpBOiytWYtj7Cm_Q04UuMht_zgcuLvjnbphidtPrDTuMBaE--HFSONJlm06ldgjh8aE1n4mbCWIAZ3XFUa4GWnlOftJ_dYugAVbC6wPBndZEZrDOccTET-7ejnGb1c851XxrPY2fjrMF3xa48PYmjE-7ms3OSI9dZdJVlCJ9TMeeuoqdb0HkE-k6IJBx5mN9tVXPE2L1ggtE1UEaoUAkOz5nInCVOmITxCXTugPr4Rf8tO_7PGIHJYE74G7wZ6Mr5QRYhdfs5GmXToFUrBclJXhPKsM4KPPvsMdvU99E50FA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
تشییع پیکر مطهر رهبر شهید ایران در قم
عکس:
احمدرضا مداح
@Farsna</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/farsna/447897" target="_blank">📅 15:45 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447896">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ebukTTdiS1mGGvhk92CBJe1mEmsbmt2tuD2Q1sdvqLZ62NDLZ3SG1-zT3jjJvajsZds6uXfxLuB95eOW6IsVxKsr13fhO6FYf6rZq8C1ovP-2Kbt0M32ney5hrGhMRI5X4-HVXRHxK3Z8j7pj_pvuDPf0CMdrkxSY7lZLsVaZoMJHBgPGpjvTxiwfr2s_29mIFOIH2HADM2gVCB77RGrH3J6iD_aTvfAwW3fO0uCfQftZzbo_BoOR7i-8UNCgckJL8_uPfenxxre7ekraC8oWPsFFS_TjTeR2LgMnzFS55U4vRirtXMY5Dl1FIf1zIv1xs6UiVyFD90lUKbQIFUKHQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جابه‌جایی ۲۴ میلیون مسافر با حمل‌ونقل عمومی در ایام وداع و تشییع رهبر شهید
🔹
معاونت حمل‌ونقل شهرداری تهران: ناوگان حمل‌ونقل عمومی پایتخت در سه روز برگزاری مراسم وداع و تشییع رهبر شهید انقلاب، ۲۴ میلیون مسافر را جابه‌جا کرد و رکورد جدیدی در جابه‌جایی مسافر به ثبت رسید.
در این مدت:
🔸
۱۴ میلیون و ۸۰۰ هزار نفر با مترو
🔸
۸ میلیون و ۶۰۰ هزار نفر با اتوبوس
🔸
۶۰۰ هزار نفر با تاکسی
تردد کردند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.78K · <a href="https://t.me/farsna/447896" target="_blank">📅 15:36 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447890">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/nZlnTvuQGPjvZiSM6mer6srJkFGm8wOWTzZ-J7Q6dZ1aG4YisQxbSmqw4eMdnBBDZqM9o3NxVSrYmPI7m06TevNGxQzk-rSe3HxQETbUTNT08DtgtcD6Qym03BFLhbBBe5XipQSc2KirCurRY7bLoumgVmPYnJMgrQ6KI-VgoRKijYIAEyeaMWaZ7GDXv62M2d4_d2b2mcsPJzgscSLYo3uXOw3885AYo8ApcvC4lGcsCpFtgxwMD9L4LPd2bbsOH5b17AU8Kq9Q9_IFPm-rCLmqFazK8OXNyCPloUF3_AxZiCbuVp-bLGlCamtc_PMjwZtFyKGKqfTsQ0j4LUg9hQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/u8CzO9VnY3z4L5SoKAP9q9Vbyhzl2yyPwHU8YHbWyZEEyY6W7BNd5FKtV8MaFe-HGrDiPVJ0cLyqOUXxjaEM6cc9UcOY5Cr7mmry624MasXDv5PVVTb-RO8SJS2I4xd2Bv421XcIYST5Jogi64fxIaQqv_Otec7K19WymA14QnvpKCwFTNXp-rW7HXTXI924kTFCtmlTZqCeB9CfwdHthw0OClnyemWv6NRa75FqIojFtlNO0BAEVtSVXDg21LXZ0D8PdXTkI06GfGmzNfXH1ovoQs1dmV2TC-EQLWJvOJ7HSAnEO-CB9tH__CDDzVglLRu_nCeMarosYn5h6-fNnw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/fE04QwvoPikCYo5KeqQ4A6CaFFIbY2ttOrQ4wrRaRUL7fJB22ggc7F_VKi_KUZ_I461jXOuoZiTalPVbk2OT691xXtUoZ7DVMV1c969Iw6YXmjFbtHGUC-SVVw41jJkHMtwafmnTEG42NW-B757fi704p7DcPvXH6_kofFeRFqjRcP4g5I5twhaC7tWuYhCBbDmU7eRObEiV1Xz28cfRHhMFu6hSP51stIq0mewZX2Lb77zU-0fIS6aOvhVMmf1xSj2goiWPWa3TFn2Yst8Weaw3C6gt0ldI4mSQ5htyofASM8NNLRqOQjje1Cv-1tlFTUFlb4ZaNl8OEsuKYqLrbQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/VNwLKRM80LyFs9cRfJE2WtESQ-tW9Q4KTRMHtBPiWGpWsrL9e8XUqeew7y291XXjX__JhkwChtb6rgwrK-DBT8Y8AzTpLB9j86xulsQ_xfG5rti4iSuLXU0FkeiuNZ_quPzizIR5R16zwekslyJJIdlh6_E61cq6GvIse3qw9pS8A9rByFaWqNPGulTCwmpdRna91PAmB53cvu7VAlMLssJqWqO6w11d4uspacqzal_kSfW4tNKVQXOYBy-3VfFlHsmPZwpm1C6V_Szf1gWSQs2UALyNc5gcuAS54ARl_XHZwLrTeliO-hAy6kuHsfNwxkIQlET0bR9XejHLUDlRIg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Ac2--cd2lUj5qHxcXTDgr2v1-L54EAYVA_NehOTKrgQKPMK5hIepSOketgL-VvxrNPxsjyElmzInf1BqfoVSdgmdYJgE6YN9YngfOlVBoPhTz1zR5Cr8zZF5Wbe0Td4PvqjtwnYvou4y0_t59Ibcn0_dBia3qfZEax2vEVRLF-_zxdgiXjSTCKiY5CBHHA3BPqbmV6fvFMEm_8oEgQKv2IyJq_nO3MLTRjXcxsY7kEV8wFamhvsPSm5QWsX8GApNfuqf2MEowDiIW1HofTofBbgK_DD689gpkSyX-Hb-DTMS07LnOoHWxToK3D2GGeul4QnNPf0S3Im8LhebXvLldA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/MckTovpj3JgWYdpGCHYK2Ikbf7bnZXJWh5MbN2yUX1UGqNj3CGp71X6d89-kc_tJ2pksm9CBdsBhpdHW9Myf1SDL2vP0YEVB1yN_dx-8kIsLDP7x3WmhwleYOwBqC_a5jmFioBxSlZKoncxB8sITBGae3IE2yKPua8U6yimL4CzMdgUsmnzqdv3XaKDoNpAzkQF_76Q3m3TT-O7w2sGWoVUnXi6DWxy6s2JcgBPky4PVFii-LJ4PSeiefvzro5VsYtgzZVmxVXgmXKKusyqBiHI3Ko9_nlw4aILm8bwvAIC77Ra46Qxi2bQuhvp-d6fsYyn_vOYlqdRphMX9JHqR3g.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
عراقی‌ها، آماده برای بدرقۀ امام مجاهد شهید
@Farsna</div>
<div class="tg-footer">👁️ 9.71K · <a href="https://t.me/farsna/447890" target="_blank">📅 15:29 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447889">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3d6a4568ee.mp4?token=VB-44vaoXYTD90SSqP0SbWyGnPlsPjAJSEbQaEfYtYevfPUxgy8NyrToqmlyR7cZXEkWlCFOU3gXDmOiWy-CfcD6bBZeNY1wIhwZTOVc5sbrkVbYoc1QiDfcIGIl_YE4FN138YkcNUc9eZsQat_j6Q7V4F_W5UmP3CARRg1IyBTCqB60YhxyvODTpmmvw4zooiImwUDlZ7r5Kazl_8rk97IuSpiUryIgoi-MyvjHJUJRHirMaNhTdzQZ4oJCDoWegkhHEYYRwgN8PKTwyU8jTWk38jf0N_5Omux7LvBA2pv6oDlfWM8Dx6dK1fJXDe-uwhWrGOzoa2R_KNdJ_9shrQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3d6a4568ee.mp4?token=VB-44vaoXYTD90SSqP0SbWyGnPlsPjAJSEbQaEfYtYevfPUxgy8NyrToqmlyR7cZXEkWlCFOU3gXDmOiWy-CfcD6bBZeNY1wIhwZTOVc5sbrkVbYoc1QiDfcIGIl_YE4FN138YkcNUc9eZsQat_j6Q7V4F_W5UmP3CARRg1IyBTCqB60YhxyvODTpmmvw4zooiImwUDlZ7r5Kazl_8rk97IuSpiUryIgoi-MyvjHJUJRHirMaNhTdzQZ4oJCDoWegkhHEYYRwgN8PKTwyU8jTWk38jf0N_5Omux7LvBA2pv6oDlfWM8Dx6dK1fJXDe-uwhWrGOzoa2R_KNdJ_9shrQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
ترامپ برای شرکت در نشست ناتو وارد ترکیه شد  @Farsna</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/farsna/447889" target="_blank">📅 15:11 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447888">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/05958b3d00.mp4?token=gLwEB5GfrtZWndpp15WkfR1-sOaL5IYlrLrhXXJyGl9SRJf7iI1oVr5kmABsrueE7F6EqGdRq6cvPgtbzizTuYZIw_TgjSa8zePiKcJi-QJZCWqNEIstVmA7IeCzQ6YO2OoKU1lX2lL2x6Oq1vaiuAVbKuNav_81L-86R4-AJ-B8lmx2nX8abRgH0hBIDYOH1OtpnxvVV8rHP6IDAV8oJP4OSJCURNdYGFFyotSxEmqb4Fzm-ZaHt8Iueu_vwPLOvX9RLshBkT-nUEqL2Fc80syUqciTBAnXmewkojABnLmQ00VrHtpzezsUpzu1vxgiF8y3KoFgnPYz84crA2UDag" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/05958b3d00.mp4?token=gLwEB5GfrtZWndpp15WkfR1-sOaL5IYlrLrhXXJyGl9SRJf7iI1oVr5kmABsrueE7F6EqGdRq6cvPgtbzizTuYZIw_TgjSa8zePiKcJi-QJZCWqNEIstVmA7IeCzQ6YO2OoKU1lX2lL2x6Oq1vaiuAVbKuNav_81L-86R4-AJ-B8lmx2nX8abRgH0hBIDYOH1OtpnxvVV8rHP6IDAV8oJP4OSJCURNdYGFFyotSxEmqb4Fzm-ZaHt8Iueu_vwPLOvX9RLshBkT-nUEqL2Fc80syUqciTBAnXmewkojABnLmQ00VrHtpzezsUpzu1vxgiF8y3KoFgnPYz84crA2UDag" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
پیکر مطهر رهبر شهید با بغض و اشک مردم ایران بدرقه شد
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/farsna/447888" target="_blank">📅 15:08 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447887">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a71d2baf61.mp4?token=MDxkYZ9PoFYkya5Yb_cxhq9BIzwusOyHvn2TeqYXJcU5GBXCLxrRK2A_wrLUMRSth5zsY5Yot7C9WAh0uybqO5uF2Lz3HnENw_bzEU4aPvXSJvCM_JkXyzo29-YjCzvfdRXCQ_2c3EigUsBLog495Zav54bU3rEPVWmoM0uNXg2vxCCgX_dXYRKkO90ms0I2g4Mm1PrBy1MEI-sCAFoAWVQ6VGwKqsFHSmDtoMsGSz1oT8T1evLvO3ufIZwRjFUlrbPfVXUURkRjYs9tWfsNyTHkn8o43YAsfad1jm-vnPul-c2J2M8upCg9TnqOM0ttvq5tPqZE4UVA03SB6sarNw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a71d2baf61.mp4?token=MDxkYZ9PoFYkya5Yb_cxhq9BIzwusOyHvn2TeqYXJcU5GBXCLxrRK2A_wrLUMRSth5zsY5Yot7C9WAh0uybqO5uF2Lz3HnENw_bzEU4aPvXSJvCM_JkXyzo29-YjCzvfdRXCQ_2c3EigUsBLog495Zav54bU3rEPVWmoM0uNXg2vxCCgX_dXYRKkO90ms0I2g4Mm1PrBy1MEI-sCAFoAWVQ6VGwKqsFHSmDtoMsGSz1oT8T1evLvO3ufIZwRjFUlrbPfVXUURkRjYs9tWfsNyTHkn8o43YAsfad1jm-vnPul-c2J2M8upCg9TnqOM0ttvq5tPqZE4UVA03SB6sarNw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
نایب‌رئیس مجلس اعلای شیعیان لبنان در سفر به تهران با عراقچی دیدار و گفت‌وگو کرد
@Farsna</div>
<div class="tg-footer">👁️ 9.89K · <a href="https://t.me/farsna/447887" target="_blank">📅 15:05 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447880">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/cbH0fx7syI_mcoSEWBX0F5pXlnd02lfI6jqKI2I7nOYpMCu2zmSJu5dy3RVyy0k-pEaQNX2wlKF5Pf5lgUWu1pGXuVpAe9smi6v-nqBeH_PTr14PdKCI9EWmvDDfetaP6g8Z56jti8H985x4PT0ggtn2tD_3ZVbIQb3seboObO-0n5Nwc6huC2g_2GvurRDEH_nZn8QfBjt29cTZAdcD0mbGyHEh40LTRssBRS6tYB8Iwp3YwVLp433sR5a-F0BfVCeyRq7lK_9ftJyRSsYvycbko5gEUc7ehkLB33v75PZNZZ9Bv3wAPWEUZtDoLILwleqzheHQkzc3-oIWDfzFLw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/mlJp0zIYalWBnwUbcB2eS70xBo1T9FNRszhZN12Jq8l29QTnUZlBuxdR7aDAm8NWTX80OA19IeaWp_Z4PaxV0Mcyf9qoNUIbS5RHOFZJEAa_ZdQr5QUyWUUpS7C5_KITfIZC0dNTDgXtNerb7xUwP6ggAP1TePhy_aILlC_vbGyKz6G38Klxsu04lWKZwnYHVcbyLflYZslG0O6rr9zun_7ksyQQdf2r-0GyQbDK9-8m1dv8OC02cdAwxXbIDwYpL34Txt1_s1OczmfXJqP4RHXQaG4o35YWTKKSnS56JB89UVM_f_SbPgyUHZJIPjlGZsMLFwwUxK-TuJNobge8pw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/mHijAYNl1YRD_tujN0jyapAe5Hq1j2IzWSbLh17tqlz4wpzyxH_Jj8Fjzg0Hnd4H4COtbC0KyggtUrioQt_407ejGsaT6eSBO9AaZRmHtdBhXT5v4DEv5Yl175HoUeGe7D5SrXcXAVQfR_ADk19IRBJWVJ9Fe-8IooMuaeMCAUEGQny1x7bhTjd39_HDPUwQxFqN1cgCdBJDEw8_N1-jml_7-rpeFDfayl6Pad0_0pnfXOz-4_9-6R7ftW0e1emOUqHBfiaJRZ_FW2mzqyHOVFBK8_t3D83KsSRMprRpIq330ZhjTaj1vgYqsyQlZXyY16LDhs8J95FSB0uge5vqaw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Yd3SvF2QadUwBCeAo_Iph66_qBzOEBD6G1qZdCmJziRkqxNNyzrzEjuM4JVg5rSkuMW2lBKOZpdzXmYxInM4s61ou4TMRa8wH8h54tONuMbsKi-gmP0qQqXSsYpsKxR0IXfSi1mF0zIRnhE4u3rSfUKkW3UwtLE6BZ2OfL-MK5BhRdRNJoGbEDufhkT4MZSnrWJfYgB94Z71nMOVi_1Ui8bbSXvO0MLXZoBpnqGbncBcpKztp8Z_f5eDQ6RClIYl1YhC01FhMq5PGsfWqk5y3EtFFf_PEJI9Rv2DBfFF9tefNPtCy_NpxrTU4_TJLmpzA2eokC5AGNPGpgANtkLeUQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/MHotbM_kIqP6gZZeUx7Thpptzsxw6wcNVERssO2z2M4_6PvvI3CfetmriM4KtA_wc-mlQ_EWedhkrlWpiPpAf4JTLCWgRunUTfg_jzZrY4I6sx9QLv0y5v7pcVWqpMMWu3tuWw7_ikjRPkYFP3UoXRuNmnojeoETq3MzJsil3keYw3f7XsaKzhkpVP9PQXI1f5HXJjzbl5gDztE4WSanGnC_Dw2iGn7BiwivFEWGlPXxC8EP4NzCz6Xv5o48jPXaRc8oBi0Co0A09aApB9SYqGZ4aFj73dr-K_hxq1jQ4QW8mpmUtEF8ogcrVk4PftjQrN-nrBQ-0ggzOdpzMWJqNw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/h3cSgF54t-bIm98IadSjceP04pXIGmNsvlVQqL26gCETatrpZrBEgNdn6tBoUhNYq2R90L-JdIFiDduSCqkkh2vFUstfxWGn_pEZE44dRKbvPFhoTEp-fSDIMMTJCSOujDhlFIRBu_s7keoSPsPUaNFmxLey1p6yt8v7SsDMD3fK09FARl_l68ziVVS4qNBnrqiA-4XTOGcBYe1ycS3GIKqT4nZWbOE3wavls9lF9m3MRsXshE2yGlF7vycFsubop0XpptMn8SyIGRN9s5XjS0WizxSKBiw400nhpKul8k8ipbazot0lE7kHpax8MiQ64zkS2M877Qsq2Gkl2ZvV3w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/J_iAj2Q6v_2MJup9OEc_9SsFyloeU0L8k6JUrxZspO_HBsPrzBEJDU6740SlkLS8DpYila2FJ5e8NKoiLMdTaMmzo7LbAXxxwf1Dqn4oCKOFwCsXQdbSzJ2a0ED6LAPjpC83LxhWI00OdBquoxjNuGhfHGHyZCaSokLmCXRbWsmgG9rAP1vch8WPd4aaPAWFFrYbkWmSle0J-qdt7B7nQuWL3R0JPjvsrcowTp9w-Ub78a6ck7hUDcRfSi-Huo8jlLy489nTB3wtK-0GZcQx57N7MzFEbWc3sTDVKGPrHb-QFHF5-5FjYyq-tPXx_Qzgqm-jPvBnKWqLGRx1I_Fuhw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
نشست رسانه‌ای مهمانان خارجی تشییع
رهبر شهید
عکس:
زینب حمزه‌لویی
@Farsna</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/farsna/447880" target="_blank">📅 15:01 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447879">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bbbb7123ed.mp4?token=gOpoA2lvJwwP8U9pa-utnwPiKuJjqcxYpzWx_DjZlIZ64HVrJUpmTYBJYLoD4x5ZDzypBF5r41SlOoOL9UOL6_PM0KqIKnPiIwhVg-0PE4XIZaEE3eHsdLz8JyKMZeX64n7PV9yjchL47Bbk6u5OwYemYOPoSmfVCIwhieu3dHFOxGdwPR_3Dj5PnwlwN0Jdc_Vj_trO_1tZuST9sggjh6T9emSDNcy4ZLQNv5-nzONzF2hVqIdYlcnzYg0tUvcTtAUBO43KbaUshnCmwCG1j9019A2PoMe_O-bkcp5txhi9W_hUOASvnsIGYVPqat7HA-_tFOn5s2DP0Ule4kXQm0Dk1ILOlBllpAjldi2cWgHCizp2JZIDim-Pu6Jv5C5z3UZlOQLIOD8J8Ve5b-xTwbIWeUaPq-qDOOuAAvkUw9xEccSv17Eff_4rv58BUQQHy2SyLVyxxKSJrw0kziwSOmTuAS6GvCzokGOxlt82AE1BoweEzr6U_kxkAu87FRv4D3GQstBu_lw6zwKtGcZU9b04FEt2TLeXC30O_nYZNnko6QWG_PJs8kLPY4UDCGbYxXioPhsTjGZPrcRWgMIXipraElMjaWiTeXqC7QiHzHU2dlzAZsgyFweUQ1LigCVzVr0-oi4fWlBlDGdZVIb-mY21ZWKmWzkQeldlVqmAn00" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bbbb7123ed.mp4?token=gOpoA2lvJwwP8U9pa-utnwPiKuJjqcxYpzWx_DjZlIZ64HVrJUpmTYBJYLoD4x5ZDzypBF5r41SlOoOL9UOL6_PM0KqIKnPiIwhVg-0PE4XIZaEE3eHsdLz8JyKMZeX64n7PV9yjchL47Bbk6u5OwYemYOPoSmfVCIwhieu3dHFOxGdwPR_3Dj5PnwlwN0Jdc_Vj_trO_1tZuST9sggjh6T9emSDNcy4ZLQNv5-nzONzF2hVqIdYlcnzYg0tUvcTtAUBO43KbaUshnCmwCG1j9019A2PoMe_O-bkcp5txhi9W_hUOASvnsIGYVPqat7HA-_tFOn5s2DP0Ule4kXQm0Dk1ILOlBllpAjldi2cWgHCizp2JZIDim-Pu6Jv5C5z3UZlOQLIOD8J8Ve5b-xTwbIWeUaPq-qDOOuAAvkUw9xEccSv17Eff_4rv58BUQQHy2SyLVyxxKSJrw0kziwSOmTuAS6GvCzokGOxlt82AE1BoweEzr6U_kxkAu87FRv4D3GQstBu_lw6zwKtGcZU9b04FEt2TLeXC30O_nYZNnko6QWG_PJs8kLPY4UDCGbYxXioPhsTjGZPrcRWgMIXipraElMjaWiTeXqC7QiHzHU2dlzAZsgyFweUQ1LigCVzVr0-oi4fWlBlDGdZVIb-mY21ZWKmWzkQeldlVqmAn00" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📽
خدمت رسانی بیمارستان سیار برکت در چهلسرا به زوار آقای شهید
ایران
@Farsna</div>
<div class="tg-footer">👁️ 9.12K · <a href="https://t.me/farsna/447879" target="_blank">📅 15:00 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447878">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromدرگاه فرهنگ</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7b651a243a.mp4?token=sDeaMYeFkeOJr9ZJgakFx_xpzhTh2jnrTzG2aQI4Ln1TsmAsHal7CAJOqLRpVi6V7dBXqpIgyjbmkes3qcyy_yrc9rrXvZPiUFqX08aGMpKndxdQTX60oPsSEnY9nC1k5Z4QolvUGoBQIsZbJEGzjKRYKQu7QsVP8M2ZzW9FoIrjxkvcxx9bXZW_gNx5_XRt3MxAaA6F7u4eXXAHJQ5XLbr0CiyZZ45RNAWWl8YnQKfwnRoh6exXnstsiOc2IkBTDeUdafHH4idmWhXQhMO_TZWAVP_2zVJI0sT5iWX0drJnTWkGj1mFbMI1ZWJx8KxN8tW-vdkroQvSwWuCtoyFvAhaFEOKdQSbK8kFIJstIqzuxxugXwJ5iIAag8AoC2k-8bMycMEny80iLPeUVui7vy_GoIDVGu_W65hHj9s1beqxb8kNGuC6-TZqa0PUqH6TTGyCZ44vYr6E_2CY0yQgpd78oonJcgzOXt72RFzvhgSrHYREP8_V1YHu8SDRyFU6PFGpMMry1gqNRKo1GXzgXdWuOkUFaYSRfVyPlGrF_WuTNOaa46rrHqwCjpc9xphFm-auBSVjnzNQ2x1Lx8U7lgGPltz6kY-aUQcIOOEJTdTK5ZG8Tp6li48WE-ye_33zrYiRrXH-VQl-Zw9w75yYzVnZHZZiTwI_Yzeh5VwCMyo" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7b651a243a.mp4?token=sDeaMYeFkeOJr9ZJgakFx_xpzhTh2jnrTzG2aQI4Ln1TsmAsHal7CAJOqLRpVi6V7dBXqpIgyjbmkes3qcyy_yrc9rrXvZPiUFqX08aGMpKndxdQTX60oPsSEnY9nC1k5Z4QolvUGoBQIsZbJEGzjKRYKQu7QsVP8M2ZzW9FoIrjxkvcxx9bXZW_gNx5_XRt3MxAaA6F7u4eXXAHJQ5XLbr0CiyZZ45RNAWWl8YnQKfwnRoh6exXnstsiOc2IkBTDeUdafHH4idmWhXQhMO_TZWAVP_2zVJI0sT5iWX0drJnTWkGj1mFbMI1ZWJx8KxN8tW-vdkroQvSwWuCtoyFvAhaFEOKdQSbK8kFIJstIqzuxxugXwJ5iIAag8AoC2k-8bMycMEny80iLPeUVui7vy_GoIDVGu_W65hHj9s1beqxb8kNGuC6-TZqa0PUqH6TTGyCZ44vYr6E_2CY0yQgpd78oonJcgzOXt72RFzvhgSrHYREP8_V1YHu8SDRyFU6PFGpMMry1gqNRKo1GXzgXdWuOkUFaYSRfVyPlGrF_WuTNOaa46rrHqwCjpc9xphFm-auBSVjnzNQ2x1Lx8U7lgGPltz6kY-aUQcIOOEJTdTK5ZG8Tp6li48WE-ye_33zrYiRrXH-VQl-Zw9w75yYzVnZHZZiTwI_Yzeh5VwCMyo" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">طنین اذان در لحظه ورود؛ گویی آسمان هم به استقبال رهبر شهید آمده بود
🏴
آخرین ورود به میدان آزادی
#باید_برخاست
#یالثارات_الحسین
@dargah_farhang</div>
<div class="tg-footer">👁️ 8.64K · <a href="https://t.me/farsna/447878" target="_blank">📅 14:59 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447877">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-footer">👁️ 9.51K · <a href="https://t.me/farsna/447877" target="_blank">📅 14:59 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447876">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">مازندران فردا تعطیل شد
🔹
استاندار مازندران:‌ در راستای تسهیل تردد زائران برای حضور گسترده در تشییع رهبر شهید، کلیهٔ ادارات، دستگاه‌های اجرایی، مراکز آموزشی و دانشگاه‌های استان به استثنای شعب بانک‌ها و دستگاه‌های خدمات‌رسان فردا تعطیل است. @Farsna - Link</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/farsna/447876" target="_blank">📅 14:54 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447874">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/I5fZDTANAZ1pBoe-4f7B6t9XxYH0O62TRGcNI6XCKx324PHKhL_m08QrG6StqsKzhlvu_7HMrqCHt3kjp7q5v8RL2XZBx0lkqmc_yjfqD3O0A0nuRKl1LB9ZBmIr88lFAyfkrfDmurUTh2vUP0TaLlV9WM5gWFQRJxY-jSp_2tfVk9qSc3FnqE9IFK201pOpVrU7jSPvf2jmjUoQdp2bZ9UjWHOxT6Y3szMDX7MlT460lgt_rjHBOFdnC7FB8FmkBz6zznqL0VCM7W8XAVpqxcFbpWkYZ35pQ5GdlIr6wpA16BZoFTuvl4nULNQSo_edWTi75x4xzMZtC20KaKQxTA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
عمامهٔ مشکی‌ات ماندگار شد ای آقای شهید ایران...
@Farsna</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/farsna/447874" target="_blank">📅 14:39 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447873">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/326861d6c8.mp4?token=LICzIv5OWNmVLRf9HM3maA331QKp2Sh_EX1pz84TwhmsOE7d68BSxubfHj5-1NCsyA0Bg8rpRRcWXVqcjUEbglk7hzrTo0Uw3alBS5cLoVuAg_sXMwVd4Xuhc3PxtDEYgCTGLhjTSS-zd29XCtX_MGIHeELi-TxdTMZMXauxQJUIULAD_PBd4ZLDVmVmK-r4_GvOR7K8xBZpSZ0gz8fYv4CHZVh9Z33JXRJB57Z4Z8qhUDzw0xWHAk3lU0giQay9yZhKqaSTGCXmFjXeUNx4-zT_-ahg5Yu48ivrex55dT25hnHWV-EzfvEbZ-GSQZqBM9MFf6CLGz55EY-2W7tQJQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/326861d6c8.mp4?token=LICzIv5OWNmVLRf9HM3maA331QKp2Sh_EX1pz84TwhmsOE7d68BSxubfHj5-1NCsyA0Bg8rpRRcWXVqcjUEbglk7hzrTo0Uw3alBS5cLoVuAg_sXMwVd4Xuhc3PxtDEYgCTGLhjTSS-zd29XCtX_MGIHeELi-TxdTMZMXauxQJUIULAD_PBd4ZLDVmVmK-r4_GvOR7K8xBZpSZ0gz8fYv4CHZVh9Z33JXRJB57Z4Z8qhUDzw0xWHAk3lU0giQay9yZhKqaSTGCXmFjXeUNx4-zT_-ahg5Yu48ivrex55dT25hnHWV-EzfvEbZ-GSQZqBM9MFf6CLGz55EY-2W7tQJQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
تصاویر هوایی از موج جمعیت در تشییع رهبر شهید در قم
@Farsna</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/farsna/447873" target="_blank">📅 14:13 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447872">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cc22eef9fd.mp4?token=D5WSUTYLlPFcQw5N9AvRYsIMVo4AGMH1aFdVaNxKubDRaQAnhgYtqejMNWXNmQkBT5mrKqNQ0NB3CVLjNARnUo_kzhLZePRb9VZbVkA32k9J8Xsmm5NRcLgQczaK4XSIaK-OXXvRE6Z4nNTbXkykxlNB6dJZYuORhEXstKbpTwdOPGlCW07ejM6obYnLmKNLAbjWD4XP_LZRNNrb0NNyZzDC6SZsdC9ozCygJCYE0J5paBu7OxF3mL8sp-2fuq8_mmyCtAlO9PFYLOn8RT9M2CxiTfFJc9IKDm4Vccje59RAmzi4v15S_o1ad2wCzwVC8NiaQPutUSUgm-3P0kRwAg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cc22eef9fd.mp4?token=D5WSUTYLlPFcQw5N9AvRYsIMVo4AGMH1aFdVaNxKubDRaQAnhgYtqejMNWXNmQkBT5mrKqNQ0NB3CVLjNARnUo_kzhLZePRb9VZbVkA32k9J8Xsmm5NRcLgQczaK4XSIaK-OXXvRE6Z4nNTbXkykxlNB6dJZYuORhEXstKbpTwdOPGlCW07ejM6obYnLmKNLAbjWD4XP_LZRNNrb0NNyZzDC6SZsdC9ozCygJCYE0J5paBu7OxF3mL8sp-2fuq8_mmyCtAlO9PFYLOn8RT9M2CxiTfFJc9IKDm4Vccje59RAmzi4v15S_o1ad2wCzwVC8NiaQPutUSUgm-3P0kRwAg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
ترامپ برای شرکت در نشست ناتو وارد ترکیه شد
@Farsna</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/farsna/447872" target="_blank">📅 14:13 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447870">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ff6481e194.mp4?token=FLZVXlA7Gi0NW3HCARSryjNOnYykskUO8RRORMw8-KhlCNxJhIxF7Z5oxffcaodJGfQhMJb-DeHV838DbhzN7S2LkcPaqtnp_ZpFHwTw388siMtzqWSpajJxUVnr1RagzAYa_grKORkR4mjCJK6zir79QZ6fCkEoR16hmOVe7wKLlxvaFb6K38_J8TYqQcr50olwfM3StQ0dYW3tMELYdSrUoiUhl36-h7VrGNn96L0UUfHC5uImYIRHYcSmDjYxnjBOrgsrFrv0P4_YaL0OA8x7iFtxbbhRoTerwU_05EgJUHiPeauvXwiLiMpGPpZsO-4YKC-C8Nssqnx7pd2yfF2nXFsqf_o5vlaw0bEn_UPL66Q-zlTAbV8zufT5s8dL-xlwG13SybPwKJU9DyzxYSmpuZELVVajlV4nUIuTR_87dIBp4A2np590jBwAt8UM-BLCZtUoCAW1zXaCsrDKgVAyLMkee7LJv_9yWh_iPUNLmHPeNeXP8lHVzRCyh7W8127HjXzFdevIwxhMU5Ay4AIIAwucFjIX3FT7Va_v4UfQ5c1zC1dbAWBZpklrDaYARvKDQ0vOw4uFiB-3tdl6QHkv_niY-sN0vFrz70KU5naq-PvRN7Wove9tpp9KmRT4fi8GS8rlgrU7M6f-c8qdg35KwtiYgQUrvqitudSpETA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ff6481e194.mp4?token=FLZVXlA7Gi0NW3HCARSryjNOnYykskUO8RRORMw8-KhlCNxJhIxF7Z5oxffcaodJGfQhMJb-DeHV838DbhzN7S2LkcPaqtnp_ZpFHwTw388siMtzqWSpajJxUVnr1RagzAYa_grKORkR4mjCJK6zir79QZ6fCkEoR16hmOVe7wKLlxvaFb6K38_J8TYqQcr50olwfM3StQ0dYW3tMELYdSrUoiUhl36-h7VrGNn96L0UUfHC5uImYIRHYcSmDjYxnjBOrgsrFrv0P4_YaL0OA8x7iFtxbbhRoTerwU_05EgJUHiPeauvXwiLiMpGPpZsO-4YKC-C8Nssqnx7pd2yfF2nXFsqf_o5vlaw0bEn_UPL66Q-zlTAbV8zufT5s8dL-xlwG13SybPwKJU9DyzxYSmpuZELVVajlV4nUIuTR_87dIBp4A2np590jBwAt8UM-BLCZtUoCAW1zXaCsrDKgVAyLMkee7LJv_9yWh_iPUNLmHPeNeXP8lHVzRCyh7W8127HjXzFdevIwxhMU5Ay4AIIAwucFjIX3FT7Va_v4UfQ5c1zC1dbAWBZpklrDaYARvKDQ0vOw4uFiB-3tdl6QHkv_niY-sN0vFrz70KU5naq-PvRN7Wove9tpp9KmRT4fi8GS8rlgrU7M6f-c8qdg35KwtiYgQUrvqitudSpETA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
یک محله در مشهد برای تشییع رهبر شهید پای‌کار اسکان زائران آمد
🔹
در آستانۀ مراسم تشییع رهبر شهید در مشهد، اهالی شهرک شهید رجایی با راه‌اندازی پویشی خودجوش، برای میزبانی از زائران پای‌کار آمدند.
🔹
ساکنان این محله تاکنون بیش از ۳۰۰ پتو و دیگر اقلام مورد نیاز را برای تجهیز محل‌های اسکان زائران جمع‌آوری کرده‌اند تا سهمی در میزبانی شایسته از شرکت‌کنندگان در این مراسم بزرگ داشته باشند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/farsna/447870" target="_blank">📅 14:07 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447869">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">فرودگاه بوشهر از شنبه بازگشایی می‌شود
🔹
مدیرکل فرودگاه‌های بوشهر: نخستین پرواز فرودگاه بوشهر پس از وقفهٔ ۴ ماهه روز شنبه توسط شرکت هواپیمایی ساها انجام می‌شود.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/farsna/447869" target="_blank">📅 14:05 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447868">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">مازندران فردا تعطیل شد
🔹
استاندار مازندران:‌ در راستای تسهیل تردد زائران برای حضور گسترده در تشییع رهبر شهید، کلیهٔ ادارات، دستگاه‌های اجرایی، مراکز آموزشی و دانشگاه‌های استان به استثنای شعب بانک‌ها و دستگاه‌های خدمات‌رسان فردا تعطیل است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/farsna/447868" target="_blank">📅 13:52 · 16 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>

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
<img src="https://cdn4.telesco.pe/file/Xv_Fisb2B9Gc4S4juiSUqUljC5omq2RpA4QBEO3OEyqu2DKfYoX3KieZ8feykro9bJ_cBkDhA-ZLBcoWTYTS0lMjMoN0vlYMoEkj8Q1uXdZdQoszwpF4y_WuvRoXC9roPbm463h6AQEwbnEdGMsVIqmAItV6jaHSrKqL-uF3Uo_V3kLTU5SWGhaoO03DQpFID-UUMN11FZNIB6t2Wh26RByFnMJwUnDYRJfGsfGI2wgMbhQP_ApVIuBNpukjNOo4TBI66Vi_z5nJjacRxQka0sCar-j8wHleS4LnlR1RSmAK0_Ihn4kIGC_0vDmGZqZhGSb5f43_b1c8Tqtt45sT1g.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرگزاری فارس</h1>
<p>@farsna • 👥 1.82M عضو</p>
<a href="https://t.me/farsna" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 حقیقت روشن می‌شود‌‌تبلیغات@Farsnews_adsارتباط@FarsNewsفارس‌پلاس@Fars_Plus‌ورزش@SportFarsجهان@FarsNewsIntعکس@FarsImagesپیام‌رسان‌ها@Farsnaاینستاگرامinstagram.com/fars_newsتوییترtwitter.com/FarsNews_Agency</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-26 15:17:21</div>
<hr>

<div class="tg-post" id="msg-456557">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GuQVOtZ47_bmo0rN2_USpxlLvhyyYDwbeybrrRzmutdtP9x4tvK0tw1Df4GmmsFSqu9mLu1_D9TIAoi4T579G27ztIHr9LfM31gNrQ_W_0PnJq6EZdY8wHbDmG8L5YAjWIMovrPwrX2-Tds5GqtdaLKqhp3sebENK756AhWXa92XsX-vBdpMzXrhvE-o1UvN0-shKC-BPU_bEQ0JxGAXsDv__FCUbt772ZQNqoUoNIVEbpB09k4Cxhv7jKgJW_eGGoXqOOyZyXHjVcuSNovFcl3hK_xqDReRbq1HueudwjjR61m-KgijpZmpYhEgO6ezYNVhn_SyFT99RjiMvsKHyQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دانیال ایری با عقد قراردادی ۴+۱ ساله به پرسپولیس پیوست
@Farsna</div>
<div class="tg-footer">👁️ 207 · <a href="https://t.me/farsna/456557" target="_blank">📅 15:18 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456556">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/630026d9ce.mp4?token=A75J10k6m_gyLGm2R1HL2f8zLb4lfUY9hEq-zjKGPBuwoj5fTxE_RK9pnKWu6FwfI0McCGDLgXNGG4b5cgQo8Y4ltyo9L_IKstzraXF_18SafLdTDlfOu5iKd6yJOspTFn92WPAhbOxb9KkFG7YMVRsQPR2zNg_gom4lEAvE_aZNC5lBLAtYVZl61emZd6_UihP5l2KIqu-ObL3LEmjXmbXCI6kj972sWM3NcbemJRLmA44VgvNoei9X2ra1LHzwFTXQEUYT9J8x8rh5o6gdU1hCrw6ovUt5b1pyifYoSaUAVr9MR8xfhG3MGXAI3TX6_bcPls_XZGGC2kjg3_4PEw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/630026d9ce.mp4?token=A75J10k6m_gyLGm2R1HL2f8zLb4lfUY9hEq-zjKGPBuwoj5fTxE_RK9pnKWu6FwfI0McCGDLgXNGG4b5cgQo8Y4ltyo9L_IKstzraXF_18SafLdTDlfOu5iKd6yJOspTFn92WPAhbOxb9KkFG7YMVRsQPR2zNg_gom4lEAvE_aZNC5lBLAtYVZl61emZd6_UihP5l2KIqu-ObL3LEmjXmbXCI6kj972sWM3NcbemJRLmA44VgvNoei9X2ra1LHzwFTXQEUYT9J8x8rh5o6gdU1hCrw6ovUt5b1pyifYoSaUAVr9MR8xfhG3MGXAI3TX6_bcPls_XZGGC2kjg3_4PEw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سبوس</div>
<div class="tg-footer">👁️ 909 · <a href="https://t.me/farsna/456556" target="_blank">📅 15:14 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456555">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ae7bcb0b00.mp4?token=D2Ck_IJdWSjbQUHBhe3KHjMr2QgIBJ8I9wnNyByTV3JE5AJ9qrNrqhtzF2Do74l8SDyA21R09nV6sFG6aRfJQ4ZZn09jl-0wkhFFbos9opnHBTTM7ijfkmUQgn--xsj31Of1bXNU7fG3M92OPOZHY0kOId53rdHeQw6UHVNwi7UUqbENtwypowtUHc1H5DvX90_BkgZ6GE82aiIeOtAsNRnR9-0bR9JnvOgntOJXREZbXJz9KUXIaU5y0sbRsF0tcPyQm5M04cJ-oo35ZwEzsOcxIhT5-uv3JeFI8b45f1gKypcRIvh32FC_qzzq8fpUSojuYhx1N2wpGvF_3fIi3Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ae7bcb0b00.mp4?token=D2Ck_IJdWSjbQUHBhe3KHjMr2QgIBJ8I9wnNyByTV3JE5AJ9qrNrqhtzF2Do74l8SDyA21R09nV6sFG6aRfJQ4ZZn09jl-0wkhFFbos9opnHBTTM7ijfkmUQgn--xsj31Of1bXNU7fG3M92OPOZHY0kOId53rdHeQw6UHVNwi7UUqbENtwypowtUHc1H5DvX90_BkgZ6GE82aiIeOtAsNRnR9-0bR9JnvOgntOJXREZbXJz9KUXIaU5y0sbRsF0tcPyQm5M04cJ-oo35ZwEzsOcxIhT5-uv3JeFI8b45f1gKypcRIvh32FC_qzzq8fpUSojuYhx1N2wpGvF_3fIi3Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
رکورد زدیم؛ البته در کاهش زادوولد!
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 3.65K · <a href="https://t.me/farsna/456555" target="_blank">📅 14:45 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456554">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AYhaAuWt7pwMcoK7bdgvPJevdp512JOcDip6FQa7J7uC2j-38mkwujOJZd2ou0aCSCtegROIO9dwcDcTFiDA96PF9-UgaPCRQVpKOdttp8CWk00YOi2BQTMJZBe8oPyfWMsdSwpTjF07EZCbyAxnUApnDj2nNR-Kn4FIB04QwnhajkGK3V-8ZpDTKx3k7-IH-ZCYrwjXa0kc8JKY27uLRAWdlFPG58iOnM1CyJWAh2urohSljxLoo5LzQ3atsy3Qn2EYcVmYlyAQn0Ea1tVqTaJJMLu315QSLZDWWxDG_vT8S6AlxNlAFJFvmcv5JOqcf2t-moU20B-nLnRy1OziwQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هدف نخست ترامپ از جنگ با ایران: بازگشت به قبل از جنگ!
🔹
جی‌دی‌ونس، معاون رئیس‌جمهور آمریکا در مصاحبه با فاکس‌نیوز گفته که نخستین هدف کنونی دولت ترامپ، حتی قبل از توافق هسته‌ای با ایران پایین آوردن قیمت نفت و بنزین است.
🔹
چندماه قبل‌تر سخنان مارکو روبیو،…</div>
<div class="tg-footer">👁️ 4.14K · <a href="https://t.me/farsna/456554" target="_blank">📅 14:41 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456553">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفالس نیوز</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/900d69e35d.mp4?token=uF5lKF8DGtCFy0dKucdmhsnD7BddTdzfK9sWhCBEhmPfjBYsNLJhj0qcKERDZvb_cgyBkFu56tx3dIUaV-40qc2iLB4msWjU8xh4tmTUX6W-2hL7sQ2ovMTB8JY9zTybo2UKnUq1qVGOwnNaX-GOsprYUmj9qGYt2TQEbiPpkZ7nf7u5K_8VSldwm_ebc7iQtf8HONMVDAapcaw58SrXNCN1C95qAUYKI8khOSW8k-77-4vlAx6Ksj8r7j8iSDxcvap2s3szhqi5dCZFEcQKzOMAR4rMuVhPO-FzWFD20_X4ci_pyTzopvcvg6aVaW8GmskqZvyM0tugJuOnzvxhyg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/900d69e35d.mp4?token=uF5lKF8DGtCFy0dKucdmhsnD7BddTdzfK9sWhCBEhmPfjBYsNLJhj0qcKERDZvb_cgyBkFu56tx3dIUaV-40qc2iLB4msWjU8xh4tmTUX6W-2hL7sQ2ovMTB8JY9zTybo2UKnUq1qVGOwnNaX-GOsprYUmj9qGYt2TQEbiPpkZ7nf7u5K_8VSldwm_ebc7iQtf8HONMVDAapcaw58SrXNCN1C95qAUYKI8khOSW8k-77-4vlAx6Ksj8r7j8iSDxcvap2s3szhqi5dCZFEcQKzOMAR4rMuVhPO-FzWFD20_X4ci_pyTzopvcvg6aVaW8GmskqZvyM0tugJuOnzvxhyg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تقطیع صحبت‌های مجری صداوسیما دربارۀ «جنوب ایران»
🔹
به‌تازگی ویدیویی در فضای مجازی منتشر و ادعا شده است که مجری صداوسیما در آن می‌گوید: «جنوب ایران فدای جنوب لبنان».
🔸
اما نسخۀ کامل ویدیو نشان می‌دهد این عبارت، نقل‌قول از وطن‌فروشانی بوده که پس از حملۀ آمریکا به مدرسۀ شجره طیبه میناب در هرمزگان، از این حمله ابراز شادی کردند، اما بعد از حملات آمریکا به جنوب ایران، خود را دلسوز مردم این منطقه نشان دادند.
@Fals_News
-
Link</div>
<div class="tg-footer">👁️ 4.21K · <a href="https://t.me/farsna/456553" target="_blank">📅 14:35 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456552">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">‌ سرلشکر ایزدی: در جنگ اخیر بیش از ۲۰۰ هواگرد دشمن ساقط شد
🔹
جانشین فرمانده‌کل سپاه: در جنگ اخیر نه تنها ایران اسلامی تجزیه نشد و خدشه‌ای به نظام اسلامی وارد نشد بلکه خود را قوی‌تر و استوارتر به دنیا نشان داد
🔹
بزرگ‌ترین قدرت نظامی جهان و قدرت نظامی منطقه…</div>
<div class="tg-footer">👁️ 4.27K · <a href="https://t.me/farsna/456552" target="_blank">📅 14:33 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456550">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7bc20e07ba.mp4?token=Xij-WEtjC0mRH8sK0FYQo166OfbDJsCHit2-fZT6HX8BlQ2gJyAFM4sdk75oNwetn7G98hVbpCPQcu_INaD-RxmSnm2IoauANhmsU4CXaU0DFhjAtFKkatJHSsovXnawPGY53nQsQCRWBbKk6Mv8dhozuvI_BXxtUsj0gLR_o3CW4qxVVYz0Ev-EjO4c5Ll1qyk-RtOwFrlHKI_5-g9ejrswrJn3ENKAk3pahGKxrSfZkASYTTYTlJu4-W9T5OeNboTF-kTNxW7FtznlUpQ7cHESQ6jamnJCMmz5MBPoXMXNpsLHbC3J6YJHzSzfgw4hTpAJPJnKvn9GUggexcPnCQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7bc20e07ba.mp4?token=Xij-WEtjC0mRH8sK0FYQo166OfbDJsCHit2-fZT6HX8BlQ2gJyAFM4sdk75oNwetn7G98hVbpCPQcu_INaD-RxmSnm2IoauANhmsU4CXaU0DFhjAtFKkatJHSsovXnawPGY53nQsQCRWBbKk6Mv8dhozuvI_BXxtUsj0gLR_o3CW4qxVVYz0Ev-EjO4c5Ll1qyk-RtOwFrlHKI_5-g9ejrswrJn3ENKAk3pahGKxrSfZkASYTTYTlJu4-W9T5OeNboTF-kTNxW7FtznlUpQ7cHESQ6jamnJCMmz5MBPoXMXNpsLHbC3J6YJHzSzfgw4hTpAJPJnKvn9GUggexcPnCQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بلاگری که به مقدسات توهین کرده بود  دستگیر شد
🔹
قوه‌قضائیه: درپی انتشار ویدیویی توهین‌آمیز در فضای مجازی از سوی یک زن بلاگر، با دستور مقام قضایی متهم شناسایی و دستگیر شد.
🔹
برای این فرد پروندۀ قضایی تشکیل شده و درحال رسیدگی است. @Farsna</div>
<div class="tg-footer">👁️ 5.51K · <a href="https://t.me/farsna/456550" target="_blank">📅 14:14 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456549">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EtBn22awwS49YkMmrTx15qlcZxCYo8q1OBXzzCU-EdwcokM3Jwd0Hc4TKIEFJeo7WwHKrjX2iYKrhH1V2bW6jnnuNBcxCwO2zexV07eLhlX4JYz0oAkH5aP9oxRBonViyCW6OlNHEjVdLWqc-jcwSBrt18X1QIj8eo2BiGFmptnZ71C9rfZeYkAtbYj1JmafGAoVhSQUrK2_aO7JmPlCoTPoEygf-Z0u7dVjCk6Md_q7V0n6t9KqMGWgjuiRcLPz3JRGG1o46istE4j5Rb-ccU4Z96MRMmjq6qsCJG5_DnEHIFXJnHHC92gL8a18kaBHVnY4iN59kboWGkF4Ktz4nA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ولایتی: معادلات منطقه تغییر کرده و امروز خانوادۀ آمریکایی هزینۀ قمار سردمدارانش را نقداً می‌دهد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 5.86K · <a href="https://t.me/farsna/456549" target="_blank">📅 14:05 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456548">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">🎥
رئیس سازمان بهینه‌سازی: خودروسازهای داخلی هیچ‌وقت هزینۀ خودروی پرمصرف و بی‌کیفیت‌شان را نداده‌اند، فقط مردم و بیت‌المال این هزینه را می‌دهند؛ ما باید ریشۀ این موضوع را بخشکانیم.  @Farsna</div>
<div class="tg-footer">👁️ 5.96K · <a href="https://t.me/farsna/456548" target="_blank">📅 14:00 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456547">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MTdWhUon7zjVpwptMHh1QekQnrzwjNVQ3CeotzK6ed48PxhZ28PunqFRuWODhH0YmMBwGj64QXYFbZSJ5m8ovod2QBZGxJrkPSkugbEtzdHRSHBhxtgTuSFoe77UDLtSZdaQ3cPhX3zYhqR1aHRgq82GuYL1vnP80ajrXVIfp_4dVfHgpNf6NgC_O0wKUrZMHTBxxJ5p78Bp94EXiB4FgO2XgHxcMZ5j-q1vXIDaO-eddY2yLyfeCMou_RJpfCqjGr640DVMnWt6r10EV1wAxaxo_1ZQ2BgLHNT-m_PH5HeMFspFrD7JRH5b8KS1YQJ95eRHIbd2Hv85sTClJnvPgg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سخنگوی سپاه: رسانه‌ها در جنگ اخیر
پیوند خیابان، میدان و دیپلماسی را ساختند
🔹
امروز رسانه‌های ما به‌راحتی توانستند عرصۀ جنگ را شناسایی کنند و جنگ را علاوه‌بر عرصۀ زمینی، به عرصۀ اذهان بکشانند و اجازه ندهند دشمن در عرصۀ ذهن‌ها تصرف کند و یک جنگ ذهنی و جنگ ادراکی را شکل دهد و بتواند ادراک جامعه را مدیریت کند.
🔹
رسانه امروز علاوه‌بر روایت‌گری و واقع‌نمایی، واقع‌سازی می‌کند. رسانه امروز بخشی از جنگ و بخشی از سازوکار جنگ است.
🔹
در جنگ اخیر رسانه‌ها به خوبی توانستند رابطۀ بین خیابان، میدان و دیپلماسی را برقرار کنند و این رابطه را در اذهان مردم و جامعه تثبیت کنند و از هرگونه رخنه برای تفرقه‌افکنی مراقبت کنند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 6.71K · <a href="https://t.me/farsna/456547" target="_blank">📅 13:48 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456546">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">جانشین فرمانده‌کل سپاه: ملت ایران دستاورد ۳۵ سالۀ دشمن را خاکستر کرد
🔹
سرلشکر ایزدی: بعد از فراز جنگ رمضان یک وضعیت بدیع و جدیدی را در صحنۀ جهانی منطقه‌ای و حتی کشورمان ملاحظه می‌کنیم.
🔹
به عبارتی ما در این فرازی که نقطۀ عطف آن شهادت جانسوز قائد امت بود با…</div>
<div class="tg-footer">👁️ 7.51K · <a href="https://t.me/farsna/456546" target="_blank">📅 13:21 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456545">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/488dfc14ab.mp4?token=ACVbCR7PFT56NRwNdqtEpqImpwv8Y_llKH9o67G7avMyvq38mPQ6VUfJEht91GQEXdIUr0PKk__UZOPCWmc2S__J1ITeyzp9X19-24vMgo7N_xnv3yLKK1mOsxXOO_v5z-LEjITQGTJi1V6hjjbPkYJkOA_sFyYD9BU1Ma88iHbVFRCuYY3kmtEehrocZjA5ca7O1FhLvaCrXjzI78oXIGAlM2hiDVjVK2YYpKuc3dVNy8J4HDJnLh_CB3_7926YIi7vBKsWoIjhxD2CpvoQ4FXJ8SZPE0oiEVjJJBT2eDmU-GnT1vN5isIWB3MX2K6G-N6tFKYVKdBAYiyVlBsmtg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/488dfc14ab.mp4?token=ACVbCR7PFT56NRwNdqtEpqImpwv8Y_llKH9o67G7avMyvq38mPQ6VUfJEht91GQEXdIUr0PKk__UZOPCWmc2S__J1ITeyzp9X19-24vMgo7N_xnv3yLKK1mOsxXOO_v5z-LEjITQGTJi1V6hjjbPkYJkOA_sFyYD9BU1Ma88iHbVFRCuYY3kmtEehrocZjA5ca7O1FhLvaCrXjzI78oXIGAlM2hiDVjVK2YYpKuc3dVNy8J4HDJnLh_CB3_7926YIi7vBKsWoIjhxD2CpvoQ4FXJ8SZPE0oiEVjJJBT2eDmU-GnT1vN5isIWB3MX2K6G-N6tFKYVKdBAYiyVlBsmtg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
حملهٔ مجدد پهپادهای اوکراینی به مسکو
🔹
اوکراین یکی از بزرگترین حملات پهپادی به مسکو را انجام داد و انبار فروشگاه بزرگ اینترنتی وایلدبریز (Wildberries) را به‌آتش کشید.
🔹
وزارت دفاع روسیه اعلام کرد دیشب ۸۰۰ پهپاد را رهگیری کرده و شهردار مسکو هم اعلام کرد که…</div>
<div class="tg-footer">👁️ 6.9K · <a href="https://t.me/farsna/456545" target="_blank">📅 13:20 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456544">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Q87TPguft236LJTtgk8O3WkxiVPEh6oxhMS2Wc9dZhtpk2q_pldB6hw41ypmGOwugDOEvS1IqdqbXzCE03BnrGfkv8uAFfeEK8RfLhpc6eV8MKrMTjceYRMxDiuFZhdRY_gZ23ALpGxMAV_h1SPUO3Fl-sehNpQWBNRiyiDQlXY6s7xvkju3RpUXFaveii7upt3AHnN2H8VOYGwxaGXy_YBKHUcW-OlhDjOEQUbZIEbn4UIbZWIxLBtSDu6E8unC6X_V5XyigDTP9BUGCgHHaYragt8RSDLmdwXJkZs4FXpxeVztiSUQO2QvwgZyAeMSvRjuPfVd2xvLN5lP0DA-6A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
اربیل مدعی حملهٔ پهپادی به دفتر مسرور بارزانی شد
🔹
تشکیلات «مبارزه با تروریسم کردستان عراق» مدعی شد که ۲ پهپاد انتحاری دفتر مسرور بارزانی، نخست‌وزیر کردستان عراق را هدف قرار داده‌اند.
🔹
طبق این اطلاعیه، ساختمان سازمان امنیت داخلی اقلیم کردستان نیز هدف این…</div>
<div class="tg-footer">👁️ 6.71K · <a href="https://t.me/farsna/456544" target="_blank">📅 13:15 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456543">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/62513eb08a.mp4?token=kxH_FBryMAoU4zKzX87dmhJoOTo6fhBqy2UpaIF8RG2NXbU-2V7tVCCgVIFqcLnFUwKvglWG5hEH3vLtHLFHjbqFylycRh2l6dwm7N0fxDNTIopopOK2_Uz5L0RziDQZ7QGyIvQ0GxC6532to4A1K1YIdYf2frlE_9faPlxll_dWG-QxVlfX48nJ0EmMMSUE7NakZDuea3FUnpi_-92V7ILry8DS_COknpVhyQjmWP4sPwDu25zChmOCgTjo6eu4rh3xC2uRydIGAiVE_8LDQUUoZATNAZnbsDI3kpQJh2fFtikpqfByes27oLSBXk8pL8T2wKtwZl6TMLjKANmjBA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/62513eb08a.mp4?token=kxH_FBryMAoU4zKzX87dmhJoOTo6fhBqy2UpaIF8RG2NXbU-2V7tVCCgVIFqcLnFUwKvglWG5hEH3vLtHLFHjbqFylycRh2l6dwm7N0fxDNTIopopOK2_Uz5L0RziDQZ7QGyIvQ0GxC6532to4A1K1YIdYf2frlE_9faPlxll_dWG-QxVlfX48nJ0EmMMSUE7NakZDuea3FUnpi_-92V7ILry8DS_COknpVhyQjmWP4sPwDu25zChmOCgTjo6eu4rh3xC2uRydIGAiVE_8LDQUUoZATNAZnbsDI3kpQJh2fFtikpqfByes27oLSBXk8pL8T2wKtwZl6TMLjKANmjBA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
اژه‌ای: در دورهٔ جدید قوه‌قضائیه انتصابات جدید انجام خواهد شد
🔹
برخی از افراد دور همین میز ممکن است به‌دلیل ایجاد تحرک، جابه‌جا شوند.
🔹
شخصاً پیشنهادات افرادی در دستگاه‌هایی خارج از قوه‌قضاییه از جمله سپاه، وزارت اطلاعات و برخی مسئولان سابق در دستگاه قضایی را دریافت کردم.
@Farsna</div>
<div class="tg-footer">👁️ 7.64K · <a href="https://t.me/farsna/456543" target="_blank">📅 13:00 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456542">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/r4SDrz86quS3uD-9___-xuQlYINLiynaF7wyebrnFEdVmpxSYkt-X-HWT58CWG9ZWqGvzystGbWIaOMdfLclPrkhCeUshoKIpvx36KXbD5PZ_-lF0CQ4LYV8OFYptYm3O9O37N-x_0fQoMAtqI_WksyDdQR3qRb-Ni1_wL5g92gwrz_ygohlogdOHa4uO-vODv4oY2vlGjgaQYiIkJmZGIU1M3exxPcA6rqub26W9khIrvRCtTGEnBK0Ivt6x8E3EOQEmiYJBC9q-LZ6stDfGZWG9Uh6R6ryffEAQr4fDe556r_GC8PL8Bz4mYNoKjqtGP3VJ-6fUKeVnGHyd29gGw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جانشین فرمانده‌کل سپاه: ملت ایران دستاورد ۳۵ سالۀ دشمن را خاکستر کرد
🔹
سرلشکر ایزدی: بعد از فراز جنگ رمضان یک وضعیت بدیع و جدیدی را در صحنۀ جهانی منطقه‌ای و حتی کشورمان ملاحظه می‌کنیم.
🔹
به عبارتی ما در این فرازی که نقطۀ عطف آن شهادت جانسوز قائد امت بود با یک بعثتی در جامعه مواجه شدیم و یک نگاه متفاوتی به انقلاب اسلامی و جمهوری اسلامی در جهان را شاهد هستیم.
🔹
این بعثتی که اتفاق افتاده یک ترجمانی دارد؛ این بعثت نتیجۀ بعثت درونی انسان‌هاست.
🔹
بعثت و بیداری ملت ایران در جنگ شناختی، دستاورد ۳۵ ساله دشمن را خاکستر کرد و جمهوری اسلامی را قوی‌تر و استوارتر از گذشته به میدان آورد.
🔹
دشمن اهداف مقطعی را دنبال نمی‌کند. هدف اصلی آنها مقابله با مبانی دینی، علمی و هویتی ملت ایران و به‌دنبال تضعیف پایه‌های اصلی نظام است
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.35K · <a href="https://t.me/farsna/456542" target="_blank">📅 12:52 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456541">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kF0V4B0Qs8CSL1hX3Sm7RBYdRPKwtfxl3nu3O0eJKEZECHNMtj6Xv--zyGbPHxHTs9gle4o20BZ3ij7olnpvaCRZ1h16aayjhOwdGx9djMc1O2f3TvxHVBkvSgJXknQfkTBDMKtJT6zm1Hz-s4KCmFwWQg7ut-F8jXSCcJ_euWPR780SAvT6rsLHDYqj6sXS2GUaF13cGSQD5kjMcY9Jh4CSXQfnah-mUbUwxG-kE1AEA2jXh77vYgC1GGFNMziL0Uc5GhSXRcA-62u2hzwbimYOiHUJv-keNwXiZcoxeEoDgW0oFvhcXPl-SHWauFAEGLDOYqezqHYt_73CAUJUBA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رکورد جدید بورس در مرز ۵ میلیون و ۹۰۰ هزار واحد
🔹
شاخص کل بورس در پایان معاملات امروز با جهش ۱۳۲ هزار واحدی به ۵ میلیون و ۸۹۸ هزار واحد رسید.
@Farsna</div>
<div class="tg-footer">👁️ 7.46K · <a href="https://t.me/farsna/456541" target="_blank">📅 12:36 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456540">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iX-N6Xigziku_awR91PQWghBqTKqIDz2G5O2C_-ASGjGG97ucSV_bwY6RHfeQP2GTdN0mUIpv2ccSGo6f9KBsr9ji9sWi3vyY6ULMv6of7XXRQg7R7qum4oLXOs_DIl92vYt3OGKEur9CedLP4qXc9OiVaKhzEzSgetfVN-sKLihgH4d0QE6OJcS5PWSpGXrRrxzmKC-5cvmd4ho2T-2JaLbuZEDsCwgqO5b-eMlz85u3NPMmsDnhx4j0XwpGQymRUw2WrI44YFkTGiSNEHyCdqbV4ZRhw8v9Afh0IgoPnAb60II8lM38fnY6wNCtriMCMGYUJX4kUQxhtkVDzdBCg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حاجی‌صادقی: هدف اصلی دشمن فرماندهی افکار جامعه است
🔹
نماینده ولی‌فقیه در سپاه: دشمن برای ایجاد شکاف و از بین بردن انسجام جامعه با استفاده از ادبیات دینی و حتی با عنوان دفاع از ولایت، افراد و جریان‌هایی را وارد میدان می‌کند تا انسجام جامعه را هدف قرار دهند.
🔹
دشمن با استفاده از انواع رسانه‌ها و ابزارهای هنری وارد میدان شده و میلیاردها دلار برای این عرصه سرمایه‌گذاری کرده تا بر ذهن و ادراک جامعه اثر بگذارد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.87K · <a href="https://t.me/farsna/456540" target="_blank">📅 12:16 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456539">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/85391bbbde.mp4?token=t2LvkrvODK44PwqShrSDQp8mhqsUirsaGTuLL6puEnb2ZstZJbDzKRjuRp_XAO2GxfuQjRU5YLbasyr5jbS1tEwvGslFwQVKjxqKMFXK9fV7mv586p-tr_7f6MdRehGggylObPpbaqgy1X0A83zGCe6bFNyWNEQOflrmA4BCVYTTAUH4OCvmHQIlYSI9nIfBkeLup3AqrdXaYu6gb3K_zgkbeDcsEz6iJ52slmUtwOY74wIiykq1QniycmM_qS1sIeY5GDxz3ffpic7KXoJZhU_QD2-L5GmkHy4Aw9VX_bwIS_q3erorGLriauyu3ZxLF8WQ3qJvbIUSMU1EWykhdA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/85391bbbde.mp4?token=t2LvkrvODK44PwqShrSDQp8mhqsUirsaGTuLL6puEnb2ZstZJbDzKRjuRp_XAO2GxfuQjRU5YLbasyr5jbS1tEwvGslFwQVKjxqKMFXK9fV7mv586p-tr_7f6MdRehGggylObPpbaqgy1X0A83zGCe6bFNyWNEQOflrmA4BCVYTTAUH4OCvmHQIlYSI9nIfBkeLup3AqrdXaYu6gb3K_zgkbeDcsEz6iJ52slmUtwOY74wIiykq1QniycmM_qS1sIeY5GDxz3ffpic7KXoJZhU_QD2-L5GmkHy4Aw9VX_bwIS_q3erorGLriauyu3ZxLF8WQ3qJvbIUSMU1EWykhdA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سخنگوی وزارت خارجه در واکنش به مخفی‌شدن ترامپ در کامیون غذا: این ترس همواره با جنایت‌کاران همراه خواهد بود و آرزوی مرگ آرام را به‌گور خواهند برد
🔹
ملت ایران مفتخر به این است که رهبرانشان از خطر نترسیدند و تا لحظهٔ آخر در محل‌های خدمتشان از عزت کشور دفاع کردند.
@Farsna</div>
<div class="tg-footer">👁️ 7.48K · <a href="https://t.me/farsna/456539" target="_blank">📅 12:08 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456538">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/eb708e5299.mp4?token=awp-fgzFWfvc5YJNmE2ES9AvVCYYjAG7tTMigB2Ff0Gm223y9IpGBtM3LqO2kEIa4aIyWXMJVcxp4l6D4wXvxMyLPEUrbQMWBKM9psDkWNUqncA3Ko-o_BoaVuB7IAXHSghxfTAEGN9MHzcdhxf1ndOHUSKxXrpYxIAgf45_eLO28Kt90KDiqQHC1zm99PGW1iYLRUNkcUJ20yG7LgppK9sPCdymFbOJyudjEYjkAujRYHR9-XnXEtXAITDAr8_jDfwmGLuzKODneyda7zPqwpSLS0ex2OdTxm-y8xb4mW37I1xChd4UeL-mCPYupAMpRCUUHLykwCpjPVpO9D5RwA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/eb708e5299.mp4?token=awp-fgzFWfvc5YJNmE2ES9AvVCYYjAG7tTMigB2Ff0Gm223y9IpGBtM3LqO2kEIa4aIyWXMJVcxp4l6D4wXvxMyLPEUrbQMWBKM9psDkWNUqncA3Ko-o_BoaVuB7IAXHSghxfTAEGN9MHzcdhxf1ndOHUSKxXrpYxIAgf45_eLO28Kt90KDiqQHC1zm99PGW1iYLRUNkcUJ20yG7LgppK9sPCdymFbOJyudjEYjkAujRYHR9-XnXEtXAITDAr8_jDfwmGLuzKODneyda7zPqwpSLS0ex2OdTxm-y8xb4mW37I1xChd4UeL-mCPYupAMpRCUUHLykwCpjPVpO9D5RwA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🖼
معاون وزیر خارجه: آلودگی نفتی سواحل قشم، ناشی از آثار تجاوز نظامی خارجی در منطقه است
🔹
این قبیل خسارات وارده بر محیط‌زیست سواحل ایرانی خلیج فارس، ضرورت تعریف و اعمال سازوکار مدیریت تنگه هرمز توسط ایران به‌عنوان کشور ساحلی را بیش‌ازپیش، برجسته می‌کند. @Farsna</div>
<div class="tg-footer">👁️ 7.2K · <a href="https://t.me/farsna/456538" target="_blank">📅 12:02 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456536">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">انفجار کنترل‌شده در جنوب اصفهان
🔹
سپاه اصفهان: احتمال شنیدن صدای انفجار کنترل‌شده در صفه، بهارستان و اطراف آن تا ساعت ۱۴ امروز وجود دارد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.13K · <a href="https://t.me/farsna/456536" target="_blank">📅 11:52 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456535">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JYA-q_WoILPjPc_UuIqaeCMT1OcV8nD-zNy2hhLJ6jTfUj41PrGoGFQRxEdN_JVQhWb6pRfPQwE6gZ7OzEoBcUokq1HhV_Z_N1WdnUl3Uxhs-tYwGZQKMLumZPZhOD3Rm6FF29aNfik__lIJRdjzPEWXYf0JXkr45YxJKeI3DRUjVzwsLebH8CQeKoJHGqHDZ02v4a7HjJmHCAYJSdJdjJ8lY-p4nV0ywbec1t2NCyD228uJyw_YZdpcJHn5TqlgH5rGPHNCmilYicetGci6me4TY4QKhsPHJVI-XI4tuNm667sh6V6i9gYwy3ButhyPQ91J9snwDVAO37dwfdyhbQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‌ بخش عمدهٔ آلودگی نفتی سواحل قشم مهار شد
🔹
معاون دریایی بنادر هرمزگان: تاکنون بخش عمده‌ای از آلودگی‌های نفتی سواحل قشم مهار شده و عملیات پایش، جمع‌آوری پس‌مانده‌های نفتی و پاکسازی منطقه تا رفع کامل آثار آلودگی ادامه دارد. @Farsna - Link</div>
<div class="tg-footer">👁️ 7.44K · <a href="https://t.me/farsna/456535" target="_blank">📅 11:50 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456534">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3fa912b817.mp4?token=a7bcNafRLX4ga2kNtK_1ouimReO-H0NncOOQJxf7MZ3JRFd4vfP5J5swbRub9XpBrSAQWwTKyrpoUM3Vabk3cpR3p5ZyTh73NwSmnByZU8XUh1AwyVo9ZuulBF5Ysr8HQdFqkyBdxBfl9FCm1KuTPdepNpUpyZyQat9WiI1ppHtcV7ovQ_5qXqmfOwy-9cntd1n949DdzDd_Y24VcY6wQa-wacF-D6taKEM7d8kmhaGfsCaAUE33qocyGftkiNHvgxGxjOr1w5JWue__GmSbRLGfIy2HEQ5XE7-pyTU8mGYInt0nEp8xAp4DI_U_OXHlLOUyOZn30B3PKWxR5r3Tdw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3fa912b817.mp4?token=a7bcNafRLX4ga2kNtK_1ouimReO-H0NncOOQJxf7MZ3JRFd4vfP5J5swbRub9XpBrSAQWwTKyrpoUM3Vabk3cpR3p5ZyTh73NwSmnByZU8XUh1AwyVo9ZuulBF5Ysr8HQdFqkyBdxBfl9FCm1KuTPdepNpUpyZyQat9WiI1ppHtcV7ovQ_5qXqmfOwy-9cntd1n949DdzDd_Y24VcY6wQa-wacF-D6taKEM7d8kmhaGfsCaAUE33qocyGftkiNHvgxGxjOr1w5JWue__GmSbRLGfIy2HEQ5XE7-pyTU8mGYInt0nEp8xAp4DI_U_OXHlLOUyOZn30B3PKWxR5r3Tdw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سخنگوی وزارت خارجه: در تفاهم پیش‌بینی شده بود که طی ۶۰ روز دربارهٔ رفع تحریم و موضوع هسته‌ای مذاکره شود، اما به‌دلیل نقض‌های فاحش و گسترده‌ای که آمریکا انجام داد، اصلاً مذاکره‌ای را شروع نکردیم.  @Farsna</div>
<div class="tg-footer">👁️ 7.18K · <a href="https://t.me/farsna/456534" target="_blank">📅 11:44 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456533">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">🔴
اربیل مدعی حملهٔ پهپادی به دفتر مسرور بارزانی شد
🔹
تشکیلات «مبارزه با تروریسم کردستان عراق» مدعی شد که ۲ پهپاد انتحاری دفتر مسرور بارزانی، نخست‌وزیر کردستان عراق را هدف قرار داده‌اند.
🔹
طبق این اطلاعیه، ساختمان سازمان امنیت داخلی اقلیم کردستان نیز هدف این حملات قرار گرفته است.
@Farsna</div>
<div class="tg-footer">👁️ 7.41K · <a href="https://t.me/farsna/456533" target="_blank">📅 11:36 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456532">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rt4_flKzwjqdK-Bw288faerbppOpPm1jSlpGCZoQDqvOv7kw5GDPr6UaYnLxZWZYy4KoomYN5T_wUYzB8Bak0nX3ExTVoa-TMx9RH9R3ywBoCIQZoyshEyftFRMCrwFyKD7-Gw9NQKItR5ARFDIndfqeRS7xWrhpSiBBO7Xq0xkyMY8X-w1Tv5-poiJITNbpajMKlp-L9n8xwrOU6BAy35ySGr7NpSCsbKmrfCTleNM-cYN-N9tEYQ5BEOYw2h_jOKe8raARq3ukJpaV2JUJykylOJ1IxZsHz-6gb-1jYW_RaI6nh3Yr3mM_QFG-p6yeWSKbwcWyAsuZblclo5axWA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎥
رئیس سازمان بهینه‌سازی: ۳ طرح پیشنهادی بنزین روی میز دولت است و هرکدام منتقدان و طرفدارانی دارد
🔹
هرکدام از این ۳ طرح تصویب شود، قطعا آن را پیش از اجرا اعلام می‌کنیم و مردم را غافلگیر نخواهیم کرد. @Farsna</div>
<div class="tg-footer">👁️ 7.42K · <a href="https://t.me/farsna/456532" target="_blank">📅 11:35 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456531">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/25766eff35.mp4?token=qvaslcvdbqSCyba0_czJ7PlmJ-ryxEl7nOZkKuEy7K-6fPrHT4W8v8AvANUBVXJMS454TFduyOubDg9u4SRvzkJVcu7ZmMP7kuOZNYOxHJHMKIc01M9SggtFjMxzAlGP__wBieMJG-A8tK_7aCe41vtJ42txjV7bydH2AFKclBSgTkiCnaRbwBewC12N0R_JvXTNtNxYF0xT6Qn4SJQHILQCbhLIynH0G2nvzKAS6iFefrHxMK6ito4uGc3Cw1w1K-kpRu-Bp2F8psBwalxs4_bEx9v8z16SCXQq8Xm-8FXphso7tBe7SVn-YvswCm80PkOeo9PBvhJ3csE1sOYJLg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/25766eff35.mp4?token=qvaslcvdbqSCyba0_czJ7PlmJ-ryxEl7nOZkKuEy7K-6fPrHT4W8v8AvANUBVXJMS454TFduyOubDg9u4SRvzkJVcu7ZmMP7kuOZNYOxHJHMKIc01M9SggtFjMxzAlGP__wBieMJG-A8tK_7aCe41vtJ42txjV7bydH2AFKclBSgTkiCnaRbwBewC12N0R_JvXTNtNxYF0xT6Qn4SJQHILQCbhLIynH0G2nvzKAS6iFefrHxMK6ito4uGc3Cw1w1K-kpRu-Bp2F8psBwalxs4_bEx9v8z16SCXQq8Xm-8FXphso7tBe7SVn-YvswCm80PkOeo9PBvhJ3csE1sOYJLg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">عراقچی: آتش‌بسی وجود ندارد که بخواهیم آن را تمدید کنیم
🔹
آنچه در پایان جنگ و در یادداشت تفاهم اسلام‌آباد اعلام شد «پایان جنگ» بود. آمریکا تفاهم را نقض کرد و درگیری‌ها مجدداً آغاز شده.
🔹
ما چیزی به‌عنوان آتش‌بس نداشتیم که حالا بخواهد تمدید شود؛ ما «پایان جنگ»…</div>
<div class="tg-footer">👁️ 6.96K · <a href="https://t.me/farsna/456531" target="_blank">📅 11:28 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456530">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">‌ ثبت‌نام حج ۱۴۰۶ آغاز شد
🔹
سامانه «حج من» از ساعت ۱۰ صبح امروز برای متقاضیان سال ۱۴۰۵ فعال شد تا مراحل ثبت‌نام و معاینات پزشکی با دقت بیشتری انجام شود.
🔹
سایر متقاضیان نیز بر اساس جدول اولویت‌ها، وارد فرآیند خواهند شد.  @Farsna - Link</div>
<div class="tg-footer">👁️ 7.26K · <a href="https://t.me/farsna/456530" target="_blank">📅 11:18 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456529">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8301d537ed.mp4?token=vflG4Ae4yaXMM8Ex7kLWwqXnCZ1QFvI6SYk7FwXptXYaXP-1SJCTh2ZYe7UDsR20Lf2B6xP5WNSGrzBcvhqQjotz5-8fx5S501bQQ8ZJ7MfKILKJ9o9QUP4KYZk5nrHC2Zr8RLr9PsXPMc02opNw9sVkqxytMGMaHNT0BjhaC8iPAIi0D677TtwtPWtMkDh2VKXL3E4z8WT2dNW7JfmoSVTqWZlua-3yfeLwSVpE_XCsYfoiFx7adSOXzipmrEbmLtSCZ2EwtCYV7p5Tw5IGkO2qcV3hHeq2LMmALqrFhpUDLAuaksw06iJh9ZLLnUurG0fvUz7N8y-OElMSn2sUBw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8301d537ed.mp4?token=vflG4Ae4yaXMM8Ex7kLWwqXnCZ1QFvI6SYk7FwXptXYaXP-1SJCTh2ZYe7UDsR20Lf2B6xP5WNSGrzBcvhqQjotz5-8fx5S501bQQ8ZJ7MfKILKJ9o9QUP4KYZk5nrHC2Zr8RLr9PsXPMc02opNw9sVkqxytMGMaHNT0BjhaC8iPAIi0D677TtwtPWtMkDh2VKXL3E4z8WT2dNW7JfmoSVTqWZlua-3yfeLwSVpE_XCsYfoiFx7adSOXzipmrEbmLtSCZ2EwtCYV7p5Tw5IGkO2qcV3hHeq2LMmALqrFhpUDLAuaksw06iJh9ZLLnUurG0fvUz7N8y-OElMSn2sUBw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
وزیر کشاورزی: از زمان شروع جنگ ۴۰ روزه از ذخایر کالاهای اساسی استفاده نکرده‌ایم؛ نه‌تنها چیزی از آن کم نشده بلکه درحال اضافه‌شدن است.
🔹
محاصرهٔ ایران چیز جدیدی نیست؛ ایران به مسیرهای زمینی و دریایی متعددی دسترسی دارد و چرخ امنیت غذایی کشور همواره در حرکت…</div>
<div class="tg-footer">👁️ 6.89K · <a href="https://t.me/farsna/456529" target="_blank">📅 11:14 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456528">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/944a019ec7.mp4?token=v4VLU3bqkQMWKPZLJgwr74GOxkEu6cbYNu3k4phTnUD5sIYh7LEldiGmQCnY-CBHQBmXfEXFNsenW2eFMW94dkOyYXL8-JLeNKYR0YkqIfJQzKTd84zWzyMIYP2Uz9VCIpELaQykYrPsLiezoZUyVaRDtyreNvti4AUXgntcrsyoXn_SOO99mIxCHSEerxTJqO5OW2aMp6qofDqgBcUhJ-BgEKHAZlCRZuwHsX5ZO_seq-Mg3bxRm4vN6tBwsQeZvwLYX7hNUNZiI1zOtYMotBN5mtvtZ50iU_kRpAOBuZYm4uR1VuU5STbQJEtK5OKNtDqlP1x062jHbohWUoYQFg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/944a019ec7.mp4?token=v4VLU3bqkQMWKPZLJgwr74GOxkEu6cbYNu3k4phTnUD5sIYh7LEldiGmQCnY-CBHQBmXfEXFNsenW2eFMW94dkOyYXL8-JLeNKYR0YkqIfJQzKTd84zWzyMIYP2Uz9VCIpELaQykYrPsLiezoZUyVaRDtyreNvti4AUXgntcrsyoXn_SOO99mIxCHSEerxTJqO5OW2aMp6qofDqgBcUhJ-BgEKHAZlCRZuwHsX5ZO_seq-Mg3bxRm4vN6tBwsQeZvwLYX7hNUNZiI1zOtYMotBN5mtvtZ50iU_kRpAOBuZYm4uR1VuU5STbQJEtK5OKNtDqlP1x062jHbohWUoYQFg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‌ باقرزاده: قطر به جای تکذیب اسارت خلبانان ایرانی، دفع وقت نکند
🔹
فرمانده کمیتۀ جست‌وجوی مفقودین ستادکل نیروهای مسلح: تیمی متشکل از کارشناسان زبده نیروی هوایی کشورمان چندین ماه است که در انتظار ورود به قطر و بررسی میدانی هستند.
🔹
با کارشکنی‌های پیاپی و دفع‌الوقت…</div>
<div class="tg-footer">👁️ 7.43K · <a href="https://t.me/farsna/456528" target="_blank">📅 11:06 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456527">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/507dba98f8.mp4?token=krpLcEzmgj8YjmzdFoqFDKCsuLoZhhlw-sjOKw-n7-wYN19aXX5ipog6HdNiixB-0UFg63_dEzYFnoyzplz5YBszCShfSdVSn0GItg22A5BDBgIsjNxCXzuZkE6EpHPN7vK--dWBqjndUjwYnq4OzekSaBdkjgW1iSto_Q00F7vA7eVdeoZR_tGyYQYqdnIq30Wdw0Nk2_0g5iD0iXiYwiwqMvyyTxs4tjpXjkfbU8XOUOCTVQZKrJGG9HPjzIz2hiYUnGsWFUylW4M8AZvFBc_DbprsA4UstzZLkF-74nA5hCKO4-zhqj49bt5b4il5N6EKc9Qp0MmC9yOe_-y9Pw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/507dba98f8.mp4?token=krpLcEzmgj8YjmzdFoqFDKCsuLoZhhlw-sjOKw-n7-wYN19aXX5ipog6HdNiixB-0UFg63_dEzYFnoyzplz5YBszCShfSdVSn0GItg22A5BDBgIsjNxCXzuZkE6EpHPN7vK--dWBqjndUjwYnq4OzekSaBdkjgW1iSto_Q00F7vA7eVdeoZR_tGyYQYqdnIq30Wdw0Nk2_0g5iD0iXiYwiwqMvyyTxs4tjpXjkfbU8XOUOCTVQZKrJGG9HPjzIz2hiYUnGsWFUylW4M8AZvFBc_DbprsA4UstzZLkF-74nA5hCKO4-zhqj49bt5b4il5N6EKc9Qp0MmC9yOe_-y9Pw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
وزیر کشاورزی: قیمت اغلب کالاهای اساسی و مواد غذایی نسبت به هفتهٔ گذشته و نسبت به ماه گذشته رو به پایین است.
🔹
مرغ سال گذشته ۱۴۰ هزار تومان بود الان بیش از ۳۷۰ هزار تومان است که دلایل خود را دارد.
🔹
جنگ روی افزایش قیمت‌ها تاثیر گذاشته و قیمت‌های جهانی ۱۰…</div>
<div class="tg-footer">👁️ 6.64K · <a href="https://t.me/farsna/456527" target="_blank">📅 11:05 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456526">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ueogWeBDy0_aauLxGxHm67ZTdqEmZqitk2R4EvXoeHWu_ydun48FEyXYWrHCb7k2P14nIy1v5BZ8aiOhWt3H7eBrPNbtq0jkK092MRpSJr0gHYatE09ComdZAYJWC5Zbz_Bu-vzlxBz3h8HAlSNFO0CnVwEEzSNfCnLmZoYFLLl2tLzrWSpIWNRrRJ7wMGX4Ax3QB4wFDAMr9eyq0ke3AAJe007AzuhmBHLHkgY6SqJu5cqbIZvxxKkaGlHpYcMZE0ivsrFYaqlVWyccQmGUzJp2yE5whITl9uUtuoYZGXjSm_PpaGkWLam80G8T2LNn7SkSWqMj9T_aeYsjFcRMIw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بسته بودن تنگه هرمز،‌ بازگشت به مدرسه را برای آمریکایی‌ها گران کرد
🔹
همزمان با آغاز فصل بازگشت به مدرسه در آمریکا، افزایش هزینه‌های زندگی بار مالی سنگین‌تری بر دوش خانواده‌ها گذاشته است. تعرفه‌های تجاری دولت دونالد ترامپ و پیامدهای جنگ با ایران به افزایش قیمت کالاهای مورد نیاز دانش‌آموزان و سایر هزینه‌های خانوار دامن زده‌اند.
🔹
والدین آمریکایی در گفت‌وگو با ام اس نَو از افزایش شدید قیمت کالاهایی مانند کوله‌پشتی، دفتر، جعبه غذا و لوازم الکترونیکی ابراز نگرانی کرده‌اند. یکی از مادران مجرد چهار فرزند در ویرجینیای غربی گفته است حتی یک کوله‌پشتی ساده ۳۵ دلاری نیز برای او گران تمام می‌شود.
🔹
این فشار اقتصادی به هزینه‌های مدرسه محدود نمی‌شود. تغییرات ایجادشده در برنامه‌های کمک غذایی و درمانی در پی تصویب طرح موسوم به «لایحه بزرگ و زیبای ترامپ» نیز دسترسی برخی خانواده‌های کم‌درآمد به کمک‌های غذایی و پوشش درمانی را دشوارتر کرده است.
@FarsNewsInt
-
Link</div>
<div class="tg-footer">👁️ 6.63K · <a href="https://t.me/farsna/456526" target="_blank">📅 10:55 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456525">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dd2fd5eddd.mp4?token=v5q75H3G0QllwBp7sPO6_7fEHFD7BxghyGf1-3HPN7E7kHPXcnZBE-3QZtrq_4jc2h-GJkEaYmMzZtmlGx0JUwSVD3iDvVUvo9W_EGcHpmdznrmHdhCRITB4o9KMLMoieWbDLTPmIEvp6CBVVWsLTeqXUA-8m82V7U0xG7knN6REV8sgu2of88YQx82rrTIm4E1ZWZCOX3kUwddy8e6duZRbe5QKQ7KDPe5PpsYnA3vmAklVj1IjoVw-B2sGT1kO7Xs5rw9uQNejzbjga40lWN-2O43-paJNUWEroSKiaqKGIwtmjEw_CQrWh48CKUMVq1yF1dPCDIIK2g2YMruPUDzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dd2fd5eddd.mp4?token=v5q75H3G0QllwBp7sPO6_7fEHFD7BxghyGf1-3HPN7E7kHPXcnZBE-3QZtrq_4jc2h-GJkEaYmMzZtmlGx0JUwSVD3iDvVUvo9W_EGcHpmdznrmHdhCRITB4o9KMLMoieWbDLTPmIEvp6CBVVWsLTeqXUA-8m82V7U0xG7knN6REV8sgu2of88YQx82rrTIm4E1ZWZCOX3kUwddy8e6duZRbe5QKQ7KDPe5PpsYnA3vmAklVj1IjoVw-B2sGT1kO7Xs5rw9uQNejzbjga40lWN-2O43-paJNUWEroSKiaqKGIwtmjEw_CQrWh48CKUMVq1yF1dPCDIIK2g2YMruPUDzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تاکید رئیس‌کل بانک مرکزی بر پیگیری مسائل صادرکنندگان و پیمانکاران ایرانی در عراق
🔹
رئیس‌کل بانک مرکزی در دیدار با تجار، صادرکنندگان و پیمانکاران ایرانی در سفارت ایران در بغداد، مسائل و موانع فعالیت اقتصادی در بازار عراق را بررسی کرد.
🔹
موانع بازگشت ارز صادراتی،…</div>
<div class="tg-footer">👁️ 6.42K · <a href="https://t.me/farsna/456525" target="_blank">📅 10:53 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456524">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8251e814b0.mp4?token=GesQIlHpP5OohsIzBP0lKRhMYzfWboMobIWd1mdszXt0pq-1mfaXSJix9ouG9ngS8DtZ_LeevS2maEs5thMk-Ft68gJY2p0s7zRfsNiFJFMqSkFaE6e6jh4r2bOtr6-uw0PPQ0wT8qrqo0wCTAaXvvtTQDuipx0kOyQWPzAXIMRlKicVCKaQcaG77J_m5_m1t5v_GapScgTV4WfXHtFJeSE7zmyhwsRYPkLrnGQ_rXdgSbmyGpSCdzgrxvO8ciY-8loPIjbzYR7iXR8JsT2mi6ejfYE3HYBxJHT0h7Wr0aZSiEuVioo0nAePAwIUIaYO_gEWGGmYNrK_hB4SIs0SzTKy1aUbhSrzHCuel15TwuHu6pdTybTdrhK10xQ6yT15ubfNbWpL2jmJKCXO0rrYOHX-NLJ5BsUc1qCb1mdN_u0bD3SjHYcSdXadL_ZJrTRShyZm_0_BZeiHAPSqVk9nhKqvzuUhXvqrOLAYvqbpdsQSenKamTe_mR55CqztMj8Kqvd_SgCs0kMLzv19dOqV-CCPXVr4h6eM56kINHNyD0iJQ0CpKpyL7i5JQkOpTb_24UokgN8KS46vE4Azwnaz8nV4bSd-ifIHzyNq3_lP354VD5xbBdFIp_cenjbuKCjL9WOrTImDDgSkH31VyuNbv0g2bxfvozlJ3IGOYimlBLE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8251e814b0.mp4?token=GesQIlHpP5OohsIzBP0lKRhMYzfWboMobIWd1mdszXt0pq-1mfaXSJix9ouG9ngS8DtZ_LeevS2maEs5thMk-Ft68gJY2p0s7zRfsNiFJFMqSkFaE6e6jh4r2bOtr6-uw0PPQ0wT8qrqo0wCTAaXvvtTQDuipx0kOyQWPzAXIMRlKicVCKaQcaG77J_m5_m1t5v_GapScgTV4WfXHtFJeSE7zmyhwsRYPkLrnGQ_rXdgSbmyGpSCdzgrxvO8ciY-8loPIjbzYR7iXR8JsT2mi6ejfYE3HYBxJHT0h7Wr0aZSiEuVioo0nAePAwIUIaYO_gEWGGmYNrK_hB4SIs0SzTKy1aUbhSrzHCuel15TwuHu6pdTybTdrhK10xQ6yT15ubfNbWpL2jmJKCXO0rrYOHX-NLJ5BsUc1qCb1mdN_u0bD3SjHYcSdXadL_ZJrTRShyZm_0_BZeiHAPSqVk9nhKqvzuUhXvqrOLAYvqbpdsQSenKamTe_mR55CqztMj8Kqvd_SgCs0kMLzv19dOqV-CCPXVr4h6eM56kINHNyD0iJQ0CpKpyL7i5JQkOpTb_24UokgN8KS46vE4Azwnaz8nV4bSd-ifIHzyNq3_lP354VD5xbBdFIp_cenjbuKCjL9WOrTImDDgSkH31VyuNbv0g2bxfvozlJ3IGOYimlBLE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
وزیر کشاورزی: با اصلاحاتی که در سیاست ارز ترجیحی انجام شد، تولید دانه‌های روغنی با سرعت بیشتری ادامه خواهد داشت.   @Farsna</div>
<div class="tg-footer">👁️ 6.61K · <a href="https://t.me/farsna/456524" target="_blank">📅 10:48 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456523">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qYOjrxBWymvAjJPA7416dz3dLrK4GHEREofrSomaJaHfDLf_b_StHLC8YRo8_Rrldxn3KYKE75VGYLdsnU286r4JHhSPjWlABRTu960fCkDE-yvuo_dJ36YYIv-nk4IzegqL7dJbjzskF6cNDHSzZsTrNLPM5HWwepniHxaAN0wBDdyijoFGIYG2uYYyQYg1mQDjFuihpShDSTB9-9U1XMe3lqFWqIHr65nO-tV054w_5kIRSgTtCgPJNatR20qq3skFyB1Lq8N9nbmPiOQqPrwVPruo7oMFnkzWZytlrJTi4rJRhAd6b5oKfsYxlzYT5rnDD7r8dcyB470wnWI0UQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مسکن مهر در دستور کار پیگیری دیوان محاسبات
🔹
دیوان محاسبات: قصور در تکمیل و تحویل حداقل ۸۰ هزار واحد باقی‌ماندۀ مسکن مهر در سنوات گذشته، علی‌رغم ایفای تعهدات مالی متقاضیان، درحال رسیدگی است و فرآیند مستندسازی پرونده مسئولان وقت در حال انجام است.
🔹
در تعامل با وزارت شهرسازی مقرر شد مبلغ ۲۰ هزار میلیارد تومان در سال جاری برای تکمیل و تحویل واحدهای باقی‌مانده اختصاص یابد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.16K · <a href="https://t.me/farsna/456523" target="_blank">📅 10:41 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456522">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d5fa181a7b.mp4?token=gSdIHvxbchMDSkumbI0CsCWx6aEu4vjDtz3TlhrxaQWcQcATVRN7T68b3Wr2U_C-RJJhFkeiqhijeq0wl32eXCeUEH8Mk45WPyhjdrYGS0lZpcD8RjrSuPFONxDyvLsLLPS4U0Fs9xUHY0TOdgorSLO_gZZBjDjkJWx7ukwBfrJhPtMxXCca0U_tHYRUFgGcfEZUB35q2-gFjPFN3FFQoVI8h0ylFto9M7UWhmbfAUgBIXXGZskuTugjttRAIrHZTHH8uo89hqcV-WNRqTgjm_QzLlGCkbhFmPNrUANUIZoPUqmOoQD3AuwVDfoeFv6OrukQ6ag74Eqf1klHMGjLCA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d5fa181a7b.mp4?token=gSdIHvxbchMDSkumbI0CsCWx6aEu4vjDtz3TlhrxaQWcQcATVRN7T68b3Wr2U_C-RJJhFkeiqhijeq0wl32eXCeUEH8Mk45WPyhjdrYGS0lZpcD8RjrSuPFONxDyvLsLLPS4U0Fs9xUHY0TOdgorSLO_gZZBjDjkJWx7ukwBfrJhPtMxXCca0U_tHYRUFgGcfEZUB35q2-gFjPFN3FFQoVI8h0ylFto9M7UWhmbfAUgBIXXGZskuTugjttRAIrHZTHH8uo89hqcV-WNRqTgjm_QzLlGCkbhFmPNrUANUIZoPUqmOoQD3AuwVDfoeFv6OrukQ6ag74Eqf1klHMGjLCA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
وزیر جهاد کشاورزی: قیمت در بازارهایی مثل قند، شکر، آرد و روغن مشکلی ندارد؛ حتی چند درصد پایین‌تر از قیمت تعادلی مشخص‌شده در سازمان حمایت از مصرف‌کننده و تولیدکننده است.  @Farsna</div>
<div class="tg-footer">👁️ 7.19K · <a href="https://t.me/farsna/456522" target="_blank">📅 10:30 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456521">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9cc7bea42f.mp4?token=NAhjxLjKWksLOunphYS-lZKLfHSudLxDoefYsanSifkhOF_w1jBjrAH-aPwLQpS_2YjGvU-rzNzJx-uKDzs-BHBcwehibTFL8NDJmryrZZMb5VpCSAm_hb1bRK1T3CNQ_v0ZEVT3WPm92tn3W09lUvDvhe-3_EuXhz-ngBnJLd3OZc6KyfOXKKxSN_vlAg0t4sUOpxJXacGAfab29G0Ese7zqx5_2-Jb0v9s1nz1CnI4E2cUZBzUK_lX79gxIwhuW6FZy8I3qr67uwlR8rkb7U97A3a3D9cughVNO8NqEj4L41mOCmyGv08ZFc-xJ32D5thgUTnJgYffuBZ4OncPag" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9cc7bea42f.mp4?token=NAhjxLjKWksLOunphYS-lZKLfHSudLxDoefYsanSifkhOF_w1jBjrAH-aPwLQpS_2YjGvU-rzNzJx-uKDzs-BHBcwehibTFL8NDJmryrZZMb5VpCSAm_hb1bRK1T3CNQ_v0ZEVT3WPm92tn3W09lUvDvhe-3_EuXhz-ngBnJLd3OZc6KyfOXKKxSN_vlAg0t4sUOpxJXacGAfab29G0Ese7zqx5_2-Jb0v9s1nz1CnI4E2cUZBzUK_lX79gxIwhuW6FZy8I3qr67uwlR8rkb7U97A3a3D9cughVNO8NqEj4L41mOCmyGv08ZFc-xJ32D5thgUTnJgYffuBZ4OncPag" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
وزیر جهادکشاورزی: ۸.۲ میلیون تن گندم از کشاورزان خریداری شده و امسال وضعیت تولید خوب است.
🔹
همچنین از مجموع ۴۰۰ همت طلب گندمکاران، ۲۱۸.۵ همت پرداخت شده است. @Farsna</div>
<div class="tg-footer">👁️ 7.85K · <a href="https://t.me/farsna/456521" target="_blank">📅 10:17 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456520">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/953c8a4026.mp4?token=ATebPtYMbHGuPTz30IXONQDGF-yvetCdPiJTpyep3QcfXWgudwTzjE83WYvnhPmjGk4K3qu4GlDGWsQyb0IjcU0dw9d1Jmo3xGIxRoy54Dr3RnAy8mH8z_4NuV-qe3jAZyqpw6y1B4xUatZQzi_BDbPEWQWZpXxx-jwK057r-YT74oVL4ccPw7wvJem0qAI9Z5vIBab8Aveui0yLgEpmNm5hdRCi5MoAco5e2RopK9iFpEmbzNupD66XrENvWaP1gUOTwKFPU9-I35BPRJpNNmf7M34ZddGtn9s2BISH9KiA4Rxx4Mmz68KYU0v41tQfX6JDooCWFiTgcy5dz7ORCA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/953c8a4026.mp4?token=ATebPtYMbHGuPTz30IXONQDGF-yvetCdPiJTpyep3QcfXWgudwTzjE83WYvnhPmjGk4K3qu4GlDGWsQyb0IjcU0dw9d1Jmo3xGIxRoy54Dr3RnAy8mH8z_4NuV-qe3jAZyqpw6y1B4xUatZQzi_BDbPEWQWZpXxx-jwK057r-YT74oVL4ccPw7wvJem0qAI9Z5vIBab8Aveui0yLgEpmNm5hdRCi5MoAco5e2RopK9iFpEmbzNupD66XrENvWaP1gUOTwKFPU9-I35BPRJpNNmf7M34ZddGtn9s2BISH9KiA4Rxx4Mmz68KYU0v41tQfX6JDooCWFiTgcy5dz7ORCA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‌
🔴
سرپرست دادسرای جنایی تهران: ۹ عامل اصلی مرتبط با قتل حمیدرضا رجب‌زاده دستگیر شدند.  @Farsna</div>
<div class="tg-footer">👁️ 7.91K · <a href="https://t.me/farsna/456520" target="_blank">📅 10:14 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456519">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/416e249c60.mp4?token=L7O1imtG0KtS5COs0kwIc8K9UvnLuUNwuC6iRMIEW7dQ4xh1Et70aJzj9CW9Ukh1pUuUpGyOIYPv2NVnbMrEqjo2QED2RNWLJ4QF469DhsytbwcWqS_RU0-2SMAAaxBQ3Dz6TrpuF3T2cwiOigmnKckmXNNrpPJRxhNlb08sJYHeTwTvTHN-0KstlNJKqtJbM7E6A_MBnxEtb_3l0oXHIRyn2VQcsrKReDgEKHOUVGOFftpDFTT0bgXCcVldg_PvzKPqPf5nZlYXtZrV3fYxNtfsH1sxLtx8_n4DTkvU7hhi6xbwAd3UEnuMasoaO2U5p4YHsv_zRqz6wQ3B_-jvGg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/416e249c60.mp4?token=L7O1imtG0KtS5COs0kwIc8K9UvnLuUNwuC6iRMIEW7dQ4xh1Et70aJzj9CW9Ukh1pUuUpGyOIYPv2NVnbMrEqjo2QED2RNWLJ4QF469DhsytbwcWqS_RU0-2SMAAaxBQ3Dz6TrpuF3T2cwiOigmnKckmXNNrpPJRxhNlb08sJYHeTwTvTHN-0KstlNJKqtJbM7E6A_MBnxEtb_3l0oXHIRyn2VQcsrKReDgEKHOUVGOFftpDFTT0bgXCcVldg_PvzKPqPf5nZlYXtZrV3fYxNtfsH1sxLtx8_n4DTkvU7hhi6xbwAd3UEnuMasoaO2U5p4YHsv_zRqz6wQ3B_-jvGg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
توضیحات وزیر جهادکشاورزی دربارهٔ تخلف ۴۵ هزار میلیارد تومانی نهادهٔ دامی: چنین اعداد و ارقامی سوءتفاهم است و برای دولت چهاردهم نیست.  @Farsna</div>
<div class="tg-footer">👁️ 8.24K · <a href="https://t.me/farsna/456519" target="_blank">📅 10:08 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456518">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8ab49e9f1e.mp4?token=QkMDCxzLT-0N7eCQgMEf6TZD_NRkT-ev7Hdty-Tu_EgUxEFeZRkQIOfG8V35dAWMbqIaFKU2xjGqWIqajbq2RuYbpOf45UWPwEA5AxUKxxHXe6yi0N9hE5mYidlVcFKSsVENl4E5GrJvf1yXyRDcAc6wCXVv_F02MtGCLeBfUtBCbjy4582qogEE33atv12MA_kCoCFCztPUjmpRg0aUlNlJGU1dmzDQeqYYFCv95eQ2jm8gpCiWY2CGvJpuguR57cMNhYB1poXKO8rFGzjwR0FoNmE505QLYUQ1bK2FSk8Uq10ju0LS2grgSsi3dWMdh7PHuBs6kHwLFWdv5Y2BXA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8ab49e9f1e.mp4?token=QkMDCxzLT-0N7eCQgMEf6TZD_NRkT-ev7Hdty-Tu_EgUxEFeZRkQIOfG8V35dAWMbqIaFKU2xjGqWIqajbq2RuYbpOf45UWPwEA5AxUKxxHXe6yi0N9hE5mYidlVcFKSsVENl4E5GrJvf1yXyRDcAc6wCXVv_F02MtGCLeBfUtBCbjy4582qogEE33atv12MA_kCoCFCztPUjmpRg0aUlNlJGU1dmzDQeqYYFCv95eQ2jm8gpCiWY2CGvJpuguR57cMNhYB1poXKO8rFGzjwR0FoNmE505QLYUQ1bK2FSk8Uq10ju0LS2grgSsi3dWMdh7PHuBs6kHwLFWdv5Y2BXA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
توضیحات وزیر جهادکشاورزی دربارهٔ تخلف ۴۵ هزار میلیارد تومانی نهادهٔ دامی: چنین اعداد و ارقامی سوءتفاهم است و برای دولت چهاردهم نیست.
@Farsna</div>
<div class="tg-footer">👁️ 8.21K · <a href="https://t.me/farsna/456518" target="_blank">📅 10:05 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456517">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eN9V3x8jvFq36nF9mO86tIaUo11PtRLAVlCjhQospTgel8ohf73Jr8U9cFbJZ89ikspOdezml_wY6YkqbZmfjNcXSAjP-aBKTDCKstWh01kvo6Uy2Ar09Ipf6-k_xlqLBmTpBIwNmhlQ7F8ybCvgd1wT0a8PJkV2GBYX2MC8gue2kpEMzyylPBCofGSoIzZtnc--WlSc-6XtYCmoidTcGevtSHp-0327-sR3V6zW1pooDJEjGCEzn8TE5ydoNxsGfQy3nYrZfrQRU8pM1C1DhwmMMsTyyHA0fGDC2V0Zn-dXogEaeYNrTeqReSaCjTa1bpHmJnNe4WXIBFTtBbXt6w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">امارات برای نجات بنادرش دست‌به‌دامن خزانهٔ دولت شد
🔹
صندوق ثروت دولتی ابوظبی «لیماد» قصد دارد با پرداخت ۸.۶۶ میلیارد دلار، سهام سهامداران خرد گروه بنادر ابوظبی را بازخرید و مالکیت این شرکت راهبردی را کامل کند.
🔹
این اقدام در شرایطی انجام می‌شود که بنادر امارات به دلیل بحران تنگهٔ هرمز و کاهش شدید فعالیت‌های تجاری با چالش جدی مواجه شده‌اند.
🔹
براساس گزارش ارائه‌شده، فعالیت بندر جبل‌علی تا ۹۰ درصد کاهش یافته و حجم جابه‌جایی کانتینر در بنادر گروه بنادر ابوظبی نیز ۶۵ درصد افت کرده است.
🔹
امارات برای جبران این وضعیت به بنادر شرقی مانند فجیره و خورفکان روی آورده، اما ظرفیت محدود این بنادر فشار زیادی بر زیرساخت‌های حمل‌ونقل وارد کرده است.
🔹
این شرایط، همراه با هزینهٔ سنگین بازخرید سهام، نشانه‌ای از تلاش ابوظبی برای حفظ کنترل بر زیرساخت‌های حیاتی و مدیریت پیامدهای بحران تجارت دریایی عنوان شده است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.35K · <a href="https://t.me/farsna/456517" target="_blank">📅 09:48 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456515">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fd2592cfef.mp4?token=k_ol12mMzVEpkUUkUo8QfuEZYbJ8-TBe1zZI4s2_-4gRWxILlLwEONY3hfzEROLKVxyX5AUGbl25VCb2VrFLDbX-p5qk40IEiKJMOn26uI4AuZHTaqKatUx2J7sHzrGzxcmdSzCVsOeH-BqclEDNu9BpV8QxLiDWfacucadea989j8ujs8Gk6gAt-M1NtTIlnO6dOk_gyr2hgiLJP6Ghy4pgC6P96pjqL8fFIYeJDhB7_PAFtiQBlNKVyrc0BUKd0iJHIKJtJckYNdx_yTNDzkOfYqWSYv4Yj-T8VU8EnzWZK1Zog2IlIdQk58WxpwswaHpzDa5AONMvSrC7b96Wmw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fd2592cfef.mp4?token=k_ol12mMzVEpkUUkUo8QfuEZYbJ8-TBe1zZI4s2_-4gRWxILlLwEONY3hfzEROLKVxyX5AUGbl25VCb2VrFLDbX-p5qk40IEiKJMOn26uI4AuZHTaqKatUx2J7sHzrGzxcmdSzCVsOeH-BqclEDNu9BpV8QxLiDWfacucadea989j8ujs8Gk6gAt-M1NtTIlnO6dOk_gyr2hgiLJP6Ghy4pgC6P96pjqL8fFIYeJDhB7_PAFtiQBlNKVyrc0BUKd0iJHIKJtJckYNdx_yTNDzkOfYqWSYv4Yj-T8VU8EnzWZK1Zog2IlIdQk58WxpwswaHpzDa5AONMvSrC7b96Wmw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
شمال کشور امروز بارانی‌ است
🔹
هواشناسی: امروز در شمال آذربایجان‌غربی و شرقی، اردبیل، گیلان، مازندران و گلستان و ارتفاعات البرز رگبار، رعدوبرق و گاهی وزش باد شدید موقت پیش‌بینی می‌شود.
@Farsna</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/farsna/456515" target="_blank">📅 08:45 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456514">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">پیش‌فروش بلیت‌ قطارهای مسافری برای بازۀ شهریورماه آغاز شد.
@Farsna</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/farsna/456514" target="_blank">📅 08:34 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456513">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">آغاز توزیع کارت کنکور ۱۴۰۵
🔹
داوطلبان کنکور تا چهارشنبه ۲۸ مرداد فرصت دارند کارت آزمون خود را از سایت سازمان سنجش دریافت کنند.
🔹
آزمون تجربی صبح، هنر و زبان‌های خارجی بعدازظهر پنجشنبه ۲۹ مرداد، ریاضی، فنی و انسانی صبح جمعه ۳۰ مرداد برگزار خواهد شد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/farsna/456513" target="_blank">📅 08:29 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456512">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aAMAenRJR-71Rp5YtBz4EekmYcUyS6Vx5COChhk-XUWjntjMGrsl7HojXl-L-jt9xzskRVodxe37gJSPNzNAQLQU_SUtRXCBqPxoDINGCXA3mGzsGIxE9gCkc6F42lTaQtxlsZPyyasQfFu143dOB7PHJldmWDG9vVDFNk3WD3WQe5-jxTyqnt4uKWU0t8UL3vTCWQ9fAYB3LKg8bksJhfy9Z0W9DY3UvrKuI_irn5zzinUJfZ288prgalmCuYHA4CcX8rmSzorE5Jdyfj2Y_EPXMbVqFYwEaTJmOd1yuEYpMHClQ9q-UaTniSXFlgYZ1eFnbv2VAenAYM7dqfLWPg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تویوتا در تنگۀ هرمز روغن کم آورد!
🔹
جنگ در منطقه و بسته شدن تنگۀ هرمز، زنجیرۀ تأمین روغن موتور خودروسازی‌های بزرگ دنیا از فولکس واگن تا تویوتا را به بن‌بست کشاند و قیمت روغن‌های پایه را در بازارهای جهانی سه برابر کرد.
🔹
بر اساس گزارش فایننشال تایمز، کمبود شدید روغن‌های پایه با کیفیت بالا که مادۀ اولیه تولید روغن موتورهای مدرن هستند، شرکت‌های بزرگی چون فولکس واگن،  استلانتیس و تویوتا را ناچار به جست‌وجوی ترکیبات جایگزین و تأمین‌کنندگان جدید کرده است.
🔹
منابع اصلی این روغن‌ها در غرب آسیا قرار دارند و اختلال در مسیرهای حمل‌ونقل دریایی و کاهش فعالیت پالایشگاه‌های منطقه، عرضه را به شدت محدود کرده است.
🔹
خودروسازان در ماه‌های ابتدایی از ذخایر خود استفاده کردند، اما با تداوم ناآرامی‌ها، این ذخایر رو به اتمام است و بازارهای آمریکا و اروپا که بیشترین وابستگی را به واردات از این منطقه دارند، با شوک جدی روبه‌رو شده‌اند.
🔗
شرح کامل گزارش را
اینجا
بخوانید.
@Farsna</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/farsna/456512" target="_blank">📅 07:53 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456511">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dhIPmamgMTPGS2x5vrKAOCQFvwYBC74v5fqmp36s-WjC564iwR-CurVfq20qyBYYM4r2QZ70YdcfHAk20mWH9nuZXhdByRMzMbyCyJcWSYuA-wMDTGXQpvKxZvZpYiEAAFungDWUNMAdyxmC9irEhp1DtAqLt_XNuEj47T7EugKi71LyRAU2jG9WrDGgdDxYUy4m2SdOE0yrsElkTpVRjvuz2Zwo_ua13mcqmeUXQ9G0jIC7_0xlxCB4UDPuoQ0TA-nzqznehYFNHPeHdbMZtSFKOQoQx_r4fa0f9YAQKyMBhYKrWOLjUYJpZ_6ceKR54RWKPMo1qn16ZTcdhgV-8Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
معاون بین‌الملل وزارت خارجه: وزیر امنیت ملی رژیم صهیونیستی برای کشتار در غزه «سهمیۀ شبانه» تعیین کرده است؛ ۳۰ تا ۴۰ نفر.
🔹
این جنایتکار صهیونیست هم‌زمان از اخراج فلسطینیان و شهرک‌سازی در سراسر غزه صحبت می‌کند.
🔹
این اعترافات باید برای روز حساب و محاکمۀ این جنایتکاران ثبت و حفظ شود.
@Farsna</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/farsna/456511" target="_blank">📅 07:22 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456510">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس هنر</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/c7xyDzdu304Dyevdeq9am670-Fjq-Si087jWhPIn-5xgwfHSy-17GwOYVjKeau3Suk12qYSValnB33cuZ4orsIRO-XGfICi04fdzlETqYuT8LHA_SKGZFcZCJxbnp5Cv-kmRh7ia0ZZ_zfhpmx9n2JDQKzDHp64zcbm9Hl61eFm5qkRfgHf9220Xq7ivtxssgNgUrWVKGvne1KodBRvhpue_WguUqzp7Gdg15hCGoaqNyw7wGPX_9ZmwzwdrTvtfe9ST68ZiDtCuxE2S_vljbBRED3rWhXuuEa2tc-j1oQG4_dBVoe4NGO-wxlII5CJl4nhWbtcLVnL623fl4wpnLA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هنوز رکورد دست قدیمی‌ها است
🔹
بررسی فهرست پربیننده‌ترین تولیدات رسانه‌ای در تیرماه ۱۴۰۵(مرکز متا)، یک نکتۀ قابل تأمل دربارۀ وضعیت مخاطب تلویزیون نشان می‌دهد.
🔹
از میان پنج اثری که در صدر جدول مخاطبان قرار گرفته‌اند، چهار اثر متعلق به دهۀ ۹۰ و سال‌های پیش از آن هستند و تنها نمایندۀ تولیدات دهه ۱۴۰۰، سریال «تانک‌خورها» است؛ سریال گیل‌دخت هم  اواخر دهۀ ۹۰ تا ابتدای سال ۱۴۰۰ تولید، و سال ۱۴۰۱ پخش شد.
🔹
بر اساس این آمار، «دلدادگان» با ۲۸.۵ درصد در رتبۀ نخست قرار گرفته و پس از آن «گیل‌دخت» با ۲۶ درصد، «مختارنامه» با ۲۵ درصد و «زمانه» با ۲۲ درصد ایستاده‌اند. «تانک‌خورها» نیز با ۱۴ درصد در رتبۀ پنجم قرار دارد.
🔸
آرشیو تلویزیون همچنان یکی از مهم‌ترین منابع جذب مخاطب است و آثار قدیمی در بسیاری از موارد توان رقابت جدی با تولیدات جدید را دارند.
@Farsnart
-
Link</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/farsna/456510" target="_blank">📅 06:53 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456509">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">هشدار سطح زرد هواشناسی؛ تندبادهای شدید در راه تهران
🔹
سازمان مدیریت بحران کشور: از دوشنبه تا پنج‌شنبه در مناطق جنوبی، غربی، تا حدودی مرکزی، و ارتفاعات استان تهران شاهد افزایش وزش باد یا وقوع تندباد خواهیم بود.
🔹
احتمال تشدید این شرایط جوی در ساعات عصر و شب وجود دارد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/farsna/456509" target="_blank">📅 06:20 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456505">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس معارف</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/fQGP4jQLexWjc-zs225ubPataPiYsi397NQROYa2Bee23bhJncbn0ApjK282Ev1oB3CSWuz6ncZBHM9S0hE34RsYgqywRUqPJnju4zwFLoR0K1GOarZ75-qXrAIBMgTg7HjiR7wu9_QeoT6kM4_dBb1bXvyReS2upuvg21NoH68vaNVfcEIozX27W5E2TPrWalmF1kOAbGch-DHRHeg4FlM4s7-1IXRHVP9xJR9SMtfAecN5pX2LdTeyxMH0wp10ILXbeQg_0YPotH7rQquTVQHMjWAPH4WQ2kQnkMHvP6etDpWav3Xfr01_DmMpejyIYruv1K-uljdBbKj3T4noig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/OElXG6gIZaPkLpQ4dx2D0wFpeKgNlNOSIoWzHwN9-jGMXVSlIoCM1xRgz-GSLv0lJMrO2Jt-lil2mFRgUtSSzilkGkRf-27hc--4gygKAM7OSkzyjOce1Bg4w9_kpRndb6JBP_NIaYu-Ep8DpXbCInquNVsgFvazzhOQ42BVhS0EOoUIA_tSTuPeA65ysHbUVRHZpMk50DVWGehg3AQZvuzeoKSf6_c9BH6SrBsWKXNQxKy78fazASQo-nwZFT7Jtb7c-0zPp_jfGJyKCrfj1b3uqCmvr0bS3Fs-f_acIr3I1sbBMw18tVn_bi7ZjRO1acivvPH--3IFv7a8IfSOcQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/H08PZlZEk6pPXPVjOHnfpNrY2XYKOSAF6FHWhWvtrv_aE1JVRdNsQVZS8hrL_tI0epQzZwnGiwtUXKrTuxH9wOJQ4WCZfe2YwGIAs7SNokCmetfwNz593J-RpLN3B15zpaRRxGCF9GxqsNkBxOo8IF8zj8sWXq4dCLHASRvaPf1rIZ8BVWsLEnYB01qh9cZW98clqkXssCXeMcT3yYxQOk22xpM3j_ndohAz-jffHbvDknlnptRq66YY_hyO_e1nhsOgXn96WjqHpes9kF-46c_Bz-dvz-cfJknK50tC7Kn8yr3Z-sAY9rPshu-m-Oyr9qZAUaMQ439L0ubjiqFDCw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/GqrD8a7YbmDrC0N3emsXv75-HsPda_pI8avj-1zPInNqEn-d1yoTPcsOdnG1Py8laJKkpgqL6lQgha3nILu7hIi2K4jdQIYBDoqVtZ4_OKj93S1ApBLrRhOCsa1I3NVcIGLPmo-2GJ114_0jGPwl0_mV8-yVkdogEWoinBEkOCGNaNv18Mwjz3PczOuLeTWIvS2Yz7rjOAJHn12ygD7o24XbfjpqNek0sUJHHgn7Y1oSJIzJqm8B9O6SauNjksdSQ_e4oW7bq7DIblw52hZ5qH-wY3WTZivjHxvoInQwhwsqGlKs_NQafl6ZlkYIBN5OaAJaDch9rw_mz9jxssWqCQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🖼
از مهمان کار نکِش
@FarsMaaref
💠</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/farsna/456505" target="_blank">📅 05:43 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456504">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/I2WkpjCkKXkZNRqLTrTb3U0aJ6dwv8AFO0s7q6Fb9zaUFVSIwhh66W5xOl84HsgRE-XbvyBZnqsauGRVxyumZ2w31LCz7L7nnPjOpox3ZHpj1dKawrxme7LhyMxmegelWCIqVpaZGP4NchVq5r-a097vmbIEv_ecDkU2NhyDBWaLpPSJsf3ep8znZAqeOT6Ybhb3rk3sfxgL72NwKr6hQXj-gxAVbSJXpAnvaBPjTnfekGOi-w6c8I44proUo6Lh7OtV8yoLum2a3JyjsqV5qrll7v_trbovP2UJFwWdY1jXI6Mpn3avgKIR2GmB42jzpkNoMb6FF7UE3_JyJv3wNg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بی‌کلاه‌ها صدرنشین تخلفات موتوری‌ها
🔹
رئیس پلیس راهور تهران بزرگ از ثبت بیش از یک میلیون و ۲۴۷ هزار تخلف موتورسیکلت‌سواران از ابتدای سال ۱۴۰۵ خبر داد.
🔹
بر اساس مادۀ ۱۶۴ آیین‌نامۀ راهنمایی و رانندگی، استفاده از کلاه ایمنی برای راکب و سرنشین موتورسیکلت الزامی است. با این حال، ۶۱۹ هزار فقره تخلف مربوط به نداشتن کلاه ایمنی بوده است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/farsna/456504" target="_blank">📅 05:06 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456503">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/21499fbbf9.mp4?token=hcDSc-k5L9ZW9cNVWgiX2CTWZV7NEhgvJRtS6MkPzQ1d1CU7X_bpPv8Hdx1aNyowTWiBRmB04IoeXDwylEnCTlAoaxvPhMBbY3Q4RBay-Zhq5uUF1cTJ0r3HHZ9uStuDXqG7E_w_pzcReZGXzHm1zcO4eDATrL21mUylWil-kJ4bBJ3CRdl2f24CPiiKzwotTh0OJ3E9m6W78xWl0Lf__lFaJN4fiH4jxQ4d796sAenz256oD5E9oxaSj6OpwaefnmHFNnsHRJRB3BD0jjmc3Du3hupsFuYsQrxA_pB_N-QGv7bccld8TUeBxlbhJKdkYgkQ9k8Jg9IA7wI2a_KiOg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/21499fbbf9.mp4?token=hcDSc-k5L9ZW9cNVWgiX2CTWZV7NEhgvJRtS6MkPzQ1d1CU7X_bpPv8Hdx1aNyowTWiBRmB04IoeXDwylEnCTlAoaxvPhMBbY3Q4RBay-Zhq5uUF1cTJ0r3HHZ9uStuDXqG7E_w_pzcReZGXzHm1zcO4eDATrL21mUylWil-kJ4bBJ3CRdl2f24CPiiKzwotTh0OJ3E9m6W78xWl0Lf__lFaJN4fiH4jxQ4d796sAenz256oD5E9oxaSj6OpwaefnmHFNnsHRJRB3BD0jjmc3Du3hupsFuYsQrxA_pB_N-QGv7bccld8TUeBxlbhJKdkYgkQ9k8Jg9IA7wI2a_KiOg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
شور انتقام‌خواهی ملت مبعوث قم به شب ۱۶۹ رسید
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.91K · <a href="https://t.me/farsna/456503" target="_blank">📅 04:35 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456502">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nMPrNSNrFUW5jmbsHukj_Rt5DoeRY1xEjMOG2LWMg2GoekOhAQUgxNA2MN4xxt3jiwN-LLocztCQnAXYG3SdD5cpmUKWL4ol2WrkJ6DSfrPS3ZUn6O19cMO6xug2gXOOK346pmBpNZt-Jw2s7XMcth5vlS0IQ98sQk7TZ2KvWK9HoPwu5ADF-JMhC1adQT1LC0CBm24mBwcswhj-Yzv2Hwoge43j2sS64yY6SouO_vowvVR1ECoLCZDhOkT-RmYzHdzQ-I18SHwrCa2n1YMA2Q3Hwajq38diLv0n1zLkCN6CV-E7kHRPKfoz_mWgXuPxCEpLxoecp5KwMcjOfu9TRA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">۱۳۹ کتاب درسی در سال‌جاری تغییر می‌کند
🔹
رئیس سازمان پژوهش و برنامه‌ریزی آموزشی: با توجه به تحولات بازار کار، تغییرات فناوری و ملاحظات دنیای آموزش، ۶۸ کتاب درسی پایۀ دهم و ۷۱ کتاب پایۀ یازدهم فنی‌وحرفه‌ای و کاردانش در سال تحصیلی جاری تغییر می‌کند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/farsna/456502" target="_blank">📅 04:09 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456501">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/caf9ea2519.mp4?token=eEayGC8d9t3AOMhrN3NtRiVtJHgu28JlAzZ_6Pdnr3Uktf5rrBnpJ-h7Cu8ROOHurKGO6wQsRuKNZrQoQuKjJ1PfYv_XII_-digx-UipYHkKPtrMoOHUQPyXTPBt14M7NCQ0itiumAvl67UBtlEn_RdaI_DKqyHfGiXt7gxjep9Mmt5pN4l2eOeDYJOnSFZ42tyNMtfd2ZxcvGjiLxuqWEBrhjxCOTY3jRTRVim1yQo1uLMn0o0NmvjCGRm-_qTNX0UgJYSLOYfyPR_zGR2YzluSIXP6GIrzfvWJNzAgdnkBhJIYOh6R_JKOXmTMfY-xkHNeegAgD7TwbJIVvKl3yg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/caf9ea2519.mp4?token=eEayGC8d9t3AOMhrN3NtRiVtJHgu28JlAzZ_6Pdnr3Uktf5rrBnpJ-h7Cu8ROOHurKGO6wQsRuKNZrQoQuKjJ1PfYv_XII_-digx-UipYHkKPtrMoOHUQPyXTPBt14M7NCQ0itiumAvl67UBtlEn_RdaI_DKqyHfGiXt7gxjep9Mmt5pN4l2eOeDYJOnSFZ42tyNMtfd2ZxcvGjiLxuqWEBrhjxCOTY3jRTRVim1yQo1uLMn0o0NmvjCGRm-_qTNX0UgJYSLOYfyPR_zGR2YzluSIXP6GIrzfvWJNzAgdnkBhJIYOh6R_JKOXmTMfY-xkHNeegAgD7TwbJIVvKl3yg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
حال‌وهوای مزار رهبر شهید انقلاب در رواق دارالذکر حرم مطهر رضوی
@Farsna</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/farsna/456501" target="_blank">📅 03:39 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456500">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">المیادین از حملۀ توپخانه‌ای رژیم صهیونیستی به شرق شهر غزه خبر داد.
@Farsna</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/farsna/456500" target="_blank">📅 03:17 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456499">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LV2N1XCI2GtcxHGGHFYrq8KpdBClIkPYD1QODIl8n3NEOZZNXdPgnD2wsOb7yPgdJa--Zp9mj9_bLhp3VIhzTAUti5KJ26-fX3-pS3Q8BrJlH1jbi7d5K3OoKVAC3oPscFbRpW_d2u8_5ZMePtxiAzbXPN5Rwdw1DLWbtSer6Zphfmt5bIpKE9eU2AN7PETMnnrmUgcWKWpUQR-r7EmYDgtgJX88iQwFi-KN_Tq0juY-TL_70cauow3YBm2VyIiEOW4aZttuB1Z-6hfgMexGcH1hYplxHZtWHp1fE4Ljvu9WBRpSY4zkVvT9Ok-bO8RfP3Hns6MLfevhFBjXKrJ4kg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎥
اولین تصاویر از ۶ متهم پروندۀ قتل حمیدرضا رجب‌زاده
🔸
حمیدرضا رجب‌زاده حدود ۱۷ روز پیش ناپدید شده بود اما ۶ روز پیش ویدیویی از پیکر آسیب‌دیده‌اش در یک کانال ضدانقلاب منتشر و در فضای مجازی دست‌به‌دست شد. در نهایت روز گذشته پیکر سوخته حمیدرضا رجب‌زاده در اطراف…</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/farsna/456499" target="_blank">📅 02:47 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456498">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس علم و فناوری</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qEmB5tYDSX6L0CAcxciB4p3_otluUpdAMrRmi6hSiPhlG6puopFgpDOs3NrpDFd2Em2flVstwMAgXE_JdFsf8iwiLbjNV3NegqUkewMGwoHEbCCBnI7kv0nfWEleIcKpwYUJxg00ejm6W9Fvzp1O0VIAKxbxz08hY2BmAORPFc2Y61NDgQMMK9-5tVnFQCEAGbTlW2zEy5OQHPgNCzV2Ge9gQNCvPj09Dk1fBLHamGsJe7BGAPzPHWoe9sshJUY34CWBIhrOWynm1ShR-MPT6mJS6ZXX-J7xfGN1YJP0Gg_WYEESQRunCTPcAU9TZWVfQyx1BS2-cgw72vhk-y3V_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تبدیل کشتی‌های معمولی به سلاح شناور
🔹
تصاویر منتشرشده از یک کشتی کانتینری چینی نشان می‌دهد پکن در حال آزمایش تجهیز شناورهای تجاری به سامانه‌های نظامی ماژولار است؛ سامانه‌هایی که می‌توانند کشتی‌های باری معمولی را در زمان جنگ به سکوهای پرتاب موشک، پهپاد و تجهیزات نظامی تبدیل کنند.
🔹
یک کشتی کانتینری در کارخانۀ کشتی‌سازی هودونگ-ژونگ‌هوا در شانگهای با مجموعه‌ای از سامانه‌های قابل‌جابه‌جایی دیده شده است؛ از حدود ۶۰ سلول پرتاب عمودی موشک و رادار گرفته تا سامانه‌های دفاع نزدیک و تجهیزات پرتاب پهپاد.
🔹
مرکز تحلیل چین این تحول را بخشی از روند گسترده‌تر ادغام ناوگان غیرنظامی در عملیات جنگی می‌داند؛ اقدامی که می‌تواند تشخیص مرز میان «کشتی غیرنظامی و سکوی نظامی» را برای طرف مقابل دشوار کند.
@FarsnaTech
-
Link</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/farsna/456498" target="_blank">📅 02:43 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456491">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/EsNEiU8ABHjzqmHrrfzlYZyaPRdP1lcGst3zrMUnDWEgqYMaOtCH0Bt7X2m3FgacROIm0Ef2nD5EU8m0db_8aVuwjvE1Os2hghJ-q6vn0kszJkeBQ5GaevhYWgGvIy4y_kPH3UMZB38mklXUIZVgHZHzkJAriPoaMRQhhEf2xSMV01aKEIKJ4lbqnnueODaCuGFNqLMUOM2Z0-QO9HsvR883fiWJB25Vwi5TdYNbCXNe_9TTApJNakjsADaE_6Kw6NnM4DjRR8sUQcskeGEisepASgSruM_qJQuaVXBaDzoH0Rx2QJKuMHBRCjM8Rh_RoKeomSCReLo0eb0gVg2lLg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/TvpwJogorfBseUKuXvYTKXxhsWhgTwXylW_qUIT6c9A5uoMin4hJyyAJ1ZXdBXb42RAZO8hlWhKEHFX7gP00VMPkB6SRIEAgNlPMAHdkolngDdUk5xq9Vq467_TXpvKoc7XTtbG5M_2LOvY3WsylTqyBF7S_zeIniYJ7EOwWJM0w47m6_KxsXRmnCp-XX3NOkW900Q5NtXthQW1sa1kJVjfoD8Qd4Sf5fPDnGsZ8o8YOKQkEcrq_RowfvmIgoUSPjJIXQUPzeyaGWaEzNOVSkD31laeq2eXBw61VDsUFUMLcBSHHSZg8T7S7jlw0WQ51Dd3BLPOmTdbi6pi2aCnTng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/TBxqC_vnIi6qJiSwkPPTKJCdma2_kokfgLMfcZRlwdgnVRg_HU4blB5ZC-nFK9EJlbYmybYGLCpvkpcybr4pb09uWzZt6iV7CaPzq0G4cj5TOhFPXKTC9FAsahs-hpU3rN2HyesobqyjxToox1Lx9WNbr3wOR0xQU3Vf5XzElYlO65aL4-jymHTNG3896gACOSBAiSQL54yZyCnBEil0QtgaP6XPEoAAj04SAbw163EhVsilpJIBs0yDWGXqkfWjMq5PCV-lhR56ekxyO1Kbs0L51W3gXAHLFP7Wm-JwGzM_DZ5-99ApWQcq_MYHQezHMsce1rNeXFD_KDPWTfWzRA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/pB4fraDEPM7BHvyrtZdTYuTgM4Ce-HUJzb2AKrXP43eN3nCjYdUf3j2jZkOeS7FjbpMXjdqSBItrTfV9YDhJ9UKn_GQCvLiJsDxqASXKKoNGn8W6rA0bAStvlLdsp1uE9SZySVaV34SP54LO9d33X-EWZuKJ5swTCg3cRkHmog3C04bGLm0QbUHl2xaI18OThrnmAaqLSIkYA1SElhjE1Vgn0Y5AR1LesXOfLKq15ZJVxs1bIq4cOZkpxbxzgpfGwDgW2srXiSCCgp_rK4NroWFbebYcK7lVHvqlm6dOlISxDJEK3AIycLMBImMb-HJqQEwLRW0QKUhMloO_-JJxXA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/UXIF5xiTY4qu0sCttZFKHupqEYMrd0JXPg1r_p12crS9vNrPLPObphJNEHHeaof3Bj3VmXzR9r-3bZ7n_lHG07ZFndDUOIRu6p7UkuSWpSCC0cpBrYQFTGWsMnSwMhx713F0EIWI9W7OZP1poUaNJIjINavcAoUNDlmt4nbTIqb367lhLDRyBL5W4JWPewiXiMXGeL4VHuPQmUme7rv1TZFxJKwW6Ld8KR4bcENK3kzIySdZSoHFgxIGCYhidAP2jkNlOnoPaOcmmn-EnZOOUzd_i8O1f4ckw76OY4l4P1lfkiNDNLE9QktEztuArx9Nww4eQhv4t3ewIEYjr2t0Cw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/a1iL_Jv1rPOJyyhQhkqHJIcnSsCAsvX00Yhde5hevZyCQA_QGEQ55OtFb73u5Hryz-1AKWQeGMdUVtuYozgyqFNbFaLC7SeoX-wf2Bo9YJ1TZfG5aSQ2moOdLEtxhYP2kwchgtYPaH5QjvhmBvmhAvIHAFn66KV8g7OXVV4KQv_PsOe9DBAd61jjpwdE39Zgn0WULtrK1eSNBzf0D5X6-_jUaF77oliOa452tPhJkpZNi19_Tha4AWdd8xkRXPVxti7gNDgnSRzXgdidUMrDELq5m0MlBN54Ow7cAE2UkRXaak5kcTOSgBcQZe3fCF2SkhnIejCxGLsoyBYNggMzPQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Pbb79ZchnOlLCm9NoaSmx1D8hxeH9zM_zfZ6SdbZe8AEvSoClUoleAqR2QuCGKKycy0EnvKs-EgjqcNRsGDwHfpenae8fnpGPTM6FN10lAa7NN-HPGkyCE5GspAcby4Y8iEJ69nN66mcCQ-9R7zOqoSt9F44JHxajvEa_uPuSE1t2wtbhKIKJ6DOx1w6XSOwEmjEC0NqJ-RL1dPVpzOM7h_SIeQ6r9vpgs6Cz1CACp3xId4RlPD5IVKhxS-hCHRGi2EYDzr0lbsn07u1jOl7_l8hyAH-hznE1zz_jATuCHU6UWVmKsl_c-weTKSsoDQqhTYBnfTk3q5Qhu0TXM8t1A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
کرمان در شب ۱۶۹ خون‌خواهی
عکس:
مهدی امین‌زاده
@Farsna</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/farsna/456491" target="_blank">📅 02:15 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456490">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">منابع خبری از حملات رژیم صهیونیستی به مناطقی در جنوب لبنان خبر می‌دهند.
@Farsna</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/farsna/456490" target="_blank">📅 01:54 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456489">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WpSGkLSbvHzkFJoKZ30unKUfbsxZicsg_sxplfu9L96uINK5KN1PLvZASm3HLeddm5ae-d7_StQtJHT_6gCTDr_0VaHyhwIrnkSgy5qw9fDG5vRxbm0KFswWTXSaHMRQDBXfufV_DTDLjRd0De-4MVYzicmJ_ltFQsThkOc3flLMUZ4J6vNlItitK4OuzlFmT12Rh8joKdtu-gKWZsRdRYWUrviEn5wSRFsR5ruc-_QN1TQJCwA-pnNNoXIs9cFdqmnMVDQBMySXlzC7QJabVVI8fVfG3uhViP1_AC2oPXnIG9GYtnlOWOhVUvjkMF5A_HirbmxiMWzZSdFKnH80xw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اردوغان: اسرائیل آغازگر جنگ کنونی در منطقه است
🔹
رئیس‌جمهور ترکیه در مصاحبه با الجزیره: اسرائیل عامل اصلی و بازیگر اصلی جنگ بوده و تل‌آویو همواره گزینۀ جنگ را تشویق کرده است.
🔹
ما نمی‌توانیم غزه را تنها بگذاریم. هر وظیفه‌ای که در قبال غزه برعهدۀ ما بوده، تا امروز انجام داده‌ایم و در ادامه نیز انجام خواهیم داد.
🔹
حماس تمام همبستگی صادقانه‌ای را که از دستش برمی‌آید نشان می‌دهد، اما از سوی اسرائیل چنین رویکرد مثبتی وجود ندارد.
🔹
در شرایط کنونی [لبنان]، اسرائیل طبیعتاً متجاوز است. لبنان در حال حاضر به‌طور مداوم هدف حملات اسرائیل قرار دارد و ما باید هرچه سریع‌تر لبنان را از این حملات نجات دهیم.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/farsna/456489" target="_blank">📅 01:33 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456488">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JCQi-Nk92zDUUrvC4_IwcL-6SS26-DRvNs1pPOXK3jYiQncujWUfWduR6bJ1J7mw5Nsk_7lPYB0RvFcunnMmvk-CZtHeIc2tF38jGz5EFYpOVHaJdhZUEsUr1ifnDy57sHbUfhjiTHHdig-xyCoLpqi6TWjhOnKfwEgcj-IAUjVcW_4YqPaU6PcCgv866wSgNSveadfQTdPDj13cUoanjIrExUZdTR7raMR-ZwOxza1fRw2by-v6pg_aiBfb--yLfzTnEZPorZZeux3z8E83bNZlcgJnz0PSl5lw52qK6TMy8hymKvyOliDkFhO7WC8B7boYFKDRcQQugX7OjtNUCw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خودکشی یک نظامی صهیونیست دیگر پس‌ از بازگشت از غزه
🔹
روزنامۀ اسرائیلی یدیعوت آحارانوت: یک عضو از نیروهای ذخیرۀ ارتش اسرائیل درحالی که مشغول به خدمت نبود، روز پنج‌شنبه خودکشی کرد.
🔸
ارتش رژیم صهیونیستی با بیان ارتباط احتمالی خودکشی با حضور او در جنگ غزه، اعلام کرد که پس از بررسی، مشخص شده شرایط مرگ او ممکن است به خدمت نظامی‌اش مرتبط باشد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/farsna/456488" target="_blank">📅 01:10 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456483">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/JYSLXWEvuCi2Ie1Zk7j7TYGmIg7EeiiqU7t5V7_1xStDIX4lHIdOBnATdolNWRZU6JUphn-YfsuLKzTbitBVBl-4g-pi4Q9S9IMkowSmTEgFEsydoVAresnqEuXjuXysUnC1hzeq9Rf6otgDZkS0BAdJANUjGnwXPcgJV-cZbVw37nmbfFTdo08CbGmlkMOvDLUNi3vo0MFW9xThz8UEW4J2j9LM3EFSOsyl3VF8ydgN9eincd5PhxRUt0yPWr8j3pbhFSxk-ov7Q5j4VwpJ9mb53zotiy_9xcbB9SUJoA6yJr6BLk60QmvZRS_Mo98TKcX2LWz_wfplB-FM2nBFIQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/oNGg8NrF68-m9PupqKNlTeIVA_R0aVUuyvcP-32ASj9_ysHL0A00a3NB556w3cLwNcIvJSkLrgOFVwBnk_U038IE-h5T8Dh2WdX_8KeIO_xz5sJBA5D-XEdNArCvMAdGD24PaqXiE4l-icOMqlX8xzwZLN_t9VFebe4nknIo_IkR5PsrfWP-swKhGPUtMPAaLKbYTUwamzrxe-OptWPnKJPdbGH-IHFnsl7Pu4BcyVSNV8gBJuMuFgO4cBiVgky3bzS1lhOJ2JsM1HZkZshs8rydQNu7IQ60XRaIjSNXAoHNPpkPyECijtXP51H3K2Gqogodrw14W6XU6zuoqlzQUA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/KMtmd0zXUDE_wgHFJ7LzM6_RpB4LWqAsp-s8tFb3I05_3-pWkc6m08Zda6fbXZPDzv8CknFxyCJBJ-L26ZAOSKMjSwsS7i6mcbelzFFFqj2FIDKT6DocCFolWMYDsOSNdWAVvtZBDPAnzUvE-VAns7x810nqU3Itw4_apwjS6Ai_YIgZvxczQuU88GCIOVuQqR1awqR8R5HeEc0lfTkFQGNGloGkOWI0aQuEUnxL7MgSsnfuWdCSoqVy20zHIisqw9ErXhku7xQJARabeZWEuHFo0mQS2ucQXHb_R4E3p7f3his1wi8C5zD1kzhpzkIGcReWMbuqUHJNfIAj056uRw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/UAQeeZ5L5l58b40ciLg7UJF1MgN9YHTiUcqCCTP70qeDBGByTqElUWQfJVo1AAimvdQu_KcfPQ4pd4LJusibheZS86r1VzbnbNDiXPolaR4XAowlyfRwaYxmUIjA_01ybFBZ5lmdQklk62BoRkAN8jBEWEYaaTd911nwDoDapStY6qyDoqn3TiZwsI5KXpzrdFlmBDSAxFMSu6-voFrPohWj2PUOcHm8SYgj7mlbr8LOO4pt1VJZuQQtMYABZw4Qw2FSAS-xSwVY2_Zphd_XfHeUhxqXuGaje9Q_zyyaJB80yvWLzRamGCmaLk2T7eQZQBKsradLjnRIn_wGgM9LXA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/K6SLQUUKJDHbM3BytnCdfaaKP-Zb6ACUO8WE01Y8hf-7smwbiBDCpfmrYBPZ57yJQRcIJFK2qvYWpCYi4xBBQpBDmexgYKPP4YK2oJUdIg9BRwNeLQjRf8plyW49bz-TdIJLe3aeSt2M0U8-Wz1ixYz9wXkiU9ZeCf06n4GY_BPqnOoHltUCSjA0sf33-BcUVvemI_dHRFcKUL984OuazRQKjjL5MHrPeKjQD6E0LwhpSbiSlh9ozFoTKo5kAGBpz148BRLSJMAgldREtqmUhZ2uxigauzc51C-tyUY-MKMWioYstg-aBwd-6km4ZVFODIGV2OTgcYaQmCQZ9jIZWA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📰
دکۀ روزنامه | دوشنبه ۲۶ مرداد ۱۴۰۵
@Farsna</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/farsna/456483" target="_blank">📅 00:55 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456473">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/sCbuzwFGvAaHXaM-x0sJuW4NLFYyE6xzZP-xlQbI_OZY144wkz8_XIwoWoWW0g5eIHwhVffUveQpsMXN6fQ0juIHJIcI2iamhA9hmOSZMYKmpKjYCnChLiHrEwf4MTGNeKZ82j-3wcXQAl92oTpKrewL2LSv0Vn7-bfxVi1EiwV_fHyYZ-95N-rDqMVzSwO3FeVxD83Sk7ghCABoCmPX4hAJBCdqRl2tQMkUgiNP1rmAJ7J0bVmqgOejEGVkc4_rdLrpiRWPoNUnkWE2EGuSmTPveVjDBXqQWzJbpnpR-UFpFmOj1sMhqqdwmC6XqaorTwBkoFEBS6CirwzaDsBuAQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/oZSuCIBP71-8XLsCN4Tc_JbXkLFjUXTDfEHrcvas1JNtAbmyckKB1c5uDzYnY0LmMEuIaT5VP9mybk-gc2rWWloZxOsRkqSk15fboQistHrUhshXOhjv-4f7e5wPPAqF8x6S1l8t48faspMlFNxk9wlJr3_6yWb2k0QI1Zb8VuoCei80juA5EK2RSq818htYIK68aPLljSOe_q3_xhV3V5Lfoh5fuX2K6vAbhZw19s5b3nrDerb-iv8xdh4_7rGthTQffBfLCLqQBahTigXwaFYWrS0gGHZG-9KNmQGfduIEaKVcO-8kMoegngg_yU-ceukJkD9Saz42QbYkG2US3A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/cOEOdPi9yyhMaT56XwIkqpbQg90hI2KjAITQVbU3bc7c43Rm5GlvK22KV_jCYVaktnL6Lmc4Ga46KrW7ix4WI6TqBOQHNcpMj6OhBg9BGm_whjS1iaPs0VK7MOqOb7w3QJ89F7JtAqqZinoZu0MnzssrryxKXnJfq5DGq-RX_y3EM3lmUjTuInU2_2XoqctcUHKWIPi9FGezJ8gy39kVNArPEanFY6VdDjkcm72XhCQuDNGddzzKFetaG26LUyvuTtDXk4K4L92SBxx5xsCkRVRRCyA062ze_lhnXH5d268PGUogb4DDGXCw31gTuGjJ4ePlyl2gYiOhP43EgxgKLA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/RlYvca0z8KNfY4CXon6Y95OkCE1HPfCavEdaXqtyHvfkN7x-msvZW1NKT6Tx9Sq4vAZd7yEqx9pRZI6vMDPwhBPMsLegT1FNXflTI04rISj5BOzPE6ZpQrU-31RF8zEGlbwGOMlJ3z4GCTrcTm8x81qKiKb85tKv40TUsjf-4FVvAAyJY2JAu8djkE_2B89Dgt8MMRliEubEdbHGIs75iozezlgIlPji_7So5ajgmkaY2N0WyTGN0PmeOek6CGGsh6qPzd7NL16Yq2xzA8oP7r3q7NXgtRfJkIXO4ITrM873Pn_JescO4FsaotquqA_ymKt005Tuyfg_-D-VB0xpHQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/giUxaka_kv7nphvmdpKakknofYFqMXp5ntJbtD7Sw3J_0REUkbTcR6g0QGzLE2GavrlRAGxKuktmafjroCiP12a6s_50vXzkX8tV9L4NJOdc2aSxea2ClNAWBrKZGvhqWqKPFojNw5M9ZcVd8C4P7ojW7pvcwLRJiIRsikvRU8-8cbluQFybhzXOHoJTYzIVFXEb635qIY5r61DAUj9LB_Va_JF1-gzs6P6PXyMYpRQoB_-nxGzPwF7u9Orlaa_MrrU1fMIw_HAqibgAQtRrbP-RNBalq0N5WYviEj7mf74F9yXciaUdSzMnZpuFbhvZ_1lPcQJheAEyJAwhtikZMA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ict_GJvG7AEroxP9eRPdE6BfGZ7uaEAXKRi37axq0nXyKF9NBZo6pxV6papxWbxLrDxpn4vq9XA7pM85mFpxAbEysJNCXd-3-gK96PCwmKRJd2uoOCEXFVP9kwloSQj2Nnc0m3IVN62DKkWlVufkmEsI7deWDD9sq_oXsOBamSR5rpGO1969vbLc8vTyIHkm-fJBI9F3RfG13b-ogx8ZAc6B00H9I--h_sPKEKE1z-ANbCKMySq5b-5CsZ_HoyMpZw36-I16kM8uU7nmI9UTUMtplco4-w-mOsyo6KjLb3dKZ6HTNDiT0bjl_e8VlQbmjxgpTK9YLAN1PmVUT4zgEA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/sW2c7NsTZg5I9_iXoaJOVFi2teZ9hxQ2ujNRLypjpBT-eJ2uon8HMNuVycdFb8HJ6yKBRU7OnJuAEwCzElX6LyJHfLJOQEn0DEqgWfTT-pGUjYUsEXTdXLs7g50O9KNPIgcE9Rwa0l7X5e3H-T7jpHTJe3V8Rbwc5uYbCfQSYVM13CVyXsJtfJJ-7--J-EJfM3_dfzXXeEgadlMTIg22nKv6EbbsoK0dnrDoU8WhnxBpwBzbrzQrUBaNPEiobyKQm2U9mcuNJP6gMFsZg2Ok9EnGo-6RTyesBhp2V82Spt69u3v-tlWwaTl5CzUVS0WspvhlbJUlN22hq00RJOLcpg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ce4vN0IVRfMqiTqCzBXgQs4XAY0utl0xSKxV-Pi2jyr7oOUu6XtrAONXMpYNrcr9lK-diJE0oXfKLmXnGdNBljAJf8uhw27K3OzJfZM7yGnkolPDGoEI_RZRBnPlMAbUN3YCsRRO3WBiMhQLTfWGEMu85-7a8LVxE3hscLnZz73nvFTtNcgGZusm0Wm6jVwoo3AMCeTCng2FcLqLGr3DgE8RHQlOYo4UTj21IzQZnZWyGsNVEN1WiyGyM8Mx9CwTETUxRlTUzRE9cC-TS8NZ4GWExo1NAlNHpt3iBkBYHm8KSIS2vog_DhL_8c0Wum67twvZL-izRn02YDsCWxFmCg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/WQAe8j5j4-cthQfMeEUx-TFqQX0Vu1Nms4YN7FwMH4IXJPwHCwoge4xeYcm3TY_a3aoJKr1HSkpy__dwjoBriOIY39bMiOFe_JHlt4XLdabgdHXtO2Nb8P1FAK-93Xx6_1eO0J3bvw3kVjGPru8TqQ5wqX638bHrZM4zxiCKQfFaLUQ25EEIHp4ZscahC7GLZCZtv_wAe7V79bg7_3HJZADPVfk3UbLAdZLcODxHkgL7b2RxZ2QT0Q-k5zj6pcik7VU1ZOi6o1gBFhG0XYhDY6JHh2H2Ti3SElBDop-2KZbT2bDTdohZeg2OBkm34HmVHhxHlZqWgUghSjDtE9kcwA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/orIH4Re7wYGmMz9en7gg7EYdDf7R1g0P-5pNtvXUWfGR0jU4ZgC3T2v9JuaTh9nB1YItSDLk8s3sLhN-AxTBIlJJYSBNt124mFD8mFOZHT42MQQYlK-XG7uHs1m9xP4775TQqm7eDzy7KmCfEAVWy_fQbmj-fPShMgWQ1upjWHl0897cQuTbWflYsM-pbZob2KS2Go-FewNCp3hapyAE1aC6Al18CfwkTr78jCDi-KmZEPW5WEebnu4M7Q7KZvRrV1TjDlcbjgTs-36vB1xw_E33szpdkEiQBxHiVNj0rwIGNKbZ2RQsoFhNxXTAhAJjCkNToOsUlti0iKhVXe06DQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/farsna/456473" target="_blank">📅 00:55 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456472">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PNL5vanHkMsGntUizANTZgLEwa5BnfHd1bJF7-cflanaUGfnpeteEIpCRhYxzJtw9IgN6Cs0FGArbhSuMB6i_mkaPQEy4nKn_EJUI47utVp5QLGb9escfih260HI3dZm5AO3-iZgW8lI1uxYKUUsgHb31usg_IAFMEzNXBKKrYYrO8rdlQZMbq0j3q1xj79-X3T-7a6o-2kM-_WlE5g5fiULbgs3jXUiYa7Kfzh5RjpFw2PojLIVqGam_Y8sHoANDDFPuXZPsoM5B-pEmCi3eFueZTCAotFV_uNIYmqEEZiAjqkO-kzAkRcZm6zdp2isW99cxyATlGQsSNVYuFjhxA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سپاه: پیام منتسب به فرماندۀ هوافضای سپاه جعلی است
🔹
روابط عمومی سپاه اعلام کرد صفحه و پیام صادر شده منتسب به سردار سید مجید موسوی، فرماندۀ نیروی هوافضای سپاه دربارۀ قطر جعلی است.
🔸
تنها صفحات رسمی سردار موسوی در فضای مجازی، در
ویراستی
و
اپ‌اسکرول
می‌باشد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/farsna/456472" target="_blank">📅 00:41 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456471">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">ادارات مهران و دهلران دوشنبه تعطیل شدند
🔹
با توجه به تداوم موج گرما و افزایش دمای هوا، فعالیت ادارات و دستگاه‌های اجرایی، بانک‌ها به‌جز شعب کشیک و شرکت‌های بیمه در شهرستان‌های مهران و دهلران روز دوشنبه ۲۶ مردادماه تعطیل اعلام شد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/farsna/456471" target="_blank">📅 00:24 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456470">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7ab76ea7e7.mp4?token=uP1uPmJkMnpwg5HYDF_HJBqC39rJxBDUKLaHfI0QKTwy-2-7C3vNqZgga7IGMKw4QZXCs5rGW9xb3tPOxqyDkBlAhFOebSZrxzO_4zrBtOyRam51eVvPNz74MO-xDCexyt8gN1FT8pt1neRMGq4w-3sWbKvU3WlHXcPXZeI64_2cgdemaln2ox_kKVJYE1DCZy-OcGGejd9yQF5dRK2wwWJAYO2yqd_LgfAmSoWuWzihrvvtSwtsiiJDHGrAaewERdHKjjWitedfGoqI_HpZyPDhgIXCCqs76u7hMbIhRRoadd9jrToEFBSCStl7Vy2uwD95hSLvOyXEP96rkqH-mZXUcaTyKBbv4CKkDjFwKT4LlIxq8FSA7aH_uF_Nv4OR0AyiSCie4X_3G09x3MyWdQchOkDDgvS9lunwzNZFkMd2jQHZN_8NrdMsm7yzskIhKDWLzXpV-8uRx5dTsL4E4BgW1j1NFG4nyFxGiGWyKrxhT_H7XohLuWKPTYlRFm23eSjdKCBFRukyq8r_kqVBibQt1zQDnMG_I4nbaejTgVh89mHRBue_ueD6CiEaRZmKmLQo5w-3DUv-BrHVu0t-IbDwzeP1h616WX00Wa4zzJsdUzhvgjRD29vLPN0f2x0IJlsUahOinucUzZxnnFmzBYGR8CipTKh1HcOEFt0kqwk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7ab76ea7e7.mp4?token=uP1uPmJkMnpwg5HYDF_HJBqC39rJxBDUKLaHfI0QKTwy-2-7C3vNqZgga7IGMKw4QZXCs5rGW9xb3tPOxqyDkBlAhFOebSZrxzO_4zrBtOyRam51eVvPNz74MO-xDCexyt8gN1FT8pt1neRMGq4w-3sWbKvU3WlHXcPXZeI64_2cgdemaln2ox_kKVJYE1DCZy-OcGGejd9yQF5dRK2wwWJAYO2yqd_LgfAmSoWuWzihrvvtSwtsiiJDHGrAaewERdHKjjWitedfGoqI_HpZyPDhgIXCCqs76u7hMbIhRRoadd9jrToEFBSCStl7Vy2uwD95hSLvOyXEP96rkqH-mZXUcaTyKBbv4CKkDjFwKT4LlIxq8FSA7aH_uF_Nv4OR0AyiSCie4X_3G09x3MyWdQchOkDDgvS9lunwzNZFkMd2jQHZN_8NrdMsm7yzskIhKDWLzXpV-8uRx5dTsL4E4BgW1j1NFG4nyFxGiGWyKrxhT_H7XohLuWKPTYlRFm23eSjdKCBFRukyq8r_kqVBibQt1zQDnMG_I4nbaejTgVh89mHRBue_ueD6CiEaRZmKmLQo5w-3DUv-BrHVu0t-IbDwzeP1h616WX00Wa4zzJsdUzhvgjRD29vLPN0f2x0IJlsUahOinucUzZxnnFmzBYGR8CipTKh1HcOEFt0kqwk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
چراغی که پس از ۱۶۹ شب، در کاشمر همچنان روشن است
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/farsna/456470" target="_blank">📅 23:57 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456469">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3020d64c47.mp4?token=Br_6T9o8rGo_9ylFLbvFGUSmHFqL_-Sg3Ip5PnYSQ6JSgz_SpbhgUsOv70SlS4-Ns6c36rRV0evDs8GBULTGNwMIRpz2TVL9DNzt1w-tjbM1DHMDC-zBtcU0SvJQSu6nz7MxQWFhGHz5OvDuCK1q1GPs8P-o0jjwXt4lXxG93cBX87v1iviUOT6os8EOQ3eRpuYCkUN3vr6mfJrI-U4jzdVT9xwjIaNkESis7Vdtw92ActLA3RCHvg61tD_dlbjC_8IARt6CEV3_UPuZlvqQl0s0PT-k0D3MhuIr4KeoIVbJ3A8o6dGmX3C8U5qLPgfYMqF9-heQk0TyEd1LaJTkTwZ0JBzM7VE_NRVgZuYt4zU_cDYDCSi_92FhPU8C6CKQqoQfXb2Gk1RnCz6SmElJNJk-BlyQrYhpDdvYZHuZeXDQAg9WEPoYsI4GaagmeP3SenuZlN3W2IhIRwfCrvH9i6T4_L878cBsRJUsMFBStuAZz8VuJJkUrOlgK4HAOSUwgKg6gjXkowdqZTHKcvzNHj01ptl7umqM1fvm_qNQeGHwK_ygaz3M5MZHbaVjamXYJOB8pB20GATC9s-lZHc-cniiBa30WsfCQVgAvSfNVi-qtLvTak7ydU48n7K7uynYdyqW45h2ObI1SlYrBYnChceWtBF_9yPjUV325zH3CUg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3020d64c47.mp4?token=Br_6T9o8rGo_9ylFLbvFGUSmHFqL_-Sg3Ip5PnYSQ6JSgz_SpbhgUsOv70SlS4-Ns6c36rRV0evDs8GBULTGNwMIRpz2TVL9DNzt1w-tjbM1DHMDC-zBtcU0SvJQSu6nz7MxQWFhGHz5OvDuCK1q1GPs8P-o0jjwXt4lXxG93cBX87v1iviUOT6os8EOQ3eRpuYCkUN3vr6mfJrI-U4jzdVT9xwjIaNkESis7Vdtw92ActLA3RCHvg61tD_dlbjC_8IARt6CEV3_UPuZlvqQl0s0PT-k0D3MhuIr4KeoIVbJ3A8o6dGmX3C8U5qLPgfYMqF9-heQk0TyEd1LaJTkTwZ0JBzM7VE_NRVgZuYt4zU_cDYDCSi_92FhPU8C6CKQqoQfXb2Gk1RnCz6SmElJNJk-BlyQrYhpDdvYZHuZeXDQAg9WEPoYsI4GaagmeP3SenuZlN3W2IhIRwfCrvH9i6T4_L878cBsRJUsMFBStuAZz8VuJJkUrOlgK4HAOSUwgKg6gjXkowdqZTHKcvzNHj01ptl7umqM1fvm_qNQeGHwK_ygaz3M5MZHbaVjamXYJOB8pB20GATC9s-lZHc-cniiBa30WsfCQVgAvSfNVi-qtLvTak7ydU48n7K7uynYdyqW45h2ObI1SlYrBYnChceWtBF_9yPjUV325zH3CUg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
اجتماع حماسی بروجردی‌ها در ایستگاه ۱۶۹
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/farsna/456469" target="_blank">📅 23:54 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456468">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/96aeabd46f.mp4?token=kdXDBVZfjsiiSrTD9D9FFxh46AyMH160pfj7JCV8X-l2sKszHQegnwdCVumYvzVKkSzlV429Mn5QcJBSxmeJahwTb3GlEJFSyHZ3jaOHrwG_w1aXdj30lynbwDuHfaPcVhFqcCh9OASGFB3hntnzKcQbhdLPeIKNda5gjDjwUlTAVS5pKDtNPZ0qKHo8MICGCFfwUiRF1nW25uCcvIJlreZV9VjCXKj_Ry_NgyOKwPzhx15PBbDAXYkjM2hipxFO3mwwXP7xOaDsKUneE4pBRZJF4aheeDHqZKyvTeT_WuUM96jxSfhYAsjK_XhGmmy5HV4_QcVrCXzj16E-1kN5pA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/96aeabd46f.mp4?token=kdXDBVZfjsiiSrTD9D9FFxh46AyMH160pfj7JCV8X-l2sKszHQegnwdCVumYvzVKkSzlV429Mn5QcJBSxmeJahwTb3GlEJFSyHZ3jaOHrwG_w1aXdj30lynbwDuHfaPcVhFqcCh9OASGFB3hntnzKcQbhdLPeIKNda5gjDjwUlTAVS5pKDtNPZ0qKHo8MICGCFfwUiRF1nW25uCcvIJlreZV9VjCXKj_Ry_NgyOKwPzhx15PBbDAXYkjM2hipxFO3mwwXP7xOaDsKUneE4pBRZJF4aheeDHqZKyvTeT_WuUM96jxSfhYAsjK_XhGmmy5HV4_QcVrCXzj16E-1kN5pA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
این‌جا پرچم ایران نسل‌به‌نسل می‌چرخد
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/farsna/456468" target="_blank">📅 23:48 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456467">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FgRXnRXDzBHOkJJrIMBgWwsNM5jiM8Buugsi06UR0jmIVufAJdSf4BfafmdQOFHOzryEVwaGTzgAxT-jXxC0FaQH5WYRuONZg0yVHX6WpsA0JRdXp6YNZeic1x1NqJq6p1EZl3exCYnXpW5UXdeclHC0zuMi1y-EsrLXoOHuKNCp_TeW7Sx1V0PDj_CLFijXP-kbUS2UFIUqyn0Q3BAxHCBo3ilpMfKs0ECEF6S0oBo9GeOy1fOUn3ONOx2MkqfY8knwTzw9vikcY9yACvEUFy6EDOQ1hEPDVS_6_JqrQka13JAXlzAR8qHQmIQ-ZH87Y96YMQoASostxDk8T2Ar2w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تصمیم تازهٔ جهاد کشاورزی؛ شالی‌کوب‌ها برنده، کشاورزان بازنده
🔹
حسین جعفری، رئیس اصناف کشاورزی گیلان، با انتقاد از اعلام نرخ جدید خدمات شالی‌کوبی گفت: نرخ تبدیل شلتوک به برنج ۲.۵ برابر شده، در حالی که این نرخ بدون برگزاری جلسه با نمایندگان کشاورزان و برخلاف روال سال‌های گذشته اعلام شده است. به گفته وی، افزایش هزینه‌های تولید از جمله رشد ۶۰۰ درصدی قیمت برخی کودهای فسفاته و پتاسه، فشار مضاعفی بر کشاورزان وارد کرده است.
🔹
جعفری همچنین نسبت به لغو ممنوعیت واردات برنج در فصل برداشت هشدار داد و گفت این تصمیم می‌تواند بازار محصول داخلی را با مشکل مواجه کند. رئیس اصناف کشاورزی گیلان خواستار بازنگری کارشناسی در نرخ شالی‌کوبی و مشارکت واقعی تشکل‌های کشاورزی در تصمیم‌گیری‌ها شد و تأکید کرد: حمایت از تولید و امنیت غذایی بدون شنیدن صدای کشاورزان امکان‌پذیر نیست.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/farsna/456467" target="_blank">📅 23:43 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456466">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7495006eb5.mp4?token=hp0-1otbkvo345t0Z3z_aCwQh6_vATvxKg7H11MNsPdttr-jc-0UWN5xTrXQsmgMxonvwHQ5dkXt6vH___9iaK187qi01h8ksS0zNsAyUzaSbhJwrJB0yMq6Jk7sL4j73LZvcmANUXN6lM3MDjMjVriOMxrpDn9KUWSCk9WPGyTxyh6Lxdn0BcyvA7AKFsP_VitNfG-mFfd2cZx7CjqTNXSfEgL8t4DSqdtVY-V5jXAXRN165oUqOqEWAD11l63e7BazWqy1_atwgXyFrwnuaWwFHFDye3tXo5xZFWmpPq3E0ge7zf6grh6Q3mDsh8XWsecg8lkK4JGE2MRrczD73395PVbS7WaqHl1W5mEBAM74nYXFXxXHfFBVXWkrtMgGoPCyIrW4ejytuj39Cdc9mCUCAfU2r8lBUhIA16EhRlc8rVAn9HtxlK38kH-cB4MDr_zdftvkVxfIDRvrbH8PLTBCoO7kfMytGLxaeyKHWd_nx4ZRM-Iw_zhqDuN91tHhshicJb4A1kMl7_GSKZUIudcUM1AQSkop12Smv9ETugS7ZYiz8cEIOxcwVKiy3mdguTkZVkG07Lr6y8NsXx6uwEVmcJrdfM-Za1T11XKf1tT3N0r-OjMKbPhdYc6QGVqVQMg5doccRWGRkVuPa_WjvhlT3ymoFi8-SRNEFbX1YR4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7495006eb5.mp4?token=hp0-1otbkvo345t0Z3z_aCwQh6_vATvxKg7H11MNsPdttr-jc-0UWN5xTrXQsmgMxonvwHQ5dkXt6vH___9iaK187qi01h8ksS0zNsAyUzaSbhJwrJB0yMq6Jk7sL4j73LZvcmANUXN6lM3MDjMjVriOMxrpDn9KUWSCk9WPGyTxyh6Lxdn0BcyvA7AKFsP_VitNfG-mFfd2cZx7CjqTNXSfEgL8t4DSqdtVY-V5jXAXRN165oUqOqEWAD11l63e7BazWqy1_atwgXyFrwnuaWwFHFDye3tXo5xZFWmpPq3E0ge7zf6grh6Q3mDsh8XWsecg8lkK4JGE2MRrczD73395PVbS7WaqHl1W5mEBAM74nYXFXxXHfFBVXWkrtMgGoPCyIrW4ejytuj39Cdc9mCUCAfU2r8lBUhIA16EhRlc8rVAn9HtxlK38kH-cB4MDr_zdftvkVxfIDRvrbH8PLTBCoO7kfMytGLxaeyKHWd_nx4ZRM-Iw_zhqDuN91tHhshicJb4A1kMl7_GSKZUIudcUM1AQSkop12Smv9ETugS7ZYiz8cEIOxcwVKiy3mdguTkZVkG07Lr6y8NsXx6uwEVmcJrdfM-Za1T11XKf1tT3N0r-OjMKbPhdYc6QGVqVQMg5doccRWGRkVuPa_WjvhlT3ymoFi8-SRNEFbX1YR4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
این خروش مردم شهرکرد در شب ۱۶۹ از تجمعات مردمی است
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/farsna/456466" target="_blank">📅 23:19 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456465">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c983a49c01.mp4?token=NLrQOpvqeJI_AIlXpLykg02TJZ8PwK2KfkV8qOGy9wmXAanvRHXJgob_9JNIWvwE8NK5kkEtafqFzGiSkA8kKfoob5EOgxE6ClTluzvNogOSBrMBy2kJVERsjrfS6JFPfM07TRKkMWwAabuRmur-5sQDI4_3uFPDnTsrKVNLLjIINdFAMwHLm5kTbH8SEhxyrkBlZLk8iev0b3aeV-ZFkEVvPZxU-wLFzyy9suay9N3Mhnsb8AQK8vKR7QtEWmItlI-5WEPT7Pe5Gyp1Hn240EgFRfDyPa72cDrrhBqH_wb8xFvgGmOQs7niMhMcne03P9reBVQLygNnOV4dBmFm2g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c983a49c01.mp4?token=NLrQOpvqeJI_AIlXpLykg02TJZ8PwK2KfkV8qOGy9wmXAanvRHXJgob_9JNIWvwE8NK5kkEtafqFzGiSkA8kKfoob5EOgxE6ClTluzvNogOSBrMBy2kJVERsjrfS6JFPfM07TRKkMWwAabuRmur-5sQDI4_3uFPDnTsrKVNLLjIINdFAMwHLm5kTbH8SEhxyrkBlZLk8iev0b3aeV-ZFkEVvPZxU-wLFzyy9suay9N3Mhnsb8AQK8vKR7QtEWmItlI-5WEPT7Pe5Gyp1Hn240EgFRfDyPa72cDrrhBqH_wb8xFvgGmOQs7niMhMcne03P9reBVQLygNnOV4dBmFm2g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
معاون سیاسی سپاه: اقدامات ما تاکنون تدافعی بوده؛ ممکن است تهاجمی هم بشود
🔹
سردار جوانی: نیروهای مسلح براساس احکام صادرشده، رویکردهای تحولی خواهند داشت و هر اقدامی برای دفاع از کشور، تأمین امنیت و خنثی‌سازی تهدیدات دشمن در زمان لازم انجام خواهد شد.
🔹
آغازگر…</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/farsna/456465" target="_blank">📅 23:15 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456464">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ce4d930c6e.mp4?token=aDCKh5NhKwtwMUz1fZAorRBF636v_hYPreTbv_qRU5FgfKtHzycH_1-QmeWPj2YhFUcix2X_Ae3uv0HBIE1xayFpMFq_S5Dwv85eqgqp0AESVLllMn3Q3vpCcruf5xJ1xWMISmAnPWUT0MkqUVti2EyeYJKZcb4zXxpbiFjqjnbelrPVrvS_AAk5ySlnsY5GZnMe0oFELpo5Xlz2XFkZpaQd7DKn_5kJqg4sTk3wETafYMdgVaaUWHLsw-IvjCu17FLn_F-pc4Pfw7-P26NIxMN0ahnxYwBFpPz3NIdEVNi6GvVMYEjSV9BO0rXgY6dv_2FHc_bIuHVmTjcrET2ERw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ce4d930c6e.mp4?token=aDCKh5NhKwtwMUz1fZAorRBF636v_hYPreTbv_qRU5FgfKtHzycH_1-QmeWPj2YhFUcix2X_Ae3uv0HBIE1xayFpMFq_S5Dwv85eqgqp0AESVLllMn3Q3vpCcruf5xJ1xWMISmAnPWUT0MkqUVti2EyeYJKZcb4zXxpbiFjqjnbelrPVrvS_AAk5ySlnsY5GZnMe0oFELpo5Xlz2XFkZpaQd7DKn_5kJqg4sTk3wETafYMdgVaaUWHLsw-IvjCu17FLn_F-pc4Pfw7-P26NIxMN0ahnxYwBFpPz3NIdEVNi6GvVMYEjSV9BO0rXgY6dv_2FHc_bIuHVmTjcrET2ERw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">قالیباف: ما در بُعد نظامی و سیاسی جنگ پیروز شدیم
🔹
آمریکا و اسرائیل با ۹ هدف مشخص به ما حمله کردند اما به هیچ‌کدام از اهداف خود در هیچ سطحی دسترسی پیدا نکردند، این بزرگ‌ترین پیروزی بزرگی برای ما بود.
🔹
امروز ما در یک جنگ ناجوانمردانه‌ هستیم که در رأس آن آمریکا…</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/farsna/456464" target="_blank">📅 23:06 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456463">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/38f51655b2.mp4?token=ZMqReO3FMNxM-qeC0eD0O0QELjncPgSSkGwVcQ6yg5sIEJConSCHpohaLa5gncbs6X6D9NcODl2xjdhraIa2LoaPrCREcE6Xt7QhC5qFxDCh6Nf59zgmvM_zISxbWawjkSqVWfABnc2zx1BO7nNlODbWM7lJCAicADokgUSW-D4oQmgU2v2xgvsFIHO0dIRLLhuYAptbDhicSYhPb1NgIIzTHLzDm-2jKcbYvmMlDOyi6vntGUz41Kf3v78__5QM8I9CYAvokjtKeHay2Ce0sn_UQpd1AaZcyaWgBoXUy5-CIvgf6YmyWOiTN4xYyJ8w8-sxxWJwxu9ws8edgl7iEA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/38f51655b2.mp4?token=ZMqReO3FMNxM-qeC0eD0O0QELjncPgSSkGwVcQ6yg5sIEJConSCHpohaLa5gncbs6X6D9NcODl2xjdhraIa2LoaPrCREcE6Xt7QhC5qFxDCh6Nf59zgmvM_zISxbWawjkSqVWfABnc2zx1BO7nNlODbWM7lJCAicADokgUSW-D4oQmgU2v2xgvsFIHO0dIRLLhuYAptbDhicSYhPb1NgIIzTHLzDm-2jKcbYvmMlDOyi6vntGUz41Kf3v78__5QM8I9CYAvokjtKeHay2Ce0sn_UQpd1AaZcyaWgBoXUy5-CIvgf6YmyWOiTN4xYyJ8w8-sxxWJwxu9ws8edgl7iEA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
معاون سیاسی سپاه: اقدامات ما تاکنون تدافعی بوده؛ ممکن است تهاجمی هم بشود
🔹
سردار جوانی: نیروهای مسلح براساس احکام صادرشده، رویکردهای تحولی خواهند داشت و هر اقدامی برای دفاع از کشور، تأمین امنیت و خنثی‌سازی تهدیدات دشمن در زمان لازم انجام خواهد شد.
🔹
آغازگر جنگ دشمن بوده و اقدامات ایران جنبه تدافعی دارد، هرچند ممکن است در آینده جنبهٔ تهاجمی نیز پیدا کند.
@Farsna</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/farsna/456463" target="_blank">📅 22:52 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456462">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b1b5f96c1a.mp4?token=fdVSFwQsEzTmXHBqk7lSLPwNAP8GzY0KDYOXLqmZoODDESUErJ0toswgWAfvWlh_Rw3UIkoD1-fm-GZ3cw_RLIHOYy_gJgXwTTCu9TpzFwcMrnJttV-sEdcqTGlw9Ay2XqwUpA43azdDZAxoKcckREwZ1M4Mk5y3JRk_bm-2qEkvyNUAvexGfrxBoDpq1albsYaqj1uoEUYdA8fVCmtEy5yHe5rMfSZm9n1CHMd2Bggz2hgHMc3VAqDRd7WiAkuceUg4n_pRgJV6Y7-pEaD2Mi3r_bsHOseFC2VYdEa7ioCuRG3rknvQmHAue3BF77vHC3EIaik28fhRV_l87Y5S5A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b1b5f96c1a.mp4?token=fdVSFwQsEzTmXHBqk7lSLPwNAP8GzY0KDYOXLqmZoODDESUErJ0toswgWAfvWlh_Rw3UIkoD1-fm-GZ3cw_RLIHOYy_gJgXwTTCu9TpzFwcMrnJttV-sEdcqTGlw9Ay2XqwUpA43azdDZAxoKcckREwZ1M4Mk5y3JRk_bm-2qEkvyNUAvexGfrxBoDpq1albsYaqj1uoEUYdA8fVCmtEy5yHe5rMfSZm9n1CHMd2Bggz2hgHMc3VAqDRd7WiAkuceUg4n_pRgJV6Y7-pEaD2Mi3r_bsHOseFC2VYdEa7ioCuRG3rknvQmHAue3BF77vHC3EIaik28fhRV_l87Y5S5A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
پزشکیان: در نهاد ریاست‌جمهوری ۸۰ درصد در مصرف آب، برق و گاز صرفه‌جویی کردیم  @Farsna</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/farsna/456462" target="_blank">📅 22:46 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456461">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/332f90307c.mp4?token=i_ttDSlpNeNLU6gxm8ElqcETItHj5c8SuU3okRDeDjQbvjOLcN137lyUpXAv2IYIo6dvGp_EOVAuAoJjPiH_mpgAMYKijO_MBxqNPAf_cafYtIGO6Zf7o7PXAQbisWMq0dwhQmutgF67gtKoqQq2OLnxPSG_NtTtQjtW4_hxkLma5k9VHFCRqVdPxBn5u4_C8sjjI5sTZJIvO3_JZioqDGuZgcLoEnVzzv9Vuf1R2bXAoFWaw7WkZLJVOtR7-IVvJqPq0GCkLYAq-dHRTDFUNC7na8yZsZpPjTRLupMkxtxatMkEBsWVlis8dNfN5M2WYzOk_tnJ8ZJTMhpHorsPpA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/332f90307c.mp4?token=i_ttDSlpNeNLU6gxm8ElqcETItHj5c8SuU3okRDeDjQbvjOLcN137lyUpXAv2IYIo6dvGp_EOVAuAoJjPiH_mpgAMYKijO_MBxqNPAf_cafYtIGO6Zf7o7PXAQbisWMq0dwhQmutgF67gtKoqQq2OLnxPSG_NtTtQjtW4_hxkLma5k9VHFCRqVdPxBn5u4_C8sjjI5sTZJIvO3_JZioqDGuZgcLoEnVzzv9Vuf1R2bXAoFWaw7WkZLJVOtR7-IVvJqPq0GCkLYAq-dHRTDFUNC7na8yZsZpPjTRLupMkxtxatMkEBsWVlis8dNfN5M2WYzOk_tnJ8ZJTMhpHorsPpA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
پزشکیان: باید با سرمایه‌گذاری روی فرزندان خود به توانمندی‌هایی برسیم که کسی جرئت نکند به خاک ما حمله کند  @Farsna</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/farsna/456461" target="_blank">📅 22:41 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456460">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3cd296c47d.mp4?token=o83ZFXGdna5qtu-9P5PdsZ3EB2t0eJocyMQo_KvFXC-Q92zW-F4yGn_aCY4PLeMidbn-UOoUrznZ58rXfqI1ocWHk83Uicyv3SNFlMLpaeA5xIK76VKfUnajKJcW6qNQMUWiCiaCmZQWpL_mncLbi5npR8L5RfUVyTwccbYAp1P9I93hiyJdcJRjWR0tyI98KWo6OjWTYEBUH88IXx-gBN85X4mPDDaH-8UckbqYIAdhgYbaV3loySh9J2WTuGFiCqx0Gq-vIkymFJqk4kN1pROiF7jBhpam3jMwrkoSIGiLfR9LJaEcrvnKb7KW5vZtj7IEl28DyEczHARlY2rvnw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3cd296c47d.mp4?token=o83ZFXGdna5qtu-9P5PdsZ3EB2t0eJocyMQo_KvFXC-Q92zW-F4yGn_aCY4PLeMidbn-UOoUrznZ58rXfqI1ocWHk83Uicyv3SNFlMLpaeA5xIK76VKfUnajKJcW6qNQMUWiCiaCmZQWpL_mncLbi5npR8L5RfUVyTwccbYAp1P9I93hiyJdcJRjWR0tyI98KWo6OjWTYEBUH88IXx-gBN85X4mPDDaH-8UckbqYIAdhgYbaV3loySh9J2WTuGFiCqx0Gq-vIkymFJqk4kN1pROiF7jBhpam3jMwrkoSIGiLfR9LJaEcrvnKb7KW5vZtj7IEl28DyEczHARlY2rvnw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
پزشکیان: باید با سرمایه‌گذاری روی فرزندان خود به توانمندی‌هایی برسیم که کسی جرئت نکند به خاک ما حمله کند
@Farsna</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/farsna/456460" target="_blank">📅 22:36 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456459">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4834b23901.mp4?token=e86EQ1bKvuKwHaCzSaDl2Tky3Y5orWSOALqfsO8LnaIgzzOSRkykyiv_pCFy0cF0olcSrlPcS5CXtUUAaEQrvbdPHV6tc8M1m7OQmFOwfPFYNarHm469ELjHSCA8V1EgsD-fyvRTQaDWHmkYcIyFG-D9_eN8NC-hcCqUpuBV6DBIao2FH8wtYxAqKc9fJzEzS1SeDZk-47Fh4L3P_I0YYD4VA3_pftYaTt3AMxSuQaDRfcyhUnssT9Rl47iyeQnq7xnuGxnhMZ0S940l2h_aAjfEY5UVoxXk5JgRczqmYBxuCpvAjBQNJ8OsBT9sxpQDuf-G8myaCaGPvvXL9-v0tg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4834b23901.mp4?token=e86EQ1bKvuKwHaCzSaDl2Tky3Y5orWSOALqfsO8LnaIgzzOSRkykyiv_pCFy0cF0olcSrlPcS5CXtUUAaEQrvbdPHV6tc8M1m7OQmFOwfPFYNarHm469ELjHSCA8V1EgsD-fyvRTQaDWHmkYcIyFG-D9_eN8NC-hcCqUpuBV6DBIao2FH8wtYxAqKc9fJzEzS1SeDZk-47Fh4L3P_I0YYD4VA3_pftYaTt3AMxSuQaDRfcyhUnssT9Rl47iyeQnq7xnuGxnhMZ0S940l2h_aAjfEY5UVoxXk5JgRczqmYBxuCpvAjBQNJ8OsBT9sxpQDuf-G8myaCaGPvvXL9-v0tg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
مردم بروجن از زمان‌ قطعی برق گلایه دارند؛ برق این شهر شب‌ها قطع می‌شود
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/farsna/456459" target="_blank">📅 22:36 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456458">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9413808a20.mp4?token=pCZPKzr2TQHn5e1KVq_AHx--F59HZIyjdMH004XznHCgM_SdTLIh1ux6Jy2ztiPGI7xkl9jSohMIo190bpcwuA2rnI8JEPOHnNGMWLYsNy2MI0P_XsYP4ycrwF_IOODewm2XdLQ2zFYXPdblqx0BDWolviBY9zO8kIdxQarLTRhUne159XrzcgVuVOFHGXkpNSzRoTR2NxCa_IkJtH6a0fTHFqA3PySwTIQ7ZKCiGuoAPyKaSi-Z7Qmao1yHwDTs12d5FzdJ4c21mO_cj59-DQ60vEidly6AvWLs0m56RvlPjqU5tUzLO5acrAnW1P9VCtxlkD2_Wq3-4ssjxH4p9A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9413808a20.mp4?token=pCZPKzr2TQHn5e1KVq_AHx--F59HZIyjdMH004XznHCgM_SdTLIh1ux6Jy2ztiPGI7xkl9jSohMIo190bpcwuA2rnI8JEPOHnNGMWLYsNy2MI0P_XsYP4ycrwF_IOODewm2XdLQ2zFYXPdblqx0BDWolviBY9zO8kIdxQarLTRhUne159XrzcgVuVOFHGXkpNSzRoTR2NxCa_IkJtH6a0fTHFqA3PySwTIQ7ZKCiGuoAPyKaSi-Z7Qmao1yHwDTs12d5FzdJ4c21mO_cj59-DQ60vEidly6AvWLs0m56RvlPjqU5tUzLO5acrAnW1P9VCtxlkD2_Wq3-4ssjxH4p9A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
اجتماع مردم مراغه در ۱۶۹ شب ایستادگی
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/farsna/456458" target="_blank">📅 22:16 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456457">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/737a9ae067.mp4?token=v_LW1ERlk9KjgqqwBu5Y2HvcLegukS49w-d2lsshW8ax1ved6bGzLi6vd6rop9664ORCZjQEk1aQ0Iy8g4mIov88bVIZsSZPnS_aDhOCueV4tNfE6s87DKS8fNUst6LFGWBF6dL8a4wO9ImCigQ94LzcdvlGf781vVR_nscOLMa-vrfBpldao0uR8oPC9C6rj9jk-HHBPtf2lIeeUBSB9lsuL5TAb2FuWqPZoVwiI2ILIGliDbjbbTtJse6risnLjq2-YMNg3pTyz0on-EFiMGmxUrF5OuZ5nepxou9BSSiy-sv2L_a_ONrLr3gi-4O7wtVEQlgeUDMD6a1Ew_RvFg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/737a9ae067.mp4?token=v_LW1ERlk9KjgqqwBu5Y2HvcLegukS49w-d2lsshW8ax1ved6bGzLi6vd6rop9664ORCZjQEk1aQ0Iy8g4mIov88bVIZsSZPnS_aDhOCueV4tNfE6s87DKS8fNUst6LFGWBF6dL8a4wO9ImCigQ94LzcdvlGf781vVR_nscOLMa-vrfBpldao0uR8oPC9C6rj9jk-HHBPtf2lIeeUBSB9lsuL5TAb2FuWqPZoVwiI2ILIGliDbjbbTtJse6risnLjq2-YMNg3pTyz0on-EFiMGmxUrF5OuZ5nepxou9BSSiy-sv2L_a_ONrLr3gi-4O7wtVEQlgeUDMD6a1Ew_RvFg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
روایت امدادگر هلال احمر از آخرین لحظات یک شهید
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/farsna/456457" target="_blank">📅 22:11 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456456">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/74fc7d771a.mp4?token=rsFY7qz_7CF94ztb-qWyr93se0riV6-ywDJzRZS7N1FpsUfJ1wCP_TgFor7jiVUeTmvaoKHxYeNKdFKxdowhKrl0CCVgDEhWjiA7UVV8EZ0Ib9JTDmjYQNremUCtKLNVhcjxgVH4kGXnhqKWPeD4uYyQH16AQjQhkXmRarg0TPg9KS5LtEbCSyB0lZfHGuaO_FN5UQm48JIyxMpjc42uJZvlhX5ZQi6WiUNnqGe_pJFyYwHRczh_ME3wPrjV4aEqvwDDLFmpSwdIgOATT7hFFZ0TJTvtG8Y2XSSxOky-rMHaXwwhsCdlJf6INw_kBfYndlWeUN9k0OpvNiHU9KZKzA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/74fc7d771a.mp4?token=rsFY7qz_7CF94ztb-qWyr93se0riV6-ywDJzRZS7N1FpsUfJ1wCP_TgFor7jiVUeTmvaoKHxYeNKdFKxdowhKrl0CCVgDEhWjiA7UVV8EZ0Ib9JTDmjYQNremUCtKLNVhcjxgVH4kGXnhqKWPeD4uYyQH16AQjQhkXmRarg0TPg9KS5LtEbCSyB0lZfHGuaO_FN5UQm48JIyxMpjc42uJZvlhX5ZQi6WiUNnqGe_pJFyYwHRczh_ME3wPrjV4aEqvwDDLFmpSwdIgOATT7hFFZ0TJTvtG8Y2XSSxOky-rMHaXwwhsCdlJf6INw_kBfYndlWeUN9k0OpvNiHU9KZKzA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
مردم در شب ۱۶۹ دست از حضور در میدان نکشیدند
@Farsna</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/farsna/456456" target="_blank">📅 22:01 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456455">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d3a28d146a.mp4?token=ZEFt8b41NlFO3SV7_eZwLsFaDmU4P2Kc-UQBC3TH36xBrbU5YEU2B0ptE6Zy0Q664seLL9Givfsx6h5sYKb_4W7SaulBiy-c-jl-4YFiKW15Q3NolOJPfGXtl7lS4gVwx6YTpUX5L_Qn-YFTFzXEK_-5bVBdPSnS8FUV2VdoZ8mcPH7kJyszdyPQJL6Ym0UqF57CWXy-TLC-km0ea9DCjXilSSSNhWBqtPTvSUdaj8j8OscBiO2o6Y788ubI9YYycz-h79xYOQ31LQw15ywgyN9aVuQjLRGIMqs6CHv9m8y21LTLwxqLN4ooKcNJ6L-JUDSWgBCdmK7YY6Fov7lN1A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d3a28d146a.mp4?token=ZEFt8b41NlFO3SV7_eZwLsFaDmU4P2Kc-UQBC3TH36xBrbU5YEU2B0ptE6Zy0Q664seLL9Givfsx6h5sYKb_4W7SaulBiy-c-jl-4YFiKW15Q3NolOJPfGXtl7lS4gVwx6YTpUX5L_Qn-YFTFzXEK_-5bVBdPSnS8FUV2VdoZ8mcPH7kJyszdyPQJL6Ym0UqF57CWXy-TLC-km0ea9DCjXilSSSNhWBqtPTvSUdaj8j8OscBiO2o6Y788ubI9YYycz-h79xYOQ31LQw15ywgyN9aVuQjLRGIMqs6CHv9m8y21LTLwxqLN4ooKcNJ6L-JUDSWgBCdmK7YY6Fov7lN1A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">رئیس‌کل بانک مرکزی برای دیدار با مقامات بانکی و اقتصادی عراق راهی این کشور شد.  عکس: فرج صمدی @Farsna</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/farsna/456455" target="_blank">📅 21:50 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456454">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">بسته خط ۱۲۲.pdf</div>
  <div class="tg-doc-extra">2.7 MB</div>
</div>
<a href="https://t.me/farsna/456454" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">بسته خط ۱۲۱.pdf</div>
<div class="tg-footer">👁️ 9.68K · <a href="https://t.me/farsna/456454" target="_blank">📅 21:46 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456453">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/28bc46a7f5.mp4?token=F2XtIfSdXDt8stswqzTjc3Sy949wZJbUSdS5pDPu9olwvem-EzilLOcJFBs7ZLsUE5g9BEE62f-jtLcLcruZMTbcWwGqmMSLI8Vu6LafgvyFVAWj-lg4Ot7MNFpeOHE_KnDGmtIkUna8_aFOwVoxwsfne5p1_WLf9vVsJFTiMhkJFvIaAPixfsrcUh37SqnhN0jf-CPc3fbcQguiAma3-zkb0rUV501jkjtKswcVc7lsBKxOSx0foQDvEGK7UAx6I0bZmN77TJgaCKegZ1Zu5aKMW26_nq5yLe1Um7Z1TFCCDDKiFLx5rSkH_dFMtTKtBf4PmX5IhDV5i1olHYrleA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/28bc46a7f5.mp4?token=F2XtIfSdXDt8stswqzTjc3Sy949wZJbUSdS5pDPu9olwvem-EzilLOcJFBs7ZLsUE5g9BEE62f-jtLcLcruZMTbcWwGqmMSLI8Vu6LafgvyFVAWj-lg4Ot7MNFpeOHE_KnDGmtIkUna8_aFOwVoxwsfne5p1_WLf9vVsJFTiMhkJFvIaAPixfsrcUh37SqnhN0jf-CPc3fbcQguiAma3-zkb0rUV501jkjtKswcVc7lsBKxOSx0foQDvEGK7UAx6I0bZmN77TJgaCKegZ1Zu5aKMW26_nq5yLe1Um7Z1TFCCDDKiFLx5rSkH_dFMtTKtBf4PmX5IhDV5i1olHYrleA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
چرا به یزد می‌گویند شهر «قنات، قنوت و قناعت»؟
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10K · <a href="https://t.me/farsna/456453" target="_blank">📅 21:40 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456452">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromاخبار چهارمحال و بختیاری</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f4cf671962.mp4?token=l928pUmFTBahpXF8CwT6aDaGCdKmyD3WiE56wmcoDOYcI7lNT84zcy3KsmzriUsGj2j4qS30xA_70l_1UQPnFd86il4ayJjiT-nxpexUyOe31wZcvqhBiKIxtGuaMjLvofYYI31gsDFCxKpCOlQQgmE71jBiw016m7VG6gFkpMCxdVUujQakDacxWj77xSmujMpRXBmIxN_KH9t_TKb6507VeRe-6perQtnxj28o_HgVoO7P9XFbjOFgc82i5JAkgJ1MmsnNeGbs-XmstwACPlWSIZlhUdwoEir8Hd2QjW5iktZJnRUWpcqe-QuuzLBAtjbfMx_eAyflkyg6pvqtZYWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f4cf671962.mp4?token=l928pUmFTBahpXF8CwT6aDaGCdKmyD3WiE56wmcoDOYcI7lNT84zcy3KsmzriUsGj2j4qS30xA_70l_1UQPnFd86il4ayJjiT-nxpexUyOe31wZcvqhBiKIxtGuaMjLvofYYI31gsDFCxKpCOlQQgmE71jBiw016m7VG6gFkpMCxdVUujQakDacxWj77xSmujMpRXBmIxN_KH9t_TKb6507VeRe-6perQtnxj28o_HgVoO7P9XFbjOFgc82i5JAkgJ1MmsnNeGbs-XmstwACPlWSIZlhUdwoEir8Hd2QjW5iktZJnRUWpcqe-QuuzLBAtjbfMx_eAyflkyg6pvqtZYWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
بازدید استاندار چهارمحال‌وبختیاری از دفتر خبرگزاری فارس در شهرکرد
@Fars_Chb
-
Link</div>
<div class="tg-footer">👁️ 9.7K · <a href="https://t.me/farsna/456452" target="_blank">📅 21:35 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456451">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/edeccab51d.mp4?token=YbKm6YROCq1rFP5CstCFbV0cHmAF88FQMT_fHko6ajN7s-zBl7QlcCNHVIvCOqK9vOOGt7XlEard_NriF3av6KZpVQS57uOifzDtZRks_FL0rcuUKYORo-q0AWmJJDJzZRYdUqFi1LYbhrcMUoA-hm-diV6t0PMITsxTv57Q83My5RNtoU6JoXAcEaJRu5GL-OYIawSk36sRIJNGJYbj57hLm_lrPf8ctcax84SrD75BnXN1042HJir-sf9NVQ9eySOjK_dIhssVO4YUWxP4u8pao3qvJi40xPqguXF2XPD5IefTo-jRG6ciUHazVq1GC4RhdW6Sr4dV7EEymlkt0w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/edeccab51d.mp4?token=YbKm6YROCq1rFP5CstCFbV0cHmAF88FQMT_fHko6ajN7s-zBl7QlcCNHVIvCOqK9vOOGt7XlEard_NriF3av6KZpVQS57uOifzDtZRks_FL0rcuUKYORo-q0AWmJJDJzZRYdUqFi1LYbhrcMUoA-hm-diV6t0PMITsxTv57Q83My5RNtoU6JoXAcEaJRu5GL-OYIawSk36sRIJNGJYbj57hLm_lrPf8ctcax84SrD75BnXN1042HJir-sf9NVQ9eySOjK_dIhssVO4YUWxP4u8pao3qvJi40xPqguXF2XPD5IefTo-jRG6ciUHazVq1GC4RhdW6Sr4dV7EEymlkt0w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
جوانی که با دست‌سازه‌هایش یاد شهدای کودک و نوجوان جنگ را زنده نگه‌می‌دارد
@Farsna</div>
<div class="tg-footer">👁️ 9.31K · <a href="https://t.me/farsna/456451" target="_blank">📅 21:35 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456450">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XZy19dcC2BRIn6canE1JOd_Az25hF_98GeO3YQoF6SlzyHmPWoJ2fqijIL7V8q-6Gh4iZiQ1BCFyAL41YgnFGIDckkkuUwJf6h6jXIv0zKqDsPq44Yayg3mo06seeb9QbV-kPOTud2V0sXDVIf6P_93KNdbl64gahhgv1vSFJw9-Elj4AYw1T5E-V9Jl9T5L1R-c7GHeqZ_FK2gwS1oD5Tm5XRE84KndJwR-_Q0BXHeZp_HRzYF-P77m4Qs-Z0CiuK1UjF_POXdzfkYBcGPieIhOQ6cFxWhYJLO1V7mDiDVorDU6WHiflZUiFghRq_wMnXpkBb5QWEaqCW3U7h_Y4g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تثبیت جایگاه کنترلی تاپیکو در پالایشگاه ستاره خلیج‌فارس
✅
درخشش ستاره در کهکشان تاپیکو
🔸
شرکت نفت ستاره خلیج‌فارس به عنوان بزرگترین پالایشگاه میعانات گازی جهان، با تولید روزانه حدود ۴۵ میلیون لیتر بنزین و تأمین بیش از ۲۰ درصد از نیاز سوخت کشور، فراتر از یک مجتمع عظیم صنعتی، شاهرگ حیاتی امنیت انرژی و تاب‌آوری اقتصادی ایران محسوب می‌شود. مجمع عمومی این شرکت برای بررسی عملکرد سال مالی منتهی به ۲۹ اسفند ۱۴۰۴، تنها صحنه ثبت رکوردهای بی‌سابقه مالی نبود، بلکه نقطه عطفی در معماری حاکمیت شرکتی آن به شمار می‌رفت. در این رویداد، هلدینگ تاپیکو با تثبیت جایگاه خود به عنوان سهامدار اصلی و کنترلی، رسماً سکان کنترل این مجموعه راهبردی را در دست گرفت. این تحول مهم ساختاری و جهش اقتصادی را می‌توان در چند  پرده از اقتدار مدیریتی و شفافیت مالی تا ارزش‌آفرینی پایدار مرور کرد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.1K · <a href="https://t.me/farsna/456450" target="_blank">📅 21:33 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456445">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromمس‌ پرس</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LBLkZWX5IWBPJzwLsA4nrZ8zOJOAl-t2TKdu1KACwDO4zns2oR6xNCiurHYvNbRY0861mRuo54fENzlUHEizPxIXgxJ6cshvIfjSBLOTrZU1RvigdcVotQLyVXketSpUD-D_FH062HTgCQw0nWjmcpKpf2JV4eUwhl3NuiEmH2fo1pD52RmlQa1dhZxA6KlokonBbTJUU5Gd7IMrQhVAlnT4Y2z3sGcKCScNDWfgqbdI_VEMyDswIH9Bk2hhrF1E-3uAjRxNWsAa1N-SRa5q9tCxuXzJXO4xiT05qAYc7OsF9vgbwny-jI65SchykmJFwVcpcPN9e8PN6Cy2Eikk0A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/eXtkwb-NYSt6muSPAp1Y46cu_5wR6ZRrabuRqu7FIsmM_t3jMtuA0DHCg075BAJWCntiGqB1fmpB3Dd0QjS9wNvfBAIADkvHvhwEpBKUeC0ucPSnI9_tqOaklHqDnpybroUMTbETcsq7dDHfzooTIgkZFzaopc9AjmSRDQ-4SPx6uMAup6pB6IyWf4tFBtParl4AI1ffD97m5iMwUv0OHHS825pqYRS1hx2SueDsCHZpHFr6mj6_YBzFIPjt6LC-gKJDBBx0yvIhDkpY8wdDV-N1aJ6bB0y6aUgrAnQH7HvsFOmqLdS-V_eVrNHpzTbygIy-Pn0mDj_rVkdLV7KiCA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/OWVLj8FlQJ6qPUnPvSPacJdBljYL7OxHacJewEfi2G2gW1e1ooB1hWRfxQdUoGLoTF2xfzoFtiHZDUkW1rgVa1C66lIUpT60AU6zLOJwSxX-2-coCBMMZwZ4nn037fnfV8633KdkqdI0SCM6o7u4BKFC3wvBMqDGk-HaERyretxprW9kKehQsxO9EHw2cWZ9_qr-0sFPds02NxEWcswjkrA5HYMyJT606ih7rghCNKkaFMEaYKITEZC9SfXcDrxFaQW_uDLB5jPFD3VqRhQuULQHMX3Te5ZdIDH2OCD0PLwCRYQZ3I5xnC-ZtGPCfgb7rr_Cxub05vN3goqkIchm2A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/mlZyxZfi8LhBMop5tIJWrGPjqQMWzk71Vl06kf9jLiu-oSqfVybHisrHFAMpMNkRrU_ej5XNGUYNv9BsE0cCXU2vycM65BX_ydWB664v_KGfVy3GjXsmxCRk0giMDyDi_IVZAcTsrMRiYFHpifSS8P5hMH9grFhZoyGR3BeouQCehDR0J7xvNOyLxjZbPYlbpbPFwj3PMYWyWYJdFRTnJi9I3ZjwEfGcgar4pGEghWvbRIa5wsPg6UCpg1JPr2b-ed-Pj_xxgrO3CoATYoQrDQxgveTRiwEmtfaGHG8bcqcmAJZpSenTWY9NR_y5Jj3cnTZ0gWzejt5O0x00i9GbzA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/bQ3Flb10Tc0T_A_UStxFYvWEfRRBWNmBfxhDa8P3Zji3JB6Hoy34uiQuau62Z3kLAF5o6b4QV156niAYEUGss7l3Wc4prJhS7biVPNdk2FqlKmWsjSTthvD_-oZuUl84wAETi8Ukbyqt0mwARXjmLKqRuM2bkZahhk1wV8j9ieZfHoy4EwbT7GBlv56pfic01gXox6HoHFZ-NLoQHqJ5U_KRQNe-KkseiDbmVDRqIhRKdKDnmJzLug-kbCQCdNqjUzAxby8PuwkG01bEKJ_0MtC-ESqHc_TF6lzdAA2eG4bxnZkyfECkmpCrpI-Bkl1gcGTr3QeSfadBt9BJSpZavA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🔸
در نشست شورای معاونان مطرح شد؛
🔰
بهبود ۱۴درصدی عملکرد ایمنی و کاهش ۵۵درصدی حوادث در شرکت ملی صنایع مس ایران
🔻
گزارش عملکرد امور ایمنی، بهداشت و محیط‌زیست شرکت ملی صنایع مس ایران در سال ۱۴۰۴ از بهبود ۱۴درصدی عملکرد ایمنی، کاهش ۵۵درصدی حوادث منجر به فوت و افزایش ۲۳درصدی نفرساعت بازرسی‌های روتین ایمنی در مجتمع‌های شرکت حکایت دارد. بررسی عملکرد سه‌ماهه نخست ۱۴۰۵ نیز بهبود وضعیت ایمنی را نشان می‌دهد.
🔹
براساس گزارش ارائه‌شده ازسوی واحد HSE در شورای معاونان شرکت ملی صنایع مس ایران، عملکرد ایمنی شرکت در سال ۱۴۰۴ نسبت به سال قبل ۱۰۵ امتیاز، معادل ۱۴درصد، بهبود یافته و در وضعیت بسیارخوب قرار گرفته است.
🔹
فرآیند ارزیابی عملکرد ایمنی مجتمع‌های شرکت به‌صورت ماهانه و بر اساس ۹ شاخص اصلی، ۲۰ زیرشاخص و ۶۷ ریزشاخص انجام می‌شود. در سال ۱۴۰۴ هر ۹ شاخص اصلی به حد پذیرش تعیین‌شده، یعنی حداقل ۷۰درصد، دست یافته‌اند و ۶ شاخص نیز نسبت به سال قبل روند افزایشی داشته‌اند.
◀️
ادامه خبر در مس‌پرس:
https://mespress.ir/x6Sy
@mespress_ir</div>
<div class="tg-footer">👁️ 8.65K · <a href="https://t.me/farsna/456445" target="_blank">📅 21:33 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456444">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-footer">👁️ 7.6K · <a href="https://t.me/farsna/456444" target="_blank">📅 21:33 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456442">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5e56aeee87.mp4?token=PSmlnGbb0zi6Z22ksS3faiMDBlHe5ePC5ZHIjLtKsgcAjSC-ztd4QySukPs4JtMkFURwVOnYkfVxQfu5efdEedsgfzdX0brk5e8hKD_UIB-Vjza8ZBWlVpBoJiXr8ZG9X0tB3mifHt2s2XVh6KyrXYJqWwOuako0nrLvvf_rfcA3i7A1p76Uo6xjdHuWQXi0mW7QsglnqKlpmFsDb4M782P9k3TUyzp6VDOgRMXdYOhwTLXGg-VrspNYsKKrAEpB-L-V9ufFwCzkP6mw-WP6ZOZrXLXK7IB5RyyElTwxvIeRIjQc9udw60qOs-voKhE9qttcxHdyejwfAFY3gIaNcw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5e56aeee87.mp4?token=PSmlnGbb0zi6Z22ksS3faiMDBlHe5ePC5ZHIjLtKsgcAjSC-ztd4QySukPs4JtMkFURwVOnYkfVxQfu5efdEedsgfzdX0brk5e8hKD_UIB-Vjza8ZBWlVpBoJiXr8ZG9X0tB3mifHt2s2XVh6KyrXYJqWwOuako0nrLvvf_rfcA3i7A1p76Uo6xjdHuWQXi0mW7QsglnqKlpmFsDb4M782P9k3TUyzp6VDOgRMXdYOhwTLXGg-VrspNYsKKrAEpB-L-V9ufFwCzkP6mw-WP6ZOZrXLXK7IB5RyyElTwxvIeRIjQc9udw60qOs-voKhE9qttcxHdyejwfAFY3gIaNcw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
نایب‌رئیس مجلس: از دولت درخواست می‌کنیم اصلاح قانون بودجه را در قالب لایحه برای مجلس آماده کند؛ مجلس آماده است بودجه‌ای با محوریت معیشت مردم و برای حل مشکلات آنان تصویب کند.
@Farsna</div>
<div class="tg-footer">👁️ 8.72K · <a href="https://t.me/farsna/456442" target="_blank">📅 21:29 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456441">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/aa938a5a8a.mp4?token=RmbV9mHEReyJt24O51E1ci0fP-ysCn3dwPsXBvbUSZsta2sDPYIcOdZO8NXWl8v3qCk6LI9VTR2a1i19XlAaoEbjj7ZJ6fdcZERibxPzdxDPbbbuzB2RUpMwZWufZfiZtULKGAm1UID6vAq5t4UIC1pel95lgi6ngQV2EwHmqEgmyuLRGroUsVSvmnD6lgq3lviqvdRYn67-9MZFEQBD8EsDcIAebIH0u8cw-NgN-Fh_d9F3bBzBnrsRikjqx_S24Pf-odBWq2wAyRw_w6o6PkCKVlbsXeOKjQkih_1zLpRMzbZP4gJ6QdnmsmYdKmg4V9QkoSSYfn-ruwr2J9Uxmq21hSIh_KNZOjouTPNSw886ZyYFzXQ3CwUHSV0GlG9yWP0NZKJD_SSAF8gr2Gb92oRinSyodebYUxAISvlHEyuVyOveOiJuTwhwjdbS3qNzEDChFVVwQa_XnDAmvqyoclkt1BTankZKdbd3msRtG_qMicFncFxS4-Q0kiIUsFvITca9j-kBjoe6R5dFESjBbjNr6_iqzgRNNewj18YD26k4z0Brt1f8U9bsQxy-gby1UuThbY5OP1UouqoslYH4jsHK9vWSQOVrgXtnpNIrQxZDZ7yDYoxpwuV8DdFn903GI1rvfvSBAJrFi4siUfbsFdkacsrCt4avh_NTWK66HnE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aa938a5a8a.mp4?token=RmbV9mHEReyJt24O51E1ci0fP-ysCn3dwPsXBvbUSZsta2sDPYIcOdZO8NXWl8v3qCk6LI9VTR2a1i19XlAaoEbjj7ZJ6fdcZERibxPzdxDPbbbuzB2RUpMwZWufZfiZtULKGAm1UID6vAq5t4UIC1pel95lgi6ngQV2EwHmqEgmyuLRGroUsVSvmnD6lgq3lviqvdRYn67-9MZFEQBD8EsDcIAebIH0u8cw-NgN-Fh_d9F3bBzBnrsRikjqx_S24Pf-odBWq2wAyRw_w6o6PkCKVlbsXeOKjQkih_1zLpRMzbZP4gJ6QdnmsmYdKmg4V9QkoSSYfn-ruwr2J9Uxmq21hSIh_KNZOjouTPNSw886ZyYFzXQ3CwUHSV0GlG9yWP0NZKJD_SSAF8gr2Gb92oRinSyodebYUxAISvlHEyuVyOveOiJuTwhwjdbS3qNzEDChFVVwQa_XnDAmvqyoclkt1BTankZKdbd3msRtG_qMicFncFxS4-Q0kiIUsFvITca9j-kBjoe6R5dFESjBbjNr6_iqzgRNNewj18YD26k4z0Brt1f8U9bsQxy-gby1UuThbY5OP1UouqoslYH4jsHK9vWSQOVrgXtnpNIrQxZDZ7yDYoxpwuV8DdFn903GI1rvfvSBAJrFi4siUfbsFdkacsrCt4avh_NTWK66HnE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
روایت مردم از اقتدار بچه‌های پدافند هوایی سپاه
@Farsna</div>
<div class="tg-footer">👁️ 9.74K · <a href="https://t.me/farsna/456441" target="_blank">📅 21:26 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456440">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JMLosyqDt4fdiRIpzNNWGjBoMngt41O5I9sefJHovbrKo3UyLq_47pJYZCeYVqp0r_InECQFWoJxTX_ryUeDoLn5TSsjI3eilZ1ogH_jEKKUDVi36pne0XkCGf8AuzsbyhGKa4VjPThZzx6cJFetXGVifgSEl8Xus0eg5JPhakhfWy68SAjskE9CI5_ip_iqcfaziksXTTGqvtSm-8xeI0N4jqIp1PRS1mAZsNeWisOV7A3VMptjlExDE-3len-BtBEVHcDJPHOQ7no127_-Cc_jM0CQIE0zExvB6hmxI12J6olF_aq3toXvaWihUC65jCfYORoq5vPUXZ-GSo5yNw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">لایحه‌ای که قبل از طرح در مجلس زیان‌آفرین شد
🔹
موجی که پس از اعلام دولت برای ارسال کنوانسیون خزر برای تصویب به مجلس در فضای مجازی به راه افتاد، خواهی نخواهی بخشی از توان، انرژی و تمرکز مردم و مسئولان کشورمان را از وقایع جنوب کشور به آب‌های ساحلی دریای خزر سوق داد.
🔹
این کنوانسیون که ۸ سال پیش به امضا رسیده و به جهت ابهام‌هایی که دارد پیشتر از مجلس به دولت برگشت داده شده، پس از چند سال فرو رفتن در محاق، به یکباره از سوی دولت حلول کرده.
🖼
اما چرا این لایحه به تمرکز فکری مردم و مسئولان ضربه می‌زند؟
🔗
دلایل این موضوع را
اینجا
بخوانید
@Farsna</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/farsna/456440" target="_blank">📅 21:20 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456439">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/415146f8fc.mp4?token=pHNegs4HkF8pyZdo-XFAkUuKaIJoZ68IL7TZbo2e55r0X1OoUSfxgT9vQDP1P15S5Qqt4WsTsE9OWxvyHePj5EOBQ9FqYpF8iCCNer-gHJCL6N3sX72mlQHeZP69tvbqpCqRBUjyr1RrzcH-0SPB4c2082A00I6FeeDL4CHMPRt3YhCvbMe-huzXVul5PBzP9wj3Rg_fZHJkz82qrVro_dGRiV-Lf5l01yIrggjXTsPmxycaSOg7aF3NRHuyZIQZ8ATGSG19rw-TWEG4iAiqse033jJuwTfF_YNxMqkz2BCHs8HLJpgIeQMWgH9qZaS6B9gMpUBPL4ULdSA68qypzw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/415146f8fc.mp4?token=pHNegs4HkF8pyZdo-XFAkUuKaIJoZ68IL7TZbo2e55r0X1OoUSfxgT9vQDP1P15S5Qqt4WsTsE9OWxvyHePj5EOBQ9FqYpF8iCCNer-gHJCL6N3sX72mlQHeZP69tvbqpCqRBUjyr1RrzcH-0SPB4c2082A00I6FeeDL4CHMPRt3YhCvbMe-huzXVul5PBzP9wj3Rg_fZHJkz82qrVro_dGRiV-Lf5l01yIrggjXTsPmxycaSOg7aF3NRHuyZIQZ8ATGSG19rw-TWEG4iAiqse033jJuwTfF_YNxMqkz2BCHs8HLJpgIeQMWgH9qZaS6B9gMpUBPL4ULdSA68qypzw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
معاون وزیر نیرو: در تلاشیم دورهٔ زمانی صدور قبض‌های برق را کاهش دهیم
.
@Farsna</div>
<div class="tg-footer">👁️ 8.5K · <a href="https://t.me/farsna/456439" target="_blank">📅 21:15 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456438">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YGCLdANpIFVNDQeXZkN2-GY4PyPBGaBoBM0pYinVrmqyhZtbKVAGqSYMFNNYY_C5rwPxsroUlL5HxwT3DiiMbdZKMzsfl6YOKBuJbydpCXByBUFqyBayoGNOfC8AkQIqJeonRUGoqi6hlsKnzH2c2soHnq2_WryHiT9R2AsmNeXwQfE4bWMHJK0sJzAb3WxBz5CGO1ZUZA72PAf-6JdSZI5jx9aKOXmVcmloRwdAEByS3PnkpTJSu2E6whKqgWC9Q6h3GiXBJLXVbaQUwq2o2rMTUBeAyxLG5ksmeAyh87BeSaU4-gi1VdvJHM1ccU4MtAMOtW6M_McC5yTlckStRw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اذعان فرمانده آمریکایی به غافلگیری از انهدام پایگاه‌ها توسط ایران
🔸
بالاترین مقام نظامی آمریکا در دوره باراک اوباما روز یکشنبه تأکید کرد که آمریکا فکرش را نمی‌کرد که ایران پایگاه‌های منطقه را «نابود کند.»
🔹
رئیس اسبق ستاد مشترک ارتش آمریکا مایک مولن در مصاحبه با ای‌بی‌سی نیوز به بررسی وضعیت نظامیان آمریکایی در غرب آسیا از جمله ملوانان ناو آبراهام و طولانی شدن مأموریت این ناو هواپیمابر گفت:‌ «این موضوع قابل توجه بوده و بسیار دشوار است. این استقرارها بسیار دشوار هستند. از نظر تاریخی، ما معمولاً قادر بوده‌ایم برای استراحت، انجام تعمیرات و سپس بازگشت به عملیات، به یک بندر برویم. حتی در زمان ویتنام، این کار را انجام می‌دادیم.»
🔹
فرمانده اسبق آمریکایی با ابراز نگرانی درباره وضعیت ملوانان در ناو آبراهام لینکلن بیان کرد: «من قطعاً با توجه به آنچه در گزارش‌های خبری دیدم، نگران شرایط کشتی بودم. می‌دانم که فرمانده ناو لینکلن، به سختی روی این مسائل کار می‌کند و همچنین معتقدم که حقیقت احتمالاً جایی در میانه (گزارش‌ها) است.»
@FarsNewsInt
-
Link</div>
<div class="tg-footer">👁️ 9.26K · <a href="https://t.me/farsna/456438" target="_blank">📅 21:12 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456437">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fd38bfd178.mp4?token=ar-T2gdzdRKbzPM8tg6b5PCjr5UmGdWr_8KmJnH1F6Zc8EorLZOgCqFFVa-_9rrV26UM8UsbVKtTYF7UIAH8QFzuj1QVirfNzeFaxWLrn_Lnl0UyE1FyI9KRNZAjd0TcWDxzc7NCrZLKF-0Fb0ZLO38Z9alC2T2kbdV1EQABbX7hdLXElQCUjtN70HvHvzjZg9ZnZnM3924_jSX-ju1eBr8tTLhY0n0fUU6vFzibPQvvtG2OB0SwOdyxoGzu_qf93T3ktJlLGY__d6wf3pZPoK9f5XGpWpJ134Vnwa9blO0eNUWCwwg26eIXLPqEifG6d13erS7lFbkyurie8MX7Aw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fd38bfd178.mp4?token=ar-T2gdzdRKbzPM8tg6b5PCjr5UmGdWr_8KmJnH1F6Zc8EorLZOgCqFFVa-_9rrV26UM8UsbVKtTYF7UIAH8QFzuj1QVirfNzeFaxWLrn_Lnl0UyE1FyI9KRNZAjd0TcWDxzc7NCrZLKF-0Fb0ZLO38Z9alC2T2kbdV1EQABbX7hdLXElQCUjtN70HvHvzjZg9ZnZnM3924_jSX-ju1eBr8tTLhY0n0fUU6vFzibPQvvtG2OB0SwOdyxoGzu_qf93T3ktJlLGY__d6wf3pZPoK9f5XGpWpJ134Vnwa9blO0eNUWCwwg26eIXLPqEifG6d13erS7lFbkyurie8MX7Aw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
وقتی نگهبان بیمارستان ناجی یک نوزاد شد
@Farsna</div>
<div class="tg-footer">👁️ 8.82K · <a href="https://t.me/farsna/456437" target="_blank">📅 21:04 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456436">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8e0585e0cd.mp4?token=WIzYl0sHDSg3BL9f4tJsVGg3GbUvU232JTGrlynve50qSUgDOwgct7sG0Vu__urT55aPk3r2N5BUe-Yde9gQkQK8-iqlDE6QkvyW46dK2KYFdH8Plfru_BBZj2iHR2o38_An6mwtB0ulwnIIixlf0gnt1EbBYFwhFD3UokTelO5cXu0QIBIjgaRdo2Pe4ymzvjM-baaoLP2yS79s7DltvHVjvEUOJRdf2xIMCJu5eMuiBNZaOdBnrqqzc9hI6KnILI1lfxvjUSxZj1Rocg0NmpO75Wsx796dJytaU3HKgckSnBwHOkQY4G3U4vUUkx4jxII5bVxaWYubuCKSlPAV8A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8e0585e0cd.mp4?token=WIzYl0sHDSg3BL9f4tJsVGg3GbUvU232JTGrlynve50qSUgDOwgct7sG0Vu__urT55aPk3r2N5BUe-Yde9gQkQK8-iqlDE6QkvyW46dK2KYFdH8Plfru_BBZj2iHR2o38_An6mwtB0ulwnIIixlf0gnt1EbBYFwhFD3UokTelO5cXu0QIBIjgaRdo2Pe4ymzvjM-baaoLP2yS79s7DltvHVjvEUOJRdf2xIMCJu5eMuiBNZaOdBnrqqzc9hI6KnILI1lfxvjUSxZj1Rocg0NmpO75Wsx796dJytaU3HKgckSnBwHOkQY4G3U4vUUkx4jxII5bVxaWYubuCKSlPAV8A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
مرتضوی، وزیر سابق کار: می‌شود هم جنگید، هم اقتصاد را مدیریت کرد.  @Farsna - Link</div>
<div class="tg-footer">👁️ 9.56K · <a href="https://t.me/farsna/456436" target="_blank">📅 20:55 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456434">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2d085f71d9.mp4?token=vdKZ7OJhuvVrSTSIJloHQhbf0z1knvbm5IRirztb85axfT3R9laeHIJB0bUxaBqgMYdekOJ95Rx6f0gzk_W3wc_u4JITgpzLU5Eht-Zi9U7JkpI69G2CKzzTo90UhKWH0uRen6oP6owOgsXBoO4tSUB-4bUhYmdl1gJNJaRDrouMQz47j--ajB7ZGDV-9khGfSnJyv75Qr2D3_KaBgKLNm44fZxcw6JQhtJ2iPdpjmU2nkHAcIrkpExqPAEaCdU5aKhTkbrv4eBK_R4539A39uQOvKh4WwCv_fW2LdpHn4fb0ckQZHbVKgG6urQ8UM8f7tQEg4p3HYFc8r7i2chCLA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2d085f71d9.mp4?token=vdKZ7OJhuvVrSTSIJloHQhbf0z1knvbm5IRirztb85axfT3R9laeHIJB0bUxaBqgMYdekOJ95Rx6f0gzk_W3wc_u4JITgpzLU5Eht-Zi9U7JkpI69G2CKzzTo90UhKWH0uRen6oP6owOgsXBoO4tSUB-4bUhYmdl1gJNJaRDrouMQz47j--ajB7ZGDV-9khGfSnJyv75Qr2D3_KaBgKLNm44fZxcw6JQhtJ2iPdpjmU2nkHAcIrkpExqPAEaCdU5aKhTkbrv4eBK_R4539A39uQOvKh4WwCv_fW2LdpHn4fb0ckQZHbVKgG6urQ8UM8f7tQEg4p3HYFc8r7i2chCLA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
نظرتان در مورد کالابرگ چیست؟
@Farsna</div>
<div class="tg-footer">👁️ 9.72K · <a href="https://t.me/farsna/456434" target="_blank">📅 20:50 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456433">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d120771984.mp4?token=bXhtikvOnOA6dpPzw4jHF60tKbM4kFgrHAO7RikMZ7TCaGCgKpPA-rRXx9ozyNDJowtu-8K70ZaJMZ0-xd_jecQcS0vaf84OvRIYCKjX5qRhJz8d5QIpN7slaa0P4lGRNRSo2fXYFbFsi2zVlGLFqnIWQ8NPNTdy5boCzPY4oZroVG33-3EA7iYtqZiPI8tX48evjb_fGUqCXeSMnUGNi4iABzWPnpYiMZEx93mxZBh2bXkyKTRY8M9ELag6kyFjEJ5rtDt3kIpZJP9FLn-ZIEsq03YLhhdxDhv8lYmZejNLn__dnc-v5N3MnBibtjonj8_vnfIMbW8jCBRIe3gcqg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d120771984.mp4?token=bXhtikvOnOA6dpPzw4jHF60tKbM4kFgrHAO7RikMZ7TCaGCgKpPA-rRXx9ozyNDJowtu-8K70ZaJMZ0-xd_jecQcS0vaf84OvRIYCKjX5qRhJz8d5QIpN7slaa0P4lGRNRSo2fXYFbFsi2zVlGLFqnIWQ8NPNTdy5boCzPY4oZroVG33-3EA7iYtqZiPI8tX48evjb_fGUqCXeSMnUGNi4iABzWPnpYiMZEx93mxZBh2bXkyKTRY8M9ELag6kyFjEJ5rtDt3kIpZJP9FLn-ZIEsq03YLhhdxDhv8lYmZejNLn__dnc-v5N3MnBibtjonj8_vnfIMbW8jCBRIe3gcqg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حملۀ فسفری اسرائیل به جنوب لبنان
🔹
منابع لبنانی از حملات جنگنده‌های رژیم صهیونیستی به مناطقی در جنوب لبنان از جمله منطقۀ علی‌الطاهر خبر دادند.  @Farsna</div>
<div class="tg-footer">👁️ 9.78K · <a href="https://t.me/farsna/456433" target="_blank">📅 20:47 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456432">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس ورزشی</strong></div>
<div class="tg-text">دربی تهران در انتظار تعیین تکلیف میزبانی
نقش‌جهان قطعی نیست
🔹
طی ساعات گذشته شایعاتی پیرامون باشگاه معرفی قطعی ورزشگاه نقش‌جهان برای میزبانی دربی توسط باشگاه استقلال مطرح شده که پیگیری‌ها نشان می‌دهد صحت ندارد. از طرفی سهراب بختیاری‌زاده در این مورد هنوز نظر نهایی خود را نداده و تصمیم شوراهای تأمین و مسئولان ورزشگاه و استانی نیز تعیین‌کننده است.
🔹
استقلال ورزشگاه نقش‌جهان اصفهان، پارس شیراز و امام خمینی اراک را به‌عنوان سه گزینه میزبانی دربی تهران مدنظر دارد و دراین‌رابطه همچنان مذاکرات خود را در ادامه می‌دهد.
@Sportfars
-
Link</div>
<div class="tg-footer">👁️ 9.18K · <a href="https://t.me/farsna/456432" target="_blank">📅 20:45 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456431">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/12b0e2e6f0.mp4?token=jJtr__nOxGyFSacPZwAYK2_dgL9gOPE_iWyk8-55F_EYOZ8mt-fxeM0Mg_ijFruuGQ8DGus0qzBe8ZhG93mBjjf_il7svAihh1wh6-AvWhpfsZOFKIg1Ork7d5xBpcbKhJjIUNjtZowM1SWVjEV05aM1QfdsUK6vNHeNzlvORt1I0___8XkOJCeL4Uphq-fus_9qJoRlcIU-lpZIrPthEB6LiVdrVpIH0joiW44CDLI60wIGK4d968kx830jTITn9BdPohs_9SRr-MvsTBY2LTP0_AhtiG3bcFLyIMIewHgXno-0vnl00q5viCg0l7VU1jCH91LDcj_V6JgE4WnFIw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/12b0e2e6f0.mp4?token=jJtr__nOxGyFSacPZwAYK2_dgL9gOPE_iWyk8-55F_EYOZ8mt-fxeM0Mg_ijFruuGQ8DGus0qzBe8ZhG93mBjjf_il7svAihh1wh6-AvWhpfsZOFKIg1Ork7d5xBpcbKhJjIUNjtZowM1SWVjEV05aM1QfdsUK6vNHeNzlvORt1I0___8XkOJCeL4Uphq-fus_9qJoRlcIU-lpZIrPthEB6LiVdrVpIH0joiW44CDLI60wIGK4d968kx830jTITn9BdPohs_9SRr-MvsTBY2LTP0_AhtiG3bcFLyIMIewHgXno-0vnl00q5viCg0l7VU1jCH91LDcj_V6JgE4WnFIw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
روایت حضور یک شهروند ناشنوا در تجمعات شبانه
@Farsna</div>
<div class="tg-footer">👁️ 9.38K · <a href="https://t.me/farsna/456431" target="_blank">📅 20:43 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456430">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/61f9ee6e4c.mp4?token=a8oDTKd7Z-SPRbsJEeZ_0yHpX-tvxiDDrlGP5vQTgGpCi3p2eeHnac8G41WX8xk9Tc1vWU81aTlzZQIkJ5B98guZRmwYz-mRwn6F6RsZ8aa2RnK90kSkFV05N4A07VAXVO50azY7QJzSWnWNeFPyvyXjKS8RWjpByfiNhRvz9Ub-6ieE-XIEWUsDp29eDbuL7IrcYs3harCoYARz-xK15pCadq1pH9ct5CyfM_qJLV9xCni6YUYW6P9SMQlnv6tR2Lrtih68qPkqpjBmxdeTAVt6R1qLoFgJVCRChK7pGjrGYUPWfFs5SmJLSeADSeaWvVVsgdRhxZkhOjmripvQ2g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/61f9ee6e4c.mp4?token=a8oDTKd7Z-SPRbsJEeZ_0yHpX-tvxiDDrlGP5vQTgGpCi3p2eeHnac8G41WX8xk9Tc1vWU81aTlzZQIkJ5B98guZRmwYz-mRwn6F6RsZ8aa2RnK90kSkFV05N4A07VAXVO50azY7QJzSWnWNeFPyvyXjKS8RWjpByfiNhRvz9Ub-6ieE-XIEWUsDp29eDbuL7IrcYs3harCoYARz-xK15pCadq1pH9ct5CyfM_qJLV9xCni6YUYW6P9SMQlnv6tR2Lrtih68qPkqpjBmxdeTAVt6R1qLoFgJVCRChK7pGjrGYUPWfFs5SmJLSeADSeaWvVVsgdRhxZkhOjmripvQ2g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
کارشناس پدافند هوایی سپاه: در روزهای اول جنگ ۶ تا ۷ پهپاد هرمس و هرون رژیم صهیونیستی همزمان بر فراز جنوب لبنان گشت‌زنی می‌کردند
🔹
با هدف‌قرارگرفتن این پهپادها در ایران، تعدادشان در جنوب لبنان به یک فروند رسید و حزب‌الله آزادی عمل بیشتری برای عملیات پیدا…</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/farsna/456430" target="_blank">📅 20:30 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456429">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f4eba8a433.mp4?token=mK778hp_V_XCbmBLl1kUhVpFSUf33ugQnj5x2U7SZm71URSsxth4Eq1Q8EvreI_QUqY1jMrZe_UenYfZpEeq44kNbNmSH9rmD4_hYIWphDBETMxkiwEctUE7BFeaIkJwlIQyvc3-W6vPIFcld15nDfuChFk6hyPzFuDldo-bJEhaCFOsIFF8G9ugwbC50NGW3Sg4V-dR25ejgkrOQyUp5Haz7Pi53KpnRMXvs_FP5mJGG8EwTx4A5EVNGD_sfJorr3Q5lBONlJgrgMoUp-2hMpvTRm-YMNFtYDKVncg46tviqeEP_XNL8avmsMV_Pp_LK6R1QjMJPJPktHvXhugD9Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f4eba8a433.mp4?token=mK778hp_V_XCbmBLl1kUhVpFSUf33ugQnj5x2U7SZm71URSsxth4Eq1Q8EvreI_QUqY1jMrZe_UenYfZpEeq44kNbNmSH9rmD4_hYIWphDBETMxkiwEctUE7BFeaIkJwlIQyvc3-W6vPIFcld15nDfuChFk6hyPzFuDldo-bJEhaCFOsIFF8G9ugwbC50NGW3Sg4V-dR25ejgkrOQyUp5Haz7Pi53KpnRMXvs_FP5mJGG8EwTx4A5EVNGD_sfJorr3Q5lBONlJgrgMoUp-2hMpvTRm-YMNFtYDKVncg46tviqeEP_XNL8avmsMV_Pp_LK6R1QjMJPJPktHvXhugD9Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
پرواز دوبارهٔ ۲ عقاب‌ در آسمان دالاهوی کرمانشاه
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/farsna/456429" target="_blank">📅 20:23 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456428">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5744721f52.mp4?token=Ewn5WS17MB7j5kAUJWl0dGfafdGf_sdUz6IsLgJ4pzguSIBndgytlKGLKMVZ3oSx5u4lp405TEBCI6h6fHm4EXxIhbx5NDqkxFM-fx--j-33AA_bg4CsPGzPeBh8EYvpUBBC19dxsQvzdsnRtl5eFGc3HPhfkk3TIskU9r7jhTgNExV_JJxFsaztQXZoNlm1iHNnqC5Hyf93a1xE_imCGrYhrV1xqHcdb4dQjPMFX1fyAr46QZinZwGYuSjok_S9AJzS_7DxGiy9a8vXVEyvhQjnhD5OErsZDrlCu8Bs-VR-rhes_V4NDSWf2Hxh5uN-0cnzPru7BWWG5X76WEJKgA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5744721f52.mp4?token=Ewn5WS17MB7j5kAUJWl0dGfafdGf_sdUz6IsLgJ4pzguSIBndgytlKGLKMVZ3oSx5u4lp405TEBCI6h6fHm4EXxIhbx5NDqkxFM-fx--j-33AA_bg4CsPGzPeBh8EYvpUBBC19dxsQvzdsnRtl5eFGc3HPhfkk3TIskU9r7jhTgNExV_JJxFsaztQXZoNlm1iHNnqC5Hyf93a1xE_imCGrYhrV1xqHcdb4dQjPMFX1fyAr46QZinZwGYuSjok_S9AJzS_7DxGiy9a8vXVEyvhQjnhD5OErsZDrlCu8Bs-VR-rhes_V4NDSWf2Hxh5uN-0cnzPru7BWWG5X76WEJKgA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
روایت یک امدادگر از جنگ رمضان: پدرم گفت حق نداری به خانه بیایی
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/farsna/456428" target="_blank">📅 20:11 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456427">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AhjNju2QK6HstkK3Gyo3m9cHIGIKNwHWWj3888dqXnvnW6lGM0Uh7y-9OknP0UEdhwSfaIbBg5w0IW_Xp0sVb62h2KSJax8i-rl0dFiavASStX6GSwmyHkRJYT0nfpo8eh5SdUpCpdwZT-M2WVzmTfeiD_eX9zKa1lUc_IBtybflRfdcxGl0cEKk2F1_FNwMNYFy_w1btdYO12ZAM5Dfc8zXMElOds4EgQwLlCGgyE62oKBMtGNPj7vis9NuoGK_RqJXIWcGtHhyD7dU_NhAqtSZSwbAOJtvNBEI43t_3ntW5nlK78Kxc5dDawcdmVkwZths2cMlAeWPIUqrofN38Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">همراه ۲.۴ میلیون زائر در مسیر اربعین
🔹
همراه اول در اربعین ۱۴۰۵ میزبان ۲.۴ میلیون مشترک در عراق بود؛ زائرانی که با استفاده از خدمات رومینگ، بدون نیاز به خرید سیم‌کارت عراقی ارتباط خود را حفظ کردند.
🔹
تخفیف ۳۰ درصدی بسته‌های ویژه سماح، ارائه ۱۰۰ هزار بسته ۱۰۰ گیگابایتی اینترنت داخلی، بیش از ۳۰۰ هزار بسته ویژه روبیکا و پشتیبانی شبانه‌روزی در مرزها و شهرهای زیارتی، از جمله خدمات همراه اول در این ایام بود.
http://mci.ir/-7J70P9
@mcinews</div>
<div class="tg-footer">👁️ 9.12K · <a href="https://t.me/farsna/456427" target="_blank">📅 20:09 · 25 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>

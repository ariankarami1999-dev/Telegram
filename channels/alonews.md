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
<img src="https://cdn4.telesco.pe/file/MTLAxeaui2u_Zq6hgfHRnz6xUtsvPzTZOtnbY9LJpJ2D8XO6SNwxZaI9exg4rqLHDw9pWmFF4ehG2LrpgPWwgQejErWrAFDO5b1STT7CIwyk0uu1jdPM4QgM_DqnTSACtvA9J3gUSmaKBUK8XQACdC2szPWZawu3Bgu8D_q5usyXZt3wYLqq40h6vdB5nKpvNu8zA4wM8L5Fr5y60tjsSuCR41dMYAAke2KSdb-jVMfX8GkK7Cuizn4FAi6sp0Yer_iZJNf16Ak2UsI--KjpiVCpeAl7T9ciV8E8wqAnjqj1CkOnwkj5N8MWqF7Zk5wvurrEe-8A75_JuzELiavguw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 اخبار جنگ الونیوز AloNews</h1>
<p>@alonews • 👥 980K عضو</p>
<a href="https://t.me/alonews" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 با الونیوز از اخبار جنگ و وقایع در چند ثانیه مطلع باش!اخبار جنگ بدون سانسور در الونیوز👌جهت رزرو تبلیغات👇https://t.me/ads_alonewsپشتیبانی کانال🕵️https://t.me/AloNews?directمالک کانال🎩@AloNewsBotX:https://x.com/AloNewsBot</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-27 04:12:47</div>
<hr>

<div class="tg-post" id="msg-142354">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">🚨
آرامش قبل طوفان دلار
❗️
💢
اگه نمیدونید ریزش داره یا صعود عضو کانال آقای ترید بشید  اونجا بهتون میگه تا 3ماه دیگه تارگت کجاست :
👇
https://t.me/+nAClsSFetLA3YjBk
https://t.me/+nAClsSFetLA3YjBk
https://t.me/+nAClsSFetLA3YjBk</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/alonews/142354" target="_blank">📅 01:45 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142353">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pjJVW4YiUoxB3zLrWx44NkFJpOgbwzWxIK_1MeUMBuZo7rRH7QFIw451poXote-JDF0_qFQLkKM7dLhCfrC5eGuauDgLK-uEUcPjkFyNe5fYKbKm4ZYT9lpIYWLZXsnToE3CWkf1iZFIYyUsIqYAhI4x687OUbw9NYw8LiJss3M0h4GVJ2VBDpejOiSsBWcBQpXE6xSEkihhsHwlAmmdIv7XZ6f0yOrXHv6pUbjuUs4I8QoX1BBhjiyOaMuto0lb025492yQZVx3_nHXQ2j3bWg08FhaF2P-bqAC183gb1oRA5z648ipDU4adWzLD_qFPCNgoZIDk7xLF79dzLPClQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
رویترز: ترامپ می‌گوید ایران به توافق مورد نظر او دست نخواهد یافت و تهدید به بمباران عمان کرد
دونالد ترامپ، رئیس‌جمهور ایالات متحده، گفت که احتمال پذیرش توافقی که واشنگتن آن را برای پایان جنگ ضروری می‌داند، از سوی ایران کم است و از تهران خواست تسلیم شود. او مجدداً تأکید کرد که هدف ایالات متحده جلوگیری از دستیابی ایران به سلاح هسته‌ای است. این اظهارات در حالی مطرح شد که مهلت ۶۰ روزه توافق ژوئن ایالات متحده و ایران بدون رسیدن به توافقی نهایی به پایان رسید، در حالی که تنگه هرمز همچنان بسته است و مذاکرات در بن‌بست باقی مانده‌اند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/alonews/142353" target="_blank">📅 01:38 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142352">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">👈
قالیباف چهارشنبه به عراق میره
✅
@AloNews</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/alonews/142352" target="_blank">📅 01:30 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142351">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">👈
دونالد ترامپ اعلام کرد که کیم جونگ اون، رهبر کره شمالی، به پیشنهاد آمریکا برای آغاز گفت‌وگوها پاسخ داده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 31.7K · <a href="https://t.me/alonews/142351" target="_blank">📅 01:18 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142350">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BPQQ7jVp0AK-EeSrVnDuMbCsN7RuKwCziJ17HjcEZjXW6ladi5xlf83FCXA6PNcY8CzdxB8bRFq1PcaS_eI-llaIQe-sEs1dr62rrcuRDZrKlZ_zeHS5rc_EkrYcKqw00xAuR5dLvenW2p3UQEwrIcxN7ctFMNiiuX46jzyi4fdhvpJJ0TDvYhhsh9w7LKnX2ZQOXv2xQVKjdrtJhI8Ak4FnKu7U426Q7zDQAmqT-tw3S5tl1P7jm61oyE2rZcH0r6oBaVJpzQHH7JU0zy6mclfLdbMyWQB5zEOjP_sHapy2T8VVrXtDJ08UKqN8yhVep8Q6PaX0EGB12Gy4MPvn4g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
رسایی:
اسرائیل باید نابود بشه و آمریکا هم از غرب آسیا جمع کنه بره
✅
@AloNews</div>
<div class="tg-footer">👁️ 40.8K · <a href="https://t.me/alonews/142350" target="_blank">📅 00:42 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142348">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RUjSKrcSCPU0NuK3PRv-MDNdo4d4kxl4JNym1GtVs94OGQqQqJRcL16orlfHWVOJETkc0vWDJs1g95KJeiyBVwLuJVwJNWEO-4PVW7w_QOO7ArEF1v7L9dOeoJ5yCBxI4yym-Z0aJsbqA_qZm3sLlx9XAVIM3WXsLWeQ2-a92g9CecjRkYUrAYk14wueEN5uYfoH2chszAAs4QtPKlayUxIx2RToEqQVvwREhSILHAmCxmgGjaux-qnCWoNgO-3GW25ZX_MWpGZu9aU3OWfXe01czYxqxwnxscZb2ZwFU1VZbMAoPpVYuejv5f3IxxcaAE5tZj4OP49fyNfihhzmPQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
پست جدید ترامپ تو تروث سوشال که سعی داره کره جنوبی رو اذیت کنه
✅
@AloNews</div>
<div class="tg-footer">👁️ 46.5K · <a href="https://t.me/alonews/142348" target="_blank">📅 00:22 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142347">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fb0e46cbee.mp4?token=Jx9oyaCOmglZUVqiYMxKwFi8sZJEbyEsCFML8ce8BW-p9LLMmYyGiI79uANDWOA62dlM2P4Z-Sq14H1BdyhuW35Z8MqIrzaV0q--RCgCf5Dqw_B4fVWiBjtQOq33Wc2oUn909_JlqOhvowJSPo-GzUU0RBZu_-L8IuwdAal3IG9PDTJZ_4dy0-myylOAcVo13OqrDpmnYzQGRX7wH6bqhj4qe3JEs5yRIUjwlvhKRWgF5h9wnREoKbnYl7QiKNfsm1r64-7FfgPCxiP_abX_pSmg4c7omNe16QDqmJeqWpYOcJebcyUF17k59dpg6G-S3X7Hw7yHjBA6ss4ek2RpZw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fb0e46cbee.mp4?token=Jx9oyaCOmglZUVqiYMxKwFi8sZJEbyEsCFML8ce8BW-p9LLMmYyGiI79uANDWOA62dlM2P4Z-Sq14H1BdyhuW35Z8MqIrzaV0q--RCgCf5Dqw_B4fVWiBjtQOq33Wc2oUn909_JlqOhvowJSPo-GzUU0RBZu_-L8IuwdAal3IG9PDTJZ_4dy0-myylOAcVo13OqrDpmnYzQGRX7wH6bqhj4qe3JEs5yRIUjwlvhKRWgF5h9wnREoKbnYl7QiKNfsm1r64-7FfgPCxiP_abX_pSmg4c7omNe16QDqmJeqWpYOcJebcyUF17k59dpg6G-S3X7Hw7yHjBA6ss4ek2RpZw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
وزیر امور مالی اسرائیل، بزیل اسموتریچ: کاری که بیش از همه پسر مرا ناراحت کرد، این بود که نتوانست بجنگد.
🔴
در روزهای اول، مدام به من می‌گفت: «بابا، کار را تمام نکن. مقداری برای من باقی بگذار.»
✅
@AloNews</div>
<div class="tg-footer">👁️ 45.9K · <a href="https://t.me/alonews/142347" target="_blank">📅 00:18 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142346">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/m6FO0_so-EXlYDf0pqSaS7-Y7hWgm479ti6yraDPzeoVkif9px3udtBlh9XLfbJyaRh9zT9DvQLnsZQw0148gDG0skkmjjs_fXo6ju-yIy8QT0bWCUVnDcSWsPDPglz9RhBhkCnaGAzd7V0PTWInIc440Ds22z5kLFfKR-Eyd9xKPoBD_zy-6yPnGv2lb5Cva6rVAXGIOa2e3DcVriqQJe_k_iPwPDcnH-k3FEwZNRtxbJDZYTcCqaKCQ46aaPvCDgicaURBhZtLG_DO7q6jJuBdt4LUOSOEJdCHGU4ohdiTjyMBRf0xb30jOpbczMAOh_A2RwQSWCTVHlcqMVtDCw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
شانس توافق هسته‌ای ایران و آمریکا تا سال ۲۰۲۹ به زیر ۲۰ درصد رسیده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 45.1K · <a href="https://t.me/alonews/142346" target="_blank">📅 00:17 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142345">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">👈
مرکز آمار ایران: نرخ تورم قیمت مواد غذایی، با احتساب سالانه، به 128 درصد رسیده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 47.5K · <a href="https://t.me/alonews/142345" target="_blank">📅 00:05 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142343">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/D7R5gSeijgT0IeEX00YTT3TnBrjHVaa_mgf5UFXjsR3NQIPr1z7n9uec5H7EVJGMkGaeOJMrbxQI1Vba3AmxmuCZFq8wt9rBVEFeYBeHzrS7EJCDxplsim-lAsdvtSf_zRnYV-B3A4yJOJc0j4qegzfELaQEuwHL1RFVw3ZLLVfsljbjvsaATZnhTSNKf88qV0CDrGtwKnyMmfAO-lyUmEv4uXrPQVS_LAG--i_Ei-gsoY-Rzjx3N0gHFqjhJVu242fsz9lK8_RDi4oV2g_t5-i6W-mrkYWilVkNoF0CA8p8rfbt1xHjRv3LhmKiFjg6Giq0QSvRlT9EGri81X6YjA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
چهار فروند هواپیمای آمریکایی تانکر سوخت‌رسان که در نزدیکی سواحل ایران پرواز می‌کنند
✅
@AloNews</div>
<div class="tg-footer">👁️ 48.7K · <a href="https://t.me/alonews/142343" target="_blank">📅 00:00 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142342">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">👈
فیلد مارشال محسن رضایی، دبیر شعام: تا حالا زیادی صبر کرده ایم ، لازم شود از NPT خارج میشویم و خودتان میدانید این یعنی چه!
✅
@AloNews</div>
<div class="tg-footer">👁️ 49.2K · <a href="https://t.me/alonews/142342" target="_blank">📅 23:55 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142341">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">‏
👈
تریتا پارسی، معاون اندیشکده کوئینسی: من به طور فزآینده‌ای به این نتیجه رسیده‌ام که جنگ آمریکا، اسرائیل علیه ایران وارد دور سوم خواهد شد
‏
🔴
تریتا پارسی، معاون اندیشکده کوئینسی نوشت: من به طور فزآینده‌ای به این نتیجه رسیده‌ام که جنگ آمریکا، اسرائیل علیه ایران وارد دور سوم خواهد شد. این اتفاق اجتناب‌ناپذیر نیست، اما نشانه‌هایی که از دو طرف و همچنین از کشورهای کلیدی شورای همکاری خلیج فارس دریافت می‌کنم، باعث شده نسبت به این موضوع بسیار بدبین باشم.
✅
@AloNews</div>
<div class="tg-footer">👁️ 48.7K · <a href="https://t.me/alonews/142341" target="_blank">📅 23:52 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142340">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">👈
مدیرعامل مخابرات: سرعت اینترنت بزودی با مهاجرت از کابل مسی به فیبر نوری تا 8 برابر زیاد میشه!
✅
@AloNews</div>
<div class="tg-footer">👁️ 48.4K · <a href="https://t.me/alonews/142340" target="_blank">📅 23:47 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142339">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NUsZ6_BseLFrRWJVjHASmEpi12n3-vaDpa_IRn_xnlo-jpXLcmsT-WmoxPmx15tJWDSxD3aPAvXZUYGElWxfxV_Qbi9GaGb8zIq93hkLpqd5wkBL-azzrqyyUqWqjS5ewbedVnhtxR5GQ0qd8-S2x7sqZgbdhP2hJ_b8icPr6fVkLLwP7NrtFCQeXk0G-JlgCwsbOgfDTwvmAOp1B_A4O7IvaBWoVJv0i4X-vMge29_ixUxZMIe0peaWJ42AVrx2rx_XZwO3Z8Og4KIup9ThHVe7a1B5hVYvHW7OC8UXay2yK-RpUNA9FCybq1AFrM1JRdpTBzkby0insMJje5qzjQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
رشد خیره کننده مساجد در انگلستان:
تعداد مساجد در بریتانیا به ۱۷۵۴ عدد رسید
✅
@AloNews</div>
<div class="tg-footer">👁️ 48.8K · <a href="https://t.me/alonews/142339" target="_blank">📅 23:44 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142336">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hxGI1ryDc8UoHh_YxIsIo7OJoOqhA_cunulx0MCQlRtldygcawnVvk_-vbbnH-nIUgpJFmGHf1zRTIN3ozMJdfyleMx_CWtqGEoHmt2B-rVw8VmPQmX0EOgcpU4ThDmhlmdY0Nv7MnONE1ZsiZyeqNN1DD52J-RCUnh2Zfc9I1vQj_mEH5cIP1zhuN8_6qX77umLNezcDK2CFzQeLg4uHMNcEbEN-M0-xR94RCMWrX8qe1gOlwxOW47BXYox2VJVPfICwlGF8vQlMjW6JIilVrvartCBTmlfTNZ-YMK41j-x_AYfUFOzdnjzEfNvm9KUEZtJqhEkwwkzfLDWaTa-Ow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/FL0RvxpiecoVdmbgZ64XCshSHCVw5A6BxtMyLbTnYlEZR0WpS-ie97_7xA35V7HqjdPKzaopvNKqKLiMk2h04450odhsXjn_gjYCQWPXbsasVItz6OaQjdvsIHMq8A_Xfh7OboJ5icVYo0IiHE3GEj3Hw5KAlxMizpEmifVvLXSHpJIO4HVP737Vgu8HwjDdgf3LM_QYaJasMStriN4AIJqb34GzPRbgrXy8tzBxkOTobe_YXOPhcwqr43nJjNQrt_9ivFpmftIJ-L_VEdw4Tlr4G9soufLZvyzg-nL-Nww2R-GwYp9mrx_c5GCfk4qVoRQLjizBpjoCScOhslr-Ng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/UI9Pea3PHxGYMw8gQojrESx9X_3dNYxFozgy_yN7RV6bS7j8DW2YIrxR-foib-uzPXkFwzXfcY15ugiBvnMcnUsZHEc4Hn7aUEBpBqmrs9xupnYBRI5xoJYnjzrhBZhPc987gyBt10a8yo0LWCi6E6QEY-yRwAnKbGwr_hzKu5lh4jGE38kKAsrOCvR1jyQ5S69CX8eQFDgNAQDVq8Z9csr06BsBFPr-_Ke8VKDUSCUz-3p-8L7GfKrELP38BIA1Ji9Vzd3s7iQYhndjO4WYVBcKYEDMOc6VWY1doOv00cC6-a8R8IcK7SGGZ8Kke0EaEohEnn2bkIkVNlGjvM2IMw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
خودداری چند فروند هواپیمای مسافربری از فرود در فرودگاه دبی و چرخیدن آن‌ها در آسمان به دلایل نامشخص.
✅
@AloNews</div>
<div class="tg-footer">👁️ 46.1K · <a href="https://t.me/alonews/142336" target="_blank">📅 23:41 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142335">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nqLIQKhIx80PSYTcJ0-C19DsOT5n6YrSjk4uKIQyWe3EGDsoJqJTmBqTJR5yaWdujVm_a-yR8Di7QD816QNAdbA76DlV5nWb6VVKMvChJbAn8rdPQooVcWgM43qWbO8eY5PlZgFpxbiAp5HUI3dnTVMXJ6hRWd-3137LvR2r_OhxToY-s64ygRozLF6YJLZePy5mSZDgQWFKyPzMipFY223bjJT6KHRnfmXeBKp38ILe5fL3I40wBp4HR2yPMycKPCc5I5E9ifd9Ev61QBURGjuivsTrrjAObki9v50U8SDffVtnUBMa-6gaxw1dKKFFzQv-YdjRvqI6zAU1wnp5XA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
در نظرسنجی جدید i24 اسرائیل: نتانیاهو و حزبش با اختلاف از آیزنکوت جلو تر هستند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 45.7K · <a href="https://t.me/alonews/142335" target="_blank">📅 23:41 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142334">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">👈
کانال ۱۲عبری: حجم صادرات تجهیزات نظامی اسرائیل به قطر در سال‌های اخیر، صدها میلیون دلار بوده است!
✅
@AloNews</div>
<div class="tg-footer">👁️ 48.2K · <a href="https://t.me/alonews/142334" target="_blank">📅 23:25 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142333">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">👈
اسماعیل بقایی و عباس عراقچی حمله به دفتر رئیس اقلیم کردستان عراق را بسیار مشکوک خواندند و اعلام کردند این عملیات ممکن است فالس فلگ یا پرچم دروغین باشد و کرد ها باید نسبت به اینگونه عملیات آگاه باشند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 49.5K · <a href="https://t.me/alonews/142333" target="_blank">📅 23:21 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142332">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">👈
پولتیکو: رئیس‌جمهور چین قرار است برای نخستین بار در ۱۱ سال گذشته روز ۲۴ سپتامبر در سفر به واشنگتن با ترامپ دیدار کند
🔴
انتظار می‌رود در دستور کار این دیدار تحولات ایران و تنگه هرمز قرار داشته باشد
✅
@AloNews</div>
<div class="tg-footer">👁️ 50.4K · <a href="https://t.me/alonews/142332" target="_blank">📅 23:16 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142331">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromالو توئیت | AloTweet</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/A9trM80BK4it7YZtyBTWRXwNlq7sdpxfsgvl7eeNMoaI9eyrrOwohSzJycUMh_7Kl_cl0WdYqQdjp9v0Ss_Ik6CroTWOvhAsb8Ro2ZD4it5rIZjKMpNe2EgerlJAVOVLvr0toNbpt0oEuQ8zNDCEL8XuBnJqr4eTfw9WqUYQmmJaDRUC3WMWcYZoL5K6x0wwdejWlbxPBDt-3ANupyvMoVyqVC0QKxRDom-w0sFP-jyxSGbRJ3j_KonN8Q8TXuP93ANzk-MDKGpjcLuyQpIzTxq44LbKNI3iqN1Pf7mCVbPL0-aQ7qxpC9yMO-CMTN5duB0qsTRjOEKCq358epxQ7A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یه پسر ایرانی بصورت ناشناس اومده این اعتراف رو نوشته:
من یه پسره ۲۱ ساله‌ام و عاشق یه زن ۴۵ ساله شدم. اولین بار که اونو دیدم، توی یه کافه کتاب بود. احساس کردم کل زندگیم دنبال یه نفر مثل اون بودم.
اونم از من خوشش اومده بود و باهم اشنا شدیم. وقتی قرار شد ازدواج کنیم پسرش که ۲۴ سالش بود مانع ازدواج ما شد
ماهم یه شب باهم نقشه کشیدیم وقتی خونه خوابیده اونو خفه کنیم تا باهم یه زندگی خوبو شروع کنیم
[
@AloTweet
]</div>
<div class="tg-footer">👁️ 49.2K · <a href="https://t.me/alonews/142331" target="_blank">📅 23:14 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142330">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-footer">👁️ 49.1K · <a href="https://t.me/alonews/142330" target="_blank">📅 23:06 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142329">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromکریپتو اسمارت | Crypto Smart</strong></div>
<div class="tg-footer">👁️ 43.1K · <a href="https://t.me/alonews/142329" target="_blank">📅 23:06 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142328">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/B-F4j6evR8xlUZdGNXmpagz-CaH734X6c_52NrlYjx9MdEOV8qNQO9a04gG12y8IOa2HupbDr0cPPNoa-l3iEkcKq0D7ej51ZNZSGe_UzX7x21AvlQW3l4RHB5sNWzAXKRwLuVqBS_DcTGqS3Ou1UP77EZNjLLmWS3vzO5MshEXFMq8LPIHBA5gzDSSlvIv9nMioicFzoBZesRrHdtmnelsduSwl1wjvO_rt5ZSKunYo6ojc-3qnOCGKwPfKdLZq2iSBmRMC5O6lurYJQcuNBDC32vz3T8LiYxZnxsqndj1LsXvYM7T6qmArR2Hmqz3xMmr1HVe1XpGOO-Ln7g--bw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
یک هواپیمای آمریکایی مدل E-3G، که برای هشدار زودهنگام و کنترل هوایی استفاده می‌شود، از ریاض به پرواز درآمد تا در نزدیکی تنگه هرمز فعالیت کند
✅
@AloNews</div>
<div class="tg-footer">👁️ 48.6K · <a href="https://t.me/alonews/142328" target="_blank">📅 23:03 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142327">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Msajx8naPmCzUseuRFShrnpqDxZBWxJYb6AucbhMrvrnQX4bMVPyfMeTOQ8mg_e-75TJoDO3u9WDGJQU8TVOn035Wulf1S_lUqGl8BJTLvF2Gmpy0TNuC8s_I5g2jl7FV5ZVYh_mrU8cv-sq9EWAOu8ftwwO37CbOh3S-Vxm1GkDK7VKAs6AWTXAlwWXqwanC04n7zb7FVqZxWhjWi3F7Pa6SSJcxJkVp8_TBMXZlapIoDJcVcO3siU6sd5A-sdydTL6dkxUdw_0Efrty97NkTm0L7ZQEsXCvotoakTq29LYTcIfdi-xQtbEE82o5-MYde72is1JdqdFjvw3o_uAfA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
غیررسمی/طبق برخی اخبار گویا بزودی قراره به فیلد مارشال، درجه سپهبدی اعطا شود
✅
@AloNews</div>
<div class="tg-footer">👁️ 50.6K · <a href="https://t.me/alonews/142327" target="_blank">📅 22:57 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142326">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">👈
کوشنر ، داماد ترامپ : گفتگوهای بین ایالات متحده و بخش‌های مختلف دولت ایران، قوی‌تر از هر زمان دیگری است.
🔴
گفتگوهای مثبت و سازنده‌ای در جریان است.ترامپ در مورد توافق با ایران صبور خواهد بود
✅
@AloNews</div>
<div class="tg-footer">👁️ 54.1K · <a href="https://t.me/alonews/142326" target="_blank">📅 22:40 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142325">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">👈
کوشنر ، داماد ترامپ : گفتگوهای بین ایالات متحده و بخش‌های مختلف دولت ایران، قوی‌تر از هر زمان دیگری است.
🔴
گفتگوهای مثبت و سازنده‌ای در جریان است.ترامپ در مورد توافق با ایران صبور خواهد بود
✅
@AloNews</div>
<div class="tg-footer">👁️ 53.7K · <a href="https://t.me/alonews/142325" target="_blank">📅 22:40 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142324">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/845779b633.mp4?token=k2ksbzlMVJrGvVCREfYml_ebIQdF8ct2jbltAumxb4QubSBdrABVss123wmYnox_u7TGDcNaztccvoQnnOF0qkl0M3vfS0OEGXEAh52rX6TGqRZy67mVQI8lVyyV49fz7_q6gZa0yMAkNpY3dHcusX6OoXb4QvaEFSh5aNrFAO7pqjhDKop0suZeyO_7V5VwwYu5Gf13wqZQdjF8kWYZCrxv5UicA4RFEYWHT_7HXyDLOA7o1zKZ2WbWLGUL4i_RAheK1WOBlEdtgQ12F4MXNPjGbYc8FXSJzBBBlLIAZY1uzWu7EP26kSzGpyCDhF6b4Y9BOpE9r0Hlovq8LJ3wl4WOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/845779b633.mp4?token=k2ksbzlMVJrGvVCREfYml_ebIQdF8ct2jbltAumxb4QubSBdrABVss123wmYnox_u7TGDcNaztccvoQnnOF0qkl0M3vfS0OEGXEAh52rX6TGqRZy67mVQI8lVyyV49fz7_q6gZa0yMAkNpY3dHcusX6OoXb4QvaEFSh5aNrFAO7pqjhDKop0suZeyO_7V5VwwYu5Gf13wqZQdjF8kWYZCrxv5UicA4RFEYWHT_7HXyDLOA7o1zKZ2WbWLGUL4i_RAheK1WOBlEdtgQ12F4MXNPjGbYc8FXSJzBBBlLIAZY1uzWu7EP26kSzGpyCDhF6b4Y9BOpE9r0Hlovq8LJ3wl4WOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
آیا بنزین گران می‌شود؟!
🔴
رضا نواز، سخنگوی صنف جایگاه داران سوخت: تا الان هیچ تغییری درباره قیمت بنزین قطعی نشده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 55.4K · <a href="https://t.me/alonews/142324" target="_blank">📅 22:28 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142323">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hv_E8Fi6zKfQ3DwPpsy-97Nj6zW-dMCNGYVtDft2KJK86VtKXvycV4d_GR60mvW-ZStG2RRG0OtStfwRHkNe9Av71_TcfgbC7jqY0e4tDb6KgjsHi9Wx2JAvUt9IAzJOqOyosVJ61xl76WwuTnzDMRLBwR1ZTnQGmg9wJaJQXk0f4-LX0SiajLR8dd6DvJLI2xh9WAJ8IOreCBmDlm47ZtJudaG4TP6IPl8eEsFP5jcNIjypiBFd6YW-vKsFQgSpOa0L_pFuK9TUXFsngq8NJJYorzAAIexizNeBxzVBXW_I4M8lLMAdZZOJLbG8mqcmoe8YKpAGDOsK41AKcjiN2g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
واکنش عراقچی به خبر امروز حمله به دفتر بارزانی در اقلیم کردستان عراق: هیچ چیزی حمله نابخردانه به دفتر نخست‌وزیر بارزانی را توجیه نمی‌کند.
🔴
دوستان کرد ما باید در برابر ترفندهای پرچم دروغین که با هدف ایجاد اختلاف میان همسایگان طراحی می‌شوند، هوشیار باشند.
🔴
ما در برابر صدام و داعش از دوستان کرد خود حمایت کردیم و از امنیتی که آنها در مرز ما فراهم می‌کنند، سپاسگزاریم.
✅
@AloNews</div>
<div class="tg-footer">👁️ 58.6K · <a href="https://t.me/alonews/142323" target="_blank">📅 22:18 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142322">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vI1xWU1jEcNpnaA0cH2a_2fUCveDEhAk2RGCgVxjm73x0JtCDJPc5AiS5LXa4kFVUW8WGBOPe8Xhhaj1BWG_Lqoyyx_uXKe5z8wH7-iRuuCy5b5Bx2uk3-j0sJ8HDvk2b1a_vMAqErrSCn4Ofmd7HEL6XzYulnL1t14zuWYfl8hU_0PjjPVGYMeYPGYEbqjfeIMHAfC_8CkR17HjyyrSA_OYDIN4smGLt6_3QK3ib75QeklwaFzcoph27BBigiUsTb8p9Nmpg9Mw0xDyJZFSbvw7GrM5K4Ot6dv_NBec_taBxffNGbuUGdS2N5LCkVPW6Maag9Vv1WtgBtSR5R8SEQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
نفت برنت با افزایش ۲.۵ درصدی از ۹۱ دلار عبور کرد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 57.8K · <a href="https://t.me/alonews/142322" target="_blank">📅 22:15 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142321">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">👈
وزیر نیرو: با درایت مسئولین، قطعی برق امسال بسیار کمتر شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 54.7K · <a href="https://t.me/alonews/142321" target="_blank">📅 22:13 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142320">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">👈
تحولات به شدت داره خبر از جنگ مجدد میده
✅
@AloNews</div>
<div class="tg-footer">👁️ 56.8K · <a href="https://t.me/alonews/142320" target="_blank">📅 22:08 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142319">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">👈
کان: احتمال شروع مجدد جنگ بسیار بالاست
✅
@AloNews</div>
<div class="tg-footer">👁️ 59.8K · <a href="https://t.me/alonews/142319" target="_blank">📅 22:01 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142318">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">🔴
فوری/قدم بعدی ترامپ مشخص شد
‼️
👇
👇
👇
👇
https://t.me/+S8mMBRHkHmFiMTFk
https://t.me/+S8mMBRHkHmFiMTFk</div>
<div class="tg-footer">👁️ 61.3K · <a href="https://t.me/alonews/142318" target="_blank">📅 21:57 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142317">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9f5f083dc2.mp4?token=f8VJir6Rb2TKvFQGVIJxnfQkitTLDlh_2F1_hqOtS8AFfq0Z-cmut9Yr_TuYGjqICwogeCfRbJN50w5ROHeI27xv6CldlKPCb6QqjbZ6O10YNkfwfjND-ukou4O9ByEs8_WBcjyJ7UgVn_1sPqFPfi2EytoAlOJ4RL3rjR4S3OWhJs8S5Ta-NaUicjJIXI18m14cBEErYmgmKznY5K5i3MYrS2Btnar1yrvpNE1WteVd8x8t-9rfiPwehmvvYbTuf5tZHzhSwrmmU6njianhn-Z4eTTpQ9tyEumUPb8UapjadeZzt0OyN0faTt4kHPPI7Kt86ea9OLYNCIwcXLw8yg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9f5f083dc2.mp4?token=f8VJir6Rb2TKvFQGVIJxnfQkitTLDlh_2F1_hqOtS8AFfq0Z-cmut9Yr_TuYGjqICwogeCfRbJN50w5ROHeI27xv6CldlKPCb6QqjbZ6O10YNkfwfjND-ukou4O9ByEs8_WBcjyJ7UgVn_1sPqFPfi2EytoAlOJ4RL3rjR4S3OWhJs8S5Ta-NaUicjJIXI18m14cBEErYmgmKznY5K5i3MYrS2Btnar1yrvpNE1WteVd8x8t-9rfiPwehmvvYbTuf5tZHzhSwrmmU6njianhn-Z4eTTpQ9tyEumUPb8UapjadeZzt0OyN0faTt4kHPPI7Kt86ea9OLYNCIwcXLw8yg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ درباره ایران: «ایران با مشکلات بزرگی روبه‌روست و وضعیت این کشور آشفته است.
🔴
نیروهای نظامی ایران کاملاً شکست خورده‌اند.»
✅
@AloNews</div>
<div class="tg-footer">👁️ 60.1K · <a href="https://t.me/alonews/142317" target="_blank">📅 21:55 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142316">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">🔴
فوری/دونالد ترامپ: به دنبال تمدید یادداشت تفاهم با ایران نیستیم‌‌
✅
@AloNews</div>
<div class="tg-footer">👁️ 57K · <a href="https://t.me/alonews/142316" target="_blank">📅 21:52 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142315">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/85f96aa426.mp4?token=WuPcIjFRHDvOMNjTCVZAN5MvTNNrGfKNJy5IYXKq4wihWkqYAeFihDE1aj4Y6NsJyz-GtY1XHsUCnyBytTDJCk7H8taX0MQ-tnV6vANjG7xjK7r2wyMQH1UpTnn1pngS4m3ahkjxBE_ifKzADO7ms-Fg4gIJx-SI1WM8mgxdikZtzXMd4tVEKlSUluctzVeStDczFXNeT8-BI0dX3gi2g_fJFeawa4yNbH5I496j3RgegpwH-GMr4686r37sNdcZcIi0D6imy9yZO_2Puk4KTLPJOptc8Ly4x-jJhis89q9LpFsdH97G1ERre-OixxxtkzUDHq33ahOdwQPnv-yoJw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/85f96aa426.mp4?token=WuPcIjFRHDvOMNjTCVZAN5MvTNNrGfKNJy5IYXKq4wihWkqYAeFihDE1aj4Y6NsJyz-GtY1XHsUCnyBytTDJCk7H8taX0MQ-tnV6vANjG7xjK7r2wyMQH1UpTnn1pngS4m3ahkjxBE_ifKzADO7ms-Fg4gIJx-SI1WM8mgxdikZtzXMd4tVEKlSUluctzVeStDczFXNeT8-BI0dX3gi2g_fJFeawa4yNbH5I496j3RgegpwH-GMr4686r37sNdcZcIi0D6imy9yZO_2Puk4KTLPJOptc8Ly4x-jJhis89q9LpFsdH97G1ERre-OixxxtkzUDHq33ahOdwQPnv-yoJw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ درباره ایران: «ما هر هفته میلیون‌ها بشکه نفت خارج می‌کنیم؛ شاید این روند متوقف شود یا حتی بیشتر گسترش پیدا کند.
🔴
تنگه هرمز باز است و قیمت نفت در حال کاهش است و این کاهش ادامه خواهد داشت؛ مگر اینکه تصمیم بگیریم اقدامی بسیار شدیدتر از آنچه اکنون انجام می‌دهیم، انجام دهیم.»
✅
@AloNews</div>
<div class="tg-footer">👁️ 56.1K · <a href="https://t.me/alonews/142315" target="_blank">📅 21:50 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142314">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/434bd2f553.mp4?token=FNL5Q3UhtiVKpb0IoBaR95yT5dgj_44xaQezo5bK4CAQAMpTSKQr1jFC6tBT3tSqeWqN8AjE03nFq048SKdBCF2vWQJm_da9wbuPkkBdYXHhD_5YTL4LShm9UZfw0Ri-m5XzAYrLYoM3ZOYPgGnKW-hIRWMTMaJEh9U2nBgMPIjy0nDA0YV-qw6x8f998J30m3uFHcUeIiDoKR_veVEj94pjQOpMlGuoZoFxT5YkECGtC4ckbK2zpAz-o4d-RPmUQBxoTlSqnTntNDc7CqG6YyARRIcJAe0S0Tr5Zlo5n1FKS5QicEe2OnHQ3dSGOL8Nu6O29rIHZIUtyJ0n06rdiA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/434bd2f553.mp4?token=FNL5Q3UhtiVKpb0IoBaR95yT5dgj_44xaQezo5bK4CAQAMpTSKQr1jFC6tBT3tSqeWqN8AjE03nFq048SKdBCF2vWQJm_da9wbuPkkBdYXHhD_5YTL4LShm9UZfw0Ri-m5XzAYrLYoM3ZOYPgGnKW-hIRWMTMaJEh9U2nBgMPIjy0nDA0YV-qw6x8f998J30m3uFHcUeIiDoKR_veVEj94pjQOpMlGuoZoFxT5YkECGtC4ckbK2zpAz-o4d-RPmUQBxoTlSqnTntNDc7CqG6YyARRIcJAe0S0Tr5Zlo5n1FKS5QicEe2OnHQ3dSGOL8Nu6O29rIHZIUtyJ0n06rdiA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ درباره ایران: «از ایده اعلام تنگه هرمز به‌عنوان قلمرو ایالات متحده خوشم می‌آید.
🔴
ما کنترل کامل تنگه هرمز را در اختیار داریم.»
✅
@AloNews</div>
<div class="tg-footer">👁️ 52.9K · <a href="https://t.me/alonews/142314" target="_blank">📅 21:48 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142313">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/abc9ea29b6.mp4?token=rcGrqMvROb3hWnnKKfFT7_beIuc5DSUIPZsiCJxQMVi9LI8mFwg1oiidpmrXRsLHiaoqgIh6ejr2khJ5KDv938i6pEINiY6P5vjSVnIMwI1i3WTS4vyXfQUl1SLf02BDDHvIfQeYyjSXVi_PQWFBzb_m4_U35Qemed8f_VZt97xr2FniYzLaRMvs-5XrSinDsEJxzbqb8uWFziTtQptIjTy7l74dwmw2Y90MtsPneUzOf9cHGn3LVjZLqtjyF5FZCRo4v9JNhMGd3N79G9qFc6-j7c3I6IGqxelqcesX2TuVV2baYtIn8-d1aPTWwM4H5y3MF1dIcgbktfx3b-CbIg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/abc9ea29b6.mp4?token=rcGrqMvROb3hWnnKKfFT7_beIuc5DSUIPZsiCJxQMVi9LI8mFwg1oiidpmrXRsLHiaoqgIh6ejr2khJ5KDv938i6pEINiY6P5vjSVnIMwI1i3WTS4vyXfQUl1SLf02BDDHvIfQeYyjSXVi_PQWFBzb_m4_U35Qemed8f_VZt97xr2FniYzLaRMvs-5XrSinDsEJxzbqb8uWFziTtQptIjTy7l74dwmw2Y90MtsPneUzOf9cHGn3LVjZLqtjyF5FZCRo4v9JNhMGd3N79G9qFc6-j7c3I6IGqxelqcesX2TuVV2baYtIn8-d1aPTWwM4H5y3MF1dIcgbktfx3b-CbIg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ: «کسانی که با ساخت سالن رقص مخالفت می‌کنند، به نظر من افرادی هستند که به کشورمان وفادار نیستند؛ بسیار، بسیار بی‌وفا به کشورمان.»
✅
@AloNews</div>
<div class="tg-footer">👁️ 51.3K · <a href="https://t.me/alonews/142313" target="_blank">📅 21:46 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142312">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8c26719b14.mp4?token=CRePsSQOgi2cKAl7ezmwsoCUvKE62pcC0Yrtb4u86orbyN-3T45jshnq_ZZZEWiMLmFtYAQwpkPwcBYhOFSDZYYSpeRh6Wg7MUm28A4HGmgFdIaKcsjd6Cwd4p9OsI6zpleTZAquzyOmwV-8YwmIvrezG65OsNVn5YVvYKQWLuj5Ol3IXA9328WkLZ7bnKs9asF7chgIqSBgWebSe1rt2dhSx9yQVbDxNoJHzRCsBwptqzpFvcwcB6XWGtLActdXbpwk3tzuJ6Urh9k1q_x7gbGmJXFZ-Vw40LK1sZtfUznUsg2aDbLbWM7fkfmaFHipQlEjann2gahX8F-hs_4v0w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8c26719b14.mp4?token=CRePsSQOgi2cKAl7ezmwsoCUvKE62pcC0Yrtb4u86orbyN-3T45jshnq_ZZZEWiMLmFtYAQwpkPwcBYhOFSDZYYSpeRh6Wg7MUm28A4HGmgFdIaKcsjd6Cwd4p9OsI6zpleTZAquzyOmwV-8YwmIvrezG65OsNVn5YVvYKQWLuj5Ol3IXA9328WkLZ7bnKs9asF7chgIqSBgWebSe1rt2dhSx9yQVbDxNoJHzRCsBwptqzpFvcwcB6XWGtLActdXbpwk3tzuJ6Urh9k1q_x7gbGmJXFZ-Vw40LK1sZtfUznUsg2aDbLbWM7fkfmaFHipQlEjann2gahX8F-hs_4v0w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
خبرنگار: آیا در ناو هواپیمابر آبراهام لینکلن غذای کافی وجود دارد؟
🔴
ترامپ: «بله، وجود دارد. گزارش سی‌ان‌ان درباره این موضوع جعلی بود.
🔴
در سال‌های گذشته، ناوهای ما مدت‌های بسیار طولانی‌تری در دریا حضور داشته‌اند.
🔴
یکی از دریاسالاران به من گفت: قربان، من مدت بسیار بیشتری از این روی کشتی‌ها بوده‌ام. نیروهای حاضر در لینکلن هم می‌گویند که به‌خوبی از آن‌ها رسیدگی می‌شود.»
✅
@AloNews</div>
<div class="tg-footer">👁️ 50.6K · <a href="https://t.me/alonews/142312" target="_blank">📅 21:46 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142311">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8dbd66f94a.mp4?token=nsERUzlHRSOs48P8LElSC1L31ApSodTcOLXOsUmSOXvQqtjT__-7IuXKHVnI0vTviLN3x9hi7ZQ4jwEOmsD65D7cPa3rwxapdbmLsfwmaU-NrLBOnKQi6u8pmFSOycZJti1pjVH9Vkyz4rPf9KEeisMIJBr9t11yilJ31R3MLLYsnXzJBGlsRw6-8utUoaWf3wdaHoNYbaeV2yW5L3UMU23hUWkHDkRBhRAE4I2_9bJyvCXS9ngb6DFta02PBdYQYpVCqO4S9aKbrT5mZMrGlZbnqfJQcjt0eB_5GOWZiLcuWopr8XToF0F-gjZTEnSWEfv_rDwUPNhBwX2b68AEfYWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8dbd66f94a.mp4?token=nsERUzlHRSOs48P8LElSC1L31ApSodTcOLXOsUmSOXvQqtjT__-7IuXKHVnI0vTviLN3x9hi7ZQ4jwEOmsD65D7cPa3rwxapdbmLsfwmaU-NrLBOnKQi6u8pmFSOycZJti1pjVH9Vkyz4rPf9KEeisMIJBr9t11yilJ31R3MLLYsnXzJBGlsRw6-8utUoaWf3wdaHoNYbaeV2yW5L3UMU23hUWkHDkRBhRAE4I2_9bJyvCXS9ngb6DFta02PBdYQYpVCqO4S9aKbrT5mZMrGlZbnqfJQcjt0eB_5GOWZiLcuWopr8XToF0F-gjZTEnSWEfv_rDwUPNhBwX2b68AEfYWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ: ساکت، ساکت، ساکت. شما بسیار بی‌احترامی می‌کنید. ساکت باشید. شما با چه کسی هستید؟
🔴
خبرنگار: من از شبکه CNN هستم.
🔴
ترامپ: شما اخبار دروغین را پخش می‌کنید. ساکت باشید، ساکت باشید، ساکت باشید. شما یک خبرنگار دروغگو هستید.
✅
@AloNews</div>
<div class="tg-footer">👁️ 46.5K · <a href="https://t.me/alonews/142311" target="_blank">📅 21:43 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142310">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7ce69956d0.mp4?token=KXtkHN3ezFJXfIla7e6pfBlWVNCMEGGKwUvwLo29-tjSVxTK1nWLewWzKaBHk0Gtfod_e6zIJWMty5ZqTTcbAuC6r1b08NQJiAmKqchu7CZcUIxGyRJ_6yHf0mAiaVWQqHKQwKpCOCKrWf5bTL2hkO8zXJoiw5g8-a5lUdvzJ2fhW-VCNK1gqzKGIZmYW1rUBVcXFor8pta0wGsszYACtZCJm3Ozpx96sihzahHLQZouQ5GQvO00YHzn2YOuBkpLrxZai2iAPbqPyW__Hsoxs4G2ZscAeB5b91cotTytQ3tk9Q_wWVrENva7swYRfD95t8XuVoIr3KnAzzjj2qBkVA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7ce69956d0.mp4?token=KXtkHN3ezFJXfIla7e6pfBlWVNCMEGGKwUvwLo29-tjSVxTK1nWLewWzKaBHk0Gtfod_e6zIJWMty5ZqTTcbAuC6r1b08NQJiAmKqchu7CZcUIxGyRJ_6yHf0mAiaVWQqHKQwKpCOCKrWf5bTL2hkO8zXJoiw5g8-a5lUdvzJ2fhW-VCNK1gqzKGIZmYW1rUBVcXFor8pta0wGsszYACtZCJm3Ozpx96sihzahHLQZouQ5GQvO00YHzn2YOuBkpLrxZai2iAPbqPyW__Hsoxs4G2ZscAeB5b91cotTytQ3tk9Q_wWVrENva7swYRfD95t8XuVoIr3KnAzzjj2qBkVA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ درباره کیم جونگ اون: «کیم جونگ اون همیشه با احترام زیادی با من رفتار کرده است.
🔴
ما مدتی را با هم گذرانده‌ایم؛ من او را درک می‌کنم و او هم من را درک می‌کند
🔴
او تقریباً از هیچ‌کس خوشش نمی‌آمد، اما من رابطه بسیار خوبی با او دارم.»
✅
@AloNews</div>
<div class="tg-footer">👁️ 45.7K · <a href="https://t.me/alonews/142310" target="_blank">📅 21:42 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142309">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/623c03350d.mp4?token=CnjUhhNda0CZ0kOVvMoyUmgk1sliGWZ7Y-mUcLOVtW2RR3uBozi2YMDhtIg5IT1Tp4PJRnPGCUlAi6nJA0e3lUXFctTNm4NTwl7GkPpdE9HSYb18Sz4WM8zspLzYmyj2VSmDmh3jVNpKUhm9NgncmuXkBnCBGD9RdIu5UUMyUCdVm-t7mIz78_AF_vIk9_HWublS0KbBbvnbEsKDEmTp-cOjI9rtE_HwVZ2LMSsNmt7C6wgTGtanXmsc86S2h4TAcPEyDJTJ3UsJYkrhNtcQ-7kdF7R_fxgAL5Vz5LHFffZs7v0K72XmK-yhRlEcAeKbqbcph_3i2Fi6bbVJpYKYgQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/623c03350d.mp4?token=CnjUhhNda0CZ0kOVvMoyUmgk1sliGWZ7Y-mUcLOVtW2RR3uBozi2YMDhtIg5IT1Tp4PJRnPGCUlAi6nJA0e3lUXFctTNm4NTwl7GkPpdE9HSYb18Sz4WM8zspLzYmyj2VSmDmh3jVNpKUhm9NgncmuXkBnCBGD9RdIu5UUMyUCdVm-t7mIz78_AF_vIk9_HWublS0KbBbvnbEsKDEmTp-cOjI9rtE_HwVZ2LMSsNmt7C6wgTGtanXmsc86S2h4TAcPEyDJTJ3UsJYkrhNtcQ-7kdF7R_fxgAL5Vz5LHFffZs7v0K72XmK-yhRlEcAeKbqbcph_3i2Fi6bbVJpYKYgQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ درباره ایران: «آن‌ها خواهان توافق هستند، اما حاضر نیستند توافقی را بپذیرند که من آن را ضروری می‌دانم.»
✅
@AloNews</div>
<div class="tg-footer">👁️ 45.7K · <a href="https://t.me/alonews/142309" target="_blank">📅 21:39 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142308">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cf45ba5f07.mp4?token=a907t6YRo-g0-3JwIT5N8gKH1EOOERwII_HKCvfXT2JAOgzkUTQByXs-nhktlVh3cQBjI_ZHteADQQRMuTLjcXN2_XX6Z3To00_b5EVVmRoAF6TP-6gIIyeDZPHwhq2A5EHEHZlUoIqE6IOxb793LKSu-yVZ4RmRMAdIGlLC85wjBeV_Wq9ycxcB4ig1UzrFpO6Wrue2XZk7ZVKHSKBsdWNzbs3c63-wUnCoTMEjd7ydDk9T-eeF_jr4rRFtOYPVjmsIXKAX68CMNGyBm57VIjt6m2oMe6naJ06CWD9arFQ_kirLges_xdpeSsb1leY7Jwpi8dkX_4hVwHk5yRxqMg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cf45ba5f07.mp4?token=a907t6YRo-g0-3JwIT5N8gKH1EOOERwII_HKCvfXT2JAOgzkUTQByXs-nhktlVh3cQBjI_ZHteADQQRMuTLjcXN2_XX6Z3To00_b5EVVmRoAF6TP-6gIIyeDZPHwhq2A5EHEHZlUoIqE6IOxb793LKSu-yVZ4RmRMAdIGlLC85wjBeV_Wq9ycxcB4ig1UzrFpO6Wrue2XZk7ZVKHSKBsdWNzbs3c63-wUnCoTMEjd7ydDk9T-eeF_jr4rRFtOYPVjmsIXKAX68CMNGyBm57VIjt6m2oMe6naJ06CWD9arFQ_kirLges_xdpeSsb1leY7Jwpi8dkX_4hVwHk5yRxqMg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ
:
«ما نمی‌توانیم مدام از همه این کشورها محافظت کنیم؛ به‌خصوص وقتی که آن‌ها حاضر نیستند در زمان نیاز به ما کمک کنند.».
✅
@AloNews</div>
<div class="tg-footer">👁️ 45.8K · <a href="https://t.me/alonews/142308" target="_blank">📅 21:38 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142307">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d292649909.mp4?token=qMtN8Hni4pgvpyK_80Ta2mU4RyjXhwAtub_m2HruAqvozIKpW06-4juFaMFaaqqvMzdVvLhN5PspnLusYgy0peTIMlJU_7Om36wJo5shQjgFNeIgtGk1beqWfTBRDIwmAhzrTpSd5biNXIRZ_84pSPqGkDqPEYBDNddQ8kK5gJ31tTBBZGgzwlrlokMdBtovonqB7eyOBwcU1zh3YyLHZhv9NqsN26SMPeho9mf6j8XjCc2LhCSqCOSRnMp74_CgSW9T0nct5yJaX6KsjpkK8yLJiUPJGSiRREyteiPi3cdvWW7GVkq_SB4Xaaz2yVDf90Khm2YZSglaLR9zmP-ouA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d292649909.mp4?token=qMtN8Hni4pgvpyK_80Ta2mU4RyjXhwAtub_m2HruAqvozIKpW06-4juFaMFaaqqvMzdVvLhN5PspnLusYgy0peTIMlJU_7Om36wJo5shQjgFNeIgtGk1beqWfTBRDIwmAhzrTpSd5biNXIRZ_84pSPqGkDqPEYBDNddQ8kK5gJ31tTBBZGgzwlrlokMdBtovonqB7eyOBwcU1zh3YyLHZhv9NqsN26SMPeho9mf6j8XjCc2LhCSqCOSRnMp74_CgSW9T0nct5yJaX6KsjpkK8yLJiUPJGSiRREyteiPi3cdvWW7GVkq_SB4Xaaz2yVDf90Khm2YZSglaLR9zmP-ouA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ
: «با رئیس‌جمهور کره جنوبی تماس گرفتم و گفتم: آیا برای موضوع ایران به ما کمک می‌کنید؟ البته اگر بخواهید؛ ما نیازی به کمک نداریم. او گفت: نه، ممنون.»
🔴
«گفتم منظورتان چیست؟ ما ۳۹ هزار سرباز آنجا داریم که از شما در برابر کیم جونگ اون محافظت می‌کنند، اما شما حاضر نیستید درباره ایران به ما کمک کنید؟ عجیب است.»
🔴
«پس چرا ما باید به شما کمک کنیم؟ حفاظت از کره جنوبی میلیاردها دلار برای ما هزینه دارد.»
✅
@AloNews</div>
<div class="tg-footer">👁️ 44.6K · <a href="https://t.me/alonews/142307" target="_blank">📅 21:38 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142306">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">👈
ترامپ: ایران می‌خواهد به توافق برسد و ما به یک دلیل آنجا هستیم و آن جلوگیری از دستیابی آن‌ها به سلاح هسته‌ای است
✅
@AloNews</div>
<div class="tg-footer">👁️ 41.3K · <a href="https://t.me/alonews/142306" target="_blank">📅 21:36 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142305">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">👈
خبرنگار: شما گفته بودید اگر عمان در مسیر بازگشایی تنگه هرمز مانع‌تراشی کند، «حسابی آنجا را بمباران خواهید کرد». آیا می‌گویید دیگر صبرتان در قبال عمان، که یک شریک راهبردی است، به پایان رسیده است؟
🔴
ترامپ: فکر نمی‌کنم آنها رفتار خیلی خوبی کرده باشند، اما ما به‌راحتی از پس آنها برمی‌آمدیم؛ درست همان‌طور که با مسائل دیگر برخورد می‌کنیم.
✅
@AloNews</div>
<div class="tg-footer">👁️ 43K · <a href="https://t.me/alonews/142305" target="_blank">📅 21:36 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142304">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0da1c4c2eb.mp4?token=HZbyd6pJWSfNJ0ygswx9pqI8zaGI4rkt6wITO9GjqpoVjkg_LZBr_Yj_RCVoa4TmzNt-cdTUoTMOy0tFX8WVpLIUMOUJT1gIPiVRDHBMnvgcEyiBPsHjq6YKNkm6WxO71wgC9iiO5XnotatPK6bWyS6zXlaLidkvqzASiSdM3Pw6wCqi8arFsfjJoOv9OF9CBGgKWugZoPq9qk6DvrKEYmjTdA-ye4GiJYbvP4Rzj9JhxdBXtm1ESe7w_B7OOHnYqybryRUBbxlrNcSNgGQpvxCEBgpjPfmdWcImXUAj1vvxP8Bap1CU5ELrrTtnIvxk2H9h2F8ddUmHsT2Ft-pnnQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0da1c4c2eb.mp4?token=HZbyd6pJWSfNJ0ygswx9pqI8zaGI4rkt6wITO9GjqpoVjkg_LZBr_Yj_RCVoa4TmzNt-cdTUoTMOy0tFX8WVpLIUMOUJT1gIPiVRDHBMnvgcEyiBPsHjq6YKNkm6WxO71wgC9iiO5XnotatPK6bWyS6zXlaLidkvqzASiSdM3Pw6wCqi8arFsfjJoOv9OF9CBGgKWugZoPq9qk6DvrKEYmjTdA-ye4GiJYbvP4Rzj9JhxdBXtm1ESe7w_B7OOHnYqybryRUBbxlrNcSNgGQpvxCEBgpjPfmdWcImXUAj1vvxP8Bap1CU5ELrrTtnIvxk2H9h2F8ddUmHsT2Ft-pnnQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
خبرنگار: چرا کیم جونگ اون به درخواست شما برای گفت‌وگو پاسخ نداده است؟
🔴
ترامپ:
«شما از کجا می‌دانید؟»
🔴
خبرنگار:
یعنی پاسخ داده است؟
🔴
ترامپ:
«اِم... بله، بله.»
✅
@AloNews</div>
<div class="tg-footer">👁️ 44.2K · <a href="https://t.me/alonews/142304" target="_blank">📅 21:35 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142303">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7fdab4a5a7.mp4?token=MX9DiQ_MLrbJmhyGIZNufr2qDFpLBRtDYVGgpEYufZV8B0bGDuRW_N74D74amxMWifVE8yX6Ona922XnhEa8GmeakafCyU-V2UZYxIPxulsBqQT_r5kbhjz5I_OxtlOsJuAb6IOsfKqO4F6TqYSTnmeBd3OKe_M1f8xkvo_ZLsgK9tamWxB6_AlG5N7iGXRlddKGnQrmpWjJExMRqVEaITT12v3hSIX7RDoFAhXiFLXl1u6KU8gy0fdhMMklk8lZBceASDa2-TAFKgTfFzF1ouDdET-ya3lgZDpwE-wb9GIg_6j1y2zSnd2z0lm3bFpjJ9UZwd86pHIMeHfxN5Po1A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7fdab4a5a7.mp4?token=MX9DiQ_MLrbJmhyGIZNufr2qDFpLBRtDYVGgpEYufZV8B0bGDuRW_N74D74amxMWifVE8yX6Ona922XnhEa8GmeakafCyU-V2UZYxIPxulsBqQT_r5kbhjz5I_OxtlOsJuAb6IOsfKqO4F6TqYSTnmeBd3OKe_M1f8xkvo_ZLsgK9tamWxB6_AlG5N7iGXRlddKGnQrmpWjJExMRqVEaITT12v3hSIX7RDoFAhXiFLXl1u6KU8gy0fdhMMklk8lZBceASDa2-TAFKgTfFzF1ouDdET-ya3lgZDpwE-wb9GIg_6j1y2zSnd2z0lm3bFpjJ9UZwd86pHIMeHfxN5Po1A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
خبرنگار: آیا به دستیابی به توافق نهایی درباره ایران نزدیک‌تر شده‌اید؟
🔴
ترامپ: «اجازه دهید ابتدا صحبت‌هایمان با رایدر را تمام کنیم؛ بعد از آن به چند مورد از این سؤال‌ها پاسخ خواهیم داد.»
✅
@AloNews</div>
<div class="tg-footer">👁️ 41.3K · <a href="https://t.me/alonews/142303" target="_blank">📅 21:34 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142301">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/gB4jSovTJvmqFqlWDHqZqgWIuSMStEp554CECMvYcZkgytCs6p6k5BincSr_HWLZM_t_lampMQI8hrgWThMPpQewEMHNFRRCxJzl6fYRwOlbGIuv-5LpGB0Kpsuh0fb_6y8iWLrX0pwcEi7MRwRU_OLaEJUf1KybvzzJoBKj2M0eeLHuz60fqhDmyw45qbiJquf9h4YejDK1ZhdlyZgrNrzSv1ldB0p_w7wdaHB_5_TDLlEoMpYk1sYsqC6LTDY8vqlN5EzeWoEYkqdlsJ57kCOeXq3W5MrUd8vBqkkiPVfuRMkaERxDAk6-wlILCMBvZW0eR3z2_qOfELJx-keMzg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/S4QKJNLGi2Ua1hHe9ifcgtTSeJZPd3A6_668AkoLdFTTel15d6pd4vk4V-9c-TM-zpgmPcpTOqsrNJvpUax5L6srRxHKgqx7E_qrlr2EhpzjSGPdqglzYwKRqFCJhSffWLu6T8SDPIAyM1L1G4Gwx5rRQLQIrvyb4lPJELrOEsBREyeR0t8kSRKoGQTO3tGDpDr8r_nAfqSvWsRgyUNOeFGITE3H2rqfyGNIz1OaariWHDdbHwWM7g3M5zKdWva0_pr0DIaDPeLK7DmAUGVCwzqm2pIoqJrtkEZoPlikQ1U63_dPzpdylsha7uiQ5YGKKsPrZH10CE9NiwwoG_bBrQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
یک فروند هواپیمای ترابری از نوع C-17A اماراتی دقایقی پیش در تل‌آویو فرود آمد
✅
@AloNews</div>
<div class="tg-footer">👁️ 42K · <a href="https://t.me/alonews/142301" target="_blank">📅 21:30 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142300">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UhXTEyp7i5HgwkNQAcYE98n_iT7LiV4ozA6VReUsCQMoMYfrfqowmD4T9s2m1cTENGZpKpO1WppR_olkuw04gOSwZfm6f5skB2erg2izR8wrYC6cNkx6GJjd_W2Jv55njKrKgnOePGEyXTeoGwhQ4t2b82pRkoEzcWQzIYzoRuCbc61pBGv0WwIDuygic3aZ1ndM68BD6eUv5Ww2YnkZWI9uE_OE70x3my9hIMSKPnyxML23ix9sbeBtDRYYLMfNAb6n1ULrxm0v4rf_RyRz7NHGwesv5eAeo0p5Y-eOW4Ex6L-Vg4xH0KExTUqzGFKPLbaixlVS8kqHidyUmMMLDA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
فوری / تلگراف: "ترامپ" در حال بررسی امکان حمله هسته‌ای به ایران با پایان مهلت توافق صلح است
✅
@AloNews</div>
<div class="tg-footer">👁️ 46.2K · <a href="https://t.me/alonews/142300" target="_blank">📅 21:26 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142299">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">👈
وزیر انرژی آمریکا: هدف، خفه‌کردن اقتصاد ایران است
🔴
وزیر انرژی آمریکا مدعی شده ایران در حال حاضر قادر به صادرات هیچ نفتی نیست و واشنگتن همزمان تلاش می‌کند جریان نفت و گاز از تنگه هرمز ادامه پیدا کند.
🔴
او گفت روز شنبه بیش از ۳۰ کشتی از هرمز عبور کرده‌اند و صریحاً اعلام کرد راهبرد آمریکا «اعمال یک محاصره اقتصادی خفه‌کننده» علیه ایران است.
🔴
پیام واشنگتن روشن است؛ حفظ جریان انرژی برای بازار، همزمان با بستن مسیر درآمدهای نفتی ایران.
✅
@AloNews</div>
<div class="tg-footer">👁️ 41.9K · <a href="https://t.me/alonews/142299" target="_blank">📅 21:23 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142298">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/690d167119.mp4?token=o0-2Wepk6TgsGfp9jGbxmruIKCcdKZTvgRVdao7KNnkGStuCfu20harpNfEXTqm7bGm95xO6I9RCeiXmLE3Zos7SzJd2r984C02suhLJeKmxlz4lp__OhkYzZCQJW1y2PSjHOKgoM1oO0bnp3JJZlAfQ6JrZqKK4bzrrW4-1avkGrd7xeUU51Vh0WI0bK0afnWpYs3HxT-Pn6sBBTZ0i7REcgHuLKTAC-1eWcnM7qS-pIFNOnzzma6EN_irFZEZFhUvuSy8DBR2HjPS1QDuCkwTYr92BhYYGiLLFyLfiFZug3Q1GfaI0h4E-5BIJoQrdlS73A7RX3AOJr3HVj4-T-Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/690d167119.mp4?token=o0-2Wepk6TgsGfp9jGbxmruIKCcdKZTvgRVdao7KNnkGStuCfu20harpNfEXTqm7bGm95xO6I9RCeiXmLE3Zos7SzJd2r984C02suhLJeKmxlz4lp__OhkYzZCQJW1y2PSjHOKgoM1oO0bnp3JJZlAfQ6JrZqKK4bzrrW4-1avkGrd7xeUU51Vh0WI0bK0afnWpYs3HxT-Pn6sBBTZ0i7REcgHuLKTAC-1eWcnM7qS-pIFNOnzzma6EN_irFZEZFhUvuSy8DBR2HjPS1QDuCkwTYr92BhYYGiLLFyLfiFZug3Q1GfaI0h4E-5BIJoQrdlS73A7RX3AOJr3HVj4-T-Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
وحشت مردمِ «گالراس» از «ابرهای خونین» در آسمان
🔴
‏ ساکنان شهر گالراسِ کلمبیا چند روز پس از وقوع زلزله‌ای قدرتمند در غرب این کشور، تصاویر غیرمعمول از آسمان شهر که با ابرهای سرخ تیره پوشیده شده را در رسانه‌های اجتماعی منتشر کرده‌اند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 43.3K · <a href="https://t.me/alonews/142298" target="_blank">📅 21:20 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142297">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Yzvbv7BGBRip-hsFkJ6eWTaRCfZCAgjKcOuvhqt8o0vN37Lf_qpPHhzG-2CzL572eMVArcqu7UhND2XOuDkHY1SVtHFOpa7fs5GLpcT-Kj2J6el0u6rmMj1WqAJoNgb-r4HpYwjYGiJ-QYO4IGjy8rL3stdjdC4JfmA_LdbFefgZpWS8hV9r3kNWicr4sqMDXCequkTuLkUxT-ekQMD72Z4FT5K3qSR3h8n3aG4SQU3Xd7WIXsEbmqEhAtPGiKsObQjryqxwqB7y2mjG_VPDJti268fP94LUyuwp1oQdVBx2YuGj9jIUFMcRKX76KFIWM29rL4FZ-rcBY76u-z7Ung.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
👈
گزارش عجیب رکنا از دعوای دختر و پسر تهرانی: دختر گوش دوست پسرش را گاز می گیرد و بخشی از آن را جدا می کند سپس وی را به بیمارستان می رساند
✅
@AloNews</div>
<div class="tg-footer">👁️ 44.7K · <a href="https://t.me/alonews/142297" target="_blank">📅 21:15 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142296">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a0b06591ce.mp4?token=Sv18o77O73hzrJcppKMtRSoUT_-H-b_sgTyoLq-QHJmNFKyPoo70fRbOO__h5jORB5rw3n1sXdgs1Je-DkPpSQ-fOR7v26JVJjJoJhb4zVv_8ueZjPFTvrYywEYXbMei7i73zNqGg9fs1Kx_zXktZ0r5dZt15PdQP--pwdf2gY2xVmUmgbHfscwwJs1WApfzqtn6EE3ob6PWqmteSInA1OkugWcAX32mfn17fmKTLnv64nsmy29E-mMjsDOztitCFW-Uy6cVjnD96DvhTrcz7b2XmOkEy_72Y3fSHSMGEkhIlZOJYJfVxI1EpBQfYg00XjCEyMIdFEujqHEfnibwuw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a0b06591ce.mp4?token=Sv18o77O73hzrJcppKMtRSoUT_-H-b_sgTyoLq-QHJmNFKyPoo70fRbOO__h5jORB5rw3n1sXdgs1Je-DkPpSQ-fOR7v26JVJjJoJhb4zVv_8ueZjPFTvrYywEYXbMei7i73zNqGg9fs1Kx_zXktZ0r5dZt15PdQP--pwdf2gY2xVmUmgbHfscwwJs1WApfzqtn6EE3ob6PWqmteSInA1OkugWcAX32mfn17fmKTLnv64nsmy29E-mMjsDOztitCFW-Uy6cVjnD96DvhTrcz7b2XmOkEy_72Y3fSHSMGEkhIlZOJYJfVxI1EpBQfYg00XjCEyMIdFEujqHEfnibwuw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
سی‌ان‌ان تصاویری از یک سامانه پاتریوت اوکراینی در نزدیکی کی‌یف منتشر کرده که فاقد موشک رهگیر است.
🔴
خدمه این سامانه می‌گویند کمبود مهمات باعث شده حدود ۱۰ هفته نتوانند هیچ هدفی را درگیر کنند؛ تصویری روشن از فشاری که کاهش ذخایر موشکی بر پدافند هوایی اوکراین وارد کرده است.
🔴
سامانه هست، خدمه هست؛ اما بدون موشک، پدافند فقط یک سکوی خالی است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 43.3K · <a href="https://t.me/alonews/142296" target="_blank">📅 21:10 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142295">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">👈
ستاد فرماندهی مرکزی ایالات متحده (سنتکام) : از زمان از سرگیری محاصره دریایی ایران، ۶۴ کشتی تجاری را منحرف و ۳ کشتی را از کار انداخته‌ایم
✅
@AloNews</div>
<div class="tg-footer">👁️ 42.3K · <a href="https://t.me/alonews/142295" target="_blank">📅 21:05 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142294">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TE2gDa5qK9quXD-M5Lnx8HbNwYcazRjJISn0jnCnIx2hPQnH_aIe1DZ1OoCkyRj9heyfTeWg0VSj-mGbdj_bjR7VzySa8-GqgiSGM6FaevxOAa2Dy-zmVYQoAviKB44Zo8DSH8A7F6ggyne5_McVPS-exdV7VZkLuu2O1Z7ei_EcjlfoXrrNpeSgC4p0OOh-xbDEjBRYIXZTdNviZFd-uA4-UTCBnvrtxZI5J_0B0uWHwMuwWijeWP2Se_-IWjx8Gv8P5F7Mb0rj0MI1D9gc1L_898K1-sGEt8tpBzspit9dj8d483tD9mLS4l9_34dgDl3zJzmewuh8fBIAJaQHpg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
👈
نفت برنت ۹۰ دلاری شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 45K · <a href="https://t.me/alonews/142294" target="_blank">📅 21:02 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142293">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NSwuRg9wE1bxDWq4B1foOyjWNbLTBF-lCCmv8b8Lss1QGBelxRkGbXF39DbRxcbYmfeIyKoiyktc45xxElUz3G2GTWIH3SEhg9a9m7khhPgfkCAf_3iCx7L8bhwiB3YmXujfUE6teXBpUc3jUFcJwqDvuzQn1g4skj-SQH-gX-DXRmB4KM2PC0lKeKflnwpd5dN3IG8Pmf6U2yZEJvEqK73c6m7AktIGdj_cSBZnoX9b0w79uVgE0JPFhJwyz2pmJVKcAPJJDOZzfkkDdE0ufTdlySZLCsXwsMnDTIGuITp5vM0R9s_WtjxmbEV_zx1_Sc8VhuKrNa5ZPj4T5AG7VQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
دیدار عبدالناصر همتی، رئیس کل بانک مرکزی با علی الزیدی، نخست‌وزیر عراق
✅
@AloNews</div>
<div class="tg-footer">👁️ 44.1K · <a href="https://t.me/alonews/142293" target="_blank">📅 20:59 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142292">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">👈
سی‌بی‌اس: کاهش تردد کشتی‌ها در تنگه هرمز؛ ناامنی همچنان ادامه دارد
🔴
بر اساس داده‌های ترافیک دریایی، تعداد عبور کشتی‌ها از این آبراه راهبردی ۱۹.۵ درصد کاهش یافته و از اوج ۱۹ مورد در ۱۱ اوت به تنها ۳ مورد در ۱۶ اوت رسیده است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 44.5K · <a href="https://t.me/alonews/142292" target="_blank">📅 20:55 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142291">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">👈
فایننشال تایمز به نقل از یک مقام اسرائیلی: اختلافاتی بین اسرائیل و آمریکا در مورد احتمال خلع سلاح حماس وجود دارد.
🔴
اسرائیل شک دارد که حماس سلاح‌های خود را تحویل دهد، در حالی که آمریکایی‌ها معتقدند این امر امکان‌پذیر است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 44.8K · <a href="https://t.me/alonews/142291" target="_blank">📅 20:50 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142290">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e7ddb0267e.mp4?token=HlopafOqoTsRrFrPUhJyeY1v60dgpAs_W7pAE2BbdhgTeZ9WZQUJfxWDfEfEvmFwsOBrzVN9x7ZG8OAnOXq6QlY174dRCtFi6dWIb1Z2fjLQBDomfxppcv3Gnhlo8unbzl3IIDHAwPKuURR1g-riSFTeGwMlMg6VdpKnOPU9EYrnFqJjPx-x00vdYS1kV9Xs9BE4vHvCQ0AlJXcZPCl6n0GrRVs0DjC-wE0337J5rtAlxSc9qwNf_77oCgPTbfB6E_fODSgOAemUH3dpmVqVEgULhSwRCrdlhyuG_07vGSk0fVCOV7qPJ7MnjH2EIvoxxuDzsdZyF_4QYKNQO3MVQw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e7ddb0267e.mp4?token=HlopafOqoTsRrFrPUhJyeY1v60dgpAs_W7pAE2BbdhgTeZ9WZQUJfxWDfEfEvmFwsOBrzVN9x7ZG8OAnOXq6QlY174dRCtFi6dWIb1Z2fjLQBDomfxppcv3Gnhlo8unbzl3IIDHAwPKuURR1g-riSFTeGwMlMg6VdpKnOPU9EYrnFqJjPx-x00vdYS1kV9Xs9BE4vHvCQ0AlJXcZPCl6n0GrRVs0DjC-wE0337J5rtAlxSc9qwNf_77oCgPTbfB6E_fODSgOAemUH3dpmVqVEgULhSwRCrdlhyuG_07vGSk0fVCOV7qPJ7MnjH2EIvoxxuDzsdZyF_4QYKNQO3MVQw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
آتیش سوزی شدید، میدان شهرداری گرگان، تا کنون بیش از ۱۰ مغازه در آتش سوخته اند
✅
@AloNews</div>
<div class="tg-footer">👁️ 46.9K · <a href="https://t.me/alonews/142290" target="_blank">📅 20:41 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142289">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EBXxcnjbPoJWrQluGiE9lzx5fyp4XKQCs5FqtOva5Wdiwq1vDYRwimkeszK1_B1-YaeFsvMRtziKsoTvYwcRR0NeWUDuO7kpt5uHu64FNG_I3dqasdSkmG-qG7hxeCAMI9lhgG5XBkYRmHAv2ocWgsFZPeDeC5C4uZwl9dxFQbXmWvfoNhDWz-oL1IuW2RE9wdHpewDfCs8tqGrVku6MxFng4fM104dh_4RgMRlIqxjxqp6l6nt7Qc-gr1yH_tO64QdoUwmSDi3_mMim1fmYh4cmcp8qgp7XPqL-oiY8bkBGwafBYJSyRhm4LqM8HxkjFtR2zroZkaO8WXxRVNIoTw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
یاشار سلطانی: ‏هشدار می‌دهم ‏نفتی را که قرار بود بر سر سفره مردم باشد، وارد بازی کثیف چند دلال⁩ دزد و چند جوجه اطلاعاتی⁩ نکنید و الا همه چیز رو افشا میکنم تا مردم بدونن چجوری دارید بیت المال رو غارت میکنید
🔴
دوران پنهان‌شدن پشت عنوان‌های امنیتی و محرمانه‌سازی فساد باید تمام شود.
✅
@AloNews</div>
<div class="tg-footer">👁️ 49.1K · <a href="https://t.me/alonews/142289" target="_blank">📅 20:35 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142288">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">👈
ذخیره نفت استراتژیک آمریکا طی هفته گذشته ۵.۳ میلیون بشکه کاهش پیدا کرده!
✅
@AloNews</div>
<div class="tg-footer">👁️ 45.6K · <a href="https://t.me/alonews/142288" target="_blank">📅 20:28 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142286">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">👈
پزشکیان: اینکه کنار گود باشیم و فقط درباره مسائل حرف بزنیم، کافی نیست
🔴
ایران برای تمام مردم ایران است و به گروه یا جناح خاصی تعلق ندارد
✅
@AloNews</div>
<div class="tg-footer">👁️ 48.3K · <a href="https://t.me/alonews/142286" target="_blank">📅 20:24 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142285">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">👈
الجزیره: رفت‌وآمد کشتی‌ها از تنگه هرمز برای سومین روز متوالی به پایین‌ترین سطح خود کاهش یافته
🔴
روز شنبه تنها ۳ کشتی، روز یکشنبه ۲ کشتی و امروز دوشنبه ۱۷ اوت نیز ۴ کشتی از تنگه عبور کرده‌اند
✅
@AloNews</div>
<div class="tg-footer">👁️ 47.9K · <a href="https://t.me/alonews/142285" target="_blank">📅 20:22 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142284">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/17f4b01950.mp4?token=ScGeHhgb19vejyJn69e-irh5_9sJhkBGe2ioknp86urNbT-XSvdJg9q2uAFou3cmsv8I_65IHPJOjEM30Rzs7zzzJbYW1DD36m1gezxjKsYjTs9r3mlbyVxHUi2u2QbUSzDgeleLaxVCGpNkPxzukG-X9exIotGK9aVcRIoqLiGJYU8oRMNCuetZW9I4a4F7u3hmY7XBHEeV6ayMd-pvD5RJk9xbeOnmnR1MCCnWQ6SzbhsXJt7MXgNKtZsEPKcB79bB7FdnEwuaJxee_FxpgIr2IhbHYoJxi_Vd60kY0lKNJL46ojeC2vNdtXAXqiMLYQcys8rUlQaGayeIbIGhIg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/17f4b01950.mp4?token=ScGeHhgb19vejyJn69e-irh5_9sJhkBGe2ioknp86urNbT-XSvdJg9q2uAFou3cmsv8I_65IHPJOjEM30Rzs7zzzJbYW1DD36m1gezxjKsYjTs9r3mlbyVxHUi2u2QbUSzDgeleLaxVCGpNkPxzukG-X9exIotGK9aVcRIoqLiGJYU8oRMNCuetZW9I4a4F7u3hmY7XBHEeV6ayMd-pvD5RJk9xbeOnmnR1MCCnWQ6SzbhsXJt7MXgNKtZsEPKcB79bB7FdnEwuaJxee_FxpgIr2IhbHYoJxi_Vd60kY0lKNJL46ojeC2vNdtXAXqiMLYQcys8rUlQaGayeIbIGhIg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
وزیر دفاع سابق اوکراین فدرورف:
مرحله بعدی این جنگ، ربات‌ها و پهپادهایی خواهد بود که با ربات‌ها و پهپادهای خودمختار دیگر می‌جنگند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 46.5K · <a href="https://t.me/alonews/142284" target="_blank">📅 20:18 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142283">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">👈
روزنامه دیلی میل به نقل از منابعی نوشت بانوی اول آمریکا نگران است که ایران، رئیس‌جمهور ایالات متحده را ترور کند و این مسئله موجب ترس همسر رئیس‌جمهور شده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 45.3K · <a href="https://t.me/alonews/142283" target="_blank">📅 20:12 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142282">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kXFfku5bJTGhmzs7FVvvB_h3cMlxwhfTC6kcVDsZLU6RnAbG9iVSEI-QyPS5vzijuKAOBVWLZPUa7KXKdOCU9vXStsmYozXi0eXM3V0E3G44PlWytI_3dpQ0FxIcRFy_z4ixFyGfXXXsHPiTFnvF9kygJ5rul8ixzrZZyY0PsjbWzu-AJNBkUXoTaaerKCiRvdv5nLhjs7408Wc79ltN-in53dtW-6VgMu7nU2hX0p3GcyvUs7cyGCxmaBtM7yb9Cs67XBbBsEwuvHvly2-gan9raxLVrnsU-DrH9b8KKvyAQBY3eILhMRVO1PO7DcJU2wvZ84wL4RG6vkt6UYmcdw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
تلگراف: روسیه دست‌کم ۱۰ پایگاه پهپادی با ۵۹ ریل پرتاب  نزدیک بخش شرقی ناتو ساخته یا گسترش داده است.
🔴
سرویس اطلاعاتی آمریکا ارزیابی کرده است که روسیه ممکن است با یک حمله محدود، این ائتلاف را آزمایش کند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 46.4K · <a href="https://t.me/alonews/142282" target="_blank">📅 20:05 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142281">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">👈
یدیعوت آحارانوت به نقل از یک مقام اسرائیلی: ما در دیدار با کوشنر تأکید کردیم که هیچ چیزی را که زمینه ساز تأسیس کشور فلسطین باشد، ارائه نخواهیم داد.
🔴
نتانیاهو از دیدار کوشنر با رهبری حماس انتقاد کرد زیرا آنها معمار هفتم اکتبر بودند و کوشنر پاسخی نداد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 45.4K · <a href="https://t.me/alonews/142281" target="_blank">📅 20:01 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142280">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6c492661c3.mp4?token=vOQ9Va1Hc7ktXsI3-FD022bikj894XEM6ILsMjs08BZhJWr-3icE8x-StgveepSYcUHez4DbtJqSUS8vMdY3OV7L6YcooAncUci8LYEEb5zK6WRSWwSLpwmQmkPOUnoLME4rCSf1xxD1EhVEc3uupBd-TUbE31TKb84eQNjnY8FcTUT_zXYcsB5Dfb3dPkqHchHg8xu1G0-5GlWzn7J73F9Xwk8lBnsBIDlyto9Qb5ADnK3bUuZrPrerz3WBiOtX2rXgzlWD0MCwXmoimE1qFiXeHbqFqsTp1uRRc36yjGzt2PKUX4mtg5AC2iiffk65ep4sKnv2-r1wMrmO4SO5t4i-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6c492661c3.mp4?token=vOQ9Va1Hc7ktXsI3-FD022bikj894XEM6ILsMjs08BZhJWr-3icE8x-StgveepSYcUHez4DbtJqSUS8vMdY3OV7L6YcooAncUci8LYEEb5zK6WRSWwSLpwmQmkPOUnoLME4rCSf1xxD1EhVEc3uupBd-TUbE31TKb84eQNjnY8FcTUT_zXYcsB5Dfb3dPkqHchHg8xu1G0-5GlWzn7J73F9Xwk8lBnsBIDlyto9Qb5ADnK3bUuZrPrerz3WBiOtX2rXgzlWD0MCwXmoimE1qFiXeHbqFqsTp1uRRc36yjGzt2PKUX4mtg5AC2iiffk65ep4sKnv2-r1wMrmO4SO5t4i-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
بنیامین نتانیاهو نخست وزیر اسرائیل: به رای دادن در انتخابات مقدماتی لیکود بروید و تیمی پیروز انتخاب کنید!
✅
@AloNews</div>
<div class="tg-footer">👁️ 45.8K · <a href="https://t.me/alonews/142280" target="_blank">📅 19:55 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142276">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/X882H5LGzRq5IG-SiVnxvTj0vtibRNQjqOLWwYiAK9hVV1mXyD-b9llo8g0kV31P71_oyYAklVgZSaFP6XNivraQ5ar82gnMeoxnWHnEvDXNvRxGn11b-b3vvN2A6eRzcCS2oXmaCXE41tXz7eH8Gs2xtM6ypcKIZzUjxQAoejL8EvsaN1nHOW_dA6ls0q1ooq5VgGG8CvmjaGoZj1Wb8y7EeEYEdSjeeN6iFTjPuRPQxLZpmslNiUk7aup5Ja3ZNymDJDaOIyK4IglT6pa41ELCuBUkd5G_xMobsBBdmHLsDEOsxDfyLGQ8CFDAxPidzUVoOayu4xgiJ9T9i1kjHw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/nQF7-2OlEJa-JCuOHYgV53aZ8SO9JeEA1ALO7BgcZgUzrA77r7fUcVzK8AtwPuVc2-YPWCnJa2faWjTEnVu24rl8fOPlYX3I3YP6Ol90PNuSjCaw4Ura4qHOap1vGqSSieKaE3kC7zgzOM7wAsiY2qMevyiTiwaM1GuzDY6RooHa9LAkiIrXPbBZCDJalwSODqpsybr2AnQ5a898cNembzFgEvIUyYJnjgONwXfA6Vu51xSIDMFM1fUnBqERmMbwVp3mG_6gfl5Tsiu70iGG5MFlStrRMQQ83nZGK5-DSI0b-43vLTa7HkTlG_jgdCK2YoejXr02GsrZDuPX0e0xog.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/G7piSbMCUsUc9p8Dvi7g5zzvmmPRzLG3Vcebr4492M8OyhRHpq_aGSGEipP9nvz2qiIcllrT87mSHLYIbIOD3dl9T2Chtiy-Mqv4JocNkkTSdXJcm4rkoOo9RzGbvoydcocMfTCQVUR_S0oB0Ai0CIR2P_mTewWTDAHLwLRi_icacgVv5J-RswpLz8GfTnoZhHYWvimDuAyXdgXwg9BBdqzVav57Vfwg3XyWJzaeJpmmANTvVYWbZBG3TXgcOL-6197SI4cE0EYhoKlt_vHlW2dwPzgK4d4GrZkuM0otHv-H2MsPQLu0BmAfkV1v5iAKW-9MDtWYd8ruT3I2hVKB_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/IlXj6ECpN2x1RunH2RzmntEWgO-YNY5FygQNdDTmeq1l4klAaDX6v29nOPg4HYTQGLeqf4y9l3Y0GWL_u2kFZVY-MUAXzgoQq49gZZSLP3eFWRLIe75dq3AXCCr7UPBSfiAJj_87uipgoSZk_sTNmN6jnOJTQZ5K621pypeAY_enfI7PkjZP-qCw3CNTGgTi0WlZSn31jcnwJZIN3RUgsguhavS2XInqPGqFWyegMOR52KFBmMXjDlqI0LhT_dxr1JTCyAnqke6cZpAp8FgkrVxOb1Le9zNh4skbcDilZMLIf55zy5VvEOy8byE_OdGfFOmsoDwVDnIQYiy3no6Kcg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
ساعاتی پیش، جنگنده‌های نیروی هوایی اسرائیل به المنصوری در جنوب لبنان حمله کردند
✅
@AloNews</div>
<div class="tg-footer">👁️ 46K · <a href="https://t.me/alonews/142276" target="_blank">📅 19:47 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142275">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BCkSVpdR_yQp0_Cys46LFrmdxPVnhY6S7M7FjrQRgDIYYfg6sNzvyanqdyYzDQPQTfsjn1URK_b8cDza62S9zTzx25ADsZTfv0To8KrcWWCySNi1q1Py3m0LqegFm5jdLk_DV1eR8GP1Pjxz4Ti5BW4fUEicMaLyzJhYnDzMpIQ4jZAxUsC4_jTVCk6Qv3N32oXQyMqmrTOEnaoeVJwNc58FEDzQ-E_mrFD1ChJEOy1znwXsJeAiWN9x-kIW22gQ8_W-qlXf0S2REreb_BOGxEyLV42vWbyr1NVxxsFGyIhwlng-qcGYeo3PpJPgJOMZ3rrMwtm4PVIVSlBMBACafQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ابراهیم رضایی، عضو کمیسیون امنیت ملی مجلس: ترامپ باز هم حرف از تسلیم ایران زده است. ایران بزرگ تسلیم‌شدنی نیست، کسی باید تسلیم شود که با ماشین غذا و با خفت و خواری فرار می‌کند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 43.5K · <a href="https://t.me/alonews/142275" target="_blank">📅 19:44 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142274">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/72764905ee.mp4?token=IgVBlkWCWmEXgDN4dCALjXxyif7Mq-7d6X7xpo2Z9ly4jfpAvwuHG6IIN2lL0g7Cab0x486PAxbw6xvcjAGxyysy2QoHRcNARMmZihoscWiLVyn44miJE1v5F_wjHTVEHlHgQSDj4TERvs074DCpbe4K9uR01cSrcdKKiNY-P9GQ368zxwDGuyYpH1w2qYPvhuc341Wz_RGWRYDjSt4JrgPE4qgMI1H1vZF3sNIWM7O5O2oDyesNCnwBb8q_uT5eJ5ot5VqzqtQSpamXNEumMWwkGQ2prqUNOEdbFjXRuh_bCWauWCb6B5Hk0WZUZly7d5FjY6hwrbwTL0A1iPL-cQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/72764905ee.mp4?token=IgVBlkWCWmEXgDN4dCALjXxyif7Mq-7d6X7xpo2Z9ly4jfpAvwuHG6IIN2lL0g7Cab0x486PAxbw6xvcjAGxyysy2QoHRcNARMmZihoscWiLVyn44miJE1v5F_wjHTVEHlHgQSDj4TERvs074DCpbe4K9uR01cSrcdKKiNY-P9GQ368zxwDGuyYpH1w2qYPvhuc341Wz_RGWRYDjSt4JrgPE4qgMI1H1vZF3sNIWM7O5O2oDyesNCnwBb8q_uT5eJ5ot5VqzqtQSpamXNEumMWwkGQ2prqUNOEdbFjXRuh_bCWauWCb6B5Hk0WZUZly7d5FjY6hwrbwTL0A1iPL-cQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
بالن جاسوسی آمریکا مجدد در آسمان استان اربیل عراق
✅
@AloNews</div>
<div class="tg-footer">👁️ 44.6K · <a href="https://t.me/alonews/142274" target="_blank">📅 19:41 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142273">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">👈
داده‌های ناوبری دریایی نشان می‌دهد که یک نفتکش متعلق به یک شرکت اماراتی هنگام عبور از تنگه هرمز، متوقف شده است.
🔴
طبق ترتیبات ایران برای عبور امن از تنگۀ هرمز، مسیر ایرانی یکی از شروط است و پرداخت‌بهای خدمات و اجازۀ ایران از دیگر شروطی است که نفتکش‌ها باید رعایت کنند.
🔴
نفتکش امارات در نزدیکی قشم متوقف شده است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 43.4K · <a href="https://t.me/alonews/142273" target="_blank">📅 19:37 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142272">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">👈
بن گویر، وزیر امنیت داخلی اسرائیل: ما هر شب باید حداقل ۳۰-۴۰ تا ترور هدفمند در غزه انجام دهیم. نه فقط اونایی که برای ما خطر دارند، بلکه اونایی که ارزش زندگی کردن رو ندارند!
✅
@AloNews</div>
<div class="tg-footer">👁️ 44.5K · <a href="https://t.me/alonews/142272" target="_blank">📅 19:35 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142271">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/foCQp7RMbgoWdlcr2JyLvyXcYN1K0ViqtChNfUmFUzhkx6i0rIeRw8q2n1fqvMFxt7unLaRPWfjctOdMFgBvyW8XdBT197gqIYqu4-ZWG8-TWjHUIr8enP6f9ILzKGUD-XP9OYHbXcmMHEQ7NX0_KHx1ct0hWn4AScbCgMQAmnoPTA6Mpk0jiK8tUrzI1gXEVvQAJCehgNGyZ-ItnJspuTkMFRxXulasDN7OPVSOjinAvd9C-RiT5pHSe3PkxXoEIABtZd_Wx_0K4In9csmEHc073Tm0X3BXgdm_bn4mifAW3-CxfyOHGUXSMhrMd7Ckc8OeoGIlzznAn9BAMNL-2Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
بن گویر، وزیر امنیت داخلی اسرائیل: ما هر شب باید حداقل ۳۰-۴۰ تا ترور هدفمند در غزه انجام دهیم. نه فقط اونایی که برای ما خطر دارند، بلکه اونایی که ارزش زندگی کردن رو ندارند!
✅
@AloNews</div>
<div class="tg-footer">👁️ 45.9K · <a href="https://t.me/alonews/142271" target="_blank">📅 19:29 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142270">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">👈
سی‌ان‌ان: کوشنر بیش از چهار ساعت نتانیاهو را تحت فشار قرار داد تا طرح آتش‌بس ترامپ برای غزه را پیش ببرد
🔴
نتانیاهو در برابر این فشار مقاومت کرد و با اشاره به انتخابات اکتبر، تأکید کرد که پیش از هرگونه عقب‌نشینی اسرائیل، حماس باید به‌طور کامل خلع سلاح شود.
✅
@AloNews</div>
<div class="tg-footer">👁️ 44.8K · <a href="https://t.me/alonews/142270" target="_blank">📅 19:24 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142269">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4c96f732b1.mp4?token=tE0pcG2EhK-pyWQu1cRN7H9yjaLRfqYZPjpMyZKf8pqr2VUS8T1I5vQFq8NYSjqcQ6-cwTtYykRZc43HNUP2IJUwyvsUAyJSPpNCuHtEGE4Nz32_L58cAQ8EqqypkIOqAUpWdWUMAA3GDKyzBS0fvbrALLUy66yas0KS51cEq1AB1EJF0_Y9pMAyUv01Qr5aYTs1xed0xzca_Wcke-21fAUmrf7m9QsVnfvUFUKxMXnE2GAVIiNrNKBo4OWkSXKk_K2sFkV2Yp1mXTdt1bWyQt3c0poagpP7wjgVoi6Mk_cUun4jvzUjIAPbr9BsXx-gZSrF5ESHe9Nt4uhfCD_kVA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4c96f732b1.mp4?token=tE0pcG2EhK-pyWQu1cRN7H9yjaLRfqYZPjpMyZKf8pqr2VUS8T1I5vQFq8NYSjqcQ6-cwTtYykRZc43HNUP2IJUwyvsUAyJSPpNCuHtEGE4Nz32_L58cAQ8EqqypkIOqAUpWdWUMAA3GDKyzBS0fvbrALLUy66yas0KS51cEq1AB1EJF0_Y9pMAyUv01Qr5aYTs1xed0xzca_Wcke-21fAUmrf7m9QsVnfvUFUKxMXnE2GAVIiNrNKBo4OWkSXKk_K2sFkV2Yp1mXTdt1bWyQt3c0poagpP7wjgVoi6Mk_cUun4jvzUjIAPbr9BsXx-gZSrF5ESHe9Nt4uhfCD_kVA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
مقام‌های محلی در ایالت اوکلاهمای آمریکا پس از وقوع آتش‌سوزی گسترده در یک مخزن گاز طبیعی، دستور تخلیه ساکنان اطراف محل حادثه در شهر گلن‌پول را صادر کردند
✅
@AloNews</div>
<div class="tg-footer">👁️ 46.5K · <a href="https://t.me/alonews/142269" target="_blank">📅 19:18 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142268">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">👈
وزارت نیروی: 4200 مگاوات برق را در نتیجه جنگ از دست دادیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 45.6K · <a href="https://t.me/alonews/142268" target="_blank">📅 19:12 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142267">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">👈
المیادین به نقل از یک منبع بلندپایه ایرانی: حادثه‌ای که امروز در اربیل، در اقلیم کردستان عراق، رخ داد، نمونه دیگری از عملیات «پرچم دروغین» است.
🔴
ایران هیچ ارتباطی با حادثه‌ای که در اربیل رخ داد ندارد و عملیات‌های ایران به‌طور رسمی و صریح اعلام می‌شوند.
🔴
هرکس به حاکمیت ایران احترام بگذارد، از احترام ایران نیز برخوردار خواهد بود.
✅
@AloNews</div>
<div class="tg-footer">👁️ 47.2K · <a href="https://t.me/alonews/142267" target="_blank">📅 19:08 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142266">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">👈
سی‌ان‌ان به نقل از یک مقام اسرائیلی:
نتانیاهو و کوشنر توافق کردند که یک ژنرال آمریکایی بر روند خلع سلاح حماس نظارت کند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 45.9K · <a href="https://t.me/alonews/142266" target="_blank">📅 19:06 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142265">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">👈
یک مقام دولتی پاکستان در اظهاراتی به «ام‌اس ناو» مدعی شد که مذاکرات برای بازگشایی تنگه هرمز و پایان مسالمت‌آمیز جنگ ایران و آمریکا همچنان ادامه دارد
✅
@AloNews</div>
<div class="tg-footer">👁️ 46.3K · <a href="https://t.me/alonews/142265" target="_blank">📅 19:03 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142264">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0512c8ba1b.mp4?token=g1rOb43XcgdH9XDY2fxc1hd-_rAUrINnD96GA6Iokp41SVLfbu9HpsvIhv7LIgN5bVmQfXaFxNTjKZ2u_y3oaJYHS0BB3Hgev1DY7V_vuTVxQOOCCt_r_NCb0hrMZmYJu_qAyzP0s-S3vwjK_4NXf4QsppliLYPbFo0gYQnUZFZ-7dA8uyxVz_0vsbSv0ohuDYEZr3qzoXGzIZgSxY5qbGPP3yrNu5rC3eKziiqVb_CkBpvG8njh54J1Md-NsfJ5fxnpkprlr8A-2kUOrQm8c8I_RVtwhGvBX4OSJabGZM7AazItdkkVM8pkxSc9GBDL9TjLvC-l-KuVWnE-zwsW_w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0512c8ba1b.mp4?token=g1rOb43XcgdH9XDY2fxc1hd-_rAUrINnD96GA6Iokp41SVLfbu9HpsvIhv7LIgN5bVmQfXaFxNTjKZ2u_y3oaJYHS0BB3Hgev1DY7V_vuTVxQOOCCt_r_NCb0hrMZmYJu_qAyzP0s-S3vwjK_4NXf4QsppliLYPbFo0gYQnUZFZ-7dA8uyxVz_0vsbSv0ohuDYEZr3qzoXGzIZgSxY5qbGPP3yrNu5rC3eKziiqVb_CkBpvG8njh54J1Md-NsfJ5fxnpkprlr8A-2kUOrQm8c8I_RVtwhGvBX4OSJabGZM7AazItdkkVM8pkxSc9GBDL9TjLvC-l-KuVWnE-zwsW_w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
مجری صدا و سیما فاش کرد: قطعا ۴ اسیر هم در کویت داریم
✅
@AloNews</div>
<div class="tg-footer">👁️ 47.3K · <a href="https://t.me/alonews/142264" target="_blank">📅 18:59 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142263">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">👈
یک حمله بمبی به یک مدرسه خصوصی در کابل انجام شد که منجر به تلفات ناشناخته‌ای در میان دانش‌آموزان شد.
🔴
مدرسه مورد هدف در منطقه‌ای واقع شده که عمدتاً توسط جامعه هزاره، که عمدتاً شیعه مسلمان هستند، مسکونی است.
🔴
هیچ گروهی مسئولیت این حمله را بر عهده نگرفته است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 44.8K · <a href="https://t.me/alonews/142263" target="_blank">📅 18:55 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142262">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">👈
داده‌های شرکت ردیابی نفتکش‌های «کپلر» نشان داد که عربستان سعودی در پی افزایش ناامنی‌ها، ارسال محموله‌های نفتی خود از مسیر تنگه استراتژیک باب‌المندب را موقتاً متوقف کرده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 43.7K · <a href="https://t.me/alonews/142262" target="_blank">📅 18:52 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142261">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">👈
یکی از ممبرا پیام داده گفته پارسال به بچم گفتم پول چیپس‌هات رو بریز قلک سال بعد پول زیادی جمع کنی اونم پول ۵۰تا چیپس رو ریخت تو قلک و دیشب باز کرد و الان پول ۵تا چیپس داره
✅
@AloNews</div>
<div class="tg-footer">👁️ 45.7K · <a href="https://t.me/alonews/142261" target="_blank">📅 18:51 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142260">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GVDepP_lsYawjZYKagTJ1dgTCJA1oxO6ufKi7xRg_OMZGvKUz79l021P08SQ_NQhjcTKTfDZTL49T4H3bOr_twsnk8LIMfrQz6EsCmUAK51RicJaX_h4z9E4M7PFSuddr_tp65TKMFVTzh0snAMgiFusQMfvFf6b0CobtEpSW9b_3arOv-kQZ8B8gMpeDxtOK4JGX2H2JYhXWP-5CyIuPJypXeEZiAWYI55I4hI2RFps_1_7ywWttl5qMfB3R73jk2Ch3YHP8kpPiD9LzBsfSlFaB2LvLKDpOLw4zCqVu-di6MEwMyrz48TnnVW_tD5mR710sZbImOFj3846HNKgeQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
دفتر نخست‌وزیر اسرائیل: نخست‌وزیر و هیئت صلح گفت‌وگوهای عمیق و سازنده‌ای داشتند.
🔴
توافق شد که دو گروه کاری تشکیل شود؛ یکی در زمینه خلع سلاح و غیرنظامی‌سازی غزه که هم اسرائیل و هم هیئت صلح مصمم هستند این کار سریع انجام شود و پیش از هرگونه بازسازی در غزه به پایان برسد.
🔴
گروه کاری دوم بر بهداشت، آب سالم و سایر مسائل بهداشت عمومی برای مردم غزه تمرکز خواهد کرد که این مسائل همچنین بر مردم اسرائیل نیز تأثیر می‌گذارند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 47.1K · <a href="https://t.me/alonews/142260" target="_blank">📅 18:47 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142259">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fhUa1x1FQhEYxfdeTCBI17AzEQtw9tgjs2KHxap5yjiy5s1gJX9qOrZ2V07w7nFQc3oWf_Kdpl87q9wrjtayozScTW9nuoCAmhmqkauFoAlcU_pnxAMK2DbUsgzuvUIPExMF_FZCeRONNpw7SuaUUEg5Kj87JkNX8141mgk64c0D1p6a1HaCEN6UVOyja1vj01WKzlFi7a9ZtXdQsIzFv8VVU1gJpCUHfVCU26bWW3N0yLALBk9Htt7GfaClpRObBbMVq0JxH0A4-GvAVYa1c2Q_MPbVCAOTQIitTY5obHqKspgfpJ8Z8Jwl6fkEyF5fi5QvvqDbb-Yekozgwt9YRA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
د
رخواست صلح از طرف پاپ!
🔴
‌بار دیگر درخواست خود را برای پایان دادن به خشونت‌های جاری علیه غیرنظامیان فلسطینی در کرانه باختری تکرار می‌کنم و فوراً از جامعه جهانی می‌خواهم برای پیشبرد راه‌حل دو کشوری و دستیابی به صلحی عادلانه و پایدار تلاش کند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 44.9K · <a href="https://t.me/alonews/142259" target="_blank">📅 18:44 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142258">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lhFpWBcX5-gSyUhPZ9ToclqFrrL0Su7v7OC4wgpZb7joeqBYof5zW86IKCHVI28uUNve2YvSpU5Wv7i-E1FGDEvsYU2M7OToGQjFdB_hMGlWhvYhcCLfL62Vm47R89ziuxspf-qQ2OR3gioEuMmG9xcIyK0xWFzwtFc2OgyYBoKcYuuPU-ezr3a0MRLGvIuzkurnakXBgnXTmEHfpj1K-eYebz9-K1tKSkCGtzCAuvbPBeXgF0O7kowoKuN4aOD5YJoUBBM3MiF_wnY2Qv4CKT5RYZpS7mzItrtqB0YCUgk6bMC6VPvU4IjKm79lkogUXYtEPAaXFIc2clfzGWdRrg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
شرکت ریتئون از گروه RTX قراردادی به ارزش ۲۲.۹ میلیارد دلار و به مدت هفت سال با نیروی دریایی ایالات متحده برای افزایش تولید موشک‌های کروز تامهاوک به بیش از ۱۰۰۰ موشک در سال به دست آورده است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 45.3K · <a href="https://t.me/alonews/142258" target="_blank">📅 18:38 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142257">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">👈
رئیس جمهوری لبنان: از برقراری روابط با ایران بر اساس «کشور با کشور» حمایت می‌کنیم.
✅
@AloNews</div>
<div class="tg-footer">👁️ 45.6K · <a href="https://t.me/alonews/142257" target="_blank">📅 18:33 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142256">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ffb511082b.mp4?token=YIpnaAe79r8BZAbgbNwYNw6L7ms1cB78rMmr0Z6-vK-Ko0W-iNKeaLXUH0zznkHR_FmWk8H8OJV1xz3CcNXl566xpVSVFNF_KBnitwZ6F4iE93NqDIdmCdt_4sGuW2Wv8NNrsVFTuK4hA-9v3kFETb4-BdNdv2ylhnuHqLuWZ8q0p3YKsJkr1ngf2-6FvvKDs9NK2dCp0t8dL-ogP7t0CCunjiqZp7Hrj6cgSFuQb6X1Mo6rX9LGro6IR49u7LgVP0BR9nRCv3S-Uo4njVl3SajrA9MjQVg2mcTbS_fF--gAgS9AlqF6Cc1-ol_4AG-Fb9ZfiqEm-RqGEpp150BmXw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ffb511082b.mp4?token=YIpnaAe79r8BZAbgbNwYNw6L7ms1cB78rMmr0Z6-vK-Ko0W-iNKeaLXUH0zznkHR_FmWk8H8OJV1xz3CcNXl566xpVSVFNF_KBnitwZ6F4iE93NqDIdmCdt_4sGuW2Wv8NNrsVFTuK4hA-9v3kFETb4-BdNdv2ylhnuHqLuWZ8q0p3YKsJkr1ngf2-6FvvKDs9NK2dCp0t8dL-ogP7t0CCunjiqZp7Hrj6cgSFuQb6X1Mo6rX9LGro6IR49u7LgVP0BR9nRCv3S-Uo4njVl3SajrA9MjQVg2mcTbS_fF--gAgS9AlqF6Cc1-ol_4AG-Fb9ZfiqEm-RqGEpp150BmXw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
مجری مشهور آمریکایی و از افراد نزدیک به ترامپ، صحبت از به کارگیری بمب اتم علیه ایران می‌کند
🔴
مارک لوین ایران را با امپراتوری ژاپن مقایسه می‌کند:
"رژیم ایران تسلیم نخواهد شد.
🔴
می‌دانید، ما قبلاً در جنگ‌هایی بوده‌ایم که با دشمنانی جنگیدیم که آنها هم تسلیم نمی‌شدند...
🔴
ژاپن را یادتان هست؟
متاسفانه، ما مجبور شدیم دو بمب اتمی بیندازیم تا آنها تسلیم شوند."
✅
@AloNews</div>
<div class="tg-footer">👁️ 48.9K · <a href="https://t.me/alonews/142256" target="_blank">📅 18:27 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142255">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nLtDOsQjBp-fYHYOmpVvSRNPIS1gTliWAcJ9TrBVXw_XqCHGyunbOlzOdXema3dtLytfMK2qgs5WjFLsGMti478tBt3mK-6K4ATVQMv3nk8m27Ph0ChmyRYXR2ny1_22VzypfEmM89URgXs4t3mMyZAjNUjXgbfmLy82mSK3YGsWk26P2OtZ3laD9LxsEyXITAv7W39C5IjYTscSF0gNYCYqP7oZbo-LiCoqw9UNaXROiiswolok0x5gGM3E34y-Wv4C_kwlzes3Oj7II1SetUe4QPbmp8VvJ8188z8jMh_uMugILGG76dAr_GueozQt-Vgzw7fyWcoDNcbdP0RMsQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
👈
۲۰۰ میلیارد دلار زیان در بازار سهام امریکا در معاملات ابتدای هفته
✅
@AloNews</div>
<div class="tg-footer">👁️ 46.5K · <a href="https://t.me/alonews/142255" target="_blank">📅 18:22 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142254">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">🚨
نمیخوام جو بدم یا ته دل کسی رو خالی کنم ولی این چنلو داشته باشید بدونید چ‌خبره :
@khabar
◀️</div>
<div class="tg-footer">👁️ 47.5K · <a href="https://t.me/alonews/142254" target="_blank">📅 18:18 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142253">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a545b29a7a.mp4?token=eO1-lwbdS6pzzbcW01NIdX9vseR6wE7RmnZp8nTJhhySD6ykzpDL0PuF4QDROh7DY1hvnOPCHL9SmwJ6yXuDVaF-ChmygRvo9awtGULkSn2Aj7qvEm3VjtkFrXgi9BP8tbQm9Sx4Roo53L1BT5uhyT4NXWctqA03nEqmav73KN0QOkKs72zVGkTzlY_mH3FkH5INqaSTJCx7A3PkY9OxqmTl7CZYEo0YtCp0qkN5LVpuowqM-3pnAW3Gr7QgOEMU8VzGemABXOvU7BjtETsAPgLqNb389lXyTZWvYV-MFtvJ6yP5yT78QlJ2r_7GIPxQcbR7rCLOJHmKH465X_JtuQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a545b29a7a.mp4?token=eO1-lwbdS6pzzbcW01NIdX9vseR6wE7RmnZp8nTJhhySD6ykzpDL0PuF4QDROh7DY1hvnOPCHL9SmwJ6yXuDVaF-ChmygRvo9awtGULkSn2Aj7qvEm3VjtkFrXgi9BP8tbQm9Sx4Roo53L1BT5uhyT4NXWctqA03nEqmav73KN0QOkKs72zVGkTzlY_mH3FkH5INqaSTJCx7A3PkY9OxqmTl7CZYEo0YtCp0qkN5LVpuowqM-3pnAW3Gr7QgOEMU8VzGemABXOvU7BjtETsAPgLqNb389lXyTZWvYV-MFtvJ6yP5yT78QlJ2r_7GIPxQcbR7rCLOJHmKH465X_JtuQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
رسایی
: «۹۰ میلیون ایرانی متهمند، مگر اینکه خلافش ثابت شود»
✅
@AloNews</div>
<div class="tg-footer">👁️ 50.1K · <a href="https://t.me/alonews/142253" target="_blank">📅 18:05 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142252">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">👈
اطلاعیه رادر کلودفلر:
ترافیک اینترنت بین الملل ایران از ۹۰ درصد به ۵۹ درصد رسیده ،وضعیت الان اینترنت ایران دقیقا مثل روزای قبل از قطعی ۸۸ روزه ی اینترنته و با اختلالات بسیار سنگین همراه شده.
✅
@AloNews</div>
<div class="tg-footer">👁️ 48.5K · <a href="https://t.me/alonews/142252" target="_blank">📅 18:01 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142251">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">👈
طی اتفاقی عجیب شهرداری الیگودرز لرستان، کف رودخونه رو آسفالت کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 49.4K · <a href="https://t.me/alonews/142251" target="_blank">📅 17:58 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142250">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/K0T5lQWekK2BR9Ogb0VXRrqF-u5e3nt2Qt46Sm0qM2HBg707DkNXe4NPH0zEl1lTh2yLmhBeGxxh3e8uY_tlOnOng6S_9ds4QL-s6ZRDaJ9L6hEfZpIXVs5JVsmtX583aalIcqqyGkvKmlvgX6VH_O3kK_H7ULITI7Gmp68ZSvzuVdQ4vxFvY_yQW61gRLgtn5B8aAbZJKn6zIz0o9jEw_PwloZQp15TfpBxMakzBsIbYuNizezdneTvgUlejOV_OzSlb0krJ7wylBde7iyu15n0GYZOy1on5YJTFgA413LJYjIIMhZqsfGB50EYWw9gTUVHN2ehpBZ9aTUZiY531A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
عوستاد رائفی پور:به ترامپ مشکوک هستم
✅
@AloNews</div>
<div class="tg-footer">👁️ 50.6K · <a href="https://t.me/alonews/142250" target="_blank">📅 17:54 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142249">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">👈
مقامات پاکستانی: مذاکرات با هدف بازگشایی تنگه هرمز و پایان دادن به جنگ همچنان ادامه دارد
✅
@AloNews</div>
<div class="tg-footer">👁️ 50.2K · <a href="https://t.me/alonews/142249" target="_blank">📅 17:50 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142248">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ME-ovMUrlvmfVSxZNrsL_1j5kyNcGaiebZShnyGVnAjM4_j7uhqViTQClFwowLDa_CpFkV7rl6xtEDEEpBGFFyA5yHZdjVcJX63njUifo1lmIcjFnjyIxAMTLKlnaKDgWBp08-ab5cExHiAdlmFKLyhCciHNxENKYTCHf1j9xDINQ7nGnF0aL6W-6j6J3NOCW3gbSCM8u7C-R8xR_KfjePaOyGy5fGblViJFiGYTDhxYt-EhfBTnQe5m6LYyUj4fZNhD6d7KRm5u568-sb7osnSF3-unFNGzqjFKZIeoPwiP9cJN1qM-_-ZxYdYk1syfJwr6-VY5cGLWv1ugcsx2uQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ظریف: قرار بود بعد رفتن آمریکا از افغانستان، نظام شاهنشاهی اونجا مجدد برگرده اما ما نزاشتیم و کمک کردیم طالبان قدرت بگیره
✅
@AloNews</div>
<div class="tg-footer">👁️ 58.5K · <a href="https://t.me/alonews/142248" target="_blank">📅 17:44 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142247">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromAlo Sport الو اسپورت</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/358b452f1a.mp4?token=KgsTpyBtSnOgcxFThacvSYcic67ppwnYCACqH_1iP8I1YV8m84Q-ADmkei72BjlLOTiZFoPJ6X07iBnsxOKPDa8CGzDNnAeOyiWENLBxkPvXrL9U8fSK5GGLA_zlU6u0RL1vHlV4oCgfacJ_uZDPytKnE6jV_wgutzGg6u3w9lu08GgOi3HlANzPzxYkwbGAQu58ncUc6PtGh8WbwYtsGPrG_xuNAM4tTciATDxZGulbRC-AFAFvK1TNFnlNWeYjM54ZfG6FYpCwNODWeNGbUd0sy03Br7hURoEqllY6SXgB4brOdne57-KiFIzlMZzxYCWg9MrjCjNDJLFtfgddYg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/358b452f1a.mp4?token=KgsTpyBtSnOgcxFThacvSYcic67ppwnYCACqH_1iP8I1YV8m84Q-ADmkei72BjlLOTiZFoPJ6X07iBnsxOKPDa8CGzDNnAeOyiWENLBxkPvXrL9U8fSK5GGLA_zlU6u0RL1vHlV4oCgfacJ_uZDPytKnE6jV_wgutzGg6u3w9lu08GgOi3HlANzPzxYkwbGAQu58ncUc6PtGh8WbwYtsGPrG_xuNAM4tTciATDxZGulbRC-AFAFvK1TNFnlNWeYjM54ZfG6FYpCwNODWeNGbUd0sy03Br7hURoEqllY6SXgB4brOdne57-KiFIzlMZzxYCWg9MrjCjNDJLFtfgddYg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👤
خداداد عزیزی: دخترهامو زور نکردم روسری سرشون کنن. برام مهم نیست چی دربارم میگن، حکومتی بودم که بیکار نبودم
@AloSport</div>
<div class="tg-footer">👁️ 51K · <a href="https://t.me/alonews/142247" target="_blank">📅 17:29 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142246">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BrH6QXjN_NNm2w2aRq0EANfbt9YLmefeGRjQ11pih7iezNraRQYJ7if34PYMup_SvMoUb1U4Bm6KxEGILfPAGh1e_qJLcWorlhqqD0P3i-c2oQjzmK6lvKxXseQJQW7Vr7g5UxuKdg54aHjbyPNg8AtkrjdyC73ws6BHgF07g-8lXGtRNS-tnXP99Ho-zqBH9ZWfgeJiuTFzuFJ6V-9MszvrlMS15MGQfAm3z-Zpl8wjez2ElKmnXnlENA-MyKwjNKXiAnifnrgC_BpTxkYgRwRBaZ6E2DbjxIWlILCRWbSRA7I9CG16Z7kGX-Mwdn44tLVKlMHIquRETTF6F1p8uQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
👈
مصطفی ایزدی، جانشین فرمانده کل سپاه پاسداران:
🔴
دنیای غرب تشنه معارف انقلاب اسلامی ماست
✅
@AloNews</div>
<div class="tg-footer">👁️ 52.4K · <a href="https://t.me/alonews/142246" target="_blank">📅 17:15 · 26 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>

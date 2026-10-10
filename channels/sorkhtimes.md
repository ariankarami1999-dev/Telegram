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
<img src="https://cdn4.telesco.pe/file/rsn5PL8jX5SrPoOPSy3vfwsiGEtBLpnSTga31KVq543CMHyKAAoLV5jccpcjKXUXajWwxzZI0D7ferzTTt7vpGVrLbVU31q0My0KWOq0itmbzFPWsGySSiYpXhJG5RM4INwAYmOR4pT5KloyXCOGg5t4KOy-lPvAdzhUzVLY6DEbQJeO9nxNmuyEjppuiWEnhplw8UdrlG0tL_EyawbWxacVSpXyuOflK94QoQtycSYfiWy_M3ND-q9OfyzY8vWDSF8bmKfymwXdOcSCApR5E_NgHy4W4lUjnfRzXPeTopJSeRzztve_icMYnY8rSbLVNzaqWbjwTX3TIMZyqfFmEA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 🚩سرخ تایمز🚩</h1>
<p>@sorkhtimes • 👥 21.5K عضو</p>
<a href="https://t.me/sorkhtimes" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ﷽ورزشی نویس پرسپولیس👤🎗️«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس.⛔رسانه سرخ تایمز مسئولیتی در قبال تبلیغات ندارد.</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-07-18 16:17:25</div>
<hr>

<div class="tg-post" id="msg-141269">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4f241a3512.mp4?token=eEsCxBUd0ZybbFmQ51YyC_Jb-JJ_GNfQ2FOYgyFdDgompiacLyPnmvXcjWq3FMEMVMaNhobIEoJxxaSgK5YrIaQzR5wNMOXoixNHJwTEBrOHRREeiJV5QiU4cpEVEiXZzqmRkkWkuIwU3Io2c_2rdIBmRHdE7EUotDJ1XksgvU6ulplthxyzui5LL8YIrA0zRLnHQeG2gQ6WwH-8XGg37F0aqw-1ZTeUX2P1YfboIp8JXE2GuztNDFlX176fOWQwX8RW5eOtJf6Tv04uUCQRk95DI466dvBfmD6Kk552aty200gFxPRua-PytApMiUa0alQ_4Yfvx7u3lMDsbJuqbA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4f241a3512.mp4?token=eEsCxBUd0ZybbFmQ51YyC_Jb-JJ_GNfQ2FOYgyFdDgompiacLyPnmvXcjWq3FMEMVMaNhobIEoJxxaSgK5YrIaQzR5wNMOXoixNHJwTEBrOHRREeiJV5QiU4cpEVEiXZzqmRkkWkuIwU3Io2c_2rdIBmRHdE7EUotDJ1XksgvU6ulplthxyzui5LL8YIrA0zRLnHQeG2gQ6WwH-8XGg37F0aqw-1ZTeUX2P1YfboIp8JXE2GuztNDFlX176fOWQwX8RW5eOtJf6Tv04uUCQRk95DI466dvBfmD6Kk552aty200gFxPRua-PytApMiUa0alQ_4Yfvx7u3lMDsbJuqbA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⭕️
ضدحمله زیبا رو ببینید
🔥
🔥
🔥
❌
با ٣ پاسِ تک‌ضرب و پاس‌ تو عمقِ زیبای محبی به بیفوما تک‌به‌تک میشه اما حیف که این کارِ تیمی با گل تموم نشد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.16K · <a href="https://t.me/SorkhTimes/141269" target="_blank">📅 15:31 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141268">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vw56z-pkpPbutR-ciBQ7ldycfTjCXjWG9Z-htVta3sMaqyqtcs6rxKd0Pe4dqtLFdyXrPZcTRheAVX7GE0KbKQvzp0UyqgUyJUKFdVmpDZMMKXlHLsjr9MBCfB89WB4mjPip5xBgWE0zLoI8tnb2jRbobQkTAJgQMP8NAv6yc1RtECEwhhaEGlcaNQj4QAJ5icFbi93zIjubEHYV4-mvpgV-WWCbGTJXt_jevVHCsTPian5GB5NnX2eIyztpz-kvx27ytiR-4JAKTovwjZu8M_dcmP3adKNJ59M6EXzmRpTn3D9cmp5-GmnsFP7Zyc_fpk4MWdbx_s3-aFprK-4Kow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
فوووووووووری / مهر
❌
محکومیت استقلال در پرونده‌ی آسانی قطعی است
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.27K · <a href="https://t.me/SorkhTimes/141268" target="_blank">📅 15:29 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141267">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4727e2d06d.mp4?token=umEPn-TFbhh70uUjjFArDc6uXPFp3NOJuYKc5FSHpVOlXWU7jP6fopH6kxwj3fe14cfizDGaGwONqPi7fQoIC7euY_Vu6_2sq8ddJIkMOapOM8bao2sCyoWvssdSVbkp6t7ClgqjkUeCIQmvoTa3yDKg3gR_YekcHIoKmMJqO0jWs8muNxs5MzW72NWjQpeliO4W7MKbmnX5-79RAEX1Fu0BJZ2nLpIrOFKDZPKh3d1-oWe2NW1xpI3gyusEjq8XfodVymnt09xx1fMMiVR_g8Dyewub75fzPHfTySDfwtjl9Fsyv3mWz4j0UJbY8Ff5tDk-zYYvdwVdmlRdvvvfCw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4727e2d06d.mp4?token=umEPn-TFbhh70uUjjFArDc6uXPFp3NOJuYKc5FSHpVOlXWU7jP6fopH6kxwj3fe14cfizDGaGwONqPi7fQoIC7euY_Vu6_2sq8ddJIkMOapOM8bao2sCyoWvssdSVbkp6t7ClgqjkUeCIQmvoTa3yDKg3gR_YekcHIoKmMJqO0jWs8muNxs5MzW72NWjQpeliO4W7MKbmnX5-79RAEX1Fu0BJZ2nLpIrOFKDZPKh3d1-oWe2NW1xpI3gyusEjq8XfodVymnt09xx1fMMiVR_g8Dyewub75fzPHfTySDfwtjl9Fsyv3mWz4j0UJbY8Ff5tDk-zYYvdwVdmlRdvvvfCw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
بیفوما و آن فرارهای همیشگی‌
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.31K · <a href="https://t.me/SorkhTimes/141267" target="_blank">📅 15:28 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141266">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">🚨
گویا پویا اسمی که امروز به میدان رفت و جوانترین بازیکن تاریخ باشگاه شد یکی از بازیکنان مورد علاقه تارتار هستش و شدیدا بهش علاقه داره و بهش قول داده که بهش بازی بده
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes
〰️</div>
<div class="tg-footer">👁️ 1.37K · <a href="https://t.me/SorkhTimes/141266" target="_blank">📅 15:27 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141265">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">🚨
این وسط شله زرد هم فجر و شش تایی کرد ..رسول خطیبی ی تنه فجرو نابود کرده
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.52K · <a href="https://t.me/SorkhTimes/141265" target="_blank">📅 15:22 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141264">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">🚨
فووووووری
🔴
باشگاه پرسپولیس وویس هایی از ایجنت یاسر آسانی داره که به پرسپولیس گفته آسانی بازیکن آزاد هست!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.61K · <a href="https://t.me/SorkhTimes/141264" target="_blank">📅 15:20 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141263">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oOf3ez5il9TVOk2uAFc5oJJbs_V9pO4O-LM6Qk7Y6QmX_hBWeDy0mPNeHn2-2skAyc8GTcuPLNV5co25aXdRPQevPV_vs91yee_ISwEofckIdYkxsoNuWO2beq5LgH0SpT3iv3Q4yhKSMPwoQOaT216ILqEBWuf6frnhEp1yP8gJ0VVzjxlNXMlVv8xA-Vljz05ysaiE_spqSmq2fKROJLme830C59Rhb6WSCfgO1X0PADMzaWPPFblIhFn8IyIedU1GrcEjBAh_mZbrLmeJ4GuojNrfaxDSr9oDDHh1AZQEJEJ7qmyeT1-S5PlXpPS3mdSby1nDo1wox4U6BLRamw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟣
نبرد حیثیتی در لیگ برتر؛ شیاطین سرخ مقابل تاتنهام، جدالی برای اثبات قدرت و تثبیت جایگاه!
[
منچستریونایتد
🔴
🆚
⚪️
ت
اتنهام
]
⚽️
منچستریونایتد با تکیه بر امتیاز میزبانی و قدرت در انتقال سریع توپ، به‌دنبال ضربه‌زدن به فضای پشت خط دفاع تاتنهام است. تاتنهام با پرسینگ و بازی مستقیم می‌تواند موقعیت‌های خطرناکی خلق کند، اما فضای خالی پشت مدافعانش نقطه‌ضعف مهمی خواهد بود.
سناریوی آماری محتمل: بازی پرموقعیت با شانس گلزنی هر دو تیم؛ نتیجه نهایی تا حد زیادی به کیفیت استفاده از موقعیت‌ها بستگی دارد.
🔵
بونوس ویژه ثبت‌نام برای کاربران سایت، با شارژ حساب از طریق کریپتو ۴٪ بیشتر از مبلغ شارژ حساب دریافت کنید.
🔗
برای پیش‌بینی این دیدار همین حالا وارد سایت اسپورت‌نود شو و پیش‌بینی خودتو با بونوس ویژه ثبت کن:
👇
2⃣
نسخه جدید سایت:
Sportn5b2.com
2⃣
نسخه قدیمی سایت:
Sport90.bet
🔗
کانال رسمی اسپورت نود:
👇
🔵
@Sportnavad</div>
<div class="tg-footer">👁️ 2.19K · <a href="https://t.me/SorkhTimes/141263" target="_blank">📅 14:33 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141262">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">✅
✅
🔴
باشگاه پرسپولیس با ارسال نامه‌ای به مهدی تاج غیرقانونی بودن قرارداد یاسر آسانی با استقلال رو یادآوری کرد/فوتبالی
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.49K · <a href="https://t.me/SorkhTimes/141262" target="_blank">📅 12:34 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141261">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cvUJuNihIG5x9MeGf5XPDb6eyt5MRJRUXRk2ebgSt7Mcky5VKb_xhlP84vkzb4Xduur-GbKe-bDtjRMQIitKVKRXpc3rJvunPu1iPc1QULpn2izos_jOH32HczHyyOgKLRQIkRMU3gZNnACV05Y6Z4vBe-uJmrExN16JldhUaupVswwNoRcU6xuFDCU-7P1vMAMGb5ZF2Dl_8p6dxoDi0KZE02n8vst7u1kNA0CgbrV8cA-WzwbnZZLPQa3AzEftXzw5lkGA2xdau9_waN4yz4BDzITSghpZvPlQkAp0-PA3mKmrPd3weJurVXKCi9z_Lm2aC_AEgCoxOSSHHte32A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💢
پرسپولیس با ۱۵ گلِ زده، بهترین خط حمله لیگ برتر را در اختیار دارد
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.58K · <a href="https://t.me/SorkhTimes/141261" target="_blank">📅 12:20 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141260">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">🔴
اوستون اورونوف با گلزنی مقابل صنعت نفت به دومین گلزن خارجی برتر تاریخ پرسپولیس تبدیل شد.   «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.65K · <a href="https://t.me/SorkhTimes/141260" target="_blank">📅 12:13 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141259">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">⭕️
تیوی‌بیفوما وینگر33ساله پرسپولیس با نمره 7.8 بهترین‌بازیکن‌دیدار امشب‌سرخ‌ها برابر نفت شد.  «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.63K · <a href="https://t.me/SorkhTimes/141259" target="_blank">📅 12:11 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141258">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BA1RTBV5QQoMlgNlUpZ_FZ_HuaSeje0aSHBIyt1xLuAAhDKFAE1EuO-K_o9tgBejIjWFCCetfzUaQG0wewqFAQjwu3CaxOiPOowLlREiL1xBDYh-WqmssnbhkFpXYJ86ElrHlOLdr08YrhZkG404HrPdVTlx3itVjrWAPPRKyRVyZz0WTbOsaPN4seVLFS_3QVqGEJZwP0YGkYP2mOAHXmZ19UejQNCRITjet0IgZpDgoQP6VRLutbFfwbrL1Ao5-hqEHxtlIRXFJniOQj109eL7NvC9Q-L_TS8MUOKKAh_3LMkavKhE2UZFzEf9qWG87hu6Wi1fVhIEsQX6Omu9qQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🤩
✅
معوقه هفته‌هفتم لیگ‌برتر فوتبال
🤩
پرسپولیس
🆚
خیبر خرم‌آباد
🇮🇷
🗓
تاریخ چهارشنبه ۲۲ مهر
⏰
ساعت ۱۷
🏟
میزبان خرم‌آباد
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.62K · <a href="https://t.me/SorkhTimes/141258" target="_blank">📅 12:09 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141257">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">🚨
🔴
◀️
مجوز خارج شدن امتیاز باشگاه پادیاب خلخال از استان صادر نشده و باشگاه پرسپولیس برای خرید امتیاز این باشگاه با مانع روبرو شده است.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.1K · <a href="https://t.me/SorkhTimes/141257" target="_blank">📅 10:45 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141256">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">🚨
🚨
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 4.31K · <a href="https://t.me/SorkhTimes/141256" target="_blank">📅 10:29 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141255">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">🚨
🚨
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 4.21K · <a href="https://t.me/SorkhTimes/141255" target="_blank">📅 10:28 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141254">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a373367fda.mp4?token=sJE0tKBkQXg4uD_5o6A6KDlr9ZAV0BA-IgvClZp2gF6RttzMMvrwyD5hK1B2Iu29pFh2c-_DvqEGtSFROB_jio9SEFbby2G3jdGur2Rb31J2BIlbH5Ji7RTTVPzxZN6h2zBFyyfy2LgCytvVU_JxMhObpM1-a1OQnj_lgzkTfGp1y5brWivVBC0BM7Ui8SHckvql3t7e1_GTnxJrdi6WF5ApKxubwejFZKEp59Cr4fTdb1-4vgB9lxIAsKMQXWCFq1B9DtoliSkQsiWB-jVuGzAyQ4I02Q0Q9medDQLI09KQ1DzWQG_fuozIBr1UCIp1GoB6DUV62bbOrvtOWeWCGA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a373367fda.mp4?token=sJE0tKBkQXg4uD_5o6A6KDlr9ZAV0BA-IgvClZp2gF6RttzMMvrwyD5hK1B2Iu29pFh2c-_DvqEGtSFROB_jio9SEFbby2G3jdGur2Rb31J2BIlbH5Ji7RTTVPzxZN6h2zBFyyfy2LgCytvVU_JxMhObpM1-a1OQnj_lgzkTfGp1y5brWivVBC0BM7Ui8SHckvql3t7e1_GTnxJrdi6WF5ApKxubwejFZKEp59Cr4fTdb1-4vgB9lxIAsKMQXWCFq1B9DtoliSkQsiWB-jVuGzAyQ4I02Q0Q9medDQLI09KQ1DzWQG_fuozIBr1UCIp1GoB6DUV62bbOrvtOWeWCGA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
آنالیز محمد تقوی از بازی پرسپولیس-صنعت‌نفت
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.29K · <a href="https://t.me/SorkhTimes/141254" target="_blank">📅 10:22 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141253">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 4.7K · <a href="https://t.me/SorkhTimes/141253" target="_blank">📅 09:24 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141252">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 4.6K · <a href="https://t.me/SorkhTimes/141252" target="_blank">📅 09:23 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141251">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">⭕️
⭕️
⭕️
⭕️
⭕️
⭕️
پویا اسمی که متولد 1 شهریور سال 1388 میباشد به جوان ترین بازیکن پرسپولیس در تاریخ لیگ برتر با 17 سال و 1 ماه و 16 روز سن تبدیل شد.
🛍
پیش از او این رکورد در اختیار احسان خرسندی مهاجم پرورش‌یافته آکادمی پرسپولیس بود که در 29 اردیبهشت 1381 در دیدار…</div>
<div class="tg-footer">👁️ 4.71K · <a href="https://t.me/SorkhTimes/141251" target="_blank">📅 09:12 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141250">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">⭕️
⭕️
⭕️
⭕️
⭕️
فووووووری؛ سازمان نظام وظیفه به بیرانوند اعلام کرده تا زمان مشخص شدن وضعیت کمیسیون پزشکی‌اش حق خروج از کشور را ندارد و ممنوع الخروج شده  «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.7K · <a href="https://t.me/SorkhTimes/141250" target="_blank">📅 09:05 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141249">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">❤️
❤️
❤️
صبحی که تیم برده و 16 امتیازی شدیم با یک بازی کمتر و تیمهای دیگه تو حاشیه هستند و پرسپولیس تو آرامش بخیر   «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.66K · <a href="https://t.me/SorkhTimes/141249" target="_blank">📅 08:59 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141248">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">❤️
❤️
❤️
صبحی که تیم برده و 16 امتیازی شدیم با یک بازی کمتر و تیمهای دیگه تو حاشیه هستند و پرسپولیس تو آرامش بخیر
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.56K · <a href="https://t.me/SorkhTimes/141248" target="_blank">📅 08:57 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141247">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cMIeEPKHVL4ZDJ0-fswROKM1rfCdpOAPIvu7vQ7oQGT-6YuPfDoa0fMgAfYHaCAQky4FvPAZb3T06aPUMZxOmr7byxuVkSwTzDLvP1m4ynhUXCAUkaZFFHc2So316SxQeGY8McTg8xSDW0ekj2A8zQbva1xtefQYKGw0BGNaQPOmSr0IoY0L76a8V7vXF7eo7JD1CPOSliWmQNXXhsLIx7UyBtk9xBvQuZJDL4wtbXpVxi-dtqJJO86Wd0qB8ArlzB0ctLtBRLlXcW7wdUB6l9y0PvFq6AOS1dnqf3EEI7Tkh6RBuCnF9FPVcZ4Rymj9DHZpmrzEBalc0FGuisdmhQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
ورود به اسپورت‌نود؛ ساده‌تر از همیشه!
🔗
دنبال یه راه سریع و بدون دردسر برای ورود به اسپورت‌نود هستی؟
🔵
با مینی‌اپ ربات رسمی اسپورت‌نود، مسیر دسترسی ساده و یکپارچه شده؛ بدون لینک‌های متعدد و مراحل اضافی، مستقیماً وارد محیط کاربری شو و از امکانات سایت استفاده کن.
🔗
ربات رسمی اسپورت‌نود:
👇
🔵
@Sportnavad_bot
🔵
@Sportnavad_bot
🔗
کانال رسمی اسپورت‌نود:
👇
🔵
@Sportnavad</div>
<div class="tg-footer">👁️ 5.14K · <a href="https://t.me/SorkhTimes/141247" target="_blank">📅 01:05 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141246">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">🏅
صحبت‌های جنجالی احمد گوهری درباره دلیل جدایی از پیکان: سرمربی فصل گذشته پیکان به جادوگری اعتقاد دارد!  «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.12K · <a href="https://t.me/SorkhTimes/141246" target="_blank">📅 01:01 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141245">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">🏅
صحبت‌های جنجالی احمد گوهری درباره دلیل جدایی از پیکان: سرمربی فصل گذشته پیکان به جادوگری اعتقاد دارد!
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.04K · <a href="https://t.me/SorkhTimes/141245" target="_blank">📅 01:00 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141244">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">⭕️
⭕️
⭕️
⭕️
⭕️
فووووووری؛ سازمان نظام وظیفه به بیرانوند اعلام کرده تا زمان مشخص شدن وضعیت کمیسیون پزشکی‌اش حق خروج از کشور را ندارد و ممنوع الخروج شده  «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.34K · <a href="https://t.me/SorkhTimes/141244" target="_blank">📅 23:51 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141243">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">🚨
🚨
🚨
#فوری/بیرانوند با دستور نظام وظیفه ممنوع الخروج است و امروز هم مجوز تمرین نداشته.
🚨
کریمی و نکونام می دانستند بیرانوند حق خروج ندارد و برای خوشایند زنوزی اخراجش کردند.
🚨
اکنون هم می خواهند سر هواداران را گرم کنند و به رسانه ها می گویند مشکل حل شده و به…</div>
<div class="tg-footer">👁️ 5.5K · <a href="https://t.me/SorkhTimes/141243" target="_blank">📅 23:44 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141242">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/diYURjpD1D14uT0Q--CKZBa9mvKmVTilq4foL0yv9CyUZGOsgZztJi6BTRj6N3kebPx-LC29CrVHRB476nQAn8DuqKzIqUSNQ1YWMtzwi2BOiOSRp5bh97uytEv_uZHoPA1fS9Y6WYdZLzwKWKzWThbqAC9h8ZtF5POi83CAHGpVit6egmKzhTQwnOmk-o0dLvRr4p_Lhfbar_PsTXjA2P76Zl-VDf0-vBA2RVcPG2-0XUvjJ6RNvvc-rk2JqYApP_G5-xFMG_lBmCgQE5WLkAUhDTDkXW8BCwRevvviMJrWRL5Gc0JcvcZt2WkOyDViVnHShPd74dtie3Kxewoglg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
اوستون اورونوف با گلزنی مقابل صنعت نفت به دومین گلزن خارجی برتر تاریخ پرسپولیس تبدیل شد.
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.54K · <a href="https://t.me/SorkhTimes/141242" target="_blank">📅 23:39 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141241">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">🚨
‼️
🇮🇷
منفوری بیرانوند ادامه داره
🚨
فوری؛ بیرانوند از هتل هم  اخراج شد!  علیرضا بیرانوند پس از درگیری لفظی با مدیران تراکتور و در آستانه سفر آسیایی این تیم، از حضور در اردوی تراکتور منع شد.  «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.69K · <a href="https://t.me/SorkhTimes/141241" target="_blank">📅 23:33 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141240">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PkQgu42Syr2XpMWMVMsGw0T0VDm9JIeMn3xJ-6e7qoHheDXPBSNFEzjaazCminb_isCUDMAHwkFzgo1hp7YC05VsXdLh8UwQbuRaRoHLuN3rs2XloblS6mwrvm0GDaMyqOVaqcymhkRlto-qK0LIDLsfjU9nZ-khn-Du1jEoDgX1_wravuNawN6wEgpxeMFVaYbkObUjHuybxH2htS6LcYY0z-qG0s4ppV24TiGpIzRnPZdis6DAZLm2FhSKfu7-biAYK-nX2r8rzHjLJKqptwv_2lbgVcfhzb8CL4x80J4pYqGga7YrOZ8P6woJ1yjLmtw5i3atcxS0tszMsraYXQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
❌
محمد نوری پس از شکست مقابل پرسپولیس به صورت توافقی از صنعت نفت آبادان جدا شد.
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.48K · <a href="https://t.me/SorkhTimes/141240" target="_blank">📅 23:31 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141239">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/47ce1b9f2c.mp4?token=jxTsn8_io4g58J3oGac1ADkO7-zqlIPCpLAa7m6NdGEprr3493A-vDxrHFMOFEZdzNst0gHz39egUrLoWISpLlCOGuNNwMCPdGn07snCeJBya3wHediiUPYqHXQo8QfpdxjxvqWIDkOyqHgJZRnIJSXR8QctvJ_1w957r-TP_tuEYMKJRv8abOodDY2mrqWq13kioELnfeHDc-Y4q7LolRbm2HhvDFqny4c2Gqm54bZmZFw1IZW7uDlx_iU8nJ_4PWO-0l2pzxPTfxFY2J7zOg_mhS9PULBGW_faJRVQP7v9tbm1Bm9Ts4ahN75itEoO7QjJEma8SF1doCG5dVU0rj8WtdoG__jXy5GKrMNCovgqliSsFdXDYD3Av8ZymbBNcNHcMFr3damBzAReHUGIwsNiPHsU7wRM2za8DtNk1SzdHCOKnCvkBSWczhr0hWPicfL7rxY6fBqWNeXngEAmjYIAx4KtEJc_whlWfTxed8dO06Ar2qVc6MHgZ-4QzIKdjhsn2leoqKg50qBV89AT7H15vTXWw6GyvitMdsStJryr5_lZzZvuaqMmYrEa55m3yQ-z-CgUZd2RIJ--tSM0Xes4v1JvADSn20bA4kXdKDmfuuctzSWKaFJcljjXLrQmgeLJxGidfTNxT_OaUmfPRxfLmfC_xMUCkSSVqTQijvk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/47ce1b9f2c.mp4?token=jxTsn8_io4g58J3oGac1ADkO7-zqlIPCpLAa7m6NdGEprr3493A-vDxrHFMOFEZdzNst0gHz39egUrLoWISpLlCOGuNNwMCPdGn07snCeJBya3wHediiUPYqHXQo8QfpdxjxvqWIDkOyqHgJZRnIJSXR8QctvJ_1w957r-TP_tuEYMKJRv8abOodDY2mrqWq13kioELnfeHDc-Y4q7LolRbm2HhvDFqny4c2Gqm54bZmZFw1IZW7uDlx_iU8nJ_4PWO-0l2pzxPTfxFY2J7zOg_mhS9PULBGW_faJRVQP7v9tbm1Bm9Ts4ahN75itEoO7QjJEma8SF1doCG5dVU0rj8WtdoG__jXy5GKrMNCovgqliSsFdXDYD3Av8ZymbBNcNHcMFr3damBzAReHUGIwsNiPHsU7wRM2za8DtNk1SzdHCOKnCvkBSWczhr0hWPicfL7rxY6fBqWNeXngEAmjYIAx4KtEJc_whlWfTxed8dO06Ar2qVc6MHgZ-4QzIKdjhsn2leoqKg50qBV89AT7H15vTXWw6GyvitMdsStJryr5_lZzZvuaqMmYrEa55m3yQ-z-CgUZd2RIJ--tSM0Xes4v1JvADSn20bA4kXdKDmfuuctzSWKaFJcljjXLrQmgeLJxGidfTNxT_OaUmfPRxfLmfC_xMUCkSSVqTQijvk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✔️
⚪️
⚽️
تاج: با یحیی گل‌محمدی برای هدایت تیم ملی امید به توافقاتی رسیده‌ایم
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.42K · <a href="https://t.me/SorkhTimes/141239" target="_blank">📅 23:28 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141238">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">✅
✅
تاج : آزادی تا 2028 باید مسقف بشه، وگرنه دیگه اجازه میزبانی نمیدن.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.5K · <a href="https://t.me/SorkhTimes/141238" target="_blank">📅 23:25 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141237">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a0fbe6664d.mp4?token=hMDaVQCA6LeV8ZdcZjQn2A-juz7qyVYuGk14j_3WbxVnSkZwf0LpnOSn5CAXy6x86hSjM-A--bhnSh5L1awTPPDNSUPeHzUsulJVAzshqT2h_up9_Rh3kmDu9DQ14tdy53Hvtfqayu-TDSqFa8fiMpM76u6YeXoImX641GTZSVu3O7Xx3qjRTB8_N-8vw8d10jbqgXy8mrQ9EpvTmRA7OVH0Fs2iUJl2RrCUqdX35s_DlM6YAcywyWGAwNWtBZ0lLdc136f6mBwzODpZs_laBe821ltMEJ1hxy8yshzcoND7YZTSRvRrBqMWNX7b0dDi3Q5GzI-oZRPtfLwUlya-iA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a0fbe6664d.mp4?token=hMDaVQCA6LeV8ZdcZjQn2A-juz7qyVYuGk14j_3WbxVnSkZwf0LpnOSn5CAXy6x86hSjM-A--bhnSh5L1awTPPDNSUPeHzUsulJVAzshqT2h_up9_Rh3kmDu9DQ14tdy53Hvtfqayu-TDSqFa8fiMpM76u6YeXoImX641GTZSVu3O7Xx3qjRTB8_N-8vw8d10jbqgXy8mrQ9EpvTmRA7OVH0Fs2iUJl2RrCUqdX35s_DlM6YAcywyWGAwNWtBZ0lLdc136f6mBwzODpZs_laBe821ltMEJ1hxy8yshzcoND7YZTSRvRrBqMWNX7b0dDi3Q5GzI-oZRPtfLwUlya-iA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
در اتفاقی غیرمنتظره پس از پایان دیدار با صنعت نفت، تعدادی از هواداران پرسپولیس با قرار دادن موانعی از جمله لاستیک خودرو در مسیر اتوبوس این تیم، مانع از حرکت آن شدند.
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.7K · <a href="https://t.me/SorkhTimes/141237" target="_blank">📅 23:05 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141236">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nBjwOIx56a6Kgdp9yKRburVAS-QFgv910DEri9pvtc1Oz_xGrm-rzzw8Y5_sCszRi8Yq1m8GIPc5hdt_L88MICg78tw0w9BD4mST-EJTqPjanV8j4CR2jZ6WJR08UVeQYr3FJ8RI_ngOexiGoL9NLFrTKHAEvSatgRdlAaYX3rLu6_OJ3iq-JKLv3X-AgowXS7Hp7d8mNNuGqaAK48jFo3m2HeHI5QvY9lhvT4fErawChkPk0aVmy7SgYGSWGUKwvgIZN7ubKn9P3QUW4jW4J_yxax1GKQ9U5qW2_SBJSsdpmQPMNyJgeB5hdy5eOOVeCPmQ4wPUcfNAvVKs2lkiFQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
‼️
🇮🇷
منفوری بیرانوند ادامه داره
🚨
فوری؛ بیرانوند از هتل هم  اخراج شد!
علیرضا بیرانوند پس از درگیری لفظی با مدیران تراکتور و در آستانه سفر آسیایی این تیم، از حضور در اردوی تراکتور منع شد.
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.7K · <a href="https://t.me/SorkhTimes/141236" target="_blank">📅 23:03 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141235">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a37a5e6308.mp4?token=VcGrjn0-pZK5Hwk7oGZNtG-y1uV8yP68L9n3NKrgzNlcgg0fazLAGEDhB_gZRzxnh0ry8qbB33QmnArX_wRA6wfT6DAoWG1LjRvViaLeBqN5WL12JXdu8sDqxgKCdXB9QDKoRzlwY_adqJE0Eo4nKga1GGFHZ29hUB6qChWd7-WU3AP7VS6b-7KxVtX3jzZM6Wq4_K8koa-DVd2FQ1C4okWY9pn3iIEqcMG5TI8ivR5TcHUrcFgHDi74Cpo7nfnLTuZArWXN_VSd4nd7kFk92_fOAVzWsM2zQhevP7pAcXCQGx0GiffIc6Uwve4gDWgwifaalMDlDTgefEauwVjnjQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a37a5e6308.mp4?token=VcGrjn0-pZK5Hwk7oGZNtG-y1uV8yP68L9n3NKrgzNlcgg0fazLAGEDhB_gZRzxnh0ry8qbB33QmnArX_wRA6wfT6DAoWG1LjRvViaLeBqN5WL12JXdu8sDqxgKCdXB9QDKoRzlwY_adqJE0Eo4nKga1GGFHZ29hUB6qChWd7-WU3AP7VS6b-7KxVtX3jzZM6Wq4_K8koa-DVd2FQ1C4okWY9pn3iIEqcMG5TI8ivR5TcHUrcFgHDi74Cpo7nfnLTuZArWXN_VSd4nd7kFk92_fOAVzWsM2zQhevP7pAcXCQGx0GiffIc6Uwve4gDWgwifaalMDlDTgefEauwVjnjQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🔴
❤️
فووووووووری ؛ بیرانوند رفته هتل محل اردوی بازیکنان تراکتور ولی توسط نگهبان هتل راه ندادنش و گفتند سیکتیر
😂
😂
😂
😂
😂
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.14K · <a href="https://t.me/SorkhTimes/141235" target="_blank">📅 22:06 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141234">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dfc26b95b5.mp4?token=Tiu1coHIp25T9lHvZj0rKubFqQJVJKd-QXWPgwQTG_AMMYzZgvJX8Xqg6-J_CtpJeEBtTER3P08ep6RlmaEQYml7N-hqnWdmhcQUWV2KFvftp9qpazLDloKTARnjDg6LN2xi4ao8OZNGXfT2Y6QPhHnCIdToTuOK1smguTnavt2_M-P7MUzgS69gZ1PNItL7Qr1K0HAcA7JyjZPD99MFHryhW8L05K5NUbDRmjgz1tpklDgi1wkHRNzHfxDdQa4EslGAJXmqR-AP3n9pR8sN6ledA6vJITIFpcEBoN9X0bh1-WzlIRwssyTLYGAntqLq5Cu5SQ5PM9jXCR6X01cXjQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dfc26b95b5.mp4?token=Tiu1coHIp25T9lHvZj0rKubFqQJVJKd-QXWPgwQTG_AMMYzZgvJX8Xqg6-J_CtpJeEBtTER3P08ep6RlmaEQYml7N-hqnWdmhcQUWV2KFvftp9qpazLDloKTARnjDg6LN2xi4ao8OZNGXfT2Y6QPhHnCIdToTuOK1smguTnavt2_M-P7MUzgS69gZ1PNItL7Qr1K0HAcA7JyjZPD99MFHryhW8L05K5NUbDRmjgz1tpklDgi1wkHRNzHfxDdQa4EslGAJXmqR-AP3n9pR8sN6ledA6vJITIFpcEBoN9X0bh1-WzlIRwssyTLYGAntqLq5Cu5SQ5PM9jXCR6X01cXjQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
اتوبوس تیم ابوالفضل جلالیو جا گذاشته تو ورزشگاه
😐
😂
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.09K · <a href="https://t.me/SorkhTimes/141234" target="_blank">📅 22:04 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141233">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">✔️
#فوری | شنیده شدن صدای چندین انفجار در شرق بندرعباس و اطراف قشم منشا صدا مشخص نیست
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.41K · <a href="https://t.me/SorkhTimes/141233" target="_blank">📅 21:27 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141232">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">🚨
محسن خلیلی، سرپرست پرسپولیس:
❌
یاسر آسانی؟ باشگاه تمام مسائل را از صفر تا صد پیگیری می کند. داخل کشور به نتیجه نرسیم صددرصد در دادگاه عالی ورزش دنبال می کنیم. ما نگفتیم این پرونده پایان یافته است. مندیت آسانی به پرسپولیس؟ بله او مندیت را داشت اما زمان همه چیز را در این زمینه نشان می دهد
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.42K · <a href="https://t.me/SorkhTimes/141232" target="_blank">📅 21:17 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141231">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">🚨
تارتار:
🔴
به خاطر گلی که خوردیم و موقعیت‌هایی که از دست دادیم ناراحتم
🔴
از شادی هواداران پرسپولیس خوشحالم؛ آنها همیشه باید خوشحال باشند
🔴
همه بازیکنان از کیفیت چمن استادیوم شهر قدس گلایه داشتند
🔴
از مسئولین کشور می‌خواهم ورزشگاه آزادی را هرچه زودتر آماده…</div>
<div class="tg-footer">👁️ 6.13K · <a href="https://t.me/SorkhTimes/141231" target="_blank">📅 20:53 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141230">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ANhTaJp4PrAQaCAfk03Y2y_TEsC3y_ttBhkELdBe0TZ-yPyM8o-7f7fc1CVKufYPHIb8HfeHsE7GDuB9vCAWEn7DJMB1CbdFNfHZ-EOrP6LeQPf4VGXINjkoIgSU4L5TuI69TlDSCsbDKO4WGMVqHcdMuHvSBNMNIQ1ITarq0Ml7VolMgDdd-HsnvYomPkYNVBbm2xkKgbDQl6yCpn7ZQ5AzCxd8bMpoBveqtxyTnRkFOmcNbBAome0K6U5rT1putuBCu5uBPsWjFgTtxPB8WQKyw2RSbHTShKeUz01ghzQeSzQv_l1mJE_MpWiWgT5f_-3DEgQoWiwe0E5nn_7hEA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
سرخپوشان پس از کسب پیروزی، جشن خود را با هواداران تقسیم کردند
❤️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.93K · <a href="https://t.me/SorkhTimes/141230" target="_blank">📅 20:48 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141229">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sCp9BmCQBBiQTRBWD9QNTltXmEBRkM0EeJXO2jUoXprEwd65DKnC2QFzRI3nJOJqkemTNlLDc3fiB40-47_DwNeyfU3OISQGXkh1y5PiteNTkvLiuFZUuZQ2HLwUF1NofliUL4iPmNVSFqJtNcpSu304ifE9BgJIy6xR2IPKyZWU6xe45wgk2shmPCI9nSxqjyyHV5lspysUlEolwHiP6-EJlOtA9NPLeBI5bVUqeM7BMwMGQvTvMQ82whgEnmtyG6kKF-RJHN_h_U-LhEcmZf3MPuzN9c0CgZ6sxPR7fqDs2QuBWp0ziZFnaLxzQUyy8idlsvYYIBm08OgTmygUPg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
زنبورها در کمین سه امتیاز؛ وردربرمن آماده شوک در خانه دورتموند!
🔥
⚡️
[
دورتموند
🟡
🆚
🟢
وردربرمن
]
⚽️
دورتموند با ۱۲ امتیاز و آمار ۹ گل زده و تنها ۲ گل خورده در ۴ هفته، برتری آماری محسوسی نسبت به وردربرمن دارد که ۸ گل زده و ۸ گل دریافت کرده است. دورتموند در ۷ تقابل اخیر مقابل برمن شکست نخورده و با توجه به فرم هجومی میزبان، شانس بیشتری برای تسلط بر بازی دارد.
سناریوی محتمل: برد دورتموند؛ هرچند برمن با توجه به قدرت گل‌زنی‌اش می‌تواند برای خط دفاع دورتموند دردسرساز شود.
🔵
بونوس ویژه ثبت‌نام برای کاربران سایت، با شارژ حساب از طریق کریپتو ۴٪ بیشتر از مبلغ شارژ حساب دریافت کنید.
🔗
برای پیش‌بینی این دیدار همین حالا وارد سایت اسپورت‌نود شو و پیش‌بینی خودتو با بونوس ویژه ثبت کن:
👇
2⃣
نسخه جدید سایت:
Sportn5b2.com
2⃣
نسخه قدیمی سایت:
Sport90.bet
🔗
کانال رسمی اسپورت نود:
👇
🔵
@Sportnavad</div>
<div class="tg-footer">👁️ 5.65K · <a href="https://t.me/SorkhTimes/141229" target="_blank">📅 20:20 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141228">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">🚨
🚨
جونم جسارت تارتار ...پوریا اسمی .بازیکن محصل و مدرسه ای و آورد داخل   «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.49K · <a href="https://t.me/SorkhTimes/141228" target="_blank">📅 20:13 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141227">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">🎤
🔴
علی بازگشا: اسناد کامل و جدیدی درباره پرونده آسانی به کمیته استیناف ارسال کردیم
🔹
امیدوارم این پرونده در داخل کشور حل شود/ اقدامات قانونی را در داخل کشور انجام دادیم و اسناد جدیدی خدمت کمیته استیناف ارسال کردیم/ امیدواریم این اسناد جدید و مهم که تا به حال به این ارکان ارجاع داده نشده موثر باشد و رای جدیدی دهند/ تمام تلاشمان این است که موضوع در داخل کشور حل شود چون احترام به ارکان قضایی کشور است/ نامه‌ای را روز گذشته به فدراسیون ارسال کردیم و ادله ما شفاف است/ چیزی که از فدراسیون می‌خواهیم اجرای قانون است نه مصلحت اندیشی/ قانون منع مصلحت نیست/ تاثیرگذاری یک بازیکن غیرمجاز می تواند نظم جدول را برهم بزند و به بقیه تیم‌ها ظلم‌ شود/ پاسخگوی هوادار و سهامدار باشگاه هستیم/ ما مندیت آسانی را در آن تاریخ دریافت کردیم/ باید رای قاطع و جذاب صادر شود/ کسی تماسی نگرفته که این موضوع پیگیری نشود/ اسناد مختلف از جاهای مختلف رسیده است/ اگر نتیجه دربی به نفع ما شود دیگر طبیعتا در کاس پیگیری نمی‌کنیم ولی ما درباره این موضوع صحبتی نکرده ایم
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.55K · <a href="https://t.me/SorkhTimes/141227" target="_blank">📅 20:02 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141226">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">🚨
پیام نیازمند: بازیای بعد فیفادی همیشه سخته/ تا جام ملت‌ها خیلی مونده و تمام تمرکزم روی موفقیت پرسپولیسه/ کاپیتانی پرسپولیس برام افتخاره  «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.46K · <a href="https://t.me/SorkhTimes/141226" target="_blank">📅 20:01 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141225">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">🚨
✅
پیام نیازمند برای اولین بار در طی حضورش در پرسپولیس به عنوان کاپیتان کارش را آغاز خواهد کرد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.65K · <a href="https://t.me/SorkhTimes/141225" target="_blank">📅 20:00 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141224">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">🚨
🚨
جونم جسارت تارتار ...پوریا اسمی .بازیکن محصل و مدرسه ای و آورد داخل   «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.79K · <a href="https://t.me/SorkhTimes/141224" target="_blank">📅 19:49 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141223">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZfuXeDPQEnSBX9247cPAV3fCFCE_6U88tZVO03Cvhwgv18fprbjpnqX7fOLHui8VWafOsCsNDaW31Vr24oHKQUBkuHYGTspWw1OuQLuU3sUvQSQK6nG8JtFpFqRICFuNrsIcnts7XORFrsq1pWRM_uVeZhbSjNvAp9DESIWPCjP40IoHv6PiNT3QVb4CA_K-lSv22vdabaf3ft8wdl3HmgNyyuE-m-2v51qeUgRL_rgUhe4rrmx5vTf9EXgXvLZVrzm42giS8xg9-ZcZo9riIkEGcVDcEUfb5qmHvqpnTxQ7zQ2rMl88rVLN8y-oZ8PMDP05aSalqOBYK_I9ePkoJg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇮🇷
جدول لیگ‌برتر پس از بازی‌های امروز
🚨
پرسپولیس با برد مقابل خیبر در بازی معوقه، به صدر جدول میره
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.93K · <a href="https://t.me/SorkhTimes/141223" target="_blank">📅 19:22 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141222">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">🚨
چشم نوازترین پرسپولیس چند سال اخیر و میبینیم ..نیمه اول و با یک گل بردیم ...تو نیمه ای که سه چهار گل و نزدیم  «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.81K · <a href="https://t.me/SorkhTimes/141222" target="_blank">📅 19:10 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141221">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">🔴
🔴
💢
خلاصه بازی پرسپولیس 3 - نفت آبادان 1  «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.92K · <a href="https://t.me/SorkhTimes/141221" target="_blank">📅 19:07 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141220">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a74657a541.mp4?token=NJ1l8M0Gih6ArxMlXswSeMLWuCkSP7Mf6Gtk6KNaHiksZmO1ejXvcRixten0v5X72ddEtIm5TSl6hwK-ccEDfkFJ9gnX3f8kpm7mpoc6RkIP_Y7Rx9bSYUmxGgshudhAc0EGcmriyhoSQa8G8a0cwuLc7DCLZllGA2vtpOAsy_VW43OPpl87k3l5UiRh5lD4YLweCi8kNjmeZ2TWCBDA7ZCt7Cg9a1L22zQOSLrvwWZBVextyyWAMlr7p_3Np8-nRm_KMxQLxWcvNf37HyVymhE8VTM297d25ERSmO97WeV9YkxKfuLmYPgTrdy4c8dS3_a08o6GMTvBvJ7n36xQBQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a74657a541.mp4?token=NJ1l8M0Gih6ArxMlXswSeMLWuCkSP7Mf6Gtk6KNaHiksZmO1ejXvcRixten0v5X72ddEtIm5TSl6hwK-ccEDfkFJ9gnX3f8kpm7mpoc6RkIP_Y7Rx9bSYUmxGgshudhAc0EGcmriyhoSQa8G8a0cwuLc7DCLZllGA2vtpOAsy_VW43OPpl87k3l5UiRh5lD4YLweCi8kNjmeZ2TWCBDA7ZCt7Cg9a1L22zQOSLrvwWZBVextyyWAMlr7p_3Np8-nRm_KMxQLxWcvNf37HyVymhE8VTM297d25ERSmO97WeV9YkxKfuLmYPgTrdy4c8dS3_a08o6GMTvBvJ7n36xQBQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">💢
شادی ایسلندی بازیکنان پرسپولیس در کنار هواداران در ورزشگاه⠀
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.88K · <a href="https://t.me/SorkhTimes/141220" target="_blank">📅 19:05 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141219">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">🔴
🔴
💢
خلاصه بازی پرسپولیس 3 - نفت آبادان 1
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.67K · <a href="https://t.me/SorkhTimes/141219" target="_blank">📅 19:04 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141218">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">🚨
🚨
جونم جسارت تارتار ...پوریا اسمی .بازیکن محصل و مدرسه ای و آورد داخل   «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.74K · <a href="https://t.me/SorkhTimes/141218" target="_blank">📅 19:02 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141217">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">🚨
🚨
🚨
🚨
سوپرایز اصلی روی نیمکت تیم هست
✔️
✔️
پویا اسمی ۱۶ ساله
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.73K · <a href="https://t.me/SorkhTimes/141217" target="_blank">📅 18:54 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141216">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6f5a2397a1.mp4?token=Eem9lbcCXKfVHT8lUf8WxZA2D0-AgR1yq9D8YLZ2LVvCtWoOidDbzWEsETmfs94rAIuhUnzTtWsFsCe-7LYRQ_PZNF3R94nsQjIs7NyhZbI6sQKeQL6xKCHkZ0NRafYP4suceznjgzaBOJa13dVZVfN8L9PMETo3XDqrPr1_AomWAmqWm9A5GpZqNDp1NNksmLy1zZv2J9jRM7uXkNQBfXRmtMttNEEMW-vdTVu_agbnvN3m4G-VBgcfB_6oecgq0qtLsLeb7VAiR0V1avJ_kg8W839Tj8Uh3iqQK0iLd1XCZJ1BL84hx8sEfs688rkcm4ecEBHh2JvkQajE0dyHqg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6f5a2397a1.mp4?token=Eem9lbcCXKfVHT8lUf8WxZA2D0-AgR1yq9D8YLZ2LVvCtWoOidDbzWEsETmfs94rAIuhUnzTtWsFsCe-7LYRQ_PZNF3R94nsQjIs7NyhZbI6sQKeQL6xKCHkZ0NRafYP4suceznjgzaBOJa13dVZVfN8L9PMETo3XDqrPr1_AomWAmqWm9A5GpZqNDp1NNksmLy1zZv2J9jRM7uXkNQBfXRmtMttNEEMW-vdTVu_agbnvN3m4G-VBgcfB_6oecgq0qtLsLeb7VAiR0V1avJ_kg8W839Tj8Uh3iqQK0iLd1XCZJ1BL84hx8sEfs688rkcm4ecEBHh2JvkQajE0dyHqg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
گل سوم پرسپولیس به صنعت نفت توسط اوستون ارونوف 85
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.64K · <a href="https://t.me/SorkhTimes/141216" target="_blank">📅 18:53 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141215">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">🚨
همون بازیکن همیشگی و تاثیر گذار ..بیفوما پنالتی گرفت و علیپور زد   «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.46K · <a href="https://t.me/SorkhTimes/141215" target="_blank">📅 18:52 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141214">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">🔴
گلللللل دوم توسط علیپور  «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.57K · <a href="https://t.me/SorkhTimes/141214" target="_blank">📅 18:25 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141213">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a110cac30b.mp4?token=Dm9Kz08zJ8ECfFpI3tw5BJg-NQ6tgu-X_UnELcKeBu75YVNNi3Qbi6wZjNylv6efRWBQygi8MdtCNul6Pz3Qs0HNioeXRekPY30isbrPcWyzieVHeruVuiHBg_UO0-yvTv6z4Ehy56YcgYJcLqyNFhO6t4RKP9V8IMvC-YDiLFjw5qePQ6PIo6xAo-Es-GS6FaLoo_q2tvd25_FGDngyHK9ax8onyihWcN-mvHqCDJA6GyK_fQ30cwppXjYqm0KYB2eWraOtuKg31psUIK9Ll-JGyTGPAlI2zTC3wD2Ued3VTV5gVblPCkvZTxylIKZFUfZTZNAU_EemJeThVseD-zzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a110cac30b.mp4?token=Dm9Kz08zJ8ECfFpI3tw5BJg-NQ6tgu-X_UnELcKeBu75YVNNi3Qbi6wZjNylv6efRWBQygi8MdtCNul6Pz3Qs0HNioeXRekPY30isbrPcWyzieVHeruVuiHBg_UO0-yvTv6z4Ehy56YcgYJcLqyNFhO6t4RKP9V8IMvC-YDiLFjw5qePQ6PIo6xAo-Es-GS6FaLoo_q2tvd25_FGDngyHK9ax8onyihWcN-mvHqCDJA6GyK_fQ30cwppXjYqm0KYB2eWraOtuKg31psUIK9Ll-JGyTGPAlI2zTC3wD2Ued3VTV5gVblPCkvZTxylIKZFUfZTZNAU_EemJeThVseD-zzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
گلللللل دوم توسط علیپور
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.55K · <a href="https://t.me/SorkhTimes/141213" target="_blank">📅 18:24 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141212">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">🚨
🚨
با تعویض اورونوف جای عمری و پورعلی جای لطیفی فر میشه اختلاف و نیمه دوم بیشتر کرد   «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.44K · <a href="https://t.me/SorkhTimes/141212" target="_blank">📅 18:12 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141211">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">🚨
چشم نوازترین پرسپولیس چند سال اخیر و میبینیم ..نیمه اول و با یک گل بردیم ...تو نیمه ای که سه چهار گل و نزدیم  «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.4K · <a href="https://t.me/SorkhTimes/141211" target="_blank">📅 18:06 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141210">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">🚨
چشم نوازترین پرسپولیس چند سال اخیر و میبینیم ..نیمه اول و با یک گل بردیم ...تو نیمه ای که سه چهار گل و نزدیم  «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.35K · <a href="https://t.me/SorkhTimes/141210" target="_blank">📅 18:03 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141209">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/36338a35c2.mp4?token=SOyPzJmVyNuFOL64JUKq412HFQVbgP4JHkcfsBKdUERV38kXCLn6kbsn0KoLRSDO2x8lEjemuucewjWZ2QLwJZsZ4INbgn20fMhnMqGOXegD7JgonqK3rHkNXWQEWAF2qmvAK5ybALCz5V66roBcqAYyXDZJ-BJThAdLn0fItWXTwoO16BzMo3EoWiRLCr1jrHr1QEGrA_5OL1gpDZyOOe6ywhr0wA2LDkEjuvODr9RBhcQbnBN58olisXOddqScG34CbCRGCnzOy41vSgS6VG36pJmpq27xwnUGfyk6gs-CmoxjGQFUkbTFSRozdc87I0Hxv3ojqqWHIijAz9IKZQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/36338a35c2.mp4?token=SOyPzJmVyNuFOL64JUKq412HFQVbgP4JHkcfsBKdUERV38kXCLn6kbsn0KoLRSDO2x8lEjemuucewjWZ2QLwJZsZ4INbgn20fMhnMqGOXegD7JgonqK3rHkNXWQEWAF2qmvAK5ybALCz5V66roBcqAYyXDZJ-BJThAdLn0fItWXTwoO16BzMo3EoWiRLCr1jrHr1QEGrA_5OL1gpDZyOOe6ywhr0wA2LDkEjuvODr9RBhcQbnBN58olisXOddqScG34CbCRGCnzOy41vSgS6VG36pJmpq27xwnUGfyk6gs-CmoxjGQFUkbTFSRozdc87I0Hxv3ojqqWHIijAz9IKZQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
چقدر خوبی شما آقای نیازمند
❤️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.34K · <a href="https://t.me/SorkhTimes/141209" target="_blank">📅 18:00 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141208">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">🚨
🚨
یک گل زدیم و سه گل نزدیم ..و همچنان پرسپولیس مثل همه بازی ها سوار بازیه  «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.33K · <a href="https://t.me/SorkhTimes/141208" target="_blank">📅 17:54 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141207">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">🚨
🚨
گل اول و زدیم خیلی زوددد....سرگیف داد بیفوما زد   «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.36K · <a href="https://t.me/SorkhTimes/141207" target="_blank">📅 17:37 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141206">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">🚨
🚨
بریم برای بازی حساس که سه امتیازش به اندازه شش امتیاز ارزش داره ..دلمون برای پرسپولیس تنگ شده بود   «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.36K · <a href="https://t.me/SorkhTimes/141206" target="_blank">📅 17:09 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141205">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">🚨
🚨
بریم برای بازی حساس که سه امتیازش به اندازه شش امتیاز ارزش داره ..دلمون برای پرسپولیس تنگ شده بود   «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.46K · <a href="https://t.me/SorkhTimes/141205" target="_blank">📅 17:02 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141204">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">🚨
🚨
بریم برای بازی حساس که سه امتیازش به اندازه شش امتیاز ارزش داره ..دلمون برای پرسپولیس تنگ شده بود
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.39K · <a href="https://t.me/SorkhTimes/141204" target="_blank">📅 16:54 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141203">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">🚨
🚨
🚨
🚨
سوپرایز اصلی روی نیمکت تیم هست
✔️
✔️
پویا اسمی ۱۶ ساله
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.5K · <a href="https://t.me/SorkhTimes/141203" target="_blank">📅 16:11 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141202">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">🚨
🚨
🚨
🚨
سوپرایز اصلی روی نیمکت تیم هست
✔️
✔️
پویا اسمی ۱۶ ساله
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.29K · <a href="https://t.me/SorkhTimes/141202" target="_blank">📅 16:11 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141201">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">🚨
نیمکت ذخیره پرسپولیس مقابل صنعت‌نفت:
❌
❌
امیررضا رفیعی، ابوالفضل جلالی، علی علیپور، پوریا شهرآبادی، امیرحسین محمودی، محمدحسین صادقی، امیرحسین طاهری، پویا اسمی، پویا پورعلی، استون اورونوف، یاسین سلمانی
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس…</div>
<div class="tg-footer">👁️ 5.11K · <a href="https://t.me/SorkhTimes/141201" target="_blank">📅 16:09 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141200">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">✔️
ترکیب اومد ..جای جلالی تیکدری بازی می‌کنه..جای پورعلی لطیفی فر بازی می‌کنه و جای شهرابادی محمد عمری بازی میکنه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.01K · <a href="https://t.me/SorkhTimes/141200" target="_blank">📅 16:08 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141199">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3c7ca0c681.mp4?token=bljcMwt4ZLsGxyR0T9JNM-NotASMitE2JMU_ihWCzH3BygaHvszuNFbxtgS0LGJ2pLYUDVORj4uFGZQ2unh_lWZdDc0vMbDkIGDsuB2AOlIZ8flj6b9Ez1fj_gfmXCfo-J9CnVO0glZ21o9wvwoVPX0hnGhU2XZ2pGhZNYHWzc4qlnytaD4QE4f4dVmUWrwhPponG4r1BidRI6-sp2lbiN36_wEZiQp7hd4ULUKYEARYVFDp72VcspOa1uHbcsFytSsiGgXZOKpYkNT9_Js_V5lIuF-VkSRhqyL25V3scHdzMmuEj6w9ms0fORSxkqhbBb_5b41KYu1sesnJXKQzFA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3c7ca0c681.mp4?token=bljcMwt4ZLsGxyR0T9JNM-NotASMitE2JMU_ihWCzH3BygaHvszuNFbxtgS0LGJ2pLYUDVORj4uFGZQ2unh_lWZdDc0vMbDkIGDsuB2AOlIZ8flj6b9Ez1fj_gfmXCfo-J9CnVO0glZ21o9wvwoVPX0hnGhU2XZ2pGhZNYHWzc4qlnytaD4QE4f4dVmUWrwhPponG4r1BidRI6-sp2lbiN36_wEZiQp7hd4ULUKYEARYVFDp72VcspOa1uHbcsFytSsiGgXZOKpYkNT9_Js_V5lIuF-VkSRhqyL25V3scHdzMmuEj6w9ms0fORSxkqhbBb_5b41KYu1sesnJXKQzFA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
باران در شهرقدس و حضور بانوان هوادار پرسپولیس
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.76K · <a href="https://t.me/SorkhTimes/141199" target="_blank">📅 16:07 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141198">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">🚨
ترکیب احتمالی پرسپولیس برای بازی با صنعت نفت
✅
حضرات/نظرات:
📺
پیام نیازمند
📺
زارع
📺
ابرقویی
📺
جلالی
📺
عیدی
📺
خدابنده لو
📺
پورعلی
📺
محبی
📺
بیفوما
📺
شهرآبادی
📺
سرگیف
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.62K · <a href="https://t.me/SorkhTimes/141198" target="_blank">📅 16:06 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141197">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">🟥
ورود اعضای پرسپولیس به ورزشگاه شهدای شهرقدس
❤️
..
🚨
هوا هم مشخصه باد و بارون شدیده
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.78K · <a href="https://t.me/SorkhTimes/141197" target="_blank">📅 16:02 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141196">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/X3LcNMPIQP3Y-Hswi7f9tabMhbrdbfkEY4uPTtJ9kdTcu8xTKRwMwZb6drxYZO5Mp-ezT-Wb0Q7DP1IiXH6OtNpoh-_kMAi8c25wRW_l6FePhVkgYtZjmCWLrR3X7AJGN20btCmKt4ZZr_q4W98CTJHRrHPLaQByCkPkBanoYC2NrndZr7b0QNiLvuTWdedwDAsoKnt2N9H3hpCzjnK_TfDUYFQgkDIDzBKM41dapWSt01BMZwvkeo9Z_7h0w5sA73thcFGZCHLz3U_JKBYyYhlX7Ey-PPYYF6n6cnCsnZnRlbNbzNSRLCC64yrkreFm4v6GOv8_OIByQ6mAjY2hJA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
نمای آنلاین استادیوم شهرقدس
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.52K · <a href="https://t.me/SorkhTimes/141196" target="_blank">📅 15:58 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141195">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">⭕️
⭕️
با اعلام باشگاه تراکتور، علیرضا بیرانوند به دلیل مصاحبه بعد از بازی با استقلال از این تیم کنار گذاشته شد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.67K · <a href="https://t.me/SorkhTimes/141195" target="_blank">📅 15:40 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141194">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/heu5e7xm-BI_JJc44SO1mGSQj9jiClUa8dXP7quxbPY1X9Gs_79YXuYqBf4E4H9pZECfSSik8cvwKl8FMldV4JlfefnHABvBovJdJvWldsE-mWHdmXm60klYrFfDvXV_zTRXi0iOB9wcxMs2IbJ61vke2JDO73eW9E_fWNmkaFHU4laj5EK0WYC904dV3JHMs_9XS2VhD8gITuA9MUe2MauUPFkPzk0s526ZLJaN_LLS8XCgCBS4IOiEZM_W5WlmgeBSMdEx_thdP_HN-ZeotDIQiz3M1Z-MNqv3FkxeOYkVuGWFfuzSS8uwQBS3KAXAnquee4CQn9awbmn44NsADQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
خروج اعضای تیم از هتل به سمت ورزشگاه شهرقدس
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.73K · <a href="https://t.me/SorkhTimes/141194" target="_blank">📅 15:38 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141193">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">⭕️
فردا ببر و محبوب تر شو .حاج مهدی تارتار
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.77K · <a href="https://t.me/SorkhTimes/141193" target="_blank">📅 15:36 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141192">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/f7JBmuZiIi1RyhtBCMdwZ2w4zENEmZIWivJHPPeH2ih-D527XmqrR44GdoUijaoj4JlK_JFRFz2TaTqkNq1r3raL27aMY6R2j0tUMnV6ynwkLpKX6amkULVHvnhiWBWOS6lXz5NXetb_cFJRSAJnmy2SJ0-luN5rz_iBiXgwAcnIlsAUQktAUsoobP2qDi7x5l7W7RTxyOKl8_HTMMF2Pe04Gtw9_VHKFkBsvYHEqEBN-SuJZkVL6T3As__lda3NfrZJo3XcFprabNEnkkdCmh10wOGkgaPtD6KNsGcY3M1DRNukEld0dxDPKeG7gDHAvavjmMKLBumfj9h8ZlekNA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❤️
علی علیپور: از پیام‌های هواداران عزیز که نگران حالم بودند متشکرم. خوشبختانه مصدومیت جزئی‌ام برطرف شده و با آماده‌سازی کامل در خدمت تیم و کادرفنی هستم.
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.86K · <a href="https://t.me/SorkhTimes/141192" target="_blank">📅 15:26 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141191">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">🚨
🚨
باشگاه تراکتور درنظر دارد تا با توجه به مصاحبه علیرضا بیرانوند، به او اجازه فسخ قرارداد و حضور در تیمی دیگر را ندهد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.86K · <a href="https://t.me/SorkhTimes/141191" target="_blank">📅 14:25 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141190">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">🇮🇷
🇮🇷
🇮🇷
به مانند بانوان ، تمام بلیط های جایگاه به فروش رسید ، دم تک تک عزیزانی که توی این شرایط اقتصادی میرن هزینه می‌کنن و مستقیم  از تیم حمایت میکنن گرم
❤️
❤️
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.86K · <a href="https://t.me/SorkhTimes/141190" target="_blank">📅 14:13 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141189">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">🙏
🙏
🙏
🙏
🙏</div>
<div class="tg-footer">👁️ 4.92K · <a href="https://t.me/SorkhTimes/141189" target="_blank">📅 14:13 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141188">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">🙏
🙏
🙏
🙏
🙏</div>
<div class="tg-footer">👁️ 4.95K · <a href="https://t.me/SorkhTimes/141188" target="_blank">📅 14:12 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141187">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OCOxS1VKnJ_Bju6uIYKCSegV98KQYsFOvWiiCEWIIhHcbHJEU5H81U1yyqLbjdd3A00s-Ajub4141HG0tv4ySZeG_kdI-6871N5-AAQCyOyKGfwE9iBmAk4khAZq_oa5DsGMr9nC_6_7A0HFuE-1Fwsd5vBUBJ-CULWz801QkDjw3qUaJbesqF9627y0FODsIhelXznajHWy_nGdoU5xk9qqb_oFs80YwcXvWsFZWN6i5f06msC73RWAO4JqtR3VKReC0SKHAyRii7B1I3gaw74eMbpTeewuIZdF4zF82W72xeKyZ0s_jlikfhzPfzPFC6dAarDHsSNPDFzsdmSsFg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#فکت
‼️
علی علیپور در این فصل تمام گل و پاس گل های خودشو در این فصل در دیدار های خانگی و در ورزشگاه شهدای شهر قدس ثبت کرده
👀
✔️
پرسپولیس امروز در ورزشگاه شهدای شهرقدس به مصاف صنعت نفت آبادان می‌ره
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.11K · <a href="https://t.me/SorkhTimes/141187" target="_blank">📅 14:09 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141186">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">🚨
علیپور هنوز زانو درد داره و بازی کردنش ریسکه البته خودش میخواد که بازی کنه تا از کورس عقب نیفته
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.82K · <a href="https://t.me/SorkhTimes/141186" target="_blank">📅 13:34 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141185">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">🚨
❌
❌
اگه امروز علیپور بازی نکنه و در غیاب کنعانی نیازمند کاپیتانه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.8K · <a href="https://t.me/SorkhTimes/141185" target="_blank">📅 13:27 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141184">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bsCK-kQ7FJtDSvQtr-6TJ5Hi39YVKRrm0Rtd9TrLagFvC2ThkY9ae2WfDoAmo3KRKKzVVjFC1hVo1Ll_sOczp-XuYVHuyzsdKBrkFrz76RTEXIqVW-pQXMFUspB2_gQuwEdFU-YuOkUjGEJOqpbgII3s-lO8iwIRUDeR_jYuLYvOGyjx9k5iqYyPAysvb_x5nTsr3tQa4ME-QpUwK83kSu4-gOuNJbQTaWEMElS14UOKRa9Xj-38PJ_2DS1MmURCCx_Mslgb-M06JH1TjsI-439BNTiLlMclThk4aftLei9INyli1d9nA7dXxfGcTKSu6hRvEzIVThvY_v0XDRr10g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
سرخ‌ها در تعقیب صدر؛ صنعت نفت، مانع بعدی پرسپولیس در مسیر سه امتیاز!
🔥
⚡️
[
پرسپولیس
🔴
🆚
🟡
صنعت‌نفت
]
⚽️
پرسپولیس با ۱۳ امتیاز از ۶ بازی و میانگین ۲ گل زده در هر مسابقه، از نظر هجومی آمار بهتری نسبت به حریف دارد. صنعت نفت در ۷ بازی فقط ۲ گل زده و با ۸ گل خورده، ضعف محسوسی در فاز هجومی داشته است. در ۵ تقابل اخیر دو تیم، پرسپولیس ۳ برد کسب کرده؛ برتری آماری با سرخ‌پوشان است، هرچند غیبت برخی مهره‌ها می‌تواند روی عملکردشان اثر بگذارد.
🔵
بونوس ویژه ثبت‌نام برای کاربران سایت، با شارژ حساب از طریق کریپتو ۴٪ بیشتر از مبلغ شارژ حساب دریافت کنید.
🔗
برای پیش‌بینی این دیدار همین حالا وارد ربات رسمی اسپورت‌نود شو و پیش‌بینی خودتو با بونوس ویژه ثبت کن:
👇
🔵
@Sportnavad_bot
🔵
@Sportnavad_bot
🔗
کانال رسمی اسپورت نود:
👇
🔵
@Sportnavad</div>
<div class="tg-footer">👁️ 5.01K · <a href="https://t.me/SorkhTimes/141184" target="_blank">📅 12:48 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141183">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2cf12ee8e5.mp4?token=H3VqD8uKILBBMJtefeq4wNfuWc00gThB-PvZIdUzTcheKDTAMlX2_pzCxsoi8yZLVeFM1IKgRWYypG307XgX4rD4P_SClWu3pFUHOltfrITHadgXR2_OUdkxUDh9ruvzOfT3cS84F7_yjkfzaCpmruNJr1R9d3y3jCY3cnBNQGqNnPOHMDozAPKeflMTk6ss3VkogJsXy1CudZqpK531x1oOb-j1xZwx8jWoRmPKKQqNeCU02wsIy4j4_PuLFc5G2KHrPjhs0C-uhSskpKUKq4eE447zg4g3rrrHIAe_XCegycfKKB-mXHqfk1jutW14gHTW-qPHPYsFlfa2oNlZhQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2cf12ee8e5.mp4?token=H3VqD8uKILBBMJtefeq4wNfuWc00gThB-PvZIdUzTcheKDTAMlX2_pzCxsoi8yZLVeFM1IKgRWYypG307XgX4rD4P_SClWu3pFUHOltfrITHadgXR2_OUdkxUDh9ruvzOfT3cS84F7_yjkfzaCpmruNJr1R9d3y3jCY3cnBNQGqNnPOHMDozAPKeflMTk6ss3VkogJsXy1CudZqpK531x1oOb-j1xZwx8jWoRmPKKQqNeCU02wsIy4j4_PuLFc5G2KHrPjhs0C-uhSskpKUKq4eE447zg4g3rrrHIAe_XCegycfKKB-mXHqfk1jutW14gHTW-qPHPYsFlfa2oNlZhQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
پرسپولیس _ نفت آبادان
❌
اولین گل یورگن لوکادیا با پیراهن پرسپولیس
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.83K · <a href="https://t.me/SorkhTimes/141183" target="_blank">📅 12:38 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141182">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">⭕️
⭕️
⭕️
زنوزی هم بالاخره طعم تلخ داشتن بیرانوند را چشید!
❌
❌
سرانجام نوبت به زنوزی و مدیران تراکتور رسید تا طعم گس داشتن علیرضا بیرانوند را تجربه کنند؛ همان مصاحبه‌ها، همان گلایه‌های مالی و همان کنایه‌هایی که پیش‌تر مدیران پرسپولیس بارها با آن مواجه شده بودند.…</div>
<div class="tg-footer">👁️ 5.07K · <a href="https://t.me/SorkhTimes/141182" target="_blank">📅 12:30 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141181">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c2a79b142e.mp4?token=pehNcIxd_ZgcPrduz_p2rrMVw-El1hCeeBbhyyxFR2JFj9KTZEUtoDIOJojz7Y3U6cSBeQf0JkVm_FtqTj4dPZIgC1gMiuFAIBCWSghNVA5CE1N0B9u6YnqO5_teYdoOIRiM6ZggEIqgbde6V1-sLb7SU0mGIIIqusFhhPHV-tJj93PDWFODgyzPW1Ott0eGfQBjsRTMSj5WvJVtd9tVQO2HmnXMb1O3uBnUWyX9AhEDirr_gmbLjfI2m-_TqryjqtI-vGA0BwlLFlkQDORjXtB75TDPE3rcMQWEBFwydL3NiMhdm21y9Pr5bbZWX_zVJtWfAj968eUO8FFYQkSXuw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c2a79b142e.mp4?token=pehNcIxd_ZgcPrduz_p2rrMVw-El1hCeeBbhyyxFR2JFj9KTZEUtoDIOJojz7Y3U6cSBeQf0JkVm_FtqTj4dPZIgC1gMiuFAIBCWSghNVA5CE1N0B9u6YnqO5_teYdoOIRiM6ZggEIqgbde6V1-sLb7SU0mGIIIqusFhhPHV-tJj93PDWFODgyzPW1Ott0eGfQBjsRTMSj5WvJVtd9tVQO2HmnXMb1O3uBnUWyX9AhEDirr_gmbLjfI2m-_TqryjqtI-vGA0BwlLFlkQDORjXtB75TDPE3rcMQWEBFwydL3NiMhdm21y9Pr5bbZWX_zVJtWfAj968eUO8FFYQkSXuw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
معذرت خواهی هوادار تراکتورسازی از هواداران پرسپولیس
😁
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.26K · <a href="https://t.me/SorkhTimes/141181" target="_blank">📅 12:27 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141180">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">⭕️
⭕️
⭕️
زنوزی هم بالاخره طعم تلخ داشتن بیرانوند را چشید!
❌
❌
سرانجام نوبت به زنوزی و مدیران تراکتور رسید تا طعم گس داشتن علیرضا بیرانوند را تجربه کنند؛ همان مصاحبه‌ها، همان گلایه‌های مالی و همان کنایه‌هایی که پیش‌تر مدیران پرسپولیس بارها با آن مواجه شده بودند.…</div>
<div class="tg-footer">👁️ 4.85K · <a href="https://t.me/SorkhTimes/141180" target="_blank">📅 12:17 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141179">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/86b4db41c1.mp4?token=H-fueZJKaOoGhvZDJzGgcaW3Y6RM9D5M4l4yEYzSirDe6uebHXYjl7_6OKG65hTi1wfbmEYitxn6MAQJu3pQNedLQ7k4pGifZr1kx1jaehz5a7lSHbvMwynI61nCJ49g0rmLGgtqxWVNrZb3_UCRs59NhvB6hNJaz_YNTBp2Y7MRl6MuFJ11K8wxjTZHVImyA3wPIQHcxhSDKuOzeuwgmWGy2iibx9fAGthMm6RZEQHy3jwjEanTDOWeYTwfLHBZx2Min-YYRHsIUaDr0cB-r5jy1YsPFM_fHeMXOo2uCHTmsikb787y228tMd6asQ9ZnUI-6sGxGpcpuMN9yXBRQg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/86b4db41c1.mp4?token=H-fueZJKaOoGhvZDJzGgcaW3Y6RM9D5M4l4yEYzSirDe6uebHXYjl7_6OKG65hTi1wfbmEYitxn6MAQJu3pQNedLQ7k4pGifZr1kx1jaehz5a7lSHbvMwynI61nCJ49g0rmLGgtqxWVNrZb3_UCRs59NhvB6hNJaz_YNTBp2Y7MRl6MuFJ11K8wxjTZHVImyA3wPIQHcxhSDKuOzeuwgmWGy2iibx9fAGthMm6RZEQHy3jwjEanTDOWeYTwfLHBZx2Min-YYRHsIUaDr0cB-r5jy1YsPFM_fHeMXOo2uCHTmsikb787y228tMd6asQ9ZnUI-6sGxGpcpuMN9yXBRQg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
گویا دانیال اسماعیلی فر هم از ناحیه ای که رامین مصدوم شد مصدوم شده و احتمالأ یک ماهی نباشه
😁
😂
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.73K · <a href="https://t.me/SorkhTimes/141179" target="_blank">📅 12:13 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141178">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/59ff4bc2f6.mp4?token=it69vtzHYFruRZ3XBH2rUaZUvmM979RSkfwLFZ4gNlwbfRYBjjl6MwB4HsNfczC-mOdISPq1CIkYJNo5qvL1eAKBWh6Io5KiePYZ131Yg-7MCFOgcAf7WZ-MmDfJQUMDlXayjlQSMMbjK5z7gY-N0UNE6LQrC3JScZYRyYfzIujCA8Cb5_JrKiwqgN25PCWzSEHq8iON0pyhB2v2iezTjtduUfKhZcLRsQ4bFUvsn6OLh83ZJU3Sfetn760D1o1CcI9lIFsScgmC-FI8XvH3kdcJrPOZjQpYxhWS6tn4rRabchARzwO3X528kaulQvFo7dwK4MQG-739z14BWKSiRQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/59ff4bc2f6.mp4?token=it69vtzHYFruRZ3XBH2rUaZUvmM979RSkfwLFZ4gNlwbfRYBjjl6MwB4HsNfczC-mOdISPq1CIkYJNo5qvL1eAKBWh6Io5KiePYZ131Yg-7MCFOgcAf7WZ-MmDfJQUMDlXayjlQSMMbjK5z7gY-N0UNE6LQrC3JScZYRyYfzIujCA8Cb5_JrKiwqgN25PCWzSEHq8iON0pyhB2v2iezTjtduUfKhZcLRsQ4bFUvsn6OLh83ZJU3Sfetn760D1o1CcI9lIFsScgmC-FI8XvH3kdcJrPOZjQpYxhWS6tn4rRabchARzwO3X528kaulQvFo7dwK4MQG-739z14BWKSiRQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
🤩
ببینید دختر هادی نوروزی چقدر بزرگ شده؛ همسر هادی بعد ۱۲ سال هنوز لباس مشکی رو در نیاورده
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.98K · <a href="https://t.me/SorkhTimes/141178" target="_blank">📅 12:09 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141177">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YqXmrj-UOfXOeouIxpO8qTBupkVQslhuS5TQPScimT5sY91aX4ypV_TnUEy_HU3aVIhM0Dmudn7kRrFxmJY77nyZBu_YJTm23mS0fB1ZxeV8-nYpC1D3ienmBAgoJLy6EiM5nd-1SK4bcKF1UuUJdLjVbFqL0m_K3Gi2Ud8F4I0mUlJEGb106KH8HPLbjwB0B6JRrr0-6WMJrwwlJBJKDkMPhANoH33yjMyFxFr23BgTLrA_N_w6xEZrNUfhBsX2A5PTU35QpdcH4ezWtbxmE6X0XwWSu35pzBWIo8JWvsYwj0UFusPXm5_EWOucjplvY2eeJ3CchqMIVbMbSWGhgA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
پرسپولیس- نفت؛ ۹۰۵ روز پس از آن برد‌ خاطره انگیز
🚨
پرسپولیس و نفت آبادان پس از ۹۰۵ روز، امروز در ورزشگاه شهر قدس مقابل هم قرار می‌گیرند. در آخرین تقابل (۳۰ فروردین ۱۴۰۳)، پرسپولیس با گل‌های اسماعیلی‌فر، آل‌کثیر و کنعانی‌زادگان به برتری رسید و در نهایت قهرمان شد، در حالی که نفت با هدایت کمالوند به لیگ یک سقوط کرد.
🚨
اکنون هر دو تیم بدون مربیان قبلی (اوسمار و کمالوند) بازی می‌کنند و از سه گلزن آن دیدار، فقط کنعانی‌زادگان در پرسپولیس مانده که او هم مصدوم است و احتمالاً به بازی نمی‌رسد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.89K · <a href="https://t.me/SorkhTimes/141177" target="_blank">📅 12:03 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141176">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">❗️
⛔️
👀
پرسپولیس ب که قرار بود به سیدجلال سپرده شود، احتمالا با محسن بنگر وارد رقابت‌های دسته دوم لیگ آزادگان می شود...
‼️
🟥
به گزارش هفت ورزشی، پرسپولیس که دنبال خرید امتیاز برای راه‌اندازی تیم دوم بود، سرانجام امتیاز پادیاب خلخال را خرید‌. گفته می‌شد هدایت پرسپولیس…</div>
<div class="tg-footer">👁️ 4.99K · <a href="https://t.me/SorkhTimes/141176" target="_blank">📅 10:58 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141175">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gX0eKUKgDLSSN0jDfWuvJNIJTjIN0Y4_DIsSJ87ilYR5HCalUmcUcS4Uz4hx_0aKcAE4zcAEFd_H0NMnEC4V1xQKwnAJQu7wFjBQm4xe62IKXQsXNkjamftWBpxRsaAwm-P2I2AO8OYF3pzCePXQt-ZrfGF3qzieOhDDI253IBD7NhOPHMJqFxOt7M1XFyAKwNYLJpd8YoVTm7SqCbghzCfVaS4_cvRsqmIr-GKZRYzBenc9FI7yq8TJhoQldtgI7Wo6hprWy24WVknY8WGjC0NmRxnpgNHXVZ9RxHGC5y3JPdovapFSIM2XBViFcNQJGH5lVr1e13zu1YnGoobnlQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
دعوا در تراکتور بالا گرفت
❌
شکایت بیرانوند از کریمی مدیرعامل باشگاه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.96K · <a href="https://t.me/SorkhTimes/141175" target="_blank">📅 10:56 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141174">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">🚨
با نظر کریم باقری و موافقت مهدی تارتار ؛ پیام نیازمند کاپیتان سوم پرسپولیس شد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5K · <a href="https://t.me/SorkhTimes/141174" target="_blank">📅 10:46 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141173">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HqBE7IQCqpdTFuNvoKvX-1VGxoSKCjXtKqGXWBoBJp8Ugbj-rLy2YjBbFVLYOAKr5jbj-1D9q26K2xAdaQdLKUewHCDVpsazqoocneqplPH6VcB4W5dMr4ASU6SdCvKdQdevkU6OU3ZBrys09_-2E12JOvI4sRbK7JA0vBeXny_c-Yk3WE2ZktZFtYq6_qYPmQSJjCXIUYVXPv-TzdYlyRqKR5HT3tVJY8j7BY_W1kf0LDLf7zd0HpgOTM4qhgin9KmyfGAOBc2M54iLn8Cqoy-YjoiV9qjCqsH1rWJu_D2WMPr2JuiG56RUSWuCwIpHOHRXGjRAVBCQFoBUW39OFg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
با نظر کریم باقری و موافقت مهدی تارتار ؛ پیام نیازمند کاپیتان سوم پرسپولیس شد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.12K · <a href="https://t.me/SorkhTimes/141173" target="_blank">📅 10:45 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141172">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">✔️
✔️
کریستیانو رونالدو امروز برای سومین روز متوالی در تمرین تیم ملی پرتغال حاضر نشد و طبق گزارش رسانه‌های پرتغالی و اسپانیایی، اردوی تیم را ترک کرده است. این اتفاق پس از اظهارات ژسوس درباره غیبت رونالدو مقابل دانمارک رخ داده و برخی رسانه‌ها احتمال بازگشت او…</div>
<div class="tg-footer">👁️ 4.93K · <a href="https://t.me/SorkhTimes/141172" target="_blank">📅 10:43 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141171">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rkIObmXqsM864XhA1P7HoN4PspoOG1LJROSgmEr08sfB6UVTulV1NgcKUpraD27vZIpWi_vccvJoVIWDrSQYuceWarpVzmqdLJVQF_3qU4MFbHQRqyLMejuS9JwHEO6OUYycfFndoG7QpB9SXEVCbBZeKy1T4fm15pDTde5fMOZ1Z-9SnQc0CRAPYbGvIuNlquvGMog-2vA053CUgMdL49N0GOmR04vDv2HRDPxmdiL006WnDv5tGWJgBcO9TRjJDVkfqoJgVkscB9mFqosCzA3kVHolCpbs6p4dEr5KsLR0793I4DkBnlC42lM3FFdrf99bzjepOP3bhBhaSXdjlA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
ورزش سه: پوریا لطیفی فر امروز قراره جای پویا پورعلی بازی کنه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5K · <a href="https://t.me/SorkhTimes/141171" target="_blank">📅 10:29 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141170">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">🚨
دعوا در تراکتور بالا گرفت
❌
شکایت بیرانوند از کریمی مدیرعامل باشگاه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5K · <a href="https://t.me/SorkhTimes/141170" target="_blank">📅 09:35 · 17 Mehr 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>

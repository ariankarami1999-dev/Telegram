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
<img src="https://cdn4.telesco.pe/file/FMVs6LjVk_ZM3lb8bBtCzSvVSb4Tq56sDklsN0NVdTrQ2_gPd573KXWqQkT-2fEkGP6U-N1IRApqISpTsh1f6V_PzUCAflNnA2UMn3rsyGQUwiiApFdvaeLNeiV5ElbkZxdem0yRD8rZfjcYSKG7Jr4b6QaLO5um_U6V6KcIrROnc9ZomXjJ9fjhy9zdEfm9ryY51Tt_whEiuXSXh1O78M1mdrYzPSxRs-1qk-CS-Qkiq0H540TzeJHHBuxIbZS-5yigB4dQ4fzrYkAfR6OURzFxhiOL1a49p9auApMfYK3eOaXjX2jEqmXDAwuRy4TriDK5Y1Q647DAMHCuwKJQTw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 🚩سرخ تایمز🚩</h1>
<p>@sorkhtimes • 👥 21.5K عضو</p>
<a href="https://t.me/sorkhtimes" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ﷽ورزشی نویس پرسپولیس👤🎗️«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس.⛔رسانه سرخ تایمز مسئولیتی در قبال تبلیغات ندارد.</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-19 13:54:21</div>
<hr>

<div class="tg-post" id="msg-135411">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">✅
✅
باشگاه الشمال قطر با ارسال ایمیلی به پرسپولیس خواستار جذب اورونوف شد. این تیم اعلام کرد که حاضره 3.5 میلیون دلار برای‌ جذب اورونوف به‌ پرسپولیس پرداخت کنن
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 578 · <a href="https://t.me/SorkhTimes/135411" target="_blank">📅 13:52 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135410">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">🔹
🔹
🔹
🔹</div>
<div class="tg-footer">👁️ 1.3K · <a href="https://t.me/SorkhTimes/135410" target="_blank">📅 13:44 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135409">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">🔹
🔹
🔹
🔹</div>
<div class="tg-footer">👁️ 1.45K · <a href="https://t.me/SorkhTimes/135409" target="_blank">📅 13:43 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135408">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">🔹
🔹
🔹
🔹
#شایعات
🔹
🔹
باشگاه پرسپولیس با رامین رضاییان مذاکراتی انجام داده است
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.45K · <a href="https://t.me/SorkhTimes/135408" target="_blank">📅 13:43 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135407">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">🔴
🔴
دنیل گرا با نظر تارتار در لیست مازاد تیم قرار گرفت.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.76K · <a href="https://t.me/SorkhTimes/135407" target="_blank">📅 13:38 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135406">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">❌
❌
خوبی بازیکن های مثل کسری طاهری پوریا شهرآبادی اینه که هیچ کدوم لیست بزرگ سال پر نمی کنن و همین طور سهمیه لیگ برتر حساب نمیشن هم جوون و آینده دارن
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.91K · <a href="https://t.me/SorkhTimes/135406" target="_blank">📅 13:36 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135405">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">✅
انصافا بعد از سالها تیم داره جووون میشه ...همه بازیکنان خوب و با استعداد و جوان داره جذب میشه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.18K · <a href="https://t.me/SorkhTimes/135405" target="_blank">📅 13:02 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135404">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">🔴
با اعلام‌ ترانسفرمارکت امید عالیشاه از پرسپولیس جدا شد
🔴
خداحافظ کاپیتان...؛ بابت تمام خاطرات خوبی که برامون ساختی ازت ممنونیم.
❤️
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.21K · <a href="https://t.me/SorkhTimes/135404" target="_blank">📅 12:59 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135403">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LEltME2vR8368ptREdgLxb_KKakaOrKEl7MVBvCB88JxvcrEv_m2wE3sAdBCTFFFnERTQHvYuDnzysPNBZ2vBZ6kR7g8rFKHmdEp4BG6zb8zE6Cdzly5FN9LoYLHEgqFPZx_dQ0SdzY9uK-I92SLf0nkl510tgArFBYPw0XkvY0Kh5R0GD1w8sPH2-ve-PFhwVKijqbkomRRJ3AyIBUg4LkCrDaRbU1qjPnWSYg47Fme3IuvYXxLaO-c03J-yEeyJLR0S98ocGMY2MLcO-PZExFTWekyu4GK_SMiUyXXA2pO8NzOaH8WqIzmT2rwAglnxdfRyMEcgUc4SzE-50eKkw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
با اعلام‌ ترانسفرمارکت امید عالیشاه از پرسپولیس جدا شد
🔴
خداحافظ کاپیتان...؛ بابت تمام خاطرات خوبی که برامون ساختی ازت ممنونیم.
❤️
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.25K · <a href="https://t.me/SorkhTimes/135403" target="_blank">📅 12:56 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135402">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">🔘
🔘
🔘
باشگاه پرسپولیس فردا یعنی روز شنبه مذاکرات نهایی و پایانی خود با دانیال ایری و باشگاه نساجی را انجام خواهد داد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.64K · <a href="https://t.me/SorkhTimes/135402" target="_blank">📅 12:46 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135401">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sjUzOcU3rx7dDJeZcNzyRJZA-3OsuGW6JkhOMJo_rHx_HcKLEAw_Vc6IZwnxFfUFLHw9_4zuBK9t73xdFYO9_GPEn0xvVTim0bCYQNc_CHXSBx_e4PqhxYrQHua_mKFxXift43s9sBBsPnxGAMtR4Tg4_JJ26tCSQJGlRqEXGhuU5GYs-NLTcdzi6vNPd3Kvcc_Rm7G4pqARY9cpVA02dnjOuGd9317w2v1wLpksjyOeH8vxSGsvkeqg2PeCi2ELBR_qAbOibuGd_5e6KwvpMJ4SCdFyiqARKR3pTUZoyLck_iBHk6sDVAtdht1ol6w_VV-Y30LdelegAt_TXEi6Cw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
آقای گل لیگ عراق چرا بدون تیمه
😂
😂
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.31K · <a href="https://t.me/SorkhTimes/135401" target="_blank">📅 12:04 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135400">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">❌
❌
دور جدید مذاکرات با ایری امیدبخش بوده و مسئولان باشگاه به جذب ایری امیدوار شدن/ قدوسی
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.31K · <a href="https://t.me/SorkhTimes/135400" target="_blank">📅 12:01 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135399">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bWPf5lHtzaCWogPX8Fmrm5B74wk-A_JbYWFLKTxz6l7HnAwSCGBXFWQRlSObVweJMFnr3bvEsPS4fpuBk7GVSBh__2k4ZHUata8jPNCfwjWupqKAKESRPx7x5xwHTiQ1hHeHZzOX8GpyoiPZHZdzVhr2h0XA1a48kdRz2vO9a1XOrOn5MUbDNZrglFLRsLTEGbh59Hs0-RRIt9YewKc7n3O-z3O6uF1KZLun85RpwWEfojTrD_O11EMe5QXRbv1H5KeuX-SvRpTxRBUOtFZLczcspNstkmEYusztR-Rt9IEReHMviTBLRt3VpLePIYFMNVqQSUpD6TjwiPqPZpXOPA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
پناه بگیرییییییید، اریک باگناما بازیکن ازاد شد.
🔴
پ.ن اوه اوه .فقط مونده این بیاد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.4K · <a href="https://t.me/SorkhTimes/135399" target="_blank">📅 11:58 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135398">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">💢
💢
💢
🚨
💢
فرهان جعفری ، دانیال ایری و پوریا لطیفی فر سه خرید بعدی هستن
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.37K · <a href="https://t.me/SorkhTimes/135398" target="_blank">📅 11:57 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135397">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">❗️
دیروزگفتیم ابوالفضل‌جلالی قراردادش رو با تیم پرسپولیس بسته فقط‌مدیریت این باشگاه بهش گفته فعلا مصاحبه نکن. حالا با اعلام ایجنتش در ترانسفر مارکت؛ سیدابوالفضل جلالی رسما سرخپوش شد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.03K · <a href="https://t.me/SorkhTimes/135397" target="_blank">📅 10:31 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135396">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">✅
پرسپولیس برای جذب ایری خیلی تلاش میکنه و بسیار خوشبینه/قدوسی
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.12K · <a href="https://t.me/SorkhTimes/135396" target="_blank">📅 10:20 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135395">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">🔴
🔴
دنیل گرا با نظر تارتار در لیست مازاد تیم قرار گرفت.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.08K · <a href="https://t.me/SorkhTimes/135395" target="_blank">📅 10:18 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135394">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">🚨
🚨
طبق گفته مدیران باشگاه یک سری مسائل حقوقی پیش اومده و تا اونا حل نشه از جلالی رونمایی نمیشه
⏺
البته یک منبع دیگه معتقد بود باشگاه میخواد‌ اول تمدید قرارداد میلاد محمدی رو انجام بده و بعد از جلالی رونمایی کنه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و…</div>
<div class="tg-footer">👁️ 5.45K · <a href="https://t.me/SorkhTimes/135394" target="_blank">📅 09:09 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135393">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">✅
ترابی در لیست پرسپولیس نیست
❗️
درحالی که در چند روز گذشته خبرهایی مطرح شده بود که مهدی ترابی مورد توجه مهدی تارتار سرمربی پرسپولیس قرار گرفته اما پیگیری خبرنگار آنا نشان می دهد که ترابی در لیست خرید سرخپوشان نیست و مذاکره ای هم با او نشده است.
✍
خبرگزاری…</div>
<div class="tg-footer">👁️ 5.42K · <a href="https://t.me/SorkhTimes/135393" target="_blank">📅 09:03 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135392">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">❗️
حضور مدایم وحید امیری در تمرینات پرسپولیس
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.35K · <a href="https://t.me/SorkhTimes/135392" target="_blank">📅 09:03 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135391">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">❌
برای تمرین امروز چهارشنبه به بازیکنان  پرسپولیس اطلاع‌رسانی شده و در این بین به ۳ بازیکن دارای قرارداد، گفته شده که تا مشخص شدن وضعیت‌شان، در تمرین شرکت نکنند.
✅
امید عالیشاه، مرتضی پورعلی گنجی و میلاد سرلک این سه بازیکن هستند.
🎗️
«سرخ تایمز» دریچه ای تازه…</div>
<div class="tg-footer">👁️ 5.29K · <a href="https://t.me/SorkhTimes/135391" target="_blank">📅 09:02 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135390">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">linebet.apk</div>
  <div class="tg-doc-extra">53.7 MB</div>
</div>
<a href="https://t.me/SorkhTimes/135390" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🪙
اپلیشیکن اندروید سایت جهانی لاین بت
💳
واریز و برداشت ریالی
🎁
هر پنجشنبه تا سقف ۱۳ ملیون تومان بونوس ورزشی
🔗
بدون نیاز ب فیلترشکن
🤩
آموزش کامل استفاده از اپ
🔜
💰
💰
💰
💰
💰
📱
Telegram Channel
👇
https://t.me/+dukgrB6-zGsyNGM8</div>
<div class="tg-footer">👁️ 5.86K · <a href="https://t.me/SorkhTimes/135390" target="_blank">📅 02:10 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135389">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/P4r1GU16gc54YdWZ4Bi0-YF9RsEtCHZQt_ksT-vIiM5PPAvo4WrnXeRaji364i3nZYAk70m_BP3XGczLekkYM9_X77QG9aKtOSKYrGlKdS8naYx_dfTd7XZ-A5EHbFm0BSj13hc_vrm13XXYIYPE9tM-KLatX-onGYM1Wk0-tqzkerHtAIORoUCik38gtXfT8DlPMvl7mlR9lt6VhzOTd4KGVb30EtrToeHxA04d4p6tAQRd4FMKj6QSp74JAQHyOgJjfCyHEOh2BYRKgS6kL-BcbL5AxdP_UO8dRWlLfu78MCkTuzppZ9IifDFIHJeAGKRJ08Pi71yH3tjlQw-eug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
اولین سایت جهانی برای کاربران ایران با واریز برداشت مستقیم
⬇️
🪙
سایت بین المللی و معتبر لاین
بت
❤️‍🔥
اسپانسر لیگ  فرانسه
💳
واریز و برداشت ریالی
👀
بازگشت باخت ب صورت هفتگی
📣
دارای پشتیبانی فارسی فعال
🎁
بونوس
💯
روز های دوشنبه
🎡
کدهدیه ثبت نام
➡️
L5670
🔗
《 لینک سایت برای کاربران ایرانی》
👍
《 دانلود اپلیکیشن اندروید》
❤️
https://t.me/+dukgrB6-zGsyNGM8
🔻
جهت استفاده از وبسایت از آی پی کشورهای آسیایی
🇷🇺
یا کانادا
🇨🇦
، استفاده کنید
Ⓜ️
✔️
آموزش کامل و جامع شرطبندی
👉</div>
<div class="tg-footer">👁️ 5.97K · <a href="https://t.me/SorkhTimes/135389" target="_blank">📅 02:10 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135388">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">❗️
فعلا عکسی از جلالی بیرون نیومده ..شاید هم کلا امروز نبوده
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.48K · <a href="https://t.me/SorkhTimes/135388" target="_blank">📅 00:27 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135387">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">❌
علی بازگشا، سخنگوی باشگاه پرسپولیس: «اینکه پیشنهادی آمده بی‌اطلاعم، اما ما می‌خواهیم اورونوف و سرگیف را حفظ کنیم.»
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.51K · <a href="https://t.me/SorkhTimes/135387" target="_blank">📅 00:26 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135386">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">❌
❌
برگام فیروز کریمی شده کارشناس بازی های جام جهانی کانال  gem tv
😂
😂
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.52K · <a href="https://t.me/SorkhTimes/135386" target="_blank">📅 00:24 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135385">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">💢
💢
💢
🚨
💢
فرهان جعفری ، دانیال ایری و پوریا لطیفی فر سه خرید بعدی هستن
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.46K · <a href="https://t.me/SorkhTimes/135385" target="_blank">📅 00:23 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135384">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">✅
✅
باشگاه پرسپولیس از دنیل گرا و بیفوما هم دعوت کرده برای مذاکره جهت فسخ به باشگاه مراجعه کنند.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.57K · <a href="https://t.me/SorkhTimes/135384" target="_blank">📅 23:43 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135383">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">💢
💢
💢
🚨
💢
فرهان جعفری ، دانیال ایری و پوریا لطیفی فر سه خرید بعدی هستن
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.65K · <a href="https://t.me/SorkhTimes/135383" target="_blank">📅 23:36 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135382">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">❌
❌
اولین بازی یک چهارم امشب انجام میشه ساعت 23/30 فرانسه و مراکش
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.5K · <a href="https://t.me/SorkhTimes/135382" target="_blank">📅 23:31 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135381">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">✅
فووووووووووووری از قدوسی
🔴
حدادی میخواد از بین علیپور و سرگیف یکی رو حفظ کنه و اگه علیپور تمدید کنه سرگیف جدا میشه 🫪
😕
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.46K · <a href="https://t.me/SorkhTimes/135381" target="_blank">📅 23:31 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135380">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">❌
❌
طبق شنیده‌ها هفته آینده جلسه‌‌ای بین ایگور سرگیف و مدیریت باشگاه پرسپولیس برگزار خواهد شد تا مدیریت‌سرخ‌ها این بازیکن رو برای‌موندن دراین باشگاه برای فصل آینده متقاعد کنند. سرگیف بخاطر مسائل خانوادگی قصد داره فصل جدید رو در لیگ برتر ازبکستان بازی کنه. …</div>
<div class="tg-footer">👁️ 6.54K · <a href="https://t.me/SorkhTimes/135380" target="_blank">📅 23:26 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135379">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PCtaeCHXvQWQEkVmJCJrJQD8H8zZqAIrp-40xRPtCEBxXYuQX5duCoSWYVxqWzXs5MDBl66sqqH_4rDxU-MyKJpIJayCkRAw1zvSpFCdBWxOMoiF-d9IfFOPfTb_JqUKh_kleEwdL0e3TGaNzAsPafmaNnM1a3MkG_bJc-LAoun-Jkia5zrWmPfVCKh5yWpUJWCA9Wzjj3bVFZ4slrqwZalrnU6RNmkx5XLh5OYS9eBnJi_5sk81okpQfRciSPoDBXMF8j6Uc154njmDemQg283zsBbDmHSEjgHe7fW-1i-vi3n7wxAm8fbIRNciVya2iqHfzXp5QRvOvFtdOt6c-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
❌
برگام فیروز کریمی شده کارشناس بازی های جام جهانی کانال  gem tv
😂
😂
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.64K · <a href="https://t.me/SorkhTimes/135379" target="_blank">📅 23:24 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135378">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">✅
فرشید حقیری :
🔴
با اسامی دارن بازیتون میدن، ترابی قرارداد داره و نمیاد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.59K · <a href="https://t.me/SorkhTimes/135378" target="_blank">📅 22:54 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135377">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">💢
هم اکنون فعالیت هواگردهای ارتش ایالات متحده در جنوب ایران
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.64K · <a href="https://t.me/SorkhTimes/135377" target="_blank">📅 22:29 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135376">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">❗️
برنامه کامل مرحله ¼نهایی جام‌جهانی
😀
فرانسه
🆚
مراکش
😀
🗓
پنجشنبه ۱۸ تیر ساعت 23:30
🇪🇸
اسپانیا
🆚
بلژیک
🇧🇪
🗓
جمعه ۱۹ تیر ساعت 22:30
🏴󠁧󠁢󠁥󠁮󠁧󠁿
انگلیس
🆚
نروژ
😀
🗓
يکشنبه ۲۱ تیر ساعت 00:30 بامداد
🇦🇷
آرژانتین
🆚
سوئیس
😀
🗓
يکشنبه 21 تیر ساعت 04:30 بامداد
🎗️
«سرخ تایمز»…</div>
<div class="tg-footer">👁️ 6.64K · <a href="https://t.me/SorkhTimes/135376" target="_blank">📅 22:23 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135375">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">❗️
❗️
ابوالفضل جلالی در تمرین امروز پرسپولیس شرکت کرد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.65K · <a href="https://t.me/SorkhTimes/135375" target="_blank">📅 22:00 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135374">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/H5U2pp5xN72UV9NpiqOzKHdws32hNZibImkFnwgCD-kj8wJCTtd7EwjaM5J3bXr9FvXx5I3yPdLnaLECRSpujhz_Mx9Uc5qlIi4oAoPKxSoIoXawqYAn44fdOVLusrhOsYu1cl7T6IQSBsK1adLKoXLBFd0lTbk6AaEarzw2mtupgtbv-Vk-0nL7cHTc5IgqWjDg53CyBAErxJKAI--BK_3a1OBvD_3Lys0KHC559cDE5xZoquHzCro-vaXDBFsBh1_tlEueS4bWU8ZZrvHbUsgKRNFlMQhVD8Rh4De5vYvKKEIk5fcnjufb7aVBpqrrxPO0olEcBFcNudOu04qy-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
از تمرین امروز پرسپولیس
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.48K · <a href="https://t.me/SorkhTimes/135374" target="_blank">📅 21:55 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135373">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">❌
❌
رسانه‌های مملکت: پرسپولیس به علیپور یه رقم مشخص پیشنهاد داده و گفته اگه بیشتر از این بخوای میتونی با یه خداحافظی خوشحالمون کنی
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.19K · <a href="https://t.me/SorkhTimes/135373" target="_blank">📅 21:52 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135372">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vsvkiNSMBIEPYeIpI802F82yCzDSANEjkOuFKfYDB2NLBY-E9rZ1lHUv5rjTRCZBIlgMQVYowBSSGEtcsoW2tKMH5IQi-xNK0037ubLR4up0-CJd4a7OvBpSiAUec5NodGS5NFZioeQ533ahCwst6mHxmwvOXJBBbO99GTyYis0CXEyI5pZyo8AG_5V2ZyGQZnN90CKa4V1h6uk0y45m_qW935qlQ_JLFn_JbNTMPjesdAsa9Jj3hBY2fMtTt8pin0eqzp2T1cJjajaiSvMlldYc7Ezm6UylJYBOBAXA7raxyfWt1rJtx-7OwrMIMVh44I_uS7zJqEeWDtEVJky0YQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❗️
حضور مدایم وحید امیری در تمرینات پرسپولیس
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.25K · <a href="https://t.me/SorkhTimes/135372" target="_blank">📅 21:51 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135371">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">🔴
🔴
محمدحسین صادقی
❌
: برای شفای مادرم دعا کنید  صادقی همچنان در تمرینات تیم پرسپولیس غایب هست
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.12K · <a href="https://t.me/SorkhTimes/135371" target="_blank">📅 21:49 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135370">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/THKz6q2axkgMuqUJ0yQh_gy7MBm8nw3_RQIbFcuNqxDt4Jneo44aYLQUMKzGrxMRG0W_ct1nC7N8kKf4fQWqrUbCL0pDKRrzHfRWcZm75INaydAyYFV08uAe9EqNt4lbYc3e5Hb0MQ2d8UlAvAe3OTa1lv-m_E3L8JpPAxza_qasEYxHpcNMYiN3O-_WvGxYzJ-57euAgK6kd3J-xov_UVm8SBZC3JWMfQp_1hDkdrbYjr34LaRCURu-0IYaoCpFm81i0O9Hj_0wlJjS0aej4cUx1LKDyb5IheTudknvo4u7jZpEl0mbbu5jKxFrxTg1kJbsakiUejrAMIRQV4lI5g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💢
هم اکنون فعالیت هواگردهای ارتش ایالات متحده در جنوب ایران
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.96K · <a href="https://t.me/SorkhTimes/135370" target="_blank">📅 21:46 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135369">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">❌
باشگاه‌الوحده 200 هزار دلارتخفیف داده و در تماس با نماینده محمد قربانی اعلام کرده هر باشگاه ایرانی 1.8 میلیون دلار پرداخت کنه رضایت نامه قربانی رو صادر میکنیم.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.25K · <a href="https://t.me/SorkhTimes/135369" target="_blank">📅 21:16 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135368">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">🔴
مهدی تارتار کادر پزشکی گل‌گهر رو به باشگاه پرسپولیس معرفی کرده و احتمال بسیار زیاد تمامی کار پزشکی گل‌گهر به پرسپولیس خواهند آمد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.22K · <a href="https://t.me/SorkhTimes/135368" target="_blank">📅 21:15 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135367">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">چنل آرون تیپ بمبه بمب
🧨</div>
<div class="tg-footer">👁️ 6.24K · <a href="https://t.me/SorkhTimes/135367" target="_blank">📅 20:58 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135366">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qlhIyErCb-PYQubc8E3gkEGUYe28T6BaYm5lexb8H2m6J0emzf0-O2ZXhHXG_wZBxLf2HJ1oQwXeNrIYxy1c8veK7v5zXVPeCFmwVtE5isJwRHr34zrigNwWo9gwDRKjoc5oO0yu-jgO4690Waxms_5lTReAryPekhYZrky4U3XKchzFY50Cy9Q4HApTm3CtcN1HoEe2GHG3253gO7X-7zQWVH7MsaJK1rz5HXqAZTQIImrU3fiRA1hHO-XK8MhaYv7nQHSCfn7aGbQhyz_2Wf7Bl-EQCfLMD45nj8U5ARBNCxFQ42t5iIVaVY2gaN0iTAsp9QdSqc3BnKjOfRqfEw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فک کنم اگه هرشب با ۱۰۰ هزار تومن میومدین چنل بت ما ، شبی بالای ۲ میلیون سود کرده بودین مثل دیشب:)
😊
😂
میگی ن ؟ بیا تو چنلمون و ببین
🔥
@aron_tip
@aron_tip
@aron_tip
@aron_tip
@aron_tip
@aron_tip</div>
<div class="tg-footer">👁️ 6.49K · <a href="https://t.me/SorkhTimes/135366" target="_blank">📅 20:58 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135365">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">❌
تصاویری از حضور بازیکنان تیم پرسپولیس برای انجام نخستین تمرین برای شروع فصل جدید که چهره ها نشون از روحیه و شادابی بچه ها داره با کادر جدید
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.46K · <a href="https://t.me/SorkhTimes/135365" target="_blank">📅 20:28 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135364">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">✅
محمدحسین صادقی پس از چند روز عدم حضور در تمرینات پرسپولیس، اعلام کرد به دلیل مشکلات خانوادگی فعلاً به تهران نمی‌آید.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.59K · <a href="https://t.me/SorkhTimes/135364" target="_blank">📅 20:20 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135363">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dMz--TFEaGxOlVxSukfi7xhJ-he11HeBnxRrPjSMqYK4ztVf-gwUxWcJfNxxBALZGxHGvLooPT40W8vdvwIqiaQMXZsbPhCTq5ADKAyLBaqupV65iMsWf4OUYMCV41eEaCTfisS-szOuHGbplr_iapUD4uhEpiN4qnpcKusb4ohvly5pNhTUucQZWTKLgFpWpODAQXlxWZi04rIVspHHbrEaekSLxiR0nJqdDzj6tifGnlzKXUJLg5R_TFiPALF6iKeLNOGjTifZJFWBrmL9d8N3fAvbojkEzs153em0FcmBoacd7U15zjKr42l_-kAFMhZkfNK7Q4f5_pq67Lv6Qg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❗️
این چرا اینطوری شد
✅
پ.ن بازیکن آزاده ولی کسی گردنش نمیگیره
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.58K · <a href="https://t.me/SorkhTimes/135363" target="_blank">📅 20:13 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135362">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">🔴
محمد قربانی: با باشگاه الوحده امارات قرارداد دارم. رضایت نامه من برای باشگاه های ایرانی 2 میلیون دلار و برای باشگاه های خارجی 3 میلیون دلار است
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.42K · <a href="https://t.me/SorkhTimes/135362" target="_blank">📅 19:59 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135361">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">❗️
ورزش سه :تارتار لیست مازادش را به باشگاه تحویل داد
❌
امید عالیشاه
❌
سروش رفیعی
❌
مرتضی پورعلی‌گنجی
❌
میلاد سرلک
✅
✅
مدیران باشگاه این تصمیم را به بازیکنان اطلاع داده‌اند و این چهار نفر اجازه حضور در تمرینات را ندارند.
🎗️
«سرخ تایمز» دریچه ای تازه به…</div>
<div class="tg-footer">👁️ 6.67K · <a href="https://t.me/SorkhTimes/135361" target="_blank">📅 18:41 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135360">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/A_-_HXWuHF5K_VV-y_P_RkYgLOppGW3wDsB32H9nWcpXbQw2zMHEnmAwzAjKgBHWh6iutvsmr9nnSWfTu4_YUbrxyJNh1NMcDo9oJyNwAp7ikwG5kC8m-c3g18yGfxpmxvO0sVxSnPLuBX1kI_12VFCxyQM0hhiQ6bdaayTYNzzsM3lRFmwg-G6keGiTatgGXAbw8MN9b1agOnBOnsOkwKk2v64ZsPU-ulKAA0hbvXMwQ8keUsHGPdfn2vMlCMiiKYVM3NLiMBpyQJs4SVGCj8npBn_Vx5Q2ayIu1ON0oFLHuodx0gSVb64pVw7jHLKKYzsuDOND0Wa2QETpWI8HeQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
سنگین ترین و غمگین ترین عکسی که تو دو هفته اخیر میتونستین ببینین!
❤️‍🩹
🤭
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.59K · <a href="https://t.me/SorkhTimes/135360" target="_blank">📅 18:29 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135359">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/75bef21d0f.mp4?token=QycmKx3Dt-3UBFIbw9Ir1VVW_FfWrqshG32-LbzOHbipqcyfFeOC4DeyE_OPIt6F0rchLjOWXG6ik8xqCATyb1nUh6OrwfSISiDIZk8a7qbtqN8mhWajRNbJsqvNVhBFHIqHmkXsvcu3nFDEbeJY0ymkFSBTebyafIX67yLJuJQbOtcZ419-SZrBLyvvUjzWqfw8CCfxVdm9YhtjVdmCFtl7J10yMqpWFDw_zTDY9loYURyrVh7ihtvwQ3uMBHotju2mHg-G4ZsdnVagCVuh0x14MNzClm16lohFHH-T4iL5eNjYuw5qmFwxAKv3FsUVpmK_h34T6iNeRZNKznj6Zg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/75bef21d0f.mp4?token=QycmKx3Dt-3UBFIbw9Ir1VVW_FfWrqshG32-LbzOHbipqcyfFeOC4DeyE_OPIt6F0rchLjOWXG6ik8xqCATyb1nUh6OrwfSISiDIZk8a7qbtqN8mhWajRNbJsqvNVhBFHIqHmkXsvcu3nFDEbeJY0ymkFSBTebyafIX67yLJuJQbOtcZ419-SZrBLyvvUjzWqfw8CCfxVdm9YhtjVdmCFtl7J10yMqpWFDw_zTDY9loYURyrVh7ihtvwQ3uMBHotju2mHg-G4ZsdnVagCVuh0x14MNzClm16lohFHH-T4iL5eNjYuw5qmFwxAKv3FsUVpmK_h34T6iNeRZNKznj6Zg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
سعید مهری : برای جلالی آرزوی موفقیت دارم؛ بازیکن پرحاشیه‌ای نبوده و به نظرم حتما موفق می‌شود و توانایی فوق العاده داره و هواداران پرسپولیس با آغوش باز او‌ را می‌پذیرند
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.44K · <a href="https://t.me/SorkhTimes/135359" target="_blank">📅 18:25 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135358">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">❌
❌
گلگهر سیرجان خواهان جذب مجتبی فخریان شد
🔴
مایل به معاوضه با پوریا لطیفی فر؟
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.75K · <a href="https://t.me/SorkhTimes/135358" target="_blank">📅 17:55 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135357">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">🚨
باشگاه سپاهان که تمایل به جذب نعمتی داشت، طی روزهای اخیر مذاکراتی با این ملی‌پوش ایران انجام داد و به توافق نهایی دست یافت تا خط دفاعی‌اش را با جذب او تقویت کند.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.58K · <a href="https://t.me/SorkhTimes/135357" target="_blank">📅 17:53 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135356">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">❗️
ورزش سه :تارتار لیست مازادش را به باشگاه تحویل داد
❌
امید عالیشاه
❌
سروش رفیعی
❌
مرتضی پورعلی‌گنجی
❌
میلاد سرلک
✅
✅
مدیران باشگاه این تصمیم را به بازیکنان اطلاع داده‌اند و این چهار نفر اجازه حضور در تمرینات را ندارند.
🎗️
«سرخ تایمز» دریچه ای تازه به…</div>
<div class="tg-footer">👁️ 6.68K · <a href="https://t.me/SorkhTimes/135356" target="_blank">📅 17:05 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135355">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">❌
❌
گلگهر سیرجان خواهان جذب مجتبی فخریان شد
🔴
مایل به معاوضه با پوریا لطیفی فر؟
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.54K · <a href="https://t.me/SorkhTimes/135355" target="_blank">📅 17:02 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135354">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">❗️
ورزش سه :تارتار لیست مازادش را به باشگاه تحویل داد
❌
امید عالیشاه
❌
سروش رفیعی
❌
مرتضی پورعلی‌گنجی
❌
میلاد سرلک
✅
✅
مدیران باشگاه این تصمیم را به بازیکنان اطلاع داده‌اند و این چهار نفر اجازه حضور در تمرینات را ندارند.
🎗️
«سرخ تایمز» دریچه ای تازه به…</div>
<div class="tg-footer">👁️ 6.63K · <a href="https://t.me/SorkhTimes/135354" target="_blank">📅 16:55 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135353">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BdUbAask9lYw46WviFXt9MrtCXCHdYtm_RGTvn0vfo29HGapSprw1Tk3XUEUMyip1fjfQ5bQan6JvzYgwdLWmwbXqlVbo8yo3CFb9J4SOd0pcKfSvkkng-x92cmeYhWDHZz3QBuWY7ihqii0QvzKx3K43wStoa__DoiLWS1-CKsTBrxzkIOgxel_sKcY-rSV3AeBYey-isew_vf0vdrxu2kTP7EyaqyLdEAXrPq5rbwWuolz8bpJRWSxBU0ARRX2G6vnbdW6AFVBVYpGyesiySkIyo6Lg4Rzixkt5VUDJ5k2m4SNoe76LATEWz4-BGItqvY-MzJbz8LzfDRPAb7t5A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🤩
#اختصاصی_سرخ_تایمز | #فوری
🤫
🏅
به گزارش رسانه «سرخ تایمز» مدیران باشگاه پرسپولیس با نظر مهدی تارتار با این چهار بازیکن وارد مذاکره شدند.
⬅️
مجید عیدی
⬅️
محمد قیرشی
⬅️
پوریا پورعلی
⬅️
پوریا شهرآبادی
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس…</div>
<div class="tg-footer">👁️ 6.63K · <a href="https://t.me/SorkhTimes/135353" target="_blank">📅 16:53 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135352">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">✅
✅
ایگور سرگیف مهاجم ازبکستانی پرسپولیس دوست دارد از تیم جدا شود!
⚠️
اما مهدی تارتار او را برای فصل آینده میخواهد و روی او حساب باز کرده است
👀
ایگور یکسال دیگه با پرسپولیس قرارداد دارد //,تسنیم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس…</div>
<div class="tg-footer">👁️ 6.24K · <a href="https://t.me/SorkhTimes/135352" target="_blank">📅 16:53 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135351">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">❗️
❗️
تارتار خواسته امروز از جلالی هم رونمایی بشه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.3K · <a href="https://t.me/SorkhTimes/135351" target="_blank">📅 16:50 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135350">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">❌
تایید شد
🔴
پوریا شهرآبادی با قراردادی ۴ ساله به پرسپولیس پیوست ‌
🔴
باشگاه پرسپولیس پوریا شهرآبادی، مهاجم ۲۰ ساله و ملی پوش تیم گل گهر سیرجان را با عقد قراردادی چهار ساله به خدمت گرفت.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.43K · <a href="https://t.me/SorkhTimes/135350" target="_blank">📅 16:49 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135348">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vDlnZTpR_X5af5xEM5HXFk9wKMSNwrFS2b5rfDDhbCFmy-iEWq4p2qR5qCuW1ROy4D3pwb3bEx0TBUpriUIfAQLg1MKiCTHsaWrYVKT9F2LKAkyPV9On936ZsTC6T8KmPY332UGvv9D_mKsP9XjgOwNmTaNrDNKdJmmOGSChdo_y7L47cjzqNdyXObQVZ7SLQd6YEqT88hTWCSfRBYFH_jRsQdfCf95bd1rIAGQllPv8qcjm1dkJ4y3ghBYXdh4erjqFrGArD19UW5rh0q_MoqfSPB8puR-3IARAw4Mz60to8mR93a5AEGNFAI7uk7TWE_k_KoajhbMR63uAeTs2WQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❗️
شهرابادی، طاهری، پورعلی و جلالی پوستر رونماییشون آمادست و فقط منتظر تأیید حدادی هستن
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.64K · <a href="https://t.me/SorkhTimes/135348" target="_blank">📅 16:41 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135346">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">❗️
❗️
در حال حاضر دو طرف مشغول حمله به هم هستند ...هم داریم میخوریم هم داریم می‌زنیم ...اوضاع خیلی بدی شده ..حملات سنگینه ...احتمالا به پایتخت برسه حملات ..خدا به همه رحم کنه تو این فشار سنگین اقتصادی
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس…</div>
<div class="tg-footer">👁️ 6.45K · <a href="https://t.me/SorkhTimes/135346" target="_blank">📅 15:44 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135345">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">❗️
میلاد سرلک پس از جدایی از پرسپولیس بصورت فشرده درحال مذاکره با گل گهر سیرجان است و اگر اتفاق خاصی رخ ندهد این بازیکن بزودی به جمع سیرجان ها اضافه خواهد شد.
🔴
🔴
همچنین گفته میشه مذاکرات امید عالیشاه با مدیران نساجی مازندران مثبت پیش رفته و اگر یکسری مسائل…</div>
<div class="tg-footer">👁️ 6.78K · <a href="https://t.me/SorkhTimes/135345" target="_blank">📅 15:07 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135344">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">❗️
❗️
فرشید حقیری: حبيبی‌نژاد از پرسپولیس پیش‌پرداخت گرفت، ولی تارتار گفت نمیخوامش و کنسل شد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes.</div>
<div class="tg-footer">👁️ 6.74K · <a href="https://t.me/SorkhTimes/135344" target="_blank">📅 15:05 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135343">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">✅
فرشید حقیری گفته مهدی ترابی هیچ‌جوره به پرسپولیس نخواهد اومد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.56K · <a href="https://t.me/SorkhTimes/135343" target="_blank">📅 15:03 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135342">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">✅
سازمان ملل : شاید باورتون نشه، بخاطر درگیری‌های مجدد تو خلیج فارس، ایندفعه خیلی بیشتر ازقبل نگرانیم.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.5K · <a href="https://t.me/SorkhTimes/135342" target="_blank">📅 14:58 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135341">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">✅
ترامپ: این اقدام، تلافی بمباران کشتی‌ها توسط ایران در دیروز است. اگر این اتفاق دوباره تکرار شود، اوضاع بسیار وخیم‌تر خواهد شد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.37K · <a href="https://t.me/SorkhTimes/135341" target="_blank">📅 14:56 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135340">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">❗️
بدنساز یونانی پرسپولیس پنجشنبه وارد ایران می‌شود
🔴
پس از انتخاب مهدی تارتار به عنوان سرمربی پرسپولیس، وی در حال تکمیل اعضای کادر فنی خود است. پیش از این حضور وحید فاضلی، علیرضا محمد و اینانلو در کادر فنی سرخ‌پوشان قطعی شده و احتمال حضور کریم باقری هم در…</div>
<div class="tg-footer">👁️ 6.31K · <a href="https://t.me/SorkhTimes/135340" target="_blank">📅 14:52 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135339">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">🔴
تیتر روزنامه گل: «گل‌گهر به پرسپولیس پیوست!»
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.28K · <a href="https://t.me/SorkhTimes/135339" target="_blank">📅 14:51 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135338">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">melbet.apk</div>
  <div class="tg-doc-extra">52.1 MB</div>
</div>
<a href="https://t.me/SorkhTimes/135338" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">✈️
اپلیکیشن MelBet
🥇
🎁
کد هدیه 100 دلاری:
Sport100
🔒
برای تعیین رمز ورود حداقل از 8 کاراکتر و حروف بزرگ و کوچک انگلیسی و اعداد انگلیسی استفاده کنید، مانند Hamid120
🇮🇷
برای تغییر زبان برنامه، زبان موبایل خود را تغییر دهید.
✅
ورود به اپلیکیشن بدون فیلترشکن</div>
<div class="tg-footer">👁️ 6.16K · <a href="https://t.me/SorkhTimes/135338" target="_blank">📅 14:49 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135337">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/HCUTalS-LfJrUFKDpJEj2_L3T5Fd0id4UQkHKkI7AneRltFMCUzTc2REh8Q6s8KelbvoTP4BnkE_KXaC49j5e08Hh3xFFNgTxsdafUDdZ3rCwKpCfZCM1R1JwbNZGHkQvYfvKH-tmk5O744wt4qSxbXcy6Nim9QlSO218HjqpY5ZV2_7Wg_cUdDifqSq4suLXiLRcoHetb82LSmCnxN5K7Qaq8KR9F4HobrzzgtSbeRzMmWbBunhttWDtx30-frWH4HDdu4z4wxE4mEB7uNYMqpa_QXAolZiN7e_R13IWYUoKmh_pv0BVUyIjhR4sDKnDjduVi2cuW8omaMTebm8tQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">▶️
بازی فوق حساااااس
فرانسه
و
مراکش
رو با آپشن های تخصصی در
MelBe
t پیشبینی کنید!
🆕
💵
امکان شارژ
کارت بکارت
و
هات ووچر
🎁
قرعه کشی و آفر های جذاب با جوایز ویژه
📱
کاملترین برنامه موبایل
🤝
اسپانسر رسمی جام جهانی
🇮🇷
پشتیبانی از زبان فارسی
✍️
حرفه ای، مطمئن و در کلاس جهانی پیشبینی کنید!
برای ورود به سایت فیلترشکن خود را خاموش کنید!
‌
🌐
Link
🔜
MelBet1.net
🌐
‌
Link
🔜
MelBet1.net</div>
<div class="tg-footer">👁️ 6.35K · <a href="https://t.me/SorkhTimes/135337" target="_blank">📅 14:49 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135336">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">❌
باشگاه پرسپولیس در تلاشه تا مهدی ترابی رو به پرسپولیس برگردونه.
🔴
البته ترابی مشکل سربازی هم داره و باید این مساله حل بشه.///خرمی
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.25K · <a href="https://t.me/SorkhTimes/135336" target="_blank">📅 14:31 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135335">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">✅
طبق‌شنیده‌ها: مدیریت پرسپولیس پیش از انتخاب مهدی تارتار بعنوان سرمربی خود؛ با ایجنت هادی‌حبیبی‌نژاد مذاکرات‌ مثبتی داشت و حالا درصورتیکه‌ تارتار تایید کنه هادی پرسپولیسی میشود.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.49K · <a href="https://t.me/SorkhTimes/135335" target="_blank">📅 14:11 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135334">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">✅
علیرضا کوشکی به نوعی فوتبال خودش رو مدیون مهدی تارتار هست
❗️
وقتی فقط ۲۰ سال سن داشت تارتار فیکس میزاشتش تو ترکیب پیکان و کوشکی رو به فوتبال ایران معرفی کرد
❌
باید ببینیم تارتار میتونه کوشکی رو راضی کنه بیارتش پرسپولیس یا نه!
✅
گرچه تاجرنیا همه توانش رو میزاره…</div>
<div class="tg-footer">👁️ 6.68K · <a href="https://t.me/SorkhTimes/135334" target="_blank">📅 13:58 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135333">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">❌
❌
گفته میشه شانس مازیار زارع و مهدی تارتار نسبت به مابقی گزینه های داخلی بیشتره!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.83K · <a href="https://t.me/SorkhTimes/135333" target="_blank">📅 13:55 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135332">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">❌
محمد قربانی: خودم داشتم بعد از جام جهانی به اروپا بروم. درحال حاضر سه پیشنهاد خوب از اروپا دارم اما خب چون مبلغ رضایت نامه بالا است باشگاه ها کمی مردد میشوند. باید ببینم تصمیم باشگاه الوحده چه خواهد بود و تابع تصمیمات این باشگاه هستم
🎗️
«سرخ تایمز» دریچه…</div>
<div class="tg-footer">👁️ 6.87K · <a href="https://t.me/SorkhTimes/135332" target="_blank">📅 12:39 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135331">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">❗️
❗️
لیست تیم ملی امید اعلام شد.
❌
در این لیست 4 بازیکن از پرسپولیس به تیم ملی امید دعوت شدند.
🔴
امیرحسین محمودی
🔴
علیرضا همایی فرد
🔴
سهیل صحرایی
🔴
فرزین معامله گری
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.94K · <a href="https://t.me/SorkhTimes/135331" target="_blank">📅 11:58 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135330">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">❌
برای تمرین امروز چهارشنبه به بازیکنان  پرسپولیس اطلاع‌رسانی شده و در این بین به ۳ بازیکن دارای قرارداد، گفته شده که تا مشخص شدن وضعیت‌شان، در تمرین شرکت نکنند.
✅
امید عالیشاه، مرتضی پورعلی گنجی و میلاد سرلک این سه بازیکن هستند.
🎗️
«سرخ تایمز» دریچه ای تازه…</div>
<div class="tg-footer">👁️ 7.08K · <a href="https://t.me/SorkhTimes/135330" target="_blank">📅 10:32 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135329">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">🔴
محمد قربانی: با باشگاه الوحده امارات قرارداد دارم. رضایت نامه من برای باشگاه های ایرانی 2 میلیون دلار و برای باشگاه های خارجی 3 میلیون دلار است
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.79K · <a href="https://t.me/SorkhTimes/135329" target="_blank">📅 10:29 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135328">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">✅
✅
بازم تایید شد
✅
محمد قربانی: بله باشگاه پرسپولیس به صورت جدی دنبال جذب من است. اما مبلغ رضایت نامه من بالا بوده و این کار را کمی سخت کرده است
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.88K · <a href="https://t.me/SorkhTimes/135328" target="_blank">📅 10:28 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135326">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">❗️
❗️
شنیده ها : فوری؛ پیغام‌جدید محمد قربانی به پیمان‌حدادی مدیرعامل باشگاه پرسپولیس: پیشنهاد مالی شما رو پذیرفته‌ام، رضایت نامه ام رو بگیرید روز شنبه قراردادم رو امضا خواهد کرد.
❌
❌
پیشنهادمالی‌پرسپولیس: سه ساله بوده. سال اول 80، سال دوم 110 و سال سوم 150 میلیارد…</div>
<div class="tg-footer">👁️ 6.81K · <a href="https://t.me/SorkhTimes/135326" target="_blank">📅 10:24 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135325">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">❌
فورییییی به نقل از CBS :
🔴
علیرضا فغانی قضاوت فینال جام جهانی 2026 برعهده خواهد داشت !
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.66K · <a href="https://t.me/SorkhTimes/135325" target="_blank">📅 10:03 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135324">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">❗️
تارتار قراره در تمرینات نظرشو راجب باکیچ و بیفوما اعلام کنه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.74K · <a href="https://t.me/SorkhTimes/135324" target="_blank">📅 09:37 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135323">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EeZcMBN8446s15_TysTk5TbPzhQt5z5G3ONL7lzExDKAa3Lil6oI4pEj8yKzCqXrJxCjxqEB1YaN784prvmMwc9ak1PZz2dGsIbhf0-uPrTDk5hEyXxUaID02j_zf91EgbRpxAY8cdS2rw8enob1PH-Bhk-8WM6MBr1Iv7SvEFzXOfX-lITPTvLmqdmoImbLwSumPiPLpLBTwHIdCj4thnBLRC4ka3oYJHm0hbC9hysL7HiBGEa6rDlQsTmM4mazNdBCrpz3xgKqqeDgeHZKEDdCKT-9Lo4DvlEVYP_jJM1064KurmUfwfb_okES4yNc95QnmJ615y65iXa4r_t5tA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
تیتر روزنامه گل: «گل‌گهر به پرسپولیس پیوست!»
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.64K · <a href="https://t.me/SorkhTimes/135323" target="_blank">📅 09:27 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135322">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">✅
ترامپ: این اقدام، تلافی بمباران کشتی‌ها توسط ایران در دیروز است. اگر این اتفاق دوباره تکرار شود، اوضاع بسیار وخیم‌تر خواهد شد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.46K · <a href="https://t.me/SorkhTimes/135322" target="_blank">📅 09:22 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135321">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">❌
مهدی زارع، گزینه جدید پرسپولیس!
🔴
🔴
طبق شنیده ها، مدیران پرسپولیس مذاکرات برای جذب مهدی زارع، مدافع ایرانی تیم اخمت گروژنی روسیه را آغاز کرده‌اند و این بازیکن یکی از گزینه‌های اصلی سرخ‌ها برای تقویت خط دفاعی محسوب می‌شود.
🎗️
«سرخ تایمز» دریچه ای تازه به…</div>
<div class="tg-footer">👁️ 6.69K · <a href="https://t.me/SorkhTimes/135321" target="_blank">📅 09:11 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135320">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ukym9YHZT5mEHn_OD9vGQb6YK91Svxzz4r_fB4VRyeZOBv89V0qDZPp-s8bNoXvY6Nllwt9AA71KhoKuEOq-hksDLjgeNudawpv3-YZE5Szwkj6j-GVdd-GzNqMESkQ7Sc1-NnvJokWrVPaoHHTU1YHprpN3JAl5Jbr-C3JruwFLd5OG8pycH2iIX30FLBLVIlPiKuFXXiHFuaTJn859JbjLa-NX8nVdygt-syDyOru-e7NKbCs6nvWB_5dcyEa-rjWqnw3Dsd0ABazcY1TOa43sI5gSjca_YMlo1UwGQVj5q3QaHcoBlwCShz1PJQkj1fB8LMzdZZaLfH5JOZDOYQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
مهدی تارتار کادر پزشکی گل‌گهر رو به باشگاه پرسپولیس معرفی کرده و احتمال بسیار زیاد تمامی کار پزشکی گل‌گهر به پرسپولیس خواهند آمد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.68K · <a href="https://t.me/SorkhTimes/135320" target="_blank">📅 09:07 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135319">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">linebet.apk</div>
  <div class="tg-doc-extra">53.7 MB</div>
</div>
<a href="https://t.me/SorkhTimes/135319" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🪙
اپلیشیکن اندروید سایت جهانی لاین بت
💳
واریز و برداشت ریالی
🎁
هر پنجشنبه تا سقف ۱۳ ملیون تومان بونوس ورزشی
🔗
بدون نیاز ب فیلترشکن
🤩
آموزش کامل استفاده از اپ
🔜
💰
💰
💰
💰
💰
📱
Telegram Channel
👇
https://t.me/+dukgrB6-zGsyNGM8</div>
<div class="tg-footer">👁️ 6.56K · <a href="https://t.me/SorkhTimes/135319" target="_blank">📅 01:28 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135318">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/miawRsilmOk6djIJSOAQduxTi2vtxQuHeXHNtijfA7tCvGidoKHwnspx_cDP9lFahnGAta4D0i1Vj1bFzw91i5m985_OmSFMuJQyp3hBYbLOf2OLmGtZpEwKCNYKgrpeRtX_AYqlrSx8bfkXnuY0HSF1l0a5U1PyBDYb0V1dPHlSl3su1GfDafHUIno994kkBHjqN0EW3vFBpO7qFkPrV6dfWMxFpEx6XcY9GVBicdQmv2gmws9ze4X1HPhakzzXoYvm5VfWLxK3APLmp7ZgB6G8Lu3rFJ4G22DC2Q1zRoBCUg9E_msg03X1mm8XraGY1K350VL1tE_VKjXfyysY6Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
اولین سایت جهانی برای کاربران ایران با واریز برداشت مستقیم
⬇️
🪙
سایت بین المللی و معتبر لاین
بت
❤️‍🔥
اسپانسر لیگ  فرانسه
💳
واریز و برداشت ریالی
👀
بازگشت باخت ب صورت هفتگی
📣
دارای پشتیبانی فارسی فعال
🎁
بونوس
💯
روز های دوشنبه
🎡
کدهدیه ثبت نام
➡️
L5670
🔗
《 لینک سایت برای کاربران ایرانی》
👍
《 دانلود اپلیکیشن اندروید》
❤️
https://t.me/+dukgrB6-zGsyNGM8
🔻
جهت استفاده از وبسایت از آی پی کشورهای آسیایی
🇷🇺
یا کانادا
🇨🇦
، استفاده کنید
Ⓜ️
✔️
آموزش کامل و جامع شرطبندی
👉</div>
<div class="tg-footer">👁️ 6.78K · <a href="https://t.me/SorkhTimes/135318" target="_blank">📅 01:28 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135317">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">🔴
🔴
مقام ارشد اسرائیلی به الحدث: ترامپ در تماس تلفنی به نتانیاهو اعلام کرد که حملات امشب به ایران تمام عیار خواهد بود.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.54K · <a href="https://t.me/SorkhTimes/135317" target="_blank">📅 01:20 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135316">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">❗️
❗️
طاهرخانی: کوشکی رقم خیلی بالایی درخواست کرده و باشگاه داره باهاش مذاکره میکنه تا قیمتشو کم کنه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.83K · <a href="https://t.me/SorkhTimes/135316" target="_blank">📅 01:18 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135315">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">🔴
🔴
علیرضا کوشکی هم‌اکنون بازیکن آزاد است اما باشگاه استقلال در تلاش برای تمدید قرارداد با او است. پرسپولیس کار راحتی برای جذبش ندارد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.76K · <a href="https://t.me/SorkhTimes/135315" target="_blank">📅 01:17 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135314">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">❗️
انفجار های چابهار خیلی شدید و بی سابقست.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 7.05K · <a href="https://t.me/SorkhTimes/135314" target="_blank">📅 23:59 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135313">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">✅
✅
ورزش سه
❌
علی علیپور در حال حاضر باتجربه‌ترین بازیکن پرسپولیس محسوب می‌شود و این موضوع باعث تسهیل در تمدید قرارداد این بازیکن شود.
🔴
هرچند که او احتمالا انتظار دارد تا پرسپولیس عدد مناسبی را پیش روی این بازیکن بگذارد تا او از نظر مالی هم شرایط بهتری را…</div>
<div class="tg-footer">👁️ 7.09K · <a href="https://t.me/SorkhTimes/135313" target="_blank">📅 23:48 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135312">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">🔴
🔴
موج جدید حملات سنگین آمریکا به جنوب کشور آغاز شده
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 7.03K · <a href="https://t.me/SorkhTimes/135312" target="_blank">📅 23:46 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135311">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">❗️
آکسیوس: شدت حملات امشب طی ساعات آتی بیشتر از دفعات قبل خواهد بود
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.98K · <a href="https://t.me/SorkhTimes/135311" target="_blank">📅 23:41 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135310">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">🔴
فوری/ CNN:
🔴
حملات آمریکا به ایران ممکن است در ساعات آینده آغاز شود، تیم امنیت ملی ترامپ در حال تصمیم گیری در مورد دامنه و گستردگی حملات آتی می‌باشند.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.9K · <a href="https://t.me/SorkhTimes/135310" target="_blank">📅 23:39 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135309">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">❗️
❗️
نساجی برای خرید ایری ۷۰ میلیارد پرداخت کرده و دو تیم استقلال و پرسپولیس هر دو بدنبال جذب این بازیکن هستن، احتمالأ رکورد مبلغ رضایت‌نامه تاریخ لیگ برتر شکسته بشه.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.87K · <a href="https://t.me/SorkhTimes/135309" target="_blank">📅 23:01 · 17 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>

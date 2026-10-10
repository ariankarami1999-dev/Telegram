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
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-07-18 03:38:05</div>
<hr>

<div class="tg-post" id="msg-141247">
<div class="tg-post-header">📌 پیام #100</div>
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
<div class="tg-footer">👁️ 1.17K · <a href="https://t.me/SorkhTimes/141247" target="_blank">📅 01:05 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141246">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">🏅
صحبت‌های جنجالی احمد گوهری درباره دلیل جدایی از پیکان: سرمربی فصل گذشته پیکان به جادوگری اعتقاد دارد!  «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.36K · <a href="https://t.me/SorkhTimes/141246" target="_blank">📅 01:01 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141245">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">🏅
صحبت‌های جنجالی احمد گوهری درباره دلیل جدایی از پیکان: سرمربی فصل گذشته پیکان به جادوگری اعتقاد دارد!
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.37K · <a href="https://t.me/SorkhTimes/141245" target="_blank">📅 01:00 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141244">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">⭕️
⭕️
⭕️
⭕️
⭕️
فووووووری؛ سازمان نظام وظیفه به بیرانوند اعلام کرده تا زمان مشخص شدن وضعیت کمیسیون پزشکی‌اش حق خروج از کشور را ندارد و ممنوع الخروج شده  «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 2.86K · <a href="https://t.me/SorkhTimes/141244" target="_blank">📅 23:51 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141243">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">🚨
🚨
🚨
#فوری/بیرانوند با دستور نظام وظیفه ممنوع الخروج است و امروز هم مجوز تمرین نداشته.
🚨
کریمی و نکونام می دانستند بیرانوند حق خروج ندارد و برای خوشایند زنوزی اخراجش کردند.
🚨
اکنون هم می خواهند سر هواداران را گرم کنند و به رسانه ها می گویند مشکل حل شده و به…</div>
<div class="tg-footer">👁️ 3.14K · <a href="https://t.me/SorkhTimes/141243" target="_blank">📅 23:44 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141242">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/diYURjpD1D14uT0Q--CKZBa9mvKmVTilq4foL0yv9CyUZGOsgZztJi6BTRj6N3kebPx-LC29CrVHRB476nQAn8DuqKzIqUSNQ1YWMtzwi2BOiOSRp5bh97uytEv_uZHoPA1fS9Y6WYdZLzwKWKzWThbqAC9h8ZtF5POi83CAHGpVit6egmKzhTQwnOmk-o0dLvRr4p_Lhfbar_PsTXjA2P76Zl-VDf0-vBA2RVcPG2-0XUvjJ6RNvvc-rk2JqYApP_G5-xFMG_lBmCgQE5WLkAUhDTDkXW8BCwRevvviMJrWRL5Gc0JcvcZt2WkOyDViVnHShPd74dtie3Kxewoglg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
اوستون اورونوف با گلزنی مقابل صنعت نفت به دومین گلزن خارجی برتر تاریخ پرسپولیس تبدیل شد.
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.25K · <a href="https://t.me/SorkhTimes/141242" target="_blank">📅 23:39 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141241">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">🚨
‼️
🇮🇷
منفوری بیرانوند ادامه داره
🚨
فوری؛ بیرانوند از هتل هم  اخراج شد!  علیرضا بیرانوند پس از درگیری لفظی با مدیران تراکتور و در آستانه سفر آسیایی این تیم، از حضور در اردوی تراکتور منع شد.  «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.61K · <a href="https://t.me/SorkhTimes/141241" target="_blank">📅 23:33 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141240">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PkQgu42Syr2XpMWMVMsGw0T0VDm9JIeMn3xJ-6e7qoHheDXPBSNFEzjaazCminb_isCUDMAHwkFzgo1hp7YC05VsXdLh8UwQbuRaRoHLuN3rs2XloblS6mwrvm0GDaMyqOVaqcymhkRlto-qK0LIDLsfjU9nZ-khn-Du1jEoDgX1_wravuNawN6wEgpxeMFVaYbkObUjHuybxH2htS6LcYY0z-qG0s4ppV24TiGpIzRnPZdis6DAZLm2FhSKfu7-biAYK-nX2r8rzHjLJKqptwv_2lbgVcfhzb8CL4x80J4pYqGga7YrOZ8P6woJ1yjLmtw5i3atcxS0tszMsraYXQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
❌
محمد نوری پس از شکست مقابل پرسپولیس به صورت توافقی از صنعت نفت آبادان جدا شد.
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.5K · <a href="https://t.me/SorkhTimes/141240" target="_blank">📅 23:31 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141239">
<div class="tg-post-header">📌 پیام #92</div>
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
<div class="tg-footer">👁️ 3.43K · <a href="https://t.me/SorkhTimes/141239" target="_blank">📅 23:28 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141238">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">✅
✅
تاج : آزادی تا 2028 باید مسقف بشه، وگرنه دیگه اجازه میزبانی نمیدن.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.49K · <a href="https://t.me/SorkhTimes/141238" target="_blank">📅 23:25 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141237">
<div class="tg-post-header">📌 پیام #90</div>
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
<div class="tg-footer">👁️ 3.95K · <a href="https://t.me/SorkhTimes/141237" target="_blank">📅 23:05 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141236">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kMYVrqQTNpFM5nh1bnyMpoQ01Va4J9jVN0kMIXs97M8bFxK2byHgHRcpwsoZ7vAm4cutYSNluNaxEgr_TEhzK8VyPKkeNio8bMzZaFKLZdwjftUw06g1gu2fqj3P1OQDS43c_O_YSDM4nhQ14ejOxq9QPP41tBDaJLJH4sDfjbSqO4HcZ1fkbQWQxBmK2yB5MeLW-w6DC5uNe5hWkHcyOVLr_nAUxpZWCXM3MAUb5rqZV03d_PndEdB5lyFyxUH9_QRQo-Ku8Uy05KBPs84U-ZGo11yu5YHQ2WATkGW6IhTsYBJvzB_wttF4OgIESlZii9mEyBJjBcLbDSZVJoTtjQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 3.94K · <a href="https://t.me/SorkhTimes/141236" target="_blank">📅 23:03 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141235">
<div class="tg-post-header">📌 پیام #88</div>
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
<div class="tg-footer">👁️ 4.95K · <a href="https://t.me/SorkhTimes/141235" target="_blank">📅 22:06 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141234">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dfc26b95b5.mp4?token=cnZfy-UbssmVggKGLl-ivHqJ9v_Vyr3O7p7fnLRSiA6B4o0FiRaoC9vCMlbc4FtsUXD3UzWus_K4Qd2i89CK7evtAMLRmdBBh4dQqucG4Na_U0oRyT6hXt9uHzdLDc8FXqKlSSTECiiciLGHRqdxyTJU5GRkfsFW8XEccGfioMBL2Uy2HNipbGX-AaYZ4QyaCQIqsQZxPhIcglyWbz3gu001D6BV3oAH63Wm2qAzuiRcIMnk_CJ-giCsfF64rtxpiUx3oNfr3d4aikdjC_jkUsID7oHUwPY6yvHS9Te7BDzhBcu8YLo77GwkdRMa1Gn_KcPVH5kQ9VUDHW293eyrFQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dfc26b95b5.mp4?token=cnZfy-UbssmVggKGLl-ivHqJ9v_Vyr3O7p7fnLRSiA6B4o0FiRaoC9vCMlbc4FtsUXD3UzWus_K4Qd2i89CK7evtAMLRmdBBh4dQqucG4Na_U0oRyT6hXt9uHzdLDc8FXqKlSSTECiiciLGHRqdxyTJU5GRkfsFW8XEccGfioMBL2Uy2HNipbGX-AaYZ4QyaCQIqsQZxPhIcglyWbz3gu001D6BV3oAH63Wm2qAzuiRcIMnk_CJ-giCsfF64rtxpiUx3oNfr3d4aikdjC_jkUsID7oHUwPY6yvHS9Te7BDzhBcu8YLo77GwkdRMa1Gn_KcPVH5kQ9VUDHW293eyrFQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
اتوبوس تیم ابوالفضل جلالیو جا گذاشته تو ورزشگاه
😐
😂
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.92K · <a href="https://t.me/SorkhTimes/141234" target="_blank">📅 22:04 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141233">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">✔️
#فوری | شنیده شدن صدای چندین انفجار در شرق بندرعباس و اطراف قشم منشا صدا مشخص نیست
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.48K · <a href="https://t.me/SorkhTimes/141233" target="_blank">📅 21:27 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141232">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">🚨
محسن خلیلی، سرپرست پرسپولیس:
❌
یاسر آسانی؟ باشگاه تمام مسائل را از صفر تا صد پیگیری می کند. داخل کشور به نتیجه نرسیم صددرصد در دادگاه عالی ورزش دنبال می کنیم. ما نگفتیم این پرونده پایان یافته است. مندیت آسانی به پرسپولیس؟ بله او مندیت را داشت اما زمان همه چیز را در این زمینه نشان می دهد
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.47K · <a href="https://t.me/SorkhTimes/141232" target="_blank">📅 21:17 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141231">
<div class="tg-post-header">📌 پیام #84</div>
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
<div class="tg-footer">👁️ 5.43K · <a href="https://t.me/SorkhTimes/141231" target="_blank">📅 20:53 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141230">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ANhTaJp4PrAQaCAfk03Y2y_TEsC3y_ttBhkELdBe0TZ-yPyM8o-7f7fc1CVKufYPHIb8HfeHsE7GDuB9vCAWEn7DJMB1CbdFNfHZ-EOrP6LeQPf4VGXINjkoIgSU4L5TuI69TlDSCsbDKO4WGMVqHcdMuHvSBNMNIQ1ITarq0Ml7VolMgDdd-HsnvYomPkYNVBbm2xkKgbDQl6yCpn7ZQ5AzCxd8bMpoBveqtxyTnRkFOmcNbBAome0K6U5rT1putuBCu5uBPsWjFgTtxPB8WQKyw2RSbHTShKeUz01ghzQeSzQv_l1mJE_MpWiWgT5f_-3DEgQoWiwe0E5nn_7hEA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
سرخپوشان پس از کسب پیروزی، جشن خود را با هواداران تقسیم کردند
❤️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.26K · <a href="https://t.me/SorkhTimes/141230" target="_blank">📅 20:48 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141229">
<div class="tg-post-header">📌 پیام #82</div>
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
<div class="tg-footer">👁️ 5.1K · <a href="https://t.me/SorkhTimes/141229" target="_blank">📅 20:20 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141228">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">🚨
🚨
جونم جسارت تارتار ...پوریا اسمی .بازیکن محصل و مدرسه ای و آورد داخل   «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.98K · <a href="https://t.me/SorkhTimes/141228" target="_blank">📅 20:13 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141227">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">🎤
🔴
علی بازگشا: اسناد کامل و جدیدی درباره پرونده آسانی به کمیته استیناف ارسال کردیم
🔹
امیدوارم این پرونده در داخل کشور حل شود/ اقدامات قانونی را در داخل کشور انجام دادیم و اسناد جدیدی خدمت کمیته استیناف ارسال کردیم/ امیدواریم این اسناد جدید و مهم که تا به حال به این ارکان ارجاع داده نشده موثر باشد و رای جدیدی دهند/ تمام تلاشمان این است که موضوع در داخل کشور حل شود چون احترام به ارکان قضایی کشور است/ نامه‌ای را روز گذشته به فدراسیون ارسال کردیم و ادله ما شفاف است/ چیزی که از فدراسیون می‌خواهیم اجرای قانون است نه مصلحت اندیشی/ قانون منع مصلحت نیست/ تاثیرگذاری یک بازیکن غیرمجاز می تواند نظم جدول را برهم بزند و به بقیه تیم‌ها ظلم‌ شود/ پاسخگوی هوادار و سهامدار باشگاه هستیم/ ما مندیت آسانی را در آن تاریخ دریافت کردیم/ باید رای قاطع و جذاب صادر شود/ کسی تماسی نگرفته که این موضوع پیگیری نشود/ اسناد مختلف از جاهای مختلف رسیده است/ اگر نتیجه دربی به نفع ما شود دیگر طبیعتا در کاس پیگیری نمی‌کنیم ولی ما درباره این موضوع صحبتی نکرده ایم
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.01K · <a href="https://t.me/SorkhTimes/141227" target="_blank">📅 20:02 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141226">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">🚨
پیام نیازمند: بازیای بعد فیفادی همیشه سخته/ تا جام ملت‌ها خیلی مونده و تمام تمرکزم روی موفقیت پرسپولیسه/ کاپیتانی پرسپولیس برام افتخاره  «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.94K · <a href="https://t.me/SorkhTimes/141226" target="_blank">📅 20:01 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141225">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">🚨
✅
پیام نیازمند برای اولین بار در طی حضورش در پرسپولیس به عنوان کاپیتان کارش را آغاز خواهد کرد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.07K · <a href="https://t.me/SorkhTimes/141225" target="_blank">📅 20:00 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141224">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">🚨
🚨
جونم جسارت تارتار ...پوریا اسمی .بازیکن محصل و مدرسه ای و آورد داخل   «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.25K · <a href="https://t.me/SorkhTimes/141224" target="_blank">📅 19:49 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141223">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZfuXeDPQEnSBX9247cPAV3fCFCE_6U88tZVO03Cvhwgv18fprbjpnqX7fOLHui8VWafOsCsNDaW31Vr24oHKQUBkuHYGTspWw1OuQLuU3sUvQSQK6nG8JtFpFqRICFuNrsIcnts7XORFrsq1pWRM_uVeZhbSjNvAp9DESIWPCjP40IoHv6PiNT3QVb4CA_K-lSv22vdabaf3ft8wdl3HmgNyyuE-m-2v51qeUgRL_rgUhe4rrmx5vTf9EXgXvLZVrzm42giS8xg9-ZcZo9riIkEGcVDcEUfb5qmHvqpnTxQ7zQ2rMl88rVLN8y-oZ8PMDP05aSalqOBYK_I9ePkoJg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇮🇷
جدول لیگ‌برتر پس از بازی‌های امروز
🚨
پرسپولیس با برد مقابل خیبر در بازی معوقه، به صدر جدول میره
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.39K · <a href="https://t.me/SorkhTimes/141223" target="_blank">📅 19:22 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141222">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">🚨
چشم نوازترین پرسپولیس چند سال اخیر و میبینیم ..نیمه اول و با یک گل بردیم ...تو نیمه ای که سه چهار گل و نزدیم  «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.41K · <a href="https://t.me/SorkhTimes/141222" target="_blank">📅 19:10 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141221">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">🔴
🔴
💢
خلاصه بازی پرسپولیس 3 - نفت آبادان 1  «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.53K · <a href="https://t.me/SorkhTimes/141221" target="_blank">📅 19:07 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141220">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a74657a541.mp4?token=ITb-pkRsVaUrOu5sf_LauM-XxY0To7U00Vga4spzxQA0gKGPefzuGPvk6w3CFbO5nmPbuK8RR6uIDbHt5RCGFvVFleFn13Vr5EqBb05sfhlfz7ZN3SIoV6ljB4Z1iWnuv7StrqDB4hvHhy0dS-18XYXCAIYkvSDwA5jlsQz5SaWgvHk5kOSsP8bZonzXoC2IPl6FJtD4A78ezf8nMncNXV3SSfOeZpDNNFBYHNuNgmCzx1mfA4GSJcrR_AhRZ7ELUdqsFMZNAMF-muFFIyzqFgyktxP7qbaBuUfgTNKbFCh4iYkFrMvKzbwTngZ_PswiCyYBsQhm8DvdHWF9y9K4xw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a74657a541.mp4?token=ITb-pkRsVaUrOu5sf_LauM-XxY0To7U00Vga4spzxQA0gKGPefzuGPvk6w3CFbO5nmPbuK8RR6uIDbHt5RCGFvVFleFn13Vr5EqBb05sfhlfz7ZN3SIoV6ljB4Z1iWnuv7StrqDB4hvHhy0dS-18XYXCAIYkvSDwA5jlsQz5SaWgvHk5kOSsP8bZonzXoC2IPl6FJtD4A78ezf8nMncNXV3SSfOeZpDNNFBYHNuNgmCzx1mfA4GSJcrR_AhRZ7ELUdqsFMZNAMF-muFFIyzqFgyktxP7qbaBuUfgTNKbFCh4iYkFrMvKzbwTngZ_PswiCyYBsQhm8DvdHWF9y9K4xw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">💢
شادی ایسلندی بازیکنان پرسپولیس در کنار هواداران در ورزشگاه⠀
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.47K · <a href="https://t.me/SorkhTimes/141220" target="_blank">📅 19:05 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141219">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">🔴
🔴
💢
خلاصه بازی پرسپولیس 3 - نفت آبادان 1
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.31K · <a href="https://t.me/SorkhTimes/141219" target="_blank">📅 19:04 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141218">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">🚨
🚨
جونم جسارت تارتار ...پوریا اسمی .بازیکن محصل و مدرسه ای و آورد داخل   «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.37K · <a href="https://t.me/SorkhTimes/141218" target="_blank">📅 19:02 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141217">
<div class="tg-post-header">📌 پیام #70</div>
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
<div class="tg-footer">👁️ 5.4K · <a href="https://t.me/SorkhTimes/141217" target="_blank">📅 18:54 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141216">
<div class="tg-post-header">📌 پیام #69</div>
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
<div class="tg-footer">👁️ 5.33K · <a href="https://t.me/SorkhTimes/141216" target="_blank">📅 18:53 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141215">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">🚨
همون بازیکن همیشگی و تاثیر گذار ..بیفوما پنالتی گرفت و علیپور زد   «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.18K · <a href="https://t.me/SorkhTimes/141215" target="_blank">📅 18:52 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141214">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">🔴
گلللللل دوم توسط علیپور  «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.29K · <a href="https://t.me/SorkhTimes/141214" target="_blank">📅 18:25 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141213">
<div class="tg-post-header">📌 پیام #66</div>
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
<div class="tg-footer">👁️ 5.28K · <a href="https://t.me/SorkhTimes/141213" target="_blank">📅 18:24 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141212">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">🚨
🚨
با تعویض اورونوف جای عمری و پورعلی جای لطیفی فر میشه اختلاف و نیمه دوم بیشتر کرد   «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.21K · <a href="https://t.me/SorkhTimes/141212" target="_blank">📅 18:12 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141211">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">🚨
چشم نوازترین پرسپولیس چند سال اخیر و میبینیم ..نیمه اول و با یک گل بردیم ...تو نیمه ای که سه چهار گل و نزدیم  «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.17K · <a href="https://t.me/SorkhTimes/141211" target="_blank">📅 18:06 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141210">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">🚨
چشم نوازترین پرسپولیس چند سال اخیر و میبینیم ..نیمه اول و با یک گل بردیم ...تو نیمه ای که سه چهار گل و نزدیم  «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.11K · <a href="https://t.me/SorkhTimes/141210" target="_blank">📅 18:03 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141209">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/36338a35c2.mp4?token=ruaPC0jqGMkisb1A6QkF3ka_K5EYKR4Vex7_dzjKfh_IBXuCE-TxjO-jTQEcwAiqsNHezS8inYlIgNfqR_iL5qGzRes6rCrDh5YnpdTTcjL0YQuQuMQZoyTunu6qlyaxWXkgjLC4RzNRusCAUwTtr3kvYAeUCJQ8l8FEgKvmMe9-aEITw288CqAymS8Ln8MyvXa2zXE2hVZ0UA8gIfqu2lKwqJfHcx-FvAJe1lNtBcDGCWUxnL2KQw74KBeMG9nSmLaPsM24eJn0EC4FZVjCIX9riPotWYVZEzgUNQOrmvdKjKJVfkm6AtkIALENESoNg2r0uVRYO9fxXupJzmDj5Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/36338a35c2.mp4?token=ruaPC0jqGMkisb1A6QkF3ka_K5EYKR4Vex7_dzjKfh_IBXuCE-TxjO-jTQEcwAiqsNHezS8inYlIgNfqR_iL5qGzRes6rCrDh5YnpdTTcjL0YQuQuMQZoyTunu6qlyaxWXkgjLC4RzNRusCAUwTtr3kvYAeUCJQ8l8FEgKvmMe9-aEITw288CqAymS8Ln8MyvXa2zXE2hVZ0UA8gIfqu2lKwqJfHcx-FvAJe1lNtBcDGCWUxnL2KQw74KBeMG9nSmLaPsM24eJn0EC4FZVjCIX9riPotWYVZEzgUNQOrmvdKjKJVfkm6AtkIALENESoNg2r0uVRYO9fxXupJzmDj5Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
چقدر خوبی شما آقای نیازمند
❤️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.11K · <a href="https://t.me/SorkhTimes/141209" target="_blank">📅 18:00 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141208">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">🚨
🚨
یک گل زدیم و سه گل نزدیم ..و همچنان پرسپولیس مثل همه بازی ها سوار بازیه  «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.1K · <a href="https://t.me/SorkhTimes/141208" target="_blank">📅 17:54 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141207">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">🚨
🚨
گل اول و زدیم خیلی زوددد....سرگیف داد بیفوما زد   «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.14K · <a href="https://t.me/SorkhTimes/141207" target="_blank">📅 17:37 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141206">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">🚨
🚨
بریم برای بازی حساس که سه امتیازش به اندازه شش امتیاز ارزش داره ..دلمون برای پرسپولیس تنگ شده بود   «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.14K · <a href="https://t.me/SorkhTimes/141206" target="_blank">📅 17:09 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141205">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">🚨
🚨
بریم برای بازی حساس که سه امتیازش به اندازه شش امتیاز ارزش داره ..دلمون برای پرسپولیس تنگ شده بود   «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.24K · <a href="https://t.me/SorkhTimes/141205" target="_blank">📅 17:02 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141204">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">🚨
🚨
بریم برای بازی حساس که سه امتیازش به اندازه شش امتیاز ارزش داره ..دلمون برای پرسپولیس تنگ شده بود
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.2K · <a href="https://t.me/SorkhTimes/141204" target="_blank">📅 16:54 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141203">
<div class="tg-post-header">📌 پیام #56</div>
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
<div class="tg-footer">👁️ 5.33K · <a href="https://t.me/SorkhTimes/141203" target="_blank">📅 16:11 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141202">
<div class="tg-post-header">📌 پیام #55</div>
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
<div class="tg-footer">👁️ 5.14K · <a href="https://t.me/SorkhTimes/141202" target="_blank">📅 16:11 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141201">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">🚨
نیمکت ذخیره پرسپولیس مقابل صنعت‌نفت:
❌
❌
امیررضا رفیعی، ابوالفضل جلالی، علی علیپور، پوریا شهرآبادی، امیرحسین محمودی، محمدحسین صادقی، امیرحسین طاهری، پویا اسمی، پویا پورعلی، استون اورونوف، یاسین سلمانی
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس…</div>
<div class="tg-footer">👁️ 4.93K · <a href="https://t.me/SorkhTimes/141201" target="_blank">📅 16:09 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141200">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">✔️
ترکیب اومد ..جای جلالی تیکدری بازی می‌کنه..جای پورعلی لطیفی فر بازی می‌کنه و جای شهرابادی محمد عمری بازی میکنه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.84K · <a href="https://t.me/SorkhTimes/141200" target="_blank">📅 16:08 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141199">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3c7ca0c681.mp4?token=HXQZVEnPAuNQg0DMe-xsUP07siPmkKFN42eTDjnDAAfKa0Conkoux6n1Og1yEG4gvMu0QgtxjSzJ9xIqJ0BThhNYRD4r-FyuSXLh7gq-JBIhOPmYOkXCNtuXvhiAhGIjybfPCBTo2m8nDBXCXgQNaPFMoAYwl-ZkCpLNy4EUVWWHFKBmAFjCYALnpC2WON91nI8bOeY0y9e7TWFmrtWrTmDbqP1lh4QtM0qMNavpuhW9lYiSSB3P75hAUQVWAhLbW4-rv3pILCpVoGTHFluogcHESbgiyT0-L-hsJzANS4Iu-a4FyhqHmUdwYU2w8LhGacR80rSGDELn9gDAaGj6Dg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3c7ca0c681.mp4?token=HXQZVEnPAuNQg0DMe-xsUP07siPmkKFN42eTDjnDAAfKa0Conkoux6n1Og1yEG4gvMu0QgtxjSzJ9xIqJ0BThhNYRD4r-FyuSXLh7gq-JBIhOPmYOkXCNtuXvhiAhGIjybfPCBTo2m8nDBXCXgQNaPFMoAYwl-ZkCpLNy4EUVWWHFKBmAFjCYALnpC2WON91nI8bOeY0y9e7TWFmrtWrTmDbqP1lh4QtM0qMNavpuhW9lYiSSB3P75hAUQVWAhLbW4-rv3pILCpVoGTHFluogcHESbgiyT0-L-hsJzANS4Iu-a4FyhqHmUdwYU2w8LhGacR80rSGDELn9gDAaGj6Dg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
باران در شهرقدس و حضور بانوان هوادار پرسپولیس
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.6K · <a href="https://t.me/SorkhTimes/141199" target="_blank">📅 16:07 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141198">
<div class="tg-post-header">📌 پیام #51</div>
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
<div class="tg-footer">👁️ 4.48K · <a href="https://t.me/SorkhTimes/141198" target="_blank">📅 16:06 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141197">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">🟥
ورود اعضای پرسپولیس به ورزشگاه شهدای شهرقدس
❤️
..
🚨
هوا هم مشخصه باد و بارون شدیده
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.6K · <a href="https://t.me/SorkhTimes/141197" target="_blank">📅 16:02 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141196">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/s3Lf65meH22Ta9jvdoFgCA1uPf05edJwMAq_iend6b1pdKuvR3Ybc0N1y4S9ovjXcUuiWOe68sMaepbPdXss3etnsd4TziIMBbwYTgN5WehvZVyip7KV3kf6wNXX_hl1iWBMGbSWg6Y4VR7Vqbz0CG3095BD6Yd8ZVUv27E9HTnWogM-JZ2LvUDWWf4MCUozxYR3H9CiovTQREZdjFlGOYd7pYC_ZReW-AdJL1v2VEjMSrXHmEDO0NMRbas0nOZnrLFIVZ9lsWGbcnYkMAWMGoiThtw6tqYJ-PyoYh0Jp6eVplgM92SW2cfKz_4WsDErMP2XZAMp77ucwyxiPzTBHQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
نمای آنلاین استادیوم شهرقدس
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.38K · <a href="https://t.me/SorkhTimes/141196" target="_blank">📅 15:58 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141195">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">⭕️
⭕️
با اعلام باشگاه تراکتور، علیرضا بیرانوند به دلیل مصاحبه بعد از بازی با استقلال از این تیم کنار گذاشته شد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.53K · <a href="https://t.me/SorkhTimes/141195" target="_blank">📅 15:40 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141194">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rmG2nTFbrNC9B1cCgcZHufJEQJOnM6ozwK8qDGICCZqTOlPU7OxdX_oLKJpxtw_87oj-uqvYkYQ1WNM0UqgLMmU2azvp-uP6t8w0zOHLXkTXswjke-EQSQ3OIMkcOAnwI3HJH1u9KyqtquI_oFsPf6Qwybj6srGoCICbgE27kSnYzSntVUIGLHBO-M2jTbT9NefzWMJSTPDpPSDO4kA8DxItUDclgrCHFGjLp0M7F9N-az-2lN7vIGYfOUvWdMHFbalcWsvuqEZ7enfexeTgNqzVcrMu_QbX25o6NkCJSyl_9fwQpXFq-8-1_hiw8WZWHofTaPX3M7mcLIVp-W034Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
خروج اعضای تیم از هتل به سمت ورزشگاه شهرقدس
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.59K · <a href="https://t.me/SorkhTimes/141194" target="_blank">📅 15:38 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141193">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">⭕️
فردا ببر و محبوب تر شو .حاج مهدی تارتار
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.63K · <a href="https://t.me/SorkhTimes/141193" target="_blank">📅 15:36 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141192">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XGlGdaJESonNsFGKyfenz5LDmKxiUrZZTvWOQnHGrCA6pRJqGcAMia7Sj32EiHLRwSMp6QvW_WWs3seDr-pvyGio2dU9OKAOH1LetAQCCS7yPDZDIDxFWPsq-y8Vz-r232ptWRr48RhLA_XsFM23CP6MsUAxOdQxYs26TH5S5HBYQSZk5vs4Kh6Q5LOPKaCYJ210RKXNxZfNhrbmxTbEYGXYb8W6noFJpDaakaHjIVBmeUzxixKZfPngByEKGXzsgI_CqIl-kgd9Xbj2swWMXi68dcpdxMF-vLlW0-XCdccpq5inf_JPzT5D2_m1AVp8VmqkiT6lFUc8lasTMBLmOQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❤️
علی علیپور: از پیام‌های هواداران عزیز که نگران حالم بودند متشکرم. خوشبختانه مصدومیت جزئی‌ام برطرف شده و با آماده‌سازی کامل در خدمت تیم و کادرفنی هستم.
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.72K · <a href="https://t.me/SorkhTimes/141192" target="_blank">📅 15:26 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141191">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">🚨
🚨
باشگاه تراکتور درنظر دارد تا با توجه به مصاحبه علیرضا بیرانوند، به او اجازه فسخ قرارداد و حضور در تیمی دیگر را ندهد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.74K · <a href="https://t.me/SorkhTimes/141191" target="_blank">📅 14:25 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141190">
<div class="tg-post-header">📌 پیام #43</div>
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
<div class="tg-footer">👁️ 4.74K · <a href="https://t.me/SorkhTimes/141190" target="_blank">📅 14:13 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141189">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">🙏
🙏
🙏
🙏
🙏</div>
<div class="tg-footer">👁️ 4.79K · <a href="https://t.me/SorkhTimes/141189" target="_blank">📅 14:13 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141188">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">🙏
🙏
🙏
🙏
🙏</div>
<div class="tg-footer">👁️ 4.82K · <a href="https://t.me/SorkhTimes/141188" target="_blank">📅 14:12 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141187">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SU53jsbrRQSXQpawav2rszME08bKyB3FQpnBe3pJ52qUo3Dc4prO8LTOo22c4d-eKw8PlJiwvUwTELNQJUvi1VT1fBi1rLdnxpMAOQNQJtbECifPGM-jNyFmJi52F-hSp4NnlC6W60YOutVWhuWVA4B_nbYBSz7G5N6UuRUAR2aRuQZPEPSksPjDoKS-yVaGEWAzl82KdgDG3z4_lAZojyufXcW84F6GU24kwnk-cj2eAlurqka7yGHJLgwGwvQsFKqNS2aEwZM2ZCymNoJIVnTI6TVeE5IRp3mfKQwjJYiqrbHCAAgfuc44B7qeKF1LoEXufJaA1cb7U24GXyV0IA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 4.98K · <a href="https://t.me/SorkhTimes/141187" target="_blank">📅 14:09 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141186">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">🚨
علیپور هنوز زانو درد داره و بازی کردنش ریسکه البته خودش میخواد که بازی کنه تا از کورس عقب نیفته
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.7K · <a href="https://t.me/SorkhTimes/141186" target="_blank">📅 13:34 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141185">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">🚨
❌
❌
اگه امروز علیپور بازی نکنه و در غیاب کنعانی نیازمند کاپیتانه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.68K · <a href="https://t.me/SorkhTimes/141185" target="_blank">📅 13:27 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141184">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ck5tddBk9gKiGUAlWr_T_di3l6jJa2F6D4ZJeT5_hVXQGwUn05ngB7lQ7FkZGn9t4OEM24aznlWp2JWKkgs5G2IP7N6oUpDzsWWOsbVTgbqUDBD1y1zLD_imEOYEJMzfRWV4dKLu8Ycks1ajyCxpYsdnTFK3ih7hVyqNWiERYY44V8kI7CaI1FS22o3yZFXtIEEVljoAuv5-AZ7fGF3aL4S2_S-BjNT35N-l6oAaYq7K5v5l26UK1AH-QP7YBGkUaWDhAd-3EoDSnQ0x5f7bEpOTGnU5oYhXiIVsmxnJ77jf8dlXkycPKiN7dGBCrMencVSdjejcdDxVrClWB0V8FQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 4.92K · <a href="https://t.me/SorkhTimes/141184" target="_blank">📅 12:48 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141183">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2cf12ee8e5.mp4?token=qtwb6kZgV0aJpyELXINDLh33EpKgMstdjeUemmxUBJ--Ydi70EUOTy31_64SzyX0GVT57poKrwYuDwtJ07n8_ga8MhSQiRTup3t33ferWbX51k1bjs7O6H-GWY5I61pXWWQTry51q20muWfCRykkkpezuidUEiWq1LkDQOsnLCE3UJtUK4G81vpFonaPsIlstm0HmplxIg_TH87cJ6gjywNuwiVbaTjc9H5xjBvidX8AyU_pLX7PZ--oqpfB38irmhi0HhWUuFZslL6EPcK6aynm3L0b8KzCscnq2zCwSl0FhxB2XGnlUorw-y3NxU3bvXsb2y0kjjUCXR0ckTIiMA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2cf12ee8e5.mp4?token=qtwb6kZgV0aJpyELXINDLh33EpKgMstdjeUemmxUBJ--Ydi70EUOTy31_64SzyX0GVT57poKrwYuDwtJ07n8_ga8MhSQiRTup3t33ferWbX51k1bjs7O6H-GWY5I61pXWWQTry51q20muWfCRykkkpezuidUEiWq1LkDQOsnLCE3UJtUK4G81vpFonaPsIlstm0HmplxIg_TH87cJ6gjywNuwiVbaTjc9H5xjBvidX8AyU_pLX7PZ--oqpfB38irmhi0HhWUuFZslL6EPcK6aynm3L0b8KzCscnq2zCwSl0FhxB2XGnlUorw-y3NxU3bvXsb2y0kjjUCXR0ckTIiMA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
پرسپولیس _ نفت آبادان
❌
اولین گل یورگن لوکادیا با پیراهن پرسپولیس
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.7K · <a href="https://t.me/SorkhTimes/141183" target="_blank">📅 12:38 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141182">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">⭕️
⭕️
⭕️
زنوزی هم بالاخره طعم تلخ داشتن بیرانوند را چشید!
❌
❌
سرانجام نوبت به زنوزی و مدیران تراکتور رسید تا طعم گس داشتن علیرضا بیرانوند را تجربه کنند؛ همان مصاحبه‌ها، همان گلایه‌های مالی و همان کنایه‌هایی که پیش‌تر مدیران پرسپولیس بارها با آن مواجه شده بودند.…</div>
<div class="tg-footer">👁️ 4.98K · <a href="https://t.me/SorkhTimes/141182" target="_blank">📅 12:30 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141181">
<div class="tg-post-header">📌 پیام #34</div>
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
<div class="tg-footer">👁️ 5.16K · <a href="https://t.me/SorkhTimes/141181" target="_blank">📅 12:27 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141180">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">⭕️
⭕️
⭕️
زنوزی هم بالاخره طعم تلخ داشتن بیرانوند را چشید!
❌
❌
سرانجام نوبت به زنوزی و مدیران تراکتور رسید تا طعم گس داشتن علیرضا بیرانوند را تجربه کنند؛ همان مصاحبه‌ها، همان گلایه‌های مالی و همان کنایه‌هایی که پیش‌تر مدیران پرسپولیس بارها با آن مواجه شده بودند.…</div>
<div class="tg-footer">👁️ 4.76K · <a href="https://t.me/SorkhTimes/141180" target="_blank">📅 12:17 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141179">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/86b4db41c1.mp4?token=jthXegCN9OdfHVvGvXEALrgajmejhCo8CdSWAkNdbA1fB2kQpaFKxAgh11-_XYM-9-NmCjir48YY-cH_MduhNi8wUXwySrRuV7T-ZhLmHMD9RCanfDA3H1jXB5pO9vUNyg8hX6HfJoTMKNjsNui3tRt3wz4kNmxVBbfRmdp-nOKzgu1Glgj-GN7Jh2EC0iz41rrS77Df1nnsFWIjEfNIV03Oh72Kvy8qHtyYqm8JteQU4qCSAKZ_ByOYcmzyui2LzoZP6d8dvTVwQJ75NAUEt_XgpQt588HkLZ-e63OQtLNk5E8DLf22M5pN_FupNsmz8GhIIMALwcZ5o2X9xxfgog" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/86b4db41c1.mp4?token=jthXegCN9OdfHVvGvXEALrgajmejhCo8CdSWAkNdbA1fB2kQpaFKxAgh11-_XYM-9-NmCjir48YY-cH_MduhNi8wUXwySrRuV7T-ZhLmHMD9RCanfDA3H1jXB5pO9vUNyg8hX6HfJoTMKNjsNui3tRt3wz4kNmxVBbfRmdp-nOKzgu1Glgj-GN7Jh2EC0iz41rrS77Df1nnsFWIjEfNIV03Oh72Kvy8qHtyYqm8JteQU4qCSAKZ_ByOYcmzyui2LzoZP6d8dvTVwQJ75NAUEt_XgpQt588HkLZ-e63OQtLNk5E8DLf22M5pN_FupNsmz8GhIIMALwcZ5o2X9xxfgog" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
گویا دانیال اسماعیلی فر هم از ناحیه ای که رامین مصدوم شد مصدوم شده و احتمالأ یک ماهی نباشه
😁
😂
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.64K · <a href="https://t.me/SorkhTimes/141179" target="_blank">📅 12:13 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141178">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/59ff4bc2f6.mp4?token=TrxTpECDWebEUno3oE0Y_fIYh9-V7YxVDx7oOg5S6BcAoN8qNp0rsGIEXPBeooXrJd8G4_0ucACPR_r6CtVzyyPrXD1ESHkGZlmd1wlac0mioQg8jccMeOYe8KANEZgwbWyRpgeMDyp6XE8msIKjsqVnb0JR2-K6U38eQnhjofYpiTOqKm0RM6jnI-RHY1jHz8FIBkmHo1H20p83gyQmov8uNtyZsDEO5-rVqUR_E12Chd3CJq8KabIW3nFYRMdZnxWMnv-iUpjfH7HBrhQWyz7WapVRsRX6zCITebZ1elauaoJIMAnQjDtq2gaKSZ8b_ur_XxgwHfhuh4LAfNE2Aw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/59ff4bc2f6.mp4?token=TrxTpECDWebEUno3oE0Y_fIYh9-V7YxVDx7oOg5S6BcAoN8qNp0rsGIEXPBeooXrJd8G4_0ucACPR_r6CtVzyyPrXD1ESHkGZlmd1wlac0mioQg8jccMeOYe8KANEZgwbWyRpgeMDyp6XE8msIKjsqVnb0JR2-K6U38eQnhjofYpiTOqKm0RM6jnI-RHY1jHz8FIBkmHo1H20p83gyQmov8uNtyZsDEO5-rVqUR_E12Chd3CJq8KabIW3nFYRMdZnxWMnv-iUpjfH7HBrhQWyz7WapVRsRX6zCITebZ1elauaoJIMAnQjDtq2gaKSZ8b_ur_XxgwHfhuh4LAfNE2Aw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
🤩
ببینید دختر هادی نوروزی چقدر بزرگ شده؛ همسر هادی بعد ۱۲ سال هنوز لباس مشکی رو در نیاورده
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.89K · <a href="https://t.me/SorkhTimes/141178" target="_blank">📅 12:09 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141177">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/r09tuiF6kdnGPQ4XxR5ipOppYrNH8mssk7Q1Ilhe4Ukz-WpVkU7pHpvAxgjvKt0kVa9Ri-To7RB5qX4JhOzM_eNhQaCiEA8tJSMKREK1xx5WcUwU9Hb936aO7Z5K6zQyh-L26GndulYIFAgc7MYZ9SsOF4z4-ng3Ho3LljB8LuROUln4FOYiGhTktR3a-v6gxZIWpOLd2G95D6FpyIcTOGhiSKxD4HqqCYpjkzVHn4sb6gYzorsjjI8V_c9fGGmGSiJ5T56IY9StN2hsGFq8TuTwM-mJdb1t9fw05wNAIU_H-9PEZOMWQAt2rQwZnwV9-TQGmwlsHF-QpEqslGTvCQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 4.8K · <a href="https://t.me/SorkhTimes/141177" target="_blank">📅 12:03 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141176">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">❗️
⛔️
👀
پرسپولیس ب که قرار بود به سیدجلال سپرده شود، احتمالا با محسن بنگر وارد رقابت‌های دسته دوم لیگ آزادگان می شود...
‼️
🟥
به گزارش هفت ورزشی، پرسپولیس که دنبال خرید امتیاز برای راه‌اندازی تیم دوم بود، سرانجام امتیاز پادیاب خلخال را خرید‌. گفته می‌شد هدایت پرسپولیس…</div>
<div class="tg-footer">👁️ 4.93K · <a href="https://t.me/SorkhTimes/141176" target="_blank">📅 10:58 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141175">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rJSAnitzsc0Ch7xzDr_LP3xjgXvXMylzJzwnRLwXqhQ9WEcms6zz_z7YsOFr1F31EIkY0WTwvtD8yBhwjzfhIyuxc_Ai31sRYCtY1FB_vFqyFvwkDyF3Kuw-Ba0lFFViUEgSbBkqx9BMj6-tHF8tr-wp1ycrviTrqOujWx5WScxrsESJGzL_I0JhoIcDACJRRH1e06ZUTY8Mha6AuFlw09Y8zRZZHDez4zdcNhxst5YL-tM5KlM0wXp_89_ciq6Ko2jQhnxxUlU3wg7lF04pv-ye9fvemVqtg-jOmd9yHmlHVUUwMFolHF4GcM2rB_c9mqHo3_iOHYBGIwQPSabxuQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
دعوا در تراکتور بالا گرفت
❌
شکایت بیرانوند از کریمی مدیرعامل باشگاه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.87K · <a href="https://t.me/SorkhTimes/141175" target="_blank">📅 10:56 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141174">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">🚨
با نظر کریم باقری و موافقت مهدی تارتار ؛ پیام نیازمند کاپیتان سوم پرسپولیس شد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.91K · <a href="https://t.me/SorkhTimes/141174" target="_blank">📅 10:46 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141173">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/StA8RRwyy5I0L-FIDnG1j6KwfaTGNLby0GBmhHpMRqRrQmziAF83_RTTW5t-i1ZLB5T-Fv_LjU5arzmIG0-0zVDhN7OwVXRWxUZ_eK-_H5NKwHtglNhsdYX67_Wjen57gEUw7UyyBryClz0bjFuqfd-2bUww82WmrJaj3TxD_-En_-p_zllTXolb_-BlqIgDhPew8JvBAu1GGH4P_iO5sKVzAFf3MBmGaSxcMT25SHGAJD8XxOemBrZyVnbsOpJpyymeT6M-KeDEGYkiveUZWBF-I78eInhpthcixPx6abHOdpglAZwDIv2TTLlNc8ztTymq11kITnTWHtHZcYOaPg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
با نظر کریم باقری و موافقت مهدی تارتار ؛ پیام نیازمند کاپیتان سوم پرسپولیس شد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.03K · <a href="https://t.me/SorkhTimes/141173" target="_blank">📅 10:45 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141172">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">✔️
✔️
کریستیانو رونالدو امروز برای سومین روز متوالی در تمرین تیم ملی پرتغال حاضر نشد و طبق گزارش رسانه‌های پرتغالی و اسپانیایی، اردوی تیم را ترک کرده است. این اتفاق پس از اظهارات ژسوس درباره غیبت رونالدو مقابل دانمارک رخ داده و برخی رسانه‌ها احتمال بازگشت او…</div>
<div class="tg-footer">👁️ 4.84K · <a href="https://t.me/SorkhTimes/141172" target="_blank">📅 10:43 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141171">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/R9CiuTIYpnn8A5ww8CYpl3oSe_rYcZzZPVEmnPJmF6sfGvT1tiR9ohQviCvvUWZNp_0bkxkxhFb0FrJJ_nyQ_1V_qOwEe47BCTV2akTQGGOH5dHev-_BrUmGDZbvKdYUytqoogPZ_KBe85t3BLWkmpRnUFjlP4Exq3wfV4nv--txuUu6jmqwwggENLczme4WA8T_IdOk-RpfK2LsLYdErh--DiC0lQX3nvTpVkUSJIrPpkvUKoeMivVOudM5BMmWF5nQrd8tyqQPlnPIsv61KaLQ_CLJqP0cmzxHcFSf1iPSiiRETS4u8JFjs5EV3EQvVlupZdap5vmDS1rY-8S55w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
ورزش سه: پوریا لطیفی فر امروز قراره جای پویا پورعلی بازی کنه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.91K · <a href="https://t.me/SorkhTimes/141171" target="_blank">📅 10:29 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141170">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">🚨
دعوا در تراکتور بالا گرفت
❌
شکایت بیرانوند از کریمی مدیرعامل باشگاه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.92K · <a href="https://t.me/SorkhTimes/141170" target="_blank">📅 09:35 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141169">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">🚨
علیرضا بیرانوند پس از استوری کنایه‌آمیز شجاع خلیل‌زاده، کاپیتان تراکتور را آنفالو کرد. شجاع هم اقدام متقابل کرد و بیرانوند را آنفالو کرد!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.07K · <a href="https://t.me/SorkhTimes/141169" target="_blank">📅 09:34 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141168">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">🚨
🚨
🚨
🚨
شجاع بیرو رو آنفالو کرده و ازهمه‌اعضای تراکتور خواسته که این بازیکن رو در اینستاگرام آنفالو کنند.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.01K · <a href="https://t.me/SorkhTimes/141168" target="_blank">📅 09:33 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141167">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">🚨
علیرضا بیرانوند: من به رختکن استقلال نرفتم. شبهات درباره صحنه گل هم درست نیست. می‌خوان به اعتبار و شخصیت من لطمه وارد کنن!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.01K · <a href="https://t.me/SorkhTimes/141167" target="_blank">📅 09:32 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141166">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">⭕️
حجت موتوری: همه بازیکن ها 8 درصد گرفتند ولی بیرانوند 35 درصد گرفته
😂
✔️
بیرانوند گوه خورده میخواد بره استقلال بعد خدمت سربازی هم با ما قرارداد داره
😂
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.23K · <a href="https://t.me/SorkhTimes/141166" target="_blank">📅 09:31 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141164">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/t2x72EWT1ydlW0wkw3Hyq5SIOIPijSXdGD9zVB5Y8dlnkvQFIf5fuke46QBoKpvFj9e12EvtEWPjXbv5jkLTaYrYFnclwNZ_uwfflM7So6aX8Rqq6u16J2vzXFffrhS_SLHvhreni57aCcZt5yfnVuKDbxLcXNJDpqfoghj38xA0wiRtxYuksRszROdjKaxsgwS1nH0k0dbBM4BcawBueqVeu6fvXEdP0Buxj50OM18iM6C2xip3qOssDf7fEY3cJCaKVvzWime1-Cx3XdvlwvCWxpRnk6p3K6UPMK5ff2cP4AHXkV4iwef7x-8zcYxNpd6SefVyKhkA9l2j4TTG4w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✖️
✅
✅
صبحتون خوش ارتش سرخ
❤️
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.16K · <a href="https://t.me/SorkhTimes/141164" target="_blank">📅 09:29 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141163">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HY4myRZgpM98Diarcgb8GJzLC6I0irNG_tVlSYZHxFhLRrTeI1ydnkMnINQ04k1hVROifCk_dlVEHTXTaJ082V36Uh5YHz64wWhPxw8qx6pPXM8znafSNbw_IJEdp9G42leKOKRhrzHC38dav4aXuNhU0g6IulIhk1A2ITSNEGSklhRYVgM6nY8nD8tnV3QpVgUcwawEuavFQEbj3aVZs5ds6SjKZN1fSiL-FclD5YBTBROIQpJxPVuQx2oZ0eRRj-_vApK67rijD1Weoqh3yW-RAm64_PtJReg1DuGRRibTV36EkF7f7qMWbgPtx3THFlmJTXtH-Id5Il8yzAUtNQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🕹
گردونه شانس رایگان وینکوبت رو از دست نده، همین الان وارد سایت شو و گردونه رو بچرخون!
🎰
هر ۱۲ ساعت یک‌بار شانس خودتان را امتحان کنید و جوایز نقدی متنوع دریافت کنید.
🎁
تا سقف ۱ میلیون تومان جایزه روزانه
✅
فعال برای تمامی کاربران
📌
برای شرکت در گردونه شانس، وارد ربات وینکوبت شوید:
👇
🤖
@Wincobet_bot
🤖
@Wincobet_bot
📌
کانال رسمی وینکوبت:
🔵
@Wincobetofficial</div>
<div class="tg-footer">👁️ 5.58K · <a href="https://t.me/SorkhTimes/141163" target="_blank">📅 01:03 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141162">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">🚨
استوری کنایه‌آمیز شجاع خلیل‌زاده به بیرانوند: تمام حقوق خود را گرفته‌ایم و از زنوزی متشکریم!
😂
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.73K · <a href="https://t.me/SorkhTimes/141162" target="_blank">📅 00:34 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141161">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lrBx91JL0EJWg2DelTy_UrnlajhIAjpTI04M_99CgTQUex_tTnndw-gICQWrwjtgwuV-Fb89mUxwHH40q2a8mm_ZbnAkDJcJHSQEIR6m_oRHSMc5dbJOtWsLgNommv4-APtGn4BvZB9Ay-9MUjkCkD45TiozJsqz9SUkIWOqWoyvR41MnoyRN7TR01QEPPZzkKk9eND7i2nTzVP4jyi2UXn2WzOOJSoLWWsRuIXoslAo6JQNdSKJY8b4eiPqrjtTDRF9FdZMfaK8YR_-UnK9x6n4_GRYttloD56qFZeFAYvpcgm6uMizpISHw1nzsc7Yu78Y0sImwexKCAnBorhuOw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
⭕️
بیرانوند تا الان عضو 5 باشگاه بوده که در هر 5 باشگاه به مشکل خورده و از اونجا به شکل غیر حرفه ای جدا شده!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.81K · <a href="https://t.me/SorkhTimes/141161" target="_blank">📅 00:32 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141160">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">🔴
👤
کنایه خداداد عزیزی به بیرانوند: اجازه هیچ حاشیه‌سازی را نخواهیم داد و از زنوزی بابت انضباط مالی قدردانی میکنم.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.84K · <a href="https://t.me/SorkhTimes/141160" target="_blank">📅 00:21 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141159">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Z3Ut1KqkHdrB0TBG6XQBOQQs8He9cPioOBhjUAuQ-VJTIL8oxnW0auJYSCiHdfyRDN_OsRnYgRlsEeoS-Je3cxDKcN8MuimKiDcQRZPZORl2bHfqkceXlqJ37qsmc8B0wvOAh_aHJvg3VoSinKjgmSB1R7ancj1xgy8Y_N_gsJIsfz-dipsSbzFlGPX4KV4SeaDI8D2EgrPkPouF5_qo6H6_U7_TskH8ypVPw8GiGwSR7antxbCoRLWA_QMGKEHQpeTkVZbNMjQHFX0oF-E5FNXk2IfMLXW7RnczXHoEo2Kjd17wAm-FNYOzeo2D_-K1VlVM6UPgk_uwvns8207utg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
کنایه خداداد عزیزی به بیرانوند: اجازه هیچ حاشیه‌سازی را نخواهیم داد و از زنوزی بابت انضباط مالی قدردانی میکنم.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.79K · <a href="https://t.me/SorkhTimes/141159" target="_blank">📅 00:20 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141158">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">🚨
استوری کنایه‌آمیز شجاع خلیل‌زاده به بیرانوند: تمام حقوق خود را گرفته‌ایم و از زنوزی متشکریم!
😂
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.8K · <a href="https://t.me/SorkhTimes/141158" target="_blank">📅 00:09 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141157">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/n8_TYVJ_3YEaphyfXk0iCy9cqh_cKLBivuYVT2bHt3Lz8sOrhMFLWqm07--3tq3YGRNM_NBROe93FX2X5ONQu5JtTLzxjv7FHS5tyUfyWEpNxuAclJoaYL3ddNxK0jS_jHO3RtRE_fS_LIKZtB5OQmLRcvQO5DPt7pYKbmjL0iCgCRawZpP6ExTE1DpkYxOGdv5bUxPlFs6zT0B9kgTAd5jhH9JqMzmXgS5pgOkfXWxtOQ5uOPZB4_Xf25QPbVdUAfo03pD74s-M04-1E2hb80LJ4SPiIFXC9VRqrVWB4bYClpB_9KFouMUPkO_XAHG3jRrIqoNcYJ9Bw2AkpSt1GQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
فووووووووووووری از آنا
🔹
باکیچ به دلایل فنی از لیست پرسپولیس کنار گذاشته شده و مصدومیتش کذب محضه!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.89K · <a href="https://t.me/SorkhTimes/141157" target="_blank">📅 00:09 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141155">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Jfq5URTkQwv_fr63UYb8Awtg9gMXnX7yXy-9KNdvp7jSOskOW6srGMD9oERIF5GnH7uj61bGSWNNFHFBegz2j9wcFZygFPABtm8FPkjmtzWUEjMdNQpIaexQd1vEkIAu9xb493Vw2FtXm9A7mZp5d1vsmSEdKBtcwKABG86BYTXc3W7bxkWMJU1GvlQWrL4jspLMR-94W8ak_Ncl8ixSlqdvzmDwM5PL_iORBt4nQ7HBrlXFyJebrmOfnT_2QZmVlB0QRygEHXGQPTY3HSdj2bbJu3HXFOwQonRTWl4i9VVrzZ-u3iUeKUBgbJetVOBB_IV16YPZM9V5gx_ZAOPwPQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
فووووووووووووری از آنا
🔹
باکیچ به دلایل فنی از لیست پرسپولیس کنار گذاشته شده و مصدومیتش کذب محضه!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.98K · <a href="https://t.me/SorkhTimes/141155" target="_blank">📅 23:24 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141154">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">🚨
22 پرسپولیسی برای بازی مقابل صنعت نفت وارد اردو شدند / یک نفر فردا خط خواهد خورد!
🔴
1_پیام نیازمند
🔴
2_امیررضا رفیعی
🔴
3_امیرحسین طاهری
🔴
4_ابوالفضل جلالی
🔴
5_محمد مهدی زارع
🔴
6_حسین ابرقویی نژاد
🔴
7_مجید عیدی
🔴
8_مهدی تیکدری
🔴
9_پوریا لطیفی فر
❗
10_محمد‌…</div>
<div class="tg-footer">👁️ 5.92K · <a href="https://t.me/SorkhTimes/141154" target="_blank">📅 23:02 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141153">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">🚨
22 پرسپولیسی برای بازی مقابل صنعت نفت وارد اردو شدند / یک نفر فردا خط خواهد خورد!
🔴
1_پیام نیازمند
🔴
2_امیررضا رفیعی
🔴
3_امیرحسین طاهری
🔴
4_ابوالفضل جلالی
🔴
5_محمد مهدی زارع
🔴
6_حسین ابرقویی نژاد
🔴
7_مجید عیدی
🔴
8_مهدی تیکدری
🔴
9_پوریا لطیفی فر
❗
10_محمد‌…</div>
<div class="tg-footer">👁️ 5.72K · <a href="https://t.me/SorkhTimes/141153" target="_blank">📅 22:53 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141152">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">⭕️
⭕️
مارکو باکیچ و دنیل گرا از لیست بازی فردا خط خورند.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.85K · <a href="https://t.me/SorkhTimes/141152" target="_blank">📅 22:51 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141151">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">❌
❌
باکیچ و لطیفی‌فر شانس برابری برای حضور در ترکیب فیکس پرسپولیس مقابل صنعت نفت دارن و تارتار هنوز تصمیم نهایی خودشو نگرفته/ایران‌ورزشی
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.52K · <a href="https://t.me/SorkhTimes/141151" target="_blank">📅 22:47 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141150">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VQ_tPfCijo6q8JU_HFfVt1TsAScufC2UOU6aohV9LUX7nBeScjzyQ8nqXY7Dqlqx_9JccQTlBXs9VOrf_KlU6s-ezERaxnaUbmxRoFWic8JeMM6fy1augcO7b1IV6HCI-WQW1j_-3H7e2gAvtTAdbjOFCiGKRcKNCne_Z5mrQzd6YNHVfK4bGeV6Nw8VYftxJ-d2W-ir0a276_7O7fVxKFVUSeAA_dCQ-dp3RkpfI11ld5Pr4jOInFEMwweOVRc5q2hsC90paUeYJiUOiTBbFlBjHTXqRUWY4cMowQTckMHdP8ttjHtPTtt7eDvm221EBFJQQG2g1GwVzkGpE_cIFA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⭕️
کنایه حجت‌کریمی به کم‌‌‌فروشی سرباز
✅
مدیر تراکتور گفته گلی که بیرانوند خورد باید از کارشناسان راجع‌بهش پرسید‌. منظورش این اشتباهه‌ فاحشه که توپ از زیر دستش رفت‌‌. به‌نظر میاد به کم‌فروشی بیرانوند و گمانه‌زنی رفتنش به استقلال اشاره کرده
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.7K · <a href="https://t.me/SorkhTimes/141150" target="_blank">📅 22:45 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141149">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">⭕️
حجت موتوری: همه بازیکن ها 8 درصد گرفتند ولی بیرانوند 35 درصد گرفته
😂
✔️
بیرانوند گوه خورده میخواد بره استقلال بعد خدمت سربازی هم با ما قرارداد داره
😂
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.6K · <a href="https://t.me/SorkhTimes/141149" target="_blank">📅 22:42 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141148">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">🚨
جواد نکونام به دلیل مصاحبه دروغ، بیرانوند رو اخراج کرد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.4K · <a href="https://t.me/SorkhTimes/141148" target="_blank">📅 22:40 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141147">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">❗️
⛔️
👀
پرسپولیس ب که قرار بود به سیدجلال سپرده شود، احتمالا با محسن بنگر وارد رقابت‌های دسته دوم لیگ آزادگان می شود...
‼️
🟥
به گزارش هفت ورزشی، پرسپولیس که دنبال خرید امتیاز برای راه‌اندازی تیم دوم بود، سرانجام امتیاز پادیاب خلخال را خرید‌.
گفته می‌شد هدایت پرسپولیس ب به سیدجلال حسینی سپرده می‌شود اما گویا باشگاه شرایطی دارد که مورد پسند سیدجلال نیست.
‼️
برابر با شنیده‌های ما سرمربی فقط حق دارد ۵ بازیکن برای تیم جذب کند که این پنج بازیکن هم از کانال مورد نظر باشگاه وارد تیم می‌شوند. بقیه بازیکنان را هم خود باشگاه به خدمت می‌گیرد.
انگار محسن بنگر این شرایط را پذیرفته و ظرف ۴۸ ساعت آینده به عنوان سرمربی تیم دوم پرسپولیس برای حضور در رقابت‌های دسته دوم لیگ آزادگان معرفی می‌شود.
‼️
راست یا دروغش گردن راوی که می‌گوید پرسپولیس امتیاز تیم پادیاب خلخال را گرانتر از قیمت عرف بازار خریداری کرده است. در خرید این امتیاز یکی از اعضای هیات مدیره که اهل استان‌های آذری زبان است نقش داشت.
همچنین رد پای یک عضو هیات رییسه فدراسیون فوتبال در این ماجرا دیده می شود، همان شخصی که یک دور مشاور مدیرعامل باشگاه بود.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
𝓣𝓲𝓶𝓮
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.66K · <a href="https://t.me/SorkhTimes/141147" target="_blank">📅 22:01 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141146">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">🚨
بیرانوند هم ظاهراً از همین حالا خودش را در استقلال می‌بیند! برای همین بدون نگرانی علیه زنوزی و مدیران تراکتور مصاحبه می‌کند. خودش هم از سربازی و بازیکن آزاد شدن حرف زده؛ انگار تصمیمش را برای آینده گرفته و دیگر نگرانی چندانی بابت واکنش مدیران باشگاه ندارد.…</div>
<div class="tg-footer">👁️ 5.78K · <a href="https://t.me/SorkhTimes/141146" target="_blank">📅 21:58 · 16 Mehr 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>

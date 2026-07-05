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
<img src="https://cdn4.telesco.pe/file/ImPoUW4ZnVcsvQH267dLrX65Qf-kW8VYx0FaFG0r47jYt5tXdYWj3qnEdyjYuD9dvLkK2fFZucj6JKVf6eGzi_MLnyz_ueZ_r-MoHvfgxnV0I-iWdhgZRYMRoBYYyY3OhkQQmtjkAKCnfs2uMvFgw2mEeiSydpSZFrnlziYAVkZHu3rvZU4dxFnRnMK4PAg6KinXRysshe5BsMZvxxzoBLhRjKYpyDVH6JINtdlz4nTsNSeIG1QKlUhaKD41H2XcYXfmLvHvFug1lbvJu8yNwaGWIZrO6F7XI4aCTboex7A3bWmh_t4ZknhmYjgvxc8GKpHLoIbOhaFSgX7aEHfQPg.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 🚩سرخ تایمز🚩</h1>
<p>@sorkhtimes • 👥 21.5K عضو</p>
<a href="https://t.me/sorkhtimes" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ﷽ورزشی نویس پرسپولیس👤🎗️«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس.⛔رسانه سرخ تایمز مسئولیتی در قبال تبلیغات ندارد.</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-14 14:06:16</div>
<hr>

<div class="tg-post" id="msg-135014">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">🚨
🚨
🚨
🔴
🔴
🔴
سرانجام تارتار به آرزوش رسید
🚨
ازش حمایت میکنین؟
👍
👎
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 999 · <a href="https://t.me/SorkhTimes/135014" target="_blank">📅 13:56 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135013">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">😀
دوماگوی دروژدک با پایان قراردادش از تراکتور جدا شد/ ورزش سه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.09K · <a href="https://t.me/SorkhTimes/135013" target="_blank">📅 13:55 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135012">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">🚨
فوری؛ با پرداخت 20 میلیارد، رضایت نامه مهدی تارتار برای پرسپولیس صادر شد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.25K · <a href="https://t.me/SorkhTimes/135012" target="_blank">📅 13:53 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135011">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/o0jCuFJes6TXRV1ZuD1LHlyvXFV_tMH0bOxOMz5XK0P_E5vo2vXFNe8xuVNmwG9YjUhqCFyMrp1CFLw64IJrtME_XqGlXkcVtoxfW1Rxphwi0BeFxG7sbcsS_zYsCBp5Nc7r_Y-oK9LooU0E45EEKfy9J4xHquASgmq-fWRadMBQgVGWpCJQjQ_YLa71Df3lBylyn3oYHjBTOam04zTxwdDuRTkkg6d9IFo5Jne1pu37tcgZd5iBFmpgH9sEkECVSbPb3VCUbKbEFvSeIMmdht9bfV8c4Vy38Au3GPIR6edtf6-tJmYA1LpCP1mPtD_OmT8TUx9RpWeVqpifOVThWQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
فوری؛ با پرداخت 20 میلیارد، رضایت نامه مهدی تارتار برای پرسپولیس صادر شد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.31K · <a href="https://t.me/SorkhTimes/135011" target="_blank">📅 13:53 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135010">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Rl7P8r9Io9dRZCy3ISaYvf5E22sj0sDxgY_jMSWBn34QgUK-87gYxvzdlcDtFh-tDMTJpc6W_B9-ohfgtTp8OpKYJ420sGfiAsnikp0580NTbRqdEFJ2YbArpcRNv9DEElkdjq_G4CCv4XxLyS2rUoFprbt01IPt7p_ghaebKBNqLvTZENB1gjNuJenx6iAEvMG6wXf28THOzLxo6bHJxJgGTfIkP1KxA5ONGKbDfxcTW9NR6vcCB2h--Ak1zMKr3nXZp25zcuID_7DOX782bGpqKqf1IAk9BzsNtyrhizWYuPA99CZOTeM1NoFifzONp_BtIYmJCBA8tAT5NQWBiA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
جام جهانی جای عجیبیه!
🔴
🔴
توی یک شب میتونی راه ۱۰۰ساله رو طی کنی و این معمولا برای دروازه بان ها میوفته
🔴
🔴
مثلا همین ووزینیا دروازه‌بان ۴۰ساله کیپ ورد که تا ۲۵سالگی زباله بازیافتی جمع آوری میکرده اما با یک شب درخشش شگفت انگیز از ۵۰ هزار فالوئر به نزدیک ۱۵میلیون…</div>
<div class="tg-footer">👁️ 1.43K · <a href="https://t.me/SorkhTimes/135010" target="_blank">📅 13:50 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135009">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">❗️
#فوری
؛ یورگن کلوپ سرمربی سابق لیورپول با عقد قرار دادی 4 ساله سرمربی تیم ملی آلمان شد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.4K · <a href="https://t.me/SorkhTimes/135009" target="_blank">📅 13:49 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135008">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-footer">👁️ 1.43K · <a href="https://t.me/SorkhTimes/135008" target="_blank">📅 13:48 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135006">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">melbet.apk</div>
  <div class="tg-doc-extra">52.1 MB</div>
</div>
<a href="https://t.me/SorkhTimes/135006" class="tg-doc-link" target="_blank">دانلود</a>
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
<div class="tg-footer">👁️ 1.94K · <a href="https://t.me/SorkhTimes/135006" target="_blank">📅 13:32 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135005">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">🔺
بانس‌های فوق خفن مل‌بت
🔺
🫴
100 درصد پاداش اولین واریز
😀
100 درصد بانس یکشنبه ها
🎁
100 درصد بانس چهارشنبه ها
🔹
هر روز 1 چرخش گردونه 1 یورویی
😀
3 درصد باز پرداخت نقدی
😀
بانس شرط رایگان 30 دلاری
🎩
10 درصد باز پرداخت نقدی کازینو
🎆
بانس هدیه روز تولد
💵
و چندین بانس دیگر از جمله بانس خوش‌آمد گویی، بانس شرطبندی طولانی مدت، بانس 1750 یورویی کازینو و...
💰
هنگام ثبت‌نام با وارد کردن کد هدیه Sport100 بانس 100 دلاری رایگان دریافت کنید!
🆕
معرفی سایت و اپلیکیشن مل‌بت
🆓
ورود به سایت مل‌بت (فیلترشکن خاموش)</div>
<div class="tg-footer">👁️ 1.88K · <a href="https://t.me/SorkhTimes/135005" target="_blank">📅 13:32 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135004">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">🚨
🚨
🚨
🔴
🔴
🔴
سرانجام تارتار به آرزوش رسید
🚨
ازش حمایت میکنین؟
👍
👎
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 2.25K · <a href="https://t.me/SorkhTimes/135004" target="_blank">📅 13:24 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135003">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/N1xAXeUKTqiMGvHsnnMHPE4q9RVa86PiycKo_Cjlq_AKRgFeGDrLJMnqiVsxidTyFNt9u1bO5ZmcKGGjP_hjD68qOs22-jwGzeuUYo4YIqNAJBcmf7MeW_6hFIEMuBWeoq-f66Wt0IcrRyW9C8uYrrS8QM5QspQxaa6JxLcJLP_1JK6I8amaCp9I2hA8sxZAfMKrGPkx0IrquH82wy9YMquiRk1EGJkAmVX8B7ZWGQhpSmmrJl1s5wspXFNl7kzfljjC4gB4fMxQCJxECT6qf5Cq2z2YvLUdGwJBG_gfWrOHVceEr24WC122v-0buljOHoZa85oVyy4FYiuK5U-0sg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🔴
🔴
🔴
سرانجام تارتار به آرزوش رسید
🚨
ازش حمایت میکنین؟
👍
👎
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 2.37K · <a href="https://t.me/SorkhTimes/135003" target="_blank">📅 13:22 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135002">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">🚨
باشگاه گل‌گهر سیرجان ساعتی پیش رضایت‌نامه مهدی تارتار را برای باشگاه پرسپولیس صادر کرد تا او سرمربی جدید سرخپوشان شود.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.01K · <a href="https://t.me/SorkhTimes/135002" target="_blank">📅 13:04 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135001">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">🚨
جلسه با تارتار در یوسف‌آباد و خارج از ساختمان باشگاه برگزار شد!
🔴
یک قدم تا مربیگری مهدی تارتار در پرسپولیس.
🔴
جلسه تارتار با فردی برگزار شد که شخصا اسکوچیچ رو در ترکیه هوا کرد.
✍
سپهرخرمی
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.04K · <a href="https://t.me/SorkhTimes/135001" target="_blank">📅 13:02 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135000">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fgv05UZxKqI7kIxBY7aJ-pWQlXnTU6RFYGE8bvmJSXgXDIM0AfGaNjq5SVOtQywlDKsV29HHXH8HddG7wTZNOKFZaPfsDCkKkGsDBxZh5l4sDsk9ZCdVvEfSUQVfgPIQUf6U2zrozw1oo00EzX_eZ8jc1XnHvpRvHwlY7jSms2d6XZKxtNYx01PDBzpvulskRBIsk5vm2HamBumCoUBD4vpcjamaY8HXEdeTs5Gpx_Hy2aiOR5tE-V-StaKquKEgcJIQ3wS0EaZVoVyRI1ejs3GAYCWHpn6GgyU5LlnSA1sALDqhWZ462Ml-_d3faItC8BwIiTfQYrF_eD1AbhBghQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
جلسه با تارتار در یوسف‌آباد و خارج از ساختمان باشگاه برگزار شد!
🔴
یک قدم تا مربیگری مهدی تارتار در پرسپولیس.
🔴
جلسه تارتار با فردی برگزار شد که شخصا اسکوچیچ رو در ترکیه هوا کرد.
✍
سپهرخرمی
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.16K · <a href="https://t.me/SorkhTimes/135000" target="_blank">📅 12:57 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134999">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">🚨
🚨
#تسنیم‌‌‌؛ مهدی تارتار در آستانه امضای قرارداد با پرسپولیس.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4K · <a href="https://t.me/SorkhTimes/134999" target="_blank">📅 12:20 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134998">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">🚨
🚨
#تسنیم‌‌‌؛ مهدی تارتار در آستانه امضای قرارداد با پرسپولیس.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.32K · <a href="https://t.me/SorkhTimes/134998" target="_blank">📅 11:45 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134997">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">✅
✅
باشگاه الشمال قطر با ارسال ایمیلی به پرسپولیس خواستار جذب اورونوف شد. این تیم اعلام کرد که حاضره 3.5 میلیون دلار برای‌ جذب اورونوف به‌ پرسپولیس پرداخت کنن
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.27K · <a href="https://t.me/SorkhTimes/134997" target="_blank">📅 11:43 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134996">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kAZ-MvfVYnM4bPWV-l_bl8azoPfRUo8FkfhKBPbJoXF54ikx505YGV6MZxLE6G7DkL7jcpvOk0y6HNa3tYnYhDqI6hbiJKKryqoWKSTSpRfJi1A2ZzJAFXas_CctinQEPCAsUvKn6-ndrpn5N51RDqBUXde1IR8M_MHdUOkTgOQCoIpJdKm2zveOMvzJjqOf6IVjpVL4kZSlqpCgSJI5_V-ARdpw3hAbLkXl2ug2U_0_Ctjvcu13cMrkHYvNOnWMjZyCVeIykZnu0-f0bILMEDyrvzbED8luMsv1amz_eaL31SZLQfbd6jLUCN0HO9evMOMSHFaKCeg-1kwHdWbS8g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
✅
بانک شهر از این موضوع اطلاع داره که اگه این فصل مثل سال گذشته رتبه پرسپولیس جزو چهار تیم برتر جدول نباشه قراردادش به عنوان مالک با سازمان خصوصی سازی فسخ میشه!؟
❗️
حالا برید دنبال انتخاب مربی ضعیف ایرانی و نقل و انتقالات ضعیف تر….!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.49K · <a href="https://t.me/SorkhTimes/134996" target="_blank">📅 11:10 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134995">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">❌
❌
قرمز آنلاین ؛ اگر تصمیم مدیریت و هیات مدیره به سمت مجتبی حسینی تغییر نکند تارتار سرمربی سرخ ها خواهد شد .
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.36K · <a href="https://t.me/SorkhTimes/134995" target="_blank">📅 11:08 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134994">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">❗️
❗️
#فووووووووری از قدوسی
🔴
تا ظهر سرمربی پرسپولیس مشخص میشه که احتمال خیلی زیاد آقای تارتار خواهد بود
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.47K · <a href="https://t.me/SorkhTimes/134994" target="_blank">📅 10:40 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134993">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">❗️
❗️
#فووووووووری از قدوسی
🔴
تا ظهر سرمربی پرسپولیس مشخص میشه که احتمال خیلی زیاد آقای تارتار خواهد بود
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.44K · <a href="https://t.me/SorkhTimes/134993" target="_blank">📅 10:39 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134992">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">✅
پاسخ یک مدیر ارشد باشگاه پرسپولیس به سوال قرمزانلاین : فردا به احتمال فراوان سرمربی معرفی می شود
❗️
این مقام مسوول ساعت ۱۲ و نیم بامداد به سوال ما پاسخ داد و به نظر می رسد منظورش از فردا همان دوشنبه باشد//قرمز آنلاین
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار…</div>
<div class="tg-footer">👁️ 4.35K · <a href="https://t.me/SorkhTimes/134992" target="_blank">📅 10:39 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134991">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">❗️
❗️
خبرورزشی: حدادی روز اخر مذاکره با اسکوچیچ که همزمان بود با روز عقد قرارداد دو تا بند به قرارداد اضافه کرد که اسکوچیچ مخالفت کرد و همه چیز کنسل شد
🔴
1_ اگه جنگ شد تا روزی که ایرانه پول بگیره
⏺
2– 500 هزار دلار از مبلغ توافق شده کم کنه
🎗️
«سرخ تایمز»…</div>
<div class="tg-footer">👁️ 4.32K · <a href="https://t.me/SorkhTimes/134991" target="_blank">📅 10:35 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134990">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">❌
۳ گزینه نهایی باشگاه پرسپولیس برای هدایت این تیم مشخص شدند:
⏺
مهدی تارتار
⏺
مجتبی حسینی
⏺
حمید مطهری
❌
شانس تارتار و حسینی تقریباً برابر بوده و شانس حمید مطهری کمتر از این دو نفر می‌باشد…
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.54K · <a href="https://t.me/SorkhTimes/134990" target="_blank">📅 09:11 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134989">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">❗️
دیگه همه گزینه شدن باید ببینیم کی مربی پرسپولیس میشه ....
❌
مازیار
❌
یحیی
❌
تارتار
❌
مطهری
❗️
مجتبی حسینی
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.56K · <a href="https://t.me/SorkhTimes/134989" target="_blank">📅 09:09 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134988">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/N4A-MS6JeqTh7P40JMAEDi6ufNAr23xahP0Hw6wtrsznG3426cRKIg5zRRqGKNOI8z6bvojV8i33tFJPtwvs4vMjJsciUX_YMpLYCgTH8J023gPgGz-jPlQmAV2O_Eg-cBykSYIiiKs40QYMtsFa2YhqrLAr3OusuSFauFHajcYb7MJM_oG3-6PtLtXAfaV2dz3Vg2D-ZAdB98sOLxTuMp2nugeJo_LWkcpDHSDrM-O7cOU-bbRghWYuDP7S_seI7tB_Ovj4EaD-5Dr4Nq4USQ3lrGxrTDLPhicUruzh5bM08TMVORbmjEF89fMD6Ofo5QnZ5ibDP9bAE0xahDG0Ug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
صبحتون بخیر ارتش سرخ
🚩
✨
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.5K · <a href="https://t.me/SorkhTimes/134988" target="_blank">📅 09:05 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134987">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">linebet.apk</div>
  <div class="tg-doc-extra">53.7 MB</div>
</div>
<a href="https://t.me/SorkhTimes/134987" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🪙
اپلیشیکن اندروید سایت جهانی لاین بت
💳
واریز و برداشت ریالی
🎁
هر دوشنبه ها تا سقف ۱۳ ملیون تومان بونوس ورزشی
🔗
بد نیاز ب فیلترشکن
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
<div class="tg-footer">👁️ 5K · <a href="https://t.me/SorkhTimes/134987" target="_blank">📅 01:56 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134986">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/izIB4TIIbgahN752LBKvPDCiQBl-ZO_CL791yB0iZexZTrZa4FkZ4Mi59SUsUyfUjScY4Fpi-pUO_M0mQ12YfpPvdTpBhhXIG_cjdr3mni_UDmvWG4hgnyaX_Gt5Kfd8nP52Qi5MHx2_RM7pubosJHOUQ1Kz_xQIP2gVvAS5vFtVXHXq7BNNE3f_Ps3V81vucND3VGyaXXUaMhfT2mmrvW9VqaXtQnEqQ_CekDP1aslrW2sOAsyJJik4YLB2jNKk5uwUvtivxFQM7JLbhHGoYFyJPX-8TOTnX0mj2GqgVbfYy8P-Whf8DqC8BuPuyHnFzbhtfh3xnNpA3ftyhg2kWg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 5.08K · <a href="https://t.me/SorkhTimes/134986" target="_blank">📅 01:56 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134985">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tS_Hl3I35DBo9qCp2sbAXXIDPdH59UZWkMCaUKE3YQXnK3ECossufGLyrQ_oxS_ot1u2iDjpN19ed5kE0LaIXbeUk0WYFCfDI1xWUANDdGxeH4ULu_nd-ZohrhtXdhw0vpaDFKOvush5YnhQlj0WrEbDRCb9hJ8BEifG4ncKSnJHCQ-9WQ7r9AAAKgX8EzCjisa3PSXNEh49WlDW3PnHcLluBgc6LozL55MC1Hl_63_XCzdZm5JbvGeHbZvUWtM2FYbgU1BGgfFq2BQSquBt2QoiR7aFbqPu6vLnXwAHNnW6c6c3HCPrbR_iXu6nGa5vasRRguZpkxLhaq3mUfppfw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❗️
یحیی گلمحمدی با حضور در تمرینات دهوک عراق به شایعات حضورش در پرسپولیس پایان داد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.13K · <a href="https://t.me/SorkhTimes/134985" target="_blank">📅 01:17 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134984">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">✅
✅
باشگاه پرسپولیس از ساعاتی پیش دوباره باب مذاکرات با اسکوچیچ را آغاز کرده است و کریم باقری مسئول راضی کردن اسکوچیچ برای برگشت به میز مذاکره است.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.29K · <a href="https://t.me/SorkhTimes/134984" target="_blank">📅 01:00 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134983">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">🔴
🔴
خداداد عزیزی: آقا کریم ترسو نیست ولی دوست ندارد اینجوری سرمربیگری را تجربه کند. آن هم باشگاه بزرگی مثل پرسپولیس. شاید او شرایط را مهیا نمی‌بیند.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.35K · <a href="https://t.me/SorkhTimes/134983" target="_blank">📅 00:55 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134982">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">❗️
❗️
کریم باقری آخرین راه ارتباطی باشگاه با اسکوچیچ
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.56K · <a href="https://t.me/SorkhTimes/134982" target="_blank">📅 00:41 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134981">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">✅
✅
شنیده ها :
🚨
انگار حدادی دریبلش خیلی رونالدینیویی بوده و دوباره رو میز مذاکره با اسکوچیچ نشسته است.//قدوسی
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.36K · <a href="https://t.me/SorkhTimes/134981" target="_blank">📅 00:40 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134980">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">🚨
🚨
🚨
🚨
🚨
فوری | حمید ابراهیمی:
🚨
مهدی مهدوی‌کیا سوپرایز بزرگ باشگاه پرسپولیس برای نیمکت سرمربیگری است!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.28K · <a href="https://t.me/SorkhTimes/134980" target="_blank">📅 00:39 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134979">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">🚨
🚨
🚨
🚨
🚨
فوری | حمید ابراهیمی:
🚨
مهدی مهدوی‌کیا سوپرایز بزرگ باشگاه پرسپولیس برای نیمکت سرمربیگری است!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.33K · <a href="https://t.me/SorkhTimes/134979" target="_blank">📅 00:37 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134978">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">⚠️
هوادار باید فشار بیاره کنسل بشه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس 𝓣𝓲𝓶𝓮
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.39K · <a href="https://t.me/SorkhTimes/134978" target="_blank">📅 00:36 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134977">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">⚠️
هوادار باید فشار بیاره کنسل بشه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس 𝓣𝓲𝓶𝓮
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.42K · <a href="https://t.me/SorkhTimes/134977" target="_blank">📅 23:51 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134976">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">✅
شنیده ها : محسن خلیلی دیروز با مهدی تارتار جلسه داشته و این مربی اعلام کرده در قرارداد جدیدش با گل گهر بند فسخی داره که میتونه به پرسپولیس بیاد!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.42K · <a href="https://t.me/SorkhTimes/134976" target="_blank">📅 23:50 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134975">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">🤩
#اختصاصی_سرخ_تایمز | #فوری
🤫
🏅
به گزارش رسانه «سرخ تایمز» و با اعلام مسئولان باشگاه پرسپولیس توافقات با مهدی تارتار انجام شده است و باید تارتار رو رسمأ سرمربی بعدی پرسپولیس بدونیم!
📚
مهدی تارتار یک دستیار اسپانیایی انتخاب کرده و با خودش به پرسپولیس میاره؛…</div>
<div class="tg-footer">👁️ 5.58K · <a href="https://t.me/SorkhTimes/134975" target="_blank">📅 23:25 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134974">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">🤩
#اختصاصی_سرخ_تایمز | #فوری
🤫
🏅
به گزارش رسانه «سرخ تایمز» و با اعلام مسئولان باشگاه پرسپولیس توافقات با مهدی تارتار انجام شده است و باید تارتار رو رسمأ سرمربی بعدی پرسپولیس بدونیم!
📚
مهدی تارتار یک دستیار اسپانیایی انتخاب کرده و با خودش به پرسپولیس میاره؛…</div>
<div class="tg-footer">👁️ 5.63K · <a href="https://t.me/SorkhTimes/134974" target="_blank">📅 23:23 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134972">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">🤩
#اختصاصی_سرخ_تایمز
|
#فوری
🤫
🏅
به گزارش رسانه «سرخ تایمز» و با اعلام مسئولان باشگاه پرسپولیس توافقات با مهدی تارتار انجام شده است و باید تارتار رو رسمأ سرمربی بعدی پرسپولیس بدونیم!
📚
مهدی تارتار یک دستیار اسپانیایی انتخاب کرده و با خودش به پرسپولیس میاره؛ همچنین فردا جلسه آخر بین پیمان حدادی و مهدی تارتار برگزار خواهد شد،که «شاید» منجر به رونمایی شود
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
𝓣𝓲𝓶𝓮
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.96K · <a href="https://t.me/SorkhTimes/134972" target="_blank">📅 23:20 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134970">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 5.56K · <a href="https://t.me/SorkhTimes/134970" target="_blank">📅 23:13 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134969">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">❌
همه دوست داشتیم اسکوچیچ بیاد ...ولی با شرایطی که گذاشته بود .مبلغی که میخواست بگیره .کار و سخت کرده بود
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.83K · <a href="https://t.me/SorkhTimes/134969" target="_blank">📅 22:17 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134968">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">❌
پیشکسوتان پرسپولیس! همچنان علاقمند هستند مهدی تارتار سرمربی پرسپولیس شود و به دنبال فشار آوردن به هیات مدیره باشگاه برای انتخاب او هستند!
🔴
🔴
مهدی تارتار حمایت های علی پروین، خودش رو تبدیل به گزینه اول سرمربیگری پرسپولیس کرده!
🎗️
«سرخ تایمز» دریچه ای تازه…</div>
<div class="tg-footer">👁️ 5.72K · <a href="https://t.me/SorkhTimes/134968" target="_blank">📅 22:14 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134967">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">🚨
🚨
🚨
🚨
🚨
فووووری از قدوسی: مهدی تارتار به احتمال زیاد تا ۴۸ ساعت آینده بعنوان سرمربی پرسپولیس انتخاب خواهد شد
😐
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.89K · <a href="https://t.me/SorkhTimes/134967" target="_blank">📅 21:53 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134966">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.64K · <a href="https://t.me/SorkhTimes/134966" target="_blank">📅 21:53 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134965">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">🔴
مارکو باکیچ: دوست دارم وحید هاشمیان به ‌پرسپولیس برگردد
😕
😕
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.5K · <a href="https://t.me/SorkhTimes/134965" target="_blank">📅 21:51 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134964">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">❗️
دیگه چاره ای نیست باید حمایت کنیم ..دیگه باید بپزیریم .شرایط مملکت جنگیه و هر لحظه احتمال جنگ هست ..خارجی نمیاد ..اگه هم بیاد ..جنگ بشه سریع فرار کرده و کل پولش و گرفته
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.28K · <a href="https://t.me/SorkhTimes/134964" target="_blank">📅 21:44 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134963">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">https://t.me/+Bt80HN28Ils5YWE0
همه فرما رایگانه رفقا
✅
✅
⭕️
فرمهای امروز از بازیهای جام جهانی رو از دست ندین
#VIPرایگان</div>
<div class="tg-footer">👁️ 5.25K · <a href="https://t.me/SorkhTimes/134963" target="_blank">📅 21:43 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134962">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ji7O6RRKo3owm4DiwkrJPbReMWTvbT7A52rEhb9OpwJsQOmUjBpnhX6MwnuIrfNb9CJI_F75CjusDeHqmRvdk9MCBVU9xqcYvYeO8LJlOsgWAp2uYrwVMhYAvyaqmeGG1UBRVqBuaFaJP7PGD2rIy1TQBWCTWclybXQFhIv51-ZwE9_lv4LCor8qbWDg43jzluZ1zq4uzctRVXnglUFn7-CpWjxR7JQmQjXB4TULdjSg3siele_H6gBx8YQ25--XiWDQnap4S1tC4SIGcFqR6ue8T2XpK0qBctvwCGrXP-jgmqwXMJajkv6KErHo0wSASLbvEV56l5Uq8QJOEaTyyg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
دوستان بت زن این کانال مخصوص شماست
بهترین آنالیز ها و آموزش ها
🆓
📈
اشتراک سایت های معروف خریداری میشه و براتون رایگان قرار میدن
💥
🥇
آموزش های جذاب و سود ده در مورد شرطبندی فوتبال
💡
چالش و قرعه کشی ها با جوایز دلاری
💵
✔️
⬇️
⬇️
روی لینک کلیک کنید
⬇️
⬇️
https://t.me/+Bt80HN28Ils5YWE0
https://t.me/+Bt80HN28Ils5YWE0
🏆
فرم از بازی امروز
🇫🇷
فرانسه و پاراگوئه
🇵🇾
با ضریب 3.50 گذاشته شد</div>
<div class="tg-footer">👁️ 5.19K · <a href="https://t.me/SorkhTimes/134962" target="_blank">📅 21:43 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134961">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">✅
✅
حاج مهدی تارتار بلاخره به آرزویش رسید ..امیدوارم صدش و بزاره و قدر این محبت خدارو بدونه ....
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.81K · <a href="https://t.me/SorkhTimes/134961" target="_blank">📅 21:42 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134960">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">🚨
🚨
🚨
🚨
🚨
فووووری از قدوسی: مهدی تارتار به احتمال زیاد تا ۴۸ ساعت آینده بعنوان سرمربی پرسپولیس انتخاب خواهد شد
😐
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.95K · <a href="https://t.me/SorkhTimes/134960" target="_blank">📅 21:41 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134959">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/tMaBc8ySZ2wXTNHZXBfsr0zXZR2t032y3EpsCFd4zx7N4aW-7C6rj1ldaYfcgvKm6923Wl9SqJFjzCnDHl7YBqIRvrGSx5mijAkYXMHipqam9ztOk3Whrn2cGHqmBbC_fm91VHD1dXafdCsUlDZAmOVfE2iMOtMd_ZCuAdiD8A_pzz4NzePZUHzuT3y8xamO7iHUhemaz2Vl8Uj1QcN3MhWMWiB9GJ0IG0XY_W10pGiNJ1EzqCWzpx_6Y1M6yt66hx8N_VanEwdWCVxZEW_t97F5f7H1uQTLWEInEzKWQsCY1y3LFqaN56ILkJjE_0fpQyh_a2rFhM4xbACppdNL1A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🚨
🚨
فووووری از قدوسی: مهدی تارتار به احتمال زیاد تا ۴۸ ساعت آینده بعنوان سرمربی پرسپولیس انتخاب خواهد شد
😐
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.34K · <a href="https://t.me/SorkhTimes/134959" target="_blank">📅 21:39 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134958">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">🚨
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 5K · <a href="https://t.me/SorkhTimes/134958" target="_blank">📅 21:37 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134957">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">❗️
دیگه همه گزینه شدن باید ببینیم کی مربی پرسپولیس میشه ....
❌
مازیار
❌
یحیی
❌
تارتار
❌
مطهری
❗️
مجتبی حسینی
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.16K · <a href="https://t.me/SorkhTimes/134957" target="_blank">📅 21:36 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134956">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">🚨
🚨
سرمربی جدید و ایرانی پرسپولیس فردا نهایتا پس فردا مشخص خواهد شد/قدوسی
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.09K · <a href="https://t.me/SorkhTimes/134956" target="_blank">📅 21:21 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134955">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">❗️
دیگه همه گزینه شدن باید ببینیم کی مربی پرسپولیس میشه ....
❌
مازیار
❌
یحیی
❌
تارتار
❌
مطهری
❗️
مجتبی حسینی
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.2K · <a href="https://t.me/SorkhTimes/134955" target="_blank">📅 21:08 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134954">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">✅
✅
باشگاه الشمال قطر با ارسال ایمیلی به پرسپولیس خواستار جذب اورونوف شد. این تیم اعلام کرد که حاضره 3.5 میلیون دلار برای‌ جذب اورونوف به‌ پرسپولیس پرداخت کنن
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.14K · <a href="https://t.me/SorkhTimes/134954" target="_blank">📅 21:02 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134953">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">✅
⚽️
❤️
عبور اوستون ارونوف از آلن ویتل
🔴
اوستون ارونوف با گلی که به سپاهان زد، با پیراهن پرسپولیس ۱۵ گله شد و به این ترتیب از رکورد ۱۴ گل آلن ویتل گذشت.
🔴
ملی پوش ازبکستانی پرسپولیس حالا در جدول گلزنان خارجی پرسپولیس در رتبه دوم قرار دارد.
🔴
همچنین سرگیف، هم‌وطن…</div>
<div class="tg-footer">👁️ 5.15K · <a href="https://t.me/SorkhTimes/134953" target="_blank">📅 21:02 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134952">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">🚨
ترامپ به آکسیوس: همه آن‌ها آنجا هستند. یک گلوله [و می‌توانیم همه آن‌ها را از بین ببریم]، اما ما این کار را نخواهیم کرد، زیرا در آن صورت، هیچ‌کس برای مذاکره با ما نخواهد ماند.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.21K · <a href="https://t.me/SorkhTimes/134952" target="_blank">📅 20:54 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134951">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">❌
❌
مارکو باکیچ:
🔴
دعوا توی رختکن بین اعضای تیم و کادرفنی یه چیز طبیعی توی دنیاس و حتی توی اروپا خیلی شدید تره؛ اما تفاوتش با اینجا اینه که توی اروپا این موضوع رسانه ای نمیشه اما توی ایران بیش از حد بهش پرداخته میشه.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق…</div>
<div class="tg-footer">👁️ 5.12K · <a href="https://t.me/SorkhTimes/134951" target="_blank">📅 20:49 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134950">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Mom0LU0huw-zy6TUOs-pVxMec4GoHdFsWPxb0nNmRZIF3kmyp2x_KCSY3mzFe7qvWX_94Pq0CfzZOcngNudqHX2wLTR2wwDyTG3hCntQTdJO8WLdvFFW0NzFsRNM80U3zv2ZmZd1n5ELb-6AzkSMB0vJxSL7fW6HQOCLvjJ1AoP9fCVzDJ_D0JkLzc7jof87MWM02DndVdP66SuGj2bGhqSzZosyHG8te4IpFEhGXmEP7qJeRoyEYcSL-zj-642d92vZHJQcSTFgYkp2zhTF2eOy_KdJ3qrKoPNdnFugbZZs5Kb71fCUw4UB7_XyYIYA8nvWKrlg2jKY7WqDAuwAnQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
ترامپ به آکسیوس: همه آن‌ها آنجا هستند. یک گلوله [و می‌توانیم همه آن‌ها را از بین ببریم]، اما ما این کار را نخواهیم کرد، زیرا در آن صورت، هیچ‌کس برای مذاکره با ما نخواهد ماند.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.23K · <a href="https://t.me/SorkhTimes/134950" target="_blank">📅 20:37 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134949">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">❗️
❗️
حمید ابراهیمی خبرنگار ورزش سه :
🔴
ماجرای خیلی ساده است! عضو هیات مدیره با بازیکنای مازاد بسته تا قراردادشون تمدید بشه و به کمک سخنگوی سکه ای مدیرعامل رو زمین بزنن و با دور کردن سرمربی مدنظر انتخاب خودشون رو داشته باشن و در نهایت مدیرعامل بشن!
🎗️
«سرخ تایمز»…</div>
<div class="tg-footer">👁️ 5.2K · <a href="https://t.me/SorkhTimes/134949" target="_blank">📅 20:10 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134948">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">❗️
دیگه همه گزینه شدن باید ببینیم کی مربی پرسپولیس میشه ....
❌
مازیار
❌
یحیی
❌
تارتار
❌
مطهری
❗️
مجتبی حسینی
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.14K · <a href="https://t.me/SorkhTimes/134948" target="_blank">📅 20:09 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134947">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">❗️
باشگاه گلگهر سیرجان که اخیرا قرارداد مهدی تارتار رو تمدید کرد بندی در قراردادش گنجانده شده درصورتیکه باشگاه پرسپولیس این سرمربی رو بخواهد با پرداخت 20 میلیارد تومان رضایت نامه تارتار صادر خواهد شد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس…</div>
<div class="tg-footer">👁️ 5.41K · <a href="https://t.me/SorkhTimes/134947" target="_blank">📅 19:55 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134946">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">🚨
🚨
#فارس ؛ مهدی تارتار در یک قدمی نیمکت پرسپولیس!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.49K · <a href="https://t.me/SorkhTimes/134946" target="_blank">📅 17:27 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134945">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qNN2kM4vy19A4Qd0vDfPa1RGR_PyJzUCO7CAkLOa3u_N2RQDST-Mk7jVSbB8RM9-mXAFuN2YERmXcZfoMQ1LaJiLIqXbi0UQjoxIbCcpCHg6ti1eYc0Sg2mAJMGJgUTqRDrCvWQl-V-SamGKmubAGzB9EuEL5JuthATYYuvS_3F1TSNVumregSekt8hSZson8awCQSjUMTLpI-H2psdme2nxSHTzq1h3ifLQR0eyU3GJ9RRxNxq-2g_PVX4xt0bUANEVLwitkHYDGxxuklv_3jnA59t2peh38FaqeKiYHwoibsa7FgLznzuEktWUrnMSqfGNDeldTUd7usr4QdRepg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
فووووری از فوتبالی: باشگاه پرسپولیس به دنبال عقد قرارداد با فاتح تریم است، سرمربی ترک تبار 2 میلیون دلار درخواست کرده است اما مدیران باشگاه پرسپولیس بیشتر از 1,5 میلیون دلار نمیدهند.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.81K · <a href="https://t.me/SorkhTimes/134945" target="_blank">📅 16:39 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134944">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">❗️
دیگه همه گزینه شدن باید ببینیم کی مربی پرسپولیس میشه ....
❌
مازیار
❌
یحیی
❌
تارتار
❌
مطهری
❗️
مجتبی حسینی
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.51K · <a href="https://t.me/SorkhTimes/134944" target="_blank">📅 16:38 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134943">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">🚨
🚨
#فارس ؛ مهدی تارتار در یک قدمی نیمکت پرسپولیس!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.64K · <a href="https://t.me/SorkhTimes/134943" target="_blank">📅 16:27 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134942">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">🚨
🏅
تفکرات علی پروینی به پرسپولیس نزدیک شدند
💥
بازگشت به روز های سیاه دهه هشتاد؟
⚠️
بعد از منتفی شدن بازگشت یحیی گل‌محمدی و در شرایطی که اختلاف مالی میان دراگان اسکوچیچ و باشگاه پرسپولیس همچنان زیاد است، برخی گزینه‌های داخلی با کمک جریان‌های رسانه‌ای در تلاش…</div>
<div class="tg-footer">👁️ 5.47K · <a href="https://t.me/SorkhTimes/134942" target="_blank">📅 16:25 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134941">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">🚨
🏅
تفکرات علی پروینی به پرسپولیس نزدیک شدند
💥
بازگشت به روز های سیاه دهه هشتاد؟
⚠️
بعد از منتفی شدن بازگشت یحیی گل‌محمدی و در شرایطی که اختلاف مالی میان دراگان اسکوچیچ و باشگاه پرسپولیس همچنان زیاد است، برخی گزینه‌های داخلی با کمک جریان‌های رسانه‌ای در تلاش هستند خود را به نیمکت پرسپولیس نزدیک کنند.
⚠️
یکی از این نام‌ها، مهدی تارتار است؛ مربی‌ای که با وجود حضور در گل‌گهر و برخورداری از امکانات یک باشگاه صنعتی، نه جامی کسب کرده و نه افتخاری فراتر از رتبه‌های پنجم در کارنامه دارد. او حتی اخیرا هم در رقابت برای سهمیه آسیایی هم ناکام ماند و شکست سنگین پنج بر صفر در خانه مقابل چادرملو هنوز از یادها نرفته است.
⚠️
سؤال اینجاست؛ آیا نیمکت پرسپولیس آن‌قدر کوچک شده که مربی‌ای بدون حتی یک جام و با این کارنامه، صرفاً با فشار رسانه‌ای، گزینه هدایت بزرگ‌ترین باشگاه ایران شود؟ پرسپولیس به مربی‌ای صاحب‌سبک، جسور، اهل جوان‌گرایی و قهرمان نیاز دارد، نه گزینه‌ای که مهم‌ترین رزومه‌اش حمایت رسانه‌ای باشد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
𝓣𝓲𝓶𝓮
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.52K · <a href="https://t.me/SorkhTimes/134941" target="_blank">📅 16:08 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134940">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">❗️
دیگه همه گزینه شدن باید ببینیم کی مربی پرسپولیس میشه ....
❌
مازیار
❌
یحیی
❌
تارتار
❌
مطهری
❗️
مجتبی حسینی
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.35K · <a href="https://t.me/SorkhTimes/134940" target="_blank">📅 15:50 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134939">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">✅
✅
فووووووووووووری
✅
✅
ورزش سه: پرسپولیس با حمید مطهری و مازیار زارع وارد مذاکره شد
😆
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.32K · <a href="https://t.me/SorkhTimes/134939" target="_blank">📅 15:44 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134938">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">✅
✅
شنیده ها: با وساطت سید جلال حسینی، مدیران باشگاه پرسپولیس امروز با مازیار زارع سرمربی ملوان بندر انزلی وارد مذاکره شدند و جلسه ای با این مربی برگزار کردند
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.22K · <a href="https://t.me/SorkhTimes/134938" target="_blank">📅 15:42 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134937">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">✅
باشگاه پرسپولیس: مذاکرات با گزینه سرمربیگری در چارچوب منافع باشگاه دنبال می‌شود ‌
🔴
سخنگوی باشگاه پرسپولیس تأکید کرد تصمیم نهایی درباره انتخاب سرمربی فصل آینده بر اساس جمع‌بندی فنی، اقتصادی و مدیریتی اتخاذ خواهد شد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق…</div>
<div class="tg-footer">👁️ 5.11K · <a href="https://t.me/SorkhTimes/134937" target="_blank">📅 15:36 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134936">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">✅
✅
شنیده ها: با وساطت سید جلال حسینی، مدیران باشگاه پرسپولیس امروز با مازیار زارع سرمربی ملوان بندر انزلی وارد مذاکره شدند و جلسه ای با این مربی برگزار کردند
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.83K · <a href="https://t.me/SorkhTimes/134936" target="_blank">📅 15:34 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134935">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">✅
✅
شنیده ها: با وساطت سید جلال حسینی، مدیران باشگاه پرسپولیس امروز با مازیار زارع سرمربی ملوان بندر انزلی وارد مذاکره شدند و جلسه ای با این مربی برگزار کردند
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.99K · <a href="https://t.me/SorkhTimes/134935" target="_blank">📅 15:33 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134934">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">❗️
❗️
شنیده ها: باشگاه داره با یک مربی فرانسوی صحبت میکنه!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.09K · <a href="https://t.me/SorkhTimes/134934" target="_blank">📅 15:33 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134933">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">MelBet2.apk</div>
  <div class="tg-doc-extra">53.8 MB</div>
</div>
<a href="https://t.me/SorkhTimes/134933" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🆕
اپلیکیشن MelBet
🔄
🎁
کد هدیه 100 دلاری:
Sport100
🤝
اسپانسر رسمی جام جهانی
🔵
کاملترین برنامه موبایل
☄️
صرافی معتبر
🤖
ربات راهنما
🇮🇷
برای تغییر زبان برنامه، زبان موبایل خود را تغییر دهید.
✅
ورود به اپلیکیشن بدون فیلترشکن</div>
<div class="tg-footer">👁️ 4.88K · <a href="https://t.me/SorkhTimes/134933" target="_blank">📅 14:56 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134932">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/mDBAG8eNdxiULvpj7_U0SsnES5u9NlcmxJMMWZPpfi4YT0AuL4kBlWeUN65JLNZOUAr5JKyAvZ342FGu8OJs9TfmHT81N2sX7-CJaVvXcb313y7Rer1Yw7I7-5s84WwrjOY5yGK2MvIpi3MZLfc6q3vv_AaEmFDpQaqwLn4b6GyQoVO7Fv4TaD-qTcIjed3lo_lH0wvziM8m9oiN8ZfwfuXNx1poQNPzPB0rAwVlCUc41WVaP_YmGU4QSm7QHMzrTWBhYtbYXVJLsS-REqYsKRxbhinAsOZGDlV59wM-Qfza7bZ7TRtsoxPpNcNuvVt07Hc2OlmP0klq52I9B4b-pQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">▶️
بازی فوووق جذااااب
کانادا
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
<div class="tg-footer">👁️ 5.03K · <a href="https://t.me/SorkhTimes/134932" target="_blank">📅 14:56 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134931">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">❌
❌
ابوالفضل جلالی که قراردادش با استقلال تموم شده، دوست داره به پرسپولیس بره. چون بازیکن آزاده، پرسپولیس شرایط جذبش رو بررسی می‌کنه، اما تصمیم نهایی رو سرمربی جدید تیم می‌گیره.
🔴
فرهیختگان
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.16K · <a href="https://t.me/SorkhTimes/134931" target="_blank">📅 13:48 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134930">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">❌
استوری دراگان اسکوچیچ :
🔴
تلاش‌ها برای جلوگیری از بازگشتم و پخش کردن دروغ درباره جدایی‌ام از ایران، مرا تضعیف نکرد؛ بلکه فقط ترس کسانی را که پشت پرده فعالیت می‌کنند آشکار کرد.
🔴
نحوه مدیریت مذاکرات توسط باشگاه، تنها نشان داد که این باشگاه در مذاکرات جدیت…</div>
<div class="tg-footer">👁️ 5.27K · <a href="https://t.me/SorkhTimes/134930" target="_blank">📅 13:34 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134929">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">#نظر_شخصی
🤩
من مقصر این وضعیت رو «فقط بانک» شهر نمیدونم این نظر منه
☑️
ببینید تیم هیچ دغدغه مالی نداره، هیچ بدهی ای نداره، حدادی بالغ بر ۵۰۰ میلیارد درآمدزایی داشته و بانک شهر کاملا ساپورت مالی کرده
📚
از دید من علت نتیجه نگرفتن پرسپولیس چندین علت داره،…</div>
<div class="tg-footer">👁️ 5.3K · <a href="https://t.me/SorkhTimes/134929" target="_blank">📅 13:31 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134928">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">❌
استوری دراگان اسکوچیچ :
🔴
تلاش‌ها برای جلوگیری از بازگشتم و پخش کردن دروغ درباره جدایی‌ام از ایران، مرا تضعیف نکرد؛ بلکه فقط ترس کسانی را که پشت پرده فعالیت می‌کنند آشکار کرد.
🔴
نحوه مدیریت مذاکرات توسط باشگاه، تنها نشان داد که این باشگاه در مذاکرات جدیت…</div>
<div class="tg-footer">👁️ 5.27K · <a href="https://t.me/SorkhTimes/134928" target="_blank">📅 13:30 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134927">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">🚨
🚨
🚨
شنیده ها: پاتریس کارترون گزینه پرسپولیس در صورت عدم توافق نهایی با اسکوچیچ!!!!!!!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.23K · <a href="https://t.me/SorkhTimes/134927" target="_blank">📅 13:28 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134926">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">#نظر_شخصی
🤩
من مقصر این وضعیت رو «فقط بانک» شهر نمیدونم این نظر منه
☑️
ببینید تیم هیچ دغدغه مالی نداره، هیچ بدهی ای نداره، حدادی بالغ بر ۵۰۰ میلیارد درآمدزایی داشته و بانک شهر کاملا ساپورت مالی کرده
📚
از دید من علت نتیجه نگرفتن پرسپولیس چندین علت داره،…</div>
<div class="tg-footer">👁️ 5.37K · <a href="https://t.me/SorkhTimes/134926" target="_blank">📅 13:03 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134925">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aflXSghYdWZc1g0TKKdn5lCBt-b81Jlc_mB8Ii1MI-CvQEoMY5ylio_BuEE5TPwX673YkA3TOV8BFo687_ZxqCt3ySmkQ4tUqw2bDCyHamtueeV68X0XjqddKy54RFJ-Bsi1Jk_YqmKJ9clUdzRF7UqAqCwP8VcQXbSshY9QojV0Cq14LacqwZJcp5v2QqVv7Gwou6aLHRxR-xiEx7ptJ26MsNYU5K1-YYlU-v6rdS3tIpiovphgdwqWWlHiojQbdGiRHI-KqLJ7R7TTSYcdb49OsW5_0vginpLNiBXBlgicJyXx0YUF96CFufjV9R_WDfgYvIzsvSWXSN6u6zSXPA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
جام جهانی جای عجیبیه!
🔴
🔴
توی یک شب میتونی راه ۱۰۰ساله رو طی کنی و این معمولا برای دروازه بان ها میوفته
🔴
🔴
مثلا همین ووزینیا دروازه‌بان ۴۰ساله کیپ ورد که تا ۲۵سالگی زباله بازیافتی جمع آوری میکرده اما با یک شب درخشش شگفت انگیز از ۵۰ هزار فالوئر به نزدیک ۱۵میلیون…</div>
<div class="tg-footer">👁️ 5.09K · <a href="https://t.me/SorkhTimes/134925" target="_blank">📅 12:52 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134924">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">❌
❌
ابوالفضل جلالی که قراردادش با استقلال تموم شده، دوست داره به پرسپولیس بره. چون بازیکن آزاده، پرسپولیس شرایط جذبش رو بررسی می‌کنه، اما تصمیم نهایی رو سرمربی جدید تیم می‌گیره.
🔴
فرهیختگان
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.04K · <a href="https://t.me/SorkhTimes/134924" target="_blank">📅 12:50 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134923">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">❗️
خداداد عزیزی: پلن B پیشنهادی ما به پرسپولیس یحیی گل‌محمدی بود، با یحیی حرف زدم در قراردادش بند فسخ وجود دارد که از دهوک جدا شود.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.01K · <a href="https://t.me/SorkhTimes/134923" target="_blank">📅 12:48 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134922">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">❗️
برنامه بازی‌های امشب مرحله یک هشتم نهایی که برای اولین‌بار ساعت‌هاش مثل آدمی زاده
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.13K · <a href="https://t.me/SorkhTimes/134922" target="_blank">📅 12:26 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134921">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">✅
سفیر آمریکا در سازمان ملل: صبر ترامپ نسبت به ایران در حال تمام شدن است.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.13K · <a href="https://t.me/SorkhTimes/134921" target="_blank">📅 12:24 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134920">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FWTlsLtPaOMBMAqUculh7-Mtqo8bDEC4UBvZtvxIopR6L0x5wKBJ15vCBa_7gVnnd5d8u5tFdLEFlsd6t2i2Klerrp9JRHOe15tuNSN37MvqjnsxB9v1cjd50u79NXWQZeHQ9rShSPqbiZCW6fgX-CmDr-SvIRotTAs-rdDwO2tgY82ddWd5hh9jr0lUZyRhjHPB7x0qu7pQ9vsLk-l987N9V639uemCUOo4QopmhDENHi8BBhZ6eKA8oPFyjkIVbUF2lIR89_TrVfKsxq4lJc6oLJs-YwWEvWy00KK6haQE54V6GBIb09CY77n2ypR4HquRs0R23wJKnM3wHyPzFA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
نتایج بازی های بامداد امروز
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.1K · <a href="https://t.me/SorkhTimes/134920" target="_blank">📅 12:22 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134919">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2fb54955fa.mp4?token=AGhZP5YRE1lpKKmGZBYIzARu7AJqkYZF-uB4QWC6L1OKKYLcAmPqs_V5QDHST9MuCSVZzRTzckNH4ssoH1TqdSCRsAOXO_RLVpwO0j2YCoIJ0HvapcIQwHFrxr_457sVxbVhRMQ8dYYYN5lLivmcMZF-eMw1tPl-3LCsZ1pahThXe7TFt48yryBvoePraPE97GObpfWo1hZlf2O4VKCzicH7QhtJ3pErRipdO13WKHmdv9I-nJ0l9trY7DeI79LDSRjQ2B5_2ceMdQYpIe2JknHJqIti8mXYeR6pC7B4cj0pJtxcX-Vl-zNdF4ckn17ihaWTucUOpzTRgzYmwKhh1A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2fb54955fa.mp4?token=AGhZP5YRE1lpKKmGZBYIzARu7AJqkYZF-uB4QWC6L1OKKYLcAmPqs_V5QDHST9MuCSVZzRTzckNH4ssoH1TqdSCRsAOXO_RLVpwO0j2YCoIJ0HvapcIQwHFrxr_457sVxbVhRMQ8dYYYN5lLivmcMZF-eMw1tPl-3LCsZ1pahThXe7TFt48yryBvoePraPE97GObpfWo1hZlf2O4VKCzicH7QhtJ3pErRipdO13WKHmdv9I-nJ0l9trY7DeI79LDSRjQ2B5_2ceMdQYpIe2JknHJqIti8mXYeR6pC7B4cj0pJtxcX-Vl-zNdF4ckn17ihaWTucUOpzTRgzYmwKhh1A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
از مدیرای بی غیرت خودمون که فعلا خبری نیست پلن B و C و G باشگاه رو از این افغانی پیگیری کنیم انگار زودتر به نتیجه میرسیم !!!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.97K · <a href="https://t.me/SorkhTimes/134919" target="_blank">📅 12:18 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134918">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">✅
شنیده ها : محسن خلیلی دیروز با مهدی تارتار جلسه داشته و این مربی اعلام کرده در قرارداد جدیدش با گل گهر بند فسخی داره که میتونه به پرسپولیس بیاد!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.02K · <a href="https://t.me/SorkhTimes/134918" target="_blank">📅 11:49 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134917">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">❗️
❗️
قدوسی : جدی ترین تماسها از بین گزینه های داخلی با مهدی تارتار صورت گرفته و تارتار گفته میتونه از گلگهر جدا بشه.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.18K · <a href="https://t.me/SorkhTimes/134917" target="_blank">📅 11:49 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134916">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">❌
❌
#فارس‌؛ اسکوچیچ که کلا کنسل شد رفت، پنج تا مربی ایرانی تو گزینه های حدادی ان که یحیی و تارتار از همه پررنگ ترن و احتمالشون بالاست.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.3K · <a href="https://t.me/SorkhTimes/134916" target="_blank">📅 11:20 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134915">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">❗️
❗️
تسنیم اعلام کرده گزینه‌های سرمربیگری پرسپولیس یحیی گل‌محمدی، مهدی تارتار و مجتبی حسینی هستن!
🔴
خجالت نکشید! حمید درخشان و بهروز رهبری فرد و پایان رأفت و حمید استیلی رو هم گزینه کنید!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.37K · <a href="https://t.me/SorkhTimes/134915" target="_blank">📅 11:19 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134914">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">❗️
🇦🇷
🇨🇻
نانا کواکو بونسام:
🔴
من با نیروهای ماورایی و روح اجدادم مشورت کردم. به مسی فقط اجازه داده شده بود که در این جام جهانی 6 گل بزنه و اون همین حالا سهمیه‌اش رو پر کرده است. ارواح به من نشان دادن که در حساس‌ترین لحظه، مقابل یک تیم غیرمنتظره پنالتی‌اش رو…</div>
<div class="tg-footer">👁️ 5.33K · <a href="https://t.me/SorkhTimes/134914" target="_blank">📅 11:17 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134913">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">❗️
❗️
تسنیم اعلام کرده گزینه‌های سرمربیگری پرسپولیس یحیی گل‌محمدی، مهدی تارتار و مجتبی حسینی هستن!
🔴
خجالت نکشید! حمید درخشان و بهروز رهبری فرد و پایان رأفت و حمید استیلی رو هم گزینه کنید!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.08K · <a href="https://t.me/SorkhTimes/134913" target="_blank">📅 11:12 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134912">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">❌
❌
حرف هوادار
✅
اقایون مدیر فکر آوردن امثال یحیی و تارتار و مجتبی حسینی رو به هیچ عنوان نکنید چون هوادار پرسپولیس اون ساختمون رو سرتون خراب میکنه حواستون باشه .
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.08K · <a href="https://t.me/SorkhTimes/134912" target="_blank">📅 11:09 · 13 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>

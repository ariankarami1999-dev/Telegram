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
<img src="https://cdn4.telesco.pe/file/beNBG5g_RvYjhQ_nOl04Ek-MPcNEKOgbLEuftYlh45LlLL2ZxTkhQx0xu9adW5vDBgkmWe5FhZD4GLLz9Hy-vyes4XhuP1N8Sg6O6YeUVxrUPYCHLZD0fnjFKGgjZ_IsQNlrmGI6beUWOpek-xkHFnKqWLndUhQWic8YWKL1QM6kXxCCoGLLt2Mc6JZl53UFOy0YDyUl77ZsVfpKpBPjaiWL4HAGWnIdZzQEbr-3u68yuDja-n0YDWjUzHS9qn4tunNvcHwwO8oOk-aL0KQv19l8NEO5wIqruWPft_xyM4NqwcNJtQTKF34dR7dI-Xk_uvY2jKm0ysy2K9Yvz73nOA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 [ Fun HipHop ]</h1>
<p>@funhiphop • 👥 185K عضو</p>
<a href="https://t.me/funhiphop" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 «قدیمی ترین اجتماع فانِ هیپ هاپی»🟡صاحب سبک🟡Tb :@FunHipHopAdsContact :@Chaman_Dar_KhakFollowing Copyright Laws©</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-11 21:52:34</div>
<hr>

<div class="tg-post" id="msg-79247">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WZsqpzgbASW-77Vn3Jq_X-51oJLQHW3b6uHiREOU_mvgpI4AJDDdah-ngb0t0QaZ09FhoIWVw2oO46Cb6ixzVrrXxKNNHFWEP30XDKFJCKzJuHik0blh1OtKHakI8FRTUShvrq4q73qsd07X6JzFBTxxOgCZc09UoAXSBE1vWhWcq0rz9Ps8SSs-h2cBqzj6ktP_xXii86omFDcJFBYMzTP0voVTaRZOLEH1a1lnFHV6G4d7ZzSQ0a3PqGxAmOkIt-E8Ig13IozCn0CRli0RTU23Tcy4gNij3JJJhsXtPzAu4HeZ-2KiiUMlYOI0bSTlT9iRwPDdqcBRjLiWYqtTrw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هلیوم جان قلب خیلی بزرگی داری
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 3.35K · <a href="https://t.me/funhiphop/79247" target="_blank">📅 21:14 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79246">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CR07VIJqnV12kbGh_9tHGhdgrtvXfw0TDnCoVZp_1e5Ev-HmzsvGMYakv6TpssltetLGjwQPxxwifrmktGBDY9n9y99HmgKy2sg8oAIGjUeQHUJARAh7ZYnBfkGrV4MCiOrbZxIunYkurziGRCT6cr1gT0BODKgtkWO_L-2Fnha4Xc6JPM8kVMJcmDaKg8rgfrMiU2G8fcyka0sal8KUR9JFML1Andg35H65JfxZJCXpYNDqWbN0v9q6Z56KYt4vRYGL_IiqsLcKEvEnQCPdf0LNQxu68W7Imhxs4YfGGaUs-1UocJUsdepGR4Ej5-7THXHC9mTYv03Z0oD5EAzNYg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🌐
با Legovpn وصل بمون، همیشه و همه‌جا
✅
سرعت بی‌نظیر برای استریم و گیم
✅
لوکیشن‌های متنوع از سراسر دنیا
✅
قیمت‌هایی که نمی‌تونی رد کنی
✅
پشتیبانی ۲۴ ساعته، ۷ روز هفته
✅
کشبک ۱۰٪ روی هر خرید
🤑
کافیگت رو بگیر، دنیا مال توئه
🌍
@vmoon_pn_bot
@vmoon_pn_bot
@vmoon_pn_bot
@vmoon_pn_bot
@vmoon_pn_bot</div>
<div class="tg-footer">👁️ 3.68K · <a href="https://t.me/funhiphop/79246" target="_blank">📅 21:02 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79245">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">لومر؛ خبرنگار نزدیک به ترامپ:
مراسم تشییع خامنه ای پر از هدف برای تروره. مراسمو بمباران کنید تموم شه.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 5.15K · <a href="https://t.me/funhiphop/79245" target="_blank">📅 20:38 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79244">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">آفریقاییا یجوری تو جام جهانی با دل و جون بازی میکنن انگار به برنده غذا میدن
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 7.83K · <a href="https://t.me/funhiphop/79244" target="_blank">📅 18:28 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79243">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">یه خبری اومده که خروج از کشور واس کسایی که پویش جان فدا ثبت نام کردن ممنوع شده.
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 8.86K · <a href="https://t.me/funhiphop/79243" target="_blank">📅 18:03 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79242">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YyYwjWjgIP7aLGGY4hE1INgXuHaiEFeAuMFa8vzw-DPsF8k1ymZdmCbODCfXBBdRlch5A5vef3r2f5Y5DBIO3cbBbT8nK1w48-AlGOdX8sYWlJhKC4nub8N34LuvR-XBIeA6kVnOqfDfuSunhWDURiaL3nbfH50Jx6n9bl-3naLkoKOuMz6XWHhrZswnRmvjZ04MymkXRidXkHs3-s5XhfNaSYnZ_qrtq-X6bDlttumk_RpCH5SCzZntsGCX8_-xuICMpXfAzZB0AUMp4o6J67YWkEQGp46c5Nv_P--XtVZlniM0ekFlXDMSDqOCDg50I8EBdBYdL7LJqJKBVcf59Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پیش بینی سه هوش مصنوعی واس مرحله حذفی جام جهانی.
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 9.24K · <a href="https://t.me/funhiphop/79242" target="_blank">📅 17:47 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79241">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KJouwAUIhdD8mLDGeGYTZoPWD8eTx7xekm2X0oroGRzE0k_e5BX_HHJPgaBdmfX9L58joG6tHIyhNSoi6ctmEbj88kkm40qRIKzHBgOeb6R8qaESyP3KVR6CEi8iwVt7gBl7eDHAVpm-TVqEo1HkHKdS32yHnL3Md2_yLc3IH-F0bNDPAQviRSmIYZEAklr7Kk9MrexA4J7TxsNWltxnviuhBXm8DGTbLEdXKh0MEdtzt26gUlDJ9WD56fbENUIbDcr3sbGgXOV5CFgCJd84kgNnFZbDLgdNPA1yaGKQk2xaCln1nlSXp8lyo5tRNJ8Xak7JPHXOz2hJcdt8No9UlA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تعداد کشته های اروپا به خاطر گرمای ۳۵-۴۵ درجه به ۲۱۲۹ نفر رسید.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 9.3K · <a href="https://t.me/funhiphop/79241" target="_blank">📅 17:35 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79240">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PP3JFINZt95y8HqiHIROFycuK7dYYihOlwKuX2tgUSJJSJmwtHoFbYwg7YyP08ChLr819KlZKBdc2gNaF_atfxf-Aeeh1MLwda4TPp5ZWB7iLuHdac2LgJPwGJnDGaQ3YR909Kw9ytgbwhNLeuTue563ZDJcXaa5oXwBT2AA44QC16Y2OFJdSqphi31UNW_suy7f07jT2k-Ed9_gA4z0rFqapUmSLQJ-rSk0xMkhX-BU_WSrxr45ElRx312Sbbl0UNKWNovBq5PEINXTUA8L7oQBs3eS3zz1BSaDiE5p0tYWYcarkn9sXKaeAekz7A2RQUkkH31Xp8AvKGZJoNM46A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تصویر منتخب بازی سنگال - بلژیک :
@Funhiphop
| Jenayi</div>
<div class="tg-footer">👁️ 9.21K · <a href="https://t.me/funhiphop/79240" target="_blank">📅 17:14 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79239">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oHe1b6y_xW6yUaXjxZcZFhd1EOu8weW7TD43NwJqYoCcsq5e-l8YaAlEHzcs5dRCNsuezyNLa8QdAVHvH4QF_QxHhW1QIJGUcEQ_uUqo2IX7JtNsS5ZDZGAuRBtCC911XiGdzPM3KNWczFV1GnnYrahBRVHWyJqL6NlWNMDsMHz4jji2uZNiLu_nr8Wb20rAFgA66vk3hJ1P_FXGLSSnsNnx5gzTpX8MIZAIerYsMgC1BM-UDnc9s0a_RRF0DJvYLxfjJRj8S0wh3P5U-4ZiSietMscGOTqaSrKY-GN0kcz6JN9uP1c5tnfLFv0xXe3eEaMciftjwfD18m523Awb6g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
پرتغال
🇵🇹
-
🇭🇷
کرواسی
🏆
یک‌شانزدهم‌نهایی جام جهانی ۲۰۲۶
🏆
🕔
بامداد جمعه ساعت ۰۲:۳۰
📍
ورزشگاه تورنتو
🎲
با بیش از ۸۵۰ نوع آپشن پیش‌بینی
⚡
با بالاترین ضرایب پیش‌بینی
✍️
اطلاعات و شرایط بازی:
- پرتغال با ۵ امتیاز، به عنوان تیم دوم به این مرحله صعود کرده‌ است.
- کرواسی نیز با ۶ امتیاز، به عنوان تیم دوم گروه خود، به این مرحله صعود کرده‌ است.
- برنده این دیدار باید در مرحله یک‌هشتم‌نهایی به مصاف برنده بازی اسپانیا و اتریش برود.
- با توجه به ستارگان و قدرت دو تیم، گزینه صعود پرتغال می‌تواند انتخاب مناسبی برای پیش‌بینی باشد.
🧠
اگر مجبور به پنهان‌کاری شدید، مسیر اشتباه است.
👍
ورود به سایت با فیلترشکن
کلیک کنید
BetForward.com
کلیک کنید
BetForward.com
🟢
دریافت سرورفیلترشکن اختصاصی
R11
🅰
💻
@BetForward</div>
<div class="tg-footer">👁️ 8.48K · <a href="https://t.me/funhiphop/79239" target="_blank">📅 17:14 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79238">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">مامان شام درست نکن نمیاییم خونه
ویناک شام خریده برامون
@Funhiphop
| Mmd</div>
<div class="tg-footer">👁️ 8.02K · <a href="https://t.me/funhiphop/79238" target="_blank">📅 17:03 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79237">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ja-uG0KjOFeDcmKAbxPStbPElbQF6Qa8v50lzRn5CoNGgkePkTsuFV8MesPgwB_J0ppuz3mP-wC6ABPXjhXnSkJ2tVK78D7J8K5_ns5EMRlImW-3SMGcjg6TQzoyybQGafgNQoRyO4bNUU2V_h2AduCbJDmhVs7ztDANhDPZ3-9USGfxv5UvqABDZubdjlOHoi_-gIaBN91lT85JMAs8YVzjcAcu-O5LfFVjsWOMUaz4Ob2oPk0vvQEFOLW-xjd7DyYWh9fC6rXfnHazZbPldOSbsa4kVUXWcJ-1pu8x4KfVl-75nsDF7W5Xct5L4a5edovmRm-5XehhHY3lKJMZdQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دیشب مراسم وداع با زن مجتبی خامنه ای بوده (دختر حداد عادل)
پ.ن: مجتبی تو مراسم زنش شرکت نکرد
@Funhiphop
| Farid</div>
<div class="tg-footer">👁️ 9.94K · <a href="https://t.me/funhiphop/79237" target="_blank">📅 16:24 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79236">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">میگن ویناک گدا گشنس بخاطر پول داره این کصونه واویلا بازیارو در میاره، خب اگه دکی نیست بیاره پول ملتو بده
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 9.83K · <a href="https://t.me/funhiphop/79236" target="_blank">📅 16:09 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79235">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">بذار جیبت بیبی از بلادیا پول زدم
@FunHipHop
| Mmd</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/funhiphop/79235" target="_blank">📅 15:43 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79234">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tmL9BWFVOiy-C64kVTEXa9OjdXfZjG-1CNWd84ifPaM8SnlLQe_wKXAcDITn8X3ClC8uxO93SEn-ouR4lh1Xt4z8t4bKIQhkNzP3IuItv8pJCGzn8bqpaN_DxyJDF_INY5RdOAKjqn6bg8iNAAuLpo3xi4lRy8DgHyM5gZPe1-iDeTzLOj_OwPoA5RRVt90ap-TxkKOcJ3I77vC3fbgfvMQovnaXTmm6rcktnq7A6u1ri8bC1Asuu-vJQMBIgVjsbbAMBwpCteY5Lc2yBJwc1sy3PxJx8-ZNhvp2KuvrxfJzG1ea_LM2QUS45RTZ3scld53nnBLeUzY7HyPoTbw_Ww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترک جدید ویناک به اسم
ویناک فلو
ریلیز شد
Youtube
Downloed
@FunHipHop
| Mmd</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/funhiphop/79234" target="_blank">📅 15:40 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79233">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">نفهمیدم پیشم بودن سارقا تو بلاد هوس</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/funhiphop/79233" target="_blank">📅 15:36 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79232">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">ویناک عجب چیزی داد</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/funhiphop/79232" target="_blank">📅 15:35 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79231">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">اگه فان هیپ هاپ نبود بازم تلگرام میومدید؟
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/funhiphop/79231" target="_blank">📅 15:32 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79230">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromAli</strong></div>
<div class="tg-text">رفسنجانی این بی جنبه بازی هارو در نیاورد
که خامنه‌ای رهبر کرد
بعد همون خامنه‌ای کشتش
این بخاطر چند میل پول داره خودشو جر میده</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/funhiphop/79230" target="_blank">📅 15:11 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79229">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">این کصکشا بهترین ترکای دو سه سال اخیرشون فیتاشون باهم بود، ریدن تو همچی
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/funhiphop/79229" target="_blank">📅 15:10 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79228">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromVinak</strong></div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/funhiphop/79228" target="_blank">📅 14:59 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79227">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">درکل کل رفاقتا رپفارس سر منفعته، همه اینایی که میبینید تو رو باهم رفیقن پشت سر هم تو پیوی اینو اون ناموسی میکشن به هم
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/funhiphop/79227" target="_blank">📅 14:30 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79226">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">چمن کونی پاشو ۷۵۰ هزار تومن بدهیتو بیار بده</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/funhiphop/79226" target="_blank">📅 14:12 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79225">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">Voice message</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/funhiphop/79225" target="_blank">📅 14:09 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79224">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">پول کاگانم نداده
😂
😂
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/funhiphop/79224" target="_blank">📅 14:06 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79223">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">Audio</div>
  <div class="tg-doc-extra"></div>
</div>
<a href="https://t.me/funhiphop/79223" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">دکی ۳۳۰‌ میلیون تومن پول ویناکو خورده.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/funhiphop/79223" target="_blank">📅 14:02 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79222">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">کونکش برداشته به باباشم زنگ زده
😂
😂
😂</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/funhiphop/79222" target="_blank">📅 14:01 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79221">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">🗣️
چاقال چاقالا چاقال چاقال
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/funhiphop/79221" target="_blank">📅 14:00 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79220">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">بابا
😂
😂
😂
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/funhiphop/79220" target="_blank">📅 13:55 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79217">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromVinak</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">Audio</div>
  <div class="tg-doc-extra"></div>
</div>
<a href="https://t.me/funhiphop/79217" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/funhiphop/79217" target="_blank">📅 13:53 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79216">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nX6fW4EHnZUH5JN9-rBWNq7ujz99MxjbgkGZ5h5lpgINRKkXGhRkYChh5Vv6L1_KSYc7iBmmujs4IoCgqyKGgANmxjcMJDZXe9VekTVlglCjelvLJ8PdwshCYtHy6wJrJC5KkqVkxDN9uMKKtwX3j3n44CylIAz8RbUz_LNG3qqR-uqP0BwBgZc3GeUhFQiy6Wput7EJOTzHJLZi1YEvyNsjU_O_kTSdrvu950Tpi23j_X10W1SKe577Zyw0d6kCEswcnSEnfQAIrTTRI1ps_3Ypn5zoF4hEqKAiV9hSe795Wpp8VDIP7nTtMch5d_XDLpROoI2rIN5CYDRTpvR8aA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دیروز تا قبل تعویض شدن مادوئکه کل موقعیت های انگلیس رو مادوئکه ساخته بود
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/funhiphop/79216" target="_blank">📅 13:21 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79215">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">تاج: پیگیر هستیم به پاس افتخار آفرینی بازیکنان تیم ملی کشورمون به هر کدومشون به عنوان پاداش خودروی لوکس یا خونه بدیم.
- جوابش با شما.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/funhiphop/79215" target="_blank">📅 13:15 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79214">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">بهترین تصمیم زندگیم ندیدن سریال و فیلم هاییه که ترند میشن
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/funhiphop/79214" target="_blank">📅 13:09 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79213">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/onRnlqIn_u5R8IcqnPZJfA9P3mJBx81LQIYRzdhNWOIj61GUyUlBw2gmpm2_NCxII1nOYjxCa09ct1-c7-oLOEm5lPBwojoSVEdzKZZ30olJUHCwMBKVyD-3XhNKwK1kSTEqKnYipq5pFvoB52FXJOemv86MtCSeXORqz2L5ygX3uIEQff_AEV3vpUicS6cbplAT0wYhuvBqClpGQLzxmAZKANJlXZJiKGClw3ygxoJlUG-DQBzDPZa4gPyyYcOn2FmbVnvlpIMvGu7SEt-Bcvrw6KHHjBtjR9rJQ3OuvuSp9XGWIKQ3MsoihjNQ0y5KpL8dWk-7FsfZ1DpsXIpSgQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پنجشنبه ها با محمود.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/funhiphop/79213" target="_blank">📅 13:00 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79212">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/r_mnWNeOltl_IzDWLPPt108xhd1qxeSmP6MZGzaptG7Gqyluwsz_hQPoE_1T-S4IpQ9lyonT5DCBClc0usO0GifqyTxnrWD3t9NBF2Sm2H99UQ2ZGY4ZF1fLbkyh-OEhR-BcZl3AHvmEZcS2g4wO2HtoHxA0l9PeIWtdvwQl8WuzjgdLH-pRjw8t9tpU3tbzMUwFB69hdZrdb2a0WBFpC4M5O_T6-dee3qTMNR3yECpQhA6aK0fdLgNhU7TYYA5mIhyKF14wYkzJ9CMKTRjD6L3UEjmW1RG5xFovHjRfYHPaxpb9Z2fgzqMOXPtqRD71XJir3BGXnnyt-U1-Eym1Dg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
پرتغال
🇵🇹
-
🇭🇷
کرواسی
🏆
یک‌شانزدهم‌نهایی جام جهانی ۲۰۲۶
🏆
🕔
بامداد جمعه ساعت ۰۲:۳۰
📍
ورزشگاه تورنتو
🎲
با بیش از ۸۵۰ نوع آپشن پیش‌بینی
⚡
با بالاترین ضرایب پیش‌بینی
✍️
اطلاعات و شرایط بازی:
- پرتغال با ۵ امتیاز، به عنوان تیم دوم به این مرحله صعود کرده‌ است.
- کرواسی نیز با ۶ امتیاز، به عنوان تیم دوم گروه خود، به این مرحله صعود کرده‌ است.
- برنده این دیدار باید در مرحله یک‌هشتم‌نهایی به مصاف برنده بازی اسپانیا و اتریش برود.
- با توجه به ستارگان و قدرت دو تیم، گزینه صعود پرتغال می‌تواند انتخاب مناسبی برای پیش‌بینی باشد.
🧠
اگر مجبور به پنهان‌کاری شدید، مسیر اشتباه است.
👍
ورود به سایت با فیلترشکن
کلیک کنید
BetForward.com
کلیک کنید
BetForward.com
🟢
دریافت سرورفیلترشکن اختصاصی
R11
🅰
💻
@BetForward</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/funhiphop/79212" target="_blank">📅 13:00 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79211">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PiilKVF6Z9mzrlsuI_tbBBn9D4dLEixSzrN0CpsQ3_OGUOAZ-BJUDYuGlxqjuo5b5JvsCuc4mQnwIJR83H0TPYp_R79D_btGIoIgqZDCW9VNr91hCVERtCWVInLWhlgo8rikBl2EY6VUu2_XwQf6zRKOqrx1wWKy4GmV3Zf9EnVfb8PL29dV27YpPsHTfhrBbn90v8aC3xQfEbGOYhhf74wwwGj65VWBCOYW5K7x3S7F29dWfDP4E1XIRX39HrYEiQM8rD6PdkN0WsfTE5ToyYunxQUMJ135GRHaRZliWb7RBkhnavKo5MQ-_Z1w9G-9M4RJixAwicifptjBj9lfdg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تاج: پیگیر هستیم تا به افتخار آفرینان تیم ملی خودرو یا ویلا به عنوان پاداش داده بشه.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/funhiphop/79211" target="_blank">📅 11:16 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79205">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">تتلو زندانه یا استودیو
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/funhiphop/79205" target="_blank">📅 02:31 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79204">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/E1QLbbPjFw3axaxaWlG2Z49hRFyEZ88xQj7bKDJNm0h6Wc6nMKfcwDZxRXmklI3SjIw1nuQOIrLkVV9Ccxpl0TJuZ5jymuTEqC_c_tzxBpnrwmTh2i1Oe-EEY6srJT5HwOon0ORzbYBm9SmJCf-ZWDgqKrbs5Y6RHA9Rx1oZgn8_-bwsMux0y6AaQ7UsHM_u-IGN3J8vQhuU1kd-d-HQ5YTucD-B57TANVTrHk35kodamDamN7c3iCSjS8DzJnaWOChUKh1bkKYX0hYdWt0Y_FmcRzukqCEqgTkluSpCOfXuTt5m1Y9lEokRhY1yN2B3UoZlmZRHN7SO8hb9fj9FRg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترک جدید تتلو  به نام تریلی ریلیز شد.
🔥
Youtube
🧃
Download
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/funhiphop/79204" target="_blank">📅 02:18 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79203">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">سنگال عجب تیم کثیفیه</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/funhiphop/79203" target="_blank">📅 02:11 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79202">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TEqGjFdNibDsZQ7Vr4SSmQvdrQlRQClGGfcdVBkiA_5v4Ln9ZgFRqtwOuZFdnaEWneX-tLOloBWuYhGy9iv95wvA4FXTgr4k6rU7m26-HVFVe5pG1ePoqDZIxpDIWG0VTkFtNDceXHmTW30bMFVdIc10kNgDlPJ6BAfkxmoBdQCNOVVSIqj61NWq4mQE-I5UYFaSOyhpIEzWjT7-RQiWLf69wlBMUFdAcJl-f-B9CQznkk_0MQ2cD811TeZwAWvxEzQt-_izdmw-E2A6fo6wrnnjCv6AQhueKx2v6XfKvf6WT2_sDI3T3UgSNdebD9hn1-uUBTQTeieW0Et9pbB2aw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اخرین فرمانده باقی مونده حماس
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/funhiphop/79202" target="_blank">📅 01:36 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79201">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">یاد ژاپن بلژیک ۲۰۱۸ افتادم</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/funhiphop/79201" target="_blank">📅 01:24 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79200">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">پشمام</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/funhiphop/79200" target="_blank">📅 01:21 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79198">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/gvv0OypzNlNrLWOEBexVWN4pYVGAWbn07tGsyjNe7eprgOoOItxYvWjwq1cNXukN-_qWMv0yI5HU7LA7K8g5UYpF2J64sPKDAUcGtAYlYm35HOHGkNdhvCqoW-pFy75HgXlF2ocSQ5V5GewJ-0CJPwR5liaeOp4L44DyBo0p9aVf1BhmWkZDoN1c2SDmLWB3q_RBnhrU1Fi68XzO8GR1hRt_DUK7E_enDPrp7CQ9xopBFaDGnbE-7AC5ytXX2Z4qGLV30KYn6dR0PZhxHAjXU-fiuBrzRLfC8HnJAkaFhGKcQYOuzGWCXYjLeNsbw8_1qmbKLsWl0apDZDp1DccSTg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/RiI5mXL16W5LCO1a1u7veLsDCHdcTNMly0skLNBiPuwJH8H243UcIq6hJ7QFqp575VL62uxMrFSNDkueNDdgxHDSdP1utsO-xtao5Aystn5M00oGi8Z04LqYQNxjxslzaMBlk90LXI0QMn-46BivuV-8qbVb-auo2WYBV7ZNCHohKiaylFqhmn9tei8rHxljKh4M-nuXHNejlMB7P1XgCJLL0bekfZImEZwPt1piH2UuI3eMdkyOJxC4a74iB-TmzSSDlJWReU-g9r3hLTeozppBCfPq-RAB7AOLjoVer_zY7XCbNk1JG956MPB2c1zBrlC5M-EX0A3Zh5OqTnQUpA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">احمد الشرع می‌خواد برا سوریه یه مجلس گذار موقت تشکیل بده که چند نفر از اعضاش رو هم خودش مستقیما مشخص می‌کنه.
بعد لیست اعضایی که برا این مجلس مشخص کرده رو پخش کرده و این بانو هم توش بوده که خیلی سر و صدا کرده چون بانو تخصص خاصی نداره و صرفا بازیگره.
انگار احمد الشرع با خودش گفته ببین می‌دونم یکم ضایع‌ست ولی مگه کی قراره جلومو بگیره؟
@Funhiphop
| Nima</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/funhiphop/79198" target="_blank">📅 00:56 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79197">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZDf3SgOfPWy2CW-Y0QvqePM6T-ubq1T8revaeqMLoorrc8lXNk_eO_kqTgXIMW0cJQvPUrnQKbWw7ne9AWIHpp1sT4CO4MkQ8JChkrtYKM1OHvb86EyJETRSsIRLDdVMyEvHSj4ROP18T97MeRKF-yRc9ZLMpqEk-ZA5aE8QExyXm-OAStBVZuNrq2dMh3v9KLiZXTnMLvPtMU5Ofp7hYMkujb2u1tBNTzYkgnwlxnW5kbUC4VTJqmdS_cXtypEPqT3uTBGaa3GL4EDQ-pnFPFP6XgLGPaWqfGodwd25Bz_kcweYEFxGd3F9Ln2wVtbU9b8yotbZhLUYLtr2t_B5Zw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اخجون میم جدید
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/funhiphop/79197" target="_blank">📅 00:34 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79196">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LPYTwJaIoOUOgkmcal_6PrIeMHuxMFb9Qi4n58DlO-hMrtCvfkK0DH62pKshIimHHgBxoxOgYxnk381YhwsLSogWkLd1E32FdPbJB-MBfwoGMP0uG7xe6wzcQm1o11YieuuvMhNfCCA8PnPBVKojsNDMtLwiNgesl7kdAMu0_BTBHaU_dgpj3Z7-hu3WTcYeIS8C136AcuTSZHJfkAu53Vfc6XjqYdRw_8TCAWYC53LNpQ562Dbp5akRomUTxNmqEBN0lU4CyzyTVAQ0sIweOQ9a9vUJCYv3PXQziB2HnY_JcbqJw7UTDN28G8b0MXmoQE9jp-XlVMZR1pp0QqdEpQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چقد گی زیاده تو سنگال  @FuunHipHop | FaRib</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/funhiphop/79196" target="_blank">📅 23:48 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79195">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">چقد گی زیاده تو سنگال
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/funhiphop/79195" target="_blank">📅 23:45 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79194">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">حسم میگه سنگال صعود میکنه
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/funhiphop/79194" target="_blank">📅 23:35 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79193">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">قهرمان جام جهانی بنظرتون؟  @FunHipHop | Arash</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/funhiphop/79193" target="_blank">📅 23:31 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79191">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">قهرمان جام جهانی بنظرتون؟
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/funhiphop/79191" target="_blank">📅 23:22 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79190">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ULIoTN8cbjAwekkqUP4Kix0kejl5w2iMHbibn7laU8D_tknuIuq1JOhWVGbhEJDzIddsSuIXCnlJKabUTU5s_NEAGL8u2UXsSS-oGPrxOYZbmdOdd9hlJl3F_IQSmpuxEfMQyVCVKNSI5FaXEMprL-ikYqhrhuuFPs8hfhk6mhb-oiA2e-kIU_jjRDf5pdfjE02geXRjjuNI84i5NQ_hbx28-LlfAe_0Bt3EM0nJKYLZjXFlwKQ4PCKYs6yQ257PYZGOsML8V3B1swQlxXcjlthxWPnQ9pjwIa_xit2luO9QOBGM1Z6LPn9N_DqjWNIKDJnvWccaZcVrK1J-QB2aiQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترک جدید حسین تی ام  به نام “اقاقیا” منتشر شد:
🔴
Youtube
🧃
Download
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/funhiphop/79190" target="_blank">📅 20:28 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79181">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">خدایا با حذف انگلیس یک بار دیگه فوتبال رو نجات بده
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/funhiphop/79181" target="_blank">📅 20:08 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79180">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">Parvaz</div>
  <div class="tg-doc-extra">Arian</div>
</div>
<a href="https://t.me/funhiphop/79180" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">@ariansongs</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/funhiphop/79180" target="_blank">📅 20:01 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79178">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">بنام خدا گل برای کنگو</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/funhiphop/79178" target="_blank">📅 19:37 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79177">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hVPn1k5LXuiBeBXrObI2B7aj-rCvelwyGjC9ofqjdTzVeZ34DflG64Q1Fauj70jSEL03VhFmwmt0Bzm5uehUajfkfgVBHsHl4nAUX38aA7H3Srieh-dzPI-LmzXPppe3ZvVNlV-3bahDD5idrBE1zO99KEfb6WkUyc_WmhIz5dMyraoCV8VOJn5hrbnh3PwU-QKPqREOJsa975HowCB9_F_R_UthVF4MiQ9NEyBn6b5kuWXYksok6F_npp3V-iFYJumA9usdTk7r1MdKFuT_oUCywuQ5SNLhFLdCx_KtUCM3quw-_PJZhMWPlJS2JQ3uta_o46PcAFDHrdGFTwDBeQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یامال: اگر قهرمان جام جهانی شوم تتو نمی‌زنم چون‌ تتو در اسلام حرام است و من مسلمانم، الحمدلله.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/funhiphop/79177" target="_blank">📅 18:41 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79176">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1b3f4634aa.mp4?token=gwPrOUFo0b62mdFNX6TzezSRMH9fXm9LYg9vboWGgzMoeN2lRUHMYUBQE39DT8gRK3lGc3ejvfh47EYjWl4byE7796mV6QJhC6Tm8NDNOREwMRxWUVBT8JsHPA3JKIByjnGWzr6W2YvRKBBgFDOUnIBR_pDpw2JWKLKhNMc7sTpOaHceorN-Y2Uk-pisEbh-ZdykZfLN0CyvIfVsOv3iPJShDF-fVqR_nnnhPjs1qDj5S1JS1HNJ5B9m13voOmjYXLMZFnQqMfgE0ZX-Ixx-GwgSCb64Ug7nzl1fsF9vqAnkAmfxiVRP02rYZFtC_XSssZg6P51m21Jrk7JP3y-QOA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1b3f4634aa.mp4?token=gwPrOUFo0b62mdFNX6TzezSRMH9fXm9LYg9vboWGgzMoeN2lRUHMYUBQE39DT8gRK3lGc3ejvfh47EYjWl4byE7796mV6QJhC6Tm8NDNOREwMRxWUVBT8JsHPA3JKIByjnGWzr6W2YvRKBBgFDOUnIBR_pDpw2JWKLKhNMc7sTpOaHceorN-Y2Uk-pisEbh-ZdykZfLN0CyvIfVsOv3iPJShDF-fVqR_nnnhPjs1qDj5S1JS1HNJ5B9m13voOmjYXLMZFnQqMfgE0ZX-Ixx-GwgSCb64Ug7nzl1fsF9vqAnkAmfxiVRP02rYZFtC_XSssZg6P51m21Jrk7JP3y-QOA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پارههههههههههه شدمممممممم
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/funhiphop/79176" target="_blank">📅 18:23 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79175">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">ویناک فردا ترک میده
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/funhiphop/79175" target="_blank">📅 18:12 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79173">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/HehbLQFgNhcqX5MrYCesu0ESxT_VXCvuDBPJxWZ4ZEdeWjCORtN0145A278nn5GtRUvaLN9qEi9iiwQcgkR3ZI-FKvawUYaPT2ZDX5bmO8GqneXFj1JFj4H2nOyXgZrKjJTY_75Tuc4FwqzjZd8fin74EKCG42uMaNA1_-PjuWuI_OE54p_Wh00oDisSgXnhSs0teHZBse0PGZh7z3kXGuyq-I33BbWMaL5hu92ftcxS6mdiEBNZ9BSOvV74E5M9HJ_PXyNCmrISLNnj4Xyds1PnyRsJwJIAvEjB7lEl2p0InIrMq3RkC4Twl-24ucaWRHD7zK9uYeC7fBlgSLL3Jg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/FVg1geVbgXgC-Qv_6wkd4H5Z9r5LliKFRLeP_DqfQtK7Gi3239X-yVJ_NKyzEuRcGgw-bWWeZjEfN1f8_B2nQXCNI0LN1LiJ-il5McbaNP4o6bXo29ba-rjdm9aluvT3HU1vNT46W9vfaZRaB6hUzB8DFHIoDqxWmmNicnEiSb4CViHskVPrj8tfwghlsIDdVHJz3OeXfbw4Qck8kXuOUMJxkJLp4Cw2L3x2fdnb-ZQ82XJYslfqMpyVYhnLF5Ue2qwGFwZ6XoP1XY-NWNT9vZt8vNGz5cvUKF8M4wByGqb5kz8sNfyf8k0RMVj9xnOFD8ZZDQ95xvQtUfmc9Sd2Dg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">خلاصه حواستون باشه عمو رو بازی ندید.
@Funhiphop
| Jenayi</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/funhiphop/79173" target="_blank">📅 17:47 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79172">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZhZ0Nj499a0GrFFtlBiXwF6biP84A7Ku-bkyAMX4xTOvdIKgkVpxsj_HhbJE2Sww4LGOmkZ0KRdeQd45aS-8pZFnGW8ixn89dxv8c2eD7vSM31Vgd8F3X7a6PLXlUH928xh8qNSJ2PP6LFbOwMNVyc8OHB6cLHtVjcrT2_hvEos3jzAbeEtqhqn7rvab5tdBkDvc16hcan_VnIvRxU_2yN554OJtNFJKUCe-jdSPjDtONGtzVf6PTz7qrdZS3DFO7LTO5xkVT2GIZ33wODS2RH0E1Zzem6W3t-GYZhMsetg-HgLk6hYlYXDZEW-llz8DUTTVZvur2gx0FJr4Yq4kSg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
بلژیک
🇧🇪
-
🇸🇳
سنگال
🏆
یک‌شانزدهم‌نهایی جام جهانی ۲۰۲۶
🏆
🕔
چهارشنبه ساعت ۲۳:۳۰
📍
ورزشگاه سیاتل (لومن فیلد)
🎲
با بیش از ۸۵۰ نوع آپشن پیش‌بینی
⚡
ضرایب شگفت‌انگیز
✍️
اطلاعات و شرایط بازی:
- بلژیک با ۵ امتیاز، به عنوان صدرنشین از گروه خود صعود کرده‌ است.
- سنگال با ۳ امتیاز، به عنوان تیم سوم به این مرحله صعود کرده‌ است.
- برنده این دیدار باید در مرحله یک‌هشتم‌نهایی به مصاف برنده بازی آمریکا و بوسنی برود.
- با توجه به عملکرد دو تیم در این تورنمنت، باید شاهد یک بازی نزدیک و غیرقابل پیش‌بینی باشیم.
🧠
پیش‌بینی آگاهانه، تمرینی برای نظم ذهن است.
👍
ورود به سایت با فیلترشکن
کلیک کنید
BetForward.com
کلیک کنید
BetForward.com
🟢
دریافت سرورفیلترشکن اختصاصی
🅰
r10
💻
@BetForward</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/funhiphop/79172" target="_blank">📅 17:47 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79170">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/gSi5zao6-8rFjhf1v4PVwGYgGd8gSvDK3RHkAPzh0lmLEwjzTS4w0Df3DKLBdFpc3cIsVvSNjCnWWHxrQfu-mn9PAMNlhCYj6T_4ErysqfgmLhAmumes2UFjw6crJasjfv-TdLhO8Xwed-5Qq6LUkfjAhuWW3J3pbv_uNv_r_5kBW84KMP9QHKvs6jCZndZzjiOxmdOEcbifIOUMas2vaczo1XhS9X2QUFgqj49fp3KGT9mrNxAIlm4j4lphpTDkar_p4kfZfD-yzIgeB8ijoj0-gdK_wudjtxyDLZLteUSAWYS41Lr4sfErnsDp5UOT2ihge9I6hONWbCfQ48jfmQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/f0fK-Q69X8AOJQrZQgd4o1O5hrTfeHDucbYu-v_gQtc6NtsIje-WpRyd1v8Y20XcKWeaNbZwVjy6FhtLn-u_ro2mzKTuxoL6S1rjkiH8sJuGBfsK3fzYF9c-ibfbeA0NByFOQq2ItHX_dUuYpXMPl0BmCAvFmUN6twzZkU89N7XO_f7_8AkU8tpSY0x7Q8ov-cMPVdDTKIK1t7enb-SSYDwvVV3noDBI-nRoteVW6MQwRVVC5NGCP5AZ0yXa2SQ94MrAQgihspt-_L78A_dvkgOnxuAt3o-6HbX98TaFPjmiRgWBI13owV0JrYrIoq7-lZSbufQwEBUZD7wSumHHxw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">امان از این پرتقال فروشا
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/funhiphop/79170" target="_blank">📅 17:00 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79169">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kvM1eXzCxEH8SDAinWt2kEW7b7_rhgVBXbh_QCInxVL4jIRf2FeRN_hKWsvVzauI7KITVq59CpLMlr1LlybK7vuX2kE_AgSrxqoM9pud52LyYub0_Q3SIg1Sm94oabFUmGv650wNLxSihEyueds3fJ3gjLLDErEJWpwjhsQSgndFfRfiU5PSDZyg7f2UWtqhFZ6syuJwS421rlLYyu_b0Eom1MFV1axW8HXmBmE9T0g53y0Po_0jn4d59AsQOKZ7-7-GIONLrBvrLWAOSQB2-kI_IKNYWURyb40Yp1gj2YjcwPF22I6Z58tkuq2ObjhaB9Ov6x3Jl8Fgkd2DFjDswg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سعید آساره فعال مدنی اهل شهرستان ملکشاهی امروز سه شنبه ۹تیرماه ۱۴۰۵ توسط  وزارت اطلاعات بازداشت شد. تاکنون از وضعیت و محل نگهداری این فعال فرهنگی -مدنی  اهل ملکشاهی اطلاعی در دست نیست.
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/funhiphop/79169" target="_blank">📅 16:15 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79166">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b10d6b449f.mp4?token=swPbnK7Mekxa2rRAbJR3wOMEbcJK88UIUu15L8oj18BGVTC3tgfFmo453uqWhQxll_8YHlYlIQ0NKND7mp5kcnQ9DqDedctm-6vqwMn3fhes_RX_l9SLnx4zjUfP5-dcTmM3jRDAZPX_p3nc0RqiQKfYGxKJekCViXXXemJ91f2hauw8fI1Dq2tJJQNo1mgLNun6UGaBEhHh1REoiFv9BpWe-cgo2Cza9tYPtc0W0_eas_zxh4lF2Edywvi-gD9OfVbQX4VRsjpo4dlJq6lpvuCw5pILNlmOvRFtMaQZ_UoC5kplD9X0g-NCd31jNyuSkuf2netipc6kHMGxxEHshA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b10d6b449f.mp4?token=swPbnK7Mekxa2rRAbJR3wOMEbcJK88UIUu15L8oj18BGVTC3tgfFmo453uqWhQxll_8YHlYlIQ0NKND7mp5kcnQ9DqDedctm-6vqwMn3fhes_RX_l9SLnx4zjUfP5-dcTmM3jRDAZPX_p3nc0RqiQKfYGxKJekCViXXXemJ91f2hauw8fI1Dq2tJJQNo1mgLNun6UGaBEhHh1REoiFv9BpWe-cgo2Cza9tYPtc0W0_eas_zxh4lF2Edywvi-gD9OfVbQX4VRsjpo4dlJq6lpvuCw5pILNlmOvRFtMaQZ_UoC5kplD9X0g-NCd31jNyuSkuf2netipc6kHMGxxEHshA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بی صبرانه منتظر ترول کردنت هستم
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/funhiphop/79166" target="_blank">📅 16:00 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79165">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vHFWHO_c6ognm3dTYDUGA72Z8c0aCtZfpHZkzOghao_Wxmtvta6BdG6biQBUg9FzRtBMIJJQ9MBchYcODrXOJLaAuPX9cwY4QMRsONjRf9jp0ExiGW26OPnwDhEt22KqaFLKA85_WKAZrLfE0jjcScd4NJ4KWBUQjL67M7808u3QXiURxTcbmeh07MpemqaSOtMT1PV5ac7V00oZidK1C0HA06mvShGVnv-MzWLVSk6fH9ElqOKqz61y2IVuCIrJz1fnNQORFielFk-JiZ6wqdKL28HXWrvSBY13ZEVl67oMyLCeb7lzt2lOQqT4F98izkThQieMQfHjDq8LOwDAuA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/funhiphop/79165" target="_blank">📅 15:45 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79164">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">وضعیت جوریه یامال مراکشو بعنوان تیم ملی انتخاب میکرد شانس بیشتری برا قهرمانی داشت تا الان که اسپانیا رو انتخاب کرده
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/funhiphop/79164" target="_blank">📅 15:37 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79163">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">بازی رفت بارسا و رعال تو لالیگا افتاده ۳ آبان تو نیوکمپ.
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/funhiphop/79163" target="_blank">📅 14:26 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79162">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">کانال ۱۲ اسرائیل: ترامپ درحال بررسی بازگشت به جنگ تمام عیار با ایرانه
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/funhiphop/79162" target="_blank">📅 13:20 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79161">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">تو زندگیم اشتباه زیاد داشتم،
(یکیش ادمینی همین چنله)
ولی هیچوقت عشق ابدی ندیدم.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/funhiphop/79161" target="_blank">📅 12:46 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79160">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6094ff0128.mp4?token=QYeIecgFDKmU93eqvNYXq1hwxLUBLcJ3Ix0O7y0xC2EfihiS1urbKjoFIRKsckJWhvcx94IbXbpmTnoA-voEd30dJib15CWgVhQYouumh_KW-7wfSAttigKoUprD4JALgw-zAGABTu9w4EH1LnKV2cp2EXZBb7cHN60gWP1HwOD1RWC1dBKPg2p9-W-3T2mmEjE5l35N1uV0QzvUK3F-mafRL9EXjm3euDShv6YsUxbX0xLQnYFWQ3K7Qv8N2XJtouTsI3PTXE4sahHOCBtgPHu00FAN-4Nafr6iuORN0rz3U-yjfiyxDsSnJjRoAvFd3aYc9SdYkuZHIba3RHdN5g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6094ff0128.mp4?token=QYeIecgFDKmU93eqvNYXq1hwxLUBLcJ3Ix0O7y0xC2EfihiS1urbKjoFIRKsckJWhvcx94IbXbpmTnoA-voEd30dJib15CWgVhQYouumh_KW-7wfSAttigKoUprD4JALgw-zAGABTu9w4EH1LnKV2cp2EXZBb7cHN60gWP1HwOD1RWC1dBKPg2p9-W-3T2mmEjE5l35N1uV0QzvUK3F-mafRL9EXjm3euDShv6YsUxbX0xLQnYFWQ3K7Qv8N2XJtouTsI3PTXE4sahHOCBtgPHu00FAN-4Nafr6iuORN0rz3U-yjfiyxDsSnJjRoAvFd3aYc9SdYkuZHIba3RHdN5g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">فرم معکوس با فان هیپ هاپ
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/funhiphop/79160" target="_blank">📅 11:29 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79159">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/E7R_NLexBOgSSutGhdaP2Te0LiekXGC2rRKbOBXpUJ57kb5nr2sU6MzaEghxVfPtEmytBE-xAo3cgH2cbH_NTzQ613Kaqnx056SzgVpAo_yFQBSVIZLkpeGb9iebgPU-HrGZAwnrMWy6zTG7mtunXgqHP2SzQlGU4fTiQF1_9oVGerCASuzlzyRVEDnwQ19CrW9iGDj1g-F-llKAeWPMb2cqapbL8ww4Jl2yh9HQHBZhUU4q9v2XduXpjTPX373unPhtRxmfacp03Re1EsgnZAiLBrua2Cr_Yba1b0P9yEfilu332DItHmqqOPcIzE640Vpqc5-eseV8RWpbG-CVrA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وضعیت صندلی قدرت تو ایران
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/funhiphop/79159" target="_blank">📅 11:22 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79158">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/A3r9RbAwoLa4IFXmX-wV57oGL7aKQP8WVtFO8RL6xK6jp47uJn7xBkpC5r_6qbZEgDGm7gDN-C3ynEYGL7vDJBFQmklQDUCSKBGCjZu9K0jqP8-RJSDtYYN7G3_gV2nIEf5qXCgbFfQYJuSYxPuRLTwX8x2sCSyIvF4kbrBUlhIORcfo5kbyh_vaIy3eYtgDEp5y_Kdx813QHy055BuzWJMmo2HF0qP1Smp6Zx1rWf3HAW9FBc1B2__1_ZlvIUg07vTo0DUB-s_ASSB76ZJn8LFQ7z_jag0brLQsORtsSHZdMtzHO2dCZ4eumNNHSQ7OPSaNDnEs9D5RUMs7Gxswdw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
بلژیک
🇧🇪
-
🇸🇳
سنگال
🏆
یک‌شانزدهم‌نهایی جام جهانی ۲۰۲۶
🏆
🕔
چهارشنبه ساعت ۲۳:۳۰
📍
ورزشگاه سیاتل (لومن فیلد)
🎲
با بیش از ۸۵۰ نوع آپشن پیش‌بینی
⚡
ضرایب شگفت‌انگیز
✍️
اطلاعات و شرایط بازی:
- بلژیک با ۵ امتیاز، به عنوان صدرنشین از گروه خود صعود کرده‌ است.
- سنگال با ۳ امتیاز، به عنوان تیم سوم به این مرحله صعود کرده‌ است.
- برنده این دیدار باید در مرحله یک‌هشتم‌نهایی به مصاف برنده بازی آمریکا و بوسنی برود.
- با توجه به عملکرد دو تیم در این تورنمنت، باید شاهد یک بازی نزدیک و غیرقابل پیش‌بینی باشیم.
🧠
پیش‌بینی آگاهانه، تمرینی برای نظم ذهن است.
👍
ورود به سایت با فیلترشکن
کلیک کنید
BetForward.com
کلیک کنید
BetForward.com
🟢
دریافت سرورفیلترشکن اختصاصی
🅰
r10
💻
@BetForward</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/funhiphop/79158" target="_blank">📅 11:22 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79157">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">۰۲۱کید تورو خدا یه کصشر جدید بخون هرجا تو اینستا میبینمت داری میگی "فیفا ترانا بن مای فلگ" خسته شدم گاییدی
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/funhiphop/79157" target="_blank">📅 10:51 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79156">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/39eac96d35.mp4?token=osjcRkWVTcPmbpZjviVyxHHhjQo66NZe1mSX1pAn_Zw9gacpiTeeJ-q_dnoT3KlpC-7_8MpcKFfkE43DVLO4ipcgbgIHTK-DASDWGwvT-hPoNSJID2JAl43n9T5x3lSU5rC7Cnld-L_WxoOdfsETi5tcvT8IzSUDIYgcBLkuEKhnw3i5nmdemSNTlovcd9DM_XASTAPLUWVRwhCCT0knNg0fO4OaaO5DfCvP8BoeBUsQcj8vGZ_gd8XULndyX984zdJylLTQYRV1APClymNhToLYrDgjjCwxA9l8KnRHXHOVIQfGw8ipBucEmy-PBI3ustduCtKoxnGX9qSbLu8Mr3Nuj2sOWOP0nG5d7KgwxnjG3coEwP-THJAfAkDn3H7YxjFx6HtSRLwl_odYviN_CKSOrXBygNTxvOawJIeNY-g69E9-CRioREjPBMl2lgZUToH1vkyvGHr6OCQMMB62Wf4aAkeHh2qZWkXLIt8S_JnH1Bs9F-hUwtdshqGQ1rTrKPoJqPqttgUvbyfgmtAeoFrQkoYoO3z0TOeFjWmaRyNhbYQSdN_LLXadWJiJbO3M6ExASAZtmdLoXrQKYJpR_fGfFdqYJiLb8xV0oOIi2g9mVCsuwgeAW7cQWGcRXB2kxdA0G6f7euv2p8yfkW2ElVf-ODvVIFpw3uZa0jHyGck" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/39eac96d35.mp4?token=osjcRkWVTcPmbpZjviVyxHHhjQo66NZe1mSX1pAn_Zw9gacpiTeeJ-q_dnoT3KlpC-7_8MpcKFfkE43DVLO4ipcgbgIHTK-DASDWGwvT-hPoNSJID2JAl43n9T5x3lSU5rC7Cnld-L_WxoOdfsETi5tcvT8IzSUDIYgcBLkuEKhnw3i5nmdemSNTlovcd9DM_XASTAPLUWVRwhCCT0knNg0fO4OaaO5DfCvP8BoeBUsQcj8vGZ_gd8XULndyX984zdJylLTQYRV1APClymNhToLYrDgjjCwxA9l8KnRHXHOVIQfGw8ipBucEmy-PBI3ustduCtKoxnGX9qSbLu8Mr3Nuj2sOWOP0nG5d7KgwxnjG3coEwP-THJAfAkDn3H7YxjFx6HtSRLwl_odYviN_CKSOrXBygNTxvOawJIeNY-g69E9-CRioREjPBMl2lgZUToH1vkyvGHr6OCQMMB62Wf4aAkeHh2qZWkXLIt8S_JnH1Bs9F-hUwtdshqGQ1rTrKPoJqPqttgUvbyfgmtAeoFrQkoYoO3z0TOeFjWmaRyNhbYQSdN_LLXadWJiJbO3M6ExASAZtmdLoXrQKYJpR_fGfFdqYJiLb8xV0oOIi2g9mVCsuwgeAW7cQWGcRXB2kxdA0G6f7euv2p8yfkW2ElVf-ODvVIFpw3uZa0jHyGck" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">فری استایل جدید یانگ کید
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/funhiphop/79156" target="_blank">📅 08:46 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79155">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">بی جنبه ترین پلیر های تاریخ ایرانیایی هستن که میرن چیت میخرن تا با چیت لول آپ کنن خودشونو.
@FunHipHop
| Reza</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/funhiphop/79155" target="_blank">📅 04:29 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79154">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dDMzrCZibv0UOmvzzel23UTi4T3SyR1OUAF5Zu67ircYbCVyb1qY2sMTKCAFn1-m-7LW6Fo6Q0gPyFEbSXJYRH7AaKMRvV9_iPVbPSPn2x1yNGTImoSYOqQVcQr8h3jmGd_a3F-FMsB1QeS2c-LCWdeU-sPDYCdySFQ9iEhG4ChV8j0Yg_wAmsUgSoluV8IBfXBxVhdVlXKiu36U2_8_EawzxD6mBW-VzUCvB7NKjJIWpUz8OfJrfsILohkr0vaLHyVQiWNT6gcT2rg0-TxbvRdD_HXLXKwWVaffQEH6P_wKAbDHWeK5gqqiI6dm60d_No5CPEhQVokG-Mh153m9Mg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وضعیت فعلی جام
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/funhiphop/79154" target="_blank">📅 02:49 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79153">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">مکزیک قطعا اکوادور رو میبره
شب خوش
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/funhiphop/79153" target="_blank">📅 02:17 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79146">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">فرمانده نیروی زمینی سپاه درمورد جنگ زمینی:  یک دفاع ملی چندلایه برای ایران آماده شده است که ساختاری غیرمتمرکز و رویکردی نامتقارن دارد که جنگ را برای دشمن سخت و غیرقابل کنترل می‌کند. جغرافیای ایران زندان و مردابی برای هر مهاجم زمینی‌ای است. نمونه‌اش ماموریت…</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/funhiphop/79146" target="_blank">📅 01:36 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79145">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LgGHJ1Wbej7uZ643hR1OMB--xEx4d5_nFpFxnVyG-RtwSO2AP-1lSr7dnQlC-4tuxwVRrhmbAYqq1-2FxjBiUwMPa7AKRyHXlOViwkP1cG_XotJtOWUwuFVSq1PYfqLS8FTssfGq7y0v8ry2XcM0MjFZR5M74u59Ae3HAOzYF_ZzeWNCHArdjhRG6kibloZyuSSF-zk7-SxLz9iF-8CryUew-EaGaNJ-1B27ErjSakEDLmF9sWoLh8V8T355JXEoTSIrqQaBj8dXCCGgwualO5qv8frFxLHSaLbeSiuIJjB1xPUxFYejbqAYv0u5lzHB1HqCI1lDNnByVlFpuI4ZUw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آماده حمله زمینی امریکا باشید
ناوهای آبی خاکی USS Boxer و USS Portland آمریکا شامل چندین هزار تفنگدار دریایی وارد منطقه خاورمیانه شدن.
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/funhiphop/79145" target="_blank">📅 01:26 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79144">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">اولیسه و امباپه جوری کنار هم خوبن من بارسایی هم یه لحظه دلم خواست اولیسه بیاد رئال</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/funhiphop/79144" target="_blank">📅 01:17 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79143">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">امباپههه
فرانسه برگشت
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/funhiphop/79143" target="_blank">📅 01:15 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79142">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">اولیسه داشت گل قرن رو میزد
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/funhiphop/79142" target="_blank">📅 01:06 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79141">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">امباپه زد ولی افساید
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/funhiphop/79141" target="_blank">📅 00:50 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79139">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/trY7zIfnvwwPvAUH-JyM4tTtuPo3So9jAg7meCnQuOWDWLdTg7QFtAJT-vipSKMWAZmuwJsXJHcPR1PB117G34zYMj6_hw89XFQX8fEH7k1A5llSM2aPRPSZYJRLZmxIqti5E4x38xW_cF92_hEUrh5r3faU1ulIPhF2MSlnB0IkFW8DYljDvmjTshs2RDRTlIjgL5Ht-F7bD4qmsxpyssgM0LaEp1hYKLS-qtEbcZsL9TMBOthDcDZ6YbjVFeOcj7BXVbsdsxKbLRx_dQryWB4qbCWPfmGPikXxKBwfjZyfnpeY1Nuw9ddGQm30ec7iqHBf4XHY925UFw2lrhZktQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عکس تابوت علی خامنه ای منتشر شد
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/funhiphop/79139" target="_blank">📅 23:03 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79137">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">صداسیما سخنرانی ممدباقرو قطع کرد
@Funhiphop
| Mmd</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/funhiphop/79137" target="_blank">📅 22:56 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79136">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dbOQjh8HGAmomXVgQxgJGgSNWDSovruU5Pt20YSsryOJDbfuzO9_GVOqb4neMivy-I2k5KW-vATXXJH1zDU15Tb0FzltHHLX2u4kKSMm17SotNqBNmnsLDKkLTFAQDf08vagHZJwZPekttZJNULnmYEW3Z_FUaz9nKeI66CahG9day319uU07FPsWngDQ_F2U69WvALdMTcbkeVxEmrbxpXMjJVG3WkL7R-9ISKSMNccI7k2i25SXLwGCGsAYpmeiRxBE-RMlzF-fIh7--8aMh-oL6WM6HDFcajFBgluUCf4CBWtFffugNEjHCzv8bon-SZDxLPzuhQH-Au1bVzGZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اسنوپ داگ
:
«یک نفر دارم که تمام‌وقت کنار من کار می‌کند و تنها وظیفه‌اش این است که به شکل حرفه‌ای برای من ماری‌جوانا و گل بپیچد. در رزومه آن شخص، در بخش مهارت‌ها واقعاً نوشته شده «پیچنده حرفه‌ای» این تخصص اوست.
من سالانه بین ۴۰ تا ۵۰ هزار دلار به او حقوق می‌دادم و تمام هزینه‌هایش را هم پرداخت می‌کردم. اما اخیراً متوجه شدم تورم در آمریکا خیلی بالا رفته و همه‌چیز گران‌تر شده است. مجبور شدم حقوقش را بیشتر کنم. تورم آمریکا عجیب بالا رفته.»
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/funhiphop/79136" target="_blank">📅 22:44 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79132">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">۶۰ گل ملی در ۵۳ بازی برای هالند
😐
🔥
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/funhiphop/79132" target="_blank">📅 22:18 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79130">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8cd63244ad.mp4?token=a5anA95wq3lWhIVCxjqTjzOdhIeSLoizAYflzDxebGVVyJnbEIJI-QraKmioMkPOqh-3RYUAlmkiKcRr7cfxCJKUkZZLDrSmn2k1JZkKIUgUbR6SoM3DeIRagorE_19Fp9rn_MH6pmRHCLTcDbJtN4383FQIFHFRHmFMGVI6Uy-b9TY_ZKuiTqwYDpXIzxRNTsl5jBfRRDtckKJYM4--VVQwC7cDVEsuBl6MtwepCxBTwVYXnWUMpnsCf0ToNr8W4zWGbwL9r1u8NLYOL10ackfZDqRMjQwT5aCP3q5xZjTxfpgS-LsJWAhGhewW6H89BjuHO83PLPVus06dRA8PnA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8cd63244ad.mp4?token=a5anA95wq3lWhIVCxjqTjzOdhIeSLoizAYflzDxebGVVyJnbEIJI-QraKmioMkPOqh-3RYUAlmkiKcRr7cfxCJKUkZZLDrSmn2k1JZkKIUgUbR6SoM3DeIRagorE_19Fp9rn_MH6pmRHCLTcDbJtN4383FQIFHFRHmFMGVI6Uy-b9TY_ZKuiTqwYDpXIzxRNTsl5jBfRRDtckKJYM4--VVQwC7cDVEsuBl6MtwepCxBTwVYXnWUMpnsCf0ToNr8W4zWGbwL9r1u8NLYOL10ackfZDqRMjQwT5aCP3q5xZjTxfpgS-LsJWAhGhewW6H89BjuHO83PLPVus06dRA8PnA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خالد مشعل یکی از رهبران حماس درکمال گستاخی اومده گفته رهبر معظم انقلاب اسلامی زبونم لال فوت شدن.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/funhiphop/79130" target="_blank">📅 22:08 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79127">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">ساحل عاج واقعا شایستگی یدونه گل زدن رو داره</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/funhiphop/79127" target="_blank">📅 22:01 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79126">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">میثاقی: بیرانوند از بشیکتاش ترکیه پیشنهاد داره  @Funhiphop | Menot</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/funhiphop/79126" target="_blank">📅 21:52 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79125">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">میثاقی: بیرانوند از بشیکتاش ترکیه پیشنهاد داره
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/funhiphop/79125" target="_blank">📅 21:42 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79121">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">ساحل عاج فعلا بهتر از نروژ بوده
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/funhiphop/79121" target="_blank">📅 21:00 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79120">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">نروژ یکی از استان های خوب ایران
به امید برد فرزندان کوروش
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/funhiphop/79120" target="_blank">📅 20:49 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79119">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/97a96b4393.mp4?token=lF1Y-o8PXHp0KZWnzgCtDG5aTi34T4h5hQjwazZeiSZUJRLcABeUtGth2OMb6akFQKlwYn_FAvV_o5tLWyEdQ9HBuvnhnDfA_AxihA9bC6l7pFzV1YGmn8DOeepXpr5BalcDVZNdVkBL9UyW2dvDUqQ2ou9vkIv-gRc0X2Pd-4HbdnmQlnRZm3ZrZIIcYsB6nheS93bqdcZCTWMli1nTm-f4B2oaL37Fm017R0s22YIwIxOrJEJXfWGxP_jKmoJ5lcBwW7OetBeTqwAQdBTqK-0TSEq9aoxw6z3r87jl3QsyR0smBWgBKtqk41l3SyUFD56vtR8fZHC6RfN3OmWquw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/97a96b4393.mp4?token=lF1Y-o8PXHp0KZWnzgCtDG5aTi34T4h5hQjwazZeiSZUJRLcABeUtGth2OMb6akFQKlwYn_FAvV_o5tLWyEdQ9HBuvnhnDfA_AxihA9bC6l7pFzV1YGmn8DOeepXpr5BalcDVZNdVkBL9UyW2dvDUqQ2ou9vkIv-gRc0X2Pd-4HbdnmQlnRZm3ZrZIIcYsB6nheS93bqdcZCTWMli1nTm-f4B2oaL37Fm017R0s22YIwIxOrJEJXfWGxP_jKmoJ5lcBwW7OetBeTqwAQdBTqK-0TSEq9aoxw6z3r87jl3QsyR0smBWgBKtqk41l3SyUFD56vtR8fZHC6RfN3OmWquw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
تحلیلگر صداسیما:
جنگ تموم نشده در وقت استراحت بین دو نیمه هستیم؛ نیمه اول هم ایران یجور زد گاییدشون که کل جهان خایه کردن.
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/funhiphop/79119" target="_blank">📅 19:55 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79117">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">یه بروزرسانی داشته باشیم از اتفاقات اخیر: محسن پاک‌نژاد، وزیر نفت رژیم جمهوری اسلامی استعفا داد. محمد اکبرزاده، معاون سیاسی دفتر نماینده رهبر جمهوری اسلامی در نیروی دریایی سپاه پاسداران در یک حادثه رانندگی در استان کرمان کشته شد. فرزاد جمشیدی، مجری صداوسیما…</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/funhiphop/79117" target="_blank">📅 19:36 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79116">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">یه بروزرسانی داشته باشیم از اتفاقات اخیر:
محسن پاک‌نژاد، وزیر نفت رژیم جمهوری اسلامی استعفا داد.
محمد اکبرزاده، معاون سیاسی دفتر نماینده رهبر جمهوری اسلامی در نیروی دریایی سپاه پاسداران در یک حادثه رانندگی در استان کرمان کشته شد.
فرزاد جمشیدی، مجری صداوسیما که در تجمعات شبانه بار ها علیه تیم مذاکره‌ کننده ایران سخنرانی و از آنان انتقاد میکرد، به صورت ناگهانی سکته کرد و مرد.
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/funhiphop/79116" target="_blank">📅 19:35 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79114">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">به نام خدا
بریم سراغ پیشبینی دقیق بازی های امشب
۱: صعود نروژ
۲: صعود فرانسه
@Funhiphop
| Farid</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/funhiphop/79114" target="_blank">📅 18:24 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79113">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/25d3fbfab9.mp4?token=bZa5rGIfqGPuv6OeBppyTfQFtzw1k8nyBsbqaQaizF-VJ5QpwUnyZgwCXRTXyFXsvRSG7Vl7lfhrIU1Nj_YP9lxqZKZa7P_7zf71r8gMhKIuvcvfGchNbAdNPpvuSDE_bbWn4mxGGlVI5IeR75oA1S0eNXwXCjhKYgermrZ2Dk5RN8MIpQ4sP0SpGCvnhOk6aXHaVz6AHTYFmxkavrvqqpqhoivSCI3Kdj4HS8OvTuIeX9-K3dfaCdYlz2JHooXmUwDZT3dUf2GfRUv6jpKYHJjvbrjWbI6W0pqhIJsJWdZKaCVzevlvzsiU2EM0AeatE7-fRkrtxfeuLllSGg7nXQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/25d3fbfab9.mp4?token=bZa5rGIfqGPuv6OeBppyTfQFtzw1k8nyBsbqaQaizF-VJ5QpwUnyZgwCXRTXyFXsvRSG7Vl7lfhrIU1Nj_YP9lxqZKZa7P_7zf71r8gMhKIuvcvfGchNbAdNPpvuSDE_bbWn4mxGGlVI5IeR75oA1S0eNXwXCjhKYgermrZ2Dk5RN8MIpQ4sP0SpGCvnhOk6aXHaVz6AHTYFmxkavrvqqpqhoivSCI3Kdj4HS8OvTuIeX9-K3dfaCdYlz2JHooXmUwDZT3dUf2GfRUv6jpKYHJjvbrjWbI6W0pqhIJsJWdZKaCVzevlvzsiU2EM0AeatE7-fRkrtxfeuLllSGg7nXQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تیزر تبلیغاتی جدید فیلم اسپایدرمن با حضور بهترین تاریخ
@FunHipHop
| Jenayi</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/funhiphop/79113" target="_blank">📅 18:10 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79111">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KdkJlIU5J3aQfJAUy713_MWh5aEMuwmynZGMecv7qCrnSKQd1Ay1fyAOlyVE42mXkZGoI2-tNspqyOuu1OQMhL3VpkCqLOYti3HpQqWhjoENTTeOLAyLi1C8nUJh8h021cIv_jD7jPelbKBislDyG9Kclxm21Ov9kvM4riQ_kKCP7WwDWi95wO-4V0DSDyjeHPwF_Iq-qcTtDBPLvyBq98KC5MIlsvsvL0PCej-b-Q5Mz7dkaKngL98AD4PFWQbuqDzB3hesm24Bh5vRi9JfcztLLq3abjJp4Wlz63KZEqZMwV6wHXeQM6XiUWRPeJUcaAFJSGOTyq2FKHyK5EW4XA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اسپانیا و ارژانتین رو هم حذف شده بدونید.
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/funhiphop/79111" target="_blank">📅 18:07 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79110">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">شبکه i24:
ارتش اسرائیل در حال آماده‌سازی برای ازسرگیری فوری عملیات نظامی علیه جمهوری اسلامی است.
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/funhiphop/79110" target="_blank">📅 17:38 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79109">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JrkLmoii329mtzHZNxqqiyAK9eeMME09Td8O1jPZIgNWh3x79RhN6ao3TUeadESsIwHVHCLIHlsu10x0cNJ0DueWANGoNTKT1ceO1e62AK9sPpWiTfvCrnqduD9p9nP3DAfKQ5elwGunh0Og1rmJhCxFEv-Gu_nC7Gt1sIaxAdHzYAjuSMvG6_IisBTyMmQYusKWtDnuZqLB0U_gwVi0KDbuoUt42U_td-D9YeLFtzP-IWqfc6lTiBtLbJfrkjLrXjECJrUKT-dHaz9d4KEIEmJJ27YPMytoMe6psl9fXsVwCWh1CbgDjVyO2yz5bxtmJegeEnnIHLtaanVJNL90Gw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">برج اسکم در علم نجوم در آستانه‌ی خط تورات که به معنای انبوه است قرار گرفته، اسکم انبوه در راه است
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/funhiphop/79109" target="_blank">📅 17:16 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79108">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GIsXYV6jbU-hiHGaStd3CFYt6HDohaz_m5vmwPIGHAWbssQNMmIXjugndGcIc0QvUCyjccQ-W5ewqaOYdM35o7PXe7SOJVAtA-0oQO7dY40iRa5gvh4K6teXxeaqPnyUz_mLNt_P7tHkj3otUEjz3vLJihaT9_6ZaTXkCl2Ve1mfWMd3nt6WN0TC-ON6RMqvmcYJab_RAWFw_wjhzOEtQHFbuaz97IkGzrNcf9HAGNzeLG2YTCGNXki4ZZ_u4JpuZbxynsm8YjCT1atS04vokgMDomGSsPOChMyNH7oHo9atCCeUhQCFqxgbLXRH9yQ4CkeR3q-0VyZ-E1oQ-oOHgQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این هفته توی ارومیه یه نفر بچه‌اش که دختر بوده بدنیا میاد و چون از بچه‌ی دختر خوشش نمی اومده، یه پسرو از بیمارستان میدزده و فرار می‌کنه. پلیس و پدر و مادر پسربچه الان دنبال این فردن.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/funhiphop/79108" target="_blank">📅 17:05 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79107">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MO051XpSKn-q4fU0X7EAoqkMcrbRYHWCXPLxMnuinRRwUDDiq-1BTooGLSCVOIXeqzN8AHsG8Ooj5tjS5ie0L2FrzmeXZ6F9vvyxOR8vIHoQVJswDQcm7FxJnC2-15B4efsMMo2w93flGz2d_zNRQcIY4AqEscFl8YKQ7G4MVuiSEWmMTu8HwmrlSKFHPhY8usl13WRUh9tYNDkZ1tnD0ifS_qGRGQnGWBj8HOyA6Dy6RcXLfA-KvlyZdKewXW_kzikjL_QY6uPkzWjTUHr-xagnZ4L1jQEYDQSgGKNORO6O3pfFB3FIr5RsL_aZkAhnhhpyH1wvZOBlOO6WUDroJw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اسپویل: فن خال سرمربی هلند شد</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/funhiphop/79107" target="_blank">📅 16:14 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79106">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aI8eS1LHvo64Wz6TqUsPdt5IlkWCb-HVWitcRNAf02cl4yqdSwkYJ7tx0tHGwZAITupBTKwEaW5tQZj3ggMqeBa6jbwQww8a0IxS-XTt6YvWiaKRv4YeslsFJxNjkcSPSoNXRhoGdW6O-Sw25IQ5pyv-IOja2ja0bxIA1Xle38hFHU3EFfrlFbHCjoFZnvE4vhKnPZvD437GtFGF-k_sthJyzZqVpgi3cqQoBEAi2RUeAxb0PvCvjXEKQCPm90Bdfl8tS6_0UzuUptmaahvq9IOdE0wrIuNsTQFGK8VT5f1vshPGrmqbLixTaGhR_AN1GGgu03gXN2ixc888y7KKVQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اینو کی زده گاییده</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/funhiphop/79106" target="_blank">📅 15:52 · 09 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>

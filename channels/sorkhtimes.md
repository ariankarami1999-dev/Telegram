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
<img src="https://cdn4.telesco.pe/file/hW1AhylyzIlB_-VBcv1mRg1NKm0peJzVfGwBGJT7ICNvj5H3OLizN7eqG3-iXD5mN33q6fKT-R6AOv3mwjL_yps2BnECFtugZj6yxijYCWU2ydgQg67m9PUrgauYSzwSz0T90LjauM-dMAQjpkkfibB-xlMbH86NcKsSTmrQ_yFUQL0rKdBjm4_yP_aftds1A7H-SNBXUrnzQfq9UphaPrUQZGuduWXhsJPjlr71eswua5NH-e9UpwNv211oy5LrI_YTklVGJyJ3d4N6fpOSUBSiI8PXt-Y8iHKeukiwfBoQ4cIjELGsY009NHhmCls_rddfIn8fXBrYueBgxn-mIA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 🚩سرخ تایمز🚩</h1>
<p>@sorkhtimes • 👥 21.5K عضو</p>
<a href="https://t.me/sorkhtimes" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ﷽ورزشی نویس پرسپولیس👤🎗️«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس.⛔رسانه سرخ تایمز مسئولیتی در قبال تبلیغات ندارد.</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-07-15 13:03:45</div>
<hr>

<div class="tg-post" id="msg-141050">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">🚨
فووووووری
✔️
💢
💢
💢
تاج دیروز با مدیران باشگاه پرسپولیس تماس داشته و گفته از پرونده آسانی بگذرید
‼️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.81K · <a href="https://t.me/SorkhTimes/141050" target="_blank">📅 12:05 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141049">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">🚨
ارسال پاسخ دوم فدراسیون به AFC بابت یاسر آسانی
🔺
فدراسیون فوتبال که با سؤال کنفدراسیون فوتبال آسیا در مورد شرایط قراردادی یاسر آسانی مواجه شده، پاسخ دوم خود را به این نهاد ارسال کرد.
🔺
فدراسیون فوتبال ایران در پاسخ دوم خود به دستورالعمل حاکم بر قراردادها…</div>
<div class="tg-footer">👁️ 1.88K · <a href="https://t.me/SorkhTimes/141049" target="_blank">📅 12:02 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141048">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">🚨
🚨
🚨
نامه دوم AFC برای بررسی پرونده یاسر آسانی؛ پاسخ نامه اول قانع‌کننده نبود
🔹
کنفدراسیون فوتبال آسیا (AFC) پس از دریافت گزارش‌هایی درباره وضعیت یاسر آسانی و احتمال غیرمجاز بودن حضور او در ترکیب استقلال، در دو نامه از فدراسیون فوتبال ایران و باشگاه استقلال…</div>
<div class="tg-footer">👁️ 1.85K · <a href="https://t.me/SorkhTimes/141048" target="_blank">📅 12:01 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141047">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/S7jJvRWDBfECMmfhZA_9isSejVFMtWn_HraaCy5Px--BZT4eb9fl1Dfw9VZnNZWLiQu9dM9GTy6wOzE2EMZTWLl6WNdGheq9oxp7IEcAuFTWYEctnp_bKHNm0TOj-hl5j9yLs3oAR1ubogAdiskXqtAgpcw7m4qQCR__X1in7uimYXFaHGPIeO5EgOdsIyhYKHV35FmxGOHvk15i9wN0SOK6bJlmUhYfxrybJBPgRNjGhaplX3z34KlKEXBdqqEePfomGkRLyUGSrPQi-Qwkyxx3vCzMTKKl5-8zlXyom1dYzj6k63l28AekyRFXFUYKpn_gS1WQE-GZ1lrZYsWOzQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
پرسپولیس و دانیل گرا بر سر فسخ قرارداد به توافق نرسیدن/
فارس
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.86K · <a href="https://t.me/SorkhTimes/141047" target="_blank">📅 11:58 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141046">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IDHaoDzSuSdWz1iu5Od4mZPOCbWwNMzxo55yGMDQ9BBkv3gIz5R8mCBLMHr0xDtEyQL3LbKX8LLI-cmXBrgDWEDsD7h3GafQkGYbn_hfCUlKvk9GhzKnm53EXBFO-sweK_7PS-3WKxQDvS5zd-PiEOYP5XieSeehxYwlncJYhu1n3avlMZRSd4KmRiBULNqEVxphSj9Sa8FsVmOTWjRmplAPcqgBLpES3HRHhzR9HedMOkYWhd6_ZrcyTXcJKNBBQCnbDxefepb9uFK4mwCryeNoPOoy9E9VSeWHTdQfL9R0pk3VRo6hKkrULI9EQSBaZeLmfevAkaTQjsMXAIeBZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔹
🤩
| طرفداری:
🔴
🇮🇷
💣
علی قلی‌زاده تمایل دارد فصل آینده در پرسپولیس باشد.
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 2.17K · <a href="https://t.me/SorkhTimes/141046" target="_blank">📅 11:40 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141045">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GPPxyMDRS1hwBDYD7-YvtFYUZZVadtfTxs1rvVAD1VT3MjPb281MbaWPCPWK41kr7MlGhmfMy2tckeGQef9YayFzVpn9V_xxefEQVrWK0R0CpEAhw8LAADFOqxCE0YJTejWuzHgNtL1xt4pZk7DGcdSXec_rtHMgKj2_Y2B1jqDa6MUKl-ONiW091fvvHnnwCIU0pyh4wDW5pnXscdBj1oj87shr_eGBxyVp9XGBLdEkbZhJTsMlD7aAw4eJqtAKm9GzV0hwGxT47SC4U7hjvcyUQEjAGquTB1gh3Y3dHeB9slyW3ZxBtv30Vmdg8XW0SFVu05JazjbBCuimiWWwkw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
حسین کنعانی کماکان شرایط حضور در میدان رو نداره و به صورت قطعی، غایب بازی پرسپولیس است
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 2.45K · <a href="https://t.me/SorkhTimes/141045" target="_blank">📅 10:56 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141044">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QpsBcmQ5bdXr7mJwCs6aifGOZZrGAbktMDMbRDjkDE3uXK5uScEM7AVoenN6SOsvtxm795AQQOEPtw8ERlFmfkqkg2o1qWgs8Td4WPknY9YshnoP3WOZZqWPnnLya1d4yMKWxZtLPjRDdEzigXh5IXNEh3_KTiXhr2oSrHdlYuq74P8fkPgpsw9ciVQeEcMKXGeiKpFvBpiXgt3qK33Z4n6luLIu97mhqHrnNZM3PmGBTLSjmGjtvzguae2gOVKtSJaIkQ6T9zbL1NZvc4eDxFpcVRT23kU1do01IXR1XivyWQcXnt0sTwnclZdS_lOgEYzQUzT34X2fmK5O_nUq6A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
استقلال بیانیه داده راجع‌به آسانی و گفته رقابت را به‌خارج از زمینِ ورزش نکشونیم
❌
کسی این حرفو میزنه که خودش از گل‌گهر شکایت کرد بخاطر باگناما و حکم ٣ بر هیچِ انضباطی گرفتن با همون امتیاز مفتِ شکایتی قهرمان شدند‌. یقه‌تون رو سر آسانی‌ ول نمیکنیم‌
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 2.99K · <a href="https://t.me/SorkhTimes/141044" target="_blank">📅 09:50 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141043">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/U9oIUYx3oBZEGQHxQariTn4-Gbml6y4aVstUxMP-R_iUaWMljpNySQ9VnsbKgVyGlo_rgRa4e9afTlCtgNOR8I316XTKZWmI-hnSNy8ZWBcNQ8MintVOhrmVuHhTdeOc1J7ReeCtoL_4Jycn9rjg7b2vw-8VLXDI7_r-eMuY43XyPYC-6TH719bvfz5cp22CVK63TeVU-l1ju1Rlly2vaWhVKXpxBQ-kWuLwMqcBTdQuco1ZUMV5yh9jSH0FOsjytfQ4UPtcbnZw24kZVhAIZFdIefOXD2ICdXmfundCmUFDrGXDPxCpaX6JYwxB2drkTKapS4svGo96-Q_9HmS_kQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
لیونل مسی تو بازی خداحافظی‌اش، ۹۳۲مین گل دوران حرفه‌ایش رو زد؛ ۱۲۶مین گلش با پیراهن آرژانتین!
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 2.94K · <a href="https://t.me/SorkhTimes/141043" target="_blank">📅 09:49 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141042">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">🎙
🇦🇷
لیونل مسی: غمگین‌ترین روز فوتبالم است
✖️
✖️
امروز احساسات زیادی دارم، اما اولین کسی که به او فکر می‌کنم پدرم است.چیزی جز تشکر از این پیراهن برایم نمانده. ۲۰ سال، حتی در سخت‌ترین لحظات، هرگز دست از جنگیدن، تلاش کردن، تمام توانم را گذاشتن و خواستنِ حضور در اینجا نکشیدم.
✅
✅
اینکه دیگر با تیم ملی آرژانتین به اینجا نیایم، درد بسیار بزرگی خواهد بود. دوست داشتم تمام عمر اینجا باشم. بازی برای آرژانتین، زیباترین چیزی است که وجود دارد.فکر می‌کنم وقت خداحافظی من فرا رسیده. با هم رؤیای من و رؤیای تمام یک کشور را محقق کردیم؛ قهرمان جهان شدن در سال ۲۰۲۲.
✅
✅
امروز باید غمگین‌ترین روز دوران حرفه‌ای‌ام را تجربه کنم؛ روزی که با تیم ملی آرژانتین خداحافظی می‌کنم. دلم برای همه شما تنگ خواهد شد. از حالا فقط یک هوادار خواهم بود؛ آن طرف، کنار شما، تا از این بچه‌ها و هر کسی که بعد از آن‌ها می‌آید حمایت کنم. برای رسیدن به موفقیت‌های بزرگ، به گروه‌هایی قوی و متحد نیاز دارید. از خدا ممنونم که مرا آرژانتینی آفرید. به آرژانتینی بودنم افتخار می‌کنم و خوشحالم که توانستم این رؤیا را در کنار همه شما به حقیقت تبدیل کنم
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 2.89K · <a href="https://t.me/SorkhTimes/141042" target="_blank">📅 09:48 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141041">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XcUF1KoI7Q1nC2sr4u1MZmy9fxP0Bwc2CneYkovIZW0j402IoyISukL07QG6WfSa_I3aidPDaVehqi5ymkMq5zN9MU8hlZGM4L4zi0FdNjge5hdcNoX8lYJqVjWUXOocVt7PT9FutDgQKvlz5qgffMQLWi12wRJti2PD4R_LiJHX_zz3_KbugOjAbXSderbQFHdAtANPTnVkedlcnPyWHh47q0CHWpgvzujzXKYIT5YeUuvW3otMdON8hJN2tugAEKvhqjucphXltuUhGmhvW9Fvwh1oa0_3CbHSDiI-b2S0fwsySlO9XhQzIKpj-ilKvYDagYHpx1Xd_J6uAUMvKA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🤖
ربات وینکوبت در دسترس تمامی کاربران
🟢
بدون اینکه از تلگرام خارج بشید میتونید مستقیم وارد سایت و بخش بازی‌ها و کازینو بشید، پیش‌بینی ثبت کنید و براحتی واریز و برداشت انجام بدید.
📌
حالت Mini App داخل تلگرامه و خیلی سبک‌تر و سریع‌تر براتون باز میشه:
👇
🤖
@Wincobet_bot
🤖
@Wincobet_bot</div>
<div class="tg-footer">👁️ 3.78K · <a href="https://t.me/SorkhTimes/141041" target="_blank">📅 01:01 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141040">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">⭕️
⭕️
ترامپ:
🟢
اکنون باید تصمیمی بگیرم: یا ایران توافق را امضا می‌کند، یا دیگر وجود نخواهد داشت.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.16K · <a href="https://t.me/SorkhTimes/141040" target="_blank">📅 00:24 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141039">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">❌
❌
❌
کهریزی از استقلال دور شد؛
❌
❌
محمد محمدی، مدیرعامل آلومینیوم اراک، به‌دلیل اختلاف در انتقال خلیفه و گودرزی به استقلال قصد دارد رضایت‌نامه عباس کهریزی را برای باشگاهی غیر از استقلال صادر کند.  «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس …</div>
<div class="tg-footer">👁️ 4.19K · <a href="https://t.me/SorkhTimes/141039" target="_blank">📅 00:23 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141038">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">🚨
#تکمیلی؛گویاخبر آزادی امیر تتلو خواننده مطرح ایرانی از زندان تایید شد و بزودی او آزاد خواهد شد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.82K · <a href="https://t.me/SorkhTimes/141038" target="_blank">📅 23:34 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141037">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">🚨
🚨
فووووووووووری
🚨
🚨
احمدرضا براتی کارشناس حقوقی: حتی اگر آسانی فسخ کرده باشه نتایج سه بر صفر نمیشه و فقط پنجره استقلال بسته میشه و آسانی چهار ماه محروم میشه
😐
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.83K · <a href="https://t.me/SorkhTimes/141037" target="_blank">📅 23:12 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141036">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">🚨
نایب رئیس فدراسیون فوتبال پرتغال: رونالدو دیگه به تیم ملی برنمیگرده  «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.91K · <a href="https://t.me/SorkhTimes/141036" target="_blank">📅 22:46 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141035">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CHHa5QWUqdVTRS5fS0aHQiu4dbqVTn9Gx8O4_gspngC4ITQ7FgBowcyzcMC6_duIl73bCLvP5CftwWRXwwIhU9AS6o_A_Fp1b9-KVmFDBywsNv-vDKiuca8zHBs79xNa38XzWamSjGrxWSQ-Zmgq_dlD0IqXCXNb8FbezMxPuxnNAINa1df9E4PzdQpYpYmAoRIEZyDf0zY2Kf9tXeRMI-XZs7c-WAJdmE18lgP5Qcj0eyqvGcFGCFMWgAbTBXNoF8CtMnsMPFrfTtCdAd6IfizUE1hPzTBapbYaGUJO83e9msyksQIizFcnSl-cuDkniQsmxzoxuix_nZB-01EFZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽
تصاویری از تمرین امروز تیم پرسپولیس
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.03K · <a href="https://t.me/SorkhTimes/141035" target="_blank">📅 21:21 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141034">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9f02aed72d.mp4?token=JaYxkpSQ00Wt-rHy2k-5RIwYSLWLvXyir_ER_LQ0AEWkVm1OlLpPgLg76MbMn5Xy9UWLASRHJq0TnLkVhcYfAiX6I7eQ801LYe7vwWaQyCkCqdOL0DxZK4zyUcG9EBLOS2MIdXH7KrrXfkG5XiTBmtof25QxTGeVP2Sp4uYKDK7RO35GxXvxUk8449d2PRE2RLVSb_6PbQ-OzrmHDT-IYHUjp3GYkWytKkRw2UxaMuAD1Ci4Y5FsNVO2_aNy4KMPXx8uDS0-UgNNig95QUZ9lS2g9mc9wo75tZodH4SF4PEjP6hSwZ2yKvjEjrc0LdmnzffSqI6kZzp_TN3fOvvFxhjZHlLNLXyOYhUNHKOF8IfiQ2rAh0T4PSkGoqJ7ma8jcv4k3dqGK5hQvF1_EBeVPbk4ZEcSDbeepN7Q0C2Q0siMfJP14Gxb2ppPheOiHQ_DFW1NsFt_w-8wrN0iIpgFZmCudN89kZAC58C42w5wTa9xl5OpzYIQAJpKAF14pDk2MjxZ51k3SFfTBVK0GFpFXHS47DPDDPJbR24izl4rgqsR4cvujtPSUyp-nWuTk2OA6ASo7N-hYWu1hKB3gyRp5LV4ppAG5P_uVi9AeFnAo9u-rcDVMhU2ijPc4ILvOPCcs40kaK9xRxvSzQL8ndVNet41ck-d8XuL2YQjy5g_RG8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9f02aed72d.mp4?token=JaYxkpSQ00Wt-rHy2k-5RIwYSLWLvXyir_ER_LQ0AEWkVm1OlLpPgLg76MbMn5Xy9UWLASRHJq0TnLkVhcYfAiX6I7eQ801LYe7vwWaQyCkCqdOL0DxZK4zyUcG9EBLOS2MIdXH7KrrXfkG5XiTBmtof25QxTGeVP2Sp4uYKDK7RO35GxXvxUk8449d2PRE2RLVSb_6PbQ-OzrmHDT-IYHUjp3GYkWytKkRw2UxaMuAD1Ci4Y5FsNVO2_aNy4KMPXx8uDS0-UgNNig95QUZ9lS2g9mc9wo75tZodH4SF4PEjP6hSwZ2yKvjEjrc0LdmnzffSqI6kZzp_TN3fOvvFxhjZHlLNLXyOYhUNHKOF8IfiQ2rAh0T4PSkGoqJ7ma8jcv4k3dqGK5hQvF1_EBeVPbk4ZEcSDbeepN7Q0C2Q0siMfJP14Gxb2ppPheOiHQ_DFW1NsFt_w-8wrN0iIpgFZmCudN89kZAC58C42w5wTa9xl5OpzYIQAJpKAF14pDk2MjxZ51k3SFfTBVK0GFpFXHS47DPDDPJbR24izl4rgqsR4cvujtPSUyp-nWuTk2OA6ASo7N-hYWu1hKB3gyRp5LV4ppAG5P_uVi9AeFnAo9u-rcDVMhU2ijPc4ILvOPCcs40kaK9xRxvSzQL8ndVNet41ck-d8XuL2YQjy5g_RG8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚽
🎙
گرشاسبی:
🔻
تاجرنیا نباید دنبال این جام باشد.
🔻
قهرمانی پرسپولیس در سوپرجام با قهرمان سال گذشته استقلال در لیگ خیلی فرق دارد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.94K · <a href="https://t.me/SorkhTimes/141034" target="_blank">📅 21:15 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141033">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">✅
✅
#ورزش‌سه : حدادی پرز گفت پرسپولیس دنبال ترابی نمیره.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.93K · <a href="https://t.me/SorkhTimes/141033" target="_blank">📅 21:03 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141032">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">🚨
🔴
باشگاه‌پرسپولیس‌امتیاز تیم‌لیگ‌دویی پادیاب خلخال روخرید و از این‌به‌بعد با نام پرسپولیس B در رقابت‌های لیگ دو کشور حاضر خواهد شد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.88K · <a href="https://t.me/SorkhTimes/141032" target="_blank">📅 21:01 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141031">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XHGXxA7MiLoUcBWqZek2GRk25WRDg0X9946WKjVtkWgezskmCIr75-XT2pl0sjZRkO7ZLNd_-dRRLIleEmAUCh8CLc9x_nhDLEivGC56cQ6m7_AuGWTVXUzhss2jf_ruAN4XwbbEUci7KFFU1kCem0g_DV5DCtTPU9Pqk8oEDfmSr7CDNC11CvkKmsf0huMxP1PIAIBskBlFYsSfKX-uuqyS-R_4kdH1JJ-v31s3wwx707DL5A3GXb52Dee4bHGPndPC2QUp_p-ESt2nFjPjFpZ4LTfm9MHz6V3bErhvqPGAYZCmT5InBqs9vUZhIr1iY9thzddIILk2PJvM5l37KA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❤️
Croatia -
🇪🇸
Spain
⏰
Tonight 22:15
🏟
Stadion Poljud
⚽️
اسپانیا با ۴۰ بازی بدون شکست و میانگین گلزنی بالاتر، از نظر فرم و قدرت هجومی برتری واضحی دارد. کرواسی در ۲ بازی اخیر ۱۱ گل دریافت کرده و مقابل اسپانیا هم در بازی رفت ۴ گل خورد؛ ضعف خط دفاعی مهم‌ترین نقطه نگرانی میزبان است. باتوجه به‌فرم دوتیم احتمال می‌رود ماتادورها در این دیدار هم براحتی پیروز میدان باشند.
🎁
بونوس ویژه اولین شارژ:
فقط با ثبت یک پیش‌بینی، می‌تونی ۱۰٪ از مبلغ اولین شارژ خود، بونوس خوش‌آمدگویی رو دریافت و سپس به موجودی اصلی حسابت اضافه کنی.
🔗
همین حالا وارد مینی‌اپ رسمی وینکوبت شو و فرصت رو از دست نده و این دیدار جذاب رو پیش‌بینی کن:
👇
🤖
@Wincobet_bot
🤖
@Wincobet_bot
📌
کانال رسمی وینکوبت:
🔵
@Wincobetofficial</div>
<div class="tg-footer">👁️ 4.83K · <a href="https://t.me/SorkhTimes/141031" target="_blank">📅 20:40 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141030">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/O0LwZh8SdSdW3_c490on0hfH_XfAgbm0TX1-l3AhaO-zczW2dazyt_mRFn_EKa3_3hNYM_2L694RQos0yKdYmdzPi5g1lvBTvTSFKUjRV-tAjJgGgjiz6fLxOENHDDLFwl4lK5jc32hDScxbeJDXWS_Zy-8POSvcBZYowSWFTh7epEFMx8jWdmRRVSFqtxa__Y6B4e1SyrmGcFzUn9PA90mQyL28CiCfr8LZqJyeuCsOSCPxxRwK3KEe3-MxAhNybZSOnQZ9hmSqvkKmHnsunPKGdEp8t8h5eNbItT_K8yHVxjeSH1nI_TMMg6iOO0D17uhbfzvulJ3irm9Xwmys0w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
محمودی: تمام تلاشم رو تو تمرینات پرسپولیس می‌کنم تا نظر کادرفنی رو جلب کنم. اول می‌خوام تو پرسپولیس بدرخشم و بعد بتونم برای تیم ملی هم بازی کنم
❤️
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.78K · <a href="https://t.me/SorkhTimes/141030" target="_blank">📅 19:58 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141029">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">✖️
✖️
✖️
مهدی تارتار با بازگشت مهدی ترابی مخالفت کرد/ورزش‌سه   «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.76K · <a href="https://t.me/SorkhTimes/141029" target="_blank">📅 19:54 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141028">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/f67oOKEwrzDWpqf27y5wjeqUjFNTmzBhtTm2tiY2CAdstBWdTEbDbzfIQYMKGWR1_e_kUxLmq4LPF1ErgldbEt-bLXjdU94a5gWWWsSDnIYTarKuYxSCNb-H0gerbUyNCzOLjBZcRXeAIsmeeeWy0_BGiP-y3dPUuWiCHHK-pwddT--oPwnTx0Xqecj2jCF8eSGcRKcbeQbt-844bhuemB36pM-qGQv5-zeFvb9vXXRSJKsLBFDWIQifwE2Pe6cruadySNGZ9VVeb48p5txnUH5WZTYGErutQ97c3MiLBKS3BkCCV7Dl1y7BzU_tAXx8ctmGjpowi-MxgXe6sPoB8A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
✅
آمریکا ویزای تیم‌های کشتی ایران را صادر کرد
🔹
آمریکا به تمامی کشتی گیران و اعضای کادر فنی تیم‌های ایران به غیر از یک مربی روادید حضور در مسابقات زیر ۲۳ سال قهرمانی جهان را صادر کرد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.9K · <a href="https://t.me/SorkhTimes/141028" target="_blank">📅 19:53 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141027">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">✔️
✔️
✔️
منهای ورزش :همراه اول تو جدیدترین شاهکارش، سقف مصرف بسته اینترنت ۷ روزه «نامحدود» شبانه رو از ۱۰۰ گیگ رسونده به ۲۰ گیگ!
✔️
اینترنت نامحدود تو ایران = ۲۰ گیگابایت!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.89K · <a href="https://t.me/SorkhTimes/141027" target="_blank">📅 19:52 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141026">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">🔻
🔻
🔻
🔻
سویه جدید کرونا، کاتریدا نام دارد!
🔴
مینو محرز، عضو ستاد ملی مبارزه با کرونا، در گفت‌وگو با #جریان:
🔴
کاتریدا، سویه جدید بیماری کرونا است که در اکثر نقاط جهان شیوع پیدا کرده و بیشتر در افراد مسن مشکل‌ساز شده است.
🔴
این بیماری، برخلاف قدرت سرایت بالایی…</div>
<div class="tg-footer">👁️ 5.28K · <a href="https://t.me/SorkhTimes/141026" target="_blank">📅 17:54 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141025">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ThDvwxeprGD3aSuHUdt43hC_0csq_MCvLT-zQ8-icQJqW-lBVj0tpRQk8nvQyLp_DMm4f3dtUbHuTnRQiynkxaXEVyR9Kre-q_Th_UNGYuy4OLeVwFEcOTo24gRaeCInOBirpI4xzHrCiq_Bgm0ZS9NO49jVgmKR3QwL99TqdgRqIovD8B1_KSXYkr9RmyGUvecno7AybC_Cjhz60e-TdGRubQED9IE3i7R1xgIK374dfZQVdVueIsQFtHf5gtb6GXzZVWv6ZO-ltkKo_6EwOQTHmTfswPic_42mii9A9FpWlzPpuT6c9lGrSR1BrbAq78U54yo-_T3QJpi6dxLcew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✖️
✖️
دنیل‌ گرا در دفاع چپ؛ چراکه نه
🤝
🤝
باشگاه پرسپولیس برای دنیل‌ گرا هزینه کرده اما ماه‌هاست که از این بازیکن بهره‌ای نبرده است.‌ گرا بزودی وارد چرخه تمرینات گروهی و مسابقات خواهد شد و می‌تواند گزینه دیگری در اختیار تارتار باشد. او در دفاع راست رقیب تازه‌ای برای مجید عیدی خواهد بود اما همچنان یک بکاپ مناسب برای دفاع چپ نیز به حساب می‌آید. پرسپولیس در دفاع چپ همچنان دچار نگرانی و کمبود است و با مصدومیت‌های متعدد جلالی اوضاع کمی نگران‌کننده پیش می‌رود پس می‌توان به جابه‌جایی‌ گرا از راست به چپ و حتی روزهایی که عیدی روی فرم نیست حساب باز کرد
✍
ورزش‌سه
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.11K · <a href="https://t.me/SorkhTimes/141025" target="_blank">📅 17:47 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141024">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TiBVanyUS6Ji-IPEa8z2fUGhs25bId4xUPrVVWqWoHqnx8qyAGnLQyv-uHDcSS0rGs4NNNwr23g77dhlRIFkweHdhS79UePIKS7gUNvWRU8hZ3sH9QK1toODGX8_JfLslnvh5hBcdWKm3NMjU7CMEHhhIeGj7EgyFtOAGyydOwzLpYT9lDTyQ-3GbrfD3-C1XP2dC5nCZOK6GK1vqg3pK2AVt8iGwOW9wRvtuHQLxm2qn5ynG216GbaIcMCn6IZMWvXBcTzQjgy_yP3mSBd3_v4YfjLzue718L73ediv5QNUFyhe4mbJ6-bxP7vh0XZq1xgHMigalu5w80YN3OBmdQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💰
مجموع قرارداد بازیکنان پرسپولیس اعلام شد
⛔
⛔
مدیرعامل پرسپولیس: «جمع قرارداد پنج بازیکن خارجی ما ۴.۰۸ میلیون دلار است.»
🔹
با دلار ۲۷۰ هزار تومانی، این مبلغ حدود ۱۱۰۱ میلیارد و ۶۰۰ میلیون تومان می‌شود؛ یعنی حدود ۱۰۱ میلیارد تومان بیشتر از مجموع قرارداد ۲۷ بازیکن ایرانی.
🔹
مجموع قرارداد این ۳۲ بازیکن هم به حدود ۲۱۰۱ میلیارد و ۶۰۰ میلیون تومان می‌رسد.
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.98K · <a href="https://t.me/SorkhTimes/141024" target="_blank">📅 17:45 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141023">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">✅
✅
مهدی ترابی به نزدیکانش گفته بعد از اینکه رباط پام رو عمل کردم، هفت ماه دوره نقاهت رو گذروندم و تمرین بازتوانی رو هم تمام کردم دوست دارم به پرسپولیس برگردم!//خرمی
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.95K · <a href="https://t.me/SorkhTimes/141023" target="_blank">📅 17:44 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141022">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">🚨
🚨
🚨
سرقت موبایل از سرمربی پرسپولیس
🎙
🎙
هفته گذشته موبایل پیمان حدادی در مسیر بازگشت از محل مسابقه به سرقت رفت و حالا این اتفاق برای مهدی تارتار تکرار شد.
🎙
🎙
امروز پس از تمرین تیم پرسپولیس، دو موتورسوار در اتوبان تهران کرج موبایل تارتار را سرقت کردند.  «سرخ…</div>
<div class="tg-footer">👁️ 4.97K · <a href="https://t.me/SorkhTimes/141022" target="_blank">📅 17:40 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141021">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">✖️
✖️
✖️
یکی از مدیران باشگاه استقلال: محمد خلیفه و حبیب‌ فرعباسی دو‌گلر تیم‌استقلال هستند و فعلا هیج برنامه ای برای جذب گلر جدید نداریم.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.27K · <a href="https://t.me/SorkhTimes/141021" target="_blank">📅 15:06 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141020">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">✔️
✔️
جباری: اورونوف قطعا مورد اعتماد ماست نیاز به زمان داشت تا با تفکرات تارتار هماهنگ بشه ما هم وقتی دیدیم پیشرفت کرده برای تشویق فیکسش کردیم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.41K · <a href="https://t.me/SorkhTimes/141020" target="_blank">📅 15:04 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141019">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">⚪️
فرزین معامله‌گری، بازیکن پرسپولیس برای گذراندن سربازی به ملوان پیوست.  «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.17K · <a href="https://t.me/SorkhTimes/141019" target="_blank">📅 15:03 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141018">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bjVgcrFKN6nNiSjz4FrV4y6sXdsv3Z85POppH2uL4XwaTc_R6lLO4hN_NOkIAmrtxSRC1pN1YzQiU9Qb1nycxTqpL4K8Dn0GWz48G8PFGW1MRuaN1fvZ-h4eQxWrEl6-PkTR04dQaHIvF5TYWQt_FUX5zE-Jn4rq0qehrEdwchTEMkHLCfLBKkyCSoeIi6PJoYmBamP8BqlS1oXkLgv2q38IPPmnVlrlWSzD1qdpkvT5fCVY7nab9pQOXjBm3qSEi3gPzZaADU8HvIMJkHgIdsHfi5erHq57lqIw60FTFEfqxtIpSJCUpJagdl-u9Nw2l7w4AvqmExe-_IYs_PQI7A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇺
نبرد آتشین بالکان؛ کروات‌ها مقابل ماتادورها!
🔥
⚡️
[
کرواسی
🇭🇷
🆚
🇪🇸
اسپانیا
]
⚽️
کرواسی با بازی فیزیکی و انتقال‌های سریع، می‌تواند میانه میدان اسپانیا را به چالش بکشد. اسپانیا با مالکیت بالا و گردش توپ سریع، شانس بیشتری برای کنترل ریتم و ساخت موقعیت دارد.
سناریوی محتمل: بازی نزدیک و تاکتیکی؛ برتری اسپانیا در مالکیت، اما کرواسی خطرناک در ضدحملات.
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
<div class="tg-footer">👁️ 5.24K · <a href="https://t.me/SorkhTimes/141018" target="_blank">📅 14:20 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141017">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qa3ESIEDp4HPLoRqr8tusrVXBWXK1pHEcg_AxtAJmzXwN4-6vOF00xWHt-Uyy9ZxZ8kXIF2p1_ooQOZT13bzi-f2C4v4b4IYr42PtthSbxvqqlI9oFLndOUdBqt9k379T8w6367nvikxY27JWcZJnIZUa-FlcJdfQliSCCG4V3zVk9rtTuvkatJ8zxLYbcrAl-11S0yfvc7dykOZ-yJKbJNW9GhRcCNm4Rxl0DrhGCTZstR6Y5V_fJE3E3BFG_MgNNoY_Gx_a8IU_LEmAL_yRFcoRbINfvovwyCofCoQeMHQKG9wLNacDDWQGlvhj8NJ33JiBjaOF60uTj-xYHNfEg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✖️
✖️
ورزش‌سه: برخلاف خبرها پرسپولیس هنوز در مورد اورونوف تصمیم نهایی نگرفته
دستمزد بالا و مصدومیت‌های اورونوف تمدیدش رو سخت کرده. البته احتمال تمدید و فروش او با قیمت بالاتر در آینده هم وجود داره.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.05K · <a href="https://t.me/SorkhTimes/141017" target="_blank">📅 13:48 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141016">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">✅
حدادی : در یک بازی رسمی از عالیشاه تقدیر میکنیم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.21K · <a href="https://t.me/SorkhTimes/141016" target="_blank">📅 13:44 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141015">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rbT4L10PQJNz3ToWjurBZthsTupJGty9Nmy9427HFgKfVxqn-j5Z2GL_t_jjrIxblyUBXaME0D8sPn38YS_JZw5bBGeHSfD5jDKj20KcvwgnLLNipCsPhumN9Q_czHz2v56UcZ5liH3-Gzjkr4ruM4Q2FUhcoeSWVS2nU4gUHRkBviW6AHJEoOaqdZCkuGcMYjROy5a8ZzTwflPdC5eXWyX9QOuoN0YSHIrxuYpeXRfDSqsO71cc-2hFHbUK_18wvQFkYSm2hnGkTloE4-EgTzhj1qT74dqALVON40MuBmBszORjMohVy0tQkW53bELYbFO74SZ8b3BDNOqhExHMWw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
به احتمال زیاد امیر تتلو به 20 سال حبس محکوم خواهد شد./آنا   پ.ن اینم نابود شد
🎗
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🚩
⭐️
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.53K · <a href="https://t.me/SorkhTimes/141015" target="_blank">📅 13:40 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141014">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/E_eM1OdKVGrQpUz52n5e1yChZ_Ur4NUUjCjkSkht_rAX5Axhq2L6xLFyvokwXctVqn9xe0c6G8hbQsSGUidTB1Jxf8G8tHe93qFBgkuXfNJMSZdOSXbUUKbyS_QQUs5wyRO8hSwc_-VtftIJiwhsYe_oWFYElAu8vZiFGXliHv3W0YnSJwIJ1P1nqR72h2wVlLjIht2_hQxbk8P3naA--D0bWwUgo6fOZMg3nyH8GW5YFKaM4v2GO6DniezfwhPG9P45xkzTYsiug12Ye3mKcTllYZ-5q8TxICTfW56kYoKRe7w6UVdZgiiJyGHVHo3yx-Rzy_8QMEA3Qj93_WE_eg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
باشگاه‌پرسپولیس‌امتیاز تیم‌لیگ‌دویی پادیاب خلخال روخرید و از این‌به‌بعد با نام پرسپولیس B در رقابت‌های لیگ دو کشور حاضر خواهد شد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.32K · <a href="https://t.me/SorkhTimes/141014" target="_blank">📅 13:32 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141013">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">❌
❌
پزشک پرسپولیس: دانیال ایری در آخرین بازی تیم امید دچار کشیدگی بالای عضله کشاله ران شده و به محض برگشت به تمرینات پرسپولیس برنامه درمانی و فیزیوتراپی‌ش آغاز شده است
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.23K · <a href="https://t.me/SorkhTimes/141013" target="_blank">📅 11:20 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141012">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">✅
✅
ترکیب پرسپولیس برای بازی با صنعت نفت دستخوش سه تغییر نسبت به آخرین بازی این تیم خواهد شد
🗣
حضور حسین ابرقویی بجای کنعانی‌زادگان
🗣
حضور تیوی بیفوما بجای اوستن اورونوف
🗣
حضور پوریا شهرآبادی بجای علی علیپور
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی…</div>
<div class="tg-footer">👁️ 5.26K · <a href="https://t.me/SorkhTimes/141012" target="_blank">📅 10:20 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141011">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oqa-pikMZ92M1hd-FOe_dtcKYFvUYQOMUBf63cmR07K8DgFVcPtaKDK_F40VHbIpazRGsIj_IGUdBEbpdzXvapqLfZPN7PUAdmgDbgx4Y_0F9GJ53LVRK9wSayKamh0eGzLapXL9yIFRRZcrTO8MMD7Ds9zOsbDFOK0ada9m6Z0hoqKxgXeGx4b47FNCQmLQDx0jZTca-IG2eYCW0fkwhKMpwZMg1OucyQ2WjbbM4iWM-aZSy8tqPM3yeA05HEpQCFOkxB_vz-mIe0KwdiMFAK0F3qMJuQwLAN9oFCFSPEoQQjwQ9ocj2MopJiO8d6EOc-zY74RRUS6xKdVD7UMCyQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
😄
بیرانوند به یعنی میگه یهنی
!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.3K · <a href="https://t.me/SorkhTimes/141011" target="_blank">📅 10:05 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141010">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">✅
✅
#فوووری از ورزش سه
✖️
✖️
محمد حسین صادقی یکی از بازیکنان اصلی پرسپولیس مقابل صنعت نفت آبادان خواهد بود
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.37K · <a href="https://t.me/SorkhTimes/141010" target="_blank">📅 10:03 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141009">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">🚨
مهدی ترابی نمی‌خواهد در تراکتور بماند و تصمیم دارد که هرطور شده به تهران برگردد و فوتبالش را در  پایتخت ادامه دهد
❌
خبرورزشی
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.23K · <a href="https://t.me/SorkhTimes/141009" target="_blank">📅 10:01 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141008">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">💥
#فوووووری  | #غیررسمی
🖍
یحیی گلمحمدی قراردادشو با دهوک عراق فسخ کرد و در استانه سرمربیگری تیم ملی امید قرار دارد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.37K · <a href="https://t.me/SorkhTimes/141008" target="_blank">📅 09:59 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141007">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">✅
✅
فووووووری
✅
باشگاه پرسپولیس نامه فسخ قرارداد یاسر آسانی با استقلال رو امروز به کنفدراسیون فوتبال آسیا فرستاد  «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.26K · <a href="https://t.me/SorkhTimes/141007" target="_blank">📅 09:57 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141005">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jhOgSH80TCEMRMGSYLrhSK0R55Z4PQ6fP1q4UlfarkOUpvN8dCteCEX5RYCN5UwVEZjYDhoumQKZSleb287B7w8dd8N0nMb2cy4D9hK7Rt_kYk_PldbU4FMPFktwP7ofjDAa9eqjp0J3HAEoD4PhMbUyx4Zfk3eIZGbaoNWhN-H11iTSOybRWlK1CPnVdwaA0VxvRfKeh9JZ-VUAY_WkJlWA33zQvzr_6AK6gV7D2LEmcIhBYw6INij4Sfj0DYoxlmctMGwShonFqYyio1WMdBwPOsnSEfvVAwEVtLTaJFrXVCdRMAZzXg0P4CtnEQFkbF2-IDx5UJXUa_6CK0LxfQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇺
سه‌شیرها در کمین؛ چک‌ها آماده‌ی شکستن نظم انگلیس!
🔥
⚡️
[
انگلیس
🏴󠁧󠁢󠁥󠁮󠁧󠁿
🆚
🇨🇿
جمهوری‌چک
]
⚽️
انگلیس با مالکیت و حجم حملات بالاتر، احتمالاً بازی را از همان دقایق ابتدایی در اختیار می‌گیرد. جمهوری‌چک روی دفاع فشرده و ضدحملات سریع حساب می‌کند؛ اما مقابل فشار مداوم انگلیس، حفظ کلین‌شیت دشوار است.
سناریوی محتمل: برتری انگلیس در موقعیت‌سازی و گلزنی، با احتمال بالاتر برد انگلیس و مجموع گل‌های ۲ تا ۳.
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
<div class="tg-footer">👁️ 5.49K · <a href="https://t.me/SorkhTimes/141005" target="_blank">📅 01:05 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141004">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TP0_zzQ_0V4CgA-v9aqmvSKSd_3AtRSrxsF2RARK26Qaur5cymzn4kHmkx3wy91i_paVN-dScbSC1F-Eiaz2-1-FxlI-W_sh75q3UWQjIYUYKOA3jYGkdVAPRiY5T9bBhrMil2nIbH-mAwEtfqmYQ11v4N22GoCj6iCZ7zALOXif0nndbq1wxE865q39M6XDeAFNjdTVG7Hf0972DhfFcv0t4l3Gp89-UCvpFICCQU20zuI8KmLZK8LcSDz5UPnpt3bx_Xx71HCc5E5EgAKYDQSLE-4NdvuLQXpEeN9JSnSrvcVK1QKqzgjD5Ntnx0xYpjtTQZj3vWrxW0qegYbo8w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
سعید شیرینی، سرپرست سابق پرسپولیس، از مطالبات حدود ۷۳ میلیارد تومانی خود از این باشگاه گذشت.
🚨
بر اساس اعلام پرسپولیس، این موضوع مربوط به دو پرونده حقوقی بوده که یکی از آنها بیش از ۴۱ میلیارد تومان و دیگری ۸ میلیارد تومان مطالبه به‌همراه خسارت تأخیر تأدیه داشته است. با اعلام رضایت شیرینی، مجموعاً حدود ۷۳ میلیارد تومان از خروج منابع مالی باشگاه جلوگیری و پرونده‌ها برای مختومه شدن ارسال شدند.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.46K · <a href="https://t.me/SorkhTimes/141004" target="_blank">📅 01:01 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141003">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">❌
❌
مهدی ترابی در اندیشه‌ی بازگشت به پرسپولیس/طرفداری
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.59K · <a href="https://t.me/SorkhTimes/141003" target="_blank">📅 23:36 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141002">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">✖️
✖️
محمودی و صادقی کماکان از آماده ترین بازیکنان تمرینات پرسپولیس هستند
✅
✅
هر دو به همراه زارع در دفاع از بهترین های بازی دیروز مقابل گل گهر بودند.
✅
✅
باتوجه به مصدومیت ها به احتمال زیاد این دو بازیکن در بازی های آتی برای سرخپوشان به میدان خواهند رفت.
🎗️
«سرخ…</div>
<div class="tg-footer">👁️ 5.68K · <a href="https://t.me/SorkhTimes/141002" target="_blank">📅 23:32 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141001">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">🚨
🚨
عادل فردوسی پور: قلعه نویی تو بازی با روسیه از عملکرد محبی راضی نبود بهش گفته خودتو بزن به مصدومیت تا تعویضت کنم
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.95K · <a href="https://t.me/SorkhTimes/141001" target="_blank">📅 22:43 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141000">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">❌
موبایل قاپ‌ها به حدادی هم رحم نکردند
💢
مدیرعامل پرسپولیس بعد خروج از ورزشگاه شهید کاظمی و دیدن بازی تیم بانوان در خودروی خود مشغول مکالمه بود، که یک سارق با موتور نزدیک شد و با قاپیدن گوشی همراه حدادی متواری شد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق…</div>
<div class="tg-footer">👁️ 5.86K · <a href="https://t.me/SorkhTimes/141000" target="_blank">📅 22:17 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140999">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">✅
✅
✅
فووووووووری از فرهیختگان
❌
❌
پرونده آسانی از دست فدراسیون خارج شد حالا دیگه فقط ای اف سی درباره این پرونده تصمیم میگیره و کسی نمیتونه کاری کنه    «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.79K · <a href="https://t.me/SorkhTimes/140999" target="_blank">📅 22:16 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140998">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">🚨
🚨
فووووووووووووری
🔴
علوی: هیچ جامی قرار نیست به استقلال داده بشه و بحث قهرمانی این تیم در سال گذشته منتفی شده
😂
😂
😂
😂
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🚨
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.74K · <a href="https://t.me/SorkhTimes/140998" target="_blank">📅 21:58 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140997">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qeA-L09epAgKZwDIbIngloviw0am_9UparaqOrGzZZQwq7Evc8NCsiBXLs2C0xvb9ZMKlRnxxE66RLbBenzSQHn6EDfWknoPgAWBKNHiBBOw1UtPw-zf-llAV4aeudRsCFy6sJk3HPP4brujf0DUbkW8YfNnJJIcqc1qR6YrbK3V6nRxPvtASFOPBVedZutY1ipKX_CUQr7T8kBMW-07hdPu0Fj50eOkW4HuZIActvYhBISoYLh6JMJZDC1dGPhAig3MpvtcDthCMy77W12vaLSpO-ZYb23h5cwef76LtDcE3vQDLaBjv4vEwGwS_KKoFEHNfZiKE9u5tLfNKI0HhQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚩
گزارش تصویری از تمرین امروز پرسپولیس
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.59K · <a href="https://t.me/SorkhTimes/140997" target="_blank">📅 21:57 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140996">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">💚
عادل فردوسی‌پور: دیگه حوصله شوخی‌کردن با قیمت دلار روهم نداریم، روزگار سخت و تلخی که سپری می‌کنیم، شروع فصل لیگ برتر، با دلار 187 هزار تومانی، بازگشتش از فیفادی، با دلار 270 هزار تومانی!
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.44K · <a href="https://t.me/SorkhTimes/140996" target="_blank">📅 21:56 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140995">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">✅
گفته میشه دولت قطر به تیم فوتبال استقلال قراره مثل آمریکا ویزا ساعتی بده تا این باشگاه برای بازی با الغرافه مشکلی نداشته باشه
😂
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.77K · <a href="https://t.me/SorkhTimes/140995" target="_blank">📅 21:12 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140994">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">✖️
✖️
✖️
فرصت طلایی
✖️
✖️
پرسپولیس در هفته‌های پیش‌رو برنامه بهتری نسبت به رقباش داره؛ استقلال و تراکتور درگیر آسیا هستن و سرخ‌ها هم بازی‌های عقب‌افتاده‌شون رو دارن.
✖️
✖️
با توجه به لغو جام حذفی، هفته‌های ۹ و ۱۰ می‌تونه فرصت خوبی برای تارتار و شاگرداش باشه تا…</div>
<div class="tg-footer">👁️ 5.79K · <a href="https://t.me/SorkhTimes/140994" target="_blank">📅 21:10 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140993">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">❌
لحظه گل ثانیه پایانی جوانان پرسپولیس مقابل پارسیان توسط محمدامین قرنجیک
👍
👍
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.72K · <a href="https://t.me/SorkhTimes/140993" target="_blank">📅 19:54 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140992">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Kko4GMFDyi8mk1Kw2i3EgTV7OA9FrxtlBpRj47-sGyKHneREUE_S4NAhDQeWF1oaRj5EvTRPMItVUHhUXjWDbFBSWT6SN4VqRhr5SIzQa4zRMMadX1jthXej5kIkH68VKvtxfOLG8ioS8l2I_PEmUgnwb_0aVP2_1Z4WHngOZsUhAMbctIOwkmSKbDQyXbn-o545wA0rrW98Uz3Q4Jcy5RqTavN_ON5mrTw8OMr6MqgYA2BjxS-fWGbzbYY6nwHSVtuRx8jc6UzTvmhxXWXB-YLoWrmiMCnQGvFTr-PRkziH16EVD42YwE6Sf6_abWeaTIZfnyJ62tpkQhA68EQl_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
✅
مهدی طارمی زمینه آزادی ۸ زندانی شد
👍
مهدی طارمی در طرح حمایت از حقوق اجتماعی و رفاه زندانیان نیازمند استان تهران، زمینه آزادی ۸ زندانی را فراهم شد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.53K · <a href="https://t.me/SorkhTimes/140992" target="_blank">📅 19:48 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140991">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">🚨
مزایده اموال پرسپولیس با یک خریدار خاص
🚨
در پی شکایت یکی از طلبکاران باشگاه پرسپولیس، دادگاه شعبه ۴۱ عمومی حقوقی تهران حکم به توقیف و سپس مزایده اموال این باشگاه داد که این مزایده در نهایت برگزار شد و بخشی از اموال پرسپولیس به فروش رسید
🚨
🚨
در این مزایده،…</div>
<div class="tg-footer">👁️ 5.26K · <a href="https://t.me/SorkhTimes/140991" target="_blank">📅 19:43 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140989">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LcKnZJYJrh4g69VT1kh3mg4JThdgKLUtsbv-WwMJcG1MrElI6dBWBnOQYQyWpqqbn4e3skwdh9o4icgTvsYmBNhQNny7wzOYsOiVhh6rEqP7-GjY87sHWO4tB7KkJU0WGSBbc46sCrcf_ckOlJgij_gZrYSJQALZ6vEZDOcG0fOT-VMp8urBP4e7r1XAZcqxUDfqh94qkksnbZIhjCl_0dkO-Hc_SVkZESk-LXFbIhltvPsr-9axth3F_-AslVE2Y4nT9RigT2FaNcOqVc5AjL9tmMv9RSnTRLzJSjbiAlTtkq63tGZ3Tpnh3aghfbfrLljk0TxvuIuZZ50RuztSmg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇺
نبرد سلسائو با وایکینگ‌ها؛ پرتغال در برابر نروژ، یک شب پر از هیجان!
🔥
⚡️
[
فرانسه
🇫🇷
🆚
🇧🇪
بلژیک
]
⚽️
فرانسه از نظر کیفیت موقعیت‌سازی و عمق ترکیب دست بالاتر را دارد، درحالی‌که بلژیک بیشتر روی ضدحمله و انتقال سریع حساب می‌کند. با توجه به قدرت هجومی دو تیم، سناریوی گل‌زنی هر دو طرف محتمل است؛ اما فرانسه شانس بیشتری برای کنترل نتیجه در نیمه دوم دارد.
سناریوی محتمل: برد فرانسه با اختلاف یک گل.
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
<div class="tg-footer">👁️ 5.37K · <a href="https://t.me/SorkhTimes/140989" target="_blank">📅 19:34 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140988">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">🔵
اعلام برنامه مسابقات هفته‌های هشتم تا دوازدهم و دیدارهای معوقه لیگ برتر
✔️
هفته‌هشتم جمعه ۱۷ مهر
🔴
پرسپولیس - صنعت نفت آبادان ساعت ۱۷
✔️
معوقه هفته هفتم لیگ‌برتر چهارشنبه ۲۲ مهر
🔴
پرسپولیس - خیبر خرم‌آباد ساعت ۱۷
✔️
هفته نهم لیگ‌برتر دوشنبه ۲۷ مهر
🔴
پرسپولیس…</div>
<div class="tg-footer">👁️ 5.27K · <a href="https://t.me/SorkhTimes/140988" target="_blank">📅 17:42 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140987">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">✔️
✔️
🚨
فووووووووری
✔️
ای اف سی در نامه ای به فدراسیون گفته پرونده فسخ یاسر آسانی مشکوکه و جزییات دقیق خواسته
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.3K · <a href="https://t.me/SorkhTimes/140987" target="_blank">📅 17:39 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140986">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UTfqvQdzcUaGSu59WVwSn0rafaRbcVz0J-p1s8uhjuXlV1PKA7TqhPRUooMo6W3HvCIGaUigyqZ1LDQ9lwE1ITBRxbuqfhLnE74IWXM3x64x35eJmNxzFW3L9Mf56Sq77ZlcFiW90uM8bRMigTK0Z2s_BKt4wuNUT0t-pxh0rSETIvorYM0TaD78E44Yc8w9XR7QMjmtVuwEJxVncr7LYMOgSyVpANTKoCD0v-Yc8SC_x6p8S1sddaVJWmVHa3msEEO93w61be3GbIkjm_NE4kyAacsdnEdcOsKkYDhcyxw2ezzidx9sSHv200TutU2V-xFcAX4mSM56O7hNC4861A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🔴
ساختمان شهدای میناب باشگاه پرسپولیس مزین به تصاویر شهدای مدرسه میناب شد
🔴
به گزارش سایت رسمی باشگاه پرسپولیس، این اقدام، ادای احترام خانواده بزرگ پرسپولیس به مقام شامخ شهدا و خانواده‌های معزز آنان و گامی در جهت پاسداشت فرهنگ ایثار، فداکاری و شهادت به شمار می‌رود.
🔴
باشگاه پرسپولیس ضمن گرامیداشت یاد و خاطره تمامی شهدای مدرسه میناب، بر ضرورت صیانت از نام و یاد شهدا و ترویج فرهنگ ایثار و فداکاری در جامعه تأکید دارد.
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.47K · <a href="https://t.me/SorkhTimes/140986" target="_blank">📅 17:32 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140985">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NduVMC64U12HyjjvHdvnqqdwrc-umbda9gAjf4gzBJkAhv1R-TdxJ8QrDop26gRct1KX8AzthRxUx22iITWAirUfkqC4aNRwnUrmDuEmF7vD-agrurILcfsfKGKAZ166JGwynAF6T_l-pjTRUMdoUuDJ4DC9_Mu9gu2PbR6qirsskBfIB3V19dCl2tOdyUNd8S4tnqK5U_alMMOnKfSSTCbX_mQQbuvzZSmbSqWzbu785pAYwZCGxiq5qsiCsej8zbApQyKi7T0pg3jX8sVFoX2rC6uqUqIiRQxEo23FRMMIjpfmr79u4QLcfVDRN-Wx8yAm_HqcXCn1swUHe0NU4g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✖️
✖️
سیدحسین شریفی به عنوان مدیر صدور مجوز باشگاه پرسپولیس منصوب شد.
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.35K · <a href="https://t.me/SorkhTimes/140985" target="_blank">📅 16:50 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140984">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">🚨
🚨
🚨
نامه دوم AFC برای بررسی پرونده یاسر آسانی؛ پاسخ نامه اول قانع‌کننده نبود
🔹
کنفدراسیون فوتبال آسیا (AFC) پس از دریافت گزارش‌هایی درباره وضعیت یاسر آسانی و احتمال غیرمجاز بودن حضور او در ترکیب استقلال، در دو نامه از فدراسیون فوتبال ایران و باشگاه استقلال…</div>
<div class="tg-footer">👁️ 5.5K · <a href="https://t.me/SorkhTimes/140984" target="_blank">📅 15:13 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140983">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">🚨
🚨
کنفدراسیون آسیا جواب فدراسیون رو نپذیرفت
✅
کنفدراسیون فوتبال آسیا برای بررسی پرونده یاسر آسانی، این بار در نامه دوم مدارک و مستندات بیشتری از فدراسیون و استقلال خواسته و تأکید کرده فوراً ارسال بشن.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس…</div>
<div class="tg-footer">👁️ 5.73K · <a href="https://t.me/SorkhTimes/140983" target="_blank">📅 15:06 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140982">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">🚨
🚨
کنفدراسیون آسیا جواب فدراسیون رو نپذیرفت
✅
کنفدراسیون فوتبال آسیا برای بررسی پرونده یاسر آسانی، این بار در نامه دوم مدارک و مستندات بیشتری از فدراسیون و استقلال خواسته و تأکید کرده فوراً ارسال بشن.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس…</div>
<div class="tg-footer">👁️ 5.23K · <a href="https://t.me/SorkhTimes/140982" target="_blank">📅 14:51 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140981">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">🚨
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 5.26K · <a href="https://t.me/SorkhTimes/140981" target="_blank">📅 14:50 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140980">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">✔️
✔️
🚨
فووووووووری
✔️
ای اف سی در نامه ای به فدراسیون گفته پرونده فسخ یاسر آسانی مشکوکه و جزییات دقیق خواسته
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.46K · <a href="https://t.me/SorkhTimes/140980" target="_blank">📅 14:49 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140979">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">🚨
🚨
🚨
🚨
🚨
🚨
🚨
🚨
⭕️
⭕️
⭕️
⭕️
⭕️</div>
<div class="tg-footer">👁️ 5.35K · <a href="https://t.me/SorkhTimes/140979" target="_blank">📅 14:46 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140978">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">🚨
🚨
🚨
🚨
🚨
🚨
🚨
🚨
⭕️
⭕️
⭕️
⭕️
⭕️</div>
<div class="tg-footer">👁️ 5.2K · <a href="https://t.me/SorkhTimes/140978" target="_blank">📅 14:45 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140977">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">🚨
والیبال به میرزایی رسید!
🔴
با حکم احد میرزایی؛ رضا صفایی سرمربی تیم والیبال پرسپولیس شد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.31K · <a href="https://t.me/SorkhTimes/140977" target="_blank">📅 14:42 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140976">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">❌
❌
سعید دقیقی در لیست نقل و انتقالاتی خود برای نیم فصل خواهان جذب سه‌ بازیکن از پرسپولیس شده است
🔴
حسین ابرقویی نژاد
🔴
یاسین سلمانی
🔴
محمد حسین صادقی
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.12K · <a href="https://t.me/SorkhTimes/140976" target="_blank">📅 14:41 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140975">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/T5j7yNRvrNvmAgGLn1dW7SliKrtB_BhTuiGzczE577gw2BbqGZBPwzSvVeK0bI4GOvDM6QNrztbx37Up78OYP_S5pgVy1PtRdJbuQAOmxSDAA5RvwCR5QPtihTKbW56apcWq3pUsLHhbgQWpCnc4dDZ2KXXqYqk6SebaO078dSOTo9eDJUivfp1lyFGb3OsZZEJO1UUYL5GG7PPqprIjUx74tnPk6BRJplBmX5SS60xMF8h8w41mXhNBYAgrrlVNFKKya6YpCXEbLMhJf0tVTSXVgCc7e1lS4rTmJrCrxsCoeeMhxRUo-BEMcxUhsZWydaqkqHRokFcHT35pmIFtFQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❤️
Italy -
❤️
Turkiye
⏰
Tonight 22:15
🏟
Stadio Renato Dall'Ara
⚽️
ایتالیا در ۳ بازی اخیر ۴ گل به ترکیه زده و در ۶ بازی خانگی اخیرش ۴ برد با کلین‌شیت داشته؛ ترکیه هم در ۳ بازی لیگ ملت‌ها فقط ۱ گل زده است. باتوجه به برتری ۴-۱ بازی رفت و برتری تاریخی ایتالیا (بدون شکست در ۱۵ تقابل)، کفه آماری همچنان کاملاً به سمت آتزوری است. احتمال می‌رود ایتالیا کنترل بازی و مالکیت بیشتر، ترکیه خطرناک در انتقال‌ها باشند و باتوجه به‌فرم دوتیم برد ایتالیا با اختلاف کم محتمل هست.
🎁
بونوس ویژه اولین شارژ:
فقط با ثبت یک پیش‌بینی، می‌تونی ۱۰٪ از مبلغ اولین شارژ خود، بونوس خوش‌آمدگویی رو دریافت و سپس به موجودی اصلی حسابت اضافه کنی.
🔗
همین حالا وارد مینی‌اپ رسمی وینکوبت شو و فرصت رو از دست نده و این دیدار جذاب رو پیش‌بینی کن:
👇
🤖
@Wincobet_bot
🤖
@Wincobet_bot
📌
کانال رسمی وینکوبت:
🔵
@Wincobetofficial</div>
<div class="tg-footer">👁️ 5.4K · <a href="https://t.me/SorkhTimes/140975" target="_blank">📅 13:05 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140974">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">✅
✅
✅
#فووووووووری از تسنیم
🔻
جلسه کمیته استیناف برای شکایت پرسپولیس از آسانی امروز برگزار میشه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.22K · <a href="https://t.me/SorkhTimes/140974" target="_blank">📅 12:14 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140973">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oJWVtMD58cm92Ly8jW3irX979R9AMo1WSekURbMuRS_huXgiY6Wtqso_0AL-yMiwA-90fK5Wtzzdyuo_3QFnrhohLKtlYAAlROfxoMcxuhaNtgLv-XeRweufhSeizHm7uQNPCzv057B-KPgSjSeQp0BP4KcsQRal4Qe_fMleFCOMTGqRPXMTdxkyZhGszXGH1QMkFAl7OaVldOmwJN4EfptAEHTuyU2M4vSwHw5gtgmmb8p4wNEPzrVpO-HJe3qEXWyWFSwjtRchTTTsrSYEQUZk3UTIzg9UPCOancwOlfG162oZV6itsk3eoF0QC66vZr5FyAebTlfs1edEnVE7vA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
مهدی تارتار قصد داره از پویا اسمی مدافع ۱۷ ساله‌ی پرسپولیس در بازی‌های بعدی استفاده کنه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.4K · <a href="https://t.me/SorkhTimes/140973" target="_blank">📅 10:59 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140972">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fHUsrkLPMeWtf8TGZ3US66iSBE7UoyQmQJPKBDPrFfuqtwocjsOsDSasZTt1lMmdFAxieZ3ruvv9fsJWjMGAbr1lrGuuT-GpblkuxB7mTS2-Zssccy2m1KWw5Mz1h6opKcHkqpUhl909rKUYKxAYz2lE1Aovx5ZTI-nSmo0I5CtMkGHUNVzDJ6-YTCi5Rat30iihQGTS6HCEVZPd8th5FJBxaTLATa0Dhx8ZbTotCRzuKKCLDiyFcHIasn0-liHr4fxwkCAuqEK5twly9OjTF2bOQCybltuROMGQpxkdYwEMqSDNrWPt64Kf7R_f_1BZ4fTLVYK9kREdKqfe86t2jQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
فوووووری
‼️
🤩
با اعلام خبرگزاری برنا
بازیکنی که مدنظر پرسپولیس بود
شرزود آسانوف ازبک بود که بین
دوراهی تراکتورسازی و استقلال قرار گرفته !!!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.29K · <a href="https://t.me/SorkhTimes/140972" target="_blank">📅 10:55 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140971">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">✅
عادل فردوسی‌پور: نیوزیلند جزو سه تیم ضعیف جام جهانی است. اما برای نتیجه نگرفتن احتمالی، برخی بهانه‌ تراشی می‌کنند. برو بجنگ بعد درباره ویزا حرف بزن.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.1K · <a href="https://t.me/SorkhTimes/140971" target="_blank">📅 10:52 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140970">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">✅
✅
✅
#فووووووووری از تسنیم
🔻
جلسه کمیته استیناف برای شکایت پرسپولیس از آسانی امروز برگزار میشه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.2K · <a href="https://t.me/SorkhTimes/140970" target="_blank">📅 10:50 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140969">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">🤩
حدادی: برای آسانی مدارکی داریم که هیچ باشگاهی نداره؛ فدراسیون هم باید استعلام فیفا رو منتشر کنه.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.22K · <a href="https://t.me/SorkhTimes/140969" target="_blank">📅 10:44 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140968">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">✅
✅
تاجرنیا: بیرانوند دوست دارد حضور در استقلال را تجربه کند.
😀
به صورت جدی درباره بیرانوند صحبتی نداشتیم اما به ما هم پیامهایی رسیده است. اما الان فرعباسی و خلیفه را داریم بنابراین بحث بیرانوند یک مقدار این موضوع از ما دور است.‌ در هر صورت او هم شایسته است…</div>
<div class="tg-footer">👁️ 5.19K · <a href="https://t.me/SorkhTimes/140968" target="_blank">📅 10:38 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140967">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cchuUjq5iQWINs2RLpaFBeNcxUGdjgfrboYrOwt2tX18J2CojN5ofajhg12q1-dZOsLlt2LccIXFHSVGPCav_hH7VmPVNtQr2XWuU-5qaIKlglASrjeixjerYyCG__irrsnWqNVhMl2Ey9w9rxzLXkLBv_FDOajmho7a4jrTLrDWQLA2KIpr86kUE7ijRk_mABO-H-MqlrsfuK3POA4aGPnrFcsLGfvLHl-hyP1_V8sJV6NHhvDtIqgWtuD72K_fJtAKJkVhFnVhQVCBm1XP0v8jbSMF8U79Fz5RYPummGNUGT-yk5q5Ugz1uNQQ3Z1wcgYPrTrF2RZBiUcD5LDohw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
شایعاتی از نهایی شدن انتقال فرهان جعفری به پرسپولیس به گوش می‌رسد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.05K · <a href="https://t.me/SorkhTimes/140967" target="_blank">📅 10:37 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140966">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">⭕️
⭕️
باشگاه پرسپولیس با خرید امتیاز باشگاه پادیاب خلخال صاحب تیم «ب» شد.
🆕
🆕
🆕
عصر امروز با حضور مدیرعامل و مالک باشگاه پادیاب خلخال در باشگاه پرسپولیس، امتیاز این تیم که امسال در لیگ دسته دوم حضور داشته به باشگاه پرسپولیس واگذار شد.
🔜
🔜
راه‌اندازی تیم «ب» یکی…</div>
<div class="tg-footer">👁️ 4.83K · <a href="https://t.me/SorkhTimes/140966" target="_blank">📅 10:35 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140965">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">❌
❌
مهدی ترابی در بیمارستان‌ آتیه تهران تحت عمل جراحی رباط صلیبی قرار گرفت و زانویش را به تیغ جراحان سپرد و شش ماه از میادین دور است.    «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5K · <a href="https://t.me/SorkhTimes/140965" target="_blank">📅 08:20 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140964">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">✅
حدادی : در یک بازی رسمی از عالیشاه تقدیر میکنیم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.4K · <a href="https://t.me/SorkhTimes/140964" target="_blank">📅 08:19 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140963">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Z1826zlQ6orbRUunn7bH25gdaiizdLlhioUQ9jZC4Ivw-NpzMhz2md2KVCZ27VUL_U0NT2Ml_w0aZj86hoPCRNNE0Ci6izs4yKqBcEE2nWd1qM6QV-vAf9ElWjQr08_bHmEdLYgmirK0hU0twz07xaz9GUUUlp4DGWnxX2Z7ihP6qVrln1Hr1m9wQOloIIIODA5EdTiE6i28-W1yqwHjBzIksShceyzLaCMnUnbYM8QTluvDd2RbtuNPeIkRpj9CUXs0Iip1K0bLmylTVnNs-mUWDCbeDSE-zTizUaBoDS3bX8tBacCFn45F9bxnef6QJ-SNJ-opR87pHPAfOj6SLA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✖️
✅
✅
صبحتون خوش ارتش سرخ
❤️
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.39K · <a href="https://t.me/SorkhTimes/140963" target="_blank">📅 08:18 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140962">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/War3LsYk-iGCe7KAdI0mDxPD5ny5tbuDi4ThDn-1HoJFa4cbD9EnLlCZENpUIoZxDp3XUdDzmOWaUb-08G03WNVLnJUZ5yqNgnyxFDNgcgdfQiP8Om7rWma03ZhuX1xf3KiKnWMXJ8a0N9Auh5IJHNWwzWlEQOqylfoXFYEVWAVtXq70u6TWu9X7wgrATjkW2RuvMzJM1Bs1Ona1s6PWgbOqwQHsyisxPPRe87MfM1CrnS70M0aWFyfFmiyUEV1AhqGOt41dJbSxnZDepvKXxJuUC3IbU2RRGPHvIu5gPo1lAvqa5CVMHWWa-10jVRCXwpWNLvtse6yf7u1XdCFa-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇫🇷
France
🆚
❤️
Belgium
⏰
Monday 22:15
🏟
Stade de France
🇪🇺
فرانسه از نظر کیفیت هجومی و میانگین موقعیت‌های خلق‌شده برتری محسوسی دارد و احتمالاً حجم بیشتری از حملات را در اختیار خواهد داشت. بلژیک در انتقال‌های سریع خطرناک است، اما مقابل فشار و مالکیت بالای فرانسه احتمالاً فرصت‌های کمتری برای تهدید دروازه پیدا می‌کند.
✅
برآورد آماری: برد فرانسه ۵۸٪ | مساوی ۲۴٪ | برد بلژیک ۱۸٪ | بالای ۲.۵ گل ۵۷٪
همچنین در غیاب دی‌بروینه و تیلمانس احتمال می‌رود خروس‌ها پیروز میدان باشند.
🟢
با درگاه بانکی اختصاصی و امن وینکوبت، حساب کاربری خودت رو به‌صورت مستقیم شارژ کن و مثل هزاران کاربر دیگه، بدون دردسر از امکانات وینکوبت استفاده کن.
🔗
همین حالا وارد مینی‌اپ رسمی وینکوبت شو و فرصت رو از دست نده و این دیدار جذاب رو پیش‌بینی کن:
👇
🤖
@Wincobet_bot
🤖
@Wincobet_bot
📌
کانال رسمی وینکوبت:
🔵
@Wincobetofficial</div>
<div class="tg-footer">👁️ 5.26K · <a href="https://t.me/SorkhTimes/140962" target="_blank">📅 01:02 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140961">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">💢
💢
مدیران پرسپولیس به تاج اعلام کردن اگه استقلال قهرمان لیگ اعلام بشه از لیگ برتر انصراف میدن
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.98K · <a href="https://t.me/SorkhTimes/140961" target="_blank">📅 00:58 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140960">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">✔️
✔️
حدادی : نمیتونم قرارداد محمودی رو اضافه کنم چون باید به سازمان بازرسی جواب بدم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.04K · <a href="https://t.me/SorkhTimes/140960" target="_blank">📅 00:52 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140959">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">❌
❌
فوووووری
🔄
🔄
حدادی: تا آخر همین ماه یه جلسه مهم برای بیرانوند تو فیفا به صورت ویدیو کنفرانس انجام میشه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.19K · <a href="https://t.me/SorkhTimes/140959" target="_blank">📅 23:48 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140958">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/L1Emvcunf3WcqJY3chQ59YTpIduq6-C9IUmItQkxERYKesQRGzI55mLdS9acMgO5WySoRHuTlAkf7OIUP1Nist_6PBJLA77oseMN7Bi4F1Su6fH0RmsUMerlVDycvXal45hgRnIZvh1r04t7-_1YORUqkEq_w0cFCt9EUd-Li_ljXZbLHUsFdmTh1caHnBkHD-ZrI4eLacmh_OFuX9fIK-IwIHUA4wnfBCV0VWVQz0hlIkBZc1apT-4YuvK-gT57HrfmVwMVu6hw3oXJpYr24MUuLeRvlu58GoZJ5e5jgCTfyakHXA4By3baHSxRcjMNl6hi0qr7WMQGeg6xdQzraQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
⚪️
برترین بازیکنان لیگ برتر تا این لحظه از نظر متریکا
1⃣
⚽️
🔻
علی علیپور 7.7
2⃣
⚽️
🔻
سعادت حردانی 7.49
3⃣
⚽️
🔻
اسماعیل قلی‌زاده 7.49
4⃣
⚽️
🔻
تیبور هلیوبویچ 7.48
5⃣
⚽️
🔻
یاسر آسانی 7.46
6⃣
⚽️
🔻
محمدمهدی محبی 7.45
7⃣
⚽️
🔻
عباس کبیریزی 7.44
8⃣
⚽️
🔻
امیرحسین حسین‌زاده 7.39
9⃣
⚽️
🔻
مجید عیدی 7.37
0⃣
1⃣
⚽️
🔻
امیرمحمد رزاق‌نیا 7.37
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.31K · <a href="https://t.me/SorkhTimes/140958" target="_blank">📅 23:39 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140957">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">✅
حدادی : در یک بازی رسمی از عالیشاه تقدیر میکنیم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.26K · <a href="https://t.me/SorkhTimes/140957" target="_blank">📅 22:28 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140956">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">❌
❌
❌
خبرنگار الجزیره در تهران: به نظر می‌رسد که همه طرف‌ها در حالت آماده‌باش کامل هستند و منتظر هرگونه تحول نظامی هستند.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.29K · <a href="https://t.me/SorkhTimes/140956" target="_blank">📅 22:23 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140955">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">❌
❌
قرارگاه خاتم‌الانبیا: براساس اطلاعاتی که دریافت کردیم، آمریکا قصد دارد دوباره به ایران حمله کند. اگر حمله کند، پاسخ دردناکی می‌دهیم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.22K · <a href="https://t.me/SorkhTimes/140955" target="_blank">📅 22:17 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140954">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">✅
✅
حدادی: قرارداد علی علیپور با پرسپولیس تمدید شد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.31K · <a href="https://t.me/SorkhTimes/140954" target="_blank">📅 22:07 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140953">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">❌
❌
غیبت عالیشاه برابر پرسپولیس/ ستاره سابق سرخ‌ها کجا بود؟
❌
امید عالیشاه در دیدار دوستانه گل‌گهر و پرسپولیس نه در ترکیب تیمش قرار گرفت و نه روی نیمکت نشست.
❌
❌
گویا عالیشاه در ورزشگاه حضور داشته و به دلیل مصدومیت جزئی در رختکن در حال گرفتن ماساژ بوده است. این…</div>
<div class="tg-footer">👁️ 5.2K · <a href="https://t.me/SorkhTimes/140953" target="_blank">📅 22:06 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140952">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">✔️
حدادی : قرارداد همایی فر ۱/۶۰۰ دو سال دیگه هم قرارداد داره فردا قرارداد هرکسو زیاد کنیم باید بریم صدتا نهاد جواب بدیم ، اضافه هم نکنیم بازیکن انگیزه ش از بین میره و راحت می‌تونه فسخ کنه
☹️
☹️
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس …</div>
<div class="tg-footer">👁️ 5.09K · <a href="https://t.me/SorkhTimes/140952" target="_blank">📅 22:04 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140951">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">🎙
🤩
پیمان حدادی: به درستی قهرمان لیگ سال پیش اعلام نشد؛  امسال ۲ همت درآمد خواهیم داشت. خیلی از باشگاه‌ها پول نداشتند. پارسال ۵۶۰ میلیارد درآمد داشتیم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.22K · <a href="https://t.me/SorkhTimes/140951" target="_blank">📅 21:27 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140950">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">👀
❓
چرا خداداد عزیزی منتفی شد؟
🤩
پیمان حدادی: سیاست پرسپولیس و تراکتور فرق دارد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.87K · <a href="https://t.me/SorkhTimes/140950" target="_blank">📅 21:24 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140949">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">🤩
🎙
با اعلام حدادی ساخت ورزشگاه به خاطر نبود ثبات اقتصادی و امنیتی فعلا قابل ساخت نیست
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.75K · <a href="https://t.me/SorkhTimes/140949" target="_blank">📅 21:23 · 12 Mehr 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>

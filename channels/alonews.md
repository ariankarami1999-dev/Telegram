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
<img src="https://cdn4.telesco.pe/file/DMbufwhNWVs3kY7FiJwsPL0X2BHS37_PSpRVEIegdQ4-vah5PTwd60Jo7BJUM3kOUUvZWwzEWfsehRi1krhM2UhcbM7YAvVuJPLNaXoiBA36D6J_GzTFJVkyKkxNpK-ECQnvBRMAxU9MbesR4Y6SjMUBebwVj7ADjPL12um68FQ3u0p6bpO3dcCfddelBo-MHKn_fea__-HMTgvbR5mTbauUwb3lgulNlcrFRxOehSqQdVshzhTI3gRlyvyYv079jyPZxdeYvw4nPI0EAdgEt9DMhv14Fq0iL1uMaan-xytx3QW56RiQxyi5cjJN3I5PsNge08GR41_1PksoyvtJ9g.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 اخبار جنگ الونیوز AloNews</h1>
<p>@alonews • 👥 988K عضو</p>
<a href="https://t.me/alonews" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 با الونیوز از اخبار جنگ و وقایع در چند ثانیه مطلع باش!اخبار جنگ بدون سانسور در الونیوز👌جهت رزرو تبلیغات👇https://t.me/ads_alonewsپشتیبانی کانال🕵️https://t.me/AloNews?directمالک کانال🎩@AloNewsBotX:https://x.com/AloNewsBot</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-12 17:48:11</div>
<hr>

<div class="tg-post" id="msg-139648">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">👈
گزارش ها از شنیده شدن صدای انفجار در دبی امارات
✅
@AloNews</div>
<div class="tg-footer">👁️ 4.09K · <a href="https://t.me/alonews/139648" target="_blank">📅 17:45 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139647">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">👈
آکسیوس به نقل از یک مطلع: نماینده ارشد شورای صلح و مشاور این شورا امروز با نتانیاهو دیدار کرده و به او ابلاغ کردند که باید حملات به غزه متوقف شود.
✅
@AloNews</div>
<div class="tg-footer">👁️ 7.17K · <a href="https://t.me/alonews/139647" target="_blank">📅 17:41 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139646">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">👈
آناتولی: منابع از تصمیم محسن نقوی، وزیر کشور پاکستان، برای سفر به ایران ظرف «یک یا دو روز آینده» خبر داده‌اند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 9.2K · <a href="https://t.me/alonews/139646" target="_blank">📅 17:38 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139645">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/He5_QH6KwS4iAyXNzz5-_SVoDnn7x0r--6yFfdaTnfn-F92lX8tqwpIN3vIxzsg0ytpePynE7ioxbjVigKyd_JRn1yLONeEzMuZMhGJpayxA_m9kjZVOhEyvnVgrYebEqkZNmXc24RrRHJGJc6ly9OdA-9QGw_naDZV-SomHMcpucHMJKo9CBjQsR1tkeZnlmue1XktxhxIIAxgXX0IvYMbPl7Xk2n_y_PQmXlX_iji3sv6ulI3COXlchwldMg_RXWsn00OQfZJe7C77ddsmaBbmtLPt400y1XYDvo93tOeOH9vWak_Ad_KTnRTZ3V-sxOgHDhejucy2hw-TgwhGrg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ترامپ عکس خودشو کنار جورج واشنگتن و آبراهام لینکلن منتشر کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/alonews/139645" target="_blank">📅 17:35 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139644">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/a9F6jQBwjNpMOYeLJQzft1LxmqK4YJllt3LdLWwKj9DIdxw_jVntwy6hw3CN5p7iwfueLlLG_fwp2Epe8DSXoKY_heUrVYtwx9r-vxM1giGERVUk6Jl4u1EVFw_aIBLXDs7sLpVhnuOl9B84c44_ajo_5U2EzpnDbCbG7qa4JWEqzkBwdxlTRNOX63RZI6nXy48nlohZiTYE2Og2jTPuujL0G08QzJ_fBvpx_FABsoTGoC8jl5IcX8CqP1nMQ_8_eC2EHJPw5xylMc3ABjIGpdYubXzHsPKcvRCfe_h80a7UihbnjFyMVxdT0FsBi4bAt_u3yhy2tz0ExpgbjIt4fA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
‏ترامپ
:
شرکت‌های نفتی، قیمت نفت رو برای مصرف‌کنند‌ها پایین بیارید، همین حالا!
✅
@AloNews</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/alonews/139644" target="_blank">📅 17:34 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139643">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">👈
فارن پالیسی: حمله زمینی گسترده به ایران بعید است، اما عملیات محدود همچنان روی میز است
✅
@AloNews</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/alonews/139643" target="_blank">📅 17:33 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139642">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">👈
روزنامه نیویورک پست گزارش داد جیانی اینفانتینو، رئیس فیفا، همزمان با افزایش فشارها برای کناره‌گیری، در پی جلب حمایت دولت دونالد ترامپ است.
🔴
بر اساس این گزارش، اینفانتینو دیدارهای خصوصی با مارکو روبیو، وزیر خارجه آمریکا، برگزار کرده و یک منبع مدعی شده است که این گفت‌وگوها «بیشتر درباره حفظ موقعیت شغلی اوست تا دیپلماسی فوتبال»
✅
@AloNews</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/alonews/139642" target="_blank">📅 17:29 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139641">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">👈
عارف: برنامه‌ای برای قطع اینترنت در صورت بروز تنش یا جنگ وجود ندارد
✅
@AloNews</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/alonews/139641" target="_blank">📅 17:26 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139640">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/g06FrT95fhlK62FjA16x5D0hzoCQbqoTHxseR3L3QbyaSrBZS9MtSfMzF7w0-4xK6g2ClAhKRgpOX_0muIkr07BfcQX8Xv7P6MU3fE0Ps_v8vcW5pM2MtUChy-FVKcujkbSTJH-4ZgoZMM9-XPBgCDwrg7QHfUiP8Sf69qIGGiNyvib-mzDmHLubN77j11SYgSR9kl6i68XBCW-_uvHd1WRYH93rLvU3NBfqJM8ycuBSbNhCzKl791fGofs-xG34ZBvUy3CqNEUdGfzC3tvmtfhAExMYq2Lmj78ziNJhD8C2PhtZ_TrxO1CYaFdJtQcEZw6NE0Qp-E40Yvs67J07xw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
مارک لوین، تحلیلگر نزدیک به ترامپ در فاکس نیوز:
🔴
از اسرائیل حمایت می‌کنم.
🔴
از اوکراین حمایت می‌کنم.
🔴
از تایوان حمایت می‌کنم.
🔴
از مردم ایران حمایت می‌کنم.
✅
@AloNews</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/alonews/139640" target="_blank">📅 17:23 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139639">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vbb6qKOPO5lnurqaYlcnK_vZ_spYc8YNiKvkkBNKi0uY8e671rTxIIUDDtKeCK0rDWS4UTrg0IFslGBvv4BDfVWzOM8z1jmH9k_MOTS8xmjnrvEoSilwcir-21PG5vWpG3tbeWZZSE9-6gcQ9h9EpECHfLyu_gM-74r0VAInvzledvTNNhojSOKKlF7tNIBAlDSg3K_Xnuq_VeNp1GFiIHzCrC2GV3vriKtaebzOKFpLlgWe-ZWSpvvbCU0ZbQA2TVs-6-AslPZbLioZKpKwzZKic3XkSBqYzQ-vPwl0hGdyfNxQOWTHnZQCwfHNLLeMo9htWO9VGOBUkjaF2wQktg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
در تمام ماه جولای ارتش روسیه تنها ۳۰کیلومتر مربع پیشروی رو به جلو داشته است، در حالی‌که ارتش اوکراین در این ماه توانست ۱۳۸کیلومتر مربع از خاک خود در جبهه لیمان، دنیپروپتروفسک و زاپورژیا آزاد کند
✅
@AloNews</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/alonews/139639" target="_blank">📅 17:19 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139638">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RsZmU8dbJq1Jugl5JOcDXbBr28cFXIM44YJeuBTimF25kcKARBNS3uBVksL_rhIz3auo0oUPbRmrGJtvqaEJvRLKGwJYoIY1tsMqlG_NmA3Thk24qgNrKia9EiDXek0ZIt9pfdDyyVqlArFsbyexhcLMWXMmX8HJbaENbiZUZ2Pw8tOoa5TsR7UPs7JfFTzliw5fPCaZyE7NZe0avi4zw0FWeS02wp4MWCLJE2hd-kC2JbU3izRpo2SmBMpWUj7KYRu6Gx03Tw4tVi8n_EckkDT_pnba6DKGPIHSzrkGXGDY5pSmBSuJpZQJ51ThGZuPu6bh9u9MN3rfiQV1sllc5g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ترامپ: آمار واقعی محبوبیت من، نه نظرسنجی‌های ساختگی رسانه‌های جعلی، بهترین نتایجی را نشان می‌دهد که تاکنون داشته‌ام. چرا هم نباید این‌گونه باشد؟ با بزرگ‌ترین کاهش مالیات و بهترین آمار اشتغال در تاریخ، بزرگ‌ترین سرمایه‌گذاری خارجی در تاریخ آمریکا، مرزهایی کاملاً امن، یک پیروزی بزرگ در ونزوئلا، خلع سلاح هسته‌ای ایران، احترام و موفقیتی بی‌سابقه در سراسر جهان و دستاوردهای بسیار دیگر.
🔴
به نظرسنجی‌های جعلی چپ افراطی باور نکنید. آن‌ها فریبکار و فاسد هستند، درست مانند دموکرات‌های فاسد و متقلبی که کشور را نابود می‌کنند.
🔴
برای عظمت آمریکا به جمهوری‌خواهان رأی دهید! از توجه شما به این موضوع سپاسگزارم
✅
@AloNews</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/alonews/139638" target="_blank">📅 17:15 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139637">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">👈
منبع ارشد حماس به الجزیرة: این جنبش با میانجیگران تماس گرفته و خواستار موضع‌گیری صریح در قبال تشدید اخیر تنش‌ها توسط اسرائیل در غزه شده است.
🔴
این جنبش از میانجیگران خواسته است تا مستقیماً مداخله کنند تا اسرائیل را به اجرای آتش‌بس کامل وادار کنند
✅
@AloNews</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/alonews/139637" target="_blank">📅 17:15 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139636">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">👈
سنتکام: نیروهای ما آماده پشتیبانی از کشتی‌های تجاری هستند که مایل به عبور از تنگه هرمز هستند
🔴
سخنگوی فرماندهی مرکزی ایالات متحده : نیروهای ما هوشیار و آماده انجام هرگونه مأموریتی هستند که به آنها محول می‌شود.
🔴
نیروهای ما آماده پشتیبانی از کشتی‌های تجاری هستند که مایل به عبور از تنگه هرمز هستند.
🔴
از ابتدای ماه مه، ما به بیش از هزار کشتی کمک کرده‌ایم تا از تنگه هرمز عبور کنند
✅
@AloNews</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/alonews/139636" target="_blank">📅 17:12 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139635">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PAZR7RfETr0Q1dDGKw1EQXazi72pwxGMGBvuAgTdXkbbqKe919EOEZSMst2hLcbNmwPm6cO5HAXmYgobrrVyM0TXto3ojEUgIYvayRTTKX0B9NNmyVY3SSS058xYbIJnRkyUxDymgArkW9hIIWcCpfXBTBHhmLxIHLB0fRT6UA_eQqLaHpCUcvaEpB00_6QZD3GcvtLT3UROSE3NkXGv1uXCT63k6AUJHCxnvMuX6Li5WhPlc6bKCe9F344IZY-z4ROl4otDVSddBFkFqYq6zKSXYB0YtAmA-tyryehNWljst7w8jV1VrjGSSmZNKHTM3P8ONON0qaTKD7X2CS1MLg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
وزیر صمت عازم پاکستان شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/alonews/139635" target="_blank">📅 17:09 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139634">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/m4NlPtPmMlRiWQi8kYwrx12Vw6YkRXZ23f4-3XWmCidUXHnbQjT0LZwuDi04IpY6ZCnHAohxhojTMfNCaEdhf7tcFFViXSVXjoKTmcRHpEmlwcidOROk9Wkg2iHmCtFvFdtAhieFrGeGzmuHKBH1hJwfLRKg16arE9JtHoX2IxDJFdh70KFWjvKuhnG7SoX9QSzaXMhDM8sL-ic8HbB6rYYitVp5JeAV9rjTQjlMEF5OXE1CGuEY_2wXlZCogGo8AL92fjK_YMMK5FNepMASdSIJoo30_fUFZF0zEnsbjZ77I00O2Son9e9NJqpHZ6YgcIMganQ4uwVv89RXk9maqw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
یک فروند هواپیمای جاسوسی مشترک RC-135W نیروی هوایی ایالات متحده (شماره دم 62-4126) به تازگی از پایگاه نیروی هوایی سلطنتی میلدنهال با شناسه OLIVE26 وارد فرودگاه چانیا در یونان شده است
🔴
این هواپیما از زمان ورود از پایگاه نیروی هوایی آفات در 5 ژوئن در پایگاه نیروی هوایی سلطنتی میلدنهال مستقر بوده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/alonews/139634" target="_blank">📅 17:09 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139633">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">👈
مقامات ارشد پاکستانی:
هیچ مذاکراتی میان ایران و آمریکا تعیین نشده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/alonews/139633" target="_blank">📅 17:07 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139632">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">👈
اسناد شرکت اسرائیلی «البیت سیستمز» فاش کرد که اسرائیل پهپاد‌های استراتژیک و سیستم‌های نظامی پیشرفته ای به امارات فروخته است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/alonews/139632" target="_blank">📅 17:02 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139631">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">👈
داده‌های ردیابی دریایی نشان می‌دهد ۶ نفتکش بزرگ با پرچم عربستان طی روزهای اخیر مسیر خود را در خلیج عدن تغییر داده‌اند.
🔴
این نفتکش‌ها پس از بازگشت از مقصدهای مختلف در آسیا، به‌جای عبور از جنوب دریای سرخ و تنگه باب‌المندب، به سمت جنوب قاره آفریقا حرکت کرده‌اند
✅
@AloNews</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/alonews/139631" target="_blank">📅 16:59 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139630">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">👈
رودا: نیروهای آمریکایی، بریتانیایی، فرانسوی و آلمانی طی ۷۲ ساعته، صدها نیرو و سامانه‌های کلیدی پدافند هوایی خود را از فرودگاه اربیل خارج کرده‌اند
🔴
این اقدام، اقلیم کردستان را در برابر حملات [احتمالی] ایران، به شدت آسیب‌پذیر کرده
🔴
در مدت سه روز، آمریکا هشت سامانه موشکی پاتریوت زمین‌ به هوا را به اردن منتقل کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/alonews/139630" target="_blank">📅 16:53 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139629">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">👈
المیادین به نقل از یک منبع ایرانی: ایالات متحده در موضوع مربوط به بسته ماندن مسیر جنوبی در تنگه هرمز، امتیازی به ایران ارائه کرده است
🔴
ایران در پاسخ به آخرین پیشنهاد آمریکا، با رد این پیشنهاد اعلام کرده است که تا پایان کامل جنگ، تنگه هرمز را باز نخواهد کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/alonews/139629" target="_blank">📅 16:45 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139628">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">👈
وزارت خارجه آمریکا: هیچ برنامه‌ای برای گفت‌وگوی مارکو روبیو با رئیس فیفا وجود ندارد
✅
@AloNews</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/alonews/139628" target="_blank">📅 16:42 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139627">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">👈
سخنگوی کمیسیون امنیت ملی: هیچ گفت‌وگویی درباره پرونده هسته‌ای در جریان نیست
✅
@AloNews</div>
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/alonews/139627" target="_blank">📅 16:41 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139626">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YugMD_g2lVrsi_-mQdRbetk6yJWwURDqUuSmdeVIgyDWQdsb1iBmbDhFfmrgGI9vBV5yO35liRJUEEplp3pizcrlZADmb1to1vPMbR9nNFc2djpP4f1ithXdR0bJeT1FoRHQ1GGW4DZzKdFKLxA6MeiTfORoOIlik_GEbhDJA9OKzFqnKhKeY9vBaVcN1Qbh9HRrJ5oY_bLrtgjKzqMGj6silENkJ8PsxYK6DBej7MS112SvQIp6O_vkXl6vVxHixICdkonqvcDt7wRS2oaZLslsEPLMmfkG6q3FzNc_qWs3cp-eEx7DivWZd7WrTRGmvDHOeN1CqXbTbyUPdXk5dQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
هر 1 گیگ اینترنت که مصرف کنید توسط اپراتور‌ها 2.7 گیگ‌ محاسبه میشه و کسی هم صداش درنمیاد
✅
@AloNews</div>
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/alonews/139626" target="_blank">📅 16:40 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139625">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">👈
بلومبرگ گزارش داد شرکت «نورثروپ گرومن» قراردادهایی به ارزش حداکثر ۳ میلیارد دلار برای تأمین قطعات کلیدی موشک‌های رهگیر ساخت «لاکهید مارتین» امضا کرده است.
🔴
این قراردادها بخشی از برنامه گسترده آمریکا برای افزایش تولید مهمات و موشک‌های رهگیر پس از کاهش ذخایر تسلیحاتی در جریان جنگ ایران عنوان شده است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/alonews/139625" target="_blank">📅 16:40 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139624">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dWUV-YIJ7x0ny_sq_PC0vJN_RBX39vlN57gjfaZfO7Ub4DhSLIkOj5kmmoW3pamu_-pkFPdp6dkortM7HzUiAABLAkWQi0CY6_jSRjy5EiMHfCZIqN8jzB55YKevIkZpnRxmBp-Mht2fvj4YkgQEjMujV53io9QSkCcUDFQo7Fc7yGHbMLFpEBJKkJVCRe40s-NKs9s0C4-8YU7nVW3Rw10rSd3WhnSzKNE5EN_85n-6JPN5rvQtsv-diZOx1Q0UBHfGaEwLsNu_PrqLIiziqWGmfZ2NPdAjmSp_dbY7_0-m9jPvgH5TQqrsyrUMG1fEnpmMd_hN_FpOc8Z-6i4XJQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
با وجود اظهارات پرزیدنت ترامپ مبنی بر آغاز مذاکرات امروز، طبق گزارش آنا‌دولو با استناد به منابع دولتی پاکستان، هنوز تاریخ یا مکانی برای از سرگیری مذاکرات مستقیم میان واشنگتن و تهران نهایی نشده است.
🔴
میانجی‌گران پاکستانی و قطری همچنان در تماس با واشنگتن و تهران برای ترتیب دادن یک نشست هستند و اسلام‌آباد و دوحه از میان مکان‌های احتمالی محسوب می‌شوند. با ادامه تبادل پیام‌ها از طریق میانجی‌گران از سوی هر دو طرف، پیشرفت‌های مثبتی در هفته جاری انتظار می‌رود.
🔴
انتظار می‌رود مذاکرات ابتدا به صورت غیرمستقیم آغاز شده و سپس به مذاکرات مستقیم تبدیل شوند. در مرحله اولیه، تمرکز بر تثبیت توقف فعلی درگیری‌ها و بازگشت به وضعیت پیش از ۹ ژوئیه خواهد بود، نه بر برنامه هسته‌ای ایران.
🔴
اجرای آتش‌بس در جنوب لبنان نیز از جمله موارد اصلی در دستور کار است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/alonews/139624" target="_blank">📅 16:38 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139620">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/WVwEt8FM6PHlXx362ACwvmYAjV4Xuay5hZLpjR-qzYueQuiQnPSK4G7nSL2bBmD1GaMviEFXLNC854htQYQlGQYrAvyGPT8DHOlFid6hU42aSgbUKJgkM8C5r9gfCCQF5FRS_gbaDMZhIy2avmfUER5QIyky8s3ZVFyvhOG-H-8OVrZ4b2H9GoxlqrAR5eSH6S6zW4cM19A1BdmwHRUjtkCSCW7HY3DXzeewpZAsJHCkWj2Bs7bgjNe3r-RMc7mMyBKjtCI2lt3MH8dG82kGF_4wKgZPM_RFT6JY9_yg_mz0q-nBI3A7LSr1cZaOwScQnBCvHcJQwedj8r-k5rL2yQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/D6g480b1TecH2v9KbA_npK-MODXFzA3CtP_poQ4zlXzbgaalpCDoov9ygpPumn2G59FkhblaDvxFV2sn1_D7R93uMbyXX1NNkgBZENXB8KMdBl9A-sY1xp8wrsVtO7f6mUA6nai0MroRYP4zmGV0CA7wgmJ_W1P1nNWjB99X8DjMISf5dxJH5KE1FKV2awDTCkn5DE8jyg5lQK-fIqZ2r4hIlOS2nMseoOjZFaPAtr2bDyrZNX-4W3VTOZpFF4AkGP_y5zcifFqgEHUHZsHI7oMRxk3KHRjF7exLJkjWaRmgIgty74p533hCahrPtw2Tly8niUJo0mVmAIJ5qeZwSg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fb22e4cb2c.mp4?token=rk7aFjymvzeWTFPBXpecf3rgogpxgMgxPAWmnWqDH7fAVA-UX500imfcYANabS116-fMP8IGAnPHyqfiIwoA3A3gswUCkE7V49_TFgtTFAkETqLoI6C0C90xG2bk99I75fmPR_zwwxTtjgnvtJJiUg2e047Zz4eDYaqcuKkyGSGY8ho_oZFYakRnp5T0KwKSwrA65majxYd9_ag2fbY155L06PEPZcRaB1QtEmoGLIpa6sV6bW2XhuySZ-ciX3UKmBGvHyhusNdL2-McJaZIpCXvVv5cwHEnnwf39f2SA2XDUnEFyCAjLqc_ow1KmBhzysfUDmgY9pLo6bzBfTDn2g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fb22e4cb2c.mp4?token=rk7aFjymvzeWTFPBXpecf3rgogpxgMgxPAWmnWqDH7fAVA-UX500imfcYANabS116-fMP8IGAnPHyqfiIwoA3A3gswUCkE7V49_TFgtTFAkETqLoI6C0C90xG2bk99I75fmPR_zwwxTtjgnvtJJiUg2e047Zz4eDYaqcuKkyGSGY8ho_oZFYakRnp5T0KwKSwrA65majxYd9_ag2fbY155L06PEPZcRaB1QtEmoGLIpa6sV6bW2XhuySZ-ciX3UKmBGvHyhusNdL2-McJaZIpCXvVv5cwHEnnwf39f2SA2XDUnEFyCAjLqc_ow1KmBhzysfUDmgY9pLo6bzBfTDn2g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
عباس عراقچی در نجف
✅
@AloNews</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/alonews/139620" target="_blank">📅 16:37 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139619">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromالو توئیت | AloTweet</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6b0c519f38.mp4?token=T1RKuqHbeXG9SCLSUhu-49yuQB-XGhRNVYehXxb9ThOt8EbuahN9a905eUMqIGv5smt-KMrhP1Q68O6OXu4l-Uuxg-1NuKwUN76sUoACuKCNQEcOOznG5Y5RtSnPf9OekLngDegQInBvaA_4DneSW8o_cjuOOYJ4T4SWBYnpz8WMJtcxtVqyQtvQRhUCN4abJjG8cwNNK-q1drWTDfAA92ndYL95LK9ojF2Wojg1dFMnr6xwh428rzmxaKAa8b7_a7I7G1uwYAYSG6niT6VN5kbtFDh2ed-2h2_Y8CHR9DwdlqmWK7a0MfZACEIIIBcY_2kgOwj5SF1IIcdaAbZz3A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6b0c519f38.mp4?token=T1RKuqHbeXG9SCLSUhu-49yuQB-XGhRNVYehXxb9ThOt8EbuahN9a905eUMqIGv5smt-KMrhP1Q68O6OXu4l-Uuxg-1NuKwUN76sUoACuKCNQEcOOznG5Y5RtSnPf9OekLngDegQInBvaA_4DneSW8o_cjuOOYJ4T4SWBYnpz8WMJtcxtVqyQtvQRhUCN4abJjG8cwNNK-q1drWTDfAA92ndYL95LK9ojF2Wojg1dFMnr6xwh428rzmxaKAa8b7_a7I7G1uwYAYSG6niT6VN5kbtFDh2ed-2h2_Y8CHR9DwdlqmWK7a0MfZACEIIIBcY_2kgOwj5SF1IIcdaAbZz3A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">صحبت های «وحیده عظیمی فر» وکیل پایه یک دادگستری؛ در مورد حقوق زنان در ازدواج.
مرد فقط با اجازه همسرش میتونه زن دوم؛ سوم و چهارم بگیره.
حق حضانت فرزند تا ۷ سالگی با مادرشه؛ بعدش هرطور که به صلاحش باشه.
حق طلاق با مرده.
جهیزیه مال زنه.
زن با ازدواج مجدد مستمری شوهر فوت شدش قطع نمیشه.
زن خیانت هم بکنه و حتی خیانتش محرز هم بشه بازم مهریشو میتونه بگیره.
[
@AloTweet
]</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/alonews/139619" target="_blank">📅 16:35 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139618">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">👈
دیده‌بان حقوق بشر: افغانستان همچنان تنها کشور جهان است که در آن دختران پس از پایان دوره ابتدایی (پس از صنف ششم) از آموزش محروم هستند
✅
@AloNews</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/alonews/139618" target="_blank">📅 16:33 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139617">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">👸
شهبانو فرح پهلوی 10 سال قبل از فتنه57 تو بهترین محله پاریس برای دانشجوهای بورسیه شاهنشاهی ایران یک خوابگاه مجلل چند طبقه میسازه
🔴
حالا اعتراض دانشجوهای چپول اونموقع چی بوده؟ باورش سخته اما اعتراض داشتن چرا این خوابگاه بلندتر و زیباتر و باشکوه تر از خوابگاههای کشورهای دیگه اس!
🤔
احمق بودن طرفداری های رژیم جای خودش چون ما میگین اونا از احمق بودنشونه که نمیفهمن ولی چپ نفهم که با بورسیه دولتی برای تحصیل رفتن اروپا و آمریکا از حرام زاده بودنشونه که نمیفهمن یعنی درآمدشون از همینه که نفهمن.
✅
@AloNews</div>
<div class="tg-footer">👁️ 29.1K · <a href="https://t.me/alonews/139617" target="_blank">📅 16:31 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139616">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/71c6686423.mp4?token=HNm4y__Hi0Sf086f2gOdWCenZVCW8J4o6mW9vErSl4xodgQLbgDi7q9vNDq7PGumaMIj98DquGibheJxOecavJAQRHUmH6KbN8z32f5drjS-B9LJS9LzfR4hYDCogCa4lDG3_FYYoCobBi_bgofsb3tp0xLhx8LWg3vs1EoOipua3Sl5-Ab3lwfD_ohHSZeG0xnOPuG8334tCXWI4lNXnj1oU2-0VF4MkjWynEo-m1JbzghPeuzPUoM0Z2rdFscOw2DKX-JTimgMEvsa4KQOC4DlJ4qfV_m50Be83SOVT1W7OLJOzyO8-V1lW48D1Z6tfYGiT8BJo9KGNkigv6o39Kjq2s1isWG_RbkZFgVm_fcCLp3_1fbxpZM75z_S2sA6Df6lW0CjlErZMuo1uoiYZM6TXiPdJ4lE-VLRiTYInmG9ENxuVnVzu3QDDuOHU2azQ7bFwmyDVCXwQeIrHm_dfsFi1v8a6mpzXk2iCwFAUDMZ_eJErz2snfhkpiWVPZMZfJHmPLs1op49z28Trlb4lZWbFIwqSvbW4r9HFqIpE8LKePDOX3zuI2q4gcD_yjM4S5avI5Pf25nOy-HiYNvjyvQqLGuo4q10OvFYDrr-PLGeHhtT_AJ739URFug_8Tyu7wyjU__bpjijcwBVwwceRCulxP2CwNfFz0iitAZgl1c" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/71c6686423.mp4?token=HNm4y__Hi0Sf086f2gOdWCenZVCW8J4o6mW9vErSl4xodgQLbgDi7q9vNDq7PGumaMIj98DquGibheJxOecavJAQRHUmH6KbN8z32f5drjS-B9LJS9LzfR4hYDCogCa4lDG3_FYYoCobBi_bgofsb3tp0xLhx8LWg3vs1EoOipua3Sl5-Ab3lwfD_ohHSZeG0xnOPuG8334tCXWI4lNXnj1oU2-0VF4MkjWynEo-m1JbzghPeuzPUoM0Z2rdFscOw2DKX-JTimgMEvsa4KQOC4DlJ4qfV_m50Be83SOVT1W7OLJOzyO8-V1lW48D1Z6tfYGiT8BJo9KGNkigv6o39Kjq2s1isWG_RbkZFgVm_fcCLp3_1fbxpZM75z_S2sA6Df6lW0CjlErZMuo1uoiYZM6TXiPdJ4lE-VLRiTYInmG9ENxuVnVzu3QDDuOHU2azQ7bFwmyDVCXwQeIrHm_dfsFi1v8a6mpzXk2iCwFAUDMZ_eJErz2snfhkpiWVPZMZfJHmPLs1op49z28Trlb4lZWbFIwqSvbW4r9HFqIpE8LKePDOX3zuI2q4gcD_yjM4S5avI5Pf25nOy-HiYNvjyvQqLGuo4q10OvFYDrr-PLGeHhtT_AJ739URFug_8Tyu7wyjU__bpjijcwBVwwceRCulxP2CwNfFz0iitAZgl1c" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
رئیس‌جمهور سوریه احمد الشرع: عملیات نظامی تنها یک ابزار است، همه چیز نیست.
🔴
وقتی با واقعیتی مانند آنچه سوریه با آن روبرو بوده سر و کار دارید، نیروی نظامی به تنهایی هرگز کافی نیست.
🔴
شما همچنین به یک استراتژی رسانه‌ای نیاز دارید. به افکار عمومی نیاز دارید. به توانایی اداره امور عمومی نیاز دارید. به ساختن نهادهای نیاز دارید. به یک اقتصاد نیاز دارید. باید به وضعیتی از توسعه دست یابید.
✅
@AloNews</div>
<div class="tg-footer">👁️ 30.6K · <a href="https://t.me/alonews/139616" target="_blank">📅 16:21 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139615">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">👈
مجری صدا و سیما: آقای شهید ما میهن پرست ترین رهبر تمام تاریخ ایران هست
✅
@AloNews</div>
<div class="tg-footer">👁️ 31.6K · <a href="https://t.me/alonews/139615" target="_blank">📅 16:17 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139614">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BaYFCvpxy4Uyyf9gkkv6WG0NCoD_SNie4XPBwObyVp00myDtU2g9gAxhoyDVpsadNL4Zw0C9CKbJLo_GV4Fuo3eXhvt7HGaG8VEYSwRAIM2GD9Q27i3U0aY6Qc_02YDu1d2mRxEyCblwvGepQZKiTNZW04BQcgrcdW7BOyVAeKn2DZIKZ52y6a7kGK0XijlOk4tDqYFgQJljEyQ5z9ed74gROn98Sjo0o0McqyYX1QN_Dwam97jVlo7qxNeFe5adYTkv00KPDL2jdF3GYRaQlG-TRgq_ZyfCG7CnAJhRv_NbhFuIcf7zTQHrKWdw-USdYSYdAKIIiwYLPgf8cB3srA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
یه کاربر خارجی توئیت زده که اگه نقشه ایران رو برعکس کنیم شبیه ترامپ‌ میشه
✅
@AloNews</div>
<div class="tg-footer">👁️ 34.7K · <a href="https://t.me/alonews/139614" target="_blank">📅 16:10 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139613">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromالو توئیت | AloTweet</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/725521aa48.mp4?token=oR7pCIxdOiIh7WnxUJPVvHHnQYr-nCyOqlPj2Jw5BnBH2Ttt5XOR2IgNFcOz7_pzh3sI0zu7xN3PEo9iI2eWNZryAQhYLxwj-MkABOrVCG3sITbsvxjsVLb3v1vwGrv4GyVGIaEBlu9f94S0VefmvvPsEqGx9cLtdBVnmB3TugJ3vN5y--WsqsSaOZw1GGnwWkDbm1ltTEaKlUEZcjedF9BAJJ23RX_K08iJrPpJ7R9zGChSczqhtJl1yUvQXV7gWb_u1mfyXAPEy3sPQNL05Ur3jbBlLaI4pMwHZp7vXLrh7RnnuYi4gcjHwk2-QI3ryd291kmIzqJOkCqw6wMb5w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/725521aa48.mp4?token=oR7pCIxdOiIh7WnxUJPVvHHnQYr-nCyOqlPj2Jw5BnBH2Ttt5XOR2IgNFcOz7_pzh3sI0zu7xN3PEo9iI2eWNZryAQhYLxwj-MkABOrVCG3sITbsvxjsVLb3v1vwGrv4GyVGIaEBlu9f94S0VefmvvPsEqGx9cLtdBVnmB3TugJ3vN5y--WsqsSaOZw1GGnwWkDbm1ltTEaKlUEZcjedF9BAJJ23RX_K08iJrPpJ7R9zGChSczqhtJl1yUvQXV7gWb_u1mfyXAPEy3sPQNL05Ur3jbBlLaI4pMwHZp7vXLrh7RnnuYi4gcjHwk2-QI3ryd291kmIzqJOkCqw6wMb5w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جوان ایرانی
💔
[
@AloTweet
]</div>
<div class="tg-footer">👁️ 35.7K · <a href="https://t.me/alonews/139613" target="_blank">📅 16:06 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139612">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">👈
هاآرتص: اسناد افشاشده نشان می‌دهد اسرائیل پهپادهای راهبردی و سامانه‌های نظامی بسیار پیشرفته‌ای را به امارات فروخته است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 36.8K · <a href="https://t.me/alonews/139612" target="_blank">📅 15:59 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139611">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qU1i3hNrj1uhAz41MeAsfrcuKBBSCkL1_GNywd1CTEMDtAhsfs9-7CdWlYEyeeRrSvCVDSNZMpSBKcWUmexj1v3rW3aF7TzbDOmZcI8LKSbgCM3ShZO2VeGGAJ4yYsCWV0pN7jy1okve7WQtooSYJyTa9kqgDvljl6w58wSX57oqEFZdMT9zNNdWnTUBPfKW-aZNSNvHzhtGL3wueOKUd15XT51r2pdhezvYtexn-VJ3XTIxMH0cmDYBmPJ_foZt9Pyr_XnEEKTGv61BZjzBgV1rGaUkqt0g4pzViSg1AlMlcLSOCYQ0LwHPVT9P4W8Gvb02XhalVWYaWWBEIpxaxg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
صادق زیباکلام:
صحبت و بحث با بسیجی‌ها مثل کوبیدن میخ تو سنگه
✅
@AloNews</div>
<div class="tg-footer">👁️ 39.8K · <a href="https://t.me/alonews/139611" target="_blank">📅 15:55 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139610">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">👈
سخنگوی کمیسیون امنیت ملی مجلس:
حمله زمینی از کردستان یکی از برنامه‌های «موساد» و «سی‌آی‌ای» است و تحرکاتی وجود دارد، اما ما اطلاعات استخباراتی خوبی داریم.
✅
@AloNews</div>
<div class="tg-footer">👁️ 39.8K · <a href="https://t.me/alonews/139610" target="_blank">📅 15:48 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139609">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ocZPYWu6xzi_Xc6DCSSgNSgvtSc3aTBexsSWs3K94hNKfayvnKy-oaaLVVKc5ctBubikYVLBT89sToH7bqyAimrzN2kOndhGG91ucyOLCjJAwSrQlHBvP1NeFzrZE67zKDybUeJxtrgU442TVcBjzZoTY51oupTrx2mbm9QvpxDtS5fwYPqMnidZloWuFNge9WTNikgFBzvPJ7f_VptzmvTxYgiIJCwAKSXvtPNhrYjwJtlvS2lM5Em1gapPZSW70UlYtSGH4KNoElgbiTiH5gdA08KfB2Q1Yi_10LZJ_NVPbB1pyYRllrfgBo6AU-hmKjuBV481-yLxrr2zflD00g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
پوردهقان
،
عضوکمیسیون صنایع و معادن مجلس
:
قاچاقچیان برنده اصلی ممنوعیت واردات لوازم خانگی هستند
✅
@AloNews</div>
<div class="tg-footer">👁️ 41.8K · <a href="https://t.me/alonews/139609" target="_blank">📅 15:43 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139608">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/bPEKjeoiw4fYoxJpLHbGWiZk8CsroXEUKnzhWq2Kp5UX5mSliZ3DA6YGjiyiGG9uKS-WXJWTGl_ZWK0k_gpYTqjGXcMIGb2O5XTYDTwrra590IDppHkwQ-ilaP6q6t2SUd8UxMbxOB1nFsYTzLaFXgnv2Nk3-SQNgWUBz42xx4lLCsGNAqfTLj0ghi8DZaBCqFS4TLRRKVKlmmbcHXUE0wmS-JoYsMzE45hbXbH2mb9QZ7pHt9cd34zLTpDaVJ0CkGVpt9okeYuZqFzvD3ihxdR1pOY_lm_Ds6z1LpZyahZQMh-L4jZzrW6K-Z0YbUE3UpN112_IWpXo2mukYnvR2Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
خبر بد برای تینیجرها
🔴
امیر و رهام، خواننده‌های گروه ماکان بند از هم جدا شدن و این گروه منحل شد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 43.9K · <a href="https://t.me/alonews/139608" target="_blank">📅 15:35 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139607">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fVcWO-geff3hHWWbExUEdkD7cRlIAsEFoFy9Fe9_DlNPcWUbYe4y2D9wA9-iv9Th5LNmymVPZYCwkKFRCY4ISRDX0z5bqtreVW9Sv1N5ey-nfIg5MtIu0QO-r9isWcX7bOJL8mKjebI-VtfIkpkCp2mG02r9ILyrg2y9gCAqdS_xpW5nbgXJmJ3LD7J1Rh2x-26Qgz364VMt-_v2QRH_fdNUcKP5PKUrMNTwRk55CcMNSfmypXQwmFiyscpqYQHX1IUWHYjalE9sq0GfaYhNxKnvXY1skUHN-LIYysw3rFMbybY46heG2ZVO41muPmwZpX2yn8rJkkQNdHqQL0Xq2A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
جواد ظریف: بسته موندن تنگه هرمز، اجماع جهانی با همراهی چین علیه ما ایجاد میکنه.
✅
@AloNews</div>
<div class="tg-footer">👁️ 47K · <a href="https://t.me/alonews/139607" target="_blank">📅 15:20 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139606">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bd3b661bd6.mp4?token=XvH_2RI_s7qAv_-TINP0k2Ad1fQNr5e9zrArXwunqyphlTNJ7icuwDaHJded4UXjBrkN8eZOWQ7_iisKdLWkTN1kW8CwsjIysgRXWDphIpkuu9AiWsc4D8_ikc2v9NPIFT20dNh9Mqyj_eMjFfjO7rd9tDeVOJhu5m2b9eHW_nHeyOXI-wj7_0jYtlkZ_8Mo7RiTqYieheOt1J9ZT7co-dFbRCPuI8BHy5qG0vaL3q9H-oACBcBYPOQLXQHrsd51vOKVdg7DWv3NKiWexsJenwXgiFMb_1oU5pJS7rKpXYIwz9d-UIHZIuYIzcUa2RImxWtulV9pAOFJxfFElov2mA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bd3b661bd6.mp4?token=XvH_2RI_s7qAv_-TINP0k2Ad1fQNr5e9zrArXwunqyphlTNJ7icuwDaHJded4UXjBrkN8eZOWQ7_iisKdLWkTN1kW8CwsjIysgRXWDphIpkuu9AiWsc4D8_ikc2v9NPIFT20dNh9Mqyj_eMjFfjO7rd9tDeVOJhu5m2b9eHW_nHeyOXI-wj7_0jYtlkZ_8Mo7RiTqYieheOt1J9ZT7co-dFbRCPuI8BHy5qG0vaL3q9H-oACBcBYPOQLXQHrsd51vOKVdg7DWv3NKiWexsJenwXgiFMb_1oU5pJS7rKpXYIwz9d-UIHZIuYIzcUa2RImxWtulV9pAOFJxfFElov2mA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
طی سرکوب اغتشاش عده‌ای از طرفداران جمهوری اسلامی مقابل موکب آیت الله سید صادق شیرازی در عراق، 140 نفر بازداشت و 54 نفر مجروح شدن
🔴
حسین ستوده مداح حکومتی لیدر این جریان بوده و سعی داشته امام حسین رو هم سیاسی کنه اما کتک خورده
✅
@AloNews</div>
<div class="tg-footer">👁️ 49.1K · <a href="https://t.me/alonews/139606" target="_blank">📅 15:14 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139605">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/362a14235f.mp4?token=ay8ok6kqUMJvT3uI82indeXeooKD2-r-qVVVHCyGqNUmA0bzlJphRjSKwiXrabuxpoyRkisbIW6JIbhfvs2zIT8XN8ZvkTYhrRxDy4Oo8D6PEzvxOmmKDB38x4jexEf7Rf88kb12HPkLHsLxt5dJbE-r8AcFk1lJ0ju_N-A2oP3J3RsAGNbV4jTfxMswR-TuPdI2gB9E3ewviqh6z7Paw5JOE91v-ducR4wIsVLGAnZ5SOSBbxrkdtfb3AsqjFlsX_-s0BUUZioceDkRlITOUUl1uFu_hnMgMI45HqSfBaqkuEdminRDbNf_uAb21TKLC4-EoEMYqOsA-JddxDihfA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/362a14235f.mp4?token=ay8ok6kqUMJvT3uI82indeXeooKD2-r-qVVVHCyGqNUmA0bzlJphRjSKwiXrabuxpoyRkisbIW6JIbhfvs2zIT8XN8ZvkTYhrRxDy4Oo8D6PEzvxOmmKDB38x4jexEf7Rf88kb12HPkLHsLxt5dJbE-r8AcFk1lJ0ju_N-A2oP3J3RsAGNbV4jTfxMswR-TuPdI2gB9E3ewviqh6z7Paw5JOE91v-ducR4wIsVLGAnZ5SOSBbxrkdtfb3AsqjFlsX_-s0BUUZioceDkRlITOUUl1uFu_hnMgMI45HqSfBaqkuEdminRDbNf_uAb21TKLC4-EoEMYqOsA-JddxDihfA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ویدیویی پر بازدید از زیارت کربلا
✅
@AloNews</div>
<div class="tg-footer">👁️ 47K · <a href="https://t.me/alonews/139605" target="_blank">📅 15:11 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139604">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Olst-WB3XK3SKr_wtGWPtriLpbaegJ4pyFK1womdVFEapC3j9vYhAOeshepyUYPWtJhioeOa3A3kQZICP1lsDGLBGs08gn0hikN-0lo6rGmzzwFyluc9G7FWlPSwFxvhZncgzKv3R0BmGdH5_uFxQ2PCmBSdZfD5B0iSNHcmpSWWi6jojoImxpgfKZvFlcghHmwibgs_Llsij0a435MoMLzy9fg-86bnIZpeWti0ieqi21AyOlcX8KQoOzJlGVRMuTAVxI4VsXZEeuxcmb44NFXW-P0jbdwnnCeqz--MBYUO38svqtLyRMLWp_Lx4ONGw6naDRCnresF2bN3PqQYCA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
شهبازی: اینکه میبینم یه عده تروریست اعدام میشن برام از خوردن عسل شیرین‌تره
✅
@AloNews</div>
<div class="tg-footer">👁️ 48K · <a href="https://t.me/alonews/139604" target="_blank">📅 15:04 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139603">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">👈
وزیر دفاع اسرائیل، کاتز، با اعلامیه‌ای که در تلویزیون پخش شد، سردرگمی ایجاد کرد. او قصد داشت ژنرال آوی بلوت، فرمانده ستاد مرکزی نیروهای دفاعی اسرائیل (IDF)، را با ژنرال ددو بار کالیفا جایگزین کند و بلوت را به اتخاذ مواضع بیش از حد تند علیه شهروندان یهودی مهاجر و تضعیف سیاست‌های دولت متهم کرد.
🔴
نیروهای دفاعی اسرائیل (IDF) به سرعت به این خبر واکنش نشان دادند و اعلام کردند که این اقدام بدون هماهنگی با رئیس ستاد مشترک، ژنرال ایال زامیر، انجام شده است و بلوت در سمت خود باقی خواهد ماند، زیرا وزیر دفاع اختیار قانونی برای اخراج یک‌جانبه افسران ارشد ارتش را ندارد.
🔴
کاتز بعداً تلاش کرد تا از این رسوایی فرار کند و ادعا کرد که او درخواست اخراج بلوت را مطرح نکرده است و هر ادعایی مبنی بر خلاف این، "یک دروغ کامل" و "بخشی از یک کمپین سیاسی است که علیه دولت سازماندهی شده است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 48K · <a href="https://t.me/alonews/139603" target="_blank">📅 15:00 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139602">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/aa3b6f35fd.mp4?token=QbSFUVPvzXOUcFEtG-Kg2z8307XZ21kXw8erJGSFvPoWGQr8pMLuPg9pyaWho2mW0xci3wX8oaowsVdkV18Ic7FTUQ0e-jdtdPoVEhnNzUyRWiF3vV_ZQXeCmL0jIs6JwPbbSA_34_qoC_ySggn0AclUM5pnwcuG6sxkkxhvlZ_FLV4l1YaFamwWKy_uzeI_XVNkNg5mnt46pK2ctDBk92nQMyczfEcUU_C5pC3oTV0YdZsjgo0xNuN2WxMIwWff9Ly9O7JEwJXPKKz7LD3_Ab3pintdsJJ6wCGwjXcLWbreWc-_FvCtZXWJdoLcYz1KNA3GSAcwNjZNuEINcJysVg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aa3b6f35fd.mp4?token=QbSFUVPvzXOUcFEtG-Kg2z8307XZ21kXw8erJGSFvPoWGQr8pMLuPg9pyaWho2mW0xci3wX8oaowsVdkV18Ic7FTUQ0e-jdtdPoVEhnNzUyRWiF3vV_ZQXeCmL0jIs6JwPbbSA_34_qoC_ySggn0AclUM5pnwcuG6sxkkxhvlZ_FLV4l1YaFamwWKy_uzeI_XVNkNg5mnt46pK2ctDBk92nQMyczfEcUU_C5pC3oTV0YdZsjgo0xNuN2WxMIwWff9Ly9O7JEwJXPKKz7LD3_Ab3pintdsJJ6wCGwjXcLWbreWc-_FvCtZXWJdoLcYz1KNA3GSAcwNjZNuEINcJysVg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
دیدار بارزانی با الجولانی
🔴
نیچروان بارزانی رئیس منطقه کردستان عراق به دمشق سفر و رئیس شورشیان سوری ابو محمد الجولانی دیدار کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 47K · <a href="https://t.me/alonews/139602" target="_blank">📅 14:57 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139601">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">👈
ادارات و بانک‌های قم چهارشنبه تعطیل شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 47K · <a href="https://t.me/alonews/139601" target="_blank">📅 14:52 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139600">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5a3c9d3e6e.mp4?token=e_p9aGTZNckRWbPOWFwzMgO1v6EEwnv6P6wWrzWcsEBAGQpXBeaeY72n6dOAXbQoUJ8HP4Ms5EIEIpYFR2dJiZVIrM1DaI7FnMxu3DSXi6ljmoZ7LTXH2hFnPZG4WpnHtBTjbuYMuXDb0aeHMAg6tcrk5P8WCMCWJdKtRHoOiuwEh3FuMrmsE-592zOKKgP2f2kNw_ZUvn4ZtP5HSwbpmCjxJSKljkAfa8bH2eTVI0vcU8ZGgxBaDAQeXoAdcjQekAldgjRJrBFZzKEes6S5oj9C168NnKVm9J3SFFdpEYHzGXTnK8mbfz2Ix87IJoPm5oKlameAT69zhKe0_YFmdQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5a3c9d3e6e.mp4?token=e_p9aGTZNckRWbPOWFwzMgO1v6EEwnv6P6wWrzWcsEBAGQpXBeaeY72n6dOAXbQoUJ8HP4Ms5EIEIpYFR2dJiZVIrM1DaI7FnMxu3DSXi6ljmoZ7LTXH2hFnPZG4WpnHtBTjbuYMuXDb0aeHMAg6tcrk5P8WCMCWJdKtRHoOiuwEh3FuMrmsE-592zOKKgP2f2kNw_ZUvn4ZtP5HSwbpmCjxJSKljkAfa8bH2eTVI0vcU8ZGgxBaDAQeXoAdcjQekAldgjRJrBFZzKEes6S5oj9C168NnKVm9J3SFFdpEYHzGXTnK8mbfz2Ix87IJoPm5oKlameAT69zhKe0_YFmdQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
زلنسکی، رئیس‌جمهور اوکراین، اعلام کرد که رستم اومروف به عنوان رئیس سازمان اطلاعات خارجی اوکراین منصوب خواهد شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 50K · <a href="https://t.me/alonews/139600" target="_blank">📅 14:49 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139599">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">👈
منابع العربیه: نیکولای ملادینوف، مدیر شورای صلح، برای بررسی اجرای توافق غزه وارد اسرائیل شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 50K · <a href="https://t.me/alonews/139599" target="_blank">📅 14:42 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139598">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">👈
شبکه سراسری برق کوبا فروپاشید و برق در سراسر کوبا به دلیل نبود سوخت به صورت کامل قطع شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 51.1K · <a href="https://t.me/alonews/139598" target="_blank">📅 14:41 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139597">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">👈
هلی‌برن نیروهای ایرانی در کردستان عراق
🔴
مشاور فرمانده کل ارتش ایران:
نیروهای ویژه ما، 14 عملیات زمینی در شهرهای سلیمانیه و اربیل علیه گروه‌های مسلح مخالف انجام دادند. در این عملیات، تعدادی از افراد این گروه‌ها کشته و تعدادی دیگر دستگیر شدند. تیپ 23 نیز بدون هیچ‌گونه تلفات به پایگاه خود بازگشت.
✅
@AloNews</div>
<div class="tg-footer">👁️ 53.3K · <a href="https://t.me/alonews/139597" target="_blank">📅 14:30 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139596">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">👈
ظریف: امضای یادداشت تفاهم، پنجره‌ای استثنایی را برای دیپلماسی گشوده ‌است
🔴
این فرصت زمان‌دار است؛ اگر ایران در بازه‌های زمانی تعیین شده به توافق نهایی نرسد، بهبود اقتصادی دشوار خواهد بود؛ احتمال حمله مجدد هم پس از انتخابات آمریکا، منتفی نیست
🔴
بسته ماندن طولانی تنگه هرمز، اجماع جهانی را حتی با همراهی چین، علیه ایران خواهد ساخت
✅
@AloNews</div>
<div class="tg-footer">👁️ 52K · <a href="https://t.me/alonews/139596" target="_blank">📅 14:28 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139595">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uVcMLaqe6kkIhRW3J-gbxBltptpOt1_OP84iPFKdToHo8kPGzvyo5MFt4c7A0A94VFzoy4t5Fx8UXnibYAK006CR9QqtVCdq2y6tGjMnRPUXzqPBanyqMk_2NHw3tGhNBgWVa2wexUicrcyfdR9mzy2fSYRo5HTKAgzfnp8QRhmtkdh57eK8MbQpel-gjK8siHvNm1VkZcGnm-BPVXTmQZkPqNiLQo2gEq-eZk5cyyRBAzLkMPeZNHCDxSFLFHT_pvJ8683x_iCETfR6NugU7vCj01iARW_XrE1YHX6BQ6FPhyqto61yX08SpbhxHXai4XEMXc03C2aeBmbmq1sPSA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
بستنی هم قسطی شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 52K · <a href="https://t.me/alonews/139595" target="_blank">📅 14:24 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139594">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jRCJcDpFj61WKM_31drKBc6PPfcDXgQyNYYsE_ussbaiGWGnoYAFt8XUxj_sR47zXA0dRyFW4GTO3MaD8MRytmOcmAdVNIf3EPFs9rjjt828gbG7k8t3HXDB0UwhPpI5Lyq5VZvKm6r3Tcy0YLs5EqEdu4AJ2bTNnSTNcnj8INYD6fzfoMIPUymhwjFOp5r14i83gT_c0tqc4BXDfrltyBxwsFlwwn7i5LYKkufv8JYJTqLTcgSDQ-oF3vYp-H2mLpQD__oFb9y9-WI0J8Dgaa3ui2p0VFUvIPPIm_zjqBxhMiFVRpx4YNnpclxSMX32xOxF2feRmsASoNekpH-6gg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
شبکه CBS در گزارشی نوشت با وجود آنکه دولت دونالد ترامپ خود را «شفاف‌ترین دولت» معرفی می‌کند، تاکنون جزئیات بسیار محدودی درباره جنگ با ایران منتشر شده است
🔴
این گزارش می‌افزاید اطلاعات اندکی درباره روند تصمیم‌گیری، ابعاد عملیات و ارزیابی نتایج این جنگ در اختیار افکار عمومی قرار گرفته است
✅
@AloNews</div>
<div class="tg-footer">👁️ 50K · <a href="https://t.me/alonews/139594" target="_blank">📅 14:20 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139593">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/diJs0Bz18J9PvJWjrAyuZ4qDf1HhzWP0fOq4eS-LiUU909whLuuovd3FbZNj36FYi2RHl8DiQszH_qvejbVGNpaQBMzNkzYcPG4_a7Cbp_w3SOyAheoR_mYJlSI724tyRCLjic8hrxI8J5Y3_htV0pjskgzBbAXlzELOu4tLtkf0Jf1EkNg9dyZ1EV-V1kTB6Rq4iG8J5mGU2fSSvJjtC7zIaX0hlMoH5KaJOlWZLe25o5RDR-H0nZ3MQU-VByWP6siEc3Jg8gErRVCcTz_N3cuAoahc9tpXSs3FmtA6-Ye4jIdbER6p8ci0sa9q9ocpPGg4KsIVh8CdQ3a8JuGxKQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
اسکورت هوایی آمریکا در تنگۀ هرمز
🔴
پایش داده‌های ناوبری هوایی نشان می‌دهد که هواپیماهای پشتیبانی نظامی آمریکا در خلیج‌فارس فعال شده‌اند
✅
@AloNews</div>
<div class="tg-footer">👁️ 48.7K · <a href="https://t.me/alonews/139593" target="_blank">📅 14:17 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139592">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">👈
سفارت آمریکا در بیروت اعلام کرد هنوز کار فنی گسترده‌ای برای تضمین امنیت غیرنظامیان در جنوب لبنان باقی مانده است. میان تدوین توافق لبنان و اسرائیل و اجرای آن تفاوت اساسی وجود دارد و شتاب‌زدگی در اجرای توافق می‌تواند جان غیرنظامیان را به خطر بیندازد. این سفارت خواستار اختصاص زمان کافی برای اجرای مؤثرتر مراحل آزمایشی بعدی شد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 45.9K · <a href="https://t.me/alonews/139592" target="_blank">📅 14:16 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139591">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/57e8b5aa10.mp4?token=ujMf0OHM0cbQU1WAdv3D-e97j1JcWV899C90-8VQ_0sl-xrLOuKnKnWp3IFjLInobmtmaYLlI1Qo7_Dl2grwnmHFJzGv1SmKjquiu0qT1HiHQ0hgeEbegrfOQY8IqMG2ECD2bdeVgbnzFHRPSz1sIND5QJx9Ssk0XLjqZWnkVam0bP69L8NmUARxoCitymAieYEzD9v7-RU1-za3Z1U3_I0-iUmLIJ83zTEUtFkUSDlZUessf0xjNqGOf319toLdfOuKyK-fQc3B7xeLy7aTJuwL5lUflhttDJpSI9M8azmADB-AUOEpfWz64aGBrFVtyOVHhscVXLTfe4Yvpm0MqQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/57e8b5aa10.mp4?token=ujMf0OHM0cbQU1WAdv3D-e97j1JcWV899C90-8VQ_0sl-xrLOuKnKnWp3IFjLInobmtmaYLlI1Qo7_Dl2grwnmHFJzGv1SmKjquiu0qT1HiHQ0hgeEbegrfOQY8IqMG2ECD2bdeVgbnzFHRPSz1sIND5QJx9Ssk0XLjqZWnkVam0bP69L8NmUARxoCitymAieYEzD9v7-RU1-za3Z1U3_I0-iUmLIJ83zTEUtFkUSDlZUessf0xjNqGOf319toLdfOuKyK-fQc3B7xeLy7aTJuwL5lUflhttDJpSI9M8azmADB-AUOEpfWz64aGBrFVtyOVHhscVXLTfe4Yvpm0MqQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
یک پهپاد انتحاری اوکراینی به ساحلی در شهر گِلِندژیک روسیه اصابت کرد و ۴ نفر کشته و ۱۳ نفر مجروح شدن
✅
@AloNews</div>
<div class="tg-footer">👁️ 47.1K · <a href="https://t.me/alonews/139591" target="_blank">📅 14:13 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139590">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">👈
بقائی سخنگوی وزارت خارجه:
در روزهای آینده نه میزبان هیأتی خارجی خواهیم بود و نه برنامه‌ای برای سفر هیأتی از ایران وجود دارد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 46.9K · <a href="https://t.me/alonews/139590" target="_blank">📅 14:03 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139587">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6f1c6e9f40.mp4?token=ufezGQNI2LvZ3eTfg7v6CGherS9h2Z3XIRa5l4J7dHQ8h9Drr3B9t1uzykv2hiAedpUtY3G-EjKQQkNd8Jq2h_4HRf-TxMRsAED-BzQUlkvyDIK7Q-rrLZlllNyeBxGPhwZR1sMKEpwNHsyspHN8NtSnj821KwdCSc1BJlFBUOWGn4TQZHHB1Nc9uXGIz9Vd6xvIQLvvw2ymsGlSE2CE8OJJGqAgaTT3b4JKarGiE-hPwquAjd0TAj9YE8TBhF1EH-NpgXZxa0cqsMU5qhk_fYK2iFK56-V5f9C1iZqKfa0We9aoE0GdncveYRPM6cioWSJBtRPBcQin604M87QNPQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6f1c6e9f40.mp4?token=ufezGQNI2LvZ3eTfg7v6CGherS9h2Z3XIRa5l4J7dHQ8h9Drr3B9t1uzykv2hiAedpUtY3G-EjKQQkNd8Jq2h_4HRf-TxMRsAED-BzQUlkvyDIK7Q-rrLZlllNyeBxGPhwZR1sMKEpwNHsyspHN8NtSnj821KwdCSc1BJlFBUOWGn4TQZHHB1Nc9uXGIz9Vd6xvIQLvvw2ymsGlSE2CE8OJJGqAgaTT3b4JKarGiE-hPwquAjd0TAj9YE8TBhF1EH-NpgXZxa0cqsMU5qhk_fYK2iFK56-V5f9C1iZqKfa0We9aoE0GdncveYRPM6cioWSJBtRPBcQin604M87QNPQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
حمله پهپادی اوکراین به یه مرکز لجستیکی دیگه تو روسیه
🔴
اوکراین با پهپادهای انتحاری یک مرکز لجستیکی تو منطقه ولادیمیر روسیه رو هدف قرار داد
🔴
این مرکز که حدود ۱۷۰ هزار متر مربع مساحت داره، کاملاً آتیش گرفته و خسارتش می‌تونه بسیار سنگین باشه
✅
@AloNews</div>
<div class="tg-footer">👁️ 48K · <a href="https://t.me/alonews/139587" target="_blank">📅 13:58 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139586">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/osiZMV1WEeq4Yl9lBXCKl33WPvjkrSRb6hrnIWv9Zmt0O90-DYooFO7GtlnVOOlyy72fwhRg7FuU5nCrX17JEk8Kv4wrXzmp4C8-cVm6ScWBXglKb643D_qxkWJx3h4gdeQCMJ4kUGYKafaHpESiqkCki3PK5BMK8fCWDIshEKj394UyIaEF8yskJeS-9OZpDxOSIo5nzit42K26xRkIYx4hP9294Zi-us_WBFrdhGFVt7e8-hwIlk0i2uXJzTgtXUALKV2Iz9JH6lnjaDNKkKVkCuqNlvTOKyyf9Wl4QxC0wSTQsGprg2knct-ewuVH6L9w9sucJgnIkTSG2UP5qQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
رده بندی باهوش ترین کشور ها آپدیت شد و مردم ایران تو جایگاه چهارم باهوش ترین مردم دنیا قرار گرفتن
✅
@AloNews</div>
<div class="tg-footer">👁️ 48K · <a href="https://t.me/alonews/139586" target="_blank">📅 13:56 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139585">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">👈
فرماندار خوسف:  صبح امروز یک کارگر ۳۶ ساله در تونل معدن قلعه‌زری بین مینی‌لودر و واگن حمل مواد معدنی گرفتار شد و جان باخت.
🔴
هیچ انفجاری در معدن رخ نداده و اخبار منتشرشده در این‌باره صحت ندارد
✅
@AloNews</div>
<div class="tg-footer">👁️ 44.9K · <a href="https://t.me/alonews/139585" target="_blank">📅 13:56 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139584">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sxTHFmJf1mqOP9EbIDtcc1qxLfTCpNauKIF0pUB9eFJ3TdcDy2ljV0bDZwwojlSCITKOEmD3sWsvVIpxhCC_JvGsxEzinZelS7UVtyvhWpiXtdvd2ixwXaaC8gQQx-E17c3Xae3Yk14WaF80ry8HR9W-mXvFEv_V3A3taAlWpDL9USjM4TrqMGIwMXuMabbATVrFRSUlZiR6ne3NliWVk6qt7OyOqQk0lNwsJyylY9NrTB4Aj1N1phLy9WYKBQc1kQnqeaDScArnKT_RgkP_CfPNvwk119ypNChxsvVrWDhabYWCsX92DVdYMnaOTDi9fySUde66mHLyPdobUnX-Lg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ذخایر استراتژیک نفت آمریکا (SPR) هفته گذشته ۳.۷ میلیون بشکه دیگر کاهش یافت.
🔴
اکنون حجم این ذخایر به ۳۰۷ میلیون بشکه رسیده که کمترین سطح در ۴۳ سال گذشته است
✅
@AloNews</div>
<div class="tg-footer">👁️ 45.9K · <a href="https://t.me/alonews/139584" target="_blank">📅 13:55 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139583">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">👈
عراقچی، وارد نجف شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 44.9K · <a href="https://t.me/alonews/139583" target="_blank">📅 13:55 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139582">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iBZAuDnDzeDtVz47ISFANODaxjI-ua9EMqHw-HIZbK5i6w-dzTnjG8yWbPfJ6Z5MX-g18TTO-qs3q2ETFz3DVmorGmTG_Ei_gMBA0dBUSU1o_QfmSQsN-MOgppXUOQ_azm_qcwmRFCMQfmsO8aOlBPbY3XEDUjlAWMOVXVKJQGGriWiw9EbZRpJ-qlJWNr4KR8IP3lynJXjCWHAjnRlhW5lqIUulFMiFE9ZYjjvXYkhN-3HaK_enPDAnwas9ZPmdAt-wv81Q-eSZOH4bYisGHfRVq3cuJo7m6rxKYamzXcqRM4aT7MJgizeIe3EUG_VrMDfLmB04PlQ7qL7ksF4xPw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
چجوری به آیندگان بگیم سمت راستی درجهت بقای رژیم حکومت اسلامی تلاش می‌کرد و سمت چپی در جهت آزادی، دموکراسی و جدایی دین از سیاست؟
✅
@AloNews</div>
<div class="tg-footer">👁️ 47.9K · <a href="https://t.me/alonews/139582" target="_blank">📅 13:54 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139581">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">👈
سخنگوی صنعت آب: قطعی برنامه‌ریزی شده آب در دستور کار نیست/ وضعیت منابع آبی کشور به حالت «نرمال» بازگشته
🔴
استان‌هایی مانند تهران و قم، همچنان با کم بارشی مواجه هستند.
🔴
وضعیت آبی مشهد بسیار بحرانی است، به طوری که سد «دوستی» به عنوان منبع اصلی تأمین آب این کلان شهر، تنها ۳ درصد ذخیره دارد
✅
@AloNews</div>
<div class="tg-footer">👁️ 45.9K · <a href="https://t.me/alonews/139581" target="_blank">📅 13:46 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139580">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">👈
مقام‌های اوکراینی، مدیران صنعت پهپاد و کارشناسان امنیت ملی نسبت به فرا رسیدن زمستانی بسیار دشوار ابراز نگرانی کرده‌اند.
🔴
به گزارش CNBC، نگرانی اصلی این است که حملات روسیه به زیرساخت‌های انرژی اوکراین در ماه‌های آینده، سخت‌ترین چالش کی‌یف از زمان آغاز جنگ را رقم بزند
✅
@AloNews</div>
<div class="tg-footer">👁️ 47K · <a href="https://t.me/alonews/139580" target="_blank">📅 13:39 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139579">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/144ba700bd.mp4?token=Uiexov0t93YpheNjjMCaktggZdO0x3j0-aJDsizzpobAW57nbGZikbNG-5z78BCToaJf3BO3lAv2JkIvaqGtZioHCQ4zJ9RDu54qXaUTGwW7jBYuKsxWNoorU8fW0kNfkYt6IiUgu3XmJ8rj2ulPHtda_BAWWF7NGPfwko8IxSv2semgL9NI-HI2rsSl1phteGoj5txUQLVhuLpwhYFtKrkR84uh_RsBQU2IHjjzxXl7fJCssR2V07R81V1ylK8NutwKvRAhi-qEOkT838ODswHIdXtiWLcetg0YmULT-BE9BJ_t2LMtc0zav7v2yEhyozNayOuR3ihZ00r2Y9AWEyEk6FN5XyrN5kkBe8Wxr9lg9WrEYUZQp1PIowLm3ARaF_SSFmvJPhe3rwqyLFNGikLe93xEuGmyw2tcvH9NPCNgegFppvVvMqfGsx9mYAppAmzo5JyBQzP1VXrCfU3fpl7AhaUqhjM_mbCkSnW4Z4slosULjprWLbJEeql2VIOJ-1xuyf8OiEXIrfTkh2Q506vl7jg91dafRdKS2IcZn7rwFOCjiYypfZaURI0jP_gS85OYxDgIUJRxnz07hmPQuyjJ1EYi72YaxEyOCT6pwIs91-vs_XlVi-VOmIVvFgR7P0bqK7GQqFc_nfhuJ3_3GsgafAHuq7qsd_erAT0IFyg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/144ba700bd.mp4?token=Uiexov0t93YpheNjjMCaktggZdO0x3j0-aJDsizzpobAW57nbGZikbNG-5z78BCToaJf3BO3lAv2JkIvaqGtZioHCQ4zJ9RDu54qXaUTGwW7jBYuKsxWNoorU8fW0kNfkYt6IiUgu3XmJ8rj2ulPHtda_BAWWF7NGPfwko8IxSv2semgL9NI-HI2rsSl1phteGoj5txUQLVhuLpwhYFtKrkR84uh_RsBQU2IHjjzxXl7fJCssR2V07R81V1ylK8NutwKvRAhi-qEOkT838ODswHIdXtiWLcetg0YmULT-BE9BJ_t2LMtc0zav7v2yEhyozNayOuR3ihZ00r2Y9AWEyEk6FN5XyrN5kkBe8Wxr9lg9WrEYUZQp1PIowLm3ARaF_SSFmvJPhe3rwqyLFNGikLe93xEuGmyw2tcvH9NPCNgegFppvVvMqfGsx9mYAppAmzo5JyBQzP1VXrCfU3fpl7AhaUqhjM_mbCkSnW4Z4slosULjprWLbJEeql2VIOJ-1xuyf8OiEXIrfTkh2Q506vl7jg91dafRdKS2IcZn7rwFOCjiYypfZaURI0jP_gS85OYxDgIUJRxnz07hmPQuyjJ1EYi72YaxEyOCT6pwIs91-vs_XlVi-VOmIVvFgR7P0bqK7GQqFc_nfhuJ3_3GsgafAHuq7qsd_erAT0IFyg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
محمدرضا باهنر، عضو مجمع تشخیص مصلحت نظام: همه ۸۰ میلیون ایرانی حزب‌اللهی نیستند/ خانمی(دختر شهید سلیمانی) در صداوسیما گفت مملکت متعلق به حزب‌اللهی‌هاست و هر کس ناراحت است برود، در پاسخ به او گفتم شاه هم همین حرف‌ها را زد
✅
@AloNews</div>
<div class="tg-footer">👁️ 49K · <a href="https://t.me/alonews/139579" target="_blank">📅 13:36 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139578">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">👈
وزارت خارجه ترکیه: حملات مرگبار و مداوم اسرائیل به غزه نشان می‌دهد که نتانیاهو قصدی برای برقراری صلح ندارد
🔴
تنها هدف نخست‌وزیر اسرائیل، جلوگیری از صلح و ثبات در منطقه است
🔴
نتانیاهو اقداماتی انجام می‌دهد که توازن شکننده منطقه را تضعیف و تلاش‌های ایالات متحده را تخریب می‌کند
✅
@AloNews</div>
<div class="tg-footer">👁️ 50K · <a href="https://t.me/alonews/139578" target="_blank">📅 13:33 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139577">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">👈
خاویر بلاس، ستون نویس بلومبرگ، مدعی شد عراق عملاً برای هر بشکه نفت بین ۲۵ تا ۲۹ دلار مشوق پرداخت می‌کند تا شرکت‌های کشتیرانی ریسک بارگیری نفت از بنادر این کشور در خلیج فارس و انتقال آن را بپذیرند
🔴
به گفته او، سود بالقوه یک نفتکش غول‌پیکر (VLCC) از چنین محموله‌ای می‌تواند به حدود ۵۰ تا ۵۸ میلیون دلار برسد؛ البته پس از کسر هزینه‌ها و با در نظر گرفتن ریسک‌های امنیتی
✅
@AloNews</div>
<div class="tg-footer">👁️ 52K · <a href="https://t.me/alonews/139577" target="_blank">📅 13:29 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139576">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">👈
تعطیلی ادارات و بانک‌های کرمانشاه در روز چهارشنبه
✅
@AloNews</div>
<div class="tg-footer">👁️ 52K · <a href="https://t.me/alonews/139576" target="_blank">📅 13:19 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139575">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">👈
جان کندی، سناتور جمهوری‌خواه: توافق بد با ایران را نمی‌پذیریم، باید فشار حداکثری را حفظ کنیم؛ تحریم‌ها، محاصره و بمباران کوه کلنگ
✅
@AloNews</div>
<div class="tg-footer">👁️ 54.1K · <a href="https://t.me/alonews/139575" target="_blank">📅 13:07 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139574">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">👈
شاخص کل بورس تهران با رشد ۱۲۳ هزار واحدی در پایان معاملات امروز به ۵ میلیون و ۲۷۷ هزار واحد رسید
✅
@AloNews</div>
<div class="tg-footer">👁️ 55.1K · <a href="https://t.me/alonews/139574" target="_blank">📅 13:06 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139573">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">👈
مجلس خبرگان: با توجه به حوادث اخیر، امضای رئیس جمهور آمریکا فاقد اعتبار است و نمی توان به او اعتماد کرد و امید به توافق با آمریکا راه به جایی نمی برد.
🔴
برای استیفای حقوق ملت ایران فقط باید به نظرات آیت الله مجتبی خامنه‌ای عمل کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 55.1K · <a href="https://t.me/alonews/139573" target="_blank">📅 12:59 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139572">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">👈
گزارش‌ها از شنیده شدن صدای دو انفجار در حومه حمص سوریه
✅
@AloNews</div>
<div class="tg-footer">👁️ 55.1K · <a href="https://t.me/alonews/139572" target="_blank">📅 12:48 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139571">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">👈
جهت رزرو تبلیغات در الونیوز به اینجا مراجعه کنید
⬇️
https://t.me/ads_alonews
https://t.me/ads_alonews</div>
<div class="tg-footer">👁️ 55.1K · <a href="https://t.me/alonews/139571" target="_blank">📅 12:45 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139569">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/36bbe7e0e4.mp4?token=b3SxGKMqJ-ov3zkOtK7zleIj6uOwRyZKdJtDYU8SKH9cYxaAz68c2EPXiem0xpIywD1xFWlSnUtQVVCR8acuCk5_fPyL9l9GNISap7ayl1G_IJVH6NjkeczevVcUWS1aRhcGVl_gwAH4ZljSsls2uDstApykTOY05cpbXOOWcMS_c1Pvfvm4I-LH8D2koVP6drm6b5ICaSe8KCLU77cmHEnfw5WsTAgksfAiuIjqhfQPtEtxDXWNzMoxBGDPzaClQxNLORElDJOFjlu81TtRuuLlxhoOpFdTCoruT-gH_axOCbB0UUKlTO6xbTF3cNKHMMFPA3MVochrZS2zZe5wiQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/36bbe7e0e4.mp4?token=b3SxGKMqJ-ov3zkOtK7zleIj6uOwRyZKdJtDYU8SKH9cYxaAz68c2EPXiem0xpIywD1xFWlSnUtQVVCR8acuCk5_fPyL9l9GNISap7ayl1G_IJVH6NjkeczevVcUWS1aRhcGVl_gwAH4ZljSsls2uDstApykTOY05cpbXOOWcMS_c1Pvfvm4I-LH8D2koVP6drm6b5ICaSe8KCLU77cmHEnfw5WsTAgksfAiuIjqhfQPtEtxDXWNzMoxBGDPzaClQxNLORElDJOFjlu81TtRuuLlxhoOpFdTCoruT-gH_axOCbB0UUKlTO6xbTF3cNKHMMFPA3MVochrZS2zZe5wiQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
مراکشی هایی که وارد اسپانیا شده اند شعار لا اله الا الله و الله اکبر سر دادند
✅
@AloNews</div>
<div class="tg-footer">👁️ 57.2K · <a href="https://t.me/alonews/139569" target="_blank">📅 12:41 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139568">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">👈
تسنیم : هم اکنون رهگیری پهپاد MQ9 بر فراز تنگه هرمز
✅
@AloNews</div>
<div class="tg-footer">👁️ 53.1K · <a href="https://t.me/alonews/139568" target="_blank">📅 12:39 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139567">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">👈
تصاویر ماهواره‌ای و داده‌های ردیابی دریایی نشان می‌دهد که دست‌کم شش نفتکش حامل پرچم سعودی، مسیر خود را از تنگۀ باب‌المندب به‌سمت دماغۀ امید نیک در جنوب آفریقا تغییر داده‌اند تا از حملات نیروهای یمنی در امان بماند
✅
@AloNews</div>
<div class="tg-footer">👁️ 55.1K · <a href="https://t.me/alonews/139567" target="_blank">📅 12:33 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139566">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">👈
میرشایمر: اسرائیل یا باید خلع سلاح شود یا از بین برود، جهان توان تحمل این بار را ندارد
🔴
اگر اسرائیل در جنگ شکست بخورد، ممکن است به ایران حمله هسته‌ای کند مبادا در جهان هیچ دولت یاغی دیگری باقی بماند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 56.2K · <a href="https://t.me/alonews/139566" target="_blank">📅 12:26 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139565">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6c1a662d9f.mp4?token=TUqVVqobv47uKk308-N_R6oc5M6-e5LGXn3o3v4zm-TCRSURtCcgOFlFYcVMWQcuAF_GB8UpM2LB8v7lXFjC7nNl93yR_tIOWIxTaiVjGXUttIiJVx-YVR1Fr6WRKUsF4z9WZQglYhTgYxGU_A4CNvFQ6kPuA9mPUl_xOKkalfdetfIrm9uaVqXg0j_3TaMUDGpAnDBcmoE2v_w-ifTEZVz2OJr7nBKVCcTZBWCpm94p0-jOhYPrrTrPednZ5unTHvKsC6t3Pg7vBrsMicX8m_uizIu6R0PMu4dw8nzIRW2B5Dj5QPQ2T_RjUkwbBq8KLCUp4bhUMO5vUX-P1xrpvQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6c1a662d9f.mp4?token=TUqVVqobv47uKk308-N_R6oc5M6-e5LGXn3o3v4zm-TCRSURtCcgOFlFYcVMWQcuAF_GB8UpM2LB8v7lXFjC7nNl93yR_tIOWIxTaiVjGXUttIiJVx-YVR1Fr6WRKUsF4z9WZQglYhTgYxGU_A4CNvFQ6kPuA9mPUl_xOKkalfdetfIrm9uaVqXg0j_3TaMUDGpAnDBcmoE2v_w-ifTEZVz2OJr7nBKVCcTZBWCpm94p0-jOhYPrrTrPednZ5unTHvKsC6t3Pg7vBrsMicX8m_uizIu6R0PMu4dw8nzIRW2B5Dj5QPQ2T_RjUkwbBq8KLCUp4bhUMO5vUX-P1xrpvQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
پرواز پهپادهای شناسایی اسرائیل بر فراز منطقه ای در کفررمان در جنوب لبنان
✅
@AloNews</div>
<div class="tg-footer">👁️ 56.1K · <a href="https://t.me/alonews/139565" target="_blank">📅 12:20 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139564">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Xf8FpWs5IMxpCdLJAg_eQOwmDkc--0PrubjX3lVZfhA3bG8RK1VxowB5kGEWGWmkYLYs9c0ryjQqAKfckq_wIIvKfOb5q5-Ljwjw0mPldOy_IYjxblO2luzDd2bxAH4uvTda43bohax0Tpl0SGEW7ER4i29apLmxstQ72dzGhh2igI6YscqoUOe1PqOLjRrnLjhBO7Nhe_s915xJi8hs8B10eR-xi2XD-LKxw4XaY3syraPnCiISd1TM7U7DjLOVEXTL0aDf-Nuwd0uXryyZpWhxFTn8ZdAYCjNjRKmTmHhWf-4uO8PbuCPvbp2aFN9CGlq7rhuB41cHDAfMrneL0w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
بانک کپیتال وان اعلام کرده است که در پی بررسی‌های مربوط به قوانین مبارزه با پول‌شویی(AML)، حساب‌های بانکی سازمان ترامپ را بسته است
✅
@AloNews</div>
<div class="tg-footer">👁️ 55.1K · <a href="https://t.me/alonews/139564" target="_blank">📅 12:10 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139563">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">👈
هرمزگان چهارشنبه تعطیل شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 55.1K · <a href="https://t.me/alonews/139563" target="_blank">📅 12:08 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139562">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">👈
یک مقام ارشد سنتکام به استراتژیست های پنتاگون دستور داده تا دنبال یک راه حل خلاقانه و جدید برای فشار آوردن به ایران باشند، چون از نظر آنها، بمباران به عنوان اهرم فشار برای کشاندن ایران به میز مذاکره موفق نبوده
✅
@AloNews</div>
<div class="tg-footer">👁️ 55.1K · <a href="https://t.me/alonews/139562" target="_blank">📅 12:05 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139561">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">👈
سخنگوی وزارت خارجه درباره ائتلاف دریایی عربستان برای باب المندب و پیوستن پاکستان به آن گفت: من نمی‌خواهم در مورد آنچه که تحت عنوان ائتلاف تشکیل شده و قبلا هم درست شده بود و ناکارآمد بود صحبت کنم. مسئله یمن با این چیزها قرار نیست حل شود. ما باید تلاش کنیم ائتلافی برای صلح درست کنیم نه ائتلاف برای آزار رساندن و ایجاد ناامنی در منطقه.
✅
@AloNews</div>
<div class="tg-footer">👁️ 56.1K · <a href="https://t.me/alonews/139561" target="_blank">📅 12:01 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139560">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">👈
فارس: به خاطر بسته بودن تنگه هرمز قیمت گوشت گاو تو آمریکا ۱۲ درصد و مواد غذایی ۴ درصد افزایش یافته
✅
@AloNews</div>
<div class="tg-footer">👁️ 56.2K · <a href="https://t.me/alonews/139560" target="_blank">📅 11:53 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139559">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">👈
سخنگوی وزارت خارجه: ما با کشورهای منطقه همواره در تماس هستیم.
🔴
از همان نخستین روزهای جنگ تحمیلی، به‌صورت منظم در تماس بوده‌ایم
🔴
دانایان منطقه به‌خوبی می‌دانند که امنیت در منطقه تجزیه‌ناپذیر است.
🔴
ناامنی علیه یک کشور منطقه، خواه‌ناخواه به سایر کشورهای منطقه نیز سرایت می‌کند.
🔴
همچنین به‌خوبی دریافته‌اند که حضور نظامی آمریکا ناامن‌ساز و ثبات‌زدا است.
🔴
طبیعتاً همه کسانی که واقعاً صادقانه به دنبال برقراری امنیت هستند، تلاش می‌کنند مانع از تشدید درگیری‌ها شوند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 56.2K · <a href="https://t.me/alonews/139559" target="_blank">📅 11:51 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139558">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">‏
👈
آیا ایران به حمله اوکراین به کشتی ایرانی پاسخ می‌دهد؟
‏
🔴
بقایی، سخنگوی وزارت خارجه: به گفته مقامات اوکراینی این اقدام غیرعمد بود اما شواهد نشان می‌دهد که این حمله عامدانه بوده است.
‏
🔴
هر اقدامی لازم باشد انجام می‌دهیم که هم اوکراین پاسخگو باشد و هم اینکه دیگر این اتفاق نیفتد
✅
@AloNews</div>
<div class="tg-footer">👁️ 55.2K · <a href="https://t.me/alonews/139558" target="_blank">📅 11:48 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139557">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d92447bf90.mp4?token=n36I5vANg78pBOiFUmDzstKKreoj3eW2Rf4ng4athkVS7_CA1fcJpOZ6xzoTOEYjkihs3gsHZuBbPz0vjLaSSdiC8g8Deel3Nudam9tC92D3EBpaK0b9Y3Fd7YYw0EJg3nh66ad1Ywg74hjZeuJNYoQ6rxO7P1RBpROAEAaeRRRSjmv_MAHV3LzoXhUXXq2FxavcXb_f7aC4SzKMYk4lR30g68RWxfVTKRduW0kdjRvXngoaMsQP-bIev_dFsX3avoVR1-YAcD0tcYeJuolWWyC28jWHv3coEW1xKTUlDGMg2VlxvkQoBHzBnIpg_NO7ber0CVNWjFkhm9LjtgKItzRbYIYOuw4x76FZ5B0sMu7jwKJDRrP23nVY_6TzvlxPyAoalShNmPV2LhKeOIyNOeYNPFKCCatzA4sQOTrZ6ANFVseI15qJQEelBANBKpRMFFKRjuusmEBB8Xovy2GZzKc-aHLPQxDuzt-e_28o14CHSkI4ds8AFUSX0XzIcaJqzGZ1vqBk-A-DK6d0awVuNzF1cODIKDgPEfnlOjilksw1lqZELziHpR05pgTEDrFS7yQYnGCDeco8MquaIMWUoASPahqq8pQQDsCMrWtG2VK438qFAw6PbRX4vmGwjApZK_VT0WwGKYONExCuXbM1JdARZBbuf87oh0cEIELVX10" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d92447bf90.mp4?token=n36I5vANg78pBOiFUmDzstKKreoj3eW2Rf4ng4athkVS7_CA1fcJpOZ6xzoTOEYjkihs3gsHZuBbPz0vjLaSSdiC8g8Deel3Nudam9tC92D3EBpaK0b9Y3Fd7YYw0EJg3nh66ad1Ywg74hjZeuJNYoQ6rxO7P1RBpROAEAaeRRRSjmv_MAHV3LzoXhUXXq2FxavcXb_f7aC4SzKMYk4lR30g68RWxfVTKRduW0kdjRvXngoaMsQP-bIev_dFsX3avoVR1-YAcD0tcYeJuolWWyC28jWHv3coEW1xKTUlDGMg2VlxvkQoBHzBnIpg_NO7ber0CVNWjFkhm9LjtgKItzRbYIYOuw4x76FZ5B0sMu7jwKJDRrP23nVY_6TzvlxPyAoalShNmPV2LhKeOIyNOeYNPFKCCatzA4sQOTrZ6ANFVseI15qJQEelBANBKpRMFFKRjuusmEBB8Xovy2GZzKc-aHLPQxDuzt-e_28o14CHSkI4ds8AFUSX0XzIcaJqzGZ1vqBk-A-DK6d0awVuNzF1cODIKDgPEfnlOjilksw1lqZELziHpR05pgTEDrFS7yQYnGCDeco8MquaIMWUoASPahqq8pQQDsCMrWtG2VK438qFAw6PbRX4vmGwjApZK_VT0WwGKYONExCuXbM1JdARZBbuf87oh0cEIELVX10" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
میانجی‌گر جدیدی به میانجیگران موجود اضافه نکرده‌ایم
🔴
بقایی: پاکستان میانجی‌گر ایران و آمریکا است، میانجی‌گر جدیدی از جمله چین اضافه نشده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 55.2K · <a href="https://t.me/alonews/139557" target="_blank">📅 11:41 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139556">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">👈
بقایی: ما الان مذاکره با آمریکا نداریم/ مادامی که نقض عهد آمریکا ادامه دارد وضعیت تنگه هرمز تغییری نخواهد کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 56.2K · <a href="https://t.me/alonews/139556" target="_blank">📅 11:26 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139555">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">👈
بقایی: ما الان مذاکره با آمریکا نداریم/ مادامی که نقض عهد آمریکا ادامه دارد وضعیت تنگه هرمز تغییری نخواهد کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 56.5K · <a href="https://t.me/alonews/139555" target="_blank">📅 11:21 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139554">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">👈
بی حرمتی و اغتشاش حامیان جمهوری اسلامی در کربلا و توهین به آیت الله صادق شیرازی
🔴
پ‌.ن: آیت الله العظمی شیرازی مرجع تقلید شیعیان و مخالف نظام جمهوری اسلامی است
✅
@AloNews</div>
<div class="tg-footer">👁️ 56.2K · <a href="https://t.me/alonews/139554" target="_blank">📅 11:19 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139553">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jfCC51gmvTe_FAv2McM5Z48Dnr8Je3oNvo1TSRiyjA0QzUBdtkjrJ2eLmQdN-mC5NWL-lDVWzS_GJzKuwhayptKeP0JWmeXfbuKIOEHVoqBUXsFPrKebTo_BsgNfHCNJB0LkQG056ayEetA1Vsi0uleraog3WeBk9Vh-zASvgJXkRqVwH91xnZ30E4iNmyMGxtdJQRV4RL18kyO3hNhiLGcz1KRSDZH987YNi1zWBVbvj3IavwpzD7LxQbewK0U2tZj184Xt9iiR3BrHs7GiyXZrRxLDLV4MSPcHv_c7xxlbHH80kg4muwl7w1ErGt8lJjXSBayA3-vjj4g2MMWQFw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
👈
قیمت نفت برنت ۸۲ دلار
✅
@AloNews</div>
<div class="tg-footer">👁️ 56.2K · <a href="https://t.me/alonews/139553" target="_blank">📅 11:12 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139550">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromالو توئیت | AloTweet</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/kcXIEu6j1vvwLrAmijD4Hf9v1pP3zyUkQcYYn3pxLlGZLChF9WEbSLEqqecxmnT15foMRZRFjhPiRehnJffKWFRPQeSPi3zmNMzgfLMYCjBYYsgw-o_RmUqVLFZJGpp9dla-tZHZ-XReuGpkHAHJgpHEA3bII0kV4aAkjrpBkFgOKkcFkBocW5Fv70n2W-ay9QNlJliuX_fhSgoTDL18hG04MH7l7IFqWAd3gXqQEfm7smGGL1NNNXVuykOQA8jcZDjFV61svV-x5K9BeQaIR5kIbZ5ReOOnJXh5ZJJlcHEf13EtRpYGmm3qSxjst7kgigu9aUoVGLk12c2HnOU2vQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jSSfPdcj0UTsNKyAIWXweAS5P_H6nv2VjI-MJzY6EdDgBdJ4VOd3gHl0PSoV9YII0DwdRgCrGHiP8MKJNW1B50WlXNGbUauuHNYCwarZYRXIhFEDfUThBgHjiKysaZ28UUt_WGugpf8myW4A-YS7qsvCc2M_QS1D5OLtRy_2R5ZHw32RvNixbg_RlO4SN9rydZNjcK4RpnegjJZ23xLqJcJcuj2h5p775dXYJkRPqoEmjoHGyeC0joaYpoYr7pV1j-l1V2_l6FCyoD8MMYKM51wkoegfQreZH1cwdvnA_kuETEiD9CFdWeHqGyz6iMSJKaMOOg8CwY_-z2oLIQ3WDA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/YX-y7QmA7fY4ePU2RzbNbRtKAtgIZ6xfGsEGWbp9uloV_VTdShuk4EuIqCek83fh0dxFy6-bapAYQr9JLkggdUTchN7K5vro18CfVXEh6kCO-3NRvzWOj3s5DUT89eKvktayTU_burAVHUFkYY9Fj3h27BmknNmHFbPZ1xHUYNBezDp_rOtMbwsjEeE4M6xwItG9oly-Rg5RYW5P4TzMbTuLO8S0C30DU6U5999AM4TYR8PTJUkN9odwWfi8XJdpNk2czetYc9kDKxz-K5Nhh_9XOZMFQXyDfp6Cgo_S1T9mU-FbX8zVQw-NSEH1WF_iuExbZsmEn8yqKOpOf85i_w.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">داشتم قیمت PS5 و تو دیجی کالا چک میکردم که چشمم خورد به کامنت‌هاش...
[
@AloTweet
]</div>
<div class="tg-footer">👁️ 50.1K · <a href="https://t.me/alonews/139550" target="_blank">📅 11:10 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139549">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">👈
یه سریا همه چیشون شده سیاسی، دین و زندگی و غذا خوردن حتی ریدنشون</div>
<div class="tg-footer">👁️ 51.1K · <a href="https://t.me/alonews/139549" target="_blank">📅 11:08 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139548">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">👈
بی حرمتی و اغتشاش حامیان جمهوری اسلامی در کربلا و توهین به آیت الله صادق شیرازی
🔴
پ‌.ن: آیت الله العظمی شیرازی مرجع تقلید شیعیان و مخالف نظام جمهوری اسلامی است
✅
@AloNews</div>
<div class="tg-footer">👁️ 53.1K · <a href="https://t.me/alonews/139548" target="_blank">📅 11:07 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139547">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">👈
بی حرمتی و اغتشاش حامیان جمهوری اسلامی در کربلا و توهین به آیت الله صادق شیرازی
🔴
پ‌.ن: آیت الله العظمی شیرازی مرجع تقلید شیعیان و مخالف نظام جمهوری اسلامی است
✅
@AloNews</div>
<div class="tg-footer">👁️ 57.2K · <a href="https://t.me/alonews/139547" target="_blank">📅 11:05 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139546">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">👈
سخنگوی وزارت خارجه: مذاکرات با عمان در چند روز گذشته با جدیت ادامه پیدا کرده است
🔴
تماس وزیر خارجه با همتایانش با هدف جلوگیری از تشدید ناامنی و تامین منافع ملی ایران ادامه داشته است
✅
@AloNews</div>
<div class="tg-footer">👁️ 54.1K · <a href="https://t.me/alonews/139546" target="_blank">📅 11:02 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139545">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0d62bba082.mp4?token=O5EwoVuY2T5Zf8Vf2Nqqty3VSDRZkoWlATM4xYNizQMRIXeWDx3prs27cYXAoLbyg5M3OX8b09OWM0hldoHv_RwgfX2tD_yol0lL686_0ra2jKpghTH-WxQbYxuy-yc_2acIDvo9QR4f_A9MAhtE_XjMg7PtG0uzKwpVsmHnaCgyiq9iIe2xvbZjt30ATVooES7II26nm_qUsROIvc_Bf-KvQWRDfUaXQQIMbmRYKR7-oeEf4T3vTk0brb9Md3omYGSzj2JI2XCRWNSurm9UeZ563gI-SRh7ysw0ABORIVqrTaIDygzJWcbhDpD-5v7h1VnxWNiTbjdOnQ6T3enZww" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0d62bba082.mp4?token=O5EwoVuY2T5Zf8Vf2Nqqty3VSDRZkoWlATM4xYNizQMRIXeWDx3prs27cYXAoLbyg5M3OX8b09OWM0hldoHv_RwgfX2tD_yol0lL686_0ra2jKpghTH-WxQbYxuy-yc_2acIDvo9QR4f_A9MAhtE_XjMg7PtG0uzKwpVsmHnaCgyiq9iIe2xvbZjt30ATVooES7II26nm_qUsROIvc_Bf-KvQWRDfUaXQQIMbmRYKR7-oeEf4T3vTk0brb9Md3omYGSzj2JI2XCRWNSurm9UeZ563gI-SRh7ysw0ABORIVqrTaIDygzJWcbhDpD-5v7h1VnxWNiTbjdOnQ6T3enZww" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
بقایی: ‌ در وضعیت تنگه هرمز تغییری خاصی تا زمانی که آمریکا آتش بس و تفاهم نامه را نقض می کند تغییری رخ نخواهد داد
✅
@AloNews</div>
<div class="tg-footer">👁️ 56.1K · <a href="https://t.me/alonews/139545" target="_blank">📅 10:59 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139544">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">👈
احتمال شنیده‌شدن صدای انفجار در اصفهان
✅
@AloNews</div>
<div class="tg-footer">👁️ 55.1K · <a href="https://t.me/alonews/139544" target="_blank">📅 10:50 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139543">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">👈
سناتور روس: مناقشه پیرامون ایران احتمالا تا اوایل 2027 حل و فصل می‌شود
🔴
گریگوری کاراسین رئیس کمیته امور بین‌الملل شورای فدراسیون روسیه گفت، باور ندارم که مناقشه پیرامون ایران سال‌ها طول بکشد، طبق منطق رویدادها فکر می‌کنم این مناقشه تا پایان سال جاری یا تقریبا اوایل سال آینده (2027) حل و فصل شود
✅
@AloNews</div>
<div class="tg-footer">👁️ 59.2K · <a href="https://t.me/alonews/139543" target="_blank">📅 10:45 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139542">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LkG5Y8EbaFN1CDE1X5Wqr5b-VWHG6V0tvSpDko3mHK7gJp2lV9EO9LNbihOJ_KemKImxMtl-XaV5bKBpHKAWi4Tdl9zawfPTfCcBwSJ4RAOs7_Tsndqq11GafphooZHVtUxeha8mbe4GmRvpwlK1Kez7BH4oMUliBIOJLoOh11cp4DEsB42M7DpQDNjmaetibxPUprCK4MZDsI-SHt9QfkTlkP1JfZrGbJEPb4D6X4EXrqbNSsGd_q5jdYHYnLZKaY5hrjaDwG2AZVfnakA_z7rozuIgbcvupBWUPAK6fXv6dJSfni4FfUs_IGNcRgfpHaahocpH0i0Y9nOa-t-pHQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
خط فقر برای یه خانواده ۴ نفره در تهران به ۹۰ میلیون تومن رسیده. این یعنی اگه درآمد کل خانواده از این مبلغ کمتر باشه، زیر خط فقر حساب می‌شن؛ در حالی که حقوق وزارت کار فقط ۱۷ میلیون تومنه.
✅
@AloNews</div>
<div class="tg-footer">👁️ 60.2K · <a href="https://t.me/alonews/139542" target="_blank">📅 10:43 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139541">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">👈
الجزیره: پاکستان و قطر نمایندگانی را برای مذاکرات آمریکا و ایران اعزام خواهند کرد
🔴
تماس‌های عراقچی با مقام‌های پاکستان، عربستان و عراق در شکل‌گیری این روند نقش داشته است
🔴
طبق گزارش الجزیره، هدف این است که روند گفت‌وگوها هرچه سریع‌تر آغاز شود
✅
@AloNews</div>
<div class="tg-footer">👁️ 55.2K · <a href="https://t.me/alonews/139541" target="_blank">📅 10:34 · 12 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>

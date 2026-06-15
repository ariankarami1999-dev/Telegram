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
<img src="https://cdn4.telesco.pe/file/Y0GVVFWNdl89FFHo9uweoVjy62afyaji048Co82SA5r_v5K1oceFpwZNnIbWMZfYk93Mrw9elDWFwmNZnaEH2vRxTC41jIkRO15q9SJxNhi1t3tFhHF2tReBajTCTeq256ZIWhACnnAbJWWZMFuuyV4E7sbpazD82ZeJeJ0cJ9UJ9EwgFKpoRLPFaYecIliP343BryodvU0w5GHZDnb8XjAMvTuy3QMrJTWGlm_0Pqr01NcZBIaIWfIPa-TrdOQ90mqLWF4dvK04b0KAXUWgn821YVhSlPRiUNfNJnu_bUURogb22qy0Rp7AH9g-yVLk1hWSKFbC8tJB_vj0_LMcIQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 [ Fun HipHop ]</h1>
<p>@funhiphop • 👥 171K عضو</p>
<a href="https://t.me/funhiphop" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 «قدیمی ترین اجتماع فانِ هیپ هاپی»🟡صاحب سبک🟡Tb :@FunHipHopAdsContact :@Chaman_Dar_KhakFollowing Copyright Laws©</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-25 12:20:57</div>
<hr>

<div class="tg-post" id="msg-77945">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YULZ0peeYwAwoUztxKTMDyPRiYDtMNNO3mDn3zE8TszjVjUFZOnO6yqOHt1FKOcn-LxQGbH6N1v9GiqkTeyyK1wRlDFgsv2QaHVtiRnWAt5H26fJavZPy6V1RMQPOpst3a9fAXVmlbsiNErTBj3cr6SFtb-_jhgjY6_BTLps1ubkxA4IKOIC3g8L5_8o593L0HziPaDRQE3yrydJ-eruC5kl5iICbJ2YmYec6W554KFg4gZj2rkH29RU8_MuzqhmFgNM2YRW6VzXZ28c_NreC_pIfgf7pXXGKhNLtlThISSb8UfK78ey3gsioKTGtpOmKTuekOXtFUN8-zgXl1o-BQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">میدونستید آپارات چنل یوتوب داره؟
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 1 · <a href="https://t.me/funhiphop/77945" target="_blank">📅 12:22 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77944">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">میترسم حرف بزنم رئال منم بخره</div>
<div class="tg-footer">👁️ 2.12K · <a href="https://t.me/funhiphop/77944" target="_blank">📅 12:05 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77943">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">میترسم حرف بزنم رئال منم بخره</div>
<div class="tg-footer">👁️ 2.45K · <a href="https://t.me/funhiphop/77943" target="_blank">📅 12:03 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77942">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/78832f0cf9.mp4?token=FMgEU-UDfRnYzbUjEWBqdsND66gODvanpCHsDacd3QNAoP4thGRxWYg1gz7mqt7qKwec3jgjcGeLWDgUx4ky0GjeF8pKFTZT2OhQLWGrREnK1KZ7xROHOrDKcrtWYnnScx-IG80VWavU761OKA9Q7McKT_qE31I6P4An70UnE2LIQ6_etK_Dbq4Iarqhr0iWtj57D8t55Lg0t3OtBhXcsS4EiOGsjsiatzBk60UY6nYptsSBNZV72MZpwlKD6aXXaLeUJc4qGuFbFcsSJqgWn8v3SOW34PDcKzofx8UeiMa6a3Fwgty5ol0KuCtOXcndmcPlJCvE8e9h-JwXuVI-sg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/78832f0cf9.mp4?token=FMgEU-UDfRnYzbUjEWBqdsND66gODvanpCHsDacd3QNAoP4thGRxWYg1gz7mqt7qKwec3jgjcGeLWDgUx4ky0GjeF8pKFTZT2OhQLWGrREnK1KZ7xROHOrDKcrtWYnnScx-IG80VWavU761OKA9Q7McKT_qE31I6P4An70UnE2LIQ6_etK_Dbq4Iarqhr0iWtj57D8t55Lg0t3OtBhXcsS4EiOGsjsiatzBk60UY6nYptsSBNZV72MZpwlKD6aXXaLeUJc4qGuFbFcsSJqgWn8v3SOW34PDcKzofx8UeiMa6a3Fwgty5ol0KuCtOXcndmcPlJCvE8e9h-JwXuVI-sg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اول یک قیام خونین رخ میده نتانیاهو و ترامپ وارد جنگ میشن رژیم جمهوری اسلامی رو میارن پای میز مذاکره اورانیوم و موشک و رهبران رو می‌گیرند دو دستگیر و تفرقه بین نظامیان و عرازشه و بعد سقوط با فروریختن رژیم از هویتش اتفاق میفته  - ۸ سال پیش پیش‌بینی های مانوک…</div>
<div class="tg-footer">👁️ 5.01K · <a href="https://t.me/funhiphop/77942" target="_blank">📅 11:11 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77941">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">بلایی که جاستین سر ایلیا آورد :  @FuunHipHop | Jenayi</div>
<div class="tg-footer">👁️ 5.71K · <a href="https://t.me/funhiphop/77941" target="_blank">📅 10:51 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77940">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">دیگه زن مانوکو گاییدین هراتفاقی میوفته یه ربطی بهش میدن</div>
<div class="tg-footer">👁️ 6.23K · <a href="https://t.me/funhiphop/77940" target="_blank">📅 10:44 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77939">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">اول یک قیام خونین رخ میده
نتانیاهو و ترامپ وارد جنگ میشن
رژیم جمهوری اسلامی رو میارن پای میز مذاکره
اورانیوم و موشک و رهبران رو می‌گیرند
دو دستگیر و تفرقه بین نظامیان و عرازشه
و بعد سقوط با فروریختن رژیم از هویتش اتفاق میفته
- ۸ سال پیش
پیش‌بینی های مانوک خدابخشیان.
@FunHipHop
| Constantine</div>
<div class="tg-footer">👁️ 6.76K · <a href="https://t.me/funhiphop/77939" target="_blank">📅 10:42 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77938">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">مانوک ۸ سال پیش در رابطه با قهرمانی یک فرد ۴۰ ساله با لباس نارنجی صحبت کرده بود.
@FunHipHop
| Constantine</div>
<div class="tg-footer">👁️ 6.48K · <a href="https://t.me/funhiphop/77938" target="_blank">📅 10:38 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77937">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZhGZCegdpcVDrSbFG7vc8nbDRd2pCkT2S5AQhddAql1hk4cx9wDgkHUjK6iiiYIho54eFzd6wUecBI-mCOGfAtMvaxzI-C2BmgWN84elRBKg8DjiFodKpqcmUPrIFHnVqu5niKCG4MAsaAldlGwcjHpbZk44_1xEPWqCUK5A08HMAhyJcCON0pH0Vin-jjsQsYyv1pOF7V0pBKiQj_jAsS7tjm5ziwbhs_k1E4ys24YmVJZuvmub9a0wtegrb4vcaZQWSzgMzH374yNeyj5DCBRpBC7RJeTWB638jQShOW9dxgUAomXmc2F5Bjipr0x217CrzeEMXwdABjcUD6P6Kg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بلایی که جاستین سر ایلیا آورد :
@FuunHipHop
| Jenayi</div>
<div class="tg-footer">👁️ 7.13K · <a href="https://t.me/funhiphop/77937" target="_blank">📅 10:30 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77936">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">derbybet.apk</div>
  <div class="tg-doc-extra">52 MB</div>
</div>
<a href="https://t.me/funhiphop/77936" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">📲
اپلیکشن رسمی سایت دربی بت
🌐
DerbyBet.com
💰
امکان شارژ ریالی ، ووچر ، کریپتو در کمترین زمان ممکن
🔥
🆔
@DerbyBet</div>
<div class="tg-footer">👁️ 6.48K · <a href="https://t.me/funhiphop/77936" target="_blank">📅 10:30 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77935">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ok6K4gspj_VgcHebrg5-uBGEHookv0zHmFr_5JhgGaeIHxuQj0MsmFVCHUFZMdZerbrfBqdsYnT_xn-u7sq8GuEwozDGcpgY44mXfOcHCuF89BGr1nN7bBDPpGxZzNJyz7WnFyZwUghHaPQ3L0k-HrWtODDEqaqOi4shZ0iTMHyfg7bYJrrfF1ZSHfjGeMyb3l7PkmZ_BzHPtQNrMHuD6JAy9WYq7D-4lqs15CWukYN-CKShgV3Kn_9kMreEhB5gpW8jtBEGZUUQjAx-TDznZbd1i7Gd_JlylEQ-MMO_HxIAYOcDN6jjIDAkqJ4NOB_sWS75G3PlRQ7TAcS-0MDUxA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
دربی‌بت؛ جایی که پیش‌بینی فقط حدس نیست، شروعِ بردهای واقعیه!
✅
با لایسنس بین‌المللی معتبر، وارد زمینی شو که حرفه‌ای‌ها بازی می‌کنن!
✅
آفرهای خفن ثبت‌نام در دربی‌بت؛ فرصت‌هایی که تکرار نمی‌شن:
⬅️
۱۰۰٪ بونوس اولین واریز؛ شروع انفجاری
⬅️
پشتیبانی کامل از همه ارزهای دیجیتال
⬅️
درگاه ریالی و تومنی امن، سریع
⬅️
برداشت‌های آنی و بدون معطلی
⬅️
پشتیبانی حرفه‌ای ۲۴ ساعته
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _
✅
دربی‌بت؛ بازی کن، ببر، لذت ببر!r25
🅰
✅
https://DerbyBet.com
📩
@Derbybet</div>
<div class="tg-footer">👁️ 6.46K · <a href="https://t.me/funhiphop/77935" target="_blank">📅 10:30 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77934">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oRADQ_ZMlROeaIFYKw6GVCxfBV3imw7kkT7RuWXg5fTpFOjI6TzPNYoIujVarbknEKXqBEm3Coktk7tj5FxuJ-di5bL9BAfz-NOoM6a2PhifvTVmsee7Hx8z4JOFQmtotOQxqVn6qFnvh_zCANRttv7Hcg66A8e--DlGB8ZUfJ5pd7ZZL0Fj3W6M9IYC1cvK8sPiGOMhXQEg378fHkwkeBJ5ZzilzMhuQTTJlj2EIz7RTMh1U7fEc_L5DtkWGQhutu1cQ6ZJRs1OY1csZHNfQwaXmObHaksZd5nCpDJrGxI_EPNwedfUZJYbv_eEwAik2d2Gtz3YoGvw78JzLycVUA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این بنده خدا یجوری داره آب می‌ره که انگار با سیناب رفت و آمد جدی داره.
@FuunHipHop
| Nima</div>
<div class="tg-footer">👁️ 7.88K · <a href="https://t.me/funhiphop/77934" target="_blank">📅 09:45 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77933">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">توپوریا مادرش گاییده شد و تو پایان راند 4 دیگه گفت نمیتونم ادامه بدم
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 9.1K · <a href="https://t.me/funhiphop/77933" target="_blank">📅 08:37 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77932">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">جاستین بنظرم تا نرسیده فرار کن  @FuunHipHop | FaRib</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/funhiphop/77932" target="_blank">📅 08:09 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77931">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JHmilTCF47A_7HXzEFtKoLdEQB0ds5YMbdJ931dyBYVpA0_utFrZDMzliVJn0WRL-mqSV9Oy7flls1GCsp0fJ15BFZtT2BcQZtuzeVf8DGIYLVkpihDGdU9uoJF8wMhWLA9Qp2rPG5rvxgCYStczx8k5WjAnKnzFkt6iPAJGWKTkeBFcJ2xHWsmIL-vVdHaa4roHBWEH06Ai26uH09rUS-9ybDIJ0f4KqkEQ4OPkOwyY5QsHu-T0lU48OFYOjh40S41TgeBzR7h3QT5i_K3QYayqrO7V9sQfqyhAAaLy7QuMfgKVOo6aH-msOJ03nAFu2B2JwBgO7ONhxqdp3m651A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جاستین بنظرم تا نرسیده فرار کن
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/funhiphop/77931" target="_blank">📅 08:04 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77930">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">گوزیدی داداش  @FuunHipHop | FaRib</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/funhiphop/77930" target="_blank">📅 07:56 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77929">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sxyFpZ-t4RIvquFqsdaZOAIncLnGVcLZCZOsYRMwm3fI-W32zo3QEbzXce3isYcnpZ0MZsHO2LMMczZn4fhh-AZuEvAaOACPXtIb7Yqu2hx91YODI5G1WwDLgrCOG4qu_-eW-B1EF3QlJXrSA0xuAMpBBY6LZ_AmrNfhzmvwfB63nMMLNR7jPtHQvgMbjfvet3TCueOvqgjDbfYvM1HXejpRnoos1XJ8UvN5SE8AywWs8JuXD8FDcbQnVP4SWYIf3v-WyIDGz60MHzRw8HLRE_tOAh1K7vzhqIkmk3iiKpwb3HMg0XARO4jMOBxRsy0qxbYutFPd0alMMMCJRtFO1w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">گوزیدی داداش
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/funhiphop/77929" target="_blank">📅 07:52 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77926">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YbnmLfOtuw8SIvln70bC_xWQRpM5-EE7sj_wGVEr6GxfwfBzKicP7QhVGi4I2G3BlL1uskcxNnVrSVZK3-b1NTIydnbJewd5nwPt3q0NrPc4ksUDo-Gd49HKXR795rceFpsfVSoQh-xy0oB1NYAC8NvvvalMdL5dBgyZNEsiJQ-SYY-SPdIRVeQcLxjw7d7NjJWZzSgZK1cra15eiBxKL3SW4S8bEltG619XGks-OjmYmieAE17ZRG-S1ojAIBJi_nNQerC2A3GP6NTOp3E_-wewFlOlbb8fXwrb6-7xavU8qKea7ee8Vs3REzUJzPY-47a7CDITDU-E6Uz17vqYaw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">@FunHipHop
| Constantine</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/funhiphop/77926" target="_blank">📅 03:25 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77925">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">از اینور هم خبرگزاری سوپر معتبر مهر هم شرایط ۱۴ گانه توافق رو از قول خودش منتشر کرد که اونا برا پوشش دادن زیادی خنده دارن خودتون تصور کنید بخندید.  @FunHipHop | Nima</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/funhiphop/77925" target="_blank">📅 02:22 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77924">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">با باز شدن تنگه پس از امضای معامله در روز جمعه</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/funhiphop/77924" target="_blank">📅 02:15 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77923">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SN2FwL2gHGYBBxLkqvsRMeXYDqgjlCh7XBh8CRTdPeOihW9VXxSLTARrzthEP75IUph5myecyTIochkaBZRtP9Ew3uASEBS0zM4DAbb6k7_lb_O7vLjNX97uBQJh4m0NjcGSZ1Cz0Xx08yH8iYSolc2Qq8bnqMp-mGbbnJcOZVM_aMB_bupDichWP6fFqQIerARWVLq91dtt4Ulu0MVqfKjrvz_uYTCrXL0tklwWKKiwZLbM2YhjP12Et2gBkeIjiV8IM2Q8IjZkJW_VPo8yPBM1Ldmvc5ddI3wBG1Lhx-WbH66UVHN_7PFo4XQ-lUiaa_f7IJ91TeXrXJwcv7U3pQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این معامله بزرگ، صلح و امنیت را به کل منطقه خواهد آورد.
بسیاری از رؤسای جمهور تلاش کرده‌اند با ایران صلح کنند و همه قبل از من شکست خورده‌اند. (اوباما به کص ننت خندید)
رهبران منطقه برای اولین بار رئیس‌جمهوری را یافته‌اند که می‌تواند به آن‌ها در دستیابی به صلح واقعی کمک کند. (هنوزم داره می‌خنده خوب به صداش دقت کن)
با باز شدن تنگه پس از امضای معامله در روز جمعه، به منظور پاک‌سازی مین‌ها، نفت دوباره در هر دو انتها برای منطقه و جهان جریان خواهد یافت!
@FuunHipHop
| Nima</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/funhiphop/77923" target="_blank">📅 02:04 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77922">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">فارس: ترامپ در ازای حمله نکردن ایران به اسرائیل، پیشنهاد خروج کامل اسرائیل از لبنان و رفع فوری محاصره دریایی (به جای رفع تدریجی آن) را به ایران داد.  @FuunHipHop | Nima</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/funhiphop/77922" target="_blank">📅 01:47 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77921">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">ویویویویوی خبرگزاری Ynet به نقل از منابع آگاه:  ترامپ به ایران پیشنهاد لغو فوری محاصره دریایی در ازای عدم حمله به اسرائیل را داده است.  @FuunHipHop | Nima</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/funhiphop/77921" target="_blank">📅 01:31 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77920">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5a1eec5a77.mp4?token=MLZPOjWwY0JZccjf5jh7UPNWua1XWw_MjcuaHrtWxHv2KI_fGFSb75QCZmBcZyvS5bfd6d77r1triniKIN5HhhMiME1wohGaQMoXbuNl1Rg7MJNmK-fD2bBZfELRYJ5Q-2WeljfJmh9OwwgcALH6CzitXyc_NR12TkL0d0kekI42c0dY9egq0XYOGl59KoyVgydhOzKFrjXGS9adZnMAIUSSzLRUGXs7kTo7u037HcPaz9TDu-OfjxWkCC0kAdTIK54Ue_LXySWG1EeHL-GsGXmnTeXrlWpIDrjFSt9XPlMgBIxH2HRfDI9lWd-MlvLG5stjPiafPNpU4dmIE-D8Ow" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5a1eec5a77.mp4?token=MLZPOjWwY0JZccjf5jh7UPNWua1XWw_MjcuaHrtWxHv2KI_fGFSb75QCZmBcZyvS5bfd6d77r1triniKIN5HhhMiME1wohGaQMoXbuNl1Rg7MJNmK-fD2bBZfELRYJ5Q-2WeljfJmh9OwwgcALH6CzitXyc_NR12TkL0d0kekI42c0dY9egq0XYOGl59KoyVgydhOzKFrjXGS9adZnMAIUSSzLRUGXs7kTo7u037HcPaz9TDu-OfjxWkCC0kAdTIK54Ue_LXySWG1EeHL-GsGXmnTeXrlWpIDrjFSt9XPlMgBIxH2HRfDI9lWd-MlvLG5stjPiafPNpU4dmIE-D8Ow" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">من هیچگاه علاقه‌ای به تغییر رژیم در ایران نداشته‌ام.</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/funhiphop/77920" target="_blank">📅 01:05 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77919">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">شهباز شریف: به توافق صلح دست یافتیم. جمعه امضاش می‌کنیم. دو طرف اعلام کرده‌اند که عملیات نظامی در تمام جبهه‌ها، از جمله در لبنان، به طور فوری و دائمی متوقف خواهد شد. پس از مذاکرات فشرده، خوشحالیم اعلام کنیم که به توافق صلح بین ایالات متحده آمریکا و جمهوری…</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/funhiphop/77919" target="_blank">📅 01:01 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77918">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">این زیر یکم فوش بدید خودتونو خالی کنید
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/funhiphop/77918" target="_blank">📅 00:59 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77917">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RaReMLNFSysJDaNVr1AjPUP7KcG74_dC_pMYmL68SCea_TnUcC_KXNDbPEhvM010SyiqHrvIQ45ChtNHj1_V8xyP7stry2zCqaDgylWxZPlmm4AO8e3CFhmZNBR9sTzjBPX9omvyaUMG8LU3XUOTuq6eYVf9zq68hN91KLoh5wAp0aw1JCT7v-yia66b51z5CpVOQQQlTw8OUWh31sZ9sAcyVy7E4mVkuPtVuj6vjk1wg2WdoothS2S3_BzWbFM67qZjKUeo3nQfk5pDDt2XMqBLykiU6NUOgDy5YLOoWHeR8mRC2j2Wl0dEJSRLJzu7psBXUZ_OEdKReREfttILfw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شهباز شریف: متن توافق به دست اومده و ما انتظار داریم تفاهم نامه تا ۲۴ ساعت آینده امضا شه و بعد از اون هم یه مذاکرات در سطح فنی برا هفته‌ی آینده داشته باشیم و ممنون از همه‌ی طرف‌ها که به پاکستان فرصت میانجیگری دادن و به امید صلح پایدار.  @FunHipHop | Nima</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/funhiphop/77917" target="_blank">📅 00:49 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77916">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">ژاپن گل مساوی رو زددد
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/funhiphop/77916" target="_blank">📅 00:47 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77915">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">ترامپ چند ساعت پیش به وال استریت ژورنال:  قصد دارم به زودی بیانیه‌ای صادر کند که تأیید یک توافق با ایران است، اگرچه ایران هنوز تأیید نکرده که با شرایط موافقت خواهد کرد. این توافق به صورت الکترونیکی توسط خودم یا جِی‌دی ونس امضا خواهد شد.  @FuunHipHop | Nima</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/funhiphop/77915" target="_blank">📅 00:44 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77914">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">هنوز چیزی امضا نشده کیرم تو چنل هایی که خبر فیک میذارن
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/funhiphop/77914" target="_blank">📅 00:42 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77913">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">گللل هلند زد
فن دایک
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/funhiphop/77913" target="_blank">📅 00:40 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77912">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">ترامپ چند ساعت پیش به وال استریت ژورنال:
قصد دارم به زودی بیانیه‌ای صادر کند که تأیید یک توافق با ایران است،
اگرچه ایران هنوز تأیید نکرده که با شرایط موافقت خواهد کرد.
این توافق به صورت الکترونیکی توسط خودم یا جِی‌دی ونس امضا خواهد شد.
@FuunHipHop
| Nima</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/funhiphop/77912" target="_blank">📅 00:36 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77911">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">توییت جدید وزیر کشور پاکستان:
الله اکبر
@FuunHipHop
| Nima</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/funhiphop/77911" target="_blank">📅 00:30 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77910">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FVS29jKrFhBRAvWnkzMS-69fToPhsO9KgSBnxlSftZubdqp8W224M6UEFOKBSnM19N9hLgGilMHU6DtfG9RofxbktaIcFxb7wjwqeA-X30XXt-Nizcvyzpz0r2nq5K-GI-DK00pjtVeakktpsuLEk5LJ6kgv0ya2CrYeqghgFY1ThXTSopdRQqRbK6NC_4yvhe41u4Bn88PkOAPalPykLSQ8vgDDazTKSbB6hMYmBwM6bE5TOKoTt2MI5emui9hsbKDoXBnUsUdt9fpOfiCgBVf1YHi_HysOb7iEcHVBGw_iksJOjVDCmgthwmFFK-6u3MdhNe2MWnsVXWHFXbMgyg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">از یه جا به بعد جدی جدی داره تمام تلاشش رو می‌کنه شت پست تولید کنه:
ویکتوریا کواتس از بنیاد هریتیج کاملاً فوق‌العاده است! ممنون ویکتوریا. ایران هرگز سلاح هسته‌ای نخواهد داشت و تنگه هرمز به زودی برای کسب‌وکار باز خواهد شد!!!
@FuunHipHop
| Nima</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/funhiphop/77910" target="_blank">📅 00:11 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77909">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d0800033b0.mp4?token=fKUk62lYz1vAbydKx7fyIpeVemdOq0nHPI31nIBETQZbUpDAcnh2cxZaZwD5TBEkLCJ1EjcHIO5MZMzUOKrzatli3ker3zqgkXSLhHrqcm-It30zRJijs4D0vGsJSpBFNjdMHCns6u4rSrFrHfg-EtO2kbDzAxoIGnoQsucGvpspMk3a1VBeXTB4EM0OU75Fdz8KvL-naGW1OKUm-STylLuac8WF6BxI28hBvjFIwTbgPuqUBIppWRySysBnnEBkFYMfIbeNzKXrmwKtEb4P_0kUvJOi_rErB5DeFAlJQfx60Ilicy5zCEQjciKQLIj4UWXI4N3t0nMnYXPREyNYJw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d0800033b0.mp4?token=fKUk62lYz1vAbydKx7fyIpeVemdOq0nHPI31nIBETQZbUpDAcnh2cxZaZwD5TBEkLCJ1EjcHIO5MZMzUOKrzatli3ker3zqgkXSLhHrqcm-It30zRJijs4D0vGsJSpBFNjdMHCns6u4rSrFrHfg-EtO2kbDzAxoIGnoQsucGvpspMk3a1VBeXTB4EM0OU75Fdz8KvL-naGW1OKUm-STylLuac8WF6BxI28hBvjFIwTbgPuqUBIppWRySysBnnEBkFYMfIbeNzKXrmwKtEb4P_0kUvJOi_rErB5DeFAlJQfx60Ilicy5zCEQjciKQLIj4UWXI4N3t0nMnYXPREyNYJw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">واکنش بسیار تند باقرشاه به بعضی کارشکنی‌های بعضی افراد در مسیر مثبت و سازنده‌ی مذاکرات.
@FuunHipHop
| Nima</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/funhiphop/77909" target="_blank">📅 23:58 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77908">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">آدم شخصیت و استایل مربی ژاپن رو میبینه عشق میکنه
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/funhiphop/77908" target="_blank">📅 23:38 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77906">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">کی قراره چنلای فوتبالی تلگرام فارسی از گذاشتن عکس ممه های طرفدارا تیما با کپشن "کاش فلان تیم قهرمان شه" یا "من دیگه طرفدار فلان تیمم" دست بکشن
@FunHipHop
| Menot</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/funhiphop/77906" target="_blank">📅 23:30 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77905">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">ویویویویوی و عجب دنیایی شده پسر کانال ۱۲ اسرائیل: یک مقام ایرانی اعلام کرد که دونالد ترامپ به ایران پیشنهاد پول در ازای سکوت درباره حمله به بیروت داده است. ایران آن را رد کرده و گفت ما خیلی زود پاسخ خواهیم داد.  مقامات ایرانی همچنین تأکید کردند که «ما برعکس…</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/funhiphop/77905" target="_blank">📅 23:28 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77904">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">مگه قرار نبود امروز توافق امضا کنن؟
چیشد پس؟
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/funhiphop/77904" target="_blank">📅 23:25 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77903">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CaGp57U60W5DjXoZjzLUtIJGE3dvsYDWT3NRm9ksQ_KGAJFenlsDEhcJrWG116IcFRbOM0k_BDE8LrsKfRtAqGnwn0B02O5DZR_IqQibRdots4ENe2K3jYHnqX-2F9fyZDkVoODK12JZz0PH57CArHeHZoz4g2Xj7I0P0AhOSGNi03A3UMFDLbyUP0OocAMtIOITnfVFByUmZ9y2SOyBPc_mdQoVO4Uo0CPqLzeWLZ3MZrc7TYvqp73a1E-c3abrov8gX8UBoy4TF6-0usL9bIfHVZkmmgqxLgl6_GkDEh5r1Pq7WC6VnHXldPV0hX-49xd9Me_4XGS2UDLC_KYb0g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خارکسه تابلو
😂
@FunHipHop | Menot</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/funhiphop/77903" target="_blank">📅 23:17 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77902">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eGlWvzhaViUWHc5pxSk1q3SXDeQEeJ4gAFPztWQHwZZsVYU3VtK2e_Bb8mdsPwEsRd0GN1C34EQgKWhzWXL7tKHsoyyEDdICue4BmTA4O48PhYtOqGbnv4omUFgXYOybGSmZempxGXRH4Csgp5xtJ2PclfvFnhAoVjz2FgpKmXR9bvYfTdUM4VO-wFT2rDUelHQvjEnqHmNE3g0Xf_uT8a9-yU7oSGQMOBv1l7PEgrfFlBkRnVqwAi3Hlu2DuRobEx-2RnTdjphzJfZfpcJqFY2xKn-Alhd0Tvz-Rn9CD8q6tiIfbgfSCLF9Cme6TJig-lX7GpzyEVxNsnEAiPfn1A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خارکسه تابلو
😂
@FunHipHop
| Menot</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/funhiphop/77902" target="_blank">📅 23:12 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77901">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">سخنگوی کمیسیون امنیت ملی مجلس در گفتگویی عمیق و تخصصی با شبکه خبر:
هدف اصلی این نظام نابودی رژیم صهیونیستی تا زودتر از 15 سال آینده است.
@FuunHipHop
| Nima</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/funhiphop/77901" target="_blank">📅 22:43 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77900">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/St-P3u9AouNTyAYrrXl-DdIaQukvh6pS6A9VY7O0FcwF2X27lr7uvicmqIzjTmNe1FxZN-_Py_5Gb5hoLcnZd6ZS0W2mLh2bcacPvndDuat-XOFY6R2jaJ3Zmwg6wPsf7JnHo15hdmbvGlTwlgBra9ybV69eTUXJdPIVqm_rR1QkGgPxz7XOP6Nvg4kWYYETKVX91CIXuMo2jfRVaPuY7KFdBASd1MrFRy9-V11B0Et2BOcwDh_ubwtL2qCEtnoZozzb5WLfT3xaxPM9piW9_VxdRfGonRbpDUFUgXWljAPU2iI2fMnsc0aHin4xW3pBITv-lNbxgqr770we8IaQNQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">باقرشاه عصبانیه:
آنها هرگز نمی‌توانند هیچ بخشی از ارکان مقاومت را تک و تنها گیر بیاورند؛
مجاهدت‌های رزمندگان غیور لبنان و
دیپلماسی مقتدرانه جمهوری اسلامی ایران، حاکمیت و تمامیت ارضی لبنان عزیز را تضمین می‌کند
و بساط دیوانه‌بازی و جنگ‌افروزی رژیم اسرائیل را بر هم خواهد زد،
بچرخ تا بچرخیم.
@FuunHipHop
| Nima</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/funhiphop/77900" target="_blank">📅 22:37 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77899">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">هفتمی هم زدن  فشار بخور برزیل فن  @FuunHipHop | Farid</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/funhiphop/77899" target="_blank">📅 22:26 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77898">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">همچین تیمای تخمیی اومدن جام جهانی بعد ژنرال معتقده که تورنمت سخت تر شده
@FuunHipHop
| Farid</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/funhiphop/77898" target="_blank">📅 22:25 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77897">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">هفتمی هم زدن
فشار بخور برزیل فن
@FuunHipHop
| Farid</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/funhiphop/77897" target="_blank">📅 22:22 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77896">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">گللل پنجم آلمان  کاراسائو پاره شد   @FuunHipHop | Farid</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/funhiphop/77896" target="_blank">📅 22:14 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77895">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZL7fwEUrjsM0_ldM3FU9RF5AzaUNuygXkrh_rxDA2u-K59WkTMWOJ_MFlE0_c87U0Osq26JulozofifJw2vRgey5XUHEzR9mjjWU2dLdgw6R9ERu8fNb3VR4tqouYNXMMzXxhoXQeGSHzhDRCobiE2KWcSJrUy-Vl9ydbvSPyrtUyCshcSd060c7MqUH0r5ITONqHrRiicoEmYa45z5i2Iq2GF1fF0sp_-NPLOmtDlIuZOzbSq8uu0hDvemHmiVY1S_amKnAOu6iLVrcc6HPuY874vTQqQBZsfMuI_FkUz-usV0YCYEdkO28yuQFJNpFvd8ZjrTQKzvbeQOwnEqrIw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تقریبا شامپو شد
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/funhiphop/77895" target="_blank">📅 22:11 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77894">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">گللل پنجم آلمان
کاراسائو پاره شد
@FuunHipHop
| Farid</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/funhiphop/77894" target="_blank">📅 22:03 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77893">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">باب اسفنجی امروز زودتر فست فودی رو بست، فک کنم یه خبراییه
@FunHipHop
| Menot</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/funhiphop/77893" target="_blank">📅 21:56 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77892">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">این ترامپ کونکش واقعا ریگان پلاسه</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/funhiphop/77892" target="_blank">📅 21:52 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77891">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">ویویویویوی  کانال ۱۲ اسرائیل: اسرائیل ارزیابی می‌کند که ترامپ به زودی امتیازی به ایران خواهد داد تا در ازای آن ایران به حمله امروز اسرائیل به بیروت پاسخ ندهد. جزئیات نامشخص است، اما مذاکرات پشت‌پرده در جریان است.  @FuunHipHop | Nima</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/funhiphop/77891" target="_blank">📅 21:43 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77890">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">گللل چهارم برای آلمان
جمال
@FuunHipHop
| Farid</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/funhiphop/77890" target="_blank">📅 21:40 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77888">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QrS5zC8sIiBWGkywHvOwBhKUthDBZMr4GNf71OulN7rxZZUkknMXUbEsNkFSy4CJUJJ1GkXO5o8nXUjyyB7jdp6VRnv3Z5m7Mx1bFpAettPwQS65hZrCEFRWSUK_rODapdCuuWMCDcPHlrSlXeTfpYndeJ4UzUnppFQU_rCSES8jOfhVJ2oXrotJN1cOcSjFNwSU4zH9kQpXV1awEMSqoFgO0Fc1Q5gCtrV7WMBHjyA0Z-dumdNZq9KXxquOQyjsO6Ou5Rj4U434d76RnReuFERhrqBXwnGmU1jESLhFoI9qs_4LOptGYz3ZQ34EqgY7gh17jmkS0y-hS-YPj58c1Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bae38bd6df.mp4?token=mLUPD4bXsEFmyNvztCpEqhJYdf6_Z9ZCJWuj_DVXBEuAu1ELrbGmmqRF9J9gQD61iXS4niK_PKqPJlDXYuM_PZSuIkZcPlD6drQZkTreIcrT-qBZ0Uxaeqnxk_zb-tlK5jGDlFTfgjf87JxtNUNlRaH342XdOg2iSBZw0Y9hpPFq1DewVq755GigynDv9N6ESb2jNi3IBs0RM4j_prv4K7d_pI6dFEl1pctqPzNWaNH6bsSI8UpagSNQPvL-AET8rdYwi3UPR_OD3aFY9Os9x2XEpJCHGLdCqL6vUHFGfd-0qP28iue0ks2toL4ruLd1FQQsFIMs3HAl6XN2WYk62A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bae38bd6df.mp4?token=mLUPD4bXsEFmyNvztCpEqhJYdf6_Z9ZCJWuj_DVXBEuAu1ELrbGmmqRF9J9gQD61iXS4niK_PKqPJlDXYuM_PZSuIkZcPlD6drQZkTreIcrT-qBZ0Uxaeqnxk_zb-tlK5jGDlFTfgjf87JxtNUNlRaH342XdOg2iSBZw0Y9hpPFq1DewVq755GigynDv9N6ESb2jNi3IBs0RM4j_prv4K7d_pI6dFEl1pctqPzNWaNH6bsSI8UpagSNQPvL-AET8rdYwi3UPR_OD3aFY9Os9x2XEpJCHGLdCqL6vUHFGfd-0qP28iue0ks2toL4ruLd1FQQsFIMs3HAl6XN2WYk62A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">کسی که به مرد عنکبوتی یمنی میشناختنش رفته وروی صخره حرکت نمایشی اجرا کرد  موقع اجرای نمایش افتاد ته دره و مرد.
@FunHipHop
| Menot</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/funhiphop/77888" target="_blank">📅 21:37 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77887">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">گل سوم آلمان
هاورتز
@FuunHipHop
| Farid</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/funhiphop/77887" target="_blank">📅 21:21 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77886">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">گللل دوم آلمان
@FuunHipHop
| Farid</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/funhiphop/77886" target="_blank">📅 21:10 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77885">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">ویویویویوی
کانال ۱۲ اسرائیل:
اسرائیل ارزیابی می‌کند که ترامپ به زودی امتیازی به ایران خواهد داد تا در ازای آن ایران به حمله امروز اسرائیل به بیروت پاسخ ندهد.
جزئیات نامشخص است، اما مذاکرات پشت‌پرده در جریان است.
@FuunHipHop
| Nima</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/funhiphop/77885" target="_blank">📅 21:02 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77884">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">آلمان خورد
🤣
🤣
@FuunHipHop
| Farid</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/funhiphop/77884" target="_blank">📅 20:53 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77883">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">فرمانده قرارگاه مرکزی خاتم‌الانبیا:
ایده مقدس فتح قدس و اسرائیل و انتقام خون امام شهید هرگز فراموش نخواهد شد؛ ما منتظر کوچک‌ترین لغزش از دشمن متجاوز هستیم تا درس نهایی و فراموش‌نشدنی را به آن‌ها بدهیم.
ما با قاطعیت اعلام می‌کنیم که توانمندی‌های رزمی، دفاعی، موشکی، دریایی، پهپادی و پدافند هوایی ما قوی‌تر از قبل شده و تحت فرمان فرمانده کل قوا، آیت‌الله سید مجتبی حسینی خامنه‌ای؛ خدا سایه‌اش را مستدام بدارد، ارتقا یافته است.
@FuunHipHop
| Nima</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/funhiphop/77883" target="_blank">📅 20:50 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77882">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">آلمان چه تیم خوبی داره احتمال زیاد از گروهی صعود کنن بعد ۱۲ سال
@FuunHipHop
| Farid</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/funhiphop/77882" target="_blank">📅 20:40 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77881">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">پشمااام چه گلی زد آلمان
@FuunHipHop
| Farid</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/funhiphop/77881" target="_blank">📅 20:38 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77880">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">این آخرین نبرده، جلیلی برمیگرده</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/funhiphop/77880" target="_blank">📅 20:22 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77879">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Nt8gYjeaEr91WmvEjOIA3GJlK-g9Fhp552dGWWHTKZqpbaRpqAs_8bfysXTuvu3YE8vs9K02zxkJ7x-uw8m7hz12ny_KGJ46C50y-eXbdjADlhIQGASSWDuFncqbBM61tGvzyTjp1ADIintu_zHvZZPJwKgI8Q_jDfLDMOY0J7DJIfu6OflqPw_d725fBFYp94kqNLUlu_t6gL8dvarhEN0W3Y3WOlvigQlWf1YWDkachyWa9H10tteZDyR1kCLwrxzf2vHmEGe_qbMwuJqJWq0U5a0XgPfesJhN_hQGP7dk3OBHCnTVr7jDFzNkL_m9rU-82oSwfc44QuB4ikhrVw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رئیس کمیسیون امنیت ملی و سیاست خارجی مجلس درمورد میانجیگری ترامپ:
جنایت امروز رژیم صهیونیستی در ضاحیه بیروت بار دیگر ثابت کرد که آمریکا بدون اعتبار ضعیف است، زیرا حتی قادر به کنترل این رژیم غیرقانونی نیست.
پاسخ قوی در راه است.
@FuunHipHop
| Nima</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/funhiphop/77879" target="_blank">📅 20:06 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77878">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">ت‍       :  امضای توافق امروز به صورت الکترونیکی خواهد بود و پس از یک هفته تفاهم نامه به صورت حضوری در اروپا امضا خواهد شد.   @FuunHipHop | Nima</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/funhiphop/77878" target="_blank">📅 19:59 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77877">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">خ در ادامه: قرار بود امروز صبح توافقنامه را امضا کنیم، اما حمله اسرائیل به بیروت آن را به تأخیر انداخت. به نتانیاهو گفتم که هیچ حمله‌ی بیشتری در لبنان انجام ندهد و هشدار دادم که این حملات ممکن است معامله را به خطر بیندازد. اصلا چرا بیبی باید چنین حمله لعنتی‌ای…</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/funhiphop/77877" target="_blank">📅 19:57 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77876">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">تران در ادامه: با وجود حمله اسرائیل به بیروت و تهدید ایران به تلافی توافق امروز نهایی می‌شود. از ایران خواهم خواست پس از حمله اسرائیل به بیروت، با حملات موشکی پاسخ ندهد.  @FuunHipHop | Nima</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/funhiphop/77876" target="_blank">📅 19:49 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77874">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">ترامپ: توافق ظرف دو تا سه ساعت نهایی می‌شود. حزب الله به ناکجا آباد اسرائیل حمله کرده بود و هیچکس آسیب ندید ولی اسرائیل در جواب به بیروت حمله‌ی بزرگی کرد و این مرا به شدت عصبانی کرد. به نتانیاهو زنگ زدم و به او گفتم لعنتی، داری چکار می‌کنی؟  @FuunHipHop |…</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/funhiphop/77874" target="_blank">📅 19:46 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77873">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">ترامپ:
توافق ظرف دو تا سه ساعت نهایی می‌شود.
حزب الله به ناکجا آباد اسرائیل حمله کرده بود و هیچکس آسیب ندید ولی اسرائیل در جواب به بیروت حمله‌ی بزرگی کرد و این مرا به شدت عصبانی کرد.
به نتانیاهو زنگ زدم و به او گفتم لعنتی، داری چکار می‌کنی؟
@FuunHipHop
| Nima</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/funhiphop/77873" target="_blank">📅 19:43 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77872">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">رسمی:
توافق نامه بین ایران و آمریکا توسط ترامپ و علی لاریجانی امضا شد!
پایان جنگ ۲۵ ساله
@Funhiphop
| Farid</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/funhiphop/77872" target="_blank">📅 18:54 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77871">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HSn6eASx7Ka8lhHzgRcZYkTzb8hRiaJi3RseMFWeoa573mlr_4RJLSsUh25WSXmhL8f8msHYWSUA77ESaME-EGYoE8_-hFjPshYgJ2o4b_TVWib3yTgIxRnGV_7SGoXYKP1nYstBSc-Nb27_G7d0jhVvnzB3fZhGK9YY7Sl0NEGKFS-NHBsV0lnTQEH_vM8Nr54RC3b1tkoU8SUIJ62r_WtwxUzQ9uyUh8pRY5iXuiwmkQU6k1z6Ml6BEgIvEHlLvpGXYjQn0Mjf_iK6t_VhJcxsfwJxr2AZpeWomRO8rtLrXArftqb10mFZmzASEFAFANFZux0jfx76glVD0qHQpg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بهش گفتم 90 درصد زیبایی دنیا مال توئه
خندید شد 100 درصد.
@Funhiphop
| Jenayi</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/funhiphop/77871" target="_blank">📅 18:48 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77869">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/dDHa18KWuhb-Cq5HNjBru3gPcvGBCclQB7RuscHkw9R7TNCh1f3dxgaXIiz9CV8InipZAgvQthMpPM6afOlcCIWzPkmRUMsz84LCqMBM4l04drqp4qIs_k2FrnEtiRd0u5GrZd1Ggl-TAl1lkGMH9mEFer0SBYev5UW2EV23Qdw79lIKoBOTFqAq_H6N2Rs3Pi7KjTF4nwOuQtw6r4RisYV9Uzc4NrAWIQP2yYb6RoHoIZH5L5juq-TaAsqUpfg17f64LsD8EI5dy2j6aH0gOfqdmSK7HkLDzt-Z6dSTChNRw9ebh1Cjn_SFfTiSl2ZqMEVXaFCO-55gcT6IXIudVQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/TqwGEngfzrn0QwztxLkVHB5NN9g4HhcxKAxBzAjsS-psFrN2u0Vg1abvi-cHT0eRcQUksSXW_dInuUN4am525aacijMz7JBU8fEovZzmeahX725rVJMAtKRD5LzUIQC5S29oDNCzsGZkq_t67DT4W80xDtVpveOHb1WGiUBEufRrj4nRP7f8Sp7-idI6fDdQolQFfEhotJdU_yfmCUTlL1ZL5QCWs6EWp9QS4qBMLlZcorUaw5-HM0hL0TGi9d7JcGl86Y6McPqkb5lik1uak0F7cVQKK5_aMmO6R5gjIeZIjMzP1rHDW6CHYQkSh9ydHeefZn9cTlPJnWi8t1mtTQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">هوادار ترکیه تو بازی صبح امروز با استرالیا :
@Funhiphop
| Jenayi</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/funhiphop/77869" target="_blank">📅 18:35 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77868">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">با ماف بت از جام جهانی پول در بیار چون کلی هدیه هم خود سایت میده
💵</div>
<div class="tg-footer">👁️ 9.65K · <a href="https://t.me/funhiphop/77868" target="_blank">📅 18:35 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77867">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Y7xK1WeQMXMIxNauct5MNB32i-v9Va3HcQ-L-gZxo8f4T4Gf23abRLNmscC7hIhbR27FPqqLbPO39hUgTJKd6p3BceetWsFn6aZLdBdXzrvA453mnebVJlnKJHI4EcYXo5RhHGZ54hFCGH1YEidUIxeIsyP2TDiurrW87YFfxV8I3JikAWplK287SjsV_0d71iCqs-SI1QpiFItPQpyFWWr9ws6pKKDtIi63hPLk9yXHNprJ13qyn7a07XzvlZEQBmh_0O67CWNdE9rXx9DuTTTCA0E6V2E0o6tNA549oRvP9zxJ76BdTgOludEhpo3HSirtQEVBmTG1_mGib1HCGQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
چرا سایت بین المللی ماف بت بهترین انتخاب برای پیش بینی جام جهانی
❓
1️⃣
شارژ و برداشت اسان و سریع
2️⃣
پر اپشن ترین سایت فعال در ایران
3️⃣
دارای مجوز رسمی curacao
4️⃣
کارت به کارت همیشه فعال
➖
هدایا بی نظیر ماف بت:
👇
🎁
100% بونوس خوشامدگویی
🎁
برگشت باخت هفتگی
🎁
هر روز 100% فری بت هدیه
🎁
هر روز 20% شارژ اضافی
🎁
گردونه شانس با جوایز بی نظیر
👍
با فعالیت در ماف بت طعم واقعی امکانات در سایت جهانی حس میکنید
👍
🎯
ادرس بدون فیلتر سایت:
✅
https://mafclub.online/fa/?btag=260368
✔️
کانال تلگرام سایت: g24
🅰
🔹
https://t.me/+3Zxs6WU7L_UzY2Fk</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/funhiphop/77867" target="_blank">📅 18:35 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77866">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/liig-ahfVXzEX7mkkS-Cs-LBs5i9F8dlxK1cfTrz8WwQyBzSxb9G0y2F99Qe0UXHEb3C8uWYN23jXzQT8Kq2OiRyehTQQpnov1VHzp50fneeiWRs6eovIrUR-L-5bLolZkwGnmQnuuwsC8Z1xv1d5D2rtIkR2vrehFahg2vcMFU-lh9DxV9q6nHA2cNv5N_QU4AtDhppDtSQHtfyh6lJqe4zAYNjFAqDLLYvLIRsPCGINuE2cfW2JMwiC3JVtDoE9JBe6H9e_HkTTRFclNn0e_gELoItB8vbu6yZabA-TwwmFFZHmO3tCp9y4wrWsGiLFgeEQ8JYvHY54-Ubp2pJfg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ:
حمله امروز صبح به بیروت نباید اتفاق می‌افتاد، به‌ویژه در روز خاصی که ما به توافق صلح با ایران بسیار نزدیک هستیم.
اسرائیل حق دفاع از خود را دارد، اما حمله‌ای که به آن پاسخ داده شد بسیار کوچک و بی‌اهمیت بود، هیچ‌کس آسیب ندید، زخمی نشد یا کشته نشد و نباید این روند مهم را مختل کند.
نباید حملات بیشتری از سوی اسرائیل در هیچ نقطه‌ای از لبنان صورت گیرد، اما همچنین نباید حملات بیشتری از سوی هیچ طرف دیگری، از جمله حزب‌الله، علیه اسرائیل انجام شود.
این می‌تواند آغاز یک صلح طولانی و زیبا باشد — بیایید آن را خراب نکنیم!
@FuunHipHop
| Nima</div>
<div class="tg-footer">👁️ 9.7K · <a href="https://t.me/funhiphop/77866" target="_blank">📅 18:21 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77865">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/I5YSkiVsqNXGShYCPBuYmqjCsUK3hxx3BGXBzcXe8p1xVh8xLf9k7yHAMnVO1aTS_iir8tB8aLLT15hyJAgjF0spLJG2N8XesGsWxtZ_2P5rhoKrPoxJgo1KuoMs9WvVz9-l91uOAOEYk63_QBpa5_q9GJFvSi-mzwFQYaLdHs_w6AuiTb8jzCQcb-D9T4MoEkKUOl6ljai51aEu9aBA0bfqz2QqIFHEaUyKgzWFmTWoB4lT1ZpXEwVOAnDg2xtT2v09jENN3eqz196VCFtDHJBz06PaWQOMcgicyKDIsMkYyIDAraveWG3clFmMVNVzVjd7pv9SSl7btxTTIbx9vA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">استوری جدید رضا پیشرو
@Funhiphop
| Jenayi</div>
<div class="tg-footer">👁️ 9.8K · <a href="https://t.me/funhiphop/77865" target="_blank">📅 18:09 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77864">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CR4jLwHeoVhE7bltLreaKGPWnJPQHG59XHOtIA1w0g3dHx8X3kdsQFfqwzhbgGSsVQTQqYtzPmiOzMTQBlmL_AMF0VWuD5U3TIh2x1K4uZa_kPwVqyeTHx5V_22o8cCGPxvIKOs8-7-X3iCxPBsSvlnHLt0R-PjyamRFU6AJiSpUBCVaSAssyzgxHuXCWkDLjKlKtPbft3JZ4G1r_m_dkHE3vgYwKNF3r6zzAgW5WkzRGg5bqZfABltjkMwIM1pEI5cMg2RXZvp8-1qpAvKy4lDseKntnLnRxThzOj5CKxUpx0SvFYUuZLLtXPljyomO9ZkmcmDieuQD2Nq8hiavYg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فروش ویژه | ارزان و با کیفیت
❤️
🔥
200 گیگ فقط گیگی 2/800 تومان
💵
100 گیگ فقط گیگی 2/990 تومان
💵
50 گیگ فقط گیگی 3/600 تومان
💵
20 گیگ فقط گیگی 4/950 تومان
💵
10 گیگ فقط گیگی 6/000 تومان
💵
بدون ضریب، همراه با لینک ساب
🛡
کیفیت مطلوب، قیمت عالی
🛡
پشتیبانی تا پایان سرویس
🛡
⚡️
جهت خرید از ربات اقدام کنید.
🕶
@Hunter_VpnRobot</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/funhiphop/77864" target="_blank">📅 18:03 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77863">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">طبق تحلیل‌های بسیار پیچیده و عمیق بنده، سپاه به زودی چند تا موشک از ایران به سمت اسرائیل لانچ می‌کنه، ولی احتمال می‌دم شدت زد و خورد اونقدرا بالا نباشه که بخواد آسیب جدی به مذاکرات بزنه و آتش‌بس هم همچنان برقرار می‌مونه.
@FuunHipHop
| Nima</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/funhiphop/77863" target="_blank">📅 17:24 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77862">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZMldp9UM5L47DNj6Kkt2K_1Dj0CwdcqYH2NKPkA0jIgvp-YryFHxiQjs1537eVRQKud4ee9ZRBa_NT-cazBaebV22rseWJQFEMPwDQ68uQUIDTrhOg1fmRx7Rwhld-upGD4oPL8Qc8ze_2ILjWF0RO3f2A-QEPGF-IxzDzRPMQpOdymHx8n4OXgVYYZ3PcHV95OuhA1Vn5AsylSUIDoHO4DsaLYBdSSY5QOPpTgSNCCq9OskwO6x-CXnRkattn0-Ryj3HsdATkyKqnqfUGvT6Q7adwNFTgLhbemY4wSgnKq7yZPiDlZbKHnFxBN8fkBiqQQ6kb7UnZYHqZhXcZTldA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">توئیت جدید باقر شاه
با وجود این شرایط جدی میخوان توافق امضا کنن؟
@Funhiphop
| Farid</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/funhiphop/77862" target="_blank">📅 16:13 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77861">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">تا این لحظه خبری از ترور نعیم قاسم منتشر نشده
@Funhiphop
| Farid</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/funhiphop/77861" target="_blank">📅 16:00 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77860">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/66e866b19a.mp4?token=Y2-hBsoIqkmsgvhjklf3Qzt3D8we2bEWQIfne_TU15x63MY--aR-bGYeupGVOotQ_B2fkMrOYM3mCPlm4HiPmRs7DKDXroKs8GpnoJ0Q_VjNefUpbpnAwcEE2KBm3-UJ5XxulTgSD82NeRcpmLy1tGxUy0qiSat85hUH27TZ_kVNPfFwodA7e1HKsiuyoVswm5wAhMOHoxzXeOr9RqaQFBNry5q29L7IzoiQQRMHU1VX33bi4EL5_e8eAoHnaDSjK_EslO9l80kKJCPYJBEf-NcfYN2igRVxhNuFy3rHTIueJi4_V7f7maR8-pY-PmYAm7PR2cot5YxGNXMLKf0t1w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/66e866b19a.mp4?token=Y2-hBsoIqkmsgvhjklf3Qzt3D8we2bEWQIfne_TU15x63MY--aR-bGYeupGVOotQ_B2fkMrOYM3mCPlm4HiPmRs7DKDXroKs8GpnoJ0Q_VjNefUpbpnAwcEE2KBm3-UJ5XxulTgSD82NeRcpmLy1tGxUy0qiSat85hUH27TZ_kVNPfFwodA7e1HKsiuyoVswm5wAhMOHoxzXeOr9RqaQFBNry5q29L7IzoiQQRMHU1VX33bi4EL5_e8eAoHnaDSjK_EslO9l80kKJCPYJBEf-NcfYN2igRVxhNuFy3rHTIueJi4_V7f7maR8-pY-PmYAm7PR2cot5YxGNXMLKf0t1w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پزشکیان:
پیامبر رفت تو یه جنگی؛ لت و پار شد و برگشت
@Funhiphop
| Farid</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/funhiphop/77860" target="_blank">📅 14:55 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77859">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">کانال ۱۲ اسرائیل: هدف در حمله به ضاحیه جنوبی نعیم قاسم بوده است
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/funhiphop/77859" target="_blank">📅 14:25 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77858">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">اسرائیل دوباره شروع کرد به گاییدن ضاحیه بیروت
@Funhiphop
| Farid</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/funhiphop/77858" target="_blank">📅 14:18 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77857">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YG7w-Makferko6thvU6LuBAqybrDQBBjWOJ1gnfE55bbXDCKOIBxLajT7nfqBTiD3w49d4mCiH99z-3sIp-VbQ45H0aib9xen9pWklK33u-5ySVKCQTmH0FxEmmQla4CkWJaGRthfLX_SeKXCIcrMJyw_np_kzlsSZ5ngcQAD1tEEaPwe5VOtRI-Ak2_Rl0f6G5DuC-jCL3LPoGcGJXWlu-w41zGVEr9crvnUhV1isrkgWQEBwrJ3kQ-xhCwIV_QjNEyaHH6Gf4_An0ke8WO1nS_umMHu6Deu1J8fbxwJhDSA1nczkIu9o8UTgzqaz9Fgpq_cnp0tUGygNuDE7t5IA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/funhiphop/77857" target="_blank">📅 14:11 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77856">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">امتحانات نهایی و کنکور ارشد بخاطر مراسم تشییع جنازه علی خامنه ای یک هفته عقب افتاد
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/funhiphop/77856" target="_blank">📅 13:50 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77855">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">امروز ساعت چند قراره توافقو امضا بزنن؟
@FunHipHop
| Reza</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/funhiphop/77855" target="_blank">📅 13:06 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77854">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">دادگاه عالی امریکا ممنوعیت ورود پرچم شیر و‌ خورشید رو که از سوی فیفا به درخواست جمهوری اسلامی اعلام شده بود رو لغو کرد
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/funhiphop/77854" target="_blank">📅 13:01 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77853">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pc_ZzvdesoZ74c-KhMKiLgfcFvOwz3zlKRq2hLPJn5-q_bCWPmC0Ilse3EhWCy2pOc2efXRiLzuu3BoF8XjiddNbjn_aMVPbEdkPWSwRgFrawzyRcFXnAshtVCnRjGc-POXv4NtHuuWI5lZcXLwPtzo489pWJUSyAbPUTC5EMQhll_VYABLaNFUGUfaHLJ5nRIZyXQRuUlpt2pMnB41I79OZPMVnNo5X92HtEc6XJdSOsLfKosTXV_egvvpdr3a1GM2K1_0KLb2vr3uSTo9yuYUZvoQ8xrZYexEuNSwCsyTZ9g0694wcWFwOCO6yX-51aH9baxlGw012isr-9CSP3Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">میرباقری(رهبر پایداریچی ها) دستی حزبشو کشید.
@FunHipHop
| Menot</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/funhiphop/77853" target="_blank">📅 12:26 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77851">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/UsSDDXmxvfyWF9Oww0BAJwywOsiL4ICr9cEiLg7fvoZtq_oLerbRBlVUERGjU4X0Kl9cSZ7eEFj2K_fWGiNIxrOPt1mqVALfFctNGvaYqd0-2mM-A1DIqT39L-jNGxGkEK5pj2mUfud--Sua-7b2Oov4-7RRL_z2d7mxu33XqfaE3qv-Y29coK3eZ9e7rxsNjw26tuufeWaKGA0TNPToivOtVB6-Y1GyQBhmFjE14717pJR7OPhAMALDn7mbnp5CdshBk5EJB6lACz3UCvJ-Lt2rDrhDQ1bW-nRVs_Lm_0FBMXNY6sEIVZDSDCr6OSNE3b9sXiy1PEgonhrMIXKKsA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/QdVqFJw709z12YwrcgR6QkCywGoc9r694fod5qHMjGfuuaIA1FuE5rk7HoZUuJ3fnm9bBDNFcDKage0YNXvgOfgo2YU3ItrMGMXx5a95fV89Rc3XU-cK_yo6EdNwP6gC2T0EF6-LjEzMGEQFOHesttylklde3IrYg9yLcK4fKYbAx_JuRZANCoWhPUDMxd2CpsA47rZXHf58o5EFlFn3MKh3IojXYOT-mUl09J4nSx42xlqjxl1A0koeKs2P7m3uWvSUxBxQ37buOz6mErcw0DNVy7vYJsJoEc5tja60NIIHa8Wh3PahuevPQgIRmgFmDnPdmJf5xXAIulnYrg_IIg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">امروز تولد این دو نفره
🥰
@FuunHipHop
| Jenayi</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/funhiphop/77851" target="_blank">📅 11:38 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77850">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LuEG5CBSIvkuFkMy5RsSHuGrzmcKAykbfSco2tG9v5nPpffAQl3I3gKOxM9GxUGo8SOlL_tkyQNpa_IgEFF8cf2NpBumJ7_915VeE-Msn5wnvpP1c9zrHZjHcGxaGQow_mjAmRhITCIA0oBNxVlvD7nusBZPfFr9lU-QHSiBxiP2-CWyXpq5EW6nw7n3RtNRAwxNkNDU-9QkU86Q1wPdYgND6lEMHW3TA5CYM4L5_Bd5gO02q0HEqy29SeKvPpw3WlgEMCJw2FRrahdYROlmQV5lv_xzEEohUYvQlaw2FLC2sT-tCQ9J5Bo-0FEu-EpPvheTdzReqRKcpJH9Vcnqxg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جام‌جهانی امسال چقد عجیبه.
@FuunHipHop
| Jenayi</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/funhiphop/77850" target="_blank">📅 11:34 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77849">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">derbybet.apk</div>
  <div class="tg-doc-extra">52 MB</div>
</div>
<a href="https://t.me/funhiphop/77849" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">📲
اپلیکشن رسمی سایت دربی بت
🌐
DerbyBet.com
💰
امکان شارژ ریالی ، ووچر ، کریپتو در کمترین زمان ممکن
🔥
🆔
@DerbyBet</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/funhiphop/77849" target="_blank">📅 11:34 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77848">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/L2Kc_YcDcUyxFltYscCGIDbsXKkqHZWOe9aPxsSuIOAS16txpjYEoV6uR5kRCZXLfHRzuOq6u52Bm5u0IiZIY4F12LHQTEpSeDR73bnpB9b1HG1qGIJrV1cl5Upob008FzkU6ZdcqAHz3x24uMFw1dc-mphDBM-kccNNSSR7lgsD_MmvYJ5PXQon5P1bVms8YJfG3lgnZmEmw_x6vBqb39Ld5Q66pxxCH8Zce_fZcYleRW3YV4YkPs1sZHQ1KtiPsm1VduSetXMxfqGpPmq2AeN3hAfjEeBnH7L9nJVh8XiBVvfvOA1NFTXVsdEhBIejFAZ9zPhpQiecNVqekF3Kng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
دربی‌بت؛ جایی که پیش‌بینی فقط حدس نیست، شروعِ بردهای واقعیه!
✅
با لایسنس بین‌المللی معتبر، وارد زمینی شو که حرفه‌ای‌ها بازی می‌کنن!
✅
آفرهای خفن ثبت‌نام در دربی‌بت؛ فرصت‌هایی که تکرار نمی‌شن:
⬅️
۱۰۰٪ بونوس اولین واریز؛ شروع انفجاری
⬅️
پشتیبانی کامل از همه ارزهای دیجیتال
⬅️
درگاه ریالی و تومنی امن، سریع
⬅️
برداشت‌های آنی و بدون معطلی
⬅️
پشتیبانی حرفه‌ای ۲۴ ساعته
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _
✅
دربی‌بت؛ بازی کن، ببر، لذت ببر!r24
🅰
✅
https://DerbyBet.com
📩
@Derbybet</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/funhiphop/77848" target="_blank">📅 11:34 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77846">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/r_HPlt9dw5A2C72LENieKkl9V3QAY6-NvZX-Mz4PCNDu1cKq3WQI_cRSLOr4dY_bV5zHhzGcYh7JeE_tTb0QCHlrI6-Yr4JG8taF4dQ1PdQbviMvW6RmSYlvBRFoxi7M4TRchztWw5h13rEBIFyoyjMYknRgbYR_x5_yMwduwwn4EUzn2Q8gpjNyhYxvy99YkDml7am7mTl9IDnaZI99x_d6sF8a2jd61KnvD1kcdMO2VxCXA7c6fQS40yPeN5osioZ9HQpS9vfYcNf8sP--lDrQlk5uXpbCi8JXgyfpJ8syuZz11DffVrQyQ5YfOPiEVOCHyLCJEhhJp19MdbWPpg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اسمو
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/funhiphop/77846" target="_blank">📅 08:00 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77834">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vTEuxdgh1Z2P0sXlk9QUJcDt5gniWYHQqFusSr-mzygGFYTxQyfGMbsClu3LJwUBFDyarTWy27GOW8R2fffofIKgfb0ZTkf_InZKvJp3CelbkJ6JtaZL33r_sTJN3wl2jL1dUeNoGb-ZVRjGVCChAEt7usGPScM5TXGNafClJCu8pB6NRXL6h1uyCECcEkkI2kBodyzLap3O7mkq-M5pUEn90RJ2bRMthnEqM9oQJrMyBGSiosLXKROsGjXsDmX1BQVHtf9fX8IDTpm6esb2SyiLYo1q5PG39ZTijrsg-e-371Zc_kIrMXyazUaw05Tub_t7YFuWPoPmJfKLOQHbyQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این خارکصده هم باز کسشر پست کرد
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/funhiphop/77834" target="_blank">📅 02:53 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77826">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">گل گل گل</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/funhiphop/77826" target="_blank">📅 02:06 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77824">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">اشرف حکیمی چرا فاز روبرتو کارلوس گرفته</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/funhiphop/77824" target="_blank">📅 02:05 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77823">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">آلیسون یلحظه شد سیدحسین حسینی
این چه خروج کسشری بود
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/funhiphop/77823" target="_blank">📅 01:56 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77822">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">مراکش زددددد
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/funhiphop/77822" target="_blank">📅 01:55 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77821">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">گلللللل</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/funhiphop/77821" target="_blank">📅 01:55 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77818">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hqUV4UuqN0WOKNci_ph3O1BI72GylYdMsIQZjrvPdj22npC2PLSU1XWAPxGg7FuXLjn5QHYndTpatjemxk-434WDuarYvP9QE0SbMaqAvewlEkDUzFByakezSf04vjH3eKgFW8IKTzeVf_h8eSqLEQBizaF6DOOjlTrTDSTLvZm4lA5KOkZsahNfsJHaznT0JfU2VWIOTDw-ALOrrC0jbQ0RyULVWKSiXcyfUoUR601GpNXGmiUS9JF5jn3LNwvg2P7FumUMOj9-5ypsMUKQWl5VHVbthMvtXaif1O5VwqkyhyBVN2mGooK-NBe_5qHpqbGgzYwug0gV7enXA_Me8g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترکیب برزیل واس بازی امشب
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/funhiphop/77818" target="_blank">📅 01:23 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77809">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">قطر دقیقه نود و پنج گل مساوی رو زد به سوییس.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/funhiphop/77809" target="_blank">📅 00:33 · 24 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>

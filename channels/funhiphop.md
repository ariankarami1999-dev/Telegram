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
<img src="https://cdn4.telesco.pe/file/fBAmYd-I9BNuZ9ku8kjiNhbLvFZ2r_ThimJMHr8g3NbUTl7vT17zxg5CyNMYDQyxf81HTjSS40djUGe9e9b1hkuQDMpOn0Q4Lt8Dja7EnnICgmTe-IGD-vDZf0peSc_cwDkInqfe9tHuNOeT0rrc4pYlsOeOFX_hfh51iBhWynbUL9luppdI73osm6LmyZzKAs2GAjE6kpkJIMqU0S6Behe1dK0wTLswlQ3V6RXstg2ytYGB23n2MH9kW637K2sXAvf8R-bKWDcGQSpK5fqIpJmcNEgLQ0Z-hCotm8YsyvDixfbkFt80PnhdJj9XKADSpTzLa4XJ05Iu9nYsyQn0zQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 [ Fun HipHop ]</h1>
<p>@funhiphop • 👥 268K عضو</p>
<a href="https://t.me/funhiphop" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 «قدیمی ترین اجتماع فانِ هیپ هاپی»🟡صاحب سبک🟡Tb :@FunHipHopAdsContact :@Chaman_Dar_KhakFollowing Copyright Laws©</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-07-20 20:39:24</div>
<hr>

<div class="tg-post" id="msg-84732">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">هالند راجب شایعات سقوط منچسترسیتی و جدا شدنش از سیتی: خب اگه سیتی سقوط کنه مسی باید نگران بشه، چون من برم چمپیونشیپ رکورد ۹۲ گل تو یسالش تو خطر میفته.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 4.22K · <a href="https://t.me/funhiphop/84732" target="_blank">📅 20:11 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84731">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dh_NPMb_8N9fQqOKWZzddb59pBVULU_16tc_I8i9AQREwK9lxEuZD7AW8vAmDlJ2AIbggroGoNtUl1UN_hPl780CqgyMqjRoKA-GoA4-WAgq0j_L7cd29CRiB6zqAfr-nGRZFGkhmtWdozqVZVmPa52K71mPBoPcDmm_1o-MmteGu4WOeUrCdV9FHgj8D15Ua8FxWFBICiVsCT0OGBIdt1YZ3Aa6eam_LLOkmirhHcxMF3xUHCRn4alsIg0GSbUbJT4TyNnvERj1YIsWaDiO1A_TQF_UT-7fc4p6DVzBe23mVZZqaBP0kZNDm50pIoswmUb9jP8voChLGXFLQWSsaw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تهران رتبه ۴۵۹ بهترین شهرای جهان رو با کمال شایستگی کسب کرد‌
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 5.21K · <a href="https://t.me/funhiphop/84731" target="_blank">📅 20:02 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84730">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/eecaea14fc.mp4?token=Dsr0gcNNCd6qudLi4x4F83Fb2R2LMMLM1wjTAxg_DlCx9yISAPqSyVJu11fgE1gpaIErMsV0GAHE75bCqHdn09aMSNdrcK2lrSBEaMGvUt4Kpir2sr_GRy_GF4ZLwh4i5-Ys764HTdEdzi8GATJ_lbhbo5H2jkGEerPR7Xizey-k4pKLEzU6AUH6z6wcpbMFDOHSmJ11AY4MBXU5DrxzYnC78Y296Kb7sZnKcnfYCI-azdaURFGAUwdaMxJWq1hQwo0FsPKuaoYOwiCxXXvBIQaRzoiBsvZV1R6uSkJXcUTM73KgtPexTsfbhd3yoJ--DSQak27JMdgvR4GTCfocLg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/eecaea14fc.mp4?token=Dsr0gcNNCd6qudLi4x4F83Fb2R2LMMLM1wjTAxg_DlCx9yISAPqSyVJu11fgE1gpaIErMsV0GAHE75bCqHdn09aMSNdrcK2lrSBEaMGvUt4Kpir2sr_GRy_GF4ZLwh4i5-Ys764HTdEdzi8GATJ_lbhbo5H2jkGEerPR7Xizey-k4pKLEzU6AUH6z6wcpbMFDOHSmJ11AY4MBXU5DrxzYnC78Y296Kb7sZnKcnfYCI-azdaURFGAUwdaMxJWq1hQwo0FsPKuaoYOwiCxXXvBIQaRzoiBsvZV1R6uSkJXcUTM73KgtPexTsfbhd3yoJ--DSQak27JMdgvR4GTCfocLg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">فک کن برا ۲۵ تومن حقوق مجبور باشی بری تو باغ وحش درس بدی، معلما واقعا بدبختن حاجی.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 6.42K · <a href="https://t.me/funhiphop/84730" target="_blank">📅 19:53 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84729">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ujy6T--S7my6Wz4Qm3QxrXbUX4Jr_9RUfKh-X-KoPQVt36L_QxfVlaNHLIxFj9QwUx8_6Icn5EMSkBIeUIjRLcjoz07qYJCrobyqBfAGJnC64uhVDgTQxqzGOOSxzZa_NsYPc21DOWNbcsvBkZnO9ubTnvcQAXjUYLCoxHRDE-bhgDlIPpw0KV-l7cYeXY_UsrNiv43KMt1SeH5Fb-Z2cLBm1cPS70ePGdaNaYN3qKL8K0RPG9TNZPS20V6les5hjoo4d9BBV2RfC6nQ8Mmlg2AgLUJOQOIqQV0-nEnHbuOUOZW0sD4NhNa6v6Q2zLAHPQ5LrBC-x4E-0ZEcMUpN7A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">😎
۱۰۰,۰۰۰,۰۰۰ تومان!
🎁
🫰
💰
فقط با یک ثبت‌نام ساده در
BerryBet
می‌تونی وارد این آفر بشی!
💰
✅
شرط رایگان دریافت کن
💯
کد طرح تشویقی:
888
💸
شانس برد تا
🔢
🔢
🔢
میلیون تومان
💸
🕔
همین حالا ثبت‌نام کن
G20
🅰
🛒
ورود به سایت
👇
✅
https://ikruyxysd.shop/fa/affiliates/?btag=914641_l303106
⚡️
کانال رسمی ما در تلگرام
👇
✅
https://t.me/BerryBetOfficial</div>
<div class="tg-footer">👁️ 5.52K · <a href="https://t.me/funhiphop/84729" target="_blank">📅 19:53 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84728">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">شاهین نجفی میخواد بیاد استانبول، دسترسی بهش راحت تره لطفا با راکت بزنیدش</div>
<div class="tg-footer">👁️ 7.42K · <a href="https://t.me/funhiphop/84728" target="_blank">📅 19:10 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84727">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">نخست‌وزیر بریتانیا: حمله به پایگاه RAF فیرفورد تقریبا به‌طور قطع به دستور سپاه پاسداران انجام شده است.
اندی برنهام اعلام کرد:
«می‌توانم تایید کنم که ارزیابی ما نشان می‌دهد این اقدام به احتمال بسیار زیاد در ایران هماهنگ شده و تقریبا به‌طور قطع به دستور سپاه پاسداران انقلاب اسلامی انجام شده است.
ما چنین تهدیدهایی در خاک خود را تحمل نخواهیم کرد. با استفاده جمهوری اسلامی از شبکه‌های مجرمانه مقابله خواهیم کرد و از تمام اختیارات خود برای هدف قرار دادن این شبکه‌ها و منابع مالی آنها استفاده می‌کنیم.
تحریم‌های بیشتری اعمال خواهیم کرد تا توانایی جمهوری اسلامی و سپاه پاسداران برای آسیب رساندن به ما را محدود کنیم.»
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 8.82K · <a href="https://t.me/funhiphop/84727" target="_blank">📅 18:37 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84726">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">شین: پرتاب دو موشک بالستیک از یزد
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/funhiphop/84726" target="_blank">📅 17:13 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84724">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Jasm4MYJdCHBQsBArMuIj7tuMZZyTdhuH1pkowlbGJbzVPDFfG9aaafKrcV9x5bae8Czmb0OxxNDLQfLnkm6vEcEM26zzD0h3BjAjqfZrT_iPsoc8cjv4Mkei6cnXsIxVNykYcEtfL5f810qiwPz_zWvpBdB80_5p1vcI3pHRmeJjbkzrQ5t-9r0qteqDg7nHKpQgN4gGQTojpRXJLicE5Cg-xpXmwsO5AD0cNAI6YB67aQw3sDEurzza0mtyjTqwLsSCUBuhpRQK_yXMsTfEYBp7kuxU4oRZuxRzkuM-KNpn7GPZKNfI5vAC-h2EsUBZL9Bi44IqucCsZP--g4hAA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/PDOkeUveuNlD3jrtqM6AgyrXtHeSpev19l-knoA54vfvQvLeOkRoxS1DJ8zLRjRAY6fI03O9xdb-luMkRvawGfTDoADhDbdAaaR_xmwmxuCCMPerS5D0BidvA0dlkJ-qUanNF2WfIo-qfVayMWvs-Xxp5aDo3_1QJ-zXPW7jwC6vt3u9rGSpm85mYOLKFA8G6bq7xuClDuTDaZBdCSitc1dwMDmH9ruzsJvp6aelnCgyqtBf0gRHMgehlwBaIi-MMfEZ6x0Ww8WOvyPQUmAloAoV_DmjA4lTdbTb9pyecKB1pIrm-RR0fuVXb2Y2tfvth1G52m9jha0YPzqtf30FkQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">نتانیاهو لایو گذاشته داره راجب انتخابات حرف میزنه  @FuunHipHop | FaRib</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/funhiphop/84724" target="_blank">📅 16:55 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84723">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/40ca73243e.mp4?token=odl9LF0ucOKSedDhDJ6EcNc17g_S3tkQOafMlaZ3o98wGQg1SWwGAKmHNNuW1ZdD09YrUpA0yqNYpCMCT011yjC0a99-wwzWsFlPpM5p2B_XU8wa7Eq5TQdRt_1An-vJ-Gwi-O-x7N41WPOFSCLPYv2KJG6H3ZzwdsrdVA-WS6wnaalMV_7eQclEqYuXo-cKcJkXfoRpZYBbBffP0eBNPYAh7LNIzH480jIkndmDbOup8eU61_NahmaGT4WkvV7lZPZ-MUOXZIPqFOSd5tEDntpoiybAeXrM9uP89iczkmu9GH7P7J-saAd7NUMGYUe0TrD8Li6hWdlYyCzmV19vbQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/40ca73243e.mp4?token=odl9LF0ucOKSedDhDJ6EcNc17g_S3tkQOafMlaZ3o98wGQg1SWwGAKmHNNuW1ZdD09YrUpA0yqNYpCMCT011yjC0a99-wwzWsFlPpM5p2B_XU8wa7Eq5TQdRt_1An-vJ-Gwi-O-x7N41WPOFSCLPYv2KJG6H3ZzwdsrdVA-WS6wnaalMV_7eQclEqYuXo-cKcJkXfoRpZYBbBffP0eBNPYAh7LNIzH480jIkndmDbOup8eU61_NahmaGT4WkvV7lZPZ-MUOXZIPqFOSd5tEDntpoiybAeXrM9uP89iczkmu9GH7P7J-saAd7NUMGYUe0TrD8Li6hWdlYyCzmV19vbQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ی نفر تو ارومیه اومده واسه ی مسیر نزدیک اسنپ بگیره بعد اسنپ رفته بخاطر ۱۰۰ هزارتومن یه راننده از ساری فرستاده، راننده و مسافر هر دو پشماشون ریخته:
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/funhiphop/84723" target="_blank">📅 16:39 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84722">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RouOSpv5BeQ3oK5jcUgWQSahhb-6JiNJ3QowAz8mW94GCYJm9JBuKOvNXJaLNbNIs1F7rNDwrF6Wj4p9Ooy5PPGmw3ZU648EoTI4IX9yBr4g9r8cZfzYydxkNgT89R14tn-BtC20pQ1MMAH5kaQGPVWcg8B2Ho2pE2Ej9mg22iP1NXyj4pyOs2NO227Yz1ozaKFItAib45z8aJQiHhElr_yHXfjiPxmSKgm4uFSKaQ0UdY1VpC1CJtSj4dRW83EyYH8lV-_awf6X_CtA2-Wrfm8JOEEzsbJPgyFipUWUGVydjEv_CT-PFHG-WipvXsFhUfcZHT3S20kIsnRaFRukFw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نتانیاهو لایو گذاشته داره راجب انتخابات حرف میزنه
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/funhiphop/84722" target="_blank">📅 15:33 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84721">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/479ab143f8.mp4?token=husiemTfQGbdjJMVUpiNAKeYQCdHzJuW7NZaKqN2ZPusY27DqXA97ATBwo2AkGamLexC4JFFyq6xsbj6sNtc3gD4gbLhOUFuFZO65hj5PW2Jb7Zv24QNYGd7ccVjJG-L8C8qms17X7H-lKMOPazsilfWpv3YdEg7omIkWNcluF5xeCrhwyecxQTW7Wtb1pBn9Vk4TWAIcp0wHTZmA0N7Dqi3X6DgiQM2B8GWLmcmztKVC4N7HQ48S3u_GVYK9TGdIwJIOzzIS9l1eVzZKvMXHmjzdzbH_SFK1T-OYF1F-cmTzVGdXxaKBADTjjgCXytUFEF1Ki6_356eWpJ1fqra0w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/479ab143f8.mp4?token=husiemTfQGbdjJMVUpiNAKeYQCdHzJuW7NZaKqN2ZPusY27DqXA97ATBwo2AkGamLexC4JFFyq6xsbj6sNtc3gD4gbLhOUFuFZO65hj5PW2Jb7Zv24QNYGd7ccVjJG-L8C8qms17X7H-lKMOPazsilfWpv3YdEg7omIkWNcluF5xeCrhwyecxQTW7Wtb1pBn9Vk4TWAIcp0wHTZmA0N7Dqi3X6DgiQM2B8GWLmcmztKVC4N7HQ48S3u_GVYK9TGdIwJIOzzIS9l1eVzZKvMXHmjzdzbH_SFK1T-OYF1F-cmTzVGdXxaKBADTjjgCXytUFEF1Ki6_356eWpJ1fqra0w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تمرین حرفه ای کماندو ها و نوپو تو سنندج
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/funhiphop/84721" target="_blank">📅 13:44 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84720">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">نظام‌وظیفه با درخواست کمیسیون پزشکی علیرضا بیرانوند مخالفت کرد و این بازیکن از اول آبان‌ماه باید به سربازی اعزام‌شود
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/funhiphop/84720" target="_blank">📅 12:26 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84719">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">پزشکیان : داریم در تهران آب زیرزمینی را استفاده می‌کنیم و اگر تهران هم با همین روند رشد کند از کجا باید آب بیاوریم؟ باید برای حل این موضوعات چاره‌ اندیشی کنیم
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/funhiphop/84719" target="_blank">📅 11:25 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84718">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tUvbrH2bpp22UR4bdfrKGYN9nIpy_wnhTe71zO17u91oBcdIdApXWCs9H7yP20JyMPhsCatxk3Qfze6YItXp98V9--Muy7Xq5YeDEISTpGajmDnw_mRzetJ2B3DGW8F8X5s7DiP27RSj9rpIymj9Uzq7-m6MTsTNHwagrfCTgJdoR6g9-T49D143IU0ZSdGJUiBSgdafPZjxIU8kCuZjo_1QgoBTWRo0EzlOj6Td4eFmJudmKwbHrel9mC_tVGKezQyukZxVRi77Dzj2vaG_5XZRsYumnxiR--DwmsC2X7fjBcdw9nfstgbYEw0rYkkjsxLBm-YsXwGSCMp4XKMaLQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">😭
😭
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/funhiphop/84718" target="_blank">📅 11:00 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84717">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/abc4e72c98.mp4?token=u2fxY8mhKR7E6Pz419A10YhFmSCzBrBxSsfc_IwEw2vAK90KmeB0BFTo4xGlM16XtyYJ8N9bl8xjDyByu6Y2yLvR5KDL5HqCZC6qItSt3J_mYqpbI1rRCdygOdztCVdP99PN9v1vkJncCK8mhexHPy1lYLuPJUxUYJnnIxuBPd5_XLTcSr3gbDXkSnW0l9wODaYsugVHYAaYMfdN6PSgN_vY5v2PPb9MkBtJR8OphVLPHGFrO5kFUIfP7w1I_SsONVNnsPXEtcbrnw6lOSjpM6BWW-F1luWVI_OLyJY2WYPaECVNynIAfsIXXVvYCuWvsIe7HcwQRchL4Xt047BFTA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/abc4e72c98.mp4?token=u2fxY8mhKR7E6Pz419A10YhFmSCzBrBxSsfc_IwEw2vAK90KmeB0BFTo4xGlM16XtyYJ8N9bl8xjDyByu6Y2yLvR5KDL5HqCZC6qItSt3J_mYqpbI1rRCdygOdztCVdP99PN9v1vkJncCK8mhexHPy1lYLuPJUxUYJnnIxuBPd5_XLTcSr3gbDXkSnW0l9wODaYsugVHYAaYMfdN6PSgN_vY5v2PPb9MkBtJR8OphVLPHGFrO5kFUIfP7w1I_SsONVNnsPXEtcbrnw6lOSjpM6BWW-F1luWVI_OLyJY2WYPaECVNynIAfsIXXVvYCuWvsIe7HcwQRchL4Xt047BFTA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بالاخره دختر اومد تو اکسپلورم باورم نمیشه
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/funhiphop/84717" target="_blank">📅 10:47 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84716">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">همین حالا ثبت‌ نام کنید و از بونوس های جدید ما لذت ببرید
💵
🛍
👆</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/funhiphop/84716" target="_blank">📅 10:47 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84715">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NXBzhBMZeTTYfhsvLcLvpIKiMTOtNG5pfVCs4DamKb8zMaRi6V7coXFn_ZTYr0hp1y7twAXFgUx4hkSuLjNmxHr3b2QLzBHm1rAIYVE8wtDzAwX_ekGRLDLwvRyKowNUaTg_VnKENN4IQpaztft8tRE55uBaRKWEbj-oNawdDyqxIU97LiaevfJtOlj0cjYxjFWsR1EQRKOnjdEdumHisUzzRfJXZfhw7LegMGZe84iRPgc6p05kb5_IuqrRvf9KPqfiqiCa7IyA_EZJ3OK6n4fnCtuhk3QyJxf3XKfSCp6E_HyVZ3H1tSNXWH6dSKpkp_Qa_oFkmjBvaCbnEroiSw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚡
بری بت | BerryBet
🔥
مسابقات امروز
👍
⚽️
الغرافه  - استقلال
🌎
ساعت ۲۱:۴۵
⚽️
تراکتور  - الشمال
🌎
ساعت ۱۹:۳۰
﻿
💸
ضرایب ویژه و رقابتی
⚡
پیش‌بینی سریع، تسویه آسان و پخش زنده مسابقات
🎯
همین حالا شانس خودت رو امتحان کن و هیجان فوتبال رو چند برابر کن!
✅
۱۰٪ شارژ بیشتر برای روش‌های رمزارز
🤙
ورود سریع | شارژ آنی | پشتیبانی ۲۴ ساعت
کانال سایت:
✅
https://t.me/BerryBetOfficial
آدرس سایت:
🅰
r20
🔗
https://ikruyxysd.shop/fa/affiliates/?btag=914641_l303106</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/funhiphop/84715" target="_blank">📅 10:47 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84714">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/408b52a61f.mp4?token=onzG9_gy3WrFe42wZZsod0xRxla83PfFJf8jMcRIz7XnGS3UJbc2yx0iFPmzzXrkCntvhlVARqptipXNnCKcrv1uvP59dSAbPJH6_oSKESfbWnWmrjOe8T5RHExNVwkjOrTsotSUkPEpxU4-YcDuKykoQiJUEipoMEppAF7gGReUGbc2I8iUzH449akN0GYnbMXHqRl_5evCT1AjeLMy15VaXU86fxGnVSdxrU43kBDEzZ8K_vhWdBAMa3xKnmJuCgUKl37xwkAt9PCLTc5ClNiJVqEJnyBBA-AeGrXyVy2NqJas7WLpzJuCxzbLECnE_wbhnVAnRVr2ufsB9fQXCg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/408b52a61f.mp4?token=onzG9_gy3WrFe42wZZsod0xRxla83PfFJf8jMcRIz7XnGS3UJbc2yx0iFPmzzXrkCntvhlVARqptipXNnCKcrv1uvP59dSAbPJH6_oSKESfbWnWmrjOe8T5RHExNVwkjOrTsotSUkPEpxU4-YcDuKykoQiJUEipoMEppAF7gGReUGbc2I8iUzH449akN0GYnbMXHqRl_5evCT1AjeLMy15VaXU86fxGnVSdxrU43kBDEzZ8K_vhWdBAMa3xKnmJuCgUKl37xwkAt9PCLTc5ClNiJVqEJnyBBA-AeGrXyVy2NqJas7WLpzJuCxzbLECnE_wbhnVAnRVr2ufsB9fQXCg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">قرار دعوای دخترای دهه نودی بخاطر یه پسر
انگار یه دختری به دوست پسر یه دختر خانوم دیگه تو اینستاگرام ریکوئست داده و همین باعث ناراحتیش شده.
@FunHipHop
| Mehrdad</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/funhiphop/84714" target="_blank">📅 10:25 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84713">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">روسیه حرف ترامپو به چپشم نگرفت و به نیروگاه برق خارکیف اوکراین حمله کرد
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/funhiphop/84713" target="_blank">📅 01:31 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84712">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">به رضا پیشرو ميگن: از مسافرت برامون چی آوردی؟ ميگه: تشريف.  @FunHipHop | Arash</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/funhiphop/84712" target="_blank">📅 01:08 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84711">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">بچه‌ رضا پیشرو یک ماه دیر به دنیا میاد، ازش اجاره میگیره.  @FunHipHop | Arash</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/funhiphop/84711" target="_blank">📅 00:45 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84710">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">دسسسسسخوش و کیرخر.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/funhiphop/84710" target="_blank">📅 23:31 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84709">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HBs0P6QchLxX-yL8sbRYCIRfg2v39NI1uynfrzxtL-5tW1TIh85WjmiCFjVh1U0odLGRTWVD5Ovyl4Eou2ZTCdHZBWOaikbh7DhsWvwJmCqh35M6hWyMUBIC0npeuvU1GQ2qN6KnoSZHV3bUTTv5Ah_NF1aalB3yiIw6ryAYV6rRJsh-YWC1SabLeseVJOuLfc4lyF8LOEQHRlchbzwstNbG9FweN7VikE0hLXxiifL0RqPMDnsLtuXEUUZFgTG75pvlL9F2dyqLkm1snxDYJHj987XewsdmUOZKpaluCoTKhr8-PTZ7bbjW6pohKv4i0wg58HOMs6xzyHhiwuWy8A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دوستان First blood از اینجا اومد
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/funhiphop/84709" target="_blank">📅 23:04 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84708">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">تا دیروز هر روز صبح میرفتم سایت چک میکردم بلیط بازی بارسا و گالاتا رو بخرم یه امروز چک نکردم کسکشا تصمیم گرفتن بفروشن و تموم شده</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/funhiphop/84708" target="_blank">📅 21:12 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84707">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">تا دیروز هر روز صبح میرفتم سایت چک میکردم بلیط بازی بارسا و گالاتا رو بخرم یه امروز چک نکردم کسکشا تصمیم گرفتن بفروشن و تموم شده</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/funhiphop/84707" target="_blank">📅 21:11 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84706">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">خاطرات وینی پرایم داره برا ارائوخو زنده میشه
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/funhiphop/84706" target="_blank">📅 20:30 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84705">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">دوکو خداسسسسسسسسس</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/funhiphop/84705" target="_blank">📅 20:26 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84704">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GY8OyAR5VcJmuVmSGumTeoW1E4IfYWrTycXBRnFEROumdrQTpPHTWQJRqQwIqyWw1KkvFQbkxmjkGPC7sQSczCZEn2C9W829UU1KJBct9dPF0OlhEGQvnxGMGbUaj0rPAuwqA6rbT6veUCkeXNsv-t-RCPd_pGBNHyNNhnU62w-JOki9WKv4eU5UBY-_LEctt6Ynd31YtjOfVzd775ZLWI1IdHNahNgYqP3BIPTTuK69OvUpWq4aLoNdPo5L7h7O5ruw0op6y89DLD6SLBSlFLnCf4gZrJDTSpdF6THy5XqeFEOPWmr4SY4MKAfKEvQ7gPk03uSaOfv1VJjwfeWZIw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چه سخنان شگفتی به زبان  می‌رانی، ای مرد؟
❌
چی کصشر میگی کصخل
✅
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/funhiphop/84704" target="_blank">📅 20:00 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84703">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6cd2361427.mp4?token=cnGcICsuBWHAYLHYc4dOARmGZLxIcmbB_ZbROmgZT56J0qJjgNQV9zKhu_4C5cotwOHzIxi3pQXJJD6Fa9iU-uUl7VDQCZxTQs-dN3gKARiXukDHnAxJ2miNBZ8tCyoDK4tl-X1bbuariV35Az1izYJ7Y3IqS6NiUC6LXYbxVVQdua0MAqVap2cFJbtqyG0rdcKiX-DH76Zr-T9IgXt7-UscLnLSw8U2X-KemGO_tOeiV64-BIBfsC_LZXnwO2aV8AEXqEwJUBv0LZXE64ZBAowUi_jLAi9OH8UW_UZ4xNnD3XfG7aN-NXIulswdr8IFKop5cUlQ-JZvcDQrBpdGAr-WR_JVydHs-jCupXLHwHY030K0h-RJTWOSyJoTwgqdM2Ei0SqIvprMqxPvCtw0ObqNurhUj2L8raDprl39KIEKz3uaTllGQKT8_F7N-kKeXuxP-c3SX_ynB6J_BlUXL6vd9CxKjIIUIZCzChrqbvYlYxing9uIgwaJDlXu5y2KBrA56QzmplnivUno1FEYYNWMteZBeQu-TYa8ttuYjLmLJHIaOe5cVsBmM0-6GXwdt81u_4Dw9Q3CHspiBAoup8s5oRai8dYpetnuv3VkPmt5hIQVvgJ_L-G46EocsJBSupZBASxYPawvcWkHZ2Swfrhg7CMJcQ4xUOqkP_bngy8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6cd2361427.mp4?token=cnGcICsuBWHAYLHYc4dOARmGZLxIcmbB_ZbROmgZT56J0qJjgNQV9zKhu_4C5cotwOHzIxi3pQXJJD6Fa9iU-uUl7VDQCZxTQs-dN3gKARiXukDHnAxJ2miNBZ8tCyoDK4tl-X1bbuariV35Az1izYJ7Y3IqS6NiUC6LXYbxVVQdua0MAqVap2cFJbtqyG0rdcKiX-DH76Zr-T9IgXt7-UscLnLSw8U2X-KemGO_tOeiV64-BIBfsC_LZXnwO2aV8AEXqEwJUBv0LZXE64ZBAowUi_jLAi9OH8UW_UZ4xNnD3XfG7aN-NXIulswdr8IFKop5cUlQ-JZvcDQrBpdGAr-WR_JVydHs-jCupXLHwHY030K0h-RJTWOSyJoTwgqdM2Ei0SqIvprMqxPvCtw0ObqNurhUj2L8raDprl39KIEKz3uaTllGQKT8_F7N-kKeXuxP-c3SX_ynB6J_BlUXL6vd9CxKjIIUIZCzChrqbvYlYxing9uIgwaJDlXu5y2KBrA56QzmplnivUno1FEYYNWMteZBeQu-TYa8ttuYjLmLJHIaOe5cVsBmM0-6GXwdt81u_4Dw9Q3CHspiBAoup8s5oRai8dYpetnuv3VkPmt5hIQVvgJ_L-G46EocsJBSupZBASxYPawvcWkHZ2Swfrhg7CMJcQ4xUOqkP_bngy8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
تورنمنت پاییزی بری بت؛
5️⃣
🔣
1️⃣
میلیارد تومان جایزه!
💞
🃏
پاییز رو با یک رقابت داغ در
کازینوی
زنده
Creedroomz
شروع کن!
🎰
🎁
هر هفته
0️⃣
5️⃣
7️⃣
میلیون تومان جایزه نقدی
🧭
۱ تا ۱۵ اکتبر
🏆
جایزه برای
۵۰ نفر برتر
⭐️
هرچه
گردش مالی
بیشتر، امتیاز بیشتر!
💝
بازی کن، امتیاز بگیر و برای جایزه‌های پاییزی رقابت کن!
🎉
📱
ورود به سایت
👇
📱
https://ieoruyxtsud.shop/fa/affiliates/?btag=914641_l303106
📱
کانال رسمی ما در تلگرام
👇
🅰
g19
📱
https://t.me/BerryBetOfficial</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/funhiphop/84703" target="_blank">📅 20:00 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84702">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/J6_HXShplvmrIYLaTa7WmMdaxncBGc2tAsyHs4cfCXxTBQWcbYudKSIS_P_HpglCZzZLfcBo7fF-LCfBWRxQsCFC17RmRTzqYZDvrUJb6lKQpU_Lel0dRPTMHuqc2373i69X4vluDKsCIv10HomZ8hUs-2IsEC9Uk_Gv9Kjv_tJ8qAA6puKzbh0KVJuEyfVYOeYOhYg7GMuxITRfGoETkFTYnS2ZGMeQclGjIy9nmj8Gntx7EkFJbEYVX3RdlQg2YDdq_MEdZv-QI2iotSoQ8TRFxslpx_VodMSZ989SRtIxaLqE5SnotlnB5Xl6AAEZ3kYwhogJEpOxK3aLgmGsPw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تو بابلسر ی کافه افتتاح شده که با پستونک به مشتریا نوشیدنی میده :
@FunHipHop
| Mehrdad</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/funhiphop/84702" target="_blank">📅 19:24 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84700">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PAUvfFp8QOy2Wu0PvqZp6WyC2Ug_nQ1xAVeq6WcP8mMPqWNebpl1ufRf9pws669vfmSX1UWO2FHUlOmDxv-0PcQUGMXLks6OybJRPOgupjmtvFwdZom1dACsMUJLiATJq7skMlfkq1KfpecPg4IZJti7pwAt8GrYuBPN3j_Y5wcnNA_2jmbvn6MhAzMEfngv0F2YtiR1VHDr8dHBYs3ugUpPefwlcRx_XPAp5KuFZPFdYaPg5CXzj6AiBE6b-1lG_xVaup7Fj7bIF12kls2xIlu698FgldM9Q_cv-IVu_IvbsFaTjNZdE0lVPXG1LzPV3Ne46F_qbl62evNKxXYv5g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خدا به طرفدارا لیورپول صبر بده، حضرت ایوب هم نمیتونست همزمان مونیوز و بارکولا رو تحمل کنه.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/funhiphop/84700" target="_blank">📅 18:04 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84699">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KeoBJ0i-oW-07AgSSPNDS8di2GCaf2mx-l5KktsH7qp33fxt209QyzBfdiZ0ckL7F1XvOtrQxCK0pZGDLAjUD25vJfEKU36IlGfNyFippfIZyav7LJmWUltlItucJFwZcZtvY-KyE0EsfoNDptg0KQujLF3WM7yPqExbTJudcgt_ib-JMgBSQFDfiFwd0yR_AYTZBO40cJvBsh0Wz-8CKcJrF5oc1VAZNKCszvfs6lA4jXSUgXLNsAn0ij6QAjVcqvFucM6XbjwJMyDOVh2JpBuJgAKcEGMdHQYVVtmBvW_eXFLN2JIrr58xxNvcvJJBupstomeXBkH4rFtQDFJbXw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مسیری که گل‌گهر برای رسیدن به بحرین رفته:
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/funhiphop/84699" target="_blank">📅 16:50 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84698">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4dde88b838.mp4?token=AaCUbxBChKd1J1gqFIJW3V7l2LzMNHoGns20PUvqzd9uvM1DBH8cAhU5FPbtZTEvs2MTh7jzKvpUx15ox4gFYZVkZ-JROLReGu0ZcQioIKyN4q2MtSdL6BLLKchC9pMn0vIr2zVAvZNRYtLdnSlg-tQWHjR2CKRfaiKTe6H1m4EmbSeIGfrbqRZP6lyhlzycBnCcLZMCmh343JvtWx59o599pofMkA4MQUh-M6k4qQsULjpvwQ5q3ATQws55svuBQuyRwKcdBPXrRawm07Va02PFY_BBoNMmYawkgKIx-H9OI3OLFyF4dqZ_j48TN-B06xsm-pRAGyeZs6CLWctaBw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4dde88b838.mp4?token=AaCUbxBChKd1J1gqFIJW3V7l2LzMNHoGns20PUvqzd9uvM1DBH8cAhU5FPbtZTEvs2MTh7jzKvpUx15ox4gFYZVkZ-JROLReGu0ZcQioIKyN4q2MtSdL6BLLKchC9pMn0vIr2zVAvZNRYtLdnSlg-tQWHjR2CKRfaiKTe6H1m4EmbSeIGfrbqRZP6lyhlzycBnCcLZMCmh343JvtWx59o599pofMkA4MQUh-M6k4qQsULjpvwQ5q3ATQws55svuBQuyRwKcdBPXrRawm07Va02PFY_BBoNMmYawkgKIx-H9OI3OLFyF4dqZ_j48TN-B06xsm-pRAGyeZs6CLWctaBw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">آقا ابوطالب یک رپرا
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/funhiphop/84698" target="_blank">📅 16:29 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84697">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">دختر خانومای گل، روزتون مبارک.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/funhiphop/84697" target="_blank">📅 16:03 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84696">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ioERhyB7j8izmWmla2t65fv1HPMGWgvWB-Vs2K4NjwWCdoZjAEf_cABVmRk0cgOKx-naFg5f-eRQLlUPI3Lwz379KosxLEbMrB-ygt8MZstj7CRqDaXWjO5t46RP2YM-KqkFJiiTaLs0jGBo2UCzKQPFM4PNPmBgENsvSztJvbtotDRVPPtu0b1sJDmqPX03siA2cvNFT1H6MtdJyGIH0S6xYo0l77_UH3CP5S0FA34kdxVg6kQp3R2iluIXBITjPDcL0_ekt1LCqgzvMZw5BMJcDbt57r93xVCTQglcmgJ_UOvhxrY6kMn-1nVZUKPgVsl0-asjQvTIl5cZYP3cEA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">گراز پدرته کصکش، حرف دهنتو بفهم
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/funhiphop/84696" target="_blank">📅 15:44 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84694">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GCjSwEpfdeTr0WuTfMzCf9ouryJ8e99h3E8RSnm9q6bOtBZ-QWcEsMreBOB_ihcXuKOEwJibAzrPoJyqsrLdLJgqeoorsS0CfWMP900Rp3NrYOeLJ4AkZk7MdouBBBWpm3gDIwyZkmnaPvIVXCNSgO99_0bmf6mUG4-WivIeabdyZuesldQ_NXH4TAYmqA6QjseOJRqNbqdxj9WXA7OLcj-nGtzU8RmXLAoj52_DThK6aPPWZ7fKubKeVu6_YY6TSiRARiI1NzrFEw-uHRVY9Y_d8OJNNRu6TqKnZEA2MYPEbObwrBHbdI-i42JFSGz1Ceod_cTAGIfrtyjGlTqrjw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">منم یه سری رفتم موزه همینجوری تابلو راهنما رو با یه شاهکار هنری اشتباه گرفته بودم دیگه نرفتم
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/funhiphop/84694" target="_blank">📅 14:15 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84693">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">زلنسکی:
اوکراین آماده است تا حملات خود به پالایشگاه‌های نفت روسیه را متوقف کند، اگر روسیه نیز حملات خود به زیرساخت‌های انرژی ما را متوقف کند.
پ.ن: این ترامپ لامصب چیه که از یه راست افراطی مخالف مذاکره که کشورشو به کام جنگ با یه ابرقدرت کشونده همچین آدمی ساخته
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/funhiphop/84693" target="_blank">📅 14:01 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84692">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/548dd7a29a.mp4?token=DtAV5NoPV8-F5ekQK0bP-ZARlXcGTqbCWLC8BxyokB_HvBiKMBioT8wgNnt_1_f_cd5nr1dNA_gKbh8sruZDU_vhQRkF9tTFjl9MrEAJE4elInqEVNxxV2aTLa1zDgH72jRva9hei9xtHPT414WpjxQ8VNVWQe2X79DF7pdkoJJe6_xgfLEGgh2pgXz9Wt8vyATzU7AFFu1ZqmRyFCABNf-wSw2ugmEzUO58JcJE3wMr5pxQ2IOJXlCSecoSgsIt0VCf-T0W4dP3IA3vltjwAo5AMajeMisFEfCzkmhYxm0Xw5g4X1xdMDspRACxVOpTjgLA9XgJQ_Oa3KvgRqEOkg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/548dd7a29a.mp4?token=DtAV5NoPV8-F5ekQK0bP-ZARlXcGTqbCWLC8BxyokB_HvBiKMBioT8wgNnt_1_f_cd5nr1dNA_gKbh8sruZDU_vhQRkF9tTFjl9MrEAJE4elInqEVNxxV2aTLa1zDgH72jRva9hei9xtHPT414WpjxQ8VNVWQe2X79DF7pdkoJJe6_xgfLEGgh2pgXz9Wt8vyATzU7AFFu1ZqmRyFCABNf-wSw2ugmEzUO58JcJE3wMr5pxQ2IOJXlCSecoSgsIt0VCf-T0W4dP3IA3vltjwAo5AMajeMisFEfCzkmhYxm0Xw5g4X1xdMDspRACxVOpTjgLA9XgJQ_Oa3KvgRqEOkg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بنازم یه جوان فلسطینی که کشته شده بود بعد از به صدا درومدن آژیر خطر پاشد فرار کرد.
@FunHipHop
| Mehrdad</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/funhiphop/84692" target="_blank">📅 13:00 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84691">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NmXGXWg-lSuTwUFz6Ak6vN01zk-5_6OOouW5UNsKv2fIIPVMm3s840q8TC_bgUBoGiItNAVt3Ux7KnRWF5jF8VTOw3_71g0OD74bt_sfNpQEnEKP8TEux29pfnFPxrQydC3pWH66SBkj4bvkzOosdAVjrGy3ZnjJFVtv1S4FortHiW6swsCJdy-JQB19gFeNN8YhPVHBcaF-BhwClLtEMZGBQQMNVBJdnf6CttlOkwWBcaQvtc01YCjoBmRCslaI_481e21M3B_1WSr6MEQ6ly7VeLh9yDk3Aa_eq5Ecv4HQSoYk1wWLDDQpB95u1vvqELF0x3CKk1pZzqZ-C3ttig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">گنگتون بالاست مشتی
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/funhiphop/84691" target="_blank">📅 11:48 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84690">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">همین حالا ثبت‌ نام کنید و از بونوس های جدید ما لذت ببرید
💵
🛍
👆</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/funhiphop/84690" target="_blank">📅 11:48 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84689">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lqp_vnigLxyATFDzCWIpXGGOf4nq96xcwi4HwACbYB6txf4SCVQ-0KqtTc7FL1D25Q-kYK4DugOkqqvLiZlGyehuj6LgGVOhPMveoXugKnWcyDkefwV3ZlfMd-cIcwc4j525a1OMhTB2rnovQosz1QpJLfwHwrC_DMqmfrtIdDxk6bD7AQvZrkiBEUvVgi_gppVHdAsQpqc4XctFaYlSeWCmVAloFdDPCTPLKO_fwPSJCk6XXEf4j8cnzbNNQhdLnVd733OgmHneP0mdcksh9oUd6DEW77Maas74Bz33g7Fsb5NrIisF4FYFLzU33mvAhljgjJfVv_X-lrLpXkc3oQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚡
بری بت | BerryBet
🔥
مسابقات امروز
👍
⚽️
لیورپول  - منچستر سیتی
🌎
ساعت ۱۹:۰۰
⚽️
هال سیتی  - اورتون
🌎
ساعت ۱۶:۳۰
﻿
💸
ضرایب ویژه و رقابتی
⚡
پیش‌بینی سریع، تسویه آسان و پخش زنده مسابقات
🎯
همین حالا شانس خودت رو امتحان کن و هیجان فوتبال رو چند برابر کن!
✅
۱۰٪ شارژ بیشتر برای روش‌های رمزارز
🤙
ورود سریع | شارژ آنی | پشتیبانی ۲۴ ساعت
کانال سایت:
✅
https://t.me/BerryBetOfficial
آدرس سایت:
🅰
r19
🔗
https://ieoruyxtsud.shop/fa/affiliates/?btag=914641_l303106</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/funhiphop/84689" target="_blank">📅 11:48 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84688">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PrPOfUUcEJDZitFiHVRosTuDMrV1fXRj2EGHnVwFXrB_I0uSOG302XgNhQXIf1JXEQMsaIhIdNYRMrEw7GvmmpqlGAVg3rAUus7P2PphOmZTVkHpfYuuzhfSfGco4FwrmdhxR1MxqWPdf3ZnNBnICerB2BOUMMSy8wnRwSIONEn8PzMomSKRikeMtVa9dzo9mHAesoIivXAxqiz6Dg5gevRfiVfXfJF32Oc6RfmZBg2DnKMtELJJ8bsp8QsE-HEOLPzAkBArndwdM488WcBvIgZg2Z2QNXJeJf1CUyxNcjHkROTYhmANML_Bd6tN4QkrdCHdnEGA465VeNok2sDHog.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دم هرکی اینو ساخته گرم یه ماه بود از تهه دل نخندیده بودم
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/funhiphop/84688" target="_blank">📅 01:52 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84687">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NtZVpf3sm_GVi17K890iYuYnBYYAWYvgZDtybu2EH2IrF80NCilJLCGY3raqj4AgUy0MTMgO7zauCZbyZ4KKhqifjef-YiFpjUL4_0TRAjvRnuXmx2uXFxIg8zm_DHlyC4DSdWEoyTU-xC6Mv9Dsm8vwlmEJIOqJy-dvTuANdr2-puCJmqDpe7Biy97QCoFCjvRgQYOTcD_HEx7XiZIBv-Oypm2PTeOcf8Mms-_fyXRqR8AaUMMWWSwPBJkyHEzVILitaWVvFduXvkmhsENApLut9f1yqep8WX_AUeGonTQXkLaHTzJK3Y0QJfcE3m4sq1ol_XzUJyF6N9r7lrM71Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بمیرم واس دلت دادا
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/funhiphop/84687" target="_blank">📅 01:24 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84686">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">داور کسکش فقط به من کارت نداد
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/funhiphop/84686" target="_blank">📅 00:29 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84685">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b32a1ac263.mp4?token=cYJeGccHL1lTKNeTcE05JqLUt-jR2Xs7LM2-3OW9_0DccrZP1wv2jrHk3yoq6cFtZV5pKpqnnx76vlJJW3QwIR8NE_oWomims2f34HuXEIB8vuAY3A_AOAUWS-QPA2kB4suuzim6HffV0JU93J8-_w41woKA-5tDic3xm3KrrVl9jV2pqsag6M-mreTM7tRMdOVDowSHXoKxm0fKWkRqYdjNkH-2HHvfEgr-qKEyYjELZPBg_FBM92dmUF8uONUK1rQSB6sqpPQ28JMx6XrmENRizdQVvtvWbQnaupniufq4Cxed83zdF4dMKmUaLmfZ_J5w6KdSE9nsAf6OjLSDnUAuDAml0vllLTFHnkfOon68FMhdCpwTP639nZ_Yz4oZwEDxWhIHiFnE2nRS6hXqP31rl5aFCG4YSrRDpBjN42-MNKX7aOdv4nCGI5a5qT2mEvWxODNF48VRUgVeOjDYT05UO-QljUf7IE0z5yEJ8PfzDeoaYYWP0nPoiiTkxkdxpXDnhhb6SNVsly_dIqxBQTdwlKRNuxi5y5JrSivwTN1aYAQrvHAAloRVIGAmtCeylylirmEMsGQbCj8mgf2V7TOXeuej9INjyHKcWP3Kl40Yd50jFc1xwOY5UuhiqDuKUSbW6D9MkVSLg4iYh-2RtdWvIp3WZDVcg9NXTY29Jf4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b32a1ac263.mp4?token=cYJeGccHL1lTKNeTcE05JqLUt-jR2Xs7LM2-3OW9_0DccrZP1wv2jrHk3yoq6cFtZV5pKpqnnx76vlJJW3QwIR8NE_oWomims2f34HuXEIB8vuAY3A_AOAUWS-QPA2kB4suuzim6HffV0JU93J8-_w41woKA-5tDic3xm3KrrVl9jV2pqsag6M-mreTM7tRMdOVDowSHXoKxm0fKWkRqYdjNkH-2HHvfEgr-qKEyYjELZPBg_FBM92dmUF8uONUK1rQSB6sqpPQ28JMx6XrmENRizdQVvtvWbQnaupniufq4Cxed83zdF4dMKmUaLmfZ_J5w6KdSE9nsAf6OjLSDnUAuDAml0vllLTFHnkfOon68FMhdCpwTP639nZ_Yz4oZwEDxWhIHiFnE2nRS6hXqP31rl5aFCG4YSrRDpBjN42-MNKX7aOdv4nCGI5a5qT2mEvWxODNF48VRUgVeOjDYT05UO-QljUf7IE0z5yEJ8PfzDeoaYYWP0nPoiiTkxkdxpXDnhhb6SNVsly_dIqxBQTdwlKRNuxi5y5JrSivwTN1aYAQrvHAAloRVIGAmtCeylylirmEMsGQbCj8mgf2V7TOXeuej9INjyHKcWP3Kl40Yd50jFc1xwOY5UuhiqDuKUSbW6D9MkVSLg4iYh-2RtdWvIp3WZDVcg9NXTY29Jf4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ:
این فوق العادس پسر. من میتونم کسشر ترین حرف‌ها رو بزنم، و شما تشویق می‌کنید.
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/funhiphop/84685" target="_blank">📅 00:23 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84684">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">مورینیو رو
😂
😂
@FuunHipHop | FaRib</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/funhiphop/84684" target="_blank">📅 00:04 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84683">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">مورینیو رو
😂
😂
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/funhiphop/84683" target="_blank">📅 00:00 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84681">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/kRz_i4G2SV3MRKN0iBpuyXYx9s6nThZi-TKmPpovoq5g1C01P_DtpmjXofMcK_J3q1lR6td9tbVLIbeLuWl4jMtPLGQ9u3fosBHZCpiN4E_pt5nnh9FvFXLP0WLFlo2i0i6FaSwF--hbAwBMgmSiDLeSNOPUR4JV6_E73i8fyjKgj_o78K5RaM9IErjk2SWAtq2imO3xqq3u9Eq1KtWpDdxzgExPdfKvXMC4pYI6mibLWOU7l5Cri-l0l1yoZjUUjy8y4bF5OT5R__8rRCPAWHLx6L1GXOnXq-BBd8Qs2C-xDRt9N8WeULiVCqGEgav-GbsXK-w9JuyIznznzxRHQw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Ozs-hP02zFSGZyWaVVgDsaPO4UTymqLYyrTWAfHEQ6p4Rr3NMI3Js2H7mTYoja1QnpLVQHxmqgHS9ndp9KGb2DnI6rDiKTyHiO0XeVlUMTnwXmlXPyF5G7amlpSJ7JS50h0R6V2miPALNISf0Xh_zRdrdcCgmFMpxTD4XHOIXugnoPNAa60vjVDuMBsE_bX2YjCMbPiF8JcQ8z9-Li4KtMt4DNzYYc-X3CIh1djX352r7NUhbG2s6eyMxGkZpMAXngu17JPCrN-9uM8WMOCKH8Ykzzm_GFOuCE4j9ODoraQv24r0GZhFPN4rFkJetmU1pyXdjm7vrKcJ2edhQJ0iGA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">با پاسپورت شمرون به ۱۹۵ تا کشور میشه سفر کرد؟
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/funhiphop/84681" target="_blank">📅 23:46 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84677">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/MUD58bRRBeytLyd0Kv3hyySDl0eW_Li6AXgKtbLfA2CUflGc4iwPLMEHnbCjZ-Uu0EoAMbn1VKUHgDPogoE68NDwmOW2JcM38RtA9etGGaz8Pb3a9YHmKx0FbmcLPbpJnoxgVebhj_ed2gEr9qB3KmMpSnaA1Z-7yTY8mjWoRZQl3hsdVEBWmW3VgGgtH-AHLnjR3FNDdX3BkYDom0083x_X5HoTsSPTAHeEpzmMWmx1SFWEhP29lEdRsW9akx78qnYS_cC7esme-9CziBBwNPh28otLLyn-tFRWglc6DgIKABdSS5-ee-DEOsMlnQNA8U4UlbGCZ_2p1-IdQAC0Zw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/T72jE7XsrntlSk9t4-KTu_4zbVvKFSxlUrdwbcGwUNNOOdNGuoZHdKIDa6b6GSFyPLdzPRm27K5vz2RzkD5WKv6SXubA9hd4Fe6PkdS7lnfTknOddh-ioqhL2ferT7caCFFFiieUc5H1qjYUTRtDHiDhvMv1qSnrVSF6CH5teflbGPidE_8aXmHsftr5Cn43TcUVgOCQC87XEQLPl58TGZGLjoWdvmhbztYX6HjQbbtCd9fIwIcFG1pOM6WnWj4gPwI2TPptAWk2JZzX-vVrTRK-F-eE2WrZTO6yky-7XvJONOQ7zpTVXCoRDeP6HCvVODIfvotrS-Dbtem_A4HLiw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vdYKSGzY4-c4InoTaN2xZsZnA3q8K1l3QxjYvq2bYmd8DCqM8xzYc1chqotZgkIOHqB7mBIs-hZF2uxhNPJD6XTXr1XW4WqwMPAzgsm6QusmtEUIXzWPU-om7Or-wQ07sSeWccwhoEJiLarWfbp2bRe9mJTxAlU23vBZUzf8NxNp1qHlgxD_pNzWaIreDYdB9LAiekFYuL-ZFZK-4uw64dkvhhyKp49sEM8fJW0MOtof78eRgBEMJlyG6gcAemZoqmbip2SnOyvr0WxCsNtiMkSdZhe_yvjLIu6TL2kn0sQjpppN7i4k4dPd8mTslQw_I4xwzCRZHBk0jMOwSWPoEw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/cTC3Y_wMvhoo2J22lP5IZNYKeqMaOaffBs9xbphlqEag1HmAB9k_xlaDx_xunxucD1DtcOinXu2g-hLuFbB5wwovlcjJh39CoH1_239EfOGp28RoPffJJ6vGQNByrf1g87p0ObP17sJ6yC1RATc1pCxyNB2jfe13Cq0UegFw-aayrSEjnjpJQ2sToUKmS3Hc_4iG_85-8HjDQSPgRXF3NK0lqc3c2OBnkQ6WIrYZuKsDJrXnOwrcG3FgKueOV9iB14XDOmTXebpejZNqOJzgvjC-LoZC66wMMb_MVf5rZkDKtQcdhIkSFP8rv7GZ1oJ5oY2bCqK1Fb2wJOehoI5W7g.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">بسیجی‌ها امروز با پرچم فلسطین رفتن دم در سفارت فرانسه که به سرکوب خشونت آمیز اعتراضات تو فرانسه اعتراض کنن.
@Funhiphop
| Nima</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/funhiphop/84677" target="_blank">📅 22:17 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84676">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cd88d22e31.mp4?token=Wa-d6f7xv4q-I7WAOEC4w7RHRAywt6GiGvODADbgUYp_4vZPsg7ndCtywMVRuS2qBF3mEExj3HXlfI-1_Lb7WCt68VzkBc9NNRPsmyacQIR00Kw2t8ijfCIhgk3p9OZgOnu4ytlGCZXzmSYJQn3Nk5wloJyZhFotPoHGoJJIZ_RsAB2rOHkV2zSewI_weLy1gN5pz7CMeZExSTG84HReudzHM0-bk9c2MuT3QVCJYVPx3XlBqYUJjBM0Vq12VYUT0huwnk1xpdQQP0dEpud7_TY4eNKZg4BGYPwj5AJwiAPtbFcGxBUodWS0-rMMnjg0WQvSvNBWCH93-x9L6WCivQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cd88d22e31.mp4?token=Wa-d6f7xv4q-I7WAOEC4w7RHRAywt6GiGvODADbgUYp_4vZPsg7ndCtywMVRuS2qBF3mEExj3HXlfI-1_Lb7WCt68VzkBc9NNRPsmyacQIR00Kw2t8ijfCIhgk3p9OZgOnu4ytlGCZXzmSYJQn3Nk5wloJyZhFotPoHGoJJIZ_RsAB2rOHkV2zSewI_weLy1gN5pz7CMeZExSTG84HReudzHM0-bk9c2MuT3QVCJYVPx3XlBqYUJjBM0Vq12VYUT0huwnk1xpdQQP0dEpud7_TY4eNKZg4BGYPwj5AJwiAPtbFcGxBUodWS0-rMMnjg0WQvSvNBWCH93-x9L6WCivQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خمسه میگه به خدا من بادیگارد ندارم چرا به من فحش میدید
@FunHipHop
| Mehrdad</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/funhiphop/84676" target="_blank">📅 22:01 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84675">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QybGDGj2TL7SPiDuUgu1FOvqSfwHNhDjVZ0yw1B-V8cvNlsCqQN6xEnljijBu7cL7082YOz9CeZiSk8dz_lV8kE6ISMdi-U8CVjRzddG3wYknWn0-ggvUQocWrOg16jBhQxNkifwWFBYA9Zw4o9ATxJ3utvsQHdbP-r4exzzJr9WYq-vb6yH9R5WVPIdVhSovUcZdT1Q-61G7KzD4-s-s_PeOFNI5YQ95Bc6HglIMV-heSyFA-2AOpHfnwkUA_5fGW4XuaZGMRgs_PDKyFbyMuKBsC-Eg1_ns4HouEhLFLsAkzzwYoVzN2um9S7DPWKCXrRIORt6Q_7dRcWBRyaeaw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پاره شدم.
بعد از اون کامنتای مردم، اسطوره نوید برگشت به تیجی گفت شما اسطوره و مرجع تقلید منید و افتخار می‌کنم که باهاتون تو یه خاک نفس می‌کشم؛
تیجی هم اد استوری کرد نوشت پرچمت بالاس
❤️
@Funhiphop
| Nima</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/funhiphop/84675" target="_blank">📅 21:19 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84674">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from“Creator”</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">Talangor</div>
  <div class="tg-doc-extra">The Creator & Lickel</div>
</div>
<a href="https://t.me/funhiphop/84674" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">ترک جدید The Creator و Lickel بنام تلنگر منتشر شد
🆔️
@Amircreatorrr
🆔️
@Rapkadeh_official
®
🎶</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/funhiphop/84674" target="_blank">📅 21:09 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84673">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from“Creator”</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/clnPzevm3AUfCtnXAMuG0HcQEzhynQAGQWHNLDuYMOI4d1-upWA94NzP84F90wMqJyQatF7sUSrtcUQkA1DpRMDnYRr-GU9ylR5AaFKxxnzOYp7QA8CCWYrKrlhEN_Shmq2OFtUriCZZuasABUr3JBtUFMMoZU4HX0Pe1xKlSeWlVRqPjvb4RRFOx5aTYrmYECv2YmvWK1WRpOSlh7Vvwq9JbGcGemNfJBB0Ooe43EZ4fPNeaK7uhivMmd2FrqRhgPv8XbkRIfUl6tkYSlNmtghjk3daquxmKyxWSSYB9Jb4zLxrCrRx2ayCt6wyzJSoqy8SXIcYrkGai3y7ysT1FA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترک جدید The Creator و Lickel بنام تلنگر منتشر شد
🆔️
@Amircreatorrr
📥
Download
نظر شما درباره این ترک ؟
عالی
👍
خوب
🔥
متوسط
❤️
ضعیف
👎
🆔️
@Rapkadeh_official
®
🎶</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/funhiphop/84673" target="_blank">📅 21:09 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84672">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/25eadd38c3.mp4?token=r4NKKvJKdGDm-jFaeiHQhMaR0AILyySmgHof_em2L6Tuj4sSNm279ZkZU68J-hDn7QSNAN_obYJ7YmGd6VoWVr9FaVInmEoxn-5gYmDUVlf6EVBhAV7VaE2Udm8SWX6mZgjnz2JcPg1SKDyscaeE08pvG_iKp1ZKzyPQ1q9_n-uzLnnmBu8pQnx1UcAcuOBESPgbZTx9fSiPN7rpwbKGtes64OYM764OrH1TnUv2r453awyqLY0kCoqIW_csIRfMkxvg0odr1YpR6MxK-X2emBTMZ9vxP_I1jvib0z3-nRlvwgG5Nh0wqoyrkD2kpk6RMS_OfBDet_9AmqFBFFIG8w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/25eadd38c3.mp4?token=r4NKKvJKdGDm-jFaeiHQhMaR0AILyySmgHof_em2L6Tuj4sSNm279ZkZU68J-hDn7QSNAN_obYJ7YmGd6VoWVr9FaVInmEoxn-5gYmDUVlf6EVBhAV7VaE2Udm8SWX6mZgjnz2JcPg1SKDyscaeE08pvG_iKp1ZKzyPQ1q9_n-uzLnnmBu8pQnx1UcAcuOBESPgbZTx9fSiPN7rpwbKGtes64OYM764OrH1TnUv2r453awyqLY0kCoqIW_csIRfMkxvg0odr1YpR6MxK-X2emBTMZ9vxP_I1jvib0z3-nRlvwgG5Nh0wqoyrkD2kpk6RMS_OfBDet_9AmqFBFFIG8w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ببین عرفان جان میدونم ضرورتی نداره من الان این پستو بزارم، ولی تورو خدا برای یک بارم شده یچی بخون بشه گوش داد، من خیلی دوستت دارم ولی واقعا نمیشه گوشت داد، لطفا لطفا
🙏
🫀
🌱
🌹
✨
🌟
⭐️
🔥
🌈
☀️
🌨
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/funhiphop/84672" target="_blank">📅 20:47 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84671">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">🚨
ترامپ درباره اوکراین:
«پیشنهاد می‌کنم اوکراین رهبر جدیدی انتخاب کند که بتواند به توافق برسد.
-به دلایلی، زلنسکی هیچ‌وقت به توافق نمی‌رسد.»
بابا یکی جلوی این کصکشو بگیره
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/funhiphop/84671" target="_blank">📅 20:29 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84670">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">وضعیت فرودگاه ریاض  @FunHipHop | چمن در خاک</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/funhiphop/84670" target="_blank">📅 20:23 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84669">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/E5yO_kZDXjTKjRnnvra1MBXS_Hkn1D4X6IhRuKJzXZ3a2-7sN5_BTdC3HdGKQPCD_LoiiOZPUA0gkvvbaBe-zwHOSv9cWWrjK9MzND0vvyj4KRUPWXOtuQDclar1RnTd-9qfMts9IIKUbLJorpp4pzKqKscuFbwdM1CL-oVEqsAIRSdnJ_mOPlh6tTD8NAl5JO2G9gxL2QH3IKppjtOiGlVSFoNnQh2oDPi9d1_Uo-JRQt6QWGqgh6-w-jJULEDsaSoTbkpwcvJ_ZT7hoCNw-uoidEtd3QddqJWbakoRzOsIshHA2o0Gdy-qRqWU6rs6E5576hVdOOxdGWaKKupRKw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وضعیت فرودگاه ریاض
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/funhiphop/84669" target="_blank">📅 20:22 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84668">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">شانس
0️⃣
0️⃣
1️⃣
میلیون تومانی خود را در بری بت از دست ندهید
🔥
😎</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/funhiphop/84668" target="_blank">📅 20:22 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84667">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/n53UEGFsNXz4Cc0Bbl9BjC-679bEVGVyWQ6STFRES0QaBWxuZsJaSXErj7s6j-aUyFXQK8ctqQ_udrLV-CBz_Sfb6fnNmLXQrhS6uLUbIuocA0u7X8n0uuftr5zgXpNz5d7nSYEqR0HgS2dm0um0eQ1LYXN6xzNaRv6tz3olQs53DoYrzwv_zBv0l-nwjYJlpSU1MXTVvz-VcuJuhDYvcOL5yEl-_Qig2UVdA2-RxCZSpe3rRCbm8LJXmRxIHwnfXA8d2fo114ZwKgf_e-S6pINWsGQWoj0B0eBh_IcEb7bzBwhiRwohVbB_LeQnWZVQnmIOeIsjQ_E7yAwPltvLdg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">😎
۱۰۰,۰۰۰,۰۰۰ تومان!
🎁
🫰
💰
فقط با یک ثبت‌نام ساده در
BerryBet
می‌تونی وارد این آفر بشی!
💰
✅
شرط رایگان دریافت کن
💯
کد طرح تشویقی:
888
💸
شانس برد تا
🔢
🔢
🔢
میلیون تومان
💸
🕔
همین حالا ثبت‌نام کن
G18
🅰
🛒
ورود به سایت
👇
✅
https://ieoruyxtsud.shop/fa/affiliates/?btag=914641_l303106
⚡️
کانال رسمی ما در تلگرام
👇
✅
https://t.me/BerryBetOfficial</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/funhiphop/84667" target="_blank">📅 20:22 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84665">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4aae2137c8.mp4?token=ECLbN9Qs30CS1mSpnHLn5VZq6PFSJXlITW8guTJkhPGdkHQ4y40hpRzJ8sAGmsxUOyEVcVJYPPYed4mGgtV2zHMmYIRZaHlDOwtpoE3rOnliOkNhZJ9OCqmHjxitwDUSBH4uJZ2UqBiBmTkZNpuDIfHI2LLdh0WOve-Qz1izfHgp2kHQVy7QofDJYgJIxTol4gagqBtjtjML1k9mFLK7iCIHFzD-t9Het95by-dOfpKll8rUx6YyK6G0ssbTBBiqlHF0QNHj3zHctSgtuMkxOMEkrBiAFxrhlUcKYNVoGVzlMyaGB6DYF9ZFys4brihShGQk3qp8uyrZRpJnOjQbuw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4aae2137c8.mp4?token=ECLbN9Qs30CS1mSpnHLn5VZq6PFSJXlITW8guTJkhPGdkHQ4y40hpRzJ8sAGmsxUOyEVcVJYPPYed4mGgtV2zHMmYIRZaHlDOwtpoE3rOnliOkNhZJ9OCqmHjxitwDUSBH4uJZ2UqBiBmTkZNpuDIfHI2LLdh0WOve-Qz1izfHgp2kHQVy7QofDJYgJIxTol4gagqBtjtjML1k9mFLK7iCIHFzD-t9Het95by-dOfpKll8rUx6YyK6G0ssbTBBiqlHF0QNHj3zHctSgtuMkxOMEkrBiAFxrhlUcKYNVoGVzlMyaGB6DYF9ZFys4brihShGQk3qp8uyrZRpJnOjQbuw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">Voice message</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/funhiphop/84665" target="_blank">📅 20:13 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84664">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">امین تیجی جن زده شده.
@Funhiphop
| Nima</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/funhiphop/84664" target="_blank">📅 19:55 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84663">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">چرا حس میکنم هوا دلش میخواد سرد بشه ولی روش نمیشه</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/funhiphop/84663" target="_blank">📅 19:45 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84661">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/kw_OPsNjRUGumxxcINiNyCYYK7l3AJKLTUZaJsQp31R4C-xlkJ9UopO01I8zpTlrv6oEKzXdQTev-TRuS7Vn8Gup5FPxyeQnjDENfPr4lkZZVCNmiBOwCCxl7XQhfQSooOybo1c8YeiR8itsBu7glp_PYmHKDpVJTOMK1BDQxAnPQZ0Wh_UwFmbPjGH3M2jIQG5M1spovxHi67EO6WMnpMhEdjYVi7WTHSt4c6eEjXfU-exnPPc0BB3vGcDXXVpQu7NKipTDW-ZqeJbRd0uewnVRYeZQLadwwlsJWiw7Qem7XqHkGGwAcwuvTz1gaRFqmeokJbX7h0e1wDlcIulJyQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/rXuB-pMkS0z4QUlHycdR68jzgEi6Ulon_pr0wBm1tfw9REBOr4KrkUb9zMfvOOZV6SJJl9RvkgITMlnde4z9W_8ilhLW_dUOBJo4nYCUGRpoNQ12wUNFTloVgNmjUDrUw_l2NC9A48Dua2A-LVgEsysHxafMh7T2mDHwXi63x__HKZJYPYYMvLocfbUQspqTGdaYj5IW9JUS1N0PgUbWXna8jLrnW8tIy4NiEKQZFQGeBASkoXsXKkShuXatPFPBBt2hD6UejJjfFZoBYSBwhFfW6wLKru6Pm3RyAvA2R1XHm3jjmoOUhLpzOsUVOxxzR72a1y22SV1tgmAzdqA0mQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">کریستیانو رونالدو موقتاً از تیم ملی پرتغال محروم شد!
فدراسیون فوتبال پرتغال بعد از جدایی جنجالی رونالدو از اردوی تیم ملی، تصمیم گرفته فعلاً این ستاره رو محروم کنه.
کمیته انضباطی هم رسماً پرونده رونالدو رو باز کرده و قراره به‌صورت فوری به این ماجرا رسیدگی کنه.
هنوز تصمیم نهایی درباره مدت محرومیت رونالدو گرفته نشده و مشخص نیست تا چه زمانی از حضور تو تیم ملی محرومه.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/funhiphop/84661" target="_blank">📅 16:50 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84660">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">کاش آرتا و هیچکس یه فیت بدن، هم فنای آرتا کف و خون قاطی میکنن صدای اگزوز خاوری هیچکسو بشنون هم فنای هیچکس کصخلشون در میره صدای اوب دار آرتا رو گوش بدن
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/funhiphop/84660" target="_blank">📅 15:54 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84658">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ijXpebEaBrSnDQ9deTqcU2vmVyMYaDEVTrCiKpmhozKzXztI1M8l3pJYjhA-CupFKEdpMV7w_vaJVf4EQLI6EWREWM-laLInrs4Hd_rc03KyXi7lOQyxZlDHKvXxH8z11bhZefhm9H_5EsMek05RyYwaa_dnQFVLWig1bot2t5iSENSIjLt_IMeSrO8vocDQU6ras4H5JqAmhAd7s_9YU2W7Hx19kpAFw8e05VN1ZT6SqmH0FJyb05Cx50_gGkO7_dqAEre2ll2kDrwNVR3EpBsO4EsAQBkZ9EgvWM66zOTPk9gZUn1yu5-ab00N7czZngWqcvKX85XX6ZfLq6pNwQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/RaL6uWRsfuhNoxHzj9b3kJWqPLxsaUAFk74rU1IygrxeDyR21eTW-za-pavnEvGbyMHVfJOKNrfLE6O7ok1UCCNEwpnHflVZ_Ge59HRwzQDM6Kafn0TVsFQRovL4EDbBcQYKovqiH_A4kRdTjsBLl7Sq78xyoSjZNAGRFxThtY132FBUPPUkUOVWof5KNWT2UtMWrFVMPNfHJjvLZ_9h_rVgkPPycUgWy1Mgvwxwi3JXLMEoK8EIHdJFEVVTxmzk1kU5quavQwcuKKjWq9103G9l-EH9tYUFPMFZAtbokYg01kqRNO0PIlBsinzVqrhFQOUqa4AgxZPP3NdHy73gKw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">سوتیدا، ملکه تایلند برای نخستین بار پرواز انفرادی خود را با هدایت یک جنگنده گریپن در استان سورات تانی در جنوب این کشور با موفقیت انجام داد.
وی همچنین خلبان بوئینگ 737  هم می باشد.
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/funhiphop/84658" target="_blank">📅 13:59 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84657">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">حصین جان جوس ورد از اون دنیا هنوز داره آلبوم میده، این یاد کیریو بده کونکش پیر شدیم
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/funhiphop/84657" target="_blank">📅 12:00 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84656">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">در این دوره از تاریخ که ما شاهد امپراتوری آمریکا در دنیا هستیم و دیگه بریتانیای کبیر و شوروی سابقی وجود نداره، هنوز عده ای وجود دارن که کلش آف کلنز بازی میکنن، منم جزو اون عده ام، کسی کلن فعال داره؟
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/funhiphop/84656" target="_blank">📅 11:40 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84655">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">ترامپ:
ما گرینلند رو با قیمت مناسب به دست آوردیم: صفر دلار!
کصکش املاکی
😂
😂
😂
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/funhiphop/84655" target="_blank">📅 11:20 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84654">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TZ3Osm6cRTEUohz8IUOjFgPRa8RgwZwNtxFGLXDOD7FrFFc79J2wwnKSanwfIKc1rl78f1aFqJktpGES3gCPmfenxvPDzCi3GfHLPvfSQ994_DrSsYr9wei0CiBQiu8gpxGIxR5ZGjCczlufTIbwFmgAvTWEtGC-S-nC6pTxa_8k161cjw1pJC8sr0i4zUZZ5ivwXdcOYClSeyZr2ujObu6uptu8K6Yr4OjabffPAaP1AA5Cj0T-CwXPWYphoK0zItpl8D_accyJhly80vrgj56kF_36WZgPFrnP1bU3OAHvCLxpTGRYYSqcjMpQIjNnXESl7vC8r2irdNBgeGTc_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">من میدونم تا مدت ها قراره اکسپلورم با این تصاویر گاییده شه، فقط بگید چقدر طول میکشه، میخوام بدونم تا کی اینستارو باز نکنم
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/funhiphop/84654" target="_blank">📅 11:12 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84653">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">همین حالا ثبت‌ نام کنید و از بونوس های جدید ما لذت ببرید
💵
🛍
👆</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/funhiphop/84653" target="_blank">📅 11:12 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84652">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SkdtTNsDFVygUm-qqCOL_SN0TMyUKRtc7fPzAX-WViRRQjRX8mwsp7rl5hq9CP-RermsqkAnu6IU-JKFsCNhuzU7MpIb-OfgYIUx8CDo2RYeZ6H-ZDITXgNP7Rwv_ypPbW7iHWVx2e2525z3IhqYg_9Y3LEP-LiHUxmlQK0Qv89ZWKIaaUCf5S_b1qFtuWv9tdsM2BV3u4PeanS8erIz7-KPPhrqGU37xk8eCsiGEeZrcwAlAX7I1QOXGLBLy5M9y4nuHXegvwxnJYhjWXXFbeihVzbmn8z1Zqzfk30x0kP-yAIvihpwUi6WHX4FNtipZVer8C_kyh9VUXEtDdxndQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚡
بری بت | BerryBet
🔥
مسابقات امروز
👍
⚽️
چلسی  - بورنموث
🌎
ساعت ۱۷:۳۰
⚽️
منچستر یونایتد  - تاتنهام
🌎
ساعت ۲۰:۰۰
﻿
💸
ضرایب ویژه و رقابتی
⚡
پیش‌بینی سریع، تسویه آسان و پخش زنده مسابقات
🎯
همین حالا شانس خودت رو امتحان کن و هیجان فوتبال رو چند برابر کن!
✅
۱۰٪ شارژ بیشتر برای روش‌های رمزارز
🤙
ورود سریع | شارژ آنی | پشتیبانی ۲۴ ساعت
کانال سایت:
✅
https://t.me/BerryBetOfficial
آدرس سایت:
🅰
r18
🔗
https://yewirkxojf.shop/fa/affiliates/?btag=914641_l303106</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/funhiphop/84652" target="_blank">📅 11:12 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84651">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4795cf2815.mp4?token=RBRw1wj5Qr7BwF09sUIqSYkxkc7EtQoFTgRMZ2lIVIA88WHG7Q16ZDvbIy3awpVp-UxfacmlkiYj_kkKcWsD7LSX7aSfD-DWUCHFQiPI3_UgDTHEBKL6DtVuSIcv2iFPPukIFuoZNgcBAt8m7HoZXui0giRRTbNtggxatkBiLAU9uAr9m5OhdIdr7Trz0Fms-fBo9iuEbcVNBwCEklj2FmS70DEJ8GZ6DXJp_6Cikp4-t_hn7PeKXL5_-91gDFlaYz4C7V_XyFz0M4WeJZ95HnOlcSduoR3U_5zwT_Gg8IAMy8mpAJtnojpOSC39JS68-ZldN2dpEb_gnj0fDp1CCA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4795cf2815.mp4?token=RBRw1wj5Qr7BwF09sUIqSYkxkc7EtQoFTgRMZ2lIVIA88WHG7Q16ZDvbIy3awpVp-UxfacmlkiYj_kkKcWsD7LSX7aSfD-DWUCHFQiPI3_UgDTHEBKL6DtVuSIcv2iFPPukIFuoZNgcBAt8m7HoZXui0giRRTbNtggxatkBiLAU9uAr9m5OhdIdr7Trz0Fms-fBo9iuEbcVNBwCEklj2FmS70DEJ8GZ6DXJp_6Cikp4-t_hn7PeKXL5_-91gDFlaYz4C7V_XyFz0M4WeJZ95HnOlcSduoR3U_5zwT_Gg8IAMy8mpAJtnojpOSC39JS68-ZldN2dpEb_gnj0fDp1CCA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خداوکیلی ۵ سال پیش به یکی میگفتی پیشرو و هیچکس رو قراره یه روز کنار تهی و ۰۲۱کید و آرتا تو یه کنسرت ببینی فکر میکرد مواد زدی
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/funhiphop/84651" target="_blank">📅 09:58 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84650">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/258be0442c.mp4?token=EYcAtRs69buwHYYxAiF5YRK7FD9SIRhaE4IMqqxmPt4QzsamhecyQ3K1qVrnL73J_beihbdboZnxSnhLmAOrcRjG7Ti6XaBB629wO-NY4BmEM0XefvIHqsWHF4W80d15Ce3q00jDOn0rba0i400OddXmCFqS6S5OmN0v0qe9uZKjUIsfbdVCuZVROtgp0-9o2HbNWG8Hr7Jhc_13Oslw9NyxGvcLXJ-boBnM0C0DwWW-etPFM82InaEA1gaMj_4T0EMam__6qFMl4FITbTKw6o_0tggq8J8ibImOPkt6w481vFNUPX-wEexHKcukLQeowsJZO2fmQug2L45jGGvBHQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/258be0442c.mp4?token=EYcAtRs69buwHYYxAiF5YRK7FD9SIRhaE4IMqqxmPt4QzsamhecyQ3K1qVrnL73J_beihbdboZnxSnhLmAOrcRjG7Ti6XaBB629wO-NY4BmEM0XefvIHqsWHF4W80d15Ce3q00jDOn0rba0i400OddXmCFqS6S5OmN0v0qe9uZKjUIsfbdVCuZVROtgp0-9o2HbNWG8Hr7Jhc_13Oslw9NyxGvcLXJ-boBnM0C0DwWW-etPFM82InaEA1gaMj_4T0EMam__6qFMl4FITbTKw6o_0tggq8J8ibImOPkt6w481vFNUPX-wEexHKcukLQeowsJZO2fmQug2L45jGGvBHQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ درمورد جنگ ایران:
آنها یا همه چیز را به ما خواهند داد، یا دیگر وجود نخواهند داشت، آنها این را می‌دانند.
@Funhiphop
| Nima</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/funhiphop/84650" target="_blank">📅 05:06 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84649">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">تو تنگه بزن بزنه
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/funhiphop/84649" target="_blank">📅 01:21 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84648">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">اوه اوه
روسیه تا ۷ اوریل سال ۲۰۲۷ توسط امریکا معافیت تحریمی گرفت
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/funhiphop/84648" target="_blank">📅 00:09 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84647">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/n3NtNaHVxxDya6XTNE6xyh1sD_bZ6zmOtI9trG3BhbDnaiDcF-aSOeOrGDkiIf42NQvG0Csm4NP7y_-IG__-pjaNa_ozIb2mw8EKZMXAZWLZB5GJ9drwRkPY-76HZyoJuXTu0P1m6_SbViFp-bFspp3lPUYTpKoAnKLqqkli0M7_reojXQhz17r64maVY8e2SYWw5oUYbXnXzKbuVgfzjxkO9a_rrI8iPQKmGLudaPramGvlHQX_XlJqU4wrXDcX_0HUXcdCib4V9WfNhZH9cWVP_VkszDd180jppIk7J4IydBmf4UjBE27O7iq4GADr3zXqyySBqEtM6wFmq3nn4g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هی داره یکی بهشون اضافه میشه
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/funhiphop/84647" target="_blank">📅 23:03 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84646">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LzeSfT-fRsZdm6oCar9e5SnpPwUMCarpAosYqFdAzDHzMZh1a1B5THXHEF-C9hH3dkpFMDAqZn0hihwhjDF8uXUb-6-0EPRnQc7msaZSgKYh1WfN_T9Pw5zFarhP38zoYcLYlLq1XACwEc2vMqx4dMBeikqluKhW-aVXQ9V2SyWb5zs31InOFDUsKT_1KRvxtXL8zaahU_qctSShdmE_VPfBKH5XXWlwQtaQzVuiZCNMssILOntRxPeQDy6QId29uaSs9TERN3eCNwo360nwrNbWKZhrpcyt-WYNP5IO_o_kyIGxGU0XRdb5AqkPduEYLAceS-OVBiCBMNZSIJYN8A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">الان فعلا پست ندارم اینو داشته باشید تا بعد
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/funhiphop/84646" target="_blank">📅 20:52 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84642">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/g-M5z8l_jLx-Y-vaCdXUmpP2WHXaHEz1EUuOhw29F9FjF6G2N57j8dmaHoqc0mCj677BYxotIv90c8pPkOyD_0lGIXAEGeh4qO0uRbf4adwCryotHu_kofVjSChz3KqEBveYCMDLviTv3AldfRrZt659ZJGsyqBoLDH8NIDLeiBzqUnBcL17IxvgSYxCXPRCbBh_XQ-p44j92FROoMySlo4_dbdrpGa42QRZLB9zJTZWza-zf6lu6DVcD-ZpLxL-T7xAyUaInpqmPrro5tZghybZxK2i2KSn9ELT3MUa9G5T9mlDKId010-om-kXYMBfEoBYvUiG18OlJbmNFLivHA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/gVLq0DYiy0KVa3iRLlOXTbGqpnLHRXlW_BjPV_i0bgCTlBOIbqkklfGM45zwU5eibpv-oRx5uzVxqLSW1UgnvPmJNx0VQDMsvD3OYnQr-nPNf1m3DwME3_631pU23bUGXsDb9JwIdSMisCHuU_7sW6vkqhH4A8m5hutAacgbFThoPfsvxYdX5CRS-n4XD8F86q2uP7wCWa5fvFJGPE5S_NAofyyEsdwoqxOITq3M4zw-G53wCkE4SEAVX4mflXB6xywKBeuFhOrBZItDQ7M2ZAft0MkrfMMGDsF9miK9XjJCxJ6mY8kVxntwWhkYglErSlBECjoJxfomSWn_VIAdEQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/i0qQO3MuFM-gXYUPn5x8aDH136l4Q2VkmZRRupZ7AZoQg_fPOgKD1bSvdJIhfa-UMLMl9H2UDiGcHnnwqTC-cpYkp-4ojkHMhID-Eof2TRM34xoUJQ9l16XGeZPhOXy-SKEMC9R3AfMZTTuezAX1qrZKe8iKhblnDuNCwesItvNFUJg1VTLct26pGXWLPu3GEs2NFti-gYVg4H8tY5ShszOx9hCuA-w-UyjT6PSh9imyHvCjCrlxZsw4_eKS7KssucGK647yU38Sa9znGM71QS3KRyfJgBN1EDivKove45dnkg23p9trUibQF2KH9LAt0HBzphw78huTfqDQZ0JrIw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/O3QL7k2I2CgQ32FK1T-lHsJ6NHwDsHcxI-nH6y9B2nzObytRt2vFsHLT4mh6MgNPxLqrlc177t96eiXLlLKQZ2yHY_2Qmg4XFz3og-hWGDf9AwXBIMa1yBSYho2p4EA7lLiTkH-TXE-hftsE28VONdUzgin63Y2cARFTncvLqx0PQGadotvjrqmbvkjpdvnrLkR4Ms7kY4BzClj5wRCrPWuxYRHdwmXDQVlRqFZ1Oecgrj7nCY43c1-zKRMKOkw1eUjbjXFiHWdI3tta59rS551DCOyhLZRs2OyjY6EsYMuEOzCwIEmrxM4mY4VTf1S-1DjZRPlN1mhLGG4RBXwDlQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">همزمان با ماه کامل بر فراز آرامگاه کوروش بزرگ، این اثر هنری زیبا خلق شد:
@FunHipHop
| Mehrdad</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/funhiphop/84642" target="_blank">📅 20:30 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84641">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TX9fFXuOzcERwCxeH_uwjLzfpoud0dEQ8Hi3izmu3n37i5yEiuEikCZEhhdPoolDVadvDA1i2nGLJJycusVbN6aDAHGiCV_khY44V7T_bu-_YjD7Vb3I7jVszJYYJR98js53wdavQdfBQMKM4kiG5HQciqi8UTlfgQuPFsJEndEqgBGosrGYOUKVmgeyfFOWdC6Aq2tlRLP_9Skn7hpUwbpQERC5YR027N_g_i5nTmx8QnKo4ZAPDIKmtnk8fBfEHdRMa7GaMFBYKF4W10ZU-0q97d4TwqGkCjrfS-lCR3BFmzJeze4wlqpeUdNA5zysCR7zHTIhzNsvt0PyC-Xqow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چجوری مصرفمون از خود افغانستان بالا تره؟
@FunHipHop
| TemSah</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/funhiphop/84641" target="_blank">📅 20:28 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84640">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/V9ID-pkDHoBjw40WNnt1-2fOD_3s9hTfhrnoDtNT25zbYBaj55Gl41pgtS1Co92a_cZ5Uv3zlzQCuPaEhghz-b0DqTYe4__H2nqvZ9HifheluizNoZ9YppBkGWuMXtBIz5hLkGQynihRQDtZSFpqB-ppDnvDKr9o4_697RMk9Al2Vih0HtFwvadQtDLwY-NxFivphOTtK5nwpqPNyH1kBx7b641jwUdyPeg2HpIUmxxc_6nCJgVBdhDSUDCsqmoW04kI3jJ_CLiXEcPPzw1r-YtAHUO7LkKrQXarbFYm39Kxltl0XcesnukQ6qyBm70p97VNm9nNeaIHjIEhFr4Qvw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">😎
۱۰۰,۰۰۰,۰۰۰ تومان!
🎁
🫰
💰
فقط با یک ثبت‌نام ساده در
BerryBet
می‌تونی وارد این آفر بشی!
💰
✅
شرط رایگان دریافت کن
💯
کد طرح تشویقی:
888
💸
شانس برد تا
🔢
🔢
🔢
میلیون تومان
💸
🕔
همین حالا ثبت‌نام کن
G17
🅰
🛒
ورود به سایت
👇
✅
https://yewirkxojf.shop/fa/affiliates/?btag=914641_l303106
⚡️
کانال رسمی ما در تلگرام
👇
✅
https://t.me/BerryBetOfficial</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/funhiphop/84640" target="_blank">📅 20:28 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84639">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LOgi4lWr-y8_PPs3O1Yw8CpmCwMT5zXf4QURkihDRjtBpc4rrXxjvAYAECSjYkGk4mdcktpSSm0aprsS4lPlopffMq_S-yVjw7AZ98gtVyfkwMzEkuT4DeqkzZwXO7b5NsEZKewXMLW7K97hqhOcbDdjxj4aPYDhseBeDuI7sFoMy_s66iR2X4QeiK77xuOg1paRHnAF106nfNKZiBFGuiH7M0YQcEPAor469SnV2x0d09-29lrbBDzKU7XD0xYTW78dBrNmXqApag8nKgKH_O7ZwnzI1g1cMNIonr0tqMemHR9vDiefq16roypcxPRsPAXz8fzqq7BD4U2SjBECCQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خدایا خودت رحم کن
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/funhiphop/84639" target="_blank">📅 19:23 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84638">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XnFQ46A4xYaE34IajcyJxPyEXO93_REAM9Nu3RE0tax1_aODbuUzmkBdD-NlpBzq8em1XMGDxGmIq2TFyQ8inUbrM9J-Oy1sSJzrqZPFX2XVytIMts4NU0-S5X1iezKdLjNJA5ktrFTWmtbOe5LVa26MOn8Vs4-l5cVqERNLil4tnL-NJBWci8CJaI-7QuOEDiEyqjibMtjhk0WLpxgqW_Fa0UU9GhZrtOBRzDIinEbRw5GuhMK21RyytfhcjfPjMQGUN6TwO--go0ACKCCrqrEA9T0jMa5DW2VLsPcp0pAPx2MFP4JjikaqxPTgZ_gM9Cq0_NWEC6s69zOOF2GjSw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عجیب ترین چیزی که امروز دیدم
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/funhiphop/84638" target="_blank">📅 19:11 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84637">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">دولت آمریکا در حال رایزنی با پاکستان و ترکیه برای بستن تمام مسیرهای زمینی ورود و خروج از ایرانه.
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/funhiphop/84637" target="_blank">📅 17:59 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84636">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">خدابنده‌لو چقد شبیه رودری بازی میکنه</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/funhiphop/84636" target="_blank">📅 17:42 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84635">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">گزارش‌های اولیه از کشته‌شدن معاون اجتماعی انتظامی استان در پی انفجار مین کنار جاده‌ای علیه خودروی نیروهای انتظامی در منطقه چشمه‌زیارت زاهدان حکایت دارد.
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/funhiphop/84635" target="_blank">📅 16:59 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84634">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">میرسلیم، عضو مجمع تشخیص مصلحت نظام : تیبا در سطح ماشینای معروف خارجیه و به راحتی می‌تونه باهاشون رقابت کنه.
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/funhiphop/84634" target="_blank">📅 16:04 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84633">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">شب جمعه خود را چگونه گذراندید؟  @FunHipHop | Arash</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/funhiphop/84633" target="_blank">📅 15:45 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84632">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">بچه‌ رضا پیشرو یک ماه دیر به دنیا میاد، ازش اجاره میگیره.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/funhiphop/84632" target="_blank">📅 14:02 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84631">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ev3BQB0gDKvgFV35Lo2DRsGHurfyGQsMlfRxQVd7ZMcHhyIcSS4gOREjEZWQr1B1LVm9lNNjGSHsxA1IabHuzCl48057f9xyBcOhXncSpUGm9LljVp4S2a_hpoLSDRhXGLEArPfwkUqpnjcflwxEOTNjCCV1Vw59D-OGlxJP_8a8qLboXG2PgLun2InG0eUO2HMqd5q0vTdDq6s0V5Q1AOtdKSmpRvmEozhw4ATS6Om95Q8VtbJtFEizRhxd8SZtioVmoBhL5t_w93fdw6q7oGAiE01WlBSc2824WXlSFvR1-Z1z2KTTAvkw7AnOexGJj4Ua69yG4JKpWLOCTyFICg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ماشالا حاج اقا
@FunHipHop
| Mehrdad</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/funhiphop/84631" target="_blank">📅 13:17 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84630">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">سر همین اصلا به مشکل خوردن، پیشرو زنگ زده بود به هیچکس گفته بود داداش مالزی کنسرت دارم، هیچکس گفته بود خوش بگذره داداش</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/funhiphop/84630" target="_blank">📅 12:43 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84629">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">سر همین اصلا به مشکل خوردن، پیشرو زنگ زده بود به هیچکس گفته بود داداش مالزی کنسرت دارم، هیچکس گفته بود خوش بگذره داداش</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/funhiphop/84629" target="_blank">📅 12:39 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84628">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">من اینو صب دیدم سریع رد کردم گفتم ای آیه</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/funhiphop/84628" target="_blank">📅 12:36 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84627">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromᴀᴍɪɴ.</strong></div>
<div class="tg-text">من اینو صب دیدم سریع رد کردم گفتم ای آیه</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/funhiphop/84627" target="_blank">📅 12:35 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84626">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ndx7-Jfs63UDe-1JEtuqqSqgXTT-Sbfmu7-90FXB_CVC6q752qPETlv1DuigpRA-F40s6aMXb8EKT4fkNcK-lS1nglHK4dLOQyBtLu_iXldZ4HGTXss32nnOWx3WBIYNokFo7E_RK4NpPlJUBLkWzk5Cp3m9M9dtf_DuMl97q4AjbpLiS4aKkzm3KVS7JRsSLpQyJZIa6HLaVksybW_9BNbDm60mezUghsyk4W7SQo2ZLLEnJbV6uYHdwSh8sz5HOK3hprziz7v1lmcfwP_47CRuvVX5peECKmGtVcWbA1RdnHiTlbMQS6_fa1QqYQpeVC3spA8PCIBikXK-qiDuZw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حالا فک کن فیت بدن
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/funhiphop/84626" target="_blank">📅 12:29 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84625">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">هالند و امباپه تعویض بشن بین سیتی و رئال جفتشون بهترین تیمای جهان میشن
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/funhiphop/84625" target="_blank">📅 11:58 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84624">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cirIW3f7kgPIknsaoegpUyVK7zWvT6utCFhhoPNw0dTy_9KP6taUoAgib1TtwigSZRJKnVWmuCd53oiSBacPM27GcmHpXNmiaJaUxnUK0Dp-pEdb07fPqLH01yEMQvsoWLf-Pd6Fb7G2aavGnQghELNUlOLNff-s8wfSVuyhH_nU2QIsrxlk_m1FOZXM7MnhsxPgTG7h_24BW6tdEooWwZa3Vu5Hhw8Q5OH7CZ7EwEIlDhQFhpI6xliozrgk360c5cNZo4-9wHWxMSt6kz1_4oL_4SV54QOVzZoaD90uoB0hzscVFKR_A5BMAkSzkoFdo1dRQ6FTHL4rJPgVKw98yA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پس داستانای کیلیان دیکتاتور حقیقت داره پسر
آاس :
امباپه توی رئال هیچ رفیق صمیمی‌ای نداره و اون توی رختکن رئال احساس غریبه بودن میکنه. با بلینگهام بینشون یه جور تنش و سردی وجود داره، با وینیسیوس هم رفیق نیست و با بقیه بازیکنا هم رابطه‌شون بیشتر در حد کار و فوتبال حرفه‌ایه. حتی از بازیکنایی که قبلاً باهاشون صمیمی بود هم کم‌کم داره فاصله میگیره، کلا تو تیم کسی با امباپه حال نمیکنه
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/funhiphop/84624" target="_blank">📅 11:31 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84623">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/M6ZgnNj3zRIEXC0fF8es-l32qSrSFZYew4KFeU6sBbw8TjCexD3d9e0nFI6x6Telutm-TAPipTLA4ieqEiUkcSYQ53z6VgTxvs21kZMCnDg5Ek3LQQIt-cBLQVEI9ynyklbryOA7EaI45g6k8MX1_vgUHE3xbhrMvzBbVk-ooN_Cz4hw1BaPD2Ye-9Q9XUpE2mlzvGaFAofnVDipQXMjowIqntPuHr9Tnj1jzHafsnVZW-1sv1II8_OuW-vG3TcYygysEPq_0DHAOAz8RVjwYq8M1yOn60zjLxi9edqQ0oiNlHjg5ZOoIskVxZvM8jFOZ97XMRv7BDpqeOv58BA4jg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مستند تک قسمته ۲ دقیقه ای(یک دقیقش تبلیغاته)
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/funhiphop/84623" target="_blank">📅 11:00 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84622">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">عراقچی پالس های مثبت از مذاکره با آمریکا داده، شیشه هاتونو ضربدری چسب بزنید
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/funhiphop/84622" target="_blank">📅 10:40 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84621">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">ویچرت؛ تحلیلگر معروف آمریکا در توییترش: اسرائیل دقیقا قبل از‌ انتخابات آمریکا به ایران حمله میکند. این پست رو‌ ذخیره کنید.
پ.ن: این یه بارم گفته بود آمریکا لحظات آخر جنگ ۴۰ روزه میخواسته به ایران بمب اتم بزنه که ایران میفهمه و مذاکره کردن رو میپذیره، قبل از شروع جنگ ۱۲ روزه ام میگفت دیر یا زود یه جنگی بین ایران و اسرائیل اتفاق میوفته
پ.ن۲: آیزنکوت رقیب نتانیاهو در انتخابات اسرائیل هم دقیقا همچین حرفی زده دیشب
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/funhiphop/84621" target="_blank">📅 10:20 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84620">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">من جای تهی بودم دیسای قدیمی پیشرو و هیچکس به هم دیگه رو جلوشون پلی میکردم و از واکنشاشون فیلم میگرفتم
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/funhiphop/84620" target="_blank">📅 09:58 · 17 Mehr 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>

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
<img src="https://cdn1.telesco.pe/file/L-ONBxCTRyobFDLFoC6q-rKxjaxKEJWd1qQPrSrDPf6Z7L7elDrqR8VOZFFEIML2WacOMqwlgstjrDLoXyj_MJcbhU2urfub0HgF8grqwgz8wpbYxv8YrtPjndcB8zrUhaYpkaGgj64nTaScF1UuCAUEwnsNbuvS0PTaG3W5ANLGLzt16fEWaCPajERxCSBY3zyk1PGicYS8CQQx-KGscH7X7iCrZr9e7N8dk4pcRvkjV6JzPLWjiZ42FDH2Fv0BV--IBiivNl4BC_zEi_4msag_8RO3FPVTBZ_TJzpS1TKA9e-gsslzKZE-Fz_D6Rpayjz-kf6ataKGV2Cnx2VNxA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Vahid Online وحید آنلاین</h1>
<p>@VahidOnline • 👥 1.33M عضو</p>
<a href="https://t.me/VahidOnline" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ارسال پیام:@Vahid_Onlineinstagram.com/vahidonlineتلاش می‌کنم بدونم چه خبره و چی میگن. اینجا بعضی ازچیزهایی که می‌خواستم ببینم رو همونجوری که می‌خواستم بهم نشون داده بشه می‌گذارم.استوار بر حمایت‌های مردمی:ماهانهvhdo.nl/patreonیک‌بارهvhdo.nl/paypal</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-15 03:29:29</div>
<hr>

<div class="tg-post" id="msg-75943">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/tipqLGT5iBgzRXpNsMcbiAXkQ2jWglmRxD6Xv5HGkldOiovXKgHRCFIZmUF5ct6ZMfpl8xpiXmrnm9pwqB0bnTb2J327rI5jU454plunkPgACtZsT274w-EP3kUYKekv8c9J5WBI2bJ6fUKesEaM4kNyYy-cGJXIV3EG7sAw61rlv6YmXWfLHDtTUTdsfCnDj04l_QX2ypa-blVR4Ra6ph4BMUMU0ipA65HtLL0R6JIK42gfbmsJ-egM1cG5YZeibbIa56DaBBfZ9w3_tJdDNfw9fUWhSuvxC8mwCRjEZ9n0RcdUzuZFm4wtMk7QLSMIiwPd6py6tCkeyBJ4PbCMiA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔻
ترامپ: ایران نباید سلاح اتمی داشته باشد
دونالد ترامپ، رییس‌جمهوری آمریکا، در کاخ سفید در پاسخ به این که اگر حکومت ایران نیروهای آمریکایی را بکشد، آیا جنگ با جمهوری اسلامی را از سر خواهد گرفت، گفت: «این دلیل خوبی برای چنین کاری خواهد بود. اگر آن‌ها نیروهای آمریکایی را بکشند، فکر می‌کنم خیلی سریع دست به این کار بزنم.»
ترامپ درباره جمهوری اسلامی تاکید کرد: «آن‌ها نمی‌توانند سلاح هسته‌ای داشته باشند.»
رییس‌جمهوری آمریکا گفت: «ما برای به‌دست آوردن اورانیوم غنی‌شده آن‌ها به توافقی با ایران نیاز نداریم.»
او درباره کمک ناتو به بازگشایی تنگه هرمز نیز گفت: «ما به آن‌ها فرصت دادیم که کمک کنند، اما نخواستند کمک کنند. این موضوع برای آن‌ها بسیار پرهزینه خواهد شد، چون نباید چنین کاری می‌کردند. باید کمک می‌کردند.»
🔻
ترامپ درباره جنگ: چه از نظر نظامی و چه روی کاغذ، ما پیروز خواهیم شد
دونالد ترامپ، رییس‌جمهوری آمریکا درباره جنگ ایران گفت: «چه از نظر نظامی و چه روی کاغذ، ما پیروز خواهیم شد. بخش اصلی این است که تنگه فورا باز خواهد شد.»
ترامپ افزود: «آن‌ها (جمهوری اسلامی) هیچ نیروی دریایی ندارند، هیچ نیروی هوایی ندارند. ما آن‌ها را نابود کرده‌ایم.»
او ادامه داد: «رهبری‌شان را از بین برده‌ایم و تقریبا همه آن‌ها را نابود کرده‌ایم. بعد در رسانه‌های جعلی می‌خوانید که آن‌ها در جنگ خیلی خوب عمل می‌کنند. واقعا باورنکردنی است. ما هر چیزی را که می‌شد نابود کرد، از بین بردیم.»
🔻
ترامپ: حکومت ایران درباره توان و اراده آمریکا دچار اشتباه محاسباتی شده است
دونالد ترامپ، رئیس‌جمهوری آمریکا، در نشست کابینه در کاخ سفید با اشاره به مذاکرات جاری و وضعیت تنگه هرمز گفت یکی از محورهای اصلی توافق، بازگشایی فوری تنگه هرمز برای عبور و مرور کشتی‌ها است و تأکید کرد آمریکا «هم در میدان نبرد و هم در عرصه دیپلماسی» پیروز خواهد شد.
رئیس‌جمهوری آمریکا مدعی شد توان نظامی جمهوری اسلامی به‌شدت تضعیف شده و گفت: «آن‌ها دیگر نیروی دریایی و نیروی هوایی مؤثری ندارند. ما تقریباً همه توان نظامی و ساختار رهبری آن‌ها را نابود کرده‌ایم.»
او در پاسخ به پرسشی درباره احتمال ازسرگیری جنگ در صورت کشته شدن نیروهای آمریکایی توسط حکومت ایران گفت چنین اقدامی می‌تواند دلیل کافی برای اقدام نظامی جدید باشد و در آن صورت آمریکا «بسیار سریع» واکنش نشان خواهد داد.
ترامپ همچنین درباره ذخایر اورانیوم غنی‌شده ایران گفت آمریکا در مقطعی گزینه خارج کردن این مواد را بررسی کرده بود، اما به دلیل نیاز به حضور طولانی‌تر نیروهای آمریکایی از این طرح صرف‌نظر شد. به گفته او، واشینگتن همچنان توانایی دسترسی به این مواد را دارد.
وی افزود آمریکا با استفاده از سامانه‌های پیشرفته نظارتی و امکانات فضایی، تمامی مناطق مورد نظر را به‌طور کامل زیر نظر دارد و هرگونه تحرک را رصد می‌کند.
ترامپ درباره احتمال دیدار با مجتبی خامنه‌ای نیز گفت شخصاً تمایلی ندارد و چنین پیشنهادی را هم مطرح نکرده است، اما اگر چنین دیداری انجام شود، با احترام برخورد خواهد کرد.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 170K · <a href="https://t.me/VahidOnline/75943" target="_blank">📅 00:04 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75942">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/aviJdhSe3q7EffXWxStQTNXI_65wDmTiS-vjnH5nAnxhgGOfEUb025014EUyeNxqVGo8eHM1VNBP-4YjmHFbKj8MCfrh0I8uunVE9u3kzGGz8Y33xcDVr-a33qugy-r0Bqs78acMX4kP00EcnZPRhSFyws5EtKKmXs_dLAUuvVcnhe6My5uoBeigyfm2Eym0ImrMMLyTim_Pt46Sv4rj10R2LaRHjUZjSdWYPcQvgZUSpC80geOHpHzssgvKHmQxR76SYt6griOTwsU-dB2PIooNgwWAeXAuZkN5AxS8-dvfphEpqznJ4ybSCIdN6zxlRgdnrfZSKbe-dBVXUoDSCg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">العربیه پنجشنبه شب ۱۴ خردادماه، به نقل از منابع اختصاصی گزارش داد محسن نقوی، وزیر کشور پاکستان، برای پیشبرد مذاکرات میان جمهوری اسلامی ایران و آمریکا به تهران سفر می‌کند.
به گفته این منابع، سفر نقوی در چارچوب تلاش‌های میانجی‌گرانه اسلام‌آباد میان تهران و واشنگتن انجام می‌شود.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 167K · <a href="https://t.me/VahidOnline/75942" target="_blank">📅 00:01 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75941">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/GNMmMCJDEAkHWHG_gavpxKPk9K7ZJG5KrcAbbFcRJYkeeNygnOkp1Drryr9pKBjYkq6CC1q6z5Z6qwpntfyNPMBvY9nyGNpCNXmoZg0xHYD2ovjrvqn8jujLHWoBFh1HslaVw577smRqlGIECO_gDSCqAO4_bJYyGZ9C0l4xik_o-cC79sEnPUQua1kW7ejE5txNu6z8cK6uJ9DAt5Jn8T6XOs8oUALwopgfqAMM-i08PYKk5pi3FkTnUWKYjb6e7ML5diIjZInwyXkDviiofeMuC-ABBuuQpvzZ7J7MvT8bOsc_4REgRoT_MYp49TUDxCeHYhofGgT41Q-rWdQdGQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دونالد ترامپ، رئیس‌جمهوری آمریکا، روز پنج‌شنبه گفت ایالات متحده بر جمهوری اسلامی غلبه می‌کند، یا با توافق یا با عملیات نظامی.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 160K · <a href="https://t.me/VahidOnline/75941" target="_blank">📅 00:00 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75940">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/srGeW1mIBAu8QzEumCtzjgPY2x0PsNVfw6sOot4yNuVbStukIdlxpJ011VUFKjomDhDe-lsHfFSdUXrDzYgXN7BR4hyqzNty-i1fSCHjZj96Xi_5YyCILEj8IfnLFFrHaG2Tkub-2B5Lj5OhgEDQuFs1mSAr-_TWdMHABsJrU1GZpC8AiaAEowSJeUFHBZYYxbDPtOM0YoHnl5JIEdBjU6aM48cdaZtsXMgY9-wscSs004K8IGfc6zJ-HX-hFCCGa94pdDhcrCHJHkoq66rPxX7ruA4SvygfMSNXk78uhdINmppTVfhtV-b0Rph4Ile2w1yalMX3d0asmwElMaHHlg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آژانس بین‌المللی انرژی اتمی پنج‌شنبه ۱۴خرداد۱۴۰۵ در گزارشی به کشورهای عضو، بار دیگر از جمهوری اسلامی خواست «به‌طور فوری» درباره سرنوشت ذخایر اورانیوم غنی‌شده خود پس از حملات سال گذشته آمریکا و اسراییل به تاسیسات هسته‌ای این کشور توضیح دهد.
در این گزارش همچنین از مقامات جمهوری اسلامی خواسته شده تا زمینه ازسرگیری کامل بازرسی‌ها را فراهم کنند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 256K · <a href="https://t.me/VahidOnline/75940" target="_blank">📅 19:16 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75939">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/FHOVjf3h0V5ZUJOtgwWUi4QpRUC4TY6FCwn9U-3HNl76KZ0iD-NHdaOG2pAfc6REtugwRbcOnFBAL4FJURINXY6pmqd0z__B-Mmt2IdBUEYvD-FtHu8qZ22740-AC6BuZU464vr9kkyTLtovhysTUcfcUwrEcuxLsVakSEVWqZ2C-raPkxwzUUlih-IuVNhBGrcnBQ5NMrWOTskPGrAH6LJPAe0x9LD7YPtGNOiyCQFnGeW38Q9996ZoRlY97fsz03R5FqQ785ir0eoVrC__wDaac47Y3Mj4qEqIc1By0iZIuuFlPRod2ZGWTRJpEHXsErbp8oGGP1nDi0I-dgrDEw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دبیرکل گروه حزب‌الله طرح آتش‌بسی را که دولت‌های لبنان و اسرائیل در مذاکراتی با میانجی‌گری آمریکا بر سر آن توافق کرده بودند، رد کرد.
ایالات متحده روز چهارشنبه اعلام کرده بود که لبنان و اسرائیل بر سر اجرای یک آتش‌بس به توافق رسیده‌اند؛ توافقی که مشروط به توقف حملات حزب‌الله و خروج نیروهای این گروه از مناطق مرزی جنوب لبنان است.
@
VahidHeadline
نعیم قاسم، دبیرکل حزب‌الله لبنان، توافق دولت لبنان با اسرائیل که با میانجی‌گری آمریکا تدوین شده است را «تسلیم و شکست تمام‌عیار» توصیف کرد و گفت حزب‌الله تنها به توقف کامل حملات، آتش‌بس و خروج اسرائیل از خاک لبنان متعهد است.
او همچنین خلع سلاح حزب‌الله را به معنای از بین رفتن قدرت لبنان دانست و تاکید کرد این موضوع برای حزب‌الله قابل پذیرش نیست.
پس از توافق آتش‌بس میان اسرائیل و حزب‌الله لبنان، آمریکا برای حل‌وفصل اختلافات مرزی و مسائل امنیتی میان دو طرف نقش میانجی را بر عهده گرفته است. در همین حال، موضوع خلع سلاح حزب‌الله و نحوه اجرای آتش‌بس همچنان از مهم‌ترین محورهای اختلاف میان دولت لبنان، حزب‌الله و اسرائیل به شمار می‌رود.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 281K · <a href="https://t.me/VahidOnline/75939" target="_blank">📅 16:47 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75938">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/NNG6cWU70R2p2RGikqaZvFWoFYyOhbbhqfn-BUAs2cfPSoXbkcMjrlGKzhXpzI52p0dU0Xgm9cTYFrMBPJUUfUCMElxiv-3kJ6ZHDBPVF_x7OtLl1syJYLPnFR498ffcDno5WZxyx_luN3KoRw7ChjnkQCbosiKmSVl7655WTKfgj__2f0UyVlshXyJhNWa_RikprNoyL5tCE6-7n8gchAslXF2HmXF-JtD0iEcGQwuk5Wq-TuExgjZbEjT2pfWB__OzFY-5jAuoVuNVrGn3wEo-02L1bF8SxnyfFIha_o0yTei50spWQ0o0epaU89z9MuA3mh1SJDhRqZ25_VHuJw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرگزاری تسنیم، وابسته به سپاه پاسداران روز پنجشنبه ۱۴ خردادماه و ساعاتی پس از انتشار ویدیوها و تصاویری از برخورد پهپاد سپاه به فرودگاه بین‌المللی کویت، به نقل از یک منبع نظامی، آن‌ها را «تصویرسازی دروغین دشمن» خواند.
این منبع نظامی به تسنیم گفت:‌«پرتاب پهپادهای هوافضای سپاه به سوی اهداف آمریکایی در کویت، در نیمه شب و اصابت هم در نیمه شب (و در تاریکی هوا) صورت گرفته است درحالی که در فیلم و عکسهای ادعایی که از پهپاد در فرودگاه منتشر شده، هوا کاملاً روشن و مربوط به روز است.»
سپاه پاسداران پیش از انتشار تصاویر برخورد پهپاد با پایانه مسافربری شماره ۱ فرودگاه کویت ادعا کرده بود که موشک‌های سامانه ضدهوایی آمریکا به این محل برخورد کرده بودند.
این منبع نظامی که نامش فاش نشده به تسنیم گفت:‌ «فاصله «هدف» پهپادهای هوافضای سپاه تا فرودگاه کویت بیش از ۴۰ کیلومتر است و این نیز نشان می‌دهد که اصابت به فرودگاه کویت ارتباطی به پهپادهای ایران ندارد.»
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 258K · <a href="https://t.me/VahidOnline/75938" target="_blank">📅 16:39 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75937">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/deQ3uGLInXjoGnHndg1u4wgYv4Oy6k5fbSIIRZlhnGSZbhIRXtB4_PA0NucRa6kuVK026V34FpLG-2sYNacPqOMXhmX0D1_Q8VQ01sppcjCk8pxdIvya9gcYU_F_AN9esw6fdHC4S8_ThRR7UQlASeZTjpeDMN2MJdAJ-5lwKUo_NAqWC3ZjQTrmzYh4Z448xZbiFQTwI64Lu4jtxJkFuyENXSHGokex8V8A8BfrOy2a2GpRRgaHWamt6FCEMCU_jOX3gEhvfc9T5PqteL6F4ipSHok_Izbl6c6IBGjNwKzC8JWX6NIKrMJLFzEzVnzFnTTdQFkgZkiPVuz7SM_gRw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پیام مکتوب و منسوب به مجتبی خامنه‌ای، سومین رهبر جمهوری اسلامی، در مراسم سالگرد مرگ روح‌الله خمینی در تهران، خوانده شد.
در این پیام که محمدجواد حاج‌علی‌اکبری، امام جمعه تهران، روز پنجشنبه ۱۴خرداد خواند، رهبر جمهوری اسلامی‌ آمریکا و اسرائیل را به «جنگ ترکیبی» با ایران متهم کرد و گفت این جنگ «بر دو نقطه متمرکز است؛ یکی تاب‌آوری مردم و دیگری ایجاد اخلال در دستگاه محاسباتی مسئولان کشور».
مجتبی خامنه‌ای همچنین هرگونه اقدامی که به‌گفتهٔ او «موجب بدبینی و سرخوردگی» شود را «کمک به دشمن» خواند و خواستار «حفظ وحدت و انسجام و اعتماد متقابل» مردم و مسئولان نظام شد.
مجتبی خامنه‌ای هفتهٔ گذشته نیز به تمام کسانی که آن‌ها را «جان‌فدایانی که دل‌شان برای اسلام و انقلاب یا استقلال و سربلندی ایران می‌تپد» نامیده، هشدار داده بود که «اختلافات غیرموجه و حتی موجه را به تنازع و تفرقه تبدیل نکنند».
در بخش دیگری از این پیام، اسرائیل «پادگانی متعلق به نظام سلطه» توصیف شده و تاکید شده است این کشور از هر اقدامی برای جلوگیری از پیشرفت ایران کوتاهی نمی‌کند.
این پیام همچنین اعلام کرده است: «دشمن خبیث در مصاف با فرزندان دلاور شما در نیروهای مسلح دچار شکست شده است» و افزوده است دشمن پس از آنچه «تحقیری پرمعنا و عمیق» خوانده شده، تمرکز خود را بر تضعیف تاب‌آوری مردم و ایجاد خطا در دستگاه محاسباتی مسئولان قرار داده است.
در پایان، در این پیام از همگان خواسته شده است با ایستادگی، روشن‌بینی، حفظ وحدت و انسجام و همصدایی نکردن با دشمن، «نقشه شوم» او را خنثی کنند.
از زمان اعلام نام مجتبی خامنه‌ای، به عنوان سومین رهبر جمهوری اسلامی، تصویر یا صدایی از او منتشر نشده و رسانه‌های ایران فقط پیام‌های کتبی از او منتشر می‌کنند.
مراسم سالگرد مرگ روح‌الله خمینی که هر سال ۱۴ خرداد با سخنرانی رهبر جمهوری اسلامی و با حضور پرشمار مقامات و فرماندهان ارشد نظامی برگزار می‌شد، امسال به‌صورت خیلی محدود و بدون حضور مقامات نظام برگزار شد.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 240K · <a href="https://t.me/VahidOnline/75937" target="_blank">📅 16:35 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75936">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TovUDbG5NGCljVEeiyEbt5fvrenHdHOEzuY5KdWtfGjeDad7GFEQcNWSO-4Rdveq8w-xDaQSKOna0uYBNxeyfK0dnjfTp8URxwfRcn4R-4U0iMA9BnYeJqV2RhSnWgdVtEgdvWxOaX00tu2DPBGTNfr_9wEm7KnjdKZiZ2CopNQXfczPOcQ4IgcuAMO6svrOQjn00cg2LEUnDUmP1v7sO4EZZq3OzD3XzEWA1yyDdIvs9DcSVvdePZy4FynG68263FCPRBt3V35B_3ItAAiW1Jbfen58MBITRcBNsNfiW2fxsDzahJExaLLwAY726MI05O_BxahaZ-9eSgJaOKWjdA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
دونالد ترامپ، رئیس جمهوری آمریکای روز پنجشنبه ۱۴ خردادماه از تصویب قطعنامه «پایان جنگ ترامپ با ایران» به‌شدت انتقاد کرد.
رئیس جمهوری آمریکا در این پیام نوشت:‌ «دیروز، در یک رای‌گیری بی‌معنی، مجلس نمایندگان، چهار جمهوریخواه بد و تمام دموکرات‌ها، درست در میانه مذاکرات نهایی من برای پایان دادن به جنگ با جمهوری اسلامی ایران، به محدود کردن اختیارات جنگی من رای دادند. چه کسی چنین کار غیرمیهن‌پرستانه‌ای انجام می‌دهد؟ آنها می‌دانند مذاکرات در چه مرحله‌ای است.»
ترامپ با انتقاد تند از نمایندگان حامی این طرح نوشت: «دموکرات‌ها از سندرم اختلال روانی [بیماری مخالفت] ترامپ تغذیه می‌شوند. آنها ترجیح می‌دهند کشورمان شکست بخورد تا اینکه به من یک پیروزی دیگر، از پیروزی‌های بسیار، بدهند. چهار نماینده جمهوریخواه، داستان آن‌ها کاملا متفاوت است. آن‌ها خودنما هستند! آن‌ها باید از خودشان خجالت بکشند.»
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 228K · <a href="https://t.me/VahidOnline/75936" target="_blank">📅 16:30 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75935">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/b2qa6yutjdtAVd4444DLCR1aaES1-HrrnzRDWR-fetuzMBXLKW17Cy0rh5cBgz2nrlfqBUUc4EMibDqJtBqZurzCOIOnPMQ4evMxapn0flP23zhoOF3OkB73nwGIxjFehOa7YJjUiHqDnqvGTmqYbiSRjP_lksMQoko99tuq9KXoxPkpX5YpSizx7cTxyX9vw6FsMn8oaZd6vHBdkYMEG7xoj6xKl8EU4ZNa12ieUDYgVpUMFUJsATNHh7EfsklL-XYvdpzTOmjw2mgUEfPfDc4ryY0VVw4PVkKJlIWO92VNgL1AL0y3vkdWVjNIAo3KTOi6piYerQMqsmWJiwjbDg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مرجان ساتراپی، نویسنده، تصویرگر و فیلمساز ایرانی-فرانسوی و خالق کتاب مصور «پرسپولیس»، در ۵۶ سالگی درگذشت.
به گزارش خبرگزاری فرانسه، نزدیکان ساتراپی اعلام کردند او «کمی بیش از یک سال پس از درگذشت ماتیاس ریپا، همسرش و عشق زندگی‌اش، از غم درگذشت.»
ساتراپی سال گذشته نشان لژیون دونور دولت فرانسه را در اعتراض به ریاکاری دولت فرانسه در قبال مردم ایران و جمهوری اسلامی رد کرد.
مرجان ساتراپی با انتشار «پرسپولیس»، کتابی مصور درباره زندگی خود در ایران و مهاجرت، به شهرت جهانی رسید. این اثر با استقبال گسترده مخاطبان روبه‌رو شد و به یکی از آثار شاخص ادبیات مصور معاصر تبدیل شد.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 247K · <a href="https://t.me/VahidOnline/75935" target="_blank">📅 16:28 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75934">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/K4Ad6sB8xSBbx4WDn6TBG5u5XhPfrQt29jPvkftgX5Vuar8m01kw00fEm2QzRpDnNciWrdP0fme0Z8JirbOxwXkLLTXxPx3PzbvoJN-v5dvM16u6AEXwMdJaQyBeMUgf7GPE3o0NM6VftWf09PLOhPxvOAqqTp4cWuZFH6JAb0bo9uBG8n7zhw9P_TgtKmoSe05bnZDAURiJDmlyse8qc6MJ4QhujB8jcDZKsZJAzCU-udVK0vNOWLwnDKDPxrfw6gBk2N7qw-i_R3u2wDZfTaENchy0RRFaFuUJBdLRUB7QRD2aqRWyQ9aWEtyJb6FYoyGh6XHvaZ0ksWpLU1rZXA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سازمان هه‌نگاو و سازمان کوییرهای ایرانی سیمرغ با انتشار اطلاعیه‌هایی خبر کشته‌شدن مهشید فلاحی، زن ترنس، در سنندج را تکذیب کردند.
این سازمان‌ها ضمن عذرخواهی درباره انتشار این خبر نادرست، با وجود راستی‌آزمایی‌های قبلی، گفتند اسناد جدید نشان می‌دهد این شهروند زنده است.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 244K · <a href="https://t.me/VahidOnline/75934" target="_blank">📅 16:27 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75933">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XBIZv-2wISESfIIEFbySMjk6lImjMc0jsmLCWst05lhx42uQLYHGmL_TyrLY7BGJdqLyJj0nR-IAVRJ6dzCspLx81vjxR2Tu_SjMwrfO2heaPPMkDA0WZ_Z9xjQgd54PUHyaEM80B4SB6YAFrszZl6OAv3epG33vu6UH9tKIE8mkKSJw7BZk5MfYHDeb6ugHb6knB2dtUoXy1F22gzt1fPwBGe2_xQEGl3TjnRQ2PNDXkweMQt_nzH9ZlUSMJFrMOM_EoL6gEVY_7V8KEtawPHxQzXfJiyS1WvvplLKMaPeicp8B8skbfDCEszNFaOycr8OcIcX9f8FJJu1wD1gbSw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">الحدث گزارش داد آمریکا و جمهوری اسلامی به توافقی چهار مرحله‌ای نزدیک شده‌اند که با کاهش تنش‌ها آغاز می‌شود و به پرونده هسته‌ای و ترتیبات امنیتی منطقه ختم خواهد شد و انتقال از هر مرحله به مرحله بعدی، پس از «اجرای تعهدات» انجام می‌شود.
طبق این گزارش، مرحله نخست توافق شامل توقف عملیات نظامی مستقیم و پرهیز از هرگونه تشدید تنش یا گشودن جبهه‌های جدید در منطقه است. مرحله دوم نیز بر امنیت کشتیرانی، بازگشایی تنگه هرمز و ترتیبات امنیتی ویژه گذرگاه‌های دریایی و خطوط انرژی متمرکز است.
به نوشته الحدث، مرحله سوم این توافق شامل اعتمادسازی اقتصادی، کاهش محدود برخی تحریم‌های جمهوری اسلامی، آزادسازی بخشی از اموال مسدودشده ایران و ارائه تسهیلات مرتبط با صادرات نفت است.
بر اساس این گزارش، مرحله چهارم توافق پیچیده‌ترین مرحله به شمار می‌رود و ممکن است ماه‌ها طول بکشد. این مرحله شامل بررسی برنامه هسته‌ای ایران، سطح غنی‌سازی اورانیوم و سازوکارهای نظارتی و ترتیبات امنیتی منطقه‌ای است.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 345K · <a href="https://t.me/VahidOnline/75933" target="_blank">📅 02:49 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75932">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/huHdFD3cViR196V8SxHOQ2JAyKqyZwHwqSI7v1CVtCyldSxYbATLmUMBngQj0wsJ0uJiEBBqj6QtaRjgEXcCYc-pzV2TrIq66G6X5CHU2vkuOdpITAE4ZkSQWmOzScvxZs1qkW48Z6yfsxzss_-ODFXRDBvT1LPtFKqvumLZBTZ4qdfgpiY3XvUeO6CBiQwUZdAs3082QKMZs5HcazpfshcSjijzDaQFMCv0X9NG_5Fca57YFxb9x9M-LHfcVJAiXQMrIoOp6wRYrncV7lCNpmzgK04_3ITEszH44s6mGC3_GOw6FEmTQFSgqRZoeDMoYBajREWPpNk7Gsnf0C2Hag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزارت خارجه آمریکا اعلام کرد اسرائیل و لبنان بر سر اجرای یک آتش‌بس به توافق رسیده‌اند.
بر اساس بیانیه منتشر شده، اجرای این توافق «منوط به توقف کامل» حملات حزب‌الله و همچنین تحقق چند شرط دیگر است.
این توافق پس از آن اعلام شد که حملات اسرائیل به جنوب لبنان در روز چهارشنبه دست کم ۹ کشته بر جای گذاشت و حزب‌الله نیز راکت هایی را به سوی شمال اسرائیل شلیک کرد.
در بیانیه چهارشنبه شب وزارت خارجه آمریکا آمده است: «همه طرف‌ها بار دیگر تاکید کردند که آینده روابط میان اسرائیل و لبنان باید توسط دو دولت مستقل و حاکم تعیین شود. آنها هرگونه تلاش از سوی دولت‌ها یا بازیگران غیردولتی برای گروگان گرفتن آینده لبنان را رد کردند.»
حزب‌الله تاکنون به صورت رسمی درباره این توافق اظهار نظر نکرده است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 315K · <a href="https://t.me/VahidOnline/75932" target="_blank">📅 02:49 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75931">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/a5b9c36ab1.mp4?token=aZGgbMiscKhNOn3SnloHy_yGZ3cUrR5SO1sLGS44YWyawD2wMTuTjswpG-WAy_3cu1pCBhr_P_oORakqFUDt2ofQRQuSzinA8WsK5yyLeh1nQFM19IJxr4AvDWY3x3_hIHAl_d6KTwH9aSX2p3GG7GB4x-5mf8YLwJJeZoh86lh_RLArO6qtgjCmRq5zysYToYzOHeU0251wg3NeI8T74EamoDkPBWfwzfufSV3p28pIfibuA2bulLuytBgLH4_blcqJxQ-BJnDCPAaT8hwvWfs6H0bd0xk_TD2EyyGWYBkjSAgC3Df0Fby99DfPUV0gWQ0fy1P9pPzstbaS5aMwSg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/a5b9c36ab1.mp4?token=aZGgbMiscKhNOn3SnloHy_yGZ3cUrR5SO1sLGS44YWyawD2wMTuTjswpG-WAy_3cu1pCBhr_P_oORakqFUDt2ofQRQuSzinA8WsK5yyLeh1nQFM19IJxr4AvDWY3x3_hIHAl_d6KTwH9aSX2p3GG7GB4x-5mf8YLwJJeZoh86lh_RLArO6qtgjCmRq5zysYToYzOHeU0251wg3NeI8T74EamoDkPBWfwzfufSV3p28pIfibuA2bulLuytBgLH4_blcqJxQ-BJnDCPAaT8hwvWfs6H0bd0xk_TD2EyyGWYBkjSAgC3Df0Fby99DfPUV0gWQ0fy1P9pPzstbaS5aMwSg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">لحظه اصابت پهپاد انتحاری شاهد 136 به ترمینال فرودگاه کویت از دید دوربین مدار بسته.
mohsenreyhani01
سازمان هواپیمایی کشوری کویت با انتشار ویدیویی گزارش کرده که «نخستین تصاویر» حمله پهپادی به فرودگاه بین‌المللی این کشور که از طریق دوربین‌های مداربسته بیرون و داخل فرودگاه ثبت شده را علنی می‌کند.
در این تصاویر که از چند زاویه بیرون و داخل فرودگاه دیده می‌شود یک پرتابه مشابه پهپادهای انتحاری به سقف ترمینال فرودگاه برخورد و موجب انفجاری بزرگ می‌شود.
در ویدیویی دیگر، وزارت کشور کویت با انتشار ویدیویی اعلام کرد که شیخ فهد یوسف سعود الصباح، معاون اول نخست‌وزیر و وزیر کشور نیز ضمن بازدید از ساختمان ترمینال ۱ فرودگاه بین‌المللی کویت، این حمله را «تجاوز فجیع ایران» خواند.
کویت اعلام کرده در جریان این حمله یک نفر کشته و بیش از ۶۰ نفر مجروح شدند. فرد کشته شده تبعه هندی بوده و وزارت خارجه هند گفته چند شهروند دیگر این کشور نیز در این حمله زخمی شده‌اند.
سپاه پاسداران که شب گذشته از حملات موشکی و پهپادی خود به پایگاه‌های آمریکایی در کویت و بحرین خبر داده بود، روز چهارشنبه گفت «هیچ شلیکی به سوی فرودگاه کویت» انجام نداده است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 310K · <a href="https://t.me/VahidOnline/75931" target="_blank">📅 01:47 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75930">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/m15FtrVGVSH91Q2tEyB1FeLyKystFcjKoaYUhAM2GXjSfynm-iB_yi7yDjC0CuIE0j80lgGX3jHptdaSeZkwzx4QpGXC8RXeDAyl1-oiNNQJwf5ITBcY_i4KeqRyOxuikCeKGjM2f9JBbOa7Os_snc6Tc3mERdemHf9n4GFCt3hghcx68Er3gCuWSSSVj5JWj2JxFzVP8uo8eVqfJkDEGF2ug4BaB7FTASR427VwWG42d-AuQPJ25gTgQ_MJCumC1eLY500Zst69lB3AE2UUGQRDW8rtd1T6o7UAKX5_GGuViRppPOPca9JcDLf4wnH0jYzc1MnnFh0ZgpkEJmXzGA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مجلس نمایندگان آمریکا روز چهارشنبه از قطعنامه‌ای به رهبری دموکرات‌ها حمایت کرد که هدف آن متوقف کردن جنگ با حکومت ایران تا زمان صدور مجوز از سوی کنگره است.
به گزارش رویترز این قطعنامه با ۲۱۵ رای موافق در برابر ۲۰۸ رای مخالف تصویب شد و چهار نماینده جمهوری‌خواه نیز به دموکرات‌ها پیوستند.
این رای‌گیری تازه‌ترین شکست سیاسی دونالد ترامپ در کنگره به شمار می‌رود؛ با وجود آنکه جمهوری‌خواهان در هر دو مجلس اکثریت شکننده‌ای دارند.
بنا به این گزارش، این اقدام عمدتا جنبه نمادین دارد، زیرا برای اجرایی شدن باید در سنا نیز تصویب شود و همچنین برای عبور از وتوی احتمالی دونالد ترامپ به حمایت دو سوم اعضای هر دو مجلس نیاز دارد.
با این حال، این رای‌گیری نشان‌دهنده افزایش نگرانی در کنگره درباره جنگ با حکومت ایران است.
سه قطعنامه مشابه پیشین در مجلس نمایندگان شکست خورده بودند، اما با اختلاف آرای کمتر از دفعات قبل.
همچنین سنا ماه گذشته یک قطعنامه مشابه را در یک رای‌گیری رویه‌ای به پیش برد؛ اتفاقی که پس از هفت تلاش ناموفق قبلی رخ داد.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 304K · <a href="https://t.me/VahidOnline/75930" target="_blank">📅 01:29 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75929">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/QyBnkPnfWzzSDKpl57PE01YYGMsoM-hjbqtGCuHvuUHReKEHb79WqIiGycgVhZG2jzebUNwmdnbXINIV3pd9uhHV8arQ_yD8IaJI8qVLHt7y3cyYCSFVfrXIlndU7K36TwaATFXCUII1E0gilLrowhen7rbXIJLcnfSU5tOGvppTrJAsq-xP_EyTGBRvQ2LhydJ1SdaU-84eiJBzMgJJTeRqvfNHUbtND8f3tVUTjpbStgfJ7ihg1lOxUK59JoSYCnmmD8QtNUyLhnmXt9fwxsjiLzwrIYBfH2hUklwBod12zFTvO7SHAH8aGLT4GHQG2wXO6iPClUvQosRGcygvQg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔻
ترامپ: می‌توانیم همه را نابود کنیم، اما ترجیح می‌دهم به توافق مکتوبی برسیم
دونالد ترامپ، رییس‌جمهوری آمریکا چهارشنبه ۱۳ خرداد در کاخ سفید درباره حمله جمهوری اسلامی به کویت و شکستن آتش‌بس گفت: «ما سه‌شنبه شب حسابی به آن‌ها (جمهوری اسلامی) ضربه زدیم، و در واقع دیشب هم همین‌طور. و وقتی موضوع را برای من توضیح دادند، گفتم بسیار خب، پس همین کار را می‌کنیم، اما ما هم کمی داشتیم شدید به آن‌ها ضربه می‌زدیم.
ترامپ گفت: «بنابراین برای بعضی چیزها دلیلی وجود دارد، و معمولا دلیلی هست که گاهی منطقی به نظر می‌رسد. و خب، آن‌ها کاری انجام دادند که خیلی… مسئلهٔ بزرگی نبود. ما خیلی سریع جلویش را گرفتیم، همان‌طور که با بزرگ‌ترین ارتش جهان این کار را می‌کنیم. اما بعضی‌ها ممکن است بگویند که آن‌ها تا حدی تحریک شده بودند، چون ما به دلیلی دیگر اقدام قاطعی انجام داده بودیم. بنابراین آن‌ها در حال تلافی بودند.»
او در ادامه گفت: «خود مذاکرات بسیار خوب پیش می‌رود. بسیار خوب. اگر اتفاق بیفتد؛ ممکن است اتفاق بیفتد، ممکن هم هست نیفتد، چه کسی می‌داند. اما اگر اتفاق بیفتد، ممکن است همین آخر هفته رخ دهد. تقریبا اوضاع به همین شکل است.
آنجا بخش متفاوتی از جهان است، می‌دانید. من می‌گویم در آن بخش از جهان، آتش‌بس یعنی این‌که به شکلی ملایم‌تر به تیراندازی ادامه بدهید.»
ترامپ افزود: «تحت هیچ‌ شرایطی نمی‌توانیم اجازه دهیم ایران به سلاح هسته‌ای دست پیدا کند، هر اتفاقی ممکن است بیفتد وقتی با ایران طرف هستید، اما وقتی با کشورهای دیگر هم طرف هستید، این یک بخش بسیار بی‌ثبات از جهان است، احتمالا بی‌ثبات‌ترین بخش جهان.
رییس‌جمهوری آمریکا تاکید کرد:
«ما از سه تیم رهبری عبور کرده‌ایم. این یک وضعیت نظامی است، و واقعا هیچ ارتشی مثل ارتش ما وجود ندارد. ما می‌توانیم دو، سه هفته دیگر ادامه بدهیم و همه را کاملا نابود کنیم. ترجیح می‌دهم این کار را نکنم. انجامش خیلی آسان است. آن‌ها آماده‌اند که این کار را انجام دهند. می‌خواهند انجام دهند.»
ترامپ گفت: «اما اگر بتوانیم چیزی را مکتوب به دست بیاوریم که همان نتیجه را بدون کشتن همه به‌دست بدهد، من آن را ترجیح می‌دهم. فکر می‌کنم بیشتر افراد من هم همین را می‌خواهند. بعضی‌ها نه، اما بیشترشان بله. یعنی ما بالاترین بازار سهام تاریخ را داریم، با وجود یک درگیری نظامی یا جنگ. بعضی‌ها اسمش را جنگ می‌گذارند، بعضی‌ها درگیری نظامی. برای ما چیز بزرگی نیست.»
🔻
ترامپ: اورانیوم غنی‌شده زیر کوه دفن شده و می‌خواهیم آن را خارج کنیم
دونالد ترامپ، رییس‌جمهوری آمریکا چهارشنبه ۳ خرداد درباره خروج اورانیوم غنی‌شده از ایران گفت جمهوری اسلامی در مقاطع مختلف با این موضوع موافقت کرده، اما چند بار نیز نظر خود را تغییر داده است و این مسئله بیش از حد بزرگ‌نمایی شده است.
او گفت: آن‌ها [با خروج اورانیوم غنی‌شده از ایران] موافقت کردند و بعد گاهی هم مخالفت کردند. این یکی از چیزهایی است که درباره‌اش صحبت کردیم. خیلی هم بیش از حد بزرگ‌نمایی شده است. من خودم آن را بیش از حد بزرگ‌نمایی کردم.
ترامپ با اشاره به گزارش آژانس بین‌المللی انرژی اتمی گفت این مواد «نابود شده» و زیر کوهی دفن شده‌اند که تقریبا فروریخته است.
او افزود بیرون آوردن این مواد بسیار دشوار است، اما تاکید کرد: «من می‌خواهم آن را به دست بیاوریم.» به گفته او، آمریکا و احتمالا چین تنها کشورهایی هستند که تجهیزات لازم برای چنین عملیاتی را دارند.
رییس‌جمهوری آمریکا همچنین گفت سه سایت مورد نظر به طور دائمی زیر نظر هستند و در صورت هرگونه تحرک، آمریکا از آن مطلع خواهد شد.
او افزود: «اگر کسی به آنجا برود، دقیقا می‌بینیم چه اتفاقی می‌افتد و کمی هم بیشتر آن را منفجر می‌کنیم.»
رییس‌جمهوری آمریکا درباره مین‌روبی در تنگه هرمز گفت ایالات متحده از مین‌روب‌های زیرآبی استفاده کرده و مین‌ها را پاکسازی کرده است.
او افزود: «تنگه هرمز بلافاصله پس از امضا باز خواهد شد.»
🔻
ترامپ: ایران یک مشکل بزرگ جهانی بود و اگر مهار نمی‌شد، می‌توانست خاورمیانه را نابود کند
دونالد ترامپ، رییس‌جمهوری آمریکا درباره گفت‌وگو با حزب‌الله گفت آمریکا برای نخستین بار با این گروه صحبت کرده و سه‌شنبه توافق شده که شلیک انجام نشود.
او افزود اسرائیل نیز قرار نیست شلیک کند و تاکید کرد موضوع‌های مرتبط با تنگه هرمز، برنامه هسته‌ای و لبنان باید از یکدیگر جدا بررسی شوند.
ترامپ گفت بنیامین نتانیاهو، نخست‌وزیر اسرائیل، برای او «شریک بسیار خوبی» بوده است.
او همچنین با اشاره به نقش آمریکا در تحولات منطقه گفت بدون کمک واشینگتن، اسرائیل قادر به انجام عملیات اخیر نبود.
ترامپ افزود ایران «یک مشکل بزرگ جهانی» بوده و اگر مهار نمی‌شد، می‌توانست خاورمیانه را نابود کند.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 309K · <a href="https://t.me/VahidOnline/75929" target="_blank">📅 23:55 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75928">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ncjgwF4MClSDBl5C1aUbV_kWScuBoIkNwI9Cal4SoNfnrvC-Ogne4iNtfrwv7XH9IbNDA0i0jTf_RnAI-F82lkfOZt7Bl7-VeopMPnyzqjewLGE3hIhL_sCmRjelpPRhHA9BNbk2GlUGTzdRB5R1if80My1eSJrGns57WBiSffbVksJRplzusD2GUzhcNjZ_Sjml0cDnRcGwfxVOSbjMk0ovpLIKhKCrWbBtcIx0lg7Sazgzf7wYy01GMIHYqMNW8kdcSn78VKMcXTfuQGsqClsl1AOkjbSLD6GHSrGdPddOWwb6eHNmfw_f3ptJcr0sG8c6VWO_KzXteqIAK1HLWQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عباس عراقجی، وزیر خارجه جمهوری اسلامی، روز چهارشنبه تهدید کرد که حمله احتمالی اسرائیل به بیروت، پایتخت لبنان، باعث «ازسرگیری کامل جنگ» ایران با آمریکا و اسرائیل خواهد شد.
او در گفت‌وگو با شبکه المیادین، نزدیک به حزب‌الله لبنان، همچنین ادعا کرد که بعد از تهدید اسرائیل برای حمله به ضاجیه، حومه جنوبی بیروت و مقر اصلی حزب‌الله، نیروهای نظامی ایران در «وضعیت آماده‌باش کامل» قرار گرفتند.
عباس عراقچی در گفت‌وگوی روز چهارشنبه خود همجنین اعلام کرد که ارتباط با دولت آمریکا «قطع» نشده است، اما افزود که «هیچ پیشرفت ملموسی در روند مذاکرات حاصل نشده است».
ساعتی پیش مارکو روبیو، وزیر خارجه آمریکا، اعلام کرد که ایران هنوز تصمیم نهایی خود برای پایان دادن به جنگ را اعلام نکرده است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 288K · <a href="https://t.me/VahidOnline/75928" target="_blank">📅 23:51 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75927">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/sJ35_92HLR1bdYxjr1a9lMWtXcfwxKy9qIAKwQcDwn_NxGCYuYl148CkEhRdMfkcw0bhCkzWegEAjlle7tBbnNxzEWeIYor6GMOD4qpanWTxdTAi661a3VP-d0wYenUNjcujcprnqsrdCeA3K5B_mdLWhRQq_ROvb_OdDiMC2wStUNY5O-0QGrk08oskRM1shy44dG1Ys2dT6Yz4FUA8yd4ALiO70wBobMPEuEof99hdvzNb8MietldZJVX1qRx9fDuArXd4kfgQbtphKqfQii3KYt67WJvHj_CdojIHby5ECP-faGnmzydciKmz46rYyTTwwZpEx2__JmBwRVZhUQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سنتکام
ادعای جمهوری اسلامی
درباره شلیک به یک ناوشکن آمریکایی رو دروغ خوند.
CENTCOM
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 287K · <a href="https://t.me/VahidOnline/75927" target="_blank">📅 23:08 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75926">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/993ece4c51.mp4?token=CbUKGHyCZieTU9T1llRMotuU6B0xUY6ZWGJH7aUNvA_4zlfr0Hijb2k07lfmqNllma1PgbB4pg9E_wgSooh4vFAvEXRKU5CnM_RE6k2TqI0PxcK6ZLCQo0v9pzj4yqYrVrxnLyNFHnGRxfNxS0PVzAyIQcKVurhooPmJYIxmC4WmL-sRf3Iv0kFx-i1oDHHwfVboFvcds_e2UeXDDn03HBuu_TFGQ_fCCSHaDeXPw5fEG8_Lday626v9Aveke_f0EOqpGiovFcaBo20eG7TNf_Kp6ZjQYsu0gmfJPvPcnCQxccOSOW5uebbhDZjj32mjCn39BWn2qdA2tKqnhuYEhw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/993ece4c51.mp4?token=CbUKGHyCZieTU9T1llRMotuU6B0xUY6ZWGJH7aUNvA_4zlfr0Hijb2k07lfmqNllma1PgbB4pg9E_wgSooh4vFAvEXRKU5CnM_RE6k2TqI0PxcK6ZLCQo0v9pzj4yqYrVrxnLyNFHnGRxfNxS0PVzAyIQcKVurhooPmJYIxmC4WmL-sRf3Iv0kFx-i1oDHHwfVboFvcds_e2UeXDDn03HBuu_TFGQ_fCCSHaDeXPw5fEG8_Lday626v9Aveke_f0EOqpGiovFcaBo20eG7TNf_Kp6ZjQYsu0gmfJPvPcnCQxccOSOW5uebbhDZjj32mjCn39BWn2qdA2tKqnhuYEhw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شلیک موشک‌های ارتش به ناوچه آمریکا در دریای عمان
شامگاه چهارشنبه، خبرگزاری فارس نزدیک به سپاه پاسداران به نقل از نیروی دریایی ارتش جمهوری اسلامی از هدف قرار دادن «مرکز فرماندهی و کنترل ارتش آمریکا» خبر داد.
فارس نوشت: «ساعاتی قبل و درپی نقض مقررات تنگه هرمز و شرارت علیه شناورهای تجاری ایرانی از سوی ارتش آمریکا، نیروی دریایی ارتش جمهوری اسلامی، به‌محض کشف و شناسایی، «مرکز فرماندهی و کنترل» این شرارت، مستقر در یک فروند ناوشکن آمریکایی را هدف قرار داد.»
در رسانه‌های جمهوری اسلامی ویدیوی کوتاهی از لحظه شلیک موشک‌های ارتش به اهداف مورد نظر در دریای عمان منتشر شده است.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 285K · <a href="https://t.me/VahidOnline/75926" target="_blank">📅 23:01 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75924">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/EhGGKcbnAMFZCunsqEoAvD5VzBy3bLcyrepiQlsAoqTk3eLEuFyK3CYvUyZ_ulI0laodDSgxcx9NSNOmbutxVLpg4x2MM9kBr7DQZKgRvf909n-t8k1uRpt9uvyZ_cbImqd2DDb02TUA1g3Sx7rtTXQD9RtRnQ__zqWAi_vML6fmilzXDfn6h6dBZpsV0zTy6yik1ioyCezcZPWC8L1OpjI2cAjP_nsjsXXHssQeOt6yswwb9myTzO5tiXQifs4nkxpPNalKqbx2vBWamq-jxqJ0tVhql6NVbAsTEzFKMA1ZOWULtBgjGfiCy-5R959uADEijVq9JM5pv5Tem2m9Ag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/X8hTIlHTd6axJSRzDGZLFNpjaI-41H5ktKZ2C9iOr2CzFRTLrVtJxYK6EsusF5tbYsWc3wcXyMu4ZWYALb4LWh7cJZ9Vu7LDA9QdGTTqfqeI0InceCLCetcv_aipFlmaT4DrGIe1XcOKk7avjZTDdolX-dY6UGgxgBWQdwGV3pvN8aqFXA-ZUqnmvztH25kDtyl-zMPRxvfQLVIlBCzBa5i0Lx8OFQwEMEOQy7ZkBw_OVwhd6G1ARRLzt9JSITQHYR4MayIHy65gcvDHssuwPmhVYCrAAJGVabO_9Pl2KT1J2F45ZUtKocHh8-dEhK3foglNGmuhwTSaN02ao2MTcg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">فرماندهی مرکزی ایالات متحده اعلام کرد ادعای جمهوری اسلامی مبنی بر اینکه به ترمینال مسافری فرودگاه بین‌المللی کویت حمله نکرده و خسارت ناشی از یک موشک رهگیر آمریکایی بوده، «کاملا نادرست» است.
سنتکام اعلام کرد جمهوری اسلامی با پهپاد به این فرودگاه غیرنظامی حمله کرده و این اقدام را «عامدانه، محاسبه‌شده و بی‌دلیل» توصیف کرد.
@
VahidOOnLine
پیش‌تر:
حسین محبی، سخنگوی سپاه پاسداران، گفته است که تخریب ترمینال فرودگاه بین‌المللی کویت «ناشی از خطای سامانه‌های پاترویت آمریکایی بوده است.»
به گزارش رسانه‌های داخلی ایران آقای محبی اضافه کرده است که سپاه «هیچ شلیکی» به سمت این فرودگاه نداشته است.
او مدعی شد که بنا به تحقیقات سپاه: « تخریب ترمینال مسافربری فرودگاه کویت ناشی از خطای سامانه‌های پاتریوت آمریکایی بوده است، که پس از شکست در رهگیری موشک‌های ایرانی بر این ترمینال فرود آمده‌اند.»
در نتیجه فرود آمدن یک موشک در فرودگاه بین‌المللی کویت، دست‌کم یک نفر کشته و چند نفر زخمی شدند. فرد کشته شده تبعه هندی بوده و وزارت خارجه هند گفته چند شهروند دیگر هند نیز در این حمله زخمی شده‌اند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 276K · <a href="https://t.me/VahidOnline/75924" target="_blank">📅 22:59 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75913">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/hJH-YOGTeVm4Z82DZFFLXem67PDKsH3Ukp6YSJza-neud4VOlI-DavNoPLIqDaqO_97iS5dbsgzdLRmhPvMm8_1Waw8ek8tj3WgoY47MUwGfz57FD2doj7lFgFabMq8Kr4xrYvD7QK-QN1MlkscBOSF_1YDwZbn4qCYXuV8-wV76ui-1uNJ_4BpCE2OZc2n90Bs847-Ii07UWzeebAU9DLePXlZd9GaAGikA7lf1TJm0A7MA8LA9my0nIQBDP098VDtbqiu14eAgQJQdpn3bVpDKblxKqaUj6PvX7gMtg73WRzO_6c74GfBs6sZqdPqVPO-ysGEvVjCG3m7viJcIlA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/iD1Tw6m_cXU-9Ttag7ZU9uI7Zi3aLfPFYY95LpZbvfcMJtT7778IhiYC2CBBEiWkzk-QW4zGh7AA5a_6NMAgSHDNDIF5KvkMfe4sF50cf7PecbXZUGJOCkc_7TagMpzvGR6LGP62KZ222tIUm_vxkdVuNeNuTZSLefyjLwFOVxqT7nIbwbBPKLFO4dCUqHxe-41VzIb0kc2YrV_qdO0NPZh2FkTYVFeCxgfOSQi1QgvLZUhZu9kE50HWS0_pZklWUuZStKmx8w1nAM8tfCLiMVvc6kHbKK4K4MqY5GIgx_5bxHuTCmYlgEI_xBwEboAuCHXetmw_pm_2jOUovcnSow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/ZuH5yNF2-80oJbx4xnrLLsAnM4FNo4IT_Cc64eOpkKB3Owz2_MGMZc5UAWnnikyJbw1IhaIMpGUN07uZbLvGWYFBh3NVYiwAhHsr0W_qwVVkGZxNjitVCcRe2TWFp6sSTZj9MKv3wAyyhxudvw98vkrYELX15igF941zdGBaM43I98Nbg-y7OZb2wz0l0Mdhn5_K-SBCMqU2RcAGEUX7MS21j_lYQUAMEkm4IzyNSqbJ2T9fm9aN9j_QPdRRlJ-lsN0yPGrJ7ZP-_h4s0pI-WJLeG0grHuoDp8y04HwsHcKWvjW48OU-vx2RP0XcfUEFwjl65Y-HezXhkH-2LcU_pA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/QpPd-7bipumuAjmOIvIUVaVjqfkamwljyDtxBk9GjzrFhdQVyIWqR8ZuiOoTqOjcAg2-YEb7m0wce6ItCJ5PLtIxibGF0IGmn1HDaLBDIgBrpV00Wg-ZTMfYEa3c_GZUwSD_7tzDtsu3mgXlE9I7j-t1s_c0sDgNi46-cFn9UhY-VdYPgenk8Rz8gSpxgTiGThcc_aPKosrPXQmr0Q1SB8WDnBcqAzMvzEH1iZWXeXX_I0dzdbxin2D-8vMGol0_e-OjS7hNSsJXNDnLMP7Ci7oI7n4GWZxqc_mVt-C6mH34RsKiDImOLXRl-9fbYYLPlnOe7lmeuBnh7cSDZzHBGA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/NLbjPC1OKLAs3ShywBxwEqfV0ktVrWecETv7L_J25j6FynmNAsphW7Lo4HUIAB15fAVkqbkmeRD3TRaKaHCcI7s0xGw3kyU-R5Z9LwnDU28t5FY7eC9rKDqshsN0gAXkfdZrHJ6E0Lyo_NxB-44vL8Ai2Iv7udJk6dGLYP9oCu2_7ehnyiFT-JSdzi8EL5LwncRRZQh-EydCiHPOQZFD519sOF20Gc22zg9BiHp34fksxzVkxdik9RA16dU1fLcGviWJJAtLJCFyLtdG63WWEzyDjKfwESxab2qGXN1YZLxNOiRkeMkyX9vW3IZafTcHOGkTUVidGJfk70wRD1Gzqg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/UWHB9s6XEi6y9WHEvp5LtxNCaMRphs5vnq8LBrsoN9XW_Gs-r-pdU2ubWHXWpg6x5K-CG1lPR-yHMXGGJHkTAE6N2fDtBrqH4vLDuVo01S7B90tbFlOiMj3VJu_YkFflH6d0TNf78lL_1HgWH_vBNAp_1a3MmHvx6idQxjPYIJ0_eHNB32Y1wypxeqYwBRAbPKy0cbo9LlFQuUGCdZ8aGnUDWPnNXdVykSGlsgpiNj3s9lPak03a2QI6QhbPjyuhe4M1moU41ZgX9f-nqK7lUNVaqufI-_x4Z7kbDGeEw1HejYCqDYO5IfvmzYvufqVJkFVtSubazR4scjvViSl2MA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/GfjmlOEE9wJG4Pah5vJ1p-z0QfdPC7qngl8Pc1VmLf7Y0B1j9Ek6iSuYKyME-P0UqhQ5J-HM5z9ozXABYDyx_HiFylWIuKQbxhtoIR1Uvac7ku-GNdu78YAyzEwX7tGjrqPwvH3M3IrrGKo5Q47KJvm0GmQ1R_HbdYrj6QHuyrTuZxFtrjqF1O5puCLgQw2nUbIntrG45PnChC3ZgrkC4R-Ruy0WB6m7ksKi2A9YlM7CZoFojY0TA2fa_X_aYA92mruncg9MvxaQOTazIV6JY35l-JApfzR2kWoOT_ARYSlUibdc0hLKnI9_ZxOx-QUIuwbn2U76OLjmQ3-gjJcrwg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/DaPTjlCw3sEZBHlTvBF-k6OxXZLJEcQK6We33f0yKGnkE6Jpx6Wq1Hy5Y15pNZAQxXuRhlcF39KjXLXMhfYJFemSpdLHj_Z13ofXE0_90yrnqzEtsKvxTGDaeGOFZkLdpDkaY6sG2QoNSalrLrm5s3Q9UM8sph7xFtbxGiq1QQ3DGtIWXoQpMx1AG_IBBre78V0JoLs29ciMY2A0tvlN3jwRSwsyczTN48Djpsld2sXEU3y5Lyus6wGtt1uG7XQeiLG4M7SF9bHOvZkTFFnF5O27rX5ZahUAhAi2_Ja3lDZZPrKnVWbLU4vs04uQjrT7965dNw-o3uvnOr63CW_lIw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/iXsRbTSLeeaFCwijr6yOLjf3_rnykEz-u_Or5lElMn-9N4W-TrqCdWqFIoIKmxr3BdX7N2NUSziSq4dNYOAe5Re0ZXKck3NByhg1VhGPa_x1LyRurC7Ye8DfS6ilt09tas37C2oRAB74qY100eB3HdxCZuM_2bv1787vZkmrn-LOHxU9BkVwAnghNkXJoUK52I24l6WtGnod8biW78hG77WSBp7dSpzQ0QERTt0XZX1dXBZAI8ZvnsmMQVVX3U2DBCSOFjTUOciL6CrLNzHmP5c7XnDaPE3hQo_J0LEJQAvg4l4eyJHArprNtPAx0io4f04ZNHFWua24rJgUfVqIWQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/h_q_hMZYxSXsdQTEKfduD-5rnlQVxIzhNSuGhT8cwei3QPc4gDS25J7J-N_ZFyAFUynUxibx_-2Jmz90xE8AMVFWjfGShf8abuIJ9hiMz_cTfgz1PsmH2rHLSNLLdfui-CcZvSN85VWv9qIhnBChDpVILp_69ta_q8Gc8TriB_8hBxBgtizOidE5y4E2Y5Ea3KtYV_3SqHiKZK2GX9t1AXDT8AvVF8ptB3m0fEKOKgs2BUPgj-Kbp-Ynv1_25FBVN6D4JgRw1xSwNa8PEMerv_9518qDEo3mFhA7JWMbn_a1rBFDgGs8mAXgSA3I8agw07rqnPkrJZEhVgkE-zFjlg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">وزارت دادگستری آمریکا روز چهارشنبه اعلام کرد مدیرعامل یک شرکت فناوری در کالیفرنیا به اتهام تأمین تجهیزات آمریکایی برای نهادهای هسته‌ای و نظامی ایران بازداشت شد.
بر اساس بیانیه این وزارتخانه، جمشید قُمی، ۶۳ ساله، شهروند دو تابعیتی ایران و آمریکا و ساکن نیوپورت کوست در ایالت کالیفرنیا، به «تبانی برای نقض قانون اختیارات اقتصادی در شرایط اضطراری بین‌المللی» متهم شده است.
او متهم است که «تجهیزات پیشرفته شبکه، امنیتی و رمزنگاری ساخت آمریکا را برای مشتریان ایرانی، از جمله نهادهای هسته‌ای و نظامی حکومت ایران تهیه کرده است.»
وزارت دادگستری آمریکا همچنین اعلام کرد که جمشید قمی از «شرکت‌های پوششی» در امارات متحده عربی برای پنهان کردن محموله‌های تجهیزات شبکه و رایانه‌ای که مقصد نهایی آنها ایران بود، استفاده می‌کرد و این شرکت‌های واسطه برای مخفی نگه داشتن مقصد واقعی کالاها و دور زدن تحریم‌های ایالات متحده به کار گرفته شده بودند.
جان آیزنبرگ، معاون دادستان کل آمریکا در امور امنیت ملی، در این بیانیه گفت: «طبق آنچه در کیفرخواست آمده، قمی با تأمین فناوری آمریکایی برای سازمان انرژی اتمی ایران و سایر نهادهای تحریم‌شده مرتبط با برنامه هسته‌ای ایران، به ثروت دست یافته است.»
او افزود: «بخش امنیت ملی وزارت دادگستری افرادی را که برای پیشبرد اهداف هسته‌ای ایران قوانین ما را نقض می‌کنند، پاسخگو خواهد کرد.»
به گفته وزارت دادگستری ایالات متحده، متهم بیش از ۱۵ میلیون دلار از ایران به حساب‌های بانکی خود در آمریکا و یک حساب امانی منتقل کرده و به‌دروغ این پول را به سازمان مالیات آمریکا به‌عنوان ارث خارجی اعلام کرده است.
بر اساس این اتهامات، اظهارنامه‌های مالیاتی فدرال او تقریباً هیچ درآمدی را نشان نمی‌داد و بالاترین درآمدی که در هر سال گزارش کرده بود تنها ۲۰٬۶۸۴ دلار بوده است.
وزارت دادگستری آمریکا همچنین مدعی است که او از درآمد حاصل از «طرح دور زدن تحریم‌ها» برای تأمین هزینه ساخت یک عمارت چند میلیون دلاری در اورنج کانتی کالیفرنیا استفاده کرده است.
@
VahidHeadline
دادستانی علاوه بر درخواست مجازات حبس، به دنبال مصادره اموال وی از جمله عمارت گران‌قیمت اوست.
بازپرسان معتقدند او به مدت بیش از یک دهه از طریق شرکت خود در تهران به نام «فراز پرداز رایانه»، بیش از ۲۵۰ تن تجهیزات کنترل‌شده تکنولوژی را به‌صورت مخفیانه خریداری کرده است.
او متهم است که با استفاده از حساب‌های شخصی در eBay و PayPal و از طریق شرکت‌های صوری در امارات کالاها را تهیه و به ایران ارسال می‌کرد.
@
VahidOnline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 323K · <a href="https://t.me/VahidOnline/75913" target="_blank">📅 22:00 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75911">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/o0hsy8EgkG_qW4zts1ZM_9JgAJi6auEF2hfMrsjBiaRYxKAeKT87LGR_psLkaYq1y_S_xWUDOUBZMCuW7pOMzA7glfGys6zwsbvMVeWqf2ENe7hawAtKQLtpQ-pKFwdylDfpaP6Wf39zbmbPiqAgkAk8orZ3T4qPrEFaudOEHoEqs1uw33ly88kUTj5iA6XtNLK32Fp_EqETmWHxH_yd73rlcA98gfpmXDUWuwyZeuL75PpQvWBb9hTRJMXYPE3kbQ_uzZtly_yCP-BoUe3O_Oiv_Sab5_sHnzl_9Rk0vuwZSdLqUlwzkANySSsqj9kzZkdDflHpGLKOFjJM9kHhAg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/k9vGZCsI_qWoIx5gVdHajgc_0o6RJHmH6M4hEx5ZU5DIyoOR4zjw9NoTlKjA8fCSaGJrZnWjPeqmJJUoK6Dw5PPF8591UHlCJCvvtc0U9nIPVzbl4HMwfaBzJsUwjxo0-R70zDjoaIdQcOQ3Ky0JaVDKIjaDCUlqDa_DRwM7rXvpJCZFzmVq-AyY1p49MCh5TfsFB2Rnf0S-NuUNoGJgKDmOB9YSyzZCCl8Q2ju96s3_-sAQIU0aX0AB0FJFo3hrEOBpFInkXebOSgx_LJ0T9gvCX88bhTYO6YYfpRHUC-i5WMxnSRr3grRqbAhc7jDLPU_pzdxomTpuJfkL5yTlog.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">سی‌ان‌بی‌سی، ترجمه ماشین:
▪️
نتانیاهو از پاسخ به سوالی در مورد اینکه ترامپ در تماس تلفنی این هفته به او فحاشی رکیک کرده و رئیس جمهور آمریکا گفته است اگر او نبود، نتانیاهو الان زندانی بود، طفره رفت.
نتانیاهو در پاسخ به سوالی در مورد اینکه ترامپ ظاهراً او را «دیوانه» خطاب کرده است، گفت: «وارد جزئیات نمی‌شوم.»
[ولی ترامپ در
مصاحبه با NBC
گزارش آکسیوس رو تایید کرد که بهش گفت دیوانه]
▪️
نتانیاهو می‌گوید او و ترامپ «اختلافات تاکتیکی» دارند اما «در مورد مسائل اصلی اتفاق نظر دارند»
نتانیاهو هرگونه اشاره‌ای به اختلاف با ترامپ را کم‌اهمیت جلوه داد و گفت اگرچه آنها گاهی اوقات «اختلافات تاکتیکی» دارند، اما «در مورد مسائل اصلی اتفاق نظر دارند».
او گفت که این موارد شامل جلوگیری از دستیابی ایران به سلاح هسته‌ای و تهدید اسرائیل با آن می‌شود.
او گفت: «گاهی اوقات، مثل بهترین خانواده‌ها، این اختلافات تاکتیکی را داریم. اما ما همیشه راهی برای حل آنها پیدا می‌کنیم و این کار را به عنوان دوستان خوب انجام می‌دهیم.»
او گفت: «ما می‌توانیم صبح اختلاف نظر داشته باشیم» و تا بعد از ظهر به زمینه مشترک برسیم.
▪️
نتانیاهو در پاسخ به این سوال که آیا واقعاً آتش‌بس با ایران برقرار شده است، گفت: «فکر می‌کنم یک بازی تاکتیکی در حال انجام است.»
نتانیاهو گفت: «و ایران مطمئناً می‌داند [ترامپ] چه گفته است، اینکه در صورت لزوم، بازگشت کامل به اقدام نظامی وجود خواهد داشت. این تصمیم رئیس جمهور است، اسرائیل آماده است، و نیروهای آمریکایی نیز آماده هستند.»
او گفت: «فکر می‌کنم ایران باید این را در نظر بگیرد. فکر می‌کنم آنها دارند این را در نظر می‌گیرند که دارند با آتش بازی می‌کنند، این واضح است.»
▪️
نتانیاهو از اقدام تلافی‌جویانه ترامپ در محاصره بنادر ایران در تنگه هرمز تمجید کرد و آن را «بسیار مؤثر» خواند.
او گفت: «محاصره معکوس، یک حرکت هوشمندانه بوده است.»
▪️
نتانیاهو گفت که «هر دو روز یک بار» با ترامپ صحبت می‌کند.
او گفت که دو رهبر «اهداف مشترکی دارند... ما می‌خواهیم به آنها دست یابیم.»
اما در پاسخ به این سوال که از توافق آتش‌بس احتمالی چه انتظاری دارد، نتانیاهو اذعان کرد که «این یک سوال بی‌پاسخ است که جنگ چگونه باید پایان یابد.»
▪️
نتانیاهو گفت نهادهایی که به نفت ارسالی از طریق تنگه هرمز متکی هستند، در حال حاضر «در حال توسعه مسیرهای جایگزین» هستند که کمبود عرضه انرژی ناشی از بسته شدن مؤثر این آبراه کلیدی در طول جنگ را جبران خواهد کرد.
▪️
نتانیاهو انتظار دارد که تغییر رژیم در ایران رخ دهد زیرا رهبری فعلی «به شدت» تضعیف شده است - اما پیش‌بینی نکرد که این اتفاق چه زمانی رخ خواهد داد.
نتانیاهو گفت: «شما نمی‌توانید دقیقاً پیش‌بینی کنید که چنین رژیمی چه زمانی سقوط می‌کند. شما در بسیاری از موارد آن را پیش‌بینی نکردید: نه در رومانی، و نه در سقوط دیوار برلین، و هیچ‌کس آن را پیش‌بینی نکرد، اما این اتفاق افتاد. چرا؟ چون ترک‌ها از زیر در حال گسترش بودند.»
او گفت: «در واقع، شما همین الان در ایران شکاف‌های عظیمی دارید و نمی‌توانید پیش‌بینی کنید که چه زمانی این اتفاق خواهد افتاد.»
«اما من دیروز در یک نشست عمومی اینجا گفتم... ببینید، من معتقدم که در نهایت این شکاف‌ها گسترش پیدا می‌کنند و رژیم سقوط خواهد کرد و ما تمام تلاشمان را خواهیم کرد.»
نتانیاهو گفت: «من فکر می‌کنم که ما باید به مردم ایران کمک کنیم تا این رژیم را سرنگون کنند، و این تغییر نکرده است، اما دقیقاً در لحظه‌ای که ما انتخاب می‌کنیم، این اتفاق نخواهد افتاد.»
او گفت: «فکر می‌کنم آنها به شدت تضعیف شده‌اند.»
nbcnews
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 330K · <a href="https://t.me/VahidOnline/75911" target="_blank">📅 19:01 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75910">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/GjFybxQSwCyzekvS3I4bDa4jtRD_bNW5DBIYmeJQNzWPkR1jALxmdYMVdov3nHas7jNN40JmK0hNMtEYM-Np8PeWVra7W-Xatua2zUn-o6nRx8chr0iJrzQ9JP0Nd-prWf53HmxbwpfPmsP0aPDpkND13asl_osT8ZRWVAK7ja2JjZoBaPwqGk9rMwtHsDU-N0tp-KSbZegue1-AK6PzQYdTl-_eam5zQ8g1nSMkmpDjMAd6CoJ5bi1sVpGG1x0ddZbVIr3nI9D59bz93v-b_xDOaHqmP1PA_yVY8_Q46HwOY3WJ8Rk9gOJH7TLJBdXh-J-legcH61N4Zd7OYe35Gw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مارکو روبیو، وزیر امور خارجه آمریکا، روز چهارشنبه گفت که سرنوشت ذخایر اورانیوم ۶۰ درصدی ایران در مرکز مذاکرات با واشینگتن قرار دارد و تهران هنوز با یک توافق صلح موافقت نکرده است.
روبیو در جلسه کمیته روابط خارجی مجلس نمایندگان آمریکا گفت: «فکر می‌کنم اکنون در برخی از اسنادی که میان دو طرف رد و بدل شده، این موضوع به‌طور واضح مورد توجه قرار گرفته است، اما تا صبح امروز هنوز تأیید نهایی از سوی نظام تصمیم‌گیری آن‌ها را دریافت نکرده‌ایم.»
روبیو در مجلس نمایندگان آمریکا بار دیگر بر اظهارات پیشین خود مبنی بر پایان جنگ با ایران تأکید کرد و گفت: «ما دیگر حملات مستمر در داخل ایران برای تضعیف توان نظامی آن کشور انجام نمی‌دهیم، زیرا عملیات "خشم حماسی" به پایان رسیده است.»
روبیو با تأکید بر اینکه آمریکا به اهداف خود دست یافته، افزود: «ما پیروزی را این‌گونه تعریف می‌کنیم: نابودی زیرساخت‌های صنایع دفاعی ایران، کاهش قابل توجه تعداد پرتابگرهای موشکی که در اختیار دارند و کاهش چشمگیر ذخایر پهپادی آن‌ها.»
او ادامه داد: «ما به همه این اهداف دست یافتیم. علاوه بر آن، آنچه از نیروی هوایی ایران باقی مانده بود را نابود کردیم و کل نیروی دریایی متعارف آن را از بین بردیم.»
با این حال قانونگذاران حزب دموکرات در این نشست موضع آقای روبیو درباره پیروزی آمریکا را به چالش کشیدند.
از سوی دیگر ایران بامداد چهارشنبه کویت را هدف حملات پهپادی و موشکی قرار داد که به گفته مقام‌های کویتی باعث کشته شدن یک نفر و زخمی شدن دست‌کم ۶۳ تن دیگر شد.
@
VahidHeadline
📡
@VahidOnline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 346K · <a href="https://t.me/VahidOnline/75910" target="_blank">📅 17:58 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75909">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">پیام‌های دریافتی ساعت ۱۳:۴۵
سلام وحید همین الان بندرو زدن فکر کنم فرودگاه یا پایگاه هوایی بود صداش زیاد بود جوری که تا شهر نمایشو لرزوند
بندرعباس سمت اسلکه صدای انفجار یا بمب
وحید جان بندرعباس صدا انفجار خیلی بلند 13:45
بندرعباس رو زدن خیلی بد بود این دفعه صداش از همیشه بیشتر بود خونه لرزید
سلام ساعت 13:46 بندرعباس صدای انفجار اومد.
غرب بندرعباس
بندرعباس صدای چندین انفجار سنگین همین الان شنیده شد
همین الان بندر رو زد
سلام ، ۱۳:۴۵ صدای ی انفجار با لرزش شدید بندرعباس
سلام 13:46 صدای انفجار بندرعباس
وحید بندرو فکر کنم زدن صدا انفجار اومد
سلام همین الان قشم صدای انفجار شدید اومد
هرمزگان صدا اومد
بعدش این خبر منتشر شد:
"معاون سیاسی، امنیتی و اجتماعی استانداری هرمزگان گفت: صدا‌های شنیده شده در شهر بندرعباس ناشی از انفجار‌های کنترل‌شده مهمات دشمن است."
(گزارش درست اینه که: صدا شنیدم.
از روی شنیدن صدا نمیشه گفت "زدند"، "حمله شده" و...)
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 320K · <a href="https://t.me/VahidOnline/75909" target="_blank">📅 17:20 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75908">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Ir1-0EVPwT6KfsVcZ0hOhhTPIvcfIUypZNRZkmLQKRQjFofsTBQnVmD985IhRViY4ApC8i4RyZjBzRrRlJ1k-8-8SsEjdVvsPCdEvV2_0RQOarkN9IsQwehf23S1LcK9JOxSSJDDF7tWMorlnxwEBXmHfszlkCzvNxBnjWKlNpZCjcc_p_KiHat1gdn_dtM02AXp-ewRCPL_Ll9F4ixaU59hDxD3zO7zcRVEjHo9TmBwol9uFZugOLSWJrdoKFgehIFLPNbbjW_9tcsy1xCNHbeAhq4bt1grIhZ9gVA_nWZnQ5EKHcsUsycSLTdnpqwzdQ3Gi9aJd3HSCSsGE5QWDQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کاظم جلالی، سفیر جمهوری اسلامی در روسیه با اشاره به سفرهای علی لاریجانی دبیر سابق شورای عالی امنیت ملی به مسکو گفت: سفرهای او، به جز دو مورد که خبری کردیم، بقیه محرمانه بود. یعنی هم ما و هم طرف روس، سفرها را رسانه‌ای نکردیم. فقط دو سفر اعلام شد.
جلالی به خبرآنلاین گفت، لاریجانی سفرهای محرمانه زیادی به روسیه داشت و در یک سال‌و‌نیم اخبر، هفت بار به روسیه سفر کرد. جلالی بدون اشاره به دلیل این سفرها و موضوعات مورد مذاکره گفت: «در یکی از این سفرها، طرف روس با من تماس گرفت و ابراز علاقه کرد که سفر رسانه‌ای شود و آقای لاریجانی هم مخالفتی نکردند و خبر آن منتشر شد. اما سفر آخری که در ۱۰ بهمن‌ماه ۱۴۰۴ صورت گرفت، به شکل دیگری رسانه‌ای شد.»
جلالی افزود: «ما دیدیم وقتی هواپیمای ایشان حرکت کرد، سه یا چهار هزار نفر در فلایت‌رادار آن را تماشا می‌کنند. زمانی که هواپیما در مسکو نشست، این رقم به ۳۴ هزار نفر رسیده بود. برای فلایت‌رادار، این عدد بسیار بالایی است. بعد هم یک‌سری شایعات شکل گرفته بود. در ماشینی که ایشان سوار شدند، به ایشان گفتم که این سفر را باید رسانه‌ای کنیم. پرسیدند چرا؟ گفتم با توجه به حوادث ۱۸ و ۱۹ دی، الآن عده‌ای از ضدانقلاب‌ها تلاش می‌کنند این خبر را به شکل دیگری جلوه دهند. برخی نوشته بودند که رهبر نظام به روسیه رفته یا برخی گفتند که پول‌ها را به روسیه برده‌اند و این خبرهای عجیب زیاد شده بود.»
جلالی در ادامه گفت: در ۱۰ بهمن، زمانی که علی لاریجانی با پوتین ملاقات داشت، در پایان جلسه من گفتم اگر اجازه دهید ما یک خبر کوتاه، با هماهنگی، منتشر کنیم. به این ترتیب همان دو سفر رسانه‌ای شد.
سفیر جمهوری اسلامی در روسیه همچنین گفت: پس از کشته شدن علی لاریجانی، پوتین متن پیام تسلیت خود را آماده کرده بود اما گفتیم منتشر نکند تا اول رسانه‌های داخلی خبر مرگ را اعلام کنند. [چون فعلا به مردم کشور خودمون دروغ گفتیم و ضایع میشه!]
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 317K · <a href="https://t.me/VahidOnline/75908" target="_blank">📅 17:06 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75907">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZQ2QwON7evbFHKhcE16K-o0B5ItLMxwmw4K91btsJp9WYFpmeJ6pS22tieNoVBcgCwirWIrXUuN2EInTrTsp4QLUn-Tk8DUhITRQgDFFN4z7uGnmzKkoB6XxuuGc8fQIWrU6C9ETr-KYC5siJfesbixVh_vulcQmIq_OH7DbAMpLi5XoH5mKXktM0HpUBMwOY_SKuCX4_jrKkCHRwlhh2T0qkxOIC11I8qRm8fKRaP1XyvA5_RKVZjLYUvnxfGqeoXqP5rZbDA-HrmUeKgL8_OR6NNu12WJ-D26MKbEzbc-YRXZQ_6TVmkTfkrZSEP1iTjJIwRAoItdW4HPLKjUfSA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دونالد ترامپ، رئیس‌جمهور آمریکا، در گفت‌وگو با پادکست «پاد فورس وان» متعلق به نیویورک‌پست گفت که جمهوری اسلامی موافقت کرده که سلاح هسته‌ای نداشته باشد، اما همزمان یادآور شد که تهران همچنان می‌تواند «نظر خود را تغییر دهد.»
او در این مصاحبه که روز چهارشنبه منتشر شد، گفت: «ما باید کاری در قبال ایران انجام می‌دادیم، زیرا صرف‌نظر از اینکه وضعیت ما [از نظر اقتصادی] چقدر خوب است، نمی‌توانیم اجازه دهیم آن‌ها سلاح هسته‌ای داشته باشند.» پرزیدنت ترامپ اما اضافه کرد که «آن‌ها از قبل موافقت کرده‌اند که سلاح هسته‌ای نداشته باشند.»
وقتی در این گفت‌وگو از پرزیدنت ترامپ سؤال شد که آیا رژیم ایران با این شرط موافقت کرده یا خیر، او تصریح کرد که «بله، آن‌ها با این موضوع موافقت کرده‌اند.»
او اضافه کرد: «منظورم این است که آن‌ها اکنون می‌توانند نظر خود را تغییر دهند، اما این یکی از چیزهایی بود که باید با آن موافقت می‌کردند و موافقت کردند، این موضوع اصلی و بزرگ بود.»
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 270K · <a href="https://t.me/VahidOnline/75907" target="_blank">📅 17:03 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75906">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KcTjlJSSvzkmEVCRDxBFWU4xcR0mTAAiA5x1uJ_3wxqSTLwkQ54Rohj-AQwRnjBKP5j6xChO5TxW_U-pXjthgHl8Vh_6qHVOYZTUnPtUh3mZrB1fdpgekQ2Jjyo69vUSmKl80JJL1BIEKI9aORKp5VSu9AHVf92rtW0jo0G4x8Eitr-hr9fNrUEhMgym9hq4gz4uKhQ7pEg6DGVw41-R8czHCQYy04vcSaPNV6IZf892R7EuxbF2oX7vHSk-pxNoAxXu4gjWuxcUrzG8t8vts20wR-cIQfkxUCJiXnT2MlQHrKGNmKmHQOkO2lYCDg5p7Hw5Hgt2XDs5D4RJg76DCw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزیر خارجۀ ایالات متحده می‌گوید این کشور مصمم است مانع از تلاش ایران برای «جا زدن» افراد مرتبط با سپاه پاسداران در کاروان تیم ملی فوتبال برای شرکت در جام جهانی شود.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 255K · <a href="https://t.me/VahidOnline/75906" target="_blank">📅 17:02 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75897">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/T-RE8KuFr8CcE8yPmotQJq_60rNEYhObNCv5JX_OtaI60vVrMISMeaERx-bWVesXkl0BYpII4WLX-s8IRerbfE2o8L8jxV2nNpywDo0CVMh91voyOWgvHvClyZ5awoonjQMi5DDe7rFCfVrgqqPOd2uHbd-XvDeXPRbmQJ-3z7YzRYK9xVdtRTxD3rpRIqXSMTB7GpCXYr5XsvJbWzkyrGQ-M1RHbyfUg_lqY9yePK288n2LSlCTbCqvXlYYo5aRww-70UPa5XLNpsLYazIWXeW6cKUA9Q7HvlM9kAApeADFaR0MQYqQKH7rR5_F4ohZ9UUcPO1pw7FfM5499qrZqg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/BTSq0n4abKiTItr7U7ur0GdTEJn4XKWJq2Ck-qDFbP6o3R0c7hcWXNzvQt3ahNZOGZFh6DUMPH0oo08zlnYW5BwqZTh1mLRHpvGFCpwr-LyCCPbR2CRlI1JJk9VaT01X6FLkNzgMfp4v3Enk7Batgi5T87ex5ZO54dhPp-n33koL49D2jxtqUgmaYrm37lU5sFId34BBML9fq9R9yOolOezPDEIbVJaXjgkcBciW0VGlm9_0fW-wPOrEkDt-tweobRN8PHN1YbtZywKKCKdMy0-K2m1zbG3XDoRVAJG3-3rzkGPRbGy_YmT2gKibNmdJCpA_V0fAD7Of2KvN59oe8g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/Dm4a7EFimEHRkRZ4jRj-kSdsuUB6eGrjfEJAx8G8ACqz6hQ1iE5oZEOWHyRWMGf7QJeQwJYc9YD9t0FJougqpa7GGZFFZGQSnhLvkc0i9-Zir4HZqj4jBOKLkqONyph62l1c8t_eRBs9FOITeMjjjz1miH2e2VuRa5LG-9-3MdFPh6OGfurNGDRWMBHMy9KXVGyb8Q_xUl8a9i-LcAbRXdOp5F8OLkZBLZkR_QxSkSuXgv5sRR9B1xyMA40Ty4u9TX-1hBJ7_i8aoJvjSE-d5T0JW43Z4XL2Gf3yvwYqDkaQeKi9P8eSxZmWJI7kshoL1BXe3MMBjt0h4DuU_YJLOA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/icWMcuVpgEWer1w7HXrvofZqG0ImMvbCt0imNEXut8qPkgKr69SRrSwfojhHXbB3q8UzhxZp_hCV1A2AEjoYL7akEUlYSm-5jDKJHkaiiGe7RuACQwF8ZsZTvvvJIfUdvi6_MJzBLBjdTtk94e7BnrmEmEyb7Adv0d0VhPfOqNgOJxV0RE0ijsIq_rDczoLtnz_GZZiWLeYNYjElnI4jv5QIEpovJMOq8x9K-emlYV3-8rosfs1M5lC3fpzuU8PhilwB_p_cD8OJvZGOdhtBjBtRiMMzna5jbM7zkPmLjchTPXbxhyRQ34UlZFvVmkRf-agFGMKLLWSY-yvzHzCfhg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/i-ZxSJQRIOwfWpPRaYCpnNbxxEpcQPZGKBH0S174svhQL6EpgAm98VtjY5MV31vrZ7eV26vHKdDQwXzusIn_vwTkvtPqj6C51lk12v5YN_CyDZPEHESk2F09qpfWfFdYLbh3scZ8SXRHU_Njit3H6hyEhkyO-3sUMGmha7G59tBWXuadNQFd33xrh3uwuJWF_AJyRCByOgAUB6yW6_w3ITsHXeigENTswdq_yEapOMI5gCFgJimUK5cTxI97HkqGDyFyRveEb09c_-FEnz4i7U7Rh7Bj_ZrvPSZbT4ZyK35Db7vxqVx8S6Eyd-e97cUJFqtWRYawYj2ESqDkdh1lQw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/I5MlyVjXHhXb4lBg9XzJVx39GYs_3pjbqsElrzjMLwNJwbGjFwIlnGCbI6xH7yZDpHqxgZLPhSsfXGEbPqJVsKOQ8hfXcpz1eE1g8sdPk56rGM_aG_zQngHC3ZpJxkdngJq2YxdlcyAAmDBlDDNAOrcfa1Ou5WPOTD7Ue3NyPYXu8Q0HZu7xqSuaVS6y0bVtr7_iR_IyyKED8l_FYC5nVzMff6u4yhyDImcC4izDA7UJ9uaHNVd5fxGmd0WNsLvoq_6w78nirdFrwfMZjJBKniI8_0M8hwAWV7d4HbwII2yDV0SHtj7NDmA4nDT-Z6p3dxvGcYkGsdShfWzQWYb7kw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/DhOtnLfkcpxA4F8FzxQZdi8Bt_xCtfdlEmuZt_Hr3AOo6Nny_iVk8m8yo-KflDqjotb56TfQbOEfF4tXo0yRdif_4fSkZIOHYJUtqrJAWNA0mCsK476Qes8IWKymQqK6SUA-mfIPhuow6bne5OIICapcYHsw3c9WM0J8zlkdIBp0VkWBZPkff_cC67D7URNQ7VcKARZjgAjb7RiKK0XxvGjCi9f8IaE0AtxLleb6mUlUMQ66eAHPpyxaZWG6PYAbOWHYOtUGElH51QdljcZl_sCL32ayCnhdH8VDHZNCccsfW_jO8vQ6Ct85I95bNVpZEm5A-sJsbygufnppPcKG7A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/sZLhBX_-mml2TpKTuCUR2R8QlPvcU7xmjI5zBzGLHggvV0OwSmaaeu3zPtHZaTR8syT65Zjhei6EMmzbpour0fKw6kM8XFHqjl81cO94owhgyv1pqIzMtycSePE5HxRaRM0XcEndZ-ZGlBwuZqdVNUfxB46-yMhnFE5Tvn67lc16sJ1m9qugDdrGHpaqJVAP2dTYIQhgMxbCZcDdpUsxTURQptXuSI9hiIUMxBBLa9vELE-_N987rOSXOuirajuha3spZBqsfPxkhoZeUaaZOSsMhUiSE0efGnYEug-nqG-yqwmXJuUIrkwwS9dK1KAKoK09now2LmFZROWmVls1hg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/1acb519b46.mp4?token=Uxw8E-wYsFj_vFWUS4NJUp7kxHpHSxXYHo-8unsy1seFsTY7A8UrCeUpYPPzvHWSn87pcLNEUgKWS4WkWsUZbsESDxV0XhCBmnphOJwtXgJApnUP6tOoxmXbFRdVSoLGosHjRecdGF3WXsO1m6n4C0S4J82833AuR6KJHr2UkXZV_G-4OVt5GJy9LQTWRprK1EYmWmtmOjF31byYXhS_otQK-fZHmDjwB4fQCKc6_bcEKO4fCrkuzVgQChP0aeHHaxpAeaoEu1mANpoIIoo29v8N7DyhOpXwEKNPWuuTv4uHKEkmQ3TPf_LGsy07ZlRdzKtuXGbkv5S4ZGlTlYckVA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/1acb519b46.mp4?token=Uxw8E-wYsFj_vFWUS4NJUp7kxHpHSxXYHo-8unsy1seFsTY7A8UrCeUpYPPzvHWSn87pcLNEUgKWS4WkWsUZbsESDxV0XhCBmnphOJwtXgJApnUP6tOoxmXbFRdVSoLGosHjRecdGF3WXsO1m6n4C0S4J82833AuR6KJHr2UkXZV_G-4OVt5GJy9LQTWRprK1EYmWmtmOjF31byYXhS_otQK-fZHmDjwB4fQCKc6_bcEKO4fCrkuzVgQChP0aeHHaxpAeaoEu1mANpoIIoo29v8N7DyhOpXwEKNPWuuTv4uHKEkmQ3TPf_LGsy07ZlRdzKtuXGbkv5S4ZGlTlYckVA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وزارت خارجه کویت روز چهارشنبه ۱۳ خرداد اعلام کرد در حملهٔ پهپادی ایران به «تأسیسات غیرنظامی» این کشور، از جمله فرودگاه بین‌المللی کویت و برخی نمایندگی‌های دیپلماتیک، یک نفر کشته شده است.
وزارت بهداشت این کشور نیز اعلام کرد در این حمله دست‌کم ۶۳ نفر زخمی شده‌اند.
وزارت خارجه کویت در بیانیه‌ای که ساعاتی پس از گزارش‌های اولیه از حمله منتشر شد، مشخص نکرد که کدام نمایندگی‌های دیپلماتیک در این حمله آسیب دیده‌اند.
ساعتی بعد وزارت دفاع این کشور اعلام کرد که روز چهارشنبه ۳۰ موشک بالستیک و پهپاد را که ایران شلیک کرده بود، شناسایی کرده است.
سعود عبدالعزیز العطوان، سخنگوی این وزارتخانه، گفت: «از بامداد امروز، نیروهای مسلح ۱۳ موشک بالستیک متخاصم را در حریم هوایی کویت شناسایی و با آنها درگیر شدند. این موشک‌ها بر فراز چندین منطقه مسکونی رهگیری شدند که در نتیجه آن، بخشی از بقایای آنها سقوط کرد.»
او خبر داد نیروهای مسلح کویت ۱۷ پهپاد متخاصم را شناسایی و با آنها مقابله کردند و افزود: «این تجاوز شنیع ایران، تأسیسات غیرنظامی و حیاتی را هدف قرار داده بود.»
وزارت امور خارجه هند اعلام کرد که یکی از شهروندان این کشور در فرودگاه کویت کشته شده است و این حمله را محکوم کرد.
این وزارتخانه در بیانیه‌ای اعلام کرد: «ما بار دیگر از همه طرف‌ها می‌خواهیم که به چنین حملاتی علیه اهداف غیرنظامی پایان دهند.»
پیش‌تر، خبرگزاری دولتی کویت گزارش داده بود که حمله بامداد چهارشنبه به فرودگاه بین‌المللی این کشور چندین زخمی بر جا گذاشت، فعالیت فرودگاه را به حالت تعلیق درآورد و برخی پروازها به فرودگاه‌های دیگر هدایت شدند.
اداره کل هوانوردی غیرنظامی کویت هم اعلام کرد ساختمان ترمینال شماره یک فرودگاه در این حمله «به شدت آسیب دیده است».
شرکت هواپیمایی کویت نیز اعلام کرد پروازهای روز چهارشنبه خود را تغییر زمان‌بندی خواهد داد. با این حال، اداره هوانوردی غیرنظامی این کشور ساعاتی بعد خبر داد که پس از ارزیابی خسارت‌ها و اجرای تدابیر ایمنی، پروازهای شرکت هواپیمایی کویت از ترمینال شماره چهار از سر گرفته شده است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 239K · <a href="https://t.me/VahidOnline/75897" target="_blank">📅 17:01 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75896">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/THoMtmVdgj8i3iwj0Pp4oo3k67qyEbcv7tKtlPuVdaqbexUv80z-wvPNLULmmHz2gWtSZH8g-x8hFgx92e6jFxaTgdTpyvbzSVgXwX8cAQLrd234HicZ8h7jJ50STtTie5QUNnldsT_aaPeMQsHJKQp_Ujz22_BiJDkjGF2W5FyJMCYWRR62EEFGYPX1lV1Rn7_z6JdITKuVabWM8-OJtWGBBJkOPIKrRT3hRdXDBLJ17yspFNC199-O05CjqQRIXz8sBW91574SyqfIUP8gv6RWCcmjxi6Dk-bofGDGtm9OQvxH-jB0tfkCXxWUerrYuPbMeaSDuhS8Q5FcXWg9LA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرگزاری میزان وابسته به دستگاه قضایی جمهوری اسلامی، از اجرای حکم اعدام فتح‌الله آوری، به اتهام قتل محمدجواد بخشیان، از نیروهای انتظامی در جریان اعتراضات دی ماه ۱۴۰۴ در همدان خبر داد.
خبرگزاری میزان مدعی است که در زمان دستگیری، «آلت قتاله (چاقو)، هودی مشکی و همچنین همان کتانی سفیدرنگی که در تصاویر دوربین‌های مداربسته محل حادثه مشاهده شده بود»، کشف شده است.
خبرگزاری میزان مدعی شد که آقای «آوری» دارای سوابقی چون «آدم‌ربایی»، «ضرب و جرح عمدی»، «تهدید با چاقو» و «شرکت در سرقت مقرون به آزار» بوده است.
اما خبرگزاری مهر در ۲۹ دی ماه ۱۴۰۴ و زمانی که خبر از دستگیری وی در غرب تهران داد،‌ او را «دارای سوابق کیفری و امنیتی» معرفی کرده بود.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 253K · <a href="https://t.me/VahidOnline/75896" target="_blank">📅 16:53 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75894">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/ZP20OMo_FFs38l45_kOeZXymr2-gn8OCvM_Vx9KodXKdyrlwB4JA8sb2sNJsZWE2P-04FYS4KgGrVO7vT4FGxxcq7REah7sepPTXJQXEds7DTt6W8WJvHdXFZ0X0bPxqOS3DYwcsb7gwbDPhNvQIPFNKBscz3E-VZmyI7_CPoExtX4OJ535mBUoHaugcXhUgW6Qu5trB1did-szBH_nsgOTutMNSjX0oCid9DJNs8ClmI1y0_dac9ADth60Ks4kb5j7a9yQ6fv538L700-w8FlpjSHnsuM6TjX3DgXyUZ5DA-gFas7MqEv6_WGdwbZhnFbtM966aw5LarZgbO8sy6w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/ZP20OMo_FFs38l45_kOeZXymr2-gn8OCvM_Vx9KodXKdyrlwB4JA8sb2sNJsZWE2P-04FYS4KgGrVO7vT4FGxxcq7REah7sepPTXJQXEds7DTt6W8WJvHdXFZ0X0bPxqOS3DYwcsb7gwbDPhNvQIPFNKBscz3E-VZmyI7_CPoExtX4OJ535mBUoHaugcXhUgW6Qu5trB1did-szBH_nsgOTutMNSjX0oCid9DJNs8ClmI1y0_dac9ADth60Ks4kb5j7a9yQ6fv538L700-w8FlpjSHnsuM6TjX3DgXyUZ5DA-gFas7MqEv6_WGdwbZhnFbtM966aw5LarZgbO8sy6w.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">.</div>
<div class="tg-footer">👁️ 299K · <a href="https://t.me/VahidOnline/75894" target="_blank">📅 16:52 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75892">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/5e49979671.mp4?token=Ll7dVgdfArQyD6q29vJoWUFUUuURwV8tH-ZHYT_gh_Wc3caBn19KZKaFTg_l-OxgPvDScrG2gEnJvrForzxStSfxJT9tY6SjiCpOhFzIBu1Q4CPCtuuGo4A0FddRraFaALA8E_X_55v_eneg28fE85WCFXxlUdkTyo34qRuoau-hG87nMHaf43xl4Z8F5AeBbUa0LMRSQSCbbGkoaaGhCNZ_AS1PUdkGe-4wEjRYCIYmYRwBaP-gVHKIEpZMk825I7n_izc-RV34VdHSW4Tw9xDlKoqVk9yp9L5K6IsD4kAAsYUAK6qu-MMWgqg2Q-tk6wZbw2nlfJXl3Twnf_IQrg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/5e49979671.mp4?token=Ll7dVgdfArQyD6q29vJoWUFUUuURwV8tH-ZHYT_gh_Wc3caBn19KZKaFTg_l-OxgPvDScrG2gEnJvrForzxStSfxJT9tY6SjiCpOhFzIBu1Q4CPCtuuGo4A0FddRraFaALA8E_X_55v_eneg28fE85WCFXxlUdkTyo34qRuoau-hG87nMHaf43xl4Z8F5AeBbUa0LMRSQSCbbGkoaaGhCNZ_AS1PUdkGe-4wEjRYCIYmYRwBaP-gVHKIEpZMk825I7n_izc-RV34VdHSW4Tw9xDlKoqVk9yp9L5K6IsD4kAAsYUAK6qu-MMWgqg2Q-tk6wZbw2nlfJXl3Twnf_IQrg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">"انفجار خودرو در جایگاه سوخت‌گیری تهرانپارس"
خبرگزاری فارس و تسنیم با انتشار ویدیوهای بالا نوشتند:
سخنگوی سازمان آتش‌نشانی:
در ساعت ۶:۱۴ صبح امروز، وقوع یک مورد انفجار در جایگاه سوخت گاز واقع در بزرگراه یاسینی، مسیر غرب به شرق، بعد از سه‌راه تهرانپارس (نرسیده به پل ۱۲ فروردین) به سامانه ۱۲۵ اعلام شد. بلافاصله نیروهای دو ایستگاه آتش‌نشانی به محل حادثه اعزام شدند.
در بررسی‌های اولیه مشخص شد که یک دستگاه خودروی نیسان یخچال‌دار در حال سوخت‌گیری در این جایگاه بوده که به دلایل نامشخص و در حال بررسی، دچار انفجار شده است.
خوشبختانه این انفجار منجر به آتش‌سوزی نشده بود، اما شدت آن باعث وارد آمدن خسارات قابل‌توجهی به بدنه خودروی نیسان و بخش‌هایی از سقف و دیواره‌های جایگاه سوخت شده است.
در این حادثه دو نفر شامل راننده خودروی نیسان (حدوداً ۶۰ ساله) و یکی از متصدیان جایگاه (حدوداً ۴۰ ساله) دچار مصدومیت شدند.
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 388K · <a href="https://t.me/VahidOnline/75892" target="_blank">📅 08:31 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75891">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">پیام‌های دریافتی:
شرق تهران
تهران نو صدای انفجار شنیده شد
وحید جان ۵:۵۸ صدای تک انفجار شمال شرق تهران، سنگین بود. مثل بمب بود
سمت شرق تهران یه تک صدا اومد ۵:۵۷ وحید جان
ساعت 5:56 تهران شرق یه صدایی مثل انفجار شنیدم دقیق نمیدونم
سلام، ساعت ۵:۵۷
شرق تهرانیم و انگار صدای انفجار از جنوب غربی بود
تهرانپارس صدای انفجار اومد ساعت۶صبح
منم صدای انفجار ساعت ۶ شرق تهران بیدارم کرد ولی چون ادامه نداشت فکر کردم اشتباه کردم تا پیام بقیه رو دیدم
سلام، ساکن شرق تهرانم، تهرانپارس- با صدای انفجار ساعت حدود ۵:۵۶ بیدار شدم اول فکر کردم توهم زدم، الان که پیغام‌های شما رو خوندم گویا بقیه هم شنیدن.
الان حدود ۵ دقیقه ممتد صدای آژیر میاد حالا آمبولانس یا آتش نشانی نمیدونم.
سلام، پردیس چهارشنبه ۱۳ خرداد ۶ صبح صدای مثل بمب اومد
وحید جان من تو نارمک صدای انفجار شنیدم ولی نزدیک نبود  ۵:۵۸
شرق تهران یه صدای خیلی بلند اومد ۵:۵۷
سلام تهرانپارس فلکه اول ساعت ۶ یک صداى انفجار بلند اومد و از  ساعت ۶:۱۹  تا ۶:۲۲ صداى آژیر ماشین هاى امبولانس و اتش نشانى میاد
آپدیت:
دلیل احتمالی انفجار در پست بعدی
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 403K · <a href="https://t.me/VahidOnline/75891" target="_blank">📅 06:07 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75890">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OT-JsxBpYF8dIFYkcL6xwZB-ATTyneaa2h6aZoHaE92yckCGd6bwyx1nYJO5rsBua5LYGIkMpkC5DaEXmz1yVOmTqa-FZC-8ZV0jwItA3oxMKiKbg8nyBymYihkSGBUwcJ3pMA1Habc5X3VCTb8rwNI1yACd5C9DLjrsTao2D46tgThCeuuz_k8GGzGW5liR7zBt4RVZTdjoGD9_YJLZQdLO4zcUA4xyLjQJTwhCqEANy9d75A_qtfuMgNH9do0QsgwLCrH60LbnJt_71Vw-iAiDRobuIWZpRbHGJ6VnRpsADfVx5l46Tmd2klJ32ZHJA9gr7a1xgTYtcMAHV8ayuA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نیویورک‌پست می‌نویسد، بر اساس گزارشی جدید، یک خلبان جنگنده «اف-۱۵ئی استرایک ایگل» نیروی هوایی آمریکا در جریان جنگ ایران در کمتر از یک ماه دو بار در کویت (آتش خودی) و ایران سرنگون شد، اما هر دو بار زنده ماند.
هویت این خلبان هرگز به‌طور علنی اعلام نشده است. مقام‌های کنونی و سابق نظامی به نشریه «های ساید ساب‌استک» گفتند که او یکی از دشوارترین پنج هفته‌های دوران خدمت یک خلبان نیروی هوایی آمریکا را از زمان جنگ ویتنام پشت سر گذاشته است.
به نوشته نیویورک‌پست، بدبیاری او از دوم مارس آغاز شد؛ زمانی که در یک حادثه آتش خودی در کویت، نیروهای دفاعی این کشور به اشتباه به سوی سه فروند جنگنده اف-۱۵ئی آمریکایی شلیک کردند.
در این حادثه، هر شش خدمه این سه جنگنده مجبور شدند با استفاده از صندلی پران از هواپیما خارج شوند و با چتر در خاک کویت فرود آیند. همه آن‌ها سالم نجات پیدا کردند.
با وجود این حادثه، به گفته پیت هگست، وزیر جنگ آمریکا، خلبانان تنها چهار هفته بعد دوباره به ماموریت بازگشتند و در عملیات بمباران اهدافی در تهران شرکت کردند؛ اقدامی که او آن را نشانه شجاعت و فداکاری این نیروها دانست.
نیویورک‌پست می‌نویسد، اما چند روز پس از آن ماموریت، بدشانسی بار دیگر به سراغ یکی از این خلبانان آمد. یک جنگنده اف-۱۵ئی بر فراز ایران هدف قرار گرفت و دو سرنشین آن در خاک ایران سقوط کردند.
این خلبان در سوم آوریل به‌سرعت نجات داده شد، اما افسر سامانه‌های تسلیحاتی همراه او زخمی شده بود و پس از آنکه ایران برای دستگیری او جایزه تعیین کرد، ناچار شد مخفی شود. او روز بعد در عملیاتی نجات پیدا کرد.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 380K · <a href="https://t.me/VahidOnline/75890" target="_blank">📅 04:46 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75889">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/N5AgRgyRo2FLmohPzOzol4od-I7REpgENdEG5zO1Fq5DnkZGRXmvZQwQ-dPv4jeQNoZonvYcycBVxZhjE5vGq_z3EvC4MC5q5XiD4105zk5Fj_8vH6bLKkxtmrXixDJ3iijFuZqLuAcnGQ5ZtH7mYNl_SwyNV6SNrLXWn_0VqP4Hu7wKeqS90a76fNKuYis66dhzLU3T3YtNbF8vczDGr9E8sxYNumqTiWh4agqbOk7hXkHjR8oKINCUOP8MN4TfGiKRkLcfPCYbEMgp545nZyg37FmsOYwHKiRLqwRoK2U4gha6H7zR9mfjy9hhlZtkiConuqcaNxIpCVpDsHNBRw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ستاد فرماندهی مرکزی آمریکا در شبکه‌های اجتماعی اعلام کرد که سپاه پاسداران مدعی شده که در حملات امروز با موشک و پهپاد به مقر ناوگان پنجم آمریکا در بحرین و یک پایگاه هوایی آمریکا در منطقه ضربه زده است.
سنتکام گفت این ادعا نادرست است و تمام حملات جمهوری اسلامی به نیروهای آمریکایی شکست خورد.
@
VahidHeadline
آپدیت:‌
سنتکام توییت دیگری هم منتشر کرد:
ستاد فرماندهی مرکزی آمریکا (سنتکام) دقایقی پیش اعلام کرد که «موج دیگری» از حملات پهپادی جمهوری اسلامی که نیروهای آمریکایی در کویت را هدف گرفته بود، ناکام ماند و پهپادها به اهدافی که داشتند برخورد نکردند.
سنتکام افزود پدافند هوایی ستاد فرماندهی مرکزی ایالات متحده «با موفقیت چندین پهپاد را سرنگون کرد. سنتکام گفت هیچ یک از پرسنل و یا تجهیزات آمریکا آسیبی ندیده است.
@
VahidHeadline
(مثل دو روز گذشته در این ساعت، ده‌ها پیام دیگر از تهران دریافت کردم درباره صدای عجیب پرواز هواپیما که منجر به بیدار شدن خیلی‌ها شد.)
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 346K · <a href="https://t.me/VahidOnline/75889" target="_blank">📅 04:22 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75888">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ce2dAoSl8lQ5OOUZWw6EbOSpHcnUtCqAzmOstauES2GFJgnWt43kiH6DMCOXPMR5xKa6MjjKW2hOgxo1n6ZoHVbMH7JGQC8d1XU3Cgje40GptvBUrK8uvnyPDZ5E8oAhfQp1v23l4GBlZEqdiA0YdNLFV-gEelqutF_cnXNv__IxTPYo_3lqzyDRB-cP9n3jS__AeVSOMBeHtW-UzBNw38cvCCarRFsd-3LznitilMRHS0kJMnouBGiXIzlZYBZ8CSWbuhN840Yei4F5XlFUpFOTz_dSGdnloEnFFjFiKidclOAi7vYye3oJSEmwHXrSw0-3PNo7QQWiGllIFTdQBA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سنتکام از حمله به جزیره قشم پس از دفع حملات موشکی جمهوری اسلامی خبر داد
ترجمه ماشین:
نیروهای آمریکا و شرکایش در برابر رفتار تهاجمی ایران دفاع کردند
تامپا، فلوریدا — نیروهای آمریکا در تاریخ ۲ ژوئن با موفقیت چندین موشک بالستیک و پهپاد ایرانی را منهدم کردند و در پاسخ به تلاش‌های ایران برای حمله در سراسر خاورمیانه، حملات دفاع از خود را در جزیره قشم انجام دادند.
ایران چندین موشک بالستیک به سوی همسایگان منطقه‌ای شلیک کرد؛ با این حال، هیچ‌کدام به اهداف مورد نظر خود اصابت نکردند.
دو موشک ایرانی که به سوی کویت شلیک شده بودند، پیش از رسیدن به هدف سقوط کردند یا در مسیر متلاشی شدند و سه موشکی که به سوی بحرین شلیک شده بودند، بلافاصله توسط نیروهای پدافند هوایی آمریکا و بحرین رهگیری شدند.
لحظاتی پیش از آن، نیروهای فرماندهی مرکزی آمریکا، سنتکام، سه پهپاد تهاجمی یک‌طرفه را که ایران به سوی دریانوردان غیرنظامی در حال عبور قانونی از آب‌های منطقه‌ای شلیک کرده بود، سرنگون کردند.
نیروهای آمریکایی همچنین حملات دفاع از خود را علیه یک ایستگاه کنترل زمینی نظامی ایران در جزیره قشم انجام دادند.
هیچ‌یک از نیروهای آمریکایی آسیبی ندیدند. نیروهای سنتکام در جریان آتش‌بس جاری، همچنان هوشیار و آماده دفاع در برابر تجاوز بی‌دلیل ایران هستند.
CENTCOM
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 342K · <a href="https://t.me/VahidOnline/75888" target="_blank">📅 03:17 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75887">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/N1iO7QywIqlZIu_LKTPneevQ4KoHxSbxejT8TnxAv-qkheE5bSXzzt9bCsuQ8W7P-Lu_0Y1NiUmVagGJzc6W2k4NzjhPVWQHmiYzkGft9YvtOL_skwGO8CfXr-2z0hOJrXRzj8rWzMPhDGWHngARteMvSz7hyCt8GLlZEQv_GqbIssl7tMZJVHiWSIyYQY-06Yy2VedbSCF5zC6UPZzYB9tPkBe2fN-87J5kRiirWNUcEsy90UOjRAAirOM-gdqPwFN1xTsO8qwDjt4lbaI2ztbfz6e_diJTTZ--gnsQGECd_3uL5M2cGCEjiGDs_usd21qQW-AxHicv43iMn8yCBA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ساعتی پس از مخابره گزارش‌های متعدد از حملات موشکی به نقاطی در کویت و بحرین، سپاه پاسداران با انتشار اطلاعیه‌ای رسما از حمله به پایگاه ناوگان پنجم نیروی دریایی آمریکا خبر داد.
@
VahidHeadline
بیانیه سپاه به نقل از منابع جمهوری اسلامی
"بسم الله القاصم الجبارین
فَمَنِ اعْتَدَىٰ عَلَيْكُمْ فَاعْتَدُوا عَلَيْهِ بِمِثْلِ مَا اعْتَدَىٰ عَلَيْكُمْ
در اواخر شب گذشته ارتش متجاوز آمریکا یک نفتکش ایرانی را در حوالی تنگه هرمز مورد اصابت پرتابه هوایی قرار داد که این نفتکش از محل موتورخانه دچار خسارت گردید.
در پاسخ به این تجاوز و نقض مقررات تنگه هرمز شناور متعلق به دشمن آمریکایی صهیونی به نام پانایا مورد هدف موشک های نیروی دریایی سپاه قرار گرفت.
دشمن آمریکایی در تجاوزی مجدد یک دکل مخابراتی سپاه در جنوب جزیره قشم را هدف پرتابه های هوایی خود قرار داد در پاسخ به این تجاوز پایگاه هوایی و بالگردی آنان مستقر در یکی از کشورهای منطقه و همچنین مرکز ناوگان پنجم دریایی آمریکا مورد تهاجم موشکی و پهپادی نیروی هوافضای سپاه قرار گرفتند.
پیش از این اخطار داده بودیم که در صورت تجاوز پاسخ متفاوت و سنگین تر خواهد بود و همینطور اقدام کردیم. این پاسخ ها باید عبرت شده باشد.
تکرار می کنیم برهم زدن امنیت تنگه هرمز تاوان سختی برای ارتش متجاوز آمریکا خواهد داشت.
و ما النصر الا من عندالله العزیز الحکیم"
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 318K · <a href="https://t.me/VahidOnline/75887" target="_blank">📅 02:40 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75886">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/sQ-8tUToYlcJqIciEklzirCOCUg69sn_G9Grt6iul-vjVtU1-Qpbz9jtc7gZE2Q4Rrx4aOzLvZhA020kctmr38JBnds8rgGdNvs01bftd2HRugl0G1t1wNiORmqTX1ESUgUBuQyzzxENgzirK80EtHVFFtaX1pw6GXrnQzWRrohtksZ4krRWQ5tyxbS0LPfWSllsTvh0p8d_PG5XynMY5Zjv5o9WAXJIdFqVXwt-sggJPSrnnKFhBKFB2Ba8ZIj2hSnyn3aBDOskAF4PUboDRKwxKShD4vXMOf2qTurMyyQ2UYgTrBcLGp8i6_MKvTTzf7nTMwfZOG3SR1RG7DqMFA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پیام‌های دریافتی:
عکس بالا: بندر کنگان دو تا موشک شلیک شد سمت کشور های عربی 2.19
ساعت ۲:۲۰ از جم بوشهر موشک زدن
درود همین الان از جم دو عدد موشک شلیک شد به سمت خلیج فارس
از جم ساعت ۲:۲۱
دو تا موشک پرتاب شد
از جم بوشهر هم دو تا زدن
همين الان
شلیک موشک از شهرک موشکی شهید چمران جم هم اکنون
ساعت ۲:۲۳ دقیقه صبح دو موشک همزمان
آپدیت: پرتاب سوم
سومی هم پرتاب شد
یکی دیگه هم همین الان شلیک شد
۲:۲۴ از جم یکی دیگه پرتاب شد
🔄
آپدیت:
وزارت کشور بحرین دقایقی قبل از به صدا در آمدن «آژیر خطر» خبر داد و از ساکنان این کشور خواست به نزدیکترین مکان امن بروند. این هشدار پس از آن است که کویت نیز اعلام کرد مشغول مقابله با حملات هوایی است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 306K · <a href="https://t.me/VahidOnline/75886" target="_blank">📅 02:23 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75885">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/UDVWMW7T5_6mhnY7QH8gAhZ6lq1vUBmYTVgfOOevaJ6mMGwLtSCGNbsfw4ln03sbQCPwHvBE__qPgL86qjeYB2nTRmAGxKJTwlxoyhu96bu8D93MPunTA305dZbn1WovucekXWq36FKQqb9-JGuMwAjoiXJfsqa4PW6n0T9PEET61oT1A9zhMgmuL9_M16iiGe3SV6JotKecD_w5H_ketcqq52bgaGxZke-hY1nbP5p-HpVlWiSJrqTTKbWNnOgAF6xDevEoguWeKn3h_243il2PKHSlGPlVkmRawoenbD43kZipSsNcS0Ba87o9FLQwIuE0NVVSB-phCsHbyTRIrg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پیام‌های دریافتی:
۲:۰۷ همین چند ثانیه پیش صدای پرتاب موشک از توی خود شهر داراب شنیده شد.
الان دوباره صدای پرتاب موشک اومد
وحید سلام
یکی دیگه هم الان زدن از داراب
۲ دقیقه پیش
۲ تای قبلی هم یکیش تو هوا ترکید
آپدیت: عکس بالا
و پیامی دیگر از کویت: دوباره صدای آژیر
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 309K · <a href="https://t.me/VahidOnline/75885" target="_blank">📅 02:10 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75884">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/FByRQ4HwUNnM083vYF9HqyVIXau3KPyVJu47DjQATMbTSQBIS3hE4UhfDbE-asPJZP1CcFRmYhzzUl96jdXSs8PwgZtG2S7Rb_IGPtzd74HEbdnX_JGXgBuwnZcONp9q4mev9pxR2vLQpFrcbkcj64Xl00Dqf8y58Mb1agNF7qjL8g5fnzHvLkjWe-kliYNMr0BLdRRdBunzZQCIJYOa_yWMvWzT8tWvzHr2q0bDkfEfAV5_cMTzQpsUJBPX6QX1h_9-Z13r3zoo0bE78hc3ckRy9UJxvPRZf0zqgg4QToudrJos_xujPUE2LiP4rOmEbwmYleXrdWTYz95WSZB8Dg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">از داراب در استان فارس پیام‌هایی درباره شلیک موشک دریافت می‌کنم. هم‌زمان اسکرین‌شات‌هایی هم از کویت دریافت می‌کنم که میگن هشدار اعلام شده.
چهارشنبه ۱۳ خرداد
Vahid
ارتش کویت
اعلام کرد
سامانه‌های دفاعی این کشور در حال مقابله با حملات موشکی و پهپادی خصمانه هستند.
VahidOOnLine
ستاد کل نیروهای مسلح کویت با انتشار بیانیه‌ای فوری اعلام کرد که سیستم‌های پدافند هوایی این کشور، بامداد چهارشنبه، ۱۳ خردادماه، مشغول مقابله با حملات موشکی و پهپادهای متخاصم در آسمان کویت هستند. ارتش کویت در این اطلاعیه تاکید کرد که صدای انفجارهای شنیده‌شده در مناطق مختلف، ناشی از عملیات موفقیت‌آمیز سامانه‌های دفاع جوی در رهگیری و انهدام این «اهداف متخاصم» است. مقامات نظامی کویت از تمامی شهروندان و ساکنان این کشور خواسته‌اند تا آرامش خود را حفظ کرده و به طور کامل به دستورالعمل‌های امنیتی و ایمنی صادر شده از سوی مراجع مربوطه پایبند باشند.
@
VahidOOnLine
پیام‌های دریافتی که پیش از اخبار بالا نقل کرده بودم:
سلام همین الان ساعت ۱:۲۳ دقیقه دوتا موشک از داراب استان فارس پرتاب شد
یکیش حین رفتن ترکید
همین الان داراب صدای انفجار شدید اومد و شیشه ها لرزید
کل همسایه ها ریختن تو کوچه ببینن چه خبره
وحيد همين الان اژير كويت فعال شد دوباره
٦ تا انفجار خيلي سنگين تا الان
توي اين ٣ ماه اينقد صداش سنگين نبود
سلام آژیر در کویت
۵ انفجار بزرگ در کویت نسبت به روزهای قبل بیشتره
آپدیت:
ما بین فسا و داراب هستیم
یه صدای انفجار وحشتناک اومد ولی نفهمیدیم چیشده
من داراب هستم
ما عروسی بودیم تقریبا ساعت ۱.۴۰ دقیقه بود که یه صدای انفجار اومد و سقف سالن لرزید
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 342K · <a href="https://t.me/VahidOnline/75884" target="_blank">📅 01:26 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75883">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">پیام دریافتی تایید نشده:
صدای  انفجار روستای نخل گل قشم
سلام وحید جان
قشم صدای پایان جنگ در همه جبهه ها از جمله لبنان میاد
خبرگزاری مهر هم نوشته:
"بامداد چهارشنبه صدای انفجار‌هایی در محدوده شهرستان قشم از سوی منابع محلی و ساکنان این جزیره گزارش شده است."
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 313K · <a href="https://t.me/VahidOnline/75883" target="_blank">📅 01:26 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75882">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/f311feab7d.mp4?token=KsFvLDjmavZYlFt5iqceS5ERZRLo_BW2wl4H7hib4vovcEhVooIbe5bOmbjYuCcQE4B2YJBAcjHoCzlVUukdm9lIGxKsXyDTGkiGD_Daah4RjnpyvH3jgMM9CVm5djRtKEgB45p7-YPo4Ekd8uGLdkGFEzR1LzNPR7NNdT9HN47SkZhoBoSztPSIK2TD17JzGqTM90_FRIAqWSMXiZB5_YqVQQ7a6q2bD6ISL74L9d2awh9ZDtBLKXgFnNlnWEVIzMttfOtC1H811LAh7k_ICgNcSryJCbHErMhyEawYiJKU7zFrvJQRWKkPor4wmti8J4m7K3OTppYn_sG3FdK2mw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/f311feab7d.mp4?token=KsFvLDjmavZYlFt5iqceS5ERZRLo_BW2wl4H7hib4vovcEhVooIbe5bOmbjYuCcQE4B2YJBAcjHoCzlVUukdm9lIGxKsXyDTGkiGD_Daah4RjnpyvH3jgMM9CVm5djRtKEgB45p7-YPo4Ekd8uGLdkGFEzR1LzNPR7NNdT9HN47SkZhoBoSztPSIK2TD17JzGqTM90_FRIAqWSMXiZB5_YqVQQ7a6q2bD6ISL74L9d2awh9ZDtBLKXgFnNlnWEVIzMttfOtC1H811LAh7k_ICgNcSryJCbHErMhyEawYiJKU7zFrvJQRWKkPor4wmti8J4m7K3OTppYn_sG3FdK2mw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ارتش آمریکا به یک کشتی دیگر شلیک کرد.
بیانه سنتکام، ترجمه ماشین:
تامپا، فلوریدا — نیروهای آمریکا [امروز] ۲ ژوئن یک نفتکش بدون بار را که قصد داشت به سوی یکی از بنادر ایران در خلیج [فارس] حرکت کند، از کار انداختند.
فرماندهی مرکزی آمریکا، سنتکام، تدابیر محاصره را علیه نفتکش M/T Lexie با پرچم بوتسوانا اجرا کرد؛ این کشتی هنگام عبور از آب‌های بین‌المللی به سوی جزیره خارک در حرکت بود. خدمه کشتی هشدارهای مکرر را نادیده گرفتند و طی یک دوره ۲۴ ساعته چندین بار از اجرای دستورهای نیروهای آمریکایی سر باز زدند.
در نهایت، یک هواپیمای آمریکایی با شلیک یک موشک هل‌فایر به موتورخانه کشتی، آن را از کار انداخت و مانع رسیدن نفتکش به ایران شد.
سنتکام از ۱۳ آوریل اجرای محاصره همه رفت‌وآمدهای دریایی به بنادر ایران و خروج از آن‌ها را آغاز کرده است. با ادامه آتش‌بس با ایران، نیروهای آمریکا تاکنون شش کشتی تجاری را از کار انداخته و مسیر ۱۲۲ کشتی را تغییر داده‌اند.
CENTCOM
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 370K · <a href="https://t.me/VahidOnline/75882" target="_blank">📅 00:37 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75881">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/JOJE2zeqiuH-QpHDlIsCjvR1aa_0YyzSAUwaHHMys2E0Wk-Aqf97oSG0IvGjTITh58xYxS8E5HAjgw58aMhXM3Gk9RocKIAreKJNcHnHfJNsGPlCVJG8aDfOha9IA0T0cFMP1qERm4Zn09d_3CXe8zTzj6tl9FgXjHn3OmQPw0v4j5pq-lPcwI9xCYbFmQ2-9Qua3a4rTwP8_n4qTBhO7bBwz2fvUiwL7C2a9gjqhD_hl-d9jnZ5DQCKspZ21y8AHJoJG1Qxu-IKDrKU7yAGeE-KCQWlQ_gc6oulQrvRhvxnzV0fvgPr40XC4sf1SzYtfX48JuPeydZYh-sO6Hp7eA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ: گزارش‌ها درباره توقف مذاکرات درست نیست
ترجمه ماشین:
گزارش‌های رسانه‌های اخبار جعلی مبنی بر اینکه جمهوری اسلامی ایران و ایالات متحده آمریکا چند روز پیش گفت‌وگو را متوقف کرده‌اند، نادرست و خطاست.
گفت‌وگوهای میان ما به‌طور مداوم ادامه داشته است؛ از جمله چهار روز پیش، سه روز پیش، دو روز پیش، یک روز پیش، و امروز.
اینکه این گفت‌وگوها به کجا می‌رسند، هیچ‌کس نمی‌داند؛ اما همان‌طور که به ایران گفتم: «وقت آن رسیده است، به هر شکل ممکن، توافقی انجام دهید. شما ۴۷ سال است که مشغول این کار بوده‌اید و دیگر نمی‌توان اجازه داد این وضعیت ادامه پیدا کند!»
رئیس‌جمهور دونالد جی. ترامپ
realDonaldTrump
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 363K · <a href="https://t.me/VahidOnline/75881" target="_blank">📅 20:40 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75880">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/amRyqR15HhoLeMwCFHm7j7oRELCeDXVf7-rHQMj8kRY22-dTohDrOWj9m3Mj3x8VDNRcF4nxB-9dEeOqkw8aGPatlm9o2ou6dvgPrYg_lbZ74rk6NLG-rOp7Cszi3vLnDwx8EsaHjRl47oL-j5sOVx6_oVgFq_xyYv8HV2tnHEpJRmEq2INxx4p1PQT1QvXOdgjR2LUGDgO5maVWxjwX7UmTdZ9SjpWTZQFbmAoubOD7-zgwwqYBwYYm1d-x8ixXuAjEnY09WnVkNMW05dLimL3JkH8F2ky-BPL-YS9PPXA_Rr7ZrEtGNmG5XAZcVHdAGPAXZECf-WZdVOWElQUb3g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مارکو روبیو، وزیر خارجه آمریکا در جلسه کمیته روابط خارجی سنا گفت که نشانه‌هایی وجود دارد مجتبی خامنه‌ای رهبر جدید جمهوری اسلامی در سطحی به شکل فزاینده‌ای در حال مشارکت در روند مذاکرات است، «اگرچه تمام ارتباطات او به صورت مکتوب و از طریق واسطه‌ها بوده است.»
آقای روبیو افزود: با توجه به اتفاقاتی که برای رهبران متعدد در آن سیستم رخ داده است، تصور می‌کنم که حضور بسیار علنی احتمالاً چیزی نیست که در داخل برای آن‌ها توصیه شود.
او همچنین در پاسخ به سناتور دموکرات کریس مورفی، کاهش تحریم‌ها در ازای بازگشایی تنگه هرمز را رد کرد و گفت که هرگونه کاهش تحریم‌ها باید پس از امتیازات عمده در مسئله هسته‌ای و اورانیوم غنی‌شده صورت گیرد.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 353K · <a href="https://t.me/VahidOnline/75880" target="_blank">📅 19:41 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75878">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/pXejWV2Z5IVsr9Eu3QbpTznapJmwoWH5O5WC7H27XCEQ0g5EphMj5n6zyd-lDgbhy8dhS4umphBCk-qEIRZTfJYkogblyEfTeVLkNtnCfDraZupy71ghWiiw3JqTdoUkx045K8FRFPGS8pBI6SMVqAKuOuNwrBLkPOFpAdOBFmXka7YVJps9gicG1SzDwFgnh_NENHKPAnOJnQiD8WjVhPpDA0zdVCf2kSluFBwwzLs6b1FETg5XXuqFPYBnkcKWTgMvcWNjrrnS8cnbd-rRyC123Yx1mxyQhY2Jny4QWrbDOGyuppFByR3fuQrkrxDppPPe9lvdT3hY9BqbyIxUHg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/MR-RBl3rNbBfrG4YiQN-jE9vnYaSpkAVihQ2zXiNxT3CvzmnLa6J6qecIAwp9VHAFezPGLD8bis6x-kFxB4DB1rHa0Alecr2KaE00YAYha58UkI-UF_-NapckR83CktmJKjH9jp4x2W0YZqgPw7TTDWosp3nbaapGgy7pNgKRinnLeWGRFGP0oDhhucfUhYmSdwHoRmRrEX093PQ5PLoCSoB1kHZGxdPDnQeY94kLpetrnohK0LWtn2yIgsQV7RoBtoY5CgS5V_ax3NH1ZOUYCntk6OCnCUawGUtY5wRwliGL_BH3gFltzmXmrDsuvcmAuQ0Tap_qL4RrnWFlnEGQw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">مارکو روبیو در جلسه کمیته روابط خارجی سنا گفت: «چیزی به نام نیروی دریایی جمهوری اسلامی وجود ندارد. آنچه باقی مانده تعدادی قایق کوچک است که روی آن‌ها مسلسل نصب شده و نیروی دریایی واقعی در کف اقیانوس قرار دارد.»
او افزود: جمهوری اسلامی همچنان تعداد زیادی پهپاد در اختیار دارد. توان بازدارندگی متعارف تهران به‌طور قابل توجهی تضعیف شده است.
@
VahidOOnLine
وزیر امور خارجه ایالات متحده در جلسه استماع سنا تاکید کرد که شرط اول آمریکا برای مذاکره با جمهوری اسلامی، بازگشایی کامل و بدون قید و شرط تنگه هرمز است.
او در ادامه تاکید کرد که منظور از بازگشایی، بازگشت شرایط به پیش از جنگ و عبور و مرور آزاد تمام کشتی‌ها از این آبراه راهبردی، بدون محدودیت و مانند سایر آبراه‌های جهان است.
@
VahidOOnLine
او گفت باز کردن تنگه هرمز شرط اول آمریکاست اما صرف این کار باعث برداشته شدن تحریم‌ها نخواهد شد و رفع تحریم منوط به شرایطی خواهد بود.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 342K · <a href="https://t.me/VahidOnline/75878" target="_blank">📅 19:00 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75877">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ime8SnlF-1yvS58sKlOWqIFUKg3HTOEdmZ1t0M-GqJNx8gXV-6b_2iLxKojz175DBHdgBiUhoctOFfa_CjteuRKyQcdvj7QfA1xzANCN0ufLz1OLm6ub8jsin1gdn6PwDLtUAn1eEYTMAxOQ4VSSLYRnn8nstlRVr35iImwUnrJXzyxqK--WnAascsPe157XkehfwAbdtODgINHtmYaeLXFq3LsQq2Trkwp8FRRHdoq_OThZXH0FBGTNfT9CkPlkQiEFHXuyKUfmc4BUXSae6DwkRKkobX_-HsCobN8y1cbRN7YjTqHKPMYzW97aO-1yBIQE3HjoCQvbjsWvoBn66w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بنیامین نتانیاهو، نخست‌وزیر اسراییل، در مراسم تودیع دیوید بارنئا، رییس موساد، گفت جمهوری اسلامی تاکنون به دلیل توطئه‌هایش علیه اسراییل بهای سنگینی پرداخته و سرانجام این حکومت سقوط است.
بر اساس گزارش دفتر نخست‌وزیر اسراییل که روز سه‌شنبه ۱۲ خرداد ۱۴۰۵ در شبکه ایکس منتشر شد، نتانیاهو در این مراسم گفت: «هر کسی که بدخواهی علیه اسراییل در سر می‌پروراند، بداند که توطئه‌هایش شکست خواهد خورد و بهایی که خواهد پرداخت بسیار سنگین خواهد بود. بهایی که جمهوری اسلامی تا همین‌جا پرداخته است، بسیار سنگین است. پایه‌های رژیم وحشت در ایران ترک خورده و دیگر به آنچه بود باز نخواهد گشت. من به شما می‌گویم سرانجامش سقوط است.»
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 312K · <a href="https://t.me/VahidOnline/75877" target="_blank">📅 18:23 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75876">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/rdz8xT1X9TeJXSLNXD4uvL5mQGjtbbr8lKnmoAYHcelpWpbnLrs2twWU-XACkBiYEMDUigLufPUtcIr_yJBUCh9aM5xS-an7OuW0YvxThfTDSOU3bIgxxKGbHiIcorKCBWrJR-Wnql6aj47YWyDZMimGdmJYuXmXz5FYQSEzHM0uvHfP_-9Do5K6ETdH6-BgTVOblZ-q3-jqQRskqgNjaJVJDcx_9--N2CSd56--HqGl_5iPy5zFoqtCEJcwR7eY9bISib-j3uCYt9hoIBqlVwVEKnC4kwsxD-dkltmH8lnET3zKaosa0PFe1V4yqob7gDfuUlvS0nMKyk0OtL_rqw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مارکو روبیو، وزیر خارجه آمریکا در جلسه کمیته روابط خارجی سنا گفت که جمهوری اسلامی در حال دستیابی به سلاح هسته‌ای بود و اگر عملیات خشم حماسی صورت نمی‌گرفت دیر می‌شد.
آقای روبیو با یادآوری این که توانایی نظامی جمهوری اسلامی به شدت تضعیف شده، افزود که جمهوری اسلامی ایران برای اولین بار در تاریخ، بسیاری از شرایط مدنظر آمریکا برای رسیدن به توافق را پذیرفته است.
به گفته او شکاف در ساختار قدرت سیاسی جمهوری اسلامی و زمان طولانی رسیدن پیام‌ها مذاکرات را طولانی کرده است. اما طبعا اگر مذاکرات به هدف دلخواه آمریکا نرسد، ایالات متحده گزینه‌های دیگری را درپیش خواهد گرفت.
@
VahidHeadline
پیش‌تر ‌خبرگزاری فارس، وابسته به سپاه، به نقل از یک منبع آگاه نوشت که تبادل پیام بین جمهوری اسلامی و آمریکا برای آنچه دست‌یابی به یادداشت تفاهم اولیه بین تهران و واشینگتن خوانده می‌شود، دست‌کم چند روز است که متوقف شده است.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 278K · <a href="https://t.me/VahidOnline/75876" target="_blank">📅 18:20 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75871">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/gc34axOor23qTD80dbrXAK5E0lWg1V-0CQoBgc87MQwfHiCXKpwbDfVaRSXki-QSOLpwa-iWCvqawVcStj_AG3zvYzZx1xEfXR7dIrtzCtNFN_R3UmbqQvA8x1clqxcubJLFt0Sf8TwWDQ_sLICGx8JdcejYuLvqss3aAcjfzHVtmx3lmWhc69YGK6H7DEle_DRd8tq7NXtwnb6i7y6X5t0HgmQQGQvAfHdoyvxelbEm5wKDazLMfHkIVvY8f7atVWdXiAHHaqsr87TxDgTqVvTw8p0hLNPLRBU4lfAVKkWMw8FQu_kuuQPCf4NPKc7xRu8faLPv8r34eQumAtUOYg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/92446ed5db.mp4?token=SOWcL1OsofKEB6Q4RC3dE8yAEgg6oBVE7xpriCriO7vlRSF3hFIKY6xT-1yRMqIAXmJS51hiNxNsJ4EX39YRViOnHkT4PdHD2-Ye7cEoPB_rUtcJ6LdLu_bYuDgMMRxmf63_Ydkk7Yp3X6KiodBQbGab7CLfw0zqZUwrZVz3dlcxlGaFw3uagvpXSmdrBKwviCSliTt6PNHtv_vCF-iYwqJSozVJExqxtc6meXBgA9CBEaz3XXWpNq5oIm1xbW2czv9WuQqafBHkTlDmQGvZ7MyWBy6DenCqd9R-AnEOMze9CatLpJ3MaDz20KfSJ3UyOZmgeU1NFGmIFryLxfmByA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/92446ed5db.mp4?token=SOWcL1OsofKEB6Q4RC3dE8yAEgg6oBVE7xpriCriO7vlRSF3hFIKY6xT-1yRMqIAXmJS51hiNxNsJ4EX39YRViOnHkT4PdHD2-Ye7cEoPB_rUtcJ6LdLu_bYuDgMMRxmf63_Ydkk7Yp3X6KiodBQbGab7CLfw0zqZUwrZVz3dlcxlGaFw3uagvpXSmdrBKwviCSliTt6PNHtv_vCF-iYwqJSozVJExqxtc6meXBgA9CBEaz3XXWpNq5oIm1xbW2czv9WuQqafBHkTlDmQGvZ7MyWBy6DenCqd9R-AnEOMze9CatLpJ3MaDz20KfSJ3UyOZmgeU1NFGmIFryLxfmByA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">هما میرافشار، شاعر و ترانه‌سرای نامدار ایرانی، در ۸۹ سالگی در لس‌آنجلس درگذشت.
مرتضی برجسته اشراقی، با نام هنری مرتضی، سه‌شنبه ۱۲ خرداد، در اینستاگرام نوشت که خانم افشار هفته گذشته چشم از جهان فروبست، اما خانوادهٔ او با تأخیر این خبر را منتشر کردند.
این شاعر و ترانه‌سرا، که بر اساس گزارش‌ها، سال‌ها با بیماری آلزایمر دست‌و‌پنجه نرم می‌کرد، از پُرکارترین و محبوب‌ترین ترانه‌سرایان قبل و بعد از انقلاب ۱۳۵۷ بود.
هما افشار با بسیاری از خوانندگان برجسته ایرانی از جمله حمیرا، هایده، مهستی، ستار، ابی، داریوش، معین و عارف همکاری داشت.
او در سال ۱۳۱۵ در تهران متولد شد و در جوانی با علی میرافشار، پسرعموی حمیرا، ازدواج کرد. این پیوند، دوستی نزدیکی بین هما و حمیرا ایجاد کرد که به گفته خود او، جرقهٔ تولید بسیاری از ترانه‌ها و همکاری‌های این دو با هم شد.
@
VahidHeadline
هما میرافشار، روزنامه‌نگار، شاعر و ترانه‌سرای تصنیف‌های عاشقانه موسیقی دستگاهی و آثار به یادماندنی پاپ، در ۸۹ سالگی درگذشت؛ چهره‌های نامدار موسیقی و علاقه‌مندانش در شبکه‌های اجتماعی از مقام هنری او تجلیل کردند.
او در سه مجموعه شعری بیش از هزار سروده دارد که افزون بر ۲۵۰ شعرش در زمره ماندگارترین ترانه‌های ایرانی است و بی‌دلیل نیست که در جامعه موسیقی به «زن هزار ترانه» و یا «ملکه ترانه‌سرایی ایران» معروف شد. از همین روست که ایرج جنتی عطایی، ترانه‌سرای برجسته معاصر، هما میرافشار را پیشکسوت خود می‌‌داند که «پیش از ترانه نو و در کنار آن شهره بود.»
هما پیشگام سرودن اشعاری بود که یک زن برای معشوق می‌خواند و یا حرف‌های عاشقانه‌ یک مرد برای دلبرش، چرا که تصنیف‌سرایان آن دوران به جنسیت ترانه‌ها کمتر می‌پرداختند. او سال‌ها پیش در برنامه «یک‌ حرف و دو حرف» رادیو بی‌بی‌سی به زنده‌یاد محمود خوشنام، پژوهشگر موسیقی، در این باره گفت: «منیر طاها، سیمین بهبهانی یا لعبت والا که کار می‌کردند، من ندیدم که ترانه‌هایشان بوی زنانه بدهد مگر این که از زبان مرد بیرون آمده باشد. اگر خواننده آنها مرد بوده به ناچار باید چیزی را می‌نوشتند که یک مرد به یک زن بگوید.»
«یادم می‌آید که یکی از من پرسید که شما این حالت را چگونه می‌نویسید و من در پاسخ گفتم اگر بخواهم از زبان مرد شعر بگویم، مشتاق شنیدن همان‌هایی هستم که دوست دارم از او بشنوم. آن حرف‌ها را می‌گذاردم در کلام و اکبر گلپا می‌خواند، یا می‌دادم به محمودی خوانساری می‎‌خواند اما گاه طوری می‌نوشتم که مرد یا زن هر کدام بخوانند فرقی نکند.»
....
در ابتدای دهه پنجاه بود که اشعار هما میرافشار و ملودی‌های زیبای محمد حیدری در صدر جدول بهترین‌ ترانه‌ها قرار گرفت و نام هما درخشید؛ مثل ترانه «دیوونتم» با اجرای حمیرا: «بذار بگم دیوونه‏‌تم...آره دیوونه‏‌تم من...نشکن منو به سنگ غم... چراغ خونه‌تم من...» یا ترانه «دلم می‌خواد» با اجرای هایده: «دلم می‏‌خواد که روزی صدهزار بار... بهت بگم دوست دارم عزیزم...» و یا ترانه «میکده» با صدای اکبر گلپایگانی: «هوس میکده داره دل دیوونه‏‌ی من، نمی‌‏دونه بی‏‌تو ایام بهارو چه کنه...»
...
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 275K · <a href="https://t.me/VahidOnline/75871" target="_blank">📅 18:05 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75870">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/qjnMt6HU4SnWhy6CcXqvLXAwKcz9J8dxCfZk3WukfUgS1vrMp8y0hz-C6uuJf9R-luLln6R2osdZeNXZH2HSZuLKA9YbhEjwCPPLe81f-cw2qZqPEMyIZ-aRyxH67xmu2aUkjX4wamCbc1rNKgaEuC87PmvGWmiCYIhEctAFyaodxZVkabZPQINJqnpR6CW7X6rVCSIVjDB2fCLrKSVHQUs2nA6UBtfz9iapzcVo-65j4egwdr1scD9vQ6TuFDGfgwa2jBzISucFYJ1wccZentOMfzxwhzVsT99S43NJMI-fq_Xu5EAweZI7XUzEayds1TrpKEeG9spZVe6iSZog5A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">Gerduo
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 268K · <a href="https://t.me/VahidOnline/75870" target="_blank">📅 17:52 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75869">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qSvObuwcweD0ZHjLyVoaYs2Zq6MVfO6p0VINkaA6Pn3shxfETqeeH0LW0y5yfom0r6binyQAX-FNVwLYC1JeKaf6nxG6YEaXj3MCAm-7qzSbGOgffzOfveRJiBTzlyFW9DnbRfxWqHwNNlA-jgfJuV5onziUCAbyTWNbF9Ur9HYl6VhRoWMsiZwH9XwQgWyImUx5gwdD3RWhLBpuyIkkua1N7tXTq_3fbz3duwUqgGeb2WFAK66lfUS_A--SyIko-9pKrGGUsXMw8Wp49LTPXUxg4AJFk4XBh_R44vvH6N6GqYDuWHS4lw1eCrE-z5VgTkPa4JO-2B-Au-m2le-suQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یک مقام شهرداری تهران می‌گوید که برگزاری «مراسم بدرقه» و تشییع جنازهٔ علی خامنه‌ای، رهبر کشته‌شدهٔ جمهوری اسلامی، در شهرهای قم، مشهد و تهران «قطعی شده است».
به گزارش رسانه‌های ایران، محمدامین توکلی‌زاده معاون اجتماعی شهرداری تهران روز سه‌شنبه ۱۲ خرداد گفت که این نهاد «در حال تدارک برای حضور جمعیتی بیش از ۱۵ تا ۲۰ میلیون نفر در تهران هستیم».
او به زمان دقیق برگزاری این مراسم اشاره نکرد ولی گفت که احتمالا در پایان ذی‌الحجه و اوایل محرم برگزار شود.
این زمان تقریبا مصادف با اواخر خرداد و اوایل تیرماه است.
علی خامنه‌ای از ۹ اسفند پارسال که در حملات مشترک آمریکا و اسرائیل کشته شد، هنوز دفن نشده است.
معاون اجتماعی شهرداری تهران در ادامه گفت که «مراسم بدرقه» سه روز در نظر گرفته شده و در تهران قرار است ۲۴ ساعت طول بکشد.
به گفته توکلی‌زاده، محل دفن خامنه‌ای «طبق وصیت ایشان و توصیه‌های نزدیکان‌شان» در حرم امام هشتم شیعیان تعیین شده است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 282K · <a href="https://t.me/VahidOnline/75869" target="_blank">📅 17:50 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75868">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/i6o4eJYceVIIgwlK9cBXwwgjFO760BssBQTSTduUrAQn37HDJA6kytBAg8DhUTulZtI3oczsWsyiLqlQu2e9fhIN4tNCFQLTAPaTXIchw0Gi_Ood-VfNVUg8s8zQAo897EEdo9dnn2Cdz98gQmZaIclCDmZAPGf4RIhnb_WhYkWfiNw9FG0ihN63bnNY3QfCIsu2e1Z6pRj1xOd4AbY9atu_ypC-xuVg6tpjPryXEdJBx5eChId-FAn--B4fS6OIwtbFejEagH3PHFuR3VHXHKoIoChkFo7r__TEcSrHP_1LqE6ViesIkSY-0m-jeim2gT9OlHcuWXrTQqpZvevw9Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پس از چند روز تاخیر، بانک مرکزی و مرکز آمار ایران به‌طور همزمان گزارش‌های تورمی اردیبهشت‌ماه را منتشر کردند؛ گزارش‌هایی که با وجود تفاوت در ارقام، از تداوم روند صعودی قیمت‌ها و افزایش فشار معیشتی بر خانوارها حکایت دارد.
مرکز آمار ایران تورم ماهانه خانوارهای کشور را ۸.۸ درصد، تورم نقطه‌به‌نقطه را ۸۳.۹ درصد و تورم سالانه را ۵۷.۷ درصد اعلام کرد.
همزمان بانک مرکزی با تمرکز بر مناطق شهری، تورم ماهانه را ۸.۵ درصد، تورم نقطه‌ای را ۷۷.۲ درصد و تورم سالانه را ۵۳.۹ درصد برآورد کرد.
بر اساس گزارش بانک مرکزی، شاخص کالاها در اردیبهشت‌ماه نسبت به ماه قبل ۱۰ درصد و نسبت به مدت مشابه سال گذشته ۱۱۳.۸ درصد افزایش یافته است؛ آماری که از رشد شدید هزینه خرید اقلام روزمره حکایت دارد.
اختلاف ارقام منتشر شده از سوی دو نهاد آماری به تفاوت در جامعه آماری، سال پایه، شیوه نمونه‌گیری و وزن‌دهی کالاها و خدمات بازمی‌گردد. مرکز آمار کل خانوارهای شهری و روستایی را مبنا قرار می‌دهد، در حالی که بانک مرکزی تنها مناطق شهری را بررسی می‌کند.
مقایسه آمارها با ماه‌های گذشته نیز از شتاب گرفتن روند تورمی خبر می‌دهد. تورم نقطه‌به‌نقطه که در فروردین‌ماه ۷۳.۵ درصد اعلام شده بود، در اردیبهشت به ۸۳.۹ درصد رسید؛ افزایشی بیش از ۱۰ واحد درصدی تنها در یک ماه.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 256K · <a href="https://t.me/VahidOnline/75868" target="_blank">📅 17:45 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75867">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/695f2e3957.mp4?token=BXaFG8vV-5ok-e9fuOfQDDTb6sbrk1vviW6tv8odbz75TrlEbIawb21Zi5JY2OKlKQfe_ncz6UfA6_HEr4-byFP7qH5snJJ9mZ4bg24zPv-52M1SORjBs-AhyW-N2wQU8CiPR2BdpZ7Y40GLQhrmNYt6ijK9mOGj9qVv8VOFf_pN5w_DjpFd_nhbwzcYC6CDhbK71GqnbSMytY7hLZaB-sCzH6U71COlt4pOSX17cTg0HWPczJyDmbPcOMlmJM4-mHvoo3CjsmB8eOhoVzN6Z9HAV3tAPCItvwycD30r325nstJtxgqCd_bUfj16ExYDfjRHsYKz_6ksucTvlbzy2w" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/695f2e3957.mp4?token=BXaFG8vV-5ok-e9fuOfQDDTb6sbrk1vviW6tv8odbz75TrlEbIawb21Zi5JY2OKlKQfe_ncz6UfA6_HEr4-byFP7qH5snJJ9mZ4bg24zPv-52M1SORjBs-AhyW-N2wQU8CiPR2BdpZ7Y40GLQhrmNYt6ijK9mOGj9qVv8VOFf_pN5w_DjpFd_nhbwzcYC6CDhbK71GqnbSMytY7hLZaB-sCzH6U71COlt4pOSX17cTg0HWPczJyDmbPcOMlmJM4-mHvoo3CjsmB8eOhoVzN6Z9HAV3tAPCItvwycD30r325nstJtxgqCd_bUfj16ExYDfjRHsYKz_6ksucTvlbzy2w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">صدها دانش‌آموز روز سه‌شنبه ۱۲ خرداد با تجمع مقابل وزارت آموزش و پرورش در تهران، به تغییر قوانین کنکور، افزایش تأثیر معدل و پیامدهای جنگ بر آمادگی برای آزمون سراسری اعتراض کردند.
در ویدئوهای منتشرشده در شبکه‌های اجتماعی، شعارهایی از جمله «دانش‌آموز بیداره، از تبعیض بیزاره»، «دانش‌آموز می‌میرد، ذلت نمی‌پذیرد»، «وعده زیاد شنیدیم، عدالت و ندیدیم» و «فشار روانی کافیه، زندگی‌مونو پس بدین» شنیده می‌شود.
سیاست‌های مرتبط با کنکور از جمله افزایش تأثیر معدل و تغییر در شیوه برگزاری و زمان‌بندی آزمون‌ها، در کنار شرایط ناشی از جنگ، در ماه‌های اخیر با تغییرات و ابهام‌هایی همراه بوده که به گفته داوطلبان، موجب سردرگمی و دشواری در برنامه‌ریزی برای امتحانات نهایی و کنکور شده است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 329K · <a href="https://t.me/VahidOnline/75867" target="_blank">📅 17:44 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75866">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/kjfy3TF9cbe0u02PUOvPgWYqgpvREG95mGFPcKuEVYU2ZLj9yD9H28cIYcOWBSZ6TNuDlXe1Nw6VGClP8VhxIO5gaBgmqfJGuQP1v507t5IH98YRjKOnwlsMP5MpU6V8YaGA9FxYh0tgi7qIGY6LX9s5RGRSko7SHFCIkEDuoiQ39RWqxeXlplmWDmGjDH_EcjxJbyLBNNT2aixhHHakQ8CFCLrUhCpBdiz-2tcnV6FfSLcgO_OK8HNfueBeFldFCmOydkxDDtcZ2b1KFEWfME57KTHAmL0qs-eLBt2yfOVXw2Brm8wuzXAL6AWsrrHQSXQzFX9tWJhEQy_GSWs2wQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ برای سومین بار این متن رو علیه بعضی از رسانه‌ها پست کرد.
ترجمه ماشین:
اگر ایران تسلیم شود، اعتراف کند که نیروی دریایی‌اش از بین رفته و در کف دریا آرام گرفته، و نیروی هوایی‌اش دیگر در میان ما نیست؛ و اگر تمام ارتشش از تهران بیرون بیاید، سلاح‌ها را زمین بیندازد و دست‌ها را بالا ببرد، در حالی که هرکدام فریاد می‌زنند «تسلیمم، تسلیمم» و دیوانه‌وار پرچم سفیدِ نمادین را تکان می‌دهند؛ و اگر همه رهبران باقی‌مانده‌اش تمام «اسناد تسلیم» لازم را امضا کنند و شکست خود را در برابر قدرت و نیروی عظیم ایالات متحده باشکوه آمریکا بپذیرند، نیویورک تایمزِ رو به افول، چاینا استریت ژورنال — یعنی وال‌استریت ژورنال! — سی‌ان‌انِ فاسد و حالا بی‌اهمیت، و همه اعضای دیگر رسانه‌های اخبار جعلی، تیتر خواهند زد که ایران یک پیروزی استادانه و درخشان بر ایالات متحده آمریکا به دست آورد؛ اصلا هم رقابت نزدیکی نبود. دموکرات‌های احمق و رسانه‌ها کاملا راهشان را گم کرده‌اند. آن‌ها کاملا دیوانه شده‌اند!!!
رئیس‌جمهور دی‌جی‌تی
realDonaldTrump
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 401K · <a href="https://t.me/VahidOnline/75866" target="_blank">📅 05:13 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75865">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">باز هم صدای غیرمعمول پرواز یک هواپیما خیلی‌ها رو در تهران از خواب بیدار کرد.
پیام‌های دریافتی:
صدای هواپیما سعادت آباد
سلام، تهران صدای توافق میاد فکر کنم
صدای جنگنده یا هواپیما ۰۴:۰۹ غرب تهران
دوباره همین الان دقیقا ساعت ۴:۱۰ صدای شدید تر جنگنده غرب تهران
سلام تهران صدای جنگنده میاد چخبره؟؟!
مطمئن نیستم ولی غرب تهران فکر کنم صدای هواپیما یا جنگنده اومد
تهران سمت  سعادت اباد صدای جنگنده میاد
خیلی پایین بود صداش
همین الان تهران صدای کلی جنگنده اومد ک رد شدن
خیلی بلند بودن
صدای جنگنده غرب تهران
ساعت۴:۱۰صبح صدای جنگنده سمت شمال غرب میاد
تهران جنت اباد 4 09 صدا جنگنده اومد
4 و ده دقیقه صبح بالا سر شهرک نفت پونک جنگنده اومد آنتن قطع شد و وصل شد
همین الان غرب تهران حدود ۲ دقیقه صدای جنگنده اومد
دقیقن ده ثانیه پیش ساعت ۴:۱۰ ‌صبح یک‌هواپیمای از همونایی که موقع جنگ از بالا سر خونمون رد می شد
تهران حدود ساعت ۴ یه هواپیما مسافربری رد شد صداشم زیاد بود
هیچ وقت از این مسیر رد نمیشه!
توی فلایت رادارم نیست
شهرک‌ غرب ۴:۱۰
صدای جنگنده او‌مد
سلام وحید جان . ساعت حدودا ۴ و ۵ تا ۴ و ۱۰ دقیقه صبح شمال غرب تهران صدای مهیب جنگنده اومد. کاملا مشخص بود تو ارتفاع پایین داره پرواز میکنه . البته نه پدافند عمل کرد نه بعدش انفجاری شد. احتمالا برای نیرو هوایی ایران بوده
امروز سه شنبه دوازده خرداد ساعت ۴و۱۳دقیقه صبح صدای هواپیمای باری یا مسافری اومد چون چراغهای کابین و چشمک زن روشن بودن، مسیرش رو دنبال کردم مهرآباد ننشست تا جنوب تهران ادامه مسیر داد، صداش عین هواپیمایی بود که دیروز دوشنبه ساعت ۹و۱۵دقیقه صبح ، بسیار طولانی و ممتد حرکت می کرد به سمت  شمال ،چون از  کوه های البرز رد شد
صدای جنگنده نبود غرب تهران
یه هواپیمای خیلی بزرگ بود که اونقد پایین پرواز میکرد احساس کردم الانه که بخوره به ساختمون روبرویی خیلی بزرگ بود هواپیماش و خیلی پایین
پنجره باز بود دم پنجره خوابیده بودم صداش شبیه جنگنده نبود مابین جنگنده و پهپاد بود
همچین قیرقاژ داد رفتم رو هوا
سمت پونک
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 372K · <a href="https://t.me/VahidOnline/75865" target="_blank">📅 04:15 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75864">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">پیام‌های دریافتی درباره قطع شدن موقت خطوط تلفن همراه در بعضی از شهرهای استان‌های فارس، بوشهر و هرمزگان و...
از حدد ساعت ۲
▪️
شیراز کلا قطع شده انگار
نه میشه زنگ زد نه میشه کاری کرد
▪️
کل تلفن های همراه توی شیراز قطع شده
تمام اینترنت ها قطع شده
مشخص نیست چرا اینجوری شده
نه ایرانسل نه همراه اول نه رایتل آنتن نداره
▪️
وحید از حدود ساعت ۲:۱۰ تا همین الان انتن گوشی ها و اینترنت خانگی و هر چیز مخابراتی توی شیراز پرید
همین الان [۲:۳۰] همراه اول وصل شد با سرعت کم. ایرانسل وصل نیست
▪️
شیراز خط گوشی بیشتر از ۲۰ دقیقه رفت
از ساعتای ۲:۱۰ دقیقه تا ۲:۳۰
ایرانسل هنوز نیومده
آپدیت:
ایرانسل هم وصل شد
ولی همگی 3G  هستن
سلام وحید جان بندرخمیر هم از ساعت 2 همه چیز قطع شده الان به زور وصل شدم بهتون اطلاع بدم
اصفهان هم دقایقی خط همه رفت
تو شیراز یک دفعه همه انتن ها پرید. حتی نت مودم خونه مون هم کاملا قطع شد
الان بعد از حدود نیم ساعت دوباره انتن ها اومد
وحید فکر کردم فقط واسه من اینطوریه نت خونگی مبینت ما هم قطع شده خوزستان سربندر
از شهرستان های فارس نیم ساعت همه انتن ها رفت و اینترنت مخابرات هم کار نمیکرد الان اینترنت مخابرات اومد و انتن همراه اول هم با سرعت کم اومد ایرانسل قطعه
نت و انتن و... کامل توی بندر ماهشهر پریده
اهواز هم همینطور
سلام بندرگناوه چند دقیقه کلا همه چی قطع نه زنگ نه حتی شبکه داخلی همه چی بسته شد
بندر ساعت ۲ بامداد تقریبا آنتن ها رفت
و بعد برگشت خط 3g شده اما اینترنت کار نمیکنه
الان فقط اینترنت فیبر وصل شده
دقیقا راس ساعت ۲ کل دیتا سنتر شیراز قطع شد
تلفن همراه کاملا بدون آنتن
تقریبا ۳۰ دقیقه شد که وصل شد
همین الان حدود نیم ساعت در نورآباد ممسنی همه چی پریددد نت و آنتن و خط و همه چی
😐
شیراز از ساعت 2 تا 2:30 انتن همه اپراتور ها قطع شد
بندرعباس هم همینطور، قطع شد وحید جان تا الان
اینترنت و انتن های تلفن همراه تو قشم کلا قطع شد یهو
تقریبا ۱۰ دقیقه قطع شد
هم انتن هم اینترنت همراه
بوشهر اینترنت مخابرات و ایرانسل هی ده دقیقه ده دقیقه قطع میشه
خیلیاهم کلا قطع شدن از اشناهام
شیراز بعد از نیم ساعت وصل شد
کل سرویس های ایرانسل و همراه اول و شاتل حتی اینترنت مخابرات قطع بود
خط  ایرانسل هم برگشت
وحید سلام و خسته نباشی، اینترنت و خطا برای ده دقیقه کامل قطع شدن هم بوشهر هم بندرعباس، بوشهر وصل شده و نت همراه ضعیفه منتهی بندرعباس اینترنت ایرانسل قطع شده
وحید اصلا همه‌ی استان فارس همین شد
من فسا هستم منم قطع شدم
دقیقا از ۲:۰۲ تا ۲:۳۶ قطع شدم
وحید بوشهر هم کلا قطع شد الان وصل شده و خیلی ضعیفه یه نیم ساعتی کلا آنتن نبود
میناب هم یه ۲۰ ۲۵ دقیقه ای کلا انتن نبود
بندرعباس: ایرانسل کلا قطعه، همراه هم قطع و وصله
سلام اقا وحید داخل بندر دیلم استان بوشهر ما از ساعت ۱:۴۵ دقیقه هیچی انتن نداشتیم چه ایرانسل چه همراه الان درست شد تازه نت رو h هست
با تمام سیم‌کارت‌ها ما الان وصل شدیم
مرودشتم کامل قطع شده بود همه چی الان وصل شد
سلام وجید جان
ما برازجان هستیم
برای ما هم نت ایرانسل، همراه اول و رایتل و مخابرات کلا قطع شد
الان که برگشتن 3G هستن
سلام از جنوب استان فارس پیام میدم اینترنت خانگی و همراه و همچنین آنتن از ساعت ۲ تا حدود ۳۰ دقیقه کاملا قطع بود
بوانات برا یه نیم ساعتی انتن پرید
سلام توی یزد هم آنتن همراه اول کلا قطع شد، فکر کردم باگ گوشی خودمه، اما الان که گزارشات رو دیدم ظاهرا چیز دیگه ای بوده
درود وقت بخیر شیراز حدود ۲:۱۰ دقیقه کل خط ها انتن و اینترنتشون پرید و بعد از حدود نیم ساعت با سرعت بسیار کمی وصل شد
تشکر وحید جان
سلام وحید خط بستک و کل غرب استان هرمزگان بعد ۲۰ دقیقه وصل شد
سلام وحید جان بندرعباس الان 45 دقیقس که همه چی قطعه آنتن ایرانسل اومده ولی روشن نمیشه همه چی پریده فقط فیبر نوری وصله فعلا
سلام وحید جان :استان بوشهر :کنگان از ساعت ۲:۲۳نت ایرانسل و مخابرات پریده و هنوز وصل نشده خدا میدونه چیکار میکنن.
شهرستان
قیر و کارزین
هم ایرانسل هم همراه وصل شد اما مودم مخابرات از ساعت ۲ قطع
درود. از لاهیجان پیام میدم. اینجا هم امروز اینترنت مخابرات دو بار برای چند دقیقه رفت و بعدش با سرعت خیلی کمی وصل شد.
اصفهان هم حدود ساعت دو انتن قطع شد‌ ولی چند دقیقه بعد برگشت
سلام داخل اهواز کل آنتن ها قطع شد و سریعا به حالت قبل برگشت
مجدد همه چیز پرید توی بندر ماهشهر باز الان وصل شد
وسط بازی بودم پرید بیرون انتن رفت فکر کردم خودم اینجوری ام  از ساعت دو
الان وصل شدم دیدم بچه ها هم نیستن هیچ کدوم نوراباد ممسنی
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 395K · <a href="https://t.me/VahidOnline/75864" target="_blank">📅 02:34 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75863">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/AilBCU8dJJ1fFDyTovYwY2Jb4of9UM0P0O75P0R9PoFZfIumHdHgdFkJfcqw0ik97va3Vp4sOqvIE_hbUqKlr6wo-Xi9kRlk8n5wzZOKLdRR284feSFRbtsyL771u0v007AYmRkTWjipqngGnkTOYttWfANZy6cYnQUEjmIOLzhiXaolJNwCR_jqniiqc62_ecqtu30KVjsUz2sKs2kuPboa7VxO082Ux06M0K9OrDwDCSxypsCjMwQ3YIqal0p0qroj-2JsEBOuQ8CjZhW944sY7zRn12pxbsYdCfRr3W6zwk-NLTw2p5V87MISqSDa08ijRJxQYVoNi5L75jyxsw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دونالد ترامپ، رئیس‌جمهوری آمریکا، در گفتگوی تلفنی با شبکه خبری «ای‌بی‌سی نیوز» اعلام کرد که به نظر او، توافق با تهران برای تمدید آتش‌بس و بازگشایی تنگه هرمز «طی هفته آینده» حاصل خواهد شد.
ترامپ روز دوشنبه در گفتگو با جاناتان کارل، خبرنگار ارشد این شبکه در واشنگتن، با ابراز خوش‌بینی گفت: «اوضاع خوب به نظر می‌رسد.»
رئیس‌جمهوری آمریکا با اشاره به تنش‌های اخیر افزود: «امروز مشکل کوچکی پیش آمد، اما همان‌طور که احتمالا پیش‌تر متوجه شدید، من خیلی سریع آن را برطرف کردم.»
او توضیح داد که این مشکل ناشی از ناراحتی و عصبانیت مقام‌های ایران از حملات اسرائیل به لبنان بوده است؛ ترامپ در تشریح نحوه حل این بحران گفت: «من با حزب‌الله صحبت کردم و گفتم تیراندازی نکنید؛ با بنیامین نتانیاهو، نخست‌وزیر اسرائیل هم صحبت کردم و گفتم تیراندازی نکنید، و هر دو طرف شلیک به یکدیگر را متوقف کردند.»
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 357K · <a href="https://t.me/VahidOnline/75863" target="_blank">📅 01:37 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75862">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Dtp0xexbGcKzMTNrkru-RUuM_HkqctJGFb3clvSnmnDvAIuDAdwLOgnsD4ADCWiKEc_fy7v7PM_iipQewbQ6bZAE85ZZjtnGamSBd3B-SgycomA60G8zswqdM-Cy3DilT4pow0AzzT41_oQzjBdJXxhcMwKqa7K9BmvPdli9sSLQqjBmRK5Fzlo-gdtJfwpEPn0BalkKiDre2Wa5A63SeOJa_-vDFk7P3Fd2ifDLc5tJ3Kw0bxwmCc4GYexKyIBM0L0F6HCJwA0KHPMDeiljzVyXiff6LJ6pqKK8Is55zqwrqT63pUnJGI8uGMySLP4l-rn5w2NePYFIZ0T3fS88dQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پست ترامپ، ترجمه ماشین:
امروز با بی‌بی نتانیاهو گفت‌وگویی داشتم و از او خواستم وارد یک حمله بزرگ به بیروتِ لبنان نشود. او نیروهایش را برگرداند. ممنون بی‌بی!
همچنین با نمایندگان رهبران حزب‌الله گفت‌وگو کردم و آن‌ها پذیرفتند که تیراندازی به اسرائیل و سربازانش را متوقف کنند. به همین ترتیب، اسرائیل هم پذیرفت که تیراندازی به آن‌ها را متوقف کند.
ببینیم این وضعیت چقدر دوام می‌آورد — امیدوارم تا ابد ادامه داشته باشد!
رئیس‌جمهور دونالد ج. ترامپ
realDonaldTrump
خیلی شبیه به
پست چند ساعت پیش
ش به نظر می‌رسه. به نظر می‌رسه همون رو بازنویسی کرده ولی قبلی رو حذف نکرده.
نظر چت‌ جی‌پی‌تی:
در اصلِ پیام، تفاوت محتواییِ بنیادی ندارد:
هر دو می‌گویند ترامپ با نتانیاهو صحبت کرده، نیروهای اسرائیلی از رفتن به بیروت منصرف شده‌اند، و از طریق نمایندگان/واسطه‌ها با حزب‌الله هم درباره توقف درگیری صحبت شده است. گزارش‌های خبری هم نسخه اول را با همین مضمون منتشر کرده‌اند.
اما متن دوم از چند جهت مهم بازنویسی و تنظیم‌شده‌تر است:
۱. ترامپ نقش خودش را پررنگ‌تر کرده
در متن اول می‌گوید:
تماس بسیار سازنده‌ای با نتانیاهو داشتم و نیروها به بیروت نمی‌روند...
اما در متن دوم می‌گوید:
از نتانیاهو خواستم وارد یک یورش بزرگ به بیروت نشود. او نیروهایش را برگرداند. ممنون بی‌بی!
یعنی متن دوم بیشتر این برداشت را القا می‌کند که ترامپ شخصا جلوی حمله بزرگ به بیروت را گرفته و نتانیاهو به درخواست او عمل کرده است.
۲. عبارت «حمله/یورش بزرگ به بیروت» اضافه شده
در متن اول فقط می‌گوید:
نیروها به بیروت نمی‌روند.
در متن دوم می‌گوید:
وارد یک major raid of Beirut, Lebanon نشود.
این مهم است، چون متن دوم وضعیت را جدی‌تر و عملیاتی‌تر تصویر می‌کند: نه فقط «نرفتن نیروها»، بلکه جلوگیری از یک عملیات بزرگ در بیروت.
۳. تماس با حزب‌الله با احتیاط بیشتری بیان شده
متن اول می‌گوید:
I had a very good call with Hezbollah
یعنی ظاهرا «تماس خیلی خوبی با حزب‌الله داشتم».
اما متن دوم می‌گوید:
I also had a conversation with Representatives of the Leaders of Hezbollah
یعنی «با نمایندگان رهبران حزب‌الله صحبت کردم».
این تغییر احتمالا برای این است که مستقیم نگویند ترامپ با خود حزب‌الله «تماس خیلی خوب» داشته؛ متن دوم آن را رسمی‌تر و غیرمستقیم‌تر می‌کند.
۴. تعهد حزب‌الله محدودتر و دقیق‌تر بیان شده
در متن اول:
all shooting will stop — Israel will not attack them, and they will not attack Israel
یعنی «همه تیراندازی‌ها متوقف می‌شود؛ اسرائیل به آنها حمله نمی‌کند و آنها به اسرائیل حمله نمی‌کنند.»
در متن دوم:
they agreed to stop shooting at Israel, and its soldiers. Likewise, Israel agreed to stop shooting at them.
اینجا حزب‌الله مشخصا متعهد می‌شود به اسرائیل و سربازانش شلیک نکند و اسرائیل هم به آنها شلیک نکند.
تفاوت ظریف این است که متن اول از «attack» استفاده می‌کند که گسترده‌تر است؛ متن دوم بیشتر روی «shooting» تمرکز دارد که ممکن است محدودتر از «حمله» باشد.
۵. متن دوم تردید و شکنندگی توافق را اضافه می‌کند
متن اول قاطعانه تمام می‌شود. اما متن دوم اضافه می‌کند:
Let’s see how long that lasts — Hopefully it will be for ETERNITY!
یعنی: «ببینیم چقدر دوام می‌آورد؛ امیدوارم برای همیشه باشد.»
این جمله نشان می‌دهد ترامپ خودش هم دوام توافق را قطعی نمی‌داند و بیشتر حالت آرزویی/نمایشی به آن می‌دهد.
جمع‌بندی کوتاه
متن اول بیشتر شبیه اعلام رسمی یک توافق فوری است.
متن دوم بیشتر شبیه بازنویسی سیاسی‌تر و شخصی‌تر همان پیام است؛ در آن ترامپ نقش خودش را برجسته‌تر کرده، تماس با حزب‌الله را غیرمستقیم‌تر توصیف کرده، عبارت «یورش بزرگ به بیروت» را اضافه کرده، و در پایان هم درباره دوام توافق تردید نشان داده است.
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 348K · <a href="https://t.me/VahidOnline/75862" target="_blank">📅 01:23 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75861">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/WhfEpMaQPQF_8lM19rfQuJxjWY1dKQ6SLSjEwD2YZ7sWXYC1POi8thYrKiieyaA0T8D4pfH6_ekA5px_4MypvetaJUci3oCBb49jxdrLVEud9KYj7fyh753ogEUDGEi7DplwJS2g9LV7PTJ59_3fiNtvO4MbRSfQvvM9xD8ak3e097xOQq-7zawBuh50AM78yyD2LyKFJoVqCBv_fsnF5tOECC8OKfL-lWtiEvQzubNvlEMJc6jSZBrkYNebdLMXk2qFixJqHj2MSbRUGBg3cfNJeGpoMg87LNyRjD6djKvOljTvkIAUNkGdjOhsRL63s8gaaVN-JzbdEYwRdnfA0w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرگزاری جمهوری اسلامی، ایرنا، روز دوشنبه ۱۱ خرداد از کشته‌شدن دو سپاهی در قم خبر داد.
این خبرگزاری ادعا کرد که این دو بر اثر «انفجار پرتابه‌های باقی‌مانده از جنگ اخیر» کشته شده‌اند.
طبق این گزارش، سپاه این دو نفر را حسین رمضانیان فردویی و محمد اویسی معرفی و محل کشته شدن آن‌ها را منطقه فردو، در استان قم اعلام کرد.
با این آمار تعداد تلفات سپاه در دوره آتش‌بس جاری میان جمهوری اسلامی با آمریکا و اسرائیل، و در خارج از درگیری‌های اخیر، دستکم به ۱۶ نفر افزایش یافته است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 363K · <a href="https://t.me/VahidOnline/75861" target="_blank">📅 23:42 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75859">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/2d24e12abc.mp4?token=OyRWrpbKW264RVicMbIsctVdBHyBwvQrXXnoS8TgYri52AKrta1k27MlI6loavWnyctSpoWzMaMGk4-ZgF8ge4sLHm03qXlRpdT8q4hpiWvlE9CksFvDQIJtY86GVofHyYZS2rDNd4uXQYCZxaOQtNm4ZkUuJHA0b2QnTEDQbAEaVREJIKgreY6ilZJcdRGOG-2EHBmtn4Uyu0LU9Q0PJ_o1eeLJWBgK-QEzDT25sEDASkzJ-9jSuv0a5UrQ-Kj89iw1VZVTcwoi0EGU9_bSYRssLiTrqrsxW_dF549ROMQZGhukBKU9pbFZtTEMv2WuPj2dQzKpwgiOhGeMVj3meQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/2d24e12abc.mp4?token=OyRWrpbKW264RVicMbIsctVdBHyBwvQrXXnoS8TgYri52AKrta1k27MlI6loavWnyctSpoWzMaMGk4-ZgF8ge4sLHm03qXlRpdT8q4hpiWvlE9CksFvDQIJtY86GVofHyYZS2rDNd4uXQYCZxaOQtNm4ZkUuJHA0b2QnTEDQbAEaVREJIKgreY6ilZJcdRGOG-2EHBmtn4Uyu0LU9Q0PJ_o1eeLJWBgK-QEzDT25sEDASkzJ-9jSuv0a5UrQ-Kj89iw1VZVTcwoi0EGU9_bSYRssLiTrqrsxW_dF549ROMQZGhukBKU9pbFZtTEMv2WuPj2dQzKpwgiOhGeMVj3meQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">روابط عمومی سپاه اعلام کرد که در پی حمله ارتش آمریکا به کشتی ایرانی «لیان استار» در محدوده دریای عمان، نیروی دریایی سپاه طی یک عملیات مقابله به مثل، کشتی «ام‌اس‌سی. ساریسکا» با مالکیت «دشمن آمریکایی-اسرائیلی» را با موشک کروز مورد هدف قرار داد
IranIntlbrk
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 340K · <a href="https://t.me/VahidOnline/75859" target="_blank">📅 23:31 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75858">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/bBBV3Po9pCH2VSq50kfWmExPnby5T74mT1UjYQlW4KF8ul72KQ453GnEAk1gt0epHT-NzC1qBWafZfZC2dOtdE8UyIgHCGZtclHYBd5tiyF7wbLOpybiEMeCGp8yjCzipEdnphq24gj8eeWYtu-r6ve7P1fyJ1fwwMgG_vsxQhejEkUUYyxLhpb89zyZ6wi4pmRSOt-f3dAfL4p0HA-L1Y139ezE0OT80UsoX_MklYFFP22GCkBwTQPqJZNf0LT6OR_QfWqiRpAucqj7QzY6EZkBoHESfGPKv9eZAcVprRZxU1K9yUxEhHIkaWqcRO9OPhGnYozysmsq7tc_QWUVcg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اعلام دونالد ترامپ مبنی بر موافقت بنیامین نتانیاهو با توقف گسیل نظامیان به بیروت، در شامگاه دوشنبه ۱۱ خرداد ماه، با واکنش منفی چند چهره شاخص سیاسی در اسرائیل مواجه شد.
ایتامار بن‌گویر، وزیر امنیت ملی اسرائیل، با انتقاد از این تصمیم گفت: «زمان آن رسیده که به ترامپ نه بگوییم.»
همزمان نفتالی بنت، نخست‌وزیر پیشین اسرائیل، نیز در پیامی دولت این کشور را به ناتوانی در حفظ امنیت متهم کرد. او با اشاره به حوادث امنیتی در اورشلیم، بیت‌شمش، لبنان و غزه نوشت: «مکان‌ها متفاوت هستند، اما داستان یکی است؛ دولتی که کنترل بر حاکمیت اسرائیل را از دست داده است.»
بنت همچنین گفت: «هرج‌ومرج در همه‌جا دیده می‌شود و ما امنیت را به شهروندان اسرائیل بازخواهیم گرداند.»
یائیر لاپید، رهبر مخالفان دولت اسرائیل، نیز با انتقاد از نتانیاهو، تصمیم او را «اعلام تبدیل اسرائیل به یک دولت تحت‌الحمایه کامل» توصیف کرد.
@
VahidOOnLine
دفتر نخست‌وزیر اسرائیل در بیانیه‌ای به نقل از نتانیاهو اعلام کرد: «امشب با رئیس‌جمهوری ترامپ صحبت کردم و به او گفتم اگر حزب‌الله حمله به شهرها و شهروندان ما را متوقف نکند، اسرائیل اهداف تروریستی را در بیروت هدف قرار خواهد داد.»
نتانیاهو افزود: «موضع ما در این زمینه تغییری نکرده است.»
او همچنین تاکید کرد ارتش اسرائیل به عملیات خود در جنوب لبنان طبق برنامه ادامه خواهد داد.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 353K · <a href="https://t.me/VahidOnline/75858" target="_blank">📅 23:21 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75857">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/QRWZ0jrHidRTCfFTx8dA3NbK_MwXBIVvFg1ps_xvllcr2ZEBvBqghzzgO-ERk3LZ34P_oXMLSClx0-5D3F7RDX07lk1MmxYfBRtCogdDXySaVSMp7DjA2ZDaGQ1Bi55Tr2zdQIXoTGRbIuT9zXbw7ReHBbF4jaVqeY5fX3xwHjZJJyRfvW3v3k-QYYZsfiEt2Rb_L5AjmRjYaWvod1F92ZBGnWn55BQwV8tQT3ZW35WplEvS9DaNIm1TJPfB3Ulu6Cu79EQCj0fijp9JxWqjMBqbjdZj6vTKAHju18e_iF42Dj66I2EKoFRUicyQ09UwlLjjfy9CB5qHP7nNHCMZfw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قاآنی: ادامه حملات به لبنان و غزه، باب‌المندب را به تنگه هرمز تبدیل خواهد کرد
اسماعیل قاآنی، فرمانده نیروی قدس سپاه پاسداران، شامگاه دوشنبه ۱۱ خرداد ماه در پیامی که رسانه‌های دولتی ایران منتشر کرده‌اند، نوشت جنگ اسرائیل در لبنان و غزه «در سایه حمایت‌های وقیحانه آمریکا، عزم محور مقاومت را برای توسعه پشتیبانی‌ها از هر دو جبهه، اقدام برای فعال‌سازی سایر جبهه‌ها و همسان‌سازی وضعیت ترافیکی تنگه باب‌المندب با تنگه هرمز رقم خواهد زد.»
فرمانده نیروی قدس سپاه همچنین هشدار داد که ادامه عملیات اسرائیل در جنوب لبنان و غزه، این کشور را با واکنش‌های گسترده‌تری از سوی حزب‌الله و گروه‌های فلسطینی روبه‌رو خواهد کرد.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 335K · <a href="https://t.me/VahidOnline/75857" target="_blank">📅 23:21 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75856">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/OcL1tW6T1SWiDeR6TdW1u5kPIo6hm5FKu_ifEnhKXX3sion6VpZqkuNMc4jtcamswlueNWPXbdiFftP8cTxrX8KYKa5aVOon_-326dRYIbiesrHXNMLKNtSFmVBPp06HgptZyhYI5j5wnrTWZ8onyW3HImzkKG7vt_uJpZuLqTYzISkpXPZjLTvkPoQN-0bruhrdhRZkTdRHcTBjbpfg01Wam-C4tj2Z7UM-CVZ6xrSMZqT-Dl4a_PK_cu0EzJxc1mszINcfH_doK3EEGEbzVhQAcZCsRv6uDnts4qY8y9wc-tXd45GWbJRbHtxBdxeS9QyoYAOH96P7gaCJ07MAOw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ: مذاکرات با جمهوری اسلامی ایران با سرعتی بالا ادامه دارد.
از توجه شما به این موضوع سپاسگزارم!
رئیس‌جمهور دونالد جی. ترامپ
realDonaldTrump
این دفعه گفت "جمهوری اسلامی ایران"
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 348K · <a href="https://t.me/VahidOnline/75856" target="_blank">📅 21:15 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75855">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/kWAiiUUo6rs1_ye_e5KayWhHVH_rWR0HEYaUQNYPlZ81TBMFfcOLew4UNNgLAgR4fUCq8EEfkoWJqLhA1t9T9339va8wm5IDpezl7_nNKfN0K7OHT24VXxqTd4uhyHYcWgNpak9U1fJO6fL3TQbML35mTOlqULyaBzEwRzED7dxl8_9gxjVDOpCk5rVTX0SmsDs91l3NSR-x1L98cqrjR90Zf_ZMNae-FfOU69zTF1PKQ7NcL4lLvTncxJo1uD70qUFPI9cF2dOy2CuEvuhddozGFrUiL_4mH0rIOgpdptLmstZSTesArYd274EYYJjlErT7VVqLyKRk3NBB3YKFKw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ: اسرائیل و حزب‌الله پذیرفتند حمله‌ها متوقف شود
ترجمه ماشین:
من تماس بسیار سازنده‌ای با نخست‌وزیر اسرائیل، بی‌بی نتانیاهو، داشتم و هیچ نیرویی به بیروت اعزام نخواهد شد؛ و هر نیرویی هم که در مسیر بوده، همین حالا بازگردانده شده است.
همچنین، از طریق نمایندگان بلندپایه، تماس بسیار خوبی با حزب‌الله داشتم و آن‌ها پذیرفتند که همه تیراندازی‌ها متوقف شود — اینکه اسرائیل به آن‌ها حمله نکند و آن‌ها هم به اسرائیل حمله نکنند.
رئیس‌جمهور دونالد جی. ترامپ
realDonaldTrump
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 362K · <a href="https://t.me/VahidOnline/75855" target="_blank">📅 21:08 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75854">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/CuBBcLiM2wmUheUdTaHutot2g7PA2lkbAzZuMa2XvIuXkLA1HTDhFu99vH5dcr9Qpm3eVJKLhRIo3ZMW_qutvlhms7qZp6B-peb9A5pZawkrsETPud4n4hz1drmyt-OzP5KnPp6jI_CRKoA9OhyWcgSri2zBTBMCrGrP960p57YkUAN_ucQ1Zcz74ET18GlAyWHEIY9eGNXaMOwseuDybWwW0msB1OAq1F7mmVBhKTmLj7CsnHM9gKA0bDS5gFMbXtz3SrKc5BTurHxZay4E5hkRd5_9aOGnboRtIaFWMKHz56eiDriC_o-xPHKgQXhlDGBe682D39SiVNGfkYMFnQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ: محاصره را حفظ می‌کنیم
توییت‌های خبرنگار NBC، ترجمه ماشین:
تازه: رئیس‌جمهور ترامپ به من گفت که درباره گزارش‌ها مبنی بر تعلیق مذاکرات ایران با آمریکا، چیزی از ایران نشنیده است؛ اما اگر درست باشد، اشکالی ندارد:
«فکر می‌کنم اگر حقیقت را بخواهید، زیادی حرف زده‌ایم. به نظرم سکوت کردن خیلی خوب خواهد بود، و این می‌تواند برای مدتی طولانی باشد.»
او ادامه داد: «این به آن معنا نیست که قرار است برویم و همه‌جا آنجا بمب بریزیم. فقط سکوت می‌کنیم. محاصره را حفظ می‌کنیم. محاصره یک تکه فولاد است.»
آیا می‌تواند آن‌ها را آن‌قدر منتظر بگذارد تا کوتاه بیایند؟
«فکر می‌کنم تا هر وقت که بخواهند می‌توانم صبر کنم. آن‌ها دارند ثروت هنگفتی از دست می‌دهند...»
همچنین وقتی از نویسنده کتاب «هنر معامله» درباره گزارش‌های تعلیق مذاکرات پرسیدم به نظر می‌رسید با اکراه نوعی احترام برای مذاکره‌کنندگان ایرانی قائل است:
«این حرف مناسبی است، چون آن‌ها مذاکره‌کنندگان بهتری هستند تا جنگجو.»
GarrettHaake
الان هم:
ترامپ و نتانیاهو دارند تلفنی صحبت میکنند.
J74wabx
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 355K · <a href="https://t.me/VahidOnline/75854" target="_blank">📅 20:15 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75853">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/l4O1tCYokJo4LGi38PiMAkiypF0LFC3lnTcPJAQ6bl39UFU5Vns94gLa6T4CnqbJIhUMhs3LCxM6I6u-y5qmabaea_7h3C43Mu5S89T0I0Zyxd1fUc1Fvdd4PVzsd4c0NkDlby_bLamDrc5_M7dCU7lGZ7z2XFIpC3NVMxL1R8hQBF667LIBh-zJOn9ngNSUQhA8Rbl0qt3wXbUW0ZW8ni1kveyLksx4aa7zb7jY8hR-OtZsQLefMOmnRu2TO_RfFMAfZ1xWf3vJF3HRjZ2Cx89t4rNrVAf-uyLeY67-G3HqCeOmevkowxV-kYwnqt05ccBz4NdrDg_0DZr5lQQE2w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هم‌زمان با صدور هشدار تخلیه از سوی ارتش اسراییل برای ساکنان حومه جنوبی بیروت، فرمانده قرارگاه مرکزی خاتم‌الانبیا به ساکنان مناطق شمالی اسراییل هشدار داد که در صورت عملی شدن تهدیدهای اسراییل علیه لبنان، برای جلوگیری از آسیب، این مناطق را ترک کنند.
علی عبداللهی، فرمانده قرارگاه مرکزی خاتم‌الانبیا، اعلام کرد بنیامین نتانیاهو «در ادامه شرارت‌های خود در منطقه»، ضاحیه و بیروت را به بمباران تهدید کرده و برای ساکنان این مناطق هشدار تخلیه صادر کرده است.
او افزود: «با توجه به نقض مکرر آتش‌بس توسط اسراییل، در صورت عملی شدن این تهدید، به ساکنان بخش‌های شمالی و شهرک‌های نظامی در سرزمین‌های اشغالی هشدار می‌دهیم اگر نمی‌خواهند آسیب ببینند منطقه را ترک کنند.»
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 319K · <a href="https://t.me/VahidOnline/75853" target="_blank">📅 19:44 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75852">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/89a4fe09bd.mp4?token=ShP9U2F4kFhSWaO6ErdYEUETdqWCChIzvTt_cSyalX9bs2VQyk8hxP6YgZlIIYoP9vGeI6ifyhSIKwQ6h9cyqpw9kTRnpYKDvNa_tO-DYXJNTOCt-5aJ5Yw0dbWrD204g_HXa2_NRTHHqyi4nCfszRGQFgEyYWyxWOJTj-9h8dwY55C_rueVnt2Y0-g6JpmJTcQpjEUn0mcdHa4H1WWJHXZIWN_hZXjunrDL4ooD4RQxl6ovGBJ-Q1MOIAinYtYmVYjRQBbyQweaDnQHsfH5VlOOepOahZiRrLRRMHvyUm2Y97bT1Rvly6tX0pBfcCyJP6qvJKpOKAzN5MYT7M0KCw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/89a4fe09bd.mp4?token=ShP9U2F4kFhSWaO6ErdYEUETdqWCChIzvTt_cSyalX9bs2VQyk8hxP6YgZlIIYoP9vGeI6ifyhSIKwQ6h9cyqpw9kTRnpYKDvNa_tO-DYXJNTOCt-5aJ5Yw0dbWrD204g_HXa2_NRTHHqyi4nCfszRGQFgEyYWyxWOJTj-9h8dwY55C_rueVnt2Y0-g6JpmJTcQpjEUn0mcdHa4H1WWJHXZIWN_hZXjunrDL4ooD4RQxl6ovGBJ-Q1MOIAinYtYmVYjRQBbyQweaDnQHsfH5VlOOepOahZiRrLRRMHvyUm2Y97bT1Rvly6tX0pBfcCyJP6qvJKpOKAzN5MYT7M0KCw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">«حمید سلیمیان» در حال نواختن تنبک
#حمید_سلیمیان
، متأهل و پدر یک پسر چهارماهه شامگاه ۱۸ دی‌ماه ۱۴۰۴ در جریان اعتراضات در زرین‌شهر اصفهان با شلیک مستقیم گلوله جنگی جان خود را از دست داد.
حمید سلیمیان راننده یکی از شرکت‌های فولاد بود و به گفته نزدیکانش به موسیقی علاقه فراوانی داشت او  تنبک و سنتور می‌نواخت.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 313K · <a href="https://t.me/VahidOnline/75852" target="_blank">📅 19:10 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75843">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/TltVUAAIkSw1uYLADa_WyeE2yWfSBvpCQc56H5wTR7XdGhEy-5bX4AIl9XgIbezVko14k0LqwGYX75XJQRx-5gn6sK0zxvZEFki3iKDCXf_9c1fMsTLgSdS5MiKfT8zAS7JLbXlHRZlvhP2uYSeg7T-SOU0ozs5lxvKpBmRuOFOkj-N1MTo5vKmU2H9uaUmSPUbkeh50MOAAcRj0zvFpj2J3uo9rXqE68rOEesrOK5EQscrhBd1vgnWnkPEHnNhb9_r2ZQNQVwjmgNmhEMUqhfkfSzQNPIUPD_Nknmgz8J13gAFlgPGDxcRZI7Ye7ixC9zpuo2_wlerh_F_s5-H3Wg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/SgTGh08g7v571aNDzhwPMutod_HX9xacKKRGCdiKIieYoEUdBZxEBSeu6imzA_yq_TYuTnhQ_7ylSVKlILzwAchLc5VUSfn9N2xzaA8kTH2_kuX6oqisW_FWWRTqx7s4-J34Nb8KQPx0IaCQGO4ONeYAVlbzlL-m4dVLArajUAbomqeGCdyUpbbO1YDqIGZBX0M1kUhAurDgOWipw0OPVStIIBJMAQZxk4N0CRCLnKpepTB5Mc19_XDKKnqZuwZPzi_oMSEwqcuyr1CwjyEuplUkAQJ5Y_tntdDG49y4ui_IF12pWY0zrT5HlXEgYlWIdU39zff_viyKbBgsUmNzYA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/cOwKh8dM4M7S21L5XNjVUh73favWS5SFWwTwdvO8SjOJEKBmR7Q82TUkJmlVzUuquk5ZxOKn3cdcEfpKkdhxI_8UVgR-3-KKUklqHgYq8w02XjR0jPNRJq7qBaLdHRFErRMpHV_xZyvLjd4yb_FgOGAbzpIjlhn1muJf0bR3xLXJT5LBUGdd21owo-aApG2fzvOc1v1nbuynnOk24b8yL1hIHMSLmcH6HlvY7HY3RIhuJlPmhUFJBWyO5uiCdA14HA4JUh684xmKOyrE5jz0mMrLLpyfy2uLnXykU_PRNm7qHO1AeCox3LU0S7wIAZMICERNMcrQmeTlP9D3Ogf1Fw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/tUoi_gI-FCsWl43goxRB-wBrwrUardUMz6ZpcKE0sEzNjg8Faq7CnKCjBQwqBeZqTYYW3Kdck0vcMI5wumLtaN8_FfKmanA4cpp7ySnuMhnELM3y5Yn-wKV1EIzdmythnrsRZJ6U6W5ZwuNaI6q_rGbrCtWJ8mcSkM_RoxdTF47fuaPD1VTMMeDU2CNo0zlPrkXX34l4bHOhUUbJhi-pONWat9hPCav4e-jvN2uTx4zwIE6iJPVEON20nr1vD3g6XuEFdFNaumGyTRlfLKUP-71wBP_gdzFWNXYgIWkHTPlivEeopHh_VfkuJii_hhOvXBO8Hnyoo0QAH-ziDscKZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/ckupAXvPMq-wvlykv316PE5h5YJifVAYyK_hBPs4_dUZkeHH0cwGbbHQS6ICXBDExFHFYL_TC8mhua9nWUyCyK1wMsRZc8xQYd3q7UmHhGqrg3Msd37NtLGGxhRTOTHo9IJuwo1_a508yXMg7le14Ehd77DErCWfe0O2FVO93N4bohX0GpaFOAhdMsU9wmrrhMOOsXWKiSAMHIFCORd-ZhSfQn_88q4oEGythyooTVWRYRXt4vPFqhJYIcV4Yib2uIm4obkCkVHxyEfIsYl8jS49cAnwDDssgGsJW_fZBffSfeEQgS2Z-pCtYKRwS_dn0AHp8GjV5SRlYXPmc6YXKw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/PlSY3Vx8vNXRlUOGdwTePSW8V0igdrBcgJf1hqBM56KKb0rR1kAOpuGeTunYAYIIqI55cgSrg_r1lSlVQoppxueegKsfWJ0MA31eOE9GZVoOKwpMXbJpwGAvKr5m1QZGdUZx0mNG_WgzTooMIVEaO7vXw2-BGB_KYKIvWLcLwObY-fL1a2jrMfELZ242BPAa9gE2RE5jWA9f3jpwQkKSvJ0bZYs3I2FltA3dIzI5mtLbjOp71x4325vRyqEfmPBiNE58oQ6QcjsTOaMulA_zAk_sA5uDhEHDAiRubHSM1NM8d-HjLxHeGAFQRCrkcO8FlNT6vKk9-YfeHNZ7mJWw8Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/Cfrcjk34SUxhlG-gui-2d3lAdRwD5C0NHb9TMefQq_LiWc6w-egnHGsNdcBYDzCTFZtAZnskPKvX12NAtLNRePZRUToy4VDstcQmOyIJ52RGZbdAoZ-TCpZQk4D9c1-H9DmOogrvqnQOlsug_GcZmypWW45Y1CysGsSEc9E3_UGMT7gWBpFlbQtcddKwWkNE-aC8nQ1Sz8R87ScrHSdEW3Uz0nb98q0iEajOwnactzdeMfVaPHoVEuo4ofUSAUWi_oKTgyp236fGELxRyMG8_NbRyr3UGdh-SuYKgtEh30AImxtcCts2A-xnGPqrkMzAV3mGEN3cWSXjwkgTmVPJkA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/RrXAS63plC8UiAZoX4voavNr99MZv4eNWfSZ8HDQLw0KzMA_AIKIBHV_PROdTbYkAhjXnBiWO2-E_FwTYqhthUiYP0J5cI2VJV5iwAlBPUx_2oT7niYvyTM5qgXaYUQ-mwSwnmONJBwP0B3Z3hZH3u-CgBbCQa2YA7R4i4L6JHzi95ci34qndhBrVRnWFALHum6GbWhIj84xAV5Ud6poBA-lJpE-Ogdb65kyZExcbaos6fSqiJhs54rHuWxbfAzx5VTl3YWQhTHpU3g1TIjNgiMCr1K5a74Fj0zrZ-DkkaykXLgFHrS1b-f6H_F6M5VXKhG0L00OkcNv7hKmnJt_Sw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/be1yO8c-VtxQw4y4e7xiUClGdlAiVVCQPRH5d5S2bfr6uEMMOHnLSehgUMDTVDikyduhxnltVQqDE1HwnLXpZflYbMLjAQykIuNKSW2aPhdBTvDkUmJ2ETN1wufbp7B2mwFtwdFBJJp2oYS4OKlTslTuRGVLOHnxchcMgcGCHvsiA-aC6ORglPQgJo2g1cMQJlxuj1Gs7hG7uixxJFSeccqp10GfV3-yQU0-p-J1x5BxUrZVP59CXRx3AVIdqeRssF7a4aphbNt8x2KvCOaSeoCZ22y70T8omuHtt_rB3Au83frWTx4o4T9e3uPlxD15dgI23umijUKKGHsiPV6Gaw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">هم‌زمان با تشدید حملات نظامی اسراییل به لبنان، مقام‌های جمهوری اسلامی بار دیگر تاکید کردند که هرگونه آتش‌بس میان ایران و آمریکا باید شامل همه جبهه‌های درگیری، به‌ویژه لبنان، باشد و هشدار دادند ادامه حملات به این کشور می‌تواند پیامدهایی در پی داشته باشد.
بنیامین نتانیاهو، نخست‌وزیر اسراییل، روز دوشنبه ۱۱ خرداد ۱۴۰۵، اعلام کرد که به ارتش این کشور دستور داده است اهداف متعلق به حزب‌الله در ضاحیه، حومه جنوبی بیروت، را هدف قرار دهد. او در یک پیام ویدیویی گفت: «هیچ وضعیتی وجود نخواهد داشت که حزب‌الله شهرها و شهروندان ما را هدف قرار دهد اما مقرهای تروریستی آن در ضاحیه بیروت از حمله مصون بماند.»
دفتر نخست‌وزیر اسراییل در بیانیه‌ای اعلام کرد نتانیاهو و یسراییل کاتس، وزیر دفاع این کشور، در پی آنچه «نقض مکرر آتش‌بس از سوی حزب‌الله» و «حملات علیه شهرها و شهروندان اسراییل» خوانده شده، به ارتش دستور حمله به «اهداف تروریستی» در حومه جنوبی بیروت را داده‌اند.
نتانیاهو همچنین گفت عملیات زمینی ارتش اسراییل در لبنان در حال گسترش است. اسراییل در جنوب لبنان منطقه‌ای امنیتی ایجاد کرده و می‌گوید هدف از آن جلوگیری از حملات حزب‌الله به مناطق شمالی این کشور است.
در واکنش به این تحولات، عباس عراقچی، وزیر امور خارجه جمهوری اسلامی، در شبکه ایکس نوشت: «آتش‌بس میان ایران و آمریکا، بدون هیچ ابهامی، آتش‌بسی در تمام جبهه‌ها، از جمله لبنان، است.» او افزود نقض آتش‌بس در هر جبهه‌ای «به معنای نقض آتش‌بس در تمامی جبهه‌ها» خواهد بود.
عراقچی همچنین آمریکا و اسراییل را مسوول پیامدهای هرگونه نقض این آتش‌بس دانست. جمهوری اسلامی پیش از این نیز بارها اعلام کرده بود که آتش‌بس میان ایران و آمریکا باید سایر جبهه‌های درگیری، به‌ویژه لبنان، را نیز در بر بگیرد.
ابوالفضل شکارچی، سخنگوی نیروهای مسلح جمهوری اسلامی، نیز به اسراییل هشدار داد که «تداوم جنایات در لبنان برای نیروهای مسلح ایران قابل تحمل نخواهد بود.»
هم‌زمان، محمدباقر قالیباف، رییس مجلس شورای اسلامی و رییس هیات مذاکره‌کننده ایران با آمریکا، با اشاره به آنچه «محاصره دریایی و تشدید جنایات جنگی در لبنان» خواند، این اقدامات را «شواهد آشکار عدم پایبندی آمریکا به آتش‌بس» توصیف کرد.
قالیباف در پیامی به زبان انگلیسی در شبکه ایکس، بدون اشاره به جزییات بیشتر، نوشت: «هر انتخابی بهایی دارد و زمان پرداخت آن فرا می‌رسد. همه‌چیز در نهایت سر جای خود قرار خواهد گرفت.»
این اظهارات در حالی مطرح می‌شود که عملیات نظامی اسراییل علیه حزب‌الله، از گروه‌های مورد حمایت جمهوری اسلامی در منطقه، شدت گرفته است. با وجود تاکید مکرر تهران بر ضرورت گنجاندن لبنان در هر توافق آتش‌بس میان ایران و آمریکا، این مطالبه تاکنون محقق نشده است.
اسماعیل بقایی، سخنگوی وزارت امور خارجه جمهوری اسلامی، نیز روز دوشنبه در نشست خبری هفتگی خود گفت: «ما تاکید کردیم و کماکان تاکید داریم بر این نکته که آتش‌بس در لبنان بخش لاینفک هرگونه آتش‌بس و هرگونه توافق نهایی برای خاتمه جنگ است.»
او همچنین حملات اسراییل به لبنان را از عوامل ایجاد تاخیر در روند دیپلماتیک برای پایان دادن به جنگ میان ایران و آمریکا دانست و بار دیگر بر ضرورت برقراری آتش‌بس در لبنان به عنوان بخشی جدایی‌ناپذیر از هر توافق نهایی تاکید کرد.
@
VahidHeadline
تازه‌تر:
خبرگزاری تسنیم، وابسته به سپاه پاسداران، گزارش داد که جمهوری اسلامی در واکنش به ادامه حملات اسراییل به لبنان و آنچه «نقض آتش‌بس در همه جبهه‌ها» خوانده شده، روند گفت‌وگوها و تبادل پیام با آمریکا از طریق میانجی‌ها را متوقف خواهد کرد.
تسنیم همچنین مدعی شده است که ایران و گروه‌های هم‌پیمان آن در «جبهه مقاومت» در حال بررسی اقداماتی از جمله انسداد تنگه هرمز و فعال‌سازی سایر جبهه‌ها از جمله تنگه باب‌المندب هستند. این گزارش می‌گوید این اقدامات با هدف واکنش به حملات اسراییل و حامیان آن در دستور کار قرار گرفته است.
@
VahidHeadline
ارتش اسرائیل در بیانیه‌ای به ساکنان منطقه ضاحیه در جنوب بیروت هشدار داد و از آن‌ها خواست برای حفظ جان خود این منطقه را تخلیه کنند.
در این بیانیه آمده است اگر حزب‌الله به شلیک راکت به سوی شهرها و شهرک‌های اسرائیل ادامه دهد، ارتش اسرائیل اهدافی را در ضاحیه جنوبی هدف قرار خواهد داد.
در ادامه تاکید شده است دولت اسرائیل با مردم لبنان در حال جنگ نیست، بلکه با سازمان تروریستی حزب‌الله می‌جنگد.
@
VahidOOnLine
در پی اعلام خبرگزاری تسنیم مبنی بر توقف «گفتگوها و تبادل متون از طریق میانجی» میان تهران و واشنگتن، بهای جهانی نفت بیش از ۵ درصد افزایش یافت و به بالاترین سطح خود در هفته‌های اخیر رسید.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 316K · <a href="https://t.me/VahidOnline/75843" target="_blank">📅 19:08 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75842">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BBp8t4E1031vzIIy8KMYIT7vl-X-MaIO-b_2iYbh97KHghP-TA0Q_rzLILlnA9NalFjQYp_l2jU4bGrWmOqvrEqnrs-vXfn0pRoFbzoy4p_-3286vHefp54ErkPuL2JTxU4Um1lNHaMIzdcSO-3wYqop2x1Z8VBzjnxM5wTFoe--pS7iCI-WDHTNV_tsYeMqof11o3KW749xVglsIz7TwUOy5qbGjrzPssTfS8hE8Rqeja6WWlOLRYjICYmqKg09A5DuVpOlDpxaU8AjXwthWgBb-ImIYW9JBw-DjuMkce_jvo659tv6ckINPtaQIfF2-mE5I2aRPj6GOUPne7wNPg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رسانه‌های ایران از کشته شدن یک دانشجوی زن در دانشکده دندانپزشکی قزوین به ضرب گلوله خبر داده‌اند.
میزان، خبرگزاری قوه قضائیه، از قول دادستان قزوین نوشت: «بررسی‌های اولیه نشان می‌دهد این دو دانشجو که در آستانه فارغ‌التحصیلی قرار داشتند، در مرحله متارکه از یک رابطه عاطفی بوده و پیش از این نیز اختلافات خانوادگی شدیدی با یکدیگر داشتند. صبح امروز، مرد جوان با یک قبضه سلاح کلت جنگی وارد محوطه درمانگاه شده و چهار گلوله به ناحیه سینه دانشجوی دختر شلیک کرده است. شدت جراحات وارده به‌حدی بوده که متأسفانه وی در همان محل جان خود را از دست می‌دهد.
در اطلاعیه دانشگاه علوم پزشکی قزوین در این باره آمده است: «انگیزه این واقعه، مسایل شخصی و خانوادگی بوده و ارتباطی با فرآیندهای اداری یا محیط آموزشی دانشکده ندارد.»
به گفته حمیدرضا قافله باشی، رئیس دانشگاه علوم پزشکی قزوین، «این تیراندازی به دلیل خصومت‌ خانوادگی اتفاق افتاده و دو دانشجو که زن و شوهر بودند در اثر شلیک جان خود را از دست داده‌اند.»
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 358K · <a href="https://t.me/VahidOnline/75842" target="_blank">📅 19:05 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75841">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">پیام‌های دریافتی از تهران درباره صدای پرواز یک جنگنده یا هواپیمایی دیگر مربوط به جمهوری اسلامی:
سلام تهران صدای جنگنده اومد همین الان
غرب تهران وحشتناک صدا جنگنده میاد ۹:۱۵
صدای جنگنده داره میاد غرب تهرانم ساعت ۹.۱۴
سلام وحید همین الان تهران صدای جنگنده میومد نزدیک ۲ دقیقه
شمال شرق تهران صدای جنگنده
سلام تهران صدا جنگنده شدید
الان از بالا سر ما صدای جنگنده اومد
رد شد رفت
همین الان منطقه گیشا صدای جنگنده میاد
همین الان ساعت ۹:۱۵ دقیقه صدای جنگنده سمت غرب تهران اومد(فکر میکنم جنگنده ارتش بوده باشه)
سلام وحید از سمت لویزان تهران موشک بلند شد
وحید الان ساعت ۹:۱۵ صدا جت منطقه ۲ تهران
تهران-فرمانيه
ساعت 9;16 صداي جنگنده مياد
وحید تهران ساعت ۹:۱۷ صدا جت میاد زیاد
هروی
الو سلام تهران سمت شهرک غرب صدای نمیدونم هواپیما بود جنگنده بود چی بود خیلی نزدیک بود
الان ساعت ۹:۱۷ دقیقه در قیطریه صدای جنگنده اومد
شرق تهران صدای جنگنده شنیده شد الان
سلام تهران صدا جنگنده شدید
احتمالا جنگنده های خودشونه
ساعت۹:۱۷
سلام دوشنبه تهران ساعت ۹:۱۵ صدا جنگنده من شنیدم سمت هروی
صدای جنگنده تهران ۹:۱۷
صدای جنگنده منطقه ۳
خیلی پایین بود
تهران صدای جنگنده اومد
سلام ساعت ۹:۱۵ سمت دروس تهران صدای جنگنده اومد
صدای جنگنده شمال تهران ساعت ۹:۱۵ رقیقه
سلام ساعت ۰۹۱۵ دوشنبه صدای پرواز چند جنگنده شمال تهران
منطقه ۳ صدای جنگنده انقدر زیاد و وحشتناک بود که از خواب بیدار شدم
سلام  پاسدارانیم صدای جنگنده اومد چند دقیقه پیش
صدای جنگده نارمک
سلام وحید. صدایی که ۹:۱۵ اومد شبیه جنگنده بود ولی از پنجره نگاه کردم شبیه هواپیمای مسافربری بود فقط نمیدونم چرا از ارتفاع کم حرکت میکرد
سلام آقا وحید من خونم گیشاسصدای جنگنده نبود هواپیما بود من بالای خونه رفتم دیدم ولی هواپیما بزرگ بود ی مقدار دیگه باری بود یا سواری نمیدونم ولی از بالای گیشا رد شد
من از روستای اطراف شهریارهستم یه هواپیمای مسافربری بزرگ تو ارتفاع پایین از بالا سرمون رد شد به وضوح دیدمش صداش زیاد بود
سلام وقت بخیر نیاورانم صدای جنگنده اومد وحشتناک بود
وحید من شهرک محلاتیم
بین ۹:۱۵ تا ۹:۲۰ صدای جنگنده میومد
(با ارتفاع پایین)
سلام وحید جان صدای وحشتناک جنگنده ۳ ۴ دقیقه پیش خونرو لرزوند
-هواپیمای کارگو سپاه از تهران بلند شد
.
-صدای جنگنده برای این بود؟
-ممکنه برای اسکورتش بوده باشه
J74wabx
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 427K · <a href="https://t.me/VahidOnline/75841" target="_blank">📅 09:18 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75840">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">پیام‌های دریافتی از
#بندرعباس
درباره شنیده شدن صدای سه انفجار:
بندرعباس ساعت ۹:۰۷ سه تا انفجار
الان بندرعباس ساعت 9:7 دقیقه 3انفجار قوی
یک صداهایی شبیه برخورد جسم سنگین (بمب یا هرچی) به زمین داره میاد از دوردست.
بندرعباس ساعت ۹:۰۹ صبح دوشنبه
سه تا صدای  انفجار اومد بندرعباس
ساعت ۹ و هشت دقیقه
دوشنبه، ۱۱ خرداد ۹:۰۷ صبح. بندرعباس.
صدای ۳ تا انفجار از نزدیکی پایگاه هوایی شنیده شد.
آپدیت:
خبرگزاری تسنیم وابسته به سپاه مدعی شده که مربوط به مهمات خنثی نشده بوده. البته دو روز پیش‌تر از این هم اعلام کرده بودند که طی ۷۲ ساعت آینده قراره از این صداها شنیده بشه در بندرعباس.
پیام‌های دریافتی از
#اصفهان
درباره شنیده شدن دو صدای انفجار از دور:
پیام ساعت ۹:۱۷: اصفهان صدای انفجار میاد، دو بار پشت سر هم
اصفهان همین الان صدای انفجار اومد سمت ناحیه ۶
الان اصفهان یه صدایی مثل صدای انفجار اومد
سلام وحید، اصفهان ساعت ۹:۱۸ ۲تا صدا مثل انفجار و کمی لرزش حس کردم فاصلش خیلی دور بود، بین ساعت ۸ تا ۹ هم یک صدای مشابه اومد فکر کردم توهم زدم
اصفهان صدا انفجار نزدیکای جی شیر(مطمئن نیستم)
سلام. اصفهان حدود ساعت ۹:۱۵ صدای ۲ تا انفجار به فاصله چند ثانیه.
نمی دونم چیزی زدن یا دارند مهمات خنثی می کنند. البته تقریبا هر روز صبح یه صدا میاد که به خنثی سازی میخوره.
امروز ۲ تا پشت سر هم بود.
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 406K · <a href="https://t.me/VahidOnline/75840" target="_blank">📅 09:10 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75839">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/nDTEH2RVxmevlXIpt0EkvPcjaHuS9LxhMxoJL3Lw7YWiSZcU2zo09Xc_2tBhjH-XC-yLIYUokhFASht-pqZSgMv1p1zprwOWSoHVSzwLtG3_lW3DVOBU5S8XIecXgZ4NzP3wUWzqCJiC3sSUYH8zhBnompKCTtbghhvi3NFSrGYtCnyrNoxXj7Q_47saNCU-WKWB6DA3ljuEN11XEJke6rD3XEizKBMmj2JORvXuEaQDuVIMpTmrNifB5shT_A3iC3PD9o20A5dHsKzuiUeEQfnhDeVhonztSY7kvgsz0t2t0baXQMtWh7fjEDeB9gknTO3cJpf-ukyINKkxxvqW3w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پست ترامپ، ترجمه ماشین:
ایران واقعاً می‌خواهد به توافق برسد، و این توافق برای ایالات متحده آمریکا و کسانی که با ما هستند، توافق خوبی خواهد بود.
اما آیا دموکرات‌های کودن و بعضی جمهوری‌خواهانِ ظاهراً غیرمیهن‌دوست نمی‌فهمند وقتی سیاسی‌کارها مدام و با شدتی بی‌سابقه غر می‌زنند که باید سریع‌تر حرکت کنم، یا کندتر، یا جنگ کنم، یا جنگ نکنم، یا هر چیز دیگری، کار درست و مذاکره برای من خیلی سخت‌تر می‌شود؟
فقط بنشینید و آرام باشید؛ در پایان همه‌چیز خوب پیش خواهد رفت — همیشه همین‌طور است!
رئیس‌جمهور، دی‌جی‌تی
realDonaldTrump
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 399K · <a href="https://t.me/VahidOnline/75839" target="_blank">📅 08:43 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75838">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">پیام‌های دریافتی:
امیدیه خوزستان صدای انفجار شنیده میشه
از امیدیه خوزستان پیام میدم
طرفای ساعت ۸:۱۳ دقیقه صدای ترکیدن اومد
ساعت ۸:۳۱ دوباره زدن
همین چند دقیقه پیش صدای انفجار واضح ای اومد
امیدیه هستم و صدای دوتا انفجار شدید ساعت 8:33 اومدش.
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 363K · <a href="https://t.me/VahidOnline/75838" target="_blank">📅 08:40 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75836">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">قوه قضائیه جمهوری اسلامی اعلام کرد که دو نفر دیگر از معترضان دی‌ماه ۱۴۰۴ را به اتهام «آتش‌زدن مسجد [گیشا]»، «لیدری کودتا»، «تخریب اموال عمومی» و «مسدودسازی خیابان‌ها» اعدام کرده است.
نام این دو معترض که بامداد دوشنبه یازدهم خرداد اعدام شدند، مهرداد محمدی‌نیا و اشکان مالکی اعلام شده است.
میزان نوشته این دو «از عوامل اصلی آتش‌زدن مسجد جعفری در محله کوی نصر تهران [بودند] که اقدام به تخریب و آتش‌زدن مسجد، تخریب اموال عمومی، درگیری با مأموران حافظان امنیت، انسداد خیابان‌ها و ممانعت از عبور و مرور مردم کرده بودند.»
دستگاه قضایی جمهوری اسلامی در ماه‌های اخیر به شکل تقریباً روزانه اقدام به اجرای احکام اعدام معترضان و یا افرادی می‌کند که آن‌ها را به همکاری با آمریکا و اسرائیل متهم می‌کند. برخی نهادهای حقوق‌بشری می‌گویند جمهوری اسلامی از اعدام برای ایجاد فضای ترس و به‌عنوان عامل سرکوب استفاده می‌کند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 378K · <a href="https://t.me/VahidOnline/75836" target="_blank">📅 08:08 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75834">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/FNHV_CUcXD0i8TkMEXElrJQXDkPzYU6nnVD5io90t8fpEs_5dVzM2NaNGBbcH3wtemTQ-TT03zZBCJFDKPDd2IZXBiULwUU4p6ts7QFNZT2bAsNHnWsCWjgKu7wlvfMSWwV7pEKX-_1T2oKfmkEVqZZOuFzAPcp3-VfvEDxm631zUBEyS9VhClHdNvb5Oh8DbZyB9ahC9m7ehHb1X-cVE2Nu7kLJWprBKVj1ks82PAHANyuIe9TDqLb0nFNTEow7mT4vU6XFtce6qoZWHRF-WIW1E76wvo9vMR0dEQOjiJTZi05Tr5tC8vZ-JPiB0mFQq04DK_qQswDdErCtFoyw1g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/sy_OzNz9RuERGUk49mRjyDN6-FXexnaKhWk2BnDWi7F7Pk7h8XuiansARjjSp_dcb2d3bWTDfoWt4f0WbdikUjXauQBCY3sNSqIzFZhDXUNCTBoKbonYHh4Xt94pDUipLtW5Xg8Yh_smPueTnYoWc3-skBlKzqLi4xy4NSKmcZ6G7xGKEgmODklwuMeNR7avCU4q3d_PuroOuxmsf953O963a-JgtBWMHrqWFaz90jijGdYS6aPSWKt61go34KLEKP6fvIBMfzxLwcbU7uHwevQHPntNbnCTXqJLdtbFQHkD95N6htXRPdrh_RMMllaicMPdOP4q5sMJ3o6nsAizaw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">بیانیه سپاه: ساعتی پیش آمریکا به دکل مخابراتی سیریک حمله کرده بود پاسخ دادیم
من اون موقع فقط از یک نفر دو پیام داشتم:
ساعت 4:00 چهار انفجار در شهرستان سیریک
پایگاه سپاه سرخور زدن
ساعت 4:26 دوباره یکی زد
هرمزگان شهرستان سیریک
و الان کسی تصویر دوم بالا رو فرستاد و نوشت:
"حدود ساعت چهار صبح، آمریکا با چند موشک به اینجا حمله کرد.
پایگاه  نیروی دریایی سپاه  شهرستان سیریک ، حوالی روستای گروک"
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 353K · <a href="https://t.me/VahidOnline/75834" target="_blank">📅 07:20 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75833">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/a89b39dc76.mp4?token=Rs2_lEqI0XmonT4WRxI0q9qI63L86cp4Nk_kdnkkN1C4gmQvd6zeDm2LYcUEzEUn5PWoirDgTopuOJR6M5evpqBvBtoRdJW1Q9CmWDLaMgzzb2WUNRBCIZzvVm_gWLOL_FzyqShcaXCS8zt2YO-QpuBjKqqM1AzRmxCmNfg-IHDQa6EX18511aKpAGh30p0MduKJxlvjgoFKTbLdkdqjFm0sK5Q1Xh9e9uGH3jKZoY6_8FYyq3gHivgZ7nPGB5mi5tawP-D-fFWQgpXpLRFKXxpvTLrsgor6ZTX73T7wgUfdzaX0q5V8oRiERJAehLLrApdxpDt0cQnFhTlXUtcQig" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/a89b39dc76.mp4?token=Rs2_lEqI0XmonT4WRxI0q9qI63L86cp4Nk_kdnkkN1C4gmQvd6zeDm2LYcUEzEUn5PWoirDgTopuOJR6M5evpqBvBtoRdJW1Q9CmWDLaMgzzb2WUNRBCIZzvVm_gWLOL_FzyqShcaXCS8zt2YO-QpuBjKqqM1AzRmxCmNfg-IHDQa6EX18511aKpAGh30p0MduKJxlvjgoFKTbLdkdqjFm0sK5Q1Xh9e9uGH3jKZoY6_8FYyq3gHivgZ7nPGB5mi5tawP-D-fFWQgpXpLRFKXxpvTLrsgor6ZTX73T7wgUfdzaX0q5V8oRiERJAehLLrApdxpDt0cQnFhTlXUtcQig" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">'شلیک موشک از
#امیدیه
در خوزستان'
ویدیوی دریافتی دیگر از همان موشک،
دوشنبه ۱۱ خرداد ساعت ۶:۳۰
Vahid
ستاد کل
ارتش کویت
دقایقی پیش اعلام کرد سامانه‌های پدافند هوایی این کشور در حال مقابله با حملات موشکی و پهپادی دشمن هستند.
به گزارش خبرگزاری رویترز، جزییات بیشتری درباره این حمله پهپادی منتشر نشده است.
ارتش کویت در بیانیه خود تاکید کرد که صداهای احتمالی انفجار ناشی از رهگیری اهداف مهاجم از سوی سامانه‌های پدافندی است و از شهروندان خواست دستورالعمل‌های ایمنی را رعایت کنند.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 323K · <a href="https://t.me/VahidOnline/75833" target="_blank">📅 07:01 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75832">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/PsNhLMLJHMVHEEi7ATdlQ5dZeOpgjSzyhmY9l7xuLHSmO9jRugPxYs-0w9H3BiTkTU01eYFAZTaFPu0A-zQ6RS26XQ4OxY81898OWJQ1XpYCots77sTc9I6uA0KL9R3I7wfmGcFxrh0hYO0fcgVRtbJgHUYvH3ITht2DbfkdZDz3a9eTowOCOD61YyEXd6No5ZTVvKM2FmiJA3sAROYe0WaL1JecE-griOiAz_dNnwdGXv0aYROREUDOYmcYReMJcQmi9vY60Ep335TeI-8rJXsM92wJZim-LCO3tGHZ1L0jwyF-Jb2hqbXGGosSCyt6r_npYQCwCTM3o8B6lhPoaw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بیانیه سنتکام درباره حملات شنبه و یکشنبه
(از جمله حمله ساعاتی پیش به سیریک هرمزگان که با توجه به
پستی پایین‌تر
گویا حدود ساعت ۴ صبح دوشنبه به وقت ایران انجام شده. در آمریکا هنوز یکشنبه است.)
ترجمه ماشین:
"آمریکا در واکنش به تجاوز ایران، از خود دفاع کرد و تهدیدها را از کار انداخت
تامپا، فلوریدا — فرماندهی مرکزی ایالات متحده آمریکا، سنتکام، این آخر هفته حملات دفاعی علیه سایت‌های راداری ایران و مراکز فرماندهی و کنترل پهپادها در گروک ایران و جزیره قشم انجام داد.
این حملات حساب‌شده و عامدانه، روزهای شنبه و یکشنبه و در پاسخ به اقدامات تهاجمی ایران انجام شد؛ اقداماتی که شامل سرنگونی یک پهپاد MQ-1 آمریکا بود که بر فراز آب‌های بین‌المللی فعالیت می‌کرد. جنگنده‌های آمریکایی به‌سرعت واکنش نشان دادند و پدافند هوایی ایران، یک ایستگاه کنترل زمینی، و دو پهپاد تهاجمی یک‌طرفه را که تهدیدی آشکار برای کشتی‌های در حال عبور از آب‌های منطقه‌ای محسوب می‌شدند، منهدم کردند.
هیچ‌یک از نیروهای نظامی آمریکا آسیب ندیدند. سنتکام در جریان آتش‌بس جاری، در واکنش به تجاوز بی‌دلیل ایران، به حفاظت از دارایی‌ها و منافع ایالات متحده ادامه خواهد داد."
CENTCOM
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 311K · <a href="https://t.me/VahidOnline/75832" target="_blank">📅 06:57 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75828">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/UBBrP6gZn1hPDj9Vw5NVmBT1qmQZQbmjSO-Sul7BkhUgay4grZO-5PRxYr-rsa8AbhyKENdF7lE4NscSZugBdRjxzNZQqS_b8aJycITcyqumYINjQsJMI73s5MhVmVR0iKm0a96ScAS1muS-WKjIIYkyRhiKlRkJQpURrVmU47LQhOgrPerGAyEav9WnnNMPwPKf2P7GtvCBeWI8DFTFjjzNFaxu4_PpwcIfCSRwsSyjZosxJ9dufxXbtmDZbC6L1u27o50WaWZug5GJkYLjShi61FBXIfkm0zVKu91M7RDDHi-4SGHtpfFsKwXND7ruGm3J1a0pWHnbJdo0VoSeQw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/OfvfqSg4mky3Oz3YLmcapgB9KrwTlK6Qa04scmbJ4MDxkF1KfaLfZlAZ8sqN48mqNWF_wivEs1UfbM7N5zzIqchYYv8f-pjWpFHIMAI4mvWpuewntWDCgNoxMkAUdSQgYEEGUDivbZewxuC75zd17yGpbCI1m-wHSiMsNB1K5wQT0QkFuFByTpj6JvHpYJx4_1e3oh38TRXKA4ug0NzC7yNqLI5FgpI1WjHp6ihkw6vs8ZnxWk3HiEiB7_BhTywckidMiGkaJtCViII8CKs4Nr3m2GTn3-qewPnSNYmCCGzx8Sjjpj8sVPRk3G3EYFGzUBUsmWW5VsJDxVtc_bW1RA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/oJBV6_ezyyAxu1bvX_FNPXEBKTu6bVMmnCL4Ab8n2GnPkQY1gsbq3-RskqFbtTZjyaTIW-3EMKfsiNYY1ENaLEPudnYiGifl514fVcrKch6qqVhXwWqEgF5OWE2mzW5gMKZyPszg1hjYhURlTEnEi4g8br9NOoAArmjqM-XLZpfPt_kq6nzCcfPKoKFiUVhObCyqwK5dAPeBC9FYo891XBSSqSZm1Oktb4jrUxgmfkXlgIF0FrrjPsPMtsC6v5_gaPTrkKl_HQYfr_IGuAx_LuhC05y8K40mGEErqPzmziLlHkHyRXi3fSp5QgU3hEed4fWi4HMvufxpQ1VuJoFATQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/1affc9bf27.mp4?token=TS6342YK8z-Y0oKSKbFp2zRdNHp05Bk73O_g5A7ubFbDYAoo9GgVyJrXfqUlaZd7zwe0EvROm01hiD24J_p310jsNFdPgWOUW7M-IOtTA89AbXhw36S305T76udMS_1Svfy-hgqQdwQjwb-evOxzwEOTN_NJAVtArUkwymRyltfMkYhn0XTY-j9B-a9bR8yerIkkBlCVSfAEDUOhrPTG4LsH4FQpogfvJIYazJ0qWorK7fCVxj3QJNtP8_DG9inWLy8DPrNRZAX2hNjK77lZXv-A-beJ8f7iVDgWU8ZqZcSnI3AntTO7mif_xauTl0zXMIuexAXgNJjPB94ReCE9og" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/1affc9bf27.mp4?token=TS6342YK8z-Y0oKSKbFp2zRdNHp05Bk73O_g5A7ubFbDYAoo9GgVyJrXfqUlaZd7zwe0EvROm01hiD24J_p310jsNFdPgWOUW7M-IOtTA89AbXhw36S305T76udMS_1Svfy-hgqQdwQjwb-evOxzwEOTN_NJAVtArUkwymRyltfMkYhn0XTY-j9B-a9bR8yerIkkBlCVSfAEDUOhrPTG4LsH4FQpogfvJIYazJ0qWorK7fCVxj3QJNtP8_DG9inWLy8DPrNRZAX2hNjK77lZXv-A-beJ8f7iVDgWU8ZqZcSnI3AntTO7mif_xauTl0zXMIuexAXgNJjPB94ReCE9og" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">'شلیک موشک از
#امیدیه
در خوزستان'
تصاویر دریافتی، دوشنبه ۱۱ خرداد ساعت ۶:۳۰ به وقت
#ایران
Vahid
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 295K · <a href="https://t.me/VahidOnline/75828" target="_blank">📅 06:45 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75827">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/nyvdjarWolyCF3hKXANBF3VpRg8bATPh74B_fnXZcOISY_22UO7mVskNN-lGIMmPRB8in_ME-DF9_jMSHEDSzlstTuPxeY5wqZpTmEdKkITz4JE17hcgEAYIzJVp2oQzJi8C7fpV8fFM3doXMNaRN4U3HIOkUCj4qo6gFykXppDdAtnsTCBCSEIUFbzGKM4kDNLiQ79TuEtxCGPJ9obZ0j1RtXF5hJKAp_oMMQO0qKsKIMrHs9D_lP0GHsEQHhYdA0Ptep_3Kw_OsZhrm7Cbci4wM7GtyOpdk-0jK-ryJj27V8-oszDG-U31E8HV3DZ1z5UJJQUBC4CiwNFhVJN3Tg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شلیک موشک به کویت
دوباره همز‌مان پیام‌هایی درباره شلیک موشک از امیدیه خوزستان و اعلام هشدار در کویت دریافت کردم.
دوشنبه ۱۱ خرداد
ساعت ۶ به وقت کویت که میشه ساعت ۶:۳۰ به وقت ایران
Vahid
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 343K · <a href="https://t.me/VahidOnline/75827" target="_blank">📅 06:33 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75826">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/bwn4MFAKVy0wJ5vMqJdDE2NrsJllaeXx0PabcvhYosI10u7IuG_OQCXq4862Ind4DbHZmyKXJBRg9zPGMJqK0IhgUNA0CjK0a5B4AfY98Dmi7kFnV26FPYfquIPI3Ofuj0YXITBJfPpa-g7fwkTi-9O1wgmi3YYDGOO8Sq3ipTK_OgH36iw40AT42KVPpqiLN6Agn0S9bipetpYJ-RX-1uKfvsD04x3C4sMt2MmaUDf3a0-RJtQTeWk9E79PDR8JT2uq37GawmNCzGPBTlg6UiRimIAVjVAu6E89iDZ6NfY7Mut4PXDzzhJaYbyUbGwKT7Ypq0ow0_rNDORY2vZwyA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پست ترامپ، ترجمه ماشین:
رسانه اخبار جعلی سی‌ان‌ان امروز طبق معمول گفت که توافق هسته‌ای ایرانِ من درباره مسائل هسته‌ای صحبت نمی‌کند؛ در حالی که در واقع، بسیار روشن تصریح می‌کند که ایران سلاح هسته‌ای نخواهد داشت.
سپس با جزئیات بسیار محکم و مفصل، به جنبه‌های مختلف دیگر موضوع هسته‌ای می‌پردازد.
در واقع، بیشترِ این توافق درباره همین موضوع است.
سی‌ان‌ان و بسیاری دیگر در رسانه‌های اخبار جعلی، فاجعه‌ای با رتبه‌های پایین هستند.
حتی با مالکیت جدید هم بعید است اوضاعشان هرگز بهتر شود!!!
رئیس‌جمهور، دی‌جی‌تی
realDonaldTrump
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 357K · <a href="https://t.me/VahidOnline/75826" target="_blank">📅 03:32 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75825">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/rnpKptZCeH8NdErty9x6SxSwH9aHDcPibCzsxN4ftMGoW9t7VbcV1bMQnjIf4COTPViy0hVZTIcAwwUS7WPCELZWZi07MLHl2qnKq1t9K_0xHgVcGHSIM9NlQnbiq-lYvA27Dt0loORysgQJPSk8BPrjTf6_DIIHcIPSssE8D6AIxLEDr5yeoW6oZATAWt3rH2PxtRE8BmM-6wZy_0-22j3CBt75ImAU63XPkOQ24YlA0hFHyw1f_ixzyCFt7z5zI3IRyVXUaiySgoIYnHKY-fJvKdyRJWaxPFEggkzC9HgKOQaUSVdvG_EXTfkJiiQMoC7S58WTH_7SA7Z7ErwuEw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فاکس نیوز هم به درخواست استعفای پزشکیان پرداخته:
FoxNews
چند مقام دولتی با تکذیب شایعه استعفای مسعود پزشکیان، آن را «خبر کذب با هدف ایجاد ناامیدی» خواندند.
فاطمه مهاجرانی، سخنگوی دولت، الیاس حضرتی و علی احمدنیا که از اعضای شورای اطلاع رسانی دولت مسعود پزشکیان هستند در پست‌های جداگانه به ادامه کار رئیس جمهوری و تلاش او برای «حل مسائل کشور» اشاره کرده‌اند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 414K · <a href="https://t.me/VahidOnline/75825" target="_blank">📅 00:19 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75824">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/eCZwpE7CbrlsbTn6YUPxBaVzFivY_fHm3WxlxrWPX1nrpI8n40fIzfcQrEZzMYLO4wDZkJ68Y6ot81aDhnA1mRwcf0qJ0FGXiLPDfJsum-QeIZNwK599uaNbj-J9YYPW2enmJw1BCpk5WVJHHypWgACA0D75tcHMT-un8LtZzV2RmnDbmcX8HEzycX-DcvUQkceJ8rXxN45RrMn08RNSG9PcxSGBWnUjv_s68HZ0DMYMZvRdazO_T_w2EBJPAoRhibICxc6XR2Qo0mJkgYcM0qDyJuTs6hIDC2KvdCABvmvIoW1neTGXSlC6e9hwaHON42Sif5OTJ1g926WHH9GXQw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رسانه‌های جمهوری اسلامی وقوع دو انفجار را که تقریبا هم‌زمان در تهران و کرمانشاه و در ساعات پایانی یکشنبه گزارش شد به نشت گاز نسبت دادند.
سایت تسنیم، نزدیک به سپاه پاسداران اعلام کرد که در ساعات پایانی روز یکشنبه، «انفجار گاز» در محله باغ ابریشم کرمانشاه باعث مصدومیت ۲ نفر شد.
این سایت‌ همچنین [با انتشار عکس بالا] مدعی شد که انفجار در یک واحد مسکونی در «فاز یک اندیشه» در استان تهران ناشی از «نشت گاز» بوده است.
خبرگزاری ایسنا به نقل از سخنگوی اورژانس استان تهران می‌گوید این انفجار تاکنون ۶ مصدوم بر جای گذاشته است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 416K · <a href="https://t.me/VahidOnline/75824" target="_blank">📅 23:54 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75823">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/5c3fc33b86.mp4?token=EfFLl1RV_7YosR9jonmkVZj0uKgLiOwj5oab05rzJ_GV92bk-ybsYuyIzyTweZZ_plymuzsBq-xgZUhKcfyNGcxJh-NJNRHzPpnIspY_ePnLvfI1EFFvj3F5oy2r2DLsoA8CqIHCHQH33BfRpxcc_cPsaMVaN60Ue40MCUw0AsvdIYxRo1vRHByXeK5XQ2JuGRdTmqxz2Oic-Dqn4pvQ-Tq0QslDzp_h3GhSqZJM73VTL_qSiF0fkTKYa7BfpipUV7YFQT6xH0gjWcUKtximV_SWRsWpGe03ihKYuOaEvS2J1FuLsjGtX_RIXAYTTiM1GYIgVgbG3_IuZDt2WiajiQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/5c3fc33b86.mp4?token=EfFLl1RV_7YosR9jonmkVZj0uKgLiOwj5oab05rzJ_GV92bk-ybsYuyIzyTweZZ_plymuzsBq-xgZUhKcfyNGcxJh-NJNRHzPpnIspY_ePnLvfI1EFFvj3F5oy2r2DLsoA8CqIHCHQH33BfRpxcc_cPsaMVaN60Ue40MCUw0AsvdIYxRo1vRHByXeK5XQ2JuGRdTmqxz2Oic-Dqn4pvQ-Tq0QslDzp_h3GhSqZJM73VTL_qSiF0fkTKYa7BfpipUV7YFQT6xH0gjWcUKtximV_SWRsWpGe03ihKYuOaEvS2J1FuLsjGtX_RIXAYTTiM1GYIgVgbG3_IuZDt2WiajiQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خبرگزاری تسنیم، وابسته به سپاه پاسداران انقلاب اسلامی، در واکنش به گزارش شبکه ایران اینترنشنال درباره استعفای مسعود پزشکیان، رییس دولت، این خبر را تکذیب کرد و آن را «شایعه‌سازی» خواند.
شبکه ایران اینترنشنال، ساعاتی پیش در گزارشی اعلام کرد مسعود پزشکیان در نامه‌ای رسمی به دفتر مجتبی خامنه‌ای، رهبر جمهوری اسلامی، خواستار کناره‌گیری از سمت خود شده است. این رسانه همچنین نوشت در این نامه به وجود اختلافات ساختاری در اداره کشور و نقش نهادهای نظامی در تصمیم‌گیری‌های کلان اشاره شده است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 432K · <a href="https://t.me/VahidOnline/75823" target="_blank">📅 21:14 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75822">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/KiDLB3W3oJlbhaSpaGNK8PR5SdFXGQgrLCUqy8s6xsko87qqPR3Dv-gpilDOiLHQd6lBP9swwj032tGkg8cd_LNknRWGeghciAyg1MektjUBFOiMYAWM3QvNoW_F8V0lY6LBk6huSVH-nPMWIJzs9ML7lBjZVOa68QuL26j5TVFW932cqsmdaQL8nas0Ph1GFztYVO7IMF1mVERV9a5_sNqLhtGei2mKr1SAvTAeS-z5Bf9nFDLCvK1igrUCjTxGx46gfslcvRXLXC53KPAudSgqznaOyZOT3XwHBiqYAMU8lSca9piz0GE0cy8W1lLfTD_iwQScbVy3wa6BM6nWUQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">IranIntlbrk
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 432K · <a href="https://t.me/VahidOnline/75822" target="_blank">📅 20:03 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75821">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/E43tK20gs070UIxXigp-2qDjJGvX3rR0w6HDDBCvMlEma6E-2MW0Swb8RioarqRXVvLXZ4dnlxMaJqRmtvsQjrv8JIrAtZoAdfMorpiQdq9mmL6WEAAcwDRwOThoeKOpZ_4wMNBvJ6vmvomg_w-sHxBojbMOPQsmIsbiW6RpLTbr61hrB1ueZWvk0DHlJcrJJWrl4f9Kj5Lj9XlGJ6X8RYiymSyEklmsNSDulzIaakb-9GCceTsoX0Z6oSgtdzuuHzbH_UO-GgRaiaBAvi-_nKZbh79fl5WzfchEhaWACWQXeJ_AF6wg5EqSkk2F13y6B23Nk-K5dmAKu7tIiWC0sQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مسعود پیاهو، مردی که تصویر معترض نشسته مقابل نیروهای پلیس یگان ویژه در مقابل پاساژ علاالدین در آغاز اعتراضات دی ماه سال گذشته را منتشر کرد،
به گفته وکیلش
به ۱۰ سال زندان محکوم شده است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 426K · <a href="https://t.me/VahidOnline/75821" target="_blank">📅 19:07 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75820">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/6220710705.mp4?token=hDMpSIfFSJVckrTOVo30T-npCjR_dGyGDBKG1FDJ_n5SIZNWd6th4PquDTRf1qHme9wT84Qmx4kKnFfgeIA0vBq96aKG0_I1kjg_7cvFHNHiBb4g1V1mzCiz9dnV2R64O_KF4Yp3jIcj3zcx27eRAp7YV-xMIIGjGu4jWUaT9T-EyNJHL1Tetg7konEQurY72td8hCQ1HPnyfYsbYD_VLhS-rImhW4mN8IMXUiHfLhVLVOCWa6A4X-y5YCucJUP0yssTjjdfr94X5rG6ZjdN2oLE8-Jda4NmQshhpqzoyMtGE2g1yT5eVkbmIzrNz4W1qmm-m1CSzlcZZgA3BjfGYQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/6220710705.mp4?token=hDMpSIfFSJVckrTOVo30T-npCjR_dGyGDBKG1FDJ_n5SIZNWd6th4PquDTRf1qHme9wT84Qmx4kKnFfgeIA0vBq96aKG0_I1kjg_7cvFHNHiBb4g1V1mzCiz9dnV2R64O_KF4Yp3jIcj3zcx27eRAp7YV-xMIIGjGu4jWUaT9T-EyNJHL1Tetg7konEQurY72td8hCQ1HPnyfYsbYD_VLhS-rImhW4mN8IMXUiHfLhVLVOCWa6A4X-y5YCucJUP0yssTjjdfr94X5rG6ZjdN2oLE8-Jda4NmQshhpqzoyMtGE2g1yT5eVkbmIzrNz4W1qmm-m1CSzlcZZgA3BjfGYQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اسکات بسنت، وزیر خزانه‌داری آمریکا، در گفت‌وگو با فاکس‌نیوز درباره ایران اعلام کرد: لایه اول و دوم حکومت آن‌ها از بین رفته و اکنون با لایه سوم روبه‌رو هستیم. شاید آن‌ها دیده‌اند برای بقیه چه اتفاقی افتاد و می‌بینند ترامپ آماده انجام چه اقداماتی است.
بسنت افزود: اگر ترامپ با این توافق موافقت کند، همین حالا به رهبران جمهوری اسلامی می‌گویم که او این توافق را هم از نظر نظامی و هم از نظر اقتصادی اجرا خواهد کرد. آزادی کشتیرانی در خلیج فارس از طریق تنگه هرمز باید به وضعیت پیشین بازگردد.
او درباره اینکه آیا ترامپ «کار را تمام خواهد کرد» گفت: اگر «تمام کردن کار» یعنی اطمینان از باز بودن تنگه هرمز، در اختیار گرفتن اورانیوم با غنای بالا و نداشتن سلاح هسته‌ای از سوی جمهوری اسلامی، پس کار تمام شده است.
بسنت تاکید کرد: چه از طریق مداخله نظامی، چه محاصره یا فشار اقتصادی، این نخستین بار در ۴۷ سال گذشته است که ایرانی‌ها درباره نداشتن سلاح هسته‌ای گفت‌وگو می‌کنند. این موضوع پیش‌تر ممنوعه بود و اکنون برای نخستین بار روی میز مذاکره قرار گرفته است.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 368K · <a href="https://t.me/VahidOnline/75820" target="_blank">📅 19:07 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75819">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفرهمند عليپور Farahmand Alipour</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/65778ca5eb.mp4?token=sXjMG4_MSycKYWKaPqp0Y9Uz3_-5C-lz3fo1VP9mHnaQQb1AKzla6dFDycP5Cgfm2C6PyU8sf-QqCIq483qVZAPCAlwXJeG4IOLivu2qUY8KsuFVvblFQNPqje_RIl8E4Gj1XzFAj2m4I3EJGBfXY9pw5nLH-TZLP8fYbPrfGoIhJx5wGkHtL9GbNwQnqktefxE73VcO2Kyby7tHetbECInAOjqHHWHH26Z3ioEE27R1D2N7WnmTgvbiOrrCPs-KPsPu_w6YK2d8CzUalGfuZWPGmPPIkddw7Ma1X98_arwsH40RejM2Y3bkUtoSIUe0Tdxv4bBNMMbnNac3lC8v-w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/65778ca5eb.mp4?token=sXjMG4_MSycKYWKaPqp0Y9Uz3_-5C-lz3fo1VP9mHnaQQb1AKzla6dFDycP5Cgfm2C6PyU8sf-QqCIq483qVZAPCAlwXJeG4IOLivu2qUY8KsuFVvblFQNPqje_RIl8E4Gj1XzFAj2m4I3EJGBfXY9pw5nLH-TZLP8fYbPrfGoIhJx5wGkHtL9GbNwQnqktefxE73VcO2Kyby7tHetbECInAOjqHHWHH26Z3ioEE27R1D2N7WnmTgvbiOrrCPs-KPsPu_w6YK2d8CzUalGfuZWPGmPPIkddw7Ma1X98_arwsH40RejM2Y3bkUtoSIUe0Tdxv4bBNMMbnNac3lC8v-w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">عراقچی در تاریخ ۲۹ آبان ۱۴۰۴
در تلویزیون جمهوری اسلامی میگه ترامپ به ما نامه‌ای داده و صراحتا نوشته
«دو گزینه بیشتر نیست»
یا جنگ و خونریزی یا مذاکره مستقیم
«برای از بین بردن غنی‌سازی و موشکی»
این مصاحبه چند ماه بعد از جنگ ۱۲ روزه بود! یعنی در آبان ماه، مشکلات آمریکا و جمهوری اسلامی همچنان همون چیزهایی بودند که باعث یک جنگ شد، و این مصاحبه یک ماه پیش از آن بود که دست به قتل‌عام مردم در خیابان‌ها بزنید!
الان هم محور مذاکرات کاملا مشخصه!
همون چیزهایی است که جنگ ۱۲ روزه رو رقم زد. همون چیزهایی است که در آبان ماه عراقچی در تلویزیون گفت.
خون تک‌تک ایرانیان از جمله کودکان میناب پای شماست! شما طرف مذاکره بودید، شما انتخاب کننده و تصمیم گیر بودید.
و شما بین اورانیوم و موشک، و یا جان مردم، زیرساخت‌های کشور، فولاد و پتروشیمی و…
اورانیوم و موشک و دشمنی با اسرائیل و آمریکا رو انتخاب کردید! هنوز هم طرف مذاکره و تصمیم‌گیر شما هستید! و‌ جنگ ‌از سر گرفته بشه باز تصمیم و انتخاب شماست و مقصر شما هستید!
نمی‌توانید پشت کودکان میناب قایم بشید و از کشتار دیماه فرار کنید!
هر خون و ‌هر ویرانی ، همه پای شماست.</div>
<div class="tg-footer">👁️ 322K · <a href="https://t.me/VahidOnline/75819" target="_blank">📅 19:05 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75818">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/fWcZxqxpUhK8Vid1dV3r_IpoydjmAw9-AjsP0DExskio0Jd2-rQ9N-_BTtnBCQmfYl-7Qp4KEI94qnKSy8_0O7RwQOYuFGH1KRF9IhuWfFzPlW3hizbMACABrQu4bgbsFnazH2DacNrtWE8PopR-d1HYuX7K2BgtJcELcW4lijJ1axqOn4pkj5DlaLPnKXbnmGXoGOGN09iOqSghwvPgMPfMFkxwA8cjbIopSD2M6lmYdX7Q1HY-sJJ1OVt-QA8FM30xEyA8UwyXjxHydNz-0Yq1ZPjHKFkV3_IYzK0btmushdGDK6gDxTwNAWDKOxwL42NU2QaAW8WY_PXnNgIZsg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حسن و حسین امیری، دو برادر دوقلوی ۲۰ ساله محبوس در زندان قزلحصار کرج، از سوی شعبه ۲۶ دادگاه انقلاب تهران به ریاست قاضی ایمان افشاری به اعدام محکوم شدند.
بر اساس اطلاعات دریافتی هرانا، مبنای صدور این رای اتهام «جاسوسی برای اسراییل» عنوان شده است.
یک منبع مطلع در گفت‌وگو با هرانا اعلام کرد در کیفرخواست صادرشده علیه حسن و حسین امیری، مشاهده تصاویری از ساختمان‌های آسیب‌دیده به عنوان مستند اتهام «جاسوسی به نفع اسراییل» مورد استناد قرار گرفته است.
این منبع همچنین گفت: «حسن و حسین امیری به دستور بازپرس پرونده به صورت جداگانه در زندان قزلحصار نگهداری می‌شوند و از حق ملاقات با یکدیگر محروم هستند. این دو زندانی در حال حاضر در سوییت ۳۵ این زندان محبوس هستند.»
بر اساس این گزارش، این دو برادر پیشتر در یکی از ایست‌های بازرسی و پس از بررسی تلفن همراهشان بازداشت شدند.آن‌ها پس از بازداشت، به مدت دو ماه در وضعیت بلاتکلیف در زندان قزلحصار کرج نگهداری شدند.
👈
حسن و حسین امیری از دو سالگی در مراکز بهزیستی پرورش یافته‌اند و خانواده‌ای برای پیگیری وضعیت قضایی و حقوقی خود ندارند. به گفته آشنایان این دو جوان، نبود حامی خانوادگی بر نگرانی‌ها درباره روند رسیدگی به پرونده آنان افزوده است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 310K · <a href="https://t.me/VahidOnline/75818" target="_blank">📅 18:51 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75817">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/V5IEQB555CBp0unvEiWNZ8TYfOm9dJAhtsvw8MYPPV4Qv1Cs01_InobLmrsHySIyfEeQ3EOipi8amsRaCNHDYZEoo3ocXE30MPKm6qqmH7MiQxSYobFMjp8U1djZgZzRyx71mdb-XPpb3J6D0jNwP6rM4krvdPA8f_0y9XKnQM4vG1QKofLjRdRXSNL68HG8ew2J2SbA-ebuu4bF9sfewTik3iMGM35MM0mtazE4AiyT-RFQ--LzMd4xEFELCC-oKfLpsZ0cjiMvqKtYQeePBRQLTnF7F0rS0Wjg2qP75tq2vUCrZKNw-t1o4nNpuX6XlGuNds8C5iWXaGz1wW9oeA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سی‌ان‌ان: ایران چندین ورودی تأسیسات موشکی زیرزمینی خود را بازگشایی کرده است
شبکه خبری سی‌ان‌ان روز یکشنبه ۱۰ خرداد با استناد به تصاویر ماهواره‌ای اعلام کرد ایران توانسته از زمان توقف جنگ شماری از زرادخانه‌های موشکی مدفون خود بر اثر حملات هوایی آمریکا و اسرائیل را از زیر خاک بیرون بیاورد.
حملات آمریکا و اسرائیل با تخریب جاده‌ها و مسدود کردن ورودی تونل‌ها، دسترسی ایران به پایگاه‌های موشکی زیرزمینی را محدود کرده بود.
سی‌ان‌ان ادعا کرده است که ایران تاکنون ۵۰ مورد از ۶۹ ورودی تونلی را که در ۱۸ تأسیسات موشکی زیرزمینی توسط آمریکا و اسرائیل هدف قرار گرفته بودند، بازگشایی کرده است، از جمله در پایگاه‌هایی در خارج از اصفهان و در اطراف خمین.
بر اساس گزارش این شبکه خبری، ایران همچنین بخش‌های دیگری از این پایگاه‌ها را نیز ترمیم کرده است؛ از جمله جاده‌هایی که آمریکا و اسرائیل برای جلوگیری از تردد پرتابگرهای موشکی بمباران کرده بودند. تصاویر ماهواره‌ای نشان می‌دهند که تقریباً تمامی گودال‌های ناشی از بمباران اکنون پر شده‌اند و در دو پایگاه، این جاده‌ها حتی دوباره آسفالت شده‌اند.
ایران شبکه پایگاه‌های زیرزمینی خود را در عمق خاک و در مواردی زیر کوه‌ها ساخته است تا در برابر حملات هوایی مصون باشند، به همین دلیل آمریکا و اسرائیل بسیاری از ورودی‌های این تأسیسات را بمباران کردند؛ اقدامی که در کنار تلاش برای شناسایی و نابود کردن پرتابگرهای موشکی، باعث شد توان ایران برای شلیک موشک به‌طور قابل توجهی محدود شود.
این حملات خسارت سنگینی به پایگاه‌ها وارد کرد؛ به‌گونه‌ای که بیشتر ورودی‌های تونل‌ها زیر حجم عظیمی از آوار مدفون شدند و جاده‌های منتهی به این سایت‌ها نیز به‌شدت تخریب شدند.
سی‌ان‌ان می‌گوید باز کردن ورودی تأسیسات موشکی زیرزمینی می‌تواند به ایران این قابلیت را دهد که در صورت وقوع دور جدیدی از درگیری‌ها، موشک‌های بالستیک بیشتری نسبت به اواخر جنگ ۴۰ روزه به سمت اسرائیل و کشورهای دیگر شلیک کند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 321K · <a href="https://t.me/VahidOnline/75817" target="_blank">📅 18:49 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75816">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/r_s7UiONBVJ0VQvFIjdV1Le_aPHZnGtLkcI5hiHYOkiiQSezuI4XeKSNX2V7O8LvmEu-Vr5rioH9y5sl0vPQ9we_zzsNrQnc1ctUZM6VUhSkPbPjqE2ixy2ZR5Y2cnYLRcqws3AoFkGbmDDMKd_aPECnz7VksxJ_XejIDegi-nxTI9qfnoLU4JTGB3wk5PWB9dfHFjcLnOf5SLI3ZDhEld5e2fyYgmgWNpLKXoaOEyI68vpHolctGAWVy2OELLORRyjS4060mz6v9Cy8BS7bMpzjs9CXUcClFO6MkO7XWZ5sqG5A6h3M627ecUGveCtTBPZ_U8Lxn8aK7EojRluJzw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بر اساس مصوبه جدید شورای شهر تهران، هزینه خدمات مرتبط با خاکسپاری در بهشت‌زهرا به‌طور میانگین حدود ۴۰ درصد افزایش یافته و در برخی موارد رشد تعرفه‌ها به ۵۰ درصد رسیده است.
روزنامه دنیای اقتصاد گزارش داد نرخ خدماتی از جمله حمل متوفی، تغسیل، تکفین، تدفین و برگزاری مراسم افزایش یافته است. بر اساس این مصوبه، هزینه انتقال هر متوفی از سطح شهر تهران تا شعاع ۱۰ کیلومتری ۵۰ درصد افزایش داشته است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 323K · <a href="https://t.me/VahidOnline/75816" target="_blank">📅 15:59 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75815">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/o9owrn0ip3_kOISzTSqy_CIcOAdquew7ynbbNR9QET9FpqCUjghVFB0k7pOi3YN6g_EdJzlSDDhL0Hh5cSzPS2XtHSzQf11Oq-oiC2w2VXFcU-5iI-W3LGmiDAzBwybhDvLfcu6Pk_9_1vRWHlahZYLGvPfNncyIYI3UrUivMFUNXre4J2UrOKFvJcvP04oJtjULHattA_RJ8YrEA8FKsHQgN4EXe6hCYvecivOXZSvF-67pjEfZ1224YGzGakE-MXd--G0VTg9pUx843F8YFKDZlT9GvMlwDC_mDTk2y4Tz_HG-NfQsEd5fxupWG_gaRGhHLqvJkZAb2lObDcSUeQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سایت هرانا گزارش داد زهرا شهباز طبری، زندانی سیاسی محبوس در زندان لاکان رشت، پس از نقض حکم پیشین در دیوان عالی کشور، بار دیگر از سوی شعبه دوم دادگاه انقلاب رشت به ریاست محمدعلی درویش‌گفتار، به اتهام «بغی از طریق عضویت و فعالیت در سازمان مجاهدین خلق» به اعدام محکوم شد.
این زندانی سیاسی ۶۸ ساله، در فروردین ۱۴۰۴ در منزل شخصی خود در رشت بازداشت شده بود.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 311K · <a href="https://t.me/VahidOnline/75815" target="_blank">📅 15:58 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75814">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gzZLH8wKnvWJNWSf4n91-hYVqOdGPqM5N2nWjSid7NoUD5HtpO8J0dUG27zXie1pBXhaUrOibhBr1cD8MbaFgraJJ5px5DfIDTNygxnGt6QWPRa7Mo5t8RrFgIhJaJ-r7xuiQSMWiCKanBFwQDsTRMxJ_pvOxln9DkFFRJa7c3XB28VRUIdiIrdx689WDsYmPEw4C0C5B_JW2ENrYzChGVtC35Mu5oKdr2EPqNixkrbLG71Rezfhaz_GdhgV8Lgzg-yK8vXhunupexBy_po_a3cfPeeH1D2y6QCW7mT6kj2YsyAmrCn0x4Vc2Y_cjdDg2R6aFD5zs6GlovBFNMwM5Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نیروی دریایی سپاه پاسداران روز یک‌شنبه اعلام کرد‌ «طی شبانه‌روز گذشته ۲۸ فروند کشتی اعم از نفتکش، کانتینربَر و سایر کشتی‌های تجاری پس از کسب مجوز با هماهنگی و تأمین امنیت نیروی دریایی سپاه از تنگه هرمز عبور کردند.»
ساعتی پیشتر روزنامه اسرائیلی «اسرائیل هیوم» نوشته بود که ده‌ها نفتکش حامل نفت و گاز طبیعی مایع در هفتهٔ گذشته با اجازه آمریکا و پرداخت عوارض به ایران از تنگهٔ هرمز عبور کرده‌اند.
این در حالی است که دولت آمریکا بارها اعلام کرده است با پرداخت عوارض به ایران برای عبور از تنگه هرمز مخالف است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 305K · <a href="https://t.me/VahidOnline/75814" target="_blank">📅 15:57 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75812">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/pBLcdDis6H065Br9U1k5zkxs0hOGCmesLiwE_RrFPKOy2CZdnhieR9CdF8JqqRwFgL8lPpSTLbb0iTYguTJuD2DtowHp0-hqrOKreM2tH_BGlbXj0KXpyQlEDCg-QK3oTVxCBNqraCsP6OaxpWFP0XqAS-Wug0RdMOI9iDgbSqM97ZLlH8mE4jFg40mEMQzqXQBCgG1vM6j4uiFdmI8nNaexAB83fBlo25G6PfVX3dYrJCONrLclm16UaW8in4Mm4H1iEtyhWmVcGVw_Qq1AsClPHOBA03D7SJYx2A-SUFwncTvKKJ-AvsJxQjZXf0AHCPJsKWk1Wb_1Y2ptMoelYg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/c9b60ac63f.mp4?token=eaMYfcuFtCN9eSH2XHY8r8Ak58u7zUDkMzQZ4uIG_uu4BtX_A8OhH3YVJ_CEEoTn86oxzu9lArgcJEY6KPr1QGzLZGXYkwARwA2nuCyPsen4YMZ8ohIKtbnjCorypNRnl8UKJPoLE9LgXXq6-8FkRMZet5usNkoOYWbYubyZaMZleXxEbpiA6BinIxKs3OHiodylT5ddzgExK-N4HrBXjbO7Sq6OaLXZI0O8Ds5hYxUVayJAZxsZ6VJE-kWPsFxope-WFME1kW5W6G3h9dRLLb0bd5N95GA_UgiRrIo24IgdQlrw65_LMHUjagGPrO7uS2eDGI5RRN2pwogTxwmrRA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/c9b60ac63f.mp4?token=eaMYfcuFtCN9eSH2XHY8r8Ak58u7zUDkMzQZ4uIG_uu4BtX_A8OhH3YVJ_CEEoTn86oxzu9lArgcJEY6KPr1QGzLZGXYkwARwA2nuCyPsen4YMZ8ohIKtbnjCorypNRnl8UKJPoLE9LgXXq6-8FkRMZet5usNkoOYWbYubyZaMZleXxEbpiA6BinIxKs3OHiodylT5ddzgExK-N4HrBXjbO7Sq6OaLXZI0O8Ds5hYxUVayJAZxsZ6VJE-kWPsFxope-WFME1kW5W6G3h9dRLLb0bd5N95GA_UgiRrIo24IgdQlrw65_LMHUjagGPrO7uS2eDGI5RRN2pwogTxwmrRA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جلسه مجازی صحن مجلس شورای اسلامی به ریاست محمدباقر قالیباف و مشارکت آنلاین ۱۸۷ نماینده و حضور ۱۴ نماینده برگزار شد.
در این جلسه که اولین جلسه از سومین سال مجلس دوازدهم بود، اعضای جدید هیئت رئیسه مجلس سوگند یاد کردند.
جلسه روز یک‌شنبه، دهم خردادماه، همچون جلسات معدود گذشته در مکانی مخفی برگزار شد.
محمدباقر قالیباف در همین جلسه تأکید کرد که «تا اطمینان پیدا نکنیم که حقوق ملت ایران را گرفته‌ایم، هیچ توافقی تأیید نمی‌شود».
قالیباف که از او به عنوان رئیس هیئت مذاکره‌کننده ایران نیز یاد می‌شود در این جلسه بیانیه‌ای را قرائت کرد و در آن ادعا کرد که «در حال عقب نشاندن دشمن در یک جنگ تاریخ‌ساز هستیم».
@
VahidHeadline
محمدباقر قالیباف، رییس مجلس شورای اسلامی گفت: «سومین سال مجلس دوازدهم را در حالی آغاز می‌کنیم که یاد و خاطره رهبر شهید با ماست و هنوز فقدان رهبر و پدر امت را باور نمی‌کنیم.»
او ادامه داد: «رهبرمان به ما آموخت مقابل زورگویی و تهدید، ذره‌ای سر خم نکنیم و با مشت‌های گره کرده مقابل خصم تا آخرین قطره خون مبارزه کنیم.»
قالیباف اضافه کرد: «دیدن جای خالی رهبری برایمان جانکاه است، ولی دلگرم به مدیریت و رهبری جدید هستیم.»
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 298K · <a href="https://t.me/VahidOnline/75812" target="_blank">📅 15:57 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75810">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/RuuV-oIEYy1R75S9HETXcwV_wZET0YAhozDdC6_HVg80nSQySlVrFxU5xmkfsTi42tz9bvle5ojDS3RK23H8-tQVhdnrkWtIAA7Sitn7I4aM-qH-Wn3aC8k-Wk5CkINDQDqaDtkVkTrwg1M5Da6MpQhUJVypejSsNSAowSBg7qL_yQ73jXdIuoR3_lFSZoyklL3-KSsx_8Fh9ZcuMH2wsiMqoIfOQ08j0wcX3W1Vv0X1Ah5LnpZBzu52WRVVAs8qQvd6avP67R6abA4Nn336SoDa25xTmE8YK7TeZyJngwglsVXpsibSouVRpWOSxSC9C2bADPQE5FhIPNuksINTPQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/8e2c9e72d6.mp4?token=LBaXLkjkd9xHvBd6FiakOlMKxBPTzYOTpYwB293zD2asrfMIeBSZJ7DTBUF5YS3PQCxU0rYWsJesrMfhVLSwagtDKpxAJhZkBPZFQ9JmUU7KJWy4zwo8fLIXj58-_wLBOS91_Ej8eNn8Ya06p_qZRFkD57q97xGlm4Ynj73KFA2esPA5XWq83cgELIC13AEzIrvnpbHSsPimSSCQbesIj6X5jcW-xFxhb2Hpx8V6IgkMOY0xbcR41HfP4yVXhoYnx7zziXyf7QTSeqmabPtioCkuNM0k9BajspNHJCiEf_uUS4rl_GcbxFAdHM2qewlkqS4PyES7irFljCoRYhcMTw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/8e2c9e72d6.mp4?token=LBaXLkjkd9xHvBd6FiakOlMKxBPTzYOTpYwB293zD2asrfMIeBSZJ7DTBUF5YS3PQCxU0rYWsJesrMfhVLSwagtDKpxAJhZkBPZFQ9JmUU7KJWy4zwo8fLIXj58-_wLBOS91_Ej8eNn8Ya06p_qZRFkD57q97xGlm4Ynj73KFA2esPA5XWq83cgELIC13AEzIrvnpbHSsPimSSCQbesIj6X5jcW-xFxhb2Hpx8V6IgkMOY0xbcR41HfP4yVXhoYnx7zziXyf7QTSeqmabPtioCkuNM0k9BajspNHJCiEf_uUS4rl_GcbxFAdHM2qewlkqS4PyES7irFljCoRYhcMTw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نیروی انتظامی تهران کافه‌ای در خیابان ولیعصر را که در آن برنامه‌های موسیقی اجرا می‌شد، به بهانه آن چه «فعالیت‌های مروج فرقه‌های انحرافی» خواند، پلمب کرد.
مرکز اطلاع‌رسانی پلیس جمهوری اسلامی در اطلاعیه‌ای نوشت: «این کافه با برگزاری برنامه‌هایی با ظاهر موسیقی غربی، بستری برای حرکات نابهنجار، و آنچه که ماموران توصیف کرده‌اند "تحرکات شیطانی" فراهم آورده بود.»
نیروی انتظامی جمهوری اسلامی نام این کافه را ذکر نکرد اما ادعا کرد که «مشتریان این کافه، شامل دختران و پسران جوان، در وضعیتی غیرطبیعی و با حرکاتی عجیب و غریب، که از آن به عنوان “شیطانی” یاد شده، مشاهده گردیدند.»
پیشتر نیز بسیاری از کافه‌ها و اماکن کسب و کار به اتهام‌های مشابه پلمب شده‌ بودند اما جمهوری اسلامی سرکوب‌ شهروندان را از زمان اعتراضات دی‌ماه گذشته تاکنون شدت بیشتری داده است.
موج تازه اعدام‌ها، صدور احکام سنگین و بازداشت‌ها نگرانی فعالان و نهادهای حقوق بشری را برانگیخته است.
@
VahidHeadline
ویدیوی بالا رو هم به عنوان "تحرکات شیطانی" در اون کافه منتشر کردند!
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 359K · <a href="https://t.me/VahidOnline/75810" target="_blank">📅 15:52 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75809">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/D6vG-k9aYC3AJ-D4V9Wcgz1kdBaoGr5a2UXJZMbbTamvRWtv2WxS0YUpGDql_MnMw1M697Q-OLMiT-Z39fA83tV8SSIxgbJIDBeS5PEAbNJVEwrac0tKwOOV91logH5oVV2dHTmg8-BtPSAqhx1GIUrrkw-cBXFVfyu3Yw3m--Q72eRnMieQwga8Oq5anhbS6NlRU04BWMGUWt-Oe6SLYM50vbq-gDps9OwBidCSY1nhpHvoStcCEyktNQLoAvTRAwOgN7xuY2tjaCWvwZhMjgS8Wm5Jx0GMNnFS7YIZpCMNzvMmfmBO3dNuJF9uxwbjVCAKX9FKuiOLJhojHEcEwQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آکسیوس، ترجمه ماشین:
رئیس‌جمهور ترامپ در جلسه‌ای که روز جمعه در اتاق وضعیت برگزار شد، خواستار چند اصلاح در توافقی شد که فرستادگانش با همتایان ایرانی خود به آن رسیده بودند؛ این را یک مقام ارشد دولت و منبع دومی که در جریان موضوع قرار گرفته بود، گفته‌اند.
...
مقام‌های ایرانی به رسانه‌های دولتی گفتند که آن‌ها نیز متن نهایی را تأیید نکرده‌اند؛ هرچند دو مقام آمریکایی پیش‌تر در طول هفته مدعی شده بودند که تهران آماده امضاست و همه چیز به تصمیم ترامپ بستگی دارد.
به گفته این دو منبع، ترامپ از تیم خود خواست تغییراتی در پیش‌نویس مربوط به بندهای برنامه هسته‌ای ایران ایجاد کنند.
در شکل فعلی، این تفاهم‌نامه شامل تعهد ایران به دنبال نکردن سلاح هسته‌ای است، اما امتیاز مشخص دیگری فراتر از آن در آن نیامده است.
در این متن آمده است که یک بازه ۶۰ روزه برای مذاکره درباره تعهدات هسته‌ای ایران و کاهش تحریم‌ها از سوی آمریکا وجود خواهد داشت؛ نخستین موضوعات در دستور کار نیز چگونگی تعیین تکلیف ذخایر اورانیوم غنی‌شده ایران و محدود کردن غنی‌سازی بیشتر خواهد بود.
ترامپ می‌خواهد تلاش کند این بخش را اصلاح کند.
یک مقام ارشد دولت گفت: «موضوع، جزئیات بیشتر درباره این است که آمریکا چگونه مواد را دریافت می‌کند و زمان‌بندی آن چگونه خواهد بود»؛ منظور او اورانیوم غنی‌شده بود.
منبع دوم گفت ترامپ همچنین می‌خواهد برخی از عبارت‌ها درباره بازگشایی تنگه هرمز را اصلاح کند.
این مقام آمریکایی گفت به ترامپ گفته شده است حدود سه روز طول می‌کشد تا ایرانی‌ها با پاسخ برگردند. این مقام ارشد دولت گفت: «آن‌ها عملا در غارها هستند و از ایمیل استفاده نمی‌کنند.»
این مقام ارشد دولت گفت: «توافقی در کار خواهد بود. اینکه چقدر قریب‌الوقوع است، باید دید. ما حاضریم صبر کنیم تا رئیس‌جمهور آنچه را خواسته به دست بیاورد. ممکن است یک هفته طول بکشد. ممکن است کمتر باشد. ممکن است بیشتر باشد. امیدواریم در آغاز هفته چیزی داشته باشیم.»
axios
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 411K · <a href="https://t.me/VahidOnline/75809" target="_blank">📅 05:02 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75808">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tBkXx0NHQVncKx_92FXGJ3mxcPiSXnZzMgLEpl9llvgo2tXH9fCjqR6q5NQC0lMObXZPW3_iUzUBjuXp2HpZYybaKtpgVXtSHoQrCPRHDYcJqYprf_ZupJF4o3xNzk92QvDUdfi2-geU3rm4TK82LXZnFrNFFE_8ifMA8-qp4h2o7hZGdU1UkD1nv5MCfjhOwoQ48nXngxJee5q5PF4sgsTiKa1oIr4AyMAT7X_yQL1rDi2CJFcZalPqiosD2xSNHJaVGS8Ft_8DKVjpMLze08AUoA3foBAWQ3W500shHfqhSp6iZFHYm5Ns2QgIwXOActU4Hbl77RJhjn4rgTBrKg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">روابط‌عمومی سپاه بامداد یکشنبه، ۱۰ خردادماه، اعلام کرد یک پهپاد «ام‌کیو۱» (MQ1) ارتش آمریکا را منهدم کرده است.
خبرگزاری فارس نوشت: «این پهپاد با ورود به آب‌های سرزمینی ایران قصد انجام عملیات خصمانه داشت که بلافاصله در رصد و هدف موشک‌های پدافند سپاه قرار گرفت و سرنگون شد».
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 385K · <a href="https://t.me/VahidOnline/75808" target="_blank">📅 04:46 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75807">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/fDroVwo1mE0nWduoG7PaPsbst_V_FJOXjHw2veQ9yeaJRYeMukvsIvL7yCkHEVzZ5V1lCM_3EzVN3a_eYkgfFM_tZHXHDezD7xYgiEHZMpR9qNHAOZBYg0JoL_b0EXoZCTjso7Lji1zxS8_defY-eKcAKkWQJw1M_P5Eo5RJiAWYgLfEl50mgrEsmPgBcQKSZJaJUwL7JJZSMe6iHghXovPVdNVOi3vyxx1ZIfFLR24GCI0-LJzyhXCHC7uYYxUYILCG_a8Wv-R-OJhJDQzJtbQb3rTUy2u6FXmoGXo_5yjZFSvpc9Ttj94PTZdNWXGRZCK9kTgUJhsOJKXvvjMEUg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ستاد فرماندهی مرکزی ارتش آمریکا، سنتکام، اعلام کرد نیروهای این کشور یک کشتی تجاری با پرچم گامبیا را که به گفته واشینگتن در نقض محاصره دریایی به سمت یکی از بنادر ایران در حرکت بود، در خلیج عمان هدف قرار داده و از ادامه مسیر آن جلوگیری کرده‌اند.
سنتکام روز شنبه نهم خرداد در بیانیه‌ای گفت نیروهای آمریکایی روز هشتم خرداد کشتی «لیان استار» را هنگام حرکت در آب‌های بین‌المللی به سوی یکی از بنادر ایران شناسایی کردند و بیش از ۲۰ بار به خدمه آن هشدار دادند.
به گفته این نهاد نظامی، پس از آنکه خدمه کشتی به هشدارها توجه نکردند، یک هواپیمای آمریکایی با شلیک موشک هلفایر به اتاق موتور کشتی، آن را از کار انداخت.
سنتکام افزود این کشتی دیگر به سمت ایران در حرکت نیست.
در این بیانیه آمده است که از زمان اجرای محاصره دریایی علیه ایران، نیروهای آمریکایی پنج کشتی تجاری را از کار انداخته و ۱۱۶ کشتی دیگر را وادار به تغییر مسیر کرده‌اند.
سنتکام جزئیات بیشتری درباره محموله کشتی یا مقصد دقیق آن در ایران ارائه نکرده است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 413K · <a href="https://t.me/VahidOnline/75807" target="_blank">📅 21:52 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75806">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DhiJT3I6Nw0NhdVuo2-uxMpxLxKN4ZE8CKo5lchChs_ldQWTpZ7prbloHk7ojwOLDLKZQy6OUiXNkG4J263m3xXQiVwWe-s--TDYoFtYhXAvJTEWRTqGiNWokRKLjS69scQD3boPGXFM5REuD6A9DHR7rHcqbJiJBT8vVKcdmGeAtkxT1HOYPEsPpVmKSHuErvRVFhT6T_ED7lCXEDXhieX32nRUAFYJma0p_wXezTJFYIp8VHfOhF_N85yudZ7WaWdYF4XkjKNzvgytH2OCmH8extDOR14ictvCiqgS-XPWWwovnaQHkv4DrJwT5WN8GqUiS7Q7Cyiecb918Suxfg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">صداوسیمای جمهوری اسلامی در گزارشی درباره تفاهم احتمالی بین تهران و واشینگتن با عنوان «جزئیات غیررسمی»، اعلام کرد آمریکا متعهد شده در طول ۶۰ روز امکان دسترسی جمهوری اسلامی به ۱۲ میلیارد دلار از دارایی‌ها را به‌گونه‌ای فراهم کند که این منابع قابلیت انتقال و هزینه‌کرد در بانک‌های مقصد را بدون محدودیت داشته باشد.
این گزارش افزود که بر اساس این تفاهم، جمهوری اسلامی مرجع انحصاری تشخیص ماهیت شناورهای عبوری است و هر شناوری که محموله آن تهدیدآمیز شناخته شود یا بهره‌بردار نهایی آن در «خصومت» با جمهوری اسلامی باشد، به عنوان کشتی تجاری شناخته نشده و اجازه عبور از مسیرهای تعریف‌شده را ندارد.
صدا و سیما تاکید کرد که این رونوشت هنوز در حکم یک تفاهم غیررسمی است چون مسیر آن همچنان در چرخه بررسی، مذاکره و بازبینی قرار دارد.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 376K · <a href="https://t.me/VahidOnline/75806" target="_blank">📅 21:24 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75805">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nMiqXe13JyxaQeV74DSNp7kjYtBz9ot2gA4UVotKAzECpiCDJlQf0anq0oFWq5uQ7V7QZg7YcbajW1sZmb-5uCKGqVjN3WheRVizy5x7Arq52PCZHLCIjcCuuPKukKVmB2U5_GhQtup9Gl_7G6zmVK1oXEe05JCst9wBZxQXB6CAPYiNzd9gMsZpS7SC_s7g7_Yuf5BDmB0DLqwdf7tVlv-vn0WCrPY8xjDGARPgXxwhYYh48joCEDGOAiqQWBb6yHl4x-Nl4j8l1ZD_R8rYNFCO4-_uoshJTJRf9N48zPg2a_L1Z_v_LyKAKh-rE8IeYJ6Oc1sf759UpOGAe5ajpw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
به گزارش نیویورک‌پست، در پی حمله موشکی جمهوری اسلامی به یک پایگاه هوایی در کویت، چند نفر از نیروهای نظامی و پیمانکاران آمریکایی مجروح شدند. این حمله در حالی رخ می‌دهد که دونالد ترامپ، رئیس‌جمهوری آمریکا، در حال ارزیابی پذیرش آخرین پیشنهاد صلح تهران یا بازگشت به شرایط جنگی است.
یک منبع مطلع روز شنبه نهم خرداد، اعلام کرد که در پی رهگیری یک موشک «فاتح-۱۱۰» توسط پدافند هوایی کویت طی ۲۴ ساعت گذشته، قطعات و ترکش‌های ناشی از انهدام موشک بر فراز پایگاه هوایی «علی السالم» فرود آمده و منجر به جراحت سطحی چند آمریکایی شده است. این حادثه همچنین خسارت شدیدی به دو پهپاد «ام‌کیو-۹ ریپر» (MQ-9 Reaper) به ارزش تقریبی ۳۰ میلیون دلار وارد کرده است.
این حمله در شرایطی صورت گرفته که دونالد ترامپ روز جمعه با تیم امنیتی خود تشکیل جلسه داد و اعلام کرد که قصد دارد تصمیم نهایی را درباره توافق با ایران اتخاذ کند؛ توافقی که شامل تمدید ۶۰ روزه آتش‌بس، بازگشایی تنگه هرمز و آغاز مذاکرات بیشتر درباره مواد هسته‌ای ایران در ازای لغو محاصره دریایی آمریکا می‌شود.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 381K · <a href="https://t.me/VahidOnline/75805" target="_blank">📅 21:08 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75804">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/U_Xg2N0RWhiAC9ytk22ksW2JTiUMxf6l_m1spOMRDCrVq-LuTCNXH0l-a4FsO_-E-QP5bcuk7vy9hVT_Zx-2a0NcnXLwsvcL05HOs8g7h4_t4RHXKBUAOKvm-8s6-vZVRbG09u4jcV4QEtLukiDLZFK6xUIhluIpWeTG_6qveji0LWGIEEWZfrmNCOMXF6M7qIV4ydmRphtJvhaN5z16CYSIVIpM-uW1oKNxZJ28VtGj-awadPB2EKvLPblIV0RCHfCjUEpcLfAJBxQLW-QYsMpuLdBiAc8ujCHx2m_W7fWeiZeZ8ofVvumvlAGKcGdnh16JE8JaDX4y3KiK1cgDVA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قرارگاه مرکزی خاتم‌الانبیا در بیانیه‌ای اعلام کرد که هرگونه اقدام شناورهای نظامی جهت مداخله در مدیریت تنگه هرمز یا ایجاد اختلال در تردد، مورد هدف نیروهای مسلح جمهوری اسلامی قرار خواهد گرفت.
در این بیانیه آمده: «هرگونه تخلف از این ضوابط، امنیت تردد آن‌ها را با مخاطره جدی مواجه خواهد کرد.»
قرارگاه مرکزی خاتم‌الانبیا اعلام کرد کلیه کشتی‌ها، شناورهای تجاری و نفتکش‌ها صرفا ملزم به تردد از مسیرهای تعیین‌شده و اخذ مجوز از نیروی دریایی سپاه پاسداران هستند.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 362K · <a href="https://t.me/VahidOnline/75804" target="_blank">📅 19:02 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75803">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/83c715fa8b.mp4?token=IeKyrlMoapoqIWgi4QZyp3VQv_Fm2hJHdDiEwufOhuSwaCE7AJ2kdiP2CdY1-Qob-5hn45MCX5UaSqAl0gBlOnv1CkpaU2wFDJzx1TQx4jm3ik0vYDeGTzLUwvmpOT-BiHOMKB-kOwSk4RhChuNKFIpIWD079Nb7oD34EdG7i3CUCi9dW66saMWNAIL15pYmXhpNUuL_MgFmF4PSsZ-s9W_cX8F4frZSGnIKLZibNaeJKPmin8EfJzoFIomDdkfck32IAc0V4kOVxRK6TQltCtF2LpTXufbE1D-u0Zftbue9n99bKBnvPQ6iETiHaabJgWZixWoJvdLsVjNksQzrtw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/83c715fa8b.mp4?token=IeKyrlMoapoqIWgi4QZyp3VQv_Fm2hJHdDiEwufOhuSwaCE7AJ2kdiP2CdY1-Qob-5hn45MCX5UaSqAl0gBlOnv1CkpaU2wFDJzx1TQx4jm3ik0vYDeGTzLUwvmpOT-BiHOMKB-kOwSk4RhChuNKFIpIWD079Nb7oD34EdG7i3CUCi9dW66saMWNAIL15pYmXhpNUuL_MgFmF4PSsZ-s9W_cX8F4frZSGnIKLZibNaeJKPmin8EfJzoFIomDdkfck32IAc0V4kOVxRK6TQltCtF2LpTXufbE1D-u0Zftbue9n99bKBnvPQ6iETiHaabJgWZixWoJvdLsVjNksQzrtw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پیت هگست، وزیر دفاع آمریکا، روز شنبه نهم خرداد گفت ایالات متحده در صورتی که مذاکرات با ایران به توافق منجر نشود، آماده ازسرگیری حملات علیه جمهوری اسلامی است.
هگست در جمع خبرنگاران گفت: «در حال حاضر تمرکز ما بر حفظ آمادگی و آماده بودن برای بازگشت به عملیات است، اگر لازم باشد.»
او افزود دونالد ترامپ «صبور» است و به دنبال دستیابی به «توافقی خوب» است که تضمین کند ایران هرگز به سلاح هسته‌ای دست پیدا نخواهد کرد.
اظهارات وزیر دفاع آمریکا در حالی مطرح می‌شود که مذاکره‌کنندگان تهران و واشینگتن در تلاش‌اند اختلافات باقی‌مانده بر سر برنامه هسته‌ای ایران را برطرف کنند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 346K · <a href="https://t.me/VahidOnline/75803" target="_blank">📅 18:45 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75802">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/bh7cVd5nlDr5BVX0r6gtiTZCbXXMyjHFoBx15tIx7GA1IElD-s3ikeKw2rQ-thL3s_QTuoNkETrxJmARXTLxVBN-pl36na_CMnI3QMNyAFb3Gy3O8DSbPbdljSlFsepC1K_C1Cm_QSXoiVPGCHq2WPUiyByNXhy11kb-nCX3HRs8O-60-3-qNNI7I9q13iLqp2Bk8jI-xYS08s5-E3hV2pXLx3BEpunPbYXPJOT4L6NIET2D52r174YKxcFm-nnKZLKeu3EXTm0v2H_sQMXLy49lyy4WmNrsMMrZrJjheZiik9SUwh4BusEzUvqYyFp58X48xPXUCWYW5XZHgCKwvA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مصطفی نیلی، وکیل دادگستری، اعلام کرد شعبه اول دادگاه انقلاب شیراز بنیامین نقدی را با اتهام «افساد فی‌الارض» به اعدام محکوم کرده است.
نیلی در گفت‌وگو با امتداد گفت که بنیامین نقدی شامگاه ۱۳ دی‌ماه در شیراز به دلیل شعله‌ور کردن یک کپسول آتش‌نشانی به سمت ماموران نیروی انتظامی بازداشت شد.
به گفته این وکیل دادگستری، در ابتدا اتهام «شروع به قتل» به موکلش تفهیم شد، اما پس از آن اتهام وی به «محاربه» تغییر یافت.
او افزود پس از پایان تحقیقات مقدماتی، کیفرخواست بنیامین نقدی با اتهام‌های «محاربه»، «عضویت در گروه‌های برهم‌زننده امنیت کشور»، «اجتماع و تبانی به قصد ارتکاب جرم علیه امنیت کشور» و «فعالیت تبلیغی علیه نظام» صادر شد. به گفته نیلی، در خصوص اتهام‌های «ایراد صدمه جسمانی به ماموران» و «حمل سلاح سرد» قرار منع تعقیب صادر شده بود.
نیلی همچنین گفت قضات شعبه اول دادگاه انقلاب شیراز در جریان رسیدگی، مجموعه اتهام‌های مطرح‌شده را مصداق «افساد فی‌الارض» تشخیص داده و بر همین اساس حکم اعدام برای بنیامین نقدی صادر کرده‌اند.
وکیل بنیامین نقدی با اشاره به قصد خود و همکارانش برای اعتراض به این رای گفت که در مهلت قانونی درخواست فرجام‌خواهی خواهند کرد. او ابراز امیدواری کرد که با توجه به این که به گفته وی در جریان رخداد مورد اشاره هیچ فردی آسیب ندیده است و اقدامات موکلش مصداق افساد فی‌الارض نیست، حکم صادره در دیوان عالی کشور نقض شود.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 392K · <a href="https://t.me/VahidOnline/75802" target="_blank">📅 18:26 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75801">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromNima Akbarpour🔥نیما</strong></div>
<div class="tg-text">اینترنت در ایران آزاد و عادی نشده. بیشتر مسیرهای خارجی یا بسته‌اند یا نیمه‌بازند. فقط بعضی مقاصد و مسیرهای خاص اجازه عبور دارند. همین باعث شده فیلترشکن‌های معمولی خوب کار نکنند.
در این میون بعضی از افرادی که دامنه‌ها و مسیرهای سفیدشده دارند، دسترسی می‌فروشند. نتیجه‌اش هم شده اینترنت نابرابر، رانتی و پر از راه‌حل‌های موقت.
انگاری که درِ ساختمون رو کمی باز گذاشته باشن که هوا بیاد، اما اجازه ندن کسی ازش رد بشه.
برای همینه که گوشی‌تون ممکنه نشون بده که اینترنت دارید، حتی شاید اولش سایت یا اپ مورد نظر رو باز کنه یا بهش واکنش نشون بده، اما در عمل از اینترنت خبری نیست.</div>
<div class="tg-footer">👁️ 390K · <a href="https://t.me/VahidOnline/75801" target="_blank">📅 18:01 · 09 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>

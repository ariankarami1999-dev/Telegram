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
<img src="https://cdn1.telesco.pe/file/MuCKw3Rg8hbO_j7S8WTBlZdllqb4iyoD2IFG19pKYo1kM6SicdewFXCXACVLXZRmgMjVf0xfMUjxGaQlx2CpPaglrVLmY1FnVGMy1aGyRsqpC_NmsPqBWQWKqh_WqN57g5S8NFkX4HSceWy1x0qXK3bOmqzMek8AIMelPpkZL8JTcQB9Te2ZQq10I0dg9mSalJY0nDNW-Dpm9DPVqyLcFC8pqY2R-_FIrELx9CtCB3c9I-asQhWN6rOM0pKePDtO9XE24EBuSYKbc3DgVpMhbRKIrxRHN-5Y3U5gfSzGDZLmwgtPKC4y1TAFSjAiRJURgOCfWKaGx86MaZK1Y6rHvQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Vahid Online وحید آنلاین</h1>
<p>@VahidOnline • 👥 1.36M عضو</p>
<a href="https://t.me/VahidOnline" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ارسال پیام:@Vahid_Onlineinstagram.com/vahidonlineتلاش می‌کنم بدونم چه خبره و چی میگن. اینجا بعضی ازچیزهایی که می‌خواستم ببینم رو همونجوری که می‌خواستم بهم نشون داده بشه می‌گذارم.استوار بر حمایت‌های مردمی:ماهانهvhdo.nl/patreonیک‌بارهvhdo.nl/paypal</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-28 23:42:23</div>
<hr>

<div class="tg-post" id="msg-76496">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nV06vF0_fspZIE0iFE7yQCK3k9AmedtKmOQz2Ce2es-78wzgjDuG2gA4nBOrsyNuTMslnlBqvhmMuvrl4k-lpUrJIu0qDdaKbWApa0KCH25FCmS4sUTf204qrVy7uBSt8DAzWzYhueZ2hURr3bHxiEgoHWkoNDETc-lqYHdLlakIQ0cUH2ueqcAyPDXbXhWd5rIufPCMr30uMg5g7ooMYplmsRbfY0u4k_5LlDWusRtLuC4NVh5GPyefuPtQjbtURxS8CnfCL-YpVNU29LYkmVvYjN5nhS057sIFv4lBIhoC9YxO0HGMEASjGXDuM4N1fdM1bgsrrY8Q3Kk0JDB0RA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">المیادین به نقل از یک منبع آگاه گزارش داد هیات مذاکره‌کننده جمهوری اسلامی به دلیل ادامه حملات اسرائیل به جنوب لبنان، سفر خود به سوئیس برای آغاز نخستین دور مذاکرات ۶۰ روزه را به حالت تعلیق درآورده است.
المیادین افزود: تهران پیش‌تر به آمریکا و میانجی‌ها اطلاع داده بود که پرونده لبنان در ادامه یا توقف مذاکرات نقشی محوری دارد و هشدار داده است حملات اسرائیل تا عمق ۱۰ کیلومتری خاک لبنان نقض یادداشت تفاهم و توافق چارچوب است.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 76.2K · <a href="https://t.me/VahidOnline/76496" target="_blank">📅 23:10 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76495">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/kc3Y5QakLwdyxaC-Aui6mAO6HPgUp8IosqP4XGC-Ld6pNaGhKcCksSs7R9d1LsTNqL1baVJ1eNSzQEJ19hd3USRa2N1gpgN13gq7xquS3UHd1qbiVDLQQGzUbgZDr44VnVH0KdlMUpwf6GIlMlLzgl7QGuh5yXvxPxgW-dHDO-4mdO84JUUwCzvEkZhrkkdkjvaBWTDCtFLG04w169nMclyFAqBa4zFpmbUHbs4eHjdR66YRNDqNPflea3x0WDWKs9U10fwGYkOUXmNp1j-qDVG0SUB2_9tvNTBOrjo3R7jVTnlM5SMopmzadjgNxgnks7bXxVku92pu9Wr1RYWUVA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">توییت کاخ سفید:
رئیس‌جمهور دونالد ج. ترامپ تهدیدی را حل کرد که واشنگتن چهل سال صرف مدیریت آن کرده بود: ایران هرگز سلاح هسته‌ای نخواهد داشت.
یک پیروزی برای آمریکا.
🇺🇸
WhiteHouse
ترجمه با هوش مصنوعی به تصویر اضافه شده.
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 106K · <a href="https://t.me/VahidOnline/76495" target="_blank">📅 22:49 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76494">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/B2y3Ij6sxjDixVR6sTfQ0mdn-FpPtvcRy315hJhMbM2uyW2NBqt9XOwzS-9otLPKbhEqamttk3eANdrikbZwqr8iGiPLLpWsqmpzY-5GsM6sMG5cn1DiBC1C5llAIZSQlaqJEbyD3EzmQ8ErnrWzG9cBEydgvXUutZfCH5SZWdRTp2ChHCuA8KQDHzd6LX1CdN_x4WpH8sdGY0utwIONPolio6AddacA0DqVqu4Gs49PRlFY21fI3Wr8ex3BxD-EIgqzQizuXNKgFUE_sFZabft2182dWa_rzfVObVPBdTipqSta7EJ7iM5Rd7Q0ksB_NKbi0FlTkyN4wlWSS-UwMg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">'
بیانیه شورای عالی امنیت ملی
'
منابع حکومتی:
🔹
در اجرای بند ۵ یادداشت تفاهم اسلام‌آباد، کشتی‌های تجاری متقاضی عبور از تنگه هرمز باید درخواست خود را به مدیریت آبراه خلیج فارس (PGSA .ir) ارسال نمایند.
🔹
به موجب یادداشت تفاهم اسلام‌آباد، به مدت شصت روز، هیچ‌گونه هزینه‌ای از متقاضیان اخذ نخواهد شد و این هزینه‌ها توسط دولت جمهوری اسلامی ایران تأمین می‌گردد.
🔹
بر این اساس به مدیریت آبراه خلیج فارس دستور داده شده است، در جهت تحقق اهداف تفاهم‌نامه درخواست‌ها را با سرعت و اولویت رسیدگی و پاسخ دهد.
🔹
با توجه به شرایط خاص و وجود برخی مخاطرات ایمنی در مسیر عبور و به دلیل لزوم حصول اطمینان از تردد ایمن و جلوگیری از حوادث دریایی، لازم است کشتی‌ها در مسیر و زمان اعلامی به آنها عبور نمایند تا به تدریج، امکان تردد افزایش یابد.
🔹
ترتیبات اجرایی و جزییات فنی عبور از تنگه هرمز از طریق مدیریت آبراه خلیج فارس اعلام می‌گردد.
🔹
در خصوص سایر موضوعات، از جمله مین‌زدایی، اقدامات لازم مطابق بند ۵ یادداشت تفاهم اسلام‌آباد انجام خواهد شد.
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 128K · <a href="https://t.me/VahidOnline/76494" target="_blank">📅 22:31 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76493">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/cZPTXDRa-op4XQWhoAo-aSzbtnM5rY2wAKnfB6zROMH6hAymg1ijkzkK6mn8acJC9U4dy6efqAOfB2pktjTaypZV1VF0Yaz1_TBNxVrNPivHe_WVeFxyefqIBNTkzUKH4k3knK3j_tIxN9KgciDGQX-xT8ummJaQRxkObHYbj5IpPy3V7MHKKo_fQoNAy28M8QBH25rgtrX9ZTmC9P1IbakqU7LqFHSH1GlLFQZG-RnT-MVH0H_qFiUTv4cA5jBar1YlqcmPqJu4w8Hpg1jR1V_U0uCiIDc2BizbueJ90x5WfUMJPX584Hcg3qjuv0RwuOjlrbodUIHsoLz0hQ4lbw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ: انتظار آتش‌بس کامل در همه جبهه‌ها از جمله لبنان را دارم
ترجمه ماشین:
ایالات متحده به صلح متعهد است و ما همه در منطقه خاورمیانه را تشویق می‌کنیم که به تعهد خود برای فراهم کردن امکان پیشرفت زیبای مذاکرات ما پایبند بمانند.
بازارها از آنچه در حال رخ دادن است استقبال می‌کنند: قیمت نفت به‌شدت پایین آمده و سهام به‌شدت بالا رفته است.
ما انتظار آتش‌بس کامل در همه جبهه‌ها، از جمله لبنان، حزب‌الله و اسرائیل را داریم.
از توجه شما به این موضوع سپاسگزارم!
رئیس‌جمهور دونالد ج. ترامپ
realDonaldTrump
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 120K · <a href="https://t.me/VahidOnline/76493" target="_blank">📅 22:30 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76492">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromPourostad وحید پوراستاد🔷(Vahid Pourostad)</strong></div>
<div class="tg-text">« پیام منتسب به مجتبی خامنه‌ای در واقع نوعی فاصله‌گذاری حساب‌شده با تفاهم ایران و آمریکا است. مجتبی خامنه‌ای رهبر جمهوری اسلامی اجازه امضا را داده، اما مسئولیت سیاسی و اجرایی آن را بر دوش پزشکیان و شورای عالی امنیت ملی گذاشته است.
پیام همزمان رو به داخل و بیرون نوشته شده است. در داخل می‌گوید رهبر با رضایت کامل وارد این مسیر نشده و دولت باید پاسخگوی نتیجه باشد. در برابر آمریکا هم این سیگنال را می‌فرستد که تفاهم، زیر فشار ترامپ و دولت او به‌معنای عقب‌نشینی قطعی نیست؛ بلکه مشروط است و اگر شروط ایران محقق نشود، موافقت نهایی رهبر با توافق نهایی هم تضمین‌شده نخواهد بود.
در واقع متن، بیش از آن‌که اعلام رضایت از توافق باشد، تلاشی برای حفظ دست بالا در مرحله بعدی است: هم مسیر مذاکره باز می‌گذارد، هم امکان عقب‌نشینی تبلیغاتی حفظ می‌شود, هم به واشینگتن گفته می‌شود که فشار بیشتر ضرورتا به انعطاف بیشتر ایران منجر نخواهد شد»
@pourostadv</div>
<div class="tg-footer">👁️ 134K · <a href="https://t.me/VahidOnline/76492" target="_blank">📅 22:19 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76491">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/qLbL4cGf8ud8Z9sRjh8Iaqq_PA18YetVJy2iPpvpUwL3ntXeAWRIqlQX0I09SDLZcdUiXsOxkx52QcHFnAOLhpdT-rMt8oySBA_2S5AzKM4XnwfnBOCDIPpXgTpP73iK1D-6T0SME0x1VKbyy_p3z7lQkPe6msqKiwvGe7-xLGB1L8mLuWc6oFrhQGApvIlXpZLMYhIHWxG7ocZ4f2_e0iK22fS-3sJoSXjheBspGGWDh39zSw8gB83iqHAAUuXk1-qq_wG3fmzGHj7Spa8On8eEk6aRUwZ3MCPlg0l4e9S6LFIp4Q5GqxQedDusqsXMB2FrTznrD9tui-BOoBwewQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مسئول
گردن‌نگیر
جوان شد
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 206K · <a href="https://t.me/VahidOnline/76491" target="_blank">📅 21:19 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76490">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/bQsdIvwu7tUDNcLQbBw6OeUy3mGwrS0c8c6q-cuG14QL3yRfcI84z4j5Xtnv4tu8hLm06a3axymeLExsUjFeFo-IBhzy8y0P-vCxVoSuJr5MvhSgFZv8eNcHDfm3EP9WpPhRKKYUdbss_ATA-R1QYvflCataX1OMW0G3fTM6SIYGBwJnePLWNfJwoljXhZAGnC64k_2MERA-GYlNXLnuNjbcUHZo9-78qheSICyud03Ll3HaPoDxGLeWgJ7v2VcZ0W4JbN8MYopnBIJR1eVJIuWcui403onjpJnT0-41PhjHAdHsUn3uwnxfRYA_PjyceDa2kdaullmWCO5ipAeOTA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رسانه‌های ایران پنج‌شنبه شب متن پیام مکتوبی منسوب به مجتبی خامنه‌ای را منتشر کردند که در آن رهبر جمهوری اسلامی درباره امضای تفاهم‌نامه میان ایران و آمریکا گفته است که «نظر دیگری» داشته و مسئولیت آن را بر عهده مسعود پزشکیان، رئیس شورای عالی امنیت ملی، و دیگر اعضای این شورا دانسته است.
در این پیام درباره توافق با ایالات متحده آمده است:
«بنده علی‌الاصول، نظر دیگری داشتم ولی از باب تعهدی که رئیس‌جمهور محترم به‌عنوان رئیس شورای عالی امنیت ملی از طرف خود و سایر اعضا در پاسداشت حقوق ملت ایران و جبهه مقاومت به بنده دادند و تصریح به قبول مسئولیت آن نمودند، اجازه آن را صادر نمودم‌.»
در این پیام به تفاهمنامه اخیر به عنوان «تفاهم‌نامه‌ای بین رئیس‌جمهوران ایران و آمریکا» اشاره و گفته شده است که رهبر جمهوری اسلامی و مردم از این لحظه «منتظر تحقق شروط گفته ‌شده» خواهند بود.
در این پیام آمده که مذاکرات حضوری آینده «به معنی پذیرش نظر دشمن نخواهد بود.»
VahidOOnLine
در تیتر و متن نامه و خبرهایی که درباره‌اش تولید میشه بسیار تاکید دارند که این تفاهم‌نامه‌ای بین پزشکیان و ترامپه و نمی‌گن بین ایران و آمریکا
در واکنش‌ها از تقلیل نقش
قالیباف
یا محافظت ازش با سپر کردن پزشکیان هم میگن.
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 204K · <a href="https://t.me/VahidOnline/76490" target="_blank">📅 21:14 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76489">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Zmwr4MxxcrS4mqzb9oqtxO25wr4LDqRFadDYKWybjfjRwYDo4djGCZ4YWq0pPR5WHI3kQAxJFncYT1p9hFx-mQqXUM0AYbSmL0yGJiBkWQx0hNT9t9MGXKKCF57VuQQtWiEI22fqVmTNTuCK7IV65ioFSWGxXyhzVQnTu0yjFACaAuCeE70U-OxYxxPJYjmkkmMYxS-4fJsZ8Z_NunNGepvq4AAAmdBZn8cquG6aZBaHQlioQZcKfTIFRMwegOyH3x8-gNwICBMevFcgm5bT-a3NGBWrKUxe-2s9o_2uw3C6j4kuZqT6NgfqZ7LGXuqcgyXJidWqOfX2IgJDsNBXUA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پست ترامپ، ترجمه ماشین:
هیچ پرداخت ۳۰۰ میلیارد دلاری از سوی آمریکا به ایران در کار نیست.
این خبر جعلی است!
تنها چیزی که نصیب آمریکا شده، موفقیت، کاهش قیمت نفت و پیروزی است.
بازار سهام را ببینید.
تبلیغات «دُمکرات‌ها» در جریان است!!!
رئیس‌جمهور دی‌جی‌تی
(توضیح: Dumocrat بازی زبانی تحقیرآمیز با Democrat است؛ از ترکیب ضمنیِ dumb به معنی «احمق» و Democrat. در ترجمه می‌شود چیزی مثل «دُمکرات‌ها» یا «دموکرات‌های احمق» آورد، بسته به لحن مورد نظر.)
realDonaldTrump
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 196K · <a href="https://t.me/VahidOnline/76489" target="_blank">📅 20:45 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76488">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/FXQi0cAoN9P5qGyxXbH5gUw98SZqooVGtFb6rSMCngNBPrXtCpWJympTzFeBBWo9sGu0LTLRjCtKz2OoGOwAVzddP3beXy0CxQtUtOHarhA8z54d4fzA8ByeZKA7j-YsK17hiKJD_L1cEomHjwTjNPXB9kku4LJb5GYuWdd_t054bPvc5Pf3kGtlPy_mdm4ZopXmjDQfJAiYz91S4t9JVPdg32A76-05UQYuck3jUduMXcvcU0opQ3Ur-JDl6yqWYkcvbFeXPQ7VluSozMyaH6iIJZUXWjys2lrU5DIF8r2TjOUFT5D2tkiYLEB-ArAhwGi7TVOeQyRh-T3Lo5DdYQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اعلام پایان محاصره دریایی
پست سنتکام، فرماندهی مرکزی ایالات متحده، ترجمه ماشین:
امروز، نیروهای آمریکا مطابق دستور رئیس‌جمهور، محاصره‌ی همه‌ی رفت‌وآمدهای دریایی به مقصد بنادر و مناطق ساحلی ایران و از مبدأ آن‌ها را رفع کردند.
نیروهای آمریکایی مانع عبور کشتی‌ها به سوی بنادر ایران در خلیج فارس و خلیج عمان، یا خروج از آن‌ها، نمی‌شوند.
همه‌ی تلاش‌های نظامی آمریکا برای اجرای محاصره متوقف شده است.
کشتی‌های بزرگ نیروی دریایی ما در منطقه‌ی کلی باقی خواهند ماند تا اطمینان حاصل شود که همه‌ی جنبه‌های توافق رعایت، اجرا و به‌طور کامل لازم‌الاجرا و مؤثر باقی می‌ماند.
CENTCOM
البته سنتکام ننوشته خلیج «فارس»
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 196K · <a href="https://t.me/VahidOnline/76488" target="_blank">📅 20:30 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76487">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/IGYJ2KETS3MZAE8iCSwt6rBifT62XhA_JRaqNqVP4ZHx2uiWrdYdMyy4_vzMUfqT3R7TEoVYdgG0_hm2NT7LmkeU-q0R9D1cviPHL_4Tjz-OHS6FiGCIkzVG_0oKnq8xwepM4UWG9UIr-DxI-qzMkIX5SmzkYOAeoTJZSaj9f7hUXI1hQXLTm46pHs3EjbSel0Sr-orvAkXJEVaCWC6DZUFp5TZsMBcP3oF3GmX-vy2OcdJcSG5oqKBT18qB87fIdBenT2fHD86ScIDyI1_imUrv5RtdwQZMviuXWuUbU0-B82VN2CBwyZIvehUbch_x48jBAnGnOjnJGiLSJOY-qQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این توییت ۹ سال پیش ترامپ داره توجه می‌گیره: ایران به آخر خط رسیده بود و آماده فروپاشی بود، تا این‌که آمریکا از راه رسید  و در قالب «توافق ایران» به آن یک طناب نجات داد: ۱۵۰ میلیارد دلار. realDonaldTrump
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 183K · <a href="https://t.me/VahidOnline/76487" target="_blank">📅 20:13 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76485">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/90d4e8375c.mp4?token=rDi-vv67BZO_LOkaO7lD3Irtd1Red8pQ2WSzxW9yJrS8DgZH0RX5OQaIRqVedY8lbs8A1lJ8sxf7dPDvSC0qVUQPdxJvfi2f7o-MdT-VqRKAWAozkVo2TefmlUJT_xWp4YcpOjU1dkiNUQuNjyXdj3nnhGdC2K9eKYsriZEvbPeclnWgQTh6oufG2UZm4LxbhmJhQxQ8sQ12NSyQ5GXaLzc9Z73hUdlecGIdN-7np9muFay1-UFuSTzzUWkr7p-y4G01LTuJxewiLaby-rAvKlqEHvZnipwLUm7G4jFW0i90YygBK4WiPA2uC2wu6WrFBYuXCmphId3S7C2FQ8T3EA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/90d4e8375c.mp4?token=rDi-vv67BZO_LOkaO7lD3Irtd1Red8pQ2WSzxW9yJrS8DgZH0RX5OQaIRqVedY8lbs8A1lJ8sxf7dPDvSC0qVUQPdxJvfi2f7o-MdT-VqRKAWAozkVo2TefmlUJT_xWp4YcpOjU1dkiNUQuNjyXdj3nnhGdC2K9eKYsriZEvbPeclnWgQTh6oufG2UZm4LxbhmJhQxQ8sQ12NSyQ5GXaLzc9Z73hUdlecGIdN-7np9muFay1-UFuSTzzUWkr7p-y4G01LTuJxewiLaby-rAvKlqEHvZnipwLUm7G4jFW0i90YygBK4WiPA2uC2wu6WrFBYuXCmphId3S7C2FQ8T3EA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">محمدباقر قالیباف، رئیس مجلس شورای اسلامی در ایران که ریاست هیئت مذاکره‌کننده ایرانی با نمایندگان آمریکا را برعهده داشت، عصر چهارشنبه در مصاحبه‌ای مفصل با تلویزیون حکومتی در ایران به نهایی شدن تفاهمنامه میان تهران و واشنگتن واکنش نشان داد و آن را موفقیتی بسیار بزرگتر از مقابله نظامی با ایالات متحده دانست.
او در مورد دستاوردهای ایران گفت: «هر آنچه را که با اقدام نظامی می‌خواستیم به دست بیاوریم، چندین برابر آن را از طریق مذاکره گرفتیم؛ اصلا قابل قیاس نبود. هر جنگی ممکن است پیروزی‌هایی داشته باشد، اما اگر این پیروزی‌ها در نهایت به یک سند حقوقی و سیاسی منجر و ثبت نشود، هیچ منفعتی نخواهد داشت.»
او در بخشی از صحبت‌های خود درباره انتقام کشته شدن علی خامنه‌ای گفت: «همان‌طور که خونخواهی امام حسین، ظهور امام زمان است، خونخواهی رهبر شهید هم آزادی قدس است... صد نتانیاهو بند کفش امام شهید ما هم نمی‌شود.»
قالیباف در مورد وضعیت تنگه هرمز هم گفت: «تنگه هرمز هرگز به شرایط قبل بازنخواهد گشت. البته این به آن معنا نیست که ما در تنگه هرمز بخواهیم برخلاف قوانین بین‌المللی و مقررات دریانوردی عمل کنیم.»
@
VahidHeadline
قالیباف در مصاحبه‌ای که همزمان با انتشار مفاد تفاهم‌نامه تهران و واشنگتن از صداوسیما پخش شد، گفت برای حضور در مذاکرات با دولت دونالد ترامپ تمایلی نداشت و به دلیل نقش ترامپ در کشتن قاسم سلیمانی، «کراهت شدید» برای ورود به این روند احساس می‌کرد. او افزود که با وجود این مخالفت شخصی، به درخواست مقام‌های جمهوری اسلامی مسئولیت مذاکرات را پذیرفت.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 184K · <a href="https://t.me/VahidOnline/76485" target="_blank">📅 20:05 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76484">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/v0wmglo2wLqA2xkIeBQfABGkM2sDPp5vilcv0Cdtx1qzqnfOstFEGsKMPpZxbX_TQxnkVDrnb5AGec2HWsEZqk-LsfM1f8PFskl5iYYTNjUtHk96Rq7NMUVtUJ0n-Lkc7kf-tGFB-6FnvWPTsxhHv_Tn4ga6DJJQZpHpr_0VbPc_OcSEEba9DYbmLU9ere_hVji5iEz_1IK1OVxIPrpL7bwafvTsPN_EOKzD-nwM7VbzysCbNE25E8_xOWOjnbU-u1mJ1_QD76jsAo17eG_IydG4mli7F5qCWgmZI1fCxZzjU46v3e1q0UipaoacMHUaRYEC6y1CsIBrJ7jJmLC9uA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بنیامین نتانیاهو، نخست‌وزیر اسرائیل، یک روز بعد از امضای تفاهم‌نامه ایران و آمریکا در نخستین موضع‌گیری خود اعلام کرد که نیروهای اسرائیلی از جنوب لبنان عقب‌نشینی نخواهند کرد و تا هر زمان که لازم باشد منطقه حائل امنیتی خود را در آنجا حفظ خواهند کرد.
این اظهارات پس از آن مطرح شد که دونالد ترامپ، رئیس‌جمهور آمریکا، طی روزهای اخیر از عملیات اسرائیل علیه حزب‌الله لبنان انتقاد کرد و آن را بیش از حد «تهاجمی» دانست.
نتانیاهو در یک مراسم رسمی گفت: «ما امنیت و رونق را به شهرهای شمالی بازخواهیم گرداند.»
او افزود: «این امر مستلزم حفظ منطقه امنیتی در جنوب لبنان است؛ مستلزم آن است که آنجا را ترک نکنیم، تا زمانی که نیازهای امنیتی اسرائیل چنین ایجاب کند.»
رسانه‌های رسمی لبنان پیش‌تر گفتند که در حملات صبح پنجشنبه ارتش اسرائیل به جنوب لبنان، ساعاتی بعد از امضای تفاهم ایران و آمریکا، سه نفر کشته شدند.
از سوی دیگر، یک مقام ارشد اسرائیلی پنجشنبه به خبرگزاری رویترز گفت که اسرائیل «در حال انجام مذاکراتی سرسختانه» با ایالات متحده دربارهٔ موضوع ادامه استقرار نیروهای اسرائیلی در جنوب لبنان است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 194K · <a href="https://t.me/VahidOnline/76484" target="_blank">📅 19:10 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76483">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">شروع سخنرانی جی‌دی ونس، معاون رئیس‌جمهور آمریکا:
🔸
دیشب، ۱۲.۵ میلیون بشکه نفت از تنگه هرمز عبور کرد.
این بالاترین میزان از آغاز درگیری است.
🔸
ایرانی‌ها برای دومین شب متوالی به هیچ کشتی‌ای در تنگه هرمز شلیک نکردند. تا این لحظه، آنها به تعهد خود پایبند بوده‌اند.
سنتکام اجازه داده است که دوازده کشتی از محاصره دریایی ما عبور کنند، بنابراین ما نیز به تعهد خود عمل می‌کنیم.
🔸
شما چیزهایی درباره ۳۰۰ میلیارد دلار یا ۲۴ میلیارد دلار، یا این یا آن عدد یا مقدار پول خواهید شنید، و واقعیت ساده این است که تنها راهی که ایرانی‌ها به هیچ یک از این منابع دست پیدا کنند — حتی یک سنت، به هر حال، از ایالات متحده آمریکا تحت هیچ شرایطی — اما
تنها راهی که آن‌ها می‌توانند از این معامله بهره‌مند شوند این است که کاملاً مطیع باشند و رفتار خود را تغییر دهند.
اگر ایرانی‌ها رفتار خود را تغییر ندهند، برنامه نظامی و هسته‌ای آن‌ها همچنان نابود خواهد شد؛ اگر رفتار خود را تغییر دهند، آنگاه رابطه‌ای تحول‌آفرین با خاورمیانه خواهند داشت.
این یک برد-برد برای ماست.
🔸
در ایران تقسیمات واقعی وجود دارد.
آنچه دیده‌ایم این است که عمل‌گرایان در حال پیروزی در بحث هستند.
🔸
من کسانی را دیده‌ام که به این توافق شک دارند — افرادی می‌گویند ایرانی‌ها هرگز رفتار خود را تغییر نخواهند داد.
خب، شاید این درست باشد، و اگر چنین باشد، آن‌ها هیچ‌کدام از مزایای این معامله را به دست نمی‌آورند. اما آیا ارزش امتحان کردن ندارد؟
🔸
می‌گویم دوره ۶۰ روزه رسماً امروز شروع شده است.
پس بله، توافق دیروز شروع شد — ما امروز ساعت ۶۰ روزه را شروع خواهیم کرد.
🔸
تمام چیزی که رئیس‌جمهور دیروز گفت این است که، البته، کشورها حق دفاع از خود را کنار نمی‌گذارند.
اسرائیل حق دفاع از خود را کنار نمی‌گذارد اگر حزب‌الله به اسرائیل راکت یا پهپاد شلیک کند.
ایرانی‌ها حق دفاع از خود در کشورشان را کنار نمی‌گذارند، اما
ما انتظار داریم که به عنوان بخشی از توافق نهایی، آن‌ها نتوانند موشک‌هایی بسازند که بتواند به طور گسترده کل جهان را تهدید کند،
و این همان چیزی است که رئیس‌جمهور ایالات متحده دیروز گفت. و ببینید، خیلی ساده است: نمی‌توانید به کشوری — چه اسرائیل، چه ایران — بگویید که حق دفاع از خود را نداشته باشد.
🔸
خبرنگار: رئیس‌جمهور ترامپ دیروز گفت که اگر مذاکرات این دور به مشکل بخورد، شما را مقصر خواهد دانست. آیا نگرانید که او شما را به عنوان مقصر معرفی کند؟
جی‌دی ونس: نه، اصلاً. فکر می‌کنم رئیس‌جمهور شوخی می‌کرد، همان‌طور که اغلب این کار را می‌کند.
🔸
جی‌دی ونس درباره تنگه هرمز:
ما هرگز نمی‌خواهیم این اتفاق دوباره بیفتد، درست است؟ این موضوع مربوط به عوارض نیست.
این درباره اطمینان از این است که تنگه‌ها هرگز به عنوان نقطه گلوگاهی برای اقتصاد جهانی استفاده نشوند.
صادقانه بگویم، این چیزی نیست که ایرانی‌ها بخواهند.
🔸
جی‌دی ونس درباره برداشتن تحریم‌ها:
صادقانه بگویم، ما این را به عنوان امتیاز بزرگی به ایرانی‌ها نمی‌دیدیم — ایران... این را به عنوان امتیاز به آن‌ها نمی‌دید، چون چیزی که مانع فروش نفت آن‌ها می‌شد تحریم‌ها نبود.
آن‌ها بدون هیچ تخفیفی مقدار زیادی نفت می‌فروختند، چون تحریم‌ها اساساً بی‌اثر بودند.
در آن زمان، کاری که تحریم‌ها انجام دادند این بود که سیستم مالی ایران را به نوعی به سیستم بانکداری سایه‌ای منتقل کردند.
با برداشتن تحریم‌ها، ما در واقع قادر خواهیم بود کمی ببینیم که سیستم مالی آن‌ها پول را کجا می‌فرستد و از کجا دریافت می‌کند. این یک مزیت واقعی است.
🔸
آنچه به برخی از منتقدان توافق که شنیده‌ام می‌گویم، کسانی که می‌گویند «خب، ایران تمام این مزایا را به دست خواهد آورد».
تکرار می‌کنم آنچه را که گفته‌ام و احتمالاً باید چندین بار تکرار کنم: مزیتی که ایرانی‌ها به دست می‌آورند و قبلاً نداشتند چیست؟ و پاسخ هیچ است.
آنها هیچ چیزی به دست نمی‌آورند مگر اینکه رفتار خود را تغییر دهند. اگر رفتارشان را تغییر دهند، این چیزی است که باید جشن گرفت.
🔸
هیچ‌کس نمی‌تواند حق دفاع از خود یک کشور دیگر را نادیده بگیرد — اسرائیل حق دارد از خود دفاع کند.
اما اساساً، اسرائیلی‌ها، درست مانند همه‌ی مردم دیگر، باید به این روند صلح که اساساً برای آن‌ها و کل منطقه مفید است، احترام بگذارند.
🔸
در انتقاد از اسرائیل: به نظر می‌رسد که ما درست در آستانه یک پیشرفت بزرگ در توافق هستیم، و ناگهان یک انفجار بزرگ در یک مرکز جمعیتی غیرنظامی در بیروت رخ می‌دهد و بسیاری از افرادی که هیچ ارتباطی با حزب‌الله ندارند جان خود را از دست می‌دهند. این قابل قبول نیست.
🔸
توافق هسته‌ای اوباما اجازه غنی‌سازی داد — توافق ما این اجازه را نمی‌دهد.
توافق اوباما اجازه انباشت مواد با درجه تسلیحاتی را داد؛ توافق ما در واقع به نابودی آن انبار مواد غنی‌شده منجر می‌شود.
توافق اوباما بیش از یک میلیارد دلار پول آمریکایی به آنها داد؛ این توافق هیچ دلار پول آمریکایی به آنها نمی‌دهد.
🔸
آنها تعهدات هسته‌ای بسیار مشخصی داده‌اند.
آنها متعهد به نابودی ذخیره بسیار غنی‌شده‌ای شده‌اند که در اختیار دارند.
اما نکته دوم، تنها کاری که ما انجام داده‌ایم برداشتن محاصره در تنگه است — که اساساً آن را به وضعیتی که قبل از درگیری بود بازمی‌گرداند.
🔸
خانم‌ها و آقایان، کلمات مهم نیستند، ما درباره تأیید صحت صحبت می‌کنیم.
🔸
فرض کنیم — دو سال بعد، آن‌ها آنچه را که ما باید در برنامه هسته‌ای ببینیم انجام داده‌اند و تحریم‌ها را طبق توافق آزاد می‌کنیم.
سپس تصمیم می‌گیرند که برنامه هسته‌ای را دوباره بسازند.
البته در این صورت، آن تحریم‌ها دوباره باز خواهند گشت.
و به همین دلیل است که این موضوع واقعاً شبیه یک دکمه تنظیم است: هرچه رفتار خوبشان را افزایش دهند، ما می‌توانیم تسهیلات اقتصادی را افزایش دهیم؛ اگر رفتار خوبشان را کاهش دهند، می‌توانیم آن را قطع کنیم.
🔸
آنچه واقعاً اتفاق افتاد این است که ما یکشنبه یادداشت تفاهم را امضا کردیم. این موضوع شرایط توافق را تثبیت کرد.
ایرانی‌ها به ما آمدند و گفتند: «ما دوست داریم متن را تا جمعه منتشر نکنیم.» من واقعاً این را درک نمی‌کردم—می‌خواستم متن را فوراً منتشر کنم. اما برای اینکه با آنها کنار بیاییم، گفتیم: «باشه، ما تا جمعه صبر می‌کنیم.»
و سپس در طول دوشنبه و سه‌شنبه، در حالی که رئیس‌جمهور در نشست جی۷ بود، شاید رهبران خارجی با ایرانی‌ها صحبت می‌کردند و آنها را تشویق می‌کردند که این کار را انجام دهند.
ما قطعاً به آنها می‌گفتیم:
«ما تمایل شما برای عدم انتشار متن تا جمعه را درک می‌کنیم، اما می‌دانید که ما در یک نظام دموکراتیک زندگی می‌کنیم. مردم آمریکا می‌خواهند متن این توافق را ببینند. ما قطعاً دوست داریم هر چه زودتر آن را منتشر کنیم.»
و بنابراین آنها تصمیم گرفتند که رئیس‌جمهورشان آن را امضا کند، رئیس‌جمهور ما آن را امضا کند، و سپس متن را به عنوان یک سند امضا شده فوراً منتشر کنند.
🔸
اینکه فکر کنیم فروش چند میلیون دلار نفت قرار است اقتصاد ایران را به طور بنیادین تغییر دهد، درست نیست.
🔸
در مورد وجوه مسدود شده، مقدار پول — صادقانه بگویم نمی‌دانم.
اعدادی بیش از ۱۰۰ میلیارد دلار شنیده‌ام. در واقع اعدادی بیش از ۲۰۰ میلیارد دلار هم شنیده‌ام.
بیشتر آن در حساب‌های ایالات متحده نیست؛ بیشتر آن یا در خلیج فارس است، یا در اروپا، یا جای دیگری.
اما مقدار دقیق پول را نمی‌دانم — مقدار زیادی است.
🔸
من گزارش‌هایی دیده‌ام — نمی‌دانم این از کجا آمده — که قطری‌ها میلیاردها دلار و دارایی‌های ایرانی را آزاد کرده‌اند.
این اصلاً درست نیست. برای قطری‌ها غیرممکن است که بدون موافقت ما این کار را انجام دهند، و قطعاً بدون اینکه ما ببینیم.
🔸
درباره موشک‌های ایرانی:
توانایی آن‌ها در پرتاب موشک به طور قابل توجهی کاهش یافته است.
آیا این توانایی صفر شده؟ خیر. اما به طور قابل توجهی کاهش یافته است.
ما آن مأموریت را رها نکرده‌ایم. ما آن را به انجام رسانده‌ایم.
🔸
خدا را شکر. خوشحالم که پاپ چیزهای مثبتی درباره تفاهم‌نامه ما گفته است.
🔸
آنچه ما می‌گوییم این است که
نیروها را به سطح قبل از درگیری بازمی‌گردانیم،
قصد نداریم چند گروه ناو هواپیمابر اضافی را آنجا نگه داریم.
ایرانی‌ها این را نمی‌خواهند؛ صادقانه بگویم، ما هم این را نمی‌خواهیم.
🔸
خبرنگار: چه کسی آن صندوق ۳۰۰ میلیارد دلاری برای ایران را تأمین مالی می‌کند؟
جی‌دی ونس: تمایل زیادی از سوی دنیای عرب و حتی خارج از دنیای عرب وجود دارد که اگر ایران رفتار مناسبی داشته باشد، واقعاً در آن دخالت کنند.
🔸
کمی به توانایی رئیس‌جمهور ایمان داشته باشید، با توجه به اینکه او ما را تا اینجا رسانده است، می‌تواند ما را به گام نهایی برساند.
🔸
دونالد جی. ترامپ تنها رئیس دولتی در سراسر جهان است که در این لحظه نسبت به ملت اسرائیل همدردی دارد.
اگر من در کابینه دولت اسرائیل بودم، شاید به تنها متحد قدرتمندی که در سراسر جهان دارم حمله نمی‌کردم.
🔸
در سه ماه گذشته، دو سوم سلاح‌های دفاعی که از اسرائیل محافظت کرده‌اند، توسط دست‌های آمریکایی ساخته شده و با مالیات‌های آمریکایی پرداخت شده‌اند.
مشکل اسرائیل دونالد جی. ترامپ نیست، و هر کسی در اسرائیل که فکر می‌کند بزرگ‌ترین مشکلشان رئیس‌جمهور ایالات متحده است، باید بیدار شود و واقعیت وضعیت کشورشان را درک کند.
🔸
خبرنگار: چه چیزی مانع ایران می‌شود که در آینده برنامه هسته‌ای خود را بازسازی و از سر بگیرد؟
جی‌دی ونس: اول از همه، آنها باید پول زیادی به دست آورند تا بتوانند برنامه هسته‌ای خود را بازسازی کنند.
c-span
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 190K · <a href="https://t.me/VahidOnline/76483" target="_blank">📅 19:03 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76482">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BTu26V8cU7QhHovqKXIpVkYKjo_P2J9Vyd8YQtDjdMiHdu6lmq2gJOS37UQl71pyEaITW0elclg3K_Q83wl90480BOmKuT2Du2jZ-me43iyO-0_5V7HipHZwOOozJxLYaf1gaFHtXkeohpgEB7ekXQEA8KMf46GM5pys1dHFuRCQ2kcHoBSQOljzGbT14M8RAj14dsv9_tABP--BwXw9Syvha3joj7dir7PilZJqrBSnQmrG4kr9EEgU_qvMqM8MeRVSjeqeOjxlMmr3fXIsUvhGUw7NlFHpzVJQUUyLZikw3GOEuwf8QiNd6FJm4MGBOlrBJvP45Gq8c37z7_JJdA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">معاون وزیر کشور و رییس سازمان امور اجتماعی ایران می‌گوید به افرادی که در تجمعات شبانه «دوقطبی‌سازی» می‌کردند، در یک نامه به طور «محرمانه» تذکر داده است.
«محمد بطحایی»، بدون اشاره به نام این افراد گفته است که «مورد اول مربوط به یک سازمان و تشکل سازمانی بود و در دو مورد دیگر به‌صورت فردی، نامه‌ محرمانه و البته همراه با احترام و تکریم برای افراد مورد نظر ارسال شده است.»
پس از اینکه گفته شد ایران و آمریکا به امضای تفاهم‌نامه‌ای برای رسیدن به یک توافق پایدار نزدیک هستند، برخی مخالفان این توافق که از چهره‌های نزدیک به جبهه پایداری، تشکل سیاسی اصولگرا و تندرو در ایران هستند، علیه «عباس عراقچی» و «محمدباقر قالیباف» شعار دادند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 196K · <a href="https://t.me/VahidOnline/76482" target="_blank">📅 18:27 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76481">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/lJJXCRb7SAV7jLCZ6PYaGOcECXj06AM3kayRp87vs8d6KSTSKvJFEBtgadt4uk7_G_L02YxzAb41LtwmsCOqaB7XWvJ1yFrs6S4beztzRzc95RViE7q-XI2Cz5l9V8X7C3WsBeiru9HGS5lQawkS73xSDXV9NvEDvyv2jQqvVTChfGGQv7Z4jrJPwZWwypFvcnbrOkKuFvPVO2Eh3XDRvffdOtOZfygtY4kabddbF59ydw5JOurf8f6GJap4XUSf-pcmXJ-RbHYhoAQEJUqgiNIE2PVgZGwIrY1NGWxcEdvcBBUur30PZ4-IGdhvF2TZhXS5Zav21265K2Vm25JENQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ایرنا: به پاکستان گفته شده "نیازی به برگزاری نشست حضوری در سوئیس نیست"
ننوشتند کی گفته:
منابع دیپلماتیک پاکستان گفتند که سفر برنامه ریزی شده شهباز شریف نخست وزیر این کشور به سوئیس لغو شده است.
این منابع مدعی شدند که از آنجایی که یادداشت تفاهم اسلام‌آباد از سوی رئیس جمهوری اسلامی ایران و رئیس دولت ایالات متحده به امضا رسیده است، به طرف پاکستانی اعلام شد ‌که اکنون نیازی به برگزاری نشست حضوری در سوئیس نیست.
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 216K · <a href="https://t.me/VahidOnline/76481" target="_blank">📅 17:39 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76480">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/u32BKjKf27bwbFSfjFEBR-U0aN0uHW7gozPoqR-n3dn5AdfHj-w2hd8IxCAPubMUBavH7JghLJlPMiMd0Nchu86LZ6GLRpO--HJuFZn5ll8kmRpZomAAqmHrl1pPiqzJadPpeGDoAcgM4pTBaVSecTGcJImNdjS4N5nyb_S9srOK2qs7g51gBiFI58fw7RROOkvdTxKWznsGtlPCOk4Wn_fcRypv7ni7GqiJYezEiD0YXEy477TOIPCQ46NeTjGsAbefyYUojb6sI3TEJoUx1sir7gdnkuUQQRj0cybvmN5aw480OB0fS3VtkBvkyodTCSl80RHQBWe5BdJk-uF5Jg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پست ترامپ ترجمه ماشین:
«نفت در جریان است، ایران هرگز نمی‌تواند سلاح هسته‌ای داشته باشد، جهان امن خواهد بود! بازارهای سهام غرش‌کنان پیش می‌روند، مشاغل در سطح رکورد هستند، و قیمت‌ها در حال کاهش‌اند؛ مقرون‌به‌صرفه شدن! کشور ما مثل هیچ‌وقتِ دیگر قدرتمند، امن و محترم است. «خواهش می‌کنم!» رئیس‌جمهور دی‌جی‌تی»
realDonaldTrump
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 210K · <a href="https://t.me/VahidOnline/76480" target="_blank">📅 17:37 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76479">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/K6CtZUKjLtXyMPHI7ixXn4EiP5FiVQ79L1J_ejLJMyQxgnM76-tFuh_nkeMCgIarTH2aPfnk5YaCjW-Q6kDFqWsoHemanGh4Fce8nX5gwQZLRzycTxLis7aPu4lpq-LZ5Bx2Kka4NCYYqgj-kJpMdRrrYJbNAfKfbQBLXUj3UYhIyvA107ZRD6jntwCtdtKdb0NJ6KgC3xX--MBxBbwbMGIxaekzNzjfjEbjcnti5HWliY7LnxLNyVbQ0kJXiT5HgJGbCv7Orkx-auiaEeq_eZ0VaevY8196FaqAm0IuZEaFYywoECG_AttM8YQNJXZ2uX4uxkC8zdoPQhj1TlcvGw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پست چند دقیقه پیش ترامپ: "پاپ لئو از توافق صلح آمریکا و ایران تمجید کرد."
realDonaldTrump
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 228K · <a href="https://t.me/VahidOnline/76479" target="_blank">📅 16:37 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76478">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/bVmnJB5JP1zGHKGGvnhKGhJGjRqIX7Fcw1rfFfvRUURK2S9pHPVplaH3VltJSVjgyTeu49yB_rCxM4mXlfjylPPSdJPFvHxkp1yMBTUj-bVNUzKOeyqggTm4EjiIRf3wOTOsMXI_VbbfbeG_brDymr9ty511k3OZhR_bAqsYEhmrMrriFy80ZsTOAnYk9tAec0ynyQ4586_TDdAWIbohFNaoGOFhlvoLL6zXMOjozEu9FfUDx6VVNR70wcpRmJtAuMg0XkBKQPArXZudrYEW1qLLGo9TC49_c2aGbDVyHlmquCWZQz3COSwk2-wu_siSBrZ5bidy6YObMlFDYDGYWA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پست چند ساعت پیش ترامپ:
این احمق‌ها که فکر می‌کنند من در قبال ایران به اندازه کافی سخت‌گیر نبوده‌ام، در حالی که بازار سهام همین الان به رکوردی تاریخی رسیده و قیمت نفت هم دارد «سقوط» می‌کند، یا حسودند، یا آدم‌های بدی هستند، یا احمق‌اند.
آمریکا را دوباره عظیم کنیم!!!
رئیس‌جمهور دی‌جی‌تی
realDonaldTrump
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 228K · <a href="https://t.me/VahidOnline/76478" target="_blank">📅 16:35 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76477">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/v49e6Sm5v6kGMlZwt6iwTapAQYGr4Wn-KMFE5hzKSYIQHusngl9U1PAMwRwEkRBf2nslkiUhWuA9LcJu8zgTJhpxLTsXQFd0FXArGwR1xOkxCWqYc41ZQKO8gf9ZLZg1RIFwwfayihVqGgGdguy2J39dBgLy4DyeXesejfVmH2kLzRZjZTIZ8_SgRa7iC7MHtJ6z4TlzIPE3lDN1w7KCjh5_o5CwGMOJqNdEtAe-GDSQ24CO2PZKVHN8sMm-u3mMR4snv8Z3O1n8ItzbgYZs8iSD-8Af_d3MrLYavdeBD6uUVXrl-cA4KE6NejmyuzhYLRHEp2JPN5k9cd5cid90fg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پیت هگست، وزیر دفاع آمریکا، روز پنج‌شنبه ۲۸ خرداد در یک موضع‌گیری درباره تفاهم‌نامه اسلام‌آباد تأکید کرد که ارتش آمریکا قرار است «چماق بزرگ پشت مذاکرات» باشد.
او همچنین تأکید کرد که هر گونه تغییر در اندازه حضور نظامی آمریکا در خاورمیانه «بسته به شرایط» خواهد بود.
این نخستین اظهار نظر هگست در پی امضای تفاهم‌نامه اسلام‌آباد میان تهران و واشینگتن است که بامداد پنج‌شنبه توسط رئیس جمهور ایران هم امضا شد و رسمیت یافت. دونالد ترامپ ساعتی پیش از مسعود پزشکیان سند را امضا کرده بود.
متن تفاهم‌نامه‌ای که دولت آمریکا به امضایش رضایت داد حتی از چند روز پیش از امضا شدن هم انتقادهایی در پی داشت، انتقادهایی که با انتشار متن کامل آن افزایش یافت.
به نظر می‌رسد که سخنان وزیر دفاع آمریکا هم تا اندازه‌ای پاسخ به همین انتقادها باشد.
به گفته پیت هگست،‌ آمریکا «از موضع قدرت به توافق با ایران رسید».
@
VahidHeadline
وزیر دفاع آمریکا همچنین گفت که برخی کشورهای اروپایی آماده‌اند در عملیات پاکسازی مین‌ها در تنگه هرمز مشارکت کنند.
هگست در عین حال از بریتانیا خواست نقش گسترده‌تری ایفا کند و گفت که این کشور باید «گام بیشتری بردارد.»
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 228K · <a href="https://t.me/VahidOnline/76477" target="_blank">📅 16:32 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76476">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ly5U_mxRmWrvCjfPe6tJH7bbxxWgAvHoOSlfj5OUSqjLBj1Hz7By7WjHSxmO-bGZWonHxyaL7ggPIRRek0OA4RKMmD8_2mq4apJALOFEKkpjGuWNvLgnbEoz_lSTMUpPoRd8SQhsyiqFPUiEswvE3A2p-UFRi1s40u6S2u6qbT8IITK8V6JIcO7qlGDy-8FiBX8d2BqivhefCyf78NoeE36WxDtO7d3FPY1Su-fFizmCWZqHe8TMA-73KgsgaK43xjBIwswgQAyOj0WZSvidvtfubiU2G3BBFHSKq-rrU6O8Uu3sUeGMExzDXBmjNHCImz5k_fD6u1aGJ4watlowgw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دادگاه کیفری استان قم، پرستو احمدی، خواننده، و هشت نفر دیگر از دست‌اندرکاران و نوازندگان «کنسرت کاروانسرا» را به‌طور جداگانه به ۷۴ ضربه شلاق تعزیری، دو سال ممنوع‌الخروجی و دو سال ممنوعیت از فعالیت هنری محکوم کرد.
اتهام این هنرمندان در این حکم قضایی جریحه‌دار کردن عفت عمومی از طریق تولید و انتشار محتوای مبتذل و خلاف اخلاق در بستر فضای مجازی» عنوان شده است.
پرستو احمدی ۲۱ آذر سال ۱۴۰۳، به همراه گروهی از نوازندگان مَرد شامل احسان بیرقدار، سهیل فقیه‌نصیری، امین طاهری و امیرعلی پیرنیا، در کانال یوتیوب خود ویدئویی بدون حجاب اجباری، از «کنسرت کاروانسرا» یا «کنسرت فرضی» را منتشر کرد.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 263K · <a href="https://t.me/VahidOnline/76476" target="_blank">📅 16:30 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76475">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Z7yvfqsAaFR586Nwg5kag4hAxw-zoSkMMD3GnieKFp3BuS6MV8OtbvSKLUFhqSDx1gx15BgO0EdltHR2conugbKSRsdWkXLkRM0r0q0EDWy-A0mOne1GEK1J-N5UylqJzFG4weY9XKzlIp6uSTCObbFaRFDAPDYRB-XpXbfe9hIdJSUDRzBor9O-QrVd55TfnPC0BYsjE0DhlXdxb9A5KQlBK8h8abTxpPJKlFvVP8Y9fBpxfUemwoz1c1-UvgvregWub3Cp-ieHMrGPwvc2D4DshMnBcrOdEGo8vjLz8PFpg0aG88VqfjEthAsGO3cRWmFeF-grRXWfU0KJxwBdBA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این توییت ۹ سال پیش ترامپ داره توجه می‌گیره:
ایران به آخر خط رسیده بود و آماده فروپاشی بود، تا این‌که آمریکا از راه رسید  و در قالب «توافق ایران» به آن یک طناب نجات داد: ۱۵۰ میلیارد دلار.
realDonaldTrump
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 390K · <a href="https://t.me/VahidOnline/76475" target="_blank">📅 05:48 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76474">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/JH13bf3XNn73ub8equbj2ooEyEmRsrLBw7FdzJ070IGJCbc2uqQTzge-aIJvOacqgsHA0MlFbcayMJ4g6dQ2ogAGcwPwjPjXp7H38W4WP_2oVnBumUxBhKNOeJ_tn4oT8ttvMhCQY9acRWFJZYFIHNqXnBKaJxTlRrJb3mfv-ra9jNgXRPNv5PObo5baZuEh3ODDqMuYcPz-Th1Dcf2Nh8p9s_TqaC5_m_WSlghzvTd9PxZPjJNi8z9HltbS8l-fWikcvL4MIG1jiwJlSA98Q8GcItRshoPkAJCPhE2IgzZhg1Adg4C7R-kGaIUjrE8Kmp1OT7TEa-jOQcYB0j4DOQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">درستش کردم
MahvashJebeli
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 390K · <a href="https://t.me/VahidOnline/76474" target="_blank">📅 04:35 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76471">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/TvBEF3Q3I_kUbA5_Z8-m-Of3z_0fOY83EIdSWJFyEXKkem3DhP0TAR0rrHD2B9XYAhy2tKfPm-tJinLh_IwPGNiKGZUFg54Lyy_XcJrFyB46TOwLkjH75xlTeho0LVDDdzOTbK0m3F6dpWyMb8DrnkD6aE0FsNInzQmLXvswxTg-04HIlp0bQGBSPpPh1_AH4BeM685I3eQ-dA3Ua4SDhiBQu-8Oj1j7UVFH5qDNxM7iq5BEOVFW98Nne3aIov4Z56RuD5Xy8fC7qddtRB6bdh0kd6Mnlwv5osJqZFQuzWfMgMzLdbyCp7XMWDoS7rSSqMKNB-WOyZuyEjVWJIAEKQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/aAbJBCbAWum1ncwuNiTuiUhyhQwzMwPITNVHWHYXYFiIq5bjUMv91vzQhC5lZvIPJ_0jYo2gaWzbxwZzsiyhmd26ooApdnhwsxy3JFDjVpjwuxdWr7QSaa4GRcqFp7LEJ3kyWN2uvhiNKXJrppkskFQef2JbUmmjrSONZCSMB7NmBFnAa__LYFVkSM3qCnhtaGWCYk33a3QXQIyfu74sriTpjeOKCFh2LXghOnT7U98GVEST82Rn5mlX5pAkHgK9x6hqUnUeMDFpH7zbKmBNM_KNQQAEuEHMTIZjF7L42s0PkgVzIqa0QTftEiQH0_664ut2L598bSPbSVJ_p3vHvw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/KCsVeih5Lu5Zh7NJcJOaxX2f_5yaO8tPbv5x29iCsfXN3mfWBtnj866QKFMeb09A11NJEaCL78xd0cRtP1WHt0VIqcVCOgU_jHpXh_YlNsvVm5i5YM21WAwdx5nPqCdomluQHFJG9UtMF3uPriWaU5nQM1ejq0wZbavltbnpg3T8GgGaRhzcOpRJh3NtBWo0WgCbsfBoTcXTWKKix_bn9rWPM9u-14djV93w7EKyRE50VX6O46Ibhxwz5vYGotx50b2RZMp_6_qXrzeAxepv2dgyeyX-o5ze0cY3dw7qJQ7azXH9J0UJal02lMz-bbX1gggaWB5Ve9MyWKo6GuL0aQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">امضای پزشکیان پس از
امضای ترامپ
تصاویر منتشر شده از سوی ایرنا
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 396K · <a href="https://t.me/VahidOnline/76471" target="_blank">📅 03:50 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76470">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/a6a09c6ccc.mp4?token=CPcoKpgCvaUwS3ZOhfd-gvGqGDc9yksHYlWHKXjF8KdgVCB1CZ4L2IeGwZJkkb_J9mQ5Xm212R9-9wkIoMEnqkoG5xOIZnek4H8OL1YJxQXZaKIFB2lxlp51EBI65bZOBOywUUCOzA6hdsWe7MYovFlVd6ox6eeiw219vhkA-nJ4ndmNNvqOKNqMYIqulflnmSSp1EnF49dbPtQhxI4vCWW7_6Jgl8OZLeoKe9DyCpi4Q3i5mDP0PTfl42Y5a3tSU7ImHp8lnCCQ4lB80rIiDncvbYgjgs-eiLIpzFO-jZYBv523Q49XxmL8o7f35zFgLFDL9ScVrC_C8wIIkFIzZw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/a6a09c6ccc.mp4?token=CPcoKpgCvaUwS3ZOhfd-gvGqGDc9yksHYlWHKXjF8KdgVCB1CZ4L2IeGwZJkkb_J9mQ5Xm212R9-9wkIoMEnqkoG5xOIZnek4H8OL1YJxQXZaKIFB2lxlp51EBI65bZOBOywUUCOzA6hdsWe7MYovFlVd6ox6eeiw219vhkA-nJ4ndmNNvqOKNqMYIqulflnmSSp1EnF49dbPtQhxI4vCWW7_6Jgl8OZLeoKe9DyCpi4Q3i5mDP0PTfl42Y5a3tSU7ImHp8lnCCQ4lB80rIiDncvbYgjgs-eiLIpzFO-jZYBv523Q49XxmL8o7f35zFgLFDL9ScVrC_C8wIIkFIzZw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">لحظه امضای یادداشت تفاهم از سوی ترامپ
دونالد ترامپ، رئیس جمهور آمریکا که چهارشنبه شب در کاخ الیزه میهمان ضیافت شام با امانوئل مکرون بود نسخه نهایی و منتشر شده تفاهم‌نامه با جمهوری اسلامی ایران را امضاء کرده است. مسعود پزشکیان نیز این سند را امضاء کرده است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 386K · <a href="https://t.me/VahidOnline/76470" target="_blank">📅 03:25 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76459">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/10e61c88b0.mp4?token=dWKJLaFZKB6qKX-m26EsslzRbmAj2SP-Ym2YH4CGsfsH3Cg3dj41kkxmtca83TPtFAhLUmTz3QO2epwlfrZAdWt7tDtM25PCBkoWvknPqBcFExm3c60ll4IZDa-rMaLrTzPnfNwVHIvUsPg6MamPI4J4cexM6HHk1AXXs5PrZj3cigU7uAtVXih2EBbIzSc7Dm6TdWTFjJDN0x3SiD1Ks8zPClQui9bxtR9ufK1WJ3UopXKTFtmEU9BcFY0AZlEaR5uWVZJUfz_v0uKPvTZTC3tOTnxpAEcp2Eij5JbvyItvbDryNIve0SkySRT7SW8sbyMQeLxThc4b96-eIpwI5w" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/10e61c88b0.mp4?token=dWKJLaFZKB6qKX-m26EsslzRbmAj2SP-Ym2YH4CGsfsH3Cg3dj41kkxmtca83TPtFAhLUmTz3QO2epwlfrZAdWt7tDtM25PCBkoWvknPqBcFExm3c60ll4IZDa-rMaLrTzPnfNwVHIvUsPg6MamPI4J4cexM6HHk1AXXs5PrZj3cigU7uAtVXih2EBbIzSc7Dm6TdWTFjJDN0x3SiD1Ks8zPClQui9bxtR9ufK1WJ3UopXKTFtmEU9BcFY0AZlEaR5uWVZJUfz_v0uKPvTZTC3tOTnxpAEcp2Eij5JbvyItvbDryNIve0SkySRT7SW8sbyMQeLxThc4b96-eIpwI5w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">☄️
ترامپ و پزشکیان امضا کردند
دونالد ترامپ، در پاسخ به سوال خبرنگاران که آیا تفاهم‌نامه با جمهوری اسلامی را امضا کرده است پاسخ داد: «بله امضا کردم...در ورسای امضا کردم.»
@
VahidHeadline
پیش‌تر
:
بقایی: همین الان که با شما صحبت می‌کنم یعنی بامداد ۲۸ خرداد احتمالاً متن تفاهم نامه اسلام آباد به امضای روسای جمهور ایران و آمریکا رسیده باشد.
آپدیت:
توییت شهباز شریف نخست‌وزیر پاکستان
ترجمه ماشین:
باعث افتخار من است که اعلام کنم «یادداشت تفاهم تاریخی اسلام‌آباد» امروز به‌صورت الکترونیکی میان ایالات متحده آمریکا و جمهوری اسلامی ایران امضا شد. این یادداشت تفاهم به امضای رؤسای محترم هر دو کشور رسیده و من نیز به‌عنوان میانجی آن را تأیید کرده‌ام. امضای این توافق در بالاترین سطح دولت‌های مربوطه، نشان‌دهنده تعهد دو طرف به حل‌وفصل دیپلماتیک این مناقشه است. یادداشت تفاهم اسلام‌آباد با اثر فوری لازم‌الاجرا خواهد شد و در نخستین گام، جمهوری اسلامی ایران فوراً تنگه هرمز را بازگشایی خواهد کرد و ایالات متحده آمریکا نیز بلافاصله محاصره دریایی را لغو خواهد کرد.
پاکستان، با حمایت دولت قطر به‌عنوان میانجی مشترک، مراسم رسمی را طبق برنامه در تاریخ ۱۹ ژوئن ۲۰۲۶ در سوئیس میزبانی خواهد کرد تا این رویداد تاریخی گرامی داشته شود و گفت‌وگوهای فنی آغاز گردد.
صمیمانه‌ترین تبریکات و قدردانی خالصانه خود را به رئیس‌جمهور ایالات متحده، دونالد جی. ترامپ، تقدیم می‌کنم؛ کسی که تعهد استوارش به دیپلماسی و ترجیحش برای حل‌وفصل مسالمت‌آمیز، بار دیگر به پایان دادن به مناقشه‌ای کمک کرد که می‌توانست پیامدهای ویرانگری برای منطقه و فراتر از آن داشته باشد. همچنین از تلاش‌ها و کوشش‌های خستگی‌ناپذیر تیم مذاکره‌کننده ایالات متحده، از جمله جی.دی. ونس، استیو ویتکاف و جرد کوشنر، به‌خاطر نقش ارزشمندشان در این دستاورد تقدیر می‌کنم.
احترام و قدردانی عمیق خود را نسبت به حضرت آیت‌الله سید مجتبی حسینی خامنه‌ای، رهبر عالی جمهوری اسلامی ایران، و رئیس‌جمهور مسعود پزشکیان ابراز می‌کنم؛ به‌خاطر خرد، دوراندیشی و دولتمردی آنان در پذیرش آرمان صلح. همچنین مایلم تلاش‌های تیم مذاکره‌کننده ایران، از جمله محمدباقر قالیباف، عباس عراقچی و اسکندر مؤمنی را به رسمیت بشناسم؛ کسانی که صبر، پایداری و تعهدشان به تعامل سازنده، در به ثمر رسیدن این توافق نقشی اساسی داشت.
مایلم به‌طور ویژه از تلاش‌های صادقانه و تعامل سازنده رهبری دولت قطر در کمک به رسیدن به این نقطه قدردانی کنم. همچنین از رهبری پادشاهی عربستان سعودی، جمهوری ترکیه و جمهوری عربی مصر به‌خاطر نقش ضروری و مشارکت‌های ارزشمندشان در این زمینه، بسیار تقدیر می‌کنم.
همچنین مایلم به‌طور ویژه از فیلد مارشال سید عاصم منیر یاد کنم؛ کسی که تلاش‌های خستگی‌ناپذیر، فداکاری بی‌چشمداشت و نقش کلیدی‌اش در تسهیل این پیشرفت و پیشبرد آرمان صلح و ثبات منطقه‌ای حیاتی بود.
باشد که این یادداشت تفاهم، بنیانی پایدار برای تفاهم بیشتر، احترام متقابل و رفاه مشترک در سراسر منطقه باشد.
CMShehbaz
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 397K · <a href="https://t.me/VahidOnline/76459" target="_blank">📅 00:52 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76458">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">"متن کامل یادداشت تفاهم اسلام‌آباد بین جمهوری اسلامی ایران و ایالات متحده آمریکا"
به نقل از ایرنا:
https://telegra.ph/mou-06-17-2
ترجمه متن منتشر شده از سوی آمریکا
@
VahidHeadline
مقایسه نسخه منتشر شده از سوی ایرنا با نسخه  نسخه آمریکایی که بی‌بی‌سی به آن دست یافته است، نشان می‌دهد دو نسخه از این توافق ۱۴ بندی تقریبا به طور کامل یکسانند.
تنها تفاوت جزئی در بند ششم دیده می‌شود؛ بندی که با این عبارت آغاز می‌شود:
«ایالات متحده آمریکا متعهد می‌شود با همکاری شرکای منطقه‌ای، یک برنامه نهایی مورد توافق طرفین با حداقل ۳۰۰ میلیارد دلار برای بازسازی و توسعه اقتصادی جمهوری اسلامی ایران تدوین کند. سازوکار اجرای این برنامه به عنوان بخشی از توافق نهایی، ظرف ۶۰ روز نهایی خواهد شد.»
آخرین جمله این بند در نسخه آمریکایی چنین است:
«تمام مجوزها، معافیت‌ها و اجازه‌های لازم برای انجام معاملات اولیه مرتبط، از سوی ایالات متحده آمریکا صادر خواهد شد.»
اما در نسخه منتشر شده توسط ایرنا، واژه «اولیه» از این جمله حذف شده است.
با این حال، به نظر نمی‌رسد این تفاوت جزئی تغییری اساسی در مفهوم یا محتوای توافق ایجاد کند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 406K · <a href="https://t.me/VahidOnline/76458" target="_blank">📅 22:53 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76456">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/euPHE1-JtV9D8nK0_yjvMC52DcJCANC4Ia_ssmwuXyL28iSb10tFRtqFabguCeau32MrbhmYx4mpQTFpJommOu212Vtw2pBaNhn439gMEjMLgRF0gUib_9xnB2fGHeuVhnbynSXXfr6ex44Zj6VVCVWKlhahP_WGusfTR2VApbpHSCFMkl2nc0OcsC606zJeIT0HqiRNx-RJUGgriKdjNdaRYHIMuBjeKikzjKOW_xk-uh9RVr4_KtF53I4VpUMFqkxKjeByInMMRs-LwCmxR8FxrLygiy1FVmGuQPqh7Wa0DdT6fzxowEIY67FzocKHKDt7r9Jcb-QrE6Z5-nAr0g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سخنگوی وزارت خارجه جمهوری اسلامی روز چهارشنبه از احتمال امضای توافق پایان جنگ توسط روسای جمهوری ایران و آمریکا خبر داد و گفت این مسئله «در حالی بررسی است».
به گزارش رسانه‌های نزدیک به حکومت ایران، اسماعیل بقائی درباره احتمال امضای یادداشت تفاهم از سوی مسعود پزشکیان و دونالد ترامپ اعلام کرد: «این ایده مطرح است و همچنان در حال بررسی است.»
پیش از این طرف‌های ایرانی و آمریکایی خبر داده بودند جی‌دی ونس، معاون رئیس‌جمهور آمریکا، و محمدباقر قالیباف، رئیس مجلس شورای اسلامی، در سوئیس این تفاهم‌نامه را امضا خواهند کرد.
دولت سوئیس تأیید کرد مراسم امضای این تفاهم در اقامتگاه کوهستانی بورگن‌اشتوک برگزار خواهد شد.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 384K · <a href="https://t.me/VahidOnline/76456" target="_blank">📅 21:28 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76455">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">کنفرانس خبری ترامپ
:‌
🔸
یکشنبه، ما به توافقی با ایران رسیدیم که همه چیزهایی را که قصد داشتیم به آن دست یابیم محقق می‌کند—همه چیز و حتی بیشتر.
🔸
اگر این توافق را انجام نمی‌دادیم، می‌توانستیم برای ۲ تا ۳-۴ هفته یا حتی ۲ سال بمب‌های بیشتری رها کنیم.
شما هرگز تنگه هرمز را باز نمی‌دیدید.
🔸
اگر من ژنرال سلیمانی را نکشته بودم، احتمالاً الان درباره این توافق صحبت نمی‌کردیم، چون او نابغه‌ای دیوانه بود.
آنها هرگز نتوانستند جایگزین او شوند.
🔸
رهبران جهان از اینکه ما به توافق رسیدیم بسیار خوشحالند، همه‌شان.
هیچ کشوری به ما نیامد و نگفت «لطفاً آقا، بمب‌ها را روی آن‌ها رها کن. لطفاً بمب‌ها را رها کن» — آدم‌های احمق این را می‌گویند.
🔸
رهبران جدید ایران باهوش هستند، بسیار باهوش.
آنها بسیار کمتر رادیکال شده‌اند. فکر می‌کنم واقعاً کشورشان را دوست دارند. آنها خوب هستند.
🔸
نمی‌خواستم شاهد یک فاجعه اقتصادی باشم؛ اگر این روند ادامه پیدا می‌کرد، ممکن بود اتفاق بیفتد.
هر بار که درباره صلح صحبت می‌کردیم، بازار سهام بالا می‌رفت.
بازار سهام از هر کسی که آنجا هست، از جمله افرادی که روی این صحنه هستند—به جز من—باهوش‌تر است.
🔸
بازار سهام بسیار درخشان است. و هر بار که چیزی شگفت‌انگیز می‌گفتیم، مثل «ما قرار است توافق کنیم»، بازار بالا می‌رفت.
و هر بار، هر بار که چیزی منفی می‌گفتیم، مثل «ببین چی شده، ما نمی‌توانیم توافق کنیم»، بازار پایین می‌آمد — خیلی زیاد، خیلی، خیلی زیاد.
این به شما چیزی می‌گوید.
🔸
من نمی‌خواستم مثل هربرت هوور بزرگ دیر کنم. من آن را نمی‌خواستم.
[چت‌جی‌پی‌تی: هربرت هوور رئیس‌جمهور آمریکا در آغاز رکود بزرگ ۱۹۲۹ بود. در حافظه سیاسی آمریکا، هوور نماد رئیسی‌جمهوری است که بحران زیر دستش منفجر شد و بعد متهم شد که دیر، ناکافی و با احتیاط بیش از حد واکنش نشان داد. حتی محله‌های فقیرنشین دوران رکود را با تمسخر Hoovervilles می‌گفتند.
پس منظور ترامپ احتمالاً این است: نمی‌خواستم آن‌قدر صبر کنم تا بحران از کنترل خارج شود و بعد همه بگویند رئیس‌جمهور دیر جنبید.]
🔸
درباره کشتن قاسم سلیمانی:
این یک همکاری مشترک بود، همان‌طور که در کسب‌وکار املاک می‌گوییم. این یک همکاری مشترک بین اسرائیل و ما بود.
ما یک ماه آن را بررسی کردیم. تقریباً یک ماه قبل می‌دانستیم که او با کدام هواپیما سفر خواهد کرد.
او فقط با خطوط هوایی تجاری، آن‌های بزرگ و پرجمعیت سفر می‌کرد، چون می‌دانست ما او را سرنگون نمی‌کنیم. آن‌ها خیلی باهوش هستند.
اما ما می‌دانستیم که او در آن هواپیما خواهد بود، او را دنبال کردیم، و سپس اسرائیل به من اطلاع داد که آن‌ها این کار را انجام نخواهند داد. و من باید تصمیم می‌گرفتم.
و من به او گفتم، «خب، اگر اسرائیل این کار را نمی‌کند، ما همه آماده‌ایم. آیا انجامش می‌دهیم؟ دوست داری انجامش دهی یا نه؟» گفتم، «البته، اگر می‌خواهی انجامش دهی، ما می‌توانیم انجامش دهیم.»
🔸
درباره نتانیاهو: بیبی نتانیاهو مرد خوبی است. گاهی کمی هیجان‌زده می‌شود، اما اتفاقاً مرد بسیار خوبی است.
ما یک اختلاف کوچک درباره لبنان داشتیم — من گفتم، می‌توانی کمی ملایم‌تر باشی، بیبی، لازم نیست هر بار که کسی وارد می‌شود یک ساختمان را خراب کنی؛ این کار حزب‌الله است.
🔸
نتانیاهو به کشور آمد و از باراک حسین اوباما، رئیس‌جمهور، التماس کرد که برجام را انجام ندهد. او گفت این می‌تواند پایان اسرائیل باشد، و اگر من وارد ماجرا نمی‌شدم، همینطور می‌شد.
و اوباما به او گوش نداد.
بیبی واقعاً به کنگره رفت و از آنها التماس کرد، اما به جایی نرسید. و آنها این توافق وحشتناک را داشتند که برای اسرائیل فاجعه‌بار بود.
🔸
این یک یادداشت تفاهم است. اگر در ۶۰ روز انجام نشود، اشکالی ندارد، ما به بمباران بازمی‌گردیم.
می‌دانید، من نمی‌خواهم این کار را بکنم، چون خیلی خوب است، خیلی خوب.
اما، خب، ممکن است مجبور شویم، چون هرگز اجازه نمی‌دهیم آنها سلاح هسته‌ای داشته باشند.
🔸
توافقی که ما با ایران روز یکشنبه به آن رسیدیم، به زودی امضا خواهد شد، فردا، شاید روز بعد.
🔸
ترامپ درباره اسرائیل:
فکر می‌کنم آنها می‌توانند در مورد حزب‌الله بهتر عمل کنند. نمی‌گویم نباید از خودشان محافظت کنند، بلکه می‌گویم — وقتی دو پهپاد به بیابان شلیک می‌شوند و بی‌خطر سقوط می‌کنند، نیازی نیست ساختمان‌ها را در بیروت خراب کنند.
آنها می‌توانند بهتر رفتار کنند. و صادقانه بگویم، آنها می‌توانند کار بهتری انجام دهند — من آنها را دوست دارم، به عنوان یک شریک عالی بودند، اما می‌توانند در مورد حزب‌الله خیلی بهتر عمل کنند.
🔸
ترامپ درباره ایران:
خب، آنها به سرمایه‌گذاری نیاز دارند، چون ما یک و نیم تریلیون، شاید دو تریلیون دلار خسارت وارد کردیم.
پس کسی باید به آنها کمک کند — خب، هیچ تضمینی برای کمک به آنها وجود ندارد، و ممکن است همسایگانشان کمی به آنها کمک کنند، نمی‌دانم، اما این مقدار زیادی پول است.
تقریباً هیچ‌کس چنین پولی ندارد — این همان نوع خسارتی است که وارد شده است.
🔸
آنها از یک نظر فرهنگی ابتدایی دارند، اما این فرهنگ ابتدایی نابغه است، آنها مردم بسیار باهوش و مذاکره‌کنندگان بسیار خوبی هستند.
🔸
درباره موشک:
ما در حال کار روی یک تلاش موازی با کشورهای خلیج فارس برای رسیدگی به مسائل غیرهسته‌ای هستیم، مانند موشک‌های بالستیک متعارف، که درباره آن صحبت خواهیم کرد و حمایت خواهیم کرد.
منظورم این است که آنها باید مقداری داشته باشند، چون دیگران مقداری دارند، شما هم باید داشته باشید — کسی این را گفت، «نباید به آنها یکی بدهید»، و من آدم‌هایی دارم — بعضی از این آدم‌ها را دوست دارم، اما فکر نمی‌کنم این را، فکر نمی‌کنم آنها باهوش باشند.
«البته، نباید اجازه دهید هیچ موشکی داشته باشند» — من گفتم، خب، من چه کار کنم، آیا می‌خواهم به عربستان سعودی اجازه دهم موشک داشته باشد، اما آنها نداشته باشند؟ «بله، قربان.»
اینطور کار نمی‌کند، می‌دانید، اینطور کار نمی‌کند، و موشک‌ها مشکل نیستند — موشک‌ها به یک مکان کوچک برخورد می‌کنند، اما سیاره را منفجر نمی‌کنند.
🔸
اگر آنها به توافق احترام نگذارند، یا برخی موارد حتی در توافق ذکر نشده باشد — این یک یادداشت تفاهم است، اما ما درک مشترکی از برخی مسائل داریم بدون اینکه آن را مکتوب کنیم — و، اگر آنها به آن احترام نگذارند، احتمالاً دوباره به بمباران آنها باز خواهیم گشت تا زمانی که به آن احترام بگذارند.
می‌دانید، شگفت‌انگیز است که بمب‌ها چه کار می‌توانند بکنند.
🔸
مردم می‌خواهند من پل‌ها را بمباران کنم.
من قبلاً این کار را انجام دادم، چون می‌دانید، آنها به یکی از وعده‌هایشان عمل نکردند و من بزرگ‌ترین پل آنها را بمباران کردم، معادل پل جورج واشنگتن در ایران.
اما ما آن پل را بمباران کردیم، شما دیدید.
🔸
می‌خواهم از چین، رئیس‌جمهور شی، تشکر کنم، من با او بودم و او کاملاً بی‌طرف ماند، کاملاً بی‌طرف، و من این را قدردانی می‌کنم.
و می‌خواهم از ولادیمیر پوتین تشکر کنم، او بسیار بی‌طرف بود.
🔸
خب، آزادسازی پول‌ها — پاسخ آسانی دارد.
ما مقدار زیادی از پول آن‌ها را گرفته‌ایم، و پول آن‌ها را از آن‌ها گرفته‌ایم.
وقتی پول ما نیست، پول آن‌هاست و ما در یک زمان مشخص آن را مسدود کردیم.
فکر می‌کنم باید آن را پس بدهیم، می‌دانید؟
اگر پس نمی‌دادیم، هیچ‌کس دیگر هرگز در دلار سرمایه‌گذاری نمی‌کرد.
🔸
گزارشگر: یک مرد دانا زمانی گفته بود، در ژانویه ۲۰۲۰، «ایران هرگز در جنگ پیروز نشده، اما هرگز در مذاکره شکست نخورده است.»
ترامپ: این را چه کسی گفته؟
گزارشگر: دونالد ترامپ.
ترامپ: اوه، فکر می‌کردم همین را می‌خواهی بگویی.
🔸
اگر آنها پرچم سفید تسلیم را بالا ببرند و بگویند «سپاس خداوند را که دونالد ترامپ بزرگ‌ترین رئیس‌جمهور تاریخ است»، نیویورک تایمز و سی‌ان‌ان خواهند گفت «ایران پیروزی بزرگی به دست آورد.»
🔸
راستی، محاصره تأثیرگذارتر از تمام حملات هوایی بود، جایی که ما بمب‌هایی به ارزش یک میلیارد دلار روی ایران ریختیم.
🔸
گزارشگر: چرا حالا برای شما قابل قبول است که آنها بخشی از توان موشکی خود را حفظ کنند؟
ترامپ: آنها چه چیزی را حفظ می‌کنند؟ آنها اکنون کمتر از دیگر کشورها دارند.
ما احتمالاً ۸۴، ۸۵ درصد از موشک‌هایشان را از کار انداختیم، بقیه زیر زمین هستند و حتی نمی‌توانند آنها را بیرون بیاورند.
🔸
ترامپ درباره ایران: آیا می‌خواهید اجازه دهید ۹۱ میلیون نفر از گرسنگی بمیرند؟
🔸
خبرنگار: آیا اکنون می‌توانید بگویید که آیا کسی در دولت شما بابت حمله به مدرسه‌ای که در اولین روز جنگ بیش از صد کودک را کشت، مسئول شناخته خواهد شد؟
ترامپ: اشتباهاتی رخ می‌دهد، جنگ چیز زشتی است، می‌دانم که در حال بررسی است.
من از پیت هگست سؤال می‌کنم چون آن‌ها در حال بررسی این موضوع هستند.
🔸
خبرنگار: چرا برای مراسم امضای توافق صلح ایران نمی‌مانید؟
ترامپ: ممکن است بمانم.
🔸
گزارشگر: آیا در این موضوع عنصری وجود دارد که شما معاون رئیس‌جمهور را بفرستید، اگر موفق شد که عالی است، شما به عنوان کسی که او را فرستاده نابغه به نظر می‌رسید. و اگر موفق نشد، تقصیر معاون رئیس‌جمهور است.
ترامپ: من این ایده را دوست دارم. خب، به این صورت، اگر موفق شد، من اعتبارش را می‌گیرم. اگر موفق نشد، تقصیر JD است.
بهتر است مراقب باشی، JD. او هواپیمایش را برمی‌گرداند و از اینجا فرار می‌کند.
بله، من این ایده را دوست دارم. فکر می‌کنم ایده خوبی است.
📡
@VahidOnline
بخش‌های بالا رو من انتخاب نکردم. هم‌زمان با حرف‌هاش از منابع خارجی با ترجمه ماشین گذاشتم.</div>
<div class="tg-footer">👁️ 354K · <a href="https://t.me/VahidOnline/76455" target="_blank">📅 19:39 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76454">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qTxQ0xk5UlYJYLMexPCq_GqhHwPInsCmNG2AYlvvSD21Oa2HgDdTUE3MfllkhMIvSaNZAz23lhhXrScYlFr2jCan4Ij-L3GhhYd1Ctb60YBHVML9Y65m-7bCKOtSPy5_9cXDC1zGt8eW87_z6s9GCuH9nhScEMMzAKLSoj6hCnmljMXgalc202cK6zz_rGeDWCCZeVTCyf3mHhdqkeaQ1zKfidLGsgk1HfbdgrMzibSu1a4DryLT3rbWowCtrU8sMNdoGDBfXJe4zJiOr8BBcJztL0vO-IDOD1xW8K0U0qzIe6d7OI5a2_htL3jQ6SvT3EsvyW9iVI5o33KNT_482g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شورای هماهنگی بانک‌ها، روز چهارشنبه ۲۷خرداد ۱۴۰۵، اذعان کرد بخشی از خدمات چهار بانک ملی، تجارت، صادرات و توسعه صادرات پس از گذشت چهار روز همچنان با محدودیت روبه‌رو است.
این شورا پیشتر در ۲۳ خرداد از وقوع یک «حمله سایبری محدود» به این چهار بانک خبر داده و اعلام کرده بود که این حمله موجب اختلال در ارائه برخی خدمات بانکی شده است.
رسانه ایران آی‌تی گزارش داده است که بر اثر این اختلال چند روزه، میلیون‌ها کاربر همچنان به حساب‌های خود دسترسی ندارند. این رسانه با انتقاد از وضعیت پیش آمده نوشت بسیاری از فعالان بازار از انجام معاملات مهم در بورس، طلا و سایر دارایی‌ها بازمانده‌اند.
شبکه بانکی ایران در سال‌های اخیر بارها هدف حملات سایبری قرار گرفته و در مواردی نیز اطلاعات مشتریان برخی بانک‌ها در فضای مجازی منتشر یا خرید و فروش شده است.
با وجود این، شورای هماهنگی بانک‌ها تاکید کرده است که سپرده‌ها، تراکنش‌ها و اطلاعات مالی مشتریان این چهار بانک در «امنیت کامل» قرار دارد.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 288K · <a href="https://t.me/VahidOnline/76454" target="_blank">📅 19:17 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76453">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/h0bIOsj8QDEfR4Kcz6GBLoHpiKbT0MH6JqduQ-0DnvVm0TRc9RcbiSTIKpPSqBmbI9JhJqKaqrpwEsKK1KsTAYhMyNPQt-SRjwEikJH5qJUwEBXRD0oLgnz4x8nPeOGa2cLnac8sqq1pP2IlFeRYQNdLS1cyOeHoQGFwDEn-4iUGbdngqV2l1Te_HSQ2ovyAfpYdY_JfLa0UJcRWm3GDcxGx9829qQC9i9MsS-YH_TW1VMEt1IIiBa7d1Fz5W0Sms867Uh555z4h_cvuFAdisrSbFeuPB4JaoaTCxZ8_KF019fEuEA87Q0esi3aTrC1abv0X86kQGkCIhDeMP1tPCw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تفاهم‌نامه ممکن است زودتر از نشست سوئیس امضا شود
آکسیوس، ترجمه ماشین:
آمریکا، ایران و میانجی‌ها در حال گفت‌وگو درباره برگزاری مراسم امضای یادداشت تفاهم هستند؛ مراسمی که در حال حاضر برای جمعه برنامه‌ریزی شده، اما به گفته یک دیپلمات از یکی از کشورهای میانجی و یک منبع دوم آگاه از گفت‌وگوها، ممکن است زودتر و حتی روز چهارشنبه برگزار شود.
چرا مهم است: اگر چنین اتفاقی بیفتد، یادداشت تفاهم به‌صورت الکترونیکی امضا خواهد شد، بخش‌های مربوط به تنگه هرمز در توافق اجرایی می‌شود و آمریکا ممکن است سرانجام متن توافق را منتشر کند.
منبع دیپلماتیک گفت گفت‌وگوها درباره جلو انداختن جدول زمانی با هدف باز کردن تنگه هرمز زودتر از جمعه انجام شده، چون هر دو طرف درباره این موضوع توافق داشتند.
عامل دیگر می‌تواند فشار سیاسی بر کاخ سفید برای انتشار متن یادداشت تفاهم باشد.
منبع آگاه از گفت‌وگوها مدعی شد این ایران بوده که خواسته متن تا زمان امضای رسمی منتشر نشود و رد کرد که کاخ سفید در واکنش به فشار سیاسی چنین تصمیمی گرفته باشد.
وضعیت فعلی: تا صبح چهارشنبه، هیچ تصمیم نهایی درباره تغییر زمان امضا گرفته نشده بود.
کاخ سفید از اظهارنظر خودداری کرد.
خبر اصلی: حتی اگر زمان امضا تغییر کند، نشست هیئت‌های آمریکایی و ایرانی، به ریاست معاون رئیس‌جمهور ونس و محمدباقر قالیباف، رئیس مجلس ایران، طبق برنامه روز جمعه در سوئیس برگزار خواهد شد؛ این را منابع گفتند.
انتظار می‌رود آنها درباره آغاز مذاکرات بر سر برنامه هسته‌ای ایران گفت‌وگو کنند.
نکته مبهم: یک مقام ارشد دولت به خبرنگاران گفت این توافق روز یکشنبه به‌صورت الکترونیکی از سوی رئیس‌جمهور ترامپ، ونس و قالیباف امضا شده است.
منبع دیپلماتیک مدعی شد چنین امضایی انجام نشده است.
منبع آگاه مدعی شد که این امضا انجام شده و امضای جدید یک «امضای دوم» خواهد بود. روشن نیست چرا دو امضا لازم بوده است.
چه چیزی را باید زیر نظر داشت: کاخ سفید از روز یکشنبه گفته است که باز شدن تنگه از سوی ایران و لغو محاصره آمریکا فقط از روز جمعه، پس از مراسم رسمی امضا، آغاز خواهد شد.
به گفته منبع دیپلماتیک، اگر توافق زودتر امضا شود، این روند هم جلو خواهد افتاد.
axios.com
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 280K · <a href="https://t.me/VahidOnline/76453" target="_blank">📅 19:09 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76452">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/cc6738c570.mp4?token=ToGvJshIRFBR-v1p8jDRyWSkF8cWLEvZ9KPLTRKBrLUVDGU0Ab2CDIAyEufaqN7OuuSwXRwB_G_DG68ITqhfSp9SerJeEXhyIv1PD5nzyp5cH5rCJN9F1CNyHLXwFkoDTW5Xni2SLbZZxzwW04kc-QF7Lg4jjQYTSibcC3B-74__Z_C9QFb5vMLIpA4QE38XyPusgDH5-IMfmkDlvEXzyQ--qREG6YXd-4ClXS96EF-oKQCRIE_4kd-r1JmQNNOpTgfMPLmqO-PdwVQ9_SbMnUMqS-Bubn1sMc4Y6KGDGGpd0pbuPvPEKW5H_NBba_FQw1vklVp2bT41h-GTAOFltg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/cc6738c570.mp4?token=ToGvJshIRFBR-v1p8jDRyWSkF8cWLEvZ9KPLTRKBrLUVDGU0Ab2CDIAyEufaqN7OuuSwXRwB_G_DG68ITqhfSp9SerJeEXhyIv1PD5nzyp5cH5rCJN9F1CNyHLXwFkoDTW5Xni2SLbZZxzwW04kc-QF7Lg4jjQYTSibcC3B-74__Z_C9QFb5vMLIpA4QE38XyPusgDH5-IMfmkDlvEXzyQ--qREG6YXd-4ClXS96EF-oKQCRIE_4kd-r1JmQNNOpTgfMPLmqO-PdwVQ9_SbMnUMqS-Bubn1sMc4Y6KGDGGpd0pbuPvPEKW5H_NBba_FQw1vklVp2bT41h-GTAOFltg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">رئیس جمهوری آمریکا در دیدار با نخست وزیر هند در حاشیه نشست گروه هفت گفت: تغییرات جمهوری اسلامی با دستور من برای کشتن قاسم سلیمانی آغاز شد.
دونالد ترامپ افزود: جمهوری اسلامی رده اول و دوم رهبری خود را از دست داده و اکنون با توافق من هرگز به سلاح هسته‌ای دست پیدا نخواهند کرد.
@
VahidHeadline
دونالد ترامپ، رییس‌جمهوری آمریکا، گفت از حق اسرائیل برای دفاع از خود حمایت می‌کند، اما انتظار دارد این کشور در تصمیم‌گیری‌هایش «قضاوت درست» داشته باشد.
@
VahidOOnLine
ترامپ در پاسخ به پرسش خبرنگاری که از او پرسید «آیا برخورد گرم رهبران اروپایی نشان‌دهنده همسو شدن آن‌ها با جهان‌بینی شماست؟»، گفت: «فکر می‌کنم آن‌ها به این نتیجه رسیده‌اند که حق با من بود. یک‌جورهایی همیشه حق با من است و در نهایت، آن‌ها هم معتقدند که حق با من بود.»
رئیس‌جمهوری آمریکا که در کنار نارندرا مودی، نخست‌وزیر هند با خبرنگاران صحبت می‌کرد، با اشاره به تمایل ناگهانی دیگر کشورها برای ورود به فرآیند توافقات اخیر افزود: «حالا یک‌دفعه همه‌شان می‌خواهند وارد ماجرا شوند و مشارکت کنند؛ در حالی که کار دیگر تقریبا تمام شده است و اصلا دلیلی ندارد آن‌ها را مشارکت دهیم.»
@
VahidOOnLine
بقیه حرف‌هاش (بی‌ربط به ایران):
۲۰ دقیقه ۲۲۰ مگابایت
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 263K · <a href="https://t.me/VahidOnline/76452" target="_blank">📅 18:57 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76451">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/tdnLnKmBJ_iL-6dR1O5RqJaki7be3w4RaGbF4LpxZqMskToNFtqttNn3RIxD7c1ZtGNF0DqpTXgY-gvtIHvqodHIrXjEPmdF5dX_2_xsF6h5gTi0jH-zU1J7s3-awfxpPkXDBKmNhIuv03J3DdSBLuB_KevW6TxX6cOV_xxbTyuwh--nKwTZqnGWhpDceEN957F4-xOaHZZL90UrI3WTfVN6EzgvgMPPVsB4kmHLO1yGYJcbNglJDIich_9VA5lOXAU4jw03vtqgYAG_TsUq2pOgJFKc6drU_gi4LSxC0o-yORoCeLa9yO-RcBzoaRr0UVfCvTY9R6MGMrJgAdOm7w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پست ترامپ، ترجمه ماشین:
من ۴۵ دقیقه دیگر از فرانسه یک کنفرانس خبری برگزار خواهم کرد. سپس برای شام با رهبران فرانسه و دیگر رهبران اروپایی به ورسای می‌روم و امشب به خانه بازمی‌گردم!
این سفر موفقیتی بزرگ بود، اما چیزی که بیشتر از همه می‌خواستند درباره‌اش حرف بزنند، این واقعیت بود که ایران سلاح هسته‌ای نخواهد داشت و تنگه هرمز فوراً باز خواهد شد.
در همه شاخص‌ها، ارقام مربوط به اقتصاد ایالات متحده عالی است؛ امروز شمار افرادی که مشغول به کار هستند از هر زمان دیگری بیشتر است. بیش از ۱۹.۱ تریلیون دلار در آمریکا سرمایه‌گذاری می‌شود، کارخانه‌ها و همه چیزهای دیگر در حال شکل‌گیری است؛ اما نکته مهم این است که ارقام اخیر بازار سهام به خاطر این توافق سر به فلک کشیده و به همین ترتیب، قیمت نفت هم به‌شدت در حال سقوط است!
رئیس‌جمهور دونالد جی. ترامپ
realDonaldTrump
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 266K · <a href="https://t.me/VahidOnline/76451" target="_blank">📅 17:49 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76450">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LjDtZAY2RBPf0cCjhvJ0CabE8ldMs4an1msdCyaxCo1yb07zM0vdrlGQ0lTVXlpwTiD3uNrsUyFYW3CkSNhpGjT8_pozunv6-wg8izC9ize3_P_3PceW56DVw11dSRjbSeSOI8pGUb_y1GO728EZycgqaGaFBtKcU2PARAnWW9fqE7Gm4_kFl3YYVjA3hskS0R4jZYHRV7uQ4JgbPyGM5uhuAj8po_X3t_VN4LDn4byA_CAYT4H4pat3tWSD1zt6LZDZImEdK11NzWz_hSSWRq27W8d5Sj59J4Qw-sqnMLqR-6l3TEdGGowvOypu7Tn7qX9PkEykdqv_RJpg6EcNmw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جی‌دی ونس، معاون رئیس‌جمهوری آمریکا، در گفتگو با برنامه صبحگاهی شبکه سی‌بی‌اس (CBS)، از سیاست‌های دولت دونالد ترامپ در قبال جمهوری اسلامی ایران دفاع کرد و به انتقاد از کسانی پرداخت که به گفته او، صرفا به دنبال تداوم درگیری نظامی هستند.
ونس با تفکیک میان «ابزار» و «هدف» در سیاست خارجی واشنگتن گفت: «رئیس‌جمهوری از دیپلماسی، اهرم‌های اقتصادی و فشار نظامی استفاده کرد تا مطمئن شود ایران به سلاح هسته‌ای دست پیدا نمی‌کند؛ هدف اصلی همواره همین بوده است». او با انتقاد از تندروها افزود: «بعضی‌ها فقط می‌خواهند بمباران‌ها ادامه داشته باشد، بدون اینکه توجه کنند آیا این کار اصلا دستاوردی برای مردم آمریکا دارد یا خیر».
معاون رئیس‌جمهوری آمریکا در پایان تاکید کرد که هدف ترامپ ایجاد بدبختی و رنج برای مردم ایران نیست، بلکه تمرکز اصلی دولت او، مهار برنامه‌های تسلیحاتی و جلوگیری از دستیابی تهران به سلاح هسته‌ای است.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 269K · <a href="https://t.me/VahidOnline/76450" target="_blank">📅 17:42 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76449">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/QwWIuHX7oAXDr-alfX-WAOQaf827BTW65mh1eHqv5BPVJng-KCfBLl7PH0z0CNMlHpWxmRfe_wfVAGTMhaKqvC7bW1-mATFe3acgRtHaB8KWeawn59r_GJGcTNQsEsh21yLNHYWcfxpL0w7OFOtxm36Fpn0gWEEQ4Gct5AJY13ro1OpLREDidO9CPafZvh34fMLowKvhyKE5ENmRtkjzSC9Xo6bLiuFiNNXRHYxR09QQWbmwlaw34-AdCpQ7CkGdtGiPirmuVJd2v-z0y_e6R54PLj8qjMKBZYe-_zs5NHTr_8XnUw4z3KjwJalmp2GWJxYRaxIxJKdtAO6Vf1iEhQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">.</div>
<div class="tg-footer">👁️ 266K · <a href="https://t.me/VahidOnline/76449" target="_blank">📅 17:32 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76448">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/790e3a4857.mp4?token=U37ED-hBUYhRTXlv7YSVE4XvHSpB1dpAgUtWLpFi0WX6OdauIfPy9QHCQ6ms0gJe6qLqayFv-qOGorgPEvQJzTk_yGvcLrDuIKOa-6HPQJPycTJwLRTaXTYbgvPnA_2Lgj1GZmE2u2CDpGiMKYQ0BO6QijxPwNcbT_AODJ6USiZmDl9qq5YDorAouYTMiWOmdrthM5IGtlPTlLXQaPnzkG1U7XudihNsbWcKnaY_WR9st132LMWrK5pNfDXRUEvcVVN5UGtbGMkMrib1IuX6xBxBLqRdwFOZh_YVsJ_7N-7oWlu9sUSaUC84oUO_R6SVRUrUCytzXatd9Jn1UYcraw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/790e3a4857.mp4?token=U37ED-hBUYhRTXlv7YSVE4XvHSpB1dpAgUtWLpFi0WX6OdauIfPy9QHCQ6ms0gJe6qLqayFv-qOGorgPEvQJzTk_yGvcLrDuIKOa-6HPQJPycTJwLRTaXTYbgvPnA_2Lgj1GZmE2u2CDpGiMKYQ0BO6QijxPwNcbT_AODJ6USiZmDl9qq5YDorAouYTMiWOmdrthM5IGtlPTlLXQaPnzkG1U7XudihNsbWcKnaY_WR9st132LMWrK5pNfDXRUEvcVVN5UGtbGMkMrib1IuX6xBxBLqRdwFOZh_YVsJ_7N-7oWlu9sUSaUC84oUO_R6SVRUrUCytzXatd9Jn1UYcraw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">زاکانی: خامنه‌ای در «عراق» هم تشییع می‌شود
علیرضا زاکانی، شهردار تهران روز چهارشنبه ۲۷ خردادماه برای نخستین بار و برخلاف گفته‌های پیشین مقام‌های جمهوری اسلامی اعلام کرد که مراسم تشییع علی خامنه‌ای در عراق هم برگزار می‌شود.
زاکانی به خبرنگاران گفت پس از دو روز مراسم وداع، جسد علی خامنه‌ای در روز ۱۵ تیر در تهران، ۱۶ تیر در قم و ۱۷ تیر در عراق تشییع خواهد شد.
مقام‌های جمهوری اسلامی پیش از این اعلام کرده بودند که رهبر پیشین  در مشهد دفن خواهد شد.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 280K · <a href="https://t.me/VahidOnline/76448" target="_blank">📅 16:30 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76447">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/6d8cc30b9b.mp4?token=NALzashQOBSO4dzQCWN2XVRI4-TSSkZTem1V9OUZTMu9EnfauvDNTvOLcYeQCOW1evIOj73o5VSGJf64oZBOqePLdS-NBCXYUC839CpMdYYGPj3sZL1i8WROsGUyaG20WyRUSLl1bZqqhj5_Ea1uAA46L6IInf9ECofgr0cdhe7dfqH9A4xVolwJq8FFQz_mt4dYnEkC8adARGyJYmr40_h7M51Okq_vk6LxYw5ZSw08BO8CbgfgaDGyAdVHLeY08hC_dWHbor9lKn5dvsRhdqqCB5oEKXAjTDjFb1TuCPQHyX_8vYPdDhRHWIqWvTm7rlNurbYtwJ9p6cNn8lMtaA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/6d8cc30b9b.mp4?token=NALzashQOBSO4dzQCWN2XVRI4-TSSkZTem1V9OUZTMu9EnfauvDNTvOLcYeQCOW1evIOj73o5VSGJf64oZBOqePLdS-NBCXYUC839CpMdYYGPj3sZL1i8WROsGUyaG20WyRUSLl1bZqqhj5_Ea1uAA46L6IInf9ECofgr0cdhe7dfqH9A4xVolwJq8FFQz_mt4dYnEkC8adARGyJYmr40_h7M51Okq_vk6LxYw5ZSw08BO8CbgfgaDGyAdVHLeY08hC_dWHbor9lKn5dvsRhdqqCB5oEKXAjTDjFb1TuCPQHyX_8vYPdDhRHWIqWvTm7rlNurbYtwJ9p6cNn8lMtaA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">محمدباقر قالیباف، رییس مجلس جمهوری اسلامی و رییس هیات مذاکره‌کننده جمهوری اسلامی با آمریکا، درباره اهمیت روابط اقتصادی با چین گفت جمهوری اسلامی باید از مرحله تقابل عبور کند و بر توسعه اقتصادی متمرکز شود.
قالیباف در نشست همفکری نماینده ویژه در امور چین با اتاق بازرگانی ایران گفت: «باید سنگر را از بچه‌های لانچر تحویل بگیریم، مردم را از زیر فشار اقتصادی دربیاوریم و کشور را بسازیم.»
او با توصیف جایگاه چین به‌عنوان کشوری «منحصربه‌فرد» برای جمهوری اسلامی در حوزه تجارت، افزود پکن باید باور کند که تهران «شریکی به تمام معنا» برای چین است.
رییس مجلس جمهوری اسلامی گفت هر بلوکی که با حضور کشورهای ساحلی خلیج فارس شکل بگیرد، محوریت آن «حتما چین و جمهوری اسلامی» خواهد بود.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 273K · <a href="https://t.me/VahidOnline/76447" target="_blank">📅 16:11 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76445">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Bp5i7DIbqQcVoP5_TWckEOWjstW8HnlM9iufcNNauIljgo1IZvLtNN5BFts1NpBizq-OjmDYylbd2Srk6xBAOEJ13oP_AEKrWoqtJ9AuPxBsr7PlfV_Gln8gupxzZZVVXzmP_UCxGD6JTkkqfndp7U9cgEJZZWVSbLvy-5cqs-mzBlz1o3PA69q6pFtxXov3YrmtCNc1qj26p2qRrsp-9JD45wa3IdBeouKRs6jOZXG96WTjllniWhmasW0nV90MycDl3QM5IuCJkqEnpBgjTuQCUgLFTN5sKLgGS5MNG0Cj3DzTLHRek8KIXyYp7C-Uhtt--Xb38ec6REiPCZX39Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/cda5339562.mp4?token=GcNui2Ak6bbq9kGFd9OYhGho8EH4X2D4O4V_6DZI6S1HYTRR6KbOD8ddMqGNTosxr6CgH_EVhhIFbsZBUWrrUqXqG5BZuD5hPcE_qrPWNreA1lEBT4Tda0-oQhZnarE3kLrcAFEZA13CuIDQ9U6gnE51-EEGKvi6CWcFGDNUU2QR7CPQ6u_AuIzRJ7GMc4ScZ8XnLYiLVLBpIv9PeQYxbNGETVseZZ4wcZiD2mM5s_XacGfnAvsAxftIyd63xOpyJ0nTnkzvrEKe2RW5Pb9DB4_p66PibPVVG3ticC9vZjrRtGid90nrBPKH1GWDOL_qortT_DMtbaLtG4AuEnkJmQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/cda5339562.mp4?token=GcNui2Ak6bbq9kGFd9OYhGho8EH4X2D4O4V_6DZI6S1HYTRR6KbOD8ddMqGNTosxr6CgH_EVhhIFbsZBUWrrUqXqG5BZuD5hPcE_qrPWNreA1lEBT4Tda0-oQhZnarE3kLrcAFEZA13CuIDQ9U6gnE51-EEGKvi6CWcFGDNUU2QR7CPQ6u_AuIzRJ7GMc4ScZ8XnLYiLVLBpIv9PeQYxbNGETVseZZ4wcZiD2mM5s_XacGfnAvsAxftIyd63xOpyJ0nTnkzvrEKe2RW5Pb9DB4_p66PibPVVG3ticC9vZjrRtGid90nrBPKH1GWDOL_qortT_DMtbaLtG4AuEnkJmQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دونالد ترامپ می‌گوید اگر از توافق رضایت نداشته باشد و ایران رفتارش را اصلاح نکند، بار دیگر ایران را بمباران خواهد کرد.
رئیس‌جمهور آمریکا که روز چهارشنبه در نشستی خبری همراه با عبدالفتاح السیسی، رئیس‌جمهور مصر، در حاشیه نشست رهبران گروه ۷ در فرانسه صحبت می‌کرد، گفت: «این فقط یک یادداشت تفاهم است. اگر از آن راضی نباشم و رفتارشان را اصلاح نکنند، دوباره به سمت آن‌ها شلیک می‌کنیم و روی سرشان بمب می‌اندازیم.»
دونالد ترامپ همچنین گزارش‌ها دربارهٔ سرمایه‌گذاری ۳۰۰ میلیارد دلاری این کشور در ایران بر اساس تفاهم‌نامه را نادرست خواند، اما گفت که آمریکا مانع سرمایه‌گذاری دیگر کشورها در ایران نخواهد شد.
متن تفاهم‌نامه هنوز  منتشر نشده، اما بر اساس یکی از بندهای متنی که برخی رسانه‌های آمریکایی منتشر کرده‌اند، چنین ذکر شده که «ایالات متحده متعهد می‌شود همراه با شرکای منطقه‌ای خود، طرحی جامع و مورد توافق دو طرف برای بازسازی و توسعه اقتصادی جمهوری اسلامی تدوین کند و تأمین مالی دست‌کم ۳۰۰ میلیارد دلار را تضمین نماید. سازوکار اجرای این طرح، به عنوان بخشی از توافق نهایی، ظرف ۶۰ روز تدوین خواهد شد».
رئیس‌جمهور آمریکا همچنین گفت در متن تفاهم‌نامه گفته نشده است که آمریکا پولی به ایران پرداخت می‌کند و وجود بندی دربارهٔ رفع فوری تحریم‌های ایران در متن تفاهم‌نامه را نیز رد کرد.
در متن منتشرشده در رسانه‌های آمریکایی، که صحت آن هنوز مورد تأیید قرار نگرفته، آمده است که «ایالات متحده متعهد می‌شود بر اساس جدول زمانی مورد توافق در توافق نهایی، همهٔ انواع تحریم‌های اعمال‌شده علیه جمهوری اسلامی ایران را لغو کند؛ از جمله قطعنامه‌های شورای امنیت سازمان ملل و شورای حکام آژانس بین‌المللی انرژی اتمی و همچنین تمامی تحریم‌های یکجانبه آمریکا، اعم از اولیه و ثانویه».
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 261K · <a href="https://t.me/VahidOnline/76445" target="_blank">📅 16:02 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76444">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/XbAv1y8bN8CKut1Cw_wNrrpFN64oHK23oUS8DW7rPPO2-uEjJ6vc8tSSFh9I7_PF-K7rsmwdoYhYjbrKUV_EQkO5nx8vQmqcFUvlwDtIiwAGqZTBd894_9JUwL4EFvc25YlE8_IfrsgDm8D_N4rhmklm3nqBClw6uBsrnDKoSnR2c0LLRF1IPcGQBIBmakVmFyfJGy4mLJ_MHiNKbkC5dwJuS9W8b_mMSzNScgSOQQ5X0uMigmEvWECVKFkjSG2r1rn_v1Tbe8_a36QFyrovWxpdS3isBew1NH-PERvJwYI3ccUC0p_LJkUqJS3t3mB10BBiVF56bpUHr0dM3XhPSQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ابراهیم رضایی، سخنگوی کمیسیون امنیت ملی و سیاست خارجی مجلس جمهوری اسلامی، با انتقاد از یادداشت تفاهم میان جمهوری اسلامی و آمریکا، این توافق را «نامتوازن» توصیف کرد و گفت همه خطوط قرمز جمهوری اسلامی در آن رعایت نشد.
رضایی در یک گفت‌وگوی تلویزیونی افزود جنگ پایان نیافته و نباید تصور کرد شرایط از وضعیت تقابل خارج شده است. او گفت: «ما در یک جنگ ترکیبی تمام‌عیار هستیم و باید از فرصت ایجادشده برای قوی‌تر شدن استفاده کنیم.»
سخنگوی کمیسیون امنیت ملی مجلس جمهوری اسلامی همچنین از منتقدان یادداشت تفاهم دفاع کرد و گفت نباید مخالفان تفاهم را «تندرو» خواند. او افزود: «اگر این افراد نبودند، الان سربازان آمریکایی بالای سر ما بودند.»
رضایی پیش‌تر نیز در شبکه اجتماعی ایکس نسبت به نحوه دفاع حامیان توافق از این تفاهم‌نامه انتقاد کرد. او از مقام‌های جمهوری اسلامی خواست از منابع عمومی برای تبلیغ «توافق» استفاده نکنند، منتقدان را تحمل کنند و برای توجیه تصمیم‌گیری‌ها از رهبر جمهوری اسلامی هزینه نکنند.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 234K · <a href="https://t.me/VahidOnline/76444" target="_blank">📅 16:02 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76443">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JPdI7zwlo6a94Arrsih2RfSp8rl3H_65YJZh9s2mRxyMKT8P21TRkCh6VpXjn9Fs9d5nvI0zRMLI1qDAjy4J7PGflfCf2f-9R1qrvE0DhUJn2MhRK2VN3UpD4yilAeGPpHfFXNDOPZZxqCmSDEF3epxLLsiZgYTB1mWPd3sCQAV8NzBXrox5LZHTcFGV_9P-dva4IeC7UTzM67VbUWJ6xxth1k6iECZubyaHKjecLUVxflCZ6RpJBZtNc_uEbr-NH-y87DsCOUbmK3wf0xWG1GSXlTIsnBYgbUynzGxSVxdgmflWhRFDSreOq_KXGtYKY9Ms5VsPjMZAKWxFdW7-6g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در ادامهٔ روند کاهشی قیمت ارزهای خارجی در بازار آزاد ایران، روز چهارشنبه ۲۷ خرداد قیمت هر دلار آمریکا به حدود ۱۵۳ هزار تومان رسید و قیمت سکه طلا هم در محدوده ۱۶۰ میلیون تومان اعلام شد.
قیمت دلار آمریکا که در مقطعی تا ۱۹۰ هزار تومان بالا رفته بود، تا کنون حدود ۲۰ درصد کاهش پیدا کرده است.
قیمت هر گرم طلای ۱۸ عیار نیز روز چهارشنبه به ۱۵ میلیون و ۷۶۷ هزار تومان و «سکه امامی» نیز به ۱۵۹ میلیون و ۵۰۰ هزار تومان کاهش یافت.
در مقابل، شاخص بازار سهام بورس تهران از زمان اعلام توافق رشد چشمگیری داشته و روز چهارشنبه با ثبت رکوردی تازه به بیش از ۵ میلیون و ۱۰۰ هزار واحد رسید.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 223K · <a href="https://t.me/VahidOnline/76443" target="_blank">📅 15:57 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76442">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bWoQQh8YL8udXclQzF58U_JqGFQ7VJ5VK4sE-WsgQblKqx3BTDoLEWD3-DV3REnuwktqs4QFOTbK_u0LJJGFzXckECmeZNTfinXefRW2xzokTsz6rR6_HFc3VjxSa0CIkQCzMJtLXYrDOEZPFa8rHxNBeDY9EugBes8RPpaZdjbexbq7DD2URqRyKD7sWCEVSu7SlG7af9ed6wbkdaV4njdPisOxKq-u7xVouTFPmPtYdn62699qOSKfEKkibDz2Tfk3kz8fZfl105qqZBorvYyyYoFv2NRGT6s8TRSF2VywfhofO7QSc94F7a3ApJu6do9eHeX05RfOWlcRYkRX8w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سران هفت کشور صنعتی جهان (G7) در بیانیه پایانی نشست خود از توافق میان ایالات متحده و جمهوری اسلامی حمایت کردند و آن را فرصتی مهم برای جلوگیری از دستیابی حکومت ایران به سلاح هسته‌ای و محدود کردن فعالیت‌های موشکی و منطقه‌ای تهران دانستند.
رهبران آمریکا، کانادا، فرانسه، آلمان، ایتالیا، ژاپن و بریتانیا همچنین اعلام کردند آماده‌اند در روند اجرای این توافق مشارکت داشته باشند.
در بخش دیگری از این بیانیه، بر ضرورت حفظ آزادی کشتیرانی و عبور بدون مانع کشتی‌ها در آبراه‌های بین‌المللی تاکید شده و این موضوع یکی از ارکان اصلی تجارت جهانی توصیف شده است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 209K · <a href="https://t.me/VahidOnline/76442" target="_blank">📅 15:57 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76441">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ZpXUbgWCatbccKRX4xvQK3iypqVSMXp_JlSVOEFzFvUsuAyk8XYPegpYDfim49_jhI_D8j_SQIXreWA8e4qZzTvpdSCXMvNL6y0-5RgIX9PFs093cwvoU6869eAFoY9zt6jL3xuEugEJS6OHMvD5GtdlSbBCR-KkReFvSiZ-v_Ig3HWHI5WJ2MHA5xYuN3Lrvz18IeuqtaN6y6pfr4VdaU_ez1xnQ0DO4Eq2MwJFe8ERQx6qnbmN_FJ7BEiu_y0nWDrme4zztTJwl_-Fs0FVTat8UTqyUOTfuXT_Auav-wDj2_l-sHcumcxAy_f-HU0YL5ILiOUcqpGftMKDdswFGA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">«مهری فرج‌زاده» ۳۶ ساله، ساکن کرج و مادر دو فرزند، روز جمعه ۱۹ دی‌ماه ۱۴۰۴ در فردیس کرج هدف شلیک گلوله قرار گرفته و جان خود را از دست داده است.
به گفته منابع مطلع، گلوله به ناحیه جمجمه او اصابت کرده بود و مهری فرج‌زاده پیش از رسیدن به بیمارستان «به‌آفرین» فردیس جان باخته بود.
نزدیکان او می‌گویند پس از دو روز پیگیری، پیکر مهری فرج‌زاده را روز ۲۱ دی‌ماه از بهشت سکینه کرج تحویل گرفتند.
مهری فرج‌زاده خانه‌دار بود و دو فرزند داشت. دختری ۱۵ ساله و پسری ۱۰ ساله که با کشته شدن مادرشان با فقدانی جبران‌ناپذیر روبه‌رو شدند.
@
VahidHeadline
آپدیت:
پیام دریافتی: پسرعمه‌ی مهری، اکبر حسن‌پور هم ۱۹ دی تو گوهردشت کرج با گلوله کشته شد. اکبر دو دختر ۱۶ و ۱۸ ساله داشت.
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 214K · <a href="https://t.me/VahidOnline/76441" target="_blank">📅 15:56 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76440">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromبنیاد عبدالرحمن برومند برای حقوق بشر در ایران</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/C7SGknz_YkMFUpLxjI0J0YGlN79IbuYr6P9eTJpDfIUoU-428QgObibE0gEqZdc-KE8z5S2oQg9LifUB_IWKCQUIVrUC3x-podVxZKv01LKe00jnHCFWHc5u7Ow_qWgrl3qPFaFvPv7GPw4BjaElmK6v6OqAYIBGL7UnwPK6nNPsNzj8fpMWUgLJ6Dl3i7p7EyFXRuyKx6hvLXZVMs5TL44iSmQ2qbZAvEh08YF6LI6Ja-AfvbseK3boSCOh9ry2YllEikNNHiCRiyDbaPM7paVTKXOKcOAdPPVPOMrtpQsH1X4SwmnS7BtiwDff_KphP-uKf9Sm7bK6y9NHML0wEQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
🔴
بنیاد عبدالرحمن برومند از اول ژانویه ۲۰۲۶ تاکنون، ۷۴۶ مورد اعدام را در ایران مستند کرده است که تنها ۵۲ مورد آن از آغاز ژوئن ۲۰۲۶ به اجرا درآمده است.
‏
🔸
جمهوری اسلامی در سایه جنگ و در واکنش به اعتراضات سراسری دی ماه ۱۴۰۴ به اجرای اعدام‌های سیاسی شتاب بخشیده است. از ابتدای سال جاری میلادی تاکنون، دست‌کم ۴۵ معترض و زندانی سیاسی متهم به جرایم علیه امنیت ملی، از جمله جاسوسی، اعدام شده‌اند.
‏
🔸
گزارش‌های رسیده به بنیاد عبدالرحمن برومند نشان می‌دهد که مبنای حقوقی اصلی بسیاری از این احکام اعدام، «اعترافات» اجباری اخذ شده از زندانیان تحت فشارهای جسمی و روحی بوده است؛ امری که نقض آشکار حقوق اولیه دادرسی عادلانه و مصونیت‌های بین‌المللی در برابر شکنجه به شمار می‌رود.
‏⁧
#نه_به_اعدام
⁩
@IranRights</div>
<div class="tg-footer">👁️ 283K · <a href="https://t.me/VahidOnline/76440" target="_blank">📅 15:55 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76439">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/649b79d41e.mp4?token=a-dnCl2geiAHTDe8xF7_4puBKr6jHF18MB5vNuIRdevAKxVg6GdE1NY3coxhuuDkuM0Lq0BqPQ2Qbo9vxNQU04pWE68Ja4pqNFxHPMXYg4nCt_w59q8sLj-l2k85uZ99caaSzb3SHJgZGgkUrBHQteMRNroBJ4Rq-7obMnaedt4s1Ur7Q_9y4XLYfDlPhss5g1D9MHFx9YulSQ_uKZpRzo2vRt3kd0TSs3lz_mefmUl-K_caFiTHHzQHLAH0YDTKyiy7Um-JGfVRjGH6kT6LCKUy8hVWwUbDo2ITLwiDbslz9mdHY4Ru9mGbkWPkGSIYkoEZ1RgkrQmFacw6wPfCNA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/649b79d41e.mp4?token=a-dnCl2geiAHTDe8xF7_4puBKr6jHF18MB5vNuIRdevAKxVg6GdE1NY3coxhuuDkuM0Lq0BqPQ2Qbo9vxNQU04pWE68Ja4pqNFxHPMXYg4nCt_w59q8sLj-l2k85uZ99caaSzb3SHJgZGgkUrBHQteMRNroBJ4Rq-7obMnaedt4s1Ur7Q_9y4XLYfDlPhss5g1D9MHFx9YulSQ_uKZpRzo2vRt3kd0TSs3lz_mefmUl-K_caFiTHHzQHLAH0YDTKyiy7Um-JGfVRjGH6kT6LCKUy8hVWwUbDo2ITLwiDbslz9mdHY4Ru9mGbkWPkGSIYkoEZ1RgkrQmFacw6wPfCNA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یک جت خصوصی تو یک اتوبان در تگزاس سقوط کرده، راننده‌ها رفتن کمک سرنشینها
J74wabx
یک نفر کشته شد؛ پنج نفر به دلیل استنشاق دود در بیمارستان بستری شدند.
AZ_Intel_
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 333K · <a href="https://t.me/VahidOnline/76439" target="_blank">📅 09:23 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76438">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BO542S0Utm5hG-i1KaAhEeH4yzTij1jYWcM-Vniv1kNh3j1UnPyDNzs698xKZKwLJDb6c0O45xZR5TJbqfkbBy0GQH7vpPPBaD1u1kgvQS9n0t5tsOKqMJxCe9SQXRnkgl31vRVsyUzq0s-wZ7vp5o_BQ0vyHXDXxBCVMnepp-EMhyTDZXqj0sBYOfLHY7QbcxXEesM3bkhEUjO1cUiqOM5s1Yxb4rIEPxOwNWpdYhGclIBGbKnzaVpqJFz8cR1QJzgAuDGxhsE4_rqU5YhGMGDznwa_w13yHB5QFlpLhP-oee0IwMwd8UVZpRA2OpVqW_qokKWQAMK6ed3D36pC-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نخستین نفتکش‌های حامل نفت خام ایران از زمان آغاز محاصرۀ دریایی آمریکا، از تنگۀ هرمز خارج شدند. این موضوع را صبح چهارشنبه یکی از وب‌سایت‌های ردیابی کشتی‌ها اعلام کرد.
وبسایت «تنکر ترکِرز» (Tanker Trackers) که ذخیره و حمل‌ونقل محموله‌های نفتی را دنبال می‌کند، بر اساس داده‌های دیجیتال منطبق با تصاویر ماهواره‌ای، «اولین صادرات نفت خام ایران در دو ماه اخیر» را تأیید کرده است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 344K · <a href="https://t.me/VahidOnline/76438" target="_blank">📅 08:48 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76437">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tvIOuu6ibgLINe0RTdPZzF_kvv2ETOAvHqdwzdEHaKfSkDLTKLXT8DCQsIDrTwvNRYPlHh4Zp_tFjXn8ye5fLUEfnj3eIZP4eyJqmaRYaiQKWdElEQHkMDaTmYjFdKY32Xj5LkBemhVBT4lbx-Q7_H2Y3-FTF590Uf1V6v9WUr1_hzXqTtZePibPONLzwT5CVCwv78JQTQ0F6-Yz33vvFfoHXNLqo-f0hZxIOfmPZGHqej-8nHdx4GPvJ5W7hwcbb7lEl31Ivc5VCGTgLoOp00W39LBYl-JzyzD9RqmMIMDj5b_bzOS_PPirtKGR2aZVQGi_XKnVASMRc97DpqNlDw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">به گزارش ان‌بی‌سی، حکومت ایران پس از اعلام یادداشت تفاهم با آمریکا، همچنان تعداد «زیادی» پهپاد به سمت شناورهای تجاری در تنگه هرمز پرتاب کرده است.
شبکه ان‌بی‌سی به نقل از یک مقام آمریکایی گزارش داده که سپاه پاسداران پهپادهایی پرتاب کرده که آمریکا توانسته آنها را پیش از آنکه تهدیدی برای شناورهای تجاری، کشتی‌های نظامی و خدمه حاضر در منطقه ایجاد کنند، رهگیری کند.
بر اساس این گزارش، سپاه پاسداران از زمان امضای «الکترونیکی» یادداشت تفاهم در روز یکشنبه، هر شب اقدام به پرتاب پهپاد کرده است.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 349K · <a href="https://t.me/VahidOnline/76437" target="_blank">📅 05:11 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76436">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/75a49fba40.mp4?token=PzSDPXX9cCJloTtgStM99dUBIk4fHTqLf0MNYFzWZydta6AZCZJI8muqAgrhqeMZ1oGTQTA-0BxiTCnjxD79a8qMuYoGyvD51Q7E0-N0zR0q3N8u-xEgePcMcJt1Z8OPwq-vGOeG2dOzg4rKfbGPERTrteSShJvPmMdCVUava2OrwN7BUU9Im71SilDFegrJkqnOvCyvqGGr5L6FK_aOWKEK7HWsyajFrOX_-TSiq3fcuZRG6YoRj9_Jr8jk3Xr7d0hvFT7yvPKC3RP2rhVTlSHpgU_FMfBtJHeE0iM9zYjk6hextm5UQQ1UmiGsmCHidCdNDLxonjU3aLnniypqPw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/75a49fba40.mp4?token=PzSDPXX9cCJloTtgStM99dUBIk4fHTqLf0MNYFzWZydta6AZCZJI8muqAgrhqeMZ1oGTQTA-0BxiTCnjxD79a8qMuYoGyvD51Q7E0-N0zR0q3N8u-xEgePcMcJt1Z8OPwq-vGOeG2dOzg4rKfbGPERTrteSShJvPmMdCVUava2OrwN7BUU9Im71SilDFegrJkqnOvCyvqGGr5L6FK_aOWKEK7HWsyajFrOX_-TSiq3fcuZRG6YoRj9_Jr8jk3Xr7d0hvFT7yvPKC3RP2rhVTlSHpgU_FMfBtJHeE0iM9zYjk6hextm5UQQ1UmiGsmCHidCdNDLxonjU3aLnniypqPw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جی‌دی ونس، معاون دونالد ترامپ که روز جمعه در سوئیس تفاهم‌نامه پایان جنگ با ایران را امضاء خواهد کرد، گفته مفاد این توافق اولیه در یک جمله چنین خلاصه می‌شود که اگر ایران به تعهدات خود در چارچوب این توافق عمل کند ایالات متحده آماده فراهم کردن زمینه برای بازگشت این کشور به صحنه اقتصاد جهانی است.
آقای ونس روز سه‌شنبه در گفت‌و‌گو شبکه رادیویی سیروس ایکس‌ام گفت: «دونالد ترامپ هرگز نگفت که هدف اقدامات او به قدرت رساندن رضا پهلوی در ایران است. آنچه گفت این بود که اگر مردم ایران بپا خواسته‌اند و مقابل حکومت خود ایستاده‌اند، خیلی هم خوب است اما آنچه او می‌خواهد اطمینان یافتن از فعالیت‌های هسته‌ای ایران است چه از طریق دیپلماتیک و چه از طریق جنگ که خب در نهایت راه دوم روی داد». 06:21
معاون رئیس جمهور آمریکا همچنین تصریح کرد که خواسته منتقدان آقای ترامپ مبنی بر ادامه جنگ با ایران با آن چه دونالد ترامپ به مردم آمریکا همیشه وعده داده و قصد اجرای آن را دارد، «همسو نبوده و نیست.»
آقای ونس در این مصاحبه چند بار تاکید کرد که آنچه به لحاظ اقتصادی ایران از آن منتفع خواهد شد «به هیچ وجه» از منابع و دارایی‌های آمریکا پرداخت نخواهد شد بلکه در صورت همکاری ایران و اجرای همه مفاد توافق، آمریکا با رفع تحریم‌ها به سرمایه‌گذاری در ایران «فرصت» خواهد داد.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 363K · <a href="https://t.me/VahidOnline/76436" target="_blank">📅 03:05 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76435">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/cS9g7kqUcnnpf7bXF3UU6c1V_QF8l4s57UmmsxCSqAJ8jFhCQ27PuqLd5B21WAwTO-n2CxCXMCtmGrhmow7tHv-p8xTNCn0Mws_gIYXbPCrlsusPURZ22sRWeddMswkcwNeWS611R8IrjtcEkY_UJXc01TUb_NIQDUSkKajvkdeAJdj23_67CxZABXpWRH05-jfOoaZcDIblY7RafI-Iur2P3zHRIrQm7APNSuEgCLFtSRKLGRz5FhqRCCBNKo2G88Dms2P5xmHSG-1lgaQTvt6Yvb0UdKSh8Bz2SWbUGJTnFE_c2a8G_2RzQgUtrEB3RVmzzWvhqJQKITpsuBBb3Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تصویری که در شبکه‌های اجتماعی
منتشر
شد، دارا خسروشاهی، مدیرعامل ایرانی‌-آمریکایی شرکت اوبر، را در استادیوم سوفای لس‌آنجلس و در جریان دیدار تیم‌های ایران و نیوزیلند در جام جهانی ۲۰۲۶ نشان می‌دهد.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 370K · <a href="https://t.me/VahidOnline/76435" target="_blank">📅 23:24 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76431">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/aEx9eRNQhjb0SbTvIsZnV6Yx4TcwmILst3c030_4JAOIlTI19jQTiSpSQKK0VprfoyCkOrU3iczubgW0E28CuCJaZ15Kpcuy_f1mZvafEjsKjWTarrnh-wosXMdUlf5DDjnG_E8y5sTSsZDOX_m0cl1Q_JRmobCLzhX9UPdHVuY4kw07BiOv88NWSHNXIASx-rywbaLN1XaXanXfKt9T_LU6_KPRzfOSkItm3XOJrQpl4MbhxjX0UX0rpzMhmeBNMfmScX9932GD3F3fPwqB2e4ditB3f8M15s5VL8EnS4mFczWeITbzSNK4Ewu0MSgI7zT5Yyerf3_Hb9SJGCfrXA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/SzgThJsGw_XFvwSIXS38cBJWasIfaVqcKF3RWfRoG3q_XnftyirB69Mlu4u8xc2fz6-KkcGM_CvwuVIxRm3cpPBqXZjZaLDlsVyu8wARBwdMNVl6yeazqd-PT2x6Uoj-u6cEeCMS-KoKk0Da6hIGfAxbRBezhuK5ydAiNS9H1djpcAdDIMFd8zFLq45NMGazrE3kib3aeytRVcUB4DIPsT6mLP1_53esGv4YZK76kgZFwJ-6uG9BpN2hiST9E4iP6VCewCuZagusOcxCqW_HbKUsHFV204drIiorVFC_NCw_K8kbHE4sIPaVU6W61mPdzCmMW0apEBO1fXTNXy2wtA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/JcnUXxO-ttZrABSTdFEJP4ojAiAON-4mKN6YvK2dAJVRg1tlDcRSZFOZZI_f0lxYF_N0ziEvWAhynFZlWQfvr9t3JTub-gNvrYlxLGrzgW6TdhwaQJ4dLz0K1Xy9szMq6K8zsD7YAhDMX9fqWykYXz7RCwbI-VUtGKOuBQUrhlDNGndLvTr5jR6XhaGEptxSp7uEUbgbYN7IM5HSsdAoEt2ABQQToIkHtVYww4y2uJxhsNGXZ6MGEY9j6hULQI89Nr227E1xj-YP7Lw2zB6IjwVGy2ooBTfNYmh3GZIpEaKCXtkubfyI1oXHRycsUjeK1cyJZulfArGj0q8mxBqHZw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/57a8c06d44.mp4?token=r_PdveMM_T65yxgFW1fnigScDx0M2cnQaQERn6ZAaqjiz6EtbDpdps1ZNXdil-2I3K7qLAj17CMWyT0ixzTZCbFrGyMKYHbt4qdDiTyb37PbmECF86QzvELV87yqNavE6M0_gzZs2tsmVhztM-NHqPybzUA0QCyrQNCUfXWPav02ri827A8Rp6ylfoUhlFK5my8Nzu_iZRxO0mhhPHqmUK6lG0yF8hVDC3dYPDHeJHadx_COLm2p0wBOHZv7T6MDwfy211zwoVkhZMF7VeOyYX71tEWjG_Pi9MgWnrjHqVyceBI7sbYRdc-UMbNfrxd_qYMCHk3O7Kih96em-L5QRg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/57a8c06d44.mp4?token=r_PdveMM_T65yxgFW1fnigScDx0M2cnQaQERn6ZAaqjiz6EtbDpdps1ZNXdil-2I3K7qLAj17CMWyT0ixzTZCbFrGyMKYHbt4qdDiTyb37PbmECF86QzvELV87yqNavE6M0_gzZs2tsmVhztM-NHqPybzUA0QCyrQNCUfXWPav02ri827A8Rp6ylfoUhlFK5my8Nzu_iZRxO0mhhPHqmUK6lG0yF8hVDC3dYPDHeJHadx_COLm2p0wBOHZv7T6MDwfy211zwoVkhZMF7VeOyYX71tEWjG_Pi9MgWnrjHqVyceBI7sbYRdc-UMbNfrxd_qYMCHk3O7Kih96em-L5QRg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مکان جلسه امضای تفاهم‌نامه
ترجمه ماشین:
توافق چارچوبی میان آمریکا و ایران قرار است روز جمعه، ۱۹ ژوئن، در بورگن‌اشتوک امضا شود؛ نه آن‌طور که ابتدا تصور می‌شد، در ژنو.
این موضوع را وزارت امور خارجه فدرال سوئیس، در پاسخ به شبکه SRF تأیید کرده است.
وزارت خارجه سوئیس توضیح داد: «این مکان، یعنی بورگن‌اشتوک، از سوی میانجی‌ها، پاکستان و قطر، و همچنین آمریکا و ایران پیشنهاد شده است.»
به گفته این وزارتخانه، سوئیس زمینه گفت‌وگوها را فراهم می‌کند و شرایط دیپلماتیک لازم را ایجاد می‌کند تا این دیدار بتواند در سوئیس برگزار شود.
وزارت خارجه سوئیس درباره روند برگزاری و جزئیات امضای برنامه‌ریزی‌شده، اطلاعاتی ارائه نکرد.
srfnews
چت‌جی‌پی‌‌تی:
«بورگن‌اشتوک» به‌عنوان منطقه/کوه در سوئیس است، ولی مجموعه هتل‌ها و ریزورت بورگن‌اشتوک با قطر پیوند مستقیم دارد. Bürgenstock Resort Lake Lucerne بخشی از مجموعه هتل‌های لوکس سوئیس است که مالک آن شرکت/گروه هتل‌داری  Katara Hospitality مستقر در قطر است.
رستوران «Parisa – Persian Cuisine» در بورگن‌اشتوک نیز نخستین‌بار در سال ۲۰۱۲ در دوحه افتتاح شد و بعداً شعبه‌هایی در سوئیس، مراکش و نقاط دیگر پیدا کرد.
در ژوئن ۲۰۲۴ نیز بورگن‌اشتوک میزبان نشست صلح اوکراین با حضور ۹۲ کشور و ۸ سازمان بین‌المللی بود. در آن نشست هیأت‌هایی از اوکراین، آمریکا، فرانسه، آلمان و کانادا شرکت کردند، اما روسیه حضور نداشت.
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 381K · <a href="https://t.me/VahidOnline/76431" target="_blank">📅 22:40 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76430">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/WpASyBaIlX_Ht5U2nK41y4nj13WaxfhsbRxJg6wX7EjSx8Y7D3smJowiEdRRTdcCQOX7K4J8tuejVfHBWgYtbOnoRRm8IZQERa8bLRArdgwc1eRldofyxYKhpdXZUNVQD-NR1QhBQp6cwCSBZIcZfV6M_K5rf5LKtJVTdC2MXqDFO0ANrVOlqb8xBevHsoDhIhv6ye23enXfYGNpojFTSS6LzL1mP6DxR-c5UH2SXotIORBIMdBgMBayieiDwGbtIHuU1oRCrwPMEfss5IDQ8mTu61z5r-1clrNFRBFfu74dOPLymmCnDqd3JdlwV5TbnN3C0jK_zFGkdYJhdUbYoA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اختصاصی رویترز: منبع آگاه می‌گوید توافق ایران شامل یک صندوق ۳۰۰ میلیارد دلاری است که بیش از نیمی از آن تاکنون تعهد شده است.
ترجمه ماشین:
دبی، ۱۶ ژوئن، رویترز — یک منبع آگاه مستقیم از جزئیات توافق به رویترز گفت در توافق چارچوبی آمریکا و ایران، یک صندوق خصوصی ۳۰۰ میلیارد دلاری برای تحریک سرمایه‌گذاری در ایران پیش‌بینی شده و بیش از نیمی از این مبلغ نیز هم‌اکنون تعهد شده است.
این منبع که به دلیل اعلام‌نشدن رسمی این طرح، در حالی که واشنگتن و تهران آماده امضا در روز جمعه می‌شوند، به شرط ناشناس‌ماندن سخن می‌گفت، گفت هدف این صندوق آن است که برای هر دو طرف انگیزه اقتصادی ایجاد کند تا به یک توافق نهایی برسند.
مقام‌های آمریکایی و ایرانی روز یکشنبه گفتند که بر سر چارچوبی برای پایان‌دادن به جنگ خود به توافق رسیده‌اند؛ جنگی که از ۲۸ فوریه، زمانی که نیروهای آمریکا و اسرائیل به ایران حمله کردند، آغاز شد. این چارچوب همچنین شامل توقف محاصره ایران از سوی آمریکا و بازگشایی تنگه هرمز، مسیر کلیدی تأمین نفت و گاز جهان، است.
این منبع گفت صندوق جدید، یک ابزار سرمایه‌گذاری خصوصی است، نه برنامه‌ای برای بازسازی یا پرداخت غرامت، و هیچ پول یا کمک بلاعوض دولتی در آن وجود نخواهد داشت. او افزود شرکت‌هایی مستقر در آمریکا، کشورهای عربی خلیج فارس، آسیا، آمریکای جنوبی و آفریقا با تأمین مالی آن موافقت کرده‌اند.
به گفته این منبع، سرمایه‌گذاری‌های تعهدشده حوزه‌هایی از جمله انرژی، لجستیک، تولید صنعتی و حمل‌ونقل را در بر می‌گیرد.
یک منبع ارشد ایرانی به رویترز گفت تهران در ابتدا خواستار ۴۰۰ میلیارد دلار غرامت بابت خسارت‌های جنگی از آمریکا شده بود، اما واشنگتن گفته بود چنین مبلغی را پرداخت نخواهد کرد.
پس از آن، ایده این صندوق که قرار است «صندوق بازسازی و توسعه» نامیده شود، مطرح شد.
منبع ایرانی گفت سازوکار پیش‌بینی‌شده شامل مشارکت کشورهای منطقه به شیوه‌های مختلف است. این شیوه‌ها شامل تضمین وام‌ها، ایجاد خطوط اعتباری یا تأمین مالی مستقیم بازسازی مکان‌های آسیب‌دیده در جنگ، از جمله تأسیساتی مانند مجتمع فولاد مبارکه، پالایشگاه‌ها، فرودگاه‌ها و به‌طور گسترده‌تر زیرساخت‌های آسیب‌دیده از درگیری، می‌شود.
ایران، به‌عنوان یکی از بزرگ‌ترین اقتصادهای خاورمیانه، در چهار دهه گذشته تقریباً هیچ سرمایه‌گذاری مستقیم خارجی قابل توجهی جذب نکرده و به دلیل موج‌های پیاپی تحریم‌های آمریکا و تحریم‌های بین‌المللی، از بازارهای جهانی سرمایه کنار گذاشته شده است.
این کشور دومین ذخایر اثبات‌شده بزرگ گاز طبیعی جهان و چهارمین ذخایر اثبات‌شده بزرگ نفت جهان را در اختیار دارد.
ایران همچنین جمعیتی جوان و تحصیل‌کرده با بیش از ۹۲ میلیون نفر، پایه صنعتی متنوع و ظرفیت‌های بکر قابل توجهی در بخش‌هایی از پتروشیمی و معدن گرفته تا گردشگری و کشاورزی دارد.
این منبع گفت صندوق سرمایه‌گذاری کاملاً جدا از مسیر موازی مذاکرات درباره رفع تحریم‌های آمریکا و آزادسازی دارایی‌های حاکمیتی ایران است که در خارج از کشور مسدود شده‌اند. او این دو را سازوکارهای مالی متمایز با اهداف و جدول زمانی متفاوت توصیف کرد.
این صندوق تا زمانی که یک توافق نهایی و رضایت‌بخش حاصل نشود، ایجاد نخواهد شد و عملیاتی هم نخواهد شد. تفاهم‌نامه، پس از امضا، قرار است روند را طی ۶۰ روز آینده ساختاربندی کند.
این منبع گفت: «این صندوق فقط زمانی ایجاد می‌شود که توافق نهایی امضا شده باشد. در طول این ۶۰ روز، مدیران صندوق با ایرانی‌ها و سرمایه‌گذاران کار خواهند کرد تا پروژه‌ها را برنامه‌ریزی و محدوده آنها را مشخص کنند.»
وزارت خارجه ایران و وزارت خارجه پاکستان، که به میانجی‌گری در توافق مربوط به صندوق سرمایه‌گذاری کمک کرده بود، بلافاصله به درخواست‌ها برای اظهار نظر پاسخ ندادند.
یک سخنگوی کاخ سفید به مصاحبه روز دوشنبه جی‌دی ونس، معاون رئیس‌جمهور، با شبکه سی‌بی‌اس اشاره کرد که در آن گفته بود ایران در صورت پایبندی به توافق با واشنگتن، از جمله برچیدن برنامه هسته‌ای خود، حذف ذخایر مواد غنی‌شده و پذیرش یک رژیم سخت‌گیرانه بازرسی و اجرای تعهدات، می‌تواند به یک صندوق بازسازی ۳۰۰ میلیارد دلاری با حمایت کشورهای خلیج فارس دسترسی پیدا کند.
این منبع نگفت که صندوق چگونه یا توسط چه کسی اداره خواهد شد و یادآور شد که جزئیات کلیدی هنوز باید نهایی شود.
این منبع از شرکت‌هایی از کره جنوبی، ژاپن، سنگاپور، مالزی و آمریکا به‌عنوان شرکت‌هایی نام برد که تعهداتی داده‌اند، اما از ارائه فهرست کامل خودداری کرد.
تفاهم‌نامه ۶۰ روزه یک چارچوب است، نه توافق نهایی، و انتظار می‌رود مذاکره‌کنندگان آمریکایی و ایرانی در این دوره روی مسیرهای متعددی کار کنند که مسائل هسته‌ای، تحریم‌ها و امنیت منطقه‌ای را در بر می‌گیرد.
reuters
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 330K · <a href="https://t.me/VahidOnline/76430" target="_blank">📅 22:23 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76429">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/vrZj-TfmjN6ZbeLnmJsUvmcn6t-bGfeARrRFZ3PN7_yv1Ogogib-THZYcnoTjnNyOj3ZUFDw_WqM-GEKlsoeHazrqKBj7IoUvN4erL-hlm7YkFdtC-cCpbtcUntajFwyP5zYhT0d3t0R5_2LEsptaPJOXZaFmcwvLrsDDGAG84O1gtpAOayfQP7MPU67NPsx6AY9KCyPFBQDWwKn3hUt2KMhrEfBtK67jbHP9PNk5ixs1X1Tg8VyWqgdnE8lFtOaWrlGoZsPDnoFTh5GkyV2AeU_JPAU3V6YAsclkfD986Sv0q0nsaIKXM-56Vxyws8xrNH7HPWijugwHXgVEM2tXg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در پی حملات روز سه‌شنبه ارتش اسرائیل به جنوب لبنان که چهار کشته به جا گذاشت، قرارگاه مرکزی خاتم‌الانبیا تهدید به پاسخ کرد. این حملات بعد از اعلام توافق ایران و آمریکا انجام شد.
قرارگاه خاتم‌الانبیا که وظیفه هماهنگی میان نیروهای مسلح جمهوری اسلامی را برعهده دارد، در بیانیه‌ای اعلام کرد که اگر اسرائیل به حملات خود در جنوب لبنان پایان ندهد، باید منتظر «پاسخ سخت» نیروهای مسلح جمهوری اسلامی باشد.
در این بیانیه ادعا شده که در پی اعلام نهایی شدن تفاهم پایان جنگ توسط دونالد ترامپ، ارتش اسرائیل «۸۴ بار» آتش‌بس در جنوب لبنان را «نقض کرده است».
لبنان ساعتی پیش اعلام کرد که حملات اسرائیل در جنوب این کشور چهار کشته بر جای گذاشته است؛ این در حالی است که اسرائیل گفت چند راکت شلیک‌شده از سوی حزب‌الله را رهگیری کرده و حملاتی را نیز انجام داده است.
خبرگزاری رسمی لبنان گزارش داد که پهپادهای اسرائیلی دو خودرو را در شهر میفدون و یک خودروی دیگر را در شهرک نزدیک شقین، هر دو در منطقه نبطیه، هدف قرار دادند که «بر اساس آمار اولیه به کشته شدن چهار نفر» و زخمی شدن تعدادی دیگر منجر شد.
ارتش اسرائیل اعلام کرد که پس از آنکه «یک خودروی مشکوک» را در منطقه‌ای که نیروهایش در آن فعالیت می‌کردند شناسایی کرد، حمله‌ای را در جنوب لبنان انجام داد، اما محل دقیق این عملیات را مشخص نکرد.
ارتش همچنین گفت که نیروهایش چندین راکت شلیک‌شده به سمت نظامیان اسرائیلی در جنوب لبنان را رهگیری کرده‌اند و در پی آن، نیروی هوایی اسرائیل سکوی پرتاب این راکت‌ها را «هدف قرار داده و منهدم کرده است.»
@
VahidHeadline
📡
@VahidOnlinene</div>
<div class="tg-footer">👁️ 305K · <a href="https://t.me/VahidOnline/76429" target="_blank">📅 22:16 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76428">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XiVfGWhZydYcxBsNsOyQZQgAe2KBC-FNZJj8Tq0nFPqJ03bvl91M4lSwNbODbh6CFLiNN1KVbcWfyDQgy2czFR7PTAIxFQUD4KWQxVWtQoqVcGGeVnnHXVIRR8_eBCFebkk2KA79Qug_g_Eu0JfZMSCWWE_HN1rdFqz844n4Ag4bfjBHIAXfS5xY-YtQmPj4Il-jEvaFOU2QmYtmFR1TpLN3FaiP6yJw5HJ8n0nbDslQu2VxVDSKxd_KL2_y7TmNSK9VUj9rtL0AmnbQeM_9xdU5Dwu3MXGRil17MJqwrG9IUHGwket9ZeYq3sTTu4nCwidQ_l90RQw0_6COYs5AAA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">طیبه نظری مکی آبادی، مادر دادخواه مریم آروین و از بازداشت‌شدگان مراسم هفتم خسرو علیکردی در مشهد، از سوی دادگاه انقلاب این شهر به پنج سال زندان محکوم شد.
بر اساس حکمی که در تاریخ ۲۳ خرداد از سوی شعبه اول دادگاه انقلاب مشهد به ریاست قاضی غلامرضا اکبری مقدم صادر و به این شهروند ابلاغ شده، او بابت اتهام «اجتماع و تبانی علیه امنیت کشور» به چهار سال حبس و به اتهام «تبلیغ علیه نظام» به یک سال حبس محکوم شده است.
طیبه نظری، مادر وکیل جوان، مریم آروین است که در جریان اعتراضات «زن، زندگی، آزادی» در سال ۱۴۰۱ در سیرجان به دلیل دفاع حقوقی از بازداشت‌شدگان دستگیر و مدتی پس از آزادی موقت، به طرز مشکوکی جان باخت.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 323K · <a href="https://t.me/VahidOnline/76428" target="_blank">📅 20:49 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76427">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GzaPJe2q4CqHuIon1FfhbDp5ABIDq1TpwSTP8QmlAinNLH3sAHH6f3E9WGbNUQ75bbWGV-mDoNAhKc8T_m9qXgcJVZLdUXHL12CAeSUbkMpHH9ocXGPmto_UhMn5vRnEkJGiUn8ppPSxUrmuzbqrYPbbRh8kNHZoCjp3Sgdl0QgXhDh3FqGGMIda_ocSq_KFlGWOXO4an5-S0zrHs6pn_diITduFOPpUFdZfoA-4MFHhZPRoCWF5NcyTUJM6iKhIutJHk1d8ovlHPaaAMaNyS47knB4hju04h_L-uM0Lbe7aKcPEKjrulUCgcR3_NiT5bvN3tfAc6YUYB5HV-sQf3Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">روزنامه وال‌استریت جورنال و خبرگزاری رویترز روز سه‌شنبه به شکل جداگانه و به نقل از منابع آگاه گزارش دادند که یادداشت تفاهمی که ایران و آمریکا به آن دست یافته‌اند، به ایران اجازه خواهد داد «بلافاصله» فروش نفت و دیگر فرآورده‌های نفتی خود را آغاز کند.
منابع این دو رسانه گفته‌اند مفاد مربوط به لغو تحریم‌های فروش نفت ایران پس از امضای توافق در همین هفته اجرایی خواهد شد و خدماتی از جمله بانکداری، حمل‌ونقل و بیمه را که برای تسهیل این فروش‌ها لازم هستند، در بر می‌گیرد.
وال‌استریت جورنال به نقل از این افراد گزارش داد که با اجرایی شدن این یادداشت تفاهم، موانع ناشی از تحریم‌ها بر صادرات نفت ایران و خدمات پشتیبان مرتبط با آن برداشته خواهد شد تا امکان انجام این معاملات فراهم شود.
یک مقام آمریکایی نیز در گفت‌وگو با رویترز تأکید کرد که این توافق دارای شروطی مشخص است.
او که به شرط ناشناس ماندن صحبت می‌کرد، گفت: «این یک توافق مبتنی بر عملکرد است. ایران تنها در صورتی می‌تواند از مزایای این یادداشت تفاهم بهره‌مند شود که به تمامی بندهایی که با آن‌ها موافقت کرده پایبند بماند؛ از جمله نداشتن سلاح هسته‌ای، خنثی‌سازی مواد غنی‌شده خود و عدم مداخله در جریان آزاد کشتیرانی در تنگه هرمز.»
یادداشت تفاهم ایران و آمریکا که ۲۴ خرداد به صورت الکترونیکی امضا شد، قرار است روز ۲۹ خرداد در سوئیس با حضور مقام‌های ارشد دو کشور به شکل حضوری نیز امضا شود.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 324K · <a href="https://t.me/VahidOnline/76427" target="_blank">📅 20:48 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76426">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gfvPhZYVQw6Xueh8HcP_PbFUpbUo2NhaR89HnNu-NQgdtnho--iuu_tNY8GT2O4MHjExPkYo_Gu6abOoDWEvfnbfkD39-P_3j3XuSHUdECWcuqo6ozliFcaebk3GkXc-KC60wN1ZXM77N6Y2m-Izg2oPAPPAxWtTHSDz1bg6CTZM8avGoveghVQR9RDKUgq1kKHjusLbVnkOHvqG45SbRmHDBKL8s8ueVdTOsuV8816-jTzdzYcPHTfPxvgjGqlYsflXq8aJOb4f8ywD3LURaUyPWV0luttm9zax2SMTZjdVYnFqwO_Iqdl7soJM35DKST6sm0wAoYGNoWfu4afdfQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در پی
آن گفته ترامپ
:
لیندزی گراهام، سناتور جمهوری‌خواه آمریکا، در شبکه ایکس نوشت گسترش توافق‌های ابراهیم و ایجاد ثبات و رفاه در خاورمیانه یکی از مهم‌ترین اهداف دونالد ترامپ است و این هدف زمانی محقق می‌شود که جمهوری اسلامی تضعیف شود یا رفتار خود را تغییر دهد.
او افزود که امیدوار است مذاکرات پیش رو برای پایان دادن به برنامه هسته‌ای ایران موفق باشد.
لیندزی گراهام اضافه کرد: «جمهوری اسلامی و نیروهای نیابتی آن به‌شدت تضعیف شده‌اند و توانایی آن‌ها برای رقم زدن رخدادی مشابه هفتم اکتبر دیگر وجود ندارد.»
او ادامه داد: «اگر درگیری با جمهوری اسلامی به گسترش توافق‌های ابراهیم، همگرایی منطقه‌ای و صلح پایدار منجر شود، این نتیجه یکی از موفق‌ترین عملیات‌های نظامی در تاریخ آمریکا خواهد بود.»
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 325K · <a href="https://t.me/VahidOnline/76426" target="_blank">📅 18:52 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76424">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromﻣﺎﻧﺎ ﻧﻴﺴﺘﺎﻧﻲ Mana Neyestani</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/lNweZSksB8hdjw2akuULntol7J3yX5sV_td_ixP-wsRoqjDXKKNbTol8sMgINFnDae0LhW_7IQzUljMV39xqxzk94Z4q-KBf1Cvs-SL0paJeMYGsyNB3hnws9kafDNKLIRaN4_il7z2VA_bGon8dQQTxZjiolF33RuepSfcp-GFqTG1_7i1Tw-PwLp8eRxQaJ0zr80z4dgHRgsu1rDdxMyY5SEcyM0KbC97LZYsZuKz1VaB94qg4MZW1DxfkKxNKbjmrc5X2uY6FMtG52GH4RbSTnngDi400KCgchObcDxh8ZmSeQonmHEixBvidkEvWSSCErDApKZhMaLwp_oeKmw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/NHCIJ9kkPIK9-dZ63m9gD2axTkv8EievOXZ7zSTo9CoKyZsNKiR3IOAFqnc5kHsdyKjWyWh0jyZdyjQT2jdveEBd45xcq-b0O9Kzqkk-y2H6Hln8ka-6QOoAx3zVpIh6ZgfFtdaLnrdf5fFYa_a_XLMLdoT83g-0XHSrR2Qr8JJqPKkVC6Rir0WvXWc-4sCG8vDbhaiRbbza8pPwx-6qN1UEE3ZMUWYbhQsvAFkhqoL14V_38RJNWxZ8ngJhqdITT56tSlxWBeePKUaSMuWxT4c8atldjxnwxegymV_EhLcdhEwwoH6jb6ElEiHoXUJgN0_2-4EuZRUiNfPbWr4Q7A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">پهلوان سازش ناپذیر
@mananey
مانا نیستانی</div>
<div class="tg-footer">👁️ 312K · <a href="https://t.me/VahidOnline/76424" target="_blank">📅 17:16 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76416">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/g8rQd4Pf3DnQ8bBYxgYPXCdI8bpmrVnnmz2bMP273GsGqezOWn_BFVFq7HjcQjE3hBkCrg-DgjALtALA7UBTQSPjlW9UEY4H75eWaZ4SxghqB3na0o0RVWj-GSX_44rZe9BIGfTFRnolHk6NiR4Af_keweRkE6rrAfPi_VWjc16_oG6052mhD41wlBQR97UIcCxxWskZI6TiFKuYQR8DAhfNR6eIMZTOSb1QE3UoWFad7gO3IWhjUPpzalymRz_NbrOcSnHzZBAwxEQ_OO5MunG2jNsuh1XD_yDAVj-2HM4kKpAkJliWwyU9SZinhB4OTK6g44r-HFBMuvoCbfFtGA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/sy8WEArwIZmRkWh1XmM2_pZG8BxJlDnVO-iktdz17KLAUq3QMqWbSK9JPfc_dCJi-br6zllds-cqR3Y5sJF2HrefGMJrZjuSw_H0qNdFQq-Qzwtj14xhEMOZxYXEDbZmQMXdu20R4iCNQDYxx3bXEneh2skpeICzY1Orey-HkxmRm0iSVesvEj-rnaaSiZb_YbOD_dwkHbtODD6QAE5c6y9E5-jJhha3oddsAyutqjpf4--9DVrhxTWto1RViTdaN9rFfDE8CBjqpy5ReJVwIxLCN3dG55G0VfbiSXCv4QdHRrkRuM0-UNQovqeEuNUaK3W14mNOalBD3u4ocAeZLg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hb-sIv2VS9csjjO0dnCtddip1hrM6HBEGHoPTGYjDgETnwoQ98_I5wLNXL6-sFRJW86_k_FvI4nksXHeG0dh5KzqySRYQD6dD0MKFUZSH0DCNP6eoQgb5ngKYqV1h3dtpt9UMLrvz-mdabBWGUhBI3s_4rC_sWr0FknLA5xRVFTUejrjKZOojdsnUUg6kfdqCBLn5JCfxUXpeK9Nksl7zyFD9uXT6dH-tUrRjOZR2ENOuwDu7f77ZqBACuXJkUehiL8wsyk-eRnH8rtFnJrcNhqpiTGAR9U2ceuQaeBtaTD839KXQs-wGtbbIVc5V6oWaA3aJ6JlmZT-98S2SpLf6w.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/faa23faa31.mp4?token=AIn5kmkeHfuJ2NHszDmZIZrlfcb_2L4JoxPX0UbDNJmN0bnvYJMLEfw3CPaIxaBNIDF8K8EdaO2n8ggf_LZnN_zqExI-Rub9jilCGp3c5esySx8EZzbWNQjzT2ohPgfnHjjUBK9znTWApYGEhmfhmmZ0jjUvc7xJg-H9WBGBBx0GJlCilsGLOxQmawTdLBJ2WAu4x1PF25OQzF5HZe9YmX5pv7XXQGFdLf7VSjxSG-UmuYXHiZZd_qvRBAfAG8WXHojIkknZgVp2Uyjwq3LkLBENhim2eqj9da5QPjMmNHQaJP0cfbWvqsztnt4QtUokTgwS2urta2gc3JdnClUBBw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/faa23faa31.mp4?token=AIn5kmkeHfuJ2NHszDmZIZrlfcb_2L4JoxPX0UbDNJmN0bnvYJMLEfw3CPaIxaBNIDF8K8EdaO2n8ggf_LZnN_zqExI-Rub9jilCGp3c5esySx8EZzbWNQjzT2ohPgfnHjjUBK9znTWApYGEhmfhmmZ0jjUvc7xJg-H9WBGBBx0GJlCilsGLOxQmawTdLBJ2WAu4x1PF25OQzF5HZe9YmX5pv7XXQGFdLf7VSjxSG-UmuYXHiZZd_qvRBAfAG8WXHojIkknZgVp2Uyjwq3LkLBENhim2eqj9da5QPjMmNHQaJP0cfbWvqsztnt4QtUokTgwS2urta2gc3JdnClUBBw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ که پیش‌تر در پیام‌هایی خطاب به ایرانیان از «کمک در راه است» سخن گفته بود، اکنون در گفت‌وگو با مقام‌های قطر، کشته‌شدن معترضان را عمدتا به «گروه‌های قبلی» در جمهوری اسلامی نسبت می‌دهد و میان بخش‌های مختلف رژیم مرزبندی تازه‌ای می‌سازد.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 332K · <a href="https://t.me/VahidOnline/76416" target="_blank">📅 17:07 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76415">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/0db862b726.mp4?token=YVl4UcmqHJv5TPg1dOxbN_kreXXRdIHmS5vLYSuGk5xh1GY7EkMCXOG1d9qPP6qBJ3MdaNGxNqweqC0qDRNkZn9tFge0BJDKJkVfiZ7bj_yikIPkvXfi_GncjtAC05Tkb58eMYRKAqvmo8JPZnmdjJml4hDEFv7m1DfjSN2zETQ-l_1zpe2LpEiWPOJTvs05UcjDSJE5tMi8y2CanPTu9k1CHtwLQxiAxvOJK-dglc4WLXQSNGkoto8gagaoyPJ9cJJQUKZnd4CxdExTg9IWf3Q2ADBDRkY-BCimrY-h0uVgK4RnBAraNMGmGib8fyAoUc-9cYJOgdl51RGkzVN6Wg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/0db862b726.mp4?token=YVl4UcmqHJv5TPg1dOxbN_kreXXRdIHmS5vLYSuGk5xh1GY7EkMCXOG1d9qPP6qBJ3MdaNGxNqweqC0qDRNkZn9tFge0BJDKJkVfiZ7bj_yikIPkvXfi_GncjtAC05Tkb58eMYRKAqvmo8JPZnmdjJml4hDEFv7m1DfjSN2zETQ-l_1zpe2LpEiWPOJTvs05UcjDSJE5tMi8y2CanPTu9k1CHtwLQxiAxvOJK-dglc4WLXQSNGkoto8gagaoyPJ9cJJQUKZnd4CxdExTg9IWf3Q2ADBDRkY-BCimrY-h0uVgK4RnBAraNMGmGib8fyAoUc-9cYJOgdl51RGkzVN6Wg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دونالد ترامپ، رئیس‌جمهوری آمریکا، در حاشیه نشست سران گروه هفت (G7) در اویان فرانسه و در دیدار با امیر قطر، از رویکرد نظامی بنیامین نتانیاهو در قبال لبنان انتقاد کرد.
ترامپ با اشاره به حمله هوایی اسرائیل به بیروت، درست دو ساعت پیش از امضای توافق آتش‌بس با جمهوری اسلامی ایران، آن را «کور و بی‌هدف» خواند و گفت: «به آن‌ها فهماندم که اصلا از این کار راضی نیستم. برای کشتن یک نفر لازم نیست یک آپارتمان را با خاک یکسان کنید؛ آدم‌های زیادی آنجا هستند که همه‌شان حزب‌الله نیستند.»
رئیس‌جمهوری آمریکا با بیان اینکه اسرائیل زمان زیادی است که با حزب‌الله می‌جنگد و افراد زیادی کشته می‌شوند، پیشنهاد داد که کنترل این گروه به سوریه واگذار شود.
ترامپ با تمجید از عملکرد احمد الشرع، رئیس‌جمهوری سوریه در ساماندهی سریع این کشور گفت: «او با مشارکت من و اردوغان روی کار آمد. او از حزب‌الله خوشش نمی‌آید و این کار را بهتر انجام می‌دهد؛ اگر اسرائیل نمی‌تواند بدون کشتن دیگران کار را تمام کند، سوریه این کار را خواهد کرد.»
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 284K · <a href="https://t.me/VahidOnline/76415" target="_blank">📅 16:54 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76414">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Xuh2Lc5J0EtStkrktC-yRHmivwVih8cgX6aZFO1Gyd7thAmuvDXqCy4f97Lccx6IE2u8GhxMxD1NWYkxTVcnR1dBqE87u9SAO_mTW8X8_dtF7Qmy7BTlExa0K9P-ul5AGhtmEMITNQrL0X3dz8q5mxWs4gZH9V5y3PVQq4m8FNpvvwB97zBjPwdQf-IAO-PFawL07_DoDcIQF1lCudw1LFHnCWOGaWuf4NqmawC43Vkq6dmSxVKYPZwoS4qtdU__6lyWO3UxPVKoSX7xNaelkBMDppvpnYfCMzFrChwj_OlUggO6JQ1BHysyr6VflLdw2xxvlbp7vgfyT1-4Gjk_GQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دونالد ترامپ، رییس‌جمهوری آمریکا، در پاسخ به پرسشی درباره متحدان او که نسبت به چارچوب تفاهم با جمهوری اسلامی تردید دارند، از جمله لیندزی گراهام، سناتور جمهوری‌خواه، با لحنی طنزآمیز گفت: «لیندزی تردید دارد؟ باید با او صحبت کنم؛ دچار دردسر بزرگی می‌شود.»
ترامپ سپس تلاش کرد نگرانی‌ها در میان هم‌حزبی‌های خود را کم‌اهمیت جلوه دهد و گفت گراهام «آدم خوبی» است و مشکلی با این توافق ندارد.
او افزود: «این توافق یک موضوع مهم را به‌خوبی پوشش می‌دهد. ما بابت آن هیچ پولی پرداخت نمی‌کنیم.»
رییس‌جمهوری آمریکا ادامه داد: «بازارها اکنون نسبت به زمانی که کار را آغاز کردیم در سطح بالاتری قرار دارند.»
ترامپ گفت: «اختلاف فقط بر سر یک موضوع است؛ این‌که ایران هرگز سلاح هسته‌ای نخواهد داشت؛ هرگز، هرگز و هرگز.» او افزود: «بقیه مسائل اهمیتی ندارند.»
@
VahidOOnLine
آپدیت:
توییت گراهام
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 267K · <a href="https://t.me/VahidOnline/76414" target="_blank">📅 16:53 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76412">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/AxXq5n_JQ0OsnNaOBDIK4aAUDCQ3M-724vHcLONMfp-0hCDdmFEB0k0OK_Bw4hCuzNXuNJYYvzVYii0zgCwJTXuv7bIntZbtXkKW2DqysaGZ8f2RPFY46l5jR4CiJLof25nOjZq5BBXLsMBtwcqrEAvEKZhDP7m10wC69GhqJoQ8OBQAXix3Iu7x9s2txS6HMHFauuI5e8jZGijddR5zXg5EL1OlbJBKT1r-ZDtdyqstmtCzytAmZD4XujIdAgk4xLiV85Y2piQoLKVhUtX9Gr-kPHPj6wI50TA_XP-fLSR4VSnyKke4qOn_x6qP6Dig3YDziqrYXify1WFN-wXZlA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/Mzg_WvDTEqeUSol01hU9zkCgLkk865_EJg30KgP3WeZtnYbMaczj3HTwY_4BI4WHGDTN_HkIEN2xadBj39pxSqd_ms0E2pGpa03CaBBm5s3K2-hXZ-sUSloRGkYk6ePYFiDqhlWFw8w1VEf_I5S7ZQWNBrnx9eNUVY9CSosZp2s57ZjJ0DzzmFwjn9EE9tKBLel8sDmGagPSH1wz61TtbVaX1savIjqg3ZVYJsHdLavGyvzxZuDltbsCL4wMdH_1xrE6xNo0yfH0NsqSoenI19OUSwZDG7Mkn_B2TtvH5awl9ZSTdmWb1n28JFmt0kt3CfNHaIBv6G72DID1MJstLw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">پیام‌های دریافتی درباره دو پست قبلی
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 250K · <a href="https://t.me/VahidOnline/76412" target="_blank">📅 16:44 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76411">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ig1504zUQXSiOmcFiNlccZ3rnf4HXH3ky0s-ydD2ZqzVCrSu9BeYLoPu-PKKtHJYPwKfXfBUjuZiWcyUgacEhys-lZnGXOOrxlRG5e1hAiLxNKE_LpQnmb8JF4FSE5JtTDDCqcnapB0b_P_pSMNcQP7Y4TPW3XGFGdfab0vCcreVDfscfxlAw_GEXhWdUOvMLWL-SFFwXl3ZdlHZhXk5QfcamUxeJpmE5meh9Qydzq6dZ-3fGGLKYD3CY-9WE3Ji57kKx3xN_t_oc-XZrqLjOownJiXS7KzIUCKMqowSfLNyDAu4BtlocXstdcmZkEv1XaEzQCKZOcxBuo-yujqkJQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دونالد ترامپ، رئیس‌جمهور ایالات متحده، روز سه‌شنبه اعلام کرد توافق صلح با ایران را برای «بررسی» به کنگره آمریکا می‌فرستد.
او در جریان دیدار با محمد بن زاید آل نهیان، رئیس امارات متحده عربی، در حاشیه نشست گروه ۷ در فرانسه به خبرنگاران گفت: «هرگز به فرستادن آن فکر نکرده بودم، حتی یک بار هم به آن فکر نکرده بودم، اما این کار را خواهم کرد. آن را به کنگره می‌فرستم. از این ایده خوشم می‌آید.»
برخی قانون‌گذاران جمهوری‌خواه پیش‌تر خواستار بررسی متن این توافق شده بودند.
آقای ترامپ همچنین وعده داد که متن توافق با ایران را «ظرف یکی دو روز آینده» به‌صورت عمومی منتشر خواهد کرد و حتی این احتمال را مطرح کرد که کل سند را در برابر دوربین‌ها قرائت کند.
او گفت که منتظر فراهم شدن یک «فضای رسمی» برای انتشار عمومی این متن است.
رئیس‌جمهور آمریکا اعلام کرد: «دوست دارم ابتدا یک چارچوب رسمی برای این کار فراهم شود، اما هیچ مشکلی با انتشار آن ندارم؛ این یک سند عالی است.»
او در ادامه افزود: «محتوای آن این است: ایران هرگز سلاح هسته‌ای نخواهد داشت.»
ترامپ درباره مرحله بعدی مذاکرات با ایران که برای آن مهلتی ۶۰ روزه تعیین شده است، گفت: «فکر می‌کنم این روند خیلی سریع پیش خواهد رفت.»
او افزود: «ایران می‌خواهد این موضوع را نهایی کند. آن‌ها باید به فعالیت‌های عادی خود بازگردند و روابط اکنون عادی‌سازی شده است؛ بنابراین فکر می‌کنم این روند خیلی سریع پیش خواهد رفت.»
ترامپ در ادامه گفت: «ممکن است سریع‌تر پیش برود، ممکن است هم زمان بیشتری طول بکشد، اما می‌تواند خیلی سریع انجام شود.»
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 273K · <a href="https://t.me/VahidOnline/76411" target="_blank">📅 16:38 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76410">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/pmMoNqZ5WEAEZSL1GankLbcV6QrzY2Ccq4mhRzv6di4yFGtzsHODDG_XqSchtzlRQUmcpdmpoKfwnwK82QDuLNwKKlxUAqE8fCcS4qkMHiWaX0oioD9KjncMnGMaUmt8dpBSXUrYve6AwQzHhjTvuC0yTLoLSrrHG_ripMxIjFTOEAUkwU8_Eq7YPoomkFv8qLU4XQz7GoqbLbYd5yatsHodzq9t9eYepiYvpBPPfwziALED0UxvBJz_b4_GwtgaivRRrVyANPU1gWGB91Hoh__jz7VUnwN8AcQVlvEYTV3-xoo_a-UxyufbD1pepvsHAtqr17FDOvS3uvuSxJ2bfg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قوه قضائیه جمهوری اسلامی اعلام کرد که روز سه‌شنبه ۲۶ خرداد دو نفر دیگر از معترضان دی‌ماه پارسال در شاهرود اعدام شدند.
خبرگزاری میزان، اسامی افراد اعدام‌شده را جواد زمانی و ابوالفضل ساعدی اعلام و گفته است که آن‌ها به اتهام «محاربه» و «افساد فی‌الارض» اعدام شدند.
این نخستین مورد از اعدام معترضان در ایران پس از اعلام توافق تهران و واشینگتن برای پایان دادن به جنگ ۴۰ روزه است.
در بیانیه رسمی قوه قضائیه، از قول محمدصادق اکبری رئیس دادگستری استان سمنان ادعا شده است که افراد اعدام‌شده «اقدام به تخریب و آتش‌زدن اموال عمومی و خصوصی، حمل و استفاده از سلاح سرد و گرم و اخلال در نظم و امنیت عمومی، اجتماع و تبانی علیه امنیت کشور و سایر اقدامات مجرمانه» در شهر شاهرود کردند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 354K · <a href="https://t.me/VahidOnline/76410" target="_blank">📅 16:22 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76408">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/up6z8r--O2uH37fEWUPZNdpca7f3Kw6SdV_AM4k49tUjm4LNMrF9od_2AndguppV0qGSjcnbUXDYjjqhF6apGA9MtxlhT7KOVww4JoirUc2VP5rk3JAP6KrCAuWkflnpGs4-2reJi8JNgMQX6opzWTwUqgeqafWkgY6lgL_NsFdx7s-MQn7aY9iAZHsSFcUhy804fq6O2H322511tdnmAf88-HwbqigMuVtZ3Lg9_jRIR6p0UD_xTI4aWcCwBBKpGEC0qCWEQcQZm9MmnM6bW3_PFiQZ-TElx2Zm1MunymABahXPzfu3a-g9Lq7kfsBibqH2C3jVh1lNklRJuHl7bQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/L7ifM49kYSO8nxVXjPjVLzMgZs3q2skPciAyWmOijLjOFymmkiUVoPn7h_2Tc71-DrKwyqSlCKwcbs8ltRpkP4y3b5mnxCoPJ0hYPl-akJP1OiirKRLdQl1Vr8k0S_s_dGtsUyrWYhzH7s1B5VBHbaka8kxYBR7DBxtLJOm20L4JWToL-eMT1_l5PjRn3pMDkkF16untpAdMscLq5NudM_cxtwGu-M2lFujPj2MUq5qhUhpoEOodUjeACS3lq_HXRz27--QwqoYhVPUeAKqjQxdqE30ivzzq2tdKveJS8a2yOOGyVn3h79dA1JGW7GGu-wDTxDIF3HqzdjKmLtYtbw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">مسابقه نخست تیم ایران در جام جهانی ۲۰۲۶ مقابل تیم نیوزیلند با نتیجه ۲-۲ پایان یافت.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 406K · <a href="https://t.me/VahidOnline/76408" target="_blank">📅 06:51 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76407">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/d6aa89bbb6.mp4?token=HMhm5r8M09zM3CTVNjLHWNbwxJ4A2_iTfQN75eYi5COqTFhHN1_AK23te-RvjXTvBE7J7gBp8xrvAhkFtRtXVjuF8PrYPegg6fq-tKOTXt7pV1DpyGczh9i89ByPaTlpx4ybOlYcFO1HZUMXdVYaoXDhN4IE4C-tAub7XpkRbRN44JE1PDEuMmyFwXOKs9kU-gHXIdQeigPjgVKoFOIGkNYNSoAqFdDqhgMTHYTlVfOAuvprsJRMYW7yMCQmtFzKtSIzQAMfuVsQetmBM9SLxMVkaTCoojMVXzrxmXgebB6JLS9w4N5-Gb42OOTZFOWM5H7dlwQ8oMPHbHoNlYIdug" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/d6aa89bbb6.mp4?token=HMhm5r8M09zM3CTVNjLHWNbwxJ4A2_iTfQN75eYi5COqTFhHN1_AK23te-RvjXTvBE7J7gBp8xrvAhkFtRtXVjuF8PrYPegg6fq-tKOTXt7pV1DpyGczh9i89ByPaTlpx4ybOlYcFO1HZUMXdVYaoXDhN4IE4C-tAub7XpkRbRN44JE1PDEuMmyFwXOKs9kU-gHXIdQeigPjgVKoFOIGkNYNSoAqFdDqhgMTHYTlVfOAuvprsJRMYW7yMCQmtFzKtSIzQAMfuVsQetmBM9SLxMVkaTCoojMVXzrxmXgebB6JLS9w4N5-Gb42OOTZFOWM5H7dlwQ8oMPHbHoNlYIdug" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جی دی ونس معاون رئیس‌جمهور آمریکا ویدیویی منتشر کرده:
رئیس جمهور از روز اول صریحاً گفته است: ایران هرگز سلاح هسته‌ای نخواهد داشت.
بار دیگر، تلاش‌های رئیس جمهور ترامپ برای برقراری صلح، علیرغم تلاش‌های بی‌شمار افرادی که از آمریکا و رئیس جمهور ترامپ متنفرند، برای مردم آمریکا نتیجه داده است.
JDVance
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 403K · <a href="https://t.me/VahidOnline/76407" target="_blank">📅 03:54 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76406">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Bgg1SPggmUqTTgwwhhNFqu0oyMfCCwk3Rv0-exWkj8bOFrblUtPwKCZ7Cshst2kLIXz78iS7SqvD9KQzpNiVBnst9TqzdvWV7G1j_4m_3hEopL2pZtW2vd-d4M-M5adMr8-c9QFtpDF7mIjR4jaYmocvEZND8y_1eOrerdiSSqLVuB8icWIufSGEZTGklLA5Bwr5iVuUMDiQYPpeAWWNZYKuuzJkxEt7T7E8RgF1Nq8n3xlGzVUR0WPijVJGxsOBxjQXmZn3cb60rZF1AIoib2pWR2gkpBss5qVqSjbEsNuz1EQR__ELNFABg6B2nG207TAqCb-bai-8-7mNyu8_mg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پست ترامپ، ترجمه و توضیح ماشین:
ایران موافقت کرده است که هرگز سلاح هسته‌ای نداشته باشد! همچنین، داستانی که می‌گوید آمریکا ۳۰۰ میلیون دلار به ایران پرداخت می‌کند، خبر جعلی است که دموکرات‌های احمق منتشر کرده‌اند!!!
رئیس‌جمهور دی‌جی‌تی
(عبارت «Dumocrats» ترکیبی تحقیرآمیز از
Dumb
و
Democrats
است؛ یعنی چیزی مثل «دموکرات‌های احمق»)
realDonaldTrump
البته حرف از سیصد «میلیارد» دلار بود نه میلیون. ترامپ هم پرداخت از سوی آمریکا رو تکذیب کرده ولی
ونس هم نگفته بود که آمریکا قراره بپردازه
.
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 389K · <a href="https://t.me/VahidOnline/76406" target="_blank">📅 02:49 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76405">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sblXMsyzzNj_UJH3ykz_iixEOmIk0E0OvNrmMc_Lmqrou6qKLeKHHG4vkA8V8LF3g9Q0b-btXos9So8GZoulOxzwSAUvHZFtGFghzaZwQ8Cu8apd3DxYCDrtfNuVfTTrFaKlQKacZDOaKkXOiLAnh8LvQumeawTHuA2WYliTZiVsmmjPB0WqY9DfdnosJ9gE222FiouADSzNaw1YLw4fGEV7r9YfUZ_7enwchxQ5NyxK1ELrulaCfCIDGwTkvPEnxsK_94RJ_fcMQo7S0F7m0Tb9KHTsGBEPhGkL5KuCoNRF50iO1UjQ5Z6ayix3RN8_CSuoLjRG4BHYjfsfDIomKw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سه منبع مطلع که با خبرنگار اکسیوس گفتگو کرده‌اند، می‌گویند: جان رتکلیف، رئیس سازمان اطلاعات مرکزی آمریکا (سیا)، به دونالد ترامپ و دیگر مقام‌های ارشد دولت گفته است اطلاعاتی که چند نهاد اطلاعاتی آمریکا جمع‌آوری کرده‌اند، درباره آمادگی ایران برای ارایه امتیازهایی که واشینگتن در یک توافق نهایی هسته‌ای میان دو کشور خواستار آن است، تردید‌های جدی ایجاد کرده است.
براساس این گزارش، رتکلیف تنها فردی نیست که در تیم ترامپ دچار تردید است. مارکو روبیو، وزیر خارجه آمریکا، و پیت هگست، وزیر جنگ، نیز در نشست‌های داخلی نگرانی‌ها و پرسش‌هایی درباره این توافق مطرح کرده‌اند.
در مقابل، جی‌دی ونس، معاون رئیس‌جمهوری، و استیو ویتکاف و جرد کوشنر، نمایندگان آمریکا، از توافق حمایت کرده‌اند.
به گفته دو منبع، ترامپ و تیمش اطلاعاتی را بررسی کردند که چند نهاد اطلاعاتی آمریکا جمع‌آوری کرده بودند و نشان می‌داد شیوه‌ای که مقام‌های جمهوری اسلامی در گفت‌وگوهای داخلی خود درباره توافق صحبت می‌کنند، با آنچه به میانجی‌ها و آمریکا گفته‌اند، همخوانی ندارد.
به گفته دو منبع، رتکلیف و روبیو اعلام کردند که بر اساس همین اطلاعات، نسبت به این‌که حکومت ایران با اقدام‌های هسته‌ای مورد نظر آمریکا موافقت کند، تردید دارند.
یکی از منابع مطلع گفت: «اطلاعات موجود نشان می‌دهد نیت‌های ایران با تعهداتی که در چارچوب توافق پذیرفته، همخوانی ندارد.»
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 375K · <a href="https://t.me/VahidOnline/76405" target="_blank">📅 02:49 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76403">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/YWyLV4ZYmor-Qk88TPENH_tDRftCOaguoPPlNu5E_SR1vH9aeq2Lvi2Osg678k2xVjLodNt2-DOsN4SvJBtJR2YPaaiDK8EoKiY-zH4aYU9d2gvOx1m9oYU0JcVnKAGEtq1VRf3VrgCNXlurHNbKj-ivmAbtCKUvzz2rU_Pg2X8JSBu6ECkSZiVTDXs4eGAqJXgQyw_7KzDYrQVQP77H41xa-r3NBp_LwdCNDCGcoYCD-MQaDvPWhHAsrWIV1SNkQt_4_2g0Ip39W_rDgrCKBX-r7mSZb2LyLM3UcKy2t1ffi7fGbZ6kpwAJeq02CqJNWwIQv1nGUdCqiehJRyUd_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/D9RREjtQjPgGsLX_sld21YeFNqAxkmrxsBdD26XlQw5CJefvTMgyTRN4OEY1AhHKJFq2OMd4UIfl-m7H0cJZq52PhP_d4Bxe9OUCi0hyW7skUtPH9Uq7LZn56hYd0iTXp7WvurrnmeMtrxG7eeABwZpD_3PzGblkNBN_qnM180k2xmyavUbwX69MhfFtgsbgEz2aJR7a5oWIVKvg_uzZ_qb_DRjugDJEf6Zz34X6UD76vpiW2e79UxZK4Lb9xTTxUT7V93NAckWkfHPsNWJJDipx2zlU__5TbPCSWiAB1Zsfa7w6efRj3ks2I_zueqTjtgiMsvyuRAbxygGgt0c0IQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">جی‌دی ونس، معاون رئیس‌جمهوری ایالات متحده، روز دوشنبه در گفتگو با «سی‌ان‌ان» اعلام کرد که یادداشت تفاهم میان آمریکا و ایران سندی بسیار کلی و در حدود «یک صفحه و نیم» است.
ونس با اشاره به اینکه این متن تنها یک چارچوب کلان را تعیین می‌کند، تاکید کرد که جزئیات مربوط به موضوعات مختلف باید در طول مرحله مذاکرات فنی آینده مشخص و حل‌وفصل شوند.
به گفته او، این تفاهم‌نامه ساختاری را ایجاد می‌کند که بر اساس آن، ایرانی‌ها در صورت پایبندی به تعهدات خود، از مزایای این توافق بهره‌مند خواهند شد.
معاون رئیس‌جمهوری آمریکا در بخش دیگری از این مصاحبه گفت که در همان «بند اول» این سند، انتظار واشنگتن مبنی بر تعهد ایران به «صلح و ثبات منطقه‌ای» به صراحت مطرح شده است.
او تصریح کرد که بر اساس این بند، همان‌طور که ایالات متحده به صلح متعهد است، تهران نیز متعهد می‌شود که تامین مالی سازمان‌های تروریستی خشن و دامن زدن به بی‌ثباتی در منطقه را به طور کامل متوقف کند.
@
VahidOOnLine
جی‌دی ونس، معاون رئیس‌جمهوری ایالات متحده، در گفتگو با «سی‌ان‌ان» ضمن تکذیب گزارش‌های مربوط به آزادسازی زودهنگام اموال ایران گفت: «تا این لحظه حتی یک دلار از دارایی‌های مسدود شده ایران آزاد نشده و هیچ‌گونه کاهش تحریمی از سوی ایالات متحده یا شرکای ما در خلیج‌فارس صورت نگرفته است.»
ونس با اشاره به گزارش‌های نادرست در این زمینه افزود: «تندروها و برخی عناصر در داخل ساختار سیاسی ایران، برای متقاعد کردن افکار عمومی خود، دستاوردهای تهران از این توافق را بزرگ‌نمایی می‌کنند، بدون اینکه به تعهداتی که ایران برای کسب این امتیازات باید به آن‌ها تن بدهد، اشاره‌ای کنند.»
معاون رئیس‌جمهوری آمریکا با تاکید بر اینکه این توافق در صورت اجرا شامل یک بسته کاهش تحریمی بسیار بزرگ برای مردم ایران خواهد بود، تصریح کرد: «این تفاهم‌نامه نحوه تعامل ایران با جهان و منطقه را به طور اساسی تغییر می‌دهد، اما تهران تنها زمانی از این مزایا بهره‌مند خواهد شد که به تمامی تعهدات خود عمل کند.»
او در پایان به مخاطبان توصیه کرد که نسبت به بیانیه‌های تبلیغاتی و پروپاگاندای حکومت ایران بدبین باشند و تاکید کرد که بهره‌مندی از این فرصت بزرگ، کاملا به پایبندی عملی ایران به وعده‌هایش بستگی دارد.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 352K · <a href="https://t.me/VahidOnline/76403" target="_blank">📅 01:35 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76402">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/v_nfyQi44SrcRyzn1kD9LHS3tuKxq31B-9RbxLlukDhqz24tjfsjOWuNyqbzTb-tHIw0GcGj1CqbvFO46K0poZ3nyJ7IP3HFcgOf9gifa5M5exCCaWav6Wra3d6aKD3KccHmSLsgkWZbUb5HXU3PHo1WI7vb7g5wjkTLLVYtfASR5b6NCoxHbFRpYtQVvDXXyAkmKflY29IlqFuyx6Nw3nYSOizIGpBkuylM2LRsm5LEuI0h40BD8YYFDnWpIh_DwALnsyupGooPK8FiiaQZlSPYXlO9LCKSa1X0jbB7Au_I2pZ3nesf6R9eIrhkE7_BcUcVmd7eFNklLM_uFVay1w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرگزاری مهر:  منابع محلی از شنیده شدن صدای انفجارهایی در مناطق جنوبی جزیره قشم و تنگه هرمز خبر می‌دهند.
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 341K · <a href="https://t.me/VahidOnline/76402" target="_blank">📅 00:44 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76400">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/DpFDFMBZvlw2vX1zjXKIy2LLHqrr1Sv8HHHll7mLbIylrsxeKGWO_fCsluf0h8bJKvCFzikb-KlA1_0ElPuYfHF8by-nqWzcJNJ64lfU9iAr41xr-oUfKNU3Kp_sIAlqoa7DEY_oGbUgbLpCDNnN-j0gmS6CB3I9ApT3bxJoNf-bJ5RhVXVacGZrNREyOf5oYo5gMDdM2fBySpO1_U3VPxhy15YBjwOa4CstyI4PmCEUsfVOqejIpxlhErBI466Kj-YWBl0r4wV5EqMQr18fn1koLnjWa1xg-2OQAcuObaNg5fgInCrsUUM3V40zMvC1hSlxduJIrbCmNU1uIxTojQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/O_ACZxIz3K67QUUAtQClxJjKNfH6Ljzu-RMXHeWgq2u9mahoVE5_dO1P75sNtMGqkbvaaX5qhPs3zRRuZGcOST5sY1zQ-M8CENmZIsb8fPZ4d5yCOz1p9vYHuMp4jpxjCnZX4i91hqVrx8SlGmD-8lu0uNatZiQdjzT1GkN06r1zaOWj82dlEHbXR7ZtSQAdkZxJxngbaRo-8C3UFS6rgC-_ERdSxdg0wea6HEzHehzYu9Hh61co0JHEkjbM_TS8PLhbpQU6Eo2mupJZeD80b4T79uKTtuETK3JDY2z1i_lKNX5dBjVmvx-JFJwiM2ir6KDHQZgvNZicdm1PL8oPYQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">خبرگزاری تسنیم، وابسته به سپاه پاسداران، نوشت: رفع محاصره دریایی عملیاتی شد و ۳ نفتکش و ۲ کشتی حامل کالای اساسی جمهوری اسلامی از محاصره دریایی عبور کردند.
پیش‌تر ‌‌ارتش آمریکا در یک یادداشت هشدار اعلام کرد که محاصره بنادر ایران تا زمان تکمیل یک توافق آتش‌بس با این کشور که برای ۱۹ ژوئن (۲۹ خرداد) برنامه‌ریزی شده است، همچنان برقرار است.
@
VahidOOnLine
بر اساس گزارش فارس، دیگر خبرگزاری وابسته به سپاه، یک نفتکش غول‌پیکر ایرانی (VLCC) به همراه یک کشتی حامل نهاده‌های دامی با گذر از منطقه محاصره در آب‌های آزاد به سمت بنادر ایران حرکت کرده‌اند؛ هم‌زمان یک نفتکش دیگر نیز با عبور از دریای عمان و خط محاصره، مسیر خود را به سمت مقصد صادراتی پیش گرفته است.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 347K · <a href="https://t.me/VahidOnline/76400" target="_blank">📅 00:27 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76399">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">پیام‌های دریافتی نیم‌ساعت پیش:
صدای انفجار سیریک ولی با فاصله تقریبا دور
سلام وحید
۲۳:۵۷ دوشنبه ۲۵ خرداد قشم
خودم یه انفجار و موج رو حس کردم، اما بچه‌ها میگفتن دوتا بوده و قبلش هم حس شده، جایی که من هستم نزدیک تنگه است، شاید از روی دریا بوده
۰۰:۰۴ سه‌شنبه ۲۶ خرداد
مجدد دوبار احساس شد
سلام وحید خوبی
ساعت ۱۲ و ۵ دقیقه سمت سیریک صدای انفجار از سمت دریا اومد
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 336K · <a href="https://t.me/VahidOnline/76399" target="_blank">📅 00:27 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76396">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Euvt4de1Q8wPnSNIBaqUNIxmJRfYk9UWqV63esDaxYQWwQMJRvS5cqT3B4yiNzKxyF8Z3ElgWwgSfcQapv-f8tce6vW0Mo-Pb8DqrJvsCzSpLCgFW98uZtnDsNIhABYV1Nr4cXHKZwTOKkqcURmXDDqiyaleMAhiGFTrnEGp3pU1dRZQNZ3-qfYGFRh7PROp2ZOF74Dg-mZWc1eRQCnbajJDbg8ogh9o3YL6beiZQWl-4efmhuOjRNtA68ZUNiPfcnR-8slpHQTWDHbui-byn5Dom8t77_7RrnJYGtZfuLYqB5h5PyBFbVhfNCzAtvzqK0_HKAexdbzQ_R9VdFNR9A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/759110416d.mp4?token=iIp-DS68apZxHEMnGGZpe1RRnrHRAAwj0szjHp34TreqnlrdiiO7_eBi_hcB4H46QAfaPL-yoIEWX4yXmI5gAEYk7FbsKY1P8GyT38aLOJmJe0QEcYkRjBcSSGJEYRNqUigkpRCQBHM8PsQguDH09y9WrGarQ6-TsdRtNgYfN8ORQmN5iXLeJTRCvIVvbjN_KHpMpXWmpwcsr5SR7NsWIIP6qdT2vZD_ty8GSUSqw8t5B3_ClxYTIgyKRPXlo5hiEHMrKndngiO6lLsDRoBqoFd1EW310Bn0ICFeHFvvijPIFF4z3u0hZ-M0TPADMUQ45puHNwizIvHDbrsm4MFAww" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/759110416d.mp4?token=iIp-DS68apZxHEMnGGZpe1RRnrHRAAwj0szjHp34TreqnlrdiiO7_eBi_hcB4H46QAfaPL-yoIEWX4yXmI5gAEYk7FbsKY1P8GyT38aLOJmJe0QEcYkRjBcSSGJEYRNqUigkpRCQBHM8PsQguDH09y9WrGarQ6-TsdRtNgYfN8ORQmN5iXLeJTRCvIVvbjN_KHpMpXWmpwcsr5SR7NsWIIP6qdT2vZD_ty8GSUSqw8t5B3_ClxYTIgyKRPXlo5hiEHMrKndngiO6lLsDRoBqoFd1EW310Bn0ICFeHFvvijPIFF4z3u0hZ-M0TPADMUQ45puHNwizIvHDbrsm4MFAww" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پایگاه نیروی هوایی ادواردز آمریکا اعلام کرد یک بمب‌افکن بی-۵۲ روز دوشنبه ۲۵ خردادماه در ایالت کالیفرنیا سقوط کرده است.
بر اساس بیانیه منتشرشده از سوی این پایگاه، هواپیما «اندکی پس از برخاستن» از باند فرودگاه پایگاه ادواردز و در ساعت ۱۱:۲۰ صبح به وقت محلی دچار سانحه شد.
در این بیانیه آمده است: «تیم‌های امدادی بلافاصله به محل حادثه اعزام شدند و عملیات امداد و بررسی همچنان ادامه دارد.»
مقام‌های آمریکایی تاکنون جزئیاتی درباره علت سقوط، سرنوشت خدمه یا میزان خسارات احتمالی منتشر نکرده‌اند.
«بی-۵۲ استراتوفورترس» یکی از مهم‌ترین بمب‌افکن‌های دوربرد نیروی هوایی آمریکا است که از دهه ۱۹۵۰ در خدمت ارتش این کشور قرار دارد و توانایی حمل تسلیحات متعارف و هسته‌ای را دارد.
@
VahidOOnLine
آپدیت:
هر هشت سرنشین آن جان باختند.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 365K · <a href="https://t.me/VahidOnline/76396" target="_blank">📅 22:54 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76395">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/10d585b107.mp4?token=orkFoiOL8RanIQuXIvG09j3EZw7dxIAqdIXjDtxqiToG3byVglY660gaEhkaj5b-5mB1hXl7eccmJEmXUk1ibeC7-NBgbf42Welb5tnTZ3qL2vQug8y35Fpe5YNebmeSJQcqyCCaYICm9mNCiWZ98YeAnFsA-vvFoKogWhR4F1hC8w468QSR37G1av0Mx39CZWZUGfAvlqL-jLQrjtMNSWm4oauE8ttCWvAIMlCDjvOwYRhvqhH2Rx_ZUkr9B5wtwFmscbvLH1EfluUKeU88IheTtRxIMZE4IKNTMZJgZBo5ZBFd9HTA_l0FVcF_RhsTiXGsTCPHqhO2xCxi4Lhdp4Lvt2_b85UD1u-JWHWuVVnRJNsMxNvvS8J3wNCU4_FFccH3Rcwrx9YY0dX6ovtRsazLwikhDFwEXdxKtXwu4t16uyDVovs5IQn50hC7TEl-nKoSoP9V8EQVwC-J7JZadCt7hp1505tQncbCtXqu412Gj7uZHZPPliKBzaW4a664aMb6nCuywD4GvRooDjeOiZq1aBQ3VKn3hi9rONn1B3Hkg_-g5L_woGcImcOa9zKaFdgR0V5HhULexKuhrhMbRA9v67xy8kgDzeDGfYlQwGYPWICqjLIahzYrJosTFRmp-vivjcNmohc-qKHjXd8raWhTjsIka7qQfPwqA8uuTRs" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/10d585b107.mp4?token=orkFoiOL8RanIQuXIvG09j3EZw7dxIAqdIXjDtxqiToG3byVglY660gaEhkaj5b-5mB1hXl7eccmJEmXUk1ibeC7-NBgbf42Welb5tnTZ3qL2vQug8y35Fpe5YNebmeSJQcqyCCaYICm9mNCiWZ98YeAnFsA-vvFoKogWhR4F1hC8w468QSR37G1av0Mx39CZWZUGfAvlqL-jLQrjtMNSWm4oauE8ttCWvAIMlCDjvOwYRhvqhH2Rx_ZUkr9B5wtwFmscbvLH1EfluUKeU88IheTtRxIMZE4IKNTMZJgZBo5ZBFd9HTA_l0FVcF_RhsTiXGsTCPHqhO2xCxi4Lhdp4Lvt2_b85UD1u-JWHWuVVnRJNsMxNvvS8J3wNCU4_FFccH3Rcwrx9YY0dX6ovtRsazLwikhDFwEXdxKtXwu4t16uyDVovs5IQn50hC7TEl-nKoSoP9V8EQVwC-J7JZadCt7hp1505tQncbCtXqu412Gj7uZHZPPliKBzaW4a664aMb6nCuywD4GvRooDjeOiZq1aBQ3VKn3hi9rONn1B3Hkg_-g5L_woGcImcOa9zKaFdgR0V5HhULexKuhrhMbRA9v67xy8kgDzeDGfYlQwGYPWICqjLIahzYrJosTFRmp-vivjcNmohc-qKHjXd8raWhTjsIka7qQfPwqA8uuTRs" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">"خون آقامون رو چند فروختید؟"
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 355K · <a href="https://t.me/VahidOnline/76395" target="_blank">📅 22:47 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76394">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/4de6c46b4e.mp4?token=HmFwFdeI_D0CAbmHMaQExalxQJKVBXlohDKdU8KVkFUTSb081iZRHTAYXVtZHRiOI0JqoH-tq9BIfHjcaXezsdrIPol_ieHVKdXBaRNCK40xAZlqy6uvYDcwVGZbcfGPFO6rXtZu76VcXbxMpj4uocHL7Y-CbxtGCNlUStt47Kk94vLfVmtnVee1eXwClN11i_M9pvkVTR6ZYULByssCiZgRHJTj2ZrcM66ZiH6LKBtoxNSFWtdk72MKzQUVs8epcAjFRwSUE2nNmzAB3DeH4wGwMGYqhz5h-mC_yw2lqYCwLmpzA3lShZvRev7VzWkGd4pm1ai9bq04dWL2Q689fA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/4de6c46b4e.mp4?token=HmFwFdeI_D0CAbmHMaQExalxQJKVBXlohDKdU8KVkFUTSb081iZRHTAYXVtZHRiOI0JqoH-tq9BIfHjcaXezsdrIPol_ieHVKdXBaRNCK40xAZlqy6uvYDcwVGZbcfGPFO6rXtZu76VcXbxMpj4uocHL7Y-CbxtGCNlUStt47Kk94vLfVmtnVee1eXwClN11i_M9pvkVTR6ZYULByssCiZgRHJTj2ZrcM66ZiH6LKBtoxNSFWtdk72MKzQUVs8epcAjFRwSUE2nNmzAB3DeH4wGwMGYqhz5h-mC_yw2lqYCwLmpzA3lShZvRev7VzWkGd4pm1ai9bq04dWL2Q689fA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">عباس عراقچی، وزیر امور خارجه ایران، روز دوشنبه ۲۵ خرداد به خبرنگاران گفت که قرار است روز جمعه در کشور سوئیس که محل دقیق آن مشخص خواهد شد، دیداری بین هیئت‌های دوطرف انجام شود.
او توضیح داد که در این دیدار، «قرار است روسای هیئت‌های دو طرف ابتدا این یادداشت تفاهم را امضا کنند و پس از آن اولین دور مذاکرات بعدی را داشته باشیم.»
@
VahidHeadline
محمدباقر قالیباف، رئیس مجلس شورای اسلامی نیز در واکنش به امضای تفاهم‌نامه توقف مخاصمه خطاب به مردم این کشور گفته است: «با مقاومت تاریخی شما و رشادت نیروهای مسلح دربرابر آنان که قصد جان این ملت و نابودی و تسلیم این مملکت را کرده بودند، ایران گامی بلند به سوی پیروزی نهایی برداشت. می‌خواستند و نتوانستند.»
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 299K · <a href="https://t.me/VahidOnline/76394" target="_blank">📅 22:47 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76392">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/c3fdaedd66.mp4?token=B7YnHfPOwQOTfc1RntSIzvJDo2cgEqkJK3hRcoZJ7y9ePxVlI5SGOOvWBPR9Nlq2W83luv5bcUth-j3OuXxeweC1ADx9PABOStMPZVSvvY-1ffmwkeOaDcKGXt4dJxiCCBoA8ogKRr28HTKT57HsXWNcUDamb6Lcee2QxxGed3s67TqLAJtVEioH3QfUmyqUK1l_sM9IB7JKuvLQnzQ-dzFXPwFVT6jMMuOiQ3EKlGvJ6PVVLEk15i8H96NZ4B3pcuB0IOkRf86mcVr6gKePdlkIkvcod7tuh7rx40kEOzcd1it3MmwqtVkPI6_yfpPkfFNRph4s8rvIO6tx_sZpLw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/c3fdaedd66.mp4?token=B7YnHfPOwQOTfc1RntSIzvJDo2cgEqkJK3hRcoZJ7y9ePxVlI5SGOOvWBPR9Nlq2W83luv5bcUth-j3OuXxeweC1ADx9PABOStMPZVSvvY-1ffmwkeOaDcKGXt4dJxiCCBoA8ogKRr28HTKT57HsXWNcUDamb6Lcee2QxxGed3s67TqLAJtVEioH3QfUmyqUK1l_sM9IB7JKuvLQnzQ-dzFXPwFVT6jMMuOiQ3EKlGvJ6PVVLEk15i8H96NZ4B3pcuB0IOkRf86mcVr6gKePdlkIkvcod7tuh7rx40kEOzcd1it3MmwqtVkPI6_yfpPkfFNRph4s8rvIO6tx_sZpLw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جی‌دی ونس، معاون رئیس‌جمهور آمریکا، در گفتگو با شبکه سی‌بی‌اس اعلام کرد ایران در صورت پایبندی به تعهدات خود ممکن است به صندوقی برای بازسازی دسترسی پیدا کند که از سوی کشورهای حاشیه خلیج فارس تأمین مالی خواهد شد.
ونس با اشاره به مزایای احتمالی توافق برای تهران گفت ایران «ممکن است» حدود ۳۰۰ میلیارد دلار منابع مالی برای بازسازی از کشورهای خلیج فارس دریافت کند، اما تحقق این امر را منوط به اجرای کامل تعهدات جمهوری اسلامی دانست.
او افزود آمریکا با سرمایه‌گذاری کشورهای حاشیه خلیج فارس برای بازسازی ایران موافق است، اما این اتفاق تنها زمانی رخ خواهد داد که ایران به برنامه هسته‌ای خود پایان دهد، فعالیت‌های مربوط به مواد غنی‌شده را متوقف کند و با یک نظام بازرسی و نظارت گسترده موافقت کند.
معاون رئیس‌جمهور آمریکا همچنین تاکید کرد رسانه‌های نزدیک به حکومت ایران بر مزایای توافق تمرکز خواهند کرد، اما از امتیازاتی که تهران باید در مقابل واگذار کند کمتر سخن خواهند گفت.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 317K · <a href="https://t.me/VahidOnline/76392" target="_blank">📅 22:40 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76390">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromFactNameh | فکت‌نامه</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/n-_KCHaMer8e6kLemR0Gi11SJP023pHT6dpmRvJ0lwZAUIxlzG0I0rsroGy1J6KxGVUiJZLRaknuxZq5UCPEvKn_R8mX4BDB4ARR-96y-stiGMkajxjvbotSa8q25ilHrO7liMUYBeGafPlyepiK9-fpJewBlcyIMOtqaE_Pzrgn6EElzpsXU91MS1Crd8XIFL38uDs6BGUVMdW_QhL4NCULAuxaQuHidVW4y_FSfakXvZQFUYlkXJEUAjN61xrOpscph2NHGBm31og4f_HzQK5W6HHx-PkNRjDSJmCpagZMCV4ZSD628obE9LmLqscijCu_ILvOCO2yBggphlwbXQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/t8oMA5HF4rzVnsv9WyYo4DwJ1cWOoQbxWd7tWvmkyWRuBqhjpWCUvTyfWujiavRiQBUtElH5GO1m7d9rKNvQ3YcJz8nCZ02BLzwDD1kQp5Iuya0s_bXeAWJJJvVr_tiES5YWH4Fi0qSBCYJkrdgBSqWKM678MGHnuyQKLB93dzCkIktsMaNdfr2nrMuHhcGuCcxGOzY4inLHz_3SbbSibB8_ssY-DqFVywDJ9Yw2FBOzARxOQ9IdVmrogBab7BsDiAx8EbNzXm--2ng4xUupb4nHNGorpcJQit7wdWKnbjjXfLvRjKhqG_aKykgMi_moWWOVo6FrWVSeBTXWpFopaA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">❌
ویدیوی قدیمی منتسب به تیراندازی به هواداران حکومت در تجمع شبانه
🔹
ویدیویی در شبکه‌های اجتماعی منتشر شده که ادعا می‌کند صحنه تیراندازی به مخالفان توافق با آمریکا در تجمعات شبانه هواداران حکومت ایران را نشان می‌دهد.
🔹
این ویدیو قدیمی است و ارتباطی به تجمعات شبانه هواداران حکومت در ایران ندارد.
🔹
ویدیو مربوط به دهم اسفند ۱۴۰۴ و برخورد پلیس عراق با هواداران جمهوری اسلامی است که سعی داشتند به سفارت آمریکا در بغداد نزدیک شوند.
🔹
گزارش‌هایی از تجمع مخالفان توافق جمهوری اسلامی با آمریکا منتشر شده اما خبر تیراندازی به آنها در هیچ منبع رسمی منتشر نشده است.
🔹
این ویدیو پیش‌تر نیز با ادعای نادرست دیگری به اعتراضات دی ۱۴۰۴ منتسب شده بود.
🔹
بنابراین فکت‌نامه به ادعای مطرح‌شده درباره این ویدیو نشان
«نادرست»
می‌دهد.
👈
در فکت‌نامه بخوانید
🌐
@Factnameh</div>
<div class="tg-footer">👁️ 289K · <a href="https://t.me/VahidOnline/76390" target="_blank">📅 22:18 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76389">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/ccb668e4af.mp4?token=vW-AEVNpuzfgNRBMlNz5yuHrliAhGh1N-xsbTw1W6CHjEr0kp_kfP9G4elHkZspljTmUXyopRriWXDfif2MTfkkOXEydrduzZklcADejrL1Nj-nK_rprTliBe8DsuUYhfJheNwjQ-lfa-CGVWXpgm1HJ4EuqrNjHc9C4C_Yd1UTtDdKIYU7-z7QMo6PlImQYxY0EWboGoCPZwfKD-nCCJOuWaTU9mFQ_BmwyR1p8XdcYjKFXrpX2IbGayDX8pEnJXpZr4cTinstWtQZ_1-cHAqulKsc9w4rXdrinCtPWcgI37JH70HQkd9R9z9MiA1fIK5zDHUaOfQ9KDfTnGGZfxA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/ccb668e4af.mp4?token=vW-AEVNpuzfgNRBMlNz5yuHrliAhGh1N-xsbTw1W6CHjEr0kp_kfP9G4elHkZspljTmUXyopRriWXDfif2MTfkkOXEydrduzZklcADejrL1Nj-nK_rprTliBe8DsuUYhfJheNwjQ-lfa-CGVWXpgm1HJ4EuqrNjHc9C4C_Yd1UTtDdKIYU7-z7QMo6PlImQYxY0EWboGoCPZwfKD-nCCJOuWaTU9mFQ_BmwyR1p8XdcYjKFXrpX2IbGayDX8pEnJXpZr4cTinstWtQZ_1-cHAqulKsc9w4rXdrinCtPWcgI37JH70HQkd9R9z9MiA1fIK5zDHUaOfQ9KDfTnGGZfxA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بنیامین نتانیاهو، نخست‌وزیر اسرائیل، اعلام کرد نیروهای اسرائیلی در آنچه «مناطق امنیتی» در غزه، لبنان و سوریه خواند، تا زمانی که برای تأمین امنیت اسرائیل ضروری باشد، باقی خواهند ماند.
بنیامین نتانیاهو، نخست وزیر اسرائیل، روز دوشنبه در یک کنفرانس خبری تأکید کرد که به‌رغم امضای تفاهم‌نامه میان ایران و آمریکا، چالش کشور اسرائیل به پایان نرسیده و «ما باید گوش به‌زنگ بمانیم و در مواقع لزوم از خود دفاع کنیم».
به گفته دولت آمریکا، جمهوری اسلامی در قالب تفاهم‌نامه‌ای که روز یک‌شنبه امضا شد تعهد داده است که هرگز به دنبال سلاح هسته‌ای نرود.
نخست وزیر اسرائیل در ادامه سخنان خود تأکید کرد که «با یا بدون توافق، ایران هرگز به سلاح هسته‌ای دست نخواهد یافت».
نتانیاهو در نشست خبری خود همچنین گفت که حملات مشترک در کنار آمریکا به ایران خساراتی سنگین وارد کرده و به گفته او «بعضی معتقدند که خسارت اقتصادی به ایران یک تریلیون دلار بوده است».
او در ادامه گفت:
ما به مردم ایران قول دادیم که شرایطی را فراهم آوریم که رژیم آیت‌الله سرنگون شود، نمی‌دانم چه زمانی این اتفاق خواهد افتاد، ولی خواهد افتاد.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 311K · <a href="https://t.me/VahidOnline/76389" target="_blank">📅 22:09 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76386">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/d206f4a845.mp4?token=PUsnrhOnkHRzF5I-x1uWXp1dOzX5FkjY3hNe7a9CTo4WB97WCNYrBYNRiLyarJiHs16U_7Am0wnmGmJwgLiqz9Ghy37ob4DrLlSmqZ7pdhxWnij97qLRk87fQWVUto39y_wh3qaFlqa34q-l4yN1F-gfpR_zncQqQKZPP07CogT8z_QC3hW_XRVlsyhxvAmUW_wCvDPO7o5Gc0prejXBJj8RdMjsD_zrT0ZTB58oZloE07c36vtFF_zCbbcP49VFUGOE39HtoDW6so6X6TX3MhfoM94j5UuoNieO7OwQ-qzcJUV_47WH-xxm4mpvinkZC6uszVd838MSX8VYl5d1cw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/d206f4a845.mp4?token=PUsnrhOnkHRzF5I-x1uWXp1dOzX5FkjY3hNe7a9CTo4WB97WCNYrBYNRiLyarJiHs16U_7Am0wnmGmJwgLiqz9Ghy37ob4DrLlSmqZ7pdhxWnij97qLRk87fQWVUto39y_wh3qaFlqa34q-l4yN1F-gfpR_zncQqQKZPP07CogT8z_QC3hW_XRVlsyhxvAmUW_wCvDPO7o5Gc0prejXBJj8RdMjsD_zrT0ZTB58oZloE07c36vtFF_zCbbcP49VFUGOE39HtoDW6so6X6TX3MhfoM94j5UuoNieO7OwQ-qzcJUV_47WH-xxm4mpvinkZC6uszVd838MSX8VYl5d1cw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">'
#آتش‌سوزی
در  شهرک امید
#تهران
'
تصاویر دریافتی از شهروندان،‌ دوشنبه ۲۵ خرداد، حدود ساعت ۲۱
Vahid
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 304K · <a href="https://t.me/VahidOnline/76386" target="_blank">📅 21:30 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76385">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/8e8cc0eeaf.mp4?token=u75v_cTuT2j52mjhxkI9g3IJSyPaPFQbfNSdPrhFwy3GwPbIk-D5GQ3ITh_DyRzBB1pMj6LpUYUbkok-qsTsfmCl4ehA7B__poAO6vJhMnAuxAANhd1UECG0nZWIz71WCnL04GLImlhdEykS-l3ou8Ij6Er6Bgymj57p-WeiQwsKAP58aySWCj6kNVfJJpXq6gYjYs_oiDGARkjeyKiv2j0dlwY__4gQav8nj2Xbt5VlNz56QD58YLIIp2h71H4Dnkvvk3cFpeubPAn3Oe7VTR0huAxMYyEWh1tsoasXHZmY7WGwbWa7N2GfvxvKMp_jclSDj9LWGPeqbGAxWZmnlA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/8e8cc0eeaf.mp4?token=u75v_cTuT2j52mjhxkI9g3IJSyPaPFQbfNSdPrhFwy3GwPbIk-D5GQ3ITh_DyRzBB1pMj6LpUYUbkok-qsTsfmCl4ehA7B__poAO6vJhMnAuxAANhd1UECG0nZWIz71WCnL04GLImlhdEykS-l3ou8Ij6Er6Bgymj57p-WeiQwsKAP58aySWCj6kNVfJJpXq6gYjYs_oiDGARkjeyKiv2j0dlwY__4gQav8nj2Xbt5VlNz56QD58YLIIp2h71H4Dnkvvk3cFpeubPAn3Oe7VTR0huAxMYyEWh1tsoasXHZmY7WGwbWa7N2GfvxvKMp_jclSDj9LWGPeqbGAxWZmnlA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدیوی دریافتی از
#آتش‌سوزی
چیزی به اسم "موکب"
منابع حکومتی به نقل از سخنگوی آتش‌نشانی تهران: آتش گرفتن گاز پیک‌نیک در یک موکب مستقر در میدان تجریش
#تهران
باعث سرایت آتش آن به چادر شده و دود بلندی در منطقه  ایجاد کرده است. بازار تجریش از این آتش آسیبی ندیده و آتش به سرعت خاموش
Vahid
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 321K · <a href="https://t.me/VahidOnline/76385" target="_blank">📅 20:33 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76384">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/db_OTtL6aPVm0tkdc8twwXPd7qIC3qIxczHn49HZjL1WnnXtX00U8xhvBBq-ERHSK4WbfShvbNYSRrc05GrtTssTs2jVzCox1PvRJTACYVd0tPr5R-MLN2Mb1gTgpCH-YVeTsFQU1amKtBXCpB6ScblYrxaQLQkZxHymBoMrjhN4bs1ELhsu-xaXbPuFOjSE6B4HyvUw62oNlZAnHTGuCj5sQLq1a9K1_2oXulD3t83Bqow7Gd73efiNR5xPK2XfcK_eMzd5841wCT4GqEkb-mjUpIC8WZTr3XyrgaLnZhTyTleeeM7FMULzIqXNmdja2Vzl3ATvA7yLtExD82kJdw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یک مقام ارشد آمریکایی روز دوشنبه اعلام کرد تفاهم‌نامه میان آمریکا و جمهوری اسلامی به امضای دونالد ترامپ، رییس‌جمهوری آمریکا، جی‌دی ونس، معاون رییس‌جمهوری آمریکا، و محمدباقر قالیباف، رییس مجلس جمهوری اسلامی، رسیده است.
او گفت در مرحله بعدی مذاکرات، آرایش فعلی نیروهای نظامی آمریکا حفظ خواهد شد، اما در صورت دستیابی به توافق نهایی، کاهش نیروهای نظامی در نظر گرفته شده است.
این مقام همچنین گفت مذاکرات فنی از اواخر این هفته آغاز می‌شود و جزییات توافق طی ۲۴ تا ۴۸ ساعت آینده منتشر خواهد شد.
او افزود آزادسازی دارایی‌های مسدودشده و کاهش تحریم‌ها به اجرای تعهدات وابسته است.
این مقام ارشد آمریکایی همچنین گفت: «از عملکرد عمانی‌ها در مذاکرات پیش از جنگ رضایت نداشتیم.»
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 302K · <a href="https://t.me/VahidOnline/76384" target="_blank">📅 19:44 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76383">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/e48597c90a.mp4?token=liYkFO7BGbAc6UPZ0ofqxv4zDdexlrfzYnCQqrqapwCS_WXJ8iTQkO3Ug791QqKCLZnVHdT9OIMHGIJJNeHbJ6MoqZD2kEWpnQ7jYVs-19Cw40IsRFMj9_ku99hS4r3prLxorMw4k-V0nCO6sTeMJ-Fulr3x9HMzPHqzwh1Ztaef_Db73c2rycdvJ2mtipKmInoJ3kuduTZhbfgYOyF1lA8IuHdwIsGROgxcccNaqoF4XAem0LEG2dn-sU_AGtq3BBJGamOrLMSVoPCpmB3VlFyiNUCNz2bnGZMPfiGKouFrZnNXQ-Ej0Tssrd6Jhdf4TAhvpHnp2oUdxulZ1pN0nA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/e48597c90a.mp4?token=liYkFO7BGbAc6UPZ0ofqxv4zDdexlrfzYnCQqrqapwCS_WXJ8iTQkO3Ug791QqKCLZnVHdT9OIMHGIJJNeHbJ6MoqZD2kEWpnQ7jYVs-19Cw40IsRFMj9_ku99hS4r3prLxorMw4k-V0nCO6sTeMJ-Fulr3x9HMzPHqzwh1Ztaef_Db73c2rycdvJ2mtipKmInoJ3kuduTZhbfgYOyF1lA8IuHdwIsGROgxcccNaqoF4XAem0LEG2dn-sU_AGtq3BBJGamOrLMSVoPCpmB3VlFyiNUCNz2bnGZMPfiGKouFrZnNXQ-Ej0Tssrd6Jhdf4TAhvpHnp2oUdxulZ1pN0nA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">رییس‌جمهوری ایالات متحده دوشنبه اعلام کرد که توافق با ایران امضا شده و متن توافق حاصل شده با ایران پس از مراسم امضای رسمی در جمعه منتشر خواهد شد.
دونالد ترامپ که در هنگام ورود به اویان در فرانسه، برای شرکت در نشست گروه هفت صحبت می‌کرد، همچنین گفت تنگه هرمز تا جمعه به‌طور کامل باز خواهد شد.
ترامپ در کنار امانوئل مکرون، رییس‌جمهور فرانسه، گفت مشخص نیست آیا در مراسم روز جمعه که قرار است در ژنو برگزار شود شرکت خواهد کرد یا نه، اما معاون رییس‌جمهور آمریکا، جی‌دی ونس، در آن حضور خواهد داشت.
او گفت: «توافق کاملا امضا شده است. و همان‌طور که می‌دانید تنگه اکنون تا حدی باز شده است. روز جمعه کاملا باز خواهد شد.»
ونس پیش‌تر گفته بود این توافق یکشنبه به‌صورت دیجیتالی امضا شده و هیچ‌گونه بودجه‌ای آزاد نشده است.
در پاسخ به این سؤال که متن یادداشت تفاهم چه زمانی منتشر خواهد شد، ترامپ گفت: «احتمالا خیلی زود. بعد از جمعه... فکر می‌کنم در آینده بسیار نزدیک.»
ترامپ همچنین گفت هرگونه کاهش تحریم‌ها علیه تهران «به رفتار ایران بستگی دارد. اگر آن‌ها کاری را که باید انجام دهند انجام دهند، این روند آغاز خواهد شد.»
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 294K · <a href="https://t.me/VahidOnline/76383" target="_blank">📅 19:43 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76382">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/06a4a159c2.mp4?token=vOJw24hbT-b0XgbWXuhenBa_-DLDJ3dQe5u5cUpVBzuxAqekFcj0kXW_wh5l5uGBbsBMzJGu4sfLrSYV0YvEswxFq3Snoql6KgRc7eMFHQI1DJi2LosP3b7XR4r_l623Op0KuLrO_2cx3-UYCpNGjM_nEPSwZNE355sy-LK1FW-nTPK7DVhPxQ-cEYDISKBEuDtPkqnJXIkfuVz773NBbXHAx33EuzXDYJiDnsl91xyoyNzxidxaUS3IjA8OqFsp-jFEsHQDWZ3pSjgwVbHOZkUYVJMxdgICUy5SRWnBHr9mVip4Vz--gJcHPd53VHWmYePFLacIGgOqFNF7RIeJIA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/06a4a159c2.mp4?token=vOJw24hbT-b0XgbWXuhenBa_-DLDJ3dQe5u5cUpVBzuxAqekFcj0kXW_wh5l5uGBbsBMzJGu4sfLrSYV0YvEswxFq3Snoql6KgRc7eMFHQI1DJi2LosP3b7XR4r_l623Op0KuLrO_2cx3-UYCpNGjM_nEPSwZNE355sy-LK1FW-nTPK7DVhPxQ-cEYDISKBEuDtPkqnJXIkfuVz773NBbXHAx33EuzXDYJiDnsl91xyoyNzxidxaUS3IjA8OqFsp-jFEsHQDWZ3pSjgwVbHOZkUYVJMxdgICUy5SRWnBHr9mVip4Vz--gJcHPd53VHWmYePFLacIGgOqFNF7RIeJIA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اکانت فارسی وزارت خارجه آمریکا با انتشار ویدیوی بالا نوشت:
جی. دی. ونس، معاون رئیس‌جمهور ایالات متحده: توافق با ایران، «مبتنی بر عملکرد» است.
«باید به خاطر داشته باشیم که اقتصاد آنها اساساً نابود شده است. برنامه هسته‌ای آنها اساساً نابود شده است. اگر آنها [در چارچوب این توافق] اقدامات درست را انجام ندهند، از همان ابتدا هرگز پولی در اختیار نخواهند داشت که بتوانند برنامه هسته‌ای خود را بازسازی کنند.
USABehFarsi
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 279K · <a href="https://t.me/VahidOnline/76382" target="_blank">📅 19:21 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76379">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/coRVeYenbw22jaZ_SGL1iMaqGlQ-22UeXsPy3BH9GSR0HFKUszNGYhOcVz3k4pLuL4JmRBQzOZMD-QOSMroSjoId0lIKHsl4sWjrKiQs7d3FXhXi1oC8A4KIB6kFbognZWnxjrQSI1XYkYeMniEG-9eQirlXt6v6I3tiAsiZMTmE3GBtF3JRVY3r9YbqaiHOcE9KzQhLb2wju94scNRgAPOV2XlJMscMdnObjImmD_BEieLZQYGGq90Qv823xI7078DsS9kVtw1aW3k-nLNxUpBdf1fRi5YR7Bb9hhOtxzIIc-pt0LDwBJloXol0ID6g9XwWvM-iwNfkaRytcJOQGw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/i3unUqYPHjNjeqUydf9n3xqDWoWVGlKwhzxErV3-eRs_12TGfbX1JDUjSuY1KqTaZoqpPPlJDezgD8aDQsCFpdraWtz9wKf7PKsmoxWvh2mJRp84Lkag8dips1e-l1voEuVEbXRpNGEftTg7V41It3SvdBnAhwDYYO9jpx8pW0BF5QE5o-g7TVC_BzwM1dbTkhxeIgXp0sJ8FwwZ01uzJPABI7-Go4uQ53BRpnJws9pff2PbpMa_36y9dqyJXiDkPYVd0VsHo2uk0bkTHbjKDaG2uOLE7w2WeqDhN3f8UhFytrlPkDWmEKNBPrCDubawvBEIRybuh6f5qe0eAVo4Rw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/jiJ80Ww8WrwQ5g--nTvVs95nBtQ69VCUtb8qfAdIwE4kaE9_lISbtOmFo47HgnH5aYwzAIEMEf_Ht5YwifUi_4CZVdoEeD3cjifajYczprBIuW153ETEn6ENXNXGNM5lRFG569JM28DKnzYooGmOd_asDUm1OO9V2h5a75O43BRKJEGYFoZ1GOWZ8z8ejMmghKQFSQLT4k6k4UIVyXR72Zr0VsFppgYHgkYTsTBNX7aFzJweC8nIM3QITtRWl0urpyF8bqCCWRd9pWHYih8LLA9VArhE9kxUd0okizrJSS6GaV1OOy1ChClaP6XcA1bbhECOUvo1-nieyhiZZaISkA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">منابع حکومتی با انتشار تصاویر بالا نوشتند:
کلاهک ۵۰۰ کیلویی موشک تاماهاوک سقوط کرده در اطراف ورامین خنثی شد
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 268K · <a href="https://t.me/VahidOnline/76379" target="_blank">📅 19:10 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76378">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/N8aMlwDNtUp37kbQcyBsektSKGmzKdVqlAd4G5apa_zYPupIcKq9AOlBGkT2fcts6b0jNWtFfBEfybH9YNev1wAnSrASmqHHUCPsavgsJSY0b3aq46KpSWoPWeDKvIrH9wcVoVpd8gIVCTn6JU-ynzgDKtKu7mDphwmywFvgl92-mWYRjgR6onZuQmIA6c4V03-TAOhwTfk1vrnLIhtJSM26qrrZ0wWPGkigmUh6okrtU8Lyfgfe0kLKkJqNSDt-4M4VFzhFrwO1QFAbLGT-MuDSH_bekj8D-U-rZpCtYIFVkGrOt_vnG7XgaUvysY0RPdFyrh57DE8foe5Yok7uig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پلیس اطلاعات تهران، روز دوشنبه ۲۵ خرداد ۱۴۰۵ از بازداشت سه شهروند به اتهام انتشار مطالبی در شبکه‌های اجتماعی خبر داد.
خبرگزاری مهر به نقل از پلیس اطلاعات تهران بزرگ گزارش داد که این افراد در پی رصد فعالیت‌های فضای مجازی شناسایی و بازداشت شده‌اند. به گفته پلیس، بازداشت‌شدگان متهم هستند با انتشار مطالبی در شبکه‌های اجتماعی به مقدسات و آنچه «مدافعان وطن» خوانده شده، توهین کرده‌اند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 298K · <a href="https://t.me/VahidOnline/76378" target="_blank">📅 19:02 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76374">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/RaOT5frnlQcrUplPvgg63Cce8S1UW4zDA19CcOYOBJLheO5j80dJMTeH59pqtCazPeCfpNFUOPdzcSK6zxqGhqULE07nUKuy-9eYQO2XFLaG5lWwZJmaPqK1tNOvBt8KWxta86OVojihuHfTEEOgBLR_nzhZDCk6vHfq7dgUbQXL3QsjQd67ahUHosv5yleQeD0p6jGv4DrP_LBlyO9crnfBIerzCgByJk2p0o5yS1NEgQ4cSHoScGi6EMtRe17ElwdQFpFI4QdaPKVNcq0ZyTzLHbC_H-2vFTYughec2V9EMnhEyL3zIBhR1DNDNQ2ftXVx2VjYSE32fqPRw2jO8g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/Xt36FPFyXQGiZ7FZUEACgTG2M1yB12RTPJDWbxtzgE2figk1hDhkHL-DibX-sWyxTajOg-eUV6U3Sgwn6DNuyTtRnOzdZuwCGj0DFI9kr1Ig7tl7DDJcoisyCafZ8WafHcblney_YX-nvjdxHqjzKDGOWJpxD3WcqWHmw4KmaNN7jzB1OaGnjcEmjJLiJ3688l2xBkfNURwtlHhNVCwhLiQ45F1ncsPegqAs6u91ESsEn5daV9FQ_J2d1bPNJK6gszcJWATxCFWk1fTWS8dYdc809SwXda-ddWWbpmoy9C7iI6gYwbg44Lc4QWt4Xc0advQuX3r64_hkbx8QFTp8Xw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/diSBgv5wErS6hLtakI726MANbDRPUtujWHpuzEu-eJtoNCbhG1TMev2kLdkEIzbg03ZaRJbPEUS8h_hstSnYF9pVJR-H3f9gHLWSGJz2db4OF4XHgAP5jUcXkTusIU1R89LEQOEkbp-O2y949RazRBGSYUXJ2j0NCWkqtOjSRWinUyM36ZesVlWOKi680GgmslmIvx3d-0ySqgQr3mS99DiVZTI2R1lkuOUMUqUDYBAUV7jqpb9EBjkGYZKSrAz_s2BK62l-OVMSCW7NvwhgYfEcWJfK_QC3dF6q_XnKCEzIeLo1VEPUPsCpGzXJaP4TBp6j0dyuCxWAwMI0PowDzw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/65becd728e.mp4?token=nAov0VLi9XIwE-rjpeB7NAh2TafIBBXTNbjVHlwSGr7TU5TIVIYNj1dZFpE8UEkl37TutIE_o6ChmvZRGszSyq6qJxj9zyg1UbKEeeaTsiR_0L6qPW2kK8gZyQFkfHr-gI6jvAWPQ3IpCa7A7y60WAA21rGWbsirrwYK_IAZ1kkZTGZXae2n6WMZT9V79c3lYWJWTiX3n3awsXauvB71SKJS5y7e8HIsquJUajACk4rb28GghHy2OWIlmsVtmm-We4ZyJUktQ3sD5ILEGoqKpBBzOGHROWZw1gY3JnZF8GFEWWhR5iKaz6v7BX5k_fyQP1KK_Njg8hpc5jtj30TkoQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/65becd728e.mp4?token=nAov0VLi9XIwE-rjpeB7NAh2TafIBBXTNbjVHlwSGr7TU5TIVIYNj1dZFpE8UEkl37TutIE_o6ChmvZRGszSyq6qJxj9zyg1UbKEeeaTsiR_0L6qPW2kK8gZyQFkfHr-gI6jvAWPQ3IpCa7A7y60WAA21rGWbsirrwYK_IAZ1kkZTGZXae2n6WMZT9V79c3lYWJWTiX3n3awsXauvB71SKJS5y7e8HIsquJUajACk4rb28GghHy2OWIlmsVtmm-We4ZyJUktQ3sD5ILEGoqKpBBzOGHROWZw1gY3JnZF8GFEWWhR5iKaz6v7BX5k_fyQP1KK_Njg8hpc5jtj30TkoQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تصاویر دریافتی از دود یک آتش‌سوزی 'در میدان تجریش
#تهران
دوشنبه ۲۵ خرداد، الان'
Vahid
آپدیت در پست‌های پایین‌تر
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 263K · <a href="https://t.me/VahidOnline/76374" target="_blank">📅 18:51 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76373">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vjTZMhuR7g51Up_xq3XIhMFIU4TfHro3vchtHS8RZoKeCUabcTd0pUG76VBObwZEb1G0lhbor4l9Cxq1Iy-H_OB4RsXUKuIWJuabXZPu5xJDqAqctzUsCKo8X0OgA7-Y4nk-seabsqp9PwOFD_usqPn3oEaMtSEq1E1UDsSzeUWvcVLyyYc0hl6kUDi-Rl4FkgjrK2aNFrKiOF81d7Jzvs5hAH_T62XtmBlfPl6KQcam5U5CCHgQaT-NJnMHUX5NRkG2F69lqGOGzG1drBg4OWCLnoVKU2gcbKPvemPW7lhfAdU8-jYf5yx-MRjlCS9PraTl281hT8NlwKuSL-4EVg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرگزاری رویترز به نقل از منابع امنیتی لبنان و رسانه‌های دولتی این کشور گزارش داد یک حمله پهپادی اسرائیل خودرویی را در جنوب لبنان هدف قرار داد و راننده آن کشته شد.
این نخستین حمله مرگبار گزارش‌شده اسرائیل در لبنان از زمان اعلام توافق میان آمریکا و جمهوری اسلامی است.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 260K · <a href="https://t.me/VahidOnline/76373" target="_blank">📅 18:51 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76372">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SmYXXu7WhojiDlWLS0u0SR0GzXnkpPG-SKVpUnAa0pJ0mIDVRQC8nDLMyg8xRXHR2hzIp4k79qdDHVI6S4PtILWxL20vrBYY25aRxWCW-ev7sjJbvCeKqx6fTHZMeAZCHHhr6uSbgfapT5xH7HLS2tJ5uII4xMyZNl52SEqURQwGsBpBL2brP2Ds-5xOdOi82q1wtOMxIMvY4I-Fr3Uk7FBFJa6cKtXkkyihiNB6_VI49IKMlt4kOkCUaOi7lu9rGFNeErgLW51Yc-wC3bhQTNQRugGcFRFRGyd-L6dXqaiXbfqQIXvGKFDgug7MoHBToHoB2SbbvVOuuPUpDzmKPA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جی‌دی ونس، معاون رئیس‌جمهور آمریکا، روز دوشنبه ۲۵ خردادماه اعلام کرد آمریکا و ایران پیش از مراسم رسمی امضای توافق، روز یکشنبه (به وقت آمریکا) آن را به‌صورت دیجیتال امضاء کرده‌اند.
ونس در گفتگو با شبکه ای‌بی‌سی گفت توافق روز یکشنبه «به‌صورت دیجیتال» امضاء شده و قرار است مراسم رسمی امضای آن روز جمعه در ژنو برگزار شود.
در همین حال، مسعود پزشکیان، رئیس جمهوری ایران نیز، روز یکشنبه در مراسمی دولتی با اعلام همین خبر گفته بود، توافق روز جمعه و حضوری امضاء می‌شود.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 254K · <a href="https://t.me/VahidOnline/76372" target="_blank">📅 18:40 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76371">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Btmdrs7-6ZhCfi0nlIQZHb3KOubxVv0LV6ltz3MwLxpn8gmcDqWs3ZLgRjmC5_s-Si3_mF0Y6dMY1Wm0W-KrgeMnhR5nlxRZA9OpRtGrgAD8lZD6sBHiAuf3V2Rw37P6Igu5GMxsaoxplbEH_k2LXqHOIHqHve9gxhbhMu_MT82MdccofSvqWFvU5S9kDh6EGffLxvwbojNCAvB0l7vcGdYwfnhuJTZpu81P56O-ZluG4eYJq8V_K0VoCSfTBzC-HXjROY5EZ8tFOTXE-r_BCgn30mfpF1Q5v1DccH4QzHqo5svx4xY9rjhDvZI-ImWmSJNEo4PmPI3kIZFpzMmEFg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">با وجود اعلام مقام‌های بانکی درباره رفع اختلال در خدمات بانک‌های ملی، تجارت، صادرات و توسعه صادرات، خبرگزاری فارس وابسته به سپاه اعلام کرد که بخشی از خدمات غیرحضوری و اینترنتی این بانک‌ها همچنان با اختلال مواجه است.
پیش‌تر این بانک‌ها در اطلاعیه‌های جداگانه اعلام کرده بودند که تمامی خدمات کارتی و سامانه‌های اینترنتی و موبایل‌بانک به حالت عادی بازگشته است.
فارس گزارش داد در حال حاضر خدمات مبتنی بر کارت در پایانه‌های فروشگاهی و دستگاه‌های خودپرداز این بانک‌ها فعال می باشد، اما بخشی از خدمات اینترنتی و غیرحضوری همچنان دچار اختلال است.
شورای هماهنگی بانک‌ها، وابسته به ساختار بانکی جمهوری اسلامی، روز شنبه ۲۴ خرداد حمله سایبری به سامانه‌های چهار بانک ملی، تجارت، صادرات و توسعه صادرات را تأیید کرده بود.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 252K · <a href="https://t.me/VahidOnline/76371" target="_blank">📅 18:35 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76370">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jUKm_gK_6bWelnn8BgvqQ_UsPVC7lKuPGz8UuoJBGNtgZ-eiWEt2jeDJcKQ1k_6PItHenqxD5ceQ2PJ8F53FdLPHYx9-dAZxZn15Ru0j4CODm8cL4sSF9xvLnCHxmhFlzS5vK_ZIhy134E3EM12RnCvV8EoXaB9bC8sBonLtGOV9n9jsa53HMeMmMOgPrKlfkfPowami8FuQ351Cc2u0C4cTiZkRg2Tjkvh9N90iotgBP81ZyVEXuF-a1T9rs204C90iBzG_ewPJj3nXGSi9aWjgE5mbBKoL-B6z-0q7DRJB1T_Td2s8w5zIjeKVnGcxIFGCXPpdUYuzNpcdCz2jIw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">روز دوشنبه، به دنبال اعلام توافق ایران و آمریکا بر سر امضای تفاهم‌نامۀ پایان جنگ، قیمت ارزهای خارجی و سکه طلا در بازار آزاد ایران کاهش قابل توجهی یافت.
وب‌سایت‌های اعلام نرخ آزاد ارز و طلا، بعدازظهر روز دوشنبه قیمت هر دلار آمریکا را کمتر از ۱۶۲ هزار تومان اعلام کردند که نشان‌دهنده کاهشی در حدود ده هزار تومان از زمان اعلام توافق موقت است.
قیمت هر دلار آمریکا در روزهای گذشته بیش از ۱۷۱ هزار تومان گزارش می‌شد.
قیمت سایر ارزهای خارجی هم در بازار آزاد ایران کاهش مشابهی داشت.
همزمان قیمت هر سکه طلا در حدود ۱۶۷ میلیون تومان اعلام شد که نسبت به روز قبل کاهشی پنج میلیون تومانی را نشان می‌داد. این میزان کاهش در حالی رخ داد که قیمت طلا در بازارهای جهانی پس از اعلام توافق ایران و آمریکا افزایش یافته بود.
قیمت دلار و طلا در بازار ایران از زمان وقوع جنگ در ایران افزایش یافته و در روزهایی هر دلار آمریکا تا مرز ۱۹۰ هزار تومان هم معامله شده بود.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 231K · <a href="https://t.me/VahidOnline/76370" target="_blank">📅 18:34 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76369">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SMd7iPP0uqztNYsyy3KquVtQGucrDrcd5to9KLid8oHQGJU6axhjVJpvscjg5voNWqaDTDpZzL3MMuC3KmWh7V0FpLXVdnEdW5zJ7Z2vwMmx6Z-WJQeuK7hGYQ49V93lTbRVbaYSya5MYXvRIErYXp3MUcXesyxrIsJbkH4Q8YqQnehBk9eC3u1NfasrJhUcaEtUY0Y6sAjXgDe7Dy3REocKxDhe0u0uB8_H_yhjhJQJbhgpFHU5Hbz_SpGDBBqmC3JdcL59JTs2SXlx7X1fPVnGJnAQFdazVGVkEdAaN-owE9uA8m_GKvjC0dAzw_h0_iOCrVeMO-LFfULjRmOv2w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دونالد ترامپ، رئیس‌جمهور آمریکا، روز دوشنبه ۲۵ خردادماه در پیامی در شبکه اجتماعی تروث سوشال اعلام کرد کشتی‌ها، از جمله نفتکش‌های حامل نفت، حرکت از تنگه هرمز را آغاز کرده‌اند.
ترامپ نوشت: «کشتی‌ها در حال حرکت هستند؛ بسیاری از آن‌ها با نفت بارگیری شده‌اند و از تنگه هرمز خارج می‌شوند. آن‌ها از مسیر جنوبی حرکت می‌کنند؛ مسیری که کاملا امن، مطمئن و پاک است.»
رئیس‌جمهور آمریکا همچنین افزود: «مسیرهای دیگری نیز برای تردد وجود دارد.»
پیام ترامپ در حالی منتشر می‌شود که صدا و سیمای جمهوری اسلامی ایران، روز دوشنبه در گزارشی تصویری اعلام کرده بود: «بیش از ۹۶ ساعت است که نیروی دریایی سپاه هیچ مجوز عبوری صادر نکرده است.»
پیشتر رویترز گزارش داده بود، نخستین نفتکش حامل گاز طبیعی مایع پس از اعلام پایان جنگ جمهوری اسلامی ایران و آمریکا، صبح دوشنبه از تنگه هرمز عبور کرده است.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 222K · <a href="https://t.me/VahidOnline/76369" target="_blank">📅 18:33 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76368">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bra1ZLL1otXdbllUz4ra5vw9dSRAPgSKAWvw_rb4jckDGv1nuJ0egMO1J8XKzHAH4HKG9CHBVUZ-tGju0SkfLBydEHhm96a_LRjUPeILjbXI9Ks0P5L65wEkPwkrFRSiccRDfw7lFNsWMysZyzNegj6waLX7q57onmhgiKr9e_1nnQNSmGUI5Y2f5hGxPmZUZucLJ0QPbySL4hUrgWzzLLe9shZqXQ0R0160PVF0-QUw_aw-YNk4JxuZ-ztcljETJB0UpGXRyGfVjmFe6cu1vCbLSC8qrXQ3MPCT6-K0n0A826x5UfmUbFB1YBeCTk-RzE0tHykiOh_t8YZqu2khNQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">معاون رئیس‌جمهور آمریکا می‌گوید تفاهم‌نامه ایران و آمریکا روز جمعه در حضور عباس عراقچی و محمد‌باقر قالیباف در سوئیس امضا خواهد شد.
جی‌دی ونس گفت که «جزئیات زیادی از توافق هنوز حل‌و‌فصل نشده است» اما آمریکا انتظار دارد که تنگه هرمز «در درازمدت بدون عوارض باز باشد.»
سخنگوی وزارت خارجه جمهوری اسلامی اما گفته است که هنوز مشخص نیست که چه کسی از جانب ایران تفاهمنامه را امضا می‌کند.
اسماعیل بقایی همچنین تاکید کرد که ایران «به‌دنبال گرفتن عوارض نیست» اما «هزینه ارائه خدمات» را دریافت خواهد کرد.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 217K · <a href="https://t.me/VahidOnline/76368" target="_blank">📅 18:33 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76367">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vV-LMxQLpEPaoTcXqO_payPkcNAC5w3IDjAhj_nW3Ns1kiSjpUQFO1nJZsrWl97uscbuu4w0MNeW3dAc1-PmirnfUGwjKnhOKb31Q8tvAMtq4zg-Nej0lIRt-EZ5_BAPPXDiR9Eu1hotfK3l_PN_jbpEQHp49dB4SX4k53J9Nj0k_-IvGd1SP_ToCiuZscB5I5ObjkmyWVQRyXuJp1gyCHCqfrUcSbsLsDUCBG4A4krOPpZ_3Ees9u_j8uSdpe5opjLMIbverrYB0vouEPERdpe86hiJwf8F12Uhe7ifjIfyM-gS5mVUkH0oVV5mkP2Ne9qkI23jrj-AAaBPblrf0Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">«نوید عالم‌چهره» ۴۴ ساله، ساکن ملک‌شهر اصفهان و پدر دو دختر، روز جمعه ۱۹ دی‌ماه ۱۴۰۴ هدف شلیک گلوله جنگی قرار گرفت و جان خود را از دست داد.
به گفته منابع آگاه، گلوله جنگی از پشت به پهلوی او اصابت کرده بود.
خانواده می‌گویند نوید عالم‌چهره هنگام مجروح شدن هنوز هوشیار بود و توسط اعضای خانواده به بیمارستان غرضی اصفهان منتقل شد.
به گفته آنان، کادر درمان پس از تحویل گرفتن او اعلام کردند که برای عمل جراحی به اتاق عمل منتقل خواهد شد.
نزدیکان نوید می‌گویند تا صبح مقابل بیمارستان منتظر ماندند، اما با باز شدن درهای بیمارستان و مراجعه برای پیگیری وضعیت او، دیگر اثری از نوید پیدا نکردند. به گفته نزدیکان، پس از دو روز جست‌وجو و مراجعه به مراکز مختلف، سرانجام پیکر او را در سردخانه باغ رضوان اصفهان پیدا کردند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 237K · <a href="https://t.me/VahidOnline/76367" target="_blank">📅 18:32 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76366">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mHN_FOckJWv4REBKM91Pmdk8guRgGedrWXqi7n0QTWzVoVOCDmQNOfHMp6395U_lMG0V8ePqCai_w3dbTb628PJZetXMUTXre5T56k6eoV--O-Q4IcmosqrDlaAwrJf8xKhaa9zbjhHmcAM58a84om4HxlYSf4Gc9WYeov4-1W6X-jzlhLApEo68tD79sfBERa8qC5zAbgtwypvg09xKGAMWjNJFFD53TSI9G7v2ZPwhO8FbvlWizZ4DCBeo6c7dT-6rxZfFHlOwKWx5vlCmUwaoB9tlVfSP44bn8xLXn6voEGwoNeukMYnC4xzraC6eqczn2b8ps6HU-0ODl7FYQg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کمیسر عالی حقوق بشر سازمان ملل اعلام کرد که از آغاز سال جاری میلادی تاکنون، دست‌کم ۴۰ نفر در ایران به اتهام‌های مرتبط با «امنیت ملی» اعدام شده‌اند که در میان آن‌ها ۱۸ معترض نیز دیده می‌شود.
ولکر تورک روز دوشنبه ۲۵ خرداد افزود: «مقامات دست به سرکوب شدید زده‌اند، هزاران نفر را بازداشت کرده و محدودیت‌های بیشتری بر فضای مدنی اعمال کرده‌اند».
او در بخش دیگری از اظهاراتش از اعلام توافق صلح میان ایالات متحده و ایران استقبال کرد و از همه طرف‌ها در منطقه خواست حداکثر خویشتنداری را رعایت کنند.
تورک گفت: «از اعلام این‌که ایالات متحده و ایران بر سر یک توافق صلح به تفاهم رسیده‌اند که شامل آتش‌بسی فوری و دائمی، بازگشایی تنگه هرمز و چارچوبی برای ادامه مذاکرات است، استقبال می‌کنم».
او افزود: «در این مقطع حساس، روشن است که همه طرف‌ها باید حداکثر خویشتنداری را به خرج دهند و برای اجرای سریع و با حسن نیت توافق حاصل‌شده تلاش کنند».
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 239K · <a href="https://t.me/VahidOnline/76366" target="_blank">📅 18:31 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76362">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/beda093be0.mp4?token=qaqVUYd-jXmaTlsBhElGHC2jnPurzq0ndEktvDKG_QHWJ1rPmD43T9NFZyNj0RHsTrsU7742b0rflGQjPuuiqB1SXI7Ayhc_EeERyQ8NlhNm8XTd9rg5mt_7QWN1ynxP72aeJuTDRs2OmuIioTeai4iwjMgmCrXhFA35wrOS1gLQW-XXXHo-TumbZtrDaEDlsbL1hlqGOH4CUKRL8hYbkM4JQK1CuBfoaRMdzAL9Qg41KNWJ9Kj9Rpe8QFnnnEiGNkYQjG4KCLy5z9EOf3fUL2EGajFgXB09yqhdohRxOY81RMFC9dTW3bn6VnZ3kTbEFqPUwzECykzZNrNsknXUxw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/beda093be0.mp4?token=qaqVUYd-jXmaTlsBhElGHC2jnPurzq0ndEktvDKG_QHWJ1rPmD43T9NFZyNj0RHsTrsU7742b0rflGQjPuuiqB1SXI7Ayhc_EeERyQ8NlhNm8XTd9rg5mt_7QWN1ynxP72aeJuTDRs2OmuIioTeai4iwjMgmCrXhFA35wrOS1gLQW-XXXHo-TumbZtrDaEDlsbL1hlqGOH4CUKRL8hYbkM4JQK1CuBfoaRMdzAL9Qg41KNWJ9Kj9Rpe8QFnnnEiGNkYQjG4KCLy5z9EOf3fUL2EGajFgXB09yqhdohRxOY81RMFC9dTW3bn6VnZ3kTbEFqPUwzECykzZNrNsknXUxw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بهروز رضوی، گوینده محبوب علی خامنه‌ای، درگذشت.
FattahiFarzad
بهروز رضوی، گوینده، صداپیشه، ترانه‌سرا و بازیگر، پس از دوره‌ای بیماری در ۷۸ سالگی درگذشت.
او فعالیت حرفه‌ای را از سال ۱۳۴۷ با گویندگی در رادیو آغاز کرد و طی بیش از پنج دهه فعالیت، به یکی از شناخته‌شده‌ترین صداهای رسانه‌ای ایران بدل شد. روایت مجموعه مستند «ایران» از جمله ماندگارترین آثار او به شمار می‌رود.
بهروز رضوی علاوه بر فعالیت در رادیو و تلویزیون، در سینما و دوبله نیز حضور داشت و در آثاری چون «گناه فرشته»، «سفر به چزابه» و «نجات‌یافتگان» ایفای نقش کرده بود.
او همچنین شاعر ترانه‌های «کویر دل» و «گمشده» با صدای مرجان بود.
این هنرمند متولد یزد از سال ۱۳۷۴ در کرج زندگی می‌کرد و برادر عاطفه رضوی، بازیگر و چهره‌پرداز، است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 357K · <a href="https://t.me/VahidOnline/76362" target="_blank">📅 18:29 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76361">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cLbd0mfteFRedzw4audHLIptTCBFnK1TWq8JyIKOgQwYiymXJJJianephTLlrXjmu6o7LH1PzkQNhUrbx1ZqEb36_smQlrwrCiF6XRFcx10AJB3JXcaZwFwpB1tV6iusGanS6n60pLnbtE9SpWwU8et9Hu-eeMD_e_Kd-CfciOq2qZiiHW2n3w0XZy8-Ui7clfd0hwENCofyh9X7i8NfJgnU9aPxJ2ahnQH51PzzEtIVSfFHLYgAmcWfTs-pb5QcArs9iRh8fbUiwDiTMG0nWt5NfeNtTm-91Jj1wCGLAb31Kl4i2a8XjKsOU8345a5FvoT3SN5Y9bqAEytwPsbGQQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">به گفته دو مقام جمهوری اسلامی که نیویورک‌تایمز نام آنها را اعلام نکرده، تهران تا پس از عبور ساعت از نیمه‌شب به وقت محلی صبر کرد تا توافق را نهایی کند، زیرا نمی‌خواست این رویداد مهم با روز تولد دونالد ترامپ، رئیس‌جمهوری آمریکا، در روز یکشنبه هم‌زمان شود.
بر اساس این گزارش، اختلاف زمانی هفت‌ونیم ساعته میان تهران و واشینگتن باعث شد هر دو طرف بتوانند روایت مورد نظر خود را از زمان نهایی شدن توافق ارائه دهند. ترامپ گفته بود توافق در روز یکشنبه نهایی شده، در حالی که ایران اعلام کرده بود این روند در روزی بعد از آن تکمیل شده است. دونالد ترامپ ۱۴ ژوئن ۱۹۴۶ به دنیا آمده است.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 464K · <a href="https://t.me/VahidOnline/76361" target="_blank">📅 03:44 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76360">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">مصاحبه ترامپ با نیویورک‌تایمز، ترجمه ماشین:
رئیس‌جمهور ترامپ بعدازظهر یکشنبه در مصاحبه‌ای گفت توافقی که با ایران به دست آورده، در نهایت تضمین خواهد کرد که تنگه هرمز  «برای همیشه بدون عوارض» باشد و استدلال کرد که با وجود مخالفت‌های بنیامین نتانیاهو، نخست‌وزیر اسرائیل، او اسرائیل را از نابودی هسته‌ای نجات داده است.
آقای ترامپ همچنین اصرار کرد که اگر ایران نتواند به توافق نهایی هسته‌ای با ایالات متحده برسد ــ روندی که دستیارانش می‌گویند انتظار دارند روز جمعه در سوئیس آغاز شود ــ او حملات نظامی به تهران را از سر خواهد گرفت یا در ازای دریافت ۲۰ درصد از درآمدهای منطقه، ایالات متحده را به «نگهبان خاورمیانه» تبدیل خواهد کرد.
در یک گفت‌وگوی تلفنی ۲۸ دقیقه‌ای که آقای ترامپ از محل اقامتش در کاخ سفید آغاز کرد، و در یک تماس کوتاه بعدی، رئیس‌جمهور ادعا کرد که تصمیمش برای حمله به ایران در اواخر فوریه و محاصره دریایی بعدی بنادر این کشور پس از آنکه تهران تنگه را بست، خاورمیانه را به سود آمریکا دگرگون کرده است.
او که در روز تولد ۸۰ سالگی‌اش صحبت می‌کرد و صدای جمع شدن خانواده‌اش برای شام جشن تولد در پس‌زمینه شنیده می‌شد، از دو رهبر اقتدارگرا ــ شی جین‌پینگ، رئیس‌جمهور چین، و ولادیمیر وی. پوتین، رئیس‌جمهور روسیه ــ به‌خاطر کمک به این توافق تمجید کرد و
آقای نتانیاهو را به‌دلیل انجام حملاتی که نزدیک بود توافق نهایی را از مسیر خارج کند، به‌شدت مورد حمله قرار داد.
آقای ترامپ درباره نخست‌وزیر اسرائیل گفت: «او آدم بسیار دشواری است، و صادقانه بگویم باید بابت این کار از ما بسیار سپاسگزار باشد. چون اگر ایران سلاح هسته‌ای داشت، اسرائیل دو ساعت هم دوام نمی‌آورد.»
با اینکه متن توافق هنوز منتشر نشده است، به نظر می‌رسید آقای ترامپ در حال توصیف امتیازهایی از سوی ایران است که این کشور هنوز نداده، یا به مذاکرات بعدی موکول شده است. برای مثال، تفاهم‌نامه فقط عوارض عبور از تنگه را به مدت ۶۰ روز تعلیق می‌کند و سپس وعده گفت‌وگوی منطقه‌ای درباره آینده را می‌دهد.
ایران پیش از جنگ هرگز عوارضی دریافت نمی‌کرد، بنابراین آقای ترامپ در اصل در حال جشن گرفتن بازگشت به وضعیت پیش از جنگ است.
آقای ترامپ بارها تفاهم‌نامه جدید خود را با توافق سال ۲۰۱۵ میان باراک اوباما، رئیس‌جمهور وقت، و رهبری ایران مقایسه کرد و گفت توافق او تضمین خواهد کرد که ایران «نتواند سلاح هسته‌ای تولید یا خریداری کند». ایران زمانی که در سال ۱۹۷۰ پیمان منع گسترش سلاح‌های هسته‌ای را تصویب کرد، با این موضوع موافقت کرده بود و در صفحه نخست توافق دوران اوباما نیز دوباره بر آن تأکید کرد.
در سه ماه گذشته مذاکرات، که به رهبری استیو ویتکاف، فرستاده ویژه رئیس‌جمهور، و جرد کوشنر، داماد او، انجام شد، ایرانی‌ها اصرار داشتند که هرگز از حق خود برای غنی‌سازی اورانیوم تحت آن پیمان دست نخواهند کشید.
آقای ترامپ گفت هنوز بر سر این موضوع مذاکره می‌کنند که آیا ایران غنی‌سازی خود را برای ۲۰ سال تعلیق خواهد کرد یا نه ــ ترامپ تلویحاً گفت شاید به تعلیق ۱۵ ساله رضایت دهد ــ اما گفت ایران برای همیشه به غنی‌سازی در سطوح پایین محدود خواهد شد؛ سطوحی که «هرگز نمی‌تواند از سوی ارتش استفاده شود».
توافق دولت اوباما نیز همین شرط را داشت، اما پس از آنکه آقای ترامپ در سال ۲۰۱۸ آن توافق را کنار گذاشت، ایران غنی‌سازی در سطوح بسیار بالاتر را آغاز کرد؛ از جمله اورانیوم نزدیک به سطح مورد نیاز برای بمب، با غنای ۶۰ درصد.
در جریان این گفت‌وگو، رئیس‌جمهور حال‌وهوایی شادمانه داشت و درباره رویداد آتی «یو‌اف‌سی» که قرار است در محوطه جنوبی کاخ سفید برگزار شود و احتمال اینکه باران آن را مختل کند، صحبت کرد. او گفت: «در زمان جنگ چنین چیزهایی پیش می‌آید.»
nytimes
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 415K · <a href="https://t.me/VahidOnline/76360" target="_blank">📅 03:18 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76359">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/129bb5a743.mp4?token=O8jwWuFK2LuQkAbrnOd1SUdr3Jz7TaSMaa9R-jxqjKegmDRVVoyhfL1HMXb83ggqrhOlbnjtvaj6hTe_kkw6l3zip65pDTDAVqdzsB_SjW9I0YcO5SB4IKCxE1saXpQRDx8OGS6W6hpkrdwMxWShd9v3te8JMliw7LZTdYhCojPe8fdHC3c4Hsh2EYs1pqn9IY0oFntHFnkIcyUVgwsvN77liflGEgZMSj9Tpi1cFmY_ogidFADHQtQmEgCTVDhWWzOob6Ak4PQ6EsqRV0s09ZvTUo5IyxvHqbXRssYujmtpp45vS_NITRBLlWmSLbYOOy6HX0xx85zXJdoCAEoe7g" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/129bb5a743.mp4?token=O8jwWuFK2LuQkAbrnOd1SUdr3Jz7TaSMaa9R-jxqjKegmDRVVoyhfL1HMXb83ggqrhOlbnjtvaj6hTe_kkw6l3zip65pDTDAVqdzsB_SjW9I0YcO5SB4IKCxE1saXpQRDx8OGS6W6hpkrdwMxWShd9v3te8JMliw7LZTdYhCojPe8fdHC3c4Hsh2EYs1pqn9IY0oFntHFnkIcyUVgwsvN77liflGEgZMSj9Tpi1cFmY_ogidFADHQtQmEgCTVDhWWzOob6Ak4PQ6EsqRV0s09ZvTUo5IyxvHqbXRssYujmtpp45vS_NITRBLlWmSLbYOOy6HX0xx85zXJdoCAEoe7g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">قالیباف پیش از چنج‌رژیم: مذاکره با قاتل سلیمانی شرافتمندانه نیست
همزمان با انتشار خبر توافق میان واشنگتن و تهران، ویدیویی از اظهارات محمدباقر قالیباف، رئیس مجلس شورای اسلامی، در روز شنبه ۲۰ بهمن‌ماه ۱۴۰۳ بار دیگر در شبکه‌های اجتماعی بازنشر شده است.
قالیباف در ششمین همایش ویژه فرماندهان و کارکنان ستاد فرماندهی سپاه، در پاسخ به پرسشی درباره تفاوت کامالا هریس و دونالد ترامپ گفته بود: «حتما فرق دارد، ترامپ قاتل شهید سلیمانی است. مگر ما می‌توانیم بی‌تفاوت باشیم؟ پس حتما برای ما فرق می‌کند.»
او همچنین با اشاره به مواضع علی خامنه‌ای درباره مذاکره با آمریکا گفته بود: حضرت آقا می‌فرمایند شرافتمندانه نیست، خب شرافتمندانه نیست.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 376K · <a href="https://t.me/VahidOnline/76359" target="_blank">📅 02:58 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76357">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/KZYhEm-4Kj4LVXLerCkh9_XrYtlJuUx1Poy5g378W957JQw130q_tjoXuF-uAqEwd-8ms8Ect2_EbDhEO9nG2-oJ9ateGjsaoHg4uffNiymjYkY3BJa1gueONdpP1wZ2yt42i1ye5h8TUZ4MIoymh5mdqI1DWeueyKPSOiwiV05iBZMoQPJN9vHVt4TZSxUydat-y3dNs0XxBTZPaepeBXIZPtAyUFzNtg7xva27KPqDm0A1BuTGECSr5KIjSOYv3a4h4hGYpww8hBfwmUWrJurmndPeI2oWnY8kaJ-nGuu8AylDnY3uhCVhy5JNqco7J6nW4meCQuL4B27Rb_bLYg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/G-ihrsgr0nwCK8eLREb8Gy4NBLeP_-jOxJSifn0YgWljY6kOCtsPxbaKUdPuURXUY5TaR99MynFobqwRMPqDPFfYCFQVV6h2W4Sqew8UN9-qV4-ZqPUYLHAu-X028ZpujOcNxcKmjqAI0D38pH-EGElmk1O_5DGLdx8NXSOFjN0dvBObUJyY6SNjthV6YmIIHAEl2w60OJ0d1c1eheAPmzGPoMxDzmqseZm2JNBSUGhh-gzetkZPOkSKBjeOn2ba0kZYNfoV_eOzucn8tF5EH7tyFRgOKBr9ubwSfEUZnBnN-o5oPaet46kxoKBYQX-WG3n8yM0AcSa3KJfjpTExZw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">کی‌یر استارمر، نخست‌وزیر بریتانیا، اعلام کرد که از توافق اعلام‌شده میان آمریکا و حکومت ایران «به گرمی استقبال می‌کند» و آن را «گامی بسیار مهم رو به جلو برای پایان دادن به جنگ، تضمین ثبات منطقه و بازگشایی تنگه هرمز» توصیف کرد.
استارمر در بیانیه‌ای که روز یکشنبه در شبکه‌های اجتماعی منتشر کرد، افزود: «ما آماده‌ایم از گفت‌وگوهای فنی که اکنون آغاز خواهد شد حمایت کنیم. اولویت ما این است که این توافق به صلحی پایدار و ماندگار تبدیل شود و برای تحقق این هدف با شرکای بین‌المللی همکاری خواهیم کرد.»
او گفت حمایت بریتانیا می‌تواند، در صورت نیاز، شامل «راه‌اندازی ماموریت دفاعی، مستقل و چندجانبه‌ای باشد که بریتانیا و فرانسه تاکنون نقش پیشرو در برنامه‌ریزی آن داشته‌اند؛ به‌ویژه برای ارائه کمک در زمینه پاکسازی مین‌ها» در تنگه هرمز.
نخست‌وزیر بریتانیا همچنین تاکید کرد: «موضع قاطع و دیرینه بریتانیا همچنان این است که ایران هرگز نباید به سلاح هسته‌ای دست یابد.»
@
VahidOOnLine
امانوئل مکرون، رئیس‌جمهوری فرانسه، بامداد دوشنبه ۲۵ خردادماه در پیامی در شبکه اجتماعی اکس از توافق حاصل‌شده میان واشنگتن وتهران استقبال کرد و خواستار اجرای سریع و کامل آن از سوی همه طرف‌های درگیر شد.
مکرون گفت این توافق باید زمینه بازگشایی فوری و بدون قید و شرط تنگه هرمز را فراهم کند. او افزود ماموریت بین‌المللی ایجادشده با همکاری بریتانیا آماده پشتیبانی از این روند است و ازسرگیری تردد دریایی بدون محدودیت و عوارض، برای ثبات منطقه‌ای و اقتصاد جهانی ضروری است.
رئیس‌جمهوری فرانسه همچنین گفت این توافق می‌تواند راه را برای مذاکراتی گسترده‌تر درباره برنامه هسته‌ای و موشکی ایران و مسائل امنیتی خاورمیانه هموار کند. او تاکید کرد فرانسه آماده است در کنار شرکای خود برای دستیابی به صلحی پایدار در منطقه نقش‌آفرینی کند.
مکرون در بخش دیگری از پیام خود بر حمایت فرانسه از تلاش‌های دولت لبنان برای بازگرداندن حاکمیت کامل این کشور تاکید کرد و گفت برقراری آتش‌بسی پایدار برای تحقق این هدف ضروری است.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 361K · <a href="https://t.me/VahidOnline/76357" target="_blank">📅 02:53 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76356">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/NasP4pHL-3vyW0mKpkRNV67VhH1aACgDRSmEWD6ojnVu5pkQDlpc_yEQyt6w81WlH52Q-ALcVeKpSWtBi5IUSGuz7__gwMszDeBPQKJTsHZltEwtVLWIUiAkSUfdDP-zH9i1npd67YsIgn4bQ0MLJgM9zLQro0034bFY54UktCl6feaynV5F2Gthy3GoUmBCoI3iFzeSQHcSeci7C4OMXqibdxIxucHm7Yx4xNwCFQAejLwyCpbhy9z7Fq27BK1Vw2Vu9Ptb0Ojf0Lb42Dm-MwmKOQ2lf8-5OIvJOs5cSA6puX8srmY7gMVRZLGs_ZWdqf8Th9c3yH2n-I9ezHaBpw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">روزنامه معاریو به نقل از منابع اسرائیلی گزارش داد بنیامین نتانیاهو، نخست‌وزیر این کشور، در گفت‌وگو با دونالد ترامپ، رییس‌جمهوری آمریکا، به صراحت اعلام کرد که اسرائیل خود را به بند مربوط به لبنان در توافق میان آمریکا و حکومت ایران متعهد نمی‌داند.
بر اساس این گزارش، نتانیاهو گفت که ارتش اسرائیل از لبنان عقب‌نشینی نخواهد کرد، در مواضع فعلی خود باقی خواهد ماند و به اقدامات خود برای خنثی کردن تهدیدهای حزب‌الله، از جمله نابودی زیرساخت‌های تروریستی و پاسخ به هرگونه حمله علیه اسرائیل، ادامه خواهد داد.
به نوشته معاریو، برداشت منابع اسرائیلی آن است که «توافق احتمالی ایالات متحده با ایران، دست اسرائیل را در عرصه لبنان نخواهد بست. پیام اصلی این است: اسرائیل منافع امنیتی-راهبردی مستقلی در لبنان دارد و قصد دارد بر آن پافشاری کند.»
این روزنامه نوشت: «اکنون باید دید این شفاف‌سازی‌ها — فراتر از تماس تلفنی نتانیاهو و ترامپ — در بوته واقعیت چگونه عمل خواهد کرد.»
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 317K · <a href="https://t.me/VahidOnline/76356" target="_blank">📅 02:33 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76355">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">بیانیه دبیرخانه شورای عالی امنیت ملی:
متن یادداشت تفاهم پایان جنگ پس از چند ماه مذاکره فشرده نهایی شده است
جنگ در تمامی جبهه‌ها از جمله لبنان از امشب به صورت فوری و دائمی پایان می‌یابد
متنی که در خبرگزارهای حکومتی منتشر شده:
بیانیه دبیرخانه شورای عالی امنیت ملی درباره توافق پایان جنگ
میان ایران و آمریکا
بسم الله الرحمن الرحیم
به اطلاع ملت شریف ایران می رساند:
▪️
جمهوری اسلامی ایران در پرتو راهبری رهبر شهید خویش، تفوق خود در برابر دشمن امریکایی صهیونی را تکمیل کرده و ذیل تدابیر رهبری عالی قدر نظام (حفظه الله تعالی)، حمایت های آحاد مردم و تلاش مجاهدانه رزمندگان اسلام، به دنبال یک دوره مذاکرات دشوار و فشرده چند ماهه، و بر اساس مصوبه شورایعالی امنیت ملی، متن یادداشت تفاهم در خصوص مذاکرات پایان جنگ (مذاکرات اسلام آباد) را میان ایران و امریکا در شامگاه 24 خرداد ماه، نهایی کرد.
▪️
بر اساس توافقات انجام شده، جنگ و عملیات نظامی در تمامی جبهه ها از جمله لبنان از امشب به صورت فوری و دائمی پایان یافته و به علاوه، محاصره دریایی علیه ایران بلافاصله و به طور کامل خاتمه می‌یابد.
▪️
امضای این یادداشت تفاهم در روز جمعه 29 خرداد به طور رسمی انجام خواهد شد.
▪️
مذاکرات برای توافق نهایی، به پس از اجرای تعهدات طرف مقابل وفق یادداشت تفاهم موکول خواهد شد. جمهوری اسلامی ایران از تلاش های جمهوری اسلامی پاکستان و دولت قطر قدردانی می کند.
والسلام علیکم و رحمت الله و برکاته
دبیرخانه شورای عالی امنیت ملی
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 316K · <a href="https://t.me/VahidOnline/76355" target="_blank">📅 02:26 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76354">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/8a76f7084c.mp4?token=sG1oqKLzm4CrYcH4r4AtXKYGOX-U12XOmmw4FAcEgUBsQkF562W7R1dIRD3Cl6rCV9436uNnNUVwfk-HNAsPRKAQbn-payIS5fytzMAa19UBN4EXAtj35NqvYTERyThhQJFo-8hNIONzFy_YZcrLRuS2DSauHr3kJLe8gt2b1w1eRrhmNVAuo-x61ntQo6ofw752EhHfvSp-xt24gcS0jDdPITRk1F-ah_vlxBzUZStGP7vxs79TYfumFbOC9sWvRW9LPjuTg899cSJDE_2sJB_V64nz8ZwdZb9hUkkYHFFIfwyHQHi3omRSoVw-8VDh52w-XgJhns2BThCx1E1gOw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/8a76f7084c.mp4?token=sG1oqKLzm4CrYcH4r4AtXKYGOX-U12XOmmw4FAcEgUBsQkF562W7R1dIRD3Cl6rCV9436uNnNUVwfk-HNAsPRKAQbn-payIS5fytzMAa19UBN4EXAtj35NqvYTERyThhQJFo-8hNIONzFy_YZcrLRuS2DSauHr3kJLe8gt2b1w1eRrhmNVAuo-x61ntQo6ofw752EhHfvSp-xt24gcS0jDdPITRk1F-ah_vlxBzUZStGP7vxs79TYfumFbOC9sWvRW9LPjuTg899cSJDE_2sJB_V64nz8ZwdZb9hUkkYHFFIfwyHQHi3omRSoVw-8VDh52w-XgJhns2BThCx1E1gOw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خبرگزاری فارس:
‌غریب‌آبادی، معاون وزیر خارجه: در مذاکرات ۶۰ روزه در مورد چند موضوع بحث خواهیم کرد:
🔸
۱. خاتمه تمام تحریم‌ها و قطعنامه‌های شورای امنیت
🔸
۲. موضوعات هسته‌ای
🔸
۳. تعیین سازوکار نهایی بازسازی ایران
🔸
۴. تعیین سازوکار اجرایی برای نظارت بر تعهدات طرفین
خبرگزاری مهر:
جزئیات جدید از پیش‌نویس تفاهمنامه ۱۴ ماده ای ایران و آمریکا
جزییات این پیش‌نویس به شرح ذیل است:
۱- توقف دائمی و فوری جنگ در همه جبهه ها از جمله لبنان
۲- تعهد آمریکا به عدم مداخله در امور داخلی ایران و احترام به حاکمیت جمهوری اسلامی ایران.
۳- رفع کامل محاصره دریایی ظرف ۳۰ روز
۴- تعهد آمریکا به خروج نیروهایش از پیرامون ایران
۵- بازگشایی تنگه هرمز ظرف ۳۰ روز با ترتیبات ایرانی
۶- تعلیق تحریم های فروش نفت، محصولات پتروشیمی و مشتقات و دسترسی کامل ایران به منابع مالی آن.
۷- لزوم ارائه طرح های بازسازی ایران حداقل به مبلغ ۳۰۰ میلیارد دلار توسط آمریکا و متحدانش
۸- ۶۰ روز مذاکره برای رسیدن به توافق نهایی مبتنی بر موضوعات هسته ای و لغو کامل تحریم های اولیه، ثانویه، آمریکا و قطعنامه های شورای امنیت سازمان ملل و شورای حکام آژانس بین المللی انرژی اتمی
۹- تکرار تعهد ایران در پیمان ان پی تی مبنی بر عدم تولید سلاح هسته ای
۱۰- در دوره مذاکرات آمریکا متعهد شده به نیروهای خود در منطقه اضافه نمی کند و تحریم جدیدی هم وضع نخواهد کرد.
۱۱- آزادسازی ۲۴ میلیارد دلار پول های بلوکه شده ایران در دوره ۶۰ روزه مذاکرات نهایی. نیمی از این مبلغ قبل از شروع مذاکرات باید در دسترس ایران قرار گیرد.
۱۲- تشکیل سازوکار نظارتی برای اجرایی کردن توافق.
۱۳- توافق نامه نهایی توسط قطعنامه شورای امنیت سازمان ملل به تایید می رسد.
۱۴- مذاکره نهایی قبل از آزادسازی نیمی از پول های بلوکه شده ایران، تعلیق تحریم های نفتی ایران و رفع محاصره دریایی آغاز نمی شود و توافق نهایی صرفا در موضوع سرنوشت مواد غنی شده و غنی سازی، رفع تحریم ها، برنامه بازسازی اقتصاد ایران انجام می شود و بحث درباره برنامه موشکی ایران و حمایت از گروه های مقاومت به صورت قطعی از دستور کار خارج شده است/مهر
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 303K · <a href="https://t.me/VahidOnline/76354" target="_blank">📅 02:11 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76353">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/hoZokdI9yRyxYiAv8MiDDj0hrCH3LO2I0nYqN0ChLxrZmkemBy2vvZ-T6Q1--uz7HaucWoFmhp3nyH_K2-S4JhTxLC2zWKOL988rvKYN_TzHAph-Hvtl2CbtWCTKEgPm9UdLWYVFtFzFTB76HOs4-A39MKSxIjo3OkZpNVAatUf_QI5Oj3SOHmEKT7C-D4ShGWNsvWhT8g-J_Hm15IQ6rR1QWKiFQ41AKz8l_Qka4l0Yl6mcG19dje7SWwNRix4PyOrWH-NKdNnX7e-KXnlPJ838icm7G-ZT8n8UvQzAYv-7ZFvX3bmdvokZYnxSQtV1DTQRO5wNfCvavhmnOt4CVA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ: تنگه هرمز جمعه پس از امضا باز می‌شود
روسای جمهور پیش از من در رسیدن به صلح با ایران شکست خورده بودند
پست ترامپ، ترجمه ماشین:
این توافق بزرگ، صلح و امنیت را برای کل منطقه به ارمغان خواهد آورد. بسیاری از رؤسای‌جمهور تلاش کردند با ایران صلح کنند، اما همه پیش از من شکست خوردند. رهبران منطقه، برای نخستین بار، رئیس‌جمهوری را یافته‌اند که می‌تواند به آن‌ها کمک کند به صلح واقعی دست پیدا کنند.
با باز شدن تنگه پس از امضای توافق در روز جمعه، برای مقاصد مربوط به پاک‌سازی مین‌ها، نفت دوباره از هر دو سوی آن برای منطقه و جهان جریان خواهد یافت!
رئیس‌جمهور دونالد جی. ترامپ
realDonaldTrump
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 297K · <a href="https://t.me/VahidOnline/76353" target="_blank">📅 02:01 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76352">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/da696e6ada.mp4?token=YqxX6lSGqg9ZwJSHT6Wpm1ErYruKhrwWc-RDZx8v6TDQ6fK0lVfSu5jr7RpTJx0-BWEMUb0A1r81DOFA1_DoliUPaiknI6Q3N6fYGU7TRUiFLApAzcl9kZfjCuoda_2MafHvMnO45EeYdsLHZBM9pXyo1rBr81ConU1gbr545-LDgtceXeJqVGJWQ4nOCQdjbqRcSDgQ3HQ4obM74mr6icmOmkJWXOxX-AyJHwBcwFY5L3pgp5ImRd11E3C0rEHEPzxe_J0ItZjt5-HUhGJTywQN3VB0jotJKi6HKgL6vPoIJWSW5xOxa_d_-O5WhGDyQ7x3uxtNk5cqu-IDgvMYwQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/da696e6ada.mp4?token=YqxX6lSGqg9ZwJSHT6Wpm1ErYruKhrwWc-RDZx8v6TDQ6fK0lVfSu5jr7RpTJx0-BWEMUb0A1r81DOFA1_DoliUPaiknI6Q3N6fYGU7TRUiFLApAzcl9kZfjCuoda_2MafHvMnO45EeYdsLHZBM9pXyo1rBr81ConU1gbr545-LDgtceXeJqVGJWQ4nOCQdjbqRcSDgQ3HQ4obM74mr6icmOmkJWXOxX-AyJHwBcwFY5L3pgp5ImRd11E3C0rEHEPzxe_J0ItZjt5-HUhGJTywQN3VB0jotJKi6HKgL6vPoIJWSW5xOxa_d_-O5WhGDyQ7x3uxtNk5cqu-IDgvMYwQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جی‌دی ونس، معاون رییس‌جمهوری آمریکا، به شبکه خبری فاکس گفت: «بر اساس توافق حاصل‌شده میان واشینگتن و تهران، ایران به طور دائمی از دستیابی به سلاح هسته‌ای منع خواهد شد.»
او افزود: «تنگه هرمز بلافاصله بازگشایی می‌شود و محاصره دریایی آمریکا پایان خواهد یافت.»
به گفته معاون رییس‌جمهوری آمریکا، با اجرای این توافق، زمینه برای سرمایه‌گذاری‌های گسترده در منطقه فراهم خواهد شد.
ونس در عین حال تاکید کرد اجرای این توافق به پایبندی جمهوری اسلامی به تعهداتش بستگی دارد.
@
VahidOOnLine
جی‌دی ونس، معاون رییس‌جمهوری آمریکا، گفت قصد دارد در مراسم رسمی امضای یادداشت تفاهم میان آمریکا و جمهوری اسلامی حضور داشته باشد، اما احتمال دارد دونالد ترامپ نیز شخصا در این مراسم شرکت کند.
ونس در گفت‌وگویی کوتاه با شبکه فاکس نیوز گفت: «فکر می‌کنم هنوز در حال بررسی جزییات و هماهنگی‌ها درباره افرادی هستیم که در مراسم امضا حضور خواهند داشت. من قطعا قصد دارم در آنجا باشم، اما این احتمال وجود دارد که خود رییس‌جمهوری نیز در مراسم حضور پیدا کند.»
سرویس مخفی آمریکا معمولا حضور همزمان رییس‌جمهوری و معاون رییس‌جمهوری را، به‌ویژه در سفرهای خارجی، به دلایل امنیتی و ملاحظات جانشینی توصیه نمی‌کند.
این اظهارات ساعاتی پس از آن مطرح شد که شهباز شریف، نخست‌وزیر پاکستان، از برگزاری مراسم رسمی امضای توافق میان آمریکا و جمهوری اسلامی در روز جمعه در ژنو سوئیس خبر داد.
قرار است دونالد ترامپ پیش از آن برای شرکت در نشست سالانه گروه هفت به فرانسه سفر کند.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 323K · <a href="https://t.me/VahidOnline/76352" target="_blank">📅 01:53 · 25 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>

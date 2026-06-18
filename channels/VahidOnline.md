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
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-28 17:57:40</div>
<hr>

<div class="tg-post" id="msg-76481">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/lJJXCRb7SAV7jLCZ6PYaGOcECXj06AM3kayRp87vs8d6KSTSKvJFEBtgadt4uk7_G_L02YxzAb41LtwmsCOqaB7XWvJ1yFrs6S4beztzRzc95RViE7q-XI2Cz5l9V8X7C3WsBeiru9HGS5lQawkS73xSDXV9NvEDvyv2jQqvVTChfGGQv7Z4jrJPwZWwypFvcnbrOkKuFvPVO2Eh3XDRvffdOtOZfygtY4kabddbF59ydw5JOurf8f6GJap4XUSf-pcmXJ-RbHYhoAQEJUqgiNIE2PVgZGwIrY1NGWxcEdvcBBUur30PZ4-IGdhvF2TZhXS5Zav21265K2Vm25JENQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ایرنا: به پاکستان گفته شده "نیازی به برگزاری نشست حضوری در سوئیس نیست"
ننوشتند کی گفته:
منابع دیپلماتیک پاکستان گفتند که سفر برنامه ریزی شده شهباز شریف نخست وزیر این کشور به سوئیس لغو شده است.
این منابع مدعی شدند که از آنجایی که یادداشت تفاهم اسلام‌آباد از سوی رئیس جمهوری اسلامی ایران و رئیس دولت ایالات متحده به امضا رسیده است، به طرف پاکستانی اعلام شد ‌که اکنون نیازی به برگزاری نشست حضوری در سوئیس نیست.
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 46.4K · <a href="https://t.me/VahidOnline/76481" target="_blank">📅 17:39 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76480">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/u32BKjKf27bwbFSfjFEBR-U0aN0uHW7gozPoqR-n3dn5AdfHj-w2hd8IxCAPubMUBavH7JghLJlPMiMd0Nchu86LZ6GLRpO--HJuFZn5ll8kmRpZomAAqmHrl1pPiqzJadPpeGDoAcgM4pTBaVSecTGcJImNdjS4N5nyb_S9srOK2qs7g51gBiFI58fw7RROOkvdTxKWznsGtlPCOk4Wn_fcRypv7ni7GqiJYezEiD0YXEy477TOIPCQ46NeTjGsAbefyYUojb6sI3TEJoUx1sir7gdnkuUQQRj0cybvmN5aw480OB0fS3VtkBvkyodTCSl80RHQBWe5BdJk-uF5Jg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پست ترامپ ترجمه ماشین:
«نفت در جریان است، ایران هرگز نمی‌تواند سلاح هسته‌ای داشته باشد، جهان امن خواهد بود! بازارهای سهام غرش‌کنان پیش می‌روند، مشاغل در سطح رکورد هستند، و قیمت‌ها در حال کاهش‌اند؛ مقرون‌به‌صرفه شدن! کشور ما مثل هیچ‌وقتِ دیگر قدرتمند، امن و محترم است. «خواهش می‌کنم!» رئیس‌جمهور دی‌جی‌تی»
realDonaldTrump
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 48.6K · <a href="https://t.me/VahidOnline/76480" target="_blank">📅 17:37 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76479">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/K6CtZUKjLtXyMPHI7ixXn4EiP5FiVQ79L1J_ejLJMyQxgnM76-tFuh_nkeMCgIarTH2aPfnk5YaCjW-Q6kDFqWsoHemanGh4Fce8nX5gwQZLRzycTxLis7aPu4lpq-LZ5Bx2Kka4NCYYqgj-kJpMdRrrYJbNAfKfbQBLXUj3UYhIyvA107ZRD6jntwCtdtKdb0NJ6KgC3xX--MBxBbwbMGIxaekzNzjfjEbjcnti5HWliY7LnxLNyVbQ0kJXiT5HgJGbCv7Orkx-auiaEeq_eZ0VaevY8196FaqAm0IuZEaFYywoECG_AttM8YQNJXZ2uX4uxkC8zdoPQhj1TlcvGw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پست چند دقیقه پیش ترامپ: "پاپ لئو از توافق صلح آمریکا و ایران تمجید کرد."
realDonaldTrump
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 123K · <a href="https://t.me/VahidOnline/76479" target="_blank">📅 16:37 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76478">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/bVmnJB5JP1zGHKGGvnhKGhJGjRqIX7Fcw1rfFfvRUURK2S9pHPVplaH3VltJSVjgyTeu49yB_rCxM4mXlfjylPPSdJPFvHxkp1yMBTUj-bVNUzKOeyqggTm4EjiIRf3wOTOsMXI_VbbfbeG_brDymr9ty511k3OZhR_bAqsYEhmrMrriFy80ZsTOAnYk9tAec0ynyQ4586_TDdAWIbohFNaoGOFhlvoLL6zXMOjozEu9FfUDx6VVNR70wcpRmJtAuMg0XkBKQPArXZudrYEW1qLLGo9TC49_c2aGbDVyHlmquCWZQz3COSwk2-wu_siSBrZ5bidy6YObMlFDYDGYWA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پست چند ساعت پیش ترامپ:
این احمق‌ها که فکر می‌کنند من در قبال ایران به اندازه کافی سخت‌گیر نبوده‌ام، در حالی که بازار سهام همین الان به رکوردی تاریخی رسیده و قیمت نفت هم دارد «سقوط» می‌کند، یا حسودند، یا آدم‌های بدی هستند، یا احمق‌اند.
آمریکا را دوباره عظیم کنیم!!!
رئیس‌جمهور دی‌جی‌تی
realDonaldTrump
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 127K · <a href="https://t.me/VahidOnline/76478" target="_blank">📅 16:35 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76477">
<div class="tg-post-header">📌 پیام #96</div>
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
<div class="tg-footer">👁️ 124K · <a href="https://t.me/VahidOnline/76477" target="_blank">📅 16:32 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76476">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ly5U_mxRmWrvCjfPe6tJH7bbxxWgAvHoOSlfj5OUSqjLBj1Hz7By7WjHSxmO-bGZWonHxyaL7ggPIRRek0OA4RKMmD8_2mq4apJALOFEKkpjGuWNvLgnbEoz_lSTMUpPoRd8SQhsyiqFPUiEswvE3A2p-UFRi1s40u6S2u6qbT8IITK8V6JIcO7qlGDy-8FiBX8d2BqivhefCyf78NoeE36WxDtO7d3FPY1Su-fFizmCWZqHe8TMA-73KgsgaK43xjBIwswgQAyOj0WZSvidvtfubiU2G3BBFHSKq-rrU6O8Uu3sUeGMExzDXBmjNHCImz5k_fD6u1aGJ4watlowgw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دادگاه کیفری استان قم، پرستو احمدی، خواننده، و هشت نفر دیگر از دست‌اندرکاران و نوازندگان «کنسرت کاروانسرا» را به‌طور جداگانه به ۷۴ ضربه شلاق تعزیری، دو سال ممنوع‌الخروجی و دو سال ممنوعیت از فعالیت هنری محکوم کرد.
اتهام این هنرمندان در این حکم قضایی جریحه‌دار کردن عفت عمومی از طریق تولید و انتشار محتوای مبتذل و خلاف اخلاق در بستر فضای مجازی» عنوان شده است.
پرستو احمدی ۲۱ آذر سال ۱۴۰۳، به همراه گروهی از نوازندگان مَرد شامل احسان بیرقدار، سهیل فقیه‌نصیری، امین طاهری و امیرعلی پیرنیا، در کانال یوتیوب خود ویدئویی بدون حجاب اجباری، از «کنسرت کاروانسرا» یا «کنسرت فرضی» را منتشر کرد.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 126K · <a href="https://t.me/VahidOnline/76476" target="_blank">📅 16:30 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76475">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Z7yvfqsAaFR586Nwg5kag4hAxw-zoSkMMD3GnieKFp3BuS6MV8OtbvSKLUFhqSDx1gx15BgO0EdltHR2conugbKSRsdWkXLkRM0r0q0EDWy-A0mOne1GEK1J-N5UylqJzFG4weY9XKzlIp6uSTCObbFaRFDAPDYRB-XpXbfe9hIdJSUDRzBor9O-QrVd55TfnPC0BYsjE0DhlXdxb9A5KQlBK8h8abTxpPJKlFvVP8Y9fBpxfUemwoz1c1-UvgvregWub3Cp-ieHMrGPwvc2D4DshMnBcrOdEGo8vjLz8PFpg0aG88VqfjEthAsGO3cRWmFeF-grRXWfU0KJxwBdBA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این توییت ۹ سال پیش ترامپ داره توجه می‌گیره:
ایران به آخر خط رسیده بود و آماده فروپاشی بود، تا این‌که آمریکا از راه رسید  و در قالب «توافق ایران» به آن یک طناب نجات داد: ۱۵۰ میلیارد دلار.
realDonaldTrump
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 357K · <a href="https://t.me/VahidOnline/76475" target="_blank">📅 05:48 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76474">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/JH13bf3XNn73ub8equbj2ooEyEmRsrLBw7FdzJ070IGJCbc2uqQTzge-aIJvOacqgsHA0MlFbcayMJ4g6dQ2ogAGcwPwjPjXp7H38W4WP_2oVnBumUxBhKNOeJ_tn4oT8ttvMhCQY9acRWFJZYFIHNqXnBKaJxTlRrJb3mfv-ra9jNgXRPNv5PObo5baZuEh3ODDqMuYcPz-Th1Dcf2Nh8p9s_TqaC5_m_WSlghzvTd9PxZPjJNi8z9HltbS8l-fWikcvL4MIG1jiwJlSA98Q8GcItRshoPkAJCPhE2IgzZhg1Adg4C7R-kGaIUjrE8Kmp1OT7TEa-jOQcYB0j4DOQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">درستش کردم
MahvashJebeli
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 361K · <a href="https://t.me/VahidOnline/76474" target="_blank">📅 04:35 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76471">
<div class="tg-post-header">📌 پیام #92</div>
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
<div class="tg-footer">👁️ 364K · <a href="https://t.me/VahidOnline/76471" target="_blank">📅 03:50 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76470">
<div class="tg-post-header">📌 پیام #91</div>
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
<div class="tg-footer">👁️ 354K · <a href="https://t.me/VahidOnline/76470" target="_blank">📅 03:25 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76459">
<div class="tg-post-header">📌 پیام #90</div>
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
<div class="tg-footer">👁️ 377K · <a href="https://t.me/VahidOnline/76459" target="_blank">📅 00:52 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76458">
<div class="tg-post-header">📌 پیام #89</div>
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
<div class="tg-footer">👁️ 390K · <a href="https://t.me/VahidOnline/76458" target="_blank">📅 22:53 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76456">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/m41zDE-9CfWXx_zTCJvkSA2DzT-eBj5ubHeSSXS0ZB0h16EU4hMcrcbvypSbvEvKB8qvuIZcsrtjqy0wOcn1Sebz-UBkUYN2ID-fW2jSY7vgBPVt0ANNfEXxLdc6Sh8fgyqDX8OEcYDXBwg8ixnG9fLZvaeDe2FtQAZDJ99nRFZeJri4JsmNwDosbx3vpF5qPTyzgz7VIqDauSqk5y2n7yEoqVy40L-Jg2hNMUTDOzonzQEQw5eGoTDzs6G-7gPtwPCPTWTOdUEH9dx6373iMHRCTeIazAZVJw8jZraz4rKH7oM5bfseYjS983Ai82N70Rz2lHcrAcSASRmFEFVCMg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سخنگوی وزارت خارجه جمهوری اسلامی روز چهارشنبه از احتمال امضای توافق پایان جنگ توسط روسای جمهوری ایران و آمریکا خبر داد و گفت این مسئله «در حالی بررسی است».
به گزارش رسانه‌های نزدیک به حکومت ایران، اسماعیل بقائی درباره احتمال امضای یادداشت تفاهم از سوی مسعود پزشکیان و دونالد ترامپ اعلام کرد: «این ایده مطرح است و همچنان در حال بررسی است.»
پیش از این طرف‌های ایرانی و آمریکایی خبر داده بودند جی‌دی ونس، معاون رئیس‌جمهور آمریکا، و محمدباقر قالیباف، رئیس مجلس شورای اسلامی، در سوئیس این تفاهم‌نامه را امضا خواهند کرد.
دولت سوئیس تأیید کرد مراسم امضای این تفاهم در اقامتگاه کوهستانی بورگن‌اشتوک برگزار خواهد شد.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 372K · <a href="https://t.me/VahidOnline/76456" target="_blank">📅 21:28 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76455">
<div class="tg-post-header">📌 پیام #87</div>
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
<div class="tg-footer">👁️ 342K · <a href="https://t.me/VahidOnline/76455" target="_blank">📅 19:39 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76454">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/U4qr1TB_eZ3XVabcm-00QywaYCDvZZU_xzxMt9qMWKKC6kAM7EqSW0QKrc0JIvgMWc14pfotDkESHsCwDDYTT5P2yOpq0cFypAOF2nKNDuVB63NJWXewShrQgJNH9kLQQD40kbcTfikSp1cE8OXaG9Y9_K0zB-1lppa6y1OxHsJcuYzuJ_-bTSYyBuJ-05mIhHSJ3j8pmg0_EAyZbKDT1pkop75R_zrUJtcOXqh4C2NEdnX_vFco_Dw72jzVxOwJd2hGdIVIfZ_6qAx5WIbjzqZsIduzhSIjcCWvcCdwpwJFhUEZiE9FkI7cKi15WM76Auqyy-7F1GRcRm3OovE9bg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شورای هماهنگی بانک‌ها، روز چهارشنبه ۲۷خرداد ۱۴۰۵، اذعان کرد بخشی از خدمات چهار بانک ملی، تجارت، صادرات و توسعه صادرات پس از گذشت چهار روز همچنان با محدودیت روبه‌رو است.
این شورا پیشتر در ۲۳ خرداد از وقوع یک «حمله سایبری محدود» به این چهار بانک خبر داده و اعلام کرده بود که این حمله موجب اختلال در ارائه برخی خدمات بانکی شده است.
رسانه ایران آی‌تی گزارش داده است که بر اثر این اختلال چند روزه، میلیون‌ها کاربر همچنان به حساب‌های خود دسترسی ندارند. این رسانه با انتقاد از وضعیت پیش آمده نوشت بسیاری از فعالان بازار از انجام معاملات مهم در بورس، طلا و سایر دارایی‌ها بازمانده‌اند.
شبکه بانکی ایران در سال‌های اخیر بارها هدف حملات سایبری قرار گرفته و در مواردی نیز اطلاعات مشتریان برخی بانک‌ها در فضای مجازی منتشر یا خرید و فروش شده است.
با وجود این، شورای هماهنگی بانک‌ها تاکید کرده است که سپرده‌ها، تراکنش‌ها و اطلاعات مالی مشتریان این چهار بانک در «امنیت کامل» قرار دارد.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 278K · <a href="https://t.me/VahidOnline/76454" target="_blank">📅 19:17 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76453">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/eIQ-7DF2bDE6Tk2gRkl-r3zKqMzo2cQt4gyCFw1okrzuTwZzG-GrUVOpBEAz4t13cCzicYvTpUnIATGWxu7HmVIWOVj1zt7Zf9w0BJ21Nho9SjqKtMfGvRxp8s3iffuy7ck19ke42duH8UPsy47ktL9K9nVL-mKaCKUnrGJahGA4VtDZkYaVEPKKDtd9OtP-qLbeF26FvrAWYgLBTL3P0PtHrICaHdSR_5yApDDMJm2I8CD66W4akAPzHX2KkR_KpGwLAauhP0-Up-C2h91q3gE9UI29ZiB1dUrjMGdYZZTbOvzWVq9Hp1c47r-GMjBgt4EeyAbGpEpqSzU2gcBpNg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 261K · <a href="https://t.me/VahidOnline/76453" target="_blank">📅 19:09 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76452">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/cc6738c570.mp4?token=qiuoS_aXJn4evdJ64PhQITyW3gn8fAbUw5mS2MZWP5LKR0lcjFkN-cCYciAr1mnqKU2ywL0QVEab8zLzqDLuLqrqE263x4j9N23tCSBpz6Li_vR1p4ynFVtRh5JayUjTAZp1gMgT7TFnFSWInvT6hYuQiQRuUxT-Fq1TnNnEt-fCipX3wecYityqJ2ug7-vyKV1z152tMQDLg1knI1mN8VU6XWt8wjp11T450CltY1bmu_J-U599FE_U_lSo1_Z99bibYPRUYH_Dpc-2-eJ8hsuq_vjI398gxHCRdaHTGoKO8q5_3AdT1-c5jxS_72EbDBvG3SLOzswfDo6IFeYzXA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/cc6738c570.mp4?token=qiuoS_aXJn4evdJ64PhQITyW3gn8fAbUw5mS2MZWP5LKR0lcjFkN-cCYciAr1mnqKU2ywL0QVEab8zLzqDLuLqrqE263x4j9N23tCSBpz6Li_vR1p4ynFVtRh5JayUjTAZp1gMgT7TFnFSWInvT6hYuQiQRuUxT-Fq1TnNnEt-fCipX3wecYityqJ2ug7-vyKV1z152tMQDLg1knI1mN8VU6XWt8wjp11T450CltY1bmu_J-U599FE_U_lSo1_Z99bibYPRUYH_Dpc-2-eJ8hsuq_vjI398gxHCRdaHTGoKO8q5_3AdT1-c5jxS_72EbDBvG3SLOzswfDo6IFeYzXA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 252K · <a href="https://t.me/VahidOnline/76452" target="_blank">📅 18:57 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76451">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/tdnLnKmBJ_iL-6dR1O5RqJaki7be3w4RaGbF4LpxZqMskToNFtqttNn3RIxD7c1ZtGNF0DqpTXgY-gvtIHvqodHIrXjEPmdF5dX_2_xsF6h5gTi0jH-zU1J7s3-awfxpPkXDBKmNhIuv03J3DdSBLuB_KevW6TxX6cOV_xxbTyuwh--nKwTZqnGWhpDceEN957F4-xOaHZZL90UrI3WTfVN6EzgvgMPPVsB4kmHLO1yGYJcbNglJDIich_9VA5lOXAU4jw03vtqgYAG_TsUq2pOgJFKc6drU_gi4LSxC0o-yORoCeLa9yO-RcBzoaRr0UVfCvTY9R6MGMrJgAdOm7w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پست ترامپ، ترجمه ماشین:
من ۴۵ دقیقه دیگر از فرانسه یک کنفرانس خبری برگزار خواهم کرد. سپس برای شام با رهبران فرانسه و دیگر رهبران اروپایی به ورسای می‌روم و امشب به خانه بازمی‌گردم!
این سفر موفقیتی بزرگ بود، اما چیزی که بیشتر از همه می‌خواستند درباره‌اش حرف بزنند، این واقعیت بود که ایران سلاح هسته‌ای نخواهد داشت و تنگه هرمز فوراً باز خواهد شد.
در همه شاخص‌ها، ارقام مربوط به اقتصاد ایالات متحده عالی است؛ امروز شمار افرادی که مشغول به کار هستند از هر زمان دیگری بیشتر است. بیش از ۱۹.۱ تریلیون دلار در آمریکا سرمایه‌گذاری می‌شود، کارخانه‌ها و همه چیزهای دیگر در حال شکل‌گیری است؛ اما نکته مهم این است که ارقام اخیر بازار سهام به خاطر این توافق سر به فلک کشیده و به همین ترتیب، قیمت نفت هم به‌شدت در حال سقوط است!
رئیس‌جمهور دونالد جی. ترامپ
realDonaldTrump
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 257K · <a href="https://t.me/VahidOnline/76451" target="_blank">📅 17:49 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76450">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LjDtZAY2RBPf0cCjhvJ0CabE8ldMs4an1msdCyaxCo1yb07zM0vdrlGQ0lTVXlpwTiD3uNrsUyFYW3CkSNhpGjT8_pozunv6-wg8izC9ize3_P_3PceW56DVw11dSRjbSeSOI8pGUb_y1GO728EZycgqaGaFBtKcU2PARAnWW9fqE7Gm4_kFl3YYVjA3hskS0R4jZYHRV7uQ4JgbPyGM5uhuAj8po_X3t_VN4LDn4byA_CAYT4H4pat3tWSD1zt6LZDZImEdK11NzWz_hSSWRq27W8d5Sj59J4Qw-sqnMLqR-6l3TEdGGowvOypu7Tn7qX9PkEykdqv_RJpg6EcNmw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جی‌دی ونس، معاون رئیس‌جمهوری آمریکا، در گفتگو با برنامه صبحگاهی شبکه سی‌بی‌اس (CBS)، از سیاست‌های دولت دونالد ترامپ در قبال جمهوری اسلامی ایران دفاع کرد و به انتقاد از کسانی پرداخت که به گفته او، صرفا به دنبال تداوم درگیری نظامی هستند.
ونس با تفکیک میان «ابزار» و «هدف» در سیاست خارجی واشنگتن گفت: «رئیس‌جمهوری از دیپلماسی، اهرم‌های اقتصادی و فشار نظامی استفاده کرد تا مطمئن شود ایران به سلاح هسته‌ای دست پیدا نمی‌کند؛ هدف اصلی همواره همین بوده است». او با انتقاد از تندروها افزود: «بعضی‌ها فقط می‌خواهند بمباران‌ها ادامه داشته باشد، بدون اینکه توجه کنند آیا این کار اصلا دستاوردی برای مردم آمریکا دارد یا خیر».
معاون رئیس‌جمهوری آمریکا در پایان تاکید کرد که هدف ترامپ ایجاد بدبختی و رنج برای مردم ایران نیست، بلکه تمرکز اصلی دولت او، مهار برنامه‌های تسلیحاتی و جلوگیری از دستیابی تهران به سلاح هسته‌ای است.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 249K · <a href="https://t.me/VahidOnline/76450" target="_blank">📅 17:42 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76449">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/WagzUcbYigO7WVjtr04zD6K68iOB_0mHIrz23NNLWAtCfxiorQ7X_yvYmbsV9qxESKVxMZyyPsvdav9I0bQR9fj-fGaiUK6fr36ZpqH7Xv-YE1UuZWKt0QKlG21u8p8mrdiPoRlJf3jRYVMgVr8dZpxvHl0Jqqi6tNz0I0OD1mHMtsMLdfOHII5wRTxMGnD77t5EIyEooqpqwDJVR1zHIyKaz6pKEnZXucMs2raa8pv2IA2v-m8bvVzvjy5bkV3MT4JOuTwe393fQDjQNi_5dVch7c27gEux2OrHRQpNv5ImJd8AewGn8mdObImYrTo_MGh5n_IXxJe_ENXeWDwgEw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">.</div>
<div class="tg-footer">👁️ 257K · <a href="https://t.me/VahidOnline/76449" target="_blank">📅 17:32 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76448">
<div class="tg-post-header">📌 پیام #80</div>
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
<div class="tg-footer">👁️ 268K · <a href="https://t.me/VahidOnline/76448" target="_blank">📅 16:30 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76447">
<div class="tg-post-header">📌 پیام #79</div>
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
<div class="tg-footer">👁️ 265K · <a href="https://t.me/VahidOnline/76447" target="_blank">📅 16:11 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76445">
<div class="tg-post-header">📌 پیام #78</div>
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
<div class="tg-footer">👁️ 252K · <a href="https://t.me/VahidOnline/76445" target="_blank">📅 16:02 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76444">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/XbAv1y8bN8CKut1Cw_wNrrpFN64oHK23oUS8DW7rPPO2-uEjJ6vc8tSSFh9I7_PF-K7rsmwdoYhYjbrKUV_EQkO5nx8vQmqcFUvlwDtIiwAGqZTBd894_9JUwL4EFvc25YlE8_IfrsgDm8D_N4rhmklm3nqBClw6uBsrnDKoSnR2c0LLRF1IPcGQBIBmakVmFyfJGy4mLJ_MHiNKbkC5dwJuS9W8b_mMSzNScgSOQQ5X0uMigmEvWECVKFkjSG2r1rn_v1Tbe8_a36QFyrovWxpdS3isBew1NH-PERvJwYI3ccUC0p_LJkUqJS3t3mB10BBiVF56bpUHr0dM3XhPSQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ابراهیم رضایی، سخنگوی کمیسیون امنیت ملی و سیاست خارجی مجلس جمهوری اسلامی، با انتقاد از یادداشت تفاهم میان جمهوری اسلامی و آمریکا، این توافق را «نامتوازن» توصیف کرد و گفت همه خطوط قرمز جمهوری اسلامی در آن رعایت نشد.
رضایی در یک گفت‌وگوی تلویزیونی افزود جنگ پایان نیافته و نباید تصور کرد شرایط از وضعیت تقابل خارج شده است. او گفت: «ما در یک جنگ ترکیبی تمام‌عیار هستیم و باید از فرصت ایجادشده برای قوی‌تر شدن استفاده کنیم.»
سخنگوی کمیسیون امنیت ملی مجلس جمهوری اسلامی همچنین از منتقدان یادداشت تفاهم دفاع کرد و گفت نباید مخالفان تفاهم را «تندرو» خواند. او افزود: «اگر این افراد نبودند، الان سربازان آمریکایی بالای سر ما بودند.»
رضایی پیش‌تر نیز در شبکه اجتماعی ایکس نسبت به نحوه دفاع حامیان توافق از این تفاهم‌نامه انتقاد کرد. او از مقام‌های جمهوری اسلامی خواست از منابع عمومی برای تبلیغ «توافق» استفاده نکنند، منتقدان را تحمل کنند و برای توجیه تصمیم‌گیری‌ها از رهبر جمهوری اسلامی هزینه نکنند.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 230K · <a href="https://t.me/VahidOnline/76444" target="_blank">📅 16:02 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76443">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JPdI7zwlo6a94Arrsih2RfSp8rl3H_65YJZh9s2mRxyMKT8P21TRkCh6VpXjn9Fs9d5nvI0zRMLI1qDAjy4J7PGflfCf2f-9R1qrvE0DhUJn2MhRK2VN3UpD4yilAeGPpHfFXNDOPZZxqCmSDEF3epxLLsiZgYTB1mWPd3sCQAV8NzBXrox5LZHTcFGV_9P-dva4IeC7UTzM67VbUWJ6xxth1k6iECZubyaHKjecLUVxflCZ6RpJBZtNc_uEbr-NH-y87DsCOUbmK3wf0xWG1GSXlTIsnBYgbUynzGxSVxdgmflWhRFDSreOq_KXGtYKY9Ms5VsPjMZAKWxFdW7-6g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در ادامهٔ روند کاهشی قیمت ارزهای خارجی در بازار آزاد ایران، روز چهارشنبه ۲۷ خرداد قیمت هر دلار آمریکا به حدود ۱۵۳ هزار تومان رسید و قیمت سکه طلا هم در محدوده ۱۶۰ میلیون تومان اعلام شد.
قیمت دلار آمریکا که در مقطعی تا ۱۹۰ هزار تومان بالا رفته بود، تا کنون حدود ۲۰ درصد کاهش پیدا کرده است.
قیمت هر گرم طلای ۱۸ عیار نیز روز چهارشنبه به ۱۵ میلیون و ۷۶۷ هزار تومان و «سکه امامی» نیز به ۱۵۹ میلیون و ۵۰۰ هزار تومان کاهش یافت.
در مقابل، شاخص بازار سهام بورس تهران از زمان اعلام توافق رشد چشمگیری داشته و روز چهارشنبه با ثبت رکوردی تازه به بیش از ۵ میلیون و ۱۰۰ هزار واحد رسید.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 215K · <a href="https://t.me/VahidOnline/76443" target="_blank">📅 15:57 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76442">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bWoQQh8YL8udXclQzF58U_JqGFQ7VJ5VK4sE-WsgQblKqx3BTDoLEWD3-DV3REnuwktqs4QFOTbK_u0LJJGFzXckECmeZNTfinXefRW2xzokTsz6rR6_HFc3VjxSa0CIkQCzMJtLXYrDOEZPFa8rHxNBeDY9EugBes8RPpaZdjbexbq7DD2URqRyKD7sWCEVSu7SlG7af9ed6wbkdaV4njdPisOxKq-u7xVouTFPmPtYdn62699qOSKfEKkibDz2Tfk3kz8fZfl105qqZBorvYyyYoFv2NRGT6s8TRSF2VywfhofO7QSc94F7a3ApJu6do9eHeX05RfOWlcRYkRX8w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سران هفت کشور صنعتی جهان (G7) در بیانیه پایانی نشست خود از توافق میان ایالات متحده و جمهوری اسلامی حمایت کردند و آن را فرصتی مهم برای جلوگیری از دستیابی حکومت ایران به سلاح هسته‌ای و محدود کردن فعالیت‌های موشکی و منطقه‌ای تهران دانستند.
رهبران آمریکا، کانادا، فرانسه، آلمان، ایتالیا، ژاپن و بریتانیا همچنین اعلام کردند آماده‌اند در روند اجرای این توافق مشارکت داشته باشند.
در بخش دیگری از این بیانیه، بر ضرورت حفظ آزادی کشتیرانی و عبور بدون مانع کشتی‌ها در آبراه‌های بین‌المللی تاکید شده و این موضوع یکی از ارکان اصلی تجارت جهانی توصیف شده است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 202K · <a href="https://t.me/VahidOnline/76442" target="_blank">📅 15:57 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76441">
<div class="tg-post-header">📌 پیام #74</div>
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
<div class="tg-footer">👁️ 206K · <a href="https://t.me/VahidOnline/76441" target="_blank">📅 15:56 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76440">
<div class="tg-post-header">📌 پیام #73</div>
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
<div class="tg-footer">👁️ 273K · <a href="https://t.me/VahidOnline/76440" target="_blank">📅 15:55 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76439">
<div class="tg-post-header">📌 پیام #72</div>
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
<div class="tg-footer">👁️ 329K · <a href="https://t.me/VahidOnline/76439" target="_blank">📅 09:23 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76438">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kPNAvhmB2x4A8-fmVp99yv3P4pdwPhcHHL8CCYwC19nQJf5nSXwbrCVqL6rncPPra-e9RSDW98Fg7pwyEpVdu8j6Wu10u_dNvMAQjGMpGXBFmm2BnZRHed6Xmaz5xzB6sCbBZnNcQdmbt9tYsIvvPHg1mhmN3oihAAUoIeN2MSfS8bis2okxXaL0QKDPLoZGSb3-lQa2UYLb1NOwraB4ZA9cAK_ut2aJYhoCIGRMTxgs_6T2bUQr5WnY6D_R-abwmbPZPzSM_-Wa7weUyNEWL4Z8cvGOGflx7MrhmPYTHHgbgOcymCltfoMrOgpafnY0gSMhjXX7IheEkJkbYdNjSA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نخستین نفتکش‌های حامل نفت خام ایران از زمان آغاز محاصرۀ دریایی آمریکا، از تنگۀ هرمز خارج شدند. این موضوع را صبح چهارشنبه یکی از وب‌سایت‌های ردیابی کشتی‌ها اعلام کرد.
وبسایت «تنکر ترکِرز» (Tanker Trackers) که ذخیره و حمل‌ونقل محموله‌های نفتی را دنبال می‌کند، بر اساس داده‌های دیجیتال منطبق با تصاویر ماهواره‌ای، «اولین صادرات نفت خام ایران در دو ماه اخیر» را تأیید کرده است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 339K · <a href="https://t.me/VahidOnline/76438" target="_blank">📅 08:48 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76437">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tvIOuu6ibgLINe0RTdPZzF_kvv2ETOAvHqdwzdEHaKfSkDLTKLXT8DCQsIDrTwvNRYPlHh4Zp_tFjXn8ye5fLUEfnj3eIZP4eyJqmaRYaiQKWdElEQHkMDaTmYjFdKY32Xj5LkBemhVBT4lbx-Q7_H2Y3-FTF590Uf1V6v9WUr1_hzXqTtZePibPONLzwT5CVCwv78JQTQ0F6-Yz33vvFfoHXNLqo-f0hZxIOfmPZGHqej-8nHdx4GPvJ5W7hwcbb7lEl31Ivc5VCGTgLoOp00W39LBYl-JzyzD9RqmMIMDj5b_bzOS_PPirtKGR2aZVQGi_XKnVASMRc97DpqNlDw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">به گزارش ان‌بی‌سی، حکومت ایران پس از اعلام یادداشت تفاهم با آمریکا، همچنان تعداد «زیادی» پهپاد به سمت شناورهای تجاری در تنگه هرمز پرتاب کرده است.
شبکه ان‌بی‌سی به نقل از یک مقام آمریکایی گزارش داده که سپاه پاسداران پهپادهایی پرتاب کرده که آمریکا توانسته آنها را پیش از آنکه تهدیدی برای شناورهای تجاری، کشتی‌های نظامی و خدمه حاضر در منطقه ایجاد کنند، رهگیری کند.
بر اساس این گزارش، سپاه پاسداران از زمان امضای «الکترونیکی» یادداشت تفاهم در روز یکشنبه، هر شب اقدام به پرتاب پهپاد کرده است.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 346K · <a href="https://t.me/VahidOnline/76437" target="_blank">📅 05:11 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76436">
<div class="tg-post-header">📌 پیام #69</div>
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
<div class="tg-footer">👁️ 358K · <a href="https://t.me/VahidOnline/76436" target="_blank">📅 03:05 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76435">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/D7nfsqRoiSxZE8WgyEK4EGTE05ztnquSfjsYW9j3WcO0y9kD1ZXromD9MxpIKYIcSLT07FK9HdrZ5TbvLAu1_eEoNZlflQbNrGcgtwI3RnKR1k54v6mcXiw-87ck-YV4yfMPNMtp1oo1cOsQGlxb7yAxTSTyWBEp93I9QH55GhQjUhKfG8BMWxLcYJY5EGqj5Y-isjpi2GMUWzvWwxe8ZhMz2R-vUk3chh21gZ0sOlMlhDCV0YFoIyZD7wOi2B59-zCGm31rjqwUBO5tmYH8CoZPD7ijHw_FigqwH58OdHC6TdIaZIlFWR2cXdLcawDNl602InR4Wmdv7CYWPDvwsA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تصویری که در شبکه‌های اجتماعی
منتشر
شد، دارا خسروشاهی، مدیرعامل ایرانی‌-آمریکایی شرکت اوبر، را در استادیوم سوفای لس‌آنجلس و در جریان دیدار تیم‌های ایران و نیوزیلند در جام جهانی ۲۰۲۶ نشان می‌دهد.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 367K · <a href="https://t.me/VahidOnline/76435" target="_blank">📅 23:24 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76431">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/aEx9eRNQhjb0SbTvIsZnV6Yx4TcwmILst3c030_4JAOIlTI19jQTiSpSQKK0VprfoyCkOrU3iczubgW0E28CuCJaZ15Kpcuy_f1mZvafEjsKjWTarrnh-wosXMdUlf5DDjnG_E8y5sTSsZDOX_m0cl1Q_JRmobCLzhX9UPdHVuY4kw07BiOv88NWSHNXIASx-rywbaLN1XaXanXfKt9T_LU6_KPRzfOSkItm3XOJrQpl4MbhxjX0UX0rpzMhmeBNMfmScX9932GD3F3fPwqB2e4ditB3f8M15s5VL8EnS4mFczWeITbzSNK4Ewu0MSgI7zT5Yyerf3_Hb9SJGCfrXA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/XQ4EX1vNVUBAhTXUuWJCK0rzNdVM92Tvg_7PwK91P_F8bxLaIK43DqaHaluA0mtBFkRyVoMpjjoBDaBUkT_KjZmP2A0EFq5VnY4GgLLMgiLua2tjGt98gZe_yY7VFcO6CTPB_3TiIsDKO4djBuwdH0CP33WBCEfDGAGbICOzgSEEgNKIfxQoI99BH3tiXSmXfgQknqswV6TPcGyQkFoQ1UwXGoHperT22CdP13h6uHw1QionvkFc2LSujGPQgYwdjrvvFuQ4o7cXXN2PKIBMKVet1bklQdWj7f7aDWdA4xD5kYoue7ksyo4Btnhei-tY7Xn4GhYtUH3_toU_s-ADuQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/JcnUXxO-ttZrABSTdFEJP4ojAiAON-4mKN6YvK2dAJVRg1tlDcRSZFOZZI_f0lxYF_N0ziEvWAhynFZlWQfvr9t3JTub-gNvrYlxLGrzgW6TdhwaQJ4dLz0K1Xy9szMq6K8zsD7YAhDMX9fqWykYXz7RCwbI-VUtGKOuBQUrhlDNGndLvTr5jR6XhaGEptxSp7uEUbgbYN7IM5HSsdAoEt2ABQQToIkHtVYww4y2uJxhsNGXZ6MGEY9j6hULQI89Nr227E1xj-YP7Lw2zB6IjwVGy2ooBTfNYmh3GZIpEaKCXtkubfyI1oXHRycsUjeK1cyJZulfArGj0q8mxBqHZw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/57a8c06d44.mp4?token=GW1jYfN9js2MDUhort_8rZ71A942Wj7Lqc9yKS_X5LkFejB5sbDVrhK-yIsDqoWGq2WQ2gzyVHSoEkC-7zLWoh2T_tybSvmYiaJXz9VeJF6vFfUHs2pedimRieIiIqY1QUrM-C5lo61eZa8L-IgH6kpy2raell1NomvYGgU3qHn-Su8wwjPLTgooikdthlpBvtODKJT3Lt9Ckt2jtRFlAHfLZISJ7UNjUS0K2fu7MDepAiY4zabfFyB7oLgUobt8kBVwFJic2etFgbgnd3eNDdE0M5SKUEOM510rdW6ygt-ukXDprEMIgB_i94LNhbwZSjQLvRALaqLwqtjU0skEJA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/57a8c06d44.mp4?token=GW1jYfN9js2MDUhort_8rZ71A942Wj7Lqc9yKS_X5LkFejB5sbDVrhK-yIsDqoWGq2WQ2gzyVHSoEkC-7zLWoh2T_tybSvmYiaJXz9VeJF6vFfUHs2pedimRieIiIqY1QUrM-C5lo61eZa8L-IgH6kpy2raell1NomvYGgU3qHn-Su8wwjPLTgooikdthlpBvtODKJT3Lt9Ckt2jtRFlAHfLZISJ7UNjUS0K2fu7MDepAiY4zabfFyB7oLgUobt8kBVwFJic2etFgbgnd3eNDdE0M5SKUEOM510rdW6ygt-ukXDprEMIgB_i94LNhbwZSjQLvRALaqLwqtjU0skEJA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 379K · <a href="https://t.me/VahidOnline/76431" target="_blank">📅 22:40 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76430">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/JsDZO6RaL6vNABDd9m6pv5gGeA6QfcKcgYwkQSrqVPXVS3Ag8tAxwZ0kCAsq5mpulzyePi1kIe5W2MypMhWmpySHrw3ez5bumIHhL6arJkJodPHS3LBtJiyJl7OrONFVrJcXbc7RmqK5MgJ0UyCR9BuDCAyE53SLaPFXQLC3SmYYA4ELy2-ciRppcywBtGiNS_aMgHv80uqiN6xONLxAsyutPZB4gIMMo2mLc5RsnQkd9VHj55BLyr0W5dnoZCUciC55kns8sfXJ78QFva7hLOUnehED9KdsQjwzL0zngTz5C84jlhwye0gNS9z8kRn1qFA6baPI_rLNRfYW77jG2g.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 328K · <a href="https://t.me/VahidOnline/76430" target="_blank">📅 22:23 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76429">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/MfAlYLGV6pACicaNBckOf_QGYaEznL1cJaxMCHQkHvdvmKRV5BP_PaaGOhxjpxxCFeBp1CqH-2XLInqp8pQE8wrUIIyZSVjn_AneDD_e3Dxkj46chhBD6aTtK14hT8JVfLKo9WEu5jvjseAnW_CmjmCJwMMs-XBIYnoh52f4PUWPbr914i-9y96SnzBQJs27FoUcZ0QovkrFGM1bzdxFhBe-H5sHGqRdjD64zaqeKaVqZaqz385wwnETR-Ym3tjH02dNAd2PNhz1bbUGr3HuD-rfIYUFkmTmucG-FJiMkgm8qo-6IR1THqDpe_JL7M4MxqgDTa4E2VyDKEgBjr1AbQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 303K · <a href="https://t.me/VahidOnline/76429" target="_blank">📅 22:16 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76428">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/X9yw6FLVuNWtNdigYASO_cW3lZBbxTmQPePpURq7NXnINewOtWj55d7Dj_YE7i7ylJf0w0rNdM9swYsjaze9PWI1nRmEQimabW7PdLt33Pt6YGj7aH_CmyQ7xABzt71diSGOtQZSV_uBx0dYU0opCuggpBCpWYolgrBzS5nLOqLepaKtshzFObu9-FvMHCvisPdv6rME_zoDCVAZ_tphVfDP1b9KRa3k5tsUq05Gerfd6g_VgqILNk59Eaj_XC2mf9UzZoJUsVkeN7KWmnLwKTl04CPlmmqf_nkrrZf66lHiieqrHg91lwsxni4nNwPZi8HwoJQSegzYO6H2ZDX4Ew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">طیبه نظری مکی آبادی، مادر دادخواه مریم آروین و از بازداشت‌شدگان مراسم هفتم خسرو علیکردی در مشهد، از سوی دادگاه انقلاب این شهر به پنج سال زندان محکوم شد.
بر اساس حکمی که در تاریخ ۲۳ خرداد از سوی شعبه اول دادگاه انقلاب مشهد به ریاست قاضی غلامرضا اکبری مقدم صادر و به این شهروند ابلاغ شده، او بابت اتهام «اجتماع و تبانی علیه امنیت کشور» به چهار سال حبس و به اتهام «تبلیغ علیه نظام» به یک سال حبس محکوم شده است.
طیبه نظری، مادر وکیل جوان، مریم آروین است که در جریان اعتراضات «زن، زندگی، آزادی» در سال ۱۴۰۱ در سیرجان به دلیل دفاع حقوقی از بازداشت‌شدگان دستگیر و مدتی پس از آزادی موقت، به طرز مشکوکی جان باخت.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 321K · <a href="https://t.me/VahidOnline/76428" target="_blank">📅 20:49 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76427">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cWsaU7remxMo0hZw50x-NWGKF3aaYYQvEtJjSCXuy0J0MEhd-5BC_9by9SSv0vHzL7lG6YzFGCEexCyE57bxf_mpD-90HGtY2ANxlUKEF-6E_M6m4XBqn3u-IfjOe_QDP7ZtILfrba_Usau3fcgbVWRm_c67lDPXfZNTwEQ13FAzZN7VzGuBg5KSkGjJVkl380NPIoBZMUx1jLaoNzen8qL-Roajas7_WUXBFvggzaxc7b4oD91eKdnpntjA84XpKmrYyFUH2WWBIYfYPut1sYXrTNrgMt9SbcdtDzWpi7N1oI5j2FBlYXLReFt5ytNlZjcT6-Gljmmzp2YsX3ZleA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 320K · <a href="https://t.me/VahidOnline/76427" target="_blank">📅 20:48 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76426">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fKDXDARID4XyYiYayN_c6xLGrrFpa_9yfxfLPAeUq1x2e3SumLNHQfXjbU0LFK4TlLFf7Mye7iMtXkx7vfq7uspycUi6YSmBK0PXR453qwNItObH7S6KDxReJkgYIXwP7AuJAZLTqUZV5wrAeyK_H2UqvJCW8p62x3W8vkxNJW6d_3oKHn8jhsY8yt5EnTtdVsBOHGlCHGj2JuTXxs8fLZqdajrLRCrZ7Ub2ByMS48Pp-Dhn5PNillvbuL9w5MNN5qCW-upsJRs5tAW6vXJdc2VSliN7f6tm_lvlK8dum7wTpK9byQ5z_M6Nk4AX9sKUXL0Y0GNnVnECd1y46IQ00A.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 322K · <a href="https://t.me/VahidOnline/76426" target="_blank">📅 18:52 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76424">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromﻣﺎﻧﺎ ﻧﻴﺴﺘﺎﻧﻲ Mana Neyestani</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/lNweZSksB8hdjw2akuULntol7J3yX5sV_td_ixP-wsRoqjDXKKNbTol8sMgINFnDae0LhW_7IQzUljMV39xqxzk94Z4q-KBf1Cvs-SL0paJeMYGsyNB3hnws9kafDNKLIRaN4_il7z2VA_bGon8dQQTxZjiolF33RuepSfcp-GFqTG1_7i1Tw-PwLp8eRxQaJ0zr80z4dgHRgsu1rDdxMyY5SEcyM0KbC97LZYsZuKz1VaB94qg4MZW1DxfkKxNKbjmrc5X2uY6FMtG52GH4RbSTnngDi400KCgchObcDxh8ZmSeQonmHEixBvidkEvWSSCErDApKZhMaLwp_oeKmw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/NHCIJ9kkPIK9-dZ63m9gD2axTkv8EievOXZ7zSTo9CoKyZsNKiR3IOAFqnc5kHsdyKjWyWh0jyZdyjQT2jdveEBd45xcq-b0O9Kzqkk-y2H6Hln8ka-6QOoAx3zVpIh6ZgfFtdaLnrdf5fFYa_a_XLMLdoT83g-0XHSrR2Qr8JJqPKkVC6Rir0WvXWc-4sCG8vDbhaiRbbza8pPwx-6qN1UEE3ZMUWYbhQsvAFkhqoL14V_38RJNWxZ8ngJhqdITT56tSlxWBeePKUaSMuWxT4c8atldjxnwxegymV_EhLcdhEwwoH6jb6ElEiHoXUJgN0_2-4EuZRUiNfPbWr4Q7A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">پهلوان سازش ناپذیر
@mananey
مانا نیستانی</div>
<div class="tg-footer">👁️ 311K · <a href="https://t.me/VahidOnline/76424" target="_blank">📅 17:16 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76416">
<div class="tg-post-header">📌 پیام #60</div>
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
<div class="tg-footer">👁️ 329K · <a href="https://t.me/VahidOnline/76416" target="_blank">📅 17:07 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76415">
<div class="tg-post-header">📌 پیام #59</div>
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
<div class="tg-footer">👁️ 283K · <a href="https://t.me/VahidOnline/76415" target="_blank">📅 16:54 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76414">
<div class="tg-post-header">📌 پیام #58</div>
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
<div class="tg-footer">👁️ 265K · <a href="https://t.me/VahidOnline/76414" target="_blank">📅 16:53 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76412">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/AxXq5n_JQ0OsnNaOBDIK4aAUDCQ3M-724vHcLONMfp-0hCDdmFEB0k0OK_Bw4hCuzNXuNJYYvzVYii0zgCwJTXuv7bIntZbtXkKW2DqysaGZ8f2RPFY46l5jR4CiJLof25nOjZq5BBXLsMBtwcqrEAvEKZhDP7m10wC69GhqJoQ8OBQAXix3Iu7x9s2txS6HMHFauuI5e8jZGijddR5zXg5EL1OlbJBKT1r-ZDtdyqstmtCzytAmZD4XujIdAgk4xLiV85Y2piQoLKVhUtX9Gr-kPHPj6wI50TA_XP-fLSR4VSnyKke4qOn_x6qP6Dig3YDziqrYXify1WFN-wXZlA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/Mzg_WvDTEqeUSol01hU9zkCgLkk865_EJg30KgP3WeZtnYbMaczj3HTwY_4BI4WHGDTN_HkIEN2xadBj39pxSqd_ms0E2pGpa03CaBBm5s3K2-hXZ-sUSloRGkYk6ePYFiDqhlWFw8w1VEf_I5S7ZQWNBrnx9eNUVY9CSosZp2s57ZjJ0DzzmFwjn9EE9tKBLel8sDmGagPSH1wz61TtbVaX1savIjqg3ZVYJsHdLavGyvzxZuDltbsCL4wMdH_1xrE6xNo0yfH0NsqSoenI19OUSwZDG7Mkn_B2TtvH5awl9ZSTdmWb1n28JFmt0kt3CfNHaIBv6G72DID1MJstLw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">پیام‌های دریافتی درباره دو پست قبلی
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 249K · <a href="https://t.me/VahidOnline/76412" target="_blank">📅 16:44 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76411">
<div class="tg-post-header">📌 پیام #56</div>
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
<div class="tg-footer">👁️ 271K · <a href="https://t.me/VahidOnline/76411" target="_blank">📅 16:38 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76410">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/pmMoNqZ5WEAEZSL1GankLbcV6QrzY2Ccq4mhRzv6di4yFGtzsHODDG_XqSchtzlRQUmcpdmpoKfwnwK82QDuLNwKKlxUAqE8fCcS4qkMHiWaX0oioD9KjncMnGMaUmt8dpBSXUrYve6AwQzHhjTvuC0yTLoLSrrHG_ripMxIjFTOEAUkwU8_Eq7YPoomkFv8qLU4XQz7GoqbLbYd5yatsHodzq9t9eYepiYvpBPPfwziALED0UxvBJz_b4_GwtgaivRRrVyANPU1gWGB91Hoh__jz7VUnwN8AcQVlvEYTV3-xoo_a-UxyufbD1pepvsHAtqr17FDOvS3uvuSxJ2bfg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قوه قضائیه جمهوری اسلامی اعلام کرد که روز سه‌شنبه ۲۶ خرداد دو نفر دیگر از معترضان دی‌ماه پارسال در شاهرود اعدام شدند.
خبرگزاری میزان، اسامی افراد اعدام‌شده را جواد زمانی و ابوالفضل ساعدی اعلام و گفته است که آن‌ها به اتهام «محاربه» و «افساد فی‌الارض» اعدام شدند.
این نخستین مورد از اعدام معترضان در ایران پس از اعلام توافق تهران و واشینگتن برای پایان دادن به جنگ ۴۰ روزه است.
در بیانیه رسمی قوه قضائیه، از قول محمدصادق اکبری رئیس دادگستری استان سمنان ادعا شده است که افراد اعدام‌شده «اقدام به تخریب و آتش‌زدن اموال عمومی و خصوصی، حمل و استفاده از سلاح سرد و گرم و اخلال در نظم و امنیت عمومی، اجتماع و تبانی علیه امنیت کشور و سایر اقدامات مجرمانه» در شهر شاهرود کردند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 350K · <a href="https://t.me/VahidOnline/76410" target="_blank">📅 16:22 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76408">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/up6z8r--O2uH37fEWUPZNdpca7f3Kw6SdV_AM4k49tUjm4LNMrF9od_2AndguppV0qGSjcnbUXDYjjqhF6apGA9MtxlhT7KOVww4JoirUc2VP5rk3JAP6KrCAuWkflnpGs4-2reJi8JNgMQX6opzWTwUqgeqafWkgY6lgL_NsFdx7s-MQn7aY9iAZHsSFcUhy804fq6O2H322511tdnmAf88-HwbqigMuVtZ3Lg9_jRIR6p0UD_xTI4aWcCwBBKpGEC0qCWEQcQZm9MmnM6bW3_PFiQZ-TElx2Zm1MunymABahXPzfu3a-g9Lq7kfsBibqH2C3jVh1lNklRJuHl7bQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/L7ifM49kYSO8nxVXjPjVLzMgZs3q2skPciAyWmOijLjOFymmkiUVoPn7h_2Tc71-DrKwyqSlCKwcbs8ltRpkP4y3b5mnxCoPJ0hYPl-akJP1OiirKRLdQl1Vr8k0S_s_dGtsUyrWYhzH7s1B5VBHbaka8kxYBR7DBxtLJOm20L4JWToL-eMT1_l5PjRn3pMDkkF16untpAdMscLq5NudM_cxtwGu-M2lFujPj2MUq5qhUhpoEOodUjeACS3lq_HXRz27--QwqoYhVPUeAKqjQxdqE30ivzzq2tdKveJS8a2yOOGyVn3h79dA1JGW7GGu-wDTxDIF3HqzdjKmLtYtbw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">مسابقه نخست تیم ایران در جام جهانی ۲۰۲۶ مقابل تیم نیوزیلند با نتیجه ۲-۲ پایان یافت.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 404K · <a href="https://t.me/VahidOnline/76408" target="_blank">📅 06:51 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76407">
<div class="tg-post-header">📌 پیام #53</div>
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
<div class="tg-footer">👁️ 402K · <a href="https://t.me/VahidOnline/76407" target="_blank">📅 03:54 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76406">
<div class="tg-post-header">📌 پیام #52</div>
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
<div class="tg-footer">👁️ 388K · <a href="https://t.me/VahidOnline/76406" target="_blank">📅 02:49 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76405">
<div class="tg-post-header">📌 پیام #51</div>
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
<div class="tg-footer">👁️ 374K · <a href="https://t.me/VahidOnline/76405" target="_blank">📅 02:49 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76403">
<div class="tg-post-header">📌 پیام #50</div>
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
<div class="tg-footer">👁️ 349K · <a href="https://t.me/VahidOnline/76403" target="_blank">📅 01:35 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76402">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/v_nfyQi44SrcRyzn1kD9LHS3tuKxq31B-9RbxLlukDhqz24tjfsjOWuNyqbzTb-tHIw0GcGj1CqbvFO46K0poZ3nyJ7IP3HFcgOf9gifa5M5exCCaWav6Wra3d6aKD3KccHmSLsgkWZbUb5HXU3PHo1WI7vb7g5wjkTLLVYtfASR5b6NCoxHbFRpYtQVvDXXyAkmKflY29IlqFuyx6Nw3nYSOizIGpBkuylM2LRsm5LEuI0h40BD8YYFDnWpIh_DwALnsyupGooPK8FiiaQZlSPYXlO9LCKSa1X0jbB7Au_I2pZ3nesf6R9eIrhkE7_BcUcVmd7eFNklLM_uFVay1w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرگزاری مهر:  منابع محلی از شنیده شدن صدای انفجارهایی در مناطق جنوبی جزیره قشم و تنگه هرمز خبر می‌دهند.
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 340K · <a href="https://t.me/VahidOnline/76402" target="_blank">📅 00:44 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76400">
<div class="tg-post-header">📌 پیام #48</div>
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
<div class="tg-footer">👁️ 346K · <a href="https://t.me/VahidOnline/76400" target="_blank">📅 00:27 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76399">
<div class="tg-post-header">📌 پیام #47</div>
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
<div class="tg-footer">👁️ 335K · <a href="https://t.me/VahidOnline/76399" target="_blank">📅 00:27 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76396">
<div class="tg-post-header">📌 پیام #46</div>
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
<div class="tg-footer">👁️ 364K · <a href="https://t.me/VahidOnline/76396" target="_blank">📅 22:54 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76395">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/10d585b107.mp4?token=N8foZdWfhSPneEgKtw3862G2PwNngT14ZsX5WRUQ2h-sTW3qvP3KOT4ddtmh0NAD4bHAx5LEjSJ9JEjXmx9KWfQKgCRjmHB7HgwyKl67YqjsvHJZis07ZHkwKg1W3Q2rDaNH7-pkN7Abg9AqGzeTVp5LT3_CnbOLD2r13cjQqh1aHCxl1OSgwWi6kFoUc380jiwt1hd2m2au3EbqAb4W0fni-VYjjB3YcnUKyp0UMwPa4gYBaf8YoJ2SsAASJtN8qLpZzDol81KcEWxXHSW7WX3Jv7kjWaeya0s_k5EgLwFS5xJjY7_6YBOayj8dte2XZs-CRdlxuVNSWZVLPEFjR7aWNq-7xI_HfTj91FL1PuELHEyJlUmeY7UQmBvc2-jkNmc5r5RXww-EYN-5IX8mW0c0kc_QPuRya9_6H-5XY3DUkyjXcgy2KP1hYPM-UZNUKGzdFTMWACYZX8bvhHRvKvZul3QHhfhRVJoXIjtpkxobb6tfaF14mI-3De6vMLmZRbxvaY5pcNq7s_OUxc_UIhdwjMlIiJEG64NW99YLuKl1cR9fRwxYJkBMIiUMRGm34terre6ht1p7T4luaG4DHGOg9x6ZDWmJ2p-a27p8ltEsQB_QBSuScpyj9gcBqX1T77zQtvrZzR83ykQ-uBvnjOMmU0F-vXjvLwhuGsF7r70" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/10d585b107.mp4?token=N8foZdWfhSPneEgKtw3862G2PwNngT14ZsX5WRUQ2h-sTW3qvP3KOT4ddtmh0NAD4bHAx5LEjSJ9JEjXmx9KWfQKgCRjmHB7HgwyKl67YqjsvHJZis07ZHkwKg1W3Q2rDaNH7-pkN7Abg9AqGzeTVp5LT3_CnbOLD2r13cjQqh1aHCxl1OSgwWi6kFoUc380jiwt1hd2m2au3EbqAb4W0fni-VYjjB3YcnUKyp0UMwPa4gYBaf8YoJ2SsAASJtN8qLpZzDol81KcEWxXHSW7WX3Jv7kjWaeya0s_k5EgLwFS5xJjY7_6YBOayj8dte2XZs-CRdlxuVNSWZVLPEFjR7aWNq-7xI_HfTj91FL1PuELHEyJlUmeY7UQmBvc2-jkNmc5r5RXww-EYN-5IX8mW0c0kc_QPuRya9_6H-5XY3DUkyjXcgy2KP1hYPM-UZNUKGzdFTMWACYZX8bvhHRvKvZul3QHhfhRVJoXIjtpkxobb6tfaF14mI-3De6vMLmZRbxvaY5pcNq7s_OUxc_UIhdwjMlIiJEG64NW99YLuKl1cR9fRwxYJkBMIiUMRGm34terre6ht1p7T4luaG4DHGOg9x6ZDWmJ2p-a27p8ltEsQB_QBSuScpyj9gcBqX1T77zQtvrZzR83ykQ-uBvnjOMmU0F-vXjvLwhuGsF7r70" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">"خون آقامون رو چند فروختید؟"
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 354K · <a href="https://t.me/VahidOnline/76395" target="_blank">📅 22:47 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76394">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/4de6c46b4e.mp4?token=unWxnK2YE1gKAx-9WA8E5VLS0S2z0ytIGkEVpBWiS3P6nlozBylItkcjstzf9H53Pq3yt_CvdYlBiI0d_d0-BQUm4LI_LuKaF1SaYKo4oc6z4i8X_TB3U6RyA94UGqsVGl3lkmJhMAnor_MeZUi0UXbjDiF0dGkN1EU_BQDvsRv71SiziNn8jCQTdDjKXul8zYomHOf7wjsy-_LiESDxZ8CGk0mDbIP6WI1DtBNP0Ghf6zbckZPhF0SsQ0NJoRqUaZyszTWsgGbk-efyZbP1MSXH6_BbPAyVhaN8oSlcehfPmaPsn2vY7H1MBaeBZjAg5iCpWArxTLK3Ol7THHVbaA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/4de6c46b4e.mp4?token=unWxnK2YE1gKAx-9WA8E5VLS0S2z0ytIGkEVpBWiS3P6nlozBylItkcjstzf9H53Pq3yt_CvdYlBiI0d_d0-BQUm4LI_LuKaF1SaYKo4oc6z4i8X_TB3U6RyA94UGqsVGl3lkmJhMAnor_MeZUi0UXbjDiF0dGkN1EU_BQDvsRv71SiziNn8jCQTdDjKXul8zYomHOf7wjsy-_LiESDxZ8CGk0mDbIP6WI1DtBNP0Ghf6zbckZPhF0SsQ0NJoRqUaZyszTWsgGbk-efyZbP1MSXH6_BbPAyVhaN8oSlcehfPmaPsn2vY7H1MBaeBZjAg5iCpWArxTLK3Ol7THHVbaA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/c3fdaedd66.mp4?token=auRfEc0mwR7gRsSNSvXLHZmR78wSkvjN-R4KWKjJz0zyEQn1xTHX-p87whLtY1JDIZczLk2CtVJfOSJ607czj8wWXYBWNUKtySIYfd3H7akYvErGuBHeWV4BS9sqOTvjxH8N4QlbHP6w4d-RUHIGiF_o0_BYTG6fENATyc0UXTfytInRKSI85vdXINkFvXjOvmh-6bYHxg7slXwi0rsW8BHX6CLjpr1pGwYGGZYtxc6YcOiJ74wzemjiyFCUi-3REHJgGXsFvM6sJgEvUL9bJ9Gv1rYAhp4vAxFvpLZpiFYC-e15QPzD2ykExESNtUFfeyR80emHgl84-aKbAy01tQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/c3fdaedd66.mp4?token=auRfEc0mwR7gRsSNSvXLHZmR78wSkvjN-R4KWKjJz0zyEQn1xTHX-p87whLtY1JDIZczLk2CtVJfOSJ607czj8wWXYBWNUKtySIYfd3H7akYvErGuBHeWV4BS9sqOTvjxH8N4QlbHP6w4d-RUHIGiF_o0_BYTG6fENATyc0UXTfytInRKSI85vdXINkFvXjOvmh-6bYHxg7slXwi0rsW8BHX6CLjpr1pGwYGGZYtxc6YcOiJ74wzemjiyFCUi-3REHJgGXsFvM6sJgEvUL9bJ9Gv1rYAhp4vAxFvpLZpiFYC-e15QPzD2ykExESNtUFfeyR80emHgl84-aKbAy01tQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جی‌دی ونس، معاون رئیس‌جمهور آمریکا، در گفتگو با شبکه سی‌بی‌اس اعلام کرد ایران در صورت پایبندی به تعهدات خود ممکن است به صندوقی برای بازسازی دسترسی پیدا کند که از سوی کشورهای حاشیه خلیج فارس تأمین مالی خواهد شد.
ونس با اشاره به مزایای احتمالی توافق برای تهران گفت ایران «ممکن است» حدود ۳۰۰ میلیارد دلار منابع مالی برای بازسازی از کشورهای خلیج فارس دریافت کند، اما تحقق این امر را منوط به اجرای کامل تعهدات جمهوری اسلامی دانست.
او افزود آمریکا با سرمایه‌گذاری کشورهای حاشیه خلیج فارس برای بازسازی ایران موافق است، اما این اتفاق تنها زمانی رخ خواهد داد که ایران به برنامه هسته‌ای خود پایان دهد، فعالیت‌های مربوط به مواد غنی‌شده را متوقف کند و با یک نظام بازرسی و نظارت گسترده موافقت کند.
معاون رئیس‌جمهور آمریکا همچنین تاکید کرد رسانه‌های نزدیک به حکومت ایران بر مزایای توافق تمرکز خواهند کرد، اما از امتیازاتی که تهران باید در مقابل واگذار کند کمتر سخن خواهند گفت.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 316K · <a href="https://t.me/VahidOnline/76392" target="_blank">📅 22:40 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76390">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromFactNameh | فکت‌نامه</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/ShJmU4EVYhG_pt9yoMRdCzHOxm-iEbOD5xJVOXegINsECnx72inSlHxhNgw3AD7YBINlsCEYXpUL_ef7l6OuxrkE2vFITsEQJ_72EsV92AMfYfW4vkzEf5eyr4Ix8Eao8TUr1Q62K3lhhYKxKsrTsbwpGXPk4z5OnP0kP898GyIjA0wiTxXv88iriFLe3DWilprpKaEAB1uk1Vt1nuk71hG_o4yaK54Ki-b0pASQ5yejV7eM9C6coR35P9QaiN_vYxK2HAGACSmc9Y7GX6kTd8ySPg7jENRzJD-47sPc-g3nITfOcQGQcdsP7WEyqSCR-ihiA9kKEhFCTrgDf6a_2w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/dq-k2OzbU4xwQwcn0sqLXhk3aVndzh14f7s6LxTk0q1K4ALdVvQ-c21ypm-eLGpUktns97VHYcXnJPAXDGWTZGhonhnpvzwc2RmUr4bJOcEzNuZBQdeytEz40WxwPsjouV3DKlsW3FFeilCOLQUTSz54-BM0xVjg6k6MA5m4J76WNNPyOm86zL1KS41iAr4YZiJDd_F5_kyF_uZ53MUbj8cWvR1JG-P-kXBOaj2mtp8PlCXk2taOJrih12GcCLFr0rPKUvhnQhfCowJrhLVYWp41kKvN3HYctVdzlSH_nqHzFPkXzeHhJBSxB1KhWRxA-ow7CBJZH2gFwxlL65Wurg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/ccb668e4af.mp4?token=j3x4UVztt3vG4JGDe7lMtVRxCVoB_xkO4o5dnQak-4imHKEMrGnNZEmKYIi0YX9ezSzEHmwiZPSLvGlb5pbY4uZiuQvW-SH4_f_jeUBgndkSiCj0Z2-It305bGRi-9g0x68xPxJQHIwORT5PPmeFsPtVYyggTOK-yToYoFWxxEHjwn3r9-nOMtmhoyS0Eb4Uzxa-ZvHEn0zXRbhJIJvA5O7ffYb85onTR_oIZy8yDVwL_7u_CMQFR5V-ajFhWhW6ePzlUrnqN14XgrLJb9YnYuR7a2WLJ_jolcEVNdbg6lBPYTBOHb9T00wrOAnTCzxPPCNq8gCJ2rFe_Kj07C68ow" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/ccb668e4af.mp4?token=j3x4UVztt3vG4JGDe7lMtVRxCVoB_xkO4o5dnQak-4imHKEMrGnNZEmKYIi0YX9ezSzEHmwiZPSLvGlb5pbY4uZiuQvW-SH4_f_jeUBgndkSiCj0Z2-It305bGRi-9g0x68xPxJQHIwORT5PPmeFsPtVYyggTOK-yToYoFWxxEHjwn3r9-nOMtmhoyS0Eb4Uzxa-ZvHEn0zXRbhJIJvA5O7ffYb85onTR_oIZy8yDVwL_7u_CMQFR5V-ajFhWhW6ePzlUrnqN14XgrLJb9YnYuR7a2WLJ_jolcEVNdbg6lBPYTBOHb9T00wrOAnTCzxPPCNq8gCJ2rFe_Kj07C68ow" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 310K · <a href="https://t.me/VahidOnline/76389" target="_blank">📅 22:09 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76386">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/d206f4a845.mp4?token=J_uahCfp3rJCmhWucWg_4qTgVpQF0f2g1NAodMFjSRzcGhg3WsB9kTKchI1VhCbIdWP_Ow5-RqZXP9nF0waDWuGtOy18XM2om6vTogsgGp9uI3OS99SGgHbfgEWJc0T1OAdVn7t27mROvaYkgeHgT6Gpdv68VjVbMOwg4eibCXOBodPbszho9YDJOTIUR-E2fU1yNH-B_TVU64n_OWRJ36Secvy4owhOShheK4GeaqGNaNP45kLY5tvIWWzv5SAhXunrws6KWK9KNHIUUMQtT6Rjw2M9HKc2DnDu2LMxv6aEqZYIVHRYf72mGggbNO42zBQsGfa_-GIMj2E_ipRWJA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/d206f4a845.mp4?token=J_uahCfp3rJCmhWucWg_4qTgVpQF0f2g1NAodMFjSRzcGhg3WsB9kTKchI1VhCbIdWP_Ow5-RqZXP9nF0waDWuGtOy18XM2om6vTogsgGp9uI3OS99SGgHbfgEWJc0T1OAdVn7t27mROvaYkgeHgT6Gpdv68VjVbMOwg4eibCXOBodPbszho9YDJOTIUR-E2fU1yNH-B_TVU64n_OWRJ36Secvy4owhOShheK4GeaqGNaNP45kLY5tvIWWzv5SAhXunrws6KWK9KNHIUUMQtT6Rjw2M9HKc2DnDu2LMxv6aEqZYIVHRYf72mGggbNO42zBQsGfa_-GIMj2E_ipRWJA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 303K · <a href="https://t.me/VahidOnline/76386" target="_blank">📅 21:30 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76385">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/8e8cc0eeaf.mp4?token=Fr94WfS_ISCRwPNHnaQNyoAXaNAndsqgp5FM3ipc2UUuvDPWdYkx77lzwBEkUNeIxN4HRW9xjDIyCTi3Q2by2ah4vdd5Os36hL1E-fa291Z3qS_tFbdV68seX8PKWeRwvqgf-7kA4e2hdAuOmnvJGNlySmFI6OxpsqgVVdm-6FggtUhry_4oqikDcM0phP3ojtVrRr8xYIks8N4rgL3B6KYGPG2iNw_1CoeUG5tiqhMnea2oAaycEpy7M-94xVNExbjvb1RTXiRhuVHRq9Ohudx9rEkXDBViJTy5zdM3nzb9na06JGhRuVNFzuGlf2jsvTq8btxPQGczdgcWLMlr9g" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/8e8cc0eeaf.mp4?token=Fr94WfS_ISCRwPNHnaQNyoAXaNAndsqgp5FM3ipc2UUuvDPWdYkx77lzwBEkUNeIxN4HRW9xjDIyCTi3Q2by2ah4vdd5Os36hL1E-fa291Z3qS_tFbdV68seX8PKWeRwvqgf-7kA4e2hdAuOmnvJGNlySmFI6OxpsqgVVdm-6FggtUhry_4oqikDcM0phP3ojtVrRr8xYIks8N4rgL3B6KYGPG2iNw_1CoeUG5tiqhMnea2oAaycEpy7M-94xVNExbjvb1RTXiRhuVHRq9Ohudx9rEkXDBViJTy5zdM3nzb9na06JGhRuVNFzuGlf2jsvTq8btxPQGczdgcWLMlr9g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 320K · <a href="https://t.me/VahidOnline/76385" target="_blank">📅 20:33 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76384">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/si5-_auRC9CMQIZ2_HJP7-zatTkBxXIRUD606yBKf45y7RpuwpL0KwYH5MPLT2hlkU0fsaA06dZui0c0qhlzyraxDF-NQsCcGUPGiwX9f326ptg8FOPZAK3o_xR3rHk3PEejpez_MokU9QRfNVUydxhNDXjO7Xchn15ljgGzB5FyXlb1VX_1_Pf21IwM2dRthIditltJomf2bliDV_UwxSYbfDORAgxb8IkL9whAvXJ4jpa3bKhQgeQiKVW-stCLLTpDOPclPLAfoaM3S6BZdXCiQXmb2PBplc-_bQvONeqnIwfG2sa-atn8vWTUWORj3fhdhPkjwbVBgKCVJK2YOw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/e48597c90a.mp4?token=FIjq8S-cWyJcjtPnTOCyrzRJ-QYg5zc6BWmfNF-KTiLeIE1eFjOlk22RbGw4qrLsSOXCxmQQtHmnNht_t_tLfkzaTdhNVBJMGT6In0Zd5ZGm_FwMe6VS-IChxtWXkE_5a9LRBG3_KywiYfQxj01fcpYQAa3FZOVnnPbjIi4pq0CN5gE0GknAwxjUFyuEIpJ33tTNlNanRNNF0CllRgymxnIogQYqA6TsmgYDMcfid7Yc7j_y6fhSz9nDkmFzl-izKMmwg_dyWBKxvLBGtVkwHjcVRDu9RMsOhoSzDoQdStZBvVRJgmRfOsjQFM655FWkOMSDxzl6DmagSMgtX8QUVA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/e48597c90a.mp4?token=FIjq8S-cWyJcjtPnTOCyrzRJ-QYg5zc6BWmfNF-KTiLeIE1eFjOlk22RbGw4qrLsSOXCxmQQtHmnNht_t_tLfkzaTdhNVBJMGT6In0Zd5ZGm_FwMe6VS-IChxtWXkE_5a9LRBG3_KywiYfQxj01fcpYQAa3FZOVnnPbjIi4pq0CN5gE0GknAwxjUFyuEIpJ33tTNlNanRNNF0CllRgymxnIogQYqA6TsmgYDMcfid7Yc7j_y6fhSz9nDkmFzl-izKMmwg_dyWBKxvLBGtVkwHjcVRDu9RMsOhoSzDoQdStZBvVRJgmRfOsjQFM655FWkOMSDxzl6DmagSMgtX8QUVA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/06a4a159c2.mp4?token=t-NJD_6LshZfGo_mDneDReo45gTmlf9n8zamMM-ADLSA5MVAZVAV73JXRU4BIndOa_2um8qdB6K0Q_ZWUstq5Knuw4Uxs1gSzoaobRfBBeDb7jcelBMCwjVDgYFEBrhVL82KJ_6IR4lTFWfJiDzkeZ5Z2AkaOhIk-_YYyddqyYCkkp3Y4qqWdoAv1riFmueM088eqAvmEO83PCEbTX1kdGE6ouJKib0DaO30ax14luz8YDIswzxlubrr7vtHlKfciQzRrKkrn470fbFRf6TRcPcgPp5x9bADcNVDbgKxduDvXmdBR91wVVkaP-DvK0WhKXQjFZpLmk85kKdvTv_IGw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/06a4a159c2.mp4?token=t-NJD_6LshZfGo_mDneDReo45gTmlf9n8zamMM-ADLSA5MVAZVAV73JXRU4BIndOa_2um8qdB6K0Q_ZWUstq5Knuw4Uxs1gSzoaobRfBBeDb7jcelBMCwjVDgYFEBrhVL82KJ_6IR4lTFWfJiDzkeZ5Z2AkaOhIk-_YYyddqyYCkkp3Y4qqWdoAv1riFmueM088eqAvmEO83PCEbTX1kdGE6ouJKib0DaO30ax14luz8YDIswzxlubrr7vtHlKfciQzRrKkrn470fbFRf6TRcPcgPp5x9bADcNVDbgKxduDvXmdBR91wVVkaP-DvK0WhKXQjFZpLmk85kKdvTv_IGw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/cQeP2gJec8TzbBI7-EfYHGin75bE0wS8K3ITAFxeHTnSBhUF737tFb_QHKrqa_pxpsiyM1dXFfjC8wTKIi2R-ttKe89lk_w3HDu-F01KC_jCmhAE2LyxF54BRGxsfYTF1RfTReKAl05x-SwZGeZe7nQc2TTA9Bvm5fUs2BrdWtaIxgVyF3KWeLbsO9E7PVYVMMXTbFF1g3dHEyV7yXXi_82smKjuU710ccwPGau9Hq3kOr447EaWkfj09sIXk5gCbh3XOLrJneOO3u_Y7ENNd1l8cF4COLyqoeXQvcra8JtYu7RHs1Y42VCchtmPIaho04U0oBN1josv2Z4XKHWvqA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/NYQd2NEiPyD5wKYyMGaJ9awHPXOK6shfrHzby6FjqMjxaW73C3QSDqYGbQDn-BfsJ1_zskLx3BMD8vkoFPX1O5vPQGFvGpOVCigKHCoiHeE40XBsYp1fA6on_lnMZDTRrbpPG2RG1fAX-zFyOjEiahmub8gQ3-Q0BsqToECrLaCWJa_R9DaRUThfHWvvtWpQ_gBkK2fgusFQIY1MBqOk44vBXOP66eIWoxut4TDyA5yNoVi_SEb9C9HARodVxc-MH1CSMm-qrWeygRpx5PiA1htvKj8Hhb1PP2osrogOQEe66u6Iy_fYDe47TQ5bHk7tRSS1YOS9pbQxydbqjId-1g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/A6cXOr2LsiTajA_F_vF0no7iM1Jt3fuhfKdyar_h0Hak6LRqgWOqyE-_lv6xCSegKffyfQhrlsgJThsxvxTxNxdCd1VxpZfW_UUwgGFREFF6sXkn_h9q15YVNFeqEP3MfnzpTbikwFCj-dE6Fo2s5mgYFbM9zeXBajw2MGlsyuvDWbNhvp1tMGGacjSp7Q8vG-ffPW3S6GxUVaB6x7Sk3QH0XeFhgj0pa1EeM0neScFFf9Tx2mPJJfygS9QKX9LZAMxW0ZCoPDvVgdZfHKLMki5hkJStvZpg1xQ7I3t4CUXO_Cnig57XgQmwA3PFgQU_tHhYiebKtYEKFSTc5VjiOw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">منابع حکومتی با انتشار تصاویر بالا نوشتند:
کلاهک ۵۰۰ کیلویی موشک تاماهاوک سقوط کرده در اطراف ورامین خنثی شد
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 268K · <a href="https://t.me/VahidOnline/76379" target="_blank">📅 19:10 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76378">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BGq3heVq2giv6L2jdfK0MZgj3qlCTiXta56CGMEwfwt4JTjfAl7mEyF75IKvqyFi9kz9sr8IdhtTsJnabOpUxRKvtPTDsl1W6YucXDKpzgxMJFVgWDXOO_IeQMwgldaA9Q5bCpB60_GwOtNKrSPE1dcvDdEbWHc-xzc2Pkm3oXtdJ9fdWWalHdPLmvrt7RQMXQ6YoYNg7g_ynFwZiiBUnfYKQI-M0R7Bpee2iCwYWpzsaEgMzYbe4u9NBEN0rkfIFWkMmCRlMT5q-LAsoroS8LdMqT6kucyxvr8nHUTI6s6uXcnXpHR0Emgdaubi0OqGhAqw5HHKsRjYa9kgFFpQvA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پلیس اطلاعات تهران، روز دوشنبه ۲۵ خرداد ۱۴۰۵ از بازداشت سه شهروند به اتهام انتشار مطالبی در شبکه‌های اجتماعی خبر داد.
خبرگزاری مهر به نقل از پلیس اطلاعات تهران بزرگ گزارش داد که این افراد در پی رصد فعالیت‌های فضای مجازی شناسایی و بازداشت شده‌اند. به گفته پلیس، بازداشت‌شدگان متهم هستند با انتشار مطالبی در شبکه‌های اجتماعی به مقدسات و آنچه «مدافعان وطن» خوانده شده، توهین کرده‌اند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 298K · <a href="https://t.me/VahidOnline/76378" target="_blank">📅 19:02 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76374">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/tEhZNUTwVage71pHA2_0hX1Q20mLBTFyytTCJkimDkx2CMb1xoPqvl0ob_amKPIBHECtdb8u9Ppix96egHvlDCgZNSi2xlkqA_WumFgHF50CLTKbMJWhmIpm-f93BTGWx3QdA4UYPCM2cXV-P0oLUMP8Or8YO90ufkslJWKI-KT4YN_xqsJvGM9H0X-fKAR5J31LlGS1hf1L2uk1bzGutHRyI952iNMu3rX2XCLGRBUV-1j9WZK29mGRNXIVhKD0tIKO66FDvs5MbSGbMYkw621kpe7CQFuYdJfzFaDv73l-2nXC9HeA99dvnKdYEMPHWYKf7Gtq5tyyOd1IV4crsA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/YVI3AbTqCtTOrQdejZ4G1L8dRVU2ypFWCZXgbTiCwzSQePbZXRYdrEYQ8XFq2sgY5eAg_SbNbl24H56e63P3H4P-d8tBF_bs3_9N5HbN1iqOARcKHjckAbLduI-AtyU6cq9n5Zi-vwN40PI0eAJsng1ous7Xin93OCfugiiA_jK6oX-uOAZJ2yX7JoVk5Jm4Hcn6awLgtXIFBdqAB8z8sBAxlzN4K0XMjikhNZss8vuPXGu_AXj7EjGx2o-BIShac6qNwNoFRJSTdhBMEvJvRKvc4ztEuN4kh9NTWQoT5Ze2NbQSUWHtdh1z7M0q3nGJ0ph2eX6455XofWF2-EUQkw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/t7opohQjzaRNTuSnTjGJCOb7EZ4yhT6tz4ynwdWrYi_Z6Xuq-GLveh6qF88vxBnAgMAoJtwXsdbjl3mx8e0JVm2CiAc3R3JNmrIluw1BZlP33CjHZzxJjnHKBxj1rB0UoJ0QD6iU-_BERJV_W7w1XBObCcNESRcPpfDofXO4r9CxuIsCDu1fghGxAqXDb4sm9PH-1DXXQujiGdJlRjc6E4t4b92MLmJLUsWv7j5E9ggtgFCGnHtW1ojOS-4vL4zxHlzzgMDuvp3A01Z3NW2-YE6XntSKyjGvclrO7K2LZBFG_DPMR3JoEUYIxEfRteuIEDpLMtnLYLhOuq44sozfBg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/65becd728e.mp4?token=kE5ir-q8LOxPU5D3EYd-J5SYOMJBjYqq97HO6ICoNxqlZwjeHob7wbYk0VBfBupvWjxT-K_QLlOYjElTOraLwZix5ssSS0dfKz83ZDkMPJ7Y0HR9iFJ3xAjQ2SMnmLeCqH_Ua8SUsn6g1e8QYW6gCPjETH4hy3SL8eaNo3XGl3QLe9OaUs2Wcq5qTpClQUxS6iwVblAiW65_tT5a7XLdSYZhl7A2U0vyGX4dvSpndxbFkRjRTPRTMST6olwrUFQFhTG-c9eh3EzBPLEGO_qCo-_Nk_BqknZbjpg8DBWl2BUUaKMMHVIi0J-Z5zQpANd99mF3vkr9sB5RB1ka9tYBiA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/65becd728e.mp4?token=kE5ir-q8LOxPU5D3EYd-J5SYOMJBjYqq97HO6ICoNxqlZwjeHob7wbYk0VBfBupvWjxT-K_QLlOYjElTOraLwZix5ssSS0dfKz83ZDkMPJ7Y0HR9iFJ3xAjQ2SMnmLeCqH_Ua8SUsn6g1e8QYW6gCPjETH4hy3SL8eaNo3XGl3QLe9OaUs2Wcq5qTpClQUxS6iwVblAiW65_tT5a7XLdSYZhl7A2U0vyGX4dvSpndxbFkRjRTPRTMST6olwrUFQFhTG-c9eh3EzBPLEGO_qCo-_Nk_BqknZbjpg8DBWl2BUUaKMMHVIi0J-Z5zQpANd99mF3vkr9sB5RB1ka9tYBiA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GjU4xEw8wc_cpXk1jlNhgBcSxxDq1pyCrNMk_-WZAhJ7RTMi2spQfNuWw4SztNEw_eFHl9LgV2UNGyUJTSL0eUPIQ1pRCH-aN7sUkXzCMNXrTLmUMqPF0D-LQSbIwbXIOJ_1a4HvEhuhav6M1opzyJK6mz1C01Zo1L8dvRXPcN47wseuHDT2eXN7lJdfkyKDAWlkpjMWxvM1V9JWI7Kijl-Ps-N3bdSWHHjlrgPATmQADLMhzZVLCfxiUsgJ0jtir9jieLLU7YY0m9NT9YswVNONwv6Me8EQGLgaklMpaXoJZ95vqdmoX12K3lon_GNHxboQ4NHp2hlmhE7sslu6VA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرگزاری رویترز به نقل از منابع امنیتی لبنان و رسانه‌های دولتی این کشور گزارش داد یک حمله پهپادی اسرائیل خودرویی را در جنوب لبنان هدف قرار داد و راننده آن کشته شد.
این نخستین حمله مرگبار گزارش‌شده اسرائیل در لبنان از زمان اعلام توافق میان آمریکا و جمهوری اسلامی است.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 260K · <a href="https://t.me/VahidOnline/76373" target="_blank">📅 18:51 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76372">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PRj4XIhVgzsNQNOZRFD_fs57eXo0pK3ynL0eNvGa7gDEQi0jl3FHqthIHRtbAbE-M8AR_KpdhPW6dPGlETnPH2G3x17UmOvjU8iC_g0LWlbmlTjCg2VQyUYGuLR_H7yRd2dghjrQHVml_VniNhQZZHxawsOMp0S2OS94VK8hs2i7YAytmqCBSdQAWN7TX5lKi_MMXZKN9qDoull_78yhn0ZX9mPbgPBMa-PxnD2BXwOu6I-ZhhyO07upW5ahxEV9AhZd8UnwmtM3LQ43le9SWm_Lr3wM501Jegruo9UvTYqt0Quq6cjtcsnB2XX1Jb4MjYTOZOHsSZPw31z2VPaoag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جی‌دی ونس، معاون رئیس‌جمهور آمریکا، روز دوشنبه ۲۵ خردادماه اعلام کرد آمریکا و ایران پیش از مراسم رسمی امضای توافق، روز یکشنبه (به وقت آمریکا) آن را به‌صورت دیجیتال امضاء کرده‌اند.
ونس در گفتگو با شبکه ای‌بی‌سی گفت توافق روز یکشنبه «به‌صورت دیجیتال» امضاء شده و قرار است مراسم رسمی امضای آن روز جمعه در ژنو برگزار شود.
در همین حال، مسعود پزشکیان، رئیس جمهوری ایران نیز، روز یکشنبه در مراسمی دولتی با اعلام همین خبر گفته بود، توافق روز جمعه و حضوری امضاء می‌شود.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 253K · <a href="https://t.me/VahidOnline/76372" target="_blank">📅 18:40 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76371">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oj3Ni8WhAJBoTFvB8g_rciAx_9Ffq0k5rTThuEtxlu0g89qNWc3HMrPecweTTOs1GK44eWXjN82EvloZeWdrk9ylWrQ7joRhk1swBOAtdYgim_1U_Qyd_1t890_ysU6tnHDCnGcFqjxAM3Ap303naz_Ee4ydCsvWDU4EC4cI_9uV48YobiJ9Aw47X1PNIYttdnKZxv6OkCmXS3y7T4-jyQklp2krmb1ykL1iiZnVURUz3fpuu1yr0zYMfId1NYhsXuDHfxuHjDrPeVrAFFBcWoy5ZQVSxUjoJjF2MSOxpTzjKFWNOV_Tpr0y8s0NzkbJ7S4JWPNBbJP8omwWhwZDfA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RiZKte_NL2ck3NRryZSx6dRK9HpHUe0y-juEUOXyb6KIbUj5exg-rAGislR-tu5-joKUFl9b72DXMpxGaiGbPCMmB8ov5FCUi_c3LjzyYjbjgxXWQO2OFbd1Az9xQhAYO829dkSUhfZTftDkR4g8KZfuv1uSMdjvmezR9PfG1GC2AEOPRcfuQZY_tSZPz3XM9LhugPsVW0wvaugwJkM_Wpbyw10o8lpmzW8YN-OJ9TtzZHbPSs3JCqL2QZPPLZfOLAk0V9DnIPnpVmySFRwO9fMe6PPf1oio57gJLPzDfzIj0d9Z5Nzo6jW3FWS5W_UiHU-tqsCyRV4WSGjCAaOYag.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mDRBchUYkTTRvAVF-i8-faRWdrTdMrPpGT3G56Xh5hJxIT3X1Jg12mPOnSDMSpmVBWdnfCTHkQx-4CNhMDHjKYda2ftUoRYW3tcl6OQkoLPZDQyU0B_ceaTuTYO4DXbhUizjj1V8msKsH1UHVVgh9jQOZFQSGHZ3hp-41mJcEVIq_n-ToJpO1Qs7dVtU1OMgCDtsJwrgrQGGKFCiNWCu4mbJ9tJH5Dgek_ztv8lidQhxBNQxIqSv8B2DQKANSd-Kfa8Gando64pA0SF6yD5_X9c6yHXPZa4ecfrqOV9ZQXtn8FoWCRROLVMyniJclsei5lSA1q9QnA2iK9UPCCrHBQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/haTouuUOdHBqsKszZOG9FzHxbEuz745nDJ0ffjUPluZlx-yJG9-ITRX3Yti3xzBgGSRpJW3PLymeKOP2NSZzn0X-F8VNvcaGSPJQmwWS3_KUQm7NZb2quzRNfGrf1BIEgcrOO1C6zMG469wT89QIZJZkcfx3R1hYGImOwa6tkmefRykb5K_UncOYcFwpO74CmKMb2as6-HcUV_7MZH4FfKI1V4oEqJh1j8hBsHJPxOiwepjVD_ZjFzFJ7z_E5o3u3FapEdc2ZvBaKoMp05KWIxDDZIQaJp7RPKMb3aobre_DI3TyJSE7o7H5icWjPbh6v5_4sJXxiXmpQ-P7pdTCEA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AlZi2p4-HZNBTTSlKHBnC6Z_LIHA6MYqIVsRTjtkRTBLyZdBs3YbfpuifxxljnhBuAEceEH3OmwGVQ4dz6mPOas4dvGxfgwEzLGlDeyCLF0O1L-dzmWUwGM31HyY5JfiBYC5HMLikQQrDsg9L9ldiWn829_XjIS26gL7EG9fkhcXKD50XoRs9Cd61yk4IWh-QKIc4kzfraDCTXOQOXkP5RdeTDr1pOhG6payNAiIqzukQgGEDbBRP1j8vaIqJhE8xE-X8ivy-V5Up_JvkavhWhlznZ2UqfSaDh2fgBpzPtgM3RQsQ1jNKRKvfLurPWeiZZ8jB3RRkv3izYZrHyUSMA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/R_QPT0NyWGmhEIDbdMKZF9Z4V4SMpTQsmcHJp3Y8IBneN2cSNd1IUh51yCCf4C6DIPi2sHjMBSyCEHbfBRL4qMes-QUOF9zztCoC1mybPHczDrvIqG5nuYOjzdjc8diLq4EnBbQpVodEouUgI23L3Dh8uhGm39E_W5taCji2hMI45Yh2ZNtJe2FSj9w_mJnNVuHT_qjCd4UUwz4DYUUGXfcq3ClIMMx56fnBkqj6YDk0UsVAcXaC_AsQ8zuKB9nFLtyEd8IFr_Pi4yM2UJeD-MVkUb2WdMGwwuToKweN0GqBjre45yGJZdoTdEsozb7SB5hVKsrfpY9OlY-FUMuvKA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کمیسر عالی حقوق بشر سازمان ملل اعلام کرد که از آغاز سال جاری میلادی تاکنون، دست‌کم ۴۰ نفر در ایران به اتهام‌های مرتبط با «امنیت ملی» اعدام شده‌اند که در میان آن‌ها ۱۸ معترض نیز دیده می‌شود.
ولکر تورک روز دوشنبه ۲۵ خرداد افزود: «مقامات دست به سرکوب شدید زده‌اند، هزاران نفر را بازداشت کرده و محدودیت‌های بیشتری بر فضای مدنی اعمال کرده‌اند».
او در بخش دیگری از اظهاراتش از اعلام توافق صلح میان ایالات متحده و ایران استقبال کرد و از همه طرف‌ها در منطقه خواست حداکثر خویشتنداری را رعایت کنند.
تورک گفت: «از اعلام این‌که ایالات متحده و ایران بر سر یک توافق صلح به تفاهم رسیده‌اند که شامل آتش‌بسی فوری و دائمی، بازگشایی تنگه هرمز و چارچوبی برای ادامه مذاکرات است، استقبال می‌کنم».
او افزود: «در این مقطع حساس، روشن است که همه طرف‌ها باید حداکثر خویشتنداری را به خرج دهند و برای اجرای سریع و با حسن نیت توافق حاصل‌شده تلاش کنند».
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 237K · <a href="https://t.me/VahidOnline/76366" target="_blank">📅 18:31 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76362">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/beda093be0.mp4?token=B3g5RKhueti4UmdML5eoQj01D1Ir9pPgDMwFQ1905IsOirBFGI3OlM3u1TXzpFZKF67iYkZk8Kew7V2xaKffg7iPZ778Nh-MoeHDhLih8qniEBB4wZLtXeptnCOGDJNeQOldX04OmLkvweWLZuFAke9-TxR5V0cTko391Xv8XEqaycHvz9LPtF5WmnpxbVfNhqoe6o_ziqe5VUIiOvC78m3w8XAolSTNR2micgnvXqlq6GBB6BKjmKN2EHuCfAkHZthPkk9ZJ9b2PKoDpFZDsy51xylRPUB02ZvsW7T6kDtMz6qv6caINj5n9A79_MWG60Ctv1EjwKJQ4ogDozvCtg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/beda093be0.mp4?token=B3g5RKhueti4UmdML5eoQj01D1Ir9pPgDMwFQ1905IsOirBFGI3OlM3u1TXzpFZKF67iYkZk8Kew7V2xaKffg7iPZ778Nh-MoeHDhLih8qniEBB4wZLtXeptnCOGDJNeQOldX04OmLkvweWLZuFAke9-TxR5V0cTko391Xv8XEqaycHvz9LPtF5WmnpxbVfNhqoe6o_ziqe5VUIiOvC78m3w8XAolSTNR2micgnvXqlq6GBB6BKjmKN2EHuCfAkHZthPkk9ZJ9b2PKoDpFZDsy51xylRPUB02ZvsW7T6kDtMz6qv6caINj5n9A79_MWG60Ctv1EjwKJQ4ogDozvCtg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 354K · <a href="https://t.me/VahidOnline/76362" target="_blank">📅 18:29 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76361">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DhC_ChfRXGVeyNs7u1VN_jR47tKGtJUzGGuXCDA5sENGJuCDlcZOt0vkybDeh0u_VUAhNiG6EbZbAUD7amSHuM6wC6442DQ9L1E7WSv_spGH94ynWeCoeewLeOfpu6rt4B8lFdSQMg5eE3eXCuVr6CuXEmdcDoFsarLBZFyteMcZcSqu9NQVw3q_cbE2pFRWRowpWG1ujw3iMGqWuzBswZ1dccvIdrZ-hEYRPvXKupq3S4u8-NQb_5txtw4YrCIgE6w8JpQks5euZMoZ0p_lROC0G_OyHjJ2kBxRs5CLBQL4PedstB1uVwtFT9aYs9EijmmrWc60xv7QmyDKuHYK6A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">به گفته دو مقام جمهوری اسلامی که نیویورک‌تایمز نام آنها را اعلام نکرده، تهران تا پس از عبور ساعت از نیمه‌شب به وقت محلی صبر کرد تا توافق را نهایی کند، زیرا نمی‌خواست این رویداد مهم با روز تولد دونالد ترامپ، رئیس‌جمهوری آمریکا، در روز یکشنبه هم‌زمان شود.
بر اساس این گزارش، اختلاف زمانی هفت‌ونیم ساعته میان تهران و واشینگتن باعث شد هر دو طرف بتوانند روایت مورد نظر خود را از زمان نهایی شدن توافق ارائه دهند. ترامپ گفته بود توافق در روز یکشنبه نهایی شده، در حالی که ایران اعلام کرده بود این روند در روزی بعد از آن تکمیل شده است. دونالد ترامپ ۱۴ ژوئن ۱۹۴۶ به دنیا آمده است.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 462K · <a href="https://t.me/VahidOnline/76361" target="_blank">📅 03:44 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76360">
<div class="tg-post-header">📌 پیام #22</div>
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
<div class="tg-footer">👁️ 414K · <a href="https://t.me/VahidOnline/76360" target="_blank">📅 03:18 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76359">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/129bb5a743.mp4?token=G27fPbzKiFUaO8yHWM_TSh2EkCnJ5rqhfOsTWp5sn-DIzkSv6rgSW7C76Y7gk31SwnRcClGr20U8F7U4fjVcj939Feg1Tvib4lLnpxsw9qeTfDKaC1cK4EaTZ3i4Qmq041iPUV2m4-2uER4GWgFOVjcL04bLKDrndOxAAMmR78eLD6q73yYyCZvDDjZH3CkK8KSWpF2P6V9xh78kuajj3JnDS3O3KQV82C634hiKE95qLx6UTpOekVzOQyRAftJilbglOoFCL7EwkpjcICCKgP85r2lUE4cLDc-tbPFEXSgJxC7x1novAGv1spNvE4LVLSO7TiYs_ZYJ99kGS7NzmQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/129bb5a743.mp4?token=G27fPbzKiFUaO8yHWM_TSh2EkCnJ5rqhfOsTWp5sn-DIzkSv6rgSW7C76Y7gk31SwnRcClGr20U8F7U4fjVcj939Feg1Tvib4lLnpxsw9qeTfDKaC1cK4EaTZ3i4Qmq041iPUV2m4-2uER4GWgFOVjcL04bLKDrndOxAAMmR78eLD6q73yYyCZvDDjZH3CkK8KSWpF2P6V9xh78kuajj3JnDS3O3KQV82C634hiKE95qLx6UTpOekVzOQyRAftJilbglOoFCL7EwkpjcICCKgP85r2lUE4cLDc-tbPFEXSgJxC7x1novAGv1spNvE4LVLSO7TiYs_ZYJ99kGS7NzmQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/n7f3IaLOVzq0zltYDCxV1c8MES1M-T-Q1YhvWwouEo_mMSztz2hIqigt1qmtWjFkS604eiHTg9fZtbdm2s-c6BwuDfaSL0f5hUGft9TaMQB2VbX2_097CvRjsfBeiFZpk6ehinKFihNz-mhAt3mSpc7V6nc1QY-k_OnLmQ57_X9qMBulVzUmwqU_9VTtWLQ8WyLd4iUy5wHki1MH36g4zOtjwul8-y-xJVwoQmTBCP_d1VneD9lYJsqJ5pEfSVIihfvvQgI0auqHMApFLnfwPtHfFdO0AiSEZ4hqPmmImrOWT4eiL0gfsewho9cN2B98tBNSGjytO2qbKZalt1Tugg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/uaB1IVh3fpUCPM9tLLMHqQ3AGBgk56NbgbDl4HPTIPXTpzwr5z6b5-SWTDLf9ofzwKRwOAhB_UjtCbvljEjSW0LdytFCaIqk-014__x6LYztrF8OsBxZM7a--s_wsWnJf84aK8T8APo3t6snLjAxLnooceBw5I5XR_S6RKTMeDkFF4QmzVqFWn-AYvidm7HsXOODYwL49ETRg1TENXpzhK7qDeuQBmW1Y-qc9xbDKCKW44IhvJZGKa1fHmwPWSIBoteMMUl3mP1wMEv0GrWtISUNb2rgvQSoEFQurHVaz3ZJgRtFjcMfl-HX7PlXNEE0KP2fwsk5C3lqpYUD26rDJA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/GOiEU4yDVbiTgqHHZv3QKRxI4QTxwaZMbXgoyhIC17z8qHTyTpHNxY8EjgAnYGTnTa-y1FffwqQcV2H4Kq7SgBiy9mvqU5W236OkK9Kq87F9Y6IJ1RI-6JXySiU4a_y1Rd-_8s0fAHtjAFm6db9xmrEK8IBqjXQ8jnBZYzb179G_Z1MYBw0QC5nE6RAR34cckQSd1DCwH74jVeI8GNOJKRtMuqOiLeD_zFAxnp29PZ6RQzMwOsSo_zhA5D2BOId4v6jWcsWrFGipmH8WrKLt_zVmARcIzjzhPwUCVNJEXPdyy6II1TsJggUhVAeghFOLhdW5ywl31i5nZ_4fRVMCcg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #18</div>
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
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/8a76f7084c.mp4?token=uMOJcv_Imr4WlaGRmt5r5yoA7jvjOW8x_OgTea-P1LDwUZaQ7nagsxI0dRroHlr0uho0OX6Eev744If4qO4nv4zhXAsGWT3Ub16kpBbw1aAGmvOZmTebJCl3NCZWQ7yUPIZScI4Mulu0ZWIFyVOdWsU_XYNlmMSmA2GdLkFesg5kDJKi_rH19ZkJtg22G2kbwOzy_QUO7t8NuI2eCwoQWBI96ZBspsuAph51cv1-efvPoYWsq8v68Ut3Dqpj0wf5qBwsOCTW9CFJ5_o7n-u01Eq91Bs5wodzk8Ai1jNwuO4UF4bK8SERqD08Ve8O55w9NUst1z8DvQmXVo4UTiOKOQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/8a76f7084c.mp4?token=uMOJcv_Imr4WlaGRmt5r5yoA7jvjOW8x_OgTea-P1LDwUZaQ7nagsxI0dRroHlr0uho0OX6Eev744If4qO4nv4zhXAsGWT3Ub16kpBbw1aAGmvOZmTebJCl3NCZWQ7yUPIZScI4Mulu0ZWIFyVOdWsU_XYNlmMSmA2GdLkFesg5kDJKi_rH19ZkJtg22G2kbwOzy_QUO7t8NuI2eCwoQWBI96ZBspsuAph51cv1-efvPoYWsq8v68Ut3Dqpj0wf5qBwsOCTW9CFJ5_o7n-u01Eq91Bs5wodzk8Ai1jNwuO4UF4bK8SERqD08Ve8O55w9NUst1z8DvQmXVo4UTiOKOQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Mi9s7RhssR8KFfvUTbgAkRD3xFueRsQIPHQpuYpNLR8uCag0Gr4aWS99wAWJqpVIkNIL5F6PDiBVsnRZRG8TmODeBZN2Krycd3dnQ6XCkMEseNdhOHQsfCD5tFwrGAveLAA8ZtTN9PYwdySzYtlFyxJH5dF1l0s--Xa5R1l0DbaSKswQaS9kwaOi5SgnjSuSapvdcllJUJ3sMSHUkCn8-1LciLkjqif281P1HYiWeLAPVGEXLe_T_jdZ8n5Uh9xd53Mrxve1Id36o1ANVtC48RZS5k867jmDJkoEkbsfuUNbHU6xT_Z1oX6dqCVkywVMtDfVNRGEN6dKKTGQwn26EA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/da696e6ada.mp4?token=ZksclkljObQNiCLNuKkpQD2rqr2NajSqHBOp-PmkhEV5llq0JW2u12CxjN2P5mJz5aoM_gLRSbgZ99WKDj03ZZfcoQtrAPQgpQSJyfE4HhyEmff6F2JxKD5t-n08GWgQIIR84osAaZ1lRpHtZTjIbt6ie-i1k1_OTPTXn6PeazByhf2Rxu3BhC0EAL-z8o_F3zDa0b1P7HG1VcAlbmPviaFZzHJnaVVztJwfbD5R1-OLWUB3Y_V2XAfj63t3z_tLZwtWmEpea8IfjLO8eAl-D_vDCQoCFo_kskILoollRK66M74KeCymfL4WlodrkLOS7JR0xqXu7gp4-tIV23Kvrg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/da696e6ada.mp4?token=ZksclkljObQNiCLNuKkpQD2rqr2NajSqHBOp-PmkhEV5llq0JW2u12CxjN2P5mJz5aoM_gLRSbgZ99WKDj03ZZfcoQtrAPQgpQSJyfE4HhyEmff6F2JxKD5t-n08GWgQIIR84osAaZ1lRpHtZTjIbt6ie-i1k1_OTPTXn6PeazByhf2Rxu3BhC0EAL-z8o_F3zDa0b1P7HG1VcAlbmPviaFZzHJnaVVztJwfbD5R1-OLWUB3Y_V2XAfj63t3z_tLZwtWmEpea8IfjLO8eAl-D_vDCQoCFo_kskILoollRK66M74KeCymfL4WlodrkLOS7JR0xqXu7gp4-tIV23Kvrg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 322K · <a href="https://t.me/VahidOnline/76352" target="_blank">📅 01:53 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76351">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/22e031404e.mp4?token=LuKGe952nM7tV9OcIRryG9XNovaHRoaGQ0Y-XZosg3fRdcEhyDd4tSrXLUugyt-8WxPkCLVvRaIWkgHSzLsYJEmvLnyDuEKDYZGchi6Z5VT-jFv-Ey78mnRoOwKIAOTPtj5IKgInT29Kseh4u_sLb6PM2wOpdFZsMVzjWrHdpf5C1FRRrvJtcRQqydhyLs5KqAUwQhF13zMjPcESAFG51jt6aqpt66MdRN0Bs5RCwUy0tyN1_zJYuXxeg0vQh-QKRuS1L6-xsbLauHPDZAie3vATBDp4b6yGTxZtLQmdUvWQ1Y_Tul0890wWVdxj_Q5ViHpcrZJy5MfzjkGNpHxROw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/22e031404e.mp4?token=LuKGe952nM7tV9OcIRryG9XNovaHRoaGQ0Y-XZosg3fRdcEhyDd4tSrXLUugyt-8WxPkCLVvRaIWkgHSzLsYJEmvLnyDuEKDYZGchi6Z5VT-jFv-Ey78mnRoOwKIAOTPtj5IKgInT29Kseh4u_sLb6PM2wOpdFZsMVzjWrHdpf5C1FRRrvJtcRQqydhyLs5KqAUwQhF13zMjPcESAFG51jt6aqpt66MdRN0Bs5RCwUy0tyN1_zJYuXxeg0vQh-QKRuS1L6-xsbLauHPDZAie3vATBDp4b6yGTxZtLQmdUvWQ1Y_Tul0890wWVdxj_Q5ViHpcrZJy5MfzjkGNpHxROw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اعلام خبر توافق و توقف جنگ در شبکه خبر
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 358K · <a href="https://t.me/VahidOnline/76351" target="_blank">📅 01:06 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76350">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/PJlP7gcgtNKW-dGlkf0HRuCo5hrbdjbTHD8Lpqy6vuYF--BzSVqzTXjn8d_u2BSC6R1--TBK9rHRPBpGDjMxD6YqOIfdEfjHK-WT2Kbsb2HBcSDE8WnoXN8wPSmFaGynjJM8Y-8EbYljABr1y69412_RyJbRkOB_hmCA_ylLlRMT9Ce4qyxJ2BRMOYo7br94Jm_AwdzEmY1trWEXY7yEE-o3eZ3FFfVkVhbqs8a2uYxw7TTGIbT227jTjWFEA-5Z_Hb6WBUa-FCsjG7aIumlAQyUXnf3UzNejiYlAlIPJ2ZqIF-Y_hgK259kWIbWaBU1t-IUHH3vo99vNOejrs09KQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">☄️
ترامپ: تبریک به همه، توافق نهایی شد
پست ترامپ ترجمه ماشین:
توافق با جمهوری اسلامی ایران اکنون کامل شده است. به همه تبریک می‌گویم!
بدین‌وسیله من به‌طور کامل اجازه بازگشایی بدون عوارض تنگه هرمز را صادر می‌کنم و هم‌زمان با این، مجوز برداشته شدن فوری محاصره دریایی ایالات متحده را صادر می‌کنم.
کشتی‌های جهان، موتورهای خود را روشن کنید. بگذارید نفت جریان پیدا کند!
رئیس‌جمهور دونالد جی. ترامپ
realDonaldTrump
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 377K · <a href="https://t.me/VahidOnline/76350" target="_blank">📅 01:02 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76349">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/M9iNV1zhWPTXvxUbTK5vmXBH_hH0If_CjIfJ86IWYLYcYbMkWTOSDRcK-jYgkMEC-ATWjbALcBQaV5GkXw-xRMP085Tnw9B_YURblydfSAeQVPx2RUSkubLthN2PzevEVqGhov4UiDxKMRyWi6dmNCAdcmps4l4G7pyeBoqJC1BLhOc-RU2onPJklJTbacUTjT3Dt3w9DsNCdzy4viDBUCeT--QyF1Fa1DTVgUi8ZIF53y5KMmuALYaUHQ6IEUTVgoIHldUoKc0-YLG-bb8MkBS4umDWeh14oV0Z5mdt7L9_nr_jgjvhl6BynMHy4U2kTK0ckLbVBSrzhNUtHAvmVw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شبکه خبر:
نخست‌وزیر پاکستان از دستیابی به توافق و پایان جنگ خبر داد
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 328K · <a href="https://t.me/VahidOnline/76349" target="_blank">📅 00:53 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76348">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/DqeuYEWuDRahayNPYDySUn1XbPNvqzCHjXIr5f8p5kB8tn0cM-nFWreqBOwl5rvSFxdDYPoLqmNpd7TDd7Q5yo76BG6_peBLRfBxP90IvWE9Cm_xDMCD-BrnIfFqRu8OK7QD1wu2A9BSDF4eFbjI3S2PKJaZWLF77bIc5ytItbJ-mpgrvD-QWbMpbgAXHP1yRHYEs6FOAQPVIqLIF5A8v7Qua9Q78yuJWBe5IYvfvLmy5soekGLPU9OVfYhjqELOxbiz_GO55gl-_V0j9cQp2FZ42pGzofH-jEDc7D5lxdIvXFv3ABoZit8h9G_0Y1HcnDqRQelFzcA2YqRRi_1GdA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">☄️
نخست‌وزیر پاکستان: توافق حاصل شد
مراسم امضا جمعه در سوئیس امضا می‌شود
پست شهباز شریف، ترجمه ماشین:
در پی مذاکرات فشرده، خوشحالیم اعلام کنیم که توافق صلح میان ایالات متحده آمریکا و جمهوری اسلامی ایران حاصل شده است. هر دو طرف پایان فوری و دائمی عملیات نظامی در همه جبهه‌ها، از جمله در لبنان، را اعلام کرده‌اند.
مراسم رسمی امضای توافق روز جمعه، ۱۹ ژوئن، [۲۹ خرداد] در سوئیس برگزار خواهد شد.
مایلیم از ایالات متحده آمریکا و جمهوری اسلامی ایران به‌خاطر تعهدشان به یافتن راه‌حلی دیپلماتیک برای این مناقشه تشکر کنیم. همچنین مایلیم قدردانی صمیمانه خود را از برادرانمان در این تلاش میانجی‌گرانه، رهبری بزرگ دولت قطر، به‌خاطر حمایتشان در دستیابی به این توافق ابراز کنیم. به‌ویژه از رهبری دوراندیش پادشاهی عربستان سعودی و جمهوری ترکیه نیز به‌خاطر مشارکت‌های عظیمشان در این زمینه تشکر می‌کنم.
اکنون که توافق برقرار شده است، میانجی‌ها مجموعه‌ای از نشست‌ها را در این هفته تسهیل خواهند کرد. این گفت‌وگوهای پیش از اجرا، زمینه را برای مذاکرات فنی و مراسم رسمی امضا فراهم خواهد کرد.
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 338K · <a href="https://t.me/VahidOnline/76348" target="_blank">📅 00:52 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76347">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/cb9bbe1383.mp4?token=I9PleFtLrNgpNJjMw2sZZv3dJvmklN3Zy5PMaqVYITLKj6_EDuq5kgCmNuJrkyEmu-opGOtZmAkl-BIKSrCgqeQ00UqqDDtvRhZtIn6o9PAqltXtOajgGMbm2VQHGcpnatMnp-1QhZnU_4I4Q3_K4vSe_IxfjbnCe-qRXr88v8jaiWcjhF5Tk2gV_EwnC5HpgtpwmY6y96jvqtdUBhGVhFSzzhl8cr5LhAzTJrG5plAma8CumprFiONjRm-fiKoqLyz51S4_MyVQ4ycm3La30DLGNBhA8AH75ty2hGQl8O4YkifhutFsnJYkSIi0Nr_ONBovCWZQHefqsIS6dRHwGg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/cb9bbe1383.mp4?token=I9PleFtLrNgpNJjMw2sZZv3dJvmklN3Zy5PMaqVYITLKj6_EDuq5kgCmNuJrkyEmu-opGOtZmAkl-BIKSrCgqeQ00UqqDDtvRhZtIn6o9PAqltXtOajgGMbm2VQHGcpnatMnp-1QhZnU_4I4Q3_K4vSe_IxfjbnCe-qRXr88v8jaiWcjhF5Tk2gV_EwnC5HpgtpwmY6y96jvqtdUBhGVhFSzzhl8cr5LhAzTJrG5plAma8CumprFiONjRm-fiKoqLyz51S4_MyVQ4ycm3La30DLGNBhA8AH75ty2hGQl8O4YkifhutFsnJYkSIi0Nr_ONBovCWZQHefqsIS6dRHwGg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدیوی منتشرشده در شبکه‌های اجتماعی نشان می‌دهد جمعی از حامیان تندروی جمهوری اسلامی کفن‌پوش شده و در تجمعی مقابل استانداری زنجان شعار «اگر چیزی امضا شه، مسئول باید کشته شه» سر دادند.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 295K · <a href="https://t.me/VahidOnline/76347" target="_blank">📅 00:44 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76346">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/BByjkmsuSHQvd8IfBuQODe1lO7mIFT6c2JPFTDRjpqFt9R6SAJEKad-LC0ATnxwZJk3TgURqZNOJpXcxCE2JHLOOHdTs1QqqyqqCyO-cnyvTDfuiKnWwiK2IqhBG5cAIaFEf5vpICRQ_Ft8u6WRw7eobVaTTLvdOiOelQ8WvHfn3UH0TPuRI1qwZ5JVrnsS1cnMkFTtcUDBFDmXUxzb7iacpEeSFqhJ8XHx_fdpitF2OIbH5dDhcyHoAdTklkIVP77LL-eh7qa2PEV_wTKd17PIrZDJ7Zv8ZTklAKYNkoKDkH5X1zIPnqpoWOfR2RIc6iWhb-U_uX_H7Zmt1hf937g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دونالد ترامپ، رییس‌جمهوری آمریکا، در گفت‌وگو با
وال استریت ژورنال
گفت توافق با جمهوری اسلامی قریب‌الوقوع است، اما تهران هنوز موافقت خود با آن را تایید نکرده است.
ترامپ افزود قصد دارد به‌زودی بیانیه‌ای صادر کند که در آن اعلام خواهد شد آمریکا با جمهوری اسلامی به توافق رسیده است.
او گفت این توافق، در صورت نهایی شدن، یا توسط خود او یا از سوی جی‌دی ونس، معاون رییس‌جمهوری آمریکا، به‌صورت الکترونیکی امضا خواهد شد.
رییس‌جمهوری آمریکا روز یکشنبه این توافق را گامی بزرگ در مسیر پایان دادن به درگیری نزدیک به چهارماهه توصیف کرد.
ترامپ همچنین گفت این توافق شامل تعهد جمهوری اسلامی به دست نیافتن به سلاح هسته‌ای و بازگشایی فوری تنگه هرمز خواهد بود. او افزود عجله‌ای برای خارج کردن مواد هسته‌ای از ایران وجود ندارد و این موضوع می‌تواند در مرحله‌ای بعدی دنبال شود.
ترامپ گفت: «بعدا و زمانی که آماده باشیم وارد عمل شویم، مواد هسته‌ای را جمع‌آوری خواهیم کرد. به نظرم طی یک یا دو ماه آینده این کار انجام می‌شود و عجله‌ای وجود ندارد.»
@
VahidOOnLine
نقل خبرگزاری فارس:
ترامپ: به‌زودی بیانیه‌ای صادر خواهم کرد که تایید می‌کند آمریکا با توافق با ایران موافقت کرده است
🔹
این توافق به‌صورت الکترونیکی، یا توسط من یا توسط معاونم ونس امضا خواهد شد.
🔹
توافق شامل تعهد ایران به عدم دستیابی به سلاح هسته‌ای و بازگشایی فوری تنگه هرمز خواهد بود.
🔹
ایران هنوز موافقت خود با این توافق را تایید نکرده است.
🔹
هر زمان که آماده باشیم، مواد هسته‌ای را تحویل خواهیم گرفت و این اتفاق ظرف یک یا دو ماه آینده رخ خواهد داد.
🔹
من خواهان پایان یافتن حملات هستم و ایرانی‌ها هم می‌خواهند که جنگ تمام شود.
🔹
من هیچ‌وقت به دنبال تغییر رژیم ایران نبوده‌ام.
🔹
بازرسی‌های بسیار دقیق و شدیدی از ایرانی‌ها به عمل خواهد آمد.
🔹
در این توافق پولی به ایران داده نخواهد شد، اما احتمالاً تحریم‌ها لغو می‌شوند؛ باید ببینیم در عمل چگونه رفتار خواهند کرد.
🔹
محاصره دریایی اعمال‌شده علیه ایران موفقیت‌آمیز بوده و تاثیر آن از حملات نظامی هم بیشتر است.
🔹
نتانیاهو از این توافق حمایت می‌کند؛ این توافق برای او خوب است چون تحت هیچ شرایطی اجازه نمی‌دهد ایران به سلاح هسته‌ای دست پیدا کند.
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 320K · <a href="https://t.me/VahidOnline/76346" target="_blank">📅 00:41 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76345">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/OjnFx6K5yi0I363Y0jLAhT16v_rAxcpe1rWT4kYxSAwWOuqg98jpfUYsOg704EMi_UOxwzHp24G6Sq0HsK5-eTMy-RmrpJ7vtGvbNpuka-6uXJ7SilSbInj5DwokEPiDfvVrFXfGFXwpRJAhWilJUs1q_RHcZZdPsXHC5W_TuQ4knVPvhGOyBKd2tnzOf4KXh0cm778kbASttwVo5tzScOigJs_rDgqRMjmxBaiBvUoyKQRixUcvfGehFJLIQNEj7ojQlFI-z_A3cugAVB1hptrNa6srfeFfDSJ3hsz7j_ofCdUYGYmaN1ISQaHN2vGGkZI9hYcOBkvQ2fpBp7CG-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">به گزارش «کانال ۱۲» اسرائیل، بنیامین نتانیاهو و دونالد ترامپ لحظاتی پیش به صورت تلفنی گفتگو کردند و رئیس‌جمهوری آمریکا، نخست‌وزیر اسرائیل را در جریان «پیشرفت‌های کلیدی برای امضای توافق با ایران» قرار داد.
مقامی ارشد اعلام کرده که احتمال امضای این توافق «حتی طی همین امشب» (بامداد دوشنبه به وقت تهران) وجود دارد.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 340K · <a href="https://t.me/VahidOnline/76345" target="_blank">📅 00:13 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76344">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">پست‌های ترامپ، ترجمه ماشین:
سناتور جک رید، یک «دموکرات» از رود آیلند، وقتی گفت توافقی که ما همین حالا انجام دادیم به خوبی فاجعه اوباما، معروف به برجام، نیست، دروغ گفت.
رید یا یک کلاهبردار تمام‌عیار است یا بی‌کفایت.
توافق اوباما مسیری به سوی سلاح هسته‌ای برای ایران بود، همراه با پول نقد و همه چیز؛ یکی از بدترین و احمقانه‌ترین توافق‌هایی که آمریکا تا به حال انجام داده است؛ به همین دلیل هم می‌گویم «دموکرات‌های احمق»!
توافق ما دیواری در برابر دستیابی ایران به سلاح هسته‌ای است؛ درست نقطه مقابل اوباما.
جک رید را استیضاح کنید!
(توضیح ماشین: در متن اصلی چند غلط املایی عمدی هست: Dumocrats به‌جای Democrats برای تحقیر دموکرات‌ها و Obuma به‌جای Obama.)
realDonaldTrum
ویکتوریا کوتس از بنیاد هریتیج واقعاً فوق‌العاده است! او موضوع را مثل تعداد کمی از دیگران می‌فهمد. متشکرم ویکتوریا.
ایران هرگز سلاح هسته‌ای نخواهد داشت و تنگه هرمز هم به‌زودی برای تجارت باز خواهد شد!!!
رئیس‌جمهور دی‌جی‌تی
realDonaldTrump
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 354K · <a href="https://t.me/VahidOnline/76344" target="_blank">📅 00:10 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76343">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/nbfOtwcL6CdBkfZvCcaiYN9gleL5mRBu0CWRxxS7PyuekkamHvM7lhRoBH1pkSjunuoYJKtHEy3R9Wf4svu0MRgeznFecmltQR0e1SmjE1VFnckTUUXgc6LBeB36YzrXAuxjDyej3bNKtfdZqwHcNDpFutefLjkznGodb6eCdJbYG_84WlU7ig9yDhtmKf2meXbmI3eBp_ComJNXS1DT7-9hxy-7iOHft3t7-CBybZm4q9ZbjaTUZP44HYoZ4rakfGZm2Xi3Dk4qqbTDU4C6MScDuTravx17zwaqFtBqTSFZb7vK5xf4bVDSW3MXcwXuu5ulEPW7SHCzXpedz4XK2w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">محمدباقر قالیباف، رییس مجلس جمهوری اسلامی، در واکنش به حمله اسرائیل به اهدافی در جنوب بیروت در
شبکه ایکس
نوشت: «مجاهدت‌های رزمندگان لبنان و دیپلماسی مقتدرانه جمهوری اسلامی حاکمیت و تمامیت ارضی لبنان را تضمین می‌کند و بساط دیوانه‌بازی و جنگ‌افروزی اسرائیل را بر هم خواهد زد، بچرخ تا بچرخیم.»
قالیباف تاکید کرد که هیچ‌یک از ارکان مقاومت را نمی‌توان «تک و تنها» قرار داد و حاکمیت و تمامیت ارضی لبنان حفظ خواهد شد.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 372K · <a href="https://t.me/VahidOnline/76343" target="_blank">📅 22:39 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76342">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ram-Iyka5A-ykf3f80koyXMbBWiqB_cpi8wskQf91ZcpSWfiHtUTi56e1gdC_RYoMZFrJUFy2DQ8b-1cC36ceYBACTY40_5HMTSTaWrBNCoPIOJPXjgQXA7niFEG7QeTJmtjRJiB43StOmiyW3l3enfxHjzOG-gy5nOBX5B3bxp053KGY1B2f2yS1-vxPPsG90qH7hK2-XNQWipxshn8S1peBfsoW1xPYGZI9FcWx_Q5gI9Kz4qSV_Se05cCBnviPI8zizntd56R7TwYhXajHZePTSRmnvP0BVoVtoOOmGzR21mQuulDg20pBYYGOSngoHyY7jhTZuaI1bcGaTnAig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرگزاری تسنیم و صدا و سیما:
پروازهای فرودگاه‌های غرب کشور تا اطلاع ثانوی لغو شده است.
این تصمیم در پی شرایط موجود اتخاذ شده است.
سازمان هواپیمایی تا این لحظه هیچ نوتامی منتشر نکرده است.
خبرگزاری مهر:
هیچ نوتام جدیدی درباره محدودیت پروازی صادر نشده است
🔺
مجید اخوان، سخنگوی سازمان هواپیمایی کشوری در گفتگو با خبرنگار مهر درباره برخی اخبار منتشرشده در فضای مجازی مبنی بر صدور نوتام جدید برای محدودیت پروازی در فضای هوایی کشور، اظهار کرد: هیچ‌گونه نوتام جدیدی در این خصوص صادر نشده است.
🔺
نوتام مربوط به محدودیت پروازی در غرب کشور، همان نوتام قبلی است و اطلاعیه جدیدی در این زمینه صادر نشده است.
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 388K · <a href="https://t.me/VahidOnline/76342" target="_blank">📅 22:23 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76341">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/201a6972d8.mp4?token=Mk8L--wqH0rffy5IT9REo_6M0JFIVeohR0oHfKNfbUgiWCJRHrvMPoO5k7wRwfE7DjlRniyQCi93WA5hVGrQ7228G6El35KyQaTkv5d7O1LVmkT67gkoJQqmSrZVBwTPUB02YcwylO-M0h837BgnmIGZ_cR0SIdiwNiwkAZwIp2xPbASKM8BGbLtXzgZJ38PnPI7JMp9X2ffqhJwNRTjOGvCZ5gnYk6NMpi92KSLwK0H-DHCRkkfem0TpV4AuTiUExGnaYKf5R3_SFwcZye2_y3NaCzQ3gzW3Q89dMr6yEwL-Hg0WuxyIZTRc6c-E5x4JyFTQlbeW3jC7cB8fS4ZKA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/201a6972d8.mp4?token=Mk8L--wqH0rffy5IT9REo_6M0JFIVeohR0oHfKNfbUgiWCJRHrvMPoO5k7wRwfE7DjlRniyQCi93WA5hVGrQ7228G6El35KyQaTkv5d7O1LVmkT67gkoJQqmSrZVBwTPUB02YcwylO-M0h837BgnmIGZ_cR0SIdiwNiwkAZwIp2xPbASKM8BGbLtXzgZJ38PnPI7JMp9X2ffqhJwNRTjOGvCZ5gnYk6NMpi92KSLwK0H-DHCRkkfem0TpV4AuTiUExGnaYKf5R3_SFwcZye2_y3NaCzQ3gzW3Q89dMr6yEwL-Hg0WuxyIZTRc6c-E5x4JyFTQlbeW3jC7cB8fS4ZKA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شماری از حامیان جمهوری اسلامی و مخالفان توافق با ایالات متحده، در تجمع خود با سر دادن شعار خواهان اعدام عباس عراقچی، وزیر خارجه حکومت ایران شدند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 384K · <a href="https://t.me/VahidOnline/76341" target="_blank">📅 21:16 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76340">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/nASc3b6tpQr7LC5pg43-8krORn5iKLrzCDwrZmGOKjV2ohVQ_DUak-kq_F9hlS1KmF6286B7LItmigmYHDc8nZCgRi-nLxzXtyBczyMRkgYxI4rtU7BWQ2melBAy5gYqQmA-ROfjL-2XP80PYM9fiv4hcnbVTDoXx5wtnadtJHUSmu8DUJxvlYEKXzDHdxa2TC-pb3_6qzZI5rZ-We_Rsbz591Z3GSrRjnCfggK_B8Is1Occl9IU4j5efQp0wnWRsHNkcl1KdfXkJj12hkfP33QqlyWu4j-8B1oKZyYdNzuGxxHQ2TMnIdsUOpqOLOOQ7BpQHdCDIj2cT8b5JorAww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">"‏پاسخ رزمندگان اسلام در پیش است."
محمدباقر ذوالقدر، دبیر شورای عالی امنیت ملی در جمهوری اسلامی
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 380K · <a href="https://t.me/VahidOnline/76340" target="_blank">📅 21:10 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76339">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Iansmh686wKrT31o6AW9Z4rabwSZnquaboeswkHv3FhpbLr6CbF0PwPZlNm4DBoPog_X4CdtvIYZqwm7BXq_qVitQU8XgO-va1rXhwIYoXj1NYzowdZFF85DAnqgYdAx3XfP6ah7dolxuGr-yHgqgz5beLw4XtQq6Jj14Y0jYuZM5iWyz91MI8Vf04K7X_JEcQA2TSQdo-bTQZe3ALj9Ez_kEtYjksHvoCMyP3BWNw4o3C-0bh1AA4K-akCzkaNLjpwGG6SYGqMzq54kOT70WtO5VPzuGSc5eGoLUe2KtGAfTGheail8xKZzpYweB5FxoRN6RDnJG1JpqWocJwXxlg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نصب تصاویر #مجتبی خامنه‌ای و آدولف #هیتلر با هم عکس جعلی چهره رهبر جدید جمهوری اسلامی (دستکاری شده با هوش مصنوعی) رو با استناد و افتخار به سخنان جعلی و چرندیات هرگز گفته نشده آن جنایتکار دیگر منتشر می‌کنند. عکس دریافتی از بابلسر، سه‌شنبه ۴ فروردین Vahid
📡
…</div>
<div class="tg-footer">👁️ 371K · <a href="https://t.me/VahidOnline/76339" target="_blank">📅 20:58 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76338">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YhcC5Pavwo7lxvGD-YtE75LGU3AxCiXxuJFyxOdoWmlR3zFXuYD4JOMP1b1CCOpTgONhEyn2BjKjBiwozR4Pmow8_8onOez9OD0ui7agr13b-lkNOklwS5IV4P2NuTB4B47zSyA89c3ZlGNEGvCN1NHUD3BjVRDBaUHfOJ9EV6LoJwN1WG6h5iLJBY4NSuqyw8WQUkDj1UaLZyFh2Zfv0z5pr1duJplBKQ4xI8Eiob7VIGhusfJwtKM6dhzUI8qtANUoemrkanyB9C-jt4r8hh0MU2ceq7noepskhmc2tb34MndKzjFqiSibdM-cxuiuOx3DDwqotRhSTCWg5y6G8Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مسعود پزشکیان، رئیس‌جمهور ایران، در پی انتقادات برخی حامیان حکومت از محتوای توافق احتمالی با آمریکا، روز یکشنبه گفت که روند مذاکرات بر اساس مصوبات شورای عالی امنیت ملی و دیدگاه‌های رهبر جمهوری اسلامی پیش می‌رود.
او در دیدار با مدیران رسانه‌های داخلی افزود: «تصمیمات راهبردی کشور باید در چارچوب سازوکارهای قانونی اتخاذ شود و همه جریان‌ها و گروه‌ها نیز خود را ملزم به تبعیت از این تصمیمات بدانند.»
در آستانهٔ امضای تفاهم‌نامهٔ ایران و آمریکا برای پایان جنگ، اعتراض‌ در میان حامیان تندروی حکومت به متنی که به‌عنوان تفاهم‌نامه در برخی رسانه‌ها منتشر شد بالا گرفته و تجمعاتی نیز توسط گروهی از طرفداران جمهوری اسلامی علیه این تفاهم و مذاکره‌کنندگان برگزار شده است.
در یکی از این تجمعات در تهران، تجمع‌کنندگان علیه عباس عراقچی، وزیر خارجه، و محمدباقر قالیباف، رئیس مجلس شورای اسلامی، شعارهایی سر دادند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 361K · <a href="https://t.me/VahidOnline/76338" target="_blank">📅 20:05 · 24 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>

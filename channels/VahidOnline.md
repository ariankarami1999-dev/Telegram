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
<img src="https://cdn1.telesco.pe/file/a0ULoZ2nX5qitCgeFM3ShDqbZrxcwohOPIn5ZnCF_ByX3qZXXI8XgE_xI-hRSNp55PksLAHTcokCzbmPb9TtV314_Q7EzvQjjyWynxnUaGXERGJzk7ZxFY2tCiJ97WZVVVA45ERd_I_7cWUapW15CAliRpV97-Yvfo99_-jkLkIjEZUmewr2tp0tBJ9b2mM-NMk4d9jKjuxEaqNxgTrHCjDBQTPZQlsJQmJV6E6r5SP4rXUo2QzAhUuCGDsccPKwizYM2sYsKChQeCI_33O5xyMEhH6eQeA3I2ExMkBEX-A0D33-1LVnhBme4C0bhCZBDgEAWSYZhTBPFnpTge06Mw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Vahid Online وحید آنلاین</h1>
<p>@VahidOnline • 👥 1.34M عضو</p>
<a href="https://t.me/VahidOnline" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ارسال پیام:@Vahid_Onlineinstagram.com/vahidonlineتلاش می‌کنم بدونم چه خبره و چی میگن. اینجا بعضی ازچیزهایی که می‌خواستم ببینم رو همونجوری که می‌خواستم بهم نشون داده بشه می‌گذارم.استوار بر حمایت‌های مردمی:ماهانهvhdo.nl/patreonیک‌بارهvhdo.nl/paypal</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-19 13:59:26</div>
<hr>

<div class="tg-post" id="msg-76091">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/PrfAT11O5ozS61N8kEYAHnvDNbIxv_-hKesRf-KQHxgAFprPI4wwllULLB9-iMCHiDMvgJ-8ndyyerbNkhPiimmYWaMUBNauiqIdbpENsh91X_8QiAoFMfFxtFIpCvr61B31pHoT_cQZUaSKuMlg6CEqJhgBE658r32FOCLL1v0c_5UceMk09MMDWVHr03UF6-Oj6jZJeR5idhLCFjodZwMzoLiS6pvFscO1Vb0dctoe4QtTDfJt5ZBHYkVa5a6yE9XQjP3e2LevNMjb5Rz9FzK0Iy8ULFMIdd0PPTQ7cpn3VVDjJkpsGgvTdjywfKpHPaAamf1ptP6ma0YBQvY5eg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جی دی ونس، معاون ترامپ، در مصاحبه با فاکس‌نیوز ابراز اطمینان کرد آمریکا و جمهوری اسلامی می‌توانند درباره پرونده هسته‌ای به یک توافق بلندمدت برسند.
او گفت صرف‌نظر از اینکه اسرائیل از این موضوع خوشش بیاید یا نه، چنین توافقی به نفع آمریکا است و واشینگتن به پیگیری آن ادامه می‌دهد.
ونس با اشاره به نگرانی درباره اینکه تهران ممکن است در حال بازی دادن واشینگتن باشد، گفت: یکی از مهم‌ترین عوامل موفقیت این توافق نهایی این نیست که جمهوری اسلامی چه چیزی روی کاغذ می‌نویسد، بلکه این است که آیا واقعا به برخی از الزامات توافقی که به آن می‌رسیم پایبند می‌ماند یا نه.
او با تاکید بر اینکه آمریکا تعهد جمهوری اسلامی به چنین توافقی را در بلندمدت راستی‌آزمایی خواهد کرد، گفت
:
بیایید صادق باشیم. ایرانی‌ها نمی‌خواهند این جنگ ادامه پیدا کند. ادامه جنگ به نفع آن‌ها نیست. آن‌ها پای میز مذاکره آمده‌اند و پیشنهادهای واقعی را مطرح می‌کنند. اگر به این توافق برسیم، یک موفقیت بزرگ برای مردم آمریکا خواهد بود.
@
VahidOOnLine
جی دی ونس در گفتگو با شبکه فاکس نیوز: موضع رییس‌جمهوری کاملا روشن بوده است. اسرائیل اهداف خاص خود را دارد، اما هدف اصلی آمریکا در قبال ایران این است که اطمینان حاصل شود ایران به سلاح هسته‌ای دست پیدا نمی‌کند
جی دی ونس: در ماه‌های گذشته و در واقع طی حدود یک سال و نیم اخیر، شرایطی ایجاد شده که رییس‌جمهوری معتقد است ــ و من هم فکر می‌کنم درست می‌گوید ــ می‌توان به یک راه‌حل بلندمدت برای مسئله هسته‌ای ایران دست یافت
ونس: ممکن است اسرائیل از چنین توافقی خوشش بیاید یا خوشش نیاید، اما ما معتقدیم این مسیر به نفع ایالات متحده آمریکا است.
به همین دلیل به دنبال آن خواهیم رفت، زیرا این همان چیزی است که رییس‌جمهوری آمریکا برای انجام آن انتخاب شده و همان کاری است که برای خدمت به مردم آمریکا باید انجام دهیم
IranIntlbrk
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 284K · <a href="https://t.me/VahidOnline/76091" target="_blank">📅 06:35 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76090">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aZML2JARgSRvjm68olzvzzRD2wS0e5Ul8OlP5rxtpJ-ddwe73bQROOMDO7XqtDGIwMlOePG3YwRxfF3Ldjb-llFxh1xUoLRxXLd_0qTY7K6Hz3_1524UWgbECrvvu5bjcuLQ2SvW3Q-hpFcJiMVkhKubsb4I-836nklFuU1t6VCpoBHMfOYbQo2nSUnQMo7kZlJ5VE2TU7cL2IJaBuULQct6BOSGNhD0HwWME9JumvWSxOTbgI3OmCgnAIZLrxgVPU1QBxYA3YouvSP2g54q4aCTJ_iqLR9EQjIVnaUmYbuhSbliTyY_lawMWDv0LZCXo4DY9ooKXEhPm3i7OlhFgQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دونالد ترامپ، رئیس‌جمهوری ایالات متحده، روز دوشنبه با تاکید بر موضع سرسختانه واشنگتن در قبال برنامه‌های هسته‌ای تهران، با تقدیر از همراهی لیندزی گراهام، سناتور برجسته آمریکایی گفت:
«لیندزی در تمام این مسیر پابه‌پای من جنگیده و ما تیم بسیار سرسختی بوده‌ایم. من فکر می‌کنم در حال پیروز شدن در این نبرد هستیم، اما طی دو هفته آینده با اعلام پیروزی کامل، برنده واقعی آن خواهیم شد. این یک پیروزی کامل خواهد بود که بسیار زود رخ خواهد داد.»
رئیس‌جمهوری آمریکا در ادامه با اشاره به نابودی گسترده زیرساخت‌های نظامی ایران، این وضعیت را مصداق تحقق «صلح از طریق اقتدار» دانست و خاطرنشان کرد:
«ما در حال حاضر مشغول مذاکره هستیم و آن‌ها به شدت می‌خواهند یک توافق بسیار خوب انجام دهند. آن‌ها اکنون حاضرند همه‌چیز را به ما واگذار کنند و توافق کنند که ایران هیچ سلاح هسته‌ای نداشته باشد.»
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 318K · <a href="https://t.me/VahidOnline/76090" target="_blank">📅 02:43 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76089">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sooMTPCcYTo7nTyBCvdtgC9uI0smz-3LMGAo53OQyzibkDc-4rCmLJMSzBivjsmWnounNX5TKD4PxOtoQdDC7emhPF_Cw-e1TDoGPEIy8c89YU7QU4EfB92S6dslx6las-ayaWT8xSD-l4x2W95RGHN8-rLdEpw1rGUgSucCS3rvzHZvOHOzIlGY6QoneX8y7ZWePPVBGgQBMPzFfQU8wSAOYwZqQXYqWFmxu7aVhT-NdgKDEqxaNqzGRYuVU3XWaFCLZnZ4bI1OysWDQPdc1QC78BwLWAC9atNVk_mZ3uOa95pF2EGPk5rgkriCFVgvEXj0SF4eOU1O4Z1p4b2gVw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اسماعیل قاآنی، فرمانده نیروی قدس سپاه پاسداران در اظهاراتی جدید به حمله موشکی شب گذشته از خاک یمن به سوی اسرائیل واکنش نشان داده و آن را نشانه‌ای آنچه «هوشمندی جبهه مقاومت» خوانده، دانسته است.
آقای قاآنی روز دوشنبه گفت: «اقدام به موقع و با اقتدار یمن قهرمان نشان از هوشمندی جبهه مقاومت دارد اگر لازم شد دیگران نیز می‌آیند. شرارت‌های رژیم صهیونی و آمریکا در این منطقه عکس‌العمل جبهه متحد مقاومت را در پی خواهد داشت. رزمندگان بدون مرز مشرف برگلوگاههای عبور شما هستند به تعرض ادامه دهید گلوی شما را خواهند گرفت.»
یکشنبه شب ارتش اسرائیل اعلام کرد که پرتاب یک موشک از خاک یمن به سوی اسرائیل را رصد کرده و کمی بعد از رهگیری آن خبر داد.
کمی بعد حوثی‌های یمن حمله به اسرائیل را تایید کردند و گفتند که «منطقه اشغالی یافا» را هدف قرار داده‌اند.
حوثی‌ها همچنین در بیانیه‌ای «ممنوعیت کامل و مطلق» تردد دریایی اسرائیل در دریای سرخ را اعلام کردند:
«ما در قبال محاصره ناعادلانه تحمیل‌شده بر مردم خود و مردم محور جهاد و مقاومت در فلسطین، غزه، ایران، لبنان و عراق ساکت نخواهیم نشست.»
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 311K · <a href="https://t.me/VahidOnline/76089" target="_blank">📅 02:14 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76088">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/cf7a40e8ba.mp4?token=A3rBuOwRiOqjBHpEQGTEP2m-aLGLXLXfEDClE17Lz3b1vogyQUDUwxZz-PzIs3thf9u0MUSFL0-1njuqyu5QI89aL7VNVNT2mx9lIzKzgZLH68xyrhGTTQqQx7r_0fzC2Ao0mdtGPYVm7u685IOztkkGleU-y-en-zerMPiWknygowWVS7XTeemMmqnoSdIpnLJbfqI4_f2j4Wng_GCjLBunctuY7h5-UrPR3J33rXwVvL03dXgOyWpgkKrrB-DhjAqanJap69mo9tjXFmaPy-gWmhkTM5VvcvzTqmVlrQrVd__07-ioApI-kVXiqqwo0kqU4o_luPqkxNIcqn9o8w" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/cf7a40e8ba.mp4?token=A3rBuOwRiOqjBHpEQGTEP2m-aLGLXLXfEDClE17Lz3b1vogyQUDUwxZz-PzIs3thf9u0MUSFL0-1njuqyu5QI89aL7VNVNT2mx9lIzKzgZLH68xyrhGTTQqQx7r_0fzC2Ao0mdtGPYVm7u685IOztkkGleU-y-en-zerMPiWknygowWVS7XTeemMmqnoSdIpnLJbfqI4_f2j4Wng_GCjLBunctuY7h5-UrPR3J33rXwVvL03dXgOyWpgkKrrB-DhjAqanJap69mo9tjXFmaPy-gWmhkTM5VvcvzTqmVlrQrVd__07-ioApI-kVXiqqwo0kqU4o_luPqkxNIcqn9o8w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">کارشناسی حکومتی در صداوسیمای جمهوری اسلامی مدعی شد آمریکا در جنگ ۴۰روزه بیش از ۷ تا ۸ هزار زخمی و دست‌کم هزار کشته داشته است.
او گفت: «برای ما کشته گرفتن از آمریکایی‌ها و اسرائیلی‌ها هیچ کاری ندارد» و افزود جمهوری اسلامی به درخواست «عالمانه و عاجزانه» کشورهای منطقه خویشتن‌داری کرده است.
پیش‌تر، دونالد ترامپ، ریس‌جمهوری آمریکا، چهارم خرداد در مراسم «روز یادبود»، یاد ۱۳ نظامی آمریکایی کشته‌شده در جریان جنگ ایران را گرامی داشت و گفت آن‌ها جان خود را فدا کردند تا اطمینان حاصل شود که ایران «هرگز به سلاح هسته‌ای دست نخواهد یافت.»
@
VahidOOnLine
"روایت فتح"
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 324K · <a href="https://t.me/VahidOnline/76088" target="_blank">📅 01:03 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76087">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">زمین‌لرزه در هرمزگان
پیام‌های دریافتی:
سلام وحید جان
زلزله همین الان بندر عباس ساعت ۱۲:۴۰
آقا وحید بندرعباس همین الان زلزله اومد
قشنگ زمین لرزید
00.39 بندرعباس زلزله شد
زمین لرزه نسبتا شدید ساعت ٣٩ دقیقه بامداد بندرعباس
داداش همین الان بندرعباس زلزله‌ اومد
🔄
آپدیت:
‌
خبرگزاری فارس: زلزله‌ای به بزرگی ۵ و در عمق ۲۲ کیلومتری زمین، منطقۀ سرگزی احمدی در شمال هرمزگان را لرزاند.
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 330K · <a href="https://t.me/VahidOnline/76087" target="_blank">📅 00:42 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76086">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/d82nhegdaOnYSCL5ROa2KPeynhPaWIjxmAkHuwcG8cnPHAXPSs40k_6w2zLK1HWHWGjGOX4HIyvQual9XUtBYc8Ju-M3OAFB3r8op-nwck1xg3oUGSud9G6he2Akntghoku9301r83PzaSf_NSevgL2YZ8aMVlC2NwGM4YxUb5KBQzJ2BWsuKAFQ48uQgxIc-Imc-D2PJTSMAQv58kI8PyQreicP8hlIaMgzFKO-NYzX1l8xAZghhdQsNNUDn7olSw5am9gZ3CIDqB08ER4dieq-uquIs0cVbBJOoTIAOTi0PEFRC-Xez33-MA0QikU5BA71YjYmluTpnqjPmnMA2w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‌سارا اسمیت، سردبیر بخش آمریکای شمالی بی‌بی‌سی، در یک تماس تلفنی کوتاه با دونالد ترامپ درباره گفت و گوی تلفنی روز گذشته او با بنیامین نتانیاهو، نخست وزیر اسرائیل، پرسید.
وقتی از آقای ترامپ سؤال شد که آیا نتانیاهو با حمله موشکی به ایران در روز یکشنبه از درخواست او سرپیچی کرده است، رئیس‌جمهور آمریکا این موضوع را رد کرد و گفت: «نه، نه. موشک‌ها از قبل شلیک شده بودند. آن‌ها از قبل در راه بودند.»
او سپس افزود: «اگر به او بگویم کاری انجام دهد، انجام می‌دهد.»
این تماس کمتر از یک دقیقه طول کشید.
در بخش دیگری، سارا اسمیت از آقای ترامپ پرسید که برای متوقف کردن حملات اسرائیل به ایران به نتانیاهو چه گفته است.
«تنها چیزی که گفتم این بود که باید از عقل و منطق استفاده کنیم. ما به امضای یک توافق بسیار قدرتمند و بسیار خوب نزدیک هستیم. بدون سلاح هسته‌ای، بدون هیچ چیز دیگر.»
او ادامه داد: «می‌دانید، باید از مقدار زیادی عقل سلیم استفاده کنیم. همه چیز خوب بود.»
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 323K · <a href="https://t.me/VahidOnline/76086" target="_blank">📅 00:26 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76085">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">پیام‌های دریافتی تایید نشده:
وحید جان گیشا یه جارو زدن یه انفجار وحشتناک بود
[از روی صدای یک انفجار چطور میشه تشخیص داد که دلیلش حمله بوده یا چی؟]
وحید جان ۱۲ و ۱ دقیقه صدای انفجار خیلی خیلیییی بزرگ
گیشا
سلام از گیشا
یه صدای خیلی بلند انفجار اومد
همین ده دقیقه پیش
همه ی همسایه ها اومدن دم پنجره
نمی‌دونم چی بود خیلی عجیب بود
همه جا لرزید
📡
@VahidOnline
۲۰ دقیقه صبر کردم ولی پیام‌های زیادی دریافت نکردم.
آپدیت:
ما وسط گیشاییم و خونه هم ساکته، کوچیکترین صدایی نیومده
وحید جان راست میگن دقیقا ۱۲ و یک دقیقه در گیشا صدای انفجار بزرگ اومد،اما فقط یکی و واقعا نمیدونم چی بود، ضمنا برخورد به زمین و یا عمیق نبود.
من گیشا زندگی میکنم ، با اینکه امروز ظهر هم گفتند یک جا یک جای گیشا را زدند متوجه نشدم
حتی الان هم که پیام گذاشتی داشتم می‌خوندم اما متوجه انفجاری نشدم
من گیشا هستم چیزی نشنیدم
آپدیت:
بعدش کلی پیام دیگر هم در تایید و تکذیب شنیده شدن صدا دریافت کردم ولی چون بعد از انتشار پست بودند نمیشه خیلی روشون حساب کرد.
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 320K · <a href="https://t.me/VahidOnline/76085" target="_blank">📅 00:19 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76084">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sibo_5yl3Cy5VlKfwcLY33fOJSduRNs4KtITDsRqdmL7l2qj2Bu_nDWWKiAWVcVe08rj87-XrkqXJVtlQsWwbMghl5Ax4924_QWvBzvqa1fvHmtUywhJKjYS2kkzjJ14wRaZv5xAPh9h5XF53WYEflwNeS6gCWaim7SUzO8NtwCvkLfCtfoA5kmjT7gWKE3d6N-iKQaPB_b7_Gn8q9JoVwMySFP21kdPfHNpzd4exIsSSsz2fcc2pve7zVPbQmoCoK9yCE9NgULMYO9nuExYEIiCx4nBtZgAKz20UwPb5Vf5Li-72WhA6BeP4HSp0VD6brk5HL05zR0ZNLVsQ1gN8Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
شبکه خبری سی‌بی‌اس، روز دوشنبه ۱۸ خرداد ماه گزارش داد، دولت دونالد ترامپ قصد دارد روند لغو تابعیت ۱۷ شهروند آمریکایی را که به تقلب در پرونده‌های مهاجرتی یا برخی جرایم متهم هستند، آغاز کند.
بر اساس این گزارش، وزارت دادگستری آمریکا این افراد را به پنهان کردن اطلاعات مهم، ارائه اطلاعات نادرست در روند دریافت تابعیت یا ارتکاب جرایم مختلف متهم کرده است.
سی‌بی‌اس نوشت این اقدام بخشی از کارزار گسترده دولت ترامپ برای استفاده از سازوکار قانونی سلب تابعیت از افرادی است که به گفته مقام‌های آمریکایی، شهروندی این کشور را از طریق تقلب یا پنهان‌کاری به دست آورده‌اند.
در میان افرادی که هدف این اقدام قرار گرفته‌اند، نام چند نفر که به جرایمی از جمله سوءاستفاده جنسی از کودکان، کلاهبرداری مالی، پولشویی، تقلب مهاجرتی و استفاده از هویت‌های جعلی متهم یا محکوم شده‌اند، دیده می‌شود.
تاد بلانش، معاون دادستان کل آمریکا، گفت دولت در برابر سوءاستفاده از روند دریافت تابعیت «هیچ‌گونه مدارا» نخواهد داشت.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 341K · <a href="https://t.me/VahidOnline/76084" target="_blank">📅 23:18 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76083">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/f3D8ASStHr6ADCZqQXmEwYiyy8WaplyaW1P5mR9UqS4qvN1YBmt0V9YiCxQBe7ZxJ6RVcQVpyTIa94jg3KBxabHAoN49p2ghnnMZ8_14NRKAoZaMd-gyGiDBF81aGIgB5E07Ruos05f2XemJt-bWWpmuabEbpK3dzBHK1BUuhWdDeiiKQ8bunqWvpM4c71oxauTaZqKtdfWAEy0s6W17Bd7Tr5_VRSIizfbQh2jiKyNUWG2diKVLwNvxgRW_Mp6DpyN312m4ThIf5F2OVOBmyk2qO9CBKqXmg-apNGeC25tSGdID_e_zKIVW2BTScXRZZlGD-H-Ago6s6-CgDDUJyQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شبکه خبری سی‌ان‌ان، شامگاه دوشنبه ۱۸ خرداد ماه، به نقل از یک منبع اسرائیلی و یک مقام آمریکایی آگاه گزارش کرد اسرائیل در حال آماده شدن برای حمله‌ای گسترده به تهران بود، اما دونالد ترامپ، رئیس‌جمهوری آمریکا، در تماس تلفنی با بنیامین نتانیاهو از او خواست از انجام حملات تلافی‌جویانه بیشتر خودداری کند.
به گفته منبع اسرائیلی، ترامپ در این تماس از نتانیاهو خواست دامنه واکنش اسرائیل را محدود کند تا از تشدید تنش‌ها جلوگیری شود.
بر اساس این گزارش، نتانیاهو در نخستین تماس که شامگاه یکشنبه به وقت آمریکا انجام شد، در برابر درخواست ترامپ مقاومت کرد و اصرار داشت اسرائیل باید به حملات ایران پاسخ دهد.
با وجود اخطار ترامپ در گفتگوی یکشنبه شب، ارتش اسرائیل برخی اهداف را در ایران، از جمله یک مجتمع مهم پتروشیمی، هدف قرار داد.
این شبکه همچنین نوشت لحن گفتگوهای اخیر ترامپ و نتانیاهو به اندازه تماس‌های هفته گذشته تند نبوده است. به گزارش سی‌ان‌ان، در تماس‌های هفته گذشته تنش میان دو طرف به حدی رسیده بود که ترامپ با الفاظ تندی با نخست‌وزیر اسرائیل صحبت کرده بود.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 345K · <a href="https://t.me/VahidOnline/76083" target="_blank">📅 22:37 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76082">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ko1ea_En5RrwDGvFCwTRFNPAXQ6g6Sf_fm6XaQuZ-rUWVL2YCVXlsRr8K0uULiKheKUXg3HCa07pV2XKNlLLansLdrE7JRScjAMGcVrf4I3q8nlWmI6i_0Jyr8Ux1dWSJDwLj7GkJ_kSoelSJ5MHe3m2uz7oAEz60Kk-UL-R3Vemo8YQvvKWfeVue9J3MHt6HD5RPDf6cV_rHpoPeTdZjUXHW7XeT4QFp6jL69kSRf9H62cUOz2cy__7kBJoB06gsjKrSXPgw2Dhqb50aS4RLJPamOu9WUEbREKwL4Lq3F2pNeWk4D8SnQ3Kxr8NNdqvWioWbFMU49Rs2xVTs-4B_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">محمدرضا عارف، معاون اول پزشکیان، درباره حملات موشکی اخیر جمهوری اسلامی به اسرائیل نوشت که دشمن در کوتاه‌ترین زمان ممکن ناچار به التماس مجدد برای پذیرش توقف آتش از سوی تهران شد.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 315K · <a href="https://t.me/VahidOnline/76082" target="_blank">📅 22:37 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76080">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/Xb-56ebX1KZoCulOjofdDyrdH_4VwagRB1oleJEVbIbLrRn7nbxMpXaXcm4e7ytfjuPVJk7lITcgzDgf8jOOeKpzM_hcQK0DCPPJKBUic_R2FsLKMMFFhb6yLpqPSswNX_oPi6vtEASdtu59gvvpIvhrE7DE2vTiyDYdmcPnWv931gDihr7IXywLQdj9LVqi0rma14hujxvt8uWjt4KQ5BSGtXbkcb_ukxq3f6Ua0KNED4IBip-pXkBpdo9MzA31tjKMCv9R5uMkkQA3mfkSMEJkaPd1RG1yGl26n05iewWoWALx99m_dsET6HHE3lB8zKiX_g5pol2B78pWxPhDcw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/HG098BTaKIzPFpHKr98sdV7aK8b9994YgzwlezFocxD4Mtq_12NRZbBYxtjr9oBxvMaoayWI8P3se-KNMy5ziGXZz_udz6MViTeig-DSctK6PPKdNXPV7a81zg2eL5JdiPeRHpFq9fvbEHLPtWr7NyQJhEB9JG6qtuectEjdd-ASGu7-iN5BsUQvWTKQ_IrABYxQYVc30WGO8jy2zOlDn4goe-rJKhaHkSbZJGXBAdm9uhTZcCkFNo-Kd5LhX0WNDSNQz8fxyWPE784wpc32OtZlpfWVph1S7mJXQ87tVbbj-Hbo05-91fx19bVOwbHExyYHr-6ElxGTZmPstFkOxg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">ترامپ گفت: «به بی‌بی گفتم خیلی مراقب باش چه کار می‌کنی، چون ممکن است خیلی زود در برابر ایران تنها بمانی».
@
VahidOOnLine
دونالد ترامپ، رئیس‌جمهوری آمریکا، روز دوشنبه در گفتگو با کانال ۱۲ تلویزیون اسرائیل اعلام کرد توانسته دامنه حمله اسرائیل به ایران را محدود کند و بنیامین نتانیاهو را برای کاهش تنش‌ها تحت فشار قرار داده است.
ترامپ گفت: «من موفق شدم شدت حمله اسرائیل به ایران را کاهش دهم.»
او همچنین افزود شماری از کشورهای منطقه از او خواسته‌اند بر نتانیاهو فشار بیاورد تا از تشدید درگیری‌ها جلوگیری شود.
رئیس‌جمهوری آمریکا در ادامه گفت در مورد حمله به ایران به نخست‌وزیر اسرائیل هشدار داده است: «به نتانیاهو گفتم خودت را در برابر ایران تنها خواهی یافت.»
ترامپ همچنین گفت نتانیاهو «با تاخیر مرا در جریان حمله به ایران قرار داد، اما من موفق شدم این حمله را کاهش دهم.»
کانال ۱۲ تلویزیون اسرائیل عصر دوشنبه ۱۸ خردادماه به نقل از یک مقام رسمی دولت نتانیاهو اعلام کرده بود اسرائیل حملات به ایران را به درخواست دونالد ترامپ متوقف کرده است.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 350K · <a href="https://t.me/VahidOnline/76080" target="_blank">📅 21:16 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76079">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/tWifXmXFXwyqiZ-3ybTx4mOqWghUWVWOXRkArLQRAaHNNV-AQExcoIJBOda4fZWKJDScIDPLKKgxj0DgGnOyp_6JiUYXTJkx_HtT_9rSUn2uPKjmy4Twnldif4ZhGZ1ssQ3pMDDjvii-kmi68NDYcvR0SaXc0uGd0eUgqb7l5zxO0KA7YUV9WCpYl87FGu6VZjqP3EEeNHh0N0gSZP70wptJp0NgLFN2iWnmK2-x5Q9VI7IYngEX7DIIRLnL61UsW-T4WPx5kNLNe0bs2i50tjhmALbmgbuy9U4SUoQV1uQtINJqEGGacUJ2DHS-9oFKi8zobfpHa-Whc-9Q3cl6pw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سنتکام: نیروهای آمریکا نفتکشِ متخلف را در خلیج عمان از حرکت بازداشتند
پست اکانت فرماندهی مرکزی ایالات متحده، ترجمه ماشین:
تامپا، فلوریدا — نیروهای آمریکایی روز ۸ ژوئن یک نفتکشِ بدون بار را در خلیج عمان از کار انداختند؛ پس از آن‌که این کشتی با تلاش برای حرکت به‌سوی یک بندر ایرانی، محاصره جاری علیه ایران را نقض کرد.
فرماندهی مرکزی ایالات متحده، سنتکام، نفتکش
M/T Marivex
با پرچم پالائو را هنگامی که در آب‌های بین‌المللی خلیج عمان به‌سوی ایران در حرکت بود، از کار انداخت. یک جنگنده
F/A-18 سوپر هورنت
از ناو
USS Abraham Lincoln (CVN 72)
پس از آن‌که خدمه کشتی از اجرای دستورهای نیروهای آمریکایی سر باز زدند، یک مهمات دقیق‌زن را به بخش‌های مهندسی و هدایت کشتی شلیک کرد. کشتی Marivex دیگر به‌سوی ایران حرکت نمی‌کند.
از زمان آغاز محاصره در ۱۳ آوریل، نیروهای سنتکام هفت کشتیِ متخلف را از کار انداخته‌اند، ۱۳۴ کشتیِ فرمان‌بردار را به مسیر دیگری هدایت کرده‌اند و اجازه عبور به ۴۲ کشتیِ حامل کمک‌های بشردوستانه داده‌اند.
CENTCOM
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 353K · <a href="https://t.me/VahidOnline/76079" target="_blank">📅 20:05 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76078">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/iB0QKCtArmoFbiXAb018md-VQLihHw4V5hJ1yGQDa1ej37xLVmX_hdrUdVFNYh7jzPw6MoJuUtByEg1k145ex_7BKOgDKy_yhyFSh7HM65gvbj_xknlnl_6fILfpf6fFb18Hhl1-79Dh9tahgczSU2PSrYgBCRa-G36I-KK8ydJqAM5EwpExUeEJgQ9BnYYOWwA8fOxcO_9TCD52BDofd78hsQl8HoxAg7WibBuBhbZ8mxHYu7Ijn6jo2gHX23ke79CyRqVRpgWixm1jpncweXaL9jCiKOX-XcKRFZbjSKIrecTQnWskd923B24KAEyy_5MEOxmSzHB3ncMceH355g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حامد تیزرویان، عکاس حیات‌وحش و فعال محیط زیست، در ساری بازداشت شده است.  به گفته زینب رحیمی، روزنامه‌نگار حوزه محیط زیست، آقای تیزرویان روز ۱۴ اردیبهشت ۱۴۰۵، بازداشت شده و موبایل و دیگر وسایل الکترونیکی او ضبط شده است.   اتهام مطرح‌شده علیه آقای تیزرویان «اجتماع…</div>
<div class="tg-footer">👁️ 317K · <a href="https://t.me/VahidOnline/76078" target="_blank">📅 19:59 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76077">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/mEUcx48n-hiCOHTCGBUPWyqcZnNA3re_REm099aQG2d7RHH-Zwey48UVilxsMcfZuhVI_YQPUvySZg6bL3jeydQTj2imcKIzVxSkM3DSlbmS-csA-gP5_7U5LxmpHJ-dn6yhnbCEHYhKJq2Knc38hR_wg_xMIFPpbKZOboO9rYupnNnHAzdwle63j7g0z377VPk7QPwMPZHiPNN0PRUQMIr5wt0a8yVMKnCztJWbS9huryqCkJqzyi8pphtV5z6fg6jmxWBv3TjLOMOdrKWNXlrcl2I2R2qK6V5TkXwTQYu39peBXea-nonR5h1eGGDaWp73ug1wIpm5LimvvQf_yQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ایران وضعیت پرواز‌ها به حالت عادی برگشته است
سازمان هواپیمایی کشوری ایران عصر دوشنبه اعلام کرد که فضای هوایی کشور به شرایط عادی بازگشته و عملیات هوانوردی مطابق با اطلاعیه‌های هوانوردی (نوتام)، از سر گرفته خواهد شد.
ایران ساعاتی پیشتر گفته بود که تمام پروازها از فرودگاه‌های کشور لغو شده است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 330K · <a href="https://t.me/VahidOnline/76077" target="_blank">📅 19:56 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76076">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/pnuW0e1Poi087U6dqYwn03jL2o2HPcurN-EPy9BmsS4kxCmUzLZJspntXmenEo7Cu-kwNd63XOHg8BqrXkb6VvlycGy4jKwseNOavvb4bO7YFSQ4_Bc-vJifiW4b57sTXD6uUUAxni0uOx-UyeXmJoI03D_571W1um3ntjkChg_8lU8iZDtejvqPhorJ3XqOZ0i-sx0-c3OdI5XznvmDuYkiHXG9a6LCeVkKGCeT-RJpuPg4ctM5mzjROOkTkGxZfPte5g5Po-0nUm4LFqkRJ_8SBSSV4eAN12l6NnldO_8v4E1RSXCslndPEttQt63UnC01sKYkL4CHwUNUWNnKoQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزارت دفاع عربستان سعودی اعلام کرد یک موشک بالستیک که از یمن شلیک شده بود، در منطقه‌ای خالی از سکنه در نزدیکی مرزهای عربستان سعودی و یمن سقوط کرد.
به گزارش رویترز، وزارت دفاع عربستان سعودی اعلام کرد این موشک به سمت یکی از کشورهای منطقه در حرکت بود.
همزمان حوثی‌های یمن، تحت حمایت جمهوری‌ اسلامی، اعلام کردند دوشنبه یک حمله موشکی به منطقه یافا در اسرائیل انجام داده‌اند.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 311K · <a href="https://t.me/VahidOnline/76076" target="_blank">📅 19:42 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76075">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TqM3MbBrfT8b8iDAS9gAzjmYFhh1gXO_GY5qEylIFFaqJ1KXe6t9c08S-KQl8vtXvmH4fUn5f3YD483aBrzX-ZqJfeOufuIULXRucRtom5K0rPkT4qmRYgaUuJt7W510yEEimpju03EAOJFx8jDO1MxZkZ2ZlpWGNihuCYeWRy0-AItidOTIsXEcq0__pwcSV_VwyLkKsdB-Tq3dnYz5ygEYaYR7rTxjtFYH8feaDLXA9o4VszWTsyXFQzFketAihzjOe2-kvCxHWAFcTD9xuKHeSn9qbRRZqNr6i7ROlK2hd-33o1tPPIrgLUiJMkavy-iLgF47KyEp4bw9sEouOA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یک مقام آمریکایی، روز دوشنبه ۱۸ خرداد ۱۴۰۵، اظهارات مطرح‌شده از سوی ارتش اسراییل مبنی بر مشارکت ایالات متحده در رهگیری موشک‌های بالستیک شلیک‌شده از جمهوری اسلامی به سوی اسراییل را رد کرد.
به گزارش سی‌ان‌ان، این مقام آمریکایی گفت ارتش ایالات متحده هیچ‌یک از موشک‌های ایرانی که بامداد دوشنبه به سمت اسراییل شلیک شدند را رهگیری نکرده است.
این موضع‌گیری در حالی مطرح می‌شود که در دورهای پیشین درگیری میان ایران و اسراییل، آمریکا با استفاده از سامانه‌های دفاعی خود در رهگیری برخی موشک‌های شلیک‌شده به سوی اسراییل مشارکت داشت.
@
VahidHeadline
نباید اینجوری نگاه کرد که تعداد موشک‌ها چقدر بوده و نیاز به کمک داشتند یا نه؟
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 308K · <a href="https://t.me/VahidOnline/76075" target="_blank">📅 19:14 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76073">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/idYrxJNd2GYYwkdZ_ZwZlfceYwkvo2Z1_M_N-xPvcGBQXhJnS_yjaH7Upzt3m_mUfo1y1MjJ7S1Apz_LxwoyXXDATyzdTJ6lkGWbjsz0b-__8scGQKq2ejsVjtrcE3z7gX3wTRVYH48e0xPtNOgswFdVRuQe4ab9hSbT-6KV8YD5Yj_aIpbGeN-GctCB0EQI118Lh2ZTIRaqLQIvKL27PjWTXAGkuqAwoHZ1BUeFT9QXKUv5ZN8HJscVIBLlvdowhIflgKD1kRe_eqhk-3lX_9lyc-8OimQ1b4abUsuvxWkBkMQCYFnc_uz4dKtI3zWkl0Nblo09nNOXmkM0Ri20Jg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/fca0bb1962.mp4?token=aTpR2YfMTsmvT5MmH1ssZeAzyNmlr-TVI3aPvCD4xZLZCXGimtwAtaUNICOeoQPUeyi1iCPdwk7361_e7QUAY3S5FEE0iV0yqdD1VGJuocpoJQQs_Gxg2S0uGKlfVe2LMIeBD6NSsthvv8Aa93RWn8kwkEGJe34myRTRmCo9HtoFUO7-WRz2MbDx-x2rmhiplXF4a2H495S8XgH8VzvnZS3R9RO0TDg2cImBuBwPALYkYwfeJiRhd7E0Sg6LoSoyUqfpzXWpDyWhBIEBvwf_usN3bSdTro2AMJYurVQamH5qug7VsPl3ZoAFxjwEcWiEQ0hjlcm7KrU-1odc3QQM5Q" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/fca0bb1962.mp4?token=aTpR2YfMTsmvT5MmH1ssZeAzyNmlr-TVI3aPvCD4xZLZCXGimtwAtaUNICOeoQPUeyi1iCPdwk7361_e7QUAY3S5FEE0iV0yqdD1VGJuocpoJQQs_Gxg2S0uGKlfVe2LMIeBD6NSsthvv8Aa93RWn8kwkEGJe34myRTRmCo9HtoFUO7-WRz2MbDx-x2rmhiplXF4a2H495S8XgH8VzvnZS3R9RO0TDg2cImBuBwPALYkYwfeJiRhd7E0Sg6LoSoyUqfpzXWpDyWhBIEBvwf_usN3bSdTro2AMJYurVQamH5qug7VsPl3ZoAFxjwEcWiEQ0hjlcm7KrU-1odc3QQM5Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نخست‌وزیر اسرائیل روز دوشنبه ۱۸ خرداد با اشاره به توقف حملات متقابل اسرائیل و ایران گفت «آتشباری متوقف شده اما اگر رژیم تروریستی (ایران) اشتباه کند، ما به شدت پاسخ خواهیم داد».
بنیامین نتانیاهو در اولین پیام ویدئویی خود پس از آغاز موج تازه حملات ایران و اسرائیل، افزود: «ایران و حزب‌الله از همیشه ضعیف‌تر و ما قوی‌تر از همیشه هستیم».
به گفته او، «ایران و حزب‌الله تلاش کردند معادله جدیدی را به ما تحمیل کنند که از نظر ما غیرقابل تحمل و غیرقابل قبول است. آن‌ها فکر می‌کردند که از خاک لبنان و از ایران به اسرائیل حمله می‌کنند و ما سکوت خواهیم کرد. این اتفاق نیفتاد و نخواهد افتاد، نه در زمانی که من رهبر هستم».
نخست‌وزیر اسرائیل تصریح کرد: «ما حمله خواهیم کرد، با قدرت پاسخ خواهیم داد. به نابودی تمام زیرساخت‌های تروریستی آن‌ها در جنوب لبنان ادامه می‌دهیم، و امنیت را به شمال باز خواهیم گرداند. اگر به موقع و با قدرت اقدام نکرده بودیم، امروز این‌جا نبودیم».
نتانیاهو همچنین گفت که ایران به سلاح هسته‌ای دست نخواهد یافت.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 306K · <a href="https://t.me/VahidOnline/76073" target="_blank">📅 19:13 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76072">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/YkCRkxLsL6k2V0LDY0BhFK6My384Kze0QXJ_tb55y4h7uIbQ6-NVsTHRNTK6z0ik7yzFZjYP29ANFLu89XYsn0kuy4rbsb-lQV82s_gZIhIVGip4VMc3i8N6eFtsi6i4IcQllfpUIZRQOi7xzJs3owieP4H1cQD_mkPUNQajvZLgR3YAeHEaWz5tbMk2N_QAhyUEpntLkDGPamzVHygOMKZd2nwjs-5fdDq92AY145JUmmRmG0rwDamt1_KLd-2EUkSh0di9Tnut74m8_j-yi0_Y_NfVRsVIk2LSfjVR6UwPEzQD_VzxLFh5UTzfzvnl8qI6CXS2smVE7zey0o1Mig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اسرائیل هشدار تخلیه فوری برای مناطقی از لبنان صادر کرده.
J74wabx
ارتش اسرائیل با صدور یک «هشدار فوری» از ساکنان جنوب لبنان، به‌ویژه در منطقه «زقوق المفدی» خواست خانه‌های خود را ترک کرده و به سمت شمال حرکت کنند.
آویخای ادرعی، سخنگوی عرب‌زبان ارتش اسرائیل، در شبکه اجتماعی ایکس نوشت: «در پی نقض توافق آتش‌بس از سوی گروه تروریستی حزب‌الله، ارتش اسرائیل ناگزیر است با قدرت اقدام کند. ارتش اسرائیل قصد آسیب رساندن به شما را ندارد.»
او همچنین هشدار داد: «هر فردی که در نزدیکی نیروهای حزب‌الله، تأسیسات آن یا تجهیزات و امکانات رزمی این گروه حضور داشته باشد، جان خود را به خطر می‌اندازد.»
این در حالیست که ایران امروز گفت عملیات جنگی علیه اسرائیل را متوقف کرده است اما هشدار داد اگر حمله به لبنان ادامه پیدا کند با شدتی بیشتر از قبل پاسخ خواهد داد.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 297K · <a href="https://t.me/VahidOnline/76072" target="_blank">📅 19:01 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76071">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/qBDLjdtl_t9bjWTicJ_R1RayOoqHYWD69J70FbqDsWPN1vMD_yxZmxZDMDJFHikhp2sK21luo8DGgrGyMUi45av3d8ln_lTAUllTIyiWhyzRxDMYnhTvXv3YVvtUtZIw-GThFsPIHh64oW_pNkQnLqVCsIjOn6Yn7k4xbuwyIa1BBk7rDf0nzSfJ_urkj19NynAnEYHxdFANjGPYd8j7vf01vmXS_Q3LBtKoxa7YTaUSosPuiEUzzyHKnMRvd6LKfWBm2sWE_Rw4up3lsvofZ3Nh1qCi8Ay-NiywSA7hvo59p7LnjFAlDKSacQ2sFrW2FKiCVo69-SW-sU54KCk0cA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">IranSaat25
(وطنه*)
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 289K · <a href="https://t.me/VahidOnline/76071" target="_blank">📅 18:54 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76070">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/dXYpbQWew5-TQuMA-d2aN3OVpwzfGh4KaQyvhDzNtD2dlX7h-_trfP9vOeagy9m2rvCQcAdLID8RJbKdmg5hoI89Db_OiEgaPKkEWaoMg-Vq99hLLLzYD_rfKCDdO0KcaHRCs6qVv_3p2EUUVGp4NmIaR4FpHtpSwG5M7EWBvzWZ5TT_ibKhuUT6jWNH6AWR7JdLV-tb5Hu34ma1XSJRmpKYcQjiaGeZyvjOxn8hk666j4GKlhttmfccNGlaJ73TdB-FDJtzF43ZRrS2eyBzMoBa9RWLzbamA9QV9fEC316HGk9VwwtEgW35nT4GsBlCxjwXMX0Q7_hbb8Bxe1Oyvw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">Atlansick
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 298K · <a href="https://t.me/VahidOnline/76070" target="_blank">📅 18:51 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76069">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ArYq0KqbvYgkidQwU9cT_ksZbKBFEqxFmKa-ji1taRNkjTHjXBLRqBJVtcj9vUi2hxJRpGUs3h_R40xmeX7ZTHAbLGAYeoSrEJOry9ljdgAKD7GB_JRRHlZq5d7kD5Bked4cZtSzE3LaCKc0biDtGUjWtiV9UC-wCbopsC5sK9NzSmGhAsFb2A-ZzYv5D5ywz3fcajeGkcSn4OWiUF3GMVDao9T5UuuRQy3Nwdf-5yuwcM8g_C3wywqpEVWCtUAtDzRVCv8kWZK3hQcyp9vfamWoHPTPMzamslx0l84t87K7lf1fG3wR9WzT9q3wFl05lpCuhH21L6m5nnNqSTBlrg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">محمدباقر ذوالقدر، دبیر شورای عالی امنیت ملی جمهوری اسلامی ایران، در پیامی که روز دوشنبه ۱۸ خرداد منتشر شد، هشدار داد در صورت تکرار اقدامات آمریکا و اسرائیل، منطقه با پیامدهای گسترده‌ای روبه‌رو خواهد شد.
ذوالقدر در این پیام نوشت: «تهدید معتبر را از جایی غیر از واشنگتن و تل‌آویو جست‌وجو کنید.» او افزود: «اگر ائتلاف شیطانی صهیونی-آمریکایی دیگر بار دست از پا خطا کند، منطقه برایش جهنم خواهد شد.»
دبیر شورای عالی امنیت ملی در بخش دیگری از این پیام مدعی شد که جمهوری اسلامی طی «چهل و هفت سال و صد روز مقاومت»، از میدان جنگ تا عرصه سیاست و دیپلماسی، معادلات امنیتی جهان را تغییر داده است.
این پیام پس از آن منتشر شد که قرارگاه مرکزی خاتم‌الانبیا اعلام کرد عملیات نیروهای مسلح جمهوری اسلامی علیه اسرائیل پایان یافته است. رسانه‌های رسمی اسرائیل نیز از توقف حملات این کشور به ایران به درخواست دونالد ترامپ خبر داده‌اند.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 281K · <a href="https://t.me/VahidOnline/76069" target="_blank">📅 18:43 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76068">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DThcraQCG6qhSAbbaLzg5dwZicOYdguRQBLA8__Eh_62Xa8hKW6YoaBqHyKj2396fW291wUeokYuROqI-bAeaetxvdbgOrvdYcz5cT9xA3qi4wsmp-SW7hlynOmqskd9kBToWKkt53LwUePXZinCHFw15nhn72I3n0yyeGZGumdkYvV-DpxDhm_Zr7SUg9XmrxV6r9j5vuc7BNNymGSSwTZLdaqyfFBn4qSgDNNFwDoP2HneZzlae__JFcO3Xc8LTwYV84aFiI1N28KRNS0cIwmnCSXgOy9NpYIJJCcgjZg0hcptUwvVWVIXXBi0RlObTgxW4s1IzLkoW6IR9RRFEA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یسرائیل کاتز، وزیر دفاع اسرائیل، اعلام کرد هرگونه حمله به شهرهای شمالی این کشور با حمله به ضاحیه در جنوب بیروت پاسخ داده خواهد شد و ارتش اسرائیل به عملیات خود در لبنان علیه سازمان «تروریستی» حزب‌الله ادامه خواهد داد.
او افزود: ما تهدیدات جمهوری اسلامی را کاملا رد می‌کنیم. هرگونه تلاش تهران برای پیوند دادن لبنان و ایران و حمله به اسرائیل، همان‌طور که یک‌شنبه اتفاق افتاد، با شدت زیادی پاسخ داده خواهد شد.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 271K · <a href="https://t.me/VahidOnline/76068" target="_blank">📅 18:43 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76066">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/4c3ab90b1c.mp4?token=nlRKTE9Nc-fV01lYKauH3qBQimduXoWKCb6kgrKzdnWqs4B1jRTWjMxZXUT3SEgxX4Wx3pmK7AZc6wG1BrHWj_j08RZ90F04gLA0bvU3MB_e8QoRCb5QI7bPw2kgDkU1QxXrc1dljwZXIMC3Nnr6Vcg8hsexUQlFx_ATRLkfOpKqCGsgplXhz4E0D70PQFaBkG-DdUNAAUC0l2-MqHrZQyiFQxTj5h6Ser52ikfPBRXYuEX2-izYO3_Du8xhGAf7OgFSuGBcplWwSrqRPC6Py0-AmjBRx_KNczzs0de3bRCXdtTnCDDdWZLFJcyVLv5SLEylU37Zq2mOSt8hUEWCHA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/4c3ab90b1c.mp4?token=nlRKTE9Nc-fV01lYKauH3qBQimduXoWKCb6kgrKzdnWqs4B1jRTWjMxZXUT3SEgxX4Wx3pmK7AZc6wG1BrHWj_j08RZ90F04gLA0bvU3MB_e8QoRCb5QI7bPw2kgDkU1QxXrc1dljwZXIMC3Nnr6Vcg8hsexUQlFx_ATRLkfOpKqCGsgplXhz4E0D70PQFaBkG-DdUNAAUC0l2-MqHrZQyiFQxTj5h6Ser52ikfPBRXYuEX2-izYO3_Du8xhGAf7OgFSuGBcplWwSrqRPC6Py0-AmjBRx_KNczzs0de3bRCXdtTnCDDdWZLFJcyVLv5SLEylU37Zq2mOSt8hUEWCHA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ارتش اسراییل، روز دوشنبه ۱۸ خرداد، ویدیویی را از لحظه حمله به یک سامانه پدافندی جمهوری اسلامی منتشر کرد.
ارتش اسراییل گفته نابودی سامانه‌های پدافند هوایی ایران، آزادی عمل هوایی بیشتری برای عملیات‌های بعدی فراهم می‌کند و بخشی از تلاش این کشور برای مقابله با تهدیدهای جمهوری اسلامی به شمار می‌رود.
@
VahidHeadline
و در پستی دیگر ویدیوی دوم بالا رو درباره مجتمع پتروشیمی در ماهشهر منتشر کردند.
بدون هیچ شرحی درباره اقدام نظامی خودشون نسبت به اون مجتمع پتروشیمی
نه در متن پست نه در خود ویدیو
اگر قبلا تایید نکرده بودند که به اونجا حمله کردند این طور پست گذاشتن بیشتر شبیه به تهدید به نظر می‌رسید. شاید الان هم همینطور باشه.
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 265K · <a href="https://t.me/VahidOnline/76066" target="_blank">📅 18:39 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76065">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/LKSkITTAPT8iYfdq8841J1U39Vbycv6qkEj6T86xE7h8QA8ntS8iTcTPpemy6025NhEbmkWsvuea56e_05lpZ_NhlgxcF3-vGU-49xTMFX3NZ3mqHLkC0OQ-cidtSXSYUIjR-TG-GxAfLnbu39vq3ngeWdP74c98bRR47wl6OhwVewYzYCvYvorOCcNGkd9khoCC_WEvzmID8nOUYzDIMXa0lEDYbEm57z9nH4qSV9LTYv27F7wmGh61HO9672nmjo8lrRnWEW2sbB8n6egjwUovi7pZOrDYq571Do4mqNE5SyE_0NGVKXhj7w0oitCJ0x0tg39v581tldrOrdy87w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">توییت محمدباقر قالیباف:
"معادلهٔ آتش‌‌بس روی کاغذ و نقض مکرر آن در میدان را بر هم زدیم.
تا زمانی که ارادهٔ واقعی برای اعتمادسازی نداشته باشید، پاسخ ایران همین خواهد بود."
mb_ghalibaf
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 263K · <a href="https://t.me/VahidOnline/76065" target="_blank">📅 18:30 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76064">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PUJA541Z0iUwvvSP4BjgaGUfwQZzD5MAqXKDG8o_ul6QKT8m6Yo66VHDmQawXhl_s9gLZKbAZypLUmxGym_t1-Gy7Lbxtqn_zrPCc8YlGP2nHxdewBpa_qHQO-ZIn1zXoT1aIlDhBxbFnj-EkJppHoPywY4HZPiHNSQETM7gwd0__yMTRHCcwziz7S43axj3_cP5r7JKZ87Zaixhj0SB3lauzJb-3isu9zo1PExKsRY2TiN27O6UJSMUlA4mUqVXtEClAUhUnzbz7VFf0XjiBCp3BkAtznf7-3L8fzgOiX7oHRdsH08Gz-jG5FPGnQZMniMxbLpPeb2lTf_IIQbYbg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رسانه‌های دولتی لبنان گزارش دادند یک حمله هوایی اسرائیل روز دوشنبه ۱۸ خرداد یک خودرو را در شهر صور در جنوب لبنان هدف قرار داده است.
خبرگزاری ملی لبنان اعلام کرد: «یک حمله هوایی دشمن، خودرویی را با موشک در شهر صور و در نزدیکی ساختمان صلیب سرخ لبنان هدف قرار داد.» تاکنون جزئیاتی درباره تلفات احتمالی یا هویت سرنشینان این خودرو منتشر نشده است.
این حمله ساعتی پس از آن صورت گرفت که جمهوری اسلامی ایران و اسرائیل پس از ۱۶ ساعت درگیری نظامی اعلام کردند حمله به یکدیگر را متوقف می‌کنند.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 264K · <a href="https://t.me/VahidOnline/76064" target="_blank">📅 18:29 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76063">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/O3hbE973k9_4riEpDsXp_04kyD7dOTZl6rgtTzwI5dL7mSHtNnB1MB1PJ8zKZZi_aNAhqGdjQmFfetPKFLt8lk56cdLGuW8ihMXYt2ctJkAOXfr_mt1UucGM1yqESTZvBfeXweHQYYLhifnuC_KPsPDcFNLbBidCBnbFRwwdc-JIwkNeXealsLOrUkAIQ7A_XYIAbEPVSdFV-iu1A7wrOD47IYLM3zPhQ0e_XqY1mLsLxcLvaD3Ie0LvGEnk5mFjfMzQxZTSvhnLhwAqWH-mK_MkfLHWW2YXsAjuz-4z2qs_gZepooriT6SaPSQ-lxV9z3MIC4CD7G2SeQRFK0ABwg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رییس سازمان اورژانس ایران، روز دوشنبه ۱۸ خرداد ۱۴۰۵، اعلام کرد در جریان حملات اسراییل به ایران، ۱۵ نفر مجروح شده‌اند و تاکنون هیچ موردی از جان‌باختن شهروندان گزارش نشده است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 265K · <a href="https://t.me/VahidOnline/76063" target="_blank">📅 18:22 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76062">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FWvamWPV6sBQ8vxxzof1aDm_2q-yRmrrBgP1dHvMYVOos-BGls0JPy4uUnqnaAwiAZ5qVVdZAE9DV0h984j7nv9x-3JGOAt-viLAPdZZ-8-XDe46yIXSK99ULPYmCAqdzQuaUU6oOxB0PxCwY0AnVhNs7khmygmAk0-C9W6u3GS0Nswci0vLEq3593iy_Oc8Y1_UqwL6YgQv5WDnyze2oApKEDxhSzsHTClVHYPpZFnt7VxkBb2VwnN2r8rm9caQUaQTxYMHBhb2DD_LKQw1k1dA3Jmhupa6LyABaoqFeJvd3RCBFtxuHxhIO0aAhKABUz9mU33X0i6YD2crkF9_bg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرگزاری ایسنا عصر روز دوشنبه، ۱۸ خردادماه، به نقل از شرکت فرودگاه‌ها و ناوبری هوایی ایران خبر داد که «همه پروازهای فرودگاه‌های کشور تا اطلاع ثانوی لغو شد».
این اداره همچنین از تمام مسافران خواست تا «جهت حفظ نظم و پیشگیری از هرگونه سردرگمی، تا زمان اعلام وضعیت عادی از سوی مراجع ذی‌صلاح به فرودگاه‌ها مراجعه نکنند».
این خبر ساعتی پس از آن منتشر شده که قرارگاه مرکزی خاتم‌الانبیاء سپاه در آغاز بعدازظهر روز دوشنبه با انتشار بیانیه‌ای از توقف عملیات نیروهای مسلح جمهوری اسلامی علیه اسرائیل خبر داد.
همزمان رئیس سازمان حج و زیارت خبر داده است که «با توجه به شرایط پروازهای بازگشت حجاج احتمال تأخیر در برخی پروازها حتی تا ۷۲ ساعت وجود دارد».
او اضافه کرد: «برای فردا (سه‌شنبه ۱۹ خرداد) ۱۰ پرواز پیش‌بینی شده که امیدواریم بخش عمده آن‌ها انجام شود.»
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 313K · <a href="https://t.me/VahidOnline/76062" target="_blank">📅 18:22 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76061">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ns28mmaEqFHd715oBQ8Ul7u-gQHwAd8dczbTTpai-8Rv3leACEOiMCcCscVoeqmBS6D6qbZJeIEe5DrnEsz8iCIqlPlrpNdAtXL_T8GBw86GOwlGP-4H8I_SDsyuO030mmbjAF3Uj7aFFpp2wz4MG8rBxRg5kXow0pr7NvNr-nzHzvnHF8ARtXZs6R1UUWFe4yCGnIrKxxG6msXEfVgUR581n-fIiJD8FGTg3wFX4DRcoAJFmy-fdRmPwWEtPRgUXs4uE15QhpQgL4NSS6hFX1ShQe78sSqkFpc4zl1aI_Diokqwps8hqMDiKodYwD4Fq8zhvJKdvKlYupf1ZX2l5A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کایا کالاس، مسئول سیاست خارجی اتحادیه اروپا، روز دوشنبه ۱۸ خرداد اعلام کرد که اتحادیه اروپا به‌دلیل تهدید آزادی تردد دریایی توسط جمهوری اسلامی، تحریم‌هایی را علیه شماری از افراد و نهادهای ایرانی اعمال کرده است.
کالاس این اظهارات را در جمع خبرنگاران و در حاشیه نشست وزیران دفاع اتحادیه اروپا در قبرس مطرح کرد.
هنوز جزئیات بیشتری درباره این تحریم‌ها ارائه نشده است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 390K · <a href="https://t.me/VahidOnline/76061" target="_blank">📅 15:37 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76060">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/4b31564948.mp4?token=O59wzMvsVgFtboLWYy9_DGFQDIwq2USHlqeGL_qgsWC48RDZPKzjuNGjVZO5gTVrnTGqRm1kwHfXS1pD8L1RF20wN7cBDyRzWPSNdWaKc7ia3kIoPFVoZ7diIyT0ow7fDeIrQhOhdZuZB4DTMxLyLy7yMF2M6XxbgvVYEMR8TraRUcyhfbNMQrYSXcoYKJYtBTcear4ODYXsWSptSfZF_k_1lYkU3v7ZbuWyYyCxdhqjJsLYC9vCFT5V90XxMiPo97r2NczdJyaiym2ApuEIwEhJPMfOWyOyEGOO2UKFDcbsmDD1UN6IX6JIs0NFYnEt4VGGmzWNvJNezbcOKU2CVA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/4b31564948.mp4?token=O59wzMvsVgFtboLWYy9_DGFQDIwq2USHlqeGL_qgsWC48RDZPKzjuNGjVZO5gTVrnTGqRm1kwHfXS1pD8L1RF20wN7cBDyRzWPSNdWaKc7ia3kIoPFVoZ7diIyT0ow7fDeIrQhOhdZuZB4DTMxLyLy7yMF2M6XxbgvVYEMR8TraRUcyhfbNMQrYSXcoYKJYtBTcear4ODYXsWSptSfZF_k_1lYkU3v7ZbuWyYyCxdhqjJsLYC9vCFT5V90XxMiPo97r2NczdJyaiym2ApuEIwEhJPMfOWyOyEGOO2UKFDcbsmDD1UN6IX6JIs0NFYnEt4VGGmzWNvJNezbcOKU2CVA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدئویی در شبکه‌های اجتماعی از لحظه حمله‌ الهه و شهربانو منصوریان به اتاق ریاست فدراسیون ووشو و شکستن دوربین مداربسته منتشر شده است.
طی سال‌های اخیر
خواهران منصوریان
بارها به ساختمان فدراسیون یا کمپ تیم‌های ملی حمله کرده یا با مدیران درگیر شده‌اند، اما همواره از حمایت نهادهای حکومتی برخوردار بوده‌اند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 379K · <a href="https://t.me/VahidOnline/76060" target="_blank">📅 15:31 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76059">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nAbzoYyBTM4k4Ys6S0dkeYqyTISv_rqOel4vTE4gP2wGnpmJBPvu9T3SDL7EDwxpzovud9MbSgfD2PnJUbWnuMOq2OugMmC6U8LCh6twQT0Ix4okUxe2jY19-fiiJNXdgc6X70eOfgijLf8B-2xTZmTdL0mxgiVSSfFFVYRqOIemqBWdV4I5fXPSrCuxt9yaH3mD5UpikUvshT7VbtEYquoNgJh0xSnaaFJy_I4mDNlS9Tusty6YnV-w1haCIyq5cP275bv-mHXWpeEDyqWQFSDau5LUqTQJKGe8uoTsqclJzAodrTyujaxdcGW8tZh0lY9vjNo3St9Bz35OAFfHvw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⭕️
سپاه پاسداران از «توقف عملیات» علیه اسرائیل خبر داد
♦️
قرارگاه مرکزی خاتم‌الانبیا سپاه پاسداران، روز دوشنبه ۱۸ خرداد ماه با اعلام آنکه نیروهای مسلح جمهوری اسلامی ایران در واکنش به حملات اسرائیل به منطقه ضاحیه و جنوب لبنان «پاسخی دردناک» به این کشور داده‌اند، از «توقف عملیات» نظامی خبر داد.
بر اساس بیانیه قرارگاه خاتم‌الانبیا، پرتاب موشک به اسرائیل «در راستای حمایت از مردم مظلوم لبنان» توصیف شده است.
در این بیانیه آمده است که این پاسخ برای اسرائیل و حامیانش باید «درس عبرت» باشد.
قرارگاه خاتم‌الانبیا همچنین اعلام کرد «توقف عملیات نیروهای مسلح» در دستور کار قرار گرفته است.
با این حال، در این بیانیه هشدار داده شده که در صورت ادامه حملات و اقدامات اسرائیل، به‌ویژه در جنوب لبنان، جمهوری اسلامی ایران «اقدامات بسیار شدیدتر و کوبنده‌تر از قبل» انجام خواهد داد.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 437K · <a href="https://t.me/VahidOnline/76059" target="_blank">📅 15:01 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76057">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/u3hRruqTgnk9KVaBKoZX1sqDkNR9T7zTZ0MuObaGPRhooi_lLMkk6Ficdvd1PcBvPuAkBVbzklCmWbOPh9zv0R0WB_AKbSucOiDoFC29Tfdrcec5_XCtHP7nq_zsBSTHJaLyVFxP1b9B8U--GV7kEJ6zkT1zjFnpNQNZFpCvtc7rvmiXjvKYKfjaRlFVEKS6lpUyQXO7LhWSWEm53t2jYBhapfzXdm6sAI_PARwSDoMKQqDPwXswmrOT2-MwqSTJcqvld9bHA-Xm0L7p8gRQovIAOESD6GyReeEdvlOdBNygYbIsThQZZIBU91ANZa_c0ZNvAMaQ_PROQ6tHBbRVRw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/qO3dujOpiGLweSgtzZLBB5m3wR5Ca0h3BAWTucMreEAiyE4Ce3ZedOLBAF5OpdJrZvVBj9YOwxy-oNHtZmAZ4kbSx5Q3bGfjSoEAwENh2I7VtDmIun8gjtSxJM2GqxWRSendIKMV162tOhCH22en261N78ze5l3wXWBzUG8dcLSUt0SR1c-8Rz79L_gOCf2uN4xJeADS3BlUGTBe5dYOGzsgqHcpm5jqQ3NX9gQqJvBhV6lP_XR_ba_zaiHs6O2GEr-ZkyVcfeZxpzERr_dqCQubCgRGR0nQIheFwGOsTeprM9dV3zmtXnicFmxyth1Xo3eMeTZfUzNEsHfbsB4nqw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">اسرائیل و ایران باید فوراً «تیراندازی» را متوقف کنند.
رئیس‌جمهور دونالد جی. ترامپ
realDonaldTrump
دو طرف، اسرائیل و ایران، به دنبال برقراری فوری آتش‌بس هستند! مذاکرات نهایی درباره «صلح» در جریان است، مگر آنکه نادانی یا حماقت مانع آن شود. محاصره تا زمانی که «توافق نهایی» حاصل شود، همچنان برقرار خواهد ماند و با تمام قدرت و اثر کامل اجرا خواهد شد. امور باید به‌سرعت پیش برود. از توجه شما به این موضوع سپاسگزارم!
رئیس‌جمهور دونالد جی. ترامپ
realDonaldTrump
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 411K · <a href="https://t.me/VahidOnline/76057" target="_blank">📅 15:01 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76056">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/UGZY9JJmLB5IvTBZIQWkI0QoVa8-5tq6phw_OpE4poilx52gABU47eY02GbBmeT5SeSVh395eAE5g6O6lkeOT-dO25DD65tqiZycFRltf6eclGzqMOnfDpsZtfHmsFZ1KjvG6NWNrZfix5EO6bwbYLKtOCSF7JygBbbDFft6NNGo6n28s79EqlS0xNwjjacPia2e8OnLqDVQeMzNkZGcE1HkaAzEzbUi6YPQnmguj3LqblfU8nD_CzuWjv7mE74aG3VuqZy3FKiEPKAiRA7iEk8C2I8U-ewwrGPcuAOnFhPR7ae4Jbrs_Gp9u5byVwpqldl-xTkxDF0WmNk-5f5KiA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رسانه‌های وابسته به جمهوری اسلامی گزارش داده‌اند که نیروی هوایی اسرائیل همچنان حملات خود را در نقاطی از کشور ادامه می‌دهد.
بر اساس این گزارش‌ها، فرودگاه شیراز در جنوب کشور نیز در میان اهداف حملات اخیر قرار داشته است.
هنوز جزئیات دقیقی درباره میزان خسارت، وضعیت پروازها و تلفات احتمالی منتشر نشده است.
@
VahidHeadline
در خبری دیگر:
خبرگزاری مهر وابسته به سازمان تبلیغات اسلامی نوشته:
"پهپاد متخاصم دشمن آمریکا_صهیونیستی توسط پدافند هوایی در آسمان تهران هدف قرار گرفت و منهدم شد./ مهر"
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 501K · <a href="https://t.me/VahidOnline/76056" target="_blank">📅 11:55 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76055">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/f-h8toECyVXn4mwM4ren5uUVtA1gQOOxF9F7ek0l8dkmmOXdLHmfUa5iJS80Tq02qeQMPXbr3n8tBQa7BFvJPkO6AWMxs-1ORBj3_-xFCCGmus2_v1MnA5GV5l7Q5aUiQJlNVn2ECRDKvuswuQTaOZ5Y6lsl5qm3YmHjs7L-lLnAVS9KFD3l6aONCMaqy9wihO9NvLZlJFrUjSzeDyHvBFN1CtrUKrX8cQwm3ld1qkEzDp_vBd2j7p9g6crkyjgHh11s1_oE_aYj1yZARrLwEfVJXnri-5XeyOeGtLgH8bxTNqTZUErDCXNd1cHGA71cNGwK-xNhfQfQi8VFXuKWgw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سپاه پاسداران در بیانیه‌ای گفت در پاسخ به حمله اسرائیل به صنایع پتروشیمی ایران به صنایع پتروشیمی حیفا حمله موشکی کرده است.
بنابر این بیانیه، هدف قرار دادن اهداف غیرنظامی و تاسیسات نفتی «بازی خطرناکی» است که زیرساخت‌های انرژِی منطقه را تهدید می‌کند.
پتروشیمی کارون ماهشهر که در بیانیه سپاه نامش برده نشد، تاسیساتی است که هدف حمله اسرائیل قرار گرفته است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 496K · <a href="https://t.me/VahidOnline/76055" target="_blank">📅 11:47 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76054">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">پیام‌های دریافتی:
‌
وحید تهران صدای مهیب وحشتناک
ساعات 11:33 دقیقه جنوب تهرانسر صدای انفجار اومد
سلام ساعت ۱۱:۳۰ رباط کریم صدای انفجار
تهران صدا و موج شدید انفجار ۱۱:۳۲
همین الان صدای تک انفجار غرب تهران
زدن تهران صدا واضح انفجار
ساعت ۱۱:۳۳: صدای یک انفجار شنیده شد - تهران آزادی
صداش خیلی زیاد نبود حوالی غرب باید باشه احتمالا
اسلامشهر صدای انفجار ساعت ۱۱:۳۲
تهران الان صدای انفجار اومد
تهران غرب ۱۱:۳۳ تک انفجار بزرگ
سلام وحید جان.۱۱:۳۳ تهران صدا انفجار اومد.من غربم صدا دور بود ازم
۱۱:۳۳ دقیقه صدای انفجار ملارد فکر کنم زدن
ما سمت مهرآبادیم ساعت ۱۱:۳۲ صدای انفجار اومد
صدای انفجار در اسلامشهر ساعت ۱۱:۳۴
وحید ما غربیم 11.33 صدا انفجار امد
یه صدای تک انفجاری اومد الان انگار سمت یافت اباد
بهشت‌زهرام. از نزدیک اینجا صدای انفجار اومد. ساعت یازده‌و‌سی‌و‌دو.
همین الان اسلامشهر تهران ۲ تا صدای انفجار
سلام وحید جان، صدای انفجار در فردیس
غزب تهران سمت پونک همین الان صدای انفجار
تهران اطراف اتوبان نواب صدای انفجار
شهرک غرب
صدای مهیب انفجار از دور اومد
وحید قلعه حسن خان دو تا صدا انفجار قوی
سلام باقرشهر کهریزیک صدای انفجار 11:33
وحید داداش سمت دریاچه ۳ تا انفجار ولی دور بود
11:32
گرمدره صدای بمی داشت تک صدا بود ولی دلم یجوری شد
سلام وحید جان من سمت مهرشهر هستم ساعت 11:31
صدای انفجار خیلی وحشتناکی اومد
از شرق کرج یا غرب تهران
ساعت ۱۱:۳۳ سمت ملارد صدای انفجار وحشتناک اومد
سلام ۱۱:۳۳ صدای انفجار اومد از جنوب تهران از دور بود
تهران سمت شریعتی ساعت۱۱:۳۲ صدای خیلی دور انفجار اومد
از ملارد ساعت ۱۱:۳۳ یدونه صدا اومد
وحید اسلامشهر دوتا صدای خیلی وحشتناک اومد
ساعت ۱۱:۳۴ اسلامشهر ۲ انفجار با فاصله یک دقیقه
ما سمت چهارراه ولیعصریم دقیقا ۱۱:۳۳ دای انفجار از دور اومد
سلام ما عظیمیه کرج ساعت 11:33 صدا شنیدیم، دور بود
سلام من نزدیک مهرآبادم یدونه صدا اومد بنظرم بلند بود اما خیلی نزدیک نبود
بازم هم مهرشهر کرج صدای یک انفجار
ساعت ۱۱:۳۵
درود گلشهر صدای انفجار اومد همین حالا
ما تو یافت ابادیم صدایی که اومد نسبتا دور بود ولی خیلی مهیب بود
سلام وحید جان من سمت شمال تهرانم ۱۱:۳۳ دقیقه صدای انفجار دور ولی سنگین اومد
آپدیت:
پیام‌های زیادی درباره فعالیت پدافند در مناطق مختلف تهران دریافت می‌کنم.
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 506K · <a href="https://t.me/VahidOnline/76054" target="_blank">📅 11:33 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76053">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/tKzBdURTKuLwI0Hy_YOfkOOOc7CknKcfjGV_1NbeymxEofPs3nVUElk5evN5ESztrZ_bLGlB4bNGL0Z25juxsVCKpW7vekzdbMWBR3jZU5Id3BAtxHrXpOP_5W1dEXqDwkyuHwNIRDIAmlKSIMhwgXDikh0ulEDzmB8jTUTgB1jLDtiXQlN_ySMAx5VSN-CDyiKnaQflFF_57wEJKprVZm16t1YAusQNFXotCQfoA05LYi97PKfzFy3oCoY_Yi8eoWeZyzz2u445RYXQhFoAkfGjQi8rvY-M6mJhz8bmyY6qpyXE6yHWkJuEZeRbY0dFfjwtToviy72wJOMfbY5rQg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پست ایلان ماسک: "تنگه هرمز به نام اهورا مزدا از آیین زرتشت نامگذاری شده است."
elonmusk
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 439K · <a href="https://t.me/VahidOnline/76053" target="_blank">📅 11:30 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76052">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cOBe4gx7ghLCFad-o7396r48TiT08IPjCz_njorYOSp8AfaMqsRVWM7T50TZ0UwDEutJAxDLOYDafMsPpL-ivFuknZ--1fy3gwFf1BiPVbusO3IR8zjiwLp9xeAX8cj_RDCIv2S9VHBsUyvNvDjM6nmKH0befetm2nJmaXa_1p3sJTpRU_U1rUvz6adcI8KKsp5h1yX5kPhiCfs77YKW4ynO5PystzQXo1XYPd4pLFH_vDFxgy2EcvtMm68myiL2iN0lEb00itVEiYmSLzxVWFP2oNgtb_-p97pyibyOtnl6xstwIciPCo50KRovyETAEIC9pYjn1lzEuznF4Ut9Ug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">«اسماعیل بقایی»، سخنگوی وزارت امور خارجه جمهوری اسلامی، در نخستین کنفرانس خبری خود پس از آغاز حملات ایران به اسراییل گفت که اتفاقات ساعات‌ گذشته، به بی‌اعتمادی موجود میان تهران و واشنگتن دامن خواهد زد.
بقایی در نشست خبری خود گفت تبادل پیام میان ایران و آمریکا تاکنون در فضایی لبریز از بی‌اعتمادی انجام شده و به گفته او، آتش‌بس نیز «به طور مستمر و مکرر» از سوی طرف مقابل نقض شده است. او تاکید کرد جمهوری اسلامی هر زمان که لازم بداند برای دفاع از «امنیت کشور» اقدام خواهد کرد.
سخنگوی وزارت امور خارجه همچنین آمریکا را مسوول تحولات اخیر منطقه دانست و گفت اسراییل بدون هماهنگی با واشنگتن اقدامی انجام نمی‌دهد.
به گفته او، وزارت خارجه آمریکا حمایت از اسراییل را دلیل اصلی جنگ علیه ایران دانسته و جمهوری اسلامی از همکاری و هماهنگی کامل فرماندهی مرکزی ارتش آمریکا، سنتکام، با اسراییل در حوزه‌های دفاعی و تهاجمی اطلاع دارد.
بقایی با اشاره به تفاهم آتش‌بس ۱۹ فروردین، آمریکا را مسوول هرگونه نقض آن دانست و گفت پیامدهای تشدید تنش در منطقه متوجه واشنگتن خواهد بود.
او همچنین از «رافائل گروسی»، مدیرکل آژانس بین‌المللی انرژی اتمی، انتقاد کرد و گفت در صورت تصویب قطعنامه‌ای علیه ایران در شورای حکام آژانس، تهران «پاسخ مناسب» خواهد داد.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 428K · <a href="https://t.me/VahidOnline/76052" target="_blank">📅 11:21 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76051">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/025351cf82.mp4?token=WkekflisnLiPnKmRO1XVHG8Kb1Y4LL0VuihEbAMqgI3e_HDqp2PXv1jiYbThdF6Uh10ZRK4DsKVuUDrtv5sxiL_5dQbMzp0ydLVGpADLf5m2JN1GlaDQXb-kryyR06qKWry9CNu-CQiUUZX-YiVmtaPU6A4Ss3BDvAobHZMG-xuA-JvIq1UWHonJQLqMDsAwNNtSTy9xK6CJ17RemvuTTbDiLraL8_SCRhRyKEEsx_paJ2dvO7xeJjZ8sP2cI9qjORDflqu4CmeE8OCdWlFv4oh-yuFnbmBJgxibstRekyFrjlceIcBVpV4mOx1-QFd1yRifxnJZbFKgM77cQ8Sh6w" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/025351cf82.mp4?token=WkekflisnLiPnKmRO1XVHG8Kb1Y4LL0VuihEbAMqgI3e_HDqp2PXv1jiYbThdF6Uh10ZRK4DsKVuUDrtv5sxiL_5dQbMzp0ydLVGpADLf5m2JN1GlaDQXb-kryyR06qKWry9CNu-CQiUUZX-YiVmtaPU6A4Ss3BDvAobHZMG-xuA-JvIq1UWHonJQLqMDsAwNNtSTy9xK6CJ17RemvuTTbDiLraL8_SCRhRyKEEsx_paJ2dvO7xeJjZ8sP2cI9qjORDflqu4CmeE8OCdWlFv4oh-yuFnbmBJgxibstRekyFrjlceIcBVpV4mOx1-QFd1yRifxnJZbFKgM77cQ8Sh6w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اکانت ارتش اسرائیل با انتشار ویدیوی بالا نوشت: "در دوره اخیر، سامانه‌های پدافندی در چندین منطقه مختلف در ایران مستقر شده بودند، ... این حمله منجر به انهدام این سامانه‌ها شد."
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 399K · <a href="https://t.me/VahidOnline/76051" target="_blank">📅 11:20 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76050">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bQxYDHLFxpLm6jMZ-X-KalExbxSeit5jcAI5dICvXs0RKPnrVZFjcK8t9CiuPKhcIbTWngYuNSsiOnT33QyMOvq5KizO9mKYzCAnrpzWufOiDlPNLBBX7UFkhf73XUcqd84m-HrzVh2eAh0z1RfveBJkNnw1suI73HKvopZ9WzD9Iz4xa1PBTRe0D_B670qBoSOopOzjea25Bxk2TFSWqs5IPxwrLdZt0IysbNslSjoXkFCiHzarmYA1mLCvMVLQyE8WpdmMrYxQMWSAdP4HCkm5j2v4qXjBAIY9xYB9EJFmx48UIItty_ys-Eg2woP1mQ5FAEbJBexX1QZrEmR0GA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزارت امور خارجه قطر اعلام کرد «محمد بن عبدالرحمن آل ثانی»، نخست وزیر و وزیر امور خارجه این کشور، در تماس تلفنی با «عباس عراقچی»، وزیر امور خارجه جمهوری اسلامی، درباره تلاش‌های میانجیگرانه میان ایالات متحده و ایران و همچنین تحولات لبنان گفت‌وگو کرده است.
بر اساس بیانیه وزارت امور خارجه قطر، نخست وزیر این کشور در این تماس بر حمایت دوحه از تلاش‌ها برای مهار تنش‌ها و دستیابی به توافقی جامع که به تقویت امنیت و صلح در منطقه کمک کند، تاکید کرد.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 436K · <a href="https://t.me/VahidOnline/76050" target="_blank">📅 10:35 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76046">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/rlPPrOJ7pW6tspT17iXD0403adRYGedBJ5JyfEWALtJBvcJ_Ams06vLJLeFp4ffpAmDbWr1o8XNyu3lXEpGGsp0-Qf0-ACn4PGukMFlOakg5KFD9flQU3yjUQt0OAjWIHe07MWTeV270n4J0D4hnJvjW0GQy3dwMCod6AFt_goKjsBZE9qXu4XvrzasC4N_PubBctNxI5mEbbbliWuPuxYtKf31X6FEmsGbbu-XHY8pZ51oxUiWFkwZcrTvCMfqEpxieQGncrinb9IufIhaG1dgswdKa-IUTmSpKjy1Vw_M-7ilINo-0eYPE1bJvPZtDU2wbWE4xJ4A-xe54Fdonig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/NQeyd1se9fF9moXb0YVhhbrHYpYm9Wll7hzZ87jJg1WJHIxh3zpXai9nqA28BAhWqxllQCqOY3qegvBhmKla12OoyAIAO3ZjLpkNlIyYy0fiDcWc42lGBgCttondyJJU7GfWcb6PkZzTJspa-EBjyNVqDnFR9IJdD-AidAk-9gOhGOGxrVpP2zTBqSvT1DB3g7MRNlndl_pnGZIoJEtaUbGQa_b2ej8D2xhUiXr9UlPzTIc7hCcTSPlNI8W1x2_V5icVZqqM0cyHaasJI2ta91CpaXiHif2foi49tG_C9tzOvQB_-0ho2nhoIQZJsZrzOVl6ZnCyREd5bSsi5V15Dw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/HIvTlHixRGR8LQ1v8RORiB4mjGogvr7GmgtPtSJCllxZeyMssntkTvOwk4NRrlClnW0G2JzUiFaw351lF7ERAUuB1Jdud2eCP0VqJwPqVdhoijBsW7oYwpEkvImP1agnqtDjDchmjmKfagUfsyljPffbvFldm58bGBBWW3e6aDYQpGmtZ4OEf2goH458c8Xp80upqANipq49CGkQdI_j6NaY9h-_WtmxiUGg49OIHWzrcVjF_Oqvs0iy74tWoOmGbjbM4_WxQNBTBKSRR8JJIqpyyDjiMJ32LIcyd8niKESD-86YXWokUAPYJw7VjiHtYThGGaAN_eo27-tEtFeqVA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/551c6649bd.mp4?token=mdaD2rT-SevZsNIIXAxSoY0j3QHkWYXoyGIKUV2KEwzl9-dIzBV-OeYDJDGV7wn9-GGfuNRRoPPoEM-HtJI1VPPm158jVF0fxeLNvlPA9Ug3-cpOyOiwYwaFCDmFn0otA83luVkEanY2-_YFBY62qrAmSb5eHN3Z7dUFwK0Cssmv52rc9PMQ38RLVhkGwVrWKLUJWcQYzo0T90K7JQrhGFDOgyciFcIOIGzwaY8WciwzOUgOYp3QamX0jAZQprRMJRWkKGqXFd9tJXMY5ARSid_geMaQ3KFzMTOqmRBx-Gs7He3R7zNKYYTrITJs13R_xrOtQIDb3VAr3gEwkdidYw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/551c6649bd.mp4?token=mdaD2rT-SevZsNIIXAxSoY0j3QHkWYXoyGIKUV2KEwzl9-dIzBV-OeYDJDGV7wn9-GGfuNRRoPPoEM-HtJI1VPPm158jVF0fxeLNvlPA9Ug3-cpOyOiwYwaFCDmFn0otA83luVkEanY2-_YFBY62qrAmSb5eHN3Z7dUFwK0Cssmv52rc9PMQ38RLVhkGwVrWKLUJWcQYzo0T90K7JQrhGFDOgyciFcIOIGzwaY8WciwzOUgOYp3QamX0jAZQprRMJRWkKGqXFd9tJXMY5ARSid_geMaQ3KFzMTOqmRBx-Gs7He3R7zNKYYTrITJs13R_xrOtQIDb3VAr3gEwkdidYw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پیام‌های دریافتی:
ما کاشان هستیم
اینجا قشنگ صدای موشک رو حس کردیم که داره رد می‌شه
همین الان ساعت ۱۰ و ۱ دقیقه.
از خمین همین الان موشک زدن
شلیک موشک از ابهر ساعت ۱۰
خمین ۹.۵۷
وحید طرفای ابهر خرمدره ازناب زنجان موشک زدن ساعت ۱۰.۰۲
سلام شلیک موشک از استان مرکزی
وحید جان سلام ساعت ۹.۵۸ دقیقه یه موشک از ابهر زدن
سلام از کاشان هم همین الان موشک زدن
شلیک موشک از زنجان ده صبح
سلام از خوانسار صدای موشک اومد، رد موشک هم توی آسمون هست.
همین الان از زنجان دو تا موشک بلند شد
هم‌زمان پست ارتش اسرائیل:
ارتش اسرائیل شناسایی کرده است که مدتی پیش موشک‌هایی از ایران به سمت حریم کشور اسرائیل شلیک شده‌اند.
سامانه‌های پدافندی در حال رهگیری این تهدید هستند.
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 446K · <a href="https://t.me/VahidOnline/76046" target="_blank">📅 10:04 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76045">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/2e62b7f335.mp4?token=HXxlvs62QzJoWnuCPNPjTBPaL1BysQt0wPoZAyKdpLU5-po5zyDfv9B71b55WUmsbnN-xl9mXnHGla3FS7YfM3yBal2JNlEf_RlZUa3QgHGITl3HtV-YANZq_dWnyk60rH6G6QteqJRcoe_CFj1L7S_wjZQbxtBTppyLqqSdrAHf4l2Kz-0efyXgJh0vKsLEIiw9i66taPlxCz9GkFFbMyHCtEq2cuVieJ1fEWpniHf4OG8OntWNktnpBpWzKgYRuh7KkoICDZjZIRAvy8_ekeiPyiwiTdydqsj8Un_RRv0KWHkgqYRN4gGBDPIgkthqvgUe1Y9AXlM2NvCkzrDc7A" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/2e62b7f335.mp4?token=HXxlvs62QzJoWnuCPNPjTBPaL1BysQt0wPoZAyKdpLU5-po5zyDfv9B71b55WUmsbnN-xl9mXnHGla3FS7YfM3yBal2JNlEf_RlZUa3QgHGITl3HtV-YANZq_dWnyk60rH6G6QteqJRcoe_CFj1L7S_wjZQbxtBTppyLqqSdrAHf4l2Kz-0efyXgJh0vKsLEIiw9i66taPlxCz9GkFFbMyHCtEq2cuVieJ1fEWpniHf4OG8OntWNktnpBpWzKgYRuh7KkoICDZjZIRAvy8_ekeiPyiwiTdydqsj8Un_RRv0KWHkgqYRN4gGBDPIgkthqvgUe1Y9AXlM2NvCkzrDc7A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">لحظه اعلام خبر حمله موشکی به اسرائیل در تجمع هواداران گروه‌های مسلح شیعه در تهران
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 467K · <a href="https://t.me/VahidOnline/76045" target="_blank">📅 09:15 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76044">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mhWHrE5PdIKQhNmHZb-pKNAIO735Q1DjjLo3H58fswwdc_Ivhg_5Xq5aKXw0pXUSXbJOSYv3zHMfe8K0EFkhn0Z1O5g67NkPdJQv2s18ZX-70dMlq4S_2Ha0viXugjSSGYAeWmXMKXYTIoUjOyJ_ZhizBy1bmZQNapPvmymkaoW-Eyb2Y80RnwvF4wX-KoWER-n78e_ljyaJGVL_803QaLjEHd5n2kUKzTIhpeROjLFqUu8GFnx3oLc0bc_nFjrpbr0TfM84y0C-eUB8XpzT_XfDr6kfYVq9BSUwlpvOFeqQ9if7y0sf0yN-lvAW9pRdlXaLwbRXZPMFzK03onc5rw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ارتش اسرائیل اعلام کرد که تمامی موشک‌های پرتاب‌شده از سوی جمهوری اسلامی در صبح دوشنبه به سوی اسرائیل رهگیری شدند.
ارتش اسرائیل افزود که پرتابه‌ای که به یک زمین باز در کرانه باختری اصابت کرد، احتمالاً یک قطعه بزرگ باقی‌مانده پس از عملیات رهگیری بوده است.
در همین حال، پس از آنکه هشدار اولیه در اورشلیم درباره حمله موشکی جمهوری اسلامی صادر شده بود، برای این منطقه وضعیت پایان هشدار اعلام شد، زیرا موشک جمهوری اسلامی موفق به رسیدن به خاک اسرائیل نشد.
@
VahidHeadline
به گفته نیروهای امدادی اسرائیل، اصابت یک قطعه از موشک‌های شلیک شده از ایران، به چند خانه در یکی از شهرک‌های کرانه باختری آسیب وارد کرد.
در این حادثه مجروحیت گزارش نشده است.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 453K · <a href="https://t.me/VahidOnline/76044" target="_blank">📅 09:03 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76043">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/8e89e6ed06.mov?token=B-JJVE_zBGYvUS5_21-LhMlVMmiclF72EG4DI0fVlrDNF1rXG4PiYbl7hdYCe5kSHxCZw_AXz5yN4QFkp4JjwnOGFFWJ8IqGIA3kZqrJMdvCgUdXTmgrq0p--N1cDqtzSwY6_3fshn0T8ne_7cg1xuptHDE2vXkTBnn0QV9RxsdOkqAJQn3nMo_li6aTZZQ_Vo_FOoWatCpz2XxgmeZ-KvX2h8xd0JFittJcXkfjpuBQLtw_HuyEgGSvLw_0ihhY9sdSTltBT617V0rFs-hd5Ip833nkzmLOkg53zuzdf-VhWdludNV462REDPStHRgycK1In5ERtma7lTTPl3lpwQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/8e89e6ed06.mov?token=B-JJVE_zBGYvUS5_21-LhMlVMmiclF72EG4DI0fVlrDNF1rXG4PiYbl7hdYCe5kSHxCZw_AXz5yN4QFkp4JjwnOGFFWJ8IqGIA3kZqrJMdvCgUdXTmgrq0p--N1cDqtzSwY6_3fshn0T8ne_7cg1xuptHDE2vXkTBnn0QV9RxsdOkqAJQn3nMo_li6aTZZQ_Vo_FOoWatCpz2XxgmeZ-KvX2h8xd0JFittJcXkfjpuBQLtw_HuyEgGSvLw_0ihhY9sdSTltBT617V0rFs-hd5Ip833nkzmLOkg53zuzdf-VhWdludNV462REDPStHRgycK1In5ERtma7lTTPl3lpwQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">@
iliaen
ارتش اسرائیل حمله به سایت‌های پتروشیمی در جنوب غرب ایران را تایید کرد
به دنبال گزارش خبرگزاری فارس مبنی بر حمله به مجموعه پتروشیمی کارون در ماهشهر که خساراتی به دنبال داشته، ارتش اسرائیل حمله به سایت‌های پتروشیمی در جنوب غرب ایران را تایید کرد و گفت به اهداف متعددی در مجموعه پتروشیمی ماهشهر حمله کرده و جزئیات مربوط به این حمله را به زودی ارایه خواهد داد.
ارتش اسرائیل پیش‌تر گفته بود که مواضع حکومت ایران را در غرب و مرکز ایران هدف گرفته است.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 446K · <a href="https://t.me/VahidOnline/76043" target="_blank">📅 08:55 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76042">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/ac9a29e4c7.mp4?token=qOe0GSMBpTxS_HdRFdESRHSMIo7Z3oJmF-VQjm22n_F125QqyqfC7gVf1wTtEgcBpMYudFPZ1Ckvet7vvD75qduF9iE8-RCxs_bHuMIsBuk6IJtC8G855O7zKfZiHIcW39vMm8fpvU-R-NcuQtLtiHuCP0fcm7cOwSRQaa_NNZLeB5ZKI4BiFkkFsV5tchpJqNxCpxRQUtpne2NoB8rQzYPqsUpig2FOfR3UPlFizBycxsF1Qfw7JH5cu1CbR2XCK7D5T1l0CSge-U85LxPJdpKT5ZXtw8zlU9_HmTEKG9G31QXR9etvYG_t35EGMvJeYF7JtrUUsfn4IqNqIPC8dw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/ac9a29e4c7.mp4?token=qOe0GSMBpTxS_HdRFdESRHSMIo7Z3oJmF-VQjm22n_F125QqyqfC7gVf1wTtEgcBpMYudFPZ1Ckvet7vvD75qduF9iE8-RCxs_bHuMIsBuk6IJtC8G855O7zKfZiHIcW39vMm8fpvU-R-NcuQtLtiHuCP0fcm7cOwSRQaa_NNZLeB5ZKI4BiFkkFsV5tchpJqNxCpxRQUtpne2NoB8rQzYPqsUpig2FOfR3UPlFizBycxsF1Qfw7JH5cu1CbR2XCK7D5T1l0CSge-U85LxPJdpKT5ZXtw8zlU9_HmTEKG9G31QXR9etvYG_t35EGMvJeYF7JtrUUsfn4IqNqIPC8dw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اصابت موشک به شهرک یهودی‌نشین ایتامار نزدیک شهر نابلوس و در بخش شمالی کرانه باختری رود اردن
FattahiFarzad
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 452K · <a href="https://t.me/VahidOnline/76042" target="_blank">📅 08:09 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76041">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aBR5wayG9A9lSu0zaWjXZw1PlRbYCdJsk5l0t5XkN4zP0-6CK90GKukwxrvZwWq8UXLH4m5EKthgJgcf4dZqFmxvV_uMPEEITdpLY3sJ8xEAoU3-Z_QjGKJSg-D3dwuFlj9p2t1rchsNgmoFkw-0LdLrx-gi5FTPkMBCGZGOpt5z6CmfVZSVuIiYUldK1CV2pC4SJjm3H-4szcSDkXxUsoQHTaR0Xq5Og1Gjh3GDgLyM4515PaOXRb4o1Un87EtKeNbHuMqk4K2Fj2PxeeJDacaHPkICqP_VGplVDBUlT0sRGmuExjLABuHK5tA0ZufEqVwqWQc7Q2L91AK-ej5rAA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ارتش اسرائیل بامداد دوشنبه از رصد موشک‌های پرتاب شده از سوی ایران به سمت اسرائیل خبر داد و اعلام کرد: سامانه‌های پدافندی در حال رهگیری این تهدید هستند.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 428K · <a href="https://t.me/VahidOnline/76041" target="_blank">📅 08:00 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76040">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">پیام‌های دریافتی در پی گزارش‌ها از شنیده شدن صدای انفجار در ماهشهر:
وحید پتروشیمی کارون تو ماهشهر زدن
آقا وحید سلام پتروشیمی کارون منطقه ویژه ماهشهر زدن دستور دادن کارگران و پرسنل برگردن خونه هاشون
سلام ماهشهر پتروشیمی کارون ساعت ۷:۳۰ یک انفجار رخ داد
وحید جان منطقه ویژه ماهشهر صدای وحشتناکی اومد. میگن شرکت کارون رو زده
آپدیت:
پیام دریافتی: کانال ماهشهر هم اعلام کرد
پتروشیمی کارون رو زده
اما صدای انفجار مثل انفجارهای قبل نبود
همه نشنیدن
معلوم نیست با چی زده این بار
🔄
آپدیت:
خبرگزاری فارس، نزدیک به سپاه: " تهاجم هوایی دشمن صهیونیستی به شرکت پتروشیمی کارون ماهشهر
حیاتی، معاون امنیتی و انتظامی استانداری خوزستان: دقایقی پیش شرکت پتروشیمی کارون ماهشهر مورد تهاجم هوایی و اصابت پرتابه‌های دشمن صهیونیستی قرار گرفت و بخشی از آن آسیب دید.
خبر تکمیلی در خصوص خسارات و تلفات احتمالی متعاقبا اعلام خواهد شد."
‌
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 422K · <a href="https://t.me/VahidOnline/76040" target="_blank">📅 07:53 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76030">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/eCLt7IZL77KShOuYb0l9Do389fnvgvKmrNGRCXsohyMcbsoQoVakuWPUgnX6oHqvnI33_O0gvKxP9YrcoJS3eK1yXfY3UU85FYMmnSFLEbz_ZB1drDPB0zfhYiHY-5bp6y7-1KvvA5XXnjGm-8z9w694u2BTRyo0XoKpg496g1sDTC4_gIjuO7v_y-AURRpfdMQz3j1Yc7gWqi3Q9SPc8IgdwVi5j3lzGUjZmzB4-WbBDR3rr7ac5IASJdmOKne_XnS0gMwKCDZVY7_NFZ-kP4rK92xx0ELXOesHOgXPrIujhbe-bDHFx0v9jL9A1FrRujkmUAgFbMAxNLn5XYo-Ww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/pecAYElhVz4BG_NJCVwNEHtLX7UahrrByDsHd02298htu_0JNLdwQ7Z8RJ_vJpV8r9zJJ-Ar-w0xaiD2pg2_V1MWvOHU7KBqVbvrFhRGGN4M3MCCXcW2V5UVEcgFmRK5fOxYwKvlcDWqFauuhLYsq-dQ3Wbv-A8gQeb8oL4gKq-7E5gc11y_hMAUZ4r40sMsycA5Ew8uoc5YGrH6Zf6Z8dre8VEpL1z81eKiM2v8hdyNg1GWRe9PDXVH3B5mxv-yAtvCMg73rmTN4XzL6pnfipphl4PtVqHe-YfxfOVyJlbKuOr0IKILsqCbmVX-WsSBS4HCA72vbgE1OcUxS7B4lw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/VI22V4Axc52GtwUo2KiOZEPaRO8Yzyqz9Ezhvr8JHaORMnLdusy-q6FYQM9c5pG-aE4tqrOdWTmiEL5qe8si7o9h3anhYSE7GtYoZ5LXTOJ0KtxSwxGkmLRzxWOiB0WRNFKpkQpNgE1g7GaHJ7kSkQrh9oZhERJBttNwynXsHzlvwMDtETDBZ6-08MDJvbN5h3j9u3B46fh3NrFBom8loT71IYOn1y-KCRsGO2lGg2_FpjR_OMt07j5amckOwo0yfe8mYO0vJR3yKCYTE0CHMqtnGzUe1pmqeOR6hKkGf76v2qIXj8e8CXoCq8SZxN7jS5BILsF382uCBsF6Vax0Hg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/KUiqLRNS-eYJP1eaGJYxcxcZdWtg9TAKnHugN1rGCtvBr07y3HMObxT6RqPxNLPC6haaHHS80YekliN5gxKHQrVHyxSiss8TE5kO907F7gducxpThZYBMUEvo9iXWwTyE6a9luTfC1iH5fjpwVpDXwI5-iCyXoavtkcweossq4Be-kmW86JWSwhKyZQvSMRu7pwxT52Bui0xQOWsb4QrIFfXHEsgas7Ugl8HFPcrVvvnIAzuIjva7qesK_d-0HPgYio948o08Pf7KLT_MbUUYVTNBYJ35dkhFbw-7n9PM5n5kwVD1QX0coqPHmD2kPr74DO5FjushHdAi0JDLOuAJA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/D6jQhhMusmHau6VxoqMl8Xhj1gJr1xXUa94F7uwG3KyJ2OcrYy5iflNsokNpMfyl9sEM4tYz78SPBzLihqBmpuKVvSPVkQZv0-pRe054se11JFC6Kkj_UiB51hvTuq5k21XToTAQzqgXBR2rrkCBAjJSyD1Yl_u9SnAxe_0cSo-Hvwhv5PI5GAqlIPm5_egYz-j35pkdqXkOxaCPveRmYg4C_8ob0PnlbRfxWsmr92DxzeK59W7c4oChIC8dbchRDPyXQBtYD0aXHzU7sr1e010K41fP1KS6CJOTEWyPmbaZPPWRHTBwlZIsPrC0YG48Exh_Q_zqyeIsEBSoXpavBg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/08feac2b13.mp4?token=vrsA-bdIB0h45HSAxHWA9rUE1ob0E1QjlhOnj3vsQ2Jbl1HW52jCRp-ItKf-1qtUTW_DKhkRACRaDxD8qxGSS_anB7Eafbr9rvFbhez9xpLURKbyHt1nHsdn2ZWVhyUJIMwTdd1D9UdBZlpauYbyewVYmcg451LZoMPe2cP_o0AdPzdeL5Mo_GkaI1S06tNlWXZpwJ_Z22xLTiDxxjerG6f7iO_O_Sqw09jMKh7f03cFoWEq4dldnWb8HWxGNxNtx492LVv9VwaFLsTL_gVUa1KSe235D-eV5EXlWFLb1uX1EQhIvzH7NuIw8lbSPcSd8RhWv8ywrgZZhS4CHt796A" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/08feac2b13.mp4?token=vrsA-bdIB0h45HSAxHWA9rUE1ob0E1QjlhOnj3vsQ2Jbl1HW52jCRp-ItKf-1qtUTW_DKhkRACRaDxD8qxGSS_anB7Eafbr9rvFbhez9xpLURKbyHt1nHsdn2ZWVhyUJIMwTdd1D9UdBZlpauYbyewVYmcg451LZoMPe2cP_o0AdPzdeL5Mo_GkaI1S06tNlWXZpwJ_Z22xLTiDxxjerG6f7iO_O_Sqw09jMKh7f03cFoWEq4dldnWb8HWxGNxNtx492LVv9VwaFLsTL_gVUa1KSe235D-eV5EXlWFLb1uX1EQhIvzH7NuIw8lbSPcSd8RhWv8ywrgZZhS4CHt796A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پیام‌های دریافتی:
۷:۴۰ پرتاب موشک از بیدگنه
بیدگنه شلیک موشک بالستیک همین الان
همین الان ۷:۴۰ موشک از بیدگنه رفت
دوباره از ویلاشهر نجف‌آباد موشک زدن
وحید جان همین الان از کرج موشک پرتاپ کردن
7:39 دقیقه از ملارد صدای پرتاب موشک
یکی دیگه همین الان اصفهان
شمال اصفهان یدونه موشک دو دقیقه پیش پرتاب شد
الان دوباره موشک زدن ٧/٤٢
اینجا،اصفهان یک بار ساعت ۷:۳۰ دقیقه یک بار هم الان،۷:۴۰ موشک پرتاب کردند.
۷:۴۰ از سمت ملارد انگار یک موشک زدن.
وحید همین الان از جهانشهر کرج صدای پرتاب موشک میاد خیلی صداش شدیده.
سلام وحید 7:40 صدایی شبیه به برخواستن موشک از نزدیکی مهرشهر کرج
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 400K · <a href="https://t.me/VahidOnline/76030" target="_blank">📅 07:46 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76029">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/VQyg2mFMkjmfyr0LXos0ZQaM9ZBv-fTXw8QD589Degt24De-wcRIg2XEJV-q5NoqVZV24MNH7EjVmCZBzhYUpfaqGJG5O2utv3BCWDqgPC84yAJ51K_aTyemqWNCgkhLcnX7W7Ax3pGpSLEfrjb3j4mXTch1R_7ygYgYKNHXOrzy-E5WOAtRIkXqOmr8kED2K7TE0ANla9DWs2Vg1_T5-oDq83WHw31Qkq0J_1k863Mi7lKg5KMeiPc3Qebem3pS6QoBzKlybEdhSktx7SjdB-QmUBaoAC5bYZPJqUkZT2wJWai5h2J1u5n1ekMf91rHPvSZy973IeRSZtGj_8j8Tg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پیام‌های دریافتی تایید نشده:
۳تا موشک از کرمانشاه همین الان
وحید کرمانشاه همین الان صدای وحشتناک اومد
سلام ۷.۳۰ صدای انفجار از کرمانشاه . احتمالا پرتاب موشک
سلام وحید جان
7:28 بندرماهشهر صدای انفجار اومد
وحید 7:30 دقیقه ارومیه یه صدای سنگین اومد
الان ۷:۳۱ از ویلاشهر نجف‌آباد موشک زدن
الان کرمانشاه صدای انفجار شدید
شلیک موشک از ارومیه
خرم آباد 2 تا موشک از پایگاه امام علی انداختن
از ارومیه موشک فرستادن
پرتاب موشک از نجف آباد
اصفهان شلیک موشک
سلام وحید جان از خمینی شهر یکی زدن
آقا وحید همین الان شلیک موشک از فلاورجان اصفهان
شلیک موشک از ارومیه
با صدای انفجار زیاد
سلام وحید آنلاین همین الان ساعت ٧/٣٠ از اصفهان موشک زدن
سلام وحید جان همین الان موشک زدن سمت اسرائیل از اصفهان
موشک الان زدن از پادگان پشت ویلاشهر نجف آباد
سلام ماهشهر ۷:۲۶ دقیقه صدای یک انفجار شدید اومد
از کرمانشاه ۴ شلیک، نه ۳ تا
ماهشهر حدود ۷:۳۰ صدای انفجار اومد
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 373K · <a href="https://t.me/VahidOnline/76029" target="_blank">📅 07:31 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76028">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tIU14Z-_KarbrWrynZP6cykdcz-D5CnU_0ZEdlBe70TU6SdXj1ywfbyyqx3HziYC8SH20DhtukaKfcaNtGORsRb7QKBV5u32b4WqAN6BJUYw3K3WWGpkBbzOmc3uu3CuzaQPD3bLwy3qeNiKF2VhV7JDLw7LtmG--S7tmYajq0pYKQDZenmQACKZT_j9VJ_y0of4CAe2-U96JZsOXZ8tideJhgZZRT3IO0QmFuCMtU3rYRK5B7z5urOB_cCd-Erv86gnHhSmjWSL3-1ANimlWhTJbHmuwbgtWAnU9k2LCbEneJzJ_oVU8Oib4_hQblPwkVM09uEPhpuXt5fRNTXe2A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ساعتی بعد از موج حملات موشکی ایران به شمال اسرائیل، خبرگزاری تسنیم، نزدیک به سپاه پاسداران، در تحلیل و تفسیری درباره ابعاد نظامی این حمله گزارش کرده که در حملات موشکی و پهپادی یکشنبه شب، سپاه پاسداران از «پهپادی ناشناخته» که از موتور جت بهره می‌برد، استفاده کرده است.
کارشناس نظامی تسنیم همچنین از شلیک موشک‌های خیبرشکن با کلاهک‌های خوشه‌ای در جریان این حملات خبر داده است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 350K · <a href="https://t.me/VahidOnline/76028" target="_blank">📅 07:23 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76027">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rg1uhIcUHcirweXmiww7G4iHn-_GbZpQOY2Vn8YH4hHW_G7QmgjxFCjNxpve6yvyEHqHu9wllYgD6oNEyEldi-wda9HPl9Pj8Ph9KWI5sPqDh8q8j5RBDWzGHbWyQxb9FXItbcU7WRDD51MbO84oVamcrK5Q1GLN1voLABGZzag4xuo25ks8vD702IfSpH1GBwjvFizZh5fuWKf6zwOvj1nRL3YAW4RKeTl0x30AMl8UG4eVMVLOMuH3HBRifrhSeTuoe8ehcG5sw6gw-iG5A-c_wWdjAu-nLa5i4o9504xgj6wbitIgd0rghA7FfHNYCKLhlT5ev_35hphaUOXJog.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یخیئل لایتر، سفیر اسرائیل در آمریکا، در پیامی در اکس نوشت: ارتش اسرائیل پس از شلیک موشک‌های بالستیک ایران به سمت اسرائیل، سایت‌های پرتاب موشک زمین‌به‌زمین و همچنین زیرساخت‌هایی را که به بخش انرژی مرتبط نبوده‌اند، هدف قرار داده است.
لایتر افزود: «ایران امروز ۱۱ موشک بالستیک به سمت اسرائیل شلیک کرد. هر یک از این موشک‌ها می‌تواند یک محله کامل را با خاک یکسان کند و صدها نفر را بکشد. هیچ کشور دارای عزت‌نفس در جهان چنین حمله‌ای را تحمل نمی‌کند و اسرائیل نیز نخواهد کرد.
سفیر اسرائیل در ادامه نوشت: «مردم لبنان، حزب‌الله به‌عنوان نیروی نیابتی ایران را رد کرده‌اند و به ایران گفته‌اند از کشورشان خارج شود. اگر حزب‌الله به اسرائیل شلیک کند، مراکز فرماندهی آن در ضاحیه به‌شدت هدف قرار خواهند گرفت. این موضوع هیچ ارتباطی با ایران ندارد. همه از این رژیم ایرانیِ دیوانه خسته شده‌اند.»
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 346K · <a href="https://t.me/VahidOnline/76027" target="_blank">📅 07:20 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76026">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HDM2neptRwqXsJlTXGI3dkJsf24Yny-YaX3wLm7t_HtoE9J_5KyQBsaksas6STg3ZqYNQiGzNcQ3Uk9zhzDp391wNZn4KleQy2GgFGJxR11hAEpAZtYMHL4u-IM8K1913Pn22xcupxdSAOe5X1bv5soFTqXVzISM7OXTqAq4U0omhV9JN2KThr-NTIaDH6SshRDr8HGiDF8F0FCDvcmAN_S2bvL7KA8ExHVlvC9LmZMCcnBfDDkWPQSIUz5wqOhpZwRcmycNHEqW04Tde_yXgHx44tg9hQcSgU2wZ4pXZNrG9jGXsULyFrcuUgevbrNwZ4MUkixUpYidaH-YVPTKCw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔻
یک مقام آمریکایی به رسانه‌های این کشور گفته است که ارتش ایالات متحده در حملات شبانه اسرائیل به ایران هیچ نقشی نداشته است.
نشریه آکسیوس به نقل از یک مقام وزارت دفاع آمریکا گزارش داده که این حملات اسرائیل «نسبتا محدود» بوده است.
این گزارش در حالی منتشر می‌شود که دونالد ترامپ، رئیس جمهور آمریکا، پیش از حملات از بنیامین نتانیاهو، نخست‌وزیر اسرائیل، خواسته بود در بحبوحه تلاش‌های دیپلماتیک جاری از اقدام تلافی جویانه علیه ایران خودداری کند.
آکسیوس پیش‌تر گزارش داده بود که آقای نتانیاهو به صورت غیررسمی یا به تعبیر این رسانه «تلویحا موافقت کرده بود» که این درخواست ترامپ را بپذیرد.
حملات شبانه اسرائیل ساعاتی پس از شلیک موشک‌های ایران به شمال اسرائیل انجام شد و در حالی صورت گرفت که واشنگتن همچنان می‌گوید در تلاش برای نهایی کردن توافقی با تهران و جلوگیری از تشدید بیشتر تنش‌ها در منطقه است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 366K · <a href="https://t.me/VahidOnline/76026" target="_blank">📅 07:20 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76025">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/kcfELKgvQkhDrJaepSIejYe9D8tmauxmLgPYadU3rql8uba3uTvdDcuF1E2wOnKqRpJX2bPS7BgPa-ZbRvdFqHrVHqfnpfQYjTqKBzf_IiUkMPcR9Eyn27h5AQvnQGurf7t66BGEQ2E-jdwH8Ohp0OPRueeW8GS-rhP3JecU6e7lJxXgRKCa23M9dFS6jNIyGlYxlZk-BNvFODDfx8pSZ9mRyI017YPcN1Qm5thBX6L4FWt5sQ0Xx8Yl0Nia08Zdd2iVDdPzmCOLrbzucTfELgdKCAAF_6Fad5Xzbleivqg_Uf9ibb5lGdy9F5r18JwSllQUdXOM_dxwG9fZbSusaQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سخنگوی ارتش اسرائیل پس از حمله‌های یکشنبه شب سپاه به شمال اسرائیل و حمله‌های متقابل ارتش اسرائیل به غرب و مرکز ایران در بامداد دوشنبه اعلام کرد که ارتش اسرائیل یک موشک شلیک شده از یمن را رصد کرده و سامانه‌های پدافندی در حال رهگیری آن هستند.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 361K · <a href="https://t.me/VahidOnline/76025" target="_blank">📅 06:35 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76024">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/vai3Os2Bg26YdQuAHO5XgNmQNZkhgL9v0_ELsx3QXGM1pTbpsv7gsaxVpkl6UcZ2wXP84-ktApTfeq0AOVkT5am_hdKXwW6zrgIT1JvgxkxlfvnMAhqKewGcNule84DkKnaFYQbyjRQKWg95j1MKTHsoyu5YzyX91Zq3BTjVl8DqNjWRneHe2PgoN4PIaVCWdytL-ZXdeR-W303t77K88t9bGV9bPpJNHcKW--6su5HE9o0cNrC6-VrvAaaIn0ciPN4_TMHzasOzc01o-RKsVUB-oRrjs17zgiiEwVA7Pcrw6ZIfwRyxoSzdfJBOKKR7sT_b0yf-2AXcIwJkq0R-wA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آسوشیتدپرس گزارش داد که عربستان سعودی در منطقه‌ای که پایگاه هوایی شاهزاده سلطان، میزبان نیروهای آمریکایی است، آژیر خطر موشکی به صدا درآورد.
@
VahidHeadline
آپدیت:
خبرگزاری صداوسیما، وابسته به رادیو و تلویزیون جمهوری اسلامی، به نقل از «یک منبع نظامی» اعلام کرد که جمهوری اسلامی هیچ شلیکی به سوی پایگاه هوایی در الخرج در عربستان سعودی انجام نداده است.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 359K · <a href="https://t.me/VahidOnline/76024" target="_blank">📅 06:09 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76023">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cBzyDgG8Ii8P74iIffBW85hLpthblHZNvYrZKhDpanen00mHEyjyrsrR9qkwoUwyHizS3DramtTV-1Z44OEWx42ylRtL6Dbv78e7LQ1BZGuIVNJbVtLgCsmjuA-g8829eVIPO06h8qmweJapW4IWX4bwDV2neg_vNCttDSQ-mH5b7fKlQl0xbVXR30LCZkRXXH_BVwxL9N65pBRuvMdu5jNYrlDLUzxEXTWLrZgVvRhBTGyHio8X_-OSmkraRS_xmJT88OXFk5NUWy7A2nSt-81ZTOJsqDph-bRgKMTaCwg5AZ-R18dudCwA0nY0Rz2kfIJ4hoORt51UHH-KwGkMSA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آتش‌نشانی تهران اعلام کرد: صبح دوشنبه دست کم صدای ۲ انفجار حوالی ساعت ۴:۴۳ و ۴:۴۵ در نقاط مختلفی از غرب تهران شنیده شد و ادعاهایی درباره هدف قرار گرفتن فرودگاه مهرآباد منتشر شده است. سخنگوی آتش نشانی تهران از آماده باش آتش‌نشانی خبر داد، اما اعلام کرد که نقاط شهری در تهران هدف قرار نگرفته‌اند.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 354K · <a href="https://t.me/VahidOnline/76023" target="_blank">📅 05:57 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76022">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/V3K7pvZQJ74HSIheHcOx-MLuS8SHCuLe07L8FoLxQIw9ZkEc256jGPelgVYbglJf-gonhzD_NdaESNMeihW5kqIdN92Z4GFbh9JMXlJxrmHpSXABbFfH-262roRvR8s8ceYU8X2xyMnG18QT9_vsH1FaHQJcdcLkiTdtv9J__hSUxzykUhqA-qnXRka79IMRtWwuEK_go_Nq6JLCfW82nxadPMBv-ZlG0e-p19ExleDmBSzAWReyPI4nhtI1TOUS4L6EI7c9-Ma7YZb_mxeajsBfiERVU0I_P4EF-RA685vq75cz12M-3i6l1sgjKK9PadcYycMltPEiVItQNwKuVg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یک خبرنگار اسرائیلی حوزه دفاعی به نام امیر بوخبوط می‌گوید که نیروی هوایی اسرائیل صبح دوشنبه به ده مکان در ایران حمله کرده است که از جمله سامانه‌های پدافند هوایی و موشک‌های بالستیک در آن‌ها قرار داشتند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 340K · <a href="https://t.me/VahidOnline/76022" target="_blank">📅 05:51 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76021">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/UoXo4XwKDxkbYKmbSyqu1RwfWNC0xf9CdadBcuT8t-P7x-6Sl7uZIEJw6I8KqPZeXfVQkGqmy-t_iZkpwc4fTI63iWQE0_D3gQ78U0XPkb-_Lj3WSsJUotbbKdFoR5i9SDxEDGLf0bz2PRnF-r9TX5vqcVYB1DMwv_od4xrBXAC7e0ei415B37qt7NSP6bBjdIBqVWs5u_g00H2OHXKg_KVbeevBr1HQuthjcACu4FSa52cOAAdg-jIkImmEDalVeWNNlBQoS9gfCQbcThHnPuBOEeKGVBccgSDRUOp46r25iY587A-a3Q_rXZuPNXF3LwRpDx6WioGfG8br1jjZkw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">درپی اعلام حمله هوایی ارتش اسرائیل به نقاطی در غرب و مرکز ایران، سپاه پاسداران انقلاب اسلامی بیانیه‌ای صادر کرد و نوشت که اسرائیل «با استفاده از موشک‌های بالستیک هواپرتاب اقدام به حمله به اهدافی» در خاک ایران کرده است.
ارتش اسرائیل حمله هوایی به مرکز و غرب ایران را اعلام کرده اما هنوز نوع سلاح‌های به‌کاررفته در این حملات را اعلام نکرده است.
خبر این حملات درحالی منتشر می‌شود که یک مقام آمریکایی به اکسیوس گفته بود دونالد ترامپ، رئیس‌جمهور آمریکا، روز یک‌شنبه در تماس تلفنی با بنیامین نتانیاهو، نخست‌وزیر اسرائیل، از او خواسته بود فعلاً از حمله تلافی‌جویانه به ایران خودداری کند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 332K · <a href="https://t.me/VahidOnline/76021" target="_blank">📅 05:43 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76019">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/iTbYht3G06viGWpYjwBS0EUwkCe6avrx6Hqno9EJQJiJpNQZFgzMtJZI3ZYjR58bCc0_C-3TJepuZIncOIbxBVGqB4i6QAbC5ZmhoQqkDmzPzx4SaesVJSaYkwj0pnS_Tb4ADN8LU2oMFvdLzJth__ixB_7vq_qEh23yXud81cyBl_moqyrwUHqyecbE5sDFwywr0bGWGwdNbPPHup521Jmg7-jeFca-QNuYE0mzrTJvXAuB-GxH9s7G_9gLnRPB-_16yDv5YkYzLhguoy4PBKWpb9DYG4P9LhurS4jcCC_adL_cXpyY9ZqN5X4m4zhE7QBaZBmYFHQSCwwIjOJJVw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/itceta9F42w9irAQbHoGRKO7VvHu5iezQs6nhZMYtTyv50GRemHevdBwVOY4HYmTeRyBvzpYt1_rfpe9vjiHejqj7qE5kGfYRzutJyO3Az5fzIXIF8NQHfTOtnGZrIUHSfuzuhHO9aazobsvsATHRGR1xg11ozHX7SIzI-jo5y-x2FiziwpamCJCsWiENX1kEsHOxmaFttBCWZQOCeIrdV2HnC0p_-eXgjIheNTOtQqFgb61mHhOCHydi_fZPh6mkvblCP3p8e_5fnEZmQiHLgckO_iRgBx3p7a4CS4v3JlEtEZ-_qIQ2uXhdJNfjmJKgRMvbrQwAUWT5cbRm2fZTQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">کانال ۱۲ اسرائیل از حمله نیروی هوایی این کشور به فرودگاه مهرآباد تهران خبر داد.
@
VahidOOnLine
درحالی که هنوز ارتش اسرائیل اعلام نکرده حمله‌های بامداد دوشنبه در پاسخ به حمله‌های یکشنبه شب سپاه پاسداران به شمال اسرائیل را با چه تجهیزات و تسلیحاتی انجام داده است، کانال ۱۴ تلویزیون اسرائیل گفت که جنگنده های اسرائیلی اهدافی را در ایران هدف قرار داده است.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 331K · <a href="https://t.me/VahidOnline/76019" target="_blank">📅 05:42 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76018">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/mo6uTOaArz4jAGbdShX6V3y-jIlPiCk6XU9RAE7XGyxPbqMDvXKLhRFFOTPSs5lCFVJxa7hGJxfZw7V4ohBSH2BoObOwUKBxt3o-dv_j7QZfJamZABaArq_It3NFrNgoPIJErMD0ewf5vW6Iz9n5NqEUud_3fx7SweCshKPl5IDFqMeuFxSZog8MbPEgEgkfx18CB9m7DMWulXNdxOgz4Y0R_yBmXaJC_RTkmcErJy14j0Dm8BazTLZPKjCb6mZSInuyIflIxeCyhFwu7nYT9XaKWII57ATgKoUNgJlmlJ97ZqCFxuKbzEROMaJCbG9cVUdsVmZ5BNPDJf92naImqA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👆
نجف اباد ساعت ۴:۴۰ فکر کنم با پهپاد زدن
سار پیام‌های دریافتی:
کرج هستیم الان  دوشنبه ساعت ۴:۴۳ دقیقه صبح  از راه دور صدای انفجار بسیار بزرگی اومد
سلام وحید سمت شهرک غرب ۴:۴۳ دو بار تا الان صدا اومد خفیف بود
ما رباط کریم هستیم
ساعت ۴:۴۵ صبح ۴ بار صدای انفجار اوم
وحید ساعت 4:44 صدای انفجار نزدیک سمت جنوب تهران (باقرشهر)  شنیده شد طوری ک خونه لرزید
سلام،چهاردانگه دوبار صدای بلند اومد ساعت ۴:۴۳ دقیقه
سلام وحید سمت مهرآباد ساعت 4:45 دو تا صدای انفجار شبیه دوران جنگ اومد
ما شمال غرب تهران چند دقیقه پیش و دقایق قبلش صدای انفجار مهیبی شنیدیم ولی دور بود. صدای جنگنده هم نیومد
...
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 313K · <a href="https://t.me/VahidOnline/76018" target="_blank">📅 05:42 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76017">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/YrgqUscBntjbBn1VdWnGyu0h9qdr1fja6W_FWMvedYzPYKHG6PgG3r1WwjY-q62oWrG8JcjXMtSXxuATIMTdOUX6iBRvFcvp8zLsQekox4hAjei-qT_U5GVPKTR6SHAReRsmB7krIHzq_njNFWiw1d_k_honHmaXXvXrDxXy0SBQLMKyzbJvFSR4meX7DCxbnBC68iXcLK13b2pzRXdJxTJO1epDA4YukEZPeYFWvYM8xXZeefTs3B1biLxYjALUD5UUTOBhnDQWDF3rUvqU4U83W5ae0tifdgv1Z89kOLh5rxzw2DEln8b6wqqjx4tHr_i7LvyuRSdaiXTs16BbJw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👆
دریافتی با شرح: نجف‌آباد
سایر پیام‌های دریافتی ساعت ۴:۴۵
سلام ساعت ۴:۴۵
سمت خزانه دوبار صدا انفجار اومد
صدای بمب جنوب تهران ۴:۴۵
سلام همین الان صدای دو انفجار از میدان المپیک
داره میزنننه
فردیس کرج ۴:۴۵
همین الان صدای مهیب سمت مهرآباد
ساعت ۴:۴۴ سمت غرب صدای عجیب و بلند اومد ، لرزش خفیف سعادت آباد
تهران اندیشه
دوبار صدای انفجار همین الان
سلام اصابت موشک غرب تهران تا الان دوتا انفجار 4::44
صدای دو انفجار با فاصله کرج
ساعت 4:43 دقیقه غرب تهران صدای تک انفجار
دو دقیقه بعد دوباره صدای انفجار اما دور تر
صدا انفجار داره میاد سمت غربه انگار
دوتا صدای انفجار غرب تهران
تهران زرگنده ساعت ۰۴:۴۳ صدای دو انفجار اومد
الان ساعت 4:43 دقیقه و 4: 45 دقیقه صبح غرب تهران صدای انفجار کوبنده شدید
همین الان دو تا صدای انفجار در اصفهان شنیده شد.
سلام وحید. شهرک اکباتان. صدای انقجار اومد دو بار همین الان. ساعت ۴:۴۳ و ۴:۴۵ دقیقه
صدای انفجار , کرج , ساعت ۰۴:۴۲ , ۱۸ خرداد ۱۴۰۵
صدای انفجار , کرج , ساعت ۰۴:۴۵ , ۱۸ خرداد ۱۴۰۵
کرج صدای انفجار 4:45
جنوب غرب تهران دو سه تا صدا مثل انفجار از دور اومد
صدای دو انفجار مرکز تهران ۴ و ۴۵ دقیقه صبح
یه صدای گروم مانندی اومد اما دوره مرزدارانیم ساعت ۴:۴۳ بعدی ۴:۴۵
سلام وحید جان ساعت 4:40 دقیقه رباط کریم حداقل 4 تا صدای انفجار اومد
ساعت ۴:۴۳ و ۴:۴۵
۲ تا صدای مهیبی اومد نمیدونم چی بود
سمت خیابان زنجان
زد صدا اومد شهران ۴:۴۳
دوباره زد
نزدیک نیست ولی صدا میاد
۴:۴۵ تهران شهران
وحید ۴:۴۳ صدای انفجار دریاچه چیتگر
کرج مهرشهر دو تا انفجار به همراه لرز ساعت 4:40
احتمال میدم سمت فردیس باشه
وحید تهرانم سمت شرق یه صدا هایی میاد شبیه انفجار ولی نمیتونم تشخیص بدم
۴.۴۵ دقیقه تهران سمت غرب ۲ تا صدا انفجار
سلام غرب تهران دو بار صدای انفجار اومد
سلام وحید ساعت ۴:۴۵ دقیقه شرق صدای انفجار اومد.البته دور بود.
وحید ۴:۴۲ پرند صدای انفجار مهیب حداقل دوتا
سمت م معلمم یافت اباد
همین اطراف بوده صداش همراه با لرزش بود
دوتا صدا انفجار 4.43
وحید جان ساعت ۴:۴۵ سه تا صدا شبیه انفجار سمت غرب شنیده شد.
وحید جان شهرری همین الان دوجا رو زدن شیشه ها لرزید
ساعت ۴:۴۵ ۱ انفجار دیگه شنیده شد
دومی صدای مهیب تر بود
جنوب غرب تهران سمت تهرانسر همین الان صدای دو تا انفجار اومد حس میکنم موشک بود
سلام تهران سمت شرق و غرب صدای خیلی بدی اومد
۲ تا پشت سر هم ساعت 4:43
مرکز شهر سمت ۷تیر. ۳تا صدای انفجار از دور اومد الان ساعت ۴:۴۵
وحید جان صدای دو تا انفجار به فاصله یکی دو دقیقه حدود ساعت ۴:۴۴ از نزدیک ستارخان شنیدم
سمت صادقیه تهران تا الان دو بار صدا شنیده شد
از ساعت ۴:۴۰ تا ۴:۴۵
اما بنظر دور بود معلوم نیست کجا بود
سلام مرکز شهر تهران ساعت ۴:۴۳ دوتا صدای انفجار پشت سرهم اومد ولی صدا دور بود
سلام اسلامشهر ساعت 4:42 بامداد صدای خیلی بلند اومد
صدا انفجار تهران ساعت 4:44 سمت پیامبر مرکزی
دو تا صدای انفجار مانند اطراف اصفهان چند دقیقه پیش( فکر کنم نجف آباد ۴:۴۲)
ساعت ۴:۴۵ و ۴:۴۰ دوتا صدا انفجار اومد
سمت مهراباد
سلام اقا وحید ، سمت شهرری رو فکر کنم زدن خیلیی صدای بدی اومد من از خواب پریدم
سلام وحید جان  الان
دو بار بیدگه ملارد رو زد
کرج مهرشهر
صدای دو انفجار ۴:۴۳ و ۴:۴۶
وحید حوالی ۴:۴۰ تهران صدای انفجار شنیدم
دو مرتبه بود، اولی اومد بعد از ۵ دقیقه دومی ترکید
4:45 فردیس 2 صدای انفجار از دور دست
دوتا صدای بدجور اومد ساعت ۴‌.۴۰
سمت خانی آبادم ولی صدا یکم دور بود
ولی زیاد بود مثل غرش بود
شهریار صدای چند انفجار بیشتر سمت رباط کریم می خورد باشه
درود وحید جان ساعت ۴:۴۳ دقیقه ۳تا صدای انفجار توو پرند شنیدیم
سلام ساعت4:42دقیقه صبح صدای انفجار در اشتهارد شنیده شد 2مین بعدش هم بازم صدای انفجار صدای بمی داشت
سلام اقا وحید من اسلامشهرم با صدا انفجار بیدار شدم
صدا صدای زدن بود،سه تا انفجار شنیدم
وحیدجان سمت شرق اتوبان بسیج صدای 2تا انفجار اومد ساعت 4:45
رباط کریم صدای شدید انفجار
چهار پنج تا
غرب تهران ۴ و ۴۰ صبح صدای دو تا انفجار اومد اولی شدید بود از خواب پریدم
ساعت ۴:۴۵  دو بار صدای انفجار اومد کرج
تهرانسر ساعت ۰۴:۴۳ صدای انفجار شنیدیم و از خواب پریدیم.
اصفهان چند تا انفجار شنیده شد
ساعت ۴:۴۲ دقیقه، از سمت غرب تهران دو تا صدای تک انفجار اومد. یکی دور و یکی نزدیک
درود صدای چهار انفجار شدید اومد ما سمت نسیم شهر هستیم جوری بود از خواب بیدار شدیم
ما نزدیکی اکباتان زندگی می‌کنیم و توی پنج دقیقه ی اخیر سه تا صدای انفجار شنیدیم
کرج صدای انفجار میاد
قطعا حمله شده
رعد و برق و غیره نیست
اصفهان دوبار صدای انفجار 4:42صبح
هیچ صدای جنگنده یا موشکی نیومد
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 314K · <a href="https://t.me/VahidOnline/76017" target="_blank">📅 05:29 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76016">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">پیام‌های دریافتی از ساعت ۴:۴۰
سلام وحید جان
4:40 دقیقه انفجار از سمت سپاه تبریز طرف متظریه اومد
۴:۴۰: وحید ارومیه یه صدایی اومد نمیدونم چی بود
صدای انفجار شدید در ار‌ومیه
مشخص نیست صدای چیه
سلام آقا یک صدای مهیبی همین الان از ارومیه اومد ساعت ۴:۳۹. شب هم البته چندین تا موشک از اینجا فرستاده شده بود.
سلام وحید ارومیه ساعت 3:39 صبح صدا اومد و انگار زدن چون خونمون لرزید و دقیقا مثل موقع جنگ بود
وحیدجان نجف‌ آباد صدای چند انفجار شدید. ۴:۴۲
وحیددد
دارنن  اصفهانو میزنن
نجف اباددد  سمت ویلا شهر
دوتا زدن همه جا ترکید
لرزید داریم سکته میکنیم
شاباد موج انفجار شدید
سلام وحید غرب تهران صدای انفجار شدید اومد همین الان ۴:۴۳
وحید اینجا صدا انفجار اومد ۳ بار
خیلی بلند و نزدیک. ما کامل از خواب پریدیم
بدون صدای جنگنده بود.
نجف آباد اصفهان
خمینی شهر دوبار صداری انفجار اومد
وحید زد الان تهران رو
یوسف آباد ۴:۴٣ صدای انفجار از دور شنیدیم.
مجدد ۴:۴۵ صدا اومد.
۴:۴۲دقیقه همین الان دو انفجار پی در پی اسلامشهر
انفجار مرکز تهران ساعت ۴:۴۳
وحید زدددددددد
بالاخره زد
همین الان ۴:۴۳
غرب تهران سمت جنت آباد صدای وحشتناک اصابت موشک یا بمب
صدای جنگنده نیومد
دوباره الان ۴:۴۵ دومی  رو زد
توضیحات اینکه چند دقیقه قبلش برق نوسان شدید کرد
صدای دو تا انفجار همین الان نجف آباد اصفهان
انفجار لرزش شیشه صادقیه تهران
غرب تهرانسر یدونه صدا
اسلامشهر همین الان صدای انفجار مهیب شنیده شد
سلام ساعت ۴:۴۱ صبح، صدای انفجار شدید تو تبریز اومد، جوری که از خواب پریدم، قطعا پدافند و اینا نبود...
وحید جان از سمت قروه کردستان صدای سه انفجار شنیدیم با فاصله ۱۵ دقیقه، به نظرم موشک خوردیم چون لرزشش زیاد بود
سلام وحید جان
ساعت ۴:۴۴ صبح اسلامشهر مرجان آباد
۲ انفجار شدید پشت سر هم
جنت آباد جنوبی صدای انفجار - ساعت ۴:۴۴ صبح - ادامه دار نبود در حد دو سه تا بود
۴:۴۵ مجدد زدن
ساعت ۴:۴۴ دوشنبه صدای ٢ انفجار با فاصله ١ دقیقه از هم غرب تهران
الان صدای دو تا انفجار شدید اومد . اصفهان
سلام از انديشه
وحيدجان فكر كنم ٢تا صداي انفجار بمبي اومد اينجا
صدای انفجار از دور
غرب تهران ۴:۴۳ حدودا
ساعت ۴:۴۲ دو تا صدای انفجار توی قائمیه اسلامشهر  اومد
پشت سر هم
آنقدر شدید بود شیشه ها به شدت لرزید
ساعت ۴:۴۲ صدای انفجار خیلی خفیف شمال اصفهان
انگار خیلی دور بود از ما
فکر کنم ۳ تا بود
اسلامشهر ساعت ۴.۴۴ دقیقه صدای  سه تا انفجار اومد
وحید حان مرکز تهرانیم، ساعت ۰۴:۴۴ صدای ۳ تا انفجار شنیدیم.
وحید سلام. صدا دوتا انقجار ۴/۴۱ نجف اباد
صدای انفجار فردیس
وحید نجف اباد صدای انفجار بلند  چند تا شیشه های خونمون لرزید مثل چی
بیدار شدیم ۴.۴۳
یه جارو زدن داره مثل چی ازش دود میره سمت همین نیرو انتظامیو اینا که توی جنگم زدن
الان صدای دوتا انفجار اومد
شیشه ها لرزید
مثل صدای لانچ موشک بود
شاید جای رو زدن ولی صدای جنگنده نیومد
خمینی شهر
سلام نجف آباد الان صدای ۱۰ تا انفجار اومده و جنگنده
سلام نجف اباد ساعت ۴:۴۲ دو تا انفجار خیلی بزرگ کامل مثل وقتایی که میزدند بود. صدای زیاد و بعدم موجش اومد
سلام وحید همین الان صدا انفجار اومد سمت تهرانسر در حدی که شیشه لرزید
دوباره الانم اومد ولی دور بود
4:41 صدای انفجار اومد
04:44یکی دیگه.
فکر کنم بیدگنه رو زدن
چند دقیقه پیش تو استان کردستان شهرستان قروه سه تا صدا اومد آسمون صافه ولی اطراف رو زدن احتمالا
غرب تهران صدای انفجار
مجدد
وحید داداش صدا انفجار کردستان
سلام كرج ٤:٤٣ صدا انفجار طوري از دور اومد. رعدو برق نبود
بازم الان صدا اومد
ساعت 4:42 صدای انفجار خفیف و لرزش زمین سمت صادقیه تهران
4:44 صدای دوم شدید تر بود. صادقیه
توهم زدم یا صدا اومد؟ سمت ملارد
زدن وحییید زدنننن
انلاین شو وحید بد دارن میزنن
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 312K · <a href="https://t.me/VahidOnline/76016" target="_blank">📅 05:18 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76015">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/YYETQt0dDP0fALoCWTVr3sYA8Gp7F3SqWS8JJq5uwkuNe4B2BD-IxD2ouZQ9GhuMCgtIcb5kPamLCqrVCmXEjTpDVcFOYz2LRylyAnReagXdtE_S_MGsgqcB_KQhmFP4jqRcnTiThCckXx1UGg_GAilRMqMtmYeacRgMohzmQOcaZshZ8jET5ZNLK78WzZqqxL8ylDPeV4NkW5oqT6OQs-qjFNSpOQyaoKcKKfA_3TLuLDle9Jb4nP2yyvmrYjdcw8EpTmtHSzzYEaFjPACaP1btH7vnc40YPvqyV7UA2yFI4ZQsKKlXWWu4QLHaxJweCp8RfLVfKLN0jU7eIG4PKw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ارتش اسرائیل با انتشار بیانیه‌ای از حملات هوایی به چند نقطه ایران خبر داده و گفته است: «نیروی هوایی اسرائیل، تحت هدایت رکن اطلاعات ارتش، اندکی قبل به اهداف نظامی رژیم تروریستی ایران در غرب و مرکز ایران حمله کرد.»
پیش از این سپاه پاسداران هشدار داده بود که در صورت اقدام متقابل اسرائیل با شدت بیشتری واکنش نشان خواهد داد.
جزئیات بیشتری درباره ماهیت اهداف مورد حمله، میزان خسارات یا تلفات احتمالی منتشر نشده است.
این حملات پس از آن انجام می شود که ایران ساعاتی پیش چندین موج حمله موشکی به شمال اسرائیل انجام داد و سپاه پاسداران اعلام کرد این حملات آغاز یک هفته عملیات مستمر خواهد بود. همزمان، مقام‌های اسرائیلی هشدار داده بودند که در برابر حملات ایران واکنش نشان خواهند داد.
این تحول در حالی رخ می دهد که دونالد ترامپ، رئیس جمهور آمریکا، در ساعات گذشته از بنیامین نتانیاهو خواسته بود از اقدام تلافی‌جویانه خودداری کند تا روند مذاکرات و توافق احتمالی با ایران آسیب نبیند.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 314K · <a href="https://t.me/VahidOnline/76015" target="_blank">📅 05:15 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76014">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eRP8Sv77-LYRmeDBLX2xKT4XxGB_JoArKyesRKK4KyiGZzYD6TFQbcSjJA-05xDr9kYf-A2QPk5FQfroLAdeHNncuXl3WUy3T8iXE_u7UtNy756yLcpIMjmxJLihM1tJWAFj5thSoKr-80X1rSFJZJeI0DEWJEFPb0ENP0sFiGYcx78NCH1Au-eTlKZNgJ7RbAZoV7RVl6WmhPHpVD2W9Xlw6UjoMIdpB9TNP-GeHxBK2SbwzxradO4bSYVDDmqW_8LmH7uynF4nLty3of6S_wYWboZE_4xR14CVon-SO3H0MQSaMxk0sy3QpxE0fKPkN6yA2il8cX-uRxNFJ0LAHQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
رسانه‌های رسمی ایران از شنیدن انفجار و حمله هوایی به چند شهر ایران از جمله تهران، اصفهان، تبریز و نزدیک به کرج خبر می‌دهند.
bbc.in
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 334K · <a href="https://t.me/VahidOnline/76014" target="_blank">📅 05:15 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76013">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oVFp78cIvq-Pdi91lu0zRm3zzclp6TZ7IKrvRi_ayf28PgIfvVlYMiV6PCNe7dLOL94GJV8Op_Y_Spj_U7jyYwKc_Qd_StibL93_4TS5OmaSruIawlw-0vOzkgPiYjyrE2uw3DnPEzwciGIfl-WmBp_Mt6aRxoTxVqRpgzXP-XtthpOYl6b4aRZuSMPT8ntf2rjrfyrzcmuLVsMKftV5sBDqD1xFETWVzJZTIbXquUo0xDphhnSudsnxZbG4cKY5TtjXebrPcG8lOvzVQPtrTS4jdWAE0iuXeNx5DrS4apTYk5KCAJIxn4tmfaAtfv1pWX9vJEN7ozZadYmt1Y1adQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرگزاری فارس از وقوع انفجار در تهران، اصفهان و تبریز در بامداد دوشنبه خبر داد. خبرگزاری تسنیم از وقوع انفجار در کرج در بامداد دوشنبه خبر داد. ارتش اسرائیل نیز اعلام کرد نیروی هوایی این کشور «مدتی پیش» اهداف نظامی متعلق به «حکومت ایران» را در غرب و مرکز ایران هدف قرار داده است.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 338K · <a href="https://t.me/VahidOnline/76013" target="_blank">📅 05:15 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76012">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/AAUvJltQym-WEVY3mcJEmVXgKOD9kSKK99cGVmykCPpJ3UOzAaAR_xmFHBB6dY_NaaDlH43ZDjPWZovuBLNR6jbf0_09b6Sj3gV2cJ3MvnwVrsdFKCScyH_xwYCjgYH6a5lDC1_8mKHSy3hludhlQULwU0YD7E6ne6TcN3x-I4lBUATUQoHaq-mFY93HLCC6bTBLHgyCARGtCTw8dbimOkuzDJqWQj2oNLKY2tqPaXR4Hx9GL_d4jb_HomcE01GDApz_g2nm7K2APUpa6tAwuCvJeisKHk5KPb-th1S9ueKBuBUK1CbhDNjP5oDAuNjwGuBfTLTzHezxQPB8Pz36Yw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">به گزارش اکسیوس، بنیامین نتانیاهو، نخست‌وزیر اسرائیل، با درخواست دونالد ترامپ، رئیس‌جمهوری آمریکا، برای به تعویق انداختن پاسخ به حملات موشکی بالستیک ایران موافقت کرده  تا به واشنگتن چند روز دیگر فرصت داده شود تلاش‌های دیپلماتیک برای دستیابی به توافق با تهران ادامه یابد.
بر اساس این گزارش به نقل از یک مقام ارشد آمریکایی و یک مقام ارشد اسرائیلی، ترامپ در تماس تلفنی یکشنبه شب از نتانیاهو خواسته از انجام حمله تلافی‌جویانه خودداری کند، زیرا به گفته مقام آمریکایی، او معتقد بوده «ما به انجام یک توافق خوب نزدیک هستیم».
طبق این گزارش، نتانیاهو تلاش کرده با این درخواست مخالفت کند و ترامپ را متقاعد کند که اجازه حمله به ایران را بدهد، اما در نهایت «تا حدی به‌طور غیررسمی» با درخواست رئیس‌جمهور موافقت کرده است.
این مقام آمریکایی گفته است که این گفت‌وگو بسیار آرام‌تر از تماس پرتنش هفته گذشته درباره طرح‌های اسرائیل برای حمله به بیروت بوده است؛ زمانی که ترامپ به‌طور علنی اعتراف کرده بود بر سر نتانیاهو فریاد زده و الفاظ تندی به کار برده بود.
پس از این تماس، این مقام گفته است: «فکر می‌کنیم رئیس‌جمهور کمی زمان خریده است. او بسیار قاطع است که ما به توافق با ایران نزدیک شده‌ایم. فکر نمی‌کنم در حال حاضر حمله اسرائیل قریب‌الوقوع باشد.»
او همچنین گفته است: «ما در یک لحظه حساس هستیم — چرا باید وقتی در راند چهارم هستید، یک توافق احتمالی را به خطر بیندازید؟ رئیس‌جمهور فکر می‌کند سه ماه است درگیر این موضوع هستیم و اکنون زمان پایان دادن به آن است.»
با این حال، هنوز تصمیم رسمی در اسرائیل گرفته نشده و طبق گزارش شبکه ۱۲، نتانیاهو تا نیم ساعت پیش همچنان در حال برگزاری نشست با مقامات ارشد امنیتی درباره این موضوع بوده است.
@
‌VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 386K · <a href="https://t.me/VahidOnline/76012" target="_blank">📅 02:10 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76011">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Uc_0aAMwKIopFKTIvmrkYsxaInEQYNw5eqAEUyxduWEmDmxNbzFqJIBuupAw1OY_rfw9xlfzXR0v6Y87OZ2mia8ZBLFmarvX84gNNTfd-HGSc6GM0Kzu0AecJs2fmIF50PlwU-vRHnwDS0zpsxBs4-gwrji7vxnYd7Clyjfh0SI0RaY-7EPNBK-1lWbGPl_fg4qajrXy5dx1xH8_oaYIVCjuLK8ZJSZPFUBhMkbbtMwyKVY13ve9ERTcv-Zs3qSrDSK6PGucv3orQ_m_umsLfLv67hlmPu76EUE9AiI7JAlA2UZ68iESCVZacl6BgZC5jBrB-DzTsl05z_ohvjaJ9A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ می‌گوید هر توافقی که او با حکومت ایران کند نخست وزیر اسرائيل خواهد پذیرفت
رئیس‌جمهوری آمریکا در گفت‌وگویی تلفنی با فایننشال تایمز گفت که بنیامین نتانیاهو، نخست‌وزیر اسرائیل، چاره‌ای جز پذیرش هر توافقی که آمریکا در مورد آن با رژیم ایران مذاکره و نهایی کند نخواهد داشت.
دونالد ترامپ گفت زیرا «تصمیم‌گیرنده اصلی رئیس‌جمهوری ایالات متحده» است.
دونالد ترامپ به فایننشال تایمز گفت: «او (بنیامین نتانیاهو) هیچ انتخابی نخواهد داشت. این من هستم که تصمیم می‌گیرم. همه تصمیم‌ها را من می‌گیرم. او (نتانیاهو) تصمیم‌گیرنده نیست.»
به گزارش فایننشال تایمز، آقای ترامپ این اظهارات را اندکی پس از آن مطرح کرد که جمهوری اسلامی در جدی‌ترین نقض آتش‌بس از زمان توافق آتش‌بس در اوایل آوریل، چندین موشک بالستیک به سوی اسرائیل شلیک کرد.
آقای ترامپ تأکید کرد که حملات موشکی جمهوری اسلامی تغییری در تمایل او برای به نتیجه رساندن مذاکرات میان آمریکا و حکومت ایارن ایجاد نکرده است.
او به فایننشال تایمز گفت: «این موضوع هیچ تأثیری بر توافق نخواهد داشت.»
ارتش اسرائيل به صدای آمریکا گفت که جمهوری اسلامی یازده موشک به اسرائيل شلیک کرد. ارتش اسرائيل پیشتر گفت که حملات موشکی جمهوری اسلامی را دفع کرده است.
در همین حال در واکنش به حملات موشکی جمهوری اسلامی، ارتش اسرائیل در بیانیه‌ای به صدای آمریکا گفت که رئیس ستاد کل ارتش اسرائیل، ایال زمیر، در حال ارزیابی وضعیت در مجمع ستاد کل است. ارتش اسرائيل به صدای آمریکا گفت: «نیروی دفاعی اسرائیل به محض صدور دستور، با قاطعیت به دشمن حمله خواهد کرد.»
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 399K · <a href="https://t.me/VahidOnline/76011" target="_blank">📅 02:08 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76010">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">خبرگزاری تسنیم: "صدایی که دقایقی پیش در تهران شنیده شد مربوط به رعد و برق است و این صدا ارتباطی با پدافند یا موضوع نظامی نداشته است."
من هم پیام‌هایی گرفته بودم که بعدش با «ببخشید انگار رعد و برق بود» آپدیت شدند
.
زیاد پیش میاد.
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 405K · <a href="https://t.me/VahidOnline/76010" target="_blank">📅 01:16 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76009">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/PytS26iIXnrkcxYYXADnOfPlqtyrlOUB1KA-MN4MicwndZ_p8iZx-nD2cE9xs7j0A0jKmF_TSrxqnue6Tmi2ndBq4KV7Bpig80wRV8Zk2MOfz9HSAKBibtA8P3kAzEkrUn0pujFCKY8vW2ioaLXa9JypdhJWBF2dAnSdnojdAF60XnuR8oyDIxWgy-r8e6dc1Qa2-oTFH0T-M5mdJwa7NMakU-umyfTIzNc_n5YJ3eaoq4fYL4qu3LueTMNaoq0csACOyK5_afMTz9cQaROGnuUfGIwEDzKdt78SCkk6qCMJrbKnAWijdXuldfdx9tqOHa3PsfJhyw8ySfz6qqUEiA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">shamidartii
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 427K · <a href="https://t.me/VahidOnline/76009" target="_blank">📅 01:07 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76008">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rtTwt1ooJXCZx41Pu73VQCzDiogBQwu6zRVCFdKnv9qs6_RzwbtwlAHbNVEbi_v-p2RVM9gkYB6a1W69C9DD2uPoYGACkYhJtRcDQ1SFJaTLftdj4GsN_Ye0jtTSTccgPNTSAey0TxYpwJEIRmw4NHr63AW6HG9WWoDfPiY_vSQmHRfhbwJ3G4O6Yi4N49yzQdDfQ8vaSm4JKdqKCF0EZpWS1zLCWHOisNikcbqxRPApk0Av72hDtsS4e6LF9P7aWQOB8aqC5IA-8xZOD9digab-JiyObrt14ioIY5rBtTuttqhEhu-i887ckTAlZJPokP1mkCNbSxHKMNJEDewFCA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">با به اوج رسیدن نگرانی از آغاز درگیری مجدد نظامی میان ایران و اسرائیل، سازمان هواپیمایی ایران اعلام کرد تمامی پروازهای شهر فرودگاهی امام خمینی از بامداد دوشنبه ۱۸ خرداد تا اطلاع ثانوی متوقف خواهد شد.
در اطلاعیه این سازمان آمده است: «مسافران از مراجعه به فرودگاه خودداری کرده و اخبار بعدی را از مراجع رسمی پیگیری کنند.»
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 419K · <a href="https://t.me/VahidOnline/76008" target="_blank">📅 00:58 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76007">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/RMSidFdUAfKY6vnEigyc461jKr1Q242h_r0FZKtImknEQMz7mlKxYMEuviqOUM1sNFeOFqO7yblI42dTIufKwXQ7ojPXEBFojRHWOUXxQU0M7Bwddi7OgenwugUQPaJ8vW9lF5iODi1HVIX9P71QyQwguPZ7CvuX2NNGTry9hxlalC1CmPpWaHtZxFQo_ozGJyDvlGYmMZWQ41bd6ZWsqGfZfZJejsSTwtgW4cnhJppumALJ-ueQ32ZFAZNL0LHHWNpi_xyYkX9b4wAxRGU4LhvlM_Wa0cHEx2umq1vlFNBn9neydY3Y3lEJOWjaECo1pLlsoPBXzttbMareT5rJ6Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ایتامار بن گویر، وزیر امنیت ملی راست‌گرای تندرو اسرائیل، پس از حملات جدید موشکی ایران به شمال اسرائیل، خواستار واکنشی شدید شده است.
او عصر یکشنبه در پیامی کوتاه به زبان عبری در شبکه اجتماعی ایکس نوشت: «امشب تهران باید بسوزد!»
اظهارات ایتامار بن گویر در حالی مطرح شده که ایران ساعاتی پس از حمله اسرائیل به حومه جنوبی بیروت، موجی از موشک‌ها را به سوی اسرائیل شلیک کرد. ارتش اسرائیل اعلام کرده است که این موشک‌ها رهگیری شده‌اند و گزارشی از تلفات فوری منتشر نشده است.
ایتامار بن گویر از چهره‌های تندرو کابینه بنیامین نتانیاهو به شمار می‌رود و در روزهای اخیر نیز از توافق آتش‌بس میان اسرائیل و لبنان انتقاد کرده بود.
@
VahidHeadline
نفتالی بنت، نخست‌وزیر پیشین اسرائیل، در واکنش به حملات موشکی جمهوری اسلامی به اسرائیل، در شبکه ایکس نوشت: «خویشتنداری یا واکنشی نمادین، این پیام را به دشمنان ما منتقل خواهد کرد که ریختن خون شهروندانمان بی‌هزینه است؛ از این‌رو اسرائیل باید با قدرت و به‌طور موثر عمل کند.»
بنت نوشت: «این یک لحظه آزمون است: «آیا اسرائیل کشوری دارای حاکمیت است که توانایی دفاع از خود را دارد؟»
نخست‌وزیر پیشین اسرائیل نوشت: «در این موضوع، همه ما، تمامی شهروندان اسرائیل، در کنار یکدیگر ایستاده‌ایم.»
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 408K · <a href="https://t.me/VahidOnline/76007" target="_blank">📅 00:46 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76006">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/HVf3xMT8EyZX8x5ESr2jz9m4Gi5jQq8Ybd4qWVmJnUH-851KgZ_O_htfKi2armSc0WLNaGxrMt3szLFa1S3N66BZ3oR3f4kgZQuj1s6VIJM0jlfZs3XRSyq94N8pi4sd07Fth_cnCnBkaeZsQsMkcbCkWbBl71bKCcsN8_9tiHLOoA9djGVpZCRLwjjZucnceYMt8szItlfKR4I1mm022-UsfyIrH5kASU7nLeKik0cmjsALQ4Q7CNCsfQcDP7dDxDlrN6kg8yJOQaVaQ1QfBXchqWu70EomxoXezzQk-Y4_O6W-R4nstqz6D-WeCARijv8Nk0RTxYIY7WttzXTlLQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">همزمان با حملات موشکی ایران به اسرائیل، تسنیم، خبرگزاری وابسته به سپاه، یکشنبه‌شب، در پی شنیده شدن صدای انفجار در تبریز، گزارش داد: «براساس پیگیری‌ها، صدای شنیده شده در‌ فرودگاه تبریز تست پدافند بوده و هیچ‌گونه حمله‌ای به این فرودگاه اتفاق نیفتاده است».
@
VahidOOnLine
پیام‌هایی که من دریافت کرده بودم:
سلام وحید جان
الان ۲۳:۵۵ سه صدای انفجار بزرگ آمد تو تبریز
پیام بعدی در ۱۹ دقیقه بامداد: همین الان باز زدن تبریز رو
سلام وحید جان
تبریز ساعت ۱۲:۱۵ نزدیک لشکر عاشورا صدای انفحار اومد.
البته شدتش مثل انفجار های جنگ ۴۰ روزه نبود.
تبریز نیم ساعته صداهای عجیبی میاد
مطمعنا صدای پدافند نیست انفجاره
هم اکنون صدای چند انفجار شدید در تبریز
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 419K · <a href="https://t.me/VahidOnline/76006" target="_blank">📅 00:29 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76005">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/mjXidkwSCc8Bgb2Ud-Lpf25aaMRcCTve_QRhDR-ieyfVot5ZUXRG5Ewd1AYjdRRD-F8AZ9oskKlf7BUt7kqzamX96ZCVZlLJYA9swDZ9NVrGiD3G8D7Q13m2ytJf33f8LajkYk7tqYizzRGOC7XxiwjDOFYjCIgTp6YoHTfy38VI-A-p6MV7zcvBzKtcAdNp1NdnvQJ9lz6Gdz_m6khoRhT08szsW9zDIiO_Wx3O38boJ3DEdGwDjA7fkfNoriON9wh-fiR0Uhy9JEn3zReN2xetqLm2_hKjU7v0seKes-zBNELabTlhYnrJVsiWigRM3Rs4flCMw57Nnt2V1R8xZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سخنگوی ارتش اسرائیل، افی دفرین، می‌گوید پس از حمله موشکی بالستیک جمهوری اسلامی ایران به اسرائیل، ایال زمیر، رئیس ستاد ارتش اسرائیل، در حال انجام ارزیابی و تصویب برنامه‌های آینده است.
سخنگوی ارتش اسرائیل گفت: «رژیم تروریستی ایران اشتباه بزرگی مرتکب شد.»
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 410K · <a href="https://t.me/VahidOnline/76005" target="_blank">📅 00:13 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76003">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/iUyUf-9Nmt9mdJGqJ_kZBfA-iqb-chFwAZvWzECuEQ7RmYR48iCVq-3biJ_5L4nxl6RK2JOp1PhSZwzqpdP2VZd8L83W2yeb6ZTFCIn_6cuM14uUyLGXAa1OhV61hkfev_rTLBpxnSp2BCfQ8gF5it01bSDcgplFMSch_GZBCUgOE1JIjWnoD1mQPyz5KsxRdXv73LpDRCeN8QGKsInaAVEXj7uIXRUx4ttSSoL8JLihg6ZNxL886iOK8eQeQ-LvyhupGa6XjbqXSNCztBrvKSkhaAzbC7HDltcuSN5oIlvo1A5nPMcDaVBr79jHGvDRfuAYzUdYVUFMlxjvEOPJlw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/BAPdd5Xda3w8RR4hbcPfrt9mQOEeZ4renQB0-0RHbBiszKHkFTIPJVD3BhwEllGcrWTWfdz6KJ4dMcE-viuiV-Rc7h60FJGn1Pjv_M8anXi9HVZ3tH0HnP3njeq0nBdrIWW8BOqGrUSmtLUJVhiiA9Ni7kLibfVFWkV12drkWhIE7UYqjpRi1KoPBmpm6vKfMmsSesKtUdL2-emCPQIbZ0PjtSYNanTW7fobQEAswrEowaKdB-vB_Mo7BwCWnt6p3D8VRuOjI5BkFae6EyjZPVXh0yc8bv0icjLANcETuzcb1416SUVOE-eeQrlBugfu62yMFnL-JXwnAMEREH-pKg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">پیام‌های دریافتی:
ما تهرانسریم
تو این 1ساعت اخیر که اینا اسرائیل رو زدن
نزدیک به 8تا هواپیما مسافربری از مهرآباد بلند شد
نهمی هم الان رفت
انگار دارن فرودگاه رو خالی میکنن
سلام از تهران داره همینجور هواپیما بلند میشه همشونم تو ارتفاع کم پرواز میکنن
همین الان از بالا سر مهرآباد یه هواپیما با چراغ روشن از غرب به شرق رفت
مسیر خیلی غیرعادی با ارتفاع خیلی کم ۰۰:۰۸
آپدیت:
بعدش کلی پیام مشابه دیگر دریافت کردم.
آپدیت:
وحید جان همچنان پروازها از فرودگاه مهراباد به سمت شرق ابران ادامه داره احتمالا هر ۴/۵دقیقه یک پرواز بوده لاینقطع
شاید ۳۰/۴۰هواپیمای مسافربری پریدن تو این دو ساعت
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 428K · <a href="https://t.me/VahidOnline/76003" target="_blank">📅 00:13 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76002">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/TG6iahpIR_r7iEBnnwwmRqVj4Lwd68yYCtB1vIh-gpJMop0ATjMLcTzmc5rJVtiD6ggwaAKBRbShJ2gPttXraG2aL7g8h3-PFKetz697dg25wzb6iQ2YidQCMe4qi1TC12y31rSgzwTdll5GCyV64SncgYzm54EhcPU1E-j9pmdhIueFO__prIuPnX44dxd1ELiIjx-AEVJoxqenXRslidsjYFGgqQ2DV52SGYJU2vJZP28s-clY4JyEX01WqVvGTC83Qes6-pJ2v_qWSNWnB8-RVYiMVsLaZAhCfLgma3AYvvC48nBqzlp-HvkcVonw8i-BegNyRwZUjp3oiilVPQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ: حملات ایران به کسی آسیبی نرساند، امیدوارم اسرائیل تلافی نکند
درپی اعلام خبر حمله موشکی ایران به اسرائیل در شامگاه یک‌شنبه، دونالد ترامپ، رئیس‌جمهور آمریکا، در گفت‌وگویی تلفنی با خبرنگار اکسیوس گفت: «همین حالا با بی‌بی (بنیامین نتانیاهو) تماس می‌گیرم و به او می‌گویم تلافی نکند. هر دو طرف کار خودشان را کرده‌اند. اسرائیل حمله خود را انجام داد و ایران هم حمله خود را انجام داد. دیگر نیازی به حمله دیگری نیست.»
دونالد ترامپ در این گفت‌وگو افزود: «حملات ایران به کسی آسیبی نرساند. امیدوارم اسرائیل تلافی نکند. اگر بی‌بی (بنیامین نتانیاهو) پاسخ بدهد، این ماجرا همان‌طور که در ۴۷ سال گذشته، یا حتی در ۳۰۰۰ سال گذشته، ادامه داشته، باز هم ادامه پیدا خواهد کرد.»
ترامپ افزود: «ما به یک توافق نهایی با ایران بسیار نزدیک هستیم. این توافق، توافق خوبی خواهد بود. نمی‌خواهم به خاطر اتفاقاتی که اکنون در حال رخ دادن است، این روند از بین برود.»
این اتفاق چند ساعت بعد از آن رخ داد که ارتش اسرائیل منطقه ضاحیه در جنوب بیروت را هدف قرار داد و ایران تهدید کرد به این حمله پاسخ خواهد داد.
یک منبع ارشد ایرانی هم به خبرگزاری رویترز گفته است که «ایران به هر حمله اسرائیل با نیرویی شدیدتر پاسخ خواهد داد.»
ارتش اسرائیل اعلام کرده است همه موشک‌هایی را که تاکنون از سوی ایران شلیک شده‌اند رهگیری کرده است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 454K · <a href="https://t.me/VahidOnline/76002" target="_blank">📅 23:45 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76001">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/FuEvfpdOiT3L8FReWvB7waLq8QMV1xtLV6ZDd8pnu-ZxzOhTPnNKUHnWA6Mhftyk80ds_IIPoeY_1WMAKwP6ld5-wZmunHMDMU450JH8_Dt9c4fT-NJwsk4DZxT_jNrQEQ3HRPioyb_PpxbBsYPgxCopdyupJ8N4-ITsYlU-KqDhTJiE4wpN1QfW5ME2RsRMgxlR0XMJZB5n_s4v51VkVhaKnB5zCxP_fOztIVhQHcsgqhHUw9WiMAS-uqKqShWLbQ2eXMnn0Yc925VUL0jYWmAp5iqSqQwJ4tnvj2cgPPtWqKnkZafkbnaW9R6sd1racAQN7ZlpSZHZNtuxt4wZVg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">mohsenreyhani01
سپاه پاسداران پس از حملات موشکی به اسرائیل در بیانیه‌ای اعلام کرد عملیات شامگاه یک‌شنبه صرفا یک اعلام اخطار بود و در صورت تکرار حملات، پاسخ‌ها گسترده‌تر خواهد بود و تمام اهداف آمریکایی-اسرائیلی را در منطقه در بر خواهد گرفت.
در این بیانیه آمده است: پذیرش آتش‌بس از سوی ما در ۱۹ فروردین ماه مشروط به توقف آتش در تمام جبهه‌ها بود اما مثل همیشه آمریکا و اسرائیل به تعهد خود پایبند نبودند، هم حملات را در لبنان ادامه دادند و هم با تعرض مکرر به سواحل و شناورهای ایرانی در تنگه هرمز، دریای عمان و اقیانوس هند آتش‌بس را نقض کردند.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 466K · <a href="https://t.me/VahidOnline/76001" target="_blank">📅 23:33 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76000">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Twz8jrUBwzr7ph0rUUO-6VP5uI2GHvhC52X5_HdsDrhySDE4Dc497kEh9ORkaGro6pxl873DuvUZa8NpdZiJJnGmP4zzG24GRXH4PeDoKP2jXVP0I3ymeQfXM84fXzbvfq6HfZqyf6NrkL87AWM3GzYByYr36_fWda80ade5XVF6em1V-Pa9ebPJGC3xbbUpr2r8AQX2WSw8qtFD3bhjUQtlSd2zB8EIaicoGsQMKWKc9oF92R2bxTJIIskyBqvGtw-StBw077eC4vkyMmNdQItoLhtaocTcGpszjgXVrvCSbloy5Q-5gKs2LtBqI_V7RZjf2pL7WdHSBRBRT9d_0g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دونالد ترامپ به شبکه فاکس نیوز گفت: پیشنهادی که به ایران دارم این است: موشک‌های خود را شلیک کرده‌اید، همین کافی است.
او افزود: به میز مذاکره بازگردید و توافق کنید.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 479K · <a href="https://t.me/VahidOnline/76000" target="_blank">📅 23:23 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75999">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/dAZAN5zoPk5b_TdiOWeKYJ7x25kUWmFLlY73ZQnZj7x5OeODX-WLsVjOj1Dgb10jylo1MlayNwEu8hvrrTLLyuX0cypkqME7n5f_CJRQddxibQuDRB9ez_XLh0U-Kgh1mQ2jIGtcGsacoppMTsWW8nkZiwSFSeyxqCATKSmR-TNvwanyLbGawTvTeKTJSxEDYTm-gEx62DqCsMP66jAibd7T2p8o7pltpmc46UMbdDOJXAHkS7uFjiXYAI8fKJP5UbBKk96kwv7teTClbUyCDKHK7qbPFDLJmbcSD-0euuynHPLcgPMUtfFF7_YOVTvpWitimSRfXu7opJtoZB-wQg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نیروی هوایی اسرائیل در بیانیه‌ای دقایقی قبل اعلام کرد که این نیرو تاکنون تمامی موشک‌های شلیک‌شده از سوی جمهوری اسلامی ایران را رهگیری و منهدم کرده است. این نیرو گفت ارتش اسرائیل اکنون پرتاب‌های بیشتری را که به سمت اسرائیل شلیک شده‌اند شناسایی کرده است.
@
VahidHeadline
ارتش اسرائیل به صدای آمریکا گفت که جمهوری اسلامی تاکنون یازده موشک به سمت اسرائیل شلیک کرده است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 479K · <a href="https://t.me/VahidOnline/75999" target="_blank">📅 23:17 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75998">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">توییت باراک راوید، خبرنگار آکسیوس:
یک مقام اسرائیلی به من گفت که اسرائیل قصد دارد به حمله ایران تلافی کند.
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 465K · <a href="https://t.me/VahidOnline/75998" target="_blank">📅 22:57 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75997">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/CtUCqcMWrZtOPFK9bETwzZ3F8ivnY3JW1iHY_K6Ddk6aNYqrm22JoXOHzX2yAzhu4ziKq8k8G9aRP1dYMGYLlFDjKkrfUrWUQhJZ0n0wfCafFNjxtrAo4PAo274N_ZpHgnxtMCWS4H6rPE56AXi6ljObCvZoYxaLnyiELKUyrTLnovt1-QX3UDxPH6MWg2V0CL2-rn-SbKG7d7MW-WHe-g35Gd9VmlAtmRS51lAuGAGmywocsgvz-OtzmjWzEu3T_HfwMjKyvEElJ_5LUrm6yQ1MMFVFV6ijKKOpna6EYka_pD6dUSnpLINGj8WkKFr_MncwP0akqcWHQD7412FNJA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سپاه: در صورت گسترش حملات پاسخ ما کوبنده‌تر خواهد بود
به نقل از تسنیم، خبرگزاری وابسته به سپاه:
"فرمانده قرارگاه حضرت خاتم‌الانبیا(ص):
رژیم متجاوز صهیونیستی با نقض مکرر آتش‌بس شرارت های خود علیه مردم مظلوم لبنان با چراغ سبز و حمایت آمریکای جنایتکار و سکوت مجامع بین المللی را روز به روز افزایش داده و با استفاده از سلاح های ممنوعه از جمله بمب های فسفری مرتکب جنایات جنگی می گردد.
با وجود هشدارهای قبلی جمهوری اسلامی ایران، رژیم کودک کش صهیونیستی با عبور از همه خطوط قرمز و افزایش حملات در جنوب لبنان، ضاحیه بیروت را هدف قرار داده است.
قبلا اخطار داده بودیم در صورت گسترش جنایت در ضاحیه بیروت، اهدافی را در سرزمین های اشغالی مورد هجوم قرار می دهیم.
ارتش صهیونیستی باید حملات خود به جنوب لبنان و ضاحیه را متوقف نماید و در صورت گسترش حملات خود به آن منطقه و یا پاسخ به اقدام ایران با ضربات کوبنده تر و پشیمان کننده روبرو و حملات ویرانگری علیه رژیم و حامیان آن آغاز خواهد شد."
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 478K · <a href="https://t.me/VahidOnline/75997" target="_blank">📅 22:50 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75996">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">☄️
موج بعدی شلیک موشک به سمت اسرائیل
پیام‌های دریافتی:
دوباره شلیک از کرمانشاه
دوباره یکی دیگه زدن الان
یکی بود
10:44 دوباره صدای انفجار اومد کرمانشاه
صدای انفجار مجدد
بازم زدن
همین الان صدا اومد از روانسر کرمانشاه
22:47 شلیک موشک از تبریز
آذرشهر [نزدیک تبریز] صدای موشک ۳ تا
سلام وحید
ساعت ۲۲:۴۰ ۴ تا شلیک از تبریز به فاصله هر یک دقیقه
نور خیلییی زیادی داره و صدای زیاد
🔄
آپدیت:
منابع حکومتی نوشتند از اصفهان و ارومیه هم موشک شلیک شد.
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 468K · <a href="https://t.me/VahidOnline/75996" target="_blank">📅 22:45 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75995">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">☄️
'شلیک موشک از کرمانشاه'
‌
بعضی از پیام‌های دریافتی:
سلام همین الان صدای موشک از کرمانشاه اومد
سلام صدای جنگنده در کرمانشاه
سلام وحید جان.
همین الان ساعت ده و نیم دو تا موشک از کرمانشاه شلیک شد
صدای غرش  شدید ترسناک ساعت 10.31 شب کرمانشاه میاد
وحید همین الان از کرمانشاه موشک پرتاب شد
از کرمامشاه الان دوتا موشک شلیک کردن
صدای پرتاب موشک از کرمانشاه الان
سلام وحید جان
من کرمانشاهم
الان ۱۰:۳۰ یه صدایی شبیه شلیک موشک اومد
مطمئن نیستم، ولی دقیقا شبیه صدایی بود که زمان جنگ میومد.
🔄
توییت ارتش اسرائیل:
ارتش اسرائیل موشک‌هایی را که از ایران به سمت اسرائیل شلیک شده بود، شناسایی کرد. سیستم‌های دفاعی برای رهگیری این تهدید در حال فعالیت هستند.
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 492K · <a href="https://t.me/VahidOnline/75995" target="_blank">📅 22:32 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75994">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">پیام‌های دریافتی از شنیده شدن صدای جنگنده در تهران که لابد داخلی است:
سلام وحید جان ۲۱:۳۲ شمال غرب تهران صدای شدید جنگنده
درود وحید جان
صدای جنگنده (؟) غرب تهران
۲۱:۳۲
صدای جنگنده غرب تهران ساعت ۹:۳۲
بازهم مرکز تهران صدای جنگنده یا هواپیما رو نمیدونم ولی خیلی پایینه ساعت ۲۱:۳۳
شهرک غرب
صدا جنگنده
صدای جنگنده ساعت ۲۱:۳۵ دقیقه، شمالغرب تهران
مرکز تهران صدای جنگنده میاد شدییید
صدای نامتعارف جنگنده در مرکز تهران از ساعت ۲۱:۳۳
غرب تهران صدا جنگنده داریم 9.32
۹:۳۱ شهرآرا صدای جنگنده میاد وحشتناک خیلی پایینه
سلام الان نیروهوایی صدای خیلی عجیب میاد صدای جنگنده ست انگار خیلی بلنده
سلام وحید . ساعت ۹ و ۳۳ دقیقه شب مرکز تهران صدای جنگنده میومد واضح . ۱۷ خرداد .
سلام ساعت ۲۱ و ۳۳ دقیقه شنیده شدن صدای جنگنده زیاد ، امیرآباد تهران
صدای جنگنده میاد سمت مرکز شهر
آپدیت: کلی پیام مشابه میاد که دیگه نقل نمی‌کنم. درباره صدای هواپیما اهمیتی نداره که در کدوم محله شنیده شده.
بین پیام‌های اولیه دو تا پیام هم بودند که نادرست به نظر می‌رسند:
سلام وحید، اینجا شهریار صدای موشک میاد. احتمالا از بیدگنه جمهوری اسلامی داره موشک میزنه
وحید از بیدگنه موشک زدن ۲۱:۲۸
صداش تا فردیس اومد قشنگ
آپدیت:
در پیام‌های بعدی روی این تاکید می‌کنند که صدا طولانی بود و چند دقیقه طول کشید.
بعضی‌ها هم نوشتند این بار هم هواپیمای مسافربری بوده با رفتاری عجیب و پرواز با ارتفاع کم.
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 470K · <a href="https://t.me/VahidOnline/75994" target="_blank">📅 21:37 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75993">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/iHpDXHYGxrimzn8l3JCv4cFaNTymHhE2zmwa3ZHhrqCXqRDv-9n_1yY2UjAte3wH8lx2mVfhS9knOwU7op9bJmdHE1RQaB3FJIdXyYXlSYgnqZgMv3SDWmHHRhknt8i0CiT8IZoTfXpfb_AcwMsW-kXX_O7NUAiFAsK4J-QpY2Qjgpn-9qYSihXQwk0aGiXugZnceVfoCSSgoocjv37AMqGoJLaa7q_JMYbBucqS7LnzpGlmFgWlL9hHs6b08FQHg_xuBhWumZBvcMnqG-X76cte--0xmAKjkEqUXr2fE3rHXfmimBv7yCSMeyeL920QJQNtgNRzhC6wWJCdmJhwkw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">توییت پزشکیان علیه صدا و سیما
رئیس دولت در جمهوری اسلامی، تلویزیون حکومتی را در شبکه فیلترشده ایکس تهدید کرد:
drpezeshkian
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 472K · <a href="https://t.me/VahidOnline/75993" target="_blank">📅 20:51 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75991">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/h9bshdflDweqamcOokATRStd9HVKrpjom2cRC8NkmnkV9phek2vhklK4cllhrdgRXtpEOzLtMBpUobIP4WfeouLy6Syw-RRGNY6uyNRauh07QwwfRsdT_0RHlhIL4Zws_CvcfZS-F4l2fbFrGBhjVKuoCSPVpfMdJuWitzgoJdq0uJcYwOZkBU9UlPu_Ww9IH4d9mHDrDp_7JIWoe95b69MvJvRGYV9kF01lIoveFejUc3Io0sdf943NHOd54KTqVZWo6jXaS_OmkUhyhg6hjFKv-sgHV9JOsWHQ-R7cqDtjsq0iA1wo5BuBi6k-fvzUF3MqhRPL0O33mXVPp4J6eQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/SgdJ4RrA85Ozup1OSqiwExebrmVRkGMmNCdkZiYGMLlsxDsttODg239OPVUnefnm51yUEHc51nmNyeAhvQKOLd-tC7MX4JEkd_xzLWLUHGQKrQSQe5FReRr4ratwaAfWUGXzjwm5lZulM2VIIvEb1aH7zzwMuXzkFG_ukiYtXIlZvCkbAZjEjPgY5sNDNgbs_sx_CFBgaO5zEa6zG7EAZgy1rHmPF-KgW6gUx-i96xrOpxQxRYhEaQ3qgIomT_JAZhZ4r_tqg5qK1MHb8WaGY0-_CR5N9E2a92rZLdDye-XtFu81xGdC0Gnq_x0Yg2qb3uJsbb2UAMzSfcNZvekGUQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">قالیباف در واکنش به حمله اسرائیل به بیروت تهدید کرد پایگاه‌های آمریکا هدف قرار می‌گیرند
:
mb_ghalibaf
رئیس مجلس شورای اسلامی که مذاکره‌کننده ارشد جمهوری اسلامی در گفت‌وگوها با ایالات متحده است، در شبکه ایکس نوشت که محاصره دریایی علیه ایران و «چراغ سبز امروز آمریکا» به اسرائیل برای حمله به ضاحیه «پایگاه‌ها و دارایی‌های آمریکا و رژیم در منطقه را به اهداف مشروع تبدیل می‌کند».
اسرائیل ساعاتی پیش اعلام کرد در واکنش به حملات حزب‌الله به خاک خود، مواضع حزب‌الله در حومه جنوبی بیروت را هدف قرار داده است. از سوی دیگر دونالد ترامپ، رئیس‌جمهور آمریکا، اعلام کرد که قصد دارد نیروهای آمریکایی را تا زمان «تکمیل» روند توافق با ایران در منطقه نگه دارد.
قالیباف در بیانیه خود ایالات متحده و ‏اسرائیل را متهم کرد که «نه به آتش‌بس پایبندند نه به گفتگو باور دارند» و افزود که این کشورها «با محاصرهٔ دریایی و نقض توافقات دربارهٔ لبنان نشان دادند که فقط زبان قدرت می‌فهمند».
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 446K · <a href="https://t.me/VahidOnline/75991" target="_blank">📅 20:00 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75990">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/AoOvJ_JULF2ldAidsVihWE45kATrWLjRiTN7CkLhl1SKIls9VEWyCqcLJwzcbLXlprN2QeRID1VatRUi29v8rWoPbfC9jae0cORtI16-Oe41WDSefGSlTUyDeL9ktIgxnpKfE8WiiuDlLnXzsXh83RYOlsFloBxUkxEa5ShbXwaY40v-Hv6RfhzUg0GXHYJhUnCmcuql58ASSDvL9UZsbS53H2nr4S917nH7LvBKSkArzeUzAYgE0vxol9tQ4w6sCXCa1wSH3oU7i38G4bAo3NF01dIjAq1jZ89yy78F8m-Ux9FkFfO25QK9oIpmLI_J-hFSEC2R_PFNTfy9YZcvPg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ابراهیم رضایی: امشب به اسرائیل پاسخ دردآور خواهیم داد
توییت سخنگوی کمیسیون امنیت ملی مجلس شورای اسلامی
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 423K · <a href="https://t.me/VahidOnline/75990" target="_blank">📅 18:12 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75989">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aE5pArPUS-G-KhwoHjqyLuS0Wz-zH23Fgowc8SyHuWZKAj6Ba9wklU6FoI_jAuoKoMFfHFUo1eFuaihC-JWdMpITHnlK0vI9Dc2Oau3ej54sUVTReuJtRYg5X6o4c6m6DSyH4PvBjV8W5w1Cp7oi-s1OM6x8Ebb8579cneBImk0Z2h6TnAOTJ4K4ZH2AMDxslBdoZB0ipskqTw7d9ZfsfQ_JxBjKvmQ91vfsj0rVq0n1YloPBPrkYSx_BE8TmUd36z_muJrEdC5u4ALeXv-4wRxgFmn7pNcFPPoGbtrxc6nUsnJ5m1hUszS3NxGHmPFQy-YHdb5ZyVFi8z-SgkbRJg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">«وحید هاشمی» ۲۶ ساله و تبعه افغانستان، شامگاه ۱۸ دی‌ماه ۱۴۰۴ در خیابان ۲۰۲ فلکه تهرانپارس هدف شلیک گلوله جنگی قرار گرفت و ساعاتی بعد بر اثر شدت جراحات جان خود را از دست داد.
به گفته نزدیکان، گلوله جنگی به ران پای چپ او اصابت کرده بود. وحید هاشمی حدود دو ساعت پس از تیراندازی به بیمارستان تهرانپارس منتقل شد، اما به دلیل خونریزی شدید جان باخت.
خانواده وحید هاشمی پس از ناپدید شدن او به جست‌وجوی او پرداختند و سرانجام پس از شش روز موفق شدند پیکر او را پیدا کنند.
پیکر وحید هاشمی در تاریخ ۲۴ دی‌ماه در قطعه ۹۶ بهشت زهرا به خاک سپرده شد.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 387K · <a href="https://t.me/VahidOnline/75989" target="_blank">📅 18:04 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75984">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/KUna3ycvq1PBnkBj14iWMTP-VDtpsy30OFLNBaTUOUeo8tZYTi7zGQfbU0W3O30BMKmFDDzjMmHgPNDNAUh_k0pGOFrO95y9NGq04GGSYYy_MnOc49N464EMDWpvrvHEaQojJcvKlQcO7P6tkFr5wdlwvHPAtY2eCYKsP9jn2Nzb8N6IzL9ofJsZ882gaAMWdc9rWBQYyOR60slhW-E2BEpsQS6THjxmgOTYcGQI4P021mSFMXlO3JFK7oc-5COPwI2TKvBcDZqTLv7fpjgV58fEAbFkuaGm_NBZEmNpyieI63txpcqPtYr7fXyQ289NlfsuB0rOJgbonVMNWfR_ZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/Qcx-KFyZzM9goihUjwhZavcnQmVizTFNW3jQlpoJDSuGrdU8vOj911thIqVCyheCws5Jxum6afJO4kvghZ6Q0hOuOmcHQTtHASumRsQmjZ7azzVn7QhKMcOStlJLrJ-X9JLcJTwG9drNSbfv776YTZ7mbY3QKeinHj9sINGsw1LQ60C96pUfqEC-lUlBTmrQgow-7Llc30EFO128W3SKLVceQxr7lDoAI4GIF6KFa0ReXPKtgc7VnHQTaSdgQis657BJFJuk0czxP1hdRJAO61eqUBOT69Aa68xVdco4eg80VbW9g0mMPyOTO9KC-zPYcK0nWSsVQ779ClS6JSVjpA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/MJ6yzds6vxYhX4Ltj8oCn8RwHJwOSBUsgvGE5r8M9ObnQx33HqF0pV6u2D3OUnXl0uepwbj8628ZQ5OeRtfskmyGsqRYieib0mRlqX08dtMEmHB51rqzLVgJqh3rp5ZIODJNNDQCG9f-mAVTW1iSbxMnOoG3acXPssyW0IZK6jpal_Lhg8ey6EmUok_-0nyJN5h59cekWyEFFIhDl3UkzrpI-ASN1En0mBLJBSXBy5avX17xu-Ro1bWt-CeiSdZMAd51RFebwUYBLZmFRrBo3T3btsFZQsDVZZ_3ZpZjbPGCZ-bootI4CBFHz1aBbEZQ-nUrzGl2-BzXka_ICIvsKQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/poojeyx9qDZYZlNs5DqyN4c1TbmmWedj_QyTyhJaoLVS5ZLpk_Lo-tElFrvPaCWuN3AKzSKkVBo3qGlvu44bCMn7B8r56WuYU_sKYJqFdhjBSWW6mhIOhhUENKJXXrvST0kdVCLUH0BsvKjHjodyD-cEnXbcDD9Zc67eZxYPSQ5xSHzm8S1Dm5KL4pCL-qvyIVLRfzCJrm7Ta3vnbeaHEb40FwIzxV1254smdZhKNAtVh7C136tNLQFOqwADa0VI0gMA0vT5hn1MReIUk1vDCq1r4gATDVBrMnpsL3BIpBv6U8W8QTKQKby_jcIQnex0z1y-sDVTfDSk6CyFdxHqWg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/pxWtREGFL8XKMn_1SulcXaBM16DRtYEWhnLG3ijulG-a4QamribDEZBe889wFl9n_XMf10g8agBK89gnppKaULatMqnTGfCCD8iggYHXeTKq7eUTU6uH4mQHE0mdyLYb57eG_o803XjEyMoM3kPonjBev-HuNxtG-PgH5b4yTYeKwO5vWeGs-26zcXeG-8CSm8XiyyuNf9lENzpbD02bEFVbx8X8IAKFT4gQWksCP6LWuOZ6FSK0gFLYtH5Z4uGRspA1Y_NKMY0dEzW6ydtlCAhy26_VI22czx7A2y3cZ4AwhTg6KpMoRUrFqNYG5H2Mg6rBj9H30Pk0Ml89_otGMA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">ترامپ: پیش از نهایی شدن توافق، دارایی‌های ایران آزاد نخواهد شد
دونالد ترامپ، رییس‌جمهوری آمریکا، در گفت‌وگو با شبکه ان‌بی‌سی نیوز گفت که به‌عنوان بخشی از هرگونه توافق، دارایی‌های مسدودشده ایران را از ابتدا آزاد نخواهد کرد و هیچ تحریمی را نیز پیشاپیش لغو نخواهد کرد.
او افزود که اصراری ندارد لبنان در توافق کوتاه‌مدت میان واشینگتن و تهران گنجانده شود.
ترامپ در پاسخ به این پرسش که آیا این اقدامات پس از توافق انجام خواهد شد، گفت: «بله، بعد از آن. اگر رفتار مناسبی داشته باشند و به تعهدات خود عمل کنند، آن وقت گفت‌وگو را آغاز می‌کنیم.»
رییس‌جمهور آمریکا اضافه کرد اگر بتواند با تهران برای پایان دادن به جنگ سه‌ماهه میان دو کشور به توافق برسد، آمریکا با ایران برای جمع‌آوری و نابودی ذخایر اورانیوم با غنای بالای این کشور همکاری خواهد کرد.
او افزود در صورت عدم دستیابی به توافق، واشینگتن توان نظامی جمهوری اسلامی را بیش از پیش تضعیف خواهد کرد تا نیروهای آمریکایی بتوانند با امنیت کامل این مواد را خودشان جمع‌آوری کنند.
ترامپ افزود که خواهان اضافه شدن بندی جدید به توافق است تا ایران نتواند با خرید سلاح هسته‌ای یا تجهیزات مرتبط، محدودیت‌های توافق را دور بزند.
او گفت: «پرسیدم اگر آنها خودشان سلاح هسته‌ای تولید نکنند اما آن را خریداری یا به هر شکلی به دست آورند چه؟ من می‌خواهم در متن توافق عبارت خرید، تهیه یا کسب سلاح نیز گنجانده شود. آنها نه حق تولید سلاح هسته‌ای را دارند و نه حق خرید یا دستیابی به آن را. تهران در ابتدا کمی با این درخواست مخالفت کرد اما از موضع خود عقب نشست.»
دونالد ترامپ، رییس‌جمهور آمریکا، درباره مجتبی خامنه‌ای و محل اقامت او گفت: «او به‌شدت زخمی شده است. نمی‌خواهم بگویم می‌دانم کجاست یا نه، اما احتمال زیادی وجود دارد که از محل اقامت مجتبی خامنه‌ای مطلع باشم.»
ترامپ همچنین اعلام کرد فعلا قصد خروج نیروهای آمریکایی از منطقه را ندارد؛ حتی با وجود آتش‌بس شکننده و ارزیابی او مبنی بر اینکه توان تهاجمی و دفاعی جمهوری اسلامی به‌شدت آسیب دیده است.
او افزود: «هزینه نگه داشتن حدود ۵۰ هزار نیروی آمریکایی در منطقه بسیار ناچیز است و ممکن است برای اعمال فشار در مذاکرات به آنها نیاز داشته باشیم».
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 338K · <a href="https://t.me/VahidOnline/75984" target="_blank">📅 17:58 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75983">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/8f1a01266b.mp4?token=m2f6dx6muhbt84AC395YErWzq98q0IbyLx1heKYdWhBdwW9czlbWCOYP_UBdEd95bhjHCBXlqD_nQuyjA51hesaYpiu-qcXVjruwShcKlqxTU-R8JQujTdc_NogBkYjHcuGaARjhGMFe7wfraHbYuKBwbyzVOtbqCFDZfUNXjn04ZQFm3K6gVYjBQnDI-xM7nuead-9Id5q34cDN9dnXjJr5LV13gx6spuQPulV2gyWgB4V5lcp7lC2_WL0wjZx1f0f610c6AYjNDaMTI1_H6-GufC-zqJSKMSjQPfH1WcGA4rrmpV4a8o9gJhXwnXyw45VytpLL3SUfSuhNx6fSeQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/8f1a01266b.mp4?token=m2f6dx6muhbt84AC395YErWzq98q0IbyLx1heKYdWhBdwW9czlbWCOYP_UBdEd95bhjHCBXlqD_nQuyjA51hesaYpiu-qcXVjruwShcKlqxTU-R8JQujTdc_NogBkYjHcuGaARjhGMFe7wfraHbYuKBwbyzVOtbqCFDZfUNXjn04ZQFm3K6gVYjBQnDI-xM7nuead-9Id5q34cDN9dnXjJr5LV13gx6spuQPulV2gyWgB4V5lcp7lC2_WL0wjZx1f0f610c6AYjNDaMTI1_H6-GufC-zqJSKMSjQPfH1WcGA4rrmpV4a8o9gJhXwnXyw45VytpLL3SUfSuhNx6fSeQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دفتر بنیامین نتانیاهو، نخست‌وزیر اسرائیل، روز یکشنبه اعلام کرد که ارتش این کشور مراکز فرماندهی نیروهای مسلح را در حومه جنوبی بیروت هدف حمله قرار داده است.
در این بیانیه آمده است: «مطابق دستورهای نخست‌وزیر نتانیاهو و وزیر دفاع کاتز، نیروهای دفاعی اسرائیل دقایقی پیش یک مرکز فرماندهی نیروهای مسلح را در منطقه ضاحیه بیروت هدف قرار دادند. این اقدام در پاسخ به شلیک‌های حزب‌الله به سوی خاک اسرائیل انجام شده است.»
این نخستین حمله به پایگاه اصلی حزب‌الله از زمان برقراری آتش‌بسی است که روز ۱۶ آوریل با میانجی‌گری طرف‌های بین‌المللی حاصل شد. آمریکا هفته گذشته اعلام کرد دولت‌های اسرائیل و لبنان به تمدید آتش‌بس به شکل مشروط دست یافتند.
حزب‌الله، گروه مورد حمایت جمهوری اسلامی، پیشنهادهایی را که برقراری آتش‌بس را به خلع سلاح این گروه مشروط می‌کند رد کرده و تأکید دارد که اسرائیل باید ابتدا حملات خود را متوقف کرده و نیروهایش را از جنوب لبنان خارج کند.
ضاحیه محل اصلی استقرار فرماندهی و نیروهای حزب‌الله است. این گروه از سوی آمریکا تروریستی شناخته می‌شود، اما اتحادیه اروپا تنها شاخه نظامی آن را در فهرست سازمان‌های تروریستی قرار داده است.
ارتش اسرائیل ساعتی پیش گفته بود دو پرتابه شلیک شده از لبنان به سمت خاک اسرائیل را رهگیری کرده است.
ایران که در حال مذاکره با آمریکا برای رسیدن به توافق پایان جنگ است، پیش‌تر تهدید کرده بود در صورت حمله اسرائیل به بیروت، جنگ را ازسرمی‌گیرد.
@
VahidHeadline
📡
@VahidOnline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 295K · <a href="https://t.me/VahidOnline/75983" target="_blank">📅 17:53 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75982">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/9915e8c302.mp4?token=RLOFjEARux6GwkSUGCQRTvBBU_IxGO3lDWvjvVGsxhRLV1oBIcZuzU-We8V4ZMzG0WjB4IpL667umx73dkL6_rEMV2xJK4fcsN4dHCXpjB2iCZVqmL3i_80S7r7XyD6W6js3uUBbCXUehEJDTUZufvAfbkYqlrKzlMunRDjE2avnqy-_YoFyiZ9DzdvtI9h5OwxoYMo7zyjwB6eobjwOKI1fzRmLtJxNyx4LNtV4nWsGUWSfrdCXZzkWZexRF8ApkvfxJ2V9njO_yLmV6LhINq0LhwWPGMsZQqIagxtRFPqUsq63i-OfnOFmp-8fnyr9japJ-ZB8TxX5Gv9IF3oFig" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/9915e8c302.mp4?token=RLOFjEARux6GwkSUGCQRTvBBU_IxGO3lDWvjvVGsxhRLV1oBIcZuzU-We8V4ZMzG0WjB4IpL667umx73dkL6_rEMV2xJK4fcsN4dHCXpjB2iCZVqmL3i_80S7r7XyD6W6js3uUBbCXUehEJDTUZufvAfbkYqlrKzlMunRDjE2avnqy-_YoFyiZ9DzdvtI9h5OwxoYMo7zyjwB6eobjwOKI1fzRmLtJxNyx4LNtV4nWsGUWSfrdCXZzkWZexRF8ApkvfxJ2V9njO_yLmV6LhINq0LhwWPGMsZQqIagxtRFPqUsq63i-OfnOFmp-8fnyr9japJ-ZB8TxX5Gv9IF3oFig" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یک کشته و دست‌کم پنج زخمی در تیراندازی مرگبار در اسرائیل؛ دو مهاجم کشته شدند
ارتش اسرائیل اعلام کرد دو مهاجم حمله تیراندازی روز یکشنبه در مرکز اسرائیل، پس از عملیات نیروهای امنیتی کشته شدند؛ حمله‌ای که به گفته امدادگران، یک کشته و دست‌کم پنج زخمی برجای گذاشت.
این حمله در چند نقطه در نزدیکی حصار امنیتی کرانه باختری رخ داد. امدادگران اسرائیلی گفتند قربانیان در سه محل جداگانه هدف قرار گرفتند.
به گزارش تایمز اسرائیل، یک مرد ۳۱ ساله که نزدیک تزور ناتان هدف قرار گرفته بود جان باخت و یک مرد حدوداً ۴۰ ساله در وضعیت وخیم به بیمارستان منتقل شد. چند زخمی دیگر نیز با جراحات متوسط یا شدید به مراکز درمانی انتقال یافتند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 272K · <a href="https://t.me/VahidOnline/75982" target="_blank">📅 17:53 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75981">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Y9PsobPjys87qPVOFvFoCpOLcB60U_4_OpiwM3e6iNdr-itGK-rvuqDk3R2bQp2UFrORqx7ra4k17EB7isqGSm98efyZJLRadPN_ycBxTuoDfUIiGzjSEzjcjVZTn6RguqOI7lp6MuGmnLL7QEaqmmnJrD-n_qC15y0ygLyI0hijaEarefGxpTPLK8lQXunwcgY0M-g-iNnf1PP8YFqKHxrguhgiMksruZiDRcdqMFJrvGfAvauAfY-gaPJPcVCLybcG6inoPMdWJoOYwHgoyeMPKYUzthSxuYbrBDorTd9ugo2ZQIoRg-Ykp6igZbY_G8tmbW8UW1ZKv8zi5cMpHg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزیر کشور پاکستان که حامل «نامه‌ای ویژه» از طرف ژنرال عاصم منیر، فرمانده ارتش پاکستان، برای مجتبی خامنه‌ای است، روز یکشنبه  ۱۷ خردادماه آن را به عباس عراقچی، وزیر خارجه جمهوری اسلامی تحویل داد.
خبرگزاری فارس، نزدیک به سپاه پاسداران، روز یک‌شنبه، ۱۷ خردادماه، ویدئویی منتشر کرد که وزیر کشور پاکستان در آن می‌گوید حامل «نامه‌ای ویژه» از طرف ژنرال عاصم منیر، فرمانده ارتش پاکستان، برای مجتبی خامنه‌ای است که به عنوان جانشین پدرش، علی خامنه‌ای، معرفی شده است.
در سه ماهی که از آغاز جنگ و معرفی مجتبی خامنه‌ای به عنوان رهبر می‌گذرد، نه فایلی صوتی از او منتشر شده و نه ویدئویی که نشان دهد او از حمله مرگبار به بیت پدرش در روز ۹ اسفندماه جان سالم به در برده است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 250K · <a href="https://t.me/VahidOnline/75981" target="_blank">📅 17:52 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75980">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ml-6wmfGlwjcbzRb18YbJxBMfCSqjutjJTpR2FCmIELbxwQdhSwgGh2OfOS0nzraPOOfS_DsU2oan6INIRr3OECphy1HNz5okbSwa9vxxYfrQrG6SMfFsCO-nzmsvwOw1B1oA1_BM3eZSnHpUVzEYuqhPs1kHT1UNU4zaRZtKCSg1PLWZw6fU0dXB0ZlHE4ip3jspE4T-2UzpkBXO82HwCI2nu-aI8prDVL9lPqn40oxOlaqDT-tcXMHw2Unpli4bc-xfWZZTgCTrj4MarZnSA7pW9PnNRT4jg34Ya3-uVzguD8c2rUe-WA0EVX7sq75JLve6EjmIAeEwzWakjjv_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">برخلاف برخی گزارش‌ها درباره ورود و خروج تیم ملی فوتبال ایران به خاک آمریکا، رئیس فدراسیون فوتبال کشور روز یک‌شنبه توضیح داد که تیم ملی یک روز قبل از هر مسابقه اجازه ورود به خاک این کشور را دارد.
پیشتر ابوالفضل پسندیده، سفیر جمهوری اسلامی ایران در مکزیک، گفته بود که بر اساس شرایط تعیین‌شده برای روادید اعضای تیم ملی فوتبال ایران، بازیکنان و کادر فنی تنها در روز برگزاری مسابقات خود اجازه ورود به خاک آمریکا را دارند و باید همان روز این کشور را ترک کنند.
به گزارش ایسنا، مهدی تاج که خود نتوانست ویزای آمریکا را دریافت کند روز یک‌شنبه همچنین گفت: «واقعا عجیب است که اینها تا این حد در حوزه اداره فوتبال دخالت می‌کنند. این کار نادر است.»
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 326K · <a href="https://t.me/VahidOnline/75980" target="_blank">📅 17:51 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75979">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TAynm-kvCCW_UXUJRhGwD413eymeehhTVx_uGjWUXmVGAtNuYfTFH3kl8QtVoeWGd1mvnbIa6yVmW2IcWkZVeUYJ3McC1iU48fdegoFe78jLdTMYudV8EGBrA5QOIyIr56nR7Pxe0MkvtkfAT-bS7_tnaemVxMBbEgY0iOeZQDU0UiLzlmKlKq01qu9Aj1qh4tTGxxvTw9F3orj3j-VTKKV5c08BuPoJxvaw_oXb9PoQPdI1kMGrADBclRz5Dbsdhojlcl99O-TWH84nOe7zpfVUI5wyMiqJ3dkiC_-HW94AzpKjbYvKlMk5c3Kqiaf-odEKKC2XrloOZZ6-VDWZIw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سازمان حقوق بشر کارون، روز شنبه ۱۶خرداد ۱۴۰۵ در گزارشی درباره اجرای قریب‌الوقوع حکم اعدام پنج زندانی سیاسی به نام‌های مسعود جامعی، علیرضا مرداسی (حمیداوی)، فرشاد اعتمادی‌فر، حسن مصلاوی و رضا عبدالی هشدار داد.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 345K · <a href="https://t.me/VahidOnline/75979" target="_blank">📅 17:51 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75978">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/i55Q7ketVZtjFzjw39EgUQCBdF1r3ZamnDOD9nN6v1zipAX6t_-mUQSOrV-53W-C2-YhoCcSFuNilWriG8S6Fp4EWFNWq_EhhriowiVLrw16mv6f2NggwO6Tuy5p0sYM_zD83el896ADfGGreGig1Zx8GkmkAqdKkunAhhzCGvMAwLw2hzCVfWr3Ekrnfv8eDlLdU4r5m25So5QVchAR7mp169AYBQrIItrN59w2N_b8uus0ZYrVU4UmdPrGgkoujawlj8amQ48SlEI-kvfd5PdhHIGylJMHg21pZeZCtN_WAqMuKS7jACCdrhbCci0pUCHgONRR_nltMgeRrfY7Ew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ستاد فرماندهی مرکزی آمریکا، شنبه‌شب به وقت واشنگتن در بیانیه‌ای گفت اوایل امروز، نیروهای ایالات متحده در خاورمیانه دو پهپاد تهاجمی یک‌طرفه ایران را که تهدیدی برای تردد دریایی بین‌المللی در تنگه هرمز محسوب می‌شدند، سرنگون کردند.
سنتکام افزود که نیروهای آمریکایی همچنان آماده در برابر اقدامات تهاجمی جمهوری اسلامی هستند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 374K · <a href="https://t.me/VahidOnline/75978" target="_blank">📅 05:03 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75977">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Sgpr8sFBJs8I4gOMHEoDMv4Av5LSjRGnsZ-pssifshs9CHIR5psqSCPrfv2L_bqoWvL967Aa6V-RTy3nMV44NFdSTgXovXx3j8Q1y18IMRq6cyIR-4H7QOPBm7IttCgNXl_LuTmTKso-O3j07OnIbClT37YJBbN1sQNrEpyV02DF5nhB-y3ORDC9va7Q3wn5Pj5jK6hh9NLcrJMY97K8fmREjEzROLfKxF4_wLyMW1IDT6Xy61H382-vrd7Xla4V12hrnalUyn0T6NErtbSX2OYGV6bRH5i402imtRpd0bJ3NyQbV6kqW72sWjzWYqiDocjgGd4gYguQMkHu0hW5cA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرگزاری فرانسه گزارش داد، ابوالفضل پسندیده، سفیر جمهوری اسلامی در مکزیک به خبرنگاران گفته است بر اساس شروط تعیین‌شده برای ویزای اعضای تیم ملی، بازیکنان و کادر فنی تنها در روز برگزاری مسابقات خود اجازه ورود به خاک ایالات متحده را دارند و باید بلافاصله پس از پایان بازی، این کشور را ترک کنند.
این محدودیت سخت‌گیرانه در شرایطی ابلاغ شده است که کاروان تیم ملی ایران روز شنبه، تحت سایه یک بحران دیپلماتیک شدید میان تهران و واشنگتن، اردوی تمرینی خود در ترکیه را به مقصد مقر جدید خود در شهر تیخوانای مکزیک ترک کرد.
براساس این گزارش، با توجه به اینکه هر سه بازی مرحله گروهی ایران قرار است در خاک آمریکا برگزار شود، این اولین بار در تاریخ جام جهانی است که یک کشور میزبان، پذیرای تیم ملی کشوری می‌شود که با آن در وضعیت جنگی قرار دارد.
این دستورالعمل جدید واشنگتن در تضاد کامل با اظهارات قبلی امیرمهدی علوی، سخنگوی تیم ملی قرار دارد که پیش‌تر مدعی شده بود ویزاها «چندبار ورود» هستند و تیم یک یا دو روز پیش از مسابقات به محل بازی‌ها خواهد رسید.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 384K · <a href="https://t.me/VahidOnline/75977" target="_blank">📅 02:20 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75976">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/XTWoiO2B50fPGSKnWbUv9yOjSQ3W6rbpYjXWGmrWFT5jqQUJ5DnaZyTTukgFIeX3k_zc9qQ8L-oR8VXD2fES9Jbm4jdMpzlfQZ_wIUkCy3tmuMk90ikE6yeTBCbkObbWf0-wh3y5fagAZpEnoIFSdg0yWUs1rvPvVTGz2ueqjdahgE7pf1MPj2gnVe4r6rnhBlZEuMcrlfyjMGgDEu4fU1Z6mv_iYkGMveOyUwuQbH0fs2836zLCXE9L46Xn5rHMkU0-rWYOFPC6SwmUXpZNk35lAclmZ3iDhvm5bssm5b4Lck_InOB5e6Ig9FXq-Ef2aXBISiLFO0DqIiRkOA2cDg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رویترز به نقل از منبعی آگاه گزارش داد که آمریکا در حال بررسی تحویل دارایی‌های بلوکه شده ایران به کشورهای خلیج فارس جهت بازسازی و جبران خسارات ناشی از حملات جمهوری اسلامی است
رویترز خبر داد که وزیر خزانه‌داری آمریکا به تیم خود دستور داده خسارات واردشده به کشورهای خلیج‌فارس در حملات جمهوری اسلامی را بررسی کنند
رویترز به نقل از یک منبع آگاه خبر داد که آمریکا دارایی‌های ایران را برای حمایت از بازسازی و جبران خسارات آینده ناشی از حملات جمهوری اسلامی را در اختیار کشورهای خلیج فارس قرار خواهد داد
رویترز به نقل از این منبع نوشت که آمریکا همچنین بررسی خواهد کرد که آیا می‌توان از دارایی‌های ایران برای جبران خسارات گذشته نیز استفاده کرد یا نه
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 398K · <a href="https://t.me/VahidOnline/75976" target="_blank">📅 00:44 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75975">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">تسنیم،‌ منبع وابسته به سپاه:
"روابط عمومی نیروی دریایی سپاه: صدای انفجار شنیده شده از اطراف جزیره خارک مربوط به خنثی‌سازی مهمات باقی‌مانده از جنگ تحمیلی سوم در منطقه بهرگان است."
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 378K · <a href="https://t.me/VahidOnline/75975" target="_blank">📅 22:08 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75974">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/VHZ8ljxDnIhRo191C0Cy39ZtULSaKRoMKMi0zeok1H9VVNh0-cbbyjQjTHIc6kHfS3of38H718FVN-NjgCuAUXbk_1SUc9BKIGsdxTd387fnM5GvTF2zioIJXsdNw6vce0gauPg77NPLOCPM8llej2Vucc1Bn2-isdyZ2pWJIxxJVqHDrMX1Vw9_fZsvwiAemz3ciEMtgafhyzwMrTUdNvaJX-NMNzReBIPCYddC3Oxd1o_-o33sAJ4VzV7wZwB82JNq0l_LhFOocF6vEBzH6db5UHNziQoj_W6yrXiG_SxGfsj36lzqYccvybkDjPbvyStaWU27hI-eDf1O2wU_NQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">احمد خاتمی، عضو مجلس خبرگان، در دیدار با اعضای شورای اداری شهرستان سیرجان با اشاره به وضعیت جسمانی مجتبی خامنه‌ای، گفت: در جریان حمله روز نخست جنگ، او از ناحیه پا دچار آسیب‌دیدگی شد؛ به‌گونه‌ای که احتمال قطع پا نیز مطرح بوده، اما این اتفاق رخ نداد و او هم‌اکنون در سلامت به سر می‌برد.
این در حالی است که از روز ۹ اسفند سال ۱۴۰۴ و حمله به دفتر علی خامنه‌ای، هیچ تصویر یا فایل صوتی از مجتبی خامنه‌ای منتشر نشده است.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 377K · <a href="https://t.me/VahidOnline/75974" target="_blank">📅 22:03 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75973">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/eAjIji8IHHuas3lVW7-3qiJQwAUo51_lJ2NirsbSjm63ZLMI4pmE9jsWynW2xBzlW8h5wF2FhVLakOw5KJesevzc6IFlhaXd_9ChGdaVOyFOsHhFvS6iEjUIq00gruFagtR0amO9d8Oyh-7kwbBSEJkmUMXlaks6hOCiozY-0hduKX5FqI4JHORHYVzHbDaMQRt0_xMNgMkXw8OFFqew3eXgkL07sU0YrA5kzt49iY4ab2U0z3UoNg5rtOUuv29FVMooiQWJKptY7ecr6UrHZuRoT5fVJlxapvIgG5YsbC5X2R7Vj2q7JYy3RQ8V88FGNevEWUMeMra92gqPJaLpQQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرگزاری ایسنا نوشت که محسن نقوی، وزیر کشور پاکستان، در جریان سفر به تهران حامل پیام ویژه‌ای از عاصم منیر، رییس ستاد کل ارتش پاکستان، به مجتبی خامنه‌ای است.
@
VahidOOnLine
خبرگزاری تسنیم، وابسته به سپاه پاسداران، روز شنبه ۱۶ خرداد ۱۴۰۵، گزارش داد محسن نقوی، وزیر کشور پاکستان، وارد تهران شده و قرار است با عباس عراقچی، وزیر امور خارجه جمهوری اسلامی دیدار و گفت‌وگو کند.
بر اساس این گزارش، نقوی پیش از سفر به تهران با شهباز شریف، نخست‌وزیر پاکستان، دیدار کرده و در جریان این ملاقات، دستورالعمل‌هایی درباره سفر به ایران و روند رایزنی‌های مرتبط با مذاکرات جمهوری اسلامی و آمریکا دریافت کرده است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 356K · <a href="https://t.me/VahidOnline/75973" target="_blank">📅 20:27 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75972">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/baDRXhqrcFluIM22s3oY3Waf1DW6N4v3K-cVUPZCkz2utenQAlfaqM4PXHpWRN8dBcPKPsgbvJWXQdeelSJI1jBRObNvzPKAa-quTOeGj0MmE_-N78Gj-Nv2JBGH6_1DFOvs1ti18GIK68t30BHRrCk0uJNZyZGntH2Y7OvjFjQ7Y0Hj0vGCntUDGM6TOQlBegt5k3g60ICifKgH2vIelzu_3uSL9gzkWaXGPocmgYQdQdHtoU8j2XQxMcTrMn1Cnw7u4AzCbk9SUoCPJCvz3JlzbOQTvG0XLLrwVBH1Nbvaj6vFmwc1eYVjGIghOW0ts9EROQGC7xNH85qhSeUjgg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">محمدرضا عارف، معاون اول مسعود پزشکیان، در بازدید از دانشگاه علم و صنعت گفت: در جنگ‌های اخیر شاهد مهاجرت معکوس نخبگان و مردم به کشور بودیم. باید از ظرفیت ایرانیان علاقه‌مند به خدمت به کشور استفاده کنیم و با طراحی مشوق‌های مناسب، زمینه بازگشت نخبگان و استادانان را فراهم سازیم.
او افزود: نباید دنبال این باشیم چرا استادان مهاجرت کرده‌اند، بلکه باید به بازگرداندن آنان بیندیشیم.
در روزهای اخیر، بینش بلور، معروف به قصیر، خواننده لس‌آنجلسی، با حضور در تهران در تجمع حامیان حکومت در میدان انقلاب ترانه اجرا کرد.
همچنین صدف طاهریان، بلاگر ساکن ترکیه، تمام پستهای صفحه اینستاگرام خود را حذف کرده و با انتشار استوری‌هایی، از حضور خود در ایران خبر داده است.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 352K · <a href="https://t.me/VahidOnline/75972" target="_blank">📅 20:03 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75971">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QZKFEk1Ov1RIt4EOKHE0SwGUxGGr4txrujFJ2E_PE9MT6uAoopwy6IkupB1-oJ10mz_ARvqi8EaVMMmRDb20OsAV4bJJPpiC1RWyWAgKDc75aMMhvXFASrK6TfrXnhiowxaTk4wyIuKcZlzUPg47QW4jWIXjoczjbJxIcZEzCO1K4lFCo0fm1_Lbfe8StHv2mrIfWrOsg6fEs4XxBpskTuEr1yM1k6M4CYFZzwxwc33tnpJmEQL8-vvxineZKnQoAmVv8c3NllevFTj6qarqMWmxOVuRSSMk7ASQMFcP8TwxPab9lk18OgKhkIF4gHu21iC7unjOSm95SAnTzW8rHg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزارت امور خارجه جمهوری اسلامی در بیانیه‌ای حمله بامداد شنبه ۱۶ خرداد ۱۴۰۵ ارتش آمریکا به تاسیسات راداری و نظارت ساحلی در منطقه سیریک و جزیره قشم را «نقض آشکار آتش‌بس» و «تجاوز نظامی علیه حاکمیت ملی و تمامیت سرزمینی ایران» خواند و آن را به شدت محکوم کرد.
در این بیانیه آمده است که تاسیسات هدف قرار گرفته، ماموریت حفاظت از امنیت مرزهای کشور و امنیت کشتیرانی در آبراه‌های بین‌المللی را بر عهده داشته‌اند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 319K · <a href="https://t.me/VahidOnline/75971" target="_blank">📅 19:56 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75969">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/kCogO7m8d5CJitw_wYpWD0yFb8YQMnHAHF3CD5bQEF_rQPR_oCyc7DQSnoDDEYKs3RHYymPAo3Mnx3lyN0eHBesLDVKQzNzekRKW8dg8uvgmjd6_5I6xLERHS1CN5E9N5ogFFjwfrq7N0_9ZHoVFGpyVV4989k745OCMN9TNHMkYqwlFCzwpBaz_H7AWoDsO-6GWXOC-3k38wOjY3aOL1JR4uy_qQLxWKfsnVpARToI0RN_fRTj7RvGGJr2iiHqPGpxfHqtKRLG-rWYPuXMcFrP9Lujc-XuS21awYFs1mx0plTQyIqUqljZbI3RTgBUQGFN0LnSVt5qGLrgO8BYygw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/mxQTT6-sIKg4ek_UlnbqnqyHuQblIeyUv4P1ZaxxASV4NhOqvsl-uUZDdWwDf9DJFgib87TtxQYgvcsoJ9Gv9yPF3IqeQR26Oncs51K7fqaNU3jKQj8TvNNXyCBOKCpC5Ce5QrLZYktcoYdCPF7FUNTl3hQcIYWKx7v4rxRyV1vvTO1ouz5mNNNGfvuezAk08XFGf9VedQnbz9ou8315TMlg-tNbS9hTrqezi-kz3GAB37Z7YpikN886iFH7yPh4d1pkejeb07Y1XDHpA32LZ46rp3Nl1tziCGqHUMDe7M7Vd4yR8oawWULT-u0uczWPTDGOOx-XGlms3GSZG5GfCg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">عباس عراقچی، وزیر امور خارجه جمهوری اسلامی، روز جمعه در شبکه ایکس در پاسخ به انتقاد صریح مقامات عالی‌رتبه لبنان تمام تقصیر را متوجه اسرائیل دانست.
نواف سلام، نخست‌وزیر لبنان، روز جمعه، ۱۵ خردادماه، در یک نشست مطبوعاتی با لحنی صریح رهبران ایران را خطاب قرار داد و گفت: «به جنوب ما رحم کنید؛ از تبدیل کردن آن و مردمش به یک برگۀ معامله دست بردارید.»
ژوزف عون، رئیس‌جمهور لبنان، نیز در مصاحبه با سی‌ان‌ان پیام مشابهی برای ایران داشت. او گفت: «اینجا کشور شما نیست، کشور ماست. مداخله در کشور ما وظیفۀ شما نیست.»
در پاسخ به این انتقادات که مقامات لبنان ماه‌هاست با صراحت مطرح می‌کنند، عراقچی در پیامی نوشت: «اگر لبنان ابزار معامله برای ایران بود، خیلی وقت پیش به توافق رسیده بودیم.»
وزیر خارجه جمهوری اسلامی در ادامه خطاب به عون نوشته است: «آقای رئیس جمهور، لبنان را از دست دشمن واقعی‌تان نجات دهید.»
عراقچی در پیام خود می‌گوید: «بر اساس گفته‌های آقای عون، هر کس باشد فکر می‌کند که ایران است که یک‌پنجم لبنان را اشغال کرده،‌ یک‌چهارم مردمش را آواره کرده و هر روز کشورش را بمباران می‌کند.»
@
VahidHeadline
ساعاتی بعد نیز اسماعیل بقایی، سخنگوی وزارت امور خارجه ایران، در پیامی به لهجه لبنانی نوشت: «بیبیع اللی واقف حدّو، وبیشتری اللی واقف ضدّو»؛ عبارتی که به معنای «کسی که کنار او ایستاده را می‌فروشد و کسی که مقابل او ایستاده را می‌خرد» است.
رئیس‌جمهوری لبنان همچنین خطاب به ایران و سپاه پاسداران گفته بود: «این کشور، کشور ماست نه کشور شما» و تاکید کرده بود که لبنانی‌ها از جنگ خسته شده‌اند و خواهان زندگی در صلح و ثبات هستند.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 306K · <a href="https://t.me/VahidOnline/75969" target="_blank">📅 19:53 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75968">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/04b6cd8529.mp4?token=kEMR22oiVsNvQI7CLTR0wEMgd6kGEF6Yu29CJihctkJE_GNueLQXaeNca6rkgNiDMMcXQQnZxyE5zL6mIJ2NQLlTAgv6AEHCGdStwa1lG4O5PUnB6vh1Wq5V6uHVZN2zxDWNezwuslXwcyH0pv8dvMXDfXSneGEOkMsQfZjaDTc0LKgBsq-w75eo1ij8EZwvlYX-GQMk03eb5dQ-OQw3tFRt7IcfHCRebcZOCkhZritlsa07iehz34qwRnQtCwwTHcKbBoEUoYswPuiOHvQdKNLjJqfnUj4YXC3NwS7KC4kBcriL9oschPou2Py9J3jAC32u0wdAkhHrUtOy9AyZbg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/04b6cd8529.mp4?token=kEMR22oiVsNvQI7CLTR0wEMgd6kGEF6Yu29CJihctkJE_GNueLQXaeNca6rkgNiDMMcXQQnZxyE5zL6mIJ2NQLlTAgv6AEHCGdStwa1lG4O5PUnB6vh1Wq5V6uHVZN2zxDWNezwuslXwcyH0pv8dvMXDfXSneGEOkMsQfZjaDTc0LKgBsq-w75eo1ij8EZwvlYX-GQMk03eb5dQ-OQw3tFRt7IcfHCRebcZOCkhZritlsa07iehz34qwRnQtCwwTHcKbBoEUoYswPuiOHvQdKNLjJqfnUj4YXC3NwS7KC4kBcriL9oschPou2Py9J3jAC32u0wdAkhHrUtOy9AyZbg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شماری از دانش‌آموزان اصفهان روز شنبه ۱۶ خرداد در اعتراض به حضوری برگزار شدن امتحانات تجمع کرده و با سر دادن شعار «دانش‌آموز داد بزن، حقتو فریاد بزن» خواستار تغییر نحوه برگزاری آزمون‌ها شدند.
@
VahidOOnLine
صدها دانش‌آموز روز شنبه ۱۶ خرداد در شهرهای مختلف ایران ازجمله تهران، مشهد، اصفهان، شیراز و چندین شهر دیگر تجمع اعتراضی برگزار کردند.
دانش‌آموزان در تهران مقابل دبیرخانه شورایعالی انقلاب فرهنگی و در شهرستان‌ها مقابل ساختمان وزارت آموزش و پرورش تجمع کردند.
آنها به تغییر قوانین کنکور و افزایش تاثیر معدل در کارنامه کنکور سراسری معترض هستند.
گزارش‌های غیر رسمی از حضور نیروهای انتظامی و یگان ویژه در اطراف محل تجمع دانش‌آموزان در مشهد حکایت دارد.
پیشتر هم صدها دانش‌آموز روز سه‌شنبه در شهرهای تهران، مشهد، همدان و چندین شهر دیگر با تجمع مقابل ساختمان وزارت آموزش و پرورش به تغییر قوانین کنکور و افزایش تاثیر معدل در کارنامه کنکور سراسری باتوجه به تاثیر منفی جنگ بر آمادگی آن‌ها برای آزمون ورود به دانشگاه اعتراض کردند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 310K · <a href="https://t.me/VahidOnline/75968" target="_blank">📅 19:50 · 16 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>

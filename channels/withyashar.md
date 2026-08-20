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
<img src="https://cdn4.telesco.pe/file/rD-B_9qY6QhjqkNKUYxDPIztv2EmZuimDk5WbswTXZETnefm-6qq_NccBMKitvCaUrFdxRqEJXMzrEtIQl7iu7TOHq_Rv-loqQYwgtJBTgk_nmhQCRG5w6HdHGjH7-BL1ynJuKxKLl2SyEeC4W_IkCbtZq-XRpMgDHGovu_UUN97xgdl12oPFHm4zDJ9lwMBZX8uING9shqwK34ynXqAyBPnKrL1_DfXHkYr9Q9uDRO_xPPNTo6kKtPwHkmZe6C1-ktYGugXF_PrTcRJbA5iiaALGJSQphC5yfg-e_9SqwOzMU7nH5gB1NBf9PfPEs1GsTR1LbiZrzq2XoCOT_Qc6A.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 WarRoom with YASHAR</h1>
<p>@withyashar • 👥 443K عضو</p>
<a href="https://t.me/withyashar" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 چنل رسمی«اتاق جنگ با یاشار»اخبار لحظه ای و فوری از‌ جنگ با تحلیل📸instagram.com/yashar🐦x.com/yasharrapfa📺youtube.com/yasharrapfa⛑️paypal.com/paypalme/yasharrapfa</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-29 21:02:54</div>
<hr>

<div class="tg-post" id="msg-21251">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">کانال 15 عبری : نتانیاهو در حال حاضر جلسه‌ای خصوصی با حضور روسای سازمان‌های امنیتی، از جمله سازمان‌های اطلاعاتی، برگزار می‌کند تا در مورد تمام تحولات آتی، به ویژه در سوریه و در روابط با ترکیه، بحث و تبادل نظر کنند. این اقدام در پی اعلام ترک‌ها مبنی بر ادامه فعالیت‌هایشان در سوریه صورت می‌گیرد.
@WarRoom</div>
<div class="tg-footer">👁️ 9.88K · <a href="https://t.me/withyashar/21251" target="_blank">📅 20:55 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-21250">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">اسکات بسنت، وزیر خزانه‌داری آمریکا:
دوشنبه جزئیات اقدامات جدید را اعلام می‌کنم. اگر سیاست
حداکثر فشار اقتصادی
ادامه یابد، فعلاً احتمال آغاز دوباره عملیات نظامی گسترده کم است. آمریکا در عین حال کنترل تنگه را در اختیار دارد و می‌تواند جریان انرژی را مدیریت کند. ما در حال اجرای
بزرگ‌ترین عملیات هماهنگ انزوای اقتصادی در تاریخ جهان
هستیم و به کشورها هشدار می‌دهیم که اگر به تجارت، انتقال پول، خرید نفت یا انتقال کشتی‌به‌کشتی با ایران ادامه دهند، با تمام توان تحریمی آمریکا مواجه خواهند شد. هدف،
درهم‌کوبیدن اقتصاد این رژیم جنایتکار، قطع توان مالی آن برای حمایت از نیروهای نیابتی و تأمین هزینه‌های نظامی
است. بسنت تأکید کرد: «این روش در همه جا جواب داده؛ ما یک ضربه دوگانه شامل
محاصره و سخت‌ترین تحریم‌های تاریخ
وارد می‌کنیم و
در ایران نیز موفق خواهد شد. ما این رژیم را فرو خواهیم ریخت.
@WarRoom</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/withyashar/21250" target="_blank">📅 20:43 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-21249">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">بسنت ، وزیر خزانه‌داری آمریکا:  ما نظام ایران را سرنگون خواهیم کرد @WarRoom</div>
<div class="tg-footer">👁️ 29.3K · <a href="https://t.me/withyashar/21249" target="_blank">📅 20:22 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-21248">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">‏وزارت جنگ ایالات متحده در حال بررسی برکناری مکس لدرر، ناشر باسابقه روزنامه نظامی «استارز اند استرایپس»، پیش از موعد بازنشستگی اوست. این اقدام پس از انتشار گزارش‌های انتقادی فیک این روزنامه درباره وضعیت خدمه ناو هواپیمابر «آبراهام لینکلن» در جریان جنگ علیه جمهوری اسلامی و همزمان با تشدید اختلاف میان این رسانه و مقام‌های نظامی آمریکا مطرح شده است.
@WarRoom</div>
<div class="tg-footer">👁️ 35.7K · <a href="https://t.me/withyashar/21248" target="_blank">📅 20:09 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-21247">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SpZG7G-Ghs6cp-xTTIOzy3m_b09nCP4PV6l5g07GsesAqUknWr07onOBTsuRxLvTJm3V-PS8UDH6BMdZGQtFxGxkAGSrEBtIX9Yw32bBzdgQ4izXGG0BF_DSeZFEKEJyZ4W_UyyjZIKnJrpBZsSVVQesmaVnBGlchSfoxq9taWgv2wEGY2Houpa6d9VZmacHEUAH8byrF0bn0eKppwihFmzn6O4u_vhJcm4DuozxpkiCbcoBvbc5X0JClKuCh7EJzRjvyo-icynKDbWLckmfkWrnTb4r6tKI1F88895iqAJ40gWYxvzsb5RH6IU8mNPudNrfejfo_Zrfu7A5du1rjg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سنت‌کام : نیروهای ایالات متحده از زمان تقویت محاصره بنادر ایران، ۶۷ کشتی تجاری را تغییر مسیر داده‌اند، ۳ کشتی را غیرفعال کرده‌اند و ۲ کشتی را برای اطمینان از رعایت مقررات به بازجویی و بازرسی برده‌اند.
@WarRoom</div>
<div class="tg-footer">👁️ 41.2K · <a href="https://t.me/withyashar/21247" target="_blank">📅 19:55 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-21246">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">کانادین پرس :
پیر پویلیور،
رهبر حزب محافظه‌کار کانادا و رهبر اپوزیسیون رسمی این کشور
، از رضا پهلوی، ولیعهد ایران، دعوت کرده است به کانادا سفر کند. پویلیور روز شنبه در مراسمی در بریتیش کلمبیا اعلام کرد که علاوه بر این دعوت، قرار است به‌صورت مجازی با رضا پهلوی دیدار کند. او در این مراسم گفت این دیدار فرصتی برای گفت‌وگو درباره
دموکراسی و امنیت ایرانیان خارج از کشور
است.
@WarRoom</div>
<div class="tg-footer">👁️ 54.4K · <a href="https://t.me/withyashar/21246" target="_blank">📅 19:04 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-21245">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">بسنت درباره ایران: ما از این وضعیت مناقشه با ایران عبور خواهیم کرد. نمی‌دانیم چه زمانی. @WarRoom</div>
<div class="tg-footer">👁️ 58.4K · <a href="https://t.me/withyashar/21245" target="_blank">📅 18:53 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-21244">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ae3286979e.mp4?token=cbDolKyd-8dKTzKE7umfWhnM3fOYJitZT37elXu4LeGhC7HxWXOZDDYLBpaIC5b422EF-8zJfu_QCw0gT5_Z3ZZ8bp5W6r-4jfsO7Fys8q3NoYjxQSCejAnIBqA0Zcp2B5hYARK7_JKDcejqM99ysi7vAQPI7qK5SajcJcT6hoVg9n4RvpUy7OIqnug8QE7IHHyYDiidlmg9aEhAdrLu38PY2K0PmtZfoNn7mKtvY851qlGznQS6TSVtDKprJhhFCNqGOulkAmH4VsH-4p21BRy-0-4KCRDTlF4dy_tXW59pMWPhyTEj3Rt6RWpdWgYkyVJtwkN4EQ1Ch2uaYYCcgA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ae3286979e.mp4?token=cbDolKyd-8dKTzKE7umfWhnM3fOYJitZT37elXu4LeGhC7HxWXOZDDYLBpaIC5b422EF-8zJfu_QCw0gT5_Z3ZZ8bp5W6r-4jfsO7Fys8q3NoYjxQSCejAnIBqA0Zcp2B5hYARK7_JKDcejqM99ysi7vAQPI7qK5SajcJcT6hoVg9n4RvpUy7OIqnug8QE7IHHyYDiidlmg9aEhAdrLu38PY2K0PmtZfoNn7mKtvY851qlGznQS6TSVtDKprJhhFCNqGOulkAmH4VsH-4p21BRy-0-4KCRDTlF4dy_tXW59pMWPhyTEj3Rt6RWpdWgYkyVJtwkN4EQ1Ch2uaYYCcgA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بسنت درباره ایران: ما از این وضعیت مناقشه با ایران عبور خواهیم کرد. نمی‌دانیم چه زمانی.
@WarRoom</div>
<div class="tg-footer">👁️ 57.8K · <a href="https://t.me/withyashar/21244" target="_blank">📅 18:52 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-21243">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">مسرور بارزانی، نخست‌وزیر اقلیم کردستان عراق به المانیتور با اشاره به بیش از
۱۰۰۰ حمله موشکی و پهپادی
علیه اقلیم از زمان آغاز جنگ آمریکا و اسرائیل با ایران در ۲۸ فوریه، خواستار تقویت پدافند هوایی شد. او هشدار داد خروج سامانه‌های
پاتریوت و نیروهای آمریکایی
، اقلیم را آسیب‌پذیرتر می‌کند و از آمریکا و متحدانش خواست برای تأمین پدافند هوایی، سامانه‌های هشدار زودهنگام و تجهیزات مقابله با پهپاد کمک کنند. بارزانی همچنین گفت حملات اخیر به دفتر شخصی او و خانه رئیس شورای امنیت اقلیم با هدف
ارعاب و کشاندن اقلیم به درگیری
انجام شده است. او مدعی شد پهپادهای استفاده‌شده در این حملات
ایرانی و از نوع حدید-۱۱۰
بوده‌اند و هیچ کس دیگری ندارد؛ ادعایی که ایران آن را رد کرده است
@WarRoom</div>
<div class="tg-footer">👁️ 72.9K · <a href="https://t.me/withyashar/21243" target="_blank">📅 17:19 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-21242">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">اتاق جنگ با یاشار : فلورا جون ۲ @WarRoom</div>
<div class="tg-footer">👁️ 92.6K · <a href="https://t.me/withyashar/21242" target="_blank">📅 15:13 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-21241">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">العربیه : ۳ نفر از نیروهای سپاه در حملات به مواضع حوثی های یمن کشته شدند
@WarRoom</div>
<div class="tg-footer">👁️ 91.3K · <a href="https://t.me/withyashar/21241" target="_blank">📅 15:08 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-21240">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">یک مقام آمریکایی و یک مقام کاخ سفید به خبررگزاری سمافور گفته‌اند که دولت آمریکا معتقد است
مذاکرات ایران و عمان از چند هفته قبل عملاً شکست خورده است
. احتمال دریافت عوارض از کشتی‌ها برای عبور از تنگه هرمز و پیشبرد سازوکاری جدا از مذاکرات مستقیم تهران و واشنگتن از دلایل اصلی نارضایتی دولت ترامپ عنوان شده است.
@WarRoom</div>
<div class="tg-footer">👁️ 97.5K · <a href="https://t.me/withyashar/21240" target="_blank">📅 14:05 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-21239">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">نتانیاهو: بازسازی نوار غزه تنها در صورتی امکان‌پذیر خواهد بود که حماس به طور کامل از سلاح‌های خود محروم شود.
@WarRoom</div>
<div class="tg-footer">👁️ 99.4K · <a href="https://t.me/withyashar/21239" target="_blank">📅 13:35 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-21238">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">نتانیاهو : شما سورپرایز خواهید شد
@WarRoom</div>
<div class="tg-footer">👁️ 106K · <a href="https://t.me/withyashar/21238" target="_blank">📅 12:57 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-21237">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a5cd8ea5eb.mp4?token=tKjrzqK0vYJyRf84bDnBJLTSbPgF42V_LoSTPWHrhNF0NOqSa6tdsbC2J0_-MveuFYsayUOktaNgBTQp0JqV44iFAy0RT-5LqFLTzuv6wcupCxNfJxl-dJiW-3QfdRCHvQO9GuiOkMdfT-mnygWE3h8q7pr1HKaDhJ7GgWbzwoKNRH2gFAzQ7nXMoA3KPZTGD9xyLJUqWi3j8nbj1diYcpEcvKiDIPbbn23TleYr2Voon-5Zv1pBsXM5DsHguCHilDkZAt9UCLkrqy7NjUZxETxqhfO780pGh9EGyS767M32knrAlJ7WbmSdsWd7lbU710G1PclGpQrcyga9ztjtoQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a5cd8ea5eb.mp4?token=tKjrzqK0vYJyRf84bDnBJLTSbPgF42V_LoSTPWHrhNF0NOqSa6tdsbC2J0_-MveuFYsayUOktaNgBTQp0JqV44iFAy0RT-5LqFLTzuv6wcupCxNfJxl-dJiW-3QfdRCHvQO9GuiOkMdfT-mnygWE3h8q7pr1HKaDhJ7GgWbzwoKNRH2gFAzQ7nXMoA3KPZTGD9xyLJUqWi3j8nbj1diYcpEcvKiDIPbbn23TleYr2Voon-5Zv1pBsXM5DsHguCHilDkZAt9UCLkrqy7NjUZxETxqhfO780pGh9EGyS767M32knrAlJ7WbmSdsWd7lbU710G1PclGpQrcyga9ztjtoQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">روابط عمومی پالایشگاه نفت تهران:
ستون‌های دود در آسمان تهران، ناشی از آتش‌سوزی در دو مخزن مربوط به بسته‌بندی و انتقال محصولات نفتی، در محوطه پالایشگاه نفت در پایتخت تهران است. هیچ آتش‌سوزی در داخل خود پالایشگاه رخ نداده است.
@WarRoom</div>
<div class="tg-footer">👁️ 107K · <a href="https://t.me/withyashar/21237" target="_blank">📅 12:37 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-21236">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">رسانه‌های سعودی به نقل از منابع گزارش دادند:
دولت ترامپ از اطلاعاتی درباره یک طرح ایرانی برای عملیات‌هایی که فراتر از هدف قرار دادن کشتی‌ها است، و همچنین طرح نیروهای یمنی برای افزایش هدف قرار دادن کشتی‌ها در تنگه باب‌المندب، مطلع شده است.
ترامپ به تیم خود اطلاع داده است که در صورت ناکارآمدی تحریم‌های اقتصادی، احتمال انجام حملات گسترده علیه ایران وجود دارد.
@WarRoom</div>
<div class="tg-footer">👁️ 102K · <a href="https://t.me/withyashar/21236" target="_blank">📅 12:29 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-21235">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">بیتکوین در حال پرواز است و با قدرت از مرز ۷۱،۰۰۰ دلار هم عبور کرد.
@WarRoom</div>
<div class="tg-footer">👁️ 105K · <a href="https://t.me/withyashar/21235" target="_blank">📅 11:45 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-21234">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e050dd4cf1.mp4?token=CfXFokdN_zRmiSS74QsKxJISX9G71-nPLImkYx4oUQExHo2PtNLLmZRbqlKDywGKvD_tWNFH3xcOd5BTcQN6KD4SciNyY8Zi9MLuhq82Sl4XVi0oABtyClMLLLgJL9VB_MHvcP3SCWqdQmtWzR8Kh7IQTZgr1_0-TTn2RD4yDtEr5Kag-ap7wnxwS-aJ7zn3hexO-3P1l8zZeN_lEJVO8xv-rhDAevtpW-bbV4BOBaSap21ptJemGvPFHvxq9t4gOgzyZIIRyeJQbHM9la56G1p-R9OB9t6BhHMcB4DRq7MA8dlr1TZ2BEDw8Y72VVwNOB69JmHByXBJDvhc-8AWRY3-5RUgFttzG2_82JYa4CHyD7NHA2gCM2XSJ3pUDlcRwKOSI6e0qFzbsm3gXIDyHwQ_HAEGcaQ_JmlOdwix1EEGq6PuQ--GzxqUF_J2K0uT_1Bmj7It5uARA7X_RBYqPErIdZuTw6O2s_LXDpFcN7_e33BO3toVWG1G43Rc8pVVjO8TX7oB-6LqxIQU_a-mq6-FQyUWvs-d5eHEpPrd4I30EjN_WjBcb1_am5FJIUJ5aa6xqz7qiI5yOBsoShbS4ouT0QMBptkFPwAnug1OAn_pEEWeRixoQQjgRuLRbRp3T3KP3aJb0baKjaTluapvfkqFlDL6-V7-mJUPrlVGxao" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e050dd4cf1.mp4?token=CfXFokdN_zRmiSS74QsKxJISX9G71-nPLImkYx4oUQExHo2PtNLLmZRbqlKDywGKvD_tWNFH3xcOd5BTcQN6KD4SciNyY8Zi9MLuhq82Sl4XVi0oABtyClMLLLgJL9VB_MHvcP3SCWqdQmtWzR8Kh7IQTZgr1_0-TTn2RD4yDtEr5Kag-ap7wnxwS-aJ7zn3hexO-3P1l8zZeN_lEJVO8xv-rhDAevtpW-bbV4BOBaSap21ptJemGvPFHvxq9t4gOgzyZIIRyeJQbHM9la56G1p-R9OB9t6BhHMcB4DRq7MA8dlr1TZ2BEDw8Y72VVwNOB69JmHByXBJDvhc-8AWRY3-5RUgFttzG2_82JYa4CHyD7NHA2gCM2XSJ3pUDlcRwKOSI6e0qFzbsm3gXIDyHwQ_HAEGcaQ_JmlOdwix1EEGq6PuQ--GzxqUF_J2K0uT_1Bmj7It5uARA7X_RBYqPErIdZuTw6O2s_LXDpFcN7_e33BO3toVWG1G43Rc8pVVjO8TX7oB-6LqxIQU_a-mq6-FQyUWvs-d5eHEpPrd4I30EjN_WjBcb1_am5FJIUJ5aa6xqz7qiI5yOBsoShbS4ouT0QMBptkFPwAnug1OAn_pEEWeRixoQQjgRuLRbRp3T3KP3aJb0baKjaTluapvfkqFlDL6-V7-mJUPrlVGxao" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اتاق جنگ با یاشار : فلورا جون ۲
@WarRoom</div>
<div class="tg-footer">👁️ 109K · <a href="https://t.me/withyashar/21234" target="_blank">📅 10:56 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-21233">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CBM6kMV1Hwi-9dWv2CncqqUuZks4iDB9HBwsvwIAcZaruh7GAvObxVp_d0CGoQcyKAVO1pk4tWraCSO1q0bqYC944tKv0iLg-MjB0Yiuk9_XbfcTjlEBrTjdJluio0Md-Gt_mNIUtaDHrFWFoeuc3uZ3avIONvXrUkbfMrOaZ6FbGboRDe3_qEYXnTV0vRnCwUXt9ouPfpG10OWMNhbhgh4EGg4MK9SMwcmc_vI16uncETo_pD_TDtE7MGRFcUGR85NDvMx3Bdig9vpm7rTOY-TOS-m_T5Jd_6v3WI6T3ysIz170SNdRICnxsocqnFGWonVTg2SAiMxyhLgBhsyAsg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قوه قضائیه اعلام کرد: حکم قائم حسینی معروف به آرین ، تبعه خارجی و از متهمان پرونده موسوم به «میدان علیخانی» اصفهان، اجرا شد.
@WarRoom</div>
<div class="tg-footer">👁️ 108K · <a href="https://t.me/withyashar/21233" target="_blank">📅 10:22 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-21232">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">اکسیوس گزارش داد که ارتش آمریکا در اقدامی محرمانه، یک کریدور دریایی در مسیر ورود و خروج کشتی‌ها از تنگه هرمز ایجاد کرده است
تا روزانه میلیون‌ها بشکه نفت از این مسیر عبور کند؛ اقدامی که به گفته دو مقام آمریکایی، با وجود بن‌بست در جنگ، موفقیتی قابل توجه برای واشنگتن محسوب می‌شود.
بر اساس این گزارش، این عملیات طی چند هفته گذشته در جریان بوده و هر شب حدود ۱۵ تا ۲۰ نفتکش از طریق یک مسیر جنوبی در امتداد سواحل عمان وارد تنگه هرمز شده یا از آن خارج می‌شوند.
@WarRoom</div>
<div class="tg-footer">👁️ 110K · <a href="https://t.me/withyashar/21232" target="_blank">📅 08:01 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-21231">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KBnd-YGSWQomt0JCsJe4zjGkaMx0yMSgbowdWEK9UeK6yCwYrw4g3WDmPUrQkfwBI37O3KPYmTJaKjB96WivVxSeyqj4AanNqPisXz0HzuBuUXAuGKj6-yBZVVN-9lrztPuf-e7NXbuHl29VAlpN35WD_DNRYTq6mvuKYlIbxJYX5-xzTbm0FmM_jW3byXO7oWMVKDoAhIBYL85bJT24FetmBMNnq8G8jBryIpSnghcR_fcbyVURJvxuLDqz0aFWtnkBAfJa89A0Vo4cQ0y_2lsH4ndqO-jAS7sxFvsePKMbz3FytFZSTauP3IO95yU3vMK85UUnpQUadGGv0__9ww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ در تروث : هیچ‌کس به‌اندازه من به جمهوری اسلامی ایران فرصت نداده است تا به یک توافق برسد. متأسفانه، آنها از این فرصت استفاده نکردند. بنابراین، امروز اعلام می‌کنم که
کمرشکن‌ترین عملیات اقتصادی‌ای که تاکنون علیه هر کشوری انجام شده است
را آغاز خواهیم کرد! این عملیات، جنگ اقتصادی و انزوایی در مقیاسی بی‌سابقه خواهد بود. نیروی دریایی آنها از بین رفته، نیروی هوایی‌شان نابود شده، کارخانه‌های نظامی‌شان به ویرانه تبدیل شده و ارزش پولشان از بین رفته است؛ کشورشان نیز به تار مویی بند است. امروز همچنین اعلام می‌کنم که
هر کشوری که به مؤسسات مالی، شرکت‌ها، فرودگاه‌ها یا نهادهای دولتی خود اجازه دهد هرگونه کمک حیاتی به ایران برسانند، خودش با پیامدهای اقتصادی بسیار سنگینی روبه‌رو خواهد شد.
قاچاق نفت، خطوط مبادله ارزی، انتقال پول نقد، صرافی‌ها، ثبت کشتی‌ها و شرکت‌های پوششی —
همه اینها باید همین حالا متوقف شوند.
خودتان می‌دانید چه کسانی هستید. این یک
«روز دی اقتصادی»
خواهد بود و ما نیاز داریم همه متحدانمان در کنار ایالات متحده آمریکا بایستند تا تهدید ایران را منزوی و شکست دهند. این دیوانگان در آخرین نفس‌های خود هستند و این اقدامات تاریخی، آنها و توانایی‌شان برای گسترش تروریسم در سراسر جهان را فلج خواهد کرد.
ایران هرگز به سلاح هسته‌ای دست نخواهد یافت.
@WarRoom</div>
<div class="tg-footer">👁️ 117K · <a href="https://t.me/withyashar/21231" target="_blank">📅 07:54 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-21230">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">بامداد نیک و خجسته ، پیج اینستاگرام رو برگرگردوندم ، خواب بودم
instagram.com/yashar
پیج دوم پشتیبان :
instagram.com/yasharmotors</div>
<div class="tg-footer">👁️ 109K · <a href="https://t.me/withyashar/21230" target="_blank">📅 07:52 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-21229">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b17a03cc01.mp4?token=V97PMqM_N3hosT91z7Tvxg30V8S3pCvnSF1JF38sl2Xw5K-koIqEnraxjJjAjCF_6l47VLsE2GrNiyvT7hSudqhO1LK-sw2Mf6nzPSVcTsGugDub2IsoEDKYxSsu7gppOovcEaqsRFdnft52xl6CCAx7wCv1EtUyI-9IxhR0SJkWtnDzRnBfa9vfv3PoyS4BWqGzk-GiV0z78knlQYH5CQqBSWdYv8ePFsbXfE_TsOAeinVld96llnaZguaKvsYK3rqFe3Ju_H_gYjEqutaktbsFc0gpI8s9xSpIdVv6qfYBKlUfI14sKYyO0PZCD3BPZKDHgelGKMTi4qXUUUt1Cy6oPYmYpG6HWQUR20cnD0NmptJFoUdZSN8fS2c2ouveI6UhQTTOBnMCKXtzptpmign8OfU7k8m2Iwe4gBGn7ULApkC4BVNzhrrsb2OD1a_wZT7IxeGItENPHwfyQzRKj3Nv3Y__IFkT-VJ8bDQOo00x_gK-s1ddiwRnTs8xnw0F_rnc9MaNMV1Uc1hN2zzD1NKjCZ9I1ZIs_5KJ-ZO7E7vA7eapIigLyv4PccO1SF76W59eY-VzMhlN0WGw6d-qS-rm6jc2ZxwY6lrmP22Z_E1hlOypUrt4dMa9jbsN4FBTle1UEl18lnBej2pU2N1J8HI-QiJLd7XWb3G9EoCUP-E" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b17a03cc01.mp4?token=V97PMqM_N3hosT91z7Tvxg30V8S3pCvnSF1JF38sl2Xw5K-koIqEnraxjJjAjCF_6l47VLsE2GrNiyvT7hSudqhO1LK-sw2Mf6nzPSVcTsGugDub2IsoEDKYxSsu7gppOovcEaqsRFdnft52xl6CCAx7wCv1EtUyI-9IxhR0SJkWtnDzRnBfa9vfv3PoyS4BWqGzk-GiV0z78knlQYH5CQqBSWdYv8ePFsbXfE_TsOAeinVld96llnaZguaKvsYK3rqFe3Ju_H_gYjEqutaktbsFc0gpI8s9xSpIdVv6qfYBKlUfI14sKYyO0PZCD3BPZKDHgelGKMTi4qXUUUt1Cy6oPYmYpG6HWQUR20cnD0NmptJFoUdZSN8fS2c2ouveI6UhQTTOBnMCKXtzptpmign8OfU7k8m2Iwe4gBGn7ULApkC4BVNzhrrsb2OD1a_wZT7IxeGItENPHwfyQzRKj3Nv3Y__IFkT-VJ8bDQOo00x_gK-s1ddiwRnTs8xnw0F_rnc9MaNMV1Uc1hN2zzD1NKjCZ9I1ZIs_5KJ-ZO7E7vA7eapIigLyv4PccO1SF76W59eY-VzMhlN0WGw6d-qS-rm6jc2ZxwY6lrmP22Z_E1hlOypUrt4dMa9jbsN4FBTle1UEl18lnBej2pU2N1J8HI-QiJLd7XWb3G9EoCUP-E" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اتاق جنگ با یاشار : خونثانیاهو
@WarRoom</div>
<div class="tg-footer">👁️ 126K · <a href="https://t.me/withyashar/21229" target="_blank">📅 00:15 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-21227">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/C6sFeWtfYQXI82ZE_EF0baTOhgcYhn-TMrhNjg4k36DaL-h0jzPvlZc2EDci0HGqGk9YTHUf9XioekFkn2bpBJqfNmodxTOcHgErNSTVdvYhsVmsoLHlGA7FeMq-6rRadauqYx_lwwRPMFUTxxEu3tJ1wGyAaoQBq54P1sPZIK69mee4BEgBQt9U5xVFh7NPO5mc-_OcB5IdyxgQW-7hbKmRlEXeLSw1qmRm48hj1Z59YiHeIvLFNc5OaR1xYC61jHFTg1LZ-v4Z5q9O-mnyZGN81LjrUzZYYdLALBsf-FX8rkabDAsRjGqe_y1xkDzulsXBNf46Ptd1bhHN-n_P-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/cKWWRlZa7-69bBHZKvAefSsNuwMY3jQ6YHaxr5x7pznAqVI2AqcCZ2p4wFGhRnzOUsJBqwgnfdkSdP9ghd9AxIRTlvksZ26z7DVbQCbYAI4VkVRTTMHmDIbuo_bgwiyuX7_gar8tWlcCvvlBNZOCbyjnijL8AXXo0YM5LsV7bf2la1SXCRLRanBB_ctBDGTA8W94iI3i3Y3TGOSsRHtj0PRNlIdZTq5Dpelrqcc4czMcSJ03pxDFQrqCUfLSFXH-Np4Fz4iFqRgQl7J7G7aB01wqfjFHmRZ8vCUvDnYUqS8C_U6FrIiHyTUTTV5nYbffZnPTHh3surzZ4tRYZLSioQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">تویت جدید مم باقر که با سرش تنگه هرمز رو بسته نگه داشته
🤣
@WarRoom
یاشار : خودش داره میگه تنها راش اینه سرم بره</div>
<div class="tg-footer">👁️ 127K · <a href="https://t.me/withyashar/21227" target="_blank">📅 23:34 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-21226">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f25637c93b.mp4?token=HiV6Jal7DlL8798TRI6JnF-yXJv_efliPhj0RexAtRSWEF6HxKrQ2nhWfR_jBO27fYtmGShENcVjIg98xjocjvzRxMLYYNoC7a0HelYS81hO_RQc6_FsAerldu1mnBVXuNwaHRKicnCMCZpdJnMpxHj6dCRJv6xDXouQnnVh0X0fufWi0i77xszieQ0kgIULnn86_mxKlZzLYQ4hoAosW-r0jmrXsyh333YvbhQF0AGINXMk6X7yV3N8vztY6yjZoYt48UxYNF_ApzCahkXsplxy0_GCKoA1DHJM8B6Zpl--pNQfve1hEsefVrH2cL2MpUUNLPGk5BIxegnZEMZSRw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f25637c93b.mp4?token=HiV6Jal7DlL8798TRI6JnF-yXJv_efliPhj0RexAtRSWEF6HxKrQ2nhWfR_jBO27fYtmGShENcVjIg98xjocjvzRxMLYYNoC7a0HelYS81hO_RQc6_FsAerldu1mnBVXuNwaHRKicnCMCZpdJnMpxHj6dCRJv6xDXouQnnVh0X0fufWi0i77xszieQ0kgIULnn86_mxKlZzLYQ4hoAosW-r0jmrXsyh333YvbhQF0AGINXMk6X7yV3N8vztY6yjZoYt48UxYNF_ApzCahkXsplxy0_GCKoA1DHJM8B6Zpl--pNQfve1hEsefVrH2cL2MpUUNLPGk5BIxegnZEMZSRw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ در مورد ایران:
ما چیزهایی داریم که می‌توانیم علیه ایران تحریم کنیم. ما تحریم‌های بسیار سختگیرانه‌ای داریم و خواهیم دید چه اتفاقی می‌افتد.
@WarRoom</div>
<div class="tg-footer">👁️ 123K · <a href="https://t.me/withyashar/21226" target="_blank">📅 23:22 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-21225">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0003edd740.mp4?token=vVES2fALxOKdRJTho8e01gvpiBaH-Uv7QzfECQgCha1bNWH78C1RhdUuaY0gVBIuuskffiHWEW4hsAOr-gJwpd0PK8GAdqzyU4vcRbbRzodXWrex1Mi4EECQ0ItendKbDn-Juh7isHYp3KV6Qpbh-YjjnZVALfsHPuLD4HGB0vDGmOmdk6Ls0ypvZ2XDxxOTygUeSO3oGxiXTLvpXXbeElh_W9pF2QUOWth8ZdoPAUtJnp3tux0KXikdjUhdW4sk4TzwIj1aDaxGNjplVfUVt12l6plWk37uUKEyjmyaBsgxX3qT0lRk48qEXGj8qwXhsajCoIRb2v0rbHc8RrS3aw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0003edd740.mp4?token=vVES2fALxOKdRJTho8e01gvpiBaH-Uv7QzfECQgCha1bNWH78C1RhdUuaY0gVBIuuskffiHWEW4hsAOr-gJwpd0PK8GAdqzyU4vcRbbRzodXWrex1Mi4EECQ0ItendKbDn-Juh7isHYp3KV6Qpbh-YjjnZVALfsHPuLD4HGB0vDGmOmdk6Ls0ypvZ2XDxxOTygUeSO3oGxiXTLvpXXbeElh_W9pF2QUOWth8ZdoPAUtJnp3tux0KXikdjUhdW4sk4TzwIj1aDaxGNjplVfUVt12l6plWk37uUKEyjmyaBsgxX3qT0lRk48qEXGj8qwXhsajCoIRb2v0rbHc8RrS3aw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ درباره ایران:
خطوط لوله زیادی در حال ساخت هستند. من فکر می‌کنم تنگه هرمز به اندازه گذشته مهم نخواهد بود.
در حال حاضر، تنگه باز است. قایق‌های زیادی از آن عبور می‌کنند. مردم این را گزارش نمی‌کنند.
@WarRoom</div>
<div class="tg-footer">👁️ 122K · <a href="https://t.me/withyashar/21225" target="_blank">📅 23:11 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-21224">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">ترامپ: در حال حاضر با ايران مذاکره نمی‌کنیم، زیرا مذاکره با آن‌ها اتلاف وقت است.
@WarRoom</div>
<div class="tg-footer">👁️ 117K · <a href="https://t.me/withyashar/21224" target="_blank">📅 23:08 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-21223">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Oy0R7sVdYAritd2tcy02nEelMkM-T26Bbxg7o0ShfVLhSKw-wEpCpo0KTvZF3SbRvTMsF-MvVu4wqzINT2wRbokCnBKwsqmCVJkqKXuyYdVHnGMdCUrYujdBlqhq0zwQ3GqNQXYXxFkfRDcmsUhrGeXqIxjHk3yY1tZY6C5TKQRi9ZQmTnR2WogUIxUHsYKAlmszdTftZrSgcuF1pOzyapabqX0RtD0amKKZxPJYKF4zuVsz-YT68RnoQXQ97i9fpd-Cea8sQB6jGuzPfCw0LgS8fPAhhXOsYZXKj9TJAWbzaKEWvpjlIj0xGMoSLBFEuwhEAjdw7XtmETjbV8WxHw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فرانسه نیلوفر شادمهری، رایزن فرهنگی جمهوری اسلامی را از این کشور اخراج کرد.
@WarRoom</div>
<div class="tg-footer">👁️ 122K · <a href="https://t.me/withyashar/21223" target="_blank">📅 22:34 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-21222">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">زلزله ۴.۲ ریشتری حوالی گیلانغرب در استان کرمانشاه را لرزاند
@WarRoom</div>
<div class="tg-footer">👁️ 116K · <a href="https://t.me/withyashar/21222" target="_blank">📅 22:29 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-21221">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">کانال 13 اسرائیل به نقل از یک منبع نظامی: آخرین چیزی که به آن نیاز داریم، یک جنگ تمام‌عیار با ترکیه است. ما از میدان‌های درگیری کافی در حال حاضر برخورداریم.
@WarRoom</div>
<div class="tg-footer">👁️ 119K · <a href="https://t.me/withyashar/21221" target="_blank">📅 22:06 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-21220">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">نتانیاهو: ما توضیح دادیم که با حضور نظامی ترکیه در سوریه مخالفیم، و به نظر می‌رسد که آنها به خوبی به ما گوش ندادند، بنابراین تلاش کردیم تا آنها بهتر درک کنند.
@WarRoom
😁</div>
<div class="tg-footer">👁️ 121K · <a href="https://t.me/withyashar/21220" target="_blank">📅 21:34 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-21219">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">ممرضا نقدی : ما باید به بازدارندگی دست پیدا کنیم. برای ما خوب نیست که کسی بتواند تصمیم بگیرد به ایران حمله کند، و سپس، در صورت شکست، عقب‌نشینی کند، خود را سازماندهی کند و شش ماه بعد دوباره بازگردد.
@WarRoom</div>
<div class="tg-footer">👁️ 120K · <a href="https://t.me/withyashar/21219" target="_blank">📅 20:57 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-21218">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">مارک لوین : من با ویکتور دیویس هنسون (مورخ، نویسنده و تحلیلگر سیاسی آمریکایی) موافقم؛ او در برنامه من در فاکس نیوز استدلال کرد که ما باید از تشکیل یک دولت در تبعید ایران با رهبری شاهزاده رضا پهلوی حمایت کنیم. و اگر رژیم ایران فروبپاشد، او می‌تواند در دوران گذار، به‌عنوان یک رهبر موقت ایفای نقش کند.
به مردم ایران سلاح بدهید!
@WarRoom</div>
<div class="tg-footer">👁️ 121K · <a href="https://t.me/withyashar/21218" target="_blank">📅 20:24 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-21217">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">رویترز: بریتانیا امروز ۷ فرد و نهاد جدید مرتبط با ایران را به فهرست تحریم‌های خود اضافه کرد. این تحریم‌ها در چارچوب تحریم‌های رژیم ایران اعمال شده
@WarRoom</div>
<div class="tg-footer">👁️ 117K · <a href="https://t.me/withyashar/21217" target="_blank">📅 20:06 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-21216">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">ارتش اسرائیل: ما دیروز در منطقه ساحلی، یک فرمانده گردان و سه فرمانده گروه را از نیروهای نخبه در گردان بیت لاهیا وابسته به حماس به هلاکت رساندیم.
@WarRoom</div>
<div class="tg-footer">👁️ 113K · <a href="https://t.me/withyashar/21216" target="_blank">📅 20:00 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-21215">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">ترامپ امروز در کاخ سفید با شماری از مدیران و چهره‌های بزرگ صنعت رمزارز دیدار می‌کند. در این نشست، مقررات جدید بازار کریپتو، قانون CLARITY و تعیین حدود اختیارات SEC و CFTC بررسی خواهد شد. رؤسای SEC و CFTC و مدیران شرکت‌هایی از جمله Coinbase و Ripple نیز در این نشست حضور خواهند داشت
@WarRoom</div>
<div class="tg-footer">👁️ 112K · <a href="https://t.me/withyashar/21215" target="_blank">📅 19:37 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-21214">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ab2cd42e14.mp4?token=D9QJrXbs_dq6snmuuBAgcVN0EwcLCmR2LXXMvm_qZE9OMRJQ14a-eGLARdXihHzFuuFP5Cd3pE-XnrfRkJCvA0CAoPD8zHJae0Gy4LfHFA8Ba_WBDnBHtNjwqwrhLSfNsgAhfReBjD9KO6dhotTVdCrbPsmscja1Gbg55eXVfTLPorpGHxAbMqF-mFbDqSCdQeCPx_LE-tHYRtKb_0mYp1EyYJ80dLCQ2cDgSj4e7xkrSvZKraZELwpuoqlWArVkBYvsTLAKV0KwpJySNLjjKNUjm97mEXMLCZZ5Ou0wgdCMFw0OyhDnu3EHJLFO4l-bnjYHVGry84FedkaPxZGRkgHcHH5EF35LOATnDFTPV9LbOPoimhSZPpAFeldj8DBYV5fwnha1f7BkXUzQB0b_wlmt7V0ubKi_CQhq_HKUlgTFJ9IGfknsX9hlOWIz9FOI5rqohwRup-eIIdeKaYciwHg3LPAqk71ZOc_XDaqg1fEgMn8Y9FzKbGJ2WQPyYQWj3p3NPNIOB0oyWUxjv_qF4SwccnsqUpdHw_5i1fvQfz7V8JvTy0Bn_R8iLC-tAu0p5qfxjKsw0Ti8qKDpEpgnfqf-vNcrYk42ecAbOQOkpbRhNrCeLcLCaOt9g_HmOgylB86zUaDqWwObVWYfI3Azo73WNUrVUx6p3gCwMAJhosY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ab2cd42e14.mp4?token=D9QJrXbs_dq6snmuuBAgcVN0EwcLCmR2LXXMvm_qZE9OMRJQ14a-eGLARdXihHzFuuFP5Cd3pE-XnrfRkJCvA0CAoPD8zHJae0Gy4LfHFA8Ba_WBDnBHtNjwqwrhLSfNsgAhfReBjD9KO6dhotTVdCrbPsmscja1Gbg55eXVfTLPorpGHxAbMqF-mFbDqSCdQeCPx_LE-tHYRtKb_0mYp1EyYJ80dLCQ2cDgSj4e7xkrSvZKraZELwpuoqlWArVkBYvsTLAKV0KwpJySNLjjKNUjm97mEXMLCZZ5Ou0wgdCMFw0OyhDnu3EHJLFO4l-bnjYHVGry84FedkaPxZGRkgHcHH5EF35LOATnDFTPV9LbOPoimhSZPpAFeldj8DBYV5fwnha1f7BkXUzQB0b_wlmt7V0ubKi_CQhq_HKUlgTFJ9IGfknsX9hlOWIz9FOI5rqohwRup-eIIdeKaYciwHg3LPAqk71ZOc_XDaqg1fEgMn8Y9FzKbGJ2WQPyYQWj3p3NPNIOB0oyWUxjv_qF4SwccnsqUpdHw_5i1fvQfz7V8JvTy0Bn_R8iLC-tAu0p5qfxjKsw0Ti8qKDpEpgnfqf-vNcrYk42ecAbOQOkpbRhNrCeLcLCaOt9g_HmOgylB86zUaDqWwObVWYfI3Azo73WNUrVUx6p3gCwMAJhosY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ : مردم دارند جایگزینی برای تنگه هرمز پیدا می‌کنند. می‌دانید جایگزین‌ها چیست: تگزاس، آلاسکا، لوئیزیانا.
مردم برای نفت دارند به آمریکا می‌آیند.
@WarRoom</div>
<div class="tg-footer">👁️ 110K · <a href="https://t.me/withyashar/21214" target="_blank">📅 19:28 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-21213">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cce66acfb3.mp4?token=Rcb942gW5roIYmOf-erCGiw6emms0_KK_aQTgwEkUUV3kqmZRV7wEQcnWmYrfvf_Ljh3o8ubOE4RZpFYG0t8dgQEhxtZrnV-cMhOjFKpnZm5whNN6JXtP6-Q-Y5SBLcLa_2WJ3lcJVtmS3ZY1AVoFS_C9OO7u_VJjH8I-hfQsXWw2WMJFV8zIY-0GvfJhfziZEUfGewvnwOySR98fBFNp66djw3IPlyyKk7kzzzx2l4Les1HJYsddqhmJzUOSWQ6I3QMm-jjPBA0NcfRLnhC5CSmr51sMJSz-CL50JFCH-C10ONPbxsf0ulxWX6qCvbWABCJ8i2D686rD3LGKlAI6g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cce66acfb3.mp4?token=Rcb942gW5roIYmOf-erCGiw6emms0_KK_aQTgwEkUUV3kqmZRV7wEQcnWmYrfvf_Ljh3o8ubOE4RZpFYG0t8dgQEhxtZrnV-cMhOjFKpnZm5whNN6JXtP6-Q-Y5SBLcLa_2WJ3lcJVtmS3ZY1AVoFS_C9OO7u_VJjH8I-hfQsXWw2WMJFV8zIY-0GvfJhfziZEUfGewvnwOySR98fBFNp66djw3IPlyyKk7kzzzx2l4Les1HJYsddqhmJzUOSWQ6I3QMm-jjPBA0NcfRLnhC5CSmr51sMJSz-CL50JFCH-C10ONPbxsf0ulxWX6qCvbWABCJ8i2D686rD3LGKlAI6g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ: ما تنگه هرمز را کاملاً در اختیار داریم و کنترل آن را در دست داریم.
@WarRoom</div>
<div class="tg-footer">👁️ 106K · <a href="https://t.me/withyashar/21213" target="_blank">📅 19:13 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-21212">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">ترامپ در مورد ایران:
ایران نمی‌تواند سلاح هسته‌ای داشته باشد. می‌دانید چرا؟ چون از آن استفاده خواهند کرد.
ما اجازه نمی‌دهیم از آن استفاده کنند.
@WarRoom</div>
<div class="tg-footer">👁️ 105K · <a href="https://t.me/withyashar/21212" target="_blank">📅 19:11 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-21211">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/34d548b77d.mp4?token=PKIjmU2bQRIv-6pK1LBsKsu7MXSYDfe2ejxNQHeaKacJIlqOpNVh8mwDVTETb6LgggyUv2AsNJqgajgPgekwDELzmQefjU6AEw0i-dIMaz_iLbRtdrqj56wAMG5TEzOmHYJxu6GtJqNCQxTcWsLACnbnuOuNdUMESwnxOt6eiICfvtZL34-4Z-HVjZBqweapPccV-oUJI3dfZSHUn5MQfVv7s3SD7swcWHCOVssAYboB4861-VG_pmJaE7vnS3Rfmw_H1EDBgUnnDG975FjQ3beomfl7oG5J_Bax430drf_diiTby_XAN1wRYWj1PJEzKxGW75H95SDTtwzOp-g_RQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/34d548b77d.mp4?token=PKIjmU2bQRIv-6pK1LBsKsu7MXSYDfe2ejxNQHeaKacJIlqOpNVh8mwDVTETb6LgggyUv2AsNJqgajgPgekwDELzmQefjU6AEw0i-dIMaz_iLbRtdrqj56wAMG5TEzOmHYJxu6GtJqNCQxTcWsLACnbnuOuNdUMESwnxOt6eiICfvtZL34-4Z-HVjZBqweapPccV-oUJI3dfZSHUn5MQfVv7s3SD7swcWHCOVssAYboB4861-VG_pmJaE7vnS3Rfmw_H1EDBgUnnDG975FjQ3beomfl7oG5J_Bax430drf_diiTby_XAN1wRYWj1PJEzKxGW75H95SDTtwzOp-g_RQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خبرنگار: آیا شما دوباره با ایران مذاکره خواهید کرد؟
ترامپ: شاید در مقطعی، اما الان به همین حالت اوضاع خیلی خوب است.
@WarRoom</div>
<div class="tg-footer">👁️ 105K · <a href="https://t.me/withyashar/21211" target="_blank">📅 19:10 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-21210">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cc2b72a973.mp4?token=fels-pyjlQ9sVfDF9Sh4uBA581VMUfMVAxJvJMX5QJnV04dEOQsqaQw610bcDyaZZP2TbDfOvbFQVVdZuuos8yTHJjts2cvuqKNdkSsryRorfiwKbVtqL60ltSyh6wOK-z9yMk41TPXr9c-ixIdl6cYbTmm0h7tmMD8o7su_SD2VmOuSq592PvEtuKE21mMWfmLh2Ww2SHs8H9J0PwBx0PdRu7h20xW0h8rixoiTfhEp9y4waxjJTp8efQRiwlhAjQPKEG0qscGlA-K5TTmx8OSMIvj-rrlGlxi_h6AJBbMd2K_xaAqj4Qu879zPK_LDuQsH_4BnYeL6ZfxnnRP-Og" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cc2b72a973.mp4?token=fels-pyjlQ9sVfDF9Sh4uBA581VMUfMVAxJvJMX5QJnV04dEOQsqaQw610bcDyaZZP2TbDfOvbFQVVdZuuos8yTHJjts2cvuqKNdkSsryRorfiwKbVtqL60ltSyh6wOK-z9yMk41TPXr9c-ixIdl6cYbTmm0h7tmMD8o7su_SD2VmOuSq592PvEtuKE21mMWfmLh2Ww2SHs8H9J0PwBx0PdRu7h20xW0h8rixoiTfhEp9y4waxjJTp8efQRiwlhAjQPKEG0qscGlA-K5TTmx8OSMIvj-rrlGlxi_h6AJBbMd2K_xaAqj4Qu879zPK_LDuQsH_4BnYeL6ZfxnnRP-Og" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ درباره تنگه هرمز:
قرار نیست کارمان بی‌نقص باشد، اما نفت زیادی از آن خارج می‌شود، خیلی زیاد.
مردم شگفت‌زده هستند.
@WarRoom</div>
<div class="tg-footer">👁️ 109K · <a href="https://t.me/withyashar/21210" target="_blank">📅 19:09 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-21209">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ca74a36348.mp4?token=oApoYSR3jsVa-M8hLHPJH7kdylhilKZiEC2xyvozMpmtxw4q_bDiZ6G75Q_uXijD-ncHGtJ7uWMV9qY7m4IRIdyvn0bMwtpq6mfm5iuGNHjNRCa7C9UMd0QXeRT4TFXF0C1Gb2NduUiklt-HqnNjNulO7dChNzX2vWqpSmtYtVq5YBiHpcfiGNoy7FzLva3KD2TSRaAMv2qoagP3JelHw5JR4IMoa7dGYk_q-A6oX6pW3PZQTBSjf378_GJpcFxxPPlfIzcbyba0jlxNXon8pY0ciP_qxuU1yWsy30i480cwxNqQ6CEuIvGF4eOtcn1f-GQj7FEv5Plw8Zhtz-6lDDzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ca74a36348.mp4?token=oApoYSR3jsVa-M8hLHPJH7kdylhilKZiEC2xyvozMpmtxw4q_bDiZ6G75Q_uXijD-ncHGtJ7uWMV9qY7m4IRIdyvn0bMwtpq6mfm5iuGNHjNRCa7C9UMd0QXeRT4TFXF0C1Gb2NduUiklt-HqnNjNulO7dChNzX2vWqpSmtYtVq5YBiHpcfiGNoy7FzLva3KD2TSRaAMv2qoagP3JelHw5JR4IMoa7dGYk_q-A6oX6pW3PZQTBSjf378_GJpcFxxPPlfIzcbyba0jlxNXon8pY0ciP_qxuU1yWsy30i480cwxNqQ6CEuIvGF4eOtcn1f-GQj7FEv5Plw8Zhtz-6lDDzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ در مورد کیم جونگ اون:
این واقعیت که من با کیم جونگ اون خوب کنار می‌آیم چیز خوبی است.او ۵۷ سلاح هسته‌ای بسیار قدرتمند دارد. هرگز نباید اجازه می‌داد این اتفاق بیفتد، اما او آنها را دارد.من با او خیلی خوب کنار می‌آییم. من کیم جونگ اون را خیلی خوب می‌شناسم. او خوب خواهد بود.تا زمانی که یک رئیس جمهور باهوش داشته باشیم، او خوب خواهد بود. اگر یک رئیس جمهور احمق داشته باشیم، احتمالاً او خوب نخواهد بود.
@WarRoom</div>
<div class="tg-footer">👁️ 111K · <a href="https://t.me/withyashar/21209" target="_blank">📅 19:04 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-21208">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">پولیتیکو : ایران و آمریکا وارد فاز صبر و انتظار شده‌اند؛ هر یک منتظرند تاب‌آوری دیگری زودتر تمام شود
@WarRoom</div>
<div class="tg-footer">👁️ 112K · <a href="https://t.me/withyashar/21208" target="_blank">📅 17:20 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-21207">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tIjS6vezFUJzeL6ncKpSsUP4PvDIAQ4f7qMgJ-BVlWyIk6JTjALnHJxU2CQ5LgXkPpLf9a_6njq6v06peIPBgQzVyC70SZ6F4GBCgeHsct0GmWPRTOMPBKLU0Kn1D6M24Q3TBbBbn5QADGWt1JYaoiTdD9Ifa7rkbA87-0Ckjze_b1zes2Z_3e0yG9CtqXco9EEGxJXUkFrTh0coJNfX_mtp6lvkU9XJrSL7m-51-rG1QXnKEi5285VmDA7c_rTSVVu0bEeZhgCTCaaObJq6y-F_DmQocMJVfOaKPIPHW8qccIiJSTODCGSOhomxl3aDULzm7qBhUO-RKKoGK4xo7w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سنتکام: یک فروند جنگ الکترونیک EA-18G Growler نیروی دریایی آمریکا، هنگام انجام گشت‌زنی بر فراز خاورمیانه، از یک فروند KC-135 Stratotanker نیروی هوایی آمریکا سوخت‌گیری می‌کند
@WarRoom</div>
<div class="tg-footer">👁️ 117K · <a href="https://t.me/withyashar/21207" target="_blank">📅 16:00 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-21206">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">مرندی مشاور تیم مذاکره کننده : دیروز، کاخ سفید گفت که مذاکراتِ وجود نداشته با ایران را «به حالت تعلیق درآورده» است؛ ظاهراً با این هدف که فشار اقتصادی را افزایش دهد. اما چیزی که کاخ سفید نمی‌گوید این است که آن‌ها تا همین امروز همچنان در حال ارسال پیام به تهران هستند.
@WarRoom</div>
<div class="tg-footer">👁️ 117K · <a href="https://t.me/withyashar/21206" target="_blank">📅 14:47 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-21205">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">یک مقام ناتو در واکنش به گزارش‌ها درباره احتمال تهدید اهداف آمریکایی در اروپا از سوی ایران گفت:
ناتو آماده مقابله با هرگونه تهدید علیه کشورهای عضو است و برای دفاع از همه متحدان خود هر اقدام لازم را انجام خواهد داد.
این مقام تأکید کرد که وضعیت بازدارندگی و دفاعی ناتو «قوی و مؤثر» است و یادآوری کرد که سامانه‌های پدافند هوایی ناتو پیش‌تر نیز موشک‌های بالستیک شلیک‌شده از ایران به سمت ترکیه را در چهار مورد رهگیری کرده‌اند.
@WarRoom</div>
<div class="tg-footer">👁️ 118K · <a href="https://t.me/withyashar/21205" target="_blank">📅 14:41 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-21204">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">ناو هواپیمابر یواس‌اس جورج واشنگتن به عنوان بخشی از عملیات خود در منطقه عملیاتی ناوگان هفتم ایالات متحده، از تنگه سنگاپور و تنگه مالاکا عبور می‌کند.
@WarRoom</div>
<div class="tg-footer">👁️ 120K · <a href="https://t.me/withyashar/21204" target="_blank">📅 14:19 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-21203">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">وال استریت ژورنال: مقام‌های عرب می‌گویند ما «بین ایران و آمریکا گیر افتاده‌ایم»
آن‌ها معتقدند جمهوری اسلامی در نهایت به افزایش فشار اقتصادی، واکنش نظامی نشان خواهد داد، در نتیجه، جنگ دوباره می‌تواند شدت بگیرد
حملات اخیر جمهوری اسلامی در تنگه هرمز، روشی را که برای حفظ صادرات و تولید نفت به کار گرفته شده ، تهدید می‌کند , در این روش که «سفرهای شاتل» نامیده می‌شود، نفت خام و فرآورده‌های نفتی از داخل خلیج فارس به کشتی‌هایی منتقل می‌شوند که در خارج از منطقه منتظر هستند تا محموله را به بازارهای جهانی منتقل کنند
@WarRoom</div>
<div class="tg-footer">👁️ 119K · <a href="https://t.me/withyashar/21203" target="_blank">📅 14:12 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-21202">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">ارتش اسرائیل : ما در چارچوب خنثی کردن شبکه تونل‌های سازمان‌های تروریستی، دو تونل زیرزمینی حماس در شرق خط زرد در نوار غزه را مسدود کردیم که در مجموع بیش از دو کیلومتر طول داشتند.
@WarRoom</div>
<div class="tg-footer">👁️ 120K · <a href="https://t.me/withyashar/21202" target="_blank">📅 12:57 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-21201">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7d47b2eca4.mp4?token=Qxj9Ju0wI19QC19yB78YhUHERbSTEWDtrkNIgjcprOY0U7NBj1BDMoB8rt-KheT8LPVvGAXyWow_lcNwON-Hh9GqCTs0PtpmHsi_LEzeVqPRKjSeDbN1I0mWi4jnC7n3w3yXQ9LmGWFhfnC7PHPh-twTm-dNvD0J_mQVGj-Ogt8VH7SiauYev8qpdRQ3pVRTDkxvW5qylbXO4pc-3XdFK0LR_UoAig3LFj7mf8rnD7lKy21I1ZM78U2XJh8OSsr10A3m6OXZVqmqVVRRq0dW3G4ajo3jvf72ji-wj-G_Ei-OOl6YFcET_Ic5EPMx46riJoZ0kSXu7QC0Cz-0yREFZYi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7d47b2eca4.mp4?token=Qxj9Ju0wI19QC19yB78YhUHERbSTEWDtrkNIgjcprOY0U7NBj1BDMoB8rt-KheT8LPVvGAXyWow_lcNwON-Hh9GqCTs0PtpmHsi_LEzeVqPRKjSeDbN1I0mWi4jnC7n3w3yXQ9LmGWFhfnC7PHPh-twTm-dNvD0J_mQVGj-Ogt8VH7SiauYev8qpdRQ3pVRTDkxvW5qylbXO4pc-3XdFK0LR_UoAig3LFj7mf8rnD7lKy21I1ZM78U2XJh8OSsr10A3m6OXZVqmqVVRRq0dW3G4ajo3jvf72ji-wj-G_Ei-OOl6YFcET_Ic5EPMx46riJoZ0kSXu7QC0Cz-0yREFZYi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ممباقر در عراق…
@WarRoom</div>
<div class="tg-footer">👁️ 121K · <a href="https://t.me/withyashar/21201" target="_blank">📅 11:48 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-21200">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">سی‌ان‌ان: ایران بخش قابل‌توجهی از کنترل خود بر تنگه هرمز را از دست داده است.
بر اساس داده‌های شرکت کپلر، در دو هفته گذشته
بیش از ۸۰ درصد کشتی‌های عبوری از مسیر تحت نظارت عمان
در بخش جنوبی تنگه عبور کرده‌اند؛ مسیری که ایران با آن مخالف است. برخی کشتی‌ها نیز با وجود تهدیدهای ایران، با اتکا به حضور نیروی دریایی آمریکا از این مسیر عبور کرده‌اند. یک تحلیلگر کپلر گفته است که به نظر می‌رسد ایران
دست‌کم بخشی از کنترل تنگه را از دست داده است
؛ هرچند ایران همچنان با تهدید حمله و ایجاد بازدارندگی، توان تأثیرگذاری بر رفت‌وآمد دریایی را حفظ کرده است.
@WarRoom</div>
<div class="tg-footer">👁️ 116K · <a href="https://t.me/withyashar/21200" target="_blank">📅 11:07 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-21199">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">الجزیره : این ترامپ نیست که مانع عبور کشتی‌ها از تنگه هرمز می‌شود، بلکه شرکت‌های بیمه این کار را می کنند
تا زمانی که تهدید فیزیکی علیه تردد دریایی وجود داشته باشد، این شرکت‌ها از قدرت مالی خود برای جلوگیری از عبور کشتی‌ها استفاده خواهند کرد
بدون تضمین‌های قاطع مبنی بر اینکه کشتی‌ها از حملات ایران در امان خواهند بود، مالکان حاضر نمی‌شوند که در تنگه تردد کنند
@WarRoom</div>
<div class="tg-footer">👁️ 118K · <a href="https://t.me/withyashar/21199" target="_blank">📅 11:02 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-21198">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">اورشلیم پست: تام باراک، نماینده ویژه آمریکا، هشدار داد که حمله اسرائیل به پایگاه هوایی ابو الظهور در نزدیکی ادلب در سوریه، می‌توانست منجر به تشدید تنش‌ها و یک رویارویی نظامی مستقیم، احتمالاً با ترکیه، شود.
@WarRoom</div>
<div class="tg-footer">👁️ 118K · <a href="https://t.me/withyashar/21198" target="_blank">📅 10:56 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-21197">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">رویترز : آمریکا برای
بازسازی ذخایر تسلیحاتی و افزایش توان تولید مهمات
، بودجه‌ای بیش از یک تریلیون دلار پیشنهاد کرده است. پنتاگون قراردادهای تسلیحاتی را از پنج‌ساله به
هفت‌ساله
افزایش می‌دهد تا شرکت‌های دفاعی با اطمینان بیشتری کارخانه‌ها و ظرفیت تولید خود را گسترش دهند. هدف، افزایش شدید تولید
موشک‌های رهگیر پاتریوت و THAAD
و جبران ذخایری است که در جنگ ایران و دیگر درگیری‌ها کاهش یافته‌اند. همزمان، آمریکا تولید موشک‌های کروز را نیز افزایش می‌دهد؛ از جمله قرارداد
۲۲.۹ میلیارد دلاری هفت‌ساله با ریتیان برای افزایش تولید تام‌هاوک از حدود ۶۰ فروند به بیش از هزار فروند در سال
.
@WarRoom</div>
<div class="tg-footer">👁️ 117K · <a href="https://t.me/withyashar/21197" target="_blank">📅 10:45 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-21196">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">فایننشال تایمز: ایران در صورت تشدید جنگ از سوی ترامپ، حمله به اهداف نظامی آمریکا در اروپا را بررسی می‌کند.
به گفته دو منبع نزدیک به حکومت ایران، نیروهای ایرانی گزینه حمله به دارایی‌های نظامی آمریکا در
بلغارستان و قبرس
را بررسی کرده‌اند. همچنین حمله به
کابل‌های فیبر نوری زیردریایی در تنگه هرمز
نیز از گزینه‌های مورد بررسی است. این منابع هشدار داده‌اند که در صورت حمله آمریکا به زیرساخت‌های ایران، تهران ممکن است دامنه درگیری را فراتر از خاورمیانه گسترش دهد.
@WarRoom</div>
<div class="tg-footer">👁️ 119K · <a href="https://t.me/withyashar/21196" target="_blank">📅 10:39 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-21195">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TaholLRlji45H6NE53p14vdw_dC9EQyhbtLNwLv98ktf03zkWVe80DwLuEJylMPP4-JzFdW_vta5p4SJ76OUvbtuZXmsP_w9JGk51WRWar9UZ2zQM4OWJoiedF5x6OMXlUaeR4F3JLGrcLvOALAt1PsMeM8snRqdZ-8vKozdxDNGTHHCoCYZ33b8J7rkEJqu7smDQbXIXYegyt8Z5DJlDHbAdQJWVMwTGgJ0lKno2Ys7XvT6WkWISRsJRmLoFgogE01ISB0Irdi1hSW3u2nbaSfwgW3eri3Kmp5XDR_r_c-SO_bHn3MJnfzFmKfZqVqEGi4Z28vw0d3nOeAHt6xkrg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تا سقف ۱۰ میلیون دلار پاداش برای اطلاعات درباره هکرهای ایرانی
بهزاد مصری , کیوان فیاض ، مجتبی غاله‌کوهی ، آرمان کهزادیان ، صابر شهبازی
@WarRoom</div>
<div class="tg-footer">👁️ 124K · <a href="https://t.me/withyashar/21195" target="_blank">📅 10:31 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-21194">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">یک مقام ارشد وزارت خارجه آمریکا می‌گوید:
«اهرم‌های متعددی وجود دارد که رئیس‌جمهور می‌تواند در هفته‌ها و ماه‌های آینده، در صورت انتخاب این مسیر از سوی ایران، فشار آن‌ها را افزایش دهد.»
@WarRoom</div>
<div class="tg-footer">👁️ 122K · <a href="https://t.me/withyashar/21194" target="_blank">📅 10:25 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-21193">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-footer">👁️ 131K · <a href="https://t.me/withyashar/21193" target="_blank">📅 03:13 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-21192">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-footer">👁️ 135K · <a href="https://t.me/withyashar/21192" target="_blank">📅 02:39 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-21191">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-footer">👁️ 136K · <a href="https://t.me/withyashar/21191" target="_blank">📅 02:26 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-21190">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-footer">👁️ 136K · <a href="https://t.me/withyashar/21190" target="_blank">📅 02:12 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-21189">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-footer">👁️ 138K · <a href="https://t.me/withyashar/21189" target="_blank">📅 01:18 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-21188">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-footer">👁️ 139K · <a href="https://t.me/withyashar/21188" target="_blank">📅 01:10 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-21187">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">الجزیره : ترامپ به تیم خود دستور داده تا زمانی که ایران آماده امضای توافق نیست، با این کشور دیگر مذاکره نکنند @WarRoom</div>
<div class="tg-footer">👁️ 140K · <a href="https://t.me/withyashar/21187" target="_blank">📅 00:46 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-21186">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">اینترنت</div>
<div class="tg-footer">👁️ 137K · <a href="https://t.me/withyashar/21186" target="_blank">📅 00:38 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-21185">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">خبرنگار شبکه ۱۲ اسرائیل:
نتانیاهو با یک رویکرد برنامه‌ریزی‌شده، در حال آماده‌سازی جنگ آینده علیه ترکیه است.
@WarRoom</div>
<div class="tg-footer">👁️ 139K · <a href="https://t.me/withyashar/21185" target="_blank">📅 00:09 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-21184">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">ترامپ در فاکس‌نیوز هشدار داد که اگر عمان مانع منافع آمریکا شود، این کشور را بمباران خواهد کرد @WarRoom</div>
<div class="tg-footer">👁️ 138K · <a href="https://t.me/withyashar/21184" target="_blank">📅 00:02 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-21183">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">خبرنگار اکسیوس: «مقام ارشد اسرائیلی ادعا می‌کند که حمله به پایگاه نیروی هوایی سوریه در منطقه ادلب با هدف جلوگیری از استقرار نظامی ترکیه در آنجا انجام شده است.» مقام ارشد ترکیه پاسخ می‌دهد: «هیچ حضور ترکیه‌ای در پایگاه هوایی وجود نداشت. اسرائیل در حال بهانه‌تراشی…</div>
<div class="tg-footer">👁️ 136K · <a href="https://t.me/withyashar/21183" target="_blank">📅 23:59 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-21182">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">خبرگزاری الخلیج ،وزارت خارجه امارات :
در پی تشدید تنش‌های منطقه‌ای، تمامی فعالیت‌های تجاری، مبادلات تجاری و معاملات مالی با ایران تا اطلاع ثانوی متوقف شد.
@WarRoom</div>
<div class="tg-footer">👁️ 135K · <a href="https://t.me/withyashar/21182" target="_blank">📅 23:55 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-21181">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">❤️‍🩹</div>
<div class="tg-footer">👁️ 131K · <a href="https://t.me/withyashar/21181" target="_blank">📅 23:43 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-21180">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">سیریک موشک بلند شد
🚨
🚨
🚨
@WarRoom</div>
<div class="tg-footer">👁️ 131K · <a href="https://t.me/withyashar/21180" target="_blank">📅 23:33 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-21179">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">اتاق جنگ با یاشار : گزارشهای مردمی از وضعیت ایران بهم نشان میده که فقط یک جرقه لازمه تا این انبار باروت رو منفجر کنه
@WarRoom</div>
<div class="tg-footer">👁️ 132K · <a href="https://t.me/withyashar/21179" target="_blank">📅 23:14 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-21177">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/r0vk3uuCkbZtToMHVKyoGO8vSChW9AX31UQYIEYjflJNpVew_N0dW6TyJH79JkmIxjAA6YTjDoYt06pJWoaNsyX2zOwOS81Fb6X8wshpSZ1H7fp0roS0sbnKXDYkNravBcSmo8DyLTupt0Ck26yCRXAijcuIxU84nwpwaZ1dGSqLWqbszg6_6MaYLbJLmJYvV6YJU2ksmJ_5VtvCKDNK4Ux2gd6AO9tjyIgrovm1bz_Fs7OgJLY8HlzuTGpr5EW7lSv_nNhqeO6pzGt659vJfZHTLvQAGYEP6JlEXthdpL0FbZEyxsbA--VjQYT38Lm45-bNfzYAPoZx_KlE8my_3A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/cyOiPGFwrXxB3a8KBlpEDFcaWTp-sHKCNnrke3aoZEvw5KN2SQMbw04SMGiCjtaWVQBZO3vfT1-CZyfTept51nOWxVjEOqqZzFd0EQDxbX2qhdbsY0Hef6pGbm7N_l0jUe0MLmOEYjp8gGfmSwlaxQJO_bcvYsNpW4y_8bYWhvL2JKfI3IYe19HcET8qJzMlkVlCbCs0QOFtuIqXqcvtmmArvuetl2aCtB_B9qdyafqJGTIvA94ukuyIjkqvBFCiKe5EdrsbXfSUDQDwL1J0dxtlxdESAFLRlHglIxNMndVXQSI8YFZzBhWDws-uaDpmaLFayH8Mse4zE7LdeB9PUQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">برنامه کوروش بزرگ ۲ روز سالگرد مهسا امینی ، که شاهزاده در تورنتو صحبت میکنه و لیست قیمت های بلیت این برنامه
@WarRoom</div>
<div class="tg-footer">👁️ 136K · <a href="https://t.me/withyashar/21177" target="_blank">📅 23:09 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-21176">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">سفیر جمهوری اسلامی در کویت امروز با ۴ نیرو سپاه پاسداران که از چند ماه قبل در این کشور بازداشت شده‌اند، دیدار کرد.
@WarRoom</div>
<div class="tg-footer">👁️ 130K · <a href="https://t.me/withyashar/21176" target="_blank">📅 22:54 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-21175">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">اورشلیم پست : پنتاگون از  ۳۰ دانشگاه خواسته بررسی کنند که با نهادهای علمی چین، روسیه و ایران چه نوع همکاری‌هایی دارند و آیا از طریق این همکاری‌ها ممکن است اطلاعات حساس پژوهشی آمریکا به خارج منتقل شود یا نه ،
یک مقام آمریکایی گفت دانشگاه‌های هاروارد، ام‌آی‌تی و دانشگاه برکلی کالیفرنیا هم جزو این ۳۰ دانشگاه هستند
@WarRoom</div>
<div class="tg-footer">👁️ 134K · <a href="https://t.me/withyashar/21175" target="_blank">📅 22:20 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-21173">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/UrQJZRBOb5_HN9k4dJiyee0ZT1lSZ8xC3_8KyQT4djXMg4qoDAVjdthIhm3FjcGS5SPTIB4B7RZIn_PJAFCJBi4k7_BKi69RP9JnzsW2QEARSnWv5aMMn3RaaPlg1a20Vv05v9vRCdkMAYY8ZIndT56s-rLjr8NOh4pjmvNBr2s-e-SsxmAbsCpXgqwyy70jPTVJpVv_dFUmVHJHAw4wPpT1E6UHpcphp0OQZd0UW01G_wQnhAxbScQDYphhECEbJZnZT0hIpQCXnKDnZjSzkOLROLLcKPi_qzgz1yWi-GsCtvhkY4txXozthjBpay_zorPg0IrvAtqfPnuJns304w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/d3mGhPuKNCFZbZCxIM7jN54U5FHWzDNtoaGEh2nJe4S_cO91j3Li_KraWYyYyiwupFVEpj4vpG0wnm-NUMCdTvtbnrBLjs811mwX5Q3LcRkQDohnSSbCKUqzkx1joUP3g63WqZ5eSQfpH1aAE8aEslq2eycmqGowZQfxzC-KRvZZi62wUjl-r8w8srgOwa4d1tkCaU_FBigA1Ydfqc8SpXykgNUdKypEEivDwpWUfbUnYE-9pFemlMUyUTvwmJy33j0bq1MpeVsl82MGtAqCpSFznO71nTB4UV-1HFQiL-3rMUkmEqe7Xhp7gwK4SMAFiSPzXBpoS-QZSCgx-PDoKA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">تصاویر ماهواره‌ای دیروز حداقل ۲۲ هواپیمای سوخت‌رسانی آمریکایی را در فرودگاه رامون و تقریباً ۱۹ هواپیمای دیگر را در پایگاه هوایی عوودا در جنوب اسرائیل نشان می‌دهد
علاوه بر این، حدود ۲۰ هواپیمای سوخت‌رسانی دیگر در فرودگاه بن گوریون وجود دارد که تعداد کل هواپیماهای مستقر در اسرائیل را به تقریباً ۶۰ فروند می‌رساند.
@WarRoom</div>
<div class="tg-footer">👁️ 134K · <a href="https://t.me/withyashar/21173" target="_blank">📅 20:52 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-21172">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">روبرتو کارلوس : مسلمان شدم.
@WarRoom</div>
<div class="tg-footer">👁️ 133K · <a href="https://t.me/withyashar/21172" target="_blank">📅 20:14 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-21171">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">وزارت دفاع امارات : دو موشک بالستیک را که از سمت ایران در حال حرکت بودند، شناسایی و دفع کردیم. @WarRoom</div>
<div class="tg-footer">👁️ 130K · <a href="https://t.me/withyashar/21171" target="_blank">📅 20:11 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-21170">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">وزارت دفاع امارات : دو موشک بالستیک را که از سمت ایران در حال حرکت بودند، شناسایی و دفع کردیم.
@WarRoom</div>
<div class="tg-footer">👁️ 129K · <a href="https://t.me/withyashar/21170" target="_blank">📅 20:09 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-21169">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/H5F93Vlh3Z1sFkkU9KEAaIgg3d18W7afcRGG-SZucB4-QutuyLiWtLOROu4YWyA-R1hOlnfIC4HqWH8fGc4fyAdNf4y5gWMPjyClCLKx5nQeohBSelbP3xL_ftKdtAoJRGWh_2xdLowwjy-0H1VJZVHuJp4RdYpZtm_Gw0_Vr1hhnz-KM4k51_W6MKT8q1ejCm2nbh02Q0r-tZ2_1BKVoY55sU4yk5lX7lonCzID3pZzVMLJ-f-XwxHjEDNwzXmOg_EfhkCorAnXW9S6myixzCws9pTRoLgjMSt0xEDVbVOkCHvggzF7XHP9zZGaekNrmsrfEpYOwFNb0HfjYNc60A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏UKMTO با تأخیر گزارشی از حادثه‌ای در تنگه هرمز دریافت کرده است.
یک شخص ثالث گزارش داده است که یک کشتی فله‌بر هنگام عبور از تنگه هرمز مورد اصابت یک پرتابه ناشناخته قرار گرفته است. این برخورد باعث آسیب به سمت راست کشتی و تلفات خدمه شده است.
@WarRoom</div>
<div class="tg-footer">👁️ 128K · <a href="https://t.me/withyashar/21169" target="_blank">📅 20:05 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-21168">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">خبرنگار اکسیوس: «مقام ارشد اسرائیلی ادعا می‌کند که حمله به پایگاه نیروی هوایی سوریه در منطقه ادلب با هدف جلوگیری از استقرار نظامی ترکیه در آنجا انجام شده است.» مقام ارشد ترکیه پاسخ می‌دهد: «هیچ حضور ترکیه‌ای در پایگاه هوایی وجود نداشت. اسرائیل در حال بهانه‌تراشی برای بمباران کشورهای همسایه و تضعیف ثبات در منطقه است.»
@WarRoom</div>
<div class="tg-footer">👁️ 123K · <a href="https://t.me/withyashar/21168" target="_blank">📅 19:58 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-21167">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cz857Va67wJLOY1gqHN-Qkv_HDBnEhojN1QyD7kd8HvD_CmcFIizge5aZWrxvV3JcO4QtQHx9FXquuTuSVBT9AjPRtncsY0-OmWWMUjshGzJElLpepqQNNdit2G0kwz_rQliBznGkFn8GNCreJvC5gMYPdEkIRDueY_8tj6AsWgcp2oCq1c61UtlGbiL6cFJX10h7USycPQCfFZMn7sYX2eqnSyv8irunKmocHefnWBYJrOsT2r5LMnn_9ATFJldPrZNCfvffFW8l5WI0ZwbnBYH3T5tpfzaQoPOvksALj9dCqLLFyDuCN7_iZtCGfBQb5vl2_cKYP8ZpJdqQLJWsw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزارت جنگ آمریکا با انتشار این عکس از ترامپ نوشت : ما پیروز خواهیم شد
@WarRoom</div>
<div class="tg-footer">👁️ 129K · <a href="https://t.me/withyashar/21167" target="_blank">📅 19:54 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-21166">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">خبرگزاری رژیم تسنیم مدعی شد که
پرتابه‌های شلیک‌شده به سمت امارات از یمن شلیک شده‌اند.
این ادعا تاکنون
به‌طور رسمی تأیید نشده
و منابع مستقل نیز هنوز آن را تأیید یا رد نکرده‌اند.
@WarRoom</div>
<div class="tg-footer">👁️ 127K · <a href="https://t.me/withyashar/21166" target="_blank">📅 19:15 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-21165">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">الجزیره : ترامپ به تیم خود دستور داده تا زمانی که ایران آماده امضای توافق نیست، با این کشور دیگر مذاکره نکنند
@WarRoom</div>
<div class="tg-footer">👁️ 128K · <a href="https://t.me/withyashar/21165" target="_blank">📅 19:04 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-21164">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">آلارم حمله موشکی در‌امارات ممکنه باز اشتباه اومده باشه @WarRoom
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 131K · <a href="https://t.me/withyashar/21164" target="_blank">📅 18:33 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-21163">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">آلارم حمله موشکی در‌امارات
ممکنه باز اشتباه اومده باشه
@WarRoom
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 136K · <a href="https://t.me/withyashar/21163" target="_blank">📅 18:24 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-21162">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/g6skVPTXmP8sBwSB2zCdcE5aG951rX3bnTd4tmnFQ57bLS9EPY5RskuY48PBZN9FSTe2ZNCdwRyimKDvVFcud5QgIZKsSh6phcanDWXmLnnsFEYCoOlgnDIabwVMo_USUZhgfVvSpTSxaP1MmzZ46uB__tQJcdfhbBoJ03905inmffujuaxh-tWy6R_nbPKQNYKQqwy8fzG12YoXsleMSsOhaELGFYrZV8p7H7ZWqHRrC67uuQE0Xoz14_47pAm6i_hVrMXL0X-p6lxcII_IoWoRC8wkS4jzvLAcY-9bhj01jM20_wp3X3csl_TWrpOodILdQDQ6jGxQEq09BsC1JA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ در تروث : هیچ مذاکره یا گفتگویی با جمهوری اسلامی ایران در حال انجام یا برنامه‌ریزی نشده است. محاصره دریایی به قوت خود باقی است. تنگه هرمز باز و فعال است. تمام مین‌های آبی برداشته یا منفجر شده‌اند. از توجه شما به این موضوع متشکرم!
@WarRoom</div>
<div class="tg-footer">👁️ 139K · <a href="https://t.me/withyashar/21162" target="_blank">📅 17:10 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-21161">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jrD_8RpzBKEQLI-3UZqdC8w8dDr5ABeX_xPZvEqSvasZ5xbMx63Ee3qrajwzng3TIqsvCtLmGeJuuXi9CZWMS3ynjbCxD-9svgTRWrWy-37UT3iwt83jVVGzQYBW42mW1W7vnu7wUnPUL1S3Xdc7mEtSMF3RvE2N14ZF0AA7UUR86aD4JEiZ9UKX1kmIOxBA0c0NNPUH8SuMonuGwn06oWXUjAHAbGvq4278B6Uhuvp1FjNYUn4oW-iIeoVqNwS7DrCTqyPClGJtgMJFV3pqDOWgnKTtMlu-Qb88yfihB6FTFZYKyDcs38_1MS5Gef5rqFx4dhXlv5v81RIg2YGItQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ در تروث و سیگنال حمایت از تغییر رژیم در ایران : لیندسی همین چند هفته پیش داشت خوش می‌گذراند! کلاهش را ببین!
@WarRoom
🚨
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 134K · <a href="https://t.me/withyashar/21161" target="_blank">📅 16:49 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-21160">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VZKyz59pEqEuUnWA279L9lBj5tOaZFKcXPDJMz6v_vI_d-NLZh4Yk-B4R-A4y4kgTchi51pY2YB3KC6uD4K_oqX3pobMOA0_lgNE9BOr1lu6QU_YibJS_4vfU4JwsTAyL2pdvQGqGo-5f3dumCFGvuZti9ILJHNIqYzvH7mq_9y1DorwTnqhY9QEa32ZRwCn2GIaQS2hb96KGnvtuAhHF5kdJn4fFtX1hIYsDaZ1bT9qlTJuJiv2BqJIYiaxPsBNjXp9Zo7tvcf1SZRRUfBysFiZW9hCJYZ_CNZIpFHKK1SeuZhPMiPsmqOtgxFcGMhVszFzjKFiXyoYJpMoc1mVXw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هواپیمای مخوف جنگ الکترونیک EA-37B کامپاس کال ، در حال کم کردن ارتفاع برای فرود در پایگاه آمریکا در جزیره خانیا یونان میباشد ، از این هوا پیما فقط ۵ دستگاه تا کنون تولید شده
@WarRoom
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 124K · <a href="https://t.me/withyashar/21160" target="_blank">📅 16:21 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-21159">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/77ba9d3c18.mp4?token=HaDROTkAQ5a1JC0X3ISUZNeE6GlHCkr0ybrz4-ivuVJiELltd5m1nDUFk3pQFfzPWVtN743M3CvnfZRkeRcaU6Lr1s10gK3pcTh_SyPVYjUwDYL6dsgN69hmsRqKDVC3Ql475Q35_LK7PiFEPCR6_utDhQoLm0Ye0GS2EIMY3CsL15V8PgtMvsUIntJMiLunK1khXHkJAdPaXnLl9UWYjoHiWR1QvDoK2IDmZ1CQMmad2DWw8OGQFYdbKi_knLqy3mp5_K36YNgFZr9diP0FJy62gGjs7XBwhtp8ALJCz-yBvcFGDHUvpGrYPG_CZZvi0VgPtHw3V1500aEyNVF1WA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/77ba9d3c18.mp4?token=HaDROTkAQ5a1JC0X3ISUZNeE6GlHCkr0ybrz4-ivuVJiELltd5m1nDUFk3pQFfzPWVtN743M3CvnfZRkeRcaU6Lr1s10gK3pcTh_SyPVYjUwDYL6dsgN69hmsRqKDVC3Ql475Q35_LK7PiFEPCR6_utDhQoLm0Ye0GS2EIMY3CsL15V8PgtMvsUIntJMiLunK1khXHkJAdPaXnLl9UWYjoHiWR1QvDoK2IDmZ1CQMmad2DWw8OGQFYdbKi_knLqy3mp5_K36YNgFZr9diP0FJy62gGjs7XBwhtp8ALJCz-yBvcFGDHUvpGrYPG_CZZvi0VgPtHw3V1500aEyNVF1WA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دارلین گراهام در مورد اسرائیل:
من با نتانیاهو و همسرش ملاقات کرده ام. آنها برای تشییع جنازه لیندزی در شهر بودند.
من یک چیز را به او اطمینان دادم که در کنار اسرائیل نیز خواهم بود
@WarRoom</div>
<div class="tg-footer">👁️ 122K · <a href="https://t.me/withyashar/21159" target="_blank">📅 15:32 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-21158">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RAFmPvqVulaziw9f2shML-3LFtvR6UGURFaTI5SQhv6D1GwvGPQNWggCF5GXMJ1AwYYKLUe8oHfe-YNBqil4FfJOephdL3SBIxGnOb2iK5dFsU7lTFxXwvM-NUhDGUiFhRVjGEQLUs2y96dqWkQPUZimEV2mGbgp8qlwwL7v99zno8O_Q6jQUJKgi2cgxNltYEoXmOwZ_oZUdhFDeY17jsF5sQJLnaya2qT7nFXOc04AI9pyPS0p4QETAso65fDw8yr8KInknEhGh9hpTwCFBun9a_f7i2zs5i3tHBD1e7kibRbmZH-2MthmdLvI_LvH-f8cyzuV3ioVO5PdEaha4A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ :
منطقه جدید متعلق به آمریکا, تنگه هرمز
@WarRoom</div>
<div class="tg-footer">👁️ 123K · <a href="https://t.me/withyashar/21158" target="_blank">📅 15:04 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-21157">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">سخنگوی وزارت امور خارجه قطر: ما نمی‌دانیم چه انگیزه‌ای باعث شده است که ايران پس از گذشت 6 ماه، موضوع خلبان‌ها را مطرح کند.
@WarRoom</div>
<div class="tg-footer">👁️ 121K · <a href="https://t.me/withyashar/21157" target="_blank">📅 14:38 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-21156">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">رئیس اتاق مشترک ایران و عراق :
ایران حدود ۱۲ میلیارد دلار از عراق طلبکار است
@WarRoom</div>
<div class="tg-footer">👁️ 123K · <a href="https://t.me/withyashar/21156" target="_blank">📅 14:36 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-21155">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-footer">👁️ 126K · <a href="https://t.me/withyashar/21155" target="_blank">📅 14:03 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-21153">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LMagUlUpBrbBff0PkYzXSjQmcqwTNRpK_jXoYQ1XY0n-2gImGbnVri_sC9cJV4xpvvOqybjKjzgAq0yujx7r3RzwDhcW-FPv7q1487jBz7TZI-X1FitGpT7hWWB-mIALh61TWzs8D2wofc0cjMV8adU9_Urm2j9f-PzlH-mYh5itP9sD_57p7D9wzXJ_qFMU3a2-SA5KIycWxTVIFSmN6eFb1rIFM2BRMp1TGrg2VSvuWjeYYrzWPthbmK_i3WDAGSqc7lOc6JKna7OIbwMtya48apzfqKuX3gCMfVZo0xgLUAyvd6JED5NsiJbzxdzmSCinCsKyBQbWJdBcsSUmkw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/TQ-0or16P9MY9BuqsgFyu6XdN4wKa1pTyXTvR9LeNv20dBOwVqQuF6wcN6V2D56z8rHGcOiCOHtq7AbhSRC7_QM5P4JHsNa8cs9jdLxx--qEGWhua4Z2uBrLW5WkHeL9Kg3sOr6kB8oCk4NYATzlsrrNhH6P8g0kR-o8mx5ZQlWME8gvl-bwoZHb3OMvEqB19yymO6-IYjy9Vp4_-3oTQi4GHfwcgCkKS-b6JrYT4lxuXntKo5uZmNhmnQY01j9MehMuNMvgms4y0nInuBbMdteXwEydd49u5Or9UbyHA8gVrfY31uUvrS8KDTF9hdFpEMln_wI8PLhi_IZiWFpKnQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">حقیقت یاب رپفا : عکس امیر تتلو در زندان که رسانه های سود جو بدون دقت پخش کردن  جعلی است! با  حتی کمی دقت فتوشاپ و کات ضعیف دست راست امیر و همچنین بی کیفیت کردن عکس برای پوشاندن خطا های سازنده آماتور آن مشخص است ، عکس اصلی رو هم قرار دادم که ببینید فرم دست ها هم یکسان است
@WarRoom
@RapFA
✅️</div>
<div class="tg-footer">👁️ 131K · <a href="https://t.me/withyashar/21153" target="_blank">📅 13:57 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-21152">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">ان بی سی : روسیه از طریق دریای خزر قطعات پهپاد، مهمات و تی‌ان‌تی را برای کمک به بازسازی ذخایر ایران که در حملات آمریکا و اسرائیل آسیب دیده‌اند، به ایران ارسال می‌کند. مسیر خزر عملاً غیرقابل مسدود کردن است. نیروی دریایی کشورهای غربی بر اساس کنوانسیون سال ۲۰۱۸ دسترسی قانونی به این منطقه ندارند و کشتی‌ها نیز مرتب سامانه‌های ردیابی خود را خاموش می‌کنند
@WarRoom</div>
<div class="tg-footer">👁️ 125K · <a href="https://t.me/withyashar/21152" target="_blank">📅 13:39 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-21151">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">رسانه های رژیم :  اسم فرودگاه مهرآباد به فرودگاه آیت الله خامنه‌ای تغییر خواهد کرد
@WarRoom</div>
<div class="tg-footer">👁️ 128K · <a href="https://t.me/withyashar/21151" target="_blank">📅 13:26 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-21150">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">رویترز
:
دو شرکت بزرگ حمل و نقل چینی، ارسال نفتکش‌ها را از طریق تنگه‌های هرمز و باب‌المندب متوقف کردند.
@WarRoom</div>
<div class="tg-footer">👁️ 129K · <a href="https://t.me/withyashar/21150" target="_blank">📅 12:00 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-21149">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">بوشهری های عزیز خنثی‌سازی هست اعلام شده
@WarRoom</div>
<div class="tg-footer">👁️ 132K · <a href="https://t.me/withyashar/21149" target="_blank">📅 11:27 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-21148">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">بلومبرگ : با اعلام عدم تمایل دونالد ترامپ، رئیس جمهور آمریکا به تمدید توافق رو به پایان با ایران و تشدید تنش‌ها در تنگه هرمز، چشم‌انداز صلح در خاورمیانه با رکود تازه‌ای مواجه شد.
@WarRoom</div>
<div class="tg-footer">👁️ 132K · <a href="https://t.me/withyashar/21148" target="_blank">📅 10:23 · 27 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>

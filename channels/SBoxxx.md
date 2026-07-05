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
<img src="https://cdn4.telesco.pe/file/NTwd6NGwGeXhGSofxTqHhyAgz147cYOE-SAIgj79NFbxyUAk4x8WC5X32srz2KPQPpFemErka1TsfCiGU4PDD1Jyyjc0jKMg9YHoqArSoHzJ9hrXvy6pAyPTwwn6F3zAeS1r6WyZ1oEYA5Lmxm60eNrGIYXlUI8GmAG-RlshAWMZW9VQFf9RMTPfK8NbSTCRDsFLoDDdEeJn5HqzRtvnLRtCDff7uuLESxs-L8IvP48eIf7mJDccyid_0S_zIAj1HAufBYu2xi35A5ZJRFu2JSzAQlQTuKRBfDRJSInJsBiF0EhWrLiDPQJTLt-zhR6UxEPKsH6zzdW9TyddzznY_Q.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Secret Box</h1>
<p>@SBoxxx • 👥 10.1K عضو</p>
<a href="https://t.me/SBoxxx" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 تاریخ، ژئوپولیتیک و بازارهای مالی</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-15 00:18:48</div>
<hr>

<div class="tg-post" id="msg-18235">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">سخنگوی دولت ایران، فاطمه مهاجرانی:  "ما در حال پیگیری قانونی شکایت مربوط به ترور رهبر سابق هستیم که با جمع‌آوری شواهد آغاز شده است".</div>
<div class="tg-footer">👁️ 2.22K · <a href="https://t.me/SBoxxx/18235" target="_blank">📅 22:31 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18234">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Fwr-aVCJuKWF3RXA5m1WDfodFqPf1ASk-o9S5ZKo6Py2nslv-PVQgYsE4ODCxPRDwdis66Dac7l1nkUB5Z3w-rf4glaWu-in1aPYAUi5GpWsEZAk5EDFxjNHrh4_dDuUYGqZlMkkyYkFZZoao3R5P7LM-f8CkAR9O4MXupW6uXaYpCMBcyx8UfZKYj4henzRiafcOlonl8x9au9oNlP2XNm3rDsZDPuN9LcRt3FSg3nsbJqWZpiRN5rfcfSL2tJMdicD4HNpnGz3ZwQZ2X5tI8mJNaaQb_Bm-9K77XAB4jS7YOjoSSBvNU2qSwvjvjqmPF8X9hKE_kSI1HAH1KQNRQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⭕️
استقرار بالن نظارتی (الکترواپتیکی)  در آسمان تهران</div>
<div class="tg-footer">👁️ 2.76K · <a href="https://t.me/SBoxxx/18234" target="_blank">📅 21:45 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18233">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">نتانیاهو:
«برخی روستاهای مسیحی‌نشین لبنان در واقع درخواست الحاق به اسرائیل را داده‌اند، زیرا ما از آنها در برابر حزب‌الله محافظت می‌کنیم.»</div>
<div class="tg-footer">👁️ 2.98K · <a href="https://t.me/SBoxxx/18233" target="_blank">📅 21:14 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18232">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">ایران می‌گوید از آتش‌بس با ایالات متحده برای تقویت آمادگی رزمی خود استفاده می‌کند.</div>
<div class="tg-footer">👁️ 3.42K · <a href="https://t.me/SBoxxx/18232" target="_blank">📅 20:10 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18231">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">دو نکته:  — از این میان ما سومی (J-20) را داریم. (البته ماکت ش)  — آخری (جنگنده کان یا خان ترکیه) فقط یک مشکل کوچک دارد و آن اینکه موتورش هنوز پیدا نشده که انشالله این هم حل می شود.</div>
<div class="tg-footer">👁️ 3.69K · <a href="https://t.me/SBoxxx/18231" target="_blank">📅 17:59 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18230">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">🔴
چرا نتوانستیم از صدام حسین غرامت بگیریم؟  حمزه رحیم صفوی.  @MonazeratChannel</div>
<div class="tg-footer">👁️ 3.97K · <a href="https://t.me/SBoxxx/18230" target="_blank">📅 16:10 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18229">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromمناظره‌ها</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c2f11f469c.mp4?token=tbWNI13x8ZWeGjfhx21I_0ZevN_hIQL6z7WPdlbgYjXRj3Xh5dAhg5DE0NMZTzutz5z4eLLTxdV5D5nmVJ0xAWIKCMXscsBWmQIPgV4027YQy93QNxVRZRRaWvJ7jz1wMd_txThu6sAmpZaSNINCtmN7KzycqQX2IKFrIen9Gz4AJz08bmbdMMbZdwTESaaYxbNeh_ignS1x1x_ufcmaQ5IOTBsv-xDROGqXome3h14YdQ7IarsaTMpjDbRsXJ9fbgRu04I5XEVQFOsbxZJvv6BR8l12tFix8UcmbwfhjFQsLwDGcnIeFrwptTAW9ngzDQATS45XZqykW-hWTQpuMQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c2f11f469c.mp4?token=tbWNI13x8ZWeGjfhx21I_0ZevN_hIQL6z7WPdlbgYjXRj3Xh5dAhg5DE0NMZTzutz5z4eLLTxdV5D5nmVJ0xAWIKCMXscsBWmQIPgV4027YQy93QNxVRZRRaWvJ7jz1wMd_txThu6sAmpZaSNINCtmN7KzycqQX2IKFrIen9Gz4AJz08bmbdMMbZdwTESaaYxbNeh_ignS1x1x_ufcmaQ5IOTBsv-xDROGqXome3h14YdQ7IarsaTMpjDbRsXJ9fbgRu04I5XEVQFOsbxZJvv6BR8l12tFix8UcmbwfhjFQsLwDGcnIeFrwptTAW9ngzDQATS45XZqykW-hWTQpuMQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
چرا نتوانستیم از صدام حسین غرامت بگیریم؟  حمزه رحیم صفوی.
@MonazeratChannel</div>
<div class="tg-footer">👁️ 3.84K · <a href="https://t.me/SBoxxx/18229" target="_blank">📅 16:06 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18228">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">سخنگوی دولت ایران، فاطمه مهاجرانی:  "ما در حال پیگیری قانونی شکایت مربوط به ترور رهبر سابق هستیم که با جمع‌آوری شواهد آغاز شده است".</div>
<div class="tg-footer">👁️ 3.79K · <a href="https://t.me/SBoxxx/18228" target="_blank">📅 15:57 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18227">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">مسؤولان آمریکایی نگران بودند که اسرائیل ممکن است در طول مذاکرات صلح حساس در بهار امسال، از جمله وزیر امور خارجه عباس عراقچی و رئیس مجلس محمدباقر قالیباف، رهبران مذاکره‌کننده ایران را ترور کند.  با نگرانی از اینکه چنین حمله‌ای مذاکرات را متوقف کرده و جنگ را…</div>
<div class="tg-footer">👁️ 3.77K · <a href="https://t.me/SBoxxx/18227" target="_blank">📅 15:52 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18226">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">📌
وخیم تر شدن وضعیت صنعت آلمان در اثر جنگ خاورمیانه  صنعت آلمان که پیش‌تر هم تحت فشار بود، با آغاز جنگ خاورمیانه، افت تولید صنعتی، کاهش رشد صادرات و افت محسوس مازاد تجاری در مارس، وارد وضعیت ضعیف‌تری شده و احتمال بازبینی نزولی رشد اقتصادی سه‌ماهه اول را بالا…</div>
<div class="tg-footer">👁️ 3.88K · <a href="https://t.me/SBoxxx/18226" target="_blank">📅 15:11 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18225">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">قالیباف، در مراسم تشییع رهبر سابق ایران:  «ثمره خون خامنه‌ای آزادی بیت المقدس خواهد بود».</div>
<div class="tg-footer">👁️ 3.98K · <a href="https://t.me/SBoxxx/18225" target="_blank">📅 13:04 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18224">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">سخنگوی دولت ایران، فاطمه مهاجرانی:  "ما در حال پیگیری قانونی شکایت مربوط به ترور رهبر سابق هستیم که با جمع‌آوری شواهد آغاز شده است".</div>
<div class="tg-footer">👁️ 4.04K · <a href="https://t.me/SBoxxx/18224" target="_blank">📅 12:59 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18223">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">کلا خاطره خوبی از محاسبه خسارات و جمع آوری شواهد نداریم.
بار پیش
هم که جناب عراقچی داشتند خسارات اشتباه محاسباتی اسراییل در جنگ ۱۲-روزه را محاسبه می‌کردند که اشتباه محاسباتی بعدی روی داد و اصلا محاسبات ما به هم ریخت.</div>
<div class="tg-footer">👁️ 4.1K · <a href="https://t.me/SBoxxx/18223" target="_blank">📅 12:40 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18222">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">سخنگوی دولت ایران، فاطمه مهاجرانی:  "ما در حال پیگیری قانونی شکایت مربوط به ترور رهبر سابق هستیم که با جمع‌آوری شواهد آغاز شده است".</div>
<div class="tg-footer">👁️ 4.32K · <a href="https://t.me/SBoxxx/18222" target="_blank">📅 12:15 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18221">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">سخنگوی دولت ایران، فاطمه مهاجرانی:
"ما در حال پیگیری قانونی شکایت مربوط به ترور رهبر سابق هستیم که با جمع‌آوری شواهد آغاز شده است".</div>
<div class="tg-footer">👁️ 4.4K · <a href="https://t.me/SBoxxx/18221" target="_blank">📅 12:14 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18220">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">Trump Accounts
سرمایه‌گذاری بر نسل آینده یا
پروژه‌ای سیاسی؟
دولت دونالد ترامپ با معرفی طرح «Trump Accounts» تلاش کرده است ایده‌ای را به اجرا بگذارد که در ظاهر، حمایت از آینده مالی کودکان آمریکایی را هدف قرار داده است. بر اساس این برنامه، برای هر کودک واجد شرایط، حسابی سرمایه‌گذاری ایجاد می‌شود و دولت برای نوزادان متولدشده در بازه زمانی تعیین‌شده، مبلغ اولیه‌ای را به این حساب واریز می‌کند. دارایی این حساب‌ها نیز در صندوق‌های شاخص کم‌هزینه سرمایه‌گذاری می‌شود تا در بلندمدت از رشد بازار سهام بهره‌مند شود.
طرفداران این طرح معتقدند که ایجاد سرمایه از ابتدای زندگی می‌تواند فرهنگ پس‌انداز و سرمایه‌گذاری را در جامعه آمریکا تقویت کند. از نگاه آنان، حتی یک سرمایه اولیه نسبتاً کوچک نیز در صورت رشد مستمر بازار، می‌تواند هنگام ورود فرد به بزرگسالی به منبعی برای تأمین هزینه تحصیل، خرید نخستین مسکن یا آغاز یک کسب‌وکار تبدیل شود. این رویکرد همچنین می‌تواند وابستگی شهروندان به کمک‌های مستقیم دولت را کاهش داده و مشارکت آنان در اقتصاد و بازار سرمایه را افزایش دهد.
در مقابل، منتقدان بر این باورند که اثر واقعی این برنامه به توانایی خانواده‌ها برای واریز مبالغ بیشتر به حساب فرزندانشان بستگی دارد. از این منظر، خانواده‌های پردرآمد بیش از دیگران از مزایای رشد سرمایه برخوردار خواهند شد و در نتیجه، شکاف ثروت میان طبقات مختلف جامعه ممکن است کاهش نیابد و حتی در بلندمدت افزایش پیدا کند. همچنین برخی ناظران، انتخاب نام «Trump Accounts» را اقدامی با رنگ‌وبوی سیاسی می‌دانند که می‌تواند این برنامه را به بخشی از میراث سیاسی رئیس‌جمهور تبدیل کند.
در مجموع، موفقیت یا شکست «Trump Accounts» به عملکرد بازارهای مالی، میزان مشارکت خانواده‌ها و نحوه اجرای مقررات آن وابسته خواهد بود. اگرچه این طرح می‌تواند گامی در جهت گسترش سرمایه‌گذاری عمومی باشد، اما قضاوت نهایی درباره آثار اقتصادی و اجتماعی آن تنها پس از گذشت چند سال و مشاهده نتایج عملی امکان‌پذیر خواهد بود.</div>
<div class="tg-footer">👁️ 4.38K · <a href="https://t.me/SBoxxx/18220" target="_blank">📅 11:15 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18219">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">رئیس‌جمهور فرانسه ماکرون:
فرانسه دارایی‌های ضد مین را به خاورمیانه اعزام کرده است، از جمله به‌ویژه دو کشتی  ویژه جستجوگر مین
همراه با دو ناوچه و یک هواپیمای گشت دریایی، این دارایی‌ها آماده هستند تا در کنار شرکای ما، به از سرگیری کامل کشتیرانی و تضمین ایمنی ترافیک در تنگه هرمز کمک کنند</div>
<div class="tg-footer">👁️ 4.46K · <a href="https://t.me/SBoxxx/18219" target="_blank">📅 08:53 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18218">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">🔻
پناهیان ؛ مشاوره ریاست نهاد نمایندگی رهبر در دانشگاه‌ها :
حاضریم تمامی منافع ملی را فدای خونخواهی رهبر شهیدمان کنیم</div>
<div class="tg-footer">👁️ 5.11K · <a href="https://t.me/SBoxxx/18218" target="_blank">📅 23:49 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18217">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">🔻
بابک زنجانی
:
به زودی خونخواهی رهبر شهید شروع خواهد شد و آن خون خواهی اقتصادی است</div>
<div class="tg-footer">👁️ 5.18K · <a href="https://t.me/SBoxxx/18217" target="_blank">📅 23:44 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18216">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">ایران قصد دارد به چین تعرفه‌های ترجیحی برای تنگه هرمز ارائه دهد
تهران قصد دارد به چین و سایر کشورهای دوستانه تعرفه‌های ترجیحی برای هزینه‌های عبور و مرور ورودی تنگه هرمز اعطا کند.</div>
<div class="tg-footer">👁️ 4.88K · <a href="https://t.me/SBoxxx/18216" target="_blank">📅 22:40 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18215">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">به گزارش کانال 15 اسرائیل، دونالد ترامپ از اسرائیل خواسته است که فعالیت‌های نظامی خود را در لبنان افزایش ندهد، زیرا نمی‌خواهد این امر در مذاکرات جاری او با ایران دخالت کند.
به همین دلیل،  نتانیاهو یک عملیات نظامی که پیش از این برای منطقه علی‌الطاهر برنامه‌ریزی شده بود، را به تعویق انداخته است.</div>
<div class="tg-footer">👁️ 4.79K · <a href="https://t.me/SBoxxx/18215" target="_blank">📅 22:36 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18214">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">رئیس‌جمهور عراق:   عراق نه با ایران در برابر آمریکا متحد است نه با آمریکا در برابر ایران</div>
<div class="tg-footer">👁️ 4.81K · <a href="https://t.me/SBoxxx/18214" target="_blank">📅 21:31 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18213">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">رئیس‌جمهور عراق:
عراق نه با ایران در برابر آمریکا متحد است نه با آمریکا در برابر ایران</div>
<div class="tg-footer">👁️ 4.74K · <a href="https://t.me/SBoxxx/18213" target="_blank">📅 21:28 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18212">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">ترامپ، رئیس‌جمهور ایالات متحده، گفت که آمریکا می‌توانست رهبران ایران را که برای مراسم تشییع آیت‌الله علی خامنه‌ای، رهبر پیشین، جمع شده بودند، هدف قرار دهد، اما این کار را انجام نمی‌دهد زیرا می‌خواهد مذاکرات هسته‌ای را حفظ کند.  «همه آن‌ها آنجا هستند. با یک…</div>
<div class="tg-footer">👁️ 4.84K · <a href="https://t.me/SBoxxx/18212" target="_blank">📅 20:49 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18211">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">ترامپ، رئیس‌جمهور ایالات متحده، گفت که آمریکا می‌توانست رهبران ایران را که برای مراسم تشییع آیت‌الله علی خامنه‌ای، رهبر پیشین، جمع شده بودند، هدف قرار دهد، اما این کار را انجام نمی‌دهد زیرا می‌خواهد مذاکرات هسته‌ای را حفظ کند.
«همه آن‌ها آنجا هستند. با یک شلیک [می‌توانیم همه آن‌ها را از بین ببریم]، اما این کار را نخواهیم کرد زیرا در آن صورت کسی برای مذاکره باقی نخواهد ماند»</div>
<div class="tg-footer">👁️ 4.91K · <a href="https://t.me/SBoxxx/18211" target="_blank">📅 20:40 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18210">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">اردوغان به اسرائیل هشدار داد: "نباید اجازه داد اسرائیل منطقه را در خون غرق کند."
رئیس‌جمهور ترکیه، اردوغان، در سخنانی مشترک با نخست‌وزیر پاکستان، لحن تندی علیه اسرائیل اتخاذ کرد.</div>
<div class="tg-footer">👁️ 4.71K · <a href="https://t.me/SBoxxx/18210" target="_blank">📅 20:01 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18209">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">باز این پفیوزها می خواهند تندروهای داخلی را تحریک کنند تا تنگه را ببندند و قیمت نفت بالا برود و غرب از کمک بیشتر به اوکراین که خشتک روسها را بر کله شان کشیده منصرف بشود.</div>
<div class="tg-footer">👁️ 4.68K · <a href="https://t.me/SBoxxx/18209" target="_blank">📅 18:35 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18208">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">ترکیه با موفقیت موشک بالستیک TAYFUN Block-3 را علیه هدف کشتی متحرک با سرعت هایپرسونیک آزمایش کرد.
شرکت ROKETSAN یک آزمایش آتش‌زنده از موشک بالستیک TAYFUN Block-3 انجام داد و با موفقیت یک کشتی سطحی بدون سرنشین آزاد در حرکت را در دریا با یک سر جنگی زنده با سرعت هایپرسونیک هدف قرار داد.
هدف حدوداً ۷ متری — که یک قایق ماهیگیری کوچک بود — با آنچه شرکت آن را «دقت جراحی‌گونه» توصیف کرد، نابود شد.
این آزمایش نخستین مورد از این دست است که در آن یک موشک بالستیک که با استفاده از سر جستجوگر برای هدایت در مرحله پایانی، یک کشتی سطحی متحرک را در دریا درگیر و هدف قرار می‌دهد.
ترکیه می‌گوید این نخستین یکپارچه‌سازی چنین سر جستجوگری بر روی یک موشک بالستیک در داخل کشور است و یکی از تنها چند نمونه در سراسر جهان — قابلیتی که به طور موثر یک موشک بالستیک را به یک سلاح ضد کشتی تبدیل می‌کند.
سرعت پایانی هایپرسونیک TAYFUN آن را تا حد زیادی در برابر پدافند‌های متعارف دفاع هوایی مصون می‌سازد.
نسخه Block-3 پیشرفته‌ترین نسخه از برنامه موشک بالستیک توسعه‌یافته داخلی ترکیه را نشان می‌دهد.</div>
<div class="tg-footer">👁️ 4.89K · <a href="https://t.me/SBoxxx/18208" target="_blank">📅 18:08 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18207">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">یک کارشناس:
به نظر می‌رسد که ایران در مراسم تشییع جنازه رهبر خود هر هیئت خارجی را با یک آیه قرآن مرتبط کرده است که هدف سیاسی خاصی را دنبال می‌کند.
عربستان سعودی: آیه ای درباره دو ارتش که در جنگ با یکدیگر روبرو می‌شوند، یکی مومن و دیگری غیرمومن.
ترکیه: آیه ای که کسانی را که در راه خدا می‌جنگند، بر کسانی که "نشسته"اند، برتری می‌بخشد.
دولت لبنان: آیه ای درباره افرادی که در صورت درخواست، از انجام فداکاری خودداری می‌کنند.
حزب الله: به آنها گفته شد "ضعیف نشوید یا غمگین نشوید، شما برتر هستید."
حماس: آیه ای که مردانی را که عهد خود را با خدا وفا کردند، مورد تقدیر قرار می‌دهد، "برخی از دنیا رفته‌اند، و برخی دیگر در انتظارند."
حوثی‌های یمن: آیه ای که به مومنانی که بدون سستی جنگیدند، ستایش می‌کند.
قطر: آیه ای درباره بخشش و لطف الهی، که به عنوان اشاره‌ای به نقش میانجی‌گری این کشور خوانده شد.</div>
<div class="tg-footer">👁️ 5.74K · <a href="https://t.me/SBoxxx/18207" target="_blank">📅 13:52 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18206">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">اظهارات مدودف، نخست‌وزیر روسیه:  ایران به جای سلاح‌های هسته‌ای، سلاح دیگری را کشف کرده است که از نظر قدرت، نه ضعیف‌تر از سلاح‌های هسته‌ای است و آن، تنگه هرمز است.  بحث‌ها حول این موضوع است که چگونه باید به توافقی دست یافت تا این تنگه در آینده به چه صورت عمل…</div>
<div class="tg-footer">👁️ 4.86K · <a href="https://t.me/SBoxxx/18206" target="_blank">📅 13:43 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18205">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">جناب الکساندر سرگین هستند از گه خورهای اعظم که بیرون گود نشسته و به ما میگویند لنگش کن!</div>
<div class="tg-footer">👁️ 4.94K · <a href="https://t.me/SBoxxx/18205" target="_blank">📅 13:42 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18204">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/d9y7aIPYKUqPAQEy2yGgNpK3TAAMLfsAKHqIP3cib-JJsRH9RaVAfOoQZMOi4Idhqf7VlRWfbVqPuxns3oFTHBNmFNsWPyD1Ui8-uTxLAcRgb65Lac9b3nfkK5BVYSpQ_vtB3okoqluQr5hnR2ZxXtXQTdAJwBctWWjIk1YOO3f1ZFdBRFKgdpYr9yBx_W8yVpmH3NFogqs11VYOcTmfzjhO93B40w4Sx8XcT-PAYFnMyINhde4dpoTGD39HkKEooE5yuOjKm9XJyV5Md_82JuhzuDmeI1p5DHXFrmDHn_TAm4kWBRj00B0BR382pxIY4-9kr6okzTD_-62kgPpkww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ونس ترنس هست اما نجس هم هست؟!</div>
<div class="tg-footer">👁️ 4.94K · <a href="https://t.me/SBoxxx/18204" target="_blank">📅 12:09 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18203">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">رسانه‌های غربی:
عمان قصد دارد پای کشورهای‌اروپایی را به تنگه‌ی هرمز باز کند و از آنجا که ایران قرارداد تقسیم تنگه را با عمان به امضا رسانده دیگر حق قانونی برای جلوگیری از این موضود ندارد.
در اولین قدم نیروی دریایی فرانسه قصد دارد در تنگه هرمز مستقر شود</div>
<div class="tg-footer">👁️ 5.18K · <a href="https://t.me/SBoxxx/18203" target="_blank">📅 10:14 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18202">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">امروز پوتین با لباس نظامی با رسانه ها گفتگو کرده و عملاً می خواهد از اعتبار و جایگاه خود دفاع کند.  حس خوبی ندارم....</div>
<div class="tg-footer">👁️ 4.93K · <a href="https://t.me/SBoxxx/18202" target="_blank">📅 10:07 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18201">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">ترامپ
:
ما مناقشه با ونزوئلا را در یک روز حل و فصل کردیم و ضربات بسیار سختی به ایران وارد کردیم.
طرف ایرانی بسیار مشتاق است و به هر طریقی به دنبال دستیابی به یک توافق سیاسی با ما است.
ما از روی حسن نیت به ایران یک هفته فرصت دادیم تا عملیات را متوقف کند تا مراسم تشییع جنازه برگزار شود.</div>
<div class="tg-footer">👁️ 5.15K · <a href="https://t.me/SBoxxx/18201" target="_blank">📅 09:45 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18200">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/W5D8Sw0FnYcxRHERm08-Cevmca2IctvQ32-gXlCCVKx0JP6QtJV2FnmRQJIoN56Fl8v9DEoiGO2dZp1LEjwY_Rzui7FoNN0m4zN0rV2U0ocqMiZzOYa_6SS87i3aAQ2ppRjhraptrYHW0UTT6vCLo6XjpOX4XCNv9yP_wBCOngFo8X1t-WpEmSSp4HojK4oTZwBVxE0kS9IKOoDaZR-jukSgrGTaGcB9YjxymE_3RXPGkIw80ORNXyFvBS1t5a8mwlLehObF1xDgSdcUCFbRFwNgMBiKOMGO125szBKjsFZKPvRHq38uIdjcNZdWt3PWq9682v0Zltqar5QEw3nJ9w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خطر جنگ هسته ای؟!
ساعت نمادین روز رستاخیز بار دیگر به یک یادآور قدرتمند از خطرات رو به رشد برای جامعه بین‌المللی تبدیل شده است. د
ر ارزیابی ابتدای سال ۲۰۲۶، مجله «بولتن دانشمندان اتمی»
عقربه‌های این ساعت را به ۸۵ ثانیه قبل از نیمه‌شب (ساعت فاجعه) رساند که نزدیک‌ترین فاصله به نقطه نمادین فاجعه جهانی در تاریخ است. این سازمان، تضعیف امنیت بین‌المللی، ضعف چارچوب‌های کنترل تسلیحات و رفتارهای فزاینده پرخاشگرانه قدرت‌های بزرگ را به عنوان دلایل اصلی این تصمیم ذکر کرد.
یکی از واضح‌ترین نشانه‌های این تضعیف، افزایش بکارگیری اصطلاحات هسته‌ای در گفتمان سیاسی و پوشش رسانه‌ای است. عباراتی مانند «حمله هسته‌ای»، «ضربه هسته‌ای»، «تهدید اتمی» و «تشدید هسته‌ای» بسیار بیشتر از چند سال پیش به کار می‌روند. در حالی که عبارت «حمله اتمی» بیشتر با اوایل جنگ سرد مرتبط است، گزارش‌های مدرن ترجیح می‌دهند از اصطلاحاتی مانند «حمله هسته‌ای» و «تهدید هسته‌ای» استفاده کنند. این تغییر نه تنها نشان‌دهنده تغییر زبان، بلکه نگرانی مجددی است که سلاح‌های هسته‌ای دوباره در محاسبات استراتژیک نقش مرکزی پیدا کرده‌اند.
جنگ در اوکراین نقش عمده‌ای در این روند داشته است. از آغاز این درگیری، مقامات روسی بارها امکان استفاده از سلاح‌های هسته‌ای را مطرح کرده‌اند، در حالی که دولت‌های غربی و تحلیلگران درباره اعتبار این تهدیدات بحث کرده‌اند. بولتن به طور خاص اشاره کرده است که جنگ روسیه و اوکراین با تحولات نظامی بی‌ثبات‌کننده و ارجاعات مکرر روسیه به سلاح‌های هسته‌ای همراه بوده است، که خطر محاسبه نادرست بین کشورهای دارای سلاح هسته‌ای را افزایش داده است. شکست‌های نظامی اخیر و فشارهای اقتصادی رو به رشد، بحث‌ها درباره گزینه‌های استراتژیک روسیه را تشدید کرده‌اند. گزارش‌ها و تحلیل‌ها بر فشارهایی که یک درگیری طولانی‌مدت بر تولید صنعتی، تحریم‌ها و زیرساخت‌های انرژی تحمیل کرده است، تأکید داشته‌اند. این فشارها باعث شده است که برخی تحلیلگران گمانه‌زنی کنند که مسکو ممکن است برای بازدارندگی از مداخله بیشتر غرب، بیشتر به سیگنال‌های هسته‌ای متکی شود. با این حال، فعلاً و در شرایط کنونی گمانه‌زنی درباره تصمیمات آینده روسیه نباید با شواهدی مبنی بر استفاده قریب‌الوقوع از سلاح‌های هسته‌ای اشتباه گرفته شود. کارشناسان نظامی و سیاسی عموماً چنین گفتمانی را بیشتر ابزاری برای اجبار و بازدارندگی می‌دانند تا نشانه‌ای قابل اعتماد از استفاده نزدیک از سلاح‌های هسته‌ای. با این حال کمبود گسترده بنزین و گازوئیل یا صف‌های طولانی سوخت در سراسر روسیه  بشدت روی روحیه و غرور ملی روسها تاثیر منفی گذاشته اند و برای نخستین بار از سال 2006 به این سو، مردم روسیه تصور می کنند استانداردهای کیفیت زندگی شان رو به نزول نهاده است. این مسئله روی پوتین و هیات حاکمه روسیه فشار می آورد تا دست به اقدامات تهاجمی تری برای تسلیم کردن اوکراین و ناتو بزنند که یکی از آنها می تواند بهره گیری از سلاحهای کشتار جمعی باشد.
از سوی دیگر، ناکامی نسبی آمریکا در دستیابی به همه اهداف نظامی اش در ایران نیز می تواند از دیگر حوزه هایی باشد که نهایتاً ترامپ را به استفاده از سلاح های هسته ای وادار کند. در این حوزه می توان به اشاره ترامپ به راهبرد «شرمن» استناد کرد که استعاره ای از یک استراتژی ویرانگر مخرب با تلفات بالا برای به تسلیم کشاندن دشمن می باشد. (
لینک
)</div>
<div class="tg-footer">👁️ 5.1K · <a href="https://t.me/SBoxxx/18200" target="_blank">📅 02:11 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18199">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iUatg6eM4gF9wuaeHNv9MS7Uuq15bQHkfkrD_TJd32GurhSxADzYzoC2ViBI10NSy-NP8R2rp7Qu28gMib4Ga0NE6unCLhfQut62KIxz3wngq00EgrUD5x2ttblp30TgEvVTT9bjIGypDOGKJX5ML0kLI_F5QGfekq6MsZ_AtRxC2AEcW1ZUtqgz0zXq29rsK3afUzZ3MHSDxJKwhyXErWfDvQ1_bhwAieK5pGwuF55dK3qKcNv6zSNp0nGSpMhzAdytd7ddwjYEUg-gSLk3AMHMhTRwTe6_cFD1e9c2rIS0nc9WZAb8Hihzs78v4xOMuXnhyxelM-SSIMrxusWvow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در اینجا گفته شد که پوتین مانند گربه ای در گوشه اتاقی بسته گیر افتاده و این خطرناک است</div>
<div class="tg-footer">👁️ 5.02K · <a href="https://t.me/SBoxxx/18199" target="_blank">📅 01:33 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18198">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rSaIwnvUoeukQ229YqKd50KqZeKsi9wiftvMaKp_ycG4WKhnppYJ8vClH8czw9gkd4TLgQTRUPD35GD0oC6ZvGM1gWhDGVOkS6N2KgdazP8qmUi3v-yy8EKRt33SjJ98-Jk1nfyj9T59eHx1mTkNE5XVnkfIQ_yUFUe0b8O7hbmvtqj2gVJwWxswKhHosCUCvbCqaOnYS7yR3Nt4RcYCjRXwVx6F7T4BctJRzF5Bqgkei6cn8ipaNC7ZtIbOP5YHlLw6N_fsx5ZjSHHXCqL665K-aNwd7NeyBC4KZh-_rS09YRUzy2URkit-O8xNrjfrq7ymyLi4_AG0-IHwqfMgGw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#پادکست_GeoMarkets  شماره — 1  جمعه 3 جولای 2026</div>
<div class="tg-footer">👁️ 4.88K · <a href="https://t.me/SBoxxx/18198" target="_blank">📅 01:25 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18197">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">دونالد ترامپ در آخرین افشای مالی سالانه خود گزارش داد که در سال ۲۰۲۵ حداقل ۱.۴ میلیارد دلار از کسب‌وکارهای مربوط به ارزهای دیجیتال و میم‌کوین‌ها درآمد داشته است. ارزهای دیجیتال به‌وضوح بزرگ‌ترین منبع درآمد او بوده‌اند.   این گزارش همچنین نشان داد که او ۲۶…</div>
<div class="tg-footer">👁️ 4.95K · <a href="https://t.me/SBoxxx/18197" target="_blank">📅 22:06 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18196">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">#پادکست_GeoMarkets  شماره — 1  جمعه 3 جولای 2026</div>
<div class="tg-footer">👁️ 4.91K · <a href="https://t.me/SBoxxx/18196" target="_blank">📅 22:03 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18195">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">مسکو با فروپاشی بنزین روبرو شده است.  پهپادهای اوکراینی عملیات بزرگترین پالایشگاه مسکو را مختل کرده‌اند  و این واحد تا سال ۲۰۲۷ تعطیل شده است، - رویترز</div>
<div class="tg-footer">👁️ 4.97K · <a href="https://t.me/SBoxxx/18195" target="_blank">📅 22:02 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18194">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">امام جمعه کرج:   اورانیوم غنی‌شده را رها نمی‌کنیم وتنگه هرمز را رها رها نمیکنیم</div>
<div class="tg-footer">👁️ 4.95K · <a href="https://t.me/SBoxxx/18194" target="_blank">📅 20:57 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18193">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">امام جمعه کرج:
اورانیوم غنی‌شده را رها نمی‌کنیم وتنگه هرمز را رها رها نمیکنیم</div>
<div class="tg-footer">👁️ 4.92K · <a href="https://t.me/SBoxxx/18193" target="_blank">📅 20:56 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18192">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">موسسه رتبه‌بندی فیچ، ریسک‌های مرتبط با ایران برای بخش‌های شرکتی در سطح جهان را مجدداً ارزیابی کرد
از دید این موسسه، شکنندگی توافق موقت ۶۰ روزه، به همراه عدم مشارکت اسرائیل، نشان می‌دهد که درگیری خاورمیانه همچنان تهدیدی برای صادرکنندگان شرکتی محسوب می‌شود.</div>
<div class="tg-footer">👁️ 5.02K · <a href="https://t.me/SBoxxx/18192" target="_blank">📅 20:50 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18191">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">نتانیاهو و ترامپ توافق کردند که به زودی در ایالات متحده با یکدیگر دیدار کنند - رسانه‌های اسرائیلی.</div>
<div class="tg-footer">👁️ 4.87K · <a href="https://t.me/SBoxxx/18191" target="_blank">📅 20:13 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18190">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">نتانیاهو و ترامپ توافق کردند که به زودی در ایالات متحده با یکدیگر دیدار کنند - رسانه‌های اسرائیلی.</div>
<div class="tg-footer">👁️ 4.73K · <a href="https://t.me/SBoxxx/18190" target="_blank">📅 20:12 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18189">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TlHsoveQ5-aWA68AYdxILWFLphp1hgpnn54AIcdx38OSm7d7maeo5H8w5maheKJFVgihTklo4BHFpeEEAuQtFgcPLs6_wwpTbadzCll2KMW_GGKuLGZ7JPObClhdytzuLdMFF-wdc3HBglNaoTAjuPN1y0DPY7Wo0VvlbwPR55FPqOQZd3fTk5dzNgO2d6obk2U6b49FU1r5V3rAJBUGKdWeHNd_WkUelPEMSmLbQ3p7mkHL3sE4aino1DV02S2h8SNKxgv6HJ6e35t6D6lg5OZKB-eYUc2kquLKABfPY8raoEMi56WUpwyBOBIzRsC60rkTf3EW1Rw3lqAVuD3clg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">راه اندازی ساختمان عظیم وزارت دفاع مصر!
افتتاح مجموعه «هشت‌ضلعی» (The Octagon) به‌عنوان مقر جدید وزارت دفاع و فرماندهی راهبردی مصر را می‌توان یکی از مهم‌ترین نمادهای تحول ساختاری نیروهای مسلح این کشور در دهه اخیر دانست. این مجموعه عظیم که در پایتخت اداری جدید مصر ساخته شده، قرار است تمامی ستادهای اصلی نیروهای مسلح را در یک مرکز واحد گرد هم آورد و با بهره‌گیری از سامانه‌های پیشرفته فرماندهی، کنترل، ارتباطات و مدیریت اطلاعات، سرعت و هماهنگی تصمیم‌گیری‌های نظامی را به شکل قابل توجهی افزایش دهد.
ساخت چنین مرکزی تنها یک پروژه عمرانی نیست، بلکه بخشی از راهبرد بلندمدت قاهره برای تبدیل ارتش مصر به نیرویی مدرن، شبکه‌محور و آماده مقابله با تهدیدات متنوع منطقه‌ای است. طی سال‌های گذشته، مصر سرمایه‌گذاری گسترده‌ای در نوسازی تجهیزات نظامی، توسعه صنایع دفاعی و خرید سامانه‌های پیشرفته از کشورهای مختلف انجام داده و اکنون ایجاد یک مرکز فرماندهی یکپارچه، حلقه تکمیل‌کننده این روند محسوب می‌شود.
از منظر ژئوپلیتیکی نیز افتتاح «هشت‌ضلعی» پیام مهمی برای بازیگران منطقه دارد. مصر در سال‌های اخیر تلاش کرده جایگاه خود را به‌عنوان یکی از قدرت‌های اصلی نظامی و امنیتی خاورمیانه و شمال آفریقا تثبیت کند. تمرکز فرماندهی نیروهای زمینی، دریایی، هوایی و پدافندی در یک مجموعه واحد، ضمن افزایش کارآمدی عملیاتی، توان مدیریت بحران‌های هم‌زمان در جبهه‌های مختلف را نیز تقویت می‌کند.
همزمان، انتقال وزارت دفاع از مرکز سنتی قاهره به پایتخت اداری جدید، نشان‌دهنده اهمیت این شهر در ساختار آینده حکومت مصر است. دولت مصر با انتقال تدریجی نهادهای حاکمیتی به این شهر، در پی ایجاد مرکز سیاسی، اداری و امنیتی جدیدی است که از زیرساخت‌های مدرن و استانداردهای بالای حفاظتی برخوردار باشد.
در مجموع، افتتاح «هشت‌ضلعی» را باید فراتر از افتتاح یک ساختمان نظامی ارزیابی کرد؛ این پروژه نماد ورود نیروهای مسلح مصر به مرحله‌ای جدید از سازماندهی، فرماندهی و آمادگی عملیاتی است و می‌تواند بر موازنه قدرت و معادلات امنیتی منطقه نیز تأثیرگذار باشد.</div>
<div class="tg-footer">👁️ 4.87K · <a href="https://t.me/SBoxxx/18189" target="_blank">📅 20:11 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18188">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">حوثی ها می‌گویند جنگنده‌های سعودی را از آسمان یمن بیرون کردند زیرا سعی در جلوگیری از فرود یک هواپیمای مسافربری ایرانی در صنعا داشتند.
آن‌ها هشدار دادند که اقدامات آینده سعودی با حملات به فرودگاه‌های سعودی و سایر اهداف حیاتی پاسخ داده خواهد شد.</div>
<div class="tg-footer">👁️ 4.77K · <a href="https://t.me/SBoxxx/18188" target="_blank">📅 18:46 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18187">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">از زمانی که روس‌ها تلگرام را محدود کرده اند و ایلان ماسک هم استفاده دزدانه شان از استارلینک را محدود کرده، توان آفندی پهپادی ارتش ظفرنمون مسکووی بشدت کاهش یافته است.</div>
<div class="tg-footer">👁️ 4.83K · <a href="https://t.me/SBoxxx/18187" target="_blank">📅 16:15 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18186">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">اسرائیلی ها، تاسیس پایگاه نظامی از سوی ترکیه در عمق خاک سوریه را به عنوان تهدیدی برای خود ارزیابی می کنند!  حملات ویرانگر اسرائیل ضد پایگاه T-4 نیز در همین راستا ارزیابی می شود.</div>
<div class="tg-footer">👁️ 4.83K · <a href="https://t.me/SBoxxx/18186" target="_blank">📅 15:50 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18185">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/soB-Oa_eKNH_5K0_qUc-iBZ5liJOVTNryYB3Uvc_oh78kUcRU_UK3bVW2nfSic5lfWxTeVylZqnfSNhPKRRXO7Tva4AJbYDorMgfoXD33TAnOp7QqJJCLRw8uZ_iWvhxI1PJcKbKLxYZ4XJ3FNh-UAQKOcK8jMZQ7RBFDnbNh3iAFiozj8fT8P9-trQv5L0HxyBnqvmOBRu-N1eHSGYVElAvMMbb48yqcjuh5HvQYL1BFKo8z-NdYktfEI3CfqimOt-dAUzMpXjckvKURC2HOM41uFlbMQmocu3KsaG3BICKUL0ZMSv-Jk3cjdL7Z6tHKjW3lZj6CIJ2la5rBDn8CA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پس فرق این دوره ۶۰ روزه با بعدش این است که ممکن است بعدش آمریکا عوارض عبور بگیرد!  سبحان الله!</div>
<div class="tg-footer">👁️ 5.14K · <a href="https://t.me/SBoxxx/18185" target="_blank">📅 13:30 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18184">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-poll">
<h4>📊 مدت زمان و محتوای پادکست مطلوب است:</h4>
<ul>
<li>✓ کوتاه تر — بازاری تر</li>
<li>✓ کوتاه تر — بدون تغییر محتوا</li>
<li>✓ بدون تغییر در مدت زمان — بازاری تر</li>
<li>✓ بدون تغییر در مدت زمان و محتوا</li>
</ul>
</div>
<div class="tg-text">#پادکست_GeoMarkets  شماره — 1  جمعه 3 جولای 2026</div>
<div class="tg-footer">👁️ 4.77K · <a href="https://t.me/SBoxxx/18184" target="_blank">📅 11:21 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18183">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">Audio</div>
  <div class="tg-doc-extra"></div>
</div>
<a href="https://t.me/SBoxxx/18183" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">#پادکست_GeoMarkets
شماره — 1
جمعه 3 جولای 2026</div>
<div class="tg-footer">👁️ 4.76K · <a href="https://t.me/SBoxxx/18183" target="_blank">📅 11:17 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18182">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hex09h-9P4KTYvg1mOnLaXnprXD8wgt49nYQIflWasdwFTZBxhuVy4p1GtP8Sfhzyk3OIB5OTZCY2690mcIHCr9gRdF3EHZ7_v6MPFdFadWv3PmcDGF2ZNB68Xl55IklzBdpS2ebVmMogbUNxSI6sGb5FeoJjf5URlZL0UBJrCTdenRQ4La5-W2fzsit0sCqvSaPo0OPPPTzfVbTD63jwv0yMOPh1YSmVV2M-v-Xn6bRrJMxf4rlzh9flHvMLJNiP30q4q0L_VFPUhhT3qqdkhFQaUtYZs4xZYsYEJGMwoCkcfUp6Wf6Xd-LLTRPI2A_ZCQqDhN_lhNfUC0FaBe1ew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#GRI
شاخص ریسک ژئوپولیتیک برای امروز نسبتاً پایین است و ریسک پذیری ملایم پیش بینی می شود.</div>
<div class="tg-footer">👁️ 4.75K · <a href="https://t.me/SBoxxx/18182" target="_blank">📅 10:48 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18181">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">این بستن تنگه هرمز نهایتا باعث:  — ایجاد مسیرهای جایگزین  — تقویت تقاضا برای نفت آمریکا، کانادا و روسیه — تسریع در انقلاب انرژی سبز  خواهدشد</div>
<div class="tg-footer">👁️ 4.7K · <a href="https://t.me/SBoxxx/18181" target="_blank">📅 10:44 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18180">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">تحلیل مهدی خانعلی‌زاده از مخالفین توافق با آمریکا از وضعیت اجرای تفاهم‌نامه پایان جنگ در روز چهاردهم</div>
<div class="tg-footer">👁️ 4.77K · <a href="https://t.me/SBoxxx/18180" target="_blank">📅 10:35 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18179">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">تحلیل مهدی خانعلی‌زاده از مخالفین توافق با آمریکا از وضعیت اجرای تفاهم‌نامه پایان جنگ در روز چهاردهم</div>
<div class="tg-footer">👁️ 4.67K · <a href="https://t.me/SBoxxx/18179" target="_blank">📅 10:28 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18178">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Dc3l3_WR2i4Ia4N5IsMh9gSPhaNaNHNq6UUTzUSBLdGp3UMOdqgSlCCTMbobFLqh3uGGgcc-daHownncpsSRVxP0VAXy5OjLSjTT1B83zKDDqKw8TRBe7Pgz1Jl9RZsrxiU_2wjnKq8bl7hxYH2ydjGrMWKTANM6U2cGfkLl5yckOzBRoH1xuqc2Bi5bKfJ9JE93_WzLyLK2puX_fter61jR9Q1G5sokFPPQzIHzvipqdft7J6E9CasR8XBDy6lL_80mMURjf-1TiVHcyXdN4tLOGLdIAJF2-S_-GXGVkme6_4hgdT-kf4A8bwD5J9K9-1UluHUhu2IJShNdGAMFjQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تحلیل مهدی خانعلی‌زاده از مخالفین توافق با آمریکا از وضعیت اجرای تفاهم‌نامه پایان جنگ در روز چهاردهم</div>
<div class="tg-footer">👁️ 4.83K · <a href="https://t.me/SBoxxx/18178" target="_blank">📅 10:25 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18177">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">همکاری نظامی اسرائیل-مراکش و پیام راهبردی به مادرید
همکاری نظامی اسرائیل و مراکش دیگر صرفاً یک رابطه تجاری در حوزه صنایع دفاعی نیست؛ این همکاری به تدریج به یکی از مهم‌ترین مؤلفه‌های معادلات ژئوپلیتیکی غرب مدیترانه تبدیل شده است. از انتقال فناوری پهپادهای انتحاری و سامانه‌های شناسایی گرفته تا تولید مشترک برخی تجهیزات نظامی در خاک مراکش، شواهد نشان می‌دهد که تل‌آویو در حال سرمایه‌گذاری بلندمدت بر ارتقای توان نظامی رباط است.
این تحول زمانی اهمیت بیشتری پیدا می‌کند که در کنار سردی بی‌سابقه روابط اسرائیل و دولت چپ‌گرای اسپانیا قرار گیرد. دولت مادرید در دو سال گذشته از منتقدان جدی سیاست‌های اسرائیل در غزه بوده، از به رسمیت شناختن کشور فلسطین حمایت کرده و در مجامع بین‌المللی مواضعی اتخاذ کرده که با مخالفت شدید تل‌آویو روبه‌رو شده است. (لینک ها:
یک
|
دو
|
سه
) طبیعی است که این تنش سیاسی، بر محاسبات راهبردی اسرائیل نیز تأثیر بگذارد.
در چنین فضایی، افزایش توان نظامی مراکش پیامدهایی فراتر از شمال آفریقا دارد. مراکش همچنان ادعای حاکمیت بر سئوتا، ملیله و چند قلمرو اسپانیا در سواحل آفریقا را حفظ کرده است. هرچند رباط بارها تأکید کرده که این موضوع را از مسیرهای سیاسی دنبال می‌کند، اما از نگاه بسیاری از ناظران اسپانیایی، تجهیز ارتش مراکش با فناوری‌های پیشرفته اسرائیلی، موازنه قوا در غرب مدیترانه را به زیان اسپانیا تغییر می‌دهد. پرسش نمایندگان حزب راست گرای Vox ووکس در پارلمان اسپانیا درباره آمادگی این کشور در برابر پهپادهای انتحاری ساخت مشترک اسرائیل و مراکش نیز بازتاب همین نگرانی است.
سیاست بین‌الملل، برداشت بازیگران نیز به اندازه نیت آنها اهمیت دارد. حتی اگر انگیزه اصلی اسرائیل اقتصادی یا ژئوپلیتیکی باشد، نتیجه عملی آن افزایش فشار امنیتی بر کشوری است که در سال‌های اخیر یکی از منتقدان اصلی سیاست‌های تل‌آویو در اروپا بوده است. از این منظر، تسلیح مراکش را می‌توان نه لزوماً «مجازات» اسپانیا، بلکه پیامی راهبردی در راستای بازآرایی موازنه قدرت در غرب مدیترانه دانست؛ بازآرایی‌ای که به‌طور طبیعی هزینه‌های راهبردی بیشتری را بر مادرید تحمیل می‌کند و می‌تواند بر محاسبات آینده دولت اسپانیا در قبال اسرائیل نیز اثرگذار باشد.</div>
<div class="tg-footer">👁️ 4.69K · <a href="https://t.me/SBoxxx/18177" target="_blank">📅 01:51 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18176">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0ff61a516b.mp4?token=ZPIYquKPvqnqj8yOJFUVej-tOZ617elnT-e_146EIJhppnRFL_B38Esa6NiY6bl7n6cVx5lqejAzlGI7Flzkurm9ps61OTr87Hime0xMxSnU082gRHkTdCPXKcO6xdqfjLMwFQ3EZVPedSFXthTo286gFvYTW1VOUW9gZusPnBHVOrppgZ528CEwqZTG6ZT97P-lAfQSlspItbU7A-kdBUePYWwb5j2pekBbcZH_tPe-gjLdUC1ouIkl-POFhYI37rsTf8VJuMeXyBDW1tiWhb2XW2jnekiQdN3DwZ0-4YijU3Um0pO3bMdfm8lT6F9vntDTyJ39qr-GL7YgLlKbog" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0ff61a516b.mp4?token=ZPIYquKPvqnqj8yOJFUVej-tOZ617elnT-e_146EIJhppnRFL_B38Esa6NiY6bl7n6cVx5lqejAzlGI7Flzkurm9ps61OTr87Hime0xMxSnU082gRHkTdCPXKcO6xdqfjLMwFQ3EZVPedSFXthTo286gFvYTW1VOUW9gZusPnBHVOrppgZ528CEwqZTG6ZT97P-lAfQSlspItbU7A-kdBUePYWwb5j2pekBbcZH_tPe-gjLdUC1ouIkl-POFhYI37rsTf8VJuMeXyBDW1tiWhb2XW2jnekiQdN3DwZ0-4YijU3Um0pO3bMdfm8lT6F9vntDTyJ39qr-GL7YgLlKbog" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ:  ما رادارهای ایران را نابود کردیم. آن‌ها هیچ راداری نداشتند. و هنوز هم ندارند.  ما چند شب قبل دوباره آن را نابود کردیم. آن‌ها یک رادار جدید و پیشرفته داشتند. آن‌ها آماده بهره‌برداری از آن بودند، اما ما آن را نابود کردیم.</div>
<div class="tg-footer">👁️ 4.64K · <a href="https://t.me/SBoxxx/18176" target="_blank">📅 01:44 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18175">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">ترامپ:
ما رادارهای ایران را نابود کردیم. آن‌ها هیچ راداری نداشتند. و هنوز هم ندارند.
ما چند شب قبل دوباره آن را نابود کردیم. آن‌ها یک رادار جدید و پیشرفته داشتند. آن‌ها آماده بهره‌برداری از آن بودند، اما ما آن را نابود کردیم.</div>
<div class="tg-footer">👁️ 4.63K · <a href="https://t.me/SBoxxx/18175" target="_blank">📅 01:35 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18174">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">مسؤولان آمریکایی نگران بودند که اسرائیل ممکن است در طول مذاکرات صلح حساس در بهار امسال، از جمله وزیر امور خارجه عباس عراقچی و رئیس مجلس محمدباقر قالیباف، رهبران مذاکره‌کننده ایران را ترور کند.
با نگرانی از اینکه چنین حمله‌ای مذاکرات را متوقف کرده و جنگ را دوباره شعله‌ور کند، واشنگتن از کشورهای منطقه خواست تا ایران را از این خطر آگاه کنند.
ایران اقدامات امنیتی گسترده‌ای برای محافظت از هیئت خود انجام داد، از جمله اسکورت نظامی و تغییر برنامه‌های سفر پس از دریافت اطلاعاتی درباره احتمال حمله اسرائیلی.
منبع: نیویورک تایمز</div>
<div class="tg-footer">👁️ 4.93K · <a href="https://t.me/SBoxxx/18174" target="_blank">📅 22:39 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18173">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-poll">
<h4>📊 در‌ جنگ میان ترکیه و اسراییل دوست دارید:</h4>
<ul>
<li>✓ پیروزی ترکیه</li>
<li>✓ پیروزی اسراییل</li>
<li>✓ جنگ فرسایشی بدون برنده</li>
<li>✓ من Gay هستم و دوست دارم جنگ نشود</li>
</ul>
</div>
<div class="tg-footer">👁️ 4.79K · <a href="https://t.me/SBoxxx/18173" target="_blank">📅 22:14 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18172">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">برای این جنگ لحظه شماری میکنم…</div>
<div class="tg-footer">👁️ 4.64K · <a href="https://t.me/SBoxxx/18172" target="_blank">📅 21:57 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18171">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">وزیر امور خارجه ترکیه، هاکان فیدان:
سیاستمداران آمریکایی تا زمانی که حمایت از اسرائیل به منافع خودشان خدمت کند، از اسرائیل حمایت می‌کنند.
این پویایی آن‌قدر طولانی شده است که همسویی بین حمایت از اسرائیل و پیشبرد منافع ایالات متحده به عنوان یک فرض دائمی تلقی شده است.
با این حال، برای اولین بار از زمان نسل‌کشی در غزه، تحلیل‌هایی که ظهور کرده‌اند به نتیجه متفاوتی اشاره دارند: «سیستم موجود در حال کار علیه منافع ماست.»
هیچ‌کس ادامه سیستمی را نمی‌خواهد که در نهایت علیه منافع خودشان کار می‌کند.
در سراسر جهان، از دانشگاه‌ها تا روزنامه‌ها، احساسات ضد اسرائیلی به‌طور چشمگیری افزایش یافته است.
چرا؟ زیرا مردم می‌بینند که اسرائیل آشکارا در حال ارتکاب کشتار است و در هر جایی که اقدام می‌کند، نقش بی‌ثبات‌کننده‌ای ایفا می‌کند.
در گذشته، آن‌ها می‌توانستند این موضوع را با چند مانور رسانه‌ای ساده پنهان کنند. اکنون، دیگر نمی‌توانند آن را پنهان نگه دارند.
اسرائیل در حال حاضر به دنبال یک دشمن جدید است.
تا زمانی که اسرائیل — یا هر بازیگر دیگری — به روش‌هایی عمل کند که با منافع ملی و منطقه‌ای ما در تضاد است، ما هیچ دلیلی برای ترسیدن، مردد شدن یا عقب‌نشینی نداریم.
ما مشکلی با رویارویی نداریم. اگر به آنجا برسد، برای ما مسئله‌ای نیست.
اسرائیل فقط مشکل من نیست؛ مشکل جهان است.</div>
<div class="tg-footer">👁️ 4.87K · <a href="https://t.me/SBoxxx/18171" target="_blank">📅 21:55 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18170">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">وزیر دفاع اسرائیل:
ارتش اسرائیل باید برای انجام جنگ مستقل علیه ایران آماده شود.</div>
<div class="tg-footer">👁️ 4.72K · <a href="https://t.me/SBoxxx/18170" target="_blank">📅 21:27 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18169">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">عبدالمجید حکیم الهی، نماینده رهبر ایران در هند، گفت که به دلیل نگرانی‌های امنیتی، بعید است آیت الله مجتبی خامنه‌ای در مراسم تشییع جنازه پدرش شرکت کند.
وی افزود که آیت الله مجتبی خامنه‌ای مایل بود نماز میت را اقامه کند، اما مقامات امنیتی این کار را بسیار خطرناک دانسته‌اند.</div>
<div class="tg-footer">👁️ 5.23K · <a href="https://t.me/SBoxxx/18169" target="_blank">📅 21:00 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18168">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">تولید نفت خام کویت در ژوئن به طور میانگین ۱.۶۵ میلیون بشکه در روز بود در مقابل ۵۷۸,۰۰۰ بشکه در روز در ماه مه</div>
<div class="tg-footer">👁️ 4.68K · <a href="https://t.me/SBoxxx/18168" target="_blank">📅 19:03 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18167">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">🩵
کاتز ؛ وزیردفاع دولت اسرائیل
:
ما درحال توسعه لیزرهای فضایی برای تهاجم خارج از جو زمین هستیم
يسرائيل كاتز ،  اعلام کرد دولت اسرائیل در حال توسعه لیزرهای فضایی به منظور توانایی حمله در فضا است.
به گزارش اورشلیم ،پست کاتز در نشستی با خبرنگاران نظامی گفت: یکی از اهداف اصلی که نخست وزیر و من تعیین کرده ایم این است که برترین استعدادها را جذب کنیم تا امروز هیچ کشوری توانایی اجرای حمله در فضا را نداشته است. ما باید در برخورداری از این توانایی کشور پیشرو جهان باشیم
او افزود: اگر به این هدف دست یابیم این امر میتواند برتری بازدارندگی، توانایی حمله و انهدام و دیگر برتری های راهبردی ما را در برابر دشمنانی که از منابع گسترده برخوردارند تضمین کند
کاتز پنجشنبه گذشته گفته بود اسرائیل مصمم است به بازیگر پیشرو در زمینه توانایی حمله از فضا تبدیل شود با این حال این نخستین بار بود که به طور مشخص از لیزرهای فضایی نام می برد
اسرائیل هم اکنون نیز در این حوزه از کشورهای پیشرو به شمار میرود و سامانه موسوم به پرتو آهنین (Iron Beam) را به عنوان یک لیزر فضایی مستقر در زمین تولید کرده است
سامانه پرتو آهنین که اواخر سال گذشته به ارتش اسرائیل تحویل داده شد نقطه عطفی تاریخی به شمار میرود زیرا نخستین سامانه دفاع لیزری عملیاتی جهان است که میتواند راکتها پهپادها و خمپاره ها را با هزینه ای بسیار کمتر از رهگیرهای سنتی، خنثی کند</div>
<div class="tg-footer">👁️ 5.06K · <a href="https://t.me/SBoxxx/18167" target="_blank">📅 16:04 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18166">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">🔴
فرمانده سپاه پاسداران قم
:
تمهیدات زیادی اتخاذ کردیم اما بصورت قطعی نمی‌دانیم در مراسم تشییع رهبرانقلاب چه اتفاقی خواهد افتاد</div>
<div class="tg-footer">👁️ 4.9K · <a href="https://t.me/SBoxxx/18166" target="_blank">📅 15:58 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18165">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">دور بعدی مذاکرات آمریکا و ایران در ۱۸ ژوئیه (۱۶ روز دیگر) آغاز می‌شود.</div>
<div class="tg-footer">👁️ 5K · <a href="https://t.me/SBoxxx/18165" target="_blank">📅 14:35 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18164">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">🔻
غضنفری ؛ نماینده مجلس
:
یک شبه کودتای سیاسی علیه رهبری نظام درجریان است - تجمعات شبانه نباید جمع شود</div>
<div class="tg-footer">👁️ 5.25K · <a href="https://t.me/SBoxxx/18164" target="_blank">📅 13:33 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18163">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">دلار ۱۷۷۰۰۰ تومان!</div>
<div class="tg-footer">👁️ 5.28K · <a href="https://t.me/SBoxxx/18163" target="_blank">📅 11:30 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18162">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MDHUowY0bM2t6DRdFt_81-ucsN41jihP_HESZnHgEb0Wqbk2Du9ACGmhsLZBRVcZXFBhS209knBS-Ln2rrsJ_IzXUCwdi9vUlCtwAssrNfRHCa95I2uC1ca_H6qD70S6OL4RlyTX7xbAHSIU8Q3WsI71freya31YLv-vVpdneU116NVAIY6sbKPnE0fiyI65pfaVMwPy9Nn2ySyKkZ1GPjdw6jZcgRP4GNYgRHAvp22VhTyhvabjob14ySrftIu--cAF24lZFh96a_BjN3rkBYMBWgA14HTkDsMAFCSXy6qfcaWW08CdUfch2VDifATXZKaEqO24MEuxTH77_v4tZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#GRI
شاخص ریسک ژئوپولیتیکی برای امروز در سطح بالایی قرار دارد.
توصیه می شود با توجه به انتشار گزارش NFP، امروز با کمترین حجم معامله کنید.</div>
<div class="tg-footer">👁️ 5.29K · <a href="https://t.me/SBoxxx/18162" target="_blank">📅 09:57 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18161">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">جهش انفجاری معاملات شخصی ترامپ در سه ماهه نخست ۲۰۲۶!</div>
<div class="tg-footer">👁️ 5.26K · <a href="https://t.me/SBoxxx/18161" target="_blank">📅 01:56 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18160">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">گویا گروه‌های مسلح تجزیه طلب کردی با حزب الله طاق زده شده اند.</div>
<div class="tg-footer">👁️ 5.53K · <a href="https://t.me/SBoxxx/18160" target="_blank">📅 01:38 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18159">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">آمریکا رسماً توافق‌نامه‌ای برای ساخت سفارت دائمی در اورشلیم امضا کرد.</div>
<div class="tg-footer">👁️ 5.17K · <a href="https://t.me/SBoxxx/18159" target="_blank">📅 00:07 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18158">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">سقوط بالگرد MH-60S Seahawk نیروی دریایی ایالات متحده در دریای عرب
ناوگان پنجم ایالات متحده اعلام کرد که یک بالگرد MH-60S Seahawk نیروی دریایی ایالات متحده که به ناو هواپیمابر USS George H.W. Bush اختصاص داده شده بود، اوایل روز چهارشنبه در دریای عرب فرود اضطراری انجام داد.
سه نفر از چهار خدمه در وضعیت پایداری پیدا شده‌اند. جستجو برای یافتن نفر چهارم در حال انجام است.
ناوگان پنجم اعلام کرد که هیچ نشانه‌ای مبنی بر اینکه این وضعیت اضطراری ناشی از اقدام خصمانه بوده باشد، وجود ندارد و علت آن در دست بررسی است.
این دومین سقوط بالگرد نظامی ایالات متحده در منطقه در هفته‌های اخیر است.
یک بالگرد AH-64 آپاچی ارتش در 9 ژوئن در خلیج عمان سقوط کرده بود که ترامپ گفت که نیروهای ایرانی آن را سرنگون کردند و خدمه توسط یک قایق بدون سرنشین Corsair نجات یافتند.</div>
<div class="tg-footer">👁️ 5.24K · <a href="https://t.me/SBoxxx/18158" target="_blank">📅 20:56 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18157">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">جی‌دی وانس در مورد ایران:  چند روز پیش چند بمب روی آنها انداختیم. می‌دانید چرا؟ چون ایرانی‌ها به کشتی‌های تجازی شلیک می‌کردند.  چند بمب انداختیم، اهرم فشار اعمال کردیم و در عوض در سه روز گذشته، عبور و مرور تجاری آزاد داشته‌ایم.</div>
<div class="tg-footer">👁️ 5.26K · <a href="https://t.me/SBoxxx/18157" target="_blank">📅 20:01 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18156">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">جی‌دی وانس در مورد ایران:
چند روز پیش چند بمب روی آنها انداختیم. می‌دانید چرا؟ چون ایرانی‌ها به کشتی‌های تجازی شلیک می‌کردند.
چند بمب انداختیم، اهرم فشار اعمال کردیم و در عوض در سه روز گذشته، عبور و مرور تجاری آزاد داشته‌ایم.</div>
<div class="tg-footer">👁️ 5.06K · <a href="https://t.me/SBoxxx/18156" target="_blank">📅 19:48 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18155">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">موجودی نفت خام آمریکا در ذخایر استراتژیک نفت (SPR) در هفته گذشته به پایین‌ترین حد از ماه مه ۱۹۸۳ رسید - EIA|</div>
<div class="tg-footer">👁️ 5.11K · <a href="https://t.me/SBoxxx/18155" target="_blank">📅 18:24 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18154">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">ذخایر نفتی آمریکا و جنگ با ایران  آمریکا از ذخایر راهبردی نفت به‌عنوان ابزاری برای مدیریت شوک‌های بازار و کنترل فشار انرژی استفاده کرده و کاهش اخیر این ذخایر باعث شده بازسازی آن‌ها به یکی از اولویت‌های مهم واشنگتن تبدیل شود.  برخی تحلیلگران معتقدند کاهش تنش…</div>
<div class="tg-footer">👁️ 4.97K · <a href="https://t.me/SBoxxx/18154" target="_blank">📅 18:23 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18153">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dUbMZ7wYXy-DmObvjf8GJwvl5ae3iahuf0WnVBG6zTE5Ye0jcVSFCIjuaPsjhbkvkQ5gdl4Z4l22DYNCIAfqu22AKU8ltOVjAkPt7zmTe9Rd_99cTxVt_Lk9Miq-XCQW5crHUFqlJMFY8_TdnTjHshAGLa6rRSGaob7Ey_RsQSCB5sCV6KCiFbiByM0yp3XhfD2Xzd80qNVCYXctjB7_IeUvIoQtNyPXCgAvDyRiyB3HMWCN3TIZfTsfPvVzMQNRwnB7TMEHqv4VCj0hFeT4BBfiZCovx1DmaFhdnj1rknycs7J3LIQtoIr4vykYFdwQKLyHDuJZjfTDShtUaYniNQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">برای سومین روز متوالی ، امانوئل مکرون با عینک آفتابی دیده شده است.
به نظرتان کار آن عفریته زنش است یا صبیه وجیهه رفیق بهزاد؟!</div>
<div class="tg-footer">👁️ 5.08K · <a href="https://t.me/SBoxxx/18153" target="_blank">📅 15:51 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18152">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">گفته می‌شود با اجرایی شدن این توافق، قیمت چص فیل در سرزمینمان بزودی ۹۰ درصد سقوط می کند</div>
<div class="tg-footer">👁️ 4.88K · <a href="https://t.me/SBoxxx/18152" target="_blank">📅 15:35 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18151">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">به گزارش العربیه، آمریکا و ایران به توافق اولیه برای آزادسازی ۳ میلیارد دلار از دارایی‌های مسدود شده ایران دست یافتند.</div>
<div class="tg-footer">👁️ 4.88K · <a href="https://t.me/SBoxxx/18151" target="_blank">📅 15:30 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18150">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">#GRI  شاخص Geopolitical Risk Index برای امروز در حالت Clear قرار دارد و احتمالاً شاهد افزایش جریانات ریسک پذیری خواهیم بود.</div>
<div class="tg-footer">👁️ 4.92K · <a href="https://t.me/SBoxxx/18150" target="_blank">📅 15:25 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18149">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MrVKQeeZNlRJVEOQKfTXviJifUJErqZOeISCPdjE1RuTDSEjYJyj8se7EF21v7bUs3J8YHVlsg6iMH7GWYG5-Mj6OhH9pFKSyVfTYHZ09VZ871yLGDMNQAQMLAT0Mg91dxDU7TlZwcRnnfsoEDDctDLh5O31MHvDvsMJ7pZaG_KOdunXBNfVKPa6mYV5bQHHuL8YC3ioZcWJRqBjzo3s9ZaXrDhJlbyxKbabLNLlqYWkOuKWuJWh6HrL5ysPnSdilA6c8VS1TsEjisF02-8doTgHLbPyaZ_g6i0UU0T2u0vC_TI7JrSa8Lwra5Nb8dTIPovKfETjzn6_K2rCYAC_1Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رشد دارایی های ریسکی و افت بهای نفت!</div>
<div class="tg-footer">👁️ 4.99K · <a href="https://t.me/SBoxxx/18149" target="_blank">📅 14:55 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18148">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fEOdDC8MU_z5ZvA0FvXSLhD7mzDrOOvJhobgaSMqNc6AA3dfB0aM9sLRxlmuZeXIyRuGhBovu-zIW334wSXcLFk1Wfe2Ed2qJLA_kqOWXPRNol5vzywuHl_gq3YOHJca_2c_21DttSrsC6oo_uT-aAxX7cBK9NuxgZj_HMJOhPPDHKsGVKOfQAQj767aMuXxN_mODLDdkoCgu4g5IkU3v8Qwa3MDXWzoHL36LHG2GBhv7bhgt0YdD4eETQM13tqgkyBjkV2CxiE2IzORnZgfWrardXyorOq9-3hvPcrhiLWibCS0oYeSZ5PDKZq-XOaiRE3xEr67cqio2BzeTTSDAA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#GRI  شاخص Geopolitical Risk Index برای امروز در حالت Clear قرار دارد و احتمالاً شاهد افزایش جریانات ریسک پذیری خواهیم بود.</div>
<div class="tg-footer">👁️ 4.57K · <a href="https://t.me/SBoxxx/18148" target="_blank">📅 14:52 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18147">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">عراقچی در پاسخ به تهدید کاتز برای ترور رهبر جدید ایران:
شرایط تفاهم‌نامه اسلام‌آباد کاملاً واضح و برای همه قابل مشاهده است.
رئیس‌جمهور آمریکا متعهد شده است که حیوانات خانگی خود را در تل‌آویو ساکت نگه دارد. اگر آنها به ارباب خود توجه نکنند، ایران به آنها درس خواهد داد.
هر تهدیدی علیه مردم و رهبری ما پاسخ فوری و قدرتمندی دریافت خواهد کرد.</div>
<div class="tg-footer">👁️ 4.86K · <a href="https://t.me/SBoxxx/18147" target="_blank">📅 14:48 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18146">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/41c5e5e0c5.mp4?token=t7QSPSJd0_GKG_gxIjx9Cf1vnaapS63KkFZ_aT9srM06Vld2h4ud0TBcvhcJUXnv9LelH7zDwe_9USBwl1G2TX9UtW1htrLtkJHW2GvwSTe_RjFoZY8VmaNUnGa0M8PvQqC5MwiE-gE8CFBKxy3idiOpL-cOuCCDD--kdI00EdvblxJ1CW2eEwuMG3OmSnRc7o2GZArHnYgANFYjIKGBmvvVSfX8RsA6bBYZXQ0_j_lUx7DqOS6U3dEX_POHnZ_own6YDaU18X0QozUOeireHOOuF-YteRkH3sEuC44CuTPShZ9YDWtTwSLFog2eskrjIji8hrEWLUcrnVD78Q4WUQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/41c5e5e0c5.mp4?token=t7QSPSJd0_GKG_gxIjx9Cf1vnaapS63KkFZ_aT9srM06Vld2h4ud0TBcvhcJUXnv9LelH7zDwe_9USBwl1G2TX9UtW1htrLtkJHW2GvwSTe_RjFoZY8VmaNUnGa0M8PvQqC5MwiE-gE8CFBKxy3idiOpL-cOuCCDD--kdI00EdvblxJ1CW2eEwuMG3OmSnRc7o2GZArHnYgANFYjIKGBmvvVSfX8RsA6bBYZXQ0_j_lUx7DqOS6U3dEX_POHnZ_own6YDaU18X0QozUOeireHOOuF-YteRkH3sEuC44CuTPShZ9YDWtTwSLFog2eskrjIji8hrEWLUcrnVD78Q4WUQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ذخایر نفتی آمریکا و جنگ با ایران  آمریکا از ذخایر راهبردی نفت به‌عنوان ابزاری برای مدیریت شوک‌های بازار و کنترل فشار انرژی استفاده کرده و کاهش اخیر این ذخایر باعث شده بازسازی آن‌ها به یکی از اولویت‌های مهم واشنگتن تبدیل شود.  برخی تحلیلگران معتقدند کاهش تنش…</div>
<div class="tg-footer">👁️ 4.98K · <a href="https://t.me/SBoxxx/18146" target="_blank">📅 14:09 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18145">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">محبوبیت فردریش مرز  به پایین‌ترین میزان خود رسیده است!  بنا بر گزارش بیلد و با استناد به داده‌های مؤسسه تحقیقاتی INSA، حدود دو سوم آلمانی‌ها از عملکرد صدر اعظم فریدریش مرز ناراضی هستند.  این رسانه اضافه می‌کند که حدود ۷۰٪ از شهروندان آلمان از عملکرد دولت ناراضی‌اند.…</div>
<div class="tg-footer">👁️ 4.32K · <a href="https://t.me/SBoxxx/18145" target="_blank">📅 14:03 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18144">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">💳
اعتراض عضو فقهای شورای نگهبان به بازشدن اینترنت بین‌الملل
🔹
مدرسی یزدی
:
باز گذاشتن شبکهٔ جهانی اینترنت بدون ملاحظات کارشناسی دقیق از جانب متخصّصان متعهّد، به انواع بهانه‌هایی که نمی‌تواند جبران‌کنندهٔ آسیب‌های همراه آن باشد ـ از قبیل آنکه کسب مردم آسیب می‌بیند یا حقّ مردم است یا خلاف وعدهٔ انتخاباتی رئیس‌جمهور محترم است ـ کاری بسیار خطرناک است. این کار، اقتصاد کشور، امنیّت شغلی مردم، امنیّت داد‌و‌ستد‌های تجاری، امنیّت نهاد‌های مهمّ کشوری و امنیّت شخصیّت‌های مؤثّر نظام و سلامت روانی اقشار مختلف مردم به‌ویژه نوجوانان و جوانان را در تیررس دشمن آمریکایی صهیونی قرار می‌دهد</div>
<div class="tg-footer">👁️ 4.6K · <a href="https://t.me/SBoxxx/18144" target="_blank">📅 13:18 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18142">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UYVKspDONevEcKdI2cASm09tE6Psq3aqP4ZtPXAKbf-7hmUcXNY93HVlfLFYXg7Od_XOajcSOBbaVA2OY0icZyVC6fI7up2fyJbE5UeFQ6WJVPzdjKJItFQp9K8mDfl5H0xwksAFtcyLxFQvgJlpDPBeaazmLBON_fDRjseHqecBUrs_OZWdIY8__qbhrHnLaf6TCYCbGWeEVQc8zgISxPl3PjFoZcSugitRjbcT84m6ZLLHb8K3JByGOPKkltYy34vBH9oVzgbf0awRbV-QbaSiBceXFxg1InHx1Jc1yJftYH-yzOeieASerE4EplCq8DCpED4AnB2z9MUHoAVA3w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖌
از امروز اینجا پادکست های روزانه ژئوپولیتیک و بازارهای مالی ارائه خواهدشد.  یک شاخص ریسک ژئوپولیتیکی هم طراحی کرده ام که هر روز 2 بار در ساعت های 10 و 18 بروزرسانی می شود.</div>
<div class="tg-footer">👁️ 4.52K · <a href="https://t.me/SBoxxx/18142" target="_blank">📅 12:34 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18141">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">Audio</div>
  <div class="tg-doc-extra"></div>
</div>
<a href="https://t.me/SBoxxx/18141" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🖌
از امروز اینجا پادکست های روزانه ژئوپولیتیک و بازارهای مالی ارائه خواهدشد.  یک شاخص ریسک ژئوپولیتیکی هم طراحی کرده ام که هر روز 2 بار در ساعت های 10 و 18 بروزرسانی می شود.</div>
<div class="tg-footer">👁️ 4.63K · <a href="https://t.me/SBoxxx/18141" target="_blank">📅 11:22 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18140">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">Secret Box
pinned «
🖌
از امروز اینجا پادکست های روزانه ژئوپولیتیک و بازارهای مالی ارائه خواهدشد.  یک شاخص ریسک ژئوپولیتیکی هم طراحی کرده ام که هر روز 2 بار در ساعت های 10 و 18 بروزرسانی می شود.
»</div>
<div class="tg-footer"><a href="https://t.me/SBoxxx/18140" target="_blank">📅 11:15 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18139">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">🖌
از امروز اینجا پادکست های روزانه
ژئوپولیتیک و بازارهای مالی
ارائه خواهدشد.
یک
شاخص ریسک ژئوپولیتیکی
هم طراحی کرده ام که هر روز 2 بار در ساعت های 10 و 18 بروزرسانی می شود.</div>
<div class="tg-footer">👁️ 4.48K · <a href="https://t.me/SBoxxx/18139" target="_blank">📅 11:09 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18138">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VFIsBQ79AT9ewL5MTR-YJKrxmlzmexTpdXO9ZIb8bVWNvpPQfRk2oIOsmKYj_8DVm5CNdLg7YDHdSpkE1PqdWM5KtIOQuRbBW6gUnX-v3LakA6aeFDG9uCB6MHGUHySfKVp2Rvx_MJJVIpzv1q02hd-ipTx2FPTaofjWWYEXyWt5u-PMhCe0ebDOu2rfdFhKwAgHOCVhC4KwHuJ7PRsOyQGkH9HzDBFiT-EHRvaR2DgudtohBKQaErZ_DJFaNT22x39dxj-k3un5XBwtdRvEuhorUvLjijeHj9DVlNZ-NfWGRUe9kynOJudEfW2yEE1yLmsi3t_dbEYgUkrBoD4O7g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اظهارات جدید قاسمیان:   واشنگتن را اشغال کنید؛ ترامپ را دستگیر کنید و به ایران بیارید</div>
<div class="tg-footer">👁️ 4.64K · <a href="https://t.me/SBoxxx/18138" target="_blank">📅 10:53 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18137">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">اظهارات جدید قاسمیان:
واشنگتن را اشغال کنید؛ ترامپ را دستگیر کنید و به ایران بیارید</div>
<div class="tg-footer">👁️ 4.55K · <a href="https://t.me/SBoxxx/18137" target="_blank">📅 10:50 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18136">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cq-OGO7FrDjOmcHv29l_jH-9Q4WxGrfxyeATC4u__7aZ5EwAssOfwq6heX0gWXwC46TXtwmvPefquBOcsskODYM9Y2pReD1__6sz8yxfCpJDeqLcXWyll7xqw-loaoXdfw1EFS1nVQjqcpJCNQi8V_fzg590ZJFJWOB-uvSVgVzdUzjDauq7-WFW44X2f7rysv0AH3veGkJVmnxcp9rYARe5xX8j837-Co-bAdytDOtB8WbHQ6DkkSxOQzvN19HF2QyFIOz_bmXZLL8KMN03MKHQXwzji9-En7p62vQ1u3ENme7D7wSkGHZstWU6LxWr6u7D9pyRCxeI44rlEkUTFA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 4.51K · <a href="https://t.me/SBoxxx/18136" target="_blank">📅 10:15 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18135">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dicK4AMTc9tsUWG7UcuCr5mhPmlih3vshCdLNH1KstrbYfAUvxvqF6x6FZ0VAlASYWU7FFt6R8z29adGpc84lAk00-ZFwa54pkQXoLETKDXA1W_qDmOSPq15xtEpbKLBTuxwna1RGL3meGxmV9vaa2oG6Vj7s8HYHHPN_4l4nD4tsu_8Rz2yXBb6oiYtLA-LNYGb8q1jWesXtCxc0yy2qt2wlUoyjbfWhX0QvWvTJooxmd1Vlp6iR-XOirtT49tTlGjC5KoiZHh31yi9LH-N3Q-Yb7IXgaGlr8XqtJiVfi7yj5RGtOeLugsFvwYgZo_DsdElX3PcZW-nC35jwmqKSQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سنتکام اعلام کرد دو ناو آبی‌ـ‌خاکی آمریکا، باکسر و پورتلند، در حال حرکت به سمت خاورمیانه هستند.
این دو ناو معمولا برای انتقال نیرو و عملیات آبی خاکی و ... مورد استفاده قرار می‌گیرند.</div>
<div class="tg-footer">👁️ 4.88K · <a href="https://t.me/SBoxxx/18135" target="_blank">📅 10:15 · 10 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>

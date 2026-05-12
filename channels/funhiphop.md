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
<img src="https://cdn4.telesco.pe/file/np-bduLHKN5_kiTOnwkOrXEaVFdG9Tc8VsatPIrh9nkK_5zKCLz4tbog8paJtm12CKEaWo07itz6O7XiRzuWhbuX8GPFtUPYcacT2jv2SwpBCneTD6YdKwOtsih9df2CS2h3QW-InCP32Yo-p-Eu2j7Wloec4qAQ7LhduUcikhO9dI0AacWJYGaJRPdNT4WOkSW1HsidExZuhoz1XzSvQe4uuEpqefUnBYjuZhceMprEfWsM4_YDlpIzLqMVeT4ICvMtU_bq1k1IqsRZWtp02Z6dk3LwfVFCr0mOEyZhmoCvGHrbHy3UmdIvzPJj0a0RQC8iaMcwPShsx_-zZgJvKg.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 [ Fun HipHop ]</h1>
<p>@funhiphop • 👥 139K عضو</p>
<a href="https://t.me/funhiphop" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 «قدیمی ترین اجتماع فانِ هیپ هاپی»🟡Tb :@FunHipHopAdsContact :@Chaman_Dar_KhakFollowing Copyright Laws©</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-02-22 19:27:59</div>
<hr>

<div class="tg-post" id="msg-74704">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">سرورهامون با بالاترین سرعت و کیفیت ممکن هستند
💢
تعرفه هامون به صورت زیر هست
📥
1G- 250
⚡️
2G- 500
🌟
3G- 750
💎
5G- 1,200
👑
10G- 2,300
⚡️
20G- 4,500
👁
سرویس‌ها به‌صورت یک‌ماهه ارائه میشن و هیچ‌گونه محدودیت کاربری ندارن
👥
🤩
با خیال راحت روی چند دستگاه استفاده…</div>
<div class="tg-footer">👁️ 502 · <a href="https://t.me/funhiphop/74704" target="_blank">📅 19:07 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-74703">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromShyPxnGuin🐧</strong></div>
<div class="tg-text">سرورهامون با بالاترین سرعت و کیفیت ممکن هستند
💢
تعرفه هامون به صورت زیر هست
📥
1G- 250
⚡️
2G- 500
🌟
3G- 750
💎
5G- 1,200
👑
10G- 2,300
⚡️
20G- 4,500
👁
سرویس‌ها به‌صورت
یک‌ماهه
ارائه میشن و هیچ‌گونه
محدودیت کاربری
ندارن
👥
🤩
با خیال راحت روی چند دستگاه استفاده کنین و بدون دغدغه از کیفیت و سرعت لذت ببرین
🚀
حتما دقت کنید سرورها همراه با ساب و بدون ضریب هستند
👍
@PenGu_Sup
🐧
@PxnGuin
⚡️</div>
<div class="tg-footer">👁️ 563 · <a href="https://t.me/funhiphop/74703" target="_blank">📅 19:02 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-74702">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">اکسیوس:
ممکنه آمریکا بزودی به کوبا حمله کنه.
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 888 · <a href="https://t.me/funhiphop/74702" target="_blank">📅 18:48 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-74701">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">احتمالا هفته دیگ پیش خریدGTAVI به قیمت ۸۰ دلار رو کنسول ها میاد.    @FunHipHop | Taymaz</div>
<div class="tg-footer">👁️ 1.15K · <a href="https://t.me/funhiphop/74701" target="_blank">📅 18:22 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-74700">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">احتمالا هفته دیگ پیش خریدGTAVI به قیمت ۸۰ دلار رو کنسول ها میاد.
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 1.45K · <a href="https://t.me/funhiphop/74700" target="_blank">📅 18:09 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-74699">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">رویترز:
یک مقام پنتاگون می‌گوید جنگ با ایران تا این لحظه حدود ۲۹ میلیارد دلار برای ایالات متحده هزینه داشته است.
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 1.68K · <a href="https://t.me/funhiphop/74699" target="_blank">📅 17:49 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-74698">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hf-CLdA7IA4JqnOP1aiSlyXmEXp3cltPFJPkayXsorFjPzyrJHEhvuph1svgtw4PU1r6XOUplVcH07-dFozHohAyFKJJS3iOo1pn4fKFLn6ovkzA4bIbE4QZYA9TD46YcVD8HgZJ2S4Ip5HweJiDEJyVVJquTvEImUdSlj-YQU-zrjCIFE6eFWZTy-nPyufu5Gml8BzkaQAtR7xcnGQeu-awcY-3OaLIRqL6SGW5Ku2CIvJHRKFZwZFDWzZIspQxK-1a7_j2u22NN8Nfug-Lafx17F6VsLTMhltnHdaewSFQDnpopCN4oZlFlBwHg7skVeBzDASq0TEUNSQ2nwbkJg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وال استریت ژورنال بر خلاف چیزی که خیلی ها تصور میکنند! چین در مذاکرات جدید با امریکا کارت برتری نسبت به ترامپ نداره. اقتصاد چین با مشکل هایی چون رشد ضعیف, بیکاری جوانان, کاهش مصرف داخلی و بحران بدهی رو به رو هست. بخش بزرگی از اقتصاد چین بر پایه صادرات و عرضه…</div>
<div class="tg-footer">👁️ 1.74K · <a href="https://t.me/funhiphop/74698" target="_blank">📅 17:38 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-74697">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">ترامپ
ایران از نظر نظامی شکست خورده و
احتمالاً هنوز خودش هم این را نفهمیده است
.
اگر
نیویورک‌تایمز
را بخوانید، فکر می‌کنید ایران اوضاعش خیلی خوب است.
@FunHipHop
| NIC333</div>
<div class="tg-footer">👁️ 1.79K · <a href="https://t.me/funhiphop/74697" target="_blank">📅 17:28 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-74696">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">ترامپ
چین قدرتمند است،
اما ما از چین هم قوی‌تریم
. از نظر نظامی از هر کشور دیگری قدرتمندتریم.
این را در ونزوئلا دیدید. برای بیشتر کشورها آن عملیات خیلی سخت می‌بود، اما ما در یک روز انجامش دادیم و حالا
نتیجه‌اش
را ببینید.
به ایران هم نگاه کنید... آن‌ها همه‌چیزِ بزرگی داشتند،
اما حالا همه‌اش از بین رفته است.
@FunHipHop
| NIC333</div>
<div class="tg-footer">👁️ 1.8K · <a href="https://t.me/funhiphop/74696" target="_blank">📅 17:27 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-74695">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">ترامپ
ما صددرصد به آثار و بقایای هسته‌ای دست پیدا می‌کنیم؛ کل ماجرا را کامل به دست می‌آوریم.
@FunHipHop
| NIC333</div>
<div class="tg-footer">👁️ 1.71K · <a href="https://t.me/funhiphop/74695" target="_blank">📅 17:26 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-74694">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">ترامپ
ما قوی‌ترین ارتش دنیا را داریم.
الان هم این را می‌بینید؛ مثلاً درباره ونزوئلا. الان رابطه خیلی خوبی با ونزوئلا داریم. میزان محبوبیتم آنجا به ۹۹٪ رسیده، باور می‌کنید؟
حالا ایران هم تقریباً همین وضعیت را دارد؛ فقط کشور بزرگ‌تری است با ۹۵ میلیون جمعیت. راستش را بخواهید، ما همه‌چیز را نابود کردیم.
@FunHipHop
| NIC333</div>
<div class="tg-footer">👁️ 1.71K · <a href="https://t.me/funhiphop/74694" target="_blank">📅 17:25 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-74693">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">ترامپ
من رابطه خیلی خوبی با بی‌بی دارم. ما واقعاً مثل دو شریک واقعی کنار هم بودیم.
اگر ما دوتا نبودیم، اسرائیلی هم وجود نداشت؛ مخصوصاً بدون من قطعاً چنین چیزی ممکن نبود.
@FunHipHop
| NIC333</div>
<div class="tg-footer">👁️ 1.58K · <a href="https://t.me/funhiphop/74693" target="_blank">📅 17:24 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-74692">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">سید روزنبرگ
«آقای ترامپ، آیا واقعاً در
تهِ دلتون
باور دارید که می‌تونید جلوی غنی‌سازی اورانیوم ایران رو بگیرید تا
اصلاً و ابداً
دستشون به بمب نرسه؟»
ترامپ
«
شک نکنید، صد در صد!
اونا متوقف می‌شن. ایرانی‌ها خودشون به من گفتن که ما قراره به اون
"غبار هسته‌ای"
برسیم (ما مواد رو ازشون می‌گیریم).»
@FunHipHop
| NIC333</div>
<div class="tg-footer">👁️ 1.58K · <a href="https://t.me/funhiphop/74692" target="_blank">📅 17:23 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-74691">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5168dede5b.mp4?token=hnREdlmTm7WrPU4fJlALJUsp3yFld8iUC-bNsTVbjko6-emEuEUklWj1zFhVJJaCOd9YeI9tv0wL-sQV8jz1nXXKJGnihLILu-mog5KdoUx0BQIoM5YUJtsSiSgdTuH4cshiND8jAGF_F3WSI4wK9PEskNkvvhidZIyvsXtP5zcZpu1unYjA9pzauAXm41jb6TdEEp_FzKcu_WkFado-kwgYPxiJplv7nvAF_er1GV_Mtn5suNBeZDwphgnqZhE8erGD7A6Mso129uOeKAsTYozb0BawrCTIjXdNqDheCrKcccSZvrB3U4jkBQbLKQ22Utc1OH4XQGcaoI5zGkVukA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5168dede5b.mp4?token=hnREdlmTm7WrPU4fJlALJUsp3yFld8iUC-bNsTVbjko6-emEuEUklWj1zFhVJJaCOd9YeI9tv0wL-sQV8jz1nXXKJGnihLILu-mog5KdoUx0BQIoM5YUJtsSiSgdTuH4cshiND8jAGF_F3WSI4wK9PEskNkvvhidZIyvsXtP5zcZpu1unYjA9pzauAXm41jb6TdEEp_FzKcu_WkFado-kwgYPxiJplv7nvAF_er1GV_Mtn5suNBeZDwphgnqZhE8erGD7A6Mso129uOeKAsTYozb0BawrCTIjXdNqDheCrKcccSZvrB3U4jkBQbLKQ22Utc1OH4XQGcaoI5zGkVukA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پیت هگست:
قطعاً، ما در حال پیروز شدن هستیم.
و در تمام مراحل این نبرد پیروز شده‌ایم.
ایران بر اساس کاهش چشم‌گیر توانمندی‌هایش، این موضوع را به‌خوبی می‌داند؛ به همین دلیل است که شاهد تمایل آن‌ها برای نشستن پای میز مذاکره بودیم.
چگونگی حل‌وفصل این موضوع بر اساس
شرایط ما و شرایط پرزیدنت ترامپ خواهد بود.
ما تمام مهمات و توانمندی‌های لازم برای این کار را در اختیار داریم.
@FunHipHop
| NIC333</div>
<div class="tg-footer">👁️ 1.73K · <a href="https://t.me/funhiphop/74691" target="_blank">📅 17:09 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-74690">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1516ee5e2a.mp4?token=r4GmcKWdMFG9t166hyVVS54xYxAfQL6Dz5-LA2WTY4YZYR_4B9WNNTDPsuKxcSK04JuxsmHNwtSjhb4F37lefmAK4R29gRsUfILLm4ycjLPaAhzqYOUR5mwRzVC4Q7Qf_N6Y9IgrJej0ly_s8HAswYOsGM-JJSbulwxbQA0t6yuuAUAMudd-mZTK00Bi18gY4rkgFla4b2fWbtTtRdFC3HBi8AKc4VZtAvWdIuRsUamOtYz13JxFwPCL6zRsYI6wkg4fcrl1RlDKoVKyYAtSu3iNyZyNfWQOvimFgPQO3PstxTlmOYM1ekzyII73qSFboVO1ufI-sseK2asKG1t9hA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1516ee5e2a.mp4?token=r4GmcKWdMFG9t166hyVVS54xYxAfQL6Dz5-LA2WTY4YZYR_4B9WNNTDPsuKxcSK04JuxsmHNwtSjhb4F37lefmAK4R29gRsUfILLm4ycjLPaAhzqYOUR5mwRzVC4Q7Qf_N6Y9IgrJej0ly_s8HAswYOsGM-JJSbulwxbQA0t6yuuAUAMudd-mZTK00Bi18gY4rkgFla4b2fWbtTtRdFC3HBi8AKc4VZtAvWdIuRsUamOtYz13JxFwPCL6zRsYI6wkg4fcrl1RlDKoVKyYAtSu3iNyZyNfWQOvimFgPQO3PstxTlmOYM1ekzyII73qSFboVO1ufI-sseK2asKG1t9hA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خانم مک‌کالوم
«به عقیده من، "قانون اختیارات جنگی" باید فعال شود و موضوع به کنگره بیاید؛ هرچند نمی‌دانیم نتیجه چه خواهد بود. آیا شما
طرح جایگزینی (Plan B)
دارید؟»
پیت هگست
«عضو ارشد، باید بگویم که ما برای تمامی این سناریوها برنامه داریم. برنامه‌ای برای
تشدید عملیات
در صورت لزوم، برنامه‌ای برای
عقب‌نشینی تاکتیکی
در صورت نیاز و برنامه‌ای برای
جابه‌جایی تجهیزات و نیروها
. اما قطعاً در این نشست، با توجه به
حساسیت مأموریتی
که رئیس‌جمهور برای اطمینان از عدم دستیابی ایران به سلاح هسته‌ای بر عهده گرفته است، گام بعدی را فاش نخواهیم کرد.»
@FunHipHop
| NIC333</div>
<div class="tg-footer">👁️ 1.72K · <a href="https://t.me/funhiphop/74690" target="_blank">📅 17:04 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-74688">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">اگه اینترنت پرو برا کنترل فضای مجازیه و برا همه نیست با کدوم منطقی پیامکش برا بابا بزرگم اومده</div>
<div class="tg-footer">👁️ 2.12K · <a href="https://t.me/funhiphop/74688" target="_blank">📅 16:35 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-74687">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">قطعی اینترنت قطعا بخاطر مسائل امنیتی نیست، قطعا بخاطرجلوگیری از ارتباط اجنت موساد با خارج از کشور نیست، قطعا بخاطر نفرستادن محتوا به اینترنشنال نیست
فقط یک دلیل داره اونم رانت و سود کلان برای دولته، سودی که اپراتورهای موبایل و دیتاسنترهای بزرگ مثل آروان‌کلود در این ۱۰ هفته بدست اوردن برابری میکنه با بودجه کامل چندین ساله مملکت پس به عبارتی حالا‌حالا‌ها قرار نیست وضعیت اینترنت برگرده به شرایط عادی و شاید هم هیچوقت برنگرده
دلایل مختلفی داره از جمله اینکه یواش‌یواش و در خفای کامل پیامک اینترنت‌پرو به حجم عظیمی از مردم ارسال شده و ملت درمانده مجبور به خرید اینترنت‌پرو و یا خرید سرویس‌های VPN به قیمت بالا شدن، به عبارتی مردم دارن خودشونو با این وضعیت وفق میدن و فعلا خبری از اینترنت بین‌المللی برای عموم مردم نیست
@FunHipHop
| ALI</div>
<div class="tg-footer">👁️ 2.21K · <a href="https://t.me/funhiphop/74687" target="_blank">📅 16:33 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-74686">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">با ۳۰ میلیون تومان موجودی، برای سه ماه آینده باید ۴۰۰ میلیون چک و بدهی پاس کنم و نمیدونم چه کنم
این یکی از برکات پیروزی های ج.ا در جنگ مقابل حمله بشردوستانه آمریکاست، به مشکی مادرخراب و شاه تحلیلگران مرادویسی برسونید اینارو با واقعیت دل جامعه رو به رو شن</div>
<div class="tg-footer">👁️ 2.37K · <a href="https://t.me/funhiphop/74686" target="_blank">📅 16:12 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-74685">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">دوستان به یامال خرده نگیرید یارو تو ناف اروپا بزرگ شده و تنها ایدش از اسلام وجود الله و روزه گرفتن و نماز خوندنه</div>
<div class="tg-footer">👁️ 2.4K · <a href="https://t.me/funhiphop/74685" target="_blank">📅 16:08 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-74684">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">در لفافه اینو میگم:
دین محترم اسلام به بهترین شکل در حال اجرا شدنه.
@FunHipHop
| Constantine</div>
<div class="tg-footer">👁️ 2.46K · <a href="https://t.me/funhiphop/74684" target="_blank">📅 16:06 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-74683">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Swz8ms6V3ZniMwjnwAGQSfAB4DyF652d8heQ6W2mn8t6P9Z3g4ai78HTBlTAmsBa3oFhGmo5KKZv_bB-I3GsXCscGvQrbdz7q49JC9DFW8uBlae1QejJfL2oPquGTxL2lxXvVaMFtg4ePSMMe114Mpfx9UgJrfKxGpTafunpG5_zDlkdzZ6VGuTcey9gwcjj9o6XKXYQpeo0zhc9_C0aCiFbcm8tnyV_2rUM7N5cxRcT4ESqvaJ546xb9yPbGjFHeSt0X5hVAgwhirw01sd5A_upkt_lbAbpOWX07sc-d4NUvXIGKcoXhX6pbMAzhojmXU5_gamATpkSPvKM-Y4ftQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تقریباً توی این ۲۰ سال و اندی زندگی اندکی که داشتم، هیچ موجود زنده ای رو ندیدم که آرزوی مرگ کنه واسه نوزاد کسی.
@FunHipHop
| Constantine</div>
<div class="tg-footer">👁️ 2.64K · <a href="https://t.me/funhiphop/74683" target="_blank">📅 15:56 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-74681">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/YbN8mVQIUFdIae57itOIP8i8Chs9-WfBy15cKgIi6f1RnIyiBM9t_xDiKOpRqDmsvmvae1FmkfTFexqpuHpYBXr3MUG2Iu4gG-lJHllvdo6qXsHrbFKOpm1gljFKQTEs84lqyVsQbaXHGaoRdqUCc-zQeYLQkawPW_JAyTRH0YlrPm-TOPwgKRzurWhxn7-oWoloJjcRBrSg8CNqPTDjVcl7I1Xnt_ob0JGKbtNVOR0Z-Kw2zpzY1dHPPcirWOFfy2gW8C4YbHk_zr2F9IFlN7HQALjY0eAkQ4dl8s760Qmud0esvKl5Lj0lTu_EJS4-e2JkNLGD-Fex0MSZqjZS0Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/E-sd9e3OWujj6dgt9IWQRvkmDjmxtsSfdrQs0IMabfbUKPhRFfydO-GsVSMQ6xwkqyEiEVY--NJbRsS6w6CLsfFAYdm5G01Tbfm4a6vNKty40RrRSqt7Zgm4ynDvZ5WTqfi-xHAMqNUGyE1lWykIUW25oXluZrSrOiu0NEKLfJfEZ5PoO6Fcac12OhG0t6rAH15Xj9PsyqFzIkTEj20LX1xS2S7bPngC8hl1uOAArE-GVQceyCQUH33c1QPh2pGWhpiy0pC2ug4mxijvsD5nQq7APRxvdbxxibcGGZum6psjpmBqFQ020M1WNa4Lbw0-v3OKumS_3noifP_iO0miuQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">توییت های جدید ترامپ
بای بای قایق های سریع
دموکرات ها عاشق
فاضلاب
هستند.
@FunHipHop
| NIC333</div>
<div class="tg-footer">👁️ 2.61K · <a href="https://t.me/funhiphop/74681" target="_blank">📅 15:40 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-74680">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">😠
ترامپ
کوبا درخواست کمک کرده و قرار است با آن‌ها گفت‌وگو کنیم.
@FunHipHop
| NIC333</div>
<div class="tg-footer">👁️ 2.54K · <a href="https://t.me/funhiphop/74680" target="_blank">📅 15:38 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-74679">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">کشف خط لوله قاچاق سوخت تو بندرعباس
دریابانی بندرعباس یه
خط لوله ۶ کیلومتری قاچاق سوخت
رو پیدا و منهدم کرده؛
خطی که قاچاقچی‌ها زیر ماسه‌ها و بستر دریا قایمش کرده بودن.
ظاهراً سوخت از ساحل مستقیم با این خط لوله به شناورهای داخل دریا منتقل می‌شده و ماجرا خیلی فراتر از قاچاق‌های ساده بوده.
این کشف دوباره نشون میده قاچاق سوخت تو بعضی مناطق جنوب کشور داره به شکل حرفه‌ای‌تر و سازمان‌یافته‌تری انجام میشه.
@FunHipHop
| NIC333</div>
<div class="tg-footer">👁️ 2.7K · <a href="https://t.me/funhiphop/74679" target="_blank">📅 15:24 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-74678">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uzgNQ63QP8c8i8sSFzhxmkiVGTbuJlGC1iLq9CUDkf-biOOar6IP57_cwPrWeJv-TVSTVTUFOqJ9vfn9NvyuPRNB1eSH18CuKSwY3lPKsg28aaEQH1Pl2g-u67B_6V1ggjwixzhnCFAJIsqCAir7iO93DE_ei-zqbrmrRQbX082WmfDkVPu26G03OMEx43kHvezPG5_xhRaDF0n_Ps17pmBBr_LgqE9a5bMVOp77pHu39p4P7iCopTxbSLTkhG-1ibOno8B3ja9Qu_GtoMgA24YjktWV9t_5MNvh6oCLXSadr85ul8EmPh0N0VvSvxBtwYpLG95AVHpDHMUSQZZkBQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فارکس سیتی پرو
فشار نفت و هرمز روی بورس هند
بورس هند این روزها زیر فشار نگرانی‌های نفت، تنش‌های هرمز و فضای ریسک‌گریز بازار قرار گرفته و معامله‌گرها محتاط‌تر شدن.
صحبت‌های اخیر دولت هند هم
کمکی به آرامش بازار نکرده
و فشار فروش رو تو بعضی بخش‌ها بیشتر کرده.
هند یکی از بزرگ‌ترین واردکننده‌های نفت دنیاست و هر تنش در تنگه هرمز می‌تونه مستقیم روی اقتصاد و بازار مالی این کشور اثر بذاره.
از طرفی چون هند جامعه بزرگی از کاربران
کریپتو
داره،
کاهش
ریسک‌پذیری
تو این بازار می‌تونه روی فضای کریپتو هم تاثیر
منفی
داشته باشه.
@FunHipHop
| NIC333</div>
<div class="tg-footer">👁️ 2.89K · <a href="https://t.me/funhiphop/74678" target="_blank">📅 15:08 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-74676">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">ویو ها یکم بیشتر شده
سوراخ جدیدی باز شده؟
@FunHipHop
| Menot</div>
<div class="tg-footer">👁️ 2.94K · <a href="https://t.me/funhiphop/74676" target="_blank">📅 14:55 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-74675">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">وزیر اقتصاد
شصت همت (هزار میلیارد تومان) برا خسارت جنگ کنار گذاشتیم عشقا, اصلا نگران نباشید.
@FunHipHop
| NIC333</div>
<div class="tg-footer">👁️ 3.3K · <a href="https://t.me/funhiphop/74675" target="_blank">📅 13:57 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-74674">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">سیناب خبر از برنامه های جدید خودشو پیشرو و تیمش میده، یه دزدی دیگه تو راهه فکر کنم
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 3.45K · <a href="https://t.me/funhiphop/74674" target="_blank">📅 13:45 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-74673">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">توهم
بزرگترین عامل سقوط است.
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 3.52K · <a href="https://t.me/funhiphop/74673" target="_blank">📅 13:36 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-74672">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">وال استریت ژورنال
بر خلاف چیزی که خیلی ها تصور میکنند!
چین در مذاکرات جدید با امریکا کارت برتری نسبت به ترامپ
نداره
.
اقتصاد چین با مشکل هایی چون ر
شد ضعیف, بیکاری جوانان, کاهش مصرف داخلی و بحران بدهی
رو به رو هست.
بخش بزرگی از اقتصاد چین بر پایه
صادرات و عرضه زیاد
بنا شده, از
خودرو
و
فولاد
گرفته تا
پنل های خورشیدی
و اگه آمریکا و متحداش تعرفه های سنگین تری اعمال کنن میتونن مستقیم به روی
کارخانه ها
و
صادرات
و
جریان نقدینگی
چین اثر منفی بزارن.
از طرف دیگه ترامپ ابزار هایی مثل
تعرفه جدید
,
تحریم بانک های چینی
و
محدود کردن دسترسی چین به سیستم مالی غرب
و کاملا در اختیار داره.
حتی برخی تحلیل ها میگن که واشنگتن ممکن هست که از پکن بخواد حمایت اقتصادی خودشو از
ایران
و
روسیه
کاهش بده و محدود تر کنه.
@FunHipHop
| NIC333</div>
<div class="tg-footer">👁️ 3.78K · <a href="https://t.me/funhiphop/74672" target="_blank">📅 12:56 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-74671">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/G9b9FZzTlx-d6sbov6ghBFyr4uFO1KUyhz8vh6OJbrCCBb-kTnH0ZzuXXx2qrSV_XWEGZcUyfraRi-x1k_9cBGn53l-8Eae3ZW1Aj8lnQHlf5KTcmWLzmUJVYlM886IPq0YwYmWsLfsRT8tTtDweg8Tq_kKeZubymWzq8IFGXVJ46dPC9ufPFABgjcLwkNExJ341ut1CtE48e82vbZf8YCAp5Wrsgeal5In3_PfRhOqh-kRNICRiPrMtffgQdX4NrOg7ks_4t0lTJ9w_JeP0kyUbg2LK6HnzND8j1cAdRm9lBM7h4HLpZhbLhXmqjQheiSCeeltCJwTGSeAYJr_kcg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">منتظر بمب اتم باشید
ابراهیم رضایی عضو کمیسیون امنیت ملی مجلس: اگه حمله کنید اتم درست میکنیم
@FunHipHop
| ALI</div>
<div class="tg-footer">👁️ 3.7K · <a href="https://t.me/funhiphop/74671" target="_blank">📅 12:45 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-74670">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4814fa6eb9.mp4?token=MJxU34BXgxr8wC-KiPsHudcQcayURLmCO7EV7FrNLRefOv0DboFi8EXyd2iYJnnNUp9YX8HywuvQiUMcaByryyPoqkJmwlLku3nsKIz--CKBwlF88UVex7a_s6P5CLZUVVWO_gvSM7QgA0eeZYknwxgbwo2Hpzy_yxzyWy8gZMV06o81o78-3KHWgPNqYqvny6U1yjCxqs5h07KnI4afSYF3c1q2WWxtwzT4n662kbEXc94NOJVuBQK5nJ9JjpJI2F0rM3kceKipaCUeDoVE5z9ZinQfqP3x0IhFUF5ApjCXLAys-jPGa3OI012gVYXB7A4QGHXzqN6QkBGdUjPFSQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4814fa6eb9.mp4?token=MJxU34BXgxr8wC-KiPsHudcQcayURLmCO7EV7FrNLRefOv0DboFi8EXyd2iYJnnNUp9YX8HywuvQiUMcaByryyPoqkJmwlLku3nsKIz--CKBwlF88UVex7a_s6P5CLZUVVWO_gvSM7QgA0eeZYknwxgbwo2Hpzy_yxzyWy8gZMV06o81o78-3KHWgPNqYqvny6U1yjCxqs5h07KnI4afSYF3c1q2WWxtwzT4n662kbEXc94NOJVuBQK5nJ9JjpJI2F0rM3kceKipaCUeDoVE5z9ZinQfqP3x0IhFUF5ApjCXLAys-jPGa3OI012gVYXB7A4QGHXzqN6QkBGdUjPFSQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">رسانه‌های عبری از شناسایی نخستین مورد ابتلا به ویروس نادر «هانتا» در تل‌آویو خبر دادند
@FunHipHop
| ALI</div>
<div class="tg-footer">👁️ 3.75K · <a href="https://t.me/funhiphop/74670" target="_blank">📅 12:37 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-74669">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">یک خبر بسیار جدید و غیر منتظره: امروز در جریان شهادت نتانیاهو در دادگاه، نتانیاهو یک پاکت محرمانه دریافت کرد و پس از خواندن آن گفت: «باید فورا بروم. باید»  @FunHipHop | Nima</div>
<div class="tg-footer">👁️ 3.85K · <a href="https://t.me/funhiphop/74669" target="_blank">📅 12:15 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-74668">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">"نتانیاهو به علت دریافت یک پاکت فوق محرمانه جلسه دادگاه خود را ترک کرد"  ناموسا وکیل اینو پیدا کنید، ۱۰ ساله داره دادگاهی که میدونه توش محکوم میشه رو میپیچونه هیچ کاریشم نمیشه کرد  @FunHipHop | چمن در خاک</div>
<div class="tg-footer">👁️ 3.87K · <a href="https://t.me/funhiphop/74668" target="_blank">📅 12:09 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-74667">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">ری اکشنا چرا رفته بالا</div>
<div class="tg-footer">👁️ 3.94K · <a href="https://t.me/funhiphop/74667" target="_blank">📅 11:34 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-74665">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Fg6lMV9zryEkiARo4zrsD_5LnEd_Z6kNbYYBsncegJfhPeSB_FDz9DKPLvFEAuXTY4V_oF8kWDnJorOyQCSBATaU58zhm06t2J7Lkqxl1IBMqMiRP9yyBPPXcC8D-oHdUdgIPvpg4YXeJ1lWlBD1M0BueNiCJNo1hr9rvnIJOQenPFx41JGuimokSjmxcBF08WsHPOE6kvP9x6nSfDCfMd4kobbDqY5OoeUIr2rx6vtEbovACLRp-agvBiaVKWkX20zwWfna7fVpi_lNC0_H9BUXf495lIouHsO6f_Cucr8fVyPvtC4w9dctQmJoZm8HfMUIVxJcOOmLfrIiuMRIAA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پیامی که روی بسیاری از تلفن‌های اسرائیلی دریافت شده:
جمهوری اسلامی ایران شما را به همکاری در زمینه اطلاعات دعوت می‌کند.
برای همکاری، با سفارت‌های ایران در کشورهای مختلف یا یکی از اپراتورهای سایبری ایرانی به صورت آنلاین تماس بگیرید. هم‌اکنون ساختن آینده خود را آغاز کنید.
@FunHipHop
| ALI</div>
<div class="tg-footer">👁️ 4.5K · <a href="https://t.me/funhiphop/74665" target="_blank">📅 11:07 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-74664">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">نرخ تن فروشی پسر چنده دوستان
@FunHipHop
| Menot</div>
<div class="tg-footer">👁️ 4.46K · <a href="https://t.me/funhiphop/74664" target="_blank">📅 10:16 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-74663">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">ترامپ کونی اتم بزن ما از شر این دندون درد راحت شیم</div>
<div class="tg-footer">👁️ 4.98K · <a href="https://t.me/funhiphop/74663" target="_blank">📅 06:00 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-74662">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">(محض اطلاعت به عنوان یه دختر همین الانم زیاد از مغزم استفاده کردم بس.)</div>
<div class="tg-footer">👁️ 5.32K · <a href="https://t.me/funhiphop/74662" target="_blank">📅 03:38 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-74660">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">واللا اسرائیل آمریکا هفته گذشته به حمله دوباره علیه ایران نزدیک شده بود، اما اطرافیان ترامپ از او خواستند قبل از هر اقدام نظامی، آخرین فرصت به مذاکرات داده شود و به همین دلیل تصمیم به تعویق افتاد. همزمان فرماندهان ارشد ارتش اسرائیل در جلسات داخلی تأکید کرده‌اند…</div>
<div class="tg-footer">👁️ 5.49K · <a href="https://t.me/funhiphop/74660" target="_blank">📅 02:01 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-74659">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">واللا اسرائیل
آمریکا هفته گذشته به حمله دوباره علیه ایران نزدیک شده بود، اما اطرافیان ترامپ از او خواستند قبل از هر اقدام نظامی، آخرین فرصت به مذاکرات داده شود و به همین دلیل تصمیم به تعویق افتاد.
همزمان فرماندهان ارشد ارتش اسرائیل در جلسات داخلی تأکید کرده‌اند که دولت اسرائیل باید حمله به زیرساخت‌های مهم ایران را به‌صورت جدی بررسی کند.
@FunHipHop
| NIC333</div>
<div class="tg-footer">👁️ 5.24K · <a href="https://t.me/funhiphop/74659" target="_blank">📅 02:00 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-74658">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">عراق:
ما تأیید و تأکید می‌کنیم که در حال حاضر هیچ نیرو یا پایگاه غیرمجازی در خاک عراق وجود ندارد.
@FunHipHop
| ALI</div>
<div class="tg-footer">👁️ 5.01K · <a href="https://t.me/funhiphop/74658" target="_blank">📅 01:42 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-74657">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">نزنید آقا نزنید
اف کندی، وزیر بهداشت ایالات متحده:
پسران نوجوان امروزی تنها نصف مردان در سال ۱۹۷۰ اسپرم دارند.
@FunHipHop
| ALI</div>
<div class="tg-footer">👁️ 4.97K · <a href="https://t.me/funhiphop/74657" target="_blank">📅 01:41 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-74656">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">دبیرکل سازمان ملل:
جنگ باید سریعاً تموم شه.
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 5K · <a href="https://t.me/funhiphop/74656" target="_blank">📅 00:33 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-74655">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">ناموسا این آدم الان عادیه؟  @FunHipHop | چمن در خاک</div>
<div class="tg-footer">👁️ 4.95K · <a href="https://t.me/funhiphop/74655" target="_blank">📅 00:16 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-74654">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sNsrnPJUcmXfWsBfTfN_ntbS4506eYV_MY1QB-5-pMouHobSSMEvA_O13tNRLVtjcG8U05H_ZfraZveNbVKlPD4SznTTLeIX1xuwLTXWl6wYKfBdlFWycKb5DhKoNxlRwAIwYd83fkTKrZFcJjKIFwMCIrGnuiTgqSw7-RKP9VpaR6SU13leND8wwGTpyHnpMsGe9wsotNn0Tax7JDhSfdNCHsIQC00ks30qALiatIkDDTGNP3EwCyPcm4z4EWUfYwdygZneHghVWNynSksm6w84aTliltITBBRygfWbbv_osV60oX9rpMhOm0eDkF71n_0TVuIsaAZOReGxkRebjQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ناموسا این آدم الان عادیه؟
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 4.8K · <a href="https://t.me/funhiphop/74654" target="_blank">📅 00:08 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-74653">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">دو مقام ارشد آمریکایی به فاکس نیوز:
ترامپ به از سرگیری جنگ با ایران متمایل شده.
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 4.23K · <a href="https://t.me/funhiphop/74653" target="_blank">📅 00:00 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-74652">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">کیر وه کوص دالگ سلبریتی هایی که پرچم کشوری جز کشور خودشون رو دستشون میگیرن برای عرض خایه مالی
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 4.27K · <a href="https://t.me/funhiphop/74652" target="_blank">📅 23:59 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-74651">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">🔥
خبر خوب برای همراهان SU vpn
🔥
به خاطر حمایت شما و برای رقابتی‌تر شدن سرویس‌ها، قیمت پلن‌های VPN کاهش پیدا کرد
✅
💰
تعرفه‌های جدید:
🔹
هر گیگ ۳۵۰
👈
۳۰۰ تومان
🔹
پلن ۱۰ گیگ ۳۰۰
👈
۲۵۰ تومان
🔹
پلن‌های ۲۰ گیگ به بالا ۳۵۰
👈
۲۲۰ تومان (هر گیگ)
⚡️
اینترنت پرسرعت
⚡️
مناسب…</div>
<div class="tg-footer">👁️ 4.34K · <a href="https://t.me/funhiphop/74651" target="_blank">📅 23:49 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-74650">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WtxgTDhDrI3-W4zFuI2kaoKdkJkx50BJyhq_5uLKQzBQH6R6G0H0EU9KUp_XS7SygS11QSIufNQ56AcaLc-VaWneGKfTLRxXZscg81IAKlBBNo5-5RVJ9jrnHQDN7lvEOh9ptmurVpqKNdGVDJTg1OIXA7-qHdusnDqu1ftnx2CRa0bAzH4tNWS5Lu5BVHj9gTeYFbYjWAIN8x3bMxm_JcqDieyvnKQhjJr0UJALN34RE3wHVxDDxHa8SMvB4mYXPClfWJ7yRFGzrZpL4c3_fFiDF8vkBrlCOSVEGjLQTd8JMVmAnEHxdtZEL5GHzFgM2Ay37uBxnxpWhZUzikDWLw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رای قلعه نویی برای توپ طلا مشخص شد  @FunHipHop | Taymaz</div>
<div class="tg-footer">👁️ 4.1K · <a href="https://t.me/funhiphop/74650" target="_blank">📅 23:17 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-74649">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/A_ViggUc5CM3LC0Uxt1apfoTSq4p4DR84BXVBx2R1j5Q84i32_80migqQ7ZbPBt1yAh0l_2di8J9gvuEIBwYQFoSi4wInDtcXSPjMNfpv7fQQKnUFevGKlev38yi8KnBifQJ4kHSox9r49FNJxie1A9HucBDMvzxqldbfFWQdR98rwW6VdjtF59oGOx7cQxz3XtcxFTurth-jcBzDTsuY22P7LgfKyjVYz--CBB_dZdwU71vUzscthSjaBwwrFFG972FtdJNeU8s1F_c_sXZ53k41ww7bAW_Zb8zsnSlwTx_Za0fPL8kKaOqZIP4hmIm724l7oBVlDyLrQLZlPp3oQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رای قلعه نویی برای توپ طلا مشخص شد
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 4.18K · <a href="https://t.me/funhiphop/74649" target="_blank">📅 23:07 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-74647">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CMRZj1CkMueUZsLPMOefaHU0uazmW0mHT92ZyEAE_iEViHzjD1df1mtQdP-6VxNZwRwOm0OpAU4ySOS8cg_JouLKRbuXSDOeHYW99PpLwY9r4OvVbUucG2q2cXjT7cRii5pubcc-59nYyufzZPwS0FwUiOHCMHhxt2242kI1rm2MjPkncAeqQc4sT8n99cfligjt0pI9eRQOTzK0wZAen4wmXDlQJk6-tjtxF_GGKmeiN2-oaDs9--pceC8RCKdkvFjp7AZRb1_MuTn3A9pEE954VRuCmFvqp8u19lojqN8xcZh3GjzqtcLxRrVAppdlBElDD5YolIMN68sVYRVmag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دکتر قالیباف:
نیروهای مسلح ما آماده‌اند تا پاسخی شایسته به هرگونه تجاوز بدهند؛
استراتژی اشتباه و تصمیمات نادرست همیشه به نتایج اشتباه منجر می‌شوند— کل جهان این را فهمیده است.
ما برای همه گزینه‌ها آماده‌ایم؛ آنها شگفت‌زده خواهند شد.
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 3.96K · <a href="https://t.me/funhiphop/74647" target="_blank">📅 21:58 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-74646">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">منابع نیمه‌معتبر عبری فان‌هیپ‌هاپ:
اکنون گفتگوهایی با آمریکا درباره از سرگیری جنگ با ایران در جریان است.
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 3.77K · <a href="https://t.me/funhiphop/74646" target="_blank">📅 21:50 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-74645">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">واشنگتن پست:
نیروی دریایی ایالات متحده تأیید کرد که یک
زیردریایی موشک بالستیک کلاس اوهایو مسلح به سلاح هسته‌ای در جبل‌الطارق پهلو گرفته است
.
افشای علنی غیرمعمول یکی از محرمانه‌ترین دارایی‌های آمریکا.
این اعلامیه چند ساعت پس از آن منتشر شد که ترامپ پیشنهاد آتش‌بس جدید ایران را «کاملاً غیرقابل قبول» خواند.
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 3.94K · <a href="https://t.me/funhiphop/74645" target="_blank">📅 21:16 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-74643">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e348238b19.mp4?token=o1xmmZmZuRxsxU0mafpexbJb-76R1CRJeyPwxx-gFxC_0__mD64fkjeQVerMF-XFAiXvtYTkmkZaL7i-Q6v1J-1tQm_Z6zMKIwggUBZYBX4CzIoLPtxVgRLO5PXiYOlTX3g3iIL3pmkGEoQkX5CkVO1qg3gPz1YDelujDoNjkzv82dPpphisSLQweJaNaJdPZb-VxNP8CLZBatPgraSBromZzhguVWzocC-96WQNUe1DSnkmGIZMeOmnbxwhZSI_bt_fmMlk5i_yfgMTwnOLwwpRTXhEtuBEO_pQm5Q7IiPx2iMuAZGbr1s4LiO6Je2aSI-c0UrRbXmct1fzqfPIjQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e348238b19.mp4?token=o1xmmZmZuRxsxU0mafpexbJb-76R1CRJeyPwxx-gFxC_0__mD64fkjeQVerMF-XFAiXvtYTkmkZaL7i-Q6v1J-1tQm_Z6zMKIwggUBZYBX4CzIoLPtxVgRLO5PXiYOlTX3g3iIL3pmkGEoQkX5CkVO1qg3gPz1YDelujDoNjkzv82dPpphisSLQweJaNaJdPZb-VxNP8CLZBatPgraSBromZzhguVWzocC-96WQNUe1DSnkmGIZMeOmnbxwhZSI_bt_fmMlk5i_yfgMTwnOLwwpRTXhEtuBEO_pQm5Q7IiPx2iMuAZGbr1s4LiO6Je2aSI-c0UrRbXmct1fzqfPIjQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ:
من این هفته قراره رودررو با رئیس‌جمهور چین درباره ایران حرف بزنم.
ایران کشور خیلی قشنگیه، ولی یه سری آدم‌ها اون رو اداره می‌کنن که شاید اصلاً نباید اونجا باشن.
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 3.9K · <a href="https://t.me/funhiphop/74643" target="_blank">📅 20:49 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-74642">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">اینجوری که ترامپ داره از هانتاویروس حرف میزنه شک ندارم سازندش خودشه
@FunHipHop
| ALI</div>
<div class="tg-footer">👁️ 3.61K · <a href="https://t.me/funhiphop/74642" target="_blank">📅 20:38 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-74641">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">ترامپ: من زیاد صحبت نمی‌کنم چون گروهی بزرگ از ژنرال‌های نظامی منتظر من هستند و این (جلسه) مهمه و مربوط به کشور بسیار دوست‌داشتنی ایرانه.
🥰
🥰
🥰
@FunHipHop | Nima</div>
<div class="tg-footer">👁️ 3.69K · <a href="https://t.me/funhiphop/74641" target="_blank">📅 20:28 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-74640">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">ترامپ: من زیاد صحبت نمی‌کنم چون گروهی بزرگ از ژنرال‌های نظامی منتظر من هستند و این (جلسه) مهمه و مربوط به کشور بسیار دوست‌داشتنی ایرانه.
🥰
🥰
🥰
@FunHipHop | Nima</div>
<div class="tg-footer">👁️ 3.25K · <a href="https://t.me/funhiphop/74640" target="_blank">📅 20:20 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-74639">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9c40e0494d.mp4?token=mkR3WUKFuoZdPcl87tE9qxX49S-bxWGuVWqeO81hAah90abvSsNOANPlLBEWfDSawtWxY_s77kKEcgGSTxjYXJmClLLtiP2d6hL6nGYj0qDe5jX7vi4gxxR-Cgf3C8Vf8Ddw81_B8O-jOHA805vevsIH_8bnwzsWK077Ba9gheB8i65keyHC0Xj2kI56p-zhRsZTp8z2ojFdRyHVQP0raNdH0vzmAgwS9EszDpAoBP38Sp6gV00ro_BUV8Sp_xsd7Vw04kF8l28Fb7qFOOuA0q1WLPAQJH1yGkTZSw0LG6E_0s_JzTufFGxX7UeNew0lpKoESIEB6kqpoacr2Rk80g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9c40e0494d.mp4?token=mkR3WUKFuoZdPcl87tE9qxX49S-bxWGuVWqeO81hAah90abvSsNOANPlLBEWfDSawtWxY_s77kKEcgGSTxjYXJmClLLtiP2d6hL6nGYj0qDe5jX7vi4gxxR-Cgf3C8Vf8Ddw81_B8O-jOHA805vevsIH_8bnwzsWK077Ba9gheB8i65keyHC0Xj2kI56p-zhRsZTp8z2ojFdRyHVQP0raNdH0vzmAgwS9EszDpAoBP38Sp6gV00ro_BUV8Sp_xsd7Vw04kF8l28Fb7qFOOuA0q1WLPAQJH1yGkTZSw0LG6E_0s_JzTufFGxX7UeNew0lpKoESIEB6kqpoacr2Rk80g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خبرنگار:
آقای رئیس‌جمهور، آیا در حال حاضر آتش‌بس برقرار است؟
ترامپ:
باید بگویم که وضعیت آتش‌بس فوق‌العاده ضعیف است.
من آن را در ضعیف‌ترین حالت می‌دانم. همین الان بعد از خواندن آن تکه زباله‌ای که برای ما فرستادند... حتی تمامش نکردم. گفتم وقتم را برای خواندنش تلف نمی‌کنم.
می‌توانم بگویم که در حال حاضر، این آتش‌بس با دستگاه زنده‌ مانده است.
زنده نگه داشتن با دستگاه زیاد هم چیز خوبی نیست، موافقی؟ عواقب بدی دارد.
من می‌گویم این آتش‌بس در وضعیت وخیمی قرار دارد که پزشک وارد اتاق می‌شود و می‌گوید: قربان، عزیز شما تقریباً ۱٪ شانس زنده‌ ماندن دارد.
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 3.37K · <a href="https://t.me/funhiphop/74639" target="_blank">📅 20:19 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-74638">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">یک منبع به شدت آگاه و نزدیک به تیم مذاکرات به تسنیم: برخلاف ادعای برخی رسانه‌های غربی، در متن ایران چیزی به عنوان پذیرش خروج مواد غنی شده هسته‌ای از کشور، وجود ندارد. ﻿ @FunHipHop | Nima</div>
<div class="tg-footer">👁️ 2.97K · <a href="https://t.me/funhiphop/74638" target="_blank">📅 20:03 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-74637">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">یک منبع به شدت آگاه و نزدیک به تیم مذاکرات به تسنیم:
برخلاف ادعای برخی رسانه‌های غربی، در متن ایران چیزی به عنوان پذیرش خروج مواد غنی شده هسته‌ای از کشور، وجود ندارد.
﻿
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 3.07K · <a href="https://t.me/funhiphop/74637" target="_blank">📅 19:57 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-74636">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c368c47031.mp4?token=RYqWSJ8RhbuKRm-KAQ3RXrSEEoojrpeA_9PlV1RdZ5_sCcejPO5L3czXQhub57HbD4YINHg7CHEBKHzyJBkHiFmDnV8QRKJNIBWkcLSQFbTdYErK3kSyEsQePOvRg92KHZXLRfgWkQ-o_U3DThNrHf3u1AqjQOeJ4PkxtOAsNeAvC0ffpyOWs8hTYFrnNBUsQS4wM5oYBIIeCLiD0svMJ0-Ia1aZVcc2U6VdG6X_o62RQZMpjuf_x-yZD09i0045kRas2zN8XegF-je3Pndn6Ge1FPbmSWbDXi6xD5QAcgoLtBiA2hdFRMftdGS6_4FifI3ZxONYvedkRV7d9g2vxg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c368c47031.mp4?token=RYqWSJ8RhbuKRm-KAQ3RXrSEEoojrpeA_9PlV1RdZ5_sCcejPO5L3czXQhub57HbD4YINHg7CHEBKHzyJBkHiFmDnV8QRKJNIBWkcLSQFbTdYErK3kSyEsQePOvRg92KHZXLRfgWkQ-o_U3DThNrHf3u1AqjQOeJ4PkxtOAsNeAvC0ffpyOWs8hTYFrnNBUsQS4wM5oYBIIeCLiD0svMJ0-Ia1aZVcc2U6VdG6X_o62RQZMpjuf_x-yZD09i0045kRas2zN8XegF-je3Pndn6Ge1FPbmSWbDXi6xD5QAcgoLtBiA2hdFRMftdGS6_4FifI3ZxONYvedkRV7d9g2vxg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ درباره رهبران ایران:
من با آنها سر و کار دارم و به آنها می‌گویم: «شما مردم دیوانه‌اید. شما دیوانه‌اید. شما دیوانه‌اید.»
من به آنها می‌گویم شما دیوانه اید و آنها می‌دانند من چه احساسی دارم.
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 3.07K · <a href="https://t.me/funhiphop/74636" target="_blank">📅 19:53 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-74635">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8fd979db91.mp4?token=YZGOkASkWtC4cqwiaHr5HwIGrMsozjYRbguRnjF6og0T6DS-jvez7l6nRp1dp40DIvuY7bue8kDBuHPgikD16ZV1p2iDSnu50SVibdkYmalj6gtfZ23vx8L_IJn8vYJpOK4EMUPU3U2iLX3M_JnKKHuCyMQGVk-X2udEkGhRMV-R7VBlNU2ppdZDI6QZkrlsLT4ll9NZPUSp4oxJaOyZNqJMb6TUGN-gInbsBnJNUNDfRbWg_4Wp5YWNsWL97bHP_S2FhxbdZ-HB1X_DBSutHoLo9wKaJZUB3yG-DXAklhuVE1Gxd1Y3ZXo0QR18YYQKtcgY79Vqpdg_KG5GwXKerw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8fd979db91.mp4?token=YZGOkASkWtC4cqwiaHr5HwIGrMsozjYRbguRnjF6og0T6DS-jvez7l6nRp1dp40DIvuY7bue8kDBuHPgikD16ZV1p2iDSnu50SVibdkYmalj6gtfZ23vx8L_IJn8vYJpOK4EMUPU3U2iLX3M_JnKKHuCyMQGVk-X2udEkGhRMV-R7VBlNU2ppdZDI6QZkrlsLT4ll9NZPUSp4oxJaOyZNqJMb6TUGN-gInbsBnJNUNDfRbWg_4Wp5YWNsWL97bHP_S2FhxbdZ-HB1X_DBSutHoLo9wKaJZUB3yG-DXAklhuVE1Gxd1Y3ZXo0QR18YYQKtcgY79Vqpdg_KG5GwXKerw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خبرنگار:
درمورد ایران آیا معتقدید راه حل دیپلماتیک هنوز هم ممکن است یا فقط راه حل نظامی را اثر بخش می‌بینید؟
ترامپ:
خب راه حل دیپلماتیک هنوزم ممکن است.
ببینید آنها مردم بسیار بی‌احترامی هستند، رهبری‌شان.
من قبلت ۵ بار با آنها توافق کردم اما آنها ناگهان نظرشان را تغییر دادند.
﻿
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 2.91K · <a href="https://t.me/funhiphop/74635" target="_blank">📅 19:50 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-74634">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f89493fa89.mp4?token=caClSDKYxfxtkSw4z2a-Sp2sguqsa5r6Ei1MbVHa_iCJDK7XriGHb7i-BXkeWj6T16fOCzDq14a4I1XMpvXJ9c04VuwoBrIM_NRkCiO3FKvOJ_9AEwCFKh9HizXjTatT8itR7FEjuf9XUreg-fnJUn560y_yglUqp4t-N5lCosVA3GN2hn1Wqg_-zVJO3DLmHL80V8qfzI0D8oM2C_MD0jH4EG0V7ZMaip_iphxv1HenIVNXkrCuol9-Xzv3rR_o9zmnNrd8flQn-hw8dB7S2gf5WUOGnWY2QGt7h24jqxbO01E9o5eU1rhEv3ntFfjLsEYzA_SymXgFsSCv8-b6wA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f89493fa89.mp4?token=caClSDKYxfxtkSw4z2a-Sp2sguqsa5r6Ei1MbVHa_iCJDK7XriGHb7i-BXkeWj6T16fOCzDq14a4I1XMpvXJ9c04VuwoBrIM_NRkCiO3FKvOJ_9AEwCFKh9HizXjTatT8itR7FEjuf9XUreg-fnJUn560y_yglUqp4t-N5lCosVA3GN2hn1Wqg_-zVJO3DLmHL80V8qfzI0D8oM2C_MD0jH4EG0V7ZMaip_iphxv1HenIVNXkrCuol9-Xzv3rR_o9zmnNrd8flQn-hw8dB7S2gf5WUOGnWY2QGt7h24jqxbO01E9o5eU1rhEv3ntFfjLsEYzA_SymXgFsSCv8-b6wA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ:
بسیاری از مردم می‌پرسند: «آیا او اصلا درمورد ایران برنامه‌ای دارد؟»
البته که برنامه دارم. بهترین برنامه‌ای که تا به حال وجود داشته را دارم.
ایران از نظر نظامی کاملا شکست خورده است، البته آنها مقداری از مهمات خود را در چند هفته گذشته بازسازی کرده‌اند ، ما می‌توانیم آنها را ظرف یک روز از بین ببریم.
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 2.77K · <a href="https://t.me/funhiphop/74634" target="_blank">📅 19:39 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-74633">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5cd45ad50d.mp4?token=lRwW0TNhthWRKQ5nTZwadZDuWGJm_evkFtQ-eAqYFemqHCdOP5-CqSy5iEHJ5ekJHUzfnIXqJzTrGB16bFhdj8FkGbiMkTLs7kfZt7QaJxydkxoMpJ3vJE0uhjGH4KS-zhdkGXwGE73yHSDuq5rI9EaTTXqIIHBErE8InfmGrh-uEZ3HnXLnGQ71PfAa7I9ED5tAVnBJ5pt6JQJL1K4KkGx17Dn16Hb_Yv0chIcedxpkE3F2DUHJPFO101EkI4iaeaf2mz26zX_KxOwclzT46z7IuXx6vMIUzqHnKNKhEw9h1F0gihqqfxTCkoyzn1KkDVoxz85owPfqBjm6ynj8LQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5cd45ad50d.mp4?token=lRwW0TNhthWRKQ5nTZwadZDuWGJm_evkFtQ-eAqYFemqHCdOP5-CqSy5iEHJ5ekJHUzfnIXqJzTrGB16bFhdj8FkGbiMkTLs7kfZt7QaJxydkxoMpJ3vJE0uhjGH4KS-zhdkGXwGE73yHSDuq5rI9EaTTXqIIHBErE8InfmGrh-uEZ3HnXLnGQ71PfAa7I9ED5tAVnBJ5pt6JQJL1K4KkGx17Dn16Hb_Yv0chIcedxpkE3F2DUHJPFO101EkI4iaeaf2mz26zX_KxOwclzT46z7IuXx6vMIUzqHnKNKhEw9h1F0gihqqfxTCkoyzn1KkDVoxz85owPfqBjm6ynj8LQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ:
کردها فقط می‌گیرند، می‌گیرند، می‌گیرند.
من از کردها بسیار ناامید شده‌ام.
آنها قرار بود سلاح‌ها را به داخل ایران حمل کنند اما خودشان آنها را برداشتند.
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 2.97K · <a href="https://t.me/funhiphop/74633" target="_blank">📅 19:23 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-74632">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/37d7d60d96.mp4?token=CpF46Eat8XdvLGoH59HvYWgFdCSyYRYWuffy2NKhJpgfsduzngEiW8L3jS9VGEWCiT6BFVaf0x_LY6XVsdI4T9EUcZCZN4zx3kkBREzV1O-7cCaxtzaBREwDvZwYUQy3BW9JhJo_f_LX5gzbOsr0VVROlU7elcqtj2-htDc8fL6DJgbVubbPmoWIkuhcU59nES3wRiBYT2VB6HwM-Jb7aLZRcaxyo8CNmYMdFq8C9vsxthLo5LV63-3uC_qBUwEi3DUjpy8wroq7pQEXfw288tm4ZIhTSxuta-COKpA3UkO5NRSgLH0X9r79vkyfLa7_13yg-qQ_U_hezcBAxSKyRw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/37d7d60d96.mp4?token=CpF46Eat8XdvLGoH59HvYWgFdCSyYRYWuffy2NKhJpgfsduzngEiW8L3jS9VGEWCiT6BFVaf0x_LY6XVsdI4T9EUcZCZN4zx3kkBREzV1O-7cCaxtzaBREwDvZwYUQy3BW9JhJo_f_LX5gzbOsr0VVROlU7elcqtj2-htDc8fL6DJgbVubbPmoWIkuhcU59nES3wRiBYT2VB6HwM-Jb7aLZRcaxyo8CNmYMdFq8C9vsxthLo5LV63-3uC_qBUwEi3DUjpy8wroq7pQEXfw288tm4ZIhTSxuta-COKpA3UkO5NRSgLH0X9r79vkyfLa7_13yg-qQ_U_hezcBAxSKyRw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ درمورد مقامات ایرانی:
مگر آنها چقدر احمق هستند؟ آدم‌های احمق. آنها فکر می‌کنند که خب، من از این خسته می‌شوم، حوصله‌ام سر می‌رود، تحت فشار قرار می‌گیرم.
هیچ فشاری وجود ندارد. ما پیروزی کامل خواهیم داشت. ما از نظر نظری، از دیدگاه نظامی، قبلاً پیروزی کامل را داریم.
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 2.84K · <a href="https://t.me/funhiphop/74632" target="_blank">📅 19:16 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-74631">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">سخنگوی کمیسیون امنیت ملی به نقل از رئیس سازمان انرژی اتمی:
فناوری هسته‌ای در دستور کار مذاکرات نیست.
چون غنی‌سازی قابل مذاکره نیست.
فعالیت‌های صنعت هسته‌ای ایران صلح‌آمیز بوده و صلح‌آمیز باقی خواهد ماند.
اقدامات لازم برای حفاظت احتمالی از مراکز و دارایی‌های هسته‌ای برنامه‌ریزی و اجرا شده است.
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 3.15K · <a href="https://t.me/funhiphop/74631" target="_blank">📅 19:04 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-74630">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e8cf705ff8.mp4?token=aQWUfy3ddj1pvozHlTAAEOXT7BwS2m-Nre2uIMcGTYtnOkFYiHjwPMRLRK_9eZ-ReC6oxsJ5YTmIz6_yRdaJu8wSA5hQjXxwIk64YgYbqYs6rNXuG0uMMj-9_QM9E1_9rFlWjHF6OglD2CqK4OrRdNDvIWN2d00Ly8L2bwLW_g9daT_9XyaYw2C3ZLBROoE-EKfBPBsCM_oLKNp8Axa1hMv72xshVPfk-PFKV8oAwRD6NEJvtdDxBu_NqsFfiRFxT1y-etpyOwUQ7GhxOD02P9Mo2Dyi7ZNeK_j69pEopv7rKkJaRRl8z7MCgPkdjyRoNlVpRe5kGqNdsBtQc2wECQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e8cf705ff8.mp4?token=aQWUfy3ddj1pvozHlTAAEOXT7BwS2m-Nre2uIMcGTYtnOkFYiHjwPMRLRK_9eZ-ReC6oxsJ5YTmIz6_yRdaJu8wSA5hQjXxwIk64YgYbqYs6rNXuG0uMMj-9_QM9E1_9rFlWjHF6OglD2CqK4OrRdNDvIWN2d00Ly8L2bwLW_g9daT_9XyaYw2C3ZLBROoE-EKfBPBsCM_oLKNp8Axa1hMv72xshVPfk-PFKV8oAwRD6NEJvtdDxBu_NqsFfiRFxT1y-etpyOwUQ7GhxOD02P9Mo2Dyi7ZNeK_j69pEopv7rKkJaRRl8z7MCgPkdjyRoNlVpRe5kGqNdsBtQc2wECQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ:
من زیاد صحبت نمی‌کنم چون گروهی بزرگ از ژنرال‌های نظامی منتظر من هستند و این (جلسه) مهمه و مربوط به کشور بسیار دوست‌داشتنی ایرانه.
🥰
🥰
🥰
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 3.55K · <a href="https://t.me/funhiphop/74630" target="_blank">📅 18:51 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-74629">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">ترامپ:  رهبران تندروی ایران هم تسلیم خواهند شد. تا زمانی که به توافق نرسیم با ایران مذاکره و تعامل خواهیم کرد.  @FunHipHop | Nima</div>
<div class="tg-footer">👁️ 3.52K · <a href="https://t.me/funhiphop/74629" target="_blank">📅 18:31 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-74628">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">ترامپ: پروژه‌ی آزادی این بار دامنه‌ای گسترده‌تر و فراتر از فقط همراهی کشتی‌ها از تنگه هرمز خواهد داشت.  @FunHipHop | Nima</div>
<div class="tg-footer">👁️ 3.52K · <a href="https://t.me/funhiphop/74628" target="_blank">📅 18:22 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-74627">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">ویویویویوی ترامپ به فاکس نیوز:  در حال بررسی از سرگیری عملیات «پروژه آزادی» هستم.  @FunHipHop | Nima</div>
<div class="tg-footer">👁️ 3.42K · <a href="https://t.me/funhiphop/74627" target="_blank">📅 18:19 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-74626">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">ویویویویوی ترامپ به فاکس نیوز:  در حال بررسی از سرگیری عملیات «پروژه آزادی» هستم.  @FunHipHop | Nima</div>
<div class="tg-footer">👁️ 3.6K · <a href="https://t.me/funhiphop/74626" target="_blank">📅 18:12 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-74625">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">ویویویویوی
ترامپ به فاکس نیوز:
در حال بررسی از سرگیری عملیات «پروژه آزادی» هستم.
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 3.57K · <a href="https://t.me/funhiphop/74625" target="_blank">📅 18:09 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-74624">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">مشاور ارشد کاخ سفید:
در مذاکرات با ایران عجله‌ای نیست چون اقتصاد آن‌ها در آستانه فروپاشی است.
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 3.57K · <a href="https://t.me/funhiphop/74624" target="_blank">📅 17:58 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-74623">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">به دستور مقامات قضایی، ۲ واحد تجاری و ۴ واحد مسکونی منتسب به علی کریمی توقیف و مصادره شد.
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 3.72K · <a href="https://t.me/funhiphop/74623" target="_blank">📅 16:45 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-74622">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">یارو نمیتونه به کسی که نتشو قطع کرده و باعث بگا رفتن درامدش شده چیزی بگه پاشده داره به یکی دیگه کصشر میگه، چارتا کصخلم پشت دست این بازی میکنن</div>
<div class="tg-footer">👁️ 3.7K · <a href="https://t.me/funhiphop/74622" target="_blank">📅 16:42 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-74621">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">بعد خارکصه که تا دیروز پولاشو تو ویدیو هاش میکرد تو چشم اینو اون الان میگه در به در دنبال کنسرویم واسه خوردن خود کنسرو خورا کیرشونم نیست اونوریا کنسرت میزارن یا نه سریع خودتو با ملتی که هیچی از دردشون نمیدونی جمع نبند</div>
<div class="tg-footer">👁️ 3.65K · <a href="https://t.me/funhiphop/74621" target="_blank">📅 16:39 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-74620">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">بخدا این حرفایی که آدرویت زده اگه از دهن یه رپر درست حسابی در میومد میشد راجبش بحث کرد، ولی متاسفانه رپری که نمیشه یه ربع پشت سر هم گوشش داد نباید این حرفارو بزنه.</div>
<div class="tg-footer">👁️ 3.43K · <a href="https://t.me/funhiphop/74620" target="_blank">📅 16:36 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-74619">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">بخدا این حرفایی که آدرویت زده اگه از دهن یه رپر درست حسابی در میومد میشد راجبش بحث کرد، ولی متاسفانه رپری که نمیشه یه ربع پشت سر هم گوشش داد نباید این حرفارو بزنه.</div>
<div class="tg-footer">👁️ 3.38K · <a href="https://t.me/funhiphop/74619" target="_blank">📅 16:34 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-74618">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">سخنگوی وزارت خارجه در پاسخ به پست ترامپ: تصمیم را به شما و مردم‌مان می‌سپارم که آیا درخواست ایران برای آتش‌بس در کل منطقه، یا آتش‌بس در دریاها و آزادسازی پول‌های مرتبط با ما، درخواستی غیرمنطقی و غیرقابل‌قبول است؟ آیا پیشنهاد ما برای تضمین عبور ایمن از تنگه…</div>
<div class="tg-footer">👁️ 3.77K · <a href="https://t.me/funhiphop/74618" target="_blank">📅 16:28 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-74617">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">ویویویویوی  ترامپ: من همین الان پاسخ به اصطلاح «نمایندگان» ایران را خواندم. این را دوست ندارم — کاملاً غیرقابل قبول است!  @FunHipHop | Nima</div>
<div class="tg-footer">👁️ 3.51K · <a href="https://t.me/funhiphop/74617" target="_blank">📅 16:22 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-74615">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">ژاپن اگه از آمریکا بمب اتم نمیخورد تا الان با سلاح های بیولوژیکیش بلایی سر دنیا میاورد که جنگ جهانی جلوش یه شوخی بیش نمیبود.
انقدر با جمله "کشوری که خودش از بمب اتم استفاده کرده میخواد نزاره ما بمب اتم بسازیم" کون خودتونو پاره نکنید، تهش همونی میشه که از قبل مقدر شده، نه زجه و ناله های شما طرفدارای حکومت و نه زجه و ناله های مخالفای حکومت هیچکدوم به کیر هیچکس نیست، و تاثیری در روند سیاسی مقدر شده نداره.
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 3.65K · <a href="https://t.me/funhiphop/74615" target="_blank">📅 15:46 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-74614">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">بهرام اگه ایران بود دست خانومی و میگرفت میرفتن دم ساختمون وزارت ارتباطات ساز موافق سیمکارت سفید و سیمکارت پرو میزدن, یه آلبوم هم دیس به فیلترشکن فروشا میدادن.
#از_دموکراسی_بگو
@FunHipHop
| Reza</div>
<div class="tg-footer">👁️ 3.68K · <a href="https://t.me/funhiphop/74614" target="_blank">📅 15:41 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-74613">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/socqrhOoygL0P9LKneTg2EeZUPi8GSYEPKwf9JAH2pQ_4gdg4HZy1DkKeLLu20GiwOf1WrsbbeTEGO49sGIjDXkE8gJpiTMcVSw5saRw5gVXNIWyGSmmDwL19AK4CakdJ3LSj-4bATN3ZqXKCqLikSnGLyBr0B3SR9vOwoD8-PH__jUNQsVfOsyfMBvTkO85lqX95_hiSAbfy55OMTbJ71_5nnuILToJhqUZkh3rRgBuKUVTwjMbvxRHz3QWdwBgfnvKs2LkZmj8oaHdXT5eqwBrAH8BMzYVG9Dqh5L_2Wv3p8LlJIhy6iKFHc-0gWt9fyFm19cclDnqy4Ow-Fh8nA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">همون همیشگی (اگه یادتون رفته جنوب لبنانه)   @FunHipHop | Reza</div>
<div class="tg-footer">👁️ 3.67K · <a href="https://t.me/funhiphop/74613" target="_blank">📅 15:20 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-74612">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">نکته ای که درمورد بعضی کانفیگ های موجود در بازار وجود داره اینه که شما بجای اینکه به سرور خارجی وصل بشید مستقیم وصل میشید به یک سرور ایرانی و عملا هیچ سرور خارجی وجود نداره به عبارتی اشخاصی که اینترنت سفید/پرو دارن دارن با استفاده از ابزارهایی شما رو به سیمکارت…</div>
<div class="tg-footer">👁️ 3.52K · <a href="https://t.me/funhiphop/74612" target="_blank">📅 15:10 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-74611">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BD9z2Vfz9DbUXUOZtwY4oPnRddujtaRb13regv3S_N455e4ud8PJjWKZZhp1KoKr8QLCBgs849sF0SEruEuA5jNLBv7zp4lPDp4S7wyNjdpe6wk8ztefa3l72VTaT0KMmETwEG9mzaIh3JlhBNbamkbyEQQpidotMi7TfbDjU8YW0xkZO_842vgbc7R7tlDFrh9tetJ5BkQfDPik4sZZTFnSjyzf1g64tR5bo0u2rdPXMF-98jNz98UjWVoPaAG1bjGj7bj30g8R1kppq0aEnFkBcFBMfWFQid-Q2i5ViYqGE-7_fTS2E8k0v9boN4EhwYs75-9Kmqy3bFewWXaUtg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نکته ای که درمورد بعضی کانفیگ های موجود در بازار وجود داره اینه که شما بجای اینکه به سرور خارجی وصل بشید مستقیم وصل میشید به یک سرور ایرانی و عملا هیچ سرور خارجی وجود نداره
به عبارتی اشخاصی که اینترنت سفید/پرو دارن دارن با استفاده از ابزارهایی شما رو به سیمکارت خودشون وصل میکنن:))
نکته مهمتری که وجود داره بیشتر این رنج‌ایپی ها ثبت شده توسط شرکت های افغانی
🇦🇫
هست که این یه فرضیه رو ایجاد میکنه:
نکنه اینترنت پرو/سفید پولش میره تو جیب افغانستانی ها؟!
از نظر دولت شاید اینترنت گیگی ۵ هزارتومن مشکل امنیتی داشته باشه اما اینترنت (کانفیگ گیگی خداتومن و یا بسته اینترنت سفید/پرو) هیچ مشکل امنیتی نداره و همه میتونن ازش استفاده رو بکنن
خود دولت در جریانه از وضعیت بازار و میدونه که بازار VPN ها به چه شکله اما چون سود هنگفتی داره در این باره سکوت کردن و دارن پولشون رو میخورن و به ریش من و توی ایرانی میخندن
@FunHipHop
| ALI</div>
<div class="tg-footer">👁️ 4.2K · <a href="https://t.me/funhiphop/74611" target="_blank">📅 15:05 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-74610">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ntSeqRcl7FpimyCN4PUF8Fd3EDJp_M3UG1i75J01oHixxAam0wS8HC8doMzKKzsdDiQ7k_QgD2gNHrCtPNbq_JT1XXeEg1GuOpdD6UuVkH59EJMv3Xit5UR2W_425Wf1vALFNT76GRXX0w8XlKg71NYHDUITlf59yZlO5TQqLuSon4DG27i7TQH6EjMpN0KRAN_wShhewwmcvuIg2EbsmCyrpvGQX7FbCzyss714q0IelNeLty3eWP8SADIR2uSBCYE4f9Pl31VBuYq7GAw9jVzZ6Kgc2DR9ZTRcVJUqe0WFlXdeQQeMywSDZqeOlUDEPo--iNutAztqwjCMmpO6iA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">همون همیشگی (اگه یادتون رفته جنوب لبنانه)
@FunHipHop
| Reza</div>
<div class="tg-footer">👁️ 3.66K · <a href="https://t.me/funhiphop/74610" target="_blank">📅 14:54 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-74609">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">اینطور که داره برا همه پیامک اینترنت پرو میره فک کنم دردشون فقط قیمت و احراز هویت بود
@FunHipHop
| Menot</div>
<div class="tg-footer">👁️ 3.9K · <a href="https://t.me/funhiphop/74609" target="_blank">📅 14:45 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-74608">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">بنیامین نتانیاهو در ادامه کشورهای عربی به‌دنبال تقویت روابط خود با اسرائیل هستند تا ایران را مهار کنند. برخی از کشورهای عربی می‌گویند و من قبلاً هرگز چنین چیزی نشنیده بودم. بیایید اتحادمان با اسرائیل را تقویت کنیم، چون این کار در عمل باعث بازدارندگی در برابر…</div>
<div class="tg-footer">👁️ 3.97K · <a href="https://t.me/funhiphop/74608" target="_blank">📅 14:11 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-74607">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fGGwhL4_D8WZjR0rjZKvk2KRIN0TLOvq1Gc8VdmfJDEEob7u6BioUucJJGS28rRNVQ11KiW5whLzinQPfF0_KdNtxrLMuwLBQ5dPsirKPpjZxrof3IKoYthuDNQe3eycR2A_OnCzaqn57qOqmnlV_BlaUCxwre0uwPLnsJj-KH80xawieS4QN7w2Y-XGpuv7mLYLlta8ybRJdQQClKErEheqdA0LHv3flUJu7PBkJhYbqTfVlWsSNR_HQb9racm-DoazaUhJ9qpMMRBN9lXaAh1V3y15wSsnJ9k6NH2Q3nYPuvMnSrNuan7ELPfgEJmsygCjKHwh3TRBOgembWbdZg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دیشب تو حالت عادی هیچ تبلیغی از وان ایکس کنار زمین نبود ولی تو پخشی که صدا سیما میکرد اضافه شده بود، حتی نمیشه گفت هم شبکه پخش کننده ای که ازشون دزدیدن اضافه کرده چون اینا بیمه دات کام رو اضافه کردن و میتونستن اونم حذف کنن
@FunHipHop
| Menot</div>
<div class="tg-footer">👁️ 4.12K · <a href="https://t.me/funhiphop/74607" target="_blank">📅 14:01 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-74606">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/md9baKfHYGTg27GcaJZGBGT1NvkJN_ND8D2nClQ_d7rOo7oZC6Ix6web1303wWC5ChuRHJlk33Qm6UGRqaIV36LPAmbnitf3meUpO_de-rSKjDOOuyJnCELUf0Xhld5lgM_02Dm2X-WHCnUoPPS9SXJuSF31G0tC60APpXcP4VbaagvO8ZIT5-iSJ3S93B9OiPIJLRHyRA4svKLSBip7I6__nTo9tw7n7eliG5PPyl-0QlPHk24unavJNFy34YQewFbs2v4vO5E7EoWsKKtCzalgkzazelw-IALeFvR47ndfufuzpdlfQQk8pTrBewGLq52FOlt275EfTadqOu2xpw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حزب الله لبنان برا گول زدن ارتش دفاعی اسرائیل و پهپاد های انتحاری داره این حرکت و میزنه.
@FunHipHop
| Reza</div>
<div class="tg-footer">👁️ 4.25K · <a href="https://t.me/funhiphop/74606" target="_blank">📅 13:43 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-74605">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">یه حسی بهم میگه خرداد ، بمب اتم میریزن سرمون
@FunHipHop
| ALI</div>
<div class="tg-footer">👁️ 3.94K · <a href="https://t.me/funhiphop/74605" target="_blank">📅 13:24 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-74604">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">امروز تورم مصرف کننده چین و همچنین تورم تولید کننده چین افزایش بی سابقه ای داشت.
@FunHipHop
| Reza</div>
<div class="tg-footer">👁️ 4.21K · <a href="https://t.me/funhiphop/74604" target="_blank">📅 12:57 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-74603">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CzuucBF_a-HtyKaj8nK4IzQtgAHzD6odVYZwSENOqqRkO8wNttMdqztJNfLWqByJSFPy8m-sjjgssY91fkJhuwpLilYqDVgF_rX26zmmMQgKb1bdf9j19c1ArjScF4q5RVx7d-9aMcgWtYw1IBvEjwlHt6fGbE_TObCl29KxspFESH4wktcdjxDsSDqw7PGignKpyphcLtzSG88104MXA5FYQt5jJ2c8sr77Pp0UK3Z8kZwBo52ybkps2WWGPvGWMkG6iWtmaTRlkDe_nyLYLoW5MSp7gX4bOj1L0qiWI71JF16N8uwmkuF0PWIwf93EYRBBjadmgIvQJnhO3wdblg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">صدای قوی انفجار در شیراز   @FunHipHop | Reza</div>
<div class="tg-footer">👁️ 4.62K · <a href="https://t.me/funhiphop/74603" target="_blank">📅 12:50 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-74602">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">صدای قوی انفجار در شیراز   @FunHipHop | Reza</div>
<div class="tg-footer">👁️ 4.4K · <a href="https://t.me/funhiphop/74602" target="_blank">📅 12:38 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-74600">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">صدای قوی انفجار در شیراز
@FunHipHop
| Reza</div>
<div class="tg-footer">👁️ 4.58K · <a href="https://t.me/funhiphop/74600" target="_blank">📅 12:34 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-74599">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">یدیعوت آحارونوت:
نتانیاهو امروز بعدازظهر در پی بحران در مذاکرات بین ایران و واشنگتن، جلسه امنیتی برگزار خواهد کرد.
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 4.68K · <a href="https://t.me/funhiphop/74599" target="_blank">📅 12:08 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-74598">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">رشفورد و تورس تو شب خوبشونم نفری ۳ تا ریدن</div>
<div class="tg-footer">👁️ 5.08K · <a href="https://t.me/funhiphop/74598" target="_blank">📅 06:09 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-74597">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">هر فرمی که دیشب میخواستم بزنم و خوابم برد نزدمو الان چک کردم، همشون لوز شدن
@FunHipHop
| Menot</div>
<div class="tg-footer">👁️ 5K · <a href="https://t.me/funhiphop/74597" target="_blank">📅 05:47 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-74596">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">هم اکنون مادر بهرام زیر شدید ترین کیرباران
@FunHipHop
| Constantine</div>
<div class="tg-footer">👁️ 5.01K · <a href="https://t.me/funhiphop/74596" target="_blank">📅 03:53 · 21 Ordibehesht 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>

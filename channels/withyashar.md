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
<img src="https://cdn4.telesco.pe/file/L0Q1rnirt1lR6QEbjfZjDCq9aA1iQFD32S75Hd2uGRId5ri0zxgRpfd4QuOoePyZ1amM6EEuz8mkmNt0Ket1bd4p_yapk-oU0kqjirMF-ak4U0soLBPM3STg7ip0PyM7SI8rmoiZMGRf0dcSPxEweIMlrSZed4A6ht3YokSKFoerWD79Ix_UWngkVVJAZhtYrYNgqVGbqjEU3ZssIfGO1UOhI7-64eqqMDZOrtfNdthEa8RoErk5IxxjyPzu6QjcOXX5zbJqYXx8LI2XqoGek0lDZNMc9zAA34HYJvbs61xafctF5DcA_DpG0Vz9kKOhpxOW85d1Yh2I9ELeCwgEMQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 WarRoom with YASHAR</h1>
<p>@withyashar • 👥 448K عضو</p>
<a href="https://t.me/withyashar" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 چنل رسمی«اتاق جنگ با یاشار»اخبار لحظه ای و فوری از‌ جنگ با تحلیل📸instagram.com/yashar🐦x.com/yasharrapfa📺youtube.com/yasharrapfa⛑️paypal.com/paypalme/yasharrapfa</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-16 14:07:21</div>
<hr>

<div class="tg-post" id="msg-22493">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">نتانیاهو: ما به نابودی خرابکاران، پیگیری کسانی که آن‌ها را اعزام می‌کنند و تخریب زیرساخت‌های تروریسم در کرانه باختری ادامه خواهیم داد. @WarRoom</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/withyashar/22493" target="_blank">📅 13:59 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22492">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">نتانیاهو: ما به نابودی خرابکاران،
پیگیری کسانی که آن‌ها را اعزام می‌کنند
و تخریب زیرساخت‌های تروریسم در کرانه باختری ادامه خواهیم داد.
@WarRoom</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/withyashar/22492" target="_blank">📅 13:58 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22491">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">آمریکا و اتحادیه اروپا در تلاشن شورای حکام آژانس بین‌المللی انرژی اتمی قطعنامه‌ای تصویب کنه که پرونده هسته‌ای ایران رو به شورای امنیت سازمان ملل ارجاع بده.
جمهوری اسلامی هم تهدید کرده که اگه این کارو انجام بدید، جواب متقابل میدیم. بالاخره از ان‌پی‌تی خارج میشن.
پیمان NPT در سال
۱۹۶۸
برای جلوگیری از گسترش سلاح‌های هسته‌ای ایجاد شد و در
۵ مارس ۱۹۷۰
به اجرا درآمد. ایران
از دوره پهلوی
عضو NPT بوده و جمهوری اسلامی در سال ۱۹۷۹ از این پیمان خارج نشد و عضویت ایران ادامه پیدا کرد
@WarRoom</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/withyashar/22491" target="_blank">📅 13:54 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22490">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-footer">👁️ 32.7K · <a href="https://t.me/withyashar/22490" target="_blank">📅 13:32 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22489">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/q5pITdcVjxiF3hep_uNhVZ-9g3oItQZy9F41Cni7W8mk0-UtvF_1MoWoPD2LUEOz-f8uGlygSAXH73_czYeMtrYQjeCuNzMiQsGU09NHpti5XOrrfPRrNFbHJXe7MjqqHrCVb1Td5DM5WbYolD4T9jT3y1-WFCFrE90GZvTpomF7yFHHUv1CtPKa5bfIbWCR4vfZOdM-k5pGAjS3G60gyL_uAmPfJ7l8xQ9p8jvR7Isrh4QlRdHlhM7ZSGPtRRiLmMNxQqj52wUL061rxQ3OEU2Na8katiUaFKvWul1Es5WuJVDkwbPQxNwg8Q8Dxu9aVnXXu2CyUwksVMmpn3YSqQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ در تروث ویدیو برنامه مارک لوین را بازنشر کرد:
در این گفت‌وگو، ویکتور دیویس هنسون ترامپ را
«معکوس‌کننده‌ی انقلاب»
می‌نامد؛ یعنی رئیس‌جمهوری که قصد دارد روندی را که طی۵۰سال آمریکا و سیاست خارجی آن را تغییر داده،
معکوس کند
. در مورد ایران نیز تأکید می‌شود که ترامپ برخلاف سیاست رؤسای جمهور پیشین،
به دنبال مهار موقت جمهوری اسلامی نیست، بلکه می‌خواهد تهدید اصلی رژیم را از میان ببرد
؛ به‌ویژه
توان هسته‌ای و موشکی و ظرفیت آن برای تهدید آمریکا و متحدانش
. هنسون این رویکرد را بخشی از همان
«معکوس‌کننده‌ی انقلاب» گسترده‌تر ترامپ
می‌داند؛ یعنی
شکستن سیاست‌های گذشته و بازگرداندن ابتکار عمل به آمریکا
. نکته امیدوارکننده برای مردم ایران این است که در این نگاه،
جمهوری اسلامی صرفاً یک حکومت مزاحم برای مذاکره و مهار نیست، بلکه یک تهدیدی است که باید قدرت آن از بین برود.
این گفت‌وگو همچنین بر این ایده تأکید دارد که در صورت
تضعیف قدرت رژیم، مردم ایران و نیروهای مخالف جمهوری اسلامی می‌توانند نقش مهمی در تغییر آینده کشور داشته باشند.
@WarRoom</div>
<div class="tg-footer">👁️ 46K · <a href="https://t.me/withyashar/22489" target="_blank">📅 13:12 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22488">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZbH4gfxSkgq19uS9IL7xQ3LjU3JsFja2xzz5hrROawnQgtP-KHl_-xZSfIx0qbAr2dAvfmKoGhgfccdUIVDhKplKSReWSeAsURSuMwZcmfVXZxswHeshbhLk3cIb9KLPkkVWzjujANnRlMSy2oNukmkO2miiMCtjJ-OeZbH1yBqSXqzhteLTHYu4H-GpqPlvhsFIMCBNM9buavB_RI_YQGl_-ghR6skcaEEKFDJJKwHpDQMQGRLpnUMZgdY2U8LjtEqDB5X1j7kynmj59gipVwDCquUK0YaTMw53jgM1q6CId67Dw9dICmFvk7QbgMH3uX6r1h0Kzb4rOY_Wl-GWLw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ در تروث و نظارت بر نابودی قایقهای تندرو
@WarRoom</div>
<div class="tg-footer">👁️ 48.1K · <a href="https://t.me/withyashar/22488" target="_blank">📅 13:03 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22487">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0dbc57d78d.mp4?token=gIG_GbIxgdVdX06EMo-BIo78zrWlxr9PM3p5UyvCj8gA6zINVvFXk8VEnM38yXkXUJBG0MNg06HJdeM0IHBu5dwHijheluwW5HIcC0Ti6PkvaI9EHWTfR7g9bOqRL_sVnlZCSuySsvK3WCbSjpHbfOG42ZvUMGLOuelycmr-XR7KNu2pW_M4IeU-UPhTohMgjo3NW0iUC2ryUOpe-29I7MhpuFuxa2yx8qlWQC1LFCwM4VViX7FvcCF96cbHhCTUM3wRghaH8ukKOeV0x7iDInjlTieciwPpcTKhz2izmlc2NeE02cHQYUcph6pgiHmkmN1hz991yWzeu6bm2ZzVWQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0dbc57d78d.mp4?token=gIG_GbIxgdVdX06EMo-BIo78zrWlxr9PM3p5UyvCj8gA6zINVvFXk8VEnM38yXkXUJBG0MNg06HJdeM0IHBu5dwHijheluwW5HIcC0Ti6PkvaI9EHWTfR7g9bOqRL_sVnlZCSuySsvK3WCbSjpHbfOG42ZvUMGLOuelycmr-XR7KNu2pW_M4IeU-UPhTohMgjo3NW0iUC2ryUOpe-29I7MhpuFuxa2yx8qlWQC1LFCwM4VViX7FvcCF96cbHhCTUM3wRghaH8ukKOeV0x7iDInjlTieciwPpcTKhz2izmlc2NeE02cHQYUcph6pgiHmkmN1hz991yWzeu6bm2ZzVWQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ادای احترام یکی از آسیب دیدگان چشمی به ناو هواپیمابر آبراهام لینکلن در تایلند
@WarRoom</div>
<div class="tg-footer">👁️ 52.2K · <a href="https://t.me/withyashar/22487" target="_blank">📅 12:56 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22486">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">گزارش های
تایید نشده
از منهدم کردن یک کشتی جدید در
خارگ
توسط امریکا
@WarRoom
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 55.2K · <a href="https://t.me/withyashar/22486" target="_blank">📅 12:49 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22485">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">ارسالی : سلام یاشار امروز از تعزیرات اومدن گفتن تمام لاستیک های کهنه که جلوی آپاراتی ها هستش باید فوراً جمع کنن کلا 24ساعت مهلت دادن برای جمع‌آوری گفتن به خاطر این دوباره ممکنه اعتراضات شروع بشه اگه مردم لاستیکا رو از جلو در مغازتون برداشتن و تو خیابون آتیش زدن  خسارتش رو باید مغازه دار بده
@WarRoom
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 63.4K · <a href="https://t.me/withyashar/22485" target="_blank">📅 12:31 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22484">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">بقایی سخنگوی وزارت امور خارجه: ظرف روزهای آینده، تفاهم ایران و عمان درباره تنگه هرمز نزد سازمان بین‌المللی دریانوردی ثبت خواهد شد
@WarRoom</div>
<div class="tg-footer">👁️ 72.7K · <a href="https://t.me/withyashar/22484" target="_blank">📅 11:48 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22483">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">بقایی: بنا داریم در نشست مجمع عمومی سازمان ملل مشارکت کنیم به شرط آنکه آمریکا ویزایمان را به موقع صادر کند
فرانسه، انگلیس و آلمان به دنبال تشدید اوضاع هستند، حتما ایران در قبال اقدام نسنجیده‌ سه کشور اروپایی و آمریکا تدابیر لازم را می‌اندیشد
@WarRoom</div>
<div class="tg-footer">👁️ 73.7K · <a href="https://t.me/withyashar/22483" target="_blank">📅 11:42 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22482">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e2b940d08b.mp4?token=daHztKY9159pFIW-qgekN47MqS0CEp4wnSDcDl9WVT21v2QYD9FB61GAT3xAqcbWj2QNsiZxEDcIjrHsO5eWkDbhQKCt4lb-JA56R92LoqBDOqlOXr2uCuuqVOVamF4iCzRFbVs03ZOhXxwWbTnvezjWVU7jD0sauObbagswyxcWB_FV3j8yePtqwN3sAXFCWXQ0kjBMwoSNXfkxO1gwjrgRNZ31yQXlni8C3uLAbT4xzGVJounUORpLqMuAZV4nxNvl-KLyjaV88CNLW0rB59y7-Aefld1e1BnFH8zh2-eLevgGvTH8G5DynJCVpyC2_Iuz0kBMTd3dmte_sj3sa1tLMYkxeB3Em6XSyDwI1vLTfP6iTnJBccrV3H3EoGOghMv8FkqUJnrXAck-D1KqSe8RTsF16_6PAlue5EOy1V3mImzRzQuUftDH43cqC6tMeFBAAPTXMnzSidFuj0ggP9Ydtjc_Dn31G7WOcS1SSMjwRwSypsQ-2gpCWMLTbDaTPuZ3ESKDNfvVpnUm70dEHw8ACoTx0WxakQ_76cAetucOG_trb6AB_h6OaUBe6geli81mEXVxcwGCmoPOH4qvg3jt0_0RaIZqiFgVzhYJf5L8BADWBRg-pfRmvvME_Z2Fdv-opGO-S-D78WvhkvwdqTl0VRcZktBR18YgQb7D_BY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e2b940d08b.mp4?token=daHztKY9159pFIW-qgekN47MqS0CEp4wnSDcDl9WVT21v2QYD9FB61GAT3xAqcbWj2QNsiZxEDcIjrHsO5eWkDbhQKCt4lb-JA56R92LoqBDOqlOXr2uCuuqVOVamF4iCzRFbVs03ZOhXxwWbTnvezjWVU7jD0sauObbagswyxcWB_FV3j8yePtqwN3sAXFCWXQ0kjBMwoSNXfkxO1gwjrgRNZ31yQXlni8C3uLAbT4xzGVJounUORpLqMuAZV4nxNvl-KLyjaV88CNLW0rB59y7-Aefld1e1BnFH8zh2-eLevgGvTH8G5DynJCVpyC2_Iuz0kBMTd3dmte_sj3sa1tLMYkxeB3Em6XSyDwI1vLTfP6iTnJBccrV3H3EoGOghMv8FkqUJnrXAck-D1KqSe8RTsF16_6PAlue5EOy1V3mImzRzQuUftDH43cqC6tMeFBAAPTXMnzSidFuj0ggP9Ydtjc_Dn31G7WOcS1SSMjwRwSypsQ-2gpCWMLTbDaTPuZ3ESKDNfvVpnUm70dEHw8ACoTx0WxakQ_76cAetucOG_trb6AB_h6OaUBe6geli81mEXVxcwGCmoPOH4qvg3jt0_0RaIZqiFgVzhYJf5L8BADWBRg-pfRmvvME_Z2Fdv-opGO-S-D78WvhkvwdqTl0VRcZktBR18YgQb7D_BY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">کاخ سفید : در روشن‌ترین روز، در تاریک‌ترین شب، هیچ پلیدی از دید من پنهان نخواهد ماند. بگذار کسانی که قدرت پلیدی را می‌پرستند، از قدرت من برحذر باشند... نور فانوس سبز!
کد سیگنال این پیغام
:در داستان اصلی «Brightest Day»،
Entity منبع اصلی حیات و نیروی زمین
است که پس از حملات نکرون و نیروهای تاریکی به‌شدت تضعیف می‌شود.
Entity به دلار آمریکا، منبع اصلی قدرت اقتصاد جهانی، تشبیه شده که بر اثر سال‌ها سیاست انفعالی و بی‌ثباتی‌های ناشی از جمهوری اسلامی تضعیف شده است.
حلقه فانوس سبز نیز نماد
اراده، غلبه بر ترس و ایجاد تغییر
است؛ و جهت‌گیری آن به سمت سرزمین ویران‌شده، به حرکت ترامپ و آمریکا به سوی خاورمیانه و به‌ویژه
ایران، به‌عنوان مرکز ثقل منطقه
تعبیر می‌شود. در پایان داستان، نور سفید نگهبانی را برای احیای زمین انتخاب می‌کند؛ این تصویر نماد
آغاز دوره‌ای تازه برای بازگرداندن ثبات و امنیت به منطقه
است.
پیام نهایی: پایان دوران مماشات با جمهوری اسلامی، اراده برای تغییر و آغاز روند بازسازی نظم خاورمیانه با محوریت ایران
@WarRoom</div>
<div class="tg-footer">👁️ 78.9K · <a href="https://t.me/withyashar/22482" target="_blank">📅 11:15 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22481">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">مدیرعامل شرکت فرودگاه‌ها:
۲۷ فرودگاه در جنگ آسیب دیدند
که آسیب‌ها در سطوح مختلف پروازی، باند، ساختمان های ایمنی، دستگاه‌های کمک ناوبری و بازرسی، ترمینال های مسافری و...بودند.بارها گفته‌ایم که بعد از آتش‌بس جنگ ما تازه شروع شده است.
بازسازی آنها کار سختی بود، ولی انجام شد، زیرا در بخش ساخت و ساز فرودگاهی توان خوبی داریم.
@WarRoom</div>
<div class="tg-footer">👁️ 76.8K · <a href="https://t.me/withyashar/22481" target="_blank">📅 10:58 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22477">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bf4f398265.mp4?token=oQWJGjJojS-C0lnA-Qv95rV3ULmCsq369n29lJbhEU3FuIyzjmwNJgsds4bi-Dq3w4KzssLyCKQEWKyQ5hpsSp4X9wNXLZNHQDKhDjGCDYnbsf7v5s6ssgYacpuOV2calArKgyHOTpbBGGRgmpi2kI60WxUNYxRykZU2-dw8Hsfqoi7SquM57Y3t2MuJADOSKY4FaTHMzB3_ZmFDKHXY3u4M1U3RldGjwLURckU07LjyAP5QZkfK9CQWoEfjXsBZHTBXQAFOfuOj_yPF22IzEoUYVadB1trx9Sys4A32pjBhjc_dOp4VVzcpAX76UmNNwiJG6lZHiFI5hmnkA5m2lA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bf4f398265.mp4?token=oQWJGjJojS-C0lnA-Qv95rV3ULmCsq369n29lJbhEU3FuIyzjmwNJgsds4bi-Dq3w4KzssLyCKQEWKyQ5hpsSp4X9wNXLZNHQDKhDjGCDYnbsf7v5s6ssgYacpuOV2calArKgyHOTpbBGGRgmpi2kI60WxUNYxRykZU2-dw8Hsfqoi7SquM57Y3t2MuJADOSKY4FaTHMzB3_ZmFDKHXY3u4M1U3RldGjwLURckU07LjyAP5QZkfK9CQWoEfjXsBZHTBXQAFOfuOj_yPF22IzEoUYVadB1trx9Sys4A32pjBhjc_dOp4VVzcpAX76UmNNwiJG6lZHiFI5hmnkA5m2lA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏خبرگزاری عراقی «بغداد الیوم» گزارش داده بیش از ۱۵۰ نفر آزادی خواه ایرانی به محل اسکان دانشجونماهای عراقی گروه تروریستی «حشدالشعبی» حامی جمهوری اسلامی در دانشگاه سمنان هجوم برده و شماری از آنان را مورد ضرب‌وشتم قرار دادند. تعدادی زخمی شدند و ادعا کرده پول، تلفن همراه و ساعت برخی از آنها نیز گرفته شده. گزارش‌هایی از تجمع مقابل خوابگاه و محاصره تعدادی از دانشجویان عراقی منتشر شده است. پلیس رژیم جمهوری اسلامی در محل حاضر شد
@WarRoom</div>
<div class="tg-footer">👁️ 82.1K · <a href="https://t.me/withyashar/22477" target="_blank">📅 10:43 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22476">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ddc3ca6006.mp4?token=ny9ig1GhZWEFapAiWHfCZlnFgGSgQFKs8anbU-uDxP7glkVaOz02TmNiv17WjB9RDiysUZnqKzhi4okF15e8hIeywr3QUWqHXMiF5914hz3Deml74h15Lyv1rAFSsLlmnsKN0suGpvubtXYGYEvfmIOL9rEBwsd63e5fLENzK_lEI-R4BOY4PWDNVcY1iGgrarrhLezs8LW0stkj0nYkr2ZFLNZ5Ld_RwsjKrhU0-7JtwLWkicVqqfyvVEBqCC3ZnWdZDoBM9P-2FCpXhnyK7H9pEYfeaWBxMiwtujmVd9W3VvlEhqRCdVYr2NFyxad5OQS0yUOPyDao664Gx5cNVI9PTGVeNTOj7y9YxQ5k3l2zrM1_jO6sVjaitBe0-42Kaa0TcpQpgp9hM50AW81jfs7Hi9_XtWAgcG6pBeJkpJuJIj1zzjMQG8vAp64PrRHOVcduXftgH7d0Nq0-u4Cpc5LEN9Ujd1tamgayPeeTSY-Zpqn_VR7HYnkMDpUAJFPBAj-SFr7R-pn2kQpjqiPzdhXPdCmd2NY2OSRnDp94qXipk5WGV6in2JpGmYr4lFp7O-0dk6NMhhMO1WrWV_H3bUZfHt6S9ZaU0Oy9dGiB1LL52YFJHIkmMr9hyZ6hQnzKfTJc3GTFNzJpIo9Fo68CPKIOqAtissMXEmPAeTjTF-Y" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ddc3ca6006.mp4?token=ny9ig1GhZWEFapAiWHfCZlnFgGSgQFKs8anbU-uDxP7glkVaOz02TmNiv17WjB9RDiysUZnqKzhi4okF15e8hIeywr3QUWqHXMiF5914hz3Deml74h15Lyv1rAFSsLlmnsKN0suGpvubtXYGYEvfmIOL9rEBwsd63e5fLENzK_lEI-R4BOY4PWDNVcY1iGgrarrhLezs8LW0stkj0nYkr2ZFLNZ5Ld_RwsjKrhU0-7JtwLWkicVqqfyvVEBqCC3ZnWdZDoBM9P-2FCpXhnyK7H9pEYfeaWBxMiwtujmVd9W3VvlEhqRCdVYr2NFyxad5OQS0yUOPyDao664Gx5cNVI9PTGVeNTOj7y9YxQ5k3l2zrM1_jO6sVjaitBe0-42Kaa0TcpQpgp9hM50AW81jfs7Hi9_XtWAgcG6pBeJkpJuJIj1zzjMQG8vAp64PrRHOVcduXftgH7d0Nq0-u4Cpc5LEN9Ujd1tamgayPeeTSY-Zpqn_VR7HYnkMDpUAJFPBAj-SFr7R-pn2kQpjqiPzdhXPdCmd2NY2OSRnDp94qXipk5WGV6in2JpGmYr4lFp7O-0dk6NMhhMO1WrWV_H3bUZfHt6S9ZaU0Oy9dGiB1LL52YFJHIkmMr9hyZ6hQnzKfTJc3GTFNzJpIo9Fo68CPKIOqAtissMXEmPAeTjTF-Y" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اخیراً تماس هایی از مبداء نامشخص
(شماره نمایشی سوریه) با مردم بومی جنوب کشور حاصل میشود و درخواست میکنند که طی درگیری های پیشِ‌رو هیچگونه حمایتی از سپاه نداشته باشند
@WarRoom
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 82.4K · <a href="https://t.me/withyashar/22476" target="_blank">📅 10:30 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22475">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromS.A.H74</strong></div>
<div class="tg-text">سلام آقا یاشار گل خوبی من بندرکنگ هستم سمت دریا ساعتای ۶صدای مهیب انفجار اومد نمیدونم چی بوده</div>
<div class="tg-footer">👁️ 83.2K · <a href="https://t.me/withyashar/22475" target="_blank">📅 10:16 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22474">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">العربیه: در حملات اسرائیل به کفررمان در جنوب لبنان تا این لحظه 9 نفر کشته شدند.
@WarRoom</div>
<div class="tg-footer">👁️ 85.7K · <a href="https://t.me/withyashar/22474" target="_blank">📅 10:12 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22473">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">رویترز , تنگه هرمز در پایین‌ترین سطح تردد: داده‌های کپلر نشان می‌دهد میانگین عبور کشتی‌های حامل کالا از تنگه هرمز در ۱۰ روز گذشته به حدود ۱۰ کشتی در روز رسیده که پایین‌ترین سطح از ماه مه است. همزمان ایران اعلام کرده قصد دارد یک منطقه ممنوعه جدید در نزدیکی…</div>
<div class="tg-footer">👁️ 101K · <a href="https://t.me/withyashar/22473" target="_blank">📅 08:32 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22472">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">گزارش صدای انفجار یا پرتاب موشک از چابهار
@WarRoom
🚨
🚨</div>
<div class="tg-footer">👁️ 102K · <a href="https://t.me/withyashar/22472" target="_blank">📅 08:25 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22471">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">رویترز , تنگه هرمز در پایین‌ترین سطح تردد:
داده‌های کپلر نشان می‌دهد میانگین عبور کشتی‌های حامل کالا از تنگه هرمز در ۱۰ روز گذشته به حدود
۱۰ کشتی در روز
رسیده که پایین‌ترین سطح از ماه مه است. همزمان ایران اعلام کرده قصد دارد یک منطقه ممنوعه جدید در نزدیکی تنگه ایجاد کند؛ در مقابل، عملیات دریایی آمریکا همچنان فشار شدیدی بر مسیر صادرات نفت ایران وارد می‌کند.
@WarRoom</div>
<div class="tg-footer">👁️ 105K · <a href="https://t.me/withyashar/22471" target="_blank">📅 07:58 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22470">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EwyEGws-I_YBvl8nGt4pqydLwq3uO1iCeiKPQOckavTeNGqtwiQ9_9LkWl4ZP034IXQxMUUAtl9_O-lHofx25MjzN2Vta2l42A75qx_-BpKC3Bov8gSYYL3O7embtukV7H2VOgzWNKZOpf68mbKF7UYFZhv39aUrZSy6Jb9rdJ_m0OG1ZkK4o0-PZD4IL-3faTqwNWIwrUD771BAmXspdskniCVR5Mfuj-fyMrjbiZDgeitd3UT88l1uQTNBd-L3FWNzlKrMi2wwbqMaTAmbIiq_qhD1tbZHklgS90unuBwGbHEIEcwClSXomzFih4ecoS2f9qayCGyxj2vJrkxB-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ارسالی : سلام یاشار جان امشب اینو دیدم تو خیابون تهران رو زمین بود ، به نظر از این تراکت ها تو تعداد پخش شده باشه تو شهر ، آخر این حکومت رسیده و جشن آزادی بزرگی قراره بگیریم
@WarRoom</div>
<div class="tg-footer">👁️ 136K · <a href="https://t.me/withyashar/22470" target="_blank">📅 00:58 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22469">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Par4ylA6ye7ufnIAVYRJia7fWj8qghg8AkBMVWE5P278WikpOYpxPW-BR7hjfNfqol2ByhxsA4T-JPF_Ho1I4KVDq7TZqxp6nI9ORy27kyaut89wEKhOVAXKcn4ISro3mrAWvqJ5EjFS7_Nn5i2plpe7j69CyTzY5XMWFWbvSQdrI9ABdxtETwJWnBqKl8pRyo1JkIWE7TMQSMOqHkdsT_Bx3H-Wi_5uUqhjC4qtzw17zxyCIHokGRslQE6Ar3eQRYLAGyhCRYz4Qa4cWYhcVCqRhTztBXq1R0pZn8wRKxwYaPUaDKJEI3xrKQwI643WQl6uDRT43wqLyqod1hyIPw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">زنی که جمهوری اسلامی او را «شاه‌مهره» می‌نامد، اکنون در زندان قم جانش در خطر است، برای نجاتش کمک کنیم
نازنین برادران، معروف به
«رها پرهام»
، پس از اعتراضات دی‌ماه توسط اطلاعات سپاه بازداشت شده و بنا بر اطلاعات خانواده، اکنون در
زندان قم
نگهداری می‌شود. رسانه‌های حکومتی مدعی شده‌اند او
معاون و دست راست بیژن کیان
، رئیس اندیشکده «صدای آزادی»، بوده و برای
هدایت اعتراضات و اجرای طرح براندازی جمهوری اسلامی
آموزش دیده است. آنها همچنین مدعی ارتباط او با
آدام لوینگر، افسر سابق پنتاگون
و دیدار او با
تام کاتن، سناتور آمریکایی
شده‌اند. نهادهای حکومتی همچنین می‌گویند او در تدوین ساختار حقوقی دوران پس از جمهوری اسلامی نقش داشته است.
اعضای خانواده وی به من گفتند که او قانون پس از براندازی جمهوری اسلامی را نوشته و آن را به سازمان ملل برده است.
اعضای خانواده وی می‌گویند
او از نخستین روز بازداشت ممنوع‌الملاقات بوده و حتی اجازه تماس تلفنی و شنیدن صدایش را نداشته‌اند
و اکنون
کیفرخواست پرونده‌اش در حال صدور است
. خانواده نسبت به وضعیت و امنیت جانی او به‌شدت نگران هستند و خواستار توجه رسانه‌ها و نهادهای حقوق بشری به پرونده او هستند.
@WarRoom</div>
<div class="tg-footer">👁️ 138K · <a href="https://t.me/withyashar/22469" target="_blank">📅 00:21 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22468">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EmqwiC85n7mC6abyubUSUl5gDtZQho7KInC1k4GQTpMuyvLXlaAtHQyi5TGzHkVmnOzE_k8VNgdMPy1p-VB4gmcAemCkx9jGwTZCJiIGGUXBdwO6tpPXSn_OzivcNWy3pi_nfQX18baaxPp_CCG8PoXqyRueKodPeHmfw-2U_KSURrYo9qeXEbAm22G1_5PCxFt3Nj0VcoOci4QrHeYIuqBI-94tIOLUaiw4EyU5LFDxM0FpMNN4DdgUDNZ4WELxzUQO9VhGSh0wmk7I9wvolIoRch0hAiP_hifZH-O6m0xaey1UlD9DWuNT0mJVg9DMeXZSWwe_ThNOjtH8KD80Yw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">درگیری میان نیروهای امنیتی و مهاجمین در زاهدان؛ بر اساس آمار اولیه، ۲ تن از نیروهای امنیتی کشته شده اند. @WarRoom</div>
<div class="tg-footer">👁️ 140K · <a href="https://t.me/withyashar/22468" target="_blank">📅 23:54 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22467">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">درگیری میان نیروهای امنیتی و مهاجمین در زاهدان؛ بر اساس آمار اولیه، ۲ تن از نیروهای امنیتی کشته شده اند.
@WarRoom</div>
<div class="tg-footer">👁️ 138K · <a href="https://t.me/withyashar/22467" target="_blank">📅 23:44 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22466">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mNef0cW43_j6Ipy97MHRLls_CGAPgn8Ch-dbFgjN811Lfztp1JV5xb-LEVauWfZM3FqyHO8g7xqbf6xvli6oshoOfy7YJRmybhLWiAFfPEnkMPhE76cv9651vWKNoU9oBoSc9p7WAez8svdzcnJg13_7PfnLuWlycCOGJJOKz_9NuTfRhPdtdlw4KKOV4HtSJ39Wr3ci-Db8kcIxXNBF41Be98Dfr_EDL_WgnmgfgHXgSSWj5S1zQN56TjgltIOhLWvLD984XOjs8kFpRmoyoL8zQ1WHzIvfBshqXDQzMvylrxw7bHPrgTBOQXD93QUkx_JeYm8AL04gEiqkmyawSA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ایران کشوری در حال فروپاشی است.
@WarRoom</div>
<div class="tg-footer">👁️ 143K · <a href="https://t.me/withyashar/22466" target="_blank">📅 23:02 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22465">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hFkRWg0XGdLYLhrWMKjP-L-azzUI_TVeIwVyGzzDuwVzZpyM8T_FSy0mCepOK1On5sGPB9X8tHrfu5H1UFhGd2xS3w3Djrttq12VO1AlmBnbBdoTOmmc6UqlsBB3K5j5-FxicPgb-62nQr3JgB8Uz38zYQKt9oAGOdqdwAL5RegX7k4ofLg5YaDsdoYvchA031OIW9HdUzHRH1gUJcQHjh6YN0bW0lHdcEgCyFvYqI3cFmJgimBdYAOs_yJ091ZLrAqySNoSWkHqdnCfw9yVjR012QAfKhPg_x-Wx6CtV8gRxMPBxJBfGZc_elxQlxRh6NI5axYQvS87jQtRqTo4Pg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ در تروث : حجم نفت هرمز برگشته است!
@WarRoom</div>
<div class="tg-footer">👁️ 141K · <a href="https://t.me/withyashar/22465" target="_blank">📅 22:51 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22464">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YF9usKgzmjgW0nTqdl_7vr4abKbnqGQTn2MLPXvaO4LNOz_-BEuH6oBdbtIN4jr7RUW-rtQl0DMJo5zGnz8lIOb3DptdxD5MU77gR8tXYmOE-Ctycod8g56mfIjlBeXVh-KkMzyHKgHpDHGDXFPuuEr1DcXReRp38zAigSLfn9NvdMs9ZVuNB-EXN4CfmQ6EeIxtovHmHwQE4cjhBxK1TYfVQtzsTH23uK8HAv5NSbKWHESkj2jdga0ZyLdbFAp46YrASAky4vBoRopghumwfruPQIX0_IPzEkIKY1YwDUhyfC-mjNfzJq-clrAD7UpFpEcMiRTPleTpESEgtsvLkQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ در تروث : کابوس برایشان بساز
@WarRoom</div>
<div class="tg-footer">👁️ 137K · <a href="https://t.me/withyashar/22464" target="_blank">📅 22:47 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22463">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XHffedJDodpmEGGaTk2XImh6B24rpnDvVwLonAzeUde0aq9uzIBc2SgqrMdP1LZwKqUC7IM5F8MKhxQfxRLrWevHjZ9jwxLiO--00XKouyKotZtXflxV52nxHfkJtw8mmlUV2Qmf3iWRarTVIVvqCm0VC8oeO8hzpzTsrFpt5y450jCK1CyXChdgEmqgOji62V-QNCOASXlvK4RpCzB9QtL61jAEscZTQVb4J-r8x1gnSn70tNs4cxQnR1yVECTTEBdtuwohveFFMDe0zV62M52NFQysCjDDOOU5AtVSdfUS2oWZpWAa8BOyxKtX2__KM0fln9zSU7au5JJ5vnOhKA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ در تروث : صادرات نفت ایران در حال سقوط است
@WarRoom</div>
<div class="tg-footer">👁️ 133K · <a href="https://t.me/withyashar/22463" target="_blank">📅 22:41 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22462">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DLa3yDy0jc8Fy7HX3YMt3Z7sIxsW1wJWHeUclGxOPC728nXM55hDFyIP3g879PDU9B0gjxT85LQtHay3dUcNnD1Hro84apl6VVj9H_TrjZ_Eu11t4lRMgruNrWlC8LKzvG6InqAcqGGIyWoZNGekSRBimDFobnPhqMtd8I3ChSgiFJ2jqNt4XRJZNvrIP06Pv4tA_ImfaA6GQegXDU8PuR9Zao6ktblBEOeguRbQH05XE633r_In6OKJONHRjpWTUeKB0rePNrEZ0myt2m0IItUGVZ0RxW2oNiZxNJosHWKJrXJF7W1G3truy9UMiqJy1GiNozut-Zc65ZSTroq2Sg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ در تروث :
ایران دچار ابرتورم است
پول ایران نابود شد
@WarRoom</div>
<div class="tg-footer">👁️ 138K · <a href="https://t.me/withyashar/22462" target="_blank">📅 22:39 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22461">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TQdomFCwF6wYmos_sf0Sr8BGm5IhU9g-Va8i5Vbcz_Hk4nag1WYHAGwrKNsu2ZUAChuFTBIWbE7gSUPboZ1aZ5649IlRMuR7aYmq-GK322v9e6PyrBVx5egqLARPUhqVgrSvR9CR4AjrtbTVNfCkekOhQg72juDjnZOwI1Ho447YhphkRzwE8bAtV8fCs8hDUh4WotWTm5d7IaHSXdgwA0rbjOI3VRLB4M3TzK3hjZcfcGoDn8-G6KzT4rDEGZwgOphUQf2IbLZcyyp3zrS0ju02Z86PJg5vvCcurc-VpRrDI1errNdNyZGJUwsluNYzYrocdw8YGc9B-2q99BMhpw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ در تروث : خداحافظ خارگ
@WarRoom</div>
<div class="tg-footer">👁️ 134K · <a href="https://t.me/withyashar/22461" target="_blank">📅 22:34 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22460">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">ارتش اسرائیل پس از شلیک دو پهپاد انفجاری حزب‌الله به سمت نیروهایش در ارتفاعات علی‌الطاهر، موج تازه‌ای از حملات را در جنوب لبنان آغاز کرد. اسرائیل اعلام کرده
انبارهای تسلیحاتی، مراکز فرماندهی و زیرساخت‌های زیرزمینی حزب‌الله
را هدف قرار داده و برای انهدام دو مسیر زیرزمینی در زیر ارتفاعات علی‌الطاهر نیز آماده می‌شود. همزمان گزارش‌ها از
انفجارهای شدید و درگیری‌های سنگین در منطقه نباطیه و اطراف علی‌الطاهر
حکایت دارد
@WarRoom</div>
<div class="tg-footer">👁️ 131K · <a href="https://t.me/withyashar/22460" target="_blank">📅 22:16 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22459">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GUZ3mQQ4cyOIbx5xYAcEZNQhpkliqPWpYD4M0et_tzFvjEmXjlY3L3OkBIG6Gw6GhDx9IQ2rU8jlAHtLwVGxtIOOg86J_WmfsI1HDr7LdIkdyiBZIRoQohbwCt834Po75k6UDr5ZcfCqsR4u9x7i5l9oMI4LAKaSX13yIuXIuOXycizyalaVWuQbycg6ExPK6sjsF3yJvx4I8NcqiL5V7h3ux34UvoEFLAlWhbHi5_hV-Mt3XDLwxIqQLJ-RHmmr-NNMQ3OmfTrKqXFqm3v9f5yruBw0kp6P6nzZwQPzotA0_4B4lqFefLDWMmyL7fo7ghGKkSbzniDeaJWFHvuIeg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ در تروث: نقشه ایران رو برعکس کنید میشه تصویر من
@WarRoom</div>
<div class="tg-footer">👁️ 151K · <a href="https://t.me/withyashar/22459" target="_blank">📅 21:29 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22458">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">😂
😂
😂
😂
😂
😂
😂
🚨</div>
<div class="tg-footer">👁️ 131K · <a href="https://t.me/withyashar/22458" target="_blank">📅 21:28 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22457">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">رژیم:نرخ سوم بنزین تغییر کرد/ سهمیه اول و دوم بدون تغییر
سخنگوی دولت: نرخ کارت جایگاه سوخت از بامداد ۱۷ شهریور به ۱۰ هزار تومان افزایش خواهد یافت.
در جلسات کارشناسی اعداد متفاوتی گفته می‌شد اما چون رئیس‌جمهور به مردم قول داده بود همان ۱۰ هزار تومان تعیین شد.
۶۰ لیتر بنزین ۱۵۰۰ تومان و ۵۰ لیتر بنزین ۳۰۰۰ تومان همچنان بدون تغییر ماند. افزایش قیمت نرخ کارت جایگاه صرف معیشت مردم خواهد شد.
@WarRoom
🚨
🚨
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 138K · <a href="https://t.me/withyashar/22457" target="_blank">📅 21:12 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22456">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">کان نیوز:
ارتش اسرائیل قصد دارد
شبکه تونل‌ها و زیرساخت‌های زیرزمینی حزب‌الله در منطقه علی الطاهر در جنوب لبنان را به‌طور کامل منفجر کند
و بر اساس گزارش‌های اسرائیلی،
در انتظار تأیید مقامات سیاسی برای اجرای این عملیات است.
گزارش‌های پیشین نیز از آماده‌سازی مواد منفجره در این منطقه خبر داده بودند.
@WarRoom</div>
<div class="tg-footer">👁️ 132K · <a href="https://t.me/withyashar/22456" target="_blank">📅 21:09 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22455">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">یعنی خوشم میاد شهید سید علی خامنه ای پدر ایران خیلی میسوزونه شمارو
😂</div>
<div class="tg-footer">👁️ 131K · <a href="https://t.me/withyashar/22455" target="_blank">📅 21:00 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22454">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">یعنی خوشم میاد شهید سید علی خامنه ای پدر ایران خیلی میسوزونه شمارو
😂</div>
<div class="tg-footer">👁️ 129K · <a href="https://t.me/withyashar/22454" target="_blank">📅 20:57 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22453">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromAmin</strong></div>
<div class="tg-text">یعنی خوشم میاد شهید سید علی خامنه ای پدر ایران خیلی میسوزونه شمارو
😂</div>
<div class="tg-footer">👁️ 125K · <a href="https://t.me/withyashar/22453" target="_blank">📅 20:56 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22452">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">نتانیاهو: ما مصمم هستیم که مأموریت سرنگونی رژیم ایران را به پایان برسانیم.
پایان جمهوری اسلامی نزدیک است.
@WarRoom</div>
<div class="tg-footer">👁️ 124K · <a href="https://t.me/withyashar/22452" target="_blank">📅 20:54 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22451">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ee397b868b.mp4?token=TzVaruC1fB4WU3l_pVbgPP65YxwCehptmgmExlUfttRoX5NDCCfAgZXTqVozmVLcKpGPK0ry4QwXXVOIsWfHq6gxbt4APRQZkXodJ1Z-Zd9z1aBq9K-FlcGbuMhG0ccc5xlW46qF9pQzfrr8GBEVmO19VksCN927rMOc1FkNN3d74nAw4fsFDCxNBB5FQjKKtc5MnqerKlLfwY3s1Cs7TGa9GMe85ISKRHimYAtGvFxbqF1LMA1BaYqBf4hUK-BLsC4kA2AcSUfZxxc9yxc92vXENevgE28V-4fVX2zu6Z-i9pYDZ6BzF-qIIY2YhwZdwkcvwiTtGfcA2IySLccpig" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ee397b868b.mp4?token=TzVaruC1fB4WU3l_pVbgPP65YxwCehptmgmExlUfttRoX5NDCCfAgZXTqVozmVLcKpGPK0ry4QwXXVOIsWfHq6gxbt4APRQZkXodJ1Z-Zd9z1aBq9K-FlcGbuMhG0ccc5xlW46qF9pQzfrr8GBEVmO19VksCN927rMOc1FkNN3d74nAw4fsFDCxNBB5FQjKKtc5MnqerKlLfwY3s1Cs7TGa9GMe85ISKRHimYAtGvFxbqF1LMA1BaYqBf4hUK-BLsC4kA2AcSUfZxxc9yxc92vXENevgE28V-4fVX2zu6Z-i9pYDZ6BzF-qIIY2YhwZdwkcvwiTtGfcA2IySLccpig" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جرد کوشنر: در دنیا چیزی به نام دشمنی ابدی یا دوستی ابدی وجود ندارد.
@WarRoom</div>
<div class="tg-footer">👁️ 121K · <a href="https://t.me/withyashar/22451" target="_blank">📅 20:39 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22450">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">کریس رایت، وزیر انرژی آمریکا، در مصاحبه با
مارتا رادزاتز، خبرنگار ارشد ABC News
در برنامه
This Week
درباره ادامه جنگ و سیاست آمریکا در قبال برنامه هسته‌ای ایران گفت:
ممکن است دولت ترامپ به توافق هسته‌ای با ایران دست پیدا نکند و در عوض، توانایی تهران برای دستیابی به سلاح هسته‌ای را از بین ببرد.
رایت تأکید کرد هدف اصلی آمریکا جلوگیری از هسته‌ای شدن ایران و کاهش توانایی این کشور برای تهدید منطقه است و گفت
اگر توافقی حاصل نشود، گزینه نظامی برای نابود کردن این توانایی همچنان روی میز خواهد بود.
او همچنین گفت آمریکا در حال وارد کردن
«درد کوتاه‌مدت»
به اقتصاد و بازار انرژی است تا به گفته او به وضعیت بلندمدت بهتری برسد.
@WarRoom</div>
<div class="tg-footer">👁️ 116K · <a href="https://t.me/withyashar/22450" target="_blank">📅 20:32 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22449">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">بهنام صمدی خبرنگار بورسی: از امشب نرخ سوم بنزین ۱۰ هزار تومان خواهد شد
@WarRoom
🚨
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 113K · <a href="https://t.me/withyashar/22449" target="_blank">📅 20:27 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22448">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1f35315292.mp4?token=lyhWxVYZWMBBO9ZrXxG-Zj0AIm56Q99bWNUUffJ5RCI55tZ6Enw2NzLAY3mG2PGkbeQGYmt2t8JnFuxOofzKRMMuY235hQpRgU-CScP6iepoL3iCDVx_m52YGv6yWsGmCXk4_26e_Qd2iVyFV4VYDx3VCscRDBR1kCV33Q7fGJ5TbUTrP7xbOQhaNOFjKBni2aXEy_d2gSf0D1GvcwIVIqEaRABY4J2C8igpLvzo_4pVbm5DHRx7N9S0j0tvZeiv4oDfpp8LzozensyPK-7oSOtUzvKp9AJBiJCGn_2o96Bbmy7Wwxccgi373FyaNVzboyaA7zICWZ72m_o-Y5CGuU12jUG8Hr7S3-sJm55qp8ODK3oAbEGbhgyJ00qlyo2hCKuvxQt_Y8qeXwZMyLGAJY3cgAMhzn8rRAVSVaro-qE33dwd2EfGvP8pq8bb0UU5xE2exk9hAnZh-kj-okFfiWwVymlijlt4VfEluQQ32vl3ugDKBcG5xuQCa--guKD8l5qUg2iVx56hE5Zfzqo5DJ54KxH6wDkIPlXdVdWR1OAMPuuPODKSzl0KxkIu8kzlKXCAX27hkkqrVDwOx8acmOAxOi4L9g1HZC362lhhhhJOyceEEaJ4mLyTjnf5gowgY4c3_ZtxYLBTuZmbjhPaecn46ANzh3DjC8zSdWNElxg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1f35315292.mp4?token=lyhWxVYZWMBBO9ZrXxG-Zj0AIm56Q99bWNUUffJ5RCI55tZ6Enw2NzLAY3mG2PGkbeQGYmt2t8JnFuxOofzKRMMuY235hQpRgU-CScP6iepoL3iCDVx_m52YGv6yWsGmCXk4_26e_Qd2iVyFV4VYDx3VCscRDBR1kCV33Q7fGJ5TbUTrP7xbOQhaNOFjKBni2aXEy_d2gSf0D1GvcwIVIqEaRABY4J2C8igpLvzo_4pVbm5DHRx7N9S0j0tvZeiv4oDfpp8LzozensyPK-7oSOtUzvKp9AJBiJCGn_2o96Bbmy7Wwxccgi373FyaNVzboyaA7zICWZ72m_o-Y5CGuU12jUG8Hr7S3-sJm55qp8ODK3oAbEGbhgyJ00qlyo2hCKuvxQt_Y8qeXwZMyLGAJY3cgAMhzn8rRAVSVaro-qE33dwd2EfGvP8pq8bb0UU5xE2exk9hAnZh-kj-okFfiWwVymlijlt4VfEluQQ32vl3ugDKBcG5xuQCa--guKD8l5qUg2iVx56hE5Zfzqo5DJ54KxH6wDkIPlXdVdWR1OAMPuuPODKSzl0KxkIu8kzlKXCAX27hkkqrVDwOx8acmOAxOi4L9g1HZC362lhhhhJOyceEEaJ4mLyTjnf5gowgY4c3_ZtxYLBTuZmbjhPaecn46ANzh3DjC8zSdWNElxg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">زلنسکی، رئیس جمهور اوکراین: در طول یک سال گذشته، فکر می‌کنم ما قوی‌تر شده‌ایم. افراد ما کار بزرگی انجام می‌دهند و به دیپلماسی فرصت می‌دهند. بدون یک موضع قوی در میدان نبرد، یک موضع قوی اوکراینی، فقط اولتیماتوم وجود خواهد داشت. اما امروز، دیپلماسی امکان‌پذیر است.
@WarRoom</div>
<div class="tg-footer">👁️ 112K · <a href="https://t.me/withyashar/22448" target="_blank">📅 20:27 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22447">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/64dc505262.mp4?token=rNx1sGGGjA9PEjur0xO3CSa9b_vQQOvVDqFdCNeBN_e9ICtab6IcJSGc_czq69UvUGt2CJAStfIJqI-O4JQQYphDC9CdPal3LM9Es1ZQKi2i8uuVT9gVnITW749aZFIuThmPmRBOGRDcED1HjCYs6EHTm8t6SgK_piRTX-Psb2txb74RNp8TchAO5L88uW7xhKfY35nqcr6xYR3rcnMvxeWoYYuWbagei4VY--miqV0vbQxP-ZnC27PH_GLEc_TJt8P6DoK53sIEDK2QDfiME9U9YMby0dPcQUe4RhUJrwWsx_niIe4JlWaorgu1t57QQd__XkI9a4xDQDltsKzQCA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/64dc505262.mp4?token=rNx1sGGGjA9PEjur0xO3CSa9b_vQQOvVDqFdCNeBN_e9ICtab6IcJSGc_czq69UvUGt2CJAStfIJqI-O4JQQYphDC9CdPal3LM9Es1ZQKi2i8uuVT9gVnITW749aZFIuThmPmRBOGRDcED1HjCYs6EHTm8t6SgK_piRTX-Psb2txb74RNp8TchAO5L88uW7xhKfY35nqcr6xYR3rcnMvxeWoYYuWbagei4VY--miqV0vbQxP-ZnC27PH_GLEc_TJt8P6DoK53sIEDK2QDfiME9U9YMby0dPcQUe4RhUJrwWsx_niIe4JlWaorgu1t57QQd__XkI9a4xDQDltsKzQCA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نتانیاهو: هنوز کارهای بیشتری برای انجام دادن باقی مانده است. این رژیم در ایران به پایان آن نزدیک است. آن ضعیف است، برای بقای خود می‌جنگد، لنگ‌لنگان حرکت می‌کند و هنوز مأموریتی برای تکمیل باقی مانده که ما عزم جزم بر انجام آن داریم. این امر در نهایت چهره خاورمیانه و مسیر تاریخ را تغییر خواهد داد
@WarRoom</div>
<div class="tg-footer">👁️ 108K · <a href="https://t.me/withyashar/22447" target="_blank">📅 20:26 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22446">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">کوشنر: رئیس جمهور ترامپ می‌خواهد چارچوبی برای دستیابی به صلحی جامع و پایدار ایجاد کند، نه فقط پایان دادن به جنگ فعلی در اوکراین.
@WarRoom</div>
<div class="tg-footer">👁️ 106K · <a href="https://t.me/withyashar/22446" target="_blank">📅 20:19 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22445">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">ویتکوف: ما برای از سرگیری روند مذاکرات به کیف آمدیم و از دستاوردهایمان احساس خوبی داریم و مشتاقانه منتظر دستاوردهای بیشتر هستیم. روسیه و اوکراین باید برای پایان دادن به جنگ امتیازاتی بدهند
ماموریت من و کوشنر این است که طرف‌های روسی و اوکراینی را گرد هم آوریم و شکاف‌ها را کم کنیم تا به یک تصمیم مشترک برسیم که به جنگ پایان دهد.
@WarRoom</div>
<div class="tg-footer">👁️ 109K · <a href="https://t.me/withyashar/22445" target="_blank">📅 20:19 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22444">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">پرواز پهپادهای ایرانی بر فراز تنگه هرمز!
سازمان دریایی بریتانیا (UKMTO) اعلام کرد که پهپادهای متعلق به نیروی دریایی سپاه ، در حال پرواز بر فراز کشتی‌های تجاری در تنگه هرمز هستند.
@WarRoom</div>
<div class="tg-footer">👁️ 109K · <a href="https://t.me/withyashar/22444" target="_blank">📅 19:59 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22443">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e697dcc2d7.mp4?token=cO4rHDKpMued3bMkQMV2AEdtHXIg4KVJl512d1tMRbqd_AFhgM6gTJ7BNk-t4YaqfI5n9Re57eXOamCzZlxh7hGR137Zn4sr7VWXmeit7XiFLQH6uI36N7hYokgFbOWGKEVWDneCguz-OOwoLG2tST-T1DE0CMeYpQ_3KW1cOf0tti2YMDr_BTEhcf1gw54czQSceaZIHgJt-fuIGnA83HGGOUKXK1LKsGJRb6SmT3-iuGjJJaclzc6mQwKu62Dn5xmFneBOE_QYdBAd_kUs-qBtLA_d9GXJLq_2-2Kp4OqNWtfjqt28uL2zzHcYPiyBDci4bl436rV0mt59s-aVSQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e697dcc2d7.mp4?token=cO4rHDKpMued3bMkQMV2AEdtHXIg4KVJl512d1tMRbqd_AFhgM6gTJ7BNk-t4YaqfI5n9Re57eXOamCzZlxh7hGR137Zn4sr7VWXmeit7XiFLQH6uI36N7hYokgFbOWGKEVWDneCguz-OOwoLG2tST-T1DE0CMeYpQ_3KW1cOf0tti2YMDr_BTEhcf1gw54czQSceaZIHgJt-fuIGnA83HGGOUKXK1LKsGJRb6SmT3-iuGjJJaclzc6mQwKu62Dn5xmFneBOE_QYdBAd_kUs-qBtLA_d9GXJLq_2-2Kp4OqNWtfjqt28uL2zzHcYPiyBDci4bl436rV0mt59s-aVSQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نتانیاهو، نخست وزیر اسرائیل، درباره ایران:
آنها به ما حمله نمی‌کنند. ایران از این کار اجتناب می‌کند و دلیلش را هم می‌داند: چون اگر این اشتباه را مرتکب شوند و به ما حمله کنند، ضربه‌ای خواهند خورد که حتی تصورش را هم نمی‌کنند.
@WarRoom</div>
<div class="tg-footer">👁️ 113K · <a href="https://t.me/withyashar/22443" target="_blank">📅 19:35 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22442">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Y6Cb5e4_wJpQBzLE3ZqsFcAQA3hU3Wi2k4vGD4sExLB2ne7lPEh6qib8SWFKtWCjOU1Hvz2jzgAyKQYCWCw4E-DJoLlS8YE7nS-rH07svpzXoTvFqU6-Y-nh05DKrwKyToBcOEmTj4cYVBB7931PWnNCmloU2wTpGmVsfi-Iu3ezqGv0FnSM4V4gSK9qsIaiI0en-37kaUvtHLiN3eEcD2PMzdR6uXjiYW9IT7iRbWEr76gjQE_hMBlu2b8FNLhAjWoMfHJ2NUNu3jGeBEhsaHTGhfK9DvFCPdmx9xlFCP0F5eKlutNQGcNw6d_xYlhT1t3MrG3gS_V-VSX1SgDbkw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ در تروث خطاب به رابرت دنیرو : حتی این احمق هم داره متوجه میشه!
@WarRoom</div>
<div class="tg-footer">👁️ 118K · <a href="https://t.me/withyashar/22442" target="_blank">📅 19:26 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22441">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qjYXLuhf8LhJQ3q7h3U-I9HzoS3qyxMPoeFhizSmPGYT7gmctUkPX2BFtIMwgjlJ5APuWUKu2A1bIc3Kau-Ry48HO0GPwgbwFnnZXO-rPupiBr_ZX4fgivh4MFEJ42w2LfFlQBnpSMZbBb_TMClTE8d7yshTitcXU_9vnQbnNkNnyZhMd8Y6_q7-5ijhqvoOKApY7F76Fqw5FmKVKH8ZlJtxMspMsblLLCy--dSqt4XRPbhcEkffoDy2lOUF2zLq93U2dF9AAorhc_gInHODpGhmzU-nrH4IUp-zAP8FRqGRtyreC_EUpoSKz6yxEiVOTs2VBoTPGWoDCm61TXV1RQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">استیو ویتکاف فرستاده ویژه آمریکا: از مذاکرات جدی و مهم با اوکراین راضی و به ادامه آن خوش‌بین هستم.
@WarRoom</div>
<div class="tg-footer">👁️ 108K · <a href="https://t.me/withyashar/22441" target="_blank">📅 18:59 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22440">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Q8ESYc7Wlj9qAIxjidvlOaUaq8YVwxskdBVfAHzltUTg_c3fXkBsmoV1mowE38lBXh7Cx5KnpzotM-Hbk0IOoNpz5_k2FfPxTAYcYF7Coyj1ACtpWZqkVxkpIo00g4Zn-ce20t9-T9tIdXVu_CdxF2YAct_p4fxC-LkSFfWgt4hhlPvGIVNO8kw6zjUw6CbHbxEuS6l0woFdU5dJl_x-nKtthNodrNG3RgA-gYTXioaMyFKeuugi7f1j5VzWULlYUyGV2iGdevX2a-9Z3Sbs61AlJ3YllnAeYFk0cEBlibidt8koo43mlWbn4D9nnm_8jmwsC3lfr3AwS7WFV6R57g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ رنگ موهاشو تیره تر کرد
@WarRoom
😁</div>
<div class="tg-footer">👁️ 118K · <a href="https://t.me/withyashar/22440" target="_blank">📅 18:42 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22439">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">وال استریت ژورنال :
سالانه میلیاردها دلار از منابع مالی ایران
با وجود تحریم‌ها، از طریق حساب‌های تسویه بانک‌های آمریکایی و بانک‌های خارجی دارای روابط کارگزاری با آمریکا جابه‌جا می‌شود. در سال ۲۰۲۴ حدود
۹ میلیارد دلار منابع مرتبط با ایران
از مسیر بانک‌های آمریکایی عبور کرده است. شرکت‌های پوششی و شبکه‌های پیچیده انتقال پول، شناسایی این تراکنش‌ها را دشوار کرده‌اند. مقام‌های آمریکایی با یک دوراهی روبه‌رو هستند؛
سخت‌گیری بیشتر ممکن است به جایگاه دلار آسیب بزند و تساهل بیشتر، مسیر انتقال پول ایران را بازتر کند.
@WarRoom</div>
<div class="tg-footer">👁️ 112K · <a href="https://t.me/withyashar/22439" target="_blank">📅 18:35 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22438">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">تلگراف: لیبی کلاینر، همسر یکی از سربازانی که پس از سرنگون شدن هواپیمایشان در غرب عراق کشته شدند، در یک پست در شبکه‌های اجتماعی نوشت که دولت ترامپ او را برای دریافت غرامت‌های مالی واجد شرایط ندانسته است، زیرا کنگره به طور رسمی جنگی را علیه ایران اعلام نکرده است.
تلگراف هم گفت پنتاگون از پرداخت غرامت به خانواده‌هایی که توسط ایران در خاورمیانه کشته شده‌اند، خودداری می‌کند، "زیرا آن را جنگ رسمی نمی‌داند."
اما نکته مهم این است که
پنتاگون در نهایت غرامتِ مرگ را کلاً قطع نکرده است.
پرونده‌ای که خبر از آن شروع شد، مربوط به بیوه یک افسر نیروی هوایی،
الکس کلینر
، بود. به او گفته شده بود فقط برخی مزایای مرتبط با منطقه جنگی، از جمله
combat pay
و معافیت مالیاتی، به دلیل اینکه «جنگ رسمی نیست» شامل حال خانواده نمی‌شود
@WarRoom</div>
<div class="tg-footer">👁️ 115K · <a href="https://t.me/withyashar/22438" target="_blank">📅 18:06 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22437">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TcpPx7Ix7e74GSsvqkDnrVCWsCN83dOTkVPy-GuGQHYOS15HBh8tjOiWJ3uRofvv9Nef81BlycD6JD0ZhxlVyxlH9C8kyhbHUHKcIs2Rs040JpDwaFQss73wB2sl7zC2QA-Pis4IVIDvMgA3WKVa5PocBcfnT4wKbJ5FaEG7Ln-p8pVz7IwBX95wbx6Ue7ZaDbmfDIMes-SR0GL5qJLGDJx6OgE2NIWpT09PWOnWl9xW3G7AunNWAhpHONnmDtg01J9Q_-IxD29ImyRUC4qA2k9HifsoK1zx4ac__j813loxLtSdkw5D4Lq3Yu0Jvwf2EZjUE1yXsfhHpS0M-D6Ocg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کوه کلنگ گز لا (Kuh-e Kolang Gaz La / Pickaxe Mountain)
در شهرستان نطنزِ استان اصفهان و حدود
۱.۵ تا ۲.۵ کیلومتر جنوب مجموعه هسته‌ای نطنز
قرار دارد. مختصات ثبت‌شده‌اش حدود
33.7051, 51.7081
است.
@WarRoom
https://maps.app.goo.gl/LJq8rZ2kNdve6xiVA?g_st=ic</div>
<div class="tg-footer">👁️ 111K · <a href="https://t.me/withyashar/22437" target="_blank">📅 18:00 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22435">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">گزارشهای بسیار از شنیده شدن صدای انفجاری مهیب در اراک
@WarRoom
🚨
🚨
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 112K · <a href="https://t.me/withyashar/22435" target="_blank">📅 17:41 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22434">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">اتاق جنگ با یاشار : با تماسی‌که با منابع داشتم نفتکش هایی که دیروز که آمریکا هدف قرار داد ۱ عدد با مالکیت ایران بوده ولی ۲ عدد آنها فقط در اجاره ایران بوده که حتمأ بیمه هم داشته اند
@WarRoom</div>
<div class="tg-footer">👁️ 113K · <a href="https://t.me/withyashar/22434" target="_blank">📅 17:31 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22433">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/smjUeSorQ2ONkRwubC_SZw8GUAh8I6wLhr47UJD2CTodffH1y9goBmHYhjfbQqo2o6xZ5_GN-hCy_jc8Pjt3nhnm85icMRsphaDk4xnG3QU8ZtoHRRNYU1pkFeOuYLWiQnbV19IT5KWtylfTCMtdXOM9uA_BABz1ZZ1x0LwTuz91ByWnq_xikH4oHoiE0fTSqoEATWt7cBSsorkhOqa9EjrBv1PdPWEvylANJRvKpI4QhAvYo2gpzk_ywxy2ncG6W4GgjClZrNPBDAo9VC9V59LYokTHMZt22pDHPa8cObHzFg8Hrnjj1OlxNwDa_0vcnlXb34sZzMYmyMtH-16MjQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شکار سوخترسان آمریکای توسط دیدبان اتاق جنگ با یاشار مانند پلنگ جگوار  @WarRoom</div>
<div class="tg-footer">👁️ 114K · <a href="https://t.me/withyashar/22433" target="_blank">📅 17:27 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22432">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/85e8d0bd6c.mp4?token=duWUBlPaTKiFRSE0v0xrTQnJWdkriBJ3d3IGDpFmzkiLDX3hxnHQ-NaZAexo0v4UA-ZZUaeFdJFFJAx1OT5GGuuoKbkdWnSfWFG2dF9XgVBR4q4XgMWk5NIn9j_snPDk7RkOWjDoafUvqUvaKPO8X47RQ1QeGg6se47a3CuRohj4fXfSH5lYXXskJuHIyqAp84ljWqGBQQE431Plv-e6JX14RjGawnfJNyw_F3pZ8MYsbXn3-FGKRrA1aJcBcTVtgMfRNr8WNDkgEVtDa7bxdQsebOksHsGH8eQMZ_c4B7rwOVpgPfE-orqzYah_AwLsG6GlYOO-pKf4J773EgwS_g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/85e8d0bd6c.mp4?token=duWUBlPaTKiFRSE0v0xrTQnJWdkriBJ3d3IGDpFmzkiLDX3hxnHQ-NaZAexo0v4UA-ZZUaeFdJFFJAx1OT5GGuuoKbkdWnSfWFG2dF9XgVBR4q4XgMWk5NIn9j_snPDk7RkOWjDoafUvqUvaKPO8X47RQ1QeGg6se47a3CuRohj4fXfSH5lYXXskJuHIyqAp84ljWqGBQQE431Plv-e6JX14RjGawnfJNyw_F3pZ8MYsbXn3-FGKRrA1aJcBcTVtgMfRNr8WNDkgEVtDa7bxdQsebOksHsGH8eQMZ_c4B7rwOVpgPfE-orqzYah_AwLsG6GlYOO-pKf4J773EgwS_g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شکار سوخترسان آمریکای توسط دیدبان اتاق جنگ با یاشار مانند پلنگ جگوار
@WarRoom</div>
<div class="tg-footer">👁️ 108K · <a href="https://t.me/withyashar/22432" target="_blank">📅 17:23 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22431">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c2dc5c16b1.mp4?token=C-l2YuohKZJ1iatKuMdMe_wbBZb5VRxP173km97rBT_kTdutinsuE4MMg-TvvGMwmIhyTT5EV4sXfx31GR0OMWG2ZGigMPXrfW4jCGBsSE30t6py2qB5sD00utGNX9sHMdZrnBnT0KiyKGs1E8xfa5V7EHJdKfdT3ySrFiXLbEppwt7rGZAaei_qO4-_b2UjjAssidYFwttygJOo8v_3zQDCVfI69Lu0BQ4ux01wZD_ZhjpvmwAl_ivMXN5X5To0FrBX_G7P3-S3BU1mimhL4YgD8NBU8PjaPgRhac7AVtINTcWpUsP_5gCoi5_mfUqUA3zlXDwr2XwChNFlb5t5EA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c2dc5c16b1.mp4?token=C-l2YuohKZJ1iatKuMdMe_wbBZb5VRxP173km97rBT_kTdutinsuE4MMg-TvvGMwmIhyTT5EV4sXfx31GR0OMWG2ZGigMPXrfW4jCGBsSE30t6py2qB5sD00utGNX9sHMdZrnBnT0KiyKGs1E8xfa5V7EHJdKfdT3ySrFiXLbEppwt7rGZAaei_qO4-_b2UjjAssidYFwttygJOo8v_3zQDCVfI69Lu0BQ4ux01wZD_ZhjpvmwAl_ivMXN5X5To0FrBX_G7P3-S3BU1mimhL4YgD8NBU8PjaPgRhac7AVtINTcWpUsP_5gCoi5_mfUqUA3zlXDwr2XwChNFlb5t5EA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تلگراف: حمله به بیت رهبری با موشک‌های «بلو اسپارو» انجام شد روزنامه تلگراف گزارش داده اسرائیل در حمله ۲۸ فوریه به مجتمع رهبری جمهوری اسلامی در تهران از موشک‌های هواپرتاب بالستیک Blue Sparrow استفاده کرده است؛ موشک‌هایی با وزنی نزدیک به ۲ تن که از جنگنده شلیک…</div>
<div class="tg-footer">👁️ 109K · <a href="https://t.me/withyashar/22431" target="_blank">📅 17:08 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22430">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LVgFMt1_e3aFyYEija5YnenQIs5u1IHCctKLCRJs9qThCFJ4U0ITNKxGFfFF6TkXVuIOhEUSFRQv5afdqmi2D8hlxny7M0VDgjqoAUbZovP68VHg7vM3qzhZPSTNxn78aqE6Zc2ihfD_ywqeDaoMdojoLPheboIFcffwkMmPrlGyE1yPtkU2Xu-IyfrL0Pk0inME-q6hKZyAVKbKfng-e5fkybqnQaxdC5qjGSjwLC3EaGZ8cQo2C4LfwF5tmhpHhMwW81bzXE5Cf1sjSqQxjys9ubO1dotq6PM2w0RB77rEHD9fVgS7Ii-cmNIYeu_yp_pcCGABpGtb_Dotu2u7Nw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تلگراف: حمله به بیت رهبری با موشک‌های «بلو اسپارو» انجام شد
روزنامه تلگراف گزارش داده اسرائیل در حمله ۲۸ فوریه به مجتمع رهبری جمهوری اسلامی در تهران از
موشک‌های هواپرتاب بالستیک Blue Sparrow
استفاده کرده است؛ موشک‌هایی با وزنی نزدیک به
۲ تن
که از جنگنده شلیک می‌شوند و پس از رسیدن به ارتفاع بالا با سرعت بسیار زیاد به سمت هدف شیرجه می‌روند.
گزارش‌های اولیه از پرتاب حدود
۳۰ بمب
به این مجتمع خبر داده بودند، اما گزارش‌های بعدی استفاده از موشک‌های Blue Sparrow را مطرح کردند. با این حال، مدل دقیق تمام مهمات استفاده‌شده هنوز به‌طور رسمی تأیید نشده است
@WarRoom</div>
<div class="tg-footer">👁️ 112K · <a href="https://t.me/withyashar/22430" target="_blank">📅 17:00 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22429">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">روزهای بسیار حساس در انتظار پرونده هسته‌ای ایران
؛ نشست فصلی شورای حکام آژانس بین‌المللی انرژی اتمی از فردا با حضور نمایندگان ۳۵ کشور برگزار می‌شود و پرونده هسته‌ای ایران یکی از محورهای اصلی آن خواهد بود. آمریکا و سه کشور اروپایی در این نشست چندروزه به دنبال تصویب قطعنامه‌ای برای ارجاع پرونده هسته‌ای ایران به شورای امنیت سازمان ملل متحد، به دلیل عدم پایبندی تهران به تعهدات پادمانی خود ذیل پیمان منع گسترش سلاح‌های هسته‌ای هستند
@WarRoom</div>
<div class="tg-footer">👁️ 114K · <a href="https://t.me/withyashar/22429" target="_blank">📅 16:14 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22428">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-footer">👁️ 118K · <a href="https://t.me/withyashar/22428" target="_blank">📅 15:59 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22427">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FLDG0jao6xlqayHmkngxf6rP3Em8muu0xxUzifWqPrhtT7XDGGyZyQlGRUP_1epKti9WLy2uxiWkMVVXvzmSJKzD49Ma58WUsXI--kdVXDYGNSq7p3mKq2EzTkfD22B92GvvCo78Yz8SD8Lqt2L-5pkmR27zCUjhkleJPqKKvEjxbprvAmoSiraD0rbjxzFRmqfD5bnQzbKH0SAHbFxDvZqk2_DogkvpG3A942fvEKbGl5bo7hcrSvCezx6raIOYIz0ejHZHuFwfdc9SFsDuDIuxHN9PSqVNogj14bsrwTF7rACoVvZIJzlbhMTMsexbCaxuYnN5FdY6kPzViE8vzg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وضعیت جوری شده که حتی اوستاد هم نمیتونه تحلیلش کنه
😂
خدایاااا بسته دیگه
@WarRoom</div>
<div class="tg-footer">👁️ 120K · <a href="https://t.me/withyashar/22427" target="_blank">📅 15:56 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22426">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IkIvkjSz1oIGy-xtgsBnrvvoWusCrN3NEl4oxUSLWYLnfTSg83o2-kzWaMgLeTrbeSM2tTc7njLO7r6NCKheCx44QFvXikZLFEsdfyVSApKra80oVP8SXyb-e5-_3gn_o5wuSbOISsTiHxZ3o37dyKAF8dXr6SjCYsiFATNwxPsGsK70adHsZPGCqLAScsSwA5oSpY9_kaTb-p3upj5LLjA6a0OSjP9QgYCWz1h72EgxRJ1-HBZ9JoD-xcSUEyh3N9sTNEXwgxJFOEbrw_e3JosfSWmFdMZn-XPWCky7VXOBXVZIg5xCaTBbqBnS6xFBcxBYBIVagrJnEh26cLcvbg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سنتکام : یک جت جنگنده رادارگریز F-35A نیروی هوایی ایالات متحده در حالی که نیروهای سنتکام همچنان به اجرای
محاصره دریایی علیه ایران ادامه می‌دهند
، بر فراز آب‌های منطقه‌ای گشت‌زنی می‌کند. تا امروز ۱۵ شهریور، نیروهای آمریکایی 92 کشتی تجاری را تغییر مسیر داده‌اند، 3 کشتی را غیرفعال کرده و 2 کشتی را توقیف کرده‌اند تا از رعایت دقیق این قوانین اطمینان حاصل کنند.
@WarRoom</div>
<div class="tg-footer">👁️ 120K · <a href="https://t.me/withyashar/22426" target="_blank">📅 15:27 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22425">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">منچ‌ اوسینت : از صبح امروز دست‌کم ۳ نفتکش هنگام تردد در مسیر جنوبی تنگه هرمز، پس از شلیک هشدار نیروی دریایی سپاه، تغییر مسیر داده و برگشتند.
@WarRoom</div>
<div class="tg-footer">👁️ 114K · <a href="https://t.me/withyashar/22425" target="_blank">📅 15:23 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22424">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">رویترز:
اوپک‌پلاس امروز در حال بررسی حفظ سیاست فعلی تولید نفت برای ماه اکتبر است و انتظار می‌رود افزایش بیشتر تولید پس از ماه سپتامبر متوقف شود. رویترز می‌گوید
جنگ ایران و اختلال در صادرات نفت از تنگه هرمز
یکی از عوامل مهم این تصمیم است؛ در عین حال اعضای اوپک‌پلاس همچنان پایین‌تر از سهمیه‌های تعیین‌شده تولید می‌کنند.
@WarRoom</div>
<div class="tg-footer">👁️ 118K · <a href="https://t.me/withyashar/22424" target="_blank">📅 14:47 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22423">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">خبرگزاری i24:
ارتش اسرائیل امروز یک رزمایش ناگهانی و چندجبهه‌ای با نام
«Breaking Dawn 2.0»
آغاز کرد. این رزمایش به دستور رئیس ستاد ارتش اسرائیل انجام می‌شود و هدف آن سنجش آمادگی نیروها برای سناریوهای همزمان در چند جبهه و تقویت توان ارتش برای مقابله با تهدیدهای ایران عنوان شده است. پیشتر افشا شد که
ایران در حال آماده‌سازی یک حمله هماهنگ و چندجبهه‌ای علیه اسرائیل
است که از نظر ابعاد و هماهنگی، با حمله ۷ اکتبر مقایسه شده است.
@WarRoom</div>
<div class="tg-footer">👁️ 117K · <a href="https://t.me/withyashar/22423" target="_blank">📅 14:44 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22422">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6c2c28d2cd.mp4?token=UIZbzPv3ASuN4C8ae-avc01FkT-LwGolg2CcNSF8VsImefaYkDks_tFssHLyRnPnPe1DKM0nslMrcVxHfz3JxkEV6AN8P_cpSiQ6JCFKcAW5TMXsb89_W2luCDbJovKsJw9_DTXkK1LaLCqvJE2upTLaUvWrihakV2MyhkbwTggzZYDkFkDlnGsCUqBWuJolfXi8dYcNOTaetUd9wUtO0ekfCFOk-6rHaNjRZ12SxEbbTqx93bDhCY_6fmn_5fjO0jwmvE-qYYvOLKVo7VD78xmvGFq-eGfUtIbDtRWf442X7EqRXdy2dcePMT7uBkpLMcu7spPT12xEc-pjBAOWTZWPjQqUN4dCNFsTVzrWUy73BQY0r0Dyu6zqiMeYWPsf3Muq1oGyywON76u2f6TKSPMovibd22rD8ldoFaSRPIBqzJZKscPHskqNBERvEN1HilI5wgBHtGCo9s-mfZZdxiN76MpWJ99VSH6J6Il7ud0JMjtnm08MgwHl-C1yMY5HeZHhTosfxNUlFtxUw8mQv0hNlDRYu-1YLxh0WKQNmdKRRnU3tVIsdbKpRQZmtlCBMWlrEPlCvnrF2CyH7jNK_7W4x4L2es9AZOal9wa3qOFUpCXGlIsGHexh5Q0j_rz9hNmAb87hv-IXQj08Teo2ZIe9q2OrobUbFpZkw28O5Kw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6c2c28d2cd.mp4?token=UIZbzPv3ASuN4C8ae-avc01FkT-LwGolg2CcNSF8VsImefaYkDks_tFssHLyRnPnPe1DKM0nslMrcVxHfz3JxkEV6AN8P_cpSiQ6JCFKcAW5TMXsb89_W2luCDbJovKsJw9_DTXkK1LaLCqvJE2upTLaUvWrihakV2MyhkbwTggzZYDkFkDlnGsCUqBWuJolfXi8dYcNOTaetUd9wUtO0ekfCFOk-6rHaNjRZ12SxEbbTqx93bDhCY_6fmn_5fjO0jwmvE-qYYvOLKVo7VD78xmvGFq-eGfUtIbDtRWf442X7EqRXdy2dcePMT7uBkpLMcu7spPT12xEc-pjBAOWTZWPjQqUN4dCNFsTVzrWUy73BQY0r0Dyu6zqiMeYWPsf3Muq1oGyywON76u2f6TKSPMovibd22rD8ldoFaSRPIBqzJZKscPHskqNBERvEN1HilI5wgBHtGCo9s-mfZZdxiN76MpWJ99VSH6J6Il7ud0JMjtnm08MgwHl-C1yMY5HeZHhTosfxNUlFtxUw8mQv0hNlDRYu-1YLxh0WKQNmdKRRnU3tVIsdbKpRQZmtlCBMWlrEPlCvnrF2CyH7jNK_7W4x4L2es9AZOal9wa3qOFUpCXGlIsGHexh5Q0j_rz9hNmAb87hv-IXQj08Teo2ZIe9q2OrobUbFpZkw28O5Kw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ولودیمیر زلنسکی : «روسیه اجازه نداد هیئت آمریکایی با هواپیما وارد اوکراین شود، با وجود اینکه فرودگاه‌های ما برای ورود آن‌ها آماده بودند.»
@WarRoom</div>
<div class="tg-footer">👁️ 114K · <a href="https://t.me/withyashar/22422" target="_blank">📅 14:43 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22421">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">گاردین:
لئون پانه‌تا، وزیر دفاع پیشین آمریکا، امروز هشدار داده جنگ ایران ممکن است
شش ماه دیگر نیز ادامه پیدا کند
. او سه مسیر احتمالی برای ترامپ مطرح کرده: عقب‌نشینی، ادامه جنگ فرسایشی و حملات مقطعی، یا تلاش برای به‌دست گرفتن کنترل تنگه هرمز.
@WarRoom</div>
<div class="tg-footer">👁️ 110K · <a href="https://t.me/withyashar/22421" target="_blank">📅 14:35 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22420">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e392ac131d.mp4?token=vEGr8LbM-yootfjElO-JQrIpVs6rgbpDyMgLqhXA0rvyZi1FgtilW7gLteEWvZR5y_DuN2oJeCA_TQw9PqoNQOxKgF4Fgdal2nyDmGavlj9X7br91VVlwEFspzqvDxvmPM514lzU1GVJR4C9u1oJ2JHiogDT4qCXmyUFANNW50L8BJIPBzFCCRBQNiJ3mLB1iXzTTgfNHa2_3PgYesJpm6B5ueDa3phxR1mx_1Gds-rAadrDt4UP4r4Q5F7RhHABQ900EBqyBsm5y8Jk4JYO9uSxXWpmnwugCADlqwRDmVt84Jx-dsqjnXbsnSyeC0ovlXKDEFyC2HWBkVQ_KvqHs37IcAbQjM3gIkhOhBpyi6pJkqZAMLIrHmeMPlEm2f5uhQ4ZICycjGjwqbG5zqH2ueNqC55Y4JAFqJ78QBvTjNblcgw389rLfd4IYQKbz_IqyBdxST6iU_9sKDOfeZ2r1i1inwQUcWjKAQ068qf4ymbdcD0LSLhu-DgG7r7l8tMpZdr56MXNB_ldMcx-yiA7-3Uw0Ms7U_71a0pMEFB0OCbODJiZFeLhNSQZ53IOOJs-b50JbbBkEv28AXqhDn52UOU4szITUK-qykiUGkXaMp6v-zWVDT-AOrR0pUuEPtihYtITSBLA0sRsK_UbFUGRKjIIAMIOaWVF4hhFNSKjxP0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e392ac131d.mp4?token=vEGr8LbM-yootfjElO-JQrIpVs6rgbpDyMgLqhXA0rvyZi1FgtilW7gLteEWvZR5y_DuN2oJeCA_TQw9PqoNQOxKgF4Fgdal2nyDmGavlj9X7br91VVlwEFspzqvDxvmPM514lzU1GVJR4C9u1oJ2JHiogDT4qCXmyUFANNW50L8BJIPBzFCCRBQNiJ3mLB1iXzTTgfNHa2_3PgYesJpm6B5ueDa3phxR1mx_1Gds-rAadrDt4UP4r4Q5F7RhHABQ900EBqyBsm5y8Jk4JYO9uSxXWpmnwugCADlqwRDmVt84Jx-dsqjnXbsnSyeC0ovlXKDEFyC2HWBkVQ_KvqHs37IcAbQjM3gIkhOhBpyi6pJkqZAMLIrHmeMPlEm2f5uhQ4ZICycjGjwqbG5zqH2ueNqC55Y4JAFqJ78QBvTjNblcgw389rLfd4IYQKbz_IqyBdxST6iU_9sKDOfeZ2r1i1inwQUcWjKAQ068qf4ymbdcD0LSLhu-DgG7r7l8tMpZdr56MXNB_ldMcx-yiA7-3Uw0Ms7U_71a0pMEFB0OCbODJiZFeLhNSQZ53IOOJs-b50JbbBkEv28AXqhDn52UOU4szITUK-qykiUGkXaMp6v-zWVDT-AOrR0pUuEPtihYtITSBLA0sRsK_UbFUGRKjIIAMIOaWVF4hhFNSKjxP0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏تفنگداران دریایی و ملوانان ناو آبراهام لینکلن، مشغول عشق و حال در کلابهای  پاتایا، تایلند.
@WarRoom</div>
<div class="tg-footer">👁️ 122K · <a href="https://t.me/withyashar/22420" target="_blank">📅 14:16 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22419">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">فایننشال تایمز:
آمریکا طی چهار ماه گذشته یک عملیات پرخطر و محرمانه برای مین‌روبی تنگه هرمز انجام داده؛ این عملیات با مشارکت نیروهای ویژه، قایق‌های رباتیک و زیردریایی‌های مجهز به سونار انجام شده است. با وجود اعلام ترامپ درباره پاک‌سازی تنگه، کارشناسان هنوز درباره ایمنی کامل مسیر تردید دارند.
@WarRoom</div>
<div class="tg-footer">👁️ 110K · <a href="https://t.me/withyashar/22419" target="_blank">📅 14:09 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22418">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">رویترز:
ایران اعلام کرده نیروهایش یک شناور بدون‌سرنشین آمریکایی را هنگام تلاش برای ورود به تنگه هرمز هدف قرار داده‌اند. آمریکا هنوز این ادعا را تأیید نکرده است. این اتفاق یک روز پس از حمله آمریکا به سه نفتکش ایرانی رخ داده است.
@WarRoom</div>
<div class="tg-footer">👁️ 113K · <a href="https://t.me/withyashar/22418" target="_blank">📅 14:03 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22417">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">افزایش ۲۰ هزار تومانی نرخ دلار  دولتی:
۱۰۰۰ دلار با کارت ملی نرخ ۲۲۰ هزار تومان
@WarRoom</div>
<div class="tg-footer">👁️ 114K · <a href="https://t.me/withyashar/22417" target="_blank">📅 13:53 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22416">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/025828335d.mp4?token=rTB-OzzHHNZqJuT0CqtJWk0rnIZkq7maWIhhm_qyzS3iEJ0ytZX8R1tdsvY2ExAEwkXW3aMFJ_uF0gl_PMrWJ-OUZ3PIrtio9fZk9yNKz3bT-SXHMEC9jhj4cQorYW7A80xFVbDlhbvdj99Ent_IaspNm0qn_eEiYE3a6ibgyZG9HtitN18GDa9IOggUm_F6X334H9q92gM4A97YIN3S7aSMJBZpjqvdBvsUgYVJjL7Q84HY5Wu7LbVuLR0TJTOt4aBaSr6t5QOurULZ3UAvFBGuJ4c-sXVGg_Cj_o5V2x5ISXY3I7EGpwcAxqfq_2lwI9ESPmdiVqeI9-Z0m3E7URZdxcb_05mdyq8Vp_kJ-OXawWh0apTRn0uqVKiVX2x81oQwdfAEYMzDevFA3ebOPi9bIHiSQ-r2baR_CAt6ihRAsyeusCi4ZzgtB0NmdN9tO7QyFomXYoR1-rlwDNR3EAPTOoKJFWJ7mCIKtPhBokMl05Zu1uda-oof7r4jx_bbZRhrGuq0ApoM_6ge5oygn80LF9kAMZbSkX0h-lH6yZudUZh_OR9XIFIgx1UfwItSRNW7o9gKuAzSrmBCwkrFvgkqa47O2CtpI-P7vpURSXtyP1bXh46fYImJTLOmbVGN8T6A-GDDNuXmwDto6czTZHLaFeX9JGu2abCd2-FkbQU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/025828335d.mp4?token=rTB-OzzHHNZqJuT0CqtJWk0rnIZkq7maWIhhm_qyzS3iEJ0ytZX8R1tdsvY2ExAEwkXW3aMFJ_uF0gl_PMrWJ-OUZ3PIrtio9fZk9yNKz3bT-SXHMEC9jhj4cQorYW7A80xFVbDlhbvdj99Ent_IaspNm0qn_eEiYE3a6ibgyZG9HtitN18GDa9IOggUm_F6X334H9q92gM4A97YIN3S7aSMJBZpjqvdBvsUgYVJjL7Q84HY5Wu7LbVuLR0TJTOt4aBaSr6t5QOurULZ3UAvFBGuJ4c-sXVGg_Cj_o5V2x5ISXY3I7EGpwcAxqfq_2lwI9ESPmdiVqeI9-Z0m3E7URZdxcb_05mdyq8Vp_kJ-OXawWh0apTRn0uqVKiVX2x81oQwdfAEYMzDevFA3ebOPi9bIHiSQ-r2baR_CAt6ihRAsyeusCi4ZzgtB0NmdN9tO7QyFomXYoR1-rlwDNR3EAPTOoKJFWJ7mCIKtPhBokMl05Zu1uda-oof7r4jx_bbZRhrGuq0ApoM_6ge5oygn80LF9kAMZbSkX0h-lH6yZudUZh_OR9XIFIgx1UfwItSRNW7o9gKuAzSrmBCwkrFvgkqa47O2CtpI-P7vpURSXtyP1bXh46fYImJTLOmbVGN8T6A-GDDNuXmwDto6czTZHLaFeX9JGu2abCd2-FkbQU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">کارگران تایلندی لایه‌هایی از جلبک را از ناو هواپیمابر آبراهام لینکلن پاک کردند این ناو هواپیمابر پس از استقرار طولانی در خاورمیانه، به طور کامل تمیز شد و بازدید خود از بندر لائم چابانگ تایلند را به پایان رساند و به جنوب چین باز میگردد تا در مسیر خود به سمت سن دیگو بازگردد.
@WarRoom</div>
<div class="tg-footer">👁️ 119K · <a href="https://t.me/withyashar/22416" target="_blank">📅 13:42 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22415">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">وال استریت ژورنال : ‏
در نبرد محاصره، زمان دیگر به نفع جمهوری اسلامی نیست
.‏ ایالات متحده به کشورهای خلیج فارس کمک می‌کند تا مقادیر قابل توجهی نفت را از منطقه خارج کنند و در عین حال مانع از انتقال محموله‌های تهران می‌شوند.
@WarRoom</div>
<div class="tg-footer">👁️ 118K · <a href="https://t.me/withyashar/22415" target="_blank">📅 13:18 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22414">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">قشقاوی در گفتگو با الجزیره: جنگ فعلی برای ایران یک جنگ موجودیتی است. ایران درخصوص پاسخ به حملات آمریکا به نفتکش های ایرانی ذره‌ای تردید نخواهد کرد!
@WarRoom</div>
<div class="tg-footer">👁️ 124K · <a href="https://t.me/withyashar/22414" target="_blank">📅 12:46 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22413">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">نیویورک‌تایمز: دولت ترامپ در حال بررسی طرحی است که بر اساس آن،
خانواده‌های متأهل با یک والد خانه‌دار
نیز بتوانند از یارانه فدرال مراقبت از کودکان استفاده کنند.
این کمک‌هزینه حدود
۹ هزار دلار به ازای هر کودک در سال
خواهد بود و از یک صندوق فدرال
۱۲ میلیارد دلاری
تأمین می‌شود که در حال حاضر عمدتاً برای کمک به والدین کم‌درآمد جهت کار یا تحصیل استفاده می‌شود.
@WarRoom</div>
<div class="tg-footer">👁️ 124K · <a href="https://t.me/withyashar/22413" target="_blank">📅 12:36 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22412">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">بیش از ۵۰ هزار نفر شامگاه پنجشنبه در مراسم مذهبی «سلخوت» در محوطه دیوار غربی (دیوار ندبه؛ بخشی از دیوار حائل محوطه کوه معبد در اورشلیم) گردهم آمدند و به دعا پرداختند. بنیاد میراث دیوار غربی اعلام کرد که از آغاز ماه «اِلول»، بیش از ۵۰۰ هزار نفر در مراسم سلخوت…</div>
<div class="tg-footer">👁️ 125K · <a href="https://t.me/withyashar/22412" target="_blank">📅 12:13 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22411">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">دیدبان اتاق جنگ با یاشار از جنوب خلیج فارس نزدیک تنگه : در همین لحظه سوخترسان آمریکای در حال سوخترسانی‌به دو جنگنده آمریکایی ، چیزی که ما در صفحه مانیتور نمیبینیم ! @WarRoom
🚨
🚨</div>
<div class="tg-footer">👁️ 127K · <a href="https://t.me/withyashar/22411" target="_blank">📅 11:22 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22410">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">بسنت: محاصره و تحریم‌ها قدرتمندترین فشار اقتصادی تاریخ علیه ایران است تنها حدود ۳۰ میلیون بشکه نفت خام ایران باقی مانده که چین هنوز آن را خریداری نکرده، این مقدار به زودی تمام می‌شود و دیگر نفتی نیست که چین بخواهد بخرد @WarRoom</div>
<div class="tg-footer">👁️ 129K · <a href="https://t.me/withyashar/22410" target="_blank">📅 10:46 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22409">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">بسنت: محاصره و تحریم‌ها قدرتمندترین فشار اقتصادی تاریخ علیه ایران است
تنها حدود ۳۰ میلیون بشکه نفت خام ایران باقی مانده که چین هنوز آن را خریداری نکرده، این مقدار به زودی تمام می‌شود
و دیگر نفتی نیست که چین بخواهد بخرد
@WarRoom</div>
<div class="tg-footer">👁️ 135K · <a href="https://t.me/withyashar/22409" target="_blank">📅 10:30 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22408">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DUqhK-8AaOFnaPvUIIEKzAKmDFVugqjgtl1qm5rRdFSO_vFTn1pdcLUYsRUMFuk7O8AH4fGutfTHzOoeiuPNKqrMfMC6DZkr51yhpUNTsOiU-6RLtIdi7DdmbbFMMi8GQqV70JfMaQ7EAX-x_1b5YAqED3ItyB424CM_p9sf_OK-JgOSUXVutUiLLu8Kbel6vd1opiiPbjTDLHgQuYswa9RXcIW80l4CGX_HDpZ7g9Q5k8QACOVca1umqleEGHVoYS0zJvOJ4iAk3zBr0Ank0xMptLYq4Va26rrOgEVRgRSsaaVuxWMjkajCt92RYcTef91OtMp8XlgvKDtPQK1mxw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ در تروث : بسیار تأسف‌بار است آنچه در اسپانیا در حال رخ دادن است؛ کشوری که
ه
یچ کنترلی بر
مرزهای
خود ندارد. واو!
@WarRoom</div>
<div class="tg-footer">👁️ 132K · <a href="https://t.me/withyashar/22408" target="_blank">📅 10:23 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22407">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">دنیس راس، مذاکره‌کننده و فرستاده پیشین آمریکا در خاورمیانه، هشدار داده است که
احتمال دارد تنش‌ها در خاورمیانه به‌زودی تشدید شود
.
@WarRoom</div>
<div class="tg-footer">👁️ 136K · <a href="https://t.me/withyashar/22407" target="_blank">📅 07:39 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22406">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">مارک لوین در واکنشه حمله آمریکا به نفتکش در جزیره خارگ : «در حال نزدیک شدن به مهم‌ترین هدف اقتصادی در ایران؛ منبع مادر ثروت.»
@WarRoom</div>
<div class="tg-footer">👁️ 138K · <a href="https://t.me/withyashar/22406" target="_blank">📅 07:20 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22405">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">نیویورک‌پست:ارزیابی‌های اطلاعاتی اسرائیل حاکی است ایران با هماهنگی حزب‌الله، حوثی‌ها و شبه‌نظامیان عراقی در حال تدارک حمله‌ای چندجبهه‌ای و مشابه ۷ اکتبر علیه اسرائیل است. به‌گفته جروزالم‌پست، سپاه پاسداران رزمایش مشترک با نیروهای نیابتی و تولید پهپاد و موشک را افزایش داده است.
@WarRoom
🚨</div>
<div class="tg-footer">👁️ 145K · <a href="https://t.me/withyashar/22405" target="_blank">📅 06:54 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22404">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">مقام اسرائیلی : برای تحویل جسد اعضای حزب الله در تپه علی الطاهر، حزب‌الله باید پول موشک های شلیک شده را بدهند
@WarRoom</div>
<div class="tg-footer">👁️ 150K · <a href="https://t.me/withyashar/22404" target="_blank">📅 06:39 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22403">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">آکسیوس: سپاه پاسداران در حملات اخیر خود در مجموع ۶ کشتی را هدف قرار داده است
؛ سه نفتکش و سه کشتی. بر اساس گزارش آکسیوس، سه نفتکش در حال عبور از مسیرهای غیرمجاز یا خارج از مسیر تعیین‌شده در تنگه هرمز هدف حملات موشکی قرار گرفتند و سه شناور آمریکایی نیز هدف حملات ایران قرار گرفتند. در آخرین مورد، ایران موشک‌های بالستیک به سمت دو ناو نیروی دریایی آمریکا شلیک کرد که به گفته سنتکام، یک ناو هواپیمابر و یک ناوشکن مجهز به موشک‌های هدایت‌شونده توانستند از این حملات عبور کنند و آسیبی به نیروهای آمریکایی وارد نشد. در واکنش، نیروهای آمریکایی سه نفتکش ایرانی را هدف قرار دادند
@WarRoom</div>
<div class="tg-footer">👁️ 145K · <a href="https://t.me/withyashar/22403" target="_blank">📅 06:35 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22402">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">هم اکنون ۲ پرتاب از سیریک
@WarRoom
🚨
🚨</div>
<div class="tg-footer">👁️ 152K · <a href="https://t.me/withyashar/22402" target="_blank">📅 00:37 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22401">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/35ecaf8975.mp4?token=JaMn61fHjrpr2fUnYksRJiXhaO6bthodvqE--r99ylUcc4hTmdgDiWhxj5dAv64I9u-ogwTzdduNhrKS-So0bDhghUVJHL5yEVUzHciBvjm_TlvdHTPMEZ6-nuCNs_DOj6UYPTNNYNvTP72x4tLDqr85S9mBEOAVgPOHhgvKrYt_qJqC9sc7LBUkFpkvjWUmMKBOVQHPdzRYQjW2hY1lQyWhodDgynQZlZLebNum5kpJ0gMsIj_SOrMRsvLH81JZuZxbpx9YEnEo6GV8e-IToupI6OzDNb8RBso4J3A_UxmtQulck0Lakkv3QIyicpfAs_DK8nnw5LdgtBxWZ8DhzIkFpEsR8uiSKu7FXRuEiyw66umXcH-kDlVEGYk7qxHdXCabuYq3KGjxnQIYr8tZtX4hDHqR-NasBk0PqQBtMIKp5A9Ia7yez_fI-iETNzffosxbpE78VByXbj4_xQiIcfpkiXki8fFSMtz9QP71jtYGxpggcFL2e2eyYGdjXKB-LkGLcPTeT-PSSap3Xa0WIit5O6KG8BNcM6wVUrBG3cWN7ZIl4MH6LvU7c8rZfXpkKMYNrVqIewz_VoDSlPtXHVXaiaxlayhIAUb51qHa38cwQEfR2LFefhdT2sAtng3OFR9PA-rJvWglsTaqU3aA57pUK2M0BTrkUNl9oZSsdMQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/35ecaf8975.mp4?token=JaMn61fHjrpr2fUnYksRJiXhaO6bthodvqE--r99ylUcc4hTmdgDiWhxj5dAv64I9u-ogwTzdduNhrKS-So0bDhghUVJHL5yEVUzHciBvjm_TlvdHTPMEZ6-nuCNs_DOj6UYPTNNYNvTP72x4tLDqr85S9mBEOAVgPOHhgvKrYt_qJqC9sc7LBUkFpkvjWUmMKBOVQHPdzRYQjW2hY1lQyWhodDgynQZlZLebNum5kpJ0gMsIj_SOrMRsvLH81JZuZxbpx9YEnEo6GV8e-IToupI6OzDNb8RBso4J3A_UxmtQulck0Lakkv3QIyicpfAs_DK8nnw5LdgtBxWZ8DhzIkFpEsR8uiSKu7FXRuEiyw66umXcH-kDlVEGYk7qxHdXCabuYq3KGjxnQIYr8tZtX4hDHqR-NasBk0PqQBtMIKp5A9Ia7yez_fI-iETNzffosxbpE78VByXbj4_xQiIcfpkiXki8fFSMtz9QP71jtYGxpggcFL2e2eyYGdjXKB-LkGLcPTeT-PSSap3Xa0WIit5O6KG8BNcM6wVUrBG3cWN7ZIl4MH6LvU7c8rZfXpkKMYNrVqIewz_VoDSlPtXHVXaiaxlayhIAUb51qHa38cwQEfR2LFefhdT2sAtng3OFR9PA-rJvWglsTaqU3aA57pUK2M0BTrkUNl9oZSsdMQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سه پا : آبرومون امروز رفت فعلا این
تصاویر منتشر نشده از رصد و اقدام علیه شناور های متخلف
رو ببینید
@WarRoom</div>
<div class="tg-footer">👁️ 152K · <a href="https://t.me/withyashar/22401" target="_blank">📅 00:32 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22400">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ec62b949f8.mp4?token=U9RP0AuIZ2xbvMZW6EzZr25s_PmneSlexvipn9jqfxcNGKrc5OQaJnTumR1DnEs7i5WWGdmI3DHpPol5tNTm2e7GPyz5uJMRbeg8idtx_KNKtXnwSYfF0ahmiG-emKkSFSwDXOi5uHXkEQ6WaQU9C5oRTtX2bmRnhTsv_4TWoCGAkCSvU0MBod2N7Lup9fyr9t0q3tKdSPxW7hnBg2a3C331M4lTJhIKoTX6_sPtgs9Xq2DzW0pEiqLKDDjdjwEE6imi24Ef9wxJ-lFOMU425WIfOpv_YoGplra6BtpybPNgk0tleiW4ZOIT8DHsDT_qr7Vq9k_Dbb2vHJ27XBq9LQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ec62b949f8.mp4?token=U9RP0AuIZ2xbvMZW6EzZr25s_PmneSlexvipn9jqfxcNGKrc5OQaJnTumR1DnEs7i5WWGdmI3DHpPol5tNTm2e7GPyz5uJMRbeg8idtx_KNKtXnwSYfF0ahmiG-emKkSFSwDXOi5uHXkEQ6WaQU9C5oRTtX2bmRnhTsv_4TWoCGAkCSvU0MBod2N7Lup9fyr9t0q3tKdSPxW7hnBg2a3C331M4lTJhIKoTX6_sPtgs9Xq2DzW0pEiqLKDDjdjwEE6imi24Ef9wxJ-lFOMU425WIfOpv_YoGplra6BtpybPNgk0tleiW4ZOIT8DHsDT_qr7Vq9k_Dbb2vHJ27XBq9LQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سفیران آمریکایی، ویتکاف و کوشنر، پس از سه ساعت مذاکره با پوتین، کاخ کرملین را ترک کردند.
@WarRoom</div>
<div class="tg-footer">👁️ 153K · <a href="https://t.me/withyashar/22400" target="_blank">📅 00:20 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22399">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">رسانه های رژیم : تمامی افرادی که در کلیپ رژه طرفداران سازمان تروریستی مجاهدین خلق در کوچه پس کوچه های‌کرج، حضور داشته‌اند، توسط نیروهای امنیتی شناسایی و دستگیر شدند
@WarRoom</div>
<div class="tg-footer">👁️ 155K · <a href="https://t.me/withyashar/22399" target="_blank">📅 00:13 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22398">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">رئیس اداره اخبار مجلس:
۵۰ روز است که یه بشکه نفت هم نفروختیم.
هیچ کالایی هم از جنوب وارد کشور نشده‌. محاصره اقتصادی بدجور دستمونو بسته.
@WarRoom</div>
<div class="tg-footer">👁️ 152K · <a href="https://t.me/withyashar/22398" target="_blank">📅 23:46 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22397">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">زاکانی: وصیت نامه آقا با خودش تو بمبارون از بین رفته
@WarRoom
😁</div>
<div class="tg-footer">👁️ 155K · <a href="https://t.me/withyashar/22397" target="_blank">📅 23:10 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22396">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">نتانیاهو: «اگر ما علیه ایران اقدام نمی‌کردیم، ایران امروز بمب‌های اتمی داشت که قصد نابودی ما را داشتند.
حالا آنها دوباره تلاش خواهند کرد. آنها دوباره تلاش می‌کنند و دوباره تلاش خواهند کرد تا محوری را که ما شکستیم، بازسازی کنند.»
@WarRoom</div>
<div class="tg-footer">👁️ 154K · <a href="https://t.me/withyashar/22396" target="_blank">📅 23:09 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22395">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">قالیباف : بستن تنگه هرمز به ضرر ایران شد.
@WarRoom
😁</div>
<div class="tg-footer">👁️ 156K · <a href="https://t.me/withyashar/22395" target="_blank">📅 23:03 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22394">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">پرتاب۳ موشک از سیریک سمت تنگه ( رادار ندارن موش کور شدن ول میدن )
@WarRoom
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 152K · <a href="https://t.me/withyashar/22394" target="_blank">📅 22:43 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22393">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">صدای انفجار از تنگه ، امشب تنگه گیسو گیس کشیه
🚨
🚨
🚨
@WarRoom</div>
<div class="tg-footer">👁️ 152K · <a href="https://t.me/withyashar/22393" target="_blank">📅 22:38 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22392">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">حقیقت یاب اتاق جنگ : آنچه سنتکام امروز ، تأیید کرده این است که سپاه پاسداران به سمت
دو ناو آمریکایی
موشک بالستیک شلیک کرده و سنتکام هم می‌گوید
ناو هواپیمابر و یک ناوشکن
موشک‌ها را جاخالی داده‌اند و هیچ نیروی آمریکایی آسیب ندیده است. در واکنش، آمریکا به سه نفتکش ایرانی حمله کرده است. بنابراین رسانه های زرد که به دروغ نوشته‌اند
«جورج واشنگتن به‌دلیل موشک‌های ایرانی عقب‌نشینی کرد»
، اصلا در خبر رسمی
نیامده
کدام ناو بوش یا واشنگتن
وبعد هم اگر
تغییر موقعیت عملیاتی یا دور شدن تاکتیکی ناو از محدوده خطر
انجام شود هم نرمال است ولی سنتکام چیزی‌نگفته است که ناو منطقه را ترک کرده یا به‌دلیل اصابت/ترس از موشک‌ها عقب‌نشینی کرده باشد !!!
@WarRoom</div>
<div class="tg-footer">👁️ 152K · <a href="https://t.me/withyashar/22392" target="_blank">📅 22:28 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22391">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">عضو هیئت‌رئیسه مجلس : هم اکنون احتمال حمله به اسرائیل هم وجود دارد.
@WarRoom
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 148K · <a href="https://t.me/withyashar/22391" target="_blank">📅 22:20 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22390">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-footer">👁️ 147K · <a href="https://t.me/withyashar/22390" target="_blank">📅 21:20 · 14 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>

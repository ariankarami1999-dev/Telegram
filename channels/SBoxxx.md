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
<img src="https://cdn4.telesco.pe/file/toS-3r9JULwgq0mtrAOqJDugmd8LDspRwUTrGOFLhzFGnCE05brP29GW9LCPYBlxBNXxTDqz7hdS63gLs25IpCjKSmGxKDPqhhW8mPKpHEbnWovwaGwpWs8vQ498xLKGTxNtDGgYXtvZQtFZOZgIscUirM4BF8h89bTz-8Pxk1z9xUZSULNgeGYXQ1mxI6UZIyVtD2IGNAFV0bfDahdQx39rKLvfqC9BslTffmP2X6XRDfH_hCdmI5fdiEiElX1_V3JdUfl63O7Zn17hGQntPwm3Zpn6HC2IM6FCknJACSSFAZ3L1NXeygKKHcCfcruec3b6bOH0fBNiBX8NC-xOVg.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Secret Box</h1>
<p>@SBoxxx • 👥 9.86K عضو</p>
<a href="https://t.me/SBoxxx" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 تاریخ، ژئوپولیتیک و بازارهای مالی</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-11 19:19:40</div>
<hr>

<div class="tg-post" id="msg-16838">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">حالا توجه کنید که در همین مدت که آمریکایی ها دهها کشتی تجاری را از تنگه هرمز عبور داده اند، محاصره دریایی شان را کماکان اعمال میکنند و این یعنی کارتی که ایران دارد (تنگه هرمز) در حال کم اثر شدن است اما کارتی که آنها دارند (محاصره دریایی) کماکان در دستشان باقی…</div>
<div class="tg-footer">👁️ 209 · <a href="https://t.me/SBoxxx/16838" target="_blank">📅 19:20 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16837">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">محسن رضایی: صبر ایران حدی دارد
تنگه هرمز تحت مدیریت ایران است. اجازه تداوم محاصره دریایی را نخواهیم داد و تشدید تنش در لبنان هم تحمل نخواهد شد. صبر نیروهای مسلح جمهوری اسلامی ایران حدی دارد.</div>
<div class="tg-footer">👁️ 390 · <a href="https://t.me/SBoxxx/16837" target="_blank">📅 19:17 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16836">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hdabcsrtYtyBENUsFBcYi-gWxHZrg00kphLaEc6ARZsFCtvESUnrcCJyZI1bxNSK0f5wmVW20_kMYRQR2s7eWuwBs3hJQVXhVP2qnJfngh_xZ3afiMfPq4LP5UE2Isp9ab6iTS015vg08Ga-KKc-S2sLB2YJUJWrUmq5JPLAidaQPqLVjYdzu_MshlmxWSwhAodMdoM3mg6twFKHzjHMGBoq6h5oabSCdn56NKcY9nF6uGQzuoYihfiGu00im_vW3L6Uiux3XH6RmPfG9Juc6Q4AgOlodvjU1gbxxaXAu8z-R0uq-v7ecD4QUXQfICdS3ckxJO2t3uegPhvKj9y02A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ایده خوبی است بسم الله!</div>
<div class="tg-footer">👁️ 1.84K · <a href="https://t.me/SBoxxx/16836" target="_blank">📅 18:17 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16835">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">عراقچی: نقض آتش بس در یک جبهه، نقض آتش‌بس در تمام جبهه‌هاست  آتش‌بس میان ایران و  آمریکا، بدون هیچ ابهامی، آتش‌بسی در تمامی جبهه‌ها، از جمله لبنان، محسوب می‌شود.  نقض این آتش‌بس در هر یک از جبهه‌ها، به منزلۀ نقض آن در تمامی جبهه‌هاست.  آمریکا و اسرائیل مسئول…</div>
<div class="tg-footer">👁️ 2.29K · <a href="https://t.me/SBoxxx/16835" target="_blank">📅 18:10 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16834">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">قیمت کنونی ۱۶۹</div>
<div class="tg-footer">👁️ 1.95K · <a href="https://t.me/SBoxxx/16834" target="_blank">📅 18:08 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16833">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">با این جهش وحشتناک قیمت نفت در همین یکی دو ساعت، ترامپ مجبور به عقب نشینی است.</div>
<div class="tg-footer">👁️ 2.33K · <a href="https://t.me/SBoxxx/16833" target="_blank">📅 17:44 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16832">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">خواننده Secret Box از‌ همان روز توافق میدانست که اندوه لبنان خواهدکشت ما را.</div>
<div class="tg-footer">👁️ 2.36K · <a href="https://t.me/SBoxxx/16832" target="_blank">📅 17:40 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16831">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">خب در توافق بحث پایان جنگ در لبنان هم مطرح شده و لذا میتوان گفت این بندش هیچ وقت اجرا نخواهدشد.</div>
<div class="tg-footer">👁️ 2.37K · <a href="https://t.me/SBoxxx/16831" target="_blank">📅 17:38 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16830">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">ایران اعلام کرد که آماده بستن کامل تنگه هرمز و تنگه باب‌المندب است اگر اسرائیل حملات به بیروت را متوقف نکند</div>
<div class="tg-footer">👁️ 2.5K · <a href="https://t.me/SBoxxx/16830" target="_blank">📅 17:31 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16829">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">سخنگوی وزارت خارجه:
ما حق دفاع مشروع در برابر نقض آتش‌بس توسط آمریکا را داریم و امروز هم مبدأ تجاوز به خاک کشور را هدف قرار دادیم.</div>
<div class="tg-footer">👁️ 2.49K · <a href="https://t.me/SBoxxx/16829" target="_blank">📅 17:28 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16828">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">عراقچی: نقض آتش بس در یک جبهه، نقض آتش‌بس در تمام جبهه‌هاست
آتش‌بس میان ایران و  آمریکا، بدون هیچ ابهامی، آتش‌بسی در تمامی جبهه‌ها، از جمله لبنان، محسوب می‌شود.
نقض این آتش‌بس در هر یک از جبهه‌ها، به منزلۀ نقض آن در تمامی جبهه‌هاست.
آمریکا و اسرائیل مسئول پیامدهای هرگونه نقض این آتش‌بس خواهند بود.</div>
<div class="tg-footer">👁️ 3.17K · <a href="https://t.me/SBoxxx/16828" target="_blank">📅 15:02 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16827">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">برکشایر هاتاوی اکنون بیش از هر زمان دیگری در تاریخ خود پول نقد در اختیار دارد</div>
<div class="tg-footer">👁️ 3.23K · <a href="https://t.me/SBoxxx/16827" target="_blank">📅 14:53 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16826">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">بنیامین نتانیاهو به همراه وزیر دفاع اسرائیل دستور حمله به ضاحیه بیروت را اعلام کردند و گفته می شود ستونی طولانی و عظیم از خودروهای مردم به سمت مناطق شمالی بیروت و بیرون از آن در حرکت هستند.</div>
<div class="tg-footer">👁️ 3.48K · <a href="https://t.me/SBoxxx/16826" target="_blank">📅 13:20 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16825">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">قالیباف:
محاصره دریایی و تشدید جنایات جنگی در لبنان، گواه عدم پایبندی واشنگتن به آتش‌بس است و هر گزینه‌ای بهایی دارد که پرداخت خواهد شد.</div>
<div class="tg-footer">👁️ 3.55K · <a href="https://t.me/SBoxxx/16825" target="_blank">📅 13:05 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16824">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">بنیامین نتانیاهو به همراه وزیر دفاع اسرائیل دستور حمله به ضاحیه بیروت را اعلام کردند و گفته می شود ستونی طولانی و عظیم از خودروهای مردم به سمت مناطق شمالی بیروت و بیرون از آن در حرکت هستند.</div>
<div class="tg-footer">👁️ 3.81K · <a href="https://t.me/SBoxxx/16824" target="_blank">📅 11:54 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16823">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">️صدای انفجارها در بندرعباس کنترل شده است
صدا‌هایی که دقایقی قبل مردم در سطح شهر بندرعباس شنیدند ناشی از امحای مهمات عمل نکرده است.
روابط عمومی استانداری هرمزگان اعلام کرد: انفجار‌های صورت گرفته کنترل شده است و تا ۷۲ ساعت ادامه دارد و مردم نگران نباشند.
این انفجارهای کنترل شده از دیروز آغاز شده است و تا فردا سه شنبه ادامه دارد.</div>
<div class="tg-footer">👁️ 3.86K · <a href="https://t.me/SBoxxx/16823" target="_blank">📅 10:09 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16822">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">این جریان استعفاهای پزشکیان هم مثل خداحافظی های کریم باقری است.
سبحان الله!</div>
<div class="tg-footer">👁️ 3.85K · <a href="https://t.me/SBoxxx/16822" target="_blank">📅 09:34 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16821">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">حالا توجه کنید که در همین مدت که آمریکایی ها دهها کشتی تجاری را از تنگه هرمز عبور داده اند،
محاصره دریایی شان را کماکان اعمال میکنند
و این یعنی کارتی که ایران دارد (تنگه هرمز) در حال کم اثر شدن است اما کارتی که آنها دارند (محاصره دریایی) کماکان در دستشان باقی است.</div>
<div class="tg-footer">👁️ 3.96K · <a href="https://t.me/SBoxxx/16821" target="_blank">📅 09:16 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16820">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">ارتش آمریکا به ۷۰ کشتی تجاری کمک کرده تا در ۳ هفته گذشته با خاموش کردن سیستم GPS خود از تنگه هرمز عبور کنند.  به نظرم این رادارهای ما را میزنند تا توان رهگیری اهداف متحرک از سپاه سلب بشود و سپس کشتی ها را خارج می‌کنند.</div>
<div class="tg-footer">👁️ 3.92K · <a href="https://t.me/SBoxxx/16820" target="_blank">📅 09:14 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16819">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">ترامپ:
ایران واقعاً می‌خواهد معامله‌ای انجام دهد و این معامله برای ایالات متحده آمریکا و کسانی که با ما هستند، بسیار خوب خواهد بود.
اما آیا دموکرات‌ها و جمهوری‌خواهان به ظاهر غیر میهن‌پرست درک نمی‌کنند که وقتی سیاستمداران فرصت‌طلب بارها و بارها با سطحی بی‌سابقه به صورت منفی «نق» می‌زنند و می‌گویند که من باید سریع‌تر حرکت کنم، یا کندتر، یا به جنگ بروم، یا به جنگ نروم، یا هر چیز دیگری، برای من بسیار دشوارتر است که به درستی شغلم را انجام دهم و مذاکره کنم؟
فقط بنشینید و آرام باشید، همه چیز در نهایت خوب پیش خواهد رفت - همیشه همینطور بوده است!
رئیس‌جمهور DJT</div>
<div class="tg-footer">👁️ 3.73K · <a href="https://t.me/SBoxxx/16819" target="_blank">📅 08:40 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16818">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/I9X8vdTs_D87qjYGJPMqDBMoC1n8zKteIbCTBcS-UFwPmJr1l5RwLsR6r2VIBBYk2Ht6bxGl3z4IW-byjPhWw4dt5UburelPHmoTtJzWlY35R6-4DqlvC_sJcIAFf06UvFJORUc5D9pVhS50YYP9gHwSXCnCGq1zm9AShDL4KqIdanJurQJfUnmMTLSj7T5aep8X6Cx5GM-gO7zpvL5RbSIhiHOC_NToVbwIht_mCMs_ZNYZxUexxSmnt0h24T-JecSE3X61actYsqcNhdSWLSVrt-Bf7sgwRQelI1dm5_UprNqUVEWq-tmVn3BefWqUwlJYMm-XS5s60oVW44GUog.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حملات آمریکا به رادارهای ایرانی و پاسخ سپاه   مرکز فرماندهی مرکزی (CENTCOM) اعلام کرد که حملاتی را به عنوان «ضربه‌های دفاع از خود» علیه سایت‌های راداری و فرماندهی در گورک و جزیره قشم انجام داده است.  در پاسخ، نیروی هوافضای سپاه پاسداران پایگاه هوایی که حمله…</div>
<div class="tg-footer">👁️ 3.7K · <a href="https://t.me/SBoxxx/16818" target="_blank">📅 08:38 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16817">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SYL0l3wCNB1cAJyiK0OLpcwiHF-C_t5N7duBBiTnLTalIQqfhb-DOEyR4WtzC6EV8L0egaKb__Odl_qEyK_c_Lhhlodx6q9LuE19KfxBHme10bsEnTEP7Zpyj57-tqbj4hXNpBPUJ7NyX-5hW0gjIHm-OUqp6Azr2cnPyrt93LVEUa_BpcQ3pKhPHttBBF2tSiFD41zGMqhqYe-b0NnyONp6aemZV2GMuxrvWchmREg139MtaAJwY9b65a0BYxZXfYmVdy-QEe0n-hZ2GEm2Z33GJVcCp9ZRMvBV9Fa9tOmPNmmdFMVGSwAcRXJxAZRuJKHbm3v_OEKmQ1aNUa7DWw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">با این وضعیت به نظرم دوشنبه نفت با گپ مثبت باز بشود</div>
<div class="tg-footer">👁️ 3.64K · <a href="https://t.me/SBoxxx/16817" target="_blank">📅 08:30 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16816">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">حملات آمریکا به رادارهای ایرانی و پاسخ
سپاه
مرکز فرماندهی مرکزی (CENTCOM) اعلام کرد که حملاتی را به عنوان «ضربه‌های دفاع از خود» علیه سایت‌های راداری و فرماندهی در گورک و جزیره قشم انجام داده است.
در پاسخ، نیروی هوافضای سپاه پاسداران پایگاه هوایی که حمله آمریکا از آنجا آغاز شده بود را هدف قرار داد و گفت که «اهداف پیش‌بینی شده نابود شدند».
ارتش کویت نیز این وسط از فعالیت‌های پدافند هوایی در منطقه گزارش داد.</div>
<div class="tg-footer">👁️ 3.67K · <a href="https://t.me/SBoxxx/16816" target="_blank">📅 08:28 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16815">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">دیسکامبوباتور.pdf</div>
  <div class="tg-doc-extra">200.8 KB</div>
</div>
<a href="https://t.me/SBoxxx/16815" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">این تصویر را ترامپ دیروز پست کرده بود.  کلمه discombobulator را پیشتر ترامپ در توصیف سلاح مخفی سری که آمریکا در جریان ربودن مادورو استفاده کرد به کار برده بود و دیروز دوباره گویا به این سلاح اشاره کرده است.  گویا این سلاح به نوعی در مختل کردن کلیه دستگاه های…</div>
<div class="tg-footer">👁️ 4.01K · <a href="https://t.me/SBoxxx/16815" target="_blank">📅 00:21 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16814">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EYGplkvGiWzdhQoiYeaMAxBk_gWk-8t-BxI9PqH5Bvp2qFXFVu3NKJjHjleLzHLHMVUwHwSqa4wAtYe2tM5azNrtr6q1ZiJ7TVdbw-qH8fhXeVbv_-r9u5O0tN81AxSu12Codr8xtTGIFlGD9tjxEH8hHcYU0mOg5Gf1vBoINrkNEHCukFbk8eA3kHDofJBkFEH3b1R0hQWQk6_2ezsxVOdyS6dzQVvkVc-8Y2zmNjs4SnWKUmrFZvg_Xdj9EVOY-FYqm6IYCqyGBJCpxlYRmTGapTdzUjRdQ2jXsH1roW4oxDSeLqypCGF3Guc4x-pKDg5UXDMsVbB3ldFIogY_1A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آیا در تهران نوعی خرابی وسایل برقی، نوسان جریان برق، ناپایداری نت حس می کنید؟  بله:
👍🏻
خیر:
👎🏻</div>
<div class="tg-footer">👁️ 4.27K · <a href="https://t.me/SBoxxx/16814" target="_blank">📅 23:57 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16813">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">آیا در تهران نوعی خرابی وسایل برقی، نوسان جریان برق، ناپایداری نت حس می کنید؟
بله:
👍🏻
خیر:
👎🏻</div>
<div class="tg-footer">👁️ 4.2K · <a href="https://t.me/SBoxxx/16813" target="_blank">📅 23:43 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16812">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vGLzXYGGhoXFdnUEunpaHvw2gxW99AS3cBUHJXxYAigcWTo5Sj7l5MWexU-lMNl_2XD5Os1I55xOWBuKtFKeElEWdhQQEbqCl44YESM_MDBIP4UP9CYZYEI-5LQAB9pyniKKT1k0ouLh7RJv06lyUC5elfM74mwSMlfCFZsp0ZbUOAtwKiCJV0RKNUE8hmUCTX8YfII2QxV5KKZD9NiYbAQp5C1axtCHagiHvelfOuAFGsowtICYNFsUaAcmG5enx4izqLmem5JVpXzzYBKLzXfS8nYf9qMQopjWRwBMaZM7Q2SjwELlJ1ejrZpXPe29DDAU9K5VDU6IDDGZlHTWaw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وضعیت جنگ در جنوب لبنان!
منطقه بنفش تصرفات اخیر ارتش اسرائیل
منطقه سرخ محدوده بمباران ها و تنشهای نظامی</div>
<div class="tg-footer">👁️ 4.32K · <a href="https://t.me/SBoxxx/16812" target="_blank">📅 20:31 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16811">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">بسیار کار خوبی است و باعث کاهش فشار روی سرورهای پورن هاب می شود.</div>
<div class="tg-footer">👁️ 4.27K · <a href="https://t.me/SBoxxx/16811" target="_blank">📅 20:04 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16809">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromکاخ رسانه</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/OLEPJ8oItoDifLP1v0YJ8zm72w6mPCotPuAY6VSBtvRqTLASlVnCbDchfZEKSIJ4FcGXHK-gAyakEjKbX74f8vIZpF5xISU_8dg6QQVIJCaEfzJr-FNqmHz5ieL0zWuKVW-x_kUWjkGGn_YibZwhhA-vtoW5CYnrLM9CMUKNR9oKTFZ91uIqU0GScgOg6EGR9tC1ubQnveprw69MT5wFcTF_BE9dIPsf3XTl1FntNzgiB_rT4qhI0rb7BLiRzFAIHLor-kUjfM1N7dbtoqmNOuuwLjuzNOnFZr-jikVg2Ds9USlzgG_T2OigCHYIHEbadno8QQ1TngMq-8S6P1V56w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/JObiMz8diaRbXxTsYRedEdY1kP-gxjtivcx8IfoUnAbJMiOcy6Ux9C3XuUI77yp7d9IkmcnQmHH5Ur69AZI6VgWNZKexbW2Y5V7huS73fvVwso3xu3wwI8fvLHJTc-5iWDJGl3Gu8OguE8SuYJII075InqFRNhMm7a4kQfUNQO4079TbGjTJtTwRqJDtvWZ_X_WtTkcsQdblnobeGzp7e8wqUpXhGdVyylwtIlbuvYeZp63q8w_dPfnDHw-hGWTNCgQsH1c9vsUIQIgnGSo0QTzOlJKACR6eX0He6P1BR-G4egMEv6Ci3d5oVrmtcxB7gnUMoTKdj4BaXPdzU0TDhA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">یک کمپین عجیب در خبرگزاری فارس
گزینه «قطع داوطلبانه دسترسی به اینترنت بین‌الملل» را فعال کنید!
ایجاد کننده کمپین صالح اسکندری از موسسین حزب شریان است
@kakhresaneh</div>
<div class="tg-footer">👁️ 4.24K · <a href="https://t.me/SBoxxx/16809" target="_blank">📅 20:03 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16807">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">سی ان ان:
ترامپ با آزادسازی هرگونه دارایی ایران در توافق احتمالی مخالفت کرده است.</div>
<div class="tg-footer">👁️ 4.39K · <a href="https://t.me/SBoxxx/16807" target="_blank">📅 18:58 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16806">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/p28iyefiiNZZWr4l7uzeOikglN_15XIy4YvnYP6KxqekvOCXiRq_10AcCCgMF7oYAQZo7l1Y9PrNjlDKGzSxyjTxY3NR6eLC7C7AOkOE2oFEm4i63iaPq3mG2989dzQ991kuLliBohY44mIM46FRkkyTROcEen7vGdLDffDr8dw2AOdcEydmdowu9CXshI9jGrzuHhTTmtnHJoMRKjHuns8P5d2-nyHY62L4e1eGc0PBF-8BkrFoZaX9ktQhCdSxEs-G-miv7VG1s0zOJR7DkLx2WbI97Qah7NijI9GYGYYMmopksIFHPmb7DImWrMCPe7KeihwKksGIPh1Z8sEFAA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ فراخوان داده به تماشای برنامه امشب مارک لوین که از محافظه کاران بسیار تندروی حامی ادامه جنگ با ایران است و اساساً توافق با ایران را بی معنی می داند.</div>
<div class="tg-footer">👁️ 4.29K · <a href="https://t.me/SBoxxx/16806" target="_blank">📅 18:52 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16805">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">دقیقاً توصیف موج 4 به زبان ژئوپولیتیک.  بدترین سناریوی ممکن برای روح و روان ما و برای رشد طلا و دلار در داخل</div>
<div class="tg-footer">👁️ 4.33K · <a href="https://t.me/SBoxxx/16805" target="_blank">📅 18:27 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16804">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bhjsBC61jR_Qc5JRWplLrIsfjU-FsHP040pzZyEQdKbgl1rN-IJZPy5QyV4yIrcpDaPjlbp7HUJgHHvc4lE4ZzH1X8hJV_NC6dBwo7HNXY7GB2s0D5rc73dWQ9zU3k6EpC0icQakRcpRPlTvWL3P5VpOIhVqB63GY27x_k1PvOA4gML2xkuRn1SWQyxoeoxmAkXL68j1GecW_0_z1IPCZyfEVdd600dua8MJtOPOD77Zt63OPIUc-rbifzm9Vi3YAj0dHfiJqvT8jTl2COxscbHpyE5Bd2UU06mpVkfJgMZWnD-CkGPa5ocH0sYwGqKBOTUGFN3XnFUz4MXzL-zHVQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">به گزارش گاردین، در انگلستان، سه نوجوان مهاجر که به یک دختر ۱۵ ساله و یک دختر ۱۴ ساله تجاوز کردند، جریمه ۲۶ پوند شدند و آزاد شدند.
فعالان حقوق بشر انگلیسی نمی‌فهمند که این چگونه ممکن است، زیرا حتی جریمه پارک غیرقانونی در بریتانیا ۱۳۰ پوند است که پنج برابر بیشتر از مبلغی است که نوجوانان مهاجر پرداخت کرده‌اند</div>
<div class="tg-footer">👁️ 4.45K · <a href="https://t.me/SBoxxx/16804" target="_blank">📅 18:06 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16803">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromکاخ رسانه</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/696ee3bdc6.mp4?token=dImqC43XRhfRCF5ScQuhwC5rM5tu94xfm1Sea5fJS5t3Z1KvxFcjLrjT6kXowgrZLTCSjbhJom-ak_t1CBScoPbIUyxLggnv_WuR1ksM6v3ApbZrMSrmbuM5TV-2XE7wFh2VpmFzgP_gDZd2VFF7DG4bMGTazxiY-FmGBdAJHRWlc0zIVxAv-eeChNYy9wagY5bAYA8gH08ts5Np7ggAK6fT5ReLmKU4G6IPAfPohzSZzbe18xvLnxRVy5I9RjTjXmWe8E96VKz7FCJbjz7ttZSOWXpWiaKd-kaSYbRKreHtbHKjlI44GF0iJO1KlnMFDpbHtHBaGTvzdRKJjem3Sg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/696ee3bdc6.mp4?token=dImqC43XRhfRCF5ScQuhwC5rM5tu94xfm1Sea5fJS5t3Z1KvxFcjLrjT6kXowgrZLTCSjbhJom-ak_t1CBScoPbIUyxLggnv_WuR1ksM6v3ApbZrMSrmbuM5TV-2XE7wFh2VpmFzgP_gDZd2VFF7DG4bMGTazxiY-FmGBdAJHRWlc0zIVxAv-eeChNYy9wagY5bAYA8gH08ts5Np7ggAK6fT5ReLmKU4G6IPAfPohzSZzbe18xvLnxRVy5I9RjTjXmWe8E96VKz7FCJbjz7ttZSOWXpWiaKd-kaSYbRKreHtbHKjlI44GF0iJO1KlnMFDpbHtHBaGTvzdRKJjem3Sg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دو سال طول می‌کشد تا به شرایط قبل جنگ برگردیم
💬
اسماعیل سقاب اصفهانی، رئیس سازمان بهینه‌سازی و مدیریت راهبردی انرژی:
🗣️
آسیب‌های واقعی کمتر از برآوردهای اولیه بود، اما بازگشت به وضعیت پرچالش قبل از جنگ (با ناترازی عمیق‌تر انرژی) یک و نیم تا دو سال زمان می‌برد.
@kakhresaneh</div>
<div class="tg-footer">👁️ 4.16K · <a href="https://t.me/SBoxxx/16803" target="_blank">📅 17:44 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16802">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">نیروهای سپاه پاسداران ایران به سایت‌های گروه‌های جدایی‌طلب در شمال عراق حمله کردند —رسانه‌های دولتی</div>
<div class="tg-footer">👁️ 4.12K · <a href="https://t.me/SBoxxx/16802" target="_blank">📅 17:24 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16801">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TSTodeeNeBKGne9LcFehSPcXkUEa6leA3Tn9tQokCkVi_B7N1HPPszjykfHVf8Q1mfB9qRHhP4JcnDKVD2GPGt3KT9ZQsMJG0S2srMpLam810ZVqmJIJEbolmIHlIrloCbn3eqvLlIjsbsi9dw27s4uyzlKLLyZgblTRGO6ibjy7nrTE5kE93MRXrA7LtOsLz1ytnsuPeBgPeK9cyiBK3SZ3lxWTxhmSf53bRVFLobD3Y-GMDP8uapEfSwHVPDD0EKU9W7ymZxCEofA9PAHzarvyfAQuCX5aNFiMg56QwiB8P4RqI57ziOktFtB3EOpzb5cVaou6wj0p-f4AeysJEg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نتانیاهو:
«ما قوی‌تر از همیشه بازگشته‌ایم»
او تصرف قلعه بوفورت در لبنان را تبریک گفت و وعده «تغییر چشمگیر» در سیاست نسبت به حزب‌الله داد</div>
<div class="tg-footer">👁️ 4.34K · <a href="https://t.me/SBoxxx/16801" target="_blank">📅 15:58 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16800">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">به گفته یکی از افراد مطلع، اسرائیل در طول جنگ، سامانه‌های گنبد آهنین و نیروهای خود را برای دفاع از امارات متحده عربی اعزام کرد و ده‌ها تن از این نیروها همچنان در یک پایگاه نظامی در این کشور خلیج فارس مستقر هستند.   در اوایل آوریل، عربستان سعودی به آمریکا شکایت…</div>
<div class="tg-footer">👁️ 4.25K · <a href="https://t.me/SBoxxx/16800" target="_blank">📅 14:35 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16799">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">صداهای شنیده شده در قشم و بندرعباس ناشی از امحای مهمات عمل نکرده از جنگ رمضان است.</div>
<div class="tg-footer">👁️ 4.24K · <a href="https://t.me/SBoxxx/16799" target="_blank">📅 14:32 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16798">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">صداهای شنیده شده در قشم و بندرعباس ناشی از امحای مهمات عمل نکرده از جنگ رمضان است.</div>
<div class="tg-footer">👁️ 4.17K · <a href="https://t.me/SBoxxx/16798" target="_blank">📅 14:31 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16797">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">پاکستان به تازگی ۶ کریدور زمینی به ایران افتتاح کرده است.  ۶ مسیر زمینی از کراچی و گوادر مستقیماً به مرز ایران، گبد، تفتان، و چندین نوع دیگر.  کالاهای کشورهای ثالث اکنون می‌توانند تحت نظارت گمرکی از پاکستان به ایران با کامیون ترانزیت شوند.  بیش از ۳۰۰۰ کانتینر…</div>
<div class="tg-footer">👁️ 4.22K · <a href="https://t.me/SBoxxx/16797" target="_blank">📅 14:01 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16796">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromآمو | مطالعات تخصصی آسیای مرکزی</strong></div>
<div class="tg-text">🔵
اختلاف در سازمان کشورها ترک زبان: قزاقستان مخالف تبدیل سازمان کشورهای ترک زبان به یک اتحاد نظامی
⬅️
روزنامه برلینر زایتونگ آلمان می‌نویسد، مسائل ژئوپلیتیکی موجب بروز اختلافی کلیدی در میان کشورهای ترک زبان شده است: برخی از آنها طرفدار ایجاد اتحاد نظامی ترکی هستند، در حالی که برخی دیگر با آن مخالفند. توکایف اصرار دارد که سازمان کشورهای ترک زبان نباید به یک اتحاد نظامی تبدیل شود. در حالی که اردوغان و علی‌اف برای گسترش نفوذ ژئوپلیتیکی و ایجاد یک بلوک نظامی پافشاری می‌کنند.
🔹
قزاقستان از ایده تبدیل سازمان کشورهای ترک زبان به یک اتحاد نظامی تحت یک پروژه ژئوپلیتیکی حمایت نمی‌کند. قاسم جومارت توکایف رئیس جمهور قزاقستان، این موضع را در ۱۵ می در نشست غیررسمی سران کشورها و دولت‌های عضو این سازمان در ترکستان قزاقستان صراحتا اظهار نمود. این در حالی ست که در ماه آوریل، آندری بلوسوف وزیر دفاع روسیه اعلام کرد که مسکو حضور نیروهای خارجی در آسیای مرکزی را نخواهد پذیرفت.
🔹
رئیس جمهور قزاقستان در نشست مذکور گفت: «اخیراً، برخی ایده ایجاد یک اتحاد نظامی را مطرح کرده‌اند. نیات منفی آنها برای ما آشکار است. همچنین مشخص است که اهداف آنها هیچ ارتباطی با صلح ندارد. قزاقستان معتقد است که چنین موضعی باید قویاً رد شود. تقویت وحدت جهان ترک برای ما بسیار مهم و اولویت اصلی است».
🔹
وی اذعان نمود که سازمان کشورهای ترک زبان نه یک پروژه ژئوپلیتیکی است و نه یک سازمان نظامی، بلکه یک پلتفرم منحصر به فرد است که تقویت تجارت، اقتصاد، فناوری‌های پیشرفته، دیجیتالی شدن، فرهنگ و همکاری بین فردی بین کشورهای برادر را ترویج می‌دهد. وی افزود که کشورهای ترک زبان باید در هماهنگی زندگی کنند و با هم توسعه یابند، بدون اینکه از اهداف خود منحرف شوند.»  توکایف همچنین بر اهمیت وحدت کشورهای ترک زبان با توجه به وضعیت ژئوپلیتیکی بین‌المللی بسیار دشوار تأکید کرد.
🔹
پیش از این، آذربایجان پیشنهاد برگزاری رزمایش‌های نظامی مشترک را داده بود. اردوغان که دو روز قبل از اجلاس در یک سفر رسمی وارد قزاقستان شده بود، اغلب در سخنرانی خود به موضوعات ژئوپلیتیک اشاره می‌کرد و تاکید نمود که بحران‌های فلسطین، لبنان، ایران، اوکراین و سایر کشورها لزوم تقویت دفاع ما و گسترش همکاری در بخش صنعتی را نشان داده است. اردوغان همچنین گفت: «همانطور که بحران تنگه هرمز نشان می‌دهد، پروژه‌های حمل و نقلی که جهان ترک را به هم متصل می‌کند، به ویژه مسیر حمل و نقل ترانس-خزر، برای سال‌های آینده اولویت اصلی ما خواهد بود.
🔹
در این نشست علی‌اف نیز به جنبه های ژئوپلیتیکی فعالیت‌های این گروه اشاره می کرد و اظهار داشت: «جهان ترک باید به یکی از مهمترین مراکز ژئوپلیتیکی قرن بیست و یکم تبدیل شود. آذربایجان به تمام تلاش خود برای تقویت سازمان کشورهای ترک ادامه خواهد داد.»
🔹
این در حالی ست که این کشورها در حال تقویت روابط و همکاری های نظامی خود در قالب های دو جانبه و چند جانبه در داخل خود هستند.  در جریان همین اجلاس مشخص شد که آنکارا و آستانه برای ایجاد یک شرکت مشترک برای مونتاژ پهپادهای ANKA ترکیه در قزاقستان توافق کرده‌اند.
آمو | مطالعات تخصصی آسیای مرکزی
@C5Amu</div>
<div class="tg-footer">👁️ 4.34K · <a href="https://t.me/SBoxxx/16796" target="_blank">📅 13:56 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16795">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">🔸
سخنگوی کمیسیون امنیت ملی: برخی اخبار حاکی از موافقت آمریکا با شرایط ایران است</div>
<div class="tg-footer">👁️ 4.25K · <a href="https://t.me/SBoxxx/16795" target="_blank">📅 13:31 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16794">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PBrmUeaom8lUqbXe7Kvv2EYvsPHoxNVyMyrd8T94QrfOcAtVIvRJtEXMv2SB_eR2DOmcD8cJtRpJ6T_XJGKtqvITHoj08PS9Hx7D_sZ5cNhqR2z9xsuCyP5wgsixiqI3rOPMiC4UUR5Dhdghy553KIo_BFrIDLLSIHDN1j3INprg_OXNHtqeFCL1mdFt0Pdsen_iAkBpf3VZlji7gyIg5hR_4oNvVsMbNsA5aYVLnRmkdS2irF4DclNqQZw7_xZBqTJDd9E6Pktw-9TINWXUR0D5KsaD7siYAxjyXNE5qwu_RFGK5zoeBf2MXtQa5qZHy9QI9MlRIGX34XrECEmL3A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">طبق گزارش نیویورک تایمز با استناد به مقامات آمریکایی، ایران نتوانسته است تنگه هرمز را برای ترافیک دریایی بیشتر باز کند، زیرا قادر به یافتن تمام مین‌هایی که در این مسیر پخش کرده نیست و توانایی خنثی کردن آن‌ها را ندارد.  مقامات آمریکایی گفتند که «مسیرهای امن»…</div>
<div class="tg-footer">👁️ 4.42K · <a href="https://t.me/SBoxxx/16794" target="_blank">📅 12:07 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16793">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">ابرت کیوساکی: خالی بودن ذخایر طلا فورت ناکس باعث فروپاشی اقتصاد آمریکا می‌شود!   رابرت کیوساکی (Robert Kiyosaki)، نویسنده کتاب پرفروش «پدر پولدار، پدر فقیر»، نگرانی خود را درباره اقتصاد آمریکا با طرح احتمال مفقود شدن ذخایر طلای فورت ناکس (Fort Knox) ابراز…</div>
<div class="tg-footer">👁️ 4.38K · <a href="https://t.me/SBoxxx/16793" target="_blank">📅 08:42 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16792">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">دونالد ترامپ، رئیس‌جمهور آمریکا، یک پیشنهاد صلح تجدیدنظر شده با شرایط سخت‌تر به ایران ارسال کرده است - به نقل از چندین مقام آمریکایی در گفتگو با نیویورک تایمز.   این «پیشنهاد جدید و سخت‌تر» با هدف افزایش فشار بر ایران برای پذیرش توافق طراحی شده است</div>
<div class="tg-footer">👁️ 4.45K · <a href="https://t.me/SBoxxx/16792" target="_blank">📅 08:36 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16791">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">بن‌گویر: حملات به ضاحیه کافی نبوده است
ایتامار بن‌گویر، وزیر امنیت داخلی اسرائیل، اعلام کرد صدها نیروی حزب‌الله در هفته‌های اخیر هدف قرار گرفته‌اند، اما این اقدامات را کافی ندانست.
او خواستار تشدید حملات به منطقه ضاحیه در جنوب بیروت شد و از دولت اسرائیل خواست عملیات گسترده‌تری را علیه این منطقه انجام دهد.
اظهارات بن‌گویر در ادامه مواضع تند او درباره جنگ لبنان مطرح شده و همزمان با افزایش حملات و تنش‌ها در جبهه شمالی اسرائیل بیان شده است.</div>
<div class="tg-footer">👁️ 4.51K · <a href="https://t.me/SBoxxx/16791" target="_blank">📅 08:14 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16790">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">دونالد ترامپ، رئیس‌جمهور آمریکا، یک پیشنهاد صلح تجدیدنظر شده با شرایط سخت‌تر به ایران ارسال کرده است - به نقل از چندین مقام آمریکایی در گفتگو با نیویورک تایمز.
این «پیشنهاد جدید و سخت‌تر» با هدف افزایش فشار بر ایران برای پذیرش توافق طراحی شده است</div>
<div class="tg-footer">👁️ 4.54K · <a href="https://t.me/SBoxxx/16790" target="_blank">📅 08:02 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16789">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/efjSFT7qx0W0f9ALQJGfmqa0ojY450J51loxRv2PTENA-x5w25zGONYoDBgfbG_Cpz9HDPRAzaVby_EkOUBOzEhZYN31HDoewG3VXdKP5buLnckEE2RmAykpWd279amolXxoiI_2Gah500Cv9Pb7mOmBEKbjePzTfn0J1idjk4mNsBAibrAoKi5JqKQbcyGKw5f6GDtMiAo8T4WcTGlihX5y8D-n6yKd8rCELoD2BDEqA02d7zPs2UgU7IyEgdxiVZ6ANSo6TAE8oHlTGJX6065aV2Fmvr7LX2OSDqxoYLqe5XHxVs7So2d6GGC9SkyjNmQjgBlRvUGN39TRMMCTvQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خلاصه دیدگاه موسسه مطالعات جنگ درباره اهمیت راهبردی کنترل تنگه هرمز در دکترین جدید بازدارندگی جمهوری اسلامی:  مقامات ارشد ایرانی در ماه‌های اخیر بار دیگر بر اهمیت راهبردی تنگه هرمز به‌عنوان یکی از اصلی‌ترین ابزارهای قدرت و بازدارندگی جمهوری اسلامی تأکید کرده‌اند.…</div>
<div class="tg-footer">👁️ 4.69K · <a href="https://t.me/SBoxxx/16789" target="_blank">📅 01:20 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16788">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">بلومبرگ  گزارش داده که حمله موشکی منتسب به ایران در روز شنبه ۳۰ مه (نهم خرداد) به یک پایگاه هوایی در کویت، موجب زخمی شدن تعدادی از نیروهای آمریکایی و وارد آمدن خسارت جدی به دست‌کم دو فروند پهپاد تهاجمی «ام کیو -۹ ریپر» شده است.
بلومبرگ به نقل از فردی مطلع از جزئیات این حمله که به دلیل محرمانه بودن جزئیات نخواست نامی از او برده شود، گزارش داد که پدافند هوایی کویت توانسته است این موشک که از نوع «فاتح-۱۱۰» بوده را رهگیری کند، اما با این وجود، قطعات و آوار ناشی از آن به پایگاه هوایی «علی السالم» برخورد کرده است.
بر اساس این گزارش، حدود پنج نفر شامل نیروهای شرکت‌های پیمانکاری و همچنین نیروهای نظامی دچار جراحات سطحی شده‌اند. همچنین یک فروند پهپاد «ام کیو -۹ ریپر» به طور کامل منهدم شده و دست‌کم یک فروند دیگر به شدت آسیب دیده است. ارزش هر فروند از این پهپادها حدود ۳۰ میلیون دلار برآورد می‌شود.</div>
<div class="tg-footer">👁️ 4.71K · <a href="https://t.me/SBoxxx/16788" target="_blank">📅 00:25 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16787">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">پاریس قهرمان شد…
تبریک به گل شیفته عزیز</div>
<div class="tg-footer">👁️ 4.74K · <a href="https://t.me/SBoxxx/16787" target="_blank">📅 22:34 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16786">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">فوری | فرماندهی مرکزی ایالات متحده:   دیروز، ما یک کشتی با پرچم گامبیا را که سعی داشت با حرکت به سمت یک بندر ایرانی، محاصره را بشکند، از کار انداختیم.</div>
<div class="tg-footer">👁️ 4.73K · <a href="https://t.me/SBoxxx/16786" target="_blank">📅 22:06 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16785">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">یک کشتی تجاری متعلق به دولت ایران توسط ارتش آمریکا با شلیک توقیف شد و نتوانست وارد بنادر ایران شود.</div>
<div class="tg-footer">👁️ 4.7K · <a href="https://t.me/SBoxxx/16785" target="_blank">📅 22:03 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16784">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">با این وضعیت به نظرم دوشنبه نفت با گپ مثبت باز بشود</div>
<div class="tg-footer">👁️ 4.84K · <a href="https://t.me/SBoxxx/16784" target="_blank">📅 21:35 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16783">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">ترامپ:  محاصره دریایی ایران برداشته شده و اورانیوم غنی شده آن را خارج کرده و نابود می کنیم</div>
<div class="tg-footer">👁️ 4.86K · <a href="https://t.me/SBoxxx/16783" target="_blank">📅 21:33 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16782">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">نقش پنهان امارات در جنگ شامل ده‌ها حمله به ایران   به گزارش وال استریت ژورنال، امارات متحده عربی ده‌ها حمله هوایی علیه ایران را از روزهای اولیه جنگ آغاز کرد و تا روز پس از اعلام آتش‌بس ادامه داد،  درگیری عمیق‌تری که تاکنون در کمپین هوایی تحت رهبری ایالات متحده…</div>
<div class="tg-footer">👁️ 4.82K · <a href="https://t.me/SBoxxx/16782" target="_blank">📅 21:31 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16781">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">تا الان فکر می کردم فقط صیغه ساعتی وجود دارد...
سبحان الله؛ ویزای ساعتی را هم دیدیدم در این زندگی اما قهرمانی توفان سرخ آسیا را در همین آسیا نه!</div>
<div class="tg-footer">👁️ 4.72K · <a href="https://t.me/SBoxxx/16781" target="_blank">📅 19:51 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16780">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">حالا خوب است به این ویزا ندهند
😂</div>
<div class="tg-footer">👁️ 4.67K · <a href="https://t.me/SBoxxx/16780" target="_blank">📅 19:51 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16779">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromآمو | مطالعات تخصصی آسیای مرکزی</strong></div>
<div class="tg-text">🔵
بحران ذخایر استراتژیک در واشینگتن؛ تاجیکستان کلید حل بن‌بست تسلیحاتی آمریکا در برابر ایران
⬅️
گزارش‌های اخیر رسانه‌های آمریکایی، از جمله
ان‌بی‌سی
نیوز (NBC News)، از نگرانی عمیق مقامات دفاعی این کشور پرده برداشته است. بر اساس این تحلیل‌ها، واشینگتن در صورت تداوم یا تشدید درگیری‌های نظامی با ایران، با چالش جدی تخلیه زرادخانه‌ها روبرو خواهد شد؛ بحرانی که ریشه در کمبود شدید فلز راهبردی «تنگستن» دارد.
🔹
تنگستن که نقشی حیاتی در تولید مهمات سنگین و تجهیزات نفوذکننده نظامی ایفا می‌کند، از سال ۲۰۱۵ به این سو دیگر در داخل خاک آمریکا استخراج نمی‌شود. اکنون با جدی‌تر شدن سناریوهای تقابل نظامی با ایران، پنتاگون برای حفظ توان بازدارندگی و عملیاتی خود، ناچار به جست‌وجوی شتاب‌زده برای یافتن منابع جایگزین شده است.
🔹
در این میان، منطقه آسیای مرکزی به کانون توجه راهبردی واشینگتن تبدیل شده است. پیش از این، دونالد ترامپ شخصاً بر قرارداد تصاحب ۷۰ درصد از سهام میادین بزرگ تنگستن در قزاقستان نظارت داشت، اما به دلیل زمان‌بر بودن بهره‌برداری از این معادن، آمریکا اکنون به دنبال گزینه‌های در دسترس‌تر است.در همین راستا، نگاه‌ها به سمت تاجیکستان معطوف شده است.
🔹
همکاری‌های اخیر دوشنبه با کره جنوبی برای استخراج از معدن «میخورا» با ظرفیت سالانه ۴ هزار تن، به عنوان یک راه تنفس برای صنایع نظامی غرب نگریسته می‌شود. کارشناسان معتقدند تنگستن تاجیکستان می‌تواند به‌طور مستقیم یا با واسطه (از طریق کره جنوبی)، نیازهای مبرم ارتش آمریکا را پوشش دهد.
🔹
هدف نهایی این تحرکات، علاوه بر آمادگی برای سناریوهای جنگی در قبال ایران، قطع وابستگی کامل به چین در زنجیره تأمین مواد اولیه نظامی است. واشینگتن بر این باور است که بدون تأمین پایدار این فلز از منابعی غیر از چین، حفظ پتانسیل رزمی در برابر رقبای منطقه‌ای همچون ایران، در درازمدت غیرممکن خواهد بود.</div>
<div class="tg-footer">👁️ 4.78K · <a href="https://t.me/SBoxxx/16779" target="_blank">📅 18:42 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16778">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">- مشاور ارشد رهبر عالی ایران، محسن رضایی:
همان‌طور که پیش‌بینی شده بود، رئیس‌جمهور ایالات متحده برای سومین بار به دیپلماسی خیانت کرده است.
با ادامه محاصره دریایی و مطرح کردن مطالبات بیش از حد در مذاکرات، او یک‌بار دیگر ثابت کرده که تمایلی به مذاکره ندارد و اهداف دیگری را دنبال می‌کند.</div>
<div class="tg-footer">👁️ 4.64K · <a href="https://t.me/SBoxxx/16778" target="_blank">📅 17:19 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16777">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">پییت هگست، وزیر دفاع ایالات متحده، هشدار جدی به چین صادر کرد
پییت هگست، وزیر دفاع آمریکا، در نشست امنیتی شانگری-لا در سنگاپور (۳۰ می ۲۰۲۶) سخنرانی کرد و نسبت به تغییر اساسی در رویکرد ایالات متحده به امنیت منطقه‌ای و همکاری با متحدان هشدار داد.
هگست تأکید کرد که امنیت منطقه آسیا-اقیانوس آرام برای مدت طولانی بیش از حد به قدرت نظامی آمریکا وابسته بوده، در حالی که بسیاری از متحدان هزینه‌های دفاعی خود را کاهش داده‌اند.
ایالات متحده از متحدان خود انتظار دارد حداقل
۳.۵ درصد از تولید ناخالص داخلی (GDP)
خود را به امور دفاعی اختصاص دهند.
کشورهایی که هزینه‌های دفاعی خود را افزایش دهند، از مزایایی همچون تسریع فروش تسلیحات، افزایش تبادل اطلاعات و گسترش همکاری‌های صنعتی-دفاعی بهره‌مند خواهند شد.
وی با لحنی قاطع اعلام کرد که متحدان و شرکایی که از پرداخت سهم خود در دفاع جمعی خودداری کنند، با
تغییر روشن و اساسی
در نحوه همکاری و تعامل ایالات متحده مواجه خواهند شد.
هگست چین را به‌عنوان چالش استراتژیک اصلی بلندمدت آمریکا معرفی کرد و بر لزوم ایجاد «تعادل قدرت پایدار» در منطقه تأکید ورزید تا هیچ کشوری نتواند بر همسایگان خود سلطه یابد.
وی از گسترش فعالیت‌های نظامی و رفتارهای تهاجمی چین در منطقه انتقاد کرد.
این سخنرانی نشان‌دهنده سیاست دولت ترامپ مبنی بر فشار بر متحدان برای تقبل بار بیشتر دفاعی و اتخاذ رویکردی قاطع‌تر در قبال جمهوری خلق چین است.</div>
<div class="tg-footer">👁️ 4.86K · <a href="https://t.me/SBoxxx/16777" target="_blank">📅 11:15 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16776">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">توهم خطرناک جنگ مدرن.pdf</div>
  <div class="tg-doc-extra">328.1 KB</div>
</div>
<a href="https://t.me/SBoxxx/16776" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">مقاله ای طولانی اما بسیار خواندنی از اکونومیست درباره تحولات جنگ مدرن و خصوصاً بحث استفاده روزافزون از پهپادها و ریزپهپادها.
اشارات گسترده ای به جنگ اخیر ایران شده که خواندنی است.</div>
<div class="tg-footer">👁️ 4.65K · <a href="https://t.me/SBoxxx/16776" target="_blank">📅 10:14 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16775">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hwhsMjWK9XByOZpagKZRRlk1CDZfksDlvAnTKhOxfZjFfFKcyX0sb1bJCLsoPQqPp9Jm8_IiAzz5l_-YGc64DMBQV2d45NUPYDfd1Lrg-DAIt_9XXIquNVzI_ebzUldtkwGUPeADdNE3SBm5Al4dCMAxINFs4RFchJBhfYGlX8Nyh-P1V-zFpAMxkC75aY6jYU0OXL-_6-gw_Pg1G4RvYl28Oc4A5IclMdVFypDFRoQ6eGWXFq8Fsu1NK-oTXAm7ZhOn5nbtjx2140lQf5lPlg0ImVGzwORGoIc8aEvswRXJzWNuSA5p_M0DYeqMLY_gNuTnIEl2GS4jaefzN08mSA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اعلام هدفگیری شناورهای ایرانی در جنوب تنگه هرمز از سوی ارتش آمریکا</div>
<div class="tg-footer">👁️ 4.63K · <a href="https://t.me/SBoxxx/16775" target="_blank">📅 09:26 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16774">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">این فاکستانی ها هم فعلاً ظاهراً بلای خاصی بجز 100 مورد حادثه تروریستی که اصولاً در پاکستان از بارش باران فراوان تر است دامنگیرشان نشده اما فی الحال لیندسی گراهام گفته به آنها مشکوک است و الّا و بلّا باید به پیمان ابراهیم بپیوندند!</div>
<div class="tg-footer">👁️ 4.58K · <a href="https://t.me/SBoxxx/16774" target="_blank">📅 08:10 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16773">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">پاکستان از 3 سمت تحت فشار است:  — هند ( که همین دیروز اعلام کرد عملیات سیندور را تمام شده نمی داند) — افغانستان (که هر روز شاهد برخوردهای مرزی در مناطق پشتون نشین پاکستان هستیم) — ایالت خودمختار بلوچستان که در آن نیروهای BLA با حمایت مستقیم هند ( و شاید ایران)…</div>
<div class="tg-footer">👁️ 4.53K · <a href="https://t.me/SBoxxx/16773" target="_blank">📅 08:06 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16772">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">تحلیل من این است که ترامپ فعلا میخواهد یک دور کوتاه از حملات شدید را انجام داده و سپس اعلام پیروزی و پایان جنگ کند تا در آستانه جام جهانی، کمتر زیر فشار افکار عمومی باشد.  اما جنگ اصلی برای چند ماه بعد خواهدبود.  در واقع این جنگ کوتاه را می‌توان یک موج B درنظر…</div>
<div class="tg-footer">👁️ 4.87K · <a href="https://t.me/SBoxxx/16772" target="_blank">📅 07:40 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16767">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">نیویورک تایمز:  بحث رئیس‌جمهور ترامپ در اتاق وضعیت نزدیک به دو ساعت طول کشید، اما او به توافق در مورد یک توافق جدید با ایران نرسید، طبق گفته یک مقام ارشد دولت که با شرط ناشناس بودن برای بحث در مورد مباحثات داخلی صحبت کرد.   دولت احساس می‌کند که به رسیدن به…</div>
<div class="tg-footer">👁️ 4.86K · <a href="https://t.me/SBoxxx/16767" target="_blank">📅 22:30 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16766">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">نیویورک تایمز:
بحث رئیس‌جمهور ترامپ در اتاق وضعیت نزدیک به دو ساعت طول کشید، اما او به توافق در مورد یک توافق جدید با ایران نرسید، طبق گفته یک مقام ارشد دولت که با شرط ناشناس بودن برای بحث در مورد مباحثات داخلی صحبت کرد.
دولت احساس می‌کند که به رسیدن به یک توافق نزدیک است، اما سایر مسائل همچنان حل نشده باقی مانده‌اند، به ویژه آزادسازی وجوه مسدود شده ایران</div>
<div class="tg-footer">👁️ 4.89K · <a href="https://t.me/SBoxxx/16766" target="_blank">📅 22:26 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16765">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">تو شیر پیل افکنی !
بزن که خوب میزنی !</div>
<div class="tg-footer">👁️ 4.78K · <a href="https://t.me/SBoxxx/16765" target="_blank">📅 22:19 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16764">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">تحلیل استاد خانعلی زاده از توافق ایران با آمریکا!</div>
<div class="tg-footer">👁️ 4.78K · <a href="https://t.me/SBoxxx/16764" target="_blank">📅 22:19 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16763">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tivB0watKkGbcN28wyp31GLTYMhGEwrDs_LZYGqg2OgBB-pSaayXbpKCSnGS4kiIetCWvRvOqf8-4J1IqT92THaDdU9ewK7dRA2UwiyJhxzpIqRAvmWWzK0PazHxa84HsdyIqbo5NWo8Y6HL-Y0ev1lB3i_bM8JRTp1I1otwYGqYumdUfKUOfH3Kex7BWiBtWvwKt_qon7ACMETk22ppM-5NWOFNciiMdlbJn3dmw_qqgGGM0vqmT2QkuNmK2IwFeOJPmWSlsh0WOLIclq0v5H6fSFxrWlz0X9qhO1LYwUwxpdiooH3JebGOtYE2t8k0fpBLgeVF94MCFz2qV1rTwQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تحلیل استاد خانعلی زاده از توافق ایران با آمریکا!</div>
<div class="tg-footer">👁️ 4.87K · <a href="https://t.me/SBoxxx/16763" target="_blank">📅 22:17 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16762">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">نقش پنهان امارات در جنگ شامل ده‌ها حمله به ایران
به گزارش وال استریت ژورنال، امارات متحده عربی ده‌ها حمله هوایی علیه ایران را از روزهای اولیه جنگ آغاز کرد و تا روز پس از اعلام آتش‌بس ادامه داد،
درگیری عمیق‌تری که تاکنون در کمپین هوایی تحت رهبری ایالات متحده و اسرائیل شناخته نشده بود.
محدوده این حملات شواهد بیشتری از تمایل فزاینده این کشور به محافظت از آنچه به عنوان منافع استراتژیک خود می‌بیند ارائه می‌دهد و آن را از برخی از همسایگان خود در منطقه خلیج فارس متمایز می‌کند که رویکرد بسیار محتاطانه‌تری نسبت به تهدید از سوی ایران اتخاذ کرده‌اند.
این حملات با هماهنگی ایالات متحده و اسرائیل انجام شد که هر دو اطلاعاتی را فراهم کردند، افراد گفتند.
اهداف شامل جزایر قشم و ابوموسی در تنگه هرمز؛ بندرعباس، پالایشگاه نفت در جزیره لاروان در خلیج فارس و مجتمع پتروشیمی عسلویه بود‌ه است.</div>
<div class="tg-footer">👁️ 4.86K · <a href="https://t.me/SBoxxx/16762" target="_blank">📅 22:12 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16761">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">فعال شدن پدافند در قشم!</div>
<div class="tg-footer">👁️ 4.76K · <a href="https://t.me/SBoxxx/16761" target="_blank">📅 22:07 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16760">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">ترامپ:  محاصره دریایی ایران برداشته شده و اورانیوم غنی شده آن را خارج کرده و نابود می کنیم</div>
<div class="tg-footer">👁️ 4.98K · <a href="https://t.me/SBoxxx/16760" target="_blank">📅 18:30 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16759">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">ترامپ:
محاصره دریایی ایران برداشته شده و اورانیوم غنی شده آن را خارج کرده و نابود می کنیم</div>
<div class="tg-footer">👁️ 5.55K · <a href="https://t.me/SBoxxx/16759" target="_blank">📅 18:28 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16758">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromپیکنیک تحلیل</strong></div>
<div class="tg-text">کمیته امنیت ملی مجلس ایران:
قصد نداریم اورانیوم غنی‌شده را به کشور ثالث منتقل کنیم اما شاید آنرا به کشور رابع ارسال کنیم.
@PiknikAnalyst</div>
<div class="tg-footer">👁️ 4.43K · <a href="https://t.me/SBoxxx/16758" target="_blank">📅 15:58 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16757">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sjMOxLw83tkXIBWAgUTdkVGnIgAmORscugLjYiM8cTSfN0vipti5hrCDBiiMJg02NZg0jvYmMR1kr3ABWR7t6Z0-C5Se54E2kEpJZQBUL0GA9odaNcgmPKQkyZzIAXsTm2wCOOyD2y5lV64d6oP5rXX7C7NKlJs8l2pFmJ2tJ0nKS033lZrs3uI9ugxhtosqDCfqTEsMnVgHXXLddMglC_2huvFCwwFFV1t79N9EOwcrEVgZJSvucDKoTbdazLxojzw1KQ-7eiGZGPBCuJUSwZnNHzNQcBHZBkuFAeznUCxBu9nIyhtYayowfjNLqDzoYZ_jgHFMd0rYFdcLi02N5g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">درباره عملکرد پهپاد شاهد-136 در جنگ اخیر
جنگ اخیر نشان داد که پهپادهای خانواده شاهد همچنان یکی از مهم‌ترین ابزارهای تهاجمی ایران به شمار می‌روند، اما بسیاری از ادعاهای مطرح‌شده در فضای مجازی درباره عملکرد آن‌ها نیازمند تفکیک میان واقعیت‌های تأییدشده و ادعاهای اثبات‌نشده است.
پهپاد شاهد-۱۳۶ که در سال‌های اخیر به‌طور گسترده مورد استفاده قرار گرفته، از سامانه‌های ناوبری ماهواره‌ای و هدایت اینرسی برای رسیدن به اهداف خود بهره می‌برد. برخلاف برخی ادعاها، استفاده از ناوبری ماهواره‌ای در این پهپاد فناوری جدیدی محسوب نمی‌شود و از ابتدا بخشی از طراحی آن بوده است. آنچه می‌تواند یک تحول مهم تلقی شود، استفاده از ارتباطات داده‌ای پیشرفته، انتقال تصویر زنده و هدایت لحظه‌به‌لحظه تا زمان اصابت است؛ موضوعی که تاکنون شواهد مستقل و عمومی کافی برای تأیید گسترده آن منتشر نشده است.
در جریان درگیری‌های اخیر، گزارش‌هایی درباره استفاده از نسخه‌های پیشرفته‌تر پهپادهای شاهد منتشر شد. برخی منابع از نصب دوربین‌های اپتیکی بر روی این پهپادها و افزایش دقت آن‌ها سخن گفته‌اند. از نظر فنی، افزودن دوربین به چنین سامانه‌ای کاملاً امکان‌پذیر است، اما ادعاهایی نظیر «اصابت صددرصدی» یا «نابودی قطعی همه اهداف انتخاب‌شده» با واقعیت‌های شناخته‌شده جنگ مدرن سازگار نیست. هیچ سامانه تسلیحاتی در جهان، حتی پیشرفته‌ترین موشک‌ها و مهمات هدایت‌شونده غربی، دارای نرخ موفقیت صددرصدی نیستند.
یکی از مهم‌ترین ادعاهای مطرح‌شده مربوط به آسیب دیدن یا انهدام یک فروند هواپیمای هشدار زودهنگام آمریکایی (AWACS) در پایگاه پرنس سلطان در منطقه الخرج عربستان سعودی است. منابع ایرانی این حمله را موفقیت‌آمیز توصیف کرده‌اند و برخی تصاویر ماهواره‌ای نیز نشانه‌هایی از آسیب به یک هواپیما را نشان داده‌اند. با این حال، جزئیات کامل حادثه و نوع دقیق سلاح به‌کاررفته هنوز به‌طور مستقل و قطعی تأیید نشده است.
در خصوص سامانه دفاع موشکی THAAD نیز گزارش‌هایی از آسیب دیدن برخی تجهیزات و رادارهای مرتبط منتشر شده است. با این حال، ادعای نابودی کامل چندین آتشبار و خروج دائمی آن‌ها از خدمت هنوز از سوی منابع مستقل تأیید نشده و نیازمند شواهد بیشتری است.
در مجموع، داده‌های موجود نشان می‌دهد که پهپادهای شاهد همچنان توانایی ایجاد خسارت‌های قابل توجه و نفوذ به برخی لایه‌های دفاعی دشمن را دارند. با این حال، بسیاری از ادعاهای مطرح‌شده در شبکه‌های اجتماعی و کانال‌های خبری غیررسمی درباره عملکرد این پهپادها، فراتر از اطلاعاتی است که تاکنون به‌طور مستقل قابل راستی‌آزمایی بوده است. تحلیل دقیق تحولات نظامی مستلزم اتکا به شواهد مستند، تصاویر ماهواره‌ای معتبر و ارزیابی‌های مستقل است، نه صرفاً ادعاهای تبلیغاتی طرف‌های درگیر.</div>
<div class="tg-footer">👁️ 4.96K · <a href="https://t.me/SBoxxx/16757" target="_blank">📅 13:58 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16756">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">خلاصه دیدگاه موسسه مطالعات جنگ درباره اهمیت راهبردی کنترل تنگه هرمز در دکترین جدید بازدارندگی جمهوری اسلامی:
مقامات ارشد ایرانی در ماه‌های اخیر بار دیگر بر اهمیت راهبردی تنگه هرمز به‌عنوان یکی از اصلی‌ترین ابزارهای قدرت و بازدارندگی جمهوری اسلامی تأکید کرده‌اند. در این چارچوب، علی‌اکبر ولایتی، مشاور رهبر جمهوری اسلامی، کنترل ایران بر تنگه هرمز را «اهرم نهایی» و «ضمانت واقعی» پایداری هرگونه توافق احتمالی میان ایران و آمریکا توصیف کرد. این موضع‌گیری نشان می‌دهد که تهران، پس از تضعیف بخشی از توان بازدارندگی متعارف خود، به‌ویژه در حوزه موشکی، بیش از گذشته بر موقعیت ژئوپلیتیکی تنگه هرمز به‌عنوان یک دارایی راهبردی تکیه می‌کند.
از نگاه ایران، ارزش تنگه هرمز صرفاً در موقعیت جغرافیایی آن خلاصه نمی‌شود، بلکه این گذرگاه یکی از حیاتی‌ترین شریان‌های انتقال انرژی جهان است و توانایی تأثیرگذاری بر امنیت انرژی بین‌المللی را در اختیار تهران قرار می‌دهد. کنترل یا اعمال نفوذ بر جریان کشتیرانی و صادرات نفت در این منطقه، برای ایران ابزاری جهت ایجاد بازدارندگی، افزایش قدرت چانه‌زنی و محدود کردن گزینه‌های نظامی آمریکا و متحدانش محسوب می‌شود. در واقع، تهران تلاش دارد کنترل بر تنگه را به‌عنوان بخشی از معادله امنیت منطقه‌ای و یکی از پایه‌های نظم مطلوب خود در خلیج فارس تثبیت کند.
در همین راستا، مقامات و رسانه‌های ایرانی بر لزوم مدیریت ترافیک دریایی در تنگه هرمز تحت «ترتیبات ایرانی» تأکید کرده‌اند. برخی گزارش‌ها حاکی از آن است که ایران در مذاکرات غیرمستقیم با آمریکا خواستار به‌رسمیت شناخته‌شدن نقش محوری خود در مدیریت امنیت و عبور و مرور دریایی در این آبراه بوده است. این دیدگاه در تعارض مستقیم با سیاست سنتی آمریکا مبنی بر تضمین آزادی کشتیرانی در آب‌های بین‌المللی قرار دارد.
هم‌زمان، اختلافات اساسی میان تهران و واشنگتن درباره موضوعاتی نظیر برنامه هسته‌ای، لغو تحریم‌ها، آزادسازی دارایی‌های بلوکه‌شده و آینده حضور نظامی آمریکا در منطقه همچنان پابرجاست. گزارش‌های منتشرشده نشان می‌دهد ایران تلاش می‌کند پیش از ورود به توافقات گسترده هسته‌ای، امتیازات اقتصادی و امنیتی مشخصی دریافت کند؛ موضوعی که از نگاه آمریکا می‌تواند بخشی از اهرم فشار واشنگتن را تضعیف کند.
در فضای داخلی ایران نیز برخی رسانه‌های نزدیک به ساختار امنیتی، بر ضرورت تبدیل دستاوردهای نظامی اخیر به دستاوردهای سیاسی و راهبردی پایدار تأکید کرده‌اند. در این چارچوب، تثبیت نفوذ ایران بر تنگه هرمز به‌عنوان یکی از مهم‌ترین ابزارهای قدرت ژئوپلیتیکی کشور، جایگاهی محوری در محاسبات راهبردی تهران یافته است.</div>
<div class="tg-footer">👁️ 4.74K · <a href="https://t.me/SBoxxx/16756" target="_blank">📅 11:39 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16755">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">رسانه اسرائیلی یدیعوت آحارونوت گزارش داد که اسنادی که توسط سرویس اطلاعاتی موساد اسرائیل در ۱۳ ژوئن ۲۰۲۵، در مرحله افتتاحیه «عملیات شیر در حال صعود» منتشر شد، نشان می‌دهد که عوامل ایرانی آموزش دیده توسط اسرائیل و نه خود عوامل موساد اسرائیل در داخل ایران فعالیت می‌کرده اند.
طبق این گزارش، این عوامل در اسرائیل آموزش دیدند، به زندگی عادی در ایران بازگشتند و منتظر فعال شدن بودند. در بهار ۲۰۲۵، تیم برنامه‌ریزی مشترکی از موساد و نیروی هوایی اسرائیل به آنها مأموریتی برای از کار انداختن یک مرکز دفاع هوایی ایرانی دادند که به عنوان بخشی از تلاش‌ها برای تضمین برتری هوایی اسرائیل بر تهران تلقی می شود.
این عوامل از طریق مسیرهای مخفی قاچاق با پهپادها، موشک‌ها و تجهیزات مأموریت مجهز شدند. آنها مختصات نهایی و دستورالعمل‌های استقرار را درست قبل از عملیات دریافت کردند تا خطر نشت اطلاعات به حداقل برسد.
در آن شب، سلول‌های مرتبط با موساد دیگری نیز فعال شدند، از جمله عواملی که به هدایت حملات علیه مقامات ارشد نیروی هوا و فضای سپاه پاسداران و مختل کردن سیستم‌های دفاع هوایی و موشک‌های بالستیک در تهران و غرب ایران کمک کردند.</div>
<div class="tg-footer">👁️ 4.69K · <a href="https://t.me/SBoxxx/16755" target="_blank">📅 11:32 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16754">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">شب گذشته شهر شیعه نشین مرجعیون در جنوب لبنان توسط ارتش اسرائیل تصرف شد.</div>
<div class="tg-footer">👁️ 4.77K · <a href="https://t.me/SBoxxx/16754" target="_blank">📅 10:15 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16753">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">CNN:
پس از حملات ایالات متحده و اسرائیل که در طول جنگ راه‌های دسترسی به «شهرهای موشکی» زیرزمینی ایران را مسدود کرده بودند، حداقل ۵۰ تونل دسترسی پاکسازی و تعمیر شده اند.
تصاویر ماهواره‌ای نشان می‌دهد  که ماشین‌آلات سنگین در حال برداشتن آوار و باز کردن ورودی‌ها در چندین سایت موشکی هستند.</div>
<div class="tg-footer">👁️ 4.93K · <a href="https://t.me/SBoxxx/16753" target="_blank">📅 09:07 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16752">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">نتانیاهو:
در حال حاضر، ما کنترل کامل ۶۰ درصد از نوار غزه را در دست داریم و دستور من رسیدن به ۷۰ درصد است... ابتدا ۷۰ درصد. از همان شروع می‌کنیم</div>
<div class="tg-footer">👁️ 4.85K · <a href="https://t.me/SBoxxx/16752" target="_blank">📅 09:01 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16750">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">خبرهایی دال بر فعال شدن پدافند اصفهان!</div>
<div class="tg-footer">👁️ 5.06K · <a href="https://t.me/SBoxxx/16750" target="_blank">📅 00:07 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16749">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/M7kJ38NsEeeX7wrjkjhOIG2TWWqNsgKU_Rhsgf7t6KCXHbzR8jxZNct5e6cGqf8Uh678NJBPKFU0xE-TBmkrcJ-o5qfY1q7Wz-5miOGT27Wgbu8NXLCPfnJWBCc3TObnpgbGl1Bzy4TdrTYDTwMKfVgnZLT2-VO3nUKxm9YyL12qQuDr72DimwA1e_XWwoqjpBdghOYSsF6CmYVPQ2OAX1rJ09yq2PNUNaUtPnkGfDiLrRn87xFDldqp_GCaVNg7D_qkiOC_wMxbW3SZ7G9qinZTiHd-iFInxiB4ijilUbbqZtplrNz8lTAFpkBmjNUHwLtkA--lCeLKTTRnJtZYaA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 5.12K · <a href="https://t.me/SBoxxx/16749" target="_blank">📅 23:57 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16748">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">تسنیم گزارش داده که مردم بندرعباس نگران نباشند، منشا صداهایی که شنیده شده به درگیری‌های نظامی در دریا مربوط است!</div>
<div class="tg-footer">👁️ 5.15K · <a href="https://t.me/SBoxxx/16748" target="_blank">📅 23:53 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16747">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">تسنیم گزارش داده که مردم بندرعباس نگران نباشند، منشا صداهایی که شنیده شده به درگیری‌های نظامی در دریا مربوط است!</div>
<div class="tg-footer">👁️ 5.16K · <a href="https://t.me/SBoxxx/16747" target="_blank">📅 23:53 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16746">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">کی بشود وعده باقر اجرا بشود از شر این وضعیت راحت بشویم</div>
<div class="tg-footer">👁️ 5.13K · <a href="https://t.me/SBoxxx/16746" target="_blank">📅 23:50 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16745">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">باز گویا در هرمز تبادل آتش داریم!</div>
<div class="tg-footer">👁️ 5.1K · <a href="https://t.me/SBoxxx/16745" target="_blank">📅 23:50 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16744">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">باز گویا در هرمز تبادل آتش داریم!</div>
<div class="tg-footer">👁️ 5.12K · <a href="https://t.me/SBoxxx/16744" target="_blank">📅 23:44 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16743">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sxDaMfs6_xtp_szofgQwfleEI__eFKUScQzhV-J-_Jst9zu1KyLmhExbxztAf2dfBw7xNBpBSF1JhIKu8AeGjWtMv0wjaEovbt2HxYIXI0A13DK-3R5W8O_cIsNTN9wwP4Tn0zBFblKNWZUoS6FSHh8i-6vM4s-mftqA5gtDjO5WFAQiqnI9Fsye6AGySbixBEsEgvwwPVnmHiNgey20j6McAb1TR5ovoGqPcK8IPgX64M9CxAOrJaWB52v_HRODB1_FR_C2Z0NjZpJCT169Tejm3U0eYZBIP5mpNZvVd7LeB4N_CMs2wEcYYkfbIXLjF5t8eMSNq20SR5BNBBOeDA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#Gold</div>
<div class="tg-footer">👁️ 5.25K · <a href="https://t.me/SBoxxx/16743" target="_blank">📅 20:56 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16742">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">این عمانی ها هم بدبخت‌ها یک بار زمان شاه از شر کمونیسم نجاتشان دادیم ولی ۲۰ سال است که سر‌‌ پرونده هسته ای رنده شده اند!  اینقدر که اینها پیام آوردند و بردند، ۱۲۴ هزار پیامبر نکردند</div>
<div class="tg-footer">👁️ 4.82K · <a href="https://t.me/SBoxxx/16742" target="_blank">📅 18:38 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16741">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">اسکات بسنت، وزیر خزانه‌داری ایالات متحده:   «من این را به‌طور خاص به عمان می‌گویم؛ ایالات متحده با هر کشوری که به ایران در وضع عوارض در تنگه هرمز کمک کند، قاطعانه برخورد خواهد کرد.»</div>
<div class="tg-footer">👁️ 4.87K · <a href="https://t.me/SBoxxx/16741" target="_blank">📅 18:37 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16740">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">ترامپ تهدید به منفجر کردن عمان کرد.</div>
<div class="tg-footer">👁️ 4.99K · <a href="https://t.me/SBoxxx/16740" target="_blank">📅 18:36 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16739">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QX5fQkPwmmjQsjgF943-6atLNHtk15w05zscgbD4_5oN_Gv55NsRJjmm51cGbBECOCuBnNcrXxLwxY29fpPiRjBKZU8ckzdqhc_Ll79A6XsDmPc8F_LljS8yIoBTRfG8GiYbmXe8l2IMOiii0EgkindrQkIGQ6TV02pheX7bM5XMrcca1yFNuFV2c0bVSaPtC_vTvr7wAxW85OayKqVwIxkVRqmmc7ua_yXm4sZnn5QMtHVdAxPPjSTbe1pV5NUKEi-QXLNmRcFNtsYIABBJECBIeHCMRB2_WvI3u39A0376NyhMxxPJVgpiXYzSYhBoVxX7B6Q-gaEjRLnPkVbAQA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#VIX
— H4
شاخص ویکس از محدوده ای که جنگ شروع شد پایینتر آمده و کانال را هم شکسته.
سوگمندانه بازارها ما را به یک ورشان هم حساب نمی کنند.</div>
<div class="tg-footer">👁️ 5.13K · <a href="https://t.me/SBoxxx/16739" target="_blank">📅 18:12 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16738">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">این بازی ها فعلاً برای خالی نبودن عریضه است و اینکه فشار جمهوریخواهان تندرو از روی ترامپ برداشته بشود و این ور هم جانفدایان مقداری آرام گیرند و گرنه موج 3 جنگ تمام شده و این حمله اسرائیل به حزب الله هم بخشی از بازی است از دید من.</div>
<div class="tg-footer">👁️ 4.76K · <a href="https://t.me/SBoxxx/16738" target="_blank">📅 17:50 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16737">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">نتانیاهو:
باید مأموریت در ایران را کامل کنیم و تقریباً روزانه در این خصوص با ترامپ صحبت می‌کنم.</div>
<div class="tg-footer">👁️ 4.97K · <a href="https://t.me/SBoxxx/16737" target="_blank">📅 17:24 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16736">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">شرایط توافق شده :  هیچ گروه مسلحی در جنوب رودخانه لیتانی وجود نداشته باشد  کنترل ارتش لبنان بر جنوب  سلاح‌های حزب‌الله محدود شده یا ‌حذف بشود</div>
<div class="tg-footer">👁️ 4.88K · <a href="https://t.me/SBoxxx/16736" target="_blank">📅 16:44 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16735">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">ریچارد فانتین تحلیلگر ارشد سیاست خارجی آمریکا :   محتمل‌ترین پایان این جنگ داغ، یک توافق محدود است. سپس مذاکراتی طولانی و شاید بی‌حاصل آغاز خواهد شد. جنگ سرد از سر گرفته می‌شود. و آمریکا و ایران در انتظار دور دیگری از درگیری در روزی دیگر خواهند ماند.</div>
<div class="tg-footer">👁️ 5.13K · <a href="https://t.me/SBoxxx/16735" target="_blank">📅 14:23 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16734">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">این بازی ها فعلاً برای خالی نبودن عریضه است و اینکه فشار جمهوریخواهان تندرو از روی ترامپ برداشته بشود و این ور هم جانفدایان مقداری آرام گیرند و گرنه موج 3 جنگ تمام شده و این حمله اسرائیل به حزب الله هم بخشی از بازی است از دید من.</div>
<div class="tg-footer">👁️ 5.2K · <a href="https://t.me/SBoxxx/16734" target="_blank">📅 14:22 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16733">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">ماکرون و احیای آرمان شارل دوگل  در تحولات اخیر، رئیس‌جمهور فرانسه، امانوئل ماکرون، اقداماتی قاطعانه انجام داده که یادآور میراث شارل دوگل است و خود را به عنوان یک رهبر کلیدی در دفاع و خودمختاری اروپا معرفی کرده است. پیشنهاد ماکرون برای گسترش بازدارندگی هسته‌ای…</div>
<div class="tg-footer">👁️ 4.9K · <a href="https://t.me/SBoxxx/16733" target="_blank">📅 14:00 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16732">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HJZBpucDkw-mXQyrZfuDbdcysxj-zuSsz4v3Lx60WAUOAnZ438k2cc_r6Q8C2TGtITkCwTQzZVNM-9FNyC_QedlHQ7jinUe4E3SwJUrSuSBKcMOklohwZjWccN286R8DCM4gndJC268MF_SH61wYlohnvOpG7csEfcdLDKRe_j02vLJS0vJ7HSmfttMgH81jNnYtv94hYOz0IJMMw2HARYnZrmIX2iOwB_BT0_8kCiMOVYce02pgGVaSF6TWL4qOTFcexJzyM2DAGxzmMKE9LvHcesuGfXR93AzIVBpyKt066gtylP87u1K8SQ0UpNCjXGyA2K3htcaNlrf4ZfOBgg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">روز جهانی خودارضایی مبارک!</div>
<div class="tg-footer">👁️ 5.18K · <a href="https://t.me/SBoxxx/16732" target="_blank">📅 13:25 · 07 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>

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
<img src="https://cdn4.telesco.pe/file/aySSQUtWogR0WKgaBB5F7zD25ZLRZI0DyGeA9LYozjSZsRS_8skvJzqY4NbCnyR6s3dyo4FsNOqkmmkLywtS96KA8Upq-5G7WffySji_LH8xC0YEDVVLfoyCDWQvIGwqdokNPhzumK9LFX74f8fWMCtZaSAr-B8rSYw9FRZJrBz0jXIYGEBJzxFPPQFf1Ygvck3w4Sm8KeDfe0FwOkgw7sbYmdwh0kiprjma8FWBSeavPdKv8Jkf5vVGNPeCQGINaba46b8khDL--9FF-SioTDLUDF0E1kUery8LbxH81a6F66mqm10pvAcGgfpjL-leTvHqobN-N9GpiGnB51lPyQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Secret Box</h1>
<p>@SBoxxx • 👥 10.3K عضو</p>
<a href="https://t.me/SBoxxx" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 تاریخ، ژئوپولیتیک و بازارهای مالیhttps://secretboxxx.com/</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-27 15:41:26</div>
<hr>

<div class="tg-post" id="msg-18927">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">پس از حملات پهپادی اوکراین امروز، بخشی از منطقه مسکو روسیه توسط یک ابر ضخیم، تاریک و هولناک پوشیده شده است!</div>
<div class="tg-footer">👁️ 3.39K · <a href="https://t.me/SBoxxx/18927" target="_blank">📅 11:49 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18926">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d467cc7c82.mp4?token=bxkSkB1k8GBT0iHccYyvtZTkicCNgeP3TGoSRetCr9NlWjo2O971a_xAjkHoVZLA1xQ2DuXhzkqEvevtyeXYPGubgERyXWdWcL7TpLFiYXTXlTXWw4Nhof_kxVQyeKy8zC-mvsqhbMW2Sl8LGNZd2NJBCkp9EgJIyFTDIXr1Oe1hd7nV7SfwwC_ttFvVe0y696svR31CMnXUE66AK65bQ3C93yoeZdtZO_FMJ8KjY9_eLJ071f5ZkB83bbxtxgJGeIpMLUeXlm-F4BNSbnBHovXMN3TlytS5Z1Vb1ZbQP_7j-voc3odSMmcdMOVDkjjtnvRD4T6nSmMtNpobowhffg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d467cc7c82.mp4?token=bxkSkB1k8GBT0iHccYyvtZTkicCNgeP3TGoSRetCr9NlWjo2O971a_xAjkHoVZLA1xQ2DuXhzkqEvevtyeXYPGubgERyXWdWcL7TpLFiYXTXlTXWw4Nhof_kxVQyeKy8zC-mvsqhbMW2Sl8LGNZd2NJBCkp9EgJIyFTDIXr1Oe1hd7nV7SfwwC_ttFvVe0y696svR31CMnXUE66AK65bQ3C93yoeZdtZO_FMJ8KjY9_eLJ071f5ZkB83bbxtxgJGeIpMLUeXlm-F4BNSbnBHovXMN3TlytS5Z1Vb1ZbQP_7j-voc3odSMmcdMOVDkjjtnvRD4T6nSmMtNpobowhffg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پس از حملات پهپادی اوکراین امروز، بخشی از منطقه مسکو روسیه توسط یک ابر ضخیم، تاریک و هولناک پوشیده شده است!</div>
<div class="tg-footer">👁️ 3.65K · <a href="https://t.me/SBoxxx/18926" target="_blank">📅 11:48 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18925">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">یک مقام آمریکایی گفت که ایران یک موشک بالستیک به سمت یک پایگاه نظامی آمریکا در عربستان سعودی شلیک کرد.
این نخستین حمله مستقیم ایران به عربستان سعودی در نزدیک به چهار ماه اخیر است.</div>
<div class="tg-footer">👁️ 3.47K · <a href="https://t.me/SBoxxx/18925" target="_blank">📅 11:43 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18924">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">چین در این 4 سال مانند یک زالو، شیره جان روسیه را مکید و اکنون به دنبال زامبی کردن روسیه است.  ادعاهای ارضی چینی ها هم بعید نیست دوباره ضد روسیه مطرح بشود.  #ژئوپولیتیک</div>
<div class="tg-footer">👁️ 3.66K · <a href="https://t.me/SBoxxx/18924" target="_blank">📅 11:13 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18923">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lxKnHg5KNNU8dXxYvFjnlA-wjMs2nfzhmirZWOrhKmUmE22EjqZl8KVEQRxHZfV1X0Z6ExWbFJPtQiGpASc0af0Y5Qw7D1Tihj8fBuNXgJo_ZGPYsyXmAiELBhQfD3N3DrLxtPBOWVMWcuJurkBu6qLJ_wMlVZhwHpjh4GxUWuR6_RsMpXuc6JOa2TKIvykZs60kgOB3apYVK8fJwKzFSso6YqnmGTA-eEiP0CYdMXPV1pX5-Wa9Impq2XISjkw9sEJKxy3BzNUtPMZeGJ5Ngw9aKo3roMfBgGzxldc5d6gcjfXrQbQskxPRJPLoxnaaFPx1tYrA9XtuQl9Webf99Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نقشه زمانی تراکم حملات ایران به کویت از 3 ژوئن تا کنون</div>
<div class="tg-footer">👁️ 4.07K · <a href="https://t.me/SBoxxx/18923" target="_blank">📅 09:25 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18922">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">پرس تی وی: نیروی دریایی سپاه پاسداران انقلاب اسلامی، حملات هوایی و موشکی را علیه اسکله پشتیبانی سوختی نیروی دریایی آمریکا در بندر الاحمدی کویت و همچنین انبوهی از هواپیماهای نظامی دشمن در پایگاه هوایی شیخ عیسی بحرین انجام داد.
این نیرو همچنین، مرکز داده‌های اطلاعاتی باتلکو متعلق به دشمن در بحرین را هدف قرار داد و یک مرکز ارتباطی و سیگنال دهی آمریکایی را در کویت منهدم کرد، در حالی که کنترل کامل تنگه هرمز را حفظ کرده است.</div>
<div class="tg-footer">👁️ 4.16K · <a href="https://t.me/SBoxxx/18922" target="_blank">📅 09:12 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18921">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">استانداری هرمزگان:
پل محور رفت سه راه‌میناب به‌سمت
رودان
بعد از دو راهی سرزه مورد حمله دشمن واقع شده است.</div>
<div class="tg-footer">👁️ 4.13K · <a href="https://t.me/SBoxxx/18921" target="_blank">📅 09:10 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18920">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">سبحان الله!
شب خوش!</div>
<div class="tg-footer">👁️ 4.94K · <a href="https://t.me/SBoxxx/18920" target="_blank">📅 01:45 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18919">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">به نظر می‌رسد بانو وضعیت پدافند کویت را توصیف می‌کند!</div>
<div class="tg-footer">👁️ 4.94K · <a href="https://t.me/SBoxxx/18919" target="_blank">📅 01:42 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18917">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">اثر جاودانه بانوی دو عالم — لورا برانیگن — به نام Self Control  که در آن میفرماید:  Oh, the night is my world City light painted girl  In the day, nothing matters It's the nighttime that flatters  In the night, no control Through the wall something's breaking…</div>
<div class="tg-footer">👁️ 4.99K · <a href="https://t.me/SBoxxx/18917" target="_blank">📅 01:41 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18916">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">اثر جاودانه بانوی دو عالم — لورا برانیگن — به نام Self Control  که در آن میفرماید:
Oh, the night is my world
City light painted girl
In the day, nothing matters
It's the nighttime that flatters
In the night, no control
Through the wall something's breaking
I haven't got the will to try and fight
Against a new tomorrow, so I guess I'll just believe it
That tomorrow never comes
A safe night (You take my self, you take my self control)
I'm living in the forest of a dream (You take my self, you take my self control)
I know the night is not as it would seem (You take my self, you take my self control)
I must believe in something, so I'll make myself believe it (You take my self, you take my self control)
This night will never go</div>
<div class="tg-footer">👁️ 4.84K · <a href="https://t.me/SBoxxx/18916" target="_blank">📅 01:40 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18915">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">Audio</div>
  <div class="tg-doc-extra"></div>
</div>
<a href="https://t.me/SBoxxx/18915" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">دقت کرده اید شبهایمان شده جشنواره خبر و روزها همه خواب هستند؟!</div>
<div class="tg-footer">👁️ 4.77K · <a href="https://t.me/SBoxxx/18915" target="_blank">📅 01:33 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18914">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">دقت کرده اید شبهایمان شده جشنواره خبر و روزها همه خواب هستند؟!</div>
<div class="tg-footer">👁️ 4.69K · <a href="https://t.me/SBoxxx/18914" target="_blank">📅 01:32 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18913">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">ایران اعلام کرد که یک پهپاد MQ-9 ریپر متعلق به ایالات متحده را در نزدیکی بوشهر سرنگون کرده است.</div>
<div class="tg-footer">👁️ 4.69K · <a href="https://t.me/SBoxxx/18913" target="_blank">📅 01:29 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18912">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">از کرامات شیخ ما یکی این است
شیره را خورد و گفت شیرین است</div>
<div class="tg-footer">👁️ 4.77K · <a href="https://t.me/SBoxxx/18912" target="_blank">📅 01:26 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18911">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">سرلشکر رضایی:
هم اسمی و هم عملی دیگر چیزی به‌نام تفاهم‌نامهٔ اسلام‌آباد وجود ندارد</div>
<div class="tg-footer">👁️ 4.81K · <a href="https://t.me/SBoxxx/18911" target="_blank">📅 01:25 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18910">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">اینفانتینو: فیفا تأمین‌کننده رسمی شادی برای بشریت است.  ترامپ: مگر اینکه تیم شما ببازد.</div>
<div class="tg-footer">👁️ 4.72K · <a href="https://t.me/SBoxxx/18910" target="_blank">📅 01:20 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18909">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">اینفانتینو: فیفا تأمین‌کننده رسمی شادی برای بشریت است.
ترامپ: مگر اینکه تیم شما ببازد.</div>
<div class="tg-footer">👁️ 4.63K · <a href="https://t.me/SBoxxx/18909" target="_blank">📅 01:19 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18908">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">تسنیم حمله به یزد و لار را که فرمانداران شان تکذیب کرده بودند تایید کرد!</div>
<div class="tg-footer">👁️ 4.71K · <a href="https://t.me/SBoxxx/18908" target="_blank">📅 01:15 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18907">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">الجزیره : وقوع ۵ انفجار در شهر یزد، در مرکز کشور.</div>
<div class="tg-footer">👁️ 4.8K · <a href="https://t.me/SBoxxx/18907" target="_blank">📅 00:51 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18906">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">این توافق اساساً نوع مهندسی و طراحی اش به گونه ای است که هیچ وقت به صورت آشکار منجر به حل کامل و قاطع اختلافات نشود. عمداً بخش های زیادی به صورت خاکستری و ابرآلود باقی نگاه داشته شده تا همیشه بهانه ای بر زدن زیر میز وجود داشته باشد.  عین بلایی که سر ما تریدرها…</div>
<div class="tg-footer">👁️ 4.73K · <a href="https://t.me/SBoxxx/18906" target="_blank">📅 00:49 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18905">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">مهر:
موشک‌های آمریکا به مناطق شهر اهواز برخورد کردند</div>
<div class="tg-footer">👁️ 4.7K · <a href="https://t.me/SBoxxx/18905" target="_blank">📅 00:47 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18904">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">چی بود امضا کردند اینها؟!</div>
<div class="tg-footer">👁️ 4.66K · <a href="https://t.me/SBoxxx/18904" target="_blank">📅 00:46 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18903">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">Memorandum of Misunderstanding!</div>
<div class="tg-footer">👁️ 4.66K · <a href="https://t.me/SBoxxx/18903" target="_blank">📅 00:45 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18902">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">اخبار تاییدنشده از حمله موشکی به یزد!</div>
<div class="tg-footer">👁️ 4.67K · <a href="https://t.me/SBoxxx/18902" target="_blank">📅 00:45 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18901">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">شایعاتی تاییدنشده دال بر پیوستن اسراییل به آمریکا در حملات چند روز آینده منتشر شده.</div>
<div class="tg-footer">👁️ 4.75K · <a href="https://t.me/SBoxxx/18901" target="_blank">📅 00:41 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18900">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">شایعاتی تاییدنشده دال بر پیوستن اسراییل به آمریکا در حملات چند روز آینده منتشر شده.</div>
<div class="tg-footer">👁️ 4.79K · <a href="https://t.me/SBoxxx/18900" target="_blank">📅 00:39 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18899">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">سپاه پاسداران:
اگر آمریکا به پل‌ها و زیرساخت‌ها حمله کند، ما دارایی‌های صنعتی و فناوری اطلاعات شرکت‌های آمریکایی را که در منطقه حضور دارند، نابود خواهیم کرد.</div>
<div class="tg-footer">👁️ 4.8K · <a href="https://t.me/SBoxxx/18899" target="_blank">📅 00:26 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18898">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">حملات ایالات متحده به لار، استان فارس، ایران.
گزارش‌ها حاکی از آن است که این حملات با انفجارهای ثانویه همراه بوده‌اند.</div>
<div class="tg-footer">👁️ 4.8K · <a href="https://t.me/SBoxxx/18898" target="_blank">📅 00:22 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18897">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">رونن کوهن، رئیس هیئت مشورتی کمیته وزارتی اسرائیل در امور شین بت:
«پس از ترور رهبر ایران، یک سوء قصد علیه یکی از اعضای خانواده نخست وزیر نتانیاهو انجام شد که در آخرین لحظه  خنثی شد.»</div>
<div class="tg-footer">👁️ 4.89K · <a href="https://t.me/SBoxxx/18897" target="_blank">📅 00:15 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18896">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">همین مانده بود که یک راس دوزاری  دستمال کش  بیاید گه خوری علی دایی را بکند!
ای مگس عرصه سیمرغ نه جولانگه توست...</div>
<div class="tg-footer">👁️ 5.33K · <a href="https://t.me/SBoxxx/18896" target="_blank">📅 23:04 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18895">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">محسن رضایی: اگر حملات آمریکا تا دو سه روز دیگر ادامه پیدا کند وارد مرحله تهاجمی کامل خواهیم شد
ایران در مرحله تهاجمی کامل دیگر به مقابله به مثل اکتفا نخواهد کرد و هیچ مرز سیاسی در مقابل تهاجم ایران امنیت نخواهد داشت.</div>
<div class="tg-footer">👁️ 5.14K · <a href="https://t.me/SBoxxx/18895" target="_blank">📅 22:43 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18894">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QYiGSczFlMWyN7TPOtfmfmNOoCu_ec8hmHAJO1cmLtZnD6Np7c0SaaO7uh_TiOJuI64cv9EHElaL96masHh4QmiZJWX6wgNMoy0_DLSRmxkxhA7UCWf045iQzysMRvJnKxuF4G0m8_HK9biJLKNcF2jznOlBD-r5wcRfxLGAMX6T97ORf-8TJaUqTuV6aIebOaJNqq0fSM89gEg6Py9PF-uIddyuPY14exBMaGolRioC4yAx7Nt81CRcr6OPKx-9_1a9p8GAseOm6yQbXi4qOLoSJtPsA_NtlK7yYobmy_3aaPZbS0GpOa_1u4tkHEKCXAjLrN8XZOgiCsMpfKUA_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یادداشتی خواندنی از یورونیوز درباره ایزنکوت و حزب ش.  لینک</div>
<div class="tg-footer">👁️ 5.04K · <a href="https://t.me/SBoxxx/18894" target="_blank">📅 22:23 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18893">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">داده فروشی به سبک ترامپ!  شرکت رسانه‌ای خانواده ترامپ، Trump Media & Technology Group (TMTG)، قصد دارد سرویس جدیدی با نام Truth API راه‌اندازی کند که به مؤسسات مالی، صندوق‌های سرمایه‌گذاری و شرکت‌های معاملاتی امکان می‌دهد پست‌های منتشرشده در شبکه اجتماعی Truth…</div>
<div class="tg-footer">👁️ 5.01K · <a href="https://t.me/SBoxxx/18893" target="_blank">📅 21:45 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18892">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">تحقیقات CFTC درباره اپراتور تله‌پرامپتر ترامپ به اتهام استفاده از اطلاعات محرمانه  گابریل پرز (Gabriel Perez)، اپراتور تله‌پرامپتر که مسئول کنترل متن سخنرانی‌ها و هماهنگی نمایش آن برای دونالد ترامپ است، تحت تحقیق کمیسیون معاملات آتی کالاهای آمریکا (CFTC) قرار…</div>
<div class="tg-footer">👁️ 5.57K · <a href="https://t.me/SBoxxx/18892" target="_blank">📅 21:44 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18890">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/W5RJWFPucY2QXhjIe2qBP6MiH_nw6HFa3oNdVdYWBcHBBGsxpU2dnAquOqXLbn0wkQ9oIVz_O3MVpi926LemR9ObpV0AogxjWbevU9BaSdlGphLHWeyJimu3qHOq-Y7Sd0iM4e2xMgJa5rt3xobviCT-t_J1EABGcKjh42z28tbDi4CHvfH1MSkxJqhF8dgALAIOEM2mhNBarEDb_q01Tj9enKE-xne-f_iFDoOuAkJIEEe19rxXeMuB_pE6y0YNIhHX8vVY_ft_KXhMY1WxURJIEl-AhZeJNimg8QgIWrj4zcpJTTdcAXkUtkrHWy99LmhJWVECVj6T6ydmQAukUA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/oBu4mvjYO4O0a0iEIMciiUpBQWEv2MMSK-P-iC-BeVtejnqEsnBOmEiIymHSenE1j3QVZmjYEf6ad2HlHThT4FL12CCWkT8c3DXaYDte7qeXe5P6wOYOmxDAYsp5PmMpuwih72prjcAldyph2II24hObAjG_HN6Qb468H-vp8BvvKFDb9hM5nJGlq-7TYhxBQFTnxyzwOdJLkD7bETKuc8aysECErCOtiImI6Js2MOAAm1KGSKS3bJle4dbnn7IfaZAadYtNHe3dh42JeAkpEiQ_TE9beK_nZgApqCRRw46EsQhXr1x7xcRHKXmyjmO4nYfKcXHoqhhPMdLK_pUrhg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">همبستگی عجیبی میان شمار اعضای کانال با قیمت دلار به ریال وجود دارد!
شاید چون اینجا هیچ گاه خوش بینی متوهمانه برای مذاکرات به خواننده تزریق نشده است.</div>
<div class="tg-footer">👁️ 4.84K · <a href="https://t.me/SBoxxx/18890" target="_blank">📅 20:59 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18889">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">دولت ترامپ به اسرائیل اطلاع داده است که قصد دارد ده‌ها فروند هواپیمای تانکر سوخت‌رسان آمریکایی دیگر را به این منطقه اعزام کند، در حالی که  ترامپ در حال بررسی گسترش عملیات نظامی علیه ایران است.
اگرچه ترامپ هنوز تصمیم نهایی را نگرفته است، مقامات می‌گویند که احتمال افزایش تنش‌ها در روزهای آینده وجود دارد.
— Axios</div>
<div class="tg-footer">👁️ 5.15K · <a href="https://t.me/SBoxxx/18889" target="_blank">📅 20:39 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18888">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/E3CwG_cqPOcF4jSqtaYaWjU09OWFxgZsirrV_ShO5n0eKgtjIUImuLgeaqvZSagXGt9u8s_jEuyar54nP3LEkzMi1y9Xg4-EQuTKrrsHZPSHPyKX2P6IMo6oAQtDF0C5mKhhj9I-UW41lcD9Wxr7tx_AAO5dEfWPYU1msL1ID5X4E2rSuWSysDcDsADhMuvkmZbbbuSVyr-QlQnDcpBvium-38Cd_2Bkra8N-ODEiOiShhAJ3s7qRNNnbTD8s8v-PCRT_su1QcZw4iD-C_tOAsob65LsBLGGsWh3zK-7FcGP85K5r94VPG0a1Hyyt9MiilRQNFYMpdzmHXTMMXzAsg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">باز هم شاخص #GRI به درستی پویه های ژئوپولیتیک را تشخیص داد.  #GRI</div>
<div class="tg-footer">👁️ 5.14K · <a href="https://t.me/SBoxxx/18888" target="_blank">📅 19:33 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18887">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JI90QUFxaPk6yHxlYxsL94K9y3xw7e2u-LUIypdSKnk8a2W4Veknno8I-plBKQh9pplenE1-YzLT9KixjA3kJuO8z6eiESEP2Mwjbt--ZnjmSv08uPNz7fGmTsldaj2ctMeizJm51l1uHX28PVGFp8dKoE1QunqRhXUByotncXXLzBgiXbkDxwG-m6sG-6GXBdck5sNZ20IahGDgxkNv2_3ke-1GJfyT82oDCEYOMN95aoqhbD8oyJLDJvMz-IXHHM3OmbJaMsjNth3re5Vnbfhdv7A89g-U72hxZFpxLHVuNE8ZeIDVSUmsXxlTHDYyLKqa6gMlLGPy7-zvEIiOYg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#GRI  شاخص ریسک ژئوپولیتیک برای امروز در سطح میانه به بالا قرار دارد و از دیروز کاهش یافته است.  پیش بینی می شود بعد از یک افت دیگر در دارایی های ریسکی و طلا، از سشن نیویورک شاهد تقویت میل به ریسک پذیری باشیم.</div>
<div class="tg-footer">👁️ 4.73K · <a href="https://t.me/SBoxxx/18887" target="_blank">📅 19:14 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18886">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NUWAOJGFCxfrcDiMF-2NQXJ-WYDBJm_2MqlXVawhO0LZA67HiBmFpyNJwUsqNrhGer-En1StxNPpjQovZmr_wthwIqjc-wV4TcIbqehacQCOZq5m6o4n1YMiUdwrHAKkDMmU7t7-fwkNZFa0xYY5aZKVudc75ul2jFNxm900ROhyIq_6AapZrMMJLzWIkAFspTgGtquT47ds2Op-TiYmczUD00KZGUOFzAViAAooAAI2wo6vgeDVzyiMTu67p-yXAvjhURUoHsz2BbWQjvjwb_W6B-cOMJo01zuCcUX1Wj0ldyHmILcSGmSTmA0lR54qCWw64RB9Vnx-ull0FEgPlw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مقامات سوریه اعلام کردند که یک محموله سلاح پیشرفته را در نزدیکی مرز عراق کشف کرده‌اند که قرار بود به حزب‌الله در لبنان برسد.  وزارت کشور جولانی اعلام کرد که نیروهای امنیتی، موشک‌های دوربرد، موشک‌های هدایت‌شونده ضدتانک و پهپادها را از یک خودرو مشکوک قبل از…</div>
<div class="tg-footer">👁️ 4.89K · <a href="https://t.me/SBoxxx/18886" target="_blank">📅 17:54 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18885">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">پاکستان و کویت در مراحل اولیه گفتگوهایی برای گسترش همکاری‌های دفاعی خود هستند
به گزارش‌ها، کویت به دنبال یک توافق امنیتی به سبک عربستان سعودی است که می‌تواند شامل حضور نیروهای پاکستانی، هواپیماهای جنگنده، پهپادها، سامانه‌های پدافند هوایی و سایر حمایت‌های نظامی باشد و در مقابل افزایش همکاری و سرمایه‌گذاری در حوزه انرژی را به پاکستان پیشنهاد می دهد.
با این حال، مقامات پاکستانی اعلام کرده‌اند که استقرار نیروهای رزمی در حال حاضر مورد بررسی قرار نمی‌گیرد و تأکید می‌کنند که این گفتگوها هنوز در مراحل اولیه خود قرار دارند.
منبع: رویترز
#ژئوپولیتیک</div>
<div class="tg-footer">👁️ 4.97K · <a href="https://t.me/SBoxxx/18885" target="_blank">📅 17:45 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18884">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lhZEdceskFQe513uR9uV0rrrFdweRxS2sNazI2j7plcbUle3axvmLCqL4z6YgtRTp5TJGFsV_Q-wM37r1NimqFk_i95pAH4hEQRvBJTC0sR9VCFkXOh7T91h7nv_QofSvjA_d_2CZvP5g7-N-Ddsz-LGiYFzGHfUf1O-gsaPrQWyeEWPxKAW2h1xxmfL1zQgi9OuSgYaK3m7recT7S2jVhLmA8OnujdPL8UVIDkFqe95y5ZX1CBpZexqQHdhkEbsZSj6giy8U4nNd3fF1q-aie_SaCPWWouqrpdvDX_m0Qo61XXyCkiYfJOUA9VeLHghwNif2_NdkbOigN2jrTEuQQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وقتی همسرت رو میخوای طلاق بدی اما مهریه ش هم سنگینه!</div>
<div class="tg-footer">👁️ 6.27K · <a href="https://t.me/SBoxxx/18884" target="_blank">📅 17:14 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18883">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">نایب رئیس آرژانتین انگلیس را «دزدان دریایی غاصب» و «تجاوز‌گران» نامید و پیش از نیمه‌نهایی جام جهانی به مناقشه جزایر فالکلند اشاره کرد.</div>
<div class="tg-footer">👁️ 4.97K · <a href="https://t.me/SBoxxx/18883" target="_blank">📅 16:03 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18882">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">ترامپ در مورد نخست‌وزیر جدید عراق:  او جوان و خوش‌تیپ است.  من این را دوست ندارم. من از این خوشحال نیستم.</div>
<div class="tg-footer">👁️ 5.15K · <a href="https://t.me/SBoxxx/18882" target="_blank">📅 15:51 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18881">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">علی مطهری:   یک مقام قضایی سطح پایین دستور فیلترینگ تلگرام را داد</div>
<div class="tg-footer">👁️ 4.93K · <a href="https://t.me/SBoxxx/18881" target="_blank">📅 15:43 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18880">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">علی مطهری:
یک مقام قضایی سطح پایین دستور فیلترینگ تلگرام را داد</div>
<div class="tg-footer">👁️ 4.91K · <a href="https://t.me/SBoxxx/18880" target="_blank">📅 15:43 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18879">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dPEn4K3iAqzRajXft6Q4WEj26Z4ExrITDdwbOpykss4lyBHRqUb8Je0pyqc_A3ssskApfogPeRBugsrOA1jaXuoBU3DUMKjrXjpIICcrW2kGaIFSdfyjc9kLMdWSLSTFWyC8xGluKKLSr0SMTUe9BatzYqd9-fnnAeGaJrsJGZNbM0msYOrPURRi3b-oOTZmYEDJ8mISknV4tC9i5WjlByH3PGyol490v_OIVflqaQn2lAqVstCYvDxMt7fw3mCsejz1HYLPY_iVdu7YjpPkuOocGWQE6uz2DVHWSPMxtzGHqAbs8HIslo2I21MeSJThhT4-Ni_KNjgA9Oxe8eVSLA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مقامات سوریه اعلام کردند که یک محموله سلاح پیشرفته را در نزدیکی مرز عراق کشف کرده‌اند که قرار بود به حزب‌الله در لبنان برسد.  وزارت کشور جولانی اعلام کرد که نیروهای امنیتی، موشک‌های دوربرد، موشک‌های هدایت‌شونده ضدتانک و پهپادها را از یک خودرو مشکوک قبل از…</div>
<div class="tg-footer">👁️ 5.06K · <a href="https://t.me/SBoxxx/18879" target="_blank">📅 14:19 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18878">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">بعید نیست ترور گراهام کار روسها باشد که در هفته های اخیر به معنی واقعی کلمه تحقیر شدند و در گوشه رینگ افتاده بودند. گراهام هم یکی از شدیدترین دیدگاه های مقابله جویانه را با روسیه را داشت.  روسها خدای شیمی هستند و هر مدل عوامل شیمیایی برای ترور را که فکرش را…</div>
<div class="tg-footer">👁️ 4.73K · <a href="https://t.me/SBoxxx/18878" target="_blank">📅 14:01 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18877">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/p0QUTi0hZQYwk2xTtvCDUtAqweLfUZoBstroeE_B3ZAnuSkdFuPSjDiKerBRacX29xfMB-TerOujDe1Cr5vHDl52WiQCVQwQcCFLRS7sqsJCXXU1H2c-96Nmp4NQYRBWNOwAMD1xJwuJADQZT0v9kuO5ZiTT52RiMH4uGt5B3dMAZ-d6utOeb01Yl_SkNItm_d3qxst-PhNKic5ZpweT89bgHkWnfOZ9OA3nuUfnllosSgjHREd-jshPzps-hQ0iRBFCd5_1Fko5qZ1whF3-j1k5Qedhyt1cX1x103lV2pE2jG-85m3mD1NDV8jMiuv1WrNwy5lfww-lObQ3YCFYjQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">گراهام همین چند روز پیش در اوکراین بوده؛ جایی که اصلاً بعید نیست هنوز عوامل اطلاعاتی روسها در آن حضور داشته باشند.   مسمومیت با پولونیوم-۲۱۰ (در موارد شدید) معمولاً طی روزها تا هفته‌ها پیشرفت می‌کند. ممکن است فرد دچار ضعف شدید، تهوع و استفراغ، اسهال، آسیب…</div>
<div class="tg-footer">👁️ 5.06K · <a href="https://t.me/SBoxxx/18877" target="_blank">📅 13:59 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18876">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XZTihX6D3rqn6TtBYBEKmJQpTWBNSFntmzWr2KL5OQYNQTiMdI0nrhglZhR_XHlyljqa25SFkU2wQcCNO-jod73d9pRsuyel2YfJH2aAPJK5JUF6ALrTVLGun7Y7N6tmeYMhHsMnd3xfR9YNYpbmJuS10dBeFAxf6g1GhWT1CBnnKIhwb7b_LLMnP1OivOYRHwCSkoRXCT7imZOye03H19vttMi_0Q7EJ9LKi2fp2bk7YPaYmC0aQIDPM86Pbw-HgYR1uEF1JyCtZTLkHntQT2TlJsbaKJQEMp0U-s-LynHPdQoIwPLFvyaPQKrYaxehFSNtiP3hy_X7iTYXNC5HrQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">توفان احضاریه‌ دموکرات‌ها؛ تلاش نمایندگان کنگره آمریکا برای واکاوی معاملات ترامپ و حلقه نزدیکانش  لینک  #بازارهای_مالی</div>
<div class="tg-footer">👁️ 4.89K · <a href="https://t.me/SBoxxx/18876" target="_blank">📅 13:55 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18875">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">الازرق</div>
<div class="tg-footer">👁️ 4.58K · <a href="https://t.me/SBoxxx/18875" target="_blank">📅 13:44 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18874">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">🔴
انهدام چند فروند سوخت‌رسان و جنگندۀ آمریکایی با موشک بالستیک و پهپادهای متعدد
در موج۱۴ عملیات نصر۲
🔹
سپاه پاسداران: مردم شریف اردن؛ مردمان نجیب سرزمین قدمگاه انبیا الهی، ای مردمی که بیش از همه‌ی مردم جهان با فلسطین قرابت دارید و با دردهای مظلومان غزه و کرانه از همه آشناترید، بعد از حمله سال گذشته ما به پایگاه العدید قطر، ارتش کودک‌کش آمریکا برای دور کردن مرکز فرماندهی خود از حجم بالای آتش رزمندگان اسلام، مرکز فرماندهی نیروهای آمریکا در منطقه (سنتکام) را از قطر به الازرق در خاک شما منتقل کرد و از آن موقع تاکنون مرکز فرماندهی شرارت علیه مردم فلسطین و سایر کشورهای اسلامی در خاک شما و دردسترس شماست.
🔹
علاوه بر سنتکام پایگاه هوایی و دهها فروند سوخت‌رسان، اف۳۵، اف۱۵، و اف۱۶ آمریکایی در خاک شما مستقر هستند و از آنجا به مردم مظلوم فلسطین، ایران و لبنان حمله هوایی می‌کنند.
🔹
شب گذشته ارتش کودک‌کش آمریکا بازهم شرارت کرد و از پایگاه‌های خود در اردن برای ارتکاب جنایت جنگی بزرگ و زدن اهداف غیر نظامی از جمله چند پل، محلات مسکونی و یک مرکز پمپاژ آب در بندرعباس در جنوب ایران استفاده کرد.
🔹
در پاسخ به این شرارت، رزمندگان اسلام در موج ۱۴ عملیات نصر ۲ با رمز مبارک یا صاحب‌الزمان(عج) ادرکنی جنگنده‌ها و سوخت‌رسان‌های آمریکایی مستقر در اردن را در دو مرحله حمله با چندین فروند موشک بالستیک و پهپادهای متعدد مورد هدف قرار دادند که منجر به انهدام چند فروند سوخت‌رسان و جنگنده آمریکایی و آسیب جدی به تعداد بیشتری از آنها شد.
🔹
اینک نوبت شما مردم شریف و ارتش غیور و با شرف اردن است که به تکلیف الهی خود عمل کنند و با ضربه به منافع آمریکایی متجاوز و ضداسلام، لکۀ ننگ آمریکاییهای اشغالگر را از دامان اردن عزیز پاک کنید.</div>
<div class="tg-footer">👁️ 4.87K · <a href="https://t.me/SBoxxx/18874" target="_blank">📅 13:29 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18873">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">تیم ملی والیبال نشسته ایران با شکست ۳ بر ۱ بوسنی، نهمین بار قهرمان جهان شد</div>
<div class="tg-footer">👁️ 4.67K · <a href="https://t.me/SBoxxx/18873" target="_blank">📅 13:13 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18872">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">تیم ملی والیبال نشسته ایران با شکست ۳ بر ۱ بوسنی، نهمین بار قهرمان جهان شد</div>
<div class="tg-footer">👁️ 4.78K · <a href="https://t.me/SBoxxx/18872" target="_blank">📅 13:11 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18871">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">دولت بریتانیا سپاه پاسداران انقلاب اسلامی را در فهرست سازمان‌های تروریستی قرار داد که بر اساس آن، عضویت در این نهاد، شرکت در نشست‌های آن و حمل نماد آن در انظار عمومی جرم کیفری خواهد بود.</div>
<div class="tg-footer">👁️ 4.78K · <a href="https://t.me/SBoxxx/18871" target="_blank">📅 12:14 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18870">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">📌
تایید مواضع هاوکیش وارش از سوی همکارانش در فدرال رزرو  لوگان و اشمید تأکید کردند که تورم هنوز مهار نشده و فدرال رزرو نباید برای کاهش سریع نرخ بهره عجله کند.  این رویکرد هاوکیش می‌تواند از رشد دلار حمایت کند و در کوتاه‌مدت فشار بیشتری بر طلا وارد سازد.
🔗
…</div>
<div class="tg-footer">👁️ 4.68K · <a href="https://t.me/SBoxxx/18870" target="_blank">📅 12:01 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18869">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromCyclical Waves</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Nmlw5hPmaCNzr_lFqCMJt2xiyXtCKnQEQ_eZagWc-WIJjv7M5OuXEg7rJrs2kIujISn-tNKtz9QKpvJuTXFrQiEu-LtRhdGjk7VP-JBw54Rz_Ud6SO-lnE9nW22Qwdf-WiEaR2RkZt6_Xa-jb7FX27iAcMUnqQ3FRt5N-8ef9DZjjKFRNE08Wkt_3mndDW3Ps5G0fEmP3LqikIua4XQ8P-68wvnIy5bca78yCtmdQ8sLqLY30XusWyYD1ZFCAowL-XdmQF6-Ns1sUALYWrdjBB6i_K89jHZLUEw1kL5ENZzMKqSfkPYc2cz0ZDVvj72eIlWvdV_vuuvCbOdrm1g47w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📌
تایید مواضع هاوکیش وارش از سوی همکارانش در فدرال رزرو
لوگان و اشمید تأکید کردند که تورم هنوز مهار نشده و فدرال رزرو نباید برای کاهش سریع نرخ بهره عجله کند.
این رویکرد هاوکیش می‌تواند از رشد دلار حمایت کند و در کوتاه‌مدت فشار بیشتری بر طلا وارد سازد.
🔗
ادامه یادداشت را از اینجا بخوانید
💬
ارتباط با پشتیبانی :
@CyclicalWavesSupport
📌
کانال ما :
@cyclicalwaves</div>
<div class="tg-footer">👁️ 4.56K · <a href="https://t.me/SBoxxx/18869" target="_blank">📅 11:57 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18868">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromپیکنیک تحلیل</strong></div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/tuD4OYGmQ--OlcfdijQ5k5vhH85ubCpUPT5dnH8clu8ERiGJiWrL3dVt9uRY_GMi1ZorgqCobbNIP_XiOwveNPpvhjUShyu713rEUZ6Eowi6ipZP_JKjqUM7HHZQk7PJuymqrgK3AVHkuhpko3s8wuS-rwfhYAj4_I528wkrbn4n-ThuHsk031-_0bDFUyk8u0qu7vHr3ZCszvMw8x5JQ-ApEDHYEgyZcgGSDVA9uLlRYOdT23MnqT07SOyNkWcEKJrxNUyefcgYB6IRlnUN5tdI-pr5BCfxIkBAfsN88XqylYZBtANjg2PQWQG9kGPxZ1at5wSiyf6PFDUTDX2ozw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ـ
😄
@PiknikAnalyst</div>
<div class="tg-footer">👁️ 4.13K · <a href="https://t.me/SBoxxx/18868" target="_blank">📅 11:50 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18867">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/clMkjgrCaeDUJe1JeBUh3TEYmtYduwaSBWSxDCcF5ttkZ5Cashvw5SvTeJpxSN5UnHIIvFeWpN5kVzI8U3SJpMNSQyIpeamb4jVU6itX1YR10_7m40Of8e8PcuOTSDYC9gg31l1usClMjh0oUP-8vgusO28oL_BYxXpKoRKMnilkbGy46CydGSIL9ECyHteJLG76qwqZHlikOrw_HCWX4JIaUQd_FUcjpVvTmCH1dgt3sWgPWBm6l-u6NEaEJblJhQzwseXGNcr0eCLWVk4vAx5DHOY-BW-i1hfhiEKnjvKneJKXShTXaxMdcT-zJKnsdX1URHv400Qwvt99ZD_1jA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این نمودار نسبت بورس به سکه که دست به دست می شود و از آن عملکرد بهتر بورس نسبت به طلا در سالهای آتی نتیجه گرفته می شود تنها در صورتی محقق خواهدشد که :
— سازش اساسی — چندین بار بهتر و فراتر از برجام — داشته باشیم
— تغییر حاکمیت سیاسی در ایران روی بدهد و آن هم بدون جنگ داخلی و تجزیه
به جز این دو صورت هیچ تضمینی نیست که این بار هم محدوده حمایتی مشخص شده حتماً جواب بدهد.
تحلیل تکنیکال روی Ratio Charts هیچ تفاوتی با تحلیل تکنیکال روی نمودارهای سنتی ندارد و ممکن است همین رنج اساساً به پایین بشکند.</div>
<div class="tg-footer">👁️ 4.81K · <a href="https://t.me/SBoxxx/18867" target="_blank">📅 11:49 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18866">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Qo2noEhb6CEmZAM6-5pM5EX2YvkeIWDptDlcnhmBOr9nn2ynuQ8SgMuz72VBke0ka1o63_fzK8liz0PmYodvsamWY9yqXigsskd8gNAbmy9Ps5oOTuHwK8Hyuy1KaAi9xKxR3BoUiKzlDpMiH-BHf3gGC-X1FPs9gwqkhEEi7D-IfxWRDrOrSUOlj1V8H522rKZWCPn4_XM-g-V8gGxR3MGeBWYP_Cpw0LgD-0gOxGenJB8fd8IwnE8vdJfTy5vy8sFd3sb5cIqlU9-KOnSGUjjPq5nSRbQmsphUTX_scIQBrAJ68rQMz-FDTnrBKDtpY-cHx5-kMzboyjiqeDOQ0A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">توپ را در زمین ونس ترنس انداخت تا خودش را مبرا نشان دهد.  ونس 1405 = مرفاوی 1385</div>
<div class="tg-footer">👁️ 4.98K · <a href="https://t.me/SBoxxx/18866" target="_blank">📅 11:15 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18865">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cESjaYueX0jj2zHrnGONISfpvqKGSkAi3jg2Phd40CRl0H4zLN2irqr5lXeEBHF15ZN75tw5ANkmvVa2DBak09Y07Ml68DUh3nWydlGzxSNRCbJK0XTQ7WVizMr1Pk2atM9ZHoi0Y4mDpxmNHrpgxu1WqQHzWIF8v--31EYAaoc3TXzb8iTQYl0c7AA7I_Jwta2jyFat6grFjBLJ1YnHa_doDjg_UKKUvIDjCDizflXCwzgo-ovimL8s-Fh-QDDdu94Z_KEv6RaTSkslnIfeFnZFSVlJ6L_rGu9Q5kaMOapFrbTGDarX7znZ6m7Sb60c9QFQIEwEL2koK3fIVsXFGA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#GRI
شاخص ریسک ژئوپولیتیک برای امروز در سطح میانه به بالا قرار دارد و از دیروز کاهش یافته است.
پیش بینی می شود بعد از یک افت دیگر در دارایی های ریسکی و طلا، از سشن نیویورک شاهد تقویت میل به ریسک پذیری باشیم.</div>
<div class="tg-footer">👁️ 4.66K · <a href="https://t.me/SBoxxx/18865" target="_blank">📅 10:42 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18864">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">Audio</div>
  <div class="tg-doc-extra"></div>
</div>
<a href="https://t.me/SBoxxx/18864" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">#پادکست_GeoMarkets
شماره — 8
جمعه 17 جولای 2026</div>
<div class="tg-footer">👁️ 4.94K · <a href="https://t.me/SBoxxx/18864" target="_blank">📅 10:33 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18863">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">مرکز UKMTO:
گزارش دریافت شده حاکی از برخورد یک تانکر با یک پرتابه نامشخص در روز پنجشنبه، در فاصله ۱۹ نریلی (حدود ۳۵ کیلومتر) شرق شهر خصب کشور عمان است. گزارش‌ها حاکی از آسیب جزئی به ساختار تانکر در نزدیکی عمان است.</div>
<div class="tg-footer">👁️ 4.99K · <a href="https://t.me/SBoxxx/18863" target="_blank">📅 10:09 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18862">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">سپاه پاسداران: رادار کنترل دریایی در صخره‌های سلامه و رادار کنترل هوایی آمریکا مستقر در منطقه غنم عمان منهدم شد
در ادامه عملیات مقابله به مثل رزمندگان اسلام، سحرگاه امروز نیروی دریایی سپاه در موج ۱۳ عملیات نصر ۲ با رمز مبارک یا اباعبدالله الحسین (ع) و تقدیم به تمامی مردم‌خونگرم استان‌های خوزستان، بوشهر، هرمزگان و سیستان و بلوچستان، رادار کنترل دریایی در صخره‌های سلامه و رادار کنترل هوایی آمریکا مستقر در منطقه غنم عمان را هدف قرار داده و منهدم کردند.
عملیات مقابله به مثل با قاطعیت ادامه دارد، همان‌گونه که بعثت جانانه شما مردم؛ و تنگه هرمز هم به فضل الهی کماکان در قبضه قدرت دریادلان نیروی دریایی سپاه است</div>
<div class="tg-footer">👁️ 5.14K · <a href="https://t.me/SBoxxx/18862" target="_blank">📅 10:03 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18861">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HdYuoqkqxRYzUlxBatVywIgAG2YwT2R_OpcnZ8KdFFVUiCa5IezC9Tur3knScdkqweSMRziecaBtH0ojSkGqEmFgrJBHmtziAJyKLPtJX30QA2IOfiWJUtkWAoTILAYn1qHaiMK89rv9_DLgYya1G-gpaHZPVZSsb34678i0PyJO2O0S9eyQLSoHUT3PhXtpdeIPtUybN98n9UD8wXxUbXn1mA8LPRdfezv2cVfAYJPBDFtr-z3PjLw7T8NqUmrASi9tloo073Vicq0SUuneHXpcsSSAXN5sJcIOAFW3hfsUCgY8Y5lcE9f3EWhlnY8hL5onUhhmVnZHX1GrqIxQpw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">برج کنترل دریایی چابهار</div>
<div class="tg-footer">👁️ 5.63K · <a href="https://t.me/SBoxxx/18861" target="_blank">📅 07:39 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18860">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">به‌روزرسانی ۱۶ جولای  سنتکام: یک کشتی «از کار انداخته شد» و کشتی دیگری «برای اطمینان از رعایت کامل محاصره دریایی مداوم علیه ایران» توقیف شد.</div>
<div class="tg-footer">👁️ 5.3K · <a href="https://t.me/SBoxxx/18860" target="_blank">📅 01:46 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18859">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">تلویزیون ایران:
قطع برق در فرودگاه ایرانشهر واقع در استان سیستان و بلوچستان، در پی حمله آمریکا، اما هیچ تلفات جانی گزارش نشده است.</div>
<div class="tg-footer">👁️ 5.23K · <a href="https://t.me/SBoxxx/18859" target="_blank">📅 01:37 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18858">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Xvlk0yBWYpRwJS8OnZrQCFhI8x_C1DETIXfNGRb3uws_waST3j-T07eC3E4yUhhI1l7q68ceI9JbWQMJNJz3rYkOgmIrgg54VQBnfgsQfm_qpgOHI421qqoiLujcFlWQKWX1pn2t0wuUnNn6a6c47HS2U48DmRRllmM90KurLLal32sDMXRWWibD24NsLqa5NljCtYVB0b4ctvHQ3Y9vmNdu2qFcI15vw1rc-RaYG1XSJEDz8E2qlxeBybnQVjmpTUqVJ_dTX5osrSCXv20Z1t6w5l4qb4Up_ljE22wz7kKjDG2vr9hFSclqPZW3CN07SClCut7XKT2eTWmC9990jg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">گویا ایران مستقیماً یک سامانه موشکی زمین به زمین آمریکایی را در کویت هدف قرار داده است.</div>
<div class="tg-footer">👁️ 5.54K · <a href="https://t.me/SBoxxx/18858" target="_blank">📅 01:31 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18857">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">به‌روزرسانی ۱۶ جولای  سنتکام: یک کشتی «از کار انداخته شد» و کشتی دیگری «برای اطمینان از رعایت کامل محاصره دریایی مداوم علیه ایران» توقیف شد.</div>
<div class="tg-footer">👁️ 5.03K · <a href="https://t.me/SBoxxx/18857" target="_blank">📅 01:19 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18856">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">گزارش حمله به کویت، که احتمالاً توسط گروه‌های عراقی وابسته به ایران انجام شده است.</div>
<div class="tg-footer">👁️ 5.07K · <a href="https://t.me/SBoxxx/18856" target="_blank">📅 01:17 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18855">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">آقایان این همه می گفتند پایگاه های آمریکا در منطقه را در هم کوبیدیم!  هیچ تاثیری در کاهش توان آفندی آمریکایی ها نداشته. هر شب دارند بدتر می زنند و اینها هر شب برای سر ترامپ جایزه می گذارند!</div>
<div class="tg-footer">👁️ 5.16K · <a href="https://t.me/SBoxxx/18855" target="_blank">📅 01:08 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18854">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">رسانه های اسرائیلی:
پرواز جنگنده‌های اسرائیلی به سمت مقصدی نامعلوم.</div>
<div class="tg-footer">👁️ 5.25K · <a href="https://t.me/SBoxxx/18854" target="_blank">📅 01:08 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18853">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">گزارش حمله به کویت، که احتمالاً توسط گروه‌های عراقی وابسته به ایران انجام شده است.</div>
<div class="tg-footer">👁️ 5.09K · <a href="https://t.me/SBoxxx/18853" target="_blank">📅 01:00 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18852">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">Business Insider:
اسرائیل از حملات موشکی ایران آموخت که به رهگیرهای بسیار بیشتری نیاز دارد؛ رئیس برنامه دفاع موشکی: «این یک مسابقه است»
حملات موشکی ایران، اسرائیل را به این نتیجه رسانده است که برای جنگ‌های آینده به تعداد بسیار بیشتری موشک رهگیر نسبت به برآوردهای قبلی نیاز دارد.
«موشه پاتل» (Moshe Patel)، رئیس سازمان دفاع موشکی اسرائیل، در گفت‌وگو با
Business Insider
گفت که تجربه نبردهای اخیر نشان داده است تولید رهگیرها باید با سرعت بسیار بیشتری انجام شود، زیرا «این یک مسابقه است»؛ مسابقه‌ای میان توان تولید رهگیرهای دفاعی و توان دشمن برای تولید و انباشت موشک‌های تهاجمی.
به گفته او، سامانه دفاع موشکی
Arrow
(پیکان)، که لایه اصلی دفاع اسرائیل در برابر موشک‌های بالستیک است، در جریان حملات ایران عملکرد موفقی داشته و طی عملیات‌های سال‌های ۲۰۲۴، ۲۰۲۵ و همچنین جنگ طولانی‌تر سال ۲۰۲۶، صدها موشک بالستیک را رهگیری کرده است.
پاتل گفت نرخ موفقیت این سامانه همچنان بیش از ۹۰ درصد بوده، اما حجم حملات و تغییر تاکتیک‌های دشمن نشان داده است که موجودی رهگیرها باید بسیار بیشتر از برآوردهای گذشته باشد. به گفته او، حتی اگر سامانه عملکرد بسیار خوبی داشته باشد، در یک جنگ طولانی، مصرف رهگیرها به سرعت افزایش می‌یابد.
وی افزود که اسرائیل اکنون علاوه بر افزایش تولید رهگیرهای فعلی، توسعه نسل‌های جدید این سامانه را نیز با سرعت بیشتری دنبال می‌کند. رهگیر
Arrow 4
به مراحل پایانی توسعه نزدیک شده و
Arrow 5
نیز در دست طراحی است. هر دو سامانه قرار است با بهره‌گیری از فناوری‌های جدید، از جمله هوش مصنوعی، توان مقابله با تهدیدات آینده را افزایش دهند.
پاتل تأکید کرد که اسرائیل تمامی داده‌های به‌دست‌آمده از رهگیری‌های واقعی را به دقت تحلیل می‌کند تا سامانه‌های دفاع موشکی خود را بهبود دهد. او گفت هر درگیری واقعی، اطلاعات ارزشمندی در اختیار مهندسان قرار می‌دهد که در آزمایش‌های عادی قابل دستیابی نیست.
این مقام اسرائیلی همچنین به فشار فزاینده بر زنجیره تأمین جهانی سامانه‌های دفاع هوایی اشاره کرد و گفت افزایش تقاضا برای موشک‌های رهگیر، از جمله سامانه آمریکایی
Patriot
، نشان می‌دهد بسیاری از کشورها به دنبال تقویت دفاع موشکی خود هستند و تولیدکنندگان باید ظرفیت تولید را افزایش دهند.
او در پایان گفت درس اصلی جنگ‌های اخیر این است که داشتن یک سامانه دفاعی پیشرفته به تنهایی کافی نیست؛ کشورها باید ذخایر بسیار بزرگی از موشک‌های رهگیر نیز در اختیار داشته باشند تا بتوانند در صورت وقوع یک نبرد طولانی، به دفاع مؤثر ادامه دهند.
#ژئوپولیتیک</div>
<div class="tg-footer">👁️ 5.33K · <a href="https://t.me/SBoxxx/18852" target="_blank">📅 00:52 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18851">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">انفجارهای شدید در سیریک</div>
<div class="tg-footer">👁️ 4.95K · <a href="https://t.me/SBoxxx/18851" target="_blank">📅 00:11 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18850">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">آقایان این همه می گفتند پایگاه های آمریکا در منطقه را در هم کوبیدیم!
هیچ تاثیری در کاهش توان آفندی آمریکایی ها نداشته. هر شب دارند بدتر می زنند و اینها هر شب برای سر ترامپ جایزه می گذارند!</div>
<div class="tg-footer">👁️ 5.61K · <a href="https://t.me/SBoxxx/18850" target="_blank">📅 00:04 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18849">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">نماینده کنگره آمریکا از «تغییر رژیم» در ایران گفت
نماینده کنگره آمریکا تیم بورچت خواستار روی کار آمدن فردی در ایران شد که به گفته او با آمریکا تعامل کند.</div>
<div class="tg-footer">👁️ 5.38K · <a href="https://t.me/SBoxxx/18849" target="_blank">📅 23:57 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18848">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">حمله آمریکا به تانکرهای سوخت در بندر عباس</div>
<div class="tg-footer">👁️ 5.46K · <a href="https://t.me/SBoxxx/18848" target="_blank">📅 23:50 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18847">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">حمله آمریکا به تانکرهای سوخت در بندر عباس</div>
<div class="tg-footer">👁️ 5.35K · <a href="https://t.me/SBoxxx/18847" target="_blank">📅 23:50 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18846">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">لطفاً از مراکز نظامی فاصله بگیرید. ویدیوی وحشتناکی از اصابت موشک های آمریکایی به جایی در بوشهر دیدم.</div>
<div class="tg-footer">👁️ 5.19K · <a href="https://t.me/SBoxxx/18846" target="_blank">📅 23:49 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18845">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">انفجارهای بزرگ در بندرعباس، قشم و اهواز</div>
<div class="tg-footer">👁️ 5.09K · <a href="https://t.me/SBoxxx/18845" target="_blank">📅 23:09 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18844">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">به نظر می رسد تنها یک معجزه می تواند از بروز حمله زمینی آمریکا جلوگیری کند.
تصور می کردم در اوج گرما این کار را نکنند اما روند حوادث چیز دیگری را می گوید فعلاً.</div>
<div class="tg-footer">👁️ 5.69K · <a href="https://t.me/SBoxxx/18844" target="_blank">📅 23:09 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18842">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromآرش رئیسی‌نژاد</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/545819aa84.mp4?token=jp7CxUNSrtsadiJw-PQ7peFSvnUZjsODS4NVNlz-yzCtYQ2KynBXW89tkNnM4gcz_yoW57suvckhurGVojU_USjT-mi6zn0u6O3GvqWWa22i24Syhj7k6lMI3jH3zFWoGIdMcJYoAn6dcOxC3Uo4lR41uzD6xSuP35o-_I_TnL-OGZLoqHbw6jcK22fUm4nxRUm31XERflBinw9hMbxKZuIn4Bux0iuwSgtZ2KMBZVBAH9TD4ACIKCn6zw81KVVlyQYuXCqqRS7uGrk4sGiaiqChoSBnE2X21gZzgdxQ2kYtT3BP6zFIuxJigCkvOHryWbZfs4spXQ4sx_kmAHPnig" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/545819aa84.mp4?token=jp7CxUNSrtsadiJw-PQ7peFSvnUZjsODS4NVNlz-yzCtYQ2KynBXW89tkNnM4gcz_yoW57suvckhurGVojU_USjT-mi6zn0u6O3GvqWWa22i24Syhj7k6lMI3jH3zFWoGIdMcJYoAn6dcOxC3Uo4lR41uzD6xSuP35o-_I_TnL-OGZLoqHbw6jcK22fUm4nxRUm31XERflBinw9hMbxKZuIn4Bux0iuwSgtZ2KMBZVBAH9TD4ACIKCn6zw81KVVlyQYuXCqqRS7uGrk4sGiaiqChoSBnE2X21gZzgdxQ2kYtT3BP6zFIuxJigCkvOHryWbZfs4spXQ4sx_kmAHPnig" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">چهار ماه پیش، در مقاله‌ام در Foreign Policy، استدلال کردم که پنج نقطه استراتژیک در جنوب ایران، محتمل‌ترین اهداف هرگونه کارزار نظامی گسترده آمریکا خواهند بود. امروز، الگوی در حال شکل‌گیری حملات بیش از هر زمان دیگری با آن ارزیابی همخوانی دارد.
توالی حملات نشان از استراتژی کلان‌تر محتملی دارد. عملیات از جزایر آغاز شد، سپس به سواحل رسید و اکنون در حال نفوذ به عمق بیشتری از جنوب ایران است؛ حتی به مناطقی که دیگر در نوار ساحلی قرار ندارند. این‌ها صرفاً مجموعه‌ای از حملات تاکتیکی و پراکنده نیستند. آنچه دیده می‌شود، به نظرمی‌رسد بخشی از تلاشی گسترده‌تر برای تضعیف تدریجی معماری دفاعی ایران در کنترل تنگه هرمز و دیگر گره‌های استراتژیک، از جمله جزیره خارک، باشد.
اینکه این روند در همین نقطه متوقف شود یا نه، هنوز پرسشی باز است. اما الگوی کنونی این احتمال را مطرح می‌کند که این حملات تنها بخش آشکار یک طرح عملیاتی بزرگ‌تر باشند؛ طرحی که هدف آن خنثی کردن، یا حتی فراهم کردن زمینه برای کنترل آینده برخی از مهم‌ترین نقاط استراتژیک جنوب ایران است.
@Iran_Simorq</div>
<div class="tg-footer">👁️ 5.07K · <a href="https://t.me/SBoxxx/18842" target="_blank">📅 22:57 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18841">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">فرماندهی مرکزی ارتش آمریکا (سنتکام): ارتش ایالات متحده حملات جدیدی را علیه ایران انجام می‌دهد.</div>
<div class="tg-footer">👁️ 4.84K · <a href="https://t.me/SBoxxx/18841" target="_blank">📅 22:47 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18840">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">سخنگوی کاخ سفید، لیویت:   ایران همچنان با ایالات متحده در گفتگو است و خواهان رسیدن به توافقی است؛ حملات اخیر به دلیل نقض توافق‌نامه توسط ایران صورت گرفته است.</div>
<div class="tg-footer">👁️ 4.88K · <a href="https://t.me/SBoxxx/18840" target="_blank">📅 21:55 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18839">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">سخنگوی کاخ سفید، لیویت:   ایران همچنان با ایالات متحده در گفتگو است و خواهان رسیدن به توافقی است؛ حملات اخیر به دلیل نقض توافق‌نامه توسط ایران صورت گرفته است.</div>
<div class="tg-footer">👁️ 4.89K · <a href="https://t.me/SBoxxx/18839" target="_blank">📅 21:49 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18838">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">سخنگوی کاخ سفید، لیویت:
ایران همچنان با ایالات متحده در گفتگو است و خواهان رسیدن به توافقی است؛ حملات اخیر به دلیل نقض توافق‌نامه توسط ایران صورت گرفته است.</div>
<div class="tg-footer">👁️ 4.83K · <a href="https://t.me/SBoxxx/18838" target="_blank">📅 21:48 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18837">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XxJbeEBZqOJfQGjaih0vZmQFA7jnmX_RZ-SejnvSnDJNJSCdX_WvYxBoFsAG3SKwEtHZVPfh6OfZ6MtGv96G0MFqtfsO69dsU-vxsRKfLAjeVv_Y4s_v_eZQfHShCmmhMtHPywOkO-mwBcNdIohYTxS6yQGWUWnl5xYcxE-HlHVY8-m10E58Y27J-Rwbt86ueaql2SCQ5jcXnFKN7wZTiMgNEXq1ov_WSx5cZYYvfdP_MY-tKjX6Me7WVOApyDk5Ak96oiyav4PaZW0mtns93DV2CNCGY3_vLYpjivYQ-rh75gcyKkFMC343Hl5ZR2piNZU_calmeKKYJOahVakCIg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ایران به حملات علیه املاک ترامپ در خاورمیانه تهدید کرد
باشگاه‌های گلف و برج‌های بلند در امارات متحده عربی، عربستان سعودی، قطر و عمان می توانند هدف قرار بگیرند:
- باشگاه گلف بین‌المللی ترامپ دبی - منطقه داماچ هیلز، دبی، امارات متحده عربی؛
- هتل و برج مسکونی بین‌المللی ترامپ دبی - مرکز شهر دبی، امارات متحده عربی؛
- برج ترامپ پلازا جدّه - ساحل جدّه، عربستان سعودی؛
- برج ترامپ ریاض - ریاض، عربستان سعودی؛
- باشگاه گلف بین‌المللی ترامپ وادی صَفار - وادی صَفار، دیریاه، عربستان سعودی؛
- باشگاه گلف و ویلاهای بین‌المللی ترامپ سمایسما - سمایسما، قطر؛
- هتل بین‌المللی ترامپ عمان - مسقط، عمان.</div>
<div class="tg-footer">👁️ 4.98K · <a href="https://t.me/SBoxxx/18837" target="_blank">📅 21:40 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18836">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">وزیر امور خارجه اردن، ایمن صفیادی: ایالات متحده هیچ پایگاهی در اردن ندارد، اما سربازان آمریکایی به عنوان بخشی از همکاری نظامی بین اردن و واشنگتن، در کشور ما حضور دارند. - خبرگزاری فارس</div>
<div class="tg-footer">👁️ 4.6K · <a href="https://t.me/SBoxxx/18836" target="_blank">📅 21:37 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18835">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">وزیر امور خارجه اردن، ایمن صفیادی: ایالات متحده هیچ پایگاهی در اردن ندارد، اما سربازان آمریکایی به عنوان بخشی از همکاری نظامی بین اردن و واشنگتن، در کشور ما حضور دارند. - خبرگزاری فارس</div>
<div class="tg-footer">👁️ 4.7K · <a href="https://t.me/SBoxxx/18835" target="_blank">📅 21:36 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18834">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aicN-qsLy6TLoPwXccdqz9_HPcDMuZHcc1yg61Q0dN5EetV6YrxQ_Ta2_U50kgdqh44LVHGGc1-vaJ0DEkQk5cb9CAAp_CnwzuTmYdn61v9Weg_by5HAQ7LVdiS2LqX9jAyfm6iJPh9z4hITPwRUMLg3xYJVg4VXdXH855Sgn2hNQcKFcI3ieZ1d4XN6vWx6jKQY55X6nMN-sFNvWZURpSM83O-MbXqPOHcYlU9VGJ59qS-Dxl_mmdc4MLojevIvVHGMgFIi44uS56wprHU-nDfctUn19ITkr9wfujW4CWVrsOj-N1nNF0h4jDCZG8TGgIBxcCinlbOZK__4vFRfjw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">توپ را در زمین ونس ترنس انداخت تا خودش را مبرا نشان دهد.  ونس 1405 = مرفاوی 1385</div>
<div class="tg-footer">👁️ 5.25K · <a href="https://t.me/SBoxxx/18834" target="_blank">📅 20:03 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18833">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZwXQYN8R7M-N4lHH25-lAxnY2nUph-T0J4TuvzMZsOyHRWMJOA0mGNaqvI57DucdJWw2lZXI3kwdDdajkte8W52CUeCb3YlPB5vqtEUnDPcgsoubh82HTT-S8U4vF_jhBWgVjwBs22OuzJfwojaf6YrULEXe5iidZu-2S7MxZ5jNRhm-I_9umWt5CaX7R2LKdoa1NbytjL73usp62GK4sOlm8UDHRH2-Kumv1rswInYQvNzE0hN1wVGu5m5zUPgf5vtC43cr6OUQ_GS-bD84Vj7ROrhrXg4RbowqtlpWKUElBAH48-WIgPNXvTlRMFWf23cpqyM8zJInUBCPOIcpeA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سل طلا بسته شود.</div>
<div class="tg-footer">👁️ 4.72K · <a href="https://t.me/SBoxxx/18833" target="_blank">📅 18:48 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18832">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">موشک‌های آمریکایی به اهدافی در جزیره قشم در جنوب ایران اصابت کرده‌اند.
— خبرگزاری مهر</div>
<div class="tg-footer">👁️ 4.75K · <a href="https://t.me/SBoxxx/18832" target="_blank">📅 18:39 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18831">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">رهبر یمن سخرانی مهمی را آغاز کرده است</div>
<div class="tg-footer">👁️ 4.81K · <a href="https://t.me/SBoxxx/18831" target="_blank">📅 18:22 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18830">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">این دیگر حماقت محض است. شما شاید بتوانید با موشک و پهپاد اهدافی را در یک کشور مرفه ثروتمند مانند قطر یا کویت بزنید و آنها را وادار به دادن امتیازاتی بکنید؛ اما زدن اهداف مربوط به کشوری که مانند صوریه جولانی 15 سال است اساساً در گه فرورفته و مردمش نمی دانند…</div>
<div class="tg-footer">👁️ 4.84K · <a href="https://t.me/SBoxxx/18830" target="_blank">📅 17:55 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18829">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">مشاور محسن رضایی:   تصمیم مهمی در تهران اتخاذ شده است؛ اگر حکومت جولانی بنا به درخواست ترامپ و فشار آمریکا دست به اقدام علیه حزب‌الله بزند، با حملات موشکی و پهپادی مستقیم ایران مواجه خواهد شد. این هشدار به جولانی داده شده است.  #ژئوپولیتیک</div>
<div class="tg-footer">👁️ 5.11K · <a href="https://t.me/SBoxxx/18829" target="_blank">📅 17:54 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18828">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/S--J9EYP0yRmX9cPLnPO92ud7EDr-u9fTBPwslbxCTMKPtbDo781uJnl16s7mbFSmkQUawQUOV3e0l3VR-pc8xZ_qblzbd7K_hbzb2GTJVXIyna8TEN0A1tTVlGtVMo6MjNvgLHwOaSdUbb0sHRwvQ-JfVjpOvC1SE_EnilZ9gyr1i53ZNqIlCp3YBxMHGD3glRlizMefl-o6TCIVQnyOBzYs2Vivl0TN_TFbK35sFT05FXWNJWArEXAahi0dOvAsbSyAiPlwFFsapC2ZF7K0P5oZ85bgcCWhO_3W3WgcQDge9A1g3znojuf60oZEnaNHX_kbUQju05q2h8YFucUKA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">به نظر شما ترامپ با این سه سگ (اردوغان، فیدان، کالین) چه صحبتی می تواند داشته باشد آن هم وقتی که جولانی هم دارد به اینها می پیوندد؟!</div>
<div class="tg-footer">👁️ 4.9K · <a href="https://t.me/SBoxxx/18828" target="_blank">📅 17:52 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18827">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TbzGu-SlMd1N--1rj3a-WKle1p3OPSNjoy43SYhDVd4YqcOL9lMvGZUgtoo0aGMMNXqYIdW_Jzr9zewUtwzYvsOVUPlTtg2xyZY1u8iqM-6PxXAa4yNxXAHc-4-Mo62rvOxcMjv9SRMolcL44Mu5Wny8rLzeuVWRbuvbNch7ZMP77GeEIOSHlsO4t2awLRMsI9JG0cc-dWiZS4rxnHYOU9oMSyC2hkPQb_Kujw9sqO8tScwavWQFgVfbHgij1jvHXZTf60c8AGgG0r-2xEC_wzUt1WtwCfNa1w9AQSg0gb0A_hfGLKNzIWc2CnwLfjgabcInYI0uYCrviW2KU9X3oQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرنگار: آیا رئیس‌جمهور الشرع (جولانی) برای شما تعهداتی در مورد کمک به حزب‌الله در لبنان داد؟  ترامپ: بله، او این کار را کرد.</div>
<div class="tg-footer">👁️ 4.76K · <a href="https://t.me/SBoxxx/18827" target="_blank">📅 17:43 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18826">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">رهبر
یمن سخرانی مهمی را آغاز کرده است</div>
<div class="tg-footer">👁️ 4.72K · <a href="https://t.me/SBoxxx/18826" target="_blank">📅 17:00 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18825">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-footer">👁️ 4.83K · <a href="https://t.me/SBoxxx/18825" target="_blank">📅 17:00 · 25 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>

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
<img src="https://cdn4.telesco.pe/file/j6PzST_iXo0RLwSp6uOcTIH6kHpNRA1-buwUXEUmAwo4mIBlPO1MPk4s67Z2IMKhw1NI7xJYoU9wCS1AeGblvPJDtfswE3bQLOOMSICfQ2IncnsKpVo5tOOIhx0v75IiOQB5qvWOL6KCuwCVOz-1aywQMB3ay2UWevX879SIvkYhrZTwWJBzR1BLabAk1QKy_NVOJ1J_Uk3t7vSJGwN4pvnAiCR0OdnioyFjLhIRNZSFvZ0aP7QCCn2rd90baKrB4inLI8ARr1p_6Ib3OAXAmhNJQsaDeHATClAoyWcWTagtGhKGmaLHajj1Lg1h_S2eouwI8TjJWPtlVrKo2M2F-g.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Secret Box</h1>
<p>@SBoxxx • 👥 10.5K عضو</p>
<a href="https://t.me/SBoxxx" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 تاریخ، ژئوپولیتیک و بازارهای مالیhttps://secretboxxx.com/</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-09 20:50:37</div>
<hr>

<div class="tg-post" id="msg-19535">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/42e924f93a.mp4?token=PLgxg-mGXsw4F8XeMtkIC3L-AQrBHYv0Uy8UTQA9ezN7fBCJhivzsuJDZn_MOgcxbtLtZFiiY5QbO9cjR_8K3UpqnQZHNe-4FIkOjWqWxETLfawSf9FtU_N6IX2CMJUkRCmD5KZvGAa_ltO-jAAiiaaTajn1cUhP-FZeKzZGGn_I9CaGrhHvl56hiIHMz6ADq80Ub2g4PEhZIw7q6eBQACY4TCyHvfkMrEDzy1dqpabXGZbNoXc0_hvMWiXf995OZ-t26oCy2tfIlAuqyVkLjuN9tZLkPux4TyWGwImGA7txa4WoDuPfsbcCj8ydzWz1_V-PntuRwSOy372m_FdaMw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/42e924f93a.mp4?token=PLgxg-mGXsw4F8XeMtkIC3L-AQrBHYv0Uy8UTQA9ezN7fBCJhivzsuJDZn_MOgcxbtLtZFiiY5QbO9cjR_8K3UpqnQZHNe-4FIkOjWqWxETLfawSf9FtU_N6IX2CMJUkRCmD5KZvGAa_ltO-jAAiiaaTajn1cUhP-FZeKzZGGn_I9CaGrhHvl56hiIHMz6ADq80Ub2g4PEhZIw7q6eBQACY4TCyHvfkMrEDzy1dqpabXGZbNoXc0_hvMWiXf995OZ-t26oCy2tfIlAuqyVkLjuN9tZLkPux4TyWGwImGA7txa4WoDuPfsbcCj8ydzWz1_V-PntuRwSOy372m_FdaMw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اگر هدف پایگاه الازرق باشد هیچ اتفاقی نمی افتد.  مگر اینکه یک پایگاه الاحمر نامی را بزنند تا در هم کوبیده شود.</div>
<div class="tg-footer">👁️ 1.35K · <a href="https://t.me/SBoxxx/19535" target="_blank">📅 20:15 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19534">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">ترامپ درباره اوکراین:
تانک‌های روسی در حال حرکت به سمت کی‌یف بودند، اما در گل گیر کردند.
یک ژنرال روسی تصمیم گرفت به جای استفاده از بزرگراه که به خوبی در حال حرکت بودند، از میان گل عبور کند.</div>
<div class="tg-footer">👁️ 1.38K · <a href="https://t.me/SBoxxx/19534" target="_blank">📅 20:13 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19533">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">بسنت وزیر خزانه داری آمریکا :
ما در مارس ۲۰۲۵ شروع کردیم. در دسامبر ۲۰۲۵، بزرگترین بانک در ایران فرو ریخت.
بانک مرکزی مجبور به چاپ پول شد و این باعث تورم گردید. اکنون آن‌ها قادر به پرداخت حقوق سربازان خود نیستند.</div>
<div class="tg-footer">👁️ 1.91K · <a href="https://t.me/SBoxxx/19533" target="_blank">📅 19:44 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19532">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">عجب پولیتیکی زده اند.  به نظرم مراکش — که بشدت در خط اسرائیل و آمریکا است — عامل اجرایی است. آمریکا و اسرائیل که هر دو با دولت چپگرای سانچز مشکل دارند به مراکش گفته اند این وحوش و و طیور را بفرست سمت اسپانیا؛   حالا 2 حالت پیش می آید:  — یا دولت سانچز با بی…</div>
<div class="tg-footer">👁️ 2.18K · <a href="https://t.me/SBoxxx/19532" target="_blank">📅 19:25 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19531">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">ترامپ:
شنیدیم که در مینه‌سوتا یک حمله سایبری رخ داده است. آن‌ها آن را به ایران نسبت دادند. من این را نمی‌پذیرم.
من آن را به مینه‌سوتا و فرماندار فاسدش نسبت می‌دهم.
آن‌ها دوست دارند بگویند، «آه، این ایران است. ایران باید خیلی خوش‌شانس باشد.»
ایران مشکلات بزرگتری نسبت به نگرانی درباره مینه‌سوتا دارد.</div>
<div class="tg-footer">👁️ 2.44K · <a href="https://t.me/SBoxxx/19531" target="_blank">📅 19:09 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19530">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">روسیه حدود 30 هزار تن بنزین از مراکش وارد کرده است تا کمبود سوخت ناشی از حملات پهپادی اوکراین به پالایشگاه‌های بزرگ را جبران کند.</div>
<div class="tg-footer">👁️ 2.48K · <a href="https://t.me/SBoxxx/19530" target="_blank">📅 19:03 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19529">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SfMVMwh2tjjfPFhXx_IpSFfjcbsqNV9xobwvfLVf26eRcopTV3DL4dPYAWF6cbGqX-M2TU2rP405IfXvQMWVxX3c7jPRvpJJ8cM34FTFDjtiEmSjg7xQ0vN0CGysBKWlqcxbooj7_yb2-77fGrlkGL0VnAjmH5ozNH6n68VKOHQEZ_QfR17WNa9gq8mcOneYd12wRIOQwFn181-CtpXs8Ouhlm7RoSjxFJZqcEhAPDuewGWua-BRFxxNAa9y1w9W-KNFsTFxbieUElpNY5UJ7KeDqVkLbiahqV-2mfiAz6rIG7Bu3tU-onjB8RmrtnasE7bY00GXXsTpNw7KhI_78A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">روسیه ممنوعیت صادرات بنزین را تا سال ۲۰۲۷ تمدید کرد!</div>
<div class="tg-footer">👁️ 2.46K · <a href="https://t.me/SBoxxx/19529" target="_blank">📅 19:03 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19528">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">اسرائیل طرح "هیئت صلح" رئیس جمهور ترامپ را که هدف آن خلع سلاح حماس بود، رد کرد. این کشور مدعی است که این طرح برای اسرائیل قابل قبول نیست و اسرائیل هر حقی را برای هدف قرار دادن و کشتن افراد در غزه دارد.</div>
<div class="tg-footer">👁️ 2.99K · <a href="https://t.me/SBoxxx/19528" target="_blank">📅 17:45 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19527">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">این اسپانیایی ها 700 سال زور زدند تا عربها و بربرها را از خاکشان بیرون بریزند؛ چپ ها در 2 سال دوباره همه آن کوششها را بر باد دادند!
چپ = نکبت</div>
<div class="tg-footer">👁️ 3.11K · <a href="https://t.me/SBoxxx/19527" target="_blank">📅 17:44 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19526">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">یک زن وحشت‌زده در سئوتا درخواست کمک از نیروهای نظامی می‌کند و می گوید: "ما تنها هستیم":  ما به حضور نیروهای نظامی در خیابان‌ها نیاز داریم. آن‌ها اینجا نیستند.  ما تنها هستیم.  چطور ممکن است من نترسم؟ من می‌لرزم. این یک تهاجم است.</div>
<div class="tg-footer">👁️ 3.04K · <a href="https://t.me/SBoxxx/19526" target="_blank">📅 17:37 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19525">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">عجب پولیتیکی زده اند.  به نظرم مراکش — که بشدت در خط اسرائیل و آمریکا است — عامل اجرایی است. آمریکا و اسرائیل که هر دو با دولت چپگرای سانچز مشکل دارند به مراکش گفته اند این وحوش و و طیور را بفرست سمت اسپانیا؛   حالا 2 حالت پیش می آید:  — یا دولت سانچز با بی…</div>
<div class="tg-footer">👁️ 3.1K · <a href="https://t.me/SBoxxx/19525" target="_blank">📅 17:36 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19524">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WlwBwLoH_E_-460M1QDDiZyeq_ZqkpjqrBx1AT-Y2dDEqZEufPvP_E0NZl7bpFN3Hq8sT4m7erBLHyyKh1Jono_9HVrM5v6rolT4ULGaZoe7NfMe7yZLC0GL6qlvEXr_-fVR4lGaiuXwDf4qEQqhgD6OSrXIPOkGMA2Xat8Ka3YlkBQ94tYpeVqGLk23BHrVlgrO-26JIWPIkXY0wMjO0xgHmllMKoTtlYORsiqO_5EAXi48Pu_hd6mhPNsewPBs5wiu1O2mdcjs_kuTPp-Et--UCTvSTRrWm6U1okDVw3SvIq9uPQuljYNV3VhUh00ZbQ0bS3aONwHiuSGHCRQWlQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#GRI  شاخص ریسک ژئوپولیتیک برای امروز بسیار بالاست و پیش بینی می شود طلا (و شاخص های سهام) زیر فشار فروش بروند. (خصوصاً شاخص های سهام)</div>
<div class="tg-footer">👁️ 3.02K · <a href="https://t.me/SBoxxx/19524" target="_blank">📅 17:22 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19523">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">ترامپ:
"جنگ با ایران به خوبی پیش می‌رود. ایالات متحده ضربه‌ای سنگین به ایران وارد می‌کند و ما به سادگی به پیروزی ادامه می‌دهیم</div>
<div class="tg-footer">👁️ 3.07K · <a href="https://t.me/SBoxxx/19523" target="_blank">📅 17:14 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19522">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">ترور یک مامور فراجا در ایرانشهر  به گزارش مرکز اطلاع‌ر‌سانی پلیس سیستان و بلوچستان، ساعتی قبل افرادی مسلح به سمت مأمور انتظامی در ایرانشهر با سلاح گرم تیراندازی کردند که در پی این اقدام، استوار یکم «مهران سالارزاده» به درجه رفیع شهادت نائل شد.</div>
<div class="tg-footer">👁️ 3.25K · <a href="https://t.me/SBoxxx/19522" target="_blank">📅 17:01 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19521">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">تنگه ای که استراتژیک نخواهد ماند  وقتی گفته می شود ایران‌ استراتژیک‌ است، بخش مهمی از این‌ گزاره به دلیل اشراف جغرافیایی ایران بر تنگه هرمز است. چون دستکم‌ یک پنجم انرژی فسیلی سالانه جهان از آن می گذرد. ولی گلدن ساکس مدعی است که تا امروز ۷ خط برای دور زدن…</div>
<div class="tg-footer">👁️ 3.14K · <a href="https://t.me/SBoxxx/19521" target="_blank">📅 16:59 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19520">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pskd7x3Lzgf-C-yV_TK5V7Oxo9Dvp7ce5QiW5TfgPSp4ODdGgSDcBBRIId4LiegkRuVTK0Da7XIPzP3v91GG_iCrnsQ0cI0ojNXq1xohcLUkwEIqEaJ2LAphDo-yb-6UoWwjOO1XzQh3BkH2elzTqLWahblzdZrx044pEjFnJw5SjBYieQTyNcJBzML8uFPzXPZdh5kn0WNbSBdwSZ3w4JkG3TjSSYKc_Rz_hSWOmLOcVDKCi5CJxJMbU_dTkd7HzZ6OulgAaed2pRAfLOCQ3MusSt1jRCVHik1lSUarjOJaWjTk45T610xmEjGKSzgbjX0-nx77PgIse7fv4oTsVg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در عصر اقتصاد دانش بنیان، تنگه بندی و گردنه گیری تنها منجر به انزوا و تیپا خوردن خود عامل می‌شود و اندونزیایی ها خیلی سریع فهمیدند که این لقمه برای دهانشان بزرگ است ولی خب.</div>
<div class="tg-footer">👁️ 3.65K · <a href="https://t.me/SBoxxx/19520" target="_blank">📅 16:59 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19519">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JZwgRO16lPIQym42yuMPiwa1V18fEyXEONii_lZWAk4wVNq6tPUlQoXB-lhQ1uhJvSQQk_LGBemRocQRJu9smDmq6XMJLS5hltgdiAU3hXtACXE_o7u15_W6xJyuldv8isf5dPtmDvr6GsUN3YfLxcC2IqiD0ldX0eiFtnugIC8ehaT7FCmkPIWe_PIpz0ruw6qyxdt_1e-Fv-FqYIAdaaLqu6wB8m7I04si7NszNqomXA8l2_Z8YO4XgoC5e6XwIjL2W9uaH8GKjfKcn62T6v_g_DRIR-NzOLJYjuCvpogZSOTwYG_nDpyFzEMxwtmHVJosbiFBsCJIJe1Tgo_WBw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">همکاری نظامی اسرائیل-مراکش و پیام راهبردی به مادرید  همکاری نظامی اسرائیل و مراکش دیگر صرفاً یک رابطه تجاری در حوزه صنایع دفاعی نیست؛ این همکاری به تدریج به یکی از مهم‌ترین مؤلفه‌های معادلات ژئوپلیتیکی غرب مدیترانه تبدیل شده است. از انتقال فناوری پهپادهای…</div>
<div class="tg-footer">👁️ 3.63K · <a href="https://t.me/SBoxxx/19519" target="_blank">📅 15:18 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19518">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">GeoMarkets - podcast 16</div>
  <div class="tg-doc-extra">Ali SharifAzadeh</div>
</div>
<a href="https://t.me/SBoxxx/19518" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">#پادکست_GeoMarkets
شماره — 16
جمعه 31 جولای 2026</div>
<div class="tg-footer">👁️ 3.67K · <a href="https://t.me/SBoxxx/19518" target="_blank">📅 14:46 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19517">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">یک کشتی حمل گاز قطری که میخواسته از مسیر تعیین شده ایران عبور کند توسط آمریکا متوقف شد!</div>
<div class="tg-footer">👁️ 3.75K · <a href="https://t.me/SBoxxx/19517" target="_blank">📅 14:35 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19516">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">ایالات متحده و اسرائیل در حال بررسی محاصره زمینی ایران برای افزایش فشار اقتصادی هستند!  این پیشنهاد به دنبال متقاعد کردن کشورهای همسایه — از جمله افغانستان، ارمنستان، آذربایجان، عراق، پاکستان، ترکیه و ترکمنستان — برای محدود کردن یا بستن گذرگاه‌های مرزی با…</div>
<div class="tg-footer">👁️ 3.89K · <a href="https://t.me/SBoxxx/19516" target="_blank">📅 13:48 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19515">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">ایالات متحده و اسرائیل در حال بررسی محاصره زمینی ایران برای افزایش فشار اقتصادی هستند!
این پیشنهاد به دنبال متقاعد کردن کشورهای همسایه — از جمله افغانستان، ارمنستان، آذربایجان، عراق، پاکستان، ترکیه و ترکمنستان — برای محدود کردن یا بستن گذرگاه‌های مرزی با ایران است تا واردات و صادرات این کشور را محدود کند.
این پیشنهاد در کنار سایر گزینه‌ها از جمله حفظ محاصره دریایی، از سرگیری حملات نظامی یا پیگیری یک توافق دیپلماتیک مورد بحث قرار گرفت.
طرفداران این راهبرد استدلال می‌کنند که انزوای اقتصادی بیشتر می‌تواند دولت ایران را تضعیف کند، اگرچه تحلیلگران اشاره می‌کنند که اجرای یک محاصره زمینی با توجه به مرزهای زمینی طولانی و ارتباطات منطقه‌ای گسترده ایران بسیار دشوار خواهد بود.
— تلگراف</div>
<div class="tg-footer">👁️ 4.05K · <a href="https://t.me/SBoxxx/19515" target="_blank">📅 13:46 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19514">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">گفته می‌شود عربستان سعودی در حال آماده‌سازی یک تهاجم نظامی بزرگ علیه حوثی‌ها است که برنامه‌های آن می‌تواند شامل عملیات دریایی در دریای سرخ و حمله زمینی در یمن مرکزی باشد.
این اقدام پس از حملات حوثی‌ها به تأسیسات نفتی عربستان و محاصره کشتیرانی عربستان توسط این گروه صورت گرفته است.
منبع: گاردین</div>
<div class="tg-footer">👁️ 3.94K · <a href="https://t.me/SBoxxx/19514" target="_blank">📅 13:31 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19513">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">🔴
روز دوم تهاجم مراکشی ها به اسپانیا آغاز شد. خیلی از اسپانیایی ها از پادشاه اسپانیا خواسته اند پدرو سانچز را خلع کند و ارتش اسپانیا را به مرز های جنوبی بفرستد.
✍🏻
Desert Eagle
▪️
@World_Newsly</div>
<div class="tg-footer">👁️ 4.54K · <a href="https://t.me/SBoxxx/19513" target="_blank">📅 12:33 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19512">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromاخبار نظامی ایران و جهان</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3ff08dba4f.mp4?token=XJOlIYhKQu4kSV4zkUjC9WHdHT97Vhj62WQsKcS-FVsYchZByJe4wd2BMh_IqEPDSA7oGzl0KNWaAdRxWEQ3K9jfZ4N4c3k_OwzcwcsuINZKzlKb5961gRoXBhDFK6W37sWNriRiEPdQZSSd7gamcYpG51c4tfdcatO9W7k2VBH8lazMgxLh5SX3LKR582EyxLcdynskImyqt9aaE7j-uiVluwESbs3lwtuTqu7jwbtSLNL9sa0OX-uc9UsVxBuBRIBk_XuzRcq34oVhRK1yt_3QTaEWjK5dHgDQhgVXTj36WQheEn-sqrhRGqSBd96Io8l570iG7YJ5ZWGwO1aFFw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3ff08dba4f.mp4?token=XJOlIYhKQu4kSV4zkUjC9WHdHT97Vhj62WQsKcS-FVsYchZByJe4wd2BMh_IqEPDSA7oGzl0KNWaAdRxWEQ3K9jfZ4N4c3k_OwzcwcsuINZKzlKb5961gRoXBhDFK6W37sWNriRiEPdQZSSd7gamcYpG51c4tfdcatO9W7k2VBH8lazMgxLh5SX3LKR582EyxLcdynskImyqt9aaE7j-uiVluwESbs3lwtuTqu7jwbtSLNL9sa0OX-uc9UsVxBuBRIBk_XuzRcq34oVhRK1yt_3QTaEWjK5dHgDQhgVXTj36WQheEn-sqrhRGqSBd96Io8l570iG7YJ5ZWGwO1aFFw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
روز دوم تهاجم مراکشی ها به اسپانیا آغاز شد.
خیلی از اسپانیایی ها از پادشاه اسپانیا خواسته اند پدرو سانچز را خلع کند و ارتش اسپانیا را به مرز های جنوبی بفرستد.
✍🏻
Desert Eagle
▪️
@World_Newsly</div>
<div class="tg-footer">👁️ 3.95K · <a href="https://t.me/SBoxxx/19512" target="_blank">📅 12:30 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19511">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uuGzuVAAjgjIcZLsK9yXPJe_9OyvBPD45vxLpMaeiAyrYKaDlH0jAGXja1iDS7QCJOhCYzUSacsfwExSLjaPaD4gO_P_b5yK0VQ9I6amQNDFg0U1hbKk5DwkjW7qDm7DoJXOjaggD7ntZ1XAALkIcZuA5xZ2iPUonqXNNCtVoJq3ENNLqqypeRTXj9sGXEcqe9_lvunPMRMlbectzA8PRqVYQGuOiob5tZr2QGrSIcS9rEA69YhpA_fDLm5vFJDzMphy9e45IwpuGh64_kpD2cWIqujlGiyqFxJ6tASa3p2MqeR79eMn6afou3FF8mvyxklTFepVF_MB70ioGSgudA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">GeoMarkets Podcast Text.pdf</div>
<div class="tg-footer">👁️ 4.02K · <a href="https://t.me/SBoxxx/19511" target="_blank">📅 12:14 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19510">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">خب سیگنال پایان موج 2 از 5 دارد صادر می شود:
استاد خوش چشم: فک نکنم‌ دیگر جنگ بشود</div>
<div class="tg-footer">👁️ 4.05K · <a href="https://t.me/SBoxxx/19510" target="_blank">📅 12:00 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19509">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">پلیس:  زائران بازگشت از اربعین را به روزهای پایانی موکول نکنند</div>
<div class="tg-footer">👁️ 4.04K · <a href="https://t.me/SBoxxx/19509" target="_blank">📅 11:54 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19508">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">پلیس:
زائران بازگشت از اربعین را به روزهای پایانی موکول نکنند</div>
<div class="tg-footer">👁️ 4.04K · <a href="https://t.me/SBoxxx/19508" target="_blank">📅 11:54 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19507">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">صدها مهاجر جوان امروز صبح به سوی سئوتا در اسپانیا شنا کردند. بیش از ۱۷۰۰ نفر در یک هفته.</div>
<div class="tg-footer">👁️ 4.12K · <a href="https://t.me/SBoxxx/19507" target="_blank">📅 11:51 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19506">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OFsdrzwxbQZ1PYPSAuKOjmmOqDqIUIapXoyOCgDsurOFvbvEXVDsp9L6BAZeCGgn4iLRMNxEbg0JYfC4704Y-SXoTihl0J-to9NM70X7gCpFk30PoxTVTv5DPoFPN_U89JF_yY1dv7oB2PXZqiVl4cXhSnuqmWlU9bkVwz-mLcK6ky3ajprHhVEdEDKNJFFw7wCL7tUXQ9ceXyOM4NynhLtroPAZGjOiNQ2LYRWfSy_eV8nQO9Z88lsTnQBDwa13_qQebzSNwOM8iqlsGJVC5ejtmK1pf4yMrE6O94BnkL95xdrB4rd-OGKrftKToO_0xsZ6eRPtZBo1wDRzVOe0MA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#GRI
شاخص ریسک ژئوپولیتیک برای امروز بسیار بالاست و پیش بینی می شود طلا (و شاخص های سهام) زیر فشار فروش بروند. (خصوصاً شاخص های سهام)</div>
<div class="tg-footer">👁️ 4.13K · <a href="https://t.me/SBoxxx/19506" target="_blank">📅 11:47 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19505">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iWkO67TO8fLlNOg9KbCzNJrUEYbZOBx1p8kKTNtsv7DYe--Ycr4_LtQSyDn2S2CSkeVNKMXacHIyGLZo0TW9JQPXzz85cu6xsl2-wEwW4V9BxGruze0Q_9BbpbRusacO2vtLLWBgTs1MtC02yx4u1ikoZlZKcZhJxaN1fDrtu_uczJDPzVzXixVnWyNXACZcIqLuyQi4bDWfMeZvHI0CaxEyB2jVoj4c9ngYEs6DxOm96R6fmt4We9jDYfr9f1baYDjh6Z3eAZcbwTkTxW4dJqjQ05hSgybscu3sSWiptwHPpboAOrFk5eae3rRUUWn0MEalTIqRBcJa3IJMLIVLvQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#GRI  شاخص ریسک ژئوپولیتیک امروز در سطح میانه پایین است و حالت رنج برای طلا پیش بینی می شود.</div>
<div class="tg-footer">👁️ 4.24K · <a href="https://t.me/SBoxxx/19505" target="_blank">📅 11:42 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19504">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">شلیک موشک از ایران</div>
<div class="tg-footer">👁️ 4.42K · <a href="https://t.me/SBoxxx/19504" target="_blank">📅 10:52 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19503">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">مجری
: آیا می‌دانید چند روس در این جنگ کشته شده‌اند؟ آیا تخمینی دارید؟
زلنسکی
: مجموع تلفات روسیه ۱,۶۰۰,۰۰۰ نفر است و حدود ۷۰۰,۰۰۰ نفر کشته شده‌اند. تقریباً.</div>
<div class="tg-footer">👁️ 4.56K · <a href="https://t.me/SBoxxx/19503" target="_blank">📅 10:40 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19502">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">قالیباف:
ایالات متحده هر روز دست‌های خود را با جنایت جدیدی آلوده می‌کند؛ حمله تروریستی به خانه‌های مسکونی غیرنظامیان در جزیره قشم ادامه‌ای بر فجایع میناب و لامرد است.
آمریکایی‌ها عادت کرده‌اند که با ریختن خون بی‌گناهان، برای ضرباتی که در میدان نبرد دریافت می‌کنند جبران کنند.
آن‌ها بهای آن را خواهند پرداخت.</div>
<div class="tg-footer">👁️ 4.51K · <a href="https://t.me/SBoxxx/19502" target="_blank">📅 10:33 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19501">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">ترامپ اعلام کرد که حماس به طور کامل سلاح‌های خود را تحویل داده و غزه «در دستان یک دولت فلسطینی جدید که در خدمت مردم خود است» قرار خواهد گرفت.</div>
<div class="tg-footer">👁️ 5.03K · <a href="https://t.me/SBoxxx/19501" target="_blank">📅 02:15 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19500">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">مجری فاکس نیوز:
آیا کشورهای دیگر در منطقه که توسط ایران مورد حمله قرار گرفته‌اند، در حال تماس و تمایل به شراکت با اسرائیل هستند؟
نتانیاهو:
بیشتر از آنچه فکر می‌کنید. بیشتر از آنچه می‌توانم بگویم.</div>
<div class="tg-footer">👁️ 4.93K · <a href="https://t.me/SBoxxx/19500" target="_blank">📅 01:55 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19499">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">نصب سیم خاردار روی پنجره ها از سوی مردم اسپانیا برای مقابله با موج سرقت و جنایت مهاجرین آفریقایی</div>
<div class="tg-footer">👁️ 4.93K · <a href="https://t.me/SBoxxx/19499" target="_blank">📅 01:53 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19498">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AeKfn93j77VxC7IZ-vOUShCd37s3_tBQS0HfNd6HvvfrBCsSCpnVmuVI3mLIIFzG3xKv60HL0PHpDrJYt5kUCt94Q35DejAlDXPiOtNwIvqiuBnm7Cdc6HOfL22PaIUSNCM-4-nxU1tiWgNZwVi4TqhBeH5Ymex14pvsCtwpVdI0UjXnN__eynDUH84iBqeTAvgOtQP7ERi1FL6QRTm_5QoN3nzuvn1sD29E3n_lBeErVj6n8pum8zXFPk3faKKpynlj6akpccFqMQfv8IhpfBUNF1hS6ns6hmA8VazcgAX4YdBlUSGgHd3H9JdwWfcQZVVVABPT6_WU67b1iyIs6A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">صدها مهاجر جوان امروز صبح به سوی سئوتا در اسپانیا شنا کردند. بیش از ۱۷۰۰ نفر در یک هفته.</div>
<div class="tg-footer">👁️ 5.08K · <a href="https://t.me/SBoxxx/19498" target="_blank">📅 01:52 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19497">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">▶️
Snow-like dust covers towns across southern Lebanon following violent Israeli explosions.  @PressTV</div>
<div class="tg-footer">👁️ 4.74K · <a href="https://t.me/SBoxxx/19497" target="_blank">📅 01:49 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19496">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromPress TV</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6d0fce5d57.mp4?token=A6HAWRm9IMzzXRMu5Jt-QOi_A79PT9BRtJpVXr7gDp-vutkWK_OK4iVqVAyMafiV28zq9Nk82iCSCznrRXsuGSbQ_p0n8z8yGt0mkqq6BdLB0Q71pcCgyuYCybR54rcRNh77P5fM_VcWrHgDvIHs6PkhMQjQCUV-gJUQmDbakOf64fBTHhEWnnhipQCdtkPnAXeUEPlsa0ovLDXr0zcXhkz_wz11QKjTohWm8W31VpIsip6NLLDcxMuDipixuSLLWgk2aTtYlhqvfVFwB_xZpRxCfC9rEegMenTZ14m87alPfMK53yMPi-mOqEedno1t7o50o6yohT8lPNibRuQcNQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6d0fce5d57.mp4?token=A6HAWRm9IMzzXRMu5Jt-QOi_A79PT9BRtJpVXr7gDp-vutkWK_OK4iVqVAyMafiV28zq9Nk82iCSCznrRXsuGSbQ_p0n8z8yGt0mkqq6BdLB0Q71pcCgyuYCybR54rcRNh77P5fM_VcWrHgDvIHs6PkhMQjQCUV-gJUQmDbakOf64fBTHhEWnnhipQCdtkPnAXeUEPlsa0ovLDXr0zcXhkz_wz11QKjTohWm8W31VpIsip6NLLDcxMuDipixuSLLWgk2aTtYlhqvfVFwB_xZpRxCfC9rEegMenTZ14m87alPfMK53yMPi-mOqEedno1t7o50o6yohT8lPNibRuQcNQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
Snow-like dust covers towns across southern Lebanon following violent Israeli explosions.
@PressTV</div>
<div class="tg-footer">👁️ 4.74K · <a href="https://t.me/SBoxxx/19496" target="_blank">📅 01:48 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19495">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">عباس عراقچی، وزیر امور خارجه ایران:  "مصر یک دوست و شریک مهم در منطقه است و امنیت آن برای ما از اهمیت بالایی برخوردار است.  ما همگی باید در برابر توطئه‌ها و عملیات‌های فریبکارانه اسرائیل که با هدف تضعیف صلح منطقه‌ای طراحی شده‌اند، هوشیار باشیم.  تهدید آشکار،…</div>
<div class="tg-footer">👁️ 4.81K · <a href="https://t.me/SBoxxx/19495" target="_blank">📅 00:25 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19494">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">به نظر می رسد مصر هم کم کم به لیست اهداف مشروع ما بپیوندند.</div>
<div class="tg-footer">👁️ 4.85K · <a href="https://t.me/SBoxxx/19494" target="_blank">📅 00:24 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19493">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">عربستان سعودی ائتلاف چندملیتی برای محافظت از مسیرهای دریایی کلیدی را اعلام کرد
عربستان سعودی تشکیل یک
ائتلاف دفاع دریایی چندملیتی
را اعلام کرده است. هدف تضمین آزادی ناوبری و مسیرهای تجاری بین‌المللی در
تنگ باب‌المندب
، در
دریای سرخ
و در
خلیج عدن
است.
بر اساس وزارت دفاع سعودی،
۱۴ کشور
در حال حاضر از این ابتکار حمایت می‌کنند:
بحرین، جیبوتی، مصر، اردن، کویت، مالدیو، پاکستان، قطر، سومالی، سودان، ترکیه، یمن، عربستان سعودی و شورای رهبری ریاست جمهوری یمن.
بر اساس وزارتخانه، سایر کشورهایی که در مشورت‌ها شرکت کردند، در مرحله نهایی رای‌گیری‌های سیاسی داخلی برای پیوستن به ائتلاف هستند.</div>
<div class="tg-footer">👁️ 5.1K · <a href="https://t.me/SBoxxx/19493" target="_blank">📅 21:59 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19492">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">— منابع یمنی معتقدند که عربستان سعودی در حال آماده‌سازی برای یک تهاجم نظامی بزرگ علیه حوثی‌ها از طریق دریا و احتمالاً از طریق خشکی در یمن مرکزی است تا گلوگاه صادرات نفت خود را در دریای سرخ جنوبی آزاد  کند.
— گاردین |</div>
<div class="tg-footer">👁️ 4.93K · <a href="https://t.me/SBoxxx/19492" target="_blank">📅 21:46 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19491">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">وزارت دفاع آمریکا، قرارداد ۵۸ میلیارد دلاری برای سیستم پدافند هوایی پاتریوت به شرکت لاکهید مارتین اعطا کرد.
این قرارداد به ارزش تا ۵۸.۶ میلیارد دلار، مربوط به موشک‌های رهگیر پاتریوت است و تولید این سیستم را تا سال ۲۰۳۲ افزایش می‌دهد. این اقدام در حالی صورت می‌گیرد که درگیری‌های مداوم در ایران و اوکراین، ذخایر سامانه‌های پدافند هوایی آمریکا را کاهش داده است.</div>
<div class="tg-footer">👁️ 4.99K · <a href="https://t.me/SBoxxx/19491" target="_blank">📅 20:44 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19490">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">GeoMarkets Podcast Text.pdf</div>
  <div class="tg-doc-extra">329.6 KB</div>
</div>
<a href="https://t.me/SBoxxx/19490" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">Ali SharifAzadeh – GeoMarkets - podcast 15</div>
<div class="tg-footer">👁️ 4.99K · <a href="https://t.me/SBoxxx/19490" target="_blank">📅 20:20 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19489">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">صدها مهاجر جوان امروز صبح به سوی سئوتا در اسپانیا شنا کردند. بیش از ۱۷۰۰ نفر در یک هفته.</div>
<div class="tg-footer">👁️ 5.24K · <a href="https://t.me/SBoxxx/19489" target="_blank">📅 19:36 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19488">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">در صنعا توفان و رعد و برق شده، فکر کرده اند عربستان حمله کرده !</div>
<div class="tg-footer">👁️ 4.95K · <a href="https://t.me/SBoxxx/19488" target="_blank">📅 19:02 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19487">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">رهبر حوثی‌های یمن، عبدالملک الحوثی، درباره عربستان سعودی:
آن‌ها دام‌ها را نابود کردند؛ شترها و گوسفندان. حتی حیوانات بارکش و الاغ‌ها نیز از رژیم سعودی در امان نبودند.</div>
<div class="tg-footer">👁️ 4.94K · <a href="https://t.me/SBoxxx/19487" target="_blank">📅 19:01 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19486">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-footer">👁️ 4.81K · <a href="https://t.me/SBoxxx/19486" target="_blank">📅 18:59 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19485">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KYrZlHByrU-rgKFayaX9ttvJZ0yyqKJkSM0jslSNsAP7G878hwn3GoBg6Wp361Q38v_OU2SGzqTY_XjAaxQbqqh-wi94YrbMU-Ba3s7fVP1Ms5j3hplNRXyLghA8y0gz8utG8ZxEG8fi-i4X48twO3moOEz3crSbnttXfAR99vlJRR76DegGpBVuNgGZye2oSaDNVNkFz3QAzInVHZricbesjNn0dYR3NwJW5zV3Zd6kl-peDHFl5B1MagvVZItkWG0ES-liRC5dnawPTBoVjrbNzSOMmJtkOXmhUNJtqTLGmG8ps9baHT5A94azhTVhrVkoE-UjyxcfgQKmneiQ7w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شما ببینید در روزهای اخیر اینها به لیست اهداف مشروع ما افزوده شده اند:  — بلغارستان — بریتانیا  — اوکراین</div>
<div class="tg-footer">👁️ 4.95K · <a href="https://t.me/SBoxxx/19485" target="_blank">📅 18:24 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19484">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/K1riO7lBa2wkMZS1zm1PDWPF0F2ZA0Odq5SwtfYT7bA4q5EEo4lsLBGDjmQWw16I01onJJCbxJLPhJKNscE3ynhEZDq1dTBqxoAwxDkTy7BKZPi9J84pSGJtc4Zs-Ek77SnM-TS3AVdaBJQD3YmNvDrcsHH-XHzzvjyk3xy5zPnh_6xNWpwEblW9b5RN4ZVTmLN7HGIxWmUGNxhIY3qGlEGULrDqzR279oDEh5SbzQFmUyUUC6LK3oqnbrCuCIMqlxB_rGUtV7fvAE1FQStsDHbAkAXKvxgKeaOxKH-SoptboFwwHvNsCbPDQrbxtBRF1ZE1HDPqnZ0EkxibQpiAcw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">صدها مهاجر جوان امروز صبح به سوی سئوتا در اسپانیا شنا کردند. بیش از ۱۷۰۰ نفر در یک هفته.</div>
<div class="tg-footer">👁️ 4.96K · <a href="https://t.me/SBoxxx/19484" target="_blank">📅 18:20 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19483">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">روسیه ممنوعیت صادرات بنزین را تا سال ۲۰۲۷ تمدید کرد!</div>
<div class="tg-footer">👁️ 4.76K · <a href="https://t.me/SBoxxx/19483" target="_blank">📅 18:17 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19482">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">— مشاوران و اعضای کابینه ترامپ گزینه‌هایی برای انجام عملیات نظامی گسترده‌تر علیه ایران را به وی ارائه دادند.
— فاکس نیوز</div>
<div class="tg-footer">👁️ 4.84K · <a href="https://t.me/SBoxxx/19482" target="_blank">📅 18:09 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19481">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">سپاه پاسداران: ایران پایگاه هوایی الازرق را در پاسخ به حمله آمریکا به قشم، با نابودی سه فروند اف-۳۵ حمله کرد
سپاه پاسداران انقلاب اسلامی حمله موشکی انتقام‌جویانه به پایگاه هوایی العزرق در اردن را پس از حمله آمریکا به خانه‌های مسکونی در جزیره قشم اعلام کرد.
طبق بیانیه سپاه، این حمله به منطقه استقرار و محل نگهداری اف-۳۵ هدف قرار گرفت و سه فروند از هواپیماهای اف-۳۵ را نابود کرد و سه فروند دیگر را به شدت آسیب رساند. چندین افسر آمریکایی و پرسنل فنی نیز کشته شدند.
سپاه گفت که این عملیات در پاسخ به حمله آمریکا به قشم انجام شد که منجر به زخمی شدن اعضای یک خانواده محلی، از جمله کودکان، شد.
در این بیانیه همچنین از اردنی‌هایی که با حضور نظامی آمریکا در کشورشان مخالف هستند، تشکر شد و گفته شد که موضع آن‌ها فشار بر نیروهای آمریکایی را افزایش داده است.
سپاه در پایان با تأکید بر ادامه عملیات علیه حضور نظامی آمریکا در منطقه، بیانیه خود را به پایان رساند.</div>
<div class="tg-footer">👁️ 5.4K · <a href="https://t.me/SBoxxx/19481" target="_blank">📅 14:45 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19480">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">کشته شدن ۳ عضو سپاه پاسداران در حمله آمریکا به زنجان</div>
<div class="tg-footer">👁️ 5.01K · <a href="https://t.me/SBoxxx/19480" target="_blank">📅 14:09 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19479">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">GeoMarkets - podcast 15</div>
  <div class="tg-doc-extra">Ali SharifAzadeh</div>
</div>
<a href="https://t.me/SBoxxx/19479" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">#پادکست_GeoMarkets
شماره — 15
پنجشنبه 30 جولای 2026</div>
<div class="tg-footer">👁️ 5.31K · <a href="https://t.me/SBoxxx/19479" target="_blank">📅 13:45 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19478">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iSBMfu4k1wrVUEj6gNC2AC6Ul7ZLwJJeFexD9gMiyIge8CCcacitEj2wORtQcrxfBpdqWPdNk23c30uU8KoPa2vnHDmVgFIuz4HGjw688rjbVlA5gfSDNs_MsXWbU6vNevLO84U0PXbhTmd6oRAt2AcuTGXvK8DBzQlPkqIPgUZeMYsgrz_oVV-SVL9i3lWUOBDZYE0NNJSGNDi0G8VF1ShiV8ypwwnr1Ubmi2Y1eVF7KStg7tYYcDv3a_ln9sGG-GvEdArbMQqtwvjrE97A9EHMDOBBlw10ckgwst55OjTmUvhTsVdiQ8DRycTn2aoVAr-CGNTyKSmaJfK_RK3SPw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">لینک نشست دیروز با نیما</div>
<div class="tg-footer">👁️ 5.25K · <a href="https://t.me/SBoxxx/19478" target="_blank">📅 12:04 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19477">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e8eacd406a.mp4?token=Y9MyWmW48MW0dbeuf8PqpHgFx7tnOjB573xCq3ugkH2XtO-o79FfCbPrugwiQiuuO2JJ9RFBpH0cjc77HuQgHmlghzxrNpllPDNmJ9mfVurfGHGngQmRWy-dh3h_Fg0rh8Upn4AN0JF2DpVaRYt-enaN731HTx5sKug19xc6X4UFX-xRXu6TPZ8y2MJ1bYyX4KA3bMB8l1esECAdtGOWvfVYse2vhEK_qV6hBxqvzE5pL6dDsOMv5hfNwfszEUhCTbIHoj--eOOdwBKa4gZKZfDHXGAiFUn-gl2dqaRfd7084tVYIXeHUtfpi1YyCZl9_KCrv0RUErIL5DO28itUkg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e8eacd406a.mp4?token=Y9MyWmW48MW0dbeuf8PqpHgFx7tnOjB573xCq3ugkH2XtO-o79FfCbPrugwiQiuuO2JJ9RFBpH0cjc77HuQgHmlghzxrNpllPDNmJ9mfVurfGHGngQmRWy-dh3h_Fg0rh8Upn4AN0JF2DpVaRYt-enaN731HTx5sKug19xc6X4UFX-xRXu6TPZ8y2MJ1bYyX4KA3bMB8l1esECAdtGOWvfVYse2vhEK_qV6hBxqvzE5pL6dDsOMv5hfNwfszEUhCTbIHoj--eOOdwBKa4gZKZfDHXGAiFUn-gl2dqaRfd7084tVYIXeHUtfpi1YyCZl9_KCrv0RUErIL5DO28itUkg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">عبور موشک های زمین به زمین اتکمز آمریکایی بر فراز شهروندان کویتی به سمت شهرهای خوزستان</div>
<div class="tg-footer">👁️ 4.9K · <a href="https://t.me/SBoxxx/19477" target="_blank">📅 11:46 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19476">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lu8qH5WXwwktO0gGpbmmcgzOi8WRYhc4esaGVE5CjbAoloSDeQMK4hiBr7T3qGO1Cq-4zMveDUkxLKvEqJFe5DkMWd5xMcodFAJlyshFvOp820d4dHu1O_Wsbim_jRhYY4SX_lk_QycClJwJjPOMMZSfrL8PGhZn95T1-OkV6WjAKgj0ny-Ruoe4DQZEnenFuU4QoHEh1qblxZ8j7g1kfNg8ogLUmzbbpKvreY5mKkESPlzdkbboIIKfhAi2uEevgu9DRaqaQiDb0qrNhJBP9Hp6dxDkpouTs3jtP-bGfVcq_tEnvVU3j13ET97u5S-AEToCZnUIwrapg89C-UC-0A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این همان حرامزاده ای است که دختران را در لایوهای خودش کتک می زد و به آنها اهانت می کرد که خوشبختانه به این روز افتاده و تا مدتها نخواهدتوانست شرارت کند.</div>
<div class="tg-footer">👁️ 4.83K · <a href="https://t.me/SBoxxx/19476" target="_blank">📅 11:42 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19475">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bmAek-BXV3D8RzjK_dgJeSQCEJOCLNKEHLILRACpLFgHt5WFXph98J_eS_mnhOgSdrHF6St4PJQ6nA1pB1509ptS51d1J5vebl-Z9UDqjZtAWgCQ730hlopH5tHT4MwB-KM6rqTrqqsNjDTvU_8lAmMRN0tlBWykiP9PRarNx6sx2DIA05H8NZ71HVZV-628H7VB7Flf1c24aG7LfEcfGBlX1Bkz87jNa-tPFg0qXOWWwZd--wzGEkkZeH_jXwTQ1XCi0xWsZH07lccbEvhULaZXohCOFFkmacRqIdzD25VIVqtqtwS5Y73Ufybz5SvcxLvqDEM_jbBDsMzXHHc80g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">صدها چهره سیاسی، حقوقی و عمومی اردنی، نامه‌ای سرگشاده امضا کرده‌اند و خواستار خروج نیروهای آمریکایی از اردن شده‌اند.
آن‌ها حضور آمریکا را یک خطر امنیتی، سیاسی و اقتصادی می‌دانند که این کشور را به جنگی می‌کشد که تمایلی به آن ندارد.
این یک اقدام نادر و علنی است در کشوری که به شدت سرکوب‌گرانه با مخالفان برخورد می‌کند.
اکثر رسانه‌های اردنی از انتشار این نامه خودداری می‌کنند، و برگزارکنندگان هشدار می‌دهند که امضاکنندگان ممکن است به زندان محکوم شوند.
خشم عمومی در حال افزایش است، زیرا ایران همچنان به هدف قرار دادن حدود ۴۰۰۰ سرباز آمریکایی مستقر در اردن ادامه می‌دهد.
آژیرها در سراسر کشور به صدا در می‌آیند، و بقایای موشک‌های رهگیری شده در مناطق مسکونی سقوط می‌کنند.
این هفته، در پارلمان، یکی از نمایندگان به دلیل پیشنهاد تسلیت برای سربازان آمریکایی که در خاک اردن کشته شده‌اند، مورد انتقاد شدید قرار گرفت.
یکی دیگر از اعضا، ارتش آمریکا را به کشتن "کودکان، زنان و سالمندان" متهم کرد.
دولت همچنان به این ائتلاف متعهد است، عمدتاً به این دلیل که واشنگتن سال گذشته ۱.۶۵ میلیارد دلار کمک اقتصادی و نظامی به اردن ارائه کرده است.
اما جنگ بخش گردشگری اردن را نابود کرده است که تا ۱۸ درصد از درآمد سالانه دولت اردن را تشکیل می دهد
منبع: نیویورک تایمز</div>
<div class="tg-footer">👁️ 4.66K · <a href="https://t.me/SBoxxx/19475" target="_blank">📅 11:33 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19474">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/M6IbbXzzYYDVNOWpxOsHAKoAEi-gbIYRSPbAJ7UDVV-HnvsfHFdE--5Qdo2QjbR1mRMtFN6UBfNL18fsLLJnpGo6z-j_Xfp2rlTr8VL1iQZti6eiRgUNkmc3t3gQwvAkgKoc876yMjzUcjdqsjM-9sHJ741nuv08Q15lh-FxMusbLy4iMamcyU4ej1k2Z8Gf_jQjr_2rx5FoNRYDoclZlo0Jd1pzWV1ygIdbnk0hPpCdkxwpPwRs8bLorio-iTT2K6iumWjhC64LhY497dUPRqfzWehfQ7C-Nryj_DN1_Vi6584me2OX6fvwCuvmyVAZslc8f2xk1M0ocBtDXSH5KQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اهداف حمله پریشب حمله مشترک سعودی و آمریکا به پایگاه های حشدالشعبی در عراق</div>
<div class="tg-footer">👁️ 4.63K · <a href="https://t.me/SBoxxx/19474" target="_blank">📅 11:28 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19473">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">سپاه پاسداران:
با استعانت از خدای متعال، متجاوز همین امروز تنبیه خواهد شد.</div>
<div class="tg-footer">👁️ 4.79K · <a href="https://t.me/SBoxxx/19473" target="_blank">📅 11:06 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19472">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/l2F0zvb9-JEC9KNWCJA4q6UlVDDCl1tkEC6qQkpJ5KksMHbC96qU4378ObEONB4XmQa_XGwkIWnZwpF3ZDGCqKydlh7bE_tdUdP1bE2gygoPuR4Ix4L9nfqolsUlM1x3Ma1c4-u8RhbiSiFq8HhMTsu_E2-IhobCdtOmoHwI-y4r11aOwOhFG724mKKrNj3hYOyIfSzcsEaoQfGNVAVoh0z6-2vwddAyLXG2Yfr5YX-rt_JcGmASn6c3i6mA6MM5BKEF81vlkjfVq3WjGaK8LUnX6LxMtnq7pgYjKsaZ7vZIhK1UFe2sIKU2fwdPFD5Xd6_VXq6TUck-2ho0kIOeVw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#GRI
شاخص ریسک ژئوپولیتیک امروز در سطح میانه پایین است و حالت رنج برای طلا پیش بینی می شود.</div>
<div class="tg-footer">👁️ 4.65K · <a href="https://t.me/SBoxxx/19472" target="_blank">📅 11:03 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19471">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">این تحلیل درست 4 روز پس از پایان جنگ 40-روزه ارائه شد و همچنان بر اعتبار آن افزوده می شود و خواهیم دید روزی می رسد که تنگه هرمز را فقط خودمان استفاده خواهیم کرد.  از همه کریدورها که محروم ماندیم و سهممان .... های باقر شد این هم از تنگه هرمز!</div>
<div class="tg-footer">👁️ 4.86K · <a href="https://t.me/SBoxxx/19471" target="_blank">📅 10:14 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19470">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">پرسش: اوایل این ماه، رئیس‌جمهور ترامپ در مصاحبه‌ای با یک خبرنگار گفت که در رابطه با شما، همه می‌دانند که چه کسی رئیس است، یعنی خودش. او کسی است که تصمیم‌گیری‌ها را انجام می‌دهد. آیا شما هم این‌طور فکر می‌کنید؟
نتانیاهو: خب، شما می‌دانید که در آمریکا اغلب می‌گویند ترامپ هر کاری را که من می‌گویم انجام می‌دهد. و در اسرائیل، اغلب می‌گویند من هر کاری را که او می‌گوید انجام می‌دهم.
و گاهی اوقات، این مسائل توسط هر کسی، از جمله رئیس‌جمهور، در بحث‌های عمومی مطرح می‌شوند. اما حقیقت این است که ما شرکا هستیم. ما متحد هستیم.
او شریک ارشد است. این کشور ایالات متحده آمریکا است. بیایید این را فراموش نکنیم. و من شریک فرعی هستم، اما من نخست‌وزیر اسرائیل هستم.
و وقتی لازم باشد، من برای دفاع از منافع کشورم و امنیت کشورم، این کار را انجام می‌دهم.
منبع: خبرگزاری ABC News</div>
<div class="tg-footer">👁️ 4.76K · <a href="https://t.me/SBoxxx/19470" target="_blank">📅 10:11 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19469">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">نتانیاهو:
ترامپ اساساً سه گزینه پیش رو دارد: اول، دستیابی به یک توافق؛ دوم، ادامه محاصره؛ سوم، اقدام نظامی.
هر چیزی که منجر به پایان برنامه هسته‌ای ایران شود، چیزی است که ما می‌خواهیم. این هدف مشترک ماست.
س: وقتی با ترامپ در کاخ سفید ملاقات کردید، آیا تلاش کردید او را متقاعد کنید تا حملات به ایران را از سر بگیرد؟
نتانیاهو: در واقع نه. این یک تصویر کاریکاتوری یا تصویری اغراق‌آمیز است. این درست نیست.
ما در واقع تمام سه احتمال را بررسی کردیم، و من فکر می‌کنم که این کار را به صورت شفاف و در بین دوستان و متحدان انجام دادیم.
و این تصمیم اوست. این تصمیم اوست.
منبع: خبرگزاری ABC News</div>
<div class="tg-footer">👁️ 4.66K · <a href="https://t.me/SBoxxx/19469" target="_blank">📅 10:08 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19468">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">شب گذشته یک منزل مسکونی در قشم مورد اصابت پرتابه آمریکایی ها قرار گرفت  احمد نفیسی معاون استانداری هرمزگان از حمله دشمن به یک منزل مسکونی در محله چاه‌تنگو شهر قشم خبر داد و گفت: تیم‌های امدادی در حال جست‌وجو برای یافتن دو یا سه فرد محبوس‌ در زیر آوار هستند.…</div>
<div class="tg-footer">👁️ 4.64K · <a href="https://t.me/SBoxxx/19468" target="_blank">📅 09:57 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19467">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">فیلم سنتکام از هدف قرار دادن اهداف در حمله بامداد
چند پرتابگر متحرک نیز دیده می شوند</div>
<div class="tg-footer">👁️ 4.73K · <a href="https://t.me/SBoxxx/19467" target="_blank">📅 09:47 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19466">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">حمله موشکی ایران به اردن</div>
<div class="tg-footer">👁️ 4.72K · <a href="https://t.me/SBoxxx/19466" target="_blank">📅 09:24 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19465">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">شب گذشته یک منزل مسکونی در قشم مورد اصابت پرتابه آمریکایی ها قرار گرفت
احمد نفیسی معاون استانداری هرمزگان از حمله دشمن به یک منزل مسکونی در محله چاه‌تنگو شهر قشم خبر داد و گفت: تیم‌های امدادی در حال جست‌وجو برای یافتن دو یا سه فرد محبوس‌ در زیر آوار هستند.
احمد نفیسی خاطرنشان کرد: جزئیات تکمیلی این حادثه و وضعیت افراد گرفتار، پس از پایان عملیات امدادی و ارزیابی‌های میدانی اطلاع‌رسانی خواهد شد./ایرنا</div>
<div class="tg-footer">👁️ 5.08K · <a href="https://t.me/SBoxxx/19465" target="_blank">📅 09:19 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19464">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">شهرهای مورد حمله قرار گرفته از ساعت 3.5 بامداد
🔹
قشم
🔹
اهواز
🔹
بندرعباس
🔹
آبادان
🔹
اروندکنار
🔹
شادگان</div>
<div class="tg-footer">👁️ 5.03K · <a href="https://t.me/SBoxxx/19464" target="_blank">📅 09:18 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19463">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">شهرهای مورد حمله قرار گرفته از ساعت 3.5 بامداد
🔹
قشم
🔹
اهواز
🔹
بندرعباس
🔹
آبادان
🔹
اروندکنار
🔹
شادگان</div>
<div class="tg-footer">👁️ 5.15K · <a href="https://t.me/SBoxxx/19463" target="_blank">📅 09:05 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19462">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">حمله به آبادان</div>
<div class="tg-footer">👁️ 5.35K · <a href="https://t.me/SBoxxx/19462" target="_blank">📅 03:35 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19461">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/d0PCR8onFyoapZxNzsImldkLij9coj1putPIgKtM5EcF107HyBGYuOG0tcTT0kTnblms9-5e-4_rNDuocw10SpSez5zhUbSRMonrB-BvvnGVezBXdGd362w109hhAgfeEF5bfiAdn3kqrNmemErTYW_WpsJIZ_4Zz-kmUFIYSsWTnQpdjnAM71mx8bTS6raqv1_q0xhBvrxrtCrzc4qt-JHiaZyLsEf9PZi32mjm9UPQ1orLceIAYCmMjjxd4PedGPVEGMO6Z3r-tIT5vRy6MnygfXcnJQdvZkvEB-9rLaHGS-BV75h673dJEvWXrFRtzI5iNzZXDUoHl3zf4-zXaQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حملات آمریکا تایید شد</div>
<div class="tg-footer">👁️ 5.42K · <a href="https://t.me/SBoxxx/19461" target="_blank">📅 02:43 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19460">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">چندین انفجار در ریاض، عربستان سعودی، و بسته‌شدن باند فرودگاه پادشاه خالد در ریاض.</div>
<div class="tg-footer">👁️ 5.37K · <a href="https://t.me/SBoxxx/19460" target="_blank">📅 01:30 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19459">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">انفجار در اردبیل و ارومیه (تایید نشده)</div>
<div class="tg-footer">👁️ 5.4K · <a href="https://t.me/SBoxxx/19459" target="_blank">📅 01:28 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19458">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WGAmexAkXnldF4Y8YwP18TjvSTsgX92cbBWhagYo5h5ojGImhUifDpusTwAkK_mGmyp-x1dv7-p7Q417Z4r5hXQc6MQV2haknN9FzHCvDGRpy0P78wBVp5gokoPXv1sESMcnsqwxvlDJ8aSroxovWjg9NfkC7JoUkCLQXewbP8nIz5gBtlqCtOh-lsIqVtREPcaEkwDJbfRUjvpDyldq6HukBsaJrVtuL1PHECFDAEetfKCUP4CZ9_KLtudugO9NSFsNgT3wfmzbhg2Q2G_cD1Z2GQ124u1mEMrrLyE1n90CRs3vgt8rEzNa9d3ULgOjYg0-3QsCm5h1R0HaND-6IQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اسپانیا که اخیراً محبوب حضرات شده بود و چهره یامال را روی موشک ها میزدند، اعدام های اخیر در ایران را محکوم کرده و خواستار تعویق اعدام های برنامه ریزی شده شد.</div>
<div class="tg-footer">👁️ 5.43K · <a href="https://t.me/SBoxxx/19458" target="_blank">📅 00:56 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19457">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OFGaG1GrR9ViEcXcoPK9uyXk_KuCZbM_eberiHQD2XjJJ0IIPYlJGW6AUqfDH18nbkzs0Jq_cJxnPjGLNXq9FxD9ZRFvj1k7ITnZjgbSUOeNCm34lbm3O_3r3VSK9adXUVzhNtKNSB8_AMsQe0TQbQvQk1NxEdA7g7h5wSqYyk-4LvBiILMsPi1K9ywDQPzRFUXWDFzU27dn-McCLRfKMReHXZsFn8yeOLVl24cknUyr5U5J4PoY1hACJYS_vKb3EGTwUEN5UbIrF8Jov4JajsdNE0WZ5sxSc0ELcrLhEnl2gX6SNrEgbvhsdu2RsOQcgmeaPxrYfdfpVj_Dqqq1xg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اسپانیا که اخیراً محبوب حضرات شده بود و چهره یامال را روی موشک ها میزدند، اعدام های اخیر در ایران را محکوم کرده و خواستار تعویق اعدام های برنامه ریزی شده شد.</div>
<div class="tg-footer">👁️ 5.39K · <a href="https://t.me/SBoxxx/19457" target="_blank">📅 00:54 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19456">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/t_P0CTuUkx8PWHCct31-i2zvmKPKTInSUs2NvbnUjLvHvJEYoyQ56IfBsyMk2YSt_7eQk0ixYw_Sar3o6JcOhf-6hkh7Y3MgSk5Sz4sKoarRTWnhhsWheFHZ090sp0kBvWP0BFV9rkXk729L50eK-kyc3JKQLOLWJ6vOOF6jAiFkmTxjt8tgXPMr9ygQ2UxVLrHzPpgez9rTIQdLr5O8f3dXzYYECtxyzwCNKqI8TtvWbrCI6g73S8SFEvZ0Lso9-Z7byrQ4n-7jRXxWS7vIu17i7JVUJd_NMe_UuLK4LYSnSgla7c5W7TZ8KUV1mPahM59n2XqTXIa1LHiB2ldn9w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">امیدوارم آن یک هواپیمایی که نزدیک تهران است جنگنده نیروی هوایی ما باشد.</div>
<div class="tg-footer">👁️ 5.16K · <a href="https://t.me/SBoxxx/19456" target="_blank">📅 00:41 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19455">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">ترور یک مامور فراجا در ایرانشهر
به گزارش مرکز اطلاع‌ر‌سانی پلیس سیستان و بلوچستان، ساعتی قبل افرادی مسلح به سمت مأمور انتظامی در ایرانشهر با سلاح گرم تیراندازی کردند که در پی این اقدام، استوار یکم «مهران سالارزاده» به درجه رفیع شهادت نائل شد.</div>
<div class="tg-footer">👁️ 5.17K · <a href="https://t.me/SBoxxx/19455" target="_blank">📅 00:39 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19454">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IowB6uh4PzleCqPdJfrYqlD9szKIYxVWr_DxyA6kHVVYkkOsWQqaCfaIgVQJbc_65KZh_C5m3J7MKe10uZ5wKHBJlbp1KqzJG4ZfVWlsQg03VhFBzJ2ob6xmjpypoeS8FMzbjWDwH1lFXPGlXaCKqEFJL-tGAEXyIx1U4IOQBhS_ymIXRiXjlK6EfHjMIEEPM0w8lYVDJjiDpZ2gA7ayHFryFsNonBbbCP_6XkmhLqWzehvFryXSm-jOUY-2VshaYFszqF9Wtq_NZYHiAnYaExrmQR2uWHgchdA1RUJ0MmV2WMCmTxgp5ihzWGER9aggFH3z9X_IoLBV_C-otUKohQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#GRI  شاخص ریسک ژئوپولیتیک امروز هم در وضعیت مناسبی قرار دارد و انتظار رشد طلا می رود.  دقت کنید که امشب نشست سرنوشت ساز FOMC را هم داریم که سناریوهای موجود در این یادداشت بررسی شده است.</div>
<div class="tg-footer">👁️ 5.02K · <a href="https://t.me/SBoxxx/19454" target="_blank">📅 00:34 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19453">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3185a6e49f.mp4?token=SJSt5GYum8PJ6ZVbpLZNUvFmarzlOlJCv9QLlfq-WAkIqrUY6Xr28yiQbnNdpofVcQuShMTLx3N0aCvoX79mc8Q4B7joYufNlKZ7u3wHC7W0pNVNBcYd7iqK4FIUpfIPu5rRdOdfjAgayMy8-AFmDCwxd-vs4wX7Hy80WS0qdOwn-L-6C0XTBag2-o4lnWA3QOyoHUoA5UazYqADphJEeF6FECWxS4Cb0h8vznplDDzA594YBrEExOAHMPeobJMirKmELL0uBHKA7Ba_44Y9uYKu0RN8gm9dddbEG7acU0f_hRMCsVA_a0pansj1thwe001P_M2yFjiENn3CHqv6EA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3185a6e49f.mp4?token=SJSt5GYum8PJ6ZVbpLZNUvFmarzlOlJCv9QLlfq-WAkIqrUY6Xr28yiQbnNdpofVcQuShMTLx3N0aCvoX79mc8Q4B7joYufNlKZ7u3wHC7W0pNVNBcYd7iqK4FIUpfIPu5rRdOdfjAgayMy8-AFmDCwxd-vs4wX7Hy80WS0qdOwn-L-6C0XTBag2-o4lnWA3QOyoHUoA5UazYqADphJEeF6FECWxS4Cb0h8vznplDDzA594YBrEExOAHMPeobJMirKmELL0uBHKA7Ba_44Y9uYKu0RN8gm9dddbEG7acU0f_hRMCsVA_a0pansj1thwe001P_M2yFjiENn3CHqv6EA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یک غیرنظامی اردنی به طور تصادفی، فیوز انفجاری یک پهپاد انتحاری ایرانی مدل "شاهد" که سقوط کرده بود را هنگام بررسی آن، منفجر کرد.</div>
<div class="tg-footer">👁️ 5.19K · <a href="https://t.me/SBoxxx/19453" target="_blank">📅 00:28 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19452">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">کانال ۱۲ اسرائیل:
ارتش اسرائیل آماده حمله سراسری و بزرگ به ایران است</div>
<div class="tg-footer">👁️ 5.02K · <a href="https://t.me/SBoxxx/19452" target="_blank">📅 00:22 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19451">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">گزارش‌هایی از پرتاب موشک بالستیک از اطراف یزد در مرکز ایران</div>
<div class="tg-footer">👁️ 5.1K · <a href="https://t.me/SBoxxx/19451" target="_blank">📅 00:21 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19450">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">ترامپ درباره ایران:  آن‌ها می‌دانند که این اتفاق (حمله) در راه است. از ما می‌خواهند که این کار را نکنیم.  دیشب سعی کردند با ۵ موشک به ما شلیک کنند. ما همه آن‌ها را رهگیری کردیم.</div>
<div class="tg-footer">👁️ 5.3K · <a href="https://t.me/SBoxxx/19450" target="_blank">📅 23:09 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19449">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">ترامپ:
آندی برنهام باید به مهاجرت اشاره کند زیرا این موضوع بریتانیا را نابود می‌کند.
آن‌ها از آفریقا، آمریکای جنوبی و بخش‌های مختلف آسیا می‌آیند و در حال حمله به اروپا هستند.
این یک حمله است و بریتانیا مظنون اصلی است.</div>
<div class="tg-footer">👁️ 5.17K · <a href="https://t.me/SBoxxx/19449" target="_blank">📅 23:08 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19448">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WnD1B7fjIS1bq4F_vNMao36lB34hhjw1dgMPW_O2fa5KlnC9LUzXzpf4hmBraRvb2n7p2bTb7_KhrBG98Oi8tDhR410DF9J9ekczZoO0RlBcFuUyj14H9fFRtdXHNBnRaxvrsironsbjskydRt-8dXKJvQV3aW54vArsfh-2i-SU6yaDdOUeIqdvKvrSpx-eLVOfuvIPmoj5yHVAkzP13n0GtHnfYlLkvE2JrIrqlrJHHFXxuGcGOw8Cnd80vjnQF6SmF9LEy2_XJewrrovcThgdnWlNEpW5fiJUk3ouYZvrR3RHVle1cZiVU7yH5PCOBM4cbRABsgs1ZZGlKgsXCg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 5.15K · <a href="https://t.me/SBoxxx/19448" target="_blank">📅 22:58 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19447">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">ترامپ درباره ایران:
آن‌ها می‌دانند که این اتفاق (حمله) در راه است. از ما می‌خواهند که این کار را نکنیم.
دیشب سعی کردند با ۵ موشک به ما شلیک کنند. ما همه آن‌ها را رهگیری کردیم.</div>
<div class="tg-footer">👁️ 5.09K · <a href="https://t.me/SBoxxx/19447" target="_blank">📅 22:58 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19446">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">ترامپ درباره ایران: آن‌ها را به شدت ضربه خواهیم زد، نوبت ماست.</div>
<div class="tg-footer">👁️ 5.06K · <a href="https://t.me/SBoxxx/19446" target="_blank">📅 22:53 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19445">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">علت رشد طلا در چند دقیقه اخیر:
مقامات امنیتی مصر به شبکه خبری "الحدث" اعلام کردند که هیچگونه حمله‌ای در بندر دمیاط رخ نداده است. آن‌ها مدعی هستند که این حادثه یک آتش‌سوزی بوده که در بخش موتور یک کشتی از رده خارج شده رخ داده است. - خبرگزاری "کان" اسرائیل.</div>
<div class="tg-footer">👁️ 5.19K · <a href="https://t.me/SBoxxx/19445" target="_blank">📅 20:40 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19444">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">یک مقام ارشد از یکی از کشورهایی که در این میانجی‌گری نقش دارند: کسی که تصمیم‌گیری‌ها را انجام می‌دهد، فرمانده سپاه پاسداران انقلاب اسلامی است. - خبرگزاری کانال ۱۲ اسرائیل،</div>
<div class="tg-footer">👁️ 5.38K · <a href="https://t.me/SBoxxx/19444" target="_blank">📅 20:39 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19443">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">انفجارات در اردن!</div>
<div class="tg-footer">👁️ 4.99K · <a href="https://t.me/SBoxxx/19443" target="_blank">📅 20:37 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19442">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">رئیس‌جمهور ترکیه، اردوغان:
دولت فعلی اسرائیل که تحت تاثیر جنگ قرار دارد، با تحریکات و اقدامات سازمان‌یافته خود، همچنان منطقه ما را به سمت بی‌ثباتی سوق می‌دهد.
اسرائیل با نادیده گرفتن حقوق اساسی بشر و زیر پا گذاشتن قوانین بین‌المللی، به تدریج و گام به گام، سرزمین‌های فلسطینی را اشغال می‌کند.
اشغالگری اسرائیل، سکونتگاه‌های غیرقانونی آن، و سیاست‌های آوارگی، ارعاب و سرکوب علیه فلسطینیان در کرانه باختری – همانطور که در غزه انجام داده است – منبع اصلی مشکلات در منطقه ما هستند.
هزینه این تجاوز نه تنها توسط برادران و خواهران فلسطینی ما، و نه تنها توسط مردم لبنان، بلکه توسط مردم با ادیان مختلف و کل منطقه پرداخت می‌شود.
به عنوان مثال، به دلیل درگیری‌ها در منطقه ما، عرضه جهانی نفت، یکی از بزرگترین شوک‌های تاریخ را تجربه می‌کند.
متاسفانه، این فقط نفت نیست. قیمت بسیاری از مواد اولیه کلیدی در بازارهای جهانی، از جمله گاز طبیعی، کودها، سوخت دیزل و محصولات پتروشیمی، نیز به سرعت افزایش یافته است.</div>
<div class="tg-footer">👁️ 5.2K · <a href="https://t.me/SBoxxx/19442" target="_blank">📅 20:16 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19441">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">نتانیاهو:  من همین الان یک گفتگوی تلفنی با آقای پیتر هگست، وزیر دفاع، به پایان رساندم.  او نکته جالبی را با من در میان گذاشت. ایشان به من گفتند:   «ما به جهان نگاه می‌کنیم و کشورهایی وجود دارند که اراده مبارزه در کنار ایالات متحده را دارند، اما از توانایی…</div>
<div class="tg-footer">👁️ 4.81K · <a href="https://t.me/SBoxxx/19441" target="_blank">📅 20:03 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19440">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Vvh5pSN0gK87VHzvDtqScW85dXEZyL5rCPgvjwCY8SWcEAUrCMRNi_IT35DdlLuQC2TT8l0zbMCat7UBj72QEnJFkeLQKB4J4KDVPABmxH0XFbeoa6L9tTfg0B8uHoeOfWfDwTeLMqCNzzIoMHql8q6KV67dEdvKK155QMvSqr5CWvh3Wxd3SiMLDWYMJW_AVGmEKR-rWuXyqJFW7e3JCpCpqy0G18SQFzdJxmqBwLG9Oz6awvvFKm5MoqPM8ecyjfRR5fyOR9V5kswPz2vFrYYu12tl8JoVF3mlySOc5V2EIsVkdQLyZDd5A8w7ST7ZXJNv7667sx4hvqf10nmi3g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نتانیاهو:
من همین الان یک گفتگوی تلفنی با آقای پیتر هگست، وزیر دفاع، به پایان رساندم.
او نکته جالبی را با من در میان گذاشت. ایشان به من گفتند:
«ما به جهان نگاه می‌کنیم و کشورهایی وجود دارند که اراده مبارزه در کنار ایالات متحده را دارند، اما از توانایی لازم برخوردار نیستند. و کشورهایی وجود دارند که توانایی لازم را دارند، اما اراده لازم را ندارند اما فقط در اسرائیل است که ما هم اراده و هم توانایی را مشاهده می‌کنیم.»</div>
<div class="tg-footer">👁️ 4.91K · <a href="https://t.me/SBoxxx/19440" target="_blank">📅 20:03 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19439">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">مقامات اسرائیلی می‌گویند نتانیاهو در جلسه روز سه‌شنبه با ترامپ در کاخ سفید، نقشه‌هایی را ارائه کرد که میزان نفوذ اسرائیل و ترکیه را در سوریه مقایسه می‌کرد.
بر اساس اطلاعات ارائه شده، اسرائیل حدود 0.1 درصد از خاک سوریه را تحت کنترل دارد، در حالی که ترکیه حدود 5 درصد را کنترل می‌کند.
نتانیاهو از این تصاویر برای مقابله با فشارهای قبلی آمریکا استفاده کرد، از جمله تماس تلفنی ترامپ در اواسط ماه جولای که از اسرائیل خواست نیروهای خود را از سوریه و لبنان خارج کند.</div>
<div class="tg-footer">👁️ 4.72K · <a href="https://t.me/SBoxxx/19439" target="_blank">📅 19:57 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19438">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">به نظرم یک مقدار لیست اهداف مشروع ما دارد خیلی بزرگ می‌شود که ولی خب</div>
<div class="tg-footer">👁️ 4.69K · <a href="https://t.me/SBoxxx/19438" target="_blank">📅 19:47 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19437">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">یک مجتمع شناور ذخیره‌سازی گاز طبیعی مایع (LNG) متعلق به یک شرکت آمریکایی و دارای پرچم جزایر مارشال، در شهر دمیاط، مصر، مورد حمله حداقل یک پهپاد قرار گرفت.</div>
<div class="tg-footer">👁️ 4.67K · <a href="https://t.me/SBoxxx/19437" target="_blank">📅 19:26 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19436">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">یک مجتمع شناور ذخیره‌سازی گاز طبیعی مایع (LNG) متعلق به یک شرکت آمریکایی و دارای پرچم جزایر مارشال، در شهر دمیاط، مصر، مورد حمله حداقل یک پهپاد قرار گرفت.</div>
<div class="tg-footer">👁️ 4.92K · <a href="https://t.me/SBoxxx/19436" target="_blank">📅 19:26 · 07 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>

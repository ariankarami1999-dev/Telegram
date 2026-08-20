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
<img src="https://cdn4.telesco.pe/file/WvqYIORYUc3F48XubWuj8iP9BJ8YLp9R97bkqqkU2F8pdt_NFsgq2tOn-1WAFuJ9l4zk3t37mg5yleto-K1kPO7pXMNJk7TyzImwEVVM0N2yIfxcAJTEu9Rky6ZIrfQ7LWIghxg97SRa8Mp9UuRWlpcr5UjHVWwvyl3MmSG1afkn954eP7sj6RQ_foXMXNpJFvsWcI_IbTsZZt4VnPv1_TQBp8wz9lnxUJiZLX_CzJ2w2kSj7ko3iQcE98CwKfcqda0SDO673u4WKmSjis3Lu6GOCHlXTSpnhx8X79a-iI89wrpyw7qBwUBZ-0YdLJVC3RuXX5BfJkhNyvo78ubIJw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Secret Box</h1>
<p>@SBoxxx • 👥 10.6K عضو</p>
<a href="https://t.me/SBoxxx" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ■  تاریخ | ژئوپلتیک | بازارهای مالی ■https://secretboxxx.com/</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-30 00:49:05</div>
<hr>

<div class="tg-post" id="msg-20071">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">اظهارات معاون رئیس‌جمهور، جِی. دی. ونس، درباره ایران:
ما اکنون در یک مرحله جدید قرار داریم که موثرترین ابزاری که در اختیار داریم، فشار اقتصادی است که می‌توانیم بر آنها وارد کنیم.
این یک تعادل ظریف است، زیرا ما فشار اقتصادی بر آنها وارد می‌کنیم. آنها نیز تلاش خواهند کرد که فشار اقتصادی بر ما وارد کنند.
اما آنچه در چند هفته گذشته صادق بوده این است که آنها احساس فشار بسیار بیشتری نسبت به آنچه ما تجربه کرده‌ایم، داشته‌اند.
ما این روند را ادامه خواهیم داد، زیرا معتقدیم که این بهترین راه برای دستیابی نهایی به هدف مورد نظر است.</div>
<div class="tg-footer">👁️ 1.33K · <a href="https://t.me/SBoxxx/20071" target="_blank">📅 00:01 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20070">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">اسکات بسنت وزیر خزانه داری آمریکا درباره ایران: «ما این رژیم را سرنگون خواهیم کرد»</div>
<div class="tg-footer">👁️ 1.62K · <a href="https://t.me/SBoxxx/20070" target="_blank">📅 23:49 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20069">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gi05Tgi_p1bG6iAkVVXYZPj0D0tFqEDASoHDSXs83CTJLqAYCOblWlCyQXIDqtes51DLYlQ2pFhTwx2Xk0EvnE4eYosP2P8ERnNn7lPz5NyimMYrqXHnxtRKc9TP-8TfDt-fCaV_5fYXky1eV2ffWmdzpBdcOrTVWh6LsWhtoM14VMUFx61EqHWzSXCUJD-RKkiMLbIRln-M05rWI01_SkXQXxQ2iQWL_PfoJWIQWwzcPibBCRIVbTyU8HT60DOxasjL7tGPCJzGf2psyDHXyrcEPXtuH2C6zkM6PCe1C0NEd_Cb2KheUC0E_rJiQTxoyufERhoT9MZXSWjQI47ytw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رئیس مجلس عراق در واکنش به این عکس قالیباف، از خود عکسی منتشر کرد که در پشت سر او، بجای خلیج فارس، نام نجس خلیج عربی نوشته شده!</div>
<div class="tg-footer">👁️ 3.14K · <a href="https://t.me/SBoxxx/20069" target="_blank">📅 21:26 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20068">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">ایالات متحده آمریکا تحریم‌های جدیدی علیه حزب‌الله اعمال کرد و آن را مجدداً تحت یک قانون مربوط به تروریسم طبقه‌بندی کرد تا بر پیوندهای آن با نیروی قدس سپاه پاسداران انقلاب اسلامی ایران تأکید کند.
واشنگتن همچنین ۱۰ نفری را که متهم به قاچاق پول نقد برای حزب‌الله هستند، تحریم کرد.</div>
<div class="tg-footer">👁️ 3.04K · <a href="https://t.me/SBoxxx/20068" target="_blank">📅 21:24 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20067">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">چین می‌گوید تهدید رئیس‌جمهور ترامپ برای آغاز «جنگ اقتصادی» علیه ایران و شرکای تجاری آن کارساز نخواهد بود.</div>
<div class="tg-footer">👁️ 3.05K · <a href="https://t.me/SBoxxx/20067" target="_blank">📅 21:10 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20066">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">اسکات بسنت وزیر خزانه داری آمریکا درباره ایران: «ما این رژیم را سرنگون خواهیم کرد»</div>
<div class="tg-footer">👁️ 3.39K · <a href="https://t.me/SBoxxx/20066" target="_blank">📅 20:28 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20065">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">ضرغامی:   از اول انقلاب تحریم بودیم ولی کشور رشد کرده، پیرزن رو از تاکسی خالی نترسونین!</div>
<div class="tg-footer">👁️ 3.48K · <a href="https://t.me/SBoxxx/20065" target="_blank">📅 19:53 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20063">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">ضرغامی:
از اول انقلاب تحریم بودیم ولی کشور رشد کرده، پیرزن رو از تاکسی خالی نترسونین!</div>
<div class="tg-footer">👁️ 3.49K · <a href="https://t.me/SBoxxx/20063" target="_blank">📅 19:51 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20062">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">اسکات بسنت وزیر خزانه داری آمریکا درباره ایران: «ما این رژیم را سرنگون خواهیم کرد»</div>
<div class="tg-footer">👁️ 3.96K · <a href="https://t.me/SBoxxx/20062" target="_blank">📅 18:43 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20061">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">حوثی‌های یمن اعلام کردند که دو حمله پهپادی را علیه فرودگاه ابها و تأسیسات آرامکو در عربستان سعودی انجام داده‌اند.</div>
<div class="tg-footer">👁️ 3.84K · <a href="https://t.me/SBoxxx/20061" target="_blank">📅 17:48 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20060">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">— مرکز فرماندهی مرکزی آمریکا (CENTCOM) اعلام کرد که گروه ضربتی ناو هواپیمابر یواس‌اس جورج واشینگتن به خاورمیانه رسیده و اکنون در منطقه مسئولیت خود عملیات می‌کند.</div>
<div class="tg-footer">👁️ 3.86K · <a href="https://t.me/SBoxxx/20060" target="_blank">📅 17:05 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20059">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">رئیس مجلس عراق در واکنش به این عکس قالیباف، از خود عکسی منتشر کرد که در پشت سر او، بجای خلیج فارس، نام نجس خلیج عربی نوشته شده!</div>
<div class="tg-footer">👁️ 3.96K · <a href="https://t.me/SBoxxx/20059" target="_blank">📅 16:42 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20058">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/etjDV4LccZBgMdQgpafMKiio95HMQOQUUvlflgnfbfTx37sBqcDaHm7QUxPg4GbPwEahuSo3EkSssewTkfY8gwqFJ2uH7AhEtoEkjFlbAd8yIbZ3gs7yaVWrAeHMaBnMwEX5oa2Bmj7Uyh8XZ1r7GqQJuP0Ij9Z3RKIq3oLUd1SsOwKHX4L4Pg17piGiUMhSTuguo8l3NAErIoJzrgLG5lqwonfxneA1IOUFDI0r5aF2etzFCmq9bjAuKxYaBW8BKnBxmgnb3OtICerdr7EI1w_RgSew7d0l4J9ItO8Sk4EDBfspif4HedcwKpNdqdAsnSic7ydL5ls0jY66E85exA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سبحان الله این چه فیگوری است دیگر!  انسان گمان می کند که نعوذبالله دارند با کله نورانی شان روده بزرگ کشورمان را کلنوسکوپی می کنند!</div>
<div class="tg-footer">👁️ 4.09K · <a href="https://t.me/SBoxxx/20058" target="_blank">📅 16:39 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20057">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">اردوغان: «ترکیه در دامی که نتانیاهو برای سوریه چیده است، نمی‌افتد»</div>
<div class="tg-footer">👁️ 3.88K · <a href="https://t.me/SBoxxx/20057" target="_blank">📅 15:56 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20056">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">اردوغان:  «توافق مکه» علیه هیچ کشوری نیست و تمام دولت‌ها می‌توانند به آن بپیوندند  نباید این توافق را به بعد نظامی محدود کرد، زیرا هدف اصلی آن تقویت بعد بازدارندگی و امنیتی است</div>
<div class="tg-footer">👁️ 3.93K · <a href="https://t.me/SBoxxx/20056" target="_blank">📅 15:55 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20055">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">#GRI  شاخص ریسک ژئوپولیتیک برای امروز در بالاترین سطح خود قرار دارد و تقریباً در چنین شرایطی محال است که امروز شاهد سقف جدیدی در طلا باشیم.  انتظار افت دستکم 400 پیپی دیگر در طلا دارم.</div>
<div class="tg-footer">👁️ 3.97K · <a href="https://t.me/SBoxxx/20055" target="_blank">📅 15:40 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20054">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BtsNny39UwQCxTCNPggGM9tnMaRYIBnd4aSwqPSw2OgSHVZDlNNbsAMBteT3oL6GuCtF1og3Ld6I7uJRzcp2q26ZXCzFHOzGBE1EmIIi0P7ZRLZHKwFHT-HvY0FnB-YaNDijZwI6d8pMkTA7jxxtoaTWyLKodtBZGbhklLBbPCYVwN6xgVIPYz4hCzlEb2dgIdJpoGv-TmrmYmzoZ02fL95EQ1JDZBjkfueSEnI4bvyVmMprpY_k9zz2BPeWgLWlWFAqf2F7w2jLkelNzyL7W8vgBHlH_QFIeP_wFwwVKqc_ogxNddsio_5TW1nznuxHZmVocFhYZD_G6B_FrK-CsA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سبحان الله این چه فیگوری است دیگر!
انسان گمان می کند که نعوذبالله دارند با کله نورانی شان روده بزرگ کشورمان را کلنوسکوپی می کنند!</div>
<div class="tg-footer">👁️ 4.08K · <a href="https://t.me/SBoxxx/20054" target="_blank">📅 15:25 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20053">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">بفرمایید:  ‏ فواد ایزدی: اگر ۲۰درصد نفت دنیا را حذف کنیم؛ اقتصاد آمریکا فرومی‌پاشد!  با این کار نفت ۲۰۰ دلار خواهد شد؛ باید تصمیم بگیریم که تاسیسات نفتی منطقه را طوری موشک باران کنیم که دو سه سال برای بازسازی زمان بگیرد. ‎</div>
<div class="tg-footer">👁️ 4.18K · <a href="https://t.me/SBoxxx/20053" target="_blank">📅 14:15 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20052">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">نه دارو داریم نه بنزین نه برق نه نت نه گاز با تورم 300 درصد و رشد اقتصادی منفی و ریاست جمهوری دکتر پزشکیان و 2 جنگ بزرگ در 1 سال اخیر با گرمای 50 درجه تابستان و سرمای 20 درجه زیر صفر زمستان اما دغدغه جوان ما این است که رامین رضاییان به آن دختره چی دایرکت داده!…</div>
<div class="tg-footer">👁️ 4.01K · <a href="https://t.me/SBoxxx/20052" target="_blank">📅 14:10 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20051">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">نفت را دریابید پیش از آنکه نفت شما را دریابد!</div>
<div class="tg-footer">👁️ 3.99K · <a href="https://t.me/SBoxxx/20051" target="_blank">📅 14:04 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20050">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">به نظر من جمهوری اسلامی بزودی گزینه آخرالزمانی حمله به چاههای نفت و تاسیسات انرژی منطقه را فعال خواهدکرد که در پی آن نفت به بالای ۱۳۰ دلار و طلا به زیر ۴۰۰۰ دلار خواهندرفت.</div>
<div class="tg-footer">👁️ 4.2K · <a href="https://t.me/SBoxxx/20050" target="_blank">📅 14:04 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20049">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DchRplaD-wwIKUI2VEnDJTo-B9SFZv48AsR1lmwYzMCDrQu0LUMf2uvdU0X0VDIMks3mcAtgIJnzDJLwvCP0ZqJrspAoWIcSBx5jLaiIv5tfHxxt9Hp0chMpbAdu0sjOpz3fATXjh0gAuFS2sboskOKBtHLWOfxYjCscLEEdYH9gPwdVFNT97bKCJii-wCHZ5mWvzwNxa5HyKCVbV-QRbYX6WY_bzJ1zNggW7kkvpGwarknLixFx8JF-NSPKRPshmoi0s5hWZG26eiq4ra902wijVQf5YeBB0XkKBSas8YpbbeGqf1YBlYAi0qutPVBgF_FF4-lbAmrK3KTlIfcLLg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حادثه برای یک نفت کش در خلیج عدن!
به نظر می رسد حوثی ها تصمیم دارند کشتی را بدزدند.</div>
<div class="tg-footer">👁️ 4K · <a href="https://t.me/SBoxxx/20049" target="_blank">📅 13:22 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20048">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">اگر آلمانی ها به جای ما در این میهن اهورایی می زیستند تا الان نسلشان افتاده بود.</div>
<div class="tg-footer">👁️ 4.05K · <a href="https://t.me/SBoxxx/20048" target="_blank">📅 13:10 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20047">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">طبق داده‌های دولتی، آلمان در این تابستان ۱۴۰۰۰ مورد مرگ ناشی از گرما را ثبت کرده است</div>
<div class="tg-footer">👁️ 3.93K · <a href="https://t.me/SBoxxx/20047" target="_blank">📅 13:08 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20046">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">📌
وخیم تر شدن وضعیت صنعت آلمان در اثر جنگ خاورمیانه  صنعت آلمان که پیش‌تر هم تحت فشار بود، با آغاز جنگ خاورمیانه، افت تولید صنعتی، کاهش رشد صادرات و افت محسوس مازاد تجاری در مارس، وارد وضعیت ضعیف‌تری شده و احتمال بازبینی نزولی رشد اقتصادی سه‌ماهه اول را بالا…</div>
<div class="tg-footer">👁️ 4K · <a href="https://t.me/SBoxxx/20046" target="_blank">📅 13:07 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20045">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">— نتانیاهو، نخست وزیر اسرائیل:  «ما حضور نیروهای نظامی ترکیه در سوریه را که اسرائیل را تهدید می‌کنند، تحمل نخواهیم کرد.  ما به روشنی گفته‌ایم که حضور نظامی ترکیه در سوریه را تحمل نخواهیم کرد و به نظر می‌رسد که آنها حرف ما را خوب نشنیده‌اند. بنابراین، ما اقداماتی…</div>
<div class="tg-footer">👁️ 4.01K · <a href="https://t.me/SBoxxx/20045" target="_blank">📅 12:48 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20044">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">نماینده مجلس ایران، ابراهیم رضایی:
بهترین پاسخ به تشدید جنگ اقتصادی توسط ترامپ، خروج از پیمان منع گسترش سلاح‌های هسته‌ای (NPT) است.</div>
<div class="tg-footer">👁️ 4.07K · <a href="https://t.me/SBoxxx/20044" target="_blank">📅 11:37 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20043">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">سخنگوی سپاه پاسداران انقلاب اسلامی:
قدرت تخریبی سر جنگی موشکهای مورد استفاده در موشک‌های جدید سپاه، بسیار بیشتر از سر جنگی هایی است که در جنگ‌های قبلی استفاده می‌شد.
اگر جنگی آغاز شود، سلاح‌های ما در تمام جنبه‌ها کاملاً با گذشته متفاوت خواهند بود.</div>
<div class="tg-footer">👁️ 4.16K · <a href="https://t.me/SBoxxx/20043" target="_blank">📅 11:35 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20042">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FJgFShL-I1JVH5tjUhGuS-FrM7oD6pRS2Ay9bCBTGgZx8X_t8GKi8ighxNuXisvvyBEfc3O7L_bUpW4h6-uB15aELB_hBYg0-8uNeB2NmullRAON5ed9BWRfNwU20wH9FK0qw19wygGJNHSXp1bL_Jr8uidPA3s4_iKpec15iHrHF5Giha-GSMvRz3gcn04NQ8y8zJmVk90BTdpdVu8xEvv9_MO39Y8S2iBgWI9r-K8wX0RsG1wQE2jqiXAaYis7nGo1fUONI7S8aLy_X2BZq2IwKiSW8raL1Bu4M71Q_8ldfCEyJ5wETPMvtqTT57i72GfGo-wlbuu2JroTLEA3cQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#GRI
شاخص ریسک ژئوپولیتیک برای امروز در بالاترین سطح خود قرار دارد و تقریباً در چنین شرایطی محال است که امروز شاهد سقف جدیدی در طلا باشیم.
انتظار افت دستکم 400 پیپی دیگر در طلا دارم.</div>
<div class="tg-footer">👁️ 4.33K · <a href="https://t.me/SBoxxx/20042" target="_blank">📅 11:27 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20041">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">به نظر من جمهوری اسلامی بزودی گزینه آخرالزمانی حمله به چاههای نفت و تاسیسات انرژی منطقه را فعال خواهدکرد که در پی آن نفت به بالای ۱۳۰ دلار و طلا به زیر ۴۰۰۰ دلار خواهندرفت.</div>
<div class="tg-footer">👁️ 4.64K · <a href="https://t.me/SBoxxx/20041" target="_blank">📅 02:50 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20040">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">به نظر من جمهوری اسلامی بزودی گزینه آخرالزمانی حمله به چاههای نفت و تاسیسات انرژی منطقه را فعال خواهدکرد که در پی آن نفت به بالای ۱۳۰ دلار و طلا به زیر ۴۰۰۰ دلار خواهندرفت.</div>
<div class="tg-footer">👁️ 4.76K · <a href="https://t.me/SBoxxx/20040" target="_blank">📅 02:42 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20039">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">ترامپ:  هیچ‌کس به جمهوری اسلامی ایران فرصت بهتری برای توافق نداده است، به اندازه من. و متأسفانه، آنها نتوانستند از آن استفاده کنند.   بنابراین، امروز من جامع‌ترین تحریم‌هایی را که تاکنون علیه هر کشوری اعمال شده است، اعلام می‌کنم. این یک جنگ اقتصادی و انزوا…</div>
<div class="tg-footer">👁️ 4.58K · <a href="https://t.me/SBoxxx/20039" target="_blank">📅 02:40 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20038">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">ترامپ:  هیچ‌کس به جمهوری اسلامی ایران فرصت بهتری برای توافق نداده است، به اندازه من. و متأسفانه، آنها نتوانستند از آن استفاده کنند.   بنابراین، امروز من جامع‌ترین تحریم‌هایی را که تاکنون علیه هر کشوری اعمال شده است، اعلام می‌کنم. این یک جنگ اقتصادی و انزوا…</div>
<div class="tg-footer">👁️ 4.53K · <a href="https://t.me/SBoxxx/20038" target="_blank">📅 02:35 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20037">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">ترامپ:
هیچ‌کس به جمهوری اسلامی ایران فرصت بهتری برای توافق نداده است، به اندازه من. و متأسفانه، آنها نتوانستند از آن استفاده کنند.
بنابراین، امروز من جامع‌ترین تحریم‌هایی را که تاکنون علیه هر کشوری اعمال شده است، اعلام می‌کنم. این یک جنگ اقتصادی و انزوا در مقیاسی بی‌سابقه خواهد بود.
نیروی دریایی آنها نابود شده، نیروی هوایی آنها نابود شده، کارخانه‌های نظامی آنها ویران شده، پول آنها بی‌ارزش شده و کشورشان در آستانه فروپاشی است.
علاوه بر این، من امروز اعلام می‌کنم هر کشوری که به مؤسسات مالی، شرکت‌ها، فرودگاه‌ها یا نهادهای دولتی خود اجازه دهد هر نوع حمایتی از ایران ارائه دهند، با عواقب شدید اقتصادی روبرو خواهد شد.
قاچاق نفت، خطوط مبادله، انتقال پول نقد، صرافی‌ها، ثبت کشتی‌ها و شرکت‌های پوششی - همه اینها باید اکنون متوقف شوند. خودتان می‌دانید. این یک روز اقتصادی محوری خواهد بود و ما به همه متحدان خود نیاز داریم تا در کنار ایالات متحده بایستند تا تهدید ایران را منزوی و شکست دهند.
این دیوانه‌ها در آستانه فروپاشی هستند و این اقدامات تاریخی آنها را فلج می‌کند و توانایی آنها را برای گسترش ترور در سراسر جهان از بین می‌برد. ایران هرگز سلاح هسته‌ای نخواهد داشت.
از توجه شما به این موضوع متشکرم.</div>
<div class="tg-footer">👁️ 4.79K · <a href="https://t.me/SBoxxx/20037" target="_blank">📅 02:34 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20036">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">ترامپ: من خردکننده‌ترین عملیات اقتصادی علیه ایران را اعلام می‌کنم</div>
<div class="tg-footer">👁️ 4.23K · <a href="https://t.me/SBoxxx/20036" target="_blank">📅 02:30 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20034">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromExciton Computer Missile Program</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/da68894d0f.mp4?token=G5upduf3i34zNQGkeJp4rLm28y7ptvlsqPthB8qKHsEho41DQnUomRRaneAHF21uxnld5iyGofo04QaUy86iO3KcJjngnBVuWdzrmmAen_UJcqfuH_gaI-zW8o2gNUAmMk5pk7Y2AV0wqqhVhmzDAFxrpw1KI5ffXwxU8qd9us12WnOi98KYSn1u5T2d4IltnyxlfHXAadVdO4gy3OOWxWt5770x78ourxtlSBeebS2zRkT2_smsbW-7pCWxCI6rbLgMgO_wDTgu0UOUwsh83kgte4xrafLyEE7ub9AVRPbile6YFd8IPw4dFAhrVMPe3YMXDLgSYukmD3HBQgLtBg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/da68894d0f.mp4?token=G5upduf3i34zNQGkeJp4rLm28y7ptvlsqPthB8qKHsEho41DQnUomRRaneAHF21uxnld5iyGofo04QaUy86iO3KcJjngnBVuWdzrmmAen_UJcqfuH_gaI-zW8o2gNUAmMk5pk7Y2AV0wqqhVhmzDAFxrpw1KI5ffXwxU8qd9us12WnOi98KYSn1u5T2d4IltnyxlfHXAadVdO4gy3OOWxWt5770x78ourxtlSBeebS2zRkT2_smsbW-7pCWxCI6rbLgMgO_wDTgu0UOUwsh83kgte4xrafLyEE7ub9AVRPbile6YFd8IPw4dFAhrVMPe3YMXDLgSYukmD3HBQgLtBg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">در حمله امشب به کیف این احتمالا موشک اسکندر نیست. این احتمالا موشک بالستیک سری KN کره شمالی است که با سرعت بیشتری روی هدف فرود می آید. مانور pull-up شاید کمتر باشد. اما باز هم زاویه نزدیک به عمودی و تیز را مشاهده میکنیم. سرجنگی هم مشخصا بسی سنگین است.
@Exciton_missile_program
🚀</div>
<div class="tg-footer">👁️ 4.06K · <a href="https://t.me/SBoxxx/20034" target="_blank">📅 01:52 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20033">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">نیروهای ایالات متحده به‌صورت پنهانی یک کریدور حمل‌ونقلی محافظت‌شده از طریق بخش جنوبی تنگه هرمز را گشوده‌اند که به ۱۵ تا ۲۰ کشتی تانکر اجازه می‌دهد هر شب از آن عبور کنند.  مسئولان می‌گویند این عملیات اکنون تقریباً ۱۰ میلیون بشکه نفت در روز را جابه‌جا می‌کند—که…</div>
<div class="tg-footer">👁️ 4.27K · <a href="https://t.me/SBoxxx/20033" target="_blank">📅 00:57 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20032">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">ترامپ:  ما کنترل کامل و بی‌چون و چرا را بر تنگه هرمز در اختیار داریم.</div>
<div class="tg-footer">👁️ 4.83K · <a href="https://t.me/SBoxxx/20032" target="_blank">📅 00:56 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20031">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">— نتانیاهو، نخست وزیر اسرائیل:
«ما حضور نیروهای نظامی ترکیه در سوریه را که اسرائیل را تهدید می‌کنند، تحمل نخواهیم کرد.
ما به روشنی گفته‌ایم که حضور نظامی ترکیه در سوریه را تحمل نخواهیم کرد و به نظر می‌رسد که آنها حرف ما را خوب نشنیده‌اند. بنابراین، ما اقداماتی انجام داده‌ایم تا مطمئن شویم که آنها این موضوع را بهتر درک می‌کنند.»</div>
<div class="tg-footer">👁️ 4.41K · <a href="https://t.me/SBoxxx/20031" target="_blank">📅 22:43 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20030">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">نافتالی بنِت، نخست‌وزیر سابق اسرائیل:  ما ایالات متحده را از دست داده‌ایم. ما دنیا را از دست داده‌ایم.  ما در پایین‌ترین سطح ممکن از اعتبار بین‌المللی اسرائیل، از زمان تأسیس این کشور، قرار داریم.  باید روی این موضوع کار کنیم.</div>
<div class="tg-footer">👁️ 4.47K · <a href="https://t.me/SBoxxx/20030" target="_blank">📅 22:22 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20029">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">محمد رضا نقدی، فرمانده بسیج:
ما باید به بازدارندگی دست پیدا کنیم. برای ما خوب نیست که کسی بتواند تصمیم بگیرد به ایران حمله کند، و سپس، در صورت شکست، عقب‌نشینی کند، خود را سازماندهی کند و شش ماه بعد دوباره بازگردد.
ما باید امنیت خود را حفظ کنیم. چه این امنیت از طریق دیپلماسی و چه از طریق جنگ به دست آید، ما باید آن را به دست آوریم. این نکته اساسی است.
نه دیپلماسی و نه جنگ، به خودی خود ارزشی ذاتی ندارند؛ هر دو ابزار و روش هستند. ما باید بازدارندگی خود را بازیابی کنیم.
چگونه بازدارندگی ما بازیابی می‌شود؟ با این کار که مشخص کنیم حمله به ایران هزینه‌ای دارد.
اگر آمریکا این هزینه را از طریق دیپلماسی بپردازد – اگر بیاید و به این درخواست‌هایی که سردار رضایی به تازگی به آنها اشاره کرد، عمل کند، از طریق دیپلماسی عمل کند، غرامت پرداخت کند و بپذیرد که در هر صورت، باید هزینه‌ای را بپردازد – آنگاه به سادگی باز نخواهد گشت و دوباره تلاش نخواهد کرد. این می‌تواند بازدارندگی ما را بازیابی کند.</div>
<div class="tg-footer">👁️ 4.59K · <a href="https://t.me/SBoxxx/20029" target="_blank">📅 20:19 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20028">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">ایران در حال بررسی حملات به  خارج از خاورمیانه  است   اهداف بالقوه شامل پایگاه‌های نظامی در بلغارستان و قبرس، به‌علاوه کابل‌های زیردریایی در تنگه هرمز است.  مسئولان ایرانی به‌طور فزاینده‌ای تعارض مجدد را اجتناب‌ناپذیر می‌دانند و هشدار می‌دهند که حملات به زیرساخت‌های…</div>
<div class="tg-footer">👁️ 4.44K · <a href="https://t.me/SBoxxx/20028" target="_blank">📅 19:57 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20027">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">ترامپ:  ما کنترل کامل و بی‌چون و چرا را بر تنگه هرمز در اختیار داریم.</div>
<div class="tg-footer">👁️ 4.59K · <a href="https://t.me/SBoxxx/20027" target="_blank">📅 19:10 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20026">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">اظهارات ترامپ درباره ایران:  ایران نباید سلاح هسته‌ای داشته باشد. شما می‌دانید چرا؟ چون آن‌ها از آن استفاده خواهند کرد.  ما اجازه نخواهیم داد که آن‌ها از آن استفاده کنند.</div>
<div class="tg-footer">👁️ 4.5K · <a href="https://t.me/SBoxxx/20026" target="_blank">📅 19:08 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20025">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">گزارشگر: آیا قصد دارید مذاکرات را با ایران از سر بگیرید؟  ترامپ: شاید در یک مقطعی، اما در حال حاضر نه، فعلا اوضاع بسیار خوب است. اما شاید در یک مقطع زمانی دیگر.</div>
<div class="tg-footer">👁️ 4.48K · <a href="https://t.me/SBoxxx/20025" target="_blank">📅 19:06 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20024">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">گزارشگر: آیا قصد دارید مذاکرات را با ایران از سر بگیرید؟
ترامپ: شاید در یک مقطعی، اما در حال حاضر نه، فعلا اوضاع بسیار خوب است. اما شاید در یک مقطع زمانی دیگر.</div>
<div class="tg-footer">👁️ 4.49K · <a href="https://t.me/SBoxxx/20024" target="_blank">📅 19:06 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20023">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jvw4ggWy7AuCeepefhXBHyqKVy7KXKGbu28ElZ6liiHfDr0iCpfYb1QBhaQEGg-IIBTHZYf_z5kbghjDDvTrkcPjgxNcHfTplr338LD0ApntN-2urXSaickdxFjGXMjfcQkpDRRvxEYqHjyBrQWMSRZvT-zL9Bgd0179zfImtFdieObhoM45PjBic5PgvXlka1NcEqRoB3stvOl8jAA-JKDHJOo0SAKni7oUc9L4Uhbq_izZqoAJMuSBuguZAuWgUM9AISKZb6oY3LlKerpklaZjMuCh1NQrA5ednu8mc0qdU1lP7MIFsqSChn1fNrdzVoqozMYF-4_SX1FKrnsg4Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">درین بازار اگر سودیست با درویش خرسند است</div>
<div class="tg-footer">👁️ 4.52K · <a href="https://t.me/SBoxxx/20023" target="_blank">📅 18:35 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20022">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">#GRI  شاخص ریسک ژئوپولیتیک برای امروز در سطح میانه پایینی است و برای طلا این موضوع به صورت نسبی مثبت است.</div>
<div class="tg-footer">👁️ 4.47K · <a href="https://t.me/SBoxxx/20022" target="_blank">📅 16:27 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20021">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">ارتش اسرائیل در جنگ شدیدی با حزب الله برای تسلط بر تپه های علی الطاهر است که به شهر راهبردی نبطیه اشراف کامل دارند.</div>
<div class="tg-footer">👁️ 4.57K · <a href="https://t.me/SBoxxx/20021" target="_blank">📅 15:47 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20020">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">اظهارات نفتالی بنِت، نخست‌وزیر سابق اسرائیل، درباره ایران:  ما باید اطمینان حاصل کنیم که رژیم ایران قبل از دستیابی به سلاح‌های هسته‌ای، سقوط خواهد کرد.  بنابراین، از یک طرف، ما مانع از دستیابی ایران به سلاح هسته‌ای خواهیم شد.  و از طرف دیگر، ما برای تسریع…</div>
<div class="tg-footer">👁️ 4.64K · <a href="https://t.me/SBoxxx/20020" target="_blank">📅 15:37 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20019">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">اظهارات نفتالی بنِت، نخست‌وزیر سابق اسرائیل، درباره ایران:  ما باید اطمینان حاصل کنیم که رژیم ایران قبل از دستیابی به سلاح‌های هسته‌ای، سقوط خواهد کرد.  بنابراین، از یک طرف، ما مانع از دستیابی ایران به سلاح هسته‌ای خواهیم شد.  و از طرف دیگر، ما برای تسریع…</div>
<div class="tg-footer">👁️ 4.43K · <a href="https://t.me/SBoxxx/20019" target="_blank">📅 15:34 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20018">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">اظهارات نفتالی بنِت، نخست‌وزیر سابق اسرائیل، درباره ایران:  اگر حزب‌الله به ما آسیب برساند، ما به ایران آسیب خواهیم رساند—به روش‌های مختلف.  هرگونه حمله از سوی بازوهای "اختاپوس" ایران در داخل مرزهای اسرائیل، منجر به مجازات‌هایی خواهد شد که در داخل ایران اعمال…</div>
<div class="tg-footer">👁️ 4.47K · <a href="https://t.me/SBoxxx/20018" target="_blank">📅 15:33 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20017">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">یک جوری میگویند خویشتن داری کند انگار می‌تواند خویشتن نداری هم بکند  چیزی نمانده برای این وامانده های غارنشین حرامزاده تروریست</div>
<div class="tg-footer">👁️ 4.35K · <a href="https://t.me/SBoxxx/20017" target="_blank">📅 15:28 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20016">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">اظهارات نفتالی بنِت، نخست‌وزیر سابق اسرائیل، درباره ایران:
اگر حزب‌الله به ما آسیب برساند، ما به ایران آسیب خواهیم رساند—به روش‌های مختلف.
هرگونه حمله از سوی بازوهای "اختاپوس" ایران در داخل مرزهای اسرائیل، منجر به مجازات‌هایی خواهد شد که در داخل ایران اعمال خواهند شد.
در دولت بعدی، ما این سیاست "مجازات" را به طور کامل اجرا خواهیم کرد.</div>
<div class="tg-footer">👁️ 4.42K · <a href="https://t.me/SBoxxx/20016" target="_blank">📅 15:22 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20015">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">وقتی برخی سرمایه گذاران به امانتداری بانک انگلستان با ۴۰۰ سال سابقه برای طلایشان شک می‌کنند؛ در عجبم از ملتی که در پلتفرم های آنلاین ایرانی طلا میخرند!  راستی میدانستید آلمان چند سال است از آمریکا درخواست انتقال طلاهایش از فدرال رزرو به انبار بوندس بانک در…</div>
<div class="tg-footer">👁️ 5.47K · <a href="https://t.me/SBoxxx/20015" target="_blank">📅 14:04 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20014">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oON_gdcrjwHgb3bQBNpZ8e6u7HrK1xjlwux5tB-sSs0vkK_LkRIY3AT3Wor_QwHsy4bUTP8arzkrBQxaankNfoE0eNwy72Y48QNCGTPiKAhuA384YwFfZCu_0LabmP7LFPr-zHYDrFjt1wkOkmozNYLSUXTBhhUI0lGXkuD0No2wZPwTCKdvC2meh1UbPCsAEMH-ZoEC49aIH4cPlpBafFyNu7stZcdEsP_4ZxjBx-ggQGFYTmwG3Mh6p20Vz_6dmisOMXjzUYYBu_Xo6nuRWqpO6oAJal1h_DHNcDBjnzFJSEUvdRe0cghw_PexAnHq720FOLqYwUKokXTZltoiyg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#GRI
شاخص ریسک ژئوپولیتیک برای امروز در سطح میانه پایینی است و برای طلا این موضوع به صورت نسبی مثبت است.</div>
<div class="tg-footer">👁️ 4.65K · <a href="https://t.me/SBoxxx/20014" target="_blank">📅 13:06 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20013">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gF7jzc_9teGPnnkGU0f0CqAEkGFSatlZURBdBa06GSwb3GTQS0pEV7xraFPtmRnDviNTwWLp15--QUfqfV4AUD1A8LEIOdnLNdMPMOAs1bBFYP9mGKwe3afOiMNejI1FbNQActpl1Dn5JSOj0VrpUv8oLGOR50Jmy5Bvt075vk706T0mDrH7JLdnTObHJmz8ROXNMktHJqfc1vRSPxkXJDH5KwSwyx_JWm24EzSD01Ey5myfMMvtI_15LKU5W-8hft-DgoPlNjRrhyqXprFfJduAin1cNquFPcLjKtf5ufjQrtmEVpi5cVUDA4WYKWUDWBPMukn88rdBmx1MnD83rQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 4.8K · <a href="https://t.me/SBoxxx/20013" target="_blank">📅 13:05 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20012">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">ایران در حال بررسی حملات به  خارج از خاورمیانه  است
اهداف بالقوه شامل پایگاه‌های نظامی در بلغارستان و قبرس، به‌علاوه کابل‌های زیردریایی در تنگه هرمز است.
مسئولان ایرانی به‌طور فزاینده‌ای تعارض مجدد را اجتناب‌ناپذیر می‌دانند و هشدار می‌دهند که حملات به زیرساخت‌های حیاتی ایران می‌تواند جنگ را فراتر از خاورمیانه ببرد.
منبع: FT</div>
<div class="tg-footer">👁️ 4.89K · <a href="https://t.me/SBoxxx/20012" target="_blank">📅 11:07 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20011">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YMHmFm7rJiD4AvQ2dWJWu8oFxngWGjuwUR5Wt_vZqJPupdhC-w-k3hLptjaLmaZZg5SwP2yMcCvePDn7dpJpjA8Nx7-5cwYPh7G4GdVPEmfRerHPJmOwKignD-LW2qSfmuRPK-57tIgu-idbwVzY3p9jDEGCTZQnMXjzHZZf2J5PT5sx_2zKKNgEOkCgKTucPsRACvTmZMNAxC5547WdJlX8ALOl3SGhKECkouAwz6gk7XXNbH3vlj-E8CyloFTxYNvCoCURP5mJ-LiqNqWNH2Xz_THZWEsdzuZiD2RBBnja9tHPO2cklmZwPWqicdwzjittz73MDm1jUJKbBXnvow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نتایج انتخابات داخلی حزب لیکود و چالش‌های پیش رو
در انتخابات داخلی حزب لیکود که روز دوشنبه برگزار شد،
الی کوهن
(وزیر انرژی) در رتبه اول قرار گرفت و پس از او
امیر اوحانا
(رئیس کنست)،
یاریو لوین
(وزیر دادگستری) و
میری رگف
(وزیر حمل‌ونقل) به عنوان برندگان اصلی شناخته شدند.
بنیامین نتانیاهو
از این نتایج ابراز رضایت کرد و اعلام کرد که حزب لیکود در انتخابات
۲۷ اکتبر ۲۰۲۶
به «پیروزی بزرگی» دست خواهد یافت.
گادی آیزنکوت
， رهبر حزب یاشار و رقیب اصلی نتانیاهو، لیست کنونی لیکود را
«لیست ۷ اکتبر»
نامید و آن را مسئول «بدترین فاجعه اسرائیل از زمان تاسیس» دانست. او در پستی در شبکه X، کاندیداهای لیکود را به تقسیم جامعه اسرائیل، عدم پذیرش مسئولیت و ترویج فرار از خدمت سربازی متهم کرد.
لیست تقریبا نهایی حزب لیکود شامل
۲۵ نفر
است که
۸ جایگاه رزرو شده
برای انتخاب‌های شخصی نتانیاهو در نظر گرفته شده است.
گیدئون ساعر
(وزیر خارجه)،
حایم کاتس
(رئیس کمیته مرکزی لیکود) و
اورن دبرونسکی
از جمله افرادی هستند که نتانیاهو آن‌ها را برای این جایگاه‌ها انتخاب کرده است. همچنین،
نیر بارکات
(وزیر اقتصاد) که در رتبه ۲۴ قرار دارد، ممکن است به جایگاهی پایین‌تر منتقل شود.
بر اساس نتایج،
زئو الکین
،
مای گلان
،
یدیت سیلمان
و
اوی دیختر
احتمالاً در انتخابات آینده کرسی خود را در کنست از دست خواهند داد. نظرسنجی‌ها نشان می‌دهد که حزب لیکود در انتخابات آینده بین
۲۲ تا ۲۴ کرسی
به دست خواهد آورد، در حالی که در حال حاضر
۳۲ کرسی
دارد.
مشارکت در انتخابات داخلی لیکود
۵۳.۵٪
بود که نسبت به انتخابات داخلی سال ۲۰۲۲ (۵۸٪) کاهش یافته است. این کاهش مشارکت و همچنین تغییرات در سیستم انتخابات داخلی، که به نتانیاهو اجازه می‌دهد
۸ کاندید
را در بین ۳۰ نفر اول لیست به صورت دستی انتخاب کند، باعث شده است که رقابت برای کرسی‌ها شدیدتر شود.
انتخابات داخلی لیکود نه تنها لیست کاندیداهای حزب را برای انتخابات سراسری تعیین می‌کند، بلکه نشان‌دهنده چالش‌های داخلی و رقابت‌های سیاسی در داخل حزب است. با نزدیک شدن به انتخابات، این لیست می‌تواند تأثیر زیادی بر سرنوشت سیاسی نتانیاهو و حزب لیکود داشته باشد.</div>
<div class="tg-footer">👁️ 5.01K · <a href="https://t.me/SBoxxx/20011" target="_blank">📅 08:09 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20010">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">نشریه "اکسیوس" به نقل از مقامات آمریکایی:   دولت ترامپ از دولت سوریه خواسته بود که خویشتن‌داری کند.</div>
<div class="tg-footer">👁️ 4.76K · <a href="https://t.me/SBoxxx/20010" target="_blank">📅 02:18 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20009">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">نشریه "اکسیوس" به نقل از مقامات آمریکایی:
دولت ترامپ از دولت سوریه خواسته بود که خویشتن‌داری کند.</div>
<div class="tg-footer">👁️ 4.77K · <a href="https://t.me/SBoxxx/20009" target="_blank">📅 02:17 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20007">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eKuL4nGW-azYk5k6tljKMZDhBII9KEQoj7OCCGR1DXTKtWhR6KkOND-PCjBTjol-AB5VFyhD1XGXZmgngi7MdtBuMZLSy9YApfhYFKc70lf465EjmI99BidW382rNNWsp33-lW76MBe9U2V8VcoiaQeqc1vqgTzt8WzDDohIRp-cg2MNZQrwpemtnmt_DSO20TK4O9DI8SUD8PhzwWwK660u1_LBw54uFTQBXqjgaZtoSS9U0hGFCDp5Df57R4l8e6nqnOrj-VVpP2jjsuZybPrkudE-iEG4vP_IrF327ZFZzhJj6u_vry53bNGu2Pj4zf2HN00qXPeHUQqWGNRofA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شاید فکر کنید ایشان امام جمعه خارطوم در سودان باشد اما نه این مرد همان روبرتو کارلوس است که به دین حنیف اسلام مشرف شده و با یک دختر مسلمان به نام سهیلا ازدواج کرده است.</div>
<div class="tg-footer">👁️ 5.94K · <a href="https://t.me/SBoxxx/20007" target="_blank">📅 00:25 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20006">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">ترامپ به مشاورین ارشد خود دستور داده است تا مذاکرات با ایران را متوقف کنند!
دولت ترامپ در حال فاصله گرفتن از تلاش برای "فشار حداکثری فوری بر ایران" و حرکت به سمت یک تلاش بلندمدت برای "تحمیل فشار" بر تهران از طریق فشار اقتصادی و نظامی مداوم است.
به نظر می‌رسد هدف، افزایش تدریجی فشار بر ایران است تا زمانی که این کشور تمایل بیشتری برای پذیرش شرایط ترامپ پیدا کند.
منبع: CNN</div>
<div class="tg-footer">👁️ 4.91K · <a href="https://t.me/SBoxxx/20006" target="_blank">📅 00:18 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20005">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/n4vJCcu4zFyJqK1ydTPoCO7numyAWMyB0NGqPtuOZ_Rh9z--kbluAXLRK3caelDtT3bg5NuaFSEadW-o966zE9sv_gOqeppJJ5TzC7aayHAxj7Mvl6WHZT320Bs9nYh1DVvMT9RUIZQ5cnc922VoWzTwC6cRFceRhd08ucBNg4IrabIUpslt2lLzcaDXMpU5AOrxcU3q7vBmQ5K76eZs_YabWmwiyhFH1Qn_11C2jQvbAhX8S9pDIRFMpW7kSu2P1DJPE0cr-8nrD2Twgh1tFSE8UyUrp-qcw239vvBePzO8QlWGGRsRnD5dYMvLuR8KHuOrJw_H9VrrxYu7NxKtiQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دفتر نتانیاهو:  اسرائیل و سوریه بر سر حفظ وضعیت موجود در مسائل امنیتی به توافق رسیدند، توافقی که سوریه در آستانه نقض آن بود، با اجازه دادن به نیروهای ترکیه ای برای استقرار در یک پایگاه هوایی نزدیک به حلب.  اسرائیل بارها به سوریه هشدار داد که چنین استقراری…</div>
<div class="tg-footer">👁️ 4.96K · <a href="https://t.me/SBoxxx/20005" target="_blank">📅 00:11 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20004">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">دفتر نتانیاهو:
اسرائیل و سوریه بر سر حفظ وضعیت موجود در مسائل امنیتی به توافق رسیدند، توافقی که سوریه در آستانه نقض آن بود، با اجازه دادن به نیروهای ترکیه ای برای استقرار در یک پایگاه هوایی نزدیک به حلب.
اسرائیل بارها به سوریه هشدار داد که چنین استقراری تهدیدی برای امنیت اسرائیل خواهد بود. سوریه این هشدارها را نادیده گرفت.
اسرائیل تهدیدهایی را که امنیت خود را به خطر می‌اندازند، نمی‌پذیرد و از بازگشت به وضعیت موجود استقبال خواهد کرد.</div>
<div class="tg-footer">👁️ 4.92K · <a href="https://t.me/SBoxxx/20004" target="_blank">📅 23:57 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20003">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">امارات متحده عربی، تمامی مبادلات تجاری با ایران را به حالت تعلیق درآورد.</div>
<div class="tg-footer">👁️ 4.98K · <a href="https://t.me/SBoxxx/20003" target="_blank">📅 23:55 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20002">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">پروفسور خوش چشم:  باید برویم آب های فلوریدا را مین گذاری کنیم ...</div>
<div class="tg-footer">👁️ 4.85K · <a href="https://t.me/SBoxxx/20002" target="_blank">📅 23:54 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20001">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f3e373b297.mp4?token=aWocEaQ_Idmgp-nAi3WOu_674R7R7105N25uaC7fHDIT6ZK3X6pR4hipXS1sODFh6Z_siWZlzSZqFGKMGMLQDIPyL_MX0PultKEUM0S1wWBWE9dkC4ANuF-MJdRqtuDxd5tTWkntFtFnzeS5W-07nd5GuwzUpJJd6Q3G4mSa3aImK9RpU6tnsf0zNlAoFfyrmI6CwUaXKS1gPwNHSZJVFZKlLv8lbsSjTw4EDWuaFpbqmhRa25HvzU721bPSCH6GveEsgkbBmizKHoZHwIlRklxg4I7NP28NknfXSHzx6sT40FjL8IfUPVCyzSzpH_aiX5tB2AuwpaDGEiOe_H4xBg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f3e373b297.mp4?token=aWocEaQ_Idmgp-nAi3WOu_674R7R7105N25uaC7fHDIT6ZK3X6pR4hipXS1sODFh6Z_siWZlzSZqFGKMGMLQDIPyL_MX0PultKEUM0S1wWBWE9dkC4ANuF-MJdRqtuDxd5tTWkntFtFnzeS5W-07nd5GuwzUpJJd6Q3G4mSa3aImK9RpU6tnsf0zNlAoFfyrmI6CwUaXKS1gPwNHSZJVFZKlLv8lbsSjTw4EDWuaFpbqmhRa25HvzU721bPSCH6GveEsgkbBmizKHoZHwIlRklxg4I7NP28NknfXSHzx6sT40FjL8IfUPVCyzSzpH_aiX5tB2AuwpaDGEiOe_H4xBg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پروفسور خوش چشم:
باید برویم آب های فلوریدا را مین گذاری کنیم ...</div>
<div class="tg-footer">👁️ 5.61K · <a href="https://t.me/SBoxxx/20001" target="_blank">📅 22:49 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20000">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">تاکر کارلسون می گوید که اعتقاد ندارد که انسان‌ها بمب اتمی را ساخته‌اند.</div>
<div class="tg-footer">👁️ 4.92K · <a href="https://t.me/SBoxxx/20000" target="_blank">📅 21:02 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19999">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">تاکر کارلسون می گوید که اعتقاد ندارد که انسان‌ها بمب اتمی را ساخته‌اند.</div>
<div class="tg-footer">👁️ 4.96K · <a href="https://t.me/SBoxxx/19999" target="_blank">📅 21:01 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19998">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromپیکنیک تحلیل</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mMg5_NVDpyojFyLnQt9glOQarLtXDeho55D96uhy3-xdCybDFf6nbSroxUnR1Qs4Wxkl_qkgKe65l6HTKgJCxbZdznv7uzo4OilKvuFNtPjQH2cS3jUe92I0TkvL3S_GABTkseBAlkApfd1wz83u9CN_oOhJQ0vJqNsxVkanBMrWqTmWKYCzRzZF81psK89NrNNdi51aYkp1b3PIEqQkNpyhD4AewW0W8GGx6g7YeFAQkX_ql_9HzoHz-McKMmSR1kl2TNYwyfdyTWdAc0TUvsdXppUZWY53cxlF0ogvo66XfQbMdtXNRnvMBElTKFHMGqi9NqZ0kQgPcM2qkN4k2g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبر کوتاه بود و دردناک!
تادالافیل ۷۰۶ درصد افزایش نرخ گرفت
@PiknikAnalyst</div>
<div class="tg-footer">👁️ 4.66K · <a href="https://t.me/SBoxxx/19998" target="_blank">📅 20:30 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19997">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">یکی رهگیری شده و دیگری در آب افتاده!</div>
<div class="tg-footer">👁️ 4.8K · <a href="https://t.me/SBoxxx/19997" target="_blank">📅 20:15 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19996">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">وزارت دفاع امارات در پلتفرم ایکس اعلام کرد  : وزارت دفاع امارات دو موشک بالستیک پرتاب‌شده از ایران را شناسایی کرده است.</div>
<div class="tg-footer">👁️ 4.89K · <a href="https://t.me/SBoxxx/19996" target="_blank">📅 20:12 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19995">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">وزارت دفاع امارات در پلتفرم ایکس اعلام کرد
: وزارت دفاع امارات دو موشک بالستیک پرتاب‌شده از ایران را شناسایی کرده است.</div>
<div class="tg-footer">👁️ 4.96K · <a href="https://t.me/SBoxxx/19995" target="_blank">📅 20:09 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19994">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">#GRI  برای امروز شاخص ریسک ژئوپولیتیک در سطح نسبتاً بالایی قرار دارد و افت قیمت طلا پیش بینی می شود.</div>
<div class="tg-footer">👁️ 4.89K · <a href="https://t.me/SBoxxx/19994" target="_blank">📅 18:48 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19993">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">گویا حمله به امارات کار انصارالله (حوثی ها) است.</div>
<div class="tg-footer">👁️ 4.86K · <a href="https://t.me/SBoxxx/19993" target="_blank">📅 18:34 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19992">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-footer">👁️ 4.81K · <a href="https://t.me/SBoxxx/19992" target="_blank">📅 18:34 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19991">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">انفجارات در بندر جبل علی امارات</div>
<div class="tg-footer">👁️ 4.7K · <a href="https://t.me/SBoxxx/19991" target="_blank">📅 18:30 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19990">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/53cb17e6f7.mp4?token=OnI4PINLex7MtdvRKf5Y9cw114eRrFWTjXtQ-mBPlfPWSxYLFiFCkBDoSR0njFlLwNQiLuvRf14qwV9SWW8-Ir7Vv3K-02SuMgigHo4nkF8l7udIlhVPYj99XDHOqgvB8b66KQULkoaWknNozPo8Yvtmwsxv1ZzeBgzKnnh43b2yAF7IrCpMVoVDFcirKnieoNNFfIThOfHRKjoT3ayW4VfMHpu1uVs4B6bsFmIfNID_RSqbjN3VTw-vwbro_NIU8d42R4F0Gtigia4Qy3BDxPOUFncEB26N8-IgVxgRprShHaTlp0WKrMc0NI7gNx0BL3-wcCUQWuxMw9FOXO53IA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/53cb17e6f7.mp4?token=OnI4PINLex7MtdvRKf5Y9cw114eRrFWTjXtQ-mBPlfPWSxYLFiFCkBDoSR0njFlLwNQiLuvRf14qwV9SWW8-Ir7Vv3K-02SuMgigHo4nkF8l7udIlhVPYj99XDHOqgvB8b66KQULkoaWknNozPo8Yvtmwsxv1ZzeBgzKnnh43b2yAF7IrCpMVoVDFcirKnieoNNFfIThOfHRKjoT3ayW4VfMHpu1uVs4B6bsFmIfNID_RSqbjN3VTw-vwbro_NIU8d42R4F0Gtigia4Qy3BDxPOUFncEB26N8-IgVxgRprShHaTlp0WKrMc0NI7gNx0BL3-wcCUQWuxMw9FOXO53IA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ:   هیچ مذاکره ای با جمهوری اسلامی ایران در جریان نیست و برنامه ریزی نشده.   محاصره دریایی با تمام شدت و اثر باقی هست.   تنگه هرمز باز و در حال عمل است. تمام مین های دریایی هم حذف و یا خنثی شده اند.   از توجه شما به این موضوع سپاسگزارم، دانلد جی. ترامپ</div>
<div class="tg-footer">👁️ 5.37K · <a href="https://t.me/SBoxxx/19990" target="_blank">📅 18:26 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19989">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">طنز تاریخ در این است که پیمان دفاع مشترکی که عربها با ترک‌ها بسته اند دقیقا ۱۱۰ سال پس از جنگی روی داده که میان خودشان در قالب شورش «شریف حسین» ضد عثمانی ها درگرفت و اتفاقا نخستین شهری که عربها آزاد کردند همین «مکه» بود که نامش اکنون شده لقب پیمان دفاعی اخیر!…</div>
<div class="tg-footer">👁️ 4.52K · <a href="https://t.me/SBoxxx/19989" target="_blank">📅 18:19 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19988">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">باز سعودی ها دستکم کتک خوردن ترک‌ها در سوریه از اسراییل برای بار پنجم را محکوم کردند!  شهناز جوراب که کلا خودش را زده به کوچه علی چپ!   نه حملات یمنی ها به سعودی را محکوم کرد نه حملات اسراییلی ها به ترک‌ها را !  سبحان الله عجب پیمانی شد این پیمان ناتوی اسلامی…</div>
<div class="tg-footer">👁️ 4.52K · <a href="https://t.me/SBoxxx/19988" target="_blank">📅 18:17 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19987">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">— عربستان حملات اسرائیل به فرودگاه ابوظهور در ادلب سوریه را محکوم کرد.</div>
<div class="tg-footer">👁️ 5.18K · <a href="https://t.me/SBoxxx/19987" target="_blank">📅 18:14 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19986">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">اسرائیل فرودگاه ابوالظهور در ادلب را با ۴ حمله بمباران کرد.   طبق گزارش‌ها، نیروهای ترکیه در این فرودگاه مستقر هستند.</div>
<div class="tg-footer">👁️ 4.71K · <a href="https://t.me/SBoxxx/19986" target="_blank">📅 18:12 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19985">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">ترامپ:
هیچ مذاکره ای با جمهوری اسلامی ایران در جریان نیست و برنامه ریزی نشده.
محاصره دریایی با تمام شدت و اثر باقی هست.
تنگه هرمز باز و در حال عمل است. تمام مین های دریایی هم حذف و یا خنثی شده اند.
از توجه شما به این موضوع سپاسگزارم، دانلد جی. ترامپ</div>
<div class="tg-footer">👁️ 4.87K · <a href="https://t.me/SBoxxx/19985" target="_blank">📅 18:08 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19984">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">دولت تایوان به هر شهروند این کشور مبلغ ۳۱۴ دلار به عنوان «سود تقسیمی هوش مصنوعی» پرداخت می کند که ناشی از جهش اقتصادی این کشور به دلیل رشد تقاضا برای محصولات مرتبط با صنعت هوش مصنوعی است.</div>
<div class="tg-footer">👁️ 5.32K · <a href="https://t.me/SBoxxx/19984" target="_blank">📅 14:20 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19983">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">کشتی یونانی در هرمز هدف قرار گرفت
کشتی فله‌بر «Minoan Dignity» متعلق به یونان، هنگام عبور از تنگه هرمز هدف یک پرتابه ناشناس قرار گرفت و موتورخانه آن آسیب دید.</div>
<div class="tg-footer">👁️ 5.14K · <a href="https://t.me/SBoxxx/19983" target="_blank">📅 13:44 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19982">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">مادرقحبه ها این چه وضع اینترنت است؟!</div>
<div class="tg-footer">👁️ 5.23K · <a href="https://t.me/SBoxxx/19982" target="_blank">📅 13:35 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19981">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">با پایان مدت تعیین شده برای نهایی سازی توافقنامه اسلام آباد، اسراییل حملات سنگین خود به جنوب لبنان را از سر گرفت</div>
<div class="tg-footer">👁️ 5.18K · <a href="https://t.me/SBoxxx/19981" target="_blank">📅 13:28 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19980">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">اسرائیل فرودگاه ابوالظهور در ادلب را با ۴ حمله بمباران کرد.
طبق گزارش‌ها، نیروهای ترکیه در این فرودگاه مستقر هستند.</div>
<div class="tg-footer">👁️ 5.28K · <a href="https://t.me/SBoxxx/19980" target="_blank">📅 07:51 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19979">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">اگر تن ندارید لااقل آماده باشید!</div>
<div class="tg-footer">👁️ 5.36K · <a href="https://t.me/SBoxxx/19979" target="_blank">📅 00:54 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19978">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">خب رفتیم برای موج C از ۲ و چند صباحی دیگر فرصتی برای خرید تن و دلار و نفت</div>
<div class="tg-footer">👁️ 5.57K · <a href="https://t.me/SBoxxx/19978" target="_blank">📅 00:54 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19977">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jmtEMe1OdhlzhrRmuDol8md_WiecSeMlwU5jrsHJvStw2GQGAQgWWeco7raERuqwend9uLTEacAYO8wj3o3okYLSPfd6V5m80vAAavF0BOUScRao1XPoja9--H26FPKv3MSQj_GlTQWwEtseBaRotS4W3mK1Q1Jz6t2w19dMUKvVdxPwx8CODQXlvhZQIsKskP3dqjxHGOZvfkPIx6NeiFrWd2MYCAfkVBrovhj8cJ-9nxQnY66xgVLNXF4moiklzG84-bmtvDMIXWUNarJHJMDgilu4tOFWWJvtIhLJ5WJC9VPc17L_TFoJNeHj4tlsHcv8QSeoTGCSrb8cEo4u9w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#USOIL — H4  پوزیشن پیشنهادی.  ریوارد به ریسک خوبی دارد.</div>
<div class="tg-footer">👁️ 5.52K · <a href="https://t.me/SBoxxx/19977" target="_blank">📅 00:53 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19976">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">محسن رضایی :
تا حالا زیادی صبر کرده ایم ، لازم شود از NPT خارج میشویم و خودتان میدانید این یعنی چه!</div>
<div class="tg-footer">👁️ 5.44K · <a href="https://t.me/SBoxxx/19976" target="_blank">📅 00:46 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19975">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IsXwO886Jvbz7T3Yea7Ix7kxFUXXBee9xFQmSO9ZTrRWovl87Ny8XkeaOmtgSMeo2YpPUaCExbz97K1nyb6BFPbPxqaYvs3tmgWsfcWi9cTPjc4e1_RPNxV0g5M7moUcmxAFXnc1FdXytSJCJ4y0yUDnwRDCD-oS-YMtcIIQLjM7MNh0astu8r8qanewoTiPQHFba9wPIEHFVMOD54-CZ1t1uhT4y8cjrNwtMmwVoCmGCj0AchWFcL_sCt9451XYSUjUVwnO37MX_S8uw7-YPLOvx3Y4IZCQp8hj57rFHRF8sK62mG0akqm8S_iUZJ_w5IlzItxrFcOFQgmHqanc1g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 5.31K · <a href="https://t.me/SBoxxx/19975" target="_blank">📅 00:43 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19974">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">جرد کوشنر درباره ایران:
در حال حاضر،  ترامپ بر فشار اقتصادی متمرکز شده است.
اگر ایران مایل به پایان دادن به توافقی است که آنها با ما در مورد آن صحبت می کردند تا از توانایی خود در ساخت سلاح هسته ای چشم پوشی کند، واضح است که او مایل است توافقی را انجام دهد که می تواند برای مردم ایران عالی باشد، اما در حال حاضر آنها هیچ علاقه ای به انجام کاری که برای ما منطقی است نشان نمی دهند.</div>
<div class="tg-footer">👁️ 5.15K · <a href="https://t.me/SBoxxx/19974" target="_blank">📅 23:02 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19973">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/D1zu1aqIMvEZK2Ol1Wu_fXWBjC0OatCSqrzSA7GGKR05fyetq8hJh9PgIyFWSsqTZYMtO3C--7awQtZnCinyROATgA29n0ebJbp0y3UIGZ7S3WKNRakNLPsKlTvBAukTOiFP1g5VsdQrS4BTkPuiOwFkvVkokiIHonYEdmFrJ79u0pCLyeHn6Q9iq8S7HgB0oglrfiu_XxDKb_hWO1sHKz3um0qZKTGc_b9INDC2WYtnkSWgIMrg7jfXYGtpy_lrTpmNwVGoodtPtNNhAwGvmHsBGP0zwpAl-A52BSGOgdr93GVUJGT3hv0PPcZDKBQ5AE5B1c0h3zs0izNtiiPjiw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 5.11K · <a href="https://t.me/SBoxxx/19973" target="_blank">📅 22:10 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19972">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">ترامپ:   توافق با ایران را لغو خواهیم کرد.</div>
<div class="tg-footer">👁️ 5.21K · <a href="https://t.me/SBoxxx/19972" target="_blank">📅 22:09 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19971">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">ترامپ در مورد ایران:
آن‌ها می‌خواهند توافقی انجام دهند، اما قصد ندارند آن نوع از توافقی را انجام دهند که من احساس می‌کنم ضروری است.</div>
<div class="tg-footer">👁️ 5.19K · <a href="https://t.me/SBoxxx/19971" target="_blank">📅 21:42 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19970">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-footer">👁️ 5.1K · <a href="https://t.me/SBoxxx/19970" target="_blank">📅 21:41 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19969">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">ترامپ:
توافق با ایران را لغو خواهیم کرد.</div>
<div class="tg-footer">👁️ 5.4K · <a href="https://t.me/SBoxxx/19969" target="_blank">📅 21:40 · 26 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>

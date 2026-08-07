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
<img src="https://cdn4.telesco.pe/file/XnLpwzIENamoe8aIX6EcLx25NL2k711TOXDLwjLpk2CI2mm5ymJ68TaZcP_6YB4aCmckgKKykeifyM0giteWg_4TqWHmEvO_VwRuNx9UzS0W0HYP20o2nE5MTABdEgnWehgzKTv7ncF4IZJI0kPfXVBRrKC9gzk0ZkSO00i-MAh5szWYoi6NodWuhVOGBD0slqCjBNoC6nBdKLro95lbWfJP2jd4FncsppQeiPPpwwareqcvpm5ZluM0gGEtFH9ZJXiCOd1CVaE73HIkgClUcolxtVvPYgwTWoOk3A2q9PZu4VLloyt1_ZZy5X8FZg-mTfTrA0TKgKwt61kFucX5SQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Secret Box</h1>
<p>@SBoxxx • 👥 10.6K عضو</p>
<a href="https://t.me/SBoxxx" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 تاریخ، ژئوپولیتیک و بازارهای مالیhttps://secretboxxx.com/</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-16 23:14:41</div>
<hr>

<div class="tg-post" id="msg-19791">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">رئیس‌جمهور ایران، مسعود پزشکیان:
من نه تنها از شهادت نمی‌ترسم، بلکه آن برای من یک پیروزی بزرگ است.</div>
<div class="tg-footer">👁️ 1.52K · <a href="https://t.me/SBoxxx/19791" target="_blank">📅 22:35 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19790">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">GeoMarkets Podcast Text.pdf</div>
  <div class="tg-doc-extra">402.9 KB</div>
</div>
<a href="https://t.me/SBoxxx/19790" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">Ali SharifAzadeh – GeoMarkets - podcast 21</div>
<div class="tg-footer">👁️ 2.07K · <a href="https://t.me/SBoxxx/19790" target="_blank">📅 22:05 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19789">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">رسانه های اسراییلی:
محسن رضایی جزو اهداف ترور است.</div>
<div class="tg-footer">👁️ 3.22K · <a href="https://t.me/SBoxxx/19789" target="_blank">📅 20:47 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19788">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">در عصر اقتصاد دانش بنیان، تنگه بندی و گردنه گیری تنها منجر به انزوا و تیپا خوردن خود عامل می‌شود و اندونزیایی ها خیلی سریع فهمیدند که این لقمه برای دهانشان بزرگ است ولی خب.</div>
<div class="tg-footer">👁️ 3.45K · <a href="https://t.me/SBoxxx/19788" target="_blank">📅 19:53 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19787">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">انصافاً ببینید کشورهای منطقه (خصوصاً عراق و کویت که راهی جز هرمز برای صادرات نفت ندارند) برای گریز از اخلال ایران در هرمز چه می کنند.  خط لوله کرکوک—جیحان که الان هم فعال است.  خط لوله شرق—غرب عربستان به ینبع برای خود سعودیها فعال است و گویا عراقی ها و کویتی…</div>
<div class="tg-footer">👁️ 3.74K · <a href="https://t.me/SBoxxx/19787" target="_blank">📅 19:53 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19786">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OVxLlwFHwUCjqiMhCllb3j8TwY6repdRYJL8S5nzU8UxYMqgBRh7woxx98XibAZLqQ5rZzZ_lbzYPON3cVvef_otFRZNfmr2meYoyDpqbv9VFtLnm4N-Ys9cL7XVinWM4duuO9wyx3e6GiiNBuz_vLQFDs4YmH8d3xdj-_IfqBA2ybk8sOkRS9uwbVDdJ73tOkg7zYw8Q47Mg-UKm_vrPWFMSQtljGFoxsKwQdckrD7G2Us5-1tS30R6Asp0wSfaxcS4xAA0PwagibxycBkrz0CoWsq-BGCwX-ANFvA5h7zyHKz0CfMpmWf0Tl-B-ErhKvZjs3HHLkom8suUvseWTQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#VIX
با شاخص های سهام در سقف و نفت کنترل شده، همه چیز برای ماجراجویی دوباره ترامپ آماده است.</div>
<div class="tg-footer">👁️ 3.59K · <a href="https://t.me/SBoxxx/19786" target="_blank">📅 19:18 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19785">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VviX_gtYT2zcytMnLujQbDF_jXpwHVFfrmvJsy4qOIyTRX1WCaO5aTdTxRidsnJr5nmX1-jfLxsWH44Z3TUGeV2Bz72qWyKseGT4CTmAKCe4jD7-TEALu4uRhqiVh87uIkPR6MGk7O5ggXaleTA5hcjeGgFAGa4pBdpKb61s8dwo37cna66K1l74eJWNzrQgBEp9GcGV1KFckE9hlxU4O-podr4OgK9SPCbwqLnEkXuWyZg7Q4fUvdqjr-YFZ3oIo1PHJzBn4QGb29ow3ysgTcR0LuWhHbGYMXcq04Jb4qaKRbuZETaU_tgnWODXbjc4P4KQIU68BvzH8n2-cO9_3Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#XAUUSD — H4  میتوان چنین ساختاری برای طلا متصور بود.</div>
<div class="tg-footer">👁️ 3.63K · <a href="https://t.me/SBoxxx/19785" target="_blank">📅 19:03 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19784">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">ریاست جمهوری ترکیه:   هرگونه حمله مسلحانه به هر یک از کشورها، از جمله ترکیه، عربستان سعودی و پاکستان، حمله به همه آنها تلقی می‌شود</div>
<div class="tg-footer">👁️ 3.57K · <a href="https://t.me/SBoxxx/19784" target="_blank">📅 18:41 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19783">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iMkWA7TqdXNkb-msjKqL2PFcuDGoR1vI1v2AS2OYCperHpT2eVC7WR2rZXlGSlrTAB36tpRETBV7TrnApE02yeZ1AKMiPKO5Iv1Yd2BGt3k-LF42XrDKZlpqct2cKZy7OpA6G1bpSs5ezm1vWBjUqTIWRfuRrf4xVoms3aIlstrl_5fsVzCq8482Z31DuDlIp_dKk2fSZ7-UZwrtN5rUKN12ZzcwcHf4VtIRCoAxeXeegsx_nDdnziS870B7u0Z8GoRyysB08OrGndIUFYV1tLebb_sHV3pNZvL8u-M-QlF25qW1HmJ5sK6HZXauLUjG2zbULkpGvZd6DyZn3xihMQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ریاست جمهوری ترکیه:   هرگونه حمله مسلحانه به هر یک از کشورها، از جمله ترکیه، عربستان سعودی و پاکستان، حمله به همه آنها تلقی می‌شود</div>
<div class="tg-footer">👁️ 3.96K · <a href="https://t.me/SBoxxx/19783" target="_blank">📅 17:52 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19782">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">💙
تبریز
💙</div>
<div class="tg-footer">👁️ 3.71K · <a href="https://t.me/SBoxxx/19782" target="_blank">📅 17:39 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19781">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">اسکات بسنت در مورد ایران:
ما آن‌ها را از گلو گرفته‌ایم و آن‌ها تورم غذایی ۱۵۰ تا ۱۸۰ درصد دارند و نمی‌توانند به سربازان حقوق بدهند.
فکر می‌کنم به زودی، شاید حتی امروز یا فردا، قرار است یک توافق را ببینیم، یک آتش‌بس ۳۰ تا ۶۰ روزه و تنگه باز خواهد شد.
قیمت‌های انرژی باید کاهش یابد.
منبع: 12 News</div>
<div class="tg-footer">👁️ 3.78K · <a href="https://t.me/SBoxxx/19781" target="_blank">📅 17:30 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19780">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">تحلیلی برگریزان از خرازی درباره پاکستان، هند و چین!</div>
<div class="tg-footer">👁️ 3.98K · <a href="https://t.me/SBoxxx/19780" target="_blank">📅 15:39 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19779">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3b35e228b4.mp4?token=vBNW6kw90xZPkX9FFNOyPeLbbPuwAYdoxRDIPEoELxyESPZZ3wTfORXqL3yl50twC-OYW-sVIpmrJPWkNF25l0S3FV5t-Do0ZU3obf5bQZn5xvtYPopg3aL4NHq9STKKPvYXwKsoJE0HcI_RbNF9_yORUDbQzdT2X93AL038bV4sYaQYNlBxSH8VVnf7VKhsa9lAQuse4hpDuO7iPIvFxv98DHjzWUNG64nNu17D_fCh74o2WyZ53bu0x_kL5hbTtk5muXBpS3AnpoNvdbJtqwhxUELEAMJXcTI16NpgbKf1GVpJH0BaXf8x1oEwC-LbDXiUHwzQCjmDMV2JYXiImQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3b35e228b4.mp4?token=vBNW6kw90xZPkX9FFNOyPeLbbPuwAYdoxRDIPEoELxyESPZZ3wTfORXqL3yl50twC-OYW-sVIpmrJPWkNF25l0S3FV5t-Do0ZU3obf5bQZn5xvtYPopg3aL4NHq9STKKPvYXwKsoJE0HcI_RbNF9_yORUDbQzdT2X93AL038bV4sYaQYNlBxSH8VVnf7VKhsa9lAQuse4hpDuO7iPIvFxv98DHjzWUNG64nNu17D_fCh74o2WyZ53bu0x_kL5hbTtk5muXBpS3AnpoNvdbJtqwhxUELEAMJXcTI16NpgbKf1GVpJH0BaXf8x1oEwC-LbDXiUHwzQCjmDMV2JYXiImQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تحلیلی برگریزان از خرازی درباره پاکستان، هند و چین!</div>
<div class="tg-footer">👁️ 4.08K · <a href="https://t.me/SBoxxx/19779" target="_blank">📅 15:38 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19778">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">ارتش یمن بیانیه مهمی صادر می‌کند
سرتیپ یحیی سریع، سخنگوی نیروهای مسلح یمن اعلام کرد که نیروهای مسلح این کشور به زودی بیانیه‌ای درباره عملیات منحصر به فرد نظامی خود صادر می‌کند.</div>
<div class="tg-footer">👁️ 4.06K · <a href="https://t.me/SBoxxx/19778" target="_blank">📅 15:13 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19777">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-footer">👁️ 4.02K · <a href="https://t.me/SBoxxx/19777" target="_blank">📅 15:12 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19776">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">نکته جالب اینکه مهلت حشدالشعبی به دولت عراق فردا پایان می یابد و یمنی ها هم حملات خود را به سعودی تشدید کرده اند!  یعنی اگر فردا این پیمان دفاعی میان ترک‌ها و پاکستانی ها و سعودی ها امضا بشود، از پسفردا باید شاهد حملات متقابل اینها به حشدالشعبی و حوثی ها باشیم.…</div>
<div class="tg-footer">👁️ 4.42K · <a href="https://t.me/SBoxxx/19776" target="_blank">📅 15:05 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19775">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">ماده اصلی توافق مکه یک بند دفاع جمعی است.  هر حمله مسلحانه علیه یکی از این سه کشور به عنوان حمله علیه همه آنها تلقی می‌شود.  هدف آن تقویت بازدارندگی جمعی در برابر تجاوز و تقویت همه جنبه‌های همکاری دفاعی میان این سه کشور است.</div>
<div class="tg-footer">👁️ 4.1K · <a href="https://t.me/SBoxxx/19775" target="_blank">📅 14:54 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19774">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">نکته جالب اینکه مهلت حشدالشعبی به دولت عراق فردا پایان می یابد و یمنی ها هم حملات خود را به سعودی تشدید کرده اند!  یعنی اگر فردا این پیمان دفاعی میان ترک‌ها و پاکستانی ها و سعودی ها امضا بشود، از پسفردا باید شاهد حملات متقابل اینها به حشدالشعبی و حوثی ها باشیم.…</div>
<div class="tg-footer">👁️ 4.13K · <a href="https://t.me/SBoxxx/19774" target="_blank">📅 14:05 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19773">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">ترامپ درباره ایران:
آن‌ها می‌خواهند معامله‌ای انجام دهند. ببینید، واضح است که نمی‌خواهند مورد حمله قرار بگیرند. آن‌ها می‌خواهند معامله‌ای انجام دهند. بنابراین، خواهیم دید.</div>
<div class="tg-footer">👁️ 4.16K · <a href="https://t.me/SBoxxx/19773" target="_blank">📅 13:28 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19772">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">GeoMarkets - podcast 21</div>
  <div class="tg-doc-extra">Ali SharifAzadeh</div>
</div>
<a href="https://t.me/SBoxxx/19772" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">#پادکست_GeoMarkets
شماره — 21
جمعه 7 آگوست 2026</div>
<div class="tg-footer">👁️ 4.73K · <a href="https://t.me/SBoxxx/19772" target="_blank">📅 13:16 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19771">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">پیشروی بی سابقه حزب AfD در آلمان
حزب موسوم به گزینه جایگزین برای آلمان در نظرسنجی‌ها به بالاترین حد تاریخی خود یعنی ۲۸ درصد رسید و فاصله خود را با ائتلاف CDU/CSU افزایش داد، در حالی که حمایت‌های محافظه‌کارانه به پایین‌ترین سطح خود از سال ۲۰۲۱ سقوط کرد.</div>
<div class="tg-footer">👁️ 4.1K · <a href="https://t.me/SBoxxx/19771" target="_blank">📅 13:10 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19770">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZvOH4FBZq8UbOeKKGUskVMlOihqaqZlmLfB4b1aS8SyyFKQxBapivC4moofYxy1EHL2NCplS9MoaFo_zY5oY0eynBo4DwlsOyi7keP2XMrmXBOywxu3xvxIgWFvN-2PqRMriHzecWt_Rz9UVWeOPkMLvLvc2R0CSRlvYJvf6ytPPXPeir84bSKWSvPXGOqL2KTd2RB9dbvo-vvVxMawOer8z1cItK1IklvqX1szGx99d0w4-Vchp2xtQrmNLEOp_3VaJruc5uGo_WRehXzMgB0cssfnwRCj14ZybswzH_ntMYD5ryzpE4pfgQZ5QFR6mxEdv4qm9jyI2yluj4vUfag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#GRI
شاخص ریسک ژئوپولیتیک برای امروز در سطح بسیار بالایی قرار دارد که البته بخشی از آن به دلیل تقویم اقتصادی (گزارش NFP) است.
انتظار یک افت اصلاحی در طلا می رود.</div>
<div class="tg-footer">👁️ 4.18K · <a href="https://t.me/SBoxxx/19770" target="_blank">📅 11:19 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19769">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">مسئول ارشد سابق در پنتاگون و مدیر ارشد در مرکز اسکروفت در مورد ذخایر تسلیحاتی ایالات متحده:  «محاسبات مربوط به مهمات برای ایالات متحده بسیار جدی است،» او گفت. «با هر عملیات هوایی علیه اهداف ایرانی و حملات تلافی‌جویانه بعدی ایران، ایالات متحده توانایی‌های حیاتی…</div>
<div class="tg-footer">👁️ 4.17K · <a href="https://t.me/SBoxxx/19769" target="_blank">📅 11:16 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19768">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lRyJzX6aclD1wWI4iNphV7_Qztga4oBZcdq9uyWItANnO37GxyKXqMOnYv5HsZqJuo36rkSSuhSKtF2veLpcFjnnkKJnKJK1VDZSqxvRpMOxim-E_oe9_N9QZAshTP-X8TIFTko_XECwy3UTfahcsE3XuQFV0UTz3qbka-ywKbhOhJtGv3T_lrxj6P2ZFkEIqZSyy2Mg1W0cWLRNH298U5gtbsP7FiXkuHsdOujD1i68Wgbe9UIB_UUJiVh3lE6c39FrBmF3Asg6P5I34nMBMr88FJRc-RiK5ni6KTQNSq2YHJsxJZrwmx6RkoaF45KZn8HtdEIwZvI7LzZB64w1kQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#GRI  برای امروز شاخص ریسک ژئوپولیتیک در سطح میانه قرار دارد. پیش بینی می شود طلا امروز مقداری افت اصلاحی داشته باشد (با توجه به رشد GRI از دیروز) اما دوباره به سقف (4300) حمله ور بشود (با توجه به افت میانگین شاخص GRI در روزهای گذشته)</div>
<div class="tg-footer">👁️ 4.17K · <a href="https://t.me/SBoxxx/19768" target="_blank">📅 11:12 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19767">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">وزارت دفاع آمریکا، قرارداد ۵۸ میلیارد دلاری برای سیستم پدافند هوایی پاتریوت به شرکت لاکهید مارتین اعطا کرد.  این قرارداد به ارزش تا ۵۸.۶ میلیارد دلار، مربوط به موشک‌های رهگیر پاتریوت است و تولید این سیستم را تا سال ۲۰۳۲ افزایش می‌دهد. این اقدام در حالی صورت…</div>
<div class="tg-footer">👁️ 4.35K · <a href="https://t.me/SBoxxx/19767" target="_blank">📅 11:05 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19766">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">نکته جالب اینکه مهلت حشدالشعبی به دولت عراق فردا پایان می یابد و یمنی ها هم حملات خود را به سعودی تشدید کرده اند!  یعنی اگر فردا این پیمان دفاعی میان ترک‌ها و پاکستانی ها و سعودی ها امضا بشود، از پسفردا باید شاهد حملات متقابل اینها به حشدالشعبی و حوثی ها باشیم.…</div>
<div class="tg-footer">👁️ 4.48K · <a href="https://t.me/SBoxxx/19766" target="_blank">📅 03:01 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19765">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">ترکیه، عربستان و پاکستان در آستانه امضای پیمان دفاعی سه‌جانبه   رجب طیب اردوغان، رئیس‌جمهور ترکیه، روز جمعه راهی عربستان سعودی می‌شود تا در نشستی سه‌جانبه با محمد بن سلمان، ولیعهد سعودی، و شهباز شریف، نخست‌وزیر پاکستان، یک توافق دفاعی مشترک را به امضا برساند؛…</div>
<div class="tg-footer">👁️ 4.49K · <a href="https://t.me/SBoxxx/19765" target="_blank">📅 02:57 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19764">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">عجیب است!  الان دیدم در 17 مارس امسال — یعنی اوج جنگ 40 روزه — پنتاگون در حال نهایی کردن طرح استفاده از کلاهک های کوچک هسته ای به عنوان یک گزینه معمول جنگی (با حساسیت کمتر نسبت به جنگ تمام عیار هسته ای) بوده است.  لینک</div>
<div class="tg-footer">👁️ 4.43K · <a href="https://t.me/SBoxxx/19764" target="_blank">📅 02:21 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19763">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/t-ufZBnmQBGesdTvCPyx7KTFK_K2uJiXF3C2Ro9K_qXc4uue-3a4hnshzF5C7bGOJnW9LDpd856ffNricmu1d15m1DwjveBbOfFZk_AGH1hj1OlBwxGWdUa1dX71ExQ7UaecPViRGt6u442e1Crj41r1wpTXgky7sUDGpN4e-FoX1_TF_bHrJxk3oicnqIOyHx4fPf3qYGAFG3LVNJgTc6t4ldbzjFXDI_zS_X_y3orP2cpopuPSgw6AXNMoFU1Ek-jhymcqulw8ry697UVXoGzveO9cnv6v51a-TcAancriqdsZYx5MTaWi3aHztK4Qme1xePKClZP0OtUOb3KsNw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این منطقه سبز بالای مرزهای کنونی یمن که جیزان نیز در آن قرار دارد، تا سال 1934 متعلق به یمن بود که در پی جنگ آن سال به چنگ سعودی ها افتاد.   هنوز هم برخی ملی گرایان یمنی نسبت به جیزان، عسیر و نجران ادعاهای ارضی دارند و آن سرزمین ها را مال یمن می دانند.  #تاریخ</div>
<div class="tg-footer">👁️ 4.29K · <a href="https://t.me/SBoxxx/19763" target="_blank">📅 02:10 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19762">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">ترکیه، عربستان و پاکستان در آستانه امضای پیمان دفاعی سه‌جانبه
رجب طیب اردوغان، رئیس‌جمهور ترکیه، روز جمعه راهی عربستان سعودی می‌شود تا در نشستی سه‌جانبه با محمد بن سلمان، ولیعهد سعودی، و شهباز شریف، نخست‌وزیر پاکستان، یک
توافق دفاعی مشترک
را به امضا برساند؛ توافقی که می‌تواند به شکل‌گیری یکی از مهم‌ترین ترتیبات امنیتی جدید در خاورمیانه منجر شود.
این توافق سه‌جانبه که بنا بر گزارش رویترز قرار است در جریان دیدار رهبران سه کشور نهایی شود، در شرایطی شکل می‌گیرد که جنگ ایران و افزایش بی‌ثباتی در منطقه، معادلات امنیتی خاورمیانه را وارد مرحله تازه‌ای کرده است.</div>
<div class="tg-footer">👁️ 4.36K · <a href="https://t.me/SBoxxx/19762" target="_blank">📅 02:03 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19761">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">نگاهی به فیلم «رشته ها»!   امروز، ۶ اوت، سالروز بمباران اتمی هیروشیماست؛ روزی که در سال ۱۹۴۵ برای نخستین‌بار در تاریخ، یک سلاح هسته‌ای علیه یک شهر به کار گرفته شد و جهان وارد عصر جدیدی شد که در آن یک بحران نظامی می‌تواند، در صورت خروج از کنترل، به تهدیدی برای…</div>
<div class="tg-footer">👁️ 4.25K · <a href="https://t.me/SBoxxx/19761" target="_blank">📅 01:17 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19760">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">عجب پولیتیکی زده اند.  به نظرم مراکش — که بشدت در خط اسرائیل و آمریکا است — عامل اجرایی است. آمریکا و اسرائیل که هر دو با دولت چپگرای سانچز مشکل دارند به مراکش گفته اند این وحوش و و طیور را بفرست سمت اسپانیا؛   حالا 2 حالت پیش می آید:  — یا دولت سانچز با بی…</div>
<div class="tg-footer">👁️ 4.35K · <a href="https://t.me/SBoxxx/19760" target="_blank">📅 00:53 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19759">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">فرانسه یک پیشنهاد  را به هند ارائه داده تا یک توافق دولتی-دولتی برای خرید ۱۱۴ فروند جنگنده "رافال" برای نیروی هوایی هند، به ارزش تقریبی ۳.۲۵ تریلیون روپیه (حدود ۳۴ تا ۳۹ میلیارد دلار) منعقد شود.
بر اساس این طرح پیشنهادی، حدود ۲۰ فروند از این هواپیماها مستقیماً از فرانسه به هند ارسال خواهند شد تا نیازهای فوری برطرف شوند، در حالی که ۹۴ فروند دیگر در هند تولید خواهند شد.
یکی از اولویت‌های اصلی هند، ادغام سلاح‌های تولید داخل، به ویژه موشک هوایی به هوایی "آسترا" است.</div>
<div class="tg-footer">👁️ 4.41K · <a href="https://t.me/SBoxxx/19759" target="_blank">📅 00:28 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19758">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">به گزارش بلومبرگ، یک مقام ارشد سعودی اعلام کرد که گزارش‌های اطلاعاتی معتبری وجود دارد که نشان می‌دهد حوثی‌ها، شبه‌نظامیان عراقی و سپاه پاسداران انقلاب اسلامی ایران در حال هماهنگی برای انجام حملات به عربستان سعودی هستند.
این منبع، این گزارش‌ها را "شگفت‌انگیز" توصیف کرد، زیرا این موضوع در حالی مطرح می‌شود که ریاض در تلاش برای کاهش تنش‌ها است و مدعی است که مذاکرات به طور مثبت پیش می‌رود.
این منبع همچنین افزود: "عربستان سعودی در اتخاذ تمام اقدامات لازم برای پاسخ به هرگونه تجاوز، تردید نخواهد کرد."</div>
<div class="tg-footer">👁️ 4.44K · <a href="https://t.me/SBoxxx/19758" target="_blank">📅 00:17 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19757">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">پس از خلع سلاح نیروهای وابسته به دولت اشغالگر ترکیه (انحلال سازمان تروریستی ارتش ملی سوریه)، اظهارات خشمگینانه ای از سوی «وزیر خارجه» ترکیه، هاکان فیدان (Hakan Fidan) صادر شد:   «کلیه عناصر مسلح در سوریه موظف به تحویل سلاحهای خود هستند.»</div>
<div class="tg-footer">👁️ 4.39K · <a href="https://t.me/SBoxxx/19757" target="_blank">📅 23:25 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19756">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">پس از خلع سلاح نیروهای وابسته به دولت اشغالگر ترکیه (انحلال سازمان تروریستی ارتش ملی سوریه)، اظهارات خشمگینانه ای از سوی «وزیر خارجه» ترکیه، هاکان فیدان (Hakan Fidan) صادر شد:
«کلیه عناصر مسلح در سوریه موظف به تحویل سلاحهای خود هستند.»</div>
<div class="tg-footer">👁️ 4.26K · <a href="https://t.me/SBoxxx/19756" target="_blank">📅 23:24 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19755">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">شنیده شدن انفجار در قشم و بندرعباس</div>
<div class="tg-footer">👁️ 4.33K · <a href="https://t.me/SBoxxx/19755" target="_blank">📅 23:18 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19754">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fkdAJh2gVlWVd_GsrGNnkFNxKEIt28ZXMlh6oYIlgXLGvJ1DgNhZV69EQKC24TmDGJXzN_5Jf5AIVHKZE9_1ty5r4nxpvETwPHw23ZxJOxBvaOW-dmaYztagPhsrRUY1PtV_YeJZp_djmNZ3liP8QC1E3C8QJgDhm0c0rpBvHIV9BYUqxad1j6bx1I-l1jvZ4L1zMtRNmb83Aqi_4E52_Fn-TsLOBLmnWuGxPeXX2NV4ZKXLlPkfdrdQD769w06v4FVpGlZwpAeuaSxeiOD-Q6mizfFt6k67k0BpnLmQnrZn7zlJyRvFI0qhgB5TH9D_7fM0GreSVLLsdcptWI8Lnw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خطر جنگ هسته ای؟!  ساعت نمادین روز رستاخیز بار دیگر به یک یادآور قدرتمند از خطرات رو به رشد برای جامعه بین‌المللی تبدیل شده است. در ارزیابی ابتدای سال ۲۰۲۶، مجله «بولتن دانشمندان اتمی» عقربه‌های این ساعت را به ۸۵ ثانیه قبل از نیمه‌شب (ساعت فاجعه) رساند که…</div>
<div class="tg-footer">👁️ 4.66K · <a href="https://t.me/SBoxxx/19754" target="_blank">📅 22:05 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19753">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">شنیده شدن انفجار در قشم و بندرعباس</div>
<div class="tg-footer">👁️ 4.29K · <a href="https://t.me/SBoxxx/19753" target="_blank">📅 21:58 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19752">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">منابع فلسطینی گزارش می‌دهند که حماس، واحدهای سازمانی، فعالیت‌های مخفیانه و عملیات امنیت سایبری خود را به ترکیه منتقل می‌کند، در حالی که قطر به میزبانی رهبری این سازمان و فعالیت‌های عمومی آن ادامه خواهد داد.  — روزنامه جروزالم پست</div>
<div class="tg-footer">👁️ 4.36K · <a href="https://t.me/SBoxxx/19752" target="_blank">📅 21:33 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19751">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">انصافاً ببینید کشورهای منطقه (خصوصاً عراق و کویت که راهی جز هرمز برای صادرات نفت ندارند) برای گریز از اخلال ایران در هرمز چه می کنند.  خط لوله کرکوک—جیحان که الان هم فعال است.  خط لوله شرق—غرب عربستان به ینبع برای خود سعودیها فعال است و گویا عراقی ها و کویتی…</div>
<div class="tg-footer">👁️ 4.31K · <a href="https://t.me/SBoxxx/19751" target="_blank">📅 21:24 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19750">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kIXIV2jdbqc2Qqkt2k-Ma0tzZupitjxE0MZdOIgT-cjUert1NNyyS8W6Clp02wMa3M7wXIIdmm7aroH2xb6D7f7KhoSyNYw6D6sekhyXE5OYvz-PiVZ9fmDmfy88xEEKGlIFyrMyU6mteBK03r-D-C2iIVv61krRF2NOJvXBOWUbvbGTJ-qRXZRMWbjxquCu7Y1WeLGY4XLxuVC1V0AQfE5EFO8Fk_Y-oj2Od60PeRUd59UV8NyPD6HB5WWNKMqE1DHPdlfzTmwkLMO12zN0hA_xUxR16GI7eiABzZ0Wh4AkNOl4Gw95Fo3hQGYykgZIm1OZkdmyxF2mVCLw7ZFdzg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ضرغامی:   مذاکرات مثل خوردن گوشت الاغ مرده در بیابان است!</div>
<div class="tg-footer">👁️ 4.29K · <a href="https://t.me/SBoxxx/19750" target="_blank">📅 20:46 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19749">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EaREQp55BmqiLM-fS8scNj9dYSURG65yl4nCH9aLPPev59681p6BBqlKryZgkDxazbKCo5KwaeYOjpZVEhBBJnhyfJZkB-7E9p_DYfbLKTCXrj6vQc2QNgJX9_gxnY-K51Xa3DpY3-44xhRoWhf_-XtMm3y5_JPypkC3dS_fOTr6GYVncb8V21K3PXDORE5fHVY7vklgVlWyxAE0yIt7vKRtlULjZ_lQHgy6mcB6xd5Y7nwnaLgodtsZ8UxMRdSrGj8eLtBFh_54hyrJCJh5mr-q02vlGuXRNIDcz254ULtRI5bfNNYAoZif_KKpS_9WCDn_jbTBgdQ-6xwLI-86ww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بعید میدانم ایران چنین طرحی را ارائه کرده باشد.</div>
<div class="tg-footer">👁️ 4.7K · <a href="https://t.me/SBoxxx/19749" target="_blank">📅 20:11 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19748">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WanzgP3bTnA5hVB2bClMghxOj-szFMn5eX6euKw99A0NR2ip2lrd7kwH3_SCcOKpYwVaY5-kON2UXG9Ly58PCuELmscbTUoJYAmNl3VssnuY-xCdBac9qHwKDw7tUwfPdn-rcgIxwTj3djO33s_exeMFkiFWDPnosXsx1rtr1XA2TN2CWGJLAgYXCswTfWO5UYf-Evrx4Dr0E3unqyf21yWJ10NxWGdxXq8sIlDLLlFndLxcbDSC4cbfueJf0-4Ih6XNb9IgvG0RdTh7dsLORud97kWYQmbhlUjf88dELPaXX9f4jLqrcljSWxY3V4wN99hD5Pi7UFn1s7l_nZkKug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">من نمیدانم این اظهارنظر منتسب به سردار وحیدی درست است یا نه اما اگر درست باشد اصلاً زمان مناسبی برای اذعان به داشتن سلاح هسته ای یا حرکت در این مسیر انتخاب نشده.</div>
<div class="tg-footer">👁️ 4.2K · <a href="https://t.me/SBoxxx/19748" target="_blank">📅 20:01 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19746">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/fXsfScFte6xVfi9mF18YwTwZSh7K5UTFhiWB44lchyE46aTYn7_aPqEUF33j08haa11-iOVtBYx4Z_w1CO8VU0sM96vBTU1otkYW7nhhgVJhawLxhm-4vOknQHyVj0Mq4hi2wVI5WtFqt5C-TqpODw0l5wy4kSfN4Ktu_MjF1x3OJKAEXRetjHgoPk3zUZPObdcLLU6Lu-aXY5W3-vebut-YkNj9wot6gl7dcwG5LQtynosXCT_3WrWEmVVz3fwjZ_YzsRfU-bOdbqL9_Z0a2B_BSiJwHZvGWFVy-aiTumnnQ2wXagMJVoJrDZDIyEk-7CNoSH94TDPAAkpcY8g3PQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/s6LhDpBALlpzIps4XCBygr8dXBgP8205lrqfOfiY0T5MKmAvTDh8OCwSNZUyrMlQRYNkwxx3dXU6NQ-3zhVT9l1V8XcRkaQyZiPoaFrjfNLGEXLbAUjHvXA1I3qbzVIzPWTO-HkDAQBQvHRorktwPgooJRXbGyV_4K4e2X9UHYjNKEpc9L5A-lpNFspONDudEh8M_j1tOvjg99a1efSYB_4Xd4vka72Kcnmlct_z80QUyfxo0LhW8SIHN41wmWSO4WfZWpIVTnNlcfkyV1GEYW9F86eK4Ztxhu3NRKbmVUx5RZ9QumE5z971s9i0uKnjJiBQF_P4ZYSy3HfsPRTJRw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">من نمیدانم این اظهارنظر منتسب به سردار وحیدی درست است یا نه اما اگر درست باشد اصلاً زمان مناسبی برای اذعان به داشتن سلاح هسته ای یا حرکت در این مسیر انتخاب نشده.</div>
<div class="tg-footer">👁️ 4.69K · <a href="https://t.me/SBoxxx/19746" target="_blank">📅 19:54 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19745">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/V960z_sy0uZzuUtyIAB2UaOP2kdKhX9yG1S-u7_flfbcMma4G3tBO1B5vEh39OL1F-F2IfKsWUA0WSYPYibb7p9M-NAUA0MityENPQb-dwq-kfg-pyphYuMiSMVYEEon6DVnRFPmFYbKXOPsoQc4JytjLr2K7elik0zJeU4syQW70TeWyyuezq1xOefHR6Dj0UKi2eO3Gkjuo97gFkutENH-PsLj1OqI8vpKQVAADY1l7d1TmsQLuMTy8Pw-jHdJJQH2xKwARrBI7O3fbmO2vsQMu9KdJ36PdLf71gMGmkHc4hfDZQfeRWXkeUwVugw_XP-LdPosOjIffDlSVr8aGw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#USOIL — H4  پوزیشن پیشنهادی.  ریوارد به ریسک خوبی دارد.</div>
<div class="tg-footer">👁️ 3.99K · <a href="https://t.me/SBoxxx/19745" target="_blank">📅 19:32 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19744">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">جزئیات متن اولیۀ طرح راهبردی مدیریت تنگه هرمز
🔹
سلیمی، عضو هیئت‌رئیسه مجلس: متن اولیۀ طرح «اقدام راهبردی تأمین امنیت و پیشرفت پایدار تنگۀ هرمز و خلیج‌فارس» در کمیسیون امنیت ملی در دست بررسی است.  براساس این طرح:
🔸
عبور شناورهای متعلق به آمریکا، رژیم صهیونیستی…</div>
<div class="tg-footer">👁️ 4.13K · <a href="https://t.me/SBoxxx/19744" target="_blank">📅 19:30 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19743">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">جزئیات متن اولیۀ طرح راهبردی مدیریت تنگه هرمز
🔹
سلیمی، عضو هیئت‌رئیسه مجلس: متن اولیۀ طرح «اقدام راهبردی تأمین امنیت و پیشرفت پایدار تنگۀ هرمز و خلیج‌فارس» در کمیسیون امنیت ملی در دست بررسی است.
براساس این طرح:
🔸
عبور شناورهای متعلق به آمریکا، رژیم صهیونیستی و سایر کشورهای متخاصم از تنگه هرمز ممنوع می‌شود.
🔸
محموله‌های مرتبط با رژیم صهیونیستی، اعم از نظامی و غیرنظامی، حق تردد از این منطقه را نخواهند داشت.
🔸
شناورها یا محموله‌هایی که در اقدامات علیه جبهه مقاومت نقش داشته باشند نیز مشمول ممنوعیت خواهند بود.
🔸
کشورها و اشخاصی که به ایران خسارت وارد کرده‌اند، تا زمان جبران خسارت، مجوز عبور از تنگه هرمز و خلیج فارس را دریافت نخواهند کرد.
🔸
برای قانون‌شکنان، جریمه‌های سنگین از جمله تا ۲۰ درصد ارزش محموله، پیش‌بینی شده است.
🔸
دولت موظف خواهد شد با همکاری نیروهای مسلح، مسئولیت‌هایی مانند هدایت ناوبری، نظارت بر تردد شناورها و حفاظت از امنیت و محیط زیست خلیج فارس را برعهده بگیرد.
🔹
این طرح همچنان در مرحله بررسی کارشناسی قرار دارد و مجلس از صاحب‌نظران خواسته پیشنهادهای خود را برای تکمیل آن ارائه کنند.</div>
<div class="tg-footer">👁️ 4.33K · <a href="https://t.me/SBoxxx/19743" target="_blank">📅 19:25 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19742">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">الفاتحه مع الصلوات</div>
<div class="tg-footer">👁️ 3.97K · <a href="https://t.me/SBoxxx/19742" target="_blank">📅 19:25 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19741">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">به جایی نخواهدرسید.</div>
<div class="tg-footer">👁️ 4.16K · <a href="https://t.me/SBoxxx/19741" target="_blank">📅 19:24 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19740">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ad5a791a91.mp4?token=MxTSy2FSSTZZiGBihP6_mSqm8NVmZ2-joysf7gYBTPfnditOQ_sKKERbijmDzWv64M3iy8VsQQpwYu1KUS1wBaaV1KuD93XHzIJHVCJbjiCHwlT2ygjuqxJqNhpgNS245HaNrV8LTzEj8jhaAw5izm6VP964umU055rcRZnz2SdvG6x4zsE9wLoQx4hE3qFZkxNlMKK-T2Wfy496doEn1IlXCdQgemFhCbArxxVbEhJGmBgCmm8A3434LozSWu3HQ3eGrqjbP17Dw1vkfIHHw4tJXTGUzFENUJ4V4QpFD_dZnd97zuNachpTduA10d-ErF5RTW3xlYuB48vivigOdg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ad5a791a91.mp4?token=MxTSy2FSSTZZiGBihP6_mSqm8NVmZ2-joysf7gYBTPfnditOQ_sKKERbijmDzWv64M3iy8VsQQpwYu1KUS1wBaaV1KuD93XHzIJHVCJbjiCHwlT2ygjuqxJqNhpgNS245HaNrV8LTzEj8jhaAw5izm6VP964umU055rcRZnz2SdvG6x4zsE9wLoQx4hE3qFZkxNlMKK-T2Wfy496doEn1IlXCdQgemFhCbArxxVbEhJGmBgCmm8A3434LozSWu3HQ3eGrqjbP17Dw1vkfIHHw4tJXTGUzFENUJ4V4QpFD_dZnd97zuNachpTduA10d-ErF5RTW3xlYuB48vivigOdg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">فقط ببینید و اگر وضویتان باطل نشد رییس جمهور را دعا کنید</div>
<div class="tg-footer">👁️ 4.64K · <a href="https://t.me/SBoxxx/19740" target="_blank">📅 18:57 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19739">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">‏
دستور الزیدی برای آماده‌باش نیروهای نظامی و امنیتی عراق
همزمان با نزدیک شدن به پایان ضرب‌الاجل مقاومت اسلامی عراق به دولت برای پاسخگویی به حمله آمریکایی‌سعودی علیه مقرهای الحشد الشعبی، دستگاه‌های امنیتی و نظامی عراقی به حالت آماده‌باش درآمده است.
‎</div>
<div class="tg-footer">👁️ 4.18K · <a href="https://t.me/SBoxxx/19739" target="_blank">📅 18:50 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19738">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">بیانیه صادر شده توسط نیروهای مسلح یمن
به نام خداوند بخشنده مهربان
خداوند متعال فرمود: {هیچ تجاوزی جز بر ستمگران نیست.}
دشمن جنایتکار سعودی در ادامه تجاوز و محاصره خود علیه مردم عزیز یمن ما که نزدیک به ۱۲ سال است ادامه دارد، شاهد تجمعات نظامی گسترده سعودی در مراحل پایانی خود بوده است که هدف آن تشدید درگیری علیه استان‌های آزاد شده و مردم یمن برای منصرف کردن آنها از موضع خود در مورد پایان دادن به محاصره ظالمانه است.
بنابراین:
نیروهای مسلح ما یک عملیات نظامی گسترده و دقیق را با هدف قرار دادن مراکز تجمع نیروهای دشمن سعودی در مناطق الرویک، العبر، الثانیه و سایر اردوگاه‌های متعلق به لشکرهای اضطراری اول و سوم، با استفاده از تعداد زیادی موشک بالستیک و پهپاد انجام دادند. این عملیات منجر به موارد زیر شد:
* کشته و زخمی شدن صدها مزدور دشمن سعودی.
* انهدام و آتش زدن تعداد زیادی از اردوگاه‌ها، مراکز تجمع نیروها، انبارها و تسلیحات دشمن سعودی در منطقه الوادیعه در شرق کشور.
* انهدام تعداد زیادی از خودروهای نظامی موجود در اردوگاه‌های هدف قرار گرفته.
نیروهای مسلح یمن به دشمن جنایتکار سعودی نسبت به هرگونه اقدام تجاوزکارانه علیه کشور و مردم ما هشدار می‌دهند و عواقب هرگونه تشدید اوضاع را متحمل خواهند شد. به گمراهان و فریب‌خوردگان در میان مردم خود توصیه می‌کنیم که اردوگاه‌های دشمن سعودی را ترک کرده و قبل از اینکه خیلی دیر شود به خانه‌های خود بازگردند.
به مردم عزیز یمن در تمام استان‌ها اطمینان می‌دهیم که نیروهای مسلح کاملاً آماده مقابله با هرگونه تشدید اوضاع هستند. از همه مردم خود می‌خواهیم که هوشیار باشند و با هرگونه تجاوز سعودی مقابله کنند و به مراکز تجمع نیروهای سعودی در هر کجا که باشند حمله کنند.
ما به استراتژی «محاصره در برابر محاصره» تا زمان رفع محاصره کشورمان ادامه خواهیم داد.
خدا ما را کافی است و او بهترین سرپرست، بهترین محافظ و بهترین یاور است.
زنده باد یمن آزاد، با عزت و مستقل!
پیروزی از آن یمن و همه آزادگان این ملت باد!
صنعا، ۲۳ صفر ۱۴۴۸ هجری قمری
صادر شده توسط نیروهای مسلح یمن</div>
<div class="tg-footer">👁️ 4.49K · <a href="https://t.me/SBoxxx/19738" target="_blank">📅 18:12 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19737">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-footer">👁️ 4.35K · <a href="https://t.me/SBoxxx/19737" target="_blank">📅 18:11 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19736">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">حملات سنگین اسرائیل به جنوب لبنان آغاز شد.</div>
<div class="tg-footer">👁️ 4.69K · <a href="https://t.me/SBoxxx/19736" target="_blank">📅 16:34 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19735">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">نیروهای انصارالله یک پایگاه نظامی متعلق به نیروهای "دفاع وطن" که به عربستان سعودی وفادار هستند، در منطقه "الودعیه" را مورد هدف قرار دادند که در اثر آن دستکم ۵۰ نفر کشته شدند.</div>
<div class="tg-footer">👁️ 4.63K · <a href="https://t.me/SBoxxx/19735" target="_blank">📅 16:08 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19734">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">اسرائیل و افسانه تجزیه ایران  در ایران امروز، مدتی است که افسانه‌پردازان، بی‌ وقفه تکرار می‌کنند که اسرائیل در اندیشه تجزیه ایران است. چگونه ممکن است کشوری با جمعیتی نزدیک به یک‌نهم ایران، مساحتی حدود یک‌هشتادم، در فاصله بیش از هزار کیلومتری هوایی و نزدیک…</div>
<div class="tg-footer">👁️ 4.74K · <a href="https://t.me/SBoxxx/19734" target="_blank">📅 13:53 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19733">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">اسرائیل و افسانه تجزیه ایران
در ایران امروز، مدتی است که افسانه‌پردازان، بی‌ وقفه تکرار می‌کنند که اسرائیل در اندیشه تجزیه ایران است.
چگونه ممکن است کشوری با جمعیتی نزدیک به یک‌نهم ایران، مساحتی حدود یک‌هشتادم، در فاصله بیش از هزار کیلومتری هوایی و نزدیک به سه هزار کیلومتری زمینی (آن هم با چند کشور مهم حائل بین راهی)  قادر باشد کشور ـ تمدنی چند هزار ساله را تجزیه کند؟
این در حالی است که موضع رسمی اسرائیل نیز چنین ادعایی را تایید نمی‌کند. بنیامین نتانیاهو در رویکرد علنی خود، از جمله در سال ۲۰۲۶، شایعات مربوط به تلاش اسرائیل برای تجزیه ایران را رد کرد. خوب یا شوم، رویکرد رسمی بی بی متوجه جمهوری اسلامی است، نه تقسیم ایران.
ولی اگر روزی همبستگی ملی ایرانیان چنان فرسوده شود که کشوری این چنین کوچک و غیرهمسایه بتواند سرنوشت ایران رقم بزند، دیگر  مساله، قدرت اسرائیل نیست؛ مساله، ضعف درونی ایران است. هیچ قدرت خارجی، حتی اگر ابرقدرت باشد، نمی‌تواند کشوری را تجزیه کند؛ مگر آنکه شکاف‌های داخلی، پیش‌تر پایه‌های آن را سست کرده باشد.
از همین رو، روایت «اسرائیل در پی تجزیه ایران است» بیش از آنکه یک تحلیل استراتژیک باشد، افسانه‌ای سیاسی است؛ افسانه‌ای که گاه برای بزرگنمایی تهدید بیرونی و به حاشیه راندن مسائل و کاستی‌های درونی ساخته و بازتولید می‌شود. تاریخ نیز یک درس روشن دارد: یکپارچگی سرزمینی و مردمان کشورها را پیش از هر چیز، همبستگی ملی، مشروعیت سیاسی، حکمرانی کارآمد و رضایت شهروندان حفظ می‌کند، نه صرفاً ترس از دشمن خارجی.
#یدالله_کریمی_پور
#karimipour_k</div>
<div class="tg-footer">👁️ 4.87K · <a href="https://t.me/SBoxxx/19733" target="_blank">📅 13:52 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19732">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">GeoMarkets - podcast 20</div>
  <div class="tg-doc-extra">Ali SharifAzadeh</div>
</div>
<a href="https://t.me/SBoxxx/19732" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">#پادکست_GeoMarkets
شماره — 20
پنجشنبه 6 آگوست 2026</div>
<div class="tg-footer">👁️ 4.66K · <a href="https://t.me/SBoxxx/19732" target="_blank">📅 13:42 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19731">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/r3-emg33Omz2Z08IGI-ZGzZEMRqR8Xj0xOsIcpPhacNIVKaWo18nNmTn65hefaF1uWHlVsJ-R1HMtq2TmbMAN32ci4MSdNMI48KuGLlTcEt2tn7xM7FxP1ks9dEN9Ru7ovYoUrMmTsZKrp7d9E1cqLmtArmW5HB2lXgp73cVA_JDgX5PLCvlEUqSF-ku-SSZAi6gPWArwrMuFJkmREJ0C_sUXIsxwKRuJuh9LYavwvukwhB9kngAnZRMjZSi-sqKa7LWdOZ28KdKWZHCSwKGgfMNaAXWKmXJVCuwejr3dNhh80VcecGG1ndjNnCokNMFWfpeshQvihw2-PabYY9tVQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این تحلیل درست 4 روز پس از پایان جنگ 40-روزه ارائه شد و همچنان بر اعتبار آن افزوده می شود و خواهیم دید روزی می رسد که تنگه هرمز را فقط خودمان استفاده خواهیم کرد.  از همه کریدورها که محروم ماندیم و سهممان .... های باقر شد این هم از تنگه هرمز!</div>
<div class="tg-footer">👁️ 5.43K · <a href="https://t.me/SBoxxx/19731" target="_blank">📅 12:46 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19730">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lbieQjHwPFLlBeiZrXPxA-vED3XbV8cS2NndAQhjo-TSPiaUd0nqOWRoYHVTYIi0heHsWtE7P28PG3TASJC9W5kM-B9zvwNsJVtiTpMV0lW61-ViKrXwdx5dsmYxZkP4_t-NYZvzJ3TJJuRDMXtUQo-WIOIciKSU95d8-PRWTWzo3ip6i6nXFtEEVrVvtalcELA2vGu94NJMY_jppQE2kshLXCoajrbEACLSN0xG3CF2cNa00jfOUtAzDiAwQ8Y0CBY5WZ-eHQhNwdHxPe0jw8KmFqbm-gfq5AweNFAWPG0YNoH7yfumxMxUhL_JuDVdhYytzXzngbefsE6kwhSTuQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">گفته می شود با دیدن این عکس، ترامپ از نابودی زیرساخت های ایران صرف نظر کرده است.</div>
<div class="tg-footer">👁️ 4.79K · <a href="https://t.me/SBoxxx/19730" target="_blank">📅 12:40 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19729">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/THxZiaEkoRf9ya-PankOmLrzR_v60IiGR2u3ud4Yols7pO6IO_5aOszpBojHcb1-CdUlKQVd1hJR4AKMMK45hc0csw5hEQg2l-l5ga1fAVIviC0nVGxTa476hKEMjXGFvdxtNFu4kTbtH1XpFZ8WOKM8c78XtI5V35z4HxPrmokNA5czXg8jPFWgwlzpABwjgRY4Y90tiTdm-kLtuW2mVTb0Qj7tJypf7SBOHx1OsFIKcixUGMAwcI6mKbqfmPKrSd0vT55m7TipMydic1npTKQ5h6ENOw2IbXcSdLbspRj1vQ_j1vNCESrcyWEqMUlj0M06H718VoUfKTPA3NYLwQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#GRI
برای امروز شاخص ریسک ژئوپولیتیک در سطح میانه قرار دارد. پیش بینی می شود طلا امروز مقداری افت اصلاحی داشته باشد (با توجه به رشد GRI از دیروز) اما دوباره به سقف (4300) حمله ور بشود (با توجه به افت میانگین شاخص GRI در روزهای گذشته)</div>
<div class="tg-footer">👁️ 4.55K · <a href="https://t.me/SBoxxx/19729" target="_blank">📅 11:14 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19728">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">سبحان الله!  هندی ها حتی در باشگاه های بدنسازی شان هم ممکن است غرق بشوند!  (ماشالله چه بدن هایی هم ساخته اند در باشگاه)</div>
<div class="tg-footer">👁️ 4.71K · <a href="https://t.me/SBoxxx/19728" target="_blank">📅 10:27 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19727">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e2d8645934.mp4?token=ahAnqPh6gUk4me6l5IlE9KOZkG6-Phk6A_dfGRcH1Sj9tceXKkTAHIeLI9b4riMiBdsRBvJPeGHrTITjFSK6xraJ0r4twRr-ZropqZmRelqR7TEZxqNiqfuPDGsBru7yXN9zLmTaFslEkBUVJVbPFz-lVZfgQSbFn0i1MyqoYpffAXubbZuC-1W513sZb6L9FGaTRf3QqV2uPrP5lJU7JakC_Ns31qkEyctSkUduWJJziOOEpvx30_CpO0jFBFIvmuGAAYCgO74F5zflY2xfsQjI1z6u57zhoriUbSZjFiYsNiS542NA58wT_mU5_orFZgJPhgcC32Pb0Dvv75qmxA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e2d8645934.mp4?token=ahAnqPh6gUk4me6l5IlE9KOZkG6-Phk6A_dfGRcH1Sj9tceXKkTAHIeLI9b4riMiBdsRBvJPeGHrTITjFSK6xraJ0r4twRr-ZropqZmRelqR7TEZxqNiqfuPDGsBru7yXN9zLmTaFslEkBUVJVbPFz-lVZfgQSbFn0i1MyqoYpffAXubbZuC-1W513sZb6L9FGaTRf3QqV2uPrP5lJU7JakC_Ns31qkEyctSkUduWJJziOOEpvx30_CpO0jFBFIvmuGAAYCgO74F5zflY2xfsQjI1z6u57zhoriUbSZjFiYsNiS542NA58wT_mU5_orFZgJPhgcC32Pb0Dvv75qmxA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">این جنگ تمام هم که بشود باز هندی ها غرق خواهندشد.</div>
<div class="tg-footer">👁️ 5.02K · <a href="https://t.me/SBoxxx/19727" target="_blank">📅 10:20 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19726">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">سازمان عملیات تجارت دریایی بریتانیا:
ما گزارشی از حادثه‌ای در ۹ مایل دریایی جنوب شرقی کومزار در عمان دریافت کرده‌ایم.</div>
<div class="tg-footer">👁️ 4.92K · <a href="https://t.me/SBoxxx/19726" target="_blank">📅 04:03 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19725">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">ترامپ در مورد ایران:  ایران به ما احترام می‌گذارد. آن‌ها به ما احترام می‌گذارند.  ما در حال صحبت هستیم. ببینیم چه اتفاقی می‌افتد.</div>
<div class="tg-footer">👁️ 5.01K · <a href="https://t.me/SBoxxx/19725" target="_blank">📅 01:21 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19724">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">ترامپ در مورد ایران:
ایران به ما احترام می‌گذارد. آن‌ها به ما احترام می‌گذارند.
ما در حال صحبت هستیم. ببینیم چه اتفاقی می‌افتد.</div>
<div class="tg-footer">👁️ 5.03K · <a href="https://t.me/SBoxxx/19724" target="_blank">📅 01:20 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19723">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FPZx5aEdB4DlG_NBMhoxLv4PPZH1BEU0x0b0Ai9cU68FiETPDuxo75tpiCwrbgNyS5Df81J6sCiBAwgjaAyi9dGVypDE-Nojz_E2mzw6_-07aeIDQ4qZ26jkanWl2XsRjHKxXqq4--eRGzL_LY8jyxm1MUXvn9l_a3TEMN-TLH9CYRaJB1itgny9-g9EUyxEO5iSrS463K4IbHFa5lG33cslw79Uk0wBHkmhrDXqJbm90RchrsXQFbvpwqyzOfjaWMsDuU8MMcDHoJeOqspjF6LA_9dx7nzveCurhawSd8hrzTOj3vwdyYsqVbd_PETVbYWXqk6mrmKEFoQQKqmEBg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#XAUUSD
— H4
میتوان چنین ساختاری برای طلا متصور بود.</div>
<div class="tg-footer">👁️ 5.3K · <a href="https://t.me/SBoxxx/19723" target="_blank">📅 23:36 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19722">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cefwWMgjmuxktFpWo34dvGCsdyISEt7lESsJCE12dxDAXWApOSXROoTAnAXTWxcau3oa1foetMhOw9-DBS71WoLd0O74AUc55lbVhbhIA44fGpAavvDpc6EgcGaDtlGquRCjw5rmrbCBaXGKb5caTI5a7RyKD1rYVtu0JUjTNBGt_a8Qpi7Fut2H9eWg9Oh3sIpxFVkY0O-QoD9zcl7BWd8ODWGHILGQd3N1OEB0E62YFlgv9qU6NOhOOZwrB6W8WH8IRlz5WHHb67yA-3d5qOvWl5icRw83pJjIJE78fnItvZye_M3DP78l2N1MZ-84mtdH4AaKJWreCJP6JkCvZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#GRI  شاخص ریسک ژئوپولیتیک امروز در سطح پایینی قرار دارد و ادامه جو ریسک پذیری پیش بینی می کند.  (شخصاً با توجه به اینکه:  — عمده رشد امروز در سشن آسیا روی داده — پس فردا گزارش NFP داریم — اعتمادی به توافق ایران و آمریکا ندارم  اینجا خریدار نیستم و پله ای…</div>
<div class="tg-footer">👁️ 4.94K · <a href="https://t.me/SBoxxx/19722" target="_blank">📅 22:55 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19721">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">رئیس‌جمهور ایران، مسعود پز‌شکیان:  هر چقدر هم که فکر می‌کنم، نمی‌توانم هیچ دلیل منطقی پیدا کنم که چرا آن‌ها رهبر، فرماندهان و دانشمندان ما را به قتل رساندند.  بسیاری از فرماندهان و دانشمندانی که به قتل رسیدند، حتی صاحب خانه هم نبودند.</div>
<div class="tg-footer">👁️ 4.81K · <a href="https://t.me/SBoxxx/19721" target="_blank">📅 22:53 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19720">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">رئیس‌جمهور ایران، مسعود پز‌شکیان:
هر چقدر هم که فکر می‌کنم، نمی‌توانم هیچ دلیل منطقی پیدا کنم که چرا آن‌ها رهبر، فرماندهان و دانشمندان ما را به قتل رساندند.
بسیاری از فرماندهان و دانشمندانی که به قتل رسیدند، حتی صاحب خانه هم نبودند.</div>
<div class="tg-footer">👁️ 4.84K · <a href="https://t.me/SBoxxx/19720" target="_blank">📅 22:44 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19719">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RiOM0ayMWyoZqGlTieAdzYrbo3S9OfsRHA3IcOwNrSh9DMMXx7tatwHUYAG8t07Dju9nWmxFUJDkcZrxLt5pNJakQf06aJOhTIWqHC57tE_z56yo7lm7a9xE22tP44shjk3OVozRZcocg3BV7pWXwbeStki_IXHiGJoaplDWRhcf_ev1PcSHsNEPkF8cyDII_b5002-avwWulF6JSxe_UvnhycYoWvBp1zOYkppe8tDr5C9j0XUFQSTVDEcQjKjM2F4-DC5Vyw6V5WpNQUXg6PD920qLeeSgm_z-OidUQv6NfESMGJtZIyxUWtjj28ygThItrauVwfXV9NcaTuxnhQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#USOIL — H2  محسن رضایی: منتظر نفت ۱۵۰ دلاری طی روزهای آینده باشید.</div>
<div class="tg-footer">👁️ 4.85K · <a href="https://t.me/SBoxxx/19719" target="_blank">📅 21:50 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19718">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">روسیه به طور فزاینده‌ای از موشک‌های پدافند هوایی S-300/S-400 در نقش‌های حمله زمینی استفاده می‌کند که تهدیدات شبه بالستیک سریعی را ایجاد می‌کند که رهگیری آن‌ها دشوار است.
طبق اطلاعات استخباراتی اوکراین ذکر شده در تحلیل، روسیه حدود 200 موشک RM-48U تبدیل‌شده را در سال 2025 تولید کرده و قصد دارد بیش از 480 موشک را در سال 2026 تولید کند.
این موشک‌ها دقت کمتری نسبت به اسکندر دارند اما تعداد اهداف پرسرعتی را که اوکراین باید در برابر آن‌ها دفاع کند، افزایش می‌دهند.</div>
<div class="tg-footer">👁️ 4.71K · <a href="https://t.me/SBoxxx/19718" target="_blank">📅 21:40 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19717">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">غریب‌آبادی:   موضوع دریافت هزینه توسط ایران در تنگه هرمز بستگی به تصمیم مقامات عالی نظام و رفتار آمریکا دارد.</div>
<div class="tg-footer">👁️ 4.7K · <a href="https://t.me/SBoxxx/19717" target="_blank">📅 21:28 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19716">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">غریب‌آبادی:
موضوع دریافت هزینه توسط ایران در تنگه هرمز بستگی به تصمیم مقامات عالی نظام و رفتار آمریکا دارد.</div>
<div class="tg-footer">👁️ 4.69K · <a href="https://t.me/SBoxxx/19716" target="_blank">📅 21:27 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19715">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">فوری | معاون وزیر امور خارجه ایران: پیام‌هایی از ایالات متحده دریافت کرده‌ایم که نشان می‌دهد این کشور آماده است تا به تعهدات خود بازگردد.</div>
<div class="tg-footer">👁️ 4.74K · <a href="https://t.me/SBoxxx/19715" target="_blank">📅 21:27 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19714">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">فوری | معاون وزیر امور خارجه ایران: پیام‌هایی از ایالات متحده دریافت کرده‌ایم که نشان می‌دهد این کشور آماده است تا به تعهدات خود بازگردد.</div>
<div class="tg-footer">👁️ 4.8K · <a href="https://t.me/SBoxxx/19714" target="_blank">📅 21:21 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19713">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">رائفی‌پور:   ایران به اردن حمله کرد و ۶ جنگنده اف ۳۵ را نابود کرد چون قرار بود به مراسم اربعین و مواکب حمله کنند</div>
<div class="tg-footer">👁️ 4.8K · <a href="https://t.me/SBoxxx/19713" target="_blank">📅 20:08 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19712">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">رائفی‌پور:
ایران به اردن حمله کرد و ۶ جنگنده اف ۳۵ را نابود کرد چون قرار بود به مراسم اربعین و مواکب حمله کنند</div>
<div class="tg-footer">👁️ 4.74K · <a href="https://t.me/SBoxxx/19712" target="_blank">📅 20:08 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19711">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">منابع عربی گزارش حمله موشکی به بحرین را منتشر کردند - خبرگزاری مهر.</div>
<div class="tg-footer">👁️ 4.65K · <a href="https://t.me/SBoxxx/19711" target="_blank">📅 19:29 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19710">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">منابع عربی گزارش حمله موشکی به بحرین را منتشر کردند - خبرگزاری مهر.</div>
<div class="tg-footer">👁️ 4.72K · <a href="https://t.me/SBoxxx/19710" target="_blank">📅 19:20 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19709">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">این تحلیل درست 4 روز پس از پایان جنگ 40-روزه ارائه شد و همچنان بر اعتبار آن افزوده می شود و خواهیم دید روزی می رسد که تنگه هرمز را فقط خودمان استفاده خواهیم کرد.  از همه کریدورها که محروم ماندیم و سهممان .... های باقر شد این هم از تنگه هرمز!</div>
<div class="tg-footer">👁️ 4.61K · <a href="https://t.me/SBoxxx/19709" target="_blank">📅 19:06 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19708">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ib-IOAfi9lQT4zsx28IHq37AQ6boeIimyZ7ihxfWek5Kyvs416cjCGiwuiZHEDmWVNEtIVvOgjNwEM5OjqOJzUoscGD8nN9FMIjNQmDS1Vf9fnWy6bFaZHolcAz4ziqSuPewlkCPP1n_Z03gqZhC1sBbX8AQXniybCCyqWClDUsSd-xOl4Y0jwfpZ-5z-hO8Gb8tlilB4yIs46MoemMRkQTA-s9AMlQGgeoAXXpr8nsWxic-TKN3hdk4yO24EToX8YiMqE8SW0ctOUnvdyouEsAbPOcRiUdYjbEjKni7sQAVTc7CwteE6XwpxaOpn1Gduu1JY7r6mhiZ3jTaIvFc1A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
طرح جدید اسراییل برای ساخت
پایگاه‌های نظامی در جنوب لبنان
روزنامه هاآرتص گزارش داد که رژیم صهیونیستی حدود ۲۳۰ کیلومتر مربع از خاک لبنان را همچنان در اشغال دارد و قصد دارد بر روی ویرانه‌های روستاهای تخریب‌شده، پایگاه‌های نظامی جدید احداث کند.</div>
<div class="tg-footer">👁️ 4.64K · <a href="https://t.me/SBoxxx/19708" target="_blank">📅 18:47 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19707">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">GeoMarkets Podcast Text.pdf</div>
<div class="tg-footer">👁️ 4.36K · <a href="https://t.me/SBoxxx/19707" target="_blank">📅 18:22 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19706">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">طبق وب‌سایت وزارت خزانه‌داری ایالات متحده، ایالات متحده تحریم‌های مرتبط با ایران را لغو کرده است.  منبع: رویترز</div>
<div class="tg-footer">👁️ 4.47K · <a href="https://t.me/SBoxxx/19706" target="_blank">📅 18:16 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19705">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">فوری | یک مقام ارشد ایرانی به الجزیره گفت: هرگونه بستن یا باز کردن تنگه هرمز به اقدامات واشنگتن بستگی دارد.</div>
<div class="tg-footer">👁️ 4.45K · <a href="https://t.me/SBoxxx/19705" target="_blank">📅 18:13 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19704">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">طبق وب‌سایت وزارت خزانه‌داری ایالات متحده، ایالات متحده تحریم‌های مرتبط با ایران را لغو کرده است.
منبع: رویترز</div>
<div class="tg-footer">👁️ 4.58K · <a href="https://t.me/SBoxxx/19704" target="_blank">📅 17:46 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19703">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">منابع فلسطینی گزارش می‌دهند که حماس، واحدهای سازمانی، فعالیت‌های مخفیانه و عملیات امنیت سایبری خود را به ترکیه منتقل می‌کند، در حالی که قطر به میزبانی رهبری این سازمان و فعالیت‌های عمومی آن ادامه خواهد داد.
— روزنامه جروزالم پست</div>
<div class="tg-footer">👁️ 4.4K · <a href="https://t.me/SBoxxx/19703" target="_blank">📅 17:42 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19702">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">پیش‌نویس قانون ترکیه برای حمایت از خلع سلاح و بازگشت به زندگی عادی اعضای سازمان پ.ک.ک
ائتلاف حاکم ترکیه، روز چهارشنبه، یک پیش‌نویس قانون را به پارلمان ارائه کرد که هدف آن پیشبرد روند صلح با حزب کارگران کردستان (پ.ک.ک.) است. این قانون شامل حمایت‌های قانونی برای بسیاری از اعضای سابق این سازمان و تعلیق مجازات‌های زندان برای برخی از افرادی است که به عضویت در پ.ک.ک. متهم شده‌اند.
این قانون‌گذاری، که انتظار می‌رود در اواخر این هفته توسط پارلمان تصویب شود، به دنبال پایان دادن به درگیری‌های دهه‌ها طولانی با تسهیل بازگشت هزاران نفر از اعضای سابق پ.ک.ک. است که در حال حاضر در شمال عراق مستقر هستند.
بر اساس این قانون پیشنهادی، سازمان اطلاعاتی MIT ترکیه مسئول بررسی و تأیید خلع سلاح این گروه خواهد بود، در حالی که یک کمیته متشکل از معاون رئیس‌جمهور، چندین وزیر و رئیس MIT، بر روند تسلیم و تحویل سلاح‌ها نظارت خواهد کرد.</div>
<div class="tg-footer">👁️ 4.31K · <a href="https://t.me/SBoxxx/19702" target="_blank">📅 16:50 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19701">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">مقامات آمریکایی تأیید کردند که هرگونه توافق احتمالی با ایران، به طور قطعی تضمین خواهد کرد که تهران کنترل مسیر کشتیرانی تنگه هرمز را به دست نخواهد گرفت.</div>
<div class="tg-footer">👁️ 4.05K · <a href="https://t.me/SBoxxx/19701" target="_blank">📅 16:49 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19700">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">کونستانتینوس فلوروس، رئیس ستاد سابق ارتش یونان:  هر کسی که پا به خاک یونان بگذارد، ابتدا سوزانده خواهد شد، و سپس ما از او می‌پرسیم که کیست.  این تنها واکنش مناسب به تهدیداتی مانند: "ما یک شب سر می‌رسیم" یا "ما به جزایر شما قدم خواهیم گذاشت" است.  منبع: Proto…</div>
<div class="tg-footer">👁️ 4.17K · <a href="https://t.me/SBoxxx/19700" target="_blank">📅 16:47 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19699">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nHZUTtE5ALKnSfS1c19MtkQSLhZtlZlq-UJozCSXf2Mny_XsoU8G1uKJ5qnNVfX17zE_3xOY7nE1pFJkcyJDYOCkc9o8gNJMBrcrD_0l2EcV7dqRQ9InS9cBVNwmHlq-UJW1oF03MCKYTNOa5MZOWStBw3xWDJrRjuyS7xjgZPNNdc0B1lCi7VSCUWjU1ZZFKUykH1dTcIF9ewaTTa-_q8ox6KE07l0aq0C0JugpjbGwCuB6J9O9pcdSPFqPrAq1SdjTuxdadKYCyjAHKPlz3nBeR331R2e98NzK046172_JFs8GfDBk16HPaK9RPZRhRtpxUQf_dI4wC9190ynIPg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تنش‌های میان ترکیه با یونان دارد دوباره داغ می شود….</div>
<div class="tg-footer">👁️ 4.15K · <a href="https://t.me/SBoxxx/19699" target="_blank">📅 16:42 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19698">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oO-WVF5y1khJPzlObgos6m4HR4CxAuJrfP0sDnvLwJEjU5Nom6hzQHS_ruZw5mHmodAhr4zNt5nawmb86hCH9FxOI1WmUCwQgOLqAS3YzbOCmHfkjS6-qsCcdOCN8SL95Y_sheXANCTI4bjEmM5mGozcHLbX7-Y1L39JzVbgb0H_L-E_vtgbWA5fMC-H11zoSAZgpIhpkvP3kFmo4Z_n4Su8ugnqK4Ey7LMAaSVsdX1WlZb34gPJ3kCOWqMCT2rckkRIxtFd8uc_1IM6lQnHOrnyg-bP0Sd3kLU1Em8T9rlSz7zIgMiX9Z4T5n9K2LvLewuHL5SUq5a9_H2tMMA4Sw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این فیلم را ببینید!  در حالی که همه هنرمندان و تماشاگران (از جمله بهروز وثوقی افسانه ای) به صورت ایستاده سرود میهنی «ای ایران» را همخوانی می‌کنند، «نون میم» با آن چهره و ریخت هیستریک ش  مثل بزهای کوهی به در و دیوار خیره شده و گویی در سالن تئاتر دنبال یونجه…</div>
<div class="tg-footer">👁️ 3.94K · <a href="https://t.me/SBoxxx/19698" target="_blank">📅 16:37 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19697">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">یک مقام ارشد خلیج فارس گفت که احتمال اینکه آمریکا و ایران تا روز جمعه به یک توافق موقت برسند، ۵۰ درصد است، اگرچه هنوز گروه‌های تندرو کلیدی ایران موافقت خود را اعلام نکرده‌اند.
— سی‌ان‌ان</div>
<div class="tg-footer">👁️ 3.87K · <a href="https://t.me/SBoxxx/19697" target="_blank">📅 16:34 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19696">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">یک جا آرام می شود، 13 جای دیگر جنگ می شود</div>
<div class="tg-footer">👁️ 4.14K · <a href="https://t.me/SBoxxx/19696" target="_blank">📅 16:32 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19695">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">شب های خواهرمیانه !</div>
<div class="tg-footer">👁️ 4.3K · <a href="https://t.me/SBoxxx/19695" target="_blank">📅 16:31 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19694">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">نیروهای دفاعی اسرائیل (IDF) یک هشدار "فوری" برای تخلیه ساکنان روستای المنصوری در جنوب لبنان صادر کرده است، این اقدام قبل از حملات هوایی انجام شده است.
ارتش اسرائیل:
«حزب‌الله توافق آتش‌بس را نقض کرده است و ارتش با قاطعیت علیه آن اقدام خواهد کرد.»</div>
<div class="tg-footer">👁️ 4.35K · <a href="https://t.me/SBoxxx/19694" target="_blank">📅 16:30 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19693">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">ارتش اسرائیل برای حمله ای سنگین به جنوب لبنان آماده می شود.</div>
<div class="tg-footer">👁️ 4.3K · <a href="https://t.me/SBoxxx/19693" target="_blank">📅 16:28 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19692">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">حادثه دریایی جدید در دریای سرخ</div>
<div class="tg-footer">👁️ 4.28K · <a href="https://t.me/SBoxxx/19692" target="_blank">📅 15:50 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19691">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">GeoMarkets Podcast Text.pdf</div>
  <div class="tg-doc-extra">422.9 KB</div>
</div>
<a href="https://t.me/SBoxxx/19691" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">Ali SharifAzadeh – GeoMarkets - podcast 19</div>
<div class="tg-footer">👁️ 4.28K · <a href="https://t.me/SBoxxx/19691" target="_blank">📅 15:47 · 14 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>

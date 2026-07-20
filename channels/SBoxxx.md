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
<img src="https://cdn4.telesco.pe/file/PajIn8sC6ncbg1xm2Er28zDoS-__FbOzQTxhRVE5yY4h_Vp2UKsfUfF5hsplu-4ZEfUxFVk4otLbD9onAqSMWpFzNwKqJ_Fx7befK_lqKZEfy48x1hAybN6OG7n85KvM-iia6rxuPoFyUZ1jsrc23ODJwdgfJU0tnpeUYqVIF2mhwokflMfIMZeRMaFhdBPcZpW-rL0PyDb-YcenxJeMrtXs9sm_jzU-9XdbRGHnnH7NaRpoAM5idjn7HE7wXB-lsPL0IATC9UDLcf_ARg8oqp4zvnKZCdRSOtUS5TCF7mM05Bt1GQ3e7v_SfH-kaZyOUTBXcaLYYCoQOgyPAmcuSg.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Secret Box</h1>
<p>@SBoxxx • 👥 10.4K عضو</p>
<a href="https://t.me/SBoxxx" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 تاریخ، ژئوپولیتیک و بازارهای مالیhttps://secretboxxx.com/</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-29 04:30:39</div>
<hr>

<div class="tg-post" id="msg-18991">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">صدای انفجار در چابهار و تبریز !</div>
<div class="tg-footer">👁️ 300 · <a href="https://t.me/SBoxxx/18991" target="_blank">📅 04:05 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18990">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">ترامپ:
ایران از نظر نظامی تقریباً همه چیزش را از دست داده؛ فقط تعداد کمی موشک، پهپاد و توان تولید برایش باقی مانده، ما تنگه را کنترل می‌کنیم و ایران هیچ کنترلی روی اوضاع ندارد</div>
<div class="tg-footer">👁️ 335 · <a href="https://t.me/SBoxxx/18990" target="_blank">📅 04:03 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18989">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">کویت اعلام کرد که سامانه‌های دفاع هوایی آن پهپادهای ایرانی را رهگیری می‌کنند.</div>
<div class="tg-footer">👁️ 1.85K · <a href="https://t.me/SBoxxx/18989" target="_blank">📅 02:00 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18988">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">تا لحظاتی دیگر پخش زنده بازی تیم های  ملی New Castle و سوییس از شبکه نسیم</div>
<div class="tg-footer">👁️ 2.22K · <a href="https://t.me/SBoxxx/18988" target="_blank">📅 01:49 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18987">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TntblWapN6YB7jTjjWvMRey7Y2zzvVpa6DtK0Ul-p4atlcEj7zOceyRi-QcszK9wg91yiq61_H8B5CO2j3DajY0cuT369P24oCpYi1xZW-Ik7J5mr2ENr9f-xstFy_DhrPKf04sDEoVW-sJPI4Zfjz3ESgHGcF6hkwKr-HbV52WV_xmN8uJ-w_4CFtVpJIhopZg3b2CXUinz4mLEZsU9g1VHPYOMaV0lna282V5Z_5EWO8xcfu7FqYS7qrM9rZqp_w33ZkD4OlO1xYvAEJTdrc2shuIj8pdv4LuvU_Ujd_FDD5a4iU63cdwowjwuTuEr9yKXqVs8cdw8MxMUyDIk6A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عاقبت پرورش غیرمجاز دام و طیور در حمام</div>
<div class="tg-footer">👁️ 2.52K · <a href="https://t.me/SBoxxx/18987" target="_blank">📅 01:44 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18986">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">پمپئو: فشار اقتصادی خفه‌کننده به ایران را ادامه دهید تا اعتراضات داخلی در آنجا رخ بدهد!
وزیر خارجه دولت اول ترامپ:
واقعیت امروز این است که به‌زودی آن محاصره‌ای که سنتکام با کارآمدی بسیار برقرار کرده و همچنین تلاش برای کاهش توانایی آن‌ها در آسیب رساندن به کشتی‌هایی که از تنگه عبور می‌کنند اهرم فشار ایران را کاهش می‌دهد و در نهایت آن‌ها دیگر قادر به پرداخت حقوق نخواهند بود.
حماس، حزب‌ الله و حوثی‌ های یمن، آن‌ها نیز دیگر قادر به پرداخت حقوق نخواهند بود و پول لازم برای خرید مهمات را از دست خواهند داد. و زمانی که این اتفاق بیفتد، مردم ایران فرصتی را به دست خواهند آورد. این مسیر پیش روست. فشار اقتصادی خفه‌کننده، قدرت نظامی و صبر دیپلماتیک، به نتیجه‌ای مطلوب برای رئیس‌جمهور ترامپ و جهان منجر خواهد شد.</div>
<div class="tg-footer">👁️ 2.81K · <a href="https://t.me/SBoxxx/18986" target="_blank">📅 01:21 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18985">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">کشتی باری ترکیه‌ای گلدن لیو در اودسا هدف حمله قرار گرفت  کشتی باری گلدن لیو که پرچم گینه بیسائو را دارد و متعلق به یک شرکت ترکیه‌ای است، هنگام خروج از منطقه درگیری با محموله‌ای از غلات، توسط سه موشک کروز خ-۵۹/خ-۶۹ هدف قرار گرفت. این کشتی بخشی از «ناوگان سایه»…</div>
<div class="tg-footer">👁️ 3.5K · <a href="https://t.me/SBoxxx/18985" target="_blank">📅 00:21 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18984">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">ترکیه سیستم پدافند هوایی S-400 خود را به یک کشور خلیج فارس – احتمالاً امارات متحده عربی یا قطر – فروخته است.  جزئیات نهایی شب گذشته نهایی شد و انتظار می‌رود امروز یک اطلاعیه رسمی منتشر شود.  منبع: عبدالکادیر سلوی، روزنامه‌نگار ترکیه‌ای (روزنامه حریت)</div>
<div class="tg-footer">👁️ 3.57K · <a href="https://t.me/SBoxxx/18984" target="_blank">📅 00:17 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18983">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromپیکنیک تحلیل</strong></div>
<div class="tg-text">پناهیان:
اگه بی‌برقی و بی‌آبی رو تحمل کنید،
جهان رو آزاد می‌کنیم و آنها را هم بدون آب و برق خواهیم کرد.
@PiknikAnalyst</div>
<div class="tg-footer">👁️ 2.95K · <a href="https://t.me/SBoxxx/18983" target="_blank">📅 00:08 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18982">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">سنتکام:
یک عضو خدمه ایالات متحده در ۱۸ جولای در شمال عراق در عملیات کشته شد</div>
<div class="tg-footer">👁️ 3.98K · <a href="https://t.me/SBoxxx/18982" target="_blank">📅 22:52 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18981">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZHOSGhwz9-FeKL5DuZ3w6Pq9FmRPwixKYzvd3oKu1SX0Hi_ZudsgLEqe1_gmf5f8f6PtTXOS8PNjxbg_T7LWeYft9Cp-nfyHg_GYA1n7-p7hu_W8uq5szaAWgxqexVSKr-2Va-zTXW0DI5NfPjUMVklLt3Dc6Q4PvJAjHQf8wfJOBcKPMPq0aRe3xrjos6pU07WBmA0_nqfunsdpreOR8nBOKxmp98QPC_mcYMyc5ebaCkKaE-PEYq7rDzMnIs3c_Euw_4VOsFZMwLoN1IkNvYb10PG37i1LbMnmUW_sAZpXiI0063x8CGNBeZBg0TDD52r-LP8GIrZHTmK5qL-N-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اسپید معروف امشب موقع اجرا واسه فینال جام جهانی، رویِ لباس خودش فروهر نماد ایران باستان و آیین زرتشتی داشت.</div>
<div class="tg-footer">👁️ 4.12K · <a href="https://t.me/SBoxxx/18981" target="_blank">📅 22:51 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18980">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">کانال ۱۴ اسرائیل: ممکن است آمریکا از اسرائیل بخواهد به کارزار نظامی بپیوندد
برآورد اسرائیل این است که ایران طی روزهای اخیر در حال بررسی و بحث درباره این موضوع بوده که آیا به اسرائیل حمله کند یا نه، اما تاکنون هیچ تصمیمی در این‌باره گرفته نشده است.
ارزیابی دیگری نیز حاکی از آن است که ممکن است آمریکا از اسرائیل بخواهد حتی در صورت عدم حمله ایران، به کارزار نظامی بپیوندد.</div>
<div class="tg-footer">👁️ 4.3K · <a href="https://t.me/SBoxxx/18980" target="_blank">📅 21:32 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18979">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">مقامات ارشد اسرائیلی به سازمان پخش اسرائیل گفتند:  «ترکیه تهدید کرده است که در صورت عبور نیروهای کرد از خاک ایران به عنوان بخشی از عملیات زمینی به رهبری موساد با هدف سرنگونی رژیم، از ایران پشتیبانی هوایی خواهد کرد.»</div>
<div class="tg-footer">👁️ 4.43K · <a href="https://t.me/SBoxxx/18979" target="_blank">📅 21:31 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18978">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">گویا داریم به ساعت صفر حمله زمینی موج 5 نزدیک می شویم.  شاید سرانجام ترامپ توانسته با آب نبات هایی مانند اف-35 و قراردادهای تسلیحاتی و اجازه دادن به ترکیه برای حمله جولانی به لبنان و یافتن جای پا در عمق راهبردی اسرائیل، موافقت و همراهی اردوغان را برای حمله…</div>
<div class="tg-footer">👁️ 4.67K · <a href="https://t.me/SBoxxx/18978" target="_blank">📅 21:10 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18977">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">سایت والا:
ارزیابی‌های امنیتی اسرائیل نشان می‌دهد که رهبری ایران دستور حمله به اسرائیل را صادر خواهد کرد.</div>
<div class="tg-footer">👁️ 4.57K · <a href="https://t.me/SBoxxx/18977" target="_blank">📅 19:43 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18976">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">یک نیروگاه برق دیگر در کویت در اثر حمله ایران دچار آتش سوزی شد.</div>
<div class="tg-footer">👁️ 4.71K · <a href="https://t.me/SBoxxx/18976" target="_blank">📅 18:48 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18975">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">وزیر انرژی آمریکا کریس رایت:  رئیس‌جمهور ترامپ می‌خواهد جنگ را با یک توافق مسالمت‌آمیز با ایران به پایان برساند، اما برای انجام این کار دو طرف لازم است.  اگر آنها آماده انجام این کار هستند، این راهی است که به آن پایان خواهد یافت. در غیر این صورت، ما جریان…</div>
<div class="tg-footer">👁️ 4.73K · <a href="https://t.me/SBoxxx/18975" target="_blank">📅 18:47 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18974">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">وزیر انرژی آمریکا کریس رایت:
رئیس‌جمهور ترامپ می‌خواهد جنگ را با یک توافق مسالمت‌آمیز با ایران به پایان برساند، اما برای انجام این کار دو طرف لازم است.
اگر آنها آماده انجام این کار هستند، این راهی است که به آن پایان خواهد یافت. در غیر این صورت، ما جریان ترافیک از طریق تنگه را بدون همکاری ایران تضمین خواهیم کرد.</div>
<div class="tg-footer">👁️ 4.92K · <a href="https://t.me/SBoxxx/18974" target="_blank">📅 18:47 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18973">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Y5yh1_Qj_m7dkYJaGuReZhLrHfPgmfi-WZy098oHMUMhum2s9WrSztTJvYzmOyKUE2RrtlhedFLJfSgVZh51zKrqK52YEEtCrKF6tawJV1He1FuC3MQ1XtvbQlby843L0oLrfTv8LvLU_6vebP3jR5sfVmyh0ZNBLcjkstvjOS5Gg6eI8j_919hHwUSdstqVg5UDzNJwhvO-WkhgYX1k6f-kdz6geSoEXLIt9a3v34P6UzShXfE2fUKv4eEOghjTlI5U4oKuWq7YEDuUKqa3gEMxa8bNqhNckKiwpzQdI6owwWXfncORDI4-BFYH0x5mu8f1Cq1DwlUMt1kQIYgIlA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حملات موشکی جدید ایران  ایران موشک‌های بالستیک را به سمت اردن پرتاب کرده است   برخی از موشک‌ها به سمت بندر العقبه هدف‌گذاری شده‌اند که در جنوب اردن واقع شده است.  تلاش‌های رهگیری موشک در شهر همسایه ایلات در اسرائیل ثبت شد.</div>
<div class="tg-footer">👁️ 4.63K · <a href="https://t.me/SBoxxx/18973" target="_blank">📅 17:45 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18972">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">نیروهای مسلح اردن:   سه موشک ایرانی که به سمت پادشاهی شلیک شده بودند، رهگیری شدند -   تلویزیون دولتی|</div>
<div class="tg-footer">👁️ 4.48K · <a href="https://t.me/SBoxxx/18972" target="_blank">📅 17:43 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18971">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">نیویورک تایمز:
هجوم‌های اخیر ایران به پایگاه‌های آمریکا در اردن باعث خسارات سنگینی شده است.
بیش از چهار حمله در پنج روز، موشک‌ها و پهپادها ده‌ها سرباز آمریکایی را زخمی کردند، چندین هلیکوپتر بلک هاوک را آسیب زدند و به تأسیسات نظامی کلیدی ضربه زدند.
کشنده‌ترین حمله روز جمعه در پایگاه هوایی موافق سلطی در عزره رخ داد که منجر به کشته شدن دو سرباز آمریکایی، مفقود شدن یک عضو نیروهای مسلح و زخمی شدن چهار نفر دیگر شد.
دو روز پیش، همان پایگاه مورد اصابت قرار گرفت و حدود ۲۰ سرباز زخمی شدند.
حمله دیگری تعداد قابل توجهی از هلیکوپترهای بلک هاوک را در پایگاهی در شرق اردن آسیب زد، در حالی که حمله‌ای قبلی به یک تأسیسات مسکونی ضربه زد و چندین عضو نیروهای مسلح را مجروح کرد.
مسئولان آمریکایی می‌گویند این حملات نشان‌دهنده توانایی فزاینده ایران برای غلبه بر یا فرار از دفاع هوایی ایالات متحده است.</div>
<div class="tg-footer">👁️ 4.6K · <a href="https://t.me/SBoxxx/18971" target="_blank">📅 17:27 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18970">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">سبحان الله این چه وضعیتی است؟!
قرار بود به کمک تازیان بشتابیم تا فلسطین را از اشغال اسراییل آزاد کنند اکنون طوری شده که عربها از اسراییل کمک میگیرند تا پرتابه های ما به چاکرای پایینی شان فرو نرود!
یک جور کمدی پورن شده که انگار عطاران سناریو اش را نوشته باشد!</div>
<div class="tg-footer">👁️ 4.76K · <a href="https://t.me/SBoxxx/18970" target="_blank">📅 16:27 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18969">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">نیروهای مسلح اردن:   سه موشک ایرانی که به سمت پادشاهی شلیک شده بودند، رهگیری شدند -   تلویزیون دولتی|</div>
<div class="tg-footer">👁️ 4.63K · <a href="https://t.me/SBoxxx/18969" target="_blank">📅 16:25 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18968">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">نیروهای مسلح اردن:
سه موشک ایرانی که به سمت پادشاهی شلیک شده بودند، رهگیری شدند -
تلویزیون دولتی|</div>
<div class="tg-footer">👁️ 4.62K · <a href="https://t.me/SBoxxx/18968" target="_blank">📅 16:24 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18967">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">عراق، قراردادهایی به ارزش 60 میلیارد دلار در حوزه انرژی با شرکت‌های آمریکایی امضا کرد!  شرکت‌های غربی فعال در حوزه انرژی، روز جمعه، ده‌ها توافقنامه را با مقامات عراقی در زمینه‌های نفت، گاز و پروژه‌های خطوط لوله امضا کردند. این اقدام در حالی صورت می‌گیرد که…</div>
<div class="tg-footer">👁️ 4.77K · <a href="https://t.me/SBoxxx/18967" target="_blank">📅 14:53 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18966">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/o_t5GqjWDjxnPSejVLc0voyYNkPUMPtTjfmkqxInJQtRHwXzpBBnAq6QilKtKzjkWHDOHa92GpfcuzwPLblt9aFHog4M8zrNrK2evwzVzpA7NtIj8tSi-cJJcMFGK49HD10TskoTB9x9SWFligy6eb1mflwEkCaRxP5_-W2SVHDGHvKXm1BUxkl09Gqv5O1Lx6xMS34xLIsGln5b6o9JjHQHNOfT53aYgiYHRd5i9nA98uJOxC9VoPhEsNiEjXI6UFAPMXvSgUnxe4eHzMEHcfEDJduHht76wx5eoz7Rm8NEM7ad47fL6iKeXYtC7y7iONX9LONl57qRQQKY45ftGQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اسپورت:
کاخ سفید به آرژانتین مجوز داده تا در صورت قهرمانی جام‌جهانی، بنر «جزایر مالویناس متعلق به آرژانتینه» را در مراسم قهرمانی به نمایش بگذارند.</div>
<div class="tg-footer">👁️ 4.88K · <a href="https://t.me/SBoxxx/18966" target="_blank">📅 14:24 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18965">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">نیروی دریایی سپاه پاسداران انقلاب اسلامی:  ساعاتی پیش، چهار فروند کشتی متخلف، با حمایت تروریست‌های آمریکا، با ایجاد اختلال در سیستم‌های ناوبری و بی‌توجهی به هشدارهای مرکز کنترل تنگه هرمز متعلق به نیروی دریایی سپاه پاسداران، تلاش کردند تا تردد را مختل کرده…</div>
<div class="tg-footer">👁️ 5.07K · <a href="https://t.me/SBoxxx/18965" target="_blank">📅 13:11 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18964">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">نیروی دریایی سپاه پاسداران انقلاب اسلامی:
ساعاتی پیش، چهار فروند کشتی متخلف، با حمایت تروریست‌های آمریکا، با ایجاد اختلال در سیستم‌های ناوبری و بی‌توجهی به هشدارهای مرکز کنترل تنگه هرمز متعلق به نیروی دریایی سپاه پاسداران، تلاش کردند تا تردد را مختل کرده و از طریق یک مسیر ناامن از تنگه هرمز خارج شوند.
دو فروند از این کشتی‌ها دچار حادثه شده و متوقف شدند، در حالی که دو فروند دیگر از ادامه مسیر منصرف شدند.
نیروی دریایی سپاه پاسداران انقلاب اسلامی اعلام می‌کند که کنترل کامل تنگه هرمز در اختیار این نیرو است و تنها مسیر ایمن، مسیر مشخص و اعلام‌شده است.
همچنین تأکید می‌کند که هیچ مقداری از نفت، گاز و کود، بدون هماهنگی و مجوز قبلی از تنگه هرمز عبور نخواهد کرد.
کشتی‌هایی که تحت تأثیر اقدامات دشمنان آمریکایی قرار گرفته و وارد مسیر ناایمنی می‌شوند، قطعاً دچار حادثه خواهند شد.</div>
<div class="tg-footer">👁️ 4.96K · <a href="https://t.me/SBoxxx/18964" target="_blank">📅 13:10 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18963">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">خب جام جهانی هم امشب به پایان می رسد.
گفته می شود بازی ایران—سوییس  بعد از فینال برگزار خواهدشد.</div>
<div class="tg-footer">👁️ 5.11K · <a href="https://t.me/SBoxxx/18963" target="_blank">📅 09:46 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18962">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">سپاه با زدن پایگاه های زمینی آمریکایی ها در منطقه به نظرم دارد می کوشد تا تاریخ حمله را به جلو بیاندازد و نگذارد آمریکایی ها بسیج و تدارک کافی داشته باشند.  وقتی می دانید حریف می خواهد حمله زمینی کند خب طبیعی است پایگاه هایش را بزنید تا نتوانند آرایش مناسب…</div>
<div class="tg-footer">👁️ 5.33K · <a href="https://t.me/SBoxxx/18962" target="_blank">📅 09:33 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18961">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">چین؛ ضربه‌گیر جدید بازار نفت در بحران هرمز  در سال‌های گذشته هرگونه تهدید علیه تنگه هرمز تقریباً به‌طور خودکار با جهش شدید قیمت نفت همراه بود. دلیل آن روشن بود؛ حدود یک‌پنجم تجارت دریایی نفت جهان از این گذرگاه عبور می‌کند و هرگونه اختلال در آن، نگرانی از کمبود…</div>
<div class="tg-footer">👁️ 5.07K · <a href="https://t.me/SBoxxx/18961" target="_blank">📅 09:30 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18960">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BJlxdhyJMxOaom0_XYYhLVJFPtOvqCKIZTJ7xdOk-T0CWcQXFrH2AuJJh8S5OhlM3x7jMtrbHm1U0UQyLFuezVC_ajTHtjKA0ENz7mglUUly7G4Ert3MWM015Rkg4nTSC4VgbOLIAEF8YYFmFYAHV1fKO2HMJE9ZsfxqjZ_LvgNYE90Y2is0FXncaKAPvwx3M-Uy88jK7pF96Tg2xJ0wNAewAkvAUFrVYEDZKF3yEPuQ-4EXfcDikBCJHqVcxv0chu-JcWBVguyzqB3uBULStGT39reOdY6d2HIOwRwxwFuJmgaKTjvNtYoyXZ7ocpKgCFkvy_cqqWsNv88MX_iWsQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چین؛ ضربه‌گیر جدید بازار نفت در بحران هرمز
در سال‌های گذشته هرگونه تهدید علیه تنگه هرمز تقریباً به‌طور خودکار با جهش شدید قیمت نفت همراه بود. دلیل آن روشن بود؛ حدود یک‌پنجم تجارت دریایی نفت جهان از این گذرگاه عبور می‌کند و هرگونه اختلال در آن، نگرانی از کمبود عرضه را افزایش می‌دهد. با این حال، ساختار بازار جهانی نفت در سال‌های اخیر تغییر کرده و اکنون یک متغیر جدید در معادله ظاهر شده است:
رفتار وارداتی چین
.
چین که بزرگ‌ترین واردکننده نفت خام جهان است، دیگر صرفاً یک مصرف‌کننده منفعل نیست، بلکه به بازیگری تبدیل شده که می‌تواند شدت نوسانات بازار را تعدیل کند.
گزارش نیکی آسیا
نشان می‌دهد که چین در دوره‌های شوک عرضه، نقش «واردکننده نوسانی» (Swing Importer) را ایفا می‌کند؛ به این معنا که با کاهش موقت خریدهای خود، بخشی از کمبود عرضه جهانی را جبران کرده و از تشدید افزایش قیمت‌ها جلوگیری می‌کند.
این توانایی از چند عامل ناشی می‌شود.:
نخست، چین طی دو دهه گذشته سرمایه‌گذاری عظیمی در ایجاد ذخایر استراتژیک و تجاری نفت انجام داده است. هنگامی که قیمت‌ها افزایش می‌یابد یا مسیرهای عرضه با تهدید مواجه می‌شوند، پکن می‌تواند برای هفته‌ها یا حتی چند ماه بخشی از نیاز پالایشگاه‌های خود را از این ذخایر تأمین کند. در چنین شرایطی، کاهش واردات به معنای کاهش مصرف داخلی نیست، بلکه صرفاً جایگزینی نفت وارداتی با نفت ذخیره‌شده است.
عامل دوم، انعطاف در مدیریت ذخایر تجاری است. چین در دوره‌های قیمت پایین، معمولاً بیش از نیاز روزانه خود نفت خریداری کرده و مخازن را پر می‌کند. اما در دوره‌های افزایش قیمت، این روند متوقف می‌شود و حتی بخشی از ذخایر مصرف می‌شود. در نتیجه، واردات کاهش می‌یابد، بدون آنکه فشار قابل‌توجهی بر فعالیت‌های اقتصادی وارد شود.
از سوی دیگر، پالایشگاه‌های چینی نیز انعطاف عملیاتی بالایی دارند. بسیاری از آنها می‌توانند برنامه تعمیرات یا کاهش موقت ظرفیت تولید را با شرایط بازار هماهنگ کنند. علاوه بر این، تنوع منابع تأمین نفت از روسیه، آسیای مرکزی و سایر تولیدکنندگان غیرخلیج فارس نیز وابستگی کامل چین به نفت عبوری از تنگه هرمز را کاهش داده است.
این تحول، پیامدهای مهمی برای بازار جهانی نفت دارد. در گذشته، کاهش عرضه از خلیج فارس تقریباً به همان میزان باعث افزایش قیمت می‌شد، زیرا تقاضا در کوتاه‌مدت انعطاف چندانی نداشت. اما اکنون، کاهش چندصد هزار بشکه‌ای واردات چین می‌تواند بخشی از این شکاف را پر کند و از شکل‌گیری موج‌های شدید سفته‌بازی جلوگیری کند. به بیان دیگر، چین علاوه بر اینکه بزرگ‌ترین خریدار نفت جهان است، به یکی از ابزارهای تثبیت بازار نیز تبدیل شده است.
البته این نقش محدودیت‌های مهمی نیز دارد. ذخایر استراتژیک چین نامحدود نیست و اگر تنگه هرمز برای چندین ماه به‌طور کامل بسته بماند یا صادرات کشورهای حوزه خلیج فارس به مدت طولانی متوقف شود، پکن نیز ناچار خواهد شد با کاهش واقعی مصرف، افزایش هزینه‌های انرژی و فشار بر صنایع خود کنار بیاید. بنابراین، توانایی چین بیشتر برای مدیریت شوک‌های کوتاه‌مدت و میان‌مدت کاربرد دارد، نه بحران‌های طولانی‌مدت.
در مجموع، یکی از مهم‌ترین تغییرات بازار نفت در دهه اخیر این است که دیگر تنها عرضه‌کنندگان بزرگ مانند عربستان سعودی یا تولیدکنندگان شیل آمریکا بر قیمت‌ها اثر تعیین‌کننده ندارند. اکنون رفتار خرید بزرگ‌ترین واردکننده جهان نیز به همان اندازه اهمیت یافته است. این تحول باعث شده تهدیدهایی مانند اختلال در تنگه هرمز، هرچند همچنان خطرناک، اما نسبت به گذشته تأثیر کمتری بر جهش پایدار قیمت نفت داشته باشند؛ موضوعی که می‌تواند بخشی از اهرم فشار کشورهای صادرکننده نفت در بحران‌های ژئوپلیتیکی را نیز تضعیف کند.
#ژئوپولیتیک
#بازارهای_مالی</div>
<div class="tg-footer">👁️ 5.25K · <a href="https://t.me/SBoxxx/18960" target="_blank">📅 09:26 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18959">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nYVZvkd_M0tXeTsARxej0lizq9Df2NgnGDARoA0MPzhDtZqmJluRbxNLgAK8m8saacRiFjXumfbdovNXFWWPan5X6Vx6PUV3FOf9xMIHEs5mIgojimwAN6Id_vhE4AFKRchbXdNSj8_2e8bzwCJLbJ9xROItT5_nRxj7iwdvCuhJ8mmqsMmXRh_yTBN9TWQd7B9TsuOs_gEiCG-TPH6HOt7pBqIndQ_Cm9pmGH2NNgipjln9yn0wA7bT_yR2gSi7Epb7I0XRpf2Enmjma-HO8PQYfShntxyHAFv7dnAyKe5O145T9JQi5_9tkPCxfHb6OkWWGRy90Ph38dAsfe7JnQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تحلیلی از یکی از نزدیکان محسن رضایی</div>
<div class="tg-footer">👁️ 5.56K · <a href="https://t.me/SBoxxx/18959" target="_blank">📅 01:06 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18958">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/556a107e63.mp4?token=IrQKIPhuVhTLtK7gzM_5yYOLnIsz2xF8WxVsWU9QaLQTMDUkiwz7V7cNXbRKPWOCsFowddK_2FVHSkBZQSIhUUvd1tlFRWPYftufO7al4vm3jxQql4s9RYGlqaFXtWhF8CsK6HaJrHOUtDstxue5-haj58bPtWbKDRYKMt4y1j-dHwX-Dd4x0Y4Qe2uFRCpiTA5HA4DsYoJCHPB7_r0XkEdnas8hiTHrAtreps1_Fy2OnKWVxkuiBZsIHgG8MzdVR7YvwO7VCQl-xVCuSqmpcB8XfiDJf7ORqblftG3aFkO5j0zlBGsmL2Eyf0TihOyK0-dirgtNwHmwGy8feADJPw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/556a107e63.mp4?token=IrQKIPhuVhTLtK7gzM_5yYOLnIsz2xF8WxVsWU9QaLQTMDUkiwz7V7cNXbRKPWOCsFowddK_2FVHSkBZQSIhUUvd1tlFRWPYftufO7al4vm3jxQql4s9RYGlqaFXtWhF8CsK6HaJrHOUtDstxue5-haj58bPtWbKDRYKMt4y1j-dHwX-Dd4x0Y4Qe2uFRCpiTA5HA4DsYoJCHPB7_r0XkEdnas8hiTHrAtreps1_Fy2OnKWVxkuiBZsIHgG8MzdVR7YvwO7VCQl-xVCuSqmpcB8XfiDJf7ORqblftG3aFkO5j0zlBGsmL2Eyf0TihOyK0-dirgtNwHmwGy8feADJPw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">فوری: دو نظامی آمریکایی در اردن در جریان حملات موشکی بالستیک و پهپادی ایران کشته شدند.  در حال حاضر، یک نظامی دیگر مفقود الاثر است.  چهار شهروند آمریکایی با بالگرد به بیمارستان‌های اردن منتقل شدند و پس از درمان، ترخیص شدند.  سایر افراد که دچار جراحات جزئی…</div>
<div class="tg-footer">👁️ 5.97K · <a href="https://t.me/SBoxxx/18958" target="_blank">📅 00:04 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18957">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">بندرعباس؛ گلوگاهی که فروپاشی‌اش فاجعه است   بندرعباس تنها یک شهر ساحلی نیست؛ گره‌گاهی است که بخش بزرگی از تنفس اقتصادی و لجستیکی ایران از آن می‌گذرد. بندر شهید رجایی، بزرگ‌ترین بندر کانتینری کشور، حدود ۸۵ درصد از کل تخلیه و بارگیری بنادر ایران را انجام می‌دهد؛…</div>
<div class="tg-footer">👁️ 5.32K · <a href="https://t.me/SBoxxx/18957" target="_blank">📅 23:56 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18956">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">—گزارش‌ها حاکی از آن است که جنگنده‌های F-16 نیروی هوایی ایالات متحده مستقر در پایگاه هوایی اسپانگدالم در آلمان به خاورمیانه اعزام شده‌اند. این هواپیماها قادر به هدف قرار دادن سیستم‌های راداری پدافند هوایی ایران و همچنین دارایی‌های موشکی هوا به زمین هستند.
علاوه بر این، جنگنده‌های پنهان‌کار F-35 از پایگاه هوایی لکن‌هیت در بریتانیا نیز به همراه تانکرهای اضافی سوخت‌رسانی هوایی برای پشتیبانی از عملیات گسترده‌تر هوایی ایالات متحده به این منطقه اعزام شده‌اند.</div>
<div class="tg-footer">👁️ 5.43K · <a href="https://t.me/SBoxxx/18956" target="_blank">📅 23:55 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18955">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PsRY3rj083LuJYVctOQU7znTetNxs5c-5JpDEEbcIV2FL4KDjpgcr6D7QViooq3Q_FELbsaPg0WEMcCEcaNtdH1oLh73ULKZfN55q81CCIkBflPBNkaFHdGIdgfnSpSZ3Bpz4JAjsiAwgR4IQ8UeldLhuY6FRjKq0s-bLeQmbZB0F5uNjO3wKT3eqADYDuhyNebUKxK1Ko3BMxdhC2pj-RmPCDKsBiPSAi7Uv9-6c6cqSHqlzlhoeZr8rE0WMqKn7Ui-J_vtvfAtwT3zELIFq772OEBiQez-n43sorzlg3y0RT_KM9EwfQFy5VGGb9hSolHa_IW9ErpgcYegy7cadg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بندرعباس؛ گلوگاهی که فروپاشی‌اش فاجعه است
بندرعباس تنها یک شهر ساحلی نیست؛ گره‌گاهی است که بخش بزرگی از تنفس اقتصادی و لجستیکی ایران از آن می‌گذرد. بندر شهید رجایی، بزرگ‌ترین بندر کانتینری کشور، حدود ۸۵ درصد از کل تخلیه و بارگیری بنادر ایران را انجام می‌دهد؛ سالانه نزدیک به 6 میلیون کانتینر و تا 70 میلیون تن کالا از آن عبور می‌کند. این بندر مستقیماً به شبکه ملی راه‌آهن و بزرگراه‌های ایران متصل است و همین اتصال، آن را به مسیر اصلی جابه‌جایی تدارکات نظامی، سوخت، نیرو و کالای تجاری میان مرکز ایران و کرانه جنوبی تبدیل کرده است. موقعیت مسلط بندرعباس بر شمال تنگه هرمز نیز دروازه ایران به مهم‌ترین گلوگاه انرژی جهان است.
اما اهمیت بندرعباس به کانتینر و اسکله ختم نمی‌شود. پالایشگاه ستاره خلیج فارس در همین منطقه مستقر است؛ بزرگ‌ترین تولیدکننده بنزین ایران که به‌تنهایی حدود ۴۰ درصد بنزین کشور را تأمین می‌کند و بزرگ‌ترین پالایشگاه میعانات گازی جهان به شمار می‌رود. پالایشگاه نفت بندرعباس نیز در کنار آن قرار دارد. افزون بر این، در دوره‌های کمبود، بخشی از بنزین وارداتی ایران هم از همین بنادر جنوبی وارد و توزیع می‌شود. به بیان دیگر، تولید سوخت، واردات سوخت و ترانزیت کالا در یک نقطه جغرافیایی واحد متمرکز شده‌اند.
همین تمرکز، شکنندگی خطرناکی می‌سازد. انفجار مهیب فروردین ۱۴۰۴ (آوریل ۲۰۲۵) در بندر شهید رجایی، که ده‌ها کشته و نزدیک به هزار زخمی بر جای گذاشت، نشان داد چگونه یک حادثه واحد می‌تواند قلب تجارت دریایی کشور را از کار بیندازد و زنجیره تأمین را در سطح ملی مختل کند.
اکنون تصور کنید ایران این بندر را از دست بدهد. پیامد آن، قطع همزمان ۸۵ درصد تجارت دریایی، توقف حدود ۴۰ درصد تولید بنزین ملی و مسدود شدن یکی از اصلی‌ترین مسیرهای واردات سوخت خواهد بود؛ ترکیبی که به بحران سوخت سراسری، اختلال در زنجیره تأمین نظامی و لجستیکی، و فلج بخش عمده‌ای از اقتصاد وابسته به واردات می‌انجامد. از دست رفتن دسترسی مطمئن به تنگه هرمز نیز اهرم راهبردی ایران را به‌شدت تضعیف می‌کند.
بندرعباس دقیقاً همان نقطه‌ای است که در آن بیشترین اهمیت و بیشترین آسیب‌پذیری به هم گره خورده‌اند و بنابراین حفظ کنترل آن برای ایران نه یک انتخاب، که یک ضرورت وجودی است.
#ژئوپولیتیک</div>
<div class="tg-footer">👁️ 6.18K · <a href="https://t.me/SBoxxx/18955" target="_blank">📅 23:42 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18954">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">مقامات آمریکایی نگرانند که چین یا روسیه ممکن است به ایران در حمله به اهداف ایالات متحده کمک کنند.
به گزارش وال استریت ژورنال، ایران اکنون موشک‌های مانورپذیری را با سرعت‌های بسیار بالا شلیک می‌کند.</div>
<div class="tg-footer">👁️ 5.17K · <a href="https://t.me/SBoxxx/18954" target="_blank">📅 23:23 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18953">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">الاغ ما سالهاست در جهنم هستیم؛ دروازه هایش را بگشایی همه فرار می کنیم!</div>
<div class="tg-footer">👁️ 5.44K · <a href="https://t.me/SBoxxx/18953" target="_blank">📅 23:08 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18952">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">انتظار تشدید بی سابقه تنش ها می رود...</div>
<div class="tg-footer">👁️ 5.64K · <a href="https://t.me/SBoxxx/18952" target="_blank">📅 23:07 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18951">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fAc1lHH50I3ChWpP0b6lVAsgzc3a9X_oGQUPdJRJD3PPmsN2m14GusF_uPcT5-ko3cRoCt-buLLrcabTKcaHIbXETIixHQFBTYLUZ4TOPDAmpJISSWyXYL7jSvaltDK42D-IqhGQb4SXHHNE80KBRU0xwAmlGSOLWYwaUpEv2vbg84eTn_blqotPHqMGun4KNW-jU838tNskNy8bzrAXUu8KHKyW2hag9aGaWrWb-TnhZORMSco74LPIIM-i0v1WrVnIlQ3GJnfVxNElC44LakvGzY8E4rqaBuPf50WsUnLVfE10KEkl_l6VWXli5YY7ehZQsAtGTozNkrwehjnLuw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزیر دفاع آمریکا در واکنش به کشته شدن دو سرباز آمریکایی:
«خدا نگهدار قهرمانان. فداکاری آنها فقط عزم ما را راسخ‌تر می‌کند.»</div>
<div class="tg-footer">👁️ 5.22K · <a href="https://t.me/SBoxxx/18951" target="_blank">📅 22:52 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18950">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">کریمه؛ از ویترین پیروزی پوتین تا آسیب‌پذیرترین جبهه روسیه
حملات مداوم اوکراین، کریمه را از نماد اقتدار روسیه به یکی از ناامن‌ترین مناطق تحت کنترل مسکو تبدیل کرده است. منطقه‌ای که زمانی مقصد گردشگران بود، امروز تقریباً هر شب هدف پهپادها قرار می‌گیرد؛ تا جایی که مقامات محلی برای جلوگیری از ایجاد وحشت و اختلال در فصل گردشگری، سامانه‌های هشدار هوایی را عملاً غیرفعال کرده‌اند. در بیشتر نقاط شبه‌جزیره، حملات به پایگاه‌های نظامی، زیرساخت‌های انرژی، خطوط راه‌آهن و مراکز لجستیکی به بخشی از زندگی روزمره تبدیل شده است.
تمرکز اوکراین بر قطع شریان‌های تدارکاتی، فشار بی‌سابقه‌ای بر کریمه وارد کرده است. حمله به پایانه نفتی کرچ، آسیب به کشتی‌های باری و تهدید کریدور زمینی از جنوب اوکراین، انتقال سوخت و تجهیزات را دشوار کرده است. خاموشی‌های گسترده، محدودیت فروش بنزین و اختلال در تأمین کالاها، نشانه‌هایی از فرسایش توان لجستیکی روسیه در این منطقه هستند. همزمان، پهپادهای اوکراینی پالایشگاه‌ها و تأسیسات نفتی در عمق خاک روسیه، از جمله اطراف مسکو، را نیز هدف قرار داده‌اند و بحران سوخت را تشدید کرده‌اند.
اهمیت کریمه برای کرملین تنها نظامی نیست؛ این شبه‌جزیره مهم‌ترین دستاورد سیاسی ولادیمیر پوتین پس از الحاق در سال ۲۰۱۴ محسوب می‌شود و جایگاه ویژه‌ای در روایت ملی‌گرایانه روسیه دارد. با این حال، افزایش ناامنی، کاهش اعتماد مردم به توانایی دولت در حفاظت از منطقه و مهاجرت تدریجی خانواده‌های مرفه، نشان می‌دهد که هزینه‌های جنگ به قلب این نماد سیاسی رسیده است.
با وجود این، نشانه‌ای از تغییر گسترده وفاداری ساکنان به روسیه دیده نمی‌شود. بسیاری از مردم، به‌ویژه در سایه تبلیغات گسترده امنیتی و نگرانی از برخورد احتمالی اوکراین، همچنان بازگشت حاکمیت کی‌یف را تهدیدی برای خود می‌دانند. اما آنچه بیش از هر چیز در کریمه و حتی سراسر روسیه به چشم می‌آید، خستگی عمومی از جنگی است که پس از سال‌ها نبرد، هنوز چشم‌انداز روشنی برای پایان یا پیروزی آن وجود ندارد.
#ژئوپولیتیک</div>
<div class="tg-footer">👁️ 5.11K · <a href="https://t.me/SBoxxx/18950" target="_blank">📅 22:33 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18949">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kDJN3eysZ0jyUskuMgKm4vyXhcYZqpP9YSvExBN0w8x5cGYxVsSkk12xAyGrtJQzdwgvz8ZG3m-gT2S5fkdbtW2B6KYFYNxNl5WFpPyMVWnK5m2jZx-tMBoTcj1ns7TqzufcDq6rQ84UTIx_q1r6VIzUbfv_0Wt1gdRR63ywi6frwH-By0iboXQs6FSICuX7UiW4JoSavHHkRMPaOJiTIP01WdQDkr9r1mYtuMJeAqSUkWVuCNDp8srT1-QeEfdULUpkgIRU_6G9M1pbT40H7xTObi-dkHlFRHJlE4nfiF8aQ5xmwRlQcxZ-OvJfS13FgXgrzDfc9374ftVzXxkcgQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ولید گدبان سفیر اسرائیل در سازمان ملل:
موج آهنین درحال برخواستن است.</div>
<div class="tg-footer">👁️ 5.04K · <a href="https://t.me/SBoxxx/18949" target="_blank">📅 21:51 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18948">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ov9SGkiMXL0fZHEha79UHf67ATewcyi7dkB5FXiJqI3mobY8JBJFv6jbmebht9KNA6sy4JbHf25jAR6tcB4uv3YnNcfwZa8H2Su7TUV7wAuRHfGlZ1E4JHOSKxRELYKSGuJ6w0wlfF-NSNjwToRl-1C3zKiAqBbPS4o806cnYOuMBlhy2hdSSMRFZCu0CHX_rYAV0F0am57FMpeiud-HYJsZIkNRABzd7CYUd2MGv6oEn3Dr8mMSJLDPbU9v4ecTP9v5dJ1D2tTyFrZlQ0GabAQipciJ5Iu9-BSbzVaWSyEFW3yHdVOazFMEd2sCZOEEow1wn9pRwnxkcexJt4Y0tw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ: ممکن است سپاه پاسداران را مانند داعش نابود کنیم
دونالد ترامپ، رئیس‌جمهور آمریکا، در اظهاراتی تازه احتمال اقدام نظامی گسترده علیه سپاه پاسداران انقلاب اسلامی را رد نکرده و گفته است که واشنگتن ممکن است این نهاد را «مانند داعش از بین ببرد». این سخنان در شرایطی مطرح می‌شود که درگیری میان آمریکا و ایران پس از فروپاشی آتش‌بس دوباره شدت گرفته و دو طرف وارد مرحله‌ای از حملات متقابل شده‌اند. (
Time
)
ترامپ در پاسخ به پرسشی درباره اینکه آیا ممکن است سپاه را همانند داعش هدف قرار دهد، گفت که «خواهیم دید چه اتفاقی می‌افتد». او همچنین مدعی شد که ایران بار دیگر خواهان مذاکره شده است، اما همزمان تأکید کرد که واشنگتن حاضر نیست بدون تغییر رفتار تهران، مسیر گفت‌وگو را ادامه دهد.
سپاه پاسداران یکی از مهم‌ترین ستون‌های ساختار قدرت جمهوری اسلامی محسوب می‌شود. این نهاد علاوه بر نقش نظامی، در حوزه‌های امنیت داخلی، برنامه موشکی، فعالیت‌های منطقه‌ای و شبکه نیروهای هم‌پیمان ایران در خاورمیانه نقش گسترده‌ای دارد. آمریکا در سال ۲۰۱۹ سپاه را در فهرست سازمان‌های تروریستی خارجی قرار داد.
مقایسه سپاه با داعش از سوی ترامپ نشان‌دهنده تغییر احتمالی در سطح اهداف جنگی آمریکا است. عملیات علیه داعش عمدتاً با هدف نابودی یک گروه شبه‌نظامی فراملی انجام شد، اما سپاه بخشی از ساختار رسمی حکومت ایران است؛ بنابراین هرگونه تلاش برای «نابودی» آن، می‌تواند به معنای رویارویی مستقیم با یکی از پایه‌های اصلی جمهوری اسلامی و افزایش شدید خطر گسترش جنگ باشد.
اظهارات ترامپ در حالی بیان شده که آمریکا حملات خود علیه اهداف نظامی ایران را افزایش داده و اعلام کرده است که مراکز فرماندهی، سامانه‌های پدافندی، توان موشکی و پهپادی و زیرساخت‌های مرتبط با تهدید علیه کشتیرانی در تنگه هرمز را هدف قرار داده است. ایران نیز در واکنش، حملاتی علیه مواضع آمریکا و متحدانش در منطقه انجام داده است.
از نگاه تحلیلگران، تهدید علیه سپاه نشان می‌دهد که اختلاف میان تهران و واشنگتن دیگر تنها حول موضوعاتی مانند برنامه هسته‌ای یا تحریم‌ها نیست، بلکه به سمت یک رویارویی ساختاری درباره نقش منطقه‌ای ایران و معماری امنیتی خاورمیانه حرکت کرده است.
در صورت عملی شدن چنین رویکردی، آمریکا با یک انتخاب بسیار پرهزینه روبه‌رو خواهد شد: تلاش برای ضربه زدن به مهم‌ترین نهاد نظامی ایران، بدون آنکه تضمینی برای فروپاشی ساختار قدرت تهران یا پایان درگیری وجود داشته باشد.</div>
<div class="tg-footer">👁️ 5.43K · <a href="https://t.me/SBoxxx/18948" target="_blank">📅 21:28 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18947">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/r1q6cUZK6mDsqL3IE7CzRZRJPvCHHApemXNXLj-ulXGzZmzz8ADUvWnb3RunAY6l8bWgrCisluEE2-bbNeCqfaR9RJYQBix2H5pSWPV9XWQbB_Zn6W3mG8Jy2gE4f_pao-dMBKnvG4wQUojTAjOaf84ft6y9gCwX4rvbpDZDFHcd2aZw1ZU29pWOrzWcHftW0aZCrqMrvQOvZsA1qrfw-8cmhviNi5sSbqd-_Im_YJMt1tgWcKdWpUeebnj9c06xV3d5mH5sgB4n3ZkAqb6A_b-Sdbt8mtvdizWWX93-gl4h8IJq5pIOBbwHYnyhQIaDqzLbPMQdAi-Xz7T7TC7lIw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">انتظار تشدید بی سابقه تنش ها می رود...</div>
<div class="tg-footer">👁️ 5.42K · <a href="https://t.me/SBoxxx/18947" target="_blank">📅 21:07 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18946">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">فوری: دو نظامی آمریکایی در اردن در جریان حملات موشکی بالستیک و پهپادی ایران کشته شدند.  در حال حاضر، یک نظامی دیگر مفقود الاثر است.  چهار شهروند آمریکایی با بالگرد به بیمارستان‌های اردن منتقل شدند و پس از درمان، ترخیص شدند.  سایر افراد که دچار جراحات جزئی…</div>
<div class="tg-footer">👁️ 5.27K · <a href="https://t.me/SBoxxx/18946" target="_blank">📅 21:05 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18945">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jsPCZr7k0MdGvIzgf6LR4aqpkhqod4ZUA5j6boG_QG6NqbAg39o8Qk5JUOyl4DYtuWrXh5T4Ccb5esOYIqjnMpTJxlwSw0wrs96qFmkXtPeWa_NMhitBCjawDXIfZxfQOFnSEtZx87pwYj2Q7P8xYorgyuLmPYjXb5_hDI2irx1oSozDb7mIboMFHmSqhF4dBmXCAXHC_dK326NYwI0UXjVo5eJHElwL4gAxXEvvlE7T9mLtHznIWTZ3Tt_asEkTSuymBtdhyAr3jV2bGLxvih4BPEWV-plvzOoeMJW_vH9u38ZX_jp8lG9k6phXGQlrO7lLSryp-di1-F1H0gsSnQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پست جدید ترامپ که به نظرم به نوعی تاییدی بر حمله زمینی است.</div>
<div class="tg-footer">👁️ 6.97K · <a href="https://t.me/SBoxxx/18945" target="_blank">📅 20:59 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18944">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">فوری: دو نظامی آمریکایی در اردن در جریان حملات موشکی بالستیک و پهپادی ایران کشته شدند.  در حال حاضر، یک نظامی دیگر مفقود الاثر است.  چهار شهروند آمریکایی با بالگرد به بیمارستان‌های اردن منتقل شدند و پس از درمان، ترخیص شدند.  سایر افراد که دچار جراحات جزئی…</div>
<div class="tg-footer">👁️ 5.1K · <a href="https://t.me/SBoxxx/18944" target="_blank">📅 20:47 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18943">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">فوری: دو نظامی آمریکایی در اردن در جریان حملات موشکی بالستیک و پهپادی ایران کشته شدند.
در حال حاضر، یک نظامی دیگر مفقود الاثر است.
چهار شهروند آمریکایی با بالگرد به بیمارستان‌های اردن منتقل شدند و پس از درمان، ترخیص شدند.
سایر افراد که دچار جراحات جزئی شده بودند، به وظایف خود بازگشتند.</div>
<div class="tg-footer">👁️ 5.44K · <a href="https://t.me/SBoxxx/18943" target="_blank">📅 20:46 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18942">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Fj2ZYTD7z-lcAqUi03FDsagcgcHVnGp0X2AafuLuqj0w_TvnnHUfmMKnLKoXTJnl5zIutQUxp25QL42YxaqKimel4jpdbBlTvb1BQSLvo805jrVFzo1bz_uhHGy7-G2u5Lhyo7tMA2d1ejNctjuloRaYedBWbtDpGoSYJJ3Lt6GeJXIyiPfobks83S-VtTiSdFJ7-bk_lP802Bh5ZhJDinKng2BAqcfnkP6418cabtAK4xVb2-SXltkzGkcZbZKSwwGnwxOIAnEw-Yny3n0UxDfYMTw0PRlvHC0oeQHO-P8ZlsN4eWpIyM8PuI2aLANkr3dHUJvIFL6wpHq0vrQwBA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سنتکام می گوید در حمله سپاه به پایگاه آمریکایی ها در التنف سوریه هیچ تلفاتی وارد نشده است.  اساساً به نظر من حمله به سوریه پیامی تهدیدآمیز به جولانی بود که به حزب الله حمله نکند ولی اینها جدی گرفتند.</div>
<div class="tg-footer">👁️ 4.98K · <a href="https://t.me/SBoxxx/18942" target="_blank">📅 20:07 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18941">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4886d9a21f.mp4?token=C6dJ5KHxsQEQ_Ik_MJ_MmOPgGKusVXxn8Y5oxGVwfhD2-0yzjE-HoZRPZYlcyKhsiOXjUs3ZNfWsB1mIZXupADZ6d8gt2g4yIXAZo4M81hhm2JQfKugS90hnYuIEU9AJh5FsdOHOjIz4dhhnRMILrWIiv8z7yNuKHkKvldCOnayzyogetaVGSLT9nJABKwx8rjpAH05LU8Q1UoQ22j7wTHBlSpCSDWXxM7rbsa1UlDy2p3lbxFj6NJu9CvPfBCUcAB2h4sbonm9pIAPViVJvWcc32yBcjC_YRWJzXF92_pYVbsv1Vak4URDbu3TlWZcS7DHWR0iz4BS8mkiA5IfvnQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4886d9a21f.mp4?token=C6dJ5KHxsQEQ_Ik_MJ_MmOPgGKusVXxn8Y5oxGVwfhD2-0yzjE-HoZRPZYlcyKhsiOXjUs3ZNfWsB1mIZXupADZ6d8gt2g4yIXAZo4M81hhm2JQfKugS90hnYuIEU9AJh5FsdOHOjIz4dhhnRMILrWIiv8z7yNuKHkKvldCOnayzyogetaVGSLT9nJABKwx8rjpAH05LU8Q1UoQ22j7wTHBlSpCSDWXxM7rbsa1UlDy2p3lbxFj6NJu9CvPfBCUcAB2h4sbonm9pIAPViVJvWcc32yBcjC_YRWJzXF92_pYVbsv1Vak4URDbu3TlWZcS7DHWR0iz4BS8mkiA5IfvnQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گفته می شود این ویدیو مربوط به اعزام صدها نیروی ویژه آمریکایی به جبهه های جنگ ایران است.</div>
<div class="tg-footer">👁️ 5.25K · <a href="https://t.me/SBoxxx/18941" target="_blank">📅 20:05 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18940">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">GeoMarket Podcast -- 8.pdf</div>
  <div class="tg-doc-extra">210.5 KB</div>
</div>
<a href="https://t.me/SBoxxx/18940" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">#پادکست_GeoMarkets  شماره — 8  جمعه 17 جولای 2026</div>
<div class="tg-footer">👁️ 4.81K · <a href="https://t.me/SBoxxx/18940" target="_blank">📅 20:03 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18939">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">#پادکست_GeoMarkets  شماره — 8  جمعه 17 جولای 2026</div>
<div class="tg-footer">👁️ 4.84K · <a href="https://t.me/SBoxxx/18939" target="_blank">📅 20:01 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18938">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">بلومبرگ :   قیمت بنزین خودروها در ایالات متحده با تشدید رویارویی بین واشنگتن و تهران، بار دیگر به نزدیکی ۴ دلار در هر گالن رسیده است</div>
<div class="tg-footer">👁️ 5.43K · <a href="https://t.me/SBoxxx/18938" target="_blank">📅 19:18 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18937">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">عراق، قراردادهایی به ارزش 60 میلیارد دلار در حوزه انرژی با شرکت‌های آمریکایی امضا کرد!  شرکت‌های غربی فعال در حوزه انرژی، روز جمعه، ده‌ها توافقنامه را با مقامات عراقی در زمینه‌های نفت، گاز و پروژه‌های خطوط لوله امضا کردند. این اقدام در حالی صورت می‌گیرد که…</div>
<div class="tg-footer">👁️ 5K · <a href="https://t.me/SBoxxx/18937" target="_blank">📅 19:15 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18936">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">انتقاد شدید علی‌اکبر ولایتی مشاور رهبر شهید انقلاب در امور بین الملل از نخست‌وزیر عراق  سفری تأسف بار، بی‌موقع و تخریب کننده مجاهدتهای ملت غیور و مجاهد عراق در تاریخ چند هزار ساله این کشور بزرگ، توسط نخست وزیر جوان و کم تجربه، آقای علی الزیدی.  وی تأکید کرد…</div>
<div class="tg-footer">👁️ 4.95K · <a href="https://t.me/SBoxxx/18936" target="_blank">📅 19:03 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18935">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">📌
چرا قیمت بنزین بر نرخ تأیید ترامپ تأثیر بیشتری دارد؟  قیمت بنزین بیش از نفت خام بر محبوبیت رئیس‌جمهور اثر می‌گذارد، چون مردم هر روز مستقیماً هزینه آن را احساس می‌کنند و افزایش آن سریع‌تر به نارضایتی عمومی تبدیل می‌شود.  در بحران ۲۰۲۶ نیز با وجود کاهش نسبی…</div>
<div class="tg-footer">👁️ 4.76K · <a href="https://t.me/SBoxxx/18935" target="_blank">📅 17:49 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18934">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">وزارت خارجه قطر:
«ما مجدداً تأکید می‌کنیم که هدف قرار دادن نیروگاه‌های برق و تأسیسات شیرین‌سازی آب در کویت از تمام خطوط قرمز عبور می‌کند».</div>
<div class="tg-footer">👁️ 4.84K · <a href="https://t.me/SBoxxx/18934" target="_blank">📅 17:27 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18933">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">پس از حملات پهپادی اوکراین امروز، بخشی از منطقه مسکو روسیه توسط یک ابر ضخیم، تاریک و هولناک پوشیده شده است!</div>
<div class="tg-footer">👁️ 4.93K · <a href="https://t.me/SBoxxx/18933" target="_blank">📅 17:23 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18932">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">📌
چرا قیمت بنزین بر نرخ تأیید ترامپ تأثیر بیشتری دارد؟  قیمت بنزین بیش از نفت خام بر محبوبیت رئیس‌جمهور اثر می‌گذارد، چون مردم هر روز مستقیماً هزینه آن را احساس می‌کنند و افزایش آن سریع‌تر به نارضایتی عمومی تبدیل می‌شود.  در بحران ۲۰۲۶ نیز با وجود کاهش نسبی…</div>
<div class="tg-footer">👁️ 4.63K · <a href="https://t.me/SBoxxx/18932" target="_blank">📅 17:11 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18931">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromCyclical Waves</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PQ0-sPHyinbxAQHoAzeIvpWM0PvOKDX24lVLtLAKNZ-XniMpPw3hlYon4DbYjf6-JwEKttT4cnHXuNrTYhBPr0N0R8uAxehhZ8YZd5VHQtp-ysBK95UsFuIlq0clAEkeYgof0WNGS0tirukAV5cSyjHdKoGTNRiwmbniUExF81aZcgjj-KFkJoNDuE4UVBor1zHS2UgyDd-bWO5uOY1pX-8gz2fJxlNcoZtTSy6YM6pLPeaIAuEsW21RA14ff1A4h9FJhfpsxyT6Mt_XYXElFkiNMUUgzqoiUx4WzgLJektcKWFl5HykfgiG0OoC0Ii64GpG-jNp9ozhCgSD_k2Umg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📌
چرا قیمت بنزین بر نرخ تأیید ترامپ تأثیر بیشتری دارد؟
قیمت بنزین بیش از نفت خام بر محبوبیت رئیس‌جمهور اثر می‌گذارد، چون مردم هر روز مستقیماً هزینه آن را احساس می‌کنند و افزایش آن سریع‌تر به نارضایتی عمومی تبدیل می‌شود.
در بحران ۲۰۲۶ نیز با وجود کاهش نسبی قیمت نفت پس از آتش‌بس، ماندگاری قیمت بالای بنزین فشار سیاسی بر ترامپ را حفظ کرد و به عاملی مهم در کاهش نرخ تأیید او تبدیل شد.
🔗
ادامه یادداشت را از اینجا بخوانید
💬
ارتباط با پشتیبانی :
@CyclicalWavesSupport
📌
کانال ما :
@cyclicalwaves</div>
<div class="tg-footer">👁️ 4.7K · <a href="https://t.me/SBoxxx/18931" target="_blank">📅 17:09 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18930">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">کارشناس صداوسیما:
آمریکا در مواجهه با ایران کلأ دو راه برایش مانده: بمب اتم یا حمله زیرساختی نابودکننده</div>
<div class="tg-footer">👁️ 4.84K · <a href="https://t.me/SBoxxx/18930" target="_blank">📅 16:59 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18929">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kZmqpBe7a7BSA8TUJtlGbWr2OYNYExaVjB8kLTA0HZCbfq0wysTA5CWuxvw23dxVKcVwp8P_PC_b389PAaluQ_XPzBsy1uF2m8P8iUsuP5A-t70Fit92GjkwrXVeOfKdHhgDO5zouOS3Ivw87Ygk7sofN_t4UyH44w7pT3Hz4OCpqF4YslYo9sdo_r-Yb4Su0qlWmk2hijrTOU56RDY0moT6KzTX7CU8PxjP6iSGE3ZpgJJoJvUHKvROKICZMNwmBF1j6DPCRyATlq_pb_QNIIzwlz60o3g2ERiURzoTa_xbk7Sldt_wJGYEowd06uRcGDFF5D4NDWc5WwkwaBF6eg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اهداف مورد اصابت گرفته در منطقه از سوی سپاه</div>
<div class="tg-footer">👁️ 5.08K · <a href="https://t.me/SBoxxx/18929" target="_blank">📅 16:56 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18928">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">موشک‌های بالستیک ایرانی آکادمی امنیت کویت را هدف قرار دادند.</div>
<div class="tg-footer">👁️ 4.91K · <a href="https://t.me/SBoxxx/18928" target="_blank">📅 16:55 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18927">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">پس از حملات پهپادی اوکراین امروز، بخشی از منطقه مسکو روسیه توسط یک ابر ضخیم، تاریک و هولناک پوشیده شده است!</div>
<div class="tg-footer">👁️ 5.33K · <a href="https://t.me/SBoxxx/18927" target="_blank">📅 11:49 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18926">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d467cc7c82.mp4?token=rAB82Kf9Ur_vin6J4rx35X2lDQmDmy2WJXyd2dUX_jP5ju72VhmWnB9BSLqKU8RJ7iAujBPUrSXqkJYCnPPqkrnSV7yrnFIAC6933hl6CSpVklRf-TmjWx4UDI1mL2kBfW7aLAr25UcRfC6xhXoDfMskUa31HDNth7kKFEETS6bDdWKVg71gBEi88rCjx8rHlgo2Aa0HjydZCfWMYH1yqc9BoMd9bAKcJIk_UZNhzYLgc8bDth3fglslGZxXCSWmunTOG5t-ia9EbGSXHb2RxoZ-65tANSFY7nWnGPbN7HzCTH2sgzVnUlZtzIymD6kxOc-OXSAwRHS97riwFdn34w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d467cc7c82.mp4?token=rAB82Kf9Ur_vin6J4rx35X2lDQmDmy2WJXyd2dUX_jP5ju72VhmWnB9BSLqKU8RJ7iAujBPUrSXqkJYCnPPqkrnSV7yrnFIAC6933hl6CSpVklRf-TmjWx4UDI1mL2kBfW7aLAr25UcRfC6xhXoDfMskUa31HDNth7kKFEETS6bDdWKVg71gBEi88rCjx8rHlgo2Aa0HjydZCfWMYH1yqc9BoMd9bAKcJIk_UZNhzYLgc8bDth3fglslGZxXCSWmunTOG5t-ia9EbGSXHb2RxoZ-65tANSFY7nWnGPbN7HzCTH2sgzVnUlZtzIymD6kxOc-OXSAwRHS97riwFdn34w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پس از حملات پهپادی اوکراین امروز، بخشی از منطقه مسکو روسیه توسط یک ابر ضخیم، تاریک و هولناک پوشیده شده است!</div>
<div class="tg-footer">👁️ 5.66K · <a href="https://t.me/SBoxxx/18926" target="_blank">📅 11:48 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18925">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">یک مقام آمریکایی گفت که ایران یک موشک بالستیک به سمت یک پایگاه نظامی آمریکا در عربستان سعودی شلیک کرد.
این نخستین حمله مستقیم ایران به عربستان سعودی در نزدیک به چهار ماه اخیر است.</div>
<div class="tg-footer">👁️ 5.2K · <a href="https://t.me/SBoxxx/18925" target="_blank">📅 11:43 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18924">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">چین در این 4 سال مانند یک زالو، شیره جان روسیه را مکید و اکنون به دنبال زامبی کردن روسیه است.  ادعاهای ارضی چینی ها هم بعید نیست دوباره ضد روسیه مطرح بشود.  #ژئوپولیتیک</div>
<div class="tg-footer">👁️ 5.25K · <a href="https://t.me/SBoxxx/18924" target="_blank">📅 11:13 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18923">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oCXG0gEUrORAIu2HIR7GSSScCfvDsd02gWGBWGkbgS9ccqFKQhGQ8TpHvjU8cWaewSAgKlOS3C2C9sOnbC8iTJeQVHHFKAyv0R7Y0jn_S4XRdOyunWJ_CS7lgPKFxpU2lzskUePrun8if5cQNAr_1g648lqPgUATaykqMv_kZ6IL2F8EACfkutnFtrB7E2_hAl_qLhYOjmQR1cej7I5NaVEWanTJ85EaY9G8um3AoG7VGIh6mAC534-Js3R1GxaHPg_0cqF6X6tVYrruHPh6RfeOyeTDxPbwMUbsVzpTp5vPMbQh3OZFfMQ5Le9lPhtC0J76mQnL9bo4ZZdCSQ4S2g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نقشه زمانی تراکم حملات ایران به کویت از 3 ژوئن تا کنون</div>
<div class="tg-footer">👁️ 5.41K · <a href="https://t.me/SBoxxx/18923" target="_blank">📅 09:25 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18922">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">پرس تی وی: نیروی دریایی سپاه پاسداران انقلاب اسلامی، حملات هوایی و موشکی را علیه اسکله پشتیبانی سوختی نیروی دریایی آمریکا در بندر الاحمدی کویت و همچنین انبوهی از هواپیماهای نظامی دشمن در پایگاه هوایی شیخ عیسی بحرین انجام داد.
این نیرو همچنین، مرکز داده‌های اطلاعاتی باتلکو متعلق به دشمن در بحرین را هدف قرار داد و یک مرکز ارتباطی و سیگنال دهی آمریکایی را در کویت منهدم کرد، در حالی که کنترل کامل تنگه هرمز را حفظ کرده است.</div>
<div class="tg-footer">👁️ 5.45K · <a href="https://t.me/SBoxxx/18922" target="_blank">📅 09:12 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18921">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">استانداری هرمزگان:
پل محور رفت سه راه‌میناب به‌سمت
رودان
بعد از دو راهی سرزه مورد حمله دشمن واقع شده است.</div>
<div class="tg-footer">👁️ 5.39K · <a href="https://t.me/SBoxxx/18921" target="_blank">📅 09:10 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18920">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">سبحان الله!
شب خوش!</div>
<div class="tg-footer">👁️ 5.52K · <a href="https://t.me/SBoxxx/18920" target="_blank">📅 01:45 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18919">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">به نظر می‌رسد بانو وضعیت پدافند کویت را توصیف می‌کند!</div>
<div class="tg-footer">👁️ 5.55K · <a href="https://t.me/SBoxxx/18919" target="_blank">📅 01:42 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18917">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">اثر جاودانه بانوی دو عالم — لورا برانیگن — به نام Self Control  که در آن میفرماید:  Oh, the night is my world City light painted girl  In the day, nothing matters It's the nighttime that flatters  In the night, no control Through the wall something's breaking…</div>
<div class="tg-footer">👁️ 5.65K · <a href="https://t.me/SBoxxx/18917" target="_blank">📅 01:41 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18916">
<div class="tg-post-header">📌 پیام #26</div>
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
<div class="tg-footer">👁️ 5.36K · <a href="https://t.me/SBoxxx/18916" target="_blank">📅 01:40 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18915">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">Audio</div>
  <div class="tg-doc-extra"></div>
</div>
<a href="https://t.me/SBoxxx/18915" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">دقت کرده اید شبهایمان شده جشنواره خبر و روزها همه خواب هستند؟!</div>
<div class="tg-footer">👁️ 5.34K · <a href="https://t.me/SBoxxx/18915" target="_blank">📅 01:33 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18914">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">دقت کرده اید شبهایمان شده جشنواره خبر و روزها همه خواب هستند؟!</div>
<div class="tg-footer">👁️ 5.32K · <a href="https://t.me/SBoxxx/18914" target="_blank">📅 01:32 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18913">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">ایران اعلام کرد که یک پهپاد MQ-9 ریپر متعلق به ایالات متحده را در نزدیکی بوشهر سرنگون کرده است.</div>
<div class="tg-footer">👁️ 5.36K · <a href="https://t.me/SBoxxx/18913" target="_blank">📅 01:29 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18912">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">از کرامات شیخ ما یکی این است
شیره را خورد و گفت شیرین است</div>
<div class="tg-footer">👁️ 5.35K · <a href="https://t.me/SBoxxx/18912" target="_blank">📅 01:26 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18911">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">سرلشکر رضایی:
هم اسمی و هم عملی دیگر چیزی به‌نام تفاهم‌نامهٔ اسلام‌آباد وجود ندارد</div>
<div class="tg-footer">👁️ 5.43K · <a href="https://t.me/SBoxxx/18911" target="_blank">📅 01:25 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18910">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">اینفانتینو: فیفا تأمین‌کننده رسمی شادی برای بشریت است.  ترامپ: مگر اینکه تیم شما ببازد.</div>
<div class="tg-footer">👁️ 5.3K · <a href="https://t.me/SBoxxx/18910" target="_blank">📅 01:20 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18909">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">اینفانتینو: فیفا تأمین‌کننده رسمی شادی برای بشریت است.
ترامپ: مگر اینکه تیم شما ببازد.</div>
<div class="tg-footer">👁️ 5.18K · <a href="https://t.me/SBoxxx/18909" target="_blank">📅 01:19 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18908">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">تسنیم حمله به یزد و لار را که فرمانداران شان تکذیب کرده بودند تایید کرد!</div>
<div class="tg-footer">👁️ 5.23K · <a href="https://t.me/SBoxxx/18908" target="_blank">📅 01:15 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18907">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">الجزیره : وقوع ۵ انفجار در شهر یزد، در مرکز کشور.</div>
<div class="tg-footer">👁️ 5.3K · <a href="https://t.me/SBoxxx/18907" target="_blank">📅 00:51 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18906">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">این توافق اساساً نوع مهندسی و طراحی اش به گونه ای است که هیچ وقت به صورت آشکار منجر به حل کامل و قاطع اختلافات نشود. عمداً بخش های زیادی به صورت خاکستری و ابرآلود باقی نگاه داشته شده تا همیشه بهانه ای بر زدن زیر میز وجود داشته باشد.  عین بلایی که سر ما تریدرها…</div>
<div class="tg-footer">👁️ 5.22K · <a href="https://t.me/SBoxxx/18906" target="_blank">📅 00:49 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18905">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">مهر:
موشک‌های آمریکا به مناطق شهر اهواز برخورد کردند</div>
<div class="tg-footer">👁️ 5.19K · <a href="https://t.me/SBoxxx/18905" target="_blank">📅 00:47 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18904">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">چی بود امضا کردند اینها؟!</div>
<div class="tg-footer">👁️ 5.15K · <a href="https://t.me/SBoxxx/18904" target="_blank">📅 00:46 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18903">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">Memorandum of Misunderstanding!</div>
<div class="tg-footer">👁️ 5.15K · <a href="https://t.me/SBoxxx/18903" target="_blank">📅 00:45 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18902">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">اخبار تاییدنشده از حمله موشکی به یزد!</div>
<div class="tg-footer">👁️ 5.17K · <a href="https://t.me/SBoxxx/18902" target="_blank">📅 00:45 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18901">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">شایعاتی تاییدنشده دال بر پیوستن اسراییل به آمریکا در حملات چند روز آینده منتشر شده.</div>
<div class="tg-footer">👁️ 5.24K · <a href="https://t.me/SBoxxx/18901" target="_blank">📅 00:41 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18900">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">شایعاتی تاییدنشده دال بر پیوستن اسراییل به آمریکا در حملات چند روز آینده منتشر شده.</div>
<div class="tg-footer">👁️ 5.25K · <a href="https://t.me/SBoxxx/18900" target="_blank">📅 00:39 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18899">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">سپاه پاسداران:
اگر آمریکا به پل‌ها و زیرساخت‌ها حمله کند، ما دارایی‌های صنعتی و فناوری اطلاعات شرکت‌های آمریکایی را که در منطقه حضور دارند، نابود خواهیم کرد.</div>
<div class="tg-footer">👁️ 5.22K · <a href="https://t.me/SBoxxx/18899" target="_blank">📅 00:26 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18898">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">حملات ایالات متحده به لار، استان فارس، ایران.
گزارش‌ها حاکی از آن است که این حملات با انفجارهای ثانویه همراه بوده‌اند.</div>
<div class="tg-footer">👁️ 5.21K · <a href="https://t.me/SBoxxx/18898" target="_blank">📅 00:22 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18897">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">رونن کوهن، رئیس هیئت مشورتی کمیته وزارتی اسرائیل در امور شین بت:
«پس از ترور رهبر ایران، یک سوء قصد علیه یکی از اعضای خانواده نخست وزیر نتانیاهو انجام شد که در آخرین لحظه  خنثی شد.»</div>
<div class="tg-footer">👁️ 5.3K · <a href="https://t.me/SBoxxx/18897" target="_blank">📅 00:15 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18896">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">همین مانده بود که یک راس دوزاری  دستمال کش  بیاید گه خوری علی دایی را بکند!
ای مگس عرصه سیمرغ نه جولانگه توست...</div>
<div class="tg-footer">👁️ 5.6K · <a href="https://t.me/SBoxxx/18896" target="_blank">📅 23:04 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18895">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">محسن رضایی: اگر حملات آمریکا تا دو سه روز دیگر ادامه پیدا کند وارد مرحله تهاجمی کامل خواهیم شد
ایران در مرحله تهاجمی کامل دیگر به مقابله به مثل اکتفا نخواهد کرد و هیچ مرز سیاسی در مقابل تهاجم ایران امنیت نخواهد داشت.</div>
<div class="tg-footer">👁️ 5.4K · <a href="https://t.me/SBoxxx/18895" target="_blank">📅 22:43 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18894">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KWpXAIcUT9rLUoCpxcJ2FZueMzYClATdJEu7L6i5VKhNA9P6Gii4FEAkaH1cHNk5cntkYFplhKlDF7G-sWO9K1D56RZLwfcKwKU-Nok6Nc1Uv-1jSGGkBVPprTBZVFXeaKthlti_ZLAtM3hV_m-QuBGNaAmLhKUqRk5PAw3GpuxE7yUI5DL4FjS0twnSMclZqDsqeGYdIe-WUgCqHgcrBXtXFHxhJTO8-xpYM3G1f8mGPmTjf9Gu8ch62tOrcJM-XdLmYuJWcCjQSRNdUzWOVGEF03xK412CfrX2wGdNFaW166TO9jQRf2NKkDJjUc3aQ_c2CZO1yzbYAbX1xh4x9A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یادداشتی خواندنی از یورونیوز درباره ایزنکوت و حزب ش.  لینک</div>
<div class="tg-footer">👁️ 5.25K · <a href="https://t.me/SBoxxx/18894" target="_blank">📅 22:23 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18893">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">داده فروشی به سبک ترامپ!  شرکت رسانه‌ای خانواده ترامپ، Trump Media & Technology Group (TMTG)، قصد دارد سرویس جدیدی با نام Truth API راه‌اندازی کند که به مؤسسات مالی، صندوق‌های سرمایه‌گذاری و شرکت‌های معاملاتی امکان می‌دهد پست‌های منتشرشده در شبکه اجتماعی Truth…</div>
<div class="tg-footer">👁️ 5.17K · <a href="https://t.me/SBoxxx/18893" target="_blank">📅 21:45 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18892">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">تحقیقات CFTC درباره اپراتور تله‌پرامپتر ترامپ به اتهام استفاده از اطلاعات محرمانه  گابریل پرز (Gabriel Perez)، اپراتور تله‌پرامپتر که مسئول کنترل متن سخنرانی‌ها و هماهنگی نمایش آن برای دونالد ترامپ است، تحت تحقیق کمیسیون معاملات آتی کالاهای آمریکا (CFTC) قرار…</div>
<div class="tg-footer">👁️ 5.78K · <a href="https://t.me/SBoxxx/18892" target="_blank">📅 21:44 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18890">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/XwHcIO2zz5x44TsVk8LZewrLTTsL5kVCY9giBbS1ZV8VsaWN_3qlhqX725-T2uvDweFuPXIyA8uRab4buH0LmZRWUZD7o3DgmM3mxdMV2GPTCB1HpULuxWxzMJAd3bIdbjpTW0OCZ9EzXe68Ikp5bA2-bmREJYEby5n_hYTH7og7Vs-kXdY58_XFOlW8MfoFEz7cVGPnd7O6LzdtSvr4GbGzioSzk_J_gogL1GqkHYFF1UGHqF9tW0exciIXyc0y-9y-361iWeNKoPEquGDC-R32R95hnmKg8cbM0pImHj8_zfyZtupCgdmIx0mhAi5rbwjEfidT4tNl0NeTel82JQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/VGNjTwiymY68_UndEJLW6as_qNsty2290xyOYHsQQrJ8BEAGRLHUkfSnHUF7oDXc8J7UzsFA9WNJlQCPC4oNhCqvLCJt3tizTi27t4y7iIbKM2BnqHgQaaKBW8j3gzfgfSUSXo9CLgDd1WjZvgjgrFBxuG-UeHE0_X3M0_wIZHxo20n5CDb1r7oBZQ3zG8L1b7SmrOKztL5KiJsWkEtPmgvr4E4lsKYSft8Vl5wKs5TVhHZzSxKfS_fEw4XvXW-5Mvq5hgXN7plEYh1ZSEtK3uzy7UZRmlYs9xG1XF6I9OerH5dSGxyJJnioG189MC8hY-TwGpeqJo5_ZCAQXZT8Gw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">همبستگی عجیبی میان شمار اعضای کانال با قیمت دلار به ریال وجود دارد!
شاید چون اینجا هیچ گاه خوش بینی متوهمانه برای مذاکرات به خواننده تزریق نشده است.</div>
<div class="tg-footer">👁️ 5K · <a href="https://t.me/SBoxxx/18890" target="_blank">📅 20:59 · 26 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>

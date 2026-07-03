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
<img src="https://cdn4.telesco.pe/file/gO1DGM0xjkVNCgfyuXaA5oR_iy_nyCfP0q1AiuoR530jo7GTejCLCUWafjB0yjheb19ZogcFrJma6Mw4xTdxIRSZrnlZ5ZiOIodnKYgRotj1xzExZYvOaYPK0QAGz-zAz9Xr-LmcXKafrQ0v64k0CVcMZA-fA-Nu6ptRr6eUJ0rZa_5IRHkBa2xFhPqc5x5U8VQQ_naPlZXiC0AXRhkRcOEttZ_ixKlMTnwemUAjBsKUqsNaHfEvcuPSBaLFGYYVUYD66j28vQxiL1xJuyMqgx-uOOEIaqBkRtWNsVfMOOvb3AyV63LkZ8VTIw7WJYDzn3IvVdCoJ-0Eexb0WdMIEg.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 🚩سرخ تایمز🚩</h1>
<p>@sorkhtimes • 👥 21.5K عضو</p>
<a href="https://t.me/sorkhtimes" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ﷽ورزشی نویس پرسپولیس👤🎗️«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس.⛔رسانه سرخ تایمز مسئولیتی در قبال تبلیغات ندارد.</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-12 13:09:54</div>
<hr>

<div class="tg-post" id="msg-134834">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">❗️
❗️
درحالیکه استقلال ، سپاهان و تراکتور تمرینات شون برای فصل جدید شروع کردن اما خبری از شروع تمرینات پرسپولیس نه تنها نیست بلکه حتی تکلیف نیمکت هم مشخص نیست!
🔴
🔴
حدادی داره کاری میکنه تا دلمون برای درویش تنگ بشه!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق…</div>
<div class="tg-footer">👁️ 850 · <a href="https://t.me/SorkhTimes/134834" target="_blank">📅 12:57 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134833">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">🔴
🔴
فووووری؛ رضا شکاری از پرسپولیس جدا شد و به زودی‌ لژیونر میشه. تیم جدید شکاری در قاره آسیا خواهد بود/ورزش سه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 943 · <a href="https://t.me/SorkhTimes/134833" target="_blank">📅 12:56 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134832">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">✔️
✔️
✔️
مدیران پرسپولیس پروژه فسخ بازیکنان را کلید زدند
❌
از عملکرد امید عالیشاه اصلا راضی نبودند ؛ ومرتضی پورعلی‌ گنجی، میلاد سرلک ، رضا شکاری ، تیوی بیفوما و  دنیل گرا  بازیکنانی هستند که نامشان در لیست سیاه باشگاه دیده می‌شود. مدیران پرسپولیس چند گزینه جوان…</div>
<div class="tg-footer">👁️ 972 · <a href="https://t.me/SorkhTimes/134832" target="_blank">📅 12:55 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134831">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">❌
❌
خداداد عزیزی: ایرادات و مشکلاتی در پرسپولیس هست که این تیم را دچار بحران و حاشیه کرده است و تا حالا این مدل کار کردن رو ندیده بودم. در صورتی که در تراکتور همه چیز با یک زنگ به زنوزی حل میشد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.28K · <a href="https://t.me/SorkhTimes/134831" target="_blank">📅 12:50 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134830">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">🔴
🔴
خداداد عزیزی:علیرضا دبیر اصرار می‌کرد برم پرسپولیس
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.37K · <a href="https://t.me/SorkhTimes/134830" target="_blank">📅 12:47 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134829">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">🔴
🔴
دلیل ناراحتی اسکوچیچ از پرسپولیس اینه که قرار بوده باشگاه بهش پیش‌پرداخت بده که تا الان این اتفاق نیوفتاده/فوتبالی
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.49K · <a href="https://t.me/SorkhTimes/134829" target="_blank">📅 12:45 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134828">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">❗️
❗️
عصبانیت اسکوچیچ از باشگاه
🔴
🔴
پس از مذاکره اولیه و سپس حضوری در استانبول، اسکوچیچ در انتظار ارسال قرارداد بود که این موضوع از سوی باشگاه چند بار به تاخیر افتاد و باعث دلخوری اسکوچیچ شد. هنوز هم به شکلی عجیب و سوال برانگیز در ۲۴ ساعت گذشته این اتفاق رخ نداده…</div>
<div class="tg-footer">👁️ 1.49K · <a href="https://t.me/SorkhTimes/134828" target="_blank">📅 12:44 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134827">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">🚨
🚨
🚨
🚨
#فووووووووووووری
🔻
احمد نوراللهی در آستانه بازگشت به پرسپولیس/خبرورزشی
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.52K · <a href="https://t.me/SorkhTimes/134827" target="_blank">📅 12:43 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134826">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">❌
❌
#فوری
🗣
حضور کسری طاهری در پرسپولیس منتفی شد / ورزش سه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 2.73K · <a href="https://t.me/SorkhTimes/134826" target="_blank">📅 11:40 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134825">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">✅
با اعلام ترانسفر مارکت محمد قربانی بازیکن آزاد اعلام‌ شد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.03K · <a href="https://t.me/SorkhTimes/134825" target="_blank">📅 11:17 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134824">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">❌
❌
خداداد عزیزی :
🔴
🔴
اسکوچیچ سه هفته منتظر قرارداد با پرسپولیس بود خیلی هم راغب بود بیاد اما هر سری از طرف باشگاه بهش جواب درست نمیدادن
🔴
🔴
ما حتی برنامه ریزی نقل و انتقالات خوب کرده بودیم با چند بازیکن شاخص هم در حال توافق بودیم که همه چی بهم ریخت، داشتیم…</div>
<div class="tg-footer">👁️ 3.15K · <a href="https://t.me/SorkhTimes/134824" target="_blank">📅 11:09 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134823">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">✅
🏆
برنامه کامل بازی‌های ۱/۱۶ نهایی جام جهانی
🇿🇦
آفریقا جنوبی - کانادا
🇨🇦
🇧🇷
برزیل - ژاپن
🇯🇵
🇳🇱
هلند - مراکش
🇲🇦
🇺🇸
آمریکا - بوسنی
🇧🇦
🇳🇴
نروژ - ساحل عاج
🇮🇪
🇫🇷
فرانسه - سوئد
🇸🇪
🇩🇪
آلمان - پاراگوئه
🇵🇾
🇲🇽
مکزیک - اکوادور
🇪🇨
🇧🇪
بلژیک - سنگال
🇸🇳
🇪🇸
اسپانیا - اتریش…</div>
<div class="tg-footer">👁️ 3.18K · <a href="https://t.me/SorkhTimes/134823" target="_blank">📅 11:04 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134822">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NsNhXBbCzsqaPtBUO_oVyfgs_JsbrY0o2uyJllD0guDWeuj6suW04DoOJRSuL5s1DkFiM3aNty7RyVaCUCH_Tim33-fnmMQ_MaocFSRSQHlBKVaUiXslflkvIW9BvN8W4lLFTJQCwY76nZYMKBhPrBBsjwAE2b5VKrqTm-zyQ3plDGS_zYxmGvlqyxHppk5-W13kvM6LV0JppNQk9yK0d-gnvymKH1gZWGNcnkLTlp8k4MPS5bIVVYWNg5YeiH6YjUUNN-ve3k7dGdGs1UpXbdYQlbMR4ON5wKKN-xJmMhJio2Gvga2ffygzVXieSzkTNKIuSrCwljdaOFeFLhF_fA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
🔴
پرتغال موفق شد کرواسی رو شکست بده و در مرحله یک هشتم به مصاف اسپانیا میره.اونم فقط 72 ساعت دیگه ..تیما دیشب بازی کردن
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.36K · <a href="https://t.me/SorkhTimes/134822" target="_blank">📅 10:42 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134821">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">❗️
❗️
خداداد عزیزی:
🔴
تا جایی که من میدانم اسکوچیچ به پرسپولیس نخواهد رفت و حضورش در این تیم منتفی است!
✅
وقتی سخنگوی باشگاه، ناکاربلد باشه و دانش کافی برای جلوگیری از حواشی رو نداشته باشه، باید هم خداداد عزیزی در نقش سخنگو بیاد درمورد مسایل تیم ما صحبت کنه.…</div>
<div class="tg-footer">👁️ 3.38K · <a href="https://t.me/SorkhTimes/134821" target="_blank">📅 10:38 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134820">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">❌
رونالدو فقط انقدر تنها 25 گل با 1000 گله شدن خودش فاصله داره
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.36K · <a href="https://t.me/SorkhTimes/134820" target="_blank">📅 10:36 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134819">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">لحظه‌به‌لحظه با نبض واقعی مسابقه</div>
<div class="tg-footer">👁️ 4.81K · <a href="https://t.me/SorkhTimes/134819" target="_blank">📅 01:06 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134818">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">مزیت عضویت در کانال ما
با عضویت در این کانال:
فوتبال را حرفه‌ای‌تر دنبال می‌کنید
از تحلیل‌های سطحی فاصله می‌گیرید
درک بهتری از تاکتیک و جریان مسابقه پیدا می‌کنید
همیشه یک قدم جلوتر از بقیه خواهید بود
اینجا فقط خبر نمی‌دهیم؛
اینجا فوتبال را کالبدشکافی می‌کنیم.
https://t.me/+hhwRu0jTAzswN2Nk
https://t.me/+hhwRu0jTAzswN2Nk</div>
<div class="tg-footer">👁️ 4.82K · <a href="https://t.me/SorkhTimes/134818" target="_blank">📅 01:06 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134817">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/c2ngbMOdIvVWpT2Q3znEiaHYsseQDFFQjYFoguQX17I3OKGIeWERflhuWwp1WpZSFYPDJSXCMN00ITuvysFisL5yAK5EicDuJptj_z8X_lmkVk0zguB9oiEtUqw_iEQcNHXaHrvxRQsCio2nlInP1eGz_WvGHbOiDHYakZjhM7ASbe9-xxHKijQV2YWgBjMo2f5Tw0kB7NAXzR6Kl2dYY1q1zJ5TFW4EbRAwCyNYdveiEmYmbWG-TAcZYD23T_b8o4ZdOK55LPS4Elx8z0iiUWToq1a9N3bZfLK-qTx4l30taYxEADm-gBVCC860v6q0hUca6oawaDE6EoG6IJGoqQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">◀️
استوری خیلی سنگین رسول خطیبی
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.05K · <a href="https://t.me/SorkhTimes/134817" target="_blank">📅 00:47 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134816">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ul2pmuBSYFrnezAgN-LB3vo4qrM5Q-Jd54jpBn-Z3B5hAIqYzH1vZFqpRKhtzN6T63PbqwEy1AUpPwvbxv30E2WgViIBwd_cBgMOik4AUKwS7o97ZeZnxvvb3yw1yO6koWn6sn4H2B98E1M7f5LyTa-qPJ6HqYHII-izaB9sIARNijYFt3Yu_FKZVQbt_tKJ3ZPI2wVJd_x-8fwBGYTtef1cZv6WiQIcNf4g0SKuOVdGwHOMWWkswcCQ2RqwK5j0qsd-sZvg3oPIV9PdpEKG4u6zRaPVXWKYGy3Y8ftBYIY7M2L68qp6V9NKDKLFCcbY-W3A3847AFBL0YZ3zJ4vLg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
ادعای رسانه مصری؛ ژاوی گزینه هدایت تیم ملی ایران!
🔴
رسانه‌‌ Smashi Sports مصر، در گزارشی مدعی شد که "ژاوی هرناندز" سرمـربی سابق بارسلونا، در فهرست گزینه‌ های فدراسیون‌فوتبال ایران برای سرمربیگری تیم‌ملی قرار دارد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.29K · <a href="https://t.me/SorkhTimes/134816" target="_blank">📅 23:39 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134815">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">🔴
#جام_جهانی
🏆
کنداکتور آنلاین جام جهانی امشب و بامداد فردا مرحله یک شانزدهم نهایی:
🇪🇸
اسپانیا
🆚
اتریش
🇦🇹
⏱
ساعت ۲۲:۳۰
🇵🇹
پرتغال
🆚
کرواسی
🇭🇷
⏱
ساعت ۲:۳۰
🇨🇭
سوئیس
🆚
الجزایر
🇩🇿
⏱
ساعت ۶:۳۰
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.24K · <a href="https://t.me/SorkhTimes/134815" target="_blank">📅 23:28 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134814">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">❌
زنوزی: هدف خداداد از صحبت با پرسپولیس فقط خوشحال کردنشون بوده وگرنه میدونستم نمیره پرسپولیس
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.29K · <a href="https://t.me/SorkhTimes/134814" target="_blank">📅 22:58 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134813">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">✅
✅
واکنش زنوزی به انتقال اسکوچیچ به پرسپولیس: اسکوچیچ مربی بزرگیه و تونست تراکتور رو قهرمان کنه اما او بدون ابزار قهرمانی نمیتونه در یک تیم معمولی دوباره قهرمان بشه!!!!!!
🔴
🔴
پ.ن آقای حدادی آقایون بانک شهر بهتون بربخورههههه!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار…</div>
<div class="tg-footer">👁️ 5.27K · <a href="https://t.me/SorkhTimes/134813" target="_blank">📅 22:57 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134812">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">🔴
زنوزی: طرفداران تراکتور از گالاتاسرای و فنرباغچه بیشتر هستند
😆
😆
😆
در ترکیه ابتدا طرفدار تراکتور هستند سپس تیم شهرشان. خیابان‌های تبریز شلوغ‌تر از خیابان‌های استانبول بود. امکان نداره طرفدار گالاتاسرای، فنرباغچه و بشیکتاش بیشتر از تراکتور باشه
🎗️
«سرخ تایمز»…</div>
<div class="tg-footer">👁️ 5.33K · <a href="https://t.me/SorkhTimes/134812" target="_blank">📅 22:29 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134811">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">🚨
فوووری   حجت کریمی، عضو هیات رییسه فدراسیون: اگر رای گل‌گهر رد شود، پرسپولیس و چادرملو با هم بازی می‌کنند و برنده آن به مصاف گل‌گهر می‌رود تا سهمیه آسیایی مشخص شود. اگر هم رای تایید شود، گل گهر راهی آسیا خواهد شد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق…</div>
<div class="tg-footer">👁️ 5.25K · <a href="https://t.me/SorkhTimes/134811" target="_blank">📅 22:10 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134810">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">🔴
زنوزی: طرفداران تراکتور از گالاتاسرای و فنرباغچه بیشتر هستند
😆
😆
😆
در ترکیه ابتدا طرفدار تراکتور هستند سپس تیم شهرشان. خیابان‌های تبریز شلوغ‌تر از خیابان‌های استانبول بود. امکان نداره طرفدار گالاتاسرای، فنرباغچه و بشیکتاش بیشتر از تراکتور باشه
🎗️
«سرخ تایمز»…</div>
<div class="tg-footer">👁️ 5.25K · <a href="https://t.me/SorkhTimes/134810" target="_blank">📅 22:09 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134809">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">🔴
زنوزی: طرفداران تراکتور از گالاتاسرای و فنرباغچه بیشتر هستند
😆
😆
😆
در ترکیه ابتدا طرفدار تراکتور هستند سپس تیم شهرشان. خیابان‌های تبریز شلوغ‌تر از خیابان‌های استانبول بود. امکان نداره طرفدار گالاتاسرای، فنرباغچه و بشیکتاش بیشتر از تراکتور باشه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.24K · <a href="https://t.me/SorkhTimes/134809" target="_blank">📅 22:05 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134808">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">❗️
صفحه رسمی باشگاه دهوک عراق عکس ها و ویدیویی هایی از معارفه یحیی گل محمدی و دستیارش محمد عسگری را در پست و استوری به اشتراک گذاشته که نشان می دهد مراسم معارفه ویژه ای جذب پرافتخارترین مربی ایران در جام های سراسری برگزار شده است.
🎗️
«سرخ تایمز» دریچه ای تازه…</div>
<div class="tg-footer">👁️ 5.23K · <a href="https://t.me/SorkhTimes/134808" target="_blank">📅 21:50 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134806">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">💥
❌
با مالیاتش میشه ۲.۵ میلیون دلار معادل ۵۰۰ میلیارد تومن/نیم همت
🫦
بدون احتساب اپشن ها
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس 𝓣𝓲𝓶𝓮
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.16K · <a href="https://t.me/SorkhTimes/134806" target="_blank">📅 21:42 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134805">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">⭕️
🔴
افشاگری تازه؛ ایجنت اسکوچیچ و درخواست جنجالی ۱.۸ میلیون دلاری
🔴
شنیده‌ها حاکی از آن است که ایجنت دراگان اسکوچیچ به دنبال عقد قراردادی ۱.۸ میلیون دلاری برای این سرمربی است؛ رقمی که فاصله قابل‌توجهی با قراردادهای قبلی او در تراکتور دارد.
❗️
اسکوچیچ در فصل…</div>
<div class="tg-footer">👁️ 5.15K · <a href="https://t.me/SorkhTimes/134805" target="_blank">📅 21:40 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134804">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">🚨
🚨
🚨
فووووووووووووری
🚨
بانک شهر حضور اسکوچیچ در پرسپولیس رو مصوب کرده و امشب یا فردا باید قرارداد برای امضا به این مربی ارسال بشه/ فارس
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.19K · <a href="https://t.me/SorkhTimes/134804" target="_blank">📅 21:38 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134803">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">1xbet.apk</div>
  <div class="tg-doc-extra">54.1 MB</div>
</div>
<a href="https://t.me/SorkhTimes/134803" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">📲
جدیدترین آپدیت اندروید 1XBET
✅
ورود / ثبت نام از اپلیکیشن
🎖
بزرگترین اسپانسر رسمی لالیگا
🔵
حتما
بدون فیلترشکن
از اپلیکیشن استفاده کنید
🎁
هنگام ثبت نام کد هدیه 130 دلاری vipfarsi را وارد کنید.</div>
<div class="tg-footer">👁️ 5.02K · <a href="https://t.me/SorkhTimes/134803" target="_blank">📅 21:36 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134802">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/E0_Vb73F-jZ_BTunPRtq582TJiFhhBbZedpRiPmClxAnAwVgyfTNdl86T5-7RnnzqtpjgbjuawgOldY38ed7EdeWzBa-t9xyRa2Azd2VRn0AN4Beqr5HnJnDBCGAbf7NwkMnR1As2Z1JC25L4Fegm9gYjrsZvFsa1rk0Tv-1ZMB9afRd1lArDZ6Ne1H8ZRZGqWdKj3rt6JSowN0eNaJQY_YFZqZ8__OHb90Oap2a6Hzbiztg2WaP9PnW5tC7wDXsOmfC0EBw9TWvc7QxH6F4E8OWaG1DcPd83FC_hIN5GIVyJQp5HXWeJEy0UftFGU803UfA5mHRWK-VNjYiTppLiA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">1️⃣
وان‌ ایکس بت برترین و خفن ترین سایت پیش بینی بین المللی که به کاربران ایرانی خدمات میدهد
🔥
🎁
با افتتاح حساب در 1XBET از طریق کد هدیه
vipfarsi
تا سقف ۱۳۰ درصد به شما کاربران گرانقدر بازپرداخت هدیه میدهد
🔔
آموزش ثبت نام، واریز و برداشت
🟦
آدرس وان‌ایکس‌بت:
🌐
Link :
1XBET.COM
🌐
Link :
1XBET.COM
🔑
برای ورود به سایت از وی پی ان (فیلترشکن) کشور های آسیایی یا کانادا یا ترکیه استفاده کنید.
➖
➖
➖
➖
➖
➖
➖
➖
🌐
Channel :
@iran1xbet_official</div>
<div class="tg-footer">👁️ 4.98K · <a href="https://t.me/SorkhTimes/134802" target="_blank">📅 21:36 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134801">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">🚨
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 4.81K · <a href="https://t.me/SorkhTimes/134801" target="_blank">📅 21:34 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134800">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">🚨
🚨
🚨
فووووووووووووری
🚨
بانک شهر حضور اسکوچیچ در پرسپولیس رو مصوب کرده و امشب یا فردا باید قرارداد برای امضا به این مربی ارسال بشه/ فارس
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.84K · <a href="https://t.me/SorkhTimes/134800" target="_blank">📅 21:33 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134799">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">❌
فوتبالی : پاسخ مبهم دروژدک به دوراهی تراکتور - پرسپولیس
✅
مذاکره پرسپولیس با دراگان اسکوچیچ شایعات حضور احتمالی دروژدک در جمع قرمزهای تهران را ایجاد کرده و گفته می‌شود اسکوچیچ در صورت حضور در پرسپولیس، هموطن خود را هم به این تیم خواهد برد.
❗️
و در همین راستا…</div>
<div class="tg-footer">👁️ 4.99K · <a href="https://t.me/SorkhTimes/134799" target="_blank">📅 21:30 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134798">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">❗️
❗️
عصبانیت اسکوچیچ از باشگاه
🔴
🔴
پس از مذاکره اولیه و سپس حضوری در استانبول، اسکوچیچ در انتظار ارسال قرارداد بود که این موضوع از سوی باشگاه چند بار به تاخیر افتاد و باعث دلخوری اسکوچیچ شد. هنوز هم به شکلی عجیب و سوال برانگیز در ۲۴ ساعت گذشته این اتفاق رخ نداده…</div>
<div class="tg-footer">👁️ 4.91K · <a href="https://t.me/SorkhTimes/134798" target="_blank">📅 21:28 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134797">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">🔽
در جلسه هیات مدیره صحبت از پنج گزینه ایرانی و یک گزینه خارجی به عنوان الترناتیو اسکوچیج شده تا اگر جذب او به هر دلیل میسر نشد چه کنند
🖥
ممکن است درباره گزینه های خارجی دیگری هم در جلسات صحبت شده باشد.ما از اینکه نام،عملکرد،رزومه،زشت و زیبا و شرایط ۵ سر مربی…</div>
<div class="tg-footer">👁️ 4.95K · <a href="https://t.me/SorkhTimes/134797" target="_blank">📅 21:18 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134796">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/R8UoPrxa71R3-9twcYj_rvOHkbgsOa_uWHVYpl4fUAXlYHju--Xp6YtgAuf_0OqCe5iLXyj1MjJcJ-VR78WETWeZMi8VzBAqLJJRGY4khprC-j0ZC8ZubF9OUa92yrUTcg_U_tEUElboBQcAc_FJwi5HS1B2HZdC1iC42_2otp82rBMpx3lW0yx2u50C0DxvdwIx8UGDKhQAqHzonDeJxsGpgpSiS_F5l7iznyPOrMIMNsESyj_1wBCMyHBT3kNccPFhcJqAzO9QKG27zaGL3ZXyEFN6QXgnYVZseYUc1zRKDmR8m1asimjBZrvx3koTFRBrVeuFpKo-iyKQMJxqCg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
عارف آیمن بازیکنی که در دو فصل اخیر بسیار به پرسپولیس لینک شده بود؛ بالاخره بازیکن آزاد شد
❗️
موافق جذب این بازیکن مالزیایی هستید یا خیر؟!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.94K · <a href="https://t.me/SorkhTimes/134796" target="_blank">📅 21:15 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134795">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Y0-A_1X19Lb1k5L_Fh8dkIzvFcZUI1c8ttWIHOHUxOnAO6KpypDIPvDLVHQVuyIgKPNIqLU2nloK-vyCrS59rG5wPTHE_XrBTED7vaf6Hrrz4m6EMnViQGTkZ8UjF8Cm00z3X2KZyLQG-1s4x98pAe9NnTvRvl4dGqP9zAi5zifxlP4biLKR_nNtIz8iJMMv9ygRo27b2HTIpP8Y3NjY-NOmT_SkIoAQZ3rQX53ZqaOQPDIbFo5wR18MCFVsyHvW1kGAIfbKcZKMF_sc6xuKiiiOCsBlYOIv_X9ToMjaKxWsey21A_fi4vo2iTUtOlH104QsK_CPHHT4KAH_m0C2HQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
عارف آیمن بازیکنی که در دو فصل اخیر بسیار به پرسپولیس لینک شده بود؛ بالاخره بازیکن آزاد شد
❗️
موافق جذب این بازیکن مالزیایی هستید یا خیر؟!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.93K · <a href="https://t.me/SorkhTimes/134795" target="_blank">📅 21:15 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134794">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">❗️
❗️
خداداد عزیزی:
🔴
تا جایی که من میدانم اسکوچیچ به پرسپولیس نخواهد رفت و حضورش در این تیم منتفی است!
✅
وقتی سخنگوی باشگاه، ناکاربلد باشه و دانش کافی برای جلوگیری از حواشی رو نداشته باشه، باید هم خداداد عزیزی در نقش سخنگو بیاد درمورد مسایل تیم ما صحبت کنه.…</div>
<div class="tg-footer">👁️ 5.01K · <a href="https://t.me/SorkhTimes/134794" target="_blank">📅 20:16 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134793">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">❗️
❗️
خداداد عزیزی:
🔴
تا جایی که من میدانم اسکوچیچ به پرسپولیس نخواهد رفت و حضورش در این تیم منتفی است!
✅
وقتی سخنگوی باشگاه، ناکاربلد باشه و دانش کافی برای جلوگیری از حواشی رو نداشته باشه، باید هم خداداد عزیزی در نقش سخنگو بیاد درمورد مسایل تیم ما صحبت کنه.…</div>
<div class="tg-footer">👁️ 5.12K · <a href="https://t.me/SorkhTimes/134793" target="_blank">📅 19:27 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134792">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">✅
منتفی پشت منتفی..کنسل پشت کنسل  ..نمی‌دونم باشگاه داره چی کار می‌کنه .نه بازیکن گرفتیم .نه سرمربی داریم ....بیاین جواب ملیون ها هوادار و بدین
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.15K · <a href="https://t.me/SorkhTimes/134792" target="_blank">📅 19:24 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134791">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">✅
منتفی پشت منتفی..کنسل پشت کنسل  ..نمی‌دونم باشگاه داره چی کار می‌کنه .نه بازیکن گرفتیم .نه سرمربی داریم ....بیاین جواب ملیون ها هوادار و بدین
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.1K · <a href="https://t.me/SorkhTimes/134791" target="_blank">📅 19:19 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134790">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">❗️
❗️
خداداد عزیزی:
🔴
تا جایی که من میدانم اسکوچیچ به پرسپولیس نخواهد رفت و حضورش در این تیم منتفی است!
✅
وقتی سخنگوی باشگاه، ناکاربلد باشه و دانش کافی برای جلوگیری از حواشی رو نداشته باشه، باید هم خداداد عزیزی در نقش سخنگو بیاد درمورد مسایل تیم ما صحبت کنه.…</div>
<div class="tg-footer">👁️ 5.07K · <a href="https://t.me/SorkhTimes/134790" target="_blank">📅 19:18 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134789">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">❗️
❗️
خداداد عزیزی:
🔴
تا جایی که من میدانم اسکوچیچ به پرسپولیس نخواهد رفت و حضورش در این تیم منتفی است!
✅
وقتی سخنگوی باشگاه، ناکاربلد باشه و دانش کافی برای جلوگیری از حواشی رو نداشته باشه، باید هم خداداد عزیزی در نقش سخنگو بیاد درمورد مسایل تیم ما صحبت کنه.…</div>
<div class="tg-footer">👁️ 5.2K · <a href="https://t.me/SorkhTimes/134789" target="_blank">📅 19:17 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134788">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">✅
خداداد عزیزی: حضورم در پرسپولیس منتفی شد و در تراکتور می‌مانم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.27K · <a href="https://t.me/SorkhTimes/134788" target="_blank">📅 19:16 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134787">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">✅
✅
سعید اخباری کاری رو کرد که طی ۵ ۶ فصل اخیر لیگ برتر هیچ مربی انجام نداده بود
🔴
آسیایی کردن یک تیم غیر از تیم های پرسپولیس،  استقلال ، تراکتور ، سپاهان و فولاد
🔴
آخرین بار یحیی گل محمدی پدیده رو آسیایی کرده بود
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق…</div>
<div class="tg-footer">👁️ 5.33K · <a href="https://t.me/SorkhTimes/134787" target="_blank">📅 17:55 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134786">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromPulseGate</strong></div>
<div class="tg-text">🔰
سرویس اقتصادی
🔰
یک ماهه
25 گیگ 220T کاربر نامحدود
30 گیگ 280T کاربر نامحدود
35 گیگ 320T کاربر نامحدود
55 گیگ 420T کاربر نامحدود
100 گیگ 600T کاربر نامحدود
دوماهه
50 گیگ
380T تومن کاربر نامحدود
70 گیگ 450T تومن کاربر نامحدود
150 گیگ 700T تومن کاربر نامحدود
200 گیگ 750T تومن کاربر نامحدود
سه ماهه:
120 گیگ 680T تومن کاربر نامحدود
160 گیگ 730T تومن کاربر نامحدود
230 گیگ 800T تومن کاربر نامحدود
320 گیگ 950T تومن کاربر نامحدود
400 گیگ 1.1T تومن کاربر نامحدود
🛜
مناسب برای تمام سایت ها و اپ ها ،ظرفیت اتصال نامحدود
جهت خرید از پیوی =>
@Winstn_Churchill</div>
<div class="tg-footer">👁️ 5.21K · <a href="https://t.me/SorkhTimes/134786" target="_blank">📅 17:33 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134785">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">🚨
🚨
🚨
🚨
قدوسی: برخی منابع ما تاکید دارند قرارداد با اسکوچیچ امضا هم شده و حالا دنبال تخفیف و برخی مسائل هستند
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.31K · <a href="https://t.me/SorkhTimes/134785" target="_blank">📅 17:09 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134784">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">🔴
🔴
عادل‌فردوسی‌پور: تمام توافقات لازم انجام شده؛ دراگان اسکوچیچ سرمربی  پرسپولیس خواهد شد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.38K · <a href="https://t.me/SorkhTimes/134784" target="_blank">📅 17:08 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134783">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">✅
✅
فوووووووووووووووووری
🔴
🔴
فرهیختگان: در صورت پیوستن اسکوچیچ به پرسپولیس هلیلویچ و دروژدک دو بازیکن خارجی پرسپولیسی خواهند شد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.41K · <a href="https://t.me/SorkhTimes/134783" target="_blank">📅 17:02 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134782">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bx9UzpYT-p4iSuVy3jqcjuj8GvitjhMounH6BZP9jgL50rlLRHV-AIXAAFGqKWdRjyf02X8pt_7plQybhwtV1o3aN2bdLElySULFzPW7WprHLkVpaMUA82kjzf_AYjnvKzz0eSQ0LFKp7D_GvKAuY4iA54-TW2ul-nkoWBDDN4o-bLceaZkEpLuPrtxlr4GErFLq0TdudEnKhfoE5vTC90tCaR6tKk6OUFlcdHuTFLXw63NlAStFmiIuw32AlvAR64TZH8NxajrViwLW2GjhvcYT19PF3juWtqqgGmjl6A2N3_UHb4fOAzPvOTkb-wAPm4bZ77yDYRiPT3izMuOrKA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
✅
صحبت های جنجالی سوشا مکانی:
🔖
🔖
علیرضا بیرانوند اسمش علیرضا نیست و این آدم اسمش محمد صفر بیرانوند بود و تا 12 سالگی شناسنامه نداشت چون در محله‌ای که زندگی می‌کرد که شناسنامه نداده بودن، بعدش کلی پول به پسر عموش داد تا براش شناسنامه جعلی جور کنه و سنش رو هم اشتباه زده و الان با یک اسم و هویت جعلی زندگی میکنه و با همین ترفند سربازیش رو عقب انداخته
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.49K · <a href="https://t.me/SorkhTimes/134782" target="_blank">📅 16:14 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134780">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">❗️
یاسین سلمانی پس از ۱ سال و ۴ ماه در ترکیب اصلی پرسپولیس قرار گرفت
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.34K · <a href="https://t.me/SorkhTimes/134780" target="_blank">📅 15:32 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134779">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">melbet.apk</div>
  <div class="tg-doc-extra">52.1 MB</div>
</div>
<a href="https://t.me/SorkhTimes/134779" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">✈️
اپلیکیشن MelBet
🥇
🎁
کد هدیه 100 دلاری:
Sport100
🔒
برای تعیین رمز ورود حداقل از 8 کاراکتر و حروف بزرگ و کوچک انگلیسی و اعداد انگلیسی استفاده کنید، مانند Hamid120
🇮🇷
برای تغییر زبان برنامه، زبان موبایل خود را تغییر دهید.
✅
ورود به اپلیکیشن بدون فیلترشکن</div>
<div class="tg-footer">👁️ 5.27K · <a href="https://t.me/SorkhTimes/134779" target="_blank">📅 15:16 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134778">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/u17BJjfrg-yH4h4q1WuiRHBB-_EDSHSleWQ-mJl8GkAoFqVnNihZhugi-4TZTliWPT9ku3-9H7cZ-atM6vEHDb961XHc-CVxs9nmXF49V_WewaseQuT33NmfaRmwd4EjOgnCOOJNL1VvXrczqb5_c7Y49WJJrmOQN2aDmwM64dJlFdEOuRCUaSLcZdp0QYL__KsvOVlDZwfLNbXc7z49y6QKB0KcDzXcP0DLfiI1LRweJITnwHyc1e3Qt1VKZW16uFbaCqoB9NaMd7sMax09H6yuKdt2Ku6dXeZhQKdL4BMecUJWfhTVmPxFVJsmn503uoZSs7W8jF5PziuSe-UQJg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
55 درصد از علاقه‌مندان به فوتبال، فقط 4 سال یکبار شرط میبندن!
حالا چرا جام جهانی
❓
خیلی از نتایج تابلو و قابل حدسه
💯
مافیا که کارش دستکاری کردن نتایجه، زورش به جام‌جهانی نمیرسه و نتایج واقعیه
👀
به دلیل تعداد زیاد بازی ها، دستت بازه و کنترل ریسک و سرمایه آسونه!
🔽
🔼
💡
کافیه یه سایت معتبر پیدا کنی که شارژ کردنش آسون باشه و بدونی پولت امن میمونه، MelBet اسپانسر رسمی جام جهانی، همونیه که دنبالشی!
برای ورود به سایت فیلترشکن خود را خاموش کنید
🆕
Link
🔜
MelBet1.net
✅
🆕
Link
🔜
MelBet1.net
✅</div>
<div class="tg-footer">👁️ 5.42K · <a href="https://t.me/SorkhTimes/134778" target="_blank">📅 15:16 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134777">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">#نظر_شخصی | #شفاف_سازی
📌
این وسط ممکنه یکسری ها بخان از آب گلالود ماهی بگیرن و به نفع گزینه های خودشون شمشیر بزنن ولی موضع من مشخصه
🚩
من حالم از یحیی و هرچی مربی ایرانی بهم میخوره اسم مربی ایرانی میاد بدنم کهیر میزنه،و هیچوقت هم از اینکه پشت درویش درآومدم…</div>
<div class="tg-footer">👁️ 5.32K · <a href="https://t.me/SorkhTimes/134777" target="_blank">📅 15:08 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134776">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">🔴
🔴
مهدی رحمتی :از امیر قلعه‌نویی تعجب میکنم، اولین چیزی که او به من گفت، این بود که به هیچ‌کس هیچ قولی نده، اما خود او قول صعود داد.
🔴
🔴
اولین هدف آن ها صعود از گروه بود اما اتفاق نیوفتاد، پس بیایید عذرخواهی کنید، تاج و قلعه نویی باید حداقل از مردم عذرخواهی…</div>
<div class="tg-footer">👁️ 5.72K · <a href="https://t.me/SorkhTimes/134776" target="_blank">📅 14:23 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134775">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">✅
🏆
برنامه کامل بازی‌های ۱/۱۶ نهایی جام جهانی
🇿🇦
آفریقا جنوبی - کانادا
🇨🇦
🇧🇷
برزیل - ژاپن
🇯🇵
🇳🇱
هلند - مراکش
🇲🇦
🇺🇸
آمریکا - بوسنی
🇧🇦
🇳🇴
نروژ - ساحل عاج
🇮🇪
🇫🇷
فرانسه - سوئد
🇸🇪
🇩🇪
آلمان - پاراگوئه
🇵🇾
🇲🇽
مکزیک - اکوادور
🇪🇨
🇧🇪
بلژیک - سنگال
🇸🇳
🇪🇸
اسپانیا - اتریش…</div>
<div class="tg-footer">👁️ 5.69K · <a href="https://t.me/SorkhTimes/134775" target="_blank">📅 14:19 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134774">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">✅
محمد نصرتی درباره حضور دنیس اکرت در جام جهانی: آقای قلعه‌نویی، با دعوت از اکرت در حق یکسری بازیکن جوان اجحاف کرد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.65K · <a href="https://t.me/SorkhTimes/134774" target="_blank">📅 13:44 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134772">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/V5hjptPEz1q2RN8TjJbkd7w-rUeXQDwHUg4ZAbdoW6PCoWpMPCRzwRgu_OUk0cKdZ7MWKT3JV4l0uVwrOMz1bGytiraMJ2Vyqld5MBLKWBmzbU164k8G1NlUbBQg8DQMUYoWIzeq-YzEHlyO2VE8gwjhB1T8Rif4CRXntGtO1OcE0cewtv85J1ONWdl_HEQ3dKZH200R-Fl0XfKdp8w_650Jc1SJZwPKnhkkUxiiv_HFU767xp0JiLL-8hnOopkaq8NfGO9ge2CjPXfXYruDnCfm-7utZYNgVPsbGLN1f1IS6A0fH_m2sAwZXNbH-tiCwybJLAwiEugc2SgNUHENqQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
ماجرا وقتی عجیب میشه که بدونیم سانل کونیویچ دستیار اول اسکوچیچ در تراکتور دیروز با یک تیم اسلوونیایی قرارداد بست !
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.73K · <a href="https://t.me/SorkhTimes/134772" target="_blank">📅 12:57 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134771">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">⛔️
⚠️
گوساله! گوساله هایی که نیم فصل با هرچی اوسمار بگه، اوسمار نیارید تجمع میکنیم کیر زدید به تیم مادر تیم رو گاییدید
◀️
اینقدر گاب نباشید آدم پرستا،هدف باید موفقیت پرسپولیس باشه فرد مهم نیست
◀️
یه مشت رسانه تخمی دارن تیمو به گوه میکشن باشگاه باید همه شونو تخته کنه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
𝓣𝓲𝓶𝓮
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.57K · <a href="https://t.me/SorkhTimes/134771" target="_blank">📅 12:52 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134770">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">🔴
◀️
باشگاه پرسپولیس درآمد و سود امسال از برند و لوگوی خود (منهای پول اسپانسر و‌ مالک) را 771 میلیارد تومان اعلام کرد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.61K · <a href="https://t.me/SorkhTimes/134770" target="_blank">📅 12:48 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134769">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">#نظر_شخصی
📌
دوستان من نظر شخصیم میگم ممکنه خیلی ها موافق یا مخالف صحبت های من باشن که عقیده همه برام محترمه
📌
از دید من اقای اسکوچیچ مربی بسیار خوبیه و بنظرم باهاش میتونیم نتیجه بگیریم، اما چنتا نکته هست که منو نگران میکنه
📌
مورد اول:اسکوچیچ نشون داده قدرت…</div>
<div class="tg-footer">👁️ 5.68K · <a href="https://t.me/SorkhTimes/134769" target="_blank">📅 12:19 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134768">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">⭕️
🔴
افشاگری تازه؛ ایجنت اسکوچیچ و درخواست جنجالی ۱.۸ میلیون دلاری
🔴
شنیده‌ها حاکی از آن است که ایجنت دراگان اسکوچیچ به دنبال عقد قراردادی ۱.۸ میلیون دلاری برای این سرمربی است؛ رقمی که فاصله قابل‌توجهی با قراردادهای قبلی او در تراکتور دارد.
❗️
اسکوچیچ در فصل…</div>
<div class="tg-footer">👁️ 5.65K · <a href="https://t.me/SorkhTimes/134768" target="_blank">📅 12:14 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134766">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">🤩
#اختصاصی_سرخ_تایمز | #فوری
🤫
🏅
به گزارش رسانه «سرخ تایمز» حدادی شخصا میخاد با امید عالیشا،میلاد سراک،رضا شکاری،مرتضی پورعلی گنجی،دنیل گرا و تیوی بیفوما فسخ کنه.
❌
حالا باید ببینیم بانک شهر برای فسخ و آوردن بازیکن جایگزین بودجه میده یا نه
🎗️
«سرخ تایمز» دریچه…</div>
<div class="tg-footer">👁️ 5.63K · <a href="https://t.me/SorkhTimes/134766" target="_blank">📅 11:47 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134765">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e78b91b0d6.mp4?token=fcxd_rcBTu5IFmFohjARV_L857BRfL0tbRlhzUnmOuDQAOiHRoZrIXLI_PLVlGWgweYbFZAL6uCAiHvl8AY7w0QZm03JDu-58CR-h2e0BxInJ--0-LbFi2_XJU2WL00tRFHbr-uh-nFKzaGMl52q5oONV9OvEGiKyWsp1n9DCo05rQDCiQzvf6wC7mo1VnKfbaRllPA20bc0rq4I4pf0ybBv4YaoBEMQEPpJ7TDWGd5v-iav6mBQE90e-zBrY3dFKpqdkwB6BcUJMNZoEvV60UWo06IWJjxiW2bVjXtQZoNq2DCFDEBgoqo_b5UZhypBMe5CB7g-LNHXSQyZu512jiT5_F3vYhN9L94lGBFeocbmOrZBVP6ncz8-4vMj87UYeJehpWxw2Pi-S98BwbvQcHWdh8XhaoC42xdyuddNYgsgt1WySpjvJToXOn8fyNiefgYXLSmDQtXirypOwgW0EnzS4-91TF1QLGxjZIVpCZkyvCDjMIwAGoEz8VQJaymAGDJR5lBt_YI_tMkduUpGo9Eh85CLyyf4hbryYvhMeJz1-cR7eSoci2eaNgpOVLJn4DTGyuLX7xjyh_1Am6okKt7z5uzs3NzMoczBzAAQeF8KJ0EuLW8CvD744ZmYshK3dRm1yQyrfkl5YUuUfWKZ4D4m1mhjCkmHDM7mkcHHP1E" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e78b91b0d6.mp4?token=fcxd_rcBTu5IFmFohjARV_L857BRfL0tbRlhzUnmOuDQAOiHRoZrIXLI_PLVlGWgweYbFZAL6uCAiHvl8AY7w0QZm03JDu-58CR-h2e0BxInJ--0-LbFi2_XJU2WL00tRFHbr-uh-nFKzaGMl52q5oONV9OvEGiKyWsp1n9DCo05rQDCiQzvf6wC7mo1VnKfbaRllPA20bc0rq4I4pf0ybBv4YaoBEMQEPpJ7TDWGd5v-iav6mBQE90e-zBrY3dFKpqdkwB6BcUJMNZoEvV60UWo06IWJjxiW2bVjXtQZoNq2DCFDEBgoqo_b5UZhypBMe5CB7g-LNHXSQyZu512jiT5_F3vYhN9L94lGBFeocbmOrZBVP6ncz8-4vMj87UYeJehpWxw2Pi-S98BwbvQcHWdh8XhaoC42xdyuddNYgsgt1WySpjvJToXOn8fyNiefgYXLSmDQtXirypOwgW0EnzS4-91TF1QLGxjZIVpCZkyvCDjMIwAGoEz8VQJaymAGDJR5lBt_YI_tMkduUpGo9Eh85CLyyf4hbryYvhMeJz1-cR7eSoci2eaNgpOVLJn4DTGyuLX7xjyh_1Am6okKt7z5uzs3NzMoczBzAAQeF8KJ0EuLW8CvD744ZmYshK3dRm1yQyrfkl5YUuUfWKZ4D4m1mhjCkmHDM7mkcHHP1E" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❗️
درخواست عجیییییییب هواداران پرسپولیس از علیرضا بیرانوند
🔴
«برگرد پرسپولیس»
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.59K · <a href="https://t.me/SorkhTimes/134765" target="_blank">📅 11:42 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134764">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">✅
🏆
برنامه کامل بازی‌های ۱/۱۶ نهایی جام جهانی
🇿🇦
آفریقا جنوبی - کانادا
🇨🇦
🇧🇷
برزیل - ژاپن
🇯🇵
🇳🇱
هلند - مراکش
🇲🇦
🇺🇸
آمریکا - بوسنی
🇧🇦
🇳🇴
نروژ - ساحل عاج
🇮🇪
🇫🇷
فرانسه - سوئد
🇸🇪
🇩🇪
آلمان - پاراگوئه
🇵🇾
🇲🇽
مکزیک - اکوادور
🇪🇨
🇧🇪
بلژیک - سنگال
🇸🇳
🇪🇸
اسپانیا - اتریش…</div>
<div class="tg-footer">👁️ 5.71K · <a href="https://t.me/SorkhTimes/134764" target="_blank">📅 11:25 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134763">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">🚨
🚨
🚨
🚨
محمدحسین میثاقی: دراگان اسکوچیچ با عقد قراردادی دوساله سرمربی پرسپولیس شد. اسکوچیچ هم اکنون ترکیه است و به زودی میاد ایران!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.78K · <a href="https://t.me/SorkhTimes/134763" target="_blank">📅 11:12 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134762">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">⭕️
🔴
افشاگری تازه؛ ایجنت اسکوچیچ و درخواست جنجالی ۱.۸ میلیون دلاری
🔴
شنیده‌ها حاکی از آن است که ایجنت دراگان اسکوچیچ به دنبال عقد قراردادی
۱.۸ میلیون دلاری
برای این سرمربی است؛ رقمی که فاصله قابل‌توجهی با قراردادهای قبلی او در تراکتور دارد.
❗️
اسکوچیچ در فصل قهرمانی با تراکتور قراردادی
۷۰۰ هزار دلار
داشت،همچین قرارداد فصل  قبل او حدود
۱.۳ میلیون دلار
عنوان شده است.
❗️
از سوی دیگر، در حالی که هنوز توافق نهایی حاصل نشده، گفته می‌شود اتاق فکر آقای سردبیر از همین حالا مشغول برنامه‌ریزی و بستن تیم برای فصل آینده است.
❗️
همچنین مراجع ذی ربط به دلیل مسائل امنیتی به باشگاه توصیه کردن از جذب اسکوچیچ صرف نظر کنند
❗️
اگر این ادعاها صحت داشته باشد، روزهای پرحاشیه‌ای در انتظار باشگاه خواهد بود
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.05K · <a href="https://t.me/SorkhTimes/134762" target="_blank">📅 10:28 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134761">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 5.81K · <a href="https://t.me/SorkhTimes/134761" target="_blank">📅 10:26 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134760">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">✅
✅
فوووووووووووووووووری
🔴
🔴
فرهیختگان: در صورت پیوستن اسکوچیچ به پرسپولیس هلیلویچ و دروژدک دو بازیکن خارجی پرسپولیسی خواهند شد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.05K · <a href="https://t.me/SorkhTimes/134760" target="_blank">📅 10:18 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134759">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">🔴
🔴
واکنش یوسفی هوادار پرسپولیس به شایعات پخش شده در خصوص کمک برای خرید بازیکن یا سرمربی:
❌
با هیچ ارتباطی با مدیرای تیم ندارم
❌
نه بازیکن میخرم نه دخالت میکنم
⛔️
به دروغ نویسان هم باج نمی‌دهم!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس…</div>
<div class="tg-footer">👁️ 5.86K · <a href="https://t.me/SorkhTimes/134759" target="_blank">📅 09:16 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134758">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">❗️
رسمی؛ باشگاه های اماراتی از جذب بازیکن و سرمربی ایرانی در فصل آینده لیگ ادنوک منع شدند و تمامی بازیکنان ایرانی این لیگ ها باید به ایران بازگردند/ورزش سه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.96K · <a href="https://t.me/SorkhTimes/134758" target="_blank">📅 09:08 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134757">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/R-Rn0H2IMRbC1OOkS0Kzs5SSFNiOrvqM9NsZkQknHNhn_ew3UrbdVj-zAy5aGDB0SyxkJ4nFxcwpvxnoigO7xP4eggBgf0iDAAYwpy2JPlWfIkydyuWda0nb4hrGEAYH-BOGqOXOw1-1iPF5AKXoiarPV6yhBZ1YAuCukgOInrMhQ0IdS5FKOanXG84AJHhi7jEfFtyEXIVjvYNByKnGd7hmnY5KZJaJONlxK_ddQPH4_Tf-J4VPKo5YqKgYsipVKnI9Vr1CnR1hQr9ZWRrw2TvRY6BlOzPdA_YVVoK2LnKBcoP0N0Hf4Cnt4YxX6n79zkba239DcpVESGOkzG40jg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
صبحتون بخیر ارتش سرخ
🚩
✨
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.86K · <a href="https://t.me/SorkhTimes/134757" target="_blank">📅 09:08 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134756">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">فوتبال فقط دویدن ۲۲ نفر دنبال توپ نیست؛ جنگ افکار مربی‌هاست! اگر می‌خوای بدونی پشت پرده تصمیمات پپ گواردیولا یا کارلو آنچلوتی تو دقایق حساس چیه، جای درستی اومدی.
در [لایو تیپ]، ما بازی‌ها رو در لحظه آنالیز می‌کنیم:
📊
بررسی فرمیشن‌ها و تغییرات سیستم در جریان بازی
🎯
آنالیز تعویض‌های طلایی و تاثیر اون‌ها
🔥
بررسی نقاط کور دفاعی و فضاسازی مهاجمان
⚡️
آمار زنده و تاثیرگذار که هیچ گزارشگری به شما نمی‌گه!
اگر فوتبال رو با مغزت تماشا می‌کنی نه فقط با چشمت، جای شما اینجاست:
👇
ورود به جمع تحلیل‌گران و فوتبال‌فهم‌ها:
🔗
https://t.me/+hhwRu0jTAzswN2Nk
🔗
https://t.me/+hhwRu0jTAzswN2Nk</div>
<div class="tg-footer">👁️ 6.11K · <a href="https://t.me/SorkhTimes/134756" target="_blank">📅 00:56 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134755">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">🔴
سنگال گل اول و به بلژیک زد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.13K · <a href="https://t.me/SorkhTimes/134755" target="_blank">📅 00:45 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134754">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">🚨
🚨
🚨
🚨
#فووووووووووووری
🔻
احمد نوراللهی در آستانه بازگشت به پرسپولیس/خبرورزشی
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.5K · <a href="https://t.me/SorkhTimes/134754" target="_blank">📅 00:44 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134752">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">🚨
🚨
🚨
🚨
محمدحسین میثاقی: دراگان اسکوچیچ با عقد قراردادی دوساله سرمربی پرسپولیس شد. اسکوچیچ هم اکنون ترکیه است و به زودی میاد ایران!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.44K · <a href="https://t.me/SorkhTimes/134752" target="_blank">📅 00:24 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134751">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">🚨
🚨
🚨
🚨
اسکوچیچ امضا کرده و الان رسما سرمربی پرسپولیسه/طاهرخانی
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.39K · <a href="https://t.me/SorkhTimes/134751" target="_blank">📅 00:06 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134750">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">🚨
🚨
🚨
هوادار متمول پرسپولیس به مدیریت گفته 3 تا بازیکن شاخص براتون میگیرم و پیگیر اینم هست افشین پیروانی به تیم برگرده / فرهیختگان
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.32K · <a href="https://t.me/SorkhTimes/134750" target="_blank">📅 00:02 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134749">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">❗️
انگلیس از کنگو گل خورد
😐
🔴
چه جام جهانی سمی ایه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.22K · <a href="https://t.me/SorkhTimes/134749" target="_blank">📅 00:00 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134747">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">❌
بدرود کاپیتان دوست داشتنی ..کاپیشاه هر جا هستی موافق باشی
🤝
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.27K · <a href="https://t.me/SorkhTimes/134747" target="_blank">📅 23:39 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134746">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b9366cf9e2.mp4?token=RNdOIvMZ9ugBOlqy_FtzeBviUdazNy_fyjCzO0EdW9hb1qvKok3_U1cNKRixI8xoVVeO0aBy0Pho8HagYVCRXHCFiL7JPTeI56LrTzVO2aSPMtNl7kmV8JE_3avo9Sk753TMXrKyemvmkjPhyhYIwnLVbZHGjRNtkpAntl1QTTlSLE8wM2YypAVxHfL713-7LZhK-UTEYIxbjh4I72hLvxjHQCX1NdmEhdbwTJH0pekd4OshsSVAL2cGK3OIDicJ5EBK23ox3C0nzPTGkmeHXfqTpeA3R2oegtP6cVlv1_cWruZvb-Y7s-WMbXUy8yp4DzWsGsPHypSTjXrAeV2o6U0gDl95iem0umYLdMCUof9hszMEd8tjm1LzwdODCe_eABkiP3iPQTsEArhIyb4Nfs_PLhd_YSy_OS1dLDlPmf4PQgMict_6wepCLp7JZ6HKFQHAPUuF3piUhnDRiqjZMXnJ_GJwEpJaHByjaENcxpJBQOCJJAyWS36mcRyYkAuprdb3jr7vwJmQ8WqBtkVE-YGdqFzED0dATyqKXXv3DGTtK-U1d6Bd42J3mLMj0J1ALnC1ulV4det1oQE-2yLIcvhhuH9L3q6D9x4immPiuqv58zH1SAaUAjOuqbdh5JnERBOGULfouu5Wvy2_jamAd9SuXNZFkWhzYPI5kOw7XD8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b9366cf9e2.mp4?token=RNdOIvMZ9ugBOlqy_FtzeBviUdazNy_fyjCzO0EdW9hb1qvKok3_U1cNKRixI8xoVVeO0aBy0Pho8HagYVCRXHCFiL7JPTeI56LrTzVO2aSPMtNl7kmV8JE_3avo9Sk753TMXrKyemvmkjPhyhYIwnLVbZHGjRNtkpAntl1QTTlSLE8wM2YypAVxHfL713-7LZhK-UTEYIxbjh4I72hLvxjHQCX1NdmEhdbwTJH0pekd4OshsSVAL2cGK3OIDicJ5EBK23ox3C0nzPTGkmeHXfqTpeA3R2oegtP6cVlv1_cWruZvb-Y7s-WMbXUy8yp4DzWsGsPHypSTjXrAeV2o6U0gDl95iem0umYLdMCUof9hszMEd8tjm1LzwdODCe_eABkiP3iPQTsEArhIyb4Nfs_PLhd_YSy_OS1dLDlPmf4PQgMict_6wepCLp7JZ6HKFQHAPUuF3piUhnDRiqjZMXnJ_GJwEpJaHByjaENcxpJBQOCJJAyWS36mcRyYkAuprdb3jr7vwJmQ8WqBtkVE-YGdqFzED0dATyqKXXv3DGTtK-U1d6Bd42J3mLMj0J1ALnC1ulV4det1oQE-2yLIcvhhuH9L3q6D9x4immPiuqv58zH1SAaUAjOuqbdh5JnERBOGULfouu5Wvy2_jamAd9SuXNZFkWhzYPI5kOw7XD8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
بدرود کاپیتان دوست داشتنی ..کاپیشاه هر جا هستی موافق باشی
🤝
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.17K · <a href="https://t.me/SorkhTimes/134746" target="_blank">📅 23:37 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134745">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">✅
✅
🚨
🚨
ایلنا: قرارداد شکاری و عالیشاه فسخ شد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6K · <a href="https://t.me/SorkhTimes/134745" target="_blank">📅 23:24 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134744">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">🤩
#اختصاصی_سرخ_تایمز | #فوری
🤫
🏅
به گزارش رسانه «سرخ تایمز» حدادی شخصا میخاد با امید عالیشا،میلاد سراک،رضا شکاری،مرتضی پورعلی گنجی،دنیل گرا و تیوی بیفوما فسخ کنه.
❌
حالا باید ببینیم بانک شهر برای فسخ و آوردن بازیکن جایگزین بودجه میده یا نه
🎗️
«سرخ تایمز» دریچه…</div>
<div class="tg-footer">👁️ 5.98K · <a href="https://t.me/SorkhTimes/134744" target="_blank">📅 23:19 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134743">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">🔖
عادل فردوسی‌پور : نکنه پس‌فردا صبح با سوییس بازی داریم ما خبر نداریم اینا خبر دارن که مراسم استقبال گذاشتن
🖥
این همه تعریف از استقبال و دستاوردسازی برای چیست؟داستان تغییری نمی‌کند، ما از مرحله گروهی جام جهانی ۴۸ تیمی حذف شدیم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.02K · <a href="https://t.me/SorkhTimes/134743" target="_blank">📅 23:15 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134742">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">❗️
❗️
🔴
شنیده ها:اسکو تا اخر شب رونمایی میشه بعدشم تیکدری
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.92K · <a href="https://t.me/SorkhTimes/134742" target="_blank">📅 22:52 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134741">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oNnQhDmjkV-_yAGcwKvOTdbrx32lu3VOTYCeJVvxJX0buO_hSclY5nvPL7UysTAYgBvE4OXcA-HRUs0z0PQ97ADjQmSryJF4-yEJY8GqUMaF9f6GRSDBceNZVFQbhe06VrwdSYRZ7GlsZYzBL37pIj8CrXmO6OEK2ThcxaKBaQuYJJzRKKIwnPxU69r9VGsy5jw8S4lipGKbMvksfqC6XzuhrEalCPcwjKKM-8GdUOSguPEFEBs7hLEOrrN16d3D597UNAMk43eckMAoaNtSg9U0Mgl0wsY9O_J_WTXacxxo8wrx0dqOUF-C3-oU7-r9Ku2mOM3XIKcwpwD7EvfMoQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❗️
تمرینات پرسپولیس احتمالا از روز ۱۵ تیر در ورزشگاه شهید کاظمی برگزار می‌شود
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.07K · <a href="https://t.me/SorkhTimes/134741" target="_blank">📅 22:50 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134740">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">💬
ادعای عجیب دبیرکل فدراسیون فوتبال؛ ممبینی:
🎙
چادرملو برنده شد اما ممکن است گل‌گهر به آسیا برود!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.09K · <a href="https://t.me/SorkhTimes/134740" target="_blank">📅 22:14 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134739">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">🚨
🚨
🚨
فرهیختگان: در اردوی نیم فصل پرسپولیس  اوسمار ویرا جلسات شبانه ای در قطر  در یکی از هتل های دوحه  با هوادار متمول با هماهنگی سروش رفیعی انجام داده که این  اتفاق باعث بی اعتمادی مسئولان باشگاه شده ؛ که خبر این جلسات به گوش بازیکنان هم رسیده و حواشی در رختکن…</div>
<div class="tg-footer">👁️ 6.12K · <a href="https://t.me/SorkhTimes/134739" target="_blank">📅 22:04 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134738">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BfIUUnm0u0Sr10095MWkXRaSbGSSrBRkR4rqFwAin0nBXJuKmaCFOF_ybDFBScp83aLkAsSd1tHpiCfz28bqhjdCdfNNehmJOVQPxyhGHi8A3y-EUHtAR5TyNu3mk_cN9Im4Hd1USY2j2qwOeGxy9uVqONJX2ZlvfPsnQ3Wssygdr1wpQDdlxascx71WFVr5jag7oXmVQmB_mVcRAK0UrORe-Ijne9qvjEZVaqAiqCw2VTaRZKpif10NooTMd9cRKRZO1Yf7OvJz3L3wZqoBXf-wpr6lMYyb6TbpL9KrT0CcRePYFX9RLNARV_NC32WFWuQ0QbYhbLmAWcePjbjVlA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
با اعلام ترانسفر مارکت؛
مجتبی فخریان به پر‌سپولیس بازگشت
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.02K · <a href="https://t.me/SorkhTimes/134738" target="_blank">📅 21:57 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134737">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">❌
🚨
🚨
🚨
فووووووووووووری
🚨
محمد مهدی نبی مدیر تیم ملی، هدایت ممبینی دبیرکل فدراسیون ، مهدی خراطی مدیر اجرایی تیم ملی، سیامک قلیچ خانی مدیر رسانه ای ، محسن معتمدی‌کیا مدیر روابط عمومی و یکی از آنالیزور های کادرفنی به همراه افسران أمنیتی تیم ملی موفق به دریافت ویزای…</div>
<div class="tg-footer">👁️ 5.89K · <a href="https://t.me/SorkhTimes/134737" target="_blank">📅 21:11 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134736">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">❗️
اوه اوه ...بیست دقیقه تا حذف انگلیس توسط کنگو
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.89K · <a href="https://t.me/SorkhTimes/134736" target="_blank">📅 21:10 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134735">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">❗️
انگلیس از کنگو گل خورد
😐
🔴
چه جام جهانی سمی ایه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.73K · <a href="https://t.me/SorkhTimes/134735" target="_blank">📅 21:06 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134734">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">‼️
دانیال مرادی، رئیس دپارتمان داوری: ۱۳ کمک داور و ۱۲ داور موفق نشدند آزمون هارا پاس کنند!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.75K · <a href="https://t.me/SorkhTimes/134734" target="_blank">📅 20:59 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134733">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bd9ed04d87.mp4?token=VVK5vhfCEgpkqZeekEPoCQPYMwGNapqXZqaiWdWIZuau9_ClKaYGnOMuzgpMawbieotjqJ-GiZtNILanJWX9TdLKqc22RVaA-bIbxzu0qYH0KQGaXez7DNVMAK5H8rD3XSUMUk-HbM1T6g0ACGUYLMiSI9JgvNBZOx97BbUWzE8dzm0lledSsl57AYqfwy6rWEW9BylKHd9B1yjm1Zqc7XnomCmuCj1U0vLA8tXnhoDKzH8zyIjD6dLnObIjkHoXakIihALOSku7qtoB5KSVaS54rJZ1HtTUGuSrtWS1C5ZY64TlCf0a6AAw9ZtJ5yyKLwq3KIrgmx2MY0ZIhENq84i-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bd9ed04d87.mp4?token=VVK5vhfCEgpkqZeekEPoCQPYMwGNapqXZqaiWdWIZuau9_ClKaYGnOMuzgpMawbieotjqJ-GiZtNILanJWX9TdLKqc22RVaA-bIbxzu0qYH0KQGaXez7DNVMAK5H8rD3XSUMUk-HbM1T6g0ACGUYLMiSI9JgvNBZOx97BbUWzE8dzm0lledSsl57AYqfwy6rWEW9BylKHd9B1yjm1Zqc7XnomCmuCj1U0vLA8tXnhoDKzH8zyIjD6dLnObIjkHoXakIihALOSku7qtoB5KSVaS54rJZ1HtTUGuSrtWS1C5ZY64TlCf0a6AAw9ZtJ5yyKLwq3KIrgmx2MY0ZIhENq84i-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">💬
ادعای عجیب دبیرکل فدراسیون فوتبال؛ ممبینی:
🎙
چادرملو برنده شد اما ممکن است گل‌گهر به آسیا برود!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.64K · <a href="https://t.me/SorkhTimes/134733" target="_blank">📅 20:53 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134732">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn5.telesco.pe/file/80f7520ba9.mp4?token=eav9sZl-Y7SJSJukqvX6ojjfGSxtXXPHy-36-z_c9JaLQ7CgW2hFM_5OMe9DmxbRtWEYuj_YgCz_1lFZjJInE3NKmjmziExZ6mfVBkdTAezwR29oyOPWuVtvdtvaDb4OwH5TpengUfzPVdxBroMEexkI1onhSVyboE6_e26wR9ZPOzzo4LNNSjhNoSrfpqLiAkVu5yrsxFSRyIq6R6fRsbX4aLrC30oaPbVvvJSoOBpbznlctO_1Q5qilrAonis3iGloUeyxxktVvVbNTI_sCED5EMkYwtfB41OurQrTmNcKL0hvxYRsNK2CVx4x1pE1QAD0cqRAKcTg21VzY8_OVw" type="video/mp4">
</video>
<br>
<a href="https://cdn5.telesco.pe/file/80f7520ba9.mp4?token=eav9sZl-Y7SJSJukqvX6ojjfGSxtXXPHy-36-z_c9JaLQ7CgW2hFM_5OMe9DmxbRtWEYuj_YgCz_1lFZjJInE3NKmjmziExZ6mfVBkdTAezwR29oyOPWuVtvdtvaDb4OwH5TpengUfzPVdxBroMEexkI1onhSVyboE6_e26wR9ZPOzzo4LNNSjhNoSrfpqLiAkVu5yrsxFSRyIq6R6fRsbX4aLrC30oaPbVvvJSoOBpbznlctO_1Q5qilrAonis3iGloUeyxxktVvVbNTI_sCED5EMkYwtfB41OurQrTmNcKL0hvxYRsNK2CVx4x1pE1QAD0cqRAKcTg21VzY8_OVw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
شاهکاری دیگر از فیروز کریمی: قلعه نویی 5 سانت رو تحمل کرد 10 سانت رو تحمل کرد ولی دیگه 30 سانت رو کجاش بذاره؟؟
😐
😆
😆
😆
😆
😆
😆
😆
😆
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.94K · <a href="https://t.me/SorkhTimes/134732" target="_blank">📅 20:50 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134731">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">🤩
#اختصاصی_سرخ_تایمز | #فوری
🤫
🏅
به گزارش رسانه «سرخ تایمز» حدادی شخصا میخاد با امید عالیشا،میلاد سراک،رضا شکاری،مرتضی پورعلی گنجی،دنیل گرا و تیوی بیفوما فسخ کنه.
❌
حالا باید ببینیم بانک شهر برای فسخ و آوردن بازیکن جایگزین بودجه میده یا نه
🎗️
«سرخ تایمز» دریچه…</div>
<div class="tg-footer">👁️ 5.33K · <a href="https://t.me/SorkhTimes/134731" target="_blank">📅 20:36 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134730">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-text">🔥
💵
اگه دوست دارین از بازی های
جام جهانی
یه سود تپل و درست حسابی به جیب بزنید حتما داخل چنل بت زیر عضوشید خفنه واقعا
☑️
🖥
JOIN
JOIN
JOIN
JOIN
JOIN
JOIN</div>
<div class="tg-footer">👁️ 4.94K · <a href="https://t.me/SorkhTimes/134730" target="_blank">📅 20:23 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134729">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Bf2A5FiJ31JocWf39T3RY1IoTK29BPRi65R7wcSiMbfIFykT49j3_dSHM47EFOcZZemu2CwCgYqqfyMqz_onbGSxWRLxCgPQtiFBGCEirI0QfMP_NTVeN9Rg-26kdhT_pXSrQ4cy7GNurV4ZlbSWZKRPOMq-rVIduzkfxTTKHG8aX8z3lZh5TdXKc1plOnICh-siQsBkwhaZdTnHNsYRCMtTFOlayqGMI0dQ7s8QrA7oPxL0uTvXvpmez3xpZcHN1nzJa431HuoNrdVGvDYUoRZxwjLWuGqe5kWke5M-Rqu4Ylg7evNlep9NlXZwgGpVXuXYZezbaPGSDn7UsoWnzg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هردو تیم گل میزنند_بله
Odd: 1.80
🛫
200میلیون
بستیم روی همین بازی اگه توم میخوای کلی از این آپشن های خفن ببندی (بدون ریسک) حتما عضو کانال VIPزیر شو
🛡
https://t.me/+6L9plEThEMk5YTJk
آمار روزانه 90 درصد برد
🔥
✅
با آنالیز حرفه‌ای و تخصصی که روی ، فرم ها انجام میدیم میتونید به سود میلیونی برسید
💵
💯
🆔
@ARON_TIP
@ARON_TIP
🆔
@ARON_TIP
@ARON_TIP</div>
<div class="tg-footer">👁️ 4.3K · <a href="https://t.me/SorkhTimes/134729" target="_blank">📅 20:23 · 10 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>

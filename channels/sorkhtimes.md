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
<img src="https://cdn4.telesco.pe/file/NM4LKm_TT35KGAKay00z_65i18_5thHJYeslnpWmcOV0QDSmhzbKvs7NDT4NbPQf2TRV-upzo-YgQO1mFYqZ29_mDhiNt3OMOlvDXweqzpYUdS_PrY2Ljp1zbo45cm-h_G5p9pDtJwNzzKesQHzndi02XONcjn8s62mV7k6xAaKKE3l37NoWLZeu9trezyaGissO60fq2DXsXZnGpBn3A3DZAkdpBJ6NGIxAU88Ii1zNeEN3gDBDotNf56VKgYZgb_U_jfOvS5al3nuy3VeI9AGRu-WqRBnb-yaUdePUlQHrhnL1_6aFrkrLwkP5rXHY15xw2surgsnMfBGLwsSw9Q.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 🚩سرخ تایمز🚩</h1>
<p>@sorkhtimes • 👥 21.5K عضو</p>
<a href="https://t.me/sorkhtimes" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ﷽ورزشی نویس پرسپولیس👤🎗️«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس.⛔رسانه سرخ تایمز مسئولیتی در قبال تبلیغات ندارد.</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-25 15:44:21</div>
<hr>

<div class="tg-post" id="msg-135944">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PlyL0fZuwzbkU5OSWGo9pRpp7vletPKJfroUnQcJZRhJ4hdo_Q1F68KvQtdMfMXntoh-odfsaSQwM0dJVVDIf2CDyk7JWS4dUeEECYLGfQ_j5aFQ5U6VN9Ok9n2BsnqvCFuQ8VlgjmW4rHl7E3wNSaTGJ1x61UQFVwXYT5naVvQ0BHvKOT8QObxCS4Hoh9FbPyQNnLc6rYfkFNTajFewLX2v4jBJ66xZKDZ4g2Auo7gXmR4Dsb6oU2lfoxTKArxS2fNoM4gyie2EtA_sHhptIOGJ-WiHODjJ8xDaeC4RXfdNQUTRJkHpIEYqSmPGDQT9OaO6hk2YS05YBhFlsTTqBg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
سامان قدوس؛ بمب بعدی پرسپولیس؟
🔴
🔴
ورزش سه: پرسپولیس برای جذب سامان قدوس هافبک ایرانی اتحاد کلباء امارات درخواست داده و این بازیکن در لیست خرید سرخپوشان قرار گرفته است.
🔴
🔴
قدوس که سابقه بازی در لیگ برتر انگلیس با برنتفورد و تیم ملی ایران را دارد، یکی از گزینه‌های جذاب پرسپولیس برای تقویت خط میانی محسوب می‌شود.
🔴
❌
باید دید مذاکرات پرسپولیس با ستاره کلباء به کجا می‌رسد و آیا شاهد یک انتقال بزرگ دیگر به جمع سرخ‌ها خواهیم بود.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.15K · <a href="https://t.me/SorkhTimes/135944" target="_blank">📅 15:33 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135943">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">✅
✅
عملکرد پویا پورعلی هافبک دفاعی جدید 30 ساله پرسپولیس در فصل گذشته لیگ برتر :
🔆
21 بازی ، 1 گل / نمره متریکا : 7/03
🔴
سابقه حضور در گل گهر، تراکتور، ملوان، ذوب آهن، فجر سپاسی، خونه به خونه، بادران، شهرداری جویبار
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.21K · <a href="https://t.me/SorkhTimes/135943" target="_blank">📅 15:32 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135941">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VWYtwiN0b3KhqR5T0634ktOI4xgWujj5qpsBFflM5TtwdbvJE1ySvhc4O6o-b-14qTSUXS5i0huDe7RYuQXxSRf7JNv7s54e9Pk_dSTcHOqONRVh9rd2YqcI6g2m0zkEAjtBm6hT5AiJnXtwE71OM7bGJgQ7EoyqF_dU41ucLqP5_hlFypVdc411QJmdnEp2lB7l7EPmkKB43R1hHGY7Mwp60qCHbgrfyIg7Gftk0k_fTV4lIXfxgbrRxO-aYf5knhLNORC-mf96gngSgU0J3VAD-0WuAGVNk2LCd7i-7t-gDMz0ZqTEec6RBJkRwzoi5wbMdxOAx9ouyfsVMQAt7A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔺
فیفا قضاوت دیدار فینال جام جهانی ۲۰۲۶ میان تیم‌های ملی اسپانیا و آرژانتین را به علیرضا فغانی سپرد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 2.13K · <a href="https://t.me/SorkhTimes/135941" target="_blank">📅 15:07 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135940">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pOBFoMmXOMNpDs4KD_EO3uov577IzDv47SURsnBvdWuETT64_QFAuvXzLruTyWiBmKVeHBt5q-lmo-U2Udl7zwZ2_Hm2jKldupRWmfDkt-U8DU12nhSLJiSlMOpokRUc4FdeD2hJfcDPkw750Xqm7aTq2kwF_ynuCPWVnCkfn19aFLVeIIB40lhnj3pqW53J-FcA-N54VCJa0FPs_8I81rQt-IY7Vt5e55Okvi70W5W8IeqPBIZcZx7fVmkMsfqYiwy2Hb8y_5QfC3j8xM3ZA5h4i6PJvkZhmPMC2rMJHl6fyjC-aH1Fb_Xpu0Gcu44py1CyhUxqfNfzIhKl3y88lw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
خریدهای لیگ‌برتری پرسپولیس تا به امروز:
مهدی‌تیکدری‌نژاد، سیدمجید عیدی، پوریا شهرآبادی، ابوالفضل جلالی، پوریا پورعلی؛ هر باشگاهی هفت سهمیه لیگ برتری و سه سهمیه بازیکن آزاد داره.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 2.4K · <a href="https://t.me/SorkhTimes/135940" target="_blank">📅 15:02 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135939">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from𝙷𝚊𝚓𝙼𝙰𝚑𝚍𝚒</strong></div>
<div class="tg-text">تو دور زمونه ای که فساد حرف اولو میزنه کسی که وظیفشو انجام میده باید قدردان خودشو پدر و مادرش بود...</div>
<div class="tg-footer">👁️ 2.4K · <a href="https://t.me/SorkhTimes/135939" target="_blank">📅 15:00 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135938">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded frompourya</strong></div>
<div class="tg-text">دیگه نمیتونی زحمات یکی رو بگا بدی خیلیا به وضیفشون عمل نمیکنن</div>
<div class="tg-footer">👁️ 2.58K · <a href="https://t.me/SorkhTimes/135938" target="_blank">📅 14:56 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135937">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">وظیفه اشه  دیگه دمت گرم نداره  مثه اینه مادر به بچه اش شیر بده بگیم دمت گرم مادر که به بچه تازه بدنیا اومده شیر میدی
😂</div>
<div class="tg-footer">👁️ 2.58K · <a href="https://t.me/SorkhTimes/135937" target="_blank">📅 14:55 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135936">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromVahidreza. Sadeghpour</strong></div>
<div class="tg-text">وظیفه اشه
دیگه دمت گرم نداره
مثه اینه مادر به بچه اش شیر بده بگیم دمت گرم مادر که به بچه تازه بدنیا اومده شیر میدی
😂</div>
<div class="tg-footer">👁️ 2.64K · <a href="https://t.me/SorkhTimes/135936" target="_blank">📅 14:53 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135935">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">دمت حدادی گرم که باج به شغال نمیدد</div>
<div class="tg-footer">👁️ 2.76K · <a href="https://t.me/SorkhTimes/135935" target="_blank">📅 14:50 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135934">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromHamed 65442</strong></div>
<div class="tg-text">دمت حدادی گرم که باج به شغال نمیدد</div>
<div class="tg-footer">👁️ 2.89K · <a href="https://t.me/SorkhTimes/135934" target="_blank">📅 14:45 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135933">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromHamed 65442</strong></div>
<div class="tg-text">دم بانک شهر گرم</div>
<div class="tg-footer">👁️ 2.88K · <a href="https://t.me/SorkhTimes/135933" target="_blank">📅 14:45 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135932">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">✔️
#تایید_خبراختصاصی | #اولین_رسانه
🚨
❤️
پوریا پورعلی با عقد قرارداد دو ساله به پرسپولیس پیوست
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس 𝓣𝓲𝓶𝓮
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.1K · <a href="https://t.me/SorkhTimes/135932" target="_blank">📅 14:42 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135931">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">❌
❌
🚨
شنیده ها: امروز احتمالا ۲ رونمایی خواهیم داشت
👀
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.06K · <a href="https://t.me/SorkhTimes/135931" target="_blank">📅 14:42 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135930">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">✅
بااعلام سایت ترانسفر مارکت؛ باشگاه پرسپولیس بابت رضایت‌نامه محمد مهدی زارع 800 هزار دلار به باشگاه اخمت گروژنی روسیه پرداخت کرده است.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.13K · <a href="https://t.me/SorkhTimes/135930" target="_blank">📅 14:40 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135929">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kx0yiA2WjRFn7dzHGvfpxv05_cSEGwSR4n8Vi3wPnNzyDF1Sgp0UbPlB9it5xpRlVFRDOrg_DLjG_Tctk1P33MqKNtAGjJvFLBV6-u7pQvT-UN7KahKcJ30fZsgS7XUI-7Vnj1X9N-rcZs63C-NNxSLNnMAxtB_FiDtnpY0EDzYYkVWHbXC982elg64KJr3ekeeUSys7_rXdoFj_L357LqK_U9kftRM1cjWKBXxnE0p0tlCdH15EmzQWF1fkUfR610m6aFAwke5S2Ifjoy0oJcLSSlhQhlhj8usrPrVE73cRoG7Z_RttBC5AMeGjuK6hs2_CKPqrP_fP28sChS_IzA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
بااعلام سایت ترانسفر مارکت؛ باشگاه پرسپولیس بابت رضایت‌نامه محمد مهدی زارع 800 هزار دلار به باشگاه اخمت گروژنی روسیه پرداخت کرده است.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.22K · <a href="https://t.me/SorkhTimes/135929" target="_blank">📅 14:38 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135928">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/atQSu6XTdFmhu-Wfb4Fl2Ei6CAvKGmxbLi0O769ZJC7IThho9K3ntie_kngI283hcBP8eM6WZsIjVm3bd1bNoqBL9clrHkTKVFwvFogao-G1MeNPe_CTMejIBI7_5sP8iaRYc6GoloQQNDsNQS_5GXhe91U0LBFp104-sm8HxT3ajxbly5FbYGzs_Supq2yEg-9Xuh--laDueMveiclwcee6KY3-oDCDGm6JR5F-T7sMRDAnAvvVP3fn9zvBYagGw3BMpJrWPEiQD5IdjZ5SOzb56qkfhjKtZjMoVNlk6hmowRVMGXg95iW1qF05vmVS2LxRDIpPE9LyP5Ga5WBUsA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🤩
#اختصاصی_سرخ_تایمز | #فوری
🤫
🏅
به گزارش رسانه «سرخ تایمز» مدیران باشگاه پرسپولیس با نظر مهدی تارتار با این چهار بازیکن وارد مذاکره شدند.
⬅️
مجید عیدی
⬅️
محمد قیرشی
⬅️
پوریا پورعلی
⬅️
پوریا شهرآبادی
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس…</div>
<div class="tg-footer">👁️ 3.28K · <a href="https://t.me/SorkhTimes/135928" target="_blank">📅 14:35 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135925">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">❌
❌
فوری از فارس:
🔴
انتقال پوریا پورعلی هافبک گل‌گهر به پرسپولیس تا چند ساعت آینده امضا میشه و به زودی رونمایی خواهد شد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.28K · <a href="https://t.me/SorkhTimes/135925" target="_blank">📅 14:32 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135924">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">✅
✅
شماره پیراهن خریدهای جدید پرسپولیس
🔴
مهدی تیکدری: شماره 11
🔴
مجید عیدی: شماره 20
🔴
ابوالفضل جلالی: شماره 33
🔴
پوریا شهرآبادی: شماره 21
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.68K · <a href="https://t.me/SorkhTimes/135924" target="_blank">📅 14:16 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135923">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">🔴
تمرین امروز سرخپوشان در سالن وزنه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.67K · <a href="https://t.me/SorkhTimes/135923" target="_blank">📅 14:14 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135922">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">#تایمز_توئیت
⚠️
تو این مملکت دستت رو عسل بکنی بزاری دهن طرف دستت رو گاز میگیرن، همین زارع رو نمیگرفتن به خدای احد واحد خار مادر باشگاه رو یکی میکردید وسط فصل….
‼️
نساجی برای ایری ۱.۲ میلیون دلار و برای طاهری ۱.۳ میلیون دلار میخاست
🎗️
«سرخ تایمز» دریچه ای تازه…</div>
<div class="tg-footer">👁️ 3.82K · <a href="https://t.me/SorkhTimes/135922" target="_blank">📅 14:07 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135921">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">✅
❤️
رسمی؛ محمدمهدی زارع به پرسپولیس پیوست
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.79K · <a href="https://t.me/SorkhTimes/135921" target="_blank">📅 14:06 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135919">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/veH7CoUcikUsjRg31RKE-wTtWzl9Q359YydH3pdGahlM-BsIxrbXpwpk9NajFhtG8WWUiIP9rWzCbTRr7QYIH8g9g-P8rqECuA08wCKGUVOU5Xo2fOzz9fqW0BMLD_v9iLz-PpeJjZM_Kmmh1LrEiSFSgDJrutoNd7GpQJ6fqGahjHlBkRFgET9_XZUSJG8cPaS4eC7ylSKk7mU3vGA02nB6-r1O6avM2Sl2BJ0pBN0t6M_KlDXapZK7yZ9TlJKWITHD9eiuqxvtt860c9xtVShaees4nIUMQwPjGqyy7YDPlDEZazJsQWv9Hp-dBdmv8USa-Y00nNLdpd7pOYlhzQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
❤️
رسمی؛
محمدمهدی زارع به پرسپولیس پیوست
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.79K · <a href="https://t.me/SorkhTimes/135919" target="_blank">📅 14:05 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135918">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">#تایمز_توئیت
⛔️
❌
با یه مشت دیونه زنجیری طرفیم، باشگاه هرکسی رو میخره یه عده هستن فقط بلندن گوه بخورن
‼️
قبلا میگفتن بانک شهر گداست پول نمیده الان رفتیم یکی از بهترین دفاع وسط های ایران رو خریدیم (زارع) یه عده دهنشون رو باز میکنن که با این پول میشد ایری و طاهری…</div>
<div class="tg-footer">👁️ 3.82K · <a href="https://t.me/SorkhTimes/135918" target="_blank">📅 14:04 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135917">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">#تایمز_توئیت
⛔️
❌
با یه مشت دیونه زنجیری طرفیم، باشگاه هرکسی رو میخره یه عده هستن فقط بلندن گوه بخورن
‼️
قبلا میگفتن بانک شهر گداست پول نمیده الان رفتیم یکی از بهترین دفاع وسط های ایران رو خریدیم (زارع) یه عده دهنشون رو باز میکنن که با این پول میشد ایری و طاهری رو خرید یکی نیست اخه کون گلابی اگر میشد مغز خر خوردن برن زارع رو بگیرن ؟! اصلا میشد تو بلدی بیا بکن یه عده فواره گوزو پر مدعا نشستن بیرون میگن لنگش کن
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
𝓣𝓲𝓶𝓮
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.91K · <a href="https://t.me/SorkhTimes/135917" target="_blank">📅 13:57 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135916">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">❗️
❗️
فرهیختگان : قرار بر این شده است که  باشگاه پرسپولیس قرارداد هافبک مورد علاقه تارتار پوریا پور علی را امشب نهایی کرده تا این بازیکن بتواند از فردا در کنار سرخپوشان تمرین کند
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.13K · <a href="https://t.me/SorkhTimes/135916" target="_blank">📅 13:45 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135915">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">❗️
فارس؛ پویا لطیفی‌فر هافبک گل‌گهر در لیست خرید تارتار قرار گرفت
😐
❌
پ.ن از گل گهر بکشید بیرون ناموسا
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.22K · <a href="https://t.me/SorkhTimes/135915" target="_blank">📅 13:43 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135914">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">❗️
❗️
محمدمهدی زارع در آستانه پرسپولیسی شدن!
⌛
انتقال محمدمهدی زارع ۹۹ درصد نهایی شده و فقط واریز مبلغ باقی مانده است؛ پس از انجام پرداخت، از این خرید به‌صورت رسمی رونمایی خواهد شد. //خرمی
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
…</div>
<div class="tg-footer">👁️ 4.95K · <a href="https://t.me/SorkhTimes/135914" target="_blank">📅 12:23 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135913">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">❗️
مهدی تارتار از مدیران پرسپولیس درخواست کرده با توجه به شانس کم پرسپولیس برای جذب ایری و زارع،اقدام به بازگرداندن مرتضی پورعلی‌گنجی به تمرینات تیم کنند.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.01K · <a href="https://t.me/SorkhTimes/135913" target="_blank">📅 12:23 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135912">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">❗️
تارتار شخصاً با زارع تماس گرفته و خواهان اومدنش شده؛ باشگاه هم میخواد از اخمت‌گروژنی تخفیف بگیره/فرهیختگان
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.04K · <a href="https://t.me/SorkhTimes/135912" target="_blank">📅 12:22 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135911">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">❗️
❗️
فووووووووری
❌
فرهیختگان : اگر میلاد محمدی با باشگاه تمدید نکنه ، مدیران باشگاه از مدافع چپ جوونی که با اون به توافق نهایی رسیده‌اند ، رونمایی خواهند کرد
🔴
گفته می‌شود تمام اقدامات نهایی خرید جدید تیم انجام شده و این انتقال برای نهایی شدن تنها به یک امضا…</div>
<div class="tg-footer">👁️ 5.64K · <a href="https://t.me/SorkhTimes/135911" target="_blank">📅 10:56 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135910">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">❌
❌
میلاد محمدی همچنان تمدید نکرده و اخبار قطعی شدنش کذبه اما توافق داشته/ایرنا
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.6K · <a href="https://t.me/SorkhTimes/135910" target="_blank">📅 10:53 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135909">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">❗️
تارتار شخصاً با زارع تماس گرفته و خواهان اومدنش شده؛ باشگاه هم میخواد از اخمت‌گروژنی تخفیف بگیره/فرهیختگان
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.61K · <a href="https://t.me/SorkhTimes/135909" target="_blank">📅 10:31 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135908">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">✅
✅
#فوووووووری از طاهرخانی :
🔴
زارع در آستانه پرسپولیسی شدن..کار تمومه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.61K · <a href="https://t.me/SorkhTimes/135908" target="_blank">📅 10:30 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135907">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">✅
✅
یه خبر نصف شبی فوری، شنیده ها:
🔴
برخی از کارشناسان حقوقی معتبر به باشگاه اطلاع دادن کسری طاهری میتونه برای پرسپولیس بازی کنه و باشگاه داره مجدد واسه جذبش تلاش میکنه.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.77K · <a href="https://t.me/SorkhTimes/135907" target="_blank">📅 09:55 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135906">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">🚨
احتمال گرفتن رضایت‌نامه قرضی زارع بیشتره
✍
قرمزآنلاین
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.68K · <a href="https://t.me/SorkhTimes/135906" target="_blank">📅 09:53 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135905">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">❗️
حدادی : پول اسکوچیچ رو میدم بازیکن با کیفیت میگیرم
😂
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.62K · <a href="https://t.me/SorkhTimes/135905" target="_blank">📅 09:49 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135904">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">✅
استانداری خوزستان:
🔴
پس از تهاجم دشمن تروریستی آمریکا به شهر اهواز خساراتی به منازل مسکونی اطراف وارد شده و شیشه برخی منازل شکسته شده است.
🔴
تاکنون این حملات تلفات جانی در پی نداشته است.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.63K · <a href="https://t.me/SorkhTimes/135904" target="_blank">📅 09:46 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135903">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/slfqBtQKUMMGiOB8lPDoRz10myYy0eKHqedCo5mEzfJbO3Z7gUZ6P-N3RpTX6xuUTT_IBom3LsqZYvEC6clB76rRMnXIl1BrWwo_O9er8Yiz4mO7ujCcE6ofW1ogTiRy3zebdHmfsoXdVVY6yHgtN99X3R36KDJIUAzKOZFHDgiQGGiYxLFkgP_S-_tIJ5lk9bcbfoLuDrnJLQMLViqH2tpD7kSyUQbwZce1kK1zJkmjFsTaf4AExZlrIf6dHVwL2P7MIUPbl8QBZcgNL65tC_QLDD8r_PIRUBjQi6qP7wFsLqkPHzMEQzhy-PRJv8FE_xRgVxT0_XOhf0mnbyRFNQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
صبح بخیر ارتش سرخ
❤️
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.48K · <a href="https://t.me/SorkhTimes/135903" target="_blank">📅 08:52 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135902">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">linebet.apk</div>
  <div class="tg-doc-extra">53.7 MB</div>
</div>
<a href="https://t.me/SorkhTimes/135902" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🪙
اپلیشیکن اندروید سایت جهانی لاین بت
💳
واریز و برداشت ریالی
🎁
هر دوشنبه تا سقف ۱۳ ملیون تومان بونوس ورزشی
🔗
بدون نیاز ب فیلترشکن
🤩
آموزش کامل استفاده از اپ
🔜
💰
💰
💰
💰
💰
📱
Telegram Channel
👇
https://telegram.me/+dukgrB6-zGsyNGM8</div>
<div class="tg-footer">👁️ 5.86K · <a href="https://t.me/SorkhTimes/135902" target="_blank">📅 02:16 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135901">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/juEnYP9j3l9t8PxkbGe_CwvMATPYvmnJEg793lK5p5nXgvc_j0mDrCDFVTHt6c-KnvZ3LxjY10IX5eQ0VXrf-K4wMBUtCgOZbQgQSJAdSVHN2GQBRWKiu1ythuLGxL6Nqg1SMzOkNxsZZuqnJWfnB6dpScEUTCujRgL3i2MpgEj-G-Dy7ji18IbU7QFR8ZTXrMmaTqRRIAlcialdf-_8P3TWYbBqor7sjKle7H55nyAKywImozgPTMvlPU1Bb_MDn79hd0dbBfsJmxvGmfUtbJu0H4NZbST_rFQn7RLYW3_r94-trO7Xkqo_CoX3RBP7FBuWxVUYqns-wO9Quv3ydw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
به دنیای پیش‌بینی فوتبال و کازینو با LINEBET خوش آمدید
🌍
سایت بین‌المللی و معتبر LINEBET
⚽️
پیش‌بینی فوتبال
🎰
کازینو آنلاین
💳
واریز و برداشت ریالی
🎁
بونوس 100٪ اولین واریز
🎁
بونوس 100٪ هر دوشنبه
📞
پشتیبانی فارسی فعال
🎁
کد هدیه ثبت‌نام: L5670
🔗
دانلود اپلیکیشن اندروید
👉
🔗
لینک سایت
👉
✉️
https://telegram.me/+dukgrB6-zGsyNGM8
🌐
برای ورود به سایت از IP کشورهای آسیایی یا کانادا استفاده کنید.
🇹🇷
🇨🇦
🇮🇳
Ⓜ️
📚
آموزش کامل سایت
👉</div>
<div class="tg-footer">👁️ 6.14K · <a href="https://t.me/SorkhTimes/135901" target="_blank">📅 02:16 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135900">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">🚨
🚨
🔴
شهاب زندی مدیرعامل نساجی کسری طاهری رو گول زده و گفته پرسپولیس پولی برای خرید قطعی تو نداره بیا با ما امضا کن تا شرایط رو فراهم کنیم بری پرسپولیس و طاهری هم رفته تفاهم نامه سه جانبه امضا کرده و بعداً فهمیده چه اشتباهی کرده/ فرهیختگان
🎗️
«سرخ تایمز» دریچه…</div>
<div class="tg-footer">👁️ 6.51K · <a href="https://t.me/SorkhTimes/135900" target="_blank">📅 00:53 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135899">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">❗️
وای چه گل هایی زد آرژانتین ..گل دوم هم زد ..و انگلیس داره می‌ره رده بندی و آرژانتین داره می‌ره فینال ....
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.52K · <a href="https://t.me/SorkhTimes/135899" target="_blank">📅 00:33 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135898">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">✅
بازی شد یک بر یک
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.52K · <a href="https://t.me/SorkhTimes/135898" target="_blank">📅 00:24 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135897">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">❌
❌
انگلیس گل اول رو زد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.45K · <a href="https://t.me/SorkhTimes/135897" target="_blank">📅 00:17 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135896">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">✅
صداوسیما: ساکنان اهواز شدت انفجارها بالاست؛ از خانه‌ها خارج نشوید و تو خونه بمونید.
🔴
+طبق گزارشات شما گفته میشه برخی مناطق رو دستور تخلیه دادن.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.52K · <a href="https://t.me/SorkhTimes/135896" target="_blank">📅 00:00 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135895">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">❗️
❗️
طبق گزارشات مردمی، شدت حملات امشب به اهواز حتی از جنگ ۴۰ روزه هم بیشتر بوده
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.41K · <a href="https://t.me/SorkhTimes/135895" target="_blank">📅 23:57 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135894">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">❌
❌
نیمه اول چیز خاصی نداشت جز درگیری فقط و تو مخی بودن داور   صفر بر صفر تمام شد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.07K · <a href="https://t.me/SorkhTimes/135894" target="_blank">📅 23:47 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135893">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">🚨
فوووووووووووری
❗️
جواد خیایانی: رامین رضاییان به لگانس اسپانیا پیوسته است
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.2K · <a href="https://t.me/SorkhTimes/135893" target="_blank">📅 23:38 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135892">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">🔴
قاب سنگین امشب
🔥
🔥
🔥
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.11K · <a href="https://t.me/SorkhTimes/135892" target="_blank">📅 23:33 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135891">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">کانالی که همیشه در مسیر ورشکست کردن سایت های شرطبندی حرکت کرده!
😈
آمار ثابت 90 درصد برد
✅
فقط کافیه چند روز فرم هاش رو دنبال کنید...
⚽️
@Tipster_Mafiaa
@Tipster_Mafiaa
⚽️
@Tipster_Mafiaa
@Tipster_Mafiaa</div>
<div class="tg-footer">👁️ 5.79K · <a href="https://t.me/SorkhTimes/135891" target="_blank">📅 23:30 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135890">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PUMItG54hQohz3BBVOEjSCEZGkhP7dXjRNy6ob-dlN1cdcOTilYXv0exkd14PdO03fCDRltrB-DmvWTtyJkd5_HQWyJm_0GiNYLn5oXx_ss9HdmlyvXbYcY3aFUOGurTo76eZqHQxrHBT7Tzvt4UgXRH2ZxOFUUaygqzgZJeUVwqEVwM_aRa8IV7nkp5H-tq1zZorSIPJQY0vg5IrlCSnJcRlDLXK3VBIXxoz4z6Iq0WOIRbM140VUGl1hNVYfdK1b4dg68W_1V6mF6vMnRwtcBJQmTnNCQ1-lQs4Kimcs1uXv3tNZAm96Pty-4rJHzaPHpgRDQqYyo7K0ESrNfgnw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">میکس عالی برد شد
❤️
☑️
✔️
@Tipster_Mafiaa</div>
<div class="tg-footer">👁️ 5.84K · <a href="https://t.me/SorkhTimes/135890" target="_blank">📅 23:30 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135889">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">🔹
🔹
آغاز بازی
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.76K · <a href="https://t.me/SorkhTimes/135889" target="_blank">📅 23:29 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135888">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a436b0d04c.mp4?token=iN4uIDarUQx3apa3g957EzHlgtO8x2jf8onQEAAIPnWdzw17EzejHzFiT8I0q12nqGKlSO1nfb959_ONghF7OYRMJSF49qrUj2QYxPT5GthlWggNI9Ne-OX7Yx6N2T8X5XxlEXSkyH3aWI6sEv0eMhRrizT2BAZNAmadl6E0QIzp5V7grTUyBcxelO7GeECyVce-jP2imsaio6sRdirCeOsjxQ4NeD8ZiwVjWj35_qPU03uUR9q7lr_5IM_TFlt46PQABZ47VjHJe81WyS0pgETph3Ir7wuVS1LXK3omNttL5APUSPgxzzDdzwt9mQr69tx3VF-Pp8AlyFOV8sS2yQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a436b0d04c.mp4?token=iN4uIDarUQx3apa3g957EzHlgtO8x2jf8onQEAAIPnWdzw17EzejHzFiT8I0q12nqGKlSO1nfb959_ONghF7OYRMJSF49qrUj2QYxPT5GthlWggNI9Ne-OX7Yx6N2T8X5XxlEXSkyH3aWI6sEv0eMhRrizT2BAZNAmadl6E0QIzp5V7grTUyBcxelO7GeECyVce-jP2imsaio6sRdirCeOsjxQ4NeD8ZiwVjWj35_qPU03uUR9q7lr_5IM_TFlt46PQABZ47VjHJe81WyS0pgETph3Ir7wuVS1LXK3omNttL5APUSPgxzzDdzwt9mQr69tx3VF-Pp8AlyFOV8sS2yQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">کریم باقری: اگه جام جهانی رو 64 تیم میکنن ماهم به عنوان تیم پیشکسوتان تیم بدیم بریم
😂
😂
😂
🔴
+ خنده های علی دایی رو
😂
😂
😂
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.08K · <a href="https://t.me/SorkhTimes/135888" target="_blank">📅 23:26 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135887">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">❗️
یاسین سلمانی ماندنی شد
🔴
با نظر مهدی تارتار، هافبک جوان پرسپولیس در جمع سرخ‌ها باقی خواهد ماند و فرصت دارد خودش را در فصل جدید ثابت کند.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.7K · <a href="https://t.me/SorkhTimes/135887" target="_blank">📅 23:23 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135886">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">❗️
#فوری | ترامپ به فاکس نیوز:
❗️
حملات علیه ایران هفته آینده گسترش خواهد یافت و خاورمیانه برای آنچه بعداً رخ خواهد داد آماده میشود
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.9K · <a href="https://t.me/SorkhTimes/135886" target="_blank">📅 23:18 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135883">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">🚨
کی میبره؟
🔹
آرژانتین
❤️
🔹
انگلیس
🔥
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.94K · <a href="https://t.me/SorkhTimes/135883" target="_blank">📅 22:31 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135882">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">❗️
#فوری | ترامپ به فاکس نیوز:
❗️
حملات علیه ایران هفته آینده گسترش خواهد یافت و خاورمیانه برای آنچه بعداً رخ خواهد داد آماده میشود
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.05K · <a href="https://t.me/SorkhTimes/135882" target="_blank">📅 22:30 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135881">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">🔹
🚨
خبرگزاری فارس: پرسپولیس علاقه ای به جذب آسانی نداره
🫤
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.04K · <a href="https://t.me/SorkhTimes/135881" target="_blank">📅 22:28 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135880">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">🚨
🚨
مسئول باشگاه مذاکره‌ی پرسپولیس با یاسر آسانی رو تکذیب کرد/قدوسی
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.86K · <a href="https://t.me/SorkhTimes/135880" target="_blank">📅 22:26 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135879">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/evUvxZtRq7iBJxD23HNwf-AkHGodMIpocfYm0Ry6pT0GYBqXKRWZWOwedq5WOUo-m3KYpJ1i1hSyAWUFSOYiZT8kL8Bns-DMgy31xVkBROFY-oXVFLHzKxX2tb_3Ab-bG9-2m-mFFS-YEpU5VbA8pB0Yqpb4Qc8b1fVYXgNjRp2n6DDTq3w3Md96ZCjbEwfliIXSlshT9jvP0we0LIMe1zwZ-buSDk330MyZEiPs8qylMrRjXwybTG2Mf0Mug_SHNS7jymTp9wX5eAJo4rVz5Aps8OATPTJ48eEQc7T6xhh7hnSW639FOYzeqk7O0FsInYD8-unUxdtHclPaeO0uPg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
کی میبره؟
🔹
آرژانتین
❤️
🔹
انگلیس
🔥
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.17K · <a href="https://t.me/SorkhTimes/135879" target="_blank">📅 22:03 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135878">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">🔹
🔹
تارتار هنوز درباره‌ی جهانبخش و قدوس نظری نداده/قدوسی
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.92K · <a href="https://t.me/SorkhTimes/135878" target="_blank">📅 21:58 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135877">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">🚨
احتمال گرفتن رضایت‌نامه قرضی زارع بیشتره
✍
قرمزآنلاین
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.97K · <a href="https://t.me/SorkhTimes/135877" target="_blank">📅 21:56 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135876">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">❌
کریم باقری، کمکی که هر سرمربی آرزویش را دارد/ چرا او هیچ‌وقت سمت نفر اول بودن نرفت؟ پاسخ از زبان خود آقاکریم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.06K · <a href="https://t.me/SorkhTimes/135876" target="_blank">📅 21:52 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135875">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">❌
#فوری | ترامپ:
🔴
🔴
ایران مدتی پیش با ما تماس گرفت؛ آن‌ها می‌خواهند یک توافق انجام دهند
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.13K · <a href="https://t.me/SorkhTimes/135875" target="_blank">📅 21:35 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135874">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">❌
❌
علیرضا بابایی، مدیرعامل باشگاه چادرملو: متاسفانه طبق آخرین شنیده‌ها برخلاف پیش‌بینی‌های قبلی، کنفدراسیون فوتبال آسیا با درخواست فدراسیون ایران برای جابجایی نام چادرملو با گل گهر مخالفت کرده است.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس…</div>
<div class="tg-footer">👁️ 6.06K · <a href="https://t.me/SorkhTimes/135874" target="_blank">📅 21:31 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135873">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">🚨
🚨
مخالفت AFC با درخواست فدراسیون فوتبال ایران؛ گل گهر نماینده ایران در آسیا شد!
🚨
🚨
کنفدراسیون فوتبال آسیا با ارسال نامه‌ای به فدراسیون فوتبال ایران اعلام کرد گل گهر نماینده کشورمان در لیگ قهرمانان آسیا ٢ خواهد بود و در خواست فدراسیون برای حضور چادرملو را نپذیرفت.…</div>
<div class="tg-footer">👁️ 5.94K · <a href="https://t.me/SorkhTimes/135873" target="_blank">📅 21:29 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135872">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">❗️
فووووووووووووری
‼️
مدیر طویله استقلال: ما برای جذب دانیال ایری با باشگاه نساجی تماس گرفتیم انها به ما کسری طاهری را پیشنهاد دادند و به ما ثابت کردند که قراردادش را با این تیم امضا کرده است! ما هم در نظر داریم هر دو این بازیکنان را در صورت باز شدن پنجره نقل و انتقالاتی خریداری کنیم در غیر این صورت آنها نیم فصل به جمع اصافه شوند!!!!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.03K · <a href="https://t.me/SorkhTimes/135872" target="_blank">📅 21:27 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135871">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">🚨
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 5.96K · <a href="https://t.me/SorkhTimes/135871" target="_blank">📅 21:24 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135870">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">🚨
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 5.69K · <a href="https://t.me/SorkhTimes/135870" target="_blank">📅 21:24 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135869">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/228cd1f66e.mp4?token=dj_Orp-0OY8fLoKzPB4YYwLLI71uS6C-v6tCkzK_IvOyPrdY3rjN_DMITpj2kyXOPLHahRSwXbhm5mblcnfwoABbx8Ch6R2LTr8vNWCZvAPZ-nHKV5h8Q4niCwbIemP6ONhEOzr62LxewBm3tSt83npCVjuyq5WSoU5zbb0d9wLJDMG8JehiCeaxfXnuk7cbWHve-kKmzmOYSZn7zv6-EEOmD4pZ3KTB8PQRGWtqI3igeTVxRRkhU5WR5dF9V1KW8sWSau2c7EneLKcGjGI_Ycd6o9YGGt0M9tlu0PmuBNiw5SPxTJxEjs6A3K7PAoN3lcF18oWH3DWVF3_oyxKzuA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/228cd1f66e.mp4?token=dj_Orp-0OY8fLoKzPB4YYwLLI71uS6C-v6tCkzK_IvOyPrdY3rjN_DMITpj2kyXOPLHahRSwXbhm5mblcnfwoABbx8Ch6R2LTr8vNWCZvAPZ-nHKV5h8Q4niCwbIemP6ONhEOzr62LxewBm3tSt83npCVjuyq5WSoU5zbb0d9wLJDMG8JehiCeaxfXnuk7cbWHve-kKmzmOYSZn7zv6-EEOmD4pZ3KTB8PQRGWtqI3igeTVxRRkhU5WR5dF9V1KW8sWSau2c7EneLKcGjGI_Ycd6o9YGGt0M9tlu0PmuBNiw5SPxTJxEjs6A3K7PAoN3lcF18oWH3DWVF3_oyxKzuA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔉
دانیال مرادی رئیس دپارتمان داوری فدراسیون فوتبال: تمام ورزشگاه‌هایی که در فصل جدید میزبان مسابقات خواهند بود به طور کامل به پوشش VAR مجهز خواهند شد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.96K · <a href="https://t.me/SorkhTimes/135869" target="_blank">📅 21:04 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135868">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">❌
کریم باقری، کمکی که هر سرمربی آرزویش را دارد/ چرا او هیچ‌وقت سمت نفر اول بودن نرفت؟ پاسخ از زبان خود آقاکریم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.25K · <a href="https://t.me/SorkhTimes/135868" target="_blank">📅 20:59 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135867">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YDJkFWIquBaoG1kVSL70B4zXBj8f5dgOZeEsPtPZukBC6bmlzFIs9dASRSYYdMk7030XKZMup4wcZKp6hjjSXQ7C6vvDlAaXRkQn2CJ43S1vfqjZwh15wbY3ZPEEWEgTLAN4TpD3UGQ5V8NVaD1wr7QF2e_x3gWFYmztV7ph7l2GXykSijB1VHaZZ5kPlS1xotPTIZPOiJUfT6-CyJP7dK6FyrAvJ6t0-H9owoa5HKUyUwbNuYVfbK8OMhe3aauUGKU7rFNlE5oMOBHYDdzYJR-Ewlj4ytvcxFUhhAp-QZLurf4ayqqQOU642ifwC_TPWA0EoXIOOhA-TXrIiD7iyg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
قاب سنگین امشب
🔥
🔥
🔥
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.27K · <a href="https://t.me/SorkhTimes/135867" target="_blank">📅 20:58 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135866">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">🔴
🔴
ایجنت محمد مهدی زارع دقایقی پیش از باشگاه پرسپولیس خارج شد و گفت به زودی همه چیز مشخص خواهد شد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.1K · <a href="https://t.me/SorkhTimes/135866" target="_blank">📅 20:20 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135865">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">❗️
❗️
با رضایت مهدی تارتار از عملکرد مارکو باکیچ، این هافبک در جمع سرخ‌پوشان ماندگار شد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.26K · <a href="https://t.me/SorkhTimes/135865" target="_blank">📅 19:42 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135864">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">✅
✅
امیرحسین محمودی ستاره جوان پرسپولیس امروز ۲۰ ساله شد
❤️
🎉
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.43K · <a href="https://t.me/SorkhTimes/135864" target="_blank">📅 19:21 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135863">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">📌
مارکو باکیچ امشب پرواز داره و به تهران میاد و از فردا در تمرینات حاضر میشه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس 𝓣𝓲𝓶𝓮
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.46K · <a href="https://t.me/SorkhTimes/135863" target="_blank">📅 19:18 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135862">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">🟨
🟨
دوکو بخاطر زایمان همسرش اردو بلژیک رو ترک کرده و احتمالا بازی فردا شب مقابل تیم قلعه‌نویی رو از دست میده!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.29K · <a href="https://t.me/SorkhTimes/135862" target="_blank">📅 19:12 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135861">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">🏐
برنامه‌دیدارهای روز 24 تیر لیگ ملت‌های والیبال؛ هفته سوم لیگ ملت‌ها از فردا شروع خواهد شد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.19K · <a href="https://t.me/SorkhTimes/135861" target="_blank">📅 18:41 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135860">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">❌
❌
احتمال خیلی زیاد امیر رضا رفیعی به علاوه 60 میلیارد با لطیفی فر معاوضه میشه و توافقات انجام شده
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.22K · <a href="https://t.me/SorkhTimes/135860" target="_blank">📅 18:40 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135859">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/c_7QXX7ocjt6VjeamipYj3ODlJrw5eB6K6fyKucF6wGXVDqk4Egf_6kh6xLBxdgtUcoLv37ItqbHFrE3pNKdMQejM_uDu7vP-5XFlhqSKgb0Lok2P_UQuamw_lB1FLiOFGaCnM-mdypwqn1Smh_s7dJYh8ghxafq_IFWlSnD5iz7fj8B1ONiy9HP1zvjAK4-0Fi95BufAaXo3qaKmBdfADcssssHIYiPzvZxN7-z882uZUFwLl7Hhkof3O4rmxKWBRCLziR7bt3A5mb3E3NqiWtyU5-6U9AxCk_hkdmQc6zv3unZEsfWOQ-lX6dFAafNUTG7BFwsmrKvMDqEB4JsTQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
قرارداد پورعلی‌گنجی با پرسپولیس همچنان معتبر است و هنوز فسخی میان طرفین انجام نشده است. از همین رو، اگر باشگاه در جذب مدافعان مدنظر تارتار ناکام بماند، احتمال دارد از پورعلی‌گنجی برای بازگشت به تمرینات دعوت شود. ضمن اینکه خود این بازیکن نیز علاقه دارد به حضورش در پرسپولیس ادامه دهد!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.19K · <a href="https://t.me/SorkhTimes/135859" target="_blank">📅 18:38 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135858">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">😀
😀
😀
😀
فووووووری؛ زهره فلاح زاده خبرنگار معتبر حوزه استقلال:
🚨
🚨
🚨
مذاکرات پرسپولیس و یاسر آسانی از شب گذشته آغاز شده است
😳
😳
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.12K · <a href="https://t.me/SorkhTimes/135858" target="_blank">📅 18:27 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135857">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">🚨
فوری از ورزشه سه: اگر اتفاق خاصی رخ نده ظرف 72 ساعت آینده زارع پرسپولیسی میشه
🔥
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.24K · <a href="https://t.me/SorkhTimes/135857" target="_blank">📅 18:26 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135856">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">🔴
#فوری | ادعای اکسیوس:
🔴
🔴
ترامپ جلسه‌ای در «اتاق وضعیت» کاخ سفید برگزار کرد تا درباره یک تهاجم گسترده در ایران بحث کند
🔴
🔴
منابع می‌گوید که این حملات، دامنه‌ای فراتر از تهاجم‌های کنونی در اطراف تنگه هرمز خواهند داشت
❗️
❗️
جلسه مذکور بر طرح‌های جدید برای حملات…</div>
<div class="tg-footer">👁️ 6.28K · <a href="https://t.me/SorkhTimes/135856" target="_blank">📅 18:25 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135855">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">❌
❌
علی دایی و کریم باقری امشب مهمان برنامه عادل فردوسی‌پور برای بازی آرژانتین و انگلیس هستند.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.46K · <a href="https://t.me/SorkhTimes/135855" target="_blank">📅 17:40 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135854">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">❗️
طاهری رویای بازی تو پرسپولیس رو داشته و توسط شهاب زندی مدیرعامل نساجی گول خورده و حالا هرطور شده میخواد فسخ کنه.///فرهیختگان
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.66K · <a href="https://t.me/SorkhTimes/135854" target="_blank">📅 16:50 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135853">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">❗️
🗞
کسرا طاهری بدنبال فسخ قرارداد با نساجی تا ۴۸ ساعت آینده
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.69K · <a href="https://t.me/SorkhTimes/135853" target="_blank">📅 16:40 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135852">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">✅
پدر کسری طاهری: امشب یه جلسه مهم داریم که سرنوشت پسرم مشخص میشه
❗️
❗️
پرسپولیس کنسل نشده و بعد جلسه امشب همه چیز مشخص میشه، بعد جلسه امشب با رسانه‌ها صحبت میکنم نمی‌خوام پسرم ابزاری باشه برای درآمد و منفعت یک سری از افراد
🎗️
«سرخ تایمز» دریچه ای تازه به…</div>
<div class="tg-footer">👁️ 6.47K · <a href="https://t.me/SorkhTimes/135852" target="_blank">📅 16:40 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135851">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EUkkvoW0Es8yT46hiHtwXgepT3PWZ1K1lGETnzkl-rfTq-vQQEnYmwC5BsZp3sYYfgLCYf9L3QVEpcxEFGffhCqE1t92y-ctxMBlnVb3q536JH4F56wNeTUCkwHHgXZpmAiXkgO1XxSrIoe7lEUOY7GODq5yjme5AU7aqd5b56q2kXztopd1Y9skKwPx0mSUEpgOEYShpUjD-lxIjcOX4OABY8Rnopo4h-gqoNdRRxhZyHR3DZRsZDgygMuaqJ4LeWoJP53OB92MitGlqJqve5wSd4F34lqwZDVOqQ2kBghew4zsmx0fJEDHRPcfPu2N_hxMi7R8H1BWSs68zO-K4g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">😀
😀
😀
😀
فووووووری؛ زهره فلاح زاده خبرنگار معتبر حوزه استقلال:
🚨
🚨
🚨
مذاکرات پرسپولیس و یاسر آسانی از شب گذشته آغاز شده است
😳
😳
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.54K · <a href="https://t.me/SorkhTimes/135851" target="_blank">📅 16:31 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135850">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">🚨
🚨
🚨
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 6.17K · <a href="https://t.me/SorkhTimes/135850" target="_blank">📅 16:28 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135849">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/q3oD-IYuL37CfTKg9aSF95pzBHaNSQOu8ZBpUcQybxvsxbXJ1ruxrUbYltaLCMk7_OAsxWyTX2-AKwFiJJtl2tUkM__jZBW7ESWl4n3RU1rHx8Tjgk8VqGOZnbKlWsqtqJQFpOb0KjKNHSulHhaoWzQ3jv_I8Tyl68wLjF7ukXj0E4hu5obus_oEsua8DEtFV9teU1oZqqht7HXMBbP6jmc6VCeD2eiJSg-9ULF8hHwVeFc-pa8x7DXvAmsP9nDRnwnpsLlmue3HfGt8Xk1VHcYpZvxn912Pkyl4fX2OcHtJy6GESr-hJ55b2Fpzc_KAYTytqmCnwWVqfC_5gUcR4g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
فوری از ورزشه سه: اگر اتفاق خاصی رخ نده ظرف 72 ساعت آینده زارع پرسپولیسی میشه
🔥
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.35K · <a href="https://t.me/SorkhTimes/135849" target="_blank">📅 16:28 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135848">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">✅
پدر کسری طاهری: امشب یه جلسه مهم داریم که سرنوشت پسرم مشخص میشه
❗️
❗️
پرسپولیس کنسل نشده و بعد جلسه امشب همه چیز مشخص میشه، بعد جلسه امشب با رسانه‌ها صحبت میکنم نمی‌خوام پسرم ابزاری باشه برای درآمد و منفعت یک سری از افراد
🎗️
«سرخ تایمز» دریچه ای تازه به…</div>
<div class="tg-footer">👁️ 6.36K · <a href="https://t.me/SorkhTimes/135848" target="_blank">📅 16:27 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135847">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">❌
#فوری
🔴
یاسر آسانی ستاره آلبانیایی فصل قبل استقلال در آستانه پیوستن به تراکتور قرار دارد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.36K · <a href="https://t.me/SorkhTimes/135847" target="_blank">📅 16:20 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135846">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">❗️
پنج کاپیتان پرسپولیس در فصل پیش رو مشخص شدند
⏺
1_علی علیپور
⏺
2 _حسین کنعانی زادگان
⏺
3_محمد عمری
⏺
4– محمد خدابنده لو
⏺
5_اوستن اورنوف
🔴
پ.ن: در صورتی که وحید امیری به پرسپولیس اضافه شه، احتمالا کاپیتان اول تیم میشه.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار…</div>
<div class="tg-footer">👁️ 6.39K · <a href="https://t.me/SorkhTimes/135846" target="_blank">📅 15:10 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135845">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">❌
محسن خلیلی سرپرست پرسپولیس: برای جذب کسری طاهری باید 200 میلیارد خرج می کردیم که به این نتیجه رسیدیم که قید این بازیکن را بزنیم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.53K · <a href="https://t.me/SorkhTimes/135845" target="_blank">📅 14:54 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135844">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">🚨
🚨
افشاگری جنجالی رسانه عادل فردوسی‌پور از امیرقلعه‌نویی: سرمربی تیم‌ملی قبل از بازی با نیوزیلند تهدید به استعفا کرده و فدراسیون با پرداخت ۱۴۰ میلیارد تومان پاداش به این سرمربی در یک بانک‌خصوصی، قلعه‌نویی رو راضی به ادامه حضور در جام‌جهانی کرده! حالا هیئت رئیسه…</div>
<div class="tg-footer">👁️ 6.32K · <a href="https://t.me/SorkhTimes/135844" target="_blank">📅 14:54 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135843">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">MelBet2.apk</div>
  <div class="tg-doc-extra">53.8 MB</div>
</div>
<a href="https://t.me/SorkhTimes/135843" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🆕
اپلیکیشن MelBet
🔄
🎁
کد هدیه 100 دلاری:
Sport100
🤝
اسپانسر رسمی جام جهانی
🔵
کاملترین برنامه موبایل
☄️
صرافی معتبر
🤖
ربات راهنما
🇮🇷
برای تغییر زبان برنامه، زبان موبایل خود را تغییر دهید.
✅
ورود به اپلیکیشن بدون فیلترشکن</div>
<div class="tg-footer">👁️ 6.19K · <a href="https://t.me/SorkhTimes/135843" target="_blank">📅 14:44 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135842">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/DZ5oegeHB9LLkGc0KYkgwi0Om8mgBhdXyZuqeex6mqwl_0_VFH7Oe-fmlKOqsqeoBOML8jv6Hs3BH_7UCsBZaQREUBNcBKsBfUbapMoYowg3-oZPqBCVGwBSE4bj8ytWnIvJY5W0ZZINsjDzdoBevjLpp-433Lrs27t8DqfEhXhJplW-VnsseGjDeG4KEZsbPqNSKfgiNGJcjQFhIurpEFz8OFDFRV1KOCZwotFlSmteOUpEQHJ-jnp3scwH4_aKmlMJB_xRslei2j75d6BaKcAZB9pvlUTq6ykqKhnnGZZfmHU4hn9BD_uZK8NetK4J89v5Wm46DnDFP9MAiqSp4A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">▶️
بازی فوووق جذاااااب
انگلیس
و
آرژانتین
رو با آپشن های تخصصی در
MelBe
t پیشبینی کنید!
▶️
💵
امکان شارژ
کارت بکارت
و
هات ووچر
🎁
قرعه کشی و آفر های جذاب با جوایز ویژه
🌐
دانلود مستقیم اپلیکیشن اندروید
🤝
اسپانسر رسمی جام جهانی
🇮🇷
پشتیبانی از زبان فارسی
✍️
حرفه ای، مطمئن و در کلاس جهانی پیشبینی کنید!
برای ورود به سایت فیلترشکن خود را خاموش کنید!
‌
🌐
Link
🔜
MelBet1.net
🌐
‌
Link
🔜
MelBet1.net</div>
<div class="tg-footer">👁️ 6.26K · <a href="https://t.me/SorkhTimes/135842" target="_blank">📅 14:44 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135841">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">🔴
#فوری
| ادعای اکسیوس:
🔴
🔴
ترامپ جلسه‌ای در «اتاق وضعیت» کاخ سفید برگزار کرد تا درباره یک تهاجم گسترده در ایران بحث کند
🔴
🔴
منابع می‌گوید که این حملات، دامنه‌ای فراتر از تهاجم‌های کنونی در اطراف تنگه هرمز خواهند داشت
❗️
❗️
جلسه مذکور بر طرح‌های جدید برای حملات به اهداف استراتژیک در ایران، متمرکز بود
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.06K · <a href="https://t.me/SorkhTimes/135841" target="_blank">📅 14:33 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135840">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">🔴
🔴
با اعلام فدراسیون فوتبال، کمیته استیناف درخواست تجدیدنظر باشگاه پرسپولیس در پرونده علیرضا بیرانوند را رد کرد.
🔴
باشگاه پرسپولیس نسبت به رای کمیته وضعیت بازیکنان فدراسیون فوتبال که به موجب آن حکم به محکومیت به پرداخت مبلغ یک میلیارد و ۲۰۰ میلیون تومان داده شد، اعتراض کرده بود.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.09K · <a href="https://t.me/SorkhTimes/135840" target="_blank">📅 14:13 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135839">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">🔴
شوک به استقلال: آسانی فسخ کرد!
🔴
یاسر آسانی با ارسال نامه‌ای رسمی به باشگاه استقلال، به دلیل پرداخت نشدن مطالبات فصل گذشته و پیش‌پرداخت قرارداد فصل جدید، فسخ یک‌طرفه قرارداد خود را اعلام کرد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس …</div>
<div class="tg-footer">👁️ 6.3K · <a href="https://t.me/SorkhTimes/135839" target="_blank">📅 14:12 · 24 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>

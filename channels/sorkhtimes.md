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
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-25 18:00:25</div>
<hr>

<div class="tg-post" id="msg-135954">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">✅
✅
اورونوف چهارشنبه‌ وارد ایران خواهد شد.
🔴
پیشنهاد ۳/۵میلیون یورویی الشمال قطر صحت ندارد.پیشنهادی باشد هم با میلغ بسیار کمتری است و از قرارداد مالی او یک میلیون و ۴۰۰ هزار دلاری با پرسپولیس بیشتر نیست/قرمزانلاین
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق…</div>
<div class="tg-footer">👁️ 1.43K · <a href="https://t.me/SorkhTimes/135954" target="_blank">📅 17:41 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135953">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">✅
قدوسی در خبری فوری
❌
احمد نور میخواد برگرده
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.82K · <a href="https://t.me/SorkhTimes/135953" target="_blank">📅 17:35 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135952">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/f2powt3VISfbzCYWvxDKAaExuVXVkvyHRkEZDKMiHYiu0valsfrUrT3n7pCtAmRabXaNGljafd62bv9CV1a1d0WG101QllddMqtnLGwpxmGpmp2rQtNBBhMKE8dg9msdy6StwPSIFnGpU_jGvRrj_ajaG8XR01S5aQm-9y5Uk-NLuk68MHBaKDqFsT06s94AFQKzmwS4PRc2GBHETFcr-B0SKPZYux8or7P34-5NR-AlvFwgyo81EL4AKurpAN7jCEszZ_amfCbZ4aKXizgPbYPptIJdBaRAYqNSQmDh1Ck881RGsqYC_TKHxyl1LPQ8Z_a2RtCbUs7M8iP50IarRg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❗️
ابوالفضل جلالی بعد از پیوستن به پرسپولیس یه میلیونی شد
🎉
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 2K · <a href="https://t.me/SorkhTimes/135952" target="_blank">📅 17:31 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135951">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">🚨
🚨
باشگاه پرسپولیس مذاکرات فشرده ای رو برای جذب سامان قدوس استارت زده ..
🚨
اما نه با مدیریت حدادی  با مدیریت خود بانک شهر .
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 2.21K · <a href="https://t.me/SorkhTimes/135951" target="_blank">📅 17:26 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135950">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">❌
شایعات؛ محمدحسین اسلامی در حال مذاکره با پرسپولیس!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.22K · <a href="https://t.me/SorkhTimes/135950" target="_blank">📅 16:51 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135949">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">❌
❌
کوشکی و اسلامی توسط ترنسفرمارکت بازیکن آزاد اعلام شدند
🔴
از طرفی ایجنت هر ۲ بازیکن با ایجنت جلالی یکیه
👀
نظرتونه؟!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.34K · <a href="https://t.me/SorkhTimes/135949" target="_blank">📅 16:48 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135948">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">🚨
🚨
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 3.46K · <a href="https://t.me/SorkhTimes/135948" target="_blank">📅 16:44 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135947">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">🚨
🚨
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 3.52K · <a href="https://t.me/SorkhTimes/135947" target="_blank">📅 16:41 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135946">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fz1ioEWRpmi5XlNm_lbX9IZO6guIuPyVN_M3cZGg8ha526yBEagczgFAZjv5oYZ0EXAlDizQNcnlVPcyn1ncNQczXeGEWpc7k9ZRMXvaXLzPFmoDjnRVUGXr2RP8z88Tc_KGrdHeYJPWYeaUzIDSNyCKS1uGdAIox7_8dL9q7AwatC-HWf4EhcZyp1qX3LRoEmwW_5enzk4oFOTvBQS8jIL3RjH0-Okg77aTuBWGZGtkQHgW6s5khl97kvi2XOmsSE4lSneUZ-9ufhCMHyJc8joTUWG7d0Xo_xSaU5yHogVfhQH829J5Y-5t-5PTbKzIoQYQ3kxsNYK1LuST8TX1fQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❗️
ایجنت مرتضی اومده مرتضی رو دوباره به لیست پرسپولیس اضافه کرده ؛ باشگاهم هنوز برای مرتضی پوستر خداحافظی نزده
😑
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.41K · <a href="https://t.me/SorkhTimes/135946" target="_blank">📅 15:52 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135945">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">🚨
سامان قدوس؛ بمب بعدی پرسپولیس؟
🔴
🔴
ورزش سه: پرسپولیس برای جذب سامان قدوس هافبک ایرانی اتحاد کلباء امارات درخواست داده و این بازیکن در لیست خرید سرخپوشان قرار گرفته است.
🔴
🔴
قدوس که سابقه بازی در لیگ برتر انگلیس با برنتفورد و تیم ملی ایران را دارد، یکی از…</div>
<div class="tg-footer">👁️ 4.43K · <a href="https://t.me/SorkhTimes/135945" target="_blank">📅 15:50 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135944">
<div class="tg-post-header">📌 پیام #90</div>
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
<div class="tg-footer">👁️ 4.7K · <a href="https://t.me/SorkhTimes/135944" target="_blank">📅 15:33 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135943">
<div class="tg-post-header">📌 پیام #89</div>
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
<div class="tg-footer">👁️ 4.55K · <a href="https://t.me/SorkhTimes/135943" target="_blank">📅 15:32 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135941">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VWYtwiN0b3KhqR5T0634ktOI4xgWujj5qpsBFflM5TtwdbvJE1ySvhc4O6o-b-14qTSUXS5i0huDe7RYuQXxSRf7JNv7s54e9Pk_dSTcHOqONRVh9rd2YqcI6g2m0zkEAjtBm6hT5AiJnXtwE71OM7bGJgQ7EoyqF_dU41ucLqP5_hlFypVdc411QJmdnEp2lB7l7EPmkKB43R1hHGY7Mwp60qCHbgrfyIg7Gftk0k_fTV4lIXfxgbrRxO-aYf5knhLNORC-mf96gngSgU0J3VAD-0WuAGVNk2LCd7i-7t-gDMz0ZqTEec6RBJkRwzoi5wbMdxOAx9ouyfsVMQAt7A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔺
فیفا قضاوت دیدار فینال جام جهانی ۲۰۲۶ میان تیم‌های ملی اسپانیا و آرژانتین را به علیرضا فغانی سپرد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.79K · <a href="https://t.me/SorkhTimes/135941" target="_blank">📅 15:07 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135940">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pOBFoMmXOMNpDs4KD_EO3uov577IzDv47SURsnBvdWuETT64_QFAuvXzLruTyWiBmKVeHBt5q-lmo-U2Udl7zwZ2_Hm2jKldupRWmfDkt-U8DU12nhSLJiSlMOpokRUc4FdeD2hJfcDPkw750Xqm7aTq2kwF_ynuCPWVnCkfn19aFLVeIIB40lhnj3pqW53J-FcA-N54VCJa0FPs_8I81rQt-IY7Vt5e55Okvi70W5W8IeqPBIZcZx7fVmkMsfqYiwy2Hb8y_5QfC3j8xM3ZA5h4i6PJvkZhmPMC2rMJHl6fyjC-aH1Fb_Xpu0Gcu44py1CyhUxqfNfzIhKl3y88lw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
خریدهای لیگ‌برتری پرسپولیس تا به امروز:
مهدی‌تیکدری‌نژاد، سیدمجید عیدی، پوریا شهرآبادی، ابوالفضل جلالی، پوریا پورعلی؛ هر باشگاهی هفت سهمیه لیگ برتری و سه سهمیه بازیکن آزاد داره.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.79K · <a href="https://t.me/SorkhTimes/135940" target="_blank">📅 15:02 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135939">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from𝙷𝚊𝚓𝙼𝙰𝚑𝚍𝚒</strong></div>
<div class="tg-text">تو دور زمونه ای که فساد حرف اولو میزنه کسی که وظیفشو انجام میده باید قدردان خودشو پدر و مادرش بود...</div>
<div class="tg-footer">👁️ 4.61K · <a href="https://t.me/SorkhTimes/135939" target="_blank">📅 15:00 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135938">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded frompourya</strong></div>
<div class="tg-text">دیگه نمیتونی زحمات یکی رو بگا بدی خیلیا به وضیفشون عمل نمیکنن</div>
<div class="tg-footer">👁️ 4.71K · <a href="https://t.me/SorkhTimes/135938" target="_blank">📅 14:56 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135937">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">وظیفه اشه  دیگه دمت گرم نداره  مثه اینه مادر به بچه اش شیر بده بگیم دمت گرم مادر که به بچه تازه بدنیا اومده شیر میدی
😂</div>
<div class="tg-footer">👁️ 4.77K · <a href="https://t.me/SorkhTimes/135937" target="_blank">📅 14:55 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135936">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromVahidreza. Sadeghpour</strong></div>
<div class="tg-text">وظیفه اشه
دیگه دمت گرم نداره
مثه اینه مادر به بچه اش شیر بده بگیم دمت گرم مادر که به بچه تازه بدنیا اومده شیر میدی
😂</div>
<div class="tg-footer">👁️ 4.68K · <a href="https://t.me/SorkhTimes/135936" target="_blank">📅 14:53 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135935">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">دمت حدادی گرم که باج به شغال نمیدد</div>
<div class="tg-footer">👁️ 4.73K · <a href="https://t.me/SorkhTimes/135935" target="_blank">📅 14:50 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135934">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromHamed 65442</strong></div>
<div class="tg-text">دمت حدادی گرم که باج به شغال نمیدد</div>
<div class="tg-footer">👁️ 4.67K · <a href="https://t.me/SorkhTimes/135934" target="_blank">📅 14:45 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135933">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromHamed 65442</strong></div>
<div class="tg-text">دم بانک شهر گرم</div>
<div class="tg-footer">👁️ 4.7K · <a href="https://t.me/SorkhTimes/135933" target="_blank">📅 14:45 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135932">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">✔️
#تایید_خبراختصاصی | #اولین_رسانه
🚨
❤️
پوریا پورعلی با عقد قرارداد دو ساله به پرسپولیس پیوست
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس 𝓣𝓲𝓶𝓮
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.85K · <a href="https://t.me/SorkhTimes/135932" target="_blank">📅 14:42 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135931">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">❌
❌
🚨
شنیده ها: امروز احتمالا ۲ رونمایی خواهیم داشت
👀
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.73K · <a href="https://t.me/SorkhTimes/135931" target="_blank">📅 14:42 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135930">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">✅
بااعلام سایت ترانسفر مارکت؛ باشگاه پرسپولیس بابت رضایت‌نامه محمد مهدی زارع 800 هزار دلار به باشگاه اخمت گروژنی روسیه پرداخت کرده است.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.73K · <a href="https://t.me/SorkhTimes/135930" target="_blank">📅 14:40 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135929">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kx0yiA2WjRFn7dzHGvfpxv05_cSEGwSR4n8Vi3wPnNzyDF1Sgp0UbPlB9it5xpRlVFRDOrg_DLjG_Tctk1P33MqKNtAGjJvFLBV6-u7pQvT-UN7KahKcJ30fZsgS7XUI-7Vnj1X9N-rcZs63C-NNxSLNnMAxtB_FiDtnpY0EDzYYkVWHbXC982elg64KJr3ekeeUSys7_rXdoFj_L357LqK_U9kftRM1cjWKBXxnE0p0tlCdH15EmzQWF1fkUfR610m6aFAwke5S2Ifjoy0oJcLSSlhQhlhj8usrPrVE73cRoG7Z_RttBC5AMeGjuK6hs2_CKPqrP_fP28sChS_IzA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
بااعلام سایت ترانسفر مارکت؛ باشگاه پرسپولیس بابت رضایت‌نامه محمد مهدی زارع 800 هزار دلار به باشگاه اخمت گروژنی روسیه پرداخت کرده است.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.79K · <a href="https://t.me/SorkhTimes/135929" target="_blank">📅 14:38 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135928">
<div class="tg-post-header">📌 پیام #75</div>
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
<div class="tg-footer">👁️ 4.74K · <a href="https://t.me/SorkhTimes/135928" target="_blank">📅 14:35 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135925">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">❌
❌
فوری از فارس:
🔴
انتقال پوریا پورعلی هافبک گل‌گهر به پرسپولیس تا چند ساعت آینده امضا میشه و به زودی رونمایی خواهد شد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.68K · <a href="https://t.me/SorkhTimes/135925" target="_blank">📅 14:32 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135924">
<div class="tg-post-header">📌 پیام #73</div>
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
<div class="tg-footer">👁️ 4.98K · <a href="https://t.me/SorkhTimes/135924" target="_blank">📅 14:16 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135923">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">🔴
تمرین امروز سرخپوشان در سالن وزنه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.89K · <a href="https://t.me/SorkhTimes/135923" target="_blank">📅 14:14 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135922">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">#تایمز_توئیت
⚠️
تو این مملکت دستت رو عسل بکنی بزاری دهن طرف دستت رو گاز میگیرن، همین زارع رو نمیگرفتن به خدای احد واحد خار مادر باشگاه رو یکی میکردید وسط فصل….
‼️
نساجی برای ایری ۱.۲ میلیون دلار و برای طاهری ۱.۳ میلیون دلار میخاست
🎗️
«سرخ تایمز» دریچه ای تازه…</div>
<div class="tg-footer">👁️ 4.92K · <a href="https://t.me/SorkhTimes/135922" target="_blank">📅 14:07 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135921">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">✅
❤️
رسمی؛ محمدمهدی زارع به پرسپولیس پیوست
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.98K · <a href="https://t.me/SorkhTimes/135921" target="_blank">📅 14:06 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135919">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/veH7CoUcikUsjRg31RKE-wTtWzl9Q359YydH3pdGahlM-BsIxrbXpwpk9NajFhtG8WWUiIP9rWzCbTRr7QYIH8g9g-P8rqECuA08wCKGUVOU5Xo2fOzz9fqW0BMLD_v9iLz-PpeJjZM_Kmmh1LrEiSFSgDJrutoNd7GpQJ6fqGahjHlBkRFgET9_XZUSJG8cPaS4eC7ylSKk7mU3vGA02nB6-r1O6avM2Sl2BJ0pBN0t6M_KlDXapZK7yZ9TlJKWITHD9eiuqxvtt860c9xtVShaees4nIUMQwPjGqyy7YDPlDEZazJsQWv9Hp-dBdmv8USa-Y00nNLdpd7pOYlhzQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
❤️
رسمی؛
محمدمهدی زارع به پرسپولیس پیوست
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.01K · <a href="https://t.me/SorkhTimes/135919" target="_blank">📅 14:05 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135918">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">#تایمز_توئیت
⛔️
❌
با یه مشت دیونه زنجیری طرفیم، باشگاه هرکسی رو میخره یه عده هستن فقط بلندن گوه بخورن
‼️
قبلا میگفتن بانک شهر گداست پول نمیده الان رفتیم یکی از بهترین دفاع وسط های ایران رو خریدیم (زارع) یه عده دهنشون رو باز میکنن که با این پول میشد ایری و طاهری…</div>
<div class="tg-footer">👁️ 4.95K · <a href="https://t.me/SorkhTimes/135918" target="_blank">📅 14:04 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135917">
<div class="tg-post-header">📌 پیام #67</div>
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
<div class="tg-footer">👁️ 5.01K · <a href="https://t.me/SorkhTimes/135917" target="_blank">📅 13:57 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135916">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">❗️
❗️
فرهیختگان : قرار بر این شده است که  باشگاه پرسپولیس قرارداد هافبک مورد علاقه تارتار پوریا پور علی را امشب نهایی کرده تا این بازیکن بتواند از فردا در کنار سرخپوشان تمرین کند
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.16K · <a href="https://t.me/SorkhTimes/135916" target="_blank">📅 13:45 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135915">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">❗️
فارس؛ پویا لطیفی‌فر هافبک گل‌گهر در لیست خرید تارتار قرار گرفت
😐
❌
پ.ن از گل گهر بکشید بیرون ناموسا
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.28K · <a href="https://t.me/SorkhTimes/135915" target="_blank">📅 13:43 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135914">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">❗️
❗️
محمدمهدی زارع در آستانه پرسپولیسی شدن!
⌛
انتقال محمدمهدی زارع ۹۹ درصد نهایی شده و فقط واریز مبلغ باقی مانده است؛ پس از انجام پرداخت، از این خرید به‌صورت رسمی رونمایی خواهد شد. //خرمی
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
…</div>
<div class="tg-footer">👁️ 5.62K · <a href="https://t.me/SorkhTimes/135914" target="_blank">📅 12:23 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135913">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">❗️
مهدی تارتار از مدیران پرسپولیس درخواست کرده با توجه به شانس کم پرسپولیس برای جذب ایری و زارع،اقدام به بازگرداندن مرتضی پورعلی‌گنجی به تمرینات تیم کنند.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.74K · <a href="https://t.me/SorkhTimes/135913" target="_blank">📅 12:23 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135912">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">❗️
تارتار شخصاً با زارع تماس گرفته و خواهان اومدنش شده؛ باشگاه هم میخواد از اخمت‌گروژنی تخفیف بگیره/فرهیختگان
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.83K · <a href="https://t.me/SorkhTimes/135912" target="_blank">📅 12:22 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135911">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">❗️
❗️
فووووووووری
❌
فرهیختگان : اگر میلاد محمدی با باشگاه تمدید نکنه ، مدیران باشگاه از مدافع چپ جوونی که با اون به توافق نهایی رسیده‌اند ، رونمایی خواهند کرد
🔴
گفته می‌شود تمام اقدامات نهایی خرید جدید تیم انجام شده و این انتقال برای نهایی شدن تنها به یک امضا…</div>
<div class="tg-footer">👁️ 6.19K · <a href="https://t.me/SorkhTimes/135911" target="_blank">📅 10:56 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135910">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">❌
❌
میلاد محمدی همچنان تمدید نکرده و اخبار قطعی شدنش کذبه اما توافق داشته/ایرنا
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.06K · <a href="https://t.me/SorkhTimes/135910" target="_blank">📅 10:53 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135909">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">❗️
تارتار شخصاً با زارع تماس گرفته و خواهان اومدنش شده؛ باشگاه هم میخواد از اخمت‌گروژنی تخفیف بگیره/فرهیختگان
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.04K · <a href="https://t.me/SorkhTimes/135909" target="_blank">📅 10:31 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135908">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">✅
✅
#فوووووووری از طاهرخانی :
🔴
زارع در آستانه پرسپولیسی شدن..کار تمومه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.04K · <a href="https://t.me/SorkhTimes/135908" target="_blank">📅 10:30 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135907">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">✅
✅
یه خبر نصف شبی فوری، شنیده ها:
🔴
برخی از کارشناسان حقوقی معتبر به باشگاه اطلاع دادن کسری طاهری میتونه برای پرسپولیس بازی کنه و باشگاه داره مجدد واسه جذبش تلاش میکنه.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.1K · <a href="https://t.me/SorkhTimes/135907" target="_blank">📅 09:55 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135906">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">🚨
احتمال گرفتن رضایت‌نامه قرضی زارع بیشتره
✍
قرمزآنلاین
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.01K · <a href="https://t.me/SorkhTimes/135906" target="_blank">📅 09:53 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135905">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">❗️
حدادی : پول اسکوچیچ رو میدم بازیکن با کیفیت میگیرم
😂
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.95K · <a href="https://t.me/SorkhTimes/135905" target="_blank">📅 09:49 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135904">
<div class="tg-post-header">📌 پیام #54</div>
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
<div class="tg-footer">👁️ 6K · <a href="https://t.me/SorkhTimes/135904" target="_blank">📅 09:46 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135903">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/slfqBtQKUMMGiOB8lPDoRz10myYy0eKHqedCo5mEzfJbO3Z7gUZ6P-N3RpTX6xuUTT_IBom3LsqZYvEC6clB76rRMnXIl1BrWwo_O9er8Yiz4mO7ujCcE6ofW1ogTiRy3zebdHmfsoXdVVY6yHgtN99X3R36KDJIUAzKOZFHDgiQGGiYxLFkgP_S-_tIJ5lk9bcbfoLuDrnJLQMLViqH2tpD7kSyUQbwZce1kK1zJkmjFsTaf4AExZlrIf6dHVwL2P7MIUPbl8QBZcgNL65tC_QLDD8r_PIRUBjQi6qP7wFsLqkPHzMEQzhy-PRJv8FE_xRgVxT0_XOhf0mnbyRFNQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
صبح بخیر ارتش سرخ
❤️
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.82K · <a href="https://t.me/SorkhTimes/135903" target="_blank">📅 08:52 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135902">
<div class="tg-post-header">📌 پیام #52</div>
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
<div class="tg-footer">👁️ 6.04K · <a href="https://t.me/SorkhTimes/135902" target="_blank">📅 02:16 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135901">
<div class="tg-post-header">📌 پیام #51</div>
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
<div class="tg-footer">👁️ 6.35K · <a href="https://t.me/SorkhTimes/135901" target="_blank">📅 02:16 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135900">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">🚨
🚨
🔴
شهاب زندی مدیرعامل نساجی کسری طاهری رو گول زده و گفته پرسپولیس پولی برای خرید قطعی تو نداره بیا با ما امضا کن تا شرایط رو فراهم کنیم بری پرسپولیس و طاهری هم رفته تفاهم نامه سه جانبه امضا کرده و بعداً فهمیده چه اشتباهی کرده/ فرهیختگان
🎗️
«سرخ تایمز» دریچه…</div>
<div class="tg-footer">👁️ 6.64K · <a href="https://t.me/SorkhTimes/135900" target="_blank">📅 00:53 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135899">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">❗️
وای چه گل هایی زد آرژانتین ..گل دوم هم زد ..و انگلیس داره می‌ره رده بندی و آرژانتین داره می‌ره فینال ....
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.65K · <a href="https://t.me/SorkhTimes/135899" target="_blank">📅 00:33 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135898">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">✅
بازی شد یک بر یک
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.61K · <a href="https://t.me/SorkhTimes/135898" target="_blank">📅 00:24 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135897">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">❌
❌
انگلیس گل اول رو زد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.55K · <a href="https://t.me/SorkhTimes/135897" target="_blank">📅 00:17 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135896">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">✅
صداوسیما: ساکنان اهواز شدت انفجارها بالاست؛ از خانه‌ها خارج نشوید و تو خونه بمونید.
🔴
+طبق گزارشات شما گفته میشه برخی مناطق رو دستور تخلیه دادن.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.61K · <a href="https://t.me/SorkhTimes/135896" target="_blank">📅 00:00 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135895">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">❗️
❗️
طبق گزارشات مردمی، شدت حملات امشب به اهواز حتی از جنگ ۴۰ روزه هم بیشتر بوده
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.51K · <a href="https://t.me/SorkhTimes/135895" target="_blank">📅 23:57 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135894">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">❌
❌
نیمه اول چیز خاصی نداشت جز درگیری فقط و تو مخی بودن داور   صفر بر صفر تمام شد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.16K · <a href="https://t.me/SorkhTimes/135894" target="_blank">📅 23:47 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135893">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">🚨
فوووووووووووری
❗️
جواد خیایانی: رامین رضاییان به لگانس اسپانیا پیوسته است
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.29K · <a href="https://t.me/SorkhTimes/135893" target="_blank">📅 23:38 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135892">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">🔴
قاب سنگین امشب
🔥
🔥
🔥
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.17K · <a href="https://t.me/SorkhTimes/135892" target="_blank">📅 23:33 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135891">
<div class="tg-post-header">📌 پیام #41</div>
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
<div class="tg-footer">👁️ 5.85K · <a href="https://t.me/SorkhTimes/135891" target="_blank">📅 23:30 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135890">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PqZGrlE2d2M0lC4pKiJvBAqPKuk2GdeJG6JV5phOL4_mggiSI7fh-ypcz3W3ByDmgBBkfj1NLLqLqyUUoB4ORYiNDoZqvDI0zCGpWcv-ECKVtMbLx--BhyiEUy5KIsJkdbUY0cVN5WzSVelFFTcacsAGif8jKVyoXHnWilLfIt5Gwdo8hTtSsC279q0I4nXnDHdKeut7fWTly1pb9vCbvll8X5q7BcPDK0p1StHRvAJDnqjxW7hHPMQJzd4DqfJiCt5qT3HetD6EihnUK9wnwzyyM45d79WUr7fzw2AXsQ_62yKmNdp1mVBKWlBOkQV3SD1uOIr6dlLlNTme8Ntpcg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">میکس عالی برد شد
❤️
☑️
✔️
@Tipster_Mafiaa</div>
<div class="tg-footer">👁️ 5.9K · <a href="https://t.me/SorkhTimes/135890" target="_blank">📅 23:30 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135889">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">🔹
🔹
آغاز بازی
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.85K · <a href="https://t.me/SorkhTimes/135889" target="_blank">📅 23:29 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135888">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a436b0d04c.mp4?token=eUSgB_z0yXWJ9wM3rPrf41TZwBsHvP7KU9ogmOCywpJJK15KDaB9rK6Ob_NM_sO-YoLDhsR4kTu29VAbuwPF4WdQ853nrbUf3RJ2ZmiVyIZgxOCWf5uXDSpaPdbcqBVa4b-sLnrDk3ZgFWTgbAMg312TgWsTb-c7YG2A7pglhc5JYpgLyXEbH7tIrmnFOwsuX1BArL_9CsnsP6rwO36YvJ8vopSAycIE2kTOwCMokoVWMg16Aed-H0_B4hbQ_a3F5S3PLZlhmd4gHLKZdd7q9OXSQo5FcSamzJOZnLAtEE_k_pQg3zXSQEvAo0Hy6lYXmOvNCgB03Ncki7OvMCS_vQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a436b0d04c.mp4?token=eUSgB_z0yXWJ9wM3rPrf41TZwBsHvP7KU9ogmOCywpJJK15KDaB9rK6Ob_NM_sO-YoLDhsR4kTu29VAbuwPF4WdQ853nrbUf3RJ2ZmiVyIZgxOCWf5uXDSpaPdbcqBVa4b-sLnrDk3ZgFWTgbAMg312TgWsTb-c7YG2A7pglhc5JYpgLyXEbH7tIrmnFOwsuX1BArL_9CsnsP6rwO36YvJ8vopSAycIE2kTOwCMokoVWMg16Aed-H0_B4hbQ_a3F5S3PLZlhmd4gHLKZdd7q9OXSQo5FcSamzJOZnLAtEE_k_pQg3zXSQEvAo0Hy6lYXmOvNCgB03Ncki7OvMCS_vQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 6.14K · <a href="https://t.me/SorkhTimes/135888" target="_blank">📅 23:26 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135887">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">❗️
یاسین سلمانی ماندنی شد
🔴
با نظر مهدی تارتار، هافبک جوان پرسپولیس در جمع سرخ‌ها باقی خواهد ماند و فرصت دارد خودش را در فصل جدید ثابت کند.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.79K · <a href="https://t.me/SorkhTimes/135887" target="_blank">📅 23:23 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135886">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">❗️
#فوری | ترامپ به فاکس نیوز:
❗️
حملات علیه ایران هفته آینده گسترش خواهد یافت و خاورمیانه برای آنچه بعداً رخ خواهد داد آماده میشود
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.96K · <a href="https://t.me/SorkhTimes/135886" target="_blank">📅 23:18 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135883">
<div class="tg-post-header">📌 پیام #35</div>
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
<div class="tg-footer">👁️ 6K · <a href="https://t.me/SorkhTimes/135883" target="_blank">📅 22:31 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135882">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">❗️
#فوری | ترامپ به فاکس نیوز:
❗️
حملات علیه ایران هفته آینده گسترش خواهد یافت و خاورمیانه برای آنچه بعداً رخ خواهد داد آماده میشود
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.11K · <a href="https://t.me/SorkhTimes/135882" target="_blank">📅 22:30 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135881">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">🔹
🚨
خبرگزاری فارس: پرسپولیس علاقه ای به جذب آسانی نداره
🫤
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.1K · <a href="https://t.me/SorkhTimes/135881" target="_blank">📅 22:28 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135880">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">🚨
🚨
مسئول باشگاه مذاکره‌ی پرسپولیس با یاسر آسانی رو تکذیب کرد/قدوسی
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.92K · <a href="https://t.me/SorkhTimes/135880" target="_blank">📅 22:26 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135879">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gMzuLJrGVGwIHfw4quMNSmNCzfv9VfeRb7JDc3NR06BiNdLJ0o1-HvBI2BNWWibr-cR-mJXr3PUt4yoPnAgDBse5u3w68x4gDyryV1p3A75cRBcmT3LUdbzjO4MzbCXhwca40zw2nTHJjlO4AqDTW_jgivfBEpLnmPfxFkFChEPeYaN57OXjIuBZVz2wf9DbdWkV_AH7AhBJjgAvYAIQaxfXPPqAiSTu5daC2cflxnmcAfjy0kfwNm1cEHD3WOsVmz9WLTnSwOzQeUmW7w8amswcTk7kSJwN7rAUigj1AKG2rHEB4Npv3EE7aNgdK8w_63m02LlvcOduJu-yYQ3ymA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 6.23K · <a href="https://t.me/SorkhTimes/135879" target="_blank">📅 22:03 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135878">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">🔹
🔹
تارتار هنوز درباره‌ی جهانبخش و قدوس نظری نداده/قدوسی
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.95K · <a href="https://t.me/SorkhTimes/135878" target="_blank">📅 21:58 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135877">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">🚨
احتمال گرفتن رضایت‌نامه قرضی زارع بیشتره
✍
قرمزآنلاین
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6K · <a href="https://t.me/SorkhTimes/135877" target="_blank">📅 21:56 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135876">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">❌
کریم باقری، کمکی که هر سرمربی آرزویش را دارد/ چرا او هیچ‌وقت سمت نفر اول بودن نرفت؟ پاسخ از زبان خود آقاکریم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.12K · <a href="https://t.me/SorkhTimes/135876" target="_blank">📅 21:52 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135875">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">❌
#فوری | ترامپ:
🔴
🔴
ایران مدتی پیش با ما تماس گرفت؛ آن‌ها می‌خواهند یک توافق انجام دهند
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.16K · <a href="https://t.me/SorkhTimes/135875" target="_blank">📅 21:35 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135874">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">❌
❌
علیرضا بابایی، مدیرعامل باشگاه چادرملو: متاسفانه طبق آخرین شنیده‌ها برخلاف پیش‌بینی‌های قبلی، کنفدراسیون فوتبال آسیا با درخواست فدراسیون ایران برای جابجایی نام چادرملو با گل گهر مخالفت کرده است.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس…</div>
<div class="tg-footer">👁️ 6.12K · <a href="https://t.me/SorkhTimes/135874" target="_blank">📅 21:31 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135873">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">🚨
🚨
مخالفت AFC با درخواست فدراسیون فوتبال ایران؛ گل گهر نماینده ایران در آسیا شد!
🚨
🚨
کنفدراسیون فوتبال آسیا با ارسال نامه‌ای به فدراسیون فوتبال ایران اعلام کرد گل گهر نماینده کشورمان در لیگ قهرمانان آسیا ٢ خواهد بود و در خواست فدراسیون برای حضور چادرملو را نپذیرفت.…</div>
<div class="tg-footer">👁️ 5.97K · <a href="https://t.me/SorkhTimes/135873" target="_blank">📅 21:29 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135872">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">❗️
فووووووووووووری
‼️
مدیر طویله استقلال: ما برای جذب دانیال ایری با باشگاه نساجی تماس گرفتیم انها به ما کسری طاهری را پیشنهاد دادند و به ما ثابت کردند که قراردادش را با این تیم امضا کرده است! ما هم در نظر داریم هر دو این بازیکنان را در صورت باز شدن پنجره نقل و انتقالاتی خریداری کنیم در غیر این صورت آنها نیم فصل به جمع اصافه شوند!!!!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.06K · <a href="https://t.me/SorkhTimes/135872" target="_blank">📅 21:27 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135871">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">🚨
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 5.99K · <a href="https://t.me/SorkhTimes/135871" target="_blank">📅 21:24 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135870">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">🚨
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 5.72K · <a href="https://t.me/SorkhTimes/135870" target="_blank">📅 21:24 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135869">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/228cd1f66e.mp4?token=IbfdLr2Jb4US71aPaWtf-rFK8o-hpm9MKW_4nt56Ib9FsJ31xThp5z_dvJnDqL_xrS4omOczAiMQh__4gxcRm9IMb9CU6SdOP-tkfSCfIhDEcwFfUp8bqyqa34TLQJxLOde4EtWMJOY3DOZc3s9efLuNyGHFx0noFEl1TQY53kNzMPyDmJl1wg_5yTopGUq9cec2IoDHBepaY6sz5wSwGbxlygIxJHygV6l1hIWce7-v9SpMDmQyNa_1ka9N1NeB7jK3I03wtyc7EqO9juB2qNHWN6tYypVEKS4tj-B44zHBzJeiK4jHdVaT9f5S3K-TjrxGvYNIuy1_TnR7JsYTBg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/228cd1f66e.mp4?token=IbfdLr2Jb4US71aPaWtf-rFK8o-hpm9MKW_4nt56Ib9FsJ31xThp5z_dvJnDqL_xrS4omOczAiMQh__4gxcRm9IMb9CU6SdOP-tkfSCfIhDEcwFfUp8bqyqa34TLQJxLOde4EtWMJOY3DOZc3s9efLuNyGHFx0noFEl1TQY53kNzMPyDmJl1wg_5yTopGUq9cec2IoDHBepaY6sz5wSwGbxlygIxJHygV6l1hIWce7-v9SpMDmQyNa_1ka9N1NeB7jK3I03wtyc7EqO9juB2qNHWN6tYypVEKS4tj-B44zHBzJeiK4jHdVaT9f5S3K-TjrxGvYNIuy1_TnR7JsYTBg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔉
دانیال مرادی رئیس دپارتمان داوری فدراسیون فوتبال: تمام ورزشگاه‌هایی که در فصل جدید میزبان مسابقات خواهند بود به طور کامل به پوشش VAR مجهز خواهند شد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.99K · <a href="https://t.me/SorkhTimes/135869" target="_blank">📅 21:04 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135868">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">❌
کریم باقری، کمکی که هر سرمربی آرزویش را دارد/ چرا او هیچ‌وقت سمت نفر اول بودن نرفت؟ پاسخ از زبان خود آقاکریم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.28K · <a href="https://t.me/SorkhTimes/135868" target="_blank">📅 20:59 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135867">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Bv4Wq0dZEyXTzSblSp4MJQ--zt_ybnELh-yujjXL8MZ3ayqUF2eNfMCWA-SB1BD-bM54JJ_Gs1X02B58OLTwmANsPJgowEEz7w8rnZqWrxUBt56NTJvIyl9Qqh18Tpmm_YgiAy0OXuWUg9QV1yI9fqd92_CtqgCjV8fmgfYsRSSCTNcLg-8xMKwiROHQkwpnxG0kWrDb8SQXIBAgLM4183bORrdqt0PF1ckRuN8YKMCC53hVZKhw2_izKIxLtptpkqtpUN_u_Eqd7a96GdbOPUTSzk-4ZReYDp14vGmZgnRyrlvkJ1BpEK-l7h0_Mp56D1TQCEkscR3RB1KzSaUKrQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
قاب سنگین امشب
🔥
🔥
🔥
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.3K · <a href="https://t.me/SorkhTimes/135867" target="_blank">📅 20:58 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135866">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">🔴
🔴
ایجنت محمد مهدی زارع دقایقی پیش از باشگاه پرسپولیس خارج شد و گفت به زودی همه چیز مشخص خواهد شد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.13K · <a href="https://t.me/SorkhTimes/135866" target="_blank">📅 20:20 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135865">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">❗️
❗️
با رضایت مهدی تارتار از عملکرد مارکو باکیچ، این هافبک در جمع سرخ‌پوشان ماندگار شد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.29K · <a href="https://t.me/SorkhTimes/135865" target="_blank">📅 19:42 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135864">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">✅
✅
امیرحسین محمودی ستاره جوان پرسپولیس امروز ۲۰ ساله شد
❤️
🎉
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.46K · <a href="https://t.me/SorkhTimes/135864" target="_blank">📅 19:21 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135863">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">📌
مارکو باکیچ امشب پرواز داره و به تهران میاد و از فردا در تمرینات حاضر میشه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس 𝓣𝓲𝓶𝓮
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.49K · <a href="https://t.me/SorkhTimes/135863" target="_blank">📅 19:18 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135862">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">🟨
🟨
دوکو بخاطر زایمان همسرش اردو بلژیک رو ترک کرده و احتمالا بازی فردا شب مقابل تیم قلعه‌نویی رو از دست میده!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.32K · <a href="https://t.me/SorkhTimes/135862" target="_blank">📅 19:12 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135861">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">🏐
برنامه‌دیدارهای روز 24 تیر لیگ ملت‌های والیبال؛ هفته سوم لیگ ملت‌ها از فردا شروع خواهد شد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.22K · <a href="https://t.me/SorkhTimes/135861" target="_blank">📅 18:41 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135860">
<div class="tg-post-header">📌 پیام #12</div>
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
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/srHRHIPh92GnL9DQoT4LBOGlD6OVoWBRVYvin12iNICRPyoljgvqMCAx1aL6Czzjz621mkw3BmHavBnGLyGBXx4Zq_pj3Yuc3aivJIdUEOYQRJ4yl10cHPFwpKR1vz7tvqcubnt8oSQvYVtLFmxicx8Hrf3GdvUu2Xmne9L8lZkuvaVoCNwKmVEr6pJofJ1QtSL-2X5BHyCw-pNn03tX00gI0QMAb5IipeYLFqX4OEMqHBoNORegtgSN6IIEYlLuDui91h02opkw9wPLu-TQ7apIaUM1nNeAuBbH22jl-fj08nCsWu8b-Y3a2z8fB9jSOwYp467cN1pjCHUT_q39oA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
قرارداد پورعلی‌گنجی با پرسپولیس همچنان معتبر است و هنوز فسخی میان طرفین انجام نشده است. از همین رو، اگر باشگاه در جذب مدافعان مدنظر تارتار ناکام بماند، احتمال دارد از پورعلی‌گنجی برای بازگشت به تمرینات دعوت شود. ضمن اینکه خود این بازیکن نیز علاقه دارد به حضورش در پرسپولیس ادامه دهد!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.22K · <a href="https://t.me/SorkhTimes/135859" target="_blank">📅 18:38 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135858">
<div class="tg-post-header">📌 پیام #10</div>
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
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">🚨
فوری از ورزشه سه: اگر اتفاق خاصی رخ نده ظرف 72 ساعت آینده زارع پرسپولیسی میشه
🔥
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.27K · <a href="https://t.me/SorkhTimes/135857" target="_blank">📅 18:26 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135856">
<div class="tg-post-header">📌 پیام #8</div>
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
<div class="tg-footer">👁️ 6.31K · <a href="https://t.me/SorkhTimes/135856" target="_blank">📅 18:25 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135855">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">❌
❌
علی دایی و کریم باقری امشب مهمان برنامه عادل فردوسی‌پور برای بازی آرژانتین و انگلیس هستند.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.49K · <a href="https://t.me/SorkhTimes/135855" target="_blank">📅 17:40 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135854">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">❗️
طاهری رویای بازی تو پرسپولیس رو داشته و توسط شهاب زندی مدیرعامل نساجی گول خورده و حالا هرطور شده میخواد فسخ کنه.///فرهیختگان
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.69K · <a href="https://t.me/SorkhTimes/135854" target="_blank">📅 16:50 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135853">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">❗️
🗞
کسرا طاهری بدنبال فسخ قرارداد با نساجی تا ۴۸ ساعت آینده
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.72K · <a href="https://t.me/SorkhTimes/135853" target="_blank">📅 16:40 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135852">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">✅
پدر کسری طاهری: امشب یه جلسه مهم داریم که سرنوشت پسرم مشخص میشه
❗️
❗️
پرسپولیس کنسل نشده و بعد جلسه امشب همه چیز مشخص میشه، بعد جلسه امشب با رسانه‌ها صحبت میکنم نمی‌خوام پسرم ابزاری باشه برای درآمد و منفعت یک سری از افراد
🎗️
«سرخ تایمز» دریچه ای تازه به…</div>
<div class="tg-footer">👁️ 6.5K · <a href="https://t.me/SorkhTimes/135852" target="_blank">📅 16:40 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135851">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gWgNc9Bni3CZBibyft3kSt55XvpmVeutzTqOIA2kb-cClkIjOR3J25e3ZuzYoxUqazgnwJswyqwwui4874vcscY9P1doZyd1H81FXXHDL6o3ZnKi6rkQZcc3J5EfKRleFNtK9lcamAShWOlbuG-pYEzlCvl1kwP5qB6spzJ34WKrg754LDGIMjudL8a503EEhuKVG5Ce_SejK_cTPHtXxhdR0rXZaf5Q97KT_eIvZGGpd0Dd496fmeYZCz2DSUC23MGWtw8L9CQhlBHJg_PWVN5kzWhtPiZb32aObrqG5kpw2anrkQQavk2BHIf1FnRxoEm3QT5WpueYFmx_g20UwA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 6.57K · <a href="https://t.me/SorkhTimes/135851" target="_blank">📅 16:31 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135850">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">🚨
🚨
🚨
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 6.2K · <a href="https://t.me/SorkhTimes/135850" target="_blank">📅 16:28 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135849">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KCIjHZ_OAP2gfxBCM9mO0iu_82Cgh5l5ce6mHx1YK1GkUyATwXKsLgjt4QcqE8ZGXiKiXVRrAKFROp3UF_0PZFBGN69ONGga_0-mFRulIWHmKUGpzwKHMEFhNGcVToDBt769DuLLeBNiSqPo5G9mrUdgARla7YalW6-_dMcOGlZM2cTjddyAB_pF_UDBv_HevZPWl2LqlzR7jCF2I9N7qqKAXALa9liowU-CmjWVXZAzppOHWVkFPuP7abcVqtHCBVYidpEyPn78pflGTy9zOoh660AgFImU37UUgwNqe5YShMFL40x9keIFaV1uNeOo-srwmLzxjZzXqosZ3FKrNg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
فوری از ورزشه سه: اگر اتفاق خاصی رخ نده ظرف 72 ساعت آینده زارع پرسپولیسی میشه
🔥
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.35K · <a href="https://t.me/SorkhTimes/135849" target="_blank">📅 16:28 · 24 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>

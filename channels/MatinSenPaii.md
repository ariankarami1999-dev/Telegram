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
<img src="https://cdn1.telesco.pe/file/V3e75BByrWtY_9lIEh3cUao1hJS9hAfITLdAITejVC_BSA7Z54yxBxqHad_TP_fvUC14F_49gt0c92SaWjTXfnm7pmP1rRrtdS-yhoDGjtylO_ApTl1s3ecDINk0WhyFEDTRKQUGAFJvGlSt9FTlZ3kCzRnYshyQoPpWYgaeX3pAn1SNzL58qfLLKRrwh03p4MfDYHz4IUvBCnMDunvfJrgFtutJk6plfChpRTMVEynRdL2-_2YTJ0hj9ceFfcgfwShyHsD-CeYmVVOI0DJ4H5JVsJpTZK4lFJa0s9vQVxy9dWgysySo2yOXTWedu5X_laG7chfuVDFekvvmDAXc_w.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Matin SenPai</h1>
<p>@MatinSenPaii • 👥 156K عضو</p>
<a href="https://t.me/MatinSenPaii" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 متین هستم و کامپیوتر رو دوست دارم! در حال یادگیری هستم و چیزهایی که یاد میگیرم رو سعی میکنم به شما هم یاد بدم اگر به دردتون بخوره=)•YouTube:http://www.youtube.com/@Matin_SenPai•Github:https://github.com/MatinSenPai</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-04 00:48:49</div>
<hr>

<div class="tg-post" id="msg-5049">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/qa0QbSGUdRbhpbfgJJMt75cwDKl6Z-9D0NUTADAS9ybDXSaoz0d_KXReOjeLQugkfd1jBsbAA8t4Y4ZSwjPPJ8GBUNM54pqH6_79sN4LA1ZGvJGR4DOsRBRswxIZeAdV8ScWep9HERbqrd9UjIbRkteXM-LVtwgHiEX76xbwQ6FkMC7V6dCIsAqsyNK_77PsK58BzNG2wGBH41T6qcLLB4B9srXemJ1rH3BQTBmduO2lm5lxSdCyNZDfcmqX7d7jWqqqjM0_hGdujPU-5w2Tk4EutZ-xMYXk-ocRi-zBFksIyvTvxAjk-URjmLsawFnWkSMvy5Wz7H57tvwANz2bAQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قدرتمندتر از Fable 5 ولی رایگان! مدل مرموز Ox Alpha
توی این ویدئو رفتیم سراغ مدل مرموز Ox Alpha و اون پروژه‌ای که توی ویدئوی قبلی زدیم رو ارتقا میدیم باهاش! این مدل، به تازگی اومده و یه مدل مرموزه که هنوز اعلام نشده مال کدوم شرکته، اما بررسی و تحلیل می‌کنیم که مال کجا می‌تونه باشه. و همینطور بهتون میگم که چطور می‌تونید رایگان ازش استفاده کنید و کد بزنید
📹
تماشا در یوتوب</div>
<div class="tg-footer">👁️ 7.39K · <a href="https://t.me/MatinSenPaii/5049" target="_blank">📅 00:02 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5048">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">دوستان من کمی از لحاظ جسمی مشکل برام به وجود اومده بود. الان رو به راهم
سعی می‌کنم ویدئوی x alpha رو زودتر بذارم
❤️</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/MatinSenPaii/5048" target="_blank">📅 22:21 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5047">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">و خب من نظرم اینه که، Train بشه که بشه:)) مدل‌های قوی‌تر، ارزونتری که الان هستن و داریم ازشون استفاده می‌کنیم، بخشیش از همین طریق قدرتمندتر شدن
ولی خب شما باز اگر نگران «حریم خصوصی» هستید، دور چین و مدل رایگان و contributer رو خط بکشید</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/MatinSenPaii/5047" target="_blank">📅 11:25 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5046">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">به خاطر جالب بودن این پیشرفتش فرستادم. وگرنه به نظرم این نگرانی تا حدودی بی‌مورده.
زمانی که از مدل چینی/رایگان استفاده می‌کنیم، عملا داریم امضا میکنیم که از دیتامون استفاده بشه واسه‌ی Train کردن مدل.</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/MatinSenPaii/5046" target="_blank">📅 11:23 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5045">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/6f33bcf78a.mp4?token=dZpTKjWMWiGEmst5gOLeHrp4lXCQhqkUmzaGAyloAJwt2PZg68TpeyGdU2jZel2k6sfyJSTc0FY6Z-HxXsQYP8MssqH0QoQeAbJf0IzO3Sxjo7G_dVmX1FiDsh0japE03Z0plKUKcjRie5GkOU0gYdOjWpNAAlIQSRV1hWFFr7OCqKpl7MijpixxLDKjmCqQr-tf6J8fYcOoYXlTxUeQnyeW68HyRPm8X4T2mn97prJi2Q_XIKYWt7QOp-HeuTOx7RPJItDdZRUfiqNF-2F7FPpniSrJAJV62fmnyf5Sgq5aixfOKkLyKmImNHgRblKvl_GanZ00XeGXUfO34qOQBK7STx-THDoFE_6M3TMAhXupFLTbnvNkEOWwnUME3SB_Osac_btZqDU-QqOSh7demeGgZl4B60Zwhf8nxqhWLQEF-l9jgpjXxlC835LBHL1CzeVYPUVbN8AcZJibHR5Z90-omfW5GVz7dlEPVV-7syoVaH6cVSAd9Mjlc9n9mb6xpaMll7iwl3UUrRmJnk0Jfc8BJ6Jsxjkiyp4ZHOXFxXTaHa2pFzlxqRmAo5PM1uc8etoPbdp_63P8Hs4PkQwnooQu2rFJ-aKnzjL3R6-oVsArO3E5TEhsIBIWIWvEWNRXdHtDxFLn_iLiJZLrQo1O317OQtuMvQjJtq2U0EJZtyY" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/6f33bcf78a.mp4?token=dZpTKjWMWiGEmst5gOLeHrp4lXCQhqkUmzaGAyloAJwt2PZg68TpeyGdU2jZel2k6sfyJSTc0FY6Z-HxXsQYP8MssqH0QoQeAbJf0IzO3Sxjo7G_dVmX1FiDsh0japE03Z0plKUKcjRie5GkOU0gYdOjWpNAAlIQSRV1hWFFr7OCqKpl7MijpixxLDKjmCqQr-tf6J8fYcOoYXlTxUeQnyeW68HyRPm8X4T2mn97prJi2Q_XIKYWt7QOp-HeuTOx7RPJItDdZRUfiqNF-2F7FPpniSrJAJV62fmnyf5Sgq5aixfOKkLyKmImNHgRblKvl_GanZ00XeGXUfO34qOQBK7STx-THDoFE_6M3TMAhXupFLTbnvNkEOWwnUME3SB_Osac_btZqDU-QqOSh7demeGgZl4B60Zwhf8nxqhWLQEF-l9jgpjXxlC835LBHL1CzeVYPUVbN8AcZJibHR5Z90-omfW5GVz7dlEPVV-7syoVaH6cVSAd9Mjlc9n9mb6xpaMll7iwl3UUrRmJnk0Jfc8BJ6Jsxjkiyp4ZHOXFxXTaHa2pFzlxqRmAo5PM1uc8etoPbdp_63P8Hs4PkQwnooQu2rFJ-aKnzjL3R6-oVsArO3E5TEhsIBIWIWvEWNRXdHtDxFLn_iLiJZLrQo1O317OQtuMvQjJtq2U0EJZtyY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یک نکته عجیب در تست‌های اخیر کاربران از مدل Ox Alpha دیده شده که واقعاً سؤال‌برانگیز است.
همان پرامپت روز اول، بدون حتی یک کلمه تغییر، حالا خروجی بسیار دقیق‌تر و جزئی‌تری تولید می‌کند؛ مخصوصاً در مدل‌سازی سه‌بعدی موتور Raptor که اختلاف کیفیت با خروجی قبلی کاملاً محسوس است.
اما سؤال اصلی اینجاست:
اگر پرامپت همان است و آپدیت رسمی هم اعلام نشده، این جهش کیفیت دقیقاً از کجا آمده؟
آیا مدل در سکوت روی داده‌های جدید Fine-tune شده؟
آیا وزن‌های مدل یا پایپ‌لاین رندرینگ پشت صحنه تغییر کرده؟
یا Ox Alpha واقعاً نوعی یادگیری مداوم دارد؟
اگر این تغییرات بدون اطلاع‌رسانی رسمی در حال رخ دادن باشد، ما فقط با یک مدل بهتر طرف نیستیم؛ بلکه با مدلی مواجهیم که رفتار و توانایی‌هایش می‌تواند بدون انتشار نسخه جدید تغییر کند.
و این، از خودِ افزایش کیفیت جالب‌تر و البته نگران‌کننده‌تر است.
✍️
callitVer1</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/MatinSenPaii/5045" target="_blank">📅 11:21 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5044">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">راجب یه پادکست جالب شنیدم در مورد یه تیم نرم‌افزار نروژی که 4 ماه کامل از کلاد استفاده کردن و بعدش کلا بیخیال شدن برگشتن روی روش سنتی خودشون
فردا خلاصه‌اش رو واستون می‌ذارم</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/MatinSenPaii/5044" target="_blank">📅 00:22 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5043">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">نمیدونم واقعا چی بگم راجب اقتصاد
برق
...
می‌خواستم امشب استریم بذارم و بریم سراغ اخبار ai، برق رفت کلا تمرکز و انگیزه‌ام پودر شد.
کلا همیشه ترجیح میدم کمتر صحبت کنم راجب بدبختیامون چون همه جا میشنوید. و بیشتر تمرکز رو بذارم روی کار که کمی از این فضای حال به هم زن اقتصادی کشور دور بشیم...</div>
<div class="tg-footer">👁️ 29K · <a href="https://t.me/MatinSenPaii/5043" target="_blank">📅 22:12 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5042">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">ما الان داریم دقیقا مسیر ونزوئلا رو میریم.</div>
<div class="tg-footer">👁️ 30.5K · <a href="https://t.me/MatinSenPaii/5042" target="_blank">📅 20:40 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5041">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">راستی بچه‌ها پلن 5 دلاری OpenCode Go رو من با همین روش گرفتم. اگر که خواستید بگیرید میتونید به GLM 5.3 و اینها دسترسی داشته باشید به ارزش 60 دلار مجموعا: https://t.me/MatinSenPaii/4915</div>
<div class="tg-footer">👁️ 29.4K · <a href="https://t.me/MatinSenPaii/5041" target="_blank">📅 19:05 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5040">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">روش پرداخت بین‌المللی و گرفتن Visa Card مجازی  خب دوستان، امروز می‌خوام بهتون یاد بدم چطوری می‌تونید با این وبسایت، برای خودتون ویزا کارت بگیرید: https://app.mpay.cards?startapp=ref_PzwXZ8 (لینک رفرال هست. می‌تونید آخرش رو پاک کنید اگر دوست نداشتید) 1- بعد…</div>
<div class="tg-footer">👁️ 28.7K · <a href="https://t.me/MatinSenPaii/5040" target="_blank">📅 18:31 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5039">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-footer">👁️ 28.1K · <a href="https://t.me/MatinSenPaii/5039" target="_blank">📅 18:19 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5038">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">☠️
آموزش OpenCode، رقیب رایگان Claude Code
☀️
⭐️
توی این ویدئو: 1- با همدیگه OpenCode رو نصب می‌کنیم(کاملا رایگانه امکاناتش و اوپن سورسه) 2- طرز استفاده ازش رو یاد میگیریم و بهتون میگم کجاها خوبه ازش استفاده کنید 3- یه چیز مسخره با میمو می‌نویسیم(توی ویدئوی…</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/MatinSenPaii/5038" target="_blank">📅 18:19 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5037">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/qWsxRlQCvTrwLPfh5KYd1jPFhfMSBGEcTYCJe_4abhhLFvwQ3FAtkz1hlhJ_JgTsiIRohU_GPhleyH5e6g7WsHDBjEq5l9SgzsyShrxCyPd5NCJB3MYj-nzdTxuO8L_6DblwVHD03A0kvrenXAd9lHR8u8A5PAGDbN7AsQF3yfLSHdrMyuXW2caBI6yKc71rdLmZ0hT79bC6dBIVZm2mMT8iP9cQdLAdQ0lFH_ykySA-92uXcsg73EGI6Xh1Hh0O8NVUeze0qNXvMO_bg1wz1Pppke2XT-4hV_oqqZb28cZ4Y8O0Rpatbbwn_meyuhdbian21NP4Mn5noY8t3Ixjfg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">☠️
آموزش OpenCode، رقیب رایگان Claude Code
☀️
⭐️
توی این ویدئو: 1- با همدیگه OpenCode رو نصب می‌کنیم(کاملا رایگانه امکاناتش و اوپن سورسه) 2- طرز استفاده ازش رو یاد میگیریم و بهتون میگم کجاها خوبه ازش استفاده کنید 3- یه چیز مسخره با میمو می‌نویسیم(توی ویدئوی…</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/MatinSenPaii/5037" target="_blank">📅 18:03 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5036">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/oJw0gCWXMbg6B6P602vtdjO8Li6MAXbojLZIJe6dQ6tVQ5A0nMEbM7vBBAhy2q9dLLOhvHpOgcXDu8W_AoYOUyM2MkSqRgyR9ZkaTdFcLD5OPX25dmXfdQDrK0SzFRc_7WDs28rET2w_LHH0K4dw7SK8QI_gpG_qgU2KrMC64uEpPnFmS0J986jIEgECnY1TFG9pFCYGGR4RBuO1PBbsLdEzkYI_oarUdnGsUylNkDHqkXzeh35SCyZB2_8Q8m1lfDxOOMEUqV-uW-fhFvN5T3KLCSvutyuW0jO376ieKw_HboXKrNIKxvLHiccGm8uG--stc2HNLJLV3dLJo5GjZg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">☠️
آموزش OpenCode، رقیب رایگان Claude Code
☀️
⭐️
توی این ویدئو:
1- با همدیگه OpenCode رو نصب می‌کنیم(کاملا رایگانه امکاناتش و اوپن سورسه)
2- طرز استفاده ازش رو یاد میگیریم و بهتون میگم کجاها خوبه ازش استفاده کنید
3- یه چیز مسخره با میمو می‌نویسیم(توی ویدئوی بعدی که پشت این میاد فردا، قراره حسابی ارتقاش بدیم)
4- آخر ویدئو هم توی ثانیه‌های آخر یه چیز جادویی هست. اولین نفر برید ببینیدش
⚠️
پیش‌نیازها و نکات مهم:
1️⃣
همه‌ی مراحل ساده‌ست و نیاز به هیچ دانش شبکه یا کامپیوتری نداره
📹
تماشا در یوتوب</div>
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/MatinSenPaii/5036" target="_blank">📅 17:56 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5035">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">تموم نشو x alpha
💔</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/MatinSenPaii/5035" target="_blank">📅 17:25 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5034">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">تموم نشو x alpha
💔</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/MatinSenPaii/5034" target="_blank">📅 17:09 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5033">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">آموزش مدل‌های AI روی کتاب‌های کپی‌رایت‌دار؛ قانونی یا نه؟
خبر:
اکثر نویسنده‌ها بدون اطلاع و رضایت خودشون عملاً توی ساخت همین ابزارهایی که شغلشون رو تهدید می‌کنه سهیم شدن. TechCrunch یه تحلیل مفصل نوشته که چرا قضیه از نظر حقوقی خیلی پیچیده‌تر از یه «دزدی!» ساده‌ست و Fair Use وسط این ماجراجویی نقش تعیین‌کننده‌ای داره
🔗
https://techcrunch.com/2026/08/23/is-it-legal-to-train-ai-models-on-copyrighted-books-its-complicated/
نظر من اینه که حتی کاری هم از دستشون بر بیاد که انجام بدن، دیگه به چه درد میخوره
😂
مثلا فکر کردن OpenAI یا علی‌بابا با Qwen که خودش دزدی و دیستیلیشن از کلاد هست(
🤣
) و... تره خورد می‌کنن واسشون؟ =)) یا مثلا میان بگن آقا بیا این قسمت از کتاب شما رو قیچی کردیم از LLM چند تریلیون پارامتریمون؟</div>
<div class="tg-footer">👁️ 30K · <a href="https://t.me/MatinSenPaii/5033" target="_blank">📅 02:56 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5032">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">خب انگار قسمت نبود
👍</div>
<div class="tg-footer">👁️ 30.2K · <a href="https://t.me/MatinSenPaii/5032" target="_blank">📅 01:36 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5031">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">یه ویدئو داریم واسه Open Code
داخلش یه پلنر ساده می‌نویسیم با Mimo
توی ویدئوی بعدی که پشت سرش میاد، میدم به X Alpha و اصلا یه چیز عجیب غریبی زد.
موندم که واقعا این مدل مال کیه</div>
<div class="tg-footer">👁️ 30.7K · <a href="https://t.me/MatinSenPaii/5031" target="_blank">📅 23:34 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5030">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-footer">👁️ 31.6K · <a href="https://t.me/MatinSenPaii/5030" target="_blank">📅 20:17 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5029">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">دلار 200 رو هم رد کرد
ولی نکته‌ی دردناک اینجاست که هرچی جنس می‌خریدیم تا الان با دلار بالای 200 بوده قیمتش
الان قراره حتی بدتر هم بشه</div>
<div class="tg-footer">👁️ 30.7K · <a href="https://t.me/MatinSenPaii/5029" target="_blank">📅 20:16 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5028">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/u_k1cSFehi3jhXA60eFr-lqOHuNls07OQL0DgAQD31yFwTkyVRIaefBSyK-s9EphsAp9lfIkgnofvWdUhL9CBD5Q3lNwr5Y9LEcomykvVoO5WPew3Rev9TVd0bBbrbjkUwh0DqE_D4dYikPP3NL66pE6EC6WyMc7L0QbkMn5s1COMdF-ikSR62autwSs1G-uzM2L-v9Y7SwZDJsA6R_SVlDleQlyUa_TB3QUlm5Gy97PivUr9safUsa3NxHgjc-xNg1niGMOORt3pQNYq3n1jB3Xui8DQj8SeHjgvn08p3wOH7AtvA5srr8t_uUCU5xY5zmQh6HWMqlte1MEHV1k2A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رسیدم ۲۰۰۰
تا الان ۳۰۰ هزارتا امتیاز
دو برابر بشه میفتیم زیر ۱۰۰۰
❤️</div>
<div class="tg-footer">👁️ 30.4K · <a href="https://t.me/MatinSenPaii/5028" target="_blank">📅 19:13 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5026">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/ft440JANUNbzRFsYS5POJiv4V2bc2bhHmaeEJ6bFh6vRt5j8JQT36iNShjOZK5Nyc9kJUVVoY_1sMNG8ZLJxolsKL16etimCvbSNxFnJ2jG9gY0eR3o81-MklWBYLOJpKYEB1quSK1rUvEsj8cYlF-M2ljXUVOg0Gt73G5vtSlRbKOEQZBf8Mm-JeD7kbZHqPV4eS4C4wqBLGA0qiF2LOcDwfQn0G2e8Hw-ER4L921NblfweRc2DPulIT5SgpArGYSXO04r-vGOjSxw0ZfCjhgIcS3PtCmniuEgNDARGjew7QuNnVxV3VIcRZm5OUd26Bk4VyRwRnkAsiVu7PlX8RA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/S2wIpnSXRh0r0qdLWzC1bNdbewx_A-vwWUjXn70nD-BIwCWEOMOK6sw4IYeNt1E9EwQgTnNeYoyXux-J9EfcQBAinu59gXmJJWqylepqgFvzH9f9LUwoMG1p8PhwioiZ6504DO-0_hsvrkCiTap4dQ34i-PY_ktzt1R06RjTx7ZSCrHCyBPY5mWWe_DHKH4MNciEBfjtXGhTu1rQS0VIcV8qUF4I5PkeWP9jQ9hbe1l5M1XylizYFtgT_F-uvBWjpw7ydblcfa2MsXJrHB5HYMzHb1LyjyKwaUSp17N1NK2QJTVknM0pcdbueIttgvyRGJlNpn8S74UvhMRIpb5WwQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">یه چیزی دیدم تازگی ترند شده توی توییتر، یاد همستر افتادم
😂
😭
گویا اسمش ووچ(VOUCH) هست و طبق گفته‌ی دوستان کریپتویی، یه کمپین پولساز هستش و فقط هم یه روز ازش مونده.
اگر که تونستم جزو 1000 نفر اول بشم و جایزه‌اش رو بگیرم، یه اشتراک Claude Max میگیریم و روی استریم میریم میفتیم به جون ایده‌هایی که می‌دید. بازی سه بعدی چرت و پرت هم می‌سازیم
😂
فکر می‌کنم نهایتا 5-6 دقیقه زمان ببره انجام دادن این کارها واسه‌تون اما اگر که انجام دادید، هم به من ووچ میده هم به شما:
الف- برید توی سایت
commonsmade.com/vouch
و روی Claim With X بزنید
ب- جوین که شدید بعدش روی پروفایلتون رو بزنید. اینجا باید دوتا کار بکنید:
1- گیتهابتون رو وصل کنید
( گیتهاب ندارید هم راحت بزنید Continue with google )
2- مجددا توی همون بخش پروفایل، یه جای کد تخفیف داره به اسم gift code. کلیک میکنید روش و کد "love" رو میزنید، باعث میشه ضریب 2 بده بهتون.
بعدش بالا، سمت راست صفحه براتون 7 تا قلب ووچ میاد و میتونید به دیگران به شکل زیر ووچ بدید توی توییتر:
Hey @commonsmade, vouch @MatinSenPai
زیر این توییت من می‌تونید همین جمله بالا رو بنویسید:
https://x.com/MatinSenPai/status/2091522197537919325</div>
<div class="tg-footer">👁️ 29.4K · <a href="https://t.me/MatinSenPaii/5026" target="_blank">📅 17:17 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5025">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/oHgfJ2WleRPpcTeEoGcchJiQ4mrkIAwftjeUa8DBRMkB4Vy5v9FhUmM2Ao4HuV3qvN_gLKovKisbBITSZwl0tSwFPyNIzIEDnYTCdAx7dm21VE63mGms0RBZvXHzDg0UcrxDQ9gVN12HBFSKvvmm7mb_d1kl4oO7brRNmr3dla2KA2PU4zC_htbgFbkYExYnO5_41w_0f-hm349xIMlTGTIs6Qg82FMZ_f8kZ4x2VPtaxll4FNwTisqT7zFv0u4pFXRHUpuZe60pH4VWkXjSdhOtdMfdF6rEUMNaMMwvZ4ka-v3Lh_FrG9LX4x0MniuQntRYPnLawedVuYoE-3CJpQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">به خدا چند ساعت خوابیدما دلار کی شد ۱۹۷</div>
<div class="tg-footer">👁️ 28.8K · <a href="https://t.me/MatinSenPaii/5025" target="_blank">📅 16:33 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5024">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/1357719d90.webm?token=b0CLEZPq-C4BH5ZLcL8E2CCYkuEnTX1uEwqNtTTbLIC2bC83jq5HkoR32ACUnJmh9YQpgBk_GO4D-GEELJwBEum3xe2FC8LIFcY4vVBgB2_NrO-L0CIPMJxfJDeg-lQ14-zRZVasWQTjpZE6VAQnIbsfuse4TKxq4B8hJaJOTT7-zbQNRjkmj_C_Hq2zIKF_TAqCcGfQjv56Z94hC1fKnxrTuCNyroxo_jURfDkTmxO1fFuSlcLK_1kSKpcG3StCud7Fqw1eMAnjupEEVbsakV9j9siRgwlR_DW13pcPapnBpvHh6slbr4zRYCA-ZcTmpoyzqPzJRZBhCqOgeQ7b3g" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/1357719d90.webm?token=b0CLEZPq-C4BH5ZLcL8E2CCYkuEnTX1uEwqNtTTbLIC2bC83jq5HkoR32ACUnJmh9YQpgBk_GO4D-GEELJwBEum3xe2FC8LIFcY4vVBgB2_NrO-L0CIPMJxfJDeg-lQ14-zRZVasWQTjpZE6VAQnIbsfuse4TKxq4B8hJaJOTT7-zbQNRjkmj_C_Hq2zIKF_TAqCcGfQjv56Z94hC1fKnxrTuCNyroxo_jURfDkTmxO1fFuSlcLK_1kSKpcG3StCud7Fqw1eMAnjupEEVbsakV9j9siRgwlR_DW13pcPapnBpvHh6slbr4zRYCA-ZcTmpoyzqPzJRZBhCqOgeQ7b3g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-footer">👁️ 29.2K · <a href="https://t.me/MatinSenPaii/5024" target="_blank">📅 16:26 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5023">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">به خدا چند ساعت خوابیدما
دلار کی شد ۱۹۷</div>
<div class="tg-footer">👁️ 29.5K · <a href="https://t.me/MatinSenPaii/5023" target="_blank">📅 16:25 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5022">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">حدودا 20 روز هست که دارم با ابزارهای مختلف و AIهای مختلف کار می‌کنم و خودم رو آپدیت می‌کنم و چیزهای جدید یاد می‌گیرم، و ویدئوی جدیدی ندادم در مورد AIها تا هم دانشم بیشتر بشه هم محتوا باکیفیت‌تر. اما طی روزهای آینده، کلی ویدئوی جدید راجب تجربیات این بیست روزم می‌سازم و می‌ذارم توی کانال.
(آرک سولو لولینگ مخفی به پایان رسید
✨
)</div>
<div class="tg-footer">👁️ 33K · <a href="https://t.me/MatinSenPaii/5022" target="_blank">📅 06:33 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5020">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/MqSp2r1uyoZ58wthATQySntvjvmFaFfHf-qH5vGeleIqzDxryuZhdgpgNwe4D4qQZ5O7t5f4Bew2rM-VCbrswtW9XT52NVxEFkLBBBhuOaul-26Dh6nPQELIpRUmLiZv60Fc4hgxeAX3tIBNC64UJK2wIJRkh1pc6w7M6ErIuiqY91OcOBIFEUkZFczZcSTUmoAaWV4_Wso-PLpdG62ziFj6nIxxlq_OIKSD71_SkR9Jzy5GvlGlYX8lAsoZRao_JLVUvaY4BKnyNjJfpmx3_mGROnwD9Bdm9P7SOc_-mdfhTqINcqAvbnpAJTKaThgJTeur2qnSg7glZ8aNz7pFqw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/j2M5cHMvxihgeZZgttzUvr6eMQnmQHIa0zm7gr7dFNC_8QQFUqe3daItm448HAshn5ATUlpd_JlR7dJZmkYhpuBThuYlVinpn36_piPru204a5DNjXAtP_5nC_clRNP8bgP3XsVQnob3h_faUYqrAMiMFwaTislSeULhttpdca8XF0XQkYOHQQDuDOxvln_nLL7YKU9Z0WQXQNG7p7EamlTyvU92BlJCioSLYOtZZ4eJgt6iBafFT4RsiuuzpvXbTJrs65UT2-_kLPW_-daLDNB8ORawfyjUg3PjKfsidTBD4FAnKt1sgcWEDarKcRas7ujcz_Vxuuv6JfS3PoQK6w.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">خیلی خوشحال شدم امشب از پیام‌های محبت‌آمیزتون و از اینکه آموزش‌ها چقدر کاربردی بوده واستون
❤️</div>
<div class="tg-footer">👁️ 32.5K · <a href="https://t.me/MatinSenPaii/5020" target="_blank">📅 05:25 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5019">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Ox81ts8OsdwGzYL_4ZyaksgCB4eRFk3NO_OD_ETTecRmBn8rILExqvezGfVZ1HvC2u2ozIZcZPyH5eZyVCJe2SLy8nLB9k1dzdqMJgSKE1HLe0JpCeVqUrBVhudcW1H1j6bTsjoviLIEBTv1dm1Ea03N32Av3rezXNv3Nj2X1K3uRG4r_LxB6oHULt9obbpOn35IJg1SeNHzWOl8zDuKdCNKRAl9MKoTRCgz_TRLoenVD3w-eLymgPoVbVWyFy_k0Uu3S3cwL1MjskbmFu2XQr4YOhmPSiDcHqmazhjY3sTvtzrPwJ5IIYONikSmypNQy3aZHr40bINqVH2g_9cj-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">به نظرم یا مدل جدید شیائومی Mimo هست یا به قول یکی از بچه‌های توییتر مدل جدید خود Google(جمنای ۳.۵ پرو). گوگل هم ماشالا ید طولایی داره توی این ناشناس مدل ریلیز کردنه
😂
خواهیم دید چه خواهد شد اما تا الان خیلی خفن بوده</div>
<div class="tg-footer">👁️ 34.8K · <a href="https://t.me/MatinSenPaii/5019" target="_blank">📅 17:25 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5018">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">خیلی توی کامیونیتی خارجی بحث و جدل شده سر اینکه حدس بزنن این مدل جدیده مال کدوم شرکته، چینیه یا آمریکایی و OpenCode هم اعلام کرده که دسترسی بهش نامحدود هستش تا هفته‌ی آینده و روزی 100 تریلیون توکن تمام کاربرا می‌تونن استفاده کنن مجموعا و ظرفیتشو دارن
😂
همینطور…</div>
<div class="tg-footer">👁️ 32.9K · <a href="https://t.me/MatinSenPaii/5018" target="_blank">📅 16:41 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5017">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">خب من این آفر سه ماهه رایگان اسپاتیفای رو تونستم بگیرم با همین روشی که اینجا یاد دادم  مزیت بسیار بسیار بزرگی که داره اینه که میشه به گوگل پلی وصلش کرد و عملا توی هـــر بازی‌ای خرید کرد. البته من با VPN آمریکا chain شده رفتم که ساخت این رو هم یاد میدم بهتون…</div>
<div class="tg-footer">👁️ 35.7K · <a href="https://t.me/MatinSenPaii/5017" target="_blank">📅 08:23 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5015">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/ONhPpjjbHLVb17jLkncHxyTo3pzXfQC28qF1NYQw1QSO77BfzbbQQxOPMm-_8GtuLScTQfcDDjnhbTDGcszpDoc8tYL4DYkQioF0q4gIydJ0BU9EhXi5DjmkL4Gw-hxfDW12Sk-drKsRd25pM7tFI42SgY1a4-nNn3Cvs_FbN7vORWx9_SRZ42Wl9YF9c0fM8vUeLMR5JJdAl3_ps-LGKb0mPqp8r0C6FFDn_F8FfHEwtKZwN8LJtU5Uz2o2yqiQ1oBZ8Md-xOWHq4UKtBCcPf1MSAkZ-GZ4Kj16rMxdPVQw-Z-nJRs8Uj_odMYoy_H-lMN55e1TWRvorXubqA7HoA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/VwPKWG65cdFOxcdnRRkLRfxBbxdv-E1HZ2YVc5L2U62vMXGS2XCXEAGqQ29YLbYW24ujd9chj5M3Vno86MQXBtevwDQaOd4LCbAGybNfToOUJNQPlwM-6CCp_JS0VIcGkF9pnUL6tGsLKMcgUuuKZgW7S-3Cy_DkxmmfjcBHyPmylRIG9L1oAU5yVTaJO4ErnEed4fTKthTkLf5hs4B8TCaJ93dgwIwrMT8wl9qa1QRLbeS0Wxx98H-82cbYtxNRPNOnNYpWSs4S3lEbPncT001hMCFfAhqo5nFQy-9aJTP53lZU4oqR9Q1NnvSLxYUQhcy6vn64WhVvHqrvVxXEHA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">خب من این آفر سه ماهه رایگان اسپاتیفای رو تونستم بگیرم
با همین روشی که اینجا یاد دادم
مزیت بسیار بسیار بزرگی که داره اینه که میشه به گوگل پلی وصلش کرد و عملا توی هـــر بازی‌ای خرید کرد. البته من با VPN آمریکا chain شده رفتم که ساخت این رو هم یاد میدم بهتون
تا الان اینها رو تونستم بگیرم باهاش:
1- اشتراک ChatGPT(بیست دلاری)
2- توی کلش رویال کلی آفر گرفتم(رایگان)
3- توییتر پریمیوم(فکر کنم ۹ دلار ماهانه بودش)
4- پلن رایگان Hermes Nous Research
5- همه‌ی پرداخت‌های گوگل پلی(با آیپی آمریکا زدم. و یه سری آفرها رایگان)
6- اشتراک OpenCode Go(5 دلار)
7- آفر سه ماهه رایگان اسپاتیفای پریمیوم(با گوگل پلی. هزینه یه ماه بعدش رو هم کم کرد یعنی ماهی ۳ دلار. حواستون باشه)
و در کل اکثر جاها میشد خرید کرد، تنها چیزی که نشد بگیرم آفر رایگان GPT بود که انگار واسه‌ی خیلیا خارج از کشور هم قبول نمیکنه کلا.
و مجددا همینجا آموزشش و مابقی مزایا و معایبش رو گفتم:
https://t.me/MatinSenPaii/4917</div>
<div class="tg-footer">👁️ 35.1K · <a href="https://t.me/MatinSenPaii/5015" target="_blank">📅 08:20 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5014">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/GX-HKetuS7SKO4CUql89HYPqXp-ywCpZCJRFlQ0iEfKrOwvO_1uLk-q2DM5eLO4YdxphT1DbXgOhqZ55gBkm1h1AO_LhhKD7V4-6a3_kX2lQmgLa9PF9DkpWbiQMQ6XmT3CxmPYrklIdhTLdEYvImRpQN8k8jCCBGZSO9qhojqDb0Py_uoxns47mHu_i_JdQWtQWwrgp-6gqFQlMAlZqxtUOP-FNlopXsZxAc5z1tQJMud0RGTB0k7NuVVydGO6nFK9iiFqGZL4J6VeAt_5IYiiZkwZxmv3PAMUrCIC-0RfSd15DbRh52-_aZdc5xnI0gVCyqpnmDQmkK1r2AM515Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مدل جدید و مرموز x alpha که روی اوپن کد اومده به تازگی رو می‌تونید این شکلی تست کنید روی 9router: https://x.com/MatinSenPai/status/2090856359117902053</div>
<div class="tg-footer">👁️ 31.2K · <a href="https://t.me/MatinSenPaii/5014" target="_blank">📅 08:04 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5013">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">فکر کنم وقتشه کم کم یه لیست از چیز میزای رایگان و آفر و... هایی که با این سایت تونستم بگیرم بذارم</div>
<div class="tg-footer">👁️ 28.5K · <a href="https://t.me/MatinSenPaii/5013" target="_blank">📅 07:46 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5012">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/SN5yHjlPtJ9li1cY0s7OuqeFEacR6KpW3LqZSqCU4fX6GApq1byUX4E41P0iugrgC--HWJdO2sZ-tEfMGG1erUsWnM-jAlrznvHIuGBTw_u3oCZGcMzFRyboowcd245KyNWQ1xLMj6ouS5xEOIuzY5Oq4G-tf6x6KF5Tf_dyDGQqJKkMK-RIZMuzXFD8ZcWzN6OmNDVJ2Meldc6vdh8PMIkuQnXw1iQ9jnteKNj9p43wifucrXOzs7G3UqfU9bqtSwIs7VKA5quoPSFOv83EAnWn3YLVx_gxTiPF8C7l7J2YHxcnYP5GtDvqBbUCIM6gARsfPVZEDmt8kY5T9B5vYQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یه سریا هم یه جوری شبیه دی‌کاپریو میگن «اوه این پروژه وایب‌کد شده» انگار مچ معلم مدرسه‌شون رو وقتی دستش توی دماغش بوده گرفتن.
همونقد معصومانه و مهدکودکی</div>
<div class="tg-footer">👁️ 29.7K · <a href="https://t.me/MatinSenPaii/5012" target="_blank">📅 07:39 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5011">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">مدل جدید و مرموز x alpha که روی اوپن کد اومده به تازگی رو می‌تونید این شکلی تست کنید روی 9router:
https://x.com/MatinSenPai/status/2090856359117902053</div>
<div class="tg-footer">👁️ 30.9K · <a href="https://t.me/MatinSenPaii/5011" target="_blank">📅 23:07 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5010">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/YZwz4r4Dr-9Vo7DtSFQG_AlLI6vIEt-lvlrI6qW4skvAfoJRLezNoSgntsYBHyfw7HiRKH_zpZtLGcKEqkgJiLWDVv1bPaTVwqJSJNryyLcK_udANW_mAleixEvhvASpxzA3xHgDh_CCjykcXSyR3zVpcq1i-CjPyDayR6QOrCDJX3cKCXdP1NX-K9FMjkidCsrRHsWMtcrT6_aK1mUQU3c9oczI6pqhK1kotRJQwwe2XSvg6QYLiT5b1dZjmCx8lMEo2P70rXog4TVqDqSO7fLKVDvhvNxh6r5sqEWSM_qc8DdzKIHuotyHkJtcQGYrqHlzW4m0Xq92sniAHT4CXw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔗
WhiteAesther Android ورژن جدید
🔥
🔥
🔥
🔥
🔥
نسخه ۱.۲.۱ — رفع سه مشکل اتصال
این نسخه قابلیت بزرگ جدیدی نداره؛ سه تا مشکل رو رفع می‌کنه که باعث می‌شد اپ روی خیلی از گوشی‌ها اصلاً وصل نشه. اگه ۱.۲.۰ داری حتماً آپدیت کن.
🛠
چی رفع شد
1
.پروتکل های wireguard و warp in warp برای خیلی از دوستان اصلاً وصل نمی‌شدن
توی ۱.۲.۰ «ثبت‌نام مشترک بین پروتکل‌ها» رو به‌عنوان یک بهبود اعلام کردیم. اون کار اشتباه بود: وقتی MASQUE هویت رو ثبت می‌کرد، کلید WireGuard روی سرور Cloudflare پاک می‌شد. بعدش هیچ اندپوینتی جواب نمی‌داد و اپ می‌گفت شبکه بسته‌ست — در حالی که مشکل از هویت بود، نه از شبکه.
حالا هر پروتکل هویت خودش رو داره. اگه از ۱.۲.۰ آپدیت کنی حسابت از دست نمی‌ره.
⚠️
در عوض، اون کاهش سه‌برابری احتمال rate limit هم برگشت. اگه زیاد نصب و حذف می‌کنی، حتماً از
Settings ← Identity & access
یک بار بکاپ هویت بگیر.
۲
. عوض کردن پروتکل وسط اتصال، همه‌چیز رو خراب می‌کرد
اگه بدون قطع کردن اتصال پروتکل رو عوض می‌کردی، جستجوی اندپوینت از داخل همون تونل قبلی رد می‌شد — یعنی هزاران درخواست دقیقاً به جایی می‌رفت که قرار بود جایگزینش کنه. نتیجه: هیچی وصل نمی‌شد.
۳
. گیر کردن روی پروتکلی که شبکه‌ات بسته
پیش‌فرض قبلی H3 بود که روی UDP کار می‌کنه. اگه شبکه UDP رو بسته بود تلاش اول شکست می‌خورد و اپ دوباره همون رو امتحان می‌کرد. تا نوبت MASQUE H2 برسه چهار دقیقه و نیم گذشته بود، و عملاً هیچ‌کس این‌قدر صبر نمی‌کنه.
✨
چی جدیده
حالت Automatic — از
Routes ← Manual ← Protocol
گزینه اول حالا Automatic هست و پیش‌فرض هم شده. خودش سریع امتحان می‌کنه ببینه شبکه‌ات چی رو اجازه می‌ده، از H2 شروع می‌کنه (چون TCP روی پورت ۴۴۳ هست و شبیه HTTPS معمولی دیده می‌شه)، و هرچی جواب داد رو یادش می‌مونه تا دفعه بعد از همون شروع کنه.
روی نصب تازه: ۱۴ ثانیه تا اتصال، جایی که قبلاً چند دقیقه طول می‌کشید.
گزارش خطای واقعی — قبلاً اگه جستجو نتیجه نمی‌داد فقط می‌نوشت «اندپوینتی پیدا نشد». حالا می‌گه چرا: بسته‌ها از گوشی خارج شدن و جوابی نیومد (مشکل از شبکه‌ست)، یا اصلاً خارج نشدن (مشکل از مسیریابی خود گوشیه). لاگ خود موتور تونل هم از این نسخه داخل
Settings ← Diagnostics
هست — اگه مشکلی خوردی همون گزارش رو بفرست.
⬇️
دانلود
https://github.com/WhiteDNS/WhiteAestherMobile/releases/latest</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/MatinSenPaii/5010" target="_blank">📅 21:38 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5008">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/OMpCUCfv_sEyrRK4ZDqdcJRfg3N5G5uch-sq_T_gFuzCoOcb9n8qIpHcaIL4aGDvYBDwf84pMpgsByXGzFXV8mUpuiNcn0Qs-8MKcJDpiQlAZSLdLHJD50lnU7D5P1QYV7xTPN4DoKUN2g_Q-uRuKU0LYaP-RuBV3jCO3wiFtOYPKuTnl8nu8qKGaActOXzwHyoscxHySwGfNQ7YRhqsGj5lOsTthgiFcTo5vYgZiZIPXqUo54sKhCpN5bsrRHiigyE26imEUETIX9CRB8pj5gi33UWObl_fFXvlYTDDjZ3KSGw9EYkEB3iIJPsduAe0kxN0mcVkJLPLtSyOI3svBg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/ca9HQgFh9woJ7BTHeIJLRFn5ABoOvjZW4C6PaUjXDGU4DgkbvjA-YoQ08fxij7lB3Ed8E7VRRYG26O5zFmjGXEkql_jukTas0V0uriGbx90xXhtCe83PJV1WCIWII6xS5dWryWYf4d5L-QzHLEeCqoeiiyI8mVoRnyaxVPYVNM0F6xmeDS9k058N91g8lyUCJ6tExLXYrkg_RWgbtreCg7LiVFRCpJHBKa2wbyjTnlgXbN-8fVsKQ7E08EcDVGCMMUaiDbWQhLnl9S2_iyEqZ6nwj9XoBvrYhkKJmVqWlH8yu3lkgq0-sUpx99AHRr9A-3FwqnMxEV6Kt-6A1fz4LQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">اگه حوصله خوندن توضیحات رو ندارید، فقط ساب زیر را وارد PattNG کرده و لذت ببرید !  https://raw.githubusercontent.com/patterniha/Free-Configs/main/configs.txt  ساب هر ۲۴ ساعت آپدیت میشود. /// توضیحات:  چند تا از پروژه های عالی که کانفیگهای رایگان را جمع‌آوری…</div>
<div class="tg-footer">👁️ 28.7K · <a href="https://t.me/MatinSenPaii/5008" target="_blank">📅 15:11 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5007">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromPatt's Channel</strong></div>
<div class="tg-text">اگه حوصله خوندن توضیحات رو ندارید، فقط ساب زیر را وارد
PattNG
کرده و لذت ببرید !
https://raw.githubusercontent.com/patterniha/Free-Configs/main/configs.txt
ساب هر ۲۴ ساعت آپدیت میشود.
///
توضیحات:
چند تا از پروژه های عالی که کانفیگهای رایگان را جمع‌آوری و تست میکنند و سپس کانفیگهای سالم را فیلتر و در اختیار قرار میدهند پروژه‌ها‌ی
https://github.com/0xRadikal/Free-v2ray-Configs
و
https://github.com/itsyebekhe/PSG
و
https://github.com/Delta-Kronecker/V2ray-Config
هستند.
اما این پروژه‌ها دو مشکل اساسی دارند، اول اینکه تست کانفیگها باید از طریق اینترنت و فایروال ایران انجام شود ولی در حال حاضر تست کانفیگها در این پروژه‌ها از طریق گیتهاب انجام میشود، دوم اینکه روی نت‌های آپلود محدود (ایرانسل و ...) عملا اکثر کانفیگهای این پروژه‌ها آپلود محدود هستند و کیفیت بسیار پایینی دارند.
از آنجا که با روشهای زیادی میتوان محدودیت آپلود را روی کلودفلر دور زد، من در پروژه‌ی خودم اومدم کانفیگهای کلودفلر سالم را از پروژه‌ها‌ی اصلی جدا کردم و تغییراتی را برای دور زدن محدودیت آپلود (و همچنین دور زدن فیلتر دامنه) اعمال کردم (در حال حاضر متد fragment+fingerprint اعمال شده). بنابراین کانفیگهای نهایی سالم و با حداکثر سرعت در تمامی نتها قابل استفاده هستند.
برای دور زدن محدودیت آپلود در نتهای آپلود محدود در حال حاضر فقط باید از کلاینت
PattNG
استفاده کنید، بزودی در سایر کلاینتها نیز این مورد پشتیبانی میشود.
https://github.com/patterniha/Free-Configs</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/MatinSenPaii/5007" target="_blank">📅 15:09 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5006">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/HWUXwoY4Oj3oqVr6ta9kcA-5dv9PVo37cL-esLVkemUKDtI3dxIEUTCdSAWG1o30SMPlizbjHJtQmbWL6IdYNmjQGqnEW1J1LQ6L3e3N6_cxV9_qSyqo9JZOmCfpQQ4gllNFWeftGwwSwsiQ2emKYqjqJXKJ5kc7K4GDJPJdfJGCnqx_2kKDDZF5d6kTgnlhyqqEEDKRe97DvAtJpo6gDgEg0TSLBSrIlanQmSF6_xkMfvoj86kRl6CbnjzHWpOiF1ADA0E0qOwsvsAE6Dnv_fpIWOFg6lt7TZAw9vwoYo_8GeBXMFH5rFO5pe3a4LFvHO8gRf2kbAg2t2uQjYLu-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یه مقایسه‌ای دارم انجام میدم</div>
<div class="tg-footer">👁️ 34.7K · <a href="https://t.me/MatinSenPaii/5006" target="_blank">📅 03:19 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5005">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">آقا این Muse Spark هم عجب چیزیه:) روی هارنس درست به نظرم شاهکار میکنه. فعلا روی OpenCode به شدت سریع و اوکیه</div>
<div class="tg-footer">👁️ 35.3K · <a href="https://t.me/MatinSenPaii/5005" target="_blank">📅 03:17 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5004">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">بیاید بریم Rust یاد بگیریم لایو هستیم روی
🟩
: https://kick.com/matinsenpai</div>
<div class="tg-footer">👁️ 37.7K · <a href="https://t.me/MatinSenPaii/5004" target="_blank">📅 21:00 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5003">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">بچه ها بازی Rust نه. زبان Rust:))</div>
<div class="tg-footer">👁️ 39.1K · <a href="https://t.me/MatinSenPaii/5003" target="_blank">📅 19:11 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5002">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromMatin's Dungeon(᯽マティ️️ン先輩)</strong></div>
<div class="tg-text">بیاید بریم Rust یاد بگیریم
لایو هستیم روی
🟩
:
https://kick.com/matinsenpai</div>
<div class="tg-footer">👁️ 38.7K · <a href="https://t.me/MatinSenPaii/5002" target="_blank">📅 19:05 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5001">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">آپدیت جدید Aether:
توی این آپدیت روی مسیریابی (روتینگ) و اتصال از پشت پروکسی کار شده</div>
<div class="tg-footer">👁️ 38.8K · <a href="https://t.me/MatinSenPaii/5001" target="_blank">📅 03:22 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4999">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromMatin's Dungeon(᯽マティ️️ン先輩)</strong></div>
<div class="tg-text">هوش مصنوعی و برنامه نویسی | آینده این شغل
لایو هستیم روی کیک:
🟩
https://kick.com/matinsenpai</div>
<div class="tg-footer">👁️ 38.5K · <a href="https://t.me/MatinSenPaii/4999" target="_blank">📅 21:45 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4998">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">حس می‌کنم شدم هوش طبیعی متین سنپای که پول توکنش رو نمیده
😂</div>
<div class="tg-footer">👁️ 38.5K · <a href="https://t.me/MatinSenPaii/4998" target="_blank">📅 20:45 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4997">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">بچه‌ها شرمنده می‌کنید با استار هایی که میزنید. ممنونم
❤️</div>
<div class="tg-footer">👁️ 38.1K · <a href="https://t.me/MatinSenPaii/4997" target="_blank">📅 20:44 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4996">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromRick Sanchez🤍ریک سانچز</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/n_2d5P1WSWx7c8YrSCXul0Z9jYNCbiSKKp3NbQ67nij48LHB4nMhyExqgTdKsqhZz2unSIoSGOatBU2rf2p4nksZ_svXIQ9pcIajg27EOjsTIvr_1JINFCKLb1CbegqI6DdOu1HaUHF3Mamg4cgDqR5PWDnAg09Urrw1OL1d9qlu8HW6ay3UjfkZSBM-jDdMkrzTAVgY2uliwUBQkUIWWPh24-TUVaJtSUGJjpVucFdvMlDWN7hFBkGI-Z3_MjHsfsy9R8-Ob1Ib3xD9UYwkduKYoePtq4a5qOJfhhC2E7IouwkzeBonRuAOaMsjk8C73ohadgfVyNDtIRwdW-5YsA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نصب هرمس وب یوآی با یک کلیک
متین سنپای
بهم گفت که Hermes WebUi نصبش سخته و بهتره با یک کلیک بشه نصبش کرد برای همین روی پروژه اصلی PR زدم که اگر تایید بشه از این به بعد میتونید راحت این پنل رو نصب کنید و ازش استفاده کنید.
لینک PR:
https://github.com/nesquena/hermes-webui/pull/7152
میتونید روش ری اکت بدید شاید تاثیری داشته باشه.
اگر هم تایید نکردن مهم نیست
یک پروژه جدید روی گیت هاب خودم اوردم بالا
لینک پروژه:
https://github.com/nesquena/hermes-webui
میتونید به هرمس بدید و بگید براتون نصبش کنه
خیلی ساده همون پروژه اصلی رو میاد براتون نصب میکنه
حس می‌کنم شدم هوش طبیعی متین سنپای که پول توکنش رو نمیده
😂</div>
<div class="tg-footer">👁️ 38.8K · <a href="https://t.me/MatinSenPaii/4996" target="_blank">📅 20:42 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4994">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/Zh4rK8RxqisLylIg6gAKBg6KBaiuFDLeVemdlluhM1Bpd8RXKay0CHzhFfj3yNGHyQZIO50iGYJ9B_QWqMBi4SlhkXn11J_RzbXOMMRYUvW03xzLeCV8OxZai6PQ1JNHmkg-MaWE8GyYE674F0ZsTlvSjpT51DS1xVhxPdiwPlkGw88lZcDFpzBQC4xNH-BOVPHSoD3RHzo6GAEjZAnzWQF5zQ0CF07tRc3HKmiZFHxMPzPiR9c0rTDBZpDEGheATndPTP82HUgqDs6jGf13VzDru3RQNpGvXA_NUC3dMahXV_ZE6lX9N74wBXt2kqnCgU_u8dBOolvJfo2vqxuznQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/AK6X0HM3lDvy3X_PY50wDZDWnHtciRT47XLYh5OAIQR3b1pAEfQn1hYn73eMHeFWYdFYrV_qdgbcJonE8tAcDBUUFM5qwzvsJciFt_Uayn2qDHFaHSRgJMIQH1Cj0_amWmLPV4244MA8VvLP0V5D7FA4JT78c0hv8EmeU01tWpSTmFuCe2rpTFLbAccmsduCkJrFTPIk_yW-vMbXpadPCULX-GKmdTetKMjU3fseH0E7GxZovcDfhwX11GcEwMVZ5qZgjZESIlq5E5-WjUTnUcFXL-m5u135evFpaTES5ZOtQRyHx_-J27B86-7_-KWnbqlpYTaK0n2lUNiFYnaPmg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">روش پرداخت بین‌المللی و گرفتن Visa Card مجازی  خب دوستان، امروز می‌خوام بهتون یاد بدم چطوری می‌تونید با این وبسایت، برای خودتون ویزا کارت بگیرید: https://app.mpay.cards?startapp=ref_PzwXZ8 (لینک رفرال هست. می‌تونید آخرش رو پاک کنید اگر دوست نداشتید) 1- بعد…</div>
<div class="tg-footer">👁️ 34.7K · <a href="https://t.me/MatinSenPaii/4994" target="_blank">📅 15:42 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4993">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromMatin's Dungeon(᯽マティ️️ン先輩)</strong></div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/K5mtHHXsa2SrTIsuqJXt0EDxcNjJgHmA1XDHdjTRv2znwpIKc8Nc_yr_7T11yRylY4eWN6gdRGdsZML_hNC1aUZGHqonsXv25jy4IDNwuG9yv4ZSvHnkiUZoSZfDA-B2yJXhoJfiORNtWjHW1vfpaqosCwVk9E7AZj1-Wqv1v4RJ4UACaoXv5kp8OlQvy5tsbcaxZCUH326N7GbRjGfo1tb3DucMh70tIXze3he1U8KTRWzU5_dPA4opS9M_xHQsw6p2oSUxED1fRt0p7btl9cdSt665F-sizD1EOHxrJmIEbpJYmVeqpvNxrGRkg3l0rozd9CtWu1FwbfTRudDsOA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سرویس استریم شخصی هم نوشتم واسه خودم که با نت داخلی بیام روی Kick
(تانل rathole
😂
)
هاهاها
به من خندیدین؟
🔥
🔥
🔥</div>
<div class="tg-footer">👁️ 36K · <a href="https://t.me/MatinSenPaii/4993" target="_blank">📅 08:02 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4992">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Qsd5_tgxYaDy2lnUGdiFJ9cvp01pAMqGHgq1SBRfKq5cj8QeacSm-K7UNsq3zfPFclkz7E5fzFXZTdQp_Lw-S4tHrB46yQerXcIIsoumhmFVdnx334GM4t2FNnM0k74I1oTq_Wihj5iRJ-ioOoTf3lkm1I9qk4MtJOcRCbHYfrZS9CeiNiZh6DTtZjsf5xjRRTvIUPpYiLOgVdxkCxTwcBRG7Y71e1yGxt5-hPXvDfkbsv8IrxihRYJ3Ev61CbZEaYRXfc9nuAHEXEfdMaxs6M0SckPo5DophNLdSd_lUA590unnw19WZlSbsqq6GwIdBz7UAZxUggbRrSJJSYp6Xw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تجربه من از 5 روز کار با OpenCode Go
https://x.com/MatinSenPai/status/2089928470801318139?s=20</div>
<div class="tg-footer">👁️ 35.9K · <a href="https://t.me/MatinSenPaii/4992" target="_blank">📅 07:47 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4991">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/IADRLm8AdthjPacENzj3id-wUwnRiEijcV33eeto2qLncqvH-AVQAPZKOKDvNTA6El0so1KkvFvTvbKJVQIYl1lwc1-E7u8h5hTmcMHzEtH0ARIMmilE0ktOyq2nYShYOPE_WArzxR-UaYfQVr_yCj-8vYbSVlkWbXB1WGy5p76m_-vNdNKOd6Xqnl3ZxA9WNipc02APVKYWnpqmKAN8VJtDstiI8J4Oh9Xpqt7RtZQuAkVmE2WmfLzAOgDm24vZNQSEIg82k1XHWfg6OhaIc9mKd8wFzwS3GXu1jKeFqzmFX_3ZRVI9H9a7ZHKy3Nc4DkNixeq0E34VQIovLDXsuw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترکیب پنل BPB + متد پترنیها + Chain Proxy داره بهم سرعت آپلود خوبی روی آیپی ثابت میده</div>
<div class="tg-footer">👁️ 37.2K · <a href="https://t.me/MatinSenPaii/4991" target="_blank">📅 23:24 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4990">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">لینک داشبورد کلودفلر:
dash.cloudflare.com
لینک ویزارد تحت وب BPB جهت راه‌اندازی:
https://wizard.bpb-panel.workers.dev/</div>
<div class="tg-footer">👁️ 41.4K · <a href="https://t.me/MatinSenPaii/4990" target="_blank">📅 20:50 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4989">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/nQ6nhLetC8-hYwbGZ7CZP2yGEtyVKeN4nTnfJXC-iB9vOeHI0t0P0yOn9RE5dfkRaWJ0lvudEhmbF0H6VjRlbmloHQxX5gyLU7GbEJ87vAi7_fDraSFIglUWcdt8O2JtKWxEtN_7qfW6DthA9q1ZETsHjFS6b54eyZEGJM751KCqsiJl9Jf5USOhNcsJ2DJZSOeIzFtcKiHq3e_X7fzy9hrnPHGY1bdhGQ2of4X6L3fZ3f1w2M3ZNKwVuDPhVhUquvOS686TAhAk4UOEEQZIehXARgpcJ5GIQca1ie6RnhHrrD8CGFwoTnts-qUpoAScgF_THBR8uCQgVj2awwHJjg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">☠️
ساخت VPN رایگان بدون سرور با پنل BPB! ورژن 5
🌊
⚡️
لینک‌های استفاده شده توی ویدئو:
https://t.me/MatinSenPaii/4990
⭐️
توی این ویدئو بهتون یاد میدم که:
1- چطوری با پنل BPB برای خودتون VPN رایگان بسازید
2- روی گوشی و سیستم چطوری ستاپش کنید
3- و برای خودتون و خانوادتون، از یه VPN امن استفاده کنید
ویدئوی آموزش تنظیمات:
https://youtu.be/7G9Fjhe_NxM
ویدئوی بالا بردن سرعت آپلود:
https://youtu.be/dQKfkXnThCE
📹
تماشا در یوتوب</div>
<div class="tg-footer">👁️ 42.4K · <a href="https://t.me/MatinSenPaii/4989" target="_blank">📅 20:46 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4988">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">ویدئوی BPB دیرتر میرسه و می‌تونید اداره برق رو سرزنش کنید
😭
😭</div>
<div class="tg-footer">👁️ 35.1K · <a href="https://t.me/MatinSenPaii/4988" target="_blank">📅 19:38 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4987">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/NlFqbe0FCKrhkFw8K98ILrUuOxaM-p9jDuXHa2DPZdct6kWtDvbZjsMPkPt-qGa9UjLCFQ8qbH1E5ocRFRWMcbxgm7gMbfvuKh2CkUBfSg5zWE1A7aET31wqCUn1oessVI6SM8G2NIAg5uff7q2ErjG88H9Mi9gjLD1ZTtbGvopvozPdGza6tCVta1DoaNGDtvAjuWZJU9T23U0UGpt9t7labzXqqV9e00UP3MIw8oHDyls1QpYOTmPHZapyuN5A6r2E2KXAQuoJPkE9IWFvxy5-4IhONEkQv03A3WEzyhScTcIbn2UZi1vUk0LvwCbnqF_hySd79QHzPOH1RG7i-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">WhiteVPN دسکتاپ هم سرعتش عالیه. تازه با ساب خودش هم دارم یوتوب می‌بینم</div>
<div class="tg-footer">👁️ 37.5K · <a href="https://t.me/MatinSenPaii/4987" target="_blank">📅 13:38 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4982">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">WhiteVPN-V1.5.0-arm64-v8a.apk</div>
  <div class="tg-doc-extra">35.7 MB</div>
</div>
<a href="https://t.me/MatinSenPaii/4982" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">WhiteVPN V1.5.0</div>
<div class="tg-footer">👁️ 33.6K · <a href="https://t.me/MatinSenPaii/4982" target="_blank">📅 13:31 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4981">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RF9w3voTcpFU2txrs12taIdphqTfkQGCDybi6cGyWBbsJzTdFAlGrXzS_PIr-4cUDjeZMZbh9o7WEDAwkGmDOKEayXs7GpQmEKhtb2wUt1TNG58M_KvttZeOGtE4YiJyyRF76xZ7n46wMniiKxjSodGb9or_TsctJABgQE_6sfIM1Y0CAAyOlK1K1Mbwmlp12Gmra63UjKDrAn3RaTVjHDSxFdqUipgusfgbdz39oda_r5RjgXPrEcL-eBeHRPe4OlzJS7gHv5m6O6TePhW7lWudRuKgWsEBTq6qrEOEXmEy3l6RPi0GM8-srwE9GCvAxP2MD3z7azTPftM6Y_5srQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نسخه جدید WhiteVPN v1.5.0
توی این نسخه سعی کردیم پیدا کردن یک اتصال خوب و سریع خیلی راحت‌تر بشه. اول همهٔ اتصال‌ها بررسی می‌شن و بعد، اگر دوست داشته باشید، می‌تونید سرعت هرکدوم رو جداگانه تست کنید.
حالا می‌تونید زمان، تعداد و حجم تست‌ها رو هم خودتون تنظیم کنید تا هم کمتر منتظر بمونید و هم مصرف اینترنت دست خودتون باشه. ظاهر و بخش‌های مختلف برنامه هم مرتب‌تر شدن تا انتخاب اتصال، عوض کردن سابسکریپشن و پیدا کردن تنظیمات راحت‌تر باشه.
⚡️
تست اتصال‌ها سریع‌تر، دقیق‌تر و مطمئن‌تر شده.
⚡️
برای گرفتن نتیجهٔ بهتر، تست تأخیر حالا از سرویس پایدار گوگل استفاده می‌کنه.
⚡️
تعداد اتصال‌های هم‌زمان، زمان انتظار و حجم تست سرعت قابل تنظیمه.
⚡️
تست سرعت دیگه خودکار انجام نمی‌شه و فقط برای اتصال‌هایی که خودتون بخواید اجرا می‌شه.
⚡️
تست تأخیر و سرعت از هم جدا شدن تا خطا و تداخل کمتری پیش بیاد.
⚡️
می‌تونید چند کشور و چند نوع اتصال رو هم‌زمان برای تست انتخاب کنید.
⚡️
انتخاب و مدیریت سابسکریپشن‌ها راحت‌تر شده و از صفحهٔ اصلی هم قابل تغییره.
⚡️
صفحهٔ تنظیمات، تونل تفکیکی، اطلاعات اتصال و چیدمان فارسی مرتب‌تر و ساده‌تر شده.
دانلود آخرین نسخه از گیت‌هاب
https://github.com/WhiteDNS/WhiteVPN/releases/latest</div>
<div class="tg-footer">👁️ 28.3K · <a href="https://t.me/MatinSenPaii/4981" target="_blank">📅 13:31 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4980">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">امروز ویدئوی پنل BPB جدید رو داریم</div>
<div class="tg-footer">👁️ 34.2K · <a href="https://t.me/MatinSenPaii/4980" target="_blank">📅 12:34 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4979">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromMatin's Dungeon(᯽マティ️️ン先輩)</strong></div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/IuafyeyHj1jQDHVcaBkfdA3WBukz3HiYRm9icicew0mN9yxlVVXditZPyCO8MlmOAbsLzi-Ur7NQybN-PfQQvDxv0lU1E8gzqV8S3VJAkiRly8K1bFOAC7dumLLktAS-dcOmDCiNEShrsra5oESyZAqj7deJR6RJ3ovrnetsvd25Z_Q38R-qYpo5FGFiMRPxFx6GCpoyqhg0T1TI2pYmYEqgO4TSkHgF-j54HTuaDQTAGNjpRza8URyENgYDF17p17Fii0jWgJ_avOZXUDmQHgopdUOcNOU3gko5B7BmUeHxhmwv8jYs84gseTOgsCKO7gqjTa85QwdGA9GDFfFGaQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دمتون گرم بچه‌ها
مرسی از همه‌ی کسایی که اومدید
شبتون کانفیگی
😂</div>
<div class="tg-footer">👁️ 38.2K · <a href="https://t.me/MatinSenPaii/4979" target="_blank">📅 01:36 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4978">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromMatin's Dungeon(᯽マティ️️ン先輩)</strong></div>
<div class="tg-text">بفرمایید لایو
https://kick.com/matinsenpai</div>
<div class="tg-footer">👁️ 35.2K · <a href="https://t.me/MatinSenPaii/4978" target="_blank">📅 01:04 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4977">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">اگر دوست دارید استریم‌ها رو دنبال کنید، جوین بشید:
https://t.me/matinsdungeon
امشب یه لایو کوچیک خواهیم داشت که کمی گپ بزنیم و صحبت کنیم راجب اینکه قراره چیکارا بکنیم</div>
<div class="tg-footer">👁️ 35.1K · <a href="https://t.me/MatinSenPaii/4977" target="_blank">📅 23:36 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4976">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/AXqdGNXSrlv9nBUvumtw3GdLcdoeTzajjfPPuRy9F5QanqfvYKPvV3eNFT_XvbnR5o_4svkxDkrxGduJ43-O2m9xTrmXcDDr-nI3m37Xtly0SvEo0Lxzqoew5AOJArP-0I7rpfmGhqwtk3UBqozqqryQrufS8SFTbFQ5lif5RouCbgqjShQogrQbG-8cHQHY0QGkr56WUgTQx0_GbFZtbtVxD2i1J-dTqxFy-BALMyxiusEbH1QpnzWscNIqvvsJXTHEQvLpEHXsFACoDOLCyNTF7wwsO0I9e_MZ9ofH91ZICkraIrhU45cA9dDtXKDIX-6Sv2fEy29ym7cNo1s_Aw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این ریپو رو یکی از بچه‌ها واسم فرستاد که دوستش نوشتتش و جالب و کاربردیه، برای گرفتن کانفیگ رایگان
فرقش با بقیه ریپوهای «کانفیگ رایگان» اینه که فقط کانفیگ جمع نمی‌کنه. کانفیگ‌ها وارد یه
pipeline چندمرحله‌ای
می‌شن:
1- اول duplicateها حذف می‌شن و ساختار و endpoint هر کانفیگ چک می‌شه
🧹
2- بعد اتصال TCP سرورها تست می‌شه (سرورهای بی‌راه حذف می‌شن)
🔴
3- در نهایت هر کانفیگ با یه درخواست HTTP واقعی از طریق خود proxy توی
۳ دور مستقل
تست می‌شه
✅
یعنی چیزی که توی خروجی
verified
می‌بینید، ۳ بار واقعا کار کرده. نه فقط روی کاغذ.
🛡
اعداد و ارقامِ آخرین اجرا ( که خودم از روی index.json چک کردم):
- تغذیه از
۲۱ منبع
(۱۶ تاشون الان live هستن)
-
۱۰٬۵۵۲ کانفیگ یکتای
جمع‌آوری شده
-
۲٬۳۶۲ تا
هر ۳ دور تست رو رد کردن و وارد لیست verified شدن
- خروجی‌های
verified
،
fast
،
secure
و
top100
(۱۰۰ تا از سریع‌ترین‌ها)
- خروجی برای
V2Ray/Xray، Clash و sing-box
— اپ‌هایی مثل v2rayNG، Hiddify، NekoBox، Clash Meta پشتیبانی می‌شن
- کل سیستم هر
۱۵ دقیقه
خودکار آپدیت می‌شه
- فیلتر
secure
شامل forward secrecy هم هست و لینک‌های بدون اعتبارسنجی گواهی رو رد می‌کنه
🔐
لینک پروژه:
https://github.com/0xRadikal/Free-v2ray-Configs
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 39.2K · <a href="https://t.me/MatinSenPaii/4976" target="_blank">📅 23:06 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4975">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/njrDNeoATVLhfB4rIO2cWtL07eLMfK3IOER0RcoJ3oDFz-Z0pgmtDI1LZfTykPbNI67BGYwgblLDymMWOcHiHR6i-9zaZLMTsxQvd-r07RBGYCefv7ib1qPxXehzZ-z69SgvD73sjZJz2k8xoOw4SAvjbYae-d-tegSo-DpgGzB7BPR5KavVEjyvTUhqbsAGYyjMq27YmY20HvkCO9u1siG8kdKbdmVMR0KMnWU4JlbUiLxMrDpvESGIQlzlkK8s20Npn-yQcNt5_KQsVmp3n35HxNlv60heZ8e8maAif0ghEcAutD_FWutAeJP_BVLUC40D4nEi_HiMWgbfH0wP3Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نکته‌ای که من فراموش کرده بودم توی ویدئو بگم، این بودش که برای حل مشکل آپلود حتما باید Fingerprint رو روی Unsafe بذارید
عذرخواهی می‌کنم از همه بابت بی‌دقتیم
❤️</div>
<div class="tg-footer">👁️ 36.2K · <a href="https://t.me/MatinSenPaii/4975" target="_blank">📅 17:28 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4974">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/PXS_RTN7V0ypSp18a41G5oIenn8pNRB12IlnAieZPSRIyXw5iUnIXjqgDN6JXS6ALWjOdQCeOBGLXP6fObzpdHlldqTCxatZlFcdW4lETccbAw-1TqfC0ivkkHT9K5dYIZD_TVfPHUpLjCPdg36rTqtkQez2SVD-AIOzPLQjJ5IDVEMwQE6i9ddbWpDjjGBER1wkhzYXZz53_oVQMLOU5vJyMyGxUBn2W-ifGiMmS23nVGGS7ltlBn_Fiae8PQTl_TSPi1GJLbWkH2cc48UrSKwcnhy48pToOhdVjmtjiLXG1xsyq_D1t3i-WC8Rfhuf9qLiJhf_xE5G_RxB9VzfVw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خب به سلامتی تا ما ویدئو رو ساختیم رفع فیلتر شد Worker اما هنوزم ویدئو رو می‌تونید ببینید سر سرعت آپلود خدایی که این متد پترنیها میده
🥰
که وقتی ویس می‌دید دو ساعت صبر نکنید آپلود شه
و متاسفانه ممکنه بعدا دوباره بزنن ورکر رو فیلتر کنن</div>
<div class="tg-footer">👁️ 36.5K · <a href="https://t.me/MatinSenPaii/4974" target="_blank">📅 11:39 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4973">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">فایل و نکات مربوط به ویندوز:
https://t.me/patt_channel_x/101
مطالب اندروید:
https://t.me/patt_channel_x/91
اسکنر من:
https://github.com/MatinSenPai/SenPaiScanner
آخرین نسخه V2rayN دسکتاپ:
https://github.com/2dust/v2rayN/releases/tag/7.24.4
اپ PattNG ویژه اندروید:
https://github.com/patterniha/PattNG/releases</div>
<div class="tg-footer">👁️ 38.5K · <a href="https://t.me/MatinSenPaii/4973" target="_blank">📅 03:00 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4972">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ZiEuA1DVXzWTZS52H9eMN5gg2O3WM7CgUiHSM_SgBPUtTmuhM--YFo6GCXeLNEjHNCWTa6B0riR31IsH3Bfm9CmL76UuUW_5p9ryvVGd-kqHDMLMY5sozydUJ9ty74IUE1pqDg7-taFifM4ejOp8L8rDXGQZ79YA4j0ekDNiZ6dMgLB1R1i0MUNgfhzMEWTYgXElBdPAADHx5jHVflPiguoceNDhov4Ioxocp4cnhnbaHCQqO-NHRU8bMLdQkDMYDPFK_OXAjmGR2P_ZuAq_nkk2J0ohOoPXWB634p8wTKK4jwQTymzOZDT3k3qqzGm2taFoVpdUFMPbhdHYbJ1W2w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">☠️
رفع فیلتر کانفیگ های کلودفلر + حل سرعت آپلود
⚡️
لینک‌های مورد نیاز:
https://t.me/MatinSenPaii/4973
⭐️
توی این ویدئو بهتون اینها رو یاد میدم:
1- آموزش دور زدن فیلترینگ
Workers‌.dev
با متد پترنیها
2- از بین بردن کامل مشکل سرعت آپلود روی کانفیگ‌های کلودفلر
3- استفاده درست از اسکنر من توی این شرایط
📹
تماشا در یوتوب</div>
<div class="tg-footer">👁️ 39.3K · <a href="https://t.me/MatinSenPaii/4972" target="_blank">📅 03:00 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4971">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">ویدئوی رفع مشکل آپلود کانفیگ‌های کلودفلر و دور زدن فیلترینگ
Workers.dev
در حال ادیت توسط ادیتور عزیزه و به محض اینکه تموم بشه، آپلود می‌کنم واستون</div>
<div class="tg-footer">👁️ 36.8K · <a href="https://t.me/MatinSenPaii/4971" target="_blank">📅 23:34 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4970">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ZWmREQniVi1WIdN0AGBuUWI6RgNiew1-stnaKD7usnwP43FtNvLt7NHnejWNnS-tqz7NGmZwwfHnGMSnCwsrP5ETH5h2FOVuxxOOWhna0HjZRgtQvxzaFGX5-i62bACK-DBLfJa5LoVYgpDCsBxAuPCfA17B420DSQiqHVioo7Yxsch6ixmip9pgavV8gK-MmLJkWWw7xr1NUUmHT1w_9dWpynwuirJ4WC-5f6PEfDhCrapQEJEXdn_fnaKWGVTaNk_6KtarBIoKj5mGrefSLcraNKP_05yH0ygkFQd1F0ywqdcgH8_b00oH_ffs5-9DyZemlT9EnDSfFA-uX7ncVQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چیزهای باحالی قراره داشته باشیم به زودی
🔫
از
🟩
می‌تونید فالو کنید اگه دوست داشتید:
https://kick.com/matinsenpai</div>
<div class="tg-footer">👁️ 38.8K · <a href="https://t.me/MatinSenPaii/4970" target="_blank">📅 19:57 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4969">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">با این آموزش، نه تنها محدودیت سرعت آپلودی دیگه وجود نداره، پلکه پایداری خیلی خیلی بیشتره روی همراه اول هم هستم</div>
<div class="tg-footer">👁️ 39.9K · <a href="https://t.me/MatinSenPaii/4969" target="_blank">📅 15:25 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4968">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Yb_eWlnxiqX-tuLCGW1sjFSias3ShWssXjca5EwT7fpq5pyPtiYnPZcqpogfqiJ0USIi6ROEryb7JQFwcm0jlKmqad4GeqcIZ8MVq7y-RLQPnDsyPSVMR0gu5WQz5dhsvvDvE7F-8rf_uUApjnHSv1NIB40O-25I9IFLQHBQa-hs7zUG4z2jO11sxd5CyAqC8gfmMNSL9EqoEslSN_zRMhF4Gapp2s3go37xemjE7JUz8o-XoxeCiAZ8OXaftxSrSXkLtc_dfmq-wg9h_SxEFT9iTr0NRGCdPNq9oO4TPb6uAtVFZVLksmVN7gJP22CLCOEYxMnp63v-EwteQ6e2wg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آموزش fragment+fingerprint برای رفع فیلتر دامنه و رفع محدودیت آپلود بر روی کلودفلر (ورکر/cdn) حتی روی نت‌های محدود:  Android: https://t.me/patt_channel_x/91?single  Windows: https://t.me/patt_channel_x/101?single  Android/Windows/Mac/iOS/Linux: Use Xray-core…</div>
<div class="tg-footer">👁️ 39.7K · <a href="https://t.me/MatinSenPaii/4968" target="_blank">📅 15:10 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4967">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/jRadyaw8finOpLjkzHnJooeXNoeJr90ceG7aGxTsOVLZVZukS6Q-3JsraaxDk6d8TRehiwq-KJhm7neRDbVPTQ0GgdENNuFjOHRpcK6S386QokgIu6p3KHogDq-3jFygH0r1IUjOd2idk7Fv7VyOA3Gpl1oRfNCD3SBLETpHMPwx7dqwIafsYWBCw8HaIQGCxgfQctvGBnSZ3ITB0S5JfPedSaTo9mURg2wbOJ1-kXuUHkY97szhOLs1GZgeANibIdXrkWtwix29QHSRSy1ZJtxVvO2CeUHx1xLg2eYcWPD3xBTA1MaHzGK1-eB3b_G11VL9vHiyyVPVeuBMpTeOgQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🌐
کلاینت WhiteAesther
(دانلود همزمان برای اندروید و ویندوز / دسکتاپ)
اگر به دنبال یک اتصال فوق‌العاده پایدار، سریع و امن با پروتکل نوین MASQUE H2 هستید، نرم‌افزار WhiteAesther در دو نسخه دسکتاپ و موبایل در دسترس شماست.
✨
قابلیت‌ها و ویژگی‌های کلیدی:
🔹
مبتنی بر پروتکل پرسرعت و مدرن MASQUE H2
🔹
اتصال سریع با یک کلیک (Zero-Config)
🔹
پایداری بالا و پینگ عالی مناسب وب‌گردی، گیمینگ و استریم
🔹
سیستم محافظت از کل ترافیک دستگاه (IPv4 + IPv6)
🔹
قابلیت Reconnect خودکار و Killswitch داخلی
🔹
رابط کاربری بسیار روان، تاریک (Dark Mode) و مدرن
━━━━━━━━━━━━━━━━━━━━
📥
لینک‌های دانلود مستقیم آخرین نسخه از گیت‌هاب:
📱
دانلود نسخه اندروید (Android APK):
🔗
https://github.com/WhiteDNS/WhiteAestherMobile/releases/latest
💻
دانلود نسخه دسکتاپ (Windows / PC):
🔗
https://github.com/WhiteDNS/WhiteAesther/releases/latest
━━━━━━━━━━━━━━━━━━━━
💡
پیشنهاد: این پست را برای دسترسی سریع به هر دو نسخه ذخیره (Save) یا پین کنید.
🆔
@whitedns</div>
<div class="tg-footer">👁️ 31.7K · <a href="https://t.me/MatinSenPaii/4967" target="_blank">📅 07:45 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4966">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromPatt's Channel</strong></div>
<div class="tg-text">آموزش fragment+fingerprint برای رفع فیلتر دامنه و رفع محدودیت آپلود بر روی کلودفلر (ورکر/cdn) حتی روی نت‌های محدود:  Android: https://t.me/patt_channel_x/91?single  Windows: https://t.me/patt_channel_x/101?single  Android/Windows/Mac/iOS/Linux: Use Xray-core…</div>
<div class="tg-footer">👁️ 30K · <a href="https://t.me/MatinSenPaii/4966" target="_blank">📅 05:14 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4965">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromPatt's Channel</strong></div>
<div class="tg-text">آموزش fragment+fingerprint برای رفع فیلتر دامنه و رفع محدودیت آپلود بر روی کلودفلر (ورکر/cdn) حتی روی نت‌های محدود:
Android
:
https://t.me/patt_channel_x/91?single
Windows
:
https://t.me/patt_channel_x/101?single
Android/Windows/Mac/iOS/Linux
: Use Xray-core custom-json-config and change/add --> address, finalMask, fingerprint, cipherSuites</div>
<div class="tg-footer">👁️ 29.7K · <a href="https://t.me/MatinSenPaii/4965" target="_blank">📅 05:14 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4964">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">گویا روی سامانتل و رایتل و نت مخابرات و خیلی از اینترنت‌های خونگی هنوز فیلتر نشده Workers و بیشترین اختلال، طبق معمول روی همراه اول، ایرانسل و شاتل هست</div>
<div class="tg-footer">👁️ 38.5K · <a href="https://t.me/MatinSenPaii/4964" target="_blank">📅 00:11 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4963">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">گویا روی سامانتل و رایتل و نت مخابرات و خیلی از اینترنت‌های خونگی هنوز فیلتر نشده Workers و بیشترین اختلال، طبق معمول روی همراه اول، ایرانسل و شاتل هست</div>
<div class="tg-footer">👁️ 39.9K · <a href="https://t.me/MatinSenPaii/4963" target="_blank">📅 00:07 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4962">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">تمام #نکات واسه مشکل فیلتر شدن worker رو داخل این پست میگم:</div>
<div class="tg-footer">👁️ 40.1K · <a href="https://t.me/MatinSenPaii/4962" target="_blank">📅 22:29 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4961">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">حل مشکل اتصال به کانفیگ‌های BPB و تمام پنل‌های Worker کلودفلر:  1- آخرین نسخه‌ی Pre-Release نرم‌افزار V2rayNG رو نصب کنید(۲.۳.۴): https://github.com/2dust/v2rayNG/releases/tag/2.3.4 یا V2rayN نسخه‌ی 7.24.7 رو از گیتهاب بگیرید برای آیفون هم Sterisand آخرین…</div>
<div class="tg-footer">👁️ 40.9K · <a href="https://t.me/MatinSenPaii/4961" target="_blank">📅 22:08 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4960">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/lLXOOtuXbDokUdH3SdOHTJ0maLbMfX5xfwoAPA625y5RTBJjqnSiZOmDT9zg0MjlhWI9p1fO-m0s648KgW9Y6gOXKyTfmBFQL7iZMKlXjQlSAWzqRbVrxK76jba3pukWqaO5BsEq0IKA8uvlEXWNpodW_GuGncDbBXzv59UhbOwhR-sYO4v8U6SWdt40RhwZpmC2uNQEnF1ASJp6pQSh2tup8rdYymwiP9hVSfu1ymkzWI5ybeKygISNosyek6pr2o7tP7rLKsyDi-NO6ju4_W6imo8hWYLOZJB2PSHgLU3u1U2UrSyePTDzpl1QW6WQL__zFTMhNHnoeYFF3WoEVA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حل مشکل اتصال به کانفیگ‌های BPB و تمام پنل‌های Worker کلودفلر:
1- آخرین نسخه‌ی Pre-Release نرم‌افزار V2rayNG رو نصب کنید(۲.۳.۴):
https://github.com/2dust/v2rayNG/releases/tag/2.3.4
یا V2rayN نسخه‌ی 7.24.7 رو از گیتهاب بگیرید
برای آیفون هم Sterisand آخرین نسخه کار می‌کنه
2-
این پروژه
از دوست عزیزمون Hidden-Node با الهام گرفتن از نکته‌ای که Patterniha
اینجا
گفته بود، نوشته شده و اوپن سورسه و کانفیگتون هم جایی ذخیره نمیشه:
http://hidden-node.github.io/proxy-builder
3- وارد سایت بالا که شدید، روی بخش Fragment + Fingerprint کلیک کنید
4- کانفیگتون رو کپی، و اینجا Paste کنید
5- پایین، روی Enhance بزنید و بعدش کانفیگ جدید رو کپی و توی
v2rayNG  2.3.4
v2rayN   7.24.7
برای آیفون هم Sterisand نسخه آخر
پیست کنید و به راحتی کار می‌کنه
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 45.7K · <a href="https://t.me/MatinSenPaii/4960" target="_blank">📅 21:52 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4959">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/LSSTPX6DfJXf_LHithVrwQJ_1VnbWNPioq0EMK2fSzkL-1VUC9OMM0WhsqHqaUCGjZNRXwB87IObmLEA6KAa_frtH51QdF1CeupJ_HVpyaJcQ5ZuLldU43yd6URFHiIHPJ_gC2LG4HpgO9f26vyAVxUUqGfuqvLhzfiMYFLMAE23DY6FxZNIvmwOoegI3YJuLepZvnvuY2Q9-VReAtNd__hSf7yhNA-dbxZukxmuvYOjJfcmhve7_TDkkrSSZr7N5hyCLTEvs9lPzKOHqfhimg-KiaoeWb40A9GuotnoekinCxcbVJNBOVC6Kvwc9LyCpue0rGpBbSWPY4EEERJDMw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دست پترن عیان شد
پنل ما جوان شد
مشکل رو حل کردم با کمک Hidden-Node عزیز. الان آموزششو می‌ذارم</div>
<div class="tg-footer">👁️ 32K · <a href="https://t.me/MatinSenPaii/4959" target="_blank">📅 21:39 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4958">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NWgDPBwDshOgX82ZYSRHVT18EVC1HaLS6DYiXz8MEW31GzdI-dxfucABGiS14eavk290bj-db_jvM83YzZUfieqljVA4SPGEcg-LH4EQOvJg5FxAe9h2l5ygivMx9vujzrHkENExZCw64OjxD5cJnTiWSqemb3UXFZ3_1NRbvqm7_mJ54ApOlP4ASw_HPLoj14ZYsgpHqku44BxlurnVg83LzihNDk8qZIPT-AWh7yQ19HJCv6EZ113DIjMc2dO2Twk-tnUIlHVa5x7BHiJayqMYTxTUiW_n3enzo1rJG_PzbkxtMQZxxo20O6uSa4KWYToPKR7EXBgXQg0MtoHjKA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💬
چطوری فیلتر شدن BPB و Workers رو دور بزنید؟
میتونید با رفتن به منو تنطیمات، فعال کردن گزینه Amnezia Noise فیلترینگ ورکر رو دور بزنید و به کانفیگ های ساب BPB Warp Pro وصل بشید.
این مشابه گزینه فرگمنت هست برای Warp pro و Wireguard داخل اپ WhiteVPN</div>
<div class="tg-footer">👁️ 29.6K · <a href="https://t.me/MatinSenPaii/4958" target="_blank">📅 20:47 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4957">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1dc224c1a1.mp4?token=Es3LQgOwtD0lNEK7GJC22oNekfj-QO8F-FEKix8uQ5Gy7GbIMWT2lJ9MS0J3VjaxtaNbuL2SaWhtvVzOOUG_yFlpdiiLOPTDvclwqr6RmP_UHjiws5iCigBqKuPGZiKU-w4z4bNMsKmJwYogMJg8xvlFNQLFoB2hx2v3uv5ZID9u2WELwGq96HdzHVquYYXZuTXG8ZCAypKfOfLS8Do71rJPfnicwTH3xsxpKkJ0ig_XPs7fmQKriRUmxW5bAnar-Ggv4QwT3JCX3-c5BifefZrnXfVXrkdswry4Fz1J3eq5cA5fplK_DWIWUL0_8_cnhWw1zuAaWw0tbBXhRKN5ow" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1dc224c1a1.mp4?token=Es3LQgOwtD0lNEK7GJC22oNekfj-QO8F-FEKix8uQ5Gy7GbIMWT2lJ9MS0J3VjaxtaNbuL2SaWhtvVzOOUG_yFlpdiiLOPTDvclwqr6RmP_UHjiws5iCigBqKuPGZiKU-w4z4bNMsKmJwYogMJg8xvlFNQLFoB2hx2v3uv5ZID9u2WELwGq96HdzHVquYYXZuTXG8ZCAypKfOfLS8Do71rJPfnicwTH3xsxpKkJ0ig_XPs7fmQKriRUmxW5bAnar-Ggv4QwT3JCX3-c5BifefZrnXfVXrkdswry4Fz1J3eq5cA5fplK_DWIWUL0_8_cnhWw1zuAaWw0tbBXhRKN5ow" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">💬
دوستانی که فقط با فشار دادن دکمه کانکت براتون وصل نمیشه یا سرعت کمی دارید، از این روش میتونید تست سرعت بگیرید و بهترین کانفیگ بسته به اینترنت خودتون وصل بشید.
توجه کنید، هر تست سرعت ۱مگابایت از حجم شما استفاده خواهد کرد.</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/MatinSenPaii/4957" target="_blank">📅 20:35 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4952">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">WhiteVPN-V1.4.0-arm64-v8a.apk</div>
  <div class="tg-doc-extra">35.7 MB</div>
</div>
<a href="https://t.me/MatinSenPaii/4952" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/MatinSenPaii/4952" target="_blank">📅 20:35 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4951">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SxKJSb0hjYFUVAROcmFOGf6GGhxTbtsaVvzFeydwyFuFCGEq4EK87W9KgPN1UVlj3GrbRNOcLd2sIDH1tvvlIAZM83iXU41t_plECo_ZxXgeHJi2hvti_dEcBhF8WDmn2HWOwTa3xPTDh36gbcumm_Fu3n0KefU93QCpfwndFUIMk1XmjjOjST2y4zazBO1kQRi0lRrGWdT42JpDwlbLTxR8dwpVCpqwxFoxqJijeLa85AKeEokKfz9Du8wa95PBS4IrpMpG661l-mb54StRXomA7lP80POBbSJggS_KHnjGoIERlY9HEUmyquUwoEcufV_VGl9i9vwPEjJllhj8GA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🌎
انتشار نسخه WhiteVPN 1.4.0
• ظاهر جدید و مدرن اپ
• بهبود اتصال بعد از قطع شدن
• حل مشکل VPN Mode & Proxy Mode
• بهبود تست اتصال. حالا میتونید کشور رو فیلتر کنید و بعد تست کنید. تست هم به دو مرحه real delay و تست سرعت  تقسیم شده.
🌎
دانلود آخرین نسخه از گیتهاب
https://github.com/WhiteDNS/WhiteVPN/releases/latest</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/MatinSenPaii/4951" target="_blank">📅 20:35 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4950">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">اپ Defyx وصله
متد Aether هم وصله
کانفیگای رایگان MahsaNG هم وصله
کانفیگای مستقیم هم وصلن
پیشنهاد می‌کنم پول به فیلترشکن ندید. defyx و mahsa رو هم از گوگل پلی می‌تونید بگیرید</div>
<div class="tg-footer">👁️ 31.4K · <a href="https://t.me/MatinSenPaii/4950" target="_blank">📅 18:13 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4949">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/G2AVmNi2MHCjm80mR7kRXWq6t9a9N4SWrCcIZzI8oVJHkY51aPOwP41P3tHVNOYhk8jLWCo1CTOAGYONKqP_zPUWFHciPg7oBHEIcvQxA-OOXp1Ps_eVrPWpiZhvU76OzVb17NqZNYztMR61EdXCaI9YoUAkr1BK6I855P4lOg3zfgE932j99O-285ogDJ4HqhfgTCFzLzbid0oXd2ksLaw_HUVV1o4AZvayP2FW5qMZe8xrslbd-x1RFaIrtDJnjSizq6GL4OgMiDzUVcxF8c_Xfr2w_Yelm_FDYANQdjb6j9sIgsxQzaHDIs2sjbi0HQsyxmnlI-IHc6lyGLESLg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">https://www.youtube.com/watch?v=EZ4q5V6fZh4</div>
<div class="tg-footer">👁️ 32.4K · <a href="https://t.me/MatinSenPaii/4949" target="_blank">📅 17:55 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4948">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">پروتکل MASQUE از Aether-GUI متصله. از اینجا می‌تونید آموزش اندروید و دسکتاپش رو ببینید:
https://youtu.be/2h6qlA1pJFw</div>
<div class="tg-footer">👁️ 29.9K · <a href="https://t.me/MatinSenPaii/4948" target="_blank">📅 17:52 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4947">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">https://www.youtube.com/watch?v=EZ4q5V6fZh4</div>
<div class="tg-footer">👁️ 29.3K · <a href="https://t.me/MatinSenPaii/4947" target="_blank">📅 17:30 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4946">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">https://www.youtube.com/watch?v=EZ4q5V6fZh4</div>
<div class="tg-footer">👁️ 30.9K · <a href="https://t.me/MatinSenPaii/4946" target="_blank">📅 17:30 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4945">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">من خودم به لپ تاپم دسترسی ندارم الان. اما Sni Spoof باید جوابگو باشه قاعدتا. اما اون متد تغییر دامین رو هم الان چک کردم و بستن</div>
<div class="tg-footer">👁️ 28.8K · <a href="https://t.me/MatinSenPaii/4945" target="_blank">📅 17:29 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4943">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/lj0yJH6011TY0Avnmknr1frxIRAwYMnAJZljGTURCT3FPIEGrXAI0UUQjdGPjd0SD_F8mpETKEPG-1Fh4kuvTA-bZg92y9GUAfpSdKpNWPuuS9ElAbOOlKXzP3dMd22Z4UaO7MBes8LMmICytrZyW9ue9KsJTRBSzaNpf_jfV5R0S9mnMcEs6cx4osahGXhaHl889Taazh8Uy04kMU4bbEeYihCLNIJfmlAMDN-_2wPUlR0Yo9BbJ1jgC3HTis6arFIKh0TSSLoeVoVIawbVKI0Gf3Q_LzBfdui7dH645LgPzHcF526Dy9AnGdeyddLLn3gfdmM-4mLekb5DZujdaA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/ripJ3PyvMux1CA-5-4_Ktm9bMNrFP40VSPzhB0vRIiOxwTgCiV8M4SfHSJldMEyM21GMdovHF8w6BuJa-uwqR4mi5M-NZR83vfdoM_4-_dkzHrzYo5f41SOUGurw7lzToOJ8-PRy9NbfbXAGU1D_ZKInjcpotRhRX9mxDcFRAB0Xlk2qUjceaocV2CR0ZgQIXJeBaLFoPsMlsZt8_tVZ3ADDau7z0-HDE3PDFnuCQb805SuiuFTDf9mGjaQaEAt-hPPZzaprwQ3zxFw13HYQ6-yvNNcO5Qv3BCw6GgM834vxbXS-YvaREdP7g15vb19SfnWIcPehBn2a3n_YvTRNZg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">از صبح داشتم پیاماشو میگرفتم. الان برای خودم و دوستام هم قطع شد فکر کنم که ساب‌دامین‌های *.Workers.dev فیلتر شده باز. بررسی می‌کنم</div>
<div class="tg-footer">👁️ 32K · <a href="https://t.me/MatinSenPaii/4943" target="_blank">📅 17:21 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4942">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">از صبح داشتم پیاماشو میگرفتم. الان برای خودم و دوستام هم قطع شد
فکر کنم که ساب‌دامین‌های *.
Workers.dev
فیلتر شده باز. بررسی می‌کنم</div>
<div class="tg-footer">👁️ 34.5K · <a href="https://t.me/MatinSenPaii/4942" target="_blank">📅 17:16 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4941">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-poll">
<h4>📊 کانفیگای کلودفلر شما هم قطع شده؟ (چه Worker چه Pages و هر پنلی)</h4>
<ul>
<li>✓ آره❌</li>
<li>✓ نه. وصله✅</li>
<li>✓ نداشتم. دیدن نتایج</li>
</ul>
</div>
<div class="tg-footer">👁️ 34.5K · <a href="https://t.me/MatinSenPaii/4941" target="_blank">📅 17:14 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4939">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">برای نجات یوتوب فارسی و درصد تشخیص ویورها، برنامه‌هایی داریم. و طبق تست‌های کاملی که دیشب گرفتم، خبرای خوبی دارم واستون و توی یکی دو روز آینده می‌بینید دوستای خوبم</div>
<div class="tg-footer">👁️ 36.7K · <a href="https://t.me/MatinSenPaii/4939" target="_blank">📅 11:59 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4938">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Ixl57-4yLQeUzBlu7-XQPk3-DRY0oovhDJtMj9_Px2JGUBGHC-2hhBPzxCwfjnG5vaKJK2zqLfBRDrM-2HIEJy9e5ehr7CXIc5YM1ZUphva7tYMH5l58KtBizUl-eIiHrzjddLn7DokxMboIDdYoA455UqBkWALwfGWxGf4ofLJQUeiMdcVcOe7zWUC0a0g5yZcA2-W7lOMT5yt8ujt_p38iDoD27c8XEq0tXxYBDVqiU_OxrzVfTnZmFrXb2ZSMB6T1Wz196fYeojaWfegk0s0Rg6HwPU-69EYiyTCOH32mzmupRWxYeG36LV5BmNoPlEj7mJG_8IdzcJFnF0A8qw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">روش پرداخت بین‌المللی و گرفتن Visa Card مجازی  خب دوستان، امروز می‌خوام بهتون یاد بدم چطوری می‌تونید با این وبسایت، برای خودتون ویزا کارت بگیرید: https://app.mpay.cards?startapp=ref_PzwXZ8 (لینک رفرال هست. می‌تونید آخرش رو پاک کنید اگر دوست نداشتید) 1- بعد…</div>
<div class="tg-footer">👁️ 39.8K · <a href="https://t.me/MatinSenPaii/4938" target="_blank">📅 23:37 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4937">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/OWh2qb_2Arl4wlPEJQFXor0Op3khmsszI746IrIs5HNUrPea-ZnGOe7Y6Sh_jxrR_lx3LEYX2BYS0_xUV0U-f28DqdOwFJW45Vm6NoU2TrzHEBujZksTawEZTd_h6XKcwFjx3JH4GG0jf2F4YDwLrVRorU4KNDgD5HXahARrIGYIZpW6jdqJB85-oz0xfXzz7bXOf12YOZ5XK6d14ms5IqtR1CRqlvlbgbX0oEhPrLUt_GNtMVaRSXaBvLb3CSL5Iw9JdSqzzTdSJSqrKXkFC-geYfG4VqoHQgy-BblKm6v8BXqGUssxe64g7AI3GtfdCU5LYff7VEAeJzD4mia5eQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پرامپت ویدئو آخریم رو که با KIMI3 رفته بودم، الان دادم بهش و واقعا نزدیک بهش در آورد
🔥
به نظر باید منتظر یه مدل خفن باشیم. فعلا توی Preview هست مدل  تازه Kimi نتونست One Shot کنه، و این One Shot کرد اونم فعلا رایگان! کیمی نزدیک 3-4 میلیون پولمو خورد
😂</div>
<div class="tg-footer">👁️ 37.9K · <a href="https://t.me/MatinSenPaii/4937" target="_blank">📅 22:38 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4936">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">به همین راحتی.
تموم شد و رفت</div>
<div class="tg-footer">👁️ 37.5K · <a href="https://t.me/MatinSenPaii/4936" target="_blank">📅 21:15 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4935">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/AKGzKrIp69lPWAdn52YD7MZw0m-3KVX_suMf9q8v32dDAK2Q_UZnYfYB-jSp30kf9Zkknm4ZhnsCiRNZaP6JTNsfD0JUWJjiF_QAscwcN3-utCsjuMVgtMWxQ76JkVXE_ZbfctHQuoFkfO_f-0b7PDfD7vdGiWM6zhkGgAl9ZjlZjrd0xtp4bUOXr_upX0OGJfSTxXmiex5vsyKl5WcUMM2lvwqwP6_inh6sfPFO_aRJnjEDHNj4dMtIHUWaO8LfpomObYaSNKpBIf9j1k6vGoVIUyfXIiDBhCcXW8JBkbiqq-HRmjkvEDaG_OZVClL2t9IvS55qa7VqEez-H5SCHA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شرایط عادی :
•
دانلود آخرین ورژن WhiteVPN اندروید
•   دانلود آخرین ورژن WhiteVPN دستکتاپ
شرایط قطعی اینترنت :
•
دانلود آخرین ورژن WhiteDNS اندروید
•
دانلود آخرین ورژن WhiteDNS اندروید
•
دانلود آخرین نسخه CoreForge برای آیفون
@whitedns</div>
<div class="tg-footer">👁️ 32.6K · <a href="https://t.me/MatinSenPaii/4935" target="_blank">📅 21:14 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4934">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/dDWEKf1Y0XxyQfPePVO6NWgJU9umQOnzYjyf38b6630-ZAtS6Q5KAm7_kUNqOGzBG9Uqwl7NvG_xsSXsuW5nzz40jU3ieJKm_rchw0SBu7eOgrLVoR10H4sI5dv_qSPWP5UUHAs09WZPk6EcAgWGhktV5yQNgqWLTq1LfQfMG_I_mTj5cqKGurxLvNISgNQPK_9cSoQ08K_EOEf_o2zyxpcduCAXOUihGi0pEv7pwOj1V3LClYGJqsqK7AT2QRKxgZSe22UX4OOb2EXbbZxnvwmdDW6t4MdbgTQTPEhc2D_5g0kJ28hJplvWgZTC2_jnxB05J0sXxXBWarZVS7qrhQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دیپ سیک هارنس رو دارم تست می‌کنم، خیلی باحاله محیط UI اش سبکه، و کاربرا هم توی ردیت خیلی گفتن که Caching اش عالیه. یه بنده خدایی قسم میخورد 4 ساعت باهاش کار کردم با deepseek pro فقط 60 سنت مصرف شده بود. باحالترین قابلیتش اینه که میشه Mode شخصی ساخت. و از معایبش…</div>
<div class="tg-footer">👁️ 32.6K · <a href="https://t.me/MatinSenPaii/4934" target="_blank">📅 21:03 · 23 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>

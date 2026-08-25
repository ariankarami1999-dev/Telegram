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
<img src="https://cdn1.telesco.pe/file/m_Fmd1lFtIXu9eL5Rn4soEJ_KNrM7tt4T73524heNpsh47jhLDKNkgjvur0xDtwsaw98IpZhr1b7qFYwVuN-Aq8mAaiR6wMm5Yo4WZBUxiDWUOegpuwX51GlxLB0iPh9ikT0lMw0KGL9em0-kaoEkUDk25Gyju7kAZsxP5fWxuBNXcx-f8aq4j_dt5NQpb_nxx9jHXVh92upHaw8A5v1naf_gZpod-b10CKo91_CJ6FTZWP2oqg8yk0hMY2IpBmN35-NSyPIT6MnzJazwo6ic3MGsUcgHSuIr6Rljocw_-OKcC3Qe6PNxk-2uj9yTUs2ZiqJSuDSWrJZIwkibz5ScA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Matin SenPai</h1>
<p>@MatinSenPaii • 👥 156K عضو</p>
<a href="https://t.me/MatinSenPaii" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 متین هستم و کامپیوتر رو دوست دارم! در حال یادگیری هستم و چیزهایی که یاد میگیرم رو سعی میکنم به شما هم یاد بدم اگر به دردتون بخوره=)•YouTube:http://www.youtube.com/@Matin_SenPai•Github:https://github.com/MatinSenPai</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-03 12:01:20</div>
<hr>

<div class="tg-post" id="msg-5047">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">و خب من نظرم اینه که، Train بشه که بشه:)) مدل‌های قوی‌تر، ارزونتری که الان هستن و داریم ازشون استفاده می‌کنیم، بخشیش از همین طریق قدرتمندتر شدن
ولی خب شما باز اگر نگران «حریم خصوصی» هستید، دور چین و مدل رایگان و contributer رو خط بکشید</div>
<div class="tg-footer">👁️ 5.5K · <a href="https://t.me/MatinSenPaii/5047" target="_blank">📅 11:25 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5046">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">به خاطر جالب بودن این پیشرفتش فرستادم. وگرنه به نظرم این نگرانی تا حدودی بی‌مورده.
زمانی که از مدل چینی/رایگان استفاده می‌کنیم، عملا داریم امضا میکنیم که از دیتامون استفاده بشه واسه‌ی Train کردن مدل.</div>
<div class="tg-footer">👁️ 5.96K · <a href="https://t.me/MatinSenPaii/5046" target="_blank">📅 11:23 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5045">
<div class="tg-post-header">📌 پیام #98</div>
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
<div class="tg-footer">👁️ 6.18K · <a href="https://t.me/MatinSenPaii/5045" target="_blank">📅 11:21 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5044">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">راجب یه پادکست جالب شنیدم در مورد یه تیم نرم‌افزار نروژی که 4 ماه کامل از کلاد استفاده کردن و بعدش کلا بیخیال شدن برگشتن روی روش سنتی خودشون
فردا خلاصه‌اش رو واستون می‌ذارم</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/MatinSenPaii/5044" target="_blank">📅 00:22 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5043">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">نمیدونم واقعا چی بگم راجب اقتصاد
برق
...
می‌خواستم امشب استریم بذارم و بریم سراغ اخبار ai، برق رفت کلا تمرکز و انگیزه‌ام پودر شد.
کلا همیشه ترجیح میدم کمتر صحبت کنم راجب بدبختیامون چون همه جا میشنوید. و بیشتر تمرکز رو بذارم روی کار که کمی از این فضای حال به هم زن اقتصادی کشور دور بشیم...</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/MatinSenPaii/5043" target="_blank">📅 22:12 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5042">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">ما الان داریم دقیقا مسیر ونزوئلا رو میریم.</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/MatinSenPaii/5042" target="_blank">📅 20:40 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5041">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">راستی بچه‌ها پلن 5 دلاری OpenCode Go رو من با همین روش گرفتم. اگر که خواستید بگیرید میتونید به GLM 5.3 و اینها دسترسی داشته باشید به ارزش 60 دلار مجموعا: https://t.me/MatinSenPaii/4915</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/MatinSenPaii/5041" target="_blank">📅 19:05 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5040">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">روش پرداخت بین‌المللی و گرفتن Visa Card مجازی  خب دوستان، امروز می‌خوام بهتون یاد بدم چطوری می‌تونید با این وبسایت، برای خودتون ویزا کارت بگیرید: https://app.mpay.cards?startapp=ref_PzwXZ8 (لینک رفرال هست. می‌تونید آخرش رو پاک کنید اگر دوست نداشتید) 1- بعد…</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/MatinSenPaii/5040" target="_blank">📅 18:31 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5039">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/MatinSenPaii/5039" target="_blank">📅 18:19 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5038">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">☠️
آموزش OpenCode، رقیب رایگان Claude Code
☀️
⭐️
توی این ویدئو: 1- با همدیگه OpenCode رو نصب می‌کنیم(کاملا رایگانه امکاناتش و اوپن سورسه) 2- طرز استفاده ازش رو یاد میگیریم و بهتون میگم کجاها خوبه ازش استفاده کنید 3- یه چیز مسخره با میمو می‌نویسیم(توی ویدئوی…</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/MatinSenPaii/5038" target="_blank">📅 18:19 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5037">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/MrxPYly1YsXFo_JsD11vepyn5_cA_fEBIQseZ9g8UjvfJxttRZy_E7vUi8tqpI5f6JQq_BNbyh62VhA3dNa_NG-sV9gA6aIPUrpvYjyQHnl6nexnXGf578MWIZ1jSO3Wbron_EW4BT-uhSMhXddio-7qSflI6V4rkq57V7EBgeFtn1XiAxBv2nMxWu2ecggn5GIhdxYBZpaWgehaUMNOfL_UUZM7LQsV8YdgYNYnZchwtW10Iq-Wy6rdEHNE4tW7NK-yc2pP4zWVaTCKoF3l9H7wxyEPiVoqtLrPYTc8JIiFMCAyBB_1xhUZGyKSfkSWz_v-WfgR12yVHYu5rnmUdw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">☠️
آموزش OpenCode، رقیب رایگان Claude Code
☀️
⭐️
توی این ویدئو: 1- با همدیگه OpenCode رو نصب می‌کنیم(کاملا رایگانه امکاناتش و اوپن سورسه) 2- طرز استفاده ازش رو یاد میگیریم و بهتون میگم کجاها خوبه ازش استفاده کنید 3- یه چیز مسخره با میمو می‌نویسیم(توی ویدئوی…</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/MatinSenPaii/5037" target="_blank">📅 18:03 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5036">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/nKmq4C61Rx7UM4gwIrsRWZXVgVF9Z7Xgm1AQv77XoH2a6-P7K0Jschl7OvMOpdMHKLLghmroGLdeJE2-muKPjRUVJxZf_vFDj_6JfFJPtOUsk2Y2VjrrywulunEkg2Em5wktVfgD3HQmNwEwOBu4bG8K08vTf4fzi-MowCcZTmP_pK7NYgBQSsFIFKE5MuA0QJ5LxJOvCSWhxMD89HqDae1352Pks5jMSl-jCBMugaYk-Y8-HJ3vDUsXxZBiEIXHbVtqAz7Hd6-yLXQx3XFmp6boCqZXBetlxY9PbgZS8MHSLuV40UN0-vlK4LNPWynhkMUiF9LDlJ8P9Rqtzc-0Uw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/MatinSenPaii/5036" target="_blank">📅 17:56 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5035">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">تموم نشو x alpha
💔</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/MatinSenPaii/5035" target="_blank">📅 17:25 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5034">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">تموم نشو x alpha
💔</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/MatinSenPaii/5034" target="_blank">📅 17:09 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5033">
<div class="tg-post-header">📌 پیام #86</div>
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
<div class="tg-footer">👁️ 28.1K · <a href="https://t.me/MatinSenPaii/5033" target="_blank">📅 02:56 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5032">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">خب انگار قسمت نبود
👍</div>
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/MatinSenPaii/5032" target="_blank">📅 01:36 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5031">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">یه ویدئو داریم واسه Open Code
داخلش یه پلنر ساده می‌نویسیم با Mimo
توی ویدئوی بعدی که پشت سرش میاد، میدم به X Alpha و اصلا یه چیز عجیب غریبی زد.
موندم که واقعا این مدل مال کیه</div>
<div class="tg-footer">👁️ 29.4K · <a href="https://t.me/MatinSenPaii/5031" target="_blank">📅 23:34 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5030">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-footer">👁️ 30.5K · <a href="https://t.me/MatinSenPaii/5030" target="_blank">📅 20:17 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5029">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">دلار 200 رو هم رد کرد
ولی نکته‌ی دردناک اینجاست که هرچی جنس می‌خریدیم تا الان با دلار بالای 200 بوده قیمتش
الان قراره حتی بدتر هم بشه</div>
<div class="tg-footer">👁️ 29.7K · <a href="https://t.me/MatinSenPaii/5029" target="_blank">📅 20:16 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5028">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Y5agF9jNtFm2DHjcfmqH09iSHvJ_KnZran5NQtir9uIURMaQsFqHx9rj60ckb1xitE1_btOruzb-zB_O0ezAY-pAh6MzpSDFxkZa60O041CQbr_cBzBHhTHGlOlLraEl9RS1A94jJVDMLL6y5jQg219PWypss31NgpJLi2ku7A7E9aZu7oM_amV9FIifcfCLcME4nECHjFR654Ne2AeuPgD0IAxC7CSBxAHYzrW3PFMWlwVTm0pauJIyyPrNGvqeKZcVfafecjWk7sqBp9w5lHJA9Au18AobnlCrzAvYiK2mkxU3PwcWqCGOFTeCEQHQNv9qdhJ8219cjBuW-E2J2g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رسیدم ۲۰۰۰
تا الان ۳۰۰ هزارتا امتیاز
دو برابر بشه میفتیم زیر ۱۰۰۰
❤️</div>
<div class="tg-footer">👁️ 29.5K · <a href="https://t.me/MatinSenPaii/5028" target="_blank">📅 19:13 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5026">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/gKTAVY0S5PQvpZ-5m__4DMiof68JnGw9ddOkWa4gcFrXYrzk4IYMG5AJj4wC9ABKt8BBuw8gcrpP3xKFUSzkXzcliqFN966krvjDdD1ZxLUfvdkCasGrFmnmDDkiDuYbkmdm-gIA5o3s_AMBBnb1iRKP_LoaLr-iUjCpyPw33hTXIgrN6U5MvkTaXEot0LuQqh-1Lgrnd_K4NFJvnZA6SxCpT4hfX50esHqpQI2RAS5Y9ESJAPX_q5NmGpchn5DL8XEMIogtxuy25Thba4RO3xeSXdye8q-lQoAVRLcV7eUZOr6FHdaUxrsIxfCsgRvkBYoXOWomU6ckQA0eV1ZOKA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/ELAHoaADggkgqYgsMZcIDp2CMLUSTWJG13gayoaq0Cq16gUe_2SRNqYCgUkArm_O_m3Frkcd_y9dPHp3nRbBemoU9IhBGCq_dKkGouW-tKqItZtky2YFK_gcNTPOyxC7wvU5AKvNVOYm4ct_ep0rv4YjyAylKIuupwzYFEGVzsrxQ8188qvNsOiI5SZ2Ne3fy-cNg5Oc5GyPPR0D8BNcj064AqdTkTZq16NkUGLn4Y8RtB_j8VcH3uI38gYYdTpOnc_9gLgwtHQ10B_hsyG4n01sSMKjOE0ZWewLVsbfHfqNPyHVN5q39nazBI1TsKRZiuGBaRWZHHKuPo_tZZQUTw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 28.7K · <a href="https://t.me/MatinSenPaii/5026" target="_blank">📅 17:17 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5025">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/N-GlwsYGCrZIsrRkaiPyWxtpGjAm4omJq7CToRzRRjiB5maBKks18-qs5sKeZaNpzOtlAciYL2M9bsWH5BBGDUpFCfmwEbRszgOSManTzxPLN7hGz--a8Altl4n3qPuipjc8ehYf3RA0GL9OhWNWmWeUnUkJGxTGgP_oC4Mhz-VvJcEhOc9gH0cipK3Y23vzqOhj3jUITnuGoOOELexEtYjoMPcYXHVHvc0pezFbWaWc8eG0BY6oYaw1F_NG2qmihHvN834mEOeThnsV_QPl69JuNSbi_7DKhkhYEkIxBEgBFgqhObAk-qumVqbqJ1cYxqrpSFMAxWOl-GpW9-eolw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">به خدا چند ساعت خوابیدما دلار کی شد ۱۹۷</div>
<div class="tg-footer">👁️ 28.1K · <a href="https://t.me/MatinSenPaii/5025" target="_blank">📅 16:33 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5024">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/1357719d90.webm?token=Js9Fnjf8G3DP0lHxGFkE-yl9CW8kGZaYhwOMMr1JwBncjkP6_fZJZsQPTvo6pBsROW5gsyyOHzBJGi8vRF5CNuD6UyrDycDkZjK9aj79bLzB6LzBujplNtGe4zgOYq406mrziwTWwpCIR2dRhwL492UmfyqMlsZdyQusiVMOLQ4VaDFkCkrINOPl3NKGT9gXtzoxjOCvdbuurdOuY5zpTfM76eOVT4mupF1KaPWX2J3f5OUoQN7MiFELWvj6PdHGc8isTgRE2RzA3yGdQ3am9SJ-tqWu8K9yIKFTV12dKFLgik4JaG4vACgEm5181IDC8qahKbsU54uCokCA6px1KQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/1357719d90.webm?token=Js9Fnjf8G3DP0lHxGFkE-yl9CW8kGZaYhwOMMr1JwBncjkP6_fZJZsQPTvo6pBsROW5gsyyOHzBJGi8vRF5CNuD6UyrDycDkZjK9aj79bLzB6LzBujplNtGe4zgOYq406mrziwTWwpCIR2dRhwL492UmfyqMlsZdyQusiVMOLQ4VaDFkCkrINOPl3NKGT9gXtzoxjOCvdbuurdOuY5zpTfM76eOVT4mupF1KaPWX2J3f5OUoQN7MiFELWvj6PdHGc8isTgRE2RzA3yGdQ3am9SJ-tqWu8K9yIKFTV12dKFLgik4JaG4vACgEm5181IDC8qahKbsU54uCokCA6px1KQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-footer">👁️ 28.4K · <a href="https://t.me/MatinSenPaii/5024" target="_blank">📅 16:26 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5023">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">به خدا چند ساعت خوابیدما
دلار کی شد ۱۹۷</div>
<div class="tg-footer">👁️ 28.5K · <a href="https://t.me/MatinSenPaii/5023" target="_blank">📅 16:25 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5022">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">حدودا 20 روز هست که دارم با ابزارهای مختلف و AIهای مختلف کار می‌کنم و خودم رو آپدیت می‌کنم و چیزهای جدید یاد می‌گیرم، و ویدئوی جدیدی ندادم در مورد AIها تا هم دانشم بیشتر بشه هم محتوا باکیفیت‌تر. اما طی روزهای آینده، کلی ویدئوی جدید راجب تجربیات این بیست روزم می‌سازم و می‌ذارم توی کانال.
(آرک سولو لولینگ مخفی به پایان رسید
✨
)</div>
<div class="tg-footer">👁️ 32K · <a href="https://t.me/MatinSenPaii/5022" target="_blank">📅 06:33 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5020">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/MqSp2r1uyoZ58wthATQySntvjvmFaFfHf-qH5vGeleIqzDxryuZhdgpgNwe4D4qQZ5O7t5f4Bew2rM-VCbrswtW9XT52NVxEFkLBBBhuOaul-26Dh6nPQELIpRUmLiZv60Fc4hgxeAX3tIBNC64UJK2wIJRkh1pc6w7M6ErIuiqY91OcOBIFEUkZFczZcSTUmoAaWV4_Wso-PLpdG62ziFj6nIxxlq_OIKSD71_SkR9Jzy5GvlGlYX8lAsoZRao_JLVUvaY4BKnyNjJfpmx3_mGROnwD9Bdm9P7SOc_-mdfhTqINcqAvbnpAJTKaThgJTeur2qnSg7glZ8aNz7pFqw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/j2M5cHMvxihgeZZgttzUvr6eMQnmQHIa0zm7gr7dFNC_8QQFUqe3daItm448HAshn5ATUlpd_JlR7dJZmkYhpuBThuYlVinpn36_piPru204a5DNjXAtP_5nC_clRNP8bgP3XsVQnob3h_faUYqrAMiMFwaTislSeULhttpdca8XF0XQkYOHQQDuDOxvln_nLL7YKU9Z0WQXQNG7p7EamlTyvU92BlJCioSLYOtZZ4eJgt6iBafFT4RsiuuzpvXbTJrs65UT2-_kLPW_-daLDNB8ORawfyjUg3PjKfsidTBD4FAnKt1sgcWEDarKcRas7ujcz_Vxuuv6JfS3PoQK6w.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">خیلی خوشحال شدم امشب از پیام‌های محبت‌آمیزتون و از اینکه آموزش‌ها چقدر کاربردی بوده واستون
❤️</div>
<div class="tg-footer">👁️ 31.7K · <a href="https://t.me/MatinSenPaii/5020" target="_blank">📅 05:25 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5019">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/OdhKqSy5JGn20SopEH7jiEcN6fKOOoPknpPAmQrjBGmz0UC0VmJ9Am95nXDfCxgQroJ3pi8mNyNaM-UALus3Mf_kshUfcWmKQCwd6ruLwry5D0qvTKKUf05b-GQm-XhOYTXEmMwPdIYZFpUtLpNAd7A4xxNSE53gL9-oYvySwXidDAoT36254JqTwc_hVvwVfR5UEjIlJvwhsghemdqbQIcS7TfGF04I34dUb4AVpjGX2j2OIhmdI_xL-meQdKMzdHnXqMhggD_6Rl-ed3kXVy-zQQN1Dt9CydZEfC4STtp6LCG3fwHuhW9fMW4JeD5m2CVhaPFMI4s3tHVCwhusXA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">به نظرم یا مدل جدید شیائومی Mimo هست یا به قول یکی از بچه‌های توییتر مدل جدید خود Google(جمنای ۳.۵ پرو). گوگل هم ماشالا ید طولایی داره توی این ناشناس مدل ریلیز کردنه
😂
خواهیم دید چه خواهد شد اما تا الان خیلی خفن بوده</div>
<div class="tg-footer">👁️ 33.6K · <a href="https://t.me/MatinSenPaii/5019" target="_blank">📅 17:25 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5018">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">خیلی توی کامیونیتی خارجی بحث و جدل شده سر اینکه حدس بزنن این مدل جدیده مال کدوم شرکته، چینیه یا آمریکایی و OpenCode هم اعلام کرده که دسترسی بهش نامحدود هستش تا هفته‌ی آینده و روزی 100 تریلیون توکن تمام کاربرا می‌تونن استفاده کنن مجموعا و ظرفیتشو دارن
😂
همینطور…</div>
<div class="tg-footer">👁️ 31.6K · <a href="https://t.me/MatinSenPaii/5018" target="_blank">📅 16:41 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5017">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">خب من این آفر سه ماهه رایگان اسپاتیفای رو تونستم بگیرم با همین روشی که اینجا یاد دادم  مزیت بسیار بسیار بزرگی که داره اینه که میشه به گوگل پلی وصلش کرد و عملا توی هـــر بازی‌ای خرید کرد. البته من با VPN آمریکا chain شده رفتم که ساخت این رو هم یاد میدم بهتون…</div>
<div class="tg-footer">👁️ 33.8K · <a href="https://t.me/MatinSenPaii/5017" target="_blank">📅 08:23 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5015">
<div class="tg-post-header">📌 پیام #71</div>
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
<div class="tg-footer">👁️ 33.7K · <a href="https://t.me/MatinSenPaii/5015" target="_blank">📅 08:20 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5014">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/GX-HKetuS7SKO4CUql89HYPqXp-ywCpZCJRFlQ0iEfKrOwvO_1uLk-q2DM5eLO4YdxphT1DbXgOhqZ55gBkm1h1AO_LhhKD7V4-6a3_kX2lQmgLa9PF9DkpWbiQMQ6XmT3CxmPYrklIdhTLdEYvImRpQN8k8jCCBGZSO9qhojqDb0Py_uoxns47mHu_i_JdQWtQWwrgp-6gqFQlMAlZqxtUOP-FNlopXsZxAc5z1tQJMud0RGTB0k7NuVVydGO6nFK9iiFqGZL4J6VeAt_5IYiiZkwZxmv3PAMUrCIC-0RfSd15DbRh52-_aZdc5xnI0gVCyqpnmDQmkK1r2AM515Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مدل جدید و مرموز x alpha که روی اوپن کد اومده به تازگی رو می‌تونید این شکلی تست کنید روی 9router: https://x.com/MatinSenPai/status/2090856359117902053</div>
<div class="tg-footer">👁️ 30.6K · <a href="https://t.me/MatinSenPaii/5014" target="_blank">📅 08:04 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5013">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">فکر کنم وقتشه کم کم یه لیست از چیز میزای رایگان و آفر و... هایی که با این سایت تونستم بگیرم بذارم</div>
<div class="tg-footer">👁️ 28K · <a href="https://t.me/MatinSenPaii/5013" target="_blank">📅 07:46 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5012">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/SN5yHjlPtJ9li1cY0s7OuqeFEacR6KpW3LqZSqCU4fX6GApq1byUX4E41P0iugrgC--HWJdO2sZ-tEfMGG1erUsWnM-jAlrznvHIuGBTw_u3oCZGcMzFRyboowcd245KyNWQ1xLMj6ouS5xEOIuzY5Oq4G-tf6x6KF5Tf_dyDGQqJKkMK-RIZMuzXFD8ZcWzN6OmNDVJ2Meldc6vdh8PMIkuQnXw1iQ9jnteKNj9p43wifucrXOzs7G3UqfU9bqtSwIs7VKA5quoPSFOv83EAnWn3YLVx_gxTiPF8C7l7J2YHxcnYP5GtDvqBbUCIM6gARsfPVZEDmt8kY5T9B5vYQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یه سریا هم یه جوری شبیه دی‌کاپریو میگن «اوه این پروژه وایب‌کد شده» انگار مچ معلم مدرسه‌شون رو وقتی دستش توی دماغش بوده گرفتن.
همونقد معصومانه و مهدکودکی</div>
<div class="tg-footer">👁️ 29.2K · <a href="https://t.me/MatinSenPaii/5012" target="_blank">📅 07:39 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5011">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">مدل جدید و مرموز x alpha که روی اوپن کد اومده به تازگی رو می‌تونید این شکلی تست کنید روی 9router:
https://x.com/MatinSenPai/status/2090856359117902053</div>
<div class="tg-footer">👁️ 30.3K · <a href="https://t.me/MatinSenPaii/5011" target="_blank">📅 23:07 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5010">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/SR5CLOoHDhMoX_zdMBhozAp09DoOYwCsqNnoLNk4L2P66m972-ZNGv-YJzGtGDhVGwBu5ee3-MFn02xKV7WuBsRPstMN8N8ygrdV7igMfYsN9mqzTCZ0wKBwSYOFhbFfnEfbEi_qx_XEzcEDKiCc9xQ9Pgt1B7hTJKJvndwNtN_BRadLxcFs5A46PytA0-gO5hZpyqt2IDAm97yQcv_6ybXBti-u9SGN3xCC4Fb_IMvp1mdN_B_jBa87PrbRLZtgWRYiWzk5l4gwMlYzJI9HqLZ_AdI0QAU0hRiFsvEy2Z1PkcDMLaOtLw2Tk38ZTReTjdB-DLhfbVvxqUiR8kobfQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/MatinSenPaii/5010" target="_blank">📅 21:38 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5008">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/pY0P-YQnvaE7gni7O38GJAwq0VQdRxF6dcO0qPqi1OCVQB3fWRXZR7qVey_OX14kpbiXlOhsHz3RM563ShWiIjyyRfd3M57v4awmvlwmxP3lnY5dl0W1l0coMwULxK9r9Hmzy7jLl8Pg5rBStQ_ez9_WJGS9KVU6XZUw_-bjtSnl-MUIY4OvDkWsXL2R7ws7bzEUxR5n7_XywEmf9kGdgOjsUrmGQYxwC__p8p3y9baOP63u3Lu95kWo_8r9rAsIRsLpN4NxL-43OFj9PQWbXcJvrYrZd1k3_v_l3_mZvG04pQz2ouChh_RCb32CyyR2psJ0RyBZBKQsI-_F238cQQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/Pg46653ISeSMXhIqYfHhfkDwBVvkUUczXKfN_3Kidj7NiFMlD4hYjN9q78YFhU0Wlm43US5oGfc8jFODiHOlhI_8OK6EvFCJ5eDtD8ZNAaBaZ0F4ffAsJJxb4vxy5fqxhjmN7WsZrEy-5vpYeTNAMGpTAXWU475ABRPZxbSeJoOxYW1gmTfWmRvhpWFzDSxS-XnN_dyIJclHFNC0-QHan_H9Aa-DR_hyJXyAZYCdDR48MVOvpAualYRRBcxfvjmJ7XxqOZtozP32xFne5X6FhD6ZK5PdGnByPBtltMk9PD0J7wMcP-yHvXnG7ZhN2YPlnrbshsa2CQdLvNShKz4BLQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">اگه حوصله خوندن توضیحات رو ندارید، فقط ساب زیر را وارد PattNG کرده و لذت ببرید !  https://raw.githubusercontent.com/patterniha/Free-Configs/main/configs.txt  ساب هر ۲۴ ساعت آپدیت میشود. /// توضیحات:  چند تا از پروژه های عالی که کانفیگهای رایگان را جمع‌آوری…</div>
<div class="tg-footer">👁️ 28.1K · <a href="https://t.me/MatinSenPaii/5008" target="_blank">📅 15:11 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5007">
<div class="tg-post-header">📌 پیام #64</div>
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
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/MatinSenPaii/5007" target="_blank">📅 15:09 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5006">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/HWUXwoY4Oj3oqVr6ta9kcA-5dv9PVo37cL-esLVkemUKDtI3dxIEUTCdSAWG1o30SMPlizbjHJtQmbWL6IdYNmjQGqnEW1J1LQ6L3e3N6_cxV9_qSyqo9JZOmCfpQQ4gllNFWeftGwwSwsiQ2emKYqjqJXKJ5kc7K4GDJPJdfJGCnqx_2kKDDZF5d6kTgnlhyqqEEDKRe97DvAtJpo6gDgEg0TSLBSrIlanQmSF6_xkMfvoj86kRl6CbnjzHWpOiF1ADA0E0qOwsvsAE6Dnv_fpIWOFg6lt7TZAw9vwoYo_8GeBXMFH5rFO5pe3a4LFvHO8gRf2kbAg2t2uQjYLu-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یه مقایسه‌ای دارم انجام میدم</div>
<div class="tg-footer">👁️ 34.1K · <a href="https://t.me/MatinSenPaii/5006" target="_blank">📅 03:19 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5005">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">آقا این Muse Spark هم عجب چیزیه:) روی هارنس درست به نظرم شاهکار میکنه. فعلا روی OpenCode به شدت سریع و اوکیه</div>
<div class="tg-footer">👁️ 34.6K · <a href="https://t.me/MatinSenPaii/5005" target="_blank">📅 03:17 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5004">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">بیاید بریم Rust یاد بگیریم لایو هستیم روی
🟩
: https://kick.com/matinsenpai</div>
<div class="tg-footer">👁️ 37K · <a href="https://t.me/MatinSenPaii/5004" target="_blank">📅 21:00 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5003">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">بچه ها بازی Rust نه. زبان Rust:))</div>
<div class="tg-footer">👁️ 38.4K · <a href="https://t.me/MatinSenPaii/5003" target="_blank">📅 19:11 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5002">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromMatin's Dungeon(᯽マティ️️ン先輩)</strong></div>
<div class="tg-text">بیاید بریم Rust یاد بگیریم
لایو هستیم روی
🟩
:
https://kick.com/matinsenpai</div>
<div class="tg-footer">👁️ 38K · <a href="https://t.me/MatinSenPaii/5002" target="_blank">📅 19:05 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5001">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">آپدیت جدید Aether:
توی این آپدیت روی مسیریابی (روتینگ) و اتصال از پشت پروکسی کار شده</div>
<div class="tg-footer">👁️ 38.3K · <a href="https://t.me/MatinSenPaii/5001" target="_blank">📅 03:22 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4999">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromMatin's Dungeon(᯽マティ️️ン先輩)</strong></div>
<div class="tg-text">هوش مصنوعی و برنامه نویسی | آینده این شغل
لایو هستیم روی کیک:
🟩
https://kick.com/matinsenpai</div>
<div class="tg-footer">👁️ 38K · <a href="https://t.me/MatinSenPaii/4999" target="_blank">📅 21:45 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4998">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">حس می‌کنم شدم هوش طبیعی متین سنپای که پول توکنش رو نمیده
😂</div>
<div class="tg-footer">👁️ 38.1K · <a href="https://t.me/MatinSenPaii/4998" target="_blank">📅 20:45 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4997">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">بچه‌ها شرمنده می‌کنید با استار هایی که میزنید. ممنونم
❤️</div>
<div class="tg-footer">👁️ 37.7K · <a href="https://t.me/MatinSenPaii/4997" target="_blank">📅 20:44 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4996">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromRick Sanchez🤍ریک سانچز</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ruVxAD7ASpn_UZ1fnLBejSWIDtPnNctJky-Wh0NK-CmaT5F7wOl-J1wmkZDLVvrdgfdKYSVgTRStvMWoHKuonl0jCtggjf4PCKK1agxUwwHrrukA-MTEvKoyJSKlS1AmMdGsa4lza0Qeu-80Sa5BUMAGCCqp2YV2pQCxKbJMwfEPb28Y2sBugHDa2b0NWbhHmYx-2mqqJkpxWz4bdWpsk6PxqCTfAJWHwfOpQWRxb_3Aj02JwA888p158dtczH0d_TIWUo9xa8Za16CnJ49E4Q4rOsEOQlJkcgXvy1sclOrXyPv0WqKEFjS81PMhhDdG8TfEGkq1iIZMKisBwDp5fA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 38.4K · <a href="https://t.me/MatinSenPaii/4996" target="_blank">📅 20:42 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4994">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/KbXDtlyTFNgt9Ea5Uyei3dQ008czQ26cmeNkbyv09YO3RKi-84nEYA2s8qnUmo-bECR3RkJrIvAFsWsDodCFVWVGrj1pQp_uCutujFul-WB8l5ouy0NMBwz4S9pdwmKNSA3lKnc3xg-lXcTyifyhuV2T457voaQSFqoMTSDBuX-Xda9r0pjfHNCAWDYpA_x5Z60D9PzI7bewMlbZ74wH2VLFVd9wRvxtHB9htXb034_P6uhX8CqdAvjCVfeW_z3xkz8z447bpfV_KyZSubilSgGXX0kyldNx2oWl1s7OloSwBO2UZsdK47u4_HpkyXUckVTSVKBqGytayHRczHtgKA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/TIyMNv2BvXzib-68qXxEecHvrWsMMbE_hM6MXlQ_sUSwkD9CsmpUqDlU-rPKdrvuxkdymN4kr2S8a7W3YimNhHWar5UWw5vgig3Ou1GoNmnoTn0AE3JUZvRB7TJdXn9xiA5Cdk0HAs4yPPXXlTPlucNCI4eQiLnCXVVb_-MM7pwfjKCTmv_6SQzE6r8ZrROeFixJqKLZO48eBpbcn1gFfgQe7irQtrO05jhRQbHCU-sXPFspTxj-jtNuUOPkWpqCQNtFu0qhR1VgRmH86jB4bzawWF0acXPTEvtSu8zD_7qM_k-oxem-am4IttXPybd4wO5aEKTd2G-BMKKikvezRQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">روش پرداخت بین‌المللی و گرفتن Visa Card مجازی  خب دوستان، امروز می‌خوام بهتون یاد بدم چطوری می‌تونید با این وبسایت، برای خودتون ویزا کارت بگیرید: https://app.mpay.cards?startapp=ref_PzwXZ8 (لینک رفرال هست. می‌تونید آخرش رو پاک کنید اگر دوست نداشتید) 1- بعد…</div>
<div class="tg-footer">👁️ 34.3K · <a href="https://t.me/MatinSenPaii/4994" target="_blank">📅 15:42 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4993">
<div class="tg-post-header">📌 پیام #52</div>
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
<div class="tg-footer">👁️ 35.7K · <a href="https://t.me/MatinSenPaii/4993" target="_blank">📅 08:02 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4992">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Qsd5_tgxYaDy2lnUGdiFJ9cvp01pAMqGHgq1SBRfKq5cj8QeacSm-K7UNsq3zfPFclkz7E5fzFXZTdQp_Lw-S4tHrB46yQerXcIIsoumhmFVdnx334GM4t2FNnM0k74I1oTq_Wihj5iRJ-ioOoTf3lkm1I9qk4MtJOcRCbHYfrZS9CeiNiZh6DTtZjsf5xjRRTvIUPpYiLOgVdxkCxTwcBRG7Y71e1yGxt5-hPXvDfkbsv8IrxihRYJ3Ev61CbZEaYRXfc9nuAHEXEfdMaxs6M0SckPo5DophNLdSd_lUA590unnw19WZlSbsqq6GwIdBz7UAZxUggbRrSJJSYp6Xw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تجربه من از 5 روز کار با OpenCode Go
https://x.com/MatinSenPai/status/2089928470801318139?s=20</div>
<div class="tg-footer">👁️ 35.5K · <a href="https://t.me/MatinSenPaii/4992" target="_blank">📅 07:47 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4991">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/RD4BfDUU8cHVnWKgO6tLHFiM5znAodKsa6IaCx7JJOzGCIHJF01whElD1ZWKgINI2xw9ps7LkHMRomTjaBdh5UszB5LFhLwmn46gwnTGV1mVhIqcmmrS5YV2SFqDza_4qemAYRiWINgWR6QpuH6SwFySuZqzkRSM6IUVvdRhPcguiHEDDGxV1Y7oLR8HDx2qpb0eyZnnvSYUdAyIRzPbNt2CkzwpCKVBbVekMWIhyaVvy772KkBIHRXOzNQDvBcVjVg8hl6pYQOxLJRNCE-T-U8mZ3pnXnS6XWkgMix9FiqZ8ZV0Unk-SdV26-6mWQIf5rQswSGdgI-Vzu_9V8eNpg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترکیب پنل BPB + متد پترنیها + Chain Proxy داره بهم سرعت آپلود خوبی روی آیپی ثابت میده</div>
<div class="tg-footer">👁️ 36.8K · <a href="https://t.me/MatinSenPaii/4991" target="_blank">📅 23:24 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4990">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">لینک داشبورد کلودفلر:
dash.cloudflare.com
لینک ویزارد تحت وب BPB جهت راه‌اندازی:
https://wizard.bpb-panel.workers.dev/</div>
<div class="tg-footer">👁️ 40.8K · <a href="https://t.me/MatinSenPaii/4990" target="_blank">📅 20:50 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4989">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/PJI1Wr8yuNe0wyWt0v8I3pePrzCkvNOPKtvD_hVyZ453x-lz_kso6PmgYFjsXMojcUhFW4XjZmHQ324SZ1ryZUcXL86ahGLxYt-HLpagEf0xMs8mZinbchILeptbkMIwq6M8kdlsKUElJc_js0uIKigkOWuPSwQpEddt8550BodiIqqmrimltRhFoM2aoVOC_ul3kNQt3s8-zZ58i6N0QGaDLTi8M7G_yrZNy2AabYuQJJBwmA_ssZCKP_nMibrSDdzkrHCmmnKlKwdyIRP179MFZ97kNyCGY3Ojz4qFmqn6AimWwicNOOV5fmp0CAFEIckonsqk6BEp92BLGkholg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 41.7K · <a href="https://t.me/MatinSenPaii/4989" target="_blank">📅 20:46 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4988">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">ویدئوی BPB دیرتر میرسه و می‌تونید اداره برق رو سرزنش کنید
😭
😭</div>
<div class="tg-footer">👁️ 34.9K · <a href="https://t.me/MatinSenPaii/4988" target="_blank">📅 19:38 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4987">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/NlFqbe0FCKrhkFw8K98ILrUuOxaM-p9jDuXHa2DPZdct6kWtDvbZjsMPkPt-qGa9UjLCFQ8qbH1E5ocRFRWMcbxgm7gMbfvuKh2CkUBfSg5zWE1A7aET31wqCUn1oessVI6SM8G2NIAg5uff7q2ErjG88H9Mi9gjLD1ZTtbGvopvozPdGza6tCVta1DoaNGDtvAjuWZJU9T23U0UGpt9t7labzXqqV9e00UP3MIw8oHDyls1QpYOTmPHZapyuN5A6r2E2KXAQuoJPkE9IWFvxy5-4IhONEkQv03A3WEzyhScTcIbn2UZi1vUk0LvwCbnqF_hySd79QHzPOH1RG7i-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">WhiteVPN دسکتاپ هم سرعتش عالیه. تازه با ساب خودش هم دارم یوتوب می‌بینم</div>
<div class="tg-footer">👁️ 37.1K · <a href="https://t.me/MatinSenPaii/4987" target="_blank">📅 13:38 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4982">
<div class="tg-post-header">📌 پیام #45</div>
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
<div class="tg-footer">👁️ 32.8K · <a href="https://t.me/MatinSenPaii/4982" target="_blank">📅 13:31 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4981">
<div class="tg-post-header">📌 پیام #44</div>
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
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/MatinSenPaii/4981" target="_blank">📅 13:31 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4980">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">امروز ویدئوی پنل BPB جدید رو داریم</div>
<div class="tg-footer">👁️ 33.9K · <a href="https://t.me/MatinSenPaii/4980" target="_blank">📅 12:34 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4979">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromMatin's Dungeon(᯽マティ️️ン先輩)</strong></div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/iW_fMLElNITHNDOqBGIoslZY-RiRd9cB5pwuhInHPjxkTeIO_h8GmuvDLqzpzjbBQF_CNam5biPaCbJYt9kmc98nS50AnHrazm1rLRQFRhR9qiwocU6_UeRkpJdZBkmqBMs2H-6kA1qOe62-qV6aRc2ycMVmnMCn3aWK5vvFpN2ydN-RmjOWqb8pI3-dQaFEAVKVmreazwOWDXNjzPCjeYXx7D_5F8DmPqTWA1zljHERM28fWpF0BW_90TrqwD93RnVBzHc9RE997D5i9tCZoi7YU6QKlzF3ILf8RMZe8XiC2QqpV7KZAqg6TF6lICSN4IykLMyu4BkNzgg8E7bpMQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دمتون گرم بچه‌ها
مرسی از همه‌ی کسایی که اومدید
شبتون کانفیگی
😂</div>
<div class="tg-footer">👁️ 37.8K · <a href="https://t.me/MatinSenPaii/4979" target="_blank">📅 01:36 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4978">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromMatin's Dungeon(᯽マティ️️ン先輩)</strong></div>
<div class="tg-text">بفرمایید لایو
https://kick.com/matinsenpai</div>
<div class="tg-footer">👁️ 34.9K · <a href="https://t.me/MatinSenPaii/4978" target="_blank">📅 01:04 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4977">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">اگر دوست دارید استریم‌ها رو دنبال کنید، جوین بشید:
https://t.me/matinsdungeon
امشب یه لایو کوچیک خواهیم داشت که کمی گپ بزنیم و صحبت کنیم راجب اینکه قراره چیکارا بکنیم</div>
<div class="tg-footer">👁️ 34.9K · <a href="https://t.me/MatinSenPaii/4977" target="_blank">📅 23:36 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4976">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/uZ7zqPv8Cbzc5SAFmWm8_igiBek-Csu0oTIJqPqUSBpy45KJHu_orNPMZqjGweRYxw0QV5PmEBh4V9UewBR2q2JEkXc8mqbsqypANdmfZYBmCx-GyOQP_iX1CP-EWOU0Py47S7n6yas3AC5lEnSBBPIfepGSf02WPN7EvCNkhJ0G-4GvxwS6Lhp9N0gCmGaR53LF6d_WeL2QW0cOcpaiL55SZMdmVtxByB9ZIA_zmlAKntLnjYy_gHLUXuElggVbOiRtSTuixTwbYCbiRVfaBzw5hn3U79yAkh5Jkua5gcw_1eAgC0UJmO85M_pMZWVPdbI_FtRYgchB9rfUKeKz_g.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 38.9K · <a href="https://t.me/MatinSenPaii/4976" target="_blank">📅 23:06 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4975">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/LDVT26loBpLKLWUQy-Xwdy83oNSK7gxorB1-c_E5NyQ3-uYCYDk0-IKRLQDr9puEg6ce1PDW4ONKkBEJrBXsNg9TNC4Zd-Cc_SH8brwSiak-VKBnI4ff6FlUe2FzQNtkZSc7xmXxjUPx93f5RFue-YfODSH9cGcNUQ1XayVpPezE0YIvbeayUrx1vfaLmPBxfiOFk6eVaJypAXSBvA0BVuYqSTkTnaNuL54cBeqI15vthMXWZqxCUtteoGHGvxePNxEl9r9_c4YEhFYXeG0pVZHkfcQAOgfN_sPveQ4RuT1O1n84qMis6ZMJf2WlHmIo4ypi3KQpB0hz422brFDqJg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نکته‌ای که من فراموش کرده بودم توی ویدئو بگم، این بودش که برای حل مشکل آپلود حتما باید Fingerprint رو روی Unsafe بذارید
عذرخواهی می‌کنم از همه بابت بی‌دقتیم
❤️</div>
<div class="tg-footer">👁️ 36K · <a href="https://t.me/MatinSenPaii/4975" target="_blank">📅 17:28 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4974">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/PXS_RTN7V0ypSp18a41G5oIenn8pNRB12IlnAieZPSRIyXw5iUnIXjqgDN6JXS6ALWjOdQCeOBGLXP6fObzpdHlldqTCxatZlFcdW4lETccbAw-1TqfC0ivkkHT9K5dYIZD_TVfPHUpLjCPdg36rTqtkQez2SVD-AIOzPLQjJ5IDVEMwQE6i9ddbWpDjjGBER1wkhzYXZz53_oVQMLOU5vJyMyGxUBn2W-ifGiMmS23nVGGS7ltlBn_Fiae8PQTl_TSPi1GJLbWkH2cc48UrSKwcnhy48pToOhdVjmtjiLXG1xsyq_D1t3i-WC8Rfhuf9qLiJhf_xE5G_RxB9VzfVw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خب به سلامتی تا ما ویدئو رو ساختیم رفع فیلتر شد Worker اما هنوزم ویدئو رو می‌تونید ببینید سر سرعت آپلود خدایی که این متد پترنیها میده
🥰
که وقتی ویس می‌دید دو ساعت صبر نکنید آپلود شه
و متاسفانه ممکنه بعدا دوباره بزنن ورکر رو فیلتر کنن</div>
<div class="tg-footer">👁️ 36.3K · <a href="https://t.me/MatinSenPaii/4974" target="_blank">📅 11:39 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4973">
<div class="tg-post-header">📌 پیام #36</div>
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
<div class="tg-footer">👁️ 38.3K · <a href="https://t.me/MatinSenPaii/4973" target="_blank">📅 03:00 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4972">
<div class="tg-post-header">📌 پیام #35</div>
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
<div class="tg-footer">👁️ 39K · <a href="https://t.me/MatinSenPaii/4972" target="_blank">📅 03:00 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4971">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">ویدئوی رفع مشکل آپلود کانفیگ‌های کلودفلر و دور زدن فیلترینگ
Workers.dev
در حال ادیت توسط ادیتور عزیزه و به محض اینکه تموم بشه، آپلود می‌کنم واستون</div>
<div class="tg-footer">👁️ 36.6K · <a href="https://t.me/MatinSenPaii/4971" target="_blank">📅 23:34 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4970">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/KJrtEn5DBY0PQGbqaPkxt-HDqYnmBdNqnGPe1f4Ko8QX27mTIuPN2zxMxKnvCzcYCw-LjRhtdOB9KFdzHAEXMASoNG6RydT66UE10K_QTI_b68xYjCG2CHQcIF63n6ibuARq-tYc3FA9DrVozCFOxNGr1eFCeNHzGCLh_Pqhx4ENPJPT_kZTj-yybBkYoWD_dZn0bg7eJ62i4j31RE2140yAm8xYWQPgvHv9OIV2lOh3xNKS4M8TbC-4Vcptg6mS-EA_uyOoVOrsF4Yf6ekSs3X4j9tNUi6t_Oqkib-IUG8mz4ol_jrZqnY_FuwUx83rx5909JnMFYzGhVXoIPUNNQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چیزهای باحالی قراره داشته باشیم به زودی
🔫
از
🟩
می‌تونید فالو کنید اگه دوست داشتید:
https://kick.com/matinsenpai</div>
<div class="tg-footer">👁️ 38.6K · <a href="https://t.me/MatinSenPaii/4970" target="_blank">📅 19:57 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4969">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">با این آموزش، نه تنها محدودیت سرعت آپلودی دیگه وجود نداره، پلکه پایداری خیلی خیلی بیشتره روی همراه اول هم هستم</div>
<div class="tg-footer">👁️ 39.8K · <a href="https://t.me/MatinSenPaii/4969" target="_blank">📅 15:25 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4968">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/U82QR1Y-AjFjJ78Uvoexgpbmh5WevE6_h1Zkpulp6v9XiHm7kjLG0LadgZEgrXtXixvHheo4swKqy7qFWtXkCU8_03sW9-HoibMlHaEgSiKt0zAoSFUgMOfWeoIhJcCT-d7q3DXTV6j1ba9_FD-2pJ0O-LZHfqen52c4Gvus-yXGLYYN5Oys26SBeTmZU9rEALqPEFneuliiQCCGF8qDfHrzY7eRDGFJmcasbqkestYRnEkpqT-BlU37TND1AwOUts-0DoO0RPo83ix5JardPWUWVE4BbuI9o6hLXjEYjoULMwlSqRkO5q-tF2OmY94lXU_Vn7DRW5ot1cnD-b2cYQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آموزش fragment+fingerprint برای رفع فیلتر دامنه و رفع محدودیت آپلود بر روی کلودفلر (ورکر/cdn) حتی روی نت‌های محدود:  Android: https://t.me/patt_channel_x/91?single  Windows: https://t.me/patt_channel_x/101?single  Android/Windows/Mac/iOS/Linux: Use Xray-core…</div>
<div class="tg-footer">👁️ 39.5K · <a href="https://t.me/MatinSenPaii/4968" target="_blank">📅 15:10 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4967">
<div class="tg-post-header">📌 پیام #30</div>
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
<div class="tg-footer">👁️ 31.6K · <a href="https://t.me/MatinSenPaii/4967" target="_blank">📅 07:45 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4966">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromPatt's Channel</strong></div>
<div class="tg-text">آموزش fragment+fingerprint برای رفع فیلتر دامنه و رفع محدودیت آپلود بر روی کلودفلر (ورکر/cdn) حتی روی نت‌های محدود:  Android: https://t.me/patt_channel_x/91?single  Windows: https://t.me/patt_channel_x/101?single  Android/Windows/Mac/iOS/Linux: Use Xray-core…</div>
<div class="tg-footer">👁️ 29.9K · <a href="https://t.me/MatinSenPaii/4966" target="_blank">📅 05:14 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4965">
<div class="tg-post-header">📌 پیام #28</div>
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
<div class="tg-footer">👁️ 29.5K · <a href="https://t.me/MatinSenPaii/4965" target="_blank">📅 05:14 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4964">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">گویا روی سامانتل و رایتل و نت مخابرات و خیلی از اینترنت‌های خونگی هنوز فیلتر نشده Workers و بیشترین اختلال، طبق معمول روی همراه اول، ایرانسل و شاتل هست</div>
<div class="tg-footer">👁️ 38.3K · <a href="https://t.me/MatinSenPaii/4964" target="_blank">📅 00:11 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4963">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">گویا روی سامانتل و رایتل و نت مخابرات و خیلی از اینترنت‌های خونگی هنوز فیلتر نشده Workers و بیشترین اختلال، طبق معمول روی همراه اول، ایرانسل و شاتل هست</div>
<div class="tg-footer">👁️ 39.8K · <a href="https://t.me/MatinSenPaii/4963" target="_blank">📅 00:07 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4962">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">تمام #نکات واسه مشکل فیلتر شدن worker رو داخل این پست میگم:</div>
<div class="tg-footer">👁️ 39.9K · <a href="https://t.me/MatinSenPaii/4962" target="_blank">📅 22:29 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4961">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">حل مشکل اتصال به کانفیگ‌های BPB و تمام پنل‌های Worker کلودفلر:  1- آخرین نسخه‌ی Pre-Release نرم‌افزار V2rayNG رو نصب کنید(۲.۳.۴): https://github.com/2dust/v2rayNG/releases/tag/2.3.4 یا V2rayN نسخه‌ی 7.24.7 رو از گیتهاب بگیرید برای آیفون هم Sterisand آخرین…</div>
<div class="tg-footer">👁️ 40.7K · <a href="https://t.me/MatinSenPaii/4961" target="_blank">📅 22:08 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4960">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/LlYtCowS2LVDvVysHzpIWfLaVLsJIi3uA15v60T26wxt1AT7C15vKQ_7t1NmpBen9WY3HmAp0tZv3vSVXR6UeWPqXTb5gEaLfqndim1VEgSU37Rm6d-_ZOa73hceKiw4VaFjripr9nOu4mdIyhDIggpB3VqfV0jej9bDouzxubxeZHlE4rOM1y3lBMEq1TCDAGsCWjuY9h9Svux-GH45CNnhsjH1ucRKz0-_BQ_UUIvvk4dDUCkcSorqxLKvgiPt4BKP-R0QteIvLB3AS5gP9UFSx2dQyZvhLRisroEtjxfazVwq0G2K5zr7FFLyr6pXCYEf1X9VkUr1UQOLYJ6oQQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 45.4K · <a href="https://t.me/MatinSenPaii/4960" target="_blank">📅 21:52 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4959">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/o6Y2hJviDNJR77hCx5AfFMWSLJQf9VxgaHTtrMVYfPTbb4qadlSar2o_0EAW0x8tyUsWHMBkc-a_bOdXjfWqXhi3cGZG8he8UQrk4kp4bRTTVU7OIzSGT7BEm8rFDGeyQgOCnYWngC3wLU2emdOi6SqamsH5ILlYw3AX6vTlPg3QCI-XIBd_greqaJff0oLEa8lAhTrVjNf17KtFuJGJleYMDgCmhEZ_uQTc7WaoOlyxbe503TPeNUPCJpgiE8B09ZTWQRusyPCXZ7qHVUftBqnW9D5I6NBzOl4l1klIi5kw_Atqo5U7en9EozTSHOU6hepH0D1psHfVfCl_1WvYaA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دست پترن عیان شد
پنل ما جوان شد
مشکل رو حل کردم با کمک Hidden-Node عزیز. الان آموزششو می‌ذارم</div>
<div class="tg-footer">👁️ 31.9K · <a href="https://t.me/MatinSenPaii/4959" target="_blank">📅 21:39 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4958">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PP4FhAZPBjW3WWVxPpThUIeDpU33QIaREvIJAY1_24Wr2zEX2JM1AzDXCG278ccdaR5LX9UZ3fXxJTFzVZ7O_ThSxr_vIa9NInGLOltL_jUbykP1lVD8ZFv8XcLQzQ9Cv6_1Clx3IEfeEsx4oaCnX3jAWvcxjFCMdTrB8gRszY6YrG2Jxr9xI23BMs5ST9Rm5hXBBZZNUnwxGGWiUChsWVzOLd2JbZtInpeYRkSkgTuwxp2Rq55eHBge9y6uKgjaBOTgSPpizLAlA_KSu9iqbXbPK9f9i1PzfP0iBxGxl3jL6cRMeFi16xWlpmHobW857GCaX-PZucNN2F2ZxSkSyQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💬
چطوری فیلتر شدن BPB و Workers رو دور بزنید؟
میتونید با رفتن به منو تنطیمات، فعال کردن گزینه Amnezia Noise فیلترینگ ورکر رو دور بزنید و به کانفیگ های ساب BPB Warp Pro وصل بشید.
این مشابه گزینه فرگمنت هست برای Warp pro و Wireguard داخل اپ WhiteVPN</div>
<div class="tg-footer">👁️ 29.5K · <a href="https://t.me/MatinSenPaii/4958" target="_blank">📅 20:47 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4957">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1dc224c1a1.mp4?token=Xa3UN4lR-W5M29-FcYlhhbul3nh5qMVAjWN-c2A16ndh1jSGEwGdlyPNRoCcuH7sGtqkf69vKLuTAiswTssI_h75LHLjfBUGdx92OzpuSxSTJm0lihGkdy-TV_MbSLuuEe2Z5kAii5446eq3cAkMTwhwX_qjIHS1aYATs77aKbYyceR6xHcE1IvagK1uAIkrhqO0memqpL_LHjttOFFtR5zLQWMOvcVlFfrncgj0DHfMy9IrLdaQSFiAIC6ROIQr22aX-9IA_22Gywjsdrrptq20xKec0I0DJXUnGN9tcvw5MflNlxn3JO-9_ZIOQBtST9R_gMq-VfBrCQL5jxKhNQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1dc224c1a1.mp4?token=Xa3UN4lR-W5M29-FcYlhhbul3nh5qMVAjWN-c2A16ndh1jSGEwGdlyPNRoCcuH7sGtqkf69vKLuTAiswTssI_h75LHLjfBUGdx92OzpuSxSTJm0lihGkdy-TV_MbSLuuEe2Z5kAii5446eq3cAkMTwhwX_qjIHS1aYATs77aKbYyceR6xHcE1IvagK1uAIkrhqO0memqpL_LHjttOFFtR5zLQWMOvcVlFfrncgj0DHfMy9IrLdaQSFiAIC6ROIQr22aX-9IA_22Gywjsdrrptq20xKec0I0DJXUnGN9tcvw5MflNlxn3JO-9_ZIOQBtST9R_gMq-VfBrCQL5jxKhNQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">💬
دوستانی که فقط با فشار دادن دکمه کانکت براتون وصل نمیشه یا سرعت کمی دارید، از این روش میتونید تست سرعت بگیرید و بهترین کانفیگ بسته به اینترنت خودتون وصل بشید.
توجه کنید، هر تست سرعت ۱مگابایت از حجم شما استفاده خواهد کرد.</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/MatinSenPaii/4957" target="_blank">📅 20:35 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4952">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">WhiteVPN-V1.4.0-arm64-v8a.apk</div>
  <div class="tg-doc-extra">35.7 MB</div>
</div>
<a href="https://t.me/MatinSenPaii/4952" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/MatinSenPaii/4952" target="_blank">📅 20:35 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4951">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ujcFfeEOsNq2v6mKjirjckY7raVBBjWNHRG4vItJ9vfVRUWUpSZ3xFWd1vDXI8Z7YBnj875zKHxl6u0Gy6f__23MkRW2I0pwLaePmTw_IfWpeX4QBWntlvG0l84qMcXiiYgr1l7Y006BYiX97oUlaHoYu514YkgYwEfigaELThkQvKN0K1V6f-CsFrEprXlteUQaFAYdYbgjl2ZQtwtF1sWApjKje26FNROXtevMySVItOALUE3kSUQquph02fGa1ES3dCQwUH4_1k_8mm39K5wvZMObc40pEXSY9Oc4h0l0fT6nEhmT4AwJcozFo_pw2AAS1EdooDd9RwF3iYrWiw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🌎
انتشار نسخه WhiteVPN 1.4.0
• ظاهر جدید و مدرن اپ
• بهبود اتصال بعد از قطع شدن
• حل مشکل VPN Mode & Proxy Mode
• بهبود تست اتصال. حالا میتونید کشور رو فیلتر کنید و بعد تست کنید. تست هم به دو مرحه real delay و تست سرعت  تقسیم شده.
🌎
دانلود آخرین نسخه از گیتهاب
https://github.com/WhiteDNS/WhiteVPN/releases/latest</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/MatinSenPaii/4951" target="_blank">📅 20:35 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4950">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">اپ Defyx وصله
متد Aether هم وصله
کانفیگای رایگان MahsaNG هم وصله
کانفیگای مستقیم هم وصلن
پیشنهاد می‌کنم پول به فیلترشکن ندید. defyx و mahsa رو هم از گوگل پلی می‌تونید بگیرید</div>
<div class="tg-footer">👁️ 31.2K · <a href="https://t.me/MatinSenPaii/4950" target="_blank">📅 18:13 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4949">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/g1G-qY8CeXAphciv5eczTkH2ZYJ4iCX5Omh-y1R5ra_Li_9ToS8OFrg9i82jwqCE9x9ERCOzIikMTj8PqaD5_uqsqjke7PrYcVuudefhKRZgAxjlI0oDvEbBFMPITEW2pTAW039RusqWitayaPnD_eggUnNXBqnjJDFrhtFsPuoUP7AddcraG5AigcyqfgFAV43N4pYcbga-6UkCO7STKdTDfh39MRuIZfW2sUt6qXmY4OZoIROQlNg0Pm8Lb4ro0RS0EHP-UD9B5KDpVKfzcQbBRciAm3xKbOdHhNo7tNAesQh8eyRJmFwhxSqnFhlBwvk19brCXA5frrQkc6yM5Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">https://www.youtube.com/watch?v=EZ4q5V6fZh4</div>
<div class="tg-footer">👁️ 32.3K · <a href="https://t.me/MatinSenPaii/4949" target="_blank">📅 17:55 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4948">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">پروتکل MASQUE از Aether-GUI متصله. از اینجا می‌تونید آموزش اندروید و دسکتاپش رو ببینید:
https://youtu.be/2h6qlA1pJFw</div>
<div class="tg-footer">👁️ 29.7K · <a href="https://t.me/MatinSenPaii/4948" target="_blank">📅 17:52 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4947">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">https://www.youtube.com/watch?v=EZ4q5V6fZh4</div>
<div class="tg-footer">👁️ 29.2K · <a href="https://t.me/MatinSenPaii/4947" target="_blank">📅 17:30 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4946">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">https://www.youtube.com/watch?v=EZ4q5V6fZh4</div>
<div class="tg-footer">👁️ 30.7K · <a href="https://t.me/MatinSenPaii/4946" target="_blank">📅 17:30 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4945">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">من خودم به لپ تاپم دسترسی ندارم الان. اما Sni Spoof باید جوابگو باشه قاعدتا. اما اون متد تغییر دامین رو هم الان چک کردم و بستن</div>
<div class="tg-footer">👁️ 28.7K · <a href="https://t.me/MatinSenPaii/4945" target="_blank">📅 17:29 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4943">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/GdFZ95NelIjYJd7sU-bhqkYsM-Z7YFmpnKYQI45L0fJjcRoJiardO0QWACQ7HEQfZBHhUzBMPgGgnDIQKrrbtMiByidr32_mVct2DRp9302s37LhvAk3j7tMJeS72hW-9Y0x5x6bBeCMOCEDQa-q4tOalyKN8dEQzaqQImty_CnSfuGoQtwL03lzQ2QDQ-sbsO6p6VOfZdCYrzihSPd8JiBAnVFvxQkHRkSbGro8rkFSZsKhLLQW_0Bz6achSe75Wh6AOp2HFKBsiMqh4paBsB4PlYLLS2U9if4_H1Jdzw_nWpt1sngpi10R65dV1Ivxm1BMAk9LwO1RpctDGex5Dw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/Mto4pW4jEaLmMlQI4EvlXTFXd3EmM0OL4Lwce1qRv3AjVOHs2GAsK_Ecior3U8T57HWr_7PXAeieMB2iplU2wECC7krJTlfnjq9HlkDhg7KrSgND-EkJswHZYrGj3fl4U_e-xJ1cJlZR9usgI6OuFMdx-ptkI7xLpj7wlaYMwJ9g-fDyLsNcoWqXnepznAjdSimXuhnqRWhgMzde5OJQsJp4YsoziYOTItfps1kB1YJYZaVNY_DAxTpzzxwd01kkPTvVER60wEZCyRKaLMC6zj-j-VofrG3hu7jYlCOeXgLJJlDksfls4p9BgFZbJNDtpS8O0089kLQ4dtRfCUjLEQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">از صبح داشتم پیاماشو میگرفتم. الان برای خودم و دوستام هم قطع شد فکر کنم که ساب‌دامین‌های *.Workers.dev فیلتر شده باز. بررسی می‌کنم</div>
<div class="tg-footer">👁️ 31.9K · <a href="https://t.me/MatinSenPaii/4943" target="_blank">📅 17:21 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4942">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">از صبح داشتم پیاماشو میگرفتم. الان برای خودم و دوستام هم قطع شد
فکر کنم که ساب‌دامین‌های *.
Workers.dev
فیلتر شده باز. بررسی می‌کنم</div>
<div class="tg-footer">👁️ 34.4K · <a href="https://t.me/MatinSenPaii/4942" target="_blank">📅 17:16 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4941">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-poll">
<h4>📊 کانفیگای کلودفلر شما هم قطع شده؟ (چه Worker چه Pages و هر پنلی)</h4>
<ul>
<li>✓ آره❌</li>
<li>✓ نه. وصله✅</li>
<li>✓ نداشتم. دیدن نتایج</li>
</ul>
</div>
<div class="tg-footer">👁️ 34.4K · <a href="https://t.me/MatinSenPaii/4941" target="_blank">📅 17:14 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4939">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">برای نجات یوتوب فارسی و درصد تشخیص ویورها، برنامه‌هایی داریم. و طبق تست‌های کاملی که دیشب گرفتم، خبرای خوبی دارم واستون و توی یکی دو روز آینده می‌بینید دوستای خوبم</div>
<div class="tg-footer">👁️ 36.6K · <a href="https://t.me/MatinSenPaii/4939" target="_blank">📅 11:59 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4938">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ZfunFDNdmwMvSElgeSvANpoIp7f60OJLp75fLvQ7hdD4pc_Ytzw8dJi4d0aL4jiFe51bOx4LiLR1MSOEx8PtVOH4e_9WYvc7swSp2hGb2eN8eKRqjHk1NcWuYijnzwZJg5OdRZitNMg2ifHwW6X2t4ygUG78Kue3yNGWvjZRuaug0Na3YHZOEmVEFipMkfgezGLg_RTs76GBPHSvAf8pwAMngiDKo7KwfdK8n2hKC_37e_-7Yu0FftI-SNNYhSw8htYlveZSjPoCmaF2q6VoAWb4BSUKB5tTbBGgK59_4wSVZHcmxkZ1y-Td3EeC9lQ3OBsj5YyInn42LMa2SJtbOg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">روش پرداخت بین‌المللی و گرفتن Visa Card مجازی  خب دوستان، امروز می‌خوام بهتون یاد بدم چطوری می‌تونید با این وبسایت، برای خودتون ویزا کارت بگیرید: https://app.mpay.cards?startapp=ref_PzwXZ8 (لینک رفرال هست. می‌تونید آخرش رو پاک کنید اگر دوست نداشتید) 1- بعد…</div>
<div class="tg-footer">👁️ 39.7K · <a href="https://t.me/MatinSenPaii/4938" target="_blank">📅 23:37 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4937">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/XdMhp1ys_2b7Y2lH-TNFu8ponXnLWqBD-GeDYPDuBVtilkVIuqiOB3Plc1qtjmIwWyuLH1HZyPrHg1TqgDCgMkn709VKob6EXVJQnLbDDBvuERLu7I8245fYiKXfAZPcb5oQFNG_-d3XLEeQQGozGtDtfmdByYLmiS39lzdo0KPoHfJILCxBXYifn05aHMa3Wad4DMG5bV7FVQf2cV_dBrYFN18-93TxOH1M3f0AFhXKQciejfnoNkO64kkbfjbbMKNfegWhVEU7LlVNPlC5FbhL1AmGaCjKpfQrvqFVnlwm8D5h-ksON8J82pDgEndL8Lgzer5xGcgyWfmWyG6Z4w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پرامپت ویدئو آخریم رو که با KIMI3 رفته بودم، الان دادم بهش و واقعا نزدیک بهش در آورد
🔥
به نظر باید منتظر یه مدل خفن باشیم. فعلا توی Preview هست مدل  تازه Kimi نتونست One Shot کنه، و این One Shot کرد اونم فعلا رایگان! کیمی نزدیک 3-4 میلیون پولمو خورد
😂</div>
<div class="tg-footer">👁️ 37.7K · <a href="https://t.me/MatinSenPaii/4937" target="_blank">📅 22:38 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4936">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">به همین راحتی.
تموم شد و رفت</div>
<div class="tg-footer">👁️ 37.4K · <a href="https://t.me/MatinSenPaii/4936" target="_blank">📅 21:15 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4935">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/giVH_1uVYCKVRos3HHDdGiNNNaTfc2kU93KSRHgTrZFr4HaIe3CRLhkCtbjfKa6kLeYQaI42pSj5nbCEyKQ5xuVDtloY18Y6rc-udwmdJEMiy9o93-xj2NYyrfMS8qyGFxmnQEdfKkBTKibm_oWclxUA9Gk4lBTSbMKBufU97cYlHR3BWkuzyh1lbAVoFo2F6cAQW-YP1IPapmlht5ja8f2xSEtQ4AVojGR08r41bCNebxR3cSyT7rgyKlVG0_Td6IMyDxlbF3UxkLN6Jq-4dbRQpqscXv8au4c713ZFMjisU72cUXZ2vahJIfXB-urHTsXs17hemTwAZ40W2Hiy8Q.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 32.5K · <a href="https://t.me/MatinSenPaii/4935" target="_blank">📅 21:14 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4934">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/CxVLson9HOPLnx6Ih_47YaxONVzK1C8E_XxiF_x3EvtLX3wkSep5otMFkNhPyyL9JSnJ4ea9gXPvKQoamTvF0lUvbUOz_sWwxM62atZj4VeO10i8qyg3N-GlIJWYKaV5hfi2KGMM1dvV2i357OZ6YADlLOEXArLWH0nhTAfkxmZquLXJnjbc0gwP1At2ZE0RxXlHX7LXPJPbExvOAlZNF9__mDltc_HBPF73sATfA8F5TBN8tUA7nEMl1ygaSoSvG4Hy2139lxeLM2BhDNRkJSaHWxbWD7YT-EHneApKSul81BdZ3M_vXsKMPflEsr5KxV5-IVzvSOwDcFBIoe6cPQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دیپ سیک هارنس رو دارم تست می‌کنم، خیلی باحاله محیط UI اش سبکه، و کاربرا هم توی ردیت خیلی گفتن که Caching اش عالیه. یه بنده خدایی قسم میخورد 4 ساعت باهاش کار کردم با deepseek pro فقط 60 سنت مصرف شده بود. باحالترین قابلیتش اینه که میشه Mode شخصی ساخت. و از معایبش…</div>
<div class="tg-footer">👁️ 32.5K · <a href="https://t.me/MatinSenPaii/4934" target="_blank">📅 21:03 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4933">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/nJlBfp360ujubo3_sK4BfFIRUH0eHmANrJTZ9d1FSWfomWaBMmEhBGD4RzjxDJfnMlpT-yD0I-zWvSstWZonjbPMnVUiAAm_SF3Wkqo_jLlzKENfatFJFgQVJL_WBY_qAJ_o1N79xwRyTcteHiuw5oWgODTAUoKr1IldI18OZ9CZDMhDtJEAbFiGaGXf4S4L23vL0Y84tSv6b8zqnx_TZo5z6SzfcLcGsRY8ARdmNNgQo35scgQ-lK-Dbxs3GL7Np6rzGNSmC_3_uzym901kH6EFO3IwoPfHz8bdkXHz51akr-mezz-xRjKkOkzae6i92RVQEv7jT6yGekztoTUH4g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دیپ سیک هارنس رو دارم تست می‌کنم، خیلی باحاله محیط UI اش سبکه، و کاربرا هم توی ردیت خیلی گفتن که Caching اش عالیه. یه بنده خدایی قسم میخورد 4 ساعت باهاش کار کردم با deepseek pro فقط 60 سنت مصرف شده بود. باحالترین قابلیتش اینه که میشه Mode شخصی ساخت. و از معایبش…</div>
<div class="tg-footer">👁️ 34.7K · <a href="https://t.me/MatinSenPaii/4933" target="_blank">📅 20:50 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4932">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/a1shiCT55bM9rpp-dWkXzFUG0WkqTw7xq2tXH87ksnt43yUiUiiJvLd0KGrmoLJQfhO55Dip25JX2a86iJozVy-mZDZD-BxxjWGg7lggGXXH5z8MUxeQ847O1PMgQ19rMW9_hpqO413Yze763VMmKtJQK_lYfiMo6ZNZC5rz3Flq4rw2anRFPioh4F8fvHFO7f6KRlwamAaVWPutl88OauLcCevoBFQvAdl1Z85GIHwQZ5m-k34owKC419eWIlSLHPBAEIRdyrGq6tgY8QwOJJ7DYbd1lg8nlgz6Kn-Vm_3lx_TTrwaLlSqW9E0Xb0x0nICThioJW5XzLSRLY3IJQQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دیپ سیک هارنس رو دارم تست می‌کنم، خیلی باحاله
محیط UI اش سبکه، و کاربرا هم توی ردیت خیلی گفتن که Caching اش عالیه. یه بنده خدایی قسم میخورد 4 ساعت باهاش کار کردم با deepseek pro فقط 60 سنت مصرف شده بود.
باحالترین قابلیتش اینه که میشه Mode شخصی ساخت.
و از معایبش هم که بگم، درسته UI سبکه اما کاربر عادی ممکنه یه کم گیج بشه
و همینطور فعلا توی فاز تست هستش
و ساب ایجنت‌هاش هم مشکل دارن
پیشنهاد می‌کنم ستاپ فعلیتون رو ول نکنید بچسبید بهش، صرفا در حد تست
مدل سفارشی هم که می‌تونید اد کنید طبیعتا. من الان OpenCode Go اضافه کردم</div>
<div class="tg-footer">👁️ 34.7K · <a href="https://t.me/MatinSenPaii/4932" target="_blank">📅 20:46 · 23 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>

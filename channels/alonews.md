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
<img src="https://cdn4.telesco.pe/file/V06Vx_Ph5BJQfpTsFpQ0v7ibQsHa9vyUH3fIz-peco3MCJtmg48yka9YWNBke_-xPIK520J9ni9vJr_Fn2TCPS-udygPuRmnYg0s3RhI3WH8SWny_FXHWfXbX3dHugoutq4rIPR5OsvnU-xg9YgZFFGtu2wTZ6oFDM3Yk95Ip7MWRoATknTysgzzQKPq67NVpdyIrxlsF9_yN7bZ04etDVjTucwjzaPgDY9gk9i-772r-9j1nsLYsjxgpEQDYPiuz_YccWpXIerayTMXUAqpayIFAG3pwMdn0UBSCbfmsQ04MbhxWCh6ycomDaBdYRHg7kTC19vzuGye5fCbPzMsJg.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 اخبار جنگ الونیوز AloNews</h1>
<p>@alonews • 👥 1.01M عضو</p>
<a href="https://t.me/alonews" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 با الونیوز از اخبار جنگ و وقایع در چند ثانیه مطلع باش!اخبار جنگ بدون سانسور در الونیوز👌جهت رزرو تبلیغات👇https://t.me/ads_alonewsپشتیبانی کانال🕵️https://t.me/AloNews?directمالک کانال🎩@AloNewsBotX:https://x.com/AloNewsBot</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-07-01 18:37:34</div>
<hr>

<div class="tg-post" id="msg-148988">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/f769da6b36.mp4?token=QImMGZbCX5TWUxa58d0IJl6SIsJZKAdGGkoUip5dyX8cKyKWKh8adf7yQY6oKWKl5lZvsSVmLbRTuLA6EXv-LFX6xI75qYvKtDkMmpf2Q6pJhYsRKmkeQ0fBxasYpP1LaMBNgz5c-nUdIT9nsanO4r9GVYakCNd_HO5UilW4bGfWPOMEsEtK1bJajgtxE-hHzP6uCugWt1iqaGU6wvbWhPmq-QS4b5rDsLpr0zhu9DumTyAmGDjzZQpUR7TesJQVA8XlyrQGz8FJhOrhbxJkYiWZ_Gp08mYZIP_7Hn08y3EipH5hSqTCFCRLxpfN8p0UXMdsHyrFip28O1j8-VhLpQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/f769da6b36.mp4?token=QImMGZbCX5TWUxa58d0IJl6SIsJZKAdGGkoUip5dyX8cKyKWKh8adf7yQY6oKWKl5lZvsSVmLbRTuLA6EXv-LFX6xI75qYvKtDkMmpf2Q6pJhYsRKmkeQ0fBxasYpP1LaMBNgz5c-nUdIT9nsanO4r9GVYakCNd_HO5UilW4bGfWPOMEsEtK1bJajgtxE-hHzP6uCugWt1iqaGU6wvbWhPmq-QS4b5rDsLpr0zhu9DumTyAmGDjzZQpUR7TesJQVA8XlyrQGz8FJhOrhbxJkYiWZ_Gp08mYZIP_7Hn08y3EipH5hSqTCFCRLxpfN8p0UXMdsHyrFip28O1j8-VhLpQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
خبرنگاران ایران اینترنشنال در بیرون مقر سازمان ملل وایسادن تا پزشکیان بیاد بیرون
و ازش سوال کردن
:
🔴
خبرنگار : چرا اعدام هارو متوقف نمیکنید آقای پزشکیان؟
🔴
چرا کشتار مردم رو متوقف نمیکنید
🔴
دست شما هم به خون آلوده شده آقای پزشکیان
🔴
پزشکیانم هیچ کدومو جواب نداد  سرشو انداخت پایین راشو کشید رفت
✅
@AloNews</div>
<div class="tg-footer">👁️ 8 · <a href="https://t.me/alonews/148988" target="_blank">📅 18:37 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-148987">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/953c03a875.mp4?token=O71WtrRhT3ZQH30GM3wWn7oxveSferQObT7pGbHzqJ05IOLKAujjDDRAKRegOuPG2Wiw6SXcXHn9ee_cNLs9FmYluFlWVA92LFbw8ysUSf7ugUDshZy4677VNCp6-z3FTBwtW_u9IPyq1_-rSXo9PeV5qSTrKagdeucspg7wwVVm-1g8TajLOC4HcQ2BAQ1x9Bs38oVbRtq_BVwFYDDQ3_SYleMBaWgpWtlMkaUD55aVZw-ClhHpC43M2FmSod7B7vkeoRmiFRvglve67MQB8pgNSXIeLalddG4g1w_VFCINDXZcQOrZYF6w7LhnujoI-R_eEZHQONw4HZ25Wm1Gnw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/953c03a875.mp4?token=O71WtrRhT3ZQH30GM3wWn7oxveSferQObT7pGbHzqJ05IOLKAujjDDRAKRegOuPG2Wiw6SXcXHn9ee_cNLs9FmYluFlWVA92LFbw8ysUSf7ugUDshZy4677VNCp6-z3FTBwtW_u9IPyq1_-rSXo9PeV5qSTrKagdeucspg7wwVVm-1g8TajLOC4HcQ2BAQ1x9Bs38oVbRtq_BVwFYDDQ3_SYleMBaWgpWtlMkaUD55aVZw-ClhHpC43M2FmSod7B7vkeoRmiFRvglve67MQB8pgNSXIeLalddG4g1w_VFCINDXZcQOrZYF6w7LhnujoI-R_eEZHQONw4HZ25Wm1Gnw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
مجری آمریکایی: تعحب میکنم! ترامپ جمهوری اسلامی رو تهدید به نابودی میکنه وکلی بد و بیراه میگه اما نماینده ایران خیلی ریلکس نشسته و گوش میکنه
✅
@AloNews</div>
<div class="tg-footer">👁️ 7.15K · <a href="https://t.me/alonews/148987" target="_blank">📅 18:32 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-148986">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mRvB19FeRjmM8EuGKbXXwaLwqsjmuvjnxDVBNuvu6_c8r4or9N40wDt9bapR_XYPVxGl_pQsJ9KVW2QEJHRgTWkVqVXvc7N4gGpToz-lQ_rEiZ0zjfvHtMRe6Q1mtb3VV94g3VZWbOWgsgEsBn0H7ia8hXw_WXAdBNi7iF3VCT0fXu3pxPCFALpSjs1PJBQwvXZrBoUp9aVy3nY6sVpJ_vnXMQvt_TizMF97cPZ-CYNzr2-WT1XwxCwJmSlJX3eqVK8HCF192szsX2oNRwvf3zgttewj0lPY1cMeNAykwuT4Clb1Yd7ytln9E9HjgGMbVzcqnuo7TELqRt8E6rBxQg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
تصویری از مخاطبین سخنرانی پزشکیان در سازمان ملل
✅
@AloNews</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/alonews/148986" target="_blank">📅 18:27 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-148985">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">👈
وزیر امور خارجه آمریکا: رسیدن به توافق با ایران نیازمند کار مداوم در یک بازه زمانی طولانی است
🔴
ما به دفاع از تنگه‌های دریایی و باز نگه داشتن آنها ادامه خواهیم داد.
🔴
ترامپ گزینه‌های متعددی از جمله گزینه نظامی در اختیار دارد.
🔴
گذرگاه جنوبی تنگه هرمز باز است.
🔴
ایران معتقد است که دموکرات‌ها در انتخابات پیروز خواهند شد و ترامپ قادر به انجام اقدامی علیه آن نخواهد بود.
🔴
نیروهای نیابتی ایران در منطقه، امنیت و حاکمیت کشورهای آن را تهدید می‌کنند.
🔴
ما همیشه مطابق با منافع ملی خود عمل خواهیم کرد و نظم بین‌المللی را بالاتر از منافع خود قرار نخواهیم داد.
🔴
با کشورهای خلیج فارس در مورد لزوم باز نگه داشتن تنگه‌ها و مصون ماندن از هرگونه حمله، اتفاق نظر وجود دارد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/alonews/148985" target="_blank">📅 18:19 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-148984">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jvGd_js5lGbDQ0M5TFp9Nvw12xHKAg9ADwUvNGERTy4MH-JTVbMrqzQD3wgcTzGGc5A2JpTcfNaT3aFPtqbtqHjzjmTsViTevU85BwlOdVQeLcmPXi6PfBEx0PB3Bf70O6gmNi54guODOT625fcZmfQHUlqKXHXwlSovQZsDdoLhMClgDL6_vTsCLQ0Dx8ZlL0wGm13nRmEP-INQBFRWfgmMgSXVYSVVSb5aH2oQ-Zmu0AVeo7jlAZI-CH8fVV0Tc1-eO3FoEGfTHeQAFd-m9dG98BM6Z0_5dw3L_xT5irwQIqtxTWa-71QwHINi30JiYGBIpOzNXovur0zTZURn1Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
صف‌آرایی علیه وزیر اقتصاد در سازمان بورس
معاون اول پشت تحرکات در سازمان بورس است؟
🔴
با نزدیک شدن به پایان دوره ریاست حجت‌الله صیدی در سازمان بورس، تلاش‌ها برای حفظ او و مقابله با تغییرات مدیریتی، به شکل‌های مختلف شدت گرفته است؛ از مخالفت با برخی تصمیمات وزیر اقتصاد، علی مدنی‌زاده، تا تلاش برای بی‌اعتبار کردن برخی مدیران منصوب او در سازمان بورس.
🔴
در این میان، ادعاهایی درباره حمایت معاون اول رئیس‌جمهور، محمدرضا عارف، از برخی این اقدامات مطرح شده است؛ موضوعی که در صورت صحت، می‌تواند نشانه شکل‌گیری اختلافی جدی میان برخی جریان‌های مدیریتی اقتصادی دولت باشد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/alonews/148984" target="_blank">📅 18:18 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-148983">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">👈
سخن پایانی پزشکیان: ما آماده گفتگو هستیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 28K · <a href="https://t.me/alonews/148983" target="_blank">📅 17:59 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-148982">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">👈
پزشکیان خطاب به کشور های منطقه:
یا امنیت را با هم می سازیم یا ناامنی را با هم تحمل می کنیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/alonews/148982" target="_blank">📅 17:57 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-148981">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">‏
👈
پزشکیان: چرا برای فلسطین کاری نمیکنید؟ مگه ظلم رو نمیبینید
✅
@AloNews</div>
<div class="tg-footer">👁️ 29.7K · <a href="https://t.me/alonews/148981" target="_blank">📅 17:56 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-148980">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">👈
پزشکیان: بمب اتم و سایر سلاح های کشتار جمعی در دست اسراییل است اما از ایران می خواهند که بازرسی کنند
✅
@AloNews</div>
<div class="tg-footer">👁️ 29.6K · <a href="https://t.me/alonews/148980" target="_blank">📅 17:55 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-148979">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">👈
پزشکیان: اسرائیل به هر کشوری که دلش می‌خواهد حمله می‌کند
🔴
عاملان ناآرامی اسرائیل و آمریکا هستند
✅
@AloNews</div>
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/alonews/148979" target="_blank">📅 17:54 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-148978">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">👈
پزشکیان: حمله به زیر ساخت های غیر نظامی خلاف قواعد بین المللی است
✅
@AloNews</div>
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/alonews/148978" target="_blank">📅 17:53 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-148977">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">سالن چه خالیه
😐</div>
<div class="tg-footer">👁️ 29.6K · <a href="https://t.me/alonews/148977" target="_blank">📅 17:53 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-148976">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d5081a6f90.mp4?token=oeQXCPg-6hDnzJVS3B6YSm0p0ofMLcpX-6pDMUkZVvEccOI3eB_cAUcsEWQ1Aa8hA1M3PYDNZZmruLkllk2PSmQDaFgGET_G4Pw0jzel9C_tp3Xl7_Ndil7Yu40OAf_oJP0BAoVzL06o5Pf2DfaRPUZJpFnYOQ4guGv79rIM1L4rMWIn1qbqYLvDpJclwz4KcNZ5Ac5CmQyg1bTSgrluPxI_AJk6dEh83lTwiNIjdCeiWsrohqDuMi1inBIRqeni8XE38VV83jKgMrcu9n13ivkIEjsqH7dy6-FM-eTi9Cs7NopPSkLqazj_SeQOQtU-Zd1pmHZZWeHg5uPq-xTL7oWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d5081a6f90.mp4?token=oeQXCPg-6hDnzJVS3B6YSm0p0ofMLcpX-6pDMUkZVvEccOI3eB_cAUcsEWQ1Aa8hA1M3PYDNZZmruLkllk2PSmQDaFgGET_G4Pw0jzel9C_tp3Xl7_Ndil7Yu40OAf_oJP0BAoVzL06o5Pf2DfaRPUZJpFnYOQ4guGv79rIM1L4rMWIn1qbqYLvDpJclwz4KcNZ5Ac5CmQyg1bTSgrluPxI_AJk6dEh83lTwiNIjdCeiWsrohqDuMi1inBIRqeni8XE38VV83jKgMrcu9n13ivkIEjsqH7dy6-FM-eTi9Cs7NopPSkLqazj_SeQOQtU-Zd1pmHZZWeHg5uPq-xTL7oWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
پزشکیان: اسرائیل در شهرها و استان‌ها دست به ترور می‌زند
✅
@AloNews</div>
<div class="tg-footer">👁️ 29.6K · <a href="https://t.me/alonews/148976" target="_blank">📅 17:52 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-148975">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">👈
پزشکیان: والله دنبال سلاح اتمی نیستیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 30.1K · <a href="https://t.me/alonews/148975" target="_blank">📅 17:50 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-148974">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">👈
پزشکیان: ایران نمی‌پذیرد دانش هسته‌ای دانش انحصاری چند کشور باشد
✅
@AloNews</div>
<div class="tg-footer">👁️ 29.6K · <a href="https://t.me/alonews/148974" target="_blank">📅 17:49 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-148973">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">👈
پزشکیان: قدرت نظامی ما برای دفاع است و از هیچکس درباره آن اجازه نخواهیم گرفت
✅
@AloNews</div>
<div class="tg-footer">👁️ 30.1K · <a href="https://t.me/alonews/148973" target="_blank">📅 17:49 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-148972">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">👈
پزشکیان: دویست سال است که به هیچ کشوری حمله نکرده‌ایم و فقط در حال دفاع از خود هستیم؛ حال شما به ما می‌گویید تروریست؟
✅
@AloNews</div>
<div class="tg-footer">👁️ 30.2K · <a href="https://t.me/alonews/148972" target="_blank">📅 17:48 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-148971">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2d23473339.mp4?token=Q2JDu9zZzbkkaLYbYDwok8ouO1i1P_Oxlhxjmt_CE-w9R-h-VH_TLXjZPVoi9aD6FVrjYW4ZOBLDh2YABr8GrfJ0DN6sO9nbNS02IGeVBHyU5F1SbHY1g-1X-0ME9ZERSnonjqihKR_CF2z6SQq6iEZthwdbyfe-0O5s19Bl6OlZiK_NCqnzZN18NElzxENqFAsUTVsZvFg6zSQ0GpEfZgrdIN6Ktm4MfPu4akZYLyKJZfLvq3wDLP3FcqsHRAseB0R_sg9EgZyhSjPBzT4qdEysC-nhbiJ3A6PUkkQijZM6ZHs9qh1I4w8mzG6b-pmiy0EkMD6UogYgs448Ln-UhQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2d23473339.mp4?token=Q2JDu9zZzbkkaLYbYDwok8ouO1i1P_Oxlhxjmt_CE-w9R-h-VH_TLXjZPVoi9aD6FVrjYW4ZOBLDh2YABr8GrfJ0DN6sO9nbNS02IGeVBHyU5F1SbHY1g-1X-0ME9ZERSnonjqihKR_CF2z6SQq6iEZthwdbyfe-0O5s19Bl6OlZiK_NCqnzZN18NElzxENqFAsUTVsZvFg6zSQ0GpEfZgrdIN6Ktm4MfPu4akZYLyKJZfLvq3wDLP3FcqsHRAseB0R_sg9EgZyhSjPBzT4qdEysC-nhbiJ3A6PUkkQijZM6ZHs9qh1I4w8mzG6b-pmiy0EkMD6UogYgs448Ln-UhQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
هیئت نمایندگی آمریکا در حالی که پزشکیان در مجمع عمومی سازمان ملل متحد سخن می‌گفت، مجمع را ترک کرد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 31.3K · <a href="https://t.me/alonews/148971" target="_blank">📅 17:46 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-148970">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Sv2ijbW6TWDHHU8XWSq6vNLu5PKuhW1asn6qdJAKqVWfiDXTF0tbMpmceTudVo-mWlUcxVT9WHOtxlEZ_zQndetDCtGqb1Odj7ntGRd1t70sQpDPNeFQgHABH-QXeEHzC4r52-rtSwm3jZqCmTy12SMujbgLQerCCtuX3IJpJlXnm72QkTmdwMxo2G2agB7Mpr2I-Y82NTQXQme-rWDH3Dit1giFAUQM5xw9ToSpU8p5nQ6AgdfMVGbez1r1IZ8pMpzwqrZZ3jE7YjuGX4ik5Xha35MLw0Q9ihGho58mB9xvHUP2SIE2HT4mwiGMsgrwFyp51qPqnvIJJJSfVx4Cwg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
تصویر کودکان بیگناه مدرسه میناب در دستان پزشکیان
✅
@AloNews</div>
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/alonews/148970" target="_blank">📅 17:46 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-148969">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/091ba5b08c.mp4?token=R0Kb8ivX3jTN9Q4r4gO_uOQOeaBqTm3Bw-RyaDOpIgnULqAKwniGkLxQWC86LidWWDCkYiC81-xAuYeRkmjqchr3ugee4yY15wRQm82rlhFTdYvjPDmmItDPFawyMJCB9z8O_g2R5EXeXP7zGcTdRe3tX_IpdM5sjgwL5soOSFabs3-ORe4cEo_7Jr3TwyQSkIrHMLle-pq5Z_PNT3F-Qcm1ZwL2bESLBEqJ8KqNYwKOGybP4KYIbxBkRl26-1XpEv_Uu82cFfRnZPN02Iav7C1owfBwlVEKZeqtxVn_mSsX3FJOQGq1oYHXpoopysbLmD4INEXo5TDVFqcj_O7c2Q" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/091ba5b08c.mp4?token=R0Kb8ivX3jTN9Q4r4gO_uOQOeaBqTm3Bw-RyaDOpIgnULqAKwniGkLxQWC86LidWWDCkYiC81-xAuYeRkmjqchr3ugee4yY15wRQm82rlhFTdYvjPDmmItDPFawyMJCB9z8O_g2R5EXeXP7zGcTdRe3tX_IpdM5sjgwL5soOSFabs3-ORe4cEo_7Jr3TwyQSkIrHMLle-pq5Z_PNT3F-Qcm1ZwL2bESLBEqJ8KqNYwKOGybP4KYIbxBkRl26-1XpEv_Uu82cFfRnZPN02Iav7C1owfBwlVEKZeqtxVn_mSsX3FJOQGq1oYHXpoopysbLmD4INEXo5TDVFqcj_O7c2Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
نشان دادن تصویر علی خامنه‌ای توسط پزشکیان
✅
@AloNews</div>
<div class="tg-footer">👁️ 33K · <a href="https://t.me/alonews/148969" target="_blank">📅 17:45 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-148968">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">👈
پزشکیان در سازمان ملل:
ما قربانی تروریسم هستیم من از ایرانی می‌آیم که رهبر ما را بدون هیچ دلیلی ترور کردند
✅
@AloNews</div>
<div class="tg-footer">👁️ 29.3K · <a href="https://t.me/alonews/148968" target="_blank">📅 17:44 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-148967">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lrH4EOasXBCOoCaQNfckWMrtLdEh2YxsM7GCUWWX7QvrUotgIWLL7xASXVcmt1jZCsIkjE1WOYpK8AOoCPDuvLiyqE1YtnnMAzXskJ_Za8aeatWRaMgK-_6qhEHYSM1ZcOXbePAkP-qTsaggooa4kmzy678fe5WDKAuo7dLF5nYvzCNA-7RGqXPS8616qCL9RDDbi8ihZbxPwCay-eFaSOSdFpeBgIHqfvBZXyzZ9n9CVbborsUdq-H_YMkq1n8kdOuQe1IluI4qR_RHowpo1Zsy5QoBm2f6N6GwcDU5JVwaxv951SDJd9WJFBCl9-UkDtcbCajXafsiBxFlaHZFjQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
سیس پزشکیان توی سازمان ملل قبل سخنرانیش
✅
@AloNews</div>
<div class="tg-footer">👁️ 30.9K · <a href="https://t.me/alonews/148967" target="_blank">📅 17:42 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-148966">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LKQDhqUxfHH_9L-9yBhJArYCwlPuGbojlFDDFBCcBx0O7AkjIq7FJk05NenEbmekUCdMJklnvQPQBVHBjCm38F4V2ubDCeu3cLbrThMCed-4uASmyGcm8qRFeLD_rm56OQzLVJO8Z00Qr8U2rVLDwe1AZaXS54bDd8qDU18cSTzOcdUfeHHjZ96DxkWAqlgpbqj_OPNbNIJ8fi67GmEsNTOUZkZ4P67IyKLfSchSOZziZUUceIUQBjzzp5hIika7yDjrcLJx2SKWCHCsCJ377AU9QPXpHZ3O6Kgf8dosBzTYHtub0UQxK3MBWlsoU0H213FKdV85k5fUPoUktZHOIw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
محسن رضایی:
ممکن است ترامپ به کوهی در ایران یا سایت‌های هسته‌ای ما حمله کند؛ ما طرح پاسخ را آماده کردیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 32.4K · <a href="https://t.me/alonews/148966" target="_blank">📅 17:38 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-148965">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">👈
پزشکیان وارد سازمان ملل شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 32.7K · <a href="https://t.me/alonews/148965" target="_blank">📅 17:32 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-148964">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">👈
هشدار فیلدمارشال رضایی به ترامپ: وقت را تلف نکن و شروط ما را بپذیر
✅
@AloNews</div>
<div class="tg-footer">👁️ 35.8K · <a href="https://t.me/alonews/148964" target="_blank">📅 17:26 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-148963">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/97d21bb84f.mp4?token=CXV2xQCsN9SWdM7kJX58VMdVt8rMkRdi01-OR8VvMa3DoMNglfpLmqKqlH0aalrHIXruK9pgTACLkUpc6FGv-MsyweWqYyKXMD9ppI0q_mPwrh59RjK4HyFvPavVRqmi6AyPrN0GMRomdt-ElLMW16itwQILQjteI9Hn0DiX5WpOVGapheLw4x74BwqiWB5czpFuZwqCAxKp3UG3sT4Vg3lmaKydpY-80TGByM1RkTQ44FmWLUM-E1JQ1rVbhLQajVo4-h5uZBEt-1C5xGNv0bAAA9LKaYu0B0q7tlJL5QLI_QBU2zFApy21JvmpklVtuKNKFP8MIMtPiTml9Ak6jA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/97d21bb84f.mp4?token=CXV2xQCsN9SWdM7kJX58VMdVt8rMkRdi01-OR8VvMa3DoMNglfpLmqKqlH0aalrHIXruK9pgTACLkUpc6FGv-MsyweWqYyKXMD9ppI0q_mPwrh59RjK4HyFvPavVRqmi6AyPrN0GMRomdt-ElLMW16itwQILQjteI9Hn0DiX5WpOVGapheLw4x74BwqiWB5czpFuZwqCAxKp3UG3sT4Vg3lmaKydpY-80TGByM1RkTQ44FmWLUM-E1JQ1rVbhLQajVo4-h5uZBEt-1C5xGNv0bAAA9LKaYu0B0q7tlJL5QLI_QBU2zFApy21JvmpklVtuKNKFP8MIMtPiTml9Ak6jA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
دانیال عیوضی از بازداشتی های دی ماه که مجروح شده و از طریق ترکیه خودشو به فرانسه و سپس آمریکا رسوند تو صحن سازمان ملل در مقابل نماینده های جمهوری اسلامی بدین شکل سخنرانی کرد : تو دی ماه مردم خیابون‌هارو از جمعیت پر کرده بودن، اما با گلوله به مردم حمله کردن، ده‌ها هزار نفر به قتل رسیدن، مردم ایران هیچ مشکلی با بقیه کشورها و آمریکا و اسرائیل ندارن، ولی جمهوری اسلامی ایرانیارو بدبخت کرده، به محض اینکه دانیال اسم رضا پهلوی رو به عنوان رهبر دوران گذار آورد، هیئت ایرانی اعتراض کرد که خلاف قوانین جلسه هست، اما رئیس جلسه گفت حرفای دانیال هیچ مشکلی نداره.
✅
@AloNews</div>
<div class="tg-footer">👁️ 41.3K · <a href="https://t.me/alonews/148963" target="_blank">📅 17:15 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-148962">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">👈
محسن رضایی: در جلسه مشترک با رئیس جمهور قرار شد آقای عراقچی طی سفر به نیویورک شروط ایران را به واسطه‌ها ابلاغ کنند
✅
@AloNews</div>
<div class="tg-footer">👁️ 37K · <a href="https://t.me/alonews/148962" target="_blank">📅 17:13 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-148961">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">👈
ادعای محسن رضایی: برای اولین بار موشک ضدناوشکن روی ناوهواپیمابر جورج واشنگتن منفجر کردیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 35.8K · <a href="https://t.me/alonews/148961" target="_blank">📅 17:12 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-148960">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">👈
ادعای محسن رضایی: برای اولین بار موشک ضدناوشکن روی ناوهواپیمابر جورج واشنگتن منفجر کردیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 37.3K · <a href="https://t.me/alonews/148960" target="_blank">📅 17:10 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-148959">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">👈
فیلد مارشال رضایی: ترامپ ایران را به قدرت چهارم جهان تبدیل کرد
🔴
پ.ن: گویا فیلد مارشال از وضع مردم بیخبره
✅
@AloNews</div>
<div class="tg-footer">👁️ 38.3K · <a href="https://t.me/alonews/148959" target="_blank">📅 17:06 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-148958">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">👈
فیلد مارشال محسن رضایی: ترامپ و نتانیاهو جان سالم به در نخواهند برد
✅
@AloNews</div>
<div class="tg-footer">👁️ 38.3K · <a href="https://t.me/alonews/148958" target="_blank">📅 17:02 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-148957">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">👈
فیلد مارشال محسن رضایی: ترامپ و نتانیاهو جان سالم به در نخواهند برد
✅
@AloNews</div>
<div class="tg-footer">👁️ 39.2K · <a href="https://t.me/alonews/148957" target="_blank">📅 16:58 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-148956">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TYl4BTcYK1a3Fv3d4fVgG-w5XXaJfHm2ROtMGbsv0Nkjx-sCoBpwAcvgqVgi77D-DVqtp5OXwNGcMy_ZA8rTOFBMm0niQaw13LyFymyA57NQDbDdsTBtxKZtN_rTGxqWu8zFboh-7TjJAQJtVxf6CGkwOxZS627Qx-g_9ilg4Oi_I5lrnJ8tKtjT5TwJpFn1wqNFUUNAmuhv-lLRMg3-5lcglFGAFrxbDgRHQkpymFS8WA4XOWZguh8lruELTkU5vYfXb_f_w_lB2pRyuYwwbI5hr1Qwh_Q1GTrOhv7l6p_GgS_4re0An52cUSjMelwfKNsq41sIh2eY_INMAlle5w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
دبیر شورای اطلاع‌رسانی دولت:
دیدار عراقچی با ویتکاف مجوز دارد
🔴
هیات ایرانی با هماهنگی نهادهای مسئول و در سازوکارهای نهادی کشور به نیویورک رفته
🔴
همه برنامه ها در چارچوب تصمیمات اتخاذ شده در تهران، صورت می گیرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 39.8K · <a href="https://t.me/alonews/148956" target="_blank">📅 16:53 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-148955">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/peqB4wwA0_BAK3QJGB4n4omLNKh2GRxgwe1K39lcPF_h4JwiwMl_pOVTCELUkJ2McIQAP9bRKNlf4mR11zrYI6ZfTS-ge1ZgLQtWl0m9KR4hXE4gY31X-qxNX-JPNgQaXx6ERUAUynVxhmtu1lt9a3nnCFRPPYIn8XX0ZtPVkGaTlHUso_i7f22v3H0cKaeNT3unl07Uil4MtRusQBETYFbRPmW1flaMRScKCbttPdSzBp0dRwkIsXcVbdX9oeHmZUYi9HFImb4uD2Zw62_17dZyhq3itO_Fgkyyu2qxnuxS3mWfK6iOBvTPYw3QyhsLoZCvAIBx34QagisNpWzIpg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
قیمت جهانی نفت برنت از ۱۰۰ دلار عبور کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 38.8K · <a href="https://t.me/alonews/148955" target="_blank">📅 16:49 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-148953">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/q4UNNBJ4h5Z2jCe80KiR9jLYmBa4xS1X7F8G7iVrCPpAi7VFYIV5hEwF7DldWDDueBc5xfjplJkcUBFeHpbIQxkYmJjmWiRMQ0WDTLTOQyIQWt5w3LjgNeQkvDyljqQeDEgQslP_W49CpblUMbs5QfEwxMAVavHwBhnX0JSgGOjz64bDF6MK0ApJTqVKmnMutYtQrEpwNlEGCw31Dd8eZh2LkWv0E6-WJY_UY-VivmYiww6syhfzXnGz6kvSYfCmEFymLPLxeMFfSJ6Ux9_zm0FJ8dtvY0zA9G5IvEzry-DpDy3Isx40_DUnXLGiwRdfQlploq8vur6VS5PVbl14mw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/60ade90416.mp4?token=LaC-iFb164rGtbOWpQtsQAz_BMlEHFmtDTaUu4o5gDTpVTKXHkHMcM7xUJ4NLrrDCJ59cq2v043mpdQYZd43MWUq_iJcehKqL2tmwpQDx6arRgWts9rAOcrIxwatNvsKS2StZ75m9fjNbfXhwUME93CPXmKxwhOXEkkiZOl3QjcMWh2AGQh7ZhWqoW_ov6z45o1U5kO8OmZfbmNWf4toVXJT_aJ4y9NmAEuHo8ly96YLXPVQW_Y--4W1GH1IYvZ_lrZ6avxogaTdqFc0dJGqAcSoOGNVdL5OcpAqqRrnjuVolli2f4FRi35sfWYNLqRlAoyxrmrqIwMsO_yG2TPCqQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/60ade90416.mp4?token=LaC-iFb164rGtbOWpQtsQAz_BMlEHFmtDTaUu4o5gDTpVTKXHkHMcM7xUJ4NLrrDCJ59cq2v043mpdQYZd43MWUq_iJcehKqL2tmwpQDx6arRgWts9rAOcrIxwatNvsKS2StZ75m9fjNbfXhwUME93CPXmKxwhOXEkkiZOl3QjcMWh2AGQh7ZhWqoW_ov6z45o1U5kO8OmZfbmNWf4toVXJT_aJ4y9NmAEuHo8ly96YLXPVQW_Y--4W1GH1IYvZ_lrZ6avxogaTdqFc0dJGqAcSoOGNVdL5OcpAqqRrnjuVolli2f4FRi35sfWYNLqRlAoyxrmrqIwMsO_yG2TPCqQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
یک هواپیمای آموزشی مدل "هاوک تی۲" متعلق به نیروی هوایی سلطنتی بریتانیا، امروز اندکی پس از برخاستن از پایگاه هوایی "وللی" در جزیره انگلسی، سقوط کرد.
🔴
هر دو خلبان با موفقیت از هواپیما خارج شدند و جان سالم به در بردند
✅
@AloNews</div>
<div class="tg-footer">👁️ 39.8K · <a href="https://t.me/alonews/148953" target="_blank">📅 16:41 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-148952">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">👈
این شخص غلامرضا قاسمیان است کسی که یه مکانی درست کرده به نام پناهگاه زنان خیابانی که اونجا زنان رو جمع میکنه تا خدمات جنسی بدن! و اسمشم گذاشته شلتر
🔴
قاسمیان در این ویدیو میگه خودمم اینجا میرم و میام
🔴
صدا و سیما هم یه هفته هست اینو هی میاره تو آنتن زنده…</div>
<div class="tg-footer">👁️ 40.8K · <a href="https://t.me/alonews/148952" target="_blank">📅 16:33 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-148951">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">👈
طالبان و پاکستان درگیر شدند
🔴
روزنامۀ ۸صبح افغانستان از درگیری طالبان و نیروهای پاکستانی در مرز دو کشور در ولایت پکتیا خبر داد.
🔴
این درگیری چند ساعته ادامه داشت و به‌گفتۀ منابع، شماری از گلوله‌های خمپاره به خانه‌های مردم اصابت کرده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 41.8K · <a href="https://t.me/alonews/148951" target="_blank">📅 16:32 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-148950">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/q-kgqrjrBRmkdehNnzFl2nNoM7DO1FyFQUn0pZMtQi7dBbMGmkTZ0Tg2xVbW97gjEa4lD74MH2DEylytpcQv5M5zZaUhGXcp0c-6oyWBX7YMw0ehpDPpg9k-PNiHErCaD9FWmt2dU9UEqtQcAbg0VXEJ14sifWALEpxqffanOlVa0mFIr75SOmieHKlFgdY4fD2Y-7OZ_Ex-CfMTAAK86ykyr-uKSlMpaIBiGype4JjACBtaVYkzrkRnvrwPjRGJWi3g9qKQ_aLDWTx8p8QaX7R_xjleA0Yfio2AEbdgKcptHD3G8_76O_udCaByWrDym8vY1kfRAAPd3FHv4yogQg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
توییت جدید اسرائیل به فارسی
✅
@AloNews</div>
<div class="tg-footer">👁️ 47.1K · <a href="https://t.me/alonews/148950" target="_blank">📅 16:21 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-148949">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/H6Jr3LPETeYApytZDxedLKFTbXJeTBqhf234tC_X2ntfPiy8tdg1EfJqnl5f9NdiNVRtpJgiUAdmMfG8X2H7_lPNVJBQIXvjkHUtiQ1_lNOIeAhiHcGYUdUAUIvDlZA_xFWTgk1sf3VVMV1JTUV9qa5CuUOZibPI3vu8U6HYCFRzVL6qgGOh3qSpTaC9iAOTC_-msIyrk-LYnaHz1wjQIkooNBQ69zJ4TEaxkb-IU3sJkYrMP2GUDJqKULf8TscsRHrduQ5seGjKXgluXy-P5OfQGhxiAvuqnJb0YFUmueqi9i2r1DoM7dkmDQD0dV4qDNcOzUQsoKXq9jNqXJ0LhQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
پنج تانکر بزرگ حامل نفت خام در حال عبور از تنگه هرمز از طریق مسیر عمان مشاهده شدند و در نتیجه، هدف قرار گرفتن این کشتی‌ها منجر به نشت نفت در آب‌ها شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 45.1K · <a href="https://t.me/alonews/148949" target="_blank">📅 16:20 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-148948">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">👈
کانال 13 اسرائیل: نتانیاهو صبح امروز یک جلسه امنیتی اضطراری سطح بالا با تمام دستگاه های امنیتی و نظامی در مورد ایران برگزار کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 45.1K · <a href="https://t.me/alonews/148948" target="_blank">📅 16:13 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-148947">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dcdfbf7d1d.mp4?token=kRtZqWy0-Zj2CcmxN658JurZmvvYMYTXQzhuy8ILY5TTjve5v0qxh5hccQNGa8aJbd2xY1_g0VeG8_aQxqSQ3vdhmo7QtvP0od3mlGwsNnoxtedrIITYpJqrKjKnVzE_zYzlugoKaEwAQ_2eBesctixlX9KWlsN8C3tkgjDH-CECRzx2X7phfq0Y0skgEQChuZRdhQrf7lEk5ZbY1xrVUQlcNunD9EZv72ai6Y_XeiikT4HGkipDzVJRaHz6uiFBSxlu0HbPBH0ZpFLXixoONlzMCvCNCFZJpdCuGORcOfLVD-b42rwozBrJXKU8tqc1KvTzW4eZ35WE5AnMS6ETC4u-8d8e7A_Rh6ucHmhTJ3nmUrOHLSYI-NVFTH3zdJMq9OT6r9VhBTGXwZ9sEcS8NobxQQ9foo1JY4nhMRupAndVP6SLs3BMkRtkT_wswT-EF4UJhI7vrNdhgp9moH68hL0dlfb675PG2ym4LQ5JtttihJPUP3VfNEL6-1eiASBxOKoCKYkca5bDjBGQ3B-sQZagN2IullVaq0odtIRTf96ByKca37NP29_4MZOUwj6k-2fXdS5ZQ3hOkc518b8d6XUMB_LHnXE66kiEipjyk4jlBt7HTkkaiuoOEriY0X-KF-l1G5zr-qxqs-rsg43yx7fuuRLsY9YIJTJi3BslFKc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dcdfbf7d1d.mp4?token=kRtZqWy0-Zj2CcmxN658JurZmvvYMYTXQzhuy8ILY5TTjve5v0qxh5hccQNGa8aJbd2xY1_g0VeG8_aQxqSQ3vdhmo7QtvP0od3mlGwsNnoxtedrIITYpJqrKjKnVzE_zYzlugoKaEwAQ_2eBesctixlX9KWlsN8C3tkgjDH-CECRzx2X7phfq0Y0skgEQChuZRdhQrf7lEk5ZbY1xrVUQlcNunD9EZv72ai6Y_XeiikT4HGkipDzVJRaHz6uiFBSxlu0HbPBH0ZpFLXixoONlzMCvCNCFZJpdCuGORcOfLVD-b42rwozBrJXKU8tqc1KvTzW4eZ35WE5AnMS6ETC4u-8d8e7A_Rh6ucHmhTJ3nmUrOHLSYI-NVFTH3zdJMq9OT6r9VhBTGXwZ9sEcS8NobxQQ9foo1JY4nhMRupAndVP6SLs3BMkRtkT_wswT-EF4UJhI7vrNdhgp9moH68hL0dlfb675PG2ym4LQ5JtttihJPUP3VfNEL6-1eiASBxOKoCKYkca5bDjBGQ3B-sQZagN2IullVaq0odtIRTf96ByKca37NP29_4MZOUwj6k-2fXdS5ZQ3hOkc518b8d6XUMB_LHnXE66kiEipjyk4jlBt7HTkkaiuoOEriY0X-KF-l1G5zr-qxqs-rsg43yx7fuuRLsY9YIJTJi3BslFKc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
نتانیاهو، نخست‌وزیر اسرائیل، درباره هوش مصنوعی: من یک هدف را تعیین می‌کنم: در عرض پنج سال، ما به سومین کشور قدرتمند در زمینه هوش مصنوعی تبدیل خواهیم شد.
🔴
ایالات متحده و چین در این زمینه پیشرو هستند – کشورهایی کوچک نیستند – اما من می‌خواهم اسرائیل نیز به این جمع بپیوندد و با کمک خداوند، این اتفاق خواهد افتاد و ما به سومین قدرت در این حوزه تبدیل خواهیم شد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 46.1K · <a href="https://t.me/alonews/148947" target="_blank">📅 16:10 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-148946">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">👈
عمان هم به تحریم هوایی علیه ایران پیوست
✅
@AloNews</div>
<div class="tg-footer">👁️ 47.1K · <a href="https://t.me/alonews/148946" target="_blank">📅 15:56 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-148945">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">👈
فارس : عراقچی اجازه دیدار با ویتکاف را نداشت و باید عذرخواهی کند
✅
@AloNews</div>
<div class="tg-footer">👁️ 47.1K · <a href="https://t.me/alonews/148945" target="_blank">📅 15:54 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-148944">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/26f3ab76f2.mp4?token=jCimfKRvU7TjdGWg7VDP8iUWPY3_K-rwYuJtWnuVjhvcbCc6xNMBhGx6EbbC6LiXft4oTq3BHef7QR9lYV29M2liyhmzd2reLrbRXkQh9qyGAGxsafmdX88KFh-mhRHK7iEOuX-OHiRQuwFrzmHaUwRwfHK2SwRwJvmylxNeujRP5FTXcFu6cIRkCmRzIqgcZ0ZCLJbE8zSgos99OlH9t3momu4zkpA5s36WSqfSC-b7ocSdnyJzVqRPbW3NPAV57gFqa3fGnelsEbAnCpI4Uste8uQf9myeJnuWzMht98xiToAz-UQZC23smhU9yafYaJ78-wFiXtDNECmO8HWMxA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/26f3ab76f2.mp4?token=jCimfKRvU7TjdGWg7VDP8iUWPY3_K-rwYuJtWnuVjhvcbCc6xNMBhGx6EbbC6LiXft4oTq3BHef7QR9lYV29M2liyhmzd2reLrbRXkQh9qyGAGxsafmdX88KFh-mhRHK7iEOuX-OHiRQuwFrzmHaUwRwfHK2SwRwJvmylxNeujRP5FTXcFu6cIRkCmRzIqgcZ0ZCLJbE8zSgos99OlH9t3momu4zkpA5s36WSqfSC-b7ocSdnyJzVqRPbW3NPAV57gFqa3fGnelsEbAnCpI4Uste8uQf9myeJnuWzMht98xiToAz-UQZC23smhU9yafYaJ78-wFiXtDNECmO8HWMxA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
عمان هم به تحریم هوایی علیه ایران پیوست
✅
@AloNews</div>
<div class="tg-footer">👁️ 47.9K · <a href="https://t.me/alonews/148944" target="_blank">📅 15:51 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-148943">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">🔴
فوری / سازمان عملیات تجارت دریایی بریتانیا: گزارشی درباره یک حادثه در داخل تنگه هرمز دریافت کردیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 47.9K · <a href="https://t.me/alonews/148943" target="_blank">📅 15:49 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-148942">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromالو توئیت | AloTweet</strong></div>
<div class="tg-text">چطور برای آیفون 18تحریم نیستیم اما برای واردات دارو تحریمیم؟
[
@AloTweet
]</div>
<div class="tg-footer">👁️ 46.9K · <a href="https://t.me/alonews/148942" target="_blank">📅 15:46 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-148941">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GSoIhfgKhyxebz8YoBREiGaii63mKHKdQh0-eOLhAe2NZMCU689B0GGeJWQUQTR4Im0jIE6OPUOwJoTqUElfU5zzVku7-BHBe_OPH-BxpIEes59m-pdP9jVcnt8bA0Rega3-IQYAleeitNwpvU0BK6Jw9W-Ywi12w4L1hkkccEqF9GaMuK9-29nJikBOIas92TZlhr6vxdSfpe-VVyOAu6D4YYtXG687pITDNUhJRIldlBNhHTMF6qh8ehJ0uJzSLH-nPuwnwRpE4zjgNEloLC2bkE-Fk8YZfmo1FUtU10ftgeY0fMG-o6nK8ZfYVM4cKWHEyNHzdpwhAY_ikl63Og.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
مجتبی زارعی، عضو کمیسیون امنیت ملی مجلس: عراقچی مجوز مذاکره با ویتکاف را دارد
✅
@AloNews</div>
<div class="tg-footer">👁️ 47.9K · <a href="https://t.me/alonews/148941" target="_blank">📅 15:46 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-148940">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HZrt_OClXP0wDGph6hfKErUV3ELVPQ94Tswq2eeVEgWN7TRAik8tO6HvVij0QLuev2wSPdCQUuyYqB8AA4VmeuVD8EWwre1LSxQhvmGSxtKX3sm5wwrPAU2AraytYQSd33c2z0htBWPCrz5muwTKhtZVXCggk5geaWZkxzE-n9n2gByb1mRop4hC2kIF4XjwJ3EcTgGRR4JAQ8AtGcfwL2ye1onEEDe06ayph9iCeFPQ06r4ooC-aXEbgQEbAJMAbnDlhtszZjnYPNw27GxQ0x8bbVHhZ-KPyPzVEDsXVMLIXR5HIYGJAZefbuUCxnyUA9UNFhtk-y3vns_V0tdimQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
آیفون ۱۸ تنها دقایقی بعد از موجود شدن در دو سایت بزرگ تکنولایف و دیجی کالا اتمام موجودی شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 50K · <a href="https://t.me/alonews/148940" target="_blank">📅 15:35 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-148939">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">🔴
فوری / سازمان عملیات تجارت دریایی بریتانیا: گزارشی درباره یک حادثه در داخل تنگه هرمز دریافت کردیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 49K · <a href="https://t.me/alonews/148939" target="_blank">📅 15:31 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-148938">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nVpMBLNLEqVGDwjwsJtReivpGevJmCwLubUCB902N4RkuGM5xNcdRbrPzSxdDii9WO8q92-KnEPbYti9EnhhS-rJ_H7whHBQw9vE2vAXKXf6ryy4tOhgzJc4BZAGPhns8gltUbfE3bYhr5m_RpH4fDYDuyyYZfSdw71Xfeo8vbBMwBGj-_bUB122ZgfKkTKIzkv5LgYzBWzDYDozRt7LjM59TIKecT51_3Q9oF_6kLwUtkTuwC3v4pC8obvhxQ20uehTqmtf6wN0bsTRx9d6bfFxAU_gzgeMU3m0ek6KnV9dQQkCMaTFzlg3qJZEMH5_pMVgkBE5cRhBTYb1VNAqYA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
نوسان قیمت نفت برنت در ۲۴ ساعت گذشته
✅
@AloNews</div>
<div class="tg-footer">👁️ 50K · <a href="https://t.me/alonews/148938" target="_blank">📅 15:30 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-148937">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">👈
مارک کارنی، نخست‌وزیر کانادا، درباره ایران: «تهدید ایران یکی از بزرگ‌ترین تهدیدها در جهان و در دنیای مدرن است.
🔴
برای مثال، همچنان تهدیدی موجودیتی علیه اسرائیل از سوی ایران و متحدانش وجود دارد.
🔴
این تهدید همچنان وجود دارد؛ قابل قبول نیست و هیچ‌گاه قابل قبول نبوده است.»
✅
@AloNews</div>
<div class="tg-footer">👁️ 52.1K · <a href="https://t.me/alonews/148937" target="_blank">📅 15:16 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-148936">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/90e681aa54.mp4?token=do_MVMEyGfdxsTrMn9E3SuosBEcJQTgtukZxaCvuZVj6K82-0t4HAHV1K4EBg-kkQpXwBH03eYzY6CRHzJR5LwNPZyzsVWh9QlOWexXY4TZTVhQDH40bTtVhxhBkUk74qkoafyaVkwu2J2EDXA4qRlgJM0jIChDXZvrfT1YKpGibrs8PId5Rs5bfGKMpkPKUd1nFRc28sCO46x2Vyl1w1B9MUoHQ2AVVBkKjhEaEEbI7g_uOkonSUwvbdAZ07C2TdK1-L8196Hlfju5CxmlMbmr9aYRAbmyoSKHkeA5L1uJfzhWb8RQCZ1yzjKh2FA9QPC8eAMfcTJNHpA736tNI-g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/90e681aa54.mp4?token=do_MVMEyGfdxsTrMn9E3SuosBEcJQTgtukZxaCvuZVj6K82-0t4HAHV1K4EBg-kkQpXwBH03eYzY6CRHzJR5LwNPZyzsVWh9QlOWexXY4TZTVhQDH40bTtVhxhBkUk74qkoafyaVkwu2J2EDXA4qRlgJM0jIChDXZvrfT1YKpGibrs8PId5Rs5bfGKMpkPKUd1nFRc28sCO46x2Vyl1w1B9MUoHQ2AVVBkKjhEaEEbI7g_uOkonSUwvbdAZ07C2TdK1-L8196Hlfju5CxmlMbmr9aYRAbmyoSKHkeA5L1uJfzhWb8RQCZ1yzjKh2FA9QPC8eAMfcTJNHpA736tNI-g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
خبرنگار: «آیا فکر می‌کنید ترامپ با بیان اینکه در حال بررسی گزینه نابودی کامل ایران است، زیاده‌روی می‌کند؟ آیا چنین اظهاراتی به روند صلح کمک می‌کند؟»
🔴
مارک کارنی: «اکنون جنگ در جریان است. او با زبان جنگ صحبت می‌کند.»
✅
@AloNews</div>
<div class="tg-footer">👁️ 53.4K · <a href="https://t.me/alonews/148936" target="_blank">📅 15:06 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-148935">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/947a8913ac.mp4?token=W-oeRcPbpkdQnMxnHRTIe472CeuUjOr7UEO_0EXctHAyhNQG7uvCHB5Nhd2rvWjdiJffYjNmMj7uZOtrw0isgRimIxaXVf3lxVYV-PFrsFP-2pdsKqdVZbRFCp-ugXFCAnqHrJJWfjmubOTdP3yWc77MD8B0tIQ8FkB4i9Ha2fiiO85r7tmxgJlNjp3qz2jSdwab0_diOkuy_IA1NBe-di4gzo6ZW3bch9-Hu8FwlN09yuE3ExIQOk5RuBLpXRC81aEwbrwGJYVNYRbjN4UX51sICSsCk_cNEtL_vY4fsQQbIe-8Pp_9abhxaMrq5lIEmh63xaMprWcA8YYDFcRTQQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/947a8913ac.mp4?token=W-oeRcPbpkdQnMxnHRTIe472CeuUjOr7UEO_0EXctHAyhNQG7uvCHB5Nhd2rvWjdiJffYjNmMj7uZOtrw0isgRimIxaXVf3lxVYV-PFrsFP-2pdsKqdVZbRFCp-ugXFCAnqHrJJWfjmubOTdP3yWc77MD8B0tIQ8FkB4i9Ha2fiiO85r7tmxgJlNjp3qz2jSdwab0_diOkuy_IA1NBe-di4gzo6ZW3bch9-Hu8FwlN09yuE3ExIQOk5RuBLpXRC81aEwbrwGJYVNYRbjN4UX51sICSsCk_cNEtL_vY4fsQQbIe-8Pp_9abhxaMrq5lIEmh63xaMprWcA8YYDFcRTQQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
خبرنگار: «آیا از زمان حضور در نیویورک فرصت داشته‌اید با دونالد ترامپ یا یکی از اعضای دولت آمریکا گفت‌وگو کنید؟»
🔴
مارک کارنی: «وقتی ۱۶۰ رهبر به نیویورک می‌آیند، به نظرم ارزشمندتر این است که با افرادی دیدار کنید که معمولاً فرصت دیدنشان را ندارید.»
✅
@AloNews</div>
<div class="tg-footer">👁️ 55.1K · <a href="https://t.me/alonews/148935" target="_blank">📅 14:56 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-148934">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">👈
اسماعیل کوثری، نماینده مجلس: شان پزشکیان خیلی بالاتر از اینه که بخواد با ترامپ روبه‌رو بشه
✅
@AloNews</div>
<div class="tg-footer">👁️ 55.6K · <a href="https://t.me/alonews/148934" target="_blank">📅 14:47 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-148933">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">👈
رسانه‌های پاکستانی:امروز صبح، 8 فروند پهپاد از افغانستان وارد حریم هوایی پاکستان شدند و همگی آن‌ها مورد شناسایی و واکنش قرار گرفتند
✅
@AloNews</div>
<div class="tg-footer">👁️ 57.2K · <a href="https://t.me/alonews/148933" target="_blank">📅 14:39 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-148932">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/g3FFxSZaY4Ev5G8WZD_WtG9rqOxCa9cUQBqEJ2wBtqOZ78fGN04Yy08Z662D4k818JlffjD23nBjFsuJ-3ZM1UeLnuEcmDgHGWzd43ZaaieYGHv-dQBzWKcsV-mWBTFt_JeaTuRIC6dDKsdBZDkRbJjSMTPdPeBOkmUu2XX6wugatcw_UeE2Y8V30oZtL8x2q5LWJ6Ks2giW5w6AyCEC4fAX1s4HADF819o-uTwA-ZTxQvQ-8F3mHj78fO7_80DUtSmiB5bQEov0vBpGdDFu16KyuH7zklo7XxE5pT3KGjweNoCZZ5SlKcs_2bobhKuwk40-urlcjdxNC4C4dg5Qlg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
یک هواپیمای ایرانی در حال پرواز از تهران به امارات متحده عربی، علی‌رغم تحریم‌های اعمال‌شده توسط آمریکا
✅
@AloNews</div>
<div class="tg-footer">👁️ 59.2K · <a href="https://t.me/alonews/148932" target="_blank">📅 14:32 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-148931">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">👈
یک مقام حوثی: «اگر عربستان سعودی از حمایت آمریکا برخوردار شود، تمام منافع آمریکا در منطقه را هدف قرار خواهیم داد.»
✅
@AloNews</div>
<div class="tg-footer">👁️ 57.2K · <a href="https://t.me/alonews/148931" target="_blank">📅 14:23 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-148930">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">👈
تام باراک، سفیر آمریکا در ترکیه:
اگر به اتفاقاتی که در دو سال گذشته در سوریه رخ داده فکر کنید، هیچ‌کس نمی‌توانست تصور کند چنین تحولاتی در تاریخ خاورمیانه ممکن باشد.
🔴
من واقعاً به همه آنها افتخار می‌کنم و به آینده امیدوارم
✅
@AloNews</div>
<div class="tg-footer">👁️ 58.2K · <a href="https://t.me/alonews/148930" target="_blank">📅 14:17 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-148929">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AUBSETazldKRNA4rbSdLgfwiSuaHGT1V_BoVFxcYkT7YVg_lJYnyKUfCXvkX0jty-0TQSnJVpBh3kB6jSg8zs7lwsUmxiYzh3VD7gGs2w39AFNB3nZnrT9MANRuGxhWIg4FVTys_MW5FGK_Vk97agvTLWe2M7jgOUg9XdDXKqkglE2z97JG4CCol4zFyPXqmuhPpUr_zKsRin0c8kvXVkNRFLTrUBQJqNueh3TD8GvD45YlsXp2QD3SyuIsAZTKxHXCqwSIEoVfe3-BoU0XJlJcSvzZvJjeMpvCHq3k_2Nlhv4malJor6uMVeyD_IKWB4dPWvwHbiyMVCJ33mIvwDg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
احمد الشرع، رئیس‌جمهور سوریه، در نیویورک با ولودیمیر زلنسکی، رئیس‌جمهور اوکراین، دیدار کرد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 58.2K · <a href="https://t.me/alonews/148929" target="_blank">📅 14:14 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-148928">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">👈
آسوشیتدپرس به نقل از منابع آگاه: مستشاران سپاه در جریان تصرف بخش‌هایی از سواحل دریای سرخ به دست حوثی‌ها در منطقه حضور داشتن و به هدایت عملیات حوثی‌ها کمک کردن
✅
@AloNews</div>
<div class="tg-footer">👁️ 57.7K · <a href="https://t.me/alonews/148928" target="_blank">📅 14:11 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-148927">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">👈
بنیامین نتانیاهو، نخست‌وزیر و یسرائیل کاتس، وزیر جنگ رژیم اسرائیل با انتشار بیانیه‌ای مشترک اعلام کردند محمود ابوعلوان، «مسئول مالی حماس» را در یک حمله هوایی به خان‌یونس در نوار غزه ترور کردند
✅
@AloNews</div>
<div class="tg-footer">👁️ 60.2K · <a href="https://t.me/alonews/148927" target="_blank">📅 14:05 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-148926">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vjMimYiMaV4Y4HdMwkUyQfyPYKU0iqVk-0ANL5938or90WrexRUhDl7OG5DfLzvc8iQvH63q0IjcsGGK8klhsyu7RPQaEnAXfHw0qdDYAlWLxfwk6ezg7cVryLQGOnCeCHhD0HM3HWXSsARjk3qYVDONdfC0XYz7XPFH3986f-5-V4yRH1CrXOteF2jx6SADp1zHQRmUv0n6CaCYaeGmZA7KLjtDkxv_H30OJuvF_FYPJH-spXuG-4OOHTjR_2iro5eQ6236YD_j4qwHzWlHBwjn7FilmeuFtgqYcFkPPXOCBL24yAoUTFLs-6OMoX0qhEC3DfhxaUHIv2AOkGOTzw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
پزشکیان فرا رسیدن روز ملی عربستان را تبریک گفت
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.3K · <a href="https://t.me/alonews/148926" target="_blank">📅 13:47 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-148925">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">👈
افزایش میلیادری قیمت ۴ محصول ایران‌خودرو
🔴
قیمت ۴ محصول ایران‌خودرو امروز حداقل ۷۸۰ میلیون افزایش یافت؛ میزان افزایش قیمت هایما 7X به بیش‌از یک میلیارد و ۲۰۰ میلیون تومان رسیده است.
🔴
این افزایش قیمت خودرو درحالی اعلام شده که پیش‌از این ایران‌خودرو توقف تولید محصولات خانوادهٔ هایما را اعلام کرده بود
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.3K · <a href="https://t.me/alonews/148925" target="_blank">📅 13:39 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-148924">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">👈
آکسیوس: شورای صلح به ریاست ترامپ طرح بازسازی غزه را به ارزش ۲.۴۵ میلیارد دلار اعلام می‌کند
✅
@AloNews</div>
<div class="tg-footer">👁️ 64.3K · <a href="https://t.me/alonews/148924" target="_blank">📅 13:32 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-148923">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hitsj-UQcuOMd39vWOJmiqKVzrNxdAp5e2K6MFDxQlNvf1OZLegXVgXFCJMO_BVi2roNiEFC0k3mNqt4CEIzJu15NaK6On1v4srsq6JdT7NnQ8fBrBOF3gp0zgVXvC_6b3LdR9_gWds5Oq3vdJ6WEVxzihBymw3B0SJKYOHpIQgWEeN0xHfz1PThNIMCkY8q-qh5o0T2xF9zQJEcV6j1RUWjMijZbTD_vsdEzVKZckNgAlZJvTjy1Wiy0s5HQlMkkxbmVXuy7S-0DbGg391_978sqpmjAQc3F0f-95AP0y9M0jhbaHMm7HraYUYXjaufGC_PIn5fP-PuUJbquK5J-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ستون‌نویس بلومبرگ: عربستان سعودی بارگیری نفت خام در پایانه ینبع جنوبی در دریای سرخ، یکی از مراکز مهم صادرات نفت این کشور، را از سر گرفته است.
🔴
تصاویر ماهواره‌ای مورد استناد مربوط به ۲۱ سپتامبر هستند
✅
@AloNews</div>
<div class="tg-footer">👁️ 65.3K · <a href="https://t.me/alonews/148923" target="_blank">📅 13:24 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-148922">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">👈
فایننشال تایمز: برای نخستین بار، هزینه اجاره یک نفتکش غول‌ پیکر در مسیرهای میان خاورمیانه و آسیا، از روزانه ۱.۲ میلیون دلار فراتر رفته
🔴
حدود ۱۵ درصد از ناوگان جهانی نفتکش‌ها در سواحل عمان منتظر هستند
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.3K · <a href="https://t.me/alonews/148922" target="_blank">📅 13:17 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-148921">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">👈
کرملین: «ولادیمیر پوتین آماده دیدار با دونالد ترامپ است، اما برگزاری یک نشست بدون انجام هماهنگی و آماده‌سازی‌های قبلی، اتلاف وقت خواهد بود.»
✅
@AloNews</div>
<div class="tg-footer">👁️ 64.3K · <a href="https://t.me/alonews/148921" target="_blank">📅 13:14 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-148920">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">👈
هک گسترده اف‌بی‌آی!
🔴
یک گروه هکری با نفوذ به سامانه‌های اداره تحقیقات فدرال آمریکا (FBI)، اطلاعات شخصی هزاران مأمور این نهاد را به دست آورده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 66.4K · <a href="https://t.me/alonews/148920" target="_blank">📅 13:08 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-148919">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">👈
رئیس‌جمهور سوریه
:
«اگر سوریه به مرحله‌ای از ثبات و امنیت برسد، از فعالیت سیاسی کناره‌گیری خواهم کرد، در انتخابات ریاست‌جمهوری آینده نامزد نخواهم شد و قدرت را واگذار خواهم کرد.»
✅
@AloNews</div>
<div class="tg-footer">👁️ 65.4K · <a href="https://t.me/alonews/148919" target="_blank">📅 13:06 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-148918">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">👈
فرودگاه بین‌المللی نجف: پروازهای ورودی و خروجی این فرودگاه، از جمله پروازهای ایران، طبق برنامه‌های اعلام‌شده ادامه دارد و تاکنون دستوری برای توقف آن‌ها صادر نشده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 65.5K · <a href="https://t.me/alonews/148918" target="_blank">📅 12:55 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-148917">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">👈
جنگنده‌های عربستان سعودی مجموعه‌ای از حملات هوایی را علیه دکل‌های مخابراتی در استان الحدیده یمن انجام دادند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 65.3K · <a href="https://t.me/alonews/148917" target="_blank">📅 12:51 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-148916">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">👈
سخنگوی وزارت خارجه قطر: رهبران قطر با ترامپ در مورد پیامد‌های جنگ با ایران گفت‌و‌گو کردند
🔴
خوشحال هستیم که شاهد از سرگیری تعامل میان تهران و ایران هستیم
🔴
تمرکز بر باز نگه داشتن کانال‌های ارتباطی و ادامه تبادل پیام‌ها است
✅
@AloNews</div>
<div class="tg-footer">👁️ 66.3K · <a href="https://t.me/alonews/148916" target="_blank">📅 12:48 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-148915">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">👈
معاون اول پزشکیان : از مردم بابت گرونی‌ها عذر می‌خوام ؛اما در حال حاضر. راهکاری برای حلش وجود نداره
✅
@AloNews</div>
<div class="tg-footer">👁️ 65.3K · <a href="https://t.me/alonews/148915" target="_blank">📅 12:44 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-148914">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AnMr3L3rRiW5pr3ROWrj3DVN3xhgCJE0HvQPiyXMAULJ4YiMo2UI4jhI66XXj9FUZvD6ssy_gQb0BMb3LcnIv2q-o_HeXEzeugEKiSjuNI9JaGTtGuW4MWujjrCabR32ikz_Hieb4C7gIxRGViWJ-iqUwskbFb0ht9ZkHMEosag7LisfjnoBKiwZyB1hsmf1wCpcHImn7oBHlC7RAC4fDtZFB7OOlTlaHZq-qTP4fvdto4_QU1J0g8eURUZQp9qZ98bUm_x837eLUSO8IR1tywynrV3wBkDheZQGKTiDZZ7q43Lkh_cdeWxlDtCcldUQ6RupS6-_hKNKX3zVDsO-pA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
لارنس نورمن: در خصوص هر آنچه عراقچی در نیویورک بر سر آن مذاکره می‌کند، به نظر می‌رسد که او از حمایت نهادهای امنیتی برخوردار است
✅
@AloNews</div>
<div class="tg-footer">👁️ 65.3K · <a href="https://t.me/alonews/148914" target="_blank">📅 12:33 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-148913">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">👈
خبرگزاری فرانسه گزارش داد: یک هواپیمای مسافربری ایرانی با وجود تهدیدهای واشنگتن به اعمال تحریم، در چین فرود آمد
✅
@AloNews</div>
<div class="tg-footer">👁️ 64.3K · <a href="https://t.me/alonews/148913" target="_blank">📅 12:31 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-148912">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Mx4BeWZjppDBN-_XSS1Yg9sXrY22wKbMh12p2iItZAbYC8ktK267JfS4gSkgY-ldQzbZw8kBZ7sRmA4l7_fgE0xuzieNtvPFmq-LyrTk1B20OTdmAXCwVnhrTP1F3S7m1n_ne1XMvPrrC6r-5axQBOoVpKnna_yJqYaBrbgw3rm7qLhAw6MLnbuTVcumZm9sLKtR7YVg8GuXoMhNWm5oNjR2LIyQmt-IttrPBdUiYWReGPTneJXdqx3fxMsXBhGqBSNRWBjzHPQQ-3AwZ-7AYoKppzfB31lU1MGERqCE-y5RAodxOBkqNWV_C3HNkPRJHEXVqMLgBwFe6essPh11_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
خوش چشم: با جنگنده‌هامون میتونیم محاصره هوایی رو بشکونیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 65.3K · <a href="https://t.me/alonews/148912" target="_blank">📅 12:26 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-148911">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/677484de4f.mp4?token=Tk5fjANsZUMmWKiJZ5h648Md3kvCaozipSTG-hruL-MDN3LGU6QTYFxsnR0hIfb9hDdPS-fcBqgp3nI-f2bNEsiRiF_r6fLF6Jt_k5zx8oFGTI3xJmLv26Dmcq3avNZOkBhaog6ZMgpvChaXF2MoaZVMqPGrcVbupf36hZGSh3jpqXBkucFjwNI_fgfBMwLUGaiv774IQBWKBlGugS9eP79tukRfi0bpzriAwztNCMW0uSSCz2lzvJJxO8bDlk1md1pN1os42NpzIEf5y6TJpc5lgrkIRS0O85p6XaKDX_E0CXar5s0wNyjcgIa7mkGkqq7z5mrRzz4zqQtnh3ZP9A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/677484de4f.mp4?token=Tk5fjANsZUMmWKiJZ5h648Md3kvCaozipSTG-hruL-MDN3LGU6QTYFxsnR0hIfb9hDdPS-fcBqgp3nI-f2bNEsiRiF_r6fLF6Jt_k5zx8oFGTI3xJmLv26Dmcq3avNZOkBhaog6ZMgpvChaXF2MoaZVMqPGrcVbupf36hZGSh3jpqXBkucFjwNI_fgfBMwLUGaiv774IQBWKBlGugS9eP79tukRfi0bpzriAwztNCMW0uSSCz2lzvJJxO8bDlk1md1pN1os42NpzIEf5y6TJpc5lgrkIRS0O85p6XaKDX_E0CXar5s0wNyjcgIa7mkGkqq7z5mrRzz4zqQtnh3ZP9A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
برنی سندرز، سناتور آمریکایی: «ما در ایالات متحده باید تمام کمک‌های نظامی به دولت نتانیاهو را متوقف کنیم.»
✅
@AloNews</div>
<div class="tg-footer">👁️ 64.3K · <a href="https://t.me/alonews/148911" target="_blank">📅 12:17 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-148910">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lfotMKjS2QVcompYY_3ekpucYzGvggLq98pwc-707eJlxiv5ajBYPwPAwe7lwBmY_dUz6sLnQ6q6RIMXInGJhXpi83jyJo3juc0G5EgpovkBX4I53zTvez14qBpU9zhRk7NsBYMB3U-7IZCczblMKLubbk7eTzHi1ncPgt8tV5-HMSavEWF8PZ9sPLxvOYVasyEa7bglCyHrVbd8_ozbyyBJXOXa_HVKLgK5h6WkpnvjCkm988d1gOQHiTOX2n24FRuI3pstIQeIX-2ODi9lNTeoicBm735payZc6mxXXo6DhTQPtX2FJEXY4l1RtfQ0zTh41-cKEo6DfuHd1eFQgg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ترامپ بازنشر کرد:«ائتلاف نتانیاهو در تازه‌ترین نظرسنجی انتخابات اسرائیل پیشتاز است.»
✅
@AloNews</div>
<div class="tg-footer">👁️ 66.4K · <a href="https://t.me/alonews/148910" target="_blank">📅 12:14 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-148909">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">👈
پزشکیان امروز چهارشنبه ۱ مهر ۱۴۰۵ ساعت ۱۹:۳۵ در هشتاد و یکمین مجمع عمومی سازمان ملل سخنرانی می‌کند
✅
@AloNews</div>
<div class="tg-footer">👁️ 68.4K · <a href="https://t.me/alonews/148909" target="_blank">📅 11:58 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-148908">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">🔴
فوری / گزارش شلیک ۴ موشک به سمت تنگه هرمز.
✅
@AloNews</div>
<div class="tg-footer">👁️ 69.6K · <a href="https://t.me/alonews/148908" target="_blank">📅 11:47 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-148907">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">👈
رویترز: سقوط یک فروند اف-۱۶ ارتش آمریکا در آلمان هنگام پرواز آموزشی
🔴
یک فروند جنگنده اف-۱۶ ارتش آمریکا در پایگاه نظامی ایالات متحده در غرب آلمان سقوط کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 69.4K · <a href="https://t.me/alonews/148907" target="_blank">📅 11:38 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-148906">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">👈
بنیامین نتانیاهو، نخست‌وزیر اسرائیل:
«نشریه اکونومیست، دولت اسرائیل را — توجه کنید، پس از سه سال جنگ — به‌عنوان یکی از سه اقتصاد پویاتر جهان رتبه‌بندی کرده است. این باورنکردنی است.
🔴
از نظر من، این موضوع کمک الهی نیز هست، اما در عین حال نتیجه سیاست‌گذاری است؛ به‌طور ساده، نتیجه سیاست بازار آزاد.»
✅
@AloNews</div>
<div class="tg-footer">👁️ 69.4K · <a href="https://t.me/alonews/148906" target="_blank">📅 11:34 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-148905">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HQVShZKZ8gejhyGFOJxA8eJKTG2Fy2MzxceP1QjOf0lMlqEkyYQ_aBB06x9ac_0ecr9S_6v_DUG7eXx8PTz5fgcC5VrqtzDbmJigv7gMuWuIt2OsjDZWc-Rj5rmGr3k6IGcx3Z4B0zLiK0uariDak5S4GNW2H2Fsx5N9S6pOQcQ0SCvXfq6VUZmIy7KfrsBOhrbrdVHBZYhVjVhyUbaCymWqkIoTQZqB35l7D37r3cmXJrcHSrrnZmWiQwwtAuZVxFWRC1B2KtE8iOFQRrWL1Ks8rrdr_d7cCW5mAZd2EOwnslmfprU_QNY0MT69JdDZzamVget68vk4BMqZxhILxg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
پرواز سوخت‌رسان‌های آمریکایی در آسمان امارات
✅
@AloNews</div>
<div class="tg-footer">👁️ 66.4K · <a href="https://t.me/alonews/148905" target="_blank">📅 11:28 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-148904">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromالو توئیت | AloTweet</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2bab278fdf.mp4?token=kB-JSSkOxYm59boN4RAoKPlzeEAgjTdXZSKlwo0I0co4QQLui0GxylqiyKA_GE2Wl7hHK_tgNTbh-4CWQLfpQ3zDJOy2bGMfdVBfRwfbev3Eu6Fcabjx-CtWdAebyfyUWnukVsWrVO4U58DrbFDRT2u4trH392zA11Ux7ImXzURd6VYgFvrFEFILe8B91LjyCDBjAKiL0aR0TvolggQyWkW1QXGivL-Z7QSGfO2KTSwM1aPbB6Fh_sS-4Yt1OnfTu94zHE0IjCGouc0xypjLipBv84ih9TRccmfJL_XjAcNN8Qh1jvlIGNlZpknK235g3hYr8vl2PXUR1_02qDbG1w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2bab278fdf.mp4?token=kB-JSSkOxYm59boN4RAoKPlzeEAgjTdXZSKlwo0I0co4QQLui0GxylqiyKA_GE2Wl7hHK_tgNTbh-4CWQLfpQ3zDJOy2bGMfdVBfRwfbev3Eu6Fcabjx-CtWdAebyfyUWnukVsWrVO4U58DrbFDRT2u4trH392zA11Ux7ImXzURd6VYgFvrFEFILe8B91LjyCDBjAKiL0aR0TvolggQyWkW1QXGivL-Z7QSGfO2KTSwM1aPbB6Fh_sS-4Yt1OnfTu94zHE0IjCGouc0xypjLipBv84ih9TRccmfJL_XjAcNN8Qh1jvlIGNlZpknK235g3hYr8vl2PXUR1_02qDbG1w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">توی جشن شروع مدارس کلاس اولی‌ها رو داشتن توی تهران برگزار میکردن که به لطف اداره برق، وسط شعرخونی برقاشون کلا رفت.
[
@AloTweet
]</div>
<div class="tg-footer">👁️ 66.4K · <a href="https://t.me/alonews/148904" target="_blank">📅 11:25 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-148902">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">🚨
طلا و دلار دوباره صعودی شد
‼️
اگه نمیدونی بخری یا بفروشی حتما به اینجا یه سر بزن
👇
https://t.me/+sN8qmnF1jDJlZGRk
https://t.me/+sN8qmnF1jDJlZGRk</div>
<div class="tg-footer">👁️ 63.3K · <a href="https://t.me/alonews/148902" target="_blank">📅 11:22 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-148901">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">👈
افشای جزئیات مکالمه محرمانه داماد ترامپ و بن سلمان
🔴
نشریه آمریکایی نیویورکر فاش کرد که طی یک مکالمه محرمانه میان جرد کوشنر داماد ترامپ و محمد بن سلمان ولی‌عهد عربستان نقشه وی برای کنار زدن محمد بن نایف پسر عمویش از ولایت‌عهدی در سال ۲۰۱۷ بررسی شد.
🔴
در این گزارش به نقل از یک مسئول اطلاعاتی سابق در منطقه آمده است که کوشنر به بن سلمان ابلاغ کرده همه در دولت آمریکا به جز سرویس‌های اطلاعاتی از وی حمایت می‌کنند.
🔴
این پیام به مثابه چراغ سبز واشنگتن خطاب به بن سلمان برای اقدام علیه محمد بن نایف تلقی می‌شد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 67.4K · <a href="https://t.me/alonews/148901" target="_blank">📅 11:17 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-148900">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">👈
سخنگوی کمیسیون امنیت ملی: رهبر جدید می‌توانند درباره سلاح هسته‌ای فتوای جدید بدهند
✅
@AloNews</div>
<div class="tg-footer">👁️ 65.4K · <a href="https://t.me/alonews/148900" target="_blank">📅 11:05 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-148899">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2b004f0a6b.mp4?token=Cx2YXv5rsRdHybvyUSdIp5sWthh-Az5veeAOUgqrYr_aVeIimYLfUXAULgB29u1A-8ZswVzkVJTd41oR12k3iIGq4Nl6W3Hei4NIjB7s0KwQStqfbq5T6D4CS7m-RTTE1393dzJEPP6hHcEO7npKX1q2MpVWg5KeVOPrJMusNdvLEsS3j1fG-w-SobmXEKETx1NXW5k0-_Q-XfW3pC-2Iavs9wZJn2EXj1qF02-TmFvSrbIwArdHl4q6g9E-7g_XsKdTKEw__n31iN-_PkFWovtgGf6eFXys-d2-u6iA0Dx_2P1_NVrpca0iHxvdcxum3hgapm_kpvf4ylPvbtb3HiQDV2piR4hGdAZluLWVdq4UO3mXXKN8sMojRiuC_nFb9Tzta8oYzcQxQRqGyTpVAS2Og_yi5-eeSwuqEY7wS2j0LyqLzmQ1EZSSqvkhtlU_vwDJ46dLRruYFDoksxRHogHNtnvsAAp6ZFdcCw8F7uDzwUeP2cmu9fv8jumek9wZQv-NGUePGKbRJ48Xr4QHiKBByiblwvkbRE8ib6n2wtKXXel0_rvrYtH4G4zHcNa-rIziRPNqfJBiBbcrbI8zLrsSBRV8b4nMdny0dcmS0Bt_3Q4li55lHD8K4r3_pjCcVqeAWIqMZGit0iznMxA4FinR9UozpHLhGEgYaywMZ70" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2b004f0a6b.mp4?token=Cx2YXv5rsRdHybvyUSdIp5sWthh-Az5veeAOUgqrYr_aVeIimYLfUXAULgB29u1A-8ZswVzkVJTd41oR12k3iIGq4Nl6W3Hei4NIjB7s0KwQStqfbq5T6D4CS7m-RTTE1393dzJEPP6hHcEO7npKX1q2MpVWg5KeVOPrJMusNdvLEsS3j1fG-w-SobmXEKETx1NXW5k0-_Q-XfW3pC-2Iavs9wZJn2EXj1qF02-TmFvSrbIwArdHl4q6g9E-7g_XsKdTKEw__n31iN-_PkFWovtgGf6eFXys-d2-u6iA0Dx_2P1_NVrpca0iHxvdcxum3hgapm_kpvf4ylPvbtb3HiQDV2piR4hGdAZluLWVdq4UO3mXXKN8sMojRiuC_nFb9Tzta8oYzcQxQRqGyTpVAS2Og_yi5-eeSwuqEY7wS2j0LyqLzmQ1EZSSqvkhtlU_vwDJ46dLRruYFDoksxRHogHNtnvsAAp6ZFdcCw8F7uDzwUeP2cmu9fv8jumek9wZQv-NGUePGKbRJ48Xr4QHiKBByiblwvkbRE8ib6n2wtKXXel0_rvrYtH4G4zHcNa-rIziRPNqfJBiBbcrbI8zLrsSBRV8b4nMdny0dcmS0Bt_3Q4li55lHD8K4r3_pjCcVqeAWIqMZGit0iznMxA4FinR9UozpHLhGEgYaywMZ70" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
فرود زیبا و نرم هواپیمای حامل پزشکیان مورد توجه دنیا قرار گرفت
✅
@AloNews</div>
<div class="tg-footer">👁️ 67.4K · <a href="https://t.me/alonews/148899" target="_blank">📅 11:00 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-148898">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromAlo Sport الو اسپورت</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WQrbDoUCjeSc5sS05FEIjUn0sh5kddaSOpI9Vi2ZjooJdX_C8fnFZL32zJ976wmNq88hxLbwjm5XD4QXpYmudxAaXxT3TJnVtNj7H2AQyGlMMn4Bq6MwXow_7qzGfOJrgE951huWkN9r9zQXAy3Zoqb5mcIclSMiPM1vnEAmRNpUkIA1Cc9T_dCv_JjnbCJZb-lJtr9XDcg3YqufelFKRqenVd6I84791eS0Ltd3htG0yohPBW1-unQMmXxBXtNoU2VQxLJy8uP2OH9_crQ4_r5I0IoEukWn2z0dvgUefMYcbzgvfNCjYukT__X5LDezYQvWFrRbllA_B8Xz2HQQ-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تیم امید ایران  ۴ بر ۱ به امید کره شمالی باخت و حذف شد
جوانان ایران قرار است بعد بازگشت مجدد به پارتی برن و دختر بازی کنن و تو دلشون بگن کون لق فوتبال
@AloSport</div>
<div class="tg-footer">👁️ 63.3K · <a href="https://t.me/alonews/148898" target="_blank">📅 10:54 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-148895">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/75bb721a98.mp4?token=vA8GywJtccxhUhvwe5bYQEzpT06sODLm5jxXaVG_17ntO_pC1lUotTqvjRvtCxceaAbbg67P9NpU6wFmI9OufIcF7MWDuC9jYeblb-hBlkRkmwpnuKSayL1kGhoG52GP8GJ79cCg1RAHoKIb8n7vFT8NETEUR96FyO3f0yg-FicsQQrSU33CcGqI1qqD5WsJEdqnUGJP4HG0tFD61mEVrCsj7YXgvm3axRv-6oBnwSFYf_L8QWR9SbNIOw70dZ8JxbupbVZoo2LBwv3Kgc4rIGo6vxZKbX3MaNxieZeGaEgg2MVxgLtcG4OxGsD9XjTb19jECo0jIcIfmGEKXG21WA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/75bb721a98.mp4?token=vA8GywJtccxhUhvwe5bYQEzpT06sODLm5jxXaVG_17ntO_pC1lUotTqvjRvtCxceaAbbg67P9NpU6wFmI9OufIcF7MWDuC9jYeblb-hBlkRkmwpnuKSayL1kGhoG52GP8GJ79cCg1RAHoKIb8n7vFT8NETEUR96FyO3f0yg-FicsQQrSU33CcGqI1qqD5WsJEdqnUGJP4HG0tFD61mEVrCsj7YXgvm3axRv-6oBnwSFYf_L8QWR9SbNIOw70dZ8JxbupbVZoo2LBwv3Kgc4rIGo6vxZKbX3MaNxieZeGaEgg2MVxgLtcG4OxGsD9XjTb19jECo0jIcIfmGEKXG21WA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
حمله اقلیت یا همون امت معکوس به ناصر اسدی نماینده ایران تو سازمان ملل بخاطر اینکه موقع سخنرانی ترامپ سالن رو ترک نکرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.3K · <a href="https://t.me/alonews/148895" target="_blank">📅 10:51 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-148894">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">👈
فایننشال‌تایمز: بی‌میلی ترامپ برای مقابله با انصارالله، اعتماد ریاض را تضعیف می‌کند
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.3K · <a href="https://t.me/alonews/148894" target="_blank">📅 10:48 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-148893">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/063d554ef6.mp4?token=aeYYXOxQCC-OMUQ7CRKdqVySVNd8CwYtZlpuiB7fc9jj4A1OQfBqb-ok95Q7WjsSIo9mfRnjF1TgH4pi-jNLLUaERQl9wWk4MRNJ79KsHJWwu5Tqzzua3TGEYNdJWHrP2u7kRqgmf5iYPxPrYpRWEW1VsVEHGOtVWXk_wmTvqW_SP9507nC41vFmBFV3-alJ_ydDGlnR1iqcsi4YoYW7xBQovTnAvq2csfajspHiJrKhkba3FmDDrQmO2NLuPzcFMXdXHOzwMEw2LPa6sjxD77flEMaIh_H_FyQAJ558EFhfxVloHnfVaOnV3gkZ2hKCAnpB4NLdvvS0Vy5iFybwBQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/063d554ef6.mp4?token=aeYYXOxQCC-OMUQ7CRKdqVySVNd8CwYtZlpuiB7fc9jj4A1OQfBqb-ok95Q7WjsSIo9mfRnjF1TgH4pi-jNLLUaERQl9wWk4MRNJ79KsHJWwu5Tqzzua3TGEYNdJWHrP2u7kRqgmf5iYPxPrYpRWEW1VsVEHGOtVWXk_wmTvqW_SP9507nC41vFmBFV3-alJ_ydDGlnR1iqcsi4YoYW7xBQovTnAvq2csfajspHiJrKhkba3FmDDrQmO2NLuPzcFMXdXHOzwMEw2LPa6sjxD77flEMaIh_H_FyQAJ558EFhfxVloHnfVaOnV3gkZ2hKCAnpB4NLdvvS0Vy5iFybwBQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏
👈
رئیس‌جمهور سوریه، الشرع: وقتی در کاخ سفید با ترامپ دیدار کردم و او گفت که بلندی‌های جولان متعلق به اسرائیل است، به شوخی گفتم: «چرا نیوجرسی را به اسرائیلی‌ها نمی‌دهی؟ تو مالک بلندی‌های جولان نیستی که آن را ببخشی، اما نیوجرسی مال توست.»
🔴
فکر می‌کنم نیوجرسی پر از دموکرات‌هاست و آنها به ترامپ رأی نمی‌دهند، بنابراین خوب است آن را به اسرائیلی‌ها بدهی. حداقل این چیزی است که مالک آن هستی. ترامپ مالک بلندی‌های جولان نیست.
✅
@AloNews</div>
<div class="tg-footer">👁️ 65.4K · <a href="https://t.me/alonews/148893" target="_blank">📅 10:44 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-148892">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b1b063fe34.mp4?token=sj6XPJRtm8OswvqUYWxnf7O6xhiWCNtgfICg_Yocjw9vRoWD3UXmpYgZSa3UwarCjcnAwc7xxXYu1GkMLQESnrF8cxJrIUUlSOwUMiYPvXzMsgnLFGn-t0uULdj6nyhAH9AtN_vdoh4RW33Sq0zuGB50ZtTfQOuz2m9p6S4qWssdk3bAAs3soCVhmQZ1T9tLmHH0q2fEF3HLSX0imIVdkuTUpCU9meTeLy3qEK6BCkaYXZsxsWSgLLZsZZtDVR71siUzouZO2tYgGgncd7J0jbuw6Hsfmz5jBZsdm6HGUxSMTKUHUyr5U8dE0VBkx2TcgMa-RuVCeWqe53oit8B1wQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b1b063fe34.mp4?token=sj6XPJRtm8OswvqUYWxnf7O6xhiWCNtgfICg_Yocjw9vRoWD3UXmpYgZSa3UwarCjcnAwc7xxXYu1GkMLQESnrF8cxJrIUUlSOwUMiYPvXzMsgnLFGn-t0uULdj6nyhAH9AtN_vdoh4RW33Sq0zuGB50ZtTfQOuz2m9p6S4qWssdk3bAAs3soCVhmQZ1T9tLmHH0q2fEF3HLSX0imIVdkuTUpCU9meTeLy3qEK6BCkaYXZsxsWSgLLZsZZtDVR71siUzouZO2tYgGgncd7J0jbuw6Hsfmz5jBZsdm6HGUxSMTKUHUyr5U8dE0VBkx2TcgMa-RuVCeWqe53oit8B1wQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ورود باشکوه و ناگهانی ترامپ به نشست الزیدی، اردوغان و شماری از رهبران خاورمیانه در نیویورک
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.3K · <a href="https://t.me/alonews/148892" target="_blank">📅 10:35 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-148891">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LbTjKAh5ex6Ni6BC8J7xHwNBTLG4PIW6r615KxPB6anIC-YQEV05UR_x0H0iDHa7Xn-ZaoYeBqD93oPil61-ekqE9wn0rzmO_LlCNGG2bQUoH0zo3xJt0ZvTyG8VSCVKQrYVeZJP4sjNCakgPDbWUjv_a6zctcqjGLtPEkjXIpEeCWl8FFy0q0mH3FJT9KPXtUoRpna5Q1gDHZdM_2JCZg_600gu5cF2j0zUSD-OY49u7hCdPC5jD4Gq-5vbU0D7f4j6pg7_nL34BJG-Y2EamnIKuhZw0AUCcYR3MsdEQb8_DLxKkedyCeEvDEKYy3CCTTu0S9-bl1mub7Cvp3adHg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
حمید رسایی:
پزشکیان باید تو سازمان ملل به ترامپ سیلی بزنه
✅
@AloNews</div>
<div class="tg-footer">👁️ 64.3K · <a href="https://t.me/alonews/148891" target="_blank">📅 10:29 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-148890">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">👈
داده‌های کشتیرانی: روز گذشته ۳ کشتی باری حامل کالاهای اولیه از تنگه هرمز عبور کرد، در حالی که میانگین متحرک ۱۰ روزه، حدود ۱۵ کشتی بوده
🔴
داده‌های مربوط به عبور و مرور دریایی نشان داد که روز گذشته، سه کشتی باری حامل کالاهای اولیه از تنگه هرمز عبور کردند؛ این در حالی است که میانگین متحرک ۱۰ روزه حدود ۱۵ کشتی بوده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.3K · <a href="https://t.me/alonews/148890" target="_blank">📅 10:25 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-148889">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1ddf2a0d29.mp4?token=C6QRiXZrc4cKcAd_njyqVNJS0neA-voV_QDEW9YOIARXRtBZRef686x5Ei-2VWzuvF-59zUhsVyKkUFOqjCa_dpuaQ9ohMQoVqGNJWbbde7ViM0zxbALrN06sXpie92WrUpWLHj0uUufHrnlteYdLJ7NmOlFzaWnIiwrlk7WPCYgEUvMygkFPHyBz_b3s7kOPFy3Ceyikos7RxjDPeaXb6jApXcweJT14_rDgF0gnFElZmqgkcq4V24AEYE-U6GWXCTciOIvGhCFzBdllGwaArvlw7D02BeBQHECBljnnjP90YIaBoHHnwhTRxMqJLpmEMvdNE20PuCXjdb2oNpTtQi4gjj33mHPeJyFe0xG-GxI5NavWxlaicQ5bAR4f79zukUBgpqPrlOokA4iODTDcb4RiTCR8-bez92sAjzbWHMtMw9xw_BDUiQNQIUSBcg0O9paYluEmlbJQJWOVgZg0E7gWIr55TG5yGg_dkGLT5cDPsXbCoJvE0r_6uW96cKpjbnS9z_DQYuGllJc0RlfamNGfmE3Lyf_7nxNKAN0HyxebyCISMlCuNomGQrZkrA06QcW7O6i_5OrndOKA8vTgih8vIjLTj21afb1NbUZZKeyIJA_egUDRoLYOHCnC3jvKShpLTjsvJB3ZCLSwW0Wds6fnIWpbPs5gKzqHKR132I" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1ddf2a0d29.mp4?token=C6QRiXZrc4cKcAd_njyqVNJS0neA-voV_QDEW9YOIARXRtBZRef686x5Ei-2VWzuvF-59zUhsVyKkUFOqjCa_dpuaQ9ohMQoVqGNJWbbde7ViM0zxbALrN06sXpie92WrUpWLHj0uUufHrnlteYdLJ7NmOlFzaWnIiwrlk7WPCYgEUvMygkFPHyBz_b3s7kOPFy3Ceyikos7RxjDPeaXb6jApXcweJT14_rDgF0gnFElZmqgkcq4V24AEYE-U6GWXCTciOIvGhCFzBdllGwaArvlw7D02BeBQHECBljnnjP90YIaBoHHnwhTRxMqJLpmEMvdNE20PuCXjdb2oNpTtQi4gjj33mHPeJyFe0xG-GxI5NavWxlaicQ5bAR4f79zukUBgpqPrlOokA4iODTDcb4RiTCR8-bez92sAjzbWHMtMw9xw_BDUiQNQIUSBcg0O9paYluEmlbJQJWOVgZg0E7gWIr55TG5yGg_dkGLT5cDPsXbCoJvE0r_6uW96cKpjbnS9z_DQYuGllJc0RlfamNGfmE3Lyf_7nxNKAN0HyxebyCISMlCuNomGQrZkrA06QcW7O6i_5OrndOKA8vTgih8vIjLTj21afb1NbUZZKeyIJA_egUDRoLYOHCnC3jvKShpLTjsvJB3ZCLSwW0Wds6fnIWpbPs5gKzqHKR132I" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
امانوئل مکرون، رئیس‌جمهور فرانسه، درباره ایران: «فکر می‌کنم پس از آغاز جنگ در اواخر فوریه، اهمیت تنگه هرمز احتمالاً دست‌کم گرفته شد و امروز باید این مسئله را حل کنیم.»
✅
@AloNews</div>
<div class="tg-footer">👁️ 66.4K · <a href="https://t.me/alonews/148889" target="_blank">📅 10:09 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-148888">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">این وسط ماهم 1m شدیم
✔️
مرسی از بودنتون
❤️</div>
<div class="tg-footer">👁️ 64.3K · <a href="https://t.me/alonews/148888" target="_blank">📅 10:06 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-148887">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/l0Rw1gKcgCEU4FqUhW3aqOw3VnDnO11watw-usbWkbf8EmmE8tIN8W-MLRTpiscADmjRiA24BEJ4tbHZlu1ac4g8imwmuNCieA1REZ-pu_kD6vM_J4-QmwwUHX5JAhjhjDvOCeImBMLiAlLcXgf0SwLDXBb59EO939AP0AvoyfAnwZcIwDbm7aow4rQ9OyePK9g2aL8Qvijr-5YJDFZdJRyZrIoLWfmcT1ukmfPItlpLj6uSwX6GkZqNEvq7Nr6w1x4OSiTqlHl8aVQM6LdLtSIJtx6WOc5K77jbg37eIagyZPgde-BYVEmv46WHlkv52sJN8d-RfkNk_K-rVwBZgA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
الجولانی: به شوخی به ترامپ گفتم «اگر می‌خواهی سرزمینی به اسرائیل بدهی، چرا نیوجرسی را نمی‌دهی؟ چون تو مالک جولان نیستی»
🔴
جولان سرزمین سوریه است و درباره آن جای بحث نیست
✅
@AloNews</div>
<div class="tg-footer">👁️ 64.3K · <a href="https://t.me/alonews/148887" target="_blank">📅 10:06 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-148886">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3982b6a001.mp4?token=JlKI5uOWFG8ezpSEQVLPoVYTRGpWTw0Mq4VK-ExyFPmEtENf7oUoXlJNuuYKb-fAzKmHaga__dvKxggkK-eMM2xJd12p3X5sN63sZ1Czmo7LqcS4p5ZuVq19sGBi0rO5dh_0f3YODjEAEqDt9Tab4akctMHHFah4SisjSgnG0QJ54sFRy5Vhzl6svEFSOPZLwpX-U4kq-vgKBvulALcgZI_e-XcZq2KKnaLj8l7JdtXJTHw6luwr1o6RFkZK-3FiDYyIxjMMn1_SQQyGP5vmaTO5ioCEBakiF87Nq-hrHCqtbA__xr02qM0fAUigSSvRRfLpViy8df2hmp3BaJZrhzv_BL0Rtr2Ty4tSTgwZasBlBC8R_cziwg-ZQ_8cSgNxMSdKr4M0KH0H5Rauf4ECoa0Lc4ACLsvsYQyvAxLVPnk8lSLwGa9j6lvm1gw9Ibg2fymtMf6s_NykyvZE6T5L7grNuddAfsYW2x8pd8O1SRLa54QCns4DMlUw8DTu_d6GRHlMVIFxEJHr7l5C7bDVIOsI-9ZIlC5_2ABzDJ_Ia883CGpFVB9H3UDP8Gbg3_Ed2xDsCLu2LS09pQWhfH0B2O4BrAscwJAA8PmqxblFRGVOMrhJcdfVw9cPmde35jmvVWRx4ev1tBZj0d4Wv9yEF4KZPuA9H4NBH_GxYNqduEA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3982b6a001.mp4?token=JlKI5uOWFG8ezpSEQVLPoVYTRGpWTw0Mq4VK-ExyFPmEtENf7oUoXlJNuuYKb-fAzKmHaga__dvKxggkK-eMM2xJd12p3X5sN63sZ1Czmo7LqcS4p5ZuVq19sGBi0rO5dh_0f3YODjEAEqDt9Tab4akctMHHFah4SisjSgnG0QJ54sFRy5Vhzl6svEFSOPZLwpX-U4kq-vgKBvulALcgZI_e-XcZq2KKnaLj8l7JdtXJTHw6luwr1o6RFkZK-3FiDYyIxjMMn1_SQQyGP5vmaTO5ioCEBakiF87Nq-hrHCqtbA__xr02qM0fAUigSSvRRfLpViy8df2hmp3BaJZrhzv_BL0Rtr2Ty4tSTgwZasBlBC8R_cziwg-ZQ_8cSgNxMSdKr4M0KH0H5Rauf4ECoa0Lc4ACLsvsYQyvAxLVPnk8lSLwGa9j6lvm1gw9Ibg2fymtMf6s_NykyvZE6T5L7grNuddAfsYW2x8pd8O1SRLa54QCns4DMlUw8DTu_d6GRHlMVIFxEJHr7l5C7bDVIOsI-9ZIlC5_2ABzDJ_Ia883CGpFVB9H3UDP8Gbg3_Ed2xDsCLu2LS09pQWhfH0B2O4BrAscwJAA8PmqxblFRGVOMrhJcdfVw9cPmde35jmvVWRx4ev1tBZj0d4Wv9yEF4KZPuA9H4NBH_GxYNqduEA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
امانوئل مکرون، رئیس‌جمهور فرانسه، درباره ایران: «این درست است که ما در این جنگ حضور نداشتیم؛ نه به این دلیل که در کنار آمریکا نبودیم. ما برای آمریکا احترام قائل هستیم و فکر می‌کنم متحدان خوبی هستیم.
🔴
اما وقتی می‌خواهید کشورها و افراد را درگیر یک اقدام کنید، باید با آنها هماهنگ و برنامه‌ریزی کنید و پیش از آغاز یک جنگ با آنها مشورت کنید.
🔴
ما تصمیم گرفتیم به این جنگ نپیوندیم، زیرا معتقد بودیم — و من همچنان معتقدم — که گزینه درستی نبود.»
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.3K · <a href="https://t.me/alonews/148886" target="_blank">📅 10:02 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-148885">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qIHL-swpUvpkb60lxrHPXEgp82JO7fJ8aQU-PQKqlwko8weglAlvQmrDmhF_6W17BAErhIrnxoYnEtUc94VNs8IR_VVeZ6R49Yt_jcsc-ScJ7bYH-jLe9m6AmFkh1IVAvQu_tAj-Od7PdDL77_aec1e4bBXa9Fl0TDPlEUJuf-DZQ5h5gwo39hg1-lFoZmXq8kS7CoGu-OYjMhw_257P_fAv0dp5u8JIg5-nJmFDgHvOLOdCt4UAL4JbIu-WnMLBPUhug1Bk--YdNQH75gDuv8qc-tgMmLAICtVc5v56i-CBcNEnDNAMU9IyVTI8uZ9bRq7Ssgo8-5MtKJ7hpWVqhA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ترامپ، رئیس‌جمهور آمریکا: «تمام این آدم‌های پست، مثل کیتلان کالینز، خبرنگار درجه‌سه شبکه جعلی CNN، که واقعاً فردی ناراضی است، گفتند قرار نیست من را پوشش خبری دهند
🔴
پس چرا در محوطه رسانه‌ای سازمان ملل مثل دیوانه‌ها فریاد می‌زدند و جنجال به پا می‌کردند؟ او آنجا چه کار می‌کرد؟
🔴
او به «ترامپ» اعتیاد دارد و CNN و MSDNC هم همین‌طور. همه آنها بیمار، خائن و دیوانه هستند!
🔴
«خبر خوب» این است که آنها یک قاضی بسیار خوب، البته برای خودشان، و کاملاً بی‌وفا دارند.»
✅
@AloNews</div>
<div class="tg-footer">👁️ 64.3K · <a href="https://t.me/alonews/148885" target="_blank">📅 09:57 · 01 Mehr 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>

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
<img src="https://cdn4.telesco.pe/file/PgrcHjsDsPwoEtyTnsbNiYlZod5q46IfzaYKuA85kVY9z-Avmx7rg9aJll6Ls_Jxjsab2EeoNWnBrkFJTTMNp25tEe02z7OcQ3w2sNVdVosCkzBIAkp9Y6Lk1Sbpu8GWJ1G2prr-2QmwhCr139kvIPGV9fATSMNB5mZ90ccG5og415FZaMlSR7yFFhDO8UdezWpoZcRU11Da3sVxjs_P-unnE2KxdZNPANixbdC4Uvk9HKEM8KOz8DklwkeBbPaGeEK28whc0jrPEXZETw63eYhB6QywThkUKEYV7igWDZHyRNF1Py7OjSeKcMQKGe-cQMDl7NFgFzrGKhUB6FY37Q.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 اخبار جنگ الونیوز AloNews</h1>
<p>@alonews • 👥 932K عضو</p>
<a href="https://t.me/alonews" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 با الونیوز از اخبار جنگ و وقایع در چند ثانیه مطلع باش!اخبار جنگ بدون سانسور در الونیوز👌جهت رزرو تبلیغات👇https://t.me/ads_alonewsپشتیبانی کانال🕵️https://t.me/AloNews?directادمین کانال🎩@AloNewsBotX:https://x.com/AloNewsBot</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-14 15:39:41</div>
<hr>

<div class="tg-post" id="msg-131905">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">👈
ریاست‌جمهوری سوریه: امانوئل مکرون به‌زودی به دمشق سفر خواهد کرد و یک هیئت از سرمایه‌گذاران فرانسوی در این سفر، مکرون را همراهی خواهند کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 18 · <a href="https://t.me/alonews/131905" target="_blank">📅 15:39 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131904">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FidBA8KGjMSe9J13ACTRnkh1r3bjppUfYFMLBa89LmSXACwylTQfrke-QOT6dsPltQnJlIC2J2p3oO5q6KWQpbn3cL5Zyu6efD8s4jrYAY7ZcM46QSDK1Tg9VYl-QNAqBINcuwpyXxiVd9yiw3ZrNwIQb0GbqIv4pmkfhcol_Y63RCted6-c4Co68SOfiEtF3eVWYi5FpPqzufNjr5LUErmM7PyyyccIjpmxOJIUslEcKWn9ssA-dQixWG-S6WyKIwN5rTFKBoPHWmWi7teut0M9c2TsnpBCbE8-TIhGImZInSLO-ov_omPKFk9R2gk6ZKxxVLwohEGfPSea7N8Xeg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
پست ترامپ در تروث: از زمان آغاز جنگ در ایران، بیش از 273 آمریکایی در شیکاگو هدف گلوله قرار گرفته‌اند
✅
@AloNews</div>
<div class="tg-footer">👁️ 4.11K · <a href="https://t.me/alonews/131904" target="_blank">📅 15:35 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131903">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">👈
نتانیاهو، نخست‌وزیر اسرائیل: تهدید ناشی از غزه برطرف شده و هیچ بازسازی‌ای در این باریکه بدون خلع سلاح انجام نخواهد شد. به ساکنان غزه آزادی انتخاب داده شود تا میان ماندن یا ترک تصمیم بگیرند
🔴
ترامپ از ما نخواسته است که علیه تونل‌های حزب‌الله اقدامی نکنیم و برای باقی ماندن در امتداد «خط زرد» در جنوب لبنان، مشروعیت لازم را به دست آورده‌ایم
✅
@AloNews</div>
<div class="tg-footer">👁️ 6.19K · <a href="https://t.me/alonews/131903" target="_blank">📅 15:31 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131902">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">👈
سفیر ایران در چین اعلام کرد تهران پس از پایان دوره ۶۰ روزه توافق اولیه با آمریکا، برای کشتی‌های عبوری از تنگه هرمز هزینه خدمات دریافت خواهد کرد، اما کشورهای «دوست» از شرایط ویژه برخوردار خواهند شد
🔴
رحمانی فضلی گفت ایران همراه با عمان در حال تدوین سازوکارهای جدید برای تردد در تنگه هرمز است. او تأکید کرد مبالغ دریافتی «عوارض عبور» نخواهد بود، بلکه هزینه خدماتی مانند تأمین امنیت مسیر، نظارت بر عبور کشتی‌ها و رسیدگی به پیامدهای زیست‌محیطی تردد دریایی است
✅
@AloNews</div>
<div class="tg-footer">👁️ 8.23K · <a href="https://t.me/alonews/131902" target="_blank">📅 15:28 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131901">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">👈
فارس: قایق‌های سپاه 6 کشتی رو از تنگه هرمز خارج کردن
✅
@AloNews</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/alonews/131901" target="_blank">📅 15:18 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131900">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">👈
کدام فرودگاه‌ها فردا تعطیل هستند؟
🔴
در روز ۱۳ و ۱۴ تیرماه پروازها در سراسر کشور بدون محدودیت انجام می شود و برنامه پروازها به روال عادی ادامه دارد.
🔴
۱۵ تیرماه همزمان با برگزاری مراسم تشییع آسمان تهران به طور کامل بسته خواهد شد.
🔴
۱۶ تیرماه نیز فرودگاه مهرآباد فعالیت عادی خود را از سر می گیرد و فرودگاه امام خمینی نیز تعطیل خواهد بود.
🔴
۱۸ تیرماه همزمان با برگزاری مراسم تشییع در مشهد، آسمان این شهر و فرودگاه هاشمی نژاد به طور کامل بسته خواهد شد.
🔴
در روزهای ۱۷ و ۱۸ تیرماه نیز پروازها در سراسر کشور به جز مشهد بدون محدودیت ادامه خواهد داشت.
✅
@AloNews</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/alonews/131900" target="_blank">📅 15:11 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131899">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">👈
روزنامه عبری معاریو در گزارشی مدعی شد که دونالد ترامپ، رئیس جمهور آمریکا، برای برگزاری یک دیدار سه جانبه در کاخ سفید با حضور بنیامین نتانیاهو، نخست وزیر اسرائیل و جوزف عون، رئیس جمهور لبنان، تلاش خواهد کرد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/alonews/131899" target="_blank">📅 15:05 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131898">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e49482f3e9.mp4?token=MSfKPppzpTHDXmsx0rwmGARfta9TA1m3pgllC_xY3zdwed6kjWO1MoqMJO1FavFu8Ug7dxUL9JkxHyNVNXqdOboCxyJ65FU4NPAMSFUIlXpruZxy3KKi3QUPnrVF3tVpVIvsgfxgclsTIYEj48ohnVAQAPOgNHOxOc7XA-gVNu2iG2Lne1EVIf-xivPj9EVidq-tKynXEPbHWurqtYE6HX82dDg1495vxiILSqA1SpIH4I9pRhZXikZ4tMRlT2r-WDcG8jQwaNj4_h6r0mH93w0551R6nSvFK8OBOfEQxLC8ufj--eyQQ48i0QNAitXh9o954g-p9UxVN1w_UNwYgA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e49482f3e9.mp4?token=MSfKPppzpTHDXmsx0rwmGARfta9TA1m3pgllC_xY3zdwed6kjWO1MoqMJO1FavFu8Ug7dxUL9JkxHyNVNXqdOboCxyJ65FU4NPAMSFUIlXpruZxy3KKi3QUPnrVF3tVpVIvsgfxgclsTIYEj48ohnVAQAPOgNHOxOc7XA-gVNu2iG2Lne1EVIf-xivPj9EVidq-tKynXEPbHWurqtYE6HX82dDg1495vxiILSqA1SpIH4I9pRhZXikZ4tMRlT2r-WDcG8jQwaNj4_h6r0mH93w0551R6nSvFK8OBOfEQxLC8ufj--eyQQ48i0QNAitXh9o954g-p9UxVN1w_UNwYgA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
حضور ایمان تاجیک، سخنگوی جنگ ۱۲ روزه، تو مصلای تهران
✅
@AloNews</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/alonews/131898" target="_blank">📅 15:01 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131897">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">👈
بنیامین نتانیاهو، نخست‌وزیر اسرائیل: حزب‌الله از توافق ایران حمایت می‌کند و توافق ما را مورد حمله قرار می‌دهد
✅
@AloNews</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/alonews/131897" target="_blank">📅 14:55 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131896">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">👈
سفیر ایران در چین: کشتی هایی که از تنگه میگذرن باید هزینه ناوبری بدن ولی برای کشتی های چینی تخفیف و ملاحظات خوبی در نظر گرفتیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/alonews/131896" target="_blank">📅 14:51 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131895">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OjYhZRS2ZDfmDXNBuL-Kkaz2L1Pcg_uiRHndrIi4JpKXqcNbY2qW9WNAo7nWsfsV0ISzkb1bg6nt6PwPq3KmXrffZkFfdfjXe6FFGUqeDRad3MnTvHYm3UgXbZN_mAxBCxmhZuJ6CueM40NtuFaR5-eaPnvd5K-wSLada1-AXaGEOLeh0zMU2pFG3QlHemBLaVbmgmxRk-sgFMjZbHyaONdb_OZqkvHN1iHGKaorraa-mEhqVKXKtkDxI6kaRGuiXMCGMBQ_RpHJKdGnhlhb_FK3Q2VuWj0beVG_dQ_qc8FX0qHWVRw0aDXbTHE2r0cnSxodXA9pJxy5_vqgAxAHCg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
دیده شده در مراسم تشییع
🔴
خواهیم دید چه می‌شود...
✅
@AloNews</div>
<div class="tg-footer">👁️ 30.7K · <a href="https://t.me/alonews/131895" target="_blank">📅 14:41 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131894">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">👈
نتانیاهو : حرف‌هایی که درباره درخواست ترامپ برای حمله نکردن به تونل‌های لبنان پخش شده
🔴
کاملاً دروغه، ترامپ اصلاً چیزی رو به من نگفته
🔴
منم چنین درخواستی ازش نکردم و ما تصمیم‌هامون رو بر اساس ملاحظات خودمون می‌گیریم
✅
@AloNews</div>
<div class="tg-footer">👁️ 31.7K · <a href="https://t.me/alonews/131894" target="_blank">📅 14:37 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131893">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">👈
محمد مخبر: قاتلین امام به مرگ طبیعی نخواهند مُرد و نظام انتقام خواهد گرفت
✅
@AloNews</div>
<div class="tg-footer">👁️ 32.7K · <a href="https://t.me/alonews/131893" target="_blank">📅 14:32 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131892">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/589db9025b.mp4?token=JjLx57VdIAminIwNqONlanr6v96_llsBZmBrkiteZEWQQLkZbf2s_Q8DDbkbQhDLj_39LjuZqWRTQuHFlPm12Ffr34byhx--Jtb9MX7T7p2uzyWhG-BdQVLjYFfoLBtfPIyYuGwpgM2iWi1ATljnT4dx_tFAo4heUEaWZJByvsBvtiFbYiu9iVLRdeXlisAL4C89bKUifJSTIiGpkm5_iM7AQrseWr45-rlENI1F3kL0Sy5gdtDUTvvwEs6_f3vKAbX_0L-nRn8iSeAiuwa5zkf8HYCGmPeqPM4axNaXJGrAVqeIRpYE_Ie9jm1mP7gVnWl3mUm38ECbmC33-XvuSw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/589db9025b.mp4?token=JjLx57VdIAminIwNqONlanr6v96_llsBZmBrkiteZEWQQLkZbf2s_Q8DDbkbQhDLj_39LjuZqWRTQuHFlPm12Ffr34byhx--Jtb9MX7T7p2uzyWhG-BdQVLjYFfoLBtfPIyYuGwpgM2iWi1ATljnT4dx_tFAo4heUEaWZJByvsBvtiFbYiu9iVLRdeXlisAL4C89bKUifJSTIiGpkm5_iM7AQrseWr45-rlENI1F3kL0Sy5gdtDUTvvwEs6_f3vKAbX_0L-nRn8iSeAiuwa5zkf8HYCGmPeqPM4axNaXJGrAVqeIRpYE_Ie9jm1mP7gVnWl3mUm38ECbmC33-XvuSw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
حملات توپخانه ای اسرائیل به جنوب لبنان
✅
@AloNews</div>
<div class="tg-footer">👁️ 37.5K · <a href="https://t.me/alonews/131892" target="_blank">📅 14:15 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131890">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">👈
مدودف: ایران سلاح‌ هسته‌ای اش را حفظ می‌کند!
🔴
ایران به جای داشتن یک سلاح هسته‌ای واقعی، متوجه شده است که سلاح دیگری دارد که از سلاح هسته‌ای ضعیف‌تر نیست، یعنی تنگه هرمز، که وضعیت بین‌المللی پیچیده‌ای دارد. ایران نه تنها این سلاح‌های هسته‌ای را حفظ می‌کند، بلکه یک سلاح هسته‌ای حرارتی نیز دارد که همان تنگه باب المندب است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 39.2K · <a href="https://t.me/alonews/131890" target="_blank">📅 14:05 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131889">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nnfnWbxC785ei_68b1wEuv3hpJ2QXVutyznogvXaCZd1kCD056r-0_wfY5bg3YleqJn-jTQAKFkglO-iyaxDAvH9Z6q9j1lT9tIJ1u9KQHKzSeCnWZY2MlbIYxIB6qbOUtDp0_-nlx2E9LSqAPfAHclTsu3wqVkbsqrUlAJjRYdElWKYvaoKuW9qtx14CNewe2SryTMTkCc-oX4kuLPLG4t7_OHQST8TQkJXqCnPrCBJD8pw0hbujDknhJlY9e6EQVL4_PGppBwRg29kc65Pghca_Ce9oEem_EzLLk0Egv1IC6U8fcQo3wthHJeeOJ5OWA_qMB2Z3ajHb4LeK4Osdg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
دبیرخانه شورای عالی امنیت ملی:
این چند روز چشم‌تان را به ایران بدوزید؛ این همان ایرانی است که خیال می‌کردید چند روزه می‌توانید آن‌ را از پا درآورید
✅
@AloNews</div>
<div class="tg-footer">👁️ 39.4K · <a href="https://t.me/alonews/131889" target="_blank">📅 14:03 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131888">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">👈
خودروسازان چینی با رشد سریع صادرات و استقبال بازار اروپا، برای نخستین‌بار از نظر حجم فروش از رقبای ژاپنی عبور کردند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 41.9K · <a href="https://t.me/alonews/131888" target="_blank">📅 13:47 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131887">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">👈
شرکت بهره‌برداری متروی تهران: از بامداد تا ساعت ۹ صبح امروز، یک میلیون و ۳۰۸ هزار و ۴۴۵ مسافر، بیش از ۳ میلیون سفر در متروی تهران داشته‌اند
✅
@AloNews</div>
<div class="tg-footer">👁️ 43.2K · <a href="https://t.me/alonews/131887" target="_blank">📅 13:40 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131886">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">👈
به گفته برخی منابع در اسرائیل معتقدند احتمال وقوع یک درگیری نظامی مجدد با ایران در آینده نزدیک وجود دارد.
‎
✅
@AloNews</div>
<div class="tg-footer">👁️ 43.9K · <a href="https://t.me/alonews/131886" target="_blank">📅 13:34 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131885">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">👈
دولت ژاپن در حال بررسی کاهش سطح هشدار سفر به ایران است
🔴
در پی بروز جنگ آمریکا و اسرائیل علیه ایران، وزارت خارجه ژاپن سطح هشدار سفر اتباع خود به ایران و 3 کشور منطقه را به درجه 4 (تخلیه فوری) افزایش داده بود.
✅
@AloNews</div>
<div class="tg-footer">👁️ 44.9K · <a href="https://t.me/alonews/131885" target="_blank">📅 13:30 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131884">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/P2zbfMIwEzlvTDY-hHc7Xx5I5kgbTYgTk-oAchVgymVAEHb95OuwnD7yZOF9QMrNjxtpOe7VOYNBv2ixcq_ITohhnZcKRSo9gasOinBozkDbIYNYaniG9ZAs_pVtlabBcGqm-0qsYY7M9my8hv6lAF4GDlgDtvzMByGDWItZM99cjVjXCjdQysN9Mn_Ust2fJzd09nppSsyeAJycegWdHpItYhj-CBPSORCt7Baeb8SVibviaJRlVh3Xm_6jfR1K-Vf2tZBbsNjuGKkWAJoRiRDZdyajJJPXUQMzcCdyNLPU4j4JQuBRfl9ghdtlNqQEI8qV9aQTLDcd4zYhUYm_yA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
اینترنت آزاد کشمیرِ تحت کنترل پاکستان
🔴
با گذشت یک ماه از قطعیش، هنوز شدیداً مختلهِ - Nut blocks
✅
@AloNews</div>
<div class="tg-footer">👁️ 45K · <a href="https://t.me/alonews/131884" target="_blank">📅 13:26 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131883">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">👈
تلگرام از مرز یک میلیارد کاربر فعال ماهانه عبور کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 44.9K · <a href="https://t.me/alonews/131883" target="_blank">📅 13:21 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131882">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">👈
جوزف عون، رئیس‌جمهور لبنان :
من علاقه‌ای به اسرائیل ندارم، اما راه حل دیگری را به من پیشنهاد دهید که ما را از این جنگ‌ها بیرون ببرد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 47K · <a href="https://t.me/alonews/131882" target="_blank">📅 13:08 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131881">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">👈
العربیه: ترکیب و سطح هیئت اعزامی‌ایران هنوز نهایی نشده و پس از پایان مراسم تشییع، تعیین خواهد شد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 48K · <a href="https://t.me/alonews/131881" target="_blank">📅 12:59 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131880">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Zqy_hUPeAHlccVQL8S4HliAT1pN4MIeVRtmmdu16KSqsBIpviWP5gnENeerkDkQVk3NwoDoS_ypZG0Sga_U4-EYeyfAxi3bSqrMMXEtMuzC89MbS5iIt0ZTmOZ1WoDmbO6lAlWvRlvlXOkvpECYLVzZZU2g4KHBYuv5SgrLjBOLn9OQktJMBPhU__wi7i2D6UaJAucP3GP2OetKpZNJM15dcGcO4J-F_oiiiVvqolNGnpMH8t8EcdPYaBHw8DvPUh6dCWyLAoxjkB_SIbv88OpQqidevB6GlPTeKcUSx1L_ehN2UeHAxpOm1zAa56d6MJC1xmmdTVE14jrQ_Yq-ejQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
آمریکایی ها مجددا یک گروه از نفتکش ها را ردیف کرده و در حال اسکورت آنها به سمت تنگه هرمز هستند
✅
@AloNews</div>
<div class="tg-footer">👁️ 50.1K · <a href="https://t.me/alonews/131880" target="_blank">📅 12:51 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131879">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">👈
سامانه گنبد آهنین به امارات ارسال شد.
🔴
میری رگو، وزیر کابینه اسرائیل مدعی شد که اسرائیل سامانه پدافندی «گنبد آهنین» را به امارات متحده عربی ارسال کرده است.
🔴
وی همچنین ادعا کرد: اماراتی‌ها از ما کمک می‌گیرند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 49.1K · <a href="https://t.me/alonews/131879" target="_blank">📅 12:46 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131878">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">👈
ترامپ: نتانیاهو احتمالاً هفته آینده به کاخ سفید می‌آید
✅
@AloNews</div>
<div class="tg-footer">👁️ 48K · <a href="https://t.me/alonews/131878" target="_blank">📅 12:44 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131877">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">👈
سازمان دریایی بریتانیا: یک کشتی باری در سواحل الحدیده یمن از سوی افراد مسلح ناشناس مورد حمله قرار گرفت
✅
@AloNews</div>
<div class="tg-footer">👁️ 49K · <a href="https://t.me/alonews/131877" target="_blank">📅 12:40 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131876">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">🔴
فوری / ارتش اسرائیل از حمله هوایی به غزه و ترور دو عضو ارشد حماس خبر داد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 50.1K · <a href="https://t.me/alonews/131876" target="_blank">📅 12:36 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131875">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">👈
استانداری هرمزگان: احتمال شنیدن صدای انفجار ناشی از خنثی‌سازی مهمات در امروز وجود دارد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 49K · <a href="https://t.me/alonews/131875" target="_blank">📅 12:31 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131874">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">👈
دعوت رسمی از ترامپ برای سفر به پاکستان
🔴
آصف علی زرداری، رئیس‌جمهور پاکستان، هم‌زمان با روز استقلال آمریکا، به‌صورت رسمی از دونالد ترامپ، رئیس‌جمهور این کشور، برای سفر به پاکستان دعوت کرد.
🔴
حساب رسمی رئیس‌جمهور پاکستان در شبکه اجتماعی «ایکس» اعلام کرد مردم این کشور مشتاق استقبال از ترامپ در اسلام‌آباد هستند و میزبانی از وی را مایه افتخار می‌دانند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 50K · <a href="https://t.me/alonews/131874" target="_blank">📅 12:24 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131870">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/MrnNjYBF4klNQ2r_8wS-chlSSCZdTnwZCf6dZUT71TTpNYkm7hBQEIroJQriCQz88GqYFNtQTMcdx-v4PjMxdMVanYr51ZufK_h6eE29mEOyw3BdaIrCRGObbU__FRGRDhdlsJiuqketDWa_Rom7WR8V54swI8DwXtDtsSixp0GR8GF0kuIJ-9xMUaLDJWkz8s0HbsKIzYMcGkThltQ0VFWtMJxqMygNE8xmgIkVo_SGeBeuREVj8VoVK0OaSJSBSi8xVHKZf4HLqMMS62-OuuBix69IppiyeCusoW911lYJNMaaxRPFTNR1CSYS39aGuRoE_5Hf6QaoGtJdfg_41w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/pJX4itClcFmxRFYqW9tj2QPzHweYhvLcUSPOPTLJlX3qlNyeKo-ZYZjmwCNzeqEWqNbodzmsnV3EmQoaNcM6G3II2U1TJHrb_dNvCzF9YdUNZA6oGLGddZ5o24wmd0ZHXNfzOUqetHocEfvWoQFPsdL4of6YyHax1RmJdF_U7upQcRXZTQMBJeRjXkokKY4MRsGSKgMCyLkzpGjOpMbMFZ2EjnA2A0K-3Eywv3JhAwYipbKV72VSXtI4_fEdjsG1-gMasottrgcrydcEA3Hl8qu9IWO2dNoW4ERCKFJ_yQQhuT6oHZ8QCn_vf7eyOhcF4p-Hr1-IF-pPR19GnAaMDQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LBjZJcOfJiSmS8NbXdKjl6VPHJTN-tZ0R4CV6qoDATx3Py8VIsGg2koU-UqJEBo_8_25o6ND5SqCwmqM366txaj4SZWqTiVgdsIA5eygcDH72g5O7XQtLF4qQxhH4w2kcKk2DkAHhkLtZF8zcfwJQwR2LSe07JJzsLEtbzu4LK9lclK3gD8V5x5BsOYXXef1up7Ow4027z8f1krJWwFHTqVciTufBIOU1z4enXRJE1PsbAW0SeItGVcSMp-lVGr_id2iSQ9Hjlsyp56L3e5x7mDdWPthuKZ_OJKZKU1L5vxTW_4wpKmU4nwd0q8FcZ3HwWAITaTGKP25wdArKggNnQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/mEOiTm4hxRWKpzsDA_PN5hQQGZT9byzpa6C8wJIBYY1LfC1cH8o3KmPwLv68AwB4TSo_GWmPSHA1DjyVLw3_dnGe4U_n3FHngHFWlY3WW8-A8d_xnWF-S68mlh2KjuFkPNKjmxHEMNbOJmdYqzI0_tMdoc-aQVp-jfxDQsHTYACI3L3uvIabxPpia4TK1vignHYMYAXXWo0koVpiYszcVTOgWWmBlFH6wnQlgPvwScBnxVp8XmYWPt2LY9Obkh3cG99FIwBILBArnCKf7o1Jo3jSVfEyyEVRWltlRwGo6fZpN8T547N6nKN1oDDOjioxVNwkYdG-q9VAxG1Nj6l4ww.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
کیم جونگ اون، رهبر کره شمالی، از آزمایش‌ های موشک کروز استراتژیک و سامانه‌ های پدافندی ناو شکن جدید «کانگ کون» بازدید کرد
🔴
این آزمایش‌ها که جمعه انجام شد، شامل ارزیابی سیستم‌های شناسایی، توپ‌های دریایی و جنگ الکترونیک بود. کیم از پیشرفت تسلیحاتی ابراز رضایت کرد و دستور داد تا ظرف دو ماه آزمایش‌ها تکمیل و ناو به ناوگان اضافه شود.
✅
@AloNews</div>
<div class="tg-footer">👁️ 51K · <a href="https://t.me/alonews/131870" target="_blank">📅 12:19 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131869">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">🚨
اتفاقی عجیب در جام جهانی
‼️
🔴
گروهی از طرفداران زن آرژانتین بعد پیروزی مقابل کیپ ورد در سکوهای استادیوم کاملا عریان شدند
😐
⚠️
مشاهده فوری و بدون سانسور
⚠️</div>
<div class="tg-footer">👁️ 47.9K · <a href="https://t.me/alonews/131869" target="_blank">📅 12:15 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131867">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/cIUvDyJJoqo29hI73qqwT0ciR6GLPEnnIH93Zet_58DvTgmirTccGjy5mnMrSkJA7e7CQaYMUk_B2d3W-RpK5gGrvm6gExEZJxA-D_ec59InOu1Sb70unOcV0bjv3yC2xNUVRrJYPVL_9nY8aKxCHITNPzWCEWiKrSe49WX5D3wknwQooApFuDxkPeBuMFA5mS9Pqhk6RkMaB2oJYDPBMgJ1zv8sNSBIWvutV6MMlFHu0LpacAXD1UJEU_VNqzpDUnz8a3p4HL12v3Eec2iWJYrMLlZ4Px6KK7O0O0YDzAAyfITgOuerdaxKb-iJvRAvK3PL15BQ4cVH5eDn0Reayw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/YxILHJXPyHHyEAJSTNm6HgfLH0YusLEni9aPTcfWddGi31wdo2D_hgrfxns7MktSHcPqsE_rO357lceB7bxm9lX4ZmUeoU0mQfguCYvUIoebyodplsck8w9grStvFal5Z_sMQFVJEVTPUjMCloJTRfXXfW_ZIaUv32kggFCGMgVWGz3rVlvD0JcGcrGxKzcUMEgAyBieBX7TQbg1a1TanPKh7SVB-WzsWyYnsPu2qPiOv5zbDMxIPrKOBFY4jWfZ3f_f9ZyZ5AdFourJ4I_t3KZn3R_RosR1xybcudft0XYYg_Hh-UzutYRqdA8hLX4bgQyVl_ZkrkR_aYfO5jn-ZA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
نیویورک تایمز گزارش داد: نیروهای نظامی اوکراین با استفاده از حملات گسترده پهپادی ضربات سنگینی را به کریمه اشغالی وارد می‌کنند و هدفشان این است که این منطقه را از یک پایگاه اشغال‌شده توسط روسیه به یک کابوس برای آنها تبدیل کنند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 49K · <a href="https://t.me/alonews/131867" target="_blank">📅 12:14 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131865">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">👈
زمین لرزه شدیدی شهرستان بستک در غرب هرمزگان را لرزاند
✅
@AloNews</div>
<div class="tg-footer">👁️ 47.9K · <a href="https://t.me/alonews/131865" target="_blank">📅 12:02 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131864">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">👈
زمین لرزه شدیدی شهرستان بستک در غرب هرمزگان را لرزاند
✅
@AloNews</div>
<div class="tg-footer">👁️ 48K · <a href="https://t.me/alonews/131864" target="_blank">📅 12:02 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131863">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fa11f8e93a.mp4?token=rbyjz5g5AwH4Ypa_Wh3U9dmCIt0beuhNVVMvljlaoE_I6U2xXS1G3UC6mQaxqGCLmAHXYSZu2E39uNYTpTBNIQ-51Ts__rg5MzEUF_U54GQXZxtFSwEPpANUhATjOFL3DV7Jpz_sE9f9yxASYn4MJTq6_SJR2wAvPdilW1GITJT7kYaEMk6begJkfwWLqpmjVFNosYPIx0R2UEquG-B5dT6MsxnL-Aqc0yRUZkswVi2evyFlcHwqL00yAWfHEewFb45dPbtYOjdJkrQZ_hGCD2hUsz1B4eNWzZjYer-IQl0NokaJ_vL5QiZrXzBonAXIrecVJnQ3CaCY4HBR3eih5g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fa11f8e93a.mp4?token=rbyjz5g5AwH4Ypa_Wh3U9dmCIt0beuhNVVMvljlaoE_I6U2xXS1G3UC6mQaxqGCLmAHXYSZu2E39uNYTpTBNIQ-51Ts__rg5MzEUF_U54GQXZxtFSwEPpANUhATjOFL3DV7Jpz_sE9f9yxASYn4MJTq6_SJR2wAvPdilW1GITJT7kYaEMk6begJkfwWLqpmjVFNosYPIx0R2UEquG-B5dT6MsxnL-Aqc0yRUZkswVi2evyFlcHwqL00yAWfHEewFb45dPbtYOjdJkrQZ_hGCD2hUsz1B4eNWzZjYer-IQl0NokaJ_vL5QiZrXzBonAXIrecVJnQ3CaCY4HBR3eih5g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
تصاویر هوایی از مصلی و خیابان‌های اطراف
✅
@AloNews</div>
<div class="tg-footer">👁️ 50.4K · <a href="https://t.me/alonews/131863" target="_blank">📅 11:52 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131862">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">👈
شبکه «فرانس ۲۴» گزارش داد که دونالد ترامپ، رئیس‌جمهور آمریکا، پیش از برگزاری نشست ناتو در ترکیه، با ولادیمیر پوتین، رئیس‌جمهور روسیه، و ولودیمیر زلنسکی، رئیس‌جمهور اوکراین، گفت‌وگو خواهد کرد.
🔴
این رایزنی‌ها در حالی انجام می‌شود که جنگ اوکراین و مسائل امنیتی اروپا از مهم‌ترین محورهای نشست پیش‌روی ناتو به شمار می‌روند
✅
@AloNews</div>
<div class="tg-footer">👁️ 46.9K · <a href="https://t.me/alonews/131862" target="_blank">📅 11:49 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131861">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5b32a145c3.mp4?token=BORB3KBd4or2r48UGkuiBb8ip4vWu_jeXufBVx0RMgSSVgW-dBs3JrSPy-c3jW6X2oUpBCoSQ2biipPONWdjfBfZw52xz2VVA609EpTOyFi5O8oJzcRWTtHJSIQmA2GjRgYYPlivRyIoR-trXCRIZCscxtwRNpo5ecuxRZS_R6Ant5t9cKu51m4ao-6q7zj4pyL7i7gR-jJK5zRjZBwL7pLkRvQXDo41o1HRtffeOnROCuR5W2XJe8ZLZOh5ce7K2YkAUWTgtwJgcFcE2ooXub9QnBSZKUypnslkGI1af0gkKk1_zOxivgc3IWXsmoSyvWfIuZbdnoZSuhRUH7SiHA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5b32a145c3.mp4?token=BORB3KBd4or2r48UGkuiBb8ip4vWu_jeXufBVx0RMgSSVgW-dBs3JrSPy-c3jW6X2oUpBCoSQ2biipPONWdjfBfZw52xz2VVA609EpTOyFi5O8oJzcRWTtHJSIQmA2GjRgYYPlivRyIoR-trXCRIZCscxtwRNpo5ecuxRZS_R6Ant5t9cKu51m4ao-6q7zj4pyL7i7gR-jJK5zRjZBwL7pLkRvQXDo41o1HRtffeOnROCuR5W2XJe8ZLZOh5ce7K2YkAUWTgtwJgcFcE2ooXub9QnBSZKUypnslkGI1af0gkKk1_zOxivgc3IWXsmoSyvWfIuZbdnoZSuhRUH7SiHA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
حضور فرزندان و داماد آیت الله خامنه‌ای در نماز میت امروز مصلی تهران
✅
@AloNews</div>
<div class="tg-footer">👁️ 49.3K · <a href="https://t.me/alonews/131861" target="_blank">📅 11:44 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131860">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">👈
سخنگوی ارتش: بار‌ها اعلام کرده‌ایم که از فرصت آتش‌بس برای ارتقای توان رزمی خود استفاده می‌کنیم؛ یک لحظه را هم از دست نداده و غافل نمی‌شویم
🔴
اگر دشمنان خطایی کنند، حتما با پاسخ کوبنده نیرو‌های مسلح ایران مواجه خواهند شد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 47.9K · <a href="https://t.me/alonews/131860" target="_blank">📅 11:40 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131859">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">👈
کرملین: تماس تلفنی ۸۵ دقیقه‌ای پوتین و ترامپ درباره جنگ اوکراین
🔴
رئیس‌جمهور آمریکا پیشنهاد داد که در جریان نشست سران ناتو در ترکیه، برای پایان دادن به این درگیری کمک کند
✅
@AloNews</div>
<div class="tg-footer">👁️ 49K · <a href="https://t.me/alonews/131859" target="_blank">📅 11:34 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131858">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OD6BEzHVWUtg6UXwIrD_Kd2DxN3xAvydAMdBSDPeImtdFpQWQ4QG2MYiaqqC5fvLlFDeFOs2MPivmjtPjUHoz4vn5EZSiZZhai7cqzvcVPEN_F5YajOHtLXi0IXmoPQVFmgTktU5l0d8hlZtJqDlE_rRTy2e5Haai0lBLIc0hKIysgN9WUfhcnTKxVl4oko_CFwF8t5Gm8626bwdUiILA4HoNDnT4ggnHZX-_mKomhiq2BMIsDE13n9LXHTjZNyIzap1Wpl4zV9ZekiUuO_Jl7Aq3UwVcyUVbfgw9KnZxhUOhvU3C4EdJWsNb49inyn0gor9XOSvJAjKKXHCQ0cIeA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
هرمزلتر: نیروی دریایی سپاه با استفاده از قایق‌های تندرو، کریدور مورد حمایت آمریکا در تنگه هرمز را به طور کامل متوقف کرده و در نیم روز هیچ شناوری از این مسیر عبور نکرده
🔴
سپاه صبح امروز از طریق بی‌سیم به تمامی کشتی‌ ها هشدار داد و همزمان قایق‌های گشتی نیروهای ویژه را برای اعمال کنترل ایران بر تنگه هرمز مستقر کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 50.2K · <a href="https://t.me/alonews/131858" target="_blank">📅 11:26 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131857">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">👈
وزارت حمل‌ونقل قطر اعلام کرد فعالیت‌های دریایی از یکشنبه از سر گرفته می‌شود
🔴
این وزارتخانه ۸ تیر از همه شناورها خواسته بود تا اطلاع ثانوی تردد و فعالیت‌های دریایی را متوقف کنند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 47.9K · <a href="https://t.me/alonews/131857" target="_blank">📅 11:22 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131856">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">👈
ترامپ : ما هنوز هم پرچمی رو داریم که بعد از غرق شدن ناوگان اسپانیا در خلیج مانیل
🔴
روی ناو فرماندهی آمریکا برافراشته شد؛ یکی از بزرگ‌ترین پیروزی‌های دریایی تاریخ
🔴
همین چند وقت پیش هم کل ناوگان ایران رو با ۱۵۹ شناور به قعر دریا فرستادیم
🔴
همه این‌ها توی مدت خیلی کوتاهی انجام شد؛ انقدر سریع که باورکردنی نبود
🔴
ما قدرتمندترین ارتش دنیا رو داریم
🔴
از ارتشمون استفاده کردیم و نتایج فوق‌العاده‌ای گرفتیم
🔴
به ونزوئلا نگاه کنید، به ایران نگاه کنید؛ ما نابودشون کردیم، ارتششون رو از بین بردیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 51K · <a href="https://t.me/alonews/131856" target="_blank">📅 11:10 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131854">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/kPq_S3p3Dbgb6Yn0WWQm7OuSzK5OM6dzoQRz9CK8K0xPeJi4tPcSVi0VwawQy9lQre4G8urNWdt6Lc_6U5SCx6Og5Mm_JXjikyoQs7mkhUAtNNkpQi6ZKWngvsK7mhVVolexrce2_G5angPkPmohfV1gElJb3Jb9gB25YuUTL96fqK_NLMkl0PA-c9J9uk4thK1l-4PfQb9NQEVkEjntrq6JePQD1r0R4RA5aS6SbEuMhxYvTzG-OkvkKQGKYn48_NVhcVdTKtAnzOt0H0TkhGV_uMalo04WBTwdbfkv-UGQeGflt3CeluyNCXU2iat-ovjheHRZgXFepltDVi91ew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Mb25OjssJNQyiR-TcJsE0stBudFW3djBh7NmnAgydPpz5-hhW-_TEGo3Zque7wmDgrUX9Us9sQ6uRv-e_zOPsKmUXPDuT21_GLBNzZNG9zfvFj8LwcyYh6lztH8VNFnzxao2Grl8fHK-71k0ApzQb3PPBKd0KLsCXmlIeVujhFC_HikT_FIPFpXB7ZEO5rlFYdVsFM7iwR1XqkTmxfpaDfo00ATxASIckxekWOjxtV4e5tOLe0k0tT772EVifOB3lGpKFyGIreLIsp3Xry9EkQ7zGRddMOlDLAfHHP5wIfG68dqyVn8DDBsIB25KNUcscHnpOKcZ26zddwnW9Fy8Nw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
نخستین تصاویر از بوئینگ‌های ۷۷۷
عربستان که به‌تازگی وارد ایران شده‌اند
🔴
بوئینگ ۷۷۷ یکی از موفق‌ترین هواپیماهای پهن‌پیکر دوموتوره جهان به شمار می‌رود که برای پروازهای میان‌برد و دوربرد طراحی شده است.
🔴
این هواپیما با بهره‌گیری از موتورهای قدرتمند، سامانه‌های پیشرفته ناوبری و مدیریت پرواز، به یکی از ستون‌های اصلی ناوگان بسیاری از شرکت‌های هواپیمایی بزرگ جهان تبدیل شده است.
🔴
خانواده ۷۷۷ به دلیل مصرف سوخت بهینه، قابلیت اطمینان بالا و هزینه عملیاتی مناسب نسبت به هواپیماهای چهارموتوره، همچنان از محبوب‌ترین هواپیماهای دوربرد جهان محسوب می‌شود.
🔴
هواپیماهای واردشده به ایران از نوع بوئینگ 777-300ER هستند؛ پرفروش‌ترین و موفق‌ترین مدل خانواده ۷۷۷
🔴
این هواپیما به موتورهای GE90-115B، قدرتمندترین موتورهای توربوفن نصب‌شده روی یک هواپیمای مسافربری، مجهز است و با بردی در حدود ۱۳٬۶۵۰ کیلومتر و ظرفیت حدود ۳۶۰ تا ۴۰۰ مسافر (بسته به چیدمان کابین)، برای انجام پروازهای طولانی و بین‌قاره‌ای طراحی شده است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 52K · <a href="https://t.me/alonews/131854" target="_blank">📅 11:02 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131853">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">👈
وال استریت ژورنال: ایران، روسیه و کره شمالی، در نحوه تعامل با بازار ارز‌های دیجیتال، ایجاد رمزارز‌های اختصاصی خود و پلتفرم‌های معاملاتی برای دور زدن تحریم‌ها، بسیار پیشرفته‌تر شده‌اند
🔴
تهران و مسکو از ارز‌های دیجیتال برای خرید پهپاد و قطعات یدکی تسلیحات استفاده می‌کنند
🔴
ارز‌های دیجیتال به این کشور‌ها امکان می‌دهد تا از سیستم بانکی سنتی عبور کنند
🔴
مقامات غربی به سختی در تلاش برای همگام شدن با این وضعیت هستند
✅
@AloNews</div>
<div class="tg-footer">👁️ 53K · <a href="https://t.me/alonews/131853" target="_blank">📅 10:46 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131852">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">👈
گزارش بلومبرگ حاکی از آن است که روند عبور و مرور کشتی‌ها از تنگه هرمز، به‌ویژه در امتداد سواحل عمان، روز یکشنبه به شدت کاهش یافته است
✅
@AloNews</div>
<div class="tg-footer">👁️ 55.1K · <a href="https://t.me/alonews/131852" target="_blank">📅 10:31 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131851">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">👈
آتش‌بازی‌ها در واشنگتن، به مناسبت دویست و پنجاهمین  سالگرد استقلال ایالات متحده
🔴
ترامپ در توییتر نوشت: بهترین آتش‌بازی‌ها در تمام دوران
✅
@AloNews</div>
<div class="tg-footer">👁️ 56.2K · <a href="https://t.me/alonews/131851" target="_blank">📅 10:21 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131850">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">👈
گزارش خبرنگار ان بی سی نیوز از مصلی تهران
✅
@AloNews</div>
<div class="tg-footer">👁️ 57.6K · <a href="https://t.me/alonews/131850" target="_blank">📅 10:08 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131849">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/F7xbowJxtdZWQjR8VOiT78-bJQjUAEJe-1niFzMxX6_PUBuzB5KyEyzM8UsFJSBF51X_c1ErwZuNIOajbTnWvQoaSe8ybEWhYqcWg-5UUm3JEhdwTvDNSsVuQ6x9eFP6m7LGQtCAFCfCK-TH5vf5age_06lLhfE3oDI2KPRVXRVrQb9TatZUQeNXg6xpVOFOEeiqPkqRvdqylacymkaBktu9W53g2guAO8KV-n23b6iTPxnJemmoAsjZ-Ofwe8vkUd7KfHeuKQx8Qn1QU4LTg7ISAi6V7cYMHY6pvpZuabq06Sqc-F2T-0V9HMo41vIgDqENKmKTI0cBmGwH59BAug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
اکونومیست: آمریکا هنوز یک قدرت بزرگ است، اما دیگر مانند گذشته بر جهان مسلط نیست.
✅
@AloNews</div>
<div class="tg-footer">👁️ 57.2K · <a href="https://t.me/alonews/131849" target="_blank">📅 09:59 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131848">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">👈
ترافیک سنگین در ورودی‌های پایتخت
🔴
ترافیک در محورهای چالوس و هراز در هر دو مسیر رفت و برگشت سنگین است.
🔴
محور قدیم بومهن–تهران و آزادراه قم–تهران در ورودی‌های پایتخت با ترافیک سنگین مواجه هستند.
🔴
تمامی محورهای شمالی کشور فاقد هرگونه مداخلات جوی هستند و تردد در آن‌ها بدون مشکل جوی در جریان است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 57.2K · <a href="https://t.me/alonews/131848" target="_blank">📅 09:50 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131847">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">👈
رئیس شورای هماهنگی تبلیغات اسلامی: امروز در تهران آمادگی اسکان نزدیک به ۳ میلیون نفر را داریم!
✅
@AloNews</div>
<div class="tg-footer">👁️ 58.5K · <a href="https://t.me/alonews/131847" target="_blank">📅 09:31 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131846">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/aa2c1939de.mp4?token=kliw0VpCoo6DFPpS6-qoXL-1VAExrqkc6VPxCLd4DyfkK8GuIm0AIlLyI33nG7IeKNhfLrM5YIdwIYB1Lizq4eiIWUt_21wb77ILlnYIuTpgG3QGYboymjNNKLN5fkmfNBnt-VdDeaSZDVh6b4T7IxzPi03ju3exjAf7WklJfmXHFgP_I23cGZUaQDzlXJJ7RPxgoIPGcaGWJfL6RW7WU8xodUMPZ7ucHvzGKGscrO6xdUc6E9wQRSHn7wooA_H7mqYKiUnJd11EViy6J2gZlmMHTtliuj_vkKwAueT6OEp4dg6bbXwVmxxsTQWA6ADdlzaAGoW70mcVIYd6BXE1-Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aa2c1939de.mp4?token=kliw0VpCoo6DFPpS6-qoXL-1VAExrqkc6VPxCLd4DyfkK8GuIm0AIlLyI33nG7IeKNhfLrM5YIdwIYB1Lizq4eiIWUt_21wb77ILlnYIuTpgG3QGYboymjNNKLN5fkmfNBnt-VdDeaSZDVh6b4T7IxzPi03ju3exjAf7WklJfmXHFgP_I23cGZUaQDzlXJJ7RPxgoIPGcaGWJfL6RW7WU8xodUMPZ7ucHvzGKGscrO6xdUc6E9wQRSHn7wooA_H7mqYKiUnJd11EViy6J2gZlmMHTtliuj_vkKwAueT6OEp4dg6bbXwVmxxsTQWA6ADdlzaAGoW70mcVIYd6BXE1-Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ: ما به زودی به مریخ خواهیم رفت
🔴
ابتدا به ماه و سپس به مریخ خواهیم رفت
✅
@AloNews</div>
<div class="tg-footer">👁️ 59.2K · <a href="https://t.me/alonews/131846" target="_blank">📅 09:25 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131845">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/imJcJNzl9GhbsH_y4DbnHFJGa1zoBELPFfD2O_h0axEbeepvp2O_OD_7kpiixTTJGP5PnfvsCuiNO-UDmEBKDDvwAapqbB5eGkKiZJ-iHXrSMr5M38xmRNFsazAPWrVGKNOm1WSx68Vx1Q03X84t5nqEi0dOJsxzhZorvzzH_JLNrhzxJHsvPvzyFVTZIHAvel9B7JP7u28y9bRzrmhA71zOrYYvg48Bj1D2y3U7Jvp4IPOv7nqpkEGCZ4RXI8znuja-LYQJhRm30gZnoaqa7agtGP40uza1vkDRryODU6xEgN5RK-0T1uxuXchuVA8UxI4aSOhR_WCgE-OVLGCOWw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
تصویری از خیابان‌های اطراف مصلی تهران
✅
@AloNews</div>
<div class="tg-footer">👁️ 61.3K · <a href="https://t.me/alonews/131845" target="_blank">📅 09:13 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131843">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/mnY8Ki6KjtVFnHPATVBYODaMznKNkxSp18gKF2zlA9yWO3gTR9wtHF7XMIDtQJVZ-o9xJmvn5X3j2oPRWZD84n47iQ0zt_s4eQHB2b93PGOj6mv8DHGCPCcG_tZXiQ3Ugh6rp5DrsBPNZYWJrLvCagsds0blR9QqvZWZB7wlD487QVWS60_YF0O0s6ufwzwvTOjwMBs9mXFs5jAOgkSXOg4Xr7iuxxoZNPa9RoPd-wQa-AW5TP5B-zBZKmMITG797vWdXnA_TTcwExH0WX-S-4cLzeB6WjOyh3n_nxJgcssCGEYbrucfs1SjNIOMu1N99wQfcdAflpYPeIHHlNkNYw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/rTjceXbkj5_mhyE8OrvgXarxuXoRBPeCd-nXlrzcHrzG8foxuZ_6n_UckuY5kjYOBkw4H_fY-7hXi9DK6KON8lTfIc155p6R1a44yySXKp7W9QLW8et34OySf4mtaplo4o1iI-jZJwa42A-QYefxBVLut77z6PLGp1VCbYHr-Uo2ZPUY4nHhHG4O6HLih-xpeBsbvdGXdXKIZjVQCqZapkPyWYz9xabo0ncuFU3VeFyWIsLjlrZgqHExoYLUOWhvF0QLX8xU_eWyNSk0oaQ3fEgu8BJC_fMLeCBgxb5uU-t5VONSj-Bu0-AeBBjF4yDO8oYtL4EdCL3S-lTZN0msQA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
جنگنده های SU-34 صفر کیلومتر نیروی هوایی روسیه
✅
@AloNews</div>
<div class="tg-footer">👁️ 61.3K · <a href="https://t.me/alonews/131843" target="_blank">📅 09:10 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131842">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">👈
پوتین به ترامپ زنگ زد و ۲۵۰ سالگی آمریکا رو بهش تبریک گفت
🔴
همچنین پوتین ازش دعوت کرده که به روسیه سفر کنه
✅
@AloNews</div>
<div class="tg-footer">👁️ 60.3K · <a href="https://t.me/alonews/131842" target="_blank">📅 09:05 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131841">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">👈
زلنسکی : با ترامپ صحبت کردم
🔴
احتمال واقعی برای پایان جنگ با روسیه وجود داره
✅
@AloNews</div>
<div class="tg-footer">👁️ 60.3K · <a href="https://t.me/alonews/131841" target="_blank">📅 08:59 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131840">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">👈
وزارت دفاع چین: پکن و مسکو در ماه جاری رزمایش دریایی مشترکی را در نزدیکی شهر چینگ‌ دائو چین برگزار خواهند کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 61.3K · <a href="https://t.me/alonews/131840" target="_blank">📅 08:53 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131839">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dNSx7BZkG4UhXdUXspLAvVpbsTYuBBLFnwZHygxL8pQJzVJvdKGp5zModaT81Ieql9feydeTeBznMcV0V7wpneVqeZgw3rxCIMFkOK6iikzAswq3WISznpcxp__U7dK2MaVSwm312-qSFLBdMD5jtFwUgSIs41P-Eq0A2n0NxCtr3AflB9qlbleJ11AVFUFUd_JinnThtzPgnd6qv7g_WBGYArF-9cIuhpGpkTXoc_jrJpToUn-YjDmnoDnzJO0vAJz3qVAj6jx3d9aUMa28sLY9GBJpjJbeYatEbBE9EUJfNJ2BtHylA9ga33GL6ALUYbsXoidoXwb7TSiivUFmIA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
دیدار هیات نمایندگی حزب‌‌الله لبنان با عراقچی
✅
@AloNews</div>
<div class="tg-footer">👁️ 64.4K · <a href="https://t.me/alonews/131839" target="_blank">📅 08:49 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131838">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">👈
ترامپ:همه جای دنیا تلاش میکنند شبیه ما باشند؛ اما هیچکس نمیتواند مثل آمریکا باشد
✅
@AloNews</div>
<div class="tg-footer">👁️ 65K · <a href="https://t.me/alonews/131838" target="_blank">📅 08:45 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131837">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">👈
طبق گزارش ها شب گذشته پوتین و ترامپ در تماس تلفنی یک ساعته در مورد ایران و اوکراین گفت و گو کردند
✅
@AloNews</div>
<div class="tg-footer">👁️ 65.6K · <a href="https://t.me/alonews/131837" target="_blank">📅 08:40 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131836">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1c3c08acdf.mp4?token=Do1f6gFterKMKmEXOnSp0q0HPngZSlYTukSE9Zj-pQNWfkiMbXAYnt0YxChSBGvcTv2bLNGA2klYE1KeZtsN514fJqZruSMOXOw8mPccysfgNHqcGTCUqsruAzIiO5Oj35aN6-Gg-26YyYnwADFTdVFDq7zpvyIRYrpzQPMTHqGlhAiW6381rTRA19vLS_Kuk4WNV-HSFKSP2f-Qd14rCjlXekb_RPkY-7jLqliNh8kEjbOjjR5nmpIyBfDPzXoer2W4APcmtHZAU30THYnR4rFzQY7F3QRfB4Jj3MG_z8BM85nzCsseonv3r5b8UrEK6kCiLXYr1mv_hok-bsLTfw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1c3c08acdf.mp4?token=Do1f6gFterKMKmEXOnSp0q0HPngZSlYTukSE9Zj-pQNWfkiMbXAYnt0YxChSBGvcTv2bLNGA2klYE1KeZtsN514fJqZruSMOXOw8mPccysfgNHqcGTCUqsruAzIiO5Oj35aN6-Gg-26YyYnwADFTdVFDq7zpvyIRYrpzQPMTHqGlhAiW6381rTRA19vLS_Kuk4WNV-HSFKSP2f-Qd14rCjlXekb_RPkY-7jLqliNh8kEjbOjjR5nmpIyBfDPzXoer2W4APcmtHZAU30THYnR4rFzQY7F3QRfB4Jj3MG_z8BM85nzCsseonv3r5b8UrEK6kCiLXYr1mv_hok-bsLTfw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
پویانفر
،
مداح
:
آقایون
سیاستمدار، بسه دیگه...!
✅
@AloNews</div>
<div class="tg-footer">👁️ 76.3K · <a href="https://t.me/alonews/131836" target="_blank">📅 03:31 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131835">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cd6157bafc.mp4?token=vD3LKzhXdnYrazik4pTAVO7YyKO7Nl3gMFG_iRvGloRMMrlA3hSX6eUFHBs4qBzto5M-ksjNOs6sMa_-S1Mi_AzNjqUPCGfTTF4xCvJn9NS93mu7FIpFBF6HaZD8OP0J3QLITsVobe2psPj9R55gUBzi-hmRsqpSwwF-csfiD05QKTbn3yRoWzMSbJgdJ_IsCQreb6lScaDRn2xN29TFZl8mwRqnZkVxYJZnYvCcRJDujk0pRhwjphO_I18N28pCJCs_g49s3QaLTJu1c8oykKVld2tWePu07gVegIrK-UxQYBp-0MpuCTe018F-k5uUisxRNF4d22_Pc5kmrhaxww" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cd6157bafc.mp4?token=vD3LKzhXdnYrazik4pTAVO7YyKO7Nl3gMFG_iRvGloRMMrlA3hSX6eUFHBs4qBzto5M-ksjNOs6sMa_-S1Mi_AzNjqUPCGfTTF4xCvJn9NS93mu7FIpFBF6HaZD8OP0J3QLITsVobe2psPj9R55gUBzi-hmRsqpSwwF-csfiD05QKTbn3yRoWzMSbJgdJ_IsCQreb6lScaDRn2xN29TFZl8mwRqnZkVxYJZnYvCcRJDujk0pRhwjphO_I18N28pCJCs_g49s3QaLTJu1c8oykKVld2tWePu07gVegIrK-UxQYBp-0MpuCTe018F-k5uUisxRNF4d22_Pc5kmrhaxww" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
زاکانی و برخی از مسئولین تو حاشیه مراسم امروز رفتن چلوکباب خوردن
🔴
مردم هم اون بیرون زیر آفتاب، صف وایسادن تا غذای نیم پرس و تخم مرغ آب پز بخورن
✅
@AloNews</div>
<div class="tg-footer">👁️ 81.7K · <a href="https://t.me/alonews/131835" target="_blank">📅 02:55 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131834">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">👈
کابینه امنیت ملی اسرائیل، احتمالاً فردا عصر تشکیل جلسه بده
✅
@AloNews</div>
<div class="tg-footer">👁️ 75K · <a href="https://t.me/alonews/131834" target="_blank">📅 02:51 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131833">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1a14033e54.mp4?token=VFWYdqvFty-G_26YwuQCGmxL0v-B64eoB5MoBpAMST1pQGd_p43ituNk8GX6jSIj6mAOcPlLv7OoCeFvoW134YorF5PwIvDblAG4IMvi_d815Xnd8C4plnAozWHteW1Cq_GoBxenmJYANIYiQ3xPO15hiCS1wGH2R_myNj58Bk5c8J_f48jAp_e7pPXOauhwdKGjz_YYKfha1najOqWPM7BFKpqZ8Xug4hplJTwabTJyFIrVfiG1L4osZ8yo0E4PPu6PqlWzqYj6kXXqL8_faPqWmh70OqDBRhjVP4_L1zwIyXBCL3yaIig0QelacGa52kOYj3l6CF3mDO46iVxpLxUC5d76YGhNRiwYytWje3LKmmPueiq7QWf01grVh30edBMsCL4oj_YeqMoHMOO8xz0HbPcwVwqgtvl8kVBZgHy8KUVwKc9OC3hhJ1BcneDgo_3mXTSFeWyKg5cvIzmTvgM0gl2QX8QvjJzAqn_yHccBwWoA0gRqyXRcTHqswThorcR_BqbBqEBpb-n0U4DMcXML58rb9CG6od94sFNfsOq8Tb6tNWiKqjKd8QVBXkzOQKIon-yOEW_z1Lph_gghGqkQ1-bWbSdLVQGr2FGfZQEIVGTOPiofOlJ8GWZX72ejDWJvLQiwf5jFKr-Oer-844aNL0G0XMmlq0pkMMMZoyM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1a14033e54.mp4?token=VFWYdqvFty-G_26YwuQCGmxL0v-B64eoB5MoBpAMST1pQGd_p43ituNk8GX6jSIj6mAOcPlLv7OoCeFvoW134YorF5PwIvDblAG4IMvi_d815Xnd8C4plnAozWHteW1Cq_GoBxenmJYANIYiQ3xPO15hiCS1wGH2R_myNj58Bk5c8J_f48jAp_e7pPXOauhwdKGjz_YYKfha1najOqWPM7BFKpqZ8Xug4hplJTwabTJyFIrVfiG1L4osZ8yo0E4PPu6PqlWzqYj6kXXqL8_faPqWmh70OqDBRhjVP4_L1zwIyXBCL3yaIig0QelacGa52kOYj3l6CF3mDO46iVxpLxUC5d76YGhNRiwYytWje3LKmmPueiq7QWf01grVh30edBMsCL4oj_YeqMoHMOO8xz0HbPcwVwqgtvl8kVBZgHy8KUVwKc9OC3hhJ1BcneDgo_3mXTSFeWyKg5cvIzmTvgM0gl2QX8QvjJzAqn_yHccBwWoA0gRqyXRcTHqswThorcR_BqbBqEBpb-n0U4DMcXML58rb9CG6od94sFNfsOq8Tb6tNWiKqjKd8QVBXkzOQKIon-yOEW_z1Lph_gghGqkQ1-bWbSdLVQGr2FGfZQEIVGTOPiofOlJ8GWZX72ejDWJvLQiwf5jFKr-Oer-844aNL0G0XMmlq0pkMMMZoyM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
جنگنده‌های
F/A-18E/F
و حرکات نمایشی تو واشنگتن برای ۲۵۰ سالگی آمریکا
✅
@AloNews</div>
<div class="tg-footer">👁️ 77.4K · <a href="https://t.me/alonews/131833" target="_blank">📅 02:44 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131832">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DnPzzVlY_SOtF8ZIYajn1yFW-5NYajPUff_xnHp6SsL5e5AEKvY-hq18ONn93A7uH9nCSydaVI86d97Ak44cVcOWrjJUJr65YIADxVA19TQKN8w7N3g4kVxGLpXXwBFtCcjOjcAQnjNrX8PPihoLN0w7eBFH-5KGUtMq2kCY5pOavTohNp_SCOX1YlTEE1o7aKoE3Rf9qgCsb76WlHtECv4DmtAExcd-eYlc9e9EHh-NO6988jp7Xe2nq2Wby-dO5Gxp9prQAeac0wugM9QZW1fV7GvywHd-CimjZDZgkHwhzBUl2Mx1Nf-A36YLUiCSksMzxaUGFp86mtZm46lDjQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
گویا کامیون حمل پیکر آیت الله خامنه‌ای مبلغ2,298,000 هزار تومان خلافی داره
✅
@AloNews</div>
<div class="tg-footer">👁️ 80.6K · <a href="https://t.me/alonews/131832" target="_blank">📅 02:37 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131831">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cXl7kefGJPy1T9hKQpJv2Yct7NezMVerUtujqFE7szsndlv6v3wg1zDApKS2LU4b1SVpC5GXNa2KEY6PW0JzMAJ3DdGJajXueo_4ph9jrbZsFnmNi64Mo_L7qSgtlRy9ddwHEK3RJtT3zCgXCV49pOQu8XYEmLUGESY0gCzhwukdwUmn3Lk3I75FFGAu1vT8yeuBIYFskXro1GXK2H6HoOb0pYAPTu_hqtCGcyck2sZZYO92gsk_ig4wqRGD_kiARHKVz0aGfTqnS7SKFYbcXdQVs158nRwwcwHXCFDuPccQxiXt-wEyiMS-5AeVwqsStJa1ZaqRubkPKC0JBwjlTA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
پوستری که برای کشتن ترامپ امروز در رسانه ها و در دست مردم حاضر در مصلی دیده می‌شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 76.5K · <a href="https://t.me/alonews/131831" target="_blank">📅 02:32 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131829">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cf04045170.mp4?token=sA9pQX-ld6RbmrnjfHbNJzW5Xd_9A365s6AF32EqeGobyqukW1D2l6i-yJ0ICuTkPFQoWpNNUZhOZSYfymROw4cOnloDYyayPZb1Rz5tEmMMnm_AMEdaECZslNvu60wJ4R8sbfqllJiwqrc-2NoUMJkx4g0mnqYitAX3u18do1PfCSgal4gitLHt5nIXLUv_-gmxjScvqimWLctFMapTO5kU1Sk8oTC81rDfu7zEo1AVxdiVbTmmGHdtbU3q4VU8wvwc-BCDmA0E2ZL6lvFDdDOWtwhYGON8jkk59OgCiQL-os1cJjEVZOM4Hni51H-OkKmTSF91ZCddIpwpybNznQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cf04045170.mp4?token=sA9pQX-ld6RbmrnjfHbNJzW5Xd_9A365s6AF32EqeGobyqukW1D2l6i-yJ0ICuTkPFQoWpNNUZhOZSYfymROw4cOnloDYyayPZb1Rz5tEmMMnm_AMEdaECZslNvu60wJ4R8sbfqllJiwqrc-2NoUMJkx4g0mnqYitAX3u18do1PfCSgal4gitLHt5nIXLUv_-gmxjScvqimWLctFMapTO5kU1Sk8oTC81rDfu7zEo1AVxdiVbTmmGHdtbU3q4VU8wvwc-BCDmA0E2ZL6lvFDdDOWtwhYGON8jkk59OgCiQL-os1cJjEVZOM4Hni51H-OkKmTSF91ZCddIpwpybNznQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
حمله مجدد تندروها به قالیباف
‼️
🔴
تو چرا اسم بچه‌هات ریشه یهودی داره؟
✅
@AloNews</div>
<div class="tg-footer">👁️ 77.4K · <a href="https://t.me/alonews/131829" target="_blank">📅 02:04 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131828">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/K46Bo_fGKRWtR_8JJTNWrnKizEtgy8JX2svlhbadA1x3nwUs4AXKOhsiaQTXO44erwag-obQr6TYhczTzNaEvGworIOZGuIoWRlocx6N94naPwiHMpNuP-TFxH0I8IWVUn375R6aHVsZmTeiJJRp4yjZYkJ4Hwas0Sch8-xpqQ4Br52BvOs6mtfs5zYFz15-wvYWnLwb1wb6j5uVJx4p6YAY-qeTD1hqYNDLpTAODligB492CwUE66K9MSBwMtQQdzav-dBTPfn8l2HpaSsjSvpyjm-md8KR6LPEIHPm-lDpxgMcvbRNpQVeows1K82Fsht3pFppCVx_L_5Cd3_WYA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
نیویورک تایمز: مجتبی خامنه‌ای در تلاش است تا در تشییع پدرش شرکت کند اما مقامات امنیتی مانع هستند
✅
@AloNews</div>
<div class="tg-footer">👁️ 80.6K · <a href="https://t.me/alonews/131828" target="_blank">📅 01:56 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131826">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">🚨
از ساعاتی قبل تصاویری بسیار منشوری از آرام جوینده همسر سپهر حیدری، اسطوره پرسپولیس درحال پخش شدن است
◀️
مشاهده فوری و بدون سانسور</div>
<div class="tg-footer">👁️ 81.1K · <a href="https://t.me/alonews/131826" target="_blank">📅 01:40 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131825">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7d2bbcff1e.mp4?token=QdsIDduApGHo_5yUAT37STB3KqeW_rT3CNlppaUQkboOHDvop4MS2ckQ2efG3wO7kQgmKSaR2UNQ1zWcaeF8_aC0lf_iq6muLl4wnSwV2BP6hwH4UB5Qu5HhUmy9NfyhO3OlX_GN-7pEDBNSQQXHWD5TkmvkwDAC-Ign225kPpNrpcpy37-cIy9HgAer44oGZV4eVSHIIyb69kRcyHyfggH94sD3gGAWam5p-kTaAxV3ND-5PBGsu1z5_GfQxjoyRip9xmIHmQiFAnHLEJih_wOpy-sboYKtq613oPMIh_rIRAgk7_kp_XTjiz4NE49TMF6fgadALzFPPRazZ8G30w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7d2bbcff1e.mp4?token=QdsIDduApGHo_5yUAT37STB3KqeW_rT3CNlppaUQkboOHDvop4MS2ckQ2efG3wO7kQgmKSaR2UNQ1zWcaeF8_aC0lf_iq6muLl4wnSwV2BP6hwH4UB5Qu5HhUmy9NfyhO3OlX_GN-7pEDBNSQQXHWD5TkmvkwDAC-Ign225kPpNrpcpy37-cIy9HgAer44oGZV4eVSHIIyb69kRcyHyfggH94sD3gGAWam5p-kTaAxV3ND-5PBGsu1z5_GfQxjoyRip9xmIHmQiFAnHLEJih_wOpy-sboYKtq613oPMIh_rIRAgk7_kp_XTjiz4NE49TMF6fgadALzFPPRazZ8G30w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
قدرتنمایی جنگنده‌های ارتش بر فراز تهران
✅
@AloNews</div>
<div class="tg-footer">👁️ 87K · <a href="https://t.me/alonews/131825" target="_blank">📅 00:54 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131824">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/78f30f9eab.mp4?token=SgSEU5T2pVZkikhvBKMSreWQSHZ6hAp0FnECYfAIu5edOYZNip_hB3qWJK3dh841jyo6HKSG7UcFLTdt62dHjD3EcV453Pl4be84m7qPNybQXY2nx5jl46Bqb9I6cKICN7Oxl_I3XX1Bz5q7AoH4q-q8sIcBUVjfsKJ3NjwBv2wAXNAm9BRjD3fjcU1l_Fgkd1ZiNweV1hMj-pkhJWoLFl2Q4tbpshNmHxE4JpR3PoSW-vp4Ns1gf74ixJpCIb0xCPXT8oFh6f28I1oj6OuLVvhok1iWji1hzB4-r6G3_EnXmZdlfkGimfHKnP8Fhu7XTmkRkQTTYhP1fbT75FELcA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/78f30f9eab.mp4?token=SgSEU5T2pVZkikhvBKMSreWQSHZ6hAp0FnECYfAIu5edOYZNip_hB3qWJK3dh841jyo6HKSG7UcFLTdt62dHjD3EcV453Pl4be84m7qPNybQXY2nx5jl46Bqb9I6cKICN7Oxl_I3XX1Bz5q7AoH4q-q8sIcBUVjfsKJ3NjwBv2wAXNAm9BRjD3fjcU1l_Fgkd1ZiNweV1hMj-pkhJWoLFl2Q4tbpshNmHxE4JpR3PoSW-vp4Ns1gf74ixJpCIb0xCPXT8oFh6f28I1oj6OuLVvhok1iWji1hzB4-r6G3_EnXmZdlfkGimfHKnP8Fhu7XTmkRkQTTYhP1fbT75FELcA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
یه زمان کوچک زاده تو مجلس یقه جر داد که من به عنوان یک ایرانی راضی نیستم یک قرون از مالیاتم جز غزه خرج جای دگ بشه
🔴
بچه‌ها شما به عنوان یک ایرانی راضی هستید یک قرون از حقتون اینجوری کف خیابون ریخت و پاش بشه؟
✅
@AloNews</div>
<div class="tg-footer">👁️ 86K · <a href="https://t.me/alonews/131824" target="_blank">📅 00:45 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131823">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">👈
قالیباف: اسرائیل رو نابود میکنیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 83.9K · <a href="https://t.me/alonews/131823" target="_blank">📅 00:38 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131822">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/t4bck1aKPuLWgzzbLcFmYDkjJiPfHxBdMw-1WyudTbTY_xr4AIza1w7Yk9l0kJk9FKLe8PTXkRX1XRrBqp9FyVMa0k67HW-_aTc7jtzV3rX3bAcQa_LKezMZPaFigiIOuF_YfDYtArXvlTpKUL1pkC1sLFFqDMdvJpEMwQKLpUsLTiN9btpFk744A2Yb-vJHfIvjaPKCzbkTTCMjX_9HjFXvWxDeHmukBiKUMOW8DJ6IUTeoBLsnCUQTjfhBmE5umI2Q3nSZZml6KezUJVNa1BNiEv-GlsNFbx2aYEekbktveWe46HEBuKLWazXESmUJd7d2BLh0hWHb-f4YEUsz4A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
بیشترین چیزی که ایرانیا تو ۴۸ساعت اخیر دیدن
🔴
هر ۵ دقیقه پیامک میده
✅
@AloNews</div>
<div class="tg-footer">👁️ 85.6K · <a href="https://t.me/alonews/131822" target="_blank">📅 00:21 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131821">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2f7e4c4447.mp4?token=g0TLEzueBnG05BBiqtgT3yLDOn1qIsG9nE6qVpZ_wgTJXG4vxsFs6CUTfPB0KFJEEUvcOO_jQ2Ugv2hN0Q_jDhKjM00b--vnnTTdWDKFlWCj0LMK_zRuUII1Helcjrw2C5mOxe2dYJpz-J5qo6VUWRmlX2zG3-4MUc9zii-UWqALCDCC2wj3Dbc8tCBZ_iUk0JDb49DZg1Mtrm1ezBhvInKjK0ZAiRLEBFgkPIzRtP8wv5hcTYFDhYU1uDgxwtf3_11WHQLG_BiZq9hC10lP4lpmBuKmCHAyGt76y5bLf50y6kxE7uNXZ3Ybql9Wsv8OIZY4egpTa8ti9CAhI2T1-w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2f7e4c4447.mp4?token=g0TLEzueBnG05BBiqtgT3yLDOn1qIsG9nE6qVpZ_wgTJXG4vxsFs6CUTfPB0KFJEEUvcOO_jQ2Ugv2hN0Q_jDhKjM00b--vnnTTdWDKFlWCj0LMK_zRuUII1Helcjrw2C5mOxe2dYJpz-J5qo6VUWRmlX2zG3-4MUc9zii-UWqALCDCC2wj3Dbc8tCBZ_iUk0JDb49DZg1Mtrm1ezBhvInKjK0ZAiRLEBFgkPIzRtP8wv5hcTYFDhYU1uDgxwtf3_11WHQLG_BiZq9hC10lP4lpmBuKmCHAyGt76y5bLf50y6kxE7uNXZ3Ybql9Wsv8OIZY4egpTa8ti9CAhI2T1-w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
یکی از متولیان مراسم تهران:
تابوت حضرت آقا، یخچال قوی هست
✅
@AloNews</div>
<div class="tg-footer">👁️ 84K · <a href="https://t.me/alonews/131821" target="_blank">📅 00:10 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131820">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/byE4pv8S-GYhr2I5mWxJDRGFgodMk8yqe8ckpB6MisSHrLrEJwkOdVRl_05Y64cc6lcVq9AF_ttYKjgXN79CUlGPI_53n2AVJV0q-3SZREtG9mO-gY82gp1M5zxJtWThcPWedoDHaHT4aE_HEyzF5mExvq0nvOKJfLfWZe1oKcJB4NstXP1SPWcLJXmTjD2Tk4ESX67nSbZl_SaNWY0oVnvQ6YqTO5URXlbdM6EEY3E2s5i7LJ1wuF9ZZIFzWUyTEME_C2Q-FZlBca7-vQCG1zl_50IrVDQhx2OrJXBNXMpupSFiaSzDPE_13azrBa5AIc0vJnnUZOvllrwQKo-Sdg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
رسایی: اینترنت رو قطع کنید
✅
@AloNews</div>
<div class="tg-footer">👁️ 79K · <a href="https://t.me/alonews/131820" target="_blank">📅 00:03 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131819">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/j9mZDZ47BgoW95RlhVgkxLvsgnEPsF_OEHDj6__OZH1SKsntb20SvJT0bCJmvYOjS2qF8sU4f8POF9QhAj6q7AkreNk_6Gm2FTzc3IWD4yVvaOcoedEXWI8ip-ColAkwv5t-yO2ZgnAFT5j29hJCTfJDXEb__Xn3tlYmSjvAotlAz3BfaVxcIWZFCAg0RbewvFcACY2alravQEgEhNbhW9Q4kLCQKyAvVma1mC2qghPvyFl42V1em-HFw73bkcF5APgJ-WTPZcJQagWwcqz_2dIF3dECxvLW-yg6GydG4hwHtYq8VMfBgn8EgC92wTlBOAlo8a-E95y3A_jgyuUfvQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
نیروهای ارتش اسرائیل در حال تخریب گسترده ساختمان‌ها در منطقه حداتا در جنوب لبنان هستند
✅
@AloNews</div>
<div class="tg-footer">👁️ 78K · <a href="https://t.me/alonews/131819" target="_blank">📅 23:58 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131818">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">👈
واشنگتن پست: علیرغم ماه‌ها حملات آمریکا و اسرائیل، رژیم ایران تضعیف نشده است - و در واقع، برخلاف اظهارات ترامپ در مورد «تغییر رژیم»، در حال تقویت مجدد خود است
✅
@AloNews</div>
<div class="tg-footer">👁️ 75.2K · <a href="https://t.me/alonews/131818" target="_blank">📅 23:54 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131817">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">👈
العربیه: هیئت ایرانی شامل قالیباف و عراقچی بعد از مراسم تشییع برای مذاکره با آمریکا به پاکستان خواهند رفت
✅
@AloNews</div>
<div class="tg-footer">👁️ 76.5K · <a href="https://t.me/alonews/131817" target="_blank">📅 23:50 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131816">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">🚀
سرویس های پایدار  safe vpn
✔️
اتصال پایدار و پرسرعت
✔️
دارای ساب برای اطلاع لحظه ای از باقیمانده
✔️
متصل در تمامی دستگاه ها و اینترنت ها
✔️
مناسب استریم، بازی و استفاده روزمره
✔️
پشتیبانی تا پایان سرویس
💬
تعرفه‌ها
🔸
پلن‌های یک‌ماهه
▫️
۲۰ گیگابایت — 30,000…</div>
<div class="tg-footer">👁️ 76.1K · <a href="https://t.me/alonews/131816" target="_blank">📅 23:47 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131815">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">🚀
سرویس های پایدار  safe vpn
✔️
اتصال پایدار و پرسرعت
✔️
دارای ساب برای اطلاع لحظه ای از باقیمانده
✔️
متصل در تمامی دستگاه ها و اینترنت ها
✔️
مناسب استریم، بازی و استفاده روزمره
✔️
پشتیبانی تا پایان سرویس
💬
تعرفه‌ها
🔸
پلن‌های یک‌ماهه
▫️
۲۰ گیگابایت — 30,000 تومان
▫️
۴۰ گیگابایت — 60,000 تومان
▫️
۶۰ گیگابایت — 90,000 تومان
▫️
۸۰ گیگابایت — 120,000 تومان
▫️
۱۰۰ گیگابایت — 150,000 تومان
▫️
۱۵۰ گیگابایت — 210,000 تومان
▫️
۲۰۰ گیگابایت — 300,000 تومان
▫️
نامحدود (مصرف منصفانه ۳۰۰ گیگ) — 450,000 تومان
🔹
پلن‌های دوماهه
♦️
۳۰ گیگابایت — 50,000 تومان
♦️
۵۰ گیگابایت — 80,000 تومان
♦️
۷۰ گیگابایت — 105,000 تومان
♦️
۱۰۰ گیگابایت — 155,000 تومان
♦️
۱۵۰ گیگابایت — 230,000 تومان
♦️
۲۰۰ گیگابایت — 305,000 تومان
♦️
نامحدود (مصرف منصفانه ۴۰۰ گیگ) — 585,000 تومان
🔸
پلن‌های سه‌ماهه
▫️
۸۰ گیگابایت — 160,000 تومان
▫️
۱۰۰ گیگابایت — 200,000 تومان
▫️
۱۵۰ گیگابایت — 300,000 تومان
▫️
۲۰۰ گیگابایت — 400,000 تومان
▫️
۳۰۰ گیگابایت — 600,000 تومان
▫️
نامحدود (مصرف منصفانه ۵۰۰ گیگ) — 680,000 تومان
🤖
ربات خرید
@SafeVPNXBot
✅️
📞
پشتیبانی
@safevpn_secureSupport
✅️
📢
کانال اطلاع‌رسانی
@safevpn_suportt
✅️
😍
رضایت مشتریان
@safevpn_feedback
✅️
🌱
سپاس از اعتماد شما</div>
<div class="tg-footer">👁️ 74.1K · <a href="https://t.me/alonews/131815" target="_blank">📅 23:47 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131813">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">👈
اختلال موقت خدمات مبتنی بر کارت بانک ملی
🔴
بانک ملی اعلام کرد خدمات مبتنی بر کارت این بانک به‌منظور به‌روزرسانی و ارتقای زیرساخت‌های فنی و افزایش پایداری سامانه‌های بانکی، بامداد یکشنبه ۱۴ تیرماه ۱۴۰۵ به‌صورت موقت از ساعت ۰۰:۰۰ تا ۰۲:۰۰ در دسترس نخواهد بود.
🔴
این وقفه موقت در راستای اجرای عملیات فنی و ارتقای زیرساخت‌های بانکی انجام می‌شود و پس از پایان عملیات، خدمات مبتنی بر کارت مجدداً در دسترس مشتریان قرار خواهد گرفت.
✅
@AloNews</div>
<div class="tg-footer">👁️ 71K · <a href="https://t.me/alonews/131813" target="_blank">📅 23:47 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131811">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/41b55a06b3.mp4?token=grvvQzt70G8FOsISStSb9py3DIY4m1gJhJjKaw4xA3LrC-WU4C_Ld_k-JiwrfjCvNwo2RASprMZKF2wa73ZRErZMqsP5SwxJ0CBPnODQavLDycPOEdw5BWP-Ze5UW8tFZTEz36OrVMKq7EpUwqIzaMhE-FrIZqvKqK2O12Zr6OOhrAF1yDMC1zxtoM2GCttPmPFR4q-B-_IqHxXVjwsVSwdcRp0eZ5UCotTTiE5sAdNx9HrC0SZlzxJzYgz3O4orDtappB6XV1boZUc6A9TpeT2i0ZeY56X3ZqqycqlvDpN-BFC7Hq78At38jkVdQEoEpZrJMIARz9GSawr76TbAaQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/41b55a06b3.mp4?token=grvvQzt70G8FOsISStSb9py3DIY4m1gJhJjKaw4xA3LrC-WU4C_Ld_k-JiwrfjCvNwo2RASprMZKF2wa73ZRErZMqsP5SwxJ0CBPnODQavLDycPOEdw5BWP-Ze5UW8tFZTEz36OrVMKq7EpUwqIzaMhE-FrIZqvKqK2O12Zr6OOhrAF1yDMC1zxtoM2GCttPmPFR4q-B-_IqHxXVjwsVSwdcRp0eZ5UCotTTiE5sAdNx9HrC0SZlzxJzYgz3O4orDtappB6XV1boZUc6A9TpeT2i0ZeY56X3ZqqycqlvDpN-BFC7Hq78At38jkVdQEoEpZrJMIARz9GSawr76TbAaQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">قتل یک جایگاه دار پمپ بنزین در جیرفت کرمان
🔴
به گفته منابع محلی این حمله بدلیل مشکلات شخصی بوده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 73.1K · <a href="https://t.me/alonews/131811" target="_blank">📅 23:39 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131810">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">👈
روزنامه اسرائیلی: ترتیبی برای دیدار نتانیاهو و ترامپ انجام نشده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 70.4K · <a href="https://t.me/alonews/131810" target="_blank">📅 23:31 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131809">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EaYHjoR4qECdXCX0rQl24_1rpnin8-1YfhTMmrHpA6FimkunpZjSa3DRBqglHp3SgHgLFy0rkVS4skPuhNgt8NvBVhVM4ZOtvm5OMwfmR3ijBuQgnsd2RiIPgzxOlU_Hmx0889-RBcaFkleg7ZAVwKoklt5iXCBZEJ7RsCahGkH9Itznq_S3heTYL5Ryo-GMbnQ6DFDMLzM5WqghC-fCVkSv_Kgi8S6PQr08oMdjI0Swrd1_jusnyH1lSgcSvHC7883jzdavrp_0mVyMWTeS4NkAic_u6UjKc8Z_AZG6Qtb5BbE0n6kSrLpLIkmy1bweh0nDrONniGx4o0Ksqz_WIA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
پناهیان: حاضریم همه چی رو فدا کنیم تا آقا بازم زنده بشه
✅
@AloNews</div>
<div class="tg-footer">👁️ 74.9K · <a href="https://t.me/alonews/131809" target="_blank">📅 23:26 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131808">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/P85EXlKxSvDdZS6wYF8IE0WnI3VT7By2SldW7yZFA2ypSxxqRjSYY_fEjIMTBolwJKNHlVSBxV43opVjdgONjOdzsWFO0_g7-Fdk8d75dWmin5CgIe-7ft07P7L519LIESOioensHgEj03rWIFCWIgbXb_zl37CEo1CxfTapEzZ7yV5erbt_BYL6ndsp-7ctU2J1S50bU_71k6Bb02Dv5MIoa_ZUmcla_TZoSeOU9rWqj3B47_VZNIsrdXpzlEgBDnloZsn_roCH_2jVFgvCO_8x_WnB3tuuodnsQ-764UAhlGDo7A7UmVtP931vLlNxzdhHIz-Tm4UJoXqjkyivOw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
اتفاقی عجیب در جام جهانی
‼️
🔴
گروهی از طرفداران زن آرژانتین بعد پیروزی مقابل کیپ ورد در سکوهای استادیوم کاملا عریان شدند
😐
⚠️
مشاهده فوری و بدون سانسور
⚠️</div>
<div class="tg-footer">👁️ 76.4K · <a href="https://t.me/alonews/131808" target="_blank">📅 23:21 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131807">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">👈
بیت‌کوین بزرگترین ارز دیجیتال جهان به رشد خود ادامه داد و  از مرز ۶۳۰۰۰ دلار عبور کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 73.9K · <a href="https://t.me/alonews/131807" target="_blank">📅 23:14 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131806">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/I2fv1oarrndQkK-KWrdb1i1xsGsgMO9rPAatj26b4zWXj-shCH6kS_yYuvJkGO5c_6hY_P_WpiNns3cmf0RocvEXT3EVkDhlA5mlZ649VwbTMh9AI-q7Z-yqaSjcjRlAIhwHuoJFLwmZsp89ZAfIqB05JXGEPxL5b-ergOUkK3FORcKsZZnt80lMPU8l0e_ayh4KT648cv8u_G_yJZE425nH3sJTEoxMIilDsy_sll0ce0v19KiRaNsLS658RzN-rkXxPEpTeobYQA69h_tQj4WD09H9vK02lFLlm8B6TxwdnwNE0MT6fmWpC0aJ9ckpkmaJ_zb3xgKP3gnZjBhq4A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ترامپ: با وجود گرمای هوا، که به اندازه پیش‌بینی‌ها شدید نیست، جمعیت حاضر در واشنگتن دی.سی. فوق‌العاده است! عشق به کشور ما هرگز به این شدت نبوده است. نمایش‌های هوایی در سطحی قرار دارند که قبلاً هرگز دیده نشده بود - چه خلبان‌های فوق‌العاده‌ای، چه تجهیزات عالی‌ای!
🔴
به زودی با هم ملاقات خواهیم کرد. من حدود ساعت 10 شب در یادبود لینکلن سخنرانی خواهم کرد.
🔴
حوضچه بازتاب (رفلکتینگ پول) بسیار زیبا به نظر می‌رسد، با وجود تمام آسیب‌هایی که از سوی اوباش خرابکار به آن وارد شد. ما بلافاصله پس از این آخر هفته، آن را تخلیه کرده و خسارات وارد شده را ترمیم خواهیم کرد.
🔴
روز استقلال مبارک. کشور ما از همیشه قوی‌تر است!
✅
@AloNews</div>
<div class="tg-footer">👁️ 76K · <a href="https://t.me/alonews/131806" target="_blank">📅 22:58 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131805">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fuUntNC9AINb8kf6xWh5PdnmzMi8lU4UffdyND1e0ZCshJPYvGyhhnWnCez949HPvsIf96UnoltYTLq702ztEMS3yWdsixnCfKqrui9xQ_S2OumBV4i5VgivSo1P8yOdElJPTdtk_sRlyP2Oh1XbzFF-RBrEEjE_YyxSZ11kYRMDFks_-VMAYRwGEUGJiNElrZjxfAOgF-Z7Whu1f0QeTffQyKZMKwF6eUa9ByX7rTx_r8akeokYxQEs9g4VCGkCrLNcZlMwKaKq_jih2Wqs2ZLD8PIgKkzGcRwM9UPdge9c-cktwjfSlTmlRk0jboWTm3wTO27nLU5ip6S8sQeE9Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ترامپ: اروپا در حال یادگیری این است که وقتی جنایتکاران کشورهای جهان سوم را به داخل کشور خود راه می‌دهید، خودتان به یک کشور جهان سوم تبدیل می‌شوید.
🔴
این اتفاق به سرعت، در عرض چند لحظه رخ می‌دهد. من درست در زمان مناسب انتخاب شدم!
✅
@AloNews</div>
<div class="tg-footer">👁️ 71K · <a href="https://t.me/alonews/131805" target="_blank">📅 22:58 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131804">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WBIPQ_CLJ8rXy00QkvF59XrrGs5nPrpvSKcYkdCJY_Q5dTX6rDK8T5oDOURz_YKP9RZnVjCKFezrX-hdXwk_EE_UkZUvzDM0OyC2wpugUD-8bJr6SOuqQOgmG9hCf2oYPVELptEHczldLcH2m9qO4TdFiY1g0OqeEdx6HK4n7yRzDmLVxLlsFasLA5fammazKfv8KOLjFvrqSMOfNS52LZmx9GUx5n371__eIdcCP0wldZWDpionWHYMQ5k6Zm37ZrT52ny_x8xUxPAG6SrBBa9-GcaFh9ImJZxPA3ahKCiFpkGXkzB9lDiadh7wxs8TsVphmcbT8ZPVjS-XlhV_Ww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
پرواز سنگین سوخت‌رسان‌های آمریکایی بر فراز خلیج فارس
✅
@AloNews</div>
<div class="tg-footer">👁️ 71.2K · <a href="https://t.me/alonews/131804" target="_blank">📅 22:54 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131803">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">👈
عبدالخالق عبدالله، مشاور سابق رئیس امارات: با وجود عمق روابط و همکاری‌ها با امارات و کشورهای عربی خلیج فارس، چین ایران را مهم‌ترین شریک راهبردی خود در بلندمدت می‌داند
🔴
در محاسبات چین، پایداری ایران نشانه‌ای از افول آمریکا تلقی می‌شود که در خدمت منافع پکن است
✅
@AloNews</div>
<div class="tg-footer">👁️ 68.6K · <a href="https://t.me/alonews/131803" target="_blank">📅 22:47 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131802">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">👈
حوثی‌ها با انتشار ویدئو : برای همه احتمالات آماده هستیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 73.7K · <a href="https://t.me/alonews/131802" target="_blank">📅 22:34 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131801">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e5c8672f92.mp4?token=k6ymPzh35Gs6Hye2j7zILwSxwAqzceyKu-uK_VZrObcuXDLtaXiHD786k4zRiTy6a2_SSmJr6hbSYhzt9wf1CSqI7ojajcldoT8-RhOOrTUVEuLoXZ9tyCbWUqJ0Dp0qgbgV-wicUo5bQfS-kikQcCiV0TboLZ6tu6ZOf4K5OAIMbqZL_cvSkm5Dhwhc3WIVDj5HgAliATD4Vs19YpnWdI0jKTZQzgwMkgNfbLuSDVHGbyv1wTA4uPxlNV4yZZY_t4WhBKN5WzTLMJXNDnrECh2fb6B1dlOwgNnTQuLW1-s06sjjsSQexEQw_0RZO1i4ffv-u6noH1SASv9N0Icf2w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e5c8672f92.mp4?token=k6ymPzh35Gs6Hye2j7zILwSxwAqzceyKu-uK_VZrObcuXDLtaXiHD786k4zRiTy6a2_SSmJr6hbSYhzt9wf1CSqI7ojajcldoT8-RhOOrTUVEuLoXZ9tyCbWUqJ0Dp0qgbgV-wicUo5bQfS-kikQcCiV0TboLZ6tu6ZOf4K5OAIMbqZL_cvSkm5Dhwhc3WIVDj5HgAliATD4Vs19YpnWdI0jKTZQzgwMkgNfbLuSDVHGbyv1wTA4uPxlNV4yZZY_t4WhBKN5WzTLMJXNDnrECh2fb6B1dlOwgNnTQuLW1-s06sjjsSQexEQw_0RZO1i4ffv-u6noH1SASv9N0Icf2w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
انفجار تانکر سوخت در آمریکا
🔴
پلیس شهرستان مونتگومری در ایالت آلابامای آمریکا روز شنبه از انفجار یک تانکر سوخت و آتش‌سوزی در محل حادثه خبر داد.
🔴
این انفجار حوالی ظهر به وقت محلی رخ داده و علت آن نقض فنی اعلام شده است.
🔴
این حادثه منجر به قطع برق چندین خانه در منطقه شد. پلیس از مردم خواست تا از ورود به این منطقه خودداری کنند
✅
@AloNews</div>
<div class="tg-footer">👁️ 74.2K · <a href="https://t.me/alonews/131801" target="_blank">📅 22:21 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131800">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">👈
واشنگتن پست: ایران در موقعیت قوی‌تری در تقابل با آمریکا قرار دارد
✅
@AloNews</div>
<div class="tg-footer">👁️ 67.9K · <a href="https://t.me/alonews/131800" target="_blank">📅 22:16 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131799">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">اخبار جنگ الونیوز AloNews
pinned a photo</div>
<div class="tg-footer"><a href="https://t.me/alonews/131799" target="_blank">📅 22:15 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131798">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">👈
شرکت ملی پخش فرآورده‌های نفتی:
هیچ جایگاهی بدون بنزین نمی‌ماند
🔴
سوخت هواپیماهای حامل هیات‌های خارجی تامین شده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 71.4K · <a href="https://t.me/alonews/131798" target="_blank">📅 22:11 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131797">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">👈
دولت ونزوئلا : تعداد کشته‌ها به
۲۹۵۴
نفر افزایش یافته
✅
@AloNews</div>
<div class="tg-footer">👁️ 71.5K · <a href="https://t.me/alonews/131797" target="_blank">📅 21:55 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131796">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">👈
صداسیما: از صبح تاکنون بیش از ۲۰ بار مصلی پر و خالی شده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 73.2K · <a href="https://t.me/alonews/131796" target="_blank">📅 21:46 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131795">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/e9d5d97bd2.mp4?token=nah5fNSlEu0c3e5-2lvjlgUlrWUDiiv2QhQ-QMZAk0k6Zc_j8OqX-wzeoZ2ledUgQDStap32XfdXN8ItqECd7iqLfGdJbqP3D9jDxitQJo2KK4uT0_vCtpq2nIzG3m-fEySM6WaokPmnW2m-Kc_d0GaSgBOhshzkUcF4IDNFGM8-beAeiD1gQ5P0yJKDRdo2cx0_aEnRHUo3mnAzpqo1MIv3hoaZfo5C-fYXQIXN4DHpcHW2Zw159UNg6a4eO3uull2EGV_GWoDORPk0I_O53wLUhWshaBhXbgSzPLsmlRdJQYcdXv8vMN9g7VvsHLfNf5Vu9a-mG4snVUGR1JA0kQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/e9d5d97bd2.mp4?token=nah5fNSlEu0c3e5-2lvjlgUlrWUDiiv2QhQ-QMZAk0k6Zc_j8OqX-wzeoZ2ledUgQDStap32XfdXN8ItqECd7iqLfGdJbqP3D9jDxitQJo2KK4uT0_vCtpq2nIzG3m-fEySM6WaokPmnW2m-Kc_d0GaSgBOhshzkUcF4IDNFGM8-beAeiD1gQ5P0yJKDRdo2cx0_aEnRHUo3mnAzpqo1MIv3hoaZfo5C-fYXQIXN4DHpcHW2Zw159UNg6a4eO3uull2EGV_GWoDORPk0I_O53wLUhWshaBhXbgSzPLsmlRdJQYcdXv8vMN9g7VvsHLfNf5Vu9a-mG4snVUGR1JA0kQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ارتش اسرائیل (IDF) اعلام کرد که امروز زودتر، یک شبه‌نظامی متهم حزب‌الله در پی تعقیب در مجدل زون، منطقه صور، لبنان توسط نیروهای زمینی ارتش اسرائیل کشته شد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 74.4K · <a href="https://t.me/alonews/131795" target="_blank">📅 21:40 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131794">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FBxCMqzcN7FP7D5cpVc7gO2QqF89e7_1N9Y_f0R_IS1byBT0bpEA5QhZb8PdqREftFM_8shYKN638j3IQWMg_ozHqpQjwY3jjTEGZhqKlLPrLJrRdnB6ZH2veT8z3OdTLnKy-gctXlsheETGEy5iDcJIFijsbNangMaRyWl5Fehs7ezdp7YTDn4V8N8SKh6OgFQDlDNtQ-wZQ0WT2lx8WkUrEQonLDk0y9ok3G9Cf3H075FxBoltLBZa8TYS6SWXYkV8EDqjaKFzdcw2f4XRGBEcCSdGcPd0_phHJOjVS_111JdKnlXEZoPBYst_VwDfH8f4pg27_87T8bCGwRxGhQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ترامپ به آکسیوس: نتانیاهو میداند رئیس کیست.
✅
@AloNews</div>
<div class="tg-footer">👁️ 71.7K · <a href="https://t.me/alonews/131794" target="_blank">📅 21:33 · 13 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>

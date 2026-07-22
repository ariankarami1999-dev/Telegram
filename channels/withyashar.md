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
<img src="https://cdn4.telesco.pe/file/Ag9bJ44kEhHJJKQTg5GoERrbNhyjLUWH58OjCMtICRpGu_8sN3B6P1KqQXXEfTdPLnxt0xtFVhWWgzkEbu2bl--c54MtttYwvAIaROR1jjLejLeF6WZl20pEydiHJw0-x3fSyr3OzMqMi6byNB5lU4iyFcp2GWUB2iJKwCbaRz4dns-M4VgzG6a2TPFM4Pcomkq0OnElZ9f9dwuc2ryRmMoys3sBMWPO2Zd_GTVyjcrPVDZ2UYfBuqtXyKHWxiIIOLBxQ7XH1kdB7ByGz0FYWN4zF4ohHz7QgMKzJ2sxrRMZlgClf8KEeXi4oNIr4QCXH2PSnLyLSCF944QNVPYC1g.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 WarRoom with YASHAR</h1>
<p>@withyashar • 👥 420K عضو</p>
<a href="https://t.me/withyashar" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 چنل رسمی«اتاق جنگ با یاشار»اخبار لحظه ای و فوری از‌ جنگ با تحلیلinstagram.com/yasharhttps://X.com/yasharrapfa</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-31 22:28:39</div>
<hr>

<div class="tg-post" id="msg-19356">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">سیریک صدای توافق میاد
🚨
🚨
🚨
@WarRoom</div>
<div class="tg-footer">👁️ 55.4K · <a href="https://t.me/withyashar/19356" target="_blank">📅 22:01 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19355">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-footer">👁️ 65.7K · <a href="https://t.me/withyashar/19355" target="_blank">📅 21:52 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19354">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">سناتور در‌ جلسه سنا
:
مردم دیگر نمی‌دانند کدام روایت درباره جنگ را باور کنند؛ چون یک بار گفته می‌شود جنگ تمام شده و بار دیگر گفته می‌شود تمام نشده است. یک بار گفته می‌شود ظرف دو هفته اتفاقی می‌افتد و بعد می‌گویند نه، این‌طور نیست. یک بار می‌گویند دیگر موشکی نداریم و بار دیگر می‌گویند هنوز موشک داریم.
همین سردرگمی باعث شده بسیاری از مردم گیج، نگران و تحت فشار باشند و این جنگ را به‌شدت نامحبوب بدانند. چون تصمیم‌هایی را که رئیس‌جمهور می‌گیرد درک نمی‌کنند و با آن تصمیم‌ها موافق نیستند
@WarRoom</div>
<div class="tg-footer">👁️ 67.7K · <a href="https://t.me/withyashar/19354" target="_blank">📅 21:51 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19353">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">سد مجید گشاد زن
فرمانده هوافضا تروریستی سپاه:
به پل ها و نیروگاههای ما تعرض شود خاموشی برق متحدان و میزبانان کودک کشان قطعی است.
@WarRoom</div>
<div class="tg-footer">👁️ 72.8K · <a href="https://t.me/withyashar/19353" target="_blank">📅 21:46 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19352">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">بیانیه فرماندهی نیروی دریایی تروریست سپاه(همون چرکه):
ورودی و خروجی تنگه هرمز مشخص و در کنترل قطعی ماست. مسیرهای جایگزین ، نا ایمن و خطرناک است اخطار می دهیم استفاده نشود که تبعات سنگین و غیر قابل جبرانی خواهد داشت
@WarRoom</div>
<div class="tg-footer">👁️ 73.9K · <a href="https://t.me/withyashar/19352" target="_blank">📅 21:43 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19351">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">صدای انفجار‌ در کویت
🚨
🚨
🚨
@WarRoom</div>
<div class="tg-footer">👁️ 79K · <a href="https://t.me/withyashar/19351" target="_blank">📅 21:38 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19350">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vx6T9xnjNYdDwiWMbr2ydGetjKh_nQa2QUsxC3nI-4ISQO3ezrRZUJPIuh0eby4LWNUlJ3bqc3z5hATlbkrOyKCEiRSc235EDWiw9aPfqrd_lnJoZ7Zh2RLUAVICV9DYhZHMxAuDQrDbuotZZzOXmT27myQTUpb0ppvgEUDALEpsuCFDDZtLiXNeo2hxWrkAuBrRckMuE3dUp3mKsbBfHB7WbXxj2BZpwj_QIv53MUwCysD3gXexr5hTf4kA2QGYZ-9Ctm-33ZOAlWbcNkDW3mLw2_KaaYJeFDkRYfe1v_K3eEqNf_tgRIXnMiDLkDOUexRUNq912ylYVgSTQADOfQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبری که ترامپ بازنشرکرد
:
به سنتکام دستور داد شده دروازه‌های جهنم را به ایران باز کنن بعد از کشته شدن نیروهای آمریکایی
@WarRoom</div>
<div class="tg-footer">👁️ 83.1K · <a href="https://t.me/withyashar/19350" target="_blank">📅 21:33 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19349">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-footer">👁️ 86.2K · <a href="https://t.me/withyashar/19349" target="_blank">📅 21:23 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19348">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">موج حمله موشکی جدید رژیم
@WarRoom</div>
<div class="tg-footer">👁️ 88.3K · <a href="https://t.me/withyashar/19348" target="_blank">📅 21:20 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19347">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">خبرگزاری کان: اسرائیل از سوی ایالات متحده آمریکا مطلع شده است که این کشور قصد دارد حملات خود به ایران را تشدید کند و در روزهای آینده، و برای اولین بار در این تشدید، حملاتی را با استفاده از بمب‌افکن‌های سنگین علیه ایران انجام دهد
@WarRoom</div>
<div class="tg-footer">👁️ 98.6K · <a href="https://t.me/withyashar/19347" target="_blank">📅 20:57 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19346">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YmdhOcpDHxfR_1awcasDf1czg10G6K8JnhLZHkl66uRnNvMSWYcYP8duOpfIR46P1RxGCij2ZiCGhHiO-nfhDqJpDgS0_7mzREMyNvuEPmxrnt_ke4BBgwkrc5Lf-7p2120KK8TsjBTXEocq-oFnGCLfTf01C6OBpbCMfyGQ3nVNqpT8dVJpOpOzvsE4MJYw4-SeLG33hXmf73jIXxil50FLpWzM5szTruOPePd2hSgbsI7pNAbx8oZ0Nr2kGv9FIWwQjHu4ufkPd07P9Qtky4ygEu8FKbiLpmbknisZT9fM-OAaLkAAmh8qj8QbHG36-0rb71OITy_aLl1MgzFKpw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‎سنتکام:نیروهای ایالات متحده که محاصره دریایی علیه ایران را در دریای عرب اجرا می‌کنند، طبق اعلام سنتکام (فرماندهی مرکزی ایالات متحده) تا تاریخ ۲۲ ژوئیه، ۹ فروند کشتی تجاری را تغییر مسیر داده و ۱ فروند را از کار انداخته‌اند. ناو یواس‌اس مایکل مورفی (DDG 112) عملیات را زیر نظر دارد.
@WarRoom</div>
<div class="tg-footer">👁️ 104K · <a href="https://t.me/withyashar/19346" target="_blank">📅 20:42 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19345">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-footer">👁️ 103K · <a href="https://t.me/withyashar/19345" target="_blank">📅 20:35 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19344">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">حمله موشکی پهپادی رژیم به اربیل عراق
🚨
🚨
🚨
🚨
@WarRoom</div>
<div class="tg-footer">👁️ 105K · <a href="https://t.me/withyashar/19344" target="_blank">📅 20:27 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19343">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">علی‌رغم هشدارهای ایران ،بلغارستان اجازه استقرار هواپیماهای آمریکایی در خاک خود را می‌دهد.
@WarRoom
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 108K · <a href="https://t.me/withyashar/19343" target="_blank">📅 20:18 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19342">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d436f581ea.mp4?token=qPLEEtFkDWrupN7lFiuP_dS8aMzXHh8TqnBCatx6gB8mJSmwzJJysEOBJdXs1xBIBZPp4gUfhgJR2sgUgVx-QpC3D9SLODvFRNlFMba6Ix5T2gBDWc0e1HwtUGwiNtvkFyL0wYSdbkXq4323kEjN6-bL1Jl522QhmMjpicljMDDsxUrEFB71L4m4Iz7OkNnxJNIuLrBDA_5-bHpNWiXMSEO8OKbBC_quKDgJoqW63zGIYQrzHiYwz52UJbR-WaxazBmMv1o2uvgCkQLl9GiOxajnypfS8nlNNSXc7bZbGfWTEfp27zf7uNURNZy9QbjfJ5keCZbRskA_iT5yZc1sG0fpPMJixz2iwYOxSOg4-cIeGuDEbCntvHhw_Dix2TzrS5AWgEl2rR0eLVIwtWIjNhsXtyp5awTdijfjLSPVcZhydIx2Dn2PNxI0lwuQPABui22wk9H8xXJSSOlFOE4CgnrlLgfJD2HCQ1RRrq-5ZPTgE4uJx7TudNgVpvFhYEgh2zzlfCTLo9lKvD0QE4oAZsIhza7jupzR-SlhWwqVleyeNO4i9sn1eSJ8iJzdRsrVG2NrFXhCXi87_o6mt1ko00XWl3pLZubPK8wXdOeZt2myeK6CTa5Ok8BAp3NtFDfJkGWGU8cgekskWyJXqL2YT60-pYeSoMin2NKC_Nudc-0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d436f581ea.mp4?token=qPLEEtFkDWrupN7lFiuP_dS8aMzXHh8TqnBCatx6gB8mJSmwzJJysEOBJdXs1xBIBZPp4gUfhgJR2sgUgVx-QpC3D9SLODvFRNlFMba6Ix5T2gBDWc0e1HwtUGwiNtvkFyL0wYSdbkXq4323kEjN6-bL1Jl522QhmMjpicljMDDsxUrEFB71L4m4Iz7OkNnxJNIuLrBDA_5-bHpNWiXMSEO8OKbBC_quKDgJoqW63zGIYQrzHiYwz52UJbR-WaxazBmMv1o2uvgCkQLl9GiOxajnypfS8nlNNSXc7bZbGfWTEfp27zf7uNURNZy9QbjfJ5keCZbRskA_iT5yZc1sG0fpPMJixz2iwYOxSOg4-cIeGuDEbCntvHhw_Dix2TzrS5AWgEl2rR0eLVIwtWIjNhsXtyp5awTdijfjLSPVcZhydIx2Dn2PNxI0lwuQPABui22wk9H8xXJSSOlFOE4CgnrlLgfJD2HCQ1RRrq-5ZPTgE4uJx7TudNgVpvFhYEgh2zzlfCTLo9lKvD0QE4oAZsIhza7jupzR-SlhWwqVleyeNO4i9sn1eSJ8iJzdRsrVG2NrFXhCXi87_o6mt1ko00XWl3pLZubPK8wXdOeZt2myeK6CTa5Ok8BAp3NtFDfJkGWGU8cgekskWyJXqL2YT60-pYeSoMin2NKC_Nudc-0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بنیامین نتانیاهو در پیامی به مناسبت نهم آو گفت اسرائیل طی سه سال گذشته با حفظ وحدت داخلی از بحران عبور کرده و به جای جنگ داخلی، در برابر دشمنان متحد شده است. او تأکید کرد که این کشور با وجود ادامه چالش‌ها به دستاوردهای مهمی رسیده و مأموریت هنوز به پایان نرسیده است. وی اعلام کرد برای تقویت وحدت داخلی، در پی تشکیل یک دولت ملی فراگیر و باثبات خواهد بود که امنیت و آینده اسرائیل را تضمین کند و افزود اختلافات انتخاباتی نباید مانع حفظ انسجام جامعه شود. او همچنین با اشاره به تجربه‌های اخیر گفت مردم اسرائیل در لحظات سخت نشان داده‌اند که بیش از آنچه تصور می‌شود متحد هستند
@WarRoom</div>
<div class="tg-footer">👁️ 110K · <a href="https://t.me/withyashar/19342" target="_blank">📅 20:13 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19341">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">ارتش آمریکا در حال انجام عملیات تخلیه تمام هواپیماهای سوخت رسان و ترابری خود از قطر می‌باشد.
@WarRoom
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 109K · <a href="https://t.me/withyashar/19341" target="_blank">📅 20:06 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19340">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">کانال ۱۴ : سپاه پاسداران ایران، ایالات متحده را به حمله تروریستی «به سبک یازده سپتامبر» تهدید می‌کند.
خبرگزاری تسنیم وابسته به دولت گزارش می‌دهد که سپاه پاسداران هشدار داده است: «اگر جنگ ادامه یابد، ما عملیات پشیمان‌کننده‌ای انجام خواهیم داد که منجر به عزای ملی در آمریکا خواهد شد.»
آخرین باری که ایالات متحده برای یک حمله عزای ملی اعلام کرد، یازده سپتامبر بود.
@WarRoom</div>
<div class="tg-footer">👁️ 111K · <a href="https://t.me/withyashar/19340" target="_blank">📅 20:01 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19339">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">منابع جمهوری اسلامی : رژیم ایران معتقده مهلت‌های آتش‌بس چیزی جز فرصت‌هایی برای تجدید قوا، سازماندهی نیروها و بازگشت دوباره به جنگ نیست و نمیخواد در چنین چرخه‌ای گرفتار بشه.
@WarRoom</div>
<div class="tg-footer">👁️ 114K · <a href="https://t.me/withyashar/19339" target="_blank">📅 19:46 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19338">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">خبرگزاری رویترز: شرکت هواپیمایی کی‌ال‌ام هلند اعلام کرد تعلیق پروازهای به کشورهای خلیج فارس را تا ۶ سپتامبر تمدید خواهد کرد.
این اقدام به دلیل وضعیت بحرانی در غرب آسیا اتخاذ شده است
@WarRoom</div>
<div class="tg-footer">👁️ 117K · <a href="https://t.me/withyashar/19338" target="_blank">📅 19:28 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19337">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">اکسیوس
:
شرط اصلی ترامپ برای برقراری آتش‌بس این است که ایران حملات علیه کشتی‌ها را متوقف کند و تنگه هرمز را دوباره برای کشتیرانی باز کند
@WarRoom</div>
<div class="tg-footer">👁️ 122K · <a href="https://t.me/withyashar/19337" target="_blank">📅 19:00 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19336">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">رسانه های عبری : آمادگی در اسرائیل ، احتمال درگیری با ایران در آخر هفته @WarRoom
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 126K · <a href="https://t.me/withyashar/19336" target="_blank">📅 18:40 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19335">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">خبرنگار الجزیره:ایران ایده آتش بس موقت با آمریکا را رد کرد.
@WarRoom
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 125K · <a href="https://t.me/withyashar/19335" target="_blank">📅 18:39 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19334">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">رسانه های عبری : آمادگی در اسرائیل ، احتمال درگیری با ایران در آخر هفته
@WarRoom
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 124K · <a href="https://t.me/withyashar/19334" target="_blank">📅 18:38 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19333">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SCw8ccS7Y5vgsakC2XGW79NLhBbENuNTPW_Tln8YkQIOydBMMPTtg3ilmUBcABpJIdkJu8EycPGht-JiXk7wUC7kCq39jwwSFmkAVFgx1bWgy5balVI4zeUt6o5lnw8HzYZ6g_6otp0FI2aNi_tZGaWugNhcpNLKReQ6Nv_TzjZyNU9gCEf2eRVxvqR2Ajyu5TKH9RCcvaLdxHMnvF02asWdU-s2DvSt5rh11a1G_lROsinScQV1XxLpnnhzlIPGk6aQclkzLL6P-RVUuuO0xQktSjmyn4NeZbHDPmRMi-O5ORD0xJa5-vwnRLL9PclaXq6WSOOPeLmQXPY_GZNdQw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بعد از خوشحالی عرزشی ها از مرگ سرباز آمریکایی در هنگام خنثی سازی خدا به کمر آنها ضربه ای زد و جان دو نفر سپاهی را به همان شکل گرفت سردار احمد احمدی و سرهنگ دوم پاسدار مصطفی جمشیدیان از نیروهای واحد تخریب لشکر ۸ زرهی نجف اشرف، در هنگام چک و خنثی سازی کشته شدند
@WarRoom</div>
<div class="tg-footer">👁️ 127K · <a href="https://t.me/withyashar/19333" target="_blank">📅 18:21 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19332">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aAEzEm8Usn45UCASqOGb8KJMZl-egIilA5B2B3crZ6NxpAbnnUfpZ-7yE2ctOqfDqRMJ4wK8lJRc74kdKYny7T7rnzFgnZJPEyApxo-cICoENyhoM4y9eKQPQxGY9ykVWPtQoWm4o65wCyJXeEjCYrVnz-1huvG9HPJw8IF0YIPh-_SHwNHMpbQOSt2_NOSVR8Z9K8xjuD4p2YXWczsBtInLTinTBpsQeQmNawMNqFMncgKDQriZKdfR5wAbedV4QbqSh9p5EdLqVV_HzrnJOB4MmszcWB_G_XuFp-iBlLDUt3dkTyFUh2aVfM0kUKpkZ_e1_IgaHwasKVfIiNvkuQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یک اسکادران جنگنده پنهانکار F-35 با عبور از اقیانوس، توسط دو سوختستان استقبال و کمی دیگر در انگلستان به فرود میآیند. یکی از آنها، احتمالا به علت نقص فنی یا برای نشان دادن خود به جهان و تمرین ، آلارم فرود اضطراری روشن کرده است.
@WarRoom
🚨
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 125K · <a href="https://t.me/withyashar/19332" target="_blank">📅 18:08 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19331">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">آکسیوس به نقل از یک مقام کاخ سفید و یک منبع اسرائیلی:
کاخ سفید و دفتر نتانیاهو در حال هماهنگی برای برگزاری دیدار احتمالی ترامپ و نتانیاهو در دفتر بیضی طی هفته آینده هستن.
@WarRoom</div>
<div class="tg-footer">👁️ 122K · <a href="https://t.me/withyashar/19331" target="_blank">📅 17:59 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19330">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1cfead895f.mp4?token=r2s2-ypRtCKVs77EfcUjHqG17r3FbS9x9Kd-ZXQuru2suMMRnM6C7pwaqvxvgMxZZS65j0s86JAhfkvL2wPDe8SpT9UMISU26gXjGKuKTGaf0icDJYpXTVime58U28odV1qZXjoKtRl7omQmh-6d6HBD5y7shSkRgCvrMvLsXSTg7MvwNzRxAkmEWehFylZn3-rZVAtbG5dzus5qDo0yI-TIUo6XKRUSMUIPvSfzr48uqTEjfCPCE_Vu-MkHoOaKGRnKMy3wMHDmW-cwCKp-ZvK8gOE34nkUCdj02McQvJ7x47sDAgwlImGKvYSwmOwfnnYG-ixemkvmAa8CvU_nHw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1cfead895f.mp4?token=r2s2-ypRtCKVs77EfcUjHqG17r3FbS9x9Kd-ZXQuru2suMMRnM6C7pwaqvxvgMxZZS65j0s86JAhfkvL2wPDe8SpT9UMISU26gXjGKuKTGaf0icDJYpXTVime58U28odV1qZXjoKtRl7omQmh-6d6HBD5y7shSkRgCvrMvLsXSTg7MvwNzRxAkmEWehFylZn3-rZVAtbG5dzus5qDo0yI-TIUo6XKRUSMUIPvSfzr48uqTEjfCPCE_Vu-MkHoOaKGRnKMy3wMHDmW-cwCKp-ZvK8gOE34nkUCdj02McQvJ7x47sDAgwlImGKvYSwmOwfnnYG-ixemkvmAa8CvU_nHw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دونالد ترامپ، قرار است در مراسم انتقال رسمی پیکر سربازان آمریکایی کشته‌شده در جنگ ایران شرکت کند.
ترامپ پیش از سوار شدن به هواپیما، به خبرنگاران گفت: «جمهوری اسلامی به دلیل کشتن سربازان آمریکایی بهای سنگینی خواهد پرداخت.»
@WarRoom</div>
<div class="tg-footer">👁️ 127K · <a href="https://t.me/withyashar/19330" target="_blank">📅 17:47 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19329">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">گزارش های بسیار صدای جنگنده رامسر
@WarRoom
😁
بفرما زدم دیگه نگو</div>
<div class="tg-footer">👁️ 125K · <a href="https://t.me/withyashar/19329" target="_blank">📅 17:45 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19328">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fc4d4e3672.mp4?token=Y5P8IAJxeFgRMjvyb9heT1mvO8Ymun6nlbAZMOa2Wz243zDteUc9sPBnjV50j8ZYfyCQj5X8OaduBjyOP-7SNJlA-b9x7StrVEhzVYWezb6a9iZlY_rrVl9hocOwW8ndbLx0fzUpYwjsj1LWcm8ght8ia8-iKmSBBKY4VdLhyB7NcC0KM36m7tAeXzHlP9VFiF1_6XdufGQPum3C3VT3MQkkYFR4DH-cUmilkI-3SHJ7fSq_pEEwFXdp0-aDNTAo2Dkatvk72s-E0ESrergSOwfHlcbL_T3n6ANg27-cXbvbEAof2caet3NxTQm3WVo3sp3h53Ifsj-QuITHbwdqmA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fc4d4e3672.mp4?token=Y5P8IAJxeFgRMjvyb9heT1mvO8Ymun6nlbAZMOa2Wz243zDteUc9sPBnjV50j8ZYfyCQj5X8OaduBjyOP-7SNJlA-b9x7StrVEhzVYWezb6a9iZlY_rrVl9hocOwW8ndbLx0fzUpYwjsj1LWcm8ght8ia8-iKmSBBKY4VdLhyB7NcC0KM36m7tAeXzHlP9VFiF1_6XdufGQPum3C3VT3MQkkYFR4DH-cUmilkI-3SHJ7fSq_pEEwFXdp0-aDNTAo2Dkatvk72s-E0ESrergSOwfHlcbL_T3n6ANg27-cXbvbEAof2caet3NxTQm3WVo3sp3h53Ifsj-QuITHbwdqmA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">فاکس : بازی خطرناک تشدید درگیری؛
مقام‌های نظامی می‌گویند با نزدیک‌تر شدن حملات موشکی ایران به مناطق مرزی اسرائیل، خطر گسترش جنگ افزایش یافته است. به گفته آنها، ارتش اسرائیل در آماده‌باش کامل قرار دارد و مقام‌های تل‌آویو معتقدند تاکنون یک وضعیت بازدارندگی در برابر ایران ایجاد شده است.
بر اساس این ارزیابی، مقام‌های ایرانی نگران واکنش گسترده‌تر نیروی هوایی اسرائیل هستند، زیرا ورود مستقیم‌تر اسرائیل به درگیری می‌تواند خسارت سنگینی برای تهران به همراه داشته باشد
@WarRoom</div>
<div class="tg-footer">👁️ 128K · <a href="https://t.me/withyashar/19328" target="_blank">📅 17:42 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19327">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HsvmfIZ5lJiH2VCtlVLamNT2UEMZOgziVOE4ICWf0zlekpoMLaP1Ge0v5juymGLV0IzNFeOkatuKUaq0ub1ey3VUCMsKNpwelBA2yFF6yJzJxvKAAKt5whhRN8hnDmGwcg3CjgDjjOoXtrudgiB7aW819M6Yz8uIumIc_F-DwMFfb4stdY3FCdCO1TpP5clx8amN1MFqZ0T41wUFeU1IQKEoWQqF1X42WMypjv0fHSVaawklaTCzTn1yhBmf1_JIR5Fm984TWUgl8x0uXx591mitcy_-ZdyJR53wlNE198_4vrAO6fDqsV_n-yVvv4bW9GAfdC9nH1AmHOhDTGL4Kw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مراغه الان
@WarRoom</div>
<div class="tg-footer">👁️ 134K · <a href="https://t.me/withyashar/19327" target="_blank">📅 16:47 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19326">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/svy2sUi2OBrR_Q6mJXj-qVXLWTPlrGQd2HfzZ-b96hGM8MlAf_O-yBicgFCHH7RHijwGpdmCrljFuEfrDuVFb_51UKydqRoV-yDfGROxpGvNCKOs5v3wb8aDDkeurAHLVuQTedwXjKst1a5hOfd3SAY2-bXxUH_kcy7GinjrFSzoIhugyH0ZQJzQ3FJYCVWsW53_TtT7NZSyfjP5S0ZSgvHxR4_ow3ZaWOG-nN4QOGTkqsi5RvHGWbKBfa2vY3h22Y7idd_R1vk9h8kVAPCei2qSI6Gdj8WFpGlI7Q0WtK0ZQ_47u8bD5XuWb8hROVWsP5YeU2WI_k35unl-mZZVXQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">از این لحظه به بعد، هر زمان که جمهوری اسلامی ایران به کشتی‌ای در تنگه هرمز شلیک کند، چه با موشک، راکت، پهپاد یا هر وسیله یا سلاح دیگری، ایالات متحده یک پل یا نیروگاه، از جمله آنهایی که در کنار یا در پایتخت تهران قرار دارند را بمباران و نابود خواهد کرد. از توجه شما به این موضوع متشکرم! رئیس جمهور دونالد جی. ترامپ
@WarRoom</div>
<div class="tg-footer">👁️ 152K · <a href="https://t.me/withyashar/19326" target="_blank">📅 16:28 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19325">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">🚨
🚨
🚨
🚨
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 134K · <a href="https://t.me/withyashar/19325" target="_blank">📅 16:27 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19324">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">ترامپ در‌تروث : من به پایگاه هوایی دوفر می‌روم تا از قهرمانانمان (سربازان کشته‌شده در حمله ایران) تجلیل کنم.
@WarRoom</div>
<div class="tg-footer">👁️ 137K · <a href="https://t.me/withyashar/19324" target="_blank">📅 16:17 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19320">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/t8y5yzDNOT7WzNId7YLUGY_mEGCIdao5fG7np6OJneeS3-EyehOBYGXa5PTuGSfwrO8MCtjpeUy9ws3iNOGv28M2I2DVE7DxHUC24AXo23Oz62jKrivf9s_Lx2U-nU5espmYHhWyzQOwRJO6Hl7diJSXy0fIcnh3qUidp0V3eBfnywig2oJmuSd2EI2cRxaPC_kIMylDRG5yF1xaYS7vXWYMPACrQTo3fA_19JcOZKLdM4kVJ_hLY9NQUdG5L16qZsd3-hQLovQTXFSsN4YnPm0ferOKtlNcmqO1KehuEAfKDFvIT93-J1z_9RgPuTWsHmCLAorXKCxECT48oU9NbQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/fWSNLRXcrG9s5BkuAbR4H8Vp9itV6rfwNEIYQZ9xFNerhh9F8qg4Im_mtxoLmBGcJ-FviNuHR-gNGiFQS0Kg4Xb8Id-IfEDeMo4WMq_wbs80UpoOht2EozTIBVFuiLjcA2DML0a84o0CJpAxjvCsJ-nOKcPiLv0VHk3XhB9P4HbklCssALEdPCQrOJZJY2IKoTKGiN1xNGUBRi5EW796v-8SCiMjFFhI3Da7vxpv4aKwLaLIGk5HApDDLBbxGW-sNKn5m0zO3k2L9CnDPcoHZ3Sx7p1ywJVwP1dJxAH-ibWGvYLP_yqoVv--0zgdwrvLi9bRvNoA7fCRlM3EBduUfg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/b96zNYNZGkJLAnrHYI89gFdx2poEZHgDpBngMlFQrNtaxvRDaPcriNEa7uUua0KT2Uq76a1521scSaPQu_jx7W3_G1DpCNvBZjBenogUxVbxJMlpyATCP9LK0gA3-6FRRivpf6G2eykl63D1rxxtMuauzQQNWzk8PHxtkwoJECiGwzq8NoZYlbrkzylLnS_qRXt52vn_4aIH67AGnEZJbEcQbD4xw8mapleB0TJ3xkf0mYKGlzsixz3FuWNR0kdtLkttPc_yDkluF_HvwC38Dvu1jk2U1Vc3rMsbSj8IycqrKxNtFb2mxDepsNti8PeVmDubPdfZXSVxv2pwckNQrQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/01649fbed5.mp4?token=qw1sZoW1Wqq8KX-UMGzAOXxsNdUzPOH2GllBShdi1A4vGjV7eWWOIMOLkzlZnpLtb6HvhhfAIQiDij8OObP0ISShkDapXNm-IFK_d6TDgA7ANpJWkiddTvSs9laaY7q5pRJAJ6bwEOrrJPpp0YuM70LZ9TMo69I3khyvAN2CL_Gli4wzM9RbuKl-y65zx3wsbP599M7z5tus-iLxS0CcexH6yTc_GGXMeO46Svy-66KD3ia60a_JUuQR6fSlsRnU8xM2Lt3rle19Qsob30jbEijt0eGdh4WjyEd6w_1UQiArD4AeF6WiNMf8HqkX5zK30tJl_iwgTW6-tvV2PTKZ-g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/01649fbed5.mp4?token=qw1sZoW1Wqq8KX-UMGzAOXxsNdUzPOH2GllBShdi1A4vGjV7eWWOIMOLkzlZnpLtb6HvhhfAIQiDij8OObP0ISShkDapXNm-IFK_d6TDgA7ANpJWkiddTvSs9laaY7q5pRJAJ6bwEOrrJPpp0YuM70LZ9TMo69I3khyvAN2CL_Gli4wzM9RbuKl-y65zx3wsbP599M7z5tus-iLxS0CcexH6yTc_GGXMeO46Svy-66KD3ia60a_JUuQR6fSlsRnU8xM2Lt3rle19Qsob30jbEijt0eGdh4WjyEd6w_1UQiArD4AeF6WiNMf8HqkX5zK30tJl_iwgTW6-tvV2PTKZ-g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گزارشهای تایید نشده از حمله آمریکا  به پادگان همدان
@WarRoom</div>
<div class="tg-footer">👁️ 138K · <a href="https://t.me/withyashar/19320" target="_blank">📅 16:10 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19319">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">رسانه های رژیم از قول منابع در سپاه : دستور مقامات ارشد سپاه برای گسترش دامنه درگیری در غرب آسیا صادر شده و ضربات در ساعات آینده به مناطق غیرمنتظره خواهد رسید
@WarRoom
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 137K · <a href="https://t.me/withyashar/19319" target="_blank">📅 15:42 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19318">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">بیشترین کمکی که شما به من می‌کنید انتشار این پست است. حتما مطمئن باشید چهار پلتفرم را فالو داشته باشید
🌐
instagram.com/yashar
🌐
t.me/WarRoom
🐦
x.com/yasharrapfa
▶️
youtube.com/yasharrapfa</div>
<div class="tg-footer">👁️ 136K · <a href="https://t.me/withyashar/19318" target="_blank">📅 15:36 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19317">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">WarRoom with YASHAR
pinned «
بیشترین کمکی که شما به من می‌کنید انتشار این پست است. حتما مطمئن باشید چهار پلتفرم را فالو داشته باشید
🌐
instagram.com/yashar
🌐
t.me/WarRoom
🐦
x.com/yasharrapfa
▶️
youtube.com/yasharrapfa
»</div>
<div class="tg-footer"><a href="https://t.me/withyashar/19317" target="_blank">📅 15:34 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19316">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f1db688120.mp4?token=SRacdeGHYlCn8stlijoj6P7iujEGX8RDQihFh7dRhOKC0txg66luZcVbbUUWKTPQpOgrjOHWGbpAykPFZ8kuHoUvE3D2pt9zvgwyqPjBZQYmWViqM6RtI_WmYMuLoc44w872o_HfmiSbc6FxzjQPK-UxlgaJROZMq5MMKZHg8pjIBAWMMkppdBshkww69JDgDtg2sxja65iFdiDpO0lTfA5L80Jhhn0DZJ4s1pSvrFIfdAllH7TbFbmEOC0bEQUcVNGCYFvhFte6S4nbxHoxlxPA7sTEiiJz2RZiugcG1jgRCDySUs-lD9ZkAsEs7BMuHQ0Prfzp0CuSRf9axatpWA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f1db688120.mp4?token=SRacdeGHYlCn8stlijoj6P7iujEGX8RDQihFh7dRhOKC0txg66luZcVbbUUWKTPQpOgrjOHWGbpAykPFZ8kuHoUvE3D2pt9zvgwyqPjBZQYmWViqM6RtI_WmYMuLoc44w872o_HfmiSbc6FxzjQPK-UxlgaJROZMq5MMKZHg8pjIBAWMMkppdBshkww69JDgDtg2sxja65iFdiDpO0lTfA5L80Jhhn0DZJ4s1pSvrFIfdAllH7TbFbmEOC0bEQUcVNGCYFvhFte6S4nbxHoxlxPA7sTEiiJz2RZiugcG1jgRCDySUs-lD9ZkAsEs7BMuHQ0Prfzp0CuSRf9axatpWA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
🚨
🚨
🚨
🚨
🚨
عجب فیلمی‌ بدستم رسید</div>
<div class="tg-footer">👁️ 142K · <a href="https://t.me/withyashar/19316" target="_blank">📅 15:32 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19315">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">🚨
🚨
🚨
🚨
🚨
🚨
🚨
🚨
عجب فیلمی‌ بدستم رسید</div>
<div class="tg-footer">👁️ 129K · <a href="https://t.me/withyashar/19315" target="_blank">📅 15:31 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19314">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hJm9Sy2Nb-eGRj11AK1sk-xy8ZEq5YDgjoLfAg6OFRziPVLxEPtv07kKHAnHrsRRsR0Nh8P389kPqArTvvpBl_-CIhQL4P3Ov1Jd9IIc82kyAGB4ruHMWqoXSgMhRTOScz8sn7oxi-21qDLWRoEoFjk5XRZ1SXRhRbDg-6-9BwrXtZDSBtsh0BBi3XDp7qJst170f56s914laRWzOqdvw2WzcxwOvekzkhMJph4oP61HIN-2Wq5tY9VLTMTFqdEZY3Y14ikL0RQhodHYEg612o8RvAf6Ry0aE-H5a-nSEV7Mf79hI1QI1FNc8UX0vgrsYR2bhkeQ9n53s8FRI92rRg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">موج جدید در این عکس شلیک موشک از شیراز. همچنین دوستی به ارسال عکسی که زود پاک کرد، نتوانستم سیو کنم نوشته بود: شلیک موشک از کرمانشاه به قدری قوی بود که شیشه های مغازهم داشت میشکست.
@WarRoom</div>
<div class="tg-footer">👁️ 135K · <a href="https://t.me/withyashar/19314" target="_blank">📅 15:27 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19313">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">عربستان از فعال شدن هشدارهای زودهنگام حمله موشکی در شهر الدمام خبر داد.
@WarRoom
🚨</div>
<div class="tg-footer">👁️ 134K · <a href="https://t.me/withyashar/19313" target="_blank">📅 15:19 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19312">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">موج جدید حملات رژیم به بحرین
🚨
@WarRoom</div>
<div class="tg-footer">👁️ 137K · <a href="https://t.me/withyashar/19312" target="_blank">📅 15:10 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19311">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">خبرنگار اژدهایی : صدای ۳ انفجار در جزیره لارک و سیریک  شنیده شد
@WarRoom</div>
<div class="tg-footer">👁️ 141K · <a href="https://t.me/withyashar/19311" target="_blank">📅 14:50 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19310">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3ef1b4c242.mp4?token=Yi6HiPuHi8UJvlthI6YTv2KS74lt65ov1AEds44fG-O-dD7xvnI10r9TfOe0_5F7SB2eMITw4dXsQzYm-mC-KXgRNLQUec0mGjQREAzAvJ-EpFu_WpnUxPq0lH4YwCuPOf53sRNKEZ80gI47B2LfeC65YWvFLAtn69Hsb4Iwzl0H6-Ag4d5d_ZVosxiYEnu0MGkt0LXlrkV7GcOUgq0Uggy1Letb_1lyTXPk72HLu6jFrMfwRDeOXZKmNFvZwHeY6UTfFtyFROBSjK9QvSqiNaOh-EvTET8wctlMyjSjhXjG6hPeaxxTe4-PO9DHIwS_fYAtPeuVQrFv2sOz4LvfcA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3ef1b4c242.mp4?token=Yi6HiPuHi8UJvlthI6YTv2KS74lt65ov1AEds44fG-O-dD7xvnI10r9TfOe0_5F7SB2eMITw4dXsQzYm-mC-KXgRNLQUec0mGjQREAzAvJ-EpFu_WpnUxPq0lH4YwCuPOf53sRNKEZ80gI47B2LfeC65YWvFLAtn69Hsb4Iwzl0H6-Ag4d5d_ZVosxiYEnu0MGkt0LXlrkV7GcOUgq0Uggy1Letb_1lyTXPk72HLu6jFrMfwRDeOXZKmNFvZwHeY6UTfFtyFROBSjK9QvSqiNaOh-EvTET8wctlMyjSjhXjG6hPeaxxTe4-PO9DHIwS_fYAtPeuVQrFv2sOz4LvfcA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدیو از سیریک  @WarRoom</div>
<div class="tg-footer">👁️ 143K · <a href="https://t.me/withyashar/19310" target="_blank">📅 14:38 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19309">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">امروز صبح "مهدی خانکی" دانشجوی ۲۵ساله حقوق و از معترضان دی ماه ۱۴۰۴ اعدام شد؛
خبرگزاری میزان (وابسته یه قوه قضاییه) گفته که به دلیل همکاری با اسرائیل و آمریکا و ساخت سلاح و بمب های دست ساز، اعدام شده.
@WarRoom</div>
<div class="tg-footer">👁️ 142K · <a href="https://t.me/withyashar/19309" target="_blank">📅 14:09 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19308">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6c8c355874.mp4?token=lMvI35bkN1nDinxVE0f2ljb39zJmxCVBy1OUBoa9bDnv5AANALp3IZWx7stCOqCV9z_-H2I5r-3UM_NTN9HASGL392xWgzc1sVHL_VaUdtBtoKwmNinN0JRHjYG9HnhBKgLpS4CyIs5FMBcvQMwoiEA_XeEe5rszJTLbEHMibpCelKkkrFJFjsS_9odzqT1HOHH0P3IQNHeLijkjoAcvOETGYzpHwLF_nY5KxynfmOCz47uH1_KvwsgezYvf1g8ulw33-lO7i2KafzBvZaO__5RFibQ3NO5DZpUbA5Qy03fA9DZ2MRjkL1pyn31xaT4amtB8i_ojUuANXaKGE9WcKg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6c8c355874.mp4?token=lMvI35bkN1nDinxVE0f2ljb39zJmxCVBy1OUBoa9bDnv5AANALp3IZWx7stCOqCV9z_-H2I5r-3UM_NTN9HASGL392xWgzc1sVHL_VaUdtBtoKwmNinN0JRHjYG9HnhBKgLpS4CyIs5FMBcvQMwoiEA_XeEe5rszJTLbEHMibpCelKkkrFJFjsS_9odzqT1HOHH0P3IQNHeLijkjoAcvOETGYzpHwLF_nY5KxynfmOCz47uH1_KvwsgezYvf1g8ulw33-lO7i2KafzBvZaO__5RFibQ3NO5DZpUbA5Qy03fA9DZ2MRjkL1pyn31xaT4amtB8i_ojUuANXaKGE9WcKg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">چند انفجار پی‌درپی سیریک
🚨
🚨
🚨
@WarRoom</div>
<div class="tg-footer">👁️ 145K · <a href="https://t.me/withyashar/19308" target="_blank">📅 14:06 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19307">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">‏کانال ۱۴ اسرائیل گزارش داد که کشورهای اطراف خلیج فارس در مورد چگونگی واکنش به رژیم اشغالگر جمهوری اسلامی اختلاف‌نظر دارند. برخی به پرزیدنت ترامپ فشار می‌آورند که به ایران حمله زمینی کند و برخی دیگر خواستار مذاکره ترامپ با ایران و اعلام آتش‌بس فوری هستند.
@WarRoom</div>
<div class="tg-footer">👁️ 145K · <a href="https://t.me/withyashar/19307" target="_blank">📅 13:42 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19305">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">شبکه کان اسرائیل : جولانی اماده حمله به حزب الله می شود
@WarRoom</div>
<div class="tg-footer">👁️ 149K · <a href="https://t.me/withyashar/19305" target="_blank">📅 13:17 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19304">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">وب‌‌سایت عربی ارم‌ نیوز:آمریکا به پاکستان اطلاع داده است در شرایط فعلی با آتش‌بس با ایران موافقت نخواهد کرد.
آمریکا به پاکستان اطلاع داد که برای ایجاد آتش‌بس و میانجیگری بین آمریکا و ایران اقدامی نکند، آمریکا میخواهد تمام توانمندی‌های تهاجمی سپاه رو از بین ببرد.
@WarRoom
🚨
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 149K · <a href="https://t.me/withyashar/19304" target="_blank">📅 13:13 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19303">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">‏منوچهر متکی: به محض حمله زمینی آمریکا، حمله زمینی جمهوری اسلامی به بحرین و کویت آغاز خواهد شد
@WarRoom
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 146K · <a href="https://t.me/withyashar/19303" target="_blank">📅 13:10 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19302">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">چند انفجار پی‌درپی سیریک
🚨
🚨
🚨
@WarRoom</div>
<div class="tg-footer">👁️ 145K · <a href="https://t.me/withyashar/19302" target="_blank">📅 13:05 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19301">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">گزارش انفجار‌ سیریک
🚨
🚨
🚨
🚨
@WarRoom</div>
<div class="tg-footer">👁️ 144K · <a href="https://t.me/withyashar/19301" target="_blank">📅 13:04 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19300">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">از چه زمانی متوجه شدید جمهوری اسلامی جنایت کار است و اصلاح شدنی نیست</div>
<div class="tg-footer">👁️ 143K · <a href="https://t.me/withyashar/19300" target="_blank">📅 13:02 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19299">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-footer">👁️ 147K · <a href="https://t.me/withyashar/19299" target="_blank">📅 12:58 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19298">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">@WarRoom
ترکش های پرتاب شده به اسرائیل</div>
<div class="tg-footer">👁️ 139K · <a href="https://t.me/withyashar/19298" target="_blank">📅 12:37 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19297">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">@WarRoom
روح و روان</div>
<div class="tg-footer">👁️ 141K · <a href="https://t.me/withyashar/19297" target="_blank">📅 12:36 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19295">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LddbALYpZNo4D-OcoUWrBN3Q8QeOCqLgMDS7zVwCEn5lpgr8iDQCVFSmLv_ftU9nU3ru2jyIp6bTkiQfCncHVEFv5qGpcyVwhiy7NiaSF0q6-bjNXBu3odaMpr1twXpQPGF8ttbMqCguPZT2xiQ1LTvGEXI73DdQU22_j8mk6ANuiRwTmqa5902erzTva5AMUym3RIQ3JcBTHEiyp2UK7S1vs6QNnMOSzz5alP-ADUvvMUfmmHTqlX0e7G7HiI9pl_6fxkNct4wwkgqNLoMBFFwvT15HZCEDiTMN2dQHf0LXGdPh5DxTeNnyTJFZ-m2NhAwmoEPO38rTxo0BoI1jjA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ogwPi9Vg_5rQjEA55_jzbvUND3WAJx82R23qlg4eKxLBGUXA0YUvIRWZ3Qm6qQjFjPqaLTvqnHtUcLYx2T1kZv1_TurqpC_geugNjRDM58cGHAHorIFQ_gmSMD6Jcb9wUgI3q-1HxlctRa-BfAT12aJnHja69l8guyjjyNzWLAILLlQAHw8u8v9c-Xv8KubE8jTC1ZnpTp1CbQ_laNz7jFeXSyFsgKEAPrsJmdRpZoQFl-n6WRFBMphxpE3J2U0er3aX6YGAWvDuOtcIkLLwFiL98Oqn13mq9guee5ApKZXGw43pzFscU9fxYVnae6f6DshSTlShLyJoQV4b6S2A_A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">تصایور جدید از انفجار‌ گاز در نارمک !
@WarRoom
که دیشب یه عده به من اومد توهین کردن !</div>
<div class="tg-footer">👁️ 152K · <a href="https://t.me/withyashar/19295" target="_blank">📅 12:20 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19294">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/citLHOFCQqdVXVOAIdJltM_JFsVmEUfmOlwM8jjnd7ayY8KMUfm-zOoH7X9bE0VCNM1Lwys7vUaqdeOMzmKKC6kFTCXune6bZ8_-MC0eZHUQeUiVnZ3qPR4sVjY8xLJcKapuBbPbwv6NaM0PV-dwbVv7yfM84LvBwJn_UWl4kanzQPxfLjRek81sOIgtB6hP5Tz6cbamzQzt18UC3_LWWTzIGaO-WLtiIyyso7xwne8tiIBSo7phvVomaBy5JO6WoZjP7dXzkHv_dR716z8y-nK-ePFgoyoQQwDf8mKqAgr95RQ05kkjzS6L_HJWZ70bHOIwaCrurkCoL6ki9aueRQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یاشار : نفت به کانال مذاکرات و توافق رسید
نفت برنت به ۹۵$ رسید و هم اکنون ۹۴ معامله میشود
@WarRoom
🚨</div>
<div class="tg-footer">👁️ 156K · <a href="https://t.me/withyashar/19294" target="_blank">📅 12:08 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19293">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">ارتش جمهوری اسلامی : پایگاه "الأزرق" در أردن و پایگاه "الشیخ عیسی" در بحرين را هدف قرار دادیم
@WarRoom</div>
<div class="tg-footer">👁️ 160K · <a href="https://t.me/withyashar/19293" target="_blank">📅 09:53 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19292">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">نتیجه جلسه دیشب : این یک جلسه بررسی و پرسش‌وپاسخ بود ، جمهوری‌خواهان عمدتاً از او حمایت کردند، اما دموکرات‌ها به‌شدت از نحوه مدیریت جنگ با ایران، هزینه‌ها و نبود شفافیت انتقاد کردند ،
هگست موفق شد از مواضع دولت دفاع کند، اما هنوز موفق به گرفتن بودجه از سنا نشده است
. روند تصویب ادامه دارد و احتمال دارد رأی‌گیری نهایی در هفته‌های آینده یا پس از بازگشت کنگره از تعطیلات انجام شود
@WarRoom</div>
<div class="tg-footer">👁️ 163K · <a href="https://t.me/withyashar/19292" target="_blank">📅 09:46 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19291">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-footer"><a href="https://t.me/withyashar/19291" target="_blank">📅 09:28 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19290">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">‏معاون استاندار همدان اعلام کرد دیشب چند نقطه در شهرستان کبودرآهنگ هدف حمله هوایی آمریکا قرار گرفته و تاکنون جزئیاتی درباره اهداف، خسارات یا تلفات احتمالی منتشر نشده است.
@WarRoom</div>
<div class="tg-footer">👁️ 161K · <a href="https://t.me/withyashar/19290" target="_blank">📅 09:26 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19289">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/seSa16GNYqM_eQ_baii-lU41qbdsC3-8Zjfb8M_H5iFSbywld8baW8yg9xsBlbYV3aZuWsqgZAeCbDl3KSEu18qg8FnsIBWUtivCvzyk0-ctNC_XF9zuvIUy3O9kcYIl1cI97CcRGEOkkbH7BX52Z_t-2Y4g2BASOhUm01NzfvDbbRXrBmQmyXV1hLCICAU2Ku-KnTZtSOIUR3teRjuZd7m_Ni95bQ2nSfsRdF-8qsZXbZWJOq4mXqfWFBoRvZdSp59ojgY5ryu2QKdDq-DzIcKRaL9A1N7v1-54BwmOSW4byQ-uUG7TlvqyOXzAiwkEtLOGyiw-B0bzj22Jozvlhg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تمامی نقاطی که گزارش انفجار ارسال شده (حتی تایید نشده)
@WarRoom</div>
<div class="tg-footer">👁️ 166K · <a href="https://t.me/withyashar/19289" target="_blank">📅 08:43 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19288">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">اسپانیا ممنوعیت پرواز بر فراز حریم هوایی خود برای نیروی هوایی آمریکا را که در جنگ علیه ایران شرکت دارد، تداوم بخشید.
@WarRoom</div>
<div class="tg-footer">👁️ 160K · <a href="https://t.me/withyashar/19288" target="_blank">📅 08:35 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19287">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">فهرست حملات آمریکا در بامداد چهارشنبه
💥
سیریک (هرمزگان)
💥
بوشهر
💥
بهبهان (خوزستان)
💥
امیدیه (خوزستان)
💥
تبریز
💥
چابهار(سیستان و بلوچستان)
💥
کنارک (سیستان و بلوچستان)
💥
چوار (ایلام)
💥
آبدانان (ایلام)
💥
بانه (کردستان)
🚨
تهران: صدای شلیک پدافند @WarRoom</div>
<div class="tg-footer">👁️ 158K · <a href="https://t.me/withyashar/19287" target="_blank">📅 08:35 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19284">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/630b6aa1be.mp4?token=t5jc1uPmLrIes_nnr4SBHwoW9fgu8i_vnQ1gP630UFmttucF10hX-6tTYOtSdidyDJzucEpW6bqm5PnjGqBtan0R07iU265ZNxopisbCrhG732SX60_lFpQ_q2CTwI-tT6rRiKEV4YBHg8x5haeCKmjfv4_6i8-hAg_9PE0x3SuvJiACn83T_J7S4jhHzLuqCWhytSKmLxyEnl6k89JboRkyTlrM9aPDrY3f0PrOvdnjf7wwWL9KGshDeRS1HjPW-WGkeLJm-xHGFFgN3n_FStQJkNf-RSkzwFRuADty3Xx3Te3kmUZkez4TCE51RGgGIA2V9R8taScMlnN2xBb69Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/630b6aa1be.mp4?token=t5jc1uPmLrIes_nnr4SBHwoW9fgu8i_vnQ1gP630UFmttucF10hX-6tTYOtSdidyDJzucEpW6bqm5PnjGqBtan0R07iU265ZNxopisbCrhG732SX60_lFpQ_q2CTwI-tT6rRiKEV4YBHg8x5haeCKmjfv4_6i8-hAg_9PE0x3SuvJiACn83T_J7S4jhHzLuqCWhytSKmLxyEnl6k89JboRkyTlrM9aPDrY3f0PrOvdnjf7wwWL9KGshDeRS1HjPW-WGkeLJm-xHGFFgN3n_FStQJkNf-RSkzwFRuADty3Xx3Te3kmUZkez4TCE51RGgGIA2V9R8taScMlnN2xBb69Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدیو های حمله به پادگان بخردیان بهبهان
@WarRoom</div>
<div class="tg-footer">👁️ 156K · <a href="https://t.me/withyashar/19284" target="_blank">📅 08:31 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19282">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Gr1FP8vDT8MdPNm7AMIWovZ8m4M9rnCwlBQNMqWRWPjbSmSNV_oHYlAx4kYCWDoMZwci2-6zBKXCPyEfRSYSNDXnj_ylHk660KP1zl1u49hy055pTbjpPZjcv36M3U_LYIoGXu2lwk2ShNLGSWBP6tANZbBEseI539URbxvbzkN5vtXUVbmrs3xgJTcBM_h3W9s5iDu9Guh9UFaRmLmkakfar927j-Jgr7GHoT75sCn1ybjzNTY2Tm1sg1k4DPLvBHA7mStFkrBbR1enU_kviKUKLrHKThm7eXS93mJ8xV5s6MYVIwuwACkwOPjHk8rOCQdcQ9aIgOg-5zj3OVyhPQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/k-XF7p9vkSNu5QxvZBfEsFhd4be1Z5b5j7q5Rbz5XGdkG5d-CwN4OqUgyieP8aJwwI4XAbGif3fpmrNgUgvmQN09P8IJLGW1v7cEe2bH8zF6YHyg8bDHgqXxcrvDqHYmSg8CVMf1aAtrWgIYEaiN6kIbNsaQ4CSOZM3m3Sv-w9nRfAd0B7iw_M1zXKzs0z_dgtGHK4BERb3ftxKfM6gbWMVUG3YBr1CENOOXQEWsKGV-0Ta5bMXQnk67pdXm-nT4SglWUtdpJfGEWaAH7MTdyfOm_evs0bY59uQKe01cxWkmfiIfNLj82iD6w_UKsfKPdAf3UKZcuGkGiek39jj6xw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">فهرست حملات آمریکا در بامداد چهارشنبه
💥
سیریک (هرمزگان)
💥
بوشهر
💥
بهبهان (خوزستان)
💥
امیدیه (خوزستان)
💥
تبریز
💥
چابهار(سیستان و بلوچستان)
💥
کنارک (سیستان و بلوچستان)
💥
چوار (ایلام)
💥
آبدانان (ایلام)
💥
بانه (کردستان)
🚨
تهران: صدای شلیک پدافند @WarRoom</div>
<div class="tg-footer">👁️ 149K · <a href="https://t.me/withyashar/19282" target="_blank">📅 08:30 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19281">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kacCWa5JtlXlNYsNmPwvDqqkoaTOGGQvpNZmiHBj7XKvGSc9p6xOz6chdez_VMHfshwfPRgsDKOPFtg-VJrjl-FT_Y_LavBti7h_aPU76KQBMhe3mLT2dqeTwzDChB-B64Jl7J2oHfvhrr7B3GRhkqcHv0e-fpD2zxu7NikeJ2GT-8OTgLxZWm9a16aKKR_JSPgqvoA5p81n5Te8SDsiv8mLjNgHOSji5bh-BFdizGNODDzbVVVy6saB2xzkXp3XJwZ9aGEW-th5sY0lB_8yLMaeieShgfsjuuM7XDohnlj1Kx_eNi3Yzo5aWjQQuNB18XC1OMLZGj-HCkrLmtCeXg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هواپیمای ارتباطات هوایی آمریکایی مدل E-11A BACN (روتر وای‌فای در آسمان )از آمریکا به پایگاه هوایی رامشتاین آلمان رسید و احتمالاً در ادامه به پایگاه الامیر سلطان در عربستان سعودی منتقل خواهد شد، جایی که در حال حاضر بین ۴ تا ۵ فروند از همین نوع هواپیما مستقر هستند.
@WarRoom</div>
<div class="tg-footer">👁️ 149K · <a href="https://t.me/withyashar/19281" target="_blank">📅 08:27 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19280">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">انفجار بامداد امروز در نارمک تهران یک انفجار نامشخص باعث شد میله‌ها و ورق‌های پلاستیکی به اطراف پرتاب شده و سه تا از شیشه‌های خانه های مجاور شکسته و به خودروی ام وی ام پارک شده هم خسارت جزئی وارد شود، اما حادثه مصدومی نداشت. @WarRoom</div>
<div class="tg-footer">👁️ 149K · <a href="https://t.me/withyashar/19280" target="_blank">📅 08:24 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19279">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">انفجار بامداد امروز در نارمک تهران
یک انفجار نامشخص باعث شد میله‌ها و ورق‌های پلاستیکی به اطراف پرتاب شده و سه تا از شیشه‌های خانه های مجاور شکسته و به خودروی ام وی ام پارک شده هم خسارت جزئی وارد شود، اما حادثه مصدومی نداشت.
@WarRoom</div>
<div class="tg-footer">👁️ 154K · <a href="https://t.me/withyashar/19279" target="_blank">📅 08:20 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19278">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">فهرست حملات آمریکا در بامداد چهارشنبه
💥
سیریک (هرمزگان)
💥
بوشهر
💥
بهبهان (خوزستان)
💥
امیدیه (خوزستان)
💥
تبریز
💥
چابهار(سیستان و بلوچستان)
💥
کنارک (سیستان و بلوچستان)
💥
چوار (ایلام)
💥
آبدانان (ایلام)
💥
بانه (کردستان)
🚨
تهران: صدای شلیک پدافند
@WarRoom</div>
<div class="tg-footer">👁️ 169K · <a href="https://t.me/withyashar/19278" target="_blank">📅 08:10 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19277">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/11cb529807.mp4?token=ObyTX6I-HohtwlEuQ6-aMwJZg7M8hqGRjIplo5zlhjKmm2SHbUH8BF8qyirCJyuB36L6Ux7ouMVkdYtnOGcOv898zTlRzrwkNHxK4Qb7yRPSkG8EhYI1FAnq0IFy-NyiD0GlAeXRW33zQV-kgKM-ns-bn5327XRfSw97GTsSGxGy6tsglVedhp0uWzynMUWftU892fZP0UtxmxB2VOlGGEWR6A7qIeOEM1GQF-GntAIiTat7_a3929NsudtuFfXc8daCS4vzSVALilvHjYFUqTyzddHbr0Dk4ccaFnW1ERCTj9odyRVilN3PlXV2LBvwxTlMkcX5iQXQlXMX3eQjzQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/11cb529807.mp4?token=ObyTX6I-HohtwlEuQ6-aMwJZg7M8hqGRjIplo5zlhjKmm2SHbUH8BF8qyirCJyuB36L6Ux7ouMVkdYtnOGcOv898zTlRzrwkNHxK4Qb7yRPSkG8EhYI1FAnq0IFy-NyiD0GlAeXRW33zQV-kgKM-ns-bn5327XRfSw97GTsSGxGy6tsglVedhp0uWzynMUWftU892fZP0UtxmxB2VOlGGEWR6A7qIeOEM1GQF-GntAIiTat7_a3929NsudtuFfXc8daCS4vzSVALilvHjYFUqTyzddHbr0Dk4ccaFnW1ERCTj9odyRVilN3PlXV2LBvwxTlMkcX5iQXQlXMX3eQjzQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سنتکام :
امروز ۰۲:۳۰ بامداد
۳۱ تیر به وقت تهران حملات خود را آغاز و ۰۳:۴۵ بامداد (در ۷۵ دقیقه)
با موفقیت
یازدهمین شب متوالی حملات
علیه ایران را به پایان رساندیم.
نیروهای سنتکام
مراکز عملیات نظامی، توانمندی‌های دریایی، آشیانه‌های هواپیما، تأسیسات نگهداری پهپاد و زیرساخت‌های لجستیکی نظامی ایران
را هدف قرار دادند تا توانایی ایران برای تهدید کشتیرانی تجاری در
تنگه هرمز
بیش از پیش تضعیف شود
@WarRoom</div>
<div class="tg-footer">👁️ 170K · <a href="https://t.me/withyashar/19277" target="_blank">📅 07:54 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19276">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-footer"><a href="https://t.me/withyashar/19276" target="_blank">📅 02:16 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19275">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">میرم بخوابم بعضی ها لیاقت ندارد انگار خرج منو میدن نمیفهمن این گزارشات بر پایه پیغام های زیاده حالا حمله نبوده باشه یه عنی صدا داده که پیغام دادن این همه آدم ، شب خوش
🙌🏾</div>
<div class="tg-footer">👁️ 186K · <a href="https://t.me/withyashar/19275" target="_blank">📅 02:15 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19274">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">گزارش صدای انفجار تهران نارمک
🚨
🚨
🚨
🚨
🚨
@WarRoom</div>
<div class="tg-footer">👁️ 191K · <a href="https://t.me/withyashar/19274" target="_blank">📅 02:07 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19273">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">گزارش انفجار ‌بوشهر
🚨
🚨
🚨
🚨
🚨
@WarRoom</div>
<div class="tg-footer">👁️ 188K · <a href="https://t.me/withyashar/19273" target="_blank">📅 01:59 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19272">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uE7wr9PwAGt8EB-4h44u1bsZUq7ivoSjORxlG3uo-0zjEdbIo1KVnV0Kqjg2uCerPjgp5PTm_3lPcRrXdjHSnmA-RpyNzaPTCO2TP8ZwXr7T_VVcBY_E4-_7D7U9k6M7AESZCcWzIY6uuzRETClcY7yS6GPb2W4nNGzJ-_HE78nbljgWuGp6rE7hqyOdg8QGk-hEUWAekMZ2oCppzWZyC9k3ZfMzGyio5---44-zveKL4E45HNCwh5GvCGpRnrdYHh-61YuxlfyZ93hm6iKKmVpWLqIpaSKhR_jNohrq7-bgsZx4qw-v6gHBUCX8gmZ5-1H3xhBAF6oqgzVkhCoP9w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">۱۲-۶‏ فروند وارتاگ A10 با کیت جدید سوخترسانی هوایی بر فراز مدیترانه و در حالی که به سمت اردن در پرواز بودن از صفحه رادار محو شدند.
@WarRoom</div>
<div class="tg-footer">👁️ 190K · <a href="https://t.me/withyashar/19272" target="_blank">📅 01:59 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19271">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">ارتش کویت: پدافند هوایی در حال مقابله با حملات پهپادی از سوی ایران است
@WarRoom</div>
<div class="tg-footer">👁️ 181K · <a href="https://t.me/withyashar/19271" target="_blank">📅 01:30 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19270">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">گزارش صدای انفجار / درگیری پدافند در بحرین
@WarRoom
🚨</div>
<div class="tg-footer">👁️ 182K · <a href="https://t.me/withyashar/19270" target="_blank">📅 01:28 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19269">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">جمهوری اسلامی دید امریکا نمیزنه خودش شروع کرد ، از ملارد موشک الان پرتاب کرد
@WarRoom
🚨</div>
<div class="tg-footer">👁️ 185K · <a href="https://t.me/withyashar/19269" target="_blank">📅 01:25 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19268">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gvw_q3ulcq5y8DxcXBGiF0mvhiVW_h78xpO0YW4nbGe9CpDeI668V2apgAMS9h01v8uxqOvS4_C7St86bAVadqKtr70t7IGpGEeQp1AukTKVIsR0jeCCGnLUoyO5hdRIhJ0FY3l0Ao2A5C5czRC7eO7S27O_t3YuWYtb_oYr2ic78mXxmk7N5XV6vlImvomYZ2F5DxMLf6RmsnM45E95Y3tXBDwscE3dnYcCvXvQRZ2AygUv41Kd-sbg6lbP2a-1Bi7dyHks_OZdCdEiATow0ba8wpq3fkyxekciAT0DQpv5mky-EOHHcTRQ62fjhajEE1-lM01EUMcmJ2gDfvFDxg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سوأل امتحان تاریخ سال ۲۶۰۰ شاهنشاهی (۱۵ سال دیگه) امشب اینجا دود میشه
@WarRoom</div>
<div class="tg-footer">👁️ 189K · <a href="https://t.me/withyashar/19268" target="_blank">📅 01:04 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19267">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">هم اکنون ۶ سوخترسان از اسرائیل بلند شدند و چند سوخترسان به همراه هواپیمای  آواکس از سعودی @WarRoom</div>
<div class="tg-footer">👁️ 179K · <a href="https://t.me/withyashar/19267" target="_blank">📅 00:39 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19266">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">قرارگاه مرکزی حضرت خاتم‌الانبیا(ص): آمریکا مراکز هسته‌ای و حساس ایران اسلامی را تهدید به حمله نموده است اعلام می‌گردد چنانچه آمریکا وارد چنین مرحله‌ای بشود، آن را به عنوان توسعه جنگ در منطقه می‌دانیم و همه منافع آمریکا، هم‌پیمانان و حامیان آن ، هدف هجوم قدرتمند نیروهای مسلح جمهوری اسلامی قرار خواهند گرفت.
@WarRoom</div>
<div class="tg-footer">👁️ 181K · <a href="https://t.me/withyashar/19266" target="_blank">📅 00:26 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19264">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-footer">👁️ 180K · <a href="https://t.me/withyashar/19264" target="_blank">📅 00:11 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19263">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">بیشترین کمکی که شما به من می‌کنید انتشار این پست است. حتما مطمئن باشید چهار پلتفرم را فالو داشته باشید
🌐
instagram.com/yashar
🌐
t.me/WarRoom
🐦
x.com/yasharrapfa
▶️
youtube.com/yasharrapfa</div>
<div class="tg-footer">👁️ 183K · <a href="https://t.me/withyashar/19263" target="_blank">📅 00:01 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19262">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">بیشترین کمکی که شما به من می‌کنید انتشار این پست است. حتما مطمئن باشید چهار پلتفرم را فالو داشته باشید
🌐
instagram.com/yashar
🌐
t.me/WarRoom
🐦
x.com/yasharrapfa
▶️
youtube.com/yasharrapfa</div>
<div class="tg-footer">👁️ 187K · <a href="https://t.me/withyashar/19262" target="_blank">📅 00:00 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19261">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWarRoom with YASHAR</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">(IG @yashar)‎⁨منتظریم کی شب حمله فرا می‌رسد⁩</div>
  <div class="tg-doc-extra">اتاق جنگ با یاشار (t.me/withyashar)</div>
</div>
<a href="https://t.me/withyashar/19261" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🌐
instagram.com/yashar
🌐
t.me/withyashar</div>
<div class="tg-footer">👁️ 173K · <a href="https://t.me/withyashar/19261" target="_blank">📅 23:56 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19260">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">هگست وزیر جنگ آمریکا در سنا:
آیا شما می‌خواهید که اسلام‌گرایان افراطی یک بمب هسته‌ای داشته باشند که بتواند کل جهان را تهدید کند؟
@WarRoom
یاشار : عمو هگست داره سنا میجنگه پول جنگ رو بگیره امشب</div>
<div class="tg-footer">👁️ 174K · <a href="https://t.me/withyashar/19260" target="_blank">📅 23:53 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19259">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Gjbq9zAeGkQD9lsDUQb7dIw5YKitMN09XbdR8CM7QQx6Judz6xl1UyDxk0_OyM07tIJ3f-CZSbL57BwWE4zx-uX5YcQruv7CJg-Ic9BZOrFDx_lYK2IWM8H1M46eaxcx9Bu1GSD2Y3E8rP08eOsoD9ytwnePbQhYW54tXhP6FOFPMvuEw3iYJ6v0CIAeXcMj9XecMDt9v0OTQZWgJqGU2BNO_-WnRpsxh7ZierFMR7dx96MlzGVGQiV5_x10u0y1C8yfq7QGpBfC68XZhwzLzex-H0S2and4pFhQtkFZXFO8qEvUFw6jgdajnxUQ5_yo7eu9LAIrjCfEaCiI1v1elw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هم اکنون ۶ سوخترسان از اسرائیل بلند شدند و چند سوخترسان به همراه هواپیمای  آواکس از سعودی
@WarRoom</div>
<div class="tg-footer">👁️ 179K · <a href="https://t.me/withyashar/19259" target="_blank">📅 23:42 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19258">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">🚨
🚨
🚨
🚨
🚨
🚨
🚨
کمر بند ها رو ببندید
@WarRoom
🚨
🚨
🚨
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 167K · <a href="https://t.me/withyashar/19258" target="_blank">📅 23:39 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19257">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JW1H-K78aUu1S1dY3rRmCU2kOn5vT9j5dq8k6dY2N1H3N4nNCl-bMysFr6ssGi12aTa0y2yRs-T5PP_vIQcJ1q16VCmmUWGePXcoGrTOrjVkUfFw90vcXlf0pJibjQ5ly8e-bAbXMmZpBDXbpEKKNh9J_Moh8hSae2fr_6AeB1MFXeIgDC46s3_zujzLii_VFC_ZximP3uhjts74YzDjk12sg6Bd4n8JHIYsza1Cl0x7MhMsrKTw7yuchvWwRWpnXUFtRq1vTd_m5EMtpIpEmL8hdKLCrGU2KkPG5Xg04BNVWHSvq1CLhqoccB5no5VblOsaQVeJ92-DAwlmejNaZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ در ‌تروث:
جنگ در افغانستان: ۲۰ سال، ۲۰۰۰ کشته.
جنگ در عراق: ۹ سال، ۴۶۰۰ کشته.
ویتنام: ۱۹ سال و ۵ ماه، ۵۸۲۲۰ کشته.
کره: ۳ سال و ۱ ماه، ۳۶۵۷۴ کشته.
جنگ در ونزوئلا: ۱ روز، صفر کشته.
درگیری در ایران: ۴ ماه، ۱۸ کشته.
@WarRoom</div>
<div class="tg-footer">👁️ 171K · <a href="https://t.me/withyashar/19257" target="_blank">📅 23:35 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19256">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">پیت هگست، وزیر جنگ ایالات متحده، در جلسه سنای آمریکا به سوالات پاسخ داد و گفت که جنگ با ایران تاکنون ۳۷.۵ میلیارد دلار هزینه داشته است. وی افزود که بدون افزایش فوری بودجه، کاهش آموزش نظامی ضروری خواهد بود.
@WarRoom
یاشار : فاکتورمون داره میره بالا
🥴</div>
<div class="tg-footer">👁️ 166K · <a href="https://t.me/withyashar/19256" target="_blank">📅 23:33 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19255">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-footer">👁️ 165K · <a href="https://t.me/withyashar/19255" target="_blank">📅 23:30 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19254">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">🚨
🚨
🚨
🚨
🚨
@WarRoom
روز ۳۱ تیر</div>
<div class="tg-footer">👁️ 168K · <a href="https://t.me/withyashar/19254" target="_blank">📅 23:26 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19253">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c7699bf9bb.mp4?token=WTUPhHyvHNnBVK-Y6cz7tP1RK37LTaFO-lQfyIIWM0L03eiJqyxHprP_w46rRqytKVNm-F-MJt5sZlaK4xx8MrUex9PtSBglR_aBxyBtj9b5ymHJ2pigYF8vYvmiVJE-4Jbpzp_C-rCU4ZUFpuCO_alv61Pt9A3Fb5h8HUb0Enhk76TpORHLXHE9Jbv8xowqQmHdxpNlQWwRoifn4vKxS5kPYdtIia_VH1LJfl24pYWcMHV2smOgmWcoIqMOEgivpMKq8zXtGcVK5-qotqjk1QH7hJ8U54m4L5mqTSB5s6rTvV-TZr1riQ_M6B8LRZW6NGi0Hh_pBG_BJpQ4JEoT4A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c7699bf9bb.mp4?token=WTUPhHyvHNnBVK-Y6cz7tP1RK37LTaFO-lQfyIIWM0L03eiJqyxHprP_w46rRqytKVNm-F-MJt5sZlaK4xx8MrUex9PtSBglR_aBxyBtj9b5ymHJ2pigYF8vYvmiVJE-4Jbpzp_C-rCU4ZUFpuCO_alv61Pt9A3Fb5h8HUb0Enhk76TpORHLXHE9Jbv8xowqQmHdxpNlQWwRoifn4vKxS5kPYdtIia_VH1LJfl24pYWcMHV2smOgmWcoIqMOEgivpMKq8zXtGcVK5-qotqjk1QH7hJ8U54m4L5mqTSB5s6rTvV-TZr1riQ_M6B8LRZW6NGi0Hh_pBG_BJpQ4JEoT4A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سنتکام : هر موفقیت عملیاتی در خاورمیانه با تمرکز اعضای ارتش بر مأموریت‌هایشان بدست می آید، از جمله محاصره ایران توسط ایالات متحده، آغاز و پایان می‌یابد. تا ۲۱ ژوئیه، نیروهای آمریکایی ۸ کشتی تجاری را تغییر مسیر داده(۱ کشتی‌امروز) و ۱ کشتی را غیرفعال کرده‌اند تا محاصره را به طور کامل اجرا کنند.
@WarRoom</div>
<div class="tg-footer">👁️ 169K · <a href="https://t.me/withyashar/19253" target="_blank">📅 23:20 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19252">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">بمب اتم بزنه به کمر کسی که این خبر فیک رو پخش‌کرد !!! نترسید الان زمان جنگ جهانی دوم نیست ، جمهوری اسلامی هم امپراتوری ژاپن نیست !</div>
<div class="tg-footer">👁️ 167K · <a href="https://t.me/withyashar/19252" target="_blank">📅 23:07 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19251">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-footer"><a href="https://t.me/withyashar/19251" target="_blank">📅 23:05 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19250">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">من چت جی پی تی‌نیستم دایرکت ندید !</div>
<div class="tg-footer">👁️ 167K · <a href="https://t.me/withyashar/19250" target="_blank">📅 23:04 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19249">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">‏بلومبرگ گزارش داد اندی برنهام، نخست‌وزیر جدید بریتانیا، با استفاده آمریکا از شماری از پایگاه‌های نظامی این کشور برای انجام حملات علیه رژیم جمهوری اسلامی موافقت کرده است.
@WarRoom
عمو عندی
🤣</div>
<div class="tg-footer">👁️ 171K · <a href="https://t.me/withyashar/19249" target="_blank">📅 22:49 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19248">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">🚨
🚨
🚨
🚨
🚨
🚨
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 169K · <a href="https://t.me/withyashar/19248" target="_blank">📅 22:43 · 30 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>

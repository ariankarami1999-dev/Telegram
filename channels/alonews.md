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
<img src="https://cdn4.telesco.pe/file/ZPSi90vRTDu91IdczzyjE9fw1FWiyCs2jDhaycyQK1U3sOidwlYF83dvDkwBfMmKM_SR7h-ydBliikj3CZvytwqdnHuT6u91Ogrlvt108zv0-jMkpPA6jyK-sNdHQ7LX7xroOg7r5dL7URCrmVKcvpSJzpa5jzzxYhmJidIqIVTRfe0huENWHehycAXVtemd9-G8RQHl4ff2C_uBEIjvqCqom8EJfMpuQ0MToUeyK1qQ2EW_H2KhGjkLAk_teovl5acPVX0d3nHEcRuNNbsG5CMunicQ1RkIWqQwCOlUxBRD7qYhJCOmAM79aiwTf7pUB7JMwcclVxps4Ht8wzEQrw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 اخبار جنگ الونیوز AloNews</h1>
<p>@alonews • 👥 982K عضو</p>
<a href="https://t.me/alonews" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 با الونیوز از اخبار جنگ و وقایع در چند ثانیه مطلع باش!اخبار جنگ بدون سانسور در الونیوز👌جهت رزرو تبلیغات👇https://t.me/ads_alonewsپشتیبانی کانال🕵️https://t.me/AloNews?directمالک کانال🎩@AloNewsBotX:https://x.com/AloNewsBot</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-29 13:49:48</div>
<hr>

<div class="tg-post" id="msg-148353">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f5a87d1892.mp4?token=J37FSYtRWcqO_P-dZdYBYSTR0dFuKXJ3huiRgVw0l18My_i_3sI_JofGwBMF043fpDRigRP6LV65BYWz5iRGoXMJIyvYD-JTbd2aXtBZ1uPYMPnpA43gXx75b-1yg1RTFC35Bo2o-YFmKlXOBp0gXQbPm2mRGwcUfXZ0bHQPCAYGH_4FA4ErKCN4Qa94ET4cUzW7QaG28ZG4ad60v9q_biWmpXX2uXF0sdc1JN-GzAwPkgzLlAhtOFqWFkwn9R7CbzvocCbNOTl3K7fLBkcNY2f7RFWiQGQHH9XA88Flyj3FU3uwhi2JXRYebIM-NU3wRYM0YKM82-XfIxsY7d1DPbjfQtvJCWnzpbJW3oawVCfvpowuwJ2geUW3a5tF5ml0nOj6bATnVr7nWWs_DQExm8fOxbm8t5jHohRKQekuIhOWq6m1igTepaLkl5g8Z9ymwJCspYnXDBJYHLGUbA0NJBlkg3pxnvn9kycF1_Uv4ePIzjw7DulDuZOsRwYymj8Chs7ismJWaYUSWzQSpg0Sz3DePD22kn3gV_WsNT3DX421CwE0hmcEnrQujW1290B6PiG4ywIHBcp7Dw0nCGYVd3B3RBGFoveUCtjq97A0tC1BLlDHYKnlasqrVkg7ZA4oOCsXwpZGG4hQYhBAbYZI4E7DVh_yx3IaSA1FZwnZMVg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f5a87d1892.mp4?token=J37FSYtRWcqO_P-dZdYBYSTR0dFuKXJ3huiRgVw0l18My_i_3sI_JofGwBMF043fpDRigRP6LV65BYWz5iRGoXMJIyvYD-JTbd2aXtBZ1uPYMPnpA43gXx75b-1yg1RTFC35Bo2o-YFmKlXOBp0gXQbPm2mRGwcUfXZ0bHQPCAYGH_4FA4ErKCN4Qa94ET4cUzW7QaG28ZG4ad60v9q_biWmpXX2uXF0sdc1JN-GzAwPkgzLlAhtOFqWFkwn9R7CbzvocCbNOTl3K7fLBkcNY2f7RFWiQGQHH9XA88Flyj3FU3uwhi2JXRYebIM-NU3wRYM0YKM82-XfIxsY7d1DPbjfQtvJCWnzpbJW3oawVCfvpowuwJ2geUW3a5tF5ml0nOj6bATnVr7nWWs_DQExm8fOxbm8t5jHohRKQekuIhOWq6m1igTepaLkl5g8Z9ymwJCspYnXDBJYHLGUbA0NJBlkg3pxnvn9kycF1_Uv4ePIzjw7DulDuZOsRwYymj8Chs7ismJWaYUSWzQSpg0Sz3DePD22kn3gV_WsNT3DX421CwE0hmcEnrQujW1290B6PiG4ywIHBcp7Dw0nCGYVd3B3RBGFoveUCtjq97A0tC1BLlDHYKnlasqrVkg7ZA4oOCsXwpZGG4hQYhBAbYZI4E7DVh_yx3IaSA1FZwnZMVg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
تصاویری از لحظه وقوع تیراندازی در شهرک اسرائیلی نِوه تسوف (Neve Tzuf) در نزدیکی شهر البیره در کرانه باختری منتشر شده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 4.07K · <a href="https://t.me/alonews/148353" target="_blank">📅 13:46 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148352">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cExOGfQhBj-mNfylYL7rOKZ2ibCqBZ08mh7n2Va3scXcFct5cv3XivlOPVBmjd1sEGTnG6oPq5phvjMgu2NK2fZ8470tPHAgy7lUO_SOZAcCbQZzis1NR-e1nUPW6IgdVQlwesmfeqK_jgjXgC15czdIyQn422vPMZ5sRAsLDPc3ZCzz4wpDw2lrYMEUjUwz4294V6cXAWlnDlhW07yzFUK1D7JcYKDhuiu5z8rCicbBETulpRmejbvQCTKRLb9EAuAZMYAdH05eWknIYTaeHUrTcmC8tDNaFEpv91UfpKiIdSv-bF3TSEjfiWuUH1lYca8BLT9GprL6xKU61awV3Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
شبکه فاکس نیوز با انتشار تصاویر ماهواره‌ای از تأسیسات هسته‌ای طالقان مدعی است فعالیت قابل‌توجهی در این محل دیده شده و یک سازه بتنی روی آن ساخته شده است
🔴
آنگونه که در تصاویر ماهواره ای مشخص شده است؛ ایران برزنتی را بر فراز تأسیسات تخریب‌شده و مستحکم‌شده‌ی مدفون نصب کرده است که فعالیت‌های بازسازی در زیر آن را از دید ماهواره‌ای یا شناسایی هوایی پنهان می‌کند.
🔴
فعالیت قابل توجهی در سراسر محل ساخت‌وساز قابل مشاهده است.
🔴
وسایل نقلیه ساختمانی، از جمله کامیون‌های کمپرسی، بولدوزرها، کامیون‌های پمپ بتن و میکسرهای بتن و جرثقیل‌ها، به طور فعال برای بازسازی این تأسیسات در حال کار هستند
✅
@AloNews</div>
<div class="tg-footer">👁️ 8.15K · <a href="https://t.me/alonews/148352" target="_blank">📅 13:41 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148351">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">👈
حاجی‌دلیگانی: طرح سه فوریتی خروج از NPT تقدیم هیات رئیسه مجلس شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/alonews/148351" target="_blank">📅 13:37 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148350">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">🔴
فوری / ایلان ماسک مجوز اتصال مستقیم گوشی به اینترنت ماهواره‌ای رو گرفت
✅
@AloNews</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/alonews/148350" target="_blank">📅 13:26 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148349">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/19a38b8192.mp4?token=Au41B8w9cDVsrQysuwJSwvwZV9qrYTe6hL7rZZIhGdx6uWTPJ60U5yRZ6kiRwOv5P-lbeRII0CVRHxwqS32OqRg6jJCrZvlHgLxTukENoFQxoqQKwqk8ApQd43O6euEIVx553bagxY-S8GqWQ3OC1_VzT8Q_RObA6KUVlcky8vRx1sv2XiG2F6UFNDf5WNhAQ7JZvhzSqAPh6rSEJVbIDGh_bubRIugNiR7yS0XmGcJx6MACxKnvnDfzyc9M_1VlL8ZBsCtg-86E3-D9jEHpkIq_3BI15kCiUEF4yENNvQ91OC2uYQTCWuOS1sobMjGfGa2Sgk8Pb0NPMeJKDNzPKg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/19a38b8192.mp4?token=Au41B8w9cDVsrQysuwJSwvwZV9qrYTe6hL7rZZIhGdx6uWTPJ60U5yRZ6kiRwOv5P-lbeRII0CVRHxwqS32OqRg6jJCrZvlHgLxTukENoFQxoqQKwqk8ApQd43O6euEIVx553bagxY-S8GqWQ3OC1_VzT8Q_RObA6KUVlcky8vRx1sv2XiG2F6UFNDf5WNhAQ7JZvhzSqAPh6rSEJVbIDGh_bubRIugNiR7yS0XmGcJx6MACxKnvnDfzyc9M_1VlL8ZBsCtg-86E3-D9jEHpkIq_3BI15kCiUEF4yENNvQ91OC2uYQTCWuOS1sobMjGfGa2Sgk8Pb0NPMeJKDNzPKg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
توی برلین آلمان، یک دختر تریان(آدمایی که فکر میکنن حیوونن) به یک خانم تو خیابون حمله میکنه و گازش می‌گیره، زنگ زدن پلیس، هر چقدر از دختره اسم و فامیل پرسیدن فقط پارس کرد، پلیسا هم بردنش به ی مرکز نگهداری از حیوانات
✅
@AloNews</div>
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/alonews/148349" target="_blank">📅 13:12 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148348">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">👈
گاردین به نقل از وزیران بریتانیایی گزارش می‌دهد:بودجه ماه آینده در بریتانیا به دلیل جنگ ایران ، دشوارتر شده است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/alonews/148348" target="_blank">📅 13:10 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148347">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">👈
فارن پالیسی: روسیه مایل است ایران در شرایط جنگی‌ بماند
✅
@AloNews</div>
<div class="tg-footer">👁️ 32.6K · <a href="https://t.me/alonews/148347" target="_blank">📅 12:55 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148346">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">👈
قالیباف: جنگ بعدی ناوهای آمریکایی را در هر نقطه اقیانوس هند باشند هدف قرار می‌دهیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 37K · <a href="https://t.me/alonews/148346" target="_blank">📅 12:45 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148345">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">👈
زیدآبادی در کانال تلگرام خود نوشت:
احتمال ورود نیروهای زمینی برخی کشورهای منطقه به خاک یمن به قصد تصرف پایگاه‌های حوثی‌ها هم دور از انتظار نیست.
✅
@AloNews</div>
<div class="tg-footer">👁️ 37.8K · <a href="https://t.me/alonews/148345" target="_blank">📅 12:42 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148344">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">👈
شرکت برق البرز: در یک مزرعهٔ استخراج رمزارز که در پوشش صنعت فعالیت می‌کرد، ۳۶۲ ماینر کشف شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 38.8K · <a href="https://t.me/alonews/148344" target="_blank">📅 12:36 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148343">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">👈
واشنگتن‌تایمز نوشت: ترامپ قرار است چهارشنبه، شخصا در فرودگاه پایگاه مشترک اندروز از شی جین‌پینگ، رئیس‌جمهور چین، استقبال کند.
🔴
این کار غیرمعمول است، چون ترامپ معمولاً از رهبران خارجی در کاخ سفید استقبال می‌کند نه فرودگاه.
✅
@AloNews</div>
<div class="tg-footer">👁️ 39.8K · <a href="https://t.me/alonews/148343" target="_blank">📅 12:29 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148342">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">👈
با تصویب مجلس، وزارت کشور مکلف به راه‌اندازی «سامانه نظارت بر ارتباطات خارجی» شد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 40.8K · <a href="https://t.me/alonews/148342" target="_blank">📅 12:25 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148341">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">👈
پیمان اکبری، مجری انقلابی: کلیپی که از من بیرون اومده و کنار دوتا دختر خوابیدم هوش مصنوعی هست و میخوان خرابم کنن
✅
@AloNews</div>
<div class="tg-footer">👁️ 40.8K · <a href="https://t.me/alonews/148341" target="_blank">📅 12:19 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148340">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/v291EQp8hiDgQsqLCEXRyAXzGkcPKXToJyUMd7MKetFyw-6hj8trJk-cP24lBCmnYeohTp31dUxmye2BV0Q5oCbDllhWBTLNPYBjviS-KHANZyvOlRjboC8suzUyG39ki-NOpFHVzvXKsdrsWgWY1UjzrLbbhNLX1y2pWaVJ-ctZRBgUUp0PWRERz2mSMVsQJBoCFaPOySpmzKVYPO6Sm3atvTeGzETSv_LMGZMplGeeHuOaOlfOozlf9uMs_G69kX01tvVvlqdO7EEhWA6h1jmwoy4ukdkXOyWxe3h0C3blDwrGzmz3uQMdQegcWNe6jsgvxgBtMjRuyIR4qtUkeg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
پیمان اکبری، مجری انقلابی: کلیپی که از من بیرون اومده و کنار دوتا دختر خوابیدم هوش مصنوعی هست و میخوان خرابم کنن
✅
@AloNews</div>
<div class="tg-footer">👁️ 41.8K · <a href="https://t.me/alonews/148340" target="_blank">📅 12:16 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148339">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">👈
روزنامه کوریره دلا سرا: ایتالیا آماده اعزام ۴ کشتی جنگی به تنگه باب المندب است
✅
@AloNews</div>
<div class="tg-footer">👁️ 39.8K · <a href="https://t.me/alonews/148339" target="_blank">📅 12:14 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148338">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/14c84f4e05.mp4?token=d-dTBoQgR6I2w__mnTogNNyCEkuxDXz7snQS6NOwBGqyv-HBkV0mCKmU8JUyqVdMbFyqFl2AZ0onzaQeFxe30wvUuDHPDO7GjuoYqP-dZOsZjvHyH55fLN6W0ZJpUXk0UI1-OVStjQDuxt9t1Xn2QxRPQy3GfCQ0caOiZ_0nYXeJuFgUvEB6mYjcnV9mETqmA9UWm0vX78krVsTHk9fyXgJh3yLaKZ7n6e0ERPMe9St31X4KboRlpVvLBatSXdngn_WZ8MPo-wb0rfZcl_HyAiaHhNpUm6Hno8kva_85nKEt_c_MwRoYF0VkLZfm0QHglnZbC6p3TiNAoCnRco_Naw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/14c84f4e05.mp4?token=d-dTBoQgR6I2w__mnTogNNyCEkuxDXz7snQS6NOwBGqyv-HBkV0mCKmU8JUyqVdMbFyqFl2AZ0onzaQeFxe30wvUuDHPDO7GjuoYqP-dZOsZjvHyH55fLN6W0ZJpUXk0UI1-OVStjQDuxt9t1Xn2QxRPQy3GfCQ0caOiZ_0nYXeJuFgUvEB6mYjcnV9mETqmA9UWm0vX78krVsTHk9fyXgJh3yLaKZ7n6e0ERPMe9St31X4KboRlpVvLBatSXdngn_WZ8MPo-wb0rfZcl_HyAiaHhNpUm6Hno8kva_85nKEt_c_MwRoYF0VkLZfm0QHglnZbC6p3TiNAoCnRco_Naw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
قالیباف: نظم کهنه‌ آمریکایی در غرب آسیا فروریخته است؛ مسیر آینده نه با التماس، بلکه با عقلانیت، شجاعت و مبارزه رقم خواهد خورد
✅
@AloNews</div>
<div class="tg-footer">👁️ 42.4K · <a href="https://t.me/alonews/148338" target="_blank">📅 12:07 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148337">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">👈
دراپ سایت : بازگشت زودتر از موعد ترامپ از کمپ دیوید، ویدیوهایی از برخاستن بمب‌افکن‌های B-1 از بریتانیا و هشدار امنیتی آمریکا به شهروندان این کشور در خاورمیانه، نگرانی‌ها درباره احتمال آغاز دور جدیدی از تشدید تنش علیه ایران را افزایش داده
✅
@AloNews</div>
<div class="tg-footer">👁️ 41.8K · <a href="https://t.me/alonews/148337" target="_blank">📅 12:03 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148336">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mbmMebhKS0tHj_BE7kBAMFV7EPOyc7UWSFnrkqe7r_Bg957TkXFxm7jljVldDNyAJbtRG_DPrkR0CMzdw2vyP2AibsAQxj3ys9LKw6-DZwYoaeamHMZxFPsVbg8iFr5UzALRD0KxuYy9vIoqRTD1c0pyH5oVtu_3l2xrrj4Av9c9euRbkcF1UoxsKcsUDjGR8TVCcYanSY2R8kNQxzFR6lSQ4cYZcfSAs7s4KrU6RmJgcsrWOkPw9tmqreJYwNWAcAkqV3MgifqPGfymNu1zsMsEfe7HJWZiXIwqIgczi9inTOTd-NUJYN2s2ZqXX-yDuzOt-ZJxOcO4u5XxXRo4SQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
هیمتی: ارزونی تو راهه
✅
@AloNews</div>
<div class="tg-footer">👁️ 43.9K · <a href="https://t.me/alonews/148336" target="_blank">📅 11:54 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148335">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UhcbmknLCu97SNdYaa7P9_bbboaZlbMVmEbL9jo3yLdmWk63am5cC6wB_EWvsT9xR1wHh4KU1yjwJS_-1dBYCMszUer4ULxWiZT7WfIPqhZ2mzOol_RmzhP5Wby0QD2uGXeq5VvzWWAt4nJUb0rtEXVmyeI-lj4ej1ORguMLSFeIV437DNwygQdUnBLgvFfvdZagg_ulAxqbH_Rdwdc2UvSDBqq44bXK5PXgb_HKyt-AXdNnqu2qL_7hqx_12iryZtMQ1nb2Xw__e87UxYqZ5c_utgqM8a2nCiVgVhOnES6Tw_tKIveTptOZ4-EQAefWoX1BNIqNc0Yp3GffT_aF2Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
در حالی که تمام نگاه ها به قیمت نفت دوخته شده کمتر کسی متوجه است که این روزها حمل نفت در یک سوپرتانکر حامل ٢ میلیون بشکه به مقصد چین بشکه ای حدودا ٢۴ دلار یعنی بیش از ٢٠ درصد خود نفت هزینه دارد. رکورد بی سابقه ای است
✅
@AloNews</div>
<div class="tg-footer">👁️ 43.9K · <a href="https://t.me/alonews/148335" target="_blank">📅 11:50 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148334">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">👈
مدیرعامل مترو تهران: ساعت فعالیت مترو از اول مهر بدون تغییر، از ۵:۳۰ صبح آغاز می‌شود
✅
@AloNews</div>
<div class="tg-footer">👁️ 43.9K · <a href="https://t.me/alonews/148334" target="_blank">📅 11:47 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148333">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">👈
ارتش اسرائیل عملیات تخریب را در مناطق مجدل زون و طیر حرفا در جنوب لبنان انجام داد
✅
@AloNews</div>
<div class="tg-footer">👁️ 44.9K · <a href="https://t.me/alonews/148333" target="_blank">📅 11:43 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148332">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">🔴
تا ماه بعد وضعیت طلا چجوریه؟</div>
<div class="tg-footer">👁️ 44.9K · <a href="https://t.me/alonews/148332" target="_blank">📅 11:41 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148331">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ANHwb3QrFwwpfadeW4KzTaSRgvuSEtamSX02KBsJrP4toHrkVPiMPpuMHNNLp6W-jilMKk5gySHQovBh0TBv-LEq1ClY0xRwly-QPuD-HTmbqgC_3CllUncBeQLb0MTmdj_Y6ynoYMW7LPElt6gDP21qW52i-1StFw2nHOqmQwID6xf8KkHHHWjzmUGDDgcmnwnSkSyyYedhoGJ3moq92tqr365UgP4QajZQGlj6zb9l0Xy_ERipDFfCatt3cTmvi639qenA2bKfD3q5yOkTj4A0tfbHnqjESRwnaLOqRk3MOWb_O2UzU__SyOYVbmsUYgR9Pmk8t5PoIx1F1_IFaw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
هشدار بزرگ امنیتی آمریکا در خاورمیانه
🔴
سفارتخانه‌های آمریکا در سراسر خاورمیانه امروز به‌طور هماهنگ هشدارهای امنیتی صادر کردند.
🔴
رویداد: با توجه به تنش‌های موجود در خاورمیانه، وضعیت امنیتی همچنان پیچیده است و احتمال تشدید غیرمنتظره تنش‌ها وجود دارد.
🔴
به شهروندان آمریکایی که در حال حاضر در خاورمیانه حضور دارند توصیه شده است سطح هوشیاری خود را افزایش دهند و نسبت به احتمال لغو پروازها، بسته شدن حریم‌های هوایی و اختلال در سفرها آگاه باشند.
🔴
ایران: سفر نکنید؛ همین حالا کشور را ترک کنید
🔴
عراق: سفر نکنید
🔴
لبنان: سفر نکنید
🔴
سوریه: سفر نکنید
🔴
یمن: سفر نکنید
🔴
غزه: سفر نکنید
🔴
عربستان سعودی: در سفر تجدیدنظر کنید
🔴
بحرین: هشدار امنیتی صادر شد
🔴
عمان: هشدار امنیتی صادر شد
🔴
قطر: هشدار امنیتی صادر شد
🔴
کویت: هشدار امنیتی صادر شد
🔴
اردن: هشدار امنیتی صادر شد
﻿
✅
@AloNews</div>
<div class="tg-footer">👁️ 47.9K · <a href="https://t.me/alonews/148331" target="_blank">📅 11:33 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148330">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">👈
روزنامه عبری تایمز اسرائیل : عربستان سعودی برای مقابله و دفع حملات یمنی‌ها و به دلیل کمبود موشک‌های رهگیر، خواستار حمایت بین‌المللی شد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 45.9K · <a href="https://t.me/alonews/148330" target="_blank">📅 11:24 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148329">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZnZbLr1UPur_zeSoaGZXRAAMrke3-Z-ZtWm93kpBLkENvJmKUUCckllTxp_iWToAZa8iVkp7U9-POdNjbxOzKZ91JRJGAnETgo4960U2zsYMk0ghKeNEqvtMih33FLmC0jVGcjC7Y75qiduxWbUgz64eNIpNUo9hrQNEjcpDyqUs5zBqqv0acfSF84H0WNHTdeZZ8H7sYVFFE9NcctMKiAC9yrE38OqH6KwSnTilj6Rc3_nE6XY3W-x61PZ1RZd08hc3AYR7rYEXsl3hlGkoRgvwju5059d5EWD7Fe0SjtFEgT0c8pWfe1L7FWv6z29cTU-Lx-3Q77VfxehALtXJuw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
نماینده جمهوری‌خواه آمریکا: یمن را از ایران آزاد کنید
✅
@AloNews</div>
<div class="tg-footer">👁️ 47K · <a href="https://t.me/alonews/148329" target="_blank">📅 11:19 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148328">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">🔴
فوری / کره شمالی یک موشک بالستیک شلیک کرده است.
🔴
این موشک به احتمال زیاد به سمت دریای ژاپن در حال حرکت است
✅
@AloNews</div>
<div class="tg-footer">👁️ 51K · <a href="https://t.me/alonews/148328" target="_blank">📅 11:08 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148327">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/UpYNeK_EV_rbf7a-fjc__wEWpQYZG8d8LL9C8F5wxmuVOtraPByZEz5ZKyDxGwglYdTS5qkwCHb8iHAHdoZswdOA0TLhXbOcIFXGrPjIpKaDiNKhUM1ZEeG71bnkvvsjQh8m-8-kgHEdF3AeI09MZiYcOnTeDPp5yFYRJwcWHTJOqHf3a0zgYzaANI1VTVmkJcH7zcoVuJESySnOxaM-pa7K35kq7J1C42x4ANJ-M4t_ujihIg95JNx2462evu37jaxiC7j7t0dgiQ0RAk_Sgf_MrgPf7o_e124-3JmtOIIi2GDSjjoNDYJR-_wgmJF1hW5GsfJndN0msXCbtpZjIg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
فایننشال تایمز: عربستان سعودی از پلتفرم mBridge برای ارز دیجیتال فرامرزی که بخشی از تلاش‌های چین برای ایجاد جایگزینی برای سامانه‌های پرداخت تحت سلطه دلار است، خارج شده است.
🔴
بانک مرکزی عربستان اعلام کرده که این کشور در مه ۲۰۲۵ مرحله آزمایشی (Proof of Concept) خود را تکمیل کرده و خروج از این پلتفرم نیز بخشی از برنامه اولیه آن بوده است.
🔴
این اقدام پس از خروج مشابه بانک تسویه‌حساب‌های بین‌المللی (BIS) در سال ۲۰۲۴ صورت می‌گیرد؛ اقدامی که در بحبوحه گزارش‌ها درباره فشار آمریکا انجام شد. همچنین دونالد ترامپ، رئیس‌جمهور آمریکا، کشورهای عضو بریکس را در صورت تلاش برای ایجاد جایگزین‌هایی برای دلار، به اعمال تعرفه ۱۰۰ درصدی تهدید کرده است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 50K · <a href="https://t.me/alonews/148327" target="_blank">📅 11:08 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148326">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/af2be236d1.mp4?token=WxulCYRdIaNmYsAU1aJj5FWHFy_44ifZU1R9eoalgQGeYm90AdfVrCQ35_fbNwpfaLdXHehtHIDrpuibjKTh9lVe7j5gFTabLEcO-rVXgHhakxhhwVpvP3suDvL8J5F52IIMkurzoFSSvqSQN74J6nOHwaU35hoNs1mmRhNmnxvG3c0YAgyuto12xSJIDlFi-WGXgFwVCnOvS8ud5z-Elq2lx9G_DfT4fZKPzD8_mI_zl-XWc5gMG9BOe8CuBjj45J5KsgVbAqEwR_YA_QDgVTDAQVahfrmrGcOsYQavT3aqWvGQuik-cUbnO1txrYj_BkU-KVleZ_KhtMzeekXTxQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/af2be236d1.mp4?token=WxulCYRdIaNmYsAU1aJj5FWHFy_44ifZU1R9eoalgQGeYm90AdfVrCQ35_fbNwpfaLdXHehtHIDrpuibjKTh9lVe7j5gFTabLEcO-rVXgHhakxhhwVpvP3suDvL8J5F52IIMkurzoFSSvqSQN74J6nOHwaU35hoNs1mmRhNmnxvG3c0YAgyuto12xSJIDlFi-WGXgFwVCnOvS8ud5z-Elq2lx9G_DfT4fZKPzD8_mI_zl-XWc5gMG9BOe8CuBjj45J5KsgVbAqEwR_YA_QDgVTDAQVahfrmrGcOsYQavT3aqWvGQuik-cUbnO1txrYj_BkU-KVleZ_KhtMzeekXTxQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
یک بمب‌افکن B-1B Lancer آمریکا شامگاه امشب در حالی که با پس‌سوز کامل از پایگاه هوایی RAF Fairford در بریتانیا برخاست، فیلم‌برداری شده است.
🔴
گفته می‌شود این بمب‌افکن احتمالاً عازم خاورمیانه است
✅
@AloNews</div>
<div class="tg-footer">👁️ 49K · <a href="https://t.me/alonews/148326" target="_blank">📅 10:59 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148325">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">👈
پزشکیان: قابل قبول نیست که ما مسئول باشیم و فردی با مشکل معیشتی مواجه باشد
✅
@AloNews</div>
<div class="tg-footer">👁️ 46.9K · <a href="https://t.me/alonews/148325" target="_blank">📅 10:56 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148324">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/083f6484a3.mp4?token=csNAjm3ClSFzSmMJiHEiXJEM1wpL7dYQvQX6ER8jAd9NjC4Ve3t24OP6GcEQsum0nsBUdGZPlA4WWVLaJSqomXMDTuDQHglwBqQhci9fF7URnFNoGbmF4G4l_6UAAZNMp36wH_WOC-tFwRP_omuVM8dd-A61VbJQzpWTIP-cs96gF6xcngJ37Kh-vZ77Ds8bHM-sJD_gG6wWgjCoc3_XR21Z068sf1p_SDdPcL1vZ9Cf256JhWMGw0pziAv86MxSBvzEflBEIG9SMS9TpuI_K08FRUNz-9UYYXL8-pveLVlZ-L8eMJsn77JGWteSfweIXXlIjdoNxoCUjSnjHFXfig" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/083f6484a3.mp4?token=csNAjm3ClSFzSmMJiHEiXJEM1wpL7dYQvQX6ER8jAd9NjC4Ve3t24OP6GcEQsum0nsBUdGZPlA4WWVLaJSqomXMDTuDQHglwBqQhci9fF7URnFNoGbmF4G4l_6UAAZNMp36wH_WOC-tFwRP_omuVM8dd-A61VbJQzpWTIP-cs96gF6xcngJ37Kh-vZ77Ds8bHM-sJD_gG6wWgjCoc3_XR21Z068sf1p_SDdPcL1vZ9Cf256JhWMGw0pziAv86MxSBvzEflBEIG9SMS9TpuI_K08FRUNz-9UYYXL8-pveLVlZ-L8eMJsn77JGWteSfweIXXlIjdoNxoCUjSnjHFXfig" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
تصاویر نزدیک از حمله پهپادی اوکراین در منطقه کاپوتنیا در مسکو منتشر شده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 47.9K · <a href="https://t.me/alonews/148324" target="_blank">📅 10:52 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148323">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">👈
رئیس مرکز مدیریت بیماری‌های واگیر: کرونا بومی شده و مانند سویه‌های اولیه مرگ‌ومیر ندارد؛ اما برای سالمندان و بیماران مزمن همچنان می‌تواند خطرناک باشد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 46.9K · <a href="https://t.me/alonews/148323" target="_blank">📅 10:47 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148322">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a7442de3f9.mp4?token=QBR_J_e-HIRysr4lNcWMo-Zn_eCAP14su8Qzx61FIicy_cMgOhnDDRM_-VJmvGs0zTkP31cOZ9rRFOoRN_M4u1EZ1dHHqo3a7dhe12WCO78nvBHFJYTgVYj7bpPDsfkbtfzlF-I_zEGnKGtDZZkJ9wGduzDl6nCURDA0Cp_Hl5W547rla-ak0BnVpDZBqCNvhaMlR_ge9uwb-rqCWUG8zevjDT3xITI8gJv2wHx1GKzuTCZrTsgXNmHjOTv1UgxfO9ESyostacEngcCZgbezGmksYOCYlk_7N4rQLiVKVizjI9cFj_u7tYXBoEPHGsA7LnOwZtgXxr-JBmjiES2qNSsC3gazcZVfarhZOIwtbr1B3ptP0rjYqfRUKsbLoPwEK4RX5IHdZy3fbYT2j3SxfbxOYY3rCj7VJpEjXO3mSL06McEP3JnXp0eJq1Z47kdgJvp4ibVfJE8szMHYJmeSysDNFA-2JlV8p0BG0pRxHMjHjB9aj8oiXNhZdXFXxmNVZoGQxSIT0ElGMyYi7Cqka94udmDizqQaK1489WEtb2C_q4R68ZkW9WfRFoIb7EJnZEgYAIAsyvvi8AcnpUAF2zlbJYWfB9d4gPEiNf3t4chuzJwVA2HoqcxmcEkipmpx9IbGr2vpffXoD-ZT-LJz6ZmkfMJwXGePgEOOePGcarI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a7442de3f9.mp4?token=QBR_J_e-HIRysr4lNcWMo-Zn_eCAP14su8Qzx61FIicy_cMgOhnDDRM_-VJmvGs0zTkP31cOZ9rRFOoRN_M4u1EZ1dHHqo3a7dhe12WCO78nvBHFJYTgVYj7bpPDsfkbtfzlF-I_zEGnKGtDZZkJ9wGduzDl6nCURDA0Cp_Hl5W547rla-ak0BnVpDZBqCNvhaMlR_ge9uwb-rqCWUG8zevjDT3xITI8gJv2wHx1GKzuTCZrTsgXNmHjOTv1UgxfO9ESyostacEngcCZgbezGmksYOCYlk_7N4rQLiVKVizjI9cFj_u7tYXBoEPHGsA7LnOwZtgXxr-JBmjiES2qNSsC3gazcZVfarhZOIwtbr1B3ptP0rjYqfRUKsbLoPwEK4RX5IHdZy3fbYT2j3SxfbxOYY3rCj7VJpEjXO3mSL06McEP3JnXp0eJq1Z47kdgJvp4ibVfJE8szMHYJmeSysDNFA-2JlV8p0BG0pRxHMjHjB9aj8oiXNhZdXFXxmNVZoGQxSIT0ElGMyYi7Cqka94udmDizqQaK1489WEtb2C_q4R68ZkW9WfRFoIb7EJnZEgYAIAsyvvi8AcnpUAF2zlbJYWfB9d4gPEiNf3t4chuzJwVA2HoqcxmcEkipmpx9IbGr2vpffXoD-ZT-LJz6ZmkfMJwXGePgEOOePGcarI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
پیت هگست، وزیر جنگ آمریکا، درباره گزارش واشنگتن‌پست مبنی بر اینکه شمار بیشتری از نیروهای آمریکایی در خاورمیانه نسبت به آمار اعلام‌شده عمومی پنتاگون کشته شده‌اند، گفت: «این یک دروغ است.
🔴
این فقط یک تیتر است که آنها می‌خواهند با آن ما و رئیس‌جمهور ترامپ را بد جلوه دهند و تلاش کنند موفقیت تاریخی ما در این درگیری را زیر سؤال ببرند. این واقعاً مسخره است.
🔴
شاید مردم باید فقط دیگر حرف‌های واشنگتن‌پست را باور نکنند. فکر می‌کنم شروع خوبی باشد.»
✅
@AloNews</div>
<div class="tg-footer">👁️ 51.3K · <a href="https://t.me/alonews/148322" target="_blank">📅 10:39 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148319">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ce9J_xARZYckUdJiemVG9rjKnnP5pgTy13S_3og2go1brrF5foeJr119oDQo03jpe8qRg8ym6b8ELEWJVtuRUw5EwiiGkP8LWwk1ua_ZgX2aDfwbrgRjazeqzPXkZ32ybhtoFHXuiMhbNnFJgNxS4Z0mEaq2xCTVSYifljZYVMW3uCwD4oKxb6vbIwp5KlccvUQFQ1PYLbTL4Zj3EpbXujkzC_kAewkVC4-dRNNC2nR7NlksOROqkI7NetnAoGWa3p-7L-4LJ3H_AOvjeMLRvh04OfPMi8j_l5c47aI7y5g9241813yVHEf-BMFxidhxKQNgp5qGDSE1jQ8JDpq_Cw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/gRj-zuqSb7pcZvRIqtiz5k9nJE2kzbNcwdYqL8O9eb9-I2XB0rxKlM6Uv_UvPEc8U11X3TQPfklApSmnXC1QP2kkGDqeUtviAS53l0YI5EAWOaitbtW0EWoKSmTbM1wTBl1dEFVrAYjXXrAQkiw6eEuHp5ZTAUXlf1uWtyqkECgVNUh_e9GXnL2_D2ZBsZFWbSAHx9D4kAo1dp12JBo72TS74v4b3ct6dkWA7zCvpcAkFue7a7n5VcCaVOgnW9nX-TyAH18rooV2hXfqZUIYdDqS9d_ezO52AGtzgiUvjy3Vi2hsYeMckUcnGnx2Pb4zVQ2KCJ1mare-c5J9Dt_Hyg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ByMWyWodwMSqIcQY5HK-7c2qkWH6gyGG5kjQKJukTauheaI8asIyvoVcARhBX-1CqCKoiXUDrjYUuO4QcssNCC8Cx5HtX4crdK4-3dZ5G2V9PpsOsi3ZGpiyRSFq34v185VH2okRrORS6cKUeVWMpP8F-Bw5m056IprnAn9iXn1uLbWP9MmbktX0zE4eO26dTYz0p9KpR435xfNNhBqiheEYWVlC3rO1YAdEFsBjPcaBqSsqJNZ2ExfOODC1ufGie_zAOnll851kxsS3PG0PDmUX6kA31TadlvFgr-tfPWDoWfQ6h56SRtwkhk8Wqb4f_-e0YeXT2zSg8hXnVIu-aw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
تصاویر دیگر از پالایشگاه کاپوتنیا در مسکو، روسیه پس از حمله پهپادی اوکراین
✅
@AloNews</div>
<div class="tg-footer">👁️ 47.9K · <a href="https://t.me/alonews/148319" target="_blank">📅 10:33 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148318">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LEZJoms8EdYig2tEJSY14aEjR2Up-SlvUg6YYYcjHOuPHVtOLVdOQRhMwoo1tOfOQsbUHbmom4xyY2aghuukiQqiwMj_4ntBZNrAOmBxAQGMve3_7uT1cuWKUcAZzq0NoFVLaeXus8rKNDa9sN5-QzEgM6oI0MYD-r5u2vCxWrsDtLGqktIZATVK77ds7PKF17UPcO0A8WSjYk8AMHYMr5t2Ezu92QrocX8TW-auNAbX7Vw7stAoc6frCyurZM1YPkc6L-r7s-xK5uGE1WeCSxMyq0ceKvbR7Q1bdTojPD2_0sPnjYXZjohwlpxa85_ibxRfb--jcSRxi8PZZCWCfg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
👈
تصویری عجیب از پالایشگاه مسکو در آتش
✅
@AloNews</div>
<div class="tg-footer">👁️ 52K · <a href="https://t.me/alonews/148318" target="_blank">📅 10:19 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148317">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">👈
قالیباف: نگاهی وجود دارد که از جنگ سخن می‌گوید، اما هیچ سازوکاری برای پایان مقتدرانه آن ندارد؛ این نگاه با نفی دیپلماسی، عملاً کشور را به سمت فرسایش و درگیری بی‌پایان می‌برد
🔴
انتقال پیام‌ها و تبیین شروط ما از طریق میانجی‌ها با صراحت به طرف مقابل انجام شده
🔴
معتقدیم دوگانه‌ جنگ یا مذاکره واقعی نیست، بلکه هم باید جنگید و هم مذاکره کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 51.2K · <a href="https://t.me/alonews/148317" target="_blank">📅 10:14 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148316">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/146935a692.mp4?token=GnRGcoaB-eU7GwWExzXCYMOSbDUSswc4TpVMAUAAfVxLkRH2x6jwsmC5z4SyrSVobStJmOCT6S1nawnmfLxY7N3jaOaMyGhC99Bi74FGHy-IKVA93U0N_GlRSVdam6iaoUgFUAgOp5jafcFhlcvH1GP-Zt4-vcVTw3zDTSJqGMm2Az3JTijDBEuHLkbkQ3gUwCnS7L7Wl1SWBNI3bAcxG1H0SxJQieOolL9kAvbj7qIYje9WBCHuBPmY45LKaQF-YVcRW2xcZvIuo8sC2HDrpL2Bcj5Vu2VDXo0zH69fGBfYOfeSgXmmPYYF-OikoRfvwW88xGk8idQLO7gv8rEbtg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/146935a692.mp4?token=GnRGcoaB-eU7GwWExzXCYMOSbDUSswc4TpVMAUAAfVxLkRH2x6jwsmC5z4SyrSVobStJmOCT6S1nawnmfLxY7N3jaOaMyGhC99Bi74FGHy-IKVA93U0N_GlRSVdam6iaoUgFUAgOp5jafcFhlcvH1GP-Zt4-vcVTw3zDTSJqGMm2Az3JTijDBEuHLkbkQ3gUwCnS7L7Wl1SWBNI3bAcxG1H0SxJQieOolL9kAvbj7qIYje9WBCHuBPmY45LKaQF-YVcRW2xcZvIuo8sC2HDrpL2Bcj5Vu2VDXo0zH69fGBfYOfeSgXmmPYYF-OikoRfvwW88xGk8idQLO7gv8rEbtg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
اوکراین یکی از بزرگ‌ترین موج‌های پهپادی خود را به سمت مسکو پرتاب کرد
‏
🔴
روسیه ادعا می‌کند بیش از ۱۶۰۰ پهپاد سرنگون شده است، از جمله ۴۵۰ فروند که به سمت مسکو هدف‌گیری شده بودند.
‏
🔴
حملات به پالایشگاه نفت کاپوتنیا (بزرگ‌ترین پالایشگاه مسکو) و ساختمان‌های مسکونی اصابت کرد، که منجر به کشته شدن دو نفر در منطقه مسکو و تخلیه ۴۰۰ نفر شد.
‏
🔴
محدودیت‌های پروازی در فرودگاه‌های مسکو اعمال شد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 54K · <a href="https://t.me/alonews/148316" target="_blank">📅 10:08 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148315">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">👈
وزیر خارجه ترکیه: شرایط جدیدی برای مصالحه بین ایران و آمریکا پیشنهاد شده؛ امیدوارم آن‌ها این شرایط را بپذیرند
✅
@AloNews</div>
<div class="tg-footer">👁️ 52K · <a href="https://t.me/alonews/148315" target="_blank">📅 10:03 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148314">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">👈
توقف پروازها در فرودگاه‌های مسکو در پی حملات پهپادی اوکراین
🔴
آژانس فدرال حمل‌ونقل هوایی روسیه:
در پی حملات از سوی اوکراین و شرایط امنیتی، پروازها در دو فرودگاه مسکو متوقف شده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 53K · <a href="https://t.me/alonews/148314" target="_blank">📅 09:59 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148313">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/057ccc8854.mp4?token=R6PW2nxs3lsLsr-gjsYVZRY4kJzCgqvU1zSJdyVsul9np-CAcgkBDRXor-A6bry27-H5Nypr0K6AIWx-fiUAy4f38-6zAorqzVACDjQ1J5AQfC658pjXTFJLu8uH-n7o7wuUChts4QloKmVSGjlqc136-pJCYhWPwEOZcVgnE6rOEx3I3QpZp8KqOAD6xf_8h0WW-9z9-CiIjVlwQUjZ6NinhsC5S4BZv7kggs5U-_q03hpOC9v5GJzPBDwy9cB0yYStdstA1saxvd3xpFBYw6a47bKAMmIC01H_gK0pp94KOBzGalwVbzBU9xQWwNBMYTBUUQF7ui-ZgGLl5tR7mg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/057ccc8854.mp4?token=R6PW2nxs3lsLsr-gjsYVZRY4kJzCgqvU1zSJdyVsul9np-CAcgkBDRXor-A6bry27-H5Nypr0K6AIWx-fiUAy4f38-6zAorqzVACDjQ1J5AQfC658pjXTFJLu8uH-n7o7wuUChts4QloKmVSGjlqc136-pJCYhWPwEOZcVgnE6rOEx3I3QpZp8KqOAD6xf_8h0WW-9z9-CiIjVlwQUjZ6NinhsC5S4BZv7kggs5U-_q03hpOC9v5GJzPBDwy9cB0yYStdstA1saxvd3xpFBYw6a47bKAMmIC01H_gK0pp94KOBzGalwVbzBU9xQWwNBMYTBUUQF7ui-ZgGLl5tR7mg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ژنرال حوثی الزبیدی ادعا کرد که امارات متحده عربی از حوثی‌ها خواسته تا پروژه نئوم عربستان سعودی را بمباران کنند و در عوض قول داده است که رسما حوثی‌ها را به رسمیت بشناسد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 56.1K · <a href="https://t.me/alonews/148313" target="_blank">📅 09:43 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148312">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ph898ik0sBuh2VDwpD1JiHLpNZQ08L_YpCwSIIz4pFcUTpz2QpYppOcFt36Cm4LLHVaW5kjvOWY5yPW5wDlcxFW3GV7_XhrUvlwtnXLs84qd7iUigHpuP5uSTe0paL1NtgXpVxISuQiI0z8mEB70KUgddlKz8GEPiHWneu0xUojfaXt2-ESXVQKJLQy_ipqgk5FR44RvOcUEw-yrg8u5YbgG6zmKJf-4fneJpLabBjxtSk2RvUpW5n2TNB4u4dN3yP8uITo6_4EI8MlSmVH6-2-evqRVrc3P_DZWZAbcCaAoLBBuiQanGZ2e-fw_zl427IplLuGcH3rpggWukkfhdA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
هواپیماهای نظامی آمریکایی از مدل‌های C-17 و C-5، به همراه هواپیماهای تانکر سوخت‌رسان KC-135، در حال حرکت به سمت خاورمیانه مشاهده شدند. در روزهای گذشته، تعدادی از این هواپیماهای تانکر در تل‌آویو نیز دیده شدند
✅
@AloNews</div>
<div class="tg-footer">👁️ 56.3K · <a href="https://t.me/alonews/148312" target="_blank">📅 09:37 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148311">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">👈
وزارت خارجه آمریکا: صدور هشدار سفر برای سراسر غرب آسیا به علت احتمال تشدید درگیری‌ها میان انصارالله و عربستان
🔴
در بیانیه وزارت خارجه آمریکا درباره احتمال تشدید درگیری نظامی میان انصارالله و عربستان سعودی هشدار داده شده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 56.2K · <a href="https://t.me/alonews/148311" target="_blank">📅 09:21 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148310">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">👈
ویدیوی وایرال شده از ارزش پول ایران
✅
@AloNews</div>
<div class="tg-footer">👁️ 58.2K · <a href="https://t.me/alonews/148310" target="_blank">📅 09:13 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148309">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">👈
4 کشته در حمله آمریکا به یک قایق در دریای کارائیب
🔴
فرماندهی جنوبی نیروهای آمریکا اعلام کرد که ارتش این کشور یک قایق را به زعم حمل قاچاقچیان مواد مخدر در دریای کارائیب هدف قرار داد.
🔴
حمله آمریکا علیه این قایق در دریای کارائیب دست‌کم ۴ کشته بر جای گذاشت
✅
@AloNews</div>
<div class="tg-footer">👁️ 55.1K · <a href="https://t.me/alonews/148309" target="_blank">📅 09:09 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148308">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/M-3P6HLcBXskCB0SJSLLn9GG10TtDjQy2KMDBXmx3cUouZjB-Rk93Wk7Pe3r62ByVNCDqGUD6mmv57wjHnUqDGPuY5I-63XNe5QRPjF3X2TaAJ1c5GXL-935byns4k9BI2nVn_UdamAryKu8OP8R_GOfZmYv0EHRmvvoe5bg5Y0O0Io6Bu0aji_WcEGyZH0o_72oZHI80nPyUHNrwlCOeCm4ZI3MYlmaeIu9aI7SluUclXPCpwFfVrTIN5nl38by32wcaB_uCTKtYF6HgMHbBCUO1AnhU0F7cwnhGq9SOot_4h5Y4WWruIepKdt0uWIGasfPL1zgzh0YVuFaRzawSw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
6 فروند هواپیمای تانکر سوخت در حال پرواز در خاورمیانه هستند
✅
@AloNews</div>
<div class="tg-footer">👁️ 56.1K · <a href="https://t.me/alonews/148308" target="_blank">📅 09:06 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148307">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bSnnqGAgtvUKbsPvIBtPNnZsVp-8pTKMjBYgLE-FiFlTUu6Ou-OrWG5oqPm7AFiTyGA4Qtd5PCkWjKWnOcWwJ1pcel2kg6kgBs5NYrcEBwZN5bjXVOLryfu6Gq66MM2DDrV6kEydV9xg_un9zJ0Jy5dRCVFHcuT9qQWZOh7InWW8x8G1IUxrYxKxBfIF83HjTQghKsWJcLI1dFQos0tFrrfDei0t321-TEDB4zTX2jiS_53O5p-eDZU7aJc_SlJvAKzO1VZe0fWkDxxhBTYck74e_GNT98eDpMqVZD9EpxiUTVb3WMVwxdZl7FaxjFqDgqXDuupUorU8bEvt1RbapA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
یک هواپیمای نظامی آمریکایی مدل C-130J-30، هم اکنون از پایگاه هوایی مک‌دیل در فلوریدا (محل قرارگیری فرماندهی آمریکایی) پرواز کرده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 57.2K · <a href="https://t.me/alonews/148307" target="_blank">📅 09:02 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148306">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">👈
تردد در مسیرهای دریایی و هوایی کیش بیش از ۱۴ درصد افزایش یافت
✅
@AloNews</div>
<div class="tg-footer">👁️ 56.1K · <a href="https://t.me/alonews/148306" target="_blank">📅 08:54 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148305">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">👈
ترکیه: اسرائیل به دنبال شعله‌ور کردن فتنه در منطقه است
🔴
رئیس پارلمان ترکیه: هدف اصلی اسرائیل ایجاد فتنه میان ملت‌های منطقه و کشاندن آنها به جنگ با یکدیگر است
✅
@AloNews</div>
<div class="tg-footer">👁️ 57.2K · <a href="https://t.me/alonews/148305" target="_blank">📅 08:49 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148304">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vXKkJYWJx9xui0xpnnOTE8GfRweIRWmZrM4a5R06wrkeN00_Wjv_ip5WSxpxuJXCndEYnL9_WiDzDkBqfDGJW_6V33vBoFUszHAheWQJR_NeQqlO9coSNsMCTbIUNMDF4uwjM0803g4ia3YARCffKG5Z12x-A54rjIuNnT1SVJpC5NpGjw7FCoqouaad7o7wwRdxgRaoToQsjPjbKXHYCOtNHYpm-hNCYO1Iopo0SLbBE7RfA0U8UV_iL71WYtG_8sjoe2DnvZG9CWUi441XvvyVnMK1AEu4wjf1dK64FNMBCC441nIw_9QhV-FAK-N9Wdn4UKIRSj7cPHTcj1Jrhg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
کاخ سفید از لغو تمامی برنامه‌های امروز ترامپ خبر داد
✅
@AloNews</div>
<div class="tg-footer">👁️ 60.4K · <a href="https://t.me/alonews/148304" target="_blank">📅 08:44 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148303">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">👈
آکسیوس: ترامپ تعطیلات آخر هفته خود را در اقامتگاه کمپ دیوید نیمه‌کاره گذاشته و امشب بدون هیچ توضیحی به کاخ سفید باز خواهد گشت
✅
@AloNews</div>
<div class="tg-footer">👁️ 59.3K · <a href="https://t.me/alonews/148303" target="_blank">📅 08:40 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148302">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/oShKLMCtYeYeqzGNqddf8Xo5uE7W5WxlNmfJWMW7N-UFEM4SGadO1vprjuxfUnDzQWcVlMqF8emEyfVhEo-nag9y2xOAa0Md-JKfPe3tIZvQIcM_0PM4nU3NwtJpDMDimCsmuA0IZRZKq5QPWMCvuCFD325ge7skiHgdfC7s8ilOLFXdWYAgGleEYz-Tl9Dh4LCLCM1VKB3RQ_00fwx4AeDqHMN5Ovb7FFY4gz7gpnWN900XsHLAVFHtprBNi0VuGw3R761wPZbs2GC90uw2kRvJG6Us0CaOjEvHxv5iDEYx1z4MhIqhkTBFNcSsaRvDqI3mZqc0dX9rOhz0RGq2EA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
فوری / خبرنگار سی‌ان‌ان: نشست ترامپ در کمپ دیوید به دلیل بررسی گزینه‌های حمله به یمن بوده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.3K · <a href="https://t.me/alonews/148302" target="_blank">📅 08:35 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148301">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">👈
العربیه: مذاکره‌ای در کار نیست و فقط جنگ تکلیف را مشخص خواهد کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 69.5K · <a href="https://t.me/alonews/148301" target="_blank">📅 07:40 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148300">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/umHGKLOmQuC20GlNvV0a7DbSO3WJPwuXDRB1YZS9yRKpqWJUloZ41LtWF1kr8ApXGGgJDzl2DdwY65EUA0286TsVdp2cs94lf9TuA3ZL0sAxwOPVk_qrfT1PlY8h_CAYiDKi7-gQ1N9GBHrMgbrGTGRVedoC8jYAq4jCoz33NM5B2JOB1-M9cdc0QhC5JTAmaI7rdU-R6oL4igIFAKH6tx6I-qyhYshZpxofiUDxztzS897UM7Ttlb4DLX_tlWW2qs0VpquixoSX59JsfC_owlFsEJeXFQEsdhU4qcKYMtAlYPXbKMBQRthgtxBgDq5mbvfcbQ5qSLKIXNyElmRfSA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ان بی سی: کوه کلنگ هدف اول آمریکاست
✅
@AloNews</div>
<div class="tg-footer">👁️ 73.4K · <a href="https://t.me/alonews/148300" target="_blank">📅 07:03 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148299">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromاکوپینگ | EcoPing</strong></div>
<div class="tg-footer">👁️ 81.5K · <a href="https://t.me/alonews/148299" target="_blank">📅 02:01 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148298">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SDiWP7k7KWIypqYQgiRINk1_RC4izINLX7-X9PjPaDJNDYsyvRzINLHvD22y8hHEvYY7mu4UGvKh0CfTlX5cdfHE7ILBcnYOLOT5RP9hzn826SEFasTFQnRtfqgtCNgN0MTv3tOFxSUx4kuCzZ7vsvp_2eeANTEbZ8bVyZSlsqtHwEeLZ7rcJ_k2kkNWjbBAmjwBItGlb_rj7SZ44HdJ2gy93b4rIErtF_UWNNumEWY5CQncE8hKBSnXuTvNh8a35x998XkoSfxzdA2vLCEpE91Gq7QKT9TTysY-dsd4r8-5J-IpUxoUCtPD0JwzZsPC0Hx9wL4MTONT8siYmUbuig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
افرایش شاخص سفارش پیتزا اطراف پنتاگون.
✅
@AloNews</div>
<div class="tg-footer">👁️ 83.2K · <a href="https://t.me/alonews/148298" target="_blank">📅 01:59 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148297">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">🔴
فووووووووووووووووووووری</div>
<div class="tg-footer">👁️ 81.6K · <a href="https://t.me/alonews/148297" target="_blank">📅 01:56 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148296">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">🔴
فووووووووووووووووووووری</div>
<div class="tg-footer">👁️ 79.4K · <a href="https://t.me/alonews/148296" target="_blank">📅 01:55 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148295">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">🔴
فوری/سفارتخانه مجازی آمریکا در ایران، با توجه به تحولات اخیر در منطقه، یک هشدار امنیتی برای شهروندان آمریکایی صادر کرده است و احتمال بسته شدن فضای هوایی را اعلام کرده است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 80K · <a href="https://t.me/alonews/148295" target="_blank">📅 01:54 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148294">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">🔴
فوری/سفارت آمریکا تو عربستان هم هشدار داد
✅
@AloNews</div>
<div class="tg-footer">👁️ 80.1K · <a href="https://t.me/alonews/148294" target="_blank">📅 01:48 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148293">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">🔴
فوری/هم اکنون منطقه در آستانه جنگ جدید
✅
@AloNews</div>
<div class="tg-footer">👁️ 80.9K · <a href="https://t.me/alonews/148293" target="_blank">📅 01:47 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148292">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">🔴
فوری/سفارت آمریکا تو ترکیه هم هشدار داد
✅
@AloNews</div>
<div class="tg-footer">👁️ 79.8K · <a href="https://t.me/alonews/148292" target="_blank">📅 01:47 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148291">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">🔴
فوووووری/رویترز: ساعت صفر نزدیک است
✅
@AloNews</div>
<div class="tg-footer">👁️ 81.2K · <a href="https://t.me/alonews/148291" target="_blank">📅 01:45 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148290">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">👈
سفارت ایالات متحده آمریکا تو بحرین و اردن هم هشدار صادر کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 78.5K · <a href="https://t.me/alonews/148290" target="_blank">📅 01:44 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148289">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">👈
سفارت ایالات متحده آمریکا تو قطر و کویت هم هشدار صادر کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 78.8K · <a href="https://t.me/alonews/148289" target="_blank">📅 01:33 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148288">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">👈
سفارت آمریکا تو لبنان هم هشدار صادر کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 79.2K · <a href="https://t.me/alonews/148288" target="_blank">📅 01:25 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148287">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">👈
خبری در راه است
⁉️
🔴
سفارت آمریکا در بغداد، اخطاری امنیتی برای شهروندان آمریکایی صادر کرده است و از احتمال بسته شدن فضای هوایی به دلیل تحولات منطقه خبر داده است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 80.3K · <a href="https://t.me/alonews/148287" target="_blank">📅 01:16 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148286">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/86b9da2b2a.mp4?token=KjgHqYedBGoM8Eddk3qF3xyHfcgDDT9Q5NA8-jWHjPlQalz5kbX8bQ7MtOgrMFRCcRtsF1exatAObGDDyzEzsG3R7JbK55FQsHTutFZ4eS7brZsFO6ES5B-Agm2z4T4W6cwb0mjlAAwr5bMXYqJGE_MadGQow8AFZ2HsMUx07Mwbj1lf0iYP-geMwUjnQGXynR6y4rWC5xuUUYuzQDU-XdsHbVqnHe8iI4wU8tK1O7rnszci-h3VyRiAODDjZIQY-m85kwb8bsdGmeV_nyeUeqNdmoS2_7tOL1NpY9kPsl3Vo6GsRcT-xTWkDOFzFhtZ138IaMgQzw35kUURLfG-XA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/86b9da2b2a.mp4?token=KjgHqYedBGoM8Eddk3qF3xyHfcgDDT9Q5NA8-jWHjPlQalz5kbX8bQ7MtOgrMFRCcRtsF1exatAObGDDyzEzsG3R7JbK55FQsHTutFZ4eS7brZsFO6ES5B-Agm2z4T4W6cwb0mjlAAwr5bMXYqJGE_MadGQow8AFZ2HsMUx07Mwbj1lf0iYP-geMwUjnQGXynR6y4rWC5xuUUYuzQDU-XdsHbVqnHe8iI4wU8tK1O7rnszci-h3VyRiAODDjZIQY-m85kwb8bsdGmeV_nyeUeqNdmoS2_7tOL1NpY9kPsl3Vo6GsRcT-xTWkDOFzFhtZ138IaMgQzw35kUURLfG-XA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
حرکات عجیب دو دختر جان فدا و مومن و انقلابی در دورهمی حامیان حکومت
✅
@AloNews</div>
<div class="tg-footer">👁️ 77.8K · <a href="https://t.me/alonews/148286" target="_blank">📅 01:12 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148285">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">‏
👈
محسن رضایی:  محل تپه علی طاهر پیش از حمله تخلیه شده بود و عملیات دشمن شکست خورد
😐
✅
@AloNews</div>
<div class="tg-footer">👁️ 74.3K · <a href="https://t.me/alonews/148285" target="_blank">📅 01:03 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148284">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">‏
👈
محسن رضایی:
محل تپه علی طاهر پیش از حمله تخلیه شده بود و عملیات دشمن شکست خورد
😐
✅
@AloNews</div>
<div class="tg-footer">👁️ 76.9K · <a href="https://t.me/alonews/148284" target="_blank">📅 00:55 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148283">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">👈
سفارت آمریکا در مسقط، اخطاری امنیتی فوری برای شهروندان آمریکایی مقیم در عمان صادر کرد و از آنها خواست در شرایطی که تنش‌ها در خاورمیانه همچنان ادامه دارد، احتیاط بیشتری به خرج دهند. سفارت آمریکا به شهروندان خود توصیه می‌کند هوشیار باشند و برای احتمال لغو پروازها، بستن فضای هوایی و اختلالات سفر آماده باشند.
🔴
این هشدار، ساعاتی پس از صدور یک اخطار امنیتی مشابه توسط سفارت آمریکا در اسرائیل برای شهروندان آمریکایی حاضر در آن کشور، منتشر شد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 78.2K · <a href="https://t.me/alonews/148283" target="_blank">📅 00:50 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148282">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">👈
هم اکنون بمباران جنوب لبنان توسط اسرائیل
✅
@AloNews</div>
<div class="tg-footer">👁️ 75.8K · <a href="https://t.me/alonews/148282" target="_blank">📅 00:43 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148281">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">👈
ژنرال ارشد ناتو: ما آماده‌ایم تا به هرگونه تشدید تنش احتمالی از سوی روسیه در بخش شرقی اروپا واکنش نشان دهیم.
✅
@AloNews</div>
<div class="tg-footer">👁️ 74.8K · <a href="https://t.me/alonews/148281" target="_blank">📅 00:41 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148280">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/pYj_qBQG2fKivva3eNp5KG2KG00_nXQUzuzECiua6SVHeLrPzWXyi7z2bk_lCMy9J-6BShaTwrEX6F3__cHhGCasS94JQsIQQnnoQb7A0_Wbw5qjCP-pT7M2dfz9CCvZfI7-E91eWWslhCjQM1m6N1YsTlqP0u6VLLDjTt87UNzSsrPJCEi9tXcD4n9JvFTRTJf5fqYR-oSF9RQSophsbIyVwrsnPpdhJeL58U2o9LmxS9EZ8kCV0AZihY8A45gVlN6z1fhd4KM74_EyMq8cocFwoFv1pEaDXrlGKfEqGEWua95KxcI05MEkYbphC50NwmobtY-gP7Gsg5PxFSKlWw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
عجیب اما واقعی
‼️
🔴
یه پدر تهرانی که ۷ نفر گروهی به دختر ۱۵ سالش تجاوز کرده بودن، رضایت داد و هر هفت نفر آزاد شدن!
✅
@AloNews</div>
<div class="tg-footer">👁️ 79K · <a href="https://t.me/alonews/148280" target="_blank">📅 00:32 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148279">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7bd1c6f7c4.mp4?token=XcrFIrms4q9SZwoNVIbmELUNIk3VG8H_qAnVSwnrluFkkpSHcBGPiiM1hFs9X5tQfFinAwnMOyGR0yTW_3qeL08kYnKBhhjtcR2zCwXhGwYz4hsg7X9unTh6Dlo2K9EWv7-xFvp2y9eQrkcHegb9gOvIBLsNn6Ij4TzDghMJTJnsYqqhgxEpc45LW-ErWRYUDTQ473c1pwBQ_JxPBbyWRM10gTsIBjRrlfK6dSkNXWM40vmUNWYu9jYwb99Q6Ab5_U56PGO4SmEGLsA3wo8IHU8CJMhKM7MeyjvBMnf85ysw5DOHoVcN9ds51joVSg-NgpqYrjLhvfgq7vK1f6I7mA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7bd1c6f7c4.mp4?token=XcrFIrms4q9SZwoNVIbmELUNIk3VG8H_qAnVSwnrluFkkpSHcBGPiiM1hFs9X5tQfFinAwnMOyGR0yTW_3qeL08kYnKBhhjtcR2zCwXhGwYz4hsg7X9unTh6Dlo2K9EWv7-xFvp2y9eQrkcHegb9gOvIBLsNn6Ij4TzDghMJTJnsYqqhgxEpc45LW-ErWRYUDTQ473c1pwBQ_JxPBbyWRM10gTsIBjRrlfK6dSkNXWM40vmUNWYu9jYwb99Q6Ab5_U56PGO4SmEGLsA3wo8IHU8CJMhKM7MeyjvBMnf85ysw5DOHoVcN9ds51joVSg-NgpqYrjLhvfgq7vK1f6I7mA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
یادی کنیم از استاد
✅
@AloNews</div>
<div class="tg-footer">👁️ 74K · <a href="https://t.me/alonews/148279" target="_blank">📅 00:23 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148278">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">👈
سفارت آمریکا در اورشلیم به شهروندان آمریکایی در اسرائیل و منطقه هشدار داده است که با توجه به افزایش تنش‌ها، احتمال بسته‌شدن فضای هوایی، لغو یا اختلال در پروازها و محدودیت‌های تردد وجود دارد و از مسافران خواسته وضعیت پروازها و فعالیت فرودگاه‌ها را مرتب بررسی کنند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 72.7K · <a href="https://t.me/alonews/148278" target="_blank">📅 00:15 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148277">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">👈
گفته می‌شود کارشناسان سپاه پاسداران ایران از منطقه باب‌المندب، بندر و فرودگاه مخا و همچنین پایگاه جبل‌النار بازدید کرده‌اند تا امکان نصب رادارها را بررسی کنند و بر روند حفر تونل در ارتفاعات مشرف به منطقه نظارت داشته باشند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 73K · <a href="https://t.me/alonews/148277" target="_blank">📅 00:12 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148276">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KztRVUl5o3fiMiH8nuzUZUB2WWefvjbTPpSg2TzwW9guGUb0PIS9hrb93b3QowdZniZ7sm77osIlB3uJULaoRXMEDsc_dzL5u25OQP8-c9jU__EokFjW_m4MseJyvTkv_D_VOpI2GKt8DEKovMOLkGE3qpMzUgrhnHspes7AkZNyvywi9an6lP4kbFFFxGD_GWJyhzZzMca0kWOzvr_hGAMw2PKbB4aBf7Vjgy5S285HAuD5uIEHynmg983Lz9vgdCnfXiYo_1qIWzTbMCXWfo-KCJ3ivH-h0QvF1vDM0rEr1JA5a1dvYlDa3rzT8Sqeo9FZA8vgcQlPWXRVPfMoBg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
این وسط زن سابق سپهر حیدری وارد اونلی فنز شد تا عکس و ویدیو اشتراکی بفروشه
😐
اینجا ببینید
😐
👇
🚨
مشاهده فوری</div>
<div class="tg-footer">👁️ 74.1K · <a href="https://t.me/alonews/148276" target="_blank">📅 00:09 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148275">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">👈
امارات گزارش هاآرتص درباره هشدار به اسرائیل را رد کرد
🔴
یک منبع رسمی اماراتی گزارش روزنامه هاآرتص مبنی بر اینکه ابوظبی در هفته‌های پیش از حمله ۷ اکتبر، به اسرائیل درباره حمله قریب‌الوقوع حماس هشدار داده بود را رد کرد.
🔴
این منبع گفت: امارات مسائل امنیتی را از طریق نهادهای مربوطه با کشورهای دیگر مطرح می‌کند و چنین جزئیاتی در سطح رهبران کشورها مورد بحث قرار نمی‌گیرد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 70.4K · <a href="https://t.me/alonews/148275" target="_blank">📅 00:05 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148274">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/af31257978.mp4?token=D8S0c02OzDsQVZWueXVj03R1DNT0lpTlVylNmxq-StPPWj9M2j4Fe97o5xmWcBtmszxsHKSEMnvUQCAWxHqmU4IhUd09G1jS24zQ_wTz6OWHBH2MIPD4Qo1M7tdmBtTpn14JB42jc4SHijE64pjjOQ4N-2rn8ijH3_SBetVO7vXWmLda4Z13NGRpg3X-BVC9x5kWHUNwCXiQINeIG08Qt1E1k--noCq4J_mL4grH2v0YQGd6Mitgc7uqCzNwTVdnn1lH_8dRgwGyUjk5tyZwdupPUJg0mFC7D7fcjn8gOwOyNtgMOVvxU_Bl9cqHx-fEPAN62WwkzH9BQYzCwGlLbA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/af31257978.mp4?token=D8S0c02OzDsQVZWueXVj03R1DNT0lpTlVylNmxq-StPPWj9M2j4Fe97o5xmWcBtmszxsHKSEMnvUQCAWxHqmU4IhUd09G1jS24zQ_wTz6OWHBH2MIPD4Qo1M7tdmBtTpn14JB42jc4SHijE64pjjOQ4N-2rn8ijH3_SBetVO7vXWmLda4Z13NGRpg3X-BVC9x5kWHUNwCXiQINeIG08Qt1E1k--noCq4J_mL4grH2v0YQGd6Mitgc7uqCzNwTVdnn1lH_8dRgwGyUjk5tyZwdupPUJg0mFC7D7fcjn8gOwOyNtgMOVvxU_Bl9cqHx-fEPAN62WwkzH9BQYzCwGlLbA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
عضو دفتر سیاسی انصارالله: این پیام به ترکیه و پاکستان ارسال شد که به خودتان احترام بگذارید؛ اگر از عربستان سعودی حمایت کنید، ما به شما حمله خواهیم کرد و شما را تنبیه خواهیم کرد، و دست‌های ما از فولاد خواهد بود
✅
@AloNews</div>
<div class="tg-footer">👁️ 73.7K · <a href="https://t.me/alonews/148274" target="_blank">📅 23:54 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148272">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/q4X9jGAmr4cfYjpzFHiPt66C_TMTVECsmQ0u2_wocqAgTYT3hmVg-Uc5tcQylSgSUczNciQX3kYoeFCQvSBopUCk0Z5WG5Bf50QIXoxG1HA1IwD-0EaAyfE5dF7LADmi4bO-89aD_tw-VmWxzez9KyS7HGyfFWadKHtNbYmdSY7bVsCklradoGZK5ODt9LV9jP-bnO93JgF5Mt6T4tufKLu9tcqqvsyyFsV-wCckDkAl48qNTb6WbrUClDKCUleZPy7iwJIL6wwhdLfAGIATPlSn3NDQMvCSvjFsQqjGmRyhOnXHTFXevf6t0pnkS8JB12PwLjjXEdv7PK81wiHJzw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e4e49b11fa.mp4?token=SEYKLD5LRPNqt5CBDMVOeS-TInaEHSGQW--I2-nH3dnUaHAsxu_7h3AWXTCEpeBgLxqKEY4Q9nIRWpcEwE6G7CCbqIln-85v4kylmAHty8KuyCXm5RVSlxT59jXhUntrZ9noVeLlB5gtYN_14653iUt1bn1sqcpX--wP7LJWb-BuCU73_ZFAC2lQGV3N0FOSxHRwO449MoIAXEJ36z8VGBW8u0iTCmftx9mXrM_tpKY6AfcltAST6V2kyIY1dc2ieZp30DXQEcjUCkuKJ96A3AkzklfrJD02HYGYAUBgFoGg0hE39qwvRxTf6_RFXHz9nEoPvsDxQ-V0KK0GCQhTVQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e4e49b11fa.mp4?token=SEYKLD5LRPNqt5CBDMVOeS-TInaEHSGQW--I2-nH3dnUaHAsxu_7h3AWXTCEpeBgLxqKEY4Q9nIRWpcEwE6G7CCbqIln-85v4kylmAHty8KuyCXm5RVSlxT59jXhUntrZ9noVeLlB5gtYN_14653iUt1bn1sqcpX--wP7LJWb-BuCU73_ZFAC2lQGV3N0FOSxHRwO449MoIAXEJ36z8VGBW8u0iTCmftx9mXrM_tpKY6AfcltAST6V2kyIY1dc2ieZp30DXQEcjUCkuKJ96A3AkzklfrJD02HYGYAUBgFoGg0hE39qwvRxTf6_RFXHz9nEoPvsDxQ-V0KK0GCQhTVQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
هواپیماهای جنگی اسرائیل حملاتی را با بمباران هوایی به شهر کفر تبنیت و منطقه نباتیه الفوقا در جنوب لبنان انجام دادند
✅
@AloNews</div>
<div class="tg-footer">👁️ 71.1K · <a href="https://t.me/alonews/148272" target="_blank">📅 23:44 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148271">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">👈
نخست‌وزیر لهستان: درس تاریخ 17 سپتامبر 1939 فراموش نخواهد شد، اگر کسی جرات حمله به ما را داشته باشد، با پاسخی قاطع روبرو خواهد شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 74.4K · <a href="https://t.me/alonews/148271" target="_blank">📅 23:33 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148270">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">👈
نقض منطقه پرواز ممنوع در محل اسکان ترامپ و اعزام اف-۱۶ به منطقه
🔴
هم‌زمان با اقامت دونالد ترامپ در نزدیکی کمپ دیوید، یک جنگنده اف-۱۶ امروز شنبه پس از ورود یک هواپیما به محدوده پرواز ممنوع، به این منطقه اعزام شد.
🔴
بر اساس بیانیه نیروی هوایی آمریکا، این هواپیما حوالی ساعت ۷:۵۰ صبح به وقت محلی رهگیری شد.
🔴
در جریان این رهگیری، اف-۱۶ مُنَوَّر (flares) شلیک کرد که احتمال می‌رود ساکنان منطقه آن را دیده باشند
✅
@AloNews</div>
<div class="tg-footer">👁️ 77.3K · <a href="https://t.me/alonews/148270" target="_blank">📅 23:28 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148269">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XQxK0AoUcGtWNgmG__iFkccoKaK4pTN99DJunNPTzHVo-FXsbkSid7WBzRq5CjqBQb2w1DdiJEI24n85pB79ztXOGV5tBBhfTSXd9cZnQA-65VupQKtMOCa_a-qF_AutL4Z9m279UeT1x248Lvvoj7rmmS4eNr3odOoo-71E16l48rfvTDP18BSYwohSCts60b_spgBG3pMtLUA1zhaK-3AAji3DvRp2Y_DURz37KZqZMh-y3d5S-DIK2RTd7B1MVnZCGfsc_Hhk0a4jRyMq-hPG5tlesJPjm9P-bDGG5nXMX1OarP_9wV8OawHTGJMpyeh109ZWJnybG2r_HCHHLA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
عربستان سعودی میگوید یک موشک بالستیک شلیک‌شده از سوی نیروهای یمنی به سمت شهر ریاض را رهگیری و منهدم کرده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 77.6K · <a href="https://t.me/alonews/148269" target="_blank">📅 23:24 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148268">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromالو توئیت | AloTweet</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CMPc8cKB6QEL4U268K5pmZUaxBPYSYoWTIRNk4Zm-vvZgS8ZFlNSWOHrqzjOyHStOLF_Tn3EME-9XLVupXjL2H4hLKyCnT3Xi_ybJVxUdnucCWjAEysG3zma3I13DshGhR_P9-5LU-Usd2tzvCluvrcvtCx6XZb-mSOj-aIAZ8nx5MXu09K7SMgYgyVxcoN7T5Z5rFBu4VlRxl0g-DqR5Kd77v_7jgFnbHHlM6xirHMumNHAbIpkfNLfbOt-dCmlNMQRSv81wSt5oDz4GURcRguRBqNJI85gtw6vJAvdomY6ALJHhRdPUFDZYtPzIV4wTo7NwBh1BSZFePcbH4ljPw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دو تصویر از یک کشور به فاصله چند دهه
[
@AloTweet
]</div>
<div class="tg-footer">👁️ 68.9K · <a href="https://t.me/alonews/148268" target="_blank">📅 23:20 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148267">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">👈
رئیس مجلس نمایندگان آمریکا: جنگ با ایران در مرحله پایانی قرار دارد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 70.7K · <a href="https://t.me/alonews/148267" target="_blank">📅 23:09 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148266">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">👈
وزیر خارجه ترکیه: ما نمی‌پذیریم که عربستان به بخشی از درگیری جاری میان ایران و آمریکا تبدیل شود
✅
@AloNews</div>
<div class="tg-footer">👁️ 73.4K · <a href="https://t.me/alonews/148266" target="_blank">📅 22:59 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148265">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">👈
امارات میوه و تره‌بار صادراتی ایران را برگشت زد
🔴
رئیس اتحادیه ملی محصولات کشاورزی:
بیش از ۲۰۰ کانتینر یخچالی ۴۰ فوت حامل انواع میوه، تره‌بار و سبزیجات صادراتی ایران، از سوی دولت امارات متحده عربی برگشت داده شده است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 74.7K · <a href="https://t.me/alonews/148265" target="_blank">📅 22:56 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148264">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">👈
سخنگوی سازمان غذا و دارو: واکسن اروپایی آنفلوآنزا امسال به ایران نمی‌رسد
✅
@AloNews</div>
<div class="tg-footer">👁️ 74.7K · <a href="https://t.me/alonews/148264" target="_blank">📅 22:45 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148263">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">🔴
فوری / ترکیه: آماده کمک نظامی به عربستان هستیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 75K · <a href="https://t.me/alonews/148263" target="_blank">📅 22:32 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148262">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">👈
آموزش و پرورش: ازین پس آخرین جایی که تعطیل می‌شود مدارس است
✅
@AloNews</div>
<div class="tg-footer">👁️ 75K · <a href="https://t.me/alonews/148262" target="_blank">📅 22:29 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148261">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">🔴
فوری / ترکیه: آماده کمک نظامی به عربستان هستیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 75.1K · <a href="https://t.me/alonews/148261" target="_blank">📅 22:25 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148260">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">👈
واشنگتن‌پست: محاصره تایوان می‌تواند آمریکا و چین را وارد درگیری کند
✅
@AloNews</div>
<div class="tg-footer">👁️ 74.2K · <a href="https://t.me/alonews/148260" target="_blank">📅 22:23 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148259">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/haPaQfHUTXcyxBGOuaHoQJcDQVzWcvIrOZoJsv_aLSu1nyqNQ-KmRDFwaQT2PVf21_IhgcOxKEMRcTbnlHKiPUcbcDHMR5ZVKIjJX4WZdT8PVBck81vQvwWhjz2Ud8PmytW30jsXsq47z7yp9TswdQ0mWEsJxF1e05Uv4RDgD3_TgRSiSIpGjY-CFX2vXL6S05NcsYNyiwj1_STIj5PmXy06jObiRVlmu53wPWz7EatGXNl364vxZMiHNpztAFs4ZfFzKODaih6a6GFPXBkG648B40obEhx47ezk-BZxatF3TPjUjF_YSaEIqKM8PKDEa99zm5E0tdmvXjy4rNgffQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
انتشار تصاویر از اپراتورهای زن پهپادهای FPV در ایران
✅
@AloNews</div>
<div class="tg-footer">👁️ 77.3K · <a href="https://t.me/alonews/148259" target="_blank">📅 22:17 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148258">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">👈
تاس به نقل از یک منبع ایرانی: ایران آماده بازگشت به مذاکرات است، مشروط به اینکه آمریکا حسن نیت خود را ثابت کند
🔴
تهران همچنان برگزاری مذاکرات درباره موضوع هسته‌ای را ممکن می‌داند، اما تنها پس از اجرای کامل توافق اسلام‌آباد
✅
@AloNews</div>
<div class="tg-footer">👁️ 73.8K · <a href="https://t.me/alonews/148258" target="_blank">📅 22:00 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148257">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">👈
دولت لتونی فاش کرد که اطلاعاتی در اختیار دارد مبنی بر اینکه روسیه در حال برنامه‌ریزی برای حمله ای محدود به اعضای ناتو است
✅
@AloNews</div>
<div class="tg-footer">👁️ 74.7K · <a href="https://t.me/alonews/148257" target="_blank">📅 22:00 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148256">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">👈
حوثی های یمن: با تعداد قابل توجهی موشک بالستیک به اهدافی در ینبع، تاسیسات آرامکو و ریاض حمله کردیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 73.9K · <a href="https://t.me/alonews/148256" target="_blank">📅 21:52 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148255">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">👈
ترامپ: نیروی هوش مصنوعی [در ارتش آمریکا] تشکیل می‌دهم
🔴
رئیس‌جمهور آمریکا: درحال تشکیل نیروی هوش مصنوعی هستم؛ درست مانند «نیروی فضایی» که در دوره اول ریاست‌جمهوری‌ام تشکیل دادم.
✅
@AloNews</div>
<div class="tg-footer">👁️ 75.2K · <a href="https://t.me/alonews/148255" target="_blank">📅 21:40 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148254">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">👈
کانال ۱۴ اسرائیل : ترکیه به طور رسمی مجوز فعالیت بانک ملی ایران را در استانبول لغو کرده است. این تصمیم، عملاً تمام فعالیت‌های این بانک را در کشور به حالت تعلیق درآورده است، از جمله تمام شعب آن در شهرهای استانبول، آنکارا و ازمیر.
✅
@AloNews</div>
<div class="tg-footer">👁️ 74.2K · <a href="https://t.me/alonews/148254" target="_blank">📅 21:40 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148253">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">👈
به گزارش شبکه i24NEWS، بنیامین نتانیاهو، نخست‌وزیر اسرائیل، قبل از سخنرانی خود در مجمع عمومی سازمان ملل، در شهر نیویورک فرود نخواهد آمد.
🔴
به جای آن، او در یک پایگاه نظامی خارج از شهر به زمین خواهد نشست و سپس به منهتن و مقر سازمان ملل سفر خواهد کرد، جایی که قرار است روز پنجشنبه ساعت 14:00 به وقت محلی سخنرانی کند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 71K · <a href="https://t.me/alonews/148253" target="_blank">📅 21:35 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148252">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/025ae7d2df.mp4?token=Ej623y6o_bvxiz_lyzntEit0F9H0GicPMxRHcqdDXPrHbzHB9BTh2-mKutmPcY9CBVbdIbiFg35Nq1wcy7zjb9XZ1lvtLOxYkmm5OSdyISGlLwBMxeewhGawSKG1fwgnHWjzDif0XwXCx2SXFa55gugqSQ-_y4Ga10pdSCZMVL9mw1omTezNlElYuXusAyj5s3F4zG9iG7GnkPwomG3EJcjKiMbpxi06Nxo946_dhvqK4q9up22tTVvSWUyLAjlOYp_wDxe7sfNePpf9EGPzDLr6NG0FQ0kpcoGpFqRdMcFLFxaHf1uSRr45qET3_JkpT53UcL0RAsl5Q6zz2oQm9h4mtlJzKLelAGK0m0VEMSY5mjzFmDOzRA4p823u1SIPUGtRvu_tJeiIVZUN66keKtgqIf7_6zz0jL9ftf3amCxjapZi1UYWJh1TKgbFWrZb8v0Rqsku-DHz_I0MyZLGvtvUbD8iy16yCsTamZU86NmhdBpLebmFHgFUuE4caUwvm65rgDY2i3KH3Cu_pRgmhbD0NoUBCoJ1pPtoCXJ7z4kveta_n7iVanIbHHwp_yJ2Nyyzy2YUr0gDqvJwvMNdHDwdEinQ5CEDll5M6aivYqKhq3U7g0lh6Rm5vr6eMjRmtps0QW_ziFlVANrSyl7WZ3aY6UlIA3QHiI5lWwFmzis" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/025ae7d2df.mp4?token=Ej623y6o_bvxiz_lyzntEit0F9H0GicPMxRHcqdDXPrHbzHB9BTh2-mKutmPcY9CBVbdIbiFg35Nq1wcy7zjb9XZ1lvtLOxYkmm5OSdyISGlLwBMxeewhGawSKG1fwgnHWjzDif0XwXCx2SXFa55gugqSQ-_y4Ga10pdSCZMVL9mw1omTezNlElYuXusAyj5s3F4zG9iG7GnkPwomG3EJcjKiMbpxi06Nxo946_dhvqK4q9up22tTVvSWUyLAjlOYp_wDxe7sfNePpf9EGPzDLr6NG0FQ0kpcoGpFqRdMcFLFxaHf1uSRr45qET3_JkpT53UcL0RAsl5Q6zz2oQm9h4mtlJzKLelAGK0m0VEMSY5mjzFmDOzRA4p823u1SIPUGtRvu_tJeiIVZUN66keKtgqIf7_6zz0jL9ftf3amCxjapZi1UYWJh1TKgbFWrZb8v0Rqsku-DHz_I0MyZLGvtvUbD8iy16yCsTamZU86NmhdBpLebmFHgFUuE4caUwvm65rgDY2i3KH3Cu_pRgmhbD0NoUBCoJ1pPtoCXJ7z4kveta_n7iVanIbHHwp_yJ2Nyyzy2YUr0gDqvJwvMNdHDwdEinQ5CEDll5M6aivYqKhq3U7g0lh6Rm5vr6eMjRmtps0QW_ziFlVANrSyl7WZ3aY6UlIA3QHiI5lWwFmzis" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ارتش اسرائیل (IDF) در ادامه تحرکات نظامی خود در جنوب لبنان، اقدام به تخریب منازل  و زمین‌های واقع در شهرک «منصوری» با بلدوزر کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 71.4K · <a href="https://t.me/alonews/148252" target="_blank">📅 21:27 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148251">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NiM88_Bl61ik59z4q9Rsm3Zk7yelUCDCptbZijIlryWuSO9bELtUSJYXOiE960HilDs9Jx9RL2lSWBBFgeg-a9KaMMo_fB675YVjMwYu99lkshy7lKzV246MxkO2wrIqYUi0-AytApYs57QfdKSJBVtMzBxvXz8fCJe5E5UWUL6tjvW63f7RxkdbkpDlwARlmsDc1fRQieGA88Aly6xRkxoZB0ttwsWlsQDtOqV4GMU4u7X8daetaQkKig4obn3TbG0e8Dv7RuyB7av7TGkO-C6l35vYVP0P9EWJdbJ6Cp8-TFVUJS1FgWxrKi71UNeiOkkWqFhoEKgiSeNHIMH_9g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ترامپ در تروث سوشال: متأسفانه، دادگاه عالی ایالات متحده از شجاعت برای بزرگ کردن دوباره آمریکا محروم بوده است.
🔴
در طول ۶ ماه گذشته، با تصمیمات معیوب، سیاسی و احمقانه خود در مورد تعرفه‌ها و شهروندی حق‌الولادت، آن‌ها هزاران میلیارد دلار به ایالات متحده آمریکا خسارت وارد کرده‌اند و برای همیشه روشی که مردم از طریق آن شهروند کشور بزرگ ما می‌شوند را تخریب کرده‌اند.
🔴
این فصلی غم‌انگیز در زندگی و دوران آمریکا بوده است، اما ما پیروز خواهیم شد!
✅
@AloNews</div>
<div class="tg-footer">👁️ 69.4K · <a href="https://t.me/alonews/148251" target="_blank">📅 21:23 · 28 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>

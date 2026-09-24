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
<img src="https://cdn4.telesco.pe/file/GzIBTwRN5nn2fclwzFCG9PFzy0nXuAg-OzoitXLlwznnnaGY2HoB-7T1X2kSC4I5_hA2sf-qDr-GJoe6EWZtnIoiEKPX1O2_0ZiuaCuF51pnEyvnUGtj10DKPjvi9PDg4cXswTwCFA_YS1RkdSHJzFqJ0ivpB0HcuHRZU12XuiEsr62pHr4JjgqIEWrrFNL9kLzBYzWk1ZMf5GkiDBATox4DvuDXeYs-caUR4S9zB4SameMFDyRHiZXrWkkDQ2U-vvVjKT9PChJ6LYQgCKPZiW8z_eouCd8c_J9juYBfbEG8sWbjfS_1DfD58-0iWKIlnIZPDgnrCbWCovSHNZOr9g.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرفوری</h1>
<p>@akhbarefori • 👥 4.19M عضو</p>
<a href="https://t.me/akhbarefori" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ﷽تبلیغ درکانال خبرفوری@ads_foriارتباط مستقیم با ادمین تبلیغ@newsadminجهت رزرو تبلیغ تماس بگیرید. 09018373801؛ارتباط با ما@Ertebat_baforiiتبلیغ در ۳۰۰کانال تلگرام@Maino_marketer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-07-02 14:17:46</div>
<hr>

<div class="tg-post" id="msg-692613">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">♦️
جان باختن ۹ نظامی قزاقستانی در جریان یک رزمایش در دریای خزر
وزارت دفاع قزاقستان:
🔹
۹ نیروی نظامی این کشور در جریان تمرینات آموزشی-رزمی در دریای خزر، بر اثر وخامت ناگهانی شرایط جوی و تشدید وزش باد جان باختند.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 2.05K · <a href="https://t.me/akhbarefori/692613" target="_blank">📅 14:12 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692612">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b9b7e8145c.mp4?token=Dkd3RHLqatFbzNdTiqNFt4UERJYA_D601LOpU4vKXatOiWHYlxMphtTJOxmenDG8LOpIWWuEkw9jrsDPs7DjJiVAr3Ou-sKxaRlw9BkV6VZVKkniVg21bkNLT7LdU3c8zU5z9s-x-irAhxh46beT-V_ObeWP5IG8ssllLBDm3jbpNRo38JEpwD6HOeF4GlCzEhMFCZcZLxFaqZtigEDl4LFgZNMCsBrLtx69nnaFkbqQa_f0-tgPTyN_OjzG7FojkfGDc405YmwDId-5XsX1BXe6ShGrhNrX8l3Lbjil-IlvdCjItzg7CKZwyJRqUxPKMRYRV12YPLe79APEnNhreQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b9b7e8145c.mp4?token=Dkd3RHLqatFbzNdTiqNFt4UERJYA_D601LOpU4vKXatOiWHYlxMphtTJOxmenDG8LOpIWWuEkw9jrsDPs7DjJiVAr3Ou-sKxaRlw9BkV6VZVKkniVg21bkNLT7LdU3c8zU5z9s-x-irAhxh46beT-V_ObeWP5IG8ssllLBDm3jbpNRo38JEpwD6HOeF4GlCzEhMFCZcZLxFaqZtigEDl4LFgZNMCsBrLtx69nnaFkbqQa_f0-tgPTyN_OjzG7FojkfGDc405YmwDId-5XsX1BXe6ShGrhNrX8l3Lbjil-IlvdCjItzg7CKZwyJRqUxPKMRYRV12YPLe79APEnNhreQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
اگه این نکات رو نمی‌دونی، کت‌و‌شلوار نپوش! #فوری_استایل
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 6.4K · <a href="https://t.me/akhbarefori/692612" target="_blank">📅 14:05 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692611">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">♦️
سرلشکر صفوی: تنگه هرمز هیچ‌گاه به شکل قبل بازنخواهد گشت  دستیار و مشاور عالی فرمانده معظم کل قوا:
🔹
جمهوری اسلامی ایران به‌طور کامل «تنگه هرمز» را مدیریت و کنترل خواهد کرد.
🔹
ما و عمان به یک سازوکار برای مدیریت تنگه هرمز رسیدیم اما آمریکایی‌ها در این زمینه…</div>
<div class="tg-footer">👁️ 6.12K · <a href="https://t.me/akhbarefori/692611" target="_blank">📅 14:01 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692610">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">‼️
رسانه‌های عربی از شنیده شدن صدای انفجار در شهر جده و طائف در عربستان خبر می‌دهند/ خبرفوری
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 6.43K · <a href="https://t.me/akhbarefori/692610" target="_blank">📅 14:00 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692609">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">♦️
سرلشکر صفوی: تنگه هرمز هیچ‌گاه به شکل قبل بازنخواهد گشت
دستیار و مشاور عالی فرمانده معظم کل قوا:
🔹
جمهوری اسلامی ایران به‌طور کامل «تنگه هرمز» را مدیریت و کنترل خواهد کرد.
🔹
ما و عمان به یک سازوکار برای مدیریت تنگه هرمز رسیدیم اما آمریکایی‌ها در این زمینه کارشکنی کردند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 7.43K · <a href="https://t.me/akhbarefori/692609" target="_blank">📅 13:59 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692608">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qTDs70ywhHJmrfmkoVRHjM9_svqMKpq0nKDA2L-Fz1eJpC2nkYMx0IaAht5Qxw0mcC-5s5Nsp_x-tjJYo1yoWI1EBwoDhpRE6Hhu7avE-3W92shfV61Tg9BIQXTgvV-CpicUG0UzLKTNaOT8Rc4mSFjLutOE7ulR9hIRZDyeKQRXPRCbXDIK_a7Cz2e9bRbPPf1lJLy5Ii8AMkxx9ZUvLoUeNJ4HbnqDWRUer-sKWHxOxt7yeMfImV4fiPX0tXN9cyh2AH7mpPizMS7huWU3wLUFfWf4xBOMDDP8r3M_akcWDH9fG7eCVwOLflb9GVNhlYHCfndppuv58w4dHWpuLA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
همتی: انگلیس روغن ریخته را نذر امام‌زاده کرد
🔹
رئیس بانک مرکزی در خصوص اقدام دولت انگلیس برای تشدید محدودیت‌های مالی علیه پنج بانک ایرانی در این کشور، در همراهی با سیاست اقتصادی آمریکا، گفت: این همان مصداق روغن ریخته نذر امام‌زاده کردن خودمان است.
🔹
به نظر می‌رسد خزانه‌داری آمریکا در فشار اقتصادی به ایران به آخر خط رسیده باشد و کشورهای مختلف نیز برای نشان دادن همراهی و تبعیت خود از آمریکا، فعالیت بانک‌هایی را که بعضاً سال‌هاست در چارچوب تحریم آمریکا هیچ‌گونه عملیات بانکی در ارتباط با ایران ندارند، برای خوش‌آمد آمریکا مجدداً محدود کرده‌اند.
🔹
البته خود ما نیز برنامه داشتیم که برای کاهش هزینه بانک‌های غیرفعال در خارج از کشور، محدودیت‌هایی را بر آنها اعمال کنیم./فارس
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 8.45K · <a href="https://t.me/akhbarefori/692608" target="_blank">📅 13:56 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692607">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">‼️
رسانه‌های عربی از شنیده شدن صدای انفجار در شهر جده و طائف در عربستان خبر می‌دهند/ خبرفوری
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 7.43K · <a href="https://t.me/akhbarefori/692607" target="_blank">📅 13:55 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692606">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YFErbUp_Cskq7tTdgkGYKLGiXRSo_TE8m-VWN5E_H0LmUzlWr55gML7bkQ0-L6kFXLjwzFBSzhpkqR88sW3ubH7f8stOKoH-QmHOBVJYB0B9StxMJ6JYf3_jQM52HYftNlVGUZYE9C3rDOUJR8TSzlUpyk9mLNKFHL9kQ96vzB393X896YUkLc2ehUYk7avIbxWwoIvk-CLM1shbYpeVSNPcdhA2d4amsTBTHx4tG6A3uGY1zA8yT5efNWcQQBc1zLoGn4KRdwtfZVhxTr_sV7uQ1QArSP3wNpK8mWBjBTLWozwSIljKpKVbHvP-VrvPOc2UZUunyN1yq15nbw6xCA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
رنکینگ تیم‌های ملی پیش از آغاز فیفادی
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 9.77K · <a href="https://t.me/akhbarefori/692606" target="_blank">📅 13:48 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692605">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">♦️
قیمت گازوئیل در اروپا رکورد بی‌سابقه‌ای را ثبت کرد
🔹
میانگین قیمت گازوئیل در اتحادیه اروپا به ۲.۲۳ یورو در هر لیتر رسید.
🔹
دانمارک و فنلاند با ۲.۵۶ یورو در هر لیتر، گران‌ترین قیمت را بین کشورها دارند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/akhbarefori/692605" target="_blank">📅 13:40 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692603">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/oI9VNw8M2GibwialaXXZf-rYsiqQvm5FjL7fo6m_bSLcpmQ-D6ToyLpJCwzeFJYMN1jaHNcWtzxZ0weziwjnJzq3osW4W34n0hhpj_KSOmw88PwHhieTgVVt3TNSfguFCCukGB-hLcfNRx03R_G3HZ8goyuJeiZ2_T7w6gMKCvUy-4FZfgdY1jozgAijkBEVxekfUhr5IaR5m0zhVMGe4bOw5s90ugdhIxoP8AsUE4aHMCi9uj6sVuqXpX96BpCW7k3-jom9N7UfJRe-kEZ6l7Aa7PWIrQScBr1O8SvwCg-tih2GbBl3DBplGEJDOeF7FvzvLPKbE-1dWahqvmI5eg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/MCQbRj-ZVlUyehgI6Qm1w0Z4Cviea81ALbCnVijnN8OcnK6Bzk6TuuPEBfcZkp-bbLcWpVHC08uz4li8W6-DOHHambB0biKGVr3LUSW_vFw4sHXu5DCFBPx0L15i7dNZSeF8L1P00i8JW_-5V8Idhx717JolBocqS5Z4iKVMKoQPiYcEMS7E_esr71WOpMA2TV_AmlIodxUj4v27gVILBrK--w_Ky9Q4EWKUNYEevpk9F36MFtrRZtI3aG79b_bFe5tecBIHfvRUT8TL1bzAnt5ww2mJ81p0PI0aMPu4wuSbrSq9_fbE9Cg6DRMLAq3DUut5TKV4D3PTSVqVYAophw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
صدای شنیده شده در آبادان به دلیل نقص فنی در پالایشگاه بوده و در حال برطرف شدن است/ صداوسیما   #اخبار_خوزستان در فضای مجازی
👇
@akhbar_Khozestan</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/akhbarefori/692603" target="_blank">📅 13:40 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692602">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ue9eGJ3lCZurJOdqi_8Q2Dk321r6DnQv1u1iFo8nODvkHbSj2NZrS7L9RoQv0iUe82I_o5ecB5bvJ8tWUQ70l4S4CSKiuRiWWzRCpK6EPmWm-itNZzoje-TVqYnpkRK_r5GGuIt5ncqmVkPDnVwwEM0TPHzymeWsvyasjUasGbYUUIbBxv5UJ3HkLj2k_GzG5wM94vptlw4gkaM1lHESctaCnaEym-sb-55NCLCobrDgciDn-oxmVJa31HQ7zB652fvnZf6ZS55sIYS3LuOuoTXi9vToSMya5KaGSHA3NLT6n65CZeo_fB5X1s8d8A9NCFL_PYdCiwFrc64rMF99FA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">THEIR STYLE, THEIR STORY.
هر نسلی، استایل خودش را دارد ...
40% OFF
GERAD Kids & Juniors
تخفیف طلایی | روزهای پایانی
Instagram.com/geradofficial</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/akhbarefori/692602" target="_blank">📅 13:35 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692601">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفروشگاه قرار</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Q6mNU4sSpriTAFxcV2OVmGNRIAFYNIoOzQIki-VssLEXoIBOTrX5vCjHWS36t7vjX8Rmq3UbdAV3KN0Jpz4WX_tB9B3RNv6o8qUdV5vVCYLNWU2aJONZ-x0ce841iNjKUg_oGtrtAVlMDCVGJJrzm-VGtUxZSF-Pm2nJjoZu2toi7l2t1ctIxpTQM3RRPSMlb_4b2XVjb1Zth5w32_yPRePO3NVsZB8BaWH311LtmZG6AOSgD4qQ0tTwS-ZstgzH30PkO_ETMbictARMSuYK5J4356VRMygCs_c4c4RImAUcJO4gnJOyImlM8hvVwyOiFA4ipbSOUOuzzEZ-_YsH-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💼
Work Mate | دفتر کار همراه شما
همه‌چیز برای یک روز کاری منظم، داخل یک کیف حرفه‌ای.
از جلسه و محل کار تا سفر؛ وسایلت همیشه مرتب، در دسترس و آماده استفاده‌اند.
✨
⚡️
پاوربانک ۸۰۰۰ میلی‌آمپرساعت
🔌
دارای کابل
Type-C و iOS
📱
هولدر موبایل
📋
تخته شاسی
برای یادداشت و جلسات
💳
جای کارت و مدارک
🗂
نظم‌دهنده لوازم و وسایل روزمره
🎁
انتخابی کاربردی برای استفاده شخصی یا یک هدیه متفاوت و حرفه‌ای.
💰
قیمت: ۶,۴۹۰,۰۰۰ تومان
📩
سفارش:
@gharar_order
👀
مشاهده محصولات:
@ghararshop
🌐
ghararshop.com</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/akhbarefori/692601" target="_blank">📅 13:31 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692600">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">♦️
زاکربرگ از گجت «Muse Charm» رونمایی کرد
🔹
مارک زاکربرگ در رویداد Meta Connect از «Muse Charm» رونمایی کرد؛ گجتی کوچک با بدنه نیمه‌شفاف و نمایشگر تمام‌صفحه که امکان گفت‌وگو با دستیار هوش مصنوعی را بدون نیاز به گوشی فراهم می‌کند.
🔹
متا قصد دارد عرضه محدود این محصول را پیش از تعطیلات کریسمس آغاز کند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/akhbarefori/692600" target="_blank">📅 13:28 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692598">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">به یاد ۱۶۸ غائب امروز مدرسه
🔹
امروز، به یاد کودکان مظلوم میناب ۱۱۰۰ بسته تحصیلی به مناسبت یازدهمین سالروز تأسیس «خبرفوری» آماده و برای ارسال به جنوب کشور راهی شد.
🎒
❤️
🔹
۱۱ سال همراهی بهانه‌ای شد تا این‌بار سهمی از این جشن را با کودکان جنوب ایران قسمت کنیم؛…</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/akhbarefori/692598" target="_blank">📅 13:17 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692597">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">♦️
بانک مرکزی: صدور چک‌های رمزدار از سه‌شنبه ۷ مهر ۱۴۰۵ ممنوع و پذیرش این چک‌ها در سامانه چکاوک نیز از اول دی‌ماه متوقف خواهد شد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/akhbarefori/692597" target="_blank">📅 13:15 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692596">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">♦️
دلیل بازگشت پرواز تهران - دوشنبه به فرودگاه امام(ره) اعلام شد  سخنگوی سازمان هواپیمایی کشوری:
🔹
به دلیل اینکه ترکمنستان مجوز عبور ایرلاین‌های ایرانی را از آسمان خود صادر نکرد، پرواز تهران - دوشنبه نتوانست در مقصد فرود آید و ناچار شد به فرودگاه امام خمینی(ره)…</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/akhbarefori/692596" target="_blank">📅 13:13 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692595">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">♦️
ادعای العربیه به نقل از مدیرعامل شرکت آرامکوی عربستان: هرگونه اختلال در تأمین یا فعالیت‌های شرکت آرامکو را می‌توانیم «ظرف چند روز» برطرف کنیم
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/akhbarefori/692595" target="_blank">📅 13:09 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692594">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0c42c31b18.mp4?token=DxK0gepkOmQaJUPPQjfO4LK3ryz1fwuyo-gtkt3pSWjhtAokZ-fgMvK255Fugkqfe3sThd33V_z39iCxwJecG74wB-Cu4wjBPTCfiKXBrC8YP3AuQ9WzEJg3L6tZTxN8MrjNBzctDIkztwXa-B7LcRAyoPLzjUAYBhVPX5iTGiz02RTUyL9LsibqzDqAxJKv64eL2Vwk01MbClHmL-qGEzkFfIvtS4Wlg8Wwf8kdiWJEIjYFXLpD7LnRBnFEhxtF-5KEFJpcoPEELNltLJ1I4JNvEECyGBeIyV4VixYOJjBljbxgjW3TYrNndLrY6IxYGTSbMP6Z1w45invAvXR6aQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0c42c31b18.mp4?token=DxK0gepkOmQaJUPPQjfO4LK3ryz1fwuyo-gtkt3pSWjhtAokZ-fgMvK255Fugkqfe3sThd33V_z39iCxwJecG74wB-Cu4wjBPTCfiKXBrC8YP3AuQ9WzEJg3L6tZTxN8MrjNBzctDIkztwXa-B7LcRAyoPLzjUAYBhVPX5iTGiz02RTUyL9LsibqzDqAxJKv64eL2Vwk01MbClHmL-qGEzkFfIvtS4Wlg8Wwf8kdiWJEIjYFXLpD7LnRBnFEhxtF-5KEFJpcoPEELNltLJ1I4JNvEECyGBeIyV4VixYOJjBljbxgjW3TYrNndLrY6IxYGTSbMP6Z1w45invAvXR6aQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
واکنش چین نسبت به تحریم‌های هوایی آمریکا علیه ایران: از تحریم‌ها پیروی نمی‌کنیم
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/akhbarefori/692594" target="_blank">📅 13:07 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692593">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">♦️
پروازهای ایران-تاجیکستان لغو شد؟
🔹
«پرواز هواپیمایی وارش» از تهران به «شهر دوشنبه»؛ پایتخت تاجیکستان؛ از مرزِ هوایی لغو شد و به فرودگاه امام خمینی بازگشت.
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/akhbarefori/692593" target="_blank">📅 13:02 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692592">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b277e5e789.mp4?token=qozOkR6ct76zNfb6ou_Sd5C2xR0r1NpNEGPevjNqEoiWCdHaboPHbM_2n7O0IuqiyzHlEnR3mv21XXKNhNa_UPex2s0yJCOV7h-J5hmig0HMPoiopZi0q-6IJH5wEr5FZuBMfyUep3C2sG14t0gb30wskrExknjsIhEt32if17TKt1SfqSjl8Znsc1Kam4YQFwie2olZ_mANRrN5Cg7Rbygu8ZffPYwjDxMEzWWpPKnpK4Ckd8Xo3p3L_7mTxp_QiRYGcrNhPrshAW2YFi1WifHFlZFXS0wJFcXfgKDxdYxOP65_z4qvio5Wrqs2vPyDcIHryEARd3k1IYmLgdfVAA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b277e5e789.mp4?token=qozOkR6ct76zNfb6ou_Sd5C2xR0r1NpNEGPevjNqEoiWCdHaboPHbM_2n7O0IuqiyzHlEnR3mv21XXKNhNa_UPex2s0yJCOV7h-J5hmig0HMPoiopZi0q-6IJH5wEr5FZuBMfyUep3C2sG14t0gb30wskrExknjsIhEt32if17TKt1SfqSjl8Znsc1Kam4YQFwie2olZ_mANRrN5Cg7Rbygu8ZffPYwjDxMEzWWpPKnpK4Ckd8Xo3p3L_7mTxp_QiRYGcrNhPrshAW2YFi1WifHFlZFXS0wJFcXfgKDxdYxOP65_z4qvio5Wrqs2vPyDcIHryEARd3k1IYmLgdfVAA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
‏
آتش‌سوزی در زیرساخت برق آمریکا
🔹
منابع محلی پورتوریکو گزارش داده‌اند که بیش از ۲۱۷ هزار مشترک در چند منطقه این کشور دچار قطعی برق شده‌اند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/akhbarefori/692592" target="_blank">📅 12:56 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692584">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/OC1EEZ0EiPRdTNOXuwIqWNe-V-N1D6CvModd7dZxPQm3-fG5F5V_F8hagY93zxkQbdy_R1ejgZ64D1W7j6G2Z2Tua5BdY7H-dE3U1Z5mVQmlu-afEJpa0s-VxH3nrzgmVY7v8wd1POeOdmg2z3cSbBKtPbXirWTh-5ZRV5m4YPVZyHe4b2VtzV2JlWwF0RKJDnUN_NH4CMFk12lTp9WJUfpqLOWBOtVbc6KJyLTBMg6Ej1TwwobYnnNGBqncxHIPi2KBJgKboPq7X41X_SYV65s8lcXGnzbBQ-sxHe4P0GoJBWPMV7dXeHyYyuNMU50TLMI7EF1T40fek1H9jTswEg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/PSSID2GsJEpGShst_74UamxlZQLpYBGj-rKjtdTvi1o_82quiR2kxtcZFgz1BPrOuTK9CDbrL01hOu7HqX2wlFqUMDBS48etkzifPB0OBVp9bMzRjbSODvPzRpHRb-knqIOdSEsmXuWf5t4Ysyvvv1lVDq5bsk42wpiSc8Kr6C3gTHf6Mibo0nQOIj54V8QGSt7cQk3vPoG8SZp96SnCB89WH6OqMnptc4iyCHwunkFUJ0bs3DtUysPCk7ZM5qc_YbqXnCO5mNa4FujcT_qYyXIdkHqbBYwvl2rqxd4w2c1hxJfv6jgaKGlv5rvbheqE2PmeuPys5awDxCInfbCywg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/gvgDlCtjtNtQNnq6j3H5drmPOoK5tsqynGdtNABF8A7psJsb6HSrlyrpZaBNMQIOYjFPV1rEQs915DFDtT-AWWJYk0_iYw_yW43QDjJbV0dN_5ZddVGyf2rvQjFAoeXQ7DFpbKuMQsB6zN4ZBeCKFD56MRqP2L4nzfNhUuLGmKdhpyf88hUuxp-rdn8-VrmXpHo9mO_EGhQ_PJK3AyhZzL33OMLrvaGfeSHw3RCvr4PpwzkJVroR7ARd4AGQLD25wgPceFCZ0isPqOEvgis-MBPj03xySe3sT_wFriUVbdUfReBN3eNz4bEI_aXca2wevtnMpwHDqj4MOe_-2biqHg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/rmpz874tEJf_FFtRva7XpNHQTjZiFR555u7hhnhXUxZYKSdeu7kAABrhin7ACBt1rrwh4K7roj0ZrlIbThpVbTB38JQBdGInqzDsKcNVTd0BxVeNjWPPTB1KtGMfye-hKnmCgJoXnJtYLAe_Mj_lLxs7MUu9fxDOHQA5hdYoDdYOVFaYwwUVulJk-rWWTdsUgd_fOwKIEBqJ56lp3AObol20BAZ4bn2dDVtFBr1g3iejSaMNZxftmD9XB3EqsXjX2fYUQbAu_5bHUitkRE0mZCE_06U97h3VeexZ-x0SQqpdwSHYcQ25takexEydMWAx2vwHlaC5RwxclN6BpRS1fg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/SxgxBu6wERzwdwpTrOlxm5ykBwkejvJfaPOdRTzfScoIA3NjNSdlBepB8ZSdpVNHVcBkvGrU0hpcHHPBHNYUi70_e4oNegnro79ZDcybDCQDhA7pCVSj23P7f8HH1skelmS-wqdn1C0-xy-FNCLUlSeEqBNVnpgdjrzqwVb7Ntn2kbqnvjJi-m4AOlRgCKgEcgJp3fRRujM7B5rhWDIOXqRrBjYjoCPEBjXqLqJ9iheMSQRpkSbbiMySF6mvARSAB-pkh48J0crpBXHeA3hIUX5rM6gvnX5uoJeJxRfpSD21joZKJ5rTQJ4VmdXh-8ie0glbi9Gi1YIb7WU_MQevIA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/j2BP6MsSKH_DjCq3wGsVepFG2PtgCvW0aNIu6HMC_Z9qob672kqUaU2bDokKW78d99H_Akm9TGm0HwqGTFxyEwexjV-QjJv3zUTLLJXTjEA9UZ0tor5bIT_k1OpnzkeGexvqniF7NAB3403jGYT6pBPK57HmYNrkIe-24lK3JKv5kJ_uFT0VvC6wTrQPGnVQrUX-EIAhQSfDwGfqtlNgTCSHbGO3mky6yFNhNtXnKGUBIvScrcqfEsWlB_gHPUAHXIyAE6OqyBULKbnPaYGah-KSotIShOGH7EdW6RvtJ9zOZljvUuFCAnmVbAAFf9mB2KCdWvhtosTZo6LAzXzoxA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/aQRLL3iTMYIxOSWzGc05khOOL4uWXpu4YDTAhLms8QNmoLCJjhHHr4eFwp74cJnhYL9V-Wn1mDs1h4-nQAfntb_0NGrfnjG2JG5Il4uKJwycaNf8VNnBNTJNgsVKTJ2Hpssr5dJ9BnlQCDvC2SuMgQhR8pHek4Ix72QlXCvyfVgcrmtscppmHIqiaEh82mtuw5_69738cpVY_D9HVgslZHXgLNwEclilm3x6kzFR64Kuif0VzSM8mS10vSwETFG2iiY9M6Xyol8jZ8oEJlkvwnwOoIzUt450JEPonyaRvgd4AQlRAOL7C3n4oNw3Yi8rQdaPed_Rjo0Ikaxz0JZn1A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
هفت ترکیب عالی با گردو
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/akhbarefori/692584" target="_blank">📅 12:50 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692579">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/K_ygjUSEqC2kz6TFKSEZX9S9FVsx3QkdaLf86felyaVY77UKllkANZB-AebAoZLGOP968rdHuDIwhUzMdjedyGGG9uFUUVAAN6sDNXDJgjNEjIcT9MfFS-5uR9JnWSCJJbxF-OzwxETT_R3P9w4ON9tj2Bs4Q_ovU5vM8eKphDen64t4qn7OEX2-5Qr1mJGqLJz8fLEvB-r7taBdIjyPCy2aw2q3YO83a4EdF4VJXiao-vJk32FQYkv-mJvNSa5Q_fgtNN2zIpZkGvWoQzJC8Ejb6RdpGNV0v0KuyX8miISzlFiSI_jrMF0F0SMCUxBmESmIcU4iME2Ln6KWrNPZ2A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/gQl_tfLJ7ug9VgCUXwajEvNSm0_5WgNr0QEWGovtdCgYw-_JXhD4f2Lj3__4uiFblh8dzyKKkJXnWejsW6DSSevJA9pqfb3cBwjKhGkT48oakHd8aUjIyT-YN2GAwU3lfXRVT_DkY4EUJ13aFpRRHV3B3dUT5tEF47vicvoli_y3r0tr9pDa33FrtFIt0Nwp4vWyCWOsOb61S5XyHv4yfg1jY3mMLDtfHNyJcWd3jRwNLln0vIf5N4C1Apiqe1CEKajNhrJKjN243FhtKn-YoE7yCpq7dtWBwuAAKVpv7SHnWhib428l8aAjEHrdxwxI1WP6RUGuE1oV8N3wUcY1Xg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/RYnBi4UXcrzppI5nTO57wbIrJG8eCLFDthRWv_bSqOVhEcUwYCDY2HJpmDLGyFv_ps5i04NKPLaEoYTaIxNBAOIanG0RDoOeON4SrGeiW6vDXVc2dXeH7MKcaGgsIrNv_yDcpdO0zjjWTWTnTOOhH-UlMC6MsG-sNtiq6DgwcAv0BOLmuihvuqn0GKFaky66nSzx9TDh_nAnoPAYkcS4jUIefkj2McNJcWEVDW8vElk3d2jAyWIk1HjyLPn6Fiuze7W_M168QO3EMXHJ_rF_JcAOow4_JLeLa1lrpVDMBQ9KF1RAmmcQEMRf2DjgLwpjJlQjsHKcqfDDgCEqQZKPuQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/dSUebb1V2CL7ls7qMYtu8h_rLjwJp1yCPD9AIpWf0-ooU4PxSRwQhgv5EgBF9p54TJTxf5azh58x7C-ZEto4ObG4lG5Zet2N-39MHN2-IbozUSPmDx5b8Kg0EqV2gS_B21T-sHobwm50CKqgfB9Z7kpQ86Ek0mRf6ZS7sbZE00WJfB34AyhqPZuyLc22BPlDuT-LD6trmjt6r0JGiauEXoadoREhrhf_vya7YTt5XORjRHNAbDlxdX_ouQyGD2GDWplB_7sSeC5UwOXlV4sBNzc1eiLA3lyRFd4Fokc0AQTBxJbCxNQrd44KP0bS1WffnXmwsrQBCoJ-HHJodXIzTQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/d4l3U3EYhmIkGuv1RXZGjYpHHNazrO4v4mShyrbqCChT-UPmYaqz7BLzN4ekvDPrgQXZU5Dqhocm9fUoxU1MTofxFi00Mbx8NmYfZYv1Cd5AZvxUCZ6tJlAlKJolW1j8BIq3Cv4tdW8dQLU6DSuCM24gSCv24hcnjhyMGH7SoDguzMadcSK5DNJ0-gqLG7b12BHm2Hg8LFhekh-cygoIUzqjYCV_H4Bk02QZ07I7QSyl8PRhT1tTSmQdKBXHBuEC-o_zDMtFhImE1D_4uz7o89vOQUrDQeYox7YjqEsExXHaKsOfuE8BOj8QFwvboEi--y47xWnVruR2X0tvq1lyMA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
افتتاح چهار پروژه مهم راهداری در جنوب سیستان و بلوچستان با حضور وزیر راه و شهرسازی
🔹
همزمان با سفر وزیر راه و شهرسازی به استان سیستان و بلوچستان، چهار پروژه شاخص راهداری جنوب این استان با هدف ارتقاء و تقویت زیرساخت‌های ارتباطی، بهبود کیفیت راه‌ها و اتصال مناطق روستایی در جنوب استان سیستان و بلوچستان به بهره‌برداری رسید.
🔹
در این آئین، پروژه‌های زیرسازی و آسفالت ۱۲۸ کیلومتر و بازگشایی ۱۲۴ کیلومتر راه روستایی، روکش آسفالت ۲۰۵ کیلومتر راه اصلی، فرعی و روستایی و احداث چهار دستگاه پل بزرگ با اعتبار بالغ بر ۴۰۰۰ میلیارد تومان به بهره‌برداری رسید.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/akhbarefori/692579" target="_blank">📅 12:42 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692571">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e8a5b9bfa1.mp4?token=RQURD87EECCyF0x1TmL2ftTehXxIUgGZWAt145ca7VRO1lG1Pc5sOiaWWj-ZfUgrd1LBzugEMUhoyI3EI7iVD_CKb1PBTF0CIU13KrQz3WZM07p_rJBfkA9VOgXKgkvWXxjonuk9SDGzI2kbepAbkzYYuEe8ee2wVaFNony1BkILTZm0fkc-CIW7iQGSBdTDZ8GUBi6oae8yCAodTeZ1ZyQFuyCKlj0glqsbf5qvA-iLN5giQXkPmw59bcA8ElW07i2HsPiy7RWHe7J54BEhoQ3JP2VlsRbd4XTIX4ogWasJNsEAYrXaXm1FZSMRJN9WZKZrutbBsDGb7UFlkXOfpw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e8a5b9bfa1.mp4?token=RQURD87EECCyF0x1TmL2ftTehXxIUgGZWAt145ca7VRO1lG1Pc5sOiaWWj-ZfUgrd1LBzugEMUhoyI3EI7iVD_CKb1PBTF0CIU13KrQz3WZM07p_rJBfkA9VOgXKgkvWXxjonuk9SDGzI2kbepAbkzYYuEe8ee2wVaFNony1BkILTZm0fkc-CIW7iQGSBdTDZ8GUBi6oae8yCAodTeZ1ZyQFuyCKlj0glqsbf5qvA-iLN5giQXkPmw59bcA8ElW07i2HsPiy7RWHe7J54BEhoQ3JP2VlsRbd4XTIX4ogWasJNsEAYrXaXm1FZSMRJN9WZKZrutbBsDGb7UFlkXOfpw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
طالبان و پاکستان درگیر شدند
🔹
روزنامۀ ۸صبح افغانستان از درگیری طالبان و نیروهای پاکستانی در مرز دو کشور در ولایت پکتیا خبر داد.
🔹
این درگیری چند ساعته ادامه داشت و به‌گفتۀ منابع، شماری از گلوله‌های خمپاره به خانه‌های مردم اصابت کرده است.
🇮🇷
✊
@AkhbareFori…</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/akhbarefori/692571" target="_blank">📅 12:19 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692570">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c09492e061.mp4?token=i2n4voteqe_FusjW1H6oiEkgV-LOEyhoWavOOHdXyUPR3Oe2IXC_fFi2iLtUC4R0T7YeufSpOhq-sRy4WO8itgY5dezDFPoAsO0j82erUtD2RoMWcKiN-GsiAzawO178mHuOMuW5cQgDbF8EltnIhyTwErlyxq5KChdPMu1mV6q7k8DUusU0J1lqwTJTCjCseIKqt_UjwgsLE6_Wq-xcOonuCdrKcW76LplOKG0EbP4dV2JR23VFEuWXL5ruyIf4x7FIVcwj03hw85HWUuQoD23eFaV6w1nZEFx4YURCZ55pGjRlsNYse2jy91TrHj7rDlDnDOHxuyvl50XATcJN3A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c09492e061.mp4?token=i2n4voteqe_FusjW1H6oiEkgV-LOEyhoWavOOHdXyUPR3Oe2IXC_fFi2iLtUC4R0T7YeufSpOhq-sRy4WO8itgY5dezDFPoAsO0j82erUtD2RoMWcKiN-GsiAzawO178mHuOMuW5cQgDbF8EltnIhyTwErlyxq5KChdPMu1mV6q7k8DUusU0J1lqwTJTCjCseIKqt_UjwgsLE6_Wq-xcOonuCdrKcW76LplOKG0EbP4dV2JR23VFEuWXL5ruyIf4x7FIVcwj03hw85HWUuQoD23eFaV6w1nZEFx4YURCZ55pGjRlsNYse2jy91TrHj7rDlDnDOHxuyvl50XATcJN3A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
صحنه‌ای جالب از تردد گله گوسفندان در یک بزرگراه در یکی از شهرهای ایران
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/akhbarefori/692570" target="_blank">📅 12:17 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692569">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/A-4sR2wqPVYcASUoE9dy6Jle_tqYRI2xZ9TW_1w-z7vRlqe73B5d2Daj9DOtWF3KcT10sE8rcmJ5D5ZMkdWmDQp8S0MBs366YY4xT8yUtNASZc1IWiuQQaYC3x2Xs9wiMXQIT8eKPEfTUn8bMvnHLJSIdx8AIktDGcn0tAe3w0g6EDMsu8w17Gr3DXUYra9cpULqlnM_X30gFOFPlPw0a2poxsBLEUf5EJfdc7szNnZbjrik0PYT5p2yZaUkYBq9YjOFV7HHAlBEAvkdZ0EdjP9EujuLUh83L_KOPu1tRWDf7mukrobRcr0hYVUwkCIHRcPyi3hTQiBR3w9UgbcoqA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
قیمت نفت برنت از ۱۰۵ دلار عبور کرد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/akhbarefori/692569" target="_blank">📅 12:07 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692564">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/p51x1wDJ-NxwVzeN3F_nimt030vpwcj77VYbiDriXNXSZY3J-b9Lg79RcMpvTXvxyxe3yVt9bRNunKiDzXP2zDS3UwY524akQ3KJ2KJU4VRgAcOWnU9mJ8YITm3vLA5B8C3W9HhuGOWTh5gi9WFT_MwO9d5vWizSrY1To_nQfW0osJzBE2Xthrp38CVCSBsIU0LkyDKicRHatDZGhbfzAfAi-WZDz_9Uiwqz89Ojkxhx--XBaysA4qJYYRYkeW_V73N2D2m2Y4AhZ2GpqKHnAK0JWNjo3RJ_CQjR5mLrfVtu3ERClDe5mxJvK2PLFGVDux68VZk0TSsTzKrqKDQkcw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
چاه مکن بهر کسی، اول خودت دوم کسی
🔹
در جریان استقبال ترامپ از همتای چینی در فرودگاه، واکنش رئیس‌جمهور آمریکا به صدای شدید پرواز یک جنگنده حین پخش سرود ملی خبرساز شد.
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/akhbarefori/692564" target="_blank">📅 12:01 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692562">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/47e00a628a.mp4?token=DsX6-1HhqMNQb1PrO1HaP0wOxZlYgiT7W9jKMReveTNNJEV90y10LYyczazbinHiDQPSEK07ajVZB79iDueFHXBYhCX1iNYqa8sb4D-0HUpEOesDaFlLu2vOWtEjtvUEtGXr-8lyEP6A6Tw49uxYZyxnkitgfB2V-ft0nibEf1hwAv5QoOYLUMmkKIrZAkqiwxSEdR_EEM7Ad_KrkUU486T5y1d7VsfgmsOfpBfFqzYebJSKwRPFAbRyZNGDDaLc8h-IG_Y5_hkXoTYbmO_BGNwR51SpJYb3pqZPTkIDqcw0dxo5-JA4W943x4Ogt48pLk9s5JG-rlmWjh3vGv4TYQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/47e00a628a.mp4?token=DsX6-1HhqMNQb1PrO1HaP0wOxZlYgiT7W9jKMReveTNNJEV90y10LYyczazbinHiDQPSEK07ajVZB79iDueFHXBYhCX1iNYqa8sb4D-0HUpEOesDaFlLu2vOWtEjtvUEtGXr-8lyEP6A6Tw49uxYZyxnkitgfB2V-ft0nibEf1hwAv5QoOYLUMmkKIrZAkqiwxSEdR_EEM7Ad_KrkUU486T5y1d7VsfgmsOfpBfFqzYebJSKwRPFAbRyZNGDDaLc8h-IG_Y5_hkXoTYbmO_BGNwR51SpJYb3pqZPTkIDqcw0dxo5-JA4W943x4Ogt48pLk9s5JG-rlmWjh3vGv4TYQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
اگر به هر دلیلی با همسرتون بحث کردید، حق ندارید پای خانواده و ترومای‌ کودکیش رو وسط بکشید #سلامت_روان
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/akhbarefori/692562" target="_blank">📅 12:00 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692558">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/43db64b5a4.mp4?token=LtSx-h8n1TO7sNjUg1DL2H5bGX41mNPdmQUcsw5nLrLQ1evLvXQRDU1UaRpm-2O0lDyXWfDrlACCTgXurVMNbUfPvcR97y0l28qU8RKsVx3JRvnQG7XwEKBb41aM3cgmITY4N3ZCZJwotqBSLxSFBm2GTUy2QMl8Sru4cbPOZ9asi3lvQE195wrve9yfZrYZwIpDzAypSJED5vSJgt40LUtEfl2Qj8iDi1feU6mO-x-wCjjmdhkKo1p_VcucrJ63bksZ3bxAzZkDrA5RS0HgyeF_n-d0RYhUX_EEcbMHcM0tNOXHPpHCGGfwYqY7dI-AufLUzAoP0iw4NoLcg7qFH3-2ozAwSDgsGW2R2Q6nW2F2UyAjPtHopKMiSDyGqVT6rOT_t0qZ0PDhAM6TpfhuKf-EuzYR8fptgVNP4-pMsxZ4vehgGkMBcFRFlTIy5ad7iL7aotYpFr3OKOgcfDl3YRA3W2TTJZP_Ot4ya5pXXFXW_ZZBIEUD3YQC-vvLwzLwNqqRIpX0qgfBANjuDNau94XrJ80_8_AydSvTqg35lvwrjIKOD9KrxiuxSUTmhJqk_rXZ1hIcbGSkQ2p1W4SPFAlfR-boxLqd1xzJpfbQufRd1zJO6QNGO2WkrHeDkvTPTijZGeI3xAHqBQArX6-V5uwVaQFQ1j3WCYt8mOu0QYE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/43db64b5a4.mp4?token=LtSx-h8n1TO7sNjUg1DL2H5bGX41mNPdmQUcsw5nLrLQ1evLvXQRDU1UaRpm-2O0lDyXWfDrlACCTgXurVMNbUfPvcR97y0l28qU8RKsVx3JRvnQG7XwEKBb41aM3cgmITY4N3ZCZJwotqBSLxSFBm2GTUy2QMl8Sru4cbPOZ9asi3lvQE195wrve9yfZrYZwIpDzAypSJED5vSJgt40LUtEfl2Qj8iDi1feU6mO-x-wCjjmdhkKo1p_VcucrJ63bksZ3bxAzZkDrA5RS0HgyeF_n-d0RYhUX_EEcbMHcM0tNOXHPpHCGGfwYqY7dI-AufLUzAoP0iw4NoLcg7qFH3-2ozAwSDgsGW2R2Q6nW2F2UyAjPtHopKMiSDyGqVT6rOT_t0qZ0PDhAM6TpfhuKf-EuzYR8fptgVNP4-pMsxZ4vehgGkMBcFRFlTIy5ad7iL7aotYpFr3OKOgcfDl3YRA3W2TTJZP_Ot4ya5pXXFXW_ZZBIEUD3YQC-vvLwzLwNqqRIpX0qgfBANjuDNau94XrJ80_8_AydSvTqg35lvwrjIKOD9KrxiuxSUTmhJqk_rXZ1hIcbGSkQ2p1W4SPFAlfR-boxLqd1xzJpfbQufRd1zJO6QNGO2WkrHeDkvTPTijZGeI3xAHqBQArX6-V5uwVaQFQ1j3WCYt8mOu0QYE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
پروازهای ایران-تاجیکستان لغو شد؟
🔹
«پرواز هواپیمایی وارش» از تهران به «شهر دوشنبه»؛ پایتخت تاجیکستان؛ از مرزِ هوایی لغو شد و به فرودگاه امام خمینی بازگشت.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/akhbarefori/692558" target="_blank">📅 11:56 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692557">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/21ef4b9caf.mp4?token=BRaA9-z1lMZIRXFVUG-YO75jEX5AMfNII0RGB3fQwBLO18rbAdhvUvWzqj_4x1M4afdPchmD2Pme3JQ41-78A4bZSQjDwT2LcVE9yS4QV4AUaZ0lQ8q2ew2BniVhiH7JOj6j1rkBfkI77nMYFGH7BkulqGwqigALGE5WK7h-ZMWd7lGH2DoociUF2uf_lwvO92Kd9G2P6EMgCvgd74cWT_F4VKcxMlrcGfse2kW2Pj4pJrgOUJ5MKYUUegrc26tCQmIcaAapGYNwCmbDo4V0hloAa6ufDnSSJ_wIX_3LqTROgkD7aDbMZpTetrzm6LY_wasU9uJSTrk-6rwpHXBveQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/21ef4b9caf.mp4?token=BRaA9-z1lMZIRXFVUG-YO75jEX5AMfNII0RGB3fQwBLO18rbAdhvUvWzqj_4x1M4afdPchmD2Pme3JQ41-78A4bZSQjDwT2LcVE9yS4QV4AUaZ0lQ8q2ew2BniVhiH7JOj6j1rkBfkI77nMYFGH7BkulqGwqigALGE5WK7h-ZMWd7lGH2DoociUF2uf_lwvO92Kd9G2P6EMgCvgd74cWT_F4VKcxMlrcGfse2kW2Pj4pJrgOUJ5MKYUUegrc26tCQmIcaAapGYNwCmbDo4V0hloAa6ufDnSSJ_wIX_3LqTROgkD7aDbMZpTetrzm6LY_wasU9uJSTrk-6rwpHXBveQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
دندان‌های عقل چرا باید کشیده شوند؟
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/akhbarefori/692557" target="_blank">📅 11:51 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692556">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oNcWfqyTqLL-qMo1_P2IikeRJ7VZG8kxeGSZanYE5mKtrxpTjOCRekUmBTaL8XHuCVKNCLnl9NVnh_8hgDSl5mTGQMyLE3EaP9aRiCCrGbxcU1E9m4XUWGrw0GsDNz07JX_tswZpce9_46Ut73xtB1xbAAotElSr4DLILU5l4drU2Cdpf1-8QCt3d0LuoZIhjD7lwrNtQi5fIt6mdEL7k_VCcBdANVP9NqhgsMfMtzPXIn1vULG8kRspm9WaxxNSiCHWaqAuuMYwkcGWaL_rgrnQKJTj99cAC5nTxRU2OUXKAcqnDq7NP7lPUhSQWQVZawgkzgqiTQ66A94ul0D6kA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
سرپرست وزارت دفاع: پیام ایران از تریبون سازمان ملل روشن بود: دکترین دفاعی ایران تغییر کرده است
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/akhbarefori/692556" target="_blank">📅 11:46 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692555">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">♦️
آکسیوس: مذاکرات ایران و آمریکا در نیویورک غیرمستقیم بود
🔹
آکسیوس گزارش داد مقام‌های ایران و آمریکا در حاشیه مجمع عمومی سازمان ملل، حدود سه ساعت از طریق میانجی‌ها مذاکره کردند.
🔹
همزمان، یک مقام ارشد ایرانی به رویترز گفت تهران در صورت کاهش فشار نظامی آمریکا و رفع محاصره بنادر ایران، می‌تواند تنگه هرمز را ظرف یک هفته بازگشایی کند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/akhbarefori/692555" target="_blank">📅 11:40 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692554">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/51f8034866.mp4?token=WLgEcJTp0jArIMC2iRNlk4FgDFm4TzeaaOuqLQz5lI7s01GdjgRo6g_uUjkhsHKQd4xzHzUUcAv4gpCXHh8Q8sCpjjWPmnYj99ai3JkRIFT0T5ICtThVKRmBpoJscGthfJIFCrmzHXoC6xIRnmHHhqOjlue2swb9Zfdg4buI3TlN1juodWD1C7M18X-14w95oAGFJaAb-0pN03I8x0T0peYZblBqnQXeCAcKtts8GrlvXygjjTfCclsmPoddA9ehhbJQKRFLKlZKONVCPu_y5gPDLSzjJsGG_NQ8hFdr6TnuLSUf2rlcbY096EKhfxBih68ZEDFzvmZKQ3OJUHnqBg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/51f8034866.mp4?token=WLgEcJTp0jArIMC2iRNlk4FgDFm4TzeaaOuqLQz5lI7s01GdjgRo6g_uUjkhsHKQd4xzHzUUcAv4gpCXHh8Q8sCpjjWPmnYj99ai3JkRIFT0T5ICtThVKRmBpoJscGthfJIFCrmzHXoC6xIRnmHHhqOjlue2swb9Zfdg4buI3TlN1juodWD1C7M18X-14w95oAGFJaAb-0pN03I8x0T0peYZblBqnQXeCAcKtts8GrlvXygjjTfCclsmPoddA9ehhbJQKRFLKlZKONVCPu_y5gPDLSzjJsGG_NQ8hFdr6TnuLSUf2rlcbY096EKhfxBih68ZEDFzvmZKQ3OJUHnqBg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
حرف‌های تلخ شهرام قائدی: وظیفه بازیگر حضور در یک شو و ملق زدن نیست؛ ما مجبور می‌شویم
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 29K · <a href="https://t.me/akhbarefori/692554" target="_blank">📅 11:35 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692553">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2dbea335ba.mp4?token=Zt1idZeBVh8Bw4S7lM3UJMwnJK7EiqxIrw64BIEKssrV2ls17cnD0PRv_cDYg8vkuEYuyzYn6RMI1dHvLC_5_KtX0tEpn9cdai0oUSYEAgEziKzvxVql4tFdDOZPO7VqIgsDc7NlLjGTbmScAU8e8akIA4uLcvdi-sh6CVnpmX_a0h9bi5Wimn9pSY6S0a9w9wQ66rMVY17se9vu63-G39NItVEyZOmQ3vTkeklDwXjQj63mK0oH6XWpHyXmfbNfLeCgMp6Xumo5zpdNaKq8XnYxZkUu0LJs3cuDZNzL69Q4MHkLSNulQmBGmqQ53sQFVPlgSoLcmJcW9_aotRbYHqmR3uMj8Bw75sLtgcBhKHpBjTSD5B-wOWPxYUyMfxGqoeWoxXIHy4ZcaNJJRT1liaDZ_1O8ozKt_jmrvuwC3OImASEODdepf4e0S5Z_8HFxJTPL9DPg0-W4OP41uNn3yjyhVqNFIx6pS0xfKcLzlNLpKtLwo-4u95h_kZCXR5KNf7UF3XnyJq8LboAxMli5kyc3wvuW8BmQC5qXRN8FB24H782I1piil6WaqTstVNWCT1Z_GQmmtNK1cbj9fe7d5Rkm7XwaeA-Rdm4jT3Z7UJP9oUhxlyn8RjHfQI38cAavGshDnLoohCWE3qJKWhA3k8wuEdotoAJdpyAbH7HZCdg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2dbea335ba.mp4?token=Zt1idZeBVh8Bw4S7lM3UJMwnJK7EiqxIrw64BIEKssrV2ls17cnD0PRv_cDYg8vkuEYuyzYn6RMI1dHvLC_5_KtX0tEpn9cdai0oUSYEAgEziKzvxVql4tFdDOZPO7VqIgsDc7NlLjGTbmScAU8e8akIA4uLcvdi-sh6CVnpmX_a0h9bi5Wimn9pSY6S0a9w9wQ66rMVY17se9vu63-G39NItVEyZOmQ3vTkeklDwXjQj63mK0oH6XWpHyXmfbNfLeCgMp6Xumo5zpdNaKq8XnYxZkUu0LJs3cuDZNzL69Q4MHkLSNulQmBGmqQ53sQFVPlgSoLcmJcW9_aotRbYHqmR3uMj8Bw75sLtgcBhKHpBjTSD5B-wOWPxYUyMfxGqoeWoxXIHy4ZcaNJJRT1liaDZ_1O8ozKt_jmrvuwC3OImASEODdepf4e0S5Z_8HFxJTPL9DPg0-W4OP41uNn3yjyhVqNFIx6pS0xfKcLzlNLpKtLwo-4u95h_kZCXR5KNf7UF3XnyJq8LboAxMli5kyc3wvuW8BmQC5qXRN8FB24H782I1piil6WaqTstVNWCT1Z_GQmmtNK1cbj9fe7d5Rkm7XwaeA-Rdm4jT3Z7UJP9oUhxlyn8RjHfQI38cAavGshDnLoohCWE3qJKWhA3k8wuEdotoAJdpyAbH7HZCdg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
‌
عصبانیت رسانه‌های فارسی‌زبان خارج نشین از سخنرانی پزشکیان در سازمان ملل
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 28.7K · <a href="https://t.me/akhbarefori/692553" target="_blank">📅 11:32 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692552">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aJFWyZpr0kVB2VH7kh1Jn-NdgDEJMdOn-HyIeYvcFlLz7Fkk5NJckVfxtGEzeM-RozcS1zj25psFxeSiBSbtXEHgNuW9ZQCtedKx4wCUoodwsHEUcbRUrydobuQ5IpeOohR7IRBNVP0ltqGSzBT2GkVexfNMNV6_WGNrLOSBv98BRv4CHZ09JtB-UEBQU8bjGdo0mdBbpI6KIe0MXKOWAk6xLnx6pNr_M0cR5JTh0sAXhmyTtQyb4NQ4oMLYDHVN0xjSkguf0xzvhOkDLqj6IF199m1Kn7kVOtYYyFK1d75yAHFFa2SOH7PsFPQe4nl9w9wrDm7Wvu-BmOXPyEwACQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚠️
هشدار: مراقب کلاهبرداران رمرارز در دنیای مجازی باشید!
🔹
رایج‌ترین کلاهبرداری‌های دنیای رمزارز را بشناسید تا طعمه شیادان نشوید.
🎥
برای مشاهده ویدئوی آموزشی و دسترسی به محتوای کامل، وارد
«مدار»
شوید:
https://t.me/+0AFRVmShGBMzNDc0
https://t.me/+0AFRVmShGBMzNDc0</div>
<div class="tg-footer">👁️ 30K · <a href="https://t.me/akhbarefori/692552" target="_blank">📅 11:30 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692551">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CQmhNrP3XiueMX-4KUaShk-QbAyby2LzafDriDOYykRqpsnO7TrU-Fdp4usRuTKGzF341LrQIQKHdVGv3jg4CvOdeMJVCT8gHG-MVl-4EdUjEJRK_hYFfvNBLCWGetALwvG9qs4sVfLfqZ7pH5ZwbluwI12W2he3efJyX2LOcMcNU5ChLmXdd0WvaHA7XmUfajnlnlzUFmlE7T20hldvhooeaGkZ4-RxWnslfw9s6DDGKWsfLEUqfXs8YsmHmYH5rVYR-5ITPVId7IljTnRcp7X9jaJRJx4WYn1Po5mPPF9b-czhRJtIlCtH-yq1JnXdSRGMyRxXUwqWa3Mv-EqdAg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
پاسخ ظریف به توهین‌های ترامپ علیه ایران و تمجید از صحبت‌های پزشکیان
🔹
«قلدر کل» اجلاس مجمع عمومی ملل متحد را با میدان جنگ عصر حجر اشتباه گرفت و تهدید کرد که مادر همه جنایات جنگی را با «نابود کردن» یک ملت مرتکب خواهد شد.
🔹
پزشکیان در پاسخ، سخنرانی از پیش آماده‌شده‌اش را کنار گذاشت تا به جهان بگوید: ایران همیشه آماده دیپلماسی است اما هرگز ایرانی‌ها را تهدید نکن.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 29K · <a href="https://t.me/akhbarefori/692551" target="_blank">📅 11:26 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692550">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">♦️
ترامپ و نتانیاهو دیدار نمی‌کنند
🔹
تحلیلگران، علت این موضوع را نگرانی ترامپ از کاهش محبوبیت و ریزش آرای جمهوری‌خواهان عنوان کرده‌اند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/akhbarefori/692550" target="_blank">📅 11:24 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692549">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromالو فوری</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/t0bfPIR0dYmtahh4hWIo5NGsKjjoLmKWLsYrH-zXhOW-V_HvO675O73KuiHgwDFbma9L8ZdmGSRc8KBxqz-ff2EtXq7cR2MYkT5UL841WT1OOHqdx95kqdnuAKF4TNbM05IxW40PlqIyeOtdDHl80eMDLrRGnJZdjevtH2BobpuPMQpyPH9rXx9sY_48vaoV_lUS3TfoUYBklXmSRUOy7OkYDcabdgcig1McEd3Bw_Tr_63xZLoQSarGYRgUAb963S-fUguJaZJ606KSsp0MU3mZy_NY2Yt6hdsH32y-D1V8ukQFYJ-6nWqIPA_p5ZegtSQjZPHg2Br0ITYmED28hQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
فراخوان خبرفوری | جشن فرشتگان
🔹
همراهان گرامی خبرفوری، شما می‌توانید با ضبط یک ویدیوی کوتاه از دانش‌آموزان خود با لباس فرم مدرسه، در این پویش شرکت کنید .
🔸
از کودکان خود بخواهید این جمله را بیان کنند: «کودکان شهید میناب؛ ما راهتان را ادامه می‌دهیم.»
🔸
ویدئو های خود را به آیدی زیر ارسال کنید
👇
#جشن_فرشتگان
@Ertebat_baforii
@Alo_fori</div>
<div class="tg-footer">👁️ 4.68K · <a href="https://t.me/akhbarefori/692549" target="_blank">📅 11:20 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692548">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">چله علم النور 4_ جلسه چهارم</div>
  <div class="tg-doc-extra">علی مقدم</div>
</div>
<a href="https://t.me/akhbarefori/692548" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">♦️
جلسه چهارم؛ جایگاه حقیقی
🔹
انسان باید از خداوند درخواست کند که او را در مدار «حق الهی» که آمیخته با رحمت و فضل پروردگار است، قرار دهد.
🔹
کسی که در نام
«الْحَقّ»
پروردگار قرار دارد، از لرزش و تردید آزاد است و تحت حمایت الهی قرار می‌گیرد.
🔹
انسان باید بیش از هر سخن یا تصمیمی، نام «الْحَقّ» را بر زبان آورد تا نیت و گفتار او از باطل و لجاجت پاک شود.
🔹
در دورانی که تشخیص درست از نادرست دشوار است، تمسک به نام مبارک الْحَقّ باعث شفافیت بصیرت و تشخیص منجی از دجال می‌شود.
🔹
بزرگترین خطر برای فرد حق‌جو، گرفتار شدن در «غرورِ حق‌جانبی» است.
🔹
مسیر حق روشن و بدون ابهام است؛ در حالی که باطل همیشه با دودلی و وسواس همراه است.
🔹
اگر انسان باور داشته باشد که مسیر زندگی‌اش تحت نظارت نام مبارک الشَّهید و بر مدار الْحَقّ است، حتی سختی‌ها را بخشی از فرآیند رسیدن به جایگاه درست خود می‌بیند.
#مدیتیشن
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/akhbarefori/692548" target="_blank">📅 11:06 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692547">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">♦️
آغاز دومین مرحله پرداخت وام فوری ۱۵۰ میلیونی بازنشستگان کشور
🔹
دومین مرحله پرداخت وام فوری ۱۵۰ میلیون تومانی ویژه بازنشستگان و مستمری‌بگیران تأمین اجتماعی آغاز شد.
🔹
بر اساس دستورالعمل اعلامی، این تسهیلات بدون نیاز به ارائه چک یا ضامن ،بازپرداخت یک‌ساله و اعتبار آن در کمتر از یک‌روز کاری پرداخت می‌شود.
🔹
فرآیند ثبت درخواست و ارائه مدارک به‌صورت غیرحضوری انجام شده و متقاضیان برای ثبت درخواست نیازی به مراجعه به بانک ندارند.
🔹
جهت اطلاع از شرایط و ثبت درخواست، با کارشناسان از طریق شماره 02191551808 در ارتباط باشید.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/akhbarefori/692547" target="_blank">📅 11:03 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692546">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0685d6b2b5.mp4?token=WOV0lo2cKHEsPpXhN2KN8Z7redlS_dkWRoYuH2faCmkSt6x7PNC7IUXReF1nNAVMbxIwimoP0Oqvf6b3N4Xyu7Whc5klYb9yWvEaA2UE4Vmso8G1PnCWza8QmHzPyrx5dRqZEI9__Wl2gFI5bzE-iypwyJTrkMkdmsLwX2_m7CSmjUvETErVXyNQ7EKI-CMYrTxnqZ-moRfddFYkWmIB9OQqHDzClPO3LhhTDOIs66Xqd9Jb2NNvno30wVsLNp4VdJIX4hTKX2Z6DV-XAqjEAX5gDqY9GowCw6F_B0m6X93xkKpoCXfZ4e2N2xhbx5kKDQrHD6dlYIWlYxXr8JDTEpbV3XwuRaDdQ39ql49_Bj6iDLwBNQfUr_ohYX1woZ6NozgnIaTeQ5jods5rh5u9WaWYhmGwN6i5N2Wcf5D5VFaAqOoWtRKxI-ciG1AR193VyrC7PXXPfx7Gz3ZVqJhV-UPPuMuJpzDBLQWQeZHmjnBquECOQYDoKj2c-n5D5-T2CAB-EDnuNMwm8Mg-5XrTj3KBu1r38D_Nkj_ALVHr72v-xDkwrSRHtqLftBgwavpLSjVyBXq0rH_oeeFDg2PAND03nLPOLSmwN9Ey-USGCQa_QURsTpYCjI_UjtmyQBHv2QYvLOs76etOnMNmmov9qvxpLXOsC1ta5BWya6lpnRg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0685d6b2b5.mp4?token=WOV0lo2cKHEsPpXhN2KN8Z7redlS_dkWRoYuH2faCmkSt6x7PNC7IUXReF1nNAVMbxIwimoP0Oqvf6b3N4Xyu7Whc5klYb9yWvEaA2UE4Vmso8G1PnCWza8QmHzPyrx5dRqZEI9__Wl2gFI5bzE-iypwyJTrkMkdmsLwX2_m7CSmjUvETErVXyNQ7EKI-CMYrTxnqZ-moRfddFYkWmIB9OQqHDzClPO3LhhTDOIs66Xqd9Jb2NNvno30wVsLNp4VdJIX4hTKX2Z6DV-XAqjEAX5gDqY9GowCw6F_B0m6X93xkKpoCXfZ4e2N2xhbx5kKDQrHD6dlYIWlYxXr8JDTEpbV3XwuRaDdQ39ql49_Bj6iDLwBNQfUr_ohYX1woZ6NozgnIaTeQ5jods5rh5u9WaWYhmGwN6i5N2Wcf5D5VFaAqOoWtRKxI-ciG1AR193VyrC7PXXPfx7Gz3ZVqJhV-UPPuMuJpzDBLQWQeZHmjnBquECOQYDoKj2c-n5D5-T2CAB-EDnuNMwm8Mg-5XrTj3KBu1r38D_Nkj_ALVHr72v-xDkwrSRHtqLftBgwavpLSjVyBXq0rH_oeeFDg2PAND03nLPOLSmwN9Ey-USGCQa_QURsTpYCjI_UjtmyQBHv2QYvLOs76etOnMNmmov9qvxpLXOsC1ta5BWya6lpnRg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
چرا با آبیاری قطره‌ای دشت‌ها خشک‌تر شدند؟
کامران داوری، پژوهشگر محيط زيست:
🔹
در برنامه سوم توسعه گفتند راندمان آبیاری را ۲۵درصد بالا ببرید تا مصرف آب کم شود؛ با عجله آبیاری تحت‌فشار آوردند، اما غافل از اینکه راندمان بالا یعنی کاهش نفوذ آب به عمق زمین و توسعه سطح زیرکشت؛ راندمان بالا رفت، اما مصرف آبخوان‌ها بیشتر شد!/ تلویزیون اینترنتی مدار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/akhbarefori/692546" target="_blank">📅 11:00 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692544">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/fheSDogYwddIHlAFMFxJF9Z5IwtintLvhJy84GhSsywJBZjly6yWapJJRMdVICPvb8AVWQt3W6zluZURVxla8WVrogb0_LtQ9jrcphIKlDW43d-QgrTT8w7QRmHxLd2gYIB1vpD80U7ixnqagmxovK5Evz7r18SMngPjAOOUJ77geXRaW-WIbA8a_Af3ZnOljM_YRRGw1nAdjur4CB1EhNzjn98vfgnttws4jxe_E3TkiGu20CkPq3uHlyjLupPoD_a_XB0THGr4GYBeAi261R4zMS7pfUds2NbTiaV_sEwRUXyVG0KsodAMA62KyOEaLaWW19DGoTxpvRoN1wSImA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jE9IGTBZSXYvWAGRCQPlDObB_N6bP83WnxIwo_1WZVDCRn6ZGImPQIPMOIzcta-0upbGQHIOLUCXo00iWdCqi_7Ne4LD6pDUc5kvzOnZQQAd1rcVqbksXb_MO8B7FkMme2Ugr56RbiMTsJgY9pFA3rOQUcMtBWw8lvUxdL7jysL3zRNJTbECibePleJ1ZomL6QBTvvroSVPpGOfJFK7tjXr0L9vDtaEm-vNKpd6Oo8mf6SeAM4ZAJgBLNpViZ60WQ61qUZ55AWNXwnoFCtY2BNkjuDZ_Xcl144yuoA6tB5GQiQ8Zt4vatT0AyBiNJe0zA8X8bzRJoSRNqAZ7-TAsqA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
مشاهده افراد مشکوک نزدیک محل اقامت نتانیاهو در نیویورک
🔹
پلیس نیویورک از مشاهده سه مرد ناشناس خبر داد که بامداد امروز از یک چاه فاضلاب در نزدیکی هتلی که نتانیاهو قرار است در آن اقامت داشته باشد، خارج شدند.
🔹
این افراد با دو خودرو از محل گریختند و پلیس اعلام کرد به‌دلیل حساسیت محل و برگزاری مجمع عمومی سازمان ملل، بررسی‌های امنیتی بیشتری با همکاری نهادهای فدرال در حال انجام است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 29.6K · <a href="https://t.me/akhbarefori/692544" target="_blank">📅 10:54 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692543">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">♦️
اسقاط ناوگان فرسوده در ۳ کلانشهر در اولویت قرار گرفت
🔹
تهران، مشهد و اصفهان در اولویت نوسازی ناوگان فرسوده قرار گرفتند؛ موتورسیکلت‌های فرسوده و تاکسی‌ها در اولویت هستند.
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 30.6K · <a href="https://t.me/akhbarefori/692543" target="_blank">📅 10:46 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692542">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">♦️
معاون درمان وزیر بهداشت: افزایش تعرفه‌ها در بیمارستان‌های دولتی منتفی شد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 31.9K · <a href="https://t.me/akhbarefori/692542" target="_blank">📅 10:40 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692541">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">♦️
طلای جهانی از رشد بیشتر بازماند
🔹
قیمت طلای جهانی در معاملات پنجشنبه تغییر چندانی نداشت؛ هر اونس طلای نقدی با اندکی تغییر ۴۲۹۱ دلار و ۴۸ سنت معامله شد و طلای آتی آمریکا نیز با ۰.۲ درصد افزایش به ۴۳۲۶ دلار و ۳۰ سنت رسید.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 31.9K · <a href="https://t.me/akhbarefori/692541" target="_blank">📅 10:38 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692539">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XBDVQhB5HJofOVwEaJ_CIjsrWQjuPgJ4fvhX_rV5xPb2ZvfQiBUs85eYm5Y_wfbD_XUk7saDcWP9jMn_9BWa7KQ6HlrPzUSHmVKy9pUoPHJjeZrmNjPGZZuSVM2pxl9EP6Aiwg489oLdv7DWRkWKFnVpNojV7s93X1QFUKdSGpxHaJHaGZTAIJk7Ntp2y78k0EZWI62ItOECYEIwigNWpT9nH4DVcYuNAmJ_5il8SA07jHZ7oNUs9X4AApLaw3p9eTohyB4-Cf412a3b5yWBIeEMfOiqqHVEIleWky73aZRiq3qjxcVrIl9kIQwRbIfp_aeOMO4oj7ls_jCbjQGBHw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
آمریکا ۶ میلیون بشکه نفت ایران را دزدید
تانکرترکرز:
🔹
نزدیک به ۶ میلیون بشکه نفت خام ایران به ارزش ۶۰۰ میلیون دلار که پیش‌تر توقیف شده بود، به‌صورت بی‌سروصدا در حال عبور از اقیانوس اطلس به مقصد آمریکا است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 35.3K · <a href="https://t.me/akhbarefori/692539" target="_blank">📅 10:07 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692538">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">♦️
با اين مرینیت مرغ، حتی اگر هر روز هم مرغ بخوری ازش خسته نمی‌شی
😋
مواد لازم:
🔹
ماست یونانی ۶ قاشق
🔹
سرکه بالزامیک ۳ قاشق
🔹
روغن زیتون ۵ قاشق
🔹
رب گوجه ۲ قاشق
🔹
سیر ۴ حبه
🔹
نمک و فلفل‌سیاه
🔹
پول بیبر و فلفل قرمز
🔹
پودر سیر و رزماری
🔹
ادویه‌کاری زردچوبه
🔹
تخم گشنیز…</div>
<div class="tg-footer">👁️ 36.2K · <a href="https://t.me/akhbarefori/692538" target="_blank">📅 10:00 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692536">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7c04b0043c.mp4?token=NJd28weoARVj7Y2LeKfMOgzGkGdN-WM0XOnTtmrPitoE0Lq_ikZUe01wqL-TSPSeiLg-jVbBs8WmBE6npXMmHomo9TI-4fY5t1smC265TaOKG110HawMLJKoXIjVOtYpmuzBdiUqInPi-RmTQYgrB5L6h5KD1VeY8DWPz80DKImGHpzOqAWeEhh_GIT-xbcOXKIXtDiucx7uDFY7epsAbJQGm4gYiCiMQXkE2urTZHF6esaIOdfz86Zr9FAbwRrsu0JptVxeWoQ-QOr2IgpDHg_CEsSHcLaOk9h-rBr82VCHKRySLu4YqNKf69QztabgYkQShc3Jm_CCNOeI7mvYSg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7c04b0043c.mp4?token=NJd28weoARVj7Y2LeKfMOgzGkGdN-WM0XOnTtmrPitoE0Lq_ikZUe01wqL-TSPSeiLg-jVbBs8WmBE6npXMmHomo9TI-4fY5t1smC265TaOKG110HawMLJKoXIjVOtYpmuzBdiUqInPi-RmTQYgrB5L6h5KD1VeY8DWPz80DKImGHpzOqAWeEhh_GIT-xbcOXKIXtDiucx7uDFY7epsAbJQGm4gYiCiMQXkE2urTZHF6esaIOdfz86Zr9FAbwRrsu0JptVxeWoQ-QOr2IgpDHg_CEsSHcLaOk9h-rBr82VCHKRySLu4YqNKf69QztabgYkQShc3Jm_CCNOeI7mvYSg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
متا از عینک واقعیت مجازی جدیدش رونمایی کرد
🥽
🔹
متا از Meta VR Glasses رونمایی کرد؛ عینک واقعیت مجازی حدود ۱۰۰ گرمی که برای تماشای فیلم، سرگرمی و ارتباطات طراحی شده و به نمایشگر 5K با پشتیبانی از Dolby Vision و صدای Dolby Atmos مجهز است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 35.2K · <a href="https://t.me/akhbarefori/692536" target="_blank">📅 09:53 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692535">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">♦️
صدای شنیده شده در آبادان به دلیل نقص فنی در پالایشگاه بوده و در حال برطرف شدن است/ صداوسیما
#اخبار_خوزستان
در فضای مجازی
👇
@akhbar_Khozestan</div>
<div class="tg-footer">👁️ 37.5K · <a href="https://t.me/akhbarefori/692535" target="_blank">📅 09:39 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692534">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">♦️
حقوق کارگران چند روز کفاف زندگی را می‌دهد؟
رئیس اتحادیه پیشکسوتان جامعه کارگری:
🔹
افزایش دستمزد ابتدای سال تنها حدود ۲۳ روز پاسخگوی نیازهای کارگران بود، اما اکنون این میزان به کمتر از ۱۰ روز رسیده، بنابراین موضوع بازنگری در دستمزد کارگران ضروری به نظر می‌رسد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 38.5K · <a href="https://t.me/akhbarefori/692534" target="_blank">📅 09:34 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692533">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8a17886d44.mp4?token=Unz3EDMKAx5z7F8bExuLQWYXN-eGynT4T_3Lvs2AUMtmjazBHNWkeVn8MrdnHlZwP_ClZOczA3qSV4P66CIKH5Ml2WA3-MjNJlw5JmSajpJDUfFXh9G83DAX04ZYmOXwYhpoXtaRuoGDzHCcNz65BMgAUGmeIdAptJNArp5LC3quKntrflzcAr0Kp1c0I6-7sUp7uiVBNSJC2iDFyBx9bmGizOvIHippOQsQFkwXag9ourG2MfwPE1FkI0iUfwUquN21fu_3sr9ueStdEo8lpOxHSwHl2a1FgPUwnnI6UEH_uLZXqI8dBstIp8rWCsZhFiA_MabWHdxxDJkgmOo-cQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8a17886d44.mp4?token=Unz3EDMKAx5z7F8bExuLQWYXN-eGynT4T_3Lvs2AUMtmjazBHNWkeVn8MrdnHlZwP_ClZOczA3qSV4P66CIKH5Ml2WA3-MjNJlw5JmSajpJDUfFXh9G83DAX04ZYmOXwYhpoXtaRuoGDzHCcNz65BMgAUGmeIdAptJNArp5LC3quKntrflzcAr0Kp1c0I6-7sUp7uiVBNSJC2iDFyBx9bmGizOvIHippOQsQFkwXag9ourG2MfwPE1FkI0iUfwUquN21fu_3sr9ueStdEo8lpOxHSwHl2a1FgPUwnnI6UEH_uLZXqI8dBstIp8rWCsZhFiA_MabWHdxxDJkgmOo-cQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
شهر ارواح!
🔹
تصاویر عجیب از بخش تمام اتوماتیک بندر شانگهای چین.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 38.8K · <a href="https://t.me/akhbarefori/692533" target="_blank">📅 09:27 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692532">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">♦️
روز پُرمدال کاروان ایران
🥇
🥈
🔹
ورزشکاران ایران در رقابت‌های آسیایی موفق به کسب ۳ مدال طلا و ۴ مدال نقره شدند؛ فاطمه مجلل، کیمیا زارعی و زینب نوروزی و سهیل موسوی طلا گرفتند و سوگند سینکایی، شجاع پناهی، عرفان محرمی و تیم روئینگ چهار نفره زنان به مدال نقره…</div>
<div class="tg-footer">👁️ 39.1K · <a href="https://t.me/akhbarefori/692532" target="_blank">📅 09:10 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692531">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/adcae89f65.mp4?token=lvdH5Em4pXHGGqG1S2zubLMG8mB-SIfN5ur_IZEh2Q-QDtDQvUYu2FYKFReg6U1HDU2i5bStp_vsNQe-_lTBPpnXK0Np6Ekq7LGOzwqGLJPVGqMiA2j_WjgrbucWMsLq2V3dyyD9OTwhODiOXIOGzqzehbiWfcge58pD1S9Epi7NT83SXtL1fXRM33rX-ElfPBw0ZwYUNOanzVR2Hxc45Uv0f6q07GPK20v0Fb3OboT_SVDvc_BJNGlUTm2ig0iZH7-DTRiILU6SAyfyfQQVml_5hzp_ZzKoAgGoD-o5O2d26fVHSD7z12zrrpF_6xr8pQK9wAvNHqAA0YvSZQ1aTw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/adcae89f65.mp4?token=lvdH5Em4pXHGGqG1S2zubLMG8mB-SIfN5ur_IZEh2Q-QDtDQvUYu2FYKFReg6U1HDU2i5bStp_vsNQe-_lTBPpnXK0Np6Ekq7LGOzwqGLJPVGqMiA2j_WjgrbucWMsLq2V3dyyD9OTwhODiOXIOGzqzehbiWfcge58pD1S9Epi7NT83SXtL1fXRM33rX-ElfPBw0ZwYUNOanzVR2Hxc45Uv0f6q07GPK20v0Fb3OboT_SVDvc_BJNGlUTm2ig0iZH7-DTRiILU6SAyfyfQQVml_5hzp_ZzKoAgGoD-o5O2d26fVHSD7z12zrrpF_6xr8pQK9wAvNHqAA0YvSZQ1aTw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
هر صبح این ۵ حرکت رو در دو ست ۲۰تایی تکرار کن تا یک روز پر انرژی رو شروع کنی
💪
#ورزش_صبحگاهی
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 40.4K · <a href="https://t.me/akhbarefori/692531" target="_blank">📅 09:07 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692530">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">♦️
ادعای
وال‌استریت ژورنال: چین به ایران قطعات نظامی فرستاد
🔹
چین در جریان جنگ، قطعات مورد استفاده در ساخت پهپاد و موشک‌های بالستیک را به ایران ارسال کرده است؛ این روزنامه همچنین از ارسال ۳۰۰ تن ترکیبات شیمیایی پیش از جنگ و حدود ۱۳۰۰ محموله قطعات دومنظوره در شش ماه نخست ۲۰۲۶ خبر داده است.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 39.1K · <a href="https://t.me/akhbarefori/692530" target="_blank">📅 09:00 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692529">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VcYqrKK3Ooj5Ead7rUyysB7GlMReJAuxjXdqaEB0wxd4PlHMykiE8rpe1RO29g9_0h9d47XipvsjG5m81jRdc2EE6idzqYZx38aTGZBfYc5uUP4WYwDKyiLiTdcJSj33V79Ffwg5ZyixyoFBkwLF01REw778YVZWfFJFB8XxeHAevT0kSXZQa0-NbJdXI_U0MkasnrqErXOCJXC47wHofE8xh36AQ4UwYduCMph-_cYsARKBglwVD_iOGOhx1_BbWc8KkeY-E-bKMKwZ-NnMAeUp4UDhBlVeFMldy191CJE_82t33p4EWvVa53Zf_e1QYGFY-Gmpuc4ZC_XnnnhLkA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
نمودار کشته‌شدگان دی ماه طبق سخنان ترامپ و وزیر امورخارجه آمریکا
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 39.8K · <a href="https://t.me/akhbarefori/692529" target="_blank">📅 08:58 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692528">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">♦️
ترامپ تصویری منتشر کرد که سی‌ان‌ان، ام‌اس‌ان‌بی‌سی و پولیتیکو را به شکل کیسه‌های زباله در بیرون کاخ سفید نشان می‌دهد
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 40.4K · <a href="https://t.me/akhbarefori/692528" target="_blank">📅 08:53 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692527">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2f28499e49.mp4?token=JE6DSdKly_4NcGkEePbTnL5vlP1nojIlpY_JlLxaB_S-s_gMwV-gUk41Tb6PmYayOSaze2PzUoMHOqYIKM_EVXXZGiZVRcR50CKBpsC1EwX9HP-fDMoPGxLrY8wWNRfm59Za_OZZudRag_r5oKBX9PLXbwMOZBlw28E5usqcj_-4w_NcTkjjDg42ctFwC0wcex0avvS81VX0COluvNQ2vKdHgITmkoymsNWy9sna1_EOdGTpxfLGOW4BBaRByP29E4nk2HnqOA-IrBV1wKW0xBs6YqNxrwmNsSigqBqRI1LNLUFnfx3azXcqSdZ1joFem-YWQD6ZwqCR3ra71cz0XQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2f28499e49.mp4?token=JE6DSdKly_4NcGkEePbTnL5vlP1nojIlpY_JlLxaB_S-s_gMwV-gUk41Tb6PmYayOSaze2PzUoMHOqYIKM_EVXXZGiZVRcR50CKBpsC1EwX9HP-fDMoPGxLrY8wWNRfm59Za_OZZudRag_r5oKBX9PLXbwMOZBlw28E5usqcj_-4w_NcTkjjDg42ctFwC0wcex0avvS81VX0COluvNQ2vKdHgITmkoymsNWy9sna1_EOdGTpxfLGOW4BBaRByP29E4nk2HnqOA-IrBV1wKW0xBs6YqNxrwmNsSigqBqRI1LNLUFnfx3azXcqSdZ1joFem-YWQD6ZwqCR3ra71cz0XQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
چاه مکن بهر کسی، اول خودت دوم کسی
🔹
در جریان استقبال ترامپ از همتای چینی در فرودگاه، واکنش رئیس‌جمهور آمریکا به صدای شدید پرواز یک جنگنده حین پخش سرود ملی خبرساز شد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 42.2K · <a href="https://t.me/akhbarefori/692527" target="_blank">📅 08:45 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692526">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">♦️
الجزیره به نقل از دبیرشورای امنیت ملی:آمریکا پنج روز فرصت دارد تا شرایط ایران را بپذیرد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 40.9K · <a href="https://t.me/akhbarefori/692526" target="_blank">📅 08:42 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692525">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">♦️
چرا ملوانان ناو آمریکایی خودکشی می‌کنند؟
🔹
وضعیت بحرانی ناو آمریکایی پس از ماه‌ها حضور در جنگ با ایران که اخیرا مجبور شدن بهش پایان ماموریت بدن!
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 41.6K · <a href="https://t.me/akhbarefori/692525" target="_blank">📅 08:38 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692524">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OFjVA7OSeord3hLdLWk9lTdH3dJ9pm0_TdWQl2OAaOcE-Lq9Re-diYECSFEbAnGstbvSvnY_YSLXqwfUbyFXXphtVfQTHCdRHAdgIGq-aYb6EKdvHVFwl4hUPjzm86BAcn4x-Xg8aIUVSluVlkPVOXf0Ei2nsNo559PubkAZflP9Wco8sR0ISsUI4ZskRNb0K00HoF3-Ab4B6O8KO9iJ7sowLpd-iVUOmwyY6Lr4BsSlcL7jwnMcenRLXJcxcRVXBk84B-pTTeWmgv9tXA3g9eCgbBMnianTDNrKHDi_JuNZcW8nUjq1HH3jl8ZyefVrBgWzkOEo8XzyjUefmem8ug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
مرندی، تحلیلگر سیاسی: اگر کشورهای خلیج فارس جلوی پروازهای ایران رو بگیرن، ایران فرودگاه‌هاشون رو با زور تعطیل می‌کند
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 41.9K · <a href="https://t.me/akhbarefori/692524" target="_blank">📅 08:36 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692523">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">♦️
داریوش فرهود، پدر علم ژنتیک ایران: مهاجرت کنیم یا نه؟  #همه_باهم_برای_ایران
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 41.8K · <a href="https://t.me/akhbarefori/692523" target="_blank">📅 08:31 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692516">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/aX1sP3rbSwYDZRNPulgzBQ_qNSTVOus0-8VysTkRJLRQca3NEwu75a_VZSGHD-Bd8tV6okfxc2gDAawM5pcEj7StqYpeWe04CyPrlXXAA6lr8HTyQOkNMEfXkpt2eqvbZxyisxQPz8GKIJqKeOEd86iHh9SzD1pzaqcGwtuy2r8Uri8IYOHvxdvWFg1Kxzc4KVGglD6A1qe6vZbbUrkNBUp_H5YL8ru91ttepWF0JdCqixj2Apn9IWoVWiH7kRqjeYS2H-PvAoz2j7xQwzUkVFih4u32saOWXTqvFCwY7HVgTLVSaIqITZL6YchF-OKpYYaEYCzYUdaZXHMwZ86JQA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/HqFWp3MHnftzwADzttEF0_5xzEMZ5TYzA0Nt0jZxGW18EFxbqrG__D3svUVb4TDTJMqtIWVxci-2aKCDiCVuDtLfG1mH9tSv_XIEKkQOEtql0pEhgjn343MLlIbF98eMIEm8VBJ2fbjIfLqzOvhJV8R_LcGt4BeVN3xLpSmy-FpB5xQYaGH4YTZCvDFbTdjt4l9iIAZVA9T8kHg0jIwCd3zJcmFO23mDloMApSkhARD5jsGGshi4QBDq7Akc9VzS6uJ2PdVWjJr_f_REBlPKT-iePR8uTTc5vg4445I9z5S0ACBz9X3DQQZhNXZI-vc4SulGDIQS-EJGgo89JWts4A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/nqwl6P6xM2UNDDWhEIwxJE6XPU8RqjeZTqSQ6wOBtifog7E-8Yf3CHNtpB2hhjP_RFC-QeqfoSlUH5NXJLuHpVwFxXFNfUGt-juHumxpVWEp9M6IvpkCyNOPy1pTMcbJUGa0Wrky5Mcza-0fynybG9zMJVBYpSCsnqd094dgHAI8CdYBjRSzKKdSF6Si7tDOODNbAij8_Gf3rrTAmy_OxmWIbuPAV39iadsqcqSTgSThwPOCJXo8HXDIkthWnoj6vLjlNK_PdyvPNZj1lXA2qSOCIvy3VgVXa_F-b9xxN7GgPGywrSPeO43On7no0F6cWzcjDQA6NVl1RhL5x3pUrw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/R14IHSkx71N9MlUDNTLR7Rv-nKlwDYAwxOrr2P7s4B8E93LV5hEhITqms9PqIqO3T7zACbC_5kna-t9dFO4EwLHnRRTnsRw6qTRi6ywaVZIIlbQv5I7q4hfggxDg-jgCuz-iyEmj53JgMRconY37GzJTf4BRGqu-s9W6TIsC2q8Sn6_EzppczjVXQQPSejgZvpg0E1PugoI9WtPsFAnab18ZzbRGdfotgT6UU4jgSoqmtMQ4pxzquAzf1AtYt20yCWnntx0TXE-lRctTpMsIAMiJFD1IJTQNpr5bwfx8mZsQxZLRs24RIACenfdTwqrLN8ZO5mUwT_-IRUjIVMrHlA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/TdzEmet_wG0Irw_IMMjnXUblPSu6tYMqSVxsrKf-uIX6JzgNRYGhYNYY0YDTUWre7kod1b0QFf2OKRQvhW-yFoh8GO4UkfRHyUNkTzvceMZdzvY8sVbPdzkpt5ZfHPNU8r_KTGXT_Hbc7nDgHmJKTSzR91ZoBkpY3fED9XQ4UKlsB2j0FMGIeJwYhpvooa1MyyvzSAyhJUm_M1-6gkZ67GgUg1vYkFP7gPnPx179IZXB8BgL9VykYdqQS3ezguYGq8TWHxKKGmLhHXafN4DFn5zCprKJsz1pDeTgOImWWQqpMZPYaVxxjrY6uB_DQrCXoxlmoSLue-eW03sFccUbmw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/r5jaeKTLKXnw5SVyuFEnCErs3DbyYRIHrda4bJdGBpzDa9V57EdIchuzgX8WGOlVYy46HQY4SMM2PIIoj_Rds-0dN02SwdtQCyQEnOvCCShbaLFsWYdXywloYXqlA9oOGL4HUfXxOQvI59Xw3shZEkzMeZnEwH2uco4whuhs6KJKjXoE9xY4Tcgzd0e0Rj9f1m0UP2BkJje5uhZ-FqY9SRuCnXF2jGsi_bAOhWAu3aXV0mf7M_jxYJ3g9ONygZx2O4iDgb8jJbCfH02EcXpZFmwVbo3T9s_CznlSw2faYKyq3fuUxdLjofMcnwCa8_ikoBYObp4c0cLV1-g_ZLe4Lw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
عکس‌هایی متفاوت از جنگ تحمیلی ۸ ساله که کمتر دیده‌اید
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 41.7K · <a href="https://t.me/akhbarefori/692516" target="_blank">📅 08:13 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692515">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">♦️
رئیس سازمان برنامه و بودجه: افراد تحت پوشش کمیته امداد، بهزیستی و افرادی که استحقاق دریافت کالابرگ با مبلغ بیشتر را داشته باشند، بدون اقدام خاصی کالابرگشان افزایش می‌یابد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 39.4K · <a href="https://t.me/akhbarefori/692515" target="_blank">📅 08:07 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692513">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f9a20a33b3.mp4?token=jFiJ7d2wIA7bW9gc7l48398SvoZ6HxwnZTSPYam4GbntusXVpMX_gpfHE_nbJ46s58tngDurkipmDjyQbQnt36SYSjLPDephFwb5yS8vN1P12lb20Ip6dRLOrkWToN1W0j-pOkAAt9DtYcKlVaZ6smYpQoHGWZBvB8Dfkgpzx1FKVjui7RuwPuuEeZdEvU0bldhqCi26FKf7qAvzFd5Tl0RAEnoUg6XJXfrNUFtmU8zckO2oPIxK-SXMdzCmpXn1NAnGGhFl11s5TsOhHH_si55JI9HvcYAnfbyvIeQrPa0M8pR0g2bGY5XPibs2RwzX7Vs1u7vWNAqhpA1AFZvTmY0x-qVRc6Ea8R9bMtrCiwmc0ASqyFaPEKlmDrYIT0J9dBl1INhE9AtXk-5-RH5DaVs-k1uMrvlVgb9E8QlNEbp3OVJTDTyP2TRoIb5K5pwZRHBj_Hu7_niq_q0th3P-WtS7H_M1OGCPv0o9ANPO6E7Orr5eEEuXYw0bqSh222L5mMCExesFMCV3wwkweEsxZrDnF5Exk55RoS_7K-vpiGirbOLEVb0vLR4HVWEuuJPl-_uckP9NfzsEzPcG5KGKShipxd1JK0wC9PKinBshoCCGIg0JUK0uYumaA7f05CgPpNEgFNSOKYaYfgpqm4I9Oq5h56YxrODJlZg5dAJrqTA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f9a20a33b3.mp4?token=jFiJ7d2wIA7bW9gc7l48398SvoZ6HxwnZTSPYam4GbntusXVpMX_gpfHE_nbJ46s58tngDurkipmDjyQbQnt36SYSjLPDephFwb5yS8vN1P12lb20Ip6dRLOrkWToN1W0j-pOkAAt9DtYcKlVaZ6smYpQoHGWZBvB8Dfkgpzx1FKVjui7RuwPuuEeZdEvU0bldhqCi26FKf7qAvzFd5Tl0RAEnoUg6XJXfrNUFtmU8zckO2oPIxK-SXMdzCmpXn1NAnGGhFl11s5TsOhHH_si55JI9HvcYAnfbyvIeQrPa0M8pR0g2bGY5XPibs2RwzX7Vs1u7vWNAqhpA1AFZvTmY0x-qVRc6Ea8R9bMtrCiwmc0ASqyFaPEKlmDrYIT0J9dBl1INhE9AtXk-5-RH5DaVs-k1uMrvlVgb9E8QlNEbp3OVJTDTyP2TRoIb5K5pwZRHBj_Hu7_niq_q0th3P-WtS7H_M1OGCPv0o9ANPO6E7Orr5eEEuXYw0bqSh222L5mMCExesFMCV3wwkweEsxZrDnF5Exk55RoS_7K-vpiGirbOLEVb0vLR4HVWEuuJPl-_uckP9NfzsEzPcG5KGKShipxd1JK0wC9PKinBshoCCGIg0JUK0uYumaA7f05CgPpNEgFNSOKYaYfgpqm4I9Oq5h56YxrODJlZg5dAJrqTA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تصاویری از استقبال ترامپ از رئیس‌جمهور چین
ترامپ:
🔹
قرار است با رئیس‌جمهور چین درباره ایران و موضوعات مختلف دیگری گفت‌وگو کند.
#Devil
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 40.1K · <a href="https://t.me/akhbarefori/692513" target="_blank">📅 08:06 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692511">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RJ7xSanwk3aSQ4KNJl967mNwH_njymvRhf1dZuxLWwe6cdi-rBISqvV2rS450_nLNg5ZZ8DSg74ECkhqhcUIHL1ZKHzp3izpw8UOtLqTXyBc8iSn-fzK9fAuyxlwwNp9qr_ZpIF05_oQehyYrhjbkvhzF64moVI_0zIitAPj2eF_5totrramS139kCkWi6QU5ySwVCQiwntYbojCbb_0S2pYxgRIdllbU4Wj7xnbZwTiSw9MbBtpaIXBDYOL3akGZIzOx5-0d6u_gVMq-jQgxGIgoueS67s65E_YUHOzYSkRO__kd42kXPrY9pUmeDX411hjASFvfFXptfUhzJ0rug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
دبیر شورای اطلاع‌رسانی دولت: همه برنامه‌های هیات ایران در نیویورک در چارچوب تصمیمات در تهران، صورت می‌گیرد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 38.9K · <a href="https://t.me/akhbarefori/692511" target="_blank">📅 08:02 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692510">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">♦️
روز پُرمدال کاروان ایران
🥇
🥈
🔹
ورزشکاران ایران در رقابت‌های آسیایی موفق به کسب ۳ مدال طلا و ۴ مدال نقره شدند؛ فاطمه مجلل، کیمیا زارعی و زینب نوروزی و سهیل موسوی طلا گرفتند و سوگند سینکایی، شجاع پناهی، عرفان محرمی و تیم روئینگ چهار نفره زنان به مدال نقره رسیدند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 39.6K · <a href="https://t.me/akhbarefori/692510" target="_blank">📅 08:00 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692509">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Idds51pQkMKi5oLI3NCupqYKqq62jOLFy0l_RzV78AT0trmyPVPu1nntHUvV2D74hSWtMpU_89iz-mHGqH2z-vSzZvVig9otE1R31p8o2VP7R6yjziYSEJ4wd6JfJF5Vyz_Dvr5KDN9Z4Ym2tJsJpVm-LKnk0EOdKKj9OR3KimbrjdF3HLeV0V_xl6D_IydLDNpSlEWtMD4hYCruTLY3eK4MC_k2egdm7zi1V6uzx79P9rL6gxFXWFD0fKwd0X_BgiXycld03vT6hm-y33Tq5rUbooQXcSu_uW4eBV4YLF1QYVMgk88u6dYBo8I0Izh_d5rLfPRgqqTLP-ZnaVkK8Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هر روز خود را آغاز کنید با:
بِسْمِ اللَّـهِ الرَّحْمَـٰنِ الرَّحِيمِ
🔹
با خواندن دعای عهد و چند دقیقه گفتگو روزانه با امام زمان (عج)، پیمان همراهی و خدمتگزاری‌مان را تازه کنیم.
#صبح_نو
امروز پنج‌شنبه
۲ مهر ماه
۱۲ ربیع‌الثانی ۱۴۴۸
۲۴ سپتامبر ۲۰۲۶
پنج‌شنبه‌ها
#دعای_کمیل
بخوانیم
⬅️
متن و صوت دعای کمیل
@AkhbareFori</div>
<div class="tg-footer">👁️ 43.3K · <a href="https://t.me/akhbarefori/692509" target="_blank">📅 08:00 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692508">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromDigikala | دیجی‌کالا</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kX55Xn0yzhLAvcyio-f5SrUJpXTXg2mtvXQgWaFZrdeNN5Av1HG_JFNF9yQ-DPN_zhvx0IdPCi5HnbvKh4Cefh_Fs_ny3FawbZAAmBFi9BEXQoNO2svs4uRTmuSIbSlkplDa5bL7-1_iGvkzzoI0eJw2CuEo11AoX4qJt27k7QZjjLtpV9T91xuU3TpatMqEv1hdQ6WvOcowoGNtXbrlC3DA9Fzfq7sMKxSf2yL4RoLXuiOD9lH8cUHDhd3ecppJSnikkqVPmcHfH22oXU_HxylUa8v3YYWmP7Cpmcp1QQmGrUg6hNnJ8qLE7YTeECM5g3SmVkpn0f5rqlrso7OmkQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حراج سر ماه دیجی‌کالا شروع شد!
🛍
✨️
تو حراج سر ماه
دیجی‌کالا،
علاوه بر کلی تخفیف هیجان‌انگیز، می‌تونی برنده
آیفون ۱۸ پرو
هم بشی!
🎁
🔥
البته یادت باشه، اگر با
اشتراک پلاس
خرید کنی، هر خریدت
۲
شانس
حساب می‌شه!
🪄
و با خرید
اشتراک ۳ ماهه پلاس،
۱۰۰ هزارتومن طلای دیجیتال
دیجی‌کالا هم می‌گیری!
📱
✨
➕
اشتراک پلاس بخر، طلای دیجیتال ببر!
💸
➕
از
حراج سر ماه دیجی‌کالا با تخفیف خرید کن!
🛍</div>
<div class="tg-footer">👁️ 48.5K · <a href="https://t.me/akhbarefori/692508" target="_blank">📅 00:53 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692506">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Y4rZMH_6dmV3KDEk2qYCFUJC9EMOasNvI-tWwjj9L0BzHrevbbBYLPtP3iyg4SoEndWyQai2XVENQHaPBTPtDiNrUQ0xE9x7r0SX6J2oFnP7ww41E6vYL7NGnV3ptTipJBNvUmQzA1qyIE60eSJqKg4HelMWKRPHIw_if4iuRFa5kyZwncDS4Po5J91Py2BMl0Oe8cd15Rc7d-nXVMiOxr-lJC_hpjX0baFgAD5ub1pF86VCz10zbbjWe9DjILCcgGn_GfcNrTMKK00eUrRZQWXd5LNKPBW_IOnKrD-zyU6pCxrcXtISkAconcbHFABUbs5jpQ-tG9thT74uWT8A6g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
ست سوییشرت و شلوار مردانه بالنسیاگا مدل Hami
✔️
جنس پلی‌استر سبک و باکیفیت
✔️
فری‌سایز مناسب L و XL
✔️
مناسب هوای خنک و استفاده روزمره
✔️
راحت و خوش‌فرم؛ مناسب سفر، مهمونی و پیاده‌روی
📏
قد سوییشرت: ۷۲ | قد شلوار: ۱۰۰ سانت
🔴
قیمت 1,650,000 تومان
✅
پرداخت درب منزل
ضمانت تعویض سه روزه کالا
خرید از سایت
👇
https://memarket24.ir/product/fast/51854/180124/</div>
<div class="tg-footer">👁️ 53.1K · <a href="https://t.me/akhbarefori/692506" target="_blank">📅 00:52 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692505">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">♦️
برخی منابع فارسی: دقایق قبل صدای دو انفجار در تنگهٔ هرمز شنیده شد
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 52.6K · <a href="https://t.me/akhbarefori/692505" target="_blank">📅 00:48 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692502">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">♦️
پاسخ کنایه‌آمیز زلنسکی به خبرنگاران روس
🔹
خبرنگاران روس از ولودیمیر زلنسکی، رئیس‌جمهور اوکراین، پرسیدند:
«چه زمانی به مسکو می‌روید؟»
🔹
زلنسکی در پاسخ گفت:
«با موشک!»
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 55.5K · <a href="https://t.me/akhbarefori/692502" target="_blank">📅 00:24 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692501">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aHxl5vx-wsNW4g-a951g3Zcn1fGt_asRw3Qvzo1gEfG6Bxqze7x18UXafiuaJeGXTq7mRaksbi0IamYhMxPuV-qJVtP_sdNOujuTqi2vb_D-3ond7JnqLTBySyRnnTWOZOShUnOSBlf2-2aqh8_4wPIxwZpY33tWBfGZOkGiYIRNd_JtEMkHCj0QUhFqB470KXldp2Dpe39jIrNNNwdN4RBU7aleh5brfQPGK4kRAwQC6gQjyWOXRwbzMtddLwzfKWSP0ZCOqaxMFT-Sm2OSvaq3mP9cDBT-IeuSX0FVgKRquTiHWGhL-1ZRgdsgtSDKRcG6LcbhOU3ZnPiuNXOA8A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
مهرماه فراق
🔹
شایسته است هم‌نوا با مادران و پدران داغدار، بار دیگر یاد دانش‌آموزان شهید شده در جنگ تحمیلی اخیر را گرامی بداریم. امسال روزهای خاطره‌ساز ابتدای سال تحصیلی، برای ما غمی از فراق فرزندان سفرکرده‌مان را تازه می‌سازد. ۳۱/شهریور/۱۴۰۵
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 55.8K · <a href="https://t.me/akhbarefori/692501" target="_blank">📅 00:17 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692500">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">‼️
محسن رضایی: هر کشوری راه هوایی اش را بر روی ما ببندد، فرودگاههای آن کشور هم نمی‌توانند پرواز داشته باشند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 53.6K · <a href="https://t.me/akhbarefori/692500" target="_blank">📅 00:13 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692499">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Fi-DAZHK1XcYVARFS1yUf98wL42HpL9G3UoYuON7nAfmcRb7nTVr8VJyZ0u1YgjMIMEi13MTA2ly0unl-OdXKxG10TIbYuKkp3MKxfpU-7I8CkucHvs5wNrVhVgWcgQUVvMr7zmF7HP8ghw3O9pDtM1u86de0-Gk4DwOUp6aHtK_aGjablWCIG0BZfUcUBE_SBc3Z_YfTES8A3nTjwQ3l355Yf9-sZHPuLbZfiybVmRsaQxZqSrIZD90vSi_VqJ84gjq8EF4phlAX76qbqOL6fy53jg5GOu1eMvRNpm-1lFuQhNXYtic28xT18vUpyNjfBDjPknSx4zOGj_ICfL_dA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
دیدار پزشکیان و رئیس شورای اروپا
🔹
در حاشیه هشتاد و یکمین مجمع عمومی سازمان ملل، رئیس‌جمهور پزشکیان با آقای آنتونیو کوستا رئیس شورای اروپا و گفت‌وگو کرد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 56.5K · <a href="https://t.me/akhbarefori/692499" target="_blank">📅 00:07 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692498">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">♦️
سخنگوی سپاه: رئیس جمهور ما پیام اقتدار ملت ایران را در قلب نظام استکبار باز تولید کرد
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 53.4K · <a href="https://t.me/akhbarefori/692498" target="_blank">📅 00:03 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692497">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">♦️
پزشکیان از نیویورک خطاب به مردم: دعا کنید ناامیدتان نکنم
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 53.2K · <a href="https://t.me/akhbarefori/692497" target="_blank">📅 00:02 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692496">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromخبرفوری</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UPN9XqvNOof3hVHmh2Rq8a7vy04Vj409fvr_mdFa894d6zsl36O9H4YVejADEWfomL1QO_KHyW_YspAowHE4OLJZk06dLOYjxoctcGBEiZXl9BENoZ8Y9xfu7O2WVeb_Bls9flEDi8l4yq4GjsFirOrTx3UcPTEhvLmpuAVazhWeG1qCKfN4FbCiltiUEk8Iu0bUWIZYhRteR5EFbkYSBZje8BI0n6zYSeILt0iSwTOXXKCfFLHsCl13PU1kmKzrwZH4cdOcvwX9GYBSGdn3ae-_al6oX2wBbonc4xVqgkSvkiKdcu67aCls711U2An3R7zUOhiboZ8IOczqjxWL_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
با هم دعای فرج را برای سلامتی و فرج آقا امام زمان(عج) می‌خوانیم
🔹
با قرائت دعای فرج به این جمع میلیونی بپیوندیم
@AkhbareFori</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/akhbarefori/692496" target="_blank">📅 00:00 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692495">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromالو فوری</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/F9YbcR-WG6Uli3vXZo1qqAuSBsQUcHBDyM6xP3rtbzd6VGPLeQcGAGVDItcwoe3DPHsa2TvD-NOU819ubfOtxc3ImeoEMHP5uqd7w_y09GcHYZqdq9cwEVHV84_Rti5Etpn1t-SoJ2nD-owA7HVI384fwCqvcQGuDO8K0mv-V1e5ons5lqyuNth9AY0Jh1XJB-jgg4Yie-FqYVusRMJEzm5mijbZvLyHaw0BWSVxZ_RdTHitPB6cbx9FDp4rKIXVdcauhjEqq9-4eOBOau6RZPSlnKcOIQpf40LuBeeVn65J43BEYWbhOsrG5o8RVVoIsoafx5w6HSG4hvzMVWNrfw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
فراخوان خبرفوری | جشن فرشتگان
🔹
همراهان گرامی خبرفوری، شما می‌توانید با ضبط یک ویدیوی کوتاه از دانش‌آموزان خود با لباس فرم مدرسه، در این پویش شرکت کنید .
🔸
از کودکان خود بخواهید این جمله را بیان کنند: «کودکان شهید میناب؛ ما راهتان را ادامه می‌دهیم.»
🔸
ویدئو های خود را به آیدی زیر ارسال کنید
👇
#جشن_فرشتگان
@Ertebat_baforii
@Alo_fori</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/akhbarefori/692495" target="_blank">📅 23:57 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692494">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/db361334d0.mp4?token=SAD8vqkHQW_Y3l4t0Xlp1CYWY9tz2984uZqj7R1Km8TQRxDo4UFPlbzHfKSXkNtBmsqLz2k1JYa3Cibd_u8HyrKXnZQC0xjz9LL49d57zUsXM48IPPHfFn3HcYvNm6s5GIRz8WjkmdUSX-p_ijqRHsEY2BRc-SgO6OBHtzOaFWTsIOWWuFViayxtQI46QCjf0FBJwP_-aLxG0ETJNFcXWuPsVwGq3D7fqj6AhS5DIgO1_nuA9n5eOXNqG56Zvw9z6esFCdPtkH7yiSlBIQBhYNRWrGCVDTcIu1f6DrtpvKOTrifLXZ9fHa9f5u2P1FEPOWwGe3IyD3GwfEQWxTHt4g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/db361334d0.mp4?token=SAD8vqkHQW_Y3l4t0Xlp1CYWY9tz2984uZqj7R1Km8TQRxDo4UFPlbzHfKSXkNtBmsqLz2k1JYa3Cibd_u8HyrKXnZQC0xjz9LL49d57zUsXM48IPPHfFn3HcYvNm6s5GIRz8WjkmdUSX-p_ijqRHsEY2BRc-SgO6OBHtzOaFWTsIOWWuFViayxtQI46QCjf0FBJwP_-aLxG0ETJNFcXWuPsVwGq3D7fqj6AhS5DIgO1_nuA9n5eOXNqG56Zvw9z6esFCdPtkH7yiSlBIQBhYNRWrGCVDTcIu1f6DrtpvKOTrifLXZ9fHa9f5u2P1FEPOWwGe3IyD3GwfEQWxTHt4g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ویدیویی پر بازدید از لحظه‌ تفاُلِ امروز پزشکیان به قرآن و واکنش قابل تامل او
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 49.8K · <a href="https://t.me/akhbarefori/692494" target="_blank">📅 23:55 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692493">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SAjexuN1BqUhrstiOdUJXykMKByfiVGYhEELUxhSgkOlp_W1nIoX10-f60Tk2Rf5H-YupWRAiOhCxdRqeIqTD49h49xPm9aj3yAyiC-OnDtpzSBw-9ruXMTIeeYcCP-k8-cABxwZC7KpkpoCvTkBgSELhSg78PAexkUpTXQIP42n-i8EJV2pol6O3raAR2iCTjxgslXaA7eFpysCZnd5Q5vK-Iz-mxVgaEEEgopmIavlZW8erojzfHOEzmkQU99gTL2-VJG6eNAwK4OTrmSJdoE0EeCihlrwaAMXU3iKEm6oSGgTMl4puv6L_-ARFoFqMU3HNQqMC9FBBSNpSdYUOA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
روآن سباستین اتکینسون؛ خالق نقش ماندگار «مستربین» ۷۱ ساله شد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 48.4K · <a href="https://t.me/akhbarefori/692493" target="_blank">📅 23:51 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692492">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromمن°</strong></div>
<div class="tg-text">تقدیم به شهدای امنیتِ
سرزمین عزیزتر از جانم</div>
<div class="tg-footer">👁️ 48.1K · <a href="https://t.me/akhbarefori/692492" target="_blank">📅 23:44 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692491">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/84ca2bdb3d.mp4?token=CyIUe-vvA5Wu3Z2x9k_dv4ruA_OMZlbuR6616rmBFKt2lYorQsycd7QTykOrf-GBd8iCWpNRBn_k_iCiy7JPPVh5__bSrh4S1WgZjUAabBU7GW22TYYFQHzh_wjDjWDlxdWsI-N7tJgvBj7JcRGzTQ5pfFsFwueaTQcgyfazoD878lksBDeVYBTLn8dVjhNKHYDjGipZPcg9jaKW7Ffi6kYhebGWwJ-4naXlXVkY9NrbRPvM-lZcE7Il-97Ia-U90r9JmJif8QLO9Kts8CCMPGG0ZpjEX74nmDITFFwmTpICFoj7Ns5EKZ94qM5FTxT5kiwIf36jYmZdDbc8p2WGaA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/84ca2bdb3d.mp4?token=CyIUe-vvA5Wu3Z2x9k_dv4ruA_OMZlbuR6616rmBFKt2lYorQsycd7QTykOrf-GBd8iCWpNRBn_k_iCiy7JPPVh5__bSrh4S1WgZjUAabBU7GW22TYYFQHzh_wjDjWDlxdWsI-N7tJgvBj7JcRGzTQ5pfFsFwueaTQcgyfazoD878lksBDeVYBTLn8dVjhNKHYDjGipZPcg9jaKW7Ffi6kYhebGWwJ-4naXlXVkY9NrbRPvM-lZcE7Il-97Ia-U90r9JmJif8QLO9Kts8CCMPGG0ZpjEX74nmDITFFwmTpICFoj7Ns5EKZ94qM5FTxT5kiwIf36jYmZdDbc8p2WGaA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
کانال ۱۴ عبری: ویدویی منتشر شده از زیر گرفته شدن فرزند سفیر رژیم صهیونسیتی در غرب رام‌الله
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 50.6K · <a href="https://t.me/akhbarefori/692491" target="_blank">📅 23:42 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692490">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vmzMJEfBlwAZc3zewMw87m-UQL0Npbx2Ma4sFQCN4X91LlIxFK12hLTQq1c0i8aL2AVC3Ycz0M8snqB8nLE_qzeh35DDfwgTeOH1Zh7nEyumfc3ZkvbB0kveVfgl8Gi57K-y7YSA2SwS0dhSvGdfes2FUH1InrO6pSkP7Wph6t-wRhnWmGKms-B0TStO67jztV84qMpJlM0TlUAAprE60beUC61YuAaGAr8PYGuBVvMgTXBDErP6etneg9ZL726Stqq7GPwk7EsQZAWVDdSYj85Wfdb6uRb-ZX7lDxbBIkvOXLdRr4OkAfZ74O2QmIt5vJc2z0Yj1H1a966qBCcQXg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
این پست رو ذخیره کنید؛ ۱۵ مدل آش مناسب فصل سرما
🍜
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 50.5K · <a href="https://t.me/akhbarefori/692490" target="_blank">📅 23:34 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692488">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromآمارفکت</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Y7S29RSb_0deC712Zqd3yUVC7yQuXnKajYHtSLmGFR0pIxU7Q-KVkQVxX5KMO-6JOooYzQaRwjoNjxme52S_Lef-1f_dTBkVLGrb7HiDlp6qjyqmRLWZyouCCOgjQYPWovnreTLF2v_iNLiz_HzmPqQB4CHn6ZoU18qECfZLjdLbG0rZgRr2hmNeq4n7b44DwnnpWfE-0-O-sLTYoTDmBIGw83cH_zEFdaL9JAzKqkj4fiHP4C_7O4sHds-xLKSZOHfndb9hCqqYQsweq6DAyzbIEJ-sBsxSIzlfjxDvpUi7KaR0SKQzJad4xu9C2S0sLWFsBpB3e5A99ajYM1v0-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/AaffYVeF_0uo7jLvHWyK7wmzcwyHp3erUAjQI2FZECjvvzvb9PfcFYiCUZ13r2Gb6xKCSkyIaKxYRYszPCRbxvhEZBDz1OTG7YPQdkWm1iQzdwwXyVxz1ZXIWy5RCQUaCjxqpTCGtbHkHC5Wp3lhE9SFdrL1XtTD9C05aoBb3NLffevSO3rPBOfdTr7PDdYhYWPA5F33Y2rOj6yyxTEimeY2Uy0hCApmUb_yq-rfJYoCY5jvdsgB4CAyZzoJFNuPFF1Kr6R5DCrZ3sAUQHTj-mWxGYvsrC35Yvghb94Uk18LKCDXXqffuC1yJQXnJ34zkWFa3lewuVnQuPg4tvLXqQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">میانگین سن ازدواج زنان و مردان ایرانی
🔹
بر اساس آمارهای مرکز پژوهش‌های مجلس، میانگین سن اولین ازدواج از سال ۱۴۰۰ تا ۱۴۰۲ افزایشی بوده و در سال ۱۴۰۲ برای مردان به ۲۸.۳ سال و برای زنان به ۲۴.۱ سال رسیده است.
🔹
همچنین میانگین سن کلی ازدواج در سال ۱۴۰۲ برای مردان ۳۱.۲ سال و برای زنان ۲۶.۳ سال ثبت شده است.
🔹
طبق هدف‌گذاری و پیش‌بینی برنامه توسعه هفتم، هدف‌گذاری شده تا سال ۱۴۰۷ میانگین سن اولین ازدواج به ۲۷.۳ سال برای مردان و ۲۳.۱ سال برای زنان کاهش یابد.
📊
آمارفکت | مرجع تخصصی آمار در ایران
@amarfact</div>
<div class="tg-footer">👁️ 51.5K · <a href="https://t.me/akhbarefori/692488" target="_blank">📅 23:26 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692487">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">♦️
مدافع وطن
🔹
رئیس جمهور در مجمع عمومی سازمان ملل امروز صدای شجاعت و استواری مردم ایران شد و گفت که ایران را نمی‌توان با جنگ وادار به تسلیم کرد ما ثابت کردیم که برای دفاع از خود از جنگ نمی‌ترسیم تا پای جان برای دفاع از ایران عزیز ایستاده‌ایم. او با بیان اینکه…</div>
<div class="tg-footer">👁️ 50K · <a href="https://t.me/akhbarefori/692487" target="_blank">📅 23:22 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692486">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">♦️
عملیات وعده صادق ۵ چگونه خواهد بود؟/ بررسی پاسخ فوری ایران به حمله اسرائیل و آمریکا
🔹
در صورت تشدید تنش، ایران گزینه‌هایی فراتر از خاورمیانه را نیز بررسی خواهد کرد. گزارش‌ها حاکی از آن است که ایران ممکن است پایگاه‌های نظامی آمریکا در اروپا، به ویژه در بلغارستان و قبرس را هدف قرار دهد. بلغارستان اخیراً استفاده از پایگاه هوایی خود توسط هواپیماهای سوخت‌رسان آمریکایی را تأیید کرده است.
گزارش تحلیلی خبرفوری را اینجا بخوانید
👇
khabarfoori.com/fa/tiny/news-3247477</div>
<div class="tg-footer">👁️ 48.9K · <a href="https://t.me/akhbarefori/692486" target="_blank">📅 23:17 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692485">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OEllMJPBm3yJz-0dhNYQLgV8dT87beBm55ZqPGDyvQwAeq60uA-X3tFS46Ie4Ad9k404sUyC7AFOfEzJVOfM7S-fQKd9CP8I3Fh4TWztTqH3fhX3N4Bl1kogfWZcpsujEmF60aZAbcaji1KwA6U5BUJZrO02QDQkvDTjQXKCzktcpdc_02K5D0F3j0WkV5U8RWki_lUZrnICiIeGGahzEuiN1fR6TSnCr4sVe26ZxnWGnzvlzmxBugAj3E1WFh8kHxRqSree5d_LYn3qgyx60JXx3JYFj2gHxL7b7So06qGxMsRTfjw_mquv5dTpVazqeyNjCjwvR38hUlaDddkQTg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
اسکلت ماهی بادکنکی همینقدر جالبه
🐡
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 48.5K · <a href="https://t.me/akhbarefori/692485" target="_blank">📅 23:17 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692484">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qTC_cXAaZMJ5_xHWli5abESlx5khtXaBKagdDUbBob_WhbatkToF5dwm2r6RvY-nv5E7ezm6MgkXVdDL_YwY88UQPIwvQJHJhc0PPRLl--s9C-ekgZCTswRIKwO2Ytf_QSJqCESE1ezJMrNhFgJd0ekab4yPlzed63TVLtuxJuGNvflKj5JwK_WTEQepIhXmvkAz0wAeEsvOMdPZzU1GhzD2jPnGKxc-UoHKrky1ypXSypy7iKHWVqK4uSWSn5svWudvx9WCtcStRGCnrSjqhxFAIM6RflQAqfkZXcQ0e7s1FK1WcWO48fo6Te3CunL1c90sOxSEtaJzxUe7DxQxRw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ترس نتانیاهو از امنیتش؛ حتی یک شب هم در نیویورک نمی‌ماند
🔹
کانال ۱۳ عبری: نتانیاهو به دلایل امنیتی ویژه در خاورمیانه، حتی یک شب هم در نیویورک اقامت نخواهد کرد و فوراً به اسرائیل بازمی‌گردد.
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 48.4K · <a href="https://t.me/akhbarefori/692484" target="_blank">📅 23:17 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692483">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromروزنامه دیجیتال خبرفوری</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Aea0d78MTQpFM6SpbBX3QKZb4TaQ7eS6UcfDzPvefVjdw9twWqHDVR8UPGlTTK2tTjbAvWyfgKvsMH06wyQ3o5aGJVAkFSx57o9QO6wzr0FVTwAC_rLbfP8faQKuevZRLhHs3r2U5Q77FgCyv-LXxenvq3ZIYok5Hrq_vaWNz_15GXL-DJNoOa3lO8jgSCkQVUXq58kaJ4PTiP1fF6rJbhEXgn4doOmjd8yCmkC3Xg_4cX8cNJhlrLp5AEyKLpqQHl2OZmOldrlOcKxn6KjSBdida6EveK9NCSy08i0YkNao0Np_j1CZXTnDBPwvjDVMf1JSjAAFTeD62gGAWuZpWw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
مدافع وطن
🔹
رئیس جمهور در مجمع عمومی سازمان ملل امروز صدای شجاعت و استواری مردم ایران شد و گفت که ایران را نمی‌توان با جنگ وادار به تسلیم کرد ما ثابت کردیم که برای دفاع از خود از جنگ نمی‌ترسیم تا پای جان برای دفاع از ایران عزیز ایستاده‌ایم. او با بیان اینکه یا امنیت را با هم می‌سازیم یا ناامنی را با هم تحمل می‌کنیم افزود که ایران به سوی جهان دست همکاری دراز می‌کند، ما جهان را به صلح فرا می‌خوانیم نه از سر ضعف بلکه از سر قدرت خود.
🔹
هشتصدوشصت‌وهشتمین شماره جلد یک خبرفوری
#تیتر_یک
@rozname_fori</div>
<div class="tg-footer">👁️ 48.6K · <a href="https://t.me/akhbarefori/692483" target="_blank">📅 23:09 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692482">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c3cc2fd75c.mp4?token=c_vBqCOg1hCnftaX44GByf-wrC4wLJCtwBecWmt_1v6k1IHmISfFtOaXC7F0vXp5tEm8qf36OrHLpAr8RESr-B4yLtbJX37Sfg5v2B7i5Rouo-xTNjb_-BMDM09l3WO9okNwN3GbOY4-NkIXWtelX6RNiSlAZy3P1jb4vE05BdFIicPnbDa8XhFgQLqnRQJdCRCRGII3eZ7m0Kbuyoov0CAo7gQ2HRXF138fZNG5pbbD5nM0Vp3uYDFAlOyoRpfNR-kRZkZ6Q1oZxnPO1KnxCWaXp3cVkP_xa3W-fsDZVmoTTj59jSkQM6Hcs5qr1bT_clsekykkd0-yub4S5uv5dw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c3cc2fd75c.mp4?token=c_vBqCOg1hCnftaX44GByf-wrC4wLJCtwBecWmt_1v6k1IHmISfFtOaXC7F0vXp5tEm8qf36OrHLpAr8RESr-B4yLtbJX37Sfg5v2B7i5Rouo-xTNjb_-BMDM09l3WO9okNwN3GbOY4-NkIXWtelX6RNiSlAZy3P1jb4vE05BdFIicPnbDa8XhFgQLqnRQJdCRCRGII3eZ7m0Kbuyoov0CAo7gQ2HRXF138fZNG5pbbD5nM0Vp3uYDFAlOyoRpfNR-kRZkZ6Q1oZxnPO1KnxCWaXp3cVkP_xa3W-fsDZVmoTTj59jSkQM6Hcs5qr1bT_clsekykkd0-yub4S5uv5dw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
صحنه‌ای متفاوت از آغوش گرفتن در یک تئاتر که در فضای مجازی وایرال شده است
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 46.9K · <a href="https://t.me/akhbarefori/692482" target="_blank">📅 23:08 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692480">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XKVGqzlCADJUOeXtKhC5-OVFfJ7MDUGqTyobfbm5JQiUA9bO7qmNwA3L27DXloz_WNJd3Gw5Jssch_4KNVd2qSXulaSd6AQ-SJc5VckxndFj7QK1VsBGO_j_5C6Fx8-ufP3yfV13mE9Mkr8R7oHE-Uql-jxUtxk2pbqb1fH-4OlX6wgcEBup0XmkoSs_oE8DFnBxMJArpsSvdQcl2ac6hVg98eaWZeeVK6tcdxUGhUwIlNmKzblog7AeN1bNLHixHbQB6Yb51m_5KQ8Au67n9uoEeJoAgM6ewNLp-8MXJP9Z3BY-F8DzFqtGh9p0Lf4RplWGxvydRUZVZkQuq-Q7CA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🩺
فشارسنج سخنگو فارسی؛ اندازه‌گیری فشار، راحت و دقیق!
🔥
این فشارسنج رو می‌خوای؟ قسطی هم می‌تونی بخری!
❤️
مناسب سالمندان و افرادی که نیاز به کنترل منظم فشار خون دارن
🔊
اعلام نتیجه به زبان فارسی
📊
اندازه‌گیری فشار خون و ضربان قلب
🏠
مناسب استفاده در منزل
✅
امکان پرداخت قسطی
🔥
قیمت ویژه: فقط
1,990,000 تومان
برای اطلاع از جزئیات و خرید
👇
خرید از سایت
👇
https://memarket24.ir/product/brief/63656/180124/
مشاهده حراج آخر فصل
https://l.memarket.me/lp/615/180124</div>
<div class="tg-footer">👁️ 47.9K · <a href="https://t.me/akhbarefori/692480" target="_blank">📅 23:01 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692479">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">♦️
روح کودکان میناب همراه رئیس‌جمهور بود
🔹
انیمیشن لگویی از سخنرانی پزشکیان در مجمع عمومی سازمان ملل و یادکردن از کودکان شهید میناب
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 45.5K · <a href="https://t.me/akhbarefori/692479" target="_blank">📅 23:00 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692477">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/opMSJdpcGfId0clLJVHgkMDqOOPjIsrGI7cg7wodsmoeGY6A-mgR7JUlWBK1SbP-nmrr2_e-9vzEJPxJoKnAri_tqvO3msDBFhOi3y68EJjeAQiBff8ebfAEPuY2C88XN_F4fGGWLYvvpPJmRCyMoYGVPRyAOLItJ60_WpKsebWepPV0m0_odN2j_57NJnCMoMhfcMvVlFNVCdns138Bx4Ij0-45CodYqNSVYctJzLdgs1-QfH2-6TTRSHpMA419CvIhm3Ld7D2w18NRQDp1Da7h7MWnvMva_3zFA0ba65FovFXvw_J-ZgELHd-plo9S-u9uUTii1qJoS6zP8cHBRw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/EWWbzzS3qPxaTDrebSU_Lkims2FHlVrjNRwab4I3DiGVQIEkDd_44WDciXRyWXIrWTudVP4yD0YyHiNSgyzot8fDsi74rS61_QFqXEnriX15Gliu-xMpnk-0e-W2qtzhtOPL2QGryPxXcrauSulajB-Jkr_VpzotDRBX1oOLmsbsngKrQmcRJrOSrqqE0j77uDa5uoeQhS51vjxN75EDu9Cpywp6nUcR5OFEEhMwRvEVPtQxpa3kkGZm4a9MvtdsOcjqS3PVSsjVunCiivc6zzDqANZnRQCfJj6tXaDipP85nYQ_6VaADyTrsaF-oBomQ-gEFdS0_feig2O7C05LsQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
ماجرای ادعای عجیب یک بلاگر بانکی در پی انتشار جدول پرداختی نامتعارف بانک‌ها به کارکنانشان؛ توجیه به چه قیمتی؟
‌
🔹
یک بلاگر بانکی ادعا کرد اعداد منتشرشده حقوق کارکنان بانک‌ها (۱۲۰ تا ۱۷۰ میلیون) در واقع «هزینه کارمند» است نه حقوق دریافتی. اما بررسی مستندات نشان داد این ادعا غلط است، چون «حقوق و مزایا» بند جداگانه‌ای در هزینه‌های بانک‌هاست و هزینه‌هایی مثل بیمه در بندهای دیگر محاسبه می‌شود./ تیتر تجارت
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 46.7K · <a href="https://t.me/akhbarefori/692477" target="_blank">📅 22:59 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692476">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/06787fe62c.mp4?token=otiW-f2_GUAEYDhlKAbbqfFhzl7-kZewLvS-eXdD2P6Et5h0addnXCI3jg7tcbJq3WPZj6dUjX8Eg5z13v6fsj8UUeFWCJkObeqCHVdLaMRAl2MLAZJnHdfdGdI-ixpzPGCxPEscmc9OAXVglAO7BM585Z3SUY20adfD8oLFU56NSsTBW2T1OOOkKdoyovMZQ2adYzxxO4zIRBmJvxiX4-mCJAVkLv8FPuFSgHhf55_Unnk32Ev-49sRcgyDwxjNrpbnDVZHL0LvSM0yVljYTBLquBmAWjSUJ_POxlnZdZIOVt8gSOcL6pdZdTXnj_u47whCBJ0SSDZM5sBY4Sz-Ew" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/06787fe62c.mp4?token=otiW-f2_GUAEYDhlKAbbqfFhzl7-kZewLvS-eXdD2P6Et5h0addnXCI3jg7tcbJq3WPZj6dUjX8Eg5z13v6fsj8UUeFWCJkObeqCHVdLaMRAl2MLAZJnHdfdGdI-ixpzPGCxPEscmc9OAXVglAO7BM585Z3SUY20adfD8oLFU56NSsTBW2T1OOOkKdoyovMZQ2adYzxxO4zIRBmJvxiX4-mCJAVkLv8FPuFSgHhf55_Unnk32Ev-49sRcgyDwxjNrpbnDVZHL0LvSM0yVljYTBLquBmAWjSUJ_POxlnZdZIOVt8gSOcL6pdZdTXnj_u47whCBJ0SSDZM5sBY4Sz-Ew" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ادعای کارشناس تلویزیونی: لابی یهودی‌ها نقش پررنگی در تصمیمات کرملین دارد!
هیراد مخیری، کارشناس اوراسیا:
🔹
لابی‌های قوی یهودی در روسیه یک پیشینه تاریخی دارند و در زیرساخت‌های اقتصاد، فرهنگ و سیاست این کشور ریشه دوانده‌اند؛ این اهرم‌های فشار همواره در تصمیم‌گیری‌های کرملین نقش پررنگی ایفا کرده‌اند./ تلویزیون اینترنتی مدار
گفت‌وگوی کامل در یوتیوب
👇
https://youtu.be/IhdkEI9yI0c
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 49.2K · <a href="https://t.me/akhbarefori/692476" target="_blank">📅 22:52 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692475">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">♦️
نتانیاهو با ترس و لرز عازم نیویورک می‌شود  شبکه ۱۲ رژیم صهیونی:
🔹
نتانیاهو امشب عازم نیویورک خواهد شد و به دلایل امنیتی، زمان پرواز و محل برخاستن هواپیمای «بال صهیون» از قبل اعلام نخواهد شد.
🔹
همچنین محل فرود هواپیمای نتانیاهو هم اعلام نشده است.
📲
🇮🇷
✊
@AkhbareFori…</div>
<div class="tg-footer">👁️ 50.3K · <a href="https://t.me/akhbarefori/692475" target="_blank">📅 22:51 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692470">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/iq5wdbUcN4WM0-6whnZvObj4LWpgYFDLMJwGO4O9svDuRbS9aTZ2v784jtRDFmVV0l7T-wIGAaDfIkryEBc-1f77FevogLUV8USzuZ4HQGQ2pdywnSVS0JDgp9Zja7vSNdU3opWdbZWUFFe2ZxX4lDQDAOgbxVcckGcr2JUedvurV10b3qRNRVmklysoA84xOSXkmovQh4amAuCexkhaVp0Hty5fksfBS1OYp5YN0_RFm9cE3IZOKYMbrzMaD2f3D3p_nNkJOYJLoC878hS6wD-ol9B8N69_5HndY3cLvjajrnk1M1J3Zklk2Fe0QWEqr_Aj3vppkFgfrE2Iv2ovIQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Bv2ivejdtv_bkiu_J3xNVCIZgJ8Y-A5qHT-WTUiVkpptPtuhrzOS6XFjUOxXMrFeONCrKYiQqemED99OfJry3WubBMsUDuocZl1gRowhDGnljJWcbJ2jMVaVmUwl9Oh8vkf_2uR0A9qcHJpd9uls6CaZcTNE61diwK2i_sa7i1_OvttsRkf8WQmGres_IGp0hY2a6DE1hZ2YI36l3Qk5sY490oCXyqrP8aKA6B7x0Soy6fh_ep3Di9Q3u-WXCF7XDbmFreTW4Fp2-Z_fUAPMfs8PuUSM3QIdjcJQd0BTYmWSpyxmK1zhqb74Xz_UB37jBtOj37soiZRnNqfNB39oQQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/X3Y--jMfnQh3-kHUBbpnvryYG2KpnpSoQCiZp6mxqVH_x7WTW7O2E-GsccCz8MluMSFnRLeyNWG1Wr6RBA2ZFY8R5dyV0naDBwuxehoFkOC5KrWITqv03EP_Pd9DpHK7yGq2uXJ-mmpXJK0U-nsG-6piQUxC3nfGKL9QJkSnbgWbNM9GPt_IdZwDgEvtZxcGTJo2Si9IEOT8JYU8L5Bem3ir-c4UTKVL6KMpRHP4tfUieCcd7cf5ELofn2CQdMzfwchn4S0beDuIRQpWrjwaydidr-TTwlL18jgELtgMluhIWTxasyILUtT8aMkBrdKwpUEmh01_eUv9dRms_WH82w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/c6sHvc9MIi1HMAWOE6hvFgXXKtq8DzN9MPo04Z7_sGH7GeoErJivF7_LVH1HNq-nys7kTdt8DwYJJF1-XOccB6rMrrIjLGDoPya3f5_Y0kiW-pG_6eru0SlepieR2_O8RVMxeJ2M3f3jFK8A-xhQ120BxWjM4yje2QoyrghtmhvH85J2hSF-4s1t9e_WuhI-yvwfU2owMzKQHBaLG_SwZpq1rgi_XJVYE-49t06SlWnLDWhO3ZR6FqgQYfDGc2oOJbmwvRYe23bTDue029xZvRKCUd5vRluO1L1TLsfTnlVKn3ZetPqq8wl5Q_MRL49_j1AoG05z3PPuCta66BbQ5A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5a5c1b7e8a.mp4?token=IDcDpL9aVoLlGrAySdxGNoNdMubqM_3rJPcIuL1EKtWW2qVXdy8wMMwV5yzTZM6EZda-k_NQWC7yDu_xdzgPLcLPM5MP8a025UA0e01uEjLQB6-hheZ643d23I62YooUE7r6KkedWeFilr-aQ6d7lAiwIpNBnxxIjsLDqPqMbNEXuoftGvCbq0AoaN6WMZuFVBZWyGM5cuwkvFa8vPlSZya0hR6TfIBeTJ5g-DYrwwNs4vpqk3kM-Bi9PDAcHdUdarppd4_LJpcsh4gRjDwkUHMryHJXWjUEZLwetT2kddXN1ECTuqZIXR_Iwwo4keqrMAa49DvwDiS0QFKspIUa8A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5a5c1b7e8a.mp4?token=IDcDpL9aVoLlGrAySdxGNoNdMubqM_3rJPcIuL1EKtWW2qVXdy8wMMwV5yzTZM6EZda-k_NQWC7yDu_xdzgPLcLPM5MP8a025UA0e01uEjLQB6-hheZ643d23I62YooUE7r6KkedWeFilr-aQ6d7lAiwIpNBnxxIjsLDqPqMbNEXuoftGvCbq0AoaN6WMZuFVBZWyGM5cuwkvFa8vPlSZya0hR6TfIBeTJ5g-DYrwwNs4vpqk3kM-Bi9PDAcHdUdarppd4_LJpcsh4gRjDwkUHMryHJXWjUEZLwetT2kddXN1ECTuqZIXR_Iwwo4keqrMAa49DvwDiS0QFKspIUa8A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
هم‌اکنون فرآیند آماده‌سازی ۱۱۰۰بسته تحصیلی به یاد کودکان میناب برای توزیع در شهرهای جنوبی کشور به مناسبت تولد ۱۱سالگی خبرفوری توسط همکاران این مجموعه رسانه‌ای @AkhbareFori</div>
<div class="tg-footer">👁️ 76.2K · <a href="https://t.me/akhbarefori/692470" target="_blank">📅 22:43 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692469">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-footer">👁️ 46.7K · <a href="https://t.me/akhbarefori/692469" target="_blank">📅 22:40 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692457">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d2a682239e.mp4?token=N9TbIPnOZugGxqdeS1xfoAu_g6Cb4FWuPQrqfJHbH6F0wIq6JVEN1FJVXgoAcVMXuFpHegC0ZFHW8UDqFSr5uJlFmoiKHpo4VxFWXFbreYKqFwo_Syw_lueTbyGIZ8bLHWVla4hZXE5MAbuF_ty9QiaudG4S8ECVM4PxHGtELqACV-9n1BZV3Ikge95Bod4k80xJ7OI11JISb6EshuKNS8MjTZ7u6jjn0SNTai_dCesCwLKBtLrLfTf_VULAY2Ia2Gx-GCr483SFADkdobWgblHJWAduixsEHkztya4rRexEZEnZgCuugJwLiJ41O0sSK7nF5Ef_ycABYvQMqJgn9g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d2a682239e.mp4?token=N9TbIPnOZugGxqdeS1xfoAu_g6Cb4FWuPQrqfJHbH6F0wIq6JVEN1FJVXgoAcVMXuFpHegC0ZFHW8UDqFSr5uJlFmoiKHpo4VxFWXFbreYKqFwo_Syw_lueTbyGIZ8bLHWVla4hZXE5MAbuF_ty9QiaudG4S8ECVM4PxHGtELqACV-9n1BZV3Ikge95Bod4k80xJ7OI11JISb6EshuKNS8MjTZ7u6jjn0SNTai_dCesCwLKBtLrLfTf_VULAY2Ia2Gx-GCr483SFADkdobWgblHJWAduixsEHkztya4rRexEZEnZgCuugJwLiJ41O0sSK7nF5Ef_ycABYvQMqJgn9g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
روح کودکان میناب همراه رئیس‌جمهور بود
🔹
انیمیشن لگویی از سخنرانی پزشکیان در مجمع عمومی سازمان ملل و یادکردن از کودکان شهید میناب
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 48K · <a href="https://t.me/akhbarefori/692457" target="_blank">📅 22:31 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692456">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pzdCNEKDyHLZtQBbQzNPKG_xpK4vv6JgzWNry64AMy9V3K3SQYSDRoTgGuJN-mrHOOuoE63ixfaelyyhPnHLY3LkBtUUZ_89o8kjN-L1QwtvdafcjW52JORDoTAWE-_U7M6nJcqhW-0ELsA9isZGsCkf3HuIW7MsEZqkHEZoGwXd7S2gF5yOYL8hxAYmFl8zrRJwF6oftIqIPqRFegIR1pM-rsD9Gt5sRdMteSQimq9-3_Ypt5CGM9eK1ZEyuuCHNmfLc2iC5j3Pxx7uy6SGCK6YcUXZH0DN8h8i56lW_QnfKnU1MISanKe5pSm9XSbQdK0iTxro9oMUyxuJyuf5tw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
همان درخت، اما در چهار فصل
🍂
🍃
🌸
❄️
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 45.9K · <a href="https://t.me/akhbarefori/692456" target="_blank">📅 22:25 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692444">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/X_wlBDD4EQISbKjLUMYZnaJA9F8YAVQvB7uvANCa29WgIP6Xq15BNjP4QutPgc32PNY-ACVtliyhMeMiUUkn6S83FR5OPckOHcmnLFH-onPGWxV4jMqb9MxZgmmGhixPVNea9cbe3p2Qy2qCzRmqesrc9aduW80bhOIFb8Hn5BHp6R-ucUtXwLl3htC-Z3dZMB3PWleqgVlggPbtaMMHbZRj5KlOPoi9yS5CYGPujbZa5faCfm8QYiMraOVMd3tKW4_0bJIeyECBo-8uv5V5dH_2wbc9T5s6ZgGU8lm8wC-mKPDigaQJOLSpVOCwDjFH7yuEWao1wyxa58drFxnufw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
افزایش دستمزد کارگران بیش از نرخ تورم، از دستاوردهای میدری است
🔹
اکبر شوکت، عضو هیئت‌مدیره کانون کارگران ساختمانی کشور، با دفاع از عملکرد احمد میدری، وزیر تعاون، کار و رفاه اجتماعی، گفت: در دوره حضور میدری، افزایش دستمزد کارگران بالاتر از نرخ تورم انجام شد و انجمن‌های صنفی کارگران ساختمانی که در دولت قبل متروک شده بودند، احیا شدند.
🔹
او همچنین از احیای بیمه‌های قطع‌شده کارگران ساختمانی، سرعت گرفتن روند برقراری سهمیه بیمه و توقف پرونده‌سازی برای انجمن‌های صنفی خبر داد.
🔹
شوکت با اشاره به طرح استیضاح وزیر کار نیز گفت: بهتر بود پیش از طرح استیضاح، نظر نمایندگان مجامع کارگری و کانون‌های بازنشستگی در استان‌ها دریافت می‌شد.
🔹
وی همچنین حمایت وزارت کار از اجرای کالابرگ و اصلاح ساختار یارانه‌ها و دهک‌بندی‌ها را از دیگر اقدامات این وزارتخانه عنوان کرد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 48K · <a href="https://t.me/akhbarefori/692444" target="_blank">📅 22:22 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692443">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FKe_4Fe1_zLvfOY1BFPzB0npJ76EZJwC_4MN8m8cU6n9bYGOnKZVJZD3VdSEi3EUpn3dDUYFW8TM_jFRpQasbBwoypoMKMr-0zZsS4guE6il52iHC7uqxQrwwM9Ftk7iubfhCJavb_2FwJ-mCRLqgsRj6kGFoUTeEMf4LJ-owrkd64hX4JXhRAYjwg3GShtUkANCEXNsIddlI05l_x7kflMCqvYGplSbNklT9-DtY5UOoU6DPyMAbKEQKAY9OoY6ttJ82mC3N55gEnxZQb6hC-pPrCZ65Va5Orp84ZBuqGrKs1jiNggk3i4OlW4SpSEW19NeFQbl99IfaNhqw6jovw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
نفت برنت ۱۰۰ دلاری شد
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 47.5K · <a href="https://t.me/akhbarefori/692443" target="_blank">📅 22:21 · 01 Mehr 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>

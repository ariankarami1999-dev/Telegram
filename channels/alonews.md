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
<img src="https://cdn4.telesco.pe/file/I3wwY59EwyQschm8mCui56P2nXu8-o_BY7UETGxAtT3-qcCE0nYJMErFeXddiGjAMjgZ6zgQip1ZTHWUO480Oi414uVaMk3CVRzv81D2ZmUO3PVkVBAeuaOBfKxhZa7tFaHfUrGlDneDrvpqfqp9ibhkDB2uE3SXaIn64hEhNMvXOjzNB2n4aM1YsUtwmTKhkNehbUiSJDUzmCRHJ6Uj0FggQup31Fx2g8hm_bY6SNxEroqegudLAMwxElQgya5ZsfxAfDMAr9d0qehmmlUmC5VGt-Gh0EkOc4sUPoTS7QL4W2hxTJ63fh80HXT5zyOgdCWLm9l0sEMGXflqXvu9DA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 اخبار جنگ الونیوز AloNews</h1>
<p>@alonews • 👥 946K عضو</p>
<a href="https://t.me/alonews" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 با الونیوز از اخبار جنگ و وقایع در چند ثانیه مطلع باش!اخبار جنگ بدون سانسور در الونیوز👌پشتیبانی کانال🕵️https://t.me/AloNews?directادمین کانال🎩@AloNewsBotجهت رزرو تبلیغات👇https://t.me/ads_alonewshttps://t.me/ads_alonews</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-02-30 14:55:14</div>
<hr>

<div class="tg-post" id="msg-121276">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">👈
امارات به عراق هشدار داده جلوی اقدام یا حمله‌ای که از خاکش علیه دیگر کشورها انجام میشه رو بگیره
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 964 · <a href="https://t.me/alonews/121276" target="_blank">📅 14:53 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-121274">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7d1cc9d932.mp4?token=DVQu5yBcI9Z3PnTrAKpqn6xHed3ZJZx_ION0isLmOhaWeNbx2xdYuwrJaE0A7AWVy6KZQG40DySLfVxArZFyMQi_kyLHUOy6b6VKYAjtRYFvE2fVoizYXLh6cv__r4pM0ZJkXJJokHxxGk3AaomLTVlF9e4jLXojQznZ7UibjIL43reM3Z3AoJYW3YzSo1w1UyqqQxYoVswr4A-OhxC5LtaFCBwITSlN27gkkXYXbEbuzu6KKK7V8adUoU0M0mqkkTk2CD5GnHqcer7NSisK8PBRpjBQe6rpmoHH_xSWGv86684OCig3SIcJzsuQwipdWum0NuWOvXldSVa4bKFHMw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7d1cc9d932.mp4?token=DVQu5yBcI9Z3PnTrAKpqn6xHed3ZJZx_ION0isLmOhaWeNbx2xdYuwrJaE0A7AWVy6KZQG40DySLfVxArZFyMQi_kyLHUOy6b6VKYAjtRYFvE2fVoizYXLh6cv__r4pM0ZJkXJJokHxxGk3AaomLTVlF9e4jLXojQznZ7UibjIL43reM3Z3AoJYW3YzSo1w1UyqqQxYoVswr4A-OhxC5LtaFCBwITSlN27gkkXYXbEbuzu6KKK7V8adUoU0M0mqkkTk2CD5GnHqcer7NSisK8PBRpjBQe6rpmoHH_xSWGv86684OCig3SIcJzsuQwipdWum0NuWOvXldSVa4bKFHMw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
حزب‌الله از داخل ساختمونای غیرنظامی نیروها رو زیر نظر داشته
🔴
نیروهای یگان چندبعدی اسرائیل هم به تجهیزات دیده‌بانی حمله کردن
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 3.82K · <a href="https://t.me/alonews/121274" target="_blank">📅 14:43 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-121273">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">👈
صدا و سیما: ۵ ابرنفتکش برای گذر از تنگه از نیروی دریایی ما اجازه گرفتن
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 4.12K · <a href="https://t.me/alonews/121273" target="_blank">📅 14:42 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-121272">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/41b2997c91.mp4?token=h49sgTjVPxb6jKViBd1Zb6feoU2Vr6dwi671ePu0TrkZ5yBDTCmKlUGyRMwlax1WopCwe2Bu7gtXGc-6Y662I-Bu0IArbGyabs8PojCqM3b5RfUUx9he4DqDCo4KBPtrv12xKYyuyUnpIV9l6FS9Bw3sHZhWtfMmpWk5szBFiHC5iYR9G8tmOigOPmRjzROB-AP9VLZWQYHKEfm5NQCm6sQOWVwWF3S-jvck1RZ2WZQnaOi6kUHfuRUU9vOH_XE3ZlHSYVzWtjTwDT-aMTpr00rvoXlgFXZAjmyXG2E4qhOo57xYpVmFpgTNj1PqSDh3hPq7Hgbi4K4rxb6XEGdHz4WOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/41b2997c91.mp4?token=h49sgTjVPxb6jKViBd1Zb6feoU2Vr6dwi671ePu0TrkZ5yBDTCmKlUGyRMwlax1WopCwe2Bu7gtXGc-6Y662I-Bu0IArbGyabs8PojCqM3b5RfUUx9he4DqDCo4KBPtrv12xKYyuyUnpIV9l6FS9Bw3sHZhWtfMmpWk5szBFiHC5iYR9G8tmOigOPmRjzROB-AP9VLZWQYHKEfm5NQCm6sQOWVwWF3S-jvck1RZ2WZQnaOi6kUHfuRUU9vOH_XE3ZlHSYVzWtjTwDT-aMTpr00rvoXlgFXZAjmyXG2E4qhOo57xYpVmFpgTNj1PqSDh3hPq7Hgbi4K4rxb6XEGdHz4WOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
بن‌گیور، وزیر امنیت ملی اسرائیل، از فعالان بازداشت‌شده در کاروان جهانی صمود غزه در بندر آشدود بازدید کرد.
🔴
به اسرائیل خوش آمدید، ما اینجا در کنترل هستیم. این همان چیزی است که باید باشد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 5.08K · <a href="https://t.me/alonews/121272" target="_blank">📅 14:37 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-121271">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">👈
کنست به انحلال خود و برگزاری زودهنگام انتخابات رای داد
🔴
کنست در جلسه مقدماتی خود با اکثریت ۱۱۰ عضو و بدون هیچ مخالفتی، به لایحه انحلال خود و جلو انداختن تاریخ انتخابات رأی داد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 6.96K · <a href="https://t.me/alonews/121271" target="_blank">📅 14:30 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-121270">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">👈
رئیس مرکز رسانه مجلس: ادعای کناره‌گیری قالیباف از سرپرستی تیم مذاکره‌ کننده، کذب محض و دروغی آشکار است
🔴
این ادعا امتداد همان خط تخریبی است که تا دیروز فرماندهان را نشانه می‌رفت و امروز شهدای والامقام را
🔴
البته از جریانی که سابقه هجمه به فرماندهان نظامی، دفتر مقام معظم رهبری و مراجع عظام تقلید را در کارنامه دارد، رفتاری غیر از این انتظار نمی‌رود.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 9.75K · <a href="https://t.me/alonews/121270" target="_blank">📅 14:15 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-121269">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">👈
پوتین و شی جین‌پینگ : جنگ ایران باید سریع متوقف شه
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/alonews/121269" target="_blank">📅 14:11 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-121268">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">👈
رسانه عبری وای نت: امارات هماهنگی‌های امنیتی و عملیاتی با اسرائیل را تشدید کرده
🔴
این اقدام به منظور آمادگی برای سناریوی احتمالی بازگشت به نبرد علیه ایران صورت گرفت
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/alonews/121268" target="_blank">📅 14:03 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-121267">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">👈
یک منبع بلندپایه دیپلماتیک گفت:
فضای بی‌اعتمادی هماهنگی‌های میان ایران و پاکستان را تحت تاثیر قرار داده و همکاری‌های فشرده دو کشور طی دو هفته گذشته اکنون متوقف شده است.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/alonews/121267" target="_blank">📅 14:00 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-121266">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">👈
مقامات آلمانی دو شهروند آلمانی را به اتهام جاسوسی برای سرویس اطلاعاتی چین دستگیر کردند، دفتر دادستان فدرال آلمان گفت.
🔴
متهمان، که به عنوان شواچون و هوا شناسایی شدند، اطلاعاتی در مورد محصولات با فناوری بالا با کاربردهای نظامی جستجو کردند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/alonews/121266" target="_blank">📅 13:57 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-121265">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">👈
خبرگزاری قوه قضائیه: رشید مظاهری، بازیکن سابق فوتبال، هنگام خروج غیرقانونی از کشور دستگیر شده. پیگیری‌ها نشون میده این فرد قصد داشته با تغییر چهره و پول دادن به ماموران مرزبانی، از مرزهای غربی به صورت غیرقانونی از کشور فرار کنه، ولی موقع خروجش دستگیر شده.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/alonews/121265" target="_blank">📅 13:54 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-121264">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1d731a2a6c.mp4?token=vGdpqOer6_mR4Wmk1WnII2rTEl_aOvl81SS0XGPokVxa2Xn9ochSyxGxMkr-jurZUfNeL17j6WAZzZzxrEuLVB1M4YTv0-BkWRgDlnrOAA0k3N3e8hVoBhWJXoyFfXXayz9UKdggBFnTB3S-LMvJgi-LxNm1jY7SkcPFdy0ITKSOZDpj9pgt7oDKTycVlJdD6VJVgIxfkbtZgoPiQkwfT1xy18iQrB-TWj_B6UcIhYEuRYcOfl5CrYbFX-VcugNNlPxl1WI5vKDekfUjpC-qxtIKyezvQg1JQorZwtkP6_32wM_QTm_Egw-oCch4Vfu1K7d-689XwtFAR1N-vJkHNQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1d731a2a6c.mp4?token=vGdpqOer6_mR4Wmk1WnII2rTEl_aOvl81SS0XGPokVxa2Xn9ochSyxGxMkr-jurZUfNeL17j6WAZzZzxrEuLVB1M4YTv0-BkWRgDlnrOAA0k3N3e8hVoBhWJXoyFfXXayz9UKdggBFnTB3S-LMvJgi-LxNm1jY7SkcPFdy0ITKSOZDpj9pgt7oDKTycVlJdD6VJVgIxfkbtZgoPiQkwfT1xy18iQrB-TWj_B6UcIhYEuRYcOfl5CrYbFX-VcugNNlPxl1WI5vKDekfUjpC-qxtIKyezvQg1JQorZwtkP6_32wM_QTm_Egw-oCch4Vfu1K7d-689XwtFAR1N-vJkHNQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ابوالفضل ظهره‌وند، نماینده مجلس : اگه دشمنامون بیان رهبرامونو ترور کنن
🔴
ما هم باید جوابشونو با ترور رهبرای اونا بدیم، نه اینکه بریم پای مذاکره
🔴
اگه آمریکا بخواد تو آینده رهبرامونو بزنه، ایرانم باید واشنگتن دی‌سی رو بزنه
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/alonews/121264" target="_blank">📅 13:49 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-121263">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">👈
سقوط قیمت طلا به پایین‌ترین سطح یک ماه و نیم اخیر
🔴
هر اونس با ۰.۴ درصد کاهش، ۴۴۶۴ دلار معامله شد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/alonews/121263" target="_blank">📅 13:46 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-121262">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">👈
بریتانیا برخی تحریم‌ها علیه روسیه را با اجازه واردات دیزل و سوخت جت تصفیه شده از نفت خام روسی در کشورهای ثالث به بریتانیا، کاهش داده است.
🔴
این معافیت که امروز اجرایی شد، از طریق مجوزی دولتی صادر شده که «به صورت نامحدود» معتبر خواهد بود، مشروط به بازبینی دوره‌ای توسط وزیر تجارت.
🔴
برخی محدودیت‌ها بر حمل و نقل گاز طبیعی مایع شده روسیه نیز برداشته شد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/alonews/121262" target="_blank">📅 13:42 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-121261">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rU6r_cuuGAJpFVNw9gGCnLa1WWGHyPiC4fPZPoBIdGz59MEceenEJdxyZDxHjZ-SxtCF2adbCdXcc8_yemayKctAxUXA5L2nu5GRUlIQ3gLfGrAi2xRxGmrEAHfe7TC9Y2vDbuLLzaXGZOF3QtBcGEdsFNsu9kxdZKw_vhEY_31WAE1s5hsdhxMbHmx5M78i_HqFVQMDxwEI_5SPGBIfjfCSUfM6UWZAubS8jbNUgulbgpP9aNyZm4zJiWDt8_mOPq4qrBwC094lBb05HnDLPBUozbwN4XFlaV37szmUW2iXoAAHz5TH7NEpEoSHTaP-nEzAAm0XsEkTzSC4nKsdrA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قیمت استثنایی گیگی
9️⃣
8️⃣
1️⃣
تحویل زیر یک دقیقه
✅
دارای لینک سابسکریشن جهت دیدن حجم و کنترل مصرف
✅
بدون قطعی
✅
بدون محدودیت کاربر و زمان
✅
جمینایو چت جی بی تی و... کامل اوکیه با سرورامون
✅
🏪
پشتیبانی کامل
✅
شروع فعالیت از سال 2022
✅
پرداخت ریالی
✅
ضریب و این چیزا ندارن و تا آخرین مگابایت برای پشتیبانیش درختمتیم
🥂
💤
این تخفیف فقط تا ۱۲ شب فعاله
💤
⭐️
@Napsternetiran_bot
〰️
〰️
〰️
〰️
〰️
〰️
〰️
🔶
@Napsternetvirani</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/alonews/121261" target="_blank">📅 13:37 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-121260">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">👈
وزارت خارجه آمریکا تا سقف ۱۵ میلیون دلار پاداش برای اطلاعات در مورد شبکه مالی سپاه پاسداران تعیین کرد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/alonews/121260" target="_blank">📅 13:27 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-121259">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">👈
گروسی: برای تضمین امنیت هسته‌ای به خلیج فارس سفر می‌کنم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/alonews/121259" target="_blank">📅 13:20 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-121258">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">👈
دبیرکل ناتو: ایران با بستن تنگه هرمز، اقتصاد جهانی را گروگان گرفته است
🔴
مارک روته، دبیرکل پیمان آتلانتیک شمالی در اظهاراتی علیه ایران گفت: این اتحاد و جامعه بین‌المللی دستیابی ایران به سلاح هسته‌ای را رد می‌کنند. بسیاری از کشورها در ایجاد ائتلافی برای تضمین آزادی دریانوردی در تنگه هرمز مشارکت دارند.
🔴
ما در مورد حمایت از متحدان خود در منطقه خلیج فارس بحث خواهیم کرد.  کشورهای اروپایی، علاوه بر کانادا، از همان روز اول با گشودن پایگاه‌های نظامی به روی هواپیماهای آمریکایی، از ایالات متحده در عملیاتش علیه ایران حمایت کردند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/alonews/121258" target="_blank">📅 13:12 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-121257">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">👈
بنیات از اول خرداد ۲۰ درصد گرون میشه
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/alonews/121257" target="_blank">📅 13:08 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-121256">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ub9ZZZSx-Qq3n9--JfyUoCfU2zlDTK_R_cIVmSSsRLQoQCvHRzqUDT5YWGvZoHxJfAOktnDRKElCmRJH8E1UGxdFI7dQA0XGL5xaf0bsxs0H1CNVw3OWI7xs_yaZBl0U6XIGEctR_IsDfNpaRrFobGlXdRdw1h1WEc7t_9xQbRV7lBWu2gwf8TtWgfLWpLefd_vOHrmDEGuGozNokudKL042h0hXD5kEQEab4AxPwlNFXtaUrKybE-KbGfdA0UgVHE7dOEjloXEiN9RY9z77NVaxoM6xcqP0mIJvFNnIhJm7l3iIh5u56JJVm7UEVNmH14kJCyPQybwF-TPIvoynWQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
اعلام قیمت نهایی خودروی وارداتی لکسوس LX600
🔴
110 میلیارد تومان...!
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/alonews/121256" target="_blank">📅 13:04 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-121255">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">👈
نفوذ پهپاد به حریم هوایی اردن
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/alonews/121255" target="_blank">📅 13:00 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-121254">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/be63a69a09.mp4?token=Y7CU-HShHEZeF2wIxeCKFZ-O5dS9tEgyq9yAe1uMNDEKqpA5nmQ4Z6qtRu4SELb3DugjeM62iGNfJDikTT7Q4t5xaAV6P2A0kotvh1cxlKFUMG_M6kYHGJWtzulMfq8jyeJ0oTATU1UtGaPgMC8cg_V5XH_oQhQt1NXZmyWMChqC3npcYIbuUiS_yW9BHpgqQOkMBCFW9xtmvDVfV7SRLaUQ5COMPDDHyGCWaBzJ0q6WwRn1PYlSzfnuDI2P93dsEEcTGrG_oX2G3Ljuy_I0KPAxppjkmyXEY7HCuxoCR-bYrWHdSXAJU8zEXH-evrX1JT8VBRjCScRCrnbspOJ1bA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/be63a69a09.mp4?token=Y7CU-HShHEZeF2wIxeCKFZ-O5dS9tEgyq9yAe1uMNDEKqpA5nmQ4Z6qtRu4SELb3DugjeM62iGNfJDikTT7Q4t5xaAV6P2A0kotvh1cxlKFUMG_M6kYHGJWtzulMfq8jyeJ0oTATU1UtGaPgMC8cg_V5XH_oQhQt1NXZmyWMChqC3npcYIbuUiS_yW9BHpgqQOkMBCFW9xtmvDVfV7SRLaUQ5COMPDDHyGCWaBzJ0q6WwRn1PYlSzfnuDI2P93dsEEcTGrG_oX2G3Ljuy_I0KPAxppjkmyXEY7HCuxoCR-bYrWHdSXAJU8zEXH-evrX1JT8VBRjCScRCrnbspOJ1bA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
گزارش‌هایی از یک رویداد با تلفات انبوه در شهر دویر در جنوب لبنان پس از یک حمله هوایی اسرائیلی که حدود ۳۰ دقیقه پیش منطقه را هدف قرار داد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/alonews/121254" target="_blank">📅 12:59 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-121253">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">👈
وزیر کشور پاکستان عازم تهران شد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/alonews/121253" target="_blank">📅 12:55 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-121252">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">👈
وزارت خارجه کره جنوبی اعلام کرد: کشتی تحت مدیریت این کشور پس از مشورت با مقامات ایرانی، با خیال راحت از تنگه هرمز عبور کرد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/alonews/121252" target="_blank">📅 12:50 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-121251">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">👈
بحرین : نیروهای ما تو حالت آمادگی رزمی "کامل" قرار داره
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/alonews/121251" target="_blank">📅 12:46 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-121250">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">👈
«امارات متحده عربی به آرامی با پاکستان تماس گرفته و به دنبال درگیری مجدد است.
🔴
این حرکت پس از یک درک آشکار میان تصمیم‌گیرندگان اماراتی رخ داده است که پاکستان کشوری بسیار مهم است که نباید در سمت اشتباه قرار گیرد.
🔴
همچنین تغییری در سیاست امارات وجود دارد. برخلاف موضع قبلی خود، ابوظبی اکنون دیپلماسی را برای حل تعارض ایران-آمریکا ترجیح می‌دهد،» - کامران یوسف از شبکه جهانی تی‌آرتی و اکسپرس نیوز پاکستان.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/alonews/121250" target="_blank">📅 12:41 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-121249">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">👈
مقامات بحرین دو تبعه مصری را به اتهام ابراز همدردی با جمهوری اسلامی ایران به ۱۰ سال زندان محکوم کرده‌اند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/alonews/121249" target="_blank">📅 12:37 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-121248">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">👈
رشد ۴۲ هزار واحدی شاخص بورس در دومین روز بازگشایی بازار
🔴
شاخص کل بورس با رشد ۴۲ هزار واحدی در پایان معاملات امروز به ۳ میلیون و ۷۵۸ هزار واحد رسید.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/alonews/121248" target="_blank">📅 12:36 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-121247">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">👈
رسانه‌های اسرائیلی: ترامپ و نتانیاهو دیشب تماس تلفنی طولانی داشتند که به عنوان تماس محوری توصیف شده است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/alonews/121247" target="_blank">📅 12:31 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-121246">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">👈
طبق مصوبه جدید کارگروه تنظیم بازار، قیمت انواع چای به‌صورت دوره‌ای تعیین و اعلام می‌شود و دولت بانک مرکزی و چند وزارتخانه را مکلف به کنترل بازار چای کرد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/alonews/121246" target="_blank">📅 12:25 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-121245">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">👈
الجزیره: اکثریت روس‌ها دیدار روسای جمهور روسیه و چین را تحول آفرین نمی‌دانند، بلکه آن را گامی مهم برای تقویت روابط اقتصادی می‌بینند
🔴
برای بسیاری از مردم روسیه ملاقات پوتین و زلنسکی، قطعاً حیاتی‌تر از این دیدار است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/alonews/121245" target="_blank">📅 12:22 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-121244">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/d355e12d20.mp4?token=nqMj3Ew5dOVcao6D3Vlncv2wz1BDt_C_xjDrOYubTJicMk3eK5o9bbq7wLpONPYr8n6yKoBpA_2HMNfcIT3xSg07S29oWSEUvOQPZkqNhGaDNlI9mwiabCUSR76wkUP8ZjmNnU6v2K0nn47zWTGnnSPAi8FaN9pG3csH1HmlX6f1tTdYnegRf3CKf50Jt8g5jQogegbhCjqgeHJDXqStDnofa5DfvxKgPMl4i2_P3vEvvxwnC5_zoSQCIumvl6xRaVK129TwtaWtPM-XRACo8byF9XC5K2eP1M6bkQVeBo06D3wa86w5gjFj8gNslE0_ZI5ZqgIXXXHeKWCExahAfA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/d355e12d20.mp4?token=nqMj3Ew5dOVcao6D3Vlncv2wz1BDt_C_xjDrOYubTJicMk3eK5o9bbq7wLpONPYr8n6yKoBpA_2HMNfcIT3xSg07S29oWSEUvOQPZkqNhGaDNlI9mwiabCUSR76wkUP8ZjmNnU6v2K0nn47zWTGnnSPAi8FaN9pG3csH1HmlX6f1tTdYnegRf3CKf50Jt8g5jQogegbhCjqgeHJDXqStDnofa5DfvxKgPMl4i2_P3vEvvxwnC5_zoSQCIumvl6xRaVK129TwtaWtPM-XRACo8byF9XC5K2eP1M6bkQVeBo06D3wa86w5gjFj8gNslE0_ZI5ZqgIXXXHeKWCExahAfA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
مراسم عروسی جان فداها: عروس رفته تنگه هرمز گل بچینه!
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/alonews/121244" target="_blank">📅 12:17 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-121243">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rOn42s4cFHkuRMX42eltbnw9h6DhdO-8lfTjCDZ8yqJdSp1-hLcFfU6svnxOnTKm6nicUF20dwRxOk8uDA2tH8Yan-5Du3GBmF7fQr1tOkdqShb-SpaX21F371Ao77DOysN6CRtAHaoJkcNRnzQ1qXDbgld_U41-XQWFfrgPFQWCFV96GvcIx4ckhVejvyCScjAeHyujg5FroG0oAnKzz3YqgoyHS0e7kqa9ERmPGUb_zeSskpD2AUJdmN1uyeUvXdTvhPbEQ4KiLdBbCWSV2jY-Xrln2frdkZaJADmyBeyXnJh2ChouObQD-8i_Uoo6A77CR82zWsPLl57cBmJUjg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
حملات اسرائیل به جنوب لبنان
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/alonews/121243" target="_blank">📅 12:13 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-121242">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">👈
فرمانده سنتکام دلیل خروج ناوگروه «جرالد فورد» از خاورمیانه را اعلام کرد
🔴
«برد کوپر»، فرمانده ستاد فرماندهی مرکزی آمریکا (سنتکام)، علت خروج ناوگروه «جرالد فورد» از منطقه خاورمیانه را تشریح کرد.
🔴
دریاسالار کوپر عنوان داشت که «نیازی به حضور همزمان سه ناوگروه حامل پرچم در خاورمیانه نبود.»
🔴
وی افزود که ناوگروه‌های «جورج بوش» و «آبراهام لینکلن» همچنان در منطقه حضور دارند. کوپر گفت: «نیازی پایدار به وجود سه ناو هواپیمابر در منطقه احساس نمی‌شد.»
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/alonews/121242" target="_blank">📅 12:08 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-121241">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/X6R7qvrVpWeL291BKl6FWOMRjAURDfatz856p3vf_AIwD3KmDyvHwbfb07ZTj5zcQhif6yA27ataNuwBu4bNZfjkmnO3WNAKiIgkOHdRGXZ4o2stSQ5_NlzsMst5eXNpjXDf8NT8lDLXCBo5aSMvea7uABN4uig970UlwK4KCqLf5kytbyKViM7khnROutm4Vjic_ODM4IA_whqLmdpBj2Ke3rk6Qtw9NawMkmF-vU3Ekwo9I8EVFfGKp3w3wBC940bDQQzOw8Nd2ZJkWcKIQIKiG3WOTH5nX7aIAiFbpKtXgdTgFF3DxdyTGnopFbQC22yWM8Wj8ojoAZV0rV05jQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ارتش سوریه با یک واحد اصلی در تمرین نظامی EFES-2026 ارتش ترکیه شرکت می‌کند.
🔴
این اولین بار است که نیروهای سوریه از زمان تغییر حکومت در یک تمرین نظامی خارج از سوریه شرکت می‌کنند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/alonews/121241" target="_blank">📅 12:05 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-121240">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3d10e5ea2d.mp4?token=RpQY0Sp6hPe_Z3oZAF7RmNBO2GPK63x7CUv6YSz05ea2P6lCsq6DJ3AslYBic_OPq_YZaZ-P-vXe0sL98Q0jB0mMhcX-vLJrDRBE0btG3Y6JROrWQTzuEaiSsE1vdEwGaOQjDXG5xaXVB6oRhiwiprc0SCJ1lbpA3JgN_8d0VLZxtvwbCOb7q5cXo-HRPZx2M84RHxk_W2_qQG0qPTCh97cVxs7BP81GIs_sslvqCX9T8ADBmaPFqSj41iFRX3mdPkVYyBSoFwviqzZgbg3u8c9_q99K4o1TIV6bVRMn79nkBkGcbLa2KyIPhnaxgFB4isIuYb4WKtUCQZ21KfI22Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3d10e5ea2d.mp4?token=RpQY0Sp6hPe_Z3oZAF7RmNBO2GPK63x7CUv6YSz05ea2P6lCsq6DJ3AslYBic_OPq_YZaZ-P-vXe0sL98Q0jB0mMhcX-vLJrDRBE0btG3Y6JROrWQTzuEaiSsE1vdEwGaOQjDXG5xaXVB6oRhiwiprc0SCJ1lbpA3JgN_8d0VLZxtvwbCOb7q5cXo-HRPZx2M84RHxk_W2_qQG0qPTCh97cVxs7BP81GIs_sslvqCX9T8ADBmaPFqSj41iFRX3mdPkVYyBSoFwviqzZgbg3u8c9_q99K4o1TIV6bVRMn79nkBkGcbLa2KyIPhnaxgFB4isIuYb4WKtUCQZ21KfI22Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
شی جین‌پینگ: رئیس‌جمهور پوتین قبلاً برای بیست و پنجمین بار به چین سفر کرده است
🔴
این به خودی خود نشان‌دهنده سطح بالا و ماهیت خاص روابط چین و روسیه است.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/alonews/121240" target="_blank">📅 11:57 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-121239">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fcd06da20a.mp4?token=bH4FuD-QrRfl1cozUI6I7iRDRdX4JrIj9k5RMN1kbfOmVWQhnkGEjSax1u5VtdLOATtS12KqosHSjTPToYq-RESpT_zgorejXuQ9HWLnWD3Tyk2C4ikzc5Q0Td2AmxzyGLCYRvg2FGos3H2fpurfVkQvKtJJjdInxOJ_g5YRF-4yiTyXXTSo-OcSwLJaSjgEiSeVh3OOtRnViQIN6o4nF3d9Xqgug7pki8VDIHkY6us4A8yT8Vhp6pYpuBq2ULGvsf2caLG1rwX3IQ7CbNYA1wbpLG4_ci2qgpzqIqW9HslLuNna5WX0LT-eCspxkImZdL-bgwrSm3UZRNo0zUDZKQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fcd06da20a.mp4?token=bH4FuD-QrRfl1cozUI6I7iRDRdX4JrIj9k5RMN1kbfOmVWQhnkGEjSax1u5VtdLOATtS12KqosHSjTPToYq-RESpT_zgorejXuQ9HWLnWD3Tyk2C4ikzc5Q0Td2AmxzyGLCYRvg2FGos3H2fpurfVkQvKtJJjdInxOJ_g5YRF-4yiTyXXTSo-OcSwLJaSjgEiSeVh3OOtRnViQIN6o4nF3d9Xqgug7pki8VDIHkY6us4A8yT8Vhp6pYpuBq2ULGvsf2caLG1rwX3IQ7CbNYA1wbpLG4_ci2qgpzqIqW9HslLuNna5WX0LT-eCspxkImZdL-bgwrSm3UZRNo0zUDZKQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
تصاویری از  لحظه وقوع انفجار روز گذشته در دمشق
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/alonews/121239" target="_blank">📅 11:55 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-121238">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">👈
بیانیه مشترک چین و روسیه:
ما از طرف‌های درگیر در خاورمیانه می‌خواهیم که وارد مذاکره شوند.
🔴
هیچ کشوری یا مردمی درجه یک نیست و سلطه به هر شکلی غیرقابل قبول است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/alonews/121238" target="_blank">📅 11:51 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-121237">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">👈
دو نفتکش چینی پس از دو ماه معطلی در خلیج فارس، روز چهارشنبه از تنگه هرمز عبور کردند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/alonews/121237" target="_blank">📅 11:47 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-121236">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">👈
کشت خشخاش ممنوع شد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/alonews/121236" target="_blank">📅 11:43 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-121235">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">👈
پژمان جمشیدی از اتهام آدم ربایی و تجاوز به عنف تبرئه شده و به دلیل رابطه نامشروع به ۹۹ ضربه شلاق محکوم شده
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/alonews/121235" target="_blank">📅 11:38 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-121234">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dImrfMTGQZwYM1BY29q5gLpazpsimrakwuBq_fJ8Vfqx4yJnNqbR0vWGGKo_9jITU4zFl31vUv5YFyDNXOgV--9p-LP7AKDjD-v7H69lW1UPS5Kx7l4ODCZ6ETi0Dl7p2jQTu41ko8GCtptPCOulNaii7kcXi9tuW0zXS3RfmNgJI61f_9oH2D17qOx14L9jhPlnwMs0ZqNmPq6_bhC6GzJ0w0x3Thx7-2irZcIdTcL6C4q8F6BQBE1MTmQHcsmAVbKeoRs4qL6yLFtQ8fOhEzRSdLq4FzhG1Wxgt9eO-Fv72k9TOsw1_f4uae1DgMQMNs2Tpzn7U-WrYio3tv9L1w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
علی قلهکی، فعال رسانه‌ای: چین دیگر تمایلی به حفظ وضعیت فعلی تنگه هرمز توسط ایران ندارد و بنظر می‌رسد به زودی در بحث تنگه هرمز رودروی ایران قرار گیرد؛ آنها معتقدند ایران باید زودتر تنگه را «تعیین تکلیف» کند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/alonews/121234" target="_blank">📅 11:32 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-121233">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">👈
گویا بخشی از اموال توقیف شده علی کریمی بدون مزایده به یک شخص دیگه واگذار شده!!!!
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/alonews/121233" target="_blank">📅 11:28 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-121232">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">👈
وزارت خارجه روسیه: ایران از «پیمان منع گسترش سلاح‌های هسته‌ای» (ان‌پی‌تی) خارج نخواهد شد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/alonews/121232" target="_blank">📅 11:23 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-121231">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">👈
الجزیره: پوتین در پکن همان استقبالی که از ترامپ شد را دریافت کرد
🔴
تنها تفاوت در این بود که چه کسی در فرودگاه از او استقبال کرد؛ این فرد در مورد ترامپ، معاون رئیس‌جمهور بود و برای پوتین، وزیر امور خارجه
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/alonews/121231" target="_blank">📅 11:19 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-121230">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tkC3lU2u1nNzN_uuIGBOWZpZkJDLz2hungzHiLrWEjqZS4oAPBiKT6ih8Zhi8Nwo6cbCdPpdkPosLLxo6xK1kROTfRbFnNM1dmFLjlbD9GIIwxZqbhpTVS68IKfJpVLofYLRce6jqBGbLzPjjpeBCDgEM7W2n-lXg4LIuahjd4tB7ZTCqLqPKM8PJTMjKPF_olF0D5cI1M3aS9o4id1dBo08hTaj8qnL_hsqSzK7Yf8vV6QbT8U3Mj5eVqFUgl6OiPnWkyrpqExH1m6nsK8n-bpnvJLQXQfDrgoNgOQEuosZ6nh6u_34e0TR4m5B8zDYzalwa6QaVNpBJerfz9ppuA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
شبکه ۱۲ اسرائیل :
- اسرائیل و آمریکا برنامه ریزی کردن احمدی‌نژاد رو به‌عنوان رهبر ایران سر کار بیارن
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/alonews/121230" target="_blank">📅 11:15 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-121229">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">👈
سپاه پاسداران: با تکرار تجاوز دشمن، جنگ را فرامنطقه‌ای می‌کنیم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/alonews/121229" target="_blank">📅 11:13 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-121228">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">👈
پل مرقص، وزیر اطلاع‌رسانی لبنان در مصاحبه با «العربیه» گفت: «رئیس‌جمهور لبنان خواهان تثبیت آتش‌بس جهت موفقیت روند مذاکرات است.»
🔴
او افزود لبنان با هدف دستیابی به حقوق حاکمیتی خود با ایالات متحده آمریکا همکاری می‌کند.
این وزیر لبنانی در ادامه گفت نبیه بری، رئیس پارلمان لبنان، «لحظه‌به‌لحظه» در جریان مذاکرات با اسرائیل طی دو روز گذشته قرار داشته است.
🔴
مرقص افزود مذاکرات با اسرائیل با هماهنگی قانونی رئیس‌جمهور و نخست‌وزیر انجام می‌شود.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/alonews/121228" target="_blank">📅 11:09 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-121227">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XdjqP6O7g8WU8FGVPVG0smC3zabECWPvFv8s36YuTvgLZZUTmmeJzZDOU4-ln9D_G3otDbpnvF_UdZwq1NekEgN82ikLgMFalGSXqIofOZFfNGEYCADPDe9_0H352GTJ-kTei8vlIr35lqXG1Ng54I3_g9aaRcQj836KV-nRXG48GJMEk4RImBY0uX16D701UKuhpTsUmwCjw0subr3BLkl-GBxb3cL2T21htfomAtmroPx17z2jJsCkvwMzffGn9O9C6sT5B8alauFVvOiLoH_iSTQL-FP5ZWpwhQ1wH_pmw1kEkpyRjwiYypn4FMRfzKvbDbojPi8EHQMTUqRBnw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
رادار کلادفلر خبر از افزایش ترافیک‌ اینترنت ایران می‌دهد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/alonews/121227" target="_blank">📅 11:09 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-121226">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/i7esQQOoRtZP82qvHdQDt2q-b0Xh_lG7kV3UEvhqhPYrnMOT8UuER5xvT1KhkGVleY3DDHo_6hR_uZJIg_bIwzFUzbNyWw4RnGIVsVLDUu4GBz0qlbqrVUii4qkO26r4juqqWw5Ul26oTRp8KHWFl7fMKR5z-s_WbAhHI_4RswgsYZOhGgbEaIqCIm2-ca9YsECl29ZUL6RY_j9n_7WfuxpXxTBLNXsfZOXk5A2_BoswsVMxnBfWxJ3FTtNXF0lGoSnRMCCFIxn-o_5KM3vkcjQcsPDb7a6dx9aKP55QLdDeeDR1G-7kema_5kEFPGVvHyt6XZ5Um5Gik3FAlPZ13g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
بدون شرح
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/alonews/121226" target="_blank">📅 11:04 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-121225">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qfEMBVCmtzb1tfJRmdY6S3xFUtjMoCLCE4RhQ7oZCcN3BCK1idH7dfLNZ7GmSx9aeRfz0Ibhm7eyDblgJY4kjRj29jj5ZxSASPuSnMqYdhqtoKDSqZ0u0qcc_-BqQykf_fZsktQvgn4VkDSNLEPzGMkWp9f9yDOk42YIVS6fd3QMEzEC1ZRniNdJ6u94TSMkYuCAsK_puVoU7AUGqOzfVewEoy5FBnyV3tInhn8OnSmqBvqC7vJmUFrL81jhpkJ401FJNmNAVghBu5jOEoCZ4iQFKXFYEMTW-BIp6jg0zQLLN9NYnqfn8OLIwH_5YsCgocAjbiMHCsMadhN0ixSe6A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
میانجی‌های منطقه‌ای و مقامات آمریکایی به WSJ می‌گویند: موضع ایران در مذاکرات با آمریکا عمدتاً بدون تغییر نسبت به پیشنهادات قبلی باقی مانده است.
🔴
ایران همچنان خواستار پایان خصومت‌ها، تسهیلات مالی، غرامت برای خسارات جنگ و نقشی در نظارت بر تنگه هرمز است، در حالی که با خواسته‌های آمریکا برای تعطیلی یا تعلیق بلندمدت برنامه هسته‌ای خود در تضاد باقی مانده است.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/alonews/121225" target="_blank">📅 10:59 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-121223">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">👈
مهر: قیمت خودرو روی کاغذ کاهش یافته، اما بازار همچنان آرام نشده و انتقادها از مدیریت فروش و عدم تناسب زیرساخت‌ها با تقاضای میلیونی ادامه دارد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/alonews/121223" target="_blank">📅 10:55 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-121222">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NqZA2K39AdRGIrdI7I0dh73Aao-8A89qI_T4pVdn32_0pj7vDHsNEW_3wt7j2liYpPc43zX29dKCvbq8vxur9VbpQ45Zk2zKgYsFKUtao65yVFd4cJs-9RQ4_3R9nZwczLLIBCQu_k8TCBNI2lOkOGfxN_lHEECzJSTlbGnB6tVqOeZ_jJDKgh4EfpQ_96GUuAukW6NAUeMuNsR7IOJy2vQygYjFeypIjCVFzlfNCu0JJ7Nvg9_nTehPK6jfRK1aGO6tJxFvKXoIJCsEjkUW6Mb8ZyUXEM60KKU8SZjJ-8Aopl3oufllmoiRW7xXQ4I7FPt4Gk2_H5kYDqrcFU4K5A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
رادار کلادفلر خبر از افزایش ترافیک‌ اینترنت ایران می‌دهد؛
شروعی برای موج قوی تر فیلترینگ؟
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/alonews/121222" target="_blank">📅 10:50 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-121221">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">👈
قوه قضاییه: کشت هرگونه گیاهان مخدر از جمله خشخاش مطلقاً ممنوع و جرم است و مرتکبان به مجازات قانونی محکوم می‌شوند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/alonews/121221" target="_blank">📅 10:45 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-121220">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/D90udZftzerKC4M1fnfLsuIWBLJN6quGE2xACyeuTbCOwNH8AWb3eNFuZ9NIcXpMyNZLIXFKLHbWB-NBwfsXhXhL0CtAtbYQgp38lAEHYvyjfsKSMcMbg0XGLu0ZRJSdu_hxQtmAwA6ziNQ2ozXytuwKhmH2JI5trUv1X2HsdPRlUr7BdPJzacrE1FG_7BLXbSA6ngjaUk0hSqdlY3eG94Lzf3usIWS1M3lWOVdUEPUVXOxBfnSzUPgnk05BzepM6jG8oIMO1hAfHCWfR0oTJnuJ7scMgY68IXq6zJG9Uq1f1_kcW-_5XPsTolYlNmL39gShzhmsdxtGpq3w2NX0ag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
هند با هماهنگی ایران و آمریکا از خاورمیانه نفت می‌خواهد
!
🔴
بلومبرگ: هند برای اولین بار از آغاز جنگ علیه ایران، آماده اعزام نفتکش‌ها به تنگه هرمز و بارگیری نفت و LNG از خاورمیانه است.
🔴
این اقدام با هدف کاهش بحران انرژی و کمبود سوخت انجام می‌شود، اما با هماهنگی دیپلماتیک با ایران و آمریکا همراه است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/alonews/121220" target="_blank">📅 10:42 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-121219">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">👈
فایننشال تایمز:  شرکت سرمایه‌گذاری خطر پذیر ترامپ که در حوزه هوش مصنوعی، فناوری دفاعی و املاک فعالیت می‌کند، در حدود یک سال از ۲۰۰ میلیون دلار به ۳.۵ میلیارد دلار دارایی رسید؛ یعنی جهشی ۱۷ برابری
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/alonews/121219" target="_blank">📅 10:37 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-121218">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/c313539861.mp4?token=T8IOzy-KZnHi48o2oiA5JjIOaDYsmKp8j6z9GuhEAKKIBUWKC-r-BoFRC7gNHyttAx-3LlJaSwyUNOf2FCMDQiofBSJXTLtvvhMW6Xi3Z8G_fGW0AbUlZLbB5kkdedp6t9oxkcIVwGLpr8fsS1lxoo5UhAsSen5V0HJHUTlw6t1hW2TRqPgSk-uHKWptVM2Royf17sLsQgU8UpjFRR8OSrbAvipurVQ_ysV_aPMJ2rSYenHkv_E_7PTdcJnfuqhdwZ3fAnVdqNN6rtrk9Z1EBWHD0odl0jJdXygNrWNHxBRJ8jEJvrcJ_uu5YQs_RArLR7sBKSZf-pbaMFLRJz3Exw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/c313539861.mp4?token=T8IOzy-KZnHi48o2oiA5JjIOaDYsmKp8j6z9GuhEAKKIBUWKC-r-BoFRC7gNHyttAx-3LlJaSwyUNOf2FCMDQiofBSJXTLtvvhMW6Xi3Z8G_fGW0AbUlZLbB5kkdedp6t9oxkcIVwGLpr8fsS1lxoo5UhAsSen5V0HJHUTlw6t1hW2TRqPgSk-uHKWptVM2Royf17sLsQgU8UpjFRR8OSrbAvipurVQ_ysV_aPMJ2rSYenHkv_E_7PTdcJnfuqhdwZ3fAnVdqNN6rtrk9Z1EBWHD0odl0jJdXygNrWNHxBRJ8jEJvrcJ_uu5YQs_RArLR7sBKSZf-pbaMFLRJz3Exw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
توماس ماسی: باید زودتر اعلام می‌کردم، اما باید با رقیبم تماس می‌گرفتم و تسلیم می‌شدم، و پیدا کردن اد گالین در تل‌آویو کمی طول کشید.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/alonews/121218" target="_blank">📅 10:34 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-121217">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3a0465ca26.mp4?token=ZFK7cGXRy42T_pZCb09UR0DmQ49YksRslVxpKtlHKGqpzSDENhoPbCR7rObz3fQsytPE_12g23bcYdcR2yF06EQdew57kt35xFzStcA6yznjAAcZr-KJHuHxyR344ADwEcM-1ZsTD3SLLcPXBlwlYAg_ZWecrptkfphpuABV-H4VECLoU10UcvLZglb9prieHzmm1kC2DzXbDMatQz3ixJU7cNEazTJ9Yuwaq8NUCGW18dGNXXJ7wlCkSysKMEu2Becq50z_bilIxzh5Uo7gFWSlUfA_Chj6dGmVwMHRI5aDNKRc8i3DyGD8xvk7VTYrPs2MSR89OJd99_JBEJrpjQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3a0465ca26.mp4?token=ZFK7cGXRy42T_pZCb09UR0DmQ49YksRslVxpKtlHKGqpzSDENhoPbCR7rObz3fQsytPE_12g23bcYdcR2yF06EQdew57kt35xFzStcA6yznjAAcZr-KJHuHxyR344ADwEcM-1ZsTD3SLLcPXBlwlYAg_ZWecrptkfphpuABV-H4VECLoU10UcvLZglb9prieHzmm1kC2DzXbDMatQz3ixJU7cNEazTJ9Yuwaq8NUCGW18dGNXXJ7wlCkSysKMEu2Becq50z_bilIxzh5Uo7gFWSlUfA_Chj6dGmVwMHRI5aDNKRc8i3DyGD8xvk7VTYrPs2MSR89OJd99_JBEJrpjQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
پوتین و شی بیانیۀ مشترک تعمیق روابط چین و روسیه را امضا کردند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/alonews/121217" target="_blank">📅 10:34 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-121216">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">👈
روزنامه کیهان: روسیه منطقه کریمه رو پس گرفت و چین هم چشمش دنبال تایوانه؛ ایران هم باید بحرین رو پس بگیره.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/alonews/121216" target="_blank">📅 10:31 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-121215">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">👈
بلومبرگ: یک نفت‌کش با پرچم کره جنوبی در تلاش است که از تنگه هرمز عبور کند
🔴
نفت‌کش «یونیورسال وینر» صبح روز چهارشنبه شروع به ارسال سیگنال‌هایی کرد که موقعیت آن را در تنگه، در جنوب جزیره لارک ایران، نشان می‌دهد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/alonews/121215" target="_blank">📅 10:28 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-121214">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">👈
خضریان،عضو کمیسیون امنیت ملی مجلس: امیدوارم خبر سفر عراقچی به نیویورک برای مذاکره در خصوص تنگه هرمز دروغ باشد!
🔴
چرا ما در خصوص موضوع تنگه هرمز باید در خاک اسرائیل و آمریکا مذاکره کنیم؟
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/alonews/121214" target="_blank">📅 10:26 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-121213">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">👈
خضریان،عضو کمیسیون امنیت ملی مجلس: امیدوارم خبر سفر عراقچی به نیویورک برای مذاکره در خصوص تنگه هرمز دروغ باشد!
🔴
چرا ما در خصوص موضوع تنگه هرمز باید در خاک اسرائیل و آمریکا مذاکره کنیم؟
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/alonews/121213" target="_blank">📅 10:23 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-121212">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">👈
سایت عبری والا: مجروح شدن فرمانده تیپ زرهی ۴۰۱ و تعدادی از سربازان اسرائیلی در جنوب لبنان در پی حملات پهپادی حزب‌الله.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/alonews/121212" target="_blank">📅 10:22 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-121211">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">👈
هاآرتص به نقل از منابع اسرائیلی:
از
اظهارات ترامپ که گفته بود تنها چند ساعت با حمله به ایران فاصله داشته، شگفت‌زده شدیم؛ انتظار داشتیم که این حمله به طور مستقیم و گسترده با اسرائیل هماهنگ شه
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/alonews/121211" target="_blank">📅 10:22 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-121210">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">👈
پزشکیان: هیچ کشوری تسلیم نمی‌شود، مگر اینکه از درون دچار اختلافات شود
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/alonews/121210" target="_blank">📅 10:22 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-121209">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">👈
رسانه‌های روسیه گزارش دادند استیو ویتکاف، نماینده ویژه ترامپ به زودی به روسیه سفر خواهد کرد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/alonews/121209" target="_blank">📅 10:22 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-121208">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">👈
الجزیره: قیمت نفت پس از اینکه ترامپ گفت جنگ با ایران «با سرعت بسیار زیادی» به پایان خواهد رسید، کاهش یافت
🔴
هر بشکه نفت با کاهش ۰.۴ درصدی، به ۱۱۰ دلار و ۸۳ سنت رسید
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/alonews/121208" target="_blank">📅 09:32 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-121207">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bd0688edf0.mp4?token=v3VKNWvVD1ufGiSLCOdZjn_ydgJAv5ooTv-zSFAItCGDJ50-_aO1erxiEbiI0xQbcBsP_Ees8rj0OcWlJsGMDO24PQ_NXZvV2-bxujt53wZrBFe2gx6aZ8sSqG32fpOmlTqmMSGad-gJQDwRauxNji_rcrS6eVNMVINdtbbV2kbkSbrRsIdSBUMd_RB5ugzWviYe9bOTFobOQV-fvk-wbY2-q2S6OzdMb_3pegUOByaFI1rXYKn14mGzMBAIrsQoEzCpt25nGjGTAuqTL5hQfGOvn3ntjXm7KhWg24lT-h0o-xSh2nZOpAG6LmrTwF8uxMiBgIl8L2OCYL61ZrfniA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bd0688edf0.mp4?token=v3VKNWvVD1ufGiSLCOdZjn_ydgJAv5ooTv-zSFAItCGDJ50-_aO1erxiEbiI0xQbcBsP_Ees8rj0OcWlJsGMDO24PQ_NXZvV2-bxujt53wZrBFe2gx6aZ8sSqG32fpOmlTqmMSGad-gJQDwRauxNji_rcrS6eVNMVINdtbbV2kbkSbrRsIdSBUMd_RB5ugzWviYe9bOTFobOQV-fvk-wbY2-q2S6OzdMb_3pegUOByaFI1rXYKn14mGzMBAIrsQoEzCpt25nGjGTAuqTL5hQfGOvn3ntjXm7KhWg24lT-h0o-xSh2nZOpAG6LmrTwF8uxMiBgIl8L2OCYL61ZrfniA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
پوتین از شی جین پینگ دعوت کرد تا سال آینده به روسیه سفر کند
🔴
سفر قبلی شی جین پینگ به روسیه در ماه مه ۲۰۲۵ بود، زمانی که رهبر چین در جشن‌های روز پیروزی روسیه شرکت کرد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/alonews/121207" target="_blank">📅 09:28 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-121206">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">👈
واردات مواد اولیه پتروشیمی و پلیمری از طریق رویه‌های ملوانی و کولبری مجاز شد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/alonews/121206" target="_blank">📅 09:25 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-121204">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/bivGZmxsiheMRJxo5GyXLX5U69jFWFp3Y13llJb23Xjq1t2_GdTMpEJ73qTzht7iQQzL3KDbdesLq6wC64wWuhsJbI3FbMv7F2Efk3L7DPDSROxPZkTJHm1adVebRwOeK3_PxXmVDnHaG97OW8s_3nyvYH_5o9pt-aio2X-ZivnxiKsRp3X2mk_Fk6gMLzymia9PAiRLOiKQtkP3ZycIuGfwO0HQQRkz1-R8DUgTg-H2jJ6ucv370SJqhvk2MVn5B-fHk3J527cmjE3l4gsf8MQwvmYcIVYtEuEul4PsLyJ8zGwwDCdA0kF_7gEF_CNV33JOhLIklfWZ40ZaW1Wqig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vZpSmlRbbdjXo4KaMYYEhg0EfjCYrDb9vC18kc35Dvr7o6cGXF4U9NmMwtks1nqU_3Qa-t_wIWevCDJR3QJ_N8pRZJFB5MmrfIJU8-xtUjEhDe261hi6WP9I7_Yzim3101Ra6hdeTgi5pK0lp8cbHaRgOcItxfAErM6H5A9IMY9gdD4CdUOC0Hcw9OmcdCH0-un5jaGiICYoSN4XFiqRoT-OGbchDiO3I9d_x60NWjyPiBvYDRY7qkq6fuL3pIKQwFht2B-JG7vOOU360dt6ivWuCo6-CmFjxgQWRWuLnpkNM7I3Mqavs-X2h-8YmPwNB25skOkyJ1aKDJrVSVIaRw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
ترامپ موبایل از راه رسید / گزارش NBC از موبایل جدید ترامپ:
🔴
شبکه خبری ان‌بی‌سی نیوز به یکی از اولین نمونه‌های بررسی گوشی «ترامپ موبایل» دست پیدا کرده است؛ محصولی که دیگر با شعار «ساخت آمریکا» بازاریابی نمی‌شود. ادعایی که هنگام رونمایی اولیه از این گوشی مطرح شده بود.
🔴
مدل T1 با قیمت «تشویقی» ۴۹۹ دلار به فروش می‌رسد و به صفحه‌نمایش ۶.۷۸ اینچی، دوربین اصلی ۵۰ مگاپیکسلی و حافظه ۵۱۲ گیگابایتی مجهز است.
🔴
گوشی ترامپ موبایل در چهار نقطه از بدنه و نرم‌افزار، لوگوی «ترامپ» حک شده، پرچمی آمریکایی با ۱۱ راه‌راه به جای ۱۳ راه‌راه روی آن حک شده و از پیش، شبکهٔ «تروث سوشال» روی آن نصب است.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/alonews/121204" target="_blank">📅 09:21 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-121203">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">👈
استریت ژورنال: میانجی‌ها می‌گویند مذاکرات ایران و آمریکا پیشرفت کمی داشته و دو طرف هنوز از هم فاصله زیادی دارند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/alonews/121203" target="_blank">📅 09:17 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-121201">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e1e1b86556.mp4?token=XlOKW24EdaXZnRmpCGrH3Epezhw59mAmW7ajkrS79INPuvX64B3Zl4cSRUgqD1qNz5QKBd1YDKV7RbHlzkMqCo8xjdg8tGCN46pKmMmrGvyLAJpWhIeVcjNRrl-XBmReh8CMLKvAPD2ikOcR1ntLGcvt-rHMo6MtjC05oFyK8HCfXuN236HjiapcXxzZDcLMRMtwf7HFlqPxnmSBQrWvrpqt5l1pmBRBQfW9PAj-F509yasL6Sp-h73BKKt3M7Y-chkcSi2OC7V---cS4DZrPPApagnmIsstoqwh9Qbn0HXfXcVg4WCHcw3Cfe-YQUlXELK4fD-yASnMNclhA5cH8H-UwmLdUuW-PyrlTzsQ9mxJX5BStvfepF3sgfzaUh6huzyqzrQPVcCCHyZAKl8UXipbCB1yCRQex7SQg3MSgdNangxfJWhHjx94z1U09eOggrgAMpar3INeG_JTnwqtXnbxIdcCK-_53EoebL7T-91kwugvETEZ83qL9RrjD4ne3hZLQpbMT6YaqqabnTR06iPSPlcD7Us4ukB8ByJylEbNJ5THD8dTONLlnq4mfULdorrgs4Wnbl6fjaO6CsVgEvEyKOWAQjlyDNWih4TsBUpagnrc4To2KNpooYhJ9HCpKgCkI3n1ZplraY-MJ4LwndyAJjg44MaZgaYGy3qOPi0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e1e1b86556.mp4?token=XlOKW24EdaXZnRmpCGrH3Epezhw59mAmW7ajkrS79INPuvX64B3Zl4cSRUgqD1qNz5QKBd1YDKV7RbHlzkMqCo8xjdg8tGCN46pKmMmrGvyLAJpWhIeVcjNRrl-XBmReh8CMLKvAPD2ikOcR1ntLGcvt-rHMo6MtjC05oFyK8HCfXuN236HjiapcXxzZDcLMRMtwf7HFlqPxnmSBQrWvrpqt5l1pmBRBQfW9PAj-F509yasL6Sp-h73BKKt3M7Y-chkcSi2OC7V---cS4DZrPPApagnmIsstoqwh9Qbn0HXfXcVg4WCHcw3Cfe-YQUlXELK4fD-yASnMNclhA5cH8H-UwmLdUuW-PyrlTzsQ9mxJX5BStvfepF3sgfzaUh6huzyqzrQPVcCCHyZAKl8UXipbCB1yCRQex7SQg3MSgdNangxfJWhHjx94z1U09eOggrgAMpar3INeG_JTnwqtXnbxIdcCK-_53EoebL7T-91kwugvETEZ83qL9RrjD4ne3hZLQpbMT6YaqqabnTR06iPSPlcD7Us4ukB8ByJylEbNJ5THD8dTONLlnq4mfULdorrgs4Wnbl6fjaO6CsVgEvEyKOWAQjlyDNWih4TsBUpagnrc4To2KNpooYhJ9HCpKgCkI3n1ZplraY-MJ4LwndyAJjg44MaZgaYGy3qOPi0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
رئیس‌جمهور چین: جنگ در خاورمیانه باید فورا تمام شود
🔴
از سرگیری درگیری غیر قابل قبول‌ است
🔴
تعهد به مذاکرات به‌ویژه حیاتی است
🔴
اوضاع در خاورمیانه در مرحله‌ای تعیین‌کننده و آماده گذار از جنگ به صلح است.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/alonews/121201" target="_blank">📅 09:12 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-121200">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/SlT_bNX1uI-hKXtJHk9PrzyEtLfNGPV6FlIpYUzETuAptqqyAW1Kpt5J80n0b6wrxuWtOArEBRxeCkqpoTB27CzBz_P7z5vZ-PSj7fdzeeRfnE1ExWGRBELUpDuVE48tud_8mq72nlrpVyda565UPkO_rNGtubBqnkmNuE9HtDn1Pb7BW9u1hzd3WXJSaJftoj39DxczTwwLpWJznNTvzktJhyjT_Z2F4YIYoyisfw5mZVDkwbF88a0ctHWAzHapRNeO8wqtknM7iAj1yXfPPQzeyCa6TUd-tPEtvUOf-Xp9DHaUdlr-Nj1s-5vH7FUOt8tiDeSgg7tgzO-a-LOyuw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
بهمن فرزانه؛ قاتل الهه حسین نژاد صبح امروز اعـدام شد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/alonews/121200" target="_blank">📅 09:07 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-121199">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6701955385.mp4?token=Bbd4_pGlCFuWqahxz4HPDmch6Os4vEa1lsdvZkdJiVx00Jtgg3a1wp-yHXd17adrUTiS5QCvEZCPg4U45NAMawo-KPdpnKA-wcnrsYFi5ZttsnIAs8QZSKW7Dara55-5J9IulIa9WmU_oX6Mg96Fum6HQKC1XZiNB0DTG41z870kU7iZ9yImTl2ehJtzjYWAFaAOdITjXpju5WBNcNzPmeB39ugNf8nT7Dxi25_B-Cg1j7fnwosqR-gci2vDoVwIZeiKL4C2MeHHCdRf6W71DnPexUkCWpPK0PoKm7Ep5AB4A68SjnXbro-glM3D0BW0sjPAT0AZk_HHjU2bl_zBPg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6701955385.mp4?token=Bbd4_pGlCFuWqahxz4HPDmch6Os4vEa1lsdvZkdJiVx00Jtgg3a1wp-yHXd17adrUTiS5QCvEZCPg4U45NAMawo-KPdpnKA-wcnrsYFi5ZttsnIAs8QZSKW7Dara55-5J9IulIa9WmU_oX6Mg96Fum6HQKC1XZiNB0DTG41z870kU7iZ9yImTl2ehJtzjYWAFaAOdITjXpju5WBNcNzPmeB39ugNf8nT7Dxi25_B-Cg1j7fnwosqR-gci2vDoVwIZeiKL4C2MeHHCdRf6W71DnPexUkCWpPK0PoKm7Ep5AB4A68SjnXbro-glM3D0BW0sjPAT0AZk_HHjU2bl_zBPg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ درباره ایران:
ما همه چیز را نابود می‌کنیم و این جنگ را خیلی سریع به پایان می‌رسانیم.
آن‌ها آنقدر خسته‌اند که می‌خواهند به شدت معامله کنند.
🔴
این باید ۴۷ سال پیش اتفاق می‌افتاد. کسی باید کاری درباره‌اش انجام می‌داد. کسی باید کاری درباره‌اش انجام می‌داد.
🔴
این اتفاق خواهد افتاد و خیلی سریع خواهد بود.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/alonews/121199" target="_blank">📅 09:05 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-121198">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">👈
کانال ۱۲ اسرائیل: رهبران عربستان، قطر و امارات طی ۲۴ ساعت گذشته با ترامپ تماس گرفته و گفته‌اند: «اگر حمله کنید، ایرانی‌ها به ما حمله خواهند کرد.»
🔴
آن‌ها از ترامپ خواسته‌اند که در تصمیم‌گیری خود آن‌ها را در نظر بگیرد و فرصت بیشتری برای مذاکره بدهد. ترامپ…</div>
<div class="tg-footer">👁️ 31.9K · <a href="https://t.me/alonews/121198" target="_blank">📅 02:29 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-121197">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">👈
کانال ۱۲ اسرائیل: رهبران عربستان، قطر و امارات طی ۲۴ ساعت گذشته با ترامپ تماس گرفته و گفته‌اند: «
اگر حمله کنید، ایرانی‌ها به ما حمله خواهند کرد.
»
🔴
آن‌ها از ترامپ خواسته‌اند که در تصمیم‌گیری خود آن‌ها را در نظر بگیرد و فرصت بیشتری برای مذاکره بدهد. ترامپ نیز ظاهراً با این درخواست موافقت کرده و اعلام کرده حمله را به تعویق می‌اندازد.
🔴
با این حال،
برخی از این کشورها اکنون این ادعا را رد می‌کنند و می‌گویند چنین درخواستی نداده‌اند.
در مقابل، مقامات آمریکایی می‌گویند هر سه کشور چنین درخواستی داشته‌اند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 31.3K · <a href="https://t.me/alonews/121197" target="_blank">📅 02:29 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-121196">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/53d10498a4.mp4?token=YD8sul_L6vns3dXvVIq4kph9VjRsmAgrmItZ6BxNkg-M052lmT89c5SRqBtvMwIt0q08GyDqU2KaNjUgjPdt6LVQ4X4Itoltiknh2i1dEAXYMGdy1wo9qZX_619xiEZwvlzncFJZMdjaDhHLks2Ufoxx93MM_LOrY7j1-InsooX5jvg5BEM3PkEjJZwNjiOBrOwk3lbAnhj1qewl3ZkbN6Q07cZzp1jDB17RKssywlpiSEhdvfR0IZFLZOP86fpBx9uJIOeITOlrTtPw51q4Xs1bhE-fSOV5SF55t6YD5XN0iVHTB_3QaaAqO22GNxlDSJVMykZylsPQwkp4rNsEPQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/53d10498a4.mp4?token=YD8sul_L6vns3dXvVIq4kph9VjRsmAgrmItZ6BxNkg-M052lmT89c5SRqBtvMwIt0q08GyDqU2KaNjUgjPdt6LVQ4X4Itoltiknh2i1dEAXYMGdy1wo9qZX_619xiEZwvlzncFJZMdjaDhHLks2Ufoxx93MM_LOrY7j1-InsooX5jvg5BEM3PkEjJZwNjiOBrOwk3lbAnhj1qewl3ZkbN6Q07cZzp1jDB17RKssywlpiSEhdvfR0IZFLZOP86fpBx9uJIOeITOlrTtPw51q4Xs1bhE-fSOV5SF55t6YD5XN0iVHTB_3QaaAqO22GNxlDSJVMykZylsPQwkp4rNsEPQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
وضعیت رئیس کانون هواداران پرسپولیس
احتمالا مدیرعامل آینده...
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 30.2K · <a href="https://t.me/alonews/121196" target="_blank">📅 02:20 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-121195">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dx3Wpw8MObIDugPdKtGmyi6Mb7XZQMQ6TojoQtifDrJwrMIaNCcebvzb3eHZqFNnhnMpMJ4BMfkbvh2cTNAQ_t8m7KrOwi5Zk39gidQpu0UnL6DVWYTtjpgoKRWXerM-5f14rKUVaURxjBakdOeU-Iui5HH_8ExAbiKckm3tDW90mShcLbrNfSow50MEMou6wJetxTnNKQV-2SPMFiW2cjDOldmvaU19gSkJ80-GBJ54Yc2JwiG1UbhgyqWojDlWqe1I6tYB1XvbsYs3Q8B0xGu87c3UOxz88KXQI6DP49W0HOkwUdLDQMRuxClP2AGWCF-5RwtCMaDYFX8GRJNt_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
خضریان:
ترکیه حد خودش ندونه باهاش برخورد میکنیم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 29.2K · <a href="https://t.me/alonews/121195" target="_blank">📅 02:05 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-121194">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UPL9z-oNVmbcP5AYPWnHMM0BqZVidqauo-FqyHlAX8jWTx2ih0pwrN4WMTms8GEDQCziW2EWFiaDO7dVS0DnjEvc72BwykK5UsueHgIra1Ty5W2VmYrypdv4EF4CWUDmezsHEZ6s-DFb-xn95V9NwRp7SQTQFxX4Fk-TQ2Qk_7KRy9qD41bTSSLjUmhp7wRxojgn_mEJdYXe2INUemkI99VoKkfjl5lswRn9kLrxAtLK-TPTbNA7n4vy9eu4Xrv5NpbOpSoZYqtyjyE5twDcvOCm2rm2dFdzlhR6l06BZr86KcDivqL27d8cInU03RYIsEjF7nuKE_fdwaEsWQt82g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
نخست وزیرهای ایتالیا و هند این وقت شب دوتایی رفتن کلوسئوم رو ببینن
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/alonews/121194" target="_blank">📅 01:54 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-121193">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">👈
ترامپ: آمریکا ممکن است دوباره به ایران حمله کند، اما تهران خواهان توافق است
🔴
ترامپ گفت ایالات متحده ممکن است بار دیگر ایران را هدف حمله قرار دهد و افزود تنها یک ساعت تا صدور دستور حمله فاصله داشته، اما تصمیم گرفته آن را به تعویق بیندازد.
🔴
ترامپ همچنین گفت که که مقام‌های ایرانی خواهان دستیابی به توافق هستند، اما هشدار داد اگر توافقی حاصل نشود، حمله جدید آمریکا ممکن است ظرف چند روز آینده انجام شود
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 28.7K · <a href="https://t.me/alonews/121193" target="_blank">📅 01:43 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-121192">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SI3LeajTYgCT3wZlFeg3aAbvakdPexsE_60gp84LI4SaTgb0Wq6wkroZsleqi2GcCloRVc1HiEhhrvzhQxkwQgkhWDYBrkE3L2C2mJMhGh20cSYujPDzC-u49XyF0Y8eBsB4BK6eYmN13lEtWXpVnGbw2uTNVRQIaqzw8X3tvsnbmb191HrMzG3NndMhLTZI1Y_i9X0iwk6f9j4bgc1H8cThTyjq2JYq5nbXIRWNzuOkrFJZoP2xX6rIAtLxhVHoEaWIOx8tHoD35za5jqSBmNeQSvo9pUDGJkn3G1J09RgW6Vjs23hN14B9VteTmiGyeb3glKSxUAswxvTuspp8Ag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پائین‌ترین پینگ‌ها رو با ما تجربه کنید
✔️
🔄
کانفیگ‌های استارلینگ با پشتیبانی 24ساعته و لینک ساب
🔄
💯
مورد تایید مجموعه الونیوز
💯
📌
تحویل زیر 1دقیقه
📌
بدون هیچ گونه قطعی
💰
خرید آسان و سریع
⬇️
💎
@FastProxyMakerBot
💎
@FastProxyMakerBot</div>
<div class="tg-footer">👁️ 29.2K · <a href="https://t.me/alonews/121192" target="_blank">📅 01:37 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-121191">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">🔴
خبر فووووووووووووری/پس از ۷ تلاش ناموفق، سنای آمریکا طرحی را تصویب کرد که مصوبه کنگره را برای ادامه حملات نظامی به ایران الزامی می‌کند.
🔴
سنا با رأی ۵۰ به ۴۷، اکنون به طور رسمی «قطعنامه اختیارات جنگ در ایران» را پیش برد.
✅
@AloNews خبر جنگ</div>
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/alonews/121191" target="_blank">📅 01:33 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-121190">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">🔴
خبر فووووووووووووری/پس از ۷ تلاش ناموفق، سنای آمریکا طرحی را تصویب کرد که مصوبه کنگره را برای ادامه حملات نظامی به ایران الزامی می‌کند.
🔴
سنا با رأی ۵۰ به ۴۷، اکنون به طور رسمی «قطعنامه اختیارات جنگ در ایران» را پیش برد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 28.7K · <a href="https://t.me/alonews/121190" target="_blank">📅 01:32 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-121188">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QFrradbWceGxKz7-HdtOlIzl7pWoINZQ0of3iYRgCFKcVzmd1BqhCQtFiKIF5MhL3sPs2InVsI5EBZnlG_ZaI61ATZhilZhb3T7OMvn2nkT_YqSsegogWeWH5CFwpqlP2_tmQ_HPDN87cwu2xa9rNz_BxBR3rKNETAiAfbEXPTImr5diqTHBKxJTuopKqZ47lsPsWmqfkf3HmbOfK4aK13JfeQWFyvrLwm7-NlVqqFEfvXZUy1KZSVef2ZeJEDw7MGlxvFCE6zXYnlykREJf07VNspMnE7rDAJN_GeKIzqQQtUHk-wy0clHCVH4Xf0KbAuV0xJHAtDL9_gHIOBBvAw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/56b08bc0f2.mp4?token=FsASgN3mwJ6g4-pa9LtLAi_0j15Oj-rG8LY__z3G-pQbvk6sipp9C2EQLMqVkH89MGUfpMBmssezGVc3cYw5hc42jUwpHQ3PF5J9PqhWa80KuJahBQqupoZuKlWzq1-EnEVcerPTqQMHoTC8k-76Lp-AxI7sgrGP5CmrKYwSP7Y_7upDtvja0kw_hvprxcpEhiVmm_JDxpkQLQaYWFXQRvO-jjRaanFyY-VSqp_94bnk2OiOZPSVYETr9UG8wt4Osl4ntz09RqGzk6_05SIvJJ8JyHHNthw1JhJ1L7AKI1H-o_EE8zPEn6qd4xwUIQWsZ1XHK77Ixie5BTbbHsKnhA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/56b08bc0f2.mp4?token=FsASgN3mwJ6g4-pa9LtLAi_0j15Oj-rG8LY__z3G-pQbvk6sipp9C2EQLMqVkH89MGUfpMBmssezGVc3cYw5hc42jUwpHQ3PF5J9PqhWa80KuJahBQqupoZuKlWzq1-EnEVcerPTqQMHoTC8k-76Lp-AxI7sgrGP5CmrKYwSP7Y_7upDtvja0kw_hvprxcpEhiVmm_JDxpkQLQaYWFXQRvO-jjRaanFyY-VSqp_94bnk2OiOZPSVYETr9UG8wt4Osl4ntz09RqGzk6_05SIvJJ8JyHHNthw1JhJ1L7AKI1H-o_EE8zPEn6qd4xwUIQWsZ1XHK77Ixie5BTbbHsKnhA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
تصاویر وایرال شده از مدرسه میناب
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 28.9K · <a href="https://t.me/alonews/121188" target="_blank">📅 01:28 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-121187">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iH7qTuKhza70oJwdO2HO8zo2GjIStbpG_asrtI9RMKIKUKWzYrSvu0_Fs1Ds1OGm2pBw5WDPH9RzW-rFxZJ27-Fn-vPl-GLMOGqQvNumV6-0tdZhGpgUs4lotMW3LVAUxebaVfK4bCw-udhVTEpNEIEZlqw2PZnpAUUvHU3yL-QHo8LnHQUnDfJAnvGp1kKi7bfhxdGPrBSS9stTZ10j5PPHSwPfCZqhMzoi3wL1Em1nvS9-9U7JQvJvJxD-xmLExWuDSbqJg-j2HFgtSkV8F7UuVgjFC6KrwzYWIyvJh-L22_1Vxt02Z-HAnk-_0dqD3t2IorzfaQiDmKIjMxp4VQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
جا داره قهرمانی آرسنال رو به جاویدنام عارف جعفرزاده تبریک بگیم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 29.7K · <a href="https://t.me/alonews/121187" target="_blank">📅 00:56 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-121186">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IYHun4K1Km-dC7VEQqYIT7JcnrLL9e4nQjGv8GDKEMoI9PJSr_7uoSUc54Omzei86nhCMS7lfA4fybWQ6prm8gRapByMt6UgfRd9VubULyzqNH7XG_wDUPcSLKhx5jmef1IEuKXFpVeKdRZpldxwni5xrYjucbjHEzdYIeh4UOZQyaDu6yeYg1wLgbl-yNrzkKaPT3yis_4gPYpFIpuNUfPF-Kr0MxoCahLda9XpUC0AKbh0UiCXpZrqD_4-hbwqsEUZSYShkbBPIgH9q12RWa0oOcodaQNwhKmSDkEEpOEOxAYz1x2GsLSvg5pyz-rzkFNENVu2vGpp5F1YC5O9Uw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
لیندسی گراهام : امیدوارم و انتظار هم دارم بعد از این چند ماه مذاکره با ایرانی‌ها، دولت ترامپ هر تلاشی رو که برای دوباره کش دادن مذاکراته رد کنه
- این رژیم ماه‌ها وقت داشته به توافق برسه، ولی به نظرم واضحه دارن بازی درمیارن
-:من خودم ترجیحم راه‌حل دیپلماتیکه، ولی قدیمی‌ترین ترفند ایران همیشه این بوده : امروز و فردا کردن، کش دادن، کش دادن، کش دادن
- در مورد هر توافقی هم، منتظرم بره سنا و اونجا بررسیش کنیم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 28.4K · <a href="https://t.me/alonews/121186" target="_blank">📅 00:50 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-121185">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">👈
جهت رزرو تبلیغات vpn در کانال
#الونیوز
به کانال زیر مراجعه کنید
👇
📃
https://t.me/ads_alonews
📃
https://t.me/ads_alonews</div>
<div class="tg-footer">👁️ 28K · <a href="https://t.me/alonews/121185" target="_blank">📅 00:45 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-121184">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/E4b4EVqBcbTHzsKn6SNeaZwI1ce-baYisX9Jg0xT1CT4AHC1SpSRk_892kiffuhCzIevJYQ3T2-6qTWcamhzK8c8T2gmtvjqOgwTzFdRr9jvPNNKwMNaZJUaFFDqpgTSqqGAbLI8joUUnS2bUrOye5vWu-P8gz9Xov6aW72wwT6YksNwH_EBB9lrBCK4A5RgwyfHsejdLak_D5nFXPQkL6DUf_UmJZYRHn6J6L-XrXLbKPIN6XL4Ym7_1aIpamXRdyjBvhFsPbn8IN7stUkPeIKV8987Z69NpVvEm52CJ0J8xQQebPeRoRmSEms9XICEwXNNa-r0HpkCNmPdEwPALQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
حسین طاهری مداح:
اینکه دخترها بی حجاب میان تجمعات یعنی پیروزی انقلاب
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 29.6K · <a href="https://t.me/alonews/121184" target="_blank">📅 00:32 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-121183">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LXb_R4aL1DNE6c0eeXYhBX8GyZdxZrmU4SjpunKfw3tz4ARbaxrSIglJq1kbGxDUaRgmJqWcTz05dFs7wfOg8O4fS7-NpfNh5YtmTCobTBrrVjTSorr6zuj-Ho5SIfuc4DbvP7gkeT-MLOOGHYQthZf9pySPnaE-f6bZB9rmXtkEf5mDwf2l2ZWa7C_Wn8Hec9LoTlO271y0y8zdl-cNG0Cqj_uLir9uldEau13SpIc3bcsPTydOVCRwr4iM0DOT4sq0Mvh48KgymOTAe14Bhdm59QkFqIno_WBJFiMayOBrcUkbRRRDxgXzV0SuVsEUVvounSZzgINzsWm3ild-kA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
امروز سالگرد فرود سخت بالگرد ابراهیم رئیسی هست
✅
@AloNews خبر جنگ</div>
<div class="tg-footer">👁️ 29.5K · <a href="https://t.me/alonews/121183" target="_blank">📅 00:23 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-121182">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BJQwCiavQ-mLTk7uBAED8Vy51y5hEOQbKlxEiKEQuLGj_u0UhZrQbl52gsIN92DYETQuTUixFeLW-X10MB5323b2rKe3_SFRbwk2b1r8k2MgWOMGgsW7PiISI-SyWT0R1yohScSmAuEMVFmEzYsS6wLT-55kYE2rFI0qvIy5RvCe9-rwnIlhDRpPZ6XxaNpT6xsGiFqhYpU_5Cs3QSiU5M6364HesRg3upcRmYKwUtmLV3ZMa4e5JQzQpQB5zqqcStwCezhBU2qPVjRz15Dyg09wHp8W1--cplxF9-7GZIxIMHg6NHiuoFwOo0KbuYGFhYjD1o6zPF5yIDNEX71BEQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
امروز سالگرد فرود سخت بالگرد ابراهیم رئیسی هست
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 29.5K · <a href="https://t.me/alonews/121182" target="_blank">📅 00:15 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-121181">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromالو توئیت | AloTweet</strong></div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/kX5AarEKKbH3LvlyXWHSKiMDvXT5MRsAzItt0mMlZi8YuBxhvA7QgDDrKswfrBJtoyylgc3SpFx7aBS6iFdmILgWkAGy2sImof4_8VL5WhTCLfxYzfqCOpCOBZO6mXtsupapWZVnfEGA0TtKPIdGyGuitntccZkH4NsPvkrflf5AW3V_C3ueUjwtpKKsL3gOqqM_LUaxVEs8qFJz-dlEpwTQwIJD8I42ILCVCBAS7NumyIV8fzeydancz6qygcWpATf6TeKu94upqAkavKJudJQfOgQzn-CpyR5bnHx7mXg-1w9EXJYCT980iWkKqC-vR-XCCZPmlUZFenxp3sC3zA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">توی رستورانای تهران، یدونه سالاد شده 2 میلیون تومن!!
[
@AloTweet
]</div>
<div class="tg-footer">👁️ 28.8K · <a href="https://t.me/alonews/121181" target="_blank">📅 00:11 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-121180">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/27f199eb7e.mp4?token=c-jem0jBhVrxAntaiwpJXLMUDZvJKVt3p_8Ys2P5oRTtAqKuVENRP2DGAPtmEJP-hvy4bR4_Q1V8vPlOxlzArmmaa-Ra855M2_cFy42j8NgbvsRgZc30fP__IWsNkxfovadFGv7tkJFflOAUUKLgRXI7L-ICDM1PCijhNmbRyCxJftB5ZRNR3qKW4UaYSJ2nJyrryywpwD7oWGYdDgKfgyfw61SAnphATe170aEnX7i4i7ojChFxesGkkqf4S5xuLuyLW_gpoFW9PovecThDeFde7Ixtg6DFqutsGghbmAf04dAhTTL5NrNmaBW2KwDiahWNuKq1-83Apnt3h_s2aA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/27f199eb7e.mp4?token=c-jem0jBhVrxAntaiwpJXLMUDZvJKVt3p_8Ys2P5oRTtAqKuVENRP2DGAPtmEJP-hvy4bR4_Q1V8vPlOxlzArmmaa-Ra855M2_cFy42j8NgbvsRgZc30fP__IWsNkxfovadFGv7tkJFflOAUUKLgRXI7L-ICDM1PCijhNmbRyCxJftB5ZRNR3qKW4UaYSJ2nJyrryywpwD7oWGYdDgKfgyfw61SAnphATe170aEnX7i4i7ojChFxesGkkqf4S5xuLuyLW_gpoFW9PovecThDeFde7Ixtg6DFqutsGghbmAf04dAhTTL5NrNmaBW2KwDiahWNuKq1-83Apnt3h_s2aA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
تندروهای خیابونی این شبا تو تجمعات دارن یه‌ جوری قر میدن و میرقصن که انگاری ما رهبر آمریکا رو ترور کردیم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 29.5K · <a href="https://t.me/alonews/121180" target="_blank">📅 00:02 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-121179">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromAlo Sport الو اسپورت</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/l7Pjy7eLmJKnYlENKi70X1heM2xfB8B_GwRNDihW-2rd6UjC-wHc4t27WaEZINmePlNd6bEz1FoWYY--51P_xkwfvEEtKGi95baaXKdQLS4Wmqv5VQBUzGKNgELn1wzdc6A2DyN6nj8SM5OJifK-PYsww-zrZDGkzR9QWV-aaFaW_oaBISCNaSrfLcULpnAP8uSP7rG_uLfuLcXaoxrTNgDXghPs2jdmdPK1hcGgi0iDofH23nV5Cq_RBK3vKGuB7USEzZFPfKE1zFZAtq05I7qNV5DIBv_O412pfK5nmbniwTp_0Mkkixe2BzrfSOcqgjES0K21CqIHFFmJXhihwA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
🤩
رسمی : آرسنال قهرمان فصل 2025/2026 پریمیرلیگ شد
❤️
پروژه آرتتا بلاخره جواب داد
@AloSport</div>
<div class="tg-footer">👁️ 28.7K · <a href="https://t.me/alonews/121179" target="_blank">📅 23:57 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-121178">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ac5f337631.mp4?token=l_5gNjTK8udsop-DD_-2fm2yepr8TGNuU4ci6-VtYHSY-B4p7FFc7--o3TbeADYWVlmTX21Qkj4zBV2MNA8kJYG9jop2hM0P76y8KzeMF-sza5shVQX4mtI5X841NjDD9gMtoRbKEc4KaNmoGUhmVYvLbWB54eq4yAaUVp-ra7XygpsZLakxxFFjU18Rcq18YZUTmp8OwATrQt8BgNf8wLzbr01zQvtc_yjVwKa71VCfMlE-R7yiYkj4Qy4ocvF-sMBdI4v6ayY1bPZh3ano1hP_3q8zK1PUetfYRD1gIOKwrURYYYjg9a6fANFmFSkZg0lZ-7US5EbzHmWjKzw7EA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ac5f337631.mp4?token=l_5gNjTK8udsop-DD_-2fm2yepr8TGNuU4ci6-VtYHSY-B4p7FFc7--o3TbeADYWVlmTX21Qkj4zBV2MNA8kJYG9jop2hM0P76y8KzeMF-sza5shVQX4mtI5X841NjDD9gMtoRbKEc4KaNmoGUhmVYvLbWB54eq4yAaUVp-ra7XygpsZLakxxFFjU18Rcq18YZUTmp8OwATrQt8BgNf8wLzbr01zQvtc_yjVwKa71VCfMlE-R7yiYkj4Qy4ocvF-sMBdI4v6ayY1bPZh3ano1hP_3q8zK1PUetfYRD1gIOKwrURYYYjg9a6fANFmFSkZg0lZ-7US5EbzHmWjKzw7EA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
حمله‌‌های شدید اسرائیل به کرانه باختری
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 30.2K · <a href="https://t.me/alonews/121178" target="_blank">📅 23:48 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-121177">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bEeqH4fIy_ll-Tp0gW4aj1aPG-dSSBzSZD9XreLOdLe9cpqPY3gRaZPHFzUX3NW4tkNrsh7g0_eJCGQv2_Yplaq5-JSY_9U8jk6RjclbS7zNtW6Q8-h3SgCsJS9ZO9XaCZgwU1nMGiHYBiZpOMG5AZfOQ6Chs1psFR8gRR1NCDOC27tS4U1bVJhBz8SKn8vHC4ToR5VIbY0VL42ng3gqts7KD661EoG8oYOvMbzh6kq5I_c6DMXMedy0DFwUxJkE22HGfd-Znt-0frDDTwkydy5X-G5FNRE4iasaYEJvwmnzogUSfS2yZmrb9Sc0O_7JOb7H_6TfER7lraYq75OyeA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
آای هیمتی:
مردم جلوی گرونیا مقاومت کنن
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 30K · <a href="https://t.me/alonews/121177" target="_blank">📅 23:42 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-121176">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JYxyNs_tjYMMBfksxUW-wOve1oZI2DFPphaBFRvlxrx-x3WAMRjz383nCUga0HeMJZ0Tp0Y8fNVrLc2m5pr3kche0W0kxjGe-bOkvkMcVSTR3E3hQyWvja0MytvoFVcyHO5rNfu83N6hneaa4MhMqsws7vAHQI0nZe8LUR9CkuaVa5Ah9GSctk07DursmkQ65JJ81Fvhe8HcniTHUDUqYAnHCn5gm5U5PKOPIaCe51LgDxZof5ln0ZceVSm9e_GmyyDQRZFsOMlI4pg8BJ5N9Xw31CouMml762yH2Th1rwvMQq7JaLzy63Cr3_hSiM9Ww34cVd7gWc1kuLlNJxXFKw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
با اعلام خواهر الهه حسین نژاد، بهمن فرزانه قاتل امشب اعدام خواهد شد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 31.9K · <a href="https://t.me/alonews/121176" target="_blank">📅 23:22 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-121175">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ocmn05GMp2fBeHtpPdVaaH0mVVXw4Mp4D5y2A2MUqNsRZxleInjw_16D93iA_NDi_OQ1rGnCId_iqBxDqMkYkxEvzrzaUVOZgkM6yv6JklC9oFndv3z9i3x7xpBWSS7I8WLW3793eYVJcgUPhew86HGVhXYiMS8ZEdGMKA4JC7DJPmVTLnmIm58ksIa9AfN5oxtcJP1OKfzIzuQuRMfrR7hG4dnv1YqaAv-q03hrJ7ZjFVSm5vgiLFBBvy-mnOIQzV8SM89Ek3oVsYkawmuA472liVvGWkXTsAvFOl0K_AAl50YbMAelZCn2uyq9l7EGBIyHNsJIfPZSeLnSkiJV7w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
تصویری وایرال شده و پربازدید از رشت
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 32K · <a href="https://t.me/alonews/121175" target="_blank">📅 23:13 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-121174">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">👈
برد کوپر، فرمانده سنتکام درباره مدرسه میناب : بررسی نظامی آمریکا درباره انفجار مدرسه‌ میناب پیچیده‌ست - چون این مدرسه داخل یک سایت فعال موشک‌های کروز جمهوری اسلامی قرار داشته - هر دو طرف باید اسناد مربوط به این مدرسه رو منتشر کنن و پرونده کشته‌شدن این تعداد…</div>
<div class="tg-footer">👁️ 32.3K · <a href="https://t.me/alonews/121174" target="_blank">📅 22:56 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-121173">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/42f2f8fd3f.mp4?token=s_CwvUUFhFIGqWBJmL6aS7l-YWbekcLzp7G3aoyGVwVAgINfLHP4Ar89FrvRAwtkB-Q8BdzsHHmHhXZExcEM6MsIZykeCuALQHpFpRilUxzxW2QlSQqOr96p4Obvp8uHCkxlotHbi71DnaF5_3G3NfC-so98rjSrTwyUFhGe7lp7Fegal1v5XPiJ1ctAxE5GkvEmJ97iS0vDztHsYMhmdrJ8WNEHf2tUkc6v8Y9FOT6CHbpzqj5k6f_2-cNe1F-ENjaALfDr6_9-n_fcOD0utiSPdgMWnVNG_5fJlZNqvSAm-Sxuw179BisyZF86f7j0g0aQCOsY7i3Q-B7q74b3rA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/42f2f8fd3f.mp4?token=s_CwvUUFhFIGqWBJmL6aS7l-YWbekcLzp7G3aoyGVwVAgINfLHP4Ar89FrvRAwtkB-Q8BdzsHHmHhXZExcEM6MsIZykeCuALQHpFpRilUxzxW2QlSQqOr96p4Obvp8uHCkxlotHbi71DnaF5_3G3NfC-so98rjSrTwyUFhGe7lp7Fegal1v5XPiJ1ctAxE5GkvEmJ97iS0vDztHsYMhmdrJ8WNEHf2tUkc6v8Y9FOT6CHbpzqj5k6f_2-cNe1F-ENjaALfDr6_9-n_fcOD0utiSPdgMWnVNG_5fJlZNqvSAm-Sxuw179BisyZF86f7j0g0aQCOsY7i3Q-B7q74b3rA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
برد کوپر، فرمانده سنتکام درباره مدرسه میناب : بررسی نظامی آمریکا درباره انفجار مدرسه‌ میناب پیچیده‌ست
- چون این مدرسه داخل یک سایت فعال موشک‌های کروز جمهوری اسلامی قرار داشته
- هر دو طرف باید اسناد مربوط به این مدرسه رو منتشر کنن و پرونده کشته‌شدن این تعداد دانش‌آموز نیاز به شفافیت کامل داره
- انتظار شفاف‌سازی از طرف جمهوری اسلامی رو نداریم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 33.5K · <a href="https://t.me/alonews/121173" target="_blank">📅 22:50 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-121172">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tC4QanH4eDyljhPNvLRengegQsHx4gfyIVN0Ql1ofno9WcVmpv-Pb3elLQVxNIzgU0Io_1cTrna8RHH02qXusbHm6e1-YXKLHtzwDR4vqd5twnW1wHV9maOF2TrO9APEU-e2JlSsw7zXuNr3Wz2Qg67AExgA14SvrinjWhEMtt5Vl8pJwZ6lnLmLZZI13naGjTGBV55nSGxQ-byh2mn8BrTc2lNo8vi_y1-MiAZm7lhv8KbTMQ2XUx21zGLyQ5QdZhDa_2xTbZbZN1xfTqbvBr6jl-UV7gCndZR6isqZy_QSoKtGRamVFUjBHKpWzAkcxwRDvvU74mN9UKwtdp4evQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
کارشناس صداوسیما : وقتی ترامپ بگه می‌خواد حمله کنه؛ حمله نمیکنه
🔴
ولی وقتی بگه داریم مذاکره میکنیم، یعنی می‌خواد حمله کنه
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 33K · <a href="https://t.me/alonews/121172" target="_blank">📅 22:40 · 29 Ordibehesht 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>

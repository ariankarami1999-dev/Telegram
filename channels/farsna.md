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
<img src="https://cdn4.telesco.pe/file/fG3vvJuw8T0fTfzgoZQSwspEbnIiHj6b5SiEaW0aWg04oHDP7d6U2G2L7jAdOlA6vS4QA7a1-vZyMFFrPtFdItfAiyqSl5N7WVLPoZibzYwFJm394cS3r7peijNEgrhumMIzkkCgHwKgn6twj8M2_JdUoriEpI2Hg5WEiuUThUVPAqt2CgzibHpFYMyIHKYRWyNRL3e8PHMT9qf_GstdYDFbQJHdteAIhYVsmC_4mlgTrxcPmBIH053i9w1OkA_KB1GRnlCH_ANgR6Wl1c46eyhEAo9zxmPNha5mg1Mu8B2a4qb3wIG4bQfU_6V8pIUBPMjpfJ03G2pgdjtARIzUrQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرگزاری فارس</h1>
<p>@farsna • 👥 1.82M عضو</p>
<a href="https://t.me/farsna" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 حقیقت روشن می‌شود‌‌تبلیغات@Farsnews_adsارتباط@FarsNewsفارس‌پلاس@Fars_Plus‌ورزش@SportFarsجهان@FarsNewsIntعکس@FarsImagesپیام‌رسان‌ها@Farsnaاینستاگرامinstagram.com/fars_newsتوییترtwitter.com/FarsNews_Agency</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-06 02:23:05</div>
<hr>

<div class="tg-post" id="msg-453047">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0717616cf6.mp4?token=j5OYPsvSopFMUwES5q1rQmEYiDDPZmgiQGzozfWxjY-YsRZ_GYOrS4JwmHkiTUsLAoRL7iIAIwWIfraJpkxSCETMn81qenP8PVCZy1vs6T4sZPUOPyGz7-HKan9siKEImn9kl_wY11EVwVgTftbb-3k6pjHsXzVpK_p86Hk1gdBpzYAvVc2fNMcp21n0p_cHmXq8zVEN1d2UOpfBZu53Tocr_P8Ewg8IJwe67KwtxKGOcDdkn5UWiaNiAUejAj5Ty-um6Z_S643UFWdQubMonkOwmRI99woL-27QWnHi7ORLm_ixiRqUQBq43SU1pnT7a2CgLvkiB0YT6Ry4FuEofg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0717616cf6.mp4?token=j5OYPsvSopFMUwES5q1rQmEYiDDPZmgiQGzozfWxjY-YsRZ_GYOrS4JwmHkiTUsLAoRL7iIAIwWIfraJpkxSCETMn81qenP8PVCZy1vs6T4sZPUOPyGz7-HKan9siKEImn9kl_wY11EVwVgTftbb-3k6pjHsXzVpK_p86Hk1gdBpzYAvVc2fNMcp21n0p_cHmXq8zVEN1d2UOpfBZu53Tocr_P8Ewg8IJwe67KwtxKGOcDdkn5UWiaNiAUejAj5Ty-um6Z_S643UFWdQubMonkOwmRI99woL-27QWnHi7ORLm_ixiRqUQBq43SU1pnT7a2CgLvkiB0YT6Ry4FuEofg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
منابع عربی از حمله به مواضع تروریست‌های تجزیه‌طلب در اربیل عراق خبر می‌دهند.  @Farsna</div>
<div class="tg-footer">👁️ 2.58K · <a href="https://t.me/farsna/453047" target="_blank">📅 01:59 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453046">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d65ef6bc8b.mp4?token=U4O7bzh9eaDVt9y4BuII99SVWGi13fZ_jjzU_98wTynRxM4dnUFxDBUPzFDp17Z_r2Ke1mzTL6Q9Uqf4iR0fgrA4Z4EMh4l3GYgeaukmNIT7fClL7qcGkw30RHkFxBscfrpBD5WO2c49o8ahajD89a97WM6xDGfWL7oHQppCjb8Fj_ntj-kxXWVHWAVcLhAcTL1IZjXjyN7AonU-FAmnneD8Hpn118Bmc88zQoAIMjY9fLzobsMeVC95Jcn5zieUhB6dCat8mneCmiEev91b16lp8ZboxLreQutxBiHEFI_ik7e22DlCM0s7lRz5PPkH-Kk2QmDfLkYXETCIe-XB1Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d65ef6bc8b.mp4?token=U4O7bzh9eaDVt9y4BuII99SVWGi13fZ_jjzU_98wTynRxM4dnUFxDBUPzFDp17Z_r2Ke1mzTL6Q9Uqf4iR0fgrA4Z4EMh4l3GYgeaukmNIT7fClL7qcGkw30RHkFxBscfrpBD5WO2c49o8ahajD89a97WM6xDGfWL7oHQppCjb8Fj_ntj-kxXWVHWAVcLhAcTL1IZjXjyN7AonU-FAmnneD8Hpn118Bmc88zQoAIMjY9fLzobsMeVC95Jcn5zieUhB6dCat8mneCmiEev91b16lp8ZboxLreQutxBiHEFI_ik7e22DlCM0s7lRz5PPkH-Kk2QmDfLkYXETCIe-XB1Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
زائران ایرانی در مسیر پیاده‌روی اربعین از نجف تا کربلا هم تجمعات شبانه را ترک نکردند
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 5.05K · <a href="https://t.me/farsna/453046" target="_blank">📅 01:15 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453045">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">گزارش‌ها از حمله به کنسولگری آمریکا در اربیل
🔹
منابع رسانه‌ای عراقی با اشاره به وقوع بیش از ۷ انفجار در حومۀ اربیل، خبر دادند که کنسولگری آمریکا در این شهر نیز هدف قرار گرفته است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.05K · <a href="https://t.me/farsna/453045" target="_blank">📅 00:54 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453044">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">🔴
منابع عربی از حمله به مواضع تروریست‌های تجزیه‌طلب در اربیل عراق خبر می‌دهند.  @Farsna</div>
<div class="tg-footer">👁️ 7.32K · <a href="https://t.me/farsna/453044" target="_blank">📅 00:48 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453042">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">🔴
منابع عربی از حمله به مواضع تروریست‌های تجزیه‌طلب در اربیل عراق خبر می‌دهند.
@Farsna</div>
<div class="tg-footer">👁️ 7.75K · <a href="https://t.me/farsna/453042" target="_blank">📅 00:43 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453041">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">گزارش‌ها از حمله به یک میدان گازی در شمال عراق
🔹
منابع محلی از حمله به میدان گازی خورمور در استان سلیمانیه واقع در منطقۀ کردستان عراق خبر دادند.
🔹
همزمان پهپادهای تهاجمی خارجی نیز در آسمان اربیل، مرکز منطقۀ کردستان عراق، به سمت اهداف خود پرواز می‌کنند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.94K · <a href="https://t.me/farsna/453041" target="_blank">📅 00:32 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453039">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/27662a2de4.mp4?token=cUqhRIka03w7HrY_TUO-FBAWuegfA_--uk8pSW4A23-9f5rWZBR-19GA3NhJ1UebaIuioIWTEe8t96dK1DVtI1Js5hXDGB3Ayb8xhlRl81mMTNpU2mOmbvUKiPEg_duJrCkbKKwJDsiVNa21mz03oheLrTbaUGpbvcyFIA1mNR5vHpZf5GFTAbJ3He2yBOMJPt4xeOBU9A-uxzLx3ctMfhW57BloI9JAnMoloeYw9zjtxDEMvGgHr0oK2fS2JHYQV13hopo7LULD2To6nVMvIiSRJF56a4Cc-Txtcr3Rk3gD6JP5AHdA9drCJ_SAsnym-0lFF4SueNly6n0LAPfhbA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/27662a2de4.mp4?token=cUqhRIka03w7HrY_TUO-FBAWuegfA_--uk8pSW4A23-9f5rWZBR-19GA3NhJ1UebaIuioIWTEe8t96dK1DVtI1Js5hXDGB3Ayb8xhlRl81mMTNpU2mOmbvUKiPEg_duJrCkbKKwJDsiVNa21mz03oheLrTbaUGpbvcyFIA1mNR5vHpZf5GFTAbJ3He2yBOMJPt4xeOBU9A-uxzLx3ctMfhW57BloI9JAnMoloeYw9zjtxDEMvGgHr0oK2fS2JHYQV13hopo7LULD2To6nVMvIiSRJF56a4Cc-Txtcr3Rk3gD6JP5AHdA9drCJ_SAsnym-0lFF4SueNly6n0LAPfhbA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
حال و هوای عمود ۳۴۰ مشایه نجف تا کربلا
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.25K · <a href="https://t.me/farsna/453039" target="_blank">📅 00:20 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453038">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0bf9d824db.mp4?token=UoY4QKpnJ1SRMgRmm39Hz8VztkPqoEn1tXvrST5JrHJxSq6RzzALjfTnaJ5c_0P0CAyouWr85jET2Bidl3BVm8hwidu_a74qB5jW71i67ZW4XYBB83XJH97y5J_uCKg5rm2bBq5mLCsqj-9Jw_tOwzfpuQ7UoQwlLW8DgazJTRGLSZew3-iB8gcmCkneSg5Jz3vFbgQIpVn8CQfV6XCokc7rFOfxjkjJCSrs-FVGkyRIeq9G93GPXGiLssnpon-BYE2zFaZoMbP-wDsnfKfOiagW0RbEwX1Md56U1Qp-kQMKu8YiNvTiP98HgnoYf3fC0F4V8ij45S8wp_LDlyQA7Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0bf9d824db.mp4?token=UoY4QKpnJ1SRMgRmm39Hz8VztkPqoEn1tXvrST5JrHJxSq6RzzALjfTnaJ5c_0P0CAyouWr85jET2Bidl3BVm8hwidu_a74qB5jW71i67ZW4XYBB83XJH97y5J_uCKg5rm2bBq5mLCsqj-9Jw_tOwzfpuQ7UoQwlLW8DgazJTRGLSZew3-iB8gcmCkneSg5Jz3vFbgQIpVn8CQfV6XCokc7rFOfxjkjJCSrs-FVGkyRIeq9G93GPXGiLssnpon-BYE2zFaZoMbP-wDsnfKfOiagW0RbEwX1Md56U1Qp-kQMKu8YiNvTiP98HgnoYf3fC0F4V8ij45S8wp_LDlyQA7Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
خبرهایی از سقوط پهپاد آمریکایی در عراق
🔹
رسانه‌های عراقی تصاویری از سقوط پهپاد آمریکایی در نزدیکی سد حدیثه در استان الانبار منتشر کردند.
@FarsNewsInt</div>
<div class="tg-footer">👁️ 9.15K · <a href="https://t.me/farsna/453038" target="_blank">📅 00:13 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453037">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/394406b222.mp4?token=dB-RDE7YXb6juqW1OufHAoXwem6nTTQ49VR360yIeaGKpke11k5xhzx-xChyOKDEgXAkkTK0vVxVGegz9xPac5DBAK5WPQRM-yU4WMDyOaHZb7XGFKc-uvVHcxY-lM4dSr8zfwgjyc2oN5VCD_31K5vqHyETugPHDCBkPdz6FxPQi4LeMdy6srdCiFpKnKSltTMl1IMXputFBMqSsX5eVyz4GOqoPeppgmlDGWzIt4K9tHCmlUtHl_mths8LSrUlDJ7o9SQlfGz25yuoEVKoRJdTnWlgm0CWmY4g99nviM82cwBFYlcQ-A1cQ9Fq5vUZSmOfv0bVmMiviAfhpDpJ9A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/394406b222.mp4?token=dB-RDE7YXb6juqW1OufHAoXwem6nTTQ49VR360yIeaGKpke11k5xhzx-xChyOKDEgXAkkTK0vVxVGegz9xPac5DBAK5WPQRM-yU4WMDyOaHZb7XGFKc-uvVHcxY-lM4dSr8zfwgjyc2oN5VCD_31K5vqHyETugPHDCBkPdz6FxPQi4LeMdy6srdCiFpKnKSltTMl1IMXputFBMqSsX5eVyz4GOqoPeppgmlDGWzIt4K9tHCmlUtHl_mths8LSrUlDJ7o9SQlfGz25yuoEVKoRJdTnWlgm0CWmY4g99nviM82cwBFYlcQ-A1cQ9Fq5vUZSmOfv0bVmMiviAfhpDpJ9A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
افشاگری مقام عراقی دربارهٔ بازداشت گروه‌ خرابکار وابسته به اوکراین
🔹
مشاور امنیت ملی عراق: هسته‌های اطلاعاتی اوکراینی در عراق حملاتی را اجرا می‌کنند و آن را به گروه‌های مقاومت نسبت می‌دهند.
🔹
نهادهای عراقی افراد و عناصری را بازداشت کرده‌اند که در بازجویی‌ها اعتراف کرده‌اند که هسته‌های اوکراینی‌ حملاتی را علیه تاسیسات حاکمیتی عراق انجام داده‌اند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.55K · <a href="https://t.me/farsna/453037" target="_blank">📅 00:07 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453036">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1387c0f59e.mp4?token=RvMCGI20KqzAWWzJQ3kU2LBnPjhTnOcIUNZjMxLg_PiZfYIQci9NC0KdCIZr2opz4GVwQ9tUC3CG0bh5_sPTEaP71mfTdZywbpTAm3jxlnyCeIYApA9bIKZ_PnkBPTJrgdXNsCpljqaoFMZNlj7NkQ3PQqtcAyxY-rS8qab7tAZKraC8DEAz-Q6Y9mDMkPYO_ol1krTrs9EW_p0iJqzzxP_Ec98z9hwFf55gd8r9-gO1DPo1Ij6hKie9x16tymO9NB4ZCsy_PExPLwCLzSOPUyLcUoJ72eYntUjVHMAwT7Q4aS2VwwIn_-Gznu-3ECZ1kkDsFn7e5zCWwexf9Gwsxg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1387c0f59e.mp4?token=RvMCGI20KqzAWWzJQ3kU2LBnPjhTnOcIUNZjMxLg_PiZfYIQci9NC0KdCIZr2opz4GVwQ9tUC3CG0bh5_sPTEaP71mfTdZywbpTAm3jxlnyCeIYApA9bIKZ_PnkBPTJrgdXNsCpljqaoFMZNlj7NkQ3PQqtcAyxY-rS8qab7tAZKraC8DEAz-Q6Y9mDMkPYO_ol1krTrs9EW_p0iJqzzxP_Ec98z9hwFf55gd8r9-gO1DPo1Ij6hKie9x16tymO9NB4ZCsy_PExPLwCLzSOPUyLcUoJ72eYntUjVHMAwT7Q4aS2VwwIn_-Gznu-3ECZ1kkDsFn7e5zCWwexf9Gwsxg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
تردد شبانهٔ زائران در مرز خسروی
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.29K · <a href="https://t.me/farsna/453036" target="_blank">📅 23:57 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453035">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3be59b32e3.mp4?token=XFMXNdKRCfWg-c42mB8KSx8cr5tA85yZQWqAYamyuEpWb7t7pJTxZ7alvt2_hRFarRqmGMTG-RlbUr5GWqDVoq_FC92CfycO0x3OJkj6zOx6M8HIZLLNYks0pa8cLtxyfor_4Q4JaomiVGKszO1sR4A7bh4EUr3HVbLubkGAdANaTqUgCIBcFG8UuSKDBczC6JLM_nRWE6iZhog-EkdhlqontqVS5Y2-of6LPcFfpzg86uhIupGvIziIlV1_QVqOXe38Wht7PJQ0vEwE727PYhthdopNeQ8h_jvUSlIQy5smXPhEwfhjuh6mPo7MXoOOzJeCpge-ZpTEmAktDtD_YQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3be59b32e3.mp4?token=XFMXNdKRCfWg-c42mB8KSx8cr5tA85yZQWqAYamyuEpWb7t7pJTxZ7alvt2_hRFarRqmGMTG-RlbUr5GWqDVoq_FC92CfycO0x3OJkj6zOx6M8HIZLLNYks0pa8cLtxyfor_4Q4JaomiVGKszO1sR4A7bh4EUr3HVbLubkGAdANaTqUgCIBcFG8UuSKDBczC6JLM_nRWE6iZhog-EkdhlqontqVS5Y2-of6LPcFfpzg86uhIupGvIziIlV1_QVqOXe38Wht7PJQ0vEwE727PYhthdopNeQ8h_jvUSlIQy5smXPhEwfhjuh6mPo7MXoOOzJeCpge-ZpTEmAktDtD_YQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
عکس شهدای میناب در شهر امیرالمؤمنین(ع)
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.81K · <a href="https://t.me/farsna/453035" target="_blank">📅 23:44 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453034">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d86351cbbf.mp4?token=mATzoUMKDjdpSKCdg_rNTaq3Mf_nzQkf99jihiPEwfbjF1wz7GzrhTIx6k06QQBJAkAypvMD7KNdQYQPjKnbaWDBNlY8SwVp9GYh2duv4KeJpNlnAjasNREzw24yJdm_-maK3DoqJqzsbaIO0DmODmiAW74a0QyV5zSJ5UWreuKWa7WmWzeV0Ig5p0vm0ANng4YFva7dL1X5_temc0Iu1t8TSMGjMJMMwUjGN2NQi6-uC2N77BjkIRpc0LgHWxzh9bADTs0nHPAEutQUsxR0Dwu2Zh-bzDE8GArR2KUidquxmxeM2uHo8T04QJU-hbdKnksD3Y6HvIeUUlcY-TlsgStdVgvdTbJnaHRLW19Ke6uB1rRtdUD_4EHE_1kypPpBFF3n_wkbbDgnsF8RYt7aLFIG3dPqOSUpqXoDzvlx0ewc91d0H5XZ__Qaz-oG_scH6Y7God-oUi834jfF4ZqmqCGopS6bhtrcB7dTjoxyCGlu-nqoctfUfbh2b_PurLs0VlxcVO5OZK4cS7VR3WfpYhuZpfcUKnHOhByJlEnr2WXQbiZxFS5QbXl7uLCCO8CJkmy1uIJ2C1DTejVuSc-qs7m9h30hQs6yJDPjhgFpGYk8cI8gASuIhsZgxQ8X6SyC7kJ6NI9ePAJte21yl5iK9PrOjAgpiW-Zpt1swHTj91E" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d86351cbbf.mp4?token=mATzoUMKDjdpSKCdg_rNTaq3Mf_nzQkf99jihiPEwfbjF1wz7GzrhTIx6k06QQBJAkAypvMD7KNdQYQPjKnbaWDBNlY8SwVp9GYh2duv4KeJpNlnAjasNREzw24yJdm_-maK3DoqJqzsbaIO0DmODmiAW74a0QyV5zSJ5UWreuKWa7WmWzeV0Ig5p0vm0ANng4YFva7dL1X5_temc0Iu1t8TSMGjMJMMwUjGN2NQi6-uC2N77BjkIRpc0LgHWxzh9bADTs0nHPAEutQUsxR0Dwu2Zh-bzDE8GArR2KUidquxmxeM2uHo8T04QJU-hbdKnksD3Y6HvIeUUlcY-TlsgStdVgvdTbJnaHRLW19Ke6uB1rRtdUD_4EHE_1kypPpBFF3n_wkbbDgnsF8RYt7aLFIG3dPqOSUpqXoDzvlx0ewc91d0H5XZ__Qaz-oG_scH6Y7God-oUi834jfF4ZqmqCGopS6bhtrcB7dTjoxyCGlu-nqoctfUfbh2b_PurLs0VlxcVO5OZK4cS7VR3WfpYhuZpfcUKnHOhByJlEnr2WXQbiZxFS5QbXl7uLCCO8CJkmy1uIJ2C1DTejVuSc-qs7m9h30hQs6yJDPjhgFpGYk8cI8gASuIhsZgxQ8X6SyC7kJ6NI9ePAJte21yl5iK9PrOjAgpiW-Zpt1swHTj91E" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
نایب‌رئیس مجلس: نباید اجازه دهیم آمریکا هرموقع دلش خواست حمله کند و هرموقع به مشکل خورد عقب برود
@Farsna</div>
<div class="tg-footer">👁️ 8.48K · <a href="https://t.me/farsna/453034" target="_blank">📅 23:39 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453033">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6f820943e2.mp4?token=ag1pxXJLwwWBcQgRGiQDXzrDlMyLflUDiN1Q5oaZ7xqmOMutQDmagLiYU09AQeVvuri97tSKKun29lFKzcsnoTgROP8666N1whhDMe-JzZtlPtjO3NxfSVjlxeal0WGwiUPepcrhm52cgkgaWcY2BmCVqTYwYEIW5T-v0lm6Bhpbsi0Zi3Nz4PbWWe9SfZA0KSwspCzJ9vhNcaYM55iXD2k70YQ5NZeXmODberXMEc7LL8sQ1myifleZ2_4dy7FlguFt1AT4ovV5Ec3gTGiJBmkAnjaZL4eiMhvK8ecHzGLiKsPK5EB1SMtnoYb2nd0se-IOLjyWPp64EytUjgntuQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6f820943e2.mp4?token=ag1pxXJLwwWBcQgRGiQDXzrDlMyLflUDiN1Q5oaZ7xqmOMutQDmagLiYU09AQeVvuri97tSKKun29lFKzcsnoTgROP8666N1whhDMe-JzZtlPtjO3NxfSVjlxeal0WGwiUPepcrhm52cgkgaWcY2BmCVqTYwYEIW5T-v0lm6Bhpbsi0Zi3Nz4PbWWe9SfZA0KSwspCzJ9vhNcaYM55iXD2k70YQ5NZeXmODberXMEc7LL8sQ1myifleZ2_4dy7FlguFt1AT4ovV5Ec3gTGiJBmkAnjaZL4eiMhvK8ecHzGLiKsPK5EB1SMtnoYb2nd0se-IOLjyWPp64EytUjgntuQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
حمایت مردم از رزمندگان اسلام و خون‌خواهی امام شهید به ۱۴۹ شب رسید
@Farsna</div>
<div class="tg-footer">👁️ 8.4K · <a href="https://t.me/farsna/453033" target="_blank">📅 23:33 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453032">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8e4ffd812c.mp4?token=lcrfid4bfgbXuvfoySyz_K3WKSfxrRVg8qsfne74SdbLDGfLs_X8Q-rMufeKwhlNNaCn3Pp5vwUNglCdMmB0li0n6RnYgI0PLRdCcRicrDoZDe4Ic7uioQLts428xmQ14RE-TXoKlrmw8wB5N1kaXPbkzTZI_gicOMtC1Y9Lgg8EMN2pAIw_zjca726d7WLCy8Hc7GkMmI1rthZ2ob_GdQQNCjenwVhOn43xzNH3uF2ZqzGGNWRgdLGfKsdNaeJR0dX7q--91Q4E5IxYbTGin3zI26Y2ollwRPieTOXHg2ZnHSmvGN7-gK3IPjVi1iNMedNMrWan1msWYKPElaUPqQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8e4ffd812c.mp4?token=lcrfid4bfgbXuvfoySyz_K3WKSfxrRVg8qsfne74SdbLDGfLs_X8Q-rMufeKwhlNNaCn3Pp5vwUNglCdMmB0li0n6RnYgI0PLRdCcRicrDoZDe4Ic7uioQLts428xmQ14RE-TXoKlrmw8wB5N1kaXPbkzTZI_gicOMtC1Y9Lgg8EMN2pAIw_zjca726d7WLCy8Hc7GkMmI1rthZ2ob_GdQQNCjenwVhOn43xzNH3uF2ZqzGGNWRgdLGfKsdNaeJR0dX7q--91Q4E5IxYbTGin3zI26Y2ollwRPieTOXHg2ZnHSmvGN7-gK3IPjVi1iNMedNMrWan1msWYKPElaUPqQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
پرچم خون‌خواهی همچنان در میدان سلیمانی کرمان بالاست
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.6K · <a href="https://t.me/farsna/453032" target="_blank">📅 23:29 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453031">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bqT41hv8pqcCXOH48yiW2pYbqqlXtZQ_bVrohJWcWRWkjkYjF5h6YydtujpJK0BOw1yTyWGg5GyDZ_T2dXtjXEakL3kkUYrt5UJpweFSRm5p051y1vNCzYrfIe3JHbu0lbfjvS-VEFzwQtFL68wy4eCgwqgBqLib3ymu7bou6Yz80ykWQHpOV1kjYimQLp1-GdWMduVCTJpOazMLfl6pF_7b4Oh6HIe0tafH99-j_nkXj3sHp5gGQsCzY_uej6r11v1e-KRhYaLvvmWe_oRip5T7D8fUGSMBx6-aTbTJGsAFWHh7Xql3PoTu-FLU2rybnMEVMWrxdVHZZwNZW9_cXg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
مقاومت اسلامی عراق: هر اقدام احمقانه سعودی‌ها با پاسخی قاطع روبه‌رو می‌شود
🔹
رژیم سعودی ادعا می‌کند که عراق منبع حملاتی به برخی تاسیسات نفتی آن است؛ این ادعاهای بی‌اساس، تلاشی برای توجیه ناتوانی در پاسخ دادن به حملات موثر یمن به زیرساخت‌های عمیق آنهاست.
🔹
ما در مقاومت اسلامی به رژیم سعودی هشدار روشنی می‌دهیم که هر اقدام احمقانۀ آن‌ها با پاسخی قاطع مواجه خواهد شد که آن‌ها را وادار به پشیمانی خواهد کرد.
🔹
شما امروز بیش از هر زمان دیگری به لغو محاصره ظالمانه بر مردم یمن نیاز دارید، به‌جای اینکه به این‌سو و آن‌سو اتهام بزنید تا شکست خود را توجیه کنید.
@Farsna</div>
<div class="tg-footer">👁️ 8.85K · <a href="https://t.me/farsna/453031" target="_blank">📅 23:21 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453030">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3ad1f2e048.mp4?token=TdeeFA2Mlj6yZv92zhxVe2I4QW5k9bAbaYZ4OVN47D96ZDubMpuohjvkHbpi5FlO4CTH-prZMSGDwXu2nhQvL_HQ4r1M_YTPh99VyHFyPcXpNttxJ-FUQk5c9dRQF4ori2d0O4_3NOzYjBfXe-FOYDi908JFQ-vH66rH-cdYHxiY6sXGKRpmeet6KKAcfTQAW261R9GSHMcvD6oNKP2Ihz4ZrRdUsLqYmMpWVSyoQj5s98ArhATwVJCuYYJlGW6L6sH_jE5W_QeYCyh-g_Pp43quluy2Sc1Dvc5q7ByZeeUzn1cM1gwd9eOo3G_ZHOPz33gvp9vyIFR8Q3mLoOcMAA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3ad1f2e048.mp4?token=TdeeFA2Mlj6yZv92zhxVe2I4QW5k9bAbaYZ4OVN47D96ZDubMpuohjvkHbpi5FlO4CTH-prZMSGDwXu2nhQvL_HQ4r1M_YTPh99VyHFyPcXpNttxJ-FUQk5c9dRQF4ori2d0O4_3NOzYjBfXe-FOYDi908JFQ-vH66rH-cdYHxiY6sXGKRpmeet6KKAcfTQAW261R9GSHMcvD6oNKP2Ihz4ZrRdUsLqYmMpWVSyoQj5s98ArhATwVJCuYYJlGW6L6sH_jE5W_QeYCyh-g_Pp43quluy2Sc1Dvc5q7ByZeeUzn1cM1gwd9eOo3G_ZHOPz33gvp9vyIFR8Q3mLoOcMAA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
نمایش پایداری بروجردی‌ها در شب ۱۴۹
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.91K · <a href="https://t.me/farsna/453030" target="_blank">📅 23:20 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453028">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">🔴
منابع عراقی از انهدام یک پهپاد آمریکایی در استان الانبار در غرب عراق خبر می‌دهند.
@Farsna</div>
<div class="tg-footer">👁️ 8.5K · <a href="https://t.me/farsna/453028" target="_blank">📅 23:15 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453027">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b065ff32e8.mp4?token=BLMWIh3pZMQ6H6qEp6dNdIAtdasuwYOvsKuUxW5A7g67LvqcQJkumTkIs-8uEhdf7wMt16x5wEdRO_5Dvjiv5cJQrKlCG6m6JPMItl8K1AdDaLtwVLFF0aZfjpPMT7eD0wjcxxcrdMSDOUR_0BOSw5vBJhbuXAslbswbm8seofuzFSGBrm3UnUtSUkSZIotdIwIXko-KfYgH8-rV_4-MXO_6kZr9MftFH9GMHHAOZpM8OjhtFJxPKn9TaXxb56UMWqzuGspiXLObfVVnvn13LqgDKnujcZYP1mr9aUOHtpLSIbXol2NbVrtPeXTKfjRG_p6RTiv0bPxjEx3vfSO7Eg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b065ff32e8.mp4?token=BLMWIh3pZMQ6H6qEp6dNdIAtdasuwYOvsKuUxW5A7g67LvqcQJkumTkIs-8uEhdf7wMt16x5wEdRO_5Dvjiv5cJQrKlCG6m6JPMItl8K1AdDaLtwVLFF0aZfjpPMT7eD0wjcxxcrdMSDOUR_0BOSw5vBJhbuXAslbswbm8seofuzFSGBrm3UnUtSUkSZIotdIwIXko-KfYgH8-rV_4-MXO_6kZr9MftFH9GMHHAOZpM8OjhtFJxPKn9TaXxb56UMWqzuGspiXLObfVVnvn13LqgDKnujcZYP1mr9aUOHtpLSIbXol2NbVrtPeXTKfjRG_p6RTiv0bPxjEx3vfSO7Eg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ: ما چندین میلیارد دلار از ونزوئلا درآمد به‌دست می‌آوریم؛ این اتفاق دربارۀ ایران هم خواهد افتاد  @Farsna</div>
<div class="tg-footer">👁️ 8.76K · <a href="https://t.me/farsna/453027" target="_blank">📅 23:15 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453026">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">🎥
ایستگاه ۱۴۹ تربتی‌ها در قرار شبانۀ خیابان
@Farsna
-
link</div>
<div class="tg-footer">👁️ 8.85K · <a href="https://t.me/farsna/453026" target="_blank">📅 22:59 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453025">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d6cf4aed0f.mp4?token=YGnlNgugNah1AQ_gV1tmoXXc9HVX5nuz0Zy_mIIztoKxtE0LuktQmnjXpBn__VXvvnyDzQKEuLvUQ8gESoUuAiclPW0VHxDZ9MK1SshduBWD1ir1tqQVvsJdjgCdo3lsqoDKk5Gbx2XBRqkVlc6je-_iX7aGY4XGweW-G14T1XWWLad4yr5vqIlC-VFOZjNrT_79Z1U9qSZkXzIwKy0bdaKE74YmpeGWGFevlONCfIFcCSpEPuWpBm3pRAd78LzSm-vh0aUOb0h5QMAj3DZ1bWV8FLIbRokNeIz9QNQQsYRuQcEyDTamxpBnRoMMTqtRqcFrhzZY97atu3IcA-4jEjnsueDIh-QOrzAefpsoIBVAN0PNqiGO4i66KdBIIVWrtO01TYvxcwX6aYT_Fa_DN5CGFuyH_pKFTtx3GO2eHluP69kywqdJqJxV7JA94KTHGgyX9BnuqvstYpIECnGPhBJt16NLR6XWjIkZm4Pq3DT264Pwh95TyB7VV9lu33k9CBvsewnVNjOrmqH-aJxtOVaCuhXwsGI-31YQBsJ8kiaZ3Fm9q-QRX1U5ftj_aLZgdmhf4GwW60LI11HI8DR2B9KBH65qG5OVbD1JwXIpm21Es4ni4mf-ndRJP_vG4xLQZ_X6lGqqBndyu08lPm3tRCwsQAxIWgTYU-FtNaAtQa4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d6cf4aed0f.mp4?token=YGnlNgugNah1AQ_gV1tmoXXc9HVX5nuz0Zy_mIIztoKxtE0LuktQmnjXpBn__VXvvnyDzQKEuLvUQ8gESoUuAiclPW0VHxDZ9MK1SshduBWD1ir1tqQVvsJdjgCdo3lsqoDKk5Gbx2XBRqkVlc6je-_iX7aGY4XGweW-G14T1XWWLad4yr5vqIlC-VFOZjNrT_79Z1U9qSZkXzIwKy0bdaKE74YmpeGWGFevlONCfIFcCSpEPuWpBm3pRAd78LzSm-vh0aUOb0h5QMAj3DZ1bWV8FLIbRokNeIz9QNQQsYRuQcEyDTamxpBnRoMMTqtRqcFrhzZY97atu3IcA-4jEjnsueDIh-QOrzAefpsoIBVAN0PNqiGO4i66KdBIIVWrtO01TYvxcwX6aYT_Fa_DN5CGFuyH_pKFTtx3GO2eHluP69kywqdJqJxV7JA94KTHGgyX9BnuqvstYpIECnGPhBJt16NLR6XWjIkZm4Pq3DT264Pwh95TyB7VV9lu33k9CBvsewnVNjOrmqH-aJxtOVaCuhXwsGI-31YQBsJ8kiaZ3Fm9q-QRX1U5ftj_aLZgdmhf4GwW60LI11HI8DR2B9KBH65qG5OVbD1JwXIpm21Es4ni4mf-ndRJP_vG4xLQZ_X6lGqqBndyu08lPm3tRCwsQAxIWgTYU-FtNaAtQa4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
فرزند ارشد شهید سیدحسن نصرالله
:
شهادت امام خامنه‌ای مردم کشورهای عربی را بیدار کرد
🔸
در بعضی کشورهای عربی مردم می‌گفتند ما را فریب دادند، چشممان را بستند و عمداً کاری کردند که رهبر شهید را نشناسیم.
@Farsna</div>
<div class="tg-footer">👁️ 8.69K · <a href="https://t.me/farsna/453025" target="_blank">📅 22:57 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453024">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3a9ab4a2b5.mp4?token=f_Ddz1UyKhUTdV-v_nbFmixIlfkc8K06-yMtmSZqZHi9Fc7KiJkk8JfymD1NPIEAXUvh36LUaZnyTNrSZ0We8fjUnqvGr36bUs-zKqDe3sl0Vx5kHBRz9V_s1CwkcDju0J-t_e5xIGx-hmkKbvSrFoNVndCgg5AZU08aKbrK0Lv3w8fl5u3er-lADKhKRfQS5hFCEZhp34qs4xXes3tXPyAdffUFW8F5pZ-wfaF2oByoyRyXGH2ze2j0G-KZt2tr1KJ3sUCL4IwHmle0dXRBNskiNOkx-MBhlWktmkh2ypkqxiCstkShbtTyao70oFczWNaOzUtCEfH3_pD-XrMoAA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3a9ab4a2b5.mp4?token=f_Ddz1UyKhUTdV-v_nbFmixIlfkc8K06-yMtmSZqZHi9Fc7KiJkk8JfymD1NPIEAXUvh36LUaZnyTNrSZ0We8fjUnqvGr36bUs-zKqDe3sl0Vx5kHBRz9V_s1CwkcDju0J-t_e5xIGx-hmkKbvSrFoNVndCgg5AZU08aKbrK0Lv3w8fl5u3er-lADKhKRfQS5hFCEZhp34qs4xXes3tXPyAdffUFW8F5pZ-wfaF2oByoyRyXGH2ze2j0G-KZt2tr1KJ3sUCL4IwHmle0dXRBNskiNOkx-MBhlWktmkh2ypkqxiCstkShbtTyao70oFczWNaOzUtCEfH3_pD-XrMoAA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
رمی جمرات ۲ شیطان بزرگ در مسیر اربعین
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.78K · <a href="https://t.me/farsna/453024" target="_blank">📅 22:53 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453023">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5eb24ad700.mp4?token=FX42CXyR-uFlRBtMX0Vhg1Su7Yqyg0uvN5v9EYP3GHjA8MK_tBDGpS5JGngq8uh3WmbyN3QrmM0F4rQNTeTPKnHqIhtJZ5hEZ-yC3R_M8jhikmWLBu4CeQmn8Tr-liCwt5YTbWnWuDMHTGCNQBPVDsz9IRWwds_JUeCXL7Um9axWdGOt-9Xb41aVb3vf8IdUaekcsnsxgm3zoVp5_Sjgos7Zo2nGaV98Q4bNduafVlD0esl99jHel7-o7olQrWgaiqDudUUpSMBDmXEIpPnYDxGbBm1fgvDsGI4wxnhGhh-qHacrN_sOmGp8SGpmTyuIjAZ6rlm-S1IDRnSJb1MIgA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5eb24ad700.mp4?token=FX42CXyR-uFlRBtMX0Vhg1Su7Yqyg0uvN5v9EYP3GHjA8MK_tBDGpS5JGngq8uh3WmbyN3QrmM0F4rQNTeTPKnHqIhtJZ5hEZ-yC3R_M8jhikmWLBu4CeQmn8Tr-liCwt5YTbWnWuDMHTGCNQBPVDsz9IRWwds_JUeCXL7Um9axWdGOt-9Xb41aVb3vf8IdUaekcsnsxgm3zoVp5_Sjgos7Zo2nGaV98Q4bNduafVlD0esl99jHel7-o7olQrWgaiqDudUUpSMBDmXEIpPnYDxGbBm1fgvDsGI4wxnhGhh-qHacrN_sOmGp8SGpmTyuIjAZ6rlm-S1IDRnSJb1MIgA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
قرار شبانهٔ مردم زرند در شب ۱۴۹
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.2K · <a href="https://t.me/farsna/453023" target="_blank">📅 22:49 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453022">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/M9-HbuXtkpsvjxgymZKwixr64vcfj34wz0PAOKi2Wz1sTFeaiuW102VS3XS7Hj3bQqp7DaDv4JEstMsVNTdZrxmo6UAZ4kHiv4eDssQhf7UowRClmZDDb4W8nI79XUMtBLRmvJjcDZET0OX-n2OcExFn86PA0OyycPDVL-dkeuMeKE3jM-5BTzm5RQKWCsgeRR8wq05kh5TPqZiTe192ygXraiaMy_RbfyNGdnCLvf2oGqNi8ws8bqeCkCXcjttqm7wNPUGX4veu3_U2zvTWIUEdjuWtU359AjkJFn1YbVIQ4yEmI6rfSo5rl2kVa2dPSv59j8UVAE7dqFi5CY_p2w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
قرارگاه خاتم: تهدیدهای آمریکا را بی‌پاسخ نمی‌گذاریم
🔹
قرارگاه مرکزی حضرت خاتم‌الانبیا : آمریکا در تداوم شرارت و ناامنی در منطقه و به‌دنبال اجرای محاصره غیرقانونی دریایی ایران، طی ۳ روز گذشته اقدام به تهدید شناورها و کشتی های تجاری و نفتکش ایران در آب‌های ساحلی و سرزمینی کشور ما نموده است.
🔹
هشدار می‌دهیم این اقدام آمریکا به منزله توسعه جنگ در منطقه تلقی می‌گردد و همان‌طور که نیروهای مسلح جمهوری اسلامی ایران در میدان عمل ثابت نمودند هرگونه تهدید و شرارت ارتش تروریست آن کشور را بی پاسخ نمی‌گذارند و با آن برخورد خواهند نمود.
@Farsna</div>
<div class="tg-footer">👁️ 9.56K · <a href="https://t.me/farsna/453022" target="_blank">📅 22:37 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453021">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/186282342d.mp4?token=e6I2iQtRlOGc097yA9t5VG2Pjfi1za-ZNpcOnrHfKDeRioOkMnnmhRrnph_9J9loCMp6HGOTh1lRmclAbkC8REfxdzuAlYGATtQui7h8efE3bWKUV8hOoA27f1GWxlVf87P9vxt3DqwDH0wfHWB411GJTHe_9Du-nb6nBu-Irzqmy82IC3EsEeRWtvbjSuFrlG9OIbMkOnesQ6SSEzsbBhGX01Q6SvweLg4PljRSyCPhUJQdSasyZn0j6v5bA8sI7VJk2dq4bjw8rp5gtxGgMpWWpAyPPEQ3e7a6F75zfpCnYnocxxqDVSR7ld-_17vEsip-_AnkbdAk2J9XkbMn6DzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/186282342d.mp4?token=e6I2iQtRlOGc097yA9t5VG2Pjfi1za-ZNpcOnrHfKDeRioOkMnnmhRrnph_9J9loCMp6HGOTh1lRmclAbkC8REfxdzuAlYGATtQui7h8efE3bWKUV8hOoA27f1GWxlVf87P9vxt3DqwDH0wfHWB411GJTHe_9Du-nb6nBu-Irzqmy82IC3EsEeRWtvbjSuFrlG9OIbMkOnesQ6SSEzsbBhGX01Q6SvweLg4PljRSyCPhUJQdSasyZn0j6v5bA8sI7VJk2dq4bjw8rp5gtxGgMpWWpAyPPEQ3e7a6F75zfpCnYnocxxqDVSR7ld-_17vEsip-_AnkbdAk2J9XkbMn6DzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
اینجا تهران است نه کربلا
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.93K · <a href="https://t.me/farsna/453021" target="_blank">📅 22:33 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453020">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3009ae4044.mp4?token=px-Jk3SKVXAXRlq14mxqkGwWQyrcQHyD5HkWuY7CzDYRi6eke8lqMXfnbYdkiE40WuD5JRjUjiMGsuwgvO7stl1ZVXjUXvD19SvwMtea-5NJHtMaPyDDLnLrZNmr6ee5U9pFfQnWiVh-QrQ9wnSGqmP_sA-FxiVRF0G6VGLphEcfH8UfY-kTNqvtznlLULtL6JyOv5yDZ8dL359D_Hzux_BflyOtvRPudGIxlZMUbMeDUZOhz9Q3y-O4CcOqS2J-ogSb8QpjNAk-dGQxfib7Ilh-Hv5FlQB4Lcp7uM3DJuFV6Ajp8en2bx73tzYXVa8dPcMRngIC4c3DkdUN2O_LEw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3009ae4044.mp4?token=px-Jk3SKVXAXRlq14mxqkGwWQyrcQHyD5HkWuY7CzDYRi6eke8lqMXfnbYdkiE40WuD5JRjUjiMGsuwgvO7stl1ZVXjUXvD19SvwMtea-5NJHtMaPyDDLnLrZNmr6ee5U9pFfQnWiVh-QrQ9wnSGqmP_sA-FxiVRF0G6VGLphEcfH8UfY-kTNqvtznlLULtL6JyOv5yDZ8dL359D_Hzux_BflyOtvRPudGIxlZMUbMeDUZOhz9Q3y-O4CcOqS2J-ogSb8QpjNAk-dGQxfib7Ilh-Hv5FlQB4Lcp7uM3DJuFV6Ajp8en2bx73tzYXVa8dPcMRngIC4c3DkdUN2O_LEw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
نماینده ولی‌فقیه در خوزستان برای زائران اربعین نان پخت
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.58K · <a href="https://t.me/farsna/453020" target="_blank">📅 22:32 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453013">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/v_FRW_txJ2mr5ordR7uDXbnrdoF9-OkfTr_XPQwBD1MzXEaeazi2nX4Fbzvw-KWGcib6M50rL7aLzR0WX1xEU2GXw9Nq1pechYkMo5l7M57WkZlCloRijEdANm-__R9xGndwJwn_kkj5113ZSDOadKfdbChTDtRxh1Il9R4Y0GjLG0uOihpZgNfwBXrsMkXKxHsvUcsIGMKb7bBqYZtioLNdVj0NXgSwIJ5sPZxv42QYIxixJ76bY_KE8mwQ40Dhd2qTf33kbsb7crZ6d43jDdqJjaUGoMhh_tmZZdoD0m4LFE40Yn-g7WaNMYjryjgRmluSWuW53Uvfas4s7KF7lw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Jd5pnphMwcweqQA41RnFiEdiFrTi_udbq0bPs6aTlW7pIAghJgAU6sgbbs2BTvMXZtCpyMovACSOL38rEpSNycAKHNrMy2mTe_jiwOmuU6p67MUfEI-HN9G3ZxyoCzl2n5nr8obNjAWbN9rAU3WS3YC7m3i-zMP_10f866Z_1zuSnZICJmquEFCH4wAVDzy6Vbg81u1U5SSW_V9EbMdOPjb9q25RmlpMMdcOBkmQCDJaxNyLiGrj9LlYJfanqPebpd4wWDZc1C2cfkE-ShvH3uYR3EZS9yeXkmm1b-oVhd9xWCArDUNXSIJup_8fLoEWa8_jkJiGr99RQqAa6_JK9g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Md4v4FJIPW_2tYqvzL14Ep74rRRcPXV0tHgLhrWTujDO3IvC9pYH6MVrsykM7aBjOsJCwxCYPINbPTUlcrKGrYI52CCA5lR0YvOfq2_AGgF8Sv1NfUM-Ds34Vs-KO4WJd4-Zo0ony5ZIrk2Ux8F1O-YmSK8-XJ5srIVZJSHi2eBqlb3hHE6fXmvNtML74kvBD_MQkIFJvUo8FDfahyhjU8XbEEigrriCYGolPGwK_2DUF0U9B1622p-s6KI86y4S-EIz0mSxTKAWdtaqaFwkwcDEDmN-T1CBK3dqyDAZyayE-RBtyQQ_BhIUJrMlVIoe3RKfECWX57S9v4AIg_68sQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/g1OXDUeD2YuqBO2kPP8PXzESpKQdj-Cg3ffWXGvbX9JYUchgoL4rh4tahAajSWHLclD0KaKre7iOLGv3YCP8rZPsXMfgPQRk_lae0GmlS0jsHcNJ1PH6qqQSg42f2265ds4cpbrOy2RQSnHGySC_OhEzjXJffx-K6HhHu-sScoT2M84ndfeMjzKvAaKcaa4wOLNm6Ly58bFAJ1VRZpnUmt2nwplt136N0W0znjv370qwcXBEy6HmpmWQYLBC_LLRnrvesBArPg3OvAgwumaLn-u760hS05nKEdD4fjr-1CCpIzFACANxdjbO9AQYFk8qjgZ9jhMlDaPRzlmp61RfBQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/SbDrr8xQju2KZOPSoSHLHPzrNOnzMCam3dQETlZc2BxGkO0uAkqI4_I_NlhOQI7JiaiZE4VbxSWjFMhu0hWmgwgYQSfpicc8fqan_4VaeIGCkVuqGLy1WfxaDWH2CHwUfAPYELSVgrI_eHh6wMGEE1GCqshZhBMg0Ahw1RmKgAudJcttl6D4kWdLanY7yQltyVOZ3Xy7GIJpH7LXL9aHAIOxHYV8jO-ktP_R9_zd1VTtwGlIzSawNT8ggKrQAVZXlhPWHDmovFugANhjjXGertX4QNCdBOiZARzOVaEAnE2KQ11TmBlS_x2HneHO3ssWHnOx0FFkmyOBVLbxDurtog.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/erWyqcXWka971_mFXHGnSDmnWJjwGfWapdvoqicMBYbRWVvpuTvBCk9ZpWIqzGeXgSOqGhELU2LoG7dR4KkA2HKGydEjWXmd2LT9I7qb65DK8lUiP-_p_UztboZERsxWZwJZEhJIr9rKuLWatIT-Fhuo0jwG_TkQAKuINx6fod-Fhg3KoOfdlUADdiBWNjHO3BHSvYkmwaAhQg-TNxyQLS8Kp_IoZ34fqpH_t8cxMpO0nERd1a9-Ssiyaw3_O2XEC5rauXnAPnPhcNlZx53EBxkA_jNQT08MtPY7FhTRE9nOooVyoWaYpHiJeTLge_zy8hSZl0_n_gMyuydwpq5Cow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/KA1wmvNlfa_OJaXMndHNtNSxnyspt1QLEJSP7mZlY6QI3Y0HPSDjNzBSO9LKCtRKjyyVjBGxUKyUqW0D032RtBR2JSBc7gZdQMkS6pG4mD7VgBNVZ7fqy__Aqyy_70x2J6jQVPZ1li6GGAC2001r48Q5WoFnFcZcOSU_9eYL1xCC62DAB4C9tcPfEfn1NkCBMxqOVL8Q01Lx_bQXtoC_sBrzULHNi1BjZgESgUBLV_2pw3tiCK8woIXA1eDtgPgKOvTkfX8fW19L1EibFRUozxaahptLl22TzHxoP80LhONvoEWvfXc8NkPZEcJNiQ_UUEzFbCszrjyprHGx2gUuVQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
تردد شبانۀ زائران از مرز شلمچه
عکس:
فرید حمودی
@Farsna</div>
<div class="tg-footer">👁️ 9.4K · <a href="https://t.me/farsna/453013" target="_blank">📅 22:23 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453012">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XlcjTJ5ipWbfyx7JIeebZok_IyGFOZG1zJhSDZcSiUq80Abfhuid8K_3fVukTpxPbZ2DM5f5w9_W1MQvfl4W96JasxfuwmCPOuccmDrG3oyN28_MaFsDETV-qoNYe7TWTpTWUI-dmcZpYAe0xPEWjIwour84N-VT4UmqI0B3AM0dPJ6QKnSM_Ktu7GbNTNovMZIA631I3kTxP6ac2hkPhdm0yiCJKdnfTbxTLobTFrN8oyOQrZkW-TrBoXis3qVVl1SMl4DuSoDpc6ikPpr2PviSAnAWtQtbTG6P9y-oe0n--lPJi4vOCsHYIZyZXq2_hDxuCwfZj3D6_sWwcbFt0A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
سخنگوی شهرداری تهران: طرح ترافیک برای موتورسیکلت‌ها در اولویت نیست
@Farsna</div>
<div class="tg-footer">👁️ 8.84K · <a href="https://t.me/farsna/453012" target="_blank">📅 22:20 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453011">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e84696860e.mp4?token=BancBPSyi4bokTwANAbZXaNC-N3zHrJtPe1QuxBGVGgrdFr2E0T5w3cx4UWzCz2pWUV3guf5MmzY4HdmTbUu-oI6XLpf0yk6U-vcEh1iWtSlkRQ9bx-scSdPUbKDcDClcN_V4k5TawZm1WQzCHmATw4c6HvCh_f2d8pUn8qeWqE04TNqinDKzogXyUZnHTy70pOuoaTaaYasbXl7omPmRJao5hhqdbXHUMG4IJlBKzESU_RXXKfZ5rOomBNVUPY33Yla3Sr8N-64wYkzQuQZxBjUnRy5-wFhflku0Hy6vFFsf-blaa2irnSEXEPFB3QbEkbspVtopCnyCZaLoWOAEA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e84696860e.mp4?token=BancBPSyi4bokTwANAbZXaNC-N3zHrJtPe1QuxBGVGgrdFr2E0T5w3cx4UWzCz2pWUV3guf5MmzY4HdmTbUu-oI6XLpf0yk6U-vcEh1iWtSlkRQ9bx-scSdPUbKDcDClcN_V4k5TawZm1WQzCHmATw4c6HvCh_f2d8pUn8qeWqE04TNqinDKzogXyUZnHTy70pOuoaTaaYasbXl7omPmRJao5hhqdbXHUMG4IJlBKzESU_RXXKfZ5rOomBNVUPY33Yla3Sr8N-64wYkzQuQZxBjUnRy5-wFhflku0Hy6vFFsf-blaa2irnSEXEPFB3QbEkbspVtopCnyCZaLoWOAEA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
بهادری جهرمی: همهٔ نهادهای حقوقی گارد جنگی بگیرند و برای آمریکا هزینه بسازند
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.62K · <a href="https://t.me/farsna/453011" target="_blank">📅 22:17 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453003">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UcliUg_wBmfqCfKgM9qjObJmp-XAj_KBDwbMdylh9KUzzP0HbNlY8rpLtLd75DXV5Vip4YUQfuf_aUVBfAwCjXeeP9RWNXeBZmZfFJ4cosRWW2NZBR3iHFidmDWz7xUToQHA1ucDSSs1wkdd_Wn4-GxTxO7pW0YWMHXjnmyHN8CKioqafTpcIQuOGrKpmMl9AOg46rE6k_SZUlOzdKeGYP9RNZlJRE8Q2g5jtF0SkXdLumYgqNLHjgo9CJ1ATK1fIkTJJRyhAH1QfuDzEqKESfb3SzIpmYkrHcZN82LKr63CK_WGUW9y85DMhjaNad2knfwG6ZPjb0FnZga6kKYJeg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ: توافق هسته‌ای با عربستان منوط به سازش با اسرائیل است
🔹
توافق هسته‌ای غیرنظامی که میان وزارت انرژی ایالات متحده و عربستان سعودی در دست تنظیم است (که به صراحت متضمن هیچ‌گونه غنی‌سازی مواد نخواهد بود) و تنها به مصارف غیرنظامی اختصاص دارد نظیر آنچه ایران،…</div>
<div class="tg-footer">👁️ 9.24K · <a href="https://t.me/farsna/453003" target="_blank">📅 22:12 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453001">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HOx2TlT7yrbfmpt3-4K0KTF-DlK8TW2MsEZJPABdHnNbnoXaO66pj0ywo9InojVTeSZleacucWT4rB9GWWadhyilrPTbsIX_EZaNgAn6UiBS7gbR_6m8qvcfzRlNBZ-lctJEmr4C_KfV7ZfysbO_hw4pUmqkPisF5w8LcVBN1fEo55fR4Q5nJuFb3wVWXjeDVSSHEp9FOpKOvUQO2KXVYLW2VXyPE3hmvKvwXf2ycg8Sc6EOmLb9HR8zwTPnQKQm_9uT8woNB-ZQFwPDvbRBTCnf2HP-G3iFCInEAL8yLw8onv3gsyz9Yz5FQDslwi1d8uzqq3Z_N56BsoUc8qhlsA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📷
یاد آقای شهید ایران در بین‌الحرمین
@Farsna</div>
<div class="tg-footer">👁️ 9.27K · <a href="https://t.me/farsna/453001" target="_blank">📅 22:03 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453000">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/99d381a99b.mp4?token=USNCS6dHXiH-qOui1twcQ0gG00qrEvB6oRrd0--uABZFDLxH5FoPAM6iWiQdEabTkiGuJ4cIQ9Ffj6Lh31FGkmkMcbGxZvJ-qpukeqnQbn5G9HCz83H1Ib5XPw2k3PL-cG7b6L8sbLj_jafomtxYPTPR5sB35VPrsPyfZRHDRnDLxHD_QwVT7MP0JHQc42oPhxnp_HEUu0LsYkmLwiUfI2ookDB84hd_xwyItq3gOmrCspSJO81hf0OG16RHSZzi8Z0vPoDXxwfPFPAUIn1XtckScLuP2yChBJR59lENk3PPOtWUbHNd_-TZwjQVOQf_v8GUHOeDwfwwTjwKG-08Lw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/99d381a99b.mp4?token=USNCS6dHXiH-qOui1twcQ0gG00qrEvB6oRrd0--uABZFDLxH5FoPAM6iWiQdEabTkiGuJ4cIQ9Ffj6Lh31FGkmkMcbGxZvJ-qpukeqnQbn5G9HCz83H1Ib5XPw2k3PL-cG7b6L8sbLj_jafomtxYPTPR5sB35VPrsPyfZRHDRnDLxHD_QwVT7MP0JHQc42oPhxnp_HEUu0LsYkmLwiUfI2ookDB84hd_xwyItq3gOmrCspSJO81hf0OG16RHSZzi8Z0vPoDXxwfPFPAUIn1XtckScLuP2yChBJR59lENk3PPOtWUbHNd_-TZwjQVOQf_v8GUHOeDwfwwTjwKG-08Lw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
اعتبار آمریکا مچاله شد
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/farsna/453000" target="_blank">📅 21:49 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452999">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2bc33c0f9d.mp4?token=tPwbMcHjzxcNY1qhv6fXx-u3XUNL1-6OcDUcV5D1PDER_DHMyFV1wkW7K-FQ6nZV92i2U88gLHLTQgy5wBCV-dWrbXxqhuaXOVP-Fz_X1ZPKxOt8Fy4-a_hZlBN5ixr-pD2ziEitB4V3QHKMsB6O3iXibFg0lweKYiisTu48JhhL27Xwe1lWUP1JuESq_BVgz-zbJyfRYgUl3kAx42VmlcZgzeG4XiQn1_wrbnVYtGGcenGLiIgpLryV8VqdZBmAcmWtFPoKq98HB7gAq5dLg-pzAcGWOFgZXpKk-0TutaGikdzsY1zTANxdlcVUCrmpE17YxeI9qLhstPDBeLMUSA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2bc33c0f9d.mp4?token=tPwbMcHjzxcNY1qhv6fXx-u3XUNL1-6OcDUcV5D1PDER_DHMyFV1wkW7K-FQ6nZV92i2U88gLHLTQgy5wBCV-dWrbXxqhuaXOVP-Fz_X1ZPKxOt8Fy4-a_hZlBN5ixr-pD2ziEitB4V3QHKMsB6O3iXibFg0lweKYiisTu48JhhL27Xwe1lWUP1JuESq_BVgz-zbJyfRYgUl3kAx42VmlcZgzeG4XiQn1_wrbnVYtGGcenGLiIgpLryV8VqdZBmAcmWtFPoKq98HB7gAq5dLg-pzAcGWOFgZXpKk-0TutaGikdzsY1zTANxdlcVUCrmpE17YxeI9qLhstPDBeLMUSA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
آیت‌الله جوادی آملی: رفیق ۷۰ ساله را از دست داده‌ام
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/farsna/452999" target="_blank">📅 21:41 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452998">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5343478190.mp4?token=gM9sCzWg6iuWhzeulYeHzMM0USZmIV7uhYTil31PQz7REfVVRr8sCKUJ31BQ40GSUZa9H9XFYILLyZoEDeOUoHPKw91POIG75aOZAa0p6Nk2MAKF-oEhs0pfjs7vA6opIa6lw7hJ8_7eBmPSj7TkS2qvJ56Yar0B4cc4npqE_SHbgRWxXblDs-uHrVB91ErOEAcNzjtMwQfS1I_qPOyJjzDUvs2wSTtliCl_pWI_yLYe68s9pfxnxRWB5E5yrxEA0zhdi9ylgAgTjb4CPYH-Niz48y5YF-PZZx_3zKbvFUmnAG-OhoOCNsKoBYvo6DIpinjP9FnfDQrJIl0TnlWhxg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5343478190.mp4?token=gM9sCzWg6iuWhzeulYeHzMM0USZmIV7uhYTil31PQz7REfVVRr8sCKUJ31BQ40GSUZa9H9XFYILLyZoEDeOUoHPKw91POIG75aOZAa0p6Nk2MAKF-oEhs0pfjs7vA6opIa6lw7hJ8_7eBmPSj7TkS2qvJ56Yar0B4cc4npqE_SHbgRWxXblDs-uHrVB91ErOEAcNzjtMwQfS1I_qPOyJjzDUvs2wSTtliCl_pWI_yLYe68s9pfxnxRWB5E5yrxEA0zhdi9ylgAgTjb4CPYH-Niz48y5YF-PZZx_3zKbvFUmnAG-OhoOCNsKoBYvo6DIpinjP9FnfDQrJIl0TnlWhxg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
غلبهٔ واژه‌های خارجی بر نوشت‌افزارهای ایرانی
@Farsna</div>
<div class="tg-footer">👁️ 9.95K · <a href="https://t.me/farsna/452998" target="_blank">📅 21:35 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452997">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/248e5e9775.mp4?token=p4ChuqD8IOKXHn_ySzNl4iWycq7zXjvPoq3ZNcoJnO-KCu-zZs9-OBBbh6Ma7WZ9nw2sqi2IKGAsgw1BcWGarWXPA6pRMcc44wwaunU3G59q60KGBNvqRPdPFChwsHZNsphfRxTd4w04mfxYR_pc897IlEYK4toPxnOZBCXdn-6Op8_AboEagYWafl529VNx34h3uOKbct6F-kfHcdCHUyMOkN9keyvfJk4hMeI3Suq10lTwk3mApmX9T6c58V-FJINMzqMU5wt_I2XaVmEWMYdPuNcr3O2P5j7V0iFBFc4l8vnvsSysiq-BSR-txg0-R2sXDKa96y2A-BeoPldprDzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/248e5e9775.mp4?token=p4ChuqD8IOKXHn_ySzNl4iWycq7zXjvPoq3ZNcoJnO-KCu-zZs9-OBBbh6Ma7WZ9nw2sqi2IKGAsgw1BcWGarWXPA6pRMcc44wwaunU3G59q60KGBNvqRPdPFChwsHZNsphfRxTd4w04mfxYR_pc897IlEYK4toPxnOZBCXdn-6Op8_AboEagYWafl529VNx34h3uOKbct6F-kfHcdCHUyMOkN9keyvfJk4hMeI3Suq10lTwk3mApmX9T6c58V-FJINMzqMU5wt_I2XaVmEWMYdPuNcr3O2P5j7V0iFBFc4l8vnvsSysiq-BSR-txg0-R2sXDKa96y2A-BeoPldprDzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
وضعیت عبور شبانه‌روزی زائران از مرز خسروی
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/farsna/452997" target="_blank">📅 21:31 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452995">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/52835c2e20.mp4?token=seVbSO-JKcx_MtRZozuK7MCNzgCtYosmX_MYf8mY-woyidEAZiCmActbbD-XtcAS-mC7OLVQ_Ci9Ojz-fFn9O4BiDi02vQ3qfvaMGrQe6mt9NMEyGFAGspXeqvhY5hLO2-w_V2Ihrn9UIRzJpPU0gBfhj2K59ZTpW7WqPlSAYTNa_VYiOqdr7dqd20By7cmom65Qg8awibP197CVKs4_6oSz5TvbV1Kl_l1lvGTVAMMUqQYrll9XOEnEnyVBRZm-eKQXmG7Hi91RXUvkyxzjWnbocmV37o1xhu4kKS7zoR2ohm64nj68X5C60-7EZdYYOGrRZPgWrRT4FXaMl5rgBIi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/52835c2e20.mp4?token=seVbSO-JKcx_MtRZozuK7MCNzgCtYosmX_MYf8mY-woyidEAZiCmActbbD-XtcAS-mC7OLVQ_Ci9Ojz-fFn9O4BiDi02vQ3qfvaMGrQe6mt9NMEyGFAGspXeqvhY5hLO2-w_V2Ihrn9UIRzJpPU0gBfhj2K59ZTpW7WqPlSAYTNa_VYiOqdr7dqd20By7cmom65Qg8awibP197CVKs4_6oSz5TvbV1Kl_l1lvGTVAMMUqQYrll9XOEnEnyVBRZm-eKQXmG7Hi91RXUvkyxzjWnbocmV37o1xhu4kKS7zoR2ohm64nj68X5C60-7EZdYYOGrRZPgWrRT4FXaMl5rgBIi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
منابع عربی از حملات پهپادی به مقر تروریست‌های تجزیه‌طلب در شمال اربیل خبر دادند.  @Farsna</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/farsna/452995" target="_blank">📅 21:16 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452994">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5e63bc2605.mp4?token=FSHoHAdDSLcTo3hi1NMJbS3qEUcVXJxJBaThO-Jp7pSkUuRpR97Iexj_qmdBWlQOusBLIlucnmUvAe8nSrE6rv20n3C8LLOtp9Uo6ywR7ycRQtOJbVPSov_2CflM36E3zmCwL1wWFHBH3KlUSUmA1GYn-jvwpQVScMOsf0pYNd6IHg6tqqGjih_PcyuG8jDKp35KxNo-faNsUNs2WnWTRyvEQBzzILuW6EkVfk6nCjSRSPDYzqUo7l6U-EmLfb6xChmhyMcPfghPsm5nGWgCPVx6flv2HinLzOl74hbRmIXp2200gtHz9mOOwuJrffLdbP_3V2hoaz_niJm2rRUn2G40zBqGeLpREmJWnDNV8puGlkqFdDTiD42nlJ6FnIU1afAc4c9_lbuhEBTlcEPyMPca7QRAucdUNYnV5EBXzMX_mWzf1A_zp7Do2taACGJE-AW9ecTaeHbKQO1ppPKzPH7jj1Tc_A38Rzqaz4dL4HxmAgBcfMnMHAGFfg9ehlDVK2h6CodpVlLQqJOhWl3TbUOPpyrO7MjsPR1EerwVp_afZtzozQwgVcdXbwp3WqNh_DPfEhwUGuF6R2vnMU-qZ2Mh5hJ0ndLrLpM0Qk2-1wg9TCboAEORaFdjP5prZ-AtiLUCajh6p-ZiuVdPrEPM16Bhrl6klvkaMzu7HjPkW1A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5e63bc2605.mp4?token=FSHoHAdDSLcTo3hi1NMJbS3qEUcVXJxJBaThO-Jp7pSkUuRpR97Iexj_qmdBWlQOusBLIlucnmUvAe8nSrE6rv20n3C8LLOtp9Uo6ywR7ycRQtOJbVPSov_2CflM36E3zmCwL1wWFHBH3KlUSUmA1GYn-jvwpQVScMOsf0pYNd6IHg6tqqGjih_PcyuG8jDKp35KxNo-faNsUNs2WnWTRyvEQBzzILuW6EkVfk6nCjSRSPDYzqUo7l6U-EmLfb6xChmhyMcPfghPsm5nGWgCPVx6flv2HinLzOl74hbRmIXp2200gtHz9mOOwuJrffLdbP_3V2hoaz_niJm2rRUn2G40zBqGeLpREmJWnDNV8puGlkqFdDTiD42nlJ6FnIU1afAc4c9_lbuhEBTlcEPyMPca7QRAucdUNYnV5EBXzMX_mWzf1A_zp7Do2taACGJE-AW9ecTaeHbKQO1ppPKzPH7jj1Tc_A38Rzqaz4dL4HxmAgBcfMnMHAGFfg9ehlDVK2h6CodpVlLQqJOhWl3TbUOPpyrO7MjsPR1EerwVp_afZtzozQwgVcdXbwp3WqNh_DPfEhwUGuF6R2vnMU-qZ2Mh5hJ0ndLrLpM0Qk2-1wg9TCboAEORaFdjP5prZ-AtiLUCajh6p-ZiuVdPrEPM16Bhrl6klvkaMzu7HjPkW1A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
روایتی از پاسخ رهبر معظم انقلاب به لبیک رزمندگان مقاومت در لبنان
@Farsna</div>
<div class="tg-footer">👁️ 9.58K · <a href="https://t.me/farsna/452994" target="_blank">📅 21:09 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452993">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1561c99235.mp4?token=B85k4KsYXBmobbAm8FmX_IBjm8AYs9w1Pvvza1cllsXSi548LAOvbPV5wffRl-cSSrkJO3zu8-UB-xTRbADWwkJo8wynI7McR78MobnT5QqnLMSILnyjhgww6EFVtARMiqCBRftxBkv7Av8o0dTfI7jhZs9UtaoaxSxJChP-FaBgNeB9rrfBREa7kUoR1ncLTPLibnWImmycfdXC7TRpvuXWYKyp36T8HxUDfQDbHpPDea0-WNDNpqrKoHqkyE6yO1MxgQxCGAQiaTIbMUs6qOlNFvJmYxgmxG4skwoYJRp5lYtnz0k7-Vot102N3-TAVfk6Ny8EzN3X00jL4eb98w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1561c99235.mp4?token=B85k4KsYXBmobbAm8FmX_IBjm8AYs9w1Pvvza1cllsXSi548LAOvbPV5wffRl-cSSrkJO3zu8-UB-xTRbADWwkJo8wynI7McR78MobnT5QqnLMSILnyjhgww6EFVtARMiqCBRftxBkv7Av8o0dTfI7jhZs9UtaoaxSxJChP-FaBgNeB9rrfBREa7kUoR1ncLTPLibnWImmycfdXC7TRpvuXWYKyp36T8HxUDfQDbHpPDea0-WNDNpqrKoHqkyE6yO1MxgQxCGAQiaTIbMUs6qOlNFvJmYxgmxG4skwoYJRp5lYtnz0k7-Vot102N3-TAVfk6Ny8EzN3X00jL4eb98w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
لامرد همچنان در میدان مقاومت، وفادار به فرمان رهبر
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.69K · <a href="https://t.me/farsna/452993" target="_blank">📅 21:03 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452992">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/43dd943d6b.mp4?token=MJIJy8hWPlbV0W3eLWkvurAF3Ep6cpu_WQKW56cleJhD47TDSnRshg7OiHF_v1_exMJVapfpGyjA_cG42YqOyz1HmKHU4L_aYRgFoL-PwhGu9BWR5soqPdFNq-rFCBBKT6UhRyip6epeehr9YWdb88iraQpT7FsK82Ur8GKu-VWkb97KznAFktUgRscK74kVbZcD_t1bkcH1zBwA6Y59Jde9aU2uI5ku5_4E89wfAY1SOEvX-WYE8iaYVFsyBhej7CjL6eJzuOi2OB1WqEr6rj7ikvTJ4GYA1WzSvKNaqBh5P_9cG-tqlOz1eaRxn2KdzdY1w_5OIZTe9vpBRXb8Aw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/43dd943d6b.mp4?token=MJIJy8hWPlbV0W3eLWkvurAF3Ep6cpu_WQKW56cleJhD47TDSnRshg7OiHF_v1_exMJVapfpGyjA_cG42YqOyz1HmKHU4L_aYRgFoL-PwhGu9BWR5soqPdFNq-rFCBBKT6UhRyip6epeehr9YWdb88iraQpT7FsK82Ur8GKu-VWkb97KznAFktUgRscK74kVbZcD_t1bkcH1zBwA6Y59Jde9aU2uI5ku5_4E89wfAY1SOEvX-WYE8iaYVFsyBhej7CjL6eJzuOi2OB1WqEr6rj7ikvTJ4GYA1WzSvKNaqBh5P_9cG-tqlOz1eaRxn2KdzdY1w_5OIZTe9vpBRXb8Aw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
رئیس قوه‌قضائیه: با کارگزاران متخلف بدون اغماض برخورد می‌شود
@Farsna</div>
<div class="tg-footer">👁️ 9.87K · <a href="https://t.me/farsna/452992" target="_blank">📅 20:59 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452991">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/30d5f50cce.mp4?token=OMYr2j0-SaJTyfL2CU4LuahPfHHh1zRH48NEhG3NTYbQQX8yhBU33oYX0R9MgH2IbMvr7b0P_ZXIksxODX6SxSuueyeao5DcLgn_DNs_TdoalhJTdBh69qrwQJ04CR1_h-WZt-5KUudBfqJKDangxWFsv52gMx_zjFJW6w4y3SC1YqX1MXFXR5o1Bh1seMySoT5tq0nGsxjYfVajjpxa6vc4ZJQGb4uF0bIwm8sVry0X_osWdUxm4tr6HVUqHmsVU35X2mCMYgR096j91tXOAedEjupKV7Qh4mRGQ5eFXr0MogbqMHDkRzAgK5tDx3pJl6Eu8Xr12tTHFmh_J5DdOg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/30d5f50cce.mp4?token=OMYr2j0-SaJTyfL2CU4LuahPfHHh1zRH48NEhG3NTYbQQX8yhBU33oYX0R9MgH2IbMvr7b0P_ZXIksxODX6SxSuueyeao5DcLgn_DNs_TdoalhJTdBh69qrwQJ04CR1_h-WZt-5KUudBfqJKDangxWFsv52gMx_zjFJW6w4y3SC1YqX1MXFXR5o1Bh1seMySoT5tq0nGsxjYfVajjpxa6vc4ZJQGb4uF0bIwm8sVry0X_osWdUxm4tr6HVUqHmsVU35X2mCMYgR096j91tXOAedEjupKV7Qh4mRGQ5eFXr0MogbqMHDkRzAgK5tDx3pJl6Eu8Xr12tTHFmh_J5DdOg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
از آتش‌سوزی هتل استقلال تا ضرب‌وشتم خبرنگار صداوسیما
@Farsna</div>
<div class="tg-footer">👁️ 9.51K · <a href="https://t.me/farsna/452991" target="_blank">📅 20:58 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452990">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bdda014de4.mp4?token=VAaAFKeGbSLEMbgQrRQZc9Mk9D9gpIy-uO1UEObbpnMrk8XuP7v-MJJs1hqggprxYtCG1SlEWa61pIj7Bq-XENlyc0GWA3BdfSY3vYbXvVUSkzA0Nf3HFDr0yk5gi3-hB99Z8LVsPZsQbbuxx_vexWqDjGAUYeniGnXmas8Mw3ybH8HlaFTnUxj-Jxt1jp-jttUss5-deapWGFj478v-bjXrntKmYfXaxveTsNsRewZXoiRjsyJRFFHu8rH-9zT4YOZ_sTBlZdpQlM-c0VYwnU42B2iGGzAE6DomtPIS4XO4qBQblW3SISUSVp8_LDhVY-FnfT9D8yqeaY4DbaeJXUtrYzaKgMfKOk0ugPRnfhymJTVpsWRtiD5GFqJxbuAk_W2SsAepWlODSBp6HabmygJqqmHb5i4R84ixqjs1FGYpWXYZZ93-YnqgIiJ-0G8Z9HD0zexyyTAqLQkTeHbXEzgBArrscZlNQejZSGswS9056RuxIEVqds16X6X_H-qY8u-Ntfn7dxm4_UXS0fw7pdesbGbjwYSkR7X3NzDaYdHwTpUysDmY9vAzYl_hh5o_Kut0ztZpS4_Wali4n6nSlzfmyHElVa-Zeduh3U4p9pIWke67Nnedek6Opn29ROr6Qc_FLx4K_84zqeedlamdDX0CNiNfK9sL0zsF-CJZRxs" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bdda014de4.mp4?token=VAaAFKeGbSLEMbgQrRQZc9Mk9D9gpIy-uO1UEObbpnMrk8XuP7v-MJJs1hqggprxYtCG1SlEWa61pIj7Bq-XENlyc0GWA3BdfSY3vYbXvVUSkzA0Nf3HFDr0yk5gi3-hB99Z8LVsPZsQbbuxx_vexWqDjGAUYeniGnXmas8Mw3ybH8HlaFTnUxj-Jxt1jp-jttUss5-deapWGFj478v-bjXrntKmYfXaxveTsNsRewZXoiRjsyJRFFHu8rH-9zT4YOZ_sTBlZdpQlM-c0VYwnU42B2iGGzAE6DomtPIS4XO4qBQblW3SISUSVp8_LDhVY-FnfT9D8yqeaY4DbaeJXUtrYzaKgMfKOk0ugPRnfhymJTVpsWRtiD5GFqJxbuAk_W2SsAepWlODSBp6HabmygJqqmHb5i4R84ixqjs1FGYpWXYZZ93-YnqgIiJ-0G8Z9HD0zexyyTAqLQkTeHbXEzgBArrscZlNQejZSGswS9056RuxIEVqds16X6X_H-qY8u-Ntfn7dxm4_UXS0fw7pdesbGbjwYSkR7X3NzDaYdHwTpUysDmY9vAzYl_hh5o_Kut0ztZpS4_Wali4n6nSlzfmyHElVa-Zeduh3U4p9pIWke67Nnedek6Opn29ROr6Qc_FLx4K_84zqeedlamdDX0CNiNfK9sL0zsF-CJZRxs" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
روستایی که نانش را نذر زائران کرد
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.37K · <a href="https://t.me/farsna/452990" target="_blank">📅 20:55 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452989">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/221125e133.mp4?token=LK99ctzy-Hf-l7_oCTdI6tuaf4W2wKc1r3jve82WbvjUa1GnW65b126IrdKZQbvyF2stViyqb-ttGXmMRzeVzKuKV4CEGbAm7HtOQZ9OvQl14XQEtG0PGqksErHB7dQfalwfBKesGZT2u4qyueQXrqFaULcdLxpVtYHkTkRaElOh1BkGmc-BMeilBdhamQ12C_iYWY4ubTsxnBq_DXjcdU1zhDAmEx9JInWincI2C99qzgpaMihyFYZFWLWXUn-K2GkdebiVeLY9YGpYEVF3JLt-jyM0bHSdVHReVed0nppniCP2Prk-NxG-nzEkDkcxewfTh8HIeZAJByfN98k5BQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/221125e133.mp4?token=LK99ctzy-Hf-l7_oCTdI6tuaf4W2wKc1r3jve82WbvjUa1GnW65b126IrdKZQbvyF2stViyqb-ttGXmMRzeVzKuKV4CEGbAm7HtOQZ9OvQl14XQEtG0PGqksErHB7dQfalwfBKesGZT2u4qyueQXrqFaULcdLxpVtYHkTkRaElOh1BkGmc-BMeilBdhamQ12C_iYWY4ubTsxnBq_DXjcdU1zhDAmEx9JInWincI2C99qzgpaMihyFYZFWLWXUn-K2GkdebiVeLY9YGpYEVF3JLt-jyM0bHSdVHReVed0nppniCP2Prk-NxG-nzEkDkcxewfTh8HIeZAJByfN98k5BQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
آتش پاسخ یمن به تجاوز جدید عربستان
@Farsna</div>
<div class="tg-footer">👁️ 9.14K · <a href="https://t.me/farsna/452989" target="_blank">📅 20:54 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452988">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/774ce2727b.mp4?token=tbwWapLaKy8VBT_ikpgHxh3GafCyRQOwoT1mraXd1mjX5gQJd9ur2DW3aF-QabHIY_fi4_o0Xc4ycX78zFre9I6ebPOM8xjSbtlqKzWSWMTB5vbxbgGpJmnHBPLpBTdrZZBT7-3-ROQw_0yw44nZTHbP37kRJvQixfNGz2JqR1YH9tK8-L42ou9AXdX9XK7OoKC0qEG3SnnI-bm4Ex9Yd6P52JmNwU3dg-ncxSmzlyrlhelzraUhy6hJyqBfNElPFB2tvnc11CAbSLMms2AKjroyFwcqhhOE8Vl6LOv3TKp2HhNMo8EgkCgkXiN5dj2tN_V53r9-Q1Kzj62kmvXo9pG8vxtjBbedwTqJqcyZhEukYFTJ_-sdpoK3ZtdYRUI8AYZRjxWC8YE22jFMeetD_umE29viEZOhJn4r33JzddEvH5QdKl-EYzuL2BpkP_N9EKovpZ5IrJ7Jsmzv_A-c9-TxO5-YFHIlruS5kAbw6v_fm5GCoIMEYptxUahHVvzesyPGGKO27ZeEqZ2XKokDZsEwFC7y88OcLWB4kRwtSG-Wm7yTTNJR84ptaoKxuFJtLpi-3lfuqJLovNRvShXIEjLbvdxPHKRmqvW5y6S0qwFWzpdIfC4-p218n5o3of0JCwBMhp34j8WmHtOuKU6Oz7BFpraRAbdIjgnC6k1gNIY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/774ce2727b.mp4?token=tbwWapLaKy8VBT_ikpgHxh3GafCyRQOwoT1mraXd1mjX5gQJd9ur2DW3aF-QabHIY_fi4_o0Xc4ycX78zFre9I6ebPOM8xjSbtlqKzWSWMTB5vbxbgGpJmnHBPLpBTdrZZBT7-3-ROQw_0yw44nZTHbP37kRJvQixfNGz2JqR1YH9tK8-L42ou9AXdX9XK7OoKC0qEG3SnnI-bm4Ex9Yd6P52JmNwU3dg-ncxSmzlyrlhelzraUhy6hJyqBfNElPFB2tvnc11CAbSLMms2AKjroyFwcqhhOE8Vl6LOv3TKp2HhNMo8EgkCgkXiN5dj2tN_V53r9-Q1Kzj62kmvXo9pG8vxtjBbedwTqJqcyZhEukYFTJ_-sdpoK3ZtdYRUI8AYZRjxWC8YE22jFMeetD_umE29viEZOhJn4r33JzddEvH5QdKl-EYzuL2BpkP_N9EKovpZ5IrJ7Jsmzv_A-c9-TxO5-YFHIlruS5kAbw6v_fm5GCoIMEYptxUahHVvzesyPGGKO27ZeEqZ2XKokDZsEwFC7y88OcLWB4kRwtSG-Wm7yTTNJR84ptaoKxuFJtLpi-3lfuqJLovNRvShXIEjLbvdxPHKRmqvW5y6S0qwFWzpdIfC4-p218n5o3of0JCwBMhp34j8WmHtOuKU6Oz7BFpraRAbdIjgnC6k1gNIY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
مردم در دفاع از ایران، در همهٔ کمین‌گاه‌ها محکم ایستادند
@Farsna</div>
<div class="tg-footer">👁️ 8.93K · <a href="https://t.me/farsna/452988" target="_blank">📅 20:52 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452987">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fa9vn52DwtMtHK1j8VQOhkRNOHt36ik5RfVRUYINUdMXvIr76_zPKdkzWs35bfuzgsGbXtQUtAnzKSQZMAZgdPcj8hLramwvjzak0KMCJBErkh_UY65EFbD7Boyu4Hb4EFfVDuj6jnxRSSCdLIfjS6BiEPyy2jWn3jKYXFcHIxKjSDNGt3k8FsNKjC68IMMUGyW6dMkzLeDXlF5KQzj4p5_RgqgIVWOjlXYe3M2heZR-ODq_qV0NF3qrfB4Kif5x-ZzhcC351Pe7Cog_eu3Ote3CnksSZLHzjZuea2XwSu9cyRcPwnRY8dXCqQuuxqZ0vhLckbzIypR1rLaxGp-xBw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">غریب‌آبادی: جنایت‌های جنگ علیه ایران را تا آخر پیگیری می‌کنیم
🔹
معاون حقوقی وزارت خارجه: طبق تاکید رهبر انقلاب حتی اگر پیگیری یک پروندۀ مرتبط با جنایات آمریکا ۱۰ تا ۱۵ سال زمان ببرد، نباید روند رسیدگی متوقف شود.
🔹
تاکنون صدها سند از جنایت‌های جنگی تهیه و بیش از ۱۴۰۰ صفحه گزارش و مستند حقوقی برای ثبت در مجامع بین‌المللی آماده شده است.
🔹
بیش از ۱۲۰ سند دربارۀ نقش برخی کشورهای حوزۀ خلیج فارس در تجاوز اخیر تهیه و در شورای امنیت ثبت شده و در این اسناد، زمان، محل و مبدأ حملات به‌طور دقیق مستند شده است.
🔹
پیشنهاد کردیم برای رسیدگی به پرونده‌های جنایت‌های جنگی آمریکا دادگاه ویژه تشکیل شود. رسیدگی به ده‌ها هزار پرونده نیازمند سازوکار ویژۀ قضایی است.
🔹
ایران پیگیری حقوقی جنایات آمریکا را در سه مسیر دنبال می‌کند: محاکم داخلی، محاکم خارجی بر پایۀ اصل صلاحیت جهانی و طرح دعوا در مراجع بین‌المللی.
🔹
با استناد به کنوانسیون شیکاگو، روند حقوقی لازم برای استفاده از ظرفیت دیوان بین‌المللی دادگستری علیه آمریکا را آغاز کرده‌ایم.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.27K · <a href="https://t.me/farsna/452987" target="_blank">📅 20:48 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452986">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">🔴
منابع لبنانی: رژیم صهیونیستی ارتفاعات علی الطاهر در جنوب لبنان را هدف حملۀ توپخانه‌ای قرار داده است.
@Farsna</div>
<div class="tg-footer">👁️ 8.71K · <a href="https://t.me/farsna/452986" target="_blank">📅 20:37 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452985">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vQhDtmidu5xQGILeqkmzKGSiDPChbn-GeD6MSaJRGmHY6H9DEFhBaO-JbEqWTpliBeEierQuHmOnPQSjjlYQcHpwQvpp-NNdmvyLLk4HzSWGg6vY-Q5VEv5ZOKeq-Fh8Qnm2mjHLymrrtGEHWr-Qax2oH1I1i_IvDxdD2FK8hU0V3TLPc-UdGBzUiAD4Zfk2_9zOAFquIJZ5qEXioaDyUTHVF2ZN79P19iJ9CO-iPk8getEZEwPu3HfeE27DV2eMMj671axEYcSeEmMRD5uwIS9v2wmVBtKj9W5B7BEQeIM3bvR6nPl_1Lu89cmj350nBwm5NZSonT_hLv2rh2TOzg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ: ما چندین میلیارد دلار از ونزوئلا درآمد به‌دست می‌آوریم؛ این اتفاق دربارۀ ایران هم خواهد افتاد  @Farsna</div>
<div class="tg-footer">👁️ 9.32K · <a href="https://t.me/farsna/452985" target="_blank">📅 20:36 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452984">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">چرا بخشی از سخنان رئیس‌جمهور و رئیس مجلس در صداوسیما حذف شد؟
🔹
اسفندیاری، رئیس دانشگاه صداوسیما: مطلب مطرح‌شده در سخنرانی رئیس‌جمهور چندی پیش در دیدار با مدیران صداوسیما نیز مطرح شده بود. فیلم آن جلسه را دفتر ریاست‌جمهوری تدوین و برای پخش به صداوسیما ارسال کرده بود.
🔹
جالب این‌که در آن فیلم، دقیقاً همین بخش مورد اشاره حذف شده بود! یعنی این هجمهٔ سنگین علیه صداوسیما به بهانهٔ حذف جمله‌ای برپا شده است که پیش‌تر خودِ دفتر ریاست‌جمهوری هم به‌درستی آن جمله را از سخنرانی ایشان حذف کرده بود.
🔹
جملهٔ مورد اشاره در این سخنرانی، نقل‌قولی از جلسه‌ای خصوصی میان رهبر شهید انقلاب و رئیس‌جمهور بوده است. طبق قواعد و ضوابط حرفه‌ای و پروتکل‌های رایج در تنظیم و انتشار اخبار مربوط به رهبر معظم انقلاب، هرگونه نقل‌قول از جلسات خصوصی و محرمانهٔ ایشان ممنوع است و انتشار چنین مطالبی صرفاً منوط به تأیید دفتر مقام معظم رهبری است.
🔹
این رویه که در زمان حیات رهبر شهید رایج بود، طبعاً در شرایط فعلی و پس از شهادت ایشان باید با حساسیت بیشتری رعایت شود. اگر بنا شود هرکسی برای توجیه اقدامات فعلی خود، نقل‌قولی از جلسات خصوصی با رهبر شهید انقلاب مطرح کند، با هرج‌ومرج و آشفتگی روایت‌ها مواجه خواهیم شد.
🔹
متأسفانه همین نقل‌قول اخیر رئیس‌جمهور محترم نیز دستمایهٔ سوءاستفادهٔ برخی عناصر ضدانقلاب و منافقین خارج از کشور قرار گرفت و زمینه‌ساز اهانت و توهین به رهبر شهید انقلاب شد.
🔹
همهٔ ما بند آخر وصیت‌نامهٔ امام خمینی (ره) را به‌خاطر داریم که ایشان تصریح می‌کنند: «آنچه به من نسبت داده شده یا می‌شود، مورد تصدیق نیست؛ مگر آن‌که صدای من یا خط و امضای من باشد، با تصدیق کارشناسان؛ یا در سیمای جمهوری اسلامی چیزی گفته باشم.» براساس این حکم امام خمینی(ره)، هرگونه انتساب نقل‌قول به رهبری شهید انقلاب که خارج از اسناد و مدارک موجود باشد، باطل و غیرمعتبر است.
🔹
این امر دربارهٔ رهبر شهید نیز طبعاً صادق است و آقای رئیس‌جمهور که خود از پیروان «خط امام» هستند، قطعاً بیش از همه باید به رعایت این اصول و ضوابط در نقل‌قول از رهبر انقلاب پایبند باشند.
🔹
در مورد عدم پخش بخشی از مصاحبهٔ رئیس مجلس نیز سازمان صداوسیما بر اساس برخی سیاست‌های ابلاغی، پیشنهاد حذف ۲ دقیقه از مصاحبهٔ ایشان را مطرح کرده بود که پس از بررسی موضوع در جلسه‌ای با حضور نمایندگان نهادهای مختلف و مراجع ذی‌صلاح، نه‌تنها نظر سازمان صداوسیما صحیح تشخیص داده شد و مورد تأیید قرار گرفت، بلکه مقرر شد ۱۸ دقیقه از آن مصاحبه حذف شود.
🔹
این موضوع همان زمان به اطلاع تیم رسانه‌ای رئیس مجلس نیز رسید؛ لذا در پخش دوم، با وجود انجام این اصلاح، هیچ‌گونه اعتراضی مطرح نشد.
🔹
در مورد پخش مصاحبه‌های وزیر محترم امور خارجه با خبرنگاران خارجی نیز معمولاً با توجه به برخی اظهارنظرهای خلاف واقع، ضد منافع ملی و اظهارات سوگیرانهٔ خبرنگاران خارجی علیه ایران، پخش کامل این مصاحبه‌ها در دستور کار رسانهٔ ملی نبوده است.
🔹
هیچ درخواستی نیز از سوی وزارت خارجه برای پخش کامل این مصاحبه‌ها مطرح نشده است. ضمن این‌که اصولاً پخش کامل مصاحبه‌ای که توسط رسانه‌ای دیگر انجام شده، جز در موارد استثنا، خلاف اصول حرفه‌ای رسانه است. معمولاً رسانه‌ها به پخش بخش‌هایی از مصاحبه‌هایی که توسط دیگران انجام شده، اکتفا می‌کنند.
🔹
اگر از نظر وزیر خارجه، یک مصاحبهٔ خارجی ایشان ارزش پخش کامل در فضای داخلی را داشته، طبعاً می‌توانستند از مرکز رسانه‌ای خود درخواست کنند که آن را طبق نظر خودشان ترجمه کرده و در اختیار رسانه‌های داخلی قرار دهد.
@Farsna</div>
<div class="tg-footer">👁️ 9.61K · <a href="https://t.me/farsna/452984" target="_blank">📅 20:28 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452983">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/k5TMuZDtxuYSXgeqlY7hmNTfchLFZPWANB97f-4sbrjGl11Md-8wEPGx9Cy_m33ggCZmNE6GJLDSc958roo4XQiaWWwuuMxOgBQbcPmebcqXBAhoMbX1n1VMVvkClgCNnlGI_lVA3ZmJcsbKx6NwkR_Z0hqAbgVJlsGQZJXKiaqJxwTBOwgBX5JWhZCQJfdQacnsDNr-EUv9IFFa4ZidWOdeGYcL6JgUVDD9hL7XDXASzZdTeeTCH2-dUhG6WTeu_tMX9e3WPqKGIWkNbCn4mDAksmqXscqNcHQMFyqYo0P4VBsScD4AodFDinvuwaXfDbjgmQ_o25TvhhRH3xrENQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این لوازم الکترونیکی را به اربعین نبرید
🔹
قاعده کاربردی بستن کوله‌پشتی اربعین، سبکی و حذف بار اضافه است. در این مسیر طولانی، گوشی هوشمند و یک پاوربانک استاندارد تنها ابزارهای الکترونیکی ضروری شما هستند.
🔹
دوربین عکاسی و لپ‌تاپ را فراموش کنید. وزن زیاد، آسیب‌پذیری در برابر گرما و ضربه، و نبود فضای شارژ، آن‌ها را به باری اضافه تبدیل می‌کند. دوربین موبایل برای عکاسی زائران عادی کاملاً کافی است. همچنین به جای مونوپادهای سنگین و دست‌وپاگیر، در صورت نیاز از پایه‌های کوچک جیبی استفاده کنید.
🔹
برای حفظ آرامش و خلوت معنوی مسیر، همراه داشتن اسپیکر بلوتوثی اصلاً توصیه نمی‌شود؛ هندزفری شخصی بهترین جایگزین است. همچنین از آوردن سشوار که صرفاً فضای کوله را اشغال می‌کند خودداری کنید.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.98K · <a href="https://t.me/farsna/452983" target="_blank">📅 20:23 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452982">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lVO4m5Pr1_Kb4gHEfmjgQ9nCs1dLJoziD0RD2LC1Vnz5szCEuzpodTJ_cSXQT7AL1-crZBRlnCaQdZtsvAwGN62Pl5H4mKqp64-wg-sKtvlG589p0STREyZBoDF2cqLpeColSjhGSA_2q5ZjMLq1bXLkud7KuQizM6hH8HE-PZbHSFqOqrsT-X5vHnv8RvYXMjymauRkdnyaNX15KvjxEJ0feBP6RlX6t9Ter6_xGxQlRCadTSXRFl4gik_ecZlaSjmgxhQmMGstk50JqPepnU6cvBXvabBZCKOf8j-Dt-p4565AIZRuyrRFFoxV3v4eO1Nk_g7gfqCinMFqnU69Yg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ: ما چندین میلیارد دلار از ونزوئلا درآمد به‌دست می‌آوریم؛ این اتفاق دربارۀ ایران هم خواهد افتاد
@Farsna</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/farsna/452982" target="_blank">📅 20:18 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452981">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4511afd4f2.mp4?token=YVuzrgBT8aHkpKVotdHWtzTsu7oMwd1jmPrNAJNSDOg_97XPQSWGN0bSKo6eM1dIvHL36tWgI8wcKe8hqhmlU4tUVyUFOv_T1FLqQWbAzuD_3hm3ctOARHwpKK0XBLKrG64ys8qrcIk2E760feUnrPN5-vhv49sLlymQz6JZ-NCawI77S-3uuZvYZlycXsFKvRjpc_KAqlkhWbqh-CmqveRizxjt2uhA7d_qDMdTcAFk5Hf_40aLRkl2D6w-KOHtRvA3Z2y6QWUAZOJD__1ei2JE8mDHRAQMB56Zc9OfO6A-zqk1VVMgx3nWxThNZZs3OkZrV4avowrtXs-6X2P4KA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4511afd4f2.mp4?token=YVuzrgBT8aHkpKVotdHWtzTsu7oMwd1jmPrNAJNSDOg_97XPQSWGN0bSKo6eM1dIvHL36tWgI8wcKe8hqhmlU4tUVyUFOv_T1FLqQWbAzuD_3hm3ctOARHwpKK0XBLKrG64ys8qrcIk2E760feUnrPN5-vhv49sLlymQz6JZ-NCawI77S-3uuZvYZlycXsFKvRjpc_KAqlkhWbqh-CmqveRizxjt2uhA7d_qDMdTcAFk5Hf_40aLRkl2D6w-KOHtRvA3Z2y6QWUAZOJD__1ei2JE8mDHRAQMB56Zc9OfO6A-zqk1VVMgx3nWxThNZZs3OkZrV4avowrtXs-6X2P4KA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
«عمو لیندسی» که امروز مُرد که بود؟  @Farsna - Link</div>
<div class="tg-footer">👁️ 8.81K · <a href="https://t.me/farsna/452981" target="_blank">📅 20:15 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452980">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dGvDAKeVGsuko7r0sVR5iHi32sKSYRJXyrAC2cEb8aex6Y60Mn7iikbc7UFODACq5Lcgf0Fwc7KCARaMcFZUePqSOtdM5IxxjUw90763oIcxHQKXcTHyT3TwDypyK72YHkLkCPDqYm7LWP4Dcjzk41UjsPJ3-wAevLq5ZwyofUynTEyhOi6euTRF6riw1VoJP9QNVbQi0YXPhweiSEn2c9fK_kSIXlXwCRniLHHjAP8HwwKY4mbnAXlbKR5_4e8X3La-473OCEl2TPcPC0ihtjwq4cwxMXZyJO6jQvApAfpPemOrCSiC-ToFPwIiwWlW99ycDZLL7BkcF0T-0IPIQQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">۹۰ درصد درآمد نفتی عربستان دود شد
🔹
شرکت اطلاعات دریایی «وایندوارد» اعلام کرده که بارگیری نفت در بندر ینبع عربستان از ۲۹ تیرماه به بعد حدود ۴۰ درصد کاهش یافته.
🔹
بندر ینبع در غرب عربستان یکی از مهم‌ترین پایانه‌های صادرات نفت این کشور در سایه انسداد تنگه هرمز به شمار می‌رود
🔹
در مجموع صادرات نفت عربستان با بسته‌شدن ۲ آبراه استراتژیک هرمز و باب‌المندب به روی کشتی‌های سعودی از ۸ میلیون بشکه به ۲.۴ میلیون در روز سقوط کرده.
🔹
این یعنی روزانه ۵۰۴ میلیون دلار ضرر که ۹۰ درصد کل درآمد نفتی عربستان را شامل می‌شود.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.96K · <a href="https://t.me/farsna/452980" target="_blank">📅 20:11 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452979">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0c8ce517b4.mp4?token=CSNDW86uwaz0uuMEhMFRuHeuRRkOawmPBEY4dFSW7z8L0OuHshtilHu3GEdvRUm7Ck53NqMj1wEgr6xGAepz-HXzBLQh_wJUwtpK9rVsQMCUNz5UoIiHpzqShdOwn64QRoZ3KlSpa_QQoEkeqgjCFNIB7DHle5WZ1DKGXioaS7W4fhYZzMnVbSg12pNb1YSjoh7fUZ9eFWF7XzaAxe266BXEU1Cyus6pfoH4SamUTkb8Z2_UmLS8Z7t8lyuy9zb8LloyJgcWcvFc0BrT1x3KUOUFuglbctoJ9FFXt6bNb7mrjPEkWnX94urz6Fn48C3hV8tAKtoEGwrbaDyyyOHwNQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0c8ce517b4.mp4?token=CSNDW86uwaz0uuMEhMFRuHeuRRkOawmPBEY4dFSW7z8L0OuHshtilHu3GEdvRUm7Ck53NqMj1wEgr6xGAepz-HXzBLQh_wJUwtpK9rVsQMCUNz5UoIiHpzqShdOwn64QRoZ3KlSpa_QQoEkeqgjCFNIB7DHle5WZ1DKGXioaS7W4fhYZzMnVbSg12pNb1YSjoh7fUZ9eFWF7XzaAxe266BXEU1Cyus6pfoH4SamUTkb8Z2_UmLS8Z7t8lyuy9zb8LloyJgcWcvFc0BrT1x3KUOUFuglbctoJ9FFXt6bNb7mrjPEkWnX94urz6Fn48C3hV8tAKtoEGwrbaDyyyOHwNQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
نامی که علیه اشغالگری جنگید، اما بر پایگاه اشغالگران نشست
@Farsna</div>
<div class="tg-footer">👁️ 8.74K · <a href="https://t.me/farsna/452979" target="_blank">📅 20:05 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452978">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c068750ffd.mp4?token=diiwGC4_MHn2sXphdJQ_n7bugkfRJJxkYl__O3fivEs2bcQPuMDAZ1j9oRKTIjXpVZLy6pBCdmaaA_EjeX_lc7s5yuR3iOlEQMubBYMA_ZIqcBgpPgK9CV1fCtkNM7_c5m8IPfpUGL6LbjWjJabUWUuMRWmpkE0LUb93tKo9y99uivvAoG4Q62b_GqI6MnTa7HdgJeOhuitvapo9bE639xoo-FVe8uHPzW7LWSGK5nNt_XhBoanG0fyF_aLH6dGSdE4-frX2G4ecGRFbJHcJW-g70msL-D37Bp0zEbPC23BgdhwPkrQyPQxrdmMX-LTrG2zKxcuDQrfiwzPEWceBaA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c068750ffd.mp4?token=diiwGC4_MHn2sXphdJQ_n7bugkfRJJxkYl__O3fivEs2bcQPuMDAZ1j9oRKTIjXpVZLy6pBCdmaaA_EjeX_lc7s5yuR3iOlEQMubBYMA_ZIqcBgpPgK9CV1fCtkNM7_c5m8IPfpUGL6LbjWjJabUWUuMRWmpkE0LUb93tKo9y99uivvAoG4Q62b_GqI6MnTa7HdgJeOhuitvapo9bE639xoo-FVe8uHPzW7LWSGK5nNt_XhBoanG0fyF_aLH6dGSdE4-frX2G4ecGRFbJHcJW-g70msL-D37Bp0zEbPC23BgdhwPkrQyPQxrdmMX-LTrG2zKxcuDQrfiwzPEWceBaA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
آمریکایی‌‌ها از اسرائیل خسته شده‌اند
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.5K · <a href="https://t.me/farsna/452978" target="_blank">📅 19:46 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452977">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">🔴
منابع سوری: ارتش رژیم صهیونیستی درحال پیشروی به خاک سوریه از سمت حومۀ غربی درعا است.
@Farsna</div>
<div class="tg-footer">👁️ 9.23K · <a href="https://t.me/farsna/452977" target="_blank">📅 19:38 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452976">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/167fec05e0.mp4?token=IXv5JDayXuihtbls3t3RhDWd586Xcqn2iv6M9GAIhFXSPHn5DF2TL5eHasfWsvp51bBVt4p24towOGZpyCN5RnKl8ne1QwE5ssKJ-UpaCEwaZvfYW88QXHzhfhoOHDzCVVDAc8NXNOyPxhvLhn8grEP4sCeV3YO0GP4H_dewbxmwyAICBro-TRSE-LNwbzC3y-riJayTMBJ1UuNIjb8lxUDA9JCanqMiMhaiozhsHVq6ewWDgdWWPiYk32F3Bj_Ln3cHTjFgby8rqch6Aes5DbBmt90LaZqA8zhBcbmBe0qv8zVI8-LkG8NLi9X42jSx96ml276ag2bu9ZlYk4qFbBtcGBPZuOwFLikQgtV5KQZUtJQkb0wpNcMnDJu_0n9BvfqC1EK-dk_nzYgCtNzwaqOFEZduUMvU4XU9TBmHK6N7ul_ewl1zxGZArQLJecl8THu0UYEjsr3XxpwAEhSRavBf8hxuj557zBtefHnSC3Yuy3vHGMKROYmyiSpF-vn8q1n8vv7ZKQj4tV4BZplDfvof5e6yyw038_drZ06qS0ftInC7tyutfTnWqfWLVBXf5DnNrn7z_qdgDltMQO2_FOE-NdR04kzQxJazWOHlldNMxjHdJaraAGJq6DxZWKBiItUMuR1Pr0URwJS7gSsKdgcQkumiflcDHkDTqdkbVWI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/167fec05e0.mp4?token=IXv5JDayXuihtbls3t3RhDWd586Xcqn2iv6M9GAIhFXSPHn5DF2TL5eHasfWsvp51bBVt4p24towOGZpyCN5RnKl8ne1QwE5ssKJ-UpaCEwaZvfYW88QXHzhfhoOHDzCVVDAc8NXNOyPxhvLhn8grEP4sCeV3YO0GP4H_dewbxmwyAICBro-TRSE-LNwbzC3y-riJayTMBJ1UuNIjb8lxUDA9JCanqMiMhaiozhsHVq6ewWDgdWWPiYk32F3Bj_Ln3cHTjFgby8rqch6Aes5DbBmt90LaZqA8zhBcbmBe0qv8zVI8-LkG8NLi9X42jSx96ml276ag2bu9ZlYk4qFbBtcGBPZuOwFLikQgtV5KQZUtJQkb0wpNcMnDJu_0n9BvfqC1EK-dk_nzYgCtNzwaqOFEZduUMvU4XU9TBmHK6N7ul_ewl1zxGZArQLJecl8THu0UYEjsr3XxpwAEhSRavBf8hxuj557zBtefHnSC3Yuy3vHGMKROYmyiSpF-vn8q1n8vv7ZKQj4tV4BZplDfvof5e6yyw038_drZ06qS0ftInC7tyutfTnWqfWLVBXf5DnNrn7z_qdgDltMQO2_FOE-NdR04kzQxJazWOHlldNMxjHdJaraAGJq6DxZWKBiItUMuR1Pr0URwJS7gSsKdgcQkumiflcDHkDTqdkbVWI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
بررسی تصاویری که ابعاد واقعی انهدام پایگاه های آمریکا را فاش می‌کند
🔹
کارشناس کانادایی: انهدام رادارهای راهبردی و دوربرد توسط ایران، شکاف‌های عظیمی در پدافند موشکی آمریکا و اسرائیل ایجاد کرده است
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.55K · <a href="https://t.me/farsna/452976" target="_blank">📅 19:37 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452975">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9bd74a55e6.mp4?token=UjL7orpthD9D7IRr-FVjuTrOdYOH-CielsyQH0Z-LLEJlcVI3-ztxvY03ddPrSsQnaL9JZCCGTDHBPCo0RtOv7Q8LX4cWEbhU7iIpeiZhEwnDxFZGMBmFPCWoVY_m5MqDX9PRful_O0cZszeHo0t1n8taRlROBgKe2GBIUqCjnhtl35hQx_UKrFAaV4Cg74pbtYhD1F0JHgD2uT24zm0ZlzDldkUqg5gi35a1CY3S9C12UAqVt-jM6P2Evr2DWwzypp1GAvGmHBzhMvl8-ipIqBKYSZc5QxfGtBGC5y2Tx7WMDeIwpgRMuUAQSDm9_ez0lRZf8DD4bCuK7ZSPlH6aA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9bd74a55e6.mp4?token=UjL7orpthD9D7IRr-FVjuTrOdYOH-CielsyQH0Z-LLEJlcVI3-ztxvY03ddPrSsQnaL9JZCCGTDHBPCo0RtOv7Q8LX4cWEbhU7iIpeiZhEwnDxFZGMBmFPCWoVY_m5MqDX9PRful_O0cZszeHo0t1n8taRlROBgKe2GBIUqCjnhtl35hQx_UKrFAaV4Cg74pbtYhD1F0JHgD2uT24zm0ZlzDldkUqg5gi35a1CY3S9C12UAqVt-jM6P2Evr2DWwzypp1GAvGmHBzhMvl8-ipIqBKYSZc5QxfGtBGC5y2Tx7WMDeIwpgRMuUAQSDm9_ez0lRZf8DD4bCuK7ZSPlH6aA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📷
پرچم‌های سرخ «انتقام امام شهید» در دست زائران خسروی  عکاس: بهروز احمدی  @Farsna</div>
<div class="tg-footer">👁️ 9.32K · <a href="https://t.me/farsna/452975" target="_blank">📅 19:32 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452974">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">دادستانی تهران علیه فلاحت‌پیشه و یک رسانه اعلام جرم کرد
🔹
پس از انتشار اظهارات یک نماینده اسبق مجلس که دوره‌ای ریاست کمیسیون امنیت ملی را در زمان نمایندگی‌اش برعهده داشت، دادستانی تهران علیه این فرد اعلام جرم کرد.
🔹
برای فرد مورد اشاره و همچنین رسانه منتشرکننده پرونده قضایی تشکیل شده است و به زودی با حضور در مرجع قضایی تفهیم اتهام خواهد شد.
@Farsna</div>
<div class="tg-footer">👁️ 9.61K · <a href="https://t.me/farsna/452974" target="_blank">📅 19:29 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452973">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0a95fa2c53.mp4?token=J90C7BaYvwrF0MHC-31BrjzaZykP2Grk8xvmcJ48GnROj84tW4XKYHM0r-KxtHYX_gT11Tx8ACVoJSEV9bEfveah-j1GUVqRkjGhNJDw92wr3HP7DaQJOlQ-diRpPn4k16c778KmUfUPHlhhBON-imNdretl6STJF0adQ7gjZK2h73NskMEOMPnmQ371p7TUEDnGMkpdcYOOLm0PshIe5FSi2Lt51WoftU9hPOdvY8dKowKRkI5hUAmnYVA_0YupO6Frw4zqSuQzVW56hpknZYxM6FO-XvlX2MGLAAwMAB_nuLp8jhXoNIviwGrXOPXRMxS1oTEA5_N1dOZTu8CHNI5C1JP29l7fIqfFtbvw6d0YCzZeD5nH01pOZdvIsx9UzbeuxeaNt8UGZeh2uDdgskeFWD7wJefDqtIt2ru3YpyzYMtDAwqckKrqhgOie69yttxwnG4WhQFzXFBAddfpYKqXCYxqgb9-sxGibEYef5v4zhItXBx_CqZM6Iw6fE2EF0xs1Tu6AnBxfJOsaV14P6Lxa_11seCZ6WAMPtNZbywWZvgoyUbsVjeZ-9ZKZdYs33QPACo89zuPKNlKc-kUuBeg1VWXQzcjeayqtI1MKtJGCzkCBaF2P_ODmtT82UNLv9IbpqiwxdLk3q6X0RO2NoNpOXi7zoSsC4wpNuKsDWo" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0a95fa2c53.mp4?token=J90C7BaYvwrF0MHC-31BrjzaZykP2Grk8xvmcJ48GnROj84tW4XKYHM0r-KxtHYX_gT11Tx8ACVoJSEV9bEfveah-j1GUVqRkjGhNJDw92wr3HP7DaQJOlQ-diRpPn4k16c778KmUfUPHlhhBON-imNdretl6STJF0adQ7gjZK2h73NskMEOMPnmQ371p7TUEDnGMkpdcYOOLm0PshIe5FSi2Lt51WoftU9hPOdvY8dKowKRkI5hUAmnYVA_0YupO6Frw4zqSuQzVW56hpknZYxM6FO-XvlX2MGLAAwMAB_nuLp8jhXoNIviwGrXOPXRMxS1oTEA5_N1dOZTu8CHNI5C1JP29l7fIqfFtbvw6d0YCzZeD5nH01pOZdvIsx9UzbeuxeaNt8UGZeh2uDdgskeFWD7wJefDqtIt2ru3YpyzYMtDAwqckKrqhgOie69yttxwnG4WhQFzXFBAddfpYKqXCYxqgb9-sxGibEYef5v4zhItXBx_CqZM6Iw6fE2EF0xs1Tu6AnBxfJOsaV14P6Lxa_11seCZ6WAMPtNZbywWZvgoyUbsVjeZ-9ZKZdYs33QPACo89zuPKNlKc-kUuBeg1VWXQzcjeayqtI1MKtJGCzkCBaF2P_ODmtT82UNLv9IbpqiwxdLk3q6X0RO2NoNpOXi7zoSsC4wpNuKsDWo" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
تنگه هرمز در ۱۴۰۵/۵/۵
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/farsna/452973" target="_blank">📅 19:24 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452972">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8f8c0b6218.mp4?token=tUA1g0iMtR74E5RUcM5EoUbHgtagM68vcCk8Uq3pTL_6o7zv08ln7Jfb3MKe2PxZKZfvZkueC4LoNIR6ZR7Qw32QJwAvozuc4KL_o6COb2COzj8DQIbj15mg63qKDkV2ABZDHJVtWpixqllyL1osd3CoE1Ati_MvvG7r69qCQjpKGa8wdKulSiq2JwoWIMctz9wMA9rvEZo7QlzqRdnvX5jT7jMlGkdXgZr_LJGZXXA4JCA1eOD_lw5VGFwVf6E4xsvHMDp9kdqgttCpK7H6jD8MlDUs_EIRiZV-2EVUP6oPhMK-e1DQ2aNOVy003O7aSorFLB9HBf1saMaE7dEOEDzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8f8c0b6218.mp4?token=tUA1g0iMtR74E5RUcM5EoUbHgtagM68vcCk8Uq3pTL_6o7zv08ln7Jfb3MKe2PxZKZfvZkueC4LoNIR6ZR7Qw32QJwAvozuc4KL_o6COb2COzj8DQIbj15mg63qKDkV2ABZDHJVtWpixqllyL1osd3CoE1Ati_MvvG7r69qCQjpKGa8wdKulSiq2JwoWIMctz9wMA9rvEZo7QlzqRdnvX5jT7jMlGkdXgZr_LJGZXXA4JCA1eOD_lw5VGFwVf6E4xsvHMDp9kdqgttCpK7H6jD8MlDUs_EIRiZV-2EVUP6oPhMK-e1DQ2aNOVy003O7aSorFLB9HBf1saMaE7dEOEDzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
جادهٔ عشق؛ مسیر پیاده‌روی اربعین حسینی
@Farsna</div>
<div class="tg-footer">👁️ 9.87K · <a href="https://t.me/farsna/452972" target="_blank">📅 19:18 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452971">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ImchYrossUJNxnDcfQUnA8IbfZHwpBm4uO2zI0PZaguk4412SeSy-f1Da5qle711PxsCY5relQfzhx8ulN3AFH29u4Y8oowFDxbDXOT9Cg67OKecHmgsqk8B3f9SE_8g0qkEhlVsF-ePxZiThKz-r-5xCejYZYZQ8u8LcFWO-CEsEekxA4_cd0Qnmq3-jCF1XzAJVIF2tqWNT1bMUjcq5O2OAelf7KLCU_3ZvEFkKXW87vKNJKoDCg8vgZFPxL0vpd7VpbWJ8Pg10MDL1VEbhhOjCO_NjteyJ3d48giFIbEgpEYekfOrq_1vk_hSOCB1g05LodbPRYXYT_dzmK0eVA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ باز هم توقف حملاتش در ایران را گردن طرف‌های میانجی انداخت
🔹
رئیس‌جمهور آمریکا دونالد ترامپ باز هم مدعی شد که بنا به درخواست طرف‌های میانجی حملات به مناطق اطراف تنگه هرمز را متوقف کرده است.
🔹
در حالی که گزارش رسانه‌های آمریکایی حاکی است که حملات به مناطق جنوبی ایران به دلیل اثربخش نبودن آنها متوقف شده ترامپ گفت: «من به درخواست طرف‌های میانجی پاسخ دادم تا به مذاکرات با ایران شانس بدهم.»
🔹
او سپس بار دیگر ایران را تهدید کرد و مدعی شد: «گفت‌وگوهای عمیقی با ایران داریم اما اگر شکست بخورند به عملیات نظامی گسترده برمی‌گردیم.»
@FarsNewsInt</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/farsna/452971" target="_blank">📅 19:09 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452970">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IcKG71b7vCmXHK-QgqA1eantcdvqWj6BzjCpcNxo8rRB9QK4NtYV_ok177YDTrglDWuis3kU4_GsOUp8rY8NAD2GAOnDiuouIdofFT59gOayTK97Ka2fufsiWm1Vr0W_ibs7bZVPVg6qssNsocaChUEynhOtsdyyJe-n3UB-ThN_KfUojF9BBMYw2K50Xl7VEVPZozBM2Xf11oYeiXKe0qvZbt1xOOU71fDp7eGSjSQfXUgvegno4Cf2-xtyok5cQyBxWFQgDEnb5JQNuW832huHe8IRdoW48ABhTDblFIjb_NJi6heo4lXuSjPmEs1fI1rEmushWT_ub0HJ57TJOA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
پیمان مقاومت
@Farsna</div>
<div class="tg-footer">👁️ 9.27K · <a href="https://t.me/farsna/452970" target="_blank">📅 19:04 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452969">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">🎥
گفت‌وگویی از پشت بی‌سیم خیابان با میدان
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.4K · <a href="https://t.me/farsna/452969" target="_blank">📅 18:55 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452962">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/M1zN9-bLoqOnCRT0uzKXlbBsqfNtdPgOeZdWTicNA01sn_n1qiynTht11ze8XuFMFUCHtqyWjzDcUDfyDy9YZjJBvdQB_CR4Zi8Mf3O7NfsCGBZkNo62JCZ3DTOkg5tpPv0MqPPOCljB4hEqGMBBenG_z1c9nVMYr6FYFw4bddRDRbyvq4neFVeHUfpHdAbO2yYiYEe2OAjVjdXzIpDFO8bkorS7t7WRtABYhKxxk-vj-oQf0ssCCWnZtSAPPUyrIzUbl8nKqrS8QZT4GBfOIKv5Wbo28mJCeTpZultqqP1PRybMUy09ot_O7MJbRcrsoTdUMFC0eqcFSUWdJGN3cg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/BnQ7tG7a6ATeU10woOy6hXC__kNtS8CZ_gpFZDasD0aAd47L4PlA9xjXLerSBx0xRTfr3nYfqOvLB1ZDUr93UpUpL9ISIeHRc2BSXiZ9t97LbXtuhAgqPFLezWfXaA_LU84WIyXHVRjVk1V5z8PY5DGao4wP-pR0zt9CiM90taUfRL3nSvXItRPGiyvsjiBabcK3s3I322U-_tUruRbaNrjjfX29vmfsBjZo8xI7jwV7Gpam1501w4_79x6KNmCfyH55Hh5WgvGRElUH5fRUIJd9gzkjjQ8Ob2_Qgbq79Jny06z1K7_-86HT1DGZIFmTTQz46J_c6g6n6Ih1lLZ98g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/FLZa3KYHEsWOG_c9REi1ENLUFqnSPFNSM-PKugvgarTRCNTtTNa1bgmlvFWgRHh-VFtYRiwM2nZ_rEReUpvzjOVuu5L5faljIj9USql6pk0083o5LE390gqdIKYVYptpVnASryX94HQ-BEUcXiS3gf5VDQgiWmtN_YeEzVFyIDf6wgfooZCbTkttem65Ftqj06_TvQe46FJVgG7dvwLERYYjQtjZWzjJoD9di00UJ4B3A3kfY9F7MLw2n2Wkfw7qvCBLkjne5OpCZYMKUiROGYJYonooSjDCqRCxQ_9AIbuAteIqYXnxYo3Wyf4ucfi4VZtNEGqO1e44QYgzcKI5XQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Sb1kECSac7C-Gpmn14HDV9PoZAUpSjVYKWfkVZ6vngFBFtUoC5D01Ghgc9wAQHIplifLMuPF-k4C6uuTPPNl3T3vNBNlky_tah-U_5h3AMK1TEcIWuCZYYDzxoKw2iHxwcGSyUO1UrkycYrJyEHqvwRQekwfln44X9m1ukFXRUWK3FgBa-xkIlzBr4Jk7Taf-f6l89bGKed2Jhlp5MGrJs03JYZoZmsAi6D94lRSg2ci9Cc9LTG22tESOdfm1WFsOV8qad9MTYCK4JjH5lPkY-JxS6oUL-RrEIf-K5BPuSNhgBCVun_OPNX9iibtbbfuEhVxbRpOpLz4-PK2zj-ADw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Sol2IJliYXa18aNHvY4k_yVhG22J019X5PQ_JLV0a8cuG4wfwZEqMajnfZXDL5EriYW7TX9x6o8rUL6H63vJ_hPxxYRZnV1rqxmRF8L8XMTSAWtP_OP8WbBBAo__U9tveKrN7zT0fZW9o5Kt8s21fWBtTYXMvR_Cz7Qreltsd1kC7vJ0mbEP4Rv8hkXATY3gFZ3lrh6yH6f7-LlkrSD93LoSE7HCF8UWem_lJNVV8zrw_WWf5xr49QNoBPu0bycu02QAjSTrhYfesa4qaP8HOTrFzNxL7vqu4XbqOhsGSfbN_1NdWEHyepGvOA2tpejLN3W5W_wxeNJZpky_CnLN1g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/fJVDWtCYnpgzZJp95XSxqjErhLbAko6vrZPPIRsQNKysElnjUzGf9yL8DCfDymndSQ3iNC3cA0Pe4NtHrIpPF97hOiwXzf0GnYrW94R1wt8HNLfMwQqyk0EE7e3v1QhmS_UIh0PLqo804zttt4dMlfeCkcnSz6YTI5qHkLKdKuYPw3vBL9_Btc4dlUJf6JGTzSnxhbyzTEGwVZ3XODebm2i95t_aLBt-V6OBD_y3x8wyzdr_uVimtDc1otLmZvgKntLEO1-TJrDLsdTN4fSPYQn5lod6_dk-tTzeZpMgbPOFQBGZmoWFaa4CmwC3KwN4I8RvC0FVpMck6dPJpJCX9w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/GuASs-fG022iGenW5uwwoR3Is4RcylKqie0935foHfovGRfDEi_xyBD9j-WbOvGw5lXO8a1DvaJFRQ2va6CM0rE1FJgY_MxQVv0g2xmS72nzQRWVWisiewuKJ3_j8wSyWWU2uDudNlvD3IQKc8JDBc3VXxWLXxFR7UATu0DXOH-FMpVgvsuauzyWg0PsrQg9_yV9tYro8WR6OM5ZVl-94qgSLuOKVOffr9wcA6NN-cO0MO3ep5TBKkR9Myc4mkKc2PylsqoWWN8EbETiKnT_TqZt5lYAIRjYLKjWkd0WbhfT6gNL_ZLVUv-ibyzmmEILEC-hxTDYieO08DJglBqOqw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
پرچم‌های سرخ «انتقام امام شهید» در دست زائران خسروی
عکاس:
بهروز احمدی
@Farsna</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/farsna/452962" target="_blank">📅 18:45 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452961">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f6d49d1698.mp4?token=IH_StLqlZOU1QYcOMuqaLVoiJJNfubhJCiw21RClxIcUUQolGPFdAEOBMqBEjNhEkXjmS11NDEY2oSbGyTx1Tdj1QFa1UjqElV5NiV1KUMAc7Wz0z95moE5-bUL98tuYMeOz9AzleyrArriFYQh28qVRi906jMqsehJPNZmnh3YV7VwM1GsjhxxeA4d-FzdjtJmFuwZwg5pWsvwVN4kAMDcdHoYu44zh_Rh-TxgcopM5h3BSBX8MnrqU7K0grwA2ZZ6b3g8xQvJx0yutTbgXeWDYK-Fi4jXfKt2eJZjdDgFvgMCCSouUCrWFvvtP_HBwWFK3lNa45yPYJ1-1wY4_1Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f6d49d1698.mp4?token=IH_StLqlZOU1QYcOMuqaLVoiJJNfubhJCiw21RClxIcUUQolGPFdAEOBMqBEjNhEkXjmS11NDEY2oSbGyTx1Tdj1QFa1UjqElV5NiV1KUMAc7Wz0z95moE5-bUL98tuYMeOz9AzleyrArriFYQh28qVRi906jMqsehJPNZmnh3YV7VwM1GsjhxxeA4d-FzdjtJmFuwZwg5pWsvwVN4kAMDcdHoYu44zh_Rh-TxgcopM5h3BSBX8MnrqU7K0grwA2ZZ6b3g8xQvJx0yutTbgXeWDYK-Fi4jXfKt2eJZjdDgFvgMCCSouUCrWFvvtP_HBwWFK3lNa45yPYJ1-1wY4_1Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
آخرین دیدار مردمی آقای شهید ایران...
@Farsna</div>
<div class="tg-footer">👁️ 8.68K · <a href="https://t.me/farsna/452961" target="_blank">📅 18:42 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452960">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JbqxsoAoTXiKX5fqZvaQsgLC1QRw3wpMukOcYKgPnV8lRV3ZRP7G0IUFgSVaNDFTTq36o4Th1oqN9nIpNeDQLF3aw-64iCs_KFLp3MlLgmDGB4UbHOUNpQOSlT5SctX4DaRJIMbtQA4X1uDqUcThp3uSPaLEGYNTJK1d7s__fSUr7XczwiVLotCjDnITnfIGKD_zJisRDYR0E4jVR5BobRyEO3RPMae1M1GV8fWXc1ddbsCVMD1HVtItIvQwMznBfOC8nM4h1jWoU1NXsfZ1kTwKSS2vF-rkSPSr2y07Nid-sp0qoaK0lGnX-Cze0wXZIbmRB4cH-cbhBXU2tWeRFA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فرار نفتکش‌های عربستانی از دست یمن
🔹
داده‌های ماهواره‌ای کپلر نشان می‌دهد که نفتکش‌های حامل نفت عربستان برای فرار از حملات یمنی‌ها کانال سوئز را به جای باب‌المندب برای خروج از دریای سرخ انتخاب می‌کنند.
🔹
بیش از یک هفته است که محاصرهٔ بنادر عربستان از سوی نیروهای مسلح یمن بر اساس راهبرد «محاصره در برابر محاصره» شروع شده است و دیروز تنها ۱۴ کشتی  حامل کالا از این آبراه عبور کرده که کمترین آمار یک سال اخیر است.
🔹
ابرنفتکش «المپیک لاک» با مالکیت یونانی که بخشی از ظرفیت خود را با نفت عربستان پر کرده از سوئز عبور کرده و حالا با تغییر مقصد خود از اروپا به مقصدی ناشناس در آسیا می‌رود.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.32K · <a href="https://t.me/farsna/452960" target="_blank">📅 18:36 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452959">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a1c9b9bf4b.mp4?token=Xoip262y3akS2PGBeBjDszGsHELeZ807ez2TDhx8nk87lgreN0nMEokiVhILnA-SqjtTjjTnLKH4D4vcr90DjkNhvelRoOBgg0aEktdFLhdCPZo7xG3FJzV7BBk-0wMkyGTaTuSo1LuEvuuHSMsp1TPMU3udgX-O7EIxNBbRwWCwdo9eeFuIMK3ZddtgTCh_ZfiBntMTWYfp0-hnfaNtcx31V9BZPMciHv-BvNR-gytbWLQ_igpvwS_4lx30QFn7b4WQpUY5AK6befE0MgDAzFwEJzbqlxfMfUL2BjYNvGzBTnMTDSSnAuycIk-AHxfx0vWOWirftmBx091JCWDyaA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a1c9b9bf4b.mp4?token=Xoip262y3akS2PGBeBjDszGsHELeZ807ez2TDhx8nk87lgreN0nMEokiVhILnA-SqjtTjjTnLKH4D4vcr90DjkNhvelRoOBgg0aEktdFLhdCPZo7xG3FJzV7BBk-0wMkyGTaTuSo1LuEvuuHSMsp1TPMU3udgX-O7EIxNBbRwWCwdo9eeFuIMK3ZddtgTCh_ZfiBntMTWYfp0-hnfaNtcx31V9BZPMciHv-BvNR-gytbWLQ_igpvwS_4lx30QFn7b4WQpUY5AK6befE0MgDAzFwEJzbqlxfMfUL2BjYNvGzBTnMTDSSnAuycIk-AHxfx0vWOWirftmBx091JCWDyaA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
عبور زائران اربعین از مرز تمرچین
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.86K · <a href="https://t.me/farsna/452959" target="_blank">📅 18:24 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452958">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">‌
پاسخ شستا به گزارش زیان ۳.۸ همتی این شرکت
🔹
شرکت سرمایه‌گذاری تأمین اجتماعی در پاسخ به گزارش منتشرشده در فارس دربارۀ زیان ۳.۸ همتی این شرکت اعلام کرد: قضاوت براساس صورت‌های مالی میان‌دوره‌ای، تصویر دقیقی از عملکرد شرکت‌های سرمایه‌گذاری ارائه نمی‌دهد.
🔹
بخش عمدۀ سود شستا پس از برگزاری مجامع شرکت‌های زیرمجموعه و شناسایی سود تقسیمی، در صورت‌های مالی سالانه ثبت می‌شود و به‌همین‌دلیل، گزارش‌های میان‌دوره‌ای معیار مناسبی برای ارزیابی سودآوری نهایی نیست.
🔹
براساس برآوردها، مجموع درآمد شرکت‌های گروه شستا در سال ۱۴۰۴ به ۵۷۲ همت و سود عملیاتی آن‌ها به ۱۰۹ همت خواهد رسید که نسبت به سال گذشته افزایش قابل‌توجهی دارد. این ارقام پس از برگزاری مجمع سالانه شستا نهایی خواهد شد.»
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.15K · <a href="https://t.me/farsna/452958" target="_blank">📅 18:16 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452957">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cpvsBvtRFpeU3v-IbFhTujNXfAmy1A_zLkUM3OD7chC7Uzt3r-cIFKGyC-nTqTXhLlljLEbEXqqBVgdeJdFr_YZuhk1Vr_rFjp856mMdmyo4awRy3B8_6zaFPjt5zkFoGRaDjt4TJaxXSgTT14_-v66CA3hR_99dAIskGlJiqI0tWB15yElkyqGVSOoJGenMre9q4x2MWRRBsWeZDGA18AyDoy9xrcHXQuIth8urcAxLoktN7R_Bq_L-vsAykzGdxxeVoBshDX-ge7PFQWaBJubjEP6Q0WacZlSyyxWZDQ9ZxbNSxCvhBCwJzsNrgO7uw1wViUzFbqzHkWgn5ytNRw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فلزی که در داغ‌ترین شرایط هم دوام می‌آورد
🔹
اینترستینگ‌انجینیرینگ: محققان چین اکنون آلیاژی توسعه داده‌اند که در شرایط دمایی بسیار بالا، خواص مکانیکی خود را حفظ می‌کند و در برابر تغییر شکل و تخریب مقاوم است.
🔹
به گفتهٔ پژوهشگران، این ویژگی می‌تواند عمر قطعاتی را که در محیط‌های فوق‌داغ کار می‌کنند، افزایش دهد و نیاز به تعویض مکرر آن‌ها را کاهش دهد.
🔹
چنین موادی برای ساخت موتورهای هواپیما، سامانه‌های پیشران فراصوت، توربین‌های صنعتی و راکتورهای هسته‌ای اهمیت زیادی دارند؛ زیرا قطعات این تجهیزات به‌طور مداوم در معرض دماهای بسیار بالا قرار می‌گیرند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.32K · <a href="https://t.me/farsna/452957" target="_blank">📅 18:10 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452956">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Q8DVBkasYcWA4ZoDCLdgaPgnpqPVUcbC-2rkBF-djwvgD27JYvgDjlC1JJ6Pnxw9HAixXYTS_unn2UfPUpL6W0AMjr7fyn3ZTFMycgbKoELVdprnCV7NK7vdUFSKAw7Z_B5nKVdQNxNgOZGDcNEp71-rFlnuskpA76qy8KjCSatTLKt_NMf9nr_NObDAwALKVWnbj0vJdrG5yhLB5Ye2XvrjYoX60BzKcj73pQoO3zQJI7ArFyG_ZqrfMXi_d-lXEPVejXQkjDr-EyCu_kbC9KFS2GK-fIo_nwEicKnwEqacudKKQ9gpjHryOHSJ3RlGJhb8UAVTF2wBQLagsqE0EQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اطلاعات محرمانهٔ مشتریان بانک بزرگ هند لو رفت
🔹
رویترز: یک پژوهشگر امنیت سایبری خبر داد فایل‌هایی حاوی اطلاعات مشتریان و اسناد داخلی بانک بارودا در یکی از انجمن‌های دارک‌وب برای فروش عرضه شده است. این فایل‌ها شامل اطلاعات هویتی، جزئیات حساب‌های بانکی و برخی اسناد داخلی بود.
🔹
این بانک همچنین تأکید کرد اقدامات لازم برای محافظت از داده‌های مشتریان و بررسی ابعاد حادثه در حال انجام است و در صورت نیاز، اطلاع‌رسانی‌های بعدی انجام خواهد شد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.64K · <a href="https://t.me/farsna/452956" target="_blank">📅 17:56 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452955">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9afad1b6c3.mp4?token=hwcFW7sycq-JfKvIgqSjx86ObNtKFP3PcX6MmXH5d_fRdomirACigenxQOymktLUfzaMP1xyOL8jl3pOqTN5ytknYrFIWVzd1ce2ZtUKlrla4nOU05R_2uq7bUoAk2F3rTaUGggdliUgqVF90min3rRBUs_m9WU5-CKbprz7njXFdg93dAydiiuzjZ-SNWrLnpdD2x4aYvUgObD6fWqF_NUTJ8YMNcZoRvRET5lFAtGMMyEu180oje7J4LNyZtGFY2Tx583cKI_b4UoMTmdKHaMUMFiNvg_SeLVTRz_DjTJpMoJk_3Je98XNZ3PPp5FAsljFghT_tnWH79FwMHxihg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9afad1b6c3.mp4?token=hwcFW7sycq-JfKvIgqSjx86ObNtKFP3PcX6MmXH5d_fRdomirACigenxQOymktLUfzaMP1xyOL8jl3pOqTN5ytknYrFIWVzd1ce2ZtUKlrla4nOU05R_2uq7bUoAk2F3rTaUGggdliUgqVF90min3rRBUs_m9WU5-CKbprz7njXFdg93dAydiiuzjZ-SNWrLnpdD2x4aYvUgObD6fWqF_NUTJ8YMNcZoRvRET5lFAtGMMyEu180oje7J4LNyZtGFY2Tx583cKI_b4UoMTmdKHaMUMFiNvg_SeLVTRz_DjTJpMoJk_3Je98XNZ3PPp5FAsljFghT_tnWH79FwMHxihg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
یک پهپاد ناشناس در استان بابل عراق سقوط کرد
🔸
منابع عربی می‌گویند احتمالا این پهپاد لوکاس آمریکایی است.
@Farsna</div>
<div class="tg-footer">👁️ 9.49K · <a href="https://t.me/farsna/452955" target="_blank">📅 17:49 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452954">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/add39ded09.mp4?token=T3QzzyjEHu3V1YS9D8kkzHJVRTBLQckFcghQ1TuwDRXh3uwlm-0fAd4D7j7BLFaLFZ-ktMEIrmjDZOWHLUISFvxg_mRzOiim7VN0ABt-QpsZpND64x9s0I1SuFKAEjQEaB349loBzhip1w8TapUa52Q-950FAZEeQV3QZQKl7yS9sDZzHEX1txFd40kNDWCULcngbZXza4UEe5_LKTRSmRUoO0zKVWn3q5mqedBKNR6mWiNOWLw5copGxUJQa7_0ohTf7ZdeZYdYkPF6AL7ERCvFKmf-GZb7lmxbVATKAweFgIq3HOJyowWCOrOnrML-7svz7d1GMP_F4x8QraR6Mg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/add39ded09.mp4?token=T3QzzyjEHu3V1YS9D8kkzHJVRTBLQckFcghQ1TuwDRXh3uwlm-0fAd4D7j7BLFaLFZ-ktMEIrmjDZOWHLUISFvxg_mRzOiim7VN0ABt-QpsZpND64x9s0I1SuFKAEjQEaB349loBzhip1w8TapUa52Q-950FAZEeQV3QZQKl7yS9sDZzHEX1txFd40kNDWCULcngbZXza4UEe5_LKTRSmRUoO0zKVWn3q5mqedBKNR6mWiNOWLw5copGxUJQa7_0ohTf7ZdeZYdYkPF6AL7ERCvFKmf-GZb7lmxbVATKAweFgIq3HOJyowWCOrOnrML-7svz7d1GMP_F4x8QraR6Mg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
پنجره ای به مراسم یادبود رهبر شهید انقلاب ویژهٔ اهالی رسانه
@Farsna</div>
<div class="tg-footer">👁️ 9.4K · <a href="https://t.me/farsna/452954" target="_blank">📅 17:46 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452953">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LwRytSQdBM4mzg-fP2RcgxYDLrjl8bDe6qSdYO-dnDfEvvYTflSozHaHMBfADPewqGuBiFkbg5Zs4rP0W5u7c1qcvQp60AHkVfSIwJNuTF-OjjCArPhsm1ZC7WMgDvL41e79pRXAJBwpmTCpqiHqGYnk34ddeny59ZDXE8AXXEc1yfWzZVdA23sOrSRiHMZeFLjxE-cXunzCcv5RYeEKXKU6OLIDhBoDnBLIIYzw7BtnE1IzaOhhK_HnS0mSSt0xCqr3S2ve8oX9DBN6p7h8hbgCH71ShSjhnNpEvilqM8BUO7cfrpU9gpoirjAzhtuqclKWYqJAoRjZmtVUMNPIeA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کاپیتان استقلال آبی‌پوش می‌ماند
🔹
وجود اخبار ضدونقیض پیرامون آینده کاپیتان استقلال، ادامه همکاری روزبه چشمی با آبی‌ها تقریباً به مراحل نهایی رسیده و اگر اتفاق خاصی رخ ندهد، تمدید قرارداد این بازیکن به‌زودی اعلام خواهد شد.
🔸
روزبه چشمی که قرار است برای یازدهمین فصل پیراهن استقلال را به تن کند، در مذاکرات اخیر با استقلال بر سر مبلغ قرارداد اختلافاتی داشت.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/farsna/452953" target="_blank">📅 17:39 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452952">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d61854b39d.mp4?token=KWCfj7QxFEtED7K1rUQUt-wmRzzegrVzi7wJLWj_rdICba2cDxW5TYQasxgUqPsBEZ0IAWzmjZjBeFKW43CGAE-vZgvgUv1niWB4400lZz1HeyhBE5d6gHdaybXsFDBnilEvreiI18Piz_VwjLVMCFYM_WpeX6vYi5-B6vDZlSgoWtdrKlxpK8CupVtpSFN59PKsEyZp_3vC35Evtv8td_r8GBKKVNtFugYbBiVH8NFtbngbPn5l5-MaEsM-UHynQSzhLKqZSTaoSmu2CHoQa1ZGbfdW3-NXD0zOsp8g8eCWC_fEZOa5y7MnuHhzLmg-tAt5xCrSD5QvUN5ju0Z1dg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d61854b39d.mp4?token=KWCfj7QxFEtED7K1rUQUt-wmRzzegrVzi7wJLWj_rdICba2cDxW5TYQasxgUqPsBEZ0IAWzmjZjBeFKW43CGAE-vZgvgUv1niWB4400lZz1HeyhBE5d6gHdaybXsFDBnilEvreiI18Piz_VwjLVMCFYM_WpeX6vYi5-B6vDZlSgoWtdrKlxpK8CupVtpSFN59PKsEyZp_3vC35Evtv8td_r8GBKKVNtFugYbBiVH8NFtbngbPn5l5-MaEsM-UHynQSzhLKqZSTaoSmu2CHoQa1ZGbfdW3-NXD0zOsp8g8eCWC_fEZOa5y7MnuHhzLmg-tAt5xCrSD5QvUN5ju0Z1dg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ثبت‌نام گذرنامۀ زیارتی در میدان آزادی آغاز شد
🔹
رئیس پلیس گذرنامه و مهاجرت فراجا از راه‌اندازی بخش ثبت‌نام گذرنامه زیارتی در رویداد «محرم‌شهر» میدان آزادی تهران برای نخستین‌بار خبر داد.
🔹
سردار امید نودهی گفت متقاضیان می‌توانند هر روز از ساعت ۱۹ تا ۲۳ با مراجعه به بخش صدور گذرنامه زیارتی اربعین در محرم‌شهر میدان آزادی، برای ثبت‌نام و دریافت گذرنامه زیارتی اقدام کنند.
@Farsna</div>
<div class="tg-footer">👁️ 9.25K · <a href="https://t.me/farsna/452952" target="_blank">📅 17:33 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452951">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uKY8Be0s0yd1Pku1bNaBHYDZKn7FugXDDOVwDbZUpekOo3in4HNcilMo0YoLi6Uluz_bRh1Ti5TtCZLGkaRrSQyExxBOzRKhbpYocBlqKy3JmT87tHB53DVwFL7lxaSk3mfKts-Wl2_nEA0rvRftkTIIJUtXSapzQWnazDJjYWog28V6IsxfoPt21eAGGY497xskKdIvmdo5-pJI7ukrj_hQRbBVfbwQ9kLrpq3E-yy8Fz0g0Zju2hFjEbkEySzwGEW0fSuubNWLNl_95BWngIu0kdHkDm4HoV9JxNedz6yipEyAqpxOUJ46x1772RI3Tz6SzEXfqRZtWMo6V4Ph2A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رئیس بانک مرکزی: از ماه پیش ترمز تورم را کشیدیم
🔹
در تیرماه نرخ تورم ماهانۀ ما نسبت به ماه قبل تقریبا نصف شد. این نشان می‌دهد روندی که برخی فکر می‌کردند در آن تورم بی‌محابا افزایش خواهد یافت کنترل شده. در ماه‌های آینده نیز کنترل بیشتری روی تورم خواهیم داشت.
@Farsna</div>
<div class="tg-footer">👁️ 10K · <a href="https://t.me/farsna/452951" target="_blank">📅 17:29 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452950">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hfuS016Sp99lGvv_BHcQrpjp8lS5fivtm_JUycIqfr2U2928CZrVAH8vsftrdGRM-adLOhChMgb-AplJsZiC7KKnL2tFeNSdWpN8UmcBkBeywzxxu9xcb2orTueothYEwNw6i_Vaco4jZcf4AfqAm4Glg7VSg6HHcEbQNz9nJkoq_4THldT6KuCukTD8ZPAzeyYIs6LC69C2D0K120w3F77AGYmEM-lWc0ONRfOHbQoxnFhxN2xUVT30FPGGJyThM7et2zgWtx0bSvO-OpRwdQqqRCqRmBJl2a94uP87qmmq1dBH4GuwTP1vTHdJ4tSnetjH35rw8A6h75qa8PkJyg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تنگهٔ هرمز قیمت پروازهای آسیا-اروپا را ۳ برابر کرد
🔹
درپی تشدید تنش‌های منطقه‌ای غرب آسیا و محدودیت در استفاده از برخی مسیرها و کریدورهای هوایی، بیش‌از ۴۳ هزار پرواز لغو شده و دست‌کم ۷.۵ میلیون مسافر تحت تأثیر این وضعیت قرار گرفته‌اند.
🔹
آماری که نشان می‌دهد اختلال در مسیرهای هوایی چگونه می‌تواند در مدت کوتاهی بخش بزرگی از شبکهٔ حمل‌ونقل هوایی جهان را با مشکل مواجه کند.
🔹
گفتنی است براساس داده‌های سایت‌های بلیت فروشی قیمت برخی پروازها در مسیر آسیا-اروپا، ۳ برابر افزایش قیمت داشته است.
🔹
منشأ اصلی بحران فعلی صنعت هوانوردی، بسته شدن تنگهٔ هرمز و اختلال در صادرات سوخت جت از خلیج‌فارس است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.94K · <a href="https://t.me/farsna/452950" target="_blank">📅 17:28 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452949">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c8815d452b.mp4?token=XdnIOZGuQwkzSPitIJbMqF3m1Zu6CjFd96UF4Csm-YfZvBeqZ9IG9X3BZh_D2aoIzjfx0RiiK2UeryPQcPqycbF5K44RaAizJAUack1pyjdKrgLkFfVQymmifp4nTDbip6pffWmx4Is199m8HzOIqcsA_BUfteTnQtEYiwoK-ibKTtP0hveeh6TWd9kQa12nbRjtUZ5cEGI30dKWeQqk7MGk5CWjmO2iYJHiwFUEMWjgk_77E5jO16nvAqqHTnytp_MfIOzoyZA79Evwy5kOqMK4v9-4LvCOoXo4EORdN5syhFs0drmBRASy_Dz0NmU5LKZc5N5fwNEp3K5jfjihxA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c8815d452b.mp4?token=XdnIOZGuQwkzSPitIJbMqF3m1Zu6CjFd96UF4Csm-YfZvBeqZ9IG9X3BZh_D2aoIzjfx0RiiK2UeryPQcPqycbF5K44RaAizJAUack1pyjdKrgLkFfVQymmifp4nTDbip6pffWmx4Is199m8HzOIqcsA_BUfteTnQtEYiwoK-ibKTtP0hveeh6TWd9kQa12nbRjtUZ5cEGI30dKWeQqk7MGk5CWjmO2iYJHiwFUEMWjgk_77E5jO16nvAqqHTnytp_MfIOzoyZA79Evwy5kOqMK4v9-4LvCOoXo4EORdN5syhFs0drmBRASy_Dz0NmU5LKZc5N5fwNEp3K5jfjihxA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
غریب‌آبادی، معاون وزیر خارجه: در اسلام‌آباد طرف آمریکایی ۲ درخواست افراطی داشت و گفت اگر آن‌ها را نپذیرید مذاکرات شکست می‌خورد و ما برمی‌گردیم؛ ما درخواست‌ها را رد کردیم و گفتیم برگردید.   @Farsna - Link</div>
<div class="tg-footer">👁️ 9.32K · <a href="https://t.me/farsna/452949" target="_blank">📅 17:18 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452948">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس پلاس</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4e7fa07d21.mp4?token=PWDlj12k4fhoMgVCQxPFDIRRpYhVzDJ0n6zy8nh72KG-B-7-Sv7MYwAraAmL7HZlVvmwUDSHdXohfyq4pzx6CVx05rfU8P_SUXYKuBjIJMruJGgLqdY3_E-MfyU0NBPCgCrX0frjIw7k3ocUwZSNUyg8zFqQ4zYAag5fHVavB2zaaPSr6UJvJncUGhmjz0sZvbil37873AF6JNGGiF6MMWQ4hQoiDerkhcEcakLNsrA836Stan0WlGWnyuY4GYSwUpIPJLg-cPj6gZbrCyBMflbMiDkg1d5OrOW1yTIoY1H0oDOxtfSoufArK_uuun7DjfOVzrdw8M9V2GN3ac0fH5P4q6sKewTgiHyfDvudmBhkgC407FgZDhtFgHxqWtkRTdUfT4S7boLfd4nFG8-VREmynB7rtG0yhfgd8-sN6nk5lrJALX1mNTMLLOHVjENa6NWtHrDJtxj9f5F2Dxk5b2dAdWXOjpm-O9kDNGg_M1wc5dZKS94QGLaLKBvdTkPcchL4hAiHovaDY6RthjzhGiL6T--XyOcROYDjRx2DepM6cCvosHUUtLYkeiERvJn1sSfPvpLjEX0QhapNUU3yD--BWQXCFd27xnW1NECBpveZAMYL263vRVX08m7u27wS3WU3negYHb1KpoUVojauidvMYTRst1qKycda74cvM1s" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4e7fa07d21.mp4?token=PWDlj12k4fhoMgVCQxPFDIRRpYhVzDJ0n6zy8nh72KG-B-7-Sv7MYwAraAmL7HZlVvmwUDSHdXohfyq4pzx6CVx05rfU8P_SUXYKuBjIJMruJGgLqdY3_E-MfyU0NBPCgCrX0frjIw7k3ocUwZSNUyg8zFqQ4zYAag5fHVavB2zaaPSr6UJvJncUGhmjz0sZvbil37873AF6JNGGiF6MMWQ4hQoiDerkhcEcakLNsrA836Stan0WlGWnyuY4GYSwUpIPJLg-cPj6gZbrCyBMflbMiDkg1d5OrOW1yTIoY1H0oDOxtfSoufArK_uuun7DjfOVzrdw8M9V2GN3ac0fH5P4q6sKewTgiHyfDvudmBhkgC407FgZDhtFgHxqWtkRTdUfT4S7boLfd4nFG8-VREmynB7rtG0yhfgd8-sN6nk5lrJALX1mNTMLLOHVjENa6NWtHrDJtxj9f5F2Dxk5b2dAdWXOjpm-O9kDNGg_M1wc5dZKS94QGLaLKBvdTkPcchL4hAiHovaDY6RthjzhGiL6T--XyOcROYDjRx2DepM6cCvosHUUtLYkeiERvJn1sSfPvpLjEX0QhapNUU3yD--BWQXCFd27xnW1NECBpveZAMYL263vRVX08m7u27wS3WU3negYHb1KpoUVojauidvMYTRst1qKycda74cvM1s" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
شگفتی فرانسوی‌ها از رگ غیرت ایرانی‌ها
روایت جذاب مهرداد میناوند، خداد عزیزی و سایر فوتبالیست‌ها از تقابل با ضدانقلاب و آمریکایی‌ها
@Fars_plus</div>
<div class="tg-footer">👁️ 9.06K · <a href="https://t.me/farsna/452948" target="_blank">📅 17:17 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452947">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">هلاکت ۴ تروریست در نوار مرزی بانه
🔹
سخنگوی فراجا: درپی اقدام یکی از عناصر اصلی گروهک تروریستی پژاک برای ورود به کشور، یک خودروی سمند تیم تروریستی توسط مأموران شناسایی شد که درپی درگیری مسلحانه ۴ عضو این گروهک به هلاکت رسیدند.
🔹
در بازرسی از خودرو و محل درگیری، مقادیر قابل توجهی سلاح و مهمات اعم از  چندین قبضه کلت کمری،  خشاب، تیر جنگی و  نارنجک دستی کشف شد.
@Farsna</div>
<div class="tg-footer">👁️ 9.14K · <a href="https://t.me/farsna/452947" target="_blank">📅 17:12 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452946">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9152360a3a.mp4?token=K-7-_ZTpv83WfvRd6CQ9YH0yae7s6g5U_RC5_LHJXKv3naDa7zcuCA4ReQpTGOGdN44TBywV9wuJoje0ivfh8jXmdIKCHW3JDsHJqltG6Ep3mEE7H7Va6yWKvgUgqn2Yyg2SniCVIqLS3FigyG10o8Yi_amBWlreke50tyBmTrSYp2uvTPD1_jNAaPffY8ZWq8j_z3i9_gy1r7iMhN144runzUpWStD8gMFGxDhZPDlxFF0beHJyrmLWY2DT2jDMQFbFtLwVt6I9vQICyDU76ip48gxziAZkkR15-nkClcfc2M7Bkr5hzHzcc6tuvmEAQweFstiqps46VzA51ulp6g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9152360a3a.mp4?token=K-7-_ZTpv83WfvRd6CQ9YH0yae7s6g5U_RC5_LHJXKv3naDa7zcuCA4ReQpTGOGdN44TBywV9wuJoje0ivfh8jXmdIKCHW3JDsHJqltG6Ep3mEE7H7Va6yWKvgUgqn2Yyg2SniCVIqLS3FigyG10o8Yi_amBWlreke50tyBmTrSYp2uvTPD1_jNAaPffY8ZWq8j_z3i9_gy1r7iMhN144runzUpWStD8gMFGxDhZPDlxFF0beHJyrmLWY2DT2jDMQFbFtLwVt6I9vQICyDU76ip48gxziAZkkR15-nkClcfc2M7Bkr5hzHzcc6tuvmEAQweFstiqps46VzA51ulp6g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
غریب‌آبادی، معاون وزیر خارجه: در اسلام‌آباد طرف آمریکایی ۲ درخواست افراطی داشت و گفت اگر آن‌ها را نپذیرید مذاکرات شکست می‌خورد و ما برمی‌گردیم؛ ما درخواست‌ها را رد کردیم و گفتیم برگردید.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.48K · <a href="https://t.me/farsna/452946" target="_blank">📅 17:10 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452945">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6ac119cfee.mp4?token=dc-1o2D-rn2jBmz5u96owGrHZJJ6P1ZeawCCYQh6gScCij5vN6dQ3lRdXn7Ca5hgZunHK-L7a7oKDbc799soa3HtvTHnh7L-EoAhxAB5ZmO-KBprp54-IMUSJbyrfXtu-wEDP770LHrn8EQyobMLrSXlUXt5eFN9ity3Zuc95UpMRHIbeozxpXizY9YKjHJzp9I_cXnogWeoWpx_XmmzEXWdo-t5g00qo7ff-AnqF-0cRgjZa9Z43dvDoj1O5Ta4PuAX1SfHbtBG_pmp-ThOOi-8atlJm5Lz_Ip9gyH7L6i3mQ-ZUwhsvUH7IsszGPeWUEPIOwnHOhqLPGJdKTKyzg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6ac119cfee.mp4?token=dc-1o2D-rn2jBmz5u96owGrHZJJ6P1ZeawCCYQh6gScCij5vN6dQ3lRdXn7Ca5hgZunHK-L7a7oKDbc799soa3HtvTHnh7L-EoAhxAB5ZmO-KBprp54-IMUSJbyrfXtu-wEDP770LHrn8EQyobMLrSXlUXt5eFN9ity3Zuc95UpMRHIbeozxpXizY9YKjHJzp9I_cXnogWeoWpx_XmmzEXWdo-t5g00qo7ff-AnqF-0cRgjZa9Z43dvDoj1O5Ta4PuAX1SfHbtBG_pmp-ThOOi-8atlJm5Lz_Ip9gyH7L6i3mQ-ZUwhsvUH7IsszGPeWUEPIOwnHOhqLPGJdKTKyzg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
روایت المیادین از جهنم آمریکایی‌ها
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.79K · <a href="https://t.me/farsna/452945" target="_blank">📅 16:56 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452944">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1554001316.mp4?token=qQySlnB1FxufMGy6WDYBftqgzj9ehDsUvgbJDXQRYgVfrUdEkGq4DW9fC9Kgrrnd2P3XWRSOcx4GKPt7w1sMEY06zq2GNxVv483ptEt-vzyVC_C3cS3gieUui2Rmq9X1dIHxlg7iti3mPsMi5yObodx2mnso_jnLO2epO6hrANu_rKiMFVC4C5kbIJLQ8HIFl7IcCvTdKvhkSqcWbUscNXj1WuGh27TWVOCLFBn7q2mPGPC_ci6es97XdR9rNWt8yFsruT5bDSFhaikVQ2NIsGN2y4I5-r8VeqD0S6fOKCRReEM2fwLToG0sdI7cag5qNO4stk4iNJain7c9_PYBiA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1554001316.mp4?token=qQySlnB1FxufMGy6WDYBftqgzj9ehDsUvgbJDXQRYgVfrUdEkGq4DW9fC9Kgrrnd2P3XWRSOcx4GKPt7w1sMEY06zq2GNxVv483ptEt-vzyVC_C3cS3gieUui2Rmq9X1dIHxlg7iti3mPsMi5yObodx2mnso_jnLO2epO6hrANu_rKiMFVC4C5kbIJLQ8HIFl7IcCvTdKvhkSqcWbUscNXj1WuGh27TWVOCLFBn7q2mPGPC_ci6es97XdR9rNWt8yFsruT5bDSFhaikVQ2NIsGN2y4I5-r8VeqD0S6fOKCRReEM2fwLToG0sdI7cag5qNO4stk4iNJain7c9_PYBiA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔹
صحبت‌های دردناک حامد عسگری در حاشیۀ محرم شهر دربارۀ مادر یکی از شهدای مدرسۀ میناب که هر روز ماکارونی درست می‌کند تا شاید فرزندش بازگردد.
@Farsna</div>
<div class="tg-footer">👁️ 9.08K · <a href="https://t.me/farsna/452944" target="_blank">📅 16:55 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452940">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/v09O4J4nVcWJNPbylrAxppTsgaw-T0qrXnXbUR2rKinQUXE3b4auf5XysQauFlSsN1243OxWRS1yoRDtPDE7VyVPP3PJ3F_kbkavsZU50iDhiRbUQxXdJhfX6wTeqQEbEhXRnb_Go7cW1MxGDOypiPTHdO_SPUV0fopZk3Y16yhk0iHijPRJl-KHZFQAyZxZO3QI7E3V5Jt8BY23XL5ro1Bmlfoe2ytYw3Hec8LVO4RkL1wCAF5yPAIPLJHh-oEXsKym2VT0f1rNvJbsTLTMIp1xJqP6wUXHFQoeKDQUORvA4CqJ4SmBUBniBKzwXMX0Mj7USKZUB9LdJlP6spiTrQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‌
🔴
سخنگوی نیروهای مسلح یمن: چندین نقطهٔ حساس در مسیر تأمین و انتقال نفت خام از شرق عربستان به «ینبع»، با چند فروند پهپاد هدف قرار گرفت
🔹
این اقدام در پاسخ به نقض حریم هوایی یمن توسط پهپادهای دشمن سعودی انجام شد. @Farsna</div>
<div class="tg-footer">👁️ 9.6K · <a href="https://t.me/farsna/452940" target="_blank">📅 16:43 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452939">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/j00lDS53Nyinwvz8u7gWDTpQpLoWio5e4R86WSjzCNvbtfOpq2DI6yn_lvXNNVO0F7OLm4GRce0R692aqv5mbGCoItFatY2e8ci6KdcoXcTngV-7N00u8BNosNO1e1hUyDAzvqc47qvOMeThDxLCTpMDi3_dAIzk6FtwV78VrkU3NDqDWiAIxVL_Q8-P0Ma2eRjWLZdU_E-qS_GxMphH_HvTG7f5ISGH2vabbeq0zNQB_OnGnvhwNNgVbMxmflMkAjXCq9B6-DRGmmDHGpDQvP4DUJ80Tf6JV3fAtNXLJM2jfQuJSIMfNRIlQ3JaoL81jK5jzOH1nWqSHK-1dm5GZg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">راوی اربعین باش
🔹
این روزها میلیون‌ها عاشق، راهی سفر‌ند و هرکدام، روایت خودشان را از این مسیر دارند.
🔹
اگر شما هم امسال زائر اربعین هستید، عکس‌ها و روایت سفرتان را با ما و دیگر کاربران به اشتراک بگذارید.
🔹
مطالب خود را با هشتگ
#اربعین_۱۴۰۵
در سامانۀ فارس تعاملی منتشر یا از طریق پیام‌رسان‌ها به نشانی‌های
@Interactive_Fars
و
@fars_ma
ارسال کنید.
🔹
به برگزیدگان نیز هدایایی به رسم قدردانی‌ اهدا‌می‌شود.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.11K · <a href="https://t.me/farsna/452939" target="_blank">📅 16:42 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452938">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/390cba696e.mp4?token=B9s92zCcktCxGWBGrFLKlGCQ_urADJntO4Kpq3QgBBPoe2qgfkD_Vc8Kcf2_2jUspxT7ciGedaB_h4_5NGWevCLCr7r2ThBEZK6jKu7w19ZPfVKZHnWpVBS48yJNy5HglBMFGMc7PIxBp66mtD0OjAhL6XzWSWWi2t01AJ5s0NrHgcRkmWzV2VvrCeCcyB-_WQoE73YgG6taHd4UHyebyVv5FW7Zgq8lIpQQjpDtZmsS1eGbiBjktoToFuH6iaQ6hiOHLpHTe8hSrvAcQS3PXuKHzSpWvaK-L3W0G0iUR4euG__-CapfM-kAomC8Tv3UxKKoX41meHr9VP3xuyjfug" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/390cba696e.mp4?token=B9s92zCcktCxGWBGrFLKlGCQ_urADJntO4Kpq3QgBBPoe2qgfkD_Vc8Kcf2_2jUspxT7ciGedaB_h4_5NGWevCLCr7r2ThBEZK6jKu7w19ZPfVKZHnWpVBS48yJNy5HglBMFGMc7PIxBp66mtD0OjAhL6XzWSWWi2t01AJ5s0NrHgcRkmWzV2VvrCeCcyB-_WQoE73YgG6taHd4UHyebyVv5FW7Zgq8lIpQQjpDtZmsS1eGbiBjktoToFuH6iaQ6hiOHLpHTe8hSrvAcQS3PXuKHzSpWvaK-L3W0G0iUR4euG__-CapfM-kAomC8Tv3UxKKoX41meHr9VP3xuyjfug" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
مردم عراق! ما این اتفاق را فراموش نمی‌کنیم
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.96K · <a href="https://t.me/farsna/452938" target="_blank">📅 16:40 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452936">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b8eae8240a.mp4?token=Zb0y05SYg19IQLtKbvWiiRI5TlCGfDnxOiIIRi9v9aU3en4VzaZhFc_YkE980wWsZNJe2WlvIygHNeujDw5US2a9uqN5Lfo23dpF6BOcw6RIw3OErYNOrif9Xx4Ae_WvHWkjRxj0K3itWcIQkDGZWR9LShnExTvrYMMeMkkPseUMTlbbLXK57rHUdvb9lEUI-7XuaiK3v9nwS2Z7Hs3IdQ5q5z213_9SpxSY4Wyg6Hyg3Qc9CFvsMo1lpeybIcsA5FBz8EYT5V3DNJPQhRs8Owwdk7eCWnRCJfilO1mMY8_YzbflSD7c4KvL-RCvNxhnuoodfrK5TbAgzMbi8jx7EA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b8eae8240a.mp4?token=Zb0y05SYg19IQLtKbvWiiRI5TlCGfDnxOiIIRi9v9aU3en4VzaZhFc_YkE980wWsZNJe2WlvIygHNeujDw5US2a9uqN5Lfo23dpF6BOcw6RIw3OErYNOrif9Xx4Ae_WvHWkjRxj0K3itWcIQkDGZWR9LShnExTvrYMMeMkkPseUMTlbbLXK57rHUdvb9lEUI-7XuaiK3v9nwS2Z7Hs3IdQ5q5z213_9SpxSY4Wyg6Hyg3Qc9CFvsMo1lpeybIcsA5FBz8EYT5V3DNJPQhRs8Owwdk7eCWnRCJfilO1mMY8_YzbflSD7c4KvL-RCvNxhnuoodfrK5TbAgzMbi8jx7EA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
مسیرهای جایگزین پل‌های آسیب‌دیدۀ هرمزگان آسفالت شد
🔹
این پل‌ها در حملات آمریکا آسیب دیده‌اند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.12K · <a href="https://t.me/farsna/452936" target="_blank">📅 16:28 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452935">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">‌
🔴
وزارت دفاع عربستان: چند پهپاد از سمت عراق وارد آسمان کشور شد.  @Farsna</div>
<div class="tg-footer">👁️ 9.15K · <a href="https://t.me/farsna/452935" target="_blank">📅 16:27 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452934">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/p_GkOEtOxEPkJDSLaN9rxAYauv0wMeedx3dIu_mtX_2vKcFOEspqmNJEczEHhPnK9yXHQMQT1dlzWIDinoT8X7zbcpVTtOxuccy8jZ7qzfdCyoggkXkyEuKP1-YtbrmdYv_3_TJ72qN_tXvxsNbKxo1xNgy54V-QL0khLgfayoDWHuLPLopzuZDAIu7VK1E5ZC34442f5CE2DAlGjyEqusWwcJLMAuo3LSxO3WZIjLzRS1IYyfdopkd_BZllbaHpt7T4WvP4WXjRPTITT6NCnJwe2PaiMPqzBM7hdomep9ANCyqblIlAK4YIWBE7sR681Jb5iO590UEA3UxljxaHnw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مطالبات معوق کالابرگ، سرمایه فروشندگان را قفل کرد
🔹
طرح کالابرگ الکترونیکی که با هدف حمایت از معیشت خانوارها اجرا شد، حالا برای برخی فروشندگان به دغدغه‌ای جدی تبدیل شده است.
🔹
مغازه‌دارانی که کالاهای اساسی را در اختیار مردم قرار داده‌اند، اما به دلیل تأخیر…</div>
<div class="tg-footer">👁️ 9.18K · <a href="https://t.me/farsna/452934" target="_blank">📅 16:24 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452933">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oHn4Hmdxr4JNfQKPL7RZHbTFvT53DDF--zOWLho43-iO67QKw2oxBpNjhLa9SIfTNX65PQFeLxJEoaElYe9ntiLSaI4TaE6oxCy3dRVLaTepKdZjts1x6i200GnsYi6F6y89DrKn6STS7a4fyHip1-3sKP7ycKTrUQh6ox_p3tM43KUuBW2o5BJ18oYDX3T9lmRgGZh_Ilu9d6PyPswFZ_nRjJboVjXl1Ek25DIc2uQBIqBPCfmPnR20z_psQLGt8l_N_vO0YIYPnsnrhqI5O_2NmvYOBa5MzLbZ5f2QaBo5lmzWks-h7-LHI9kBqLr40mh9nHz0H1lnEMpetFkSpg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اعزام ۱۸ هزار زائر مناطق کم‌برخوردار به اربعین
🔹
رئیس ستاد اجرایی فرمان امام از حمایت این ستاد برای اعزام ۱۸ هزار زائر مناطق کم‌برخوردار به اربعین ۱۴۰۵ خبر داد.
🔹
سید پرویز فتاح گفت برای خدمت‌رسانی به زائران، امکانات لازم برای طبخ ۲ میلیون پرس غذای گرم، توزیع ۱۲ میلیون بطری آب معدنی و تولید روزانه ۴۰ هزار قالب یخ در مرزهای اربعین فراهم شده است.
🔹
او افزود بیمارستان سیار ۹۲ تخت‌خوابی در مسیر نجف به کربلا، بیمارستان ۴۰ تخت‌خوابی در مرز مهران و درمانگاه ۲۰ تخت‌خوابی در مرز شلمچه به زائران خدمات درمانی ارائه می‌کنند.
🔹
فتاح همچنین از ارائه مشاوره رایگان از طریق سامانه ۴۰۳۰ و اجرای پروژه‌های عمرانی و توسعه زیرساخت‌ها در مرزهای مهران، خسروی و شلمچه برای تسهیل تردد زائران خبر داد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.62K · <a href="https://t.me/farsna/452933" target="_blank">📅 16:22 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452932">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nYx5P8r9fkWE0MMVdxwrdkbYecC0PTENLnzuJNXCyhqQTZiJupO0rsgcVzkHqBKB8QsMC_O4xeHCv54fV-ZQEjxXu7gY_UNUXY6Uh_WFjaw0jDs0LzqFk37-Y3kQTQFvpfxPwz_r30ZrobZcSG20Xp6FNaVwXUfHSbwPnQC6yhUnecS5vFfIzD1jIp6hEFIhmEnXNw3AGqgLpLlQBWO87Kmv7qiCjc6FiF1W-BddlpDrQJ9XoKfXKTfdi4xZ0NOQ2z7Bo6bfo_B33WTKMpTsZRQJ5yY-9uZCmKY3985paguOf2eKhFb1-j_YV279TzM6WlfKKvx6tBFH-svyIWMKvA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">لیگ برتر ۱۸ تیمی شد
🔹
در جلسۀ امروز هیئت‌رئیسۀ فدراسیون فوتبال تصمیم گرفته شد با نیمه‌تمام اعلام‌کردن لیگ برتر و عدم معرفی قهرمان این فصل، سال آینده مسابقات به‌صورت ۱۸ تیمی برگزار شود.
🔹
دو تیم نخست لیگ دسته اول به‌صورت مستقیم راهی لیگ برتر خواهند شد و تیم…</div>
<div class="tg-footer">👁️ 9.17K · <a href="https://t.me/farsna/452932" target="_blank">📅 16:04 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452931">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromسیاسی خبرگزاری فارس</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/33c37b1d5a.mp4?token=uuV8bmla3tIPruyBnS-9jEdOyvMNGKSmZ-RXUrVkHgQalUZ9pmebTCIz_xe3eOqluUSPj4ttowdrWKJdz-xzghRpROx_oKWyZ2nFGDEZxK9IgzvibyxLFS5kQBn0vysAf60wKMPYOFKi_8_lkxQP6mBMABI9OqhstwJKlldXUO8MMMwkU543shdGhD_7GngbTU6nK5lqFRKy0LPRw__bjsxIko6kI94vKWfxfMw7DcOY_lUSaDSCq-cBJJi8vHmE3shemljOPgjI-CME9NLS1H1Sd7im61GqNQDryYkW-L82U7Dc2WCPR43hh6xZz9RGk24THUqn5JRrj3l-LdkS0aNOqd9DwULxAy6xWQ7V4qTUMyZeyTBG041H_9Dvwnl5AHU3XVsfroZxBEdstrAP6tbsu6MKDyXS_XvEEdTajlTdHvIW7B3tjNdCIpUX9F849gW-qG5Uf7EMlEraejdXWtolDzVYZFPg-I7xdz-pQ39tPuljYjvsPaj8HkZLlMz_Ir3_w0O0K5pLyA_2M-08sdeIQJ3uprLYfM03yF7k5m8ScHWVkJkzP4vzOntCnZaMIZAD4GhROPQMEVDpENJWWKkoRWJ8m2XWFeNTE6x6jLq4vM7chTVCWxFEhDcVYqDGW7rwoNyVcVZrZ-0PG2f4Wwec0A2LeTFiQx3wWUOm1GE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/33c37b1d5a.mp4?token=uuV8bmla3tIPruyBnS-9jEdOyvMNGKSmZ-RXUrVkHgQalUZ9pmebTCIz_xe3eOqluUSPj4ttowdrWKJdz-xzghRpROx_oKWyZ2nFGDEZxK9IgzvibyxLFS5kQBn0vysAf60wKMPYOFKi_8_lkxQP6mBMABI9OqhstwJKlldXUO8MMMwkU543shdGhD_7GngbTU6nK5lqFRKy0LPRw__bjsxIko6kI94vKWfxfMw7DcOY_lUSaDSCq-cBJJi8vHmE3shemljOPgjI-CME9NLS1H1Sd7im61GqNQDryYkW-L82U7Dc2WCPR43hh6xZz9RGk24THUqn5JRrj3l-LdkS0aNOqd9DwULxAy6xWQ7V4qTUMyZeyTBG041H_9Dvwnl5AHU3XVsfroZxBEdstrAP6tbsu6MKDyXS_XvEEdTajlTdHvIW7B3tjNdCIpUX9F849gW-qG5Uf7EMlEraejdXWtolDzVYZFPg-I7xdz-pQ39tPuljYjvsPaj8HkZLlMz_Ir3_w0O0K5pLyA_2M-08sdeIQJ3uprLYfM03yF7k5m8ScHWVkJkzP4vzOntCnZaMIZAD4GhROPQMEVDpENJWWKkoRWJ8m2XWFeNTE6x6jLq4vM7chTVCWxFEhDcVYqDGW7rwoNyVcVZrZ-0PG2f4Wwec0A2LeTFiQx3wWUOm1GE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
مقدم‌فر: دشمن امروز بر ایجاد اختلاف و ناامیدی متمرکز شده است
🔹
مشاور فرمانده کل سپاه: امروز اختلاف‌افکنی، تکنیک دشمن است. دشمن به این نتیجه رسیده که با کار نظامی نمی‌تواند حریف جمهوری اسلامی شود. آن‌ها در دو جنگ شکست خورده‌اند و به این جمع‌بندی رسیده‌اند که باید از داخل ما را شکست دهند؛ از طریق ایجاد اختلاف، بی‌اعتمادی به مسئولان و ناامیدسازی مردم، این‌ها همان عواملی است که انسجام ما را به هم می‌زند.
@Farspolitics
-
Link</div>
<div class="tg-footer">👁️ 8.89K · <a href="https://t.me/farsna/452931" target="_blank">📅 15:59 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452930">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cb30eccc7e.mp4?token=eWKCM5GONfRkmVSjilIa1MK0sH67MO-NgMp8fn3PAQcdGoOMzb2hDCM-R4xnBS7qkPvFFuJvCVcGQMp7AVYAvLObqmjvZX7H4tI4Wvv7l_7rpI7EmzeUIUwSonjuL6W9BkcjN7pkeUhN5hQOj0_97YU2E2TZLK29gGK-dYsOokdZDm3Bhn2fXdJXW8YqH-b_YwfVHNz7uXdUQ2ZucA3ahUX42AdAiPqiH7q29Fu-HaZOJNfe8qgI0QHKXh9Rrvk2rSn0KcOgNmf2u60h60aefzYlr3jnovulJZeo6ZKIPMzuOe_T1lcv-P9hOz5MUR-itzTJyNOMqE6ckLikIxJ9mA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cb30eccc7e.mp4?token=eWKCM5GONfRkmVSjilIa1MK0sH67MO-NgMp8fn3PAQcdGoOMzb2hDCM-R4xnBS7qkPvFFuJvCVcGQMp7AVYAvLObqmjvZX7H4tI4Wvv7l_7rpI7EmzeUIUwSonjuL6W9BkcjN7pkeUhN5hQOj0_97YU2E2TZLK29gGK-dYsOokdZDm3Bhn2fXdJXW8YqH-b_YwfVHNz7uXdUQ2ZucA3ahUX42AdAiPqiH7q29Fu-HaZOJNfe8qgI0QHKXh9Rrvk2rSn0KcOgNmf2u60h60aefzYlr3jnovulJZeo6ZKIPMzuOe_T1lcv-P9hOz5MUR-itzTJyNOMqE6ckLikIxJ9mA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
صحبت‌های سیدمجید بنی‌فاطمه در حاشیۀ محرم‌شهر دربارۀ عشق اکبر عبدی به امام حسین(ع)
@Farsna</div>
<div class="tg-footer">👁️ 9.25K · <a href="https://t.me/farsna/452930" target="_blank">📅 15:55 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452929">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">🔴
منابع عربی از وقوع انفجارهایی در عربستان و هدف‌قرارگرفتن تاسیسات نفتی این کشور خبر می‌دهند.  @Farsna</div>
<div class="tg-footer">👁️ 9.59K · <a href="https://t.me/farsna/452929" target="_blank">📅 15:44 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452928">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">🔴
منابع عربی از وقوع انفجارهایی در عربستان و هدف‌قرارگرفتن تاسیسات نفتی این کشور خبر می‌دهند.
@Farsna</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/farsna/452928" target="_blank">📅 15:43 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452927">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b74255f8ed.mp4?token=meP5XYp8Ixcw1Yxno7TsfJCZUBI2ugm764zB4FNyuQKMuoBIKfpvbbmvPOI0vbvM-9H6-k26USU1fY2Kc-bV8kPB0L8NJO-2Ec4-RCnltr0tZ5ImWoFM-g32jT6jKw3IZ0NTZZTo9Aegdy9hAG_l33n8dMx9Zkp_Eq0-PBYs6W3WXdXMpw2JzKE7N5QCLazM_Q7H_pGmgMf35XWqizmrFWUYacu0tAfG-bqROPN1DBalXh1gY3Y40U7u-3XEAwM_ydXqNFUDkAl3Thxiigj1Y1BV0JLwweVx9HUifHs1UoH-QVH8TFbLQ8UWfJdtyI5Js2Qd_h1d0DeeNWud5U1sFg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b74255f8ed.mp4?token=meP5XYp8Ixcw1Yxno7TsfJCZUBI2ugm764zB4FNyuQKMuoBIKfpvbbmvPOI0vbvM-9H6-k26USU1fY2Kc-bV8kPB0L8NJO-2Ec4-RCnltr0tZ5ImWoFM-g32jT6jKw3IZ0NTZZTo9Aegdy9hAG_l33n8dMx9Zkp_Eq0-PBYs6W3WXdXMpw2JzKE7N5QCLazM_Q7H_pGmgMf35XWqizmrFWUYacu0tAfG-bqROPN1DBalXh1gY3Y40U7u-3XEAwM_ydXqNFUDkAl3Thxiigj1Y1BV0JLwweVx9HUifHs1UoH-QVH8TFbLQ8UWfJdtyI5Js2Qd_h1d0DeeNWud5U1sFg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
حجت‌الاسلام عابدینی در سمت خدا: اربعین دو بال دارد؛ محبت به امام حسین(ع) و بغض به دشمنان
🔹
در اربعین امسال، قرار است خون‌خواهی به عنوان بغض به ظلم و ظالم به اوج خود برسد.
@Farsna</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/farsna/452927" target="_blank">📅 15:42 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452926">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">📷
زائران اربعین، استوار در مسیر
🔹
باوجود افزایش دمای هوا در مرز شلمچه، موج حضور زائران اربعین همچنان ادامه دارد.  عکس: فرید حمودی @Farsna</div>
<div class="tg-footer">👁️ 9.24K · <a href="https://t.me/farsna/452926" target="_blank">📅 15:34 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452925">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dCIpknsggGHijmUQmGl9WY06yEIUV1AepOKq4xpZYkM82YR5M2ZX3oNldsiXfUkaIpMRu_d5YyX7_isJiqAwHIrPcdECAt01KXF-11-tgVcFeJbkbyrly8HQgZ2xkj_06DpcwL7lho6DhXS183Mn_x-z4jQlgJb0Hst-HGwpF8D5Y2nD68GeLHzmO5B6xwuReoTHgsQtfEipobtOPwO-0a1ldUDC8zCm5Kd0WOh_c723lAUhm30OUI0TyHmIctY6gt645MkupiBe2otpCAk5QVB-BWzhKBhUpW1UUfcn_cZ8QCjQbaZ44DUXFUXAM8vH0x5qSY8vAzmpLU8Hd5GDpg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کدام بسته ارتباطی اربعین برای شما مناسب‌تر است؟
با نزدیک شدن به اربعین، انتخاب بسته ارتباطی مناسب به یکی از دغدغه‌های زائران تبدیل شده، به‌ویژه برای کسانی که می‌خواهند در طول سفر بدون نگرانی از هزینه‌ها به اینترنت دسترسی داشته باشند یا با خانواده و همراهان خود تماس بگیرند.
مقایسه بسته‌های همراه اول و زین عراق نشان می‌دهد برای اغلب زائران ایرانی که به اینترنت، پیام‌رسان‌ها و خدمات آنلاین نیاز دارند، بسته‌های همراه اول انتخاب کاربردی‌تر و به‌صرفه‌تری است، درحالی‌که بسته‌های زین بیشتر برای تماس‌های محلی داخل عراق مناسب‌اند.
همراه اول بسته‌هایی با ترکیبی از اینترنت، مکالمه و پیامک ارائه کرده است. در میان این گزینه‌ها، بسته ۵ گیگابایت اینترنت با اعتبار ۱۴ روزه و قیمت ۸۰۰ هزار تومان، برای زائرانی که در طول سفر به اینترنت بیشتری نیاز دارند، انتخاب قابل‌توجهی است.
در مقابل، بسته‌های زین عراق تمرکز بیشتری بر مکالمه دارند. برای نمونه، بسته‌ای شامل ۱۰ دقیقه تماس بین‌الملل و ۳۰ دقیقه تماس درون‌شبکه‌ای زین، با قیمتی حدود ۶۶۵ هزار تومان عرضه شده است.
زائرانی که بیشتر از پیام‌رسان‌ها، مسیریاب‌ها و خدمات آنلاین استفاده می‌کنند، باید حجم اینترنت را در اولویت قرار دهند.</div>
<div class="tg-footer">👁️ 9.6K · <a href="https://t.me/farsna/452925" target="_blank">📅 15:31 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452924">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oeTsv3JEzOaFEH5gwNiRIR48x-T-HUYXxRYA1xa7xuq5h-lTCVU976A4eBVUcUiPZeupELnJ6b6gRiMe9kN_UbzEl1_MoyKcqPv0kAyvmJeVKYn59Y4yNyogzGBkiKzUJQb0YLID1KB3qqd2XfhNen2oeZEk0jD83fcCcIW5YZKMo_y_ENKrO0CN3L2ynaEpEWsPCEDjaahUbFJCkilFw_u-bDiON6FKx0Zux2j8E5tdoUP_0pHnfKKJZvYoxZulIUzLe7FEXD03HSbqkLlNEtxI2VaUgkgE1oEvDjSKNIFp5DTE22KfFU1a4XdRj5_9yEXp1gTEAPGzxw74cQJuFQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔹
خدمت رسانی شعب کشیک بانک کشاورزی در مناطق مرزی به زائران اربعین حسیني
🔻
به منظور رفاه حال زائران اربعین حسینی و سهولت دسترسی آنان به خدمات بانکی، شعب کشیک بانک کشاورزی در شهرهای مرزی غرب و جنوب غرب کشور از ساعت ۰۷:۰۰ تا ۱۹:۰۰ دایر و آماده خدمت رسانی خواهند بود.
🔻
شعب کشیک در استان های آذربایجان غربی، کردستان، کرمانشاه، ایلام و خوزستان تا ۱۵ مردادماه از ابتدای وقت اداری تا ساعت ۱۹:۰۰ به صورت مستمر آماده خدمات رسانی به زائران و مراجعین خواهند بود.
اسامی شعب کشیک بانک کشاورزی در مناطق مرزی در روزهای ۵ تا ۱۵ مرداد ماه
🔗
مشروح خبر</div>
<div class="tg-footer">👁️ 8.45K · <a href="https://t.me/farsna/452924" target="_blank">📅 15:30 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452923">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-footer">👁️ 8.38K · <a href="https://t.me/farsna/452923" target="_blank">📅 15:29 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452922">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IP_bqZIKg01MTa5amaXqcqr7dwQguNXSc64u7Qi3Ou9ICPSx9VuB5LXa9L6qz1CuNt431DnYkSse2G39Emsu-R9jIT41G-o6S7AbjL_V-bJG-GjPBv7iDDXY_qVjX-yu9CbV9lmVXp8Eb-M7AMxOelqRHeDEO6ZBgpZDHnX-x0MNjMRNb8x4hWKldrXFNRBDDwXVYyrpObpfbT772l3Yk3tPN2nj4eSZ9uRJBnWUsEGBIB9J6YDYIjYTQwMkEmUpziJp4-rFg9d8sOS4vVgJFd7w3JaGusALUtWNffr5vf7c6hzeoNJOR1jKGNI6EThaB9Wib9O608gzP8yptj9z7Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎥
قلعه‌نویی: بی‌وطن‌های ایران‌فروش گفته‌اند که خوب شد تیم ملی صعود نکرد وگرنه ما بیچاره می‌شدیم.  @Farsna</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/farsna/452922" target="_blank">📅 15:26 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452921">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9419b58485.mp4?token=nNRhWKBF5Vf1MGLFs-Ypu84-sazc7rYAVVjiFPHWCpTbKfY0WhwpEwKf4Q_ABqNXQR9mGIpXV37bUbDLUi5xBYd7kHlwIIS-_JK0quezCulFsujlN2_VVe64utvjavEOlraMstHdRFDAFV-dd6RxcJk0BtI6IBVftdt6kGBQxFAYLuVmlo8tpAU4so6Q98FacTHiFgH_YbgIcYNVgksitHq6JDrArYxDrDJvsg7ViSZNNQm97iYa2HmAKTqWRYqaRc11AnB7CeSzl8JiF9LFk5hzGVYD3dLUGpJ0_QFyeyHp62IAzk4NNkfAcot7iWrUUatOTjnIVj2uYGTcV33emQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9419b58485.mp4?token=nNRhWKBF5Vf1MGLFs-Ypu84-sazc7rYAVVjiFPHWCpTbKfY0WhwpEwKf4Q_ABqNXQR9mGIpXV37bUbDLUi5xBYd7kHlwIIS-_JK0quezCulFsujlN2_VVe64utvjavEOlraMstHdRFDAFV-dd6RxcJk0BtI6IBVftdt6kGBQxFAYLuVmlo8tpAU4so6Q98FacTHiFgH_YbgIcYNVgksitHq6JDrArYxDrDJvsg7ViSZNNQm97iYa2HmAKTqWRYqaRc11AnB7CeSzl8JiF9LFk5hzGVYD3dLUGpJ0_QFyeyHp62IAzk4NNkfAcot7iWrUUatOTjnIVj2uYGTcV33emQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">آرامکو همچنان در آتش می‌سوزد
🔹
تصاویر ماهواره‌ای نشان می‌دهد که تاسیسات پالایشگاه جازان آرامکو که ۹۹ درصد ذخایر نفت خام عربستان را در خود جای داده، پس‌از حملات یمن همچنان در آتش می‌سوزد؛ احتمالا این دود عظیم ناشی‌از آتش‌سوزی یک مخزن ذخیرهٔ نفت خام است. @Farsna…</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/farsna/452921" target="_blank">📅 15:12 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452920">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">فرمانداری بندرلنگه: صدای انفجارهای امروز ناشی‌از خنثی‌سازی مهمات است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/farsna/452920" target="_blank">📅 14:50 · 05 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>

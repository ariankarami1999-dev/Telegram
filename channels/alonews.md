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
<img src="https://cdn4.telesco.pe/file/jzgVPbyU1DDeXZwZWIyF5-IMwSOTVweNrNxilHDNV0X7BZijn-0TFUQIkPDeuaBbrfth20WjyxhxfYv7gY7r3DvzPG3YhrzvsPvtQEzSGnUmBYw3Gw2-oPu10ETEGq0FGMJFFwPJbTmmDDUO5493H0sKSBgg50J5SI880HlQhCBST8Dci3vC-CcEWaHdKjQ73R946UNXs0JTlS7dGw0SUHl9wusA-nBxnCzPOXeRUtPy-0G6FuIvYZBFD4SvQfpS3lCEcskI_420-4oIJRNvTZqZeUa77cKrHmsq3-0uPEo70p5-_hOcmKJMhA5ET3f1mbpwF3lOp5VpvMFQY3FG8Q.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 اخبار جنگ الونیوز AloNews</h1>
<p>@alonews • 👥 992K عضو</p>
<a href="https://t.me/alonews" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 با الونیوز از اخبار جنگ و وقایع در چند ثانیه مطلع باش!اخبار جنگ بدون سانسور در الونیوز👌جهت رزرو تبلیغات👇https://t.me/ads_alonewsپشتیبانی کانال🕵️https://t.me/AloNews?directمالک کانال🎩@AloNewsBotX:https://x.com/AloNewsBot</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-09 22:19:56</div>
<hr>

<div class="tg-post" id="msg-138992">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">👈
خبرنگار العربیه: اسرائیل برای ساکنان منطقه غربی اردوگاه النصیرات در مرکز نوار غزه دستور تخلیه صادر کرد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 12 · <a href="https://t.me/alonews/138992" target="_blank">📅 22:19 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138991">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">👈
واشنگتن‌پست: ترامپ نباید در مورد ایران به توصیه‌های جی‌دی ونس گوش بده
✅
@AloNews</div>
<div class="tg-footer">👁️ 5.1K · <a href="https://t.me/alonews/138991" target="_blank">📅 22:16 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138990">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/27404f83be.mp4?token=Mk-mQNms0woMkoZHu09LcdEx6DD1bAJjrSPLu-Jw3TCR9Kug102TfoImyaZ3PC26gQEx4p72SQjS1XiE4Y6Rj34QE5f4sJM4S6WcOwDlEMU2Cfe8PHfYwMrSPU9hyqe2qNHHTZeKh63_7VM4IPo9KKn064_0f5z6g0AGht4pVA7O7uGg-Yl05cZN1yIpwgfzKabXt399rwpPpL9mhCUEALJrg1tA-FGZWJszQ0P189TXMoAEzg7gVRMsYEmJcDD3H4Wt2FrhHBOCpUvDAvKk4Wd4LHBU6yW_aRU5AEov0EOVr9ozCIuPhfYNlch4p9ZgAnqkto09slUiXnBYFHA5Ww" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/27404f83be.mp4?token=Mk-mQNms0woMkoZHu09LcdEx6DD1bAJjrSPLu-Jw3TCR9Kug102TfoImyaZ3PC26gQEx4p72SQjS1XiE4Y6Rj34QE5f4sJM4S6WcOwDlEMU2Cfe8PHfYwMrSPU9hyqe2qNHHTZeKh63_7VM4IPo9KKn064_0f5z6g0AGht4pVA7O7uGg-Yl05cZN1yIpwgfzKabXt399rwpPpL9mhCUEALJrg1tA-FGZWJszQ0P189TXMoAEzg7gVRMsYEmJcDD3H4Wt2FrhHBOCpUvDAvKk4Wd4LHBU6yW_aRU5AEov0EOVr9ozCIuPhfYNlch4p9ZgAnqkto09slUiXnBYFHA5Ww" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
رئیس پژوهشگاه رویان: سال گذشته یک زوج می‌توانست به طور متوسط با ۱۳ یا ۱۴ میلیون صاحب فرزند شود اما امروز ما می‌بینیم درمان به‌خاطر بالا رفتن هزینه داروها و خدمات، نزدیک ۴۰ تا ۵۰ میلیون تومان هزینه ممکن است داشته باشد
✅
@AloNews</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/alonews/138990" target="_blank">📅 22:07 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138989">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">👈
قیمت نفت خام آمریکا در معاملات آتی با ۱.۲۹ درصد افزایش به ۸۴.۶۷ دلار در هر بشکه رسید
✅
@AloNews</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/alonews/138989" target="_blank">📅 22:05 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138988">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4a48f675ec.mp4?token=vD3gPuh-okqmXi4HHNvbKSSDxDN9joWmYvy0l0c7tsEc_MjYp5BlIXZN6oYNF6aXhVMzpLlRbZchvUf5VUGpvnAJB-7yMO2zCsy4yRSSx34T_7NyGnjaIRDkiHTHUZxR9eYIOitEJSSp9v2fcoJMX8NITHDVjd06J6oAqq-fKcNAJ9a1jELd465JcK0PG1R3Ay_LuTqIabCvU7_Sp1Yems5TwN5q3SU2Jok9q0VR1uAiLuKWOYj-v0AHBDypIosOKRnkGYUEVpMtBu-uXVDRX8PGPN6hSTXiqZIjUpCRj7hsorBgwiYjZkZAlOhQE2L8eP1XzONGZKGM21cQmXOPhQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4a48f675ec.mp4?token=vD3gPuh-okqmXi4HHNvbKSSDxDN9joWmYvy0l0c7tsEc_MjYp5BlIXZN6oYNF6aXhVMzpLlRbZchvUf5VUGpvnAJB-7yMO2zCsy4yRSSx34T_7NyGnjaIRDkiHTHUZxR9eYIOitEJSSp9v2fcoJMX8NITHDVjd06J6oAqq-fKcNAJ9a1jELd465JcK0PG1R3Ay_LuTqIabCvU7_Sp1Yems5TwN5q3SU2Jok9q0VR1uAiLuKWOYj-v0AHBDypIosOKRnkGYUEVpMtBu-uXVDRX8PGPN6hSTXiqZIjUpCRj7hsorBgwiYjZkZAlOhQE2L8eP1XzONGZKGM21cQmXOPhQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
مراکشی ها  در اسپانیا مشغول غارت
✅
@AloNews</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/alonews/138988" target="_blank">📅 21:58 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138987">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f1d64e33bb.mp4?token=qgKVphvMute9IZbJcgTJdnyj7LQ1fwPNT4ueWnaRGBmJDk3k6AK6mQKp6vr6ZhtLYfaErDeO8c96p6ie2nEQnV7QI-VXtQIRsVPFnM2y5Pxk1CsrUXdcjNxuJr9u5XVEsAgjJXkpQHuivNy7pfJFnGqlMTQ2FOFKI0mNr38lDK4kgDKxk4Se_T-aiB-IsHb0viySy9w0T1OupyCsMa8-f-tILA0y2IM7grxyG_zlYUOIbKJDVcE48cwQ56nnTtAGjmssqQrtvShEwU-JIKpaT2KJL4tPGnxFggA2v13F6znynJjQdNO01n92K1YFVvUE-MmzNaa8CFaSybSQxHGvYg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f1d64e33bb.mp4?token=qgKVphvMute9IZbJcgTJdnyj7LQ1fwPNT4ueWnaRGBmJDk3k6AK6mQKp6vr6ZhtLYfaErDeO8c96p6ie2nEQnV7QI-VXtQIRsVPFnM2y5Pxk1CsrUXdcjNxuJr9u5XVEsAgjJXkpQHuivNy7pfJFnGqlMTQ2FOFKI0mNr38lDK4kgDKxk4Se_T-aiB-IsHb0viySy9w0T1OupyCsMa8-f-tILA0y2IM7grxyG_zlYUOIbKJDVcE48cwQ56nnTtAGjmssqQrtvShEwU-JIKpaT2KJL4tPGnxFggA2v13F6znynJjQdNO01n92K1YFVvUE-MmzNaa8CFaSybSQxHGvYg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
لیونل مسی: همسرم اجازه نمی‌دهد در خانه با پسرهایم فوتبال بازی کنم!
✅
@AloNews</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/alonews/138987" target="_blank">📅 21:57 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138986">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f0eba69de3.mp4?token=EJRHVxeqbzTJEVYyynK-4de3ZZbaVK3fSODHzh5_wRDyxIsKOJaCVEOZF58ZAP-HhvWc_r9rM-RbXx8V8uFD3jpelOs6mwhiCuXfPrx5sfTZERMsJxyvIM6O9axMk0T9Wm6VNW6l6BmFc1y-GxBOizdFw1tVr5U0NC4S3GJx2WeKtXdac7TgijXBcPQWCe6ezCZax8HKObNoM7KQfKdDzwlMFoCBcWcIDIrHuOhIdp8k4bCZgFa5OGoZlq6ye8o6a06E5jTWm0-q5ebudiWA9zFVKcxfkfogJC38AZlE3hbr5Ukre-0aLyb4Xc8VLw-yonZIG3uGLIABWlxTEdsPbQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f0eba69de3.mp4?token=EJRHVxeqbzTJEVYyynK-4de3ZZbaVK3fSODHzh5_wRDyxIsKOJaCVEOZF58ZAP-HhvWc_r9rM-RbXx8V8uFD3jpelOs6mwhiCuXfPrx5sfTZERMsJxyvIM6O9axMk0T9Wm6VNW6l6BmFc1y-GxBOizdFw1tVr5U0NC4S3GJx2WeKtXdac7TgijXBcPQWCe6ezCZax8HKObNoM7KQfKdDzwlMFoCBcWcIDIrHuOhIdp8k4bCZgFa5OGoZlq6ye8o6a06E5jTWm0-q5ebudiWA9zFVKcxfkfogJC38AZlE3hbr5Ukre-0aLyb4Xc8VLw-yonZIG3uGLIABWlxTEdsPbQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
احمد ایراندوست(بازیگر) فیلم رقصیدنش با آهنگ جمال جمالو رو پست کرده و تو کپشن نوشته تقدیم به روح اکبر عبدی.
✅
@AloNews</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/alonews/138986" target="_blank">📅 21:54 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138985">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/84ef9957d8.mp4?token=YpUxupHXde9w_awG5LiVlyBkLTR2cKL9OE8pU8xdJvSoyyq574P96TTnusdiGtJuQDbb_vo5oWk4Spa97894PEwNWTzySeEsa_yY-NyI1a_7n36Noryxyez1u2POSP4T5xCUmzYc63VDaQ0vIvoF4aXW2E2Xw2efdJKxkz6ia3b_C_TiO8n2G2jvYbjiLBCLsVsTVzpi4Qz2V_XsKVd7BG7VU9xq7mXnxQVHqsLdoHmo1G9KRSbeTipmGCeMH7XiYjtP1kO01LJx-2kmlu-E3KTB8PMP-LjYNQQFEM479zMwadXLGie_LLI-M0Rh0sr1ap6ixrzkDGiQiY0_rFvDFg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/84ef9957d8.mp4?token=YpUxupHXde9w_awG5LiVlyBkLTR2cKL9OE8pU8xdJvSoyyq574P96TTnusdiGtJuQDbb_vo5oWk4Spa97894PEwNWTzySeEsa_yY-NyI1a_7n36Noryxyez1u2POSP4T5xCUmzYc63VDaQ0vIvoF4aXW2E2Xw2efdJKxkz6ia3b_C_TiO8n2G2jvYbjiLBCLsVsTVzpi4Qz2V_XsKVd7BG7VU9xq7mXnxQVHqsLdoHmo1G9KRSbeTipmGCeMH7XiYjtP1kO01LJx-2kmlu-E3KTB8PMP-LjYNQQFEM479zMwadXLGie_LLI-M0Rh0sr1ap6ixrzkDGiQiY0_rFvDFg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
کامالا هریس درباره ایران: حتی اگر کنگره با آن موافقت می‌کرد، من با جنگ مخالفت می‌کردم
✅
@AloNews</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/alonews/138985" target="_blank">📅 21:52 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138984">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">👈
ویدیوی یک ساعته کل نشست پرزیدنت ترامپ با کابینه خود با زیرنویس فارسی
✅
@AloNews</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/alonews/138984" target="_blank">📅 21:51 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138983">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">👈
رئیس جمهور اوکراین: اوضاع در خط مقدم جنگ دشوار است
✅
@AloNews</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/alonews/138983" target="_blank">📅 21:49 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138982">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">👈
ترامپ: شیوه مذاکره ایرانی‌ها مرا خشمگین می‌کند؛ آن‌ها هفت ساعت را صرف موضوعی می‌کنند که می‌توانند در ۱۰ دقیقه انجام دهند
✅
@AloNews</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/alonews/138982" target="_blank">📅 21:48 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138981">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">👈
حاکم بحرین خطاب به ایران : حضرت محمد پس از قرن ها تاریکی در ایران به آن عمق روحی، انسانی و معرفتی بخشید، بخاطر تشکر از این کار حداقل دیگه به بحرین حمله نکنید
✅
@AloNews</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/alonews/138981" target="_blank">📅 21:47 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138980">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">🔴
این شهروند عزیز حرف دل میلیون ها ایرانی رو زده
🤔
تنها راه نجات ایران از دست این رژیم فاسد فقط اتحاده
✅
@AloNews</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/alonews/138980" target="_blank">📅 21:46 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138979">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">👈
شهردار مسکو: یک پهپاد که به سوی پایتخت در حال پرواز بود را سرنگون کردیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/alonews/138979" target="_blank">📅 21:41 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138978">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0047000034.mp4?token=jPb-raabRSLWi5XDL6ts8J5r5eskwrmGF8KVuPjAkYG9EFYK2krJsZYNHOpSjOJqDg6thq-BLPLpT3zK_7Pda4rqA05uSTmfANYQ6obLvbKpNH01ZDkJUQTaeKg4Fi4vha5uCHohpX1hZq72BXIzvai4kJYkYyjTdzEwd_qGStZlXbKBK4SU_pkPOudtcEmjPW9YtnHnqwGdDwuZGKjIgijqQqQggf30pQ6jvDWXE0FVZxM_SIPLXI8WwRarkC-19aeXZzb-2lY-MIqJkr4tB9wOVo5iv5abHJcHL-u3rwcaOJvC_krrSmBGGVRfLVKQVtcRii6E5BrBp3eF7Fb4AYY3erE4zIf26KIMSK81LrOYgqMlsTZNdMq5NSlwVNq0w_c_R3EKpcmlZnE7JLyXerqW-JE8HikYX6vrMUrCiu9NMq07kY_iUO2Whie8kgUbB1o4YT5ZvLYtIqSgNXPqZ-epaVRDRV9DzEHdTwqRc_iExQSR8JCcWX8AO2lvre7x73qy8GRBobkJwCUsUTf_gZzwvjlE7RDPtORGKjUyJ8REJIZSOWFr-m5djIUUol8P09bOB2pDAmqXe06GpXVmW6YnLdwrAX8j27FTy-Xzp21jWXiNmy6LU8XPyvKEGKXnHa4yAHAVMU8BzqVJP5htn2JwjYGAEB6tDqDsOPz7sI4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0047000034.mp4?token=jPb-raabRSLWi5XDL6ts8J5r5eskwrmGF8KVuPjAkYG9EFYK2krJsZYNHOpSjOJqDg6thq-BLPLpT3zK_7Pda4rqA05uSTmfANYQ6obLvbKpNH01ZDkJUQTaeKg4Fi4vha5uCHohpX1hZq72BXIzvai4kJYkYyjTdzEwd_qGStZlXbKBK4SU_pkPOudtcEmjPW9YtnHnqwGdDwuZGKjIgijqQqQggf30pQ6jvDWXE0FVZxM_SIPLXI8WwRarkC-19aeXZzb-2lY-MIqJkr4tB9wOVo5iv5abHJcHL-u3rwcaOJvC_krrSmBGGVRfLVKQVtcRii6E5BrBp3eF7Fb4AYY3erE4zIf26KIMSK81LrOYgqMlsTZNdMq5NSlwVNq0w_c_R3EKpcmlZnE7JLyXerqW-JE8HikYX6vrMUrCiu9NMq07kY_iUO2Whie8kgUbB1o4YT5ZvLYtIqSgNXPqZ-epaVRDRV9DzEHdTwqRc_iExQSR8JCcWX8AO2lvre7x73qy8GRBobkJwCUsUTf_gZzwvjlE7RDPtORGKjUyJ8REJIZSOWFr-m5djIUUol8P09bOB2pDAmqXe06GpXVmW6YnLdwrAX8j27FTy-Xzp21jWXiNmy6LU8XPyvKEGKXnHa4yAHAVMU8BzqVJP5htn2JwjYGAEB6tDqDsOPz7sI4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
یک جنگنده F35 در پایگاه نظامی کالیفرنیا آمریکا سقوط کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 30.6K · <a href="https://t.me/alonews/138978" target="_blank">📅 21:36 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138976">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/lmEn4RmWX8pguaUAY9FgnOCcUF_HHCrHPIsb7l5vseYbkfPwMElSVhwe93za95FqgFt1FLkBTpYrW3188agqdJWyb7cnr-7XpTwg33TMPfYt5yKfA1gD6Ahf6HUlC3WCV1gmk-b8u_5IYIITFBaMhK7FASkF0N0cmRF9Qtjr8P61z1l_NrlLOc-SxEu_lSy1VwQG1y5PuoOzAlelh66O6XIGpeSdArUJWRm9vGp_RIp2AtOqH6YI-Qu4sPl-M2exc7vWkuwGQQ2jzLxk6X4Imsgh-jILKEzHxQDbCAIiGw8uoQdv7ZDleixkcb-m-hqo87ZVvJshbeWq8--E51N8bw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/XWwo7nzsb-GyK5y5kYkisRNKGqkx_DwlGHUx6jnYd4JqIFPjvJciufbyzRqfyXgcgvC_Rn0GTn986cBKJYxNd7zfJIQtP7Ldx0m8nb8FEgEa5pGFjUIDC0ZS211H3eJGXUOlCYjLqmp8NpO8yU2NkHob8zHdTPEwKxSBPk-FA_xArNC5N-gzeAxLUb-RVOwJwyx4xQLDBd8LZKjgoWnXU23EgRDSAU7WwNS0lmR6c1DpiQS1z3x5eRQR6ThdbNkQuoDT9iOjaJpKlbfQ0r1o5cm_5NHmhqYCEJGOfakwDKXgXfqchfLA1VgB75aV5j3fg6L7BK3x62ioms0AODKxEA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
درگیری رسانه ایی سپاه و سنتکام
🔴
سنتکام: تنگه هرمز باز است
🔴
سپاه: تنگه هرمز بسته است
✅
@AloNews</div>
<div class="tg-footer">👁️ 31.6K · <a href="https://t.me/alonews/138976" target="_blank">📅 21:32 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138975">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">➕
حتما یک بار تست کنید تا سرعت و کیفیت رو متوجه بشید
✨
یکی از با کیفیت ترین و پایدار ترین اشتراک های بازار با قیمت خیلی مناسب حتما یک بار تست کنید
در هر صورت تمامی سرویس ها قابلیت مرجوعی دارن و هرموقع راضی نباشید میتونید مرجوع کنید
خرید فوری از ربات های زیر :
🤖
@Team_express_bot
🤖
@Team_express_bot</div>
<div class="tg-footer">👁️ 33.6K · <a href="https://t.me/alonews/138975" target="_blank">📅 21:27 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138974">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">فیلتر شکن v2ray اختصاصی
✅
اتصال پایدار و پرسرعت
✅
دارای ساب برای اطلاع لحظه ای از باقیمانده
✅
متصل در تمامی دستگاه ها و اینترنت ها
✅
مناسب استریم، بازی و استفاده روزمره
✅
پشتیبانی تا پایان سرویس
💬
تعرفه‌ها
🔸
پلن‌های یک‌ماهه
▫️
۱۰ گیگابایت — 39,000 تومان
▫️
۲۰ گیگابایت — 50,000 تومان
▫️
۴۰ گیگابایت — 95,000 تومان
▫️
۶۰ گیگابایت — 140,000 تومان
▫️
۸۰ گیگابایت — 185,000 تومان
▫️
۱۰۰ گیگابایت — 230,000 تومان
▫️
۱۵۰ گیگابایت — 340,000 تومان
▫️
۲۰۰ گیگابایت — 450,000 تومان
▫️
نامحدود (مصرف منصفانه ۳۰۰ گیگ) — 560,000 تومان
🔹
پلن‌های دوماهه
♦️
۳۰ گیگابایت — 95,000 تومان
♦️
۵۰ گیگابایت — 140,000 تومان
♦️
۷۰ گیگابایت — 185,000 تومان
♦️
۱۰۰ گیگابایت — 250,000 تومان
♦️
۱۵۰ گیگابایت — 365,000 تومان
♦️
۲۰۰ گیگابایت — 475,000 تومان
♦️
نامحدود (مصرف منصفانه ۴۰۰ گیگ) — 675,000 تومان
🔸
پلن‌های سه‌ماهه
▫️
۸۰ گیگابایت — 240,000 تومان
▫️
۱۰۰ گیگابایت — 275,000 تومان
▫️
۱۵۰ گیگابایت — 390,000 تومان
▫️
۲۰۰ گیگابایت — 500,000 تومان
▫️
۳۰۰ گیگابایت — 720,000 تومان
▫️
نامحدود (مصرف منصفانه ۵۰۰ گیگ) — 820,000 تومان
خرید فوری :
🤖
@Team_express_bot
🤝
فروش عمده و پنل نمایندگی:
📩
@expressuport
📢
کانال اطلاع‌رسانی:
🌱
@vpn_express_sup</div>
<div class="tg-footer">👁️ 32.6K · <a href="https://t.me/alonews/138974" target="_blank">📅 21:27 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138973">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e9d9e7e72d.mp4?token=fwlinUdCM4E87mfb2uw2cZJgsvndfjhpigtNURrQzGlYDix0X8D4tmVyQ1Jv3kdW6ZkcXlG80zcgxtrS0PtLBrTZbR0oVhUN2vJvr9holyFpK5C9q5kOn3Lk-sYWxQUEHrTWfIE1uTNIUPa7g6uSPmWmhhUs2rbwgwZjTcLbYCqOvW8x9M67MEbD-DNXdux6diXOhGdoXJryO9qRVHg94PYMASAUvt5G9G0T9p6sfpcVgzpZvDikxXwDI5LW2xrJelZcQH9RRRSgmRea-NKfQeNYNZogOMOPbJv3NSFjJZPvG7cBaGzhYH-jOC1dJKLPJ2n-BvuIVS7oC-vue9zsqQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e9d9e7e72d.mp4?token=fwlinUdCM4E87mfb2uw2cZJgsvndfjhpigtNURrQzGlYDix0X8D4tmVyQ1Jv3kdW6ZkcXlG80zcgxtrS0PtLBrTZbR0oVhUN2vJvr9holyFpK5C9q5kOn3Lk-sYWxQUEHrTWfIE1uTNIUPa7g6uSPmWmhhUs2rbwgwZjTcLbYCqOvW8x9M67MEbD-DNXdux6diXOhGdoXJryO9qRVHg94PYMASAUvt5G9G0T9p6sfpcVgzpZvDikxXwDI5LW2xrJelZcQH9RRRSgmRea-NKfQeNYNZogOMOPbJv3NSFjJZPvG7cBaGzhYH-jOC1dJKLPJ2n-BvuIVS7oC-vue9zsqQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
روسیه مواضع نظامی‌های اوکراینی رو با موشک‌های سنگین بمبارون کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 36.7K · <a href="https://t.me/alonews/138973" target="_blank">📅 21:14 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138972">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DOKnc69r0a-GQ589nR5AMygUoT_j8Tnp7xiW11cQr1wu25DKFQDu3UuSrIST1rJmfP-tn9J-kifA_xd6tysthhP8txYhLBli8yaHiBVcECtuvXjaynDQAZ3eSJe701HSVjOOd8btv7zaSXSZMz1QfMUmnMgtHsxQ09nTPPfQDtb60v0jV13ES19VXglFdoxQ43eqFj79lApEyNuLjKiIF7iYMXFvTsHL6OXwmD-vooDmCrJkIsrP982UwclAcTD07uqq79qcNzArH0OOQtcujBkLlGg31ew7oZ-Ipex9oYsaJtyMoVhVbOV8rufoKu3rEdn1XLW0P65W6jniLBwsDA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
سقوط بیت‌کوین به زیر ۶۳,۰۰۰ دلار در پی مداخله‌ی آمریکا در بازار ین
✅
@AloNews</div>
<div class="tg-footer">👁️ 39.8K · <a href="https://t.me/alonews/138972" target="_blank">📅 21:05 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138971">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">👈
اسپانیا: بیش از ۴۸ هزار مهاجر غیرقانونی به مراکش بازگردانده شدند
🔴
وزارت کشور اسپانیا اعلام کرد که تاکنون بیش از ۴۸۳۰۰ مهاجر غیرقانونی از شهر خودمختار سئوتا در اسپانیا به مراکش بازگردانده شده‌اند
✅
@AloNews</div>
<div class="tg-footer">👁️ 41.9K · <a href="https://t.me/alonews/138971" target="_blank">📅 20:55 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138970">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/h7i9izpgpHwiRjx-SiNAA0VL4sXJZWY87momA-hBWD4L_u1CHkxzYpZChiU1cqMUV0ZL6wKmMtm9D9WJFTPvuAoiBOh6HD_vShw3_Ne2oNvJcMcX_KgCUOG0a8lGpxDRL7zuU4JOp_SwVpdElfUhx7pVc78CPDVfyRqPa6nJb_-j94sz-M6fwMg3ViaAXiMBYzJ6m3_oW8o3aJc-x8Kp7aHp2TGQCTq8kBzLMJjlIDOxmqceBisEZxnsQJAfg5Il7exCd81mX0_dnhTutSWH7-sy_jaZIzbaWS9QU2Uem3H1dZ8KKkN_eaYSG0T1CSEcBRhLDtrw5vTX8i4tAGQ1Ug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ترامپ رسما از قالیباف و عراقچی تعریف کرد و گفت تیم ایرانی‌ها بسیار مقاوم هستند و من تحسین میکنم اونارو
✅
@AloNews</div>
<div class="tg-footer">👁️ 43.9K · <a href="https://t.me/alonews/138970" target="_blank">📅 20:51 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138968">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/eqjru22yyIUT9TJQWgTZ3yiPYv7qVP7FnQyvzgqLN2nJzbdioa7hOA8gbc0jTUAKuqw_O2qSMO55rs7k2YNg7cwIu6SAJ5epEeafC-tCWmvSAHEZA4fHO9GlsNuPum2iyZW8eJMa2_Xw2jXod3X0Zupkt9gco3uruRX19W-NqlSDhgNklUeKn8Am9y7qEGMsgYl1gIYBWYZNB_wpPPHv14ywOYKY-3Mm2xuAfCNmK0U4Tny1HNsKOY8F6HArl_sOUAub3exzgHUCTKjgaoSXGMRAsSOKB1rY0pVO2oGRywGC6pog13PNdyWAx862NWYOFScMsnTlYjLaOzqYpdYnoQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jfMYfmc2AK1JeAy1iTOYChq_QfN-kYcsBq2oOQiVRNHv78GevD8aUp-fLtky8wo2paVLUM-tKJKAX_bDIYTb7BFL3ufLi7ZeatU1sW1Dzvj5muhsobxAqHBJIbpR8YuDufkgurkuyWHOv9BPxESWdlRfOabqDs50YartrqfIteVJMuNhgdoI4Rk0Fzu4V4vV8n0iv4QcyrHbvLPGW4lLj0N7ljQI7eGWE37hQS2M6_4fYEVrA7lJLufFx8ZCelJNYmJykKsHNMnwE3Bw6DHW9I3wqXgrWhUkQ7mF9cqf062dxRvGzM8vQW5UWTuagkokHxyvuGVaDQ34PIozjQEqlw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
بر اساس تصاویر ماهواره‌ای، روز گذشته یک ناو هواپیمابر آمریکایی در ۳۴۰ کیلومتری بندر چابهار ایران مشاهده شده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 44.9K · <a href="https://t.me/alonews/138968" target="_blank">📅 20:46 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138967">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">👈
المانیتور: امریکا نیرو‌های باقی‌ماندهٔ خود را پیش از ضرب‌الاجل ۳۰ سپتامبر از عراق خارج می‌کند؛ سامانه‌های پدافند هوایی پاتریوت را نیز از اربیل جمع‌آوری کرده
✅
@AloNews</div>
<div class="tg-footer">👁️ 45K · <a href="https://t.me/alonews/138967" target="_blank">📅 20:42 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138966">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3a187554d6.mp4?token=b5RS1lDc_iTabzfnWFaDzVFD6f_CGTFhiQ7UEnL9j2jj6yFNflZNcYLzfvN4Zvp3diZ9IbcDXeKN18ROTbjZ3JovzZg5oLoJ8Pg2pYUNJd1iPLi18e9JK2RYfKYG8HmcUVXJaOOJ_bOgWLe8__0CoaTCrMaKKYVkXSqHOoGizJVC_JO07O7Jyo1rrV_AN2Pngc59nYWUceFblkLX4tW1iBxGby1Jrk1cOIkCte9NPlRbnq2PbenK5rJzT_2eqlyH_iUgxrFs1GlqeJxWHFCXRBNYyvHvE7hjuDgD-EyaZlnPD7nbJNaxJJMTG7tNcWt88uw2MCGXIJs8RRHrcXUlRg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3a187554d6.mp4?token=b5RS1lDc_iTabzfnWFaDzVFD6f_CGTFhiQ7UEnL9j2jj6yFNflZNcYLzfvN4Zvp3diZ9IbcDXeKN18ROTbjZ3JovzZg5oLoJ8Pg2pYUNJd1iPLi18e9JK2RYfKYG8HmcUVXJaOOJ_bOgWLe8__0CoaTCrMaKKYVkXSqHOoGizJVC_JO07O7Jyo1rrV_AN2Pngc59nYWUceFblkLX4tW1iBxGby1Jrk1cOIkCte9NPlRbnq2PbenK5rJzT_2eqlyH_iUgxrFs1GlqeJxWHFCXRBNYyvHvE7hjuDgD-EyaZlnPD7nbJNaxJJMTG7tNcWt88uw2MCGXIJs8RRHrcXUlRg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
خبرنگار: شما گفتید ایران هنوز برخی از توانایی‌های خود را حفظ کرده است. آیا آمریکایی‌ها باید برای این حملات پی در پی آماده باشند تا زمانی که ایران به سادگی قادر به حمله متقابل نباشد؟
🔴
ترامپ: آنها کمی قوی‌تر خواهند شد، شاید الان، اما ضعیف‌تر خواهند شد.بله، مطمئناً. شما همیشه باید هوشیار باشید.
✅
@AloNews</div>
<div class="tg-footer">👁️ 44.9K · <a href="https://t.me/alonews/138966" target="_blank">📅 20:40 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138965">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">👈
ترامپ درباره اوکراین و پاتریوت‌ها:
ما قدرتمندترین سلاح‌های جهان را داریم و باید در مورد افشای اسرار این سلاح‌ها محتاط باشیم. شما نمی‌توانید آن‌ها را کپی کنید.
🔴
این شبیه انویدیا است؛ آن‌ها یک تراشه دارند و می‌گویند که نمی‌توانید آن را کپی کنید.
✅
@AloNews</div>
<div class="tg-footer">👁️ 43.9K · <a href="https://t.me/alonews/138965" target="_blank">📅 20:32 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138964">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6359aac8e1.mp4?token=Qu3_rtKo4ItzMUuljCqseXd9iCSYIndJNkmM4GM0oEWJ4fN53fX9ZW5c5Qi2dLOLMHoxsqXHfSPbbL2ag_titecBB1ERhFSIGPTYsqiOvhv2zP4sPeWCQod-gLFeVv2x0KPLxMGVXO01H9grZ_IvqmYNW0ukmVFcsrTPngNAjRcyhgA0uVBR18Y5yKjrJHR3Y9SkwRhONG-LWWt-RzW5cE2dI8axI5_MPTKfCy11PngussN8FgN1I0l4c4MKuWlyu2X6Xb4kdL_knzWQwfqIt5qXQQnHPEpsNcC7qkHxmTQCnlFJAznCwyJ9vPnYOYpM_toAqRfRM814bIXDsFx9UA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6359aac8e1.mp4?token=Qu3_rtKo4ItzMUuljCqseXd9iCSYIndJNkmM4GM0oEWJ4fN53fX9ZW5c5Qi2dLOLMHoxsqXHfSPbbL2ag_titecBB1ERhFSIGPTYsqiOvhv2zP4sPeWCQod-gLFeVv2x0KPLxMGVXO01H9grZ_IvqmYNW0ukmVFcsrTPngNAjRcyhgA0uVBR18Y5yKjrJHR3Y9SkwRhONG-LWWt-RzW5cE2dI8axI5_MPTKfCy11PngussN8FgN1I0l4c4MKuWlyu2X6Xb4kdL_knzWQwfqIt5qXQQnHPEpsNcC7qkHxmTQCnlFJAznCwyJ9vPnYOYpM_toAqRfRM814bIXDsFx9UA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ
:
موشک تامهاوک باورنکردنی‌ترین است—می‌توانید از یک در عبور کنید، آن را از پنجره خانه عبور دهید. هیچ‌کس چیزی شبیه به آن ندیده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 44.9K · <a href="https://t.me/alonews/138964" target="_blank">📅 20:29 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138963">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/91678c091b.mp4?token=Uu2mhf3a4cmnnw3J0dd7vmPaMcgEcQprgl88NMLakHNZ_b0WWFXc4LO4XLxMhACg_8NeBrWJ8UeELHqtcI0pl6Vbp_bivQS-cgYfpEzxkTj8z_HDDH3MNN3dMo46RGJ7wZGlH_xVoa8WTZC6GIebclp1hL8JzApYpico_nMvzzzZOcV2Xe5YKCQZJVbnXTA4J1wFIZLK1o5VgIM94FHT0aMLt3os6JAhC-MqV_3UWwNDsWTEZ4PxwqgC6-is3mrn3UyJhI7BOyq020o9d7VCA_DgWYB4kmgfZL7I-Xl55TFLH_1KA6C8p9bx9xIVP7CQwwvyZlWBlDyMMXNTqXFdbg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/91678c091b.mp4?token=Uu2mhf3a4cmnnw3J0dd7vmPaMcgEcQprgl88NMLakHNZ_b0WWFXc4LO4XLxMhACg_8NeBrWJ8UeELHqtcI0pl6Vbp_bivQS-cgYfpEzxkTj8z_HDDH3MNN3dMo46RGJ7wZGlH_xVoa8WTZC6GIebclp1hL8JzApYpico_nMvzzzZOcV2Xe5YKCQZJVbnXTA4J1wFIZLK1o5VgIM94FHT0aMLt3os6JAhC-MqV_3UWwNDsWTEZ4PxwqgC6-is3mrn3UyJhI7BOyq020o9d7VCA_DgWYB4kmgfZL7I-Xl55TFLH_1KA6C8p9bx9xIVP7CQwwvyZlWBlDyMMXNTqXFdbg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
پرزیدنت ترامپ: «نیروی دریایی ایران کف اقیانوس است، نیروی هوایی‌اش رفته، رادارش رفته، رهبرانشون رفته‌اند؛ خلاصه همه‌چیز رفته!»
🔴
«
۱۵۹ کشتی داشتند؛ کل نیروی دریایی‌شان همین ۱۵۹ تا بود. الان همه‌شان کف دریا خوابیده‌اند. اگر این اسمش عملیات بزرگ نیست، پس چیست؟»
🔴
نوبت هواپیماها شد:
«۲۰۰ هواپیما داشتند؛ همه‌شان رفته‌اند، دانه‌به‌دانه. حتی یک هواپیما هم برایشان نمانده.»
🔴
پدافند هوایی؟
«خیلی خوب بود... فقط یک مشکل داشت؛ کار نکرد! حالا هم دیگر اثری از آن نیست.»
🔴
رادار؟ «
رفته
.»
🔴
رهبرانشون؟ «
رفته‌اند
.»
🔴
و بعد جمع‌بندی نهایی:
«همه‌چیز رفته.»
🔴
همه‌چیز... رفته. همه‌اش... رفته. رفته که رفته!
🔴
آخر هم با یک بالا انداختن شانه گفت:
«البته، باز هم به جنگیدن ادامه می‌دهند.»
✅
@AloNews</div>
<div class="tg-footer">👁️ 42.9K · <a href="https://t.me/alonews/138963" target="_blank">📅 20:29 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138962">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6dba80df0a.mp4?token=PllqMpRV6Sx1U21L-rRIpLUMQVTQAGeC9462saHdrSCYnwxYjU8gxVAmghnAfZKG8wHKr_iNaxZ4hN1VXv0mT0pzsCAKsQMlZc2mni5l8Dx596Rsy-t4Xqtaq3j_DBJS57t9PJQ3Olp54dOdCfZIJ87-NepniWI759f3rk5e3GK8nq3gHr_UKbpcqkZoiHqcF6wGnXMaWOdXB9SSI2kiODK567CdnqHfVVAoXtpAyI24e9jVW4y0mz5l_wW_ili3YCfpRqS2YRhYX9S67VT97eoAj-wf0-vnXKS9Ku59J4Wa3ImFzvAEWfX6007zIvCCJaz0ErrI_-xpNl_SKz9Qrw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6dba80df0a.mp4?token=PllqMpRV6Sx1U21L-rRIpLUMQVTQAGeC9462saHdrSCYnwxYjU8gxVAmghnAfZKG8wHKr_iNaxZ4hN1VXv0mT0pzsCAKsQMlZc2mni5l8Dx596Rsy-t4Xqtaq3j_DBJS57t9PJQ3Olp54dOdCfZIJ87-NepniWI759f3rk5e3GK8nq3gHr_UKbpcqkZoiHqcF6wGnXMaWOdXB9SSI2kiODK567CdnqHfVVAoXtpAyI24e9jVW4y0mz5l_wW_ili3YCfpRqS2YRhYX9S67VT97eoAj-wf0-vnXKS9Ku59J4Wa3ImFzvAEWfX6007zIvCCJaz0ErrI_-xpNl_SKz9Qrw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ درباره اوکراین: تانک‌های روسی در حال حرکت به سمت کی‌یف بودند، اما در گل و لای گیر کردند.
🔴
یک ژنرال تصمیم گرفت به جای استفاده از بزرگراه که در آنجا به خوبی پیش می‌رفتند، از میان گل و لای عبور کند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 42.9K · <a href="https://t.me/alonews/138962" target="_blank">📅 20:18 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138961">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3931af541f.mp4?token=QIShCC7iR9ob9EE2m8V-bYoyv4-qXOkf0v3o9pCtcWLxVlL4Dm8fAyaGlbhqoNj2ZQmuYYaM_49DtviAHCgDGUjMfOjOg5_ACsVnNntCxRl5hxttrx_cA_942z2XAFXZ8K3fXJynL09Qk_B6c3kGBBk7bUdualEHMbovW3vUw342H09kAwSaNpPwLJ5SHqSF05ta9FE9W4Sh66C5ZzmdGHbbKATRJBhueeuvHxCU4kqX8aCJH8Kwco6UfD6A95EbwCgAEqgctXmUw9TU8zosfsR5MeqPWyCqRD2sVRgD6waG5R0KwvREgIToUjgJ4SOQ5blbBOHlRnUMc4IEsA1nlA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3931af541f.mp4?token=QIShCC7iR9ob9EE2m8V-bYoyv4-qXOkf0v3o9pCtcWLxVlL4Dm8fAyaGlbhqoNj2ZQmuYYaM_49DtviAHCgDGUjMfOjOg5_ACsVnNntCxRl5hxttrx_cA_942z2XAFXZ8K3fXJynL09Qk_B6c3kGBBk7bUdualEHMbovW3vUw342H09kAwSaNpPwLJ5SHqSF05ta9FE9W4Sh66C5ZzmdGHbbKATRJBhueeuvHxCU4kqX8aCJH8Kwco6UfD6A95EbwCgAEqgctXmUw9TU8zosfsR5MeqPWyCqRD2sVRgD6waG5R0KwvREgIToUjgJ4SOQ5blbBOHlRnUMc4IEsA1nlA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ: ما درگیری بین هند و پاکستان را پایان دادیم. یازده هواپیما سرنگون شدند.
🔴
من گفتم: "اگر قصد جنگ کردن دارید، ما برای هر کدام از آن‌ها، تعرفه‌هایی معادل 250 درصد تعیین خواهیم کرد." آن‌ها فریاد زدند، جیغ کشیدند و هر دو طرف بسیار عصبانی بودند.
🔴
یک روز بعد، آن‌ها تماس گرفتند و گفتند: "ما جنگ نخواهیم کرد."
✅
@AloNews</div>
<div class="tg-footer">👁️ 42.9K · <a href="https://t.me/alonews/138961" target="_blank">📅 20:17 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138960">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">👈
ترامپ درباره ایران: آنها هفت ساعت درباره موضوع هسته‌ای صحبت می‌کنند. من می‌گویم: "چرا هفت ساعت؟ این کار را می‌شود در پنج تا ده دقیقه انجام داد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 41.8K · <a href="https://t.me/alonews/138960" target="_blank">📅 20:13 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138959">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">⭕️
هشدار درباره کلاهبرداری‌های اینترنتی
🔴
کلاهبرداران اینترنتی معمولاً با ایجاد هیجان، ترس، اعتماد یا عجله تلاش می‌کنند شما را وادار به واریز پول، نصب برنامه، بازکردن فایل یا ارائه اطلاعات بانکی کنند. با رعایت نکات زیر می‌توانید از خود و خانواده‌تان محافظت…</div>
<div class="tg-footer">👁️ 42.9K · <a href="https://t.me/alonews/138959" target="_blank">📅 20:13 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138958">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">👈
گزارشگر : آیا با اطمینان می‌شه گفت که ایران پشت این حملات سایبری بوده؟
🔴
ترامپ : به نظر من مقصر اصلی ایالت مینه‌سوتاست می‌دونید کار کیه؟ مینه‌سوتا
🔴
چون اون‌ها کاملاً بی‌کفایت هستن. من اصلاً فکر نمی‌کنم این یه حمله سایبری از طرف ایران بوده باشه
✅
@AloNews</div>
<div class="tg-footer">👁️ 42.9K · <a href="https://t.me/alonews/138958" target="_blank">📅 20:13 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138957">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">👈
ترامپ درباره روسیه و اوکراین:
هیچ‌کس نمی‌خواهد امتیازی بدهد، اما هم پوتین و هم زلنسکی باید برای رسیدن به توافق امتیاز بدهند
✅
@AloNews</div>
<div class="tg-footer">👁️ 40.8K · <a href="https://t.me/alonews/138957" target="_blank">📅 20:11 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138956">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">👈
ترامپ درباره ایران: «بیشتر مردم تا حالا تسلیم شده بودند. اما آنها این کار را نکرده‌اند، پس به خاطر این موضوع به آنها اعتبار می‌دهم.
🔴
آنها سرسخت هستند
✅
@AloNews</div>
<div class="tg-footer">👁️ 39.8K · <a href="https://t.me/alonews/138956" target="_blank">📅 20:10 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138955">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0770d9504e.mp4?token=Kj46UwUmlIVbJf-pvd9eDy8TYq7UXfkM1rO_HkNBLKFsgpxpqvrbK3ScJPSpQGsgiHG5k6muFyw8T05lFUOObluUEvWaVcYaMkaXIOWhrUAKpW2EAImvpohfFuzNv_-W3WCxOY5jS6N39diL22OUXBfSU2-YNNbI0bzmlFgHIcoTHzoU6ZpiMBk7qzyXp9BFhtGaP8-qdtj-GSM1f6vZ5B5OXCK3rDFk6zDspQL-Ix-TqPtAtt8pGm4nl_5iIEr2yzisvfGiGLGeRptuye1Yirwurc0Ldn8Tdr08ygyA67Sj-2OXXvzp5rxQ2kQ8qvz8s_VjYEk6lhyJQNadQyI44w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0770d9504e.mp4?token=Kj46UwUmlIVbJf-pvd9eDy8TYq7UXfkM1rO_HkNBLKFsgpxpqvrbK3ScJPSpQGsgiHG5k6muFyw8T05lFUOObluUEvWaVcYaMkaXIOWhrUAKpW2EAImvpohfFuzNv_-W3WCxOY5jS6N39diL22OUXBfSU2-YNNbI0bzmlFgHIcoTHzoU6ZpiMBk7qzyXp9BFhtGaP8-qdtj-GSM1f6vZ5B5OXCK3rDFk6zDspQL-Ix-TqPtAtt8pGm4nl_5iIEr2yzisvfGiGLGeRptuye1Yirwurc0Ldn8Tdr08ygyA67Sj-2OXXvzp5rxQ2kQ8qvz8s_VjYEk6lhyJQNadQyI44w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
خبرنگار: در مورد ایران، گزارشی وجود دارد که می‌گوید شما پیشنهادی از ارتش برای اقدام بزرگ دریافت کرده‌اید.
🔴
ادعای ترامپ: ما قبلاً اقدام بزرگ انجام داده‌ایم. چه اقدام بزرگی؟
✅
@AloNews</div>
<div class="tg-footer">👁️ 38.8K · <a href="https://t.me/alonews/138955" target="_blank">📅 20:09 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138954">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">👈
ترامپ در جلسه کابینه خود باره ایران : ما می‌توانیم با ایران به توافق برسیم، اما به دلیل دروغ‌گویی آن‌ها، اعتمادم به آن‌ها در حال از دست رفتن است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 37.7K · <a href="https://t.me/alonews/138954" target="_blank">📅 20:08 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138953">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/76ab421b66.mp4?token=EXDV6kN3XeB0_iOc3faRDDpT9pAwesZa__YmCmpztVBJcQm-5GPhOZmzKCNziBp8x_XfB5FC3tImOTK7dz285Ezi-OjOOdZ6TnLc4E_ur_40DPDCG-tPPPBVUVCXQaTwuy9ygF5qZqzkqAL0FJ7ljik-kOkgF3g47OriBorxuI4KRExzl-wHTyITIDd0RoiDu1hzRoGFZfBRdc222-iDpKLWJb4I2Z0g__BUc-IYjLQY160YINIk6UpPdCdYtBp4J-HWKyahxbMozvqhawCcVcdLjrD_kA0LKtCLdg9_0eV1Ri6o0v2t-gU89zTkZnO0sxc5uc_0TIh9v1_t_E0wWoiJMmJUHPi8i_Is8Vtzvicdpp04UIPVY_eNGxN8S8qrBoEf8ks59Z4L3VTXDBqtQpVHr2KiL0DbrTqYnJkEObedRCH4UN8i4hBubvlYXGw4MEuJv7s75zoX0RSPNmK8npFhuoALHwoc-YzXJyN3rH4YUrXboo8KzfYE-18B0IaFI6GiMYSvMflREOsFNZqeA7T0RjLtoFWC_11ML9stTVbKbohS81MEVSLXt5Xv_9uxrmqm8vpfK4w96UROey554s8-4Y7lPLpOQ0KIaADnd2eXo14TNCorggFci0CkC1ynIM2GnIbdxTEZD8B16n6Et4QoJ6M8-zbpzr5bocyf7IE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/76ab421b66.mp4?token=EXDV6kN3XeB0_iOc3faRDDpT9pAwesZa__YmCmpztVBJcQm-5GPhOZmzKCNziBp8x_XfB5FC3tImOTK7dz285Ezi-OjOOdZ6TnLc4E_ur_40DPDCG-tPPPBVUVCXQaTwuy9ygF5qZqzkqAL0FJ7ljik-kOkgF3g47OriBorxuI4KRExzl-wHTyITIDd0RoiDu1hzRoGFZfBRdc222-iDpKLWJb4I2Z0g__BUc-IYjLQY160YINIk6UpPdCdYtBp4J-HWKyahxbMozvqhawCcVcdLjrD_kA0LKtCLdg9_0eV1Ri6o0v2t-gU89zTkZnO0sxc5uc_0TIh9v1_t_E0wWoiJMmJUHPi8i_Is8Vtzvicdpp04UIPVY_eNGxN8S8qrBoEf8ks59Z4L3VTXDBqtQpVHr2KiL0DbrTqYnJkEObedRCH4UN8i4hBubvlYXGw4MEuJv7s75zoX0RSPNmK8npFhuoALHwoc-YzXJyN3rH4YUrXboo8KzfYE-18B0IaFI6GiMYSvMflREOsFNZqeA7T0RjLtoFWC_11ML9stTVbKbohS81MEVSLXt5Xv_9uxrmqm8vpfK4w96UROey554s8-4Y7lPLpOQ0KIaADnd2eXo14TNCorggFci0CkC1ynIM2GnIbdxTEZD8B16n6Et4QoJ6M8-zbpzr5bocyf7IE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
گزارشگر: چه کسی از دولت با ایران صحبت می‌کند؟
🔴
پرزیدنت ترامپ: آن‌ها همیشه می‌خواهند صحبت کنند... استیو، جرد، جی‌دی و مارکو درگیر هستند.
🔴
گزارشگر: ایران می‌گوید مذاکراتی در حال انجام نیست
🔴
ترامپ: ممکن است مدت طولانی درباره هسته‌ای صحبت کنیم و سپس آن‌ها بیرون بروند و بگویند: «ما هرگز درباره هسته‌ای صحبت نکردیم...» آن‌ها فقط کاری می‌کنند که عصبانی شوم
✅
@AloNews</div>
<div class="tg-footer">👁️ 37.8K · <a href="https://t.me/alonews/138953" target="_blank">📅 20:07 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138952">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3a12328c23.mp4?token=hxA5jl2nDaWCeEnueK9Il2rgZAPlUEXhHkrfbhfVnkoW2OuhRkaP8CjZWYJ6ATQ6tf_wbHytSuTQSVFppBdkfZTHFP7OnfoAnurASpuwQGG0OzYmRTmyoTPN-uOV0JjVZclLJz2Te6pgu7ys90HTpGOWWFI1m0iKDm8La7M9TljrDrKlNkD6GGKpPc0QhXdA4nsaB-B51jgZ8KxtbrSdaSbyO3TPlJZtFW1hIxs9q3CHXguobPBWSphru3NofaWBeraS3-wxsswaGcTLdUeDmcXO3N2amJYxSS3-b7_icU2_uXlhQB38EXsYoFUPbPZn6PJbCznh4R-EbItHK_WjaAJ5eNpeeeEDhSQ52ErRNv93W1h1XE8yJjpOKaXT4Dm9SxkfpQPS0u0ft2DxWpNSuPKOJ_dhoG6pKAfCUn6H1xumEyiqnvCVUWDkp9U0rLOp6h29TVJzF8PqptMV56DqU0oFWQ48V87YHH41hwTNkf5DeIvWEhRvGMq3868rSzGk2PyE63YVrKf6Mlz4Klaea-dIO4AkBi7uihqV5FkOLFOzv5PJgtrI7JS1AiittF4voLGbp02EtK2DGMWdGaYRCs8A4vV8BGSQCfWE5OJrhkpDux3PbnLk0ByIOU6j6jFaU0mzCbQ7c2qkGOF_8CFWLifHSbEYA9S-YmGr_HBzP8Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3a12328c23.mp4?token=hxA5jl2nDaWCeEnueK9Il2rgZAPlUEXhHkrfbhfVnkoW2OuhRkaP8CjZWYJ6ATQ6tf_wbHytSuTQSVFppBdkfZTHFP7OnfoAnurASpuwQGG0OzYmRTmyoTPN-uOV0JjVZclLJz2Te6pgu7ys90HTpGOWWFI1m0iKDm8La7M9TljrDrKlNkD6GGKpPc0QhXdA4nsaB-B51jgZ8KxtbrSdaSbyO3TPlJZtFW1hIxs9q3CHXguobPBWSphru3NofaWBeraS3-wxsswaGcTLdUeDmcXO3N2amJYxSS3-b7_icU2_uXlhQB38EXsYoFUPbPZn6PJbCznh4R-EbItHK_WjaAJ5eNpeeeEDhSQ52ErRNv93W1h1XE8yJjpOKaXT4Dm9SxkfpQPS0u0ft2DxWpNSuPKOJ_dhoG6pKAfCUn6H1xumEyiqnvCVUWDkp9U0rLOp6h29TVJzF8PqptMV56DqU0oFWQ48V87YHH41hwTNkf5DeIvWEhRvGMq3868rSzGk2PyE63YVrKf6Mlz4Klaea-dIO4AkBi7uihqV5FkOLFOzv5PJgtrI7JS1AiittF4voLGbp02EtK2DGMWdGaYRCs8A4vV8BGSQCfWE5OJrhkpDux3PbnLk0ByIOU6j6jFaU0mzCbQ7c2qkGOF_8CFWLifHSbEYA9S-YmGr_HBzP8Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ در مورد ایران
:
ما فقط می‌خواهیم پیروز شویم. ما خیلی خوب عمل می‌کنیم.
🔴
ما سعی می‌کنیم مهربان باشیم، تا جایی که می‌توانید در چنین شرایطی مهربان باشید.آنها در حال نابودی هستند
✅
@AloNews</div>
<div class="tg-footer">👁️ 34.7K · <a href="https://t.me/alonews/138952" target="_blank">📅 20:06 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138951">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/62eddc2fc0.mp4?token=CEVcWdtaB1ddxtFjImVwx6GFp9gmfAE8EmLRqcQw0jhuY_Rf5TOIyKhRcxwZI1MU4y6aN5cAplJsxLDfdOohrIqDEDST07OlBuFmnQHbk9EllwIQ1L2HauIvqlgGrootI9laef6ZIEH8RurDIhf6mvPvsiS6uYYR8QNjIBUWXGNRsxgTv6RTwoncvPAW2vwfB7FLG55198GjxHfH404UD5s3wG9rHtWPNYWVVCjJbWkmdoWpNqouzxVww69rBj0qlrx_u9yc__43UsJ8KJA1-Rdr5OIYYqMLrZKRztfvrdBvAwtp_-irkswlGR3KcCa3gQtP3Qos0VDgAnU2wTXUNQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/62eddc2fc0.mp4?token=CEVcWdtaB1ddxtFjImVwx6GFp9gmfAE8EmLRqcQw0jhuY_Rf5TOIyKhRcxwZI1MU4y6aN5cAplJsxLDfdOohrIqDEDST07OlBuFmnQHbk9EllwIQ1L2HauIvqlgGrootI9laef6ZIEH8RurDIhf6mvPvsiS6uYYR8QNjIBUWXGNRsxgTv6RTwoncvPAW2vwfB7FLG55198GjxHfH404UD5s3wG9rHtWPNYWVVCjJbWkmdoWpNqouzxVww69rBj0qlrx_u9yc__43UsJ8KJA1-Rdr5OIYYqMLrZKRztfvrdBvAwtp_-irkswlGR3KcCa3gQtP3Qos0VDgAnU2wTXUNQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
گزارشگر
:
با توجه به اینکه حماس طبق این برنامه سلاح‌های خود را تحویل می‌دهد، چه کسی را مسئول دریافت سلاح‌های آن‌ها می‌دانید؟
🔴
ترامپ
:
هیئت صلح
✅
@AloNews</div>
<div class="tg-footer">👁️ 34.7K · <a href="https://t.me/alonews/138951" target="_blank">📅 20:03 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138950">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/783659570a.mp4?token=Ke3YZxkEr-sgBacLg3DEntUzsUGqXbrmf7THgEVLannASyKw4_ZdDD4iv9Tx1w4KVbdEUjP4xT7mF5iRGOMUeJhmEQr_sBgRS6FtlMncCauvaCLi7jHoi4pXQqMIh89IzNkOfKms8ybfiLRfTiD0uP1jtRaA1nK6apkoZ0IkdjA3WKR10s8wRGhp3SqMOpsSLjRE1zT5OFTTX6Ln3-hYqubHz7-BMkgrJ2IraoWRcWVrQmhUVlr6rGevEv1ZS29zsKJ-Nc-NZU0xIBGAYi4aA1OWl6zBoj8C15okEqQjXGIZyonUxatCvLRWYUWXkjNxK5adqqpTsNLIuEcRfYIzrZW8aA2wQcy6ukLKo-pD1GHP9V_DXrRcdWssGA1TSZZ_LaYGTDQ9vn1eVru_TMcwp3nv-VeBLGAzgzVyxtQaS9820qKOb_2GducyLB12Y_-rQSQ-1IdFz5IOKQj98DFk4Nfjy534aIBzVFqIkJI4EghFy7H9_8Q-kGynKS5fy4yfkKe2hBpOoMBYNNKlwHA7VIK1B4bmDFe6sgnnFay_pqeYPyjE7eebFHbS1yJIRQGdw0O1acpDdISRlpBxS8QuxPOKwyTMV0mGjTKXKQPyMzWycN-KBLal5J6d-itJCR2UuwqDB6M5sZc1aOZd57QozrdljV8BkD3jfBW-yFef-0I" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/783659570a.mp4?token=Ke3YZxkEr-sgBacLg3DEntUzsUGqXbrmf7THgEVLannASyKw4_ZdDD4iv9Tx1w4KVbdEUjP4xT7mF5iRGOMUeJhmEQr_sBgRS6FtlMncCauvaCLi7jHoi4pXQqMIh89IzNkOfKms8ybfiLRfTiD0uP1jtRaA1nK6apkoZ0IkdjA3WKR10s8wRGhp3SqMOpsSLjRE1zT5OFTTX6Ln3-hYqubHz7-BMkgrJ2IraoWRcWVrQmhUVlr6rGevEv1ZS29zsKJ-Nc-NZU0xIBGAYi4aA1OWl6zBoj8C15okEqQjXGIZyonUxatCvLRWYUWXkjNxK5adqqpTsNLIuEcRfYIzrZW8aA2wQcy6ukLKo-pD1GHP9V_DXrRcdWssGA1TSZZ_LaYGTDQ9vn1eVru_TMcwp3nv-VeBLGAzgzVyxtQaS9820qKOb_2GducyLB12Y_-rQSQ-1IdFz5IOKQj98DFk4Nfjy534aIBzVFqIkJI4EghFy7H9_8Q-kGynKS5fy4yfkKe2hBpOoMBYNNKlwHA7VIK1B4bmDFe6sgnnFay_pqeYPyjE7eebFHbS1yJIRQGdw0O1acpDdISRlpBxS8QuxPOKwyTMV0mGjTKXKQPyMzWycN-KBLal5J6d-itJCR2UuwqDB6M5sZc1aOZd57QozrdljV8BkD3jfBW-yFef-0I" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ درباره اوکراین و سامانه پاتریوت‌ها: باید بسیار محتاط باشیم در اجازه دادن به کسی برای ساخت سلاح‌های پیشرفته ما
🔴
ما به این موضوع موافقت نکرده‌ایم. در حال صحبت درباره آن هستیم. دادن آن نوع فناوری کار دشواری است.
🔴
آن کسانی که به آن‌ها فناوری می‌دهید نیز می‌توانند علیه شما برگردند. این امکان‌پذیر است.
🔴
باید بسیار محتاط باشیم.
✅
@AloNews</div>
<div class="tg-footer">👁️ 34.7K · <a href="https://t.me/alonews/138950" target="_blank">📅 20:03 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138949">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/884550e186.mp4?token=AcdC1ti66psmAy5gmFhES2mDIHrRig_Y-HN5Ql5sRIda5Sxp7C2T-whxMlgvJnGvxk-7y0v4j29tMQzI6l7_ogCFOYr52mpqBY5hgPW41S_vNrYFe8yqsPuaOGbi9KKCjrUXHQcvNK63mhuWCYUNc3_PZb-CycDGbJAZ72H0JCmpNXqLlbJBKNtzCa-zGxKaHVZLw1R-c9WFCljIg37zNwCzo0OAOv_ew0pP35R7cA7oHhl82_1KPkspEdiGBmapYULVvua0-EQmLUal3-VVlwZVo-Bd_SHB5f2RaABMplOvXrbL7qpOJ2_CTo6NiylBwdGce32RaChwWCJBbXxPEg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/884550e186.mp4?token=AcdC1ti66psmAy5gmFhES2mDIHrRig_Y-HN5Ql5sRIda5Sxp7C2T-whxMlgvJnGvxk-7y0v4j29tMQzI6l7_ogCFOYr52mpqBY5hgPW41S_vNrYFe8yqsPuaOGbi9KKCjrUXHQcvNK63mhuWCYUNc3_PZb-CycDGbJAZ72H0JCmpNXqLlbJBKNtzCa-zGxKaHVZLw1R-c9WFCljIg37zNwCzo0OAOv_ew0pP35R7cA7oHhl82_1KPkspEdiGBmapYULVvua0-EQmLUal3-VVlwZVo-Bd_SHB5f2RaABMplOvXrbL7qpOJ2_CTo6NiylBwdGce32RaChwWCJBbXxPEg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ: بینگ، بینگ، بینگ، بینگ، بینگ، بینگ، بینگ، بینگ، بینگ، بینگ!
✅
@AloNews</div>
<div class="tg-footer">👁️ 34.7K · <a href="https://t.me/alonews/138949" target="_blank">📅 20:01 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138948">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7681e354db.mp4?token=cqZxSVpFMCHE1lupoCgeUA8KXtdPDnDj_JSn51Xz7q9qsqEdXvUoEZ6_h5Gubv1PV_axq5beP0WBTRQQTjgQlGLf8gtT3O4oC7S5cZt9Z_UiXxbAjxSFcv88MzK2MQybq8a_Y9Be2-2r-5GdmRmDgCh4Eew0Blqstxhar80uApmhaZOi-WqRmMnu72dFE8Jeh2MyYEVos9wx30nd6GcZ3wvVnWUrumRnAImKehet_rShw2OsDHGHqHrNDV0XCcqD0qDI06OcedWwwJ6ls2gAocOE9HZGpCikiMuB9-azME5-OP8LtRDCRku8Tk18D43yLsvLzxn-aqOQsuUPNCcV8A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7681e354db.mp4?token=cqZxSVpFMCHE1lupoCgeUA8KXtdPDnDj_JSn51Xz7q9qsqEdXvUoEZ6_h5Gubv1PV_axq5beP0WBTRQQTjgQlGLf8gtT3O4oC7S5cZt9Z_UiXxbAjxSFcv88MzK2MQybq8a_Y9Be2-2r-5GdmRmDgCh4Eew0Blqstxhar80uApmhaZOi-WqRmMnu72dFE8Jeh2MyYEVos9wx30nd6GcZ3wvVnWUrumRnAImKehet_rShw2OsDHGHqHrNDV0XCcqD0qDI06OcedWwwJ6ls2gAocOE9HZGpCikiMuB9-azME5-OP8LtRDCRku8Tk18D43yLsvLzxn-aqOQsuUPNCcV8A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
دونالد ترامپ در مورد ایران: ایران سلاح‌های ضد هوایی بسیار خوبی داشت، اما این سلاح‌ها کارایی نداشتند
✅
@AloNews</div>
<div class="tg-footer">👁️ 35.7K · <a href="https://t.me/alonews/138948" target="_blank">📅 20:01 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138947">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c1a4937b8c.mp4?token=neQP62BPrrLNBAhnTTE8Slb7llMqESR0IqfFDWT5NmmeAuPtFUJzm5EXSEuEmccfnF1zbuGW_mvfMqE0BlSFtdDp4prM6YAPbs-H7B3mGw-N_aIqHy0UU20Rz6xiWWB_5mLQJN5HY92wK3R4_0MRp6aovOLQBnsQWdS_8rqh28vg37k8vBcBMx5dZ2jfJLQQgGlQQaTbYA1V1Sg8qCuznoedGOUwDIfeXVYll6LcfrIrQeUF6lHmgE73E5ylNPYedYabuqJCKvKT71X4rXuECVFf_zY9npUh30i5XkvkXxMoZ7oNyAy7GsU7Ua8QnntBlvJjvsX3V3aUxFgYyKIehw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c1a4937b8c.mp4?token=neQP62BPrrLNBAhnTTE8Slb7llMqESR0IqfFDWT5NmmeAuPtFUJzm5EXSEuEmccfnF1zbuGW_mvfMqE0BlSFtdDp4prM6YAPbs-H7B3mGw-N_aIqHy0UU20Rz6xiWWB_5mLQJN5HY92wK3R4_0MRp6aovOLQBnsQWdS_8rqh28vg37k8vBcBMx5dZ2jfJLQQgGlQQaTbYA1V1Sg8qCuznoedGOUwDIfeXVYll6LcfrIrQeUF6lHmgE73E5ylNPYedYabuqJCKvKT71X4rXuECVFf_zY9npUh30i5XkvkXxMoZ7oNyAy7GsU7Ua8QnntBlvJjvsX3V3aUxFgYyKIehw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ: دولت بایدن و دولت اوباما، دولت را به ابزاری تبدیل کردند و زندگی‌ها را نابود کردند
✅
@AloNews</div>
<div class="tg-footer">👁️ 34.7K · <a href="https://t.me/alonews/138947" target="_blank">📅 19:59 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138946">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">👈
گزارشگر : درباره ایران، گزارش‌هایی منتشر شده که می‌گه ارتش به شما پیشنهاد داده اقدامات گسترده‌تری انجام بدید.
🔴
ترامپ : ما که همین حالاش هم اقدامات خیلی گسترده‌ای انجام دادیم. اصلاً منظورتون از «گسترده‌تر» چیه‌؟
✅
@AloNews</div>
<div class="tg-footer">👁️ 34.7K · <a href="https://t.me/alonews/138946" target="_blank">📅 19:59 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138945">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">👈
ترامپ درباره توافق غزه : اسرائیل از این توافق خیلی خوشحاله
🔴
توی رسیدن بهش هم خیلی بهمون کمک کرد و واقعاً خوب عمل کرد.
🔴
هیچ‌کس فکر نمی‌کرد همچین چیزی ممکن باشه؛ اینکه حماس خلع سلاح بشه.
🔴
این نشون می‌ده که ما در قبال ایران چقدر موفق بودیم. اگه برگردیم به چهار یا پنج ماه پیش، همچین توافقی اصلاً امکان‌پذیر نبود.
🔴
این یه قدم خیلی بزرگ برای خاورمیانه‌ست
✅
@AloNews</div>
<div class="tg-footer">👁️ 34.6K · <a href="https://t.me/alonews/138945" target="_blank">📅 19:58 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138944">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">👈
روبیو: ما در خاورمیانه به موفقیت‌های دیپلماتیک دست یافته‌ایم
🔴
توافق بین لبنان و اسرائیل بی‌سابقه است.
🔴
توافق حماس برای خلع سلاح یک دستاورد است
🔴
هنوز کارهای زیادی در رابطه با لبنان و اسرائیل برای حفظ و ایجاد این صلح باید انجام شود، اما این یک هدف قابل دستیابی است
✅
@AloNews</div>
<div class="tg-footer">👁️ 34.7K · <a href="https://t.me/alonews/138944" target="_blank">📅 19:56 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138943">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">👈
وزیرجنگ آمریکا: تعهد ما تزلزل‌ناپذیر است که ایران به سلاح هسته‌ای دست پیدا نخواهد کرد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 36.7K · <a href="https://t.me/alonews/138943" target="_blank">📅 19:56 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138942">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/adc88001f8.mp4?token=cmgTkAESxVSjpBWOsDe-k1ewCO6DTaHLz2HiN6VuUmuGz6158VEZIiQR-hm9saZdiypcoKetkRgmwbx4FQCSpa_syoKohBtGlW594_JpexsiqtVMwvprJF9eJk92WZq0PM_NOjvXKa4J0ImI4Uv4zpgBtMX__v8kflaGYsZpxd8JPn3flf5fSCdRyxv9RBwgg_KXUR5BVbzeuannNgB2s1CbSxAeqZK_Y2ZHLFgZQl10FzN6XN9Cgccg6nJ-dHc05c9kPckFUffpjLNChpQwBpgAtbh_sluYGw3Km9SCvC8z5qofrFFzfoD2LtHXu6MDP2u-ms_W7ugsP5FNQcbY_w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/adc88001f8.mp4?token=cmgTkAESxVSjpBWOsDe-k1ewCO6DTaHLz2HiN6VuUmuGz6158VEZIiQR-hm9saZdiypcoKetkRgmwbx4FQCSpa_syoKohBtGlW594_JpexsiqtVMwvprJF9eJk92WZq0PM_NOjvXKa4J0ImI4Uv4zpgBtMX__v8kflaGYsZpxd8JPn3flf5fSCdRyxv9RBwgg_KXUR5BVbzeuannNgB2s1CbSxAeqZK_Y2ZHLFgZQl10FzN6XN9Cgccg6nJ-dHc05c9kPckFUffpjLNChpQwBpgAtbh_sluYGw3Km9SCvC8z5qofrFFzfoD2LtHXu6MDP2u-ms_W7ugsP5FNQcbY_w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
خبرنگار: درباره ایران، گزارشی منتشر شده که می‌گوید ارتش به شما پیشنهاد داده عملیات را در ابعاد بسیار گسترده‌تری انجام دهید.
🔴
ترامپ: ما همین حالا هم اقدام بزرگی انجام داده‌ایم. دیگر «بزرگ‌تر» یعنی چه؟
✅
@AloNews</div>
<div class="tg-footer">👁️ 37.7K · <a href="https://t.me/alonews/138942" target="_blank">📅 19:55 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138941">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0bca9802ae.mp4?token=ILJVX-h0cjPWQINg52CC2s7G9ft4JWxHfr_L6Uo_Fxf5R8NMkwgQ4o17-sTSMjYcyHv_sNmr1L7bIcPdeTKfXEKXD6e0Me2Bo_8WJXP4cmNC6937aM1L4tk9kORD5i-YCfmTPe7Z_JaHQHk5vrTdk4Ne9ab3SArJYfMp4LUyAjXHEQE3VpOIDb-UHNAaF2fAad-0CrOzUgAbC-A3YxmJvIcNFVSkdVrlq6s0dnW1rkxRkIVPq4prnzgGHp6oqdOMZgG3L5wyaTZ6VMOCTnczqiMVXuxxi8q61BPdSfUFOrgvaU-BIR9eFmaDwNHLXcYXqB4dF9qN5J8GrndSri9Y7g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0bca9802ae.mp4?token=ILJVX-h0cjPWQINg52CC2s7G9ft4JWxHfr_L6Uo_Fxf5R8NMkwgQ4o17-sTSMjYcyHv_sNmr1L7bIcPdeTKfXEKXD6e0Me2Bo_8WJXP4cmNC6937aM1L4tk9kORD5i-YCfmTPe7Z_JaHQHk5vrTdk4Ne9ab3SArJYfMp4LUyAjXHEQE3VpOIDb-UHNAaF2fAad-0CrOzUgAbC-A3YxmJvIcNFVSkdVrlq6s0dnW1rkxRkIVPq4prnzgGHp6oqdOMZgG3L5wyaTZ6VMOCTnczqiMVXuxxi8q61BPdSfUFOrgvaU-BIR9eFmaDwNHLXcYXqB4dF9qN5J8GrndSri9Y7g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ درباره ایران: ما به آنها ضربه بسیار سنگینی وارد خواهیم کرد. در یک مقطعی، آنها خواهند گفت: "دیگر نمی‌توانیم این وضعیت را تحمل کنیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 37.7K · <a href="https://t.me/alonews/138941" target="_blank">📅 19:47 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138940">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/jTSlxQDJg7tCIgh3LKEhRkVGb4sI7JkbHUZSUwXS0qMHg2_SCGHXDiFIix6vbf4JtWhvYSBz-1U1SCtjdRQecR8ZeQOuEmIbnG4ulsZRSzxcIq6CEVIVim3eTSslC2NL1uyGo48lRAYPy65ParjswbVDydkwP6W85if9wOxlbvBP7NUOhdKxtif4FWQLrz24yLM8MKRoQrUcSdSbYhVXzPa1iSJkkvSDkWB2gHistAKnzzogITPqi4-gRCL6JN1kPYnw9EqM1-hPI3dix0TQyztGeEp5XDhawkQ0tvclz3YSvOPfky7QZEyuK6zMQyTB8Vt9kqPdDN-lYX_HeSmT4A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
سنتکام
🔴
ادعا: دولت ایران بار دیگر مدعی شده است که تنگه هرمز را بسته است. این ادعا نادرست است.
🔴
واقعیت: تنگه هرمز همچنان برای عبور کشتی‌های تجاری باز است. ایران کنترلی بر آن ندارد. طی چهار ماه گذشته، هزاران کشتی از این آبراه بین‌المللی عبور کرده‌اند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 38.8K · <a href="https://t.me/alonews/138940" target="_blank">📅 19:46 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138939">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2a5ffc0577.mp4?token=FBKk9HVDEbigvNnpvh7ghd-fVemDuxqu9NeQ7cCskL5Sx_sWuEYqQ_chZbPg4SYx00rho2_C6a9rP4HdGNj7p9fx4IegaI2OvLdbIKZPGM-t5-COOUQhr6rnxihEznw_UTq7RxePVEDpJDAEx_CeEoaGMd42_IaQTuYwoBUxxr35LEg_ornr2HPdTLkLdMUo8FnnxqRCiLNqWFsAKVJHYm1BaLaZcrKXuPZLQA1tMh5oARdF9A3S9_eAvYhHc991Inr9ZU4uD96-cAD3MNKkk9f2He_JtdmCZFvG6-0vAauzDN02koNrKAbXUphW59NuQlYWN1GJr1UtNIrP1F1tHALClV9xaUviNsGDL7sMUTaPBHWtIZ1MawSfpOpYCtjKZeLp3NecOr0EPJOvpz2FnaWuVirz8dSbHlHsNr7OXpTaZMuKLY1JSYYJX29vw0BzuQeh_z4w0zKXayXutiZTVBhQbQzeytYnlJujeN750Xy-AAQwn8mHqvAC9tbJA6OtOG12uGzSaxTAViCLIfwFeqBMoQUiMNeXLZ-8EGqmOWLjKnBc5cBrqwk8sFS4b2i1yfl1YHtBOO_1P4ux-xqxZ_Pyxp3PRsUPTXlOonCjfiuVmpNo6XRv7Ro8CTKW8cI1jLa7vBn5jvHLlx3GQ-i36upNK9wPO6rxzJ8TYkozU_M" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2a5ffc0577.mp4?token=FBKk9HVDEbigvNnpvh7ghd-fVemDuxqu9NeQ7cCskL5Sx_sWuEYqQ_chZbPg4SYx00rho2_C6a9rP4HdGNj7p9fx4IegaI2OvLdbIKZPGM-t5-COOUQhr6rnxihEznw_UTq7RxePVEDpJDAEx_CeEoaGMd42_IaQTuYwoBUxxr35LEg_ornr2HPdTLkLdMUo8FnnxqRCiLNqWFsAKVJHYm1BaLaZcrKXuPZLQA1tMh5oARdF9A3S9_eAvYhHc991Inr9ZU4uD96-cAD3MNKkk9f2He_JtdmCZFvG6-0vAauzDN02koNrKAbXUphW59NuQlYWN1GJr1UtNIrP1F1tHALClV9xaUviNsGDL7sMUTaPBHWtIZ1MawSfpOpYCtjKZeLp3NecOr0EPJOvpz2FnaWuVirz8dSbHlHsNr7OXpTaZMuKLY1JSYYJX29vw0BzuQeh_z4w0zKXayXutiZTVBhQbQzeytYnlJujeN750Xy-AAQwn8mHqvAC9tbJA6OtOG12uGzSaxTAViCLIfwFeqBMoQUiMNeXLZ-8EGqmOWLjKnBc5cBrqwk8sFS4b2i1yfl1YHtBOO_1P4ux-xqxZ_Pyxp3PRsUPTXlOonCjfiuVmpNo6XRv7Ro8CTKW8cI1jLa7vBn5jvHLlx3GQ-i36upNK9wPO6rxzJ8TYkozU_M" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
اسکات بسنت، وزیر خزانه‌داری ایالات متحده آمریکا در جلسه کابینه دولت: ما در مارس 2025 شروع کردیم. در دسامبر 2025، بزرگ‌ترین بانک در ایران فرو ریخت.
🔴
بانک مرکزی مجبور شد پول چاپ کند و این باعث تورم شد. آن‌ها اکنون قادر به پرداخت حقوق سربازان خود نیستند.
و به سفارش شما، ما در سرتاسر جهان به دنبال دارایی های آنها هستیم.
✅
@AloNews</div>
<div class="tg-footer">👁️ 36.7K · <a href="https://t.me/alonews/138939" target="_blank">📅 19:43 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138938">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Uiuj51xxTSINhzZEh3R4qTkjV5yXEHFN8sfeSQcLysVWpR_21SiMvE8JAqoNKnBQ9k46VTGHB8dmIYXQVC9LiH_MoVpK8HwY8iLfSU3NTU_lfGzWv4pJdg9fbVtrn4tO5U1SKWSazMnbZyrZp_-ADu_cqyxeBteUq6PZA_kSDC73lOx3jKzd66WqTavz5-FSVhPqPnbA9cX6A0ftNRpt0ATeyLSrA_XkDXItTAqwsZmFraJf8Tsg4peRqODAbBCM__G6CQg2R5BCk5kauEnrdgkIP8mC9WUNupUsNEqmvgZfmxUJHTguTUP2VCSO8jBxTG5HOQLlrZMPxYGrIbYXGg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
وزارت امور خارجه ایالات متحده آمریکا: ایالات متحده در کنار مردم اسپانیا و تمام اروپایی‌ها، در برابر این نقض فاحش حاکمیت و حقوق بشر آن‌ها می‌ایستد.
🔴
این حادثه غیرقابل قبول، نتیجه مستقیم تلاش‌های عمدی دولت اسپانیا برای امکان‌پذیر کردن و تسهیل مهاجرت غیرقانونی انبوه به اروپا است.
🔴
ما در حال بررسی اقداماتی برای دفاع از آمریکایی‌ها در داخل و خارج از کشور در برابر این تهدید هستیم و آماده‌ایم تا به سایر متحدان اروپایی که گزینه‌های مشابهی را در نظر می‌گیرند، کمک کنیم.
✅
@AloNews</div>
<div class="tg-footer">👁️ 36.7K · <a href="https://t.me/alonews/138938" target="_blank">📅 19:43 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138937">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">👈
رویترز: روسیه برای کاهش کمبود سوخت ناشی از حملات اوکراین به پالایشگاه‌های بزرگ این کشور، ۳۰ هزار تن بنزین از مراکش وارد کرده
🔴
مسکو همچنین برای تأمین سوخت به هند، بلاروس و قزاقستان روی آورده
✅
@AloNews</div>
<div class="tg-footer">👁️ 35.7K · <a href="https://t.me/alonews/138937" target="_blank">📅 19:40 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138936">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">👈
پیت هگستث، وزیر جنگ ایالات متحده آمریکا در جلسه کابینه دولت درباره استیو ویتکوف:
🔴
ما بهترین مذاکره‌کنندگان جهان را داریم
✅
@AloNews</div>
<div class="tg-footer">👁️ 37.8K · <a href="https://t.me/alonews/138936" target="_blank">📅 19:38 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138935">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7b0ec710b6.mp4?token=Zvda12r8ltMrY1Wv6FGnv8jdLDQVVWEkCs1zywfUGaOJJ9RbTp8w6THsA3mjwjNXBOW3K9o8ln3iy9RK-8qAbd47b6xmXkS7XcA7DU6esD1JDvHwVXm2UlCjAupvEdjpBWXXmUTju-P_7sU9WtcU5w9CLZ-AFzku9-N1BPUpk6xvUXE2AiUJH7oCmtaphE5AZCYmdYclk9q198X0BqBc6VNGhvRjc6PHQLazASBSPVw89t7thbc7HqaupvMHkl8lgk70XxEY874zDgCOHBkUO-yVZJGvZ8DKCG-nOxx95-r4_d6K41tSq8wSMRT2x7ZNUQKF32VVRgidGh3j6m5oXg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7b0ec710b6.mp4?token=Zvda12r8ltMrY1Wv6FGnv8jdLDQVVWEkCs1zywfUGaOJJ9RbTp8w6THsA3mjwjNXBOW3K9o8ln3iy9RK-8qAbd47b6xmXkS7XcA7DU6esD1JDvHwVXm2UlCjAupvEdjpBWXXmUTju-P_7sU9WtcU5w9CLZ-AFzku9-N1BPUpk6xvUXE2AiUJH7oCmtaphE5AZCYmdYclk9q198X0BqBc6VNGhvRjc6PHQLazASBSPVw89t7thbc7HqaupvMHkl8lgk70XxEY874zDgCOHBkUO-yVZJGvZ8DKCG-nOxx95-r4_d6K41tSq8wSMRT2x7ZNUQKF32VVRgidGh3j6m5oXg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
پیت هگستث، وزیر جنگ ایالات متحده آمریکا در جلسه کابینه دولت: شما متعجب هستید که حوثی‌ها در این درگیری درگیر نیستند، با وجود اینکه آن‌ها نیابتی از ایران هستند؟
🔴
زیرا آن‌ها وزن قدرت آمریکا را به مدت ۴۵ روز احساس کردند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 38.8K · <a href="https://t.me/alonews/138935" target="_blank">📅 19:37 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138934">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">👈
ترامپ: «هیچ اطلاعاتی وجود ندارد که نشان دهد دیوان کیفری بین‌المللی به دنبال من است.
🔴
البته ممکن است چنین اتفاقی بیفتد؛ فقط خواستم این را بدانید.
🔴
مارکو روبیو در تلاش نیست از من دفاع کند. او در تلاش است از بنیامین نتانیاهو و افراد مختلف دیگری دفاع کند.»
✅
@AloNews</div>
<div class="tg-footer">👁️ 38.8K · <a href="https://t.me/alonews/138934" target="_blank">📅 19:30 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138933">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ccd841332e.mp4?token=XlR2upzkQnJy6Lz8KO7-DGneI1guskO5flbxrruRfSXRv22SQCNLLX-KLWqNI9VKshuY6RHPNww2wlSu3nE1bpSli1I8UBRHLEGrwIHA1xhUH68VMbOOfrYH3OJq_AeLI9Y3iyiQijh9ayJjRhLfzSqFheCl3_IMu370yENTPfngX7mSojBLWpR1rGNwgvZeh9aqvIQo416PzFCJziMeOsybLRAQ-dGarlao5UVIC8Dayf_eaX2dKPidX6VJsm4q1NgKLZa1woTq2dvrigPJR90NZlT8z5p6oOT7pbNluI6nU4hHCB-fH0z5cr8DqckS2XyChOug-O_RP-DAi8379g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ccd841332e.mp4?token=XlR2upzkQnJy6Lz8KO7-DGneI1guskO5flbxrruRfSXRv22SQCNLLX-KLWqNI9VKshuY6RHPNww2wlSu3nE1bpSli1I8UBRHLEGrwIHA1xhUH68VMbOOfrYH3OJq_AeLI9Y3iyiQijh9ayJjRhLfzSqFheCl3_IMu370yENTPfngX7mSojBLWpR1rGNwgvZeh9aqvIQo416PzFCJziMeOsybLRAQ-dGarlao5UVIC8Dayf_eaX2dKPidX6VJsm4q1NgKLZa1woTq2dvrigPJR90NZlT8z5p6oOT7pbNluI6nU4hHCB-fH0z5cr8DqckS2XyChOug-O_RP-DAi8379g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ درباره ایران:ما پنج ماه است که درگیر این موضوع هستیم؛ اگر به ویتنام نگاه کنید، آن‌ها ۲۰ سال درگیر آن جنگ بودند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 40.8K · <a href="https://t.me/alonews/138933" target="_blank">📅 19:28 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138932">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">👈
ترامپ: این عصر طلایی آمریکاست و جنگی در جریان داریم؛ حدس می‌زنم بشود آن را جنگ نامید، من آن را یک عملیات نظامی می‌نامم.
✅
@AloNews</div>
<div class="tg-footer">👁️ 39.8K · <a href="https://t.me/alonews/138932" target="_blank">📅 19:27 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138931">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">👈
ترامپ: ایران دیگر نیروی دریایی در اختیار ندارد و توانمندی‌هایش  در زمینه پرتاب پهپادها از بین رفته است
✅
@AloNews</div>
<div class="tg-footer">👁️ 40.8K · <a href="https://t.me/alonews/138931" target="_blank">📅 19:26 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138930">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">👈
ترامپ: آنها چند موشک دارند، اما تعدادشان خیلی کمتر از ۴-۵ ماه پیش است. قابلیت‌های تولیدشان تقریباً به‌طور کامل از بین رفته است. ما بقیه قابلیت‌هایشان را نابود خواهیم کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 39.8K · <a href="https://t.me/alonews/138930" target="_blank">📅 19:25 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138929">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">👈
ترامپ: ایران در تعاملات بسیار فریبکارانه عمل می‌کند
✅
@AloNews</div>
<div class="tg-footer">👁️ 38.8K · <a href="https://t.me/alonews/138929" target="_blank">📅 19:25 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138928">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">👈
ترامپ : ایران الان وضعیت خیلی بدی داره؛ واقعاً خیلی، خیلی بد. روزهای خیلی سختی رو پشت سر می‌ذاره
🔴
کار کردن باهاشون هم خیلی سخت بوده؛ پر از بی‌اعتمادی و بی‌صداقتی
🔴
ولی در نهایت فرقی نمی‌کنه، چون الان تو وضعیت خیلی، خیلی بدی قرار دارن
✅
@AloNews</div>
<div class="tg-footer">👁️ 38.8K · <a href="https://t.me/alonews/138928" target="_blank">📅 19:24 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138927">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b517d36837.mp4?token=Mlp2ODjnxc3mid84NYgD3AUDuv7vgC5qnVPxPlmg2_QbUAKpqtpL3cK7oxnDZyhi4WGFgIve-QgupB-LiSc9qPma0jvm6QJ3DdJMqKB5fuGedycxJOIifRbGzXyN-AzjKlKbhKr1rbcrW1N_P7v_G8CYhPuJF2x-GSP_IcmSzlljCCV-WfEU0fQM3_3l1W0laAGS8G_dAhWI-oAk4JFogmMuYTi9n_Vwyq-HiQfip9iKxlEY7j2Bmh8uDXL-h9h1T-kdCmGDpDCdS2kJPar5jXbdmctrjE6IzsZR-GvK5ty8DHLNHZPAQayS0z3X9LEjyzpugNURAMYMis3_l9dfq6Et1yH09dPeGWUbMVkrBVV1RpFX8GBPCXNmHrptBHjtW7lGNXkkFRxhjwtVCPmu8M3R8BKOp6ivrnYGBXdvyJYlh6ilVrK_Wm8enuHX3GMGtOzmYZxsqz3VH_Jvgq5i-he23WvFMSj6GjK1jrRAnNCiPrkjv48oPUVV-3hUhAify3GYAhe4V2elKeX7Zr1J1rF-VMdujRtMcH-6bH-FsAFX7XbNCHhIFEhWCCIju2o28QvKyjYinNnQ4j-1y8biIBfzkH0_mHHBgPoiAudP_BcmGQVubmI1AIPgpqXOTIhsur6f__kI5IfQamJWBdwKw3o7sFu1iGjAnIqYN-YMzt4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b517d36837.mp4?token=Mlp2ODjnxc3mid84NYgD3AUDuv7vgC5qnVPxPlmg2_QbUAKpqtpL3cK7oxnDZyhi4WGFgIve-QgupB-LiSc9qPma0jvm6QJ3DdJMqKB5fuGedycxJOIifRbGzXyN-AzjKlKbhKr1rbcrW1N_P7v_G8CYhPuJF2x-GSP_IcmSzlljCCV-WfEU0fQM3_3l1W0laAGS8G_dAhWI-oAk4JFogmMuYTi9n_Vwyq-HiQfip9iKxlEY7j2Bmh8uDXL-h9h1T-kdCmGDpDCdS2kJPar5jXbdmctrjE6IzsZR-GvK5ty8DHLNHZPAQayS0z3X9LEjyzpugNURAMYMis3_l9dfq6Et1yH09dPeGWUbMVkrBVV1RpFX8GBPCXNmHrptBHjtW7lGNXkkFRxhjwtVCPmu8M3R8BKOp6ivrnYGBXdvyJYlh6ilVrK_Wm8enuHX3GMGtOzmYZxsqz3VH_Jvgq5i-he23WvFMSj6GjK1jrRAnNCiPrkjv48oPUVV-3hUhAify3GYAhe4V2elKeX7Zr1J1rF-VMdujRtMcH-6bH-FsAFX7XbNCHhIFEhWCCIju2o28QvKyjYinNnQ4j-1y8biIBfzkH0_mHHBgPoiAudP_BcmGQVubmI1AIPgpqXOTIhsur6f__kI5IfQamJWBdwKw3o7sFu1iGjAnIqYN-YMzt4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ درباره اسپانیا:  وقتی اتفاقاتی که در اسپانیا افتاد را دیدم، گفتم: «پسرجون، این موضوعی برای بحث در انتخابات میانی خواهد بود.» اسپانیا نمی‌داند چه کاری انجام دهد و این اتفاق امروز دوباره در حال رخ دادن است. آن‌ها در حال حمله به کشور هستند. این قانون ضعیف، مدیریت بد و قانون بسیار لیبرال است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 38.8K · <a href="https://t.me/alonews/138927" target="_blank">📅 19:24 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138926">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/43705abef4.mp4?token=jUjyqHJWYrU6nG6pHXI4czFKlGEgrj0vkBAP_zO6hIY05nDyTBCv7oqjU6FJOKXYlc5ri9xnozTA_0qRbZRzK2Hwa79A8LXUchrsSegfapsbx619jFmytylzgvub4QGW5zLrD9BEYum40GthgXgrouv9nyeSZYMgfLHaVPolnbbbbTwY6Y5qoBkXELSpwTShtrSZCMG7DbyCMmLSBjvGYeAJBUtoA5239PETceEhLuJWNJIU7JYBN6JW4W3UZQZFYC5LujTmDDmX5wKyhoQ3F46nvBoizMv-arM3ysATXQU24DBG02XWvIGvx8C6Rls-arCrEg7z0hHGwDqUHccLow" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/43705abef4.mp4?token=jUjyqHJWYrU6nG6pHXI4czFKlGEgrj0vkBAP_zO6hIY05nDyTBCv7oqjU6FJOKXYlc5ri9xnozTA_0qRbZRzK2Hwa79A8LXUchrsSegfapsbx619jFmytylzgvub4QGW5zLrD9BEYum40GthgXgrouv9nyeSZYMgfLHaVPolnbbbbTwY6Y5qoBkXELSpwTShtrSZCMG7DbyCMmLSBjvGYeAJBUtoA5239PETceEhLuJWNJIU7JYBN6JW4W3UZQZFYC5LujTmDDmX5wKyhoQ3F46nvBoizMv-arM3ysATXQU24DBG02XWvIGvx8C6Rls-arCrEg7z0hHGwDqUHccLow" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
پرزیدنت ترامپ درباره اسپانیا: دیروز اسپانیا را دیدم. فاجعه‌ای که رخ داد را تماشا کردم.
🔴
به نظر می‌رسد حمله به یک کشور توسط صدها هزار نفر.
🔴
همان اتفاق برای ما هم خواهد افتاد اگر جمهوری‌خواهان انتخاب نشوند، مگر بدتر—بزرگتر
✅
@AloNews</div>
<div class="tg-footer">👁️ 37.8K · <a href="https://t.me/alonews/138926" target="_blank">📅 19:23 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138925">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">👈
ترامپ : قیمت داروها ۳۰۰، ۴۰۰، ۵۰۰ و حتی ۶۰۰ درصد پایین اومده
🔴
هیچ‌کس تا حالا همچین چیزی ندیده و نشنیده
🔴
قیمت داروهاتون اون‌قدر پایین اومده که حتی فکرش رو هم نمی‌شد کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 38.8K · <a href="https://t.me/alonews/138925" target="_blank">📅 19:18 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138924">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">👈
ترامپ درباره کابینه‌اش : این یکی از بااستعدادترین تیم‌هاییه که تا حالا تو دولت آمریکا خدمت کرده
🔴
واقعاً یه گروه از آدم‌های بااستعدادند
✅
@AloNews</div>
<div class="tg-footer">👁️ 39.8K · <a href="https://t.me/alonews/138924" target="_blank">📅 19:17 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138923">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/006aea3c94.mp4?token=bD3cGzgGrhRcQhsumzwDfIeVQl9RIOKfUyUQ0bHey54BUH6xa1DqE7uPNzOs5_Ba1ScGQZcWuKRmot-mYcYFxcYgjLwaHYRLwFSyzqtJmYg6C7B8Xr3l7xtPVf1Ji4euNvLBx-Fg-rKFp9cc-Y_YytCi9Z1Tg5Znbc-hn921ux7iKKqq-vz2vyASS1XRKNBDkPgY-hSVF0GZ4bhpX5nGzH6BSPRtUsqXNUe9zFHzt4ZQ1WHS6swVw33zu3Cjc1jQXQ2UfGobp4UR2J2Wn9dP-uucAfn8qY1aUeN7m2UUM-aGmZu150puzsnIs5moKbKCF-XZyL0kG4N9yS_hmn3pZA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/006aea3c94.mp4?token=bD3cGzgGrhRcQhsumzwDfIeVQl9RIOKfUyUQ0bHey54BUH6xa1DqE7uPNzOs5_Ba1ScGQZcWuKRmot-mYcYFxcYgjLwaHYRLwFSyzqtJmYg6C7B8Xr3l7xtPVf1Ji4euNvLBx-Fg-rKFp9cc-Y_YytCi9Z1Tg5Znbc-hn921ux7iKKqq-vz2vyASS1XRKNBDkPgY-hSVF0GZ4bhpX5nGzH6BSPRtUsqXNUe9zFHzt4ZQ1WHS6swVw33zu3Cjc1jQXQ2UfGobp4UR2J2Wn9dP-uucAfn8qY1aUeN7m2UUM-aGmZu150puzsnIs5moKbKCF-XZyL0kG4N9yS_hmn3pZA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ
:
آن‌ها دوست دارند بگویند: «اوه، کارِ ایران است؛ ایران باید خیلی خوش‌شانس باشد.»ایران مشکلات بسیار بزرگ‌تری از آن دارد که بخواهد نگران مینه‌سوتا باشد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 40.8K · <a href="https://t.me/alonews/138923" target="_blank">📅 19:16 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138922">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cc10781ead.mp4?token=XWbQhun6VSjSJJaUwwA7SORVSx8rg6W3-WtsPfvlFqS5pQCp0QKbVaptIAmT5h4q_mUTEIvnkQ0pVN3TkE9Kq_bSzEiAUDOkEdhWzPQvwaQcuhf9c8oeGjVO5ttCNNQjFDrfRo34woYrGGq_0FxIAkmhTWavuKy_zpZQdeHiVi1ywzSNUh9oSslwB_f16CB60KmmWUEgL_bMKRTtTxAOH5U5NNGgzpw1gJUbbpWFf6PBxUaI_lY4Z-p8EBmGKZnhsEJFZKQSQZMtF1JLKyKsJTaO1i12rkQQlpLXvkGY8Ky1ZQ7_ZDWrFtKpzArNk1MdbxIK_H24NwQX-a2d-sapKg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cc10781ead.mp4?token=XWbQhun6VSjSJJaUwwA7SORVSx8rg6W3-WtsPfvlFqS5pQCp0QKbVaptIAmT5h4q_mUTEIvnkQ0pVN3TkE9Kq_bSzEiAUDOkEdhWzPQvwaQcuhf9c8oeGjVO5ttCNNQjFDrfRo34woYrGGq_0FxIAkmhTWavuKy_zpZQdeHiVi1ywzSNUh9oSslwB_f16CB60KmmWUEgL_bMKRTtTxAOH5U5NNGgzpw1gJUbbpWFf6PBxUaI_lY4Z-p8EBmGKZnhsEJFZKQSQZMtF1JLKyKsJTaO1i12rkQQlpLXvkGY8Ky1ZQ7_ZDWrFtKpzArNk1MdbxIK_H24NwQX-a2d-sapKg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ
:
ما شنیدیم که در مینه‌سوتا یک حمله سایبری رخ داده است. آنها ایران را مقصر دانستند. من اینطور فکر نمی‌کنم.
🔴
من مینه‌سوتا و فرماندار فاسد آن را مقصر می‌دانم
✅
@AloNews</div>
<div class="tg-footer">👁️ 41.8K · <a href="https://t.me/alonews/138922" target="_blank">📅 19:16 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138921">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mk_oYzHDH9ws5ZupwZ3Ar5SMQ0lt6wGYrzDZiCH1LOHT4rrEUTigJSryAmDaFjcnSVsV0o1nKLmw2FZTlDOGp3ZJQdTgb7Tk1Otqg5surucLW6E9MPwASLGJ9eEG0wRYEwDdNyGPtzVAPYGkdYTu2Z9rz1yEv-NWehSe8MxkBsSIEhMDDrOqaxGd20E7d7F2-gtQRF8V_pI5GelzgB3gvXTyaJr9BgQluVJkCRfXx3nwsQbnF1T_Wb5AzTbX_CBRrLZQ97Fb9paK2Bwh8pjE0t42WPexYEOyd_uyKZ90_rLLLVT5vCbUZ_pvO2AEmEDNd98QBoYKlsBjPW_zAnSdMg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
سفارت ایران در غنا: ما به یک کشتی قطری اجازه عبور دادیم، آمریکا آن را برگرداند چون از مسیر ایرانی استفاده کرده بود
✅
@AloNews</div>
<div class="tg-footer">👁️ 42.9K · <a href="https://t.me/alonews/138921" target="_blank">📅 19:07 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138920">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kdGC1d4qEd2q9UEtR_qxuoLPjGNGugEqvL8_qviU26UMyFjAp3B62Nplet9Uig7LTnkAB_g0whR7OkKlRPhLYMMuJV8rEwYYn_db1Rzr4NFxZMKgZCsAOsV4a2NXvv2rQYpqvWRoIsXH_oJWxStmCi4mURAWCQgRvgS1rx0GDUKkUHDPwX_BIvXQxPhH3epVXVOQ9iU_VfSbxVvWGFxOlyeUIGrsqYodFFpRGsRcNWYzKIjYphvUxwAP9_joajqtMkAvxdJztoYvTiZC20d4lkFwXSLRl9y4_NSds2_Ai6aZYOZqlGuvdoJzTupn0077jD6u7Hyj3yX9FwXzZDBkdA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
سنت‌کام: چتربازان ارتش ایالات متحده در حال شلیک گلوله ۱۵۵ میلی‌متری از هویتزر M777 در جریان یک رزمایش توپخانه صحرایی در خاورمیانه.
✅
@AloNews</div>
<div class="tg-footer">👁️ 47K · <a href="https://t.me/alonews/138920" target="_blank">📅 18:54 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138919">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bf5dd02235.mp4?token=tPs5UPs6VmyNaUzYJJVMg89v3gQpsDJw27gWX-_sFrVv2nQjYBV_XgAPfbipt6O6kHTD8QvcpyzmPRVnXU5oz5SsR3DwFLlmGpFagVHAaJNVkaWCXmp0UjvVY2tZXR__52juufbWIC4Rp5Lap_v7MTc3QIoxlnUxdd9V90058P5vuWk8lQJY2F8kr2pcGLNvOr55d3Fi1t0yfMJLWwQPl6PEybyTUppji2SSXJgrAn16K4MVlhXPz-5Q-aMzoSzkH737JVgvOADUbOUctjz_qbbap7ffxx7jVL0iPZ4F8MsTPXrzh-DAFUQJ5-WNq74lNL8HGI9fFvEbrkTakF0iPA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bf5dd02235.mp4?token=tPs5UPs6VmyNaUzYJJVMg89v3gQpsDJw27gWX-_sFrVv2nQjYBV_XgAPfbipt6O6kHTD8QvcpyzmPRVnXU5oz5SsR3DwFLlmGpFagVHAaJNVkaWCXmp0UjvVY2tZXR__52juufbWIC4Rp5Lap_v7MTc3QIoxlnUxdd9V90058P5vuWk8lQJY2F8kr2pcGLNvOr55d3Fi1t0yfMJLWwQPl6PEybyTUppji2SSXJgrAn16K4MVlhXPz-5Q-aMzoSzkH737JVgvOADUbOUctjz_qbbap7ffxx7jVL0iPZ4F8MsTPXrzh-DAFUQJ5-WNq74lNL8HGI9fFvEbrkTakF0iPA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
لحظه انهدام پهپاد انتحاری روسی توسط موشک پدافند اهدایی سوئد به اوکراین
✅
@AloNews</div>
<div class="tg-footer">👁️ 46.9K · <a href="https://t.me/alonews/138919" target="_blank">📅 18:49 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138918">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OVtuodePqyzmPuebm4OaEy2CVTcHdM9sV-xTTSYvvp5wCJlve4WNisuAZsubsqbktOnlStvfjLA4WKCfQJ3FHThvTyettThicW3s9eT_0w_1XetWcon5RcP4ZYGMTSgRtB8YsBeEtygW9lhKJtm_qC5ASY-sAlj78crRsqlv19J-uO9bhEfxFPcHRZXN4zscHOQ-hOzRDAKBTPEr9W2jyAVEgzK0O8QI1v3Hi3-_2nWvwgXiKFrpHIWCYhknrT87IitkSZMGEym4EXoENrvxr13wn-RG0LaUAGFPYCtBsJTy3JX6uVcUzORfM0SmMtn-T2zxOWnfs_53y6uGeTo6Uw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
اقامت شبانه مردم کیف پایتخت اوکراین در ایستگاه های مترو، به دنبال حملات سنگین روسیه
✅
@AloNews</div>
<div class="tg-footer">👁️ 49K · <a href="https://t.me/alonews/138918" target="_blank">📅 18:44 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138917">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">👈
بنیامین نتانیاهو، نخست‌وزیر اسرائیل، تلاش دارد پیش از انتخابات پارلمانی اسرائیل در اکتبر، به توافق عادی‌سازی روابط با عربستان سعودی دست یابد.
🔴
روزنامه هاآرتص به نقل از منابع آگاه گزارش داد نتانیاهو به چند تن از دستیارانش گفته است که پیش از انتخابات به «یک دستاورد بزرگ دیگر» نیاز دارد و منظور او توافق با ریاض است. نتانیاهو امیدوار است موفقیت حزب لیکود در انتخابات، زمینه‌ساز ادامه نخست‌وزیری او شود
✅
@AloNews</div>
<div class="tg-footer">👁️ 49K · <a href="https://t.me/alonews/138917" target="_blank">📅 18:37 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138916">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">👈
ایندیپندنت: گسترش جنگ ایران، فشار اقتصادی و سیاسی بر ترامپ را افزایش می‌دهد؛ این در حالی است ایران توان موشکی خود را حفظ کرده و انرژی جهان را تهدید می‌کند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 50K · <a href="https://t.me/alonews/138916" target="_blank">📅 18:31 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138915">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">🔴
فوری / شنیده شدن صدای انفجار در کویت
✅
@AloNews</div>
<div class="tg-footer">👁️ 52K · <a href="https://t.me/alonews/138915" target="_blank">📅 18:25 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138914">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">👈
الحدث به نقل از منابع آگاه: واشنگتن به حماس قول داده است که نتانیاهو را ملزم به عقب‌نشینی از غزه و اجرای توافقنامه خواهد کرد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 51.1K · <a href="https://t.me/alonews/138914" target="_blank">📅 18:24 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138913">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">🔴
فوری / شنیده شدن صدای انفجار در کویت
✅
@AloNews</div>
<div class="tg-footer">👁️ 51.1K · <a href="https://t.me/alonews/138913" target="_blank">📅 18:23 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138912">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">👈
ایندیپندنت: گسترش جنگ ایران، فشار اقتصادی و سیاسی بر ترامپ را افزایش می‌دهد؛ این در حالی است ایران توان موشکی خود را حفظ کرده و انرژی جهان را تهدید می‌کند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 52K · <a href="https://t.me/alonews/138912" target="_blank">📅 18:21 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138911">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">👈
وزیر خزانه‌داری آمریکا، بسنت : ما رابطه‌ای قوی‌ای با ژاپن داریم
✅
@AloNews</div>
<div class="tg-footer">👁️ 52.1K · <a href="https://t.me/alonews/138911" target="_blank">📅 18:19 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138910">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fd4cb2787b.mp4?token=IVkTmHuelF2E_kFPksBERDTvzI8OHJahgqaa48eBerOmrFVF6i996I90OpGO5QVXPE54MrJj_f3HrOso-Jt4ljdV5MdwfdsayTyKkIfvcrK9a9-B7S_nz_omuqFP6xrSJ34-bgj5Z8nW1nxHqnPMK56Z9iE2IUrAS8ibHeRDui_rVGtQOPguN8nqMTWDjGCmsRfHVhmNeBbqJxNreK9PnnS8WyoebWRuusBRWJNNxniecdkCDTaRBMFXP52eWeBu1YTlqibEAS7xrfbbQIzPw1K-Zfc0mzY3CxuSIoCKyKrKhlMU9oaCW02U3Qo3tbB2iRkWG-VYjbBYPpOgX0soBw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fd4cb2787b.mp4?token=IVkTmHuelF2E_kFPksBERDTvzI8OHJahgqaa48eBerOmrFVF6i996I90OpGO5QVXPE54MrJj_f3HrOso-Jt4ljdV5MdwfdsayTyKkIfvcrK9a9-B7S_nz_omuqFP6xrSJ34-bgj5Z8nW1nxHqnPMK56Z9iE2IUrAS8ibHeRDui_rVGtQOPguN8nqMTWDjGCmsRfHVhmNeBbqJxNreK9PnnS8WyoebWRuusBRWJNNxniecdkCDTaRBMFXP52eWeBu1YTlqibEAS7xrfbbQIzPw1K-Zfc0mzY3CxuSIoCKyKrKhlMU9oaCW02U3Qo3tbB2iRkWG-VYjbBYPpOgX0soBw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ در راه کمپ دیوید است تا با وزرای خود در مورد ایران دیدار کند
✅
@AloNews</div>
<div class="tg-footer">👁️ 53.1K · <a href="https://t.me/alonews/138910" target="_blank">📅 18:16 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138909">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">👈
وزارت دفاع روسیه امروز جمعه از تصرف دو روستای دیگر در خاک اوکراین خبر داد و اعلام کرد که نیروهای مسکو به پیشروی‌های خود در شرق و شمال شرق این کشور ادامه می‌دهند
✅
@AloNews</div>
<div class="tg-footer">👁️ 52.1K · <a href="https://t.me/alonews/138909" target="_blank">📅 18:13 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138908">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">👈
الحدث به نقل از منابع آگاه:
واشنگتن به حماس قول داده است که نتانیاهو را ملزم به عقب‌نشینی از غزه و اجرای توافقنامه خواهد کرد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 51.1K · <a href="https://t.me/alonews/138908" target="_blank">📅 18:10 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138907">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">👈
سامانه کشتیرانی مارین ترافیک: در ۲۴ ساعت گذشته همه ۵ تردد  ثبت‌شده از تنگه هرمز از مسیر ایرانی بوده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 51K · <a href="https://t.me/alonews/138907" target="_blank">📅 18:07 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138906">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">👈
وزیر خزانه آمریکا: محاصره‌ی نظامی و اقتصادی ایران متوقف نخواهد شد و ما در سراسر جهان به دنبال اموال ایران خواهیم رفت
✅
@AloNews</div>
<div class="tg-footer">👁️ 51.1K · <a href="https://t.me/alonews/138906" target="_blank">📅 18:04 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138905">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">👈
یک مقام آمریکایی: ترامپ حاضر است به مذاکرات فرصتی بدهد
‏
🔴
نیویورک پست (از رسانه های حامی ترامپ) به نقل از یک مقام آمریکایی نوشت: ترامپ حاضر است به مذاکرات فرصتی بدهد اما خواستار موافقت ایران با آتش بس است.
‏
🔴
ترامپ خواهان توافق است، اما اگر حملات ایران ادامه یابد، بهایی برای پرداخت وجود خواهد داشت.
✅
@AloNews</div>
<div class="tg-footer">👁️ 52.1K · <a href="https://t.me/alonews/138905" target="_blank">📅 18:00 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138904">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZlHY_MIqa_q4m1LvxBM84_6O4T51lvrH0T7fJalNJ7cdDi99M9RjIxWzuQoLjy3vjUHbreNaPIb6EnWQ45YceXS14VLaMkugogwEb9vpwWK41uDZr-bcvP0ktAUQrlhQ7r-AauwxP9K3CmFqMqSOQhnikR58SgvMKShVHspDWkzochYG5SRdA2e9td57tBBd9bcoG2SiJxLa7EjCEd3q6UL3pGnoUHv91K2Dr_QzVi0ywy0KVChCOkVuDzmlIcQl3ZxpPp8WIqC-erLpTdwdXIrRwL7E8RdtG5tp8hbaFF-PS4IQpQGhy7m64UVUYh58OJ1ZX4F3QKZeZy9gBq5BeQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
سخنگوی کاخ سفید: جلسه امروز کابینه دولت ترامپ به صورت زنده پخش خواهد شد!
✅
@AloNews</div>
<div class="tg-footer">👁️ 52K · <a href="https://t.me/alonews/138904" target="_blank">📅 17:59 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138903">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">👈
تماس تلفنی وزرای خارجه ایران و انگلیس
✅
@AloNews</div>
<div class="tg-footer">👁️ 52K · <a href="https://t.me/alonews/138903" target="_blank">📅 17:57 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138902">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YgPu2Z25DsAPqWBROG-x8BxUI-Btcy-zom6GfWtXcgMb0OX0Q8RsEXq6epoXaBLoC8HlM_GwG7Z5wxJ0IxugNwTTGfSGulzQ_oG3MO0sZWtgwQuOR8LyS3gn5j3zTFn8lmIZXsZi_R5QGv6gYQJNSsAAFaiCfHoiMoV4MTVhyuBk9AiZZDyicq4TKF8w8rPHWhPwsAXwiQfG9RdsKo0FNzWy_lIW91ZfExRa3ixnr0n05Gd6lHladLa3lKD3CbkPr1RjK08N8inFqFXCoGKNLfgT4PbST4EdtK50X2m7nhAeYhrRMJE677JLmoDVS1vuDbUZd8-_GOqScDbThw6yAQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
امیر بحرین: تا قبل از ورود اسلام، ایرانی‌ها در تاریکی به سر میبردند
✅
@AloNews</div>
<div class="tg-footer">👁️ 55.2K · <a href="https://t.me/alonews/138902" target="_blank">📅 17:52 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138901">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">👈
بن گویر، وزیر امنیت داخلی اسرائیل:
پیش‌نویس توافقی که توسط شورای صلح منتشر شده، برای اسرائیل غیرقابل قبول است.
🔴
عملیات‌های ترور در غزه باید ادامه یابند، همچنین تشویق به مهاجرت ادامه یابد
✅
@AloNews</div>
<div class="tg-footer">👁️ 55.1K · <a href="https://t.me/alonews/138901" target="_blank">📅 17:42 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138900">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">👈
دلیگانی، نماینده مجلس: به‌راحتی می‌توانیم شبکه برق آمریکا را از کار بیندازیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 58.2K · <a href="https://t.me/alonews/138900" target="_blank">📅 17:32 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138899">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">👈
کانال 12 اسرائیل: تا زمانی که حماس خلع سلاح نشود، هیچگونه عقب‌ نشینی نیروهای ارتش از خط زرد انجام نخواهد شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 58.2K · <a href="https://t.me/alonews/138899" target="_blank">📅 17:22 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138898">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">👈
ترامپ به فاکس نیوز: ایران در نهایت چاره ای جز تسلیم نخواهد داشت‌‌
✅
@AloNews</div>
<div class="tg-footer">👁️ 60.3K · <a href="https://t.me/alonews/138898" target="_blank">📅 17:10 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138897">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">👈
ترامپ: اتفاقی راجع به ایران قرار است بیوفتد
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.3K · <a href="https://t.me/alonews/138897" target="_blank">📅 16:58 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138895">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/C5lHI1d4DEP0SuBDWMcHWtQ930oU67IvkoZ5nz58ukRNafsmCbyBbRMEJyM0Cm0IMAYpnr7_KYDU9E_y3WCaksEhPMPNbtXP_tw1f7PdcrJV0QpAnd8OftXEsLwtIIrQ_AExefRELItJvlj7u7T5PaorGoil1dmasYVzUshXj6bnpCnXfZlP0cVwQGS1IywlDMVeIFvBL2qlDi8Fs9BMl6Wtxg1-lMPohTrymU_F_AiI4iaQxK7F7j4rk7kdhSWPeBBFhS-wmmrRLSPh-z33EjdwoETyusB7-n8MCk4N2BP4YzYgpbQB_eb7R8orHZwjs7_64ilk31hmv1QL6aLXKg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/M8bD7v3aDIO2nLDFddYsF17niTDUDn6WCr5RYDV3ps_PFJtMhtlv-DSUJgr83M-FnX_Tddw2jRCH4YVVa_hvOzXbjS6s_Im8Fqy7SPkjuW41-dIzGeW1fhdrZDQjHyMw3KmXSGGXyiA3TQ8IolSCvQQRy1YeaH1MuX618ri1AY3XBoVGKKs0lddCij0Iy8er0CC_HuOZQoEW66g7-uRyJmVTEo36Dwb17wB6-3uNVY2cQCUF-L2-BynwZyJ8LLbE-tSk9mZNw-I2ZcQV_YyCR-zV0gllTkCGGEA8dIitO0PxR_kLubgPE7Sv9mLxgcUV8SSvyHJWE4GDDcrwjyKbBQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
مقایسه جیره غذایی ارتش سوریه در دوران اسد و امروز
🔴
سمت راست جیره فعلی، سمت چپ جیره قبلی
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.3K · <a href="https://t.me/alonews/138895" target="_blank">📅 16:53 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138894">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">👈
ترامپ به فاکس نیوز: جنگ با ایران داره خوب پیش می‌ره
🔴
آمریکا داره حسابی به ایران ضربه می‌زنه و ما فقط داریم پشت سر هم پیروز می‌شیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 61.3K · <a href="https://t.me/alonews/138894" target="_blank">📅 16:46 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138893">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b4421416b9.mp4?token=GxoC56_Zm7ICXISnxAR5XkfOdqOPQEYB7edszxOiI9r5s7qWcIWDfbxGG1uTr6srY2rKFxn1ZdTtFTTGrCeLCSzkX7K-cgsyWwLa0EHxELlFZ0s8Qe7q3WbU8ZFydJv4x3OBAIUXP8XbmX9pK5DCXtAv3b4x0Vqw7DCNkSpIhUfeM22RsGQqiRpXoWF-Zfynx5mLwESk73cZdbuiuSRg1aro0GTxd1jbFkbhyFSEohAs-1ywtMWKBwvyeCDnqwlPAa2wnPBw7ZcKDKXHdYJSh_udWezMgmLX8As62lwVuHLqqp6TZeTxE79BcyafF3kFMgRW7fKIJNachjHL5RG5xg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b4421416b9.mp4?token=GxoC56_Zm7ICXISnxAR5XkfOdqOPQEYB7edszxOiI9r5s7qWcIWDfbxGG1uTr6srY2rKFxn1ZdTtFTTGrCeLCSzkX7K-cgsyWwLa0EHxELlFZ0s8Qe7q3WbU8ZFydJv4x3OBAIUXP8XbmX9pK5DCXtAv3b4x0Vqw7DCNkSpIhUfeM22RsGQqiRpXoWF-Zfynx5mLwESk73cZdbuiuSRg1aro0GTxd1jbFkbhyFSEohAs-1ywtMWKBwvyeCDnqwlPAa2wnPBw7ZcKDKXHdYJSh_udWezMgmLX8As62lwVuHLqqp6TZeTxE79BcyafF3kFMgRW7fKIJNachjHL5RG5xg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
مهاجران مراکشی که از طریق دریا وارد منطقه سوتای اسپانیا میشن :
🔴
یه نفر دوچرخشم آورده
✅
@AloNews</div>
<div class="tg-footer">👁️ 62.3K · <a href="https://t.me/alonews/138893" target="_blank">📅 16:41 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138892">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OtLFWuNOiGfuz6c5hC-8PH_6tWenz7mYSiOIsWUx4SP8CV9GAMrSVFWzxbCYiheJRaqZj5I0GE27y0nbLhWo2N2A_jk_ajpwjzEDE-W0NXZ9eq4wNoieHNoSODONoU4egIqf7uTXLUTSpSEJ9pttC-HmX_-L702QTL18wUeT5wY-coXx0MrE3rRBsKS3lNUUJG-ROhD6AX4vL_YynVy_B2hIUFiNuog-uW37vJK57eGAdeKVJFwATONZCmm3u4IaJjnghrSAssVOBg6MR24kBpi1S47rR0Vj33GxqHmHtqpkZsrEPws2MiU1uDBVQTdt622feZ84ACtMfnooAA0gNA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
لوومر، فعال سیاسی و مشاور نزدیک جریان محافظه‌کار آمریکا
از کارخونه تولید پهپادهای
SkyFall
تو اوکراین بازدید کرد
و روی دو پهپاد رهگیر
P1-SUN
امضا زد؛ و یکی از اونا‌ها به عنوان «
تقدیم به ایران»
علامت‌گذاری شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 62.3K · <a href="https://t.me/alonews/138892" target="_blank">📅 16:35 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138891">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">‏
👈
ترامپ در مورد اتفاقی که در اسپانیا افتاده:
واقعاً افتضاحه، ببینید وقتی آدم نادرستی به قدرت برسه چجوری یه کشور رو نابود میکنه. این تصاویر رو بخاطر بسپارید، اگر دموکرات‌ها دوباره به قدرت برسن همین بلا سر آمریکا هم میاد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 61.2K · <a href="https://t.me/alonews/138891" target="_blank">📅 16:27 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138890">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hYXJAL1m1abfKtUHkEWlTTDgazu9ykhKmmsCMBQMt0FJJVGtBEyUSBWNHYmhhiu-mY-62ToDUpMQW3q5uqGznhaS3bwOkrcciE0XunN1p4WZa2YuFSJIGCW1xViAU3cQM00IaOPjo1Mw1v6jfY1gp7E_HdllIUMDzoB5Tr8B2_jbDPpGeSbNGoedSHJLE6EFvKTv1QYiien6q-xnsnZZAlrEWrmFNa5qZUybT-FloEIf5bQCfDKqtCDYvV7iYGOIRLbHUY6QBiPbGUDEywBvDg3XXA5yuelK1lGZ6pMO3vxcHIr44xQV_702skYK3hAop9OuJhGAaLVrB2nhWFcDuA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
سوال و پاسخ هوش مصنوعی
✅
@AloNews</div>
<div class="tg-footer">👁️ 62.2K · <a href="https://t.me/alonews/138890" target="_blank">📅 16:27 · 09 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>

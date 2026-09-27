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
<img src="https://cdn5.telesco.pe/file/uzU0bHE8WD7WLD1RwrUy61HU63NqUuMbybJyaDwe2uMEWy-sY8kJBkNF3wDbNPJlmbjmKYpOMIvSmmjzHwwX0XH6FeII2MwZbr2YgW50TzttE7SKep-pC0Jz8wZPiSDdsvKlAigj6kbmPw09Z42NN9wYTb4jp9es8F7EDBbDmt9bIhbhpJlTArGKpskuqhxmyZXgBU_TZoxZnY-zgtLYoDbEpkqKelZ7Ext0yE9wDoa8PIyTdodov5BmagSUrsTuAMRHNNxbyVoGt5BzLcTSzb1N3s7KqLPTN-aHqUt1N31ZFaMw1fpHCQYhqrcBrk3l0zW_nwIzjdYsq3y_fTt9sA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 فوتبال 180</h1>
<p>@Futball180TV • 👥 399K عضو</p>
<a href="https://t.me/Futball180TV" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 In the name of God; The only popular sports channel on Telegram: All for Iran...🖤We respect the copyright laws and follow the laws, Mr.@Durov...🙏🌹Contact ads:@TivaAds</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-07-05 16:40:44</div>
<hr>

<div class="tg-post" id="msg-107375">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/30882bf1b3.mp4?token=k762ipX5iUAETAmAHeh-zQB-RCl8ZngCE7daZCMapBLU6eT_32QKolJLgvlIUABjSaZ5F0heMt6-5LnHLGzKQv5ekttT6cvWb1NId951xcHNeII95KzpfsjV7Z1LBih_fJF0_tPSNf5cxt0Km3vFrEynJyHX-JwS4WTccie1AZ0HJ4qGPDqA_gB0B_bBZ9QlvsdsMgb7brcb--71n1qYei_RtPHdxENbyXMRI_8Mmd1JtxyPlYrM2wAUsEdwjLi9faOl7sebD0j2Gty7TAAc--8LRi1JDagQcWpS1_MHCZ2UFI57fNHdv0-jhcr1cGErICnVwSuj6veAfMuOVeNStg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/30882bf1b3.mp4?token=k762ipX5iUAETAmAHeh-zQB-RCl8ZngCE7daZCMapBLU6eT_32QKolJLgvlIUABjSaZ5F0heMt6-5LnHLGzKQv5ekttT6cvWb1NId951xcHNeII95KzpfsjV7Z1LBih_fJF0_tPSNf5cxt0Km3vFrEynJyHX-JwS4WTccie1AZ0HJ4qGPDqA_gB0B_bBZ9QlvsdsMgb7brcb--71n1qYei_RtPHdxENbyXMRI_8Mmd1JtxyPlYrM2wAUsEdwjLi9faOl7sebD0j2Gty7TAAc--8LRi1JDagQcWpS1_MHCZ2UFI57fNHdv0-jhcr1cGErICnVwSuj6veAfMuOVeNStg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نبرد دو هیولا از دو نسل! امشب در اسلوی نروژ.
🔥
🥶
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 1K · <a href="https://t.me/Futball180TV/107375" target="_blank">📅 16:34 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107374">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/119aac7582.mp4?token=M6ZGrSzvOlIcxN4nUDyYFM0YcsryLV7-3Ac93ECVggz-ZMKvj_8HRkw8W7E5KU0I5ecmg-zpwyJxzhqIYexrXJK8gn2yo0h0df3Ji-LssVyOvbzm-LMbkZGpwkFTB29FSv3TsixCoslbgGdJwmc-yj4kPlMsgcyGQRcsSDPsFnH5XC6bGKc6KO5FEbw1E7v5sMoSrO_DP9-CAJAvnACbDRFKeWwqL2KK-rZ77WomndkaIYQ2FG8I9t4UanpEuoSeCVMg6oH5qfdp1VR8xscXsqirKBfv0CP-VN0JIUoa4fgqhELLScJsxZxihRAJztLbPiq5Q4OPvAp1_8GO0Qa4xw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/119aac7582.mp4?token=M6ZGrSzvOlIcxN4nUDyYFM0YcsryLV7-3Ac93ECVggz-ZMKvj_8HRkw8W7E5KU0I5ecmg-zpwyJxzhqIYexrXJK8gn2yo0h0df3Ji-LssVyOvbzm-LMbkZGpwkFTB29FSv3TsixCoslbgGdJwmc-yj4kPlMsgcyGQRcsSDPsFnH5XC6bGKc6KO5FEbw1E7v5sMoSrO_DP9-CAJAvnACbDRFKeWwqL2KK-rZ77WomndkaIYQ2FG8I9t4UanpEuoSeCVMg6oH5qfdp1VR8xscXsqirKBfv0CP-VN0JIUoa4fgqhELLScJsxZxihRAJztLbPiq5Q4OPvAp1_8GO0Qa4xw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇮🇷
🇮🇷
دو بازی، دو گزارش، یک تفاوت عجیب!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 3.74K · <a href="https://t.me/Futball180TV/107374" target="_blank">📅 16:05 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107373">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VM6PyoJ2mv1SHLrDgAR8C_vDhVJ68oeAWeuToFDIWWPe7Mutk2SQE1-sVlVZx83tm8mTOsI3zyW0gGlcdThJ8u5LS9KZtBN29Okp0SxalW2J7kTP5WZoxhp24Sz7Xu2e_wm4ARJGneJAhgwrX-TB5HwfCuvOjnxTWv37354CmrJ7HEPlFON5r7eLsvpGCyO-I65wGA_FYRbGiHc7EReAVyf9JxwkA-82dQjGMoWkGxk4Wzg455vrJSmXoBeVuJkvEoUinK9ruGKk9UFzJVoXP8PIwl_v81p5DsFJTLkD_kuUbfqwMi2hIr7TjVqvcZ2ZV6kBBkLMCcEtMu7GgqItIA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🏴󠁧󠁢󠁥󠁮󠁧󠁿
گاتزتا | روبرتو مانچینی در زمان حضورش تو منچسترسیتی دوتا قرارداد بسته بوده. یک قرارداد رسمی با خود باشگاه به ارزش 1.69 میلیون یورو در سال و یکی هم یه قرارداد با الجزیره امارات برای فقط چهار روز کار مشاوره به ارزش 2.03 میلیون یورو!
هردوی این باشگاه ها متعلق به شیخ منصوره.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 5.29K · <a href="https://t.me/Futball180TV/107373" target="_blank">📅 15:40 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107372">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5a4c9c45d7.mp4?token=b1jSAwk6-rTlVZmsEl9XcQ0ZvF1zBsc36OC34PreewmfQzqwqChT8PUQuG8gKhNUhjiuqwXQ54K1BHX8buBwKahAMNa_nQVznfO0jAr2ibLvjKJTCbI3blhuqQsINzfJPOlheXn9_TVurzV-gBQXWmBAkqq3EBGJyRfdAeSRHaJHdmLZnbzeiz4eORVrMmUWkPC1NMIaGnxtpHblMedZW1wjsUKBEOTJobhcNaaTDbo56i3EYmkBxYTEaZmm5C2gqJSuAb4XyFaaysxHCqj_dBF14EV5dn8Qa5_XOts0Rtb9OJ_CbgQfbrBMB34ibaaLjiYle6I4KXTzJ2higXfk4w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5a4c9c45d7.mp4?token=b1jSAwk6-rTlVZmsEl9XcQ0ZvF1zBsc36OC34PreewmfQzqwqChT8PUQuG8gKhNUhjiuqwXQ54K1BHX8buBwKahAMNa_nQVznfO0jAr2ibLvjKJTCbI3blhuqQsINzfJPOlheXn9_TVurzV-gBQXWmBAkqq3EBGJyRfdAeSRHaJHdmLZnbzeiz4eORVrMmUWkPC1NMIaGnxtpHblMedZW1wjsUKBEOTJobhcNaaTDbo56i3EYmkBxYTEaZmm5C2gqJSuAb4XyFaaysxHCqj_dBF14EV5dn8Qa5_XOts0Rtb9OJ_CbgQfbrBMB34ibaaLjiYle6I4KXTzJ2higXfk4w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👀
🏆
یامال: این توپ طلای ما رو بدید بریم.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 6.66K · <a href="https://t.me/Futball180TV/107372" target="_blank">📅 15:15 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107371">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e8c98790b5.mp4?token=h_mHWRIoydC3sPX83Ibexth-3EIL3mXQrm6KHU4limDe7F9gtGY9hhf5e86h-QvhmaWkkH5bWIzbJWu9mI_RAZSdoKL4Ki5Wjs2_6h7g4Ocn1zNydW33Agh9CuPavAcfN2d4zA0OOyveDH-F8Cj0lq6i21Ug8xXNkFViCjQg-w5HSIqb0ioNpPjMy_LWo_LaW6KSt6byuLXcKXFvIJ6yK5FfboPS-E5wovzdrYbDHg7SAShTAs6NhzKJ1kWHKgdLyTy68lrBlt1Bfkf_oiWvP7943fXy7fWQOL15JTFNcuE0BIWzUNAPGsCoXMGjcl-YdjexOLag11NEygvI9lM33Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e8c98790b5.mp4?token=h_mHWRIoydC3sPX83Ibexth-3EIL3mXQrm6KHU4limDe7F9gtGY9hhf5e86h-QvhmaWkkH5bWIzbJWu9mI_RAZSdoKL4Ki5Wjs2_6h7g4Ocn1zNydW33Agh9CuPavAcfN2d4zA0OOyveDH-F8Cj0lq6i21Ug8xXNkFViCjQg-w5HSIqb0ioNpPjMy_LWo_LaW6KSt6byuLXcKXFvIJ6yK5FfboPS-E5wovzdrYbDHg7SAShTAs6NhzKJ1kWHKgdLyTy68lrBlt1Bfkf_oiWvP7943fXy7fWQOL15JTFNcuE0BIWzUNAPGsCoXMGjcl-YdjexOLag11NEygvI9lM33Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
پنالتی که هری‌کین در تقابل مستقیم با یامال از دست داد تا سرنوشت بازی دیشب تغییر کنه!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 8.03K · <a href="https://t.me/Futball180TV/107371" target="_blank">📅 14:50 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107370">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Rb8643-yIqhfBp4XVH7VBg6a3sTf9vRIN2yC7YGLBWUDij7r4LlfjZKhC6KZabbaFOQKJMw7lvgxnujhvRy0iatABhKeFbBpcFt42_xSf4xfg9YfgWdHn951LACP-06rOhffBJ3YvK_2MsknlfFMFGXHuT9cVfE9iOTSaexdM7KqIMifkQ5lhiJdBZ-jG7zRWXHif7S23Z4yhVvzCQHfBj6WnloR73LgKNd4bA6nB0nX6Cc57fh1xqM3LKekEyXa3O_bDp8qjotMJqnTOy1otoev1x-5jEm5VLgSDPb5N6LHY3zlwa41vmuE-VqREvmsbSuHno9ip2kdAIaB2_Zyug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
پریشب نبرد منتخب آفریقا و منتخب ترکیه!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 8.88K · <a href="https://t.me/Futball180TV/107370" target="_blank">📅 14:25 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107369">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VV5fbwxYe7tf0MX0ARYpEAsrxixBC8nlTQ5jFWvGEu_8g6PF5l_F1ndwLhi6pq089FEuXuhdIB1czylaMz0mDOCwcpY9bY_8kzbU515ASj0ykds_9Hupg7xzExDAqlnkLyWJajSA6xXlcSNbITp4Bya4R-AYMFApC5rtETmEg-_JydFG_la684rMeVCQFv9bELO6dthY3B5rmMAUDIvBcXFsezTqP7ybleNXzYj0gGNh-Vx0JwTPpVFo_bQkO-4tU16WK1jIlqEKh0_9v3QGOk7tNdM05cMFX8Y-97Kl_UgxZjLoObxFHK-FffqQMgfeMHB5WSa3KJ10NXaQooIowA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👀
💥
🇪🇸
برخی رسانه‌های اسپانیایی گفتن که اگه سیتی محکوم بشه،‌ ممکنه هالند درخواست جدایی بده و با توجه به نیاز بارسا به مهاجم نوک، این بازیکن گزینه اول کاتالان‌ها میشه!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.97K · <a href="https://t.me/Futball180TV/107369" target="_blank">📅 14:03 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107368">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/t96aphotdODBeZi4G1AawWYpO82yMGMdr0tnrMHsKgt-aTGeppaCV1kJ0cVzA7PzikFw2Ue7TF9N1AS-UusGYxWAnzOL50NMhHcuXwiKzq9HD0py-H03AUI0tDtFP4LMW5hwapD_w7QJccTLqNeEjzyBoqhCK7PRbVVGdLkmFdBbeffQd_2VtFFmA5krRpiuH-9nAfRHbBf77xZ9SW-rhQ1sRCrBsedPqAVoU37hiUIvcmCeOls18be7gsNTsTAqsbbgEio5UGobwhRTCKZkh6MzuDLlEL9odD4UnnwMNARZh3aPRzDbd8J6__H805ZXhKcSfMtEHNjtMMd-HdQxgQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
🇧🇷
نتایج ضعیف برزیل آنجلوتی در مقایسه با سرمربی اسبق سلسائو در بازی‌های دوستانه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/Futball180TV/107368" target="_blank">📅 13:42 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107367">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gEV_tQ3CBnn2R-0bIK_fB0FYIfZ8abBGLiIHtOmDLlIpRU18KjMJRWltNhkKdpKNelEXXH0D38sgd7ZnNcIDR8FQJl22IfxFOSodhxFT-K64QcuQ4HoIsoZtFBIQ4eCTe4Wvu_zqp-h8z7dpUQngDAQ9Seq8Pys68j0a-0Ey3EX64xlQGOlJlEFCh3rI7oq08HCiyIGTiSqVYKTVwrZto_maFRCVG3PAh3zAvTQK8pLYdSLyOX5kIuotiYL2IKXTOROaR67mqmur0_s9OLjMbgNCT0AcF1Ffdo1EuZ9Ql_9IBIyZ5VrA7agOQ97uDR53jy44nlzOUhKb1exHnkLoQw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇮🇷
‼️
اعتراض تند عضو هیئت مدیره پرسپولیس به شایعه قهرمانی فصل‌گذشته استقلال
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/Futball180TV/107367" target="_blank">📅 13:32 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107366">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/39d99adabc.mp4?token=bx1xaaF_otYvodMMD6g63INiLc2_2y8gQCLgCDzOeZGRCefdaDllzK-OW3niMUXGzohey0cS0XywOATV2hVdK2tXM_0IkdqGh0u-guZug5ei7uK8Sny9kSNRlXb3Gj-Zx8GuftRMZNEvdKwqjJmBsM_X8C48k99Zp-kYwfPlMJpRrwZ-j4bGrzQ9Yqa2bqzU5sZw9BdJovj-5ICvNF7hV_K2JiuV6Ajdy-Wukt7LfH5vwPZAft3x4rHnPuMZaZX8R7zvwr-ro2caCwmCTY2j3pTOMhMjm-wnZb-JhkGaz5Dp2SVuU8gnqSyASt3ysMnZ2MrQUgMvlotUUXtQGOlTQUn6MPD6ljX3pEmGQ-1K4HYH_hQ40N0KcUguFbA8ZrTSxAoLjLBChyGUZw-1SIWiHVJM6--27rZJi_ZIsgz0flipe0CHQtk1GX-m8yt7wMlVwh_GygYEv-BzvWKxk82d9dcPUWKYdIFTRS5cL9-pLQ8Oczc4p43iq_poDNZ-xJehpOvcXjfWqHqg8UTn8vAWdaMqszCm9iK55-hbg3ZAjGGkyoP61ZqiPePdn-kwVdWEeOLypWKczhrxJdZfRWD83JiJTE_FHpYZHS88PcNeEqk7fjkgbu5VTOf2M8sNXRjeJqQ53yXg07JPSu4of9KauJBFl20FrY_r8DGzPSXkKog" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/39d99adabc.mp4?token=bx1xaaF_otYvodMMD6g63INiLc2_2y8gQCLgCDzOeZGRCefdaDllzK-OW3niMUXGzohey0cS0XywOATV2hVdK2tXM_0IkdqGh0u-guZug5ei7uK8Sny9kSNRlXb3Gj-Zx8GuftRMZNEvdKwqjJmBsM_X8C48k99Zp-kYwfPlMJpRrwZ-j4bGrzQ9Yqa2bqzU5sZw9BdJovj-5ICvNF7hV_K2JiuV6Ajdy-Wukt7LfH5vwPZAft3x4rHnPuMZaZX8R7zvwr-ro2caCwmCTY2j3pTOMhMjm-wnZb-JhkGaz5Dp2SVuU8gnqSyASt3ysMnZ2MrQUgMvlotUUXtQGOlTQUn6MPD6ljX3pEmGQ-1K4HYH_hQ40N0KcUguFbA8ZrTSxAoLjLBChyGUZw-1SIWiHVJM6--27rZJi_ZIsgz0flipe0CHQtk1GX-m8yt7wMlVwh_GygYEv-BzvWKxk82d9dcPUWKYdIFTRS5cL9-pLQ8Oczc4p43iq_poDNZ-xJehpOvcXjfWqHqg8UTn8vAWdaMqszCm9iK55-hbg3ZAjGGkyoP61ZqiPePdn-kwVdWEeOLypWKczhrxJdZfRWD83JiJTE_FHpYZHS88PcNeEqk7fjkgbu5VTOf2M8sNXRjeJqQ53yXg07JPSu4of9KauJBFl20FrY_r8DGzPSXkKog" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
🇮🇷
على تاجرنيا مدیرعامل استقلال: بیرانوند برای آمدن به استقلال پیام فرستاده است
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/Futball180TV/107366" target="_blank">📅 13:10 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107365">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1582f31111.mp4?token=BESxIK3uAic1BUoxkx-0F2nNBOv1QH6di46U4FkOuKj_8QrfXbhfPLNCdg75A2YVl2k5NJ2VdqstGylDI4puFzgEwqdypXQ9Wi1S8GGgY4Cys8o8nF3sOPpZjOTlKKScvNh4rWHQgKeRPVJsc6q8ib-HlWax4b1pfQBmDxSKI2v5ns9TBpgwhGWnSY0gGYN6qtVLYPlWspJwV9NCDZP5JFZEWQNMYH0BUhx2Lmmpsnn-lrNKg216SKP0At9ITp5VTBInEyBayrZflZTJ6tgIfRIrs-T3ALAoXColCDcV8eFucDyPJHe3qMpMGuAn1ipQdy1jWlYBrfjbmX4KppzBAQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1582f31111.mp4?token=BESxIK3uAic1BUoxkx-0F2nNBOv1QH6di46U4FkOuKj_8QrfXbhfPLNCdg75A2YVl2k5NJ2VdqstGylDI4puFzgEwqdypXQ9Wi1S8GGgY4Cys8o8nF3sOPpZjOTlKKScvNh4rWHQgKeRPVJsc6q8ib-HlWax4b1pfQBmDxSKI2v5ns9TBpgwhGWnSY0gGYN6qtVLYPlWspJwV9NCDZP5JFZEWQNMYH0BUhx2Lmmpsnn-lrNKg216SKP0At9ITp5VTBInEyBayrZflZTJ6tgIfRIrs-T3ALAoXColCDcV8eFucDyPJHe3qMpMGuAn1ipQdy1jWlYBrfjbmX4KppzBAQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جوری‌که بازیکنان آلمان از یورگن‌کلوپ حساب میبرن!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/Futball180TV/107365" target="_blank">📅 12:45 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107364">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8a8b1d7243.mp4?token=sVGjE6FQ5UG6LucerQ_1sPU1YM9R5wzLtlzcmrVgKszFdUotZGEN8_V5tpQfVnRaMNWDCZsfMPFaLQGVm7M0QYbZX13nZX-5kTf-WgjtEyMCFc8WIEWAIYA00GyLCwlHUrAX0o3SS8StM7mIRmPSgDFkOOSV6My-7O-wCJCIIksd8mU-fblpNkVazW8Mbur5nG__N3n1TIU9XkckLpM0Oil7mM3EpUP8C6wPMtTv-oqIUo2ZJCtiERmdLABZX8r0O_UXxXE_nWona0CX3h7EkG9uWEuMXk1xnsoTTpSEe0E9qoBa4ydHx3Fk7JFMwgPa4crdQonz8yqZk-9vWwo3qw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8a8b1d7243.mp4?token=sVGjE6FQ5UG6LucerQ_1sPU1YM9R5wzLtlzcmrVgKszFdUotZGEN8_V5tpQfVnRaMNWDCZsfMPFaLQGVm7M0QYbZX13nZX-5kTf-WgjtEyMCFc8WIEWAIYA00GyLCwlHUrAX0o3SS8StM7mIRmPSgDFkOOSV6My-7O-wCJCIIksd8mU-fblpNkVazW8Mbur5nG__N3n1TIU9XkckLpM0Oil7mM3EpUP8C6wPMtTv-oqIUo2ZJCtiERmdLABZX8r0O_UXxXE_nWona0CX3h7EkG9uWEuMXk1xnsoTTpSEe0E9qoBa4ydHx3Fk7JFMwgPa4crdQonz8yqZk-9vWwo3qw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇮🇷
🇮🇷
❌
تاجرنیا: در پرونده توهین دسته‌جمعی هواداران پرسپولیس می‌خواستیم به دادگاه CAS شکایت کنیم که شخص آقای مهدی تاج به من زنگ زد و گفت از پرسپولیس شکایت نکن
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/Futball180TV/107364" target="_blank">📅 12:15 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107363">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/Futball180TV/107363" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/Futball180TV/107363" target="_blank">📅 12:15 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107362">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/wAYvDbDzFubBlmOPaXMlv_0zo_Ub9MlUrgVW1ZjTyxeN2g2HFT6B2GVI8rcv-AK5I_3W3q5siJYiN8dBddkPvqmyj0P0RrV9KozPvv5dh7wMX4wWdcyBhgEpMinb8L1mRsQlz1dWGNLVy9tR5jjU12IxMWitXjnKzmHoQ1d-ubm86X9caNZjx8A6aZc6YEdIVemquNENiiJ62E0o1nC5Sxn5aLu2G7tcH1z5W6cdzMd4fwYvu7QyOsU3ZAelbhlMi9_uL8mSy683N0wTkeE2wRvwrpoMWI-4Wm5c_E8amBeOh7-9K-04Dkb4W-O49Ssr2dlT1POHe9f_7k6jX8wrqQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🤩
نبرد هیجان انگیز
پرتغال
🆚
نروژ
را در
TrexBet
پیش بینی کنید!
📉
نگاهی به آمار ۵ بازی اخیر دو تیم:
پرتغال: ۳ برد، ۱ تساوی، ۱ شکست و ۸ گل زده
نروژ: ۳ برد، ۲ شکست و ۹ کل زده
🦖
🦖
🦖
🦖
🦖
بونوس اولین واریز تا سقف ۱۰۰ یورو
🦖
بهترین ضرایب بین تمام سایت‌ها
🦖
واریز آسان و امن از طریق کارت به کارت
🦖
هیجان بازی، وقتی بیشتره که انتخابت حساب‌شده باشه!
TREXBET — PLAY. PREDICT. WIN.
https://TrexBet.com
T.me/TrexBet_Ir</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/Futball180TV/107362" target="_blank">📅 12:15 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107361">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6292835767.mp4?token=ksLqL9sm7hmEDY8LHSYTBe2pucYPJ-2T_EiwPoZUV5nma8Fa42ydsVHh85cREZPCYgYUbzpG2UXfVbLKk8M1X4JL4t1cSVLY8zxqSWKSQl8vLhC6ikZPZ4dj-JPDsc7qR-hi_gtg0mZZ6lCG0_HfHJ3b9ZyWN6bo5WVaaUBGA6GwbP4LvOVeZh8y1OUlWM7dgM_kzoEsV9vygQ-3qbN_5-IRbTMGLMKrpUGT6TloO6wlA3U6kT7VDzASk6KsNYtvNpQmM-1XUxCHsHT9hOciTYw4iV2TRW9xbLmW3OqbalG-DrE1u3r4k3Zgvk2wMU8zkQavDR5u6bvUviFQGF3uPggMzDFNk9b1COwzJb_LsNH8_9t5GtG5E0FY_ABYBTc10jMJKgyn5IagWsryiPPbTfrKHFR2iMkF7X_oqCc7G1lk0ofSAZQClOVd6TwRAEA4Ji6hkdhG6OW_bbXWrkWu83PVPV6Bj9NL0VJw_cEHPtNq8bW0fhhJVadQdw-ck3YNcoWqALdztkMUjuh1ENjoAwzcgxnp6NVoV8ayRNldU3mpEkhJXM_5VbLdu1CUHSorml1nk_OhpOIQYmqyjb7wgQhCkseaVENEHDRjQUXm0CDggksiUB09IAoCsM4ZxdqXkSiH1wICGSQhNTLDeg0LohfYmZgrok_NnB6h0LW0AM8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6292835767.mp4?token=ksLqL9sm7hmEDY8LHSYTBe2pucYPJ-2T_EiwPoZUV5nma8Fa42ydsVHh85cREZPCYgYUbzpG2UXfVbLKk8M1X4JL4t1cSVLY8zxqSWKSQl8vLhC6ikZPZ4dj-JPDsc7qR-hi_gtg0mZZ6lCG0_HfHJ3b9ZyWN6bo5WVaaUBGA6GwbP4LvOVeZh8y1OUlWM7dgM_kzoEsV9vygQ-3qbN_5-IRbTMGLMKrpUGT6TloO6wlA3U6kT7VDzASk6KsNYtvNpQmM-1XUxCHsHT9hOciTYw4iV2TRW9xbLmW3OqbalG-DrE1u3r4k3Zgvk2wMU8zkQavDR5u6bvUviFQGF3uPggMzDFNk9b1COwzJb_LsNH8_9t5GtG5E0FY_ABYBTc10jMJKgyn5IagWsryiPPbTfrKHFR2iMkF7X_oqCc7G1lk0ofSAZQClOVd6TwRAEA4Ji6hkdhG6OW_bbXWrkWu83PVPV6Bj9NL0VJw_cEHPtNq8bW0fhhJVadQdw-ck3YNcoWqALdztkMUjuh1ENjoAwzcgxnp6NVoV8ayRNldU3mpEkhJXM_5VbLdu1CUHSorml1nk_OhpOIQYmqyjb7wgQhCkseaVENEHDRjQUXm0CDggksiUB09IAoCsM4ZxdqXkSiH1wICGSQhNTLDeg0LohfYmZgrok_NnB6h0LW0AM8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
سوپرگل‌های زده شده با ضربه‌سر رو ببینیم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/Futball180TV/107361" target="_blank">📅 11:55 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107360">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/psD62gi5zYgQ2Ki3oM557QKUKTwJs9ZXiMcpMXAb4OdA0DbJlze1n8Gi53CbxJ6d4mokO-Tq3CTjkgykPKZHswmVNa7b6au9oSyf-D55njIPB9JDXE8jBVTI-jFfdo0NTdw8G1QWF3UoKllhSf-W6948scG8dOuBc5gEnFWxhMzt6aFk5MO6U-RUoryXEUnF9cnKLqhSb5IziJQAQpBKlm7jVFZtw8LYkIARAa9uQkAOuSJuZnDZAG1OsQSn3XziZxCUc1ovUYQNr2yXTu0I4YtOC2BPOfNeEDgkJadqQio8Xcog75dpTW5zQrIbrg4oonvqwhVoKqtHmc68ZzsKNg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇮🇷
⭕️
علی تاجرنیا: همه چیز برای اهدای جام استقلال تا قبل از بازی بعدی آماده هست و صراحتا می‌گویم به من این قول را دادند که این اتفاق بیفتد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/Futball180TV/107360" target="_blank">📅 11:42 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107359">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EMYVmU4qDodYn0UNNlPcfhKo-ijfs523CEMCoCXIdZ-0myE_H1dnYub8LRZg2twKNJj6Iu7QOFp8KZL8TUphwGX4tPCCCqc7CrnToZDitBWQ4G19wo3mejWUKYQW11wGahMMIngcM_emRdWLqd_zY1SqMU_UNbf0E_4wY9mXlP_x0hQSAThLQDXF3ZcZQJAgDNSNp05Xoez-nOedaF5D1aoS6MjE7tNoTYomfG3vAPdRLQ8ul4y3GjjjXTYDb5rdOEhgY7Zyuv_8cFY58PGZ45SnflpvDrs8Fqs0rLKSW4jdXq-5lcVSwdzNQZlz5wpyGlJZFSP-DMVBM2MC_sCvmg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
لیست محبوبان و مغضوبان امیر قلعه‌نویی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/Futball180TV/107359" target="_blank">📅 11:32 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107358">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/184858d60e.mp4?token=CSj7VusUraKzVP0mbkaTFMbe_Q751m8YnZMe3xrYkrWfli0b_zjqUFANFz-05HgIc7yxIs0mpRfzozeq5c38SbDI-qNrJQMl37x2URStjUZxUPrWznMHTSP8wD-UP6K49I_syGyw4572Q7YDHarMCvJKMnM5YMmFI1mxjObcSL5wCos5qTaIYLAWrApKmZxYEPu_vH2OuhYUkFW0gd2FWdoP5FoMX_xIuvyv0AO0G7qI8TLKHfisTYAJuIoCMkeTkXypaG0feQ5F8dstBD5UxGD5_7TOcP25J58tYuLnKjKfZPuDbIK4U_b2sO3bLlNSz0hiJw7YNMqs_vYkPVayeoWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/184858d60e.mp4?token=CSj7VusUraKzVP0mbkaTFMbe_Q751m8YnZMe3xrYkrWfli0b_zjqUFANFz-05HgIc7yxIs0mpRfzozeq5c38SbDI-qNrJQMl37x2URStjUZxUPrWznMHTSP8wD-UP6K49I_syGyw4572Q7YDHarMCvJKMnM5YMmFI1mxjObcSL5wCos5qTaIYLAWrApKmZxYEPu_vH2OuhYUkFW0gd2FWdoP5FoMX_xIuvyv0AO0G7qI8TLKHfisTYAJuIoCMkeTkXypaG0feQ5F8dstBD5UxGD5_7TOcP25J58tYuLnKjKfZPuDbIK4U_b2sO3bLlNSz0hiJw7YNMqs_vYkPVayeoWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
به‌مناسبت عملکرد قلعه‌نویی یادی کنیم از این افشاگری تاریخی محمد مایلی‌کهن!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/Futball180TV/107358" target="_blank">📅 11:05 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107357">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/22f1db9d0d.mp4?token=uJLrPWa1qgh5fPF8KJQRGf7q_BGQuq6_hzmD7_Xwp3fhAQMsxBNtgaIeCVWq7QyFHBU90Q5dNCcVfeX-oT_ubzJIitcL7wWw9J6wVDd5XzGaJcn_NiumVw10RQcQAIX_P_R2PU6LS00pf2uqclsgPYNwgVBqbEpAqfsYrbW3Ck3JGITE8Kfsq62Wi7vTHqskRrpJEeYphcqgEdWpZg9vZ4ZLtsyZs19Rbg_ihcHZG8Taf6N_wJRUTKSL1qEwXKrsTXEBFP3lYLCLajZ7oQJ6GUcpsbjLXI7ewgpoOeGFqQfvFct9cD-i-weNEbgI1sVxyIEeN1MCGEHibJ7AoO8viQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/22f1db9d0d.mp4?token=uJLrPWa1qgh5fPF8KJQRGf7q_BGQuq6_hzmD7_Xwp3fhAQMsxBNtgaIeCVWq7QyFHBU90Q5dNCcVfeX-oT_ubzJIitcL7wWw9J6wVDd5XzGaJcn_NiumVw10RQcQAIX_P_R2PU6LS00pf2uqclsgPYNwgVBqbEpAqfsYrbW3Ck3JGITE8Kfsq62Wi7vTHqskRrpJEeYphcqgEdWpZg9vZ4ZLtsyZs19Rbg_ihcHZG8Taf6N_wJRUTKSL1qEwXKrsTXEBFP3lYLCLajZ7oQJ6GUcpsbjLXI7ewgpoOeGFqQfvFct9cD-i-weNEbgI1sVxyIEeN1MCGEHibJ7AoO8viQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👀
❗️
سوپرگل‌های بازیکنان ایرانی در تاریخ به چلسی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/Futball180TV/107357" target="_blank">📅 10:40 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107356">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/805925ad6b.mp4?token=GugWogvlmZV3eYxmLCMdvkcNjhVVTBa58JNaMOS_fp31bV7RlGcfDPe07btYWOH070hF6f9VQOZGw4lT5sCsh8M7qouy20JMqjazMHjHx1pWB9Z2KRAkK4xIy8TQ6b2foRR5Ou5VjMnGneFwUPc4cHq5Vv-bTWmmYnDLMgeZMVDN5589mu3Q7SMRZz3D5Uezp5wS2vO8ajH8ku_R3GixC4yfuyjo--Zj5kbm4BTCWuAbiAl_tbOTguTynr0s2RY7XweeWE-XhYMmx9dXpgQjEv4wMh0oSIaR_nPSqbM6Bz0EvAxQTvSJv96vaT6hQon7be8xElpG6qASBP1F3wZq1A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/805925ad6b.mp4?token=GugWogvlmZV3eYxmLCMdvkcNjhVVTBa58JNaMOS_fp31bV7RlGcfDPe07btYWOH070hF6f9VQOZGw4lT5sCsh8M7qouy20JMqjazMHjHx1pWB9Z2KRAkK4xIy8TQ6b2foRR5Ou5VjMnGneFwUPc4cHq5Vv-bTWmmYnDLMgeZMVDN5589mu3Q7SMRZz3D5Uezp5wS2vO8ajH8ku_R3GixC4yfuyjo--Zj5kbm4BTCWuAbiAl_tbOTguTynr0s2RY7XweeWE-XhYMmx9dXpgQjEv4wMh0oSIaR_nPSqbM6Bz0EvAxQTvSJv96vaT6hQon7be8xElpG6qASBP1F3wZq1A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
سکانس‌جالب و وایرال شده از مرد سه‌هزارچهره
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/Futball180TV/107356" target="_blank">📅 10:15 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107355">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">‼️
⚔️
برخی از لحظات خشونت دیگو کاستا ستاره سابق چلسی و اتلتیکومادرید
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/Futball180TV/107355" target="_blank">📅 09:50 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107354">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UUlw5ZekvoL6kKMu012FrF2n0FoT3CqsvYzmRXfiT4kaRZLvm7OCXDNvPjOa1-me7plobyOV130Usox6NJKjpFXgA4Q2NN18YJZwEpFiaxYeDfPzi-Q98Zft-LaqQOYlakRxBsCYZLxvvEKxSxGgyeZ2sT2cAdjiMrakczBX2cN0Ufckuj5t1ZlwKbnahfDEUW-tpXmEjvytWfJDGkjBU83BAZIn_SuiLbC03W9_epxdN7Qy7uxBKWFWSWjTPJekR8bVRE6rraNn50QqlBMSmTc5hf1DCtWArnLaH6LUetENZJpL7WKKreX8qk1-HPogE0kZILig082ay6QCDQG3Fg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
📊
ضعیف‌ترین عملکرد‌های تاریخ رونالدو در‌ پرتغال که بازی مقابل ولز در جایگاه دوم قرار گرفت!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/Futball180TV/107354" target="_blank">📅 09:25 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107353">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8bc355e5eb.mp4?token=g_W40jbL5a7Lrj_J3iLos-bR0m7CJQNk9r352z84s4lMkKxJMZxZEm7IrY39y9YzH-ZwxfnXo45XJc2k050uGlYxqlB_MXVvYQrtiafC54lcyyWJHkQnxdDBjdxYmhC_iGgKZbQ7A7EoOtHC54P6TyoOCOXK-xqI3X0PP2hp8fmuNr2LQ9ayyTFrc9DSoJhAoI3HWo1eP6LU_nSbL5nYUZJWyPgpms8J2lMRf-I4EDLLuAKXoXVEbLFfRNwE5aVRwvFYUODYMI-QBF300fr0psjr4_27IKoNjKqI5AaEA9ez0_Nf3rXmxOHfaOPRJYgkhruXcGdTp3RO2l89g307-Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8bc355e5eb.mp4?token=g_W40jbL5a7Lrj_J3iLos-bR0m7CJQNk9r352z84s4lMkKxJMZxZEm7IrY39y9YzH-ZwxfnXo45XJc2k050uGlYxqlB_MXVvYQrtiafC54lcyyWJHkQnxdDBjdxYmhC_iGgKZbQ7A7EoOtHC54P6TyoOCOXK-xqI3X0PP2hp8fmuNr2LQ9ayyTFrc9DSoJhAoI3HWo1eP6LU_nSbL5nYUZJWyPgpms8J2lMRf-I4EDLLuAKXoXVEbLFfRNwE5aVRwvFYUODYMI-QBF300fr0psjr4_27IKoNjKqI5AaEA9ez0_Nf3rXmxOHfaOPRJYgkhruXcGdTp3RO2l89g307-Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
⚠️
آیت نوری مدافع سیتیزن‌ها تو بازی الجزایر مقابل زامبیا از دستور کادر فنی برای گرم کردن خودداری کرده و به همین خاطر از اردوی تیم ملی الجزایر اخراج شده.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/Futball180TV/107353" target="_blank">📅 09:01 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107352">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1e5fa478dc.mp4?token=r-YQUN1t7hA1VCZ-dw6JLh6f8vu7HTZPqw9f0ojUZaTxmipwLDrHETatjf4E833MjYmA_ztpjgevpQ_U6clX-oOF9Phok-yvk75pQg0i3D9-L8QlmUUBf7LnIaYLsRcf074vi41VsG7ClyyXcqk0n-qM3O1Veka_9JuW50D7npX5VwRl9tBdKH3xZT4fIFX3gQNDnJzSa4Ohh6V1X2WS_HIs2ZlZbgV_rJmS_12V5AWPx6odAJpsvpET4d2XX6UlQuBgQ0nM22WCqnDhWQLk7VjT9ssBrROgwMpMif761gDtlo47YWU7k5v9TqrxPW9tN4ulVZccJYdNHbQ4-NlBUQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1e5fa478dc.mp4?token=r-YQUN1t7hA1VCZ-dw6JLh6f8vu7HTZPqw9f0ojUZaTxmipwLDrHETatjf4E833MjYmA_ztpjgevpQ_U6clX-oOF9Phok-yvk75pQg0i3D9-L8QlmUUBf7LnIaYLsRcf074vi41VsG7ClyyXcqk0n-qM3O1Veka_9JuW50D7npX5VwRl9tBdKH3xZT4fIFX3gQNDnJzSa4Ohh6V1X2WS_HIs2ZlZbgV_rJmS_12V5AWPx6odAJpsvpET4d2XX6UlQuBgQ0nM22WCqnDhWQLk7VjT9ssBrROgwMpMif761gDtlo47YWU7k5v9TqrxPW9tN4ulVZccJYdNHbQ4-NlBUQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
🇮🇷
حجت کریمی: قطعا انتخاب سردار آزمون در ایران، تراکتور است. به هیچ عنوان دنبال جذب اوستون اورونوف نیستیم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/Futball180TV/107352" target="_blank">📅 08:04 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107351">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/Futball180TV/107351" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/Futball180TV/107351" target="_blank">📅 01:19 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107350">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MIR9rDfmWiQ0B5D7XZOBxHhVMfZtEUfJNPVnzwZTshWBbQSVjjOExn9_F-QFnOCOGIfc24OfDYqfh7ZTpx3XqaUWukJ8UdRce9GXTgmErF_PK8Mw2MyT-CHAdYOPSA5NaA6kbH6k_ZeBpRfrIVpbRMmB9kjO80mt5mrPqlo50LF0rTfp_rjQ6fBth5fXlx_6DAyXpIbSInTWPEaS79XSCYQbc9iYDbIwAjQhSYhWWEYaTjLhmqCULLY6mBeOq4x5OuWvRELpAKcuyFop2rJkcvpV3HoxcDMSMcC7FYvFwjO4nfk9_8vpZgS7XbIxhZHC_ogZMiSiCkIN_-CnwMOQMg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🦖
فقط یک بازی از میکس‌ت لوز شده؟
پولت برمی‌گرده!
میکس می‌بندی، هیجان بالا میره، اما یکی از انتخاب‌هات خراب می‌شه؟
با پیشنهاد ویژه
TrexBet
، در صورت رعایت شرایط، می‌تونی
۱۰۰٪ مبلغ شرطت رو پس بگیری
.
همین الان وارد سایت شو و شرایط آسان‌ش رو مطالعه کن!
💰
🦖
🦖
🦖
🦖
🦖
بونوس صدرصدی اولین واریز
🦖
واریز آسان، برداشت سریع
🦖
سرعت بالا، طراحی حرفه ای و تجربه ای متفاوت
https://TrexBet.com
T.me/TrexBet_Ir</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/Futball180TV/107350" target="_blank">📅 01:19 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107349">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/b1xZdSTQ3vcDjbgDz4IzxISuVmuRP_2EXw-mBFZBZ9SOKOBGOB8ODHGADmA0ZnH_RuZ11DugO9ffsG_0Acju_s9ousQIc1_6JIfgYMqvFELiSu152aMrUwstfwOFUJ9QtcIh2_3dM3vH0K4pjAmVzSeyDzkFelzRc-olxWrh6pe1a6I3buO1ArW0ZNCvhztDzjSPVpSqSfXzjNBL3NzNrFgVyVe7SKeR4SVUkXBnGK3PHrHffc7JkuIblAn4nZQyKsAsnDDfRarna6oCfZOWpqbI3c_R0rZobj6HnE-TCn66OJa55PYKXncp_nCaUQEfSYLT1rfMsBPzUZp6gMsTsw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
‼️
گوگل رسما ایرانیا رو تحریم کرد و از این به بعد مردم ایران دیگه نمیتونن حساب جدید جیمیل بسازن
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/Futball180TV/107349" target="_blank">📅 00:46 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107348">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Q929dFC8TvUw28mfwYdb6qAntmtyaMKfnOQbyi7Mrn0kyGI6RmSYf9xSH_5J7alfwH-oZI-fgN43I8UcDBmZtKOcKjip26NpLu0n7i5otaJMD__JfZlYwCZYJrEssSgIsip01jgexJf89bIlDSJkoMxfE6WlOojpQ72qeRuXDg9hH2r9t1tUnTf-cbCK_k3bsNAoQOzIcuRlVGhXPwE9pTX4YC1ZtO9hRD79Bx5MKWJZ3pe4198oqoBJYGtecSdXDlESw4KnW8MiVYAaz1Vrk0mblz2JghF9dRi9sVilt0q32CTtO8_fAPwZd_6eCPj1S6f5MZ28l4ETK3b2FLxz3w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
🚨
📊
🇪🇸
فابیان رویز تا به امروز هیچ بازی‌ای را با پیراهن تیم ملی اسپانیا نباخته است:
‏
🔻
51 بازی؛ 36 برد‏؛ 15 تساوی؛ 0 باخت
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/Futball180TV/107348" target="_blank">📅 00:31 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107347">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">🚨
🇪🇸
🚑
رئال‌مادرید اعلام کرد که ابراهیم کوناته دچار مصدومیت شده و مدتی از میادین دور خواهد بود. به گزارش برخی منابع، این بازیکن به دیدار ۱۰ اکتبر مقابل ویارئال خواهد رسید
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/Futball180TV/107347" target="_blank">📅 00:28 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107346">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VIWdD2AykCSdNiO0pwY1AMOVhJYoxqNHSIp2onPifZNN8VBEWyNp80oN5x2tAGsy9oo59K2YIj9xFe8rUr-QT_bZ0FJTnIJlBJEfMHs27DxCRwJRGtDSUItLQ6SfRhZKmN4vSMDxLM1GrX22iymoc2AVwvk3lXZqKIpuwPTm7_yC83L4DKt9_TSRzMOiIN_67k__OldZbWtqmRsEuvsBrRMnElg7P85ASWNQo5AiopSXuUW9TJJ2aBCAXMr59kFrZUPQeu9vcQGPJuxvMa5c_LyAwZ0QCFtUfg5EATQI-1m0zEDG5gIKvJP3glxIipx7Jmh7RU5I9OQlOxxP78I5_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
🚨
📊
طولانی‌ترین روند عدم شکست در تاریخ تیم‌های ملی:
‏42 مسابقه —
🇲🇦
مراکش [2023 و 2026]
‏39 مسابقه —
🇪🇸
اسپانیا [2024 و ادامه دارد]
😳
🔥
‏37 مسابقه —
🇮🇹
ایتالیا [2018 و 2021]
‏36 مسابقه —
🇦🇷
آرژانتین [2019 و 2022]
‏35 مسابقه —
🇩🇿
الجزایر [2018 و 2021]
‏35 مسابقه —
🇪🇸
اسپانیا [2007 و 2009].
‏35 مسابقه —
🇧🇷
برزیل [1993 و 1996].
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/Futball180TV/107346" target="_blank">📅 00:26 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107345">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/R7pLV58Iscxqc4yMYOM5NUIXiY0dIEoXsDPdnlg_lEAmFKC1BQ9RM9YgA8PiOuwMxH0qmpqJxKYWENd3hSIUac7vLYWF1uEERRfCid5iKaATtc_q9FkSySsLWTCadgWmLvI9fJTbSZBjb0GYjhpgLVXO-aX8Dz7CmhUwHe5rX0SYVcHkg8YgJmAKEUDnNOoYG7EbqQP04MxOEA17kFRstkJrct5AZ88O5T6UeRLAcHvQtJOjOrVkfWaLJ0HMPhk3kX_FNyWmHFmcIDcDCjqhqC_fL5KBBZ2CClknHBpiR6AIYbG9UKkn4ECqbHudT_12hc4HUVMikYehJGgMweD-tw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇺
🇭🇷
کرواسی در شب درخشش لوکا مودریچ ۴۱ ساله مقابل جمهوری چک به برتری رسید
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/Futball180TV/107345" target="_blank">📅 00:15 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107344">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GHxzLENkfwDH3FwIwt70CLGBLkeH0hslqNQLvgXcSdlIZygDC35D80jZu4-G2hu6aCLDOvpBLSLRz9ijppR0wurJBy0Tbn3pqw-j6iiKTivSWtWGsrWuYSwZHOOyEdk3HzdHZBTMQGFPfQLvfowkmQ1zTCOHA4LyCJQ-hAhw9PNcotSodSrx0jwiwx-2DRu2CBKAU8BXUvj1r0jhM6BtgqGqgB12XQb74N-xvO8vu5nXyQBAk1vSF8nzH889CMZUQkuZfYnBOnUHGu6ZB67ZUlmW_UkM3eCAZpmuFIDH2ZKcYuMOO28bcy2NM4eRfE9NIU1Rg7_M_L3Cb1PlJASrMA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇺
لیگ‌ملت‌های اروپا؛ قهرمان جهان در لندن انگلیس را از پا در آورد؛ یامال بازهم ارزش خودش را در زمین نشان داد!
🇪🇸
اسپانیا
3️⃣
-
2️⃣
انگلیس
🏴󠁧󠁢󠁥󠁮󠁧󠁿
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/Futball180TV/107344" target="_blank">📅 00:10 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107343">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/494ff796bb.mp4?token=ha63Y4ZMQhdXa6rx5BAvEv3vQSXWO6zbskT6-dEnYm4nTyGCs6W2dNvkU-4S7VKi7WZeHGfXzM3pIn1AntqfMWMkwdeOVCk9H_-zakD96Ml9zjncHT9-xkipwCGvF6Z2GT7glJwqUTOMuIySSQu6w2VJ4kr8Pg45UYPa8C4H8GjHzhU4TKbLYDMbQkNnadTMX5Ig8Kz3dWech5dRF4raUPvBoYJMmpSkNPDEgxgKp89dcF_2Xr5WTrig2eNpLiBz7XEkFxFwB3gGKx4oG3co6qKCAInajv_71mySTq_l7zmDrXRf7eK7ZXptujaBi92Z3CCM4QTraPfFFxZTD2ks8w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/494ff796bb.mp4?token=ha63Y4ZMQhdXa6rx5BAvEv3vQSXWO6zbskT6-dEnYm4nTyGCs6W2dNvkU-4S7VKi7WZeHGfXzM3pIn1AntqfMWMkwdeOVCk9H_-zakD96Ml9zjncHT9-xkipwCGvF6Z2GT7glJwqUTOMuIySSQu6w2VJ4kr8Pg45UYPa8C4H8GjHzhU4TKbLYDMbQkNnadTMX5Ig8Kz3dWech5dRF4raUPvBoYJMmpSkNPDEgxgKp89dcF_2Xr5WTrig2eNpLiBz7XEkFxFwB3gGKx4oG3co6qKCAInajv_71mySTq_l7zmDrXRf7eK7ZXptujaBi92Z3CCM4QTraPfFFxZTD2ks8w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گل‌سوم اسپانیا به انگلیس توسط اویارزابال
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/Futball180TV/107343" target="_blank">📅 23:52 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107342">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">اویارزابالللللل</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/Futball180TV/107342" target="_blank">📅 23:50 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107341">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">گلگلگلگلگلگ سوم اسپانیا</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/Futball180TV/107341" target="_blank">📅 23:50 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107340">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6a0a10c6d7.mp4?token=APdzDacQIyZh_xWhvp7HvXpvnZFL9pz6Elsxw9YltBKJmhlilrw42tmgfSC_pcToxkicqWKm-nyvBdiKE3va_oJfvnxKEajdy3VG0TNvqEYZ0BCcpq5HV4M9i3J_a4hZdstkq1IqMMtPYDaU0IACPl8C878m8yUIEYvSIjgIWetFkeWRm1MoH6CqSKpUTKY5Vu97JvPBLddYxtzPr-qgm5MDg-rd8jpOwqqBBhw0aG5zJ50uFcu40CI7zSO-GRu7iQVkh-FgvlqGBK-xPYAVBugdeEj8PVjTId7giTE9rZGfEXFFosuNnUlwGDLRcZDb1bAWFQLSncFBLbuApcYmXw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6a0a10c6d7.mp4?token=APdzDacQIyZh_xWhvp7HvXpvnZFL9pz6Elsxw9YltBKJmhlilrw42tmgfSC_pcToxkicqWKm-nyvBdiKE3va_oJfvnxKEajdy3VG0TNvqEYZ0BCcpq5HV4M9i3J_a4hZdstkq1IqMMtPYDaU0IACPl8C878m8yUIEYvSIjgIWetFkeWRm1MoH6CqSKpUTKY5Vu97JvPBLddYxtzPr-qgm5MDg-rd8jpOwqqBBhw0aG5zJ50uFcu40CI7zSO-GRu7iQVkh-FgvlqGBK-xPYAVBugdeEj8PVjTId7giTE9rZGfEXFFosuNnUlwGDLRcZDb1bAWFQLSncFBLbuApcYmXw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گل‌تساوی اسپانیا توسط الکس بائنا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/Futball180TV/107340" target="_blank">📅 23:40 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107339">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/ed28ae0d69.mp4?token=YfJEg4jM0VHylAtLucXHToDEukNrU-L0mdZkROPKie9TsOxcSVpoSAxgL4bzQK2hOitTm0kCOm06XEAkWIDG2xlBrydo6bxCGvZdSLfvSowOPX2c47ar_4lyvBrudgHNVPDIhbQgHtkkQOH_v5jOvXs-5nc973jbmFKcyExUcMEM8gFU1vRTBKkZQUkRG2N0_konT1QzhOOlbDfyahfupUImrznj0zl__UNY_zvHrVws3JLDN5RpG4TAwjeK67wd50NdTae0P05xn_BGnVIpvw3Xu5ywSxN3imlZY_JdUllzOv9ieu7UNcy3Ab2FzE6dA0EpOUbd5c3JTRoSRu137w" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/ed28ae0d69.mp4?token=YfJEg4jM0VHylAtLucXHToDEukNrU-L0mdZkROPKie9TsOxcSVpoSAxgL4bzQK2hOitTm0kCOm06XEAkWIDG2xlBrydo6bxCGvZdSLfvSowOPX2c47ar_4lyvBrudgHNVPDIhbQgHtkkQOH_v5jOvXs-5nc973jbmFKcyExUcMEM8gFU1vRTBKkZQUkRG2N0_konT1QzhOOlbDfyahfupUImrznj0zl__UNY_zvHrVws3JLDN5RpG4TAwjeK67wd50NdTae0P05xn_BGnVIpvw3Xu5ywSxN3imlZY_JdUllzOv9ieu7UNcy3Ab2FzE6dA0EpOUbd5c3JTRoSRu137w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گل‌دوم انگلیس به اسپانیا با گل بخودی کوکوریا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/Futball180TV/107339" target="_blank">📅 23:39 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107338">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/8bcae065f2.mp4?token=saa9cjiee52UmFajFpQAjHXtirwqtbTPgxxd4KaCs1sGOIcjjU1m63-sosuQ7v9RMGuWoBqsYAyCA9mYas2UipHJDcQ9lDO-4dOZFYcKNNqxq9AFVUA1V1lT1HQbEe41uyAL44veDCHPEAvdMpWJhJTRjJNyySk5_4N6Y1dLylWolfunJ04ukgrOMLLzd-cT1iJ5jhkYwDN5jn1CI669XgVCdbyezPqPIrt8QT3Ki9xrxqEIVYGo06YwGRXHP7GNEyyvZpE_kx7qJoe5kfby085tBld_3y_z1HLtj6UWprrCBG-hp7stc8B_z2d18Uq2Bws09Sxr_OIwFIUmn6voig" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/8bcae065f2.mp4?token=saa9cjiee52UmFajFpQAjHXtirwqtbTPgxxd4KaCs1sGOIcjjU1m63-sosuQ7v9RMGuWoBqsYAyCA9mYas2UipHJDcQ9lDO-4dOZFYcKNNqxq9AFVUA1V1lT1HQbEe41uyAL44veDCHPEAvdMpWJhJTRjJNyySk5_4N6Y1dLylWolfunJ04ukgrOMLLzd-cT1iJ5jhkYwDN5jn1CI669XgVCdbyezPqPIrt8QT3Ki9xrxqEIVYGo06YwGRXHP7GNEyyvZpE_kx7qJoe5kfby085tBld_3y_z1HLtj6UWprrCBG-hp7stc8B_z2d18Uq2Bws09Sxr_OIwFIUmn6voig" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گل‌اول انگلیس به اسپانیا توسط گوردون
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/Futball180TV/107338" target="_blank">📅 23:39 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107337">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">🚨
🇮🇷
⭕️
علی تاجرنیا: همه چیز برای اهدای جام استقلال تا قبل از بازی بعدی آماده هست و صراحتا می‌گویم به من این قول را دادند که این اتفاق بیفتد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/Futball180TV/107337" target="_blank">📅 22:35 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107336">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c757a44e62.mp4?token=LQmiKNiLjQDTpOeKW21ADsZCljmtP-j32XHhI7l3n6DHFrj6Du1VNjx4MxSxNtzZW0CDj4DVAIxzQulwoT98Rd99IAQV-vjlbMVw0_9lgtHiaK4ffasmZq_8u9ZvEXnMZMVhqFGAB_RSckJ2657myA5tK6PLksY6Tg7F5I5BSb7GrFwKuxzVgs4aLDnmJTapUYPJlZND7o_veB5CKfoSaTOPHudPQKfh5Pk_LupetEx5FW4Lm9keh5zIlnJlLMyq0tEDYhqUseAhFysghhCRRm4ZNHHC4fYkopnvxO1HJ0XN2RUEnop0FSIsR_8dyB9lAdB-o8YbMOxEU9RQFJokKw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c757a44e62.mp4?token=LQmiKNiLjQDTpOeKW21ADsZCljmtP-j32XHhI7l3n6DHFrj6Du1VNjx4MxSxNtzZW0CDj4DVAIxzQulwoT98Rd99IAQV-vjlbMVw0_9lgtHiaK4ffasmZq_8u9ZvEXnMZMVhqFGAB_RSckJ2657myA5tK6PLksY6Tg7F5I5BSb7GrFwKuxzVgs4aLDnmJTapUYPJlZND7o_veB5CKfoSaTOPHudPQKfh5Pk_LupetEx5FW4Lm9keh5zIlnJlLMyq0tEDYhqUseAhFysghhCRRm4ZNHHC4fYkopnvxO1HJ0XN2RUEnop0FSIsR_8dyB9lAdB-o8YbMOxEU9RQFJokKw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇸
گل‌اول اسپانیا به انگلیس توسط لامین‌یامال
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/Futball180TV/107336" target="_blank">📅 22:24 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107335">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">اسپانیا ییککککککککک</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/Futball180TV/107335" target="_blank">📅 22:22 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107334">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">لامین‌یامال زددددددد</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/Futball180TV/107334" target="_blank">📅 22:22 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107333">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">گلگلگگلگلگلگلگگلگل</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/Futball180TV/107333" target="_blank">📅 22:21 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107332">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CtcNZAI963K7MzrPiPpLdT3qG26a6hTqhujuR4jEHQebgpPGXQuDjw7ZHs7fkMFrizmlHBWmiTZu7CNJ1-rlKyrrSkngp7kbwTR4XPMCaOyc21Spn1UkHkDHt0JafQXfMprk88GLqJjIrx3jTHu1UTT4NCt1hf8f_RI6zuXUq0JB4hlw_2pdqmMeJcnQNAp0oAlak1EqvlAvUjNN-tTxuquEtRFJqWbkZPzC0H0402d82wLynhlsYFZCiHlscXA6a3xzqkJrYUsDphlTPB_cbhVKMzZd66ENlIc0cgO2HGhyPBo-IKgZmZM7h4c2D_FgyYXtPa7pBK7dV5TaBLKduQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
✔️
شماتیک ترکیب اسپانیا مقابل انگلیس
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/Futball180TV/107332" target="_blank">📅 22:09 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107331">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">🚨
🇮🇷
تاجرنیا مدیرعامل استقلال: همه چیز برای اهدای جام استقلال تا قبل از بازی بعدی آماده هست و صراحتا میگویم به من این قول را دادند که این اتفاق بیفتد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/Futball180TV/107331" target="_blank">📅 21:40 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107330">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ka0cDNi82DDVPfPiKGyUIOsrg-9DAbvXmEWwPXuF--rn6h26mw44kb8z2AUI9nBved4G3Av2mqys22dmZLo92HsjeKjHoGQhM0Mx5UBR5S__mGbVgzmXyG87a0z8q60oVozZ6dqc2Qr7P_OiGa0Zc0HL8BO7lFht013RJfyUyW6UBcvlbRvwdkPmiV-10_LYwlOp8DnG5XKj_bOSQYYxSPPf92CRXyKE4aaxG8OrftPL6-dMToTSqKKXNqeVPspw8rGBNv0SunShjZFJcEeygKEs-sA8GDHgc7-NpwIENuP9Mb3cv2il4sHle-4S0LU3sVd9LRk01z3f_SEiDHxOqA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
✔️
شماتیک ترکیب اسپانیا مقابل انگلیس
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/Futball180TV/107330" target="_blank">📅 21:04 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107329">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BwIxbrehJEtu5r4ydtTEPZLqSaOYGQLlaMz9-50iMQJ0btbcF9715q466Iv8lOkOwqkI3WS1l-VczskTVEZL5foNENNIZdWIIHBWZUPjfykko0t7jUSSzjR4jAYiAz3sP9o6Lc3NhJaM-nGtvQbgv0qDGgudRltSYUGQJCdSdfbcJSdRDNmVGodRGXFtIX398Jd59c1pmQA3xMNdCH2pzHTbaJJI6BnAHwfVkgmhA25ewIFC9SEyZ12t70VeEBzQvTG9t2rCgJPzgUN8kxl7zQVGfzPRKh9_LoaoUR_OHr8pVXRfntn1-mwKcwX-uIqYjwVAvkwZv0sG_GTRlv4FuQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
🇪🇸
🏴󠁧󠁢󠁥󠁮󠁧󠁿
آمار تقابل‌های بین انگلیس و اسپانیا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/Futball180TV/107329" target="_blank">📅 21:02 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107328">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jV7WHRDf36BDZhmJgbxph6oBHysEIx-Ep8j0Nm9WcKROhJqbZununRezyHQyBEAvZbk4InnFyi-m9P7feJPGGwTH8jtHh5xiB7LsRx9RtzXeJ-baFzcYVU6BNhwXsDMu4sgZdb40kpK12k7qRdmjG1mv1J8pQmqOx3-RwXWFuW5NnP9PJnWfA-3E6sMD4_SHAlKlKQR7S1VPk5HYkoE1tm8o10y6v7pQ-GWzZSzqye3tU1FxmCoHmjnvVS-X4_BVz0oJ9tzfx21MGpzDSuogPegV5rC2D4fS6Ds4fbGj_eyuAuIqhrVPJyTPTQnoILAlSMT4gNpPULKKPCl3NjhaVw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
✔️
شماتیک ترکیب اسپانیا مقابل انگلیس
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/Futball180TV/107328" target="_blank">📅 20:56 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107327">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/591cd9489f.mp4?token=hjWiDxzHJu-UtYwVuWLape1m8UvihnuQjP3qNTkThOERh8btWQY0b7eSDc3qUoDDiUeoRh73moxNIHVj3TIqrsi9jGKvFWhCwIYYwXS05caOxbQjnDHWfU3ZR08vWry57cqOqi19931v2CgJw8EVDqrR-s5Da-VviB84DPSgJoeExznMD-GNriOFrA4i5DGWnpKbesoD_fmW6VpFu85sqvt3JyEDFciHm3s66zDT1YldMo4RvFtqgj-t14rWj8vzfVwxRYj-dS1qV4dGFXHLu7Geww_Ca4c3zQ1O9rr_661LYTw8GIB5Z7NrMOF7_BueaXkvzwFJsSfDlNJST16FRw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/591cd9489f.mp4?token=hjWiDxzHJu-UtYwVuWLape1m8UvihnuQjP3qNTkThOERh8btWQY0b7eSDc3qUoDDiUeoRh73moxNIHVj3TIqrsi9jGKvFWhCwIYYwXS05caOxbQjnDHWfU3ZR08vWry57cqOqi19931v2CgJw8EVDqrR-s5Da-VviB84DPSgJoeExznMD-GNriOFrA4i5DGWnpKbesoD_fmW6VpFu85sqvt3JyEDFciHm3s66zDT1YldMo4RvFtqgj-t14rWj8vzfVwxRYj-dS1qV4dGFXHLu7Geww_Ca4c3zQ1O9rr_661LYTw8GIB5Z7NrMOF7_BueaXkvzwFJsSfDlNJST16FRw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👀
✔️
توصیه عادل به بچه های کنکوری
😮
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/Futball180TV/107327" target="_blank">📅 20:53 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107326">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">✅
چرا باید عضو کانال ما باشی؟
🔹
تحلیل‌های روزانه و اختصاصی بازی‌های مهم
🔹
پیشنهادهای ویژه با وین‌ریت بالا
🔹
استراتژی‌های مدیریت سرمایه برای جلوگیری از ضرر
🔹
پشتیبانی و پاسخگویی سریع در گروه VIP همین حالا به جمع حرفه‌ای‌ها بپیوند و پیش از هر بازی، استراتژی…</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/Futball180TV/107326" target="_blank">📅 20:52 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107325">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hDBpM9jX9xOhB8CZPd1vsgk6bsS5-UkPeWcydlsm67bdPZez5xYP06z0-ED0yLhv6DIRcX9GhPUbyu5sYQGlfLcXBCZGaPtE7uRtxEoRTpHVuTvjotkP53lKuDKdMMCETcUOHsdoxiQWD43ceiHV1i61g5-1x1BybTQDascMmNazUNX-ABJoW13Cjz31IyHN1NM3tDfIwAVfXPOeMh1Z7Dq9wRHOdaJEJZDS5kIrDA0PVVUfw4sR-i-3u-Zfi0ODnovWp0l1r37IZMhe_X17MK7TF85sYfcYpZr6qZ9_SgEq4fF8fulcLoeWtNo2evDFvw2X8Nn6yhKGQX4JKnQ-Cg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
چرا باید عضو کانال ما باشی؟
🔹
تحلیل‌های روزانه و اختصاصی بازی‌های مهم
🔹
پیشنهادهای ویژه با وین‌ریت بالا
🔹
استراتژی‌های مدیریت سرمایه برای جلوگیری از ضرر
🔹
پشتیبانی و پاسخگویی سریع در گروه VIP
همین حالا به جمع حرفه‌ای‌ها بپیوند و پیش از هر بازی، استراتژی برنده رو از ما بگیر!
🚀
همین حالا به جمع حرفه‌ای‌ها ملحق شو:
📢
ورود به کانال اصلی (آنالیزها و فرم‌های روزانه):
🔗
اینجا کلیک کنید و عضو کانال شوید
💬
ورود به سوپرگروه (چت و تبادل نظر کاربران):
🔗
اینجا کلیک کنید و به گروه بپیوندید</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/Futball180TV/107325" target="_blank">📅 20:52 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107324">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VuMryDX809fzVj7rXs0WCGhFfSlOfpR0ia8PdAbSLBqeaxbi1eJQPSmbaqmBQqPmByacbaOjyp1EdTA03C9T94bqqtdSy7kDvofYFmRNSUZFEsrZ0j9Ul7fBQW_3PX9QSZE4ey1jzdjIZ3KkOqU_dNRS3wVUfi9uK9SJw0LQc9GsIIam2veoHle8xckNnDPkFtBLj7nnNGkNX8XJKKkKTw2i3RDNVqRrV9KuQQ2Ja0-Uo3_9bfGbKfsREHm__cfmun_1aQs5FcayXdmumhAGK9tvkwT_cMHsOo4UiHelGOC3xoHOjdRfiaL1CjyMgauhuOF3dcuKbTXRXgk65QZqGg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
‼️
👤
علیرضا دبیر: چطور مهدی مهدوی‌کیا با یک گل به آمریکا از سربازی معاف می‌شود؟ حالا هم علیرضا بیرانوند بخاطر مهار پنالتی رونالدو باید از خدمت سربازی معاف شود و هرکاری از دستم بر بیاید برایش انجام خواهد داد!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/Futball180TV/107324" target="_blank">📅 20:49 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107323">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bc1ed24863.mp4?token=KP3FsvcRa_TtDPOKwHWkZOpylWNBhbiRACcPwJaR2E6v8c66feL4Cf08D6nERs0dZKYpgfhrucinKda1Zq8k43JTz_aCnqeAFxBTyr_XsgjDcrW-EkEBvLD1W3dWrwCzTaWdE_7Eu20cAFPBIBXdR88y3fMIoAmErRQIWtM-n6DUd4iy8GYm3YmD2y_Ya1IR-ua9stU61EOmNPim6bWnxhymg3TXZB0y8g5-9EUDJB2ZMUCJss7kwvNjPRXRfUvFn2dUmNYlKPhFhKeSTkgrhuMblfl7Lt15_s6orVvc-k16sG-CPeCH62pjcQ-1Yk60BuJqvvt1-N9N1_aXO-AnNg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bc1ed24863.mp4?token=KP3FsvcRa_TtDPOKwHWkZOpylWNBhbiRACcPwJaR2E6v8c66feL4Cf08D6nERs0dZKYpgfhrucinKda1Zq8k43JTz_aCnqeAFxBTyr_XsgjDcrW-EkEBvLD1W3dWrwCzTaWdE_7Eu20cAFPBIBXdR88y3fMIoAmErRQIWtM-n6DUd4iy8GYm3YmD2y_Ya1IR-ua9stU61EOmNPim6bWnxhymg3TXZB0y8g5-9EUDJB2ZMUCJss7kwvNjPRXRfUvFn2dUmNYlKPhFhKeSTkgrhuMblfl7Lt15_s6orVvc-k16sG-CPeCH62pjcQ-1Yk60BuJqvvt1-N9N1_aXO-AnNg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
⚽️
عصبانیت‌شدید یاسرجلالی آنالیزور فوتبال از وضعیت وخیم تیم‌ملی با قلعه‌نویی!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/Futball180TV/107323" target="_blank">📅 20:35 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107322">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">🚨
🚨
🇪🇸
بعد از تست‌های پزشکی مشخص شد که کیلیان‌امباپه حدود دو هفته از میادین دور خواهد بود و مشکل خاصی ندارد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/Futball180TV/107322" target="_blank">📅 20:20 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107321">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/6fa8be9960.mp4?token=bJUpfOZbk5Ilm0Qb0i-oHAql415yOcvvwiDFXG_jFoSBzypvKSfSxFkmOjDrZnlYU96rr4UxGaa1n4JSKkjwdMUKZLHrgSmDJqij0bNloxYlxXjO7EO-q8uTJhvKgu5c7v5CuB7dt0n9d-uKcMRUYKI7QypMzJWBk_MiUL3i93xnj0wsCuC0bRiNok4ts8bhAa5ffAtyC3VTOZDzFI50BreCK8pys0-CZLdE6MPBBA2DLSu9AizscHbqRP8r6S8klkyXsn00Jrp_zMNP5Lyk0-p0a0b-mWy_xNOB_HvEjZzsWP234kkHgDKBhLObyO0mFJLXRJ7PXR3K-Dax0orYdw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/6fa8be9960.mp4?token=bJUpfOZbk5Ilm0Qb0i-oHAql415yOcvvwiDFXG_jFoSBzypvKSfSxFkmOjDrZnlYU96rr4UxGaa1n4JSKkjwdMUKZLHrgSmDJqij0bNloxYlxXjO7EO-q8uTJhvKgu5c7v5CuB7dt0n9d-uKcMRUYKI7QypMzJWBk_MiUL3i93xnj0wsCuC0bRiNok4ts8bhAa5ffAtyC3VTOZDzFI50BreCK8pys0-CZLdE6MPBBA2DLSu9AizscHbqRP8r6S8klkyXsn00Jrp_zMNP5Lyk0-p0a0b-mWy_xNOB_HvEjZzsWP234kkHgDKBhLObyO0mFJLXRJ7PXR3K-Dax0orYdw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
🙂
تو مسابقات کبدی بانوان در ناگویا، کاپیتان ایران حریف رو گرفت عین گوسفند پرت کرد اونور :))
بعدش خودشم زد تو سرش بابت حرکتش
😂
😭
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/Futball180TV/107321" target="_blank">📅 20:04 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107320">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/95b7a70c4b.mp4?token=Q4WhJMYxl0YD77MjVR9EQ1fxPhRAegxlnEOnIAG7iOjRZQjwCHNpxwCc3DzZIOWtHRt7Y7_PqjYJhULMGzjsJIAKDLdIFKeyProawzc6dqtI3vLmfpfTmY5bDfQwqqy_N-OciqgyXHKIg2ynGue_QpfFGUoox-aBuvCBL7pII0xAcvqMNLzJTjwT-6J9aaPTnuQ8zTdqNpZZw1XeRrYcHGsZQZgbgEuoPz1wSIxxapc1aQVA_ovqnTZytbmEltIRMmPg3xeDMBJDpcPUjUDz-xXoFLKCE3Y4xGH3kcXdHuFWaxoI31ShPS-NYPevONR8wfFuvrOlvgQYWTn8XDUPiw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/95b7a70c4b.mp4?token=Q4WhJMYxl0YD77MjVR9EQ1fxPhRAegxlnEOnIAG7iOjRZQjwCHNpxwCc3DzZIOWtHRt7Y7_PqjYJhULMGzjsJIAKDLdIFKeyProawzc6dqtI3vLmfpfTmY5bDfQwqqy_N-OciqgyXHKIg2ynGue_QpfFGUoox-aBuvCBL7pII0xAcvqMNLzJTjwT-6J9aaPTnuQ8zTdqNpZZw1XeRrYcHGsZQZgbgEuoPz1wSIxxapc1aQVA_ovqnTZytbmEltIRMmPg3xeDMBJDpcPUjUDz-xXoFLKCE3Y4xGH3kcXdHuFWaxoI31ShPS-NYPevONR8wfFuvrOlvgQYWTn8XDUPiw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇮🇷
🎙
حمید مطهری سرمربی فولاد خوزستان: دوست دارم یاسر آسانی بازیکن من باشد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/Futball180TV/107320" target="_blank">📅 19:47 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107319">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1b399b2bcc.mp4?token=nc7AuqJ0PeSA6qAiFNKtzhsxv5_-elSSSIwivZmQ3fXUsw9R1I0Ttk1Ugt39ul0vs66VwF3kvOhV9k633sGLaV4nupnLJprFIgNZz78IOmAzNhr_UTwzgRfn6Y3Kj6NDszAkiaixda-rR3XB7dFVphwIqpyGYy0PCiMnF-nYMdCZHvhWaj_GITCQBqD4j5DSmkBWEFGHJ51bxezF0G45-cQAvfl62diKdFsaon5fsQOxN9Y8IlGw7HM74lbXVQXVt8a_OZC7f6bLm6cm-CbI8yNIUlk8eKUMqUM2lpf2kqjQ8KOUyFHbQxlUY57d1zhk4UVcmLk_eNXvKYFY0tLaDg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1b399b2bcc.mp4?token=nc7AuqJ0PeSA6qAiFNKtzhsxv5_-elSSSIwivZmQ3fXUsw9R1I0Ttk1Ugt39ul0vs66VwF3kvOhV9k633sGLaV4nupnLJprFIgNZz78IOmAzNhr_UTwzgRfn6Y3Kj6NDszAkiaixda-rR3XB7dFVphwIqpyGYy0PCiMnF-nYMdCZHvhWaj_GITCQBqD4j5DSmkBWEFGHJ51bxezF0G45-cQAvfl62diKdFsaon5fsQOxN9Y8IlGw7HM74lbXVQXVt8a_OZC7f6bLm6cm-CbI8yNIUlk8eKUMqUM2lpf2kqjQ8KOUyFHbQxlUY57d1zhk4UVcmLk_eNXvKYFY0tLaDg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
🇧🇷
عصبانیت رافینیا بدلیل عملکرد ضعیف وینیسیوس در بازی مقابل استرالیا!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/Futball180TV/107319" target="_blank">📅 19:33 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107318">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BO2sTbwt_sv-qrcjTNEkJHkgdFkHt1HJUW-IirgGXlVQnq698vFeWunMIOMjgFYOpWmwnZVcW_58DlGRoreC2vkZzXVvgcWYI7A56XLxkofhSjL19enT1evfkX1OVT4T4ajV4myKG58KcP3YDYXwI9tOfD73GRwgb_899kJJoHXRi8LVJxSp4tbY0IuOWI2Qt-pGIVJsmqY5uq27NYkIZvOJPxCgPTh6ZOlNNIcMv-KOcpxU9_xGvWG7s3-wrcUSNhv6i63vXoBl_emeZ_Nc1FdBCvaBVEzsY72cICGuSfRlbGbXX9lmqVwfajv98DALFEuV7Sh4w0S4UOrbmkFAYA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✔️
🇮🇷
پیام‌تبریک مالک باشگاه استقلال به مناسبت سالگرد تاسیس آبی‌پوشان پایتخت
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/Futball180TV/107318" target="_blank">📅 19:15 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107317">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Aq8cB_xZ9TbuJAbE3_QJIEW4l-0TvJiFYOsl7VqxTh-F8_KTNSfTamanBHnNy2MpBSOqo9CkzZltwANPI6YLn6wlupEnVbC1rkyWqAnmw1IOmlmvWaE7orCsJQyp3s_NaB1LwFSzy0ELT6RW_AzE83MwoSDZozTa4G5nbA3zfnmdtxShLtKkp-qZlAd2zJNLcIMPz-50AzaAXYtsSjynU3K3kSykmJgPI30-JWmfdoCDHfY7RVS1x5ozsR34y9kXv87U6FJgImS6YdBRXL8qYTmloVrnqwS3mZDcfB4EcAVuF76Cu5YwWwB1lX1JR0p_GpeVvZIz91fCr5_rv2kXVg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔹
چند روز پیش موقع آغاز سال تحصیلی تو تهران، تو یه مهدکودک مربی از بچه ها پرسید شغل باباتون چیه یه پسر ۶ ساله برای اینکه جلوی بقیه بچه ها لاتی پر کنه بلند شد گفت بابام سرقت می‌کنه تو خونمون اسلحه ام داریم
🔻
مربی میره به پلیس میگه پلیس میریزه تو خونه این پسر بچه میبینه چندین اسلحه تو خونه دارن و پدر این بچه، رئیس یک باند سرقت مسلحانه از منازل مسکونیه!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/Futball180TV/107317" target="_blank">📅 19:02 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107316">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/j1k-j45sKNfT_1CWjsv9RTfE92152fCVko29QjddG1YdaFiEJaYwqxS23YRLeu814b_gughwJcI2gVY2Gr6SX3Z4CXpLCRzuIgm4CdE6r4ZZbyDXHl5b8pzetnW1LwL19sBCHzfLH_ION3qb1g9bAsEsOXBHfLntMg3UOdKZm4WJvIZKh0WgU6BEkHddSRYgJ3YQUyoGTpSkB-X0zLDjxowI6ea2o-LfRrm4LR3_cd23qUT-rQMhfsm7Ge_ezKGK0Z6SK33kOKCbUYFCDgU2Vo_AaaQXulzKkK6raUKgHZgPhLRQ-UMr8d8ZBXZsj--w8G7FGnxetgb4aWx5gCEkGw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
🇪🇸
تیم منتخب انگلیس و اسپانیا از دید هو اسکورد به بهانه بازی حساس و دیدنی امشب
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/Futball180TV/107316" target="_blank">📅 18:40 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107315">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/Futball180TV/107315" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/Futball180TV/107315" target="_blank">📅 18:40 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107314">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mKSBBY_7KsrtjNizvFOseIR1DI7bgX7PO2zL_V2D8EYr_CruZk_trA7Ohur-GlTOaMt9N7IOVzSGMdx8MaBkjiXzSy3UqJfCjvRFeTv8s0zRDOHfS8QsPB06ZDCYOza_PCn0Z9NnOw85GUpahKhbljNeafyGCghPzpez818on_VBAnVO7AW6ogZtG2m6V_Um6bsQcsnon6RWCS-Xu1Wl3NScjTp7ApKPmcZOUvIkiz1kB47n41zdySsaKRvcVUfL3mdj-ichzFipZE5yOjxn0CVYolqcPA0IZVZyGbuZ5gN4EIlHDXVQcEThbPr3MIfR0b4NP_XjsKzRV4lPLKCzBA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🦖
با اولین واریز، بیشتر دریافت کن!  فقط در سایت جهانی
TrexBet
🦖
بسته خوش‌آمدگویی ویژه
TrexBet
تا ۱۰۰٪ بونوس واریز
🦖
تا ۱۵۰ چرخش رایگان در ۴ واریز اول
🥇
واریز اول: ۱۰۰٪ بونوس + ۳۰ چرخش رایگان
🥈
واریز دوم: ۵۰٪ بونوس + ۳۵ چرخش رایگان
🥉
واریز سوم: ۲۵٪ بونوس + ۴۰ چرخش رایگان
🏅
واریز چهارم: ۲۵٪ بونوس + ۴۵ چرخش رایگان
🦖
🦖
🦖
🦖
🦖
🦖
TREXBET — PLAY. PREDICT. WIN.
https://TrexBet.com
T.me/TrexBet_Ir</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/Futball180TV/107314" target="_blank">📅 18:40 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107313">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a50b6c2404.mp4?token=sjUVjSUuBshTV0_P2YL6ZkBabcDzoLbZUmIAO2fNX-RKGXTzDmXz03DoonB41fqZWgJVoJ074VlfVojbzpGe82XIMwSueOrp-teXsSeRdIVETUcu-NetKZLotrwX3Qv6_FzW2lTpF22OWFq40AWrjd47yAmkhonKwaDnIAMCd8ZkpVDM-ADxz_W8NA2kefmx43HWcSNTF0tNhtgUdpqDakxLevgVJxmcSCpt8mVpcBZbu96j05MkvvT9foPuH5Tv1P4M8jug7C4bHBVDINWWJmu9x-P1lgA-YzgfNd7p-aeM1PjAjBFV_CBHTVgvCcrRC8wR4iORZrCGoNma2HHZnA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a50b6c2404.mp4?token=sjUVjSUuBshTV0_P2YL6ZkBabcDzoLbZUmIAO2fNX-RKGXTzDmXz03DoonB41fqZWgJVoJ074VlfVojbzpGe82XIMwSueOrp-teXsSeRdIVETUcu-NetKZLotrwX3Qv6_FzW2lTpF22OWFq40AWrjd47yAmkhonKwaDnIAMCd8ZkpVDM-ADxz_W8NA2kefmx43HWcSNTF0tNhtgUdpqDakxLevgVJxmcSCpt8mVpcBZbu96j05MkvvT9foPuH5Tv1P4M8jug7C4bHBVDINWWJmu9x-P1lgA-YzgfNd7p-aeM1PjAjBFV_CBHTVgvCcrRC8wR4iORZrCGoNma2HHZnA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
👀
گزارش جالب توجه گزارشگر مهمترین مسابقه هفته دوم لیگ زنان بین استقلال و خاتون‌بم!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/Futball180TV/107313" target="_blank">📅 18:34 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107312">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fbYVN_XybDr9q7MAw599RDz0E0PH12J0OV8SO8KJ3jUWp4QWb7UF1kZ9S3i5c2pRBetaf2wurAADIgkUikKDRA3kJnTCzqd9hac9lbROEIQ_aasL19kirtdOWsHUzWtr7U_PxkBPcC_0pQuSlBGWajDgncobluMNJ7zmZmtMqMA0SM3Z9ODHQrHfSGYQDvbPq1Zo6VAQZif_McDRWkJxaS0MVWCD0solBtUMpdL2iIxJbhy2kioGai9NybtskPzv6ZMDPYa9_-YbN9NC_qLNTfz26Z-2iBciF417zw5-kiNVj7cn43kCsyZVT2gWhvTBHafcv7FtcuUoUbIS8mf61w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
🏴󠁧󠁢󠁥󠁮󠁧󠁿
رودری ستاره سابق سیتیزن‌ها: آنچه ما در این سال‌ها انجام دادیم قابل سلب کردن نیست. قدرت و سیطره تاریخی سیتی در لیگ‌‌برتر هرگز با رای دادگاه از بین نخواهد رفت و قهرمانی‌هایی که کسب کردیم در عین شایستگی بود!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/Futball180TV/107312" target="_blank">📅 18:04 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107311">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/h1pz-tiL58uL-G8E5rhn25mrD2Sn4tB7C6zlkN3IslO9PmocHcRp_-NJPj1MqE0U3Z9VZ1o4zqAu0HoFOlIlbq12cF1JPh3C06uDu1ohiznJLXJfQhbELTg9JE8smOA67KIETg52qRM2rLrq9dNO4YamOw_LC5QuYTAQIno410yZtaybLTSe_6nGBxkTR7ChXRW6BLIXM5Uil-M46_CP7XUCgldiEnX0vZ5ng3immN2eesyA7U0ThMtXHMc3LyOedZlgugqXlRI7ZvcjgZkPr8eCprCfNDzQFyOYhm-k5vFWjXONh9J2Kzb_drzobc-Ab9cD12kAYaMV2f1xi-c2pQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
👀
لامین یامال ستاره بارسلونا:
🔻
من برای پول فوتبال بازی نمی‌کنم، چون دوستش دارم بازی می‌کنم!
🔻
بازیکنانی که وسواس گل زدن یا پاس گل دادن دارن از بازی لذت نمی‌برن.
🔻
من برای خوشگذرونی بازی می‌کنم؛ برای دریبل زدن، برای بازی با یک یا دو ضربه، برای اینکه به هم‌تیمی‌ای که هنوز گلی نزده کمک کنم تا گل بزنه؛ من برای شادی بازی می‌کنم.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/Futball180TV/107311" target="_blank">📅 17:36 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107310">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">🚨
⭕️
⭕️
🇺🇸
ترامپ: پیشنهاد ۷ بندی ایران را رد کرده و اصلا مورد پسندم نیست
🔻
ایران خواهان توافق است و من هم از توافق خوشم می‌آید، اما این پیشنهاد غیرقابل قبول است. ایران خواهان بازگشایی فوری تنگه هرمز است زیرا متحمل خسارات سنگینی شده است. من هر توافقی را که بر اساس آن ایران بخواهد فوراً تجارت را از سر بگیرد، رد می‌کنم زیرا متحمل ضررهای بزرگی می‌شود.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/Futball180TV/107310" target="_blank">📅 17:25 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107309">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/712da7f0e0.mp4?token=HCsIC5Pln8fQukKF42XkmaWALARqN1_LnNl45XvBuxFcA6K_ycSAtj3bEEvNLMta4oLp7b35kiWdvMQN3gDGMgEhhWfYhythwmpc4unD1BAM6xY9J-WmU7WLE5lArOSFtLwUAvmSOSl03xV9u39ifV-6yNd47PtiEVqN_O9gkuABBO_P0W1ben9y2tn8GBWcnnS8tPbqggCZo-ft2RSqH-8PemVe5jfUfJ_WRSKt_rE2qz8AbZ3voM-x47qMtfbKt2wyLEwqBx0ju76_EWj5WeJYJSYvV0g3wmNoBounUQ0-ZTnMWohJodrRFOXxyiWIktAjdJWiaMgoumcYWR1YBw92GSpZKQxtSiA0VMdIZ4e225-4pZ-yErmhaQD-5bqqPvY04MuripNT8UHfXUPX7595sVm5wQXoQhmbaruaCeL17S8lcpOFjFXG8yYUuKYFSfa7PnuLf__hGZiwT_nPUOaFlixHfwoJLyg27YWrKNnSqEaC1aSumckgqInuHqXFrHfqB9mJwlLgnHVCNK4rxCofsTcVRvaxiXoKhffen5MI0eNT5YWH1NdtuLM6Gl_HUNNoi007kWQpZZckcfkftDkzdUsHi1UBgUTYB4mX4GvCAaiRpnDIyl9GNPPrvn5-K22WBldNU0vfqEbvZhsx7U_G9FV5a6vK3gPWVl5ZCTs" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/712da7f0e0.mp4?token=HCsIC5Pln8fQukKF42XkmaWALARqN1_LnNl45XvBuxFcA6K_ycSAtj3bEEvNLMta4oLp7b35kiWdvMQN3gDGMgEhhWfYhythwmpc4unD1BAM6xY9J-WmU7WLE5lArOSFtLwUAvmSOSl03xV9u39ifV-6yNd47PtiEVqN_O9gkuABBO_P0W1ben9y2tn8GBWcnnS8tPbqggCZo-ft2RSqH-8PemVe5jfUfJ_WRSKt_rE2qz8AbZ3voM-x47qMtfbKt2wyLEwqBx0ju76_EWj5WeJYJSYvV0g3wmNoBounUQ0-ZTnMWohJodrRFOXxyiWIktAjdJWiaMgoumcYWR1YBw92GSpZKQxtSiA0VMdIZ4e225-4pZ-yErmhaQD-5bqqPvY04MuripNT8UHfXUPX7595sVm5wQXoQhmbaruaCeL17S8lcpOFjFXG8yYUuKYFSfa7PnuLf__hGZiwT_nPUOaFlixHfwoJLyg27YWrKNnSqEaC1aSumckgqInuHqXFrHfqB9mJwlLgnHVCNK4rxCofsTcVRvaxiXoKhffen5MI0eNT5YWH1NdtuLM6Gl_HUNNoi007kWQpZZckcfkftDkzdUsHi1UBgUTYB4mX4GvCAaiRpnDIyl9GNPPrvn5-K22WBldNU0vfqEbvZhsx7U_G9FV5a6vK3gPWVl5ZCTs" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
از روزی که رونالدو نتونست مثل قبل بدوه و هتریک کنه، موتور تیم ملی پرتغال از کار افتاد!⁣
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/Futball180TV/107309" target="_blank">📅 17:20 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107308">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d5c5606552.mp4?token=pIkhukRLMfBOcAkjzXhoUADBYkFRYN2ayHlvoziQZY5ERHxiCgXYacfzzE4vNjbbjQNZY9fBl5V5Ik13rtdlCP15jAnDLQRdv01nsAftIngQuf-F4gBg6h9DvelIQDwsnXKr8GXGSCRbnnA5IqsQaiFn1E7JoT-qPY2ZHT-C5fjX9h4wHe_qoO4oyAsx7kefv1CmzZ6YBdmWIs_gdOvQGJp44kYY4LZXzYu9Uph5U2f682lFn15FhBg_6y6LKtnx7g4m-q1YCDXJu0TKn5h1xTvAKqsGNZ8ZVZMDj8ecopBxsROlMfbw5q9rBEtVSopS9b6da9G1hHWhnr8yBP78Qw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d5c5606552.mp4?token=pIkhukRLMfBOcAkjzXhoUADBYkFRYN2ayHlvoziQZY5ERHxiCgXYacfzzE4vNjbbjQNZY9fBl5V5Ik13rtdlCP15jAnDLQRdv01nsAftIngQuf-F4gBg6h9DvelIQDwsnXKr8GXGSCRbnnA5IqsQaiFn1E7JoT-qPY2ZHT-C5fjX9h4wHe_qoO4oyAsx7kefv1CmzZ6YBdmWIs_gdOvQGJp44kYY4LZXzYu9Uph5U2f682lFn15FhBg_6y6LKtnx7g4m-q1YCDXJu0TKn5h1xTvAKqsGNZ8ZVZMDj8ecopBxsROlMfbw5q9rBEtVSopS9b6da9G1hHWhnr8yBP78Qw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
ابراهیم‌شکوری دستیار حسین‌عبدی بعد حذف از آسیا، از ژاپن برای خودش آیفون ۱۸ آورده!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/Futball180TV/107308" target="_blank">📅 16:55 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107307">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/275c393efd.mp4?token=VJJaMT8qVjhxViWbCXgzMjCM3uHRhkzCyiaHhc9JpstYfTmUIfG-iaEie3_0UAMCmShHpQ-SGRFD545fYTqVIb3xDUdhGf5HR0uXCaASYcvmb8ybpF6a6vUTVGn2xownofOFaWmNoCi4Dk0RzBRbGEhSo09l7-i7KVWb42WLmA0-KoZuQGt7JyNZP8nS_uUc79hcyWkK6VEOWqNfQNN2R8ue4hRHze4uJMjgjX_o7MZyK0hX-YZ-cV4APeU5_YvW_k2mSLL-IP9Hr8waByWUtpqgHyFkw1Xmfhay11bq7ThwyLuwP6VKhwImWYoDFX0G69sxgA_CxIjrc1GGRjevpQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/275c393efd.mp4?token=VJJaMT8qVjhxViWbCXgzMjCM3uHRhkzCyiaHhc9JpstYfTmUIfG-iaEie3_0UAMCmShHpQ-SGRFD545fYTqVIb3xDUdhGf5HR0uXCaASYcvmb8ybpF6a6vUTVGn2xownofOFaWmNoCi4Dk0RzBRbGEhSo09l7-i7KVWb42WLmA0-KoZuQGt7JyNZP8nS_uUc79hcyWkK6VEOWqNfQNN2R8ue4hRHze4uJMjgjX_o7MZyK0hX-YZ-cV4APeU5_YvW_k2mSLL-IP9Hr8waByWUtpqgHyFkw1Xmfhay11bq7ThwyLuwP6VKhwImWYoDFX0G69sxgA_CxIjrc1GGRjevpQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👀
❌
آنجلوتی بازهم به رافینیا استراحت نداد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/Futball180TV/107307" target="_blank">📅 16:30 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107306">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eCCUlV9H9-nD_Z75jFUv-insxTas66D9pUupJhAsm93UtXI0VOUWD49x70wNgXwfATCeHvoKsD-gGX7AKJomuE8U1tPcaN5vx4hndKIJ1pAUE0eWs7LlSwBFxsfi0nUETISAM1IeBBacDBSsl1Wn9kiOIqA9xybjQ56apli1viZHS9Qkp2ZrmbLRUIKpEFTYhpRMAGlgNejWFqRKce9suMqpvq8eZS_xdVIwSJ5LbkXw5mj4AgOnKq1Wzlvr1A6tBaSB5LJVZSJx_rpZ4HOjBSNsgzvX55zntIiSlj1vq1xqVvYahQ5IJkVFFkIbkBcNnNbKYieS4yH-OGWbmKY47w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🇮🇱
🇮🇪
چند بازیکن تیم‌ملی ایرلند از بازی مقابل اسرائیل انصراف دادن و گفتن که مقابل این کشور بازی نمیکنن. در صورتی که این اعتصاب گسترده‌تر بشه و ایرلند وارد زمین نشه، اسرائیل برنده بازی معرفی خواهد شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/Futball180TV/107306" target="_blank">📅 16:00 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107305">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b29264e5e2.mp4?token=ffXzf6EAwet3DHhaY1mdV-EbKjKMOrDpFu9oZcIJkuxQ6rXmucxdrPkcNqYTP1yw4BlYAch2L-goTJ1fmJJ5I6EI0cV0Dsvhtw4vc6cn_QYj3Z16B_WUJMSeCiWlikY-dk9i6bD-66Vst9F9XYGjcjMtXQu6bMG5hj7ZmZva1s12vlVC5FOwzqMGhuiV76mrULS2J1Sb3p4weDy5K-Y1VJkp7Dz-xa33vU-xk86yw_evndE1ZpWx8RouwCK7wAlqZXAfBAQB2q2NsFmwYCCGZIyBUyx0Fah6pgjnDWVHxOtNCjd7UnY6HHbYGz_RrJ7MrS6IlD7jHLzgXSC5n71x0nITOo_qVPAo1jSfdLrbAtt6HrwK5FywmyDXbYjkGfVkduEmWcfOSbzRUvxkGE-9hRSM8fToX0Gaq3Qkof84qI0v7ChpP_HXQ8mOVEfwgIxkU08JISHMPqC43gKKOhixuat45S_xNiagOhHJe3a-VkKRWESFObb4rLRS2lTwzMQItFHwU9J_oOjRUguGKnrrE7TPitkNs9dyTnGg2tFOGg_XfKu4okswaho9sJKoyom61-ji9ulf6FM3nPdieyyPTB8eWdqydg5ILNTYoaTYnAGlZ0VqMyYAZaIRmuWEy7dlzvysZQK7_6ZcNRyITgbRFtov5Tp2oziPyFnzfJx17gg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b29264e5e2.mp4?token=ffXzf6EAwet3DHhaY1mdV-EbKjKMOrDpFu9oZcIJkuxQ6rXmucxdrPkcNqYTP1yw4BlYAch2L-goTJ1fmJJ5I6EI0cV0Dsvhtw4vc6cn_QYj3Z16B_WUJMSeCiWlikY-dk9i6bD-66Vst9F9XYGjcjMtXQu6bMG5hj7ZmZva1s12vlVC5FOwzqMGhuiV76mrULS2J1Sb3p4weDy5K-Y1VJkp7Dz-xa33vU-xk86yw_evndE1ZpWx8RouwCK7wAlqZXAfBAQB2q2NsFmwYCCGZIyBUyx0Fah6pgjnDWVHxOtNCjd7UnY6HHbYGz_RrJ7MrS6IlD7jHLzgXSC5n71x0nITOo_qVPAo1jSfdLrbAtt6HrwK5FywmyDXbYjkGfVkduEmWcfOSbzRUvxkGE-9hRSM8fToX0Gaq3Qkof84qI0v7ChpP_HXQ8mOVEfwgIxkU08JISHMPqC43gKKOhixuat45S_xNiagOhHJe3a-VkKRWESFObb4rLRS2lTwzMQItFHwU9J_oOjRUguGKnrrE7TPitkNs9dyTnGg2tFOGg_XfKu4okswaho9sJKoyom61-ji9ulf6FM3nPdieyyPTB8eWdqydg5ILNTYoaTYnAGlZ0VqMyYAZaIRmuWEy7dlzvysZQK7_6ZcNRyITgbRFtov5Tp2oziPyFnzfJx17gg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
🔴
ادعای جنجالی کریمی: خودسرانه برای بیرانوند دفترچه پست کردند؛ در تلاش‌ برای معافیت پزشکی او هستیم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/Futball180TV/107305" target="_blank">📅 15:53 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107304">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dc52d28f2d.mp4?token=IAuom0ayNw44B5vUqY-2folq-bcKwScgO-jTv6QdAQ1FBPvSAvdzV3KwcyHVFXwMXJhB-MGGwszDpV4T61tnniomRB6l2nkwl9IQdOqc_Wwd9UOo5YLmEgD_gy9uqUW_PTMRh3FGR6dwbqE58szijcM1hPxSU8PfJgSMpN5AlhwVoRxDe7dFzEqwxYN1C_TAlOgCszDoOtd6zKJpGVitXsP6srCkI2YsCc5ixJV-JGxa9WF5e4-Jb5uQCJyw1rFu8999G7iIqiVL8JF3F6li-QRd8DMN1HterPQPwux4HVD9f1DWzmhKZR55pcoGqISbKYbV3R2-G5yqaiTy-_z-WQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dc52d28f2d.mp4?token=IAuom0ayNw44B5vUqY-2folq-bcKwScgO-jTv6QdAQ1FBPvSAvdzV3KwcyHVFXwMXJhB-MGGwszDpV4T61tnniomRB6l2nkwl9IQdOqc_Wwd9UOo5YLmEgD_gy9uqUW_PTMRh3FGR6dwbqE58szijcM1hPxSU8PfJgSMpN5AlhwVoRxDe7dFzEqwxYN1C_TAlOgCszDoOtd6zKJpGVitXsP6srCkI2YsCc5ixJV-JGxa9WF5e4-Jb5uQCJyw1rFu8999G7iIqiVL8JF3F6li-QRd8DMN1HterPQPwux4HVD9f1DWzmhKZR55pcoGqISbKYbV3R2-G5yqaiTy-_z-WQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
⚠️
حسن پاجانی، قهرمان مسابقات ورزش‌های الکترونیک (بازی efootball) بازی‌های آسیایی ۲۰۲۶ ناگویا: دلیل قهرمان شدنم اینه که یه سال و نیمه ایران نیستم و اینترنت بهتری دارم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/Futball180TV/107304" target="_blank">📅 15:40 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107303">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0b2e1cd171.mp4?token=Z6L3elSW60ajlXlMZ7OL8YFH299-XjzSFvUN_d19Wlw9DJFxyJodEp-f9YG9tMSa0J-YY2swsJjZ2ZAsInUuNWV3yMFAthJN0N1obORM4wTHj34-ejQYO6UEfq5oO77Q_oZpoymXAzwxxaGQIeM9AImSVSE0phVk0rWDC9CG3hs1JUphZvztRKx7m9XxXE7gs7NpWQIfpEObsP5Rt5YY12EuVph11dE-mjJ67qJwL3bOZMOlKFIAJdglyUdZwrsFj9EumdBPFZl_zJ4IJ5f4uGzLi_wJGzQ1cvrs5dklqvuzXUAx7xCJwwdbZrFIJN17zNifN29LkQ5dYM8STatWAw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0b2e1cd171.mp4?token=Z6L3elSW60ajlXlMZ7OL8YFH299-XjzSFvUN_d19Wlw9DJFxyJodEp-f9YG9tMSa0J-YY2swsJjZ2ZAsInUuNWV3yMFAthJN0N1obORM4wTHj34-ejQYO6UEfq5oO77Q_oZpoymXAzwxxaGQIeM9AImSVSE0phVk0rWDC9CG3hs1JUphZvztRKx7m9XxXE7gs7NpWQIfpEObsP5Rt5YY12EuVph11dE-mjJ67qJwL3bOZMOlKFIAJdglyUdZwrsFj9EumdBPFZl_zJ4IJ5f4uGzLi_wJGzQ1cvrs5dklqvuzXUAx7xCJwwdbZrFIJN17zNifN29LkQ5dYM8STatWAw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✔️
🎙
هانی رامبد: امسال سال‌بسیار سختی بود اما برای آینده تمام تلاشم را برای گرفتن ویزا ورزشکاران ایرانی برای حضور در مسترالمپیا انجام می‌دهم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/Futball180TV/107303" target="_blank">📅 14:50 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107302">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c90efab6fe.mp4?token=WHjT_NmbVz-fCKo6YWdd4Pym5lQD7wOTXYLI8vTvhmyB1DpYr4ihK9A5UJredYkgpT9fzyoranv3batGIEwiLbfKtaHjH2XPk7iVun6Oxlfdi-6UpzBEf1nNRvpMe69cnoFh4zAXJvDZIMOf8EosZREYJ5--KCrHKSgEv3d3mfZfXdvHcmsPnuv0t86dyKgud7f0bHFtBEqyksZDXCJ51fmDr6U9eXQFaNk8v16Mj77EWkUzYxd_VL05wRomCZF0cU1ky3b66dki_mWvjslDqHCS1qId9BfAMAgu5_kaausZiq7aLaIT2lZS_w5Z0hTfg-s4aGdsJv8uI0PqjsGTWI2BSGGMAXTJC1dZ1p1wzj3Belb4zOeYCd-Rn8dfIe_zHzU5nOc3Cm5E-NbbVbT0G6IDFWx3SqIIfuQDkYIf1qy3sn-Gp0MPNXoxuIKL4XgNQygXMUTGXMlpPA-tXbLZ3BXNyuE-QrBrQag6-6Rpc-_VsbjV4zm4n0ikPemDVx-675geKLbTrJMIlKZ7eMwgWtTJOHxlyEoNKjYKTjZVUhNHw0N5GIHIWJLBTYPIm-ITVSuAWNIgur7rfbpsxdu257xWVUqTNvHhPfuO1JLbR1H-SeRP4kKT98m4xJ1sKwx2MazFdTOC-xkYx8YIX0mo1PCyJrC-uHFzx4Mi9UDEbTo" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c90efab6fe.mp4?token=WHjT_NmbVz-fCKo6YWdd4Pym5lQD7wOTXYLI8vTvhmyB1DpYr4ihK9A5UJredYkgpT9fzyoranv3batGIEwiLbfKtaHjH2XPk7iVun6Oxlfdi-6UpzBEf1nNRvpMe69cnoFh4zAXJvDZIMOf8EosZREYJ5--KCrHKSgEv3d3mfZfXdvHcmsPnuv0t86dyKgud7f0bHFtBEqyksZDXCJ51fmDr6U9eXQFaNk8v16Mj77EWkUzYxd_VL05wRomCZF0cU1ky3b66dki_mWvjslDqHCS1qId9BfAMAgu5_kaausZiq7aLaIT2lZS_w5Z0hTfg-s4aGdsJv8uI0PqjsGTWI2BSGGMAXTJC1dZ1p1wzj3Belb4zOeYCd-Rn8dfIe_zHzU5nOc3Cm5E-NbbVbT0G6IDFWx3SqIIfuQDkYIf1qy3sn-Gp0MPNXoxuIKL4XgNQygXMUTGXMlpPA-tXbLZ3BXNyuE-QrBrQag6-6Rpc-_VsbjV4zm4n0ikPemDVx-675geKLbTrJMIlKZ7eMwgWtTJOHxlyEoNKjYKTjZVUhNHw0N5GIHIWJLBTYPIm-ITVSuAWNIgur7rfbpsxdu257xWVUqTNvHhPfuO1JLbR1H-SeRP4kKT98m4xJ1sKwx2MazFdTOC-xkYx8YIX0mo1PCyJrC-uHFzx4Mi9UDEbTo" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⁉️
هری کین یا لامین یامال؟ تفاوت فوتبال انگلیس و اسپانیا؟ وضعیت جود بلینگام؟ مقایسه توخل و فلیک؟⁣
✔️
جواب همه سوالات با آنتونی گوردون در مصاحبه پیش از بازی انگلیس و اسپانیا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/Futball180TV/107302" target="_blank">📅 14:25 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107301">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7e44add616.mp4?token=pwnYlbmktGoqH91A0LNGk3DuhD-ZnrUz9g4-Pxhe0qtamBZHP1AwwPkDJK32RYmLC_26D-9mzBXcT_z3BRQ6qD1tpS7PwvSpecTfzlnyE5LI7Qs_RgVDz6Fh0nwwn62EmaTiKxU2wwGAOPoOGG4WbCw6T39JOxmtwFsENbgqslUEouQPvifyCtBanZZ0eWhmjGm_c-kBObIdQoQ96_-iEvulF-nJBmCAPuNPoz5TQTGpbam2MhgHjbpFhvPjLPx6Q_0O9C-Ztobp8R2gnxiGxjVApjCf7OzCpYqAHBdtcQqIL_27DLZ_TOtxlKCZCHNH0_S1LtijcZukhxWBpCL5lQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7e44add616.mp4?token=pwnYlbmktGoqH91A0LNGk3DuhD-ZnrUz9g4-Pxhe0qtamBZHP1AwwPkDJK32RYmLC_26D-9mzBXcT_z3BRQ6qD1tpS7PwvSpecTfzlnyE5LI7Qs_RgVDz6Fh0nwwn62EmaTiKxU2wwGAOPoOGG4WbCw6T39JOxmtwFsENbgqslUEouQPvifyCtBanZZ0eWhmjGm_c-kBObIdQoQ96_-iEvulF-nJBmCAPuNPoz5TQTGpbam2MhgHjbpFhvPjLPx6Q_0O9C-Ztobp8R2gnxiGxjVApjCf7OzCpYqAHBdtcQqIL_27DLZ_TOtxlKCZCHNH0_S1LtijcZukhxWBpCL5lQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
بیرانوند سر صحنه پنالتی بازی با ازبکستان به چه چیزی داشت فکر میکرد؟
😂
😂
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/Futball180TV/107301" target="_blank">📅 14:05 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107300">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0d96c298a1.mp4?token=ZoG-GvKvO0Q2j51bNBrAxs2yjqSH4-n2AyQAWuP91_RCAAcXSucPMJg1LaEYTdMbeXdwPU9I5a38kDvlX_6elogrEKwJZi5h8p9wP1We1qBS96G8db_mMXrgzHcDI0s44ZZpEeq6HsC1bDtaicxR17ZABGP0s9Ygb_g0_Sokg73wx4pmLZwg7CwXkNA8OK6bzGXp20ou1l43gsmD_Y1_1wBNI7wOsNVt6-rjRIX9SzeLAQ_YRKHu9_UotVOKtBe8q1G1y-AsaL5XAkQYpL9cZxZ5r-rMtyw6kh44TQtgqNxkXkNiyKgQ_FFRtB2RUjNPytXEioZGdHxcK0Cy-HJtyg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0d96c298a1.mp4?token=ZoG-GvKvO0Q2j51bNBrAxs2yjqSH4-n2AyQAWuP91_RCAAcXSucPMJg1LaEYTdMbeXdwPU9I5a38kDvlX_6elogrEKwJZi5h8p9wP1We1qBS96G8db_mMXrgzHcDI0s44ZZpEeq6HsC1bDtaicxR17ZABGP0s9Ygb_g0_Sokg73wx4pmLZwg7CwXkNA8OK6bzGXp20ou1l43gsmD_Y1_1wBNI7wOsNVt6-rjRIX9SzeLAQ_YRKHu9_UotVOKtBe8q1G1y-AsaL5XAkQYpL9cZxZ5r-rMtyw6kh44TQtgqNxkXkNiyKgQ_FFRtB2RUjNPytXEioZGdHxcK0Cy-HJtyg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
کری خوانی های عجیب هندی‌ها برای ایران؛ لحظات پایانی فینال کبدی مسابقات ناگویا و قهرمانی هند
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/Futball180TV/107300" target="_blank">📅 13:45 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107299">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mAVcwLLjR0QjbyOnw4JkMnh3Quh-_byKj6E-kMFToS_ZNmIPj9xsjwzBNetMQuMEJy2WMEzPweHjlZJUeWA90CLHFhhOcEZqc7s_lswcGECuoZsRcgeE7A9DWBuP_eKgDrM2q7wnLFIcFaKL7cGzhn3fPlP4AKSsRo9Cs-h0gS-StW2Uz6Bz0-dJ5BgyEKKxQ3BAk93phwTpOwCW_rKNPHG6dCO3_5_m1oej9b0RN9hYCjMhioVbgtVNe50I30neUniJaPNjjZMLFQ6cgEnExhWu1vAJZgMYU-v6fy4DgS7KttxEgywsy5zPIgOp9Ybjluebzxb46MEilRewI1EViA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
😳
تو حرم مشهد این آقا صد میلیون چک نذر کرد و انداخته تو ضریح واسه شفای زنش؛ حالا بعد یه مدت اومده رفته بالای ضریح میگه زنم مرده تا پولم رو پس ندید پایین نمیام.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/Futball180TV/107299" target="_blank">📅 13:39 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107298">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4221e00ddf.mp4?token=kzZJP72Q1WCMR_zYgszyqVZlS2GHvHyoL49hQ92t_ZlKrSai6WVRyTW1zY37pDbKdOWLsFK2bUlWvHUpGw42yS5Y-l2LjcmH4yXgVboUhQyllOJdQO-zwtdF5X7QJR2D8lgKQO7orav339v4Cz0BRgR5YcQ3epFA9tq--4hl-XlTZ5UyWSYXj2tpVMaZkUqZxXBlQVDwiFObUSFkIyJK9hkOA_HWu-PxZstmJpEv8M9NgDLXRYcsUwRlG1JN3MQETCxI23HkS_kxjPjCe6D7_GdwiARuKxJXJbN3Ak0lwp3YcVftdWdiB6QeVhC9emaxhsFJAjO2dSaJDjYukULSyKVxWfxPs4sGQek78weKkArbkVFXrlRDC6wERiR_pUFWVtpcQnXMEGQzxEYkO8VZIU6OUNarlSMSAMCBTdakGMSs7iqd4og9X-w3uc3hIGi3k8QYnA9XrQ68hjuKzjPJuPy4K2FPmWJCaw_c750srMfS-JqW00Dr6O7E6OuC2BBxzqWVdb-mtaL3D-pZqwDoe4YSNURPnmokW4SS2YsyI1kDuLzv3VXxx2eemoFW6G7zFoP4Glm_wkkDqi5ImbTw5Bg__gbZuvBniXtJZolWbZtiwgJlsJdPkVFfP-WiUHRKyUniUP0kLb4YPp82MsbFSNbhhBe7e6_QzaavjPaKOog" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4221e00ddf.mp4?token=kzZJP72Q1WCMR_zYgszyqVZlS2GHvHyoL49hQ92t_ZlKrSai6WVRyTW1zY37pDbKdOWLsFK2bUlWvHUpGw42yS5Y-l2LjcmH4yXgVboUhQyllOJdQO-zwtdF5X7QJR2D8lgKQO7orav339v4Cz0BRgR5YcQ3epFA9tq--4hl-XlTZ5UyWSYXj2tpVMaZkUqZxXBlQVDwiFObUSFkIyJK9hkOA_HWu-PxZstmJpEv8M9NgDLXRYcsUwRlG1JN3MQETCxI23HkS_kxjPjCe6D7_GdwiARuKxJXJbN3Ak0lwp3YcVftdWdiB6QeVhC9emaxhsFJAjO2dSaJDjYukULSyKVxWfxPs4sGQek78weKkArbkVFXrlRDC6wERiR_pUFWVtpcQnXMEGQzxEYkO8VZIU6OUNarlSMSAMCBTdakGMSs7iqd4og9X-w3uc3hIGi3k8QYnA9XrQ68hjuKzjPJuPy4K2FPmWJCaw_c750srMfS-JqW00Dr6O7E6OuC2BBxzqWVdb-mtaL3D-pZqwDoe4YSNURPnmokW4SS2YsyI1kDuLzv3VXxx2eemoFW6G7zFoP4Glm_wkkDqi5ImbTw5Bg__gbZuvBniXtJZolWbZtiwgJlsJdPkVFfP-WiUHRKyUniUP0kLb4YPp82MsbFSNbhhBe7e6_QzaavjPaKOog" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📊
آنالیز دربی مادرید: چرا رئال به گل نرسید؟
🧐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/Futball180TV/107298" target="_blank">📅 13:35 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107297">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/75d0bcba0b.mp4?token=lx0Jh1EyPGSFHOVeHNnhu0pp6ZW5WPN2lctKR0XwUJMwIriM20ndXYW04EFbpsh4r5W8GAKHVdUK8zzNyRqcgRMTwliBBrIAxTV1gtdxp49ZxaO0W1fa7oOjBrUd_znr1W3fDTpIxm0qWKHAbI_p_kazW91ZwlH3YmS7U3Qjz9SPcQRezjyD3s1nzgWdlqi97eKILU66Tz0FwUi6L4ifjDG3ysTRrvRUXKPUxPAS3gz6whW8MhCdEduiTqzk1H_rDAK7wLPrgHFlg3earoSSiJJuYXx_Z6DgKCbDRzyhVxLFQtW0OXx13NOXqw5AeqCOLPE3ZEDpRDDl9YVk8lGmMg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/75d0bcba0b.mp4?token=lx0Jh1EyPGSFHOVeHNnhu0pp6ZW5WPN2lctKR0XwUJMwIriM20ndXYW04EFbpsh4r5W8GAKHVdUK8zzNyRqcgRMTwliBBrIAxTV1gtdxp49ZxaO0W1fa7oOjBrUd_znr1W3fDTpIxm0qWKHAbI_p_kazW91ZwlH3YmS7U3Qjz9SPcQRezjyD3s1nzgWdlqi97eKILU66Tz0FwUi6L4ifjDG3ysTRrvRUXKPUxPAS3gz6whW8MhCdEduiTqzk1H_rDAK7wLPrgHFlg3earoSSiJJuYXx_Z6DgKCbDRzyhVxLFQtW0OXx13NOXqw5AeqCOLPE3ZEDpRDDl9YVk8lGmMg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🔴
دبیر: تراکتور برای من هیچ فرقی با استقلال و پرسپولیس ندارد
مراسم امضای تفاهم‌نامه همکاری باشگاه تراکتور و فدراسیون کشتی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/Futball180TV/107297" target="_blank">📅 13:22 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107296">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pZtY6yjOKNX7dv2V_saTQjzJdX_BMJ5NA7nDNbRUIvd3Z36YF2SF71B-bJpa9ibxXUCoelrwtBk1bl8Rg92L8IqTehFl7yzq0b82e-KXK0FDPqy9mNA5lQAGodUOUzbnQThMMMlV-wd1hIG24h-Cj1CUqNot9ykjIztY0CQC70vpnhgXPbc9cDIV_YJVrfDjdYyLieRYAPbUnVg2hWkBQ3h31kA5y_jycfta4I9WlWTNhbrT7xHQ3b3q-yQyTqpI8PiP5rBYvZiQsyE4dYm0tj7k2IrkQ5zLFGY2q3uO15TqwP0bOVi8Jpy6S_Bg2sCuVdKk5nna0nupisKsgoJ9lQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
👀
همسر سابق سپهر حیدری درباره رامین رضاییان: ایشون بااختلاف چه از نظر فنی چه ازنظر اخلاقی‌بهترین‌بازیکن حال حاضر فوتبال ایرانه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/Futball180TV/107296" target="_blank">📅 13:15 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107295">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gGGWjFSdl1AqJGSPVCvPYlyxod1mFC4vBGc7r_jcOoRNr4F7kxTAeDlwPttSvFztqZIDiWU3yMzHaN9IaaakCOBnGqssweZG7qBwXTxKO1CsflreMJeiW1C-Vjcmlnj6d7daX4064jcsC9Uh_Wn2yX8PJBwyV3JC0InkJj0wjhQPTnTiHDMreQypGTP7t5vm9aNNzHYapFDP_M8xaDJ2tCSWmO1e8M8FaZ8QEWARBIhWbfh4jdEFY4cEGZaCXpnBXJ4mGCTM3ph-kskwSINm6lDUdUIMi2LbQsW4zyH35ObbSY1QGYBbAyLD6kFShrT7KYT5dhXsKMFQPjyIfxQ4mA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
اگر قهرمانی‌های‌سیتی گرفته بشه نتیجش میشه:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/Futball180TV/107295" target="_blank">📅 13:07 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107294">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/Futball180TV/107294" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/Futball180TV/107294" target="_blank">📅 13:06 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107293">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eiaihOb3AEXQ8OdFqsPfd4IuW_vPtTLuz-PddBVsa4rysyuy6WEa8TmKHjqA7Ds_unBgF0G5xWEuSqXnawNQNIiqwcBv0tBTmpDkWss-u4pIibTapAwSlB_iwOHaqdDMKSEFpw6gQBNOnMdqK7sKjH7GkaxHrjoSpbK5zkam1szfKVXWVUji_ETTv9XU9s-AmnyZaXLoVjxFx0Ftrl9AWryvSg5zSdVkP_L2Hznx1dAeCBXQmXYONg_mTXtEEWIGCjRlaP9HH7AYZqaoxi1T0WoF9WZdsgy__8FEfdv67oUClM6JtG1j69RANX59VC9hJPeyqBNBSt7zwyc3UcgNWg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🤩
نبرد هیجان انگیز اسپانیا
🆚
انگلیس را در
TrexBet
پیش بینی کنید!
📉
نگاهی به آمار ۵ بازی اخیر دو تیم:
اسپانیا: ۵ برد و ۹ گل زده
انگلیس: ۴ برد، ۱ شکست و ۱۴ گل زده
🦖
🦖
🦖
🦖
🦖
بونوس اولین واریز تا سقف ۱۰۰ یورو
🦖
بهترین ضرایب بین تمام سایت‌ها
🦖
واریز آسان و امن از طریق کارت به کارت
🦖
هیجان بازی، وقتی بیشتره که انتخابت حساب‌شده باشه!
TREXBET — PLAY. PREDICT. WIN.
https://TrexBet.com
T.me/TrexBet_Ir</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/Futball180TV/107293" target="_blank">📅 13:06 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107292">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9fa254372b.mp4?token=oaPmTJoSgZ0_gyoLotPnARPewnE-Is2_sUpB-VJPhwr4F_zjPNwNP_vwXFY5JRqlSpWIbkdXqkyn3CA8gJq-TnxNxMrbxIgseSa2-YAeHqNnwzFJWc_kM1_4SH0nsdmZ4A5HspX1DtDhg3OCME1RRpuzOhrZhKH4MTlDSK_V2PbI9nTTaYbgPmZcecVDN-NIs4_3TFgsWIH9wlOdtZvntHv97tJ6_xDNPBq6jTkeoqNm61PFXsbHiUpkeT1dRVXfc4hYRTKC-Wg05rFKvNfHTymHoIL9R45QoDNwSAm5nLY1CAV5SxdaFdKKfwubofEBR5CF6S_rXVHy_Abqtg9ZnA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9fa254372b.mp4?token=oaPmTJoSgZ0_gyoLotPnARPewnE-Is2_sUpB-VJPhwr4F_zjPNwNP_vwXFY5JRqlSpWIbkdXqkyn3CA8gJq-TnxNxMrbxIgseSa2-YAeHqNnwzFJWc_kM1_4SH0nsdmZ4A5HspX1DtDhg3OCME1RRpuzOhrZhKH4MTlDSK_V2PbI9nTTaYbgPmZcecVDN-NIs4_3TFgsWIH9wlOdtZvntHv97tJ6_xDNPBq6jTkeoqNm61PFXsbHiUpkeT1dRVXfc4hYRTKC-Wg05rFKvNfHTymHoIL9R45QoDNwSAm5nLY1CAV5SxdaFdKKfwubofEBR5CF6S_rXVHy_Abqtg9ZnA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
❌
👀
بهزاد داداش‌زاده بازهم یک ادعای جنجالی داشته و گفته که مجید جلالی جادوگر است!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/Futball180TV/107292" target="_blank">📅 12:45 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107291">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bbf4bbaac4.mp4?token=k_CdlTlikvaWZ1SLuGuTIySWJABRMNCD9lcRFMSkBrNiGsB_3cgQQrEOR-gwNCOmJ0IowktSuiQz9dzSDhuTbhpuo3QekOXcwqSbV3eXUcjo85qAsIumZ5rPOKDZHiN5SecC6Sc-xWdxtsddcOJNPVfpFRW4DL7U-wmFWR4YHMuqthZbPOgf6XE-rrvPWCdDW6eX4og2PGj9Dw0Ggx1FXth9vycF5h14E4_2Laby7uQAbuzsr-UQ-br2uXpInxKpL1a2Nz76da2vm2uZlmVQe-wTcuD8CMy1cr7afq6WV7QuWDzqLh9usMKByfZgPHC1X0cli9-7EoCtKQndPFGN0A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bbf4bbaac4.mp4?token=k_CdlTlikvaWZ1SLuGuTIySWJABRMNCD9lcRFMSkBrNiGsB_3cgQQrEOR-gwNCOmJ0IowktSuiQz9dzSDhuTbhpuo3QekOXcwqSbV3eXUcjo85qAsIumZ5rPOKDZHiN5SecC6Sc-xWdxtsddcOJNPVfpFRW4DL7U-wmFWR4YHMuqthZbPOgf6XE-rrvPWCdDW6eX4og2PGj9Dw0Ggx1FXth9vycF5h14E4_2Laby7uQAbuzsr-UQ-br2uXpInxKpL1a2Nz76da2vm2uZlmVQe-wTcuD8CMy1cr7afq6WV7QuWDzqLh9usMKByfZgPHC1X0cli9-7EoCtKQndPFGN0A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
💥
گوشه‌ای از نمایش‌جذاب هلند زیر نظر ژاوی در اولین مسابقه رسمی مقابل آلمان
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/Futball180TV/107291" target="_blank">📅 12:20 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107290">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b671734a24.mp4?token=eZWIdJTtiCrLol8-oEUo_tFSIQy8xH84GMyT2-4Gz8xXExKP2007DuaSdBKm_kIgm90733bHo4cMSzMwGi8EuQyO3Ann9B-5M_Y9AAUYQZWii_Kqz_0zxPaIxr6_nEhIWU5ZYHCSMA9e97cfhis295nRzdtkv2_D532hJHUytBE__D8H1wt47AK6Y74CiuOiSEvjvWdp8uQ9A-B6Fmxc4pXV1KMQgfjRYmSlzsSy3ursnssvXQ6XS5lOSQ9RuG4Q6_SzdqoBth9UDr_KJxtZ7GNsxcECykrFXVNMdF7uL4F1_pZm89T_YpwiArUkDL61OpKT8mKdCeEeDtAvgORxEA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b671734a24.mp4?token=eZWIdJTtiCrLol8-oEUo_tFSIQy8xH84GMyT2-4Gz8xXExKP2007DuaSdBKm_kIgm90733bHo4cMSzMwGi8EuQyO3Ann9B-5M_Y9AAUYQZWii_Kqz_0zxPaIxr6_nEhIWU5ZYHCSMA9e97cfhis295nRzdtkv2_D532hJHUytBE__D8H1wt47AK6Y74CiuOiSEvjvWdp8uQ9A-B6Fmxc4pXV1KMQgfjRYmSlzsSy3ursnssvXQ6XS5lOSQ9RuG4Q6_SzdqoBth9UDr_KJxtZ7GNsxcECykrFXVNMdF7uL4F1_pZm89T_YpwiArUkDL61OpKT8mKdCeEeDtAvgORxEA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
وضعیت ریدمان کریم‌آدیمی در بازی مقابل هلند که حسابی اعصاب کلوپ بهم ریخت!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/Futball180TV/107290" target="_blank">📅 11:55 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107289">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">🚨
❌
⭕️
#اختصاصی_فوتبال‌180
🔹
با تصمیم اعضای فدراسیون فوتبال، حسین‌عبدی پس از رقم زدن فاجعه در ناگویا، طی روزهای آینده از هدایت تیم‌ملی امید برکنار خواهد شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/Futball180TV/107289" target="_blank">📅 11:41 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107288">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1dcbb333fe.mp4?token=iJHcBYrk3uvWVz9zRlzpC_eRV1nPTrXD9PquH9ymubgWGyirLiD9BFpj5n1XsmwsOB5p9EnbA7t2QNwLAwybaGMbM3OemCSAiYmYlM1sZeDLiV-kh4qJHHtYgYhYcM1RzULe24RzyvP4KDU-X3CaPqUhNmS3KyDZ9Le3c38Zi7p4t8vZIsKiZXTalDXLaVzjbgBFi3blPZS_nnAlV2KNjInptVd-tcPJWrz8QhsZefU9HoeNORb96LKNa585oUuIsBBIcV-Rp0j5x2Cgm7A05WyUNapL-vrNfeMyeAuWHqxk92R7zL8VoP9ge3Tj3hrWfS5AuIsLC0KP5JSNXldiCg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1dcbb333fe.mp4?token=iJHcBYrk3uvWVz9zRlzpC_eRV1nPTrXD9PquH9ymubgWGyirLiD9BFpj5n1XsmwsOB5p9EnbA7t2QNwLAwybaGMbM3OemCSAiYmYlM1sZeDLiV-kh4qJHHtYgYhYcM1RzULe24RzyvP4KDU-X3CaPqUhNmS3KyDZ9Le3c38Zi7p4t8vZIsKiZXTalDXLaVzjbgBFi3blPZS_nnAlV2KNjInptVd-tcPJWrz8QhsZefU9HoeNORb96LKNa585oUuIsBBIcV-Rp0j5x2Cgm7A05WyUNapL-vrNfeMyeAuWHqxk92R7zL8VoP9ge3Tj3hrWfS5AuIsLC0KP5JSNXldiCg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
👀
کنایه حسین‌گودرزی بازیکن استقلال به ماجرای سربازی نرفتن علیرضا بیرانوند!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/Futball180TV/107288" target="_blank">📅 11:32 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107287">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/06c8b89d1e.mp4?token=gtTv5s4x6CoFyWfZ6Dg-AM19615Wk8P2WqTvGXo3l6eAea3flfMNQ892_aKy585zAxksT9x7Xzgs68JCCV8UQ3W3DljLho8OJcDMk6kgZwwqbf5eMAKZivNkbC_3OD2dr0BKOAnwLsejJsmlxTiVwQCZmoVknXdQ_yufQVzNTuBi1mSLGLxeudOSjHbZuVhG6ynlLIppednhvGMbkFLWSJ4M3p8YolU0JWv3qQoYfYRv133bgiyEa1VBcNAbZKKAa50np7Cm3wHPcEdX8gyaKe44dGR8FqiLEv0nHoLIl8AWEqUARtmF-lXyptu8g3J6WVZVlq5Q2LUA_xsTGnrtOA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/06c8b89d1e.mp4?token=gtTv5s4x6CoFyWfZ6Dg-AM19615Wk8P2WqTvGXo3l6eAea3flfMNQ892_aKy585zAxksT9x7Xzgs68JCCV8UQ3W3DljLho8OJcDMk6kgZwwqbf5eMAKZivNkbC_3OD2dr0BKOAnwLsejJsmlxTiVwQCZmoVknXdQ_yufQVzNTuBi1mSLGLxeudOSjHbZuVhG6ynlLIppednhvGMbkFLWSJ4M3p8YolU0JWv3qQoYfYRv133bgiyEa1VBcNAbZKKAa50np7Cm3wHPcEdX8gyaKe44dGR8FqiLEv0nHoLIl8AWEqUARtmF-lXyptu8g3J6WVZVlq5Q2LUA_xsTGnrtOA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
👀
تعجب کریستیانو از تاریخ تولد هم‌تیمییش در تیم ملی پرتغال
😄
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/Futball180TV/107287" target="_blank">📅 11:05 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107286">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3dd536968a.mp4?token=FXDqsXh_340Z3uLYHhZ-QK02N73zpOVzyURWU842BSwdbh5GLcfgafZv0JDiCd-b0ZjbWUD4flv-_XLBKk1VsSo4aalfpk51WmGHjK23mARUQ5BmvDh2tx1dNVmTFsYdlMbGDEXHas7B5RNwJpeJ3OqYPo9it-YoAtpGm9FE0keOapwS4t1Vvv5KMTrMHsJtwScZclPMrf1btP3IvQ3G-m1xtRoRDqdN-9p3gHJvowuKpYXbQ4gSwwGMKE62WyFtDPIqtxd-NrR1gQZtSq6Pjm5IeG1-cGsKV5ZGLhH33-l8AF6PdBYWgLu1qFE_XhtGT6XUZOtVD0VTEEcfUj6S0A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3dd536968a.mp4?token=FXDqsXh_340Z3uLYHhZ-QK02N73zpOVzyURWU842BSwdbh5GLcfgafZv0JDiCd-b0ZjbWUD4flv-_XLBKk1VsSo4aalfpk51WmGHjK23mARUQ5BmvDh2tx1dNVmTFsYdlMbGDEXHas7B5RNwJpeJ3OqYPo9it-YoAtpGm9FE0keOapwS4t1Vvv5KMTrMHsJtwScZclPMrf1btP3IvQ3G-m1xtRoRDqdN-9p3gHJvowuKpYXbQ4gSwwGMKE62WyFtDPIqtxd-NrR1gQZtSq6Pjm5IeG1-cGsKV5ZGLhH33-l8AF6PdBYWgLu1qFE_XhtGT6XUZOtVD0VTEEcfUj6S0A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🙂
محمدصلاح رفته تو کوه‌های ترابوزان رو یه سنگ نشسته و حالا شهردار اون منطقه اومده سنگ مورد نظر رو جاذبه گردشگری کرده‌ تا مردم از نشیمنگاه صلاح دیدن کنن!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/Futball180TV/107286" target="_blank">📅 10:40 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107285">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d4c6cfb864.mp4?token=IPTNEOLdS-PeYzLSHakvuCgTDf0GequIsgZU5mtiQZVnfS27gMVd_GkSVuIl2gfjJJxt7WxoPabM-VWBQ6tzgGiZY7fjlyxYmiNsk9ThQs2N79YutW7-vjTF4HcOySKzB6CHQn4lr4v-FgVYPRX2Rqvgafov1Kg7T3OW4COVewH6dMmgjuk1kw8Mb1_D1PVzbqjh0YP1LnKSBMqk7gnjUIiixKXv9nMnFbFDhFwnCcohf7Cs8C6pBzzIX8Q22II2uD_EqLbsgbebeVlh4HVWbGh8PCXxWAMPYUYPnXCcEfYXWm1hZK7fj-aT4DfNR5YABg8NWApINdQYkPMB5xcS6w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d4c6cfb864.mp4?token=IPTNEOLdS-PeYzLSHakvuCgTDf0GequIsgZU5mtiQZVnfS27gMVd_GkSVuIl2gfjJJxt7WxoPabM-VWBQ6tzgGiZY7fjlyxYmiNsk9ThQs2N79YutW7-vjTF4HcOySKzB6CHQn4lr4v-FgVYPRX2Rqvgafov1Kg7T3OW4COVewH6dMmgjuk1kw8Mb1_D1PVzbqjh0YP1LnKSBMqk7gnjUIiixKXv9nMnFbFDhFwnCcohf7Cs8C6pBzzIX8Q22II2uD_EqLbsgbebeVlh4HVWbGh8PCXxWAMPYUYPnXCcEfYXWm1hZK7fj-aT4DfNR5YABg8NWApINdQYkPMB5xcS6w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇮🇷
🇮🇷
کنایه گودرزی به ابوالفضل‌جلالی مدافع فعلی پرسپولیس: زمان مشخص میکنه کی استقلالیه!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/Futball180TV/107285" target="_blank">📅 10:15 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107284">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e4908c84c8.mp4?token=vGeEVx7DYqchxc5SAp3DK9Ov_UXd4JV3wM1GuyA1sAK2kj4gyTdr8QWs0xtVQaFEvgPi2Ld2R75VUoijvWTFSuVmWP_Q_d01KJYGNRtbtY0DBv_dI3BPFMEj4J7uBKV38-M9DwUwhhg4TNpjksT0vGPd4tBZOp0UXyr7EAlKCalhe80N32gR7amHwqOu_kRMM1hiQRdoHE2-mJQ2Aakqu8c_oofqhN40U3E3ynru5eG3yZY5y7KgE5jK1_P3ZM9XH4EtzJl2Udxy6YAlzE0RZffBRLRTF8o3gjoR8YICia--3B_MvsjjXyqT0GojA8ZCUOkJXCNGtTWmGq0QwR4_Uw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e4908c84c8.mp4?token=vGeEVx7DYqchxc5SAp3DK9Ov_UXd4JV3wM1GuyA1sAK2kj4gyTdr8QWs0xtVQaFEvgPi2Ld2R75VUoijvWTFSuVmWP_Q_d01KJYGNRtbtY0DBv_dI3BPFMEj4J7uBKV38-M9DwUwhhg4TNpjksT0vGPd4tBZOp0UXyr7EAlKCalhe80N32gR7amHwqOu_kRMM1hiQRdoHE2-mJQ2Aakqu8c_oofqhN40U3E3ynru5eG3yZY5y7KgE5jK1_P3ZM9XH4EtzJl2Udxy6YAlzE0RZffBRLRTF8o3gjoR8YICia--3B_MvsjjXyqT0GojA8ZCUOkJXCNGtTWmGq0QwR4_Uw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🙂
🇪🇸
وضعیت روحی مورینیو، هم اکنون:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/Futball180TV/107284" target="_blank">📅 09:50 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107283">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c02c187832.mp4?token=UeDA-7EmofseyznF4nPXMlLoM2YpZIkGKiLxq621N0KnOVynQZMftM6RLXC6ZYYlVbo-LAHWIlvzdxaYJqpp7n2BIjkvD13GR42K6OJK2PFBfCHjtxfIRRMSyS31DR6qagpeiQ78i_1eUIT9DmQnFAiS-vWjjCVoyWP6vRzwolUuKge__bMKHlHyL1b98qXMz8W5GzpuBngeC2a1DMacT6kJowXyoex14p1jQ3UzPuHDGN-M2o9tfl2ZI3GHtm2hROtqjXkme2aR9ctRQpiAGBxD6OXem3Y7iczqu7MOS1SUw7qTJ1Ud0Ygk7Z8wnvoG5tm1TdSlgPgIvyAPFwUlow" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c02c187832.mp4?token=UeDA-7EmofseyznF4nPXMlLoM2YpZIkGKiLxq621N0KnOVynQZMftM6RLXC6ZYYlVbo-LAHWIlvzdxaYJqpp7n2BIjkvD13GR42K6OJK2PFBfCHjtxfIRRMSyS31DR6qagpeiQ78i_1eUIT9DmQnFAiS-vWjjCVoyWP6vRzwolUuKge__bMKHlHyL1b98qXMz8W5GzpuBngeC2a1DMacT6kJowXyoex14p1jQ3UzPuHDGN-M2o9tfl2ZI3GHtm2hROtqjXkme2aR9ctRQpiAGBxD6OXem3Y7iczqu7MOS1SUw7qTJ1Ud0Ygk7Z8wnvoG5tm1TdSlgPgIvyAPFwUlow" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
🎙
🇮🇷
کنایه توتونچی به ابوالفضل جلالی: یادش رفته بود، که گفته استقلالیه!
😁
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/Futball180TV/107283" target="_blank">📅 09:25 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107282">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NrU-veLiGQyFYGbtNHS1DVngLFzeOeCZZsmu8KP1DXTZCuNdHsPSh-W80nQvzQmg4SiRFyk2WqHK5sQpPFD-JxdQ1BGToGSNb0137mn0dyRxKKsQVBR3SBBVYT1EEpbw4OjxfHpeIc5hci3cdZml5y1u43Fb2NALUPURnWZfKDaoN73yNAu2pJniJy3_VxEJitZ3rKuyOgJfnDyikF9Vzp4HGU_VO4ItEcKHAtDa7AeFBIbTO-o12G3kvABv1ji0bYG5mcK33_vJ4rr3grFjAAlBC0AgkMBqVkxvrZcfae13A4OAp93V65K1bRy_YNBuXF09blaX-mxaGoxbzioCrQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚑
🇪🇸
آخرین آپدیت از بیمارستان شلوغ رئال که کیلیان امباپه هم به این لیست اضافه شده!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/Futball180TV/107282" target="_blank">📅 09:03 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107281">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SZy5g_VHoOah7G6gt3wG5he9psXBO4UPWMN98H3Kw8Bqlojq6E09egKdSus4fGHsJ6Yl-ihdJV0SODWc04s2-oLszXPZSEWyA5pMv4-KCt3qP6-zUieAW2f6jRjyemAsv2xWwMK8RmsRZctrnhPpt0NU8atu6bUcD2tXDJVGysJu9z852vZE-hX7ZHASccKmZSL0hMhWQMm0gqVTzxBw4yu5-GK6ef0VCFVeM_JFNomuCEmBusY5pOP3pg62WJsJKgBjHsuFw9kggfrqcBUEXlrKH52dJ3T166GFFfEQ2WuEij-Bbns1Lf2eV0JDvhbM5FcGI6zNh7LCV-DKWxUDkg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🥈
تیم‌ملی کبدی بانوان ایران با شکست مقابل هند به نایب‌قهرمانی مسابقات ناگویا دست یافت
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/Futball180TV/107281" target="_blank">📅 08:51 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107280">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4d41de8e91.mp4?token=Df6SbC1tP_FX5ytJOJ9vhOU0q6jeVQRhXLlPkLUJIGIVDvbgqLPkjgijq8dvb9QyVJPnPVnCvZifHHf38RtGD8Ts54hlzdeoxSaqh4fViwJ0By7izUeKR6zQQEsVJqCuLjFwVKKserbLZW3268WTQw3WZHhkApZfTE6riJyBjyupvTs0cVA1kg11KOAscDTJCBLeecO5rTnIscV8cMY0y-vQkmBKBkSOv8rORc49-qJ_facFuT4Lwmto0E4aZ4vaC4WA1STOJAwKNa4ZJzcHnxPfNuXh0axrZ4Ari7C9WEBWwOslVPHucvtZQlVuXvmFI4Bn-F6FFvl_oc7Dqa8y4Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4d41de8e91.mp4?token=Df6SbC1tP_FX5ytJOJ9vhOU0q6jeVQRhXLlPkLUJIGIVDvbgqLPkjgijq8dvb9QyVJPnPVnCvZifHHf38RtGD8Ts54hlzdeoxSaqh4fViwJ0By7izUeKR6zQQEsVJqCuLjFwVKKserbLZW3268WTQw3WZHhkApZfTE6riJyBjyupvTs0cVA1kg11KOAscDTJCBLeecO5rTnIscV8cMY0y-vQkmBKBkSOv8rORc49-qJ_facFuT4Lwmto0E4aZ4vaC4WA1STOJAwKNa4ZJzcHnxPfNuXh0axrZ4Ari7C9WEBWwOslVPHucvtZQlVuXvmFI4Bn-F6FFvl_oc7Dqa8y4Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
وضعیت دیشب امباپه که شرایط نهایی این بازیکن تا ساعاتی‌دیگه مشخص میشه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/Futball180TV/107280" target="_blank">📅 08:02 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107279">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/Futball180TV/107279" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBe
t
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/Futball180TV/107279" target="_blank">📅 01:34 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107278">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/X61xe__uQxUSWC5C_KPZTNM_VghnSj1IJDdAn4CStVKJUAzjmoeMV99r-7mqYajnEY-6RtE8VjGYmiLag78MK2HVeeYOoDNdf6X8gMDi0f890vDRaDp6AkMo8-4kLzEk8ibHNJXAvVI_LwyUMofFU6WGqK0Q9MtkbQrywxl9cP5nXgTEqSYjJzF7mVlGl5Ut3VEt-d5DbGcq0Fiq6wzwaBlKrSbtii2oT1TBo8RgLPBvgEYm82xQY1kqCgLuMdFBto353udiAtoiaBHPrLjHAQp_1cfS8jPCzcnDTtK2QUThfHHfuu7fIo0j8UOyxP7MM2GO_UP6X4EcNneq2A7kjA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🦖
فقط یک بازی از میکس‌ت لوز شده؟
پولت برمی‌گرده!
میکس می‌بندی، هیجان بالا میره، اما یکی از انتخاب‌هات خراب می‌شه؟
با پیشنهاد ویژه
TrexBet
، در صورت رعایت شرایط، می‌تونی
۱۰۰٪ مبلغ شرطت رو پس بگیری
.
همین الان وارد سایت شو و شرایط آسان‌ش رو مطالعه کن!
💰
🦖
🦖
🦖
🦖
🦖
بونوس صدرصدی اولین واریز
🦖
واریز آسان، برداشت سریع
🦖
سرعت بالا، طراحی حرفه ای و تجربه ای متفاوت
https://TrexBet.com
T.me/TrexBet_Ir</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/Futball180TV/107278" target="_blank">📅 01:34 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107277">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TaBa34UNimUrOvypiFQq0pwUYDz8FER-M08ieL2pS-ITksKQih6LDq11bcweUs6iRn729mF2pdkCNww4PvxVT3w1a6Nq80aGVc-dKAiGdlZ89a-W0uGq1yaFByOqLP9OnJzu_Tz4P8gSHiCBXF_KGa-HsV1RxMxCeGei-4UVpac6aJ5Odm6wDwg8idRR5y7EpEE73XTMs57DWuY0gffGqyvbVb1UmkL3_n-SMg384IN60QVqM3-dT_D4gScaXjNi-3_RRsn0foJVxpg7Tnm1-DBOBWSaba7Y_BlZuYdiYZCs7IfLoqrABSmLAwevEKsVNZ1GQx-KhtIeoapOHWmElw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
✅
©️
با اعلام سرمربی تیم‌ملی آرژانتین، کوتی رومرو کاپیتان اول تیم‌ملی آرژانتین پس از خداحافظی لیونل‌مسی افسانه‌ای شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/Futball180TV/107277" target="_blank">📅 01:28 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107276">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fdKYGOu76t0G7CfkycJBoMG5ywCt7Aix5IXias4_I8jG2DFqz_9cBRt7d_w4MKmG0aSjVVOQzkFW6DcIIc3KN5QxYsDcSCfseJjNON0ZLpEzqI2bigTn8BoD2iiTRCJXNH8vEjxmLVqsCbtfvN5nMZMKfUyU4v59vKJjVxMvUQPpApD2KTV6hpaQWYg4DMyohG4-C6kUf2G3Y8cODvuyUxi0WMLLdlhM7t_rxiQpC8dJb6qquUDaZjegKVp8wj8MQLLWUJUBEIYMUWjwSXB32zm6nQpz0Y5KNMxMtzde1gRWtDpTDGd6ZOYBNykI_uRtZy6_gB9RgdT-8HuAkY-6Qw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚑
رومانو: امباپه بدلیل مصدومیت زانو از اردوی تیم‌ملی فرانسه جدا میشه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/Futball180TV/107276" target="_blank">📅 01:19 · 04 Mehr 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>

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
<img src="https://cdn5.telesco.pe/file/gw7Tg4_vfh-B8uR4AuNRTXYvezKa7no1Vc46KaIG3kxTHJeIMgmWahIZbJQrE2LrNyISWBvQM6L3bzJYkm6n-Xaka59Ah6VotXaLl0z2VBU2S52btaUi6Gk7ELruInhWbAHF3hv-N7Iy1ToqhNzs5Xqf5mdhPeHXMlBqZQbWOvXb88pRJbAVFR-2tZP6Wiq79WDm-0HP9q-iXl1u-QhDOn7XhS0b3u7GAe5_4jLy2yfjSx78G2NcEu8AbAFEM2HZG8aDrJ1h91plFZp8SbNw9g4u7qecxGpuwV94SOjZLUEZ4GwYf6AVOlFSlpQrUCAXJchwX_bv_v4LeHq6a7f9tw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 فوتبال 180</h1>
<p>@Futball180TV • 👥 420K عضو</p>
<a href="https://t.me/Futball180TV" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 In the name of God; The only popular sports channel on Telegram: All for Iran...🖤We respect the copyright laws and follow the laws, Mr.@Durov...🙏🌹Contact ads:@TivaAds</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-18 22:26:57</div>
<hr>

<div class="tg-post" id="msg-106056">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1dcba68c3d.mp4?token=NwFYOcwVskO7aA_OU-tFjzB68dPUgnuAhmfWB4ZU3RNDFU1vFSuvJ462so3FXFMjlexiqs_biRiuCZMtK74HuMJggCn56ZJnTmmPcfZ1Rp3PqwXkriKMK31EClMBT21jJP7I3aMp2KS3CDQc_9MLgO4JWkFOlRkej-i6gfzkoJHVYaAzktHyqp4FGhcpNrOdT__QjFeCM6-zxYnCS9F9laFJTRAPeJhW4m5m5wNxsG_eH81O2FVHy6uoNGfldpevAAYZwjLTJZ8gZQ7KepkpYWsiCKRtaoIUq4t7uSJo5KJOopWxj8HEvW3YnCZ3S-scU6ESjnJYjLsId0AQvgkWew" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1dcba68c3d.mp4?token=NwFYOcwVskO7aA_OU-tFjzB68dPUgnuAhmfWB4ZU3RNDFU1vFSuvJ462so3FXFMjlexiqs_biRiuCZMtK74HuMJggCn56ZJnTmmPcfZ1Rp3PqwXkriKMK31EClMBT21jJP7I3aMp2KS3CDQc_9MLgO4JWkFOlRkej-i6gfzkoJHVYaAzktHyqp4FGhcpNrOdT__QjFeCM6-zxYnCS9F9laFJTRAPeJhW4m5m5wNxsG_eH81O2FVHy6uoNGfldpevAAYZwjLTJZ8gZQ7KepkpYWsiCKRtaoIUq4t7uSJo5KJOopWxj8HEvW3YnCZ3S-scU6ESjnJYjLsId0AQvgkWew" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
🇺🇸
ترامپ: حملات بیشتری در تنگه‌هرمز از سوی ما رقم خواهد خورد. فقط کمی صبور باشید
!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 1.23K · <a href="https://t.me/Futball180TV/106056" target="_blank">📅 22:25 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106055">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/siYKcX0gVdj-KtqI6uj7k6BDhQNY-EwVOIWfH_6K3smAMbfWgE8NBEOBQhfq5f43Sf8dKIShQR1omJcXqWmOqs6ThaYGM5BKPqcZ1Nr7TXD8ytBk5EJTCjadQkIf_w2-a2V9L7RGLLt6KGjI1ErjVcdZ_kpX_BTVl3BTE3cTljuhyugi-0Huji_2bi8vSZaV02b8eM1TcertCIuWHvmBm9h8rWJ0GIz3wjo7hT6NtHM1NWwLC9HjnSfNttfgwXbo3LeeMnmjFNiKvlEivQ5zZzMvoUh9yeKiTLZocQJjfGZSauuzUluBE9ve4IYYsTHLLQC8BgWkptkpXFpV4mygYQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
✅
🇪🇺
هفته‌اول لیگ‌قهرمانان اروپا؛ معرفی قربانی جدید تجاوزهای بارسلونا؛ فاینورد در نیوکمپ تحقیر شد؛ رافینیا و یامال مجددا درخشیدند
🇪🇸
بارسلونا
5️⃣
-
1️⃣
فاینورد
🇳🇱
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 3.97K · <a href="https://t.me/Futball180TV/106055" target="_blank">📅 22:12 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106054">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RcGQ6nzWy8yWO_lxaxbQ1Hg5s9Qj_jwbZGbkqTNGFBhg_HuBr14EQxuC_NN9dgOP3xddX4NID7Yt7BCDll46vGjl07CXZWFJnGit2J6IRBtUZ7-Xkh6EzNfeUUSVqJMFJx5RboIidkGZJhCNGHuOUSLbgSI53m-QWG5vEivlfaH-YeeiNJF2SdkwpOQKWkd0t_kh93m-kW0GdCXI9zbVQRJc-L2qaVWA6dcAQOpxOZB7_T4zRLV4CUw-9MKFVlvWhUAE6vjdxr1LoGCAQ8KEzu5UC6PGvfPz-yY-F-Nnn9WN_prLG0KwdPCwM46Yp-Z8ieQfFeU1yCQAYPhpaImVTQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
✅
🇪🇺
هفته‌اول لیگ‌قهرمانان اروپا؛ معرفی قربانی جدید تجاوزهای بارسلونا؛ فاینورد در نیوکمپ تحقیر شد؛ رافینیا و یامال مجددا درخشیدند
🇪🇸
بارسلونا
5️⃣
-
1️⃣
فاینورد
🇳🇱
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.58K · <a href="https://t.me/Futball180TV/106054" target="_blank">📅 22:09 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106053">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/0430c92c86.mp4?token=cc6brR8zAktXvzetBjR3rlgZQ90_5iCqpu4FXTuhhrvd_etQ9IFOzgppRFHALJ2nKo7YrgVxVacs7U-Ve84trrk_aNTPNgbI2ySaCmOlttSBNUPPyDrbyY2sP8al1rCfVJYZRLJzaW7IzkJ6S2DJcl6fD9kFz-XlOPqDSqEDoGeBQKTmAWQXMfTO_SjkicHhrZQkJC116i3o2FU_zAqxFmBvx3E2AeLed9r1i5s08K4oA8y4qhVXEXcVHjZ2aqPYqndzoUEH9HIHJBl6ktNZUyga7uj-C78bEtMupyurh5nDWdK70l4PkVHiCqJ_qFVbnXsEb81pCxNVPltEl2p1zwTtO3nP5ViqS_eWoCQSHyEh79yheMefd9EX56c3oPKWBIvE25Zs4_iydYcCzGQeLsQftWft9lHg1IH_fO6JF-5DHhkpSGZEsvxDJiRGopX_PqHOQXhmyw7wwxTWNV0Vyi_LqojPOi-VnH1BxwdRQf-yI6YyhSEdZTOHiwbiFXXPWQvjhH3KnIHHqZBwykJs8LjSHlCxJw8GV7Dw4Hm9_-X-mpJGSaOuc7S6HkV2Aazjo7AcML7DnIM5jjORj6_j3X9afWaiScFlHor7HeWkNoYQqti5JQo7myt95ABedHL90dE1hARUv3wt-LGsoOgWuY6PLcHmhsxM4zIJTLAez8A" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/0430c92c86.mp4?token=cc6brR8zAktXvzetBjR3rlgZQ90_5iCqpu4FXTuhhrvd_etQ9IFOzgppRFHALJ2nKo7YrgVxVacs7U-Ve84trrk_aNTPNgbI2ySaCmOlttSBNUPPyDrbyY2sP8al1rCfVJYZRLJzaW7IzkJ6S2DJcl6fD9kFz-XlOPqDSqEDoGeBQKTmAWQXMfTO_SjkicHhrZQkJC116i3o2FU_zAqxFmBvx3E2AeLed9r1i5s08K4oA8y4qhVXEXcVHjZ2aqPYqndzoUEH9HIHJBl6ktNZUyga7uj-C78bEtMupyurh5nDWdK70l4PkVHiCqJ_qFVbnXsEb81pCxNVPltEl2p1zwTtO3nP5ViqS_eWoCQSHyEh79yheMefd9EX56c3oPKWBIvE25Zs4_iydYcCzGQeLsQftWft9lHg1IH_fO6JF-5DHhkpSGZEsvxDJiRGopX_PqHOQXhmyw7wwxTWNV0Vyi_LqojPOi-VnH1BxwdRQf-yI6YyhSEdZTOHiwbiFXXPWQvjhH3KnIHHqZBwykJs8LjSHlCxJw8GV7Dw4Hm9_-X-mpJGSaOuc7S6HkV2Aazjo7AcML7DnIM5jjORj6_j3X9afWaiScFlHor7HeWkNoYQqti5JQo7myt95ABedHL90dE1hARUv3wt-LGsoOgWuY6PLcHmhsxM4zIJTLAez8A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
🇪🇸
گل‌پنجم بارسلونا توسط گابریل‌ژسوس
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 5.19K · <a href="https://t.me/Futball180TV/106053" target="_blank">📅 22:04 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106052">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">گابریل ژسوس
😂
😂
😂
😂
😂
🔥
🔥
🔥
🔥
🔥</div>
<div class="tg-footer">👁️ 5.49K · <a href="https://t.me/Futball180TV/106052" target="_blank">📅 22:00 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106051">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">پنجممییییییی بارساااااا</div>
<div class="tg-footer">👁️ 5.5K · <a href="https://t.me/Futball180TV/106051" target="_blank">📅 22:00 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106050">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">گلگلگلگگلگلگلگلگلگ</div>
<div class="tg-footer">👁️ 5.19K · <a href="https://t.me/Futball180TV/106050" target="_blank">📅 22:00 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106049">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/e47209925e.mp4?token=Fy0oqAH1VO9foaQfOzhxms81XdwVqo0_eef4iTzxnpGCc2iMKGFApwC-6U-LZf84WZuMg7TAXSQZ2DS1rsNdRKL3vmR7HRLqZVTFPd4B5hghQQ5yQyTCZCRWnzuBYeVjZVRo_Q_IEc0SZm_L580KT-D5aaMpZ42g6-pmhtKr-pyyxucdq1XtUDiNGqC9JNTGChWfGy7gT-OsAbrgZlcao1B30aF1M9zRILZQvvmrAq1t15GbiVFYQ835kBZWXbXQlT9RLDXGC26A0ax6-L12CkHglxfxo-_lLb4czSWtWJJxEfq8YDemw9wbTantCh08nSvk-KL1fUUzgdt5WYWDz4BIQ3stLI7CBusOJ-KgkA8ry6zVX9zZJ-dd_H8Bu9TCwm8QWtqZxUgeWnIh2LmaN_zxWmqdUsP6GLd4dO0yhYX0ae9_zTmU8kP-uXxZOEsPdbIUxc7q1__rpTrnCSHsJ9_R6wYoHHl2rFxa5w5AjPYypCsOdWMtt5cf-yc_XQVLA16MMPVWUguSQBnqa9ZzcijWoWpIpZqxfLSW8UhOxqu4Ep9pcTZwy5loZaBRs3KkhkbTBApjgF6nSKMek55HrmbJtnKEvunv_FsNRgILqTViiWNpP_B7zm71cBSSl4RaWV3dfaHu5J1ZBp2Tg4ma3VbKW40M22V3PY1YuRlelP4" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/e47209925e.mp4?token=Fy0oqAH1VO9foaQfOzhxms81XdwVqo0_eef4iTzxnpGCc2iMKGFApwC-6U-LZf84WZuMg7TAXSQZ2DS1rsNdRKL3vmR7HRLqZVTFPd4B5hghQQ5yQyTCZCRWnzuBYeVjZVRo_Q_IEc0SZm_L580KT-D5aaMpZ42g6-pmhtKr-pyyxucdq1XtUDiNGqC9JNTGChWfGy7gT-OsAbrgZlcao1B30aF1M9zRILZQvvmrAq1t15GbiVFYQ835kBZWXbXQlT9RLDXGC26A0ax6-L12CkHglxfxo-_lLb4czSWtWJJxEfq8YDemw9wbTantCh08nSvk-KL1fUUzgdt5WYWDz4BIQ3stLI7CBusOJ-KgkA8ry6zVX9zZJ-dd_H8Bu9TCwm8QWtqZxUgeWnIh2LmaN_zxWmqdUsP6GLd4dO0yhYX0ae9_zTmU8kP-uXxZOEsPdbIUxc7q1__rpTrnCSHsJ9_R6wYoHHl2rFxa5w5AjPYypCsOdWMtt5cf-yc_XQVLA16MMPVWUguSQBnqa9ZzcijWoWpIpZqxfLSW8UhOxqu4Ep9pcTZwy5loZaBRs3KkhkbTBApjgF6nSKMek55HrmbJtnKEvunv_FsNRgILqTViiWNpP_B7zm71cBSSl4RaWV3dfaHu5J1ZBp2Tg4ma3VbKW40M22V3PY1YuRlelP4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇳🇱
گل‌اول فاینورد به بارسلونا دقیقه ۸۲
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 5.5K · <a href="https://t.me/Futball180TV/106049" target="_blank">📅 21:59 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106048">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5cbc91a214.mp4?token=AnOqd8IcSpvxgiETr0_9_6q9b6EIw-kDK4v49I3N8bCFZuvG_IaDTwhmal6utpG-drf3EYZq8g03sov2PN7pGrr4Y_zlM0186PlGDFdIqtJoT8MJ606-wh5UWVZ9Gbh73e5OWLxlqdPWR_5HG3lubQxkRCiTBR3cn0yYs2dnDl71CJx2IXxjkl0wRElvu9zcWHqS8GJa7L9vyeO3zUWptN4vUzlr1T7VOUuAPdyjt3dzn7KVTblzRuy3Ypa5S5zwMzkacXDBUbnURaaNt3WNaTN9akb-1RZsfD7fqp2UFVT4dz3kv2KwHp7f8TqTyQvw0ia7b3wiHbUNlO9GQmXNdQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5cbc91a214.mp4?token=AnOqd8IcSpvxgiETr0_9_6q9b6EIw-kDK4v49I3N8bCFZuvG_IaDTwhmal6utpG-drf3EYZq8g03sov2PN7pGrr4Y_zlM0186PlGDFdIqtJoT8MJ606-wh5UWVZ9Gbh73e5OWLxlqdPWR_5HG3lubQxkRCiTBR3cn0yYs2dnDl71CJx2IXxjkl0wRElvu9zcWHqS8GJa7L9vyeO3zUWptN4vUzlr1T7VOUuAPdyjt3dzn7KVTblzRuy3Ypa5S5zwMzkacXDBUbnURaaNt3WNaTN9akb-1RZsfD7fqp2UFVT4dz3kv2KwHp7f8TqTyQvw0ia7b3wiHbUNlO9GQmXNdQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🔥
🐐
گل‌شماره ۹۷۹ اسطوره کریس‌رونالدو
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 5.5K · <a href="https://t.me/Futball180TV/106048" target="_blank">📅 21:58 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106047">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">فاینورد بالاخره یکی زدددد</div>
<div class="tg-footer">👁️ 5.19K · <a href="https://t.me/Futball180TV/106047" target="_blank">📅 21:57 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106046">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">گگلللگللگ</div>
<div class="tg-footer">👁️ 5.19K · <a href="https://t.me/Futball180TV/106046" target="_blank">📅 21:57 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106045">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/064c2da039.mp4?token=KyNUc2i9zW0bRzPl83FTw17od59UHJi6ymU6-kSbYmDjMsgU_e3vDicuk9fNbMw5dKe1u60IvNQE17G3VYgEmEVAF5bKSA3AVWyHSlLGqBXuKWc7P9QXVo_hEShxwK5vphfgdsL_BIAeeTXcbUkHI15nHRB3kT7RGn304vn2g-OPK2CIA2RgQJgoiXRBH2-g42vQmS9yRk-wsF4Ag1T-KyLY7Rqqvpw552EmZ-cyICEsWfs5JV8xXcSOzPtHddHynXNhPIKWbIa9ym3pM6KEwuXrMhCQfA_2E-z7rVjpUQVtY-fU36yscJHIqkr9PWFPC0RsBi3tLhpHEhkbquXIHw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/064c2da039.mp4?token=KyNUc2i9zW0bRzPl83FTw17od59UHJi6ymU6-kSbYmDjMsgU_e3vDicuk9fNbMw5dKe1u60IvNQE17G3VYgEmEVAF5bKSA3AVWyHSlLGqBXuKWc7P9QXVo_hEShxwK5vphfgdsL_BIAeeTXcbUkHI15nHRB3kT7RGn304vn2g-OPK2CIA2RgQJgoiXRBH2-g42vQmS9yRk-wsF4Ag1T-KyLY7Rqqvpw552EmZ-cyICEsWfs5JV8xXcSOzPtHddHynXNhPIKWbIa9ym3pM6KEwuXrMhCQfA_2E-z7rVjpUQVtY-fU36yscJHIqkr9PWFPC0RsBi3tLhpHEhkbquXIHw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
گل‌چهارم و تماشایی لامین‌یامال مقابل فاینورد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 5.5K · <a href="https://t.me/Futball180TV/106045" target="_blank">📅 21:55 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106044">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">سوپرررررررر کاشته تماشایی لامین‌یامال</div>
<div class="tg-footer">👁️ 5.5K · <a href="https://t.me/Futball180TV/106044" target="_blank">📅 21:53 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106043">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">گلگلگلگلگلگللگلگلگل</div>
<div class="tg-footer">👁️ 5.5K · <a href="https://t.me/Futball180TV/106043" target="_blank">📅 21:53 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106042">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">✅
🇮🇷
👤
برانکو ایوانکوویچ: بزودی برای تماشای یکی از بازی‌های پرسپولیس به ایران می‌آیم و عشق و علاقه خودم را به این تیم بزرگ و تماشاگرانش تقدیم میکنم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 6.42K · <a href="https://t.me/Futball180TV/106042" target="_blank">📅 21:47 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106041">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Sk-9JGeZreaTcFmJ2q6xaMJG6G0WMVCB6Grdu8VYJRG3y-opfgHAkmddkiJcdWkFhRWo7MhSGk3loH8zUXV_wuHYnUp3VEZHr7SctAWJpqhPxbsbPCBAPfr1uNmjdQIbmwJfcQvjg6O9Hi0ekNy6i2fx0d82vTL1WjP4tzKAF7re1ijW_Xetqiu485ZsHABmv73_WNoC35kvm8zmhgJDtAAjvZpZ9ou2-G4pulWQzNto-PFkZthOv6F9LcnaCO9JdjwpofUIzaNwu1tq2gmr7dAtc3hAqaiIKB3-ofwmQwtLAqLMlYxH_KkyPNe9hrgWrHM3z37WWpXq0zwHulr6tg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🚨
❌
گل فاینورد آفساید اعلام شد</div>
<div class="tg-footer">👁️ 7.32K · <a href="https://t.me/Futball180TV/106041" target="_blank">📅 21:41 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106040">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">🇳🇱
گل‌اول فاینورد به بارسا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 7.32K · <a href="https://t.me/Futball180TV/106040" target="_blank">📅 21:36 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106039">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/890fd0d430.mp4?token=gpVf3xiDiOsoGgtyKtc0ZftMIU9mYHM9rBZPz_GWikcsaJtJkiBzFYkEBVercBLTqieNMJB7CbArvw204k2ghLh0Vlke1ET9GWZaoo3VRbIS3-qkDBZ6A6oG87joGtLTSkviVaMfSK18hibs9-Hu9UgK1F_ZLnOQRLs1YOejYva-b-fLtavCRFXHsWnFuc30h4Fh2RraTFVW7kHcS6FQv0-Ljq-PUlqMaVKA7OyFjkUoJdavJ2WuhWZCa9iytHiHc_yR3smeYXS_vXK5UpUGa8AB3PzfQ17EKSnaXUja7El9oxqBZdsLY-ovUUfejIMBDip63Ft3oyBte1cwPXQCDaL9mywGSjFYJSxZy_04le3wQfFaxmXJfubAOVeminY1tMqw8GtIh5plP9IgSv1KOdVHhjq6bs8MhS_ZJHycqAOJ7KvR0mYGe40jVtdOIeFRr-eml59AEg2eUAWB0lUS8eUjogrL-rZOppTDoVyNBKYl-x_IiYJZXP6fDv0oZBoSFAZTpcmThpsrJVSMo8h-9Tgxp5gHJ2qqk8iXnzSoCA76swDwkRkPcQDxuAFOPHR4k4CO8P-3KMh5G3lqVSqo5na03uLUQL7f0ESyhBJ1O8bmkaTovZv6Xx3ctR1pIKHGQF-9BKySbto1RFtN58rTDWwpmDpY21ZAra80-YU8hlg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/890fd0d430.mp4?token=gpVf3xiDiOsoGgtyKtc0ZftMIU9mYHM9rBZPz_GWikcsaJtJkiBzFYkEBVercBLTqieNMJB7CbArvw204k2ghLh0Vlke1ET9GWZaoo3VRbIS3-qkDBZ6A6oG87joGtLTSkviVaMfSK18hibs9-Hu9UgK1F_ZLnOQRLs1YOejYva-b-fLtavCRFXHsWnFuc30h4Fh2RraTFVW7kHcS6FQv0-Ljq-PUlqMaVKA7OyFjkUoJdavJ2WuhWZCa9iytHiHc_yR3smeYXS_vXK5UpUGa8AB3PzfQ17EKSnaXUja7El9oxqBZdsLY-ovUUfejIMBDip63Ft3oyBte1cwPXQCDaL9mywGSjFYJSxZy_04le3wQfFaxmXJfubAOVeminY1tMqw8GtIh5plP9IgSv1KOdVHhjq6bs8MhS_ZJHycqAOJ7KvR0mYGe40jVtdOIeFRr-eml59AEg2eUAWB0lUS8eUjogrL-rZOppTDoVyNBKYl-x_IiYJZXP6fDv0oZBoSFAZTpcmThpsrJVSMo8h-9Tgxp5gHJ2qqk8iXnzSoCA76swDwkRkPcQDxuAFOPHR4k4CO8P-3KMh5G3lqVSqo5na03uLUQL7f0ESyhBJ1O8bmkaTovZv6Xx3ctR1pIKHGQF-9BKySbto1RFtN58rTDWwpmDpY21ZAra80-YU8hlg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇳🇱
گل‌اول فاینورد به بارسا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 7.32K · <a href="https://t.me/Futball180TV/106039" target="_blank">📅 21:36 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106038">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">گلگلگلگلگگلگلل اول فاینوردددددددد</div>
<div class="tg-footer">👁️ 7.31K · <a href="https://t.me/Futball180TV/106038" target="_blank">📅 21:35 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106037">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/d0ecaa5ad9.mp4?token=VagbBsNU4hTaWyebwcn6-Uf-xPtsNj-SjLlo6GaSJpD2gF-zysgYoQ-PirhPDolrJQuiKpxBtPlgiMGilUlyaWEhgTPJJXXEAQvIU3ju3tp2KC037j_GfDA_j_V5dbUtffe8Ce6xOQ6CAoupxPpOKo4GpehwS5USwxmqIRdibVSxCFWu-_lg6Us4Febetbx_vz68cgjQQjsw9hFp3DAAiNj9fy8ua4NFQT70l8xCT5fBjfRjD3mYqa3H0rphGJv9bgszuglLuj8AgVoVQc2cgRcPfInXfmYSvNsdwaWoCLlfju0_LM9BErWuwV6-ptqlzEGbGCTxKv2BdsP0OjR51A" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/d0ecaa5ad9.mp4?token=VagbBsNU4hTaWyebwcn6-Uf-xPtsNj-SjLlo6GaSJpD2gF-zysgYoQ-PirhPDolrJQuiKpxBtPlgiMGilUlyaWEhgTPJJXXEAQvIU3ju3tp2KC037j_GfDA_j_V5dbUtffe8Ce6xOQ6CAoupxPpOKo4GpehwS5USwxmqIRdibVSxCFWu-_lg6Us4Febetbx_vz68cgjQQjsw9hFp3DAAiNj9fy8ua4NFQT70l8xCT5fBjfRjD3mYqa3H0rphGJv9bgszuglLuj8AgVoVQc2cgRcPfInXfmYSvNsdwaWoCLlfju0_LM9BErWuwV6-ptqlzEGbGCTxKv2BdsP0OjR51A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
🔥
گل‌سوم بارسا روی پاس محشر پدری
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 7.32K · <a href="https://t.me/Futball180TV/106037" target="_blank">📅 21:35 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106036">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">پدری چه سوپر پاس گلی دادددددد
🔥
🔥
🔥
🔥</div>
<div class="tg-footer">👁️ 7.32K · <a href="https://t.me/Futball180TV/106036" target="_blank">📅 21:33 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106035">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">رافینیاااااااا دبل کردددددددد</div>
<div class="tg-footer">👁️ 7.31K · <a href="https://t.me/Futball180TV/106035" target="_blank">📅 21:33 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106034">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">گلگلگگلگلگلگلگلگگلگلگلگل</div>
<div class="tg-footer">👁️ 7.01K · <a href="https://t.me/Futball180TV/106034" target="_blank">📅 21:33 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106033">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QUqaXpTfshmg8f79G17NFjC7fto6evSQjc1PRf-J8GA84pToIU_fkjPqxxPrwF7kZp3tKc3mXztib9CoNKEiya6li5pU6iuBQ6gs1nkswIDlFvbJ_UhxG9K1WGg9ERuhzIDmnp77nlA_PZHEhfKACUIRfNP8U2ZEtaBsyCWQAdEBE2YgaaZPi9AOowJS7wcAcr8S95A0spOIN84svtLOh9MGz8kSfXnDTk1w-mCMgznQXAKCcp17VWftV8Y-afC6hJPzthj1EFYZ42MxQ3fI6GYyN8sNW-lCGP06i9VUHpRbmOcDaEciCBZgcewsCwqg8Srh49aWMRnMHk07bVMOmQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
⚡️
🔴
از آیفون 18 رونمایی شد.
چهار رنگ آبی، آلبالویی، مشکی و نقره‌ای.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 8.23K · <a href="https://t.me/Futball180TV/106033" target="_blank">📅 21:23 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106032">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MhChPXF3bs1KBBhD93tYEGyEZKfLEvoC4CkUaQJGPEY-iw1xnfO1VFev0hiKIwJJ9HcsKTe3AmnUQstjTsM5M_2G0TWsVDfvbKEY4ecyg54P0snWn2O9rCDgcGFRkvxk5g2G4JW-DU1W84DPagvmy8IREDj1Ryin3iuGSiwL1glku1_Q1Xkrx_0vuZRyOdB8cZU-mguu5kyARTAPLTCPrYFfvnW3rm8Eg4bopmqsE3XVbIe8OkH5KtOZC_SM4FCa2q8N4q4epu5AxypzJGVWcuxsgQi_wpPSuJZcVn9Zy2ZbgjKTTeoyo3Hz9OghpmV03yuo-3hIJmUC4uEtvjznyg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
🇪🇸
ترکیب لیورپول و اتلتیکومادرید
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 7.93K · <a href="https://t.me/Futball180TV/106032" target="_blank">📅 21:19 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106031">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dO_FEGu_gOfDEJDFm6u0MHIF9tvFn6ZunfS7vxQfgg4NQ1khh8S_OQ6sPfVbwae338KDqZPgHHS4SLiHcVkdRi3FHkTGE40ZSkOQZ2Lcwt-pF6BolitQ3uNZdsIMqKSiSgdEtbTtHDVz7fz4Q7gI5GAaTd1j2AQotYHQ1HPL-NBd0SSxhq14oiFBdSDXfnZBs7G7eWfaOxHN6fy-BUPjED4Fe9EgWaXeZR4Sf9EOXU2rxJmjSmg9b1EuMkdi4b0N8lGjbii-GOkvrRieqZ_7wnwPHf982BFkrTgfNhJPBBJoO9JNHc2ZZQtWjw6tCg09r9FpBXSDm_vnJ_2AYELabw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
🇮🇹
ترکیب تیم‌های ناپولی و آرسنال
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 7.32K · <a href="https://t.me/Futball180TV/106031" target="_blank">📅 21:19 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106030">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/O0aFcENMJHx6Qyojh2K5NGQfNUpq3F2QKV_3WavnI9pReHOsMvyYDEnivzmwmU5yxMXNESG3M8ko0CWfp5d9XHOeI6Tk5TabhFfXHFzAQxa5IaW3SKVpxRUZDvqm8o8cW9yP7eR92yh7cEV-VXk9kLYQF_KitlmN2XlDNS5tAs3aD_W4NPzGa3gBbXUuX_3kya_FD6UDi8Qeh3yZijuO2ZrvtiADKDJ4HcoA5s3eThm_TVvngQ-UvK6FONlL5IEF-Hf0CYZsQ_3OyRtOkvif8ZYtHyy1GvVAFPw5YMUzmSgNqOmvmHMq4p1Q3nF0oYyZf0oZdN9AffpSLfJocRWfMw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🇮🇷
🇮🇷
پوستر باشگاه پیکان برای بازی با استقلال
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 8.54K · <a href="https://t.me/Futball180TV/106030" target="_blank">📅 21:06 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106029">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/c8eea35c2d.mp4?token=UWVGbsyfibnPod5FZxCrHy_CSiusqMfaEs8jBfHB1reE1t6loR-b0ezs80eAraXxlsOjdsOGbXW_2vZCJGgUyCUSd7qDo7MC4T69asb4snzpoWignXrE4yvJJwiL3mviOkqv-GK5Htxylf7GYVTG7zrlz6Kp4QNk7qxsAF80iZrNOo8J8Y9ss7KYXoUXX52w6l1aOkAoH2qsTTnnh3cDWQsX1NTHAEp8OwWgQzaDI1sIKSJERtUCXcxDIxZPV2oIDejkrEYDQWqtBuOMD4CYt76OBCZ13_fq0Bl1547Ogqmr8MOXBSWaDwnO3K2ysjyFNw1BsThwVHHDMGCeBzcnGopWCeUvaWrqSeK-JxIf5rCijk_HlVu5PQ8TabLiH9dd6QvY8ybVOAEAg-iFAbYDsGhzRO-5fscuiygFXN4-nnWn2wImbAsIYIF1TXiX2IOIf05Eko3oXNzWcKwXFYLWVXQmvucOhq85nk6I7tX6idBimxURXOo3zZS5y-5QO-oUTgF0XQM9FgfplE0qXCkTgpdiIoRwKwrUGj9HvqeqmQSqZhFsNIJGs3f6D9fI4o2cWlH7OgrlQJwgW1GCqpUy0P2HpLJdFrIsqZgNJj3I5hi3F0xiT1bWmJIHo30qTXvUPhgitomUOycECZJD-Yh1h-WTLq2SmTGvF-oVmlIzcJ0" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/c8eea35c2d.mp4?token=UWVGbsyfibnPod5FZxCrHy_CSiusqMfaEs8jBfHB1reE1t6loR-b0ezs80eAraXxlsOjdsOGbXW_2vZCJGgUyCUSd7qDo7MC4T69asb4snzpoWignXrE4yvJJwiL3mviOkqv-GK5Htxylf7GYVTG7zrlz6Kp4QNk7qxsAF80iZrNOo8J8Y9ss7KYXoUXX52w6l1aOkAoH2qsTTnnh3cDWQsX1NTHAEp8OwWgQzaDI1sIKSJERtUCXcxDIxZPV2oIDejkrEYDQWqtBuOMD4CYt76OBCZ13_fq0Bl1547Ogqmr8MOXBSWaDwnO3K2ysjyFNw1BsThwVHHDMGCeBzcnGopWCeUvaWrqSeK-JxIf5rCijk_HlVu5PQ8TabLiH9dd6QvY8ybVOAEAg-iFAbYDsGhzRO-5fscuiygFXN4-nnWn2wImbAsIYIF1TXiX2IOIf05Eko3oXNzWcKwXFYLWVXQmvucOhq85nk6I7tX6idBimxURXOo3zZS5y-5QO-oUTgF0XQM9FgfplE0qXCkTgpdiIoRwKwrUGj9HvqeqmQSqZhFsNIJGs3f6D9fI4o2cWlH7OgrlQJwgW1GCqpUy0P2HpLJdFrIsqZgNJj3I5hi3F0xiT1bWmJIHo30qTXvUPhgitomUOycECZJD-Yh1h-WTLq2SmTGvF-oVmlIzcJ0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
🇪🇸
سوپرررررررگل کریم‌آدیمی مقابل فاینورد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.97K · <a href="https://t.me/Futball180TV/106029" target="_blank">📅 20:44 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106028">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IlNTgCyxX3gAaAiSevtQhBGlkAQ-x1fPLxQfD0HXhAAAl8IVZf0YEtQrCfqAVe2zJ_0Sv39N_7J97VcrcPWWA-7q-dt8Ikpxd1CpEsb1E98WRaEqclVxJJe6DKMad2r8FmoZvVFSYpvznphxlO5U4fIMRtzEoOGQz-ndNoa37lbgNFr4VZR_g9EPdLDM_vgQwUsewTSz_tfWPG94_vtPa11svKGBvS2SGAN4NdFruKKVkSTKN8an6_1Zz93DY4hIgpGEefKYwDOojCmpivTHqLH94oRDXftuSwKWN1X9K3cBgVxIRtjAqqrbTHlIsNkLk3XFlkhoovW9YKU8ielkIw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شادی بعد گل کریم آدیمی
😐
🔥
😐
🔥
😐
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/Futball180TV/106028" target="_blank">📅 20:41 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106027">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">سوپرگلگلگلگلگلگلگگلگل کریمممممم آدیمی
😐
😐
😐
😐
🔥
🔥
🔥
🔥
🔥
🔥</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/Futball180TV/106027" target="_blank">📅 20:39 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106026">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">گلگلگلگگلگلگغگلگغگلگلگ</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/Futball180TV/106026" target="_blank">📅 20:39 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106025">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Y6q0WlEMQdiDIbX6prcp3amUD_okc6dw3WaS5btUMfopM39NZRg7Z4B2wE5g1n8q_tDCyrdu9X8NH-Ke6f8PDrxRIzbboCWkS_FRLoWF7fbaQkaPPCmA9_aw2vOxfshDp8RK4Ot2MxAPIyBLyx0rylHKgjonWzSZem7jISgCaIA6MRVBQyB_HmdkRNkf7HddtXbRL70vgoPA_FEuiYM5XcUf8OUD7VncntpIWbEoBVIE0nknF41FMCXNTQ6lj-l49b1gio_IXavriN5w9EbqIXeSTJ47icJM1XEEd3tx0GJY9XY-volsTR4GAQvmH_GBV61Ufs2GqVlEfbQpwoay8w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">گلووووووو ببینیددددددد ناموسا
😐
😐
🔥
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/Futball180TV/106025" target="_blank">📅 20:30 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106024">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0f1f0f0fa3.mp4?token=WKkpTE7quXaySH5_v9e0KkMqV7--RuQA_iQ1jKSeKboz5CLshMyjc3EyPazR5gdlsUYX6Do-ow2Hk9jBGJbaua1eK4fLNwMlo6UKSSNrD03Gs7q0-1Btvw_7X5MwP46oIVpuHxUTTGYfH16b7bbgP8LQ0-RUI9iSodOJHIr_g8ZtUxMFAiBtx3u8BRILlzeHJZTYZQHLcafZsiSqSsaCLd7ahM6I_i8pT5rM4CriJlzQE7NNwLngMYuh0EI5lkfyiw6nCpN5-8gfuHfCSzOG8Sp2YX3T7kV8icXiGLFsaIBtN1-O7IFPAirwMigx4np1N7LgKRrwwwlqW8FjofRI6g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0f1f0f0fa3.mp4?token=WKkpTE7quXaySH5_v9e0KkMqV7--RuQA_iQ1jKSeKboz5CLshMyjc3EyPazR5gdlsUYX6Do-ow2Hk9jBGJbaua1eK4fLNwMlo6UKSSNrD03Gs7q0-1Btvw_7X5MwP46oIVpuHxUTTGYfH16b7bbgP8LQ0-RUI9iSodOJHIr_g8ZtUxMFAiBtx3u8BRILlzeHJZTYZQHLcafZsiSqSsaCLd7ahM6I_i8pT5rM4CriJlzQE7NNwLngMYuh0EI5lkfyiw6nCpN5-8gfuHfCSzOG8Sp2YX3T7kV8icXiGLFsaIBtN1-O7IFPAirwMigx4np1N7LgKRrwwwlqW8FjofRI6g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گلووووووو ببینیددددددد ناموسا
😐
😐
🔥
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/Futball180TV/106024" target="_blank">📅 20:24 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106023">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CGQAL6QTR2ApEX0ka5gLxO2cASoG8a8lubLXgbLY1jmmagxzGm8Yt-eBp5eApJfO2qQz0dYeCCv5AG8-9V5wEhMjiHCqpKQQu5j_WplXZh2Q425clCv_o0pWG-zfbH3q7-iRW2ZRFmX7rIpwf-C0UbidaydCJUPNnnXv6BrFcI-9dlXl8WZy24PPQL4FkU_aKl8ZSO0Gz2qNQG7rcpXT_HfunNMVm5RmrRpB-m9i1qcon0VCL_rzNbHy9iumMEuZOf6FcsJ-kME4GG3CRtIyFS88QGsQXFBWnkW5fvJUShu0wHvUGQqoftpnZyQnKQ8rO6J1tN3E7JxaxBCuyHtCwg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بلایی که سر مدافعان فاینورد آورد
😐
😐
😐
😐
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/Futball180TV/106023" target="_blank">📅 20:22 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106022">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">اینا چرا این فصل اینقدر وحشین رحمی به هیچ تیمی ندارن
😐
😐
😐
😐
😐</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/Futball180TV/106022" target="_blank">📅 20:21 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106021">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">عجب سوپرگلیییییی زدددددددددد</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/Futball180TV/106021" target="_blank">📅 20:20 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106020">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">رافینیااااااااااا</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/Futball180TV/106020" target="_blank">📅 20:20 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106019">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">بارسلونا زددددددددذ</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/Futball180TV/106019" target="_blank">📅 20:20 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106018">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">گلگلگلگلگگلگلگلگلگلگلگلگل</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/Futball180TV/106018" target="_blank">📅 20:20 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106017">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3aeda36fbc.mp4?token=X3WKJMpXM9kxBY4naYCu9770cMuvERF_T0WeiSu_BN7O__h1sPUdDUciNEon3T1aoQY9a27nRz3l4G63EYYm0GfuS_G56UqlRbqBIVQssrRVflzdvbDjDwRAB61B9rJM174Y0OAFuMuXPmWXrqauMlumv-45Jrvil5Uvvm_LAPA6V3Mq4y3yvCTCIeo9TaCc1qYVB24iG-YrwR33XWsHnm1GRYoagJNKljRWBNdpx6t1gSvWF7kuGE08tl0yqPzkurop6ED7m37ESGlMFeptXpmqEdZRg8-8ET6O-6oZjxFWUYOEc_t-O9ZocXMhQjwryhD3Ek8AbtnYWlY960sXcw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3aeda36fbc.mp4?token=X3WKJMpXM9kxBY4naYCu9770cMuvERF_T0WeiSu_BN7O__h1sPUdDUciNEon3T1aoQY9a27nRz3l4G63EYYm0GfuS_G56UqlRbqBIVQssrRVflzdvbDjDwRAB61B9rJM174Y0OAFuMuXPmWXrqauMlumv-45Jrvil5Uvvm_LAPA6V3Mq4y3yvCTCIeo9TaCc1qYVB24iG-YrwR33XWsHnm1GRYoagJNKljRWBNdpx6t1gSvWF7kuGE08tl0yqPzkurop6ED7m37ESGlMFeptXpmqEdZRg8-8ET6O-6oZjxFWUYOEc_t-O9ZocXMhQjwryhD3Ek8AbtnYWlY960sXcw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇮🇷
باشگاه سپاهان از طرح جذاب توسعه استادیوم نقش‌جهان اصفهان رونمایی کرد!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/Futball180TV/106017" target="_blank">📅 20:19 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106016">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/G8t7eq05kP9pcKbvRwI2Sis2L1ruGLr9KvR1PsrvKpi4XPIAqDjpUM23xrhZMB7OXC9gEQvY_U8iJR6sm94LXDgV230ecmSspnsgbKs_Fqp_g0x67Ky77InLltiz4GfSF520bwgJZdZH3vlr-sjz8_oLjah4Kvh7-tKeaPeWQyAyBOwSLKmwL7IzT7WteIENquTbp9Kkbdcp4S1pPNmnnLWhOVciuNMmT7ByNFwd4ju50SplrcOuLe6rqxeC5LmXPdTrM1ynidZbR_X_qQXuLLaCkkBDHVGichCldGV4GQDMyRLu036HOrWa6RIrzgu6HsRvZFi3fhjdbh3s88xg8A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🇮🇷
📱
استوری صالح‌حردانی بازیکن مغضوب استقلال برای دیدار فردای تیمش مقابل پیکان
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/Futball180TV/106016" target="_blank">📅 20:13 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106015">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Z2ncqpIj5iHHoChOwGMmlKC4zd_zVinbz_vub5RaQVI8vr5y03U-QXqcYSE8ybJgSiQMfIfv6oiVs5AxL-40PvRcBXrsP-_UdHEid4u4gVtPZSmVds1jxXAsCOuKjmyz7OxnuukcXwsg6QS6Vz1TPIAedY_Fn2KpN_sE4pGPIOfCdnACKeCBMcn-ioDEdD3xYtCSAzELvp5fWqQJrIle2hlsx7ENYK2KRF-iW7HyxAcqhqKHOQJsU4Dzj51Sh3YtIwZUxpecUsTThoSSHxfsWRkeznSepeJjSVFmD8-jaqoNKA2058r0sU4LES-Rc5I9I456ZS08sm12sM06mAE1TA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🇮🇷
📱
استوری صالح‌حردانی بازیکن مغضوب استقلال برای دیدار فردای تیمش مقابل پیکان
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/Futball180TV/106015" target="_blank">📅 20:09 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106010">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/NGbpQGelmlXkEbKwiKwJM4IWpRM1AXsR1g5pTZSUlCm2t0OnZ0tHJ0NaVJd575KvO-edxXgzP-IPokZBJpJI_hTQIHy4Bj8lGMrCU9_qQ2BIKZkmLTtJrEHWJ5q51hY2PAJX6PSiWydfdvUjbTW5uZkN3Rv0sEIeAM8-izsDR1aavuR3eqdPc5QbzmVjixCDlgsBG9tX_AeGqXLiSySkg4G6gB1JmmxYAherlWJty7CtVaXHhCLvYralkI7nyqYbeWnG49TKAUNqHnr9owbG7pWiQ5UkUrmdXr1_dJe4opwUc5MUaoSrZtW6fr6uLW0NQ960Tjpt_MhJPHEUmo2Bpg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/i5Jnvj3Z01c6-WJZ9pwc5eCQUhMgq8iCUuDEJ49R-ELe0Wz8r6BLi7NbZpjv4k1m5OJ2H8XYJhu52AxKrTeTOsuWcQJuTBBVmUnXeKaW_Ngt5p1bT2ZysicxsEwxnPrrWX7C0XK_B-xbPRE-NUOKqKT_aNt2HLqCVsRLrOQMuEcMn5OXToDTJ_276_f0w2jRQ-1jbgdzpKLYFJjzq4AeK3FoH_zQ2yKoUKp4NcFPwYIkG4oM4BUbMJaagiHtS27xlydXm2iedW2-Rb-uPoLM7Dj7iUroIcXdSHHWGRq0-nGdcd6WnWr2JVqaP8NzhopAe6Eqlc_J29J0s4co6uweQA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Ayr1XtwyJKDkI3eNPpaXduekoP4bSawyeTiol0UW3US1aMdP4RvjKczpSiR90lgaPyaq9ZPuTrtJiKUuQHHknUa1VbKTfhPs-2AzJgftBIlv109HAgGX9Z4NX65Vyy71icsJ4gvd2RLG7uIY1YRTnc8-Oqz4fY0jry5V67CWHl_l6jGRfh3cCqzFSAtaGTtutIkU7aJscRRRCpSMemM4XU1B4kn86ElY1fvnygcnLNrKXIsWxTWQpWSZ6yrCwlMqCVR__MEeJ_ihYlIUhXs6PZkwLVxVEPjByTC10LdSqaZuuquQv5R9a3-mmeVvv_x34o5uZNa4dqEK-hlOjwrFOw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qlbxQanS375JUps3dB3cZZncUddwDI5soB01YhKUyCEleSsNcqXnOrY24W-xFSALbkfMfqXLEc9oMTSw7iwIZ9fua6ivER7Kd4IQ_b9tbdp_jGNHd6Y9CnKVWZS6aQHVKDZvvTpYtxQeZOZMOnbXdHRiJ-8gxXLEzhsKiDrxtnIP1dyq62Rzoz6a3WnEOrwFidpZseKoeKRP17cd_BsOq-aljkEmGOnKEG5hCrqEoyo-9F5CMFRyHQSGWeIoY6UzkqF05q9jmwwINmaORro4Nvrp8FKzW4HxgyaUn13XvyEh24qdh5peppebrN2hSKCKKxQg1Rv2r81kPgLKCUlInQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/fXj_Z9D9KgFTUULad6ONeBwpi8ev4BdJG8LwA1XAlMWZruFCp38s1uIoJnUzYRnA2zYaju06w8I8B04_gaBo2eB78tRI7m_oqSeCItW4_EV0ZxqUED3SQ5uU_YjZ6gKMNL5jAmoDXSP88_Z21zZQcNFcyQve-n03AlosqwHi0EARnLtjYURM8eLtWWkI7UghKbut0KYYPL2J4gXzR1opCKbnEhV_uGdOSsnCN9GeV8IN5ceChU_Vnl-vyEruc9JYU7u5bpQR-5g_emz37Gb_7j9r0KlVApp8QDM83ctGOPhGrq-MYCGcNSvnoUozaSh4SA0dlnW-Z-mun3Evuq1mqg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">✅
👀
خانم موراتی از مجریان جذاب UCL
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/Futball180TV/106010" target="_blank">📅 20:02 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106009">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/H0NHZ3lQKEMLjtCSW7y_c1j-Jt_1EHpWJ_R-Qag_mq_4M37p_bTAmEBuRr2vIBRPiiPrh8jdXOXogLkyPvyyefFJQn5R3_iX4lptjQTUMKvAlNJ1JmTeSfmX3-NEH4jdKAoIai8ReDSJ-LZgfcbG402KWn9keDxEx1I9pyHOBSRPlVlDUK-4WSWBHIhyjjqRu9xJbxIIjo7JKXNFo58lYJtkGY-6HpzItH9qNsK4doYs5vBeUqk5GibeukR-L5CzB6N6DwemBMAUjnbTnMxU2gFMOoi7YRfp6wXMEam1cvq6lOLtXmWyi0bhiLGmJctwH7PBpDnqOWYcQNWCHXT46w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
❌
⚪️
سردار آزمون به لیست تیم‌ملی فوتبال ایران برای فیفادی پیش‌رو دعوت شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/Futball180TV/106009" target="_blank">📅 19:29 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106008">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QLbA0HqfXfqcZkCEXxtAWj2S2oR7Ngr8MkqVZadoJk1kuPgDkVk8X8OJNqBBNq7539ha3m6cR0Jhoa-kTEeyOIBNgMEq7eyTJokofWdBS6jZRBYxT4W8iYrdYbhgiW9VWTlP3dYDWes0UtCJd77t-7c9Ye3XjIIBkymWiMEyF_W4GHsyYn9LodoHqM3RPlQF7rKFlqtUP1jIEqj2thkTgiR0ww7XRocnoRNnlnjOVMj7e7KZjfj8uoOfsT-tBhg85XwaFcSQpYaAoNxHYJMkHx1oO9Y_uyDz-mAij1e8gUuwPUjNMUQk-ntQfT0mlmkEHdW-OTO6P2cpijWKyCCW3Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
🇪🇺
⚽️
آمار بارسلونا مقابل باشگاه‌های هلندی:
🏟️
۲۰ بازی؛ ۱۱ پیروزی؛ ۷ تساوی؛ ۲ شکست
⚽️
۴۵ گل زده؛ ۲۱ گل خورده؛ ۷ کلین‌شیت
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/Futball180TV/106008" target="_blank">📅 19:17 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106007">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QTYORrjf--ovBTkviajeU8yeYdQUUnVCtH5swh2Um6IQFXCkPoGkLf65Irg2fEVliI8y8W9H7ojN2Qwiw25kcOanGDVenKUILerHX7wWuSwu6DMJQrq37oNuHO0x30djSuIHlVvGL0XAt9II-pR35xrOM9VVz07NBEUJ3TkqC_fIzS_pi8BegaBb5cbuy8Bd8Pn4Qhe4NrKSYdb8pehvOGcPkHsjUzJyOqPGcGvBaKUIAs6KlHwhaARcQwu_LGYSDbLHz9z_0-5tRViu3zYtNajcbWpQ_bki-V5KvD9hBr0Aq9EiwKPWeqdJ0wdOpYDmkD5SBfN5unzloCdWNGT6Kw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏆
🇪🇸
ترکیب بارسلونا مقابل فاینورد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/Futball180TV/106007" target="_blank">📅 19:09 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106006">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/V3Yn8xMc2p7ToIvdZJkPtmsM1atDObDe52gMZUHtQpVgXIlhpPSNoJpDFDWCbbIqc4O6jfaBj0ulsL9EmulPPl0RZhqD4C9102JYueZXNY_nCDfb3D0wVIinRDd1vODmsRClZVboDpnIrQDPHsUSiEPJRVFsWCX8hi_A-CkzLFPIzDvQBlSx4QW7JZL1yzL-Lrqso0oYQo81pTZpCEv65M8vzFus5cZ9Ej_si02shLizxzbeP9LvDSECFfztwE-F27I2oUQk6dP5oEjBMkZAP5-gZxwwgnJvVJCrZxI2xzbPjGMNpiUbK6rIOnzHWT0S9AnjEfj9zu-mXsi51pryZg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏆
🇪🇸
ترکیب بارسلونا مقابل فاینورد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/Futball180TV/106006" target="_blank">📅 19:00 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106005">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f2045d20cc.mp4?token=QUz2amp6NkQF7Id-S2vFenUps46aLZeU8m9C9qXUkuuLW4c_6SkJ98PBUdDJkZevAJ8x4mxM-cXoXOuBTe3WVzbmIuG9CeNmtXrpF0bVg73H93qLgLyuozp1C27tuIY-SzIUiM1TInFABVsYbl67DmI2TjyamBLS8gPLd_fxplwWeQV9kxfX5jq5vP72GvgfPOiC6u5SahwxaSwQU-G6hBdStMq_NMHVQFwPXQ2eC4GxTq-0QE2V5FFN_IvVoFU3b_YsKGTIG6DC9f2t4wqc5Yw9GzaRTX-PWqo5CxC6jliHKzN6yvqWOWzZfZFXehNVMstU_W8x8fQeCkQI8RPqJw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f2045d20cc.mp4?token=QUz2amp6NkQF7Id-S2vFenUps46aLZeU8m9C9qXUkuuLW4c_6SkJ98PBUdDJkZevAJ8x4mxM-cXoXOuBTe3WVzbmIuG9CeNmtXrpF0bVg73H93qLgLyuozp1C27tuIY-SzIUiM1TInFABVsYbl67DmI2TjyamBLS8gPLd_fxplwWeQV9kxfX5jq5vP72GvgfPOiC6u5SahwxaSwQU-G6hBdStMq_NMHVQFwPXQ2eC4GxTq-0QE2V5FFN_IvVoFU3b_YsKGTIG6DC9f2t4wqc5Yw9GzaRTX-PWqo5CxC6jliHKzN6yvqWOWzZfZFXehNVMstU_W8x8fQeCkQI8RPqJw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇺
🇪🇸
🏴󠁧󠁢󠁥󠁮󠁧󠁿
تیزر جذاب از بازی امشب اتلتیکومادرید و لیورپول در لیگ‌قهرمانان اروپا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/Futball180TV/106005" target="_blank">📅 18:35 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106004">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pCPF6Xny5AqqHffPzDPUT56u8TCCYyGYt63TUPkM6Bg5oLyuhi4-6kBM7K_MXz2aR_tKHgK0VcMpQgPtMIIdo4A8rJABiISYCIzT3d1hPmxzvHIkaERFaCdIJ63_mqWlyr2PMwh3xscNIdPctPvs81rFkwvRvP29XUqYkDC4X7vWfZSJmPhnoBLWZf6HsQxnYRRRC2sbp-rark8i7Fh0moqJh0vQXorfsTMD_4tO22nKaz6ua2iW4gvWXMvwOdwWzo7MlZOQX_BEkzEhGfSeA27xUCD5XamddmMXjPSFEW4TVjjzZJZEeJ_YQEnqvb0UwQA36G2ISdiW13kRR1GywA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
😳
😳
مدل موی جدید مارکوس رشفورد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/Futball180TV/106004" target="_blank">📅 18:22 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106003">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c95f05bffb.mp4?token=SWXhphi4X4q005x0JMNfEUR9TU8quNXLylV2xmjKJqzQaU3qijdcfSzI9EEPZaFjWs5ZYBB8Q5bxNGT-tcjcp3aLPDDw12kUD432u-0_J4B79PV5-8cQQxvzKH7VQRyk2o63ZCFRn4YyAswxh5wC6090r7nut5w_tsoyoxqq2sY41NRrXwfeufLFJ4VKlv-Q9ni_DIwX2wTgOEBL3W7thQL5zJXtOvnwq8GrKv8lnIDAW5QaJSa_Sr4r07RS_eThYeLNmAWjcV3kIOe69DiTGYC74d2xPwsmsuuHGYS-tpRwsGG7ppIOKNxEiVNmkQiqGUM-PH54hrsVZ8EhcREfHg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c95f05bffb.mp4?token=SWXhphi4X4q005x0JMNfEUR9TU8quNXLylV2xmjKJqzQaU3qijdcfSzI9EEPZaFjWs5ZYBB8Q5bxNGT-tcjcp3aLPDDw12kUD432u-0_J4B79PV5-8cQQxvzKH7VQRyk2o63ZCFRn4YyAswxh5wC6090r7nut5w_tsoyoxqq2sY41NRrXwfeufLFJ4VKlv-Q9ni_DIwX2wTgOEBL3W7thQL5zJXtOvnwq8GrKv8lnIDAW5QaJSa_Sr4r07RS_eThYeLNmAWjcV3kIOe69DiTGYC74d2xPwsmsuuHGYS-tpRwsGG7ppIOKNxEiVNmkQiqGUM-PH54hrsVZ8EhcREfHg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏸
✅
سه‌قاب و سال‌ها خاطره‌سازی برای مردم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/Futball180TV/106003" target="_blank">📅 18:10 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106002">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gsJVw0mcfe6eKNmfKmyLuikzU0dySK5BmPPlbOEmxZwDO7XCKgoWlfUa_5HIertvyiIoE1bpgFw_Q6rPeMVmwNR6MpF_dHusNUnJtrhz-T4vA0MZXMFO4o1u_KjbleN-tH3Zp6qtLxOnPh5I43NyNnuDXkg81RHR4rINYDS5zxvis1E2W4JC3msB5R-hrxhTc48JSOQd9epsSvPcdFRCZh8wHEiqE3jjJE4yTSnDa59oB4zon0d6iD-sKHrq8eSNdOTOvZA4DUXN2NSXAuyAfkevOnUVsUoSigvpyEU2FxLeP5QC3nOguvFiRR4AnLqx9pZGwDlLarhq8IxzvBRDIA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👀
❗️
تصویر جدید از استایل فاطمه‌پسندیده و عاطفه رمضانی دو بازیکن سابق تیم‌ملی بانوان ایران پس از پناهنده‌شدن به استرالیا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/Futball180TV/106002" target="_blank">📅 17:45 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106001">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/C8mC5S0hlrX1vC_aUptiIO4F--_Q-WPA2xiHKcIeyzWIgcyW-AnbLAQ08RzeuGlXtJ-tuRmvod23kgkfSHvGUxuZ19BsMEDmo9WKakvevVNcBKwdzQTzWjmN6ytqBJQcGEzVpmKvkdbwAYhcf5fuo9YKv4uWhFTNlnmmtXkF5d1owBFfMuVzlUMdt0bnkF4D9J6DN_EV9sUS97CvP4-mtJ1_NJ1Lx82T6M7ZNyVo1zs5VFjXDWv0OV4hjn_pp_2RaIJ9vxSPcITKgM3A78aPOMLRVng_rj_ybbuWHA9TtYruY_HzJNRRjyok7OkKKkHl4IdRHM3v1-gXmVYdDkWz5g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇺
🇪🇸
برنامه مسابقات امروز لیگ‌قهرمانان اروپا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/Futball180TV/106001" target="_blank">📅 17:29 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106000">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/Futball180TV/106000" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/Futball180TV/106000" target="_blank">📅 17:29 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105999">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/i-SzeAXM8frUtHsvky9PqfTIgWXxsc5N6GN6z2FUr9VLY00NwfGkYN_Uw7moRNuLfzIpuXxFVMYGpo-rBH-1cVeCOP7bUB6TQsr8IvYDKCMVmbdDNxclEK4Z3Yt96sITyTT_bCg4NINLsi6Hkn4R8Q-hZZaVRRIXBpvzwcwVzDex69oMNGCxVBOj_cjssK5BGXcZvcGzJkW_jQx0rl4x23G3NNsFrBN_lyn6ZBR_r8xawoXZOK9IgfLH5LnbIc-tx6o6mNm9GgH3r-UmqP1Fqso6U5D_qqR_DN6wMqvF_XvYiHJ7ov7MnkQbctJaeEjXJElPHTnAPsD9qc45ad-z_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
آرسنال
🆚
ناپولی
⚽️
🎯
این نبرد حساس
چمپیونزلیگ
را در سایت بین‌المللی
TrexBet
پیش‌بینی کنید!
📊
نگاهی به آمار ۲ تیم در ۵ تقابل اخیر:
⚽️
آرسنال: ۵ بازی ۳ برد، ۱ تساوی، ۱ شکست و ۷ گل زده
⚽️
ناپولی: ۵ بازی ۱ برد، ۱ تساوی، ۳ شکست و ۴ گل زده
🦖
بونوس اولین واریز تا سقف ۱۰۰ یورو
🦖
بهترین ضرایب بین تمام سایت‌ها
🦖
واریز آسان و امن از طریق کارت به کارت
🦖
🦖
🦖
🦖
TREXBET — PLAY. PREDICT. WIN.
https://TrexBet.com
T.me/TrexBet_Ir</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/Futball180TV/105999" target="_blank">📅 17:29 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105998">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/30a6458393.mp4?token=Bec12cq3MVoBMHUNnjgx24g5c3ilxb_EQ2hxrwZjC3p6RnYUUcigpcMK7-Wy24A_MEmqVvHimuaEgZ_zqQfjbtVsDDqwV6OtBulExVRRk86vtbrBDXzUyJ2SIQjnLMpMdq7VBbL-sqOqtUm8hz1NrEZwMSempI6yF9goFYHAjDRuzjPjhYnPtj3Q7j3GVVApah9Fub-J8wYspQ6IEqHd0YjrY4NO03ZVFI2Z8hGrJfVWZrYuktfwNjrgcpPZ0ujFYJvYeeObCFsnuWvoyHRXvqoto_l4rGAxv8yCQ95l839yLQYMyTgmLFDgIAEzFh_DWcDvrXKz9Bs5g-sZJVVxNQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/30a6458393.mp4?token=Bec12cq3MVoBMHUNnjgx24g5c3ilxb_EQ2hxrwZjC3p6RnYUUcigpcMK7-Wy24A_MEmqVvHimuaEgZ_zqQfjbtVsDDqwV6OtBulExVRRk86vtbrBDXzUyJ2SIQjnLMpMdq7VBbL-sqOqtUm8hz1NrEZwMSempI6yF9goFYHAjDRuzjPjhYnPtj3Q7j3GVVApah9Fub-J8wYspQ6IEqHd0YjrY4NO03ZVFI2Z8hGrJfVWZrYuktfwNjrgcpPZ0ujFYJvYeeObCFsnuWvoyHRXvqoto_l4rGAxv8yCQ95l839yLQYMyTgmLFDgIAEzFh_DWcDvrXKz9Bs5g-sZJVVxNQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
👀
🇮🇷
🇮🇷
تیکه‌به سهراب بختیاری‌زاده به سبک‌ جالب مهدی تارتار سرمربی پرسپولیس
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/Futball180TV/105998" target="_blank">📅 17:20 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105997">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/04d5f7ca29.mp4?token=knbUBaGXZSOVFeAkLoOUQsvWRgz01_FeDlIujLG3XIRM3-g-pd49wftZMBJMEDWMClKIbJX3VS1UapuSUbnZjvmFkFJzwkUbVeiyUaoZFnJkfxVoWcli1O3ghZyGVP3X-VEB_5in5burGKAcqe596wzfeoHyxihiFd-LH5UIM_B09SqnEOSlClrbkaeNJa0FJYIlf0lT1ZmoDa5feT9NbcF4Q9i92O6UYPLOthEJReZznnuoEEK4SoZiAFCNbUMMFqshIYfRVDPiuhh91UYpClj_dA8x07MMXogm9Py3DMzKlue7bpKHou_XNuzJf1QXH0-0fBe7dPft-fd-UFERTQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/04d5f7ca29.mp4?token=knbUBaGXZSOVFeAkLoOUQsvWRgz01_FeDlIujLG3XIRM3-g-pd49wftZMBJMEDWMClKIbJX3VS1UapuSUbnZjvmFkFJzwkUbVeiyUaoZFnJkfxVoWcli1O3ghZyGVP3X-VEB_5in5burGKAcqe596wzfeoHyxihiFd-LH5UIM_B09SqnEOSlClrbkaeNJa0FJYIlf0lT1ZmoDa5feT9NbcF4Q9i92O6UYPLOthEJReZznnuoEEK4SoZiAFCNbUMMFqshIYfRVDPiuhh91UYpClj_dA8x07MMXogm9Py3DMzKlue7bpKHou_XNuzJf1QXH0-0fBe7dPft-fd-UFERTQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
✔️
یامال:
🔻
"فقط کافیه تیم‌هایی که این اواخر جام بردن رو ببینید؛ تو پاری سن ژرمن همه پرس می‌کنن، اینجا تو بارسا هم سعی می‌کنیم همه‌مون پرس کنیم. در نهایت تو فوتبال امروز اگه ندوی، هر کسی هم که باشی، همه تیم‌ها میبرنت."
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/Futball180TV/105997" target="_blank">📅 16:55 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105996">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/94734143dc.mp4?token=RfMHFCZge-H7R9e5NENJt75Nkd3bpUGYIxXP5nezvGPMOe19w95BlIziEHvMKJse0HxOLWkiCVmfF_PLwTEfT_SIEBby2S69fRf_uKzw2dkoaqsahUviuLQ9pGGHKZl9O1cwz73yVlzSryvqGqzGg7ZF-dq3A5Fp1SSBrNTosrdqlVAjNhZX5BEWIf50LLMFZvqJlpqDJL0k7fTx-_p6vA4W0JAqcDV6V31rJfU7kZ5jV3HFS8b1CRfGZmT_UB4QRpFgdNHT6DuyW8Yw47W197OZE2KyFQPzmRn02YyAvOLYKGb-cTcQUSkfHNNIlfCTkTbFAwN_8M5DJZDaCEW70A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/94734143dc.mp4?token=RfMHFCZge-H7R9e5NENJt75Nkd3bpUGYIxXP5nezvGPMOe19w95BlIziEHvMKJse0HxOLWkiCVmfF_PLwTEfT_SIEBby2S69fRf_uKzw2dkoaqsahUviuLQ9pGGHKZl9O1cwz73yVlzSryvqGqzGg7ZF-dq3A5Fp1SSBrNTosrdqlVAjNhZX5BEWIf50LLMFZvqJlpqDJL0k7fTx-_p6vA4W0JAqcDV6V31rJfU7kZ5jV3HFS8b1CRfGZmT_UB4QRpFgdNHT6DuyW8Yw47W197OZE2KyFQPzmRn02YyAvOLYKGb-cTcQUSkfHNNIlfCTkTbFAwN_8M5DJZDaCEW70A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👍
بانوان جذاب ایرانی در استادیوم‌های مملکت
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/Futball180TV/105996" target="_blank">📅 16:33 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105995">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/85a6a8f2ee.mp4?token=lzRF3QFqcErzGmDvOLUBVkg0zLKAyDBHK0CSJz1584SAHKDHxzt2cJj-5nGvwi9_aiPr0dBCpz2anzadmcsmlxtH5fFDhFziDwX5EzZHVCDYO3bgHNF3ixHcO8C6H9j--hRUhv7mnvvS7mltg9rkvQ_qbjfhsXU0w59kUxy68YZGWIkZinA4wbj1vhiWTdgskwb47LwJW8CUrsoUl65naka1SRj84ZtYNv-fhBEIgUKIj6cKXw2wWFQDHowwUDZVo_UrwRGzNz2QCryXz981_-iTCsbu9WfLZ7AR-f2HrK1LwObCew6xyLJfnnRJnlXU6z3G2Oy4o7K8NHzdn318cQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/85a6a8f2ee.mp4?token=lzRF3QFqcErzGmDvOLUBVkg0zLKAyDBHK0CSJz1584SAHKDHxzt2cJj-5nGvwi9_aiPr0dBCpz2anzadmcsmlxtH5fFDhFziDwX5EzZHVCDYO3bgHNF3ixHcO8C6H9j--hRUhv7mnvvS7mltg9rkvQ_qbjfhsXU0w59kUxy68YZGWIkZinA4wbj1vhiWTdgskwb47LwJW8CUrsoUl65naka1SRj84ZtYNv-fhBEIgUKIj6cKXw2wWFQDHowwUDZVo_UrwRGzNz2QCryXz981_-iTCsbu9WfLZ7AR-f2HrK1LwObCew6xyLJfnnRJnlXU6z3G2Oy4o7K8NHzdn318cQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
👀
🎙
🏆
لامین یامال: «لازم نیست کسی را قانع کنم که من شایسته توپ طلا هستم. هر کسی نظر خودش را دارد و من فقط به کاری که در زمین انجام داده‌ام افتخار می‌کنم.»
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/Futball180TV/105995" target="_blank">📅 16:05 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105994">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/13f3510400.mp4?token=V9KiznLSxXSgtQailzJ_9rV48n7EdfV5-J1kKIja4_WDFYPaj_aMG0PyWOnhzDM03vcLFfYsCC9skjniRRmzfmzem9X3FJBpiCMFpU96tCvq8idqAP8tKUUW3g708sqsxaJhXr36Ib8VM2-XDctVZvt91kM-_8TgLxvLOYGbfUrvxMWjmDRWn23Nstpe3DWzPHqftwK0i_fZJe_Z4tWSJHSHQFa1A1ugJefCD5mtfFEQYcqBJvllhTiJLr9eCVFZsSrgi_xtTXIdScUySxplyPhM282J7Mjno_WR5dEaWhVSId3w08e_SezpPVDToXVFjuvAceC9E8eR3ok9cRl0Sw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/13f3510400.mp4?token=V9KiznLSxXSgtQailzJ_9rV48n7EdfV5-J1kKIja4_WDFYPaj_aMG0PyWOnhzDM03vcLFfYsCC9skjniRRmzfmzem9X3FJBpiCMFpU96tCvq8idqAP8tKUUW3g708sqsxaJhXr36Ib8VM2-XDctVZvt91kM-_8TgLxvLOYGbfUrvxMWjmDRWn23Nstpe3DWzPHqftwK0i_fZJe_Z4tWSJHSHQFa1A1ugJefCD5mtfFEQYcqBJvllhTiJLr9eCVFZsSrgi_xtTXIdScUySxplyPhM282J7Mjno_WR5dEaWhVSId3w08e_SezpPVDToXVFjuvAceC9E8eR3ok9cRl0Sw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
🏆
نظر هانسی‌فلیک درباره توپ طلا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/Futball180TV/105994" target="_blank">📅 15:40 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105993">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7d749e34c6.mp4?token=LPQjF-JpRun6KGwrgY5yynRaEhuFl59fgMBcZJoImG7_J-8cnH5PsQ8QqfboiBQcO4HXgDhVbC7hSROhjgTTRZBMxRwZrb_mxu6asi5MJYUw2ak5J8OOp6VwCd2mUpDFAgy00QPo5s-aP3Ds63lPUpwo6fdTA2M-IBFpg0UlrgXfVlJu0-i5l3FF4uZ78CRFkjjr9_0tOU2eqGBPUxcPOKms-llpH8oAkBT8Nku9MoWi_bbh5-orECyRU5rsR8kUT9NtRTJPVKaAY054yAwhfbf3U6YCtQdtu00bXk_LY6YEQozRTI7kqI9syHxR-EOTZdTFV50LURUtFs5ULMCRRg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7d749e34c6.mp4?token=LPQjF-JpRun6KGwrgY5yynRaEhuFl59fgMBcZJoImG7_J-8cnH5PsQ8QqfboiBQcO4HXgDhVbC7hSROhjgTTRZBMxRwZrb_mxu6asi5MJYUw2ak5J8OOp6VwCd2mUpDFAgy00QPo5s-aP3Ds63lPUpwo6fdTA2M-IBFpg0UlrgXfVlJu0-i5l3FF4uZ78CRFkjjr9_0tOU2eqGBPUxcPOKms-llpH8oAkBT8Nku9MoWi_bbh5-orECyRU5rsR8kUT9NtRTJPVKaAY054yAwhfbf3U6YCtQdtu00bXk_LY6YEQozRTI7kqI9syHxR-EOTZdTFV50LURUtFs5ULMCRRg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🎙
🇪🇸
🇪🇸
لب خوانی صحبت های رودری در جریان دیدار بارسلونا مقابل والنسیا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/Futball180TV/105993" target="_blank">📅 15:15 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105992">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a4f76b6880.mp4?token=sqCOUg-nYJGZ4EytkRUcDdnhqsADBa_lVnbrS2vm0YB2jZwHD291a3145UdEDfW9J_ezZ6ovdO2v5gtlxQfGPzNoOHSMTanMoUWjuOW5OWNv4ElwICNU-OUoU5J-JnbeocDd8QuY-ledI9Vg0PMxi4fjY_ch069mWy3S_sMTCBfB0iOIkTx5TWvkbL9HNaQruEo-dfzxulVPQi4G_kRg1jwB6fQAkb_uIrh6-AMZGNCChd4AwnFCW7I9pDAK-pJ7QuVcJtUd7lC0HZ3NPrixGSzwEdhzIDP1xL30KqNmIW06ybrI_cDVVfgC9zHIvH7sxbAv6RqHxpDlXiuTURbCAg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a4f76b6880.mp4?token=sqCOUg-nYJGZ4EytkRUcDdnhqsADBa_lVnbrS2vm0YB2jZwHD291a3145UdEDfW9J_ezZ6ovdO2v5gtlxQfGPzNoOHSMTanMoUWjuOW5OWNv4ElwICNU-OUoU5J-JnbeocDd8QuY-ledI9Vg0PMxi4fjY_ch069mWy3S_sMTCBfB0iOIkTx5TWvkbL9HNaQruEo-dfzxulVPQi4G_kRg1jwB6fQAkb_uIrh6-AMZGNCChd4AwnFCW7I9pDAK-pJ7QuVcJtUd7lC0HZ3NPrixGSzwEdhzIDP1xL30KqNmIW06ybrI_cDVVfgC9zHIvH7sxbAv6RqHxpDlXiuTURbCAg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
⚠️
ماجرای صفرهای ثابت پمپ بنزین‌ها مشخص شد؛ جدیدترین شاهکار مسئولان برره‌ای مملکت
😐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/Futball180TV/105992" target="_blank">📅 14:50 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105991">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6385fe8792.mp4?token=AkhsA3B1Jtad_fIttjuqY3Ai8IeQPIA2ZAN7uYZeWNZ4JCdSMHctyH1-atOUH5YdZoE-uoNn9HBW498pp5Led6CH7b_e26-dh4JLjGgaRKuZK7ZSRiF8vy_SSPFC8ku1t11dUviuXNVireyIWNLQRJtRRyN7fxeKI2LTvNIgZr7Znm6thuy7e4N3MqkWkxKx0os2Yjj0-E9jh5atCUCOgJ2ONvLHZUasmDpnbD-_G_tQYWtJ7kx3vc5DWHvEnBHzZkijPOXKukmLn-orxZh9NnuBSXc5CgBaaCPIrhT0RsPZuZrVnQzcIoSCFtVIUGoRJkfLdLUi2HACqLEkcAx-TQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6385fe8792.mp4?token=AkhsA3B1Jtad_fIttjuqY3Ai8IeQPIA2ZAN7uYZeWNZ4JCdSMHctyH1-atOUH5YdZoE-uoNn9HBW498pp5Led6CH7b_e26-dh4JLjGgaRKuZK7ZSRiF8vy_SSPFC8ku1t11dUviuXNVireyIWNLQRJtRRyN7fxeKI2LTvNIgZr7Znm6thuy7e4N3MqkWkxKx0os2Yjj0-E9jh5atCUCOgJ2ONvLHZUasmDpnbD-_G_tQYWtJ7kx3vc5DWHvEnBHzZkijPOXKukmLn-orxZh9NnuBSXc5CgBaaCPIrhT0RsPZuZrVnQzcIoSCFtVIUGoRJkfLdLUi2HACqLEkcAx-TQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🙂
🇮🇷
🇮🇷
رشوه مادربزرگ استقلال به نوه‌هایش که شدیدا به تیم فوتبال پرسپولیس علاقه‌مند هستند
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/Futball180TV/105991" target="_blank">📅 14:25 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105990">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nBUuZYnpWp8PcE8WQSaQc9vOZb3vNqVERQRWcrU6l6JWMWGfYBM9-39mD6Wu-hKwV66NHfsN4p0LCHyAK7D9p-XNbf8j-S-EibtnGyPnq-IlJZUWJ1jy19_GQAtxZ0KZBi3tujwzRM39bu72uGQcFt2oVYAXvJPGPaJYUcRuskDr3ImO6riwNZhh1hgfbRkZkYqPqK8RaWEesIbgKLn3I5itDO3fKqxpXrGTFh1lVI57KPI8m7A7vr3rTUKHjtmqRbRhK-vE3A7xzWk6fEjj5UPyAkL6vfxpnPd-0lHmmYBNgd7SsO4xap6_DumUYqvXh20f0Yzh9PupmpyyB6kBQw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👀
📊
رقبای بارسلونای تحت هدایت هانسی‌فلیک که بیشترین گل‌رو از این‌تیم دریافت کردند!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/Futball180TV/105990" target="_blank">📅 14:01 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105989">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f3a4352655.mp4?token=kmhlS8e-s-j4M2xiH48KRo5SANETYD8mLyri9Af1aji9iPZnnzBYT4QL5PvoHVRhznrxuHEelQwQjMMxJLVRh7GEqY7QLvbmRCMa297A2TzfUVCgarfHeo4R8-lk5vgfafzzZdQvdvNBw5WvN659Il8xlOT-YQ-kLghdquCV84uzJ4fjoTq7686Yk-tVeBqBQoYrfu5-Y6AoGZ5wJJ8pUApPLH4eEUE-eciEaZuf4JNP-zo4VNiiB6iiL1aCi8YW6zCbrLf4TDzeNNHSy42p0mcf-g7jZyzc185UobHIt0VPm440G1E-FF9lAjpbTpmTkoAradERdqgCg4lVvGkiLA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f3a4352655.mp4?token=kmhlS8e-s-j4M2xiH48KRo5SANETYD8mLyri9Af1aji9iPZnnzBYT4QL5PvoHVRhznrxuHEelQwQjMMxJLVRh7GEqY7QLvbmRCMa297A2TzfUVCgarfHeo4R8-lk5vgfafzzZdQvdvNBw5WvN659Il8xlOT-YQ-kLghdquCV84uzJ4fjoTq7686Yk-tVeBqBQoYrfu5-Y6AoGZ5wJJ8pUApPLH4eEUE-eciEaZuf4JNP-zo4VNiiB6iiL1aCi8YW6zCbrLf4TDzeNNHSy42p0mcf-g7jZyzc185UobHIt0VPm440G1E-FF9lAjpbTpmTkoAradERdqgCg4lVvGkiLA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
⚠️
فرق زندگی در ترکیه و ایران از نظر خواننده ترکی؛ عایشه‌گل: مردم ایران به دنبال پول جمع کردن هستن.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/Futball180TV/105989" target="_blank">📅 13:35 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105988">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3185992aac.mp4?token=U7HSTdOFjkQ-CPtUy4rNVn98qkPhYgAWHNXMj1mK2FqondM8WsMf_bmvdxWLOL_ZuSJmp8P_0hEK1478B8vl0i5GgoTyVJCg6wDSN76PA7OUv0dfZ8nVRoqzJu_mHMN-QvAKVq5Dpe1klFm8ED7wKx4qE0VOpYOBD6v-T1pYZlWO8I4P1pE_vz1TvJ_HQG3YD5tok0sy4CcE7oMw8fBY7pk_hRmAolrHG29XnBqBH4iQTWHL5ZFIpiT6_yBxO-injURTnd_wMxfi1I10LNXwY9HQJBVID3m9Y9uyL3UUBAVkK86Dvm3pmirmQexrVgR-jHR_jFmpcAwLcoTMsNmWNw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3185992aac.mp4?token=U7HSTdOFjkQ-CPtUy4rNVn98qkPhYgAWHNXMj1mK2FqondM8WsMf_bmvdxWLOL_ZuSJmp8P_0hEK1478B8vl0i5GgoTyVJCg6wDSN76PA7OUv0dfZ8nVRoqzJu_mHMN-QvAKVq5Dpe1klFm8ED7wKx4qE0VOpYOBD6v-T1pYZlWO8I4P1pE_vz1TvJ_HQG3YD5tok0sy4CcE7oMw8fBY7pk_hRmAolrHG29XnBqBH4iQTWHL5ZFIpiT6_yBxO-injURTnd_wMxfi1I10LNXwY9HQJBVID3m9Y9uyL3UUBAVkK86Dvm3pmirmQexrVgR-jHR_jFmpcAwLcoTMsNmWNw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
⚠️
🇪🇸
توصیف عادل فردوسی‌پور از ریدمان فوق پشم ریزون دیشب رئالیا در بازی با اینتر!!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/Futball180TV/105988" target="_blank">📅 13:10 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105987">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/058b97f620.mp4?token=sfEGUGlUGzQBAwzgcfk_p_sidZN0aSzGiTFltVIx1lFbIRydHyQ8v_jLFaHUhQXfaSrLT3KyDJtBU23dYxczaAEGTRxy1kiWdBKwrWVpe5TXLig2ABd8_GCvTTcsx7rkS3ifcl-wJ92QCkjOsYppwfPk8TD5HR7LbfonWdLr8O-3PEpNuRMWRMZTieP7-rC79w6y6AfDMay_J_b31jewBqrFY7Cxool37oNc42F04fdXNlMbiOQaRsGj3WbQc6iCXJZolKjZQUw3sdAynUxKYbTktnuoc0eugeZVS8A_mjuG5Nu8l7wnjyd3NGbojcrtdoOA_1pu1lYgsevhVP5iV7Sve25PBYtiQYpwCaY2Gdl-rgqFAvCvgyeIQ2woM-BwDLz-rtOnndc_sJr1CYNZteG9cnYwSgGLTm3exa2Gw1DP1F6U_Wn6pRfT-qYZFORaeFMnLC5PZeyKHekIxAhdeOY2hdMQIOaaGT51SR6nZml1D0LFZ0OtLQk2JVrgloFji2mXDf33SJoL2tiHfECI2xvG3X-1add2kT9YOa6FGrQmYwUgm3TiEkqvC2Jlra8_0fQAnJ2Cdfo3DeiOqkXPibs1rbyKWmlz4RchpvGnZMOkyeJoJ9shN75q10IzO3VPiRsagQhNNLF_NWvGxtB8xhrmtfHf-uf92Hx5zfTfa5k" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/058b97f620.mp4?token=sfEGUGlUGzQBAwzgcfk_p_sidZN0aSzGiTFltVIx1lFbIRydHyQ8v_jLFaHUhQXfaSrLT3KyDJtBU23dYxczaAEGTRxy1kiWdBKwrWVpe5TXLig2ABd8_GCvTTcsx7rkS3ifcl-wJ92QCkjOsYppwfPk8TD5HR7LbfonWdLr8O-3PEpNuRMWRMZTieP7-rC79w6y6AfDMay_J_b31jewBqrFY7Cxool37oNc42F04fdXNlMbiOQaRsGj3WbQc6iCXJZolKjZQUw3sdAynUxKYbTktnuoc0eugeZVS8A_mjuG5Nu8l7wnjyd3NGbojcrtdoOA_1pu1lYgsevhVP5iV7Sve25PBYtiQYpwCaY2Gdl-rgqFAvCvgyeIQ2woM-BwDLz-rtOnndc_sJr1CYNZteG9cnYwSgGLTm3exa2Gw1DP1F6U_Wn6pRfT-qYZFORaeFMnLC5PZeyKHekIxAhdeOY2hdMQIOaaGT51SR6nZml1D0LFZ0OtLQk2JVrgloFji2mXDf33SJoL2tiHfECI2xvG3X-1add2kT9YOa6FGrQmYwUgm3TiEkqvC2Jlra8_0fQAnJ2Cdfo3DeiOqkXPibs1rbyKWmlz4RchpvGnZMOkyeJoJ9shN75q10IzO3VPiRsagQhNNLF_NWvGxtB8xhrmtfHf-uf92Hx5zfTfa5k" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
‼️
💙
بختیاری زاده: بازیکن به تیم امید نمی دهیم/ تیم امید مهم است ولی شرایط تیم ما مانند تیم های دیگر نیست/  فقط آن زمانی که قانونی باشد بازیکنانم را در اختیار تیم امید قرار می دهم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/Futball180TV/105987" target="_blank">📅 12:51 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105986">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fx2-7pu1dhP8W7xYhRIW2zEPoXSpTbuWiBSlhN59NVUUGoLEXJiE_gkzrq2HEUA-p--xPUjDGa0jBSWwc36h3df7cAbnr8XDdD2gRyclUxjw9eIRnPHvD61kcmGgFEu7yEQjZAb4Aj5KVQEYi_PKlfgquoeveaOVnEw-l2iKgSIYrw0tFX0rRXT3pAZsvLTmF9oXLaFA9vw3UQoN24HOi-TXdGZo6mhSfE7D5PlDil-sAcvs9TATMKeCjLlZZRYrWjPF9Bs7Wl7Ml5NWJpVmzZUBuLmI65N-jGx4lmcyn_jl00BmEpESTyPSAoTDa77DyP94hrwGpUZKDbSTOWImMQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
⭕️
⭕️
⚪️
یاشار سلطانی فعال رسانه نوشت: ‏در پرونده فساد فوتبال⁩، برای تعدادی از مدیران ارشد و چهره‌های فدراسیون فوتبال به اتهام اختلاس⁩ کیفرخواست صادر شده است
مهدی تاج⁩
‏محمدمهدی نبی
‏احسان اصولی‌صفا
‏تهمورث حیدری
‏خداداد افشاریان
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/Futball180TV/105986" target="_blank">📅 12:49 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105985">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/Futball180TV/105985" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/Futball180TV/105985" target="_blank">📅 12:49 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105984">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Z026uW3CunrBYV1BYH69uKYViT0FAXIFBluk0pIAHR3pmK5Yq_8VFYE3rKNa6YjmRKg5fvWfRaqFMmBFnDjyuNO6_jDFGhRmXeniI51MVGtJboEcQ-CPGrFRg3Sl0Cz7rYxmkVf-rlRoUe5WJ8-Dgeld6x01RzV-rePpoQEtd-UBxw1FN7PSm2OR3AM-mAyKEsajaFIxxISoRlNik4dYgVFJhqF1IDgp26AxhWXpKeqrV2YoWOGrYKI6J7MUWFwV3DDGMSd3UVFXryoQJ16JnKLHFsuSTccE0DJBuJ6GWNoVwFFI5b3Y2Gve7IkdWBUqPtMAYnwhuErkW6SpBPtM1A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
شبِ بزرگ فوتبال اروپا فرا رسید!
⚽️
اتلتیکو مادرید
🆚
لیورپول
⚽️
🎯
این نبرد حساس
چمپیونزلیگ
را در سایت بین‌المللی
TrexBet
پیش‌بینی کنید!
📊
نگاهی به آمار ۲ تیم در تقابل‌های اخیر:
⚽️
اتلتیکو مادرید: ۵ بازی، ۲ برد و ۳ شکست، ۸ گل زده
⚽️
لیورپول:  ۵ بازی، ۳ برد و ۲ شکست، ۱۰ گل زده
🦖
بونوس اولین واریز تا سقف ۱۰۰ یورو
🦖
بهترین ضرایب بین تمام سایت‌ها
🦖
واریز آسان و امن از طریق کارت به کارت
🦖
🦖
🦖
🦖
TREXBET — PLAY. PREDICT. WIN.
https://TrexBet.com
T.me/TrexBet_Ir</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/Futball180TV/105984" target="_blank">📅 12:49 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105983">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5cd51b2d93.mp4?token=bhDwR3jApRuwb9-lYiOYy5_w5oti8htsbQsTJ0akkz7-_swaQtugn8AXA5FlLU9Wzjz48QYdJqMqtmVRtaHL6NBGMsW1xbBpyYuiZTz77MkqM5b3JjYmwCdyh6BIlXos--C3cnAz-SvvSTDBHC1AX9v_2mDspVJ9Rt4LjscPGogPSrxpPWgjkkBhzc2BsolYZUJSGb1GpF-I48ZeRz0JYVhCvLEZ7GJEC4rtW16DGlEejpy1V4Q-W4B6L_U2IJjVwo2FfAvj2Utfs_Yw7-zN8u5NFTuR2LmxBAxH0qAUhmzapSisUkXBNSTnFCuSMIydtfNun9viRnTsT8cxax2WN28XnbYSzqmddAfvpEoHUsTXfp6Pud7AoS2SeJ9rcxvWXf3LsffGPBAdQ42CsCzS3LKBvUGc-rP88QoK_lm6j_mW_3rjjJYPEpDQSMjMJVt4wol2ilfaYmxTh6grYo8nMsOBnkpxFS6gPlWz3cb_gheFLce_GM7G83qOjZAUrxkQvkHfdIAi-EZzFVQ-8v0FPIII37Ha7oBEGTEF27tx2dhqln5aUrai-5cBs5mSldsO5_twF1uAWvMvjTx4wuT5vO3WZTkSsQFoRqH835p9G19IK8wwEr8LwICW5T75Gry5lWvvaRk47spD0TaKsUwAaDO7jLG-pbs7-yE76YzgeTA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5cd51b2d93.mp4?token=bhDwR3jApRuwb9-lYiOYy5_w5oti8htsbQsTJ0akkz7-_swaQtugn8AXA5FlLU9Wzjz48QYdJqMqtmVRtaHL6NBGMsW1xbBpyYuiZTz77MkqM5b3JjYmwCdyh6BIlXos--C3cnAz-SvvSTDBHC1AX9v_2mDspVJ9Rt4LjscPGogPSrxpPWgjkkBhzc2BsolYZUJSGb1GpF-I48ZeRz0JYVhCvLEZ7GJEC4rtW16DGlEejpy1V4Q-W4B6L_U2IJjVwo2FfAvj2Utfs_Yw7-zN8u5NFTuR2LmxBAxH0qAUhmzapSisUkXBNSTnFCuSMIydtfNun9viRnTsT8cxax2WN28XnbYSzqmddAfvpEoHUsTXfp6Pud7AoS2SeJ9rcxvWXf3LsffGPBAdQ42CsCzS3LKBvUGc-rP88QoK_lm6j_mW_3rjjJYPEpDQSMjMJVt4wol2ilfaYmxTh6grYo8nMsOBnkpxFS6gPlWz3cb_gheFLce_GM7G83qOjZAUrxkQvkHfdIAi-EZzFVQ-8v0FPIII37Ha7oBEGTEF27tx2dhqln5aUrai-5cBs5mSldsO5_twF1uAWvMvjTx4wuT5vO3WZTkSsQFoRqH835p9G19IK8wwEr8LwICW5T75Gry5lWvvaRk47spD0TaKsUwAaDO7jLG-pbs7-yE76YzgeTA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
🇮🇷
بختیاری زاده، سرمربی استقلال:
صالح حردانی و وساطت دیگران؟ این جلسه برای بازی با پیکان است و قبلا در موردش حرف زدم. تنها چیزی که روی آن متمرکز هستم پیکان است. همه بازیکنان برای من عزیز هستند اما نام استقلال برایم مهم تر است و اجازه بدهید روی بازی فردا تمرکز کنم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/Futball180TV/105983" target="_blank">📅 12:42 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105982">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/72b7d3e3a6.mp4?token=dcmPxbcPOrzAbq11Bvwafo-VN9AzUCyrT35PUFjZTgRrcV6YQToRl3GhIc72v76If-7GIYmasZswqJXROaCJDGZD4DtHrwPUXwFwkPZ31bOQQ_tP2DAhAsZVtPcLWKmxQfRl4mKu1Trt2-Iuj4cwhsuGac-XxD6IvH2KBgFnAWX6g4dPKKKSvdF1xgZm9jjC6RiFk009mO91CpifagTg_zFEeBwClKU3dpmnuFqBfsfh-RQ26ccsyWjPipiYAl9c_-sBQb7LI0y0Kbz13Ml7PlRqwS25vHlF9ahKaVz696JRUgL3bvQQgiFhAgKbtC_H3iaDNdTtIH51YsOcVNLxFQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/72b7d3e3a6.mp4?token=dcmPxbcPOrzAbq11Bvwafo-VN9AzUCyrT35PUFjZTgRrcV6YQToRl3GhIc72v76If-7GIYmasZswqJXROaCJDGZD4DtHrwPUXwFwkPZ31bOQQ_tP2DAhAsZVtPcLWKmxQfRl4mKu1Trt2-Iuj4cwhsuGac-XxD6IvH2KBgFnAWX6g4dPKKKSvdF1xgZm9jjC6RiFk009mO91CpifagTg_zFEeBwClKU3dpmnuFqBfsfh-RQ26ccsyWjPipiYAl9c_-sBQb7LI0y0Kbz13Ml7PlRqwS25vHlF9ahKaVz696JRUgL3bvQQgiFhAgKbtC_H3iaDNdTtIH51YsOcVNLxFQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇺
🇩🇪
🇪🇸
دیشب چهار هزار سکو برای هواداران ویارئال تو ورزشگاه دورتمند اختصاص داده بودن که خالی مونده بود. فقط ۳۹ نفر از ویارئال حضور داشتن که طرفداران دورتمند اونارو وسط خودشون جا دادن تا از تماشای بازی نهایت لذت رو ببرن و البته خیلی دوستانه تا آخر بازی کنار هم نشسته بودن
😂
😂
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/Futball180TV/105982" target="_blank">📅 12:17 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105981">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7d0af12019.mp4?token=Gntqr2F2jjqkC8MbH_Yf8G2Nu67o7O_FVrnpVfnj3_0wSTfRaMRQBtXLz69KQgYUW5qaRuUoOuekbLy8bO0Yt2KyUB53BAq1Ql7r4rr4KP2Y-dvmKTLctTca4G_NhYW3hLLs_IWjIYxI_wZpONyzzMa0Z69bKBVQ2jC-8-RRvwkk3yfroOaY-nvLbvL0B6FnCvjk8s1yhes6dlMOPCCxkmFUf_YDrfWgQBjZgZwjwcDwCCTpnYm9_qQoIAXPxuciB9KYvlXn9gMh4CVrOxFVrrETf7HgYr99TSAy-cu5ZKFi-oYOZvCttgdhLEfkbzGKQTFHty8TfXYvW2imLWUq0g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7d0af12019.mp4?token=Gntqr2F2jjqkC8MbH_Yf8G2Nu67o7O_FVrnpVfnj3_0wSTfRaMRQBtXLz69KQgYUW5qaRuUoOuekbLy8bO0Yt2KyUB53BAq1Ql7r4rr4KP2Y-dvmKTLctTca4G_NhYW3hLLs_IWjIYxI_wZpONyzzMa0Z69bKBVQ2jC-8-RRvwkk3yfroOaY-nvLbvL0B6FnCvjk8s1yhes6dlMOPCCxkmFUf_YDrfWgQBjZgZwjwcDwCCTpnYm9_qQoIAXPxuciB9KYvlXn9gMh4CVrOxFVrrETf7HgYr99TSAy-cu5ZKFi-oYOZvCttgdhLEfkbzGKQTFHty8TfXYvW2imLWUq0g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
⚠️
🔴
یادته آن شب ماله‌کشیدی؟ شاید اگر آن شب با خداداد برخورد می‌کردی امروز می‌توانستی پاسخ پسرت را بدهی!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/Futball180TV/105981" target="_blank">📅 11:55 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105980">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">🎙
🇪🇺
🏴󠁧󠁢󠁥󠁮󠁧󠁿
نظر هالند درباره اولین بازی ایوب‌بوعدی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/Futball180TV/105980" target="_blank">📅 11:32 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105976">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/XzaDtV-DnlkZrVzo_fovfsVUR4OHLlX8MACrucV5A_G0QPk4C_4qwGPjFPQmz-wSod-W0Ives7vLInLKMM3Hc5uEWKn2_IGLloJiOVKhYGsJzT6ZsYYIoF3wIaCdROBzd1TmV40bzafGh_6t-NeUkuZwmyQQY2KcWg6L2ZggfYbL5vvHIu1A2d8qVDclXxzCaBsewMHreGrRDYaqa0O3gMTwP-51HkHkYJTsfuQRZjTGHh0QTK0r4KEjPR8pPTanlPgTlKYPel025uNVzox6w6B7GPbV5Qh9WJ5a1m_07YSbj2jjB2TWqfR-qoFhFFCr2JeStJN55rCJbDqYjgw5VA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/tPOn-GOZxx6BYzzsp_k7BrU0CQ4G7ERqSs9NiOL8z2nwDzuF_wvZSAazH9-EMaW63faGaxMP9roCv-jRn_OnN70zViUxMkNxQgs75xZNL_tJ6F7Eguzp5wRbD0e696hV9OgaFXI60hEceVeAZuCLSUn58KJ7lwoUQIdnQGwRoBirxlKa5n9f9xLVhlqjnzFKWXfajdBXHNLnaq5_0raIqJfs45NoTfyK8KB25gJhIjDmQylT_x14HnSN6AA2BWABKb3hI8H9woAotgY2dU9PxmyUrBWVpmi_Hxk1MSA_0QrUub6PtY0X4wzpEnJQyNR6GU3XDiSC-cun7TV_oo38qQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/S-R4ENLxYdd1dcofDGfGN3CcOhtjbdPIQYlzm4Osfj-RvG8fH9gYppHDhJeiGl8gregBRwwp48nR7szX2A0lPM_34KdUPGhbzAO3seRtNX9nj-yusZFF0H2lTgrFQbnc3s2MZhKCcGtQBK7c7Y3oAK9FJAtUdPPw0GLl_dEqOi50PlrWYHh_4D8cw9_AacMFNt9Gqwh2wpyqXcFHmDSigB4zrrGLJ9R2AdWfr9GWPUj_TbvlNqwZ0yD6vJpbuUDJuUkluhWBjO8lKv-teOpruiojTTfHpnBtcGQ6U-cmVO84X_VAlJ51YsVGIHIm2Kfve62hCzD66cp9nlLdNHbAtg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/PUPdWcEsqZ78_42BokBn_rc2LlAgqr-UyF8IGY2fuuv09zCQlm2Sh0rrb31tg4nv94wB5jUM0N3CgCcuThGDztL1umvNqPPbNzDUZACDbT_wOnGQqFz_K6AMVGvsIUoQQBevuMpw1Pfe_5f2b4mzPAj_Tdhr0ScCsTYXYTa22-DVernpJskpLXVWpDH2fPrjFJQPxXMjcM_xUhXfwxW1wtQyv-k2gPkgL43mB2tjsUXRLQ-H5XqmbQmhC2nLOrnd4at23YKHmNWyU0ECVJmuZWtgthe94TJJf4jeX_S5dIcwP4CbsD0LzGdjQ3-mdohVYuoAoIXK-sSUAsm9rDnt6Q.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👍
✔️
🇮🇷
تمیز کردن سکوهای شهرقدس توسط دو بانوی بافرهنگ پرسپولیسی پس از بازی با ذوب‌آهن
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/Futball180TV/105976" target="_blank">📅 11:05 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105975">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/C5rvpErIHOJEnSN3OzppyGJuTvcSWuaRSWjXrehwk8aEj_vYKl4TsqRAbqf18LqcaaH18Vz-Et-B3McYgzQFDoYdlXCicWYleI-maua3XPNzT71vkmz_lUQBDWCQHTKy11TKwUy2RJ4X1X2O9AE82TQs-LDSR2Ar61cZqoFdJfEvCKJmovTIQpZGGJM-IVEcG72EV0ztQjbZ9VVtmN4IF0vQUidXtX15YMR2gt1WGh1UZXIYKTT0xRvYbs34DlAMhBWjN1KYQZcnDAiZpkNOJCc2y8ACF-0kpn5DIIX0P_FN7a4TD2iWGPVQleGx2vgHJfKs6IIKQZZ9BYqe_qdoXQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👀
‼️
تصویر جدید مهدی‌قایدی و خانوادش؛ عکس زنشو هم سانسور می‌کنه تا مثل قبلی بگا نره
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/Futball180TV/105975" target="_blank">📅 10:49 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105974">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/49d195a639.mp4?token=gRZgHRJ3eXafP4xzPmDqyBV_-qMVlAKUis3b9y92sa28BDGcA6ugFNbZ245borYLq26DMd0gYS1Dwp1sx59YotrzxlsMavLjBkKuPACIc264LvCqm2TIZGmKOYPpjVhEcnRENGPd_CKCuSQdkf2JoMwusZPlT7OEDgCkotys-ehVbpJAjjX04sw5qTuVYGXAnuts5KEfOO0m-AjszjHGwEkSnwFRXuoJqGmoJClK76gLIcMDRMHBgpFjMbF4HlNt5h_O1wp-Xnm2mawq_TODVNysZtiFa-Px3wmhvzhy2aX9XA2VzC7bfhPSHKiYEYNi_UH2XHLIOhURIV1JyiKf9g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/49d195a639.mp4?token=gRZgHRJ3eXafP4xzPmDqyBV_-qMVlAKUis3b9y92sa28BDGcA6ugFNbZ245borYLq26DMd0gYS1Dwp1sx59YotrzxlsMavLjBkKuPACIc264LvCqm2TIZGmKOYPpjVhEcnRENGPd_CKCuSQdkf2JoMwusZPlT7OEDgCkotys-ehVbpJAjjX04sw5qTuVYGXAnuts5KEfOO0m-AjszjHGwEkSnwFRXuoJqGmoJClK76gLIcMDRMHBgpFjMbF4HlNt5h_O1wp-Xnm2mawq_TODVNysZtiFa-Px3wmhvzhy2aX9XA2VzC7bfhPSHKiYEYNi_UH2XHLIOhURIV1JyiKf9g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">داستان خداداد عزیزی و عالیشاه با صدای علی دایی
😂
‼️
🚫
حاوی الفاظ نامناسب.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/Futball180TV/105974" target="_blank">📅 10:40 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105973">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/32b4f4b4bf.mp4?token=Mxada3QFpM6Hph9Akrp1WWFQJjdIKl6lYPfQAptWgtYaoafht_7C0iVB82d731VcCF29I7v33tmZbIvFh-TMwJGggb_SpWhVZ5u2JuE5PeFxTdZ-p3jNTmPCwhmltNxMuxIER2kEVqKJS1ZTzl5U8lrzVkc1D9SoyVJyR58CoNK9pEeL9YYIM1oM65wPXRiVZwtH7u17W_tB0CQd8fjtW-jFqvUimXdCOSOwLr0dHmGiTpJBGagSjZPTFCIeufZKwlXVkMSCrTgL4jMrdAiElPiybOt9PA8K19CE5gnJlx2W__icxtO5as1Bo__2p-KYlnNdmZivhQwtrQTgYNPMcQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/32b4f4b4bf.mp4?token=Mxada3QFpM6Hph9Akrp1WWFQJjdIKl6lYPfQAptWgtYaoafht_7C0iVB82d731VcCF29I7v33tmZbIvFh-TMwJGggb_SpWhVZ5u2JuE5PeFxTdZ-p3jNTmPCwhmltNxMuxIER2kEVqKJS1ZTzl5U8lrzVkc1D9SoyVJyR58CoNK9pEeL9YYIM1oM65wPXRiVZwtH7u17W_tB0CQd8fjtW-jFqvUimXdCOSOwLr0dHmGiTpJBGagSjZPTFCIeufZKwlXVkMSCrTgL4jMrdAiElPiybOt9PA8K19CE5gnJlx2W__icxtO5as1Bo__2p-KYlnNdmZivhQwtrQTgYNPMcQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🐐
🇪🇸
شعر مایکل ریچاردز در وصف امباپه پس از درخشش در بازی دیشب مقابل اینتر
😂
😂
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/Futball180TV/105973" target="_blank">📅 10:15 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105972">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cf52ab1a36.mp4?token=dWHux1f34gEkg638O-FD2zrank3mTOGIf3vuTB1LuEviKTecrfLcZnmSfxUgOxkyPvG4sYCAbpCD0qJfKHqYxmdFa3gYXAVe2fNs_IuqlUKPd7vdQwhQlZAUUOCbZP6qrNknL7tu0f15sNc-aMjMhuxm4DlNRMDVc2SsYOxL9_Xc2ou_0NRXzsy2_0u-gsdtvpW1WUzayMXm6DDBpSYyFfSQA5dGfYRIxAKGIZv-zwEByi0j2iq7Tk8PD0gFL4gPJ6K4ikueSsQgcRT66-PbZnzGH1-cM9Tvj9uHcMJLlOCQ8mU0d6EsSSZEvpibHA39Mc_GV1RGIRJsOddaxk-8yg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cf52ab1a36.mp4?token=dWHux1f34gEkg638O-FD2zrank3mTOGIf3vuTB1LuEviKTecrfLcZnmSfxUgOxkyPvG4sYCAbpCD0qJfKHqYxmdFa3gYXAVe2fNs_IuqlUKPd7vdQwhQlZAUUOCbZP6qrNknL7tu0f15sNc-aMjMhuxm4DlNRMDVc2SsYOxL9_Xc2ou_0NRXzsy2_0u-gsdtvpW1WUzayMXm6DDBpSYyFfSQA5dGfYRIxAKGIZv-zwEByi0j2iq7Tk8PD0gFL4gPJ6K4ikueSsQgcRT66-PbZnzGH1-cM9Tvj9uHcMJLlOCQ8mU0d6EsSSZEvpibHA39Mc_GV1RGIRJsOddaxk-8yg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇷🇺
نادر محمدی دیشب برای سومین بار با اوت دستی تو روسیه پاس‌گل داد و حالا اکثر رسانه‌های ورزشی جهان کرک و پرشون ریخته و گفتن که این بازیکن قشنگ به سیستم آرتتا تو آرسنال میخوره
😂
😂
😂
😳
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/Futball180TV/105972" target="_blank">📅 09:44 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105971">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d5d2267479.mp4?token=VC2nw6_mpOW8C0smenGGq38k1IuhF09_6elSQQWsm-MToB3hC2-XLDXcf7Kwzmfdy-Oi8r2rRftIKMmT2TpgrMfPtpIIrtq76E23QXinnXNL8MDRSEUyCD6dVRitO6ZvC0aQyOlpiMSAbi1GEnlRrk2cl0GvgjSHQSiTlAJu7l6qBbEEKIiI0LDznN6T1PnALTUC0ye8IIohbXhGIOT8wP7SVgBvfkBrmMgxZ6-pZqQwcikOVXLBw2A_UYApWwlteOmwbkpLyPTbcHghnU2HzsFctaG0tQYQgTdyM1On8cj4vNNftjAEEoapHYtEUClYTn3S0QOFCauKQqqu1ISaeg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d5d2267479.mp4?token=VC2nw6_mpOW8C0smenGGq38k1IuhF09_6elSQQWsm-MToB3hC2-XLDXcf7Kwzmfdy-Oi8r2rRftIKMmT2TpgrMfPtpIIrtq76E23QXinnXNL8MDRSEUyCD6dVRitO6ZvC0aQyOlpiMSAbi1GEnlRrk2cl0GvgjSHQSiTlAJu7l6qBbEEKIiI0LDznN6T1PnALTUC0ye8IIohbXhGIOT8wP7SVgBvfkBrmMgxZ6-pZqQwcikOVXLBw2A_UYApWwlteOmwbkpLyPTbcHghnU2HzsFctaG0tQYQgTdyM1On8cj4vNNftjAEEoapHYtEUClYTn3S0QOFCauKQqqu1ISaeg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👀
🇪🇺
🇪🇸
اینجا لیگ قهرمانانه رفیق! قلمروی پادشاهی رئال مادرید.
🔥
☠️
👑
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/Futball180TV/105971" target="_blank">📅 09:31 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105970">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/15481b67bd.mp4?token=UvHbxnXDCTjXOkjXC-Dg25v9JCfRQt5ESrY03x6j5iTTpg6jtH-iJDxXT4jTqwolWE_OZDd59aeN_NVpXFP-uwXFijTHQVWHjADvlMvAzw9WqyhecUUbxigBn_Ezfz5TjHAcweWBE8XMrEEmYujV5cfQ1n2Xra6C9SWoxN70xTUyl_de58NUMI6LAxAwPWWXdR4hs_hISyw3TIGIYqSk5jeiYeNuTGcTyrDkqYI4EXZC0IXqZTV5CB8RijDL9oI_mgXZ1Vh3OxvMjl6VyxatyvsKL6Wo0qeWWrJeNGV-5Z5lZhYQ_P2cAJmaAO7TATWUmQlkQfYEKDdL3PT5U7U3-nbr8FbL3VV0lkPBDwD-4D4QuVgVOciJUDkVLCiJM2T0O4eMvc1DZGK345wcqu2lEZEbmnSwF9Ws2CPb4B_PQgEy2ljy9BomRx7AhHFCCyIMUXuXiZj5WCWOQCWgPD6ypUnC_de40-6TjZfSROX2XXD9HxA9TNEq5VW4H-pIPdLsRVzmlmD4LuoLNlrmoCTY_GvKIdt38OphqSgaQb6S6CWOz2eaCw_UP7nMFNWEEaagL0BJXvkJZA3wVBcjdo_7Asbv_7jJvmgV9fe3CRiDPbDZlJXSX4Q8QRCi0vaZXMlNv_H445amd8HcZhVAKrw8I-lpLZUz6z7k-klkWdoVtUA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/15481b67bd.mp4?token=UvHbxnXDCTjXOkjXC-Dg25v9JCfRQt5ESrY03x6j5iTTpg6jtH-iJDxXT4jTqwolWE_OZDd59aeN_NVpXFP-uwXFijTHQVWHjADvlMvAzw9WqyhecUUbxigBn_Ezfz5TjHAcweWBE8XMrEEmYujV5cfQ1n2Xra6C9SWoxN70xTUyl_de58NUMI6LAxAwPWWXdR4hs_hISyw3TIGIYqSk5jeiYeNuTGcTyrDkqYI4EXZC0IXqZTV5CB8RijDL9oI_mgXZ1Vh3OxvMjl6VyxatyvsKL6Wo0qeWWrJeNGV-5Z5lZhYQ_P2cAJmaAO7TATWUmQlkQfYEKDdL3PT5U7U3-nbr8FbL3VV0lkPBDwD-4D4QuVgVOciJUDkVLCiJM2T0O4eMvc1DZGK345wcqu2lEZEbmnSwF9Ws2CPb4B_PQgEy2ljy9BomRx7AhHFCCyIMUXuXiZj5WCWOQCWgPD6ypUnC_de40-6TjZfSROX2XXD9HxA9TNEq5VW4H-pIPdLsRVzmlmD4LuoLNlrmoCTY_GvKIdt38OphqSgaQb6S6CWOz2eaCw_UP7nMFNWEEaagL0BJXvkJZA3wVBcjdo_7Asbv_7jJvmgV9fe3CRiDPbDZlJXSX4Q8QRCi0vaZXMlNv_H445amd8HcZhVAKrw8I-lpLZUz6z7k-klkWdoVtUA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
❗️
🇮🇷
باشگاه پرسپولیس دیشب طی یه حرکت سوپر و عجیب، تمامی فحاشی‌های اخیر خداداد عزیزی رو در قالب یک ویدئو تو لایو باشگاه پخش کرد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/Futball180TV/105970" target="_blank">📅 09:14 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105969">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/T0U8Cn28Wm4mCnYQ_JYK5_VbECtVlz0P1_qV07u9yJqrp5z650IadL5ZCZsErwRiifhcRuF34Emqf2NMD1Szqb6WmwYeLeIqaK2e8IhqzpcG_Xp2K-BJ8Seep6_XofE44QdPy4aEh8QVcgPZwyHwUaHDrQWdZZDKB9BztNN-vWUj65qv1G-3pxgZ9D4w1gV8XkmGTv1pV6xbpzi0Uwlt355tIFAQVvE5dhtO6pAyNK3rp3xuM-EELgACH9BXLcMBONCOHHvdOJsTp3dvYGcY6ccI_jA2v-4-ICRiZmxof8ZzbwZbixG13f99w3VU2QW61d4LTI73-R-duMEjtAoqWg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👀
📊
🇪🇸
مقایسه اسکواد دوره اول رئال‌مادرید تحت هدایت ژوزه‌مورینیو و ترکیب‌فعلی در اختیارش
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/Futball180TV/105969" target="_blank">📅 09:01 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105965">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">خب دیگه بگیرید بخوابید. تا وقتی بی‌بی دست به کار نشه این موشک زدنا اسمش ترقه بازیه
🚬
🚬
🚬
🚬
🚬
🚬
🚬
🚬
🚬
🚬
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/Futball180TV/105965" target="_blank">📅 01:19 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105964">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bf482be15e.mp4?token=UooiTrV5aHL9eskj8_v1LL--PhGlANeQErnJXQQWQ_F6K3dMQ3HEQ9VHREDdTMdADquP3F9JoDYvEYm3PZbbL2qTzFLS-MAoMeXe5nYv2o01qIXXyKF3Jt45Ew2Y_IYVebQgLjQRN4UttcsoAIWTPr1042MLVD2D7OBIkErnlQ3oiVC-bJQOsNq4rh4n8Vbwmo_o9Y6V-TtH4AlvE2ijfKL3-WjBDkDdUpda1rsOC4M3P0a_cdvrvduwEipv4v4XwbHxyfhJ4Stgl3k3p3Qjc-dGlsMd5m-grOqIFd4Ei5pGs5ccrmxzhZtlGRnBT9h2X3Fmmeg2YdGIYDRZJcCiRw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bf482be15e.mp4?token=UooiTrV5aHL9eskj8_v1LL--PhGlANeQErnJXQQWQ_F6K3dMQ3HEQ9VHREDdTMdADquP3F9JoDYvEYm3PZbbL2qTzFLS-MAoMeXe5nYv2o01qIXXyKF3Jt45Ew2Y_IYVebQgLjQRN4UttcsoAIWTPr1042MLVD2D7OBIkErnlQ3oiVC-bJQOsNq4rh4n8Vbwmo_o9Y6V-TtH4AlvE2ijfKL3-WjBDkDdUpda1rsOC4M3P0a_cdvrvduwEipv4v4XwbHxyfhJ4Stgl3k3p3Qjc-dGlsMd5m-grOqIFd4Ei5pGs5ccrmxzhZtlGRnBT9h2X3Fmmeg2YdGIYDRZJcCiRw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
🚨
🚨
⭕️
⭕️
⭕️
⭕️
لحظه باز شدن موشک با کلاهک خوشه ای
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/Futball180TV/105964" target="_blank">📅 01:16 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105963">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">🚨
🚨
🚨
🚨
🇮🇷
⭕️
⭕️
⭕️
یک منبع ایرانی نزدیک به سپاه جمهوری اسلامی: امشب از موشک‌های خیبرشکن استفاده کردیم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/Futball180TV/105963" target="_blank">📅 01:15 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105962">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a4c52f8bf8.mp4?token=LBL4L1RHuwKs5SUID3p3mrqf8c-rDcMIZjuQ0mr_VNMNaitu-HP-POMDyh86vq3qAp_kIMr7ktrGuoIOzbNWozmDC1zcuZ8k9vDxvxAGyZDv6U9wbSXdeJ6afpytBhQ66v_b0H0zjPi8MB7S0SEUGYr0GrKBdexNOg_90zyvyH8ibwq58MsXskw7Y3_bGhQ0xtBrqHY5FZR7n_dp97YuAthUmHTI31kzikaaSujyYZmOEE6GfpM5b8L2YKfs4h-kmlMDNv5RdcLJWQKrGNkLAzm1krP0O9M2PjFnlK_GVeWTgNgSW3bobYEOsXqQ7S2cPb5eV6CngdeQtqrI81h3ZQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a4c52f8bf8.mp4?token=LBL4L1RHuwKs5SUID3p3mrqf8c-rDcMIZjuQ0mr_VNMNaitu-HP-POMDyh86vq3qAp_kIMr7ktrGuoIOzbNWozmDC1zcuZ8k9vDxvxAGyZDv6U9wbSXdeJ6afpytBhQ66v_b0H0zjPi8MB7S0SEUGYr0GrKBdexNOg_90zyvyH8ibwq58MsXskw7Y3_bGhQ0xtBrqHY5FZR7n_dp97YuAthUmHTI31kzikaaSujyYZmOEE6GfpM5b8L2YKfs4h-kmlMDNv5RdcLJWQKrGNkLAzm1krP0O9M2PjFnlK_GVeWTgNgSW3bobYEOsXqQ7S2cPb5eV6CngdeQtqrI81h3ZQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
🚨
🚨
تصاویر منتسب به حملات دقایقی قبل سپاه به مناطقی از اردن
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/Futball180TV/105962" target="_blank">📅 01:13 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105961">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">🚨
🚨
🚨
🚨
🚨
⭕️
⭕️
⭕️
⭕️
حداقل ۲۰ موشک به سمت اردن شلیک شده
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/Futball180TV/105961" target="_blank">📅 01:12 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105960">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YXB6m2hnuFmfnUatvwHm6Go15NHTbzt77qN-yB8Cwl-P9w_uKIi7nLpd4BGuqCSHHN4k4gZXCv8NOM8RytViFBnChf1u3gidDGaZZFQtXGrPqEffd04nwaEYDshHnUNrMONT2VG_5YUNiWi0W8zlxHNuz52Ar0h21nP84T8jLhjyUwUhSRRQLuPoSwY0jjIOEExWe0IeuTKMrw717Tb5wJIgJ8fkOTfs8xO5cipYkCW89-FKGzQ9zoQPVcueWE4OZPaJ-nilAtQl-XzBqOXytW_ow0WbCxnC4cqaifAH8sID808OeN-FOd3BG4c_IQTjBamOby8OwitCVUWnQz-KXA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🚨
🚨
⭕️
⭕️
⭕️
⭕️
حداقل ۲۰ موشک به سمت اردن شلیک شده
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/Futball180TV/105960" target="_blank">📅 01:11 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105959">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b19aa63524.mp4?token=sBcsgfIxDxEHhGXpaTgN3HyD09tJGWY6J5WwJ5gjJQfGB0MEwdTId83DbzZ45USsb8lR7Fd-7UzghuXox-8uPVyifk8dvwksK60tgmfJzJRIgtyVNyoPqWNWTsD5ZGgfC9OZThxrSObuek942lpuxeI0MDdIzSdROApOMMTuquAIbfIZv3OPgn1SK4IvbrqnjDL2u0mGcZwBXQ_EuNrbsYdtb5zII8rSwZPDtZ6ALlvBuzGvelo3FbP7cAktcU5cHBryB8kwzUZseok_sdn2WZelOpU6GZxO5KWopFC58NHJ4LcZJg9imMgf4St1orNgpCZ4pUQSJ7sURQ4iWEap-A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b19aa63524.mp4?token=sBcsgfIxDxEHhGXpaTgN3HyD09tJGWY6J5WwJ5gjJQfGB0MEwdTId83DbzZ45USsb8lR7Fd-7UzghuXox-8uPVyifk8dvwksK60tgmfJzJRIgtyVNyoPqWNWTsD5ZGgfC9OZThxrSObuek942lpuxeI0MDdIzSdROApOMMTuquAIbfIZv3OPgn1SK4IvbrqnjDL2u0mGcZwBXQ_EuNrbsYdtb5zII8rSwZPDtZ6ALlvBuzGvelo3FbP7cAktcU5cHBryB8kwzUZseok_sdn2WZelOpU6GZxO5KWopFC58NHJ4LcZJg9imMgf4St1orNgpCZ4pUQSJ7sURQ4iWEap-A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
🚨
⭕️
⭕️
⭕️
⭕️
گویا یه دونه موشک به پایگاه آمریکا تو اردن خورده
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/Futball180TV/105959" target="_blank">📅 01:08 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105958">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">🚨
🚨
🚨
🚨
⭕️
شلیک مداوم موشک‌ از مناطق مختلف ایران به سوی کشورهای عربی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/Futball180TV/105958" target="_blank">📅 01:03 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105957">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">🚨
🏆
ژوزه مورینیو: برنده توپ‌طلا؟ بنظرم کسی که یک فصل هیچ‌جامی نگرفته هم میتونه برنده بشه. نظرم بدون شک امباپه هست!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/Futball180TV/105957" target="_blank">📅 01:02 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105956">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8d6b878d2e.mp4?token=oVgfbiWXKH_anjTsHsTURhZa1J_Qp-p0E1WMtQzkGWqxI3qoU3NLKRlBTrA5amXPMKA9CLB3825zPxcq6iUuaSJs2omTyvUuodVTfegAvRXGA94_bIGxqBUb-Py7r6lHCpgN47lXSS8ls4Oj93T7XezcuwSVGZKCLkmwOv6gdoBUYDtilcG2PbkfjHzXD1hW6jjJms8nhYbKj36Tae5wz4l6CbgbvRWni90PrZl_hoq6whHRFRV8AL__VP_SxgKz4FU8fbQ1gDItxnKrwePdOVEwEAIJpeIdS8NnFgpmIMd9L8oXDmn2vguKKFKO3drTAws6scGNO-CVIpaek39NUQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8d6b878d2e.mp4?token=oVgfbiWXKH_anjTsHsTURhZa1J_Qp-p0E1WMtQzkGWqxI3qoU3NLKRlBTrA5amXPMKA9CLB3825zPxcq6iUuaSJs2omTyvUuodVTfegAvRXGA94_bIGxqBUb-Py7r6lHCpgN47lXSS8ls4Oj93T7XezcuwSVGZKCLkmwOv6gdoBUYDtilcG2PbkfjHzXD1hW6jjJms8nhYbKj36Tae5wz4l6CbgbvRWni90PrZl_hoq6whHRFRV8AL__VP_SxgKz4FU8fbQ1gDItxnKrwePdOVEwEAIJpeIdS8NnFgpmIMd9L8oXDmn2vguKKFKO3drTAws6scGNO-CVIpaek39NUQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
🚨
⭕️
شلیک مداوم موشک‌ از مناطق مختلف ایران
به سوی کشورهای عربی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/Futball180TV/105956" target="_blank">📅 01:01 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105955">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">🚨
🚨
⭕️
لحظاتی از شلیک موشک‌های ایران
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/Futball180TV/105955" target="_blank">📅 01:00 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105954">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/721dcb7629.mp4?token=ZVvq_Nme4gTbdX9x4aSdcqYT97wj00Q7eqHiewOUQNKW9F60RSIF2b1OBSu1eaNEaXhzB6kpVyhdOB6x85aazoCa98e0TdGL4_O3Iz_3whCOULXc7uzeGySAe0zOyxWcn4EfBRxd4ouiNtuXAe7X5ZoCNmBJKrQ7qxRGbFgWGxKOnV0C_WqYJHy--SkQdV0JQKVCGll8SsHaJf87nbaqPxGeTJvAp3OIR8q3tkz9k5AfIwaaBdyI0Vj6MNxpGbYLL3U0MCLYkyLBXkLQtRYWqmiN7LJuNpUC1ScPz7ohuGkfU0vlatQiIB9E2q9beIOdRWMGJ7j6XPtzB1_Q3ashnQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/721dcb7629.mp4?token=ZVvq_Nme4gTbdX9x4aSdcqYT97wj00Q7eqHiewOUQNKW9F60RSIF2b1OBSu1eaNEaXhzB6kpVyhdOB6x85aazoCa98e0TdGL4_O3Iz_3whCOULXc7uzeGySAe0zOyxWcn4EfBRxd4ouiNtuXAe7X5ZoCNmBJKrQ7qxRGbFgWGxKOnV0C_WqYJHy--SkQdV0JQKVCGll8SsHaJf87nbaqPxGeTJvAp3OIR8q3tkz9k5AfIwaaBdyI0Vj6MNxpGbYLL3U0MCLYkyLBXkLQtRYWqmiN7LJuNpUC1ScPz7ohuGkfU0vlatQiIB9E2q9beIOdRWMGJ7j6XPtzB1_Q3ashnQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
⭕️
لحظاتی از شلیک موشک‌های ایران
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/Futball180TV/105954" target="_blank">📅 00:59 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105953">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">🚨
🚨
🚨
🚨
⭕️
📰
صداوسیما: دقایقی‌پیش ارتش آمریکا به یک شناور تجاری در نزدیکی جاسک حمله کرد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/Futball180TV/105953" target="_blank">📅 00:56 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105952">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eSgICVKToHSbQrAYSPoTxBEMxh3Q5PgskxJ4LTkwdSeN3brdONqnDCH8GAcct9e0yvEuBNke355nBaynIeDKgC2OvQawg0lMowYJJ-TUZty7NN5JAEA5BogSwIH5_HHozYWYLGD13bRRbj2k9DG1DDi-_FThEDrVJktqbDBi28HB4qWTt9Xlag-1gN2aHHKp319yP-IfR9dGlLQf7yuEVw3fqNwKqYbZhQi5opAEz1Wh9KeYiYgyGrrVRxxw_U0HbS-kDEPSe0fGejabrO3fOXdEZS4lfBIKrUWn3p28VGJNoqDCIksHmLNAgXNos5nJNFaKyWe5f5jjbgdhgpe4jA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
موشک‌های سپاه به سوی بحرین و کویت
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/Futball180TV/105952" target="_blank">📅 00:54 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105951">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pO9t9jPtBQlhpK6breBoWc9U_l3R0WMVqgV4cRpTUJTPywZ0lRwO1FHzomJCMVR0D1zKtLW3drS6c-gm6eo20w_CoxIsocoGagC7Z0qBd5cfYBEQ7C4Q4ZGMizD0NDBu2tS4DH_OYwbpywepTijIto0rcIzELHihSY0-sAvlWvYlSDEXngVyHDlkDIbUeTmcgXcHcL1r31Sm5t6YaYpqUPX9qhJv_uFXy9_thAjqD54qkBnZoNtWZ6Wy357biyybeoW4MfZqeoI86dqrY2g0E3XSlJheny2yLakv0E6ZACEwQsOLblyeInup1VenRvfWzO23ljwZIWEE2k4hg5N2Sg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🚨
⭕️
گزارش‌ها از شلیک موشک از مناطق مرکزی ایران به سوی اهدافی در خلیج‌فارس
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/Futball180TV/105951" target="_blank">📅 00:53 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105950">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">🚨
🚨
🚨
🚨
⭕️
گزارش‌ها از شلیک موشک از مناطق مرکزی ایران به سوی اهدافی در خلیج‌فارس
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/Futball180TV/105950" target="_blank">📅 00:51 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105949">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Pfhv1Py-LNEAq2rh7EqGM_2YDoZhmM6IszXu1y8JrDx4xk1gSwS2tKtBvSxG_7ULYownNq5BPxfHW4K-qLodZt5-66vyStWg6hjTOgHAKDrDKTwzXqwWblenJqi4ais1mCGE8bKIEe-tHJlwodjCzAzhsockYry1saK28Y2_FtfB9r5vS8Wls7iBkGZ9eoTwXbfc_J2WEhQYUPn5KtT6-ZS-QRSXWvLrNCHkg9oeoaAm1Mm2FliU251ek_Rv7SOygjOUy4P33cy7ssDIb7C7xcjrMSDES_E3ltnFPg7wzLawCJDiv1AI1kBBhSqmH2iHrpFyuBT7BaEe_Rv3-XZXmQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
⏸
🇮🇹
🇪🇸
هایلایت بازی جذاب و تماشایی رئال مادرید مقابل اینتر با گزارش ابوالفضل عامری
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/Futball180TV/105949" target="_blank">📅 00:50 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105948">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CXHlPHGcGY5XMm8GK0f8i38tJCZbmJlcSZ0hULWTNhjAhVzd0febTNvVTX9VXvOnntHt-11ODDdvCsXvurOrdnhzW8yxN4wxmwXld5gqd1niEy5IZWOULXCPbGpdANjjOoZ1MdkAAjmCTBDBGWrz3UmMiyYi0WTNkyt_o-x8YMvNf6xAQXtPb13qDtDhxHTR0fULXzgXKHUwArh_FgLPtSeZ7kIzvIaF-hqpvIG--tU8w6ou7d4WSyCTdl4SoKBNXtCMsqvPso3iXl3b9GJ3gkWDLSEtomVdDYVMlEQhpYDMMaarv4lcnLLDM8lijt1Gm8jdXt-1U3SzzreQEMLFSA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🥶
🇪🇺
📊
ارلینگ‌هالند در لیگ‌قهرمانان اروپا:
‏59 بازی
؛
‏59 گل.
👀
🐐
اسطوره، لیونل مسی، برای رسیدن به 60 گل در لیگ قهرمانان اروپا به 80 مسابقه نیاز داشت.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/Futball180TV/105948" target="_blank">📅 00:38 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105947">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">🚨
⏸
🇮🇹
🇪🇸
هایلایت بازی جذاب و تماشایی رئال مادرید مقابل اینتر با گزارش ابوالفضل عامری
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/Futball180TV/105947" target="_blank">📅 00:37 · 18 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>

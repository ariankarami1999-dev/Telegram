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
<img src="https://cdn5.telesco.pe/file/s_4NxRMfBBVDCCKRNPKIRT2Jss9VcKfcbnKChn_DvLTOfega6QPjOA5tatf_y33h0kemTvJMQeACEoAXay5vMAK_N9fLHjC1BEpokfHb0E9uAy6MVOmaewUltSdWed2TrIVbs-Zamjgtw1WLIwMtGwUE6kDeYBkK7abf48CopMHwdUR-b8VCdsQAGNHrGaspOyd64i6PupnrgELPtystIAVdqLkOSWh4CtAhPDwWddduW7-SwCbXaB5-Nd8osSlC07mVsCG-NhmsbqNDCMO0zCGpFzn0Q6E5oi0fTMPjN5tlzIL9ObihCsCypsBfRaV3WJmoioG97Uk7SKWdSl0QAQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 فوتبال 180</h1>
<p>@Futball180TV • 👥 393K عضو</p>
<a href="https://t.me/Futball180TV" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 In the name of God; The only popular sports channel on Telegram: All for Iran...🖤We respect the copyright laws and follow the laws, Mr.@Durov...🙏🌹Contact ads:@TivaAds</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-07-10 23:31:10</div>
<hr>

<div class="tg-post" id="msg-107712">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">سوپرگل اولیسهههههههههه</div>
<div class="tg-footer">👁️ 486 · <a href="https://t.me/Futball180TV/107712" target="_blank">📅 23:30 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107711">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">فرانسهههههه زددددددد</div>
<div class="tg-footer">👁️ 969 · <a href="https://t.me/Futball180TV/107711" target="_blank">📅 23:30 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107710">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">گلگلگلگگلگلگلگلگل</div>
<div class="tg-footer">👁️ 635 · <a href="https://t.me/Futball180TV/107710" target="_blank">📅 23:30 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107709">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e970c7c18a.mp4?token=CpaGgfe5HRbnIC0O-Q7Qn8W3rXQCDlcLljLNWyW6-prxVndrX_lZ7b-GHt1x70mnyVWpDTIYT5k-CBJlFH0D3J3IIMGfmY5x_uVDPrIDfTvXBM1Z9UN4EBX7zPmGWFczRubS4Y-vJFNvsL1CZFM1mrQCTn-HYQjBDDd99qx3EQuVlcT8fznNfUFP-hT_cG28FWp70ZbliTPVVhOHn9mDOkJrbCOXdTySBLKYht2keTzpZdqQasMvmx7EtJMZ2_0oAGhiI1l2-QhFkdUun61JZgod3IpGo6bzpIiD_6VhFLPGzVhPUNvsn5gsltXjRlQKVUWWrWe5Y20QLrNDWx5zIg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e970c7c18a.mp4?token=CpaGgfe5HRbnIC0O-Q7Qn8W3rXQCDlcLljLNWyW6-prxVndrX_lZ7b-GHt1x70mnyVWpDTIYT5k-CBJlFH0D3J3IIMGfmY5x_uVDPrIDfTvXBM1Z9UN4EBX7zPmGWFczRubS4Y-vJFNvsL1CZFM1mrQCTn-HYQjBDDd99qx3EQuVlcT8fznNfUFP-hT_cG28FWp70ZbliTPVVhOHn9mDOkJrbCOXdTySBLKYht2keTzpZdqQasMvmx7EtJMZ2_0oAGhiI1l2-QhFkdUun61JZgod3IpGo6bzpIiD_6VhFLPGzVhPUNvsn5gsltXjRlQKVUWWrWe5Y20QLrNDWx5zIg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
استقبال بی نظیر و خوش آمدگویی هواداران به زین الدین زیدان سرمربی جدید فرانسه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.51K · <a href="https://t.me/Futball180TV/107709" target="_blank">📅 22:53 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107708">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b0312a011f.mp4?token=EVRLc4pYg4QhRW4nzaIZ-Z0ncs5jP4-cyfc3AFum2_gmPc1nN117M6cL4EiIrnYNjymfM1aFT-x6krZydZ1cPREdjnVr7_PM2zGjcDr-b2G014LaV5H3FroUU6bfFnkrqr5mKCJiGT5ivtaI9K_L6iCAEBINHaGRw7sxYoRwd95hQ78jG91Nb-isLdszrQiIfaxs3dqkg2TC1kNreHQ2YgqCH-Gskp3zBGlCtgYSCOfO5iYeylFAkDujhdZiXv_7xPJqsdfCxykX5MdF5T4JK2-szBetXhgb1BVdOGFl1cmj4JEVTDwTMGsqq6aVkty6niPAESNOqJ96_DxkJK_0dA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b0312a011f.mp4?token=EVRLc4pYg4QhRW4nzaIZ-Z0ncs5jP4-cyfc3AFum2_gmPc1nN117M6cL4EiIrnYNjymfM1aFT-x6krZydZ1cPREdjnVr7_PM2zGjcDr-b2G014LaV5H3FroUU6bfFnkrqr5mKCJiGT5ivtaI9K_L6iCAEBINHaGRw7sxYoRwd95hQ78jG91Nb-isLdszrQiIfaxs3dqkg2TC1kNreHQ2YgqCH-Gskp3zBGlCtgYSCOfO5iYeylFAkDujhdZiXv_7xPJqsdfCxykX5MdF5T4JK2-szBetXhgb1BVdOGFl1cmj4JEVTDwTMGsqq6aVkty6niPAESNOqJ96_DxkJK_0dA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✔️
گل‌اول بلژیک به ترکیه توسط کوین دیبروینه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 6.01K · <a href="https://t.me/Futball180TV/107708" target="_blank">📅 22:36 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107707">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5f5c780577.mp4?token=p2MBKBWFtGJr4rKGgpIbDU3W00ux80D3mMGdvA-CRXoO68TSsv2IrLsTz941pYjEFs2sGsEllpNve8O8WlvgE93j3dAnzApFHy8bFz_0cuHv9isWN2W63BcT1a3e4PncBDs_rRL-m1AQOvY7znPEeLcYqxJy-a4Gp8OmrtfIsoXWJ3h_cLwi5-KM4RQyhkPujDEiJjGGkdyUMWmiafFUSI2OOn1bPZOxH2A8sizXU_qaOi5WXd4kX1O4m1AIj_BO7oF3M1KfbldW93Sk7ACUjq48UvRPpmnG-mC3GX5dvuc8cGZqqI29FkUug2OuPUHxHAtyMxO4jY3ptU3z1X0gPg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5f5c780577.mp4?token=p2MBKBWFtGJr4rKGgpIbDU3W00ux80D3mMGdvA-CRXoO68TSsv2IrLsTz941pYjEFs2sGsEllpNve8O8WlvgE93j3dAnzApFHy8bFz_0cuHv9isWN2W63BcT1a3e4PncBDs_rRL-m1AQOvY7znPEeLcYqxJy-a4Gp8OmrtfIsoXWJ3h_cLwi5-KM4RQyhkPujDEiJjGGkdyUMWmiafFUSI2OOn1bPZOxH2A8sizXU_qaOi5WXd4kX1O4m1AIj_BO7oF3M1KfbldW93Sk7ACUjq48UvRPpmnG-mC3GX5dvuc8cGZqqI29FkUug2OuPUHxHAtyMxO4jY3ptU3z1X0gPg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
❌
🇮🇷
علوی، سخنگوی فدراسیون فوتبال: استقلال قهرمان فصل گذشته نشده و بحث جدیدی درمورد اهدای جام به این تیم نیست
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 7.65K · <a href="https://t.me/Futball180TV/107707" target="_blank">📅 22:18 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107706">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3539953949.mp4?token=miVeijKmFQ0QfVhGpiywx5SAbteSHXz2bJSpBsMAuAYOz1ToYxDOlJ1Eg0SFon5m1XuMEDAWojeyiO0Pb7uNZ1ROfL71cDCeZB5sNDEDTpBKOLwZln_Mj5hgf_8soR4eawC0eqQatV9vCIiC9NgExEBJcjzHCnzhvJX_sieiu1OQE9SO3C0joHbohN1pnzngqgvOEzz5VCuPcYjOcSSt5B__iuF_TlEZatShcb9i3zeTyt3OXlAQfYz2EBmDB_OJ9WhrlPNxZGIr7WLgiiT5fmA0nxFKD5WBljlTJteXZd0ZqJCJKmfPlx1Ax0kzFUnkaLpMzkMf8TuuYl2Fk87SbA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3539953949.mp4?token=miVeijKmFQ0QfVhGpiywx5SAbteSHXz2bJSpBsMAuAYOz1ToYxDOlJ1Eg0SFon5m1XuMEDAWojeyiO0Pb7uNZ1ROfL71cDCeZB5sNDEDTpBKOLwZln_Mj5hgf_8soR4eawC0eqQatV9vCIiC9NgExEBJcjzHCnzhvJX_sieiu1OQE9SO3C0joHbohN1pnzngqgvOEzz5VCuPcYjOcSSt5B__iuF_TlEZatShcb9i3zeTyt3OXlAQfYz2EBmDB_OJ9WhrlPNxZGIr7WLgiiT5fmA0nxFKD5WBljlTJteXZd0ZqJCJKmfPlx1Ax0kzFUnkaLpMzkMf8TuuYl2Fk87SbA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
حاج صفی: می گویند آقای قلعه نویی با یک نفر(جواد نکونام) مشکل دارد که من را به تیم ملی دعوت کند تا رکورد آن فرد را بزنم!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/Futball180TV/107706" target="_blank">📅 21:29 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107705">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MwZRG8zF1oniTox5YS6ddBv-dAxjtG2JWFJhYFxHPdc0wJrXvxAILEQ6CVmcgb5VSjGms3rZqCOCAZSdT-jtQh1pcbEGKyiE01ggMNy-bKJma69LJRpCen-DeScFF_VgzFvYCFE9ZqCkBPnUirZp-6VAgRxui6EHKrO5hVzEI8jqUC3to3CBpSJq_7SnykM2EEwcAdtZNUaUFG6G5Hw-7r3Lk7nm3tJz7V6l572jkcCiifgneiEKF1awYrl47ZON8CINMnFXtxBlqfPy9kPDdlPaU841C-1jba-MCAGhOxGepJXhCgdISxJahbRRtn1jTNGCO9-cym4sItbDwxXpUw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇫🇷
ترکیب تیم‌ملی فرانسه مقابل ایتالیا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/Futball180TV/107705" target="_blank">📅 21:19 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107704">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XSC3npYH2gIxI4oo7kKkLPZZm1b4gRrDSjgRW2LW7_iyld9M9GAgXna3t0umfAG3WJUGX-OcNQC5s4Pha2lXh5iMaLEbKHiojasuIfd0iX5FylTbg89Y4cUej5j6-mNFFhXAwbcL9soNBDO6JPqa8m3uRJTR3gtPWfM1Azl-mC-Dp6iDQ3zdKQw93refL1bFu1GTXTsCJHUAXL2KPKghcf1VIPmL_IyNwlfWNvFDY6h2fTUraXnCo5V2O_wlVwSPK93Z3dWarL8oj5DyinS78jj9UYyMafquSr15AFkJpUVhLtY5vLyLRL3u9rn5S_NIO0fm-jitKAZ0J3EgSph77w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
👀
پیش‌بینی‌های زلاتان از برخی نتایج فصل:
🏴󠁧󠁢󠁥󠁮󠁧󠁿
🏴󠁧󠁢󠁥󠁮󠁧󠁿
لیگ برتر انگلیس؟ منچستر سیتی.
🇪🇸
🇪🇸
لیگ اسپانیا؟ بارسلونا.
🇪🇺
🇪🇸
لیگ قهرمانان اروپا؟ بارسلونا.
🏆
توپ طلایی؟ لامین یامال.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/Futball180TV/107704" target="_blank">📅 20:45 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107703">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/g66l6F_BRTfV0kWeyGLkd_YGN29Tq0JxTBG-whT3fIDboOXJOPcsAM4APGV1N8EtnG8EqGh7EZ1BnjWplrQNwH3gRwZPsXtaYAPzjT7HWlhgLHETjvaFrJaklu6AMu3c0NxARt8w2x2g28ESDsTwfYCcHzFIN_fkuhdf-tDTwkNytTOesLM7bz-TLWHMh7QPxExmM5WExAlU4bCAlN0o7S86kB4Bx8Zmm3azD5RPcpoqnnAYYhihF1fxXuHUeGeImBpPvjOhWwGzRTnfuLw_U21d8sVAmlKexG6ujErpxFNqzXj_hhPkIsRxtJAJ8fA1reEAyLIwtxc3xLjkRTPQlA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇫🇷
ترکیب تیم‌ملی فرانسه مقابل ایتالیا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/Futball180TV/107703" target="_blank">📅 20:32 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107702">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PIIkAOZPibSGolrJoYll06VE-5m5YC4N5CHT5rZ0VFjj0aPlFv1oIJ5Y9NvZGQBhrxye6U0Gk-sbFbjETK-AHvIiq3yYpZLnmIA8a0EsfvYIW2zJbvpT64mfkLDIwQ1MGVXOJkOxUWvdIX41MzxTQJMhSXyHQByyJscmezAlkckBsQzgQuxcdTcP2FISbCwErn5vQlaLYxGc3E97w_DEBvd748F8dLx3xPLyrmIDYc5efbmA5meVzyEI9DvdoHQp_bwWpUxbqM2YhJIZOH5IjwUJb6KLjmlzTIZiBuvNYd1T88oluIDh4n1ejEUPXuVOyoycxavwCOpfMld4hnFXNQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
📱
نشریه The Athletic
در فصل 2017/18، گواردیولا اولین عنوان قهرمانی لیگ را با منچسترسیتی به دست آورد.
منچسترسیتی حدود 100 میلیون پوند قوانین مالی (PSR) را نقض کرده است.
🤯
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/Futball180TV/107702" target="_blank">📅 20:24 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107701">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/af474384fb.mp4?token=MsABaXiz3p82d786M6rbiFa87cW4BpTj9Tr8nvlmecZAla2Nf2Oo9-0RKavsGn7X4_DpztVKxYDRdhxfpc1p1KnBhc-s-T5vXaHfiO6GFZI0NkIprPCmFBQaaUcUpKsxzEDaN229Nav3MAepwrrVfuzyBeY5zm7lSK_G3KJ8BZnA1V0WbC1gmRxtBZ4layhWc60Zzc_lpgsFz9mxwIsHakoAAoCF1SEeqdS-EyiqIQeMDfhhF-vmb_0QWrpHJbuqjg48141MFCn5jb4I0i-_JOuf7amXnIsKowxYoR-ZMgWl6Av5W0WBXZ2x67WnB8prx5vvULFT9HBKpxXSXWl35Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/af474384fb.mp4?token=MsABaXiz3p82d786M6rbiFa87cW4BpTj9Tr8nvlmecZAla2Nf2Oo9-0RKavsGn7X4_DpztVKxYDRdhxfpc1p1KnBhc-s-T5vXaHfiO6GFZI0NkIprPCmFBQaaUcUpKsxzEDaN229Nav3MAepwrrVfuzyBeY5zm7lSK_G3KJ8BZnA1V0WbC1gmRxtBZ4layhWc60Zzc_lpgsFz9mxwIsHakoAAoCF1SEeqdS-EyiqIQeMDfhhF-vmb_0QWrpHJbuqjg48141MFCn5jb4I0i-_JOuf7amXnIsKowxYoR-ZMgWl6Av5W0WBXZ2x67WnB8prx5vvULFT9HBKpxXSXWl35Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🎙
⚠️
رضا علیپور، نایب‌قهرمان سنگ‌نوردی بازی‌های آسیایی ۲۰۲۶ ناگویا، با انتشار ویدیویی در اینستاگرام، به پخش نشدن مسابقاتش از صدا و سیما اعتراض کرد: «همه مسابقات را صدا و سیما نشان می‌دهد؛ سکو، فینال، چه برده، چه بازنده، اما به ما که می‌رسد،‌ نشان نمی‌دهد. قضاوت با خودتان.»
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/Futball180TV/107701" target="_blank">📅 20:19 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107700">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ad5607ff2b.mp4?token=KRYByLjpjlQqBda6EAzQ0N1Vqj7PUQYx5OD4bDyyNdNgs10yiC_rD6mwg8iAW_fe6vOTqxyhSQa9wT60GX3xSYHy9Vrg_Yn8uTjnZcnGgCglK3zdNzNVx6cjvhDGTTfjRPCoM3F_LUIdNSF4p811nbvnixFRKFZpc39WE-aWoRvnlmU3AF7vo1rKtTQcr32swMkwdftyJYdoluMylf44ksxP50mVwsCw3TxCL12rIjMl-ySgk31idYh9iOmmT2QcgycA5w250rkAUGuqSz0h9-XzvqKxfc1ZHeWyaGBFqnb-Y4yYHQXrnIcrkNg08nSrF1nSSseQWColrqD-AHClaA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ad5607ff2b.mp4?token=KRYByLjpjlQqBda6EAzQ0N1Vqj7PUQYx5OD4bDyyNdNgs10yiC_rD6mwg8iAW_fe6vOTqxyhSQa9wT60GX3xSYHy9Vrg_Yn8uTjnZcnGgCglK3zdNzNVx6cjvhDGTTfjRPCoM3F_LUIdNSF4p811nbvnixFRKFZpc39WE-aWoRvnlmU3AF7vo1rKtTQcr32swMkwdftyJYdoluMylf44ksxP50mVwsCw3TxCL12rIjMl-ySgk31idYh9iOmmT2QcgycA5w250rkAUGuqSz0h9-XzvqKxfc1ZHeWyaGBFqnb-Y4yYHQXrnIcrkNg08nSrF1nSSseQWColrqD-AHClaA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
🎙
حاج‌صفی: در کار آقای قلعه‌نویی و کادر فنی تیم ملی اصلا دخالتی نمی کنیم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/Futball180TV/107700" target="_blank">📅 20:13 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107699">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f60d798d01.mp4?token=aY72Dav1RaRLw36dcegy17KCH6ADMiLj5K7xqJbAJn1uKdRRVylpydzb_xCIq9Lpf0Lyri5ImHROHLAecCB-VReLBaZ739IVP5HYzJH1qJgoxpePTc5u5RhUf6zftIA8pw_1RYcmp0l3l3jjxD1DDJLsuslWtFFBx7H1jJT--OqjAQ35bU9VHaBXLZmq23jGvFIkkLa1pCFle6-ysnMiIAKKskCls_jYtY-KnrIL_fFl2PRoo-s9A6fTfdfFzKsb3FaD8HbBuVexDTp7LTlvwkap_M_-t0XSWuYJ4yBhoU6HPOxP4t9ZpZhgy0VM82bmnnLe2ez7hs5tKReiHbcJBA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f60d798d01.mp4?token=aY72Dav1RaRLw36dcegy17KCH6ADMiLj5K7xqJbAJn1uKdRRVylpydzb_xCIq9Lpf0Lyri5ImHROHLAecCB-VReLBaZ739IVP5HYzJH1qJgoxpePTc5u5RhUf6zftIA8pw_1RYcmp0l3l3jjxD1DDJLsuslWtFFBx7H1jJT--OqjAQ35bU9VHaBXLZmq23jGvFIkkLa1pCFle6-ysnMiIAKKskCls_jYtY-KnrIL_fFl2PRoo-s9A6fTfdfFzKsb3FaD8HbBuVexDTp7LTlvwkap_M_-t0XSWuYJ4yBhoU6HPOxP4t9ZpZhgy0VM82bmnnLe2ez7hs5tKReiHbcJBA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
⚠️
درآمد ۲۰۰ میلیاردی مهدی شجاری مالک موبو نیوز
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/Futball180TV/107699" target="_blank">📅 20:04 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107698">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8956163759.mp4?token=Lcl5BurxCXGgJC1eDzoXN6IZcr_qgHvtuxjfkk4FXnnFKe-1wPHYkR9oSw4o83wjGugvUtVQXyPoL-zBdSVh3iDpfzqaLhl_J7ZqOEoDWTQMiYsgL_H3QvYwlMlkmIIweRLWdVpmW4ZyVFUVoRC1X7TDvOFP0xzlC2l_OqPaAdh-__b1AlAlOZbNVXn3txAieTd_HZ9MG0s4na-feNKm1Y60DcGPek2oXZ-9Wr4L4oZPIiqdsqsJrq1tP2PHZvK8z20wWqdRsmgPcOXTLOfZ23dH0GhvxjHIEzC_sIsE_9-GhJIoU0r8InM0dfQBSLwO3-cq6vqC3q7KXFSEdm4wQA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8956163759.mp4?token=Lcl5BurxCXGgJC1eDzoXN6IZcr_qgHvtuxjfkk4FXnnFKe-1wPHYkR9oSw4o83wjGugvUtVQXyPoL-zBdSVh3iDpfzqaLhl_J7ZqOEoDWTQMiYsgL_H3QvYwlMlkmIIweRLWdVpmW4ZyVFUVoRC1X7TDvOFP0xzlC2l_OqPaAdh-__b1AlAlOZbNVXn3txAieTd_HZ9MG0s4na-feNKm1Y60DcGPek2oXZ-9Wr4L4oZPIiqdsqsJrq1tP2PHZvK8z20wWqdRsmgPcOXTLOfZ23dH0GhvxjHIEzC_sIsE_9-GhJIoU0r8InM0dfQBSLwO3-cq6vqC3q7KXFSEdm4wQA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🤡
کیف کوک ژسوس بعد جدایی رونالدو از پرتغال
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/Futball180TV/107698" target="_blank">📅 19:33 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107697">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/263935f09a.mp4?token=Glf7Ju4GgiI4yxhrQjkXcor3XzSm_bLDjHFBKGgnFsboj7kqjlKUamqSaZECI7kFJB4HxOKhC2ZV2Ine2PkHz7M229nOSpdH7KBmcp7maAnaFaGQVbdw3AZw64Lvs1JM7O9rUvVYxxtmiNjxREf-WIRZEyvPEMmmCrPz-lVkNkCFMt9s4MKf5BYUxnkE07yDyrl2ZjI7Hb1EE_fMm80SzGeEoW0cgPR-TrlfO1XIrGkTeuUCK75IVueE2gb1UEfJhUommOtVUhWAd7RFkZAsZukB6j9CFWbg0EzpwOnU3DT7kq9HKsS0vVanp3depDbKCa67yMf9JJci1Pq1PQCEmw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/263935f09a.mp4?token=Glf7Ju4GgiI4yxhrQjkXcor3XzSm_bLDjHFBKGgnFsboj7kqjlKUamqSaZECI7kFJB4HxOKhC2ZV2Ine2PkHz7M229nOSpdH7KBmcp7maAnaFaGQVbdw3AZw64Lvs1JM7O9rUvVYxxtmiNjxREf-WIRZEyvPEMmmCrPz-lVkNkCFMt9s4MKf5BYUxnkE07yDyrl2ZjI7Hb1EE_fMm80SzGeEoW0cgPR-TrlfO1XIrGkTeuUCK75IVueE2gb1UEfJhUommOtVUhWAd7RFkZAsZukB6j9CFWbg0EzpwOnU3DT7kq9HKsS0vVanp3depDbKCa67yMf9JJci1Pq1PQCEmw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
انتقادات از صحبت‌های عجیب احسان حدادی رئیس فدراسیون دوومیدانی جمهوری اسلامی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/Futball180TV/107697" target="_blank">📅 19:03 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107696">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f9a8b7a5dd.mp4?token=MbJGRKSnvbtGr-lSHv0z-ArPaje0XcXRWHF3HbDftE06ljQJjKxbxCEOl7HtsADH4dsGkSVYc0fzCogcVcqC5zy4N76sXRCWFXdXE_rGkpOezcPaUiTtwTrHuYCsZuKHT5BlXlExm_PH1YV9WvmvPZ-UicBIKPqrCZYD1SIQBBKFwjPeK8xDYwOvGISCDVKXZWHhV4jhEkOxOIFqnSxq1QCgFGhnWQhSVuUjV3Zx-b7IWLaezDZMY3ewkq3gCevPY502Te7iG57fSnRKOfugcb1Pt-BQrmBBysHP_Nc3kOtBWYzdVjUhjl_SA-bxIKfIb-cfXs3vuaK-7yqLWHQk5w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f9a8b7a5dd.mp4?token=MbJGRKSnvbtGr-lSHv0z-ArPaje0XcXRWHF3HbDftE06ljQJjKxbxCEOl7HtsADH4dsGkSVYc0fzCogcVcqC5zy4N76sXRCWFXdXE_rGkpOezcPaUiTtwTrHuYCsZuKHT5BlXlExm_PH1YV9WvmvPZ-UicBIKPqrCZYD1SIQBBKFwjPeK8xDYwOvGISCDVKXZWHhV4jhEkOxOIFqnSxq1QCgFGhnWQhSVuUjV3Zx-b7IWLaezDZMY3ewkq3gCevPY502Te7iG57fSnRKOfugcb1Pt-BQrmBBysHP_Nc3kOtBWYzdVjUhjl_SA-bxIKfIb-cfXs3vuaK-7yqLWHQk5w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🤯
✅
کیفیت تصویربرداری با آیفون 18 و یک سوپر دوربین فوق‌العاده از سونی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/Futball180TV/107696" target="_blank">📅 18:35 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107695">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kX-45bSnKkd9vgsgoyTNzegGHLPoz0OAs8qRd-WFSNVOErUJvciuPAAzc48z-y5IJQK8L4MnYemAuSm0-rU-ero5e26pT5QYJEG1aTQiI1i-PJLobV5l5UoVymN1-Obi9r1cz46fNvRV_vWqbN5VQFJsPiUDBAB5kSNa6GrARrCWLg2CutewfCVpE9xnNcLYES0986qJR8QwC1ZDi1lCJvKj0MBDNiZNmYoRCObsnx4pGw3SL1Lncbh8DyrSrsyQQycibG2ZEM79V5ySsDHbngvbcopVtjvk94JvGsRQ1Cr6ngrEgPgaFEhO_zSzMziJiFrZNLjmyXwQphtp_5W4ow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
✔️
پرسپولیس در دیدار تدارکاتی مقابل گل‌گهر سیرجان با گل‌های محبی و محمدحسین صادقی به برتری رسید
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/Futball180TV/107695" target="_blank">📅 18:00 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107694">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qhA3ezB-uT2kQBqaLX5IrP_iXPv0C4HWK_vUGpPfnVaL4Ezf1GbJuYXoXU2q7aiJ4sun5Ne3TZJYLEmlONSFxcoxa-gNRpa3VH7gNB0XBtxaeCA8HbCF-0lH9yUUqIJvEpuwtstpyw-LkfdfW0fIVIWDDV51QIXMP8Fh1HFQuFYCgTZHq7z90yBJMgOOAnXrJXAMCFOlbzppsV-pd1S1g4pfLTxh7inyRT5f5iKXl12jF56j7OnDBJURGp55822fBlvx786lEDZXnLadkb5qWhRp76bIpc9h86w0saxua0bAlfWM6Mc-Xd-dyKzLDuApwejvicqthsDTGjQ0kt1NjA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇮🇹
یوونتوس قصد دارد تابستان آینده به عنوان بازیکن آزاد با ویرجیل‌فن‌دایک قرارداد ببندد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/Futball180TV/107694" target="_blank">📅 17:38 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107693">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/507dbd5bf2.mp4?token=kJ_SB-R-g7x3d8WG1z1Q-kK5DUe1JZOsD8VtyUtl56c9O52Gt0DeI0IokZLfluRM4YMVRs6ikfnvl-nk9OIvkhCq0cK39q8uiofMecT5PgqJDWo7xeqi_2fhGtUar1hqbeodfStUfCgIkN6NT9iJb3YR1WJWYixE8wZi0KrWI7W47GBjGAe3aBJbntd0r30JX8cZvi0XCAF9wixW9JtrbEgQok_04w21b0geBcXEychxQR8tYKu6igBdR9eBaw8TakqlrKGnbjK0h10VZvcRarnNdUWblUP43wqKc4ma18bnkdail5eBsOfmNcw51mke7ZnAUfrc9Rz0yOOhT_u3bA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/507dbd5bf2.mp4?token=kJ_SB-R-g7x3d8WG1z1Q-kK5DUe1JZOsD8VtyUtl56c9O52Gt0DeI0IokZLfluRM4YMVRs6ikfnvl-nk9OIvkhCq0cK39q8uiofMecT5PgqJDWo7xeqi_2fhGtUar1hqbeodfStUfCgIkN6NT9iJb3YR1WJWYixE8wZi0KrWI7W47GBjGAe3aBJbntd0r30JX8cZvi0XCAF9wixW9JtrbEgQok_04w21b0geBcXEychxQR8tYKu6igBdR9eBaw8TakqlrKGnbjK0h10VZvcRarnNdUWblUP43wqKc4ma18bnkdail5eBsOfmNcw51mke7ZnAUfrc9Rz0yOOhT_u3bA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🎙
امیرحسین صادقی: علی منصوریان بهم گفت چون شبیه نیکبختی، یا باید زن بگیری یا نمیذارم فوتبال بازی کنی! با حاج محمود سفت وایسادن تا زن بگیرم حتی شاهد عقدم بودن که خیالشون راحت شه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/Futball180TV/107693" target="_blank">📅 17:35 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107692">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/Futball180TV/107692" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/Futball180TV/107692" target="_blank">📅 17:35 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107691">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Pp7JQR8-HXw3yRthlOu0sVZPr97nS7ndff9q3f9d7BZcMPnp4Uztn75bWGgHYnrqUii-KYTKQZ7wWmptwpQ3aC3YoiI_amtfS-MHK9hICr-VhHxeoiDOypIiWj1WtcphdOBOGM3ndC9q8jfHpTEWc0M7VJ_7ALkMI7YzGOg6mHHQnszA2jYQ4cvpkS37_mYo7Km8FJkaM3onVg7nQx5bEFtJARrOI4V9iDhBISgSUS4pZKD5dk0F5KxMigTg78dikTMnyoc-SD9AiqnxeRnkiX1Xo_LP37w6knhzYflj6PcO_9qTI4xL5zOUcV6XyOjqMTiAwHHgRdV4tvRuJF86gw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🤩
نبرد هیجان انگیز ایتالیا
🆚
فرانسه
را در
TrexBet
پیش‌بینی کنید!
📉
نگاهی به آمار ۵ بازی اخیر دو تیم:
ایتالیا: ۳ برد، ۱ تساوی، ۱ شکست و ۷ گل زده
فرانسه: ۳ برد، ۲ شکست و ۸ گل زده
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
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/Futball180TV/107691" target="_blank">📅 17:35 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107690">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/aa4517b308.mp4?token=GRk0f3bIMRhEdZZUSJdVhhKXsvCEU8YqrGAPROm49_ux-2obLm7GK4WJAt4uqFUnkqT2IQw77TIsuhY4m-I5Dprw8926sWdPAfxI8_I55aTaCBv9ERqmNODmc1sV6kddnz2GCbSjEOMN4h87x4HHTMNuZKyKhm7h4CMaK9XrpuEpscbyNZyHV7zxv5pTaJOa51wiSgGfHikiDxwYXB7wa4-GUmnoRsphhXCc7GdTVYW8tv6cUSh4kfIu0_-e7Cb3mxAMAFbsW8qmycKnnG2_5A_I7fgYf42U-YdWSgwmshgd0nKCxoTxqBpgV_4iN-zvuDJ1ApkekpKZpvehI1P5kQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aa4517b308.mp4?token=GRk0f3bIMRhEdZZUSJdVhhKXsvCEU8YqrGAPROm49_ux-2obLm7GK4WJAt4uqFUnkqT2IQw77TIsuhY4m-I5Dprw8926sWdPAfxI8_I55aTaCBv9ERqmNODmc1sV6kddnz2GCbSjEOMN4h87x4HHTMNuZKyKhm7h4CMaK9XrpuEpscbyNZyHV7zxv5pTaJOa51wiSgGfHikiDxwYXB7wa4-GUmnoRsphhXCc7GdTVYW8tv6cUSh4kfIu0_-e7Cb3mxAMAFbsW8qmycKnnG2_5A_I7fgYf42U-YdWSgwmshgd0nKCxoTxqBpgV_4iN-zvuDJ1ApkekpKZpvehI1P5kQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
⚠️
تعجب و عصبانیت قیاسی از قیمت دلار
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/Futball180TV/107690" target="_blank">📅 17:20 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107689">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fac9f22f0e.mp4?token=l6DxHWHd-9_1y18ku6rpYjajbZ2SvxJJ0llte8UB2gRg7-RZeOUb1vb0FceMorf49QG7PgP44tm82im2dqH87zzZLYwbZq68Vson8cUwNiuQzir54AeHLeVnCrp6GGzXv1alfyHJtt4f4SP987NO5UDY6gvg5Er9Mnf0wj7Z3slw1zKwnxhDUz6qo1LlTMfiLBCuIkcXz96D2M-ysyex-RUCRp-ZDwZgX5vaxJTto2L7rmsUG8s8SBu24oNoFpevFU4n3lFb3VP6P9RVdzP-BqVcNSpgYNHsRNKLexDawAh0HY6z8DTzmH1ljb7h2_x0rJBDqZz8UGvHEOJ1BzrFjg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fac9f22f0e.mp4?token=l6DxHWHd-9_1y18ku6rpYjajbZ2SvxJJ0llte8UB2gRg7-RZeOUb1vb0FceMorf49QG7PgP44tm82im2dqH87zzZLYwbZq68Vson8cUwNiuQzir54AeHLeVnCrp6GGzXv1alfyHJtt4f4SP987NO5UDY6gvg5Er9Mnf0wj7Z3slw1zKwnxhDUz6qo1LlTMfiLBCuIkcXz96D2M-ysyex-RUCRp-ZDwZgX5vaxJTto2L7rmsUG8s8SBu24oNoFpevFU4n3lFb3VP6P9RVdzP-BqVcNSpgYNHsRNKLexDawAh0HY6z8DTzmH1ljb7h2_x0rJBDqZz8UGvHEOJ1BzrFjg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🙂
امیرمحمد، خواننده آهنگ سنی نردن گوردوم رو بردن برنامه تلویزیونی ترکیه، اولش براش دست زدن و کلی تشویقش کردن،
ولی به آخرش که رسید دیگه نتونستن جلو خنده‌شون بگیرن و همه زدن زیر خنده :)))
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/Futball180TV/107689" target="_blank">📅 16:55 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107688">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0c643f6bb4.mp4?token=s94qVjOOUXGjy97inFM_YUwXwuniL-Cr0I6Q6rcslvChQarolXW1FRIqKdQ-fjYdaEPvStITWerJ2w3Ku_Cb6ZYRUooEjwNjn5_Ulf_nPOIfcrPW1E_FAnFaYuZHQ340_uxsFb_Ua1nkgm0QeLT2g04FoEkngtRKcxreAmH0LNbUIG5o8p6gdl9vYh6fPEpLWhVeq67jsBGVMm9KPww4NsnG8tj3ahfBvHP8XiSb3pcz4n8OlgxssZsQxOTb1CGpX1U1bQQNNageqK0diMKDz8xS5PMnVJVcSweSjieU4FgrxxVRY4MKqGyMEMHYZkBPWWqHlIyE2k7u939mFXk2fQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0c643f6bb4.mp4?token=s94qVjOOUXGjy97inFM_YUwXwuniL-Cr0I6Q6rcslvChQarolXW1FRIqKdQ-fjYdaEPvStITWerJ2w3Ku_Cb6ZYRUooEjwNjn5_Ulf_nPOIfcrPW1E_FAnFaYuZHQ340_uxsFb_Ua1nkgm0QeLT2g04FoEkngtRKcxreAmH0LNbUIG5o8p6gdl9vYh6fPEpLWhVeq67jsBGVMm9KPww4NsnG8tj3ahfBvHP8XiSb3pcz4n8OlgxssZsQxOTb1CGpX1U1bQQNNageqK0diMKDz8xS5PMnVJVcSweSjieU4FgrxxVRY4MKqGyMEMHYZkBPWWqHlIyE2k7u939mFXk2fQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
👀
خوانندگی فرزند محمد شریعتمداری وزیر اسبق کار و صمت و مدیرعامل هلدینگ‌خلیج‌فارس مالک باشگاه استقلال
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/Futball180TV/107688" target="_blank">📅 16:33 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107687">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ebc463f33d.mp4?token=saKFKfShaoquLMk5pXeTNXuxMLbD3jJ7ASiD9NjBeFsNNRPiuqnJ6clcvUl2mf1oMDHp9RHhuXYWoG30bZbWPHVX6uIBJzu-Hal2o4fuB0uyFjmmPn3M3PoMF2b_Mj_sMLDtHC0rX1LM7FPQikMTcfBv0x0LbJZ__rcWCaOxizkfo2EtGcoxSpW_mrcmFAWwRfGw3BmYQJqcSsCFV8beFaV0kiGaq8IZh2qX8yPyz_mTPksuN0RlvBWHeEuZszq_qrEbvgoQ7qv44nfaycYOB2C5s3G2vEKoz2p0rZmJ8XdxEY3lGpFkT7jEOj-cp3wdGna-su9pGREZtqN3pnxrwYkt7b0BYBP2dTwx9gqppDQAB8T7ptLjGuUgI6ocuqgzZQB6GtYctnnnhUj_JvRZkidzGKCWRt-JIS3Gy8d_WbVfiaaJbBWcbZxZ5s7s-LrpLACJm4x1F2DPz5O3LM1m6seTeKpnQM7f-3BrLrtDGvZep02vbvkLNllxY7_9ERBDkFBVRa9UxzqGWbh3z60VQAudJCb2A0-7fAxCYN5ftXIf_QJSVRz6EEzeoIgykjWuX5xgMPL8907Y639ERVlsVW2FI5INDvej9YfMzCn6EAxZadLeFw7-R3V4m9V9BvWfhHZWcMIO3rXSaQD4t1NKD59RvnQflp3VKQIEm8JmiiE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ebc463f33d.mp4?token=saKFKfShaoquLMk5pXeTNXuxMLbD3jJ7ASiD9NjBeFsNNRPiuqnJ6clcvUl2mf1oMDHp9RHhuXYWoG30bZbWPHVX6uIBJzu-Hal2o4fuB0uyFjmmPn3M3PoMF2b_Mj_sMLDtHC0rX1LM7FPQikMTcfBv0x0LbJZ__rcWCaOxizkfo2EtGcoxSpW_mrcmFAWwRfGw3BmYQJqcSsCFV8beFaV0kiGaq8IZh2qX8yPyz_mTPksuN0RlvBWHeEuZszq_qrEbvgoQ7qv44nfaycYOB2C5s3G2vEKoz2p0rZmJ8XdxEY3lGpFkT7jEOj-cp3wdGna-su9pGREZtqN3pnxrwYkt7b0BYBP2dTwx9gqppDQAB8T7ptLjGuUgI6ocuqgzZQB6GtYctnnnhUj_JvRZkidzGKCWRt-JIS3Gy8d_WbVfiaaJbBWcbZxZ5s7s-LrpLACJm4x1F2DPz5O3LM1m6seTeKpnQM7f-3BrLrtDGvZep02vbvkLNllxY7_9ERBDkFBVRa9UxzqGWbh3z60VQAudJCb2A0-7fAxCYN5ftXIf_QJSVRz6EEzeoIgykjWuX5xgMPL8907Y639ERVlsVW2FI5INDvej9YfMzCn6EAxZadLeFw7-R3V4m9V9BvWfhHZWcMIO3rXSaQD4t1NKD59RvnQflp3VKQIEm8JmiiE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇵🇹
یک‌دقیقه با اسطوره رونالدو در لباس پرتغال
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/Futball180TV/107687" target="_blank">📅 16:05 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107686">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/098c9ea234.mp4?token=Jx6Xg1rmF6PMFxM2yeix1-Y057nlaQbpRDSjzNxDK_hEZaZ2x-qNoGEsPkCN8jnqOt-cWI0w4penc6WY4MYbiVWLa9r8d_uupUMTkmDy1qjK47BzU3AYEF1XfRdT7ZoCQ6cHps3Pul-FFBfy9RkLcmk7UQLrWFgH9uAJBf97BaKC3t_TFf2sNAxMxr9ac03t9j6TT1v2UbTrUIHL15z3BHZiScZEuHZ8Ok2bk6w1lX9eJ9-ZgN5ZmFH0sjQJN0Cn9gby3DOVPTssxGImKMcKsW5-ghSQwDHx0RZMYE0kH3gKH0eR_zWi0Cf7mBX0ijRAUNsl-ARLyjrTSYKlcjQ01w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/098c9ea234.mp4?token=Jx6Xg1rmF6PMFxM2yeix1-Y057nlaQbpRDSjzNxDK_hEZaZ2x-qNoGEsPkCN8jnqOt-cWI0w4penc6WY4MYbiVWLa9r8d_uupUMTkmDy1qjK47BzU3AYEF1XfRdT7ZoCQ6cHps3Pul-FFBfy9RkLcmk7UQLrWFgH9uAJBf97BaKC3t_TFf2sNAxMxr9ac03t9j6TT1v2UbTrUIHL15z3BHZiScZEuHZ8Ok2bk6w1lX9eJ9-ZgN5ZmFH0sjQJN0Cn9gby3DOVPTssxGImKMcKsW5-ghSQwDHx0RZMYE0kH3gKH0eR_zWi0Cf7mBX0ijRAUNsl-ARLyjrTSYKlcjQ01w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">از ابراهیم شکوری تا رحمان رضایی ...
‼️
در جواب ناکامی بگویید: یخورده سرما دارم
🥶
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/Futball180TV/107686" target="_blank">📅 15:40 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107685">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/086fe81733.mp4?token=uqP2mNQ1cMPf7jt_vyEBlO6gzgx3hkN95Y8MnjfddzxENcu2XcSkiyS8aJJL4X634sv_cKhcvY4n0k07zs2lof4PU6ZhWUpeX66CYIUR8J1ibWwH1qE8dawh-SgyGeslSuPrPKjgLknmaVjNI_BCGOv_aRqQGa2UhUJjxM_zK0Q-2BUDZZYiHSjMk-RnxczAhA6MQZJGvrnORVlslzVsPS5p0GAiNYfat1eHuL8zmAV5sQ63fDOepxKRu_JggsSdvr_B3F0GD8dwsLJxhkCpWg9SIaroagHZ_jNzU7MwgeCVxtqZHQDu2Q_rRuKAyC3IhiHMUoxPq1GpUSowx4h1ig" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/086fe81733.mp4?token=uqP2mNQ1cMPf7jt_vyEBlO6gzgx3hkN95Y8MnjfddzxENcu2XcSkiyS8aJJL4X634sv_cKhcvY4n0k07zs2lof4PU6ZhWUpeX66CYIUR8J1ibWwH1qE8dawh-SgyGeslSuPrPKjgLknmaVjNI_BCGOv_aRqQGa2UhUJjxM_zK0Q-2BUDZZYiHSjMk-RnxczAhA6MQZJGvrnORVlslzVsPS5p0GAiNYfat1eHuL8zmAV5sQ63fDOepxKRu_JggsSdvr_B3F0GD8dwsLJxhkCpWg9SIaroagHZ_jNzU7MwgeCVxtqZHQDu2Q_rRuKAyC3IhiHMUoxPq1GpUSowx4h1ig" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇵🇹
‼️
رونالدو رفت و پرتغال تمام شد!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/Futball180TV/107685" target="_blank">📅 15:15 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107684">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RXo_wKYEaxbxXfBaworgDwhpHCMDR-io0xWR9KDVeOerhc2VISsZLNuBQehY2pHzRIf0E7kSkL8NTJEHbt9ObJ2hFRnwXiQG1GkmehWRWBPuNIGHi_dIwd0Yv6n_AhocLnnDvk-k1c4n_XnqdFnaPyyNpedQ1GrGTVm6bSixvtDeu3FRlCD5b2VzDwfaODnD--ueFWg-FBj3q0mW8AQMFabdjvT-Gtak93nC92XeKuZACNRFU9qCf-aIvN5y_tMZnRkLuhZWskATuTBmBAhYs77fOppEbGUNuPRyO7QZ02DoUjF598FTCNOT4HX1dj3I_EIorhVXDKiof07Qt0_xgg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
✔️
🇪🇸
فابریزیو رومانو:
🔻
نتایج آزمایش‌های کادر پزشکی بارسلونا تایید می‌کند که مصدومیت عضلانی رافینیا که در اردوی تیم ملی برزیل دچار آن شد، جدی نیست. رافینیا از هفته آینده در دسترس خواهد بود.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/Futball180TV/107684" target="_blank">📅 15:12 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107683">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0b2fc633f5.mp4?token=W19ABO0rpDZAGCdBlw0gfvDCNV8PM_ZGMLJD0hMAIbRAx-4cN4thEamgDKjq0EEJvNLQuIz-cMMbsFAMAIzhSUpvxOvz-VHywO-v4DhN3zZj3HKR_Nc1-BE_vt7YZC-4QVgpK3PhjueYH5a7x9uM3XKymyLM0VwblY3jhj4eoF-OU5Hzu7rkloJMo8gliHjUB4Urj782Z1oSw3xHvhZR5XDrwoWhl7SdrPFfgXkMfX_zOa7vpdWL86Ggvpe1fwRct2Axp45WPbh-_BKFs3Ncu38QKx6wKa2DRRK0i42CyOF6K5LwvbWbhzUwH9u3yFWBTuuL6Ekvc_cucs1PcDDjZQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0b2fc633f5.mp4?token=W19ABO0rpDZAGCdBlw0gfvDCNV8PM_ZGMLJD0hMAIbRAx-4cN4thEamgDKjq0EEJvNLQuIz-cMMbsFAMAIzhSUpvxOvz-VHywO-v4DhN3zZj3HKR_Nc1-BE_vt7YZC-4QVgpK3PhjueYH5a7x9uM3XKymyLM0VwblY3jhj4eoF-OU5Hzu7rkloJMo8gliHjUB4Urj782Z1oSw3xHvhZR5XDrwoWhl7SdrPFfgXkMfX_zOa7vpdWL86Ggvpe1fwRct2Axp45WPbh-_BKFs3Ncu38QKx6wKa2DRRK0i42CyOF6K5LwvbWbhzUwH9u3yFWBTuuL6Ekvc_cucs1PcDDjZQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🔝
🌟
رسانه‌ها با انتشار این تصاویر مدعی شدن که نیروهای خنثی‌سازی هسته‌ای آمریکا همراه با یگان 75 عملیات ویژه، شبیه‌سازی و تمریناتی برای تصرف و پاکسازی تاسیسات هسته‌ای زیرزمینی ایران انجام دادن.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/Futball180TV/107683" target="_blank">📅 15:06 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107682">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0274908694.mp4?token=DqjBqkhpNjg6DWmgrBUrpZw7qGXVrlF-ncz1jT5xUYN-ErEjOoMApKfpMmKnbTTsRTYhHx3SzFqXO9frYYelM-aEpeagAD0djbRmTN-V-Vb1vAZ_RIxUL-bimWopFwMpiG5xa6qu8IO3GUOBwZNwUzzaw1EJIoh6R01JFA3elSQyOMmg8lW-bs1ZCKb9XP7jATWKFhw26op6U2b1vAViX6WDuTe1NkMZOXX6_E612K1el2k4Zc87nXYUj8MVHpoaJUkMDVnGoMK-MxTnFk4dvyBAcDJJcX1RX_N61wa-WAQolCbNyVvYryDgVZ1C84MZPaMKLrtaphdF-aL-vFxs7Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0274908694.mp4?token=DqjBqkhpNjg6DWmgrBUrpZw7qGXVrlF-ncz1jT5xUYN-ErEjOoMApKfpMmKnbTTsRTYhHx3SzFqXO9frYYelM-aEpeagAD0djbRmTN-V-Vb1vAZ_RIxUL-bimWopFwMpiG5xa6qu8IO3GUOBwZNwUzzaw1EJIoh6R01JFA3elSQyOMmg8lW-bs1ZCKb9XP7jATWKFhw26op6U2b1vAViX6WDuTe1NkMZOXX6_E612K1el2k4Zc87nXYUj8MVHpoaJUkMDVnGoMK-MxTnFk4dvyBAcDJJcX1RX_N61wa-WAQolCbNyVvYryDgVZ1C84MZPaMKLrtaphdF-aL-vFxs7Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚽️
⚽️
پایانِ متفاوتِ دو اسطوره.
💔
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/Futball180TV/107682" target="_blank">📅 14:50 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107681">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a6703d31fc.mp4?token=pVQkApfXJAcynkCAUK2rXhZ495l0eLCRQM-e_20VvZJJBKmtl7ibw2_SiRPXynaHn94xYlpNPYsuP4s6HifG95zTBp2qIXnz4gL5NlUUr5QPT06ekW5CS_BQcAjGin3pTt9oT7QqnxO6VKtESvHWmw-svunn2XOKAGMYLCXqDECQIiffW8Zzy2DiN79M5q2nkShsNl2nMWw2CN50o34GtTitRRx4p4rgCVlVuOCR_2W1CQcEzMhcPprL7Pseg8OWfQSvGDuwcww0lslkTIydphSKAuaK0VYHkno_JPLu1MXdn5DqGNwXN8zsyEOjhQ9ZEIR1QcgympGjcg-8Qm9EAqh6JVaOxK6HKSFGf1so0WNuMv0K11dbajlujiYRBYZDlkIWZ-Fv92krIywyT1uNCQ6eZj78Iqd0ceqScAa6HAohvPrQiRZneY_utwrcBuvONt_f2qihjx8RAHD1hTNcNxbp-xXIRq_AjrED430TTTgG5RQNUQCU1w_W0wxbtsgaFa4ohhY-T6mVFptRKySPLfonH7oFIfQ7uagyFWQIOG7rgAWHKurYxOTy-WKcr93hrSZ3-GBtCR1fI_U-bTfWII2rQD8_xDH3UjKEIVyGqNnWNg74hK5jGykBRXyjh5IuLiQI4x7hRYrfqZy7PvueKdbsEHOFZhE-IMP1dEArF_Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a6703d31fc.mp4?token=pVQkApfXJAcynkCAUK2rXhZ495l0eLCRQM-e_20VvZJJBKmtl7ibw2_SiRPXynaHn94xYlpNPYsuP4s6HifG95zTBp2qIXnz4gL5NlUUr5QPT06ekW5CS_BQcAjGin3pTt9oT7QqnxO6VKtESvHWmw-svunn2XOKAGMYLCXqDECQIiffW8Zzy2DiN79M5q2nkShsNl2nMWw2CN50o34GtTitRRx4p4rgCVlVuOCR_2W1CQcEzMhcPprL7Pseg8OWfQSvGDuwcww0lslkTIydphSKAuaK0VYHkno_JPLu1MXdn5DqGNwXN8zsyEOjhQ9ZEIR1QcgympGjcg-8Qm9EAqh6JVaOxK6HKSFGf1so0WNuMv0K11dbajlujiYRBYZDlkIWZ-Fv92krIywyT1uNCQ6eZj78Iqd0ceqScAa6HAohvPrQiRZneY_utwrcBuvONt_f2qihjx8RAHD1hTNcNxbp-xXIRq_AjrED430TTTgG5RQNUQCU1w_W0wxbtsgaFa4ohhY-T6mVFptRKySPLfonH7oFIfQ7uagyFWQIOG7rgAWHKurYxOTy-WKcr93hrSZ3-GBtCR1fI_U-bTfWII2rQD8_xDH3UjKEIVyGqNnWNg74hK5jGykBRXyjh5IuLiQI4x7hRYrfqZy7PvueKdbsEHOFZhE-IMP1dEArF_Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سکانس جدید از گزارشگر تکواندو براتون آوردم
😆
😆
😆
😆
😆
😆
کسب مدال طلا توسط ساغر مرادی در رشته تکواندو با شکست حریف ازبکستانی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/Futball180TV/107681" target="_blank">📅 14:41 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107680">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/353ac7dbfb.mp4?token=utvD3Pc_1LzRFIU2m9L9f5qF47hAtkkVhWKIAW4-6ASOV5jje_6b_FPJJCbluNYIvfIAo6OETWl2po-6cc69B_7k1gxX3Q3zoLNt4K-EOGI7j74PZajJACF4rHiNgry_i-kKNmkoBlM5hcAB7RlzamWBQU2PKpLDV3MnfcTuqROpdOK44TDvzLclE16O5_k-RvOSCGhhFny99QI4BlcfaZFqZhGTeMMB_YcmD5LIvPsocWxI_2ZU0uvjcjLBFXm-X8dvZRfcbGeJqeTiJ3wW538EE_nMb5vt9oCdtNhSQ0LzoDOLfypSgRNnEoBCqXbcMm7N73oYE1Lll5N_gS3qyDw6chQW65B9ocuxepk0IAwXLs5hDGh230X62ZxN6emMDmITsFzXy4OrDZEwni98NOZ-yA19iSWfykfjTYq2jCStZo5_xKNqJjXKbRH6p1UoeEeEkeXbBVSJpF-n0tQkigAO_DwMuVNox5bQ1jGcDbAvexBS3X2n9fkutDmLIFZaqD_IoxFOSFY23zXcisnvX4iQO-E9Eh94TLLwODDkLN7HYSxZg_0nOBsJyYpsAP4Wkatb92zhso-Vw0GDryavfH15gkiWPAGXsSAZh3KW6bT7HGUzZy2rfxnPSjZ3yl_BHGi5kaqXjEi9l4MD_vdLX1rMROgiLrZsNEIISTmTAAk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/353ac7dbfb.mp4?token=utvD3Pc_1LzRFIU2m9L9f5qF47hAtkkVhWKIAW4-6ASOV5jje_6b_FPJJCbluNYIvfIAo6OETWl2po-6cc69B_7k1gxX3Q3zoLNt4K-EOGI7j74PZajJACF4rHiNgry_i-kKNmkoBlM5hcAB7RlzamWBQU2PKpLDV3MnfcTuqROpdOK44TDvzLclE16O5_k-RvOSCGhhFny99QI4BlcfaZFqZhGTeMMB_YcmD5LIvPsocWxI_2ZU0uvjcjLBFXm-X8dvZRfcbGeJqeTiJ3wW538EE_nMb5vt9oCdtNhSQ0LzoDOLfypSgRNnEoBCqXbcMm7N73oYE1Lll5N_gS3qyDw6chQW65B9ocuxepk0IAwXLs5hDGh230X62ZxN6emMDmITsFzXy4OrDZEwni98NOZ-yA19iSWfykfjTYq2jCStZo5_xKNqJjXKbRH6p1UoeEeEkeXbBVSJpF-n0tQkigAO_DwMuVNox5bQ1jGcDbAvexBS3X2n9fkutDmLIFZaqD_IoxFOSFY23zXcisnvX4iQO-E9Eh94TLLwODDkLN7HYSxZg_0nOBsJyYpsAP4Wkatb92zhso-Vw0GDryavfH15gkiWPAGXsSAZh3KW6bT7HGUzZy2rfxnPSjZ3yl_BHGi5kaqXjEi9l4MD_vdLX1rMROgiLrZsNEIISTmTAAk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🥇
کسب مدال طلا توسط امیرحسین زارع با شکست حریف چینی در فینال بازی های آسیایی ناگویا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/Futball180TV/107680" target="_blank">📅 14:31 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107679">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">‼️
وضعیت عجیب عدم پاسخگویی اعضای تیم قلعه‌نویی درباره نتایج ضعیف اخیر!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/Futball180TV/107679" target="_blank">📅 14:25 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107678">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sDR0JGAtaYxJHQ2ZGqUb0aBEU5riZyvaHDh6LYP7j_tsZYx7fMsOQtNuBbqYhDvEklIO3U6PQWaKbRB9pMK1evyAoGBHWdxK3BgYmwDZXLSraLUgAPwVpE1yCTdf4L-g4rf15hgLaZzKmErI5UiSEwOqTxL1qaqNNT-42JuRLSLOcM8DqpouX4VSaM03Ie9iQW6e95IFhkgdawm4hz8fB0g7DKNEKNavnnqZy1eYnJ_HEHWke1-D1s23gH81niGkNQWTIJ77Ux0rr6Y73LF5tzVZX_lC7Wyi8FnD4jSVTPkB1E32RX2Wb7RpBELiBqkdwaNkgvWPj7mViqDA6v2Odg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🗣
⁉️
مسی یا رونالدو؟
👀
🤩
توماس مولر:
"در طول ۱۰ سال اول دوران حرفه‌ای‌ام، همیشه کریستیانو رونالدو را انتخاب می‌کردم و همیشه در مقابل او شکست می‌خوردم. اما وقتی به کل تصویر نگاه می‌کنم، متوجه می‌شوم که لیونل مسی، بزرگترین فوتبالیست است."
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/Futball180TV/107678" target="_blank">📅 14:10 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107677">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/df3d0d9fde.mp4?token=XpH9ac6dmWI3FGZKl1RSCnSzicNiIt943W_AUjYR6c6lfAaEBAUJcscsxdxjCIrYIykTMccCOfnmq4ZIpDtJx-G4xx_4e9r7_DpBE5jFwvhXQLpMzU8KHJ8GzO0u5d2vPaRPVQfLufeXGNFTKDxaFq0OhqmDujMc0ddItJti5lpyRRvVrAkd0PwxzkTyaLj4R5QQ5vBTBuoX5uQD3FiHaqS-1FiR-2A7xUUFrZeKoQfE1iiG9ZCmvVUNJgQHcdzfrvUbY9GD0We6qE_zeeMmPLp6uhB8BSGTNmen04Ql2MVy8MeTPoWhsNG5y4g6DTem_1LBmaHhE-hLYeKmQjzH8Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/df3d0d9fde.mp4?token=XpH9ac6dmWI3FGZKl1RSCnSzicNiIt943W_AUjYR6c6lfAaEBAUJcscsxdxjCIrYIykTMccCOfnmq4ZIpDtJx-G4xx_4e9r7_DpBE5jFwvhXQLpMzU8KHJ8GzO0u5d2vPaRPVQfLufeXGNFTKDxaFq0OhqmDujMc0ddItJti5lpyRRvVrAkd0PwxzkTyaLj4R5QQ5vBTBuoX5uQD3FiHaqS-1FiR-2A7xUUFrZeKoQfE1iiG9ZCmvVUNJgQHcdzfrvUbY9GD0We6qE_zeeMmPLp6uhB8BSGTNmen04Ql2MVy8MeTPoWhsNG5y4g6DTem_1LBmaHhE-hLYeKmQjzH8Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
⚽️
دیس سنگین ژوله به قلعه‌نویی بدلیل سوال عجیبش از خبرنگار ازبکستانی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/Futball180TV/107677" target="_blank">📅 14:03 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107676">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/eade000140.mp4?token=AqLbJXcrBShB2cH1_ELqn5lhYN8FJ7bPConT_08Glbe6VvD-_H__7FgYwV1B2oq9fkX610UE4Vj4E76gSO0TQaWFsHZ-I6oyIiEzXZfOb3_KGo9A4iOCK9X63iJ-GFxoB1B1U6vlTM6LE2oGyNEN7OwA0DxqvUuPkUqyatPSfSVZ95ow59hUqMuSDbbti-G37wet1ohlj-pbrQ3Yjrnl1Iut7aThGB-eodZASVc4tEjPFpwTg4rv4QDNt3JUsn38hl5vaFfI54REPaIRskuQhEN4ba3dc2jgBxVLpPpRCPrIVUlmA1o__50tY2wCylipRkooMdg2knM2FDgHGdQsYbaaxCTDFzU6ZPH14gKStZuMmzJgw8lTED0ErpsBeeM4iRWcTpovjtn7yuusPg7V7YuB49PdQptoPouEe1HWmV7zOMm6mqzRUVBPeueUi67kVZYcb9BvSeQt-EyctbrTVmLqAg8o8_kY9mT5scwJnA_ogcuBYSCAHVhDN7rUboUT_93EPn-pQhrFoFfUfWQxrehpnsR7Rq5C0ZalNVY9CV88PGZoclwYY2kHAzbZZrpzl8h7Ujzf7OrNv_HOCzyGwxs4Nck5elh7vRXjdX_zlzoQQCQhZ4u1TfejFBS5XQjW8uK0vRqw-FZN3yWtJ-woxA1fbM9OfWtmoaXOd0bBVQQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/eade000140.mp4?token=AqLbJXcrBShB2cH1_ELqn5lhYN8FJ7bPConT_08Glbe6VvD-_H__7FgYwV1B2oq9fkX610UE4Vj4E76gSO0TQaWFsHZ-I6oyIiEzXZfOb3_KGo9A4iOCK9X63iJ-GFxoB1B1U6vlTM6LE2oGyNEN7OwA0DxqvUuPkUqyatPSfSVZ95ow59hUqMuSDbbti-G37wet1ohlj-pbrQ3Yjrnl1Iut7aThGB-eodZASVc4tEjPFpwTg4rv4QDNt3JUsn38hl5vaFfI54REPaIRskuQhEN4ba3dc2jgBxVLpPpRCPrIVUlmA1o__50tY2wCylipRkooMdg2knM2FDgHGdQsYbaaxCTDFzU6ZPH14gKStZuMmzJgw8lTED0ErpsBeeM4iRWcTpovjtn7yuusPg7V7YuB49PdQptoPouEe1HWmV7zOMm6mqzRUVBPeueUi67kVZYcb9BvSeQt-EyctbrTVmLqAg8o8_kY9mT5scwJnA_ogcuBYSCAHVhDN7rUboUT_93EPn-pQhrFoFfUfWQxrehpnsR7Rq5C0ZalNVY9CV88PGZoclwYY2kHAzbZZrpzl8h7Ujzf7OrNv_HOCzyGwxs4Nck5elh7vRXjdX_zlzoQQCQhZ4u1TfejFBS5XQjW8uK0vRqw-FZN3yWtJ-woxA1fbM9OfWtmoaXOd0bBVQQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🥇
کسب مدال طلا توسط محمد نخودی با شکست حریف ژاپنی در فینال بازی های آسیایی ناگویا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/Futball180TV/107676" target="_blank">📅 13:58 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107675">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d46780b4e7.mp4?token=I2TZg1YRoNF9hEAxbcTGjx1YYzBpo2LhXl8uFcafik0Ko28LrLrlIpnsZh1c6qRuZfjDJvHNQ8RQi6M-uO9Iwr3dgtgzokkIxhIHY16Fh0KjpxrWp83PA8Uc5Cqnf5vjqxF9V-jxKnnokK4pSO5w6Diu-kFHbOVROK2K6qsA-qyzCZzUXdYsqRWifR5x83mXSVUvc7BzJKbxmmTC4GnQlyqjsqkvLgF2AHxRp1-AahzNLs-MiCYFtPQpa7Gc2mPZ1c04I2EIRbDqxonoR_CtlpqIt8ctvlREj4GGsGi0B03VorrgPkZSa6kDADDNJKYSQvcrMWP_ecRC_uBXwvSebQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d46780b4e7.mp4?token=I2TZg1YRoNF9hEAxbcTGjx1YYzBpo2LhXl8uFcafik0Ko28LrLrlIpnsZh1c6qRuZfjDJvHNQ8RQi6M-uO9Iwr3dgtgzokkIxhIHY16Fh0KjpxrWp83PA8Uc5Cqnf5vjqxF9V-jxKnnokK4pSO5w6Diu-kFHbOVROK2K6qsA-qyzCZzUXdYsqRWifR5x83mXSVUvc7BzJKbxmmTC4GnQlyqjsqkvLgF2AHxRp1-AahzNLs-MiCYFtPQpa7Gc2mPZ1c04I2EIRbDqxonoR_CtlpqIt8ctvlREj4GGsGi0B03VorrgPkZSa6kDADDNJKYSQvcrMWP_ecRC_uBXwvSebQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وضعیت آخرین اردو تیم ملی قبل سربازی =))
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/Futball180TV/107675" target="_blank">📅 13:37 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107674">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nNXJ57iMis45OWYoDy1nOnbJUa00i-7zq4O1IOk9pj4Tk3J3DPBBcmtd7LfWvwb05iD9PIcuABut2bPxXE7EfIHQ2hcoalOVtTC8hQe970sDwPxdAPCHaeSCtt0mBo0pAzbOyrT6qlAPQjLWnJYuFH0H-IfLU9q9COAtsKPCFqdfdQVEDeOXj_x2TCAiQtcCScYu-pjAHTjKIB5rWE-4gnsuw4rIvD9W8cyCn-DNv_OwfmV4W3hrGdHxfVbBP5d2yJ_TPOCmcHV-_aT2PrY6XPRcXtJoNn7PHDWJ0ke71a3EOkLfdnZ7BJ3FgiQeuEBjZtTWmxRtjlLEFHnIKewhmQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
‼️
هویلند بازیکن تیم‌ملی دانمارک: شادی دیشبم برای ادای احترام به رونالدو بود و هیچ قصدی برای توهین به بازیکنان و مربی پرتغال نداشتم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/Futball180TV/107674" target="_blank">📅 13:16 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107673">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/817ab8c188.mp4?token=PoNP1zKqVIn2tAdVfXl5d_nGkoA3ClhknuKW0__u6O7Rvxkyms_Crx9SvxlJ1_SfiWkuvessAiDpHGsP3C27AdrD9JCl3IbFEjGmkdqnQ4eSb2NkbiYJAZTEKAIa1EkSNYiCk1zXpXxCkWmXdOjWxUCE2sa98KjAzEH7VXBvG8qbko4I37CwnFPENy07u2CcuObuQ4gGtKZV2cQRaQeJITgYncMWrL9fAevmttaUIwJKy_3qubyBoH1fyLUdZ4nnybQEoQaf9eNPp9LUHnt99m_XuwCG_omU_-qO1DlLruAAQIqvlhZLk_z4EImSycIR5Jstt1AIzbLNJj2CH0OWNL5CyJErBDM328LwSlfm3o_cwPbGdc6trz9_T86lzFF_6TfjcvvTkeCgHi0LZtPTzv5BVRjUFX2cKeNtcUGvyjyyUpx_9XBIKQuvoirFvn5QFDb9rBk-Cy2iM7Uc8pnh1Q8AYaLUiuE1oAvhmHN-kpl7ZlxrPgzrf-vfqFz6eTr0EcGbvuTBeffNZ-sxxa3grymRo7CMyczleoVR_8E_jZHFWpyg38CW3uA-CnKBfOaKMnLS917DY8v_NIUnWCgETz3MonDle03Qj1lcyS3Q-fgyDCWe1EDGOpkfvFG_qraPFIVPW-kJbCmjuSCRegbcaARGxgLyD-wwOAUB3koZP3Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/817ab8c188.mp4?token=PoNP1zKqVIn2tAdVfXl5d_nGkoA3ClhknuKW0__u6O7Rvxkyms_Crx9SvxlJ1_SfiWkuvessAiDpHGsP3C27AdrD9JCl3IbFEjGmkdqnQ4eSb2NkbiYJAZTEKAIa1EkSNYiCk1zXpXxCkWmXdOjWxUCE2sa98KjAzEH7VXBvG8qbko4I37CwnFPENy07u2CcuObuQ4gGtKZV2cQRaQeJITgYncMWrL9fAevmttaUIwJKy_3qubyBoH1fyLUdZ4nnybQEoQaf9eNPp9LUHnt99m_XuwCG_omU_-qO1DlLruAAQIqvlhZLk_z4EImSycIR5Jstt1AIzbLNJj2CH0OWNL5CyJErBDM328LwSlfm3o_cwPbGdc6trz9_T86lzFF_6TfjcvvTkeCgHi0LZtPTzv5BVRjUFX2cKeNtcUGvyjyyUpx_9XBIKQuvoirFvn5QFDb9rBk-Cy2iM7Uc8pnh1Q8AYaLUiuE1oAvhmHN-kpl7ZlxrPgzrf-vfqFz6eTr0EcGbvuTBeffNZ-sxxa3grymRo7CMyczleoVR_8E_jZHFWpyg38CW3uA-CnKBfOaKMnLS917DY8v_NIUnWCgETz3MonDle03Qj1lcyS3Q-fgyDCWe1EDGOpkfvFG_qraPFIVPW-kJbCmjuSCRegbcaARGxgLyD-wwOAUB3koZP3Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
✔️
نکاتی‌که قبل از خرید آیفون دسته‌دو باید بهش توجه کرد؛ برای رفقاتون حتما بفرستید
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/Futball180TV/107673" target="_blank">📅 13:10 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107672">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uLbXBfiNIcWjDZEOYkmNm3EV5R3B8SL4ZSscsabbLd72axNBbPc4egNvbuJh9jpT7rKPThJHbreqsuG7SuaBEaXTLrBMP_Fy8FRDBhpd05lfySfbMO-8cwwxhxbv5X6xHM0SHZazl6vVjSR6o6uf8F7LSlgbqby3Pgfhavf0l6YbVurf9pnk86J_xmNUyKKN2OcS5HSGLxuzi2UB2LK8oBNz6yqgklKrxobM-TWJKCgWn1rqFXL9TdVbYZ5kTodgNzvtcC0VTAIp2jWR36AA6BDHhxfyUWwxn31c7xpAeFCHu4LoDtlZPGhryC55jGqkdqD5qEEQoc6JqUfT9g4aYg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
‼️
😐
استوری همسر رافینیا ستاره بارسا!!!
فوت‌فتیش هستید دیگه چرا علنی میکنید
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/Futball180TV/107672" target="_blank">📅 12:48 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107671">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/78eef6851e.mp4?token=uJH4ShpzsL7gZq4LC12tqY_AEhk5H-AXGDSzmufcgDA1Y9I3skOOTTNXmS-KJ4v0FF50kHoCxdXcQHhzXMy4hEdD4GgsoWDfocodiHnbFHFwoHk2ktR5nYqDlo_dhMZ5rJZ3BXAfRIEUZAR2LRvuttmsqaaQ6XZ4FOKdqOrE3jjsIyLRaFxC-azAJyg10GbtcRxSRKKhtQUlnuPfI2VOSnMOfLQOoxYeYy94shgO4ufc-14H61LFH4s8WbmZC5IChWxW3KuBqaWtsXCuO7bjZtTXZOFtfGb7Y3nPnGrG9o-3ZBMbt7lyLu2HqbpbqjCnYCQ0NbnIpMprc3jBrg57bA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/78eef6851e.mp4?token=uJH4ShpzsL7gZq4LC12tqY_AEhk5H-AXGDSzmufcgDA1Y9I3skOOTTNXmS-KJ4v0FF50kHoCxdXcQHhzXMy4hEdD4GgsoWDfocodiHnbFHFwoHk2ktR5nYqDlo_dhMZ5rJZ3BXAfRIEUZAR2LRvuttmsqaaQ6XZ4FOKdqOrE3jjsIyLRaFxC-azAJyg10GbtcRxSRKKhtQUlnuPfI2VOSnMOfLQOoxYeYy94shgO4ufc-14H61LFH4s8WbmZC5IChWxW3KuBqaWtsXCuO7bjZtTXZOFtfGb7Y3nPnGrG9o-3ZBMbt7lyLu2HqbpbqjCnYCQ0NbnIpMprc3jBrg57bA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇵🇹
‼️
🎙
واکنش متفاوت بازیکنان تیم‌ملی پرتغال به خروج ناگهانی رونالدو از اردوی تیم ملی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/Futball180TV/107671" target="_blank">📅 12:45 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107670">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MKX--JdrIUrvHlYWdTYRCBKzDtkneEchf4skgPwWfBslkljxuG5QFQl45i-tWVOy_WV5knXfqzTcf32qmQ9Rlf9KoQz_52M073Gg224k_WeqbyKS82XymCe2aWHkLm7t3sxoAzD2mdinIFMjt2_bkWZorvpWiZutzRNJP-d-fr3cOlZOrlpMlEwrSZR2_3ECCa81cZlBsVnUWtPnbTRAM5UxWmOOa6ARqZU1g1ayzY7hPcBWyHvgnBRYmCwE35KtO7Jss2_eEkWAzGHbCLFrRHaF0F1gdmgF1EkdWhIy-R41GLTNIMc5DCJSs7uRs_sgVlrEgv89w0njpatHTtzQOA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👀
🇪🇸
تایلر، د کریتور (Tyler, the Creator) هنرمندیه که تصویرش روی پیراهن بارسلونا در ال‌کلاسیکو رفت مقابل رئال مادرید قرار خواهد گرفت.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/Futball180TV/107670" target="_blank">📅 12:40 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107669">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vWM_oNJJ9s0NEV0r2K2rHKkWVdnp4ULZBAGYeRC-zIAWIRO7RFM6pTALKtmbHcC6EAxW_ddER0Mbhc07WnGvkUhma4vihAceBTCCFRlDdO-kO6xteEBZ442rkZ8hHGaQU8eZMWCjCBr5wsSJfZepCt38IV_pXImi26zK8RZVeqT1MEWu1s9Vx4IzFmAfbk_P8wclupVkPwddQjQx9ZzqQ333BL2vnGghOQ0rgbpDvLJm22QQetidNUKjVv1NoTpg2PbWapUzAy9Fmdb7PXTtZZN-N2rnFzw5NuQ4khDincp4EDwYomvNiqm2-VWCrCsnm3Fhhi1b4liQ6S-4zbE7IA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👀
🇵🇹
خط‌حمله پرتغال بدون حضور رونالدو:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/Futball180TV/107669" target="_blank">📅 12:29 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107668">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Iuo0IkgJob-J664gzd1m8L7ZZ2vTxXqNIre6bTOFqYZg1-WmzDz_bmQvJaQUzNJaeYUiCTZAkwrVp4P1CmkE79wG4zb6zWyoiAMaZr0Emebg83QezRO0vwdZT6-wpe4vtbxMh-SLgO8DrsDTswyQ3TtbzCOoX2UTCcqNhfeL2UZB6zEO-ouUV3blnmDzgApmQFiIQKLLhF5OnRnuF9QY7i0XXzhvqZmSe2nj4X7hMjQMtIP4omlMMN4N2N6_hj8QI8DlGAILJ9GsvzU4EJtv6t8AEYWtwY_8rPsvrFk2Vk720E-6PkKVO_D5c-u1asivXuc8AfY2GJE-3T7NNNSKrw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
📊
بر اساس انتخاب  بلچر ریپورت ، لئو مسی بهترین بازیکن تاریخ فوتبال است.
۱.
🇦🇷
لئو مسی
۲.
🇧🇷
پله
۳.
🇦🇷
مارادونا
۴.
🇵🇹
کریستیانو رونالدو
۵.
🇧🇷
رونالدو نازاریو
۶.
🇳🇱
یوهان کرایف
۷.
🇫🇷
زین‌الدین زیدان
۸.
🇧🇷
رونالدینیو
۹.
🇩🇪
فرانتس بکن‌باوئر
۱۰.
🇪🇸
آندرس اینیستا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/Futball180TV/107668" target="_blank">📅 12:20 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107667">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/721222cb0e.mp4?token=RwiMZDrrqClqBsbf-35znM350tcatV9Rkgn2C8WoI8657R-GC8DBuBi58UbQshPitFRQvsO5yUCEqpgem9UPC9g7QmFKJP3Y1K8mCWNzRe8Prhcj7mBptPZJhCwfCre--_AEVbIL-eDZ6YPOKFavrSPU-6TMPew9CDL5-J7D5DDfL5wnrQGe4dnbakz7qf03xTVABGhiy-J-rfs8WsVwiHDWDtmfD8mOLD5XgU3T_St5XRAnFbTGvunwkwlC2J8FKkpKGfBVErmhIiqf8G7hgc33Mu_VqmsA2DrxC54pdDwZQa9FiL9KOIUod3C3VYQRgJOb9b18o7JjV0n-UOsOAZPx2fYM2FVx2I3jgfE2ZCLaKOlO_wLDk5NZzGFOzNgQ-uqzJiHq0oKGV-bzm0EWnHR5Yv4hxFykotXttdr0s2D5RBPZuvGclXxHHwtAAYIDMnIvr8UaHuMedNH1ZWz8M66Lv202rUJNgfjEpW-thY3SiTolg2TjFHPVVgJRvlH8h4j_Qb8xpOkr5cYiPsgn25kDyua2sx_ruMwdah596ANA9b8NDLbaIGZfd9rk1NpanJqcErPDY5MUXgmpi6uVvYXIn8HHB2xcsU-SDCREObheIzFPdsLRFk519pBi_ZUeBRCJjpqqsPzX_l591LaUu3Vlh564hS5QuXNG_lGdrPw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/721222cb0e.mp4?token=RwiMZDrrqClqBsbf-35znM350tcatV9Rkgn2C8WoI8657R-GC8DBuBi58UbQshPitFRQvsO5yUCEqpgem9UPC9g7QmFKJP3Y1K8mCWNzRe8Prhcj7mBptPZJhCwfCre--_AEVbIL-eDZ6YPOKFavrSPU-6TMPew9CDL5-J7D5DDfL5wnrQGe4dnbakz7qf03xTVABGhiy-J-rfs8WsVwiHDWDtmfD8mOLD5XgU3T_St5XRAnFbTGvunwkwlC2J8FKkpKGfBVErmhIiqf8G7hgc33Mu_VqmsA2DrxC54pdDwZQa9FiL9KOIUod3C3VYQRgJOb9b18o7JjV0n-UOsOAZPx2fYM2FVx2I3jgfE2ZCLaKOlO_wLDk5NZzGFOzNgQ-uqzJiHq0oKGV-bzm0EWnHR5Yv4hxFykotXttdr0s2D5RBPZuvGclXxHHwtAAYIDMnIvr8UaHuMedNH1ZWz8M66Lv202rUJNgfjEpW-thY3SiTolg2TjFHPVVgJRvlH8h4j_Qb8xpOkr5cYiPsgn25kDyua2sx_ruMwdah596ANA9b8NDLbaIGZfd9rk1NpanJqcErPDY5MUXgmpi6uVvYXIn8HHB2xcsU-SDCREObheIzFPdsLRFk519pBi_ZUeBRCJjpqqsPzX_l591LaUu3Vlh564hS5QuXNG_lGdrPw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⁉️
👀
📊
راز شروع بازی‌های پاری‌سن‌ژرمن چیه؟ این آنالیز بسیار دیدنی رو باهم ببینیم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/Futball180TV/107667" target="_blank">📅 11:55 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107666">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nBewNz-7r1tm6mGP2jFMAWMir3vIrCvROBISB8L4wfl3JSP6ozZTJLTU07CZQo0ykUXf7XIbinZMeDVngFh4uCQEV-OGvo7kOzKTk00uwUtuNelD34yjVrO3GdPhtNtm4oin9f07xZUcjX4ZnebBN2SGkJLk_msFQhj1sr_krJXIF50k_w14fACHngQXUl8UbNtSAogSJa9hPjMCgYjqjcPSO1bSEfGKdA0Mbwbe0ET-VswypJtcn3hNzeyeYRAPbbL9A9Og-nH4Li3XMRPKXSn9RyfdzLbrLOgEfWLufiI3_UJwK5JTox8q49kCOBNf4bmBLfKGoO9cPbUF1WFSHg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
✔️
تیم‌ملی والیبال ایران با برتری مقابل پاکستان راهی فینال بازی‌های آسیایی ناگویا شد. برنده چین و ژاپن فردا به مصاف ایران میره
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/Futball180TV/107666" target="_blank">📅 11:40 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107665">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BXX3cwdbugeuENd8lyk96EMMLgItxCBmcxOPDK4fP_CH7JZ-iNv2fABk_CriZqJyvskvKkr6lAtR6fLGcG_tBdDcU0YIQ1MQzAz_s6YGpXjZp79lV8d_HCeQcQqH0Fs9OxLf6QRHfUuwmOqZ229U_Xn0KwUcuCPLjTaPw-JEERZWs_OcvO68WC5hxlMyfCZIXCKZ2dhF3L_o4l2pvlMTpsQmvlvKGp230GWLoyGeGKRasGTH_K0ndxmnfcqTyZUYiVVCNcvNcSZ6V78SQtm1HXHh6-SR-M7AtJMJJYYWLQkcpT9TFXNIVsKjaQ5pHb-HiFch4gUQOodQ2GaKwX1Ydw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پرتغال نباید فراموش کنه که رونالدو عامل کسب سه جام ملی مهم برای کشورشون شد:
🇪🇺
یورو
🏆
لیگ‌ملت‌های اروپا 2019
🏆
لیگ‌ملت‌های اروپا 2025
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/Futball180TV/107665" target="_blank">📅 11:27 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107664">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/Futball180TV/107664" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/Futball180TV/107664" target="_blank">📅 11:27 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107663">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aG8J5OuaY7BIoC5Bm-gEnBm70_IZYvZrecnrjyNBjApvghxiezGjOp6Y0OLoscd-N4kFh0UKK7zRf97aZLVcuMTHq8_f8ipkLeUPHFg9hPM_1_YasiFuhDJJuR-yB4my6-tPCj9aUrk222MUGdUu_LH3NU4L0a-Bxc4zEvmLEdpD_Gddi0B4ejtonjxP45X7E-1JiEuCnV7nJV3l_DwI_k_0VTSWJKj37Vjy4hbfavRmvjXnBS5eSEUtSfi97sUX_Z4okPPtCVOtDLRAFAhUZbhcOeaf4bkSYBGF663T8tORcp6IQuVSy29XOle-Ro5ECNPntam-54NLZmAq_aAXOA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🦖
مچ‌های مهم امروز در سایت بین المللی
TrexBet
ترکیه
🆚
بلژیک
ایتالیا
🆚
فرانسه
سوئد
🆚
بوسنی
نروژ
🆚
ولز
ونزوئلا
🆚
کره‌ی جنوبی
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
انتخابت رو انجام بده و آماده‌ی هیجان باش!
TREXBET — PLAY. PREDICT. WIN.
https://TrexBet.com
T.me/TrexBet_Ir</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/Futball180TV/107663" target="_blank">📅 11:27 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107662">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/T-IxaGk_k4FnvT3N8N8XW22OD_EpuAqJh_JXUXzjqKUtF5PyAledFGxiH7MZP-WWmE-haGE6-OeYyiZ9f4-lOIGomAMTtHWuygc8RnEwin0ydPhPBGlbKgpW4kZRl2glFHnV4mFN7WCOwnd3UnOezzoqcm9MxdVJO3m-b9lRnq661zYxwD3-njQ60tlPKxCGxTfyg1pg80ZYmdyICLNTiSwoNLuaXXx3ab647KfiHJxYswdBvcZKqPmDQcSmctUMReb_swZFld1bqVe92ffK9XJcujRnIIjw4qEVP881NahaBauoSWfUlLP1qsHNb49A1CPqLdHf-n-eOaW8L1YD_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📱
استوری یاسر آسانی در کنار وریا غفوری
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/Futball180TV/107662" target="_blank">📅 11:02 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107661">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/312a800413.mp4?token=EwL5F_xe_d_0XcRnqoSGeYci2iokpcaiY4egiiWryV2ZZ1h9o7MmBPjhEUEBnd4bWxAJQslMxtteES6KJDx7qCGJ2E6UTqVpAmZV3F59AnuO_m6jrVtZCn0EIFOwq7gdh1Atcmoa3mLw-n7JLtLmGZioqw8l0VxJWvr0ZLLRQgIiNFXaO-1VpWvtEDjKl97n7-51ePj22CT-LTTeRHq7RP_NjEVaRB8p6_18L5FrE0_o1nnGWW09kKWR8HLw4OlkeR5nLbwkZTaDOyyMBuuzACBxHb4GR8yCiIum9PcI4BIS9VzVeP9vGBz4T6GfH_mnhDDCcBKw43YAYuHyvAw1enJOq2fPznqkMIXn-F0VQN6qTIjcxPCJu7DRW34MkBzonKa4K3NdmIzlT4TkLIW3aAWSIyTc4rG8gOShHL06xrJiD5ZLwrMBAbxq8D-FYnUrYrXxgCgq_rO7P68jDszTYBY_uh3HObkSTt12LAgIFmCXXueFVShuIvpLdd0LHdwybZDMOuqfixVC7zi_WhjmPz2lf-ySDhRmwAIZlbgnt3vwxatPrlmFLXw_9T4Xyghjcwjhrhvke2zNzl2iTz0F7it8dLzeyKlBtfmzcks24BJnx0h8MRc5tG4rsUS_Y1sjl1H1RXV3Qhpjrw7dIh0V0b4t79Ehk8tixPtFwkZRJVA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/312a800413.mp4?token=EwL5F_xe_d_0XcRnqoSGeYci2iokpcaiY4egiiWryV2ZZ1h9o7MmBPjhEUEBnd4bWxAJQslMxtteES6KJDx7qCGJ2E6UTqVpAmZV3F59AnuO_m6jrVtZCn0EIFOwq7gdh1Atcmoa3mLw-n7JLtLmGZioqw8l0VxJWvr0ZLLRQgIiNFXaO-1VpWvtEDjKl97n7-51ePj22CT-LTTeRHq7RP_NjEVaRB8p6_18L5FrE0_o1nnGWW09kKWR8HLw4OlkeR5nLbwkZTaDOyyMBuuzACBxHb4GR8yCiIum9PcI4BIS9VzVeP9vGBz4T6GfH_mnhDDCcBKw43YAYuHyvAw1enJOq2fPznqkMIXn-F0VQN6qTIjcxPCJu7DRW34MkBzonKa4K3NdmIzlT4TkLIW3aAWSIyTc4rG8gOShHL06xrJiD5ZLwrMBAbxq8D-FYnUrYrXxgCgq_rO7P68jDszTYBY_uh3HObkSTt12LAgIFmCXXueFVShuIvpLdd0LHdwybZDMOuqfixVC7zi_WhjmPz2lf-ySDhRmwAIZlbgnt3vwxatPrlmFLXw_9T4Xyghjcwjhrhvke2zNzl2iTz0F7it8dLzeyKlBtfmzcks24BJnx0h8MRc5tG4rsUS_Y1sjl1H1RXV3Qhpjrw7dIh0V0b4t79Ehk8tixPtFwkZRJVA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👍
عشق به مارادونا، با توصیف آقای گزارشگر
🎙
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/Futball180TV/107661" target="_blank">📅 10:40 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107660">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/74ab0dda5d.mp4?token=KDc6xECtwD5zW4fpEOOXowI3zGicZ56r50XVlIKiIrXU24iWe6rbzyeqpQGcKM52kkDTRsy9k8_zMJ1__rzn6P0RhTrKMot1IY2QuxOnxYNzLkizxmI4Wf4BxH2T8lbr4uMClG2MpckMLDGd_f5ZRiPHnRKVpZEAo4MD6FalHnlOjySv-HvasoVwHcIfUfAK2cg2Sg0WubtU9HATkI9wrUGsi8jsOX-YE4i3hZtt3ek7tQtibU-UhVDTMgK4ExRZaLld7jj2Fn0hatbpMI53RnEMz4bfwFE-9HTqd5bAmlskUF04wjstF6vESApz0ZQgK6nTatcvDHAgscgUayfn0A" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/74ab0dda5d.mp4?token=KDc6xECtwD5zW4fpEOOXowI3zGicZ56r50XVlIKiIrXU24iWe6rbzyeqpQGcKM52kkDTRsy9k8_zMJ1__rzn6P0RhTrKMot1IY2QuxOnxYNzLkizxmI4Wf4BxH2T8lbr4uMClG2MpckMLDGd_f5ZRiPHnRKVpZEAo4MD6FalHnlOjySv-HvasoVwHcIfUfAK2cg2Sg0WubtU9HATkI9wrUGsi8jsOX-YE4i3hZtt3ek7tQtibU-UhVDTMgK4ExRZaLld7jj2Fn0hatbpMI53RnEMz4bfwFE-9HTqd5bAmlskUF04wjstF6vESApz0ZQgK6nTatcvDHAgscgUayfn0A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
اون بعضیایی که میگن از صفر شروع کردیم ولی خب ؛ صفرِ شما ها، صدِ خیلیاس!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/Futball180TV/107660" target="_blank">📅 10:15 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107659">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/orQp6eaOGkO3nTWyIv9MCITtyeS3mqYSWunAqiSpa05cjLkabJUCJL2hc98QPA_wUsmHSBRW-ihnaYY63lNgfMLNgzrq-MUkLF6OtG81s8Wn0TCsFYGEjpOR7EwcXsXSI4iBt8pxiCrdfvt4EL6wFJhrIZ6-X-TNIBfTYrE_-uZhmeKQDE2CV3FaE4IO5oPnPjCBFOsBda1-TmtDtzHEotwdQOAwLYbcvz_CRBx-KjNqNiCHdAPmEAo5rxg4V2ziQyDzXUuhqX0y6T3fF1txwXfnN3q2Cnp2NptuJr-rL1AQt3qQxbz_peCzaiAAw60j9tIVvJIZx4zQJ-HgnA4c4Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏟
بزرگترین ورزشگاه‌های تیم‌های ملی در جهان
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/Futball180TV/107659" target="_blank">📅 09:50 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107658">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QE7iutemRzApWter8mnEGdx1-lVnvit9lKdm_SKC2P3wfiDDoNTCVWkjLtcS4tuO8PMnmPt55cDkrh9KIH0DfQ20czhMnQKqyCfuqq_c-ZdwGO91qQ1HIUO8sEAzxKNcHTlEyD48zNp7rnMDMBzQoxXgmPtpJGibogEiXP5snSBLk7CsYfYVZOKI1oh58Jb07ZUAyK2qJ4VZZwL3v4LjrqbyHK70t_7zANsrn8Tz-2632K2j6Fo8O6ulcRX1t2eS5_JK2sPWpuHUYR2fFv8ZlS9R2_sHQz6pKZcR7r9kcSyl_7aDrAJV94mxwqkShlOIzO3SjeKpt-AGcIDlrqunzQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
🐐
🔥
آمار و عملکرد مسی در تاریخ کریر فوتبالش
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/Futball180TV/107658" target="_blank">📅 09:25 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107657">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/85455aa172.mp4?token=D8rmm8ktWsm-Vq5hslzIFUQmFae3PP1M9DXD715m34iO3q22SNdWRI-Egb9rTJVjHXr5Nlo8t_1UKPNS3cjCVpsz_FetFAx8ZzuMB6pRd4SGOqeoaO3sArUn7rxiaf3c6E_a04ljvBeCYk8QA1VSN4GLEe1PkB1NHKgklY1UpkCDocgoFYwRpgw3q3iHu4a887lzwkgf4PEM_8cfBL3rJEqGHyA830Jq5bPkpZXh4ZCoe3cl35_y0IS3hHviGaUaDqXrwih_yOnr_AaYsNcTm8j73DjR-kBmLPJwbQ8F6ocDmAVo_r4WGJofVY7qu2FzMLIMOrvSCiNW4O07sfurFxS6UORND4M6jk0AslIsfMsfNXbwxROVCYaCO7xJ6aebmwhoIO_n_X1i000co0YwW2vHD3vy7dgYTKwYIQtCEXemQDoq-20W0HDrq6nB_6C8087uVBJdGHhM9IrBOS0s9gA83IcyRrP739o2YEkAaVsTDn1XljJmzbIkJff4xci-9-EO32vV7ZS88hdgvsHlhmMLkU5-bZ89Pfr83IEXaIgYhNI9rYXiTBHKS6Qqz9Aq0Z8REK3TeV3DdnQ44R_ChlMRbEhQx1VqHmPRES2BQm1sYMQb5cEkTDUhA1MriDV3WagxWhSPpSCKGy7E_OBIufgvsQOJOfRk1z8Y_4-7VRs" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/85455aa172.mp4?token=D8rmm8ktWsm-Vq5hslzIFUQmFae3PP1M9DXD715m34iO3q22SNdWRI-Egb9rTJVjHXr5Nlo8t_1UKPNS3cjCVpsz_FetFAx8ZzuMB6pRd4SGOqeoaO3sArUn7rxiaf3c6E_a04ljvBeCYk8QA1VSN4GLEe1PkB1NHKgklY1UpkCDocgoFYwRpgw3q3iHu4a887lzwkgf4PEM_8cfBL3rJEqGHyA830Jq5bPkpZXh4ZCoe3cl35_y0IS3hHviGaUaDqXrwih_yOnr_AaYsNcTm8j73DjR-kBmLPJwbQ8F6ocDmAVo_r4WGJofVY7qu2FzMLIMOrvSCiNW4O07sfurFxS6UORND4M6jk0AslIsfMsfNXbwxROVCYaCO7xJ6aebmwhoIO_n_X1i000co0YwW2vHD3vy7dgYTKwYIQtCEXemQDoq-20W0HDrq6nB_6C8087uVBJdGHhM9IrBOS0s9gA83IcyRrP739o2YEkAaVsTDn1XljJmzbIkJff4xci-9-EO32vV7ZS88hdgvsHlhmMLkU5-bZ89Pfr83IEXaIgYhNI9rYXiTBHKS6Qqz9Aq0Z8REK3TeV3DdnQ44R_ChlMRbEhQx1VqHmPRES2BQm1sYMQb5cEkTDUhA1MriDV3WagxWhSPpSCKGy7E_OBIufgvsQOJOfRk1z8Y_4-7VRs" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👀
🙂
ابوطالب آماده ورود به فساد فوتبال
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/Futball180TV/107657" target="_blank">📅 09:01 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107654">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/Futball180TV/107654" target="_blank">📅 01:20 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107653">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jKI08MivWTWx_meCgMpUSKE2hh05gWZ8b5VTSYgmwQMlX6Jm1OrSqrcqDsPc5uZJ9lsJqqsbXyCwgkQkSs70avMeYtrvPeeQD3PjhHNixv8n8bSfQW9cAFJzjdcO3wKPJ8Gta3lePypy_OxhqUu4qmxntMhcVLBbplkYBRP7byHc4A2Ja7y702GeHTzf_Yybn5JEpqGEinlbMBom_LdWWN944-IC_tbUBl7JQheHCTFCUWWffEnWlCmgh6kjzBQTI0V-81RvGyKNf5WEElJy31degI9vlrfCb-T4_IL7h7P-ygSYOWNyDRmkvrC-w95Aq2YD_pIPm3bXlpBQfK-UCA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
‼️
کنایه ژسوس به رونالدو: خوشحالم که گروهی از بازیکنان را دارم که به ایده‌هایم احترام می‌گذارند
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/Futball180TV/107653" target="_blank">📅 00:53 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107652">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/URyNP9NFD64NVbx5Np3OqGYLHdvmN9F0WVNtPBmxA-QMwEPcZJJXfEQiU7toHnqe4SxYbefZE2CLeE9aci8HpJ-D8OjWeU6Zl8Z6x_j-hsMrkws5fU31VJa5_6ohv4hhSZInP6RcWBxXw21RcyBV8mQ0U19XtAqT71Mxj8rifBKzXqu3zu0FkkZ_DhNUEaO6CsBAlqtOHA6ufTO-FFtbqNGHDJbLQDwz7nSEtv5AX1WzJJrttOc2Q3-Xc0s32MvLyUWNM1100TwIBCXqDP0R6IAtpn4UAiDbvOgXFcJQ5VExVZtLIpeV3yaMNULItcHs3ZOWywhAyLMS_vl3Lsvt4w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
‼️
کنایه ژسوس به رونالدو: خوشحالم که گروهی از بازیکنان را دارم که به ایده‌هایم احترام می‌گذارند
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/Futball180TV/107652" target="_blank">📅 00:45 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107651">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LzODLpAOEJEdrhJFvauTmYyCxQ8lVUEWOP9-Ri-SA_LE7Oh9GkBBD10p6tmunaF4CT775NSpG4o5CVqQCUPP0wuQkwDvsGYdetVSAJRO3OI9IyquQdtyxHl4x4-tJKhgg2goEnctLZojBDOcG9NJTrtArd9ESba_Gz5qsQwb98mhmzccPk-zmIPwXs6X0Tcbmzz_S5vGmrGF7bsSr24FVsabx8TAuvmG-_OWPZIn3n4U6Yzx_3esOJYwfF4v7MS50ggiB-f7NWdfSaLjX6pluGqqeeh_dFGwSfuuOgv09Lnyo2n-o3GrPncH9-dfnA-kkQeBKay0T5gZ-kgSsQMRBg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
📊
عملکرد فِلیکس تحت رهبری خورخه ژسوس در تیم النصر و تیم ملی پرتغال:
🏟️
50 مسابقه.
⚽️
47 مشارکت.
⚽️
29 گل.
⚽️
18 پاس گل.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/Futball180TV/107651" target="_blank">📅 00:22 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107650">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/44b6b9a87b.mp4?token=HbA12KfBbZdmb1x6z63gKPsavAlvrCdUzqAGMyZ2WkgRVMYmdYJEmkXSwHIuxTzDdKXUSoEPSfAzk1Q5D48rxMX6Yo3seKRUltZKPx74IDak61s7qr8PloGbYzmipDX3xj6ZuUrWJOH_TZyHfBBRtWexN6rSNUQP6Rxpawcv80Rn1_Xog8SNsXprPRrlNEC8S68MhOsaoITQJsShSgrLa_icI4NUuGifhSF1a5sIGCOTnoV4Sna1VtW6mXg7Vv7c-xdBVyKUp_Ahh44MQDzefDPYHvSzeIiwtlUu6BZZCyqBbmYUZF7xq0ElHHEQ5fON7CwF-y5WtykGVggr6FPetw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/44b6b9a87b.mp4?token=HbA12KfBbZdmb1x6z63gKPsavAlvrCdUzqAGMyZ2WkgRVMYmdYJEmkXSwHIuxTzDdKXUSoEPSfAzk1Q5D48rxMX6Yo3seKRUltZKPx74IDak61s7qr8PloGbYzmipDX3xj6ZuUrWJOH_TZyHfBBRtWexN6rSNUQP6Rxpawcv80Rn1_Xog8SNsXprPRrlNEC8S68MhOsaoITQJsShSgrLa_icI4NUuGifhSF1a5sIGCOTnoV4Sna1VtW6mXg7Vv7c-xdBVyKUp_Ahh44MQDzefDPYHvSzeIiwtlUu6BZZCyqBbmYUZF7xq0ElHHEQ5fON7CwF-y5WtykGVggr6FPetw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇵🇹
گل‌چهارم پرتغال به دانمارک توسط ژائو فلیکس
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/Futball180TV/107650" target="_blank">📅 00:05 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107649">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">گلگلگلگل چهارم پرتغال توسط ژائو فلیکس</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/Futball180TV/107649" target="_blank">📅 00:03 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107648">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4bbdf1dbe2.mp4?token=PHc0fGcB9ukdCiCaUsJxf6EYD2-bFh4BWcZUhrDRSUWSflDVbPrJt8grbI-0py_hOumEfi-zZ_UuzS0RLJOoZoYkeGFOTc7PDUyeplkHdtEfm8VYd9VIDF52kBVSFUvCeNr_-jQkqWTtdu2_fSi1I7jm0x9Bm4bjhNP8p0EOhENzt6A8a6N26E19XNj2NKdDZf_OqSJ_E8I6CAzqiNTwE_znkTjfxpYMqHWiCp3WDysdZW_l52GBS3ej85DtZnII8tAu6qd1ef-gqt4Dud4m5P5yA0th26y60MwGsJee6DudfM5G7qVhWmR_kL06WXQkEcqK4liRYRrLjcmlaI1RsQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4bbdf1dbe2.mp4?token=PHc0fGcB9ukdCiCaUsJxf6EYD2-bFh4BWcZUhrDRSUWSflDVbPrJt8grbI-0py_hOumEfi-zZ_UuzS0RLJOoZoYkeGFOTc7PDUyeplkHdtEfm8VYd9VIDF52kBVSFUvCeNr_-jQkqWTtdu2_fSi1I7jm0x9Bm4bjhNP8p0EOhENzt6A8a6N26E19XNj2NKdDZf_OqSJ_E8I6CAzqiNTwE_znkTjfxpYMqHWiCp3WDysdZW_l52GBS3ej85DtZnII8tAu6qd1ef-gqt4Dud4m5P5yA0th26y60MwGsJee6DudfM5G7qVhWmR_kL06WXQkEcqK4liRYRrLjcmlaI1RsQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇵🇹
گل‌سوم پرتغال به دانمارک توسط ویتینیا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/Futball180TV/107648" target="_blank">📅 23:46 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107647">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">گلگلگل سوم پرتغال به دانمارک
ویتینیا زدددد</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/Futball180TV/107647" target="_blank">📅 23:43 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107646">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">هلند گل مساویو به یونان زد
😐
😐
😐</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/Futball180TV/107646" target="_blank">📅 23:41 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107645">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">‼️
وضعیت هلند تحت هدایت ژاوی جلو یونان!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/Futball180TV/107645" target="_blank">📅 23:39 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107644">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/37b7e5010a.mp4?token=SlbykGFvYFEXfnH3-qwQ1y-VHdUAaoALDactUgz-swsPcFcf0CXQMQuORoxcmtucYSghF4E5zaFXuNOYTWoJ7tRZNpL8323nORz2tvfsJW67Re08UBMU1q7E4ZMaW8BxeYfcnek_69mqQByG_R1VZEgpvIkqmm4ZCRYQwkM_PbYwy-EM9nTlc4BpAA57xyUeuVd44bQcqD_nFMb62NhqQ8FKwjIuiy7cZzk9KoaxANDlFyL9dN9olIyqByU4pEY--aba-byFhjr_D3D8vJ_4snNglXGVtrpggAam_8LXsuAJkJwbPEOGn3cZ1nu92otM0_7VuUwZwXfIkYy23TMl8w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/37b7e5010a.mp4?token=SlbykGFvYFEXfnH3-qwQ1y-VHdUAaoALDactUgz-swsPcFcf0CXQMQuORoxcmtucYSghF4E5zaFXuNOYTWoJ7tRZNpL8323nORz2tvfsJW67Re08UBMU1q7E4ZMaW8BxeYfcnek_69mqQByG_R1VZEgpvIkqmm4ZCRYQwkM_PbYwy-EM9nTlc4BpAA57xyUeuVd44bQcqD_nFMb62NhqQ8FKwjIuiy7cZzk9KoaxANDlFyL9dN9olIyqByU4pEY--aba-byFhjr_D3D8vJ_4snNglXGVtrpggAam_8LXsuAJkJwbPEOGn3cZ1nu92otM0_7VuUwZwXfIkYy23TMl8w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🔥
چیپ تماشایی هویلند مقابل پرتغال و به ثمر رسیدن گل دوم و تساوی دانمارک
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/Futball180TV/107644" target="_blank">📅 23:33 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107643">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lt1CapOWs3Rc5k2rBqSsb1CdxmrqIM2sJZMx0x8kH-zCTrF3lRgcvvF6nnDqeE2EjHMkNtC7mwACSQ7zGoX63PtpcXP6r4RZk2xuTGw7lgu0dK248vd1QF0S0pPt74PG4uOMrM89G9yhZvVP1LhXbpftC86AVjAyn5ayTccib77Oi4rsVFfvvgSiD0CcMMKEvb1Aq7wlrYJFmWChV0GZzuNS4PF4bXliIlCmY-SXh2e5T1gBD_vHZixD55aL2KEvs5uEbpEFFPJlW4Y3wDZZf7W3tkkpU_AZA8bOYkXbEnJXb5mGHmqsXOIGQx91iHCij5rrylp-D2e6B4JZi5seIw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
وضعیت هلند تحت هدایت ژاوی جلو یونان!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/Futball180TV/107643" target="_blank">📅 23:06 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107642">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VwI6zARmkeQh-OuZnuoTXke6UeA6-diZNqPjedAKMVenU1WAfAjfYNpLR5kFjpfgyh3y434j0lNGkowxxsjtj-HkcDa_dTKFIYUcWqqBXiUr_t1pqL4L4OP0gkw_yDdUUFDsl6WCIoxwDoWM0QIzxUvQdhCUApybQlmbZ-jvFnJ4Y6PDF5sqWxwPZnQujVgKkDAYKmktuN-yguTIgSwGu5ihxHt0MMrXZMwrwYVxtkYTwNgNU-y3uos6PzwLjWU0K6YzTkDKsrNj9dD_ETGeHr18E-dRHVw4kQ9sAhcDhqWBl5MJGT3dhFOrRlN_dWl-xv156U7clifNyVj9eM7aiQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🛍️
فوتی هدلاینز :
🔻
آدیداس قصد دارد در سال ۲۰۲۷ لیونل مسی و لامین یامال را در یک پروژه ویژه کنار هم قرار دهد؛ پروژه‌ای که نماد انتقال مشعل بین این دو خواهد بود.
♨️
همان سال ممکن است آخرین سالی باشد که مسی کفش‌های اختصاصی با نام خودش دریافت می‌کند؛ در حالی که آدیداس آماده می‌شود پس از بازنشستگی این ستاره آرژانتینی، لامین را به چهره اول جهانی این برند در فوتبال تبدیل کند.
✅
انتظار می‌رود مجموعه‌ای ویژه با نام «Messi x Yamal» عرضه شود.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/Futball180TV/107642" target="_blank">📅 23:00 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107641">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/069b82ea6e.mp4?token=UVFy3t2i_GNAtmUx4CUNXQi-Mp4ADNsUHfJO2GaCJI5PW1DDO9dNlgrr9gGVz6X3aJSAJE_W6ZNpXqKtlcrVcjlxP7lqOKjWgLQAeTzVzEy1PGUKKq1y0xgdF3q55ifRk7NQps4nDdROn-fpCxD5MA08R4nOOmTQy1n5vPGnJq6dmhIB8EG8z0tMhaaljZgzoQ18w7wC9n26mXr9EP_cW-WNYZwwm6fDh9_bO2JXYxefGzSyMo1tW47kNBYWAswUb8vV_W6Lt7HpQSShH1tjtWHsUycHV5SF1fBW6S62Td7iJubx8zpwI39hj5gmAbwqpBuHd8EV-y8lZd89xWE2-Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/069b82ea6e.mp4?token=UVFy3t2i_GNAtmUx4CUNXQi-Mp4ADNsUHfJO2GaCJI5PW1DDO9dNlgrr9gGVz6X3aJSAJE_W6ZNpXqKtlcrVcjlxP7lqOKjWgLQAeTzVzEy1PGUKKq1y0xgdF3q55ifRk7NQps4nDdROn-fpCxD5MA08R4nOOmTQy1n5vPGnJq6dmhIB8EG8z0tMhaaljZgzoQ18w7wC9n26mXr9EP_cW-WNYZwwm6fDh9_bO2JXYxefGzSyMo1tW47kNBYWAswUb8vV_W6Lt7HpQSShH1tjtWHsUycHV5SF1fBW6S62Td7iJubx8zpwI39hj5gmAbwqpBuHd8EV-y8lZd89xWE2-Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇵🇹
گل دوم پرتغال به دانمارک توسط راموس
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/Futball180TV/107641" target="_blank">📅 22:48 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107640">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/753494da36.mp4?token=ed_MoEmnDH5NndHrBpkt0aXWd9zr3ynBUKsnnPzmtLcWsm519r5BrkJ0re6uDDxl2JQCa4measwLy3qnhOZT66anLbkXrEpzCnqLeW8g1K1VfXxN-I8X5QT3S9u3FdaTFNuWi-1saQp2v_mkc9BI95d7WpyhXdu5ubycvJK4RGIs4dj4TLwHYlQ1TWVFDdYeZZPhdNJvURxjVbchPy8sF5RZLGskADtvFFsJtMZ-LDhvUBmsVin4ajLMFamWcNsGRkujq6IxZ_WARQxx0ubMn_72hYFgpz3ythmNDkx0ewn8RBtKZ3n7nEakRXQb5ElRWVg_BzNAEQ6OWDtZCzSvbQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/753494da36.mp4?token=ed_MoEmnDH5NndHrBpkt0aXWd9zr3ynBUKsnnPzmtLcWsm519r5BrkJ0re6uDDxl2JQCa4measwLy3qnhOZT66anLbkXrEpzCnqLeW8g1K1VfXxN-I8X5QT3S9u3FdaTFNuWi-1saQp2v_mkc9BI95d7WpyhXdu5ubycvJK4RGIs4dj4TLwHYlQ1TWVFDdYeZZPhdNJvURxjVbchPy8sF5RZLGskADtvFFsJtMZ-LDhvUBmsVin4ajLMFamWcNsGRkujq6IxZ_WARQxx0ubMn_72hYFgpz3ythmNDkx0ewn8RBtKZ3n7nEakRXQb5ElRWVg_BzNAEQ6OWDtZCzSvbQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇵🇹
گل اول پرتغال به دانمارک توسط کانسلو
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/Futball180TV/107640" target="_blank">📅 22:33 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107639">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/95be3e3e74.mp4?token=EfhE0YRZpBtowZd3X_POZYGuqW6k39YxbgU1rg9PKqNEs46DXcXioxtkhlCh4uCefVlQNYyvZ_dIImeubqwZB1wPyHJgUuWZkfuHGKnyGsH_fY20DJAewOc4EGkDPwiMfiPau4aRXJ9SL6A8Ap9D6XGMhUm7rcrmZAXRCRfAtgP0QjiFmOZSDPOvCuWz4NQPZllLQcs-93170-bII31ZNQuBoDpamOQQk69JAs68IbSywDb59tjZWqbshAyqMCSnO0_i1D1QkYQ38wklYZ40UrO4qIjahFZFuPTn5ix-JpQrpWUXuU0ld8vM_K3wLer-21YxZSVx2-wcsseL7T4JFQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/95be3e3e74.mp4?token=EfhE0YRZpBtowZd3X_POZYGuqW6k39YxbgU1rg9PKqNEs46DXcXioxtkhlCh4uCefVlQNYyvZ_dIImeubqwZB1wPyHJgUuWZkfuHGKnyGsH_fY20DJAewOc4EGkDPwiMfiPau4aRXJ9SL6A8Ap9D6XGMhUm7rcrmZAXRCRfAtgP0QjiFmOZSDPOvCuWz4NQPZllLQcs-93170-bII31ZNQuBoDpamOQQk69JAs68IbSywDb59tjZWqbshAyqMCSnO0_i1D1QkYQ38wklYZ40UrO4qIjahFZFuPTn5ix-JpQrpWUXuU0ld8vM_K3wLer-21YxZSVx2-wcsseL7T4JFQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
برونو فرناندزی که خیالش از بابت کاپیتانی پرتغال راحت شد و به خیال خودش از شر رونالدو خلاص شد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/Futball180TV/107639" target="_blank">📅 22:33 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107638">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">ژائو کانسلووووو</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/Futball180TV/107638" target="_blank">📅 22:31 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107637">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">پرتغال زد</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/Futball180TV/107637" target="_blank">📅 22:31 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107636">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">گگلگلگلگ</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/Futball180TV/107636" target="_blank">📅 22:31 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107635">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">یونان یکی به هلند زد که آفساید شد</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/Futball180TV/107635" target="_blank">📅 22:29 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107634">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LS714yMZMMihaVaFJ_zmKZL2ueo6KXGGAAIhISqSih1QquopB3wFWNVm_qNpQw4yYAZWP9HCQmJvpbIehrH-qEBv2ijSfHH3A2UroVGuQXPet4k_41KV7Tx6uDYlBemW0fxWDRR2aUN4kmc-aJbvdbsLZprEnhJ7tC35VyWFLWv3j5q0iT24xMwifQ5RISd-QpMvWuZKsw60osNtA2TNuAtV71yEpb9qjcUGKhBeLkeHBrXqOEcp2kkE1GswqTbFLBdwGdUclg49v_BUe_N4yCaX8nxLKTTygXRXLyNMcEjipEifTE1drr7G0aL9CLEnZjtnIg_QOCsCJGYOgT0BtA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🇪🇸
شبکه رسمی رئال مادرید:
🔻
کارنامه آقای گواردیولا، آقای ژاوی و آقای مسی، همگی زیر ذره‌بین و در حال بررسی هستند
🔻
تمام جام‌هایی که بارسلونا بین سال‌های ۲۰۰۱ تا ۲۰۱۸ به دست آورده، زیر سوال رفته و تحت بررسی قرار گرفته‌اند.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/Futball180TV/107634" target="_blank">📅 22:16 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107633">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/v7etbTd50BT6es0ModNbm2h6yvaxOW1kPSe3708e12hRzD5z-Bxw6Hv7L5GCFHclmImLAU16BY80Qcx3GdibJHB8gzxf47PExtXxcUV39DDFuOYi_TovjSDqr8snyFyHIJINJquaXoVv5bLE9dfaY5RKdgdZoEiX5ec8AyvrzG-5Ezqi7ZzM7mvSuf0GWAjDe_Cah6dpQedPe7gVoYTJDgZLIMx9mLxnIMSagEnnNXL7G455L9T_PGPTL7Hi8pNxhBrQ1K3Flc0dEAYuO0-CoY66I5qWiDV57yUtLljkbx9E6gnlXFBtmePOI43rpVFly_RI0r0GUFShTkajtkwTWQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
👀
🏆
باسکال فِری، رئیس سابق تحریریه‌ مجله فرانس فوتبال و مسئول سابق جایزه بالون دور:
‏
🔻
در حال حاضر، و با صراحت، من از لامین یامال کمی تحت تاثیر قرار گرفته‌ام. و شخصاً، جایزه بالون دور را به بازیکنی اهدا خواهم کرد که قهرمان لیگ قهرمانان یا جام جهانی شود. این دیدگاه من است.
🔻
یک نامزد، کمپین‌های انتخاباتی را در تمام روزنامه‌ها و به زبان‌های مختلف انجام می‌دهد، فقط برای اینکه بر رای‌دهندگان تأثیر بگذارد. اما من با روزنامه‌نگاران و رای‌دهندگان صحبت کردم و آنها تأیید کردند که این موضوع اصلاً به آنها خوش نیامده است.
🔻
این بازیکنی که من به آن اشاره می‌کنم، خودش را به عنوان "انتخاب شده" معرفی کرده است و من فکر نمی‌کنم که او این جایزه را ببرد. و اگر برنده شود، با وجود اینکه من این را باور ندارم، این موضوع برای آینده این جایزه خطرناک است و باعث هرج و مرج خواهد شد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/Futball180TV/107633" target="_blank">📅 21:22 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107632">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a570eeee2d.mp4?token=YT9AQaKSEzarKjMuiyMkSLMVdplIMb9ujcezrE1XfS9iJ9gpQxVHxm2xOzxsyehZIxhB6QXRtQj5DEwPCzAeykhbRTlbddMoUySjP2Wo89d0HSIWJqDjj48XjqN_4u-84o0e-vbwmeCgAaRBwV8LNmdUPvSdwvjKUoGlcFPdqYbXkk9C-hP6wZp6f4omIp8Mh_YG7DyhZEQm7u2LeuiwsHafYqbhXW3W2osW7RD7QBuL5Qs_lOoj9hKtcLNcb57qJzRDKlu-PEPOuzrg6kcnd5dqVJl5vDwBjSkq_yjhGCgk9VAxFlLxmV9wSC0HJRkyelF8G0QXmCkJmx4ED7f9_w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a570eeee2d.mp4?token=YT9AQaKSEzarKjMuiyMkSLMVdplIMb9ujcezrE1XfS9iJ9gpQxVHxm2xOzxsyehZIxhB6QXRtQj5DEwPCzAeykhbRTlbddMoUySjP2Wo89d0HSIWJqDjj48XjqN_4u-84o0e-vbwmeCgAaRBwV8LNmdUPvSdwvjKUoGlcFPdqYbXkk9C-hP6wZp6f4omIp8Mh_YG7DyhZEQm7u2LeuiwsHafYqbhXW3W2osW7RD7QBuL5Qs_lOoj9hKtcLNcb57qJzRDKlu-PEPOuzrg6kcnd5dqVJl5vDwBjSkq_yjhGCgk9VAxFlLxmV9wSC0HJRkyelF8G0QXmCkJmx4ED7f9_w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
⚠️
میلی گلد این فیلمو از طلاهاش منتشر کرد و گفت دزد نیستیم و پول مردم رو نمیخوریم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/Futball180TV/107632" target="_blank">📅 21:15 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107631">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BgNhzieP6qt9ulZP1wNl_di7RxgVJGAtX2mP_qmo2TVZrEZX_OpIlcqffBp95IFRvU-J_70nyKYcBTQHLcGyRYuy--OK7f7bvRa9NcUPT2byyu0ooKUJ9bEncZLcpSNcCkvG3CC8bYX61Ehk_LTR-BZHUePYzVGCrTLPeRumBuPOQ7LKmrQSfSyxbZDtbRDwYhxkMA_067DRFfzu3szBPGnFQMnqiKye97PilJLWrduKuRIVMIsZ8SxiVNeqlvVl7CG-0fib0lyUlW-XEDmirSTOplPHeSvnjkmmvLbu5xKnM-zEAAY7ZLsj-IhDC3p9DzwKPPCdzxAwG6Oq2C4llg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇩🇪
ترکیب آلمان برای دیدار با صربستان
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/Futball180TV/107631" target="_blank">📅 21:13 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107630">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">🚨
🇵🇹
ترکیب تیم‌ملی پرتغال مقابل دانمارک
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/Futball180TV/107630" target="_blank">📅 21:12 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107629">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uFkgFzAZN85qQ35EY4jDpIwg44t0S5K89vM7hvXcXChOnSrkm77pv8EZUE_u1rs4OYM7eJVcQ9AUSIRf4MNRfidLsjmr2bXH8jXzNxLRUB8nI0Oj765RBSLMtNzhkYE2PipHt6ALHvUCEmc82AfkYRV8AdH2WtheCmr95VP7KeOsygx1mOQiak0smcbUP0EF2jmVNtfX3DrIA83ww-Z_bqzF7vf-OVW7KA2noZJKJzUa04dq1oMYw0SdebchyhTiUx8uJLvoeLHE9msoMLlr4SWGJ0PhhTF-dU2YfFEHf4_hg8LaFEL5x5BFbU6DXPkj9R-0CL9fWyvPzJRTln26xA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇵🇹
ترکیب تیم‌ملی پرتغال مقابل دانمارک
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/Futball180TV/107629" target="_blank">📅 21:10 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107628">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eLDBWd7NR98-xm0KaAP2QzGSnkIvIADK7EN5vrcZlt5ndV0DV9xEour5tscRlH0kDlGySjzbcJn_Nl46FW7R0FGUhupcKH3dRNvrP3IiTj-qbWSohQufo_DeLXPjBB9CQDSTZt3s4XJK_mJzyaF_yt-kQGiJ2S6ji8CCADhzP894jlH_nGCj7iqYqVcFnKxYKagj1g72vqP2HnguTVvlDm1xodW74R3W-y-P37wiVsnHcthHtW2Oa3WV9lY3hDlIfvEmXHzeZUDtu1MkCraKvdqc0sdBNedLJO-MqMzDYzg0S86qmjSQS_j6N3_JC5-Mbe02BZ7i3w8IV3w6I_f1qg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
✔️
لیونل مسی، مالک جدید باشگاه اسپانیایی سی‌دی الدنسه شد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/Futball180TV/107628" target="_blank">📅 20:33 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107627">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f1b37d3dc9.mp4?token=UxwKcq1-P_u-f3ZxlkmkJUkdUxkWoWXjVP4jntGFZqQqPXCwHJbn8swrDSm_qurdGtostg7DyAPRe0qiejrTtcj3d7MTUImPiNsLWA3tRl5Vz1F0ySX2lmLe302clqj7LWPUREwu9f27sGGdtrJUJJQXwKzCIJsRqWZdYBv1NtdOOjvZlSDh-3WICeJOtVBho51n713D794tKjJnPn8U2wCSZXUuI9qyqnMgQ6lSOBXN892cpBMS-3rIm8d8KI_petVO4De8JGdNJKBAOFFoCnjH1I0W1uAQYA07QUzGTvnsrC_S5i4h7wRl0ult7q0SKRcfkLUgDcvyJv0nBphhWQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f1b37d3dc9.mp4?token=UxwKcq1-P_u-f3ZxlkmkJUkdUxkWoWXjVP4jntGFZqQqPXCwHJbn8swrDSm_qurdGtostg7DyAPRe0qiejrTtcj3d7MTUImPiNsLWA3tRl5Vz1F0ySX2lmLe302clqj7LWPUREwu9f27sGGdtrJUJJQXwKzCIJsRqWZdYBv1NtdOOjvZlSDh-3WICeJOtVBho51n713D794tKjJnPn8U2wCSZXUuI9qyqnMgQ6lSOBXN892cpBMS-3rIm8d8KI_petVO4De8JGdNJKBAOFFoCnjH1I0W1uAQYA07QUzGTvnsrC_S5i4h7wRl0ult7q0SKRcfkLUgDcvyJv0nBphhWQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
اوضاع فوتبال ایران با این آدمای لجن!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/Futball180TV/107627" target="_blank">📅 20:15 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107626">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d318c00047.mp4?token=sU0X1Y6ASixMfB2t3XW8rJ5gj97vjXabeR1oqNqnnoq7laKlqAqeelbQe5h65NxMSLkKex7btW4ljNcn_dA8ly9kBkW8ldzFx-Djstt61GCPyC8cBU_a1vUJS65yGLuIOqBcv4_dEIgFgMkMuhTkqL2MnkWGmpSRy3-ectXc7SnPHaqJaxlRURfcu2pi0pfgZe_SmOWFzA_kazqU-6YjhRzOfoTAMv60y0ah0lx1lDE5azkYqUy2wFhSPFWFLtJPY4OWfi1ykn7Zt7zT3P_q9OIbQ7uajZzvHgxeqT6r7JLPpBrR-qf8P0_MCAN9Ps0WsGScLgvJT8pgK-9eYLZImg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d318c00047.mp4?token=sU0X1Y6ASixMfB2t3XW8rJ5gj97vjXabeR1oqNqnnoq7laKlqAqeelbQe5h65NxMSLkKex7btW4ljNcn_dA8ly9kBkW8ldzFx-Djstt61GCPyC8cBU_a1vUJS65yGLuIOqBcv4_dEIgFgMkMuhTkqL2MnkWGmpSRy3-ectXc7SnPHaqJaxlRURfcu2pi0pfgZe_SmOWFzA_kazqU-6YjhRzOfoTAMv60y0ah0lx1lDE5azkYqUy2wFhSPFWFLtJPY4OWfi1ykn7Zt7zT3P_q9OIbQ7uajZzvHgxeqT6r7JLPpBrR-qf8P0_MCAN9Ps0WsGScLgvJT8pgK-9eYLZImg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🔴
🇷🇺
پوتین:
اگر حمله‌ای مستقیم توسط ناتو به روسیه صورت بگیرد، از تمامی تسلیحات متعارف و غیرمتعارف (بمب اتم) علیه آن‌ها استفاده خواهیم کرد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/Futball180TV/107626" target="_blank">📅 20:02 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107625">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6d8054bb57.mp4?token=gzGdlLhCHs1lmnUZtFOL_f5SKPfy1r2pNt1txJ0vy7-DiJUY5yOKpCYRqTeWXYsm0xgAwEdsnqYKGd9efBYtVokNkyx-Cr3bdh-qmuIHDn3FJzlzlATroqoMe62z7VXPOUy20nHImt737DOcOai3eQSCQO5ejunjjgfQki-Cns_RiN7Z8l4Gzv8HR5Zu6DfSZHllFuRTQfYO4raZlZNcEtMBaLHrNAXwB6xfy7Q5q60lxM8Xpna99HVGSSQioCwHB5cA4kr5Xt41BnivcYFNcG_ES4JMOOcAXFzK6Z__4McMwPqpbEsETHaO2D8oKMuWucMgnAIgiZjGrrD8p4Lqqj8WtdoG__jXy5GKrMNCovgqliSsFdXDYD3Av8ZymbBNcNHcMFr3damBzAReHUGIwsNiPHsU7wRM2za8DtNk1SzdHCOKnCvkBSWczhr0hWPicfL7rxY6fBqWNeXngEAmjYIAx4KtEJc_whlWfTxed8dO06Ar2qVc6MHgZ-4QzIKdjhsn2leoqKg50qBV89AT7H15vTXWw6GyvitMdsStJryr5_lZzZvuaqMmYrEa55m3yQ-z-CgUZd2RIJ--tSM0Xes4v1JvADSn20bA4kXdKDmfuuctzSWKaFJcljjXLrQmgeLJxGidfTNxT_OaUmfPRxfLmfC_xMUCkSSVqTQijvk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6d8054bb57.mp4?token=gzGdlLhCHs1lmnUZtFOL_f5SKPfy1r2pNt1txJ0vy7-DiJUY5yOKpCYRqTeWXYsm0xgAwEdsnqYKGd9efBYtVokNkyx-Cr3bdh-qmuIHDn3FJzlzlATroqoMe62z7VXPOUy20nHImt737DOcOai3eQSCQO5ejunjjgfQki-Cns_RiN7Z8l4Gzv8HR5Zu6DfSZHllFuRTQfYO4raZlZNcEtMBaLHrNAXwB6xfy7Q5q60lxM8Xpna99HVGSSQioCwHB5cA4kr5Xt41BnivcYFNcG_ES4JMOOcAXFzK6Z__4McMwPqpbEsETHaO2D8oKMuWucMgnAIgiZjGrrD8p4Lqqj8WtdoG__jXy5GKrMNCovgqliSsFdXDYD3Av8ZymbBNcNHcMFr3damBzAReHUGIwsNiPHsU7wRM2za8DtNk1SzdHCOKnCvkBSWczhr0hWPicfL7rxY6fBqWNeXngEAmjYIAx4KtEJc_whlWfTxed8dO06Ar2qVc6MHgZ-4QzIKdjhsn2leoqKg50qBV89AT7H15vTXWw6GyvitMdsStJryr5_lZzZvuaqMmYrEa55m3yQ-z-CgUZd2RIJ--tSM0Xes4v1JvADSn20bA4kXdKDmfuuctzSWKaFJcljjXLrQmgeLJxGidfTNxT_OaUmfPRxfLmfC_xMUCkSSVqTQijvk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نتایج بیلدآپ کردن امیرخان در تیم‌ملی
😐
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/Futball180TV/107625" target="_blank">📅 19:45 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107624">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1ce141f49b.mp4?token=LBSH9frhlU4HiqQJh60MPVHX7tHYqBR2O1Fh911B1e-kqwk96vQXirWpna3UpL_oCtGpFTYtpYEBxPZcGOKmZwMxxz7N0Agwbr7ZinDwgNXPAmsog56SwpgdUPX7AHXB-W9RiWH86rnIH5X9Tj19_-uJF8LNdTGogdbMSC0ucUwj5EbDOsVUQCnwAc8O-cTI0G4PqFy93A1HTHmZDYZwOtEVeMwOIgwaZym4Arnc7yRzPqL_JrUTEa68Xrrexz_wgpIjRg2eCGggtiU8ailL4k_Lho-Q_n21VBaBVZE2ozNg71PBpjbie_8l3gD7La0gSQM0mCY-zz4_eIuw7_WtaniznbOJD56FZ1z-lnpZdQ8vMe6DXewbHPPhyUGUWhEaMXrsM9seJzw4jvPMNhex06LQhre2QSWwwKtCDX5N6YUMpFplLMd3UeRWY061IpXQrK9CQkSKv30xUgxR_PIT2w_VX9ZcJ_LSt9Ty5XTgBt1kYDgIZbKqzakG8IpcI_xeMnkUoK_mUM1iiGgJvH7KUSnJbECMjc1q2YX0S5G_rTi6ytZgEpUSrNiCEpm1CnrfJM6QQkpyc2iXO7gnuCEAyTEKtv8_-LpYbIgSIU3jJ2Cl4t6ikwDFX7wX7QQ5qdzl2sd8f_4oFMaVBAzahaiF6OlVWRe4NYaozqnOOaBM1ts" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1ce141f49b.mp4?token=LBSH9frhlU4HiqQJh60MPVHX7tHYqBR2O1Fh911B1e-kqwk96vQXirWpna3UpL_oCtGpFTYtpYEBxPZcGOKmZwMxxz7N0Agwbr7ZinDwgNXPAmsog56SwpgdUPX7AHXB-W9RiWH86rnIH5X9Tj19_-uJF8LNdTGogdbMSC0ucUwj5EbDOsVUQCnwAc8O-cTI0G4PqFy93A1HTHmZDYZwOtEVeMwOIgwaZym4Arnc7yRzPqL_JrUTEa68Xrrexz_wgpIjRg2eCGggtiU8ailL4k_Lho-Q_n21VBaBVZE2ozNg71PBpjbie_8l3gD7La0gSQM0mCY-zz4_eIuw7_WtaniznbOJD56FZ1z-lnpZdQ8vMe6DXewbHPPhyUGUWhEaMXrsM9seJzw4jvPMNhex06LQhre2QSWwwKtCDX5N6YUMpFplLMd3UeRWY061IpXQrK9CQkSKv30xUgxR_PIT2w_VX9ZcJ_LSt9Ty5XTgBt1kYDgIZbKqzakG8IpcI_xeMnkUoK_mUM1iiGgJvH7KUSnJbECMjc1q2YX0S5G_rTi6ytZgEpUSrNiCEpm1CnrfJM6QQkpyc2iXO7gnuCEAyTEKtv8_-LpYbIgSIU3jJ2Cl4t6ikwDFX7wX7QQ5qdzl2sd8f_4oFMaVBAzahaiF6OlVWRe4NYaozqnOOaBM1ts" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">همین کم مونده بود اینو بلندش کنن ببرن ترکیه با سرآشپز معروف ترک‌ها ویدیو بگیره
‼️
🙂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/Futball180TV/107624" target="_blank">📅 19:15 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107623">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WH53V_GORCfvPuDCJ8oxcYJCF-f5ugI272ne90L4eD5S40Ftb3wvm-7wQse1b-P7VIMP95TKvU61EClDok91e23X75TM0piZ1F61UMRD07Z9tb9QUAJas3pueGCt6b9zFB9p6i7nwq9a7hFGGgxQCnydWwddWEX8J2AIB9ZplXHjEkWRjyGzWxT7wxdI-nyOVwd4c5bmwxAgepyO8e9eMe-F08ToHpUe86hEd_-5Q2tVRh3ZrDQZTgO4QJbLK-AcKxUKkKXABJ6QEozXxG-brQ1qKCXpQO47VnHiF9rCbv2JHoRab-n4NgVoVJvEBlVOKam8P7w4Hkp1xEadCjDwzA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
اسپورت:
🔻
باشگاه بارسلونا تاکید کرده که یوفا فقط شکایت رئال مادرید را دریافت کرده. برخلاف آنچه در رسانه‌های مادرید مطرح می‌شود، یوفا اصلا از آغاز یک پرونده تحقیقاتی صحبت نکرده.
❌
یوفا همچنین تاکید کرده که پیش از صدور حکم از سوی دستگاه قضایی اسپانیا، اقدامی در این رابطه انجام نخواهد داد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/Futball180TV/107623" target="_blank">📅 18:59 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107622">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4a15cb946b.mp4?token=SOJ1Kea6UM84Jgw6Z3-oiI4rh-vCQ2-4FFQFGUDDQ7oJtljfNDe5PlV-TYMUF7AzYfrSuJzR92SMX7q1ogYpG3TWG1K6xUTD9I-QXueZ7JUAjOEPEuPMfVUX89UAAmSNYG_TZuTqtHGRATCL2nnEuja554BPDz7suuOi5IBWqboJ4lnuYV67sPGys_sl76t46UBjBInC6NOFi3RqWMWCtH8FbFnUDVN2SkzimHB0POIAVIzOTBhAxhDhixs3M_kUpOCKGgx9RiLZqVjmTMMJG9gbg-OEcro6aSYmXpCTXuV5cmtjrycHt9cm_2xqRd-jP6xta5ZGmE5y62MkDgeELg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4a15cb946b.mp4?token=SOJ1Kea6UM84Jgw6Z3-oiI4rh-vCQ2-4FFQFGUDDQ7oJtljfNDe5PlV-TYMUF7AzYfrSuJzR92SMX7q1ogYpG3TWG1K6xUTD9I-QXueZ7JUAjOEPEuPMfVUX89UAAmSNYG_TZuTqtHGRATCL2nnEuja554BPDz7suuOi5IBWqboJ4lnuYV67sPGys_sl76t46UBjBInC6NOFi3RqWMWCtH8FbFnUDVN2SkzimHB0POIAVIzOTBhAxhDhixs3M_kUpOCKGgx9RiLZqVjmTMMJG9gbg-OEcro6aSYmXpCTXuV5cmtjrycHt9cm_2xqRd-jP6xta5ZGmE5y62MkDgeELg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
🇮🇷
افشاگری پشم‌ریزون حسن‌روشن پیشکسوت استقلال: فصل‌قبل که استقلال در کیش اردو زده بود، ساپینتو هرشب تو هتل دختر میاورد و وقتی تهران هم بودن داخل سعادت‌آباد بساط دختر بازی راه انداخته بود و هرشب با یه نفر می‌خوابید!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/Futball180TV/107622" target="_blank">📅 18:45 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107618">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">🚨
❌
🇪🇸
🇪🇸
فلورنتینو پرز به اعضای تیمش قول داده که در آخرین دوره ریاست خود باید تمامی جام‌های کسب شده بارسلونا در قرن بیست‌ویکم را پس بگیرد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/Futball180TV/107618" target="_blank">📅 18:33 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107617">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/l5dU7-Fgl_KPSPOSAAoxEzVDY82a6_pFmJVIsUMT4NsMD5eKQB1cKEkAiOlLBPY-2yy_c1beLWDDVftZMyztgQa1Iok2e73tijUR60kq7TVDqV9b7ZJYaQeoU1eT66iVL542la7lIOLJHx1KnRY4fgMfAxzmhqG-1OdemihE6BXRcTwaVdbYSqWUCw7ScPxakj1e6S57tnnBQMsDxEoDN18PYSn52GLLq2Wctg2y9_6daJolKmzWRWy0HtkA_Sx8F3EATmm8sU-3euftta7ORMfm1gyy3SnPZ0BR9HG7T2CUGj0Dc7LLXPVfpXUkRhmkBpWJzdo0Q26wKYrrZKun_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
⭕️
🇮🇷
🇮🇷
افشاگری باورنکردنی میثاقی از یک ایجنت، عارف آقاسی، پرسپولیس و پیش قرارداد برای یاسر آسانی!  محمدحسین‌میثاقی: پرسپولیس به یک ایجنت ۱۰۰ هزار دلار پول داده بود که عارف آقاسی را به پرسپولیس ببرد ولی این بازیکن را به استقلال برد و الان باشگاه از این ایجنت…</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/Futball180TV/107617" target="_blank">📅 18:29 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107616">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Vh0naYkeeaMHKsMzpr8MYpc0zN4Ni3MVLXDapY6v5dY61ISfizg_iJ9hI3_qRKbiOD0B7Db3OJ94OjMXl9g1TgcTU0Tm5sLbETJAp3LV-NbcIgkXXSyHA_nY6NspFQvjaIB3ldyLS-PllM-bM-s0YBh8gedcT7xo_DgK-pa9EtnLXzk8F0J2tH_OlyH2zZP9yCEtKiqJwdwIpT4KUCJ7iRyylTNUWDwhUafNTAbAdJk3qDr8TNJ3Z124s43QMBXZPHACITSGSPd5YRxR0Dr6VfqV4GcTbaaYju3HvmGcs_CbwDSzArAu77Sai1utB88bzR6n9PtTpossomTXw_oUlA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
‼️
🇪🇸
🇪🇸
آاس: رئال‌مادرید بیش از ۵۰ هزار صفحه مدرک علیه بارسلونا در پرونده نگریرا به یوفا ارائه داده که برای حد فاصل سال‌های ۲۰۰۱ تا ۲۰۱۸ است!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/Futball180TV/107616" target="_blank">📅 18:23 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107615">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NASGLWj7oCMp4LC4UKIhc21NA8Ss77tJIwR1aWVl0L4bjf7ryig5BBoOwy15L3qFqRCt1vFI0F29aTItafigvBNUjo3Dva1Ri93cIdxIyXhFsoi651gkvd3WvrOAzjLDQDA93-dYBh0YNMSF1qsIWQoSlDeRQB51C0kwvqAnT0tBHPbm2eZn0F3Nz-2TyBbHp3sXcq-5DcKwcangQvtU9WxtgdpmbKUJVIZ4-m6KbBjPMpcS4r2QELxRYInUdSJIm4KrRC6CtWjJhGxnxUFW34tWysCnbPjkhj9TbVgqN6phb3VMb1v7gglKMpCI2lWowvSFbaNI5d6vMB_-OPklLg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🚨
🇪🇸
🇪🇸
یوفا اعلام کرد که حجم قابل‌توجهی از اسناد مربوط به پرونده نگریرا را از باشگاه رئال مادرید دریافت کرده.
🔻
این اسناد در اختیار بازرسان اخلاق و انضباطی یوفا قرار گرفته و در چارچوب بررسی‌های جاری پرونده مورد ارزیابی قرار خواهند گرفت.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/Futball180TV/107615" target="_blank">📅 18:15 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107614">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aL-TB-h3ERBlh-lX8_-J1Fh025b2F_7q4WdQd2tMBwl5nhYmTn27RpRwkpglZeddTViubuve3KKUyj5TilgU6AC_eZGiSVecMSc5sJp_TUny0ic5zqmW2zGyc1JW1Q9GE5PJ9volijpJ5l5fXdm4hqPu7VbeiKfwHJv1V_oI-2aI30xvCv_FUAZlWkekRss-nCaM_1j22FfVsn0uSn8Bzhrbnvt0lcJ3iHZFRV5HUaYfkxg6X6SWktuVcW_q799bOwc_g2vrlQpMYfzm6sFkKK63Ir2VZd5wS5KSDVFKl6D_jwMGmZuJ5Py7hBtPQ9Fw5gXQM_flvrhAGcSMdX6uVA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🚨
🇪🇸
🇪🇸
یوفا اعلام کرد که حجم قابل‌توجهی از اسناد مربوط به پرونده نگریرا را از باشگاه رئال مادرید دریافت کرده.
🔻
این اسناد در اختیار بازرسان اخلاق و انضباطی یوفا قرار گرفته و در چارچوب بررسی‌های جاری پرونده مورد ارزیابی قرار خواهند گرفت.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/Futball180TV/107614" target="_blank">📅 18:08 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107613">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/015e854338.mp4?token=D0KfA-QwLSNroiQ1vT7MMV5v4o4ZG79pq5Cqaljxk_6Q11L8Kcl7C0_ytamDCeX_u_ShqzgdTWx0IhBIAB_1A3mOKysVUUc3dXYy3a4_eIPUE1G6NucaEYoSvG7bFdcXHEPMG1fxlS4OK5jvXq7XZU3xDO58nfZEmQ4aQ13O-e5V2Qx8ZmSdNPLpKqa1cBUsI-J4CrMsp2NZGAEIVZ4-dnu2lr9WOocmu-SYSUgA1zr5bn-wJdiSuSiBcKpmVC9yfcfsX84dDVfLh-8u9JEhS_O6_bCb3a_xDBolCmk3WdNpcUCMqzndkvB4GNLc6tJJwdu219C-WIgz4WghcvcYDQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/015e854338.mp4?token=D0KfA-QwLSNroiQ1vT7MMV5v4o4ZG79pq5Cqaljxk_6Q11L8Kcl7C0_ytamDCeX_u_ShqzgdTWx0IhBIAB_1A3mOKysVUUc3dXYy3a4_eIPUE1G6NucaEYoSvG7bFdcXHEPMG1fxlS4OK5jvXq7XZU3xDO58nfZEmQ4aQ13O-e5V2Qx8ZmSdNPLpKqa1cBUsI-J4CrMsp2NZGAEIVZ4-dnu2lr9WOocmu-SYSUgA1zr5bn-wJdiSuSiBcKpmVC9yfcfsX84dDVfLh-8u9JEhS_O6_bCb3a_xDBolCmk3WdNpcUCMqzndkvB4GNLc6tJJwdu219C-WIgz4WghcvcYDQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
اصطلاحات مثلا تخصصی الهویی که باعث بگا رفتن تیم‌ملی و قلعه‌نویی شد!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/Futball180TV/107613" target="_blank">📅 17:45 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107612">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d2985c6ba3.mp4?token=c1qRcsOYzsXpSYNExDzolC-YCC7P3V6u1EzsLPn4HGxt-pq1QlZ5Spr6S3TD9iNLzRcfiCODSeGf3kwLf6d0yhmuGqQf7SMXSV5z_FLG2XsA2ZsClgx0tbQ1vFXFjgVAtabQ70-wNEbyTDqkCZkufQvzM9MxoVPNB1lO8gUYaJXHt7xPyAXmPeLihekzvpJfdf86HRidnaRTpq-ZAs841XzVHjPLh7MEsy4hTuCAZVQo0QOVSCLGfnd4nJxT44zMEDidgnCKJ3zUYE-ulY9NyLMJRaLaaV2-NSY0bjtR9s8ZzrpyFq9zVGKwZqjxRdwJjq7rgR-w7UxwiAdE8ygHmA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d2985c6ba3.mp4?token=c1qRcsOYzsXpSYNExDzolC-YCC7P3V6u1EzsLPn4HGxt-pq1QlZ5Spr6S3TD9iNLzRcfiCODSeGf3kwLf6d0yhmuGqQf7SMXSV5z_FLG2XsA2ZsClgx0tbQ1vFXFjgVAtabQ70-wNEbyTDqkCZkufQvzM9MxoVPNB1lO8gUYaJXHt7xPyAXmPeLihekzvpJfdf86HRidnaRTpq-ZAs841XzVHjPLh7MEsy4hTuCAZVQo0QOVSCLGfnd4nJxT44zMEDidgnCKJ3zUYE-ulY9NyLMJRaLaaV2-NSY0bjtR9s8ZzrpyFq9zVGKwZqjxRdwJjq7rgR-w7UxwiAdE8ygHmA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
🥈
اولین تصویر از رضا علیپور پس از کسب مدال نقره بازی های آسیایی: پارتی من خداست
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/Futball180TV/107612" target="_blank">📅 17:30 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107611">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e174f30bb3.mp4?token=bJdk5omvgmHMoaEKM4z9DgDw4SnV19NBZrAXNtH4RJByjU2bvI8uea-Gv2aNTNvkZ9E7EOPdhsn5U46jVmSJbhcY4EvGbcIJ06cvCftt5nOHWGthFtM4dCfiw8yhVL_vgodw4wcV4vI5CCGz3qzvVRhQTjY08K5MjDvULvC99E5PZAgrA_L84FNFBkrxoA2ji7ZDzhadleH1kNQhtW8mOzhpoZxmewlpP5UO-I4Ziog-khvFLQFX0Ri2SyfyWCouI5baT2HAGdWbeDO1dtdAjmqL9tFlhYjHbnTztEAlvYLabxbiAm5FMXfISluzoveLGvGy8RMlOp_DkEkc0CrCLw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e174f30bb3.mp4?token=bJdk5omvgmHMoaEKM4z9DgDw4SnV19NBZrAXNtH4RJByjU2bvI8uea-Gv2aNTNvkZ9E7EOPdhsn5U46jVmSJbhcY4EvGbcIJ06cvCftt5nOHWGthFtM4dCfiw8yhVL_vgodw4wcV4vI5CCGz3qzvVRhQTjY08K5MjDvULvC99E5PZAgrA_L84FNFBkrxoA2ji7ZDzhadleH1kNQhtW8mOzhpoZxmewlpP5UO-I4Ziog-khvFLQFX0Ri2SyfyWCouI5baT2HAGdWbeDO1dtdAjmqL9tFlhYjHbnTztEAlvYLabxbiAm5FMXfISluzoveLGvGy8RMlOp_DkEkc0CrCLw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📱
ویدیو جدید لامین‌یامال و زیدش!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/Futball180TV/107611" target="_blank">📅 17:20 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107610">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">‼️
🏴󠁧󠁢󠁥󠁮󠁧󠁿
🏴󠁧󠁢󠁥󠁮󠁧󠁿
خلاصه مقاله جاناتان لیو‌ در گاردین در مورد ابعاد ژئوپولیتیک پرونده منچسترسیتی
🔻
برشی از متن: شما به جای ابوظبی(مالک‌ سیتی) و عربستان سعودی(مالک نیوکاسل)، به راحتی می‌توانید جف بزوس، عضوی از کنسرسیومی که اکنون تقریباً ۴۰٪ از سهام باشگاه فوتبال لیورپول را در اختیار دارد یا متا یا ایلان ماسک یا بنیامین نتانیاهو یا دونالد ترامپ را بگذارید:
یک طبقه کامل از مردانی که هیچ مرجعی فراتر از خودشان را نمی‌شناسند، کسانی که به سیاست و تجارت و ورزش و فرهنگ همیشه به یک شکل نگاه می کنند: بازی‌ است که رقیب باید به هر وسیله ممکن به زانو درآید.⁩
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/Futball180TV/107610" target="_blank">📅 16:55 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107609">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/20411da1e7.mp4?token=lJ1o0xhDf788UF5d2fNo9JgNpNAVmeEPQlh-NUYAkO9RBhKbYoO3rRTpd4TJzmkHVBpdabm765TEz39NDzDFT7rkquwgdDKyPhv7Iser1AA_4VLuz2b5HJiIAkMeY0tdaD_mCUeluuNqIInlsPIkfIMmOOqvDAsLpTnXcjTO3GiY-wQ-_-VvcBnTXnvwbVSbocZHJDRL0WJ3YFgII5aDJU8KtJxcpVaRKW7GdIdIaQek_RaUDptkde4Uvy2jwd0i_CCVVqEJp-QeHmPRjEOJPrhxSqwYEP5D437iyQg5mO_F3FvaoJsBNScpbWd-6O0u5H8YeC4kjpAlT8M9quiRNA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/20411da1e7.mp4?token=lJ1o0xhDf788UF5d2fNo9JgNpNAVmeEPQlh-NUYAkO9RBhKbYoO3rRTpd4TJzmkHVBpdabm765TEz39NDzDFT7rkquwgdDKyPhv7Iser1AA_4VLuz2b5HJiIAkMeY0tdaD_mCUeluuNqIInlsPIkfIMmOOqvDAsLpTnXcjTO3GiY-wQ-_-VvcBnTXnvwbVSbocZHJDRL0WJ3YFgII5aDJU8KtJxcpVaRKW7GdIdIaQek_RaUDptkde4Uvy2jwd0i_CCVVqEJp-QeHmPRjEOJPrhxSqwYEP5D437iyQg5mO_F3FvaoJsBNScpbWd-6O0u5H8YeC4kjpAlT8M9quiRNA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
▶️
دور دور بیژن‌مرتضوی و زنش در تهران!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/Futball180TV/107609" target="_blank">📅 16:32 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107608">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/22a1969c57.mp4?token=oq30XbxrDWTP0Tet25RH79fdKcNtZbtj4Tvady38CvtwJaE-_llDrL6W67bsh89sh2KHMtKvfFmT8J7PygZxqvse3Z0WSjuONTLWFqPd8O_xLOhwmwIo40EepQOE0DBcpuWVkobjDm9KEU6e34XkrQ5MuOhiybeO_-lZ49tWLxbdHYFzWBxjIMDknWl8VRtdgfOfsUuLmSdKBXthfMc0wrKvdqvwCT6on-zQgy7r2B5NohkFW83ifd-nSnz3phCDbx8WhlbZOJccpUB_VDXk9IJ5xuNNJIQPALkocRgUsa6oLveJgyq9Lnpgluxg9NzoVnn_OSyk3bqkkhUJ9kBVJA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/22a1969c57.mp4?token=oq30XbxrDWTP0Tet25RH79fdKcNtZbtj4Tvady38CvtwJaE-_llDrL6W67bsh89sh2KHMtKvfFmT8J7PygZxqvse3Z0WSjuONTLWFqPd8O_xLOhwmwIo40EepQOE0DBcpuWVkobjDm9KEU6e34XkrQ5MuOhiybeO_-lZ49tWLxbdHYFzWBxjIMDknWl8VRtdgfOfsUuLmSdKBXthfMc0wrKvdqvwCT6on-zQgy7r2B5NohkFW83ifd-nSnz3phCDbx8WhlbZOJccpUB_VDXk9IJ5xuNNJIQPALkocRgUsa6oLveJgyq9Lnpgluxg9NzoVnn_OSyk3bqkkhUJ9kBVJA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇮🇷
🇮🇷
حنیف عمران‌زاده مدافع سابق استقلال:
من توی دربی که چهارتا خوردیم هم بودم.
آرش رو گذاشتن وینگر که فکر نمی‌کنم اصلا اون‌جا بازی کرده بود. حالا دلیلشون چی بود؟ این‌که رامین رضاییان هی نفوذ می‌کنه از آرش بترسه و جلوی نفوذ رامین رو بگیره.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/Futball180TV/107608" target="_blank">📅 16:05 · 09 Mehr 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>

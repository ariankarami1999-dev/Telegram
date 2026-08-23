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
<img src="https://cdn5.telesco.pe/file/QiVnFq6pQeUGCSTv6-K8IeAUwFEGF6XFGiU7uwKJ3Z-hjBoNMJ18Ks4020A-NVlDzGXbpni9vCO7PQqcbc6JcWedc-aW2hx2N4LOSUuiJL6a1Cc55f3vBPbJY0b_GC8f-9AE2gIBG4VYY0H57fup8_puLdlA05IOwdstjiNen0UlWVyEXfZUf11sBa1oT2ex_tBfBpTcOiml3fJDb_ti_Df0skIs7LMGsvYkTv4z_-M3vwlnde9JmJHgtL-x-I_HM1aGhGFsjB2pWJxbCrFIYeT0rR71EOtwyEZE6R9R-xUXx9hRTPlhzNij4eqUfIDL1CiQu0Kcdcc-U_4z4ZjnIw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 فوتبال 180</h1>
<p>@Futball180TV • 👥 449K عضو</p>
<a href="https://t.me/Futball180TV" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 In the name of God; The only popular sports channel on Telegram: All for Iran...🖤We respect the copyright laws and follow the laws, Mr.@Durov...🙏🌹Contact ads:@TivaAds</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-01 10:40:51</div>
<hr>

<div class="tg-post" id="msg-104428">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c490b878e2.mp4?token=hxyncpddpCIXFBNLXzQq37rMN2B7668QtXs0jz18U8pzS69FN-Zc6WZwbDKANtuMcR2P2R4QfVcMP5sC296rFL850ojZdCtfk9DVMxmMW8pUEH9AMi-TCFWlysiddgYgMO035dqiCR0On5--AcoybI0wum337dRMCtJkpwd1dYP8k8yWT5ZaDDNu272aeHFhAcuQx2eI04_b-e3Pl4-1zfYQABjOLC-qRLc__TtNc-kHJbg5YKuvDYpe6xJrrRVzDh3Ma-H56WaS08uewcLrDs0P52XGjg8jZju2h7cYnmmcOuAvE5rqN88S5kUIyidOA28AjMgWtbSxAFlzL4-Htg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c490b878e2.mp4?token=hxyncpddpCIXFBNLXzQq37rMN2B7668QtXs0jz18U8pzS69FN-Zc6WZwbDKANtuMcR2P2R4QfVcMP5sC296rFL850ojZdCtfk9DVMxmMW8pUEH9AMi-TCFWlysiddgYgMO035dqiCR0On5--AcoybI0wum337dRMCtJkpwd1dYP8k8yWT5ZaDDNu272aeHFhAcuQx2eI04_b-e3Pl4-1zfYQABjOLC-qRLc__TtNc-kHJbg5YKuvDYpe6xJrrRVzDh3Ma-H56WaS08uewcLrDs0P52XGjg8jZju2h7cYnmmcOuAvE5rqN88S5kUIyidOA28AjMgWtbSxAFlzL4-Htg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
👀
🎙
خبرنگار: رئال مادرید ژوزه مورینیو رو چطور ارزیابی میکنید؟⁣
🇪🇸
هانسی فلیک: امروز با رئال مادرید بازی داریم؟! در مورد الچه سوال کنید.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 455 · <a href="https://t.me/Futball180TV/104428" target="_blank">📅 10:40 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104427">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b0c2144e6b.mp4?token=e8icDRuEAKm2TicwqHcsOfpP38ZY6jBP2MKvZbmJrX0uATth2z8h539XWd3jIg8TvszxF9MYLM3UJrjfZ9Q8WlK-31QqaUaf2CXqEhZM2KiNadGfM2pqsxTpab5N2dNHzfKtRRenLCWwJK4wCgbvIm2JHA6JK5IBwOFNbue2AZ_DfpsdTV0k-Q-ik4mRd4-7OUxI0A7Dp1z30zw9uMZh2iWvHki8ZKPKA58xinNYNU9Hfr60t3N9MZwDTIyysHOQ5kKVtfuWX93jIr_x1IicL0armFSz6NmwNAsjBfB8n8ri1M0LHgKNz-KErhSpUpxo0LONH-w8PGZoasVTqrRkqQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b0c2144e6b.mp4?token=e8icDRuEAKm2TicwqHcsOfpP38ZY6jBP2MKvZbmJrX0uATth2z8h539XWd3jIg8TvszxF9MYLM3UJrjfZ9Q8WlK-31QqaUaf2CXqEhZM2KiNadGfM2pqsxTpab5N2dNHzfKtRRenLCWwJK4wCgbvIm2JHA6JK5IBwOFNbue2AZ_DfpsdTV0k-Q-ik4mRd4-7OUxI0A7Dp1z30zw9uMZh2iWvHki8ZKPKA58xinNYNU9Hfr60t3N9MZwDTIyysHOQ5kKVtfuWX93jIr_x1IicL0armFSz6NmwNAsjBfB8n8ri1M0LHgKNz-KErhSpUpxo0LONH-w8PGZoasVTqrRkqQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🏴󠁧󠁢󠁥󠁮󠁧󠁿
برونو فرناندز بعد از شکست 2-0 مقابل هال سیتی: "همون اشتباهاتی که فصل قبل تو هر بازی بیرون از خانه انجام می‌دادیم."
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 2.78K · <a href="https://t.me/Futball180TV/104427" target="_blank">📅 10:15 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104426">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">👀
💥
پسر رونالدو هم راه پدر رو خوب ادامه میده و در زدن ضربه‌پنالتی استاد شده
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.55K · <a href="https://t.me/Futball180TV/104426" target="_blank">📅 09:50 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104425">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5f6325ec27.mp4?token=vrJvFBUwb3YXbC0qUlSgfuEWINSNJ-jtAdZDxDfAmWkMfPbN6iDeNfXgPXEY-a9ANAqjTysoCJZdzmsqJnd37tRudc290eY1Urw9iHM6wHOaebroPu7DuKXYcnxRNYJ6V0DtLu3JD5qbd1ulE2MOVbp2czjITPM0weJDOlqiQm6uN-d4XLzIh5rfqzzfdkET2Ykfdb5bXbizP9-ev18CY7F_M51NvBzpaML8nBnrN4ErTOwxe2OKU5MJ6mfRUZqlRhpVArBeAQ9YwU2hYmsPqD3Q6cH0kBfZOLWcpxAWVJwjYX7Rd1Ll-0O6oa4-mcT1DpVUFOQrexdGauapeVi-1w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5f6325ec27.mp4?token=vrJvFBUwb3YXbC0qUlSgfuEWINSNJ-jtAdZDxDfAmWkMfPbN6iDeNfXgPXEY-a9ANAqjTysoCJZdzmsqJnd37tRudc290eY1Urw9iHM6wHOaebroPu7DuKXYcnxRNYJ6V0DtLu3JD5qbd1ulE2MOVbp2czjITPM0weJDOlqiQm6uN-d4XLzIh5rfqzzfdkET2Ykfdb5bXbizP9-ev18CY7F_M51NvBzpaML8nBnrN4ErTOwxe2OKU5MJ6mfRUZqlRhpVArBeAQ9YwU2hYmsPqD3Q6cH0kBfZOLWcpxAWVJwjYX7Rd1Ll-0O6oa4-mcT1DpVUFOQrexdGauapeVi-1w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
گلزنی‌ساعاتی‌پیش لیونل‌مسی در شب باخت‌ مجدد تیمش اینترمیامی مقابل تورنتو
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 6.36K · <a href="https://t.me/Futball180TV/104425" target="_blank">📅 09:20 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104424">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/995ef211fc.mp4?token=BMFWZjObKZ4u0FzSgFxnThgae7_G2lwNMLepqCVvp9PAAyg9eB8QeCaI3MRmj9UD8z13e9ou8I--mWIsWDTPNf2jJCpTw7efZavn3btoHWGd0-HPPcXI2qME4qJ50iouX22kLKCswNkCFJlywOwGX4AUCKm7ZD0fCXtayuvZhcj4tT9zRE17I7R_MSisMSP7qFG43aEQQ_PlXC7jo9xIid_1LNZm4rh1qfvNSQbFsn_O_wauVeJ_DkFVY2bIkuUaL3cLshhdsVHRGdyGZNZvvFa0Q3hMGBfCCqIdu0_HT6BDN1QTEiZZqoSXeysDHNaG9eNKXbKELm6NuQ1oPocUlg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/995ef211fc.mp4?token=BMFWZjObKZ4u0FzSgFxnThgae7_G2lwNMLepqCVvp9PAAyg9eB8QeCaI3MRmj9UD8z13e9ou8I--mWIsWDTPNf2jJCpTw7efZavn3btoHWGd0-HPPcXI2qME4qJ50iouX22kLKCswNkCFJlywOwGX4AUCKm7ZD0fCXtayuvZhcj4tT9zRE17I7R_MSisMSP7qFG43aEQQ_PlXC7jo9xIid_1LNZm4rh1qfvNSQbFsn_O_wauVeJ_DkFVY2bIkuUaL3cLshhdsVHRGdyGZNZvvFa0Q3hMGBfCCqIdu0_HT6BDN1QTEiZZqoSXeysDHNaG9eNKXbKELm6NuQ1oPocUlg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
🇮🇷
جنجال‌علیرضا کوشکی مقابل نساجی که باعث نیمکت‌نشین شدنش جلو سپاهان شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 7.69K · <a href="https://t.me/Futball180TV/104424" target="_blank">📅 09:04 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104423">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">🚨
‼️
⚠️
رئیس مجلس عراق: قالیباف توی جلسه گفت خلیج فارس منم حرفشو قطع کردم گفتم خلیج عربی درسته، دوباره این کارو تکرار کرد و منم دوباره گفتم خلیج عربی درسته. قالیباف در واکنش بهم گفت مشکلی نیست شما اسم خودتونو دارید ماهم اسم خودمونو!
رئیس جمهور عراق هم گفت چطوره بگیم خلیج اسلامی که مشکلی بینمون پیش نیاد!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/Futball180TV/104423" target="_blank">📅 02:19 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104422">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qj8LtqIlxWHTPo4X178LPktTRNEUujg-4QkQmTmWgM4YBKle9wpVtWViuIGHN2chWIFn9tCg4Z_RazwQhxxjs8x4GdSGLPlcmZbaUuPLigTo8i1gbsjALnOy8qQds0mRuPeANCz2lxUzDGCnK0bTr9fg4dD1O67VcGW40d9q-onMCO3e8DiraQC1VxgqjJnEOCCzPuNTF1iIoED8Z0G5_qfQZvnV6ypC7Z62XW9MViu6TRywp8lh9WsJ_1hEJmZ-V0rffB80tViE_pQetW77-rk0fW2xGqbs7_pn3mCPa1pGS0Py-T9PZ-am2rWsazvTpLPFprUwmwwuge_93DyiGA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟣
لیونل‌مسی در ترکیب اینترمیامی مقابل تورنتو
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/Futball180TV/104422" target="_blank">📅 02:18 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104421">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TPTFxZCnNEeAYxCo6sfQg6fMAGxun--VnEXSe6paQcqzgwuIzUoczbxEmY1k2i-wWRHS9S4ufqcn0Q4ikKPbowtWINr3AjiXIhVtKRx_oer_yjhIFBTAmHjLG3y4Yr0tbcNvf4o8jGbxE44v1O3g585fs5LzrBMI7kzQuJ5B9eeyw94_N3c6E_FiyhGHzn4QgoOOBHZtgrxxEu6QQGNOr-tK2x7vTnD3EzG8fHPIIubHSngQl5yQlo40r_aucGmNV1jc7kf7R96uSk33ea5PA0xIkbMac9daSt-CYi_RTt9rLyKEMJxNhkteh22riQ-Ocz83X7evoASjLYLKVSpOTw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
🚨
🚨
🚨
‼️
🇪🇸
صفحه باشگاه اسپانیول در کنایه به قضاوت داوری بازی با رئال‌مادرید:  ‏" چند بار باید خطا کنید تا یک کارت زرد بگیرید؟ این سوال رو از طرف یه دوست مطرح می‌کنیم."
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/Futball180TV/104421" target="_blank">📅 01:43 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104420">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/C8znfux4qOm7bBgmi6srqnL6bwDqmLpKpXkQC5UpvqNQLkzKPSepQnMfTIXcbaGh-xwBSTLaZe4kA44ca0sA7TeSuAVTbb-YEJLCYrKWLPUnU37sB-OoR42sFRiHnUC_6SmKBvoQurDJRvSga9Xu_4e3lf7dHP-RaDKs3CrEp2-eyHR3TRSWSEVWKrnSbSRWN2X8n43qZQKwJSt0Wp5Ff2lkIEa3wJusj-ILQvlT33NAhHcxG3nVbViley2Ab5K8EtiB618yBMUv28zjRUTXypmN3B0L8NkMnjUn9CFQiQ45Ae5pbPNrHNflzrAx3DFOUHnmUM16isyejEdf41FfLQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
🚨
🚨
🚨
‼️
🇪🇸
صفحه باشگاه اسپانیول در کنایه به قضاوت داوری بازی با رئال‌مادرید:
‏" چند بار باید خطا کنید تا یک کارت زرد بگیرید؟ این سوال رو از طرف یه دوست مطرح می‌کنیم."
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/Futball180TV/104420" target="_blank">📅 01:42 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104419">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XIte8e1z5aJp9ggRDx24N-NGotkUjn5dbhDWGe95UFO5PZcRctdJRvVRfybSHPMmalinqROwc5MubXArWhj-FhWJfyyhsafADSybMZQzSXVB9IX3LlIc3GdNf4xDPBpnOQV0n1yq2kCz_unvjq0EoveRn7REG8TiVFUqoChrbelJfiI2fDBYboByF1GdCex2JquqA9AFvZcsQLm1lyRsLAd-YGcuXdJG9J8N2UTXF2_v_1twHAw06TZrcoaT-3u5amnT-YhJBRYjMvBL1sKilvTh2xHorfT0ONzGZV1o3tb5_4AHxuPcRA_iEacxKLCp__UysXaYngj1gbs3ZZv7Og.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
🔥
👀
نجات‌دهنده ژوزه در قلب بارسلون
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/Futball180TV/104419" target="_blank">📅 01:17 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104418">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ktxcl9FDkMFyHEfN4PeXsizNa1T1C4Mo3T6WiNIn4k1F59a8l3KFcJlnHcvEkogcI2o_s9D_sywt-Ac3rsibpDShZ1WUL94ah_USnA9B3sJlBFmGGMWR-N930EUKaYMpzlFeKzlN6WXAIV6mnLEknqTDrPy1KLd1G03XcyNKeYO8gXgyiWM0Da9ECR6Xr2l7D_R1gHKNMcjhU-VSlAfhVRql1JYiVIIP1tnzefYNZrskKda1hl87Cb6KQswbPhyBJNHoiks1N82A1VwwnDKN4OLHEs-8D6cuzOBm44S_F8GYoa9fvbEWFST5gnDadAyAv8tQJScl2_LOTxYL0TCvtA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
📊
⚽️
گل کارلوس اسپی در دقیقه 89 و 54 ثانیه.
🔥
ریال مادرید با به ثمر رساندن گلی پس از دقیقه 90، برای دومین بار در تاریخ خود، در یک بازی افتتاحیه از لیگ اسپانیا به پیروزی رسید.
🗓
پیش از این، این دستاورد در 21 آگوست 1999 در مایورکا، با به ثمر رسیدن گل تعیین‌کننده رائول در دقیقه 90+3، حاصل شده بود.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/Futball180TV/104418" target="_blank">📅 01:05 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104417">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-text">💎
میدونستین تو دربی بت
✅
با شارژ بالاتر از ۱۰۰ دلار ۱۲۰٪ بیشتر حسابتون شارژ میشه
✅
🎁
برای مبالغ بالاتر از ده هزار دلار بیمه شرطبندی ۳۵٪ داره‌
و مبالغ بالاتر از هزار دلار بیمه ۱۵٪ داره یعنی در صورت باخت مبالغ به حسابتون‌ دوباره واریز میشه.</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/Futball180TV/104417" target="_blank">📅 01:05 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104416">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">derbybet.apk</div>
  <div class="tg-doc-extra">53.7 MB</div>
</div>
<a href="https://t.me/Futball180TV/104416" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">👀
دنبال سایت معتبر برای شرطبندی می‌گردید
⁉️
🎲
سایت بین المللی و معتبر D
erby Bet
✅
✅
✅
✅
واریز و برداشت ارزی و ریالی
‼️
✅
بونوس 120% اولین واریز
‼️
✅
بونوس برای 4 واریز اول
‼️
🎁
بونوس ورزشی هر شنبه
‼️
🎁
کازینو و انفجار با ضرایب جهانی
‼️
🎁
کد هدیه ثبت نام :
Gift
🎁
دانلود مستقیم اپلیکشن اندروید
👉
🔗
لینک وبسایت
👉
⭕️
جهت استفاده از vpn از IP های آسیایی یا کانادا استفاده کنید.
🇨🇦
🇹🇷
a31
✔
@DerbyBetOfficial</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/Futball180TV/104416" target="_blank">📅 01:05 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104415">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Cd1_bJKDcz_yvbbUWqjLxiRKm24XC9dU_sBeheeSgTa8GWKkLxF-4XvR38kGRMmHzRj4g2pqETPgrLuOzb5vom6M2wO_s2aTODdfEzkr7TRHG_B9FAG_KhxJXl7ezbRGUny6G4JS5uIJ9Ltnj-qlmJuolGIfYdaO6L9115Tb1GFqpHG4cXXilNGCsMT9mHJyYVt5Nhw9cKYMEET9IdQBytDgedHJrT2TF-I7qUEx-1ICfjEKNgk8p9OXg1YwzFMEDGo8jx7w2gXWvy8LDE-S7KpwbNkN3PW203AFx5z4nH93v0tmDdTOBl46P0mIpUOkfYt60C5QuRDeRqCOo1NI6A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👮‍♂️
مد
ا
رک رسمی تحصیلی «مقاطع متوسطه و عالی»!
✔️
از دیپلم تا دکتری | کاملاً غیرحضوری
✔️
قابل استعلام قانونی
+
قابل ترجمه رسمی
✔️
مناسب برای
:
مهاجرت
|
استخدام
|
ادامه‌ی تحصیل
ارتباط با مشاور
:
https://t.me/mydiplom_support
ورود به کانال :
https://t.me/+lHweVa-y92IyZDA0</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/Futball180TV/104415" target="_blank">📅 01:04 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104414">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TYbrjm5ozjoCd08Lhq3I__dX7WrfuW2EdXGRn4yhVyw78BdDlzbhIbmib7B3qwjUNI1qYV0Mtuo1iGRV9gUq2VgtltwgW1I2nMFn0-oWR9P7wIssTQAZjCaJ21ybmFazo1bLxrST7BMBvbbX-2KI_QxjTSzbf7ESKjx9f5PUW1t1u9zffUTF32wT75aHGOhD_xqp6TBVaGdRscLsgVyZtA7Pe13q22uY8uo54ulLJMReZjZdEVSoqJMsxZl9yIGWZ8yqtEIvAcQka9lUfduXeIUsMKJsq042OUA5Z1rpxuC1_vVOh5MZ1-TKaFDZ3nrbfChiHbsbGdoSTtLklnvTDw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🇪🇸
هفته‌دوم لالیگا؛ پیروزی سخت و نفس‌گیر کهکشانی‌ها در خارج از خانه؛ مقاومت اسپانیول با گل یک بازیکن کمتر شناخته شده شکست!
🇪🇸
رئال‌مادرید
😀
-
😃
اسپانیول
🇪🇸
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/Futball180TV/104414" target="_blank">📅 00:56 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104413">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/69ada12902.mp4?token=ZqzQOO1Vt1fVjAqR9N4jJ0Yj-NaaVtUEwx1-jk15y8TY6Q1Dj4SHShza4txsG5LYkdcnggUOsgnkWr0m63IwCJptP20L1hvzJfBXEAPZLJsC13HycPY-4Bw0GuolCPz6Xs01n2e8UnQa27oo0aK9WGTc6yqpzZjmxmuMsg1fybitZUC21GFHIXZMsufboVDWrqzVBxr1tIplB6KX2o737YGfa_RlX4wfchZQMS_zyYVFJ8IJZXktNvtklpZBNyWhCeUBXXOlF9e_7EOAEDy_v7hb4uWqTOpw0dVEAT4hhPowGgWdJOIs49JySZ8KjWJuJaRAOj2E915IbQNwAfqAJg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/69ada12902.mp4?token=ZqzQOO1Vt1fVjAqR9N4jJ0Yj-NaaVtUEwx1-jk15y8TY6Q1Dj4SHShza4txsG5LYkdcnggUOsgnkWr0m63IwCJptP20L1hvzJfBXEAPZLJsC13HycPY-4Bw0GuolCPz6Xs01n2e8UnQa27oo0aK9WGTc6yqpzZjmxmuMsg1fybitZUC21GFHIXZMsufboVDWrqzVBxr1tIplB6KX2o737YGfa_RlX4wfchZQMS_zyYVFJ8IJZXktNvtklpZBNyWhCeUBXXOlF9e_7EOAEDy_v7hb4uWqTOpw0dVEAT4hhPowGgWdJOIs49JySZ8KjWJuJaRAOj2E915IbQNwAfqAJg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
🔥
🔥
گلگلگلگلگگلگلگلگلگلل رررررررئاااااال
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/Futball180TV/104413" target="_blank">📅 00:53 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104412">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">اسپیییییییییی زددددددذذ
🔥
🔥
🔥
🔥</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/Futball180TV/104412" target="_blank">📅 00:52 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104411">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">رئاااااالل دومیووووووو زددددددذ</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/Futball180TV/104411" target="_blank">📅 00:52 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104410">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">گلگلگلگلگگلگلگلگلگگلگل</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/Futball180TV/104410" target="_blank">📅 00:52 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104409">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">▶️
🇩🇪
🇩🇪
هایلایت دیدار دورتموند 1-2 بایرن مونیخ با گزارش روح الله مدرسی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/Futball180TV/104409" target="_blank">📅 00:43 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104408">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JIQTZS7rvthPg4gAfEirAiTpZvq8Ju0q2vLmVXqbqtLOsyWSKeLhLN3kuiUNg9p549ihFVUkPhJPuhm_H6m5VwJwr1yYw6RJAVVX872Y8W9oPT9Kj4PlZbOec5CUd_t0UU2NLtK27WhkjBELhv8v0N7nkJFSqO55dRfzIfAnuGoB4y-HUEiqvxMWWFFCpljzyBf74Toxl05QCwp_F82xjhOTSHdypsWgZtwTnym9VEjG7WI4OYu6x7W-b4bb_zS2oKxOcDYyYGvB5IPcZZeVv0qzDpco6fCyRAelH4kZvKaoKoYFted-_kf6ox5wPQJTzmPkOdw4JTiKVZLlui2ayg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✔️
🇸🇦
رسمی؛ داروین نونیز مهاجم الهلال با قراردادی قرضی به الدرعیه عربستان پیوست
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/Futball180TV/104408" target="_blank">📅 00:40 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104407">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RP1lzsuv_-IIMTHuL6Q9DpyhjBlmevr7eHftRw84XzSvWnYxk2KyyKgkuoghpkpL9KRqSfos1HJWzfIIlslnpvHYeKnI9sflr_fv49mWLipCYgitzXscQYvAwh0LZlltSp_n1OdEHYDdqUhLhBdsfkuglj6Az4hE0AXU01KMZmQ3xO4ButibkbrrAfbjPypr3i7CKlBnWR7PWgYqGkit8kWwnPfKVl_9Drnc-IWw0JFJy8GETtSjezFd3I_gobdynRwWO_T-M0AjcdN8KlqMpAkbpbA1WBhY7Iv5E39o606foR1b_gMvDC-YlAyH7FKsrIkx-ti05WGTLkDmwclu4w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🚨
🇩🇪
سوپرکاپ فوتبال آلمان؛ بایرن کمپانی اولین جام فصل را از رقیب سنتی گرفت؛ دورتمند بازهم مقابل باواریایی‌ها ناکام ماند
🇩🇪
بایرن‌مونیخ
😀
-
😃
دورتمند
🇩🇪
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/Futball180TV/104407" target="_blank">📅 23:54 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104406">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/06034109f1.mp4?token=X6BzSsVBRaQlL0RhfDVWoVFFssDI2PApsKEyTju084Zv7uU-094GGC48-SwSIvYHppw9f1c2qmKmshMEXneCOMTuOtXjdeQJjQTEby1v5hyZ0jL55gXg5D56jSb76lc-WvLJXw3jv4dlegCpkI1PI7lUTDBl9k4G8D3HOj3lnKycSldHgB1YPZoE8_XmrJ7Mmw9C1p4_bYVE_8zirCyCv0x4n8jbKjlDrEFB3ydMnVv1chToQk6JzeI36jz_xHPutTXYVwnBHKgs9SjnWUOEinxUTRrUBlW2Mby7SY2cyF4ldfu6SbcHpx_Km5MOiwyC-uJQYdWUEgCRU3wG1gANVA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/06034109f1.mp4?token=X6BzSsVBRaQlL0RhfDVWoVFFssDI2PApsKEyTju084Zv7uU-094GGC48-SwSIvYHppw9f1c2qmKmshMEXneCOMTuOtXjdeQJjQTEby1v5hyZ0jL55gXg5D56jSb76lc-WvLJXw3jv4dlegCpkI1PI7lUTDBl9k4G8D3HOj3lnKycSldHgB1YPZoE8_XmrJ7Mmw9C1p4_bYVE_8zirCyCv0x4n8jbKjlDrEFB3ydMnVv1chToQk6JzeI36jz_xHPutTXYVwnBHKgs9SjnWUOEinxUTRrUBlW2Mby7SY2cyF4ldfu6SbcHpx_Km5MOiwyC-uJQYdWUEgCRU3wG1gANVA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇩🇪
گل‌اول دورتمند به بایرن‌مونیخ توسط سیلوا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/Futball180TV/104406" target="_blank">📅 23:37 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104405">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/1aebcbb396.mp4?token=pnZHBmI3nxrsK3cqwHdvMchzi2zPiqbgmEZ2XZ3P1pvrJX4ArzQKRZ6KX_IDAqIDpN6G3e7qqsyNop5FUewGkCNHqcIgvl6nrvQfHNMcFlqKIaC-Vi45eMdfkb2IjAbXPv5hxqxzENIoiJCrc0kAyJ8FRoDaf9sbK18C99BuHiTBs-6hnw_u7Cjza9AlxkKE3dxWdG064lRWz-ZWaVYizsJFTlJlxnknjoDmGUw5q8gSN7WKsdkGfo0iM0ZmBYJKcTqY7B9VTW75rgq8sB0FydSytIQwCaLvBre0weaYFvfMLZPeg0CHPx7pfF4s-GQ4Oaef2a8afLVcJClArX0Iow" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/1aebcbb396.mp4?token=pnZHBmI3nxrsK3cqwHdvMchzi2zPiqbgmEZ2XZ3P1pvrJX4ArzQKRZ6KX_IDAqIDpN6G3e7qqsyNop5FUewGkCNHqcIgvl6nrvQfHNMcFlqKIaC-Vi45eMdfkb2IjAbXPv5hxqxzENIoiJCrc0kAyJ8FRoDaf9sbK18C99BuHiTBs-6hnw_u7Cjza9AlxkKE3dxWdG064lRWz-ZWaVYizsJFTlJlxnknjoDmGUw5q8gSN7WKsdkGfo0iM0ZmBYJKcTqY7B9VTW75rgq8sB0FydSytIQwCaLvBre0weaYFvfMLZPeg0CHPx7pfF4s-GQ4Oaef2a8afLVcJClArX0Iow" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
‼️
گل تساوی اسپانیول به رئال‌مادرید
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/Futball180TV/104405" target="_blank">📅 23:35 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104404">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UI-n4Vownr_hcsImjDCXScQSdQnLzVWFjiWbN-t3TgTnR8vvNn_c1A79OO4hOfnMkIWm558uOe9CqP720OeyN9BqU9YajMaVpvXkS1vklXRYadW3efdx8TDWz2PV-gsAb10knQzS4JYrJRtYBfzTcG62gEhBb3BUMxnDTx44UZeetrYLU_8fe3t8XZXzp2s0xmDTdNZVlv4Bme1vXZMthrVZx1EUssNzCgk08RaFjSJts8HYl6vqaq1i61kN8GZsn-bDfIii7tLlKqeOk24DKtAUKNANk3d4JRN7u7g9KCisdQC234lO1U5N1EID6dgdDpANFf1XwnTl0cpqbOIZyA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🤯
🚑
هویسن بنده‌خدا اوف شده
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/Futball180TV/104404" target="_blank">📅 23:27 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104403">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/64261a7aea.mp4?token=rDiKSpxg7R5FFgI-juTUq49EH5itPUVg0in4Q-BY12aSnyMr9W_mzRwVYjOzgEi17wzJa9S5mgD_RLRpu8LYfFl4dS3HBnBxxXf0T1-EUOrn83XkEPMcvwKSx2Xky0UxKYkFG0E0IEbwSPBpPDGyBRz45v2jfQcjg9SkXFG3zL5Shvyt059N4xFCHQqktthsAF_nN86sk9cV0P0NHw047ZQEZZaLIEqb23VtjyzdDToblTy7Z8XMpjQt1rB_B2JhPtcGYw3GXw49D1qdGeXKO3mgJ_Rx1KLY26X_u06Er03Ct65RrOIPS_YLUMgCQpkWZktj-DDGE2y7KZwrX3qrWA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/64261a7aea.mp4?token=rDiKSpxg7R5FFgI-juTUq49EH5itPUVg0in4Q-BY12aSnyMr9W_mzRwVYjOzgEi17wzJa9S5mgD_RLRpu8LYfFl4dS3HBnBxxXf0T1-EUOrn83XkEPMcvwKSx2Xky0UxKYkFG0E0IEbwSPBpPDGyBRz45v2jfQcjg9SkXFG3zL5Shvyt059N4xFCHQqktthsAF_nN86sk9cV0P0NHw047ZQEZZaLIEqb23VtjyzdDToblTy7Z8XMpjQt1rB_B2JhPtcGYw3GXw49D1qdGeXKO3mgJ_Rx1KLY26X_u06Er03Ct65RrOIPS_YLUMgCQpkWZktj-DDGE2y7KZwrX3qrWA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🇪🇸
گل‌اول رئال‌مادرید توسط جود بِلینگهام
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/Futball180TV/104403" target="_blank">📅 23:17 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104402">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/96a06aa961.mp4?token=rv-lWjc6f_7mM6bXTsy5k4lHtNN-DbUhsH-q5PNWNolEX9FeKXkIBawAf7-PE4V91fa2LXUGTRk7wxVGv1k1Fpbjs42TnlmnkTmlIxJ8RonI7mq08Am1uKoWPdOWdxlKTImOohQ-udyw77BW08Livkrey-m-ZddNW6KMNar6BxgL3WhwFjywClJltmU994xJ71zaFubxjlzGitwa_v2cZoIl_pqoZ0ktr0fiOUWwbjlbz9rWhdeS6ppxiP-68SaghvRurXcVkrv5WhebJP4s6hpUGkSM9NjuZ3LzKyd_3xkjPauorGbmuIZoD1lMK527QVtFZnttQ_ZlrWqHdKj_nQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/96a06aa961.mp4?token=rv-lWjc6f_7mM6bXTsy5k4lHtNN-DbUhsH-q5PNWNolEX9FeKXkIBawAf7-PE4V91fa2LXUGTRk7wxVGv1k1Fpbjs42TnlmnkTmlIxJ8RonI7mq08Am1uKoWPdOWdxlKTImOohQ-udyw77BW08Livkrey-m-ZddNW6KMNar6BxgL3WhwFjywClJltmU994xJ71zaFubxjlzGitwa_v2cZoIl_pqoZ0ktr0fiOUWwbjlbz9rWhdeS6ppxiP-68SaghvRurXcVkrv5WhebJP4s6hpUGkSM9NjuZ3LzKyd_3xkjPauorGbmuIZoD1lMK527QVtFZnttQ_ZlrWqHdKj_nQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇩🇪
گل‌دوم بایرن‌مونیخ توسط مایکل‌اولیسه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/Futball180TV/104402" target="_blank">📅 22:50 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104401">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/2962887cc1.mp4?token=pf6Kx79spGrdk1sNrpmWoO0hH_QVUJWZJk5sUOBqbbT-AY5CKog4Swq1R5M5OC-LK_i96EvauOmex73VAzfKVa922oj8EZkTaJy5Wpo52k-cnH6Yr09EHAPDknwJQojdtC-zu-drNI9Fi12ArXLHZrEfoJzamdk-2uwjHqKaBnUHNf5PgDFz8atZnUBgnWYGS_Ku-DjTbzgeZubZP3C2wDLAQTS6j4AupngyxgHqqVysAp1H7Ovs86uZuCuba6vErwWl3i_L0I0Fjd6CSzaCSjqmk1R7Zgp1NoCjiDmsRrz-w0oqkp7cgUOVqp5H4oa-BREtw5MHHXGUblAL4JmYEw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/2962887cc1.mp4?token=pf6Kx79spGrdk1sNrpmWoO0hH_QVUJWZJk5sUOBqbbT-AY5CKog4Swq1R5M5OC-LK_i96EvauOmex73VAzfKVa922oj8EZkTaJy5Wpo52k-cnH6Yr09EHAPDknwJQojdtC-zu-drNI9Fi12ArXLHZrEfoJzamdk-2uwjHqKaBnUHNf5PgDFz8atZnUBgnWYGS_Ku-DjTbzgeZubZP3C2wDLAQTS6j4AupngyxgHqqVysAp1H7Ovs86uZuCuba6vErwWl3i_L0I0Fjd6CSzaCSjqmk1R7Zgp1NoCjiDmsRrz-w0oqkp7cgUOVqp5H4oa-BREtw5MHHXGUblAL4JmYEw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇩🇪
گل‌اول بایرن‌مونیخ به دورتمند توسط برون
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/Futball180TV/104401" target="_blank">📅 22:41 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104400">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fc1145503d.mp4?token=H9fD3xrS9vDsGZEj_YsL5u5JsEQX5h07e0CTxQ7ZCNRoFC6JxZnqR0vdIAFHH8qHEqc2hbXXbOjoa0A7ao2tfI6OMGFXTu8B-WoavLDZq3Hoah_8YlVDjhJZ0WN2VRHCSluuICFfy_-P7B2qZcZV7pHY_sh6tnQ9-e2lZPjqwH60v2owYt8KNfUDAOOza7AFpAN56GenTR_qt5NvVoDD1oj1NRg2lAQCgi2d2I-JuMvs62jl-orDciCG7n2zkIMeu0Lms487GHeI3qzW69MoBTx9d69Ykpvxr_PqqrHdTkJ60mJHnRZ2qOqeZ1KGDRTZRJxhURYLRA_F2V-SFuISUw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fc1145503d.mp4?token=H9fD3xrS9vDsGZEj_YsL5u5JsEQX5h07e0CTxQ7ZCNRoFC6JxZnqR0vdIAFHH8qHEqc2hbXXbOjoa0A7ao2tfI6OMGFXTu8B-WoavLDZq3Hoah_8YlVDjhJZ0WN2VRHCSluuICFfy_-P7B2qZcZV7pHY_sh6tnQ9-e2lZPjqwH60v2owYt8KNfUDAOOza7AFpAN56GenTR_qt5NvVoDD1oj1NRg2lAQCgi2d2I-JuMvs62jl-orDciCG7n2zkIMeu0Lms487GHeI3qzW69MoBTx9d69Ykpvxr_PqqrHdTkJ60mJHnRZ2qOqeZ1KGDRTZRJxhURYLRA_F2V-SFuISUw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
🚨
🚨
🔴
علی قلی‌زاده: امیدوارم سال آینده در پرسپولیس باشم
💬
فصل گذشته تمام کارهای انتقال من به پرسپولیس انجام شده بود اما ناگهان ورق برگشت/ باشگاه لخ‌پوزنان امروز یک‌رقم می‌خواست و فردا رقم رضایت‌نامه را افزایش می‌داد/ به هرحال این ماجراها بین باشگاه‌ها طبیعی است/ امیدوارم سال آینده در پرسپولیس حضور داشته باشم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/Futball180TV/104400" target="_blank">📅 22:25 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104399">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/t8yz5H6oUWZKolgQpvLvSsQsPanMwFFNCx6oFKin0JLY7XqQzGbqtapBWhTmD9r75ag8_NivnQI_tzR8fHyyDhc6ShqEEXp02Tk6SULmdAKnHhnfQ28AUZhWZIYqg_IJ8khmoAerntTLwchoCdZgujXBQFzCtYwYb6LMrv0y_U3kpQC_0tGQkmq6JfFos1zB5ux2ikWEKlA4tSLHVqG4T249SrGIDyKK0LA63ksU6dqgB59ipRWB5LXSIwhq7qwL2kAHLF-C0qQV8extGcxk836DvYoUMv5IG_8xPL65Hf93-iguyXAoyCp61h5lKEHXHgxiUsdgRyCyjSt1-ZQrfw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🗞
🇹🇷
رومانو: فابینیو به ترابوزان‌اسپور
HERE WE GO
🔥
🔥
🔥
🔥
✅
✅
✅
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/Futball180TV/104399" target="_blank">📅 22:21 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104398">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e6d7144def.mp4?token=B2970oZBbPusszyXiQ4HdRtweb3AIvdCZatCuwfBdDHGOu6XJ6nI0shP0tpWaDHaUICoO9udJmepMwBY_cmAw4w4pNHvBFfOr8r6XDUdq8gA7kYgAD6aCdaXTZS_USh6EGAF81bYTlsT_oYHLdcRdS3BB6bQ7XvtEdD1JsYWvfPT7qhMgudWGKR226J009KhZPhWyhoQzt8iF905NobGvghB_9hfgrwIgbJf_czLPGo4Zguwgvxqdrw9kUWvgKbPnAKJxdyqYQw6bSOUDMI6j5d9eJZA-9aRgLtT52eC-U9qjFbC5HLCylVa92-k_Oc3ufdOGTwVf39mfIFo9E9QDg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e6d7144def.mp4?token=B2970oZBbPusszyXiQ4HdRtweb3AIvdCZatCuwfBdDHGOu6XJ6nI0shP0tpWaDHaUICoO9udJmepMwBY_cmAw4w4pNHvBFfOr8r6XDUdq8gA7kYgAD6aCdaXTZS_USh6EGAF81bYTlsT_oYHLdcRdS3BB6bQ7XvtEdD1JsYWvfPT7qhMgudWGKR226J009KhZPhWyhoQzt8iF905NobGvghB_9hfgrwIgbJf_czLPGo4Zguwgvxqdrw9kUWvgKbPnAKJxdyqYQw6bSOUDMI6j5d9eJZA-9aRgLtT52eC-U9qjFbC5HLCylVa92-k_Oc3ufdOGTwVf39mfIFo9E9QDg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
🚨
🤯
🔥
🔥
🔥
سوپرگل تام بالارد بازیکن بریستول سیتی به بیرمنگام
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/Futball180TV/104398" target="_blank">📅 22:05 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104397">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Nc7vuFu5bRSk9yjEZKTfNVdMESzpk3I2eJCJUmYoXEKVQwt452T4nb__B4GM0qZnm0Lmk5j2hB6nPjyRKDB0JwwrdXYmPNux_QKXduwQDQxEh2fk-WuaC4E08NY0_mR3tGH03GFcmk-ucvslCAitbYbDsM6fPOFhqin2B4WszpdHDfabBG_PNCqWTs1bJjXvPm7aN-9aJe9M34yEHl1uATWPHL4S9Q0jOOJtcyx3s329ox-V6eqIged4dQgI3mKydxHDsuVeAN-wY8un8sALuvQli2Tx6RVHclji_ixpSQ_gFZ0rCMymO5HZvxeFsZ4yRw2eEx5UX5surj2weN4Y1A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
🇪🇸
هفته‌دوم لالیگا؛ ترکیب رئال‌مادرید مقابل اسپانیول؛ ساعت ۲۳
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/Futball180TV/104397" target="_blank">📅 21:49 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104396">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/e6JkBcYMcETTqyDwFUgS67Mfg9ff-m7RyQDvmqi3aRc7KXNTHYXIUEHyGEJDP6-MdPkfEpx9WA6WqgVvUXnwSjAaqGnWin0Y0xnPAy5c56C3oLmnBRkg0Aj9csGY0zw3kZjCzchUylMLRrf0IWQmmHYpCSIz47P99YqE2kGUF6dXCvmO5_teJ10oFbXCxYrOoj4NOHXn73YoksftD0TtJjKxlWm3zJAcDJDv40Vi7l94o3R7Nbu9W7FceuevKtxksSKuhyBn4WOza2ED9nm6O0bNCGM0inER3ZGFjjyMyGDa631DS0xUoT5TBNbBLxJ6zVwjY87KhR295nOr2JLZKw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
🇪🇸
هفته‌دوم لالیگا؛ ترکیب رئال‌مادرید مقابل اسپانیول؛ ساعت ۲۳
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/Futball180TV/104396" target="_blank">📅 21:47 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104395">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/usDS8M-ieiWb6EGifjBzggAo677Cvwhao8Lm1mzfnQJKtyt72tKAZDQjhe2xnlaqhW7xBOh58ZwZSlRK0zFU2bmfvTfdTSMIvPElsfBW-ZkQIOwYbbLayX4zZawtfI1LSI2Mr0_ZAi7yricMV0Jd4657lCKcy82f5Fba--RTZ_NKEXtxHgNmbS7tI4e_pvrhOK7DfCgRbNxDDxwYB8G9FQCq2ZZm3r4s3l5Zi0Q3JUAo5kwjb7-ysJaa8lPzXLwAFfX5TKBn2iazJLiSlfELfiMtK6HXbqS6VK-WuV_M24Wesnkq8whfiG3QlPLPhoeJu08UsKLaoj33nC-1B02-gw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
✅
🇪🇸
خولیان آلوارز در لیست اتلتیکومادرید برای بازی فرداشب مقابل ویارئال
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/Futball180TV/104395" target="_blank">📅 21:38 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104394">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dauRg_y5b7HDAQggnknT_bEvN68lrFhXHQ_Zqor6B5WiA9oxALVV158rmLjgwnqwVR76QQfCDBHz2JW3hcPrmoaw_mMkfLLISwJdmGjhVUDV8CgDd57h8e7igzsnWkKCLouv6OSNkFvJirSV_YcY2dCgQrXZX_U9F7Q7iuWi2TX4MVkVZ_iJ2sopvqG2jKlLiVFqHet4B9fUL6VgOHhJYDjblBIt6C9wI1NNOvW622mfaiZF4zWW12zBq1wau1VK2X1gT3Ap9zucKaTsSBBmsy1CuF7rnu8-XjF7I28qAeWLmxfTh3AIqeh4D4L_hp9jY3lLGrid1etTkStZvRYKTg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
🏴󠁧󠁢󠁥󠁮󠁧󠁿
آخر و عاقبت تیمی که مربیش کصشر باشه و با ۳۰۰ میلیون یورو هزینه بازم بگا میره
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/Futball180TV/104394" target="_blank">📅 21:12 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104393">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IOSQov7Qdt0SLYZHgyJaNBMLxNAkYE9DfGrIA4jI64uqNgGad1vcl2Ym0pTL1AtCexh38hoSA7p2fOnTAdKOCQdUF96g42iMw7_otiwEs4nypwxH0xFYCuyIizSL7_kMWltpdv46wXll2UFFmzQhA4gXjrdY0bZX3lnuLyfKW1dW4WOnJ9TS-PvT6iAHUX_5LbEisv_IBYBWUG81VHOjGOvvKngIaJteUNN6U3Xs0RHxIL5bz3Vx6l75wJUmHAW4RzxNIb9Y6pdCiHUSxLG8n5xhINJxSnSm-7UjF6wJqeYrvDYWIozleEwEDim_lbpzt28qPlV46FFtzuN1G-WlDA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇩🇪
سوپرجام آلمان؛ ترکیب دورتموند مقابل بایرن
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/Futball180TV/104393" target="_blank">📅 21:02 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104392">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Lz9qAKRApH_PfkxtZgbYEz6Pl3IWQLr7XVNaGjoHYNthKLLcrrq2jZ6FtRmL9aUOgCB4LxDrDIRv3CqnTgAdYgsNuiQj_XUwaFXulsB_W-apBcVkr_CiYr1a_GKGn8vMeORKoKfA12GXrI33wEq7zY62SHRIazLvCmXTmAvIU4h31BG7t98Vd5WmAeLyEEcGlmWVntUhWbzlvWzRLVCUPZFTF7aK9-IitV1pI_ercDcBfORlOUDguwon-aU0_CmdYrfQfytXNSyQn7SJMdQk-kDDZqbPlkKtQdNtUHVtX0tkLDHgFEc1Z53drQOOL26FHmCLCAT3UoU0GjTB191Gxw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇩🇪
سوپرجام آلمان؛ ترکیب دورتموند مقابل بایرن
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/Futball180TV/104392" target="_blank">📅 20:58 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104391">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8f25fa8009.mp4?token=K0NtIVz-5quC4vXCplkFSIcEIvmhklHvOd-rYTiOHz6sMe0fd0LEBMMAPWT-QnrjvQpe5kdF6pcV261cGGNy3zL28nrxFQnqOznFz-Sk1QjEdKsz3M6Xs_IHTSqVMIABBecHZ626EKo3GYs0ub_SMHEbQOvEL5O4TpbYmzKhLD-D47RQUUI0weYOXJllGy8SmfYGZDW5Y_nkyGZTUqsPkkki5PFhdtM9ee55FyzTFIZ4aDEsByxQ5cnW26vSfDGLkG2vLbDTexScCJ3nOK7zZIAjffMW8ZdLpW33yC5Y01Ufx3QDMNemH58DSP64TJTiDy5U2ZZBA35fFzPBhJN4oA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8f25fa8009.mp4?token=K0NtIVz-5quC4vXCplkFSIcEIvmhklHvOd-rYTiOHz6sMe0fd0LEBMMAPWT-QnrjvQpe5kdF6pcV261cGGNy3zL28nrxFQnqOznFz-Sk1QjEdKsz3M6Xs_IHTSqVMIABBecHZ626EKo3GYs0ub_SMHEbQOvEL5O4TpbYmzKhLD-D47RQUUI0weYOXJllGy8SmfYGZDW5Y_nkyGZTUqsPkkki5PFhdtM9ee55FyzTFIZ4aDEsByxQ5cnW26vSfDGLkG2vLbDTexScCJ3nOK7zZIAjffMW8ZdLpW33yC5Y01Ufx3QDMNemH58DSP64TJTiDy5U2ZZBA35fFzPBhJN4oA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">این حرفای گواردیولا رو گوش بدید و عمل کنید
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/Futball180TV/104391" target="_blank">📅 20:56 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104390">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/V4ecEwD6StIrpt8XbFP8B90Tjl_ICBd715USYqAW3Bgksc8Y4jminaWS3edJ38BGuS6A_NvJgK4oJBEnMS6Z06AWShNRYWGmBhOgrqsocvnoyJ6VXMdinzLuIj5sN2qfm7RY6wj7UQW9DkGaktl-4XDAFpkJ25NmHMBdiEhFk03JVnEMwEJJaqNdfEPiKwAy-kbN_j7hdu8YFT77wv-EDEP958bcXhumhfOvYrT3MT_ZC4RPqnM4JKES28ACQAvNT2B_87S9fYEz3XxOsz5Xe8wfaetWhGMwvqvsdN9SZ7_bPeNzwQzHdbq0PTeGzPM37iXN7JxCPIenCnj5vpI2sg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🇪🇺
لژیونرهای ایرانی حاضر در اروپا:
🇳🇱
علیرضا جهانبخش: اکسلسیور هلند
🇵🇱
الهیار صیادمنش و علی قلی‌زاده: لخ پوزنان لهستان
🇷🇺
محمدجواد حسین‌نژاد: دینامو ماخاچ‌قلعه روسیه
🇧🇾
میلاد محمدی: ویتبسک بلاروس
🇷🇺
نادر محمدی: دسته دو روسیه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/Futball180TV/104390" target="_blank">📅 20:14 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104389">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dba53081a0.mp4?token=a3WQ-JTuweHlqa77sHDdIu_5B2vGbnJ-M43Qi6d1h0tSg4jLqxxC_hdvRYdqS6T4wzmzMsY5hFv-Y_LDDM1j_kqrVTb2PdRWyaa18Y2MhoICrtmOhJ5br0kF96ywUtjfuzAAUhOhu2FNVFKcrQi6y99O13nDorIweYzrCawzCvwM-qkuE1ZdjIhseYoMVjBHq4ELg7PXuObNOQaKRS3mvjNxT-yf276SezfS4JINOq012Yi_H8QHMD9nvcSbeJ9SDIAK32R_F-S1umkeIGrU6ufWLOQQPofRDpGRg1ZYtmUD20Qi_Iv5tckwVMLrNTtSekqYUFp2jl3LpRASbI5KyA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dba53081a0.mp4?token=a3WQ-JTuweHlqa77sHDdIu_5B2vGbnJ-M43Qi6d1h0tSg4jLqxxC_hdvRYdqS6T4wzmzMsY5hFv-Y_LDDM1j_kqrVTb2PdRWyaa18Y2MhoICrtmOhJ5br0kF96ywUtjfuzAAUhOhu2FNVFKcrQi6y99O13nDorIweYzrCawzCvwM-qkuE1ZdjIhseYoMVjBHq4ELg7PXuObNOQaKRS3mvjNxT-yf276SezfS4JINOq012Yi_H8QHMD9nvcSbeJ9SDIAK32R_F-S1umkeIGrU6ufWLOQQPofRDpGRg1ZYtmUD20Qi_Iv5tckwVMLrNTtSekqYUFp2jl3LpRASbI5KyA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
❌
🇮🇷
حمایت جانانه بهتاش فریبا عضو کمیته پیشکسوتان استقلال از رامین رضاییان: این‌که چه‌قدر پول بخواهد حق طبیعی اوست
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/Futball180TV/104389" target="_blank">📅 19:58 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104388">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f2fde5e301.mp4?token=poaZx5bOshnLl8PHQYjDLoIKuyPF0EQeimAhF4rn4MEsa8tqzzS6k0SYAUASgx0lFyKoY2oP97xhz_GbltlWPxwPDlGnC-IMu6MEhyAVq1Q0EbEi53AxL4wjWaZ7BkJoaCzcNDmycRaHX6_GXUpszGhAPEBKzkt9YUk7g-DCMQPlbOeosFV5wxK1x5t5SsVURUGWFlwPb0RDoNodLJObVZFV2mboEOywiL0A5_HK4Bhto-HstquLtJPIyEvWC26qBlnBSYo3apb_zFMunw7vLYgNw1rAUYl96GonXynDlaLMWApKB5NvjAaf9-VqVzTOwS8toE2qHFzM_7CVc2J8DA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f2fde5e301.mp4?token=poaZx5bOshnLl8PHQYjDLoIKuyPF0EQeimAhF4rn4MEsa8tqzzS6k0SYAUASgx0lFyKoY2oP97xhz_GbltlWPxwPDlGnC-IMu6MEhyAVq1Q0EbEi53AxL4wjWaZ7BkJoaCzcNDmycRaHX6_GXUpszGhAPEBKzkt9YUk7g-DCMQPlbOeosFV5wxK1x5t5SsVURUGWFlwPb0RDoNodLJObVZFV2mboEOywiL0A5_HK4Bhto-HstquLtJPIyEvWC26qBlnBSYo3apb_zFMunw7vLYgNw1rAUYl96GonXynDlaLMWApKB5NvjAaf9-VqVzTOwS8toE2qHFzM_7CVc2J8DA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">عملکرد ریدمان محمد صلاح در بازی اولش در ترکیه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/Futball180TV/104388" target="_blank">📅 19:58 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104387">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromBetegram</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SbEzuPs-Rj1dgOtAw3r14mz-PWU465w9xGqLQ84eu2taom5rFtfuz9gsTXl7l3bxOBZDtWFd5QI15Mc10XJ46w-k_6CWj9V4SZZePK0egjEoTLpVmCcc3_edg90dqG9szLdgi6jk6isIGNtWHy31WX3lKT6BJpQPb9AuuY97gaAnLKucbsS14qjahxtZrtWzUhi0Vg1-lHH2lD5soRMzCN8wUbF-tFtMyFtTP3mGzP_nz5lqCqO17OyJNk1cFqV_Y84aFd6EroxzQkI61LctQIX0hFLfnCOkkZOYRLXxjKt_lRCDXYEMm_SYIYZn91GdoiOWjOoPdtgFQARe_e8vqg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
هفته دوم لالیگا اسپانیا
🇪🇸
اسپانیول
🆚
رئال مادرید
🇪🇸
⏰
ساعت ۲۳:۰۰
🔴
بیش از ۴۰۰ نوع آپشن پیش‌بینی برای این بازی در‌‌ ‌‌بتگرام
🔼
با بالاترین ضرایب پیش بینی
💵
واریز و برداشت ارزی و ریالی
❗️
🔥
۱۰۰٪ بونوس رایگان اولین واریز
❗️
🎁
فرصت را از دست ندهید! همین حالا پیش‌بینی خود را ثبت کنید و از بونوس‌های ویژهٔ Betegram بهره‌مند شوید.
🔴
http://betegram.com/affiliates?btag=3_l7</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/Futball180TV/104387" target="_blank">📅 19:57 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104386">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/54d02a0a5f.mp4?token=pNoEEctvo8OFTq-eO5pdxpz3Mxh8D3nL0JPnrZw6v7LmyiR6fr2nOZcU9ddM8M3PLozu0kLYwp1erR-8mh451WB3Qyoajez1NeHIgZ2_4uKy-4N6m0oga1I1_zz_8LubORSq9d7Z5fFUtZ-EJrR-DhEIbSiSzOnZ4Q2KYJSnbrPlEPiKt6uEX8EuSmKJ6qVwucl1fhejadwdN6QwyHsjz1YxRjx_r_vVwccOpmAalrBm-ocMaYrgSbtyYRdRdwvIX3M3yOn7ignPnUYQ5PDUi8f6I4At43jP0fneK7uE08n5-W0lqYuxQ2sRAXIz7N3NeIzmX4sk6mH6lDBTqDba1g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/54d02a0a5f.mp4?token=pNoEEctvo8OFTq-eO5pdxpz3Mxh8D3nL0JPnrZw6v7LmyiR6fr2nOZcU9ddM8M3PLozu0kLYwp1erR-8mh451WB3Qyoajez1NeHIgZ2_4uKy-4N6m0oga1I1_zz_8LubORSq9d7Z5fFUtZ-EJrR-DhEIbSiSzOnZ4Q2KYJSnbrPlEPiKt6uEX8EuSmKJ6qVwucl1fhejadwdN6QwyHsjz1YxRjx_r_vVwccOpmAalrBm-ocMaYrgSbtyYRdRdwvIX3M3yOn7ignPnUYQ5PDUi8f6I4At43jP0fneK7uE08n5-W0lqYuxQ2sRAXIz7N3NeIzmX4sk6mH6lDBTqDba1g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👍
اقدام زیبا و تحسین‌برانگیز بازیکنان اولسان کره
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/Futball180TV/104386" target="_blank">📅 19:52 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104385">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/UDh2pgpSk5T3U_syxEk6bSZ_DRSTxRuRHg12Bv0qtdFcbxY68W2hFhh14KKxJaE63BYi7PnTVcgVxEzNXAlYy6nVaCb9FDTb0sd0ipfN1goGx14E3FjdcSGhrl09gphCfxjNOmCJ3WnQ0Fkp2M9-l-4Mu4BqK32imaVsBMyDMfMvG5cFfIj1AXTLHVA8oCwYHyo_Sz3Yx_0ppq0qrAT9pKLxIUUHZ9I9hZUVDuaLM6Xe3-wPdzmz6n2ddcTET1KJEXBAy9Yt0aNX5UEpjPFw3b9_-VHGflLj1StR4SstG9We-LUbw8_dPKisRq90v4TephV_OUY9QWoSYhgw3yNzPQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🇮🇹
🇪🇸
#فوووووری
از رئیس باشگاه اینتر: بهتر است بارسلونا خیال جذب لائوتارو را از سرش بیرون کند چون هیچ راهی برای فروش این بازیکن وجود ندارد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/Futball180TV/104385" target="_blank">📅 19:40 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104384">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f33114edb2.mp4?token=Kuzg5hbW0eTFX4_CeWQRyGhqdHGfVNtBoH6EwkXLGzVYqnpqrsJKnBoGGhSARywOINrkfykjEsxKRWVm8VcJvAXYmLZ1UoGwuTnzM7qd92vdq0OjTMBnPRtjWLlLSjs_5j5SIFVN8aigP-CTxvRFVZRsq0_v5e5A5y3yMH7DVnbZSnlDoerm1szFDg5xaYQ-8aOioKRsu3lwnx2WMjk8hto7_oS8G3f4XglOoRs7qo2C2Oq2jweUdV3ZUNznRV4hM1a7vFy_R1_EKEY0LjSaMF-AlcCEFsbdqe5pIAAI6hBfOsF2UbLw75bqg4EPiNWdWCFTCx05vO3CKcQG1PMPow" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f33114edb2.mp4?token=Kuzg5hbW0eTFX4_CeWQRyGhqdHGfVNtBoH6EwkXLGzVYqnpqrsJKnBoGGhSARywOINrkfykjEsxKRWVm8VcJvAXYmLZ1UoGwuTnzM7qd92vdq0OjTMBnPRtjWLlLSjs_5j5SIFVN8aigP-CTxvRFVZRsq0_v5e5A5y3yMH7DVnbZSnlDoerm1szFDg5xaYQ-8aOioKRsu3lwnx2WMjk8hto7_oS8G3f4XglOoRs7qo2C2Oq2jweUdV3ZUNznRV4hM1a7vFy_R1_EKEY0LjSaMF-AlcCEFsbdqe5pIAAI6hBfOsF2UbLw75bqg4EPiNWdWCFTCx05vO3CKcQG1PMPow" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚽️
گل‌تماشایی ساندرلند در مقابل ایپسویچ
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/Futball180TV/104384" target="_blank">📅 19:34 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104383">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AjvZgtMAFNlHIG5zatMfh1xbiUffuB7RrX9RxuzlBPr_FQm93exU_wgD-D0p7dDNaKc1fsse-okt__-2CSyqlHxwM_Rm1kDQ1PaHqi8WOA_MXW437KpXTGe9MOjZ4EnaOjPqgcgjo3PwSH8d6elhLyvdPo-PQFjNwBTpb1pxtmfxlwM4SybTrJMxMUWKOZNoo38V6n4lv9XF5IfjkQWBtZ7kjMIG_EIbv6T-o_J9lX9y_dq_nR1A0zuGCpAxPYVGjdKff48iT75IeCHHQNoY0Db-G3_FVMQ4nUYtUmu0LT0ooo7MPcwIao5mAhLXPyLs5665QOPt4B68Yt-zkyextg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
🏴󠁧󠁢󠁥󠁮󠁧󠁿
رومانو: دو تیم شهر منچستر به جذب بالده بازیکن بارسلونا علاقه‌مند هستند
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/Futball180TV/104383" target="_blank">📅 19:33 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104382">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aqna2Y4Q3Y5CfdxUHZWzpKBKSOfKOoTo1WPrT_xNezo0pgoBT8EyFvaRZti0rn3Tg2YKt3q3w70kbTGRcKSZa5y2j0DhEVIYx43yH5jd8EIKEMqodKm-bza1CQydEJgPBiZBABb5vcWxFzUP9USJ33pAkcD9xOy5JCTqnc6nVmzG-A28YzgdvXBAOvWbl8qiAFL4mKoJmJmLp9vuS8EY3Tza7Oyy23Hcn6wCfR6B4SD_ulrgVKK5jNtu-L3xF5EwgCW-egGOo4bRT-Y4Zu4Z3FeqU5p5bAlv_tswTgopdqmxcRgTtDaWmATRVTX5053Hjrh6JkCdJZExS8RHlWz0eg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇹
هفته‌اول سری‌آ؛ ترکیب اینتر مقابل مونزا؛ 20:00
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/Futball180TV/104382" target="_blank">📅 19:23 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104381">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/45250f7e28.mp4?token=sQ6T9-x1aSmiBs1ihT3ZmoP2rsR6NAdB6_SlXGgEVjdN5fjzmaTh-XR03Wztzn9lqSJCUCiWFE9aRmFfNxms8Wz-lcY1gWRe6WpWo8fYi1TFBK1i3sPwB7Y-jbC0T1KNjBd2NSOP4evxEZiCJo4niUI01aNdSvFY8kVPTnzclYqQ_xO_hR50B8B_WJH9-LhwuSYZ5eNpj0qoysOrFWnHSZpeW97quZnF8IcIg4LjuHs1YCZa1Fg3_LRFuQy8OlZNeRl4Ow5a4oKkalAGHjAn9bpNMVfCWA0GWHhUn9kyboJLiiGAKtco0LrUBJBkVp8P21gp-2t6WimCLBwojmWmWA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/45250f7e28.mp4?token=sQ6T9-x1aSmiBs1ihT3ZmoP2rsR6NAdB6_SlXGgEVjdN5fjzmaTh-XR03Wztzn9lqSJCUCiWFE9aRmFfNxms8Wz-lcY1gWRe6WpWo8fYi1TFBK1i3sPwB7Y-jbC0T1KNjBd2NSOP4evxEZiCJo4niUI01aNdSvFY8kVPTnzclYqQ_xO_hR50B8B_WJH9-LhwuSYZ5eNpj0qoysOrFWnHSZpeW97quZnF8IcIg4LjuHs1YCZa1Fg3_LRFuQy8OlZNeRl4Ow5a4oKkalAGHjAn9bpNMVfCWA0GWHhUn9kyboJLiiGAKtco0LrUBJBkVp8P21gp-2t6WimCLBwojmWmWA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
🇮🇷
فوتبال روان سپاهان محرم نویدکیا که با چاشنی بدشانسی همراه است...
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/Futball180TV/104381" target="_blank">📅 19:22 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104380">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-text">کانالی که همیشه در مسیر ورشکست کردن سایت های شرطبندی حرکت کرده!
😈
آمار ثابت 90 درصد برد
✅
فقط کافیه چند روز فرم هاش رو دنبال کنید...
⚽
@Tipster_Mafiaa
@Tipster_Mafiaa
⚽
@Tipster_Mafiaa
@Tipster_Mafiaa</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/Futball180TV/104380" target="_blank">📅 19:21 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104379">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from𝗧𝗶𝗽𝘀𝘁𝗲𝗿 | 𝗠𝗮𝗳𝗶𝗮</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YdSIgaAj6J6AmZMMR-CB_tl-Vm595zMsPz34tLSxF_L4AMAxs41HVvniWUVSyc_YY3a6LQt7hWMXfqdgzK2lqc7wDh7ivxe6QC6gBcMCMk57uZnurvXEwe4oQHbJSQtFDsmbPC0jNZN7pBLTfgz7v8iPxV1obdJ30UVpB2VJ71Y4afMxIv0opn_KA-qfnahoHe_xneGnglqIOCt23lDa7DRiv0YQn23mUo-ZMM_gmEEFBquW8BiOpQn7hSlQtA9LDpmDGGOBu2QcnrTLHpybUodvy0a7pchSGJIvPCN-RZSCrQLupECzEE1Dxrw11D8YX_em_Kg2Zamd-Mw-PoseMQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">میکس عالی برد شد
❤️
☑️
✔️
@Tipster_Mafiaa</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/Futball180TV/104379" target="_blank">📅 19:21 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104378">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/86b7ad297b.mp4?token=uyCylxNiF9cUFPbSaHJmBXFunfkrSia8KDgF_aKVIhnrHyhYACZp3BFNi70QAQrtrLQnVOZly3ilq4DE-cicq7Z4xluPNddyd1m5UwPprjAXGEahXY58e5xRkwUWJ79nQD6cKcC98_sYWxEwCSyIswIeBKAldr2t8vovkbQUaaI0qPwxFZSYM-ON5-6pH-PbHN2JWn6-VASwb7u3crPyG868E7HZ8rdEMFUwOzVQvHle4Tl7AXPbcBdiUa3vYQkDTaAvI2q9zQXDgMvhfZBsiWqF_OnqKHmqG8oVXm4POUg4Dw3WCmisHTkY8WaEDcaAluMKeWcyzRueBlbCLIfViw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/86b7ad297b.mp4?token=uyCylxNiF9cUFPbSaHJmBXFunfkrSia8KDgF_aKVIhnrHyhYACZp3BFNi70QAQrtrLQnVOZly3ilq4DE-cicq7Z4xluPNddyd1m5UwPprjAXGEahXY58e5xRkwUWJ79nQD6cKcC98_sYWxEwCSyIswIeBKAldr2t8vovkbQUaaI0qPwxFZSYM-ON5-6pH-PbHN2JWn6-VASwb7u3crPyG868E7HZ8rdEMFUwOzVQvHle4Tl7AXPbcBdiUa3vYQkDTaAvI2q9zQXDgMvhfZBsiWqF_OnqKHmqG8oVXm4POUg4Dw3WCmisHTkY8WaEDcaAluMKeWcyzRueBlbCLIfViw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🙂
هیچوقت این صدای تاریخی استاد مرتضی فنونی‌زاده از ذهن و خاطرات پاک‌نمیشه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/Futball180TV/104378" target="_blank">📅 19:05 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104377">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lGgS4fEfouQQHswEYHcC8vGuSCtEOnUWuzBX1yCnr_nskby_U0byJguRzN_SDwigLMtPtLcGJYQL4lImub4rNHOiL4Gq--GkI-nHzT22nPKyeQCEV00gTFxL_HhzkcTVnUF4J9IbLlYYBgoeUiDhTh_eJUPKeAwm3n_QwjE2u6XtdVGghYMOsqsCjDXIMLFKBmCYH0qd7fg7rtKMNYma68t6XltccBQ6Xt34V4oY0u4CFkHp_PidZ4KlLSzgVG4mzBKZXjKIL6ub24EhtHFE0YVNEow48azknl1-V8VtIOeYNgiKIz_Is0QDu2s8bPcYOpp-0AxInQKoh8GxeU9_eA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇮🇷
🇮🇷
پوستر کنایه‌آمیز گل‌گهر سیرجان برای دیدار فرداشب مقابل چادرملو اردکان
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/Futball180TV/104377" target="_blank">📅 18:41 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104376">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1ed1c9346a.mp4?token=leGHl_LZQMPo91GRcyviMer9KnF-ERF8rLCW9sCOI4Jho_v4Q_PUxMzEJZVCeglPL7ZH-dR6fHD6q0eclU1JDBZGeE1TPqDyaVy9GE8DBcs3f8pcK6pXdRVuu99Xwbnm9e-u5ZCwFFuRScE3wsllGbKf-9EoLa8jNNBrAke_J1pJk5leb-zJYZn-6oYOhmtAd1BVlww2liYPeGShLkQCDFEC26y8KDT_gBujpSbjgmnFrsTSXVf0ni1JwniEjqC_2x-6mi0jTYb-ylEczeyIl08kbKSOtO5EECR-UtSff9CMpewXHYJ9LPZl6j1n7WeaWjVLrJjnzZaie_gdek9CMA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1ed1c9346a.mp4?token=leGHl_LZQMPo91GRcyviMer9KnF-ERF8rLCW9sCOI4Jho_v4Q_PUxMzEJZVCeglPL7ZH-dR6fHD6q0eclU1JDBZGeE1TPqDyaVy9GE8DBcs3f8pcK6pXdRVuu99Xwbnm9e-u5ZCwFFuRScE3wsllGbKf-9EoLa8jNNBrAke_J1pJk5leb-zJYZn-6oYOhmtAd1BVlww2liYPeGShLkQCDFEC26y8KDT_gBujpSbjgmnFrsTSXVf0ni1JwniEjqC_2x-6mi0jTYb-ylEczeyIl08kbKSOtO5EECR-UtSff9CMpewXHYJ9LPZl6j1n7WeaWjVLrJjnzZaie_gdek9CMA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
👀
از حواشی کمتر دیده شده بازی استقلال و نساجی؛ عصبانیت سهراب بختیاری‌زاده از حبیب فرعباسی بابت انجام حرکات خطرناک!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/Futball180TV/104376" target="_blank">📅 18:32 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104375">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6820414d13.mp4?token=sfqJN0zpvsehJDy-quZ8Fao7iWPKcCYB2JXS_rRPJ9XRWAKYEAoiJAT6tACGIiD2RH9lH6YCZEzwz5dNgA-8-a9K1aTPU2v3IM0JW7pE0qtzwNPKNyEEp_cx17TUj-YPyf8ipT9x_yXrQ8fZW9ehI8v3fqhqAiIA-E_JMCooxOp9h9ZW8rRnKgt9CBjXQ52WuMJzF0jwljCq5pPYlknmpClR0gnj7IKn_2StU5eGBtFkqkIBEBWKtpghfeRoYNrS5KvV361vT945k2VOESJfU9Ck9jopJdP2HL0IfRlRqh0BOofsaoBhGYfr9nzWviNTA0ksQw9kaLkUNOUeQ4e2wQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6820414d13.mp4?token=sfqJN0zpvsehJDy-quZ8Fao7iWPKcCYB2JXS_rRPJ9XRWAKYEAoiJAT6tACGIiD2RH9lH6YCZEzwz5dNgA-8-a9K1aTPU2v3IM0JW7pE0qtzwNPKNyEEp_cx17TUj-YPyf8ipT9x_yXrQ8fZW9ehI8v3fqhqAiIA-E_JMCooxOp9h9ZW8rRnKgt9CBjXQ52WuMJzF0jwljCq5pPYlknmpClR0gnj7IKn_2StU5eGBtFkqkIBEBWKtpghfeRoYNrS5KvV361vT945k2VOESJfU9Ck9jopJdP2HL0IfRlRqh0BOofsaoBhGYfr9nzWviNTA0ksQw9kaLkUNOUeQ4e2wQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🤡
🏴󠁧󠁢󠁥󠁮󠁧󠁿
آغاز قدرتمند منچستریونایتد در لیگ‌برتر
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/Futball180TV/104375" target="_blank">📅 17:47 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104374">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/L2QGpjKjmFf2G6mpcUVQatJwk-xR4ZZ7Kc70MwKj74D6LAFIt8-OKVvueFjsi7logdBlH5XPVNHD0WomhqC5UKKwBRSspgkiSC8BD6sBIrIPPi_GTOata6byF6f6OqII2KpCtOUooGQy1kYU59NY3V8hfLCJ2MZDs81d0-SnrY9r7TbdT1yUaNt53grnNtQWtgIv0QAfrLZ7tkAFFGnl4aCWjV6QJtLghhj8-5Z0LFzM7gVED10Aic6odNClpB6RHxn9oyePa2K83OjmJAfR4jPwKfSfY_bp-Yc18uYvlPk1Ui7Zrc7E8oeAaTglNSFRb_3Va3fktqqeig6L9Hltgw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🚨
🇪🇸
#فوووووری
از جرارد رومرو: آلخاندرو بالده مدافع چپ بارسلونا طی روزهای آینده از جمع شاگردان فلیک جدا خواهد شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/Futball180TV/104374" target="_blank">📅 17:27 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104373">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VyJ1lDPoOUYJpYAvnEF3ZV3xbQBwZje1PGL1Nj2oJ9GH8h1HVCFm54nydpD9XnQB6nshpofEvL_AQJp0xBiBfUB_5MlCGTRKFIUjobHNEYjdvSvsH88WhkCNH7Hs8HNnOwiIHnMvxHB72iZu-FeTEHXAmRENQI3Z1oVk_eNqznSOJ9Q0B_y-mrNgqYu6j1uIAhZYt9hk_LdnRSdQPufbPnbQqqKQIuJg1L1gA4FPhWwH-FdEPvl6lMZsIrhboGq1_qG4W_-UR8i6vwPlWFQMYTuWcozx3kIS3bRyKmxYRG49DaCtyhF4bjHCGfQXSteDWzSwe0t0AJTG8zY9OT_v7w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
‼️
📊
آمار پشم‌ریزون بازی منچستریونایتد که با شکست شاگردان کریک همراه بود!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/Futball180TV/104373" target="_blank">📅 17:21 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104372">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CO_DYQPwagZcU82Xr7qfy47Ry2UYnRMKULyAcPwDwWM4AwCU8ZHCE8EUwK429TUA_8q8xX9HjhO8t8KV98KekS775Fz-TiIwwvxVOBXWcuiDZtipk0a0Vdvv8H0V0OwXS4g_cbD87YuJ-_uaMP1LSdW-fzsqeQZIs-4KNnSIeH62qjHVPeFzBsFxnKZMoSjcu1LDKSCnswMj1rWjghCAwm-XrRV2nVLQqBX5VNGCSCMAOkqHPpbV9hKkzzHfNwiQ-6Rd5nfbtIjxry6theW2Pz8vaWyHv0r8IH0p1uXw_kKcX4ax4EZBJvO_nUWAbtW-nlAzj1yMr78R6oa_7cEnhQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
‼️
📊
آمار پشم‌ریزون بازی منچستریونایتد که با شکست شاگردان کریک همراه بود!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/Futball180TV/104372" target="_blank">📅 17:12 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104371">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uCmppvx27nUZ0iDE3NrzrNrrYfAqty5cjOT9Q6bLqNG9xVWamswtFOKt2dgoTycincDjvzE7rV-aenIh1OORSUztix8yXzjL4xUMNzGgTQAXg6tFq_4HXXqwrQBrjXunFEFnt9VC_9kfvm-78lYaTWHcLQ8b_xdP0x3mCto2__UzZ59xbo2Mm4dwyrbwH_RZjuiLO4Qw29HchHzLLjhvLhSO7DpHBxApLHpJR7N3AVgJ_pr60eq8Eo-y1SZIuqzX6ORuqu43rPYFW5P3LF-t5qh1Xtis66QgDVhawl4VQazrHsrs3SQMOzJw-YpRLfmeHYuGYeXn3oP-Ow_XIYnudg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
علی‌علیپور مهاجم پرسپولیس و همسرش
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/Futball180TV/104371" target="_blank">📅 16:55 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104370">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UaArx1f21MIqvSSw0bNqd7nI6JkFW4Op0UJhKpD3EQazJh74aBLlRu2GX43f3cJ9f2LCrrpEKt6UJB_wecT7y5EKZwAseR33ecn0Hwjo9XuQcS146778R9Awiwx-1mNFK16tT2qsW_V3BQmUB5rxvXnVwzBVSFpZvlqc4ueIjxJH4B1qSa4dxB22yFlIGknBlg1DwrRSbAQV4BxMt53ji5yLgZa18rj04IcOf5MJttRoj-hFHF8fNdAODd6uYrp8IJ03-J0-OkvSE3BQa085dTD3L9-ptvJZJEiuH-socVZI-QJ4fuBJbYHwLg_Ge_mJt2tJpl02RNK_LEj7d_5ECw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
⚽️
تغییرات شگفت‌انگیز سرمربیان بیگ‌ سیکس پریمیرلیگ تنها پس از گذشت ۸ سال
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/Futball180TV/104370" target="_blank">📅 16:34 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104369">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1a75f897a8.mp4?token=gmEqO8ckQKsUBQU2V7O6LazDlH7wyOPBRequVdXWgBIqiE5hUdncqU5P4-dTfP-P3q30ToQtn_a2HdD27I8hNOQshtPDL2_ZU1n1cRXmiT5_ETxRcE_WC8lEyWq2yXb7AiBS6dMP377ZjpNg7yZZhtIrIqTa4aX2XeUXhqUcnXOFsqOFYH0dzf78UF8jmEAkXgSrLwKVChPfe77UniuQ7C_qL672nvdvFjgs6tCe5y9zc3hzXWu71bm5jxK5XVLpGoChbl_6QV6GLimWPkmZOLjpd4MnfmK6kjjqqzoUFRmBKrNNqtOMnqXQLQlZiYFi-kXYJopnWuFI-lGOgIJ7ww" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1a75f897a8.mp4?token=gmEqO8ckQKsUBQU2V7O6LazDlH7wyOPBRequVdXWgBIqiE5hUdncqU5P4-dTfP-P3q30ToQtn_a2HdD27I8hNOQshtPDL2_ZU1n1cRXmiT5_ETxRcE_WC8lEyWq2yXb7AiBS6dMP377ZjpNg7yZZhtIrIqTa4aX2XeUXhqUcnXOFsqOFYH0dzf78UF8jmEAkXgSrLwKVChPfe77UniuQ7C_qL672nvdvFjgs6tCe5y9zc3hzXWu71bm5jxK5XVLpGoChbl_6QV6GLimWPkmZOLjpd4MnfmK6kjjqqzoUFRmBKrNNqtOMnqXQLQlZiYFi-kXYJopnWuFI-lGOgIJ7ww" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🙂
دوتا پیرمرد پرحاشیه سالیان اخیر :)
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/Futball180TV/104369" target="_blank">📅 16:05 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104368">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bc446632ea.mp4?token=HhEpvr9VxH6e-0V5YzVMEeXgCb0UBS6NmtPhqpAJ8di_9M83l1tfY-zU0KAIO_RKeQNeVJv41ljE_giOzrQryG_VJtFG1HxDJfBgJ9g3C0bcHY1IzE-DgNrDYkzsl6Qy06WiCgu_7GTNvQMV2XOW82tR7GlputCjiuuh9OBJXdYK4OUoHrOgbXfe_1zSp_XWD7_1slpq9NzOBmoaIEI0sIVdt22UefT6XyrwX_sBkolHSwIfCpsIwPNQWkbDp6uBxH0YDZr2Yy_Iq8eH5Y7zmGUJDN8XMiDBC_EexUUH1__tSePPSIYR4Jfc41eS4Te5gZ05LHhb2FT-nrLXRDw0Pw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bc446632ea.mp4?token=HhEpvr9VxH6e-0V5YzVMEeXgCb0UBS6NmtPhqpAJ8di_9M83l1tfY-zU0KAIO_RKeQNeVJv41ljE_giOzrQryG_VJtFG1HxDJfBgJ9g3C0bcHY1IzE-DgNrDYkzsl6Qy06WiCgu_7GTNvQMV2XOW82tR7GlputCjiuuh9OBJXdYK4OUoHrOgbXfe_1zSp_XWD7_1slpq9NzOBmoaIEI0sIVdt22UefT6XyrwX_sBkolHSwIfCpsIwPNQWkbDp6uBxH0YDZr2Yy_Iq8eH5Y7zmGUJDN8XMiDBC_EexUUH1__tSePPSIYR4Jfc41eS4Te5gZ05LHhb2FT-nrLXRDw0Pw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
▶️
این ویدیو بسیار کاربردی برای زمانی که در باشگاه، دستگاهی برای تمرین خاص وجود نداره و باید از راه‌های جایگزین حرکات رو انجام داد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/Futball180TV/104368" target="_blank">📅 15:50 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104367">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0deddd0d6c.mp4?token=ZpvKUYq15MGih6olatWyDRbhFlZJKfWFgPBx_3-7Ww4L51s63Q7RF-l18scxMTnyC8sRCApyiAP4mueFVr2c-0_T8B9layP0zHfCLVldBOd7t48Iwnx5RvhfPZfEuwx4YcWY1nd5OAEZp4jeEb09nGEzDNVyzXlZgOW85vuGHQ97cDM9L6cliltAeaHvlaEynckLdoWrybsYxhrpcoIyDSazIBm8oI5ZzaubS_eh_DTybcwtnM7g9Lpq86w2vuG6saApHoi7A2WGiTSXwkV83lUhmPs3ZYYD013L2dkVeahHg1xGEib2YhXn5BneMNEI_0Zx9HWw_jqVDwJeW8O_5g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0deddd0d6c.mp4?token=ZpvKUYq15MGih6olatWyDRbhFlZJKfWFgPBx_3-7Ww4L51s63Q7RF-l18scxMTnyC8sRCApyiAP4mueFVr2c-0_T8B9layP0zHfCLVldBOd7t48Iwnx5RvhfPZfEuwx4YcWY1nd5OAEZp4jeEb09nGEzDNVyzXlZgOW85vuGHQ97cDM9L6cliltAeaHvlaEynckLdoWrybsYxhrpcoIyDSazIBm8oI5ZzaubS_eh_DTybcwtnM7g9Lpq86w2vuG6saApHoi7A2WGiTSXwkV83lUhmPs3ZYYD013L2dkVeahHg1xGEib2YhXn5BneMNEI_0Zx9HWw_jqVDwJeW8O_5g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🙂
‼️
هیچوقت این مصاحبه تاریخی مدیرعامل ابومسلم روی آنتن زنده با عادل فراموش نمیشه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/Futball180TV/104367" target="_blank">📅 15:40 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104366">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b033bca880.mp4?token=aKy5ZyXrSm4dqDDTuhjEWqYzzaDtVTsaY7sqa8Y_sWQsjVinen212OEgu2emVewbGk15zKYoMBX-3SCM2qoEOEq4Cp3-ldO86KNFM--NyUxGey52LpN4Q3gOxIB7jOdD7lyfj1Lx4h25hG8jcUecmzxrCfDprLLUYyzphjY2CUBzlwH3MICI6rnDe57V4Lz5d2qixYB8lEkKV9hsSD25kHcxK0eo2Tiz3DNUFg3OOBHypkGo5GHFupHgwXBVu8DbrGFs12t_Un7P-QPvmiPUSXRxeplAdVhnulYNN-glh6lO0X1y2EwLBgDhRLcuQL6OGewo-84AzJ4Kj0kPjE0kjoWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b033bca880.mp4?token=aKy5ZyXrSm4dqDDTuhjEWqYzzaDtVTsaY7sqa8Y_sWQsjVinen212OEgu2emVewbGk15zKYoMBX-3SCM2qoEOEq4Cp3-ldO86KNFM--NyUxGey52LpN4Q3gOxIB7jOdD7lyfj1Lx4h25hG8jcUecmzxrCfDprLLUYyzphjY2CUBzlwH3MICI6rnDe57V4Lz5d2qixYB8lEkKV9hsSD25kHcxK0eo2Tiz3DNUFg3OOBHypkGo5GHFupHgwXBVu8DbrGFs12t_Un7P-QPvmiPUSXRxeplAdVhnulYNN-glh6lO0X1y2EwLBgDhRLcuQL6OGewo-84AzJ4Kj0kPjE0kjoWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👀
💥
لحظاتی با لائوتارو گزینه احتمالی بارسلونا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/Futball180TV/104366" target="_blank">📅 15:15 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104365">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9536e07d63.mp4?token=Gt8nb-qAJJXkANMa_pDbOYLpY5vkcbGV2ASXgoanRVeRsjwXk82qqUvDraIv49sYaTJcY8pGJi2Mp9ygzwWZEspi1OccRmGUIW0l9X7iIrfkVQx9VP0buc1MUyWMTXIpcOo4xrIiP2sWNaxOb82a2yp9v7xiUZotc2LEot63CI2vYE2BcdUFyyjoMhIRop-NrtPPFetBjh0fF53fg_m8QBp1fSJbj0OluW2WqQe-OtiU2CnacQ22iQ34I5dtAeop8altQQlbOpP8d_4dSbSplGi74TJu5Z7fKLIoGodhciW3IbzUMFRiVZ46dut1dSK4W9wtDutxG1UwnpiCDGaoOw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9536e07d63.mp4?token=Gt8nb-qAJJXkANMa_pDbOYLpY5vkcbGV2ASXgoanRVeRsjwXk82qqUvDraIv49sYaTJcY8pGJi2Mp9ygzwWZEspi1OccRmGUIW0l9X7iIrfkVQx9VP0buc1MUyWMTXIpcOo4xrIiP2sWNaxOb82a2yp9v7xiUZotc2LEot63CI2vYE2BcdUFyyjoMhIRop-NrtPPFetBjh0fF53fg_m8QBp1fSJbj0OluW2WqQe-OtiU2CnacQ22iQ34I5dtAeop8altQQlbOpP8d_4dSbSplGi74TJu5Z7fKLIoGodhciW3IbzUMFRiVZ46dut1dSK4W9wtDutxG1UwnpiCDGaoOw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
🇪🇸
توصیه های دیدیه‌دروگبا به دیامونده
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/Futball180TV/104365" target="_blank">📅 14:50 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104364">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a301749a37.mp4?token=NSAaKF_qCNDExGodvqiQO3Pz-151uj3lgNcWX0ODC3NSesF8RTNKlaQNftxlTbuS-eMtWMDAhi680H8hPwb3ykXIPoMhGCMfOUk4fcnNiw9BTJc3oGMk3H5dzXVLCBU7kCCsROHtC4nIo2SjHF4OmN9Xd9BP0oBErEtqbOonnGYElmXKcfQ_rqHfnlJRH-u6HA-xr8VD835fV2Q-sJ5gX2GAC4nJZYtHtf_Y_fw9hGzbrIfWGjM5EFDR5a4BFgfzbgfi5n8twgrjlvaE-xTM15sqfs7Nxl4vva3l7-3tpjWrJSYBn59YbscnhNCqcEt6lGP3Dnil0GkJf2ew1UJ67g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a301749a37.mp4?token=NSAaKF_qCNDExGodvqiQO3Pz-151uj3lgNcWX0ODC3NSesF8RTNKlaQNftxlTbuS-eMtWMDAhi680H8hPwb3ykXIPoMhGCMfOUk4fcnNiw9BTJc3oGMk3H5dzXVLCBU7kCCsROHtC4nIo2SjHF4OmN9Xd9BP0oBErEtqbOonnGYElmXKcfQ_rqHfnlJRH-u6HA-xr8VD835fV2Q-sJ5gX2GAC4nJZYtHtf_Y_fw9hGzbrIfWGjM5EFDR5a4BFgfzbgfi5n8twgrjlvaE-xTM15sqfs7Nxl4vva3l7-3tpjWrJSYBn59YbscnhNCqcEt6lGP3Dnil0GkJf2ew1UJ67g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
🎙
بهنام ابوالقاسم‌پور: برای پژمان جمشیدی سند گذاشتم و او را آوردم بیرون ولی هنوز نرفتم سندم رو در بیاورم.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/Futball180TV/104364" target="_blank">📅 14:25 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104363">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0a5d5ff55a.mp4?token=LqitNLK6qmz1RxlSpB-IUTvjI-vi0J2qwM3W_WEh0HoqyD_kSnhuxKmluJltzBqwVIvjq0JFCB_RqpHoEFh2VrMnIHDhT5lic90aAymKTpYMSa_7ue3x4d6RA_NuszGQ3xEsf3yKdwub608tbAag5diUOJ2gbAATt6L4U7ad1H9W3KJD35Blyp05Sw_nTI-lRee5ftMIXlRh2ovT4c7KWZHReo0TrxK2j5iJQwrN6dOqjt2Kcx8gFfzrvc_9pn6fB-U3doYtxxfVw1f0NEAZ0qoehXD6wEe67MK6fcj9te3WXH9ZcvkIFTXzf8EpS35rdpro_q1HwceMr0B4n-VEAyOnsOvnBRLlqfe24AAOIt6OOQQWr2HcAeJd4h585aT_KhFcFsj8lAeW4orsHaa2M8rCCMxKvgq734WLFIyIaS1zTAtp9t0qong1h-R1Wa4K8AJQTgudxNrnvI9Wm-UfINqksMpzpCcElyqePsuMKiPI5VXnxDv_odHA3ZTk3TUHlEi3RmziMooiGQVSMdEu0yUZRuUnzhtsUnPBLoIiHyyrKisbVIbDcPTHFDHj8-kz5Gp7cWyiaJxij0xHaBMBoGcr3VBS49BdDy3VqNBbw1iXGwYJEDkDHjsX6xBGkApQw2e_VVt-FNnv6yCCm41BWbO9tSMXK5dLtDcZSkWqJcs" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0a5d5ff55a.mp4?token=LqitNLK6qmz1RxlSpB-IUTvjI-vi0J2qwM3W_WEh0HoqyD_kSnhuxKmluJltzBqwVIvjq0JFCB_RqpHoEFh2VrMnIHDhT5lic90aAymKTpYMSa_7ue3x4d6RA_NuszGQ3xEsf3yKdwub608tbAag5diUOJ2gbAATt6L4U7ad1H9W3KJD35Blyp05Sw_nTI-lRee5ftMIXlRh2ovT4c7KWZHReo0TrxK2j5iJQwrN6dOqjt2Kcx8gFfzrvc_9pn6fB-U3doYtxxfVw1f0NEAZ0qoehXD6wEe67MK6fcj9te3WXH9ZcvkIFTXzf8EpS35rdpro_q1HwceMr0B4n-VEAyOnsOvnBRLlqfe24AAOIt6OOQQWr2HcAeJd4h585aT_KhFcFsj8lAeW4orsHaa2M8rCCMxKvgq734WLFIyIaS1zTAtp9t0qong1h-R1Wa4K8AJQTgudxNrnvI9Wm-UfINqksMpzpCcElyqePsuMKiPI5VXnxDv_odHA3ZTk3TUHlEi3RmziMooiGQVSMdEu0yUZRuUnzhtsUnPBLoIiHyyrKisbVIbDcPTHFDHj8-kz5Gp7cWyiaJxij0xHaBMBoGcr3VBS49BdDy3VqNBbw1iXGwYJEDkDHjsX6xBGkApQw2e_VVt-FNnv6yCCm41BWbO9tSMXK5dLtDcZSkWqJcs" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🚨
بخشی‌دیگر از مصاحبه اخیر و جنجالی حسن روشن که‌ کی‌روش رو هم مورد عنایت قرار میده!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/Futball180TV/104363" target="_blank">📅 14:00 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104362">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cdb917925e.mp4?token=efj3kfxpsQylKXAbBVH_8bEvmaL6hL_dukAGxt52JCCm6dR2lE8dsyXtLhctF9BBeZuJfDFosiJ5fZzrFqc6Ki1XQyOjXsShPz43oxlNJcqygMqY5KFvpy0q_ZgNfR1WAbNyOJYlEMwzJXiLKVjaxWbdttAdmz9B_nchKpzoio1MfmyIQRX4oSb8lwtvxfCuyGCV6xeBkE0zU0Z3mZIcOhg8mwxS2O1VDY22BgPCbcVUQj7sh7zRJBNScnOIONsoBRL22W5SxsFsjuqov1w8pyyA0ch7zjttvhl2nHFczevQhEENirtANj3iDE4ye9NjiaNcefUIVg2NDQ4-UAl0yxpBZoGDMH2iX02JTD7AZvZXtjuMwpbm3zg3g6Hd9t5gg1L1GxRSu0S01-zGH9_OrYwiE2nVlcBlSsjnaWGOU5sN3Iyne7U2uO8tU6lCrRBPvjHWlOnGFBJng9vj45D7DIJWQtUiIyqrbp3RV-T5W3ncfBeHlNqfGTBHURoMicQQGjZGsBihlN_cVIGJVo6SFfY2VRNGJMtmBEla4WcHZfPiF8ZLjPt0EpjJH-QaWyTmghaO3CEVIY2ddV1xcBM9zNBCq3F_NRi2aBpTasTiXnOGVXjjxkiCmEwPIiA576A6x36wArGSLBTeBDNMFDpmcJOw6o9AUS484B_Jhi5UWA0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cdb917925e.mp4?token=efj3kfxpsQylKXAbBVH_8bEvmaL6hL_dukAGxt52JCCm6dR2lE8dsyXtLhctF9BBeZuJfDFosiJ5fZzrFqc6Ki1XQyOjXsShPz43oxlNJcqygMqY5KFvpy0q_ZgNfR1WAbNyOJYlEMwzJXiLKVjaxWbdttAdmz9B_nchKpzoio1MfmyIQRX4oSb8lwtvxfCuyGCV6xeBkE0zU0Z3mZIcOhg8mwxS2O1VDY22BgPCbcVUQj7sh7zRJBNScnOIONsoBRL22W5SxsFsjuqov1w8pyyA0ch7zjttvhl2nHFczevQhEENirtANj3iDE4ye9NjiaNcefUIVg2NDQ4-UAl0yxpBZoGDMH2iX02JTD7AZvZXtjuMwpbm3zg3g6Hd9t5gg1L1GxRSu0S01-zGH9_OrYwiE2nVlcBlSsjnaWGOU5sN3Iyne7U2uO8tU6lCrRBPvjHWlOnGFBJng9vj45D7DIJWQtUiIyqrbp3RV-T5W3ncfBeHlNqfGTBHURoMicQQGjZGsBihlN_cVIGJVo6SFfY2VRNGJMtmBEla4WcHZfPiF8ZLjPt0EpjJH-QaWyTmghaO3CEVIY2ddV1xcBM9zNBCq3F_NRi2aBpTasTiXnOGVXjjxkiCmEwPIiA576A6x36wArGSLBTeBDNMFDpmcJOw6o9AUS484B_Jhi5UWA0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">از آنفیلد تا پاپارا پارک⁣؛ ایزاک، هوادار سرسخت لیورپول و محمد صلاح، به دعوت ترابزون‌اسپور مهمان این باشگاه شد تا بار دیگر با اسطوره‌اش دیدار کند.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/Futball180TV/104362" target="_blank">📅 13:35 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104361">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kwq4ZgrDIfny8uTuDN1uTQZS3pQNexDc4RJMIJ0R-OyXn0r819qXf30T1svQlZwHb0zYn7JppDgCSjCJkPlVCj9W8awM54cPYsoItGtuRn26qFI7jp1Xh1LeYP60awRs9aZcbYYR_1YJHx9DJ7ZadZ4rxeT8Ck6qbypVgX_5TJuWR86zHprNclz9pqvkciSv-1NwGzw7Qnc6yDZUMucgbRNnmpaVtbPa1GB-YJBfNGTPb43C8bQqyc51fWfnREbCOJv2Fc7zL9yeHLr8UECFYnoyWlqrDoXQczl2UF9Y0hVpv_oLANXLyjbtPFpwdH9vLu8RG8faU_-67OGKy-aU4w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
شماره پیراهن این‌فصل بازیکنان منچستریونایتد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/Futball180TV/104361" target="_blank">📅 13:15 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104360">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/57b5cc35a2.mp4?token=N4Y-imwv2L35jKXuq_abKzJ740f-cq6SQh-AQb9y-IdE78a6HnXSsD7-lHKnQKQ-JW1dIWB_IwUJjtor_nf9uxjIrfetaHWPROZTVVoz88M8UgN3_pqpprL61ftbeCiGpXeuetGiQFzuYtJV5BnoH0gWMjdDPZwLvtKjN_VgS3bDPqFbs5gstuH7EC793hruBcvPYjz7sbDcIhQJm1MRD9apPfwAtFQsNMl0rG26WFuczaNZRcf8IknnXR0eZ-W60bjNpDaHncoGpsEPD2dQ1a7eIKReMolJLZyUqnEmMAos0-KGWF_1JPxJJkPeUPcINHqGtOPA136i2CUb0TsuVQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/57b5cc35a2.mp4?token=N4Y-imwv2L35jKXuq_abKzJ740f-cq6SQh-AQb9y-IdE78a6HnXSsD7-lHKnQKQ-JW1dIWB_IwUJjtor_nf9uxjIrfetaHWPROZTVVoz88M8UgN3_pqpprL61ftbeCiGpXeuetGiQFzuYtJV5BnoH0gWMjdDPZwLvtKjN_VgS3bDPqFbs5gstuH7EC793hruBcvPYjz7sbDcIhQJm1MRD9apPfwAtFQsNMl0rG26WFuczaNZRcf8IknnXR0eZ-W60bjNpDaHncoGpsEPD2dQ1a7eIKReMolJLZyUqnEmMAos0-KGWF_1JPxJJkPeUPcINHqGtOPA136i2CUb0TsuVQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
ویدیو وایرال شده از کنسرت خیابونی در تهران
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/Futball180TV/104360" target="_blank">📅 13:11 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104359">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vjWx21_cbCRvffczX05sdwfEvj0dnLrDKzb1i_tC-cwKurXAUPudJaAFuii-5xjSHGHliFl_5IgFXv94tp1P24-bayoWHXQiB_AcA4MzkHe2QJkeKDOCDz6ZrVraxiM8USCqf-W6yIGxy-ZU-n2ZBmB1KNjZgp3i__7AwpN0ff-mcbzEnIHfj-XTJ8RqDPO2jr6XyYrwbavc8lze57K0FhSEyI3qb0CBcRah65Fu-Ka7la-PZX4cWC_peuXlOM2cKY38VTfurGshff1gLBzbVVCvGyMU5YG0dG18P-7dHUUyK-cRAhtBdl79B1wXEzwjWms7esfvQ5WgyWI_fnlpxw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🇮🇷
اعلام لیست نهایی بازیکنان تیم ملی امید برای بازی‌های آسیایی ناگویا؛ امیرحسین حسین‌زاده تنها بازیکن بزرگسال این لیست است.
🇮🇷
بازیکنان استقلال: محمد خلیفه، رزاقی‌نیا، اسماعیل قلی‌زاده، سعید سحرخیزان
🇮🇷
بازیکنان پرسپولیس: دانیال‌ایری، فرزین معامله‌گری، پوریا لطیفی‌فر، پوریا شهرابادی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/Futball180TV/104359" target="_blank">📅 12:55 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104358">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2fc7ebac37.mp4?token=G3JHJNL3xBxLwr8FUzTiJZAKLvGoOPm-3OV-2w121GQUgKVRmm3D7xfv6NmpWnPzsahJ97QQmjZCjDiHRWhr8WmNySpzcOH7kIMTyRktRPn24_QcFHHgRLJoBpHjLh1AF_0OAebyw0tr_QTFjFne0gn0l96gLmdulp4hQnSinSokxM9ZCXk1WsqGAh0cIkdKvo8c1CRJ8UbagY18iPz2sCxorUA-eV6OUFbL23MPaz7rSaiK__ZjrdzMQmubeNLQkhwyfWvVbCs084elPkEHOOZTKfI-6tLKbOEjzG6M9-dRyRjrUAl3r2-Y0FH_1nQ0RYL4_-mmeSNlQaDlWIDwUVpPRfr8DiZxt47oTBAALlQkcf6eKbrFbrEu8eUWMNJUHQDVfAGz5qZVW3MkIIHn9S3Kp6hhouu267_DGgdBgDT9eAdvMhOshu9BCUoIjdAmLSXRCssPEZc57YB9v-w2zsKvpR8kH1tFJT79W-nC4SjfUTYhq4CukQ0miPH34dvOqb8SqApb6iVgH8nxvvSBT9f8jOd-vX7Tab5ZHxOUU1Naz_3JYfyefwGxUhb1_oEagrnxUFX-upiSAy9S2aeFHC1vG15mzuPAze0EJYggRlQbj9TugkmtLnOeQy3EWOAGrsIwfFQXypca66WvT8eEczWFkXKL6qoEQGs-XkkewcQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2fc7ebac37.mp4?token=G3JHJNL3xBxLwr8FUzTiJZAKLvGoOPm-3OV-2w121GQUgKVRmm3D7xfv6NmpWnPzsahJ97QQmjZCjDiHRWhr8WmNySpzcOH7kIMTyRktRPn24_QcFHHgRLJoBpHjLh1AF_0OAebyw0tr_QTFjFne0gn0l96gLmdulp4hQnSinSokxM9ZCXk1WsqGAh0cIkdKvo8c1CRJ8UbagY18iPz2sCxorUA-eV6OUFbL23MPaz7rSaiK__ZjrdzMQmubeNLQkhwyfWvVbCs084elPkEHOOZTKfI-6tLKbOEjzG6M9-dRyRjrUAl3r2-Y0FH_1nQ0RYL4_-mmeSNlQaDlWIDwUVpPRfr8DiZxt47oTBAALlQkcf6eKbrFbrEu8eUWMNJUHQDVfAGz5qZVW3MkIIHn9S3Kp6hhouu267_DGgdBgDT9eAdvMhOshu9BCUoIjdAmLSXRCssPEZc57YB9v-w2zsKvpR8kH1tFJT79W-nC4SjfUTYhq4CukQ0miPH34dvOqb8SqApb6iVgH8nxvvSBT9f8jOd-vX7Tab5ZHxOUU1Naz_3JYfyefwGxUhb1_oEagrnxUFX-upiSAy9S2aeFHC1vG15mzuPAze0EJYggRlQbj9TugkmtLnOeQy3EWOAGrsIwfFQXypca66WvT8eEczWFkXKL6qoEQGs-XkkewcQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
🚨
🇮🇷
‼️
#فوووووری
از بختیاری‌زاده: ناراحتی کوشکی؟‌ حرکت او حرفه‌ای نبود و فردا مقابل سپاهان نیمکت‌نشین است.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/Futball180TV/104358" target="_blank">📅 12:51 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104357">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5711b4d86b.mp4?token=UKPFfNRVhDopdQDlHBDdcK-juMoZEDUB690afTjKVDet89V-RIMhTZkvYQcuU2h-pNu8wtPSAjTPuRJ2zbupeZweZmPsQXzBR1b7AGfjRs0OC5HG_HQ_zFSlCKrtgLtvw_pRuMFRpm1NuDBpM6x_GbbsXUDwYkaJOAcHXAjlPz11QwhI8VojbDuowiRLd1XnSMyB9Jt5kZMoT6Eay1LFyYmGXCw98oBtzxXGTHSj40gjguhALkIlQnI1aBbzc4qZbZ7l_1PG4nVAFuj4QO7kA9dZRnlRo5YvaTRGcmy5Y4mRXK6RYU8v3YHLR73GtdxIYtX_ssM29BTQpmXZ7eSOQQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5711b4d86b.mp4?token=UKPFfNRVhDopdQDlHBDdcK-juMoZEDUB690afTjKVDet89V-RIMhTZkvYQcuU2h-pNu8wtPSAjTPuRJ2zbupeZweZmPsQXzBR1b7AGfjRs0OC5HG_HQ_zFSlCKrtgLtvw_pRuMFRpm1NuDBpM6x_GbbsXUDwYkaJOAcHXAjlPz11QwhI8VojbDuowiRLd1XnSMyB9Jt5kZMoT6Eay1LFyYmGXCw98oBtzxXGTHSj40gjguhALkIlQnI1aBbzc4qZbZ7l_1PG4nVAFuj4QO7kA9dZRnlRo5YvaTRGcmy5Y4mRXK6RYU8v3YHLR73GtdxIYtX_ssM29BTQpmXZ7eSOQQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🎙
نظر جمعی از هواداران اتلتیکو مادرید درباره ماندن خولیان آلوارز و واکنش دیگو سیمئونه به توهین برخی هواداران در استادیوم به ستاره آرژانتینی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/Futball180TV/104357" target="_blank">📅 12:45 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104356">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ONUPX3Ydo2Q0g7rDo2Pzp7vsYu4ShNftyiBg1a7-YDHa4noNUv94hGX6ctqMlKrIREAS0D-Kqn8bvvi3sM8d2lwxdNUQBzrbzl2BWS25iW1iMfD-dgANz-UWv9CadTlD2DXe_4DCMKmETzhq3C-sOV6kaYQuh8y3GxaOs63twt4DWdHXio8Q72w-U-Wjxea8mxzBTn7UcdDCmh_H5g5zeUf5nh4Y_854s3NhNyn34pUGHXak4r178pj_4B1oStLhq78dbqnL6YqOEqVljz25IrBPCbowZvq3CTDIBu-y-DPnZNUqBNwcCqUAbXm1baTnKQK_cknYRh_-XrAmSy4SSQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
🚨
مالکوم با عقد قراردادی پس از جدایی از الهلال به تیم‌الجزیره امارات پیوست.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/Futball180TV/104356" target="_blank">📅 12:25 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104355">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EpHnLkSIeEiJWKLDjP5Ccxo6bCGrUIPTKDWWDdH9OL9ED4wGPf_WK1_uHuq_0QjciUho5SYrcbcoS9dnnNpa93OI5DAcdUb-zEz4Dcnn3oySglFHbabYxIgxafoz8vMlXFHHHTz4niYuZvVBA3bVOdgiEcbXm5wejIVdkyuVz0gSGqHITwBFAEWp8loU4-4mG8EhCNo7ufMQMUhDO1L9Xr0quWUHGr-XUStfTbhN5AdQW_MwKiAbXp1_YeayW9N1eaxK4uCGMIm6HZ4KW_CbBwXXMf7iwhOAmRsdfYhCmZVwMl21YyN6ynKhJKj5g0E8Odr2wIZDBFaVE3xabXeKiQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
✅
سایت برنامه عادل فردوسی‌پور پس از گذشت چندین هفته رفع‌فیلتر شد و در دسترس قرار گرفت
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/Futball180TV/104355" target="_blank">📅 12:06 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104354">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ab7bebaf5f.mp4?token=l3rJAGwO6b8BVUdilEjZUjL-L8kJDptNPKwfEZXrf9Ld3LAij4fRxCl-Qkn7rYLNBEVOTHoHgSrF_lhpPHpwzyE2_z7iu7NRgpPPSfQ9s9L36qDmu-a-EHlSPvGS_nlzY5aDjGtCuMC7_Kaql0-DMJVD0-IODByoG0joZd3fzogQL1rSdaXo3hNj81qdCDXMEsIfbM1VuCd8_ehVsOcXENlzHcyRU_keQDsIR6aX0ys3X17-15v0Hz5c0qQgicqhwV9H5iy4p6ZUDN72X9qEPL_dpMOpSdoyZdYTEq7baGVQro_tZFIJAshqjB2nix3uKPosnsxR8LiRu2-ytogZ6A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ab7bebaf5f.mp4?token=l3rJAGwO6b8BVUdilEjZUjL-L8kJDptNPKwfEZXrf9Ld3LAij4fRxCl-Qkn7rYLNBEVOTHoHgSrF_lhpPHpwzyE2_z7iu7NRgpPPSfQ9s9L36qDmu-a-EHlSPvGS_nlzY5aDjGtCuMC7_Kaql0-DMJVD0-IODByoG0joZd3fzogQL1rSdaXo3hNj81qdCDXMEsIfbM1VuCd8_ehVsOcXENlzHcyRU_keQDsIR6aX0ys3X17-15v0Hz5c0qQgicqhwV9H5iy4p6ZUDN72X9qEPL_dpMOpSdoyZdYTEq7baGVQro_tZFIJAshqjB2nix3uKPosnsxR8LiRu2-ytogZ6A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نگاه طنز به معروف ترین دعواهای تاریخ فوتبال.
🙂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/Futball180TV/104354" target="_blank">📅 11:55 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104353">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">🚨
🚨
🚨
🚨
🇮🇷
حجت‌کریمی مدیرعامل تراکتور: متاسفانه قانون ورزشکار قهرمان برای معافیت سربازی شامل علیرضا بیرانوند نشده است و به احتمال بسیار زیاد باید این بازیکن راهی سربازی شود
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/Futball180TV/104353" target="_blank">📅 11:35 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104352">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/c4qlsL5NmKDJ0FhB0YS6aseB6iuoQF5LTyz0eQnOjzBbj7bCWLgmpM-yf0sySW57XgdMjGbTC5XrflJwMkeOb63OOUa-fA7rSg1UCb2noWYqJX_xZX4pIaqiFIDTJS8KrM1Yv9x9JNOBm9y8Pxnajmc4YPDOUFyoRulvXyKtzJKe4JG-naKMfdDxD5EIkUBldgPLexGN-Pi1K8HTxDa30Lea8l9_X5fkVQE53BNpgin_iby9hJdmmxcvcN4ByHTvoJ1aXBG6VNaIS31Vh9tXKcUWCe74-kQSqSNQ7u6PIIYWWonuXJIeAnLbQix3SXwRa1NCRonqUlD_HOI1LBM0fQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🚨
🇮🇷
حجت‌کریمی مدیرعامل تراکتور: متاسفانه قانون ورزشکار قهرمان برای معافیت سربازی شامل علیرضا بیرانوند نشده است و به احتمال بسیار زیاد باید این بازیکن راهی سربازی شود
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/Futball180TV/104352" target="_blank">📅 11:26 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104351">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UJNK-hCM2IHziSi-nrXk6TS3piHZTdI0-MxyhLL_v_Ut__iDr6wTr7kbnKkHvBwLCceX5okRGkdrJhIVRJwK-71QlHC4mcto73BgYhuVk5ltDEmh9xwR4t7oGmZIz7Md647ctiA11C7IGTgu93hanmZn4lQpLCvCu8gv3stykoMRz-x81ZpE01jii2IHXqCgIA19029JF4ygP3zmVGfbIJa4rQIHRoGgbp8mQKj-umechDJ8MXXjuVJVzjFOFAXRhupzjlgFVM_k7hUHo9FV-bdXXp48g0CelhSrDT0UotUmY3U8QPBn-ARHHH7nQ6VA0d59c4LidmrjhhMOBveOlQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇮🇷
✅
اعلام اسامی داوران هفته‌سوم لیگ‌برتر
🇮🇷
🇮🇷
استقلال - سپاهان / پیام حیدری
🇮🇷
🇮🇷
پرسپولیس - تراکتور/ امیر عرب‌براقی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/Futball180TV/104351" target="_blank">📅 11:23 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104350">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ehP6u837aUXxUvujHS0le1n9HS0Uz_Z3Iwj0S0QZJKtuCl4NR0E8T3Th7sriFVpOBZ-Kmx0P6xR-8kK3LJivCkD-Rhigtw1r36nNG8qiWTcLdmZR4-XthajDivABWlJNMXPDfv8CUjRpObaLbMTcIu-TqsWEd0_rZBRqvUXNdLDxr4hAzBwSWE5HfL6HQOd2SipQy90fSpREXtdS3WisnQ14ec8jBeIHeivOKgn9oxG6jrpsjGSlF7jrH-JemGUaz7JqVldovC07Ne1RBDgwlvPHopkrd-fdDr38rRrg0X6w_Rq6SXwy8O_bAOHA1_4ZAfBsFldaoJNFFrAJH9i9LA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
🇮🇷
پوستر باشگاه استقلال برای دیدار با سپاهان
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/Futball180TV/104350" target="_blank">📅 11:17 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104349">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">melbet.apk</div>
  <div class="tg-doc-extra">46.2 MB</div>
</div>
<a href="https://t.me/Futball180TV/104349" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🇩🇪
آپ اندروید سایت جهانی Melbet
💥
🎁
بونوس ورزشی هر چهارشنبه
🔥
💸
واریز و برداشت متنوع
💵
⭕️
بدون نیاز به فیلتر شکن
⭕️
🎁
کد هدیه ثبت نام Melbet90
✌️
✔
https://t.me/+x60dZGAgXTUxM2U0</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/Futball180TV/104349" target="_blank">📅 11:17 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104348">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cEoopY6RrQlGXzHIQYxhBSNnjKFfajsUMHRgVWdrB9aaTqI5eeOIRYJPpyBC1-r57bulqnAVKWXKBWd3hk_4NdQaFwO7dwDCJ4pFu5GHyHCdo7mcABmKnhkZIAYUUbnye1QBU-hi6Qpc67nHIU3Z23UBolc2YkwkcPtxOwDhMkA7_N1ZsbfffZULwZy0Fl5oW2EjNt_Q2yvqNj7yqsnNrHntUobBXiwsV6y_45IwcOWa4BYhwsHxKiNrkU55GGHT220tn5mT-1eoNgC1Hj_kST_rP9BWiNOZiaYFzPU6hA5Bn8FPFzU-3L8b3Hz1cp3VddZel05LgJXTRm-DgI0_Qg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👀
دنبال سایت معتبر برای شرطبندی می‌گردید
⁉️
🎲
سایت بین المللی و معتبر Melbet
👍
😁
😊
🙂
🥇
واریز و برداشت ارزی و ریالی
‼️
🔥
بونوس 100% اولین واریز
‼️
⚽️
بونوس ورزشی هرچهارشنبه
‼️
🆗
کازینو و انفجار با ضرایب جهانی
‼️
🎁
کد هدیه ثبت نام :Melbet90
🇩🇪
دانلود اپلیکیشن MELBET
👉
🔗
لینک وبسایت
👉
⭕️
جهت استفاده از vpn از IP های آسیایی یا کانادا استفاده کنید.
🇨🇦
🇹🇷
a31
✔
https://t.me/+x60dZGAgXTUxM2U0</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/Futball180TV/104348" target="_blank">📅 11:17 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104347">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6eb94b21a1.mp4?token=vKj8T_cTkxNoB3YZXPejKWTWAVHO5dQuK3cMDLPDM6UhgZ_4DjhnMx-uYTa4DvstNSTdyL2G_Tk35VcrcxsyAx8qMOW_pqXx6IpevoQALVedmZu7Dd4Aokxr2oXzPH1hnjjyThshU45YDtB0x_JmM09vhWu50zsWrdHZ9HV1dE8Y2v_fz4yOmN1VY-M8e4UtGrapStLyfShscU9NJBCFmqVClMvuExj921Dh36So2336dXP-azs4d5QIj9czYvbG5opR8hEGztE-eqQSVSrWvsc7tKmSqUeH2jLQHM7tzlESdfDTz9ErtIR1q7YDbwCSxnmcYvJ8TxvL_OFdH23SRg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6eb94b21a1.mp4?token=vKj8T_cTkxNoB3YZXPejKWTWAVHO5dQuK3cMDLPDM6UhgZ_4DjhnMx-uYTa4DvstNSTdyL2G_Tk35VcrcxsyAx8qMOW_pqXx6IpevoQALVedmZu7Dd4Aokxr2oXzPH1hnjjyThshU45YDtB0x_JmM09vhWu50zsWrdHZ9HV1dE8Y2v_fz4yOmN1VY-M8e4UtGrapStLyfShscU9NJBCFmqVClMvuExj921Dh36So2336dXP-azs4d5QIj9czYvbG5opR8hEGztE-eqQSVSrWvsc7tKmSqUeH2jLQHM7tzlESdfDTz9ErtIR1q7YDbwCSxnmcYvJ8TxvL_OFdH23SRg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
🎙
روایت امیرحسین اصلانیان از خوردن حکم سرمربیگری احمدرضاعابدزاده توسط آقای مدیرعامل و واکنش علی پروین به این انتصاب پرحاشیه.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/Futball180TV/104347" target="_blank">📅 11:05 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104346">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/80db36926b.mp4?token=DXF_dD62GLX0naIil6dE4Ei6jV294UVl3MEuMd4Lml9ol2DZyEHdqMo0qj7suN7_Cf_am3EyP40-8uCUauap1BIpZn6Z1FikIUAqi8mRmqVoz_f6D3jHUNCS27FVCTM7HYDXzihsziX2b0iFH4pM8WySnX2DM7GZ89p-k9pAkT7zXxlEwLMJQ_rRlmLh7Wd7hEeF9P3fuHL_1UHjvpKBPE9ctBjnwaPFds_hPyo5VcAPlZ0K1ET55ap02xdNRuPFt0unmx5DBZqZKUAVOiazk1qXNJQg6CkubeQZqst_xVfpRy5Jlv00acrVy80r4u1rixAHYI0MqJ_5OhI5zNpvhg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/80db36926b.mp4?token=DXF_dD62GLX0naIil6dE4Ei6jV294UVl3MEuMd4Lml9ol2DZyEHdqMo0qj7suN7_Cf_am3EyP40-8uCUauap1BIpZn6Z1FikIUAqi8mRmqVoz_f6D3jHUNCS27FVCTM7HYDXzihsziX2b0iFH4pM8WySnX2DM7GZ89p-k9pAkT7zXxlEwLMJQ_rRlmLh7Wd7hEeF9P3fuHL_1UHjvpKBPE9ctBjnwaPFds_hPyo5VcAPlZ0K1ET55ap02xdNRuPFt0unmx5DBZqZKUAVOiazk1qXNJQg6CkubeQZqst_xVfpRy5Jlv00acrVy80r4u1rixAHYI0MqJ_5OhI5zNpvhg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
تنگه فلوریدا را هم ببندیم؛ ایده کمتر شنیده شده از استاد خوش‌چشم، کارشناس ثابت صداوسیما که متاسفانه از سوی مسئولان لشکری و کشوری اهمیت داده نشد
😂
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/Futball180TV/104346" target="_blank">📅 10:40 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104345">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0566a44cfc.mp4?token=VYzVDEovaC58oRVwLTwt09bl_pxS_m9SS_s8a_YfaRvRIKOhy08OpJAFBW9MkIiNKkaiqp4vGszwwUt0mqbroDIlEm7yilpNypoJF5oZGjlT2KZ3cqEEI-k6f9h3dUtr_cifwmsg5VB71H-O2EDiDKRsWwJKTsMulr9LBzCZXPjaRBJCKl_cQTdRpHKcy1gnz-z6g0TSnZvW-EByxDN_h9qp68-TLxr_r_nmXYNcyjOQ8pJ-HgcyT5_bgJbgwvMcPXjIGEys_W1mAPhwnQh0Scz9URIQcYsgN68VsEFrk1BPGfmVXpKSoBfS_Ob-bhCoRpK012rju3AHOnHNY-27eg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0566a44cfc.mp4?token=VYzVDEovaC58oRVwLTwt09bl_pxS_m9SS_s8a_YfaRvRIKOhy08OpJAFBW9MkIiNKkaiqp4vGszwwUt0mqbroDIlEm7yilpNypoJF5oZGjlT2KZ3cqEEI-k6f9h3dUtr_cifwmsg5VB71H-O2EDiDKRsWwJKTsMulr9LBzCZXPjaRBJCKl_cQTdRpHKcy1gnz-z6g0TSnZvW-EByxDN_h9qp68-TLxr_r_nmXYNcyjOQ8pJ-HgcyT5_bgJbgwvMcPXjIGEys_W1mAPhwnQh0Scz9URIQcYsgN68VsEFrk1BPGfmVXpKSoBfS_Ob-bhCoRpK012rju3AHOnHNY-27eg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👀
💥
جانشین سرخیو بوسکتس در بارسلونا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/Futball180TV/104345" target="_blank">📅 10:15 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104344">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d65173b5bd.mp4?token=Ubsy2tI7eiBE_AAjx6MK_7q6uP9LFTFL0HqIBAd259UGUstKnOazJDG0SiceDvTBk-ptHSZk11eUKUnKdAwwvBKSeIUTP85o32V6GWGQwoqzdl1G4Z69ca9sy3ya8tGVT34XbPN2RGEiQg-vzUcQ4pjBC-yTRbEatT6v71slPH1qVczr58m44gqOb8MrCOey9gF2ERSHN_9plucCPhFrAtUE49LlWXpwfzs66MbD7fzn1WHwGR1w7sCSOXEaNzDMRT2a2UThr0LI0wM3LTc_n05It9z6W2k5vPyu6fxu29vuUBC__Z-Y0pBeif4BPfRpQQWHe_2e-7fJBe79fDjOIA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d65173b5bd.mp4?token=Ubsy2tI7eiBE_AAjx6MK_7q6uP9LFTFL0HqIBAd259UGUstKnOazJDG0SiceDvTBk-ptHSZk11eUKUnKdAwwvBKSeIUTP85o32V6GWGQwoqzdl1G4Z69ca9sy3ya8tGVT34XbPN2RGEiQg-vzUcQ4pjBC-yTRbEatT6v71slPH1qVczr58m44gqOb8MrCOey9gF2ERSHN_9plucCPhFrAtUE49LlWXpwfzs66MbD7fzn1WHwGR1w7sCSOXEaNzDMRT2a2UThr0LI0wM3LTc_n05It9z6W2k5vPyu6fxu29vuUBC__Z-Y0pBeif4BPfRpQQWHe_2e-7fJBe79fDjOIA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
✔️
پیام‌کودکان جنوبی خطاب به‌خانم‌مجری که میگفت جنوب ایران فدای لبنان و فلسطین: اشتباه نکن خانم مجری ما جنوبی ها فدای هیچ کشوری نیستیم ما فقط فدای کشورمون ایران هستیم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/Futball180TV/104344" target="_blank">📅 09:50 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104343">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9bde2485a2.mp4?token=ZGF9KSUTngD7IMqjsvNxjhc0hoQdPUN7ZEJhJPWHzB0WP3x0_29fxbzgcJeDJOlkrFfyvsFMML1UfCzCQyIFeG7_5y-CdULd7wjX4_EG1vKa_6JiUF8S3ZZlfImvT9kepVjZgCxsoBusBXqobajUKWVAUnBH7wehUHn3ZDpdXG0f4VJJhuAgnBLJHrLPX0Uc8iPNUih8hiVL37aC3iDO7BSxIfRn8T9iuQ6CmRv50Nj6pG6BnD-EYDJSHtD2lagTYNc2_wgoYHmlXwPZbOFBJ6GXK1az3YkTncrS-1uTQDz5Vdz7RouG4vmc_fz-sL2jRQeRrKZ9IsvLvT0TrVhQnw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9bde2485a2.mp4?token=ZGF9KSUTngD7IMqjsvNxjhc0hoQdPUN7ZEJhJPWHzB0WP3x0_29fxbzgcJeDJOlkrFfyvsFMML1UfCzCQyIFeG7_5y-CdULd7wjX4_EG1vKa_6JiUF8S3ZZlfImvT9kepVjZgCxsoBusBXqobajUKWVAUnBH7wehUHn3ZDpdXG0f4VJJhuAgnBLJHrLPX0Uc8iPNUih8hiVL37aC3iDO7BSxIfRn8T9iuQ6CmRv50Nj6pG6BnD-EYDJSHtD2lagTYNc2_wgoYHmlXwPZbOFBJ6GXK1az3YkTncrS-1uTQDz5Vdz7RouG4vmc_fz-sL2jRQeRrKZ9IsvLvT0TrVhQnw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❗️
نحوه آموزش فوتبال در کشور متخاصم آمریکا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/Futball180TV/104343" target="_blank">📅 09:25 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104342">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/B-LMtmuJ4DHLDW9owU5N2iBJQsnMX3ve9bASR_uIHygv8wmeQv36r_K9qYHFwxuOqmeu8kSh9nwQ77OMNT8y72stMe3blCCMxgM5L_v-Cw-pfAP4OtXJVOc4wVeumGP9qkNXHTMQunQYu0jGEF4jgv3CzYlO_u4dz6BPcgAcGrmwLnHrGnMPV1Acr5N9MDLXO9d4yAbflIXdD9vKG9gvx3cfuOMAfe_7K3-V8CYntq_mDurCxn2zQoy2bRFz3MRmuhJW8gC05CQ_dHQzWQ8iYZ-WKVyArjdqhdEazEQA_YTavEVE9M-VAB7Z8pgYcUii4kxF0l7crVVk-ednCc1eBQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
🇪🇺
شانس‌تیم‌ها برای قهرمانی اروپا‌بعد از پیوستن رودری به باشگاه بارسلونا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/Futball180TV/104342" target="_blank">📅 09:03 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104341">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hgKYfz1Z1vxDtIY-sFemr31CTgDuQq8URKkzLKIX0eFlFczsoxXuUAX1u2YqPzIICvIEM8iEtaSCaej_8Krx9DrGRgpxObHJOXSAmpd5-jM6NReKAfLBsC_uVkRlg7H7oNeUuL-XnAhW8wy1KiAjaxPiOMmDt_QZW5GtFwPQ5ABpSWH1MHDO2J4fuv00RvLzTGwA3u4qYDiLbJBEaXcgi6zaFwfUeTqo3_FBUnoKXA4GuzcJJ_QGA9BC7M-IbemWwLG8x0YhXaGYVNWFeljo_xIZZLvYn9wg_l1YasgZpo-JIXO7-Cfsd6pO2bcjcgxMxYh5UMc5qSCPN7WDRKbLDw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🚨
🚨
🇪🇸
🇪🇸
استوری هیدالگو، مدیر برنامه آلوارز  «هرگز از یک دروغگو نپرسید که چرا دروغ گفته است چون برای این‌که دلیلش را توضیح دهد، مجبور است دوباره دروغ بگوید.»
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/Futball180TV/104341" target="_blank">📅 02:53 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104340">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">🚨
🚨
🚨
🚨
🚨
🇪🇸
🇪🇸
استوری هیدالگو، مدیر برنامه آلوارز  «هرگز از یک دروغگو نپرسید که چرا دروغ گفته است چون برای این‌که دلیلش را توضیح دهد، مجبور است دوباره دروغ بگوید.»
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/Futball180TV/104340" target="_blank">📅 01:32 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104339">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Cxuwvlzvf3PVZ0v3-SwvYobVuxg4H2-wOLTIqGQHDSdv4ejAyoAq70UQJxiley-fcR5ZYWho99RBSBKapo618dyOhCF0TBLePWZJd6GmONwUZUpEszA2GWQyGx1qi160MyF6AvC5TsDGf90N0jFpUd4AzqRIsZoEs_m3BlAfCaErS7aH7YsteHDAQUgrSw3AIua6iT9OyW4Qsg-ocZsrDdtye4B1FOhVAsy7oJakX83knYsHjbfUywIdGHyhpSZjBxo4k7IIeabQXhz9D6HBiGc4LkNZ7NKbXcICV1YfpuBB0QUBWSj_22otviKtrQ03CTbFY3cva53jvlptzruYhA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🚨
🚨
🇪🇸
🇪🇸
استوری هیدالگو، مدیر برنامه آلوارز
«هرگز از یک دروغگو نپرسید که چرا دروغ گفته است چون برای این‌که دلیلش را توضیح دهد، مجبور است دوباره دروغ بگوید.»
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/Futball180TV/104339" target="_blank">📅 01:20 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104338">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XTn8lYTcsCPK01wKsVx-MEzyt3Xk5751FG-VuKPbUCoehpD5y7BsmSBQgRxvT10FuS060EeT9aNqexgWMbgoxvuh3PbeWnPCdbqx_1B-uUXTvdXolFXSs2sp0jacfA3_J19kDhqljNYVBZjedBYeqGyI6e1t6zLA0ov6CS0KEhdvPjHSACRgUsdvZ7uOFHjrzbR5HR8uSmsz0xTSdR4LBEj2DC2aKF34zux5pk9dRbZL6IQBcDXqGeT2TUISCHwjyHdpwnlVz_XoyC2E_Kl637MHvEF_yCsbVRq9ucxb2IK1nYu5uXQRk731C9UlDFZqKvba9DW_k3EDKcBdUpR52Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
📊
پس از پیروزی آرسنال مقابل کاونتری سیتی، میکل آرتتا به پیروزی شماره [150] خود به عنوان مربی توپچی‌ها در [249] مسابقه در لیگ برتر دست یافت.
🔥
⚽️
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/Futball180TV/104338" target="_blank">📅 00:43 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104335">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/e4cd1601ff.mp4?token=fP8KZDMeukPCfs8GGmHvcZUIb3cl1HOsIFkai--F-86jGWXp_FQinruwvq0jJVXhXf1U37m2C1kPuvrJ_XqdzHo8s_B3g4ibazPW0yFRepsD1WrfFVNq0O627tolkFyfyF3SVHkLMhyiFmXg52d6fKDPKZXjZPRUWzDveOca16tF0VrGU7dHQJkNxoo1fSfqqsOf4y3SchugKs5oV9h5KUZVkL-mAa48d1nKHw6rAfJZUR2SFRvoWu0P5Lw6CLP8jaW7Ox_p7KxgPsltEmR2t7mXN3isehIX4e9wdklynzQ60PJ09IPGbHhmROcEqjvqk6bj0hZkJ9VpyswHvX7T6qrRA14Rqr_19Jogu8dFW09WmbHlut_8GeirrdPc4zLBZBHhqecpUfVgT9UMcBV0mYXcFXTOy0JR31V5zi-vEif6vImf3wqqXPwyPu4RZZx26H3YjyS5MpMHkJQmPiDRzdJbsE92vNW0koFKP5ex73GcKCfE2e4yXrtFoIbtViUbu3LktkzwopVKy4kOIwsl4l6EPO39LpcE8qOAftc8uLJpbPpkHkspFlfMFIepZCco39rXbF1cRopGQCm1wcg8WXGp8JvIglwQjSxUxY7dhQ2Tmng-mZlkDvnvZ36_C9cIwP8sbENkyzLefY-VoSsAw0UFmZeNSXtDbbwJggGmQOI" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/e4cd1601ff.mp4?token=fP8KZDMeukPCfs8GGmHvcZUIb3cl1HOsIFkai--F-86jGWXp_FQinruwvq0jJVXhXf1U37m2C1kPuvrJ_XqdzHo8s_B3g4ibazPW0yFRepsD1WrfFVNq0O627tolkFyfyF3SVHkLMhyiFmXg52d6fKDPKZXjZPRUWzDveOca16tF0VrGU7dHQJkNxoo1fSfqqsOf4y3SchugKs5oV9h5KUZVkL-mAa48d1nKHw6rAfJZUR2SFRvoWu0P5Lw6CLP8jaW7Ox_p7KxgPsltEmR2t7mXN3isehIX4e9wdklynzQ60PJ09IPGbHhmROcEqjvqk6bj0hZkJ9VpyswHvX7T6qrRA14Rqr_19Jogu8dFW09WmbHlut_8GeirrdPc4zLBZBHhqecpUfVgT9UMcBV0mYXcFXTOy0JR31V5zi-vEif6vImf3wqqXPwyPu4RZZx26H3YjyS5MpMHkJQmPiDRzdJbsE92vNW0koFKP5ex73GcKCfE2e4yXrtFoIbtViUbu3LktkzwopVKy4kOIwsl4l6EPO39LpcE8qOAftc8uLJpbPpkHkspFlfMFIepZCco39rXbF1cRopGQCm1wcg8WXGp8JvIglwQjSxUxY7dhQ2Tmng-mZlkDvnvZ36_C9cIwP8sbENkyzLefY-VoSsAw0UFmZeNSXtDbbwJggGmQOI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
گل‌سوم آرسنال توسط اودگارد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/Futball180TV/104335" target="_blank">📅 23:41 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104334">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/ecf24c9409.mp4?token=A1PaCy21dWDV_wTc81bKQfdFcj4qZr6fPdUI7B_NCEZfXkeKhkbSKzludvqM2IsugG7ItIlAf90dLNRZU3wb37gyiQdLQKhTRrNyyYLO55FO1DbEaabLBdiFSIzOIlCFrWeXfN04fmXVXhPlrBF1XemaE9JyLJSa73TkjGDX2Zsw1DRwjq0nglbzMT6KZTzt7Pu9Y-VWzYWO1YglNbaHzMGfwgfSNTSTWw5rUUo2zbb_6wfJSfZyeGHwQ7VVFlAtMXddFM2nG5c9uJEUyWKnvvkEOTwySUNs7t9OW3jb6ZsMiW64s7h1p6GCUznukEpWdqSdxMKy9IC1MnMUC_CSWE22Ig1QkMqq9fEsZ1OoaoyuY2PfLkVav0y5xnhtW2WExjyjH8kEvzhF8f45sm1OVuXHxnjmdQszAlIIIHPem4dhAco6_jqVxcqz8SRoIN-s1vZ2FyhKoBs8ZCSYG_OnWUx_dDwJjl-tq77_TlhKB2vfs8RfZDTV-3xluJ_zTPD9-C_aig0_cfajBsAkJcekfkw6SjQBnMsWtJxaWK451OFcTLJI5fcMbzxXTI5I5BJi1SRIIWcOaFcpUBW6zidk5Y4NLzn1rEH8VSNCguNkaCDK0OwsKAgDCZ-AStq97KRxVXRrsHhIazENDbpfFFT4lBxww0LSnBcEN_yBmxI-xKg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/ecf24c9409.mp4?token=A1PaCy21dWDV_wTc81bKQfdFcj4qZr6fPdUI7B_NCEZfXkeKhkbSKzludvqM2IsugG7ItIlAf90dLNRZU3wb37gyiQdLQKhTRrNyyYLO55FO1DbEaabLBdiFSIzOIlCFrWeXfN04fmXVXhPlrBF1XemaE9JyLJSa73TkjGDX2Zsw1DRwjq0nglbzMT6KZTzt7Pu9Y-VWzYWO1YglNbaHzMGfwgfSNTSTWw5rUUo2zbb_6wfJSfZyeGHwQ7VVFlAtMXddFM2nG5c9uJEUyWKnvvkEOTwySUNs7t9OW3jb6ZsMiW64s7h1p6GCUznukEpWdqSdxMKy9IC1MnMUC_CSWE22Ig1QkMqq9fEsZ1OoaoyuY2PfLkVav0y5xnhtW2WExjyjH8kEvzhF8f45sm1OVuXHxnjmdQszAlIIIHPem4dhAco6_jqVxcqz8SRoIN-s1vZ2FyhKoBs8ZCSYG_OnWUx_dDwJjl-tq77_TlhKB2vfs8RfZDTV-3xluJ_zTPD9-C_aig0_cfajBsAkJcekfkw6SjQBnMsWtJxaWK451OFcTLJI5fcMbzxXTI5I5BJi1SRIIWcOaFcpUBW6zidk5Y4NLzn1rEH8VSNCguNkaCDK0OwsKAgDCZ-AStq97KRxVXRrsHhIazENDbpfFFT4lBxww0LSnBcEN_yBmxI-xKg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
گل‌دوم آرسنال توسط بوکایو ساکا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/Futball180TV/104334" target="_blank">📅 23:11 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104333">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/889cf6b1f7.mp4?token=jBi3B7bJqjjPEfoFx9xQrog0uUGKV_9szuOnxwdNMExzPgbnC9Dp-6dLLZ_qJARpELvIfejIzpCQRKP12IBftDn1H3OINfHzeyki0DR_hTEloExPWfyrY4zFduBx7Ikpzkt08uXdpH_1bL_JpNDCfwZFVbXbeyL1G_3leFwZK3Oww_t5QqECebwh-xJbIM3FwIdwUFGMYZCTdMbq_wso1mfE1r6LR12ZIXOL61dbw5xksHzZlWpWRcnu2GVR10Dz1_y1cKr4OARRQbmv1RBBwUM8epH6h_x1hyd4qjpYVWzu7SDruBWwPqh4UIaiUezB6itQJP3-FmPPvmdsl8EaZkR9OyPAyynheJFa-rnv2ZGmE3w8cAAMf6IiROLz5YQf0f4DFlWqkzU1KTWqKE7e7mF_AZsI3C7vGRGU85cC1ao0KYJQE9JAJDay_WgZnnzSDJ3lFP7IDRFSMYnflIhRskBB9dWWQdYXN2afbb7mJRUepOSpv-lRfmdIaYqcm9YmW233IhTA57b3zxyg_DXGs4Xk5zpxEUNo1IQBNAkyuTh3IyhVLi4LE6pxi_vh37Puzt3xwZY7WQN6CMViUIx5am-AwXkRg16naH1rwdoT9FdQVirQpttggMZVE8A5b-s1ZUTwkgxxkT0jKPY7nzLEXYhkTzm2TkxzVzPeAiT5Y5g" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/889cf6b1f7.mp4?token=jBi3B7bJqjjPEfoFx9xQrog0uUGKV_9szuOnxwdNMExzPgbnC9Dp-6dLLZ_qJARpELvIfejIzpCQRKP12IBftDn1H3OINfHzeyki0DR_hTEloExPWfyrY4zFduBx7Ikpzkt08uXdpH_1bL_JpNDCfwZFVbXbeyL1G_3leFwZK3Oww_t5QqECebwh-xJbIM3FwIdwUFGMYZCTdMbq_wso1mfE1r6LR12ZIXOL61dbw5xksHzZlWpWRcnu2GVR10Dz1_y1cKr4OARRQbmv1RBBwUM8epH6h_x1hyd4qjpYVWzu7SDruBWwPqh4UIaiUezB6itQJP3-FmPPvmdsl8EaZkR9OyPAyynheJFa-rnv2ZGmE3w8cAAMf6IiROLz5YQf0f4DFlWqkzU1KTWqKE7e7mF_AZsI3C7vGRGU85cC1ao0KYJQE9JAJDay_WgZnnzSDJ3lFP7IDRFSMYnflIhRskBB9dWWQdYXN2afbb7mJRUepOSpv-lRfmdIaYqcm9YmW233IhTA57b3zxyg_DXGs4Xk5zpxEUNo1IQBNAkyuTh3IyhVLi4LE6pxi_vh37Puzt3xwZY7WQN6CMViUIx5am-AwXkRg16naH1rwdoT9FdQVirQpttggMZVE8A5b-s1ZUTwkgxxkT0jKPY7nzLEXYhkTzm2TkxzVzPeAiT5Y5g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
گل‌اول آرسنال توسط کای‌هاورتز
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/Futball180TV/104333" target="_blank">📅 22:48 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104332">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">🚨
🚨
🚨
فابریزیو رومانو و متئو مورتو:
🇮🇹
برای مالکان و همه افراد حاضر در اینتر، لائوتارو مارتینز فقط کاپیتان نیست؛ او نماد باشگاه است.
❌
هر پیشنهادی که ممکن است برسد، بررسی نخواهد شد. موضع مالکان کاملاً قاطع است.
✔️
با ایجنت او تماس گرفته شده است؛ با این حال، تاکنون هیچ تماسی بین بارسلونا و اینتر وجود نداشته است.
🚫
اینتر قاطعانه ایستاده و پیام‌های بسیار واضح و مستقیمی ارسال می‌کند مبنی بر اینکه لائوتارو غیرقابل فروش است.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/Futball180TV/104332" target="_blank">📅 22:39 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104331">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/m4KGAyHoeuwsoLkifaykMcoUKTgjtHAPClayzYm9jfFNz8k2LnHjol-g7xt84jvO2s2n1Uw-cOVWtwWyUXMsoQLOVj4DeNqw_DgMjisd8VI12IhPKdcuVcNk9d385AxiiNb_gQCn88V_8s8RMhN2KdF-CHQQfnX6lz4ze6CLg_g0ptuh6lOszf0__AelAJJPI-MeDghsRLBNShg7_4XU2UjEhRVCKVl2yQh2XqU62JS4BwalIR0Y0WUNH8xFkt970oVyXTBmCV5Slvf-fzwY26QTguttfI55E3pp6_ihBHlSfjx26wG0G-r2tnoy0usU9u6a3r4uaRJ7Ydr08XtSmg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
❌
🔵
#رسمیییییی
؛ مالکوم از الهلال جدا شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/Futball180TV/104331" target="_blank">📅 22:09 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104330">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZWVkORlNBdd2IqkQarfEQIO0FfaJr8t-OvV8iBCJ3rkZsOkLia7Abl4r2kVZR-qnz3goh5Xd7cJIwJbLKRSokdNslvbimAlUf44n7xzp_XUgC_X6D1drdRU0GkWD59ZB5K9mghnC2bDCUz1pgkkDbrH_XfpYZv6VbmaRZwyd9Sbu1JjxGOVYy5Qgh-XNuKDmiH9ajdNYGTt1KImMKtd6IaJzPd_PpbSdTK6_jLuSOnPX8lxdsqGw9hiKULKXcIHMPNclyASzSu3Gdq0liwINQDaV_0gyYiYishKCOffGkwq4sHyr_eLml-7_JUtrVMMcQUt7Qka3ehBQDh4yzIBirQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🚨
🇪🇸
#فوووووری
از متئو مورتو: بارسلونا از انتقال خولیان آلوارز دست کشیده و این بازیکن رسما از برنامه‌های فلیک خارج شده
.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/Futball180TV/104330" target="_blank">📅 22:05 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104329">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f670f0bd57.mp4?token=WaPWF8XUb7X88-hEG9jjxyFOfYRtlCoglbPFpNs6TnqO6d3DA0KMFd7llHHyE2PEZeu5zHdHNwG6zXd_gZRfDcwpq-qZ4os8xgjZ2fzfVNrhXfEsqhvSDP-kcEcq4g5Pyc3e6CvLW8ML5hZiLkcSWDxzAv1ttgO644b6YgaB2q7UJ3T-uAKom2GM1O4k3rGAcX5f2uihMP3GKHU02rER-VfBPGr0XaJ5SQnbKFOaI5kLiM0L5NlrQltxgvMCIClmJl6zzAm958aWestzRs0HA5EB_NYuq0cf0hNRcT5zDEDIl6luEKSq31f16LufXxMpwUMT3PbM8Ja_Zw-DwMeROw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f670f0bd57.mp4?token=WaPWF8XUb7X88-hEG9jjxyFOfYRtlCoglbPFpNs6TnqO6d3DA0KMFd7llHHyE2PEZeu5zHdHNwG6zXd_gZRfDcwpq-qZ4os8xgjZ2fzfVNrhXfEsqhvSDP-kcEcq4g5Pyc3e6CvLW8ML5hZiLkcSWDxzAv1ttgO644b6YgaB2q7UJ3T-uAKom2GM1O4k3rGAcX5f2uihMP3GKHU02rER-VfBPGr0XaJ5SQnbKFOaI5kLiM0L5NlrQltxgvMCIClmJl6zzAm958aWestzRs0HA5EB_NYuq0cf0hNRcT5zDEDIl6luEKSq31f16LufXxMpwUMT3PbM8Ja_Zw-DwMeROw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">😆
حس و‌ حال مردم وقتی مسئولین درباره افزایش قیمت بنزین صحبت میکنن:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/Futball180TV/104329" target="_blank">📅 22:03 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104328">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IFSvVusiKwC8mM1Gtzgb7iHPrL_cl7CUmvWNHlJTQR3ySjXRaUkWoqtycsaBpfTW-HgriMhl-RnXkAgND5QqVeQyktB_VLNd31HmLUoS2TY0gNQyzwvdQY5sS3HKdz7vrY5A9SMPA-8hNDTf3CuoJddL7xWEsoxHOjtVg9hLMo6kKNWPmqPYYkAFwVrbH9gLhCcMQQZGv9pz0HVlb2lnixpxQxVh7FGrV76aMOFICKePO7vWsrKXQ_uaZOf6qveOd6VbqIkjEJE3MnncWsgW6RA7q5qHLkOH0Ko9aCyzYcW5qiZLW1TqxcHIeCh5Ze_xbN8e2VPu68K7Gbw_KD15Jw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🇮🇹
#رسمیییییی
؛ کورتیس جونز بازیکن لیورپول با عقد قراردادی راهی اینتر شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/Futball180TV/104328" target="_blank">📅 21:55 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104327">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DXtoA93BbKkukEHuCWf10-KEDOxVYB0MZd3TFLI8oqC12PTG_saZucjtrz5U0mLw_5vYG9TxUCDq9qONPlf21TOo7rjCubpzE3aM8H0sN_PULXXvKpHbZRU001gDKZs_6pFd9vGogeNPHuxy2bE2-qMPdnJIQOM0Sago3IsUZpEmM_9HZhj0dbEIUllueB7lKEY3S1hqHGuwdgm8JZpZDN2L18CFRBxfRtYA6NWzUS-FqLw2pfTzwgRlTrj914ALPy8B0zluDRQGD30RIBXXxdnl3CW74RRGbmwMSWN05gryFQ3WkcLeo8VQ17nPQ8nQz3TEnnUcxPnOJUzywsDtqw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
گلزنی رونالدو در شب پیروزی 4-0 النصر مقابل الریاض
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/Futball180TV/104327" target="_blank">📅 21:38 · 30 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>

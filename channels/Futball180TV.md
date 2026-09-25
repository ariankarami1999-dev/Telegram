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
<img src="https://cdn5.telesco.pe/file/UbdZzDUhN6YrwJFWDmoS48VBAiyD__74kPyYOIB9zHvCE1N5WBCYy9QJmW8wHmYgRGpjqaK-iWB1AS_VscG_5bHWjIj32zok8JJXo3RgGKT0A5XkAPsu3YHxyQ2JlWFXljevnhF6gEExAbGf6fvaGAHS3_pGrfoarR7QqKB8GvFL9-e1GaKKMEUbW9ND2G42Vp0vsJzkuNaiTFGVQu6Re-T0MgOEBVr-zkFyx4ExjoU5dRg9NGH1sHJAt94eO6773wnZbonD1qOfQjMqQES6fUt9KtaRsmyoecZSK4Ngo6r-iZveeVb5tL9PTMtxB10lU8OEXSHAfzgCLx-TakQsxg.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 فوتبال 180</h1>
<p>@Futball180TV • 👥 401K عضو</p>
<a href="https://t.me/Futball180TV" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 In the name of God; The only popular sports channel on Telegram: All for Iran...🖤We respect the copyright laws and follow the laws, Mr.@Durov...🙏🌹Contact ads:@TivaAds</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-07-03 15:32:00</div>
<hr>

<div class="tg-post" id="msg-107245">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9d52babf07.mp4?token=h1InUWFNykoNPie36IiYqNgoOnJ1pKpJtEiFK4GXsqXpJV1SsL9efDo6jYY_3Z0sqiLaQQVkYekvLOe-dB3-xUW6fL5yjpk0kHZdYd19s_RH_zqcAbingn1e7AjYiXM5GTrcU24AlCVMnP7N389pkPchke77Vcb77MhcZVHxkXlLACRo6jIo1MssEWsZiWUy87GqJb0zRUYkshjUnJd3RmdyjHvX9rQR2Uvb_KmH66GzGFdiOvqA9yRH9MShhAvfmzYKG6KXF1B8PrLmad-dwRLjTC5Vk7FFRqPtD02bCh3WQ2ZRPpEZQ2qDRG_ujIpKWZqTmk1a_AlMs9eHuEdVzg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9d52babf07.mp4?token=h1InUWFNykoNPie36IiYqNgoOnJ1pKpJtEiFK4GXsqXpJV1SsL9efDo6jYY_3Z0sqiLaQQVkYekvLOe-dB3-xUW6fL5yjpk0kHZdYd19s_RH_zqcAbingn1e7AjYiXM5GTrcU24AlCVMnP7N389pkPchke77Vcb77MhcZVHxkXlLACRo6jIo1MssEWsZiWUy87GqJb0zRUYkshjUnJd3RmdyjHvX9rQR2Uvb_KmH66GzGFdiOvqA9yRH9MShhAvfmzYKG6KXF1B8PrLmad-dwRLjTC5Vk7FFRqPtD02bCh3WQ2ZRPpEZQ2qDRG_ujIpKWZqTmk1a_AlMs9eHuEdVzg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👍
گل‌خوشکل سون‌هیونگ‌مین مقابل اکوادور که تنها با یک‌گل دیگر به بهترین گلزن تاریخ کره تبدیل میشه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 2.13K · <a href="https://t.me/Futball180TV/107245" target="_blank">📅 15:15 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107244">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/22947aa27d.mp4?token=ea02kPz5rRkXNBnBx9MW97Eu4BvJjISJ6NtNQxag3O6rj5jDrJZqxq8R6drxXNfFxUm-OT6-9PEcNouy4I5aQwA7IG8X3PT9i_FAFt1Vi_u1qIqCuF2NoA6hKS7mJcU5gSOcjKVwc7LZaON4Z4bLShkFSS9Iw2T5nWIQFBlFDJ1hjHSYtwGj8WBP8Pe8MGs0Z5EaVi1vcJEzQTNi7mQulo1waducG7w9ZwkFwecj3adKkFTgpuHl3IW2fSG-EwSXDDxwX7VKJ_5rbrpwwBAe6I7swcnFrpdkf1eP06ii8GjUBrHl8y3PRKuDpzEmC9xJ9c8CzweBHkwqCKjNRObnak1avvG5buz7A0ewLyIXWfQreKXGkeJWh4fM1QN0pnM1pbCqCc22eG4-ynqfAoJPbj2cKYz_4pxPFFNFYmXk_RirJnuIsi6xrju8D-y2_GzNrG_ih6Mz3cOGsg-kxMSH_VFF7sY7ry8HJkC-MnFgGdlYNFjWfwAI26ki-9A0teNv7YcKlVFJTxDBXFA3hvIzeLCevi1K-HKU2eFYtbnMDCr5aCtBRAmjwJxcTtiO_iimNnJ1rqly5QkauootknX0EIVYmVDnhMj9CNvc0U8LfNVV32ZYZSpZ-faQuApGrFWP-RgswmuqEJgoZqZPPqzq1aXoMJ3Bz-7_jvhOxc2dZBM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/22947aa27d.mp4?token=ea02kPz5rRkXNBnBx9MW97Eu4BvJjISJ6NtNQxag3O6rj5jDrJZqxq8R6drxXNfFxUm-OT6-9PEcNouy4I5aQwA7IG8X3PT9i_FAFt1Vi_u1qIqCuF2NoA6hKS7mJcU5gSOcjKVwc7LZaON4Z4bLShkFSS9Iw2T5nWIQFBlFDJ1hjHSYtwGj8WBP8Pe8MGs0Z5EaVi1vcJEzQTNi7mQulo1waducG7w9ZwkFwecj3adKkFTgpuHl3IW2fSG-EwSXDDxwX7VKJ_5rbrpwwBAe6I7swcnFrpdkf1eP06ii8GjUBrHl8y3PRKuDpzEmC9xJ9c8CzweBHkwqCKjNRObnak1avvG5buz7A0ewLyIXWfQreKXGkeJWh4fM1QN0pnM1pbCqCc22eG4-ynqfAoJPbj2cKYz_4pxPFFNFYmXk_RirJnuIsi6xrju8D-y2_GzNrG_ih6Mz3cOGsg-kxMSH_VFF7sY7ry8HJkC-MnFgGdlYNFjWfwAI26ki-9A0teNv7YcKlVFJTxDBXFA3hvIzeLCevi1K-HKU2eFYtbnMDCr5aCtBRAmjwJxcTtiO_iimNnJ1rqly5QkauootknX0EIVYmVDnhMj9CNvc0U8LfNVV32ZYZSpZ-faQuApGrFWP-RgswmuqEJgoZqZPPqzq1aXoMJ3Bz-7_jvhOxc2dZBM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
🎙
صحبت‌های جنجالی هادی‌چوپان درباره جاویدنام مسعود ذات پرور: منو شیر شاه، سلطان و شاه خطاب میکرد! عکس منو از باشگاه ها پایین میکشن؛ ولی من بخیل نیستم!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.8K · <a href="https://t.me/Futball180TV/107244" target="_blank">📅 14:50 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107243">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2e55638e04.mp4?token=vFdDOMgXbaZOlkKUB8k8oXb4dG6iD2S16CmWZY-aO3UzxpQYuvtQXuejgaMT8kumnzw7iLg_VOj4Ii3GvuHCyiaYkBxhw2zwJjryaXnTdQmYdoRHG3xyXygsOHrHlDliI4uVFSKG-D-6OWxS8bcdTNQ0VD1tzg52Q_8hMwNTUgDkMFcjVYvZ14NnUZfrqJtDZp3NczZqq-itRo2JldsqycVfeDZxeww340S4T88LEr6k5ChL6obgbgbsJHN_6ktGO8MXrhjKHDDAt4JD3t1eSsAC4iABOIjQ5vcDDj8nIxxWydmOorNwnWvDjooKFWb_r8IRbLhFd3c21YKVjWl947PlzHmdIzfdxZ6gj5QTlL7KLu6hcwvSSQ4OQXIhPcMltu-41MrNbDwzHrCuCDQMC6cCsKGjgX8Hn8ptdhLBWvDDEbtxeE6_nPXTS4WzC4gxS3DBTGre-nAJ4c6XdRbQGXCuSaPQ9EXw5kI54slQmE3c6GLt2r1olqdBDFQugEre7ZAHtNrcDrOlMQQYYHrM8P9gjEFYwvXMXjC5CpbX5UwxlgRgi7VzTb7GzPTCUiF2-yucRahK80bEnNZwEK5l0U35_xgl53TIr3gz7hHJtHU4OfMxkV-Q_4KpRA7QCLXPjGsgrbf24jPty1R4iKMwjGcamB95I-JT-yvCkKTr034" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2e55638e04.mp4?token=vFdDOMgXbaZOlkKUB8k8oXb4dG6iD2S16CmWZY-aO3UzxpQYuvtQXuejgaMT8kumnzw7iLg_VOj4Ii3GvuHCyiaYkBxhw2zwJjryaXnTdQmYdoRHG3xyXygsOHrHlDliI4uVFSKG-D-6OWxS8bcdTNQ0VD1tzg52Q_8hMwNTUgDkMFcjVYvZ14NnUZfrqJtDZp3NczZqq-itRo2JldsqycVfeDZxeww340S4T88LEr6k5ChL6obgbgbsJHN_6ktGO8MXrhjKHDDAt4JD3t1eSsAC4iABOIjQ5vcDDj8nIxxWydmOorNwnWvDjooKFWb_r8IRbLhFd3c21YKVjWl947PlzHmdIzfdxZ6gj5QTlL7KLu6hcwvSSQ4OQXIhPcMltu-41MrNbDwzHrCuCDQMC6cCsKGjgX8Hn8ptdhLBWvDDEbtxeE6_nPXTS4WzC4gxS3DBTGre-nAJ4c6XdRbQGXCuSaPQ9EXw5kI54slQmE3c6GLt2r1olqdBDFQugEre7ZAHtNrcDrOlMQQYYHrM8P9gjEFYwvXMXjC5CpbX5UwxlgRgi7VzTb7GzPTCUiF2-yucRahK80bEnNZwEK5l0U35_xgl53TIr3gz7hHJtHU4OfMxkV-Q_4KpRA7QCLXPjGsgrbf24jPty1R4iKMwjGcamB95I-JT-yvCkKTr034" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
به‌مناسبت بازگشت زیدان به فرانسه یادی‌کنیم از این عملکرد تاریخی اسطوره مقابل برزیل در جام‌جهانی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 6.26K · <a href="https://t.me/Futball180TV/107243" target="_blank">📅 14:25 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107242">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">🎙
👍
احمدزاده سرمربی سابق ملوان از کمک‌های اسطوره احمدرضا عابدزاده می‌گوید
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 7.34K · <a href="https://t.me/Futball180TV/107242" target="_blank">📅 14:02 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107241">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f13d64d651.mp4?token=ZJdtoPHAGUqTV-dj7vMyaEFbC_QExjonk0S3W0g4_t_viXn88CrP47MtqaQV5Ey0mm0kOZsngseuV0Bc8J1A7gInndt9l1QZo4-caxOH14mYQ3Zr-OPnY04ASWDBRVX2Su33rG7FOkoqdnC6hWksa1zD6eZg_TAYOtG67J7A-WRBjo5ujuq7A3dBC2xSF6tCies7nfeVe8OYh5-qAZOVNboR8Wa7SdQqnlMT0G7n4MKvyAoZFO82ji3S7CfGM1kezEeVYXH63ftFU90OIOWRUSGx7h0OW13n4z_oVZVtudNaNBgIAfzkWiebQv5Ltj6Kur8Gl1J6Zt8SuJLD1MIetZCyyCaYc8E4uen1dMRUmRfluM17zUURQknpboeyV7r_uVFKfz5Ywk9KF-VotkaT34LE1nQGihfbPT1tIeBbDs-UDci5qWWHrBbHljYdX-rCw2Ks0-zla70GTgX7BzBN7hD553VgcPv5MtNLiA3XTI3NPLLu09vOvpJhTiqOmDu3oD6xBaaYiOBTLmvc2GO30q4XubsBYSK91u1YlfCtkxgeHokUu3aPuOj7vQr_MZ2OVDG88dgrCE-hMHN4G2h5C3ghtxx5ZrKfa7uHaCDUxKUqUbWMf2wof5x6YQbNQWqYXlZmt3z-JgK07P1_mHqwoEpxIXk4IR91jfcoJB_5ljI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f13d64d651.mp4?token=ZJdtoPHAGUqTV-dj7vMyaEFbC_QExjonk0S3W0g4_t_viXn88CrP47MtqaQV5Ey0mm0kOZsngseuV0Bc8J1A7gInndt9l1QZo4-caxOH14mYQ3Zr-OPnY04ASWDBRVX2Su33rG7FOkoqdnC6hWksa1zD6eZg_TAYOtG67J7A-WRBjo5ujuq7A3dBC2xSF6tCies7nfeVe8OYh5-qAZOVNboR8Wa7SdQqnlMT0G7n4MKvyAoZFO82ji3S7CfGM1kezEeVYXH63ftFU90OIOWRUSGx7h0OW13n4z_oVZVtudNaNBgIAfzkWiebQv5Ltj6Kur8Gl1J6Zt8SuJLD1MIetZCyyCaYc8E4uen1dMRUmRfluM17zUURQknpboeyV7r_uVFKfz5Ywk9KF-VotkaT34LE1nQGihfbPT1tIeBbDs-UDci5qWWHrBbHljYdX-rCw2Ks0-zla70GTgX7BzBN7hD553VgcPv5MtNLiA3XTI3NPLLu09vOvpJhTiqOmDu3oD6xBaaYiOBTLmvc2GO30q4XubsBYSK91u1YlfCtkxgeHokUu3aPuOj7vQr_MZ2OVDG88dgrCE-hMHN4G2h5C3ghtxx5ZrKfa7uHaCDUxKUqUbWMf2wof5x6YQbNQWqYXlZmt3z-JgK07P1_mHqwoEpxIXk4IR91jfcoJB_5ljI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
اولین‌گزارش نیما‌تاجیک پس از ترک صداوسیما و پیوستن به پلتفرم اینترنتی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 8.58K · <a href="https://t.me/Futball180TV/107241" target="_blank">📅 13:35 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107240">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c2e9fe0aa9.mp4?token=akRmL5gF41ukOl5n71uphik_QwuQGYuj4jLq11ad8x4oPXUk7tExUJKX6RmaD18fmODRtaDnkXkZ4I8w1HyKd3-I9C1pp_LZx7kc9UOZEM8UcsRJnECEM6-mB8w3fUEOGofYd2NAz1AfOWzKZTuZPK13bjH11ooIGQRtm1TQUb2w_e-QQG0TgGJ3lRwiy3Rw_9GydgDJl9HA3q6hVgN_N2xcgp7T3X-dDIWpzz7ladTFLO70LVvWyly5jM2Z4wsL5AwC2ixa69aYLMk1EYJg-ARJtBwyxVmYCfs8BSmzOxbF60BgxpqY4A1qZYpLhiaH_jumj8_54cniLwXQ5-NqUQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c2e9fe0aa9.mp4?token=akRmL5gF41ukOl5n71uphik_QwuQGYuj4jLq11ad8x4oPXUk7tExUJKX6RmaD18fmODRtaDnkXkZ4I8w1HyKd3-I9C1pp_LZx7kc9UOZEM8UcsRJnECEM6-mB8w3fUEOGofYd2NAz1AfOWzKZTuZPK13bjH11ooIGQRtm1TQUb2w_e-QQG0TgGJ3lRwiy3Rw_9GydgDJl9HA3q6hVgN_N2xcgp7T3X-dDIWpzz7ladTFLO70LVvWyly5jM2Z4wsL5AwC2ixa69aYLMk1EYJg-ARJtBwyxVmYCfs8BSmzOxbF60BgxpqY4A1qZYpLhiaH_jumj8_54cniLwXQ5-NqUQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
🇮🇷
🇮🇷
رد رشوه میلیونی برای امتیاز دادن به استقلال
🔻
اتفاقات هفته آخر فصل ۸۱-۸۰ لیگ برتر؛ قهرمانی پرسپولیس بعد از شکست باورنکردنی استقلال به ملوانِ محمد احمدزاده
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/Futball180TV/107240" target="_blank">📅 13:10 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107237">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/WF8mm97NeRPGmqU17lvgKe0xW-29nhSwxhjyxihD2rj6Ik9nl06tjb8iaWEn1Amjd50a5dzvP02AoI4-SWyokXa0tyuDVc1L6ZO-8KVuKso4Jg1MCfqXm4shJMEFBji3RFo31XkfdDyIOQpyNFVXdLjqlu8AkCqrp0maXgv2lNP9PjxJk6HjoCAvyyR1Amyseqf_hEWepg7e-j0pfhvKwQkfGtX9jLamui6-kpAta3aKEdjJpKceJgR9zRxbCgjUVP3LCl_NBGp5Wot-J8wZ1e08pO2UMw4XeunM50Zv5q7a3TlxNTUHulk8AL0CqPDfQoHOdZYXbjo8R8Tk8_OMuQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/EH9_7LSPs_pToWXNAaZFrB5ze617QqlrQ9m9rb3TIyK-h-cAYpIzmvy8vhy96XxW4O6hQ7pahPu-6N3ayofjO8-p13jy4tPXFwIcQCZVfRNoL-hYXv16LwM5lppBaXipTvfkowOeVE56znn1lG1-4KdozVFo8tVMhjtWN51CivrmEtIQSbuout-Ct-OSVTF5T532aqn8W4u4oPFpgFaYZiJVaKkmt9M3MwO56QgEx1iSK2Ln0Xv1G5gY60jvwEvR_QuqcZM1g4-ISTqblVt-X82pQhmk2vSgYH6pEJv-h2dJALrTGuepgAN0Bi5PzBSXjftE8LB85v7qb8xCCsFNbw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/dWFQFfqo4ZWfZsjPr2SqoGEu9EJqOiU9YInzLDReGfJS4WyzRdeOcDxAvwbS7Y-gTj_ep4qlJ2FktqAK9EDmpXM2kWRfoTJfkYehRJrBHSNKtvpaccWqMBCFH395qjU_qCBmBRKvxZPZmdr1eFZ4WE2ihluBe3oljQX9BmoVLO3gLPgHiTXR6x3yclDx8L8nyg5YOY2ELabw4kN_L7mSW-yLlagVcKbcoroiR_ct2xKMygYnrdnE72rs2H_gLt8ASJLPw8OPiLhVlGsA7nreIO3owaFPVHAGYKvohcE9PgDsYxdhVyVpTrsg-Er6-bF9dTejljIbxUFt-EhAqLfPZw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">✅
🐐
🇦🇷
تصاویر اسطوره لیونل‌مسی در آخرین جلسه عکاسی با تیم‌ملی آرژانتین
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/Futball180TV/107237" target="_blank">📅 12:45 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107236">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vMay0YFVtrGoMQZ-ZLt2f4P1sKGQgZJMfHVqWLfklu65iuauvjtEHzNaoGbu-4_3Hs4hfniBeWvj2MjBBOAF1tS2TaUUEin6TEOCNzzDIqszJQen0Xjh6Y7TqcPrz8KnKJXdsNvyVaf83XAv186B-ilf6BvF4P6GyMYNSfe_LnMyghtQTjyl80o8SXyMOtJXPSydmpJTKlrsPRobcv-hll9KW_mVr4f90_MRYTPGIQ4flpccgELXDkojOcrDXyaH1OKavOJudUYUSpwy9B0p0ElCmg9sAkNXnbAxSjC0yfskPr1OzeWugtR_uKJYTrdCDHbfs8rocQu81fdBg9BIFw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇧🇷
ترکیب‌رسمی برزیل مقابل استرالیا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/Futball180TV/107236" target="_blank">📅 12:39 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107235">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f4d91b2fef.mp4?token=RQeB3KqSDDGgFF91NOGG5WbpGtyIZAn8hnDq9hyzkDtGUXAtDxtQIzTnjamPlY9pX42B1oWMzVjUZMj8ipeYGl8jlJls6LkYLX0hbpIGhCQNF0mU2fcK2aUNPBi2qtFsfyFQW5Fvcp5aankstMQ7ZPYrPjtyPDDZTHCxU1g173GTJ3DQADUuERuIXSFlb9wefqdgnOZYBsj4ot0TGAHisZW1E4aYHhnexTciAe9tkOiQtbghW-500Ao35_GGUQeb94BOpAKJsrgkfq4tukFxqPlp1ifPAOyUwH_BPslDwd6G-JnFfP9RRHnmXC5bDg7h9DgbpsoI9GqZb5WWdaGtegCR1JTNvJd51mauzvDaCDD7RAXNm0h2zyHwp15COXEycexSfYsBLn59LTvQIXH0X0vaapvkOSB1kh37UvMKHVQk1TG0zb8DU5j9mA4z86HgAUF8sZIRJZmXsEUvOEgHMD9Lxhp6HG6DklVPZ1zaFDjGXtOXJwndVFDKDdv0-k4CwM3_5JVJKEz-spuLWasR2ZnPW_L69VhfmK8O9ZdhkYhxuqehVDaFm0jhAcyl3fzgL5TPnGMAbOqvVJkIl3-W-XLArDfDDvnqZU3POcmI_22Fyh6ZI3rQogIwbTOC0wb4sV9o2eseSbtpvjqLcJ_Qfqt1Bfg92wBaz6MSPPUhUkI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f4d91b2fef.mp4?token=RQeB3KqSDDGgFF91NOGG5WbpGtyIZAn8hnDq9hyzkDtGUXAtDxtQIzTnjamPlY9pX42B1oWMzVjUZMj8ipeYGl8jlJls6LkYLX0hbpIGhCQNF0mU2fcK2aUNPBi2qtFsfyFQW5Fvcp5aankstMQ7ZPYrPjtyPDDZTHCxU1g173GTJ3DQADUuERuIXSFlb9wefqdgnOZYBsj4ot0TGAHisZW1E4aYHhnexTciAe9tkOiQtbghW-500Ao35_GGUQeb94BOpAKJsrgkfq4tukFxqPlp1ifPAOyUwH_BPslDwd6G-JnFfP9RRHnmXC5bDg7h9DgbpsoI9GqZb5WWdaGtegCR1JTNvJd51mauzvDaCDD7RAXNm0h2zyHwp15COXEycexSfYsBLn59LTvQIXH0X0vaapvkOSB1kh37UvMKHVQk1TG0zb8DU5j9mA4z86HgAUF8sZIRJZmXsEUvOEgHMD9Lxhp6HG6DklVPZ1zaFDjGXtOXJwndVFDKDdv0-k4CwM3_5JVJKEz-spuLWasR2ZnPW_L69VhfmK8O9ZdhkYhxuqehVDaFm0jhAcyl3fzgL5TPnGMAbOqvVJkIl3-W-XLArDfDDvnqZU3POcmI_22Fyh6ZI3rQogIwbTOC0wb4sV9o2eseSbtpvjqLcJ_Qfqt1Bfg92wBaz6MSPPUhUkI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
دلیل عدم دعوت مهدی قایدی به تیم ملی؛ ناراحتی قلعه نویی از عدم واکنش قایدی به صحبت‌های یک مجری در یک گفت و گوی تلویزیونی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/Futball180TV/107235" target="_blank">📅 12:38 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107234">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f256fb52d3.mp4?token=tDgf_bpJjl0SsJeaNUXj5wTEOG-A40QqiR-XRDmpFYN1Fv1vlL2vErbCfhKqQl3uR8YaPdDSotINDNjHWATxSMQKGmDSN680C53s2d4LuJDlJhdGNWfudODlHHcWg6iOea2Z1GvZFYyLTE2VZ8KY_XMZXD3NfTZJGGR2ZHJHlbjCnhbkhTG-aTxSuQxT9v95G1_yURDMYVxXZ_OI2kQDpKoZoF5MvohGyMpDCGk3EIDGGaIbvlFRAWfIT983cw2S2NCJeA4zqOfTYK1q6PlI3wt26Gjojdr3JFZmGWQ4sXPyTt9XSPmk-rvLqRThkpz1kAiSGVs0WjMmXBiagsAeTA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f256fb52d3.mp4?token=tDgf_bpJjl0SsJeaNUXj5wTEOG-A40QqiR-XRDmpFYN1Fv1vlL2vErbCfhKqQl3uR8YaPdDSotINDNjHWATxSMQKGmDSN680C53s2d4LuJDlJhdGNWfudODlHHcWg6iOea2Z1GvZFYyLTE2VZ8KY_XMZXD3NfTZJGGR2ZHJHlbjCnhbkhTG-aTxSuQxT9v95G1_yURDMYVxXZ_OI2kQDpKoZoF5MvohGyMpDCGk3EIDGGaIbvlFRAWfIT983cw2S2NCJeA4zqOfTYK1q6PlI3wt26Gjojdr3JFZmGWQ4sXPyTt9XSPmk-rvLqRThkpz1kAiSGVs0WjMmXBiagsAeTA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
‼️
درگیری با عارف آقاسی و تهدید سامان فلاح؛ دلیل دعوت نشدن کنعانی‌زادگان
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/Futball180TV/107234" target="_blank">📅 12:37 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107233">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/Futball180TV/107233" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 9.76K · <a href="https://t.me/Futball180TV/107233" target="_blank">📅 12:37 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107232">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/To6mk0TJwPzHyKm3MNeaaU88XnP2pKzG9dn5KCCMM-YwdMA5aDDpjMTrCjZ0ZrW4vgAqAy-2Zm-lzZv-XwGnTr6zjzWa0Wwi3mk5epHrswl1_8aljPytsHhJps20cMGGxvIpfZfIPfxS2WTdCnK6KAxwRfOTtjGDVPPT_fZpj0-Z8oxNRMKrFiKf1FnuHga7I3n7ZsgH62egMIWT6sqkZF7KTP1RD7OudtiyWg5BadnTn0ZvGtMgK5U59nsa_Fmtpl92cr4PnmTmsZNPfUA__zhLCfU8MPb52EEM1HgqApf6n22r3qqVoZUWLc7U4-gPQqtBwqksUtip2SbrRQWo3Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🦖
مچ‌های مهم امروز در سایت بین‌المللی
TrexBet
بلژیک
🆚
ایتالیا
فرانسه
🆚
ترکیه
برزیل
🆚
استرالیا
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
<div class="tg-footer">👁️ 10K · <a href="https://t.me/Futball180TV/107232" target="_blank">📅 12:37 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107231">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7e518e3928.mp4?token=BNXlmPH-OGcyaPAyuRericaSQRpjbN7gToy6WfXu2yYtc1yITGOLrrzpqEfCJ7xcRW1kJxrzH7e2GV8v-X47rj2ayYTcUEsjOdsVBlAn4_clK-XD2zysa-qp51YquovKf5i4FGHa3Wd1XGhZlHs_CnkdLCf6we6dLWFzb6vfeA_psMO9OF6h_iXzxD89zb6X4FxcPM0dDfPevTQmq7ZEf4MzJ0CMM29L62oSJI4ukQs9gCumGMXUTy5Mx8Iyz3zHDQ5_tEMraY0eTNjqTDPTYP6yHbIXzlvlzkyGJT3OivDZRRnoYrrIZRJwxiyFIfyQT1thLXXbJQ4KkVC4yec0NQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7e518e3928.mp4?token=BNXlmPH-OGcyaPAyuRericaSQRpjbN7gToy6WfXu2yYtc1yITGOLrrzpqEfCJ7xcRW1kJxrzH7e2GV8v-X47rj2ayYTcUEsjOdsVBlAn4_clK-XD2zysa-qp51YquovKf5i4FGHa3Wd1XGhZlHs_CnkdLCf6we6dLWFzb6vfeA_psMO9OF6h_iXzxD89zb6X4FxcPM0dDfPevTQmq7ZEf4MzJ0CMM29L62oSJI4ukQs9gCumGMXUTy5Mx8Iyz3zHDQ5_tEMraY0eTNjqTDPTYP6yHbIXzlvlzkyGJT3OivDZRRnoYrrIZRJwxiyFIfyQT1thLXXbJQ4KkVC4yec0NQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
🟥
بازیکن تیم‌ملی اسرائیل دیشب بخاطر این شادی بعد گل مقابل اتریش با کارت قرمز اخراج شد!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/Futball180TV/107231" target="_blank">📅 12:14 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107230">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">❌
بهانه‌‌های عجیب حسین‌عبدی در بدو ورود به تهران
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/Futball180TV/107230" target="_blank">📅 11:50 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107229">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e764af88a2.mp4?token=DOcPx74V43U95i8QI09ggT2P1XrTQIdf7C4HnaKYMMGL_cFOJIfHdKxxfI4m1DW3Dx1Llqykvy01x0oT2AZXrkkKtK-ZgPx8NQgrb8eO_UVL48f855NTyBzDeMDJizPmZyGkRtb-TgFlFp4NiJDtVSOmSKIbUS-YSK_EviR2TfyyHVnrG163vgyHS8aDJA7yt3nzqxvjCOATQ4CW_9lpx90JtTb1V8v7UhmKui5d-weuTPOSxuZqty6i_mzpvinBvXeegvIPQurhH_PtLntEJE1Gr5CVkmmBXkUShCasTKyGKLcwbP4hVChfyxlyY84LHcGNM-Q01_k1pGetVlsXqQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e764af88a2.mp4?token=DOcPx74V43U95i8QI09ggT2P1XrTQIdf7C4HnaKYMMGL_cFOJIfHdKxxfI4m1DW3Dx1Llqykvy01x0oT2AZXrkkKtK-ZgPx8NQgrb8eO_UVL48f855NTyBzDeMDJizPmZyGkRtb-TgFlFp4NiJDtVSOmSKIbUS-YSK_EviR2TfyyHVnrG163vgyHS8aDJA7yt3nzqxvjCOATQ4CW_9lpx90JtTb1V8v7UhmKui5d-weuTPOSxuZqty6i_mzpvinBvXeegvIPQurhH_PtLntEJE1Gr5CVkmmBXkUShCasTKyGKLcwbP4hVChfyxlyY84LHcGNM-Q01_k1pGetVlsXqQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">💥
دیدار هانی رامبد پرافتخار ترین مربی بدنسازی دنیا با بهروز تابانی قهرمان سنگین وزن ایران حاضر در مسترالمپیا 2026
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/Futball180TV/107229" target="_blank">📅 11:31 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107228">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">🎙
صحبت‌های شنیدنی محمد احمدزاده سرمربی سابق ملوان که این‌سال‌ها به شغل دیگری مشغول شده
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/Futball180TV/107228" target="_blank">📅 11:05 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107227">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LdQV7Rbfwsn2QzsLFVYDaP4SWbgz4YGEaCu27mMTOmKjWAlg0pXC7UXM44OgWuwZq5LK87eetL1M89E1lhOY5-ODFn8m6SeCmsS2q4sPNTjZRCvfK-5nljCDL7SK9QQWqVFhO2KYi1p2YVG-A1E6vgNy_tGhJoFCdjFWTUcJ_9Z02IDBvId1A_YthKAUPf69jWJj5hZfC_sdiotyRfx2wBFzVSG0fVwx5aWrDTbWV_qipk7fNGOV7G8hQNNnSvxbG6g1H-inpscv-fTxndpuSMKh5FX5cpbpb_B_w363Ho7h6ukFDlxup03fYg1wAPtWgBhxmzqV3b4-M5yo7t59Qg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
عذرخواهی اسماعیل قلی‌زاده بازیکن تیم‌ملی امید و استقلال: از همه مردم عذرخواهی میکنم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/Futball180TV/107227" target="_blank">📅 10:59 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107226">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/f_D-t8KFDb7QdR2kLcaJMyR_hxcyOkicz0Wv6KCXyK8avV2scID8y0I7CYr96yylt3zNRBidcTCzVPzbonJGB9jCf247pUCk8U6NN_0rYTpr3D7BEEpaAnMoiveW5FZ7EQu5fjKw9hN5OyfbcSd-VfoYtDWGbbi-f1yoeWu_nAsaGiMqwL6GcQdfmODmac9HQwBKVXRsBPFY6iiTns6r7veqROwvlR9MNKzEenXqh-k34WiLmkcFNyxNZVxQSqJW1QCVlC4JMZFK0KH2V171c8f9ZT96L9J5And6NVtm6UQlpc8LwWqABb1bShahOSMMSaqBd-RrowK7E0UX_ZVn8A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🎙
تیبو کورتوا: بدون شک من عملکرد بسیار بهتری از کاسیاس، نویر، بوفون و ... داشتم و خودم را از آنها بهتر و برتر میبینم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/Futball180TV/107226" target="_blank">📅 10:40 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107225">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GhOXmwC4rmy7MDUbrGWfD-qj6cfgTWXlRkEXgKVI_yANN3-kFURNTMCx_mDyb6uzbMRxqvKuyxNSbueJAWA_GYzqVUsl92QeZRTjtVaJ4zMJs0fteCZ1steJlxNSxgXyee2Ekw7OwOleGy_1VbM95LxDnnChcJjIP22blXqIcR003j0RMb7kuAO_MQDQvp-QLOnGcXC9RhC3vz9Unyl5SkTImbY19CqbFNIKptkes3mi-8I669EEG_TZPuDW5_hKXjCd2Hmp4O9q1q5SA71Dq8goVIsT33m5KqnnAvnij_UZY25-YbX9xuPZjt0JfT4y_A2ldN-GSAX5dBPiMKWOwA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
🇪🇸
رودری ستاره بارسلونا:
🔻
"من در حال کشف چیزهای جدید هستم. بازی با پاریس در ماه آینده، به همراه رئال مادرید در ال‌کلاسیکو، تجربیات جدیدی خواهند بود. احساساتی که قبلاً نداشته‌ام و مشتاقم به عنوان بازیکن بارسلونا آن‌ها را تجربه کنم. و اگر مجبور باشم یک بازی را انتخاب کنم که بیشترین اشتیاق را برای آن دارم، پاریس سان ژرمن را انتخاب می‌کنم، زیرا آن‌ها در حال حاضر بهترین تیم هستند."
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/Futball180TV/107225" target="_blank">📅 10:15 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107224">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/19143fc835.mp4?token=PmktDxg6FxxORTUMzomoJmllurqD12rdhIsZGqqjV9ouzn4XlJuhGoAL2Gk7ydAzAfSC4AVaITTYmf9QcsRgjS9CZm2NszCwsKgfIbu6WYBMx_2xXZBClkbq6wRnwbqv4H4325wCrraaPKCPvv4JjEBNAie2QMky0LB7lP6AJqUY2p46H41b86BXVeKXIoBXoDaSqf-sIoPV0tGd-kiH5d2aJyBeyrOHzwViEUm89hBMkkmbThE9aF44wIaOhfYALQP4q1zOUonKr9KrcSBvbrl1_CiPRCNaT_dkLV3gVmIjoYOq1TJHHqM7jKScnZ76He_4AQ5C_4fdw1YCOhHfoA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/19143fc835.mp4?token=PmktDxg6FxxORTUMzomoJmllurqD12rdhIsZGqqjV9ouzn4XlJuhGoAL2Gk7ydAzAfSC4AVaITTYmf9QcsRgjS9CZm2NszCwsKgfIbu6WYBMx_2xXZBClkbq6wRnwbqv4H4325wCrraaPKCPvv4JjEBNAie2QMky0LB7lP6AJqUY2p46H41b86BXVeKXIoBXoDaSqf-sIoPV0tGd-kiH5d2aJyBeyrOHzwViEUm89hBMkkmbThE9aF44wIaOhfYALQP4q1zOUonKr9KrcSBvbrl1_CiPRCNaT_dkLV3gVmIjoYOq1TJHHqM7jKScnZ76He_4AQ5C_4fdw1YCOhHfoA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">این‌صحبت‌های بامزه ابوطالب‌حسینی رو برای دوستان خرج‌نکنتون بفرستید
😆
😆
😆
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/Futball180TV/107224" target="_blank">📅 09:50 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107223">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/444d39e31d.mp4?token=BjwzZO9d-ceX3Pm38LkijvzzLcZz65PHv6dz6AiJ8M7W0cEcHmazK1ZFtrOBP0CWJ2PIc6QvpKHHh7ybbgwagJK5UbXiQPDuYWNWL-aO_dDL881YMcnk_bj0JbGeJIS2u5-zTdj3YyLrrrP5bms8kSqxZxL-j8p7mp6dljmmhJVkD3f1qQLwpnmKm9K_xgaiJ8hiIXtoeLkHv8UEpL5c-rM0ZyVQv2-CfwHjBKcHRkNksFAn2JkZO7o-cxkttyZs14Ks0dohSaAqYnj2pmwArnacrj65bKYZgHr-Sy5HC4ADE9wCnZX4Xh9hv3uZFWCIb7XBLB747i8c1S67-Lw06g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/444d39e31d.mp4?token=BjwzZO9d-ceX3Pm38LkijvzzLcZz65PHv6dz6AiJ8M7W0cEcHmazK1ZFtrOBP0CWJ2PIc6QvpKHHh7ybbgwagJK5UbXiQPDuYWNWL-aO_dDL881YMcnk_bj0JbGeJIS2u5-zTdj3YyLrrrP5bms8kSqxZxL-j8p7mp6dljmmhJVkD3f1qQLwpnmKm9K_xgaiJ8hiIXtoeLkHv8UEpL5c-rM0ZyVQv2-CfwHjBKcHRkNksFAn2JkZO7o-cxkttyZs14Ks0dohSaAqYnj2pmwArnacrj65bKYZgHr-Sy5HC4ADE9wCnZX4Xh9hv3uZFWCIb7XBLB747i8c1S67-Lw06g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❗️
و بشنوید از زندگی سخت دیومانده
‌
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/Futball180TV/107223" target="_blank">📅 09:25 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107222">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/73d0f84bdc.mp4?token=i-AmPI1Vn1KWJduLMuj_bqy7UMrhBa12Ot29BpRGFfkPhfOKlAwMIHItsrv_xBqEP6O2iaczwfVkcS6QhmpMR-DM3ezNlQQqEjTV1HnLd6tga8G_jcVJsMDGmkZWgHp6D2hLgaZFRnxjDVLEQCIaB4a9aEAgxugenh5ubDUAfOOSyCt9ImIaIedOXiAu1B4VQfESyVsVqT89UCK9HsFRBag-tqgSpiUkr7xia8jccx9v6KenQ6K9fnKuBWVeOY7PcfzteOTGKH6lARtr9hNsQMc_hMRBnf1ExLuU2kx5Xoy-oJIwBo_ExrejTAhez4GgIRGlf0TYNHX-xNE8ByBWRb5VyuZ4w9kh4mxMDKXAppEr0yUdzT4boXD5BCOkxeauzl4Hfbb4bK2i_90FH79nQhs7oOdki_R9HCW7s3hq-VCb3sv7clzuLbiab25tK4T6ttjPXL9ss54pLtvqjc5ICp5s3WHZ6ZDG4Yr8w9XXWaPK-Md2jYR04UVTKE9Ngp5seORF9JRS4aL5ix3XRACl9x_Hb-e0n8ubeESrTtEPIt4xURrXkEwZDQ-klYxtPe2cXZckZWH2AdHt7-EhUKZLTib8pERHX0MoOVWk4ODuXqKvFejkk-wo3u_10twq-EEp23onq_aZr9OLce4yRoL50g4rsy_pjc9iiyKi0xtWxFc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/73d0f84bdc.mp4?token=i-AmPI1Vn1KWJduLMuj_bqy7UMrhBa12Ot29BpRGFfkPhfOKlAwMIHItsrv_xBqEP6O2iaczwfVkcS6QhmpMR-DM3ezNlQQqEjTV1HnLd6tga8G_jcVJsMDGmkZWgHp6D2hLgaZFRnxjDVLEQCIaB4a9aEAgxugenh5ubDUAfOOSyCt9ImIaIedOXiAu1B4VQfESyVsVqT89UCK9HsFRBag-tqgSpiUkr7xia8jccx9v6KenQ6K9fnKuBWVeOY7PcfzteOTGKH6lARtr9hNsQMc_hMRBnf1ExLuU2kx5Xoy-oJIwBo_ExrejTAhez4GgIRGlf0TYNHX-xNE8ByBWRb5VyuZ4w9kh4mxMDKXAppEr0yUdzT4boXD5BCOkxeauzl4Hfbb4bK2i_90FH79nQhs7oOdki_R9HCW7s3hq-VCb3sv7clzuLbiab25tK4T6ttjPXL9ss54pLtvqjc5ICp5s3WHZ6ZDG4Yr8w9XXWaPK-Md2jYR04UVTKE9Ngp5seORF9JRS4aL5ix3XRACl9x_Hb-e0n8ubeESrTtEPIt4xURrXkEwZDQ-klYxtPe2cXZckZWH2AdHt7-EhUKZLTib8pERHX0MoOVWk4ODuXqKvFejkk-wo3u_10twq-EEp23onq_aZr9OLce4yRoL50g4rsy_pjc9iiyKi0xtWxFc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔸
❌
زیباترین ورزشگاه ایران، درست در کنار یک آرامستان؛ بررسی شرایط عجیب ورزشگاه تیم نیکاپارس چالوس
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/Futball180TV/107222" target="_blank">📅 09:01 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107221">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/Futball180TV/107221" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/Futball180TV/107221" target="_blank">📅 01:25 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107220">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WGfWvWELNG5woyT5QR01zgiLCgoylNAzK1nKp8xi3Pgy4JCiWTG1vb08f-a_pd7SFrIsCx4e7Ciyer5YCUzPunZAkoOgun6EcInY7xLVEQ0oDIdIkkJU6op8XMNn--N59utxZtqn_O3Cvwzc3EYex92-m1eWwoGnP9u_7wbz0xDL0S4TbHmiYNLNtFwsa9zdnTcWhCCPLb3QvBWGzh2fIMZCH_Qqj-2qpcYWrJ9AJeiglODMNK3ipZW_1MK6p9GfYnaeYEa0_NtXYYxyqN6x48Nzk5nata1aFfj_xKR3dx9QiAMjAG9_vs1wTmLCxQrYP4YV6VkppZcSg37luhHwOQ.jpg" alt="photo" loading="lazy"/></div>
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
واریز اول:
۱۰۰٪ بونوس + ۳۰ چرخش رایگان
🥈
واریز دوم:
۵۰٪ بونوس + ۳۵ چرخش رایگان
🥉
واریز سوم:
۲۵٪ بونوس + ۴۰ چرخش رایگان
🏅
واریز چهارم:
۲۵٪ بونوس + ۴۵ چرخش رایگان
🦖
🦖
🦖
🦖
🦖
🦖
TREXBET — PLAY. PREDICT. WIN.
https://TrexBet.com
T.me/TrexBet_Ir</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/Futball180TV/107220" target="_blank">📅 01:25 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107219">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kFzMz5Md2d9sGg1T7zloRhu8m9cH1AGZUogcwdtD9tX1ysrFIpEsuv6dFPJQRxMMU6O53bh0OfwRFDzd8tAJ1am3Lt9h7fim3PCb_5oEspi_T5EUTjz516aVZqPnXZvGRCw-ZG-iuEQkLyeNp8rV_jT0FkK0CQjXUwNR5cetl__XcKpK70U4JRs1B19LADjrVrRbdbC9wg2UZnm9tt5exrpU23PnsOkJWOMQ9tsNewTOrlhrSgEX7T2KGcGIjMdN19kqNOCCn6xCcQb60aGXH47qGeKXrnyrOR7veFG2K__NsZ56Zd04ag2RJS8-hR3e0vY6BRT4VA2TiAphXKcUmg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🇪🇸
دین‌هویسن مدافع رئال‌مادرید: شکست مقابل اتلتیکو تقصیر من بود و بابت این موضوع متاسفم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/Futball180TV/107219" target="_blank">📅 01:09 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107218">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LTLKtlFyOpY0XssEWc18X3YtWhlSI_ZXxaZhA1oSXDgKqaFUpOKD1zNOPORbwEQFF5ot6qUFnIwr_45a-WcXYrto8k_agBG0_XGfCAbDq_cnU0tGIIRMXH4CkMJC2Q1JNpxDIOnUNIONiSTSnrZBwAAZgE2ovdgQ1dKaNaYwCEQzAkb3o83xXHpEZ5VmAdB-aJHdHYOAkFs01bJIjImSFRDlf5gGKQgCbmBTGNf7F8yn7Tp0cW72cexm0i5d7fk70VP2_ldD88sjR0tmfLLBYCGBeBFQbmkmApeIiwNHngz6eHnod85-8ua3dRqdGcmDno4WBcPsToBCj3uFone17w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
✅
🇮🇷
مبین‌دهقان بازیکن تیم‌ملی امید و الوحده امارات مورد توجه سهراب بختیاری‌زاده قرار دارد و در نیم‌فصل قرار است مذاکراتی برای جذب این بازیکن از سوی استقلال آغاز شود
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/Futball180TV/107218" target="_blank">📅 00:53 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107217">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d8c410e310.mp4?token=qpQRf-eLjPWtOtoLA1crtLjw7nNr9GDxDEIjFhJ4X8U25DGEYvml73X7z0O-R-2Xt5LAN_sauqZIYb34m-LcKVcnGPUJRsIK09W5UmzWCMoPeb1XJRCTAUKvZOIzSnAt8SuBWONDl_ruGHTpLlmSz9JCh8VB9tm21M0XaHH3QkbidSAbyR5k-Lw7dxjeXsCa-1MzvB081eoJBFlg3Nam9hPnxi5O5XwvNNaZ1oClQYIo6MSR73c_clGMP35X8OeXsywryls5LJ3v5jTg8mRTsYJTC06HTS6xuY5TvefWcO-DKiP-yD9oFLUEeYwS1v4b7qFUE-f3XjL37eh8kqFuib35vS56qzgokby_Va-QRgFOq_ID6M00McgxrGyXm1U_Sh-HNiX8E-ND-SLUdMlTTBMIJyozSzL5RD-zoLDwk3gxypQS9N0tAnb96YNmurQ4VynjBZ91ZePGg0Vlmd7Jtdpkf2xJA6YiAott4cazrTwPgeu37ucjqUHL95BOuIx2GHX39QRKw8mWaMCHXO7lsQ9g0YwFJkKNoJGQUoNeFq4NIv0rNFwbR7DvJA-AZfnuEPvb46-QvNKfUMI3OWVf_6JEmodBkc0Q5qR5_oJi7HgCKEF_wdztosTaTiQUIL6K8QTnlyNTUtQICGIdjNNb9DZJ8cjkk2gBKWx-etxv_pY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d8c410e310.mp4?token=qpQRf-eLjPWtOtoLA1crtLjw7nNr9GDxDEIjFhJ4X8U25DGEYvml73X7z0O-R-2Xt5LAN_sauqZIYb34m-LcKVcnGPUJRsIK09W5UmzWCMoPeb1XJRCTAUKvZOIzSnAt8SuBWONDl_ruGHTpLlmSz9JCh8VB9tm21M0XaHH3QkbidSAbyR5k-Lw7dxjeXsCa-1MzvB081eoJBFlg3Nam9hPnxi5O5XwvNNaZ1oClQYIo6MSR73c_clGMP35X8OeXsywryls5LJ3v5jTg8mRTsYJTC06HTS6xuY5TvefWcO-DKiP-yD9oFLUEeYwS1v4b7qFUE-f3XjL37eh8kqFuib35vS56qzgokby_Va-QRgFOq_ID6M00McgxrGyXm1U_Sh-HNiX8E-ND-SLUdMlTTBMIJyozSzL5RD-zoLDwk3gxypQS9N0tAnb96YNmurQ4VynjBZ91ZePGg0Vlmd7Jtdpkf2xJA6YiAott4cazrTwPgeu37ucjqUHL95BOuIx2GHX39QRKw8mWaMCHXO7lsQ9g0YwFJkKNoJGQUoNeFq4NIv0rNFwbR7DvJA-AZfnuEPvb46-QvNKfUMI3OWVf_6JEmodBkc0Q5qR5_oJi7HgCKEF_wdztosTaTiQUIL6K8QTnlyNTUtQICGIdjNNb9DZJ8cjkk2gBKWx-etxv_pY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بومیان استرالیایی این‌شکلی از بازیکنان برزیل استقبال کردن
👀
💥
🙂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/Futball180TV/107217" target="_blank">📅 00:31 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107216">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/towhBeUOIPsnWsA6c5iNjTsHDKVeScBta3CW_UrHvPUj3JVW7U4tRFo_ZLBD0HOz8H3NojNFIFfQvA64rBrSJ1mdSCKMSYlIAibVgpFqPJzuLraWzTiwc0ivIuXcEJ5056If3nBsfbhE37z1ljq2vC7sFx5hd7vbF5BQoOnSX0oJ5vxgOwehLzF0A-3QslKOcSEUYmtCsiKN8rwguctO8zFwD-8ptLAisyL-3eT4auuzvdKSxSgG39VlY8JAZud5V4G5VAV3a77k3FSlS9lFVzMg8bePJbYA4B0hJ9Lle7waKFqFHlffWOctIU1DATz29_Az7XBtkOYyd1k-egTfWg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
✔️
نتایج‌بازی‌های امشب لیگ‌ملت‌های اروپا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/Futball180TV/107216" target="_blank">📅 00:27 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107215">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oz36Ui5c4-alPqnwVAqRTK11AJFMiWOJApokJwqrYjtGG3ZuX7rBw2XFqT4C2HMMs6uaYBfhhwEO2zqPmltpH4MetwVSsn_5PAGTEjtjUjs9SLnKTDCh1NYfvJrQOD3BndBv-7c8cK4sm3YTU2MmoAOTT7fntC61qcEddnMAkug8q_vlLSzgmfXsnh2TQELrGX2GDPhtp9Dpz08RwUvJhiVlnxjDgbtiVSvpfTytLPoBRGi8YNYOzaJz-U9Xr33ssdbWqp1l7xSmUTbEJE-lx9UtruTH7VjMZmSfTDKda3_8WtlNdkLG3Wew1miHXNRZdDhnkH570xmylW3B0cXS7Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
🇪🇺
🇳🇴
هالند اولین بازیکن تاریخ لیگ‌ملت‌های اروپا شد که به رکورد ۲۰ گل زده می‌رسد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/Futball180TV/107215" target="_blank">📅 00:24 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107214">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">‼️
⚠️
خداداد عزیزی: چرا همش با ازبکستان بازی میکنیم و میبازیم؟ با این تیم در جام ملت‌ها هیچی نمیشیم. بازیکن جوون هم که نداریم.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/Futball180TV/107214" target="_blank">📅 23:43 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107213">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VTCCB6rkhlksRSoOw3sjrVdqzj0bGBPW1loUrJ_m8xISXB6WymgD-KhOfNFCT28YWiLtsq8hJXxF3V02IFbsdXi3qWzSl3e7cZWqrnLiX7iTHnW_3yqOAeNLuB-xDuQIE7PkRi-TdfXRo-05ACxqiUZn-9oCQDNwJKe-vaU1_dzGqrhHiZz7SPAeIxuYxYuU3It8DlEWpC9X1Bnho0h_7EWiSkUn6W4wT0ds5Q1oBMcBopACMQk8i3q6d8O1KqDfweLBAFk-N0al4PUYb08y5PCMGSQtFMu_dXSOEv-zHXapIcPKzeVmuSjciui7C3vlb7iVYegQj3BIYzWtNccVWg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رونالدووووو زدددددد</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/Futball180TV/107213" target="_blank">📅 23:33 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107212">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">🐐
🤕
اسطوره رونالدو امروز اینو گل نزد تا به روند درخشان‌ خودش ادامه بده
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/Futball180TV/107212" target="_blank">📅 23:32 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107211">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ev76wjZAeGRWrCjeTSooE3f4GbDPb1dassds3Jh6pojowQ40OlNYaEVwp-bgHGL5PKYkh0b08MyBMIbaqdpO3AA4qKHioL6FV28SnoAQ_WDB0LYFyIbN2D-uY75MjvRnxgSomMgRs8h4WbMM9GrJdgc_uwOkg2rTQgtFqrpQ5vg1kmepDOVje1NbUy9-EUYd2Nmye15V9xop6d3_f_0wOW8CSHv4h9rcjq-GRAqLPCj7FrDgBnmW1GWumB24hxO2GovZ99Z9OsO8lwXUKzboTRc7VoK3af_0jnuICCCpyofHQ3u7xfN7RanOUJCt1TCwlTu3679fQVpDeJ1wN8qIrw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🐐
🤕
اسطوره رونالدو امروز اینو گل نزد تا به روند درخشان‌ خودش ادامه بده
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/Futball180TV/107211" target="_blank">📅 23:25 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107210">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YEulnqwp4j-9Nkhi3CAB8oop_TtNsOqRtdg0wdXS6tjDyY6bX1xheHm-VLuxtOYAP-UQoZxlUKzQBgEwPJMNZ6-L6xoofQeVKuwWsSgqmcYN8ttVQiz5RM57GntgGvBRKpKDn__3sNHCKEeynLj8Ms-HxwUWRzJMGRQ0UkMHDOpy0ydMnVCVF_TXVXuO0SB5dskxSWhlEACWxYPaZHnTX2GtVYX2kPq3F68hSqebdatnqub04WrWaJEk1cps6ds8Xe4rBHnJYyVBo9oN-yCeg534c2VZP-js47jt5lGjn_oBl2wFFekJaDUkoaR6HEZXlcKI_0vVwyNkYHqClO9xTQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
🇪🇺
🇳🇴
هالند اولین بازیکن تاریخ لیگ‌ملت‌های اروپا شد که به رکورد ۲۰ گل زده می‌رسد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/Futball180TV/107210" target="_blank">📅 23:21 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107209">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/a0f7b1f262.mp4?token=lmbARgmBz2U2VnhFYhG64wsqdM3iU-V9S7vwHP7Fldq2VbhP6j7-OsqIuqiC9YnTWeBB74xudBkPbdcnN7h7WGhfWsGu8g_HsnDPHnQH2b-tgYFWmnPP8wk4rbd8TROye90E0e_6aV5qP-yTet_TPrCQEeX6voNXAD6iYW7AYja37SQFRE0d7nBnZXzeahumkOpz2DSHZztKNPLUi5V3CsI8Rwg-YTrn14njhzA6C0VZ9ihQb9SxTNa_69z6TSrQJ3QmdOgEV0CZCBaC7aR1U3EymeALlEbVG1IP3mBBum9gJ6zMGmG4kMC9eh7OE6CMCMoR4bwcsc-K4oxp7O-TZXm7Y_9bsasbiea45A3dnKyVHJIAsyPgrBSNAH9ULGpAZFWLdZXl15rl9nSlv3VLH4gW81oJc5AoIxGLIgcwM82KRhwUZZ1YzSIBHJRJsDt_M-hUiMUQCznbnIru7XOhPMtWeW_--b8N9HxH8Ln7NipswSGq6BafoD7Vgrq5YHDUoxZqDqVJXiuE-mADQEjNKB9babAgqzwiBSH1W8PCn86jT1q3iU3DAoKfVO5WcmSYr6-r2-EhfZWqkcGlAONrxVDAouxs4KYAiqw5nHVMS8Em1y2kZQISv5itnVsKsV8fxMfRPWQIrrCvIiEPWELQf39TsvK8A_jclk99qCCFOTA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/a0f7b1f262.mp4?token=lmbARgmBz2U2VnhFYhG64wsqdM3iU-V9S7vwHP7Fldq2VbhP6j7-OsqIuqiC9YnTWeBB74xudBkPbdcnN7h7WGhfWsGu8g_HsnDPHnQH2b-tgYFWmnPP8wk4rbd8TROye90E0e_6aV5qP-yTet_TPrCQEeX6voNXAD6iYW7AYja37SQFRE0d7nBnZXzeahumkOpz2DSHZztKNPLUi5V3CsI8Rwg-YTrn14njhzA6C0VZ9ihQb9SxTNa_69z6TSrQJ3QmdOgEV0CZCBaC7aR1U3EymeALlEbVG1IP3mBBum9gJ6zMGmG4kMC9eh7OE6CMCMoR4bwcsc-K4oxp7O-TZXm7Y_9bsasbiea45A3dnKyVHJIAsyPgrBSNAH9ULGpAZFWLdZXl15rl9nSlv3VLH4gW81oJc5AoIxGLIgcwM82KRhwUZZ1YzSIBHJRJsDt_M-hUiMUQCznbnIru7XOhPMtWeW_--b8N9HxH8Ln7NipswSGq6BafoD7Vgrq5YHDUoxZqDqVJXiuE-mADQEjNKB9babAgqzwiBSH1W8PCn86jT1q3iU3DAoKfVO5WcmSYr6-r2-EhfZWqkcGlAONrxVDAouxs4KYAiqw5nHVMS8Em1y2kZQISv5itnVsKsV8fxMfRPWQIrrCvIiEPWELQf39TsvK8A_jclk99qCCFOTA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گل‌اول آلمان به هلند توسط انمچا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/Futball180TV/107209" target="_blank">📅 22:55 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107208">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bf1a30387c.mp4?token=emKt2cHldNGwVeEaVZ2hM_2iDx4_FZbweFmNlo67m442rGLrKmZmrlNgFe3r_HdAZ0rhLgnNecyeYLDgyOsp1pOawBW39AD9rL4NkrztPnxyHelnrgeL59yQbpdqk7Rv7zb16rqI_sDQmqeRPck1d5XTGbZuZwXS7vsdJb-CA0MkypXPOtpdtPN-MgNBETjQDbbkO-ku-SWNbfqcioWjFvRHXKqlAv8FLdw7XXXnAZYLxoi0El3Qhf59XNn-T0JCRH7IR-ql_lzbV8i18eGHoCVhttXI6LpLJooKkmDtQB3uySOotOGAKIKpWVrlPkiDPIQfTK8ciWTbtZnpJClz0Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bf1a30387c.mp4?token=emKt2cHldNGwVeEaVZ2hM_2iDx4_FZbweFmNlo67m442rGLrKmZmrlNgFe3r_HdAZ0rhLgnNecyeYLDgyOsp1pOawBW39AD9rL4NkrztPnxyHelnrgeL59yQbpdqk7Rv7zb16rqI_sDQmqeRPck1d5XTGbZuZwXS7vsdJb-CA0MkypXPOtpdtPN-MgNBETjQDbbkO-ku-SWNbfqcioWjFvRHXKqlAv8FLdw7XXXnAZYLxoi0El3Qhf59XNn-T0JCRH7IR-ql_lzbV8i18eGHoCVhttXI6LpLJooKkmDtQB3uySOotOGAKIKpWVrlPkiDPIQfTK8ciWTbtZnpJClz0Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
نتانیاهو وسط سخنرانیش یه دفعه پیجر درآورد و گفت اینارو یادتونه؟
اگه یادتون نیست، حزب‌الله خوب یادشه، چون ما با اینا، منفجرشون کردیم.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/Futball180TV/107208" target="_blank">📅 22:10 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107207">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/305c017139.mp4?token=Aeo-AQjGCM6EUjNhYDxD0fiR0zPt8HjOM5NHXBGV5KLixaHgL5btupu9v1bVzUz_KTRoSJb1oqFOnvI7QQb-V9_1MjqXIhvkR5v0iJYLXngaBgAhYhbbTqKvzzPWb9LBT7aVKRYB23S1CqLrLiHnL5TWAjPhW-q8ZIOEFmMt6pc9p6LXRPMFt5YxLCTU4LsJVImHgT-1rfDKwjLL_AQyARoYpojEQ0F4yFc7cFmjBZF60hU-fb9xP7B1MxcbX1DBRf0r5PQfpqNurrD7kW31qUfbTYtDji86bWCEsI5a81yYK7Hp2g19bqtF4ladefnA2pweFeC-ojRoX2k3i2gWwzzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/305c017139.mp4?token=Aeo-AQjGCM6EUjNhYDxD0fiR0zPt8HjOM5NHXBGV5KLixaHgL5btupu9v1bVzUz_KTRoSJb1oqFOnvI7QQb-V9_1MjqXIhvkR5v0iJYLXngaBgAhYhbbTqKvzzPWb9LBT7aVKRYB23S1CqLrLiHnL5TWAjPhW-q8ZIOEFmMt6pc9p6LXRPMFt5YxLCTU4LsJVImHgT-1rfDKwjLL_AQyARoYpojEQ0F4yFc7cFmjBZF60hU-fb9xP7B1MxcbX1DBRf0r5PQfpqNurrD7kW31qUfbTYtDji86bWCEsI5a81yYK7Hp2g19bqtF4ladefnA2pweFeC-ojRoX2k3i2gWwzzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
بنیامین نتانیاهو، نخست‌وزیر اسرائیل:
«
نابود کردن تأسیسات هسته‌ای ایران
کار دشواری بود؛ واقعاً بسیار دشوار بود.
اما برای من، این یکی از
آسان‌ترین تصمیم‌هایی بود که در دوران نخست‌وزیری‌ام
گرفتم؛ چون اگر این کار را انجام نمی‌دادیم،
همه ما کشته می‌شدیم!
»
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/Futball180TV/107207" target="_blank">📅 21:49 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107206">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/22263541ab.mp4?token=PGAlyMXrSA2JqA9f3m0AHv9YdwsNb54Iu9sfdTOTtM7Ovn-42j411Q_-bAlLqO9_yIzvRd6eYiApE16t0Bm4BtSUow3YcFrdjm_B5LXX4QitflIAVd19meZ9tnjf7xLhaO2wgKHl9c7iRF4MVMCtmEDePYIpuyTeTkTbRnXKxC5NrPZivuwxoMCligJkKaYoKX6mVhP6S8YUOVflqXRV-dJVDpa5SVL-kp2HuTTWB_1Kq3I2vGkK-ffCNw3JcY0kY-G0kpx04KkvTU78gnVFFwW4P-bETqKAEbYlUPiFvpjjGslJQ1vyIsTKBTw_wO0i2QZ2Qfo1ZYsgLB4Vl-D-BGLTemyn90OqCEznVc76bmUBtSm53GjmFvBwNt3YG69uCixF6OG54dbFsbQygrba9DXUk11eDgB4XUXbXWmpiZxr3UptRRZN4DM6xmkwadj_mTQ0_dCx10_GIqmD_9N5BknsL_YHq-cFT-_BMm2uycivycixh6bw4xvDj93KBbEiPvnSVno2vKimpyLHs-G3I652aiyu46vs989Qf8gKfUslXb5TQGA-zh8pHvK4OyX0xG8BV19B4Jy1NTa7cubTMZTr3qbfc06R1V3dfnSDRQvi8QUwgXQuA6CAdJ3tigwDHR_ip_4IxOi0ZqWns7QfEkrmh4kH0IVoGEAYtdCEQwc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/22263541ab.mp4?token=PGAlyMXrSA2JqA9f3m0AHv9YdwsNb54Iu9sfdTOTtM7Ovn-42j411Q_-bAlLqO9_yIzvRd6eYiApE16t0Bm4BtSUow3YcFrdjm_B5LXX4QitflIAVd19meZ9tnjf7xLhaO2wgKHl9c7iRF4MVMCtmEDePYIpuyTeTkTbRnXKxC5NrPZivuwxoMCligJkKaYoKX6mVhP6S8YUOVflqXRV-dJVDpa5SVL-kp2HuTTWB_1Kq3I2vGkK-ffCNw3JcY0kY-G0kpx04KkvTU78gnVFFwW4P-bETqKAEbYlUPiFvpjjGslJQ1vyIsTKBTw_wO0i2QZ2Qfo1ZYsgLB4Vl-D-BGLTemyn90OqCEznVc76bmUBtSm53GjmFvBwNt3YG69uCixF6OG54dbFsbQygrba9DXUk11eDgB4XUXbXWmpiZxr3UptRRZN4DM6xmkwadj_mTQ0_dCx10_GIqmD_9N5BknsL_YHq-cFT-_BMm2uycivycixh6bw4xvDj93KBbEiPvnSVno2vKimpyLHs-G3I652aiyu46vs989Qf8gKfUslXb5TQGA-zh8pHvK4OyX0xG8BV19B4Jy1NTa7cubTMZTr3qbfc06R1V3dfnSDRQvi8QUwgXQuA6CAdJ3tigwDHR_ip_4IxOi0ZqWns7QfEkrmh4kH0IVoGEAYtdCEQwc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
بنیامین نتانیاهو، نخست‌وزیر اسرائیل:
«
۱۴ سال پیش
، روی همین تریبون ایستادم و یک
خط قرمز
ترسیم کردم. قول دادم مانع از دستیابی
حکومت ایران
به بمب‌های اتمی شوم؛ سلاح‌های هسته‌ای که برای نابودی اسرائیل هدف‌گذاری شده بودند و می‌توانستند
تمام جهان را تهدید کنند
.
ما دقیقاً همین کار را انجام دادیم.
این کار
بسیار دشوار بود.
»
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/Futball180TV/107206" target="_blank">📅 21:48 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107205">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8ca9f3311b.mp4?token=ddD7bXWAHVq-rV_WpSzi5y0uUyKgzXdqlzjBGJ8kOI7J6Jm-Ygg_p0yqI9sjI6jYfXR0ZH3cfskg6v2JjR_UBuGNOvoVQDWYnpkpRX8wRftBHUStQA6Pb3VFFNYyDYc3Kd-Gyq6TKpRhsxIrn1coMZWyFJYeEHV5tkkHmNmfao2vhMgvZ_-QVU3yZZWqXXcEPnRE467ktQNuSbtcAj2OEWqo-5wke4U5V_OfFkVmJ7n8tmVKfKeDniQ4YD986-wZpvHhMErq2MZWh5s9v843kyHHJGkxTV07FgjrJKmh2b3fTbYOKqelmwf0hAwhG2DcHUJw3G4EZMhR_wCo0SZ5dg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8ca9f3311b.mp4?token=ddD7bXWAHVq-rV_WpSzi5y0uUyKgzXdqlzjBGJ8kOI7J6Jm-Ygg_p0yqI9sjI6jYfXR0ZH3cfskg6v2JjR_UBuGNOvoVQDWYnpkpRX8wRftBHUStQA6Pb3VFFNYyDYc3Kd-Gyq6TKpRhsxIrn1coMZWyFJYeEHV5tkkHmNmfao2vhMgvZ_-QVU3yZZWqXXcEPnRE467ktQNuSbtcAj2OEWqo-5wke4U5V_OfFkVmJ7n8tmVKfKeDniQ4YD986-wZpvHhMErq2MZWh5s9v843kyHHJGkxTV07FgjrJKmh2b3fTbYOKqelmwf0hAwhG2DcHUJw3G4EZMhR_wCo0SZ5dg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
سانسورهای تلویزیون که مغز رامبد جوان سوت کشید موقع گفتنش!
🎙
افشاگری باور نکردنی رامبد از سانسورهای صداوسیما: بعضی از افراد آنجا مریض جنسی هستند!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/Futball180TV/107205" target="_blank">📅 21:33 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107204">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/azHCfRpwX3LbdrirPZKWWJkiQcQk3CYyq26Lm6mUTPHpjQCpAKLZMPZFifHV5o4VcuZtEkve8xfs-JVfTs3CrPPQYaA6pnGriGa99Dg9mzhimbwCYefc7GWw_KUzqzigV2mPWMOUQCJCrYJQqhF6Vm7fscF2CfOvDDKcZbnlF8JaRaMEw2c5_W0jBoXy53WRSkzlakrVXhzHz0yt20w-MLmGxTelDRZk8Q8eWue5mlhm4zn_Mhfx6xKnNTCz9nIgLo-MBN2By6lHFkoP2Hk6yNk4xOX6LekpGOo0Xgml6BEUzXS7zhpzhB3DH55nlYhbRRW00pXvpcI2NuF_t3Sf1A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
✅
ترکیب هلند و آلمان/ ساعت 22:15
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/Futball180TV/107204" target="_blank">📅 21:13 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107203">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nyqmftgrTL8WC_PIWxGFFuzng1YrvvOiBheVABH2bl2iAV8AtqbhQMisFaxyj43octHY0MJtuMQvzVG29eY9fStV3-C8IfMcX8si-dkxofEOFP9NelUFy1djJOsbB8xnNSK7xRCJB63LJT34aYfoceVT0j313JhrCmbq27ApA1DJ2qgIjPBQVsP6GwlTT0F3k6Z5_R3SAQTAhM5rPCgUUqblVfjKz-HnbZzCKpmlNiagItsO813LjsCBsag6UBD4fECEXXTI70sFyE4l6oGDvEZcfZkU5oLaOClMqbvwm0_-n9udIpA9rqmBkGOaSaeMl7atQ6CYO9E7y8Owg-Ieag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✔️
ترکیب تیم‌ملی پرتغال مقابل ولز با حضور رونالدو
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/Futball180TV/107203" target="_blank">📅 21:10 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107202">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6388e432cf.mp4?token=ngNNfOndC59usdr397IuEwsx41Q965I1z7veXIy7Siodhyw4BNxPrpL1MIG6uO-himKamii92X8hocksR26vphR7KzZ5YjaYiDkjTxNa3VjPlnW5GC-W7HQBYkviY6IIFZ2cSGAFz4Wqmf7irvYnO4LVvGaUGrCfXaXucO3-jvIZyieTO9p9C9pl5YoGLkTglNmpKHGz2UiqhEi40EoStq4pHK1NvGo-ohfUeDyDuLxHxOwd1qI_bjgYleVH8wbtxypePvgEKbLkA1FSfTHv5KitcCNatdqY8E_L4PlGf4F1qd9rK6ILfEspzNqCN8D7ggR7a_4AxJd-MhaxtcTgUw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6388e432cf.mp4?token=ngNNfOndC59usdr397IuEwsx41Q965I1z7veXIy7Siodhyw4BNxPrpL1MIG6uO-himKamii92X8hocksR26vphR7KzZ5YjaYiDkjTxNa3VjPlnW5GC-W7HQBYkviY6IIFZ2cSGAFz4Wqmf7irvYnO4LVvGaUGrCfXaXucO3-jvIZyieTO9p9C9pl5YoGLkTglNmpKHGz2UiqhEi40EoStq4pHK1NvGo-ohfUeDyDuLxHxOwd1qI_bjgYleVH8wbtxypePvgEKbLkA1FSfTHv5KitcCNatdqY8E_L4PlGf4F1qd9rK6ILfEspzNqCN8D7ggR7a_4AxJd-MhaxtcTgUw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
مجید جلالی: میلیون‌ها دلار خرج مربی خارجی شده اما برای ایرانی‌ها هزینه نکرده‌ایم به همین دلیل است که می‌گویم قلعه‌نویی از مورینیو بهتر است!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/Futball180TV/107202" target="_blank">📅 20:46 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107201">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NtwCbzLb04FpKGg_laLlz3zUyLvrAakawLjAj3aLp6OB0efRIGRIW5eC6ecS3Zc7eVDEnQOvWoFcem6Kiuf6-uR4Klhl2OeEVVknQ9qG5qJkA0eNBWpaoNDep-tDqtyuKSeOnGMT5WnLW4QuhKjf9xDxc40P3slRneZC0xXMc3nGA5gIPfMkryv_hwzT-4P3CPbKO33IcbaTpoHSvWSwTi4twemZYlC0z71Clvhec17zat81BXGu76epqt3fQEOG001NHnSshaLxvkdGu1dx6jnjRjNCfAV50YYmTLcwjQ1SDt4KqTckNbX4U68uvuhEqCsfBcvFe5YX9ZGL1A6HPw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔻
🇩🇪
اسکای اسپورت: بایرن مونیخ در حال بررسی امکان اقدام برای جذب دنی اولمو از بارسلونا در پنجره نقل‌وانتقالات ژانویه است.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/Futball180TV/107201" target="_blank">📅 20:35 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107200">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dc376d50be.mp4?token=hIN3OVv0QfwUNLiyVFWSUFKu0v5pkKfNzi5ydZDSEuMlwZFItCrENVA0hp2FyF3Q0aAhLFCXrnqWYV1H4ub0gaRIOs4RQpOLjW5ofqrYgUimy1gwkOCns8nKJX6wsUkwmTGuirj-oEdPenpTmPoU1MK6HP1A-aRqwRVWCAXMWrdCV0jDlPdht8Os1nxIQUWOZ33saYoBmn5jq3TISQKM3VNgjzdu4DyNak_G_-HXwkeWTN3QBZ-YFLNIvMJFfiKj89JKipiAJvewfzsQmBxYK46uqqbdh8Crr3PgPf4cqTcw_hhwBpO6qV-WLw74yErZRDE1I4dzWgJ9bFquAJ9SK2VAoTWauNErEtnYp36OIuiboEQBFgN6kac2gJCqg3ryBP8pxzwhQu8BfHKdNoMX8mNhJm20wll1AXK_MtkTVoMlAiG3lwKjjK9YeVuirw02ZJfLZMn4MG4SrX_9YKxRvQ-CDXYAkfw393aQlvhYHWylEZxLRaG8zpG4gsDnoZcwnEYj9i4NBxMmgp9s2AxMzKq-ZO5VHFSPYVOUh8B7eyFoS8RbOxOmKza3ezlQY68XYWeCOUwwNKe2LLVn2ajKt50sa-bmclTsB53VusP3qyyM9Zi_lKNFuBBHwbrmXV2htTXa35ouMyF_ZQ_Vr1aZPTGxlpM6gaFaPzH6TlT-b-Y" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dc376d50be.mp4?token=hIN3OVv0QfwUNLiyVFWSUFKu0v5pkKfNzi5ydZDSEuMlwZFItCrENVA0hp2FyF3Q0aAhLFCXrnqWYV1H4ub0gaRIOs4RQpOLjW5ofqrYgUimy1gwkOCns8nKJX6wsUkwmTGuirj-oEdPenpTmPoU1MK6HP1A-aRqwRVWCAXMWrdCV0jDlPdht8Os1nxIQUWOZ33saYoBmn5jq3TISQKM3VNgjzdu4DyNak_G_-HXwkeWTN3QBZ-YFLNIvMJFfiKj89JKipiAJvewfzsQmBxYK46uqqbdh8Crr3PgPf4cqTcw_hhwBpO6qV-WLw74yErZRDE1I4dzWgJ9bFquAJ9SK2VAoTWauNErEtnYp36OIuiboEQBFgN6kac2gJCqg3ryBP8pxzwhQu8BfHKdNoMX8mNhJm20wll1AXK_MtkTVoMlAiG3lwKjjK9YeVuirw02ZJfLZMn4MG4SrX_9YKxRvQ-CDXYAkfw393aQlvhYHWylEZxLRaG8zpG4gsDnoZcwnEYj9i4NBxMmgp9s2AxMzKq-ZO5VHFSPYVOUh8B7eyFoS8RbOxOmKza3ezlQY68XYWeCOUwwNKe2LLVn2ajKt50sa-bmclTsB53VusP3qyyM9Zi_lKNFuBBHwbrmXV2htTXa35ouMyF_ZQ_Vr1aZPTGxlpM6gaFaPzH6TlT-b-Y" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🎙
خیابانی: تیم‌ملی با امیر قلعه‌نویی تا دلتان بخواهد به تیم ازبکستان باخته
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/Futball180TV/107200" target="_blank">📅 20:10 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107199">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/89362fa6a8.mp4?token=cWeuh0AbaEpM_w8pi7x5P_zrbadoyaRmzXo30zAool_YzvFXOk1Ht9LhgHSNbR9XydVzzH52p2VFQostEmPFb6Swfql-cPocAAij4vgMXpdhD1NG2F8UbuX47pc7rBzhR7PxfwRQYQY8pL_QzvSSpeuya0-WL85sh0bvE-NWtby2HWsRwDQ7dTI9g_AX8jg0o0puoZLrX8HXp6tV_lm2NgODGUe_ukx5MoU5_Hfbm3fvNgdxYNJkGT3h34vil8p-imrfIcDfgtzy66VXhLDPhMC09pyd3iobm2MqO4Z5Bd-TiR8WTig2cMcRM8OV2K09_5UDVIqBvEu8_mM5wehNEQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/89362fa6a8.mp4?token=cWeuh0AbaEpM_w8pi7x5P_zrbadoyaRmzXo30zAool_YzvFXOk1Ht9LhgHSNbR9XydVzzH52p2VFQostEmPFb6Swfql-cPocAAij4vgMXpdhD1NG2F8UbuX47pc7rBzhR7PxfwRQYQY8pL_QzvSSpeuya0-WL85sh0bvE-NWtby2HWsRwDQ7dTI9g_AX8jg0o0puoZLrX8HXp6tV_lm2NgODGUe_ukx5MoU5_Hfbm3fvNgdxYNJkGT3h34vil8p-imrfIcDfgtzy66VXhLDPhMC09pyd3iobm2MqO4Z5Bd-TiR8WTig2cMcRM8OV2K09_5UDVIqBvEu8_mM5wehNEQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
انتقادات تند جواد خیایانی از بازیکنان تیم ملی امید
: برای کره نه مدل مو مهم بود نه قیافه. بازیکنان میلیاردی دو زار بازی نکردند!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/Futball180TV/107199" target="_blank">📅 19:53 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107198">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EJWm8WPFuIhA4mPPd1WHKJa6WjU89AX9WGeeXOUzABbvTZJ4e9XeyiZCy-UIHQcmB4OXxlb6bzQK8cn4tCYUkzHENM19m3W0hshsiq0MQpdxk4AhapSExz3knLwT46rsU5ssFQlkBJeb85VvYd169Aw9LvJlsfd4JGLmz7ktwE_5E8z1RfOfVesIw6peNMCPo3k-JX_UgebkEkEprTa4-4o2s_F6BCA-ypVzQUz150Py3bg0dgErUgamt5JnCfmFeJbEus0BBV0NPqmeCU7LrTALm5wLrWlkWRR4MEVDf66_f1chD2HoFONwe0UhefAH-yGdariBneVzMjKRNOC-6w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
🚑
رئال‌مادرید اعلام کرد که ابراهیم کوناته دچار مصدومیت شده و مدتی از میادین دور خواهد بود. به گزارش برخی منابع، این بازیکن به دیدار ۱۰ اکتبر مقابل ویارئال خواهد رسید
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/Futball180TV/107198" target="_blank">📅 19:41 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107197">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0cb36555e1.mp4?token=AU_QrK2UY4JGfu5FknhdbhOoGW7qExvdVVM2acv9CRbGYrdbrV4EValWjPRyw9JS7LCbVmBXUbipsrwAL05SRjpUi3rl9swBkQ7ZdQxWlB0SBQ87GDH-HKCRaa5oZ0KBOGs9cD9G9fPb2QVAJjzx3mOQJZGYZVIeEU6r2Xsg9v8VisvnUVqF8G0abL1qAm_lutckezcmMfSzMis9NfzHRvXzW4wFOMZofbraglemaSAtIEGpOI2TQmHrTN4rug8F5TTRwAkUT1hu8_3uw0zqnw1AP2v9lxkkk8B572hUdQczVkssYxYHT4iWTUFC7Z6q-crgcqSmHRU9UgoVNNoqQ5QcOf4V5JCuN1HBERtoZ9HB5beKBpZ3bioas786AEhkSKkN5gXe25GIm18SNV5vlyPFYYFWQx4eqQib_WCH-tnROX7C106XVZSGBkBQCHuJJ31s-Pqx-Me8XZI8_qC8SR0LFGMZJ8uXquvzloyReGULsO6BhIPaBowJJwOn0yS3X_zUdi-935odeyZGvURNE1CLVnDrsTH-gBOSqZPzF0ajBUwEw2MTU9XQqemNpgTI9thd6kOlguv-bkqW44HkrqxJEKgn8ERqlflYbrtJDr3PpN9LLN16dlhtHeLb0lJ_4GNwPUxtb95wqAzCwdAWkQ78sCPnx1T3EzrC_hkaK8I" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0cb36555e1.mp4?token=AU_QrK2UY4JGfu5FknhdbhOoGW7qExvdVVM2acv9CRbGYrdbrV4EValWjPRyw9JS7LCbVmBXUbipsrwAL05SRjpUi3rl9swBkQ7ZdQxWlB0SBQ87GDH-HKCRaa5oZ0KBOGs9cD9G9fPb2QVAJjzx3mOQJZGYZVIeEU6r2Xsg9v8VisvnUVqF8G0abL1qAm_lutckezcmMfSzMis9NfzHRvXzW4wFOMZofbraglemaSAtIEGpOI2TQmHrTN4rug8F5TTRwAkUT1hu8_3uw0zqnw1AP2v9lxkkk8B572hUdQczVkssYxYHT4iWTUFC7Z6q-crgcqSmHRU9UgoVNNoqQ5QcOf4V5JCuN1HBERtoZ9HB5beKBpZ3bioas786AEhkSKkN5gXe25GIm18SNV5vlyPFYYFWQx4eqQib_WCH-tnROX7C106XVZSGBkBQCHuJJ31s-Pqx-Me8XZI8_qC8SR0LFGMZJ8uXquvzloyReGULsO6BhIPaBowJJwOn0yS3X_zUdi-935odeyZGvURNE1CLVnDrsTH-gBOSqZPzF0ajBUwEw2MTU9XQqemNpgTI9thd6kOlguv-bkqW44HkrqxJEKgn8ERqlflYbrtJDr3PpN9LLN16dlhtHeLb0lJ_4GNwPUxtb95wqAzCwdAWkQ78sCPnx1T3EzrC_hkaK8I" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
حمله تند خیابانی به فدراسیون: باید چه کار کرد که کادرفنی تغییر کند؟ نتیجه افتضاحی برابر ازبکستان بود. آقای قلعه‌نویی نمی‌توانید تیم را جمع کنید
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/Futball180TV/107197" target="_blank">📅 19:38 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107196">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MJJ5e6yfiOaWJd-n3Dn7xw55pf127egponiXOFSrIPgxGMJXs9LypYvXycHR7F-ifYMfGju4NVejEIxpW4XVlUyOnX-Li6Q_LCFsvAXGH8w7qIQvUjriwTdJu1e3xSSNzOLDDzO62vvDgZnpv6JSuhyK5QPHyKEMCqzpMHqTjXauECjgWxlRMq0M65oYvWNR0RSkIi_0W4QdrtrguY_TTbpHrHULoLC14f39IeihmGB5om4wC4Y95xcIgXkRg0acPO7cSq8wCdY6Gcj0Xe7AtIaJeta3ILRVj0l4Cb99URJIzw1N3hnzhBsMpuWzR7BtqD94KcVuS_mo5UusMBwhCA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
❌
پایان‌بازی دوستانه؛ به پیرمردها امیدی نداشته باشید؛ قلعه‌نویی با دستمزد ۱۵ میلیاردی پیش به سوی یک جام‌ملت‌های تاریخی می‌رود!
🇮🇷
ایران
1️⃣
-
3️⃣
ازبکستان
🇺🇿
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/Futball180TV/107196" target="_blank">📅 19:35 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107195">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qheM3tFtsc1oraBBnfdJD6eOPjPskBA2TQnBMfGwVUz-Lu2tqwlkf7QOngr20DnGVAcJvy7SgdulHCBA9GDx49gN76bMCW52via1TBCRmIOvg2V1PC7nYCktlPRjWihqQm_mDCbM4ttOMjwIp65vxc5Ui5dEjET9lnL4n1pFA7tnks8PJZqbMUTjkaXP3oB2xmR807q2fZ2hTxpM_KHu3E-Q6LEjVWkKEBvthm44aBMKLy3nzP0FocdBg8DkVe0nOHwYqTm08zMTJBiPE32h5QeeKO69aSIMxM8mWK7RXz1LXhhEeXT0ynUl1_kBqyoo29I4rqGhuf50xYK7QxZGyA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
‼️
گل سوم ازبکستان به ایران
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/Futball180TV/107195" target="_blank">📅 19:28 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107194">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c533284b0a.mp4?token=MeCpWK7SBPD1RgsiR3Z0bztSHbnDA-nvg_obJGeYGTQxLUfmcY3U9WWol7m5fX_yFPy8n8PVafOF5ykNtTRs_GWOCNi_Yj4Rm2_b19gLR0Yp4bKn4S_m4g1t6smx3B7pDEfgGdLH25fp72E-bIcklo7q44asC6dPK9o6EwCDEzTe3_rsiNA6PDUTVKwfb4mPrWNl2-RUNiBY6B9op7AAcO1bNTZW2s8-CdSP6aKtMT1Apz1JYyqJJ_81vldrMcHomxc-TRlBC0Z3g5iAw5Q-OQieYOLG0nA2iJZA94umGYS2sjhp0kBA1kRWjpQLtqIU2HMYFOzHy5bNu6YM8Kc2yQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c533284b0a.mp4?token=MeCpWK7SBPD1RgsiR3Z0bztSHbnDA-nvg_obJGeYGTQxLUfmcY3U9WWol7m5fX_yFPy8n8PVafOF5ykNtTRs_GWOCNi_Yj4Rm2_b19gLR0Yp4bKn4S_m4g1t6smx3B7pDEfgGdLH25fp72E-bIcklo7q44asC6dPK9o6EwCDEzTe3_rsiNA6PDUTVKwfb4mPrWNl2-RUNiBY6B9op7AAcO1bNTZW2s8-CdSP6aKtMT1Apz1JYyqJJ_81vldrMcHomxc-TRlBC0Z3g5iAw5Q-OQieYOLG0nA2iJZA94umGYS2sjhp0kBA1kRWjpQLtqIU2HMYFOzHy5bNu6YM8Kc2yQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
گل سوم ازبکستان به ایران
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/Futball180TV/107194" target="_blank">📅 19:25 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107193">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5cf2bcda94.mp4?token=doxN8E4Z2SkOsb7MZpqqdkjhH6AXLNINDRzeB7owb2YM1LFO2ZociegwYzhj6JDL_VfgdJ8YPB8CLATbLfqsDpkYni0ZrM2OmUWPj-D3hSCaeYEcXmjyGva-gtSPTnpbSVRcaVEGG3Ww3EKAHc87gyrJa_wzTPItCWFjMnEPwJYHX5sKcf2BrlS16GkGZRxR6H7zhGd8lLTQFxPUDB2VuPcbSOZvgfXjgFZ5oEFc6dhvHbtE9cDwP3EJ5ump921umqHZ9ZkB-wCz81CVXHWf0a4dzthFKQr0Z5MLzQITJGL2C1bfptBfGDQSD_SxiZ7Bf8hWUNapu8wU22ffNLJO1g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5cf2bcda94.mp4?token=doxN8E4Z2SkOsb7MZpqqdkjhH6AXLNINDRzeB7owb2YM1LFO2ZociegwYzhj6JDL_VfgdJ8YPB8CLATbLfqsDpkYni0ZrM2OmUWPj-D3hSCaeYEcXmjyGva-gtSPTnpbSVRcaVEGG3Ww3EKAHc87gyrJa_wzTPItCWFjMnEPwJYHX5sKcf2BrlS16GkGZRxR6H7zhGd8lLTQFxPUDB2VuPcbSOZvgfXjgFZ5oEFc6dhvHbtE9cDwP3EJ5ump921umqHZ9ZkB-wCz81CVXHWf0a4dzthFKQr0Z5MLzQITJGL2C1bfptBfGDQSD_SxiZ7Bf8hWUNapu8wU22ffNLJO1g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
گل‌دوم تیم‌ملی ازبکستان مقابل ایران
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/Futball180TV/107193" target="_blank">📅 18:49 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107192">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fb2cea4974.mp4?token=kqZzDezPZCpGUT7wC_hdifFz5f65_RkQHl91BcXmsqpz2-pB6rtlxGHsKBfFO30tfDeA_yhwuMLeCYfiwK6y-4WfbMnvQF4-0tersK6X3ClLyCKg35Xegu0U_gggaxdACSh8zk4htH0rU4iLBOVirOWjPO51eF13oZRyLPsHqYAshEpo9Sydjar16fqmhMgwsOcGJnejEv74AkZpE3cMtbWRMGN18I45dx-Fjhf0Ryh8qC9lYu0lY7RYk7lUIrubOwyP-Vbwl4w9BCsMPwhpfts3q9rOh4oNcAov4gUXF2x1V80T_k7Wle6cyrvMqtysWFUVmyZwUUmrVyfC6Xxthw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fb2cea4974.mp4?token=kqZzDezPZCpGUT7wC_hdifFz5f65_RkQHl91BcXmsqpz2-pB6rtlxGHsKBfFO30tfDeA_yhwuMLeCYfiwK6y-4WfbMnvQF4-0tersK6X3ClLyCKg35Xegu0U_gggaxdACSh8zk4htH0rU4iLBOVirOWjPO51eF13oZRyLPsHqYAshEpo9Sydjar16fqmhMgwsOcGJnejEv74AkZpE3cMtbWRMGN18I45dx-Fjhf0Ryh8qC9lYu0lY7RYk7lUIrubOwyP-Vbwl4w9BCsMPwhpfts3q9rOh4oNcAov4gUXF2x1V80T_k7Wle6cyrvMqtysWFUVmyZwUUmrVyfC6Xxthw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
لحظه اعلام پنالتی برای ازبکستان
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/Futball180TV/107192" target="_blank">📅 18:49 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107191">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/592ed07452.mp4?token=qdIQ-JHTWNnedxu9-ENa6Mi6U6DEVEXCrofHvNE_YZnw1sUmmy2GHQ3QyjntYhv_u8AMU32FKnHf39y4XUban8VL_yte7VbInc_D3DKdu9n3yeEI_FKko15Y97cuLrhOl8YLqsvOE-8ck6PSiZ64SdYe8YfyR4yTrb8Lbno6dgEdTBKG7OpbILx4Og62yk6F4rRi6yZENRUgUZkaqju8x4huzHtJKYan_h8lUyHdcrI-uuaKzlElmdUkzpFpmsKd0RmeajrlCEreutQ9NKKRb30OzLw89iHPk4KHYWMzKa-Kgq-AcLMixh3CSakT4rAr_e8ROTcJq5MWBw_6f49QDw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/592ed07452.mp4?token=qdIQ-JHTWNnedxu9-ENa6Mi6U6DEVEXCrofHvNE_YZnw1sUmmy2GHQ3QyjntYhv_u8AMU32FKnHf39y4XUban8VL_yte7VbInc_D3DKdu9n3yeEI_FKko15Y97cuLrhOl8YLqsvOE-8ck6PSiZ64SdYe8YfyR4yTrb8Lbno6dgEdTBKG7OpbILx4Og62yk6F4rRi6yZENRUgUZkaqju8x4huzHtJKYan_h8lUyHdcrI-uuaKzlElmdUkzpFpmsKd0RmeajrlCEreutQ9NKKRb30OzLw89iHPk4KHYWMzKa-Kgq-AcLMixh3CSakT4rAr_e8ROTcJq5MWBw_6f49QDw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✔️
گل اول ایران توسط رامین رضاییان(49)
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/Futball180TV/107191" target="_blank">📅 18:42 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107190">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CMSNekmPkNe9-cbkgvG3unDZu78KWxMZwNrD3SrWlhgujXfpV_x8XWV28i2PPFSQ3opgU_IoNRVamPUcIj5uLyRCf0waTCM7eqZ7lfOGaPsUha3VnHVFecrpKTKn1ya4mOaY-nCbLIm7XrWBuKQsbv6TJvgbn-RbZtDUsoPEPuHWs4eCYMB0nxT67Cvwr6HKRGV_oIdb0Xz1cT6OeYmbm6b_Tv3r7MkqOhYNTmTf5zO1jrg-euF7LZyKzIG0Yec6kRWSLUufzUZxenc8Uva5A52KKcPRUqNqq4HiJqJTrvuTSDtp6mtr191ZTgPI07QWLZNDv77yib3O7ptR7zmdIA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تا روز ششم مسابقات آسیایی ناگویا کشور چین تونسته ۱۳۰ تا مدال بگیره که ۸۰ تاش طلا بوده
😐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/Futball180TV/107190" target="_blank">📅 18:33 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107189">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GyI124zXF8Li1Dua_RRfEq2fFamnI9dHxvXHCEOCjI5qKywx7FM5Rsq9UtN4orWkh0_jfOnSWrUYPoien2td0aUw-1HKDKp4J4BtveNaQTQcuM8U_5TyCOY_Tz_ENzfYfqkcGHsclyELnp4ekgcl3UqwcMMnq6HfHh0_vmbYO0VvJ0EcCEnoRlk4W7oZZBORQ4DUPvhlsyzxVkgxD4r_-O1sDljZh7Aq3mYAdk7kHp9YSv5-Tkm9ONakKoVKpv5Dq6nWMm2k9WOozZBTSZj4D0K5iIcWHRBrvGnpkKgsAnIGvkiVPMJe9gLw1ckG0l7TANt54B_qWwPPCA51yDrpZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
🙂
واکنش یوز ایرانی وقتی می‌بینه اسمش رو به این قرمزایی که تو زمین هستن لقب دادن
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/Futball180TV/107189" target="_blank">📅 18:21 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107188">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tcXO0cNLq9J6kap95FfVwizrfUIGBlhluSFO5hoROmrykNY6njlf3NgpVl-pwH5aPzn_CXMT2uJk4X2D5h27rGCrhBsR8k49PlExU_4ocGYojCVEbE9YqKkWL3cGVxfP7TTblq0Ch-1lISUxt9SVjH3dzAowMJWn8BKN4Ost2ZLyHWKVLmqZ9-V83BOpcb9XSYy7Il2IWLpRT8xCxbvOj57oeXRbTXOtarNi-YcpuYh7SnsYZtPIK2oR7bZlgWqA-nS85lUZbbJg2YVlOzrthWqDv-_DnGu7ypODY6ITI1K10DBFVt_GpqoXyX-Niy_eHmE6WelTdIVhVz27MumhOQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
⚠️
فلسطین برای ادای احترام به تیم قلعه‌نویی در دیداری دوستانه با نیوزیلند دو-دو مساوی کرد تا یاد و خاطره جام‌جهانی برای ایران زنده شود
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/Futball180TV/107188" target="_blank">📅 18:17 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107187">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sz0reSK_lgKex5d6ORxyBXlSRlq4ZXaP_0O3Aeg4wSZlRp_0Dyk9iLfV35JKt8yA9DJJgdU94VjTO8N_wRHrj8RG5RFvYerMAZNrpenNWFwJIPuMEHzF1o5fw0cEi_4Sw7m-fFDgxqocumdyGS-1l33Xvn1DOtBMbsr-HzZdxbolZGGlO_aKlt8Hn7SjQkhyJhKAqO8nRXmFnjdoESc7ykGQ15MQEI0E17os5aYFWOfV3w5fHFuItZtpJi1VuiFi1GQPk5dha2Ej2AOX21RFhbHC1SyPbOJV7clSyFNLmSis1-Xwwnwi8EWnSpV7z4UBuCHECSZP4DPaWLIFkPNVRA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇧🇷
ترکیب احتمالی برزیل مقابل استرالیا که بالاخره احتمالا شاهد حضور اندریک خواهیم بود
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/Futball180TV/107187" target="_blank">📅 18:16 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107186">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Oec8up3Yqmm2UjhSsLIFZcqSVwZyeAaFT6hbGCVUNkU1tU8l4c943c65HJMHapk1hd61DnBdcLBbnNR8loiZzUa9cCdWM5nuEk1efOTbdQkbC31IsoyVseNrHQHYyhm0Uwtb3mTxZCyr3gGYz1TvK9_jojWpDw9ptWBHaLUTthFf-KWU8SrK-U2I0AOsNqYu-Kopveb-MziB8DQs5zbrvP_lSZWy35RTeendvGweTZNgMcq7ZvyUkqYLEJWqRDVOZfu5jNyd1pfVzA5GMo5xg2rjupCKwHLXeT5rRRLzm8m0Lb-ra0UsTiy7lbJP7MKePnyOQt-atzDkJgd-EMo91Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏆
لامین‌یامال: درحال‌حاضر در فوتبال اروپا هیچکس شبیه من فوتبال بازی نمی‌کنه و همین تمایز اصلی باعث میشه که خودم رو مستحق توپ‌طلا ببینم. البته لیونل‌مسی همواره در سطح فوق‌العاده‌ای بازی میکنه‌ و باید احترام زیادی براش گذاشت
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/Futball180TV/107186" target="_blank">📅 17:56 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107185">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9718ff60b3.mp4?token=erwGyEPwfkPMrttG0rIrJX_4WzKg12ORTXrZ2H2fusBwCxdmKSxE6BD4UBG3ThJRJpLeluQ1gNIxMUSOTVUGo6vkJfYJZ6QR_XIBXwqcjGnNi6mKDwhkkOyryGM-t8RXDhjPPE8OoJceA_FdWkidoLmUE__PpOBQ7omslXJGUXhLI7KguT1FaUx8RCIMrmO2CZzDjPfsdmb_rOfSgPwK1JG0C4_qIBPPvb-j4X1vk-X_f_ZAt4tOI243WRBBzI-6OIjggpuxDHAVLe1qmKfmLYU3-8qWxFG4peQWA55LlCuhql7oVqLGE2FVjcn6tE-r1JEH0m-Ae71JXKZ9GLsVtg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9718ff60b3.mp4?token=erwGyEPwfkPMrttG0rIrJX_4WzKg12ORTXrZ2H2fusBwCxdmKSxE6BD4UBG3ThJRJpLeluQ1gNIxMUSOTVUGo6vkJfYJZ6QR_XIBXwqcjGnNi6mKDwhkkOyryGM-t8RXDhjPPE8OoJceA_FdWkidoLmUE__PpOBQ7omslXJGUXhLI7KguT1FaUx8RCIMrmO2CZzDjPfsdmb_rOfSgPwK1JG0C4_qIBPPvb-j4X1vk-X_f_ZAt4tOI243WRBBzI-6OIjggpuxDHAVLe1qmKfmLYU3-8qWxFG4peQWA55LlCuhql7oVqLGE2FVjcn6tE-r1JEH0m-Ae71JXKZ9GLsVtg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
اشتباه عجیب از حاج‌صفی؛
گل اول ازبکستان به ایران توسط شاه‌مرادف
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/Futball180TV/107185" target="_blank">📅 17:47 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107184">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/Futball180TV/107184" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/Futball180TV/107184" target="_blank">📅 17:47 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107183">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/egh-fpgP70qDOg-bmO4N5oEnOGUc589W9QOW9Zylnxlu_PyRvF7xvTUETBoPhC5751j-WmXav6ufKnx9MPfY1nFKUm2_4sIRoSTLa6jkwVY72cKB848ncusUnW_Z9qgLJABSZhELXuC60Aj_YhjzTKTza87slEMLQm5uuPl95XbKqj9xHYETaHS0O840erOz8D8UkEXpPHS3zdhqyPUIweZXihWlfHaiywGi5QmYJqBeLJwlyDxiau2lRVd32IuzOyXu2J8ldBMES7A_DYfBqHdaJojf-GdnPOWaUc3UNwcX07H6NnZCYbZ5JujJfaJnEGCvfDKj3qRkSpMooE3GQQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🤩
نبرد هیجان انگیز
ولز
🆚
پرتغال
را در
TrexBet
پیش بینی کنید!
📉
نگاهی به آمار ۵ بازی اخیر دو تیم:
ولز: ۱ برد، ۳ تساوی، ۱ شکست و ۱۱ گل زده
پرتغال: ۲ برد، ۲ تساوی، ۱ شکست و ۸ کل زده
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
<div class="tg-footer">👁️ 17K · <a href="https://t.me/Futball180TV/107183" target="_blank">📅 17:47 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107182">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Krh2e-fZ5BL7qIERJpMxLFX8QFAJFoHykkOhMLy4VbqVtavRiGgwN-CSIu4RHKfutIOPYv6UaojMlJbZ_8H5kcSb828ZssW8Vf0c4Y5F74StIPTSVTdbIyocPaxGJVmAAwUTTbzvudHmDYDs0YtTxKLGw5zL-uj-G0_QjqQXQoIHGUB9t0s40EeBTLXJRGU_C3boMdyqI5PGqzKqaBWzDBxEBMVXs6kIicfM1E8xcTQW5K7J11u9vwtLcSCJyuhvmD_xsaDk4IkKgjsZbhVqZnAzREPiu4TLFgxKIY7PDRBDVQxJb8YJvYR0-mph0ofD7ZTl5S0yuOnhx6LL4Nv7-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✔️
بازی دوستانه؛
ترکیب ایران مقابل ازبکستان
علیرضا بیرانوند، سامان فلاح، علی نعمتی، صالح حردانی، احسان حاج‌صفی، سعید عزت‌اللهی، امید نورافکن، محمدمهدی محبی، آریا یوسفی، مهدی طارمی و دنیس اکرت آینسا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/Futball180TV/107182" target="_blank">📅 17:13 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107181">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6be9bc4836.mp4?token=RAkxAV0OlbBHiPzthZBPKgL1RcB5NHbmp5GCl3yTzokR_8a3RLC2mmI1dY9R8xCsdJDvrXp6jC64zDusLgXDolAhLpOVtpfCfwIb5JVHuNvGS8U57GB_HpCFnZ1vNQ9WRnhL_VNHbpVYGRmoTWDiprLBXLodG690V7HuXHGlpoLTDu6GYpbsnRtueK2W550IL-Aw8aj2CfM_fgG69cQV-JHQ7c13YiAgiz29Qq91K5hG-g-sbf_kHnwMA5G7oTVwoDJRsKFh4FvwhXst7yuvj0tTTkIXJTCEhIkUPBjoCFCnltPcrhuAqSg3gsBWjUBOSVepaikznTCXPWnqaqwtCA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6be9bc4836.mp4?token=RAkxAV0OlbBHiPzthZBPKgL1RcB5NHbmp5GCl3yTzokR_8a3RLC2mmI1dY9R8xCsdJDvrXp6jC64zDusLgXDolAhLpOVtpfCfwIb5JVHuNvGS8U57GB_HpCFnZ1vNQ9WRnhL_VNHbpVYGRmoTWDiprLBXLodG690V7HuXHGlpoLTDu6GYpbsnRtueK2W550IL-Aw8aj2CfM_fgG69cQV-JHQ7c13YiAgiz29Qq91K5hG-g-sbf_kHnwMA5G7oTVwoDJRsKFh4FvwhXst7yuvj0tTTkIXJTCEhIkUPBjoCFCnltPcrhuAqSg3gsBWjUBOSVepaikznTCXPWnqaqwtCA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
سوال‌کنایه‌آمیز خبرنگار ازبکستانی از قلعه‌نویی بابت عملکرد ایران در جام‌جهانی!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/Futball180TV/107181" target="_blank">📅 16:05 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107180">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e8a2786f81.mp4?token=YYIuAVVIkz1otjHHlQThVbF-yhYXEFeeIobrzA-zB0JtB6SUht_d-SKkIefS1H5jgqxdPrbSJQnPfzgWPNYKTiReGEB6eQjYpjbZjcJdnfoOjnCtwGL6VZUhQrvDGsPy1o-PSJFUQtu3ygElv8ZdcYzXcSV38DiOKxluDPXYJDgHr2wauhtepMIal_fRxnDcxOwyZGO-PYbb9J2980nc-ZEAGIBL0Z8O17_MZ5DJkq57UuQZu5lvMrb6EUMyuytSWxXO85D-tNjUlkB8iBLuUfxAETde7XGoSkutkYtEAIQ-te9nhS1CivQygrhG-PEWalP76Ry9zmt3nR6eaEKK8A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e8a2786f81.mp4?token=YYIuAVVIkz1otjHHlQThVbF-yhYXEFeeIobrzA-zB0JtB6SUht_d-SKkIefS1H5jgqxdPrbSJQnPfzgWPNYKTiReGEB6eQjYpjbZjcJdnfoOjnCtwGL6VZUhQrvDGsPy1o-PSJFUQtu3ygElv8ZdcYzXcSV38DiOKxluDPXYJDgHr2wauhtepMIal_fRxnDcxOwyZGO-PYbb9J2980nc-ZEAGIBL0Z8O17_MZ5DJkq57UuQZu5lvMrb6EUMyuytSWxXO85D-tNjUlkB8iBLuUfxAETde7XGoSkutkYtEAIQ-te9nhS1CivQygrhG-PEWalP76Ry9zmt3nR6eaEKK8A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👏
🔥
🔥
صحنه‌جالب از بازی کبدی دیروز بانوان ایران مقابل هند که واقعا محشر بود
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/Futball180TV/107180" target="_blank">📅 15:40 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107179">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/I938QnJcI5LNbBVz7vb8OO8ZSMsqkumQBBw5dP47-Z9-8A_eKzwQ7Hjf5YaolsWi9Z9nrCbSQ2lsbLSvTDk4KlreskOlMfVwkdDD1WQwP7ZVLj5lEMrGnbnGIKfJUeCRxYEN4Xxe3F26yV-hKS3MOIwKVJHNE7C1eIIqyKWFVLM_TgmulhcwCg7PPukO3GL7_JSEAMd4sbsUjzG8Pybl9kbeZO-T5h-YGv_k7HWAbSCQ-Wu9JX1OLvfGIvHYdYaF54CbncHoWjKE182cbl0i6ZafQdpN4f4jRogE_J7pCcZXbbJqc3EA9Ch1xBz-UbBWCHLbXKAwRm4oVaNMCw4cqQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
📱
استوری امیرحسین قیاسی درباره لیست جدید قلعه‌نویی و عدم دعوت از مهدی‌قایدی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/Futball180TV/107179" target="_blank">📅 15:29 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107178">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">🌟
مروری کنیم بر ادن‌هازارد نسخه جام‌جهانی ۲۰۱۸
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/Futball180TV/107178" target="_blank">📅 15:15 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107177">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/773eb10873.mp4?token=RCWz9YGVFQHP59LQ0CuhBQHOK_hEMpXJ5IxnGDh_TVXtEAJ0GsgPqslKOXq6ReVcg1MeiN2ZFEF4_MmJ_Jb4Us675B3wH00L8qvSmNyF0QOR01GhYpXtwL_MgCeQ6zhbdwXUZbVZ8MpeSnJi6c0L4G6Mq0mlPSEWWk9BVT_Mf-QFCRVk4ZxM4zbAKAr1wP_JJTPf0WZllepLLf7cTQR9GG41xVP1jWF1z-6h_Rqjbxa2I6uhtS9yN5iNTBUs7YKYtAm_CBFs6usrKsKicJEhSTjk88sXoxDanUC4vv3wUIh2AokXK87AK_0CuiySsbAdSNV9YhWKfzR_CsL7Ie5PcVEDV9KiKRPFiBavcHRVCTalKBMJJWGjj3nCfpV9uNOS0z1ONWz5ayy1CRCSAKW1JgG-TQdnsZacClMYOLcRx6o2bsP2pXZpmD_So9Ed_0YsPHAQHpOAB2WC_eLXZWV1sqFGoGyUu_WdNIuZBDU1x4ir0IbijQGu-ccj9cAcbFqZT5Mw0gYMm93HpRrqtfQlf3wbh7usKGx6gTWJTeWH52hOPzn4-rUguIEie-Ot_7OVnUNiBmx4quQLNs7dUgAnb-IkdhE456aRuS8bDGvOoWHzDnvJrvoyXBl9NsLzt3Qn1tcrp7MfrlIfg39gTBjeN67u-j5V_OGcQXLV6pqIM8s" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/773eb10873.mp4?token=RCWz9YGVFQHP59LQ0CuhBQHOK_hEMpXJ5IxnGDh_TVXtEAJ0GsgPqslKOXq6ReVcg1MeiN2ZFEF4_MmJ_Jb4Us675B3wH00L8qvSmNyF0QOR01GhYpXtwL_MgCeQ6zhbdwXUZbVZ8MpeSnJi6c0L4G6Mq0mlPSEWWk9BVT_Mf-QFCRVk4ZxM4zbAKAr1wP_JJTPf0WZllepLLf7cTQR9GG41xVP1jWF1z-6h_Rqjbxa2I6uhtS9yN5iNTBUs7YKYtAm_CBFs6usrKsKicJEhSTjk88sXoxDanUC4vv3wUIh2AokXK87AK_0CuiySsbAdSNV9YhWKfzR_CsL7Ie5PcVEDV9KiKRPFiBavcHRVCTalKBMJJWGjj3nCfpV9uNOS0z1ONWz5ayy1CRCSAKW1JgG-TQdnsZacClMYOLcRx6o2bsP2pXZpmD_So9Ed_0YsPHAQHpOAB2WC_eLXZWV1sqFGoGyUu_WdNIuZBDU1x4ir0IbijQGu-ccj9cAcbFqZT5Mw0gYMm93HpRrqtfQlf3wbh7usKGx6gTWJTeWH52hOPzn4-rUguIEie-Ot_7OVnUNiBmx4quQLNs7dUgAnb-IkdhE456aRuS8bDGvOoWHzDnvJrvoyXBl9NsLzt3Qn1tcrp7MfrlIfg39gTBjeN67u-j5V_OGcQXLV6pqIM8s" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
🎬
۵ پاس‌فوق‌العاده بیرون‌پا از لامین‌یامال
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/Futball180TV/107177" target="_blank">📅 14:50 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107176">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e78c32e4ce.mp4?token=BdE5wyFOIaRRX1REb56-kmUdA7cFe7g9zMjWUGAweKSIQpkwLKRUahzqblT3x3xja9XlyTWB5SHQvK10vogxZia3Oc_2J5Ezf40Ek1Ye6nhJUacOm-g9Ja5SqDih_IWbfTeJwlGYB2Dq6uarvMVEpGfnrrEffpoSSK820Qm9BuA29lHu_F2jLAvYlo4PtTpDdwep-YAj5x98yGQsxAEoQFR8bOx11p6hZt763srGmm1I2i8eWNNFOmbEm3OdMDrW514mj6146BkPOvVOKSe6I-Bp7pcC46XyGX1bSOb9HkyiGFOvR0sFoNwKsUBOCSPm3bX3gS0VhZLmpijagmv1dzzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e78c32e4ce.mp4?token=BdE5wyFOIaRRX1REb56-kmUdA7cFe7g9zMjWUGAweKSIQpkwLKRUahzqblT3x3xja9XlyTWB5SHQvK10vogxZia3Oc_2J5Ezf40Ek1Ye6nhJUacOm-g9Ja5SqDih_IWbfTeJwlGYB2Dq6uarvMVEpGfnrrEffpoSSK820Qm9BuA29lHu_F2jLAvYlo4PtTpDdwep-YAj5x98yGQsxAEoQFR8bOx11p6hZt763srGmm1I2i8eWNNFOmbEm3OdMDrW514mj6146BkPOvVOKSe6I-Bp7pcC46XyGX1bSOb9HkyiGFOvR0sFoNwKsUBOCSPm3bX3gS0VhZLmpijagmv1dzzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✔️
🐐
جوری که دیروز ژسوس سرمربی پرتغال از اسطوره فوتبال کریس‌رونالدو تعریف کرد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/Futball180TV/107176" target="_blank">📅 14:25 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107175">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mC-OndgsAgy4z2x4D2Sk_5pMFYmKXNd80GDsoW_Vk7UX7xX2uRGrcsM4fzaYYZC9g2re3QvpypwNB191dJKUQQJlDNDPbjMTQVxhBgsTj4YmK5KBES8u3r1MMsOs7jpQnPKdZCp2eKEq-xZRmFcHJEIBlC7gjfTvVbhAYOe8woycJTj98OwbsFA2RO5xTu_CN8Y-8UDZw1b7-3ZVEgE6BTl5HlHyYAMzIeAi5jy9UzPb6kMfalefgRoEs_xz0OTWp1FCNY9GWx0vmqV5_1eeuccmlPVJAiK8hw07q-acCXwbbRuc749fiBXRAFhIYorSyvT0qmHag5q0Brz4S6MASw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
✅
🤩
علیرضا فغانی از استرالیا و موعود بنیادی‌فر از ایران به عنوان داور در جام‌ملت‌های آسیا قضاوت خواهند کرد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/Futball180TV/107175" target="_blank">📅 14:06 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107174">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c7a03c344b.mp4?token=UUWTtj2gaYFLfDnd-VO1guAhqBVF82xRA-0lbllpdGzJoODpgtKsQF3fyOfQt_rwdMfsFGSsHq2lr61wl7Ox30kLGsblIOdDfkPlIOkuY40bB0rDOzKYGYYIQPH6HCwLc6Ge6DzhCH1hZ6eXoW_xW6gqOAGSxnQnLSISycIbTBPAGIgYYIDqwr6y1Dv_wdyzOXC7xA2IRS2l0bX7irLKxN8_m1j4fXB_g-LDTPHDGufRaLHkvaFnATGudBycuOjovbulqTr60fc1Pwa7vBeJW5ec9MWJhpWLoHFtdHtIstBy8hfXADQAKqW7QMBKaeDheScrPhj1o2hHMS1n2oMszg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c7a03c344b.mp4?token=UUWTtj2gaYFLfDnd-VO1guAhqBVF82xRA-0lbllpdGzJoODpgtKsQF3fyOfQt_rwdMfsFGSsHq2lr61wl7Ox30kLGsblIOdDfkPlIOkuY40bB0rDOzKYGYYIQPH6HCwLc6Ge6DzhCH1hZ6eXoW_xW6gqOAGSxnQnLSISycIbTBPAGIgYYIDqwr6y1Dv_wdyzOXC7xA2IRS2l0bX7irLKxN8_m1j4fXB_g-LDTPHDGufRaLHkvaFnATGudBycuOjovbulqTr60fc1Pwa7vBeJW5ec9MWJhpWLoHFtdHtIstBy8hfXADQAKqW7QMBKaeDheScrPhj1o2hHMS1n2oMszg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👀
شاید حق با پیمان یوسفی بوده باشه
❌
🎙
پیمان یوسفی پیش از شروع لیگ برتر در برنامه تلویزیونی خطاب به سخنگوی فدراسیون فوتبال: زمین و تماشاگر که ندارید، لیگ را پلی استیشنی برگزار کنید
🎮
دیروز: قهرمانی تاریخی پلی‌استیشن بازان ایران در آسیا و حذف تیم ملی امید از مرحله گروهی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/Futball180TV/107174" target="_blank">📅 14:02 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107173">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/383a3af1e5.mp4?token=WhEtiC3zirVFFDlcUOUZsWqEiYqAv9WJnbUonG-vGFAVJga_L4fcT9U20CBNTPbLWsEpHWQ1xmwpg8X-pL14zOt7rsB9Wf7xuXiewetjPQnst71jR7gqu7CVLKY2_--_4jJ3ZKKIl50wo92jftOsD_l92Qov1oERZfGuNybQ3V_Q8IbRujyb8Bvio3JVHVp8dZBp2n7GH0caGwb2bkJFJmbt9j7aVPyewPalHSHgEbftDXArTubSKqJ3jXN87sTlPVMR6z4iFTvTVLaey4mCkm_pugkx8hVo98WTFYVS2dsS666pjsZz9wgYJAJRjfhh7yYA2e9R_4btf7TK8OFM7DzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/383a3af1e5.mp4?token=WhEtiC3zirVFFDlcUOUZsWqEiYqAv9WJnbUonG-vGFAVJga_L4fcT9U20CBNTPbLWsEpHWQ1xmwpg8X-pL14zOt7rsB9Wf7xuXiewetjPQnst71jR7gqu7CVLKY2_--_4jJ3ZKKIl50wo92jftOsD_l92Qov1oERZfGuNybQ3V_Q8IbRujyb8Bvio3JVHVp8dZBp2n7GH0caGwb2bkJFJmbt9j7aVPyewPalHSHgEbftDXArTubSKqJ3jXN87sTlPVMR6z4iFTvTVLaey4mCkm_pugkx8hVo98WTFYVS2dsS666pjsZz9wgYJAJRjfhh7yYA2e9R_4btf7TK8OFM7DzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
صحبت های جنجالی هاشم بیگ زاده درباره ستارگان تیم امید ایران؛ از انتقال به پرسپولیس، ده میلیارد هم نصیب دانیال ایری نشده است
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/Futball180TV/107173" target="_blank">📅 13:33 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107172">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">🚨
⭕️
بازگشت پرواز تهران به تاجیکستان از مرز هوایی بدلیل آغاز رسمی محاصره هوایی  «پرواز هواپیمایی وارش» از تهران به «شهر دوشنبه»؛ پایتخت تاجیکستان؛ از مرزِ هوایی لغو شد و به فرودگاه خمینی بازگشت.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/Futball180TV/107172" target="_blank">📅 13:13 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107171">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e5bd37ffa3.mp4?token=XQ62VFcwGi81xUWrgZFTt-uYRYW89tRsmt6Dw3McGvzhpMbUdTOPpDm-NeezlSK0v3dbirrFVXvU7T0qq2_gaaDQjHPJT9o62b4YxRgO3xIDjN-AsYxfO8wE6AnEJe3UxvE8JgI4xh6hBt7pXjrAqGrVPSQuIK9lNo2X49-UUHuowDj0LpMhX7EtfHa9k1aKEnJhgBqKAh8Nwi2eHgtVEFGU4eIOpg1ILHNI-Qx3vRvdDiOne3iyQPwXfR2TkwR8jy1PALeAb5mrCAvHtUXeF5pRuzk_2eiY0cEB_AnRjColUAZ__4LrK1MkgVQmiR0x9R-jVJcCKsm39zAvQYG2mZhyatxhngQO2DcYDUATcYENnKNhKO2H_8DAXcQ5xCBSTEc6449DbYYG3upK2LNzkraMNpORhkof0MALVns1sNd-dl2RXoN47rPotKyhHpN_jUz2j5_STDVx-FQ8FWJZUu9Ohd88t6tYqbmZrEzFXaXgMFszf2POst6ZxyDarBTMScoz1toOB_nb2-fvyn6xlr8LGfdv4I1BLDW6XUSwh8_YprXK6iQnnbnCH4wElqJeKXNGp7Z5MyNC8mqhqbMo53i73e4JQnjUkb0Q_8GXEoflwKRoSDCmHocR-nL-asDC6PVkF4O73ESXlERODdK-5DVB4pEGaHHspe8hBghISZo" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e5bd37ffa3.mp4?token=XQ62VFcwGi81xUWrgZFTt-uYRYW89tRsmt6Dw3McGvzhpMbUdTOPpDm-NeezlSK0v3dbirrFVXvU7T0qq2_gaaDQjHPJT9o62b4YxRgO3xIDjN-AsYxfO8wE6AnEJe3UxvE8JgI4xh6hBt7pXjrAqGrVPSQuIK9lNo2X49-UUHuowDj0LpMhX7EtfHa9k1aKEnJhgBqKAh8Nwi2eHgtVEFGU4eIOpg1ILHNI-Qx3vRvdDiOne3iyQPwXfR2TkwR8jy1PALeAb5mrCAvHtUXeF5pRuzk_2eiY0cEB_AnRjColUAZ__4LrK1MkgVQmiR0x9R-jVJcCKsm39zAvQYG2mZhyatxhngQO2DcYDUATcYENnKNhKO2H_8DAXcQ5xCBSTEc6449DbYYG3upK2LNzkraMNpORhkof0MALVns1sNd-dl2RXoN47rPotKyhHpN_jUz2j5_STDVx-FQ8FWJZUu9Ohd88t6tYqbmZrEzFXaXgMFszf2POst6ZxyDarBTMScoz1toOB_nb2-fvyn6xlr8LGfdv4I1BLDW6XUSwh8_YprXK6iQnnbnCH4wElqJeKXNGp7Z5MyNC8mqhqbMo53i73e4JQnjUkb0Q_8GXEoflwKRoSDCmHocR-nL-asDC6PVkF4O73ESXlERODdK-5DVB4pEGaHHspe8hBghISZo" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
⭕️
بازگشت پرواز تهران به تاجیکستان از مرز هوایی بدلیل آغاز رسمی محاصره هوایی
«پرواز هواپیمایی وارش» از تهران به «شهر دوشنبه»؛ پایتخت تاجیکستان؛ از مرزِ هوایی لغو شد و به فرودگاه خمینی بازگشت.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/Futball180TV/107171" target="_blank">📅 13:07 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107170">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1178f7a6a1.mp4?token=LCkGZwuDT13nQQRLZn9u0P_lEHabodhvRKe_u_LEf2VHlcQO4FRUe8ugIAufIzsbDrxx2NiDoIbk8VXYHcYQHV-i6ArVzn2v4ME1tdPzM4nNkQ6bjo8QrbzS1zhFCpxlm6ekFMgGI8sBNtBqVWxP2PRkWMNhFPFLUpZQLx3CXbGzydq20B5QavdI9_piREwjbfVK2s4ylF3Rbz1fhMlX2Em0KngVG-58RsthZvM41nqeK-F4TOQh46c26b5_3TAYz9cQHTpXo8BNVPKBLrfhNgFls7sF1Lcu-gcfoIH5k_hIn3Zne_5PImpcakSN_vxEpIN6Nk2-tsuKPGtmGMeQfCwY_tgWhVW8_qpgnZ6v4nXMyM00O7cP-k8grhdTCp35I0NOwYPHTH53l2onEeLVhnbFiPdAa8n7h81Ru7jgvcK-HS62XO3TqU_VkGDudIQY19RvxS2rgorg9zjwcG1BW0E4jaISdBV8VU3oL5SzLj51hk3IzQ7S1GbNGsCH5oQVdGJ8s1nchOIAex4Z2AlSSGEiYBkUmmJvVDVYbO2qJk67_M_8A_gXw_2L9VmLi5FmmbwykaBXsUDA6Ib56l5Gt-1NWfi1u_TLcD-EfR0Oq7J433SqJWYXXQ9c2zGit7DKwkiFTHFWFyOlZ8e0AIPmyh-t0gSnBolWGYEBSICt6Ok" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1178f7a6a1.mp4?token=LCkGZwuDT13nQQRLZn9u0P_lEHabodhvRKe_u_LEf2VHlcQO4FRUe8ugIAufIzsbDrxx2NiDoIbk8VXYHcYQHV-i6ArVzn2v4ME1tdPzM4nNkQ6bjo8QrbzS1zhFCpxlm6ekFMgGI8sBNtBqVWxP2PRkWMNhFPFLUpZQLx3CXbGzydq20B5QavdI9_piREwjbfVK2s4ylF3Rbz1fhMlX2Em0KngVG-58RsthZvM41nqeK-F4TOQh46c26b5_3TAYz9cQHTpXo8BNVPKBLrfhNgFls7sF1Lcu-gcfoIH5k_hIn3Zne_5PImpcakSN_vxEpIN6Nk2-tsuKPGtmGMeQfCwY_tgWhVW8_qpgnZ6v4nXMyM00O7cP-k8grhdTCp35I0NOwYPHTH53l2onEeLVhnbFiPdAa8n7h81Ru7jgvcK-HS62XO3TqU_VkGDudIQY19RvxS2rgorg9zjwcG1BW0E4jaISdBV8VU3oL5SzLj51hk3IzQ7S1GbNGsCH5oQVdGJ8s1nchOIAex4Z2AlSSGEiYBkUmmJvVDVYbO2qJk67_M_8A_gXw_2L9VmLi5FmmbwykaBXsUDA6Ib56l5Gt-1NWfi1u_TLcD-EfR0Oq7J433SqJWYXXQ9c2zGit7DKwkiFTHFWFyOlZ8e0AIPmyh-t0gSnBolWGYEBSICt6Ok" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔺
🔸
مرگ مغزی فوتبال ایران طی دو دهه...!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/Futball180TV/107170" target="_blank">📅 12:45 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107169">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/261876d28b.mp4?token=lYnyXDGIqg7WS2vnCl0EH_ckcrYqQc8eVwSK5mrYBiMmDk1I0w-kst8KaK5Z_QLHDeUaSxv3PoRC5XJCMue3EEdkAI8skdvRPK-o0Mq1IRLsXrD9WvKN_vfuKE5vclVKWaOZTh5hjLnroAanOStScLvRjgrAIgwGTerRCPKULbRp0UcM11wSD4wK77Khx5NCgau9gSWirsIOXh5-NepKJUeP_1avg8dhCIB-JKhT1gErUg5HL196PvOv9Y8BYiQadIp-bEntDpOYWnsdH1ZzYFtVrtORY5V8kkAYsWGDZ7fMPEdY4p_E7xMRuKVTwOVTteEZa7xso9s8CX4KS39fTQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/261876d28b.mp4?token=lYnyXDGIqg7WS2vnCl0EH_ckcrYqQc8eVwSK5mrYBiMmDk1I0w-kst8KaK5Z_QLHDeUaSxv3PoRC5XJCMue3EEdkAI8skdvRPK-o0Mq1IRLsXrD9WvKN_vfuKE5vclVKWaOZTh5hjLnroAanOStScLvRjgrAIgwGTerRCPKULbRp0UcM11wSD4wK77Khx5NCgau9gSWirsIOXh5-NepKJUeP_1avg8dhCIB-JKhT1gErUg5HL196PvOv9Y8BYiQadIp-bEntDpOYWnsdH1ZzYFtVrtORY5V8kkAYsWGDZ7fMPEdY4p_E7xMRuKVTwOVTteEZa7xso9s8CX4KS39fTQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇳🇱
🇩🇪
هلند - آلمان⁣ امشب ساعت ۲۲:۱۵⁣
🔻
اولین تجربه یورگن کلوپ و ژاوی روی نیمکت دو رقیب سنتی⁣؛ کلوپ: شرایط هر دو تیم مثل همه اما من نسبت به ژاوی بازیکنای بیشتری رو در تیم ملی هلند میشناسم!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/Futball180TV/107169" target="_blank">📅 12:20 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107168">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/20e89ae843.mp4?token=hRQVXbpBqC_yksfJMdWZ9xNYxMR0InngjZUOBZO5V8QXQwNmFwhal0N8Qs-yERfadhI5qEt5C9hUVEfhHnrjlTiOsDjyNwRyCde-LP7n0RhS7vv_OdpYm9gltuYI00rawGTg5TOqCTE46bDV3EZC6aA9_kbWC8dJokqrslr_fupaf8HpNfwscrCcrtlDGXELYRst-9Fd3JbyHgaEL8t2eNSFlQkkU-qP1jxh99g9AasDU4jgSE3WpfpeTQRrWt_RT1ja4dfFVMbkaARCDmNdQpZcRtIWFfbgTkMuxM_Z-7Ztif3OPaGPC0Fvj26mACtBVFnqtdSnSQF_CdDIziMeWJfBGmC8035gn6TJAW3JSo6znkdOvu12vFK3VrYZXbDu-7apoMlRFl-dNzWhbdp7PSe-ynOKptwPkOceghCO5OYiNNX6yHOlquoyncnoZ-Y4z1wz8PMNsj5WBG1MjjAnidX_CCa_KHVHTR69Ko93U1CtM3Z6YK_2fOPyoXQq1lwOosA5vmxT3Eg13ETTgCPloj2Y_RxRAcksUg6lJHdZo-1YB-FgpnrSjfukkPFFbhCuvd9WK83OHgACqolZcyHQ4pLFoqjdmZC2cznvSRWLqd8E0ZFoJFJhptTJACFCfM2ESmXBnsZNmJGufMWU4m8WGcsrjBo1KCgGAZ7a4n-M7-U" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/20e89ae843.mp4?token=hRQVXbpBqC_yksfJMdWZ9xNYxMR0InngjZUOBZO5V8QXQwNmFwhal0N8Qs-yERfadhI5qEt5C9hUVEfhHnrjlTiOsDjyNwRyCde-LP7n0RhS7vv_OdpYm9gltuYI00rawGTg5TOqCTE46bDV3EZC6aA9_kbWC8dJokqrslr_fupaf8HpNfwscrCcrtlDGXELYRst-9Fd3JbyHgaEL8t2eNSFlQkkU-qP1jxh99g9AasDU4jgSE3WpfpeTQRrWt_RT1ja4dfFVMbkaARCDmNdQpZcRtIWFfbgTkMuxM_Z-7Ztif3OPaGPC0Fvj26mACtBVFnqtdSnSQF_CdDIziMeWJfBGmC8035gn6TJAW3JSo6znkdOvu12vFK3VrYZXbDu-7apoMlRFl-dNzWhbdp7PSe-ynOKptwPkOceghCO5OYiNNX6yHOlquoyncnoZ-Y4z1wz8PMNsj5WBG1MjjAnidX_CCa_KHVHTR69Ko93U1CtM3Z6YK_2fOPyoXQq1lwOosA5vmxT3Eg13ETTgCPloj2Y_RxRAcksUg6lJHdZo-1YB-FgpnrSjfukkPFFbhCuvd9WK83OHgACqolZcyHQ4pLFoqjdmZC2cznvSRWLqd8E0ZFoJFJhptTJACFCfM2ESmXBnsZNmJGufMWU4m8WGcsrjBo1KCgGAZ7a4n-M7-U" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📊
🇪🇸
آنالیز ویژه برای درک قدرت بارسلونا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/Futball180TV/107168" target="_blank">📅 11:55 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107167">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XSiJsikFHDqOEWVBhQxahOJICByOyTgQJVneGFoFwM-2rcscL8iNJEyZsbPlBVA2MGmIwI7zXEzgFrFrprP4phcEdo-ySxCgbZL9RqE-x18aDwP4QMebjtT8WZZ8oLc0QTz4XeeQM90DhzDhFGA0sG2Fl2mIeY9lUdLwrhLSchOG7O6CtJYUoPBAGUwsywBlokVUMoRolZRKGiTVWz-uA4p7qnjblA34Yc_ouAato7FarLos6zIh-afaeiV3JKzlI4sAN2DWyr9L50Z_NP-7Poa_wlWfE9SKyZ3lyF6nSJw7GxjP6OWtH43q7x8OsUWycSc09_UHr9XDEhpjIa07SQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
📊
5 بازیکن برتر از نظر تعداد گل‌ها و پاس گل در لیگ‌های معتبر اروپایی تا به امروز:
🔻
رافینیا دیاز – 17 مشارکت (گل و پاس گل).
🔻
لامین یامال – 14 مشارکت (گل و پاس گل).
🔹
کیلیان امباپه – 10 مشارکت (گل و پاس گل).
🔻
مایکل اولیسه – 8 مشارکت (گل و پاس گل).
🔺
فران تورس – 7 مشارکت (گل و پاس گل).
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/Futball180TV/107167" target="_blank">📅 11:32 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107166">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/Futball180TV/107166" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/Futball180TV/107166" target="_blank">📅 11:32 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107165">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VrRFh4wUs18xJJXFaCnM8HUxPjlcVHwoZGnu3bRBP2MJiRgCTZArY_RhdieRjRifRpZNl63IzzWtM5opoUmJ6GoEOlu3S8wNPHYsJ3m6iKzKvXcWVbHgOzsiupsOrOm7EDXJTT-oVPa8UkROSbeerW8VbTbrfwPMqfTwXQyFgtP3RyasGrOoCUz5nFrqKQFDCFLvu69W5x8uSFRqhLMPNcixjZvU8CYvhHBjZHCACIsRJUigsE3dl2Tfgiu21OthFk3AScZAgA00JSAtzSfSGmxidsQlV9Bftf4N-Z4gbcc9m98ZYwEm67Bq_tus5w8rYS2toezVCEYx2oh0gPsEuw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🦖
مچ‌های مهم امروز در سایت بین‌المللی
TrexBet
آلمان
🆚
هلند
دانمارک
🆚
نروژ
ولز
🆚
پرتغال
اروگوئه
🆚
ژاپن
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
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/Futball180TV/107165" target="_blank">📅 11:32 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107164">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ku5g63mfwM8lubxantrDfuVCbOMPTJDcTep3jY3KkNWIJ7Dl5Pu_UzkW7fFqjanqMdx5-PRx36Ys689LOSiG2y58SifES7xjMO4_ehnQwMuZamPw2h3-GM7IjpSXVUzzqHEodBZOjnzMil0pkiS1ay4kydqLfTUHQD_dKysq6-W8xYuJlOo9bWLbVXrqGHBAPtz7myS9hVtZ4SlS3bV8VhWErZu6z4fGlYtSEfCmfd44WXG1NbPkPBpsXWdVS6v0KPPVGwzZ5cxf_XEwZ-TVaprXOgBzqBMrrWSwqBEVJ2uuWsypqePFkyJsgNKen-b0hoi_lYhvbam4cgtBIxsqEA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
✔️
🔥
بیشترین تعداد گل/پاس‌گل در لیگ‌های برتر اروپا از ابتدای سال 2026:
🇪🇸
لامینه یامال - 24
🇩🇪
اولیسه - 24
🇩🇪
کین - 23
🇮🇹
مالن - 22
🏴󠁧󠁢󠁥󠁮󠁧󠁿
برونو فرناندز - 22
🇪🇸
رافینیا - 21
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/Futball180TV/107164" target="_blank">📅 11:05 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107163">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7f3392248d.mp4?token=hKu3I5ha61w4marIbTIJ82zLosWZCXbHpRw4mGzSrPVnFaIfCMikAigAd1gCp_T7thFCxu5uIlyIC7-EdGQOFbijWSXxwZ8851d7Wlwj7dvfaYIiw8K4WbwhVtcjgyuqFDVRencu5vdw1v-EI1CgBADkLfmzCk9vO-BUZtFcB8Fx9NyIpqGoD0vQb-gJD-eR1wGz0k1iViAFBcj0Sw6puu2I5quszv5tJN5kUyNGzzPtBFj8Be8CC3Qxb_skzXDjXvI04KgHyESVb3cyqF9iU8ZrT992LfMhvsCawku3Rw2pPL6LNBqIC2WRgYj4xrkWRU0jFA2r4i80fXzSoqrXcg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7f3392248d.mp4?token=hKu3I5ha61w4marIbTIJ82zLosWZCXbHpRw4mGzSrPVnFaIfCMikAigAd1gCp_T7thFCxu5uIlyIC7-EdGQOFbijWSXxwZ8851d7Wlwj7dvfaYIiw8K4WbwhVtcjgyuqFDVRencu5vdw1v-EI1CgBADkLfmzCk9vO-BUZtFcB8Fx9NyIpqGoD0vQb-gJD-eR1wGz0k1iViAFBcj0Sw6puu2I5quszv5tJN5kUyNGzzPtBFj8Be8CC3Qxb_skzXDjXvI04KgHyESVb3cyqF9iU8ZrT992LfMhvsCawku3Rw2pPL6LNBqIC2WRgYj4xrkWRU0jFA2r4i80fXzSoqrXcg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✔️
🎙
صحبت‌های جالب دکتر محمدحسین پور غریب درباره اهمیت ورزش: ورزش اوقات فراغت نیست!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/Futball180TV/107163" target="_blank">📅 10:40 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107162">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6d50e15c35.mp4?token=UUIKgDMVbE4QzZPEMEkfRMeLuyT-jiZryOs8V6bSM1GKyZb_n5Oo0EjzasD0vL54bEN69xJ4ul7co4Yajrwp0TTyIj10hE2E14I38lNaD4TJe1qfh4fL9lKkir7yD6HNegxjeciD0hreBCXPckX5-ClQo1-STXwpFimKGdYTO3YxVMuOrm1iyhribJvyw1jbNN2pcKy7B_62lZV0Qwruqt3cccko41WyEKkUUUJ_QLcepzGrYokTh3252qGcOdrATFitkr5Q6CsU8GEUmCPhxmJqWVE87cvRXfHehFUdI7Px0scnBy2DMkPJ6pNLWG8o9lmZAKI22p2i-LtSkfnrtQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6d50e15c35.mp4?token=UUIKgDMVbE4QzZPEMEkfRMeLuyT-jiZryOs8V6bSM1GKyZb_n5Oo0EjzasD0vL54bEN69xJ4ul7co4Yajrwp0TTyIj10hE2E14I38lNaD4TJe1qfh4fL9lKkir7yD6HNegxjeciD0hreBCXPckX5-ClQo1-STXwpFimKGdYTO3YxVMuOrm1iyhribJvyw1jbNN2pcKy7B_62lZV0Qwruqt3cccko41WyEKkUUUJ_QLcepzGrYokTh3252qGcOdrATFitkr5Q6CsU8GEUmCPhxmJqWVE87cvRXfHehFUdI7Px0scnBy2DMkPJ6pNLWG8o9lmZAKI22p2i-LtSkfnrtQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
اول مهر به روایت تصویر؛ صادقانه ترین مصاحبه مربوط به سال تحصیلی جدید
😆
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/Futball180TV/107162" target="_blank">📅 10:15 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107161">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a9544f249c.mp4?token=qh4RO6FzOR9SKxVyEjqkiPDQGr47KeHbIMDo3iwNm4Zg2Y6wU6OUZR5qmUVIG0kkmPWBdU38-q8T9AE3Pp1lU9W_My3ibxpYwGN15LiEKCsF8cuGF076dogihFZxMNI2RUxPY96wkYCAb8R6RWtJd-YRspUIYiOU8M1XbLj5KVajbpSd07_vypyl0KN1-5N1FR1Nyn31QB4D639-R6VlKVfwagyR_OLCDSHh6tbw3u5yWD20aHGh6NJ31Xn4ySHvruMICbzN3GZ-IeoOdnMw1ta4EZXOEE43Ji3CXASfosrXbLmifLt_4xFwRH25GypkHB3iTsC7SKAfOEN3P47ahw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a9544f249c.mp4?token=qh4RO6FzOR9SKxVyEjqkiPDQGr47KeHbIMDo3iwNm4Zg2Y6wU6OUZR5qmUVIG0kkmPWBdU38-q8T9AE3Pp1lU9W_My3ibxpYwGN15LiEKCsF8cuGF076dogihFZxMNI2RUxPY96wkYCAb8R6RWtJd-YRspUIYiOU8M1XbLj5KVajbpSd07_vypyl0KN1-5N1FR1Nyn31QB4D639-R6VlKVfwagyR_OLCDSHh6tbw3u5yWD20aHGh6NJ31Xn4ySHvruMICbzN3GZ-IeoOdnMw1ta4EZXOEE43Ji3CXASfosrXbLmifLt_4xFwRH25GypkHB3iTsC7SKAfOEN3P47ahw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
ویدیو از یک‌تئاتر با حضور مهرداد صدیقیان و فاطمه مسعودی که حواشی زیادی داشته!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/Futball180TV/107161" target="_blank">📅 09:50 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107160">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5567bbdad8.mp4?token=t1bQVbuUCqSW7toCTNsBTvV2NUYaeAF6PQD4xHa8RYY9EBpWTTvq6jUAlXOviIgY4UNiFUTEQ2NVqGT7cuy_-Ur7XBSQHrjWAZH-0bvEH42LsN7UHr-Mr-xg-k6gI-i4zxhjGgcWCVd4pkWfCMI7NDCCrACeMHuudYIObORaFspYl97azy-qrHWYkT_P3nMq27IBfHhiFGwunBX36wic1jEdKIbiZVAQSqtr1LUc9egMmtrxpwjhbouUd4d5VBkk14lMSbtIv1WhCrjq7JW-_D9D9LcvcahvvvPVX9MIc7zrLgr2N048StM9PG6VuxzY223TKCTqyfVRQq56QwD-VA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5567bbdad8.mp4?token=t1bQVbuUCqSW7toCTNsBTvV2NUYaeAF6PQD4xHa8RYY9EBpWTTvq6jUAlXOviIgY4UNiFUTEQ2NVqGT7cuy_-Ur7XBSQHrjWAZH-0bvEH42LsN7UHr-Mr-xg-k6gI-i4zxhjGgcWCVd4pkWfCMI7NDCCrACeMHuudYIObORaFspYl97azy-qrHWYkT_P3nMq27IBfHhiFGwunBX36wic1jEdKIbiZVAQSqtr1LUc9egMmtrxpwjhbouUd4d5VBkk14lMSbtIv1WhCrjq7JW-_D9D9LcvcahvvvPVX9MIc7zrLgr2N048StM9PG6VuxzY223TKCTqyfVRQq56QwD-VA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
«پسر بد» در روز اول مهر الگوی دانش‌آموزان!!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/Futball180TV/107160" target="_blank">📅 09:25 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107159">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a9d6b05a55.mp4?token=t2qNqYZyeol_EO7T46skfXJwV-MtBhSxtk9GW1Y43Ca6SUbp2_wuOyurqy8sEykRyr94ka9mOdcZl4LSqb4qgzFJ6Hv0h8mfD_nAQ0b6uILAeBvqmFHM1F3b9mLdyacmcoBIjz_boGOMOWfk_PJq7z-chBpDnnxj-8LSj524KEtcR0-DMQF5SJNJMH0gpLZobnm5EMJcjwxpRtVfKT3s3vV6Vn2f8-qZ4V3-2d7Xt7vd8-Ydx2utAsIaPWyjO321gCNxS9Qy_0TxUXPXg927pk9dYhbEpRZcO-YFJu9B3n-AGtVPZx9xJoxAOgaSiEhyXs-ZbuLPn5axF_x2i1OTnQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a9d6b05a55.mp4?token=t2qNqYZyeol_EO7T46skfXJwV-MtBhSxtk9GW1Y43Ca6SUbp2_wuOyurqy8sEykRyr94ka9mOdcZl4LSqb4qgzFJ6Hv0h8mfD_nAQ0b6uILAeBvqmFHM1F3b9mLdyacmcoBIjz_boGOMOWfk_PJq7z-chBpDnnxj-8LSj524KEtcR0-DMQF5SJNJMH0gpLZobnm5EMJcjwxpRtVfKT3s3vV6Vn2f8-qZ4V3-2d7Xt7vd8-Ydx2utAsIaPWyjO321gCNxS9Qy_0TxUXPXg927pk9dYhbEpRZcO-YFJu9B3n-AGtVPZx9xJoxAOgaSiEhyXs-ZbuLPn5axF_x2i1OTnQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
❌
علت‌احتمالی عدم‌دعوت قایدی به تیم‌ملی!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/Futball180TV/107159" target="_blank">📅 09:01 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107158">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Jc0ie1knvxuV0OmVnKumyAQloecz4cv7kEPTRH7076DWNpmKklSa1P9FKTYbZPGO7tmr_K4xbqY9rfqVFBNSvnUmAP2tL3aeGIXD5MWglevEN6QA2zmeamwZKGW9J2LRKeLBJeup8E9GSp0GHxagGurOJZQB6jCijMwG13Zsll6LjILo11zP7yKMVEvIZC4O2Gwik_VNAmK1H1H3pyp5o7sH2nd3tAvJV83AYR8JB4_sRtlT-Y_DgjOaEXThmApRnEvA9ctXAkXX6ODpjAVVZPsH8EYdENv-kMRtkIxkZgqMewatnNNwvgpV2h9pdKtfvTYA3qWWwIDe2WiFSQs7ng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇩🇪
آخرین پیراهن آدیداس برای آلمان پس از ۷۲ سال
؛ از ژانویه ۲۰۲۶ کمپانی نایک اسپانسر ژرمن‌ها میشه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/Futball180TV/107158" target="_blank">📅 08:04 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107155">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TSKgXs99tulV_wDwOIlEsbsVRHdepO_v8gwZhxlCynFB8PDQfoOYOWSGbtp9qbX37jhDlwAgvtGq26BlYzH5hnsKDUVKoFQikW3GSsuUySnSkgcIIlZlTj429LjC3N7wSjT2r60qjMT4vWovZz-YdaCDaoY0Jcplx_jQ79FxtrQcR-BnPZoIqVi7M0PP84_yhDElVzipxxZcMadHEgJpoCXaJynJAeBcH9I8g-KxT_OTqLYOqq_LoavOelgn52qEzqpU2mjIWR0uGjYaOTODrT5vlKwvOyx82RqPn-U57WOWtQh4ji7Rd-me04rQL356qA9St8V2uijahygwh7jivw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🏆
ژوآئو فلیکس: درسته امباپه و کین فصل فوتبالی خوبی رو داشتن ولی به نظرم لامین یامال خود فوتباله و کسیه که مستحق دریافت توپ طلاست.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/Futball180TV/107155" target="_blank">📅 01:23 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107154">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">🚨
❌
🇮🇷
🇮🇷
دیدار استقلال و تراکتور بجای ۱۶ مهر قرار است روز ۱۵ مهر برگزار شود. این اتفاق احتمالا بزودی از سوی سازمان‌لیگ‌ اعلام خواهد شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/Futball180TV/107154" target="_blank">📅 00:03 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107153">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fVxTFQ1jrrNqr7Zh6BYmbdTJkz8PUeYRUQ5Js43EcXlcP8C5VCRGIz2tczFSywTCHNPQrudRj1efC5DmC-qdUTmq5ZP8o_W3gy-uMYLBa_X00LPf8zuZOuVOJ6ncA8co6XT6J4KuytQOOeRLeC8oL0ZN7VsZS72GXlFRoOpCr2SMjYQ_EQDVfWV74cRhlWwYRUDCpCuZPK9tjTWp5w1VVIAflAkL3X-n6NgqboLSCoiC_MM698bsAGe9L07ep9SYemBx3C0KEvgx7ua3CXKV8B7Q71jecpxIQAWxCW-d8Vt4CjLYuzuqy_dHRLm9S3EhiHOvypYkbT0oaTiX4LXk9g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇮🇷
دیدیه‌اندونگ بازیکن سابق استقلال در لیست خرید جواد نکونام برای تقویت تراکتور قرار دارد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/Futball180TV/107153" target="_blank">📅 23:17 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107152">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ebd6935b14.mp4?token=ByXWdh8mzO1anVxP0xA1ywvsm_jHlFVRwp2FnOpGvZeI0ykG1qNZscKABVACBvG7HwE-U8VauYZGtXUuYjTvl_eNoRrcdJFFtnM_7kEfj8RB1hhI55A0L__p2XSBUSXEqNtZuDUbTHQmw-34Fx8R8tua_RKVWnmuj8FNFvP_2MQqsDd0dItzKOfNnqboL6DWlyd5wFt_FAu0xARPYJQys12t4-NCCi8B77gCFaObCpP9uKleldk1yg6n43ZL-GkIPgYv_xurVN1A1nB23r24WvKkJo4lkXwTsnuq9DcVuZDv4xuKGNnW6ljeb_N8isY3A6YHt_IX-Y4ySikYgVGIvA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ebd6935b14.mp4?token=ByXWdh8mzO1anVxP0xA1ywvsm_jHlFVRwp2FnOpGvZeI0ykG1qNZscKABVACBvG7HwE-U8VauYZGtXUuYjTvl_eNoRrcdJFFtnM_7kEfj8RB1hhI55A0L__p2XSBUSXEqNtZuDUbTHQmw-34Fx8R8tua_RKVWnmuj8FNFvP_2MQqsDd0dItzKOfNnqboL6DWlyd5wFt_FAu0xARPYJQys12t4-NCCi8B77gCFaObCpP9uKleldk1yg6n43ZL-GkIPgYv_xurVN1A1nB23r24WvKkJo4lkXwTsnuq9DcVuZDv4xuKGNnW6ljeb_N8isY3A6YHt_IX-Y4ySikYgVGIvA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
اکسپلور گردی احمدالشرع رئیس دولت سوریه وسط سخنرانی‌ها در سازمان‌ملل!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/Futball180TV/107152" target="_blank">📅 22:02 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107151">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ARPHFmoY4B-wPfQzcoeqfk8X4ddGg_NzDp-xYJkffvmj1IHwLb-H13UnRJr_I_Z9ydu2RnSHfQwGzhoDMumAA7WbaDt16j9VvQrwO0ur3v-hVQqwPWrR4-aIM9UAiIbI1c9tbkh58KtCaDKb2p5clk0UXGvH9nHkCizkYy1zUY5eo2forpDx4HJF_dIMXaofR_8Q5h-0hYMF2nI_3Cf7LuCWhVE5FdsfjfCArmui3zK8IchkfbGRaQGJpdu9v8-yL8b_zGhoo26s8-VE72-DhbgfjHmKvJvEgGuEFSxfQ7QR-FzbdKRmdDB8hP_7P1iQJCoatuyEGczZ97YLkVk9vg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🎙
آخرین بخش صحبت رونالدو در کنفرانس خبری خطاب به رسانه‌ها:
بعضی رسانه‌ها عاشق حمله کردن به من هستن؛ اونا سال‌هاست که سعی دارن من رو از پا در بیارن (بکشن)، اما این کار هرگز روی من جواب نمی‌ده. شاید با یک شات‌گان جواب بده، اما حتی در اون صورت هم من می‌تونم از گلوله جاخالی بدم.
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/Futball180TV/107151" target="_blank">📅 21:28 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107150">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dddf19637c.mp4?token=aCgT5AvBi-1EtrWL7BUeCTXfGdj7vw7Nyh5bkrEv8j6u6VNG-UILMuQRGRls9tqdrz7Y7Knz-9jMJk50HtCc1YicaSYam-6RZPEm6Qn4llTJoB3gNnzd7q5mZQfkvWuSYiejSXL-vexLnCOlSjLH-cWmO1wZEd7NZo-berKJatZnIHHyU2a5SUZRvq1wwuJiFkVec6pY09i1_vTtWy-TqUqjFNsK6Mt3HpTuOB9FvrPHcQaognlmLDAVYCdeb-6GFIzAewD8RLQ7twQHBW7SRYLuhFStQOLEb9Umw4twoEACdsjXS82uGAYzpAXy4vRy-hpGYugZQT-qlFkX0NqLbw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dddf19637c.mp4?token=aCgT5AvBi-1EtrWL7BUeCTXfGdj7vw7Nyh5bkrEv8j6u6VNG-UILMuQRGRls9tqdrz7Y7Knz-9jMJk50HtCc1YicaSYam-6RZPEm6Qn4llTJoB3gNnzd7q5mZQfkvWuSYiejSXL-vexLnCOlSjLH-cWmO1wZEd7NZo-berKJatZnIHHyU2a5SUZRvq1wwuJiFkVec6pY09i1_vTtWy-TqUqjFNsK6Mt3HpTuOB9FvrPHcQaognlmLDAVYCdeb-6GFIzAewD8RLQ7twQHBW7SRYLuhFStQOLEb9Umw4twoEACdsjXS82uGAYzpAXy4vRy-hpGYugZQT-qlFkX0NqLbw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
⚠️
🇮🇷
🇮🇷
کنعانی در دربی سامان فلاح رو تهدید کرده بود، حالا خودش به تیم ملی دعوت نشده است: «نمی‌ذارم پاتو بذاری تیم ملی!»
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/Futball180TV/107150" target="_blank">📅 21:01 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107149">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bHHEbi43X1RfJiwWRg9CczgRgulIAmjnnJu9Oo33JHm7D8QDeZAPjQY5FNpS2KIhnQF1aIvDPByWUVcaKPbt6MWfxqnPf6yD744musLd3OeSZWAguQNF9qwc6eI8EUg2-fexAUL4-A37ESr4UpXN6n_1CF984Cjeut53gWs3bXZLLohtD4uCM8osVDFWODZ2jsTiMGDoVCQ3pVwLorvZQXPZNWvmkapPTl4MAy_rEpWc3Vmn_lEReZsZGOBpeDhxBiAaq3ARddYUgPvgDQUdRBbt2mMhWflEAyq4e8rxPmF0ocRVJoqLMCYxAR-4VOyo4OGyzQ581YkuYJdzkTQYIA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
👀
اپدیت جدید تلگرام از میانگین زمان سین زدن و جواب دادن به پیام پیوی ها !
اینجوریه که مثلا وقتی وارد پروفایل یک شخص میشید اون قسمت بالای  شمارش میزنه بطور میانگین، چقدر سریع به پیام‌ها پاسخ میده مثلا 5 دقیقه، 2 ساعت یا 3 روز!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/Futball180TV/107149" target="_blank">📅 20:40 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107148">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/50c700c8bb.mp4?token=OitlwryrWm0hn-jNRTlzwflNQ5e68byZZTptjvfbV0SXEyuTDEsf-7WqoBNVUstHJsyDZQ1cyb_Nd-PQK7nHbVvBkU8jeugze-iTeEP_W-wEewzMyYikornrtFPPUqWA6MHzB8k3K6NxMgtSZDU_9_wBsOxPDE1MxkeuEe1dUSO0r5wZ8uPBO4Tubi0EEgaPN4bthKwVNZRsTaRxWWUdz4x2J8WaaEmYOpWWGEjnFs2nBljPvDNqapOusUf7dmuKMCYKsmmvNnwWhlAkGR5tWq7YozeLb90K1nHHOWHqD4wwt3JCrQBptrv-uEQaDWuKXVt-FbHZOYWRPafMnklQiEzELy23D3jHHVh_fZR7pNq-TLfIt2JNZEDaT2oLWUwd-Hn8cPsjWW0u_eTiNoL9lYtKDz4FFzI_isJXgEyPU1UAYI0jLTsQWebR0G6_kmB_209-K11PdEPk0OLXVIgv1IkAw212S2pnPZUGVcbV9SurLM7a7qwNWJ_XPq535AzhEXqcPQ5LrfCahJQ1suG57RPfWO_6NCPECP-doDvVA4GmZj1KFkPFvOhSPyG9B72JJggoqJ7WONhYp2qa2O7_oifpOkiMOKFxCvAg00tHr4QFWooQwxiYsQb04zo_SR6oOpAjuyKpBCQXJqjYOgQyZrlvledqSzt4SJc8_UOzCmU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/50c700c8bb.mp4?token=OitlwryrWm0hn-jNRTlzwflNQ5e68byZZTptjvfbV0SXEyuTDEsf-7WqoBNVUstHJsyDZQ1cyb_Nd-PQK7nHbVvBkU8jeugze-iTeEP_W-wEewzMyYikornrtFPPUqWA6MHzB8k3K6NxMgtSZDU_9_wBsOxPDE1MxkeuEe1dUSO0r5wZ8uPBO4Tubi0EEgaPN4bthKwVNZRsTaRxWWUdz4x2J8WaaEmYOpWWGEjnFs2nBljPvDNqapOusUf7dmuKMCYKsmmvNnwWhlAkGR5tWq7YozeLb90K1nHHOWHqD4wwt3JCrQBptrv-uEQaDWuKXVt-FbHZOYWRPafMnklQiEzELy23D3jHHVh_fZR7pNq-TLfIt2JNZEDaT2oLWUwd-Hn8cPsjWW0u_eTiNoL9lYtKDz4FFzI_isJXgEyPU1UAYI0jLTsQWebR0G6_kmB_209-K11PdEPk0OLXVIgv1IkAw212S2pnPZUGVcbV9SurLM7a7qwNWJ_XPq535AzhEXqcPQ5LrfCahJQ1suG57RPfWO_6NCPECP-doDvVA4GmZj1KFkPFvOhSPyG9B72JJggoqJ7WONhYp2qa2O7_oifpOkiMOKFxCvAg00tHr4QFWooQwxiYsQb04zo_SR6oOpAjuyKpBCQXJqjYOgQyZrlvledqSzt4SJc8_UOzCmU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
✅
چهار عمل کاربردی در نسل‌جدید گوشی‌های سامسونگ که حسابی به‌دردتون میخوره
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/Futball180TV/107148" target="_blank">📅 20:35 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107147">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/43c1442263.mp4?token=Z7QnmSfha5IPFZJHciw5nw-TO-HcLgUq645EZhQm012DZXwQVgsqp3rS3Iv65PtXVTBqIERYujj0Q7nkrNzSmgYM0LQRFIgdKgR1KzDtqQqN5yZv8J9gP5EMc80LBm7PK3WAuQDhBFH27nCef6Jc2rrcDUiaH9y8X9yh8-CgzotYkNdKy3lj_Nb6vsS076b_TXp2lu21If4-WOoUa5UmWwbkYhXzcQh4UcfjowO02mVotgegTAU2tA9u5A0H7HYJlUv43fSputu8JAuktvCFzFwA36xF3Up2xTGf4Rcy5RmLAE5XmwRTiGtyVOZqDkJPlHbwWPPYubs-DL41nNtm1g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/43c1442263.mp4?token=Z7QnmSfha5IPFZJHciw5nw-TO-HcLgUq645EZhQm012DZXwQVgsqp3rS3Iv65PtXVTBqIERYujj0Q7nkrNzSmgYM0LQRFIgdKgR1KzDtqQqN5yZv8J9gP5EMc80LBm7PK3WAuQDhBFH27nCef6Jc2rrcDUiaH9y8X9yh8-CgzotYkNdKy3lj_Nb6vsS076b_TXp2lu21If4-WOoUa5UmWwbkYhXzcQh4UcfjowO02mVotgegTAU2tA9u5A0H7HYJlUv43fSputu8JAuktvCFzFwA36xF3Up2xTGf4Rcy5RmLAE5XmwRTiGtyVOZqDkJPlHbwWPPYubs-DL41nNtm1g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">😆
‼️
مصاحبه‌سمی یک دانش‌آموز از اول‌مهرماه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/Futball180TV/107147" target="_blank">📅 20:35 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107144">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/43c1442263.mp4?token=AiZXtgkpp6z7Ii7iIT9iWSnRag8-OziKAkQ-Jc4YswX139ObaXw5xr8cESaChx4d102gzTgAaF79TSkFgZZCuqw6186ANqURxrezwPrzYggo_jD0QGP03GYdSkxSl7EeKmTeiSuC204SmxUs72Gpb8WhPPBZlpDP-oAnMwDqWOLc6PxyXsImqyf2auik6sh-jfoMaNvlwz2ewozAHONDduK9SOG7HD6pSD19ClWzL4qU13EltO1OgxqYHGs6QEj00lTjy4bx2lGjHZAWFezBTK8vcdG2z_i1aRgEwTJAr2sgiuMvSooP_zL678qw9vFcK16PH-_CDoPshPfds_xeKA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/43c1442263.mp4?token=AiZXtgkpp6z7Ii7iIT9iWSnRag8-OziKAkQ-Jc4YswX139ObaXw5xr8cESaChx4d102gzTgAaF79TSkFgZZCuqw6186ANqURxrezwPrzYggo_jD0QGP03GYdSkxSl7EeKmTeiSuC204SmxUs72Gpb8WhPPBZlpDP-oAnMwDqWOLc6PxyXsImqyf2auik6sh-jfoMaNvlwz2ewozAHONDduK9SOG7HD6pSD19ClWzL4qU13EltO1OgxqYHGs6QEj00lTjy4bx2lGjHZAWFezBTK8vcdG2z_i1aRgEwTJAr2sgiuMvSooP_zL678qw9vFcK16PH-_CDoPshPfds_xeKA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">😆
‼️
مصاحبه‌سمی یک دانش‌آموز از اول‌مهرماه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/Futball180TV/107144" target="_blank">📅 20:35 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107143">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">🚨
🚨
🚨
🚨
😆
😆
😆
رپ‌خونی سمی ابوطالب برای تیزر برنامه جدیدش
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/Futball180TV/107143" target="_blank">📅 20:16 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107142">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d24115e06f.mp4?token=uNYsnukgyYoTiAYRqBaoPajVlYE0qzB5JYMp3ZGC6U6AI7OrlG2J3Jeq6JOBbPmc7wt3QhVqEdYT2wIijj_6ErVTvAljMlhA8cUAsPC4i_hTX0H46dWlGMl3hWpLbDNcPJ3CI98I9gNJLBd8KDZBJo1PZo3Pt6UfJl8lVVhMJoKlWkeUPHKF_vO4XqyKKCAEgfSlSjZg-QRyyg_hxXI_b5JauG1xXkSYl2a5UidyR64eer8bUNufcWs6BMsH6ZhYp8aLw7VC3yfswyn9GweQuvu-mGBfdE4qRZk3Ap3wQjHMFPrKCrg5Po2ElBu6xDo9hlf5W-GC-8qgRfbFjI2H2Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d24115e06f.mp4?token=uNYsnukgyYoTiAYRqBaoPajVlYE0qzB5JYMp3ZGC6U6AI7OrlG2J3Jeq6JOBbPmc7wt3QhVqEdYT2wIijj_6ErVTvAljMlhA8cUAsPC4i_hTX0H46dWlGMl3hWpLbDNcPJ3CI98I9gNJLBd8KDZBJo1PZo3Pt6UfJl8lVVhMJoKlWkeUPHKF_vO4XqyKKCAEgfSlSjZg-QRyyg_hxXI_b5JauG1xXkSYl2a5UidyR64eer8bUNufcWs6BMsH6ZhYp8aLw7VC3yfswyn9GweQuvu-mGBfdE4qRZk3Ap3wQjHMFPrKCrg5Po2ElBu6xDo9hlf5W-GC-8qgRfbFjI2H2Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
واکنش پیمان طالبی مجری شبکه سه به شکست چهار گله تیم فوتبال امید از کره شمالی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/Futball180TV/107142" target="_blank">📅 20:02 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107141">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/D2kVL0jo1yJpP9Y6ryLx3-KYrFNS3DjfmB5Z5ZqGdVuoycLxftbOT5KPDz5AhWzdsjnbGOWPnXtdRTYw-gZKZkvt6QqmaJ3FYUsoLNKKm1ZgBhjFqlLuhaGPNb-1g99KH9JrccKmZYH4rNyHr1J0bDnj_Hw1JJfD8cgswhN9MarLBoD3oSw5jaMqCIDQKCNWXC9DWVAs5Jc0mdbWK-gc-lSsCVybh_M5rkVm8kHg76beaXYCMPaBZgmL_SFwfsH5F5ajL-cjtgAp8YJe8PxLouh9ncO8zuTKJyJABJjp_m3Y9faaxCv9yysdSckpPg18ssiAzX6jyZEr6tu4jIosew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
📱
استوری‌جالب زبیر‌نیک‌نفس بازیکن سابق استقلال به شکست ایران مقابل کره‌شمالی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/Futball180TV/107141" target="_blank">📅 19:32 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107140">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LfQo3gSsxmMg9oANLcl0-LHucijfn9TOPv7Wj_PaM3u1r1KrGcgrcxwNNRj0I11oqTECQ2K8wEeGcThY-MEmI8Z0OZp62ZSWSr9-x98rxz_3S1Eyp7Xlf_fCZ1x2faqIc8YEsh1STajzh9KXexvdRGR625AgDfbLmYepPOgJyAZgsBbUjrxxN3fefU0IP0cqn8aZxSzKcI-PZVM4fnXEDDRmWGMhgZJcQnv_MAVaSZqO0xUO3cgKQ7ia3gLNKattXxJ269rsrKglc_uYQfNwT_notyXzmkbZ73TcTgzigyikeFIkxoLDRUO3XHuBB9ga-P5RHCcIxENlMn1OhIuGKQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
🇪🇸
بهترین استارت یک‌فصل بازیکنان بارسلونا در تاریخ این تیم با صدرنشینی اسطوره ابدی مسی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/Futball180TV/107140" target="_blank">📅 19:01 · 01 Mehr 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>

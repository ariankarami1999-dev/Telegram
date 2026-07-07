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
<img src="https://cdn5.telesco.pe/file/MmVNw1imC60hETuqpU757ZhlgTDiyd4iDODdNCq437amDmWYoU4nYDbrBjItlj9HWvXutnlx_HylkupMIsL0Cy3CFqsDQJK95s4VW9Qt36QbklsNp3-2x2D0JfGFjcCEI00jArdJe6sQ88QUx7YWF1hTeh7K9EmpiQSONaE-JJXVY8_n3lPubkuVXp7CbZwrfjR-aTSrClHUmldCMQmw0F80gHgbC6a934Vfv2nQyxxMtm-eclCunApE4ygWWJ04Njun1JpZMNIFYO4Y8TupHfjshe4qDO-Gf67aK3_fYrwC6Z32M8zlgQ5eZwwrzLkltHofrIzw-EnRtLnltfvD3Q.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 جام جهانی 2026 | فوتبال 180</h1>
<p>@Futball180TV • 👥 616K عضو</p>
<a href="https://t.me/Futball180TV" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 In the name of God; The only popular sports channel on Telegram: All for Iran...🖤We respect the copyright laws and follow the laws, Mr.@Durov...🙏🌹Contact ads:@TivaAds</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-17 03:19:19</div>
<hr>

<div class="tg-post" id="msg-98993">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">🚨
🏆
برنامه کامل مرحله ¼نهایی جام‌جهانی
🇫🇷
فرانسه
🆚
مراکش
🇲🇦
🗓
پنجشنبه ۱۸ تیر ساعت 23:30
🇪🇸
اسپانیا
🆚
بلژیک
🇧🇪
🗓
جمعه ۱۹ تیر ساعت 22:30
🏴󠁧󠁢󠁥󠁮󠁧󠁿
انگلیس
🆚
نروژ
🇳🇴
🗓
يکشنبه ۲۱ تیر ساعت 00:30 بامداد
🇦🇷
آرژانتین
🆚
سوئیس
🇨🇭
🗓
يکشنبه 21 تیر ساعت 04:30 بامداد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 6.14K · <a href="https://t.me/Futball180TV/98993" target="_blank">📅 02:39 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98992">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mn1z5eXfMKK2ChUj2C2lSCsNO3oDwqlbXg7caO3Rc32ePmij33rwzCczciHjw1nDONO_Iuu3K5bj9zDJGRPdUlpSj2yHFoQCr-1CgqHPS5dYJgFCfP6AAGBYo2w5PoGJiJ8mvGet0yJXh4UcplFjzb-felipU2fJ3RsEtV8LykIw5-fcQYya3xqM_Nn_LfsCx96NKy1frrlnX_EkAl9hjmZKAXSmYF73zhKULLAITbaSVv7aXIYhG4X_uTJ3OavGLcWMyG1UZjmWnEZJzgUIQGsxgPDUuAhTIvFpWtMcj91WEbzZ1xQyUTvd9Z1bxNvKXFQsnWFFAjQ72HJ9T9eRJw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
📊
🏆
بهترین گلزنان جام‌جهانی تا پایان دور‌ ⅛
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 6.78K · <a href="https://t.me/Futball180TV/98992" target="_blank">📅 02:33 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98991">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WC4S29JAPm5tbH9eQ4nhs01MNq4rMiw96GpM-5maQ0-CmkswXFiSnpFEoYwvu47CUhNMNSYWS843NghNaS6iE34qeQ_3FtjDvA7FR8c76eQsaAlbmYOYhFHEtmKjhkRk0GLDYO2V_CywoB13j1CXffwGlf022GAs7RYf-m44khv5tUZk3obv7TJW7N-5bBcP5Ebp2F-USeOX3gE8cIpyag_5w_Wvtbdaxp4S27eoIMiyH54HFxkbE6RSUKDiOpbgh6-H3YbzOQB6oGqu332tfIz9JLuCsYf4MdhIUnMPjSclRKxku2LeOPpaALe0W63SlFIbpkp_HNc7Djj_ILRPtA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
#رسمیییییی
؛ اسطوره آربلوا سرمربی تیم فوتبال فولام انگلیس شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 7.73K · <a href="https://t.me/Futball180TV/98991" target="_blank">📅 02:30 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98989">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DRCueTDZ6mhvD71_WPCHlR8y6raQ09lqePIrxFhO7Tx1L_E27UKEXZKW2p0WsiNsS4UxnqXO5B_Jq3K0K5FSAUHsn5zxbMi6QkjeJjUAX7q2hz22_c7mWDOBljbDZ8S4nkOLbpoO3j-V7ySwRr7W7Va57fvAWD-c8FDWwepsCtNphzt_bMwp9je4uD9lAHxUPL8UtRygSOHogBgdo32p2EGR5Avp1xVa6nQyyifV9uLbDCcyFXsraqQqloz-TrJne_CJ4B4toOh9yqw0eiOStkDdcOYOYKUxK9bTOiyh404QjG-sli4zlguQla8i6-U-sKbgq0hTo0zHPVS5A2gDZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏆
برنامه کامل مرحله ¼نهایی جام‌جهانی
🇫🇷
فرانسه
🆚
مراکش
🇲🇦
🗓
پنجشنبه ۱۸ تیر ساعت 23:30
🇪🇸
اسپانیا
🆚
بلژیک
🇧🇪
🗓
جمعه ۱۹ تیر ساعت 22:30
🏴󠁧󠁢󠁥󠁮󠁧󠁿
انگلیس
🆚
نروژ
🇳🇴
🗓
يکشنبه ۲۱ تیر ساعت 00:30 بامداد
🇦🇷
آرژانتین
🆚
سوئیس
🇨🇭
🗓
يکشنبه 21 تیر ساعت 04:30 بامداد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.75K · <a href="https://t.me/Futball180TV/98989" target="_blank">📅 02:21 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98988">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/J2ezmqXtubYyJSDIu7UnYDih-u7dWHfOUv3qlWls8imJK31TjYdc7xiVNuVUbOZ_ZKkdxBKvxQBlsDEvJVQPyQ-2fdtncWfSaYo7tvtSgZsHxUMOybdg3D5kDsN4inBPV211bFfSjjdy5F-pU7-N_yLKE7_HmEB2dxouVn8TTP7mnIAVGqLn1fLLF1gP7R7eqfWjv2B0WTKc52BfVWfYRBwqrTs6XbF00H0kRWZ5Dqq86gcdgwDBET_KmqFx6yTsCPolvf4ahxyxeSOc2lKBdnD_1tWvBhgtaGKaex0sIRYMStUD3Mi0-G_3E4zJ5heQ17t3IcF2aZPaqOeoBJ2TEg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🏆
تیم‌ملی سوئیس با برتری مقابل کلمبیا در ضربات پنالتی راهی مرحله بعد شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 7.93K · <a href="https://t.me/Futball180TV/98988" target="_blank">📅 02:21 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98987">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromجام جهانی 2026 | فوتبال 180(𝐄𝐬𝐦𝐚𝐢𝐥)</strong></div>
<div class="tg-text">🚨
▶️
🏆
زنده از ضربات پنالتی(بروز میشه)
🇨🇴
✔️
❌
✔️
❌
✔️
🇨🇭
✔️
✔️
❌
✔️
✔️
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 1.38K · <a href="https://t.me/Futball180TV/98987" target="_blank">📅 02:20 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98986">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">گلگلگلگلگگلگلگل و تمامممممممممم</div>
<div class="tg-footer">👁️ 7.62K · <a href="https://t.me/Futball180TV/98986" target="_blank">📅 02:20 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98985">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">سوئیس بزنه صعود میکنه</div>
<div class="tg-footer">👁️ 7.64K · <a href="https://t.me/Futball180TV/98985" target="_blank">📅 02:19 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98984">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromجام جهانی 2026 | فوتبال 180(𝐄𝐬𝐦𝐚𝐢𝐥)</strong></div>
<div class="tg-text">🚨
▶️
🏆
زنده از ضربات پنالتی(بروز میشه)
🇨🇴
✔️
❌
✔️
❌
✔️
🇨🇭
✔️
✔️
❌
✔️
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 777 · <a href="https://t.me/Futball180TV/98984" target="_blank">📅 02:19 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98983">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">گلگلگلگگللگ</div>
<div class="tg-footer">👁️ 7.41K · <a href="https://t.me/Futball180TV/98983" target="_blank">📅 02:19 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98982">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">لوئیز  دیاززز اومد</div>
<div class="tg-footer">👁️ 7.36K · <a href="https://t.me/Futball180TV/98982" target="_blank">📅 02:19 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98981">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">کلمبیا نزنه حذفههههه</div>
<div class="tg-footer">👁️ 7.24K · <a href="https://t.me/Futball180TV/98981" target="_blank">📅 02:18 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98980">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromجام جهانی 2026 | فوتبال 180(𝐄𝐬𝐦𝐚𝐢𝐥)</strong></div>
<div class="tg-text">🚨
▶️
🏆
زنده از ضربات پنالتی(بروز میشه)
🇨🇴
✔️
❌
✔️
❌
🇨🇭
✔️
✔️
❌
✔️
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 313 · <a href="https://t.me/Futball180TV/98980" target="_blank">📅 02:18 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98979">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">گلگگلگلگ سوم سوئیس بالاخره شددد</div>
<div class="tg-footer">👁️ 6.59K · <a href="https://t.me/Futball180TV/98979" target="_blank">📅 02:18 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98978">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromجام جهانی 2026 | فوتبال 180(𝐄𝐬𝐦𝐚𝐢𝐥)</strong></div>
<div class="tg-text">🚨
▶️
🏆
زنده از ضربات پنالتی(بروز میشه)
🇨🇴
✔️
❌
✔️
❌
🇨🇭
✔️
✔️
❌
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12 · <a href="https://t.me/Futball180TV/98978" target="_blank">📅 02:17 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98977">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">پنالتی چهارم کلمبیا و گلگلگل سوووم نشددددد</div>
<div class="tg-footer">👁️ 6.88K · <a href="https://t.me/Futball180TV/98977" target="_blank">📅 02:17 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98976">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromجام جهانی 2026 | فوتبال 180(𝐄𝐬𝐦𝐚𝐢𝐥)</strong></div>
<div class="tg-text">🚨
▶️
🏆
زنده از ضربات پنالتی(بروز میشه)
🇨🇴
✔️
❌
✔️
🇨🇭
✔️
✔️
❌
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 353 · <a href="https://t.me/Futball180TV/98976" target="_blank">📅 02:17 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98975">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">گلگلگلل سوم سوئیس نشدددد</div>
<div class="tg-footer">👁️ 6.36K · <a href="https://t.me/Futball180TV/98975" target="_blank">📅 02:16 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98974">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromجام جهانی 2026 | فوتبال 180(𝐄𝐬𝐦𝐚𝐢𝐥)</strong></div>
<div class="tg-text">🚨
▶️
🏆
زنده از ضربات پنالتی(بروز میشه)
🇨🇴
✔️
❌
✔️
🇨🇭
✔️
✔️
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 374 · <a href="https://t.me/Futball180TV/98974" target="_blank">📅 02:16 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98973">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">گلگلگگلل دوم کلمبیاااا</div>
<div class="tg-footer">👁️ 6.14K · <a href="https://t.me/Futball180TV/98973" target="_blank">📅 02:16 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98972">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromجام جهانی 2026 | فوتبال 180(𝐄𝐬𝐦𝐚𝐢𝐥)</strong></div>
<div class="tg-text">🚨
▶️
🏆
زنده از ضربات پنالتی(بروز میشه)
🇨🇴
✔️
❌
🇨🇭
✔️
✔️
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4 · <a href="https://t.me/Futball180TV/98972" target="_blank">📅 02:15 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98971">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">گلگگلگل دوم سوئیس</div>
<div class="tg-footer">👁️ 6.09K · <a href="https://t.me/Futball180TV/98971" target="_blank">📅 02:15 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98970">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromجام جهانی 2026 | فوتبال 180(𝐄𝐬𝐦𝐚𝐢𝐥)</strong></div>
<div class="tg-text">🚨
▶️
🏆
زنده از ضربات پنالتی(بروز میشه)
🇨🇴
✔️
❌
🇨🇭
✔️
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 455 · <a href="https://t.me/Futball180TV/98970" target="_blank">📅 02:14 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98969">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">گلگگلگل دوم کلمبیا نشددددد</div>
<div class="tg-footer">👁️ 6.43K · <a href="https://t.me/Futball180TV/98969" target="_blank">📅 02:14 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98968">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromجام جهانی 2026 | فوتبال 180(𝐄𝐬𝐦𝐚𝐢𝐥)</strong></div>
<div class="tg-text">🚨
▶️
🏆
زنده از ضربات پنالتی(بروز میشه)
🇨🇴
✔️
🇨🇭
✔️
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 643 · <a href="https://t.me/Futball180TV/98968" target="_blank">📅 02:13 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98967">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">گلگگلگل اول سوئیس</div>
<div class="tg-footer">👁️ 6.94K · <a href="https://t.me/Futball180TV/98967" target="_blank">📅 02:12 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98966">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromجام جهانی 2026 | فوتبال 180(𝐄𝐬𝐦𝐚𝐢𝐥)</strong></div>
<div class="tg-text">🚨
▶️
🏆
زنده از ضربات پنالتی(بروز میشه)
🇨🇴
✔️
🇨🇭
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 1.01K · <a href="https://t.me/Futball180TV/98966" target="_blank">📅 02:12 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98965">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">✔️
گلگلل اول کلمبیا</div>
<div class="tg-footer">👁️ 7.42K · <a href="https://t.me/Futball180TV/98965" target="_blank">📅 02:12 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98964">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">🚨
▶️
🏆
زنده از ضربات پنالتی(بروز میشه)
🇨🇴
✔️
❌
✔️
❌
✔️
🇨🇭
✔️
✔️
❌
✔️
✔️
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/Futball180TV/98964" target="_blank">📅 02:05 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98963">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">🚨
🚨
پایان بازی سوئیس و کلمبیا
بازی راهی ضربات پنالتی شد</div>
<div class="tg-footer">👁️ 9.36K · <a href="https://t.me/Futball180TV/98963" target="_blank">📅 02:05 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98962">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Tw-UYc2wlPHEg0mMJGu037BZElAlApQonTDVTQmuQw3nkNcYra9V5wthMCi9fpLMeTn5b9Hj7TOqwp3CYLB9e-B2SHebmauLQW6cgbzd-N3mtU7TqtBB36JEaKn3JjQ0lTDJaYZj60BgSs7SMlz9fM4BAQSL0b4GL6yi02IogNdq9RxYI7PHtzEfDQYZyKtrkT8_KNZxLYpisvDMPdl9Hdi0LoSqX3N-z5f-Fu1cDpajUqo-bm1n8NQyfFS34qm_u_emGdhCIF-jw9xxegLXGZWVz8TIiJOh5p0PDMmNRMLIjxuKBBuAT1lahV2YL0aMjB--DN5dt0Z2JGd-i8bkKw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کلمبیا چه توپی نزددددد
😐
😐
😐
😐</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/Futball180TV/98962" target="_blank">📅 02:00 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98961">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">🚨
🚨
🚨
#فوووووری
؛ گزارش‌های محلی از موج جدید حملات آمریکا به سیریک
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/Futball180TV/98961" target="_blank">📅 01:57 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98960">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">🚨
🚨
🚨
🇮🇷
#فوووووری
؛ گزارش‌های تایید نشده از آمادگی همه‌جانبه نیروهای سپاه پاسداران برای حمله به کشورهای عربی و پایگاه‌های آمریکایی تا دقایقی‌دیگر
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/Futball180TV/98960" target="_blank">📅 01:50 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98959">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">وقت اضافه اول هم مساوی تموم شد</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/Futball180TV/98959" target="_blank">📅 01:48 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98958">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2e61389fce.mp4?token=A7sxW3Qz1nb4BKmqwH5QNoxFEwbvrxTXVdhX98ixuzqpO0XvoKs_Eearf-EtOnrikt7qUkYq__-eksHAVCqK8JvxUs4PFMYup1nGwZQWx5El192UabcF-KzNQhEn2opC2DdLAzdUl7CSSPUs0mSnXqGFNskN7Pj3xUfGNRh2iXzM84FaVnzYx-uOXShyux_ocAYZzecbKZRpfQnzli6J2CJ8sg-VQxXQoyakHylpqh-sQbF3hwRO7eui9GyzDYnYw7f9Op-0WeAve1E8rvHByua_2otK046-COobRS9caLCsn5RHrsDF52bb27nN8ntuGMYiQxWoUO5MicAppg9uf0OzZAhfiAaopIPHd3jC5WG2mt9s6jOYtjhinIBcdH9VuzRheYinem0laId0_jsbbU8aY76tw8WEh3OF0_HVuVKwqtt0qOYhxvFSDrfINwLb1zWD4VkLw8NbxmJFvlbXz19K3IT1kRE8T31uAw3Kfi_IfMXcQfWj8MGi4tB5EgIYRFZEeMvfUL8gZ96jzqNTRkeSZCvnCT2FOhb8-v_yTbEPDExQIWLNYiz18FGD1vP7G7uFIqvecUM3CUNCRXyyJQU-wWyZpjr8jENaMLolXgV13kiN46JNx-NAlPxUUpS5EksOyvxiRtaofNvWZEGeCCtcqCMRn3W6W3iAuACqzjQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2e61389fce.mp4?token=A7sxW3Qz1nb4BKmqwH5QNoxFEwbvrxTXVdhX98ixuzqpO0XvoKs_Eearf-EtOnrikt7qUkYq__-eksHAVCqK8JvxUs4PFMYup1nGwZQWx5El192UabcF-KzNQhEn2opC2DdLAzdUl7CSSPUs0mSnXqGFNskN7Pj3xUfGNRh2iXzM84FaVnzYx-uOXShyux_ocAYZzecbKZRpfQnzli6J2CJ8sg-VQxXQoyakHylpqh-sQbF3hwRO7eui9GyzDYnYw7f9Op-0WeAve1E8rvHByua_2otK046-COobRS9caLCsn5RHrsDF52bb27nN8ntuGMYiQxWoUO5MicAppg9uf0OzZAhfiAaopIPHd3jC5WG2mt9s6jOYtjhinIBcdH9VuzRheYinem0laId0_jsbbU8aY76tw8WEh3OF0_HVuVKwqtt0qOYhxvFSDrfINwLb1zWD4VkLw8NbxmJFvlbXz19K3IT1kRE8T31uAw3Kfi_IfMXcQfWj8MGi4tB5EgIYRFZEeMvfUL8gZ96jzqNTRkeSZCvnCT2FOhb8-v_yTbEPDExQIWLNYiz18FGD1vP7G7uFIqvecUM3CUNCRXyyJQU-wWyZpjr8jENaMLolXgV13kiN46JNx-NAlPxUUpS5EksOyvxiRtaofNvWZEGeCCtcqCMRn3W6W3iAuACqzjQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
ویدیو دیگر از حملات دقایقی‌پیش آمریکا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/Futball180TV/98958" target="_blank">📅 01:37 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98957">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6d512a0d2d.mp4?token=YEgRLWVBPpDsJYV-lIblLONVyIf9KgbVZhceeVf84dLRrydAEjNjJLF-Pol8CFzgnwC58Zixdl5slJH2l2-myb0O0fHwNgddaTulqQxGQRst0EA0-TsxXKCk6lt7CD3MeBEnviEXEDrbP8E1MqLBhQp3pFVj2I9QjGS4uImQp67N70tu5WX5yoYsFH0gBziG9Sa6CNoYcroQltPkA6qoJH2DF4RFykERxpdLk1cc4DgKO3LVRJ05WxyFeCEzNMqVfFPh86SexdPxdzkqhhFhk4fFU6vYcY0aMV2mqYGjcJYi12osK7ujMslXr2NarU-1KuFzMl7kf0Ruct0n-UeRPA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6d512a0d2d.mp4?token=YEgRLWVBPpDsJYV-lIblLONVyIf9KgbVZhceeVf84dLRrydAEjNjJLF-Pol8CFzgnwC58Zixdl5slJH2l2-myb0O0fHwNgddaTulqQxGQRst0EA0-TsxXKCk6lt7CD3MeBEnviEXEDrbP8E1MqLBhQp3pFVj2I9QjGS4uImQp67N70tu5WX5yoYsFH0gBziG9Sa6CNoYcroQltPkA6qoJH2DF4RFykERxpdLk1cc4DgKO3LVRJ05WxyFeCEzNMqVfFPh86SexdPxdzkqhhFhk4fFU6vYcY0aMV2mqYGjcJYi12osK7ujMslXr2NarU-1KuFzMl7kf0Ruct0n-UeRPA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
ویدیو‌های منتسب به حملات آمریکا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/Futball180TV/98957" target="_blank">📅 01:34 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98956">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">فک کنم اگه هرشب با ۱۰۰ هزار تومن میومدین چنل بت ما ، شبی بالای ۲ میلیون سود کرده بودین مثل دیشب:)
😊
😂
میگی ن ؟ بیا تو چنلمون و ببین
🔥
@FuckBet @FuckBet @FuckBet @FuckBet @FuckBet @FuckBet</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/Futball180TV/98956" target="_blank">📅 01:34 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98955">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/oS9e4KiNZJyk1D_HvsaiFgB56ySXMFvfqvq0_i37lb_33eHi0Hr8xUZNWdBdusJRS4umQ2wfSQ4XcVQ2gqG3EyFNqS5d5F8FW4dPSm-IQd9jWOk8c4H9xPtnNV5oKLjZMZs7c9ufhU56Q8SMH7eX36O94JTUhcrfaaYzauBIuL5hrlWjXexj8YJJtUbV4G-xFFo42-d7K8Htw8XXv0HhBPp3d32JeVy6ClXZlKIBMHgY3xsqVoGpE3gFymkE86iGYjow7OxS3pTYvU_7Aa1nU5qqHdh8yiuUoRffPC1mrTOLlH7RSI1w3-NdLM6aSfIQR8mrQdiI8ABoQbdkH1dXRQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فک کنم اگه هرشب با ۱۰۰ هزار تومن میومدین چنل بت ما ، شبی بالای ۲ میلیون سود کرده بودین مثل دیشب:)
😊
😂
میگی ن ؟ بیا تو چنلمون و ببین
🔥
@FuckBet
@FuckBet
@FuckBet
@FuckBet
@FuckBet
@FuckBet</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/Futball180TV/98955" target="_blank">📅 01:34 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98954">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">🚨
🚨
🚨
#فوووووری؛ سنتکام: در صورت نقض مجدد آتش‌بس از سوی ایران بار دیگر به دستور ترامپ محاصره دریایی ایران را با قدرت فراوان ادامه خواهیم داد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/Futball180TV/98954" target="_blank">📅 01:30 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98953">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">پایان بازی کلمبیا و سوئیس در ۹۰ دقیقه
باید شاهد ۳۰ دقیقه کیری دیگه باشیم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/Futball180TV/98953" target="_blank">📅 01:25 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98952">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">اینقدر بازی اونور کیریه که اخبار جنگ واجب تره پوشش بدم براتون
😐
😐
😐</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/Futball180TV/98952" target="_blank">📅 01:22 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98951">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">🚨
🚨
🚨
#فوووووری
؛
سنتکام: در صورت نقض مجدد آتش‌بس از سوی ایران بار دیگر به دستور ترامپ محاصره دریایی ایران را با قدرت فراوان ادامه خواهیم داد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/Futball180TV/98951" target="_blank">📅 01:16 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98950">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/s3b48AAXucW8wOyi1KSmtmTwwdXBfmnPHHSF2Q8jYZi1suoIepktmlqSfX2Mo2M4i7YJo-CLNLw82t5s5zVPwf1EvrJHAzE7ySMWWhJPrsQkK5-tB5sNs9StKM10BdRTi8EkYlhjNeCug13wOJ4cAK-U9WFUgv8jRoeyRYwpSZJTkaqA2pjx0R-S_tXYKoAWoED8_IDENwsYZBX21hVOfoUwFQ_AdxaBuRRu6kkHZgc4h6Qyn3NdN5xgk3O7is-Wr9Jko0Z9HrxppORj2sUbRWgsYXniw5J_f9s3p_hrm52Er6NIueXKWYGcFprsURS2g8eq4xk2YPG6sUfyvYLvxg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
تصویری از حمله به دکل مخابراتی سیریک
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/Futball180TV/98950" target="_blank">📅 01:10 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98949">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f434bf30ec.mp4?token=DjxjB7PGad0g8dJ6qy9_pbVvroup26pgc3sNHwYqdKfShvOorCIOV6pXdeomEtra9xW8lL7wNLOQD1_05Li81XQEic8EkOl1hHRO8TGHcLRiIKUHUYUwzcTwaI6outIpiktFWTKcn-g6bcHjTLzBAHCvffKEdo9c-ufzFx3Q5bdnvndMsIUwiL_ghukEVAR3hZcycsMwb5S8RZcdHNPxjhYJf_Car0Zok5-rhijaSNC8--0M6z7TzhxC6WU6k1b4f7QisKIQfqxzrnecjVqdaW2Bo10yNff0HoFjR3Q-VfV-HQfC6gwTLQYAQ1ZCPCbLH_IobSEh8HJeMiBuUbKGqA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f434bf30ec.mp4?token=DjxjB7PGad0g8dJ6qy9_pbVvroup26pgc3sNHwYqdKfShvOorCIOV6pXdeomEtra9xW8lL7wNLOQD1_05Li81XQEic8EkOl1hHRO8TGHcLRiIKUHUYUwzcTwaI6outIpiktFWTKcn-g6bcHjTLzBAHCvffKEdo9c-ufzFx3Q5bdnvndMsIUwiL_ghukEVAR3hZcycsMwb5S8RZcdHNPxjhYJf_Car0Zok5-rhijaSNC8--0M6z7TzhxC6WU6k1b4f7QisKIQfqxzrnecjVqdaW2Bo10yNff0HoFjR3Q-VfV-HQfC6gwTLQYAQ1ZCPCbLH_IobSEh8HJeMiBuUbKGqA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
🇪🇬
اشک‌های زیکو بازیکن مصر از ناعدالتی داوری در بازی امشب مقابل آرژانتین!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/Futball180TV/98949" target="_blank">📅 01:05 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98948">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YDpldXeWbztMLXOxeyFZBXR94sk18rGXE-V07TgbsYDWQPScP0I29tLJGjWtb8aIE7NStb7e9zZxAJ0le96QF3B_FJpteGGLMG0i0aezDNkT6VxiCXhXaVW9itb8ja0BpbBEC40Gwne37DzCM5UFhaKAZCkPRlTiLR6YS5Xz2TNUnSf-WpwGSLxNABopr7dd8WVuBW9FX45WGHX7hmNRk5pPkQR-ThnRICKZJziBAvsCrYnNpkPRAceH0bZ15TEpFxqw4rXZuIni0gD2WR3YThwJ0WoUfbdL7cVLPshbDOT7a1zbbV13-2UY7zpH9ZAuBB_PuKSazl1zGBaRGGMjyQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
سرمربی تیم‌ملی آلمان درحال تماشای بازی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/Futball180TV/98948" target="_blank">📅 01:04 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98947">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/b41hJD7I5fznITkd8MgOAvjD4IVJZ0RXQvxNV9OC6K4GKkQrxColqT5xxs1OD_EnxiqAtmB6pDhz_TaWfj11KbvM6FrmnfQXOkJ9SMawVz8oE4m_uPUu7nYlQ26SZX9IwHCxukuT88CICIgNW-ZbOZqv9IjM1nw5c10MKCVG7X8bGSkGO2LV_mlK6Y3hk8zyUXCpB0Ky3BVukkKa2HVVQaSMVV7hq75u02Bj2wfnU22TBjlbHCHjXT1rq5Gfdu1MsvTH8c3IKYGFomdOYTgw6rn4R_LxTz8rgIc10POyP4DZpqLC1VZzb4WT8m1mwwEF7BjtOPf-S7-s_yOniqfI1g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
تصویر منتسب به شناورهای سپاه در سیریک
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/Futball180TV/98947" target="_blank">📅 00:59 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98946">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">🚨
🚨
🚨
🚨
#فوری ادعای سنتکام:  نیروهای فرماندهی مرکزی ایالات متحده، مجموعه‌ای از حملات قدرتمند علیه ایران را آغاز کرده‌اند تا هزینه‌های سنگینی را به دلیل هدف قرار دادن و حمله به کشتی‌های تجاری حامل خدمه غیرنظامی بی‌گناه در یک آبراه بین‌المللی تحمیل کنند.  حملات…</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/Futball180TV/98946" target="_blank">📅 00:55 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98945">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/G8QMWRRh5h2TeLOVMFq5n80cm0ecgCVHuUen3Trf6L1e9eLBMg3NPX0bIbYFZ3QQl9Vhgkpb_H6aHjzpxN_X91D5lGJP2G4lGCRH5I9lnF8xVESF3XR37_XOvEiB2UFZM0DMA3JKWhAwfsln56OJtGF3I8hxx6ROvfM74Pe4bG1p9Q09158lz2sm5VpTuHQuuQY3yGJ1LBOjSl9taGftHzU8K9Tng3oUQhT_mPYrccddUJ3vq3-ytxoR9keybWXAWk6ovof_lzNuviGtQoV8uH_l76slr69sKiuxrxzKY0OV-CzdZeu1X1bY8VMUcJAsev9sxUu3Bz80qPKIAB_OUg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🚨
#فوری
ادعای سنتکام
:
نیروهای فرماندهی مرکزی ایالات متحده، مجموعه‌ای از حملات قدرتمند علیه ایران را آغاز کرده‌اند تا هزینه‌های سنگینی را به دلیل هدف قرار دادن و حمله به کشتی‌های تجاری حامل خدمه غیرنظامی بی‌گناه در یک آبراه بین‌المللی تحمیل کنند.
حملات ایالات متحده در پاسخ به حملات ایران به سه کشتی تجاری که در حال عبور از تنگه هرمز بودند، انجام شده است. تجاوز آشکار ایران، بی‌دلیل، خطرناک و نقض آشکار آتش‌بس بود.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/Futball180TV/98945" target="_blank">📅 00:50 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98944">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/101717de02.mp4?token=V1o0oOpJZvC3kxmPEtlnvNQdOWtTeVHKFQSjnXkSmvZUS4lBu-9ZgklW95TOpk1yh-w5hyXA8IhekolvKyzCRWZ31QVohV5it-wt-QzFD5-F2xH_htb4yA-cTvjMnpHgZp98MjhqqBu4rBhVHLAe35tne91gLaDcw--HTtXCWPiPXhW0h_rTkIv_n7VZzdCLD8kjolkxIF5XgUPrJYvSAOYEzoBnZctXr-tf4LyHcPzt5q7ujJFRjvv6SOccZJg0oAP4TsPyVH-sxNRwDEwxqsFRHPRlhUfL-TV0jpLFQbeEuq-Lf9yntRzhcPFqrEOQsevUK5z-N3boXAMHiL9klw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/101717de02.mp4?token=V1o0oOpJZvC3kxmPEtlnvNQdOWtTeVHKFQSjnXkSmvZUS4lBu-9ZgklW95TOpk1yh-w5hyXA8IhekolvKyzCRWZ31QVohV5it-wt-QzFD5-F2xH_htb4yA-cTvjMnpHgZp98MjhqqBu4rBhVHLAe35tne91gLaDcw--HTtXCWPiPXhW0h_rTkIv_n7VZzdCLD8kjolkxIF5XgUPrJYvSAOYEzoBnZctXr-tf4LyHcPzt5q7ujJFRjvv6SOccZJg0oAP4TsPyVH-sxNRwDEwxqsFRHPRlhUfL-TV0jpLFQbeEuq-Lf9yntRzhcPFqrEOQsevUK5z-N3boXAMHiL9klw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
تفاوت توجه بازیکنان آرژانتین و پرتغال به دو اسطوره؛ یکی محبوب و دیگری منفور و مغضوب
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/Futball180TV/98944" target="_blank">📅 00:44 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98943">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">🚨
🚨
🚨
#فوووووری؛ شنیده شدن صدای انفجار در جزیره هنگام و سیریک
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/Futball180TV/98943" target="_blank">📅 00:42 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98942">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">🚨
🚨
🇺🇸
#فوووووری؛ آغاز عملیات شبانه ارتش آمریکا در جزایر جنوبی ایران
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/Futball180TV/98942" target="_blank">📅 00:39 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98941">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">🚨
🚨
🇺🇸
#فوووووری
؛ آغاز عملیات شبانه ارتش آمریکا در جزایر جنوبی ایران
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/Futball180TV/98941" target="_blank">📅 00:38 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98940">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vEIbOCqXS3xNPAxAsfaCz0WB_zsXV-ztlzNTn1BJzlSxEJybz0KeJ4HdfDJJhpsEVAiJgIRQJcrW6wAb5lpU5ZtRVdMKtuHWVT6W2K2OQpQ7cwfKOKZDmhdtRuJmbh5d6GihW7AAQYLaM2TSzwKIZEnPdKvaIX7icDwXPHGyovPtcucZc0v466h3n-zNCIuI7PTlFTASglEBoA_ClThO6HXdlK8JsMhpbkLhF5dVD4qGdTlBt3DxkZ09dvR-UHM6mFcwRiA3a3l9JE4HsEo4mS_wSGt6lTn2sex0bB_fpUysymib9dCegUEZU6nyzxvDEThJLmzJd4rY1_n7uOMhEw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
👀
🏆
آرسن ونگر: «هیچ تیمی نمی‌تواند در این جام جهانی بر فرانسه غلبه کند، فقط اسپانیا می‌تواند آن را شکست دهد.»
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/Futball180TV/98940" target="_blank">📅 00:34 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98939">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/07e80f1162.mp4?token=usr__-_Vyz2K_lJBhtrc5kflVRVVPbZZCFicxiUDF1BdY9Q9HViIOEBn8Av56U769CJ7cnzimPC_SdQ7DRMKnibLmo7iF8o3CiFMy8l3em46HbjKlVwI9t7UrWCmFgLyffSxOUUUvpmGlodJbg3ObTCX2yINMFcc4FFsUOjovRt94gUvsD8AjzFUcqi3gJV1EUeuO0V-vAKhLS9-LLaKPISDiXMtUKN39FuPi8Fqn4CB0abWxDHDAiv_lIn2xXL5pOQEwzF0byor7b7tQT-deTW6QaemqUiREsnb-aq1612kZJxIttwnl65XouqfKsWVjoWrdJL003iYNbj1BwNzlQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/07e80f1162.mp4?token=usr__-_Vyz2K_lJBhtrc5kflVRVVPbZZCFicxiUDF1BdY9Q9HViIOEBn8Av56U769CJ7cnzimPC_SdQ7DRMKnibLmo7iF8o3CiFMy8l3em46HbjKlVwI9t7UrWCmFgLyffSxOUUUvpmGlodJbg3ObTCX2yINMFcc4FFsUOjovRt94gUvsD8AjzFUcqi3gJV1EUeuO0V-vAKhLS9-LLaKPISDiXMtUKN39FuPi8Fqn4CB0abWxDHDAiv_lIn2xXL5pOQEwzF0byor7b7tQT-deTW6QaemqUiREsnb-aq1612kZJxIttwnl65XouqfKsWVjoWrdJL003iYNbj1BwNzlQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">Legend
🐐
🔥
🔥
🔥
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/Futball180TV/98939" target="_blank">📅 00:25 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98938">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">پایان نیمه‌اول بازی کلمبیا و سوئیس</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/Futball180TV/98938" target="_blank">📅 00:20 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98937">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HMG9XWLP524ls80fbwaC_d9MdeBzOYPoyvBqU2pAa_uG3iQ8RxY7_tp-gA-Lcru1sJZkJRfd1_96gaIqy7xElX2qu4x-GxiyLbMOGigHb8ppYj-B7c_OEmigz6377oLbEnLxazbro3Isng2yBBgXtlntKpbntWRvuMpMJYr3zFURYXCVQRp5U_U6eK9l3De6cPPgZ9iqwAWijPpAR-N9HV64CEtLzaQG0v9XI8GBUWw1IBqtmwyI059vKglMjL8-cfUgNc7vWSRZoIlz-EjlMQ-LXjjscmoUt81eFwAviPlCMuFTpEfgqWPq6B-pIfrN1iCEEEUt-hYTi2WqQ90XEQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
‼️
🇪🇬
#فوووووری
؛ جیانی اینفانتینو پرچم مصر را در جریان مسابقه بین تیم‌های کلمبیا و سوئیس به اهتزاز درآورد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/Futball180TV/98937" target="_blank">📅 00:13 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98936">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/df3e3abdb3.mp4?token=jc0dMO-bAc1qJdxam44VIcBTwwlHvKcFZT9tEWYqKoIfidNYXT9bTUfRe4unBXYtiDJnPDIm3I0BFZNj1M9FxisoSeESXLeaG2NHPcyWMAvqePStGt5dHqTOqe6EmwZTZTcKldqaOc5UxaBhAi4CBseBi_GDp4zzH165qWsbNRMa1FkRY-DjXeG0ECawez6Ia6UHeGLzl-DXqx-k47R_qQ2Ty-PO1QFjepi94WGcAJU9czpcV3PZFlQys_5UwnNDOiVkQQBlQPopHmeLpRdr4k9P5u1ZoAXnFTwpCJXX70JW1g8rzgSU9W0R_FR09O_Y0R-JCJDGLSHnwBfNGJK07A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/df3e3abdb3.mp4?token=jc0dMO-bAc1qJdxam44VIcBTwwlHvKcFZT9tEWYqKoIfidNYXT9bTUfRe4unBXYtiDJnPDIm3I0BFZNj1M9FxisoSeESXLeaG2NHPcyWMAvqePStGt5dHqTOqe6EmwZTZTcKldqaOc5UxaBhAi4CBseBi_GDp4zzH165qWsbNRMa1FkRY-DjXeG0ECawez6Ia6UHeGLzl-DXqx-k47R_qQ2Ty-PO1QFjepi94WGcAJU9czpcV3PZFlQys_5UwnNDOiVkQQBlQPopHmeLpRdr4k9P5u1ZoAXnFTwpCJXX70JW1g8rzgSU9W0R_FR09O_Y0R-JCJDGLSHnwBfNGJK07A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
🔥
لحظه گل‌دوم آرژانتین و واکنش اسکالونی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/Futball180TV/98936" target="_blank">📅 00:05 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98935">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a31c10f53a.mp4?token=e-g9Zj6TioOiWqfb1vjTNjygPYvcwSGVekcLRVLV56xC8DY9zDp4vOJl9U15iflAbLGZ4f4b9RaiBF3Nn07sEbOqav8Bvvas98AMO011dpA5lhvLGoPNTOgEh0MJwGjmo2D9ze3MHofMU3s8YEy8iOCew8dzPpLHlmurTLfDcM_O5-fYmokldnkTrLHXxs7yGM8-ZL-2io2SpwbEH34w5JQaU_TqYe5ulOt0xdM36hCf-tQ3PJD6J7twwno24rdKyKHb8sVebvCflsV8fTTmW5LkZp01pYN_sB0IEq4r-ZnynhRoLlsbuSQmvXKcPN3JCV8qSIRejB3ry5X0TcQ-Gw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a31c10f53a.mp4?token=e-g9Zj6TioOiWqfb1vjTNjygPYvcwSGVekcLRVLV56xC8DY9zDp4vOJl9U15iflAbLGZ4f4b9RaiBF3Nn07sEbOqav8Bvvas98AMO011dpA5lhvLGoPNTOgEh0MJwGjmo2D9ze3MHofMU3s8YEy8iOCew8dzPpLHlmurTLfDcM_O5-fYmokldnkTrLHXxs7yGM8-ZL-2io2SpwbEH34w5JQaU_TqYe5ulOt0xdM36hCf-tQ3PJD6J7twwno24rdKyKHb8sVebvCflsV8fTTmW5LkZp01pYN_sB0IEq4r-ZnynhRoLlsbuSQmvXKcPN3JCV8qSIRejB3ry5X0TcQ-Gw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
🏆
🇦🇷
وضعیت رختکن تیم‌ملی آرژانتین
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/Futball180TV/98935" target="_blank">📅 00:01 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98934">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f27ddcab60.mp4?token=Lz67vPHzJ7v2KE2IOpuFahj-_Ef8uHgiwySWlDZc0jCAHyTbIc_Io_wTzNdZyCLimDl7Ea4qYdFYYIOyIz8C5vjfyrVTDHfW1BONaloEGUZ6Cf4R_hNnpmOpypLymyzQNOvZnKBd1F07UIHeHRGXBMkwy4HZcv7x9hzoNoCkeBpGoVJdIBiui0qLXg-_P0UgOTam5KLjkNuwsUFTysBWIzGcCOZ3C8fug6_NqDsEgVNoUtNfRyOXG0ZnUFT_1DB4MgAxkwhx0XitxQxB6wgKjciHmuD_TtgET27n4owgP4J-6-hbhG_qNkEKWpEc8WwUieTiaFNzCMdiPQAB7pOLJg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f27ddcab60.mp4?token=Lz67vPHzJ7v2KE2IOpuFahj-_Ef8uHgiwySWlDZc0jCAHyTbIc_Io_wTzNdZyCLimDl7Ea4qYdFYYIOyIz8C5vjfyrVTDHfW1BONaloEGUZ6Cf4R_hNnpmOpypLymyzQNOvZnKBd1F07UIHeHRGXBMkwy4HZcv7x9hzoNoCkeBpGoVJdIBiui0qLXg-_P0UgOTam5KLjkNuwsUFTysBWIzGcCOZ3C8fug6_NqDsEgVNoUtNfRyOXG0ZnUFT_1DB4MgAxkwhx0XitxQxB6wgKjciHmuD_TtgET27n4owgP4J-6-hbhG_qNkEKWpEc8WwUieTiaFNzCMdiPQAB7pOLJg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">😍
🇦🇷
احساساتی شدن لیونل اسکالونی بعد از کامبک معجزه‌آسای آرژانتین مقابل مصر
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/Futball180TV/98934" target="_blank">📅 23:50 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98933">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/awq8j6zWuxrxfGUxeOUNArLWA0WKfYvOSYi73fZg1JrHLagk--Ll2mgTWXFy5qlW5_ax8UK8zVl1gIPCNHKmbfS8g1GGFckPOBaplG5YzudAANem3mBUUjh0hev6Wx2GkA03jlcMUrfa2DaQYIt1V50kMJTIdm83HXhTQKHZET0a3FwmFB5QwbWcKyfYc18BnBcdLuhAW0cYNXuFsVoPlsDGcWo_5wl0-5BXnaZjeiJtSkYiA5gwj33j2r1AK04ygVKw7BWTe1JtQ_6SEmBFMtjdObd1Hl9HF_Jvs6owyllueBr1fTWATTn5_fzxHBCXlKYRE5T0RUyjENKH5LfeGw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بادوم زمینی استراحت نداری تو
😆
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/Futball180TV/98933" target="_blank">📅 23:47 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98932">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rU4w6oZ6UKLxAzg7lVx0Pti8k1_Q7PV87C1ZxPOCwFo2bQllK_-1sT5nriqgfgIdYUFPtePN29VO1VAuw-evhq-OP6ib2VBavZxMlTO2mMSuaMEyFQdfsiAxbbHU00eVlZup_iVSmpTloEqDtDIj1kiPewg93jyaUdyuw1DZt4QZQfR-y4Dz_7eESaEYbVuIqnMheC0FiadiedHJtGqcGRxVYPRQccDruFh8RozgDJVpwcfLGtOi7nCGdio8XGRl9Cs1K0SJCKBRaCc4JyVGC46fwIgFspqfzL9oJg3NA9pP0I4_MXxRKu82TGwnUsirzMkwVi9jq0haeZ-uzL7KeA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یه عشق از چهارتا عشق همچنان داره ادامه میده..
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/Futball180TV/98932" target="_blank">📅 23:46 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98931">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">شروع بازی کلمبیا و سوئیس</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/Futball180TV/98931" target="_blank">📅 23:30 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98930">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/slsRG9oCbKERj1j_oA36krXbTNqdm_tfLfmbYdnNsO8cxA22E6msoDSSQAAiOZ61Xf1wbRrph3LTo7OgJ2NwQncxelRV6RpLtR2mVbWSout363bYkUWyuG2CA9DqkO3vAmvCEvVhurqQy6pTfBd4kYeyoeo59gL5Ei2AUqFux5N3iKVmsILd62mTrkcNkc44QxAYm2AZ-5YFeQRiAtJly_0IENzhY6xnEPdFiqUKOXBJrYseUmtisgRJDjL-8dTc1Y9NszKnWGHkFinEljUOSRteU-O771M7jX6pJwDgL5pDVIYwdGRB5acqOpLOFZBDWajgGoKaStlxT4BVR8MNFg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
اسکالونی
: همانطور که لئو در قطر گفت، این تیم ما را ناامید نخواهد کرد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/Futball180TV/98930" target="_blank">📅 23:08 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98929">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/urc4DvLQ1fKX0q7iPx8nYZazZ2Hfczeh0jMWVZSHpfqvbvDBHrAiXOzmLakmidnA1GmuyhWJHG5vKJA7DijFbgba7YDYmgDIWRXTojzt1se2GLhcoGWdLOOz8m2SReCEu_dxTiMWhd_qGfeQMAz0OuB8ZykNdL3x2KMaFCLElUUesVuGWFnqHnW5ay0ccQZ3hdvPPLlUvfGZpkv_w7PeSDSWnyrlUioI6Ox0BdOn_Zqjc5sLlZeOIql2eafi9IAbRxq_IJuqtm75Aw4KqWVpAGjPO2x9ZoMp8o6NbixKyj1pTSYH-zUjNt5f_pB8V9xe2ydI2dzYJDLDBMmxWZFs6Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">روزنامه ESPN از مسی با این عنوان استفاده کرد:
"تنها او می‌توانست این کار را انجام دهد."
فقط او می‌توانست این کار را انجام دهد.
🥶
🇦🇷
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/Futball180TV/98929" target="_blank">📅 22:39 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98928">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">‏
🚨
🤣
کون آگوئرو بعد گل تساوی:
‏"نمی‌دانم که آیا الان دچار اختلال در ریتم قلب شده‌ام یا نه، اما اگر قرار است این اتفاق بیفتد، بهتر است همین الان اتفاق بیفتد."
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/Futball180TV/98928" target="_blank">📅 22:33 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98927">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aSLZpLZ8R2YgcT2puKt8oqVz2mSkrtq10vzNWF9qAo6zRCffgz_PO7V2fYyWgX72gr0Gi1wjPHBkpJqZJsiXQMd3CbzyLHOnhWgQPU12pw4cePaggqdPSx7yKGsqv6jV5A-42O2sB2WatzDcUo-zY-S-aNjVKvPsRhojhUXn-vDAwgEs5JQeL3Db4q4UlqI2GhjyyX8nfzZlmhk5PgCGxNpXy-fIXZwd_2E7RK7zWJso7i5uA4iO1ESKVY1Ei5M3u62taDXW2CRhO7A4r5ou7cF4N24QRzzNjfn317ubx4zhVQI5sS1RMUqp_hJjQYhdcuMof6S55qV7EEsY4MCjQw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
📊
🏆
گل انزو فرناندز، گل شماره 3000 در تاریخ جام جهانی است.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/Futball180TV/98927" target="_blank">📅 22:30 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98926">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">‏
🚨
🚨
‼️
حسام حسن، سرمربی مصری:
‏" ما بهتر بودیم، اما فوتبال عادلانه نیست. ممکن است آن‌ها بخواهند قهرمان جهان و مسی همچنان در جام جهانی بمانند، به خاطر مسائل بازاریابی."
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/Futball180TV/98926" target="_blank">📅 22:29 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98924">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/GZnb7DB3-o5Rc_wGTpRtNthdJeMYKpW792dXXbI5wKd9Gq3VgG9tksxgA9nZnWB9lfdPDy5sxmjzd935vwSy9TfSmScvgRhcndI9EyLZB68w8pvvzreuuK2pL6TVHhdk91QL0OcV8oJ-NlMBNKasMiUoNR4BCiqrh56mOhcqLfwsWZesYXaOJ3-r-05O40dj2ZPDzBjXfYatr0dCuwRK4iy6emIQJeix_aCPqDXbk15QK5T-gZ819pL1GNVf8-TZjvUUYbFLB86hLo9FYQ93ZCepU3LNZJbDnZHylSM60eFh75dqg0pjSk8az3jMCTBJtIeahV0o-ia9BW59bsDrxA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/MQKtLzxA949XqEoV5NWLWx2fAWDRx3DzKB_xepi6RotwkyW0UrxRguaIfGXGbXPwK5qMVYcH3sc877xTGjaAekPC0KZA17sL052hZi8Y1k3OMmsAptKK3-Iq1PiguE891_C3wSGKrbHs6xY-v0WuShRmrUO0EdZE10N__oXj2qk6R6kZW_oPGEjgZOoFYBiDuukwdKy6m93FKxdmMDevwMwQ-zcCUut1ICKrfKcdhuOyfzxQYEe4DgIZlUxXxTn1DtZZS4cJuIDtFnQq6X5ux0i_vTko3WuaFWDULp8RgFxSvJJR1RbBGNXT-OHNhh1O-T67BgP_8pvjCHdHV0FHpA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇨🇭
🇨🇴
ترکیب سوئیس و کلمبیا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/Futball180TV/98924" target="_blank">📅 22:20 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98923">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/e1BqA2-a13VIM7lo_39sP99URwFjXEtyCY8mPMa6H-QeXbIQ0cMJv6paSmDThYNrNyHjoep8CjPjUAuOoFsh6set6ICkq97RqzDnoJ55P-V96Oy6dDNPiv-MAwOYWXIEkoXgoA3XHMpItU4gG4BiNItbENb9i5R_2Ua7Ni194DQB_SdfxbDUTUyoBQ4Ve1mzM7NVAWimiz-pEkEIm1OYQ9v4qTnvcfZ6xOabToVc-CbS3XmEsxKRaehAYf7xbo6S1vD8A1cZceyEzgitM3COcIhNhcDq2sLZaWUppDN7DDzF_TnoPHZE8NlMRWjqZ7FKUfplqIYOxVDbvBC6awZo8w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">لیونل مسی با 39 سال سن به مسن ترین بازیکن تاریخ جام جهانی تبدیل شد که در یک بازی حذفی گل زده و پاس گل داده است.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/Futball180TV/98923" target="_blank">📅 22:09 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98922">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SrdxNd2YrkUC-LvnoaEx2HgetcISiJJP5Rpo7D-Q9US2b1yh-V_tvvuuKC6dN3Win-_1ptr1yd6cDGqB1rA_MpcuNvjxqjMNquHsjlDyq_PgB2RHiJocJt9-Ty_WiboCC40SF5BLpX6PKh5hSie1WjGpKz9Z2xuVE1ihM0oixEoyYWAJEd64GR5DUlSeKuHWYpxfaHS19cpYwGZrMvUDNQE2HQMR5A3euiwlv0Z3FfEHLLooQWu9WIq1fvxXOMNbZE635WHt0-Evg5Eoij2A3zAQbzgKg597F-2fuPbl1-otXmYvqfzWGLAT3zLe8_Gfmqfm9mLcXy2tz1vx5Pt0ig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🇦🇷
آرژانتین، اولین تیمی در تاریخ جام جهانی شد که موفق به پیروزی شد، در حالی که تا دقیقه 78 با دو گل یا بیشتر عقب بود (3-2 مقابل مصر).
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/Futball180TV/98922" target="_blank">📅 22:06 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98921">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/a9budFQNjPPgFzwpebNsoincPEnEQVSEkSkmHkRNcAFRp6GNfxFmVldIUOSni_DYNmBQTB9okH7XALxhXvJGX6uju_coT2-UBEzRaHBcYDn8xkOrrPaxZfQxsXy6T7lID22H-ndWNWN_lKzseWJ1H4yuqWaKPT2VApxxIyAlaWK2gV5d0uHpFxil0FcDK8YoT2zYREY13YMuHaWEP4wedPKq9J1_kWsI9xRYMlL-w-YTwm-vB3rbMcaiqagPHr4ac0UAllvWASCgPs6nPY1Bmm8aZddiyat3SVpOFAk7falzwcJWohhnrWhDMy_ghgxIQG-vR85S4nG7aTVddRZ6Sw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یادتونه مسی رو بخاطر اینکه جام جهانی ۲۰۱۴ رو باخت و گریه کرد مسخرش کردید
یادتونه مسی تو کوپای ۲۰۱۶ پنالتی خودشو خراب کرد و ارژانتین حذف شدو گریه کرد مسخرش کردید؟
یادتونه با ۱۰ چوب در جام جهانی ۲۰۱۸ بازی کرد و مقابل فرانسه که قهرمان شد اون سال حذف شد و گریه کرد مسخرش کردید
یادتونه میگفتید مسی تنها توی بارسلونا میدرخشه و جام ملی نداره مسخرش میکردید؟
اون الان هم گریه میکنه ولی اشکاش اشک شوقه اشک که بخاطر دومین جام جهانیش ریخته میشه اون ۳۹ سالشه ولی هنوزم بهترین بازیکن دنیاس
پس الان شماییکه ۲۰ ساله ازش متنفرین و فقط دربارش کصشعر میگین گریه کنین
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/Futball180TV/98921" target="_blank">📅 22:02 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98920">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YB-tRGIBGZwlojTgSauZsYi_DcoZyyTDhDGmsBcj-tnMVqNtbWcj8mcWKrUplnUHk1irJWnNXYze0WYFQJb22-EImMSsqsJoolJRjBGKY48kzHexdj5-D38gYEjT5YXEzZeAFhBp-ueY0VZ-33uDpRUeY-XaNbK0OPbRe-WYYkQOMMFuUHI2JdkkMZ_Geuszl-jzgclPmGtjGuumvzSOWZkNfpsVqpDDWTfJzpvM7VKIQ3Ai50zJ84Om9cmBpmtEIoKb2ZrN0rACcBfcuh-EX8jraLrW6RINQfZ-1QapW4UAAmufd2Qye6jQuCDrMM1Sa7Zcpdrh8zk8Wy8tHQVQCg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🎙
زلاتان ابراهیموویچ درباره لیونل مسی:
او به یک هیولا تبدیل شده است و هیچکس نمی‌تواند جلوی او را بگیرد. او بدون توقف به پیشروی خود ادامه می‌دهد، و این همان مسی است که من دیده‌ام، همان مسی که ما به دیدن آن عادت کرده‌ایم، و هنوز هم امروز او را می‌بینیم.
به یاد داشته باشید، او از قبل قهرمان جام جهانی شده است، و جام‌های متعددی را به دست آورده، و توپ طلایی را دریافت کرده، و همه چیز را به دست آورده است. می‌توانید به سابقه فعالیت او نگاه کنید، که بی‌نقص است، با این حال، او هنوز هم بیشتر می‌خواهد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/Futball180TV/98920" target="_blank">📅 22:01 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98919">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TVcsKhfGMRt4FCjsmI5P1O3RSEajxQPvbp3eYZTu1fLsPt5w5jmb0Vvd7aZEbB9saf-W56IpDDyCKltCoGtSjCcanh2jWu8Ejr8n4CHHivSzfmsI59ic1W-hLSvcTo9LM4321EA4Ao52YGvz-nIoIyzT3cR5IKHwbfELVM_K-1-o64TGGk8i50Ra5gq8S_EWVjqo4EbhFlm7F49TMmbz6226SVTOMB4EVcKH15DWMdIx-wRgI2a2fwMb_oR-X9Smr1K6tNJYwxQI3zGkZ8DS0sPRr5U1MnKWZtUtp4bzlhQDhukrm8DvKW27HicZqtKSKu2d1uVbRosyZr2UiIqJDQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
#فوووووری
– آرشیو VAR:
• در این صحنه، پنالتی برای مصر وجود ندارد. – یک تماس جزئی از مک آلیستر وجود دارد، اما این تماس ضعیف است و توپ دور بازیکنان بود.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/Futball180TV/98919" target="_blank">📅 21:59 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98914">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/lQhffpg5hAuc_s9MOYrh0aIyVrtgNScBmn_z6QguhW_5Zxq4-Es0kb31kck3DJOXp6UTIwo9K0c0Ukc_ZIwyntGp1dTqmMjO2NkjP51bQD8AV9k-S-c3BXw6PTiKLoRJAyQlGUJ2AgxTjgkF8zTObLjZeZUQAbQ3g4L0s2UStT0AXOZN9xEu1BkgrRO4XzcSKS4PZtegjU201lwjpeZwHtjBZonI6AhBcpsrl2AWhfm_SxtfC0OoE49KR22kB9bPdvhjiSAspzev8o5asNQHQ47Cirrsll5C2-0l0qunpmfTUuKjsANZ7YKlG_kKLtFtjDRCaAsiVvphHUQW4m8XNQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/S-6Vq2LV9rWtcLje-zwpbmyqt9AkjNTyRXDThpfxgMl0rKCL8NcRqW-uSkVALIMtxS7JDOrq3XkU8erEfoNL5XoEAc_Zz8XDmMQdIhsyJSD0o2mzmwzFUeu86Bw1Q7bPJ1qQcyXAErHvLY-HKp5uKyRDrufLBH0P1iibEFiQemGzn_A5rmKamfp8UcttP4bepVvIkyrfj2VJxvG-BRIpdCU6ZgZO3KwlPRZjIRFUadBetBruOsDyUHFf4weNPxQ14TjSf876nj0-wHmxjY6Z7akzu3i0MymMNs8_t5Do6fZdfSut6kwdki-Z0joqPsDmOm_jb3GMKrDE3ihHDADVLw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Lh9EAGhU-kauXfkJWtT_SJdxuas-vPYCYdIe_amPDhIbNiDO6v-eVOat42rk8VD9bfcMWrm9TQ4Tw22pIyA_WXcj5z6kMU4OTt2mjDa2nGiQulTnhdHXBmCdX9Lz8-ARVLeAYRUVN59ZT3hnRRpirJXIdufMShBMm0NAuHlJm3e1nEgQiI6RCyPzYDqAqBJeMNlUR8MpvPOgC_hGppVX6F-BHOp5YLNTQgwdherOhqmpWKFiklyklchqLDMZVQ1RI5EDilJGVoph7Os0KoD_vzKFk-fRHczdTZ8b9_DRd0eZl9w4a-ByUVn5a_UoS3k0MgJG1Rl2oW5uQ-sg1p6wwA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/L0K3f5Yj1Q9uG0-R2n9FChorWGMf9wj9uOMtwe8xj2RkPhpi0qyHbxt5NdXGi4FTiWb9YgidEcN7ks14NsLiVQ8o2x78Ww-PRocuLGzKHS5nidNF1jQj1kWM-6UELh61XU8braxj3yL-r1YOvnax5852f24LH9chl9JljBYp_Wviqxw3FUZ3Iq01vgNkx22l2Z1WWq1sVaYwT0dC0qpT19DHfU-tDqj3mPM9pzsDWVptFTRWCdTfx8xD_qB-WQ7iEe66x4WlmEV8tOQJIQ1S4EOD3QPVz0fuCcc77fgWGNzo9eHiNj2D-kCYHvgK6dIgms_cinZttfUXt-kVtGZdbA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Y9YogKYNFyeFsaO03iJobQqO_UYl6aPqPU7aiHwb8YZAYvCvx7FtbriLkdT4MJ3Yoeq2xaJbPiOVcGZHyEX2jXwObnWIujO7Qzo0TqJFagqoJS7UdopVOWEV_d7NkpCUfV0CmvzHTG0JbokSR4-mZMAXhofZNvp3fXEy7GJGw8mIMf41ZsaS8WmOBJZyLxVlvDFrXwDLlidYv9RcPwkije6ZygRZZhZzhqaaGN486Wo5fTB3umCLSFb-iCELngfY1fltjWgp2nls4OUGFQwsLYU4n3Ii9oh8hWSDMx6OLP5ZdIT4wctx-Nti6pijZ4Elti7Y5rhSy-S_sweakfCDXw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">تصاویر دیگر مخصوص استوری امشب
🤩
🩵
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/Futball180TV/98914" target="_blank">📅 21:58 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98913">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">🚨
🚨
🚨
‼️
مصطفی زیکو بازیکن مصر: داور تماما بر علیه ما سوت زد. امیدوارم خدا انتقام مارو بگیره
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/Futball180TV/98913" target="_blank">📅 21:57 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98912">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DbAsl0cYVlhndB6gcCOSnJxRR265XeloRByqo-DX9cYtU7zd72bLmnjArwNn4wfuo1ncen5jwfZ331HqN1trcvTwbA-x70nREjrB6hYVvi9adO8PnjJtmnHUh_AHkNYbPAxl0Wur7FTW6dYStF8bK-6Tmjc0PI67n3nW90FZY5AAyTT_eBsJYGQNk5vkgJ6CIWYdGIXLwOd3lR5ugOLFBbC7FV1SU0tW6-rlRM5HJB8qrov2w6IJCiz8GELjJhuLbvm6-wZXkWxSJ7aa0eKdMS5gWYId5R3eeNSirk3okBbzICLJ9aWxk0gcXPZ8lG2hdIQL0R07Z-vEZQyovtDk3A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اسپید بعد کامبک
😂
😂
😂
😂
😂
😂
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/Futball180TV/98912" target="_blank">📅 21:55 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98911">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">🚨
آرژانتین اولین تیم در تاریخ کل جام جهانی است که 3 تیم آفریقایی را در یک دوره شکست داده است.
- مصر
- کیپ ورد
- الجزایر
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/Futball180TV/98911" target="_blank">📅 21:52 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98910">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jLztDppCpHjX7hjTEikZlve4L23-PeCdwpxuDTyG5vMcsY6VK36CfnbLiDL78-24CNJjSBUfBLMgWAQIPvM1hTrdyLFQfIprLH4PfMZZJbEQN6gGwiyTSkAAiVxdA7-wODtmzZZEsdYFIFo8zJOR4YVIxVgDNGQJXhIygjV0VeOM38p8aaabK3ST0S67gYedGyESpCQRnhhzyXM6yIXNBjiI-8UeAcKS9i9QuAjxwi3BLTd5ce7CAJMmoNzGGOaDW9O5QCOY1Cp6OOEXvJCjY5i8LhN1DHTzn-id9XUHvui0T38qdrHVRKmwoYRyTYilrl98NvyvNK2Q4YSWzeelOw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🇦🇷
اینه فرق احترام به اسطوره‌ها
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/Futball180TV/98910" target="_blank">📅 21:50 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98909">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">🌎
✅
تیم‌های راه یافته به مرحله یک‌چهارم نهایی.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/Futball180TV/98909" target="_blank">📅 21:50 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98908">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qmRQW-AXu07IF1NsnMf-SaiakLm22a_bIPEMT25oJHasAAKcgkDwyQPvhnkD5m9filihml3ffBwaoZo6B9ppZneqFKwFIloV0X6IreBaYXDOM2_kHUU4gkTdjY87XebST9kIsd78PsC1Xvtc_78TXKJHwfy7Ekf_GFscSJ4ZMr0vN-iQQylgECusH2qDDAawEppnb38RJ38yBZRxFRhvn4bk92sxuOemgpLY6JDY9NyRhvRiPphk-xLZFR_sVdSw2-8H5uILAuNeq6QUXJJmm3GpH5NCzPX7yWVkuFlAEc7AOH6-S-lUDTjFsvQDbx9db63pavkwYtcptg75EbwdYw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🌎
✅
تیم‌های راه یافته به مرحله یک‌چهارم نهایی.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/Futball180TV/98908" target="_blank">📅 21:50 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98907">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/P5ozZDuPWUMSVh9nRZs_lxP-nd8Dtw2pbv7q_YNUOBI2ZMTrBH4JgEtma4s-sIREkapUhkjrCrYi0hBWRuyQEaV2xdiTK11eGksFytByTHvJKacyapJT80cFaLohFtWRz_R9xY-I75K3HsGV3qy1UmUFEZKoOF8bpxEhj0MS0QrB_4vXGvKZxPsftMfByg6QymElGNwPmhFfOUpH9gXqeHxXT3Ry032KHL9Cfh_x7QOa3PKVDWxM8fxEZuORRY4yWKr0GPA9QNFxW0P8a1n3zJx7MrUxExz-bx8gT1_nWtXS8rZs94T3shHXZP6d0-RrA84YNyGVVxqecjjnmFfMrQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🏆
‏بازیکنان با بیشترین مشارکت در گل‌ها در تاریخ جام جهانی:
‏30 مشارکت —
🇦🇷
لیونل مسی
🫡
🫡
‏23 مشارکت —
🇫🇷
کیلیان امباپه
‏20 مشارکت —
🇧🇷
ادسون پله
‏19 مشارکت —
🇧🇷
رونالدو (اورجینال)
‏18 مشارکت —
🇩🇪
گرد مولر
‏17 مشارکت —
🇵🇱
لاتو
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/Futball180TV/98907" target="_blank">📅 21:49 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98906">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/G9deSeFH0d8Kvf74N21HWReSs74qCux20X1Is4VyqmcoMJvCtG7a6D5lPVrs9ELoc4Wrykn5Wr_53ZGMnW0AH9wnL4yucg5UF42k5jOxZ9sU5lrePKL2RNtWH3q9PsYM0gn2XfKEkw_XZYGAIcLFoz_eWo2_S2SJGEWagGqkic9UIaUBV2qIeFruGtTRBiq5RikIJEKoYZFYyq7flApA5DyzmkwH4EpgroVGcUDGeFhIsa65mg3fdEtkY4vb2IHDe-r2HxxRm8OAYgTsv--RWIcjxh_wTOJJEVdbJoa5xc4lF47WfzwIYcy56yhiArqRE8emGPyQLqR9uVbffE1pmw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
لیونل مسی، اسطوره فوتبال، با کسب این جایزه ۱۵ بار، بیشترین تعداد جایزه بهترین بازیکن زمین را در تاریخ جام جهانی به خود اختصاص داده.
🇦🇷
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/Futball180TV/98906" target="_blank">📅 21:44 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98905">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/f8B-oLQLaIYbY5bl9dIZEeF9uY_2YsXcZfLrsfSiiLa_MfHR2db-kWE2dnL_TQhqoywJ_XJagIZ90bgHKbSFWrxwji7Tf7tioqsoaTgjtiPY1-NgRumKOrqj20MsD_O2fukCK_lkIid49osGmRyHmr_BbnUW-lJNhFAIwArqnq5PNkY-39JFoDjKprC646wdsfRG6A6CI6DRnJIl-lSokCYQON3gOBvMLwtBD7nUoaLK4eNX2S7vlZLLI1JIxAIaqw2HiAQyrC_PxJNkHIHfO7E8PnXoeJfz6tV9Y67OZCGfxUbqVQQmbmDlHoW4ebDdg8dBNH2nGCR0hYsA1uatdg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
🚨
🚨
🚨
🇦🇷
| ‏اسطوره، لیونل مسی، در 9 بازی اخیر خود در جام جهانی:
‏— 9 بازی
‏— 13 گل
‏— 3 پاس گل
‏16 مشارکت در گلزنی در طول 9 بازی.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/Futball180TV/98905" target="_blank">📅 21:41 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98904">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qhjSGUTeWV278OAo_WytSg-gJVZCBzM1JDi_RjRJskNaCKKIbkL7TuBzkdrRqBiEu_EaEz2W8A9673bluYXFsH9EYVyyb5LWW7OqY73fqGrYIcInGPus_F4vEJpx3J1UQ41hB4cE4MT9SxvnnCmgPaVsXIpff3Bg1Om509ibW70YJ_v0GnxDBiM80OIB2BtnUOwZ1CUgc9yc5jqS6F2vvEBOnaXSt63wWqRXnuXR-O_1u3iWefL_JqMXoG_M6BuTnzwQbxQjAA9QLWEW_M7Q7ykIKUmuHFj4_9TJuiSTK_xfNGHltU6LaAcWAi5ELdfjTXYOdnhz-WmtCPUqcNfX7w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
افسانه لیونل مسی، رکوردهای خود را به عنوان بازیکن با بیشترین مشارکت در گلزنی در تاریخ جام جهانی، افزایش داد!
😳
💙
30 مشارکت در گلزنی در 31 مسابقه
🇦🇷
🐐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/Futball180TV/98904" target="_blank">📅 21:40 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98903">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JjARa5DqMZP3wJH7qFFYkWd8VvbflOnU1Cry9B8HfZg8acexWxI8R4_c-YLknxujnJ9CSMc_EM0NqeIFKPPlOilqFhdM5n-zMYgnMJyxi2dTvCbK1P6cFfLrBIZ63jGrrhF4wQ89TbWEzk8gy_MdSxqa3LZqnXnVc3D6EEMd8ulkIolFbsO99Uc9JVBN6xHOTAZQkMYG5eBzHtlOASnEHHg__ODqnKlC8jlIA9QoGJNZ8dmWD45pW8AkiAXil1IvW8mOZRsQFmjTbd384Ccbuhm-RIKbkOs-bh6Z_MJyO4YZJuU2xCF1YQ-TqVJT1kOJ-kgd__NxI61jJ1kcmb7CbQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🤣
🤣
🤣
🤣
خایه‌مال باختی کههههههه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/Futball180TV/98903" target="_blank">📅 21:40 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98902">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/C8LTTIh3FC2DttCva8ymovO0_IPyzr46B_ZQW3FI7eWGftgCoxRmOv0J3oD3vgfd92GUq5k0JeJA7Pe0gzyesuX6fW5c7sSnoOBIajdiYOyPxk0hwlpyF5FXNnYe8u427JeBQX9LpkyHTYXrWmQZ0nSLDLBgkOLRCIHaa8L1yVoYPJKp1yGxLDHAigGiSIAHmTVAshv02aKJh0BVE2ILI9YqVuIrpZUj1hqXwQCkiiCwBs1vdNRT0S9dk00abBB5V3HjgrR1UU4xU5xi0a6cTVFMNKy0Oz18oxmxCtXjHLQiFq18SC43F3vMf0BVFEts1ZA-Dscad_BB84EWVM_VQw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تاریخی
معجزه‌آمیز
افسانه
🔥
🔥
🔥
🔥
لیونل مسی، بهترین بازیکن مسابقه.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/Futball180TV/98902" target="_blank">📅 21:38 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98901">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hIpvXqD6kHvVHGQhjaD6kcmW1uWGpaEPGWVR8hsXNnxrlUE_U19H_tGGNzVmnZKmcLaEiWr-1NATpUodjlBLWD04fRCx6bSzBylZ_ikQrNeJYpfq3cjBh3e2HNpssbVraj5cRMGZ8ZjnaE4qgYF-F0bWvHZbqz1ynl0gc8K0a6pzWshvk0z_u-nwQ9ZXD96-B0rfIRKprearh7LM41Qc3YLFroP-jhXTD2YDQxSAiP6-0oiWmhioVaHhMA0wN7okJqCkx3kisSF1RaeMO7MQjskoiVp9PLxARYJqSl3ijhGgyWVfJBTvM7wI1PvfIMKW-sdOmjMdFJu8-xQaSuwjtw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🤣
🤣
🤣
🤣
🤣
🤣
🤣
🤣
🤣
🤣
🤣
🤣
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/Futball180TV/98901" target="_blank">📅 21:37 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98899">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/UMSt_4Oc4BpBcmT1IqlL3NndESMndpTd5y2zeaICYL0DP4a6zud2puTLFXT6mDY-F9xWhmfrpMvPfAUozNacaAaFyZImfDkuNuoTQtajOo5aDtVPPCqAa6DTlpu48rDIt6n4exhmD8_IeB9tpM6K4lXafbDgJhVrQa0FC_FFLfjCBMeV1iyJF5lzShm_uR8mSbnWizmuBEINUj55C6eGG_WKTLwu0kyunH40nCmN9zLlz-lSkZE1UQ_7noByWZwpLRuh0A3piRrM1VOIMZ9m1Y0AV0JpbvUJ-6sAUVTBNACCk_cXnKk4Z7FA7uAsQs0h17VxRogOFCBYiRJm-htOYg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LtX_sIpeYQeKocl7oBHqhVCBgVlXJ5ZsPuEC0wcuLwA4t3c731hf5bdetEOye6LINGVdkGdGM3zHO05c2IwZebSvJ32T7opgZ1p7Q5UPbI5iI_btmorkrVbcc4NUXeut-qU-IpYm41aG-ja-Yz2CQBMj-yx-Mt2PJoyd92FoGHMvJe0p7TSDEXo6eDN769jTGspUFl7tI_SyzQuTrNe1okaFONBnN9lBzc7kD_Tng8_CJHUaK0uJ0L3zyKFf4Z8x1ReAJxUQc3aD-DnbuVuin2X9tKB5ymkMUTvN1BnS5OU6EMBHo5fv0TVlLKYycf2nD0srpjMkheZM-v2Sg103Iw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">گریه‌های اسطوره
😭
😭
😭
😭
😭
😭
❤️
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/Futball180TV/98899" target="_blank">📅 21:36 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98898">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MhBLHU41OfdVvnhOUEJ_IgSSSAQBL_UHL_sw5rEjn20So3sTQlY8tIIpXz9X4jm0dG3zsoA9N9Zu5L4r2DfpYfY3CKR03l5dR544CKbEjIXAnqkq0May2vnilEs2fwvm6iwaBgKOfl9QcAeT47pod_Tw2Eh3m8SvvmI5d-DM9cCp8ykmzYRehvbZvrqvf4TfSCWZNEDSzq8qscEIO4pkxS8EDk5rNW1xkqvHETNkLPq-zJbLZVK017tuV07TLLfU8nQGmX6mWMj3idA0TsuqBAMozWy1eUxbo-10grkml4EV8-1-UUtEk2srAmj4_ZRyGofkGvoZ6MSFOuWHWigJuQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">گریه‌های اسطوره
😭
😭
😭
😭
😭
😭
❤️
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/Futball180TV/98898" target="_blank">📅 21:36 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98897">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">چقد دلم برات تنگ بشه مسی این دیگه نامردیه تو پیر بشی اخه
😭
😭
😭</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/Futball180TV/98897" target="_blank">📅 21:36 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98896">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KKytMz9TxmowQGCkjXp2zyG4VKW7IlSBdZUWt2AgvgtCvXK4mL2I7wWhV0Ygco3Wj5BlxIcdkBGiyFMCJRz7Kjqz88-WiarxQCUKrRC2Q8Tu5hURP4iwB_1KPdiYjdJaHEmMdQmfzaRH907Toy7qNH08hGZWdQyc2fiWouXJp1UthP5p_jPRHNV74tXGrYtIknHmNTqEJedl-PR46hLAyHC30pRzgCBGEojnAqmiXgozgh6-eHJYJ6uTbUIpSsDPIndbGRnzEQX1w9Sy95fPQICf96MXXyi224dvh-t07a4V_1QoCvrL5-hezuA5WHdgT5ybdwX62XoEd61mLFS69g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏆
پایان‌بازی|بازی تاریخی آرژانتین به رهبری لیونل‌مسی؛ مصر در ۱۰ دقیقه تار و مار شد؛ قهرمان دوره قبلی بازهم با خلق نمایش باورنکردنی راهی مرحله ¼نهایی شد
🇦🇷
آرژانتین
😆
-
😀
مصر
🇪🇬
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/Futball180TV/98896" target="_blank">📅 21:35 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98895">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hHfsGKSO6fL9tAniRtDxuI8TWfqrhxfgUMbpUUaDMeICMOwKZzJI0r7SD0OnSXMRzXqJLWVOdPQ2fxcbOipDu_ad58lnF9TRNdQNXYN5nDe9GsIRxO_9imTssn1MLfuNC9RM_lyP0ZuX9fYq-R9U0DmSchwi-eXy_gatVFMRn93zy7B-FA75KxyHrFTMVkwKj2PXj-sXWnt8plIkzP-tg1trNucLw04iMBTdTJ5hjOw7iOYazyBSL-MN2vtYtj-ZIqPn7lYuXR20DDf1giVawgrFWAxxVtqp_uCZTfzFcQeeuy4wtn8lVs9fb7OInwMnrmM8IMyROa7F86ASZ4dpYQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سرمربی خایه‌مال مصر زرد گرفتتتت</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/Futball180TV/98895" target="_blank">📅 21:32 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98894">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">الان مصر نیاز به میکل مرینو داره</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/Futball180TV/98894" target="_blank">📅 21:31 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98893">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UA4k7qBU1ud7-JzkvxViYd_gKtDNilY93hCAc0Ee49rXe1QBjOqIdJGjO3zjnTfL685X8BI1clpPqmpoesh3K4x0nta_E2OAno9AfHN6Bot1_yQDZ-ZrUbii5WpH4yrYqRNu1B5XAv4nWCdab5o9uEWAVUrWdU-kCN_ZHomlZUZPunkjH7Bk-H7AvvcQsS-I2SGyTS3F9FDPFmhHwgOJbKjtDHbfMJS_j559Y8lfd4RDoqHKvnjt1B-O5mdQ1Gp86siwlJDFmWZPUVCNUdQvfurz8keXTHFSJeeXYSJKZL0yO-9f0YJncCArQeVdc3o7c6GDehXuTPtji02EESaAEw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
🔥
🔥
🔥
🇦🇷
🇦🇷
🇦🇷
🇦🇷
🇦🇷
🇦🇷</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/Futball180TV/98893" target="_blank">📅 21:28 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98892">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">🚨
🚨
🚨
گل سوم آرژانتین به مصررررررر
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/Futball180TV/98892" target="_blank">📅 21:27 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98891">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">عشششششششششششششششققققققققققققق میکنمممممم</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/Futball180TV/98891" target="_blank">📅 21:26 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98890">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">کیرررررم تو مصررررر</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/Futball180TV/98890" target="_blank">📅 21:26 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98889">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">عششششششق میکنمممممممم</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/Futball180TV/98889" target="_blank">📅 21:26 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98888">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">چییییییی بود این بازی
😭
😭
😭
😭</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/Futball180TV/98888" target="_blank">📅 21:26 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98887">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">چه بازی شددددددده</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/Futball180TV/98887" target="_blank">📅 21:26 · 16 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>

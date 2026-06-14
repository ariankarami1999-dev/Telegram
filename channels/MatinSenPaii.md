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
<img src="https://cdn1.telesco.pe/file/BKXMByZNNbUVDjdNuubKRtn0i_bN50M1GODzzpGKDkEeIndb9zS0-N6hwFRF5oi4_b76ELouzHm2u7fWv9zVnpyw7gscNBqqxrSo7Ige2bEBaGMJkO4RdRLdkeEbI_R155y1TCZmnEakpkYXNuKjQzMjw2qowbTAS9FXEIB-YU28TQpbtS-NxR-o-L0K7a2tW0oQo0jxpEAI-ea-PF8trtH9Ro1l9EeX_zyO4L7vduQqtPttZQSzKEjc3BQP77cDTCETGAlRLsQ5GCdllQ2hf2CbBSIN1rqvn1oNJxM0dSDi-yZ0Wp4BnXGqvopfu7Z1sTraaIaEppcx1CYIm3gYqg.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Matin SenPai</h1>
<p>@MatinSenPaii • 👥 162K عضو</p>
<a href="https://t.me/MatinSenPaii" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 درود! متین هستم و کامپیوتر رو دوست دارم! در حال یادگیری هستم و چیزهایی که یاد میگیرم رو سعی می‌کنم به شما هم یاد بدم اگر به دردتون بخوره =)•YouTube:http://www.youtube.com/@Matin_SenPai•Github:https://github.com/MatinSenPai</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-24 22:41:20</div>
<hr>

<div class="tg-post" id="msg-3884">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">رفقا من تبلیغ VPN و سرور مجازی و... انجام نمی‌دم. همونطور که توی دوران قطعی و از ابتدای فعالیتم این کار رو نکردم. هرچقدر هم رقم رو بالا ببرید فایده نداره. ممنون میشم واسه‌ی این پیام ندید
🙏</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/MatinSenPaii/3884" target="_blank">📅 21:47 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3883">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">رفقا من تبلیغ VPN و سرور مجازی و... انجام نمی‌دم. همونطور که توی دوران قطعی و از ابتدای فعالیتم این کار رو نکردم. هرچقدر هم رقم رو بالا ببرید فایده نداره. ممنون میشم واسه‌ی این پیام ندید
🙏</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/MatinSenPaii/3883" target="_blank">📅 19:58 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3882">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/LV2It6PnjfR3H0q6UB2r1Us-C3JhVrwxAELKkV-mVVk9fqLzqGcWy7EHPpRecKV4-_b7zy2qmgMsfeR-dlUEVvr7OFSYMVK0LMHmlCKapXJZosWtS4tPe66vJgMSQx5sHBLRQRB5oW7naxYhpU-7we85N5h804jurvb-s79-_URHorbNtRFIVz6RU-HOFi1nwlZa0Zpg-MYXcQfSbtAuaslPxZK-vfUE1u5EJ_oJhiMBtdZO6_Asbbz_J3U0H3qsHp3s-du3Yji1ZsLLINZOyUcHQwUiZGqkCfsax_9Jbu-II8_2bt_ZP6xcGvWY2bY5vEWTjN5FRWIEytAV6pIWYg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اگر این ارور رو برای اسکنر یا هر پروژه‌ی دیگه‌ای می‌گیرید، ترموکس رو از گیتهاب نصب کنید؛ درست میشه
https://github.com/termux/termux-app/releases</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/MatinSenPaii/3882" target="_blank">📅 18:46 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3881">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/HWRksh3smWzgmmGeKk2ToJ0_Ukfk641lhgUM4aKv2A5ueeCg6v1aJCQY3anX-goIQI0x-7F4owzKFwTDVbQh4K_YFAWEMkXo1E3_SkQfntf16fqHg1KpuGOzm9QRpL1c9NDHtOfY8-dVKmKCPW6dy3S4eHUjWFX-7KdOXk2SxKDIW04KUgzKhLQs7zC_rf38grL2E_Z8t6bWOdEIMtdYcBwPzJopPi9QuMFFVR3MJVWcHkEZ2b50xUmKtV-JG-PY2T_jDGwXaPwragJxNxtnUAF3enUoPSdmmPLNYrgaGHxgEM68Bd-8PmRY_71WRl2Ou5Sv6hz23GOFvBnt8ZdVKg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">من الان خودم با سرعت عالی وصلم روی ایرانسل. ۲۰ ثانیه طول کشید حدودا، منتها ممکنه تا چند دقیقه طول بکشه. ولی وقتی وصل بشه دیگه کانکت می‌مونه و قطعی نداره</div>
<div class="tg-footer">👁️ 30.8K · <a href="https://t.me/MatinSenPaii/3881" target="_blank">📅 16:11 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3876">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">whitedns-v0.0.2-arm64-v8a.apk</div>
  <div class="tg-doc-extra">23.5 MB</div>
</div>
<a href="https://t.me/MatinSenPaii/3876" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">نسخه جدید اپ WhiteDNS VPN آماده شده.
در این نسخه
• سرعت اتصال بهتر شده
• مشکل داغ شدن گوشی رفع شده
• اپ همانقدر ساده مانده و فقط شما باید دکمه اتصال رو بزنید
متاسفانه باید نسخه قدیم رو پاک کنید و این ورژن رو از اول نصب کنید. این مشکل از ورژن بعدی نخواهد بود.
ممنون
🔥
تیم
@WhiteDNS</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/MatinSenPaii/3876" target="_blank">📅 15:51 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3875">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/TmWcyj223ZVIg6g7kOOgTF1buHkQmTcUZB1RZg9mpK2APryWCRHjrmlEZdqqlMnR2FMviR8i3n7s1lViJBpe5pUhqfQDkVykXdTgcFiu7fr_29WzGuSSWyc68pse_H-kwM0uldJyI2ovZDGPVb2ISNhVMzsd1QVbFnXQpFqVcXZsnP5s4hI1LOxIaYgwsoMjsMgSNlc1i1o6ZS6PEgQmlm74rFTPDBkikvVw5w-IldVL-RqXbu-z3c4lo-gd3Lj5sP80vGSb0rK-qcnUmKLn_jhyB2zmzKxJchVeqhmmD9lzDD9iNmGEgtAcWqUVxKYnr_8ZHcUSTG90fc4TLrGgFw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فکرشو نمی‌کردم یه روزی قالب وردپرس رو هم بگن بیاید اقساطی بخرید</div>
<div class="tg-footer">👁️ 33.9K · <a href="https://t.me/MatinSenPaii/3875" target="_blank">📅 13:33 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3874">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">خب دوستان به نظر من اشتباه کردم و فونت وزیر متن هستش. مسئله اینجا بود که از من پرسید، گفتش چه ترکیبی بزنم؟ چندتا داشت، یکیش فونت مربع+یکان‌بخ بود. منم زدم همین و بعد دیدم اصلا پولیه. اما الان انگار وزیر متن انتخاب کرده
نکته اینجاست که چرا اصلا فونت‌های پولی و غیررایگان باید بهشون اشاره کنه یا دروغ بگه
🤔</div>
<div class="tg-footer">👁️ 35.1K · <a href="https://t.me/MatinSenPaii/3874" target="_blank">📅 12:16 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3872">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/hioOGdoQaickGs1OD8K_FdnzmlRW-M32C7MTFjwtvACrgxqt76GF_s6R4lqLiS6zyfdCUT9EoM5W_RxEv6PB8TFT4x_WGKs2F8DBbl_IbxwfFNZSi8itaUtBnAfXpjHC04uNnb1_Rz7rfeKEsz8j4Lh8cmN74r_ejWlIlsVmGEC8zMNL9e8Z7y1-nf0ChWJFm-5LZ8RBlCGeG6t9UBOseR95Ww9ppufNoPYdkuao03v0LSPNrKiLZx9560iHyj_2_c26OkR40gisnQdg6o8XJOKY2AKuOOvVnqzc4PfSVu-qur1UU60CkhlwI8WBjXRzdui_P5j2z6EOwjfzwxmu6w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/NQwRTCwbVP7hGJQSYAc2J4dg-lpB_OFVsScdinu6Y6Ud-PBpn6THBsf5JYER7Bt0rfMddUBt-PaPP0goLwywMVcAnUp5GTzrOf-aBOZRcbRLk_o96ASKnee2oq0vCWPjinalnhymyQYzSP7h4W1QZM8gFWvfgxwJlG-yUbMnEPvY7DLkAAR-5vM2EH2ESBZ_XsJW1vLhW0Ot-XWuLx2EYNEYXHhvQw3yplGBABT5_HWmtLdvaoh5zheZxFyYIfryVkXBNe8HJLMHFwe61Mn6YDXXHJ17lconDiNwoDg1E6vh35ZlJVTjgY26OS5ek0FgRNKBz4FtYDHHL9JO-TxyOg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">فکر کنم کپی‌رایت برای کلاد شوخی‌ای بیش نیست. اون از قابلیت اکستنشنش که کل UI و المنت‌های صفحه وب رو درجا کپی میکرد، اینم از این</div>
<div class="tg-footer">👁️ 35.8K · <a href="https://t.me/MatinSenPaii/3872" target="_blank">📅 11:13 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3871">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/oLWK250yxEi7hWCVPGf9eaM4BZ2LdRsZ8mVSDKIP_UydX0at_tk7q3uj6Sv4FmKR0YXc0Ckt7ysw3hB-O8U8NyVvpb-AFpQjLgbP4vU3t7VHxrLDsRZ47UGJCELdWwsw-Z19aDvvBCWQzHSaywo3H7-Cm6OZYk0u512-bRuzTV-dNKbK4c7VwNJLY1Yb2j-om1OTXyM0_y6aXogMGWWB8hznJZs9UNvU1261hNOp_LdavNZRooSKk9qdSxaL75bSyhiYe-Qs1cI8cUViVAbnKPVrh2eY6K14aBzxG34dTGQSza1AFs_kNpY7VBPcgU1po_OPn3tEzFxKsrej_tQ0gg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در این حد بگم که رفت فونت پولی ۵۹۹ هزار تومنی رو نمی‌دونم از کجا پیدا کرد و گذاشت توی پروژه
🤣
🤣
🤣
اصلا یه کار عجیبی کرد</div>
<div class="tg-footer">👁️ 36K · <a href="https://t.me/MatinSenPaii/3871" target="_blank">📅 10:51 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3870">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">در این حد بگم که رفت فونت پولی ۵۹۹ هزار تومنی رو نمی‌دونم از کجا پیدا کرد و گذاشت توی پروژه
🤣
🤣
🤣
اصلا یه کار عجیبی کرد</div>
<div class="tg-footer">👁️ 35K · <a href="https://t.me/MatinSenPaii/3870" target="_blank">📅 10:50 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3869">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">من منتظرم که شرایطم استیبل بشه، حدودا ۶-۷ تا ایده‌ی خوب یادداشت کردم هم راجب AI و برنامه‌نویسی هم واسه اینترنت آزاد که واستون ویدئوش رو بسازم</div>
<div class="tg-footer">👁️ 34.6K · <a href="https://t.me/MatinSenPaii/3869" target="_blank">📅 10:49 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3868">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">من منتظرم که شرایطم استیبل بشه، حدودا ۶-۷ تا ایده‌ی خوب یادداشت کردم هم راجب AI و برنامه‌نویسی هم واسه اینترنت آزاد که واستون ویدئوش رو بسازم</div>
<div class="tg-footer">👁️ 34.9K · <a href="https://t.me/MatinSenPaii/3868" target="_blank">📅 10:49 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3867">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">‏
بدافزارهایی که با ترساندن هوش مصنوعی پنهان می‌مانند!
تصور کنید یک سارق بعد از دزدی، یادداشتی آنقدر وحشتناک جلوی در خانه بگذارد که مامور پلیس بعد از خواندنش، با خود بگوید «بیخیال…» و اصلاً بازرسی را ادامه ندهد! پژوهشگران متوجه شده‌اند در موج تازه‌ای از حملات نرم‌افزاری، هکرها از ترفندی مشابه برای فریب دادن هوش مصنوعی استفاده می‌کنند؛ آن‌ها بدافزارهایی می‌سازند که بخشی از متن‌شان طوری نوشته شده که هوش مصنوعی از بررسی هرچه بیشتر صرف نظر می‌کند!
ابزارهای هوش مصنوعی کنونی، ترمزهایی از پیش تعریف‌شده دارند. برای مثال اگر از آن‌ها راجع به نحوه‌ی ساخت «بدافزار»، «تسلیحات شیمیایی» یا «تسلیحات اتمی» سوال کنید، فوراً ترمزشان کشیده می‌شود و از پاسخ دادن طفره می‌روند. حالا هکرها متوجه شده‌اند که با افزودن این نوع از متون ممنوعه به بدافزارها یا نرم‌افزارهای معتبری که آلوده شده‌اند، می‌توان فرایند بررسی امنیتی کدها از سوی هوش مصنوعی را هم مختل کرد.
به زبان ساده، مهاجم سعی دارد کاری کند که ابزار امنیتی وقتی به بدافزار می‌رسد، به‌جای بررسی دقیق کدها با خود بگوید: «من اصلاً اجازه ندارم این را تحلیل کنم» و از آن رد شود.
﻿
این نوع حمله نشانه‌ای است از ورود به مرحله تازه‌ای در امنیت سایبری؛ مهاجمان دیگر فقط انسان‌ها را فریب نمی‌دهند، بلکه رفتار هوش مصنوعی هم هدف قرار می‌گیرد و ترفندها در گذر زمان فقط پیچیده‌تر و خلاقانه‌تر خواهند شد.
✍️
NooshDaroo</div>
<div class="tg-footer">👁️ 36.9K · <a href="https://t.me/MatinSenPaii/3867" target="_blank">📅 08:56 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3866">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromSarto | سارتو</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TqYvvoDEs4AqIg2Auuh5k9XzYuEuRyUfPIePIYSePJE4zJiVNQ8f2cze9aZehFoqz-P_sFrAMJ_pP1BhkvSnBcc0iHdimMl6l7D2XcWzp3Pi6pTKUjnl4bseaIfy1tV5aYEktRMmlvssh4tOjxciBnm7Nfv2EICMeGqPIO_YKJPC5crtw0xCPmGUCnt-WOiju7wZoezlTkMf1FUAKfY1wlQuQkN2tGCtWLltFzrvB2_ZWtKZrClp-nWoxMiHuX4kyRkJyXIBH7qcnZPqVgXhpk0Gpl1Ktc7zYa3KHuVi2yiTNQHg3S6VE0DkZXUjFxh60813mhzalCwTSzot5f9Lzw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نسخه جدید دفید قراره قابلیت چت با رمزنگاری e2e داشته باشه؛
باهاش میشه ارتباط امن با خارج و داخل ایران داشت.
کل این قابلیت با ریزالور ها کار‌ میکنه تا توی فیلترینگ و قطعی شدید هم وصل بمونه.
طبق تست های من یک‌ سرور متوسط با ۸ گیگ رم و ۴ کور سی‌پی‌یو میتونه تا ۵ هزار کاربر انلاین رو هندل کنه!
اینجوری کار میکنه که هر کاربر یک اکانت رندم واسش ساخته میشه که توی سرور های مختلف ادرس اکانتش ثابت هست؛
ادرس اکانت شامل ۲۰ حرف انگلیسیه که هرکی این رو داشه باشه میتونه بهتون پیام بده.
(سیستم اکانتینگش تقریبا شکل شبکه اتریوم هست، یعنی‌یک seed دارید که با اون یک اکانت ساخته میشه)
کلاینت هر ۱۵ ثانیه به سرور هایی که بهش وصل هست درخواست میده و پیام های جدید رو میگیره و تقریبا برای ارسال یک پیام چند کلمه ای باید حدود ۴‌ کوئری دی ان اس کوچیک‌به سرور بفرسته!
واسه اینکه به سرور ها فشار نیاد محدودیت های سختگیرانه گذاشتم، ولی همه این محدودیت ها توی سرور قابل تنظیم هست و اگر سرور شخصی راه بندازید میتونید محدودیت هارو کمتر کنید.
https://x.com/i/status/2065531715041239193</div>
<div class="tg-footer">👁️ 28.5K · <a href="https://t.me/MatinSenPaii/3866" target="_blank">📅 01:38 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3865">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/SJ32wbhzWwLpsw5U_apNxCeh1_-EUyn1E0uPiMQiAEb3dRjwaroEuJMTcu92ySVlIZQ1GklXx1UY8d4dobpPA_uS2h43ZsXxieq0wPgDGU-Ua8GFmZp5YcGmZmXPgYw9R7LPeYFu-11mVmgQoKIvZelgnxKNDeUq0TrVEcB-4nIxjilDofhCTkRu6_kVDqJ6kOP-N1rjK0vbmRtVeq52pO4S13aHKQ64WRd7nbHf808OGfQwzxxiQYnegYH08awF4mqZ4kPBOAm5ugS0Q2h7bJdLoAuoKqCXvPSrVTRkrtYrNbr_PgDJL4Syl-s_0Ghv5FoycE4Ik0uaC1s1k1hAAg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رفقا به هیچ وجه روی کانفیگ Websocket معمولی سرور شخصیتون نباید اسکنر ران کنید. فقط روی Workerهاتون انجام بدید که ارزشی ندارن و ابیوز هم نمی‌خورن</div>
<div class="tg-footer">👁️ 39.9K · <a href="https://t.me/MatinSenPaii/3865" target="_blank">📅 19:40 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3864">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">برای اندروید و ترموکس، کسایی که مشکل دارن طبق این آموزش دوستمون برن</div>
<div class="tg-footer">👁️ 42K · <a href="https://t.me/MatinSenPaii/3864" target="_blank">📅 17:56 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3863">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">برقا باز شروع کردن به رفتن؟ خیلی دیدم امروز توییتر وسط کد و گیم و ادیت و... برقشون رفته بود</div>
<div class="tg-footer">👁️ 40.1K · <a href="https://t.me/MatinSenPaii/3863" target="_blank">📅 17:25 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3862">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">مرحله اول  همه بخش مرحله یک  رو کپی و توی ترموکس بذار
pkg update && pkg upgrade -y
pkg install golang git -y</div>
<div class="tg-footer">👁️ 41.3K · <a href="https://t.me/MatinSenPaii/3862" target="_blank">📅 15:35 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3861">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">دیسلایک فیک میزنن انقد خوشحال میشم پولشونو میریزن جوب
😂
(توی یه ثانیه یهو ۱۸۰ تا اومد)</div>
<div class="tg-footer">👁️ 42.5K · <a href="https://t.me/MatinSenPaii/3861" target="_blank">📅 14:03 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3860">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">نمیدونم این کانالای تلگرامی چه گیری روی ری‌اکشن دارن
میگن ری‌اکشن بزنین انرژی بگیریم. انگار از ری‌اکشن برق تولید می‌کنن
عقل ندارن راحتن به خدا</div>
<div class="tg-footer">👁️ 50.8K · <a href="https://t.me/MatinSenPaii/3860" target="_blank">📅 14:01 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3859">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">دیسلایک فیک میزنن انقد خوشحال میشم
پولشونو میریزن جوب
😂
(توی یه ثانیه یهو ۱۸۰ تا اومد)</div>
<div class="tg-footer">👁️ 58.6K · <a href="https://t.me/MatinSenPaii/3859" target="_blank">📅 13:59 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3856">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/ml8C2yGiB3n9Rconl0E-aDJaFQCBwAb8zokNVAeOiM13fGFU1gmlD15oirM4WdgVIfKbybbqfW5TLveH332Izyr7rTTQYtRu6ZPuvkrNyLNw-DP154TgNBavnFZuEoBvOIjPE9koamHTSoDGWR6XM7L4l3rfU4pauO-P9Eh2bGd0Wl871mGQos_Rzwz9enNmzmet0ORbcdwT1mEGiHpfnJGpHH_wkWn1KAkq9DKv8AK5W04hQW6J_aRmWho3o7WyS6z3RZ3Oj-yjZ-JcjKOQFSaYfoMwxvqLpV2yo_szQHkKoxv8chiMQTItHzFtOSCRzAokdXzGsbbFqcpHe9tJBQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/oVm2eyq8-quIY224joUEDLHTXS-0lpub2MlDsC4Pv8732MoC1IIXKojr-4vTzgqsXa5m59QlPi5p-bnxr1Nd4Yghe_vjUWBo9kK7RL5N7yy_Y5ThOvi_azXRy64iVHuXKS7cfs5HYHWabxGrm1RVXyFvUX86vsar1ZemeHfQ1RaciEgT4RlG4-CkcgYX4s_qFmFpUnDA9ne-sjPSZPaK5H5RkhtvurgOegitoAVLETfC7SLRlUFBOvg3omPCaEXaaFlhYN1PDTAfgxTVhMfK7svfELmIuCAk8aF6c-8lbfrFzuGcwVaXBz9vccEmb13T1eXDyKnxeMl6bRZk3v8cKw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/OPFIMg8cdeRMzEvL2O0-r19KrS_4FpdFxjA1uDEC-set_dbLn1-4mgeVCnT69WycY1di9UKXIFD7hf6XTmz1lWnrF2XNAn2I98IovuN4sOZ7rERvHstWDztkQejaDAuvFzPFGIUoHhwRh1Vz7ySYL-gYiGHelGyCrfEDQVCp9Wb8Jk9dVjOKRHmoXQ3Tf0myh0jXppZrxzKysjnViV64Vkw0INxmC-NlnVrrn3ufxaU_6lzwpKhOmKg2U-aQE1pOl6GBj56rkFiDe4K2Xo4PulQsBTdcjKdyl_sEkxbzD5opWj61zLSFAx7UJrqtVibnS3wp3sQiSulJIW5CrAIzmw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">ورژن 0.7.1 از SenPaiScanner منتشر شد
✉️
😏
پروتکل‌های جدید
: پشتیبانی از
Shadowsocks
و
VMess
اضافه شد — هر دو از فاز ۱ اسکن تا فاز ۲ xray کاملا کار می‌کنن.
🧮
خروجی چندفرمتی
: با زدن
e
بعد از فاز ۲ می‌تونید نتایج رو به سه فرمت صادر کنید:
1- لیست Subscription
2- Sing-Box JSON
3- Clash YAML
🔥
تنظیمات سرعت
: فیلتر حداقل سرعت، تست سرعت آپلود، آدرس سرعت‌سنج دلخواه، و سایز sample قابل تنظیم.
🤖
ذخیره تنظیمات
: تنظیمات اسکن ذخیره می‌شن و گزینه «retry last scan» هم اضافه شد.
📚
پشتیبانی از CIDR
: حالا می‌تونید توی
ips.txt
، مستقیم رنج‌های
/13
و... بنویسید.
📱
اولین نسخه پیش‌نمایش
اپ اندروید
با Kotlin و Jetpack Compose اضافه شد. معماری MVVM، تم‌بندی کامل، و ساخت خودکار APK از طریق CI/CD(هرچند CI/CD باید روش کار بشه هنوز).
لینک دانلود آخرین نسخه:
https://github.com/MatinSenPai/SenPaiScanner/releases/tag/v0.7.1</div>
<div class="tg-footer">👁️ 54.3K · <a href="https://t.me/MatinSenPaii/3856" target="_blank">📅 13:07 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3855">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">دوستان، این شکلی میتونید به من پیام بدید:
https://t.me/MatinSenPaii?direct
اما از اونجایی که دایرکت به شدت شلوغه، و من پیامها رو اسکرول می‌کنم پایین، ممکنه گاهی اوقات زده باشه سین شده، اما من نخوندم در واقع</div>
<div class="tg-footer">👁️ 49.1K · <a href="https://t.me/MatinSenPaii/3855" target="_blank">📅 12:13 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3854">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">حقیقتا MiMo اگر پلن پولی بده، خودم اولین مشتریش هستم. توی تسک‌های متوسط Backend شاهکار کرد امروز
هم توی سرعت
هم توی دقت</div>
<div class="tg-footer">👁️ 50.8K · <a href="https://t.me/MatinSenPaii/3854" target="_blank">📅 12:09 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3853">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">هم پشتیبانی از Trojan و Vmess و Shadowsocks اضافه شده
هم تشخیص ISP
هم تست آپلود و شخصی‌سازی تست دانلود
هم WebSocket(که بهتره On بذارید)
هم هسته رو به کلی بازنویسی کردم
و این به کوشش دوستان عزیز برنامه‌نویس دیگه هم بودش که اسمشون توی Release note میاد و contributer پروژه هستن. من شاید 20 درصد از این 10 هزار خط کد که اضافه شد توی این ورژن رو نوشته بودم</div>
<div class="tg-footer">👁️ 38.7K · <a href="https://t.me/MatinSenPaii/3853" target="_blank">📅 12:03 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3851">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/XVSayhmBs0hbKC3VvIPeAFPk84yLmvDS32SYqKHmbJcNSyDoQijpHvX2BNuNSadqVkN_oz_POVPb8QnwRArhPVvDXcqKgQI7TKh8bkU0cRAcgMCXNIGP4atrpXlrP-b9buHyJaOavwKEVS-n518qPfx2aoy12Z3FLENTL1kQyeaqG8OjeMuiM2jdtdHLs5BsTWQTpujmhXyQBx7VCVCo6cw4hwDF3XyZlF64GAr-raPRBgFK7mZJfYO_k_Qg6MQEjDj07esMpzvm3uV1pnupBXSwkpP9r5rEbeZrsgeDv-w3uGBcj-0kIo3fhE7f7qSpT3jdNpV_KBPyJhRbVXxaCg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/uRAUhd1ELO-C2HuL0Tlfo80QI5u9gDv6O65UwJC-Ussilj3x6RHLHXc94uDKgxo0VxWO9JieWGy1WRQ-jERPesovO93a3wEIXIwF9yMlzx4sgs6gfVih-FUWXs_NF1skzPSxSKhlVILyAlhdswC813YwjnePIP0unSX0G-wem0PbR_eNn-Ociz55zmXgOR3J9HbQRmGEVqMqwHSM5VuckokceP0NgDsp7Iy4blsI52pyVmalps3BOrY5ZQtxwE_-TckCDXLGRJfCSb9ScvWXfCxW4ZjKJ9R7X9iPCp2QjiigHFdHlclqC0eHVwTbuH1OKfdtT_5kiREhxjFN_ODVdA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">بازخوردهای خوبی گرفت این ورژن که باعث خوشحالیه
❤️</div>
<div class="tg-footer">👁️ 35.6K · <a href="https://t.me/MatinSenPaii/3851" target="_blank">📅 11:54 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3850">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ul1Bg1Td6chlHtAhudIqpTb800Qgp399Msel9n21NrKht0VwI6S3GMVQHTEkeZKZWpihAc2PxmKArPpkTqWjCs6YpQIHUFnVRm4KkoFeeyXM2_5yiG0aIcW6TIJInWrjb9E3Bdfoy7tsfvwVP958b5T2e_UcCMjEnhcKfxpmpQitmeGNwdxOk03xdzOM9prdDUv_zdKlhPOlg-vVDsFOTlRFy8z-daZPE8olOh_cNI9EOEbsiLSIk4wIZztL0f5oZf62lkC6gM38UchyL65dTG6P6ZzsfkWXy1pr5-el-F2FsU-6yEKk6h3kkpeAMFJafGFlUk6GlCl_tqAIgS03iw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بازخوردهای خوبی گرفت این ورژن که باعث خوشحالیه
❤️</div>
<div class="tg-footer">👁️ 33.7K · <a href="https://t.me/MatinSenPaii/3850" target="_blank">📅 11:51 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3849">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">senpaiscanner-windows-amd64.exe</div>
<div class="tg-footer">👁️ 33.3K · <a href="https://t.me/MatinSenPaii/3849" target="_blank">📅 11:33 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3848">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/SwFlvwaPv32yC6i1w0BuDiNFEhi0OUtcJzRVR1vi8CejgPtLX5k1nA7KmyfXJ0-tKvba9tfqsvhistFqb3dsq7rmB_l4BrVj5ztpGDlze2DbO6D6SU88-vGOaOPnV2RpTQpUCghBF-JhMmYuwvhpox-it64Dkk3ca5pqigm27X-WbNP1ShE5Mn4jukX00_P4zWujf0g196uZW6-wu5MotUyPTN1KA_xJFxH7X-NJ2NRVQqWwn5bPYMqI-h1rSyh_edqEC9yGK7xCmRzLCxT8Fe5D2jrlWSp7LgUSiMsXnd4lIwMfwqWfLXLU_dybHCkvlieryiomPRX96_r1sETzCw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یکی از دوستان خوب، لطف کرد و هسته‌ی اندروید و تمام چیزی که برای ورژن اندروید نیاز داریم اد کرده، صرفا منتظرم که خود اسکنر عملکردش به بهترین سطح برسه، اون موقع نسخه‌ی اندروید هم بیلد میگیرم</div>
<div class="tg-footer">👁️ 31.8K · <a href="https://t.me/MatinSenPaii/3848" target="_blank">📅 11:22 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3847">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">نکته‌ی خنده‌دار اینجاست که دولت آمریکا دستور داده دسترسی به این مدل‌ها برای هر فرد غیرآمریکایی (foreign national) — حتی داخل آمریکا و حتی کارکنان غیرآمریکایی آنتروپیک — مسدود بشه!!  آنتروپیک اعلام کرده که چک کردن ملیت کاربران به صورت عملی ممکن نیست، بنابراین…</div>
<div class="tg-footer">👁️ 32.2K · <a href="https://t.me/MatinSenPaii/3847" target="_blank">📅 11:18 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3846">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">senpaiscanner-windows-amd64.exe</div>
<div class="tg-footer">👁️ 32.4K · <a href="https://t.me/MatinSenPaii/3846" target="_blank">📅 11:14 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3845">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">senpaiscanner-windows-amd64.exe</div>
<div class="tg-footer">👁️ 33K · <a href="https://t.me/MatinSenPaii/3845" target="_blank">📅 11:07 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3838">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">senpaiscanner-darwin-amd64</div>
  <div class="tg-doc-extra">32 MB</div>
</div>
<a href="https://t.me/MatinSenPaii/3838" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">خب، دوستای من هستید یه تست از اسکنر ورژن 0.7.0 بگیرید؟</div>
<div class="tg-footer">👁️ 37.6K · <a href="https://t.me/MatinSenPaii/3838" target="_blank">📅 11:05 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3837">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">خب، دوستای من
هستید یه تست از اسکنر ورژن 0.7.0 بگیرید؟</div>
<div class="tg-footer">👁️ 33K · <a href="https://t.me/MatinSenPaii/3837" target="_blank">📅 10:50 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3836">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ZLmy4aJlYO88GRsjpiU9cE16AvjdViX6Pz2ObDv6sWCwz0AU40iZR4c6e1BwnbyXbVgtliNwCKFFGOww8NMG2fhDCPLqUebdMd6sYjzVKDKcAE5KNbg_emJhoOnPqLoOSPPYbrrsWnmU4YyssRo0CwaYxRacxCAbQpUozD9DNREzQmcuQ7AJ4uJbeyipQHWvOEPlLGY6DZrL0n-g399pBxNkMnhkJ4aaJkaJPr1Yf4cC_KUJNT4hWxRva-936EE6MrlbKWC2dQX0tAZRWyomKDPMwXnd2fqoYtIKBrtl9KfbDuZmj63Qdv1h0wWewBZAkRD8E-71WYR_g-FK68ZFMA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">لپ تاپ اوکی شده الان اومدم تست کردم MiMo رو و خوشگله یه تست پرفورمنسی بریم باهاش روی SenPaiScanner</div>
<div class="tg-footer">👁️ 36.3K · <a href="https://t.me/MatinSenPaii/3836" target="_blank">📅 10:42 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3835">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/jHrQVO_5iSsTibuzuyAfVYl1G1efXKAb9_2zwdd4dB7MMivuYXz-Ybs8Qv5DNwqB6JFzTkN4t1Pd0DrQaLOAQrod0EbZz8pqegjFcm3N1r7ac_GlGrVB50ScofU-j5N2c3SiUY_oripCH3RgPu4wwZNvtpRCBcL9b74eAFOv4QmP6GsrJOGgxW0bHIfB57Ap5XfoNo_ATD2myRd-uWNMl1qszTHC2KoUvoWitVgxDzhPjhj-qaVlohvzvaGvnc3IWLI9oP67mHft0VZxwRnsP3U_D0MG7DiV_gYw3aAjgRLJH8vwC3RMoXxGgKsV0RdFh2fBcMX50z0QTqRYR4EOJA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شیائومی از MiMo Code رونمایی کرد  توی این مجله‌های زرد دنیای AI بهش لقب «قاتل Claude Code و OpenCode» رو دادن؛ ولی بذارید واقع‌بین باشیم — یه سری ویژگی‌های جذاب داره، اما قاتل این دو تا عزیز دل نیست
😁
(مخصوصاً که خودش فورک OpenCode هست!).  خلاصه‌ی ماجرا: تیم…</div>
<div class="tg-footer">👁️ 35.1K · <a href="https://t.me/MatinSenPaii/3835" target="_blank">📅 10:19 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3834">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">برگام! آنتروپیک به دستور دولت آمریکا و دلایل امنیت ملی، دسترسی به مدل Fable 5 رو برای همه‌ی کاربرا مسدود کرد!!</div>
<div class="tg-footer">👁️ 41.9K · <a href="https://t.me/MatinSenPaii/3834" target="_blank">📅 09:24 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3833">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/J16a__9AuGVzVlx7Qpog-7eKblKawV00KF6rnWoCA2SyFrF2EcvU6NwhagmD63H7xsUhfNyr4QdmTeFrt90cq7B77_3sHbDnrApRNnPioJVJ8yZIZyXIFNAJLjYwbM-139oa7_3x4MLx9NYZM4Qgr2E-rxkQQn613FcxFIaua7FOaNX6mIqhV3ysUAoSCkq00Rge780qhAyu6HRh4PCQ2JpojKGQj7ZsOKbQRl5DU5Pl9BCraDqPuyXioA-n1lxwk_nTvb0kst1Up8SU-oq-Y5Nxb1GAi7-s9a3N4y46MuCSBjylfDfllN9oRQS-z1HRsfayQvsv7WWYLrrwn_7SjQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">برگام! آنتروپیک به دستور دولت آمریکا و دلایل امنیت ملی، دسترسی به مدل Fable 5 رو برای همه‌ی کاربرا مسدود کرد!!</div>
<div class="tg-footer">👁️ 39.9K · <a href="https://t.me/MatinSenPaii/3833" target="_blank">📅 09:12 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3832">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">این سایت رو یکی از دوستان معرفی کرد برای دامنه‌ی رایگان، یه امتحان کنید http://l53.net/</div>
<div class="tg-footer">👁️ 42.4K · <a href="https://t.me/MatinSenPaii/3832" target="_blank">📅 02:16 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3831">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/sLjNa0DxQXqHM-l26lIMwcCmIvVTQ8us2A33P0ionurp5uHe53ZE8K0rr0Boh4Orywn6w8D0FE0tFK_no_nEKePsVKwCDi5fvL0G8AgmA-kvPVdmkSybI7AFpw9VThniy_io6xPp5vSTN7QefgFypmGlFGWDzk1OLxdq-vmI1cC3C48LIG6jIkRLAd4jIk5g1dxWQghALoIJh5Y1CyjbI73s0-Q0aTIItrxw0JFELjBBc1BFbfrscFJUfguOI9bD6UDW2xVIExqHipDv-M7VEGrCVIdKj5e4HQoJPJaSHwOUHSinAIZ3vuImavgkp1AvIkscHNmbxsUlfol9mBjI0w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این سایت رو یکی از دوستان معرفی کرد برای دامنه‌ی رایگان، یه امتحان کنید
http://l53.net/</div>
<div class="tg-footer">👁️ 44.1K · <a href="https://t.me/MatinSenPaii/3831" target="_blank">📅 01:55 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3830">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">من شرایط ضبط نداشتم دوستان. یه مشکلی هم برای لپ تاپم پیش اومده که باید بدم تعمیر و ممکنه کلا مادربوردش بسوزه اگه روشن کنم ترجیح میدم ریسک نکنم چون دیگه پول ندارم بخرم
😂
تعمیر شد، آموزش‌هایی که قول داده بودم رو ضبط می‌کنم</div>
<div class="tg-footer">👁️ 40.7K · <a href="https://t.me/MatinSenPaii/3830" target="_blank">📅 01:30 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3829">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWireguard Configᵛᵖⁿ</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7797f080f2.mp4?token=kXlS2I4xHeECMEKwrh41mo-UZUanjDyLYdhdpTf6-6f1e1iZ9LMof_9_ZjHvCrNmdBN7RJfOrBo8FxacYrZ0do85n0iEO8SAvsI1CFvK_Fmo46NcONg-stCfD9PwnvtxypRsgbHvyP0YD3FJFdUw9AQCodx-bCbHWEb4bY09lFPNm33v3roGfqlGkVdZrSS5HrOv-XVY0b1mhy5b0fzbUq9tt1BYI9i8HiaXrkTm_GtHZoGVFQ5j__EDSU8lOjsMPZtK7f17wLU47YrUB-AZGh5iJjwBXYl8tjsJRgNgfxwKunLkEtfBvg6dQ6Z9_FzxCNrAifgZjcfP4VhHX_vHvw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7797f080f2.mp4?token=kXlS2I4xHeECMEKwrh41mo-UZUanjDyLYdhdpTf6-6f1e1iZ9LMof_9_ZjHvCrNmdBN7RJfOrBo8FxacYrZ0do85n0iEO8SAvsI1CFvK_Fmo46NcONg-stCfD9PwnvtxypRsgbHvyP0YD3FJFdUw9AQCodx-bCbHWEb4bY09lFPNm33v3roGfqlGkVdZrSS5HrOv-XVY0b1mhy5b0fzbUq9tt1BYI9i8HiaXrkTm_GtHZoGVFQ5j__EDSU8lOjsMPZtK7f17wLU47YrUB-AZGh5iJjwBXYl8tjsJRgNgfxwKunLkEtfBvg6dQ6Z9_FzxCNrAifgZjcfP4VhHX_vHvw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
سا
خت کانفیگ Amnezia VPN
• صبرکنید ای پی ها رو لود کنه
• بعد یکی انتخاب کنید
• تیک فعال سازی پارامترهای امنزیا 1.5 حتما بزنید
• بزنید روی ساخت کانفیگ Amneziawg
• دانلود کنید وارد کنید داخل Amnezia VPN
• میتونیدم کانفیگو کپی کنید + بزنید بعد insert بزنید کانفیگ اضافه بشه
🟡
فعلا روی ایرانسل
💯
جوابه(همراه اول ،مخابرات،سامانعلی)
📍
ای پی جدید هم اضافه می‌کنم
https://darknessshade.github.io/Amnezia-VPN-Config/
@ConfigWireguard</div>
<div class="tg-footer">👁️ 44K · <a href="https://t.me/MatinSenPaii/3829" target="_blank">📅 01:15 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3828">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">کلا فکر کنم ساعت از ۱۲ میگذره دکمه‌ی بمبارونشون روی سیریک گیر می‌کنه</div>
<div class="tg-footer">👁️ 44.6K · <a href="https://t.me/MatinSenPaii/3828" target="_blank">📅 00:12 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3827">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/XXHqqQR27TSkP9PEQEqkScao20FcFRiF3-QsQbZrg6zYO1rV-NdbphZwdYP0Z8dGpyMhregiZYwC-BX7aqjNBOCa5nqpxJS2RqPn50J9G3mhvBE72fnqCwVXBqckK9FcidssyCML7gLt6G4ao97pLyOn7a_ZrM9Ew2LhQ2DPSuE4y6eeja-k1Y3pRue7UNrqYpcJmIvulaHgEc4LTdu0hKfdR8Z7_qqe_Xr5VCzWYnIaYJ-T3ZWugD3DLnLqWyDlS7xgSGoBwRXSusytYMtXaPij2sNT4frpwYklgB_kIk_MmeHEQ-X3mytnCWXZfOOT_Rw-tCMY7I9C8wzlotkDvg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شیائومی از MiMo Code رونمایی کرد  توی این مجله‌های زرد دنیای AI بهش لقب «قاتل Claude Code و OpenCode» رو دادن؛ ولی بذارید واقع‌بین باشیم — یه سری ویژگی‌های جذاب داره، اما قاتل این دو تا عزیز دل نیست
😁
(مخصوصاً که خودش فورک OpenCode هست!).  خلاصه‌ی ماجرا: تیم…</div>
<div class="tg-footer">👁️ 45.3K · <a href="https://t.me/MatinSenPaii/3827" target="_blank">📅 00:06 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3825">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">اگر مشکل باز نشدن توییتر با پنل BPB دارید، همونطور که توی
ویدئوی تنظیماتش
یاد دادم، NAT64 یا ProxyIP ست کنید. اگر باز هم نشد، صرفا کانفیگتون رو عوض کنید با چندتا کانفیگ تست کنید، درست میشه.
proxy chain هم صد درصد درستش می‌کنه.</div>
<div class="tg-footer">👁️ 46.6K · <a href="https://t.me/MatinSenPaii/3825" target="_blank">📅 21:15 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3824">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/CflnGrM9wkL_znh2e5ejgwutoTrbA1scKVGxBwR_AAOXK1EvHBPXqsOnDJG6ISdxw5Bagqol8OSJvJnz5PhwVKlI5EnLNI9C0E8RfDvv2l9cTzR5rQ3bO5qaJQYxCqCr1LInQ0RNvw1zCOe4AobLzWXvmPirWPh2otbsJ7LtAq9DxAxx-nzbAQK4L2BcU5hBszqudQZlw_BE8VOttJdAA0HLfequZiIdF6AAz-ylcrOaFIEBaraFzyBMV_13o5uzuS4vjqAsvTBEUNA4WjgRxWTBYfuUo9RbE5tN_HRE7_dXnQEDvZhE7cmB3ftdBziFrynadx4HsSrON7rU-28B1Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شیائومی از MiMo Code رونمایی کرد
توی این مجله‌های زرد دنیای AI بهش لقب «قاتل Claude Code و OpenCode» رو دادن؛ ولی بذارید واقع‌بین باشیم — یه سری ویژگی‌های جذاب داره، اما قاتل این دو تا عزیز دل نیست
😁
(مخصوصاً که خودش
فورک OpenCode
هست!).
خلاصه‌ی ماجرا: تیم MiMo شیائومی به‌تازگی، دو روز پیش (۱۰ ژوئن ۲۰۲۶) نسخه‌ی
v0.1.0
از یه
AI coding agent اوپن‌سورس
با لایسنس MIT منتشر کرده که توی ترمینال کار می‌کنه و برای پروژه‌های پیچیده و
long-horizon
(بیش از ۲۰۰ مرحله) ساخته شده. این ابزار فقط کد نمی‌نویسه؛ می‌تونه دستور اجرا کنه، با Git کار کنه و در طول جلسات مختلف، درک عمیقی از پروژه‌ت رو حفظ کنه.
از اون‌جا که نسخه v0.1.0 هست، طبیعتاً یه پروژه‌ی اولیه و اکتشافیه — ولی معماری‌ش جدی و قابل‌بررسیه.
ویژگی‌های جذابش:
۱. حافظه ماندگار (Persistent Memory):
برخلاف ابزارهای فعلی که فقط به context window مدل تکیه می‌کنن، اینجا یه subagent جداگانه (به اسم checkpoint-writer) توی پس‌زمینه کار می‌کنه و تصمیم‌ها و پیشرفت رو لحظه‌به‌لحظه ثبت می‌کنه. حافظه روی
SQLite FTS5
(جست‌وجوی full-text) ذخیره می‌شه و توی فایل‌هایی مثل
MEMORY.md
،
checkpoint.md
و
tasks/<id>/progress.md
نگه‌داری می‌شه. وقتی context پر می‌شه، خودش از روی آخرین checkpoint بازسازیش می‌کنه؛ یعنی دیگه نیازی نیست پروژه رو از اول یاد بگیره.
۲. ویژگی Dream و Distill (خودتکاملی):
دستور
/dream
به راحتی جلسات اخیر رو اسکن می‌کنه، دانش مهم رو به حافظه پروژه منتقل می‌کنه و موارد قدیمی رو حذف می‌کنه. دستور
/distill
هم کارهای تکراری رو پیدا می‌کنه و تبدیلشون می‌کنه به skill یا command قابل‌استفاده مجدد. هر چی بیشتر کار کنی، بهتر «پروژه‌ی شما رو می‌شناسه».
۳. قابلیت Max Mode (آزمایشی):
چند راه‌حل موازی تولید می‌کنه (best-of-N) و با یه مدل داور بهترین رو انتخاب می‌کنه. که با
experimental.maxMode
توی فایل کانفیگ می‌تونید فعالش کنید.
۴. قابلیت Goal Mode:
با دستور
/goal
یه شرط توقف تعیین می‌کنی؛ وقتی agent می‌خواد متوقف بشه، یه
مدل داور مستقل
چک می‌کنه که واقعاً شرط برآورده شده یا نه — در نتیجه جلوی توقف زودهنگام و خوش‌بینانه رو می‌گیره.
۵. ویژگی Compose Mode:
با زدن کلید Tab فعال می‌شه و یه workflow ساختاریافته برای توسعه مبتنی بر spec ارائه می‌ده — با skillهای داخلی برای planning، اجرا، code review، TDD، دیباگ و merge. کل چرخه از spec تا کد نهایی.
۶. ورودی صوتی، Git و Multimodal:
ورودی صوتی real-time با
/voice
(بر پایه MiMo ASR و TenVAD، مخصوص کاربران لاگین‌شده)؛ مستقیم با Git پروژه‌ت کار می‌کنه و multimodal هم هست.
۷. سازگار با Claude Code:
authentication، skillها، MCP serverها و دستورهای قبلی رو توی یه مرحله import می‌کنه از پروژه‌ای که داشتید با Claude می‌زدید.
۸. انعطاف‌پذیری مدل:
MiMo Auto به‌صورت
رایگان(1 میلیون توکن اگز اشتباه نکنم) برای مدت محدود
و بدون کانفیگ در دسترسه، ولی خودش هم از هر API سازگار با OpenAI و prov/erهایی مثل Anthropic، DeepSeek، Kimi و GLM هم پشتیبانی می‌کنه — یعنی vendor lock-in نداریم.
نتیجه؟
طبق ادعای شیائومی، توی بنچمارک‌های SWE-Bench Pro و Terminal Bench 2 (به‌ترتیب ۶۲٪ و ۷۳٪)، با همون مدل پایه حدوداً
۵ درصد
از Claude Code جلوتره(که هنوز بعید میدونم. به چینی‌ها اعتماد ندارم). اما می‌گن تفاوت واقعی‌ش جایی خودش رو نشون می‌ده که کار طولانی و چندمرحله‌ای باشه — نه «له کردن»، ولی برتری معناداری توی long-horizon.
نحوه استفاده (خیلی ساده):
۱. نصب یک‌خطی (Mac/Linux):
curl -fsSL https://mimo.xiaomi.com/install | bash
(بهترین تجربه با iTerm یا ترمینال VSCode)
ویندوز:
npm install -g @mimo-ai/cli
۲. اولین اجرا:
خودش راهنمایی می‌کنه — MiMo Auto (رایگان) رو انتخاب می‌کنیم، با حساب شیائومی لاگین می‌کنیم، از Claude Code Import می‌کنیم تنظیمات و... رو، یا خودمون می‌سازیم.
۳.
می‌ریم تو پروژه و کار رو بهش می‌سپریم (با زدن Tab بین agentهای build / plan / compose سوییچ می‌کنیم).
لینک‌ها:
- گیت‌هاب:
github.com/XiaomiMiMo/MiMo-Code
- سایت:
mimo.xiaomi.com/en/mimocode
- بلاگ فنی (درباره long-horizon):
mimo.xiaomi.com/en/blog/mimo-code-long-horizon
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 48.3K · <a href="https://t.me/MatinSenPaii/3824" target="_blank">📅 19:33 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3819">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/CYEuFwmaO2qXJoMwjkeQ_GBOw3hVD6EIaqopit3uFU1-Yy4Ohllm9kKwTtMjeuPqxfgTIszYmbSqBHDTwS_X06wHOaGsrdzHlw9GBfybpAotF8gMLRiir3eYcTcPkY6rERkxtSgtlMeLSWlfwwDuZY2MmGKbZg-aCHlbdAUkuFg8L7Y8A_Q7aH2DALLjK4Rkj-DxEyw069JuhMa7usQiwzPLaEnpe8DEMqr_59MwQHXiJtyT_ETLvGNkTtwUylYclWyfxVJJIetZ3IwPCMtrdZ13dQpayYg3WXchpWCMfBspB79OFE3tvIP-1coOAmEcGP0TqBWxR4Jj1l92057UsA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اگر از ChatGPT بپرسید که
یه عدد بین ۱ تا ۱۰۰ انتخاب کن
بهتون به احتمال زیاد میگه 73! علتش رو هم از خودش پرسیدم:
وقتی کسی می‌گوید «یه عدد بین ۱ تا ۱۰۰ انتخاب کن»، من واقعاً عدد تصادفی تولید نمی‌کنم؛ بیشتر یک عدد دلخواه را انتخاب می‌کنم. بعضی عددها مثل ۷۳، ۳۷، ۴۲ یا ۶۹ به خاطر الگوهای آماری و داده‌های آموزشی بیشتر از بقیه به ذهن مدل می‌آیند.
جالب اینجاست که در آزمایش‌ها، وقتی از انسان‌ها می‌خواهند یک عدد «تصادفی» بین ۱ تا ۱۰۰ بگویند، عدد ۳۷ بیش از حد انتظار انتخاب می‌شود. مغز آدم‌ها از اعداد خیلی گرد (مثل ۵۰) فرار می‌کند و به سمت اعدادی می‌رود که «تصادفی‌تر به نظر می‌رسند». من هم تا حدی همین سوگیری را دارم.
پس اگر چند نفر قبلاً همین سؤال را پرسیده باشند، کاملاً ممکن است من دوباره ۷۳ را گفته باشم
امروز توی توییتر اینو دیده بودم و واسم جالب بود علتش</div>
<div class="tg-footer">👁️ 49.3K · <a href="https://t.me/MatinSenPaii/3819" target="_blank">📅 15:35 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3818">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/NLZUe0ODhDCHS0dgfujTDj7WFpyk_GgP_WIa7WZ_VWgaGm7BIKE069zAw2mEYG8ZJxlyaK9WFhiF57t6AwVCt0ZsiUWz8bC0WgwNAXuGpWOcaigHzIXNYyDduYwrG8Ib1lK2WaaMz9ocOKyRW0aAVd7xOcahJTJD1Inwn6bqtv8AMTANLohRt1sdb7-4vOnoTEVbOR1nGrLGXtFrsmxeoR1rwXSnUSWHWeor-e2GMPMAu9RELHgqGWUJANaogdTWnkgmOVhlYg-W-ZnCPxmxpJ4hcVfBW4ZasRIu0scf1Y5NnQ-tXRK4GfN3OZcYnaa-WFjy_xgRtJ27J0LZLVdoKQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یه ابزار باحال آنلاین پیدا کردم: یه عکس می‌دی بهش، بهت گرادینت میده با کلی تنظیمات.
برای وقتایی که دنبال یه بک‌گراند یا پلت رنگی هماهنگ با یه تصویری، عالیه.
تو مرورگر کار می‌کنه و رایگانه
👇
photogradient.com
‎
✍️
Reza</div>
<div class="tg-footer">👁️ 48.6K · <a href="https://t.me/MatinSenPaii/3818" target="_blank">📅 14:18 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3817">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromxsfilternet | فیلترنت(امیرپارسا گودمن)</strong></div>
<div class="tg-text">🍷
درود به همه رفقا
ابزاری که امروز معرفی میکنم...
داخل این سایت میتونید تمام ip های مربوط و بنا بر نت خودتون چه برای ورکر و کلودفلر یا شیر و خورشید اسکن کنید
❗️
ویژگی ها:
💡
اسکن راحت و سریع و دقیق
رابطه کاربری خوب برا همه سیستم ها
داشتن ip بیشتر cdn ها
لینک سایت:
✅
https://cdn-scanner-pro.vercel.app/
توسعه دهنده
@xsfilterrnet
👑</div>
<div class="tg-footer">👁️ 40.5K · <a href="https://t.me/MatinSenPaii/3817" target="_blank">📅 12:28 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3816">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2658a29175.mp4?token=kfkPiaiqUX1nRLHfv1RCGS9LK1qE5SRpXskFEJANeEl17kr4k_cCRQStJRFlPWOeCePWgDRlNTHrMhnb5Uv-8qkoevcoSKjWWSs9NnehHNUMGXFq5JIvrmlQ19etSI_YvXSA3_3Lur2HFwIQQdxAS4yxF5QtIEWPcIFvcDcqhE2kgUHanUZZgWANmq0K0vyvPO_2RatfF07sc47fchOHGjR2JrSYyh6hxrqT83J1S0kB6_xKbhkhMsOSm7yyPW6RZXHnFA_B8S36BuifIC-jYCL2au7EGS1GthWBR0Wb6RInF3zI5eYmn5Ar_ejMvVeuu0fk69_AWmzHG6OEPojsZQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2658a29175.mp4?token=kfkPiaiqUX1nRLHfv1RCGS9LK1qE5SRpXskFEJANeEl17kr4k_cCRQStJRFlPWOeCePWgDRlNTHrMhnb5Uv-8qkoevcoSKjWWSs9NnehHNUMGXFq5JIvrmlQ19etSI_YvXSA3_3Lur2HFwIQQdxAS4yxF5QtIEWPcIFvcDcqhE2kgUHanUZZgWANmq0K0vyvPO_2RatfF07sc47fchOHGjR2JrSYyh6hxrqT83J1S0kB6_xKbhkhMsOSm7yyPW6RZXHnFA_B8S36BuifIC-jYCL2au7EGS1GthWBR0Wb6RInF3zI5eYmn5Ar_ejMvVeuu0fk69_AWmzHG6OEPojsZQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">فیگما یه اکستنشن کروم منتشر کرده(فعلا برای کاربرای پلن پرو) که با رفتن توی اکثر وبسایت‌ها، می‌تونید با یه کلیک، تمام اون صفحه‌ی وبسایت رو به شکل فایل قابل ادیت فیگما دریافت کنید.
برام جالبه که سر بحث کپی‌رایت و اینا کسی بهش چیزی نگفته هنوز
😁
اما خب گویا هنوز با چنگ و دندون قصد دارن نگه دارن اکوسیستم فیگما رو بعد از اون سقوط سنگین سر Claude Design
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 48K · <a href="https://t.me/MatinSenPaii/3816" target="_blank">📅 11:49 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3815">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">‏این روزا اسم Agent Harness رو زیاد میشنویم، ولی بیاید ببینیم واقعا چیه و به چه درد میخوره!  همونطور که میدونیم context window مدل‌ها محدوده و اگه به صورت کارآمد ازش استفاده نشه، خیلی سریع پر میشه و مدل مجبوره برای ادامه، یک دور summarization انجام بده.  بعد…</div>
<div class="tg-footer">👁️ 47K · <a href="https://t.me/MatinSenPaii/3815" target="_blank">📅 10:10 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3814">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/L7wIgtVtJBula956pkGLuieLNsWkj5RwYHl0iX4KQI3a0SQXUDzqd_UrjeUosQzWR7TMrWjyIe_4rEBOp2CQRHinkBUeqvamJCx9KwIVsiGHQqLDtv7p0O73hyp3imLdAfSDXqFInEhQ6JySsiWDoWNoY5lN9C9prk5434D6sJUdY9CHjkRmWCNgDRj8s_KedUAHKDiLqo1TxyRFRNKEpvHtgagO13JxIMvtDLzwykzeUt8rmPJ47JR8hb_wbaHISJhjHoa01xyhBER-MvJ_Hr1kWCq5affAwphL9U6gakTwkuTXOq5cIlhhZH8dn36AnyHNbdC-v4rAeJDfVvGQfw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏این روزا اسم Agent Harness رو زیاد میشنویم، ولی بیاید ببینیم واقعا چیه و به چه درد میخوره!
همونطور که میدونیم context window مدل‌ها محدوده و اگه به صورت کارآمد ازش استفاده نشه، خیلی سریع پر میشه و مدل مجبوره برای ادامه، یک دور summarization انجام بده.
بعد از چند دور summarize کردن، نهایتا بخشی از دیتای مهم از بین میره و تسک به صورت کامل انجام نمیشه! پس اومدیم یک سری تکنیک پیاده کردیم مثل تقسیم کار بین sub-agentها تا از پر شدن سریع کانتکس اصلی جلوگیری کنیم.
بعد این ایده مطرح شد که بیایم هدف نهایی (PRD) رو تعریف کنیم و اون رو به تعداد زیادی sub-task تقسیم کنیم، بعد مدل رو در یک loop بندازیم که با هر بار اجرا، یک context و یک prompt جدید داشته باشه و بعد از هر iteration چک کنیم که تسک به صورت کامل انجام شده، و در غیر اینصورت چرخه رو دوباره تکرار کنیم!
در واقع به جای اینکه برای اتمام تسک به مدل اعتماد کنیم، ما در یک لایه بالاتر این رو validate میکنیم و اجینتِ تنبل رو harness می‌کنیم :))
✍️
Amir</div>
<div class="tg-footer">👁️ 50K · <a href="https://t.me/MatinSenPaii/3814" target="_blank">📅 09:07 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3813">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/hv26ajreYO9kQhTKEdUdgG1GaR6siKVRxOjYh8Q31_hIfyu_rzKkcRrI6pXwgm6H4jjMA3CotWkmB6Zin337gjrjI8Pn1AlNGcks2HlMs857uGYU8QxxzBK1XW6IRDv4t4yUpfnXjPYunaTgBC3mh5NnWM4-tgv8uR-gFlwUR7JRJxJHQ__Ju36veJNeHA0Op0WPESezPzSc1MhXUhU6ZFVO_wFmsW-yWwq8HOdnC5D6-ugiETcM8hSrco7x3aJU2L1dcEnCng9vMSwuY84EOuKyFs5pQgSEG-AXYqAIjAvHVQ7aDyuyo431tIbKL2TXb_8Ld2D-8jE3jsWm3MgvUA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بله شما می‌تونید دامنه و سرور خارج رو از سایت‌های ایرانی هم بخرید، اما چندتا نکته وجود داره:
۱- احراز هویت سایت‌های ایرانی کلا جالب نیست و خب این ریسک رو باید در نظر داشته باشید
۲- توی شرایط قطعی، فروش دامنه و سرور همه‌ی این سایت‌ها میره روی هوا
۳- شاید عجیب باشه شما اگر از سایت‌هایی مثل netlen و با کریپتو خرید کنی دامین+سرور رو، شاید ۸۰۰ هزار تومن(با کارمزد و همه‌چیش) پات بیفته. اما همین دوتا رو از سایت ایرانی بخری زیر 1 تومن نیست</div>
<div class="tg-footer">👁️ 49K · <a href="https://t.me/MatinSenPaii/3813" target="_blank">📅 07:01 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3811">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">نکات استفاده</div>
<div class="tg-footer">👁️ 48.7K · <a href="https://t.me/MatinSenPaii/3811" target="_blank">📅 01:14 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3809">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/DhQIJaVMAiYzbXbpsCYvcWtwEQDThvYXJdNCjBMF40x5mAYevrjGpXppFb3DSpZLWzjRU3WVSbXgdihIa1QRRC-Fp7ngQTiOKmbiLByCrZtxfe9OnNDEc8NmrzFaBl-l7jcDPh1DEvYYzZ_jEgZuvj7I9ovz8ItzZXMbWzx5LeaGL3eDGHJcMA9V9JB4o_43hidhKI0t43rfNcY9d6Xc8Jbd1jufSKJEIMVG9KmwfMLNx8hMpiXwysgC1MskPqqnNdm-_J-2SX4bnNCX-Eaz6g-p9QolRzWm6QNY9uc2CqRxuH-QuLYL89Z0SnbxKRgtGEpDhpt3aLq2xe7zcrKFrw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">https://github.com/patterniha/Serverless-for-Iran  * دسترسی مستقیم و بدون واسطه و با حداکثر سرعت به تقریبا تمام سرویس‌ها و وبسایت‌ها (به جز تلگرام)  ///  * حتما باید از Xray-core >= 26.6.1 استفاده کنید (v2rayNG >= 2.2.3)  * کافی است لینک subscription را وارد…</div>
<div class="tg-footer">👁️ 50K · <a href="https://t.me/MatinSenPaii/3809" target="_blank">📅 00:13 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3808">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromPatt's Channel</strong></div>
<div class="tg-text">https://github.com/patterniha/Serverless-for-Iran
* دسترسی مستقیم و بدون واسطه و با حداکثر سرعت به تقریبا تمام سرویس‌ها و وبسایت‌ها (به جز تلگرام)
///
* حتما باید از Xray-core >= 26.6.1 استفاده کنید (v2rayNG >= 2.2.3)
* کافی است لینک subscription را وارد برنامه v2rayN/v2rayNG کنید:
https://raw.githubusercontent.com/patterniha/Serverless-for-Iran/refs/heads/main/Subscription/Serverless-for-Iran.json
* نکات استفاده رو حتما مطالعه کنید.</div>
<div class="tg-footer">👁️ 40.6K · <a href="https://t.me/MatinSenPaii/3808" target="_blank">📅 23:52 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3807">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/jLRS0y3IbUHxZ28xo968naWGzeSm-fn5-LpXjLbZwtLA1MatoKqUmxMib1EIPWx2_nFTpdZ36haUbNZaWW0A2HPBJvdk9oSuibVq5uBcFdvb1Hxe-iULPJsCOz6-X5UtXuXVe8EX-OOMtSCRm3pmphtO6mHH_Si82pYIEqIerv11XQB3mudSiuywR4U1obmZxeOZP_h_0puWkdiAwgvdgR0wyBhPuYVKiH9Iv6RMLepcTrJEJ7IljfSgtSYDd-_ZmOdDe7Yc6Tss_M5P9C_4m4rDgcWvKRU0Ksly2iwRjYP3sxEBl_02L6hyO4WQlPW5N1UYzux4q-XEIZxMLaT5uQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اگر از http://Netlen.com.tr بخرید، دامنه یه دلاری هم می‌تونید بگیرید و با یه سرور ۳ دلاری و کارمزد، کلا میشه ۴.۵ دلار یعنی کلا ۸۰۰ هزار تومن. دامنه یه ساله هست، سرور یه ماهه. یعنی ماهیانه ۶۰۰ هزار تومن تقریبا. ۵ نفر باشید میشه ماهی ۱۲۰ باز هم خود دانید</div>
<div class="tg-footer">👁️ 45.4K · <a href="https://t.me/MatinSenPaii/3807" target="_blank">📅 23:52 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3806">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromxsfilternet | فیلترنت(امیرپارسا گودمن)</strong></div>
<div class="tg-text">درود به همه رفقا
🍷
اگر از پنل bpb و... استفاده میکنید میخواید ip ثابت باشه ولی جز لوکیشن آلمان
🇩🇪
میتونید از ابزار زیر استفاده کنید برای ip های مختلف برای مثال:
میتونید از ip چین استفاده کنید برای دور زدن تبلیغات یا از ip آمریکا برای بیشتر هوش مصنوعی ها خلاصه این ابزار مشابه واسه خود bpb برای ثابت کردن ip هست ولی با لوکیشن بیشتر
❗️
لینک پروژه:
✅
https://smart-ip-scanner.10-354.workers.dev/
توسعه دهنده
@xsfilterrnet
👑</div>
<div class="tg-footer">👁️ 43.2K · <a href="https://t.me/MatinSenPaii/3806" target="_blank">📅 22:50 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3805">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">‏خطر سرقت اطلاعات و رمزهای عبور؛ مراقب نسخه‌ی جعلی X-VPN باشید  محققان شرکت «سایدرز» (Cyderes) کمپینی فعال را شناسایی کرده‌اند که در آن نسخه‌های جعلی چند برنامه محبوب برای انتشار بدافزار استفاده شده‌اند. یکی از مهم‌ترین نمونه‌ها، نسخه جعلی اپلیکیشن «ایکس وی‌پی‌ان»…</div>
<div class="tg-footer">👁️ 43K · <a href="https://t.me/MatinSenPaii/3805" target="_blank">📅 22:05 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3804">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/V1AvyDrGZFkA8a-XHszgTTR_Ovq6o3CMvBTW77gI1lKopuRNDjZoEH-UC-Wz-_E7lm5dWSbUv2V95ejYYQTIbeL3EDO22O97YsC5pW5NuAEdvG4qbKAw7cBSiizbh3nuMoH_zsermGK7dHJD3vZYge3awSMBgZR6LyK59QPty8KXS49aVaIdSgFJTAsKaUG5Vn4CNBVefej7VgeeyEfxankwJqqXgaTFoRBVJGDXfY6_Ki8UcpuMzDGPOxV9gXNM7myTYYuKdv1gMe9_EXIiTDxhz3J_RBmsYurQjWdNSsdiFRGrb1BkfRILBWXDqJ2FpHrDAvtUUKYO_K28EVJRfA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
خطر سرقت اطلاعات و رمزهای عبور؛ مراقب نسخه‌ی جعلی X-VPN باشید
محققان شرکت «سایدرز» (Cyderes) کمپینی فعال را شناسایی کرده‌اند که در آن نسخه‌های جعلی چند برنامه محبوب برای انتشار بدافزار استفاده شده‌اند. یکی از مهم‌ترین نمونه‌ها، نسخه جعلی اپلیکیشن «ایکس وی‌پی‌ان» (X-VPN) است که برای نصب بدافزاری به نام STX RAT روی سیستم قربانیان استفاده شده است. این بدافزار می‌تواند رمزهای ذخیره‌شده، نشست‌های فعال و اطلاعات سیستم را سرقت کند و به مهاجم امکان اجرای دستور از راه دور بدهد.
در این حمله سرویس ایکس وی‌پی‌ان هک نشده و کانال‌های رسمی دانلود این برنامه سالم هستند. خطر اصلی متوجه کاربرانی است که نسخه آلوده را از منابع غیررسمی (در این مورد، یک مخزن ناشناس در سرویس Bitbucket) دانلود کرده‌اند. در پاسخ به این تهدید، ایکس وی‌پی‌ان به‌سرعت آپدیت نسخه ۷۷.۵.۳ ویندوز را با کنترل‌های سخت‌گیرانه‌تر منتشر کرد.
➕
نوشدارو پلاس: این هشدار مشخصاً به نسخه ویندوز X-VPN مربوط است، آن هم زمانی که کاربر نسخه جعلی و دست‌کاری‌شده را از منابع غیررسمی دانلود کرده باشد. طبق اعلام X-VPN، نسخه‌های رسمی دریافت‌شده از وب‌سایت X-VPN یا Microsoft Store تحت تأثیر این سناریو نیستند.
▪️
روش زیرکانه هکرها برای اجرای حمله
این کمپین ابتدا با نسخه‌های جعلی برنامه‌هایی مانند «بایننس» (Binance)، «بای‌بیت» (Bybit)، متاتریدر ۵ (MetaTrader 5) و کیف پول اکسودوس (Exodus)، معامله‌گران را هدف قرار داد. آن‌ها حتی به سراغ پلتفرم بازی استیم نیز رفتند و در نهایت تمرکز خود را روی کاربرانی گذاشتند که از ابزار تغییر آی‌پی ایکس وی‌پی‌ان برای حفظ حریم خصوصی بهره می‌برند.
💡
نکته: بد نیست بدانید شرکت Kaspersky (کسپرسکی) پیش‌تر متوجه شده بود که همین بدافزار با نفوذ به سایت CPUID، بیش از ۱۵۰ قربانی را در صنایع و کشورهای مختلف آلوده کرده بود.
بر اساس یافته‌های شرکت سایدرز، مهاجمان در فایل نصبی اپ‌های معتبر یک فایل مخرب به نام CRYPTBASE.dll جاسازی می‌کنند؛ تکنیکی که به آن «بارگذاری جانبی» (DLL Sideloading) می‌گویند.
به دلیل ساختار سیستم‌عامل ویندوز، فرایند نصب برنامه در ظاهر کاملاً عادی پیش می‌رود، اما فایل پنهان‌شده، بدافزار را مستقیماً به حافظه دستگاه تزریق می‌کند تا آنتی‌ویروس‌ها متوجه ردپای آن نشوند. پس از فعال‌سازی، بدافزار می‌تواند ارتباطات خود را در قالب ترافیک عادی و قفل‌گذاری‌شده وب پنهان سازد.
▪️
چطور قربانی برنامه‌های جعلی نشویم؟
دفاع در برابر این نوع حملات بسیار ساده است و نیازی به دانش فنی ندارد:
• دانلود از منابع رسمی: برنامه‌ها را فقط از وب‌سایت اصلی شرکت یا فروشگاه‌های رسمی دانلود کنید. این هشدار برای ما کاربران ایرانی که اغلب ناچار به دانلود از منابع واسطه هستیم، اهمیتی دوچندان دارد.
• تایپ مستقیم آدرس: برای جلوگیری از ورود به سایت‌های مشابه و جعلی، آدرس را مستقیم تایپ کنید و روی تبلیغات کلیک نکنید.
• استفاده از نرم‌افزارهای امنیتی: داشتن یک آنتی‌ویروس قدرتمند و به‌روز در کنار رعایت اصول دانلود امن، لایه محافظتی محکمی ایجاد می‌کند.
اگر گمان می‌کنید نسخه جعلی را نصب کرده‌اید، فرض را بر لو رفتن اطلاعاتتان بگذارید. فوراً رمزهای عبور خود را از یک دستگاه امن تغییر دهید، از حساب‌ها خارج شده و احراز هویت دومرحله‌ای را فعال کنید.
✍️
یونس مرادی(نوشدارو)</div>
<div class="tg-footer">👁️ 53.9K · <a href="https://t.me/MatinSenPaii/3804" target="_blank">📅 21:49 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3803">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/HEzjT0EAyCT4HFJaZGWGq9g1sBiJ4kyA_KW-61ujKOfsckSZd2cXUouodOTPXNMT0P6RmmdGbu6BfLHTqqGkqwVDZ3TWMjC6gQNjfStql4H4NT3GzoGzspSMuuoVpXen9vuVG2YDSuoqmAHLphS2IoNNXkgB9IAgZ3V_Hf2N_k2bCbN9TzA-shXkrpjJdrgQqcwyoioLQ22dL3-X8CvSXm5rae8lXlNJHY-J-F8R6f6wSvVUuLlrc1zCpyIq-bpylmeMyWyUcj0aMxkJQBcgv3RABkYtP4_SFpAM4awWEBEVwcZLtMMY2uNLqzw8b9dUrgOytqhxE7IoMyzc702cGg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏یه نکته‌ی جالب از کنفرانس WWDC اپل!
توی ویدیو هر بار که کلمه سیری گفته می‌شد فرکانس‌های ۳، ۴، ۵ و ۶ کیلوهرتز صدا رو کات می‌کردن. چرا؟
برای اینکه وقتی دارید ویدیو رو می‌بینید، سیری توی دیوایس‌های اطراف شما بی‌دلیل بیدار نشه.
✍️
Behrad Javed
منبع</div>
<div class="tg-footer">👁️ 44.5K · <a href="https://t.me/MatinSenPaii/3803" target="_blank">📅 20:34 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3802">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">اگر از
http://Netlen.com.tr
بخرید، دامنه یه دلاری هم می‌تونید بگیرید و با یه سرور ۳ دلاری و کارمزد، کلا میشه ۴.۵ دلار
یعنی کلا ۸۰۰ هزار تومن. دامنه یه ساله هست، سرور یه ماهه. یعنی ماهیانه ۶۰۰ هزار تومن تقریبا. ۵ نفر باشید میشه ماهی ۱۲۰
باز هم خود دانید</div>
<div class="tg-footer">👁️ 48K · <a href="https://t.me/MatinSenPaii/3802" target="_blank">📅 20:04 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3801">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">ببینید واقعا درک می‌کنم که ۶ دلار هزینه سرور و دامنه براتون زیاده، اما اگر سه چهار نفر با هم بگیرید بهتون فشار نمیاد. همه هم می‌تونید استفاده کنید
برای من سود و ضرری نداره صرفا می‌خوام بدونید که با نفری ۱۵۰-۲۰۰ میتونید راهش بندازید</div>
<div class="tg-footer">👁️ 46.4K · <a href="https://t.me/MatinSenPaii/3801" target="_blank">📅 19:58 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3800">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-poll">
<h4>📊 میتونم بپرسم چرا هنوز راه ننداختین؟</h4>
<ul>
<li>✓ هزینش زیاد بود واسم</li>
<li>✓ آموزش پیچیده بود واسم</li>
<li>✓ حوصله‌ام نشد و بعد از قطعی مغزم نیاز به استراحت داشت</li>
</ul>
</div>
<div class="tg-footer">👁️ 48.9K · <a href="https://t.me/MatinSenPaii/3800" target="_blank">📅 18:30 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3799">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">اینطور که من می‌بینم، قطعی در پیش داریم به زودی</div>
<div class="tg-footer">👁️ 49.7K · <a href="https://t.me/MatinSenPaii/3799" target="_blank">📅 17:17 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3798">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">تمام آموزش‌های مبنی بر اینترنت آزاد که من توی کانال یوتوبم منتشر کردم به علاوه‌ی توضیحات و اینکه توی چه شرایطی به چه دردی می‌خورن. از بالا به پایین، برای شرایط سخت‌تر معرفی می‌شن تا شرایط خاموشی کامل:  1- متد Paqet، ویژه‌ی شرایط الآن(کلودفلر و اینترنت بین‌الملل…</div>
<div class="tg-footer">👁️ 50.1K · <a href="https://t.me/MatinSenPaii/3798" target="_blank">📅 17:17 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3797">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">اینطور که من می‌بینم، قطعی در پیش داریم به زودی</div>
<div class="tg-footer">👁️ 52K · <a href="https://t.me/MatinSenPaii/3797" target="_blank">📅 17:14 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3796">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-poll">
<h4>📊 آیا سرور MasterDNS راه انداختید برای خودتون و خانوادتون؟</h4>
<ul>
<li>✓ آری👍</li>
<li>✓ خیر👎</li>
</ul>
</div>
<div class="tg-footer">👁️ 51.5K · <a href="https://t.me/MatinSenPaii/3796" target="_blank">📅 17:13 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3794">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">هرچی کانفیگ مرده بود با این تنظیمات واسم زنده شد. توضیحاتش رو هم میدم خدمتتون که هر کدوم چیه و Mux رو خاموش بذارید</div>
<div class="tg-footer">👁️ 51.4K · <a href="https://t.me/MatinSenPaii/3794" target="_blank">📅 16:09 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3793">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/U0rJCj7BV3H3nCyPh5wvbYOf9E1bY4h4isfythSw7yz98WebHBp0GUEyUxWqEgV0yB8WQ0PN2FOFsu6KeVxvuQdUnJ4FqV3JfDp6Muanloxz52kSUB2Be5CQwSfr-3jZXrGNpewL0TfAZh5vHQ-RHMzGQ7mQcm1QZk145g7urk9yR5B9wOoF97BUw8X0h2jcHvI9U-lbZztsy1_5kzPhq0g1ivBLnr0s1u3o8oYz0GcuXg1Ani_KTCz16U71r84RvxmoRLi5Iz39i-9fYUaB5jOpiVEisg_-LZQ1AInqkk6qbD_wHIYL3ssrgDVt6IS8mpItjZzxjgTDTQ6kHlxBuw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هرچی کانفیگ مرده بود با این تنظیمات واسم زنده شد.
توضیحاتش رو هم میدم خدمتتون که هر کدوم چیه
و Mux رو خاموش بذارید</div>
<div class="tg-footer">👁️ 49.7K · <a href="https://t.me/MatinSenPaii/3793" target="_blank">📅 15:48 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3789">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/nakgKMlfXT1uVqHRaXhIVF-sl5Ks1l7DQq4vooVJhtfwezAe0giC_9M_Yb9UINqbGdf2_3JS7mU5BeovTD1q6NvV8mLhi-Ho6G8d43wzlvvwvEuhKAGCvt6rIC7cGk4cz8ATnkihKuDM0KC_nA-ALE2c8vrtpNfVTsHvI_VOgSfOu6m-u11YSeD0XJk3bdxnsyS-YpWrJqm0UJ7xQpdVaBUvDbLKM1VoQMUCy-CLSe1Qqedr6633NoFU5y6dwvmusQBF43GYyyB8YPXflIqF41PWziJ2FplxVfkLDbUkSOxHqHB767JSWtVR0jpW-O7qkkt144VZTzQorWi7U2v3Xw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/t-2XFhT6S8zySBfnC2-SMuJMmiUJvAxvY7SXo0XsEpVYkwLZMW4LKoQ-uumLAvgfsd0p3XMCpvAXvrYsPqEItahydkkXAOQkXHu99xFOpTQdnS4OBRhlKO5_PlLa1iUis3xyUE_jlTqKPY9zXURA66Yt3WKyHFRxJLzfp-5cDWqCpqTtu7ZjgpJkZWaULKLLz_sQKsTZ6GUAcBuxZM3VgRds1_ofSb9cQnTRh3uo66kE5-lwnNs83QGlXNgy9WLeAWH-C-dj7gPxeI86qgZrEAJOLsjsYnGUVYqCJlaMtmwTT3XX4GieIVRaQ6F7Gb3VQ8IsvNl_vqYNzMs1tec2bw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/kfdU7lvNZEAHl-KnjZuAQisnE6fAK9RemfMkjAWcSBC0lj8sExozhaZh0mjyI7I3Ej5TDrkCOtaGJ5xl3H_9UlrTUC27ih2SYBPp52coa_P_OoRgdP9C2VbVZhPqJxGzLDOBUZVqeXHm7N-BXzhuKuQy5Mau_Ti6DRtiqKk3ZbYCnf2Mk_FQEoNQe2K0Uri8s7Qzo4MJfxQdSem4cVeN0Q5gjieL5OwZArNIh63VMUDPUmD118ngV1ZxSf7jRq3hNX1HOBPMhuCVKw8fE2PowZfhAFyhFLY_wxmhBUprUPMTx7WlokMw4KwQg6n_vlhV4FIU9FCQPmPTEY5q1oVaag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/NjTmmZ_qUszdkE1qaD-4s3tFqbZNdJJY6CAVnBts99drufq6JxRQB1dJssL47Iy_gBst7K1FoFE79zu2lqaj7HQN8pLI6Xb86648Uve_uu3YlyVKywFo1HH4FsoyxmhKV6h9FrR2T7jxcvyrwTiHyq-31GANTODCHGSF7VnQUqKo1WLDnVtRoOli1RVnjSMzCccAmJTtN9JF-cAsgr2hF95K8wmKFM3bRjW5PnKzNJMIwcray54o16slxf77a5GnRlLXIGx1mqs7DxuUlrflKiD5pdOZk6iQV0HyZurfaFY5VBjN1i6AsWbktcF-xwD3ZNzaLM-A-RwnYgUKJEQQaw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">آموزش فعالسازی Fragment توی اپلیکیشن MahsaNG برای رفع مشکل سرعت آپلود و محدودیت اتصال توی برخی نقاط
روی Auto بذارید فعلا، من در ادامه واستون یه سری تنظیمات پیش‌فرض می‌ذارم که تست کنید روی اینترنتتون
اگر الان کانفیگ واستون با سرعت خوبی وصله، نیازی به فعال کردن Fragment ندارید. چون سرعت کلی رو پایین میاره</div>
<div class="tg-footer">👁️ 52.8K · <a href="https://t.me/MatinSenPaii/3789" target="_blank">📅 13:39 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3788">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">ما آخر نفهمیدیم جنگ شد یا نشد</div>
<div class="tg-footer">👁️ 54.4K · <a href="https://t.me/MatinSenPaii/3788" target="_blank">📅 09:15 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3784">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">امیدوارم
WhiteDNS
ستاپ کرده باشید. برای اتصال توی شرایط جنگ
دیگه حوصله‌ی اصرار نیست</div>
<div class="tg-footer">👁️ 60.9K · <a href="https://t.me/MatinSenPaii/3784" target="_blank">📅 01:40 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3782">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">اگر خواستید مفهوم فیلترینگ منطقه‌ای رو بفهمید، سوار اتوبوس بشید و از تهران برید خوزستان. به هر شهری می‌رسید آیپی تمیزهاتون از کار میفتن و باید دوباره اسکن کنید. به استان خوزستان که می‌رسید، گوشی تبدیل به یه پاره آجر بی‌مصرف میشه و فقط می‌تونید باهاش زنگ بزنید
😂</div>
<div class="tg-footer">👁️ 56.9K · <a href="https://t.me/MatinSenPaii/3782" target="_blank">📅 01:18 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3781">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/kDFJHcHvQQZGbBQhNm4r5dtRXf5y_r_Sqwf5H7nYWt81_7-fD14RhJ07pP9vFoyzRqBxRPbVcqfC4145K83QmZi9VjHc98lwPPx302kPpBD1WIViwIlmFKkvL8qdR6uNGGc_q1bhXdblzTH5ZPp9X5nVdMsXO91CcBKGgBJwAETXoKaBC_iHIHE2LBjuQ5wii9c07bhEwnOGb75O4FBD8_Ui1fTy-dFeZIHZyUhE-pUxCCRocjQf3FZU5WHQjo6gLxk15vcgcHt_kk-I5RQtsTgAdNsHDFkd1A-wF-bnQymgQewk3T8moC8_wUYLkr_WrSbpN_QbtpzkjipIcOaB3A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏وقتشه یه سری حقایق راجب بورسیه MEXT ژاپن بگم.
حالم از این پوسترا مخصوصا راجب بورسیه‌ی ژاپن به هم می‌خوره.
واقعیت:
۱- از چندین هزار متقاضی، سالانه زیر ۵۰ نفر(متغیر) مجموعا از تمام مقاطع برگزیده میشن که اونم کاملا شانسیه.
۲- انتخاب شدن شما تماما به نیاز ژاپن بستگی داره و اصلا هم اعلام نمی‌کنن که ما به فلان رشته نیاز داریم. ممکنه شما تمام شرایط عالی رو داشته باشی با بالاترین نمره، اما «امسال ژاپن به رشته شما نیاز نداشته باشه»(مقطع ارشد و دکتری) و این رو به صورت مبهم فقط بهتون میگن که شما رد شدید! یعنی هیچ دلیلی برای رد شدنتون بهتون نمیدن توی هیچ مقطعی. شخص A با دانش نزدیک به صفر بدون بلد بودن انگلیسی یا ژاپنی قبول میشه چون ژاپن این رشته رو نیاز داره، شخص B بدون توضیح رد میشه با اینکه دانش و علم خیلی بالایی داره یا حتی مدرک زبان ژاپنی داره، چون به رشته‌اش نیاز ندارن. و فقط میگن رد شدی بدون توضیح.
۳- روند غربالگری به شدت غیراستاندارد، و رد شدن توی هر مرحله بدون توضیح هست(سه مرحله داره شامل ارسال مدارک و آزمون کتبی و مصاحبه که هرجا رد شدید، علتی نمیگن)
۴- ثبت نام برخلاف به روز بودن خود کشور ژاپن، به صورت کاملا سنتی و با پست کردن مدرک کاغذی برای سفارت توی یه فرآیند بسیار زمان‌بر و استرس‌زا(نکنه فلان چیز رو یادم رفته باشه) و هزارتا دنگ و فنگ انجام میشه. همه چیز کاغذی. همه‌چیز. یعنی حتی زحمت نمی‌دن به خودشون کد ملی شما رو وارد کنن اطلاعاتتون رو بگیرن. و توی همه‌ی ۱۵-۲۰ تا مدرکی هم که می‌خوان، یه نقطه اگر اشتباه باشه رد می‌شید توی مرحله‌ی اول. که باز هم توضیحی نمی‌دن بهتون که چرا رد شدید. صرفا میگن نقص مدارک
۵- شما ممکنه تمام تلاشتون رو بکنید، همه‌ی مراحل رو قبول بشید، اما در نهایت ژاپن توی اون سال Mext رو برای ایران کنسل کنه!! بله درست شنیدید. پارسال به خاطر جنگ ۱۲ روزه، ژاپن بورسیه‌اش رو برای ایران لغو کرد(
🤣
🤣
🤣
) صرفا چون تایم آزمونش جنگ شد. به تعویق هم ننداخت. لغو کرد. امسال هم همین شد دقیقا و به دلیل وضعیت کشور، لغو کرد. و تمام کسایی که پارسال و امسال هدفشون رو گذاشته بودن Mext، گند خورد به زندگیشون.
خلاصه‌ی کلام اینکه برای بورسیه تمرکزتون رو روی ژاپن به تنهایی نذارید و چندین تا کشور زیر نظرتون باشه</div>
<div class="tg-footer">👁️ 56.2K · <a href="https://t.me/MatinSenPaii/3781" target="_blank">📅 00:46 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3780">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/r5dqosT-DiNQdpLXujJAghTLWjeOi5XErFsNMusefeagtHuR8DhgKy987SFypir7CxXx9aiHkVT16WhyShHg7e5k_hgDSuvA-Z-U4UtG4VAFFIOysoheB_kHs7JsmpJKygIrjkp6oVCOG4hpq2JiltuQ7-cWe3o2AYoQh1l-NGb-fLCi5d3onS2nukchTVntV0MoRRzkZElIs5bK3R4olbfPv3SPWEnFcGx34CDMCKoLrFG1PsxNvxD9-CDL6g-7EFlzgM7XcFI-GCWbUYcXUPQ1bmuhcTJIHzvQmUxJty0iWLBGdLWCQhSCP5Go6zTq2zLe4U_esa23cTQMHA8JJw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⭐️
پروژه‌ی FreeLLMAPI — یه پروکسی OpenAI-compatible فوق‌العاده‌ست که ۱۶ تا از بهترین ارائه‌دهنده‌های LLM(مدل‌های زبانی بزرگ. همون هوش مصنوعی خودمون) رایگان رو روی هم جمع کرده!
تقریباً ۱٫۷ میلیارد توکن توی هر ماه ظرفیت inference (از Google Gemini، Groq، Mistral، Cerebras، OpenRouter، GitHub Models، Cloudflare، NVIDIA، HuggingFace و ... + هر endpoint سفارشی مثل Ollama، vLLM، LM Studio و غیره) می‌ده.
ویژگی‌های اصلی:
🔤
یه endpoint واحد (/v1/chat/completions) برای همه‌چی
🔤
روتینگ هوشمند + failover خودکار (اگر یه کلید به rate limit خورد، سریع میره سراغ بعدی)
🔤
مدیریت دقیق quota هر api key تا زیر حد استفاده‌ی رایگان بمونیم
🔤
کلیدها به صورت رمزنگاری‌شده ذخیره میشن
🔤
داشبورد باحال برای مدیریت api key
🔤
نصب خیلی راحت با Docker
در واقع همه free tierهای پراکنده رو تبدیل کرده به یه LLM قدرتمند و همیشه در دسترس، بدون اینکه مجبور بشی با کلی SDK و rate limit جداگانه کلنجار بری.
بهترین‌ها برای کدنویسی (بر اساس این پروژه و لیست هوش مصنوعی‌ها) عمدتاً DeepSeek V4 Pro، Qwen3-Coder سری (مخصوصاً Qwen3-Coder Next و 480B) و Codestral/Devstral هستن.
⚡️
لینک پروژه:
https://github.com/tashfeenahmed/freellmapi
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 51.1K · <a href="https://t.me/MatinSenPaii/3780" target="_blank">📅 23:43 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3779">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">من خودم با Hiddify راحتترم برای ساب، از اون استفاده میکنم کلا(با نت H+ الان دارم این پست رو می‌ذارم با همین ساب) اگر پینگ نداد، توی تنظیمات Tls Fragment رو روشن کنید</div>
<div class="tg-footer">👁️ 48.7K · <a href="https://t.me/MatinSenPaii/3779" target="_blank">📅 22:13 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3777">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/OCXD9VeVc22VfyIN-5EB1qhmPqicUAXqQeAvWGh0nImfoW1lxoIjeSsSOPeSatvNU9t_lkwsy6wm4N0IBftH_TIBNKhTD2iQ9ta-8H8A71jQRb-k3ylt6hc0FkAKBdA8gF0NnmH9LTDIR6UpwjHQAN8Bw7VI_ruWB1qaOIULibNZqgplHibqTR5sJCkOdpJYdLztBubeDU0xckeUtDNf9z88oc0HhTlJ8d8pdNpTstOOYx7LqGL77axAAeFcPL5ByaEzMT1FsWODRRG7SJjg_Wd9w2hI6GFDtWhsmFQJ7tZSIRKq1B6x_wtgIWAty-3T8O0X6OH0kYEsaGM93UcEgA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/Jjkn4wtuq8Ma5k7WAXsJgemI7bSJDlhJjndoVeiX5tw9RfEoKB4iApgu_v9cdOrNe-_-tqKm12_Gtc7__emSc2G8EtMCcwM79myXgjzKP8vk206zbvA-o-RyfaThZCfEVD4RHyzscuPI9XRC73JtbkXuobyMm6HjOCAUpu0Q4-dFbUwnZiJ23tr-2VIX9YiMTVb0Pf6vDqXRlHfIdWCd2JU1V3DXD8kRrd-7Q-4ykCjGsQUzvMc07aeJ5X9151AGhBPWE4DfqQTNwKRtRUmpANxlTWj6vxA8vVLTPcUnGikjZ2KfkJlsnWe_NcaUHCeVSUpPjVFXc41LK7DA5Qb8ug.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">بچه‌های WhiteDNS دارن رو یه چیزی کار می‌کنن که شاهکاره ایده‌اش
(عاشق UI اولیه‌ی اپلیکیشنم
😂
)</div>
<div class="tg-footer">👁️ 51.3K · <a href="https://t.me/MatinSenPaii/3777" target="_blank">📅 21:32 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3776">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/m8PxafzRHWmxSNNeCNflUayrVGai-w0uTxhknPAipnIK7iv_2HvTZAe6Yc4cCPd7d9gaf05V3oT9zzc9ZJU4uD6t9Z78Ams0IvIVmHwo5rP0Flhm5apvwLfnxRfwVAAOh0qPvGO80wXK8v_23L4RVnhlZgfFIpHSLBjAPMcECnmGMcHbS_rJCfvSRsrzdYue_MFzEx2lZP5KfRiA56EyTDOTqTEyvzgO-4hGoKk_MvKMDStCB7xiLsIAV-uMt5_rUOkEXPZWRtN__Uw9YBNe12G5LVkDeCG8hpQe-f66s8oVBi15VdTmja94EMsiqc4q5v1Tl2Ra9Q3Io4lm5CeqEw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آنتروپیک هنوز جوهر Opus 4.8 خشک نشده بود، مدل جدید Fable 5 رو به عنوان قوی‌ترین مدل عمومی Claude معرفی کرد!  این مدل توی برنامه‌نویسی، تحقیق و همینطور تحلیل تصویر عالی‌ترینه؛ هرچقدر کارمون پیچیده‌تر بشه، برتریش نسبت به مدل‌های دیگه بیشتر و بیشتر مشخص می‌شه.…</div>
<div class="tg-footer">👁️ 49.1K · <a href="https://t.me/MatinSenPaii/3776" target="_blank">📅 19:58 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3775">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/79adfc024d.mp4?token=wAyyV8gBY3hICtK44Z4gTz0ZocdVD0HWE5zhZ5ApBh_5gCrb1VKD4BLl9RolRFsZohaJaXNvslcUlV3tVuQDCPrluUBDIxWLVpvLh4zw8yFvVfHQrHzVt4hNM-irmua2IZik1GIThcadvzameJ6gefytSFYznCwuuLgreS_1hSPRu9NB5IkJQVptgD8mhtexXHt-_rIS7wYH3aAD1LyTV58czMJgS_xw-RlPnm91XuIaJaSQHyyUtrzlFEra1d0EiV2W1YspJksedxVjOJeTF4stfEYdR_0S4MRDXPFR043hhIAkIdX5gBNy2PZAZdITlGEkHLlz59Ys8vuNI05fmQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/79adfc024d.mp4?token=wAyyV8gBY3hICtK44Z4gTz0ZocdVD0HWE5zhZ5ApBh_5gCrb1VKD4BLl9RolRFsZohaJaXNvslcUlV3tVuQDCPrluUBDIxWLVpvLh4zw8yFvVfHQrHzVt4hNM-irmua2IZik1GIThcadvzameJ6gefytSFYznCwuuLgreS_1hSPRu9NB5IkJQVptgD8mhtexXHt-_rIS7wYH3aAD1LyTV58czMJgS_xw-RlPnm91XuIaJaSQHyyUtrzlFEra1d0EiV2W1YspJksedxVjOJeTF4stfEYdR_0S4MRDXPFR043hhIAkIdX5gBNy2PZAZdITlGEkHLlz59Ys8vuNI05fmQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">آنتروپیک هنوز جوهر Opus 4.8 خشک نشده بود، مدل جدید Fable 5 رو به عنوان قوی‌ترین مدل عمومی Claude معرفی کرد!
این مدل توی برنامه‌نویسی، تحقیق و همینطور تحلیل تصویر عالی‌ترینه؛ هرچقدر کارمون پیچیده‌تر بشه، برتریش نسبت به مدل‌های دیگه بیشتر و بیشتر مشخص می‌شه.
همینطور به دلیل توانایی‌های بالاش، برای موضوعات حساس مثل امنیت سایبری(هک و امنیت)، زیست‌شناسی(شاید تولید سلاح‌های زیستی)، شیمی(شاید تولید مواد مخدر
😂
) و مطالب مشابه، از مدل ضعیف‌تر Opus 4.8 استفاده می‌شه.
همینطور همزمان مدل Mythos 5 هم معرفی شده که یه نسخه از Fable 5 با محدودیت‌های امنیتی کمتره.
فعلاً Mythos 5 فقط در اختیار تیم‌های امنیت سایبری خود آمریکا و زیرساخت‌های حیاتیش هست و ممکنه بعداً برای پژوهش‌های پزشکی و امنیتی به افراد مورد اعتماد بیشتری داده بشه. طبق جدول منتشر شده، Mythos 5 و Fable 5 در بنچمارک‌ها امتیاز بالاتری نسبت به GPT 5.5 و Gemini 3.1 Pro و خود Claude Opus 4.8 کسب کردن</div>
<div class="tg-footer">👁️ 50.8K · <a href="https://t.me/MatinSenPaii/3775" target="_blank">📅 18:54 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3774">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/jIOTY9YqAjLGn1SGCQ093z1XQFT6zVhrP2XuPzzkITLVZstnIVwGLQnMyQO4Pk2krYAfTUJ5Vi85AGkCZGfym-BoYxl4fZWltl1uU4oitfvg0-YNMr62HEkBMETPcjymlDMprB1RTAKpFEpv5OZmPcu0iLqtOAPBIpEF54rhHUR0ytxhq0siRtv9SYe4-LWYKTCaTkDphlx6WLXwS5ILeayMjPxkr-bxJa8X88B2NDPcBz6gWwYN-CuOqUMRv-hPk2NKcSJDexnWkuywRQEUegLKBN_tqKhDQvCC1nsXdL-48WKe-h3-OiFC_HlleHwNUdz9b-YygSVUGcpFYWwj_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">من خودم با Hiddify راحتترم برای ساب، از اون استفاده میکنم کلا(با نت H+ الان دارم این پست رو می‌ذارم با همین ساب) اگر پینگ نداد، توی تنظیمات Tls Fragment رو روشن کنید</div>
<div class="tg-footer">👁️ 49.9K · <a href="https://t.me/MatinSenPaii/3774" target="_blank">📅 16:09 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3773">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/aqPIcfS037Gnmj4-gm42qmirqQkeIUnyWJu9BuSHWO2bA88y4KFb-TW3cuQlf17t4C4ONH8ocekkIjFF7yz2Jnbxz60RyKs3C-KmYzCML6hzQf84y_DoFoMr0ub0jiNSBxqAdQeeZv_ec-NBloTdhFF6Or_7WTyAFKqgQJV-SvUeJ-fW1eLYFykEdwow9FySf1_hmcA3j4ztvlgvD8HaTcMAqDcxTcxqZKYDJaQavk4owOR0yusygnBSbDQ32lCK_PQuXtHCW1qPDmr0hjkM_Dj59KbLjDkDNf5C1Rc1d65ZKvIT1WYfZvEREZ91yG8yty7zRnfprI9cLyMjFsfMgg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این ساب‌ها رو می‌تونید توی هر کلاینت V2rayای که دارید وارد کنید و استفاده کنید ازشون</div>
<div class="tg-footer">👁️ 51.8K · <a href="https://t.me/MatinSenPaii/3773" target="_blank">📅 14:49 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3772">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">ساب لینک مخصوص تمامی اپراتور ها نامحدود
❤️
✔️
اپدیت کنین ساب رو اگه نتونستین اضافه کنین ساب رو کافیه لینکو توی مرورگر بزنید بالا میاد و کانفیگا رو کپی کنید
⚡️
لینک ساب دائمی کانفیگ ها: https://raw.githubusercontent.com/masir-sefid/Sub/main/@Masir_Sefid.txt…</div>
<div class="tg-footer">👁️ 51.1K · <a href="https://t.me/MatinSenPaii/3772" target="_blank">📅 13:57 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3771">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromمسیر سفید🕊</strong></div>
<div class="tg-text">ساب لینک
مخصوص تمامی اپراتور ها نامحدود
❤️
✔️
اپدیت کنین ساب رو اگه نتونستین اضافه کنین ساب رو کافیه لینکو توی مرورگر بزنید بالا میاد و کانفیگا رو کپی کنید
⚡️
لینک ساب دائمی کانفیگ ها
:
https://raw.githubusercontent.com/masir-sefid/Sub/main/@Masir_Sefid.txt
⚡️
توی تمامی کلاینت ها به جز npv میتونین استفاده کنین پینگ نگیرین وصله
🟢
نحوه ی اضافه کردن ساب لینک با اپدیت خودکار
⭐️
پروکسی 1
⭐️
دونیت برای کمک به ادامه دادن این مسیر
❤️
🪐
Channel |
@Masir_Sefid
| کانال
🪐</div>
<div class="tg-footer">👁️ 50.4K · <a href="https://t.me/MatinSenPaii/3771" target="_blank">📅 13:33 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3770">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-text">⏯️
ویدیو آموزش استفاده از WhiteDNS Wizard و نصب و راه‌اندازی کامل و اتوماتیک پنل ثنایی
https://youtu.be/rxxlNXLcaqU</div>
<div class="tg-footer">👁️ 38.8K · <a href="https://t.me/MatinSenPaii/3770" target="_blank">📅 11:43 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3769">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from🛡️𝔽𝕣𝕖𝕖 𝕋𝕣𝕚𝕒𝕝 𝕂𝕖𝕪𝕤🗝️(ÐΛɌ₭ᑎΞ𐒡𐒡)</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5c2b536338.mp4?token=MwdLc5KDzFFXoIDfZyCZeP5k4ewdf1DUCrFlgYyH7kds-lOUud0wpuQiAans5ZUT0rRaXL34dwvkW8Fn59p6TvNHHSwES4MYtIxgilXQif8bEM83kfXbqvdnEgwZ4xGQHt3izpvpc9klNzkuLNaR8BcXmVUmu-CkDrEA9VT8d74e5rg9NGDm0OZ1sOqhTyaOr-3RiWDwCArA4KdlRZUs9SQZOMMNCC6UfjEYd7cjHMJLRzr3ieG29E4diO94xag6UHVLIVfsGr3nqPIajqxPiH_CcKujlT5TDj4-FIB2HQoZZLSUwhpemX6Vwp8yJ0LKQwQZlxS_NHc-2-vzGie75w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5c2b536338.mp4?token=MwdLc5KDzFFXoIDfZyCZeP5k4ewdf1DUCrFlgYyH7kds-lOUud0wpuQiAans5ZUT0rRaXL34dwvkW8Fn59p6TvNHHSwES4MYtIxgilXQif8bEM83kfXbqvdnEgwZ4xGQHt3izpvpc9klNzkuLNaR8BcXmVUmu-CkDrEA9VT8d74e5rg9NGDm0OZ1sOqhTyaOr-3RiWDwCArA4KdlRZUs9SQZOMMNCC6UfjEYd7cjHMJLRzr3ieG29E4diO94xag6UHVLIVfsGr3nqPIajqxPiH_CcKujlT5TDj4-FIB2HQoZZLSUwhpemX6Vwp8yJ0LKQwQZlxS_NHc-2-vzGie75w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">روش وارد کردن کلید avast secureline
هر کلید برای صد کاربر هستش
اگه به لوکیشن گیر داد داخل نرفت یبار کلیر کش کنید دوباره کلید رو وارد کنید یا به نت دیگه و vpn دیگه</div>
<div class="tg-footer">👁️ 50K · <a href="https://t.me/MatinSenPaii/3769" target="_blank">📅 01:20 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3768">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from🛡️𝔽𝕣𝕖𝕖 𝕋𝕣𝕚𝕒𝕝 𝕂𝕖𝕪𝕤🗝️(ÐΛɌ₭ᑎΞ𐒡𐒡)</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b056aeeb9d.mp4?token=j_6PDaAPXjsTlBhgTiceSqpxq3T9hek1OqSIzEjK_P2poqz03Dv8QxKX1NeNPj1CTkUPSAy8X6pIqKR7bGcECLWVqRWkd5BNJ2ySkIymEahuCs77hqX5XIrc9Q4U3ehFZjD9ANINxk75u_h7acDLHHaSamlynwe24cUVNXKTNo9a0kJTsVnUmWQGG2ct8VEWQbsnrHYFXB5a23dK0z9Jl2vvYBh4obAoQcTPN9KM7vG5txJo6TmQmDg5avM3qG3HuAihTX5MZV3T7fYEfB7obZ8VMJa5COppruEyOnfPbhFgCIKcEkvD3ChAC5NjA-PNTbI4MJ2kVOo3YVYEYN7aQlbqvST3iXUTndUX_U4qGJV8W0JBRDBvJL-g0A3yTeWmuLk-C1Qpp7HM7PxWau68gy8ehBkCqo56OpbR5bcemq0ibkoV3dWEscv9OgyBDb4QXKAWyRd5cbkwSflHuK0VQ9NPkyfQzlNX5h-nYQQ1BXWPV-3aNDze1xrVij-7J9rTbobF9WFsY0MMbqv_h83Q2BHL_vjCkngLzaA_3lyCoSkdXQI_PTte8Mto0w1nqT7fv3Mo3PDyDuQbofXBXuMS0myp3I-yI1BC8KsnwW2WJX1jK4VIB3k-d1XYSBzCozLTr5ZK3WUcB1sw6xKVvz-r2t1UvSppf3FhOqUcMkZajkM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b056aeeb9d.mp4?token=j_6PDaAPXjsTlBhgTiceSqpxq3T9hek1OqSIzEjK_P2poqz03Dv8QxKX1NeNPj1CTkUPSAy8X6pIqKR7bGcECLWVqRWkd5BNJ2ySkIymEahuCs77hqX5XIrc9Q4U3ehFZjD9ANINxk75u_h7acDLHHaSamlynwe24cUVNXKTNo9a0kJTsVnUmWQGG2ct8VEWQbsnrHYFXB5a23dK0z9Jl2vvYBh4obAoQcTPN9KM7vG5txJo6TmQmDg5avM3qG3HuAihTX5MZV3T7fYEfB7obZ8VMJa5COppruEyOnfPbhFgCIKcEkvD3ChAC5NjA-PNTbI4MJ2kVOo3YVYEYN7aQlbqvST3iXUTndUX_U4qGJV8W0JBRDBvJL-g0A3yTeWmuLk-C1Qpp7HM7PxWau68gy8ehBkCqo56OpbR5bcemq0ibkoV3dWEscv9OgyBDb4QXKAWyRd5cbkwSflHuK0VQ9NPkyfQzlNX5h-nYQQ1BXWPV-3aNDze1xrVij-7J9rTbobF9WFsY0MMbqv_h83Q2BHL_vjCkngLzaA_3lyCoSkdXQI_PTte8Mto0w1nqT7fv3Mo3PDyDuQbofXBXuMS0myp3I-yI1BC8KsnwW2WJX1jK4VIB3k-d1XYSBzCozLTr5ZK3WUcB1sw6xKVvz-r2t1UvSppf3FhOqUcMkZajkM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">Avast
Secureline
آموزش دریافت لایسنس‌کی یکماهه
لینک سایت
https://businesshub.avast.com/dashboard
فیک میل
https://temp-mail.org/en/
https://internxt.com/temporary-email
https://mail.tm/en/
https://temp-mail.io/en
لینک دانلود
•
Android
•
iOS
برای کانکت شدن از ی vpn کمکی حتما استفاده کنید
از پروتکل mimic و openvpn استفاده کنید
ÐΛɌ₭ᑎΞ𐒡𐒡</div>
<div class="tg-footer">👁️ 53.4K · <a href="https://t.me/MatinSenPaii/3768" target="_blank">📅 01:20 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3767">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/HPYQ-hCsxc-_pRe33OYsZPl06pE49EK1PMwLUDD5L2GyviJXeV4FH3p1w3gYgyOqV158QLfVPM-FBYoztwf5ajIRvrTW5V6RMojP6FBRsSiu7WylZRxeHBMLgawroEABP8ULWPueur3k0wn_31Ic2sYToA5GOuR3-Z0-sQZ7ep_lTqeeFA29koSAY0fh0N4-AYv5liNdKVYgTmMjnRLfXsB5KT6VP-GYsH6CUEoSFSJRoY5dZZx-iceEzyPlNQwbxwlaX-fefjWjNIllPTnRDEOUtERd8SanrVvNlWJI_hHwwfJuj421zn5HLE1-3MpcSePKEZEvmJzh1--sx9pYUg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وایب کد وایب کده. اسم دیگه روش گذاشتن قرار نیست ماهیتش رو عوض کنه
و نه خوبه نه بد. بحثش به شدت مفصله</div>
<div class="tg-footer">👁️ 55.3K · <a href="https://t.me/MatinSenPaii/3767" target="_blank">📅 22:43 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3766">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">برای WhiteDNS از
http://Netlen.com.tr
هم میتونید سرور بگیرید. فقط قبلا یه تایمی درگاه ترونش خراب بود نمیدونم درست شده یا نه
اینجا میتونید با شماره ایرانتون هم رجیستر کنید</div>
<div class="tg-footer">👁️ 58.4K · <a href="https://t.me/MatinSenPaii/3766" target="_blank">📅 17:48 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3765">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/m4kRQxKCiCBOaEgdkFKZYbxLgams7L_SEMvRYqW8f2e-NfBrTiTQ-QMxMu0cZR9vLAR1YgEhQ4djOC3T9XK_9rmPuFY9_qavE739m3tHzMVWNLhZ7A34m6Mg7yrew4AphoVioLzbiIA8qjC7p8QCD-sIE1B4hRyb9nVRgJDhgtOj2zHSwQfGwsom0g07g8UG1Xlaew5LwZ_gcBZ2aBLyc5oxLrRuoahVb1yJYUYgSGfo2N6mRBWAOiRqHZF6cP-nKCZzKQXO9I9HTcmtPZWYCHR_VpAW-S17lY6W4lyThsWzW2J0tOiEHxPNCJ_1UIFp50pHJWKZgyZ0cfarZ_Haeg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پیام بچه‌ها:
متین جان لطفا تو کانال اعلام کن که از namecheap دامنه نگیرن. من گرفتم و بعد دو روز به علت تحریمات اکانتمو بست.</div>
<div class="tg-footer">👁️ 62.9K · <a href="https://t.me/MatinSenPaii/3765" target="_blank">📅 13:34 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3764">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">اگر توی ساخت پنل bpb یا edge یا nova یا نهان ارور 1101 گرفتید، کلا از اون اکانت Log out کنید و با یه اکانت جدید شروع کنید</div>
<div class="tg-footer">👁️ 63K · <a href="https://t.me/MatinSenPaii/3764" target="_blank">📅 10:16 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3763">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">اگر توی ساخت پنل bpb یا edge یا nova یا نهان ارور 1101 گرفتید، کلا از اون اکانت Log out کنید و با یه اکانت جدید شروع کنید</div>
<div class="tg-footer">👁️ 65.8K · <a href="https://t.me/MatinSenPaii/3763" target="_blank">📅 09:42 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3762">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">دوستان اگر خواستید از سایت yotta سرور و دامنه بگیرید، می‌تونید آدرس فیک از
fakexy.com
بگیرید و استفاده کنید</div>
<div class="tg-footer">👁️ 66.3K · <a href="https://t.me/MatinSenPaii/3762" target="_blank">📅 23:53 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3761">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">Valid-08-June-MatinSenPaii.txt</div>
<div class="tg-footer">👁️ 69.1K · <a href="https://t.me/MatinSenPaii/3761" target="_blank">📅 16:19 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3760">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/67cf13d855.webm?token=vK3iujaRfCWe7JMOUy-nYDHJ9k4TkE2pW4D_kNIzRysXb9DygO0OlSPWzb9pebP7sRvk-_uVALuMyICjt5JZr2QXD7aiK-4q5AtTwybErKbvOXhMNBK8j6fDJ8Kbh_uLcxquOMWJ5LsLBoBdSoOaOZcQH5JVtFTShPoNfRW3_lTOIHnhv-vCaHYW9D5aSUJ6CX6QHXDfccL3i_hxQDPwshPGK8ZkiMdmbceMBhKklexmMC7lIJ6bGesBwli7lNM8PwbGJEdOmR9JKVA8vLw9FFw0Fksk5-eXwEdAjddT2J35y8IpCtQ0q2HOPI9F7l1ojsBtoD73AxhlzkiChtGJTg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/67cf13d855.webm?token=vK3iujaRfCWe7JMOUy-nYDHJ9k4TkE2pW4D_kNIzRysXb9DygO0OlSPWzb9pebP7sRvk-_uVALuMyICjt5JZr2QXD7aiK-4q5AtTwybErKbvOXhMNBK8j6fDJ8Kbh_uLcxquOMWJ5LsLBoBdSoOaOZcQH5JVtFTShPoNfRW3_lTOIHnhv-vCaHYW9D5aSUJ6CX6QHXDfccL3i_hxQDPwshPGK8ZkiMdmbceMBhKklexmMC7lIJ6bGesBwli7lNM8PwbGJEdOmR9JKVA8vLw9FFw0Fksk5-eXwEdAjddT2J35y8IpCtQ0q2HOPI9F7l1ojsBtoD73AxhlzkiChtGJTg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-footer">👁️ 69.6K · <a href="https://t.me/MatinSenPaii/3760" target="_blank">📅 15:56 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3759">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">Valid-08-June-MatinSenPaii.txt</div>
  <div class="tg-doc-extra">9.3 KB</div>
</div>
<a href="https://t.me/MatinSenPaii/3759" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">اینها 688 تا ریزالوری هستن که Valid بودن توی دوره‌ی قطعی برای من، از اون 5800 تا ریزالور ویدئوی WhiteDNS</div>
<div class="tg-footer">👁️ 71.1K · <a href="https://t.me/MatinSenPaii/3759" target="_blank">📅 15:49 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3758">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-poll">
<h4>📊 دوستانی که سرور دارید، دیتاسنترای ایرانتون...</h4>
<ul>
<li>✓ اصلا وصل نشده بود هنوز اینترنتش</li>
<li>✓ وصل شده بود، الان قطع شد</li>
<li>✓ وصل شده بود و هنوز وصله</li>
<li>✓ سرور ندارم، دیدن نتایج</li>
</ul>
</div>
<div class="tg-footer">👁️ 70.9K · <a href="https://t.me/MatinSenPaii/3758" target="_blank">📅 13:46 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3757">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">ترجیحا هیچ VPNای نخرید دوستان. هیچ تضمینی نیست که اگر اینترنت قطع بشه هم اونا وصل بمونن یا نه. مثل اوایل جنگ که خیلیا اسکم شدن
همون هزینه رو بذارید whitedns راه بندازید</div>
<div class="tg-footer">👁️ 81.5K · <a href="https://t.me/MatinSenPaii/3757" target="_blank">📅 12:39 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3756">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">هر پنج دقیقه میرم یه پینگ میگیرم ببینم وضعیت چیه
روانیمون کردن</div>
<div class="tg-footer">👁️ 71.3K · <a href="https://t.me/MatinSenPaii/3756" target="_blank">📅 12:17 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3755">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">اینکه هنوز اینترنت قطع نشده جای تعجب داره به خدا</div>
<div class="tg-footer">👁️ 73K · <a href="https://t.me/MatinSenPaii/3755" target="_blank">📅 12:16 · 18 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>

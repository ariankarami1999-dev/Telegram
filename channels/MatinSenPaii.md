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
<img src="https://cdn1.telesco.pe/file/u3Qs8BgjHssbfOOGleNp5TDKJ5-Ansquu_NkysCvcbd1IDdIK5PuxemG6Fe_-18UidG_ToOHnyBAyhNOvB8s-cFuELRg0p_ab3N0Ez-8bAsHFaXbVaCSN0bT663KDGJbhlczA2gAZApfWvU5o2B5s3rYZYk6PLinKtxbaDyWHv0t4fKhLVrX_fnHENC2mdOvP9drKGX4FpjfpoaL5ksBhMpMvAHYrXeRSF9gjFUfPMmnjuo2Az5gsQi-eqxEeapGjnK2gQBPYTvxY6yPGVOorMBU9Nxf0E6AyAAcW7ammXoafHRNQ2SFLDMPZUOzYJfVJS2xPDaJ2PcIr0pPMOQ22Q.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Matin SenPai</h1>
<p>@MatinSenPaii • 👥 162K عضو</p>
<a href="https://t.me/MatinSenPaii" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 درود! متین هستم و کامپیوتر رو دوست دارم! در حال یادگیری هستم و چیزهایی که یاد میگیرم رو سعی می‌کنم به شما هم یاد بدم اگر به دردتون بخوره =)•YouTube:http://www.youtube.com/@Matin_SenPai•Github:https://github.com/MatinSenPai</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-16 23:34:57</div>
<hr>

<div class="tg-post" id="msg-3733">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/eJQxmY_k642JjweXl9qAmn7acjZop1hBXjiH6Pov-n59l3i5iVeeHuSQzhyPIHcnjJaiTWxwhI_hZIN3aH8IOn-wGwcv0KVF6ByWo_6rLNUMXovFr3XOXBQGsYeck1-RvDC0v6IZwL81ZuNF9sZ_0lvbcY_29pV0k1Fo0x5wpVbbpcMvEsOO4-aFVowhWrBA55RMmz_rnw0W2c_LXUFFUiGTobCfy4z2RiMBZvYk1sclv7uo4Xp7dyUoZidBgB3sqj1CAVkKevP2CHhBhzHMuTWJrqqUyjVJC-W925Y6BfnMXHuPh945kY9cCor9pZXCY2lOWyMGyzjAGUz7s49MYQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">انگار دیسلایک اضافه کردن به توییتر</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/MatinSenPaii/3733" target="_blank">📅 20:23 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3732">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">☠️
آموزش ساده آپدیت پنل BPB به آخرین نسخه
نکته: همونطور که توی ویدئو گفتم این صرفا آموزش آپدیته و هنوز نسخه‌ی استیبل نیومده اما می‌تونید استفاده کنید از ورژن‌های Pre-release
⚡️
لینک سایت کلودفلر:
https://dash.cloudflare.com/
لینک پروژه‌ی  BPB برای دانلود فایل ورکر:
https://github.com/bia-pain-bache/BPB-Worker-Panel/releases
⭐️
توی این ویدئو بهتون یاد میدم که چه شکلی می‌تونید پنل BPB رو آپدیت کنید
⚠️
پیش‌نیازها و نکات مهم:
1️⃣
قبلش باید این شکلی یکی ساخته باشین:
https://youtu.be/_aXy8wwyRG8
✉️
تماشا در تلگرام
📹
تماشا در یوتوب
💰
دونیت</div>
<div class="tg-footer">👁️ 33.4K · <a href="https://t.me/MatinSenPaii/3732" target="_blank">📅 16:43 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3731">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-text">🔥
1500 کانفیگ جدید به ساب WhiteDNS اضافه شد
.
همون ساب های قبلی رو رفرش کنید.
⬅️
آموزش استفاده از FlClash
⬅️
آموزش استفاده از Clash Party
ممنون از همراهی شما
🤍</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/MatinSenPaii/3731" target="_blank">📅 15:44 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3730">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">⚠️
Confirmed: Metrics show a major disruption to internet connectivity in Pakistan-administered Azad Jammu and Kashmir.</div>
<div class="tg-footer">👁️ 39.3K · <a href="https://t.me/MatinSenPaii/3730" target="_blank">📅 13:10 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3729">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromHaoodi Senpai</strong></div>
<div class="tg-text">یک سری بحث و احتمال هست که یوتیوب فیلترش برداشته بشه، همون‌طور که گویا برای یک سری شده الان هم (البته مشخص نیست اختلاله یا واقعا داره رفع فیلتر میشه).
اینکه حقی که ازمون گرفتن رو بدن هنر نیست، ولی خب واقعا خوب میشه اگه این اتفاق بیفته و مردم همه بتونن دسترسی داشته باشن
♥️
همون‌طور که
قبلاً هم بارها گفتم
، ما یوتیوبر بی خانمان هم بشیم مهم نیست، مهم دسترسی درست هست و آزاد برای همه هستش.
اون یوتوبر بی‌شرفی که ناراحت میشه از آزاد شدن دسترسی هم بنظرم هرچه سریعتر آرک تمرینی نفس نکشیدن رو شروع بکنه
🫵🏻</div>
<div class="tg-footer">👁️ 39.4K · <a href="https://t.me/MatinSenPaii/3729" target="_blank">📅 12:44 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3728">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">مراقب باشید سرور ۱۲۸ مگابایت رم و بدون ipv4 و اینا نخرید دوستان
😂
اونا رو هیچ کاریشون نمی‌تونید بکنید</div>
<div class="tg-footer">👁️ 39.2K · <a href="https://t.me/MatinSenPaii/3728" target="_blank">📅 12:13 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3727">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">یکی از دوستان توییتر(ixAbolfazl)، دیشب یه سایت معرفی کردش برای پیدا کردن ارزون‌ترین سرورهای مجازی یه سریاش قیمت سالیانه‌شون کلا 2-3 دلاره. در این حد و کریپتو هم قبول میکنن مجدد یه سریا  آدرس: serverhunter.com</div>
<div class="tg-footer">👁️ 39.9K · <a href="https://t.me/MatinSenPaii/3727" target="_blank">📅 11:58 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3726">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/oa0WrOIqn7QVSjqANaGD4C1OlrkMOVANMTgdgaiGZsQoh4BBqO-zcNrRqGh4LcxI3pOC0U-IoXMXKhC45Wufg0Z23ZEZKwrATKBwRJO_dGElZiZDT8tE-pKaUryWw-qNmn-Lw7_USNWOtn8ZMSaQ_ftnfSlmhM5PgdXyZPjW2KNbOv6XzMrYRq7d22U5tilcuFRUYh7XWV7Azz7TDQpXieUGdI9WIEfe3d940vBdJwqLRkHgh-AEU7nIiAzqatag9LVYYiF3WkJhGVjggwnTnVulA8LgHCebRhQQUan0UJ8phA17_EWTnuuX8LU5INFGPg_7jFHsMTgiAWtNkoWPGw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یکی از دوستان توییتر(
ixAbolfazl
)، دیشب یه سایت معرفی کردش برای پیدا کردن ارزون‌ترین سرورهای مجازی
یه سریاش قیمت سالیانه‌شون کلا 2-3 دلاره. در این حد
و کریپتو هم قبول میکنن مجدد یه سریا
آدرس:
serverhunter.com</div>
<div class="tg-footer">👁️ 43.9K · <a href="https://t.me/MatinSenPaii/3726" target="_blank">📅 08:07 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3724">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/uwJgmGrsjw9YciJ9uzN4e9bClIPOd6zyIDpFaCq2R1_SOngGDeNC3g-HeUGVOVd5vTLDn8VemFzavtVOHX1QNar8UYTucc4zkw_mvMfsfkN9HoIxl1CKJnMmsXsfSa8Pyl4dAsxaSGgpO0Mbm7tSnUYZ6EaflNRYKXxXibiKIGUeOAXN8UT0FNRwySpi2z4Nq49tftRVX7UReAtFGlM12AnAjRo0ZMtd78d_c0x5hN6zr7Gn0o2NjSy9e-7GwbpMWZ9DuvIWTNvKNTqa-PssllN93N1s1rY00FkaXCjeYFcqhCCskBY4Vem9aPM19-6kaJSRNqAfQXlWSSGOMYzguQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/r5wKamxUWK9dZWUZG5_z2fkfUR-RcUr8HQWwmerE0NFg3xSQSFhLMS-hhKl92G7l4qO6z8E2yt9zdH1cLY9iDKJr1jQUj5CYABDkR-73QmuSIENuuuxiSExZz2qBdAczuG3WqezH1FDs3fr1ILtUaYTMfuqa5VTE50Pm6iUD42ZwTtHi_wvCEflyYz3FNpPMpvHUTpEyAQxul6Fn3r4zXDjvJW4e1fO5kwWgLI52Wx2oGeusIsCfkVVwTz0KOSnoAAbqj9en2kvy9YeKprcW60Qr9vzeWpCUo-F9Cyh_oIiOZ8xNB-rw7Mxb_Zuc0vkeR9u5zv3HgEl7InBaR0hTQA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">والا برای من هیچکدوم روی ایرانسل و همراه اول نمیان
یه سری شایعه شده بود که میخوان یوتوب رو رفع فیلتر کنن
اما خب بازیشونه دیگه. سرگرم کردن ملت</div>
<div class="tg-footer">👁️ 42.3K · <a href="https://t.me/MatinSenPaii/3724" target="_blank">📅 02:48 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3723">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/P-rAM2WB74bGNgN11y1eo4B8PZYIEaLYB1RO6yYpJ8BAsm_e66qO2YKKV5AL_6Bq1etmDtVpsQAEKLrewPUDdu3kIOaFNrdcbTHV-nVCcA6A2cDGo6jiqKdGqh8-ynPaHxgjPRE_qw5tAu-GZlafIOcKge_H1H8r13oRxivNVJhgUtZNte0DTNAb_1fiCbsw1iWNbA8AJbk7CwTC1v0LDTeT77NFmoQQWMlF0--tfztyqhEZgk2u7Ng9mNqyEPPH2tcfsVolkeBesFkVmmSdIjSc09o9KHhbLwxWev3GDR02J87YYxBKqPTHgxrP35f-5bD_yRA8XaE-j41NwGu8gA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">برای شما هم این شکلی شده بچه‌ها؟ با لایک و دیسلایک بگید
شنیدم این رو چند بار از سر شب</div>
<div class="tg-footer">👁️ 39.3K · <a href="https://t.me/MatinSenPaii/3723" target="_blank">📅 02:44 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3716">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">senpaiscanner-darwin-amd64</div>
  <div class="tg-doc-extra">31.9 MB</div>
</div>
<a href="https://t.me/MatinSenPaii/3716" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">بفرمایید تست کنید. ورژن 0.6.0</div>
<div class="tg-footer">👁️ 41.3K · <a href="https://t.me/MatinSenPaii/3716" target="_blank">📅 02:40 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3715">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/W-o1ERfEnV9M1u97tXD1oPJ8Eoq5xXpa59mi2MCPsKq-hMBceFkqeAD-9oNBiC75O9cMm3kIJ-lMF9ulbke7D-XGrxrMslwzU3rpMCR3CQp_7RRFnNqk1vFJceRreRB-p5ugpVTB9ubHgB9dTYRPto6oeI68gGnhxyQ_pVboDfPYuqOOKPhDVmmtv9HegoDWLsXr-XIk1ALK91QgpjBRy6fXOnx7cNLriFty1tja8JwTs3VxfVu53IXjvpiN23rqQruWDRXxsULDR-BMPVOsSEEMV2uLfyiY4r8diP-oTxTWs-gzAuhCyn86qaXDb2S572k2Ep_fzkd1xAnIGkCNhw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مشکل بزرگ اسکن روی اینترنت سیمکارت هم حل شد</div>
<div class="tg-footer">👁️ 39.9K · <a href="https://t.me/MatinSenPaii/3715" target="_blank">📅 01:51 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3714">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">مشکل بزرگ اسکن روی اینترنت سیمکارت هم حل شد</div>
<div class="tg-footer">👁️ 41.7K · <a href="https://t.me/MatinSenPaii/3714" target="_blank">📅 00:54 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3713">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/pCT8ofYfiYq_3X3KM7_6HNqCkL7g-B5xESdS_QOE6bd37-Rs-zb6spvUMAMyEQs0n0turChcmTXIN2Nl9QJ-jSnayY4RD9Tjy7hE1mypdiQMndxtH98-FUbxd7CN9yMH68EmbBuBsxK4ILa9PkBeRKeKIx4phxzzDLRIL212iRIzO77otSy7ch9RHySTe355IDLWsQNjvOnIag6Qqk2rIGLJuZvku6ZwEwuJdF5K0Uw-KwWSCXZHjiCFZLt7sBvLJR1uowUs27ti671r6bYX82u7bovM8EMzq1HUKrOhrk4HGM2QgEUq1ebkZE85lO8TM3CdUHfSr0kFZxGr23PEZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دوستان این رو بگم توی ورژن جدید هسته‌ی ایکس ری، حتما باید Allow Insecure رو False بذارید توی کانفیگ وگرنه ارور میده</div>
<div class="tg-footer">👁️ 41.9K · <a href="https://t.me/MatinSenPaii/3713" target="_blank">📅 00:51 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3712">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">یه کار جالبی یکی از بچه‌ها سر SenPaiScanner در آورده که واستون قرار میدم به زودی. PR های بقیه‌ی دوستان هم بررسی کردم و همه عالی بود و تأیید شد و رفت روی کد اصلی</div>
<div class="tg-footer">👁️ 41.1K · <a href="https://t.me/MatinSenPaii/3712" target="_blank">📅 00:18 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3711">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">یه کار جالبی یکی از بچه‌ها سر SenPaiScanner در آورده که واستون قرار میدم به زودی. PR های بقیه‌ی دوستان هم بررسی کردم و همه عالی بود و تأیید شد و رفت روی کد اصلی</div>
<div class="tg-footer">👁️ 41.4K · <a href="https://t.me/MatinSenPaii/3711" target="_blank">📅 00:02 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3710">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/GBkCyPkZMai0jyfvMxMVXdkkZHTsB6hSYutpA_PHkrUPQKtcBdqpGL4oY0Jv1CT8_-e3Rxi1CYs8OEKRBki_9ag2MmZm6WBBfJLvs0HW-zqFcjXA4P_e3W9SXqyv3BeUV2WN34zVuq-6kk0emSmUybZY0yXx-zlToVLGGvLoBv5oFoSfDnNGKilh7mNJFDevTWO5UyrZO-3JFqMJrQFZLYaGyhcvITR2Vigki4IIGXo3KBplYO03_Lm9dXe0nn_GoMjFP_LMFCkN-fGEIgN9D6xwBA538aUagTQIbFrbnSBifYiLPjMFWDkB_yjcN9xo5ynjiCXIQ5m5vy-owrxq9A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سرویس WhiteDNS-Wizard برای کسایی طراحی شده که سرور و دامنه خریدن، و حالا نمی‌دونن که با اینا چیکار بکنن
👍
این نرم‌افزار مولتی‌کراس پلتفرم تحت CLI اوپن سورس، از شما اطلاعات سرور و دامنه میگیره، به علاوه API-TOKEN کلودفلر، و برای شما صفر تا صد کار نصب پنل، گرفتن سرتیفیکیت و ssl و ... رو انجام میده. و این خروجی‌ها رو میده:
1- کانفیگ VLESS WS شخصی
2- کانفیگ REALITY-XHTTP شخصی
3- کانفیگ Hysteria2 شخصی
4- کانفیگ Shadowsocks شخصی
5- کانفیگ Tor vless ws
6- کانفیگ Tor Hysteria2
7- کانفیگ Tor direct
8- به زودی مستر و ... هم اضافه میشه
آموزشش رو هم داریم با آپدیت بعدی
گیتهاب:
https://github.com/iampedii/WhiteDNS-Wizard
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 44.4K · <a href="https://t.me/MatinSenPaii/3710" target="_blank">📅 22:12 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3709">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromxsfilternet(امیرپارسا گودمن)</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TZse7EYUxX38H-qV5NrAXMoUqkg5m2fcepiGHHmyYHr2UpGGbUPIBVTDO8dG002jPStOmm5KcaPzLR-qwrQpJBFIlElWK9IzCfRXvJ5dBncDEvlQ1g0jfUp7F8DLt3ijCDB7scecHjKpk7OhYiEwzK7Uri5YbHP_slEN3tTbu3aIxnSTigJ3hUy5m25qvPlMQ8K0hpAV5L0iJlYD1fFliZaYeMiQiggXmp9EhCAKwOogbAPr7iPIKHmnjS3rHqGzfz2FScqq6hKsnR4hAFfeApE2uv2XL56VYxwMo9zVtHE_KUNwoygnVAWYO7j1cmBuxIjbQnRLl_J4-4sVl7S3xg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">AzadiTunnel نسخه آیفون شیر و خورشید
👑
یک اپ iOS برای اتصال امن و پایدارتر، با تمرکز روی تجربه ساده، CDN Fronting، DNS هوشمند و تست اتصال.
📱
لینک مستقیم اپ استور:
https://apps.apple.com/ca/app/azaditunnel/id6776486891
منبع توییتر
@xsfilterrnet
👑</div>
<div class="tg-footer">👁️ 39.3K · <a href="https://t.me/MatinSenPaii/3709" target="_blank">📅 20:27 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3708">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">ورژن جدید 4.2.0 BPB رو تست کنید بچه‌ها. سازنده‌ی عزیز روی مشکل Undefined کار کرد و درستش کرد. همینطور بخش Compatibility date رو نیازی نیست دست بزنید دیگه https://github.com/bia-pain-bache/BPB-Worker-Panel/releases/tag/v4.2.0</div>
<div class="tg-footer">👁️ 44.5K · <a href="https://t.me/MatinSenPaii/3708" target="_blank">📅 18:50 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3707">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/T85PYP-27AsT5iSc0eJcDXS_GBWXQfqra1_jDwVhwWzoxBYc0ZtOKbuTWk8kXKHwuj8_6abvoP4ioKhokq4IrJgLrO1U8t2CmQL2PDbMBY3MMa8T7Lv6L-iFk-B5pBvI4oTgz2YAKWheuGjV7HlWtdM2ZJuGjqVa4V2MX6LsvV0MZox7Sl86U8XsULdto2nvaC1XgamCf0fHL5b_Tlk3YFaGB6tZlUDW-Sk5ySvekykjTRfaJAF8W-atyQmIjzE3US4kWn7QBA_K2ZrlEa0FfRyniFpnE5TxdpKrpsBQWfLiW-ws8pqtutsHHqEy1GK50dZCeZpsXp17LkE_csVsdg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏شرکت OpenAI ویژگی Dreaming رو برای حافظه ChatGPT معرفی کرد!
بالاخره بعد از مدت‌ها انتظار، OpenAI ویژگی خیلی مهمی به اسم Dreaming رو برای ChatGPT معرفی کرد. این آپدیت حافظه رو از حالت «یادآوری ساده» به یه سیستم هوشمند و پویا تبدیل کرده.
قبلاً چی بود؟
قبلاً ChatGPT چند تا نکته رو یادش می‌موند، ولی بعد از مدتی قدیمی و بی‌ربط می‌شد. مثلاً اگه بهش گفته بودی رژیم غذایی خاصی داری یا پروژه‌ای داری، بعد از چند هفته دیگه درست به یادش نمی‌اومد.
حالا با Dreaming چی شده؟
با این قابلیت ChatGPT تو پس‌زمینه (حتی وقتی باهاش حرف نمی‌زنی) همه چت‌هات رو بررسی می‌کنه، خلاصه می‌کنه، الگوها رو پیدا می‌کنه و حافظه‌ش رو همیشه تازه و به‌روز نگه می‌داره. انگار داره «رویا می‌بینه» و اطلاعات رو مرتب و هوشمندانه سازماندهی می‌کنه.
فایده‌های واقعی‌ش چیه؟
شخصی‌سازی خیلی بهتر: ترجیحاتت، علایقت، محدودیت‌هات و جزئیات زندگی‌ت رو خیلی دقیق‌تر به خاطر می‌سپاره. مثلاً اگه قبلاً گفتی عاشق عکاسی طبیعت هستی، دیگه پیشنهادهای generic نمی‌ده؛ مستقیم بهت ایده‌های مرتبط با سبک مورد علاقه‌ت می‌ده.
پروژه‌های طولانی: اگه روی یه پروژه چند ماهه کار می‌کنی (مثل نوشتن کتاب، راه‌اندازی بیزینس یا یادگیری زبان)، لازم نیست هر بار از اول توضیح بدی. ChatGPT زمینه کامل رو حفظ می‌کنه.
آپدیت خودکار: مثلاً اگه گفتی قراره به سفر بری، بعد از سفر خودش متوجه می‌شه و اطلاعات قدیمی رو پاک یا آپدیت می‌کنه.
کنترل کامل داری: می‌تونی حافظه رو ببینی، ویرایش کنی، بگی چی رو فراموش کنه یا چی رو حتماً یادش بمونه.
در کل، ChatGPT دیگه مثل یه دوست معمولی عمل می‌کنه که فقط حرفاتو گوش می‌ده (حتی این هم با ما دوست معمولیه!) حالا مثل یه دستیار واقعاً باهوش شده که تو جزئیات زندگی و کارتو درگیره و همیشه به‌روزه.
این ویژگی از امروز برای کاربران Plus و Pro در آمریکا فعال شده و به زودی برای بقیه کشورها و حتی کاربران معمولی هم می‌رسه.
لینک کامل توضیحات OpenAI:
https://openai.com/index/chatgpt-memory-dreaming/
✍️
Diego JR</div>
<div class="tg-footer">👁️ 49.3K · <a href="https://t.me/MatinSenPaii/3707" target="_blank">📅 15:37 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3706">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">ورژن جدید 4.2.0 BPB رو تست کنید بچه‌ها. سازنده‌ی عزیز روی مشکل Undefined کار کرد و درستش کرد. همینطور بخش Compatibility date رو نیازی نیست دست بزنید دیگه
https://github.com/bia-pain-bache/BPB-Worker-Panel/releases/tag/v4.2.0</div>
<div class="tg-footer">👁️ 49.8K · <a href="https://t.me/MatinSenPaii/3706" target="_blank">📅 14:16 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3705">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/UqOVGj10EWc0R_c9P9qy5ujCOlYUkfrMpVvkqCgQ6bilR5tpsfVtNy1l8YDKwRFF-4q63-gd0G9tfPM_-1xB4Tb8RmoQMShyfKNG1FD5fdKxgRw5A26YO96-ZJTDUZtkOfto1v7DFBE2wW9BUXqfprY_H10yAj8cXxDg5dJt9rn9-waXb_PX_6hebWioGFj4iGCUi8V0hFWXIYOMDEnsS7y8_sFNAutzAWgAoCrWIOrn0nd5j_KqU3D7oJpuZvYjN5vwJ2HjryG0pgSYxw0HQ89RfRcYoqA41xceLA5140fzsKxMzCCqXDtvwC40efcZzaMbExroKYnj6Ms8ZBHMLw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بچه‌ها اگر کانفیگ worker پینگ می‌ده اما درست وصل نمیشه تنظیمات مثل عکس قرار بدید fingerprint روی Firefox و Alpn روی http/1.1
یا اگر توی mahsang هستید Psiphon انتهای اتصال قرار بدید
✍️
🏴
Amin
🏴</div>
<div class="tg-footer">👁️ 51.5K · <a href="https://t.me/MatinSenPaii/3705" target="_blank">📅 11:54 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3704">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">دوستان این رو بگم توی ورژن جدید هسته‌ی ایکس ری، حتما باید Allow Insecure رو False بذارید توی کانفیگ وگرنه ارور میده</div>
<div class="tg-footer">👁️ 53.3K · <a href="https://t.me/MatinSenPaii/3704" target="_blank">📅 06:09 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3703">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/lgBoBdwMAVGE8nqDLTfe7zPIDYLx4kHtgkTqX0Wsjko2HP_Ham-3xNuxnmIzrMCX3W4ZocI-nrvq9z8qRIpgLjDemgcFMQoMmMsjw9nbMfAmQD9fkCFeq88xnxrOD6VnIGik0tki2Pk6psAyIh696z5iySdM3QGASPgO57YD2RsCoxEF2wu-X_W4Ivx9wL3fibzCakpcJhJtqOsTP4RECQUdqAMQljfu7uhJgiW6S_9UG5pZyITkGwQP3Mb7RAMzQsaOFDvNZnaMlMBAOKQvqJ-Oh1jOSaNZAslYzTqgAaFWKJnWx9m4NYTvl0N_fmR26aOatt9f3DepqBuesC31Bw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دسترسی به چند سرویس تحریمی مثل اسپاتیفای، گراک، کلاد و ... ربطی به آتش‌بس، توافق و رفع تحریم‌ها نداره و مربوط میشه به دستکاری شبکه توسط فیلترچی و عبور ترافیک از شبکه آذربایجان!</div>
<div class="tg-footer">👁️ 58.7K · <a href="https://t.me/MatinSenPaii/3703" target="_blank">📅 23:28 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3702">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/lOh5-piZXCyEetS5Mr0N45XmqhsK2RvRccEnFhZXhCl5W6QlQF1vt8ekoalZsp-XnnnSNB5aj5pBqiQxWLR-77Xm-oFmKVgJv4g8BqAj4zldHs6d3hhc6NTvxsSkNst_xkI1oOV-7jBrSGmPrjUkQq6sTLD-o2sBhSeNHXms22srND2kk7LcfmHtBDLzUYVjJ8ENKVcnJiccgTuZix7egqx6ABSW4RwOoMg5AK2ZZCrJlumZhMf8JXJhPo1yl3wJSHT2bZK4r1Ei4h4mn3fchot_Aqb0uMTmOG1QbHYQQdk4vl13t2OVjaxMjFFC5NYZg0LkqrO-epkW-X0UrgJqcg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">محدودیت کلودفلر(روزانه تقریبا ۶ گیگ) روی اکانت کلودفلر شماست. نه خود Worker
پس اگر می‌خواید این محدودیت بشه 12 گیگ، یه اتمیک میل جدید می‌سازید، یه اکانت کلودفلر جدید می‌سازید، و یه بار دیگه مراحل ساخت رو پیش میرید روی اکانت جدید</div>
<div class="tg-footer">👁️ 54.5K · <a href="https://t.me/MatinSenPaii/3702" target="_blank">📅 23:13 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3701">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-text">📌
چند نکته کاربردی برای بهتر وصل شدن با FlClash در اندروید
یکی از کاربران WhiteDNS تجربه‌ی شخصی خودش را از کار با FlClash فرستاده که برای اتصال بهتر مؤثر بوده.
اگر با FlClash مشکل اتصال، آپدیت نشدن ساب، پینگ‌های عجیب یا ناپایداری دارید، این موارد را امتحان کنید.
━━━━━━━━━━━━━━
1️⃣
بعد از نصب، قبل از اضافه کردن ساب، Resourceها را آپدیت کنید
بعد از نصب FlClash، قبل از اینکه لینک سابسکریپشن را اضافه کنید، وارد این بخش شوید:
Tools → Resource
و تمام Resourceها را آپدیت کنید.
⚠️
نکته مهم:
طبق تجربه‌ی بعضی کاربران، اگر اول لینک ساب را اضافه کنید، ممکن است بعداً Resourceها درست آپدیت نشوند یا اپ رفتار عجیب نشان بدهد.
━━━━━━━━━━━━━━
2️⃣
تنظیمات Network
از بخش Network این موارد را بررسی کنید:
✅
گزینه‌ی DNS Hijack را فعال کنید.
❌
گزینه‌ی
Allow applications to bypass VPN
را غیرفعال کنید.
این کار کمک می‌کند برنامه‌ها ترافیک یا DNS را از بیرون VPN رد نکنند.
━━━━━━━━━━━━━━
3️⃣
تنظیمات دسترسی و اجرای پس‌زمینه
بعد از نصب وارد این مسیر شوید:
Tools → Advanced Configuration → On Demand
در این بخش، گزینه‌های مربوط به دسترسی‌ها را روی Authorized قرار دهید.
همچنین در تنظیمات باتری گوشی، برای FlClash حالت Battery Optimization را غیرفعال کنید تا اندروید برنامه را در پس‌زمینه نبندد.
━━━━━━━━━━━━━━
4️⃣
گوشی روی Power Saving نباشد
اگر گوشی روی حالت
Power Saving / Battery
Saver باشد، ممکن است اتصال ناپایدار شود یا برنامه در پس‌زمینه قطع شود.
برای استفاده بهتر از FlClash، هنگام اتصال، حالت Power Saving را خاموش کنید.
━━━━━━━━━━━━━━
5️⃣
تنظیمات DNS
از بخش DNS:
✅
گزینه‌ی Override DNS را فعال کنید.
🌍
گزینه‌ی GeoIP Code را روی IR قرار دهید.
بعد از این تغییرات، لینک ساب را اضافه کنید و تست پینگ بگیرید.
━━━━━━━━━━━━━━
6️⃣
اگر ساب آپدیت نمی‌شود، حذف و دوباره اضافه کنید
طبق تجربه‌ی بعضی کاربران، FlClash گاهی نشان می‌دهد که ساب آپدیت شده، اما در عمل لیست کانفیگ‌ها تغییر نکرده است.
اگر حس کردید ساب درست آپدیت نشده:
1. لینک ساب را حذف کنید.
2. دوباره همان لینک را اضافه کنید.
3. مجدد پینگ بگیرید و تست اتصال انجام دهید.
━━━━━━━━━━━━━━
7️⃣
در تب Auto کمی صبر کنید
طبق تجربه‌ی کاربر، بعد از حذف و اضافه کردن دوباره‌ی ساب و گرفتن پینگ در تب Auto، ممکن است اول فقط چند سرور پینگ بدهند و بقیه Timeout شوند.
اما بعد از اولین اتصال، FlClash ممکن است خودش شروع کند سرورها را دوباره بررسی کند و از بالای لیست Auto دونه‌دونه سرورها را تست کند تا به گزینه‌ی بهتر برسد.
یعنی ممکن است اول یک سرور اصلاً پینگ ندهد یا در لیست بالا نباشد، اما بعد از اولین اتصال، همان سرور یا سرورهای دیگر دوباره تست شوند و وصل شوند.
⏳
گاهی این روند کمی زمان می‌برد، پس اگر همان لحظه همه‌چیز Timeout بود، چند دقیقه صبر کنید و دوباره وضعیت را بررسی کنید.
━━━━━━━━━━━━━━
8️⃣
مرتب‌سازی سرورها بر اساس پینگ
برای اینکه سرورهایی که پینگ گرفته‌اند بالای لیست بیایند، روی سه‌نقطه بزنید و وارد این مسیر شوید:
⋮ → Settings → Sort → Delay
با این کار، سرورهایی که پینگ بهتری دارند بالاتر نمایش داده می‌شوند و انتخاب سرور راحت‌تر می‌شود.
━━━━━━━━━━━━━━
✅
ترتیب پیشنهادی بعد از نصب FlClash
1. نصب FlClash
2. آپدیت Resourceها از بخش Tools → Resource
3. فعال کردن DNS Hijack
4. غیرفعال کردن Allow applications to bypass VPN
5. فعال کردن Override DNS
6. تنظیم GeoIP Code روی IR
7. غیرفعال کردن Battery Optimization برای FlClash
8. خاموش بودن Power Saving گوشی
9. اضافه کردن لینک ساب
10. رفتن به تب Auto و گرفتن پینگ
11. تنظیم Sort روی Delay
12. اتصال و چند دقیقه صبر برای تست خودکار سرورها
━━━━━━━━━━━━━━
⚠️
این تنظیمات تضمینی نیست، چون شرایط اینترنت، اپراتور و گوشی‌ها متفاوت است؛ اما برای بعضی کاربران باعث اتصال بهتر و پایدارتر شده است.
🔗
لینک ساب WhiteDNS برای FlClash:
https://sub.whitedns.one/sub/mihomo.yaml
لینک ساب برای اپ های V2Ray
https://sub.whitedns.one/sub/base64.txt
📱
یا دسترسی ساب از گیتهاب
لینک ساب برای  Clash Party & Mi Clash & FLClash
https://raw.githubusercontent.com/iampedii/whitedns-sub/refs/heads/main/mihomo.yaml
لینک ساب برای اپ های V2Ray
https://raw.githubusercontent.com/iampedii/whitedns-sub/refs/heads/main/base64.txt</div>
<div class="tg-footer">👁️ 47.6K · <a href="https://t.me/MatinSenPaii/3701" target="_blank">📅 20:31 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3700">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-text">😊
آموزش استفاده از Clash Party نسخه ویندوز در کانال یوتیوب WhiteDNS
🔥
کانال مارو Subscribe داشته باشید.
https://youtu.be/gMFH88yRghg</div>
<div class="tg-footer">👁️ 46.4K · <a href="https://t.me/MatinSenPaii/3700" target="_blank">📅 20:31 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3699">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">این هم آموزش‌های مربوطه. از لینک ساب گیتهاب استفاده کنید</div>
<div class="tg-footer">👁️ 49.2K · <a href="https://t.me/MatinSenPaii/3699" target="_blank">📅 20:31 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3698">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-poll">
<h4>📊 چرا نتونستید وصل بشید؟</h4>
<ul>
<li>✓ بلد نشدم وارد کنم</li>
<li>✓ لینک ساب رو زدم آپدیت نشد</li>
<li>✓ لینک ساب رو ژدم آپدیت هم شد، وصل نشد</li>
<li>✓ الکی دیسلایک زدم اصلا وارد نکردم</li>
</ul>
</div>
<div class="tg-text">تونستید به ساب جدید WhiteDNS وصل بشید؟</div>
<div class="tg-footer">👁️ 53.4K · <a href="https://t.me/MatinSenPaii/3698" target="_blank">📅 20:10 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3696">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">🔥
لینک ساب جدید
https://sub.iampedi2.live/sub/mihomo.yaml
📱
یا دسترسی ساب از گیتهاب
لینک ساب برای  Clash Party & Mi Clash & FLClash
https://raw.githubusercontent.com/iampedii/whitedns-sub/refs/heads/main/mihomo.yaml</div>
<div class="tg-footer">👁️ 53.3K · <a href="https://t.me/MatinSenPaii/3696" target="_blank">📅 19:58 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3695">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromxsfilternet(امیرپارسا گودمن)</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">به یاد محمد جواد حضوری.npvt</div>
  <div class="tg-doc-extra">3.4 KB</div>
</div>
<a href="https://t.me/MatinSenPaii/3695" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">💔
این کانفیگ رو به یاد محمدجواد حضوری عزیز که هم محلی من بود و دیگه پیش ما نیست میزارم تا یادش تا ابد در ذهن من و شما خواهد ماند...
به یادتیم پسر
💔
💔
💔
@xsfilterrnet
👑</div>
<div class="tg-footer">👁️ 50.6K · <a href="https://t.me/MatinSenPaii/3695" target="_blank">📅 13:38 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3694">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">😭
الان که همه‌چی فیلتر و بسته‌ست و فیلترنت داریم، یه مشکل کلاسیک ویندوز همه‌مونو کلافه کرده!</div>
<div class="tg-footer">👁️ 58K · <a href="https://t.me/MatinSenPaii/3694" target="_blank">📅 12:36 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3693">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/anBrtrRxuE8WyNP7YQwh2_uwpXm_kIp_4T-fjX6MgzLj__lPKniJhKNK0dPb_JcgFmwolhbU-4y173dSUcY1K-mudy2V89s795ENyaybu_wUiUFCEYTi0qJ8vgON9RpGDNUdP16YaXBlhPvV_JYl0rmuAj11YrRirL73fk7Ik8Jkl03FUYRgCDpmlQZoRplVAN4VtF3MGXmYWJssx0TXVbi01_nPdsjlnUNKWevKkuXCCvu9eC6odW9JxifFX-mm0Vl8aw5JZII5DnnH4HizyqwurVKzBb22W5Nkr2tq4oXP2aPCbzDT7Wl8SiCJr9PRcOUMYJVLAqY9nN9wDhy9Fg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نمیدونم چی باعث میشه یه سری دوستان ادب و نزاکت یادشون بره، ولی خب برای بقیه میگم. فکر کنم دو سه باری هم گفتم قبلا که برای مشکل سرعت آپلود متدهای پشت سی دی ان چه شخصی چه BPB و Edge:
1- فعالسازی Fragment (اون F بالای صفحه توی اپ MahsaNG با تنظیمات auto)
2- بردن کانفیگ پشت SNI-SPOOF</div>
<div class="tg-footer">👁️ 58.7K · <a href="https://t.me/MatinSenPaii/3693" target="_blank">📅 09:17 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3692">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0b2725e3a8.mp4?token=DuVecNkqdzBiwrihEHnIFF4lCGKOPug01mpeGWq-oIIvh4H-rc7oQxLuHnKki7A76OLlxEauozqeBev7dU39WsKWS_jtX3ZxsQmhTJSwqax8pDglX29e-E5XFtt51h5-ts_eT0zpQEao35XXKYTMoazkDgL9CVhfd6xlp1CXaGR3MD3H0nfMEr90_HaTCRbQ-J5f6AqenokzEu6mUb9qUsgpv8wDrEnCuFOCWdci64U_fj9SqNAU-A4r6AqHMGeel0zvRqKyv5LFvuN65WrviNXj30WS_a4k1T2MAYMpu0UOs9CcLPkzSWCCvoWpOnpLKFx-IpN14qWkMxA_wvaxRA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0b2725e3a8.mp4?token=DuVecNkqdzBiwrihEHnIFF4lCGKOPug01mpeGWq-oIIvh4H-rc7oQxLuHnKki7A76OLlxEauozqeBev7dU39WsKWS_jtX3ZxsQmhTJSwqax8pDglX29e-E5XFtt51h5-ts_eT0zpQEao35XXKYTMoazkDgL9CVhfd6xlp1CXaGR3MD3H0nfMEr90_HaTCRbQ-J5f6AqenokzEu6mUb9qUsgpv8wDrEnCuFOCWdci64U_fj9SqNAU-A4r6AqHMGeel0zvRqKyv5LFvuN65WrviNXj30WS_a4k1T2MAYMpu0UOs9CcLPkzSWCCvoWpOnpLKFx-IpN14qWkMxA_wvaxRA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">کمتر از یکساعت پیش مدل جدید تصویر ساز Reve 2.0 معرفی شد , این مدل با پیشی گرفتن از نانو بنانای دو، رتبه دوم رو در جدول مدل های تصویر ساز بعد از GPT بدست آورده
از سایت
Reve.com
‎ می‌تونید به صورت محدود و رایگان تستش کنید.
یادداشت تیم: «ما روشی نوین برای تولید و ویرایش هر نوع تصویر با استفاده از چیدمان‌های دقیق ابداع کرده‌ایم. برای نخستین بار، خلق تصاویری که گویی می‌توان آن‌ها را لمس کرد، امکان‌پذیر شده است.»
✍️
سگارو</div>
<div class="tg-footer">👁️ 59.1K · <a href="https://t.me/MatinSenPaii/3692" target="_blank">📅 05:24 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3691">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">واقعا متوجه نمیشدم چرا مردم پول vpn میدن</div>
<div class="tg-footer">👁️ 56.4K · <a href="https://t.me/MatinSenPaii/3691" target="_blank">📅 05:10 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3690">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">توی 12 دقیقه، با گوشی یا کامپیوترت بدون هیچ دانش فنی‌ای برای خودت سرور VLESS اختصاصی بساز!
🔥
توی این ویدئو، بهتون یاد دادم که چطوری از طریق وبسایت کلودفلر، پروژه BPB و پروژه BPB-ReCoder محدودیت‌های قبلی کلودفلر رو به راحتی دور بزنین و برای خودتون سابسکریپشن…</div>
<div class="tg-footer">👁️ 56.8K · <a href="https://t.me/MatinSenPaii/3690" target="_blank">📅 05:09 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3689">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">از کامپیوتر فقط دکمه خاموش روشن کردنش رو بلدی؟ نگران نباش! من بهتون یاد میدم که چطور با دانش فنی بسیار پایین، بتونید برای خودتون و خانوادتون، بدون یک ریال هزینه، VPN بسازید!
🔥
هم برای IOS، هم برای اندروید، و هم برای دسکتاپ و مک  ربع ساعت وقت بذارید این ویدئو…</div>
<div class="tg-footer">👁️ 57.2K · <a href="https://t.me/MatinSenPaii/3689" target="_blank">📅 05:08 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3688">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">یکی از دوستان این روش رو رفته بود برای مشکل اسکنر و برطرف شده بود این اشکال واسش:
متین جان برای مشکل
https://t.me/MatinSenPaii/3652
از این کد استفاده کنن دوستان
pkg install wget -y && pkg install unzip -y && wget https://uploadkon.ir/uploads/c86602_26senpaiscanner.zip && unzip c86602_26senpaiscanner.zip && cp senpaiscanner /data/data/com.termux/files/usr/bin/ && chmod +x /data/data/com.termux/files/usr/bin/senpaiscanner
بعد از اتمام کار
کافیه برای اجرا
senpaiscanner
رو بنویسن و اینتر بزنن
(توی نسخه ۵ اسکنرت)</div>
<div class="tg-footer">👁️ 58.4K · <a href="https://t.me/MatinSenPaii/3688" target="_blank">📅 23:22 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3687">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">به مناسبت ۲۰ هزارتایی شدن، یوتوب هم ۱۲۰۰ دلار از کل درآمد این چند ماهم(که موفق نشده بودم بگیرمش سر مشکل ادسنس) رو خورد و با ادسنس چینج، کلا پروند همه‌اش رو
😂
عاشق این آمریکاییام</div>
<div class="tg-footer">👁️ 54K · <a href="https://t.me/MatinSenPaii/3687" target="_blank">📅 22:52 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3686">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">به مناسبت ۲۰ هزارتایی شدن، یوتوب هم ۱۲۰۰ دلار از کل درآمد این چند ماهم(که موفق نشده بودم بگیرمش سر مشکل ادسنس) رو خورد و با ادسنس چینج، کلا پروند همه‌اش رو
😂
عاشق این آمریکاییام</div>
<div class="tg-footer">👁️ 54.6K · <a href="https://t.me/MatinSenPaii/3686" target="_blank">📅 22:47 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3685">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/u3z0LDtkBLY4cDpi_RZr3FW50eVP9z-gdJRg_-YYtoNrN-KLUFMbqf0rogvyzYDvx74MTD6PWELpvS99RELJWetP3s5zIuOX6z3fXYOBquAVI_vKf7-YjWjtP_MDjLqgVG2PFyiybO8y9Z_q5XW88hNtIlEaZF62WyDD9ilvkNNvaygLNpyw0_iyL0iUpnVwECv8sBdRSZW8olGeJYNdy3GGxSag66Hco9ZzR25KgLA60e3iUCaIWJ8HJvL9Ic_Sl_jfcBcyaPvCdlvPBDAutmUfMwUlj_TOIkOI9T82pTmaaP-fOcR0ozA-Ljq7R7IQEEfhdBquFnmQLpTuivP1Qg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عدده هیچوقت مهم نبوده و نیست. اما مناسبتیه که به خودم یادآوری کنم اهدافم رو. از 2021 که با یه گوشی و ذوق مسیرم رو عوض کردم و اومدم سراغ یوتوب، هدف والا و بلندمدت من، گذاشتن یه تأثیر مثبت روی جوونا و نوجوونای خوب وطنم بوده. کسایی که ارزشش رو دارن، عقاید و شخصیت درستی دارن، انسانیت سرمشق‌ـشونه و شرافتمندانه زندگی می‌کنن.
شاید یه جرقه‌ی امید توی این تاریکی.
شاید جلوگیری از خودکشی چندتا از برادرا و خواهرام.
شاید ایجاد شغل و ایده دادن و کمک بهشون.
توی این خراب شده، ما فقط همدیگه رو داریم.
ممنونم از تینا، پارتنر عزیزم. کسی بود که من رو از تاریکی بیرون کشید، و بهم امید زندگی داد.
پنج سال گذشت، و از مسیری که رفتم پشیمون نیستم.</div>
<div class="tg-footer">👁️ 56K · <a href="https://t.me/MatinSenPaii/3685" target="_blank">📅 22:16 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3684">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">شما یه اپلیکیشن می‌بینید، یه لینک ساب می‌بینید، من ساعت‌ها و روزها زحمت و هزاران دلار هزینه از جیب شخصی بدون چشم‌داشت و تلاش شبانه‌روزی می‌بینم. هم از بچه‌های وایت‌دی‌ان‌اس، هم از بقیه‌ی دوستامون که برای اینترنت آزاد تلاش می‌کنن
✌️</div>
<div class="tg-footer">👁️ 56.3K · <a href="https://t.me/MatinSenPaii/3684" target="_blank">📅 21:36 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3683">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-text">لینک ساب ها درست شدند
😃
🔗
لینک ساب WhiteDNS برای FlClash:
https://sub.whitedns.one/sub/mihomo.yaml
لینک ساب برای اپ های V2Ray
https://sub.whitedns.one/sub/base64.txt
📱
یا دسترسی ساب از گیتهاب
لینک ساب برای  Clash Party & Mi Clash & FLClash
https://raw.githubusercontent.com/iampedii/whitedns-sub/refs/heads/main/mihomo.yaml
لینک ساب برای اپ های V2Ray
https://raw.githubusercontent.com/iampedii/whitedns-sub/refs/heads/main/base64.txt</div>
<div class="tg-footer">👁️ 45.2K · <a href="https://t.me/MatinSenPaii/3683" target="_blank">📅 20:41 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3682">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">Matin SenPai
pinned a photo</div>
<div class="tg-footer"><a href="https://t.me/MatinSenPaii/3682" target="_blank">📅 19:39 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3681">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">الان که بهش نگاه می‌کنم، از دی‌ماه تا الان نزدیک ده سال گذشت...</div>
<div class="tg-footer">👁️ 59K · <a href="https://t.me/MatinSenPaii/3681" target="_blank">📅 15:05 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3680">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/JC4XBG4EXfBo140D914bqQCK8OF-5KCPbINoXaUhx8vcMOYokboz_4xVeyh7UsJ5WKWgiIjZX9J1yJGA2LYq4IU66UQCsVc7LFxjmRMpBOY3bM4UbO4AKzafrTI1U2Y3D6a6_NXKU70FuHxoEFA70vkuUT0tUNjMGB2m18FEyfMnRhlGfXxlEMSSVXojiLjGwLs5GKv1FIGR7Tjmnb4Fnk_xvKJBmMyeDfe8uklMPiMwbO2tKjnaz0tk0U92GGEV6v_OKDnG7M30FD1ksT2GumWkVFzEDNP0mMEMUkaytAW4Aj4lN5quJ9iMSUSvDXqIvBBx6tbTeBvUH4NBvarRUQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تمام آموزش‌های مبنی بر اینترنت آزاد که من توی کانال یوتوبم منتشر کردم به علاوه‌ی توضیحات و اینکه توی چه شرایطی به چه دردی می‌خورن. از بالا به پایین، برای شرایط سخت‌تر معرفی می‌شن تا شرایط خاموشی کامل:
1- متد Paqet، ویژه‌ی شرایط الآن(کلودفلر و اینترنت بین‌الملل باز شده) واسه‌ی هر نتی(تبدیل سرعت اینترنت داغون به سرعت خدا)
مزایا: سرعت بالا و راه‌اندازی یک باره(هم مستقیم هم تانل)
معایب: نیاز به سرور داره، روش مستقیمش فقط روی سیستم میتونه ران بشه یا گوشی Root شده و تانلش مصرف داده‌اش ۴-۵ برابره
ویدئوی اول آموزش Paqet مستقیم:
https://youtu.be/q4BbgdhPm-w
ویدئوی دوم آموزش Paqet تانل:
https://youtu.be/nwpLOANv7VY
ویدئوی سوم آموزش Paqet با نصب آسان(اسکریپت سم):
https://youtu.be/QkGI8WoOtPc
2- متدهای بر پایه کلودفلر Workers، ویژه‌ی شرایط الآن(کلودفلر و اینترنت بین‌الملل باز شده) واسه‌ی اکثر اینترنتا به علاوه‌ی آیپی تمیز
مزایا: سرعت بالا و راه‌اندازی یک باره، نامحدود بودن(هر اکانت روزانه 6 گیگابایت حدودا(هر شب ریست میشه) و می‌تونید اکانت‌های زیادی بسازید. من خودم نزدیک به ۱۰۰ تا ساختم)
معایب: فقط وب سوکت میشه ساخت و ممکنه برای گیم و... مناسب نباشه اما برای اینستاگرام و یوتوب و اینها خارق‌العادست.
سری اول کلودفلر، پنل BPB:
آموزش اول: ساخت فیلترشکن بر پایه پروژه BPB و اسکن آیپی تمیز با سیستم:
https://youtu.be/_aXy8wwyRG8
آموزش دوم: تنظیمات پنل BPB از سیر تا پیاز:
https://youtu.be/7G9Fjhe_NxM
سری دوم کلودفلر، آموزش پنل Edge:
آموزش اول، ساخت پنل Edge با سیستم به علاوه تمام تنظیماتش و ثابت کردن لوکیشن:
https://youtu.be/svYBcv4bSzo
آموزش دوم، ساخت پنل Edge فقط با یک گوشی موبایل و نصب ترموکس و اسکنر برای پیدا کردن آیپی تمیز:
https://youtu.be/2otJfXgNWCM
3- آموزش کامل خرید سرور و دامنه و نصب کاندوئیت بر روی سرور ویژه ایرانی‌های خارج از کشور که می‌خوان کمک کنن به اتصال از طریق سایفون:
https://youtu.be/DtZyWXWV4BA
4- متد SNI-SPOOFING که در صورتی که یه روزنه‌ی کوچیک باز بمونه، می‌تونید باهاش با نهایت سرعت حتی توی بدترین قطعی‌ها هم وصل بمونید.
مزایا: بدون محدودیت سرعت، می‌تونید کاملا رایگان وصل بشید(با کانفیگ‌های کلودفلر متد شماره 2)
معایب: نیاز به باز بودن اون روزنه داره، و فقط روی سیستم قابل اجراست مثل Paqet. اما قابل اشتراک‌گذاری به دیگر دستگاه‌هاست.
آموزش اول: راه‌اندازی SNI-SPOOFING و استفاده ازش روی ویندوز:
https://youtu.be/dujMBt4sCpw
آموزش دوم: رفع مشکلات و ترکیب لوکیشن متد هر کانفیگی از SNI-SPOOFING روی آمریکا:
https://youtu.be/PuYwXH4D4tU
5- متدهای بر پایه‌ی گوگل. این متدها مادامی که گوگل وصل باشن، کار می‌کنن و طیف وسیعی از متدها رو هم در بر می‌گیرن:
الف- متد MHR و زیرمجموعه‌هاش: این متد محدودیت ۲۰ هزار ریکوئست روزانه روی هر جیمیل داره و سرعت آنچنان بالایی نداره اما با تعداد ایمیل‌های بالا، میشه بهترش کرد.
آموزش اول، متد MHR خام(توصیه میشه بعدیا رو راه بندازید نه این. چون با آیپی خودتون باید برید و هوش مصنوعیا رو نمیاره واستون):
https://youtu.be/jzaqdKl40Ww
آموزش MHR-CFW(ترکیب همین، با کلودفلر برای داشتن آیپی خارج):
https://youtu.be/L3lJZrAqqUQ
آموزش راه‌اندازی MHRv-RUST با گوشی موبایل:
https://youtu.be/7YdJIJloIxY
ب- متد MITM برای دسترسی به سرویس‌های بسته شده‌ی گوگل(چون از روش یک حمله‌ی سایبری استفاده میشه روی تلگرام آپلود شده فقط):
آموزش اول دسترسی به سرویس‌های گوگل و گیتهاب:
https://t.me/MatinSenPaii/3151
آموزش دوم دانلود نامحدود از یوتوب با نت ملی بر پایه‌ی آموزش اول:
https://t.me/MatinSenPaii/3230
ج- متد Skirk بر پایه‌ی گوگل درایو که مزایاش، سرعت دانلود بالا و معایبش، Latency بالا هست؛ از کانال عزیزی:
https://youtu.be/vCr4E6Y1k4c
6- متدهای بر پایه‌ی DNS، که از روز اول جنگ وصل بودن تا آخر قطعی. اما ما اواخر قطعی بود که به بهترین ترکیبش رسیدیم. پروژه‌ی MasterDNS و کلاینت WhiteDNS. مزایا: وصل توی هر شرایطی، قابلیت اجرا روی هر پلتفرم و سیستم عاملی، حتی روی سرور، و اضطراری‌ترین راه چاره‌ی ما
معایب: مصرف حدود دو برابری اینترنت(که به نظر خودم می‌ارزه توی اون شرایط) به علت کوئری‌های DNS فراوان. همینطور نیاز به سرور داره اما از سرورهای رایگان هم می‌تونید استفاده کنید(طبیعتا سرعت خیلی پایینتر)
آموزش کامل راه‌اندازی روی گوشی و سیستم:
https://youtu.be/6Pm7kNQb3mo</div>
<div class="tg-footer">👁️ 66K · <a href="https://t.me/MatinSenPaii/3680" target="_blank">📅 14:56 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3679">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">امروز واستون دسته بندی می‌کنم یه کم راهکارهایی که تا الان دادمو</div>
<div class="tg-footer">👁️ 60.6K · <a href="https://t.me/MatinSenPaii/3679" target="_blank">📅 08:38 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3677">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/VsCx1jiT9YZJl_k-z4T9e2lT3XCwuYB4KoQUyyaXsjqM4xtitQlqeA3PhP7YWa5FlmUsPxBJqEJtA9sjWoY8m2XNVRSGyWnetaLVrdO7d23yX9jQsXU-mxk1EvWCZlBRUxyrlTJzMJnU7LUD7AOVz_965GEZWbdXyQZ2n6d678F3g280Dk_Iz8W5EaczfJIy-BEHxjLyVpxf_c3fStwEaJtMMIdlMQQUKuRr0rTqhlArilrrquqwBl6zQhVMbwIJmD28pLc7dPxNLx-QPaoCL_XUiVyoqanlnUv8F8bclrnEr_a51yWwP4uVlo4tgRWvBNr026el0gUMKh1AMqYNKA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/215e27ea42.mp4?token=mBSrfbcKwu4BnGrCyjgOwljl-peIMO9MbNA2TbXsF2YsVA1zbEU7_m_mN0dDk1TPCkWLKwVXNGazc80rGhwps13MmL233nFn04tg4ba2NtXZQ4OJ4QUNHgpmhgBZ9SoCVTuS5FDHJrFtf9HIlsj-LuhdOSkFg7Ow8jcPeRYIlSrM1HunKsF88l54evuEoe4xyDZo_eKFOvRg39cPSGyEKMVIcW4nNw9QGF_XxwoMRhO2tR9KnR14lcbYmCoyB4ySCYsZp8fZxhluWBcjXRxRLtuFI0XJXrLisAKzAwaOWz01OFkHJHvU6SU96vRR5ep8aLvoucnbYMe2HvASdr3K8w" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/215e27ea42.mp4?token=mBSrfbcKwu4BnGrCyjgOwljl-peIMO9MbNA2TbXsF2YsVA1zbEU7_m_mN0dDk1TPCkWLKwVXNGazc80rGhwps13MmL233nFn04tg4ba2NtXZQ4OJ4QUNHgpmhgBZ9SoCVTuS5FDHJrFtf9HIlsj-LuhdOSkFg7Ow8jcPeRYIlSrM1HunKsF88l54evuEoe4xyDZo_eKFOvRg39cPSGyEKMVIcW4nNw9QGF_XxwoMRhO2tR9KnR14lcbYmCoyB4ySCYsZp8fZxhluWBcjXRxRLtuFI0XJXrLisAKzAwaOWz01OFkHJHvU6SU96vRR5ep8aLvoucnbYMe2HvASdr3K8w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">Operator: Asiatech/Datacenter Time: 2026-06-02 22:22:04  The status of this service has changed to:
❌
DNS google.com via 8.8.8.8 : timeout</div>
<div class="tg-footer">👁️ 63.7K · <a href="https://t.me/MatinSenPaii/3677" target="_blank">📅 04:11 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3676">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">هیچی.
موشک زده شد؛
اونا هم گفتن دفع کردیم.
ما مردم بدبخت هم چیزای عادی‌تر دیگه‌ای از سبد خریدمون حذف میشه فردا و پس‌فردا و روز بعدش</div>
<div class="tg-footer">👁️ 62K · <a href="https://t.me/MatinSenPaii/3676" target="_blank">📅 03:56 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3675">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromSarto | سارتو</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f5a4f5e103.mp4?token=T2tzBzBat38gCkRLA1vxIGFBNTIHA5ExIvhylWpJjr7nfN21km_iFwWYvH8-4yvALq8atsf7xdvRc6EzHIYM3xMI5MGMCa8x8GjUcvI3eRSOdvo8ht72_uCVmI4V8YKo2w23KdrYz9g__XSiEww0NCHmoGgMoRCVZFgENqzdRtBBmKiR8sbD_-p97CeWta7EyhTbHxLZDXx_9dEMKNcCal13FD645PXPYvUGdqZjI3z7zOcvKRD1unYi5k8OVJhph0hh9ZcIjvChCS5MFQaJvuj3AhsX2tAHJoHbiRugkHjSYaYmqTHOjog_JqWL-p8Q-Cq7tKyptAaPq5icmjkjZal24a3e5SN1h70pCyRcvyifR-zinba33P3hQOVGbgvInJ_BahtKu65lH8nOSzcXf9qVoHaWvAywH8A2wBx5Me7mIR-FHj39GXdILszs9eQfU6QFUellcD1HbleQVXaYWE8r3RxlKDltPmpm4ZnLahEQBq2aozaJXYIqZakajQTxhOOq3CrtaYtVi8CaP8-QW8cDpwss_oNOGeVzoPd9VSkRQnekuzHVFW2VQ5EddkIOgJyuVDwZ7FZ5EYYNPcSTiC4s8xgzmI0fBlDZziZ1B1JspAL6CCkFclcG1mQc15gEHtnweCLg88a-UykXPlHnyT7VE44q82_TOn6yS5BXQXY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f5a4f5e103.mp4?token=T2tzBzBat38gCkRLA1vxIGFBNTIHA5ExIvhylWpJjr7nfN21km_iFwWYvH8-4yvALq8atsf7xdvRc6EzHIYM3xMI5MGMCa8x8GjUcvI3eRSOdvo8ht72_uCVmI4V8YKo2w23KdrYz9g__XSiEww0NCHmoGgMoRCVZFgENqzdRtBBmKiR8sbD_-p97CeWta7EyhTbHxLZDXx_9dEMKNcCal13FD645PXPYvUGdqZjI3z7zOcvKRD1unYi5k8OVJhph0hh9ZcIjvChCS5MFQaJvuj3AhsX2tAHJoHbiRugkHjSYaYmqTHOjog_JqWL-p8Q-Cq7tKyptAaPq5icmjkjZal24a3e5SN1h70pCyRcvyifR-zinba33P3hQOVGbgvInJ_BahtKu65lH8nOSzcXf9qVoHaWvAywH8A2wBx5Me7mIR-FHj39GXdILszs9eQfU6QFUellcD1HbleQVXaYWE8r3RxlKDltPmpm4ZnLahEQBq2aozaJXYIqZakajQTxhOOq3CrtaYtVi8CaP8-QW8cDpwss_oNOGeVzoPd9VSkRQnekuzHVFW2VQ5EddkIOgJyuVDwZ7FZ5EYYNPcSTiC4s8xgzmI0fBlDZziZ1B1JspAL6CCkFclcG1mQc15gEHtnweCLg88a-UykXPlHnyT7VE44q82_TOn6yS5BXQXY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎬
آموزش کامل TheFeed از صفر تا صد
اگر تازه با TheFeed آشنا شدید و نمی‌دانید از کجا باید شروع کنید، این ویدیو دقیقاً برای شماست.
👇
در این آموزش یاد می‌گیرید:
✅
اضافه کردن کانفیگ
✅
آشنایی با ریزالورها (DNS)
✅
پیدا کردن ریزالورهای سالم
✅
مشاهده کانال‌ها و دریافت محتوا
✅
آشنایی با بخش TeleMirror
✅
رفع مشکلات رایج کاربران
✅
نکات مهم برای استفاده بهتر از برنامه
دفید یک سیستم مبتنی بر DNS است که امکان دسترسی به محتوای کانال‌های تلگرام را حتی در شرایط محدودیت اینترنت فراهم می‌کند.
📢
کانال اصلی پروژه:
@networkti
📦
فایل‌های نصب:
@thefeedfile
⚙️
کانفیگ‌های عمومی:
@thefeedconfig
توضیحات متنی
👇
سلام. توی این ویدیو می‌خوام خیلی ساده و سریع نحوه کار با برنامه The Feed رو توضیح بدم.
بعد از نصب و باز کردن برنامه، اولین کاری که باید انجام بدید اضافه کردن یک کانفیگه. برای این کار از بالا روی علامت جمع بزنید و کانفیگ مورد نظرتون رو وارد کنید. کانفیگ‌های عمومی داخل کانال
@thefeedconfig
منتشر میشن و می‌تونید از اونجا دریافتشون کنید.
هر کانفیگ دارای تعدادی ریزالور پیش فرض هست که توسط سازنده کانفیگ داخل کانفیگ قرار میگیرن. بعد از اینکه کانفیگ رو اضافه کردید، برنامه شروع می‌کنه به بررسی ریزالورها. ریزالورها همون DNS هایی هستن که The Feed از طریق اون‌ها اطلاعات رو دریافت می‌کنه. این مرحله ممکنه چند دقیقه طول بکشه، پس اگر بلافاصله کانال‌ها نمایش داده نشدن نگران نباشید. بعد از پیدا شدن ریزالورهای سالم، لیست کانال‌ها دریافت میشه و می‌تونید وارد هر کانال بشید، پست‌ها رو ببینید و در صورت وجود، عکس‌ها، فایل‌ها، ویس‌ها و ویدیوها رو دانلود کنید.
اگر یه زمانی دیدید برنامه کند شده یا اطلاعات جدید دریافت نمی‌کنه، معمولاً مشکل از ریزالورهاست. برای همین داخل برنامه بخشی به اسم «پیدا کردن ریزالور» وجود داره. وارد این قسمت بشید و روی «بارگذاری لیست پیش‌فرض» بزنید. با این کار حدود ۵۸ هزار ریزالور برای اسکن آماده میشن.
اگه خودتون ریزالور خاصی دارید، می‌تونید به صورت دستی هم واردش کنید. علاوه بر این، ربات
@dns_resolvers_bot
هم می‌تونه برای پیدا کردن ریزالورهای جدید بهتون کمک کنه.
بعد دکمه «شروع اسکن» رو بزنید تا برنامه ریزالورهای سالمی که روی اینترنت شما کار می‌کنن رو پیدا کنه. وقتی چند تا ریزالور پیدا شد، می‌تونید اون‌ها رو به لیست فعال اضافه کنید. فقط یادتون باشه موقع اسکن بهتره VPN خاموش باشه تا نتیجه دقیق‌تری بگیرید.
داخل برنامه یه بخش دیگه هم به اسم Tele Mirror وجود داره. این قسمت با سیستم اصلی TheFeed فرق داره و برای نمایش کانال‌های عمومی تلگرام از سرویس‌های گوگل استفاده می‌کنه. با TeleMirror می‌تونید خیلی از کانال‌های عمومی دلخواهتون رو دنبال کنید، ولی محدودیت‌هایی هم داره؛ مثلاً امکان دانلود فایل یا پخش ویدیو توی این بخش وجود نداره. همچنین اگر سرویس‌های گوگل در دسترس نباشن، ممکنه Tele Mirror کار نکنه. البته این موضوع روی بخش اصلی TheFeed تأثیری نداره و سیستم اصلی برنامه همچنان از طریق DNS به کار خودش ادامه میده.
در نهایت اگر جایی به مشکل خوردید، اولین چیزی که باید بررسی کنید ریزالورها هستن. در اکثر مواقع با پیدا کردن چند ریزالور سالم، مشکل برنامه برطرف میشه. برای دریافت آخرین اخبار پروژه هم می‌تونید کانال
@networkti
رو دنبال کنید، فایل‌های نصب رو از
@thefeedfile
بگیرید و کانفیگ‌های عمومی رو از
@thefeedconfig
دریافت کنید.
ممنون که این ویدیو رو دیدید و امیدوارم از The Feed لذت ببرید.</div>
<div class="tg-footer">👁️ 60.3K · <a href="https://t.me/MatinSenPaii/3675" target="_blank">📅 02:05 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3674">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">من الان خودم با WhiteDNS آنلاینم(داشتم تست میکردم دامین اینها نپریده باشه)
خواهش میکنم ستاپ کنید هر چه سریعتر. هرچی نیاز دارید توی ویدیو هست
https://youtu.be/6Pm7kNQb3mo?is=Hh_zNDNmPQGHgzLb</div>
<div class="tg-footer">👁️ 59.5K · <a href="https://t.me/MatinSenPaii/3674" target="_blank">📅 01:47 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3673">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/966f6f971b.mp4?token=Uyy2ALmiJsJKSJfOkB0q5coiaNrOeD2BlPWwnUnnYWYUxhYm-tkO_HR3e2hCKz5E2UB04iEW7tXUD5pzknC1HF8rMwgjMhMmIsQpvNJuO8M2jH25dbF6mf59wEz_gvVldTTpRrKtbznpPmykS_KffVq5IMY5Y7jq-bQIHkTE9rbYqdRJQbnvot_Ut2S4JTPwuysKPl700M2LKSA6D35aIm8GaZKwWkp1N66LoSof3PbnyVIkfHR6fB46ywlSILoWvwxtQVnVxqYYk4aVihfYpXYZ04VBU2Y7-k9y1u9xws_vRUPxQkhIzSMeRW4G5iRpL4VOEJr54ZTooccQTu49Jg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/966f6f971b.mp4?token=Uyy2ALmiJsJKSJfOkB0q5coiaNrOeD2BlPWwnUnnYWYUxhYm-tkO_HR3e2hCKz5E2UB04iEW7tXUD5pzknC1HF8rMwgjMhMmIsQpvNJuO8M2jH25dbF6mf59wEz_gvVldTTpRrKtbznpPmykS_KffVq5IMY5Y7jq-bQIHkTE9rbYqdRJQbnvot_Ut2S4JTPwuysKPl700M2LKSA6D35aIm8GaZKwWkp1N66LoSof3PbnyVIkfHR6fB46ywlSILoWvwxtQVnVxqYYk4aVihfYpXYZ04VBU2Y7-k9y1u9xws_vRUPxQkhIzSMeRW4G5iRpL4VOEJr54ZTooccQTu49Jg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-footer">👁️ 63.7K · <a href="https://t.me/MatinSenPaii/3673" target="_blank">📅 01:34 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3672">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">به نظر که جنگه
چون بالستیک زدن
اگه آمریکا نگه اینا نقض آتش‌بس نیست</div>
<div class="tg-footer">👁️ 65.8K · <a href="https://t.me/MatinSenPaii/3672" target="_blank">📅 01:31 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3671">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">لطفا WhiteDNS رو ستاپ کنید هر چه سریعتر تا قطع نکردن:
https://youtu.be/6Pm7kNQb3mo?is=Hh_zNDNmPQGHgzLb</div>
<div class="tg-footer">👁️ 65.4K · <a href="https://t.me/MatinSenPaii/3671" target="_blank">📅 01:28 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3666">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">استفاده از فرگمنت هم جوابه</div>
<div class="tg-footer">👁️ 67.9K · <a href="https://t.me/MatinSenPaii/3666" target="_blank">📅 00:10 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3665">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/B2oOvhlPcPz_jDhYxIGrwsxUaiJ-Cp7qacj6SJ_Tz847IHzFVxNzeYl_5TlXhRzoNzrb5m9N9tm3itcay5F9SK5Y3LQaRqRw4sn5uVj55D_SAqTeqU_cW_XU_6623YgSxMBSDEgys95LEEcNnleJYxxl0-y0wVCX3CbQ6R9HuQMPSG5_gaGBfR7OlZ3Hsh4fKUzHhKKBh-SuwJ_f61KLlipN2sVWw4f43lYoZHrk8l_ZYFZV-TvKVlJW37iDHemqtWMMZeenWEHSd74PqIFTOZxMYv75ooLJPkvmZHIaDZ9YWQUNps3LvZOMKUUrPuqK-FbyCS1KiENH0B8pOW5A4Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">برای مشکل آپلود روی کانفیگ مستقیم پشت CDN، تنها راه استفاده از اسپوفه. sni spoof</div>
<div class="tg-footer">👁️ 67.1K · <a href="https://t.me/MatinSenPaii/3665" target="_blank">📅 00:09 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3664">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">دیدین گفتم
😂</div>
<div class="tg-footer">👁️ 68.8K · <a href="https://t.me/MatinSenPaii/3664" target="_blank">📅 22:56 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3663">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromiran internet monitor</strong></div>
<div class="tg-text">Operator: Asiatech/Datacenter
Time: 2026-06-02 22:22:04
The status of this service has changed to:
❌
DNS
google.com
via
8.8.8.8
: timeout</div>
<div class="tg-footer">👁️ 67.5K · <a href="https://t.me/MatinSenPaii/3663" target="_blank">📅 22:56 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3662">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">Operator: Asiatech/Datacenter Time: 2026-06-02 21:01:30  The status of this service has changed to:
✅
DNS google.com via 1.1.1.1 : 142.251.14.138</div>
<div class="tg-footer">👁️ 69.1K · <a href="https://t.me/MatinSenPaii/3662" target="_blank">📅 21:02 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3661">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromiran internet monitor</strong></div>
<div class="tg-text">Operator: Asiatech/Datacenter
Time: 2026-06-02 21:01:30
The status of this service has changed to:
✅
DNS
google.com
via
1.1.1.1
:
142.251.14.138</div>
<div class="tg-footer">👁️ 67.2K · <a href="https://t.me/MatinSenPaii/3661" target="_blank">📅 21:01 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3660">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/jkPQoTsU5oIW0SBrvF9AEi9HQkUKMAHQgQoJMVj6fypmx5TV41l8o6rghHDtO3PaDOctqw68Rl17NWsfNLNIAcAAD4Gk2ylZ24mUPRhcYJe-lcQYfILfQrCensFg4WOT9ZkVZ21Fapoz2b5jXbmUMczGjEhWBsSQRcR4pHmG-PuJvqf59nDmgdVzsI0XZ7dHgG1TnA-rPmGqKIGg2Ed7s9xh6ZKGFG4CzMdoJItAtZ8Ek6YSBsfV1SDSv9jw5o7YGcvvKiX89EIPlv099M1ANhFOZ1HyQUEPp42k7LIfwRldG6ilZqIawwPDy2TrGkt4fx9mzTaZb8KfTiKM9rmBPw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هرچند یک سری دیتاسنترهای خاص یه سری تانل‌ها روشون جواب میده به راحتی. از جمله Paqet و بک‌هال و  reverse</div>
<div class="tg-footer">👁️ 72.2K · <a href="https://t.me/MatinSenPaii/3660" target="_blank">📅 19:04 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3659">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/blb3dx6CzmS2tDqbm2JBt5xGHcrvQtnqcq6Tz0c64Nwm47FKm3epX3vx5UL-Lr2X_FgRNtJFRtNHyzu8rI8yAIhSR4kHRGcOFGdlSjsiRX0Dlcy0691-wfR1dqTdMp-oEp7hLKFWN9c-K9gtgi8-lfdrIF3xaKlnrlOkC15JscA_n875cS1cJVYKzCQghxBz5Gd37r3_lzXth68hIDRcNjKwUf1zNWeTDT7ey1oykCPksoecyFESMvTO0EOBaB2D2vFb3e_DSDwvrYvEf0VmMEr_ScC9u-4SUdoDwY3BNu3QYq_0-CnBKfNIDSvHUuf7G-f2G3D6GV6L5j1NwLgeUw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">☠️
ساخت نامحدود تصویر با هوش مصنوعی Nano Banana 2 گوگل + طراحی رابط کاربری(UI) و ساخت ویدئو و موسیقی
⭐️
توی این ویدئو:
1- بهتون نشون میدم که خودم Thumbnailهام رو چطوری میسازم و چه شکلی می‌تونید به صورت نامحدود از Nano Banana 2 و Pro گوگل استفاده کنید
🎤
2- یه UI باحال با هوش مصنوعی به همراه پروتوتایپ طراحی می‌کنیم
❄️
3- و با همدیگه یه موزیک در مورد 90 روز قطعی اینترنت می‌سازیم
🎧
🤎
اسپانسر ویدئو:
کانال تلگرامی ذغال سیستم؛ فروش لپ تاپ و لوازم جانبی استوک وارداتی دبی:
https://t.me/ZoghalSystem
⚠️
پیش‌نیازها و نکات مهم:
1️⃣
همه‌ی مراحل رایگانه و نیاز به پیش‌نیاز یا هزینه نداره
📹
تماشا در یوتوب</div>
<div class="tg-footer">👁️ 69.8K · <a href="https://t.me/MatinSenPaii/3659" target="_blank">📅 17:49 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3657">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">ببینید MHR و mhrv-rust و skirk و flow drive و تمامی متدهای بر پایه‌ی گوگل، با اولین بادی که از سمت سرزمین‌های دشمن بِوَزه قطع می‌شن
تنها چیزی که برای ما می‌مونه، DNS هست که همون هم ممکنه سرعتش خیلی خیلی کم باشه و می‌تونید از اینجا
https://youtu.be/6Pm7kNQb3mo
آموزشش رو ببینید.
متدهای بر پایه کلودفلر مثل BPB و Edge و... هم که یه پله بالاتر از MHR و اینها هستن و طبیعتا همیشه بعد از وصل شدن گوگل، وصل می‌شن.
هرچند به WhiteDns هم نمیشه ۱۰۰ اعتماد داشت که برامون بمونه چون توی هر سری فیلترینگ ما غافلگیر شدیم. مثلا ما به هیچ وجه فکر نمی‌کردیم بتونن جلوی Paqet رو بگیرن اما تونستن. هرچند امثال پترنیها هم با SNI Spoof، اونا رو غافلگیر کردن!
برای همین شما ترجیحا متد مستر دی ان اس رو توی Whitedns به عنوان اضطراری‌ترین راه، داشته باشید علی‌الحساب</div>
<div class="tg-footer">👁️ 67K · <a href="https://t.me/MatinSenPaii/3657" target="_blank">📅 12:13 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3656">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-footer">👁️ 60.1K · <a href="https://t.me/MatinSenPaii/3656" target="_blank">📅 11:54 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3655">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromIRCF | اینترنت آزاد برای همه</strong></div>
<div class="tg-text">گروه Void Verge در تازه‌ترین
#گزارش
خود اعلام کرده: از زمانی که اینترنت ایران دوباره توسط دولت بازگشایی شده، تغییرات گسترده‌ای در شبکه داخلی کشور درحال انجام است. پس از هفته‌ها قطعی و محدودیت، تقریباً تمام روش‌هایی که در آن دوره مورد استفاده قرار می‌گرفتند مستندسازی شده و به دست نهادهای مسئول رسیده‌اند. سیستم فیلترینگ خود را برای مرحله بعدی اختلال‌ها و قطعی‌ها آماده می‌کند و روش‌هایی مانند DNS Tunneling، MITM و Domain Fronting به احتمال زیاد در قطعی‌های آینده دیگر کارایی گذشته را نخواهند داشت.
علاوه بر این، نهادهای مسئول فیلترینگ اقدامات گسترده‌ای برای ایجاد ارائه‌دهندگان واسط انجام داده‌اند؛ سرویس‌هایی که خدمات خارجی را با محدودیت‌های شدید در اختیار کاربران ایرانی قرار می‌دهند یا وب‌سایت‌های ضروری را که امکان استفاده از روش‌های قبلی را ندارند، از طریق NAT در دسترس قرار می‌دهند. در چنین شرایطی، انتشار عمومی و علنی روش‌ها نتیجه‌ای جز آسان‌تر کردن کار نهادهای فیلترینگ ندارد. این سازوکارها باید دور از توجه، به‌صورت کلوزسورس و کم‌سروصدا فعالیت کنند.
در همین حال، مافیای اینترنت در ایران بیش از گذشته قدرت گرفته است؛ مافیایی متشکل از افرادی با دسترسی به «اینترنت سفید»، برخی ISPها و مراکز داده که از طریق سازوکارهایی مانند سرویس‌های پروکسی و سرورهای اختصاصی مجهز به NAT، اینترنت نامحدود را با قیمت‌هایی در حد صدها میلیون تومان به فروشندگان VPN عرضه می‌کنند. این مافیا آن‌قدر قدرتمند شده که توانسته بر سیاست‌گذاری‌ها نیز اثر بگذارد و حتی در شرایط بحرانی و دوران جنگی هفته‌های گذشته، به حفظ هرچه بیشتر محدودیت‌های اینترنتی کمک کند تا منافع اقتصادی خود را حفظ و افزایش دهد.
برخی شرکت‌های ساده میزبانی وب در ایران تنها طی دو ماه قطعی اینترنت، به فروشندگان بزرگ VPN با درآمدهای بسیار بالا تبدیل شده‌اند. ما در هفته‌های آینده به جمع‌آوری و انتشار اطلاعات و داده‌های لازم ادامه خواهیم داد. اگر این روند ادامه پیدا کند، هدف بعدی باید مقابله با مافیای اینترنت در ایران باشد. امیدواریم این روزهای سخت برای همه ایرانیان به پایان برسد. آسیبی که از سوی دشمنان داخلی و افرادی که زیر سایه جنگ از مردم سوءاستفاده می‌کنند به جامعه وارد می‌شود، گاهی از خود جنگ نیز دردناک‌تر است.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 59.1K · <a href="https://t.me/MatinSenPaii/3655" target="_blank">📅 11:38 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3654">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">دوستان برای هیستریا، سرورهای AWS آمازون با این سرعت جوابگو هستن چیزی که من دیدم و دوستان گفتن و متأسفانه دیتاسنتر دیگه‌ای ندیدم که به این خوبی باشه. آمازون هم گرونه به شدت
پس از آموزشش فعلا منصرف شدم</div>
<div class="tg-footer">👁️ 62.8K · <a href="https://t.me/MatinSenPaii/3654" target="_blank">📅 00:55 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3653">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">شمع Iced latte</div>
<div class="tg-footer">👁️ 65.6K · <a href="https://t.me/MatinSenPaii/3653" target="_blank">📅 23:34 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3652">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/WToUA8C7AmRfNUq27qzozCzPrcW65TSu8r5NI-Lkbu86earzwGWbXetHwzhujfDQ0DPnRES-Z1r2HY6RZDGzPSx-A5CKB5WciUjCgtMZmKrwomil8H9GRfZ2c91VpMMX76IethVjGJQxXV4WOxAy-oAxv1qJ_pH4TQEdqDVVnoFpc2OnJGmTO8K5mUk-_JzZb58xAdjUGV0pKp36oUH88uQoHqkHU2tWDfN3TLhoPWfdu45JmeNCs_YObqkdekMcK4bC65YZ-nPHvn9bVAf952Jaqdkb6kF-3I27f53eIkRB1vZOD-E0peRfMO0_7BxJJr5T0Zqi54j8DMuW0-Sahw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اگر ارور EOF و 403 گرفتید یعنی گیتهاب هنوز روی اپراتورتون مشکل داره و این یعنی اسکنر نصب نمیشه(باید با وی‌پی‌ان بزنید). طبیعتا وقتی دستور senpaiscanner رو میزنید not found میده چون اصلا چیزی نصب نشده</div>
<div class="tg-footer">👁️ 65.1K · <a href="https://t.me/MatinSenPaii/3652" target="_blank">📅 22:45 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3651">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">☠️
آموزش ساخت VPN شخصی با گوشی موبایل(کاملا رایگان) + اسکن آیپی تمیز با Termux  دوستان این متد  تا مرحله‌ی 4 اش انجام دادنش منطقیه. ما متوجه شدیم که در واقع SNI Spoofingای در کار نیست و کانفیگ داره فرگمنت میشه فقط. تا مرحله‌ی 4 پیش برید و پرسرعت به کانفیگ خودتون…</div>
<div class="tg-footer">👁️ 61.4K · <a href="https://t.me/MatinSenPaii/3651" target="_blank">📅 20:32 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3650">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/frqGSjewShQVmwXdDbPY6BQt-OzXnjmZDSPREi2q6NZx7vz6zXMniASIagwKxkVwSiGuoNp7_IHvCbJlNwVogkvKNoDRWUM7bZecBywiZVf5kOWU28GYALbMlD3rVf7_YOE0gKhr4jnH_CnTrbuc-VamFtTxJAZEIFndUTgjLVSaL38TzLW2olXn9y2kAxkHjpJK5kFICoD-6_nn3QvWGSHCo54ctyu1ptdXTunZPh78Txu10gbbcXUHNsb5S6czIEHJVqridgCmM5dpz0AKPCZiw8r8mImjMZ0JJJi0AgdH4xV_jb7WIwkInWd58T86qMm5zL5oqY9iwYvlPvFAMw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اگر به این ارور خوردید، پروژه‌ی جدید بسازید. اگر باز هم نشد، با یه اکانت دیگه وارد بشید و مجدد تست کنید. توی این ویدئو
https://youtu.be/_aXy8wwyRG8
به همین ارور خوردم و این شکلی حل شد</div>
<div class="tg-footer">👁️ 65.1K · <a href="https://t.me/MatinSenPaii/3650" target="_blank">📅 19:08 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3649">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">☠️
آموزش ساخت VPN شخصی با گوشی موبایل(کاملا رایگان) + اسکن آیپی تمیز با Termux  دوستان این متد  تا مرحله‌ی 4 اش انجام دادنش منطقیه. ما متوجه شدیم که در واقع SNI Spoofingای در کار نیست و کانفیگ داره فرگمنت میشه فقط. تا مرحله‌ی 4 پیش برید و پرسرعت به کانفیگ خودتون…</div>
<div class="tg-footer">👁️ 57.8K · <a href="https://t.me/MatinSenPaii/3649" target="_blank">📅 19:02 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3648">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">دوستان این متد  تا مرحله‌ی 4 اش انجام دادنش منطقیه. ما متوجه شدیم که در واقع SNI Spoofingای در کار نیست و کانفیگ داره فرگمنت میشه فقط. تا مرحله‌ی 4 پیش برید و پرسرعت به کانفیگ خودتون متصل بشید</div>
<div class="tg-footer">👁️ 60.4K · <a href="https://t.me/MatinSenPaii/3648" target="_blank">📅 18:09 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3646">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/p7-eWsUztwTuDEkVsxPR52QQ00yczJvXIpTYP2CYAC2kSIxq_ciWMQMdG6OdDvlBgzQyDPwias2r0zDSz8TADHwX4Xq9W0snkYJQCloykj0V3hPXfLInMNlpCBOeSgkXvn7uwRvg3QLihVViRZS0JSuGIILRIyERTQliXe2_4M_oxaLXEkJ0G0MrHpSJfizQsDxNao45WYTv-rhXW_9KCppXfTNg9ABC6FSxoJ5OhpelmtQViXDP4mcKFkmwU_Ne6ClNuVn5zJz6evIbQJ9kOKiNsraoPW83R5DIQpRk_scIFQsbNqv8cTaifG633IHuOd0h53j73xHiIBFsETRc3Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/dFH1u2XWk-N_4Pb3F16KoHtjPe43GYKThQMs1GWJE5Ew7G0oC-OZhby96ifMoicpT3p5mgrmb-0OLtQEhBVjD3tJ88WNCSPkMaBXolqN9qVd2jLk9A4FmyIf0amUZtG9pbjGKm7LlMaJG44VSI6QYSZKnLn7aacdRS0yFMfsggDmFVBVYLAG_mav4joENgvdrIVq6dAvYYYJ2YhF05pbA4-Jd-08MEVxjvTWf4z7Mb4HcsP3sfLbiBlCbr8hIt_VEXfW3k4X03utdoGR5Jjq99XeyY0Rza4M56eFTxMg0OH72gBEhLv3zed_W9-5vQLxqLg28L2O54ZEk15NoIyEwA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">☠️
آموزش ساخت VPN شخصی با گوشی موبایل(کاملا رایگان) + اسکن آیپی تمیز با Termux  دوستان این متد  تا مرحله‌ی 4 اش انجام دادنش منطقیه. ما متوجه شدیم که در واقع SNI Spoofingای در کار نیست و کانفیگ داره فرگمنت میشه فقط. تا مرحله‌ی 4 پیش برید و پرسرعت به کانفیگ خودتون…</div>
<div class="tg-footer">👁️ 62K · <a href="https://t.me/MatinSenPaii/3646" target="_blank">📅 17:47 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3645">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromMatin SenPai(᯽マティ️️ン先輩)</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">V4-Spoof-Configs-MatinSenPaii.txt</div>
  <div class="tg-doc-extra">6.2 KB</div>
</div>
<a href="https://t.me/MatinSenPaii/3645" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">لیست جدید 33 تایی از کانفیگ‌های Spoof که همه‌شون کار می‌کنن و خودم تستشون کردم</div>
<div class="tg-footer">👁️ 36.2K · <a href="https://t.me/MatinSenPaii/3645" target="_blank">📅 17:35 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3644">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">base.apk</div>
  <div class="tg-doc-extra">11.4 MB</div>
</div>
<a href="https://t.me/MatinSenPaii/3644" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">اپلیکیشن RSTA(که به زودی اوپن سورسش رو هم میسازن عزیزان)</div>
<div class="tg-footer">👁️ 59.1K · <a href="https://t.me/MatinSenPaii/3644" target="_blank">📅 17:33 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3643">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">SenPaiScanner-on-Phone.txt</div>
  <div class="tg-doc-extra">350 B</div>
</div>
<a href="https://t.me/MatinSenPaii/3643" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">دستورات اسکنر برای Termux</div>
<div class="tg-footer">👁️ 62.9K · <a href="https://t.me/MatinSenPaii/3643" target="_blank">📅 17:33 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3642">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">☠️
آموزش ساخت VPN شخصی با گوشی موبایل(کاملا رایگان) + اسکن آیپی تمیز با Termux
دوستان این متد  تا مرحله‌ی 4 اش انجام دادنش منطقیه. ما متوجه شدیم که در واقع SNI Spoofingای در کار نیست و کانفیگ داره فرگمنت میشه فقط. تا مرحله‌ی 4 پیش برید و پرسرعت به کانفیگ خودتون متصل بشید
⚡️
لینک سایت کلودفلر:
https://dash.cloudflare.com/
لینک پروژه‌ی  Edge برای ساخت کانفیگ رایگان:
https://github.com/cmliu/edgetunnel
فایل دستورات ترموکس:
https://t.me/MatinSenPaii/3643
پروژه رسول:
https://github.com/seramo/v2ray-config-modifier
نرم‌افزار RSTA Spoof هم اینجا:
https://t.me/rstasnispoof/2/1076
و
https://t.me/MatinSenPaii/3644
⭐️
توی این ویدئو این مراحل رو پیش میریم:
1- ساخت کانفیگ Edge(روزانه 6 گیگ رایگان با کلودفلر)
2- نصب و استفاده از Termux برای نصب اسکنر من و پیدا کردن آیپی تمیز
3- استفاده از اسکنر SenPai Scanner برای اسکن آیپی تمیز کلودفلر با استفاده از کانفیگ‌های Edge
4- استفاده از پروژه رسول برای انداختن آیپی تمیز به تعداد بالا پشت کانفیگ
5- استفاده از آیپی‌های تمیز توی Json  اسپوف و اتصال پرسرعت به اینترنت آزاد
⚠️
پیش‌نیازها و نکات مهم:
1️⃣
این متد نیاز به هیچ سرور و دانش شبکه‌ای نداره
✉️
تماشا در تلگرام
📹
تماشا در یوتوب
(با کیفیت بالاتر)
💰
دونیت</div>
<div class="tg-footer">👁️ 71.3K · <a href="https://t.me/MatinSenPaii/3642" target="_blank">📅 17:32 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3641">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/GjP3RVS1O4z1yIyU139JPhHlQbzmVMHz35Bx5fAvJ3knFwRPbQXrwpq7JS2o4U4Di-YhfcuYm5-FDjvurDuzTwMsY59yiyCsEV7h5PMcS0glGpvl7nr_J_7c89q-cKu8_tOu-joWgwAekL1f-uCTAkPAWj9MlRZjJRMair3n6XlPzGB_9EvUQcHmKmlcN3SFjmX6UE_uS74jPl9dh6nC5dUxsnFDHYSzSYcKJGH0HazZXh0sTsrnLfQV3yNv6TwJ5zG23xeFAAkf4fOoA0ad4MbqfGtuNdkQHAKIVWDGl4MhGD_zggrsmKtBoyqMQ8xi4MpZP5FqYv1-gNctMVhskg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این ربات از
یـ‌ بـ‌ خـ
عزیز واقعا باحاله. یه نگاه بهش بندازید:
@iNewsSummaryBot</div>
<div class="tg-footer">👁️ 56.7K · <a href="https://t.me/MatinSenPaii/3641" target="_blank">📅 16:41 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3640">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">تصمیم گرفتم یه آموزش صفر تا صد ضبط کنم برای عزیزای دلی که لپ تاپ ندارن و فقط یه گوشی اندرویدی دارن
از آموزش ساخت کانفیگ اسپوف گرفته(رایگان)
تا اجرای اسکنر روی ترموکس(سردرد)
و استفاده از اپلیکیشن اسپوفی که این دوستانمون ساختن
یه مقدار طولانی میشه اما دوست ندارم واقعا که بچه‌های اندروید کارشون لنگ بمونه</div>
<div class="tg-footer">👁️ 58.2K · <a href="https://t.me/MatinSenPaii/3640" target="_blank">📅 15:31 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3637">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/o1RANmJJbTQBgbVK5KcLu85Hs-goACmYvXM5VegfW3ucFrzWYpLs5UP_MGgrvwBwCUDrYfGLnyj0aXN-mSZQAFYwXzIXYSktUjYDmz5i__3eTyPTAEnL5Ox3kpsPceAzCu_iDjgXk7ejgGXHgdZm-kzeQOLPCqou5CgSvZNkOz2CwWZcb3seP3lI5s1V7pkhxrWGZJDHoF4MN5vUtAfpbQc7v5W4Egmyyr7BcxWMr7k6PXrt63mN29p79gF-rOiRAU2XPT_DneFf9yBhqXbLaMI57fOGUC4Ztoa4BfE6A3MbJRF4LNkDASbr5gwg632einuAcOoY-PsCvRTjqnC6ig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/o_vgu8Q2mnoxXq8grpnedKKqs1IUE7OdW9aKmgno0mIbdg9U4Hwokygzl5dXKT4Ztmr65AwG72ujfEnMtJRGw_VApdFuFa3YwyI0MGATjRvZMx2Xsc4Xm2VjgOrLRRxj3m_e4LtAIQMY4uNwId6Lh8L3f_DnBWGOSaueGIEnD7XP-evsEho-iFz2X92SayQl1IZFlRNOHSOSCaRcafyLqPxILnrcY643IXwKR6Gp1x-PjuFZVaMKxp09JHLDBdWoE3byl-BY-l7FWPJQ-aLDtNghsgxzsd6wdMpeiKxvIsJzA_hsAOFjmPJqVZ05CrmKng6hQ1v0PBI77yrCZwMYXw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">امروز راجب اینکه چه شکلی می‌تونید کانفیگ اسپوف شخصی بسازید و روی گوشی چه شکلی برای Config-Json می‌تونید اسکن کنید با ترکیب اسکنر من و پروژه‌ی Shin، ویدئو داریم</div>
<div class="tg-footer">👁️ 58.2K · <a href="https://t.me/MatinSenPaii/3637" target="_blank">📅 15:08 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3636">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-text">📱
اگر لینک ساب WhiteDNS رو میخواید از گیتهاب داشته باشید، این ریپو هر ۴۰ دقیقه با بهترین سرور ها آپدیت میشه
https://github.com/iampedii/whitedns-sub
لینک ساب برای Clash Party & FLClash
https://raw.githubusercontent.com/iampedii/whitedns-sub/refs/heads/main/mihomo.yaml
لینک ساب برای اپ های V2Ray
https://raw.githubusercontent.com/iampedii/whitedns-sub/refs/heads/main/base64.txt
@WhiteDNS</div>
<div class="tg-footer">👁️ 48.9K · <a href="https://t.me/MatinSenPaii/3636" target="_blank">📅 13:59 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3635">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">امروز راجب اینکه چه شکلی می‌تونید کانفیگ اسپوف شخصی بسازید و روی گوشی چه شکلی برای Config-Json می‌تونید اسکن کنید با ترکیب اسکنر من و پروژه‌ی Shin، ویدئو داریم</div>
<div class="tg-footer">👁️ 52.4K · <a href="https://t.me/MatinSenPaii/3635" target="_blank">📅 13:40 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3634">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a2a4acd74d.mp4?token=IE7Zou9n86QwvtvbMLgjJ9vdeFJUuEYFXN9pYVnpEqNPs_VoQvpe5u98PRd9VMZZCvwhTlETEcZu9XkhM-748giqvCShnjlwxEH4irTvaflsmex2tBLsxA62zZF2NKfd8duAxb3oOwbzLmtzt27LBknnvBStAGgD16KSxOCYK5A72mYGtrNdAql3KmF-dl_nlw5-ymX9Raw-UXewS7Kpqe2_e0Rw25yHpIyqZaFfZbfxlXxQnJg-tz1yZ6ixnSr6Ac2crY40rk7BQL_LHjwZI0M654DN2K2IK_-wcF5KsiAWg_9e5Am0CuM7yIczdAS-UmjT6W4hiCzrHJQkGCWeCjt7ka1Ku36YsFTTcNwg23g-GbuLwSAuA3AEkc47dFQYuc9kFqxJGgZja-QwyYph42dz-ds9BPL5AKOwG6GgNohxnelN7-Uh6fYiGL_Mv2exHU0Z6ajCTMa2XH7_Wd-vhLa7vHi3uUCnIjCeL6v7kEs46UNKhD9closUxp__A0-Vdn_mzWsmzCMchq0WTGY8_nPoRZdJnrE1YvNJXJeUnKFIP-xekeJhPhgbXMmhmLMtZfaG7ufCB1olbmhgBsYZEJED1AzITCtdTD1X7RSdM6w7yO3z6SEXaJUt4tWdEufYcuYQord27-iPD7tMMgRjF9ZHkZpi2pOGjN8l71d7NQk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a2a4acd74d.mp4?token=IE7Zou9n86QwvtvbMLgjJ9vdeFJUuEYFXN9pYVnpEqNPs_VoQvpe5u98PRd9VMZZCvwhTlETEcZu9XkhM-748giqvCShnjlwxEH4irTvaflsmex2tBLsxA62zZF2NKfd8duAxb3oOwbzLmtzt27LBknnvBStAGgD16KSxOCYK5A72mYGtrNdAql3KmF-dl_nlw5-ymX9Raw-UXewS7Kpqe2_e0Rw25yHpIyqZaFfZbfxlXxQnJg-tz1yZ6ixnSr6Ac2crY40rk7BQL_LHjwZI0M654DN2K2IK_-wcF5KsiAWg_9e5Am0CuM7yIczdAS-UmjT6W4hiCzrHJQkGCWeCjt7ka1Ku36YsFTTcNwg23g-GbuLwSAuA3AEkc47dFQYuc9kFqxJGgZja-QwyYph42dz-ds9BPL5AKOwG6GgNohxnelN7-Uh6fYiGL_Mv2exHU0Z6ajCTMa2XH7_Wd-vhLa7vHi3uUCnIjCeL6v7kEs46UNKhD9closUxp__A0-Vdn_mzWsmzCMchq0WTGY8_nPoRZdJnrE1YvNJXJeUnKFIP-xekeJhPhgbXMmhmLMtZfaG7ufCB1olbmhgBsYZEJED1AzITCtdTD1X7RSdM6w7yO3z6SEXaJUt4tWdEufYcuYQord27-iPD7tMMgRjF9ZHkZpi2pOGjN8l71d7NQk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یکی از دوستان زحمت کشیده یه آموزش ضبط کرده واسه‌ی اسپوف روی موبایل. چک بکنید ببینید موفق می‌شید بسازید یا نه:
https://youtu.be/spTJKgafNV4</div>
<div class="tg-footer">👁️ 55.8K · <a href="https://t.me/MatinSenPaii/3634" target="_blank">📅 13:30 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3633">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/uZvzeJH13WC84LTIfCmHRzBHhEwQ7u6KQA5MbgeHptJ5QYfj1lynolM7V2ly9wQyeZzqMRBbby_h9DhxJouKcubnMdxuvbbEXF38t7lz4Fw_UxF_tyFUbbmvoaGl-Nu5od5kny5knoOKu0fIiTnFj90wu-0LRXXHqp6ycJ-BE-aYk247DgxAU1kBJ7ACuLEkQDsNVCnqx0vdr5Qc3SVX8xvmbJ-g_cduCV9wc3Y3aLDkt48SD6FV76DFDNHnLekobb7eQZpw2WeeKzwzmuGoRXBhwzchFxnwd7aI7xpOYfmd3y_od0iYlKeq-ud3bLGSMVaZFhhkr6WFLoJkM-2tZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سلام خدمت همگی  از این به بعد می‌توانید از سابسکریپشن WhiteDNS در اپلیکیشن‌های زیر استفاده کنید:  اندروید: FlClash آیفون: Clash Mi  با استفاده از این اپلیکیشن‌ها دیگر نیازی نیست تعداد زیادی کانفیگ را به‌صورت دستی وارد کنید.  ما در سرورهای WhiteDNS بخشی از…</div>
<div class="tg-footer">👁️ 51.4K · <a href="https://t.me/MatinSenPaii/3633" target="_blank">📅 13:08 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3632">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/H0x5CLD1tYC6kbw3O3ZpRxaN6XzLPPzGnR8k40nXePcdgAvhFunuCn61WCCvbJi6lqulzpQfHqTtN0G63H_hVn3Mc6Kntd1k2mkfKLgW-QdV0JCW6Z7O7oAxu7s2hCMsqgFfS4U-z1-iWhkl2-Oce-PqDxOw-8nek-ukptF5fRrReN4jk3pODKBfVaMpX-5Dm_7XIEd2nYThIY5pHzKhwKJzfHbo3vBZa55XZAWccaTMbEJiAjhoDnxZ-Al8bcmjwUE5RFpGQTVQUfy8Ej3N-s2hxsP2OxskPI_w_PU8Bc58AyK9uQ4UrXQCdeuUB-nL80aPU-arFGSybo3uEO0zyQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سلام خدمت همگی
از این به بعد می‌توانید از سابسکریپشن WhiteDNS در اپلیکیشن‌های زیر استفاده کنید:
اندروید: FlClash
آیفون: Clash Mi
با استفاده از این اپلیکیشن‌ها دیگر نیازی نیست تعداد زیادی کانفیگ را به‌صورت دستی وارد کنید.
ما در سرورهای WhiteDNS بخشی از کانفیگ‌ها را بررسی و فیلتر می‌کنیم. سپس اپلیکیشن موبایل به‌صورت خودکار از بین کانفیگ‌های باقی‌مانده، بهترین گزینه‌ها را انتخاب کرده و به آن‌ها متصل می‌شود.
لینک WhiteDNS Sub برای استفاده در این اپلیکیشن‌ها:
https://sub.whitedns.one/sub/mihomo.yaml
لیست سابسکریپشن ما هر ۱ ساعت یک‌بار به‌روزرسانی می‌شود.
دانلود FLClan برای اندروید، مک، لینوکس و ویندوز
https://flclash.cc/en/download
با تشکر
تیم WhiteDNS</div>
<div class="tg-footer">👁️ 47.4K · <a href="https://t.me/MatinSenPaii/3632" target="_blank">📅 12:58 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3631">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">MITM-DomainFronting.json</div>
<div class="tg-footer">👁️ 59.7K · <a href="https://t.me/MatinSenPaii/3631" target="_blank">📅 01:31 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3630">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ku3RLtlJfuZTVZB2fMQYlcttzpeSoj_Cnp7uvCWUQwSBY0IDw0LPB-oUbDRAlmBRYu_HslDGDXRDe-STNCQvAiWjR-4JkGqcf8pOyWMRIBE-qDhKxRD78cldYNLX4zn8VpOE2JmJutd6ZaRmaCU2EaGT0y1g7x7JNRZyGypzAGDgW8R8cAra__45IIEnd8eWk8m9xfG1NS3aJ8bwgagVRD4pPdcsjdE_sVPLPBEQeYC7Z2FzRPRTUpDmAeXeUPrD48uA0yk83Sa1fajG9TtbXhYiNoPCRRyKN1XBuhHCxOFRjpcgd1_0ldnB5B3NODu1rVGLdYJdgkeiI3PARhVsMg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خب رفقا آموزش شکست خورد چیزی که می‌خواستم بهتون یاد بدم فعلا بسته هست و پولم حروم شد
😂
خوبه ساعتیه باز میشه خاموش کرد سعی میکنم اگر راه خوبی پیدا شد مجدد یاد بدم اینم بگم که paqet و gfk کار کردن روش که خب قبلا آموزشش رو دادم(ویدئو سوم و چهارم چنل) به راحتی…</div>
<div class="tg-footer">👁️ 63.5K · <a href="https://t.me/MatinSenPaii/3630" target="_blank">📅 01:15 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3629">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">دو ساعت درگیر این بودم که چرا x-ui بالا نمیاد روی آروان، می‌خواستم یه آموزشی ضبط کنم واستون بعد دیدم ipv4 سرور با چیزی که سنایی به عنوان ipv4 شناسایی میکنه کلا متفاوته و من سعی داشتم آیپی‌ای که وجود نداشت رو باز کنم:| هیچ ایده‌ای ندارم که چرا این بلا رو آورده…</div>
<div class="tg-footer">👁️ 61.8K · <a href="https://t.me/MatinSenPaii/3629" target="_blank">📅 01:02 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3627">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/eVvMw2A9EBQvkoGIWWVbeF-TVcKN8SYnoXOWBNHSQJRTURcwiUHTSYWvan2tO_gy29CFBjGc3MNwXvg1hzXnGehKimdzaz4meYfdq-YfOcKic6mKNoCUkdZrOQtHe_rgvAZ8PhaOK_2GECIcuUsGgKiHPRgtadbgKVWxd25JdH53tccdvtqSdhuiYAh8Xgo066ilBG-DLWbo9U2poOaq8NQG2ysf5KJDkhgPWZzWoRR1nZ4Isu8rTdJBGMjX6u4NIXuS-6xSXV9LZYfgmYeGLenD6k1unuANVK9vvDCk5diacVhmA2J1Yivzogp_X8o5BjZcVi6Ki10zrfHevjw0FA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/Kc-6Jk7sXWF8CJ5aZ4tTGKfdbHksxuei7FTFuouKYjuQO96u-yDvMS_yaeW2hw1IA5SpgA-P8Ex_tFXJ-ffRR_a2v5dpX-Ht8edcbU5WK-uUSOWpQ9Nyq6NN_o5hKUNjjn7s2CVKePF0Aa4tHYZzxWBcJH267e4E0MAEH0clDcboHyjZbFrEOpoTcURugPCZZFLdH_iDwtbLjWGhHCTcQwCiIeR7oxpPfM3GYf3Vc1bilI_l4_QBwuG1KLnpduQdbq4T9pHMCZat_NE-toWQOoAjN17e3Hfde7oDzwJIWbWcvWpA6VdURF6-izUdHLuiyMjgkDwI9m28leGF_JdQFg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">دو ساعت درگیر این بودم که چرا x-ui بالا نمیاد روی آروان، می‌خواستم یه آموزشی ضبط کنم واستون
بعد دیدم ipv4 سرور با چیزی که سنایی به عنوان ipv4 شناسایی میکنه کلا متفاوته و من سعی داشتم آیپی‌ای که وجود نداشت رو باز کنم:| هیچ ایده‌ای ندارم که چرا این بلا رو آورده آروان سر سرورا اولین بار بود با همچین چیزی مواجه شدم.
و اینکه با سرور فروغش من تونستم به گیتهاب و اینا ریکوئست بزنم نت بین‌الملل داره. نمیدونم از کی وصل شده</div>
<div class="tg-footer">👁️ 67.2K · <a href="https://t.me/MatinSenPaii/3627" target="_blank">📅 23:01 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3626">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/k934LpcVqLbgqeF4HsKG9yawvlK3GHYEqP12eiACjSZVnCUuqyczpCsqy7TiYUw3p119_FkB11x7Uw675TC-DCa4xwnSYWQdhinNh-Pg4IVopqnUqEYBq8BxS5UWMp4zH6-K-h7ezoeg-qZaDN5PCbQrjQHvl-nzfFuqpYjo0BQiNb5A-iWKB8i0_OXIPe7zbViJvsbjZp2-y8Yemwqms9EbtTakY5AKO0j7k8-aTFRdi7-espLLWooc12_uD7Fd-JpjTnDKFRQLZWzwDCBY3bCcSY9jm8Wsx61_jBjbAswdyiZjGD3KB9nGWH6PUl422E5FeOYZoHq4uvzLDyBt7w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پرسرعت‌ترین کانکشنی که میشه از یه سرور خارج داشت، Paqet مستقیم روی سرور ترکیه سه دلاری Yotta
😂
با paqctl
سم ران کردم روی سرور
با آموزش اولیه‌ام
هم روی ویندوز ران کردم</div>
<div class="tg-footer">👁️ 66.3K · <a href="https://t.me/MatinSenPaii/3626" target="_blank">📅 19:31 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3625">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">ShadowShare منبعی برای پیدا کردن سرورهای رایگان ss   vmess   trojan و...  وبسایت https://shadowsharing.com اندروید https://play.google.com/store/apps/details?id=com.v2cross.shadowshare ایفون https://apps.apple.com/cn/app/shadowshare/id1612647259
📍
آموزش استفاده…</div>
<div class="tg-footer">👁️ 64.9K · <a href="https://t.me/MatinSenPaii/3625" target="_blank">📅 17:58 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3621">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromShadowProxy66</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jordEuZZgKEawyWkscVUo1B-aF116h403z3X901t8NhKGBQsIRgBdStIyegluBnGqsMy2wlUvtqh4LO9-OBXBaH9ylvqRoZ35Z-a1H5Nod_3XH6d_W2iNRQF3HjX8hq4x6jKYrLqmtv01GasSBjQARDG7GVv2uGxZYHr9SqTm5THqUHd3XpTIf6SwtJpT3HvysUAC5s8TSgsGcrdORJKdqbCfe9jKIZWVhaw4d9KG7tGKf2pcdqQlx5B_pqwEmBSo7hupKmCpHQoOi7qbINwMIgqVwFBh50lC0d8vHVVAjIAtXXtmKw00T5q9ea54W2iUIlPqa3TmGU4fICdgY_QZg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/PLybirygb7q7gSx7OJXsYxDo_Pi4eJhmkyxdl8cUxMA7XCKKF7Z7zEZfmGjjhyzAp6TGHqnmirmZcctBHWQWmREzEfzfMH-VtDzk2EkR9AkQOBXGATKqfaz2NBbyEejtCnkhsd4evYnOo-ycRyc2algKbNKptrSZSzVWc0dOH07jgzW3tWxggHnNKdCiD9qXDRsD1t2r9_a74bXT_MuugXQqhjW9Ew3wtfa24TCPPrugCsqKkA5xgdW9Dfkvf9NcIRf1R4MbS-M4IFBfsemwhTZ-2AeZyTU56Vlz24FPGp0BwLGvZcQ6JU-X3GRMP3F1uCovqZVtt6PMNjCmKvsZ9g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/O8gPdjwfH8eK7S9kw0s0Qxz3sUGAbc7xDM7LHhO4g0HDa4LwRqpuA48k5HbO1Mm9bacvcCniRug4-Uv4yDw6oUacdiu7dFIoIK8RdDwn9wWJJ9mvf3JXfxB6muOgFfc5BuS1cSjo4UJRy-PhzeXIfmFT0J7b4hGCfT8q7DkMQA7ng1O5DrD8IRanU9N7q4JsbO782yFHWNJl5Q3duWbJNp14LqUNDtRClN6qPvoCe6KEh0e0_8irvKYESwet60H3fWOe-zSm4nFVFZjzxFmHAIoWVc9S65bkDCr5Mix_rA6h6OssfwJ-tIUDKUUSNIcL44s6ZOU2z-gXFbdLZP8r-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/fj3pdJIpiK2dCKJtUjUUJZWCkt5q5Un2xf3zl0quCAWEtcmzGNThYeQx_RrIglFd9cGl9MUSJWaLO5FPMZoOMMOgeUB53K8gFKo58GYoar_FELH-mUK1oJtH-Grn8AMd2Su7UG7Dfwh51arW1FIPbpaZDbg-4iyuH-kImBFl9k8bNDs2Db0onfcHw3ET3RxycpA6J4tnpVfyQq-a_t-hlLhkgrwSl-0AJGOQtAagaC7uT8uxQj2e2pNadOKJi7mVOpfHPLrHrzHyFB1uLTT2i7LYE-UbxWpIRb5xm3GVCASnIIjVgmd9A85Rg32tfO-QJZnoClzgKg_T6z8VGjTPqQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">ShadowShare
منبعی برای پیدا کردن سرورهای رایگان ss   vmess   trojan و...
وبسایت
https://shadowsharing.com
اندروید
https://play.google.com/store/apps/details?id=com.v2cross.shadowshare
ایفون
https://apps.apple.com/cn/app/shadowshare/id1612647259
📍
آموزش استفاده
(توجه داشته باشید کلاینت یا فیلترشکن نیست)
🌐
@ShadowProxy66</div>
<div class="tg-footer">👁️ 59.1K · <a href="https://t.me/MatinSenPaii/3621" target="_blank">📅 16:24 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3620">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/swvSrtI-I-fcrl9DVk69QexZZxePaFjRm1uPd1bNrefUIg5QWIvFw_6Y7YGieatfiTHqOy0QDAd0ucxDD7vfL7ZclLyz8lDKThUizeKl2a6I65zCu1AG-DPagoLmeq38HzCmemD6wgx_PGd40t5rY8BYvmQqiN8RMl7IEmRkDYNI7gbjlxxDcb4I1B67Sk3axlH8uyYzR-T_BuYYKYykq0BnILiuVuWbapUvZapwldeJLh04odqzHB-A7FdEeQJqQetDTrdqZ93PfRHx43Go3015lY_10zpelrRjmSg3v-MtL61GJYJL_n14F36YNjsPu3c5fEW42IZgbpKkAVwaQw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">☠️
آموزش استفاده از آیپی تمیز کلودفلر و اتصال رایگان به اینترنت + آپدیت ساخت پنل BPB
💦
⚡️
فایل اسکنر: https://t.me/MatinSenPaii/3598 پنل BPB روی گیتهاب: https://github.com/bia-pain-bache/BPB-Worker-Panel پروژه اسکنر روی گیتهاب: https://github.com/MatinSen…</div>
<div class="tg-footer">👁️ 66.7K · <a href="https://t.me/MatinSenPaii/3620" target="_blank">📅 12:14 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3619">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">من الان با این به Spoof وصلم:
{
"LISTEN_HOST": "0.0.0.0",
"LISTEN_PORT": 40443,
"CONNECT_IP": "104.17.89.5",
"CONNECT_PORT": 443,
"FAKE_SNI": "www.speedtest.net"
}
به جای connect ip، میتونید هر آیپی وایت کلودفلری که از اسکنر(
https://t.me/MatinSenPaii/3598
) به دست میارید رو قرار بدید</div>
<div class="tg-footer">👁️ 69.1K · <a href="https://t.me/MatinSenPaii/3619" target="_blank">📅 12:12 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3618">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">اگر می‌خواید گیم بازی کنید، می‌تونید از این کانفیگ‌های هیستریای مسیر سفید استفاده کنید: hysteria2://Masir_Sefid@18.159.104.97:443?sni=qus.masir-sefid.shop&insecure=0&allowInsecure=0&obfs=salamander&obfs-password=Masir_Sefid#%40%F0%9D%90%8C%F0%9D%90%9A%F0%…</div>
<div class="tg-footer">👁️ 65.7K · <a href="https://t.me/MatinSenPaii/3618" target="_blank">📅 10:54 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3617">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/AXFEeXHN2JGcTqluXGoeQNQ8z5987i-jL9VYfdhhHTW4PhGmi8IDvxtIKx_yC_Bs-TVszcGKvlHItgATcxZLkHxKb5R1oNgOqEwWcuPcs3uw-ufZSLauVvQ4sRanmmZ2tYzNxMu6zq6F2rRZA5Bef9ZGCKnI3YSan-dC_QaZRL9QvBh9FqBU2lBKybDzmRdR6iIV_ugJBbUtxhz2TmZ3oeqOyMZPWI2eytUJVUij21Up-akSzqWNoX5-580OToqzJzJKknuouRdduRDD3XGWzT0xcNQORfbnhNw5xQYzeC9dktYvVbap3zu5bsyA-exoDEjHqtRFF-cskSUOnPq84w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اگر می‌خواید گیم بازی کنید، می‌تونید از این کانفیگ‌های هیستریای مسیر سفید استفاده کنید:
hysteria2://Masir_Sefid@18.159.104.97:443?sni=qus.masir-sefid.shop&insecure=0&allowInsecure=0&obfs=salamander&obfs-password=Masir_Sefid#%40%F0%9D%90%8C%F0%9D%90%9A%F0%9D%90%AC%F0%9D%90%A2%F0%9D%90%AB_%F0%9D%90%92%F0%9D%90%9E%F0%9D%90%9F%F0%9D%90%A2%F0%9D%90%9D%2B%F0%9F%95%8A%E2%AD%90%EF%B8%8F
hysteria2://Masir_Sefid@18.159.104.97:444?sni=qus.masir-sefid.shop&insecure=0&allowInsecure=0&obfs=salamander&obfs-password=Masir_Sefid#%40%F0%9D%90%8C%F0%9D%90%9A%F0%9D%90%AC%F0%9D%90%A2%F0%9D%90%AB_%F0%9D%90%92%F0%9D%90%9E%F0%9D%90%9F%F0%9D%90%A2%F0%9D%90%9D%2B%F0%9F%95%8A%E2%AD%90%EF%B8%8F
hysteria2://Masir_Sefid@18.159.104.97:8880?sni=qus.masir-sefid.shop&insecure=0&allowInsecure=0&obfs=salamander&obfs-password=Masir_Sefid#%40%F0%9D%90%8C%F0%9D%90%9A%F0%9D%90%AC%F0%9D%90%A2%F0%9D%90%AB_%F0%9D%90%92%F0%9D%90%9E%F0%9D%90%9F%F0%9D%90%A2%F0%9D%90%9D%2B%F0%9F%95%8A%E2%AD%90%EF%B8%8F
hysteria2://Masir_Sefid@18.159.104.97:1040?sni=qus.masir-sefid.shop&insecure=0&allowInsecure=0&obfs=salamander&obfs-password=Masir_Sefid#%40%F0%9D%90%8C%F0%9D%90%9A%F0%9D%90%AC%F0%9D%90%A2%F0%9D%90%AB_%F0%9D%90%92%F0%9D%90%9E%F0%9D%90%9F%F0%9D%90%A2%F0%9D%90%9D%2B%F0%9F%95%8A%E2%AD%90%EF%B8%8F
hysteria2://Masir_Sefid@18.159.104.97:4040?sni=qus.masir-sefid.shop&insecure=0&allowInsecure=0&obfs=salamander&obfs-password=Masir_Sefid#%40%F0%9D%90%8C%F0%9D%90%9A%F0%9D%90%AC%F0%9D%90%A2%F0%9D%90%AB_%F0%9D%90%92%F0%9D%90%9E%F0%9D%90%9F%F0%9D%90%A2%F0%9D%90%9D%2B%F0%9F%95%8A%E2%AD%90%EF%B8%8F
hysteria2://Masir_Sefid@18.159.104.97:54040?sni=qus.masir-sefid.shop&insecure=0&allowInsecure=0&obfs=salamander&obfs-password=Masir_Sefid#%40%F0%9D%90%8C%F0%9D%90%9A%F0%9D%90%AC%F0%9D%90%A2%F0%9D%90%AB_%F0%9D%90%92%F0%9D%90%9E%F0%9D%90%9F%F0%9D%90%A2%F0%9D%90%9D%2B%F0%9F%95%8A%E2%AD%90%EF%B8%8F
این هم لینک سابش:
https://raw.githubusercontent.com/masir-sefid/Sub/main/@Masir_Sefid.txt
این هم کانالشون:
https://t.me/Masir_Sefid
من با همین کانفیگ‌ها توی کالاف پینگ ۶۰ و گنشین پینگ ۱۰۰ دارم و راحت می‌تونم بازی کنم.
کانفیگ هیستریا هم آموزش ساختش روی یوتوب هست، باز اگر لازم بود یه آموزش ضبط می‌‌کنم واستون. اما نیاز به سرور داره</div>
<div class="tg-footer">👁️ 72.6K · <a href="https://t.me/MatinSenPaii/3617" target="_blank">📅 10:41 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3616">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Vuj7AoU-M6CeCLVR3hh4XiwMi-B1fT0M9JNLktumfIcqOGCLKSXcs7_Z9lPqHmsRf8yb1HpDYgDQ_M9WZWbenujuput-0WgDuAE04VxGjGaGb7OhYid_oa1Ttcn4duNAeaIQtp3b5vWLbz08TgyAeBu8q0cW0LOHkILxV87KDg6rbn8t-55YOic7s7gUxH3DmAGPYHVsnTbksSZ4dTac1bE6-LUlMFQjBnByxazIWBUsYouM9kyANKXz1EVc1wVqKXUPAVCSx-jjGSe7y6MTXYQAU2muPPVOxTUfuMBEPkv1hsSNX2xCwsDNtuv58qHBfXDQGrKUc63MZfxEvBKeow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آموزش تبدیل کانفیگ به آی‌پی سفید
از این به بعد برای تبدیل کانفیگ، آی‌پی‌های خودتان استفاده می‌شود.
@WhiteDNS_Installer_bot
مراحل کار:
1. وارد ربات شوید.
2. روی گزینه «تبدیل کانفیگ با آی‌پی سفید» بزنید.
3. کانفیگ V2Ray خود را ارسال کنید.
فرمت‌های پشتیبانی‌شده:
VLESS
VMess
Trojan
بعد از تایید کانفیگ، ربات از شما لیست آی‌پی‌ها را می‌خواهد.
می‌توانید آی‌پی‌ها را به این شکل بفرستید:
8.8.8.8
104.18.1.1:8443
یا با کاما:
1.1.1.1, 8.8.8.8, 104.18.1.1:8443
نکته مهم:
اگر پورت وارد نکنید، پورت پیش‌فرض 443 استفاده می‌شود.
اگر آی‌پی را همراه پورت بفرستید، همان پورت استفاده می‌شود.
مثال:
1.1.1.1
→  پورت 443
1.1.1.1:2053
→  پورت 2053
در پایان، ربات فایل کانفیگ جدید را برای شما ارسال می‌کند که host و port آن با آی‌پی‌های ارسالی خودتان جایگزین شده است.
@WhiteDNS</div>
<div class="tg-footer">👁️ 55.8K · <a href="https://t.me/MatinSenPaii/3616" target="_blank">📅 03:28 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3615">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/syEXz-33bYZ6Nbe1uA6SolHAHRhxsniHNUyADgp20qbDcKpQhtBaVAJjB_oxtYOAwZZLp-wAcP62bCDtKDVjXQ75Wwus85sOUEwtUhBf8nmykpEDdh7gVk8ELYwby3O3UK8wBk2FlMS8GfYy-Z3ENI9PMmb-mq3MlQFVqf9x1JVyO_44njlBfqUXX_K-zh0L-d1ke7uCcWgYtDSjW_8Tj8XesdaHPDhImG67AaLEpY-Q18e8luP72nlIimTj4hpAs1WPPcUvNcWzWgg-ts9HVMiyWe5w6ZWmjE9USrTxLCkjVJ6AzF7HvPYq299NhSu6JvhFrsew-HG5HKQQKUf7kQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اگه کانفیگ کاستوم دارید(ساب نرمال)، آیپی تمیز رو باید اینجا جای address قرار بدید</div>
<div class="tg-footer">👁️ 59.6K · <a href="https://t.me/MatinSenPaii/3615" target="_blank">📅 02:21 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3614">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from𝑇𝑎ℎ𝑎</strong></div>
<div class="tg-text">https://t.me/MatinSenPaii/3613
خوبیش اینه با این روش میشه رفت و کانفیگ BPB ساخت
برا دوستانی که کلودفلر براشون بالا نمیاد یا نمیتونن وارد سایت اتومیک میل بشن
همه چیز با همین نت بدون نیاز به فیلترشکن کامل انجام میشه
بینظیرید شما
نخبه های ایران.</div>
<div class="tg-footer">👁️ 61.5K · <a href="https://t.me/MatinSenPaii/3614" target="_blank">📅 02:10 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3613">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">MITM-DomainFronting.json</div>
  <div class="tg-doc-extra">9.2 KB</div>
</div>
<a href="https://t.me/MatinSenPaii/3613" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">☠️
(اندروید و ویندوز) رفع تحریم سرویس‌های گوگل از جمله میت، جیمیل و درایو بر روی تمامی اینترنت‌ها به صورت نامحدود  این ویدئو، مقدمه‌ی اون روشیه که برای یوتوب گفتم و ویدئوی اون هم پشت این ضبط میکنم و قرار میدم خدمتتون.  لینک داخلی ویدئو: https://up.theazizi…</div>
<div class="tg-footer">👁️ 60.9K · <a href="https://t.me/MatinSenPaii/3613" target="_blank">📅 01:35 · 10 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>

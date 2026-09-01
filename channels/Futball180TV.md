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
<img src="https://cdn5.telesco.pe/file/fIG_5VExzUQQAmoxnmEfo8a0FUp6HI_KBf7L3h6-IpMBO_EynZip0hItmUlUcSmUsLtPicqcxg1ZYcgfpu42bs-Sh50OGPnrA8gY46AoCpdetsw2dtULYun7D8BQzh1CtQ022xcn3FyzP66BuaJDtkE2IyXNgo0_ahKOxh8NHJvKdTs1nT21xDnoV1hx-CxprK9T-tA_sce86jwN46MKO-uvhqoqGz87DXYGWXe5jBEP3Yxg5ZHlgr3HgjbVJG9WFnbc0B3ezCwPuiawcCkPI79c4oMRT9G8rS6PmXMrHL6Wiaw9iTgUZBJPZ_md-QKUKC7s4ASB2msdi33YhQYYfw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 فوتبال 180</h1>
<p>@Futball180TV • 👥 433K عضو</p>
<a href="https://t.me/Futball180TV" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 In the name of God; The only popular sports channel on Telegram: All for Iran...🖤We respect the copyright laws and follow the laws, Mr.@Durov...🙏🌹Contact ads:@TivaAds</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-10 09:31:03</div>
<hr>

<div class="tg-post" id="msg-105245">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/31f95056c4.mp4?token=oS6Go0P5i0hoIUEfRKkKHpHjQzpSDNGK7d0PJ87A3L4GAkFNHGitf_j1P9X50JWUyXxNn79sE8YTN72bpfu-Pu0TGKBmzozlpPQ3TbSQ2NBTddrBYQNrh5zaRwJxhPBN2gU7wWlTVMJwU8NzkgyjOJdrczrpjoINFRj0aAVHcWM_feXHZFMkp_XTG1TOoNRUVn2QRgxAPQiu6KdRXLhOhg6EU6pMCujqrLjto9TqhfULEAMC7NsmXeFB_7PBNzC2ElT9R3CxntZx5QIiKyuYj1mtP06qijebsdeL-VlCuLLk05v1TUPk4imfc3cs0UTQvS2CPY0NyLolQrNmTz1AHELEoSOBPkAd_V39a76UupUicNBuOryAlO9NDBDwsqhLhFvUJa7dr1FTvHRRC7Q8nLI8adSnDEHdrhEUOOK95Hdx9MEdqPwvgJcG-wKS-guck6E01f0C9xKYGo0S6T14jpEpPuuHyzJGA5SDi9u7EvZuEt8zh8hIW0zxggDAFSRYJQVDcIpTglXEyScslJx_5uhkuo1hrJ_Es0lMZf2TFS-ZgCL4b91U9iCR5Mz7rBNXy4gKdqZImo_qPqVLuEzdDDghmbf3_6v2-GV4f-EC5acqEBzaUKeratZ_VqNsX9Tcp1kG_NBai0NF6i89XrIiaw84RJ7Cm7in5EXfgz2jiAo" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/31f95056c4.mp4?token=oS6Go0P5i0hoIUEfRKkKHpHjQzpSDNGK7d0PJ87A3L4GAkFNHGitf_j1P9X50JWUyXxNn79sE8YTN72bpfu-Pu0TGKBmzozlpPQ3TbSQ2NBTddrBYQNrh5zaRwJxhPBN2gU7wWlTVMJwU8NzkgyjOJdrczrpjoINFRj0aAVHcWM_feXHZFMkp_XTG1TOoNRUVn2QRgxAPQiu6KdRXLhOhg6EU6pMCujqrLjto9TqhfULEAMC7NsmXeFB_7PBNzC2ElT9R3CxntZx5QIiKyuYj1mtP06qijebsdeL-VlCuLLk05v1TUPk4imfc3cs0UTQvS2CPY0NyLolQrNmTz1AHELEoSOBPkAd_V39a76UupUicNBuOryAlO9NDBDwsqhLhFvUJa7dr1FTvHRRC7Q8nLI8adSnDEHdrhEUOOK95Hdx9MEdqPwvgJcG-wKS-guck6E01f0C9xKYGo0S6T14jpEpPuuHyzJGA5SDi9u7EvZuEt8zh8hIW0zxggDAFSRYJQVDcIpTglXEyScslJx_5uhkuo1hrJ_Es0lMZf2TFS-ZgCL4b91U9iCR5Mz7rBNXy4gKdqZImo_qPqVLuEzdDDghmbf3_6v2-GV4f-EC5acqEBzaUKeratZ_VqNsX9Tcp1kG_NBai0NF6i89XrIiaw84RJ7Cm7in5EXfgz2jiAo" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
⚪️
افشاگری پشم‌ریزون عادل فردوسی‌پور از ریخت و پاش چند صد هزار یورویی مسئولان تیم‌ملی جوانان و امید در اردوی ترکیه!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 1.44K · <a href="https://t.me/Futball180TV/105245" target="_blank">📅 09:25 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105244">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7b5c71afe0.mp4?token=q6DI3gU3sOv2Y8EWPgZbCWPmEjb4wx3PBV2gf0_hbXX3NWmTk9QPT3738nB2-_5_biXZMMpF6wCQPngaE9nmJCYU8pRBjxM8OhiyOrgNttTDYMTVUGiRAI5R-Lb2j7xgCrIdVxWs4BAxAXoAOUCjxyZIHXUz5_iQZtB5a4qAReoMPbjrEjxuS8a7QR2eEPS4fOFcSFNBlxa5L0G2pOPqvFGXiQMHgHTrSSCAuE8-E55OuxDN0WGjzFzPHXWDJ_ezWVL4Rn5zyz5U-DAHvI6Y7KyvSkAktC6iDvemtpxFPSV2UCZ4gMdY0O_cvrwyv6e561z_z64MI74TWFAvSmwsKQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7b5c71afe0.mp4?token=q6DI3gU3sOv2Y8EWPgZbCWPmEjb4wx3PBV2gf0_hbXX3NWmTk9QPT3738nB2-_5_biXZMMpF6wCQPngaE9nmJCYU8pRBjxM8OhiyOrgNttTDYMTVUGiRAI5R-Lb2j7xgCrIdVxWs4BAxAXoAOUCjxyZIHXUz5_iQZtB5a4qAReoMPbjrEjxuS8a7QR2eEPS4fOFcSFNBlxa5L0G2pOPqvFGXiQMHgHTrSSCAuE8-E55OuxDN0WGjzFzPHXWDJ_ezWVL4Rn5zyz5U-DAHvI6Y7KyvSkAktC6iDvemtpxFPSV2UCZ4gMdY0O_cvrwyv6e561z_z64MI74TWFAvSmwsKQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
ویدیو خواهر پژمان‌جمشیدی از برادرش در بدو ورود به کشور کانادا پس از رفع مشکل ممنوع‌الخروج بودنش بابت پرونده اتهام به تجاوز !
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 3.78K · <a href="https://t.me/Futball180TV/105244" target="_blank">📅 09:04 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105242">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4fa9c53173.mp4?token=lxrTYq_f0ZHcBQ_jrHsFvN4an4GbpfOpmc4o2qRzqCsVmd0daY6F6J-k6gmvLtDpN8TPSj7G-d6E9EPaCdi6G6Xkta_jajy1l8fZRuwfdzi-QKNJb5-A7d5EUcO4PNfamS2wL3M2KraOa5qQKSBShvvk-9YxnrDWKSvQIEvWjV058n0is6zSTt14nNhaeCVt8DVwfNRkbyUNAKJnxojisLDM6mVFjCaW4zTtVH7d6RlGlMl_li9vlD8mhhjYnDeh1k5HQ6y4_RcNpw-3Zs2isF5p5dJu2xC4K7c4KChS46b_lw5KGgThS1eEu7AX4T_zOtcle05c1HB4kKCAFJVoag" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4fa9c53173.mp4?token=lxrTYq_f0ZHcBQ_jrHsFvN4an4GbpfOpmc4o2qRzqCsVmd0daY6F6J-k6gmvLtDpN8TPSj7G-d6E9EPaCdi6G6Xkta_jajy1l8fZRuwfdzi-QKNJb5-A7d5EUcO4PNfamS2wL3M2KraOa5qQKSBShvvk-9YxnrDWKSvQIEvWjV058n0is6zSTt14nNhaeCVt8DVwfNRkbyUNAKJnxojisLDM6mVFjCaW4zTtVH7d6RlGlMl_li9vlD8mhhjYnDeh1k5HQ6y4_RcNpw-3Zs2isF5p5dJu2xC4K7c4KChS46b_lw5KGgThS1eEu7AX4T_zOtcle05c1HB4kKCAFJVoag" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🎙
صحبت‌های عادل فردوسی‌پور در اولین برنامه فصل‌جدیدش پس از حواشی فیلتر شدن سایتش
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 6.47K · <a href="https://t.me/Futball180TV/105242" target="_blank">📅 08:01 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105241">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/Futball180TV/105241" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/Futball180TV/105241" target="_blank">📅 01:33 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105240">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HdFVJlUBRpo_vp_I-kGaf5ySDEBdkqRGpa8QrOPbIJ1qJjX53kvxOLbuk_rm1F5UXk_jrSHPsDgJzZjoqhXJWte2A3OT0aUyRu5L163DSmP-rx43OJzb3BtKNIi3rXEiRFFfcP4jDfq9lzrWyER29LyWJDC_v6I-Si1Q0J2UPzokV5GMHf9nxdVsYbsi8C0BHE_NSm-Y5BAGuZvLDvEb_XMgjUfegoIPGwgHei2JmCqcJq9atLTczl0yrok5taw-p6EsOkKyDmAQJUEKT_8T8NBO9S--GzQJ7_ad9R4O5fO452y6zcM1RYJh9mfC3RqHjqnrncs_VYGwB_H32tjgnQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تیرکس‌ بت می‌بردت وسط هیجان US Open!
🎾
🔥
🦖
رقابت‌های نفس‌گیر، امتیازهای سرنوشت‌ساز و هیجانی که تا آخرین ضربه ادامه داره!
🦖
بونوس اولین واریز تا سقف ۱۰۰ یورو
🦖
بهترین ضرایب بین تمام سایت‌ها
TREXBET — PLAY. PREDICT. WIN.
https://TrexBet.com
T.me/TrexBet_Ir</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/Futball180TV/105240" target="_blank">📅 01:33 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105239">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/Futball180TV/105239" target="_blank">📅 01:33 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105238">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/frpGRetLOPGoH9_UuwH0_sJ_qeSOZBuz82B0x9AX20oxBGBrMlPw_PMA9ROO1LFItajN8muMeclQot6-epGOWc6jqRu-F4FVenT0m6q6vrbtZyR1g0VwXNFY6Ysb3SKubKePxj_XwmhMgsJE8vg1ihZgL3GJPcdox18kEDxeaiQfhBTgr-5s9hSm4CRt54P-9fvZgl_buLQ7xcbrxuAQgO8MbXeOGb5Zzf5RGLRIGV5vEJ-rAPYV4aE2Sc5epLahLuLPE4B0K8_9gcM9HwIbrPIFx_9mOAxjmzzwPX9B6toy9HhwXEV2izzQCdligiB8a5TeV521Vs6Lji5aNCSOKA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فلیك: 91 پیروزی در 120 مسابقه با بارسا.
🥶
ژاوی: 91 پیروزی در 143 مسابقه
با بارسا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/Futball180TV/105238" target="_blank">📅 01:10 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105237">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HWl37jXyBrR6U_sNjZHdtv0w2Dc5X9H9k_5s__mZlOX3AOTmWfjH8denzAZ7QA8DDhiZDA9H5i3RO8rkg60W3cTi05J_7wAEePvn4gODUCoQDkimEFunLdjCRzUCA0bS9PUm3C8ZkDggxzhL25fswWlXxhU1Lm86pX1ga8bageC7YPc0doY5YPjDndog8GeLgju86U745wnzjPR_Cc_dsdpmE_gMRmBMp-eywtGzbN2hysr38bmyRUqwCvCCGjhVE50-thnV1g1YKKwhpcWh3P6MKVha-oJ9jbKSwVjribtg94WTEIk60vqBAjZneB3J8xU7nWB3LOoaWJysX5pDQA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
رومانو: مودریک از چلسی به تاتنهام با قراردادی قرضی HERE WE GO
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/Futball180TV/105237" target="_blank">📅 01:08 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105236">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nNSiY_amiQf1Do2lM92AVxL-mz4aupIrg84VICMI4Kg87mZr5C4rZUnfu97hzzzgypCHfs3dAag4AgneeGcvP5qDpzd5JzzwRcxppQrhN10MTTgTbirQbtEILrBp0T-y_3GVwhn40n3JSDkNeBzaVFZUVpXaxENgmaHH77TWDhfTMHDqtlNeMNVvSyg-W6-6v8tEtnb3pbnTGnyZCMjM0d4HvVRYq_2MqLrrq3UU2sPRzTd5He8JD1SwL-I1C8kJ4-HQAB5jOVrSyOs33fujEWoSNUpS7U0nwLR7cv2U4I2gWLC0OGWO4eJUNIinjsgnhWqq36GFJsGCEVA2Gg9k9Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
هفته‌سوم لالیگا؛ بلوگرانا روی نوار برد؛ پیروزی پرگل در شب بریس رافینیا و‌ یامال
🇪🇸
بارسلونا
😄
-
😀
رایووایکانو
🇪🇸
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/Futball180TV/105236" target="_blank">📅 01:02 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105235">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">لامین‌یامال دبل کرددددد</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/Futball180TV/105235" target="_blank">📅 00:55 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105234">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">بارسا پنجمییییی</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/Futball180TV/105234" target="_blank">📅 00:55 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105233">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">گگگگگگگگگل</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/Futball180TV/105233" target="_blank">📅 00:55 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105232">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">🚨
🚨
🚨
🚨
⭕️
شنیده شدن صدای انفجار متعدد در سیریک
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/Futball180TV/105232" target="_blank">📅 00:54 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105231">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">▶️
🏴󠁧󠁢󠁥󠁮󠁧󠁿
🏴󠁧󠁢󠁥󠁮󠁧󠁿
هایلایت بازی استون ویلا 0-1 آرسنال با گزارش هوتن خداپرست
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/Futball180TV/105231" target="_blank">📅 00:40 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105230">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/939ced1d89.mp4?token=r1h-ezJ_82WxAIr1cOKfxZtllfB2TjfPI5z5Q8NsGoiFj9FT5JRUmV6VEWc-z1pg0f76nGtgjxmdfvHbP4A9NrqedyK8tLXMkeShpDavERR_tcXhQnjBdvskocx5npeG-Wx6oAbYHSi3njIB__WX_W-jBAIcHRbX-uecVny5rlGxVNhVkKd4Cww-lZW94TeRumZJEn-ztKtWmVgfofR6MVcq4stUBLfcWNEYKHIRCwhMx8J3XuIMhNP3_IR9_hu1teGgjQGzE5z2NuSJvDVc6uP069DMpJIvLaA7o85kpJAPPbjfqvW7FKd8zzVMcpKLzwMjkbkT6KBnbU1rR29gc7W8IkFcF7_Vq_fkeeNz0HTqFdN0WQg2-q4lRZtYkew60snOx9wr41p2FvFwSDQBRAg9T4qALCiCEzZrxZkM7FYnDHhd9vG49b2JcfIKC-cb4Z0pBrYxy9EWFrp4LYoOy9K6Khc3-AlV1KP4mEO4Bkn3UZqrHqr0Pcz_S0YuROi5eF0N11VNHq3BZz33zIUHXCZ-3e71NG4J-07kT6caDmzMIr85VpJpZcmLJvSbLzTNxJWlJBLjQJZSawjsj3CeDpolVEk8Ys_uiESGN4VgtdmTzXPU-qGhrSqHVX0-Ygzq1UyAHg7H5ZoMDXz2H8Djbz6RYjOxmYEgew2rkR707P4" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/939ced1d89.mp4?token=r1h-ezJ_82WxAIr1cOKfxZtllfB2TjfPI5z5Q8NsGoiFj9FT5JRUmV6VEWc-z1pg0f76nGtgjxmdfvHbP4A9NrqedyK8tLXMkeShpDavERR_tcXhQnjBdvskocx5npeG-Wx6oAbYHSi3njIB__WX_W-jBAIcHRbX-uecVny5rlGxVNhVkKd4Cww-lZW94TeRumZJEn-ztKtWmVgfofR6MVcq4stUBLfcWNEYKHIRCwhMx8J3XuIMhNP3_IR9_hu1teGgjQGzE5z2NuSJvDVc6uP069DMpJIvLaA7o85kpJAPPbjfqvW7FKd8zzVMcpKLzwMjkbkT6KBnbU1rR29gc7W8IkFcF7_Vq_fkeeNz0HTqFdN0WQg2-q4lRZtYkew60snOx9wr41p2FvFwSDQBRAg9T4qALCiCEzZrxZkM7FYnDHhd9vG49b2JcfIKC-cb4Z0pBrYxy9EWFrp4LYoOy9K6Khc3-AlV1KP4mEO4Bkn3UZqrHqr0Pcz_S0YuROi5eF0N11VNHq3BZz33zIUHXCZ-3e71NG4J-07kT6caDmzMIr85VpJpZcmLJvSbLzTNxJWlJBLjQJZSawjsj3CeDpolVEk8Ys_uiESGN4VgtdmTzXPU-qGhrSqHVX0-Ygzq1UyAHg7H5ZoMDXz2H8Djbz6RYjOxmYEgew2rkR707P4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🔥
گل‌چهارم بارسلونا با گل دیدنی رافینیا و پاس فوق‌العاده تر آنتونی گوردون
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/Futball180TV/105230" target="_blank">📅 00:37 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105229">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">گلگگلگلگل چهارم بارسلونا با دبل رافینیا</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/Futball180TV/105229" target="_blank">📅 00:36 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105228">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">🚨
🚨
‼️
🇮🇷
🎙
توضیحات پیام صادقیان درباره جنجال سایت شرطبندی؛ من اصلا نمی دانستم این سایت چیست و فقط تبلیغ می کردم، تا الان یک بار هم وارد این سایت‌ها نشدم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/Futball180TV/105228" target="_blank">📅 00:32 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105227">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/40a24dc89a.mp4?token=U0nzBMaeIWX7vswrJ58kSWnc_ksgzLYsBup1TA7b9xh8JBgaVJ-E9ggdLxbNcrJM4vWpWHNSVhDqUcHEhmejL5tmQwdNXu3P476UQTY5jRH8ZOS2rkwIwm3n2NzsJbooQRVvS6tREj1iyXn3xVSO2k9RgIzIWsgGqvrTt3lKLYcaSgbZ-3O_MaJ7PSDHJ1azAp9W0i2KS2epc6eTG0W2_FQDeqdct23lTJIO8ukTbKW0I8-vBbaFEuTzkmdQD4GvNrcXYPsJx8Gac1s2S40XHii6ejj6c_DNOKNAxsp4E93dXNqr3qPhfVB5kQLpuIW2y0MlXl0HabNGnjr8Mv09Hg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/40a24dc89a.mp4?token=U0nzBMaeIWX7vswrJ58kSWnc_ksgzLYsBup1TA7b9xh8JBgaVJ-E9ggdLxbNcrJM4vWpWHNSVhDqUcHEhmejL5tmQwdNXu3P476UQTY5jRH8ZOS2rkwIwm3n2NzsJbooQRVvS6tREj1iyXn3xVSO2k9RgIzIWsgGqvrTt3lKLYcaSgbZ-3O_MaJ7PSDHJ1azAp9W0i2KS2epc6eTG0W2_FQDeqdct23lTJIO8ukTbKW0I8-vBbaFEuTzkmdQD4GvNrcXYPsJx8Gac1s2S40XHii6ejj6c_DNOKNAxsp4E93dXNqr3qPhfVB5kQLpuIW2y0MlXl0HabNGnjr8Mv09Hg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">کل‌دوم رایووایکانو به بارسلونا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/Futball180TV/105227" target="_blank">📅 00:25 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105226">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/0e2518b5e4.mp4?token=Q4g6k7ceR4kjYuHc7YqtnxGJcRj-sA5jwPBSsWuokUp7M1wzHA9OV14jd-ElxBuo9X3fMz-yyBV98XbTpT3pXsDNX0L6gd10tFwnAvPySsjQgvftiSDzsJ7uwIn52rVApdGqiKoH4wjs1DlZjJmZaXEMlJ3KPhzP6w2Idh5lfKubyrMXdCl3PIp35CqlVXri4fZWsCVTWaZh6IuzPc-IQqkCf3YUjoMWodgO3ooZLZCf_0n6vg9Eyotj3e94VdVNjuGSFM_t1MridPB9Y91640eTbQS-gB7_4-m748Hcs7cHCgIC5P8EhLjXcToApGPp1GGqKFhfe5bkgwvuh8WNaEXy7I-ZvPm8UVgznZkSp4e8vL-zlYOPi_r2DcMjSJQN-gCsFXCZOPPkFUqGoFJFdpB08aFuJQA786Tb9oeMXAPrPjs6pBMaS6bBxu80CVJdVf43ya1vyI66EQ3NO8RH-RZX9-istkdDGf14j699AzN4-v9A6eJLcrHj9JrfzfPo0lqHKqnA6OtjUROBkH_1lWcugU3SjqunqtMYR0f1wmcgByI3grhjNt4mbtdAbHDFRe9qQFeBMy4b5ozy4KJL1sT5-sycaZNGvaOBO0R4_1lP0vG_SjZ-XWAd6zoL9SNeV3Rr9udzo_pqH-KwpY4WGzNh7m2vj9Ytc99q82RzkVo" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/0e2518b5e4.mp4?token=Q4g6k7ceR4kjYuHc7YqtnxGJcRj-sA5jwPBSsWuokUp7M1wzHA9OV14jd-ElxBuo9X3fMz-yyBV98XbTpT3pXsDNX0L6gd10tFwnAvPySsjQgvftiSDzsJ7uwIn52rVApdGqiKoH4wjs1DlZjJmZaXEMlJ3KPhzP6w2Idh5lfKubyrMXdCl3PIp35CqlVXri4fZWsCVTWaZh6IuzPc-IQqkCf3YUjoMWodgO3ooZLZCf_0n6vg9Eyotj3e94VdVNjuGSFM_t1MridPB9Y91640eTbQS-gB7_4-m748Hcs7cHCgIC5P8EhLjXcToApGPp1GGqKFhfe5bkgwvuh8WNaEXy7I-ZvPm8UVgznZkSp4e8vL-zlYOPi_r2DcMjSJQN-gCsFXCZOPPkFUqGoFJFdpB08aFuJQA786Tb9oeMXAPrPjs6pBMaS6bBxu80CVJdVf43ya1vyI66EQ3NO8RH-RZX9-istkdDGf14j699AzN4-v9A6eJLcrHj9JrfzfPo0lqHKqnA6OtjUROBkH_1lWcugU3SjqunqtMYR0f1wmcgByI3grhjNt4mbtdAbHDFRe9qQFeBMy4b5ozy4KJL1sT5-sycaZNGvaOBO0R4_1lP0vG_SjZ-XWAd6zoL9SNeV3Rr9udzo_pqH-KwpY4WGzNh7m2vj9Ytc99q82RzkVo" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گل‌سوم بارسلونا به رایووایکانو
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/Futball180TV/105226" target="_blank">📅 00:25 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105225">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">گلگلگلگلگلگل دوم رایووایکانو</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/Futball180TV/105225" target="_blank">📅 00:23 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105224">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">گلگلگگلگلگلگ سوم بارسلوناااااا</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/Futball180TV/105224" target="_blank">📅 00:16 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105223">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">گلگلگگلگلگلگ سوم بارسلوناااااا</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/Futball180TV/105223" target="_blank">📅 00:16 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105222">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cd706ab6a6.mp4?token=A3EueqBlnKpPbC2oFKpqn6n7sE9x7lxnE8QGtKQZkVBmBmz6aZ4sIgdcisJEFYGtf7CJDfS3ppAK7-FawQrNQjToWlFwvaEe-k3HQLaSqmt8zXdRjJm9grdYZMJesXVpP28PdN1fR3XuoLiwdr8PgALvAr3LUr-wKI4Lx6o_5__np_uwAoNuD95xQ6ljvzuGfiOYY45jMjVbp7E_G3Y25Ytx7QCLNrehA6jxQAtDQDherl0nDZvbNsbtqjcMFHsTDaOXHzm1i_xlClbO4tgKo_6O_0iUyd7_ZeZ7RiBBOXuSu5WpKH0zvUGi7zLzrqfSyZ53J5rhk46GJlPLobKKsz-Jm_00GUJEVcKJawrn1CTXe1YJ7oa4Elffr8wGtUDb1a9Vanu30_6KMsDNEX-2Vtv5WfB_833N7jx9XXGNGRm5Cl4R4WBSLd9cYivDzdWpHZmH7cEexhcnnbCvxIpexxUywvUYM7wtWX6HSGusqG1G6xRz2SyRu7QtoB6KtYNwWxyc50a5pJqjkmxuFBlhgyDc42mlJk_oWqSKe-1IyGXFF02NJxAIIIrZCc947P6kbX1_AiDu8L_4LeO6GNATD082G-AP-wmPQQKSCu40mVmVXf_aAZvsoe70XUV5lIzyy0vu_iyLF4MVY-EbzrHJsxhXi0tnlCedk_Jz_i22GMA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cd706ab6a6.mp4?token=A3EueqBlnKpPbC2oFKpqn6n7sE9x7lxnE8QGtKQZkVBmBmz6aZ4sIgdcisJEFYGtf7CJDfS3ppAK7-FawQrNQjToWlFwvaEe-k3HQLaSqmt8zXdRjJm9grdYZMJesXVpP28PdN1fR3XuoLiwdr8PgALvAr3LUr-wKI4Lx6o_5__np_uwAoNuD95xQ6ljvzuGfiOYY45jMjVbp7E_G3Y25Ytx7QCLNrehA6jxQAtDQDherl0nDZvbNsbtqjcMFHsTDaOXHzm1i_xlClbO4tgKo_6O_0iUyd7_ZeZ7RiBBOXuSu5WpKH0zvUGi7zLzrqfSyZ53J5rhk46GJlPLobKKsz-Jm_00GUJEVcKJawrn1CTXe1YJ7oa4Elffr8wGtUDb1a9Vanu30_6KMsDNEX-2Vtv5WfB_833N7jx9XXGNGRm5Cl4R4WBSLd9cYivDzdWpHZmH7cEexhcnnbCvxIpexxUywvUYM7wtWX6HSGusqG1G6xRz2SyRu7QtoB6KtYNwWxyc50a5pJqjkmxuFBlhgyDc42mlJk_oWqSKe-1IyGXFF02NJxAIIIrZCc947P6kbX1_AiDu8L_4LeO6GNATD082G-AP-wmPQQKSCu40mVmVXf_aAZvsoe70XUV5lIzyy0vu_iyLF4MVY-EbzrHJsxhXi0tnlCedk_Jz_i22GMA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
‼️
ادعای بابایی مدیرعامل چادرملو: سه‌جانبه را برگزار کردند تا پرسپولیس آسیایی شود
❌
صحبت‌های علیرضا بابایی، مدیرعامل چادرملو، درباره پرونده جنجالی معرفی نماینده به آسیا/ رانت اطلاعاتی، دلیل گله از گل‌گهر
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/Futball180TV/105222" target="_blank">📅 00:12 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105221">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Vyf5fSoaBhNHbNCqUg10enbokW8c_6rnWiRflIVgoWID-CGi193iVXB0Ofm9M9JEGNceLH_m855GjjUTg6P_lUupk-nhZwA40wsoLfrQ-oroAFpGiUNc588-r2FkJl4S0xQa4OVw0L4mi8zBU2kbnxx4sxBVZKQXgbc11dVhY5vkUvVrt8mKmbDZguQqcyT9FrNSwMlfr6_YDNkZTmoMWtkM3mBB0toO6JKZMaalyzLY_Rr46Z2Q9pBQbJPPkz7cJC3twV-1aLNFx0Pl7po5lqB5_0GG3bnDrVCh2QmJTOGZCj0WO2tF2SZJwm7CrrCF4YYo5JgeSOew0_sIDiQelQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
✅
🇮🇷
🇮🇷
در نشست امروز کمیته داوران، موعود بنیادی‌فر نظر منتخب اعضای این کمیته بدلیل تجربه بالاتر نسبت به کوپال‌ناظمی بوده و قرار شده قضاوت بازی روز چهارشنبه که حواشی بسیاری خواهد داشت، به بنیادی‌فر واگذار شود تا بازی به درستی مدیریت شود. هنوز تیم داوری رسما…</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/Futball180TV/105221" target="_blank">📅 23:56 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105220">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/2a3572ef54.mp4?token=ZUcKh8V77lgItNdTXMKiXxdob0XtlL1vRpPW9hH2fMZBsYypZRjxxbeuCrrHXyULH0AGIqZuHG1hC_puA_EQZWDzwAwaXf7JAEkc9tT8tXv1txOnvDo__IZAJwyJaBH2s9zQD4huBoIFTF0UpFzcm67U2gFkq3W8b40e0jVyVzh-d42RdX5cCTbWjsxEXddC2_4FgOks1gE8J4sFQRB-KpssrjWkatPhh5rsCKhFuXzpv0eE29PY2M4VRd9M-roeLuDWHlrSUFmQcIGnpATiafqs8RsMSWJo3B-t7XrZ0KWvqywVyFg2eMnaukWEYi38ezVOmxO7FeVS9uVGzealk4i-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/2a3572ef54.mp4?token=ZUcKh8V77lgItNdTXMKiXxdob0XtlL1vRpPW9hH2fMZBsYypZRjxxbeuCrrHXyULH0AGIqZuHG1hC_puA_EQZWDzwAwaXf7JAEkc9tT8tXv1txOnvDo__IZAJwyJaBH2s9zQD4huBoIFTF0UpFzcm67U2gFkq3W8b40e0jVyVzh-d42RdX5cCTbWjsxEXddC2_4FgOks1gE8J4sFQRB-KpssrjWkatPhh5rsCKhFuXzpv0eE29PY2M4VRd9M-roeLuDWHlrSUFmQcIGnpATiafqs8RsMSWJo3B-t7XrZ0KWvqywVyFg2eMnaukWEYi38ezVOmxO7FeVS9uVGzealk4i-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🔥
گل‌دوم بارسلونا توسط لامین‌یامال
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/Futball180TV/105220" target="_blank">📅 23:25 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105219">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/88eb8f24c5.mp4?token=bn2SXK_y8YO_-H-8eQCjXuaIv-dlkC1VM2vp9xLT8MjPOIHHNM1ELueQkWb6mycVeJg5_sXLnard_ijX8AtIbhau2tccWI05JusGkVABKIFx9Ot2ufzsvKT_ZOyUMZ7KVUHiAnBwBpz-ZtCjYaOhEb56B2frtF84rEP10_xvRSPobab1ths7F0PzO_2wuyhU-KbMCWhfvua7mOrVScQKkuvmdsSLvhcdCfezkOECZsPgWLPR02rNttghwGivxZbK049L1Op1lSvSepjN2BlnoswuAF5tSvX6dqkQnvgTGZ91BdqUg6m_onofD5QVDi95gGPoPbMqM_0MvN6JEqPk54i-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/88eb8f24c5.mp4?token=bn2SXK_y8YO_-H-8eQCjXuaIv-dlkC1VM2vp9xLT8MjPOIHHNM1ELueQkWb6mycVeJg5_sXLnard_ijX8AtIbhau2tccWI05JusGkVABKIFx9Ot2ufzsvKT_ZOyUMZ7KVUHiAnBwBpz-ZtCjYaOhEb56B2frtF84rEP10_xvRSPobab1ths7F0PzO_2wuyhU-KbMCWhfvua7mOrVScQKkuvmdsSLvhcdCfezkOECZsPgWLPR02rNttghwGivxZbK049L1Op1lSvSepjN2BlnoswuAF5tSvX6dqkQnvgTGZ91BdqUg6m_onofD5QVDi95gGPoPbMqM_0MvN6JEqPk54i-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گل‌تساوی بارسلونا توسط رافینیا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/Futball180TV/105219" target="_blank">📅 23:24 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105218">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">گلگگلگلگل دوم بارسلونا لامین‌یامال</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/Futball180TV/105218" target="_blank">📅 23:24 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105217">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">گلگلگگلگلگلگلگ تساوی بارسلونا</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/Futball180TV/105217" target="_blank">📅 23:22 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105216">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/355ff97540.mp4?token=tdjBAwil1Kj4-f9uiL6wsW43wFWVq4zowkUPLGXHwmBqy0spKNJ9QevYf6rD8GZUo6P1LDlbXTh6UtlAt7-xNYZ3A86-39J2tEXTu1TQgO9XRUuyV_Ewn_2-SJOSHQck1hoSbjtT6qzWpj27lS0I-Mtk8GW21Y1pW8KUV3si7uE_UPh_jLNNJ726Lw6ZgPmXhvkzPd9GHqF-uBQQ8ncTyWOsSO6hRI_rWqZ7hpx9fV7qMAWnMj0q1rUa36ijgm8yMjm7YpQMcZ3lTSK27mayAItfx4InCg7GafzvwP968R-xKmzs_QxDo2vnPjgfPQ8oiW6544hZI6nBnIctsiFe162BOwbBY5g3iUbKQ_9YMPSst36ebqCoTmHLNs0cEx-RrC4l52schVTb0klhjU9s-p_6vzAaJb7TepjCTYc19cByZrf2AoXffVqkLt4cwOrkh8SiwUtoSw5VAPKL2zLNdOEnHHn2CyoNE4VFmalSM222gtrHMSB7l-ota4eerIztc6Sul02eAaZZMcXzfAt1hJ9OSrB1m6nnZCPg9ecbs8mKy_VQrOTJdtZ9mfSLF2GICGc11KswBmkHUsBcLHYfMPrhRTlhbdOyBXwy3NGhOIOgK623TIhu0LLlMZEw1h7LvVl34XAQE_NmDpBKvfz-_DHLtBFu_7I4bcpVQ_rMIJA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/355ff97540.mp4?token=tdjBAwil1Kj4-f9uiL6wsW43wFWVq4zowkUPLGXHwmBqy0spKNJ9QevYf6rD8GZUo6P1LDlbXTh6UtlAt7-xNYZ3A86-39J2tEXTu1TQgO9XRUuyV_Ewn_2-SJOSHQck1hoSbjtT6qzWpj27lS0I-Mtk8GW21Y1pW8KUV3si7uE_UPh_jLNNJ726Lw6ZgPmXhvkzPd9GHqF-uBQQ8ncTyWOsSO6hRI_rWqZ7hpx9fV7qMAWnMj0q1rUa36ijgm8yMjm7YpQMcZ3lTSK27mayAItfx4InCg7GafzvwP968R-xKmzs_QxDo2vnPjgfPQ8oiW6544hZI6nBnIctsiFe162BOwbBY5g3iUbKQ_9YMPSst36ebqCoTmHLNs0cEx-RrC4l52schVTb0klhjU9s-p_6vzAaJb7TepjCTYc19cByZrf2AoXffVqkLt4cwOrkh8SiwUtoSw5VAPKL2zLNdOEnHHn2CyoNE4VFmalSM222gtrHMSB7l-ota4eerIztc6Sul02eAaZZMcXzfAt1hJ9OSrB1m6nnZCPg9ecbs8mKy_VQrOTJdtZ9mfSLF2GICGc11KswBmkHUsBcLHYfMPrhRTlhbdOyBXwy3NGhOIOgK623TIhu0LLlMZEw1h7LvVl34XAQE_NmDpBKvfz-_DHLtBFu_7I4bcpVQ_rMIJA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
گل‌اول رایووایکانو به بارسلونا توسط کاملو
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/Futball180TV/105216" target="_blank">📅 23:16 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105215">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">گلگلگلگگلگلگلگلگل اول رایووایکانو
🔥
🔥
🔥</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/Futball180TV/105215" target="_blank">📅 23:15 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105214">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0f1302c5c0.mp4?token=TU8VJB6bRki760Ary6ZF2Hhy5jECe24VdU2SInij5RQbFvbCHqDlbVbN9DhyY3sSDdO5GzeJQ1SeinArTjbQ9oc557VZpD-FAcedBoLwZIwScZ7TDgGQ3vjDmwQW5qnxjL29rWC6-2Adn1sGz43Z8L1Z96Xlkhtr5-MT3FzuCtiaR4Znttwo0nbs3ZMVyqBiiPReyowq4SmdBh03gnGiKB8WzYZh7slh-LqkjaEtOiebwYdimSGQDOJSMcwBvslp-XIJSyojs8A8UrY9JLqDpwtxXFPIzbIKSH-hhXNwkYodx9TyCg2TnAE9bEa7ctATeWmwawePsApHOTdLmiRmQQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0f1302c5c0.mp4?token=TU8VJB6bRki760Ary6ZF2Hhy5jECe24VdU2SInij5RQbFvbCHqDlbVbN9DhyY3sSDdO5GzeJQ1SeinArTjbQ9oc557VZpD-FAcedBoLwZIwScZ7TDgGQ3vjDmwQW5qnxjL29rWC6-2Adn1sGz43Z8L1Z96Xlkhtr5-MT3FzuCtiaR4Znttwo0nbs3ZMVyqBiiPReyowq4SmdBh03gnGiKB8WzYZh7slh-LqkjaEtOiebwYdimSGQDOJSMcwBvslp-XIJSyojs8A8UrY9JLqDpwtxXFPIzbIKSH-hhXNwkYodx9TyCg2TnAE9bEa7ctATeWmwawePsApHOTdLmiRmQQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
🇮🇷
در اولین معاینات پزشکی از مهدی ترابی مشخص شده که این بازیکن دچار پارگی رباط صلیبی شده است! معاینات تکمیلی قرار است امروز انجام شود و نتایج آن اعلام‌خواهد شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/Futball180TV/105214" target="_blank">📅 22:49 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105213">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">🇮🇷
مصاحبه‌های منتخب هفته چهارم لیگ‌برتر
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/Futball180TV/105213" target="_blank">📅 22:22 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105212">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/782a933b7c.mp4?token=Ffsa7irzfb9n1A4sNE8d935BYcttu0RKIAXzWzxtVHtkAt1soQdmI2x8bvWqrdS87OyBfpp430tByzIK-GHCUEhNJqq-jRLNYgkBsFmnRBaXyZ7Pu92eus0lTVCWGzVK6IQMDhGbxTzFV37By93LuQfg4pCRpFQiW5i_LwW4jObXMxj-MB7SKnoIprXgih_p81z6eb-07mforbuhtI_ro8zLP1zUA9j8p0v2Jx0HLGDWxeJJ3ZI_msoUZgCp9uvny5hs0Ue33ivD5S_Cvu50jbmXUek8OumrgpRjAXj5h3ctOYuIpWAQFOkjs1nl0DtoiwabE_HGpw36n1zrVJk-6w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/782a933b7c.mp4?token=Ffsa7irzfb9n1A4sNE8d935BYcttu0RKIAXzWzxtVHtkAt1soQdmI2x8bvWqrdS87OyBfpp430tByzIK-GHCUEhNJqq-jRLNYgkBsFmnRBaXyZ7Pu92eus0lTVCWGzVK6IQMDhGbxTzFV37By93LuQfg4pCRpFQiW5i_LwW4jObXMxj-MB7SKnoIprXgih_p81z6eb-07mforbuhtI_ro8zLP1zUA9j8p0v2Jx0HLGDWxeJJ3ZI_msoUZgCp9uvny5hs0Ue33ivD5S_Cvu50jbmXUek8OumrgpRjAXj5h3ctOYuIpWAQFOkjs1nl0DtoiwabE_HGpw36n1zrVJk-6w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇸
لحظاتی با گابریل‌ژسوس خرید جدید بارسلونا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/Futball180TV/105212" target="_blank">📅 22:01 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105211">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FEmOUn1FADozGoj3V5dt9EcG1CKx0QAqfyTVoMmNeOlMZvXT0KfxjryusPgfFCG2dQo_k5c9a22BXVtkozTuEv6adrg6QhlCu_RQazMmGm3hCXv9OIlAZc8yyX9jxFhsd50gg6ySATxykkvISylS_IAu9BeDtXx9A1KYf4GxKDyG7cGQiyOijjXS_jCpqKUewipBjJbnChy6CTzrON9eF6ZmHsXHZJiuHcqHU6O2RM7F_OXAqffJt30G1snM7mZoHOl4-3IBAxuL7h0nr5IYGOB5m1EpoYXcXawS-fzkatPV3N6SIhCqFfz9h3h-vqATPBL71uGra0yHO48ze2ty0Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
✅
🏴󠁧󠁢󠁥󠁮󠁧󠁿
رومانو: ایلمان اندیایه از اورتون به منچسترسیتی؛ HERE WE GO
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/Futball180TV/105211" target="_blank">📅 21:51 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105210">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cIp4TgCGetKC3-jUJYohDoi-laltUvEC656R3AidOK2dWu5rivFrDYYrlA5GMT3LymZjqbguFpDWBbX6ikTisq2aqpQI530pVf8YHrMiJcT0ophPI9LRUsZeB43AbPc_G-a-FEZ26KbnXQbdSxvO8elJDTsq_E5jLJp5OmdMXD19jWI_dMci_i5SObuTd3g_EcDS7Ie-bEL2iaNWdl-2c3Bk9o0NRBaf3AHprHwVbrQhV2rY6r4Juz9HSDaVW2XYJGPAkxLUzpvkvIlxmAqSKKB2YK4QRGqIAo0GBddxMXqel5EYH8luD2hYdmSD0tXkUSC5mQqQ2wX4Is4G8IX3qg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
🇪🇸
هفته‌سوم لالیگا؛ شماتیک ترکیب بارسلونا مقابل رایووایکانو؛ ساعت 23
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/Futball180TV/105210" target="_blank">📅 21:46 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105209">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vuNo6R938Ez1CyvhI8yjq5O_Ko5zWCtCHDijxfJpyEEudMDVXlZau3zGOUJ8SXtoM8r3sH4RkU9wPp3fhrvxBdMED0hUJfSPR3V9bCKBAgD0T4xhf8CZ4g9uYXAvoq5mGAoDP9hRn9-XFsfJZs7H0HAIDm1BRl1rOdyGbAMlJsycpnkY-rCzJQG9a4h6sxk4k5QRRs_o5PX_ota-Uy3OV3lscuiBq3LBM1r9nfZcd1vHLTwVzl6O57-xK5UgW36qEY4MDUipbAIp2ua4FZlNHNKNzOLJCJLwgeXQrVtP5ORIXLgQLnWoq_qZtcLGPF_F02g3Ign5i83GVrm_U6bUPA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📱
💋
با این ویدیو فوق‌العاده و غم‌انگیز رسانه 433 میتونیم ساعت‌ها گریه کنیم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/Futball180TV/105209" target="_blank">📅 21:29 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105208">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Yr40Wx9RbYK158_9v-ToVGW8CxYWLLo3qhc7bYjNR7Ixw-UCUd_Z-LoHlz_qAvM3sXNk47TbTMIIFbqvSG-jkgjljcYHv5AmNCrJSfsL_11beYGnQ_rzmgsCzY_BzUdWgKDj7S9vEV6GbK2YQb1fxdKa1l8-rgicRzgs7Zsz7qL41rVyQb_wHzM0_eBq8gXF5ZYNu1Wexp_N529clOLrARhLNE-Fqhm2Qx-4YUao4eXEu2bojTTTTcq6eGPk3OnG-FnXC3fluCbwK7fxoPnppMPBWel64vaO4N3kNa31u_h-H09c6sooqscC6JZwQu0KCssAQ0q3ibaPYNmv4NJdcw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
🏴󠁧󠁢󠁥󠁮󠁧󠁿
رومانو: اولین پیشنهاد تیم منچسترسیتی برای جذب انزو فرناندز به دست‌ چلسی رسید
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/Futball180TV/105208" target="_blank">📅 21:24 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105207">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/t-vHaKboTZzjFI2B3AQLIyN16Zei4mcmO7HI81C-kL_sGZHgOjvsG1m6Ag44u-cSv7u6s8YJS5di6riKjfZMGzHw1IMgzCAXsBl2C81yrK0kgr-x3xA4Akw0Haz9yk7NiWncWEU8DpK3ZedvF436YmIhfuPJ63h3BiyD7XQnzSMElNkVBO_6mIOmzxqIUC02p7D_6egYp0_pntHoS5NhRkfyN-6LNWGXwCZ2BsJo9dv3mX2pKLivGW4O-HQCj7yzscV3Xa6qewJBEV0EpjtdNBhgSmGV1t4A1h03pXOpoQzU8bkPZ0unqt3VsKZCXd5-kGo3oRTbXJzLjOR0RLZbGA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
🏴󠁧󠁢󠁥󠁮󠁧󠁿
هفته‌دوم پریمیرلیگ؛ ترکیب آرسنال برای بازی امشب مقابل استون‌ویلا؛ ساعت ۲۲:۳۰
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/Futball180TV/105207" target="_blank">📅 21:16 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105206">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oNfxyztn6ooAZIRjMmX3oIeQ8FKL3kJ0Yn3ZzIT25xqrXk12SoNOPmIwm9QdizevwCY2r-f7FvdDIexpl6gtdrEvCuRWVld7ltflINKzb4P_ytTgMuT35qPEihsUlkKfuTwveX7WHbPNrBYlO_QomevX-hIAEhDVm-Qg9Y0M9FtO64VKVG8nmV-yxQ7db1bhNuHf1CW44pSMyRAcM1zprU7pvxmdqX786eLYhkDCnBpm8zGuHw7nbxerfCxYNbF3JwWqZO9kHt9Szm3oOlyg1adX6ZysDmdDwmD02Ktt9QjwRDBPJ7H9FwYlZ5pLE3awLKZvVi4WRyKRluTNGlwYPw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇩🇪
فلوریان پلتنبرگ: آینتراخت فرانکفورت درحال بررسی جذب خوسلو در ساعات آینده است
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/Futball180TV/105206" target="_blank">📅 21:13 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105205">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EQmiJwjUcDPH1H5t3neRPyknk2Uk-cKChoMgDyi-hSgtq4Xz-k8MrDrPF6PPygDdzNCUMGuqHxxGeeBy8-eWykQE2pjqYy9KaCELdk4TU_cLd0-k1CbSdVbIi2OV630i0WMF0Hnp1J4ccfT6NnMGcBb4uKo2wQDbltT1RCMFaP1BBI0yJKuMhmEtfbfwF6imZ6V6MvgMT9ibGubpSd66n0HegtkOGzw_PV_13WCPzCl6rcWD351yTdqLxTUm6hAz5t1P0Z9PJ3R0GpdjvSErKgT66Ub7GqEfYghT_NVyPvOLro2kuFCKAWYKUbmfYLjJsP83krCfUnG0wSaI_i5c3g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📱
💋
با این ویدیو فوق‌العاده و غم‌انگیز رسانه 433 میتونیم ساعت‌ها گریه کنیم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/Futball180TV/105205" target="_blank">📅 20:59 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105204">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lLWPYZkf2jJSphKP8h8yxV52AoTi4ihjFTSg3RF2s3B7yMTp8xEJmLYQE7UrVVzM1i1f_QW0ZveVHX4PQZtpsXMjJ0C64Q6-J54oFQ21CTcZpHVAIYTjQxCw-ftvilWPlx894Dt2IPGvSlGG5Jw3Gw05YsbWwnHTNT_20pZ48taziBGRJkYM0UY_TFmMBFi2cfUhjocpNTGONHNjQSlheCzUUYL3OEuHZ9U0ZPtIYH4R6fBC0U2xSr7lJv6iU1nxWGrBuiU-alqoLDEQH5o7dbWB39QQnVt8fBa41_NYnGaNldonA4t7OBP9IOm49VQoxB9Uqn2pWBEHjar0jGLt4g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سایت بلیت‌فروشی دربی طبق معمول ریده به خودش  زیر ساخت در ایران 0 گنده‌گوزی 1000</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/Futball180TV/105204" target="_blank">📅 20:57 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105203">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">🚨
🇮🇷
🇮🇷
⭕️
#فوووووری؛ بلیت‌فروشی دربی آغاز شد. برای خرید بلیت از لینک زیر اقدام کنید  https://ticket.sepahansc.com
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/Futball180TV/105203" target="_blank">📅 20:47 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105202">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">🚨
🚨
🚨
اعلام جزئیات بلیت‌فروشی دربی ۱۰۷
🇮🇷
🇮🇷
بلیت‌فروشی دربی از امشب آغاز می‌شود و سهمیه هواداران استقلال و پرسپولیس ۵۰-۵۰ خواهد بود.
🎟️
ظرفیت در نظر گرفته‌شده برای هواداران: ۳۵ هزار نفر. سامانه بلیت‌فروشی که فروش از شب شروع میشه:   https://ticket.sepahansc.com…</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/Futball180TV/105202" target="_blank">📅 20:35 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105201">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/l0_hgQNzT_7NYJURDZTBoyFmPkWTXWItbxi0nDe1OAOJ_T4dkqwycA3Q0_6WqD67jCvq5x5m7j2537rkPVQKervo8bJzTbnT3JekUl1Y5N-PiTomvaGV6fDhsUtxNndldL514o0DJ4vNLIb0aCID62-_F9ySxEb6PfS4iO2nRhgj8EO5gz8Hi9HfnuirPeIBof6J1CuGPw9c-pb_EBqPsrDkVDInPUfAgGe4WZ4-lrPNCEaG6nVyQmhKrrH9QN4TuBfbZByisHPdG4N96eZjS0Y6h3vPQfhgsSUE_FW1iyOH88eD67grY7jXpA_vdtmYBhu0DrJVotlJyTz7XQCmLg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
✅
🇮🇷
🇮🇷
در نشست امروز کمیته داوران، موعود بنیادی‌فر نظر منتخب اعضای این کمیته بدلیل تجربه بالاتر نسبت به کوپال‌ناظمی بوده و قرار شده قضاوت بازی روز چهارشنبه که حواشی بسیاری خواهد داشت، به بنیادی‌فر واگذار شود تا بازی به درستی مدیریت شود. هنوز تیم داوری رسما…</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/Futball180TV/105201" target="_blank">📅 20:32 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105200">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/M_PHKvtvqHZTPIvRhpIuZQDgXdV5ehRjR-MQl8XprOngYZVKNLy6SFm4SxAfTKCZSMZmJFfhsWzvBXz2Z4Dvjj8VXzjs3wwvPOc1udBK1nGVbzCjxzNCDJhjiw8C0pI2t33OZICo084VBKVoNlqDZOFKMl78gsNNKImSCfhw57XciSJaLLleL2lOAq-5-xwz9ADj57oiAHwhXEwjTlFNY1t7XhErlaECDLfwcj_Kl3M1Z0rStkJqcZorLVsMV172rZsR55jzJES70ZZ7DgFphE-KBDu3IS-V1y6fVyyjE2r-0CNLTWeRp7pi9xvNkkVf5wElGWTKlWCbsp9KyfT1Gw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">😃
قدرت دوس‌دختر در بازی دیشب رئال‌مادرید:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/Futball180TV/105200" target="_blank">📅 20:30 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105199">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a8cb7444c7.mp4?token=sYCsRb3IibVrnLlYff3AuDQ2BFazbPK26xl4sPZPI9rNZXSNFpSQNhbnTwU1XClznnv64KQhIzXFvaEuzC4JDHyILhL6TOzvn9_70omZqmkW0nhvTzGN_qNuX-Aw-K1fe89iQXi0befJGEZInWZClN3gsqW0G-H0u_MtNeFEigFrkb5LvL5WVjRpdh03W9qUCFgwvIMdZ1H5atmhQpC_f-AdCr1LbMz9a5-Pxer_0frgvgs2t__NwGdKqeO4KGa13pKkp1oKpXacEPf-8PPdxBEe0AYFP8UULqufX39U8wzoD2q6kB8Qn2VzcUzxR-Z9dnyO8XPKZye1RxtZy6vVpItLSXfjQ4CVSuS4UnIcNWBigXE0W4dT96Aw_C_oaf9T9a53KxEhsl46tz1cd-QRmhREsYVxU4AQpHia_dBTrhzDCak7cyxgy-oV2BHXzLNdejcklf4Qqg6YBQYtTrAEKZbwAOga00IyPVQEV7IzcOzhJr9Z-8_TVG8Uq_AFFv1E-bAIWK8Fk9qSf4rSGK8lPm5YZBobT3PGdOZAGOJxg7fwSlxH9RMhT40ZzjvXIUlY1iCop9g963MhDtZ3NXOMkljaC51xQL4vSF4LO_FycTze5op5Fa5BQsc6Rqb2kLooiXFDa_b3ZLKaPoxGP5VXUd1Fee0J7MBqqt9N1dGjGE0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a8cb7444c7.mp4?token=sYCsRb3IibVrnLlYff3AuDQ2BFazbPK26xl4sPZPI9rNZXSNFpSQNhbnTwU1XClznnv64KQhIzXFvaEuzC4JDHyILhL6TOzvn9_70omZqmkW0nhvTzGN_qNuX-Aw-K1fe89iQXi0befJGEZInWZClN3gsqW0G-H0u_MtNeFEigFrkb5LvL5WVjRpdh03W9qUCFgwvIMdZ1H5atmhQpC_f-AdCr1LbMz9a5-Pxer_0frgvgs2t__NwGdKqeO4KGa13pKkp1oKpXacEPf-8PPdxBEe0AYFP8UULqufX39U8wzoD2q6kB8Qn2VzcUzxR-Z9dnyO8XPKZye1RxtZy6vVpItLSXfjQ4CVSuS4UnIcNWBigXE0W4dT96Aw_C_oaf9T9a53KxEhsl46tz1cd-QRmhREsYVxU4AQpHia_dBTrhzDCak7cyxgy-oV2BHXzLNdejcklf4Qqg6YBQYtTrAEKZbwAOga00IyPVQEV7IzcOzhJr9Z-8_TVG8Uq_AFFv1E-bAIWK8Fk9qSf4rSGK8lPm5YZBobT3PGdOZAGOJxg7fwSlxH9RMhT40ZzjvXIUlY1iCop9g963MhDtZ3NXOMkljaC51xQL4vSF4LO_FycTze5op5Fa5BQsc6Rqb2kLooiXFDa_b3ZLKaPoxGP5VXUd1Fee0J7MBqqt9N1dGjGE0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
آخرین وضعیت زنده‌یاد ورزشگاه آزادی تهران
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/Futball180TV/105199" target="_blank">📅 20:03 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105198">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BT8FCKAtjCEUHmSwbn9NhxwPgL6CpMHAfMwXv1HfppZtxncMveJzkJAbsOaO35eWG-VoUGax7Gp53Qcd0vOQexyxUfjPUSyra0t6h9n5apDvGnOnjgrqEdb2QtYZNniBDgZRGxGxPd2oofvO5u9_GEWiLUrb9hXgpi_5ZGA_2obeSgsLgrRtUHC9hQ_RUoqWTk-b3mIJHV2Z2pRgWJMSrAsf51kK8AS7d3HzZthf4x0Z0oG1BP_H1c9FmtWco5nH33XDcNoIWVLReMXbKKbVfHFHCMxp9VCMODNHreZJNUOex3nCKVcyM0fwB_hb7jXEq5m97ibyCHADcXlr2QvSsA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
‼️
🇮🇷
آنتونیو آدان: به باشگاه استقلال گفتم که نه پول فصل قبلمو میخوام و نه دیگه حاضرم به کشور جنگی ایران برگردم. قرار نیست به استقلال برگردم بخاطر همین طلبمو بخشیدم چون وضعیت ایران خوب نبود و مشکلات این کشور رو درک کردم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/Futball180TV/105198" target="_blank">📅 19:52 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105197">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/q4Q7XUgDD1tIBW61wCvVgQXyhb-AeF8m-ysenfu7m_AZVAWQSEIfcCt0t1Zu7uYJVlsSu6-HmuolIyf-qMjhCH7UFRctDIz0XtidCIlrY0pzp37I7i5iR89OFvhYaiyoLrmwxH_UguSXuHAmoE8GM1RKZODumeBU9A3q0sGDzyg2zbPxO5OtKvKNUesPYS87q7WCiKtvIQWtvMuQcwbIloyLdLYjpLi4_G9lhs43f2eVegLhn2PooQ-jjy6K2GExdUicIfrPtbidVR0-J9NqWkEwgo7qriOVeQb16fOx7wR2E4htJ2Yc5eEHFjgz7wnb_gjeLaL0Ga1iLrwGJjDHWw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏆
نامزدهای نهایی جایزه توپ‌طلا روز ۸ سپتامبر رسما معرفی خواهند شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/Futball180TV/105197" target="_blank">📅 19:48 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105196">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FO28TqHKnkWmcsoBb71h-pv8FLSRA-S9vjPP1F6_4PEQ7TfHS2tcst2mD6Nh0KSOcY8tvxsW_sWdMmVePvot1KyEre0uoV1NNngBLU0Ie_kQHeJrD7SdSvGMKnHuGvlco5DriNWCaU80euqeTaq4pPUhhmZosxL_dFOd_pAUMGPaDdo7vnoTemDxSwc2v6Fy-O1t1w4lpDJVOBcuI8MPjupmAo05NAPIaU0H1Mb1joDehpB_j3bzB0CBs8V2XRZFSIxbVhDRHSXU34N-lw265xzpJ0U2fWVHXLyrJPMCqbNP16PcOFnSotHs41B_aOrkgL3fmgrD3fJ9p77bUa9aLg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚫
🇮🇷
🇮🇷
دربی با نصف ظرفیت نقش جهان؛ این اسمش مدیریت کردن فوتبال و مردم نیست
❌
ظرفیت ورزشگاه نقش‌جهان برای دربی از ۷۰ هزار نفر به ۳۵ هزار نفر کاهش پیدا کرده؛ یعنی عملاً نیمی از سکوها خالی می‌ماند.
✔️
در دنیا برای حضور بیشتر هواداران راهکار می‌سازند؛ اینجا اما یا تماشاگر حذف می‌شود یا بخشی از ورزشگاه را خالی نگه می‌دارند و اسمش را «مدیریت» می‌گذارند.
❗️
مدیریت واقعی یعنی فراهم‌کردن حضور بیشتر و ایمن‌تر هواداران، نه ساده‌ترین راه یعنی بستن سکوها.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/Futball180TV/105196" target="_blank">📅 19:39 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105195">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/F26bMN4vM9Wkf6jfnaUKoD7Ea6fGIPckrAtkc0jwixes1iEzoBZN-1MY056wuHsgw6w1idA9FDncy0yeUTZxS5GStUTQ3lIxmgc6adjUqLy8BGBkmTyIWDp9nKAfd2NtzgHVgHzKdLwoRrNcudekrcxEFgSQUgDuJZmeIkw59x5DC2KEovQuGntyoHziMNxbY4PSZN-W_pwwwLp15ldc0j3YBWjbo7IeC400qzNOlgZeoTOJ_TfHCdFm8xYb-pCSLkAmq2ub_mahHQtporydYBTdCOgDGbjk4S3usQYW4AD3Qqzp0q38RWX-bMIoc4A1cJQFqev5LtzHnc6v1WNL9A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
🏴󠁧󠁢󠁥󠁮󠁧󠁿
اورنشتین و رومانو: لیورپول پیشنهاد ۷۵ میلیون پوندی سیتی برای جذب گاکپو رو رد کرد و این بازیکن در آنفیلد موندگار شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/Futball180TV/105195" target="_blank">📅 19:31 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105193">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ddcd857187.mp4?token=lxtZk0GF4qPKREzywQ8g8zBavwlG4QiQB7xcUWG5BYYmgVss9N3CtCMvsK3TixyIln5XDBsMfIGh3efAZnm1AiP0sjeXYL07ZaB2yH07zP8xwl6kEdNyn-TGBuK89CVBOE49nWVJNdZjr3-FmG0zbM5KkjMrAC7J5K5Tv0-7ROjwSZjJAVt2vU8SyWEdBqrVfSclG_OXASHcziwCjxDPQ6UowUDhIjqwUI_NiDmGKkCYb8GR2gn4NjE0qJau1LEncxpMugJtAhrycU4-5BoBbTrKsW955ttgl6JoTN7WvNXtUqI9bzU2VIO0kPRa1l6PbfUTFPTiW-eP2GhCx2EoTQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ddcd857187.mp4?token=lxtZk0GF4qPKREzywQ8g8zBavwlG4QiQB7xcUWG5BYYmgVss9N3CtCMvsK3TixyIln5XDBsMfIGh3efAZnm1AiP0sjeXYL07ZaB2yH07zP8xwl6kEdNyn-TGBuK89CVBOE49nWVJNdZjr3-FmG0zbM5KkjMrAC7J5K5Tv0-7ROjwSZjJAVt2vU8SyWEdBqrVfSclG_OXASHcziwCjxDPQ6UowUDhIjqwUI_NiDmGKkCYb8GR2gn4NjE0qJau1LEncxpMugJtAhrycU4-5BoBbTrKsW955ttgl6JoTN7WvNXtUqI9bzU2VIO0kPRa1l6PbfUTFPTiW-eP2GhCx2EoTQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📱
💋
با این ویدیو فوق‌العاده و غم‌انگیز رسانه 433 میتونیم ساعت‌ها گریه کنیم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/Futball180TV/105193" target="_blank">📅 19:07 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105192">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">🚨
▶️
🇦🇷
ویدیو جدید اسطوره لیونل‌مسی از دوران حضور درخشانش در تیم‌ملی آرژانتین
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/Futball180TV/105192" target="_blank">📅 18:56 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105191">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kyppWmtdkiLx9HLNywUiGOku87O2_k2Z_ncNfxO-38HhG0KypKqssu8Es4tqZiPqF1F6bohgiGGbo2umVHB_lvHn3mRzpkP2m9km_Kh4ZMCnB1IcsSRZUy94MBBvlpFKblgeO6FXE71FVo5yhPJnpDDgsKopwOdC1SyhbYlr_VZaf3mD9oYlUxd-kn9X0119e7xq-UNvCL445tZtXkk9GRyUb-FicT1nU8tnbUeydHPb4qwHcZlWxL0lysz5fNUHF7YumZRjPqPuDLcOVwXo-ZKBSTq3GfnS-Z1-b252GXNb3ptGtFB19_29YJkLa0Msftxsdugp5vppq6ttydw6rQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
📊
🐐
عملکرد اسطوره لیونل‌مسی بهترین بازیکن تاریخ در تیم‌ملی آرژانتین:
🏆
1 قهرمانی جام جهانی
🏆
2 قهرمانی کوپا آمریکا
🏆
1 قهرمانی فینالیسیما
🏆
1 مدال طلا المپیک
🏆
1 قهرمانی جام جهانی زیر 20 سال
❤️‍🩹
207 مسابقه؛ 125 گل؛ 68 پاس گل.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/Futball180TV/105191" target="_blank">📅 18:55 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105190">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mAb8RizM8tATZ6xB8NJhIPU32DD6Uw-4c2L8PjQaXaWgdItcNZQPzgm65WZoypEEi_0ty6Ryhs00q_dVRE9OwYyTPM23pZa_GtLCBpbKhtPya-I0Tw1rv_HAkLQg9L_0mhHC2mn8tmXjWhlh1ZIPRqfIIkew4kdxyd_g1Dp3EInUdzTcQxOTn6M5QN_pSOtYdBQG-E6qDEgoXWIzixn6nQImZkB5FoLPw5AYOEx4N0T_NsoMTqsVWq7IKP7yqGnn5EsIbyNXeJMcSKFa7A6wVLiQdtthHZl50vmfKtVTpnDuXyrj0NhDUc3XLfAoRhLiZzkQcQQBxH3o-2bgSWHg-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🐐
📱
پست اینستاگرامی اسطوره لیونل‌مسی و اعلام خداحافظی از مسابقات‌ملی:
🔻
دوست دارم، و دوست خواهم داشت، و همیشه عاشق این هستم که بخشی از تیم ملی باشم. تمام تلاشم را کردم و دیگر چیزی برای ارائه ندارم.
🔻
همچنین، بازیکنان جوان فوق‌العاده‌ای هستند که در حال ظهور…</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/Futball180TV/105190" target="_blank">📅 18:46 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105189">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/s8ejWp-PtiWxy5Fb7oE8TvvcPG3_mWdmYy9aUa92OtBiwNkZmqa4K3phODIb9-FZ40twPzKjYEF7M6NVSX4UMFq0tFCqTseqI_S3bI7Fk5xIVitFiMHdd_OIs3nnQmC8D_JuG5WK7BMyjTkInpdN88e5T06zlUmgchQKnQc6u8UU_S0M2eF97Paqh46HuAYG8qynoRoM5aPf8VFOhsYmojpshx11QpXISGC_sN1IGG4P-CIZUs7CmI1PGpC7OXirJCDjut7MMSqz-ZQY4mu6fa0t0CY_J_RdBh1NxQ7x3ITsI3nnLbyq-hwo1s36TcVCXjHmd7ejFHtegg-kPumXXA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🚨
🇦🇷
❌
#فوووووری #رسمیییییی؛ لیونل‌مسی از تیم‌ملی آرژانتین خداحافظی کرد!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/Futball180TV/105189" target="_blank">📅 18:40 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105188">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/E6TvdTBrbYtLeuihgIq5LYtVh0d_xtgVajuxPzbLLT3ykql4COstB_D2_Qle975EIZnx2jXKlThShHLYiT7eipiLdsMdxp8HOgkjb4T4M0VNW2TxgYyH3u0ZXQfve-PStIAQ-RfZ_uO8LbkeeTDfDbrWVlkym60bVx0aKTknBL1Uhs2MMK9OIj3Sblfs2Oo7E8iMLvHHNYO-lxbfkE08Vo35iRJiSv6Fi6Xpq1srvfqiHzT9fCqW7dSTMkKnb23NipHDl35ByEy00ZUExEF7WG6ZR-RIwKhO0k18IytqkMLScTIsPbVVQ2liUOKa91eT70wVvwOenahwGEsm4sfNPA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🚨
🇦🇷
❌
#فوووووری
#رسمیییییی
؛ لیونل‌مسی از تیم‌ملی آرژانتین خداحافظی کرد!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/Futball180TV/105188" target="_blank">📅 18:35 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105187">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hdbv8IDz3PLuA6-YGJjbuER1tyl0tfXLi6lYnqFAGwOmyj5kQvziq5Crn-3FF4NpAMxRXPIdv7F7xvYF8-C0bf4e558MVgZbRNrqYQnQAPoybAM0p73PzWKJaIDfa-BP0mIMha23Od26Qxezmdbavc2lg1VDuloDkomhybn6PUX1Ovu-wReUQhFTMordtrPH2-XctkjL6MZi2gubdnwyDIbjfrHcseVYu2gg54XtPxMW09PPQi0wS-Yu61pHgdTQe1zhS0LSlPtMlrG1mROr4MKlllhF21HiNRvg7uuaIEQbSOBuMqyIx96DX6Q_NVUe0Kt3SV2CHeMs6Gmkcn1O3Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
🐐
مقایسه عملکرد مسی و رونالدو در میامی و النصر؛ کدومشون بهتر بودن با ریکشن بگید
لیونل‌مسی
🔥
کریس‌رونالدو
❤️
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/Futball180TV/105187" target="_blank">📅 18:32 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105186">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromMoris News</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lAuxXtY7c6Dp1BPol-ST0JPRQBxdzIrfpHOdlnrWGokfmZ2Q4RJRtLcmj_oevA7wo9ypUWAtfNJaSXB1nSal88jfIxuwxJoCaIIm9E8SkU8Bh8G1UQRJs33CooVCxO2M5I5MolbnDoQOushR7TZrCMBmbkQRJnG39QsIiIsaVlJnkNT7rInx_MK3JlQeos0AO6RBeWTZRuShaXAhCQPlErPMj1_V-qt9BFcOejgG9Hn8Qvt5ZPD3--sc0Fd33I9azXcvXjZW25CqlO8I86onRJYagviXgc-_TjEusLwrKa8hGHGkC7razi42xKcMJIaJHxPnCmbYWlZAy8h-inAIIQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وضع خیلی قاراشمیش (یاغی)
وزارت نیرو اومده هشدار داده که مردم بنزین و گازوئیل غیرمجاز تو خونه، زیرزمین یا حیاط انبار نکنن، چون خطر آتش‌سوزی و انفجار داره و ممکنه با افزایش قیمت سوخت بیشتر بشه این کار.
گفته فقط اگه واقعاً لازم بود، مقدار خیلی کم و استاندارد با رعایت کامل ایمنی نگه دارین و موارد مشکوک رو به ۱۲۵ یا نیروهای انتظامی خبر بدین.
خلاصه مواظب جون و مال خودتون و همسایه‌ها باشین، این کارا خطرناکه و به نفع کسی نیست.
@Moris_news</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/Futball180TV/105186" target="_blank">📅 18:32 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105185">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0f80bffe56.mp4?token=lTTj4b5pzba0vXwNOobCxdRQj10Gk1OfdPbxlMMCgPWdbwByespv7S1K1j7Rr4AMq6SxYf3rxBxbbJxJWJ2xrkNDQnRzDIqk4k6QPzzJgDKz0L8XsAw__Pr5FFTAISLJrz3siE_rGLp4HnoJgBhHpQzlRV5xKk8j8zx2Xmoe0SrESV_6C4niM9mqEyhCAte0Kc2qkvL9TlKDT7WPzuvnpCvWiQp1QHkI5UcAR28XSpgUQ_Y9vE9eikpzwffxYNzmhJNvbvCJdFJE_sh2DEEBE1SRgijsROZ-yqoBpmoVv56qy_EuJZ5M8Qf1RKb7qB9E6ZmCJdSpZ_yS16egLABsvw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0f80bffe56.mp4?token=lTTj4b5pzba0vXwNOobCxdRQj10Gk1OfdPbxlMMCgPWdbwByespv7S1K1j7Rr4AMq6SxYf3rxBxbbJxJWJ2xrkNDQnRzDIqk4k6QPzzJgDKz0L8XsAw__Pr5FFTAISLJrz3siE_rGLp4HnoJgBhHpQzlRV5xKk8j8zx2Xmoe0SrESV_6C4niM9mqEyhCAte0Kc2qkvL9TlKDT7WPzuvnpCvWiQp1QHkI5UcAR28XSpgUQ_Y9vE9eikpzwffxYNzmhJNvbvCJdFJE_sh2DEEBE1SRgijsROZ-yqoBpmoVv56qy_EuJZ5M8Qf1RKb7qB9E6ZmCJdSpZ_yS16egLABsvw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👍
استادیومی که تاجیکستان در کمتر از دو سال ساخته؛ امام‌علی رحمان چه رئیس جمهور شاهکاری براش این کشور آریایی و متمدن هست واقعا
❤️
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/Futball180TV/105185" target="_blank">📅 18:22 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105184">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/O-dHGPTnZDSmh4h8vFIrfcIqxiN_72p1DJqtU2qLe9k-sTuyr0BQjVCzn2U7x5RAcuv2-vDYJarlgxKajlidiH6VQR_b_aT-mkfVIdiTs3juW1lLgFFV_I9ILpACkNEuH0eOf7HXI_DIgQBidYZM1Ar4AVJfhZNaLsqAcAza1QNHGb52OujByPJxZYEA2feI99Mc0L9gZjYC9YGmf8V-_DTztlXodeFLDDypn2W7iQIJ23bXGzpjNHRDfw8d0JxhzmWF1iednBcwn3MzoDWENJ-_jxD2PgTZ02exmjQZly9-hZ_Ue1WjfVnDZlq4z1LdsDDAAaIL6qn8Lw-y2oKebA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
🗞
رومانو: بارسلونا هرگز از تلاش برای جذب آلوارز دست برنمیداره. اگر در ژانویه موفق به جذبش نشن، در تابستان ۲۰۲۷ تمام تلاششون رو انجام میدن
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/Futball180TV/105184" target="_blank">📅 18:08 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105183">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/Futball180TV/105183" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
http://TrexBet.com</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/Futball180TV/105183" target="_blank">📅 18:08 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105182">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/putqCnGYOnltcKMuK1Yy0m-P5y4XZKvj0kEboTtM4FJw09VZkQeDie0fMVlKBiZab6n97NKRSPNerieNx3k2kVmHIWbTNzuGfgspCbTugJJcPgpFUhBfzwez5K2iXdGR55ttU7hqthhJDf8XWI3PBSGmmaiCLPyFT6_8OBlsWPsZsHYA7fyoM8OZRjk_TepkoT0YEMQkFTLJZliwJeC1qcUfBUuWLwS_hxcHevqc4XlIbJ2eRtdqppGbTxaOXzMZ8r-knqhK5o9eTDrN71t7xgb7AsLNEbGDYiCKTvLtVbhChq4__dDhdF5YBhjfMpeVLIgxV6KHApOxnBimL-Y92g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🦖
میکس پیشنهادی ضریب
〰️
برای بچه‌های
TrexBet
🦖
Code TrexBet:
SKCU6
آموزش استفاده از کد شرط در سایت بین المللی تیرکس بت</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/Futball180TV/105182" target="_blank">📅 18:08 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105181">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/njndECYtzTQZYKJniJPYVzVsTtRNvQUIr6dzuz4SDR0Vhwg0UY-V8MBn3AX8hLAm9gq94wYRquBTsL6GAv0I4seYL-cgZspzleHCRW7vb8CTrNRu0lULTTGq3TL-2tdD7BGTuZISjsBdOyq0X9H5ZSK3yW_E_DCqR253PNjOWvUEs3tXHov6gzawMzcukBvmBTiPIz_agIP-vLhte0voGzE8c-AlOHM4TfPqy8MlSESF9QnPi0-7hddltM8Iwda6_t5g3GTfX4H1WJNlJxfKh5h1NJFyB32zVvj-Db8EG1e0XiLE5xwwf2jJwChrLdHLtLkA1Cc12URKg7U-7dQ1hA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👀
🏴󠁧󠁢󠁥󠁮󠁧󠁿
🇸🇦
وضعیت خوب نیوکاسل پس از جذب یایسله سرمربی الاهلی عربستان؛ در مقابل الاهلی حسابی فصل رو به ریدمان شروع کرده!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/Futball180TV/105181" target="_blank">📅 17:55 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105180">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">⭕️
⭕️
با توجه به نزدیکی به دربی پایتخت و بازدهی فوق‌العاده تبلیغات تا پایان هفته، اگر تمایل به همکاری و انجام تبلیغات مدنظر خود داشته باشید، با ×
تخفیف ویژه
× در مجموعه تبلیغاتی تیوا با بیش از ۱۵ کانال مختلف ورزشی و غیر ورزشی در خدمت شما عزیزان هستیم
برای هماهنگی و‌ کسب اطلاعات بیشتر به آیدی زیر پیام دهید. سپاسگزاریم
❤️
@Tiivaadss</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/Futball180TV/105180" target="_blank">📅 17:54 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105179">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WX0cWu7I3IZ3fba9rrslARGu6PxefiHkjLVkEQ5tenQ0WgtJtBy3QbV8l6WA0tgdxS-TiuxK50cTaduK2vO8Hi2F_JWkuqTrBrIgRmt2WsNlKTl2K8iWyWC4NuHPANHGfDvg0Ntz3ZZvBseQGjrB_M3UajqxkdbEVTXeI2dshBSoubYf69V-CvJvUrJlCI682ifYINwwGYaZA8SjI8IY9_hUClL3RfASRTCt6Lsd9XZVG26vEfUQ7KCKkgN2IqjP2mKIC9Ge7KqLxbJunQjSJhUISqMmVpPfpTBqgz-GGh0Wk48oLlbjfZNrF-W4QndzS_9TBHSyAx7tpk6QDC3a_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🔵
🗞
#فوووووری رومانو: کریم‌بنزما از الهلال عربستان جدا شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/Futball180TV/105179" target="_blank">📅 17:43 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105177">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/i3HyjmhrIFbb2rSVUBPBdPMo-YAkFWrgBM-RyXGSxVetlEDjCs4Qt7uIdZ3627SWD4WRnQpaBQK-9UEr-pv6j5oa4SzLuLVG2_Ftd1bF5I6gsfK9v9zp2nTDtVbKiirhuP44EvtemFQ1qPP1UKDn5Jl7IP4xhT5KOdMZC0L__P4_qcDzmcpG5XtSK6VYgd4GaRfZh7lKh-XRMuFa91491feByPPAM-kDr8xweIdxa5niRA6KlCDjGTh-jkRCflcQ1oYnNVQpOFfZP0yxdJLE0HdAC0vZ8zt37xAbEOQMBP4wyclfczpzsXNiJLh-WA4cE1ZDVtkNbaThKllxQVSMLg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Tr8Drs26KlXc0y4cxf0qp-7vdVAg07SLG1CHcR1lsRaXYHhCuVAvlHzrzjVV_k6fjbpc7L_cs1leLfAiiUFLGR-rGoI6TUcTWbW8iI8U0y1a_HLVV8bhR6BnV9HXFcMUX2C8Rklvoq38kc4ffCgaPJvORi_gole_ou6CBXhEbdxX-cKB2MBwn6BDKOA4c1flyhsB8Sf4bYP8UCna52hM_XBluJ6XWGg95XeOr7YDCFo0TPbWNr9Acq7xX1nKoieZQUQqtNxWTkjJ4VdokgkEgj3D-l70hF4gP6v_mgBHxC9kJlv3u0sZan9_nqW0zaGIaKZKXCXym3gFZ63E4PYwEA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👀
🇪🇺
اوا موراتی، مجری ایتالیایی چمپیونزلیگ
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/Futball180TV/105177" target="_blank">📅 17:20 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105176">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">🚨
🚨
🚨
🚨
🚑
🇮🇷
#فوووووری؛ ابوالفضل جلالی بدلیل مصدومیت از ناحیه کشاله‌ران دو دیدار آینده پرسپولیس مقابل تراکتور و ملوان رو از دست داده و وضعیت نامشخصی برای دربی داره. پزشکان حداقل ۱۴ روز استراحت رو برای این بازیکن در نظر گرفتن
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/Futball180TV/105176" target="_blank">📅 17:14 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105175">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">🚨
🇮🇷
🇮🇷
بلیت‌فروشی دربی پایتخت تا ساعاتی دیگر از طریق سایت فعال خواهد شد. ظرفیت این مسابقه به شکل برابر تقسیم شده است. ۲۹ هزار بلیت برای آقایان و ۶ هزار بلیت برای بانوان به فروش خواهد رسید
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/Futball180TV/105175" target="_blank">📅 16:53 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105174">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/15501a2dd1.mp4?token=TQj_SrbLYtpGoI0XqF2Y2WMfS4Zep14mO6nBtGSkVREmJ4dKOHZmIb2UbDrRuY1gPgqJp1DvoAMWp0ciH4E1bhd1yt74D9awB5KmYftoeimMoFioc6TilCMbbkYvvCiTzbdLnuXx-u8oErUJOVg37jMbkbqc4rmTcPTw_npjwjN87hs3TliAzf_1cuB7_AUhcdiAX7c8W0GTgTFEaUsOkhOv9XzEofkweZXqKruypYV_sWBxLpm_KvTadwgZ7_rzCgtBRuxMU9Pl0kYIiPxyrpz66DZDCKrF8KiOj837ci4i9OSVcP3HhLZeOXk60om7jH0iQM9WQrwWC70Cige-EA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/15501a2dd1.mp4?token=TQj_SrbLYtpGoI0XqF2Y2WMfS4Zep14mO6nBtGSkVREmJ4dKOHZmIb2UbDrRuY1gPgqJp1DvoAMWp0ciH4E1bhd1yt74D9awB5KmYftoeimMoFioc6TilCMbbkYvvCiTzbdLnuXx-u8oErUJOVg37jMbkbqc4rmTcPTw_npjwjN87hs3TliAzf_1cuB7_AUhcdiAX7c8W0GTgTFEaUsOkhOv9XzEofkweZXqKruypYV_sWBxLpm_KvTadwgZ7_rzCgtBRuxMU9Pl0kYIiPxyrpz66DZDCKrF8KiOj837ci4i9OSVcP3HhLZeOXk60om7jH0iQM9WQrwWC70Cige-EA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
🇮🇷
وقتی صحبت‌از دربی میشه؛ خاطره ورزشگاه آزادی با جمعیت ۱۰۰ هزار نفری و صدای عادل فردوسی‌پور زنده میشه؛ چه دورانی بود واقعا!
💔
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/Futball180TV/105174" target="_blank">📅 16:33 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105173">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">▶️
🤯
برخی از سوپرگل‌های چیپ از راه‌دور ببینیم؛ حقیقتا گل توتی به اینتر یه چیز دیگه‌بود!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/Futball180TV/105173" target="_blank">📅 16:05 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105172">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PHi52h-XHZKBcHhgc9DB127_zdldo3gAQLN8YYQ-x25Kz-dpOvuSFLK15W9bv4RhQcuEKAS7VVPGJJKZ9YdyCGOiemhYi6_hrWIQGZcOvtybNasj1wDK8_eztQdCvp99FmJrOmJ5Pazxkzs4vfil6pB9ezFazTb1lBQfoa0FxwscQ7N2Gb8t9bKynf0gLwjZdV7u8cVC68W7nRCUXe-J-j8Hk-j79F1s5bzYkXcQmZVXKQ99Gg4CLZ85OtHj6KJKDc3NbhBOEX7XgpHxmudPYsOuHim0UKQmalNljMk1QsqjnfsPpMW9QOEq4gAaIYRQdRFYv0VdFc1u9PCx5O0UaA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
🇵🇹
عملکرد اسطوره رونالدو‌ در ۲۵ سال حضورش در لیگ‌های مختلف فوتبال اروپا و آسیا!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/Futball180TV/105172" target="_blank">📅 15:40 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105171">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Zsw73-iSqcb2H2-pB34wgGBtpNjrJpp3KJDeJUWLnCnzGvUSGmQdvEZI9ri70o0mbgRhHM7zNAuGI4SUtkv-m185SJf8jadq1bpHXa7xXR8kehQ-NCK0BVM5rugBFbDqSDiHUhVyZZyZQJp63iUV7-Ry8piUWC1cFqSd8qLL-0KDIQUARuKfJ6iDjM6AoC3KZKIt2snYA55t2edPyOy1AUZiJ5H3n1hHyTCVsqH7BpwOBxrf-OTBvJYvVeocLfRNcUHn0ypFOCeqHDMvwXPBH83Ryu-4tfUwM2NXjqU0FzMaQx1mBa7HK2S6Gjo3RzL1Jzwd08e4mFSA179VsFW00w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
😢
⚠️
دختره ول‌کن رامین‌رضاییان نیست و یه ویدیو پر کرده حسابی ریده به سرتاپای اسطوره اخلاق و مردم‌دار نسل فوتبال فوتبال ایران
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/Futball180TV/105171" target="_blank">📅 15:16 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105170">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/q8Lm7-bN1KioqnL9sZxpgZRN7KIOPr6aLAw9iV3MSowjKM_JvlzuEK5hJ6aFopUlA_xRQFEgc2VNo7QErWcHCrOOT0R0qs3YpVMHeFdNC07nl0JWFs7ex2Rhh46Nz_MRsoebDOzO662yCJjcQCnkUOhOA89uJZIK1EmxVcNDz5lHFIx1JEoXjhHmf4g-NAOt-LTY7Rc7MuyUTuo2csn7lv6_3wbyZTAJVzES_ZEjfnEakMGN8Z9dlpZ0loNcE_lfFhtwzEMx0cr6GiMoDckDWhL78JD2tVrz6EPSAayuu3WrBSWYOSPPZlcPnM8aQ-rhmDUM_RUxlOjBGj3h2Hf0kQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
😱
❤️
💵
با رسیدن قیمت دلار به 210 هزار تومن ارزش حقوق یک نیروی ساده در ایران به
75 دلار
رسید. حقوقی که
یک ماه
باید با اون زندگی کنه! معادل یک
دیسک بازی کنسول
که در کشور های دیگر کودکان با پول تو جیبی می‌خرند!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/Futball180TV/105170" target="_blank">📅 15:10 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105169">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Kkc5EdFjr8zOvf-RwI3MR6rLUTTFEROxXxWFte-w0eZJDc0pUMIYrEz4igmao7h-ErLHbds88lAGw-MAYY2I7axGtOuEi12ANxRZ27ANmjpFeMnDUH85tAaMjFPWtwsevkbXmwEYs1fkdIn6rceZVTRsUmfVzXUqmF2vCA9cv_m_3O0fOwFZqA8XKv2oBdodl9b2e2N7gA_H3KzHMrl2IdwmddysJgDupEp8HdPtM1KmKCck2wbA8dd0w3X84lGmaBgcPNBh_KTY65OGRharjYeekm07FBeqftaZNQNcpjU-iCLiLVhE42fpGTWCo4vNLWFwOVhwPO_8DJ-HvkZPfQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
لیست بارسا برای بازی امشب مقابل رایووایکانو
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/Futball180TV/105169" target="_blank">📅 15:07 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105168">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/32a916d757.mp4?token=lpYKwzvQhFrDN1WtNiugndhiqdiOsWQkCumwiWJ_ozHQrUP2-4dznGxKPN_SFLMEVudP89PlbyaniARGET96gvqlIq2TBk98JrOf8mnEkiXe00MW2jWMDtdz4hQ084GGaJbyP4YQYHmf1oCjeh9A-f8YhVt6ncI4HEcSe0F7w4GurTbzwqknzWKSKOzx4F-w0T8nYChLANKogh2Df-fPWYTvi85mvmMeFn27jt6viyLVWDZq9sgq_9UcIEzHAKpET1QL_u6D6dJRDTmVF0j4rdaDV_pMd5XuKlaTO5wZr1I5W2M2N4zp754-wIPwJ04NXljNczC97_8vldpYmByyaA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/32a916d757.mp4?token=lpYKwzvQhFrDN1WtNiugndhiqdiOsWQkCumwiWJ_ozHQrUP2-4dznGxKPN_SFLMEVudP89PlbyaniARGET96gvqlIq2TBk98JrOf8mnEkiXe00MW2jWMDtdz4hQ084GGaJbyP4YQYHmf1oCjeh9A-f8YhVt6ncI4HEcSe0F7w4GurTbzwqknzWKSKOzx4F-w0T8nYChLANKogh2Df-fPWYTvi85mvmMeFn27jt6viyLVWDZq9sgq_9UcIEzHAKpET1QL_u6D6dJRDTmVF0j4rdaDV_pMd5XuKlaTO5wZr1I5W2M2N4zp754-wIPwJ04NXljNczC97_8vldpYmByyaA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
یکی دو سال پیش این ویدیو از نامجو رو دیدم که میخواد کوکو رو تو ماهیتابه برگردونه، شما اگه این ویدیو رو میدیدی از هیچ کار این ادم تعجب نمیکردی دیگه حالا فکر کنید همین آدم بعد کلی فوش دادن به جمهوری اسلامی دوباره برگشته مملکت تازه ازش استقبال کردن
😂
😐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/Futball180TV/105168" target="_blank">📅 14:50 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105167">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8fea9db172.mp4?token=uwI42SAl6qiooHXfefgieoE4DP0LjI0_NCAW2i27B4mQCK7ExleRGa7_V__4_LLzMkSb5_MH_XlYwdai7bUXofH3v6M7Npe6KWGeoIvi8M1a6KlodcZt-3Ev6-kpKQ9qEe_f4Y6hbJ4Y-PQW-S-EI63RqEQxw8C4dPQFW84Ooct6tmwsTIh4qunDz-KIdCkq8oS2gBd_yq4Wti0Ec1cXnOSgCpYXurzGkXjx8h12MrF5JZjvwZOowXackagSQfWc5_WW4ElX2wnwT9JIomvXcEdLbN8VzuQZRsXcheycd31JbwyzpgSIxsFeff6zLirGl3DGfnPwVtpMZZ0iAdcI4w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8fea9db172.mp4?token=uwI42SAl6qiooHXfefgieoE4DP0LjI0_NCAW2i27B4mQCK7ExleRGa7_V__4_LLzMkSb5_MH_XlYwdai7bUXofH3v6M7Npe6KWGeoIvi8M1a6KlodcZt-3Ev6-kpKQ9qEe_f4Y6hbJ4Y-PQW-S-EI63RqEQxw8C4dPQFW84Ooct6tmwsTIh4qunDz-KIdCkq8oS2gBd_yq4Wti0Ec1cXnOSgCpYXurzGkXjx8h12MrF5JZjvwZOowXackagSQfWc5_WW4ElX2wnwT9JIomvXcEdLbN8VzuQZRsXcheycd31JbwyzpgSIxsFeff6zLirGl3DGfnPwVtpMZZ0iAdcI4w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">💥
🇮🇷
🇮🇷
هواداران خانم خوزستانی در بازی اخیر
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/Futball180TV/105167" target="_blank">📅 14:25 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105166">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d9c2e01cdc.mp4?token=W43PZXP6EcjH5wOZKS1f9xZEHVcvh6zlwq5tC3Y7ImZQtBnDNsRbpra1lRHDqAcF4gfWAbVE7WLQX2Ypa2Lzw3WNvoJG215agNIWwRDPBsFlFK4SEyihe9KFxnugX69mexDrJlUNAJnGRDC1_SJSv-SgBYYxe9SAza2WJcYegpcUePozJz3xrVBaV9gmZ7pJ-SF0X-38q10KgeMO5EZ7Lf4rmlzlINANypx2VixGMlxRt5Q7vU1m5tZQ1GWpuI8g2gq_0lc9OI9r9uFn8say6b_p69DWCNXEqfU0XZhNw53Rw-AbCevtt1-6SrR82FYLSSqPEir922XvmJ6sxkCkvQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d9c2e01cdc.mp4?token=W43PZXP6EcjH5wOZKS1f9xZEHVcvh6zlwq5tC3Y7ImZQtBnDNsRbpra1lRHDqAcF4gfWAbVE7WLQX2Ypa2Lzw3WNvoJG215agNIWwRDPBsFlFK4SEyihe9KFxnugX69mexDrJlUNAJnGRDC1_SJSv-SgBYYxe9SAza2WJcYegpcUePozJz3xrVBaV9gmZ7pJ-SF0X-38q10KgeMO5EZ7Lf4rmlzlINANypx2VixGMlxRt5Q7vU1m5tZQ1GWpuI8g2gq_0lc9OI9r9uFn8say6b_p69DWCNXEqfU0XZhNw53Rw-AbCevtt1-6SrR82FYLSSqPEir922XvmJ6sxkCkvQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تنها‌ ایرانی که میتونیم بگیم خوشبخت شده همین همسر جان‌سینا بزرگوار هست. چه عشق و حالی میکنه ناموسا
😢
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/Futball180TV/105166" target="_blank">📅 14:02 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105165">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b552c4303b.mp4?token=bfKEbaB6IJYqX74U07lrHBIFnGOV2faCLEr3oruzX2-63sclvgAWrkMclKJsGsFy8JDoRz4YKYxIuZx66BB7Li6scBfyzBKF3fqsTYymRHqFUAinzaPMUK2gAGxYFowEO1Tswuk9_AO3nvV2r5_fqPdzxiorckpsFsF__YpZ9oZhhZu6cBOQ9wL0l0n1F11uCbu0l-ZRATGQHNmvCA2aTbYVq_sPkqmM2bMS1EsA8BmA8OUPSwh78GvFse7J5H08mkEAOccB8lb2oV69re6fIW_OehtddRPFcqAEc5s8Zm4StnhB9s9mPa5J-g0w-66olCBccB4xZ2YckUBATE7Ea5iBFA_R2rFhePKNhWZHnkiWqLDXLlWVgx3fWh8bBHHeEvYcZZbqa2KMdF3XdfJRi9IibYyf6UbUsxOkjfU8kRTQxLMxcQxiqL8MqyytxpiYqDMt7zpvT_kuVqQ8ZAZVF_840JqvmkwAp0dfTb2uIrqsPid9udmXe5I7Wv3j9R1VERjS8MzeXtTsdcClierVQ1YZy0g7wBfPwLq6P3E97fV0XZO5def3rdD13IB8gGCMi3a5Zd-PVfkZRoyz_mOHFucL6NHWEc-ptY7LX7MIc-aRyqpY5MoyznGhAddSP1p8L2Pn4C79x-4fKwf7SdhmQL_yRvPQQDlOUyNcHYlqJok" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b552c4303b.mp4?token=bfKEbaB6IJYqX74U07lrHBIFnGOV2faCLEr3oruzX2-63sclvgAWrkMclKJsGsFy8JDoRz4YKYxIuZx66BB7Li6scBfyzBKF3fqsTYymRHqFUAinzaPMUK2gAGxYFowEO1Tswuk9_AO3nvV2r5_fqPdzxiorckpsFsF__YpZ9oZhhZu6cBOQ9wL0l0n1F11uCbu0l-ZRATGQHNmvCA2aTbYVq_sPkqmM2bMS1EsA8BmA8OUPSwh78GvFse7J5H08mkEAOccB8lb2oV69re6fIW_OehtddRPFcqAEc5s8Zm4StnhB9s9mPa5J-g0w-66olCBccB4xZ2YckUBATE7Ea5iBFA_R2rFhePKNhWZHnkiWqLDXLlWVgx3fWh8bBHHeEvYcZZbqa2KMdF3XdfJRi9IibYyf6UbUsxOkjfU8kRTQxLMxcQxiqL8MqyytxpiYqDMt7zpvT_kuVqQ8ZAZVF_840JqvmkwAp0dfTb2uIrqsPid9udmXe5I7Wv3j9R1VERjS8MzeXtTsdcClierVQ1YZy0g7wBfPwLq6P3E97fV0XZO5def3rdD13IB8gGCMi3a5Zd-PVfkZRoyz_mOHFucL6NHWEc-ptY7LX7MIc-aRyqpY5MoyznGhAddSP1p8L2Pn4C79x-4fKwf7SdhmQL_yRvPQQDlOUyNcHYlqJok" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خاطره فوتبالی هلیا امامی از شبِ‌معجز‌ه‌بارسلونا در نیوکمپ: پاریسن ژرمن که گل ششم رو خورد، دور و بریام در ورزشگاه غش کردند! جو فوق العاده‌ای بود.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/Futball180TV/105165" target="_blank">📅 13:35 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105164">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">🚨
✅
🇮🇷
🇮🇷
موعود بنیادی‌فر شانس دوم قضاوت در دربی روز چهارشنبه معرفی شده و‌ قرار است ظرف ۲۴ ساعت آینده تیم‌داوری بازی حساس استقلال و پرسپولیس مشخص شود. همچنان کوپال‌ناظمی بیشترین شانس را دارد و کمیته داوران تقریبا روی این گزینه به جمع‌بندی رسیده مگراینکه امروز…</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/Futball180TV/105164" target="_blank">📅 13:31 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105163">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/38c6e037e9.mp4?token=dEF_AN_erhwAQVC3Z3SovZS-1T4uA_sP9bD9OmDrvXdvVAmxUczL8TTwZV7uj41_uflrdhS-XnaoqWv1lEO_tiUniEO9Nl0VHJ8vfDCTlVa0TUlS6LFTlvQQfVl61WrsAbjvfK4zfFN-NAOHFAQv47aOD74bM6DRhIH9kEkY_qQcb1atYXOM1B6SMkEjkTgSJzUGGKo8EV_J3zBBIy0JD0qqm-LRGf9alI4cc97sUVwOS7Q7U4LRxhYy-xI1iPJ80ur1Aavnzap6Tbd13Gesq6A6Owb2ism4Djj_WqGIaBhdnpzKwSeD-b4L7rDomAlOQG_Ut98FCx8W9Snh8d0r1rg55N1jsE88G8ZfHASJjlgwdReyo57WqFqbXAzdX9DHR0qCTvfeH6r2IEakLKbH_ojJ_jKcIZCtdeE4sU0icHqkneAsC2TQQvwl21nXMs9N7I9v1nnUYc7_j-uY4V2fqyiCDwooHUUBio5DJafdFmzj6zSXYNXq0ZnptCB3ijlawgZNKQD_Kox407W26KfXXdzY9X_rxXfsFhK4d1lwO74bU4awABCa1kRRUFQtBu45a6viB_JYTvSTECvcbWIqM7QM6cZ7AqOcJz9fGEQaID6XnU_1IlDZI6J0QJfzfnwQjjlIUtXP2nCgxs2z_ie5mFulR44_Fmjw013OlRF1_Ng" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/38c6e037e9.mp4?token=dEF_AN_erhwAQVC3Z3SovZS-1T4uA_sP9bD9OmDrvXdvVAmxUczL8TTwZV7uj41_uflrdhS-XnaoqWv1lEO_tiUniEO9Nl0VHJ8vfDCTlVa0TUlS6LFTlvQQfVl61WrsAbjvfK4zfFN-NAOHFAQv47aOD74bM6DRhIH9kEkY_qQcb1atYXOM1B6SMkEjkTgSJzUGGKo8EV_J3zBBIy0JD0qqm-LRGf9alI4cc97sUVwOS7Q7U4LRxhYy-xI1iPJ80ur1Aavnzap6Tbd13Gesq6A6Owb2ism4Djj_WqGIaBhdnpzKwSeD-b4L7rDomAlOQG_Ut98FCx8W9Snh8d0r1rg55N1jsE88G8ZfHASJjlgwdReyo57WqFqbXAzdX9DHR0qCTvfeH6r2IEakLKbH_ojJ_jKcIZCtdeE4sU0icHqkneAsC2TQQvwl21nXMs9N7I9v1nnUYc7_j-uY4V2fqyiCDwooHUUBio5DJafdFmzj6zSXYNXq0ZnptCB3ijlawgZNKQD_Kox407W26KfXXdzY9X_rxXfsFhK4d1lwO74bU4awABCa1kRRUFQtBu45a6viB_JYTvSTECvcbWIqM7QM6cZ7AqOcJz9fGEQaID6XnU_1IlDZI6J0QJfzfnwQjjlIUtXP2nCgxs2z_ie5mFulR44_Fmjw013OlRF1_Ng" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🗓
‼️
⚠️
محسن نامجو، مرداد نود و هشت:
کوروش ایرانی نبود. حافظ ایرانی نبود. ایران یه مفهوم جدیده مال صد سال قبله. گذشته‌گراها شاملو رو نمی‌شناسن عاشق فردوسی‌ان، می‌گن به فردوسی دست نزن. می‌گن گذشته‌مون بزرگه. گذشته ما کجاش بزرگه؟ یه شهر مثل پراگ داریم؟ ریشه‌ای وجود نداره. ما چیزی از خودمون نداریم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/Futball180TV/105163" target="_blank">📅 13:10 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105162">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cabb21609a.mp4?token=Y7yqdIqq2i-XCPaJq3zDbIzWnG0X2eaM9_Twjek0hQm-1j9HtmLS9FmfGdg6-6tWat10gdrTeufB1sOtwF42jvDSidCboGiw53eKsKG7MOWVgobJ4-GPNfJ4RMJim3o6dYdauqiu2nt3Gt548Zzkyt5OZgjyLSBeR5NicDsZ9crbDpiy8JPtu4C_tQYrXPBSNotZ5o_sm_M-IElxyIRJHwyzMo7WRkzCD4eT5VrP0-VR64_10ccqgDtPNEa4ugqGs217Gys2KrrLBf6OQWUz8Cn73amuGLvcBu3JTlK_HP5uCYJJIgB8jsXQODfjyCRHEFmDz98ukCVbTHo_H_NUYg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cabb21609a.mp4?token=Y7yqdIqq2i-XCPaJq3zDbIzWnG0X2eaM9_Twjek0hQm-1j9HtmLS9FmfGdg6-6tWat10gdrTeufB1sOtwF42jvDSidCboGiw53eKsKG7MOWVgobJ4-GPNfJ4RMJim3o6dYdauqiu2nt3Gt548Zzkyt5OZgjyLSBeR5NicDsZ9crbDpiy8JPtu4C_tQYrXPBSNotZ5o_sm_M-IElxyIRJHwyzMo7WRkzCD4eT5VrP0-VR64_10ccqgDtPNEa4ugqGs217Gys2KrrLBf6OQWUz8Cn73amuGLvcBu3JTlK_HP5uCYJJIgB8jsXQODfjyCRHEFmDz98ukCVbTHo_H_NUYg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🎙
⚠️
رحمان و رحیم سریال پایتخت: یه بار کار از دستمون در رفت جفتمون عاشق یه دختر شدیم!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/Futball180TV/105162" target="_blank">📅 12:45 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105161">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BvZOxPSdI-b9oHK8Lu9r2jL2lBsGJstABh-1ilYEaB6q9jL4bnZkK-W4yZycitOU01d8QWK5CI5wyQI40KEUIJRaK1DTF6f3lif3FQDDXWW2vZKrEjtn7puGltSXtXlWrnyXi2u-8BRdm8x4AXPjW2cEAX0jo9nlrwyFK-q3LDr1jAOyP4D0IICC27knFyaVf3ouns3OWQEup11qNr1RYASE8OKPYDZe3fcW3xFw0hvN30BoTclU-aP_nZCgz_I75NEUQ5ZXycCDzsR_SL509Y64E5Hw4VWSq04RUSSNmMmWl96IxngxdTB91yVe7mQGrBYsApnwjg1mtxnyTn6LeQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
🗞
رومانو: میکاییل بازا مدافع ۱۹ ساله هامبورگ با عقد قراردادی به بارسلونا پیوست
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/Futball180TV/105161" target="_blank">📅 12:41 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105160">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pWrC4-028w7Xbe9LNTIcp-bHChZ0dH4QxUqfwPuJaVPrQA__7JfYmCpGlmVfAnuUTlX2W7yRs0Qae2fFxa1Uw_iHs52TR9z9SZNHfxxelmdwmTGj9uau7KX1cEHENwiOK7OBwZ_zNZSOzs7J0Ai7uWiI-Uy0mGZr3nV6MH0R1-b6hsslYUE9YhoHXNQh7sT_ErU2qGrUpGQiUE_hxSVDJF2uwlHVgcdmLo1FQ7hTkVoRat55LLHvR7YOGqXAciPDQ01B34sBBy8Zl0SScVK01pO4-K_40YmhsnwGm8JZLPDBsCoW3qI1ibfYhfx_pu7FO7mHNde6OA0DZow1pVZ5Ng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
👀
🏴󠁧󠁢󠁥󠁮󠁧󠁿
جونیور بازیکن ۲۰ ساله برایتون بعد اینکه دیروز مقابل چلسی بازی کرد و بخاطر چهره‌اش و کچلی در این‌ سن و سال مورد حمله قرار گرفته بود، یه عکس از کودکی خودش منتشر کرد تا به شایعات پایان بده!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/Futball180TV/105160" target="_blank">📅 12:26 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105158">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/GuFk9PaSzvZAZ-foelmXYw37t9_PulHkHAJPFK_loKvnYwpDP5NiZo03P_EBZ1AOcRUH1oOGGj58_hUlckYfvawbxbffrX84qeJ80-EeQWD1qHoVvlKAsCEZMLRkcD1fHSRpoeGpFdvNsESHQN19zdWTd7mrb0EKmRF0UYJooWfRvDAYqfca1NbLTuwFiT7dZVmNYH1xmcbxyV2O5U8TefGXtUu5eQW623CaDIAsDu6Nb7q22OkZMbP7rvCc4obUrRJ4i7RU4YisSZpYXS6BJOW3XQ6qdWr5Pdxxp_n_Lr6sDGkCWqqsjnRJtDDMFzRqrDeNv2gfHBFFG7PfrlhJyQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/rGK1Aq5R0281gHIV0e5GsDZDp7wP_cyYkiruLg2J6yVTo8R1xjikcPla-Uw4UAilUXvgPrOWxYnnIEHLsFXDL230HuqQw29JXYJoQs5VdyZqbo8nVCjXNWLAx7Xm9skDRvXW7cECYdnEEzTFbNA4tucYZ1BKC9zVZ0QP6HztspJYrdwQl3VoNflK_0q_LjutKbhFu2yneU7GQnQfy3-7_rne2GclZrc7Mw5tudufGHzE25-muIK8y6OmLi069cXhqLUcC-46xeG2Illd7auuLNINvY1qtXoIwTnRp-87bBqUUhszCqpZaW4LrFzFKLJQ7bE2gQ2yja-BTMzPpx_VZA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👀
🇮🇷
مریم‌یکتایی گلر جدید تیم‌بانوان استقلال
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/Futball180TV/105158" target="_blank">📅 12:12 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105157">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">‼️
⚠️
درگیری فوق‌کیری و خشن در لیگ‌چهار برزیل؛ پشمام ببینین چجوری همو میزنن
😐
😐
😳
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/Futball180TV/105157" target="_blank">📅 12:02 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105156">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/Futball180TV/105156" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/Futball180TV/105156" target="_blank">📅 12:02 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105155">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UQNI4jHajHdB5CFZ1mjC8p7aardSj5oJGQ8NxjFRkeDVvgzO5l5meMieMGZEDq1q3uhRXFwGrAwv46CouQUo3sawOLux246xRfd2D1AoWgx8iLfhf3fIsBdgJldRc5b9HoXX5GY05KnfjFbIDibk8bTGmtNU8bECsGw6_wiEPuzDkOdqIWCiCU5SSPJiJZti51f_inBBaU9zu-o0CTOTb_7SXVzB-yPPguE_C5AstRVofCt-2XsDz5Q6KsDsg_rIJOKgHM9e-QDsLM3dL0i0gRkFA7tyZQeqB5OBCaKbEU9U28letPyKK2kLatrehZHwJ_bOC0U5z2byjKXTIb179w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🦖
مچ‌های مهم امروز در سایت بین‌المللی
TrexBet
آرسنال
🆚
استون ویلا
رایو وایکانو
🆚
لیدز یونایتد
رم
🆚
لچه
بولونیا
🆚
آتالانتا
ختافه
🆚
اوساسونا
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
TREXBET — PLAY. PREDICT. WIN.
https://TrexBet.com
T.me/TrexBet_Ir</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/Futball180TV/105155" target="_blank">📅 12:02 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105154">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6b53bca956.mp4?token=EXQcP-LTRc5I_i7Z7C5Liy4YUpd-UKbbx1Rjmo6I_pVRcUKle_xcUJJn-OdjnFsdBnthcoiczaNbOXNCOuaFLAO1OV1blvVOp4co-3flw8l5d7i6W7SiOA3FuAzgsjNvNy_hAj8gvh36Q_djsIH6Nb7Tyhr4awhtcVO-TbsaJpEei6IQiNKZ7kQdWylr9-BZZtKx38cEa1spTWuG57IPWZsfkDjjwMAqb9GagS2jBu4C0mh-0s9HEWImXIiEHu-hK1MjJR-8RYoUmvpN6RssvvA34MmrZoAv5ibToynj8AoGBCW8G1-atusZybWvpKj38lYyM1N3oq_w24e-s6-zPadWa9OUYIOxCenwqeJSdeIhZaNt4gQoH2M4T1Hmkv8ID2HhdG5i-O7sodGQfyEBgFkwlSkxxnviBlSq4ervnxZGafpZmTC9M65s5j__EbXuuSGj20o3qUJevsFRFnmBbnW2XlvS0u8gAaqxMIVFp5wK4ms0WUE1R9_Wh6mKW0T_UrUtLtXIzYsB41zt1ay5sBq_yJRBasloj0bGJLbyYFAB5g-wINmlWMpWlU-yX4jG-ecfGHoaqJIdKCAt3qGri4Q6FcAdw31zlVkUWQGT7qmv1_pmP4y0RzJKEq3owGIgIMdaPnEkkohbw9Jmot0pCp-Btw4m_b5XsWrTjpM4z0Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6b53bca956.mp4?token=EXQcP-LTRc5I_i7Z7C5Liy4YUpd-UKbbx1Rjmo6I_pVRcUKle_xcUJJn-OdjnFsdBnthcoiczaNbOXNCOuaFLAO1OV1blvVOp4co-3flw8l5d7i6W7SiOA3FuAzgsjNvNy_hAj8gvh36Q_djsIH6Nb7Tyhr4awhtcVO-TbsaJpEei6IQiNKZ7kQdWylr9-BZZtKx38cEa1spTWuG57IPWZsfkDjjwMAqb9GagS2jBu4C0mh-0s9HEWImXIiEHu-hK1MjJR-8RYoUmvpN6RssvvA34MmrZoAv5ibToynj8AoGBCW8G1-atusZybWvpKj38lYyM1N3oq_w24e-s6-zPadWa9OUYIOxCenwqeJSdeIhZaNt4gQoH2M4T1Hmkv8ID2HhdG5i-O7sodGQfyEBgFkwlSkxxnviBlSq4ervnxZGafpZmTC9M65s5j__EbXuuSGj20o3qUJevsFRFnmBbnW2XlvS0u8gAaqxMIVFp5wK4ms0WUE1R9_Wh6mKW0T_UrUtLtXIzYsB41zt1ay5sBq_yJRBasloj0bGJLbyYFAB5g-wINmlWMpWlU-yX4jG-ecfGHoaqJIdKCAt3qGri4Q6FcAdw31zlVkUWQGT7qmv1_pmP4y0RzJKEq3owGIgIMdaPnEkkohbw9Jmot0pCp-Btw4m_b5XsWrTjpM4z0Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
🇮🇷
🇮🇷
پشت‌پرده درگیری اخیر هواداران چادرملو اردکان با شجاع خلیل‌زاده!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/Futball180TV/105154" target="_blank">📅 11:55 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105153">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">🤯
🔥
رقص‌پاهای نیمار در بازی دیشب سانتوس
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/Futball180TV/105153" target="_blank">📅 11:34 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105152">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e9ba1ea291.mp4?token=BRJ6kP1SldHP0jAjL5stsoIHmEUP6YPU64raXjJburcoBqOBaHvIAqc77QwifMKNT0qoUqtrpHmWm5_EHZQqa5bNDYmnCiiICeNRRHWSkROZYyJ0p2njqqNU4uDOYF-bDpEClhYdVCVbp5bnhSMG80qwl9fd2dTPgmCI2D35BUkRaUO6xzjoWmmEwZu03Q1p7J4lV_DeYnJdEIqPe_O-AtAmP5OcBcbBh49YfiqaW0IJ8uJaMScRKAK0snxWeL4_gdjdC6MuR0PvoGyRZGTErFYfI8FJVj5vZn2aXwi7Kw-Tz0gaKx-u08mBEBIuqwwuJ06BfBzGw5871OlEOR4VKQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e9ba1ea291.mp4?token=BRJ6kP1SldHP0jAjL5stsoIHmEUP6YPU64raXjJburcoBqOBaHvIAqc77QwifMKNT0qoUqtrpHmWm5_EHZQqa5bNDYmnCiiICeNRRHWSkROZYyJ0p2njqqNU4uDOYF-bDpEClhYdVCVbp5bnhSMG80qwl9fd2dTPgmCI2D35BUkRaUO6xzjoWmmEwZu03Q1p7J4lV_DeYnJdEIqPe_O-AtAmP5OcBcbBh49YfiqaW0IJ8uJaMScRKAK0snxWeL4_gdjdC6MuR0PvoGyRZGTErFYfI8FJVj5vZn2aXwi7Kw-Tz0gaKx-u08mBEBIuqwwuJ06BfBzGw5871OlEOR4VKQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⁉️
🇪🇸
🇪🇸
خبرنگار: سرمربی مالاگا بعد از بازی گفته که داوری تأثیری روی نتیجه بازی نداشته، اما این حس رو می‌داده که اگه بازیکنای رئال مادرید رو فوت کنیم، خطا می‌گیره؛ در حالی که بازیکنای ما باید خونریزی می‌کردن تا خطا بگیره. نظرت در مورد صحبتاش چیه؟⁣
⁣
❌
🇪🇸
ژوزه مورینیو: ارزش اظهارنظر نداره!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/Futball180TV/105152" target="_blank">📅 11:05 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105151">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gW2EPDs4IvSVMWKs_W0i3YVn7HzAaQ8UoglrDZOWiWBbQ6J4pw0-5Kt5oF6ET-t-ULr5rzsNHPX57UmQHkYXevKfFAWrOtYpo85rHxD_ORiifrRQ-s4Thaicxz-iVgsfuikStn0ByHQC_auuMx4A1r38v993VTf3EO5w27b19XuoNuQZZJIuMup5EjBe84tZUuwIoc8vvF28Njl66l_dVZJXj3ICkEDLEldhdpZUe9PDVIrHmZWrHxyiCNTLJV1wAVyW33oe5bTT-THX3oRaDQqs2GNC1yRRxMyM3T3JS6WDRk_69jOmR9yfJSCyAO6s8Ut35A6PaTZqHWuvjfYPzQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇮🇷
🇮🇷
بلیت‌فروشی دربی پایتخت تا ساعاتی دیگر از طریق سایت فعال خواهد شد. ظرفیت این مسابقه به شکل برابر تقسیم شده است. ۲۹ هزار بلیت برای آقایان و ۶ هزار بلیت برای بانوان به فروش خواهد رسید
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/Futball180TV/105151" target="_blank">📅 10:45 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105150">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IbN6lfG1tTOePanY-cyGERsiImr2dOdNCa1ZdjeaVOc1fWQCbhJhCfEhgVi2oAG6ANzfS2H3SNuGMnRVSV-LDcA63dodyR7-VfPtDo_MvZlV8Ithq7oAcFiXtYs1ZEuZyAwAMVpyHe__oE1ecfh-alwMeX2DxMXMO7FL3gF3WDsyuDtGgloUMthVThHbVbfZI6xrvs5EYj86oBDRqtv7btqPv0_o9QiWG1BrO1Hc0psmB7JpqO4n1LjPws0l8Ri-Jadxf-ojq3wiXEvADztLbaYExYAs5JYcnQSRx0RXiss7Eauz4MXUOrgNa521LMsOC8Br5GxAP4YhClqQQU2N-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
❌
⚪️
پس از اتفاقات جنجالی اخیر تورنمنت سه‌جانبه، هدایت ممبینی از دبیرکلی فدراسیون اخراج و حامد مومنی موقتا جانشین وی شد!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/Futball180TV/105150" target="_blank">📅 10:33 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105149">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">🚨
🚑
❌
🇮🇷
یک‌سایت خبری روزگذشته مدعی شده که مهدی‌ترابی در بازی با چادرملو دچار پارگی رباط صلیبی شده و فصل رو از دست داده! باید منتظر تایید یا تکذیب این خبر باشیم!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/Futball180TV/105149" target="_blank">📅 10:02 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105148">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RWQx83wWbXkKejeT8xlL4FbovubtgJ72zIboXBXlpSlgb2D-zFEPrza8GHTSiIzwTokkSgvof-ZFgsR27VqM-CfyS_4RJv91etRsWjfPWFGcdU6vmDjF2TyAgj7bBWdSTz3maI8695EyToRjJx7pX38-lu7rO6RhsIsZDPwWiusRD-IP1mpmioNmPGQNcSiYYQlpLUXaHASriv3EcnOJgC9j7I7iwPNVCnfcU2YwLobtO_JJ7Po1PslPxaKF-dBApc9K4b3IRoudctemfgLW39tP6TG1XY8zRHMPwFSZ113X9Ta4s-6Sho1DA29hMZNMJtgqR6Rc_klJkHx9eSxpig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
📊
🇮🇷
آمار فوق‌العاده تراکتور در تاریخ لیگ‌برتر؛ تنها تیمی که ۴ بازی ابتدایی با کلین‌شیت برده!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/Futball180TV/105148" target="_blank">📅 10:00 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105147">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">⚽️
🔥
یه فرصت خاص و دوست‌داشتنی برای فوتبالی‌ها!
کارت‌های حساب پس‌انداز وینگر بانک اقتصادنوین، این بار با ۴ طرح جدید و جذاب
👇
⚡️
مسی | رونالدو | امباپه | یامال
و یه خبر هیجان‌انگیزتر!
🤩
💳
این کارت‌ها تنها و تنها در نمایشگاه الکامپ امسال در دسترس شما هستن.
📅
۹ تا ۱۲ شهریور
📍
محل دائمی نمایشگاه‌های بین‌المللی تهران
🏢
سالن ۷، غرفه ۲۸ | غرفه بانک اقتصادنوین
🌐
https://enbank.ir/fa/page/101088.html</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/Futball180TV/105147" target="_blank">📅 10:00 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105146">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d7b7206c7d.mp4?token=mDZOjP0CGUB-sv4ir4Az6-acIBAnCViffNVWg_Rz5k5D2vIt2zZCgpOOF09Mr8TYVafCaGbh_DaFmZVvQPx54UGML8vC2NEDlGZf9utYB1DUwaO4lwOEClhpoRxM4aJHEN05I6jN39DgdzgU5m7If526rJyyluRP5S7Fw7ylH1A21i5IUprcGA1aurspiWuU6-UT2WosyySFTpK9NUwXLQcLvcCxXP5pXNTgREfXTyyfcC4z6V6gLAfhq25JKPQgLNcqtnqRXXTw01KHGfurc4DgL4GZMEvC5kNHYS2QPbiKA8xjb75CRuGtNf9mC1wSxfBhDSwacOe9vXLpFHX9mjzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d7b7206c7d.mp4?token=mDZOjP0CGUB-sv4ir4Az6-acIBAnCViffNVWg_Rz5k5D2vIt2zZCgpOOF09Mr8TYVafCaGbh_DaFmZVvQPx54UGML8vC2NEDlGZf9utYB1DUwaO4lwOEClhpoRxM4aJHEN05I6jN39DgdzgU5m7If526rJyyluRP5S7Fw7ylH1A21i5IUprcGA1aurspiWuU6-UT2WosyySFTpK9NUwXLQcLvcCxXP5pXNTgREfXTyyfcC4z6V6gLAfhq25JKPQgLNcqtnqRXXTw01KHGfurc4DgL4GZMEvC5kNHYS2QPbiKA8xjb75CRuGtNf9mC1wSxfBhDSwacOe9vXLpFHX9mjzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇸
حسرت ششمین قهرمانی اروپا از ۱۰ سال گذشته!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/Futball180TV/105146" target="_blank">📅 09:50 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105145">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/793fcfe694.mp4?token=CP3NH0t14htBOn7PetZGPj_7QAMNeuRz9FF4ff9yeK4c5LewLYdyou2UkFEzJncrDReA_iJH9fPXJcVLoPSe_E5-tRAYPQKyjf_hol-VQjiaqRGKy4AKJX9_ImdYV9mVjq8P63NA--lvUnNzgQIYu4tJjStLbAMgWyIXrwxKR3p2Q4wn3XQYFfYMVDdQ2qoca2Je1ApHbE-SXDOT7UQt8tWExOQuNh3N8DlU7h9-a-sPVT-2zgeiNztXoVDS3jEeIBjIgSMTwUZGaTsYur5RIzChLDsbD0i6i_eIJ4V1hkF6bG1doedP3ERVHa9990kU2joJlIKQQpCfgMEIATTtBg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/793fcfe694.mp4?token=CP3NH0t14htBOn7PetZGPj_7QAMNeuRz9FF4ff9yeK4c5LewLYdyou2UkFEzJncrDReA_iJH9fPXJcVLoPSe_E5-tRAYPQKyjf_hol-VQjiaqRGKy4AKJX9_ImdYV9mVjq8P63NA--lvUnNzgQIYu4tJjStLbAMgWyIXrwxKR3p2Q4wn3XQYFfYMVDdQ2qoca2Je1ApHbE-SXDOT7UQt8tWExOQuNh3N8DlU7h9-a-sPVT-2zgeiNztXoVDS3jEeIBjIgSMTwUZGaTsYur5RIzChLDsbD0i6i_eIJ4V1hkF6bG1doedP3ERVHa9990kU2joJlIKQQpCfgMEIATTtBg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🧊
✅
این‌ویدیو بسیار کاربردی برای دوستانی که عاشق‌ درست کردن معمای روبیک‌هستن ولی کار باهاش بلد نیستن. بفرستید واسه رفقاتون عشق کنن
😁
❤️
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/Futball180TV/105145" target="_blank">📅 09:25 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105144">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2f7e507ebd.mp4?token=OjWbEnFGLTmKLKQMm3aTCzaKUcnxdzFr2FdOe8cvTdiamh_YbSTJS0OwdED80xYV6LttQ0_QHIaiP7q3KRHzswA64Gc9XfkLfvyJPoZsGFqFc-oqoYCZUcpxaM5acureYSdDhHPFX52il6W4nhpelqQ-DLuwy8HGtTPqQOsh-lBNyddMDZD98MB62W97kZgwhcG9N5okHFuzU2wJV7gRxeUwA2oVn2ibEDk_uzG-1xgIqEFmJI0pE9QDxGJ-3P_Idl4bkAYr8IXAMTmbs-QkF1kMYeCY2Ch7FaibFu930qJyjdOfR-QdHIWVAM8FdZ9375WBG66DcIbY73Iv31N1OQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2f7e507ebd.mp4?token=OjWbEnFGLTmKLKQMm3aTCzaKUcnxdzFr2FdOe8cvTdiamh_YbSTJS0OwdED80xYV6LttQ0_QHIaiP7q3KRHzswA64Gc9XfkLfvyJPoZsGFqFc-oqoYCZUcpxaM5acureYSdDhHPFX52il6W4nhpelqQ-DLuwy8HGtTPqQOsh-lBNyddMDZD98MB62W97kZgwhcG9N5okHFuzU2wJV7gRxeUwA2oVn2ibEDk_uzG-1xgIqEFmJI0pE9QDxGJ-3P_Idl4bkAYr8IXAMTmbs-QkF1kMYeCY2Ch7FaibFu930qJyjdOfR-QdHIWVAM8FdZ9375WBG66DcIbY73Iv31N1OQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🎙
رسول مجیدی مجری شبکه‌ورزش: خداداد عزیزی رو آنتن غیر قابل کنترله..!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/Futball180TV/105144" target="_blank">📅 09:04 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105141">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/Futball180TV/105141" target="_blank">📅 02:01 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105140">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7f2d04d67d.mp4?token=Oz7iuiyHHmrcc5_7t_6-_s9Wq_jkcTmdtirfrL0BGURjVkyLJTUQlovUiEF9ZLUGBJObRqDc4DSqpgsHhWg0ZaxSNB2Qe8GvyN3fVXbHB7XdQkpi2kB_ik1sQv2jPMwMkALvq6RJ6VGLYmuSShoDG-unUzgdu_1zWMScLJtSOCK6TMFZjN3rRU9nQq6J_IBwStrvRnjed_-5GM8pZRh33Ypu1r5Wk5Ek2XWN-I70bCOuMTAN_5Y1EVqk4j1EmidGKJNyeHOJV6KLvs8QWXCu55A7o99s_lBDSlAGplnneG7o-pqGV8bW1qi3gdZTuUo_anjwUWSmNL2-VR0FRuBQyQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7f2d04d67d.mp4?token=Oz7iuiyHHmrcc5_7t_6-_s9Wq_jkcTmdtirfrL0BGURjVkyLJTUQlovUiEF9ZLUGBJObRqDc4DSqpgsHhWg0ZaxSNB2Qe8GvyN3fVXbHB7XdQkpi2kB_ik1sQv2jPMwMkALvq6RJ6VGLYmuSShoDG-unUzgdu_1zWMScLJtSOCK6TMFZjN3rRU9nQq6J_IBwStrvRnjed_-5GM8pZRh33Ypu1r5Wk5Ek2XWN-I70bCOuMTAN_5Y1EVqk4j1EmidGKJNyeHOJV6KLvs8QWXCu55A7o99s_lBDSlAGplnneG7o-pqGV8bW1qi3gdZTuUo_anjwUWSmNL2-VR0FRuBQyQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
🚨
⭕️
پایگاه العدید قطر مورد هجوم موشک‌های سپاه قرار گرفت
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/Futball180TV/105140" target="_blank">📅 01:53 · 09 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>

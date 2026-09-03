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
<img src="https://cdn5.telesco.pe/file/UtTh4SnhwovT9HG_8sxaAXeUXHG-EsVkleVMYxtXqU-mMr7FNRbD0890UpZ4N4Sr5W_6edr04Kh3xmNnHW_egAf380jLNWETFSMeIzbyfzo8E5dkj756DxwWbMNB_lFcGY7uvwSeu3-TzoT66sovNuegEV7G5TgSnhZHZ6mYSSWzQuetTRh12KusE8PQefEeXUpRbGJtD_ZwTj_4GUnclmBnv-wwqJ_VVXdLLgRgB8xSvj1ULcuBbZXOE0Ca62s_j6I1v0JaIc-o-84QDLeuE8eP4dfIvBn5EDJv0IT0b8aoxuhgkcAaIbNwsimJOT0-q1BNhe4h3UhASRYIBDKoUQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 فوتبال 180</h1>
<p>@Futball180TV • 👥 430K عضو</p>
<a href="https://t.me/Futball180TV" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 In the name of God; The only popular sports channel on Telegram: All for Iran...🖤We respect the copyright laws and follow the laws, Mr.@Durov...🙏🌹Contact ads:@TivaAds</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-12 08:17:51</div>
<hr>

<div class="tg-post" id="msg-105408">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/603e84d100.mp4?token=kHxUYHyE343tS9Gbgzu4H8c9o_LxtIM8l2io8JQeTTyIazZ5lh2rexS9jd2NYgp_DksczAebGJuvzzO6FUTYbxCARLhkH04ViN42VfTWc-BFGmwb0KatOcoHrgfmtBimxpEXUw9kFW-awH9a-QgPgcstSV6wPAOCbXqnnJNpmz_p_eELTWPrgR98puLYHEx6dApJPRQcXxAocQ47idqrIip7VRqMJBrZcuQjmQj6toLgwgNzunqZerljz0d1q33UY-AQpfhh0YhliGQd_VNUXQQovGKDuj3Dt3ffo5LgjO0pXwbdfxw3FgLzXQtcUvRaYEdvXTPHMarFTM8KyunZRw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/603e84d100.mp4?token=kHxUYHyE343tS9Gbgzu4H8c9o_LxtIM8l2io8JQeTTyIazZ5lh2rexS9jd2NYgp_DksczAebGJuvzzO6FUTYbxCARLhkH04ViN42VfTWc-BFGmwb0KatOcoHrgfmtBimxpEXUw9kFW-awH9a-QgPgcstSV6wPAOCbXqnnJNpmz_p_eELTWPrgR98puLYHEx6dApJPRQcXxAocQ47idqrIip7VRqMJBrZcuQjmQj6toLgwgNzunqZerljz0d1q33UY-AQpfhh0YhliGQd_VNUXQQovGKDuj3Dt3ffo5LgjO0pXwbdfxw3FgLzXQtcUvRaYEdvXTPHMarFTM8KyunZRw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
🇮🇷
👍
وریا غفوری: یاسر‌آسانی جدا از فوتبال خوبش یک انسان شریف هست و در ایام حضورش در ایران برای یک فرد کم‌بضاعت خونه خریده
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 1.5K · <a href="https://t.me/Futball180TV/105408" target="_blank">📅 08:04 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105407">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/Futball180TV/105407" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 7.67K · <a href="https://t.me/Futball180TV/105407" target="_blank">📅 01:22 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105406">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/D1ot0_O1ssLZWH_GfdwStpnZn3ATWPuGB-zFo9XwEjQVKR7JwTMh5k46TUR31dS9zAXbvAc9vA4w2BpNekxOuKS8PyiYB4fsS8pZiE3oFHRooQhksXV-G-LmgIRKe0o566HfHuQsl8hx4hIAY-s4_TNSZz5VsXo9YQUq_8rE7edVE5t1Jqn8L7gwQ6LfNwjFXwaiHKt0bB6L9X4JzVjDIYnAMG9lztjgKSwkomOY5sHdvtIun8k10dTTiP7BYYSUSbbVbHeF2rS8NjoEg3obBEveJBLmcRYrGn5stmxqUAhjVoNgbkcKWWUxrz_4mCIFvVX3e6uSxyGdoWV4-xp5Kw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 7.72K · <a href="https://t.me/Futball180TV/105406" target="_blank">📅 01:22 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105405">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">🔴
⭕️
فوووووری/ همین الان با شروع مجدد جنگ دلار و ارز منفجر شد
😳
‼️
همین حالا چک کنید
👇
https://t.me/+S5Mn2k3LOf0wNjJk
https://t.me/+S5Mn2k3LOf0wNjJk
فوری برید ببینید
☝️
☝️
☝️</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/Futball180TV/105405" target="_blank">📅 00:34 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105404">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d578329cd4.mp4?token=FNVU25tF_hB6QFqTXfz2USl519P-B1lYN8ZBINZ9_7bf7eSvvEHkCxS2Zp4L5abDrUjqV5uu_QwWwxsBmnXZb54sF09xBWyGrmN6vMSueMEEkSU_orCi3h7dFVcW43fAVRVuzQrQ8yZcipHBi17EokSIl0EnSJU7DHz-hhAnpRkBvgfuiCbK5e4PP9S3ng-GAogElIojTnp-vTIDYM90UFR290tGG-akRV5AhKIExvi8SDCsVdt1Az148nLRpxAb_1YFJb9FCUJFvnxsz8RuKdK37kPdXqMAMrAWBibA3Tjcgb4tgCzbmU9gRtvwog9mkK2Tejnk4_9n367_jwu_1w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d578329cd4.mp4?token=FNVU25tF_hB6QFqTXfz2USl519P-B1lYN8ZBINZ9_7bf7eSvvEHkCxS2Zp4L5abDrUjqV5uu_QwWwxsBmnXZb54sF09xBWyGrmN6vMSueMEEkSU_orCi3h7dFVcW43fAVRVuzQrQ8yZcipHBi17EokSIl0EnSJU7DHz-hhAnpRkBvgfuiCbK5e4PP9S3ng-GAogElIojTnp-vTIDYM90UFR290tGG-akRV5AhKIExvi8SDCsVdt1Az148nLRpxAb_1YFJb9FCUJFvnxsz8RuKdK37kPdXqMAMrAWBibA3Tjcgb4tgCzbmU9gRtvwog9mkK2Tejnk4_9n367_jwu_1w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
🇮🇷
🇮🇷
‼️
ویدیو لحظه حمله حسین کنعانی و چنگ زدن به عارف‌آقاسی مدافع استقلال
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/Futball180TV/105404" target="_blank">📅 00:08 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105403">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qEvWfxm--jfuwSUvkYQkRpdV7MWp1fnyMMoayj3wSqLkI0xfSzpFhEmS4UA74I915c19hzskT-2JFzn7qD9F8zqv-rKjHcZuZTC4XjfMyQ4L06fpGsFwa5-GAdPXPSkN1u3wLgUONP1rLEwP9TkCN-B8MYjIvGtxyDDO2tyQbHwXKlf5DexotAczNZpe8fNNdq-jxswZPycCS64eAZ82fNuhuJJ1YduD2UyDZJpgYw1oDO9bGeC2yyhsXaLPRZVshrXVMR_OO3PXPDJJezZR0i9WLbuSdUXt0wj2DCVHRDeKsz7o0o6d_5Nhj4GlPMAYtNhjCR3rpTyj8wxbtDxbTw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
👍
فدراسیون فوتبال آرژانتین برنامه‌ریزی کرده که همه بازی‌های هفته آینده مسابقات مردان و زنان توی دقیقه ۱۰ برای یک دقیقه متوقف بشه تا تماشاچی‌ها و بازیکنا لیونل مسی رو تشویق کنن.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/Futball180TV/105403" target="_blank">📅 00:06 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105402">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e447de2235.mp4?token=fPg89FGkTwWv7oJDAO3cxs5J434Xh_pEkEjRtP4yFJ4hcqxp4tZQKAgVEs8Ie5vXVbePMM7BZca-RQfpe7Xz6aOlX981DLlw0B1KI3fRtqNmly6kGh1fw5ccmOaaiC354zNqB_9Z2IqyCJnHERADpR-znXpD_3VM3xTlmtVv3YbwT6x-HtIWH5Do2tJRgp-NaTdQCIB_vB_BwK5fm1vi5Zm8mWLu7Q1tNIBv32waVPFW1iZc_IqnjWSeh6Ap_XaMwu6sPWSZ2DqLFS_U59lIopogQ9-UEPzAuoFdGYbtvdU2GP9SeXVAe4A2dl7lN3Rm4tS78MLW17bDdZlAyi4ogA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e447de2235.mp4?token=fPg89FGkTwWv7oJDAO3cxs5J434Xh_pEkEjRtP4yFJ4hcqxp4tZQKAgVEs8Ie5vXVbePMM7BZca-RQfpe7Xz6aOlX981DLlw0B1KI3fRtqNmly6kGh1fw5ccmOaaiC354zNqB_9Z2IqyCJnHERADpR-znXpD_3VM3xTlmtVv3YbwT6x-HtIWH5Do2tJRgp-NaTdQCIB_vB_BwK5fm1vi5Zm8mWLu7Q1tNIBv32waVPFW1iZc_IqnjWSeh6Ap_XaMwu6sPWSZ2DqLFS_U59lIopogQ9-UEPzAuoFdGYbtvdU2GP9SeXVAe4A2dl7lN3Rm4tS78MLW17bDdZlAyi4ogA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
‼️
⚠️
🇮🇷
تارتار: ارونوف؟ هیچکس از پرسپولیس بزرگتر نیست
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/Futball180TV/105402" target="_blank">📅 23:16 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105401">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">🚨
‼️
🇮🇷
❤️
کنعانی زادگان: از اول بازی استقلالی‌ها موز و سنگ به سمت ما پرتاب کردند
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/Futball180TV/105401" target="_blank">📅 22:51 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105400">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c06eb0d1ff.mp4?token=vtlSLvrZ5U32lGsjD_XlcNWIO9VDz1T8TVa_Y2_DnlExCb0TjhuMamrvEFSrK4kAuMnbuhYwnbvzpo4FBf4gj22UryciTnOu2s48_L85qVfMucOI-RQPG5ai1r2f4adFERDiKKfLf2HF7aFnjM73kcI_MCqiczUSuqPkD21jC9WT6zneR_i2o2gY4BlUmEc3U30HJyDeD7aziQCjSzwc6ahHV9pOlOYSmvRPNHvLO_vqN0ejUqHAafFPBAElFEZgqcaDAbgn2jXIa7C2Jr_1hjmu6Zss0rK--G5V3roO5H7wBAH1pchAak8MnRoEhFjVEHgjchNdVwIVA9ffqaScxw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c06eb0d1ff.mp4?token=vtlSLvrZ5U32lGsjD_XlcNWIO9VDz1T8TVa_Y2_DnlExCb0TjhuMamrvEFSrK4kAuMnbuhYwnbvzpo4FBf4gj22UryciTnOu2s48_L85qVfMucOI-RQPG5ai1r2f4adFERDiKKfLf2HF7aFnjM73kcI_MCqiczUSuqPkD21jC9WT6zneR_i2o2gY4BlUmEc3U30HJyDeD7aziQCjSzwc6ahHV9pOlOYSmvRPNHvLO_vqN0ejUqHAafFPBAElFEZgqcaDAbgn2jXIa7C2Jr_1hjmu6Zss0rK--G5V3roO5H7wBAH1pchAak8MnRoEhFjVEHgjchNdVwIVA9ffqaScxw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
🇮🇷
🇮🇷
📹
مارک‌کلاتنبرگ در لایو برنامه عادل فردوسی‌پور: موعود بنیادی‌فر باید حسین کنعانی‌زادگان را اخراج می‌کرد و این تنها اشتباه فاحش داور بود
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/Futball180TV/105400" target="_blank">📅 22:48 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105399">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ce1c0fb29d.mp4?token=g5yGeNW-rs1dDltTCX853CCmxC56IPtTsDG20qYtfOMZcIe6ZFCvBc9tjKwV6mG4wofY5VQOi8r0ucaDVe9LkdCUYzdOGBL-3NpRQXeDhtn3jvTYMpysy7XKF8bp25kpcZ6cHgS_GgL-P5E7FhFKBfhsg8YG21BgXDYUk9G1KDuX9uCT8xbCKmTe2-pV4f48a4h1ZmxZu4fJodDMG9CSJuvHa4Gledr38kgWrlyRshv1I_qdemmPkzpckUt-wDH88n20_0rwJEbljvxex3wFACFQJjJhFBmdrGe95rjya0Ln7frYmL-DWmroK8YXSn_Es8-pkiyPHauxxVyzEeGP6Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ce1c0fb29d.mp4?token=g5yGeNW-rs1dDltTCX853CCmxC56IPtTsDG20qYtfOMZcIe6ZFCvBc9tjKwV6mG4wofY5VQOi8r0ucaDVe9LkdCUYzdOGBL-3NpRQXeDhtn3jvTYMpysy7XKF8bp25kpcZ6cHgS_GgL-P5E7FhFKBfhsg8YG21BgXDYUk9G1KDuX9uCT8xbCKmTe2-pV4f48a4h1ZmxZu4fJodDMG9CSJuvHa4Gledr38kgWrlyRshv1I_qdemmPkzpckUt-wDH88n20_0rwJEbljvxex3wFACFQJjJhFBmdrGe95rjya0Ln7frYmL-DWmroK8YXSn_Es8-pkiyPHauxxVyzEeGP6Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
💙
سهراب بختیاری زاده: فکر می‌کنم اگر آقا مهدی (تارتار) بازی را دوباره ببیند، نظرش عوض می‌شود.
🔵
اوت دستی یکی از راهکارهای ضربه زدن به حریف است ولی ما جزو تیم‌هایی هستیم که بازیکنی نداریم بتواند اوت دستی به آن صورت در باکس حریف بیندازد.
🔵
من بازیکنانم را تحسین می‌کنم چون دو بازی را در مدت زمانی کوتاهی انجام دادند.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/Futball180TV/105399" target="_blank">📅 22:46 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105398">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0cef9c1a80.mp4?token=vFxHz_BoXKKoS-CLhmGFX1nJozeqrKnnh0PtssWmcUSr8-In5nXx_i9RUM_ulizrNrK4K5Am_L_K0jxhjx81iOyP_iMRB87J86Z_BqBD48sHwDKcqjYl1jatPyW8cqiXEdU-VwIT6wHAJyYz9MQsWYXdZ50SEvSGayQRxc4UTkPbSf9j3CFeF6W1JFpimscyVHX02f-0kIIknSezlsP95wdkp30FqMw3Ys8hjC3jqjt6SLBeLu0b7vBfhlKwplFAlOXHSNoAAWjOnXJvUZ2NyJFqBPiAhS4ht_NepK0KGALr7zQi6KBXn2D2OhWRdAP97vcBMiSMzw5oB9_27A0t_w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0cef9c1a80.mp4?token=vFxHz_BoXKKoS-CLhmGFX1nJozeqrKnnh0PtssWmcUSr8-In5nXx_i9RUM_ulizrNrK4K5Am_L_K0jxhjx81iOyP_iMRB87J86Z_BqBD48sHwDKcqjYl1jatPyW8cqiXEdU-VwIT6wHAJyYz9MQsWYXdZ50SEvSGayQRxc4UTkPbSf9j3CFeF6W1JFpimscyVHX02f-0kIIknSezlsP95wdkp30FqMw3Ys8hjC3jqjt6SLBeLu0b7vBfhlKwplFAlOXHSNoAAWjOnXJvUZ2NyJFqBPiAhS4ht_NepK0KGALr7zQi6KBXn2D2OhWRdAP97vcBMiSMzw5oB9_27A0t_w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
💙
سهراب بختیاری زاده: کسانی که بازی را دیدند، از این بازی لذت بردند و از دربی‌هایی بود که حاشیه به آن شکل نداشت.
🔵
در نیمه دوم ما تغییراتی دادیم، به دلیل اینکه در نیمه اول نظم بازی را در میانه زمین به حریف داده بودیم و این موضوع را رفع کردیم.
🔵
روی یک غافلگیری گل خوردیم ولی برگشتیم و این نکته مهمی است. می‌شد گل‌های دیگری هم بزنیم.
🔵
هیچوقت درباره داوری قضاوت نکرده‌ام ولی دو هفته است که اتفاقاتی رخ می‌دهد. در بازی با فولاد دو کارت زرد اشتباه به ما دادند و امروز هم فکر می‌کنم صحنه اسلامی، پنالتی بود.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/Futball180TV/105398" target="_blank">📅 22:46 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105397">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rRCTjaTm5yzyRytfC8e60VFkzNNy5mPObtDKTpA3vzLcocvwhYHjmdTDrXEzU7Bz4cTNbQgrKWQaUbPUijmbho1zTCRDhXa-61FVvb3Eb0bNcvuZnDL8yR4oAAxVyORONjKNtcaoXx6NFiUjbS-IubEncoh9R2BL0klyFRk45taB6TwzTZBSgFjObYF5IY0Ffr1ST1u1QyqDiHiKw8AIcCnC6pe71UySLJyFeja_jtv9DLc-MIaoJbdKTsFQUEfLE1J1DPBEFEtDiGI2nIH1lPOGH1R9i1gatgI2l2AbraiZsirsWwcNtR_Cl9ttgItbLjT80GsLWdX6k0BJ4sj5Vg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇮🇷
🇮🇷
سپاهان در بازی مقابل نفت‌آبادان به تساوی بدون‌گل دست‌یافت!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/Futball180TV/105397" target="_blank">📅 22:35 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105396">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iiBi4V9Lq9tL_i2NpZOUCpdBCqlzq5TPVJ3uBPICnH0c3hSCp7Bz8sUiQGELN1jkwvhGgt5_bD89a-jGcNf_Ny4MbJHPJsJLK3KAvEbZLzQh-AmYFpNzycEAV-lrlnouFinLv608tnZBUDBB6133m5LTSwgExurFk-U5qEh6RcUsv8AnpusFYF5yl-U1IGxDnk2Rg-qLGOGvNOOjwATxswXUFbpNhj4V0EnkfJ-HkkU2LMscCTcLXkbG9AInsVHnnEvsoSotSonOYuwGH32vdWd3S1RccBB67Ta1hgWTr94nnmCDdy7dkm6aHWnckNDNqSvtrelJv3_YW_7RWQTRDA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇮🇷
🇮🇷
سپاهان در بازی مقابل نفت‌آبادان به تساوی بدون‌گل دست‌یافت!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/Futball180TV/105396" target="_blank">📅 22:34 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105395">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">🚨
‼️
⚠️
لحظه حمله کنعانی‌زادگان به عارف آقاسی که منجر به خونریزی گلوی مدافع استقلال شد و داور هم این صحنه را ندید!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/Futball180TV/105395" target="_blank">📅 22:26 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105394">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/507e713ebd.mp4?token=akeDvVEYOPC8nq-AZCHzYQzbWCuAaT7cw-8vXUl8-4hizyA3QiYTVDqyjWThPXWRvjdgkhTkcEpPyDOJY8z6RQB_GwHMGn3HvZyHcA2B3DKSojQKQIyykMfiE1_1pI6nj2aZo0RbTcDUiuf1TdJZ97ETQQqyFrFyjk_w-dagoPMVNpZtOmHsRle8K3hg_vdlkXXiHmwhCJuYPv9DQhHklCQbEdYaSNFrxuldLYM6puPyldfONf0rXPoUNQpfJs4_Y-seLpMymgqZ3TOJroVFSHf9I0X6Ou4Yj8yEvZO5PWEYOpQZYA3ImQycUjna_X4aUeYrHuF1aYYNusaYkGFc3w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/507e713ebd.mp4?token=akeDvVEYOPC8nq-AZCHzYQzbWCuAaT7cw-8vXUl8-4hizyA3QiYTVDqyjWThPXWRvjdgkhTkcEpPyDOJY8z6RQB_GwHMGn3HvZyHcA2B3DKSojQKQIyykMfiE1_1pI6nj2aZo0RbTcDUiuf1TdJZ97ETQQqyFrFyjk_w-dagoPMVNpZtOmHsRle8K3hg_vdlkXXiHmwhCJuYPv9DQhHklCQbEdYaSNFrxuldLYM6puPyldfONf0rXPoUNQpfJs4_Y-seLpMymgqZ3TOJroVFSHf9I0X6Ou4Yj8yEvZO5PWEYOpQZYA3ImQycUjna_X4aUeYrHuF1aYYNusaYkGFc3w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🎙
❤️
تارتار در نشست خبری: گروه داوری امروز خیلی خوب عمل کرد، خسته نباشید به آنها می گویم/ امروز هم پرسپولیس خوب بازی کرد و هم استقلال
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/Futball180TV/105394" target="_blank">📅 22:16 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105393">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">🚨
🚨
🚨
🚨
⭕️
ترامپ: برای آغاز یک حمله ویرانگر دیگر به ایران آماده‌ایم که مدت کوتاهی خواهد بود!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/Futball180TV/105393" target="_blank">📅 22:11 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105392">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/a7Ph6NOd2bi16shhNYYWHKT-vLHL45JO39HXY-B5IFce2Oe1bWhDe2loXUYlQIymWE0tQgFKavFBUDZ1oeVqyuCqfKuy2jetoCC4A-9aCcAr4BEPFlNGdJy6h_62t1GnkQWTodAHuytmqcepq2xus_rQta2q1ax2YeQBnE-jw15GO__m0SchF8LvYBo5NfcWuVS631SKZnNMb07ztzATpc8vZN4JRUEuoUFAJFLqNYpfPCFktGWft8Bn_TVe1XLTsdKKz3az7oLz7lbfeA57iNq8hKHJRiYc-Jw8cvE5SEttUP7a0yPSqEfN2rNgtZ2Dt4-L7PLSY0uoc-rDa7knfA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
‼️
🇮🇷
🇮🇷
باشگاه استقلال با انتشار این عکس نوشت: تصویری از آسیب به گلوی عارف آقاسی که توسط کنعانی‌زادگان رقم خورد و با بی توجهی داور همراه شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/Futball180TV/105392" target="_blank">📅 22:07 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105391">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/63becc7280.mp4?token=KXtei4f638h0qkGMXK8VbXSU6gSDVoEI1by3h0ZB1g6HMcPHUfAEa82GIGwya5kwzLJf_X2GQ3zS9Urn5by7L7oC5INeRrCbK9Z3q46qY3-xPsBZoxUYUZwTYzTVTpQJ9Q6z-vkyGND20g75ZtXT_-cQ0fwQhnVzmSrC9g94Gqp2dIwAcAMnz2YYDT9dGePZ00PDi25oX9XCXG8uzi72JAOT8ZUHMvCh6IGzRdnzUqzZO3oaORC2bBM1kdnZsP9ydGKy_7Vus5xhoda_J__HURPR43dzPSdQ__hMhVxp9FFGLgcCsrlH4OGUF3LbTdPNwv1nbmEsxKEs3eURhlIjRnedYHQe4c2AZDe9W-N0kag6JHrVPao2Afri89sYUqifmWENVvgJbFX2uBfVdavbByw3a8zGRYdnkmVpbBRgRNIBRDwJ8GpQkIZpxkxTHaTe0QyfSq0HFBHTAR1JBU3JESzVJDDLx-u36hBypvcY21f8RmqHd2jrwOa2O2b6vQXE48Lq99Akaa7sHnhlS8S4IRTAuoMGqv7vVD8cXRu2QUiMWo1t50Li-xMyNMJIPG8gp8TMYFUoGMAIbKU04MActWRIANB73qHlKh82x_yrbFsJqnS5U4DT9bwfAiKlk2hloPix3RpbGFg53-G-K1PYdO3kGXeb5RQYWp-b5HZdVOY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/63becc7280.mp4?token=KXtei4f638h0qkGMXK8VbXSU6gSDVoEI1by3h0ZB1g6HMcPHUfAEa82GIGwya5kwzLJf_X2GQ3zS9Urn5by7L7oC5INeRrCbK9Z3q46qY3-xPsBZoxUYUZwTYzTVTpQJ9Q6z-vkyGND20g75ZtXT_-cQ0fwQhnVzmSrC9g94Gqp2dIwAcAMnz2YYDT9dGePZ00PDi25oX9XCXG8uzi72JAOT8ZUHMvCh6IGzRdnzUqzZO3oaORC2bBM1kdnZsP9ydGKy_7Vus5xhoda_J__HURPR43dzPSdQ__hMhVxp9FFGLgcCsrlH4OGUF3LbTdPNwv1nbmEsxKEs3eURhlIjRnedYHQe4c2AZDe9W-N0kag6JHrVPao2Afri89sYUqifmWENVvgJbFX2uBfVdavbByw3a8zGRYdnkmVpbBRgRNIBRDwJ8GpQkIZpxkxTHaTe0QyfSq0HFBHTAR1JBU3JESzVJDDLx-u36hBypvcY21f8RmqHd2jrwOa2O2b6vQXE48Lq99Akaa7sHnhlS8S4IRTAuoMGqv7vVD8cXRu2QUiMWo1t50Li-xMyNMJIPG8gp8TMYFUoGMAIbKU04MActWRIANB73qHlKh82x_yrbFsJqnS5U4DT9bwfAiKlk2hloPix3RpbGFg53-G-K1PYdO3kGXeb5RQYWp-b5HZdVOY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
📊
آنالیز گل پرسپولیس به استقلال در دربی که عدم یارگیری آبی‌پوشان مشهود است
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/Futball180TV/105391" target="_blank">📅 21:58 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105390">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">🚨
‼️
🎙
تاجرنیا: موقعیت های استقلال بیشتر بود و حق ما برد بود/ یکی از جذاب ترین دربی‌های چند سال اخیر را شاهد بود
سهراب تیم بسیار خوبی را جمع کرده است/ من به این تیم امیدوارم
داوری بازی؟ مهم این بود تماشاگران بازی خوبی دیدند و باید 3 امتیاز را می گرفتیم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/Futball180TV/105390" target="_blank">📅 21:51 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105389">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KOmjgsIU_zxz4eZoFUC0PMkxmZZz3v2W-tTuk_mK-JY9Z-k9pzquw3wOzPRc2GG8XXKK22mZ3VXG2BUt_84e6Fk_SUS99OfRx1ytxLaNYn7AVcSGzthG1Eiuv_A20hqV2R8RaF8NUqXWp4SrVymOFebMnMI0RowWFuj2MVF47fUNwMODozUPNHK66YFlqPMfX22fug61HcI8uDh_bqrYyOtwjTGRejZwHAsrnXip31meSD1EE9voEGXqvseiNwJrtznz2TF5StNWtlXNYD5QAKhziivAerejraTx6rlLI5nu-H8WZk6XHTWy8n7jFpT4jmUPIVZN7MsEDtC4xFBjpA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
🇮🇷
🇮🇷
آمار بازی استقلال - پرسپولیس
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/Futball180TV/105389" target="_blank">📅 21:37 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105388">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">🚨
شکایت رسمی پرسپولیس از استقلال؛ پای ۳-۰ وسط است!
باشگاه پرسپولیس با استناد به الزامات سازمان لیگ، از استقلال شکایت کرده است. سرخ‌ها مدعی‌اند آسانی و اشورماتف طی دو فصل اخیر بدون پروانه کار و اقامت قانونی به میدان رفته‌اند و در صورت تأیید تخلف، باید نتایج بازی‌های مربوطه ۳ بر صفر اعلام شود.
حالا باید دید سازمان لیگ با این شکایت جنجالی چه برخوردی خواهد کرد!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/Futball180TV/105388" target="_blank">📅 21:37 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105387">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">🚨
🇮🇷
🇮🇷
خلاصه بازی استقلال یک پرسپولیس یک
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/Futball180TV/105387" target="_blank">📅 21:34 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105385">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DlJONgUKZR3Y_nXhVWlM8qKksQ4fVj1PEyo7HG5Fudx2mR09l5kPItVjrzGoFkYKjraB24AfMWkC15pdO6uQ3AxVXf-0YxBPNh66fR30iwO8jnq1wgwnqbR1dssDyYkggh4jc-GFkOxrzVkWrRIR4CWXHsShQUPPaOMQxQNLeO0R6KPDaZ4-c9LcvfMmXl9hBCq3vYhhRLevrDZ8IRiSl8FCfko9u8T61gZvpbKtCfie-FAQ78S9zdVsA9QmRGLqDbxdkaOXqbkz45zmf8eIuiFjRIJ-mZ2CxpuR1O0MTwzz852celt1BVoi9JWs48kczDRVFio1Paeh7Tvrs21L3A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
‼️
📊
جدول لیگ‌برتر پس از پایان بازی‌ دربی! پرسپولیس در دومین بازی بزرگ خودش هم با رقبای مستقیمش موفق به برتری نشد!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/Futball180TV/105385" target="_blank">📅 21:31 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105384">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GHC4AxN9ufNZUi8EVfp47GxS1Nspq0OM6JunGzGN9lf03IYSSXT1saR4Eom6E005_tD7kZQcv05z46_RtBuyPdk0Pe5c0yeHjAiqoUwaLMyWzSqL69oZ2HhffP7pQGSSn77UHRJHG7hBKx6Cw6XAMzA_vWgsPKhaYZR6b8oeeC-97g3Nv84byi7rDPD3vflYBSODi4ZPFl746VFL5r1K3OEX5PNNuHoxsnzI_iVUXAimVnlWY8_O6zG2YAwwxUK3tAiYooiC-ffhVBbofnAwJxCz6L3Uj6KosbImv-lPE_VEeR9mFIM_bcoVUlx_HAq70kWIwQ30ILK5fUQkQI4m0Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
✅
🇮🇷
هفته‌پنجم لیگ‌برتر فوتبال؛ ۹۰ دقیقه هیجانی و تماشایی در اصفهان بدون برنده؛ هواداران از دیدن بازی تارتتا و گواردیولا لذت بردند!
🇮🇷
پرسپولیس
😃
-
😃
استقلال
🇮🇷
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/Futball180TV/105384" target="_blank">📅 21:30 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105383">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VvBLRCxKmM0uoUN2l8pNSt3F5DbJ2Sf_VanvgHwsAuup5DVCQqKqKLuHN99WdOlxe2R978Jq_zWB_I9TM6avI7f9WwdB0jH5gFIpQ7Ow7AKJBsL2Y3dl2F85_Mh_gyyZqHYP8TQDEaaqBUKEWjgH-851G0gb2N_Qvsr61lybmr1SRey1MKr-gRU8Niz_qGrUHiXwA0O6jVDlcF7Y4Ac2WrJkfXnmBNHuwx2JskrdKdv1NsqIzvd_jNPz85P3YFWyqn-4pQugV1OmtGndkbsQ-LSQWCNwQsmFKo0ts7g8AUGIPJhJVnXH-ocDhxsH4tLU1kY8KfmIxlIkvFkJRSPT8Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
✅
🇮🇷
هفته‌پنجم لیگ‌برتر فوتبال؛ ۹۰ دقیقه هیجانی و تماشایی در اصفهان بدون برنده؛ هواداران از دیدن بازی تارتتا و گواردیولا لذت بردند!
🇮🇷
پرسپولیس
😃
-
😃
استقلال
🇮🇷
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/Futball180TV/105383" target="_blank">📅 21:26 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105382">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b714d173a5.mp4?token=JPgw2wmdtdz5qgnTLj26fStaruKon5vexK8WMi0smQP4bc0Za5Hc_eJLJst01450-cLRPfOG4rR8tAOpw7sBFExfa5JSGdOA5Z1qL_Q46WJzU1QSQEKr3chLILPUh8krU4wQ2gyhJLMYo7ImxCSxn0NrvCDU63SV2Ma003O91R3GOmr0aHc7Hy3_UoZJm0UFcXicM2hj9BezqEbEua5YbKBJf7WSOCFBgLNgnNg3PXYXsDucIIdFTbCpUf0LbX1YkU-4z4LP2DiMho4u1w_0aPdRhJ72WRZlDmZlcDsH95UOr1d1ylXKogM2N9oraJCV65YAd_cySDY6Ps2BwSj1ug" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b714d173a5.mp4?token=JPgw2wmdtdz5qgnTLj26fStaruKon5vexK8WMi0smQP4bc0Za5Hc_eJLJst01450-cLRPfOG4rR8tAOpw7sBFExfa5JSGdOA5Z1qL_Q46WJzU1QSQEKr3chLILPUh8krU4wQ2gyhJLMYo7ImxCSxn0NrvCDU63SV2Ma003O91R3GOmr0aHc7Hy3_UoZJm0UFcXicM2hj9BezqEbEua5YbKBJf7WSOCFBgLNgnNg3PXYXsDucIIdFTbCpUf0LbX1YkU-4z4LP2DiMho4u1w_0aPdRhJ72WRZlDmZlcDsH95UOr1d1ylXKogM2N9oraJCV65YAd_cySDY6Ps2BwSj1ug" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
صحنه ای که بازیکنان پرسپولیس اعتقاد به هند داشتند
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/Futball180TV/105382" target="_blank">📅 21:20 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105381">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d553ea91ff.mp4?token=ZzeUQeCHelaSsL2Lk6XkuTPDSq7lHKP-ZyqYmTzdYmOQbp3Vi9dQTQ_DIETrN0SeB5xt2F8Ygd6-basAtjXUNL1GQbOjTuSKJAesxoIpPZn94oVAiX7jTTF32OksPN6w2ZfnSlaG3pc-oU06LS9dB53D4CaD4Y0kVIWYPdpa2NMjymSdrE5JWtl34cubL1V4gwt3VTN-jpvuaENYXwElzbSHC6a900R9BlDMLJQTwp7TQVv-LXjkhkwvZFqzJ6ryk2g3w8FVi9JS_x9m8PUINbLzbTz0NqF0jSnBl52dOfSvULSIhIkhtBiiOYSRKsUxbFTHzmClItZRNDW41ZFqig" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d553ea91ff.mp4?token=ZzeUQeCHelaSsL2Lk6XkuTPDSq7lHKP-ZyqYmTzdYmOQbp3Vi9dQTQ_DIETrN0SeB5xt2F8Ygd6-basAtjXUNL1GQbOjTuSKJAesxoIpPZn94oVAiX7jTTF32OksPN6w2ZfnSlaG3pc-oU06LS9dB53D4CaD4Y0kVIWYPdpa2NMjymSdrE5JWtl34cubL1V4gwt3VTN-jpvuaENYXwElzbSHC6a900R9BlDMLJQTwp7TQVv-LXjkhkwvZFqzJ6ryk2g3w8FVi9JS_x9m8PUINbLzbTz0NqF0jSnBl52dOfSvULSIhIkhtBiiOYSRKsUxbFTHzmClItZRNDW41ZFqig" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شوت علیپور خطرناک به بیرون رفت
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/Futball180TV/105381" target="_blank">📅 21:05 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105380">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LsScHz8W8nfcdpErj5GRqav6qjBMWQY7x2EpaBlW_jQ90orasx6OacfDOorHBuxjXxWQ86WN1hh0fJMrfUR875VnGwKNVUwVl9wCMW0XXHO0ftWnVv6nd92WVhaGoa0bsopWl10uLkahFCIhfl40JADZpapyq_St5Gs0GDkjVs6dJTHymdBpoX5Nk29ghhu87eem-1YDpQJd_u-0LN4T_T4VpcL1KN8hKbqyd8YCg_s2XXRECmWNpapOmoF9Fa4Eo7nv8EXdfX8e_GrCzLeM6CdpMSe3QNOB8LqTwc4-GiIbzt0SQ_ZpaNhJWyg0aP86ERPfn6JxocAgb-JkVSZILA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
‼️
🇮🇷
🇮🇷
باشگاه استقلال با انتشار این عکس نوشت: تصویری از آسیب به گلوی عارف آقاسی که توسط کنعانی‌زادگان رقم خورد و با بی توجهی داور همراه شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/Futball180TV/105380" target="_blank">📅 20:58 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105379">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3436b36eb0.mp4?token=JY357C2MIzy9SWYZkbXQ-KccpaHXD9QlqpfRMgtuzaGzhn7xHjqxBZIPATjEZjpN_GAWWRMjS1j0ygvl_m3Qmydz1qMW16mxFZA4U9Tre9LY7zW6ML6ED9oNXbDxdBxMpgYmcgsriLuaU7tIXf6tnZS_fsjOUEskBhX6VEoMGjPp5-HWx7zeurqMDBdA-KnrLL5tRSM-hRLvB9VUB1l1wOmTsOXYrfaURHxRi7exy6LajQuIHDvNsMDeUMTvxW1xw5Ln1eTl4sW3zU8CxPyoYUS9H1FEZQ_3AhH0U0hBDIUVT8tIVj0on7moqF6TFK6I3sX-fjaHnmOOKMPe-x8kZg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3436b36eb0.mp4?token=JY357C2MIzy9SWYZkbXQ-KccpaHXD9QlqpfRMgtuzaGzhn7xHjqxBZIPATjEZjpN_GAWWRMjS1j0ygvl_m3Qmydz1qMW16mxFZA4U9Tre9LY7zW6ML6ED9oNXbDxdBxMpgYmcgsriLuaU7tIXf6tnZS_fsjOUEskBhX6VEoMGjPp5-HWx7zeurqMDBdA-KnrLL5tRSM-hRLvB9VUB1l1wOmTsOXYrfaURHxRi7exy6LajQuIHDvNsMDeUMTvxW1xw5Ln1eTl4sW3zU8CxPyoYUS9H1FEZQ_3AhH0U0hBDIUVT8tIVj0on7moqF6TFK6I3sX-fjaHnmOOKMPe-x8kZg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
🇮🇷
گل اول استقلال به پرسپولیس توسط آسانی(60)
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/Futball180TV/105379" target="_blank">📅 20:53 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105378">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">آسانییییییی</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/Futball180TV/105378" target="_blank">📅 20:52 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105377">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">یاسرررررررر</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/Futball180TV/105377" target="_blank">📅 20:52 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105376">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">استقلال مساویووووو زددد</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/Futball180TV/105376" target="_blank">📅 20:52 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105375">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">گلگلگگلگلگلگگلگلگلگل</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/Futball180TV/105375" target="_blank">📅 20:51 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105374">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c9bc0b70b2.mp4?token=SQdMYtvizasq40LrmpfSBHdvaig2VqZZhbSrc0eAYnXAgGtLOYvi0DzUwkj6xRLOROVTwRQYcAyMkHV5w5zI-8WCjMiES08OJYugnUxLNkTn4xtvEDjUhLJR5dEBMGz8X1nubG2dmwIabGZ9Jm5blqfvuz3YjVekafM4TR6m39qLO52X-ct2-gzYXY1uwrlxmseGxwZrtqa4ceukygb6qMiRTbsF07BvYlGS1mvSDbk7sLE4VTXhajDJWqUhZ-qSGS-iU4JvIgNdqDBLGOTzs9Fr2frBjMCoAoPUxxRolh2I3NzfzAXYzwxidaCTdplLThyE8-A3x_8RFv-Jph7DPY6Fwx-paIcdxVATMhwk_emVbWQOcpRidrZ4XRnbVSM6VPVe_sGcJ5Q_Y8hXhwaVD_SAJI_XkmcIl-zOCbsmeefLJ-_v0j_bd08Zwj3X0U_0h2M71TOtMBnwOWrOORQGfKPrKNXoB6Ap7JItKV1ZFhSzf1ssdIcFwDRCYjfjGJIK6Zz5M1Y1gkkOBRKOc9xYv8omriXFrsxPcz0XE9HDTBhs50t59qiscxLJ1FKwgqhrhmTbDFLpti4Hvyw-p4HeY7lzuQ7Q_yZY6kwHs8sLP5yy051TZjC1bsyv_U9liCSTOiHEx8cys84MkNI3BT_8NGpI7Y9XVsAdQdshN4ob7FI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c9bc0b70b2.mp4?token=SQdMYtvizasq40LrmpfSBHdvaig2VqZZhbSrc0eAYnXAgGtLOYvi0DzUwkj6xRLOROVTwRQYcAyMkHV5w5zI-8WCjMiES08OJYugnUxLNkTn4xtvEDjUhLJR5dEBMGz8X1nubG2dmwIabGZ9Jm5blqfvuz3YjVekafM4TR6m39qLO52X-ct2-gzYXY1uwrlxmseGxwZrtqa4ceukygb6qMiRTbsF07BvYlGS1mvSDbk7sLE4VTXhajDJWqUhZ-qSGS-iU4JvIgNdqDBLGOTzs9Fr2frBjMCoAoPUxxRolh2I3NzfzAXYzwxidaCTdplLThyE8-A3x_8RFv-Jph7DPY6Fwx-paIcdxVATMhwk_emVbWQOcpRidrZ4XRnbVSM6VPVe_sGcJ5Q_Y8hXhwaVD_SAJI_XkmcIl-zOCbsmeefLJ-_v0j_bd08Zwj3X0U_0h2M71TOtMBnwOWrOORQGfKPrKNXoB6Ap7JItKV1ZFhSzf1ssdIcFwDRCYjfjGJIK6Zz5M1Y1gkkOBRKOc9xYv8omriXFrsxPcz0XE9HDTBhs50t59qiscxLJ1FKwgqhrhmTbDFLpti4Hvyw-p4HeY7lzuQ7Q_yZY6kwHs8sLP5yy051TZjC1bsyv_U9liCSTOiHEx8cys84MkNI3BT_8NGpI7Y9XVsAdQdshN4ob7FI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
ضربه خطرناک آسانی به تیرک برخورد کرد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/Futball180TV/105374" target="_blank">📅 20:49 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105373">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/35c2230f3b.mp4?token=eaBV2eqs966XVAvuwjsBnQ6lfZf23Bv1NzVSfHABG7lIN2oF82Y-Is0D2Cf4PdrFxRUrDADIWyIvpzgdJ70O-4vnDHBUxzgTDcHHpnWiOqYjxkhr8wvl69h34tKhYZ4Fb8Nj89m7zcyFye8VkNPpr1TBSMPi3NMVIyWGrDOT-5Ar-lohbuUfOG9j_Aacy8yeDpXkT6eSEs1sfLMlrfxeKn_p8lYfmf-DZZpWWL_j0yekJ3MncZXaRMFkM1ydCQMLh56hKbvYnXx7YANY4S4Kq9ITb-b8zyA1tbZgmKNq60vKeQCUHvNF9PZ9g-mXFjNSZsBQksKZVE0lvL2x2Lhn2g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/35c2230f3b.mp4?token=eaBV2eqs966XVAvuwjsBnQ6lfZf23Bv1NzVSfHABG7lIN2oF82Y-Is0D2Cf4PdrFxRUrDADIWyIvpzgdJ70O-4vnDHBUxzgTDcHHpnWiOqYjxkhr8wvl69h34tKhYZ4Fb8Nj89m7zcyFye8VkNPpr1TBSMPi3NMVIyWGrDOT-5Ar-lohbuUfOG9j_Aacy8yeDpXkT6eSEs1sfLMlrfxeKn_p8lYfmf-DZZpWWL_j0yekJ3MncZXaRMFkM1ydCQMLh56hKbvYnXx7YANY4S4Kq9ITb-b8zyA1tbZgmKNq60vKeQCUHvNF9PZ9g-mXFjNSZsBQksKZVE0lvL2x2Lhn2g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
🇮🇷
گل اول پرسپولیس به استقلال توسط محمدمهدی محبی 50
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/Futball180TV/105373" target="_blank">📅 20:44 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105372">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">پرسپولیس زدددذذذذدذدد</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/Futball180TV/105372" target="_blank">📅 20:42 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105371">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">گلگلگلگگلگلگگلگلگلگلگ</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/Futball180TV/105371" target="_blank">📅 20:42 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105370">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8bef49689e.mp4?token=R6FBhehAk9PV6dl0Fsk2AjBUn4V2Kmc73vIT5tZgCmP8uwkXtyz2gJmkgbHh1aCRwaG-YgI8KGL0Sf8KuTKb2ofmmi3x14FmNCx-wu-ejqls4mdM8k9HFjsLQqSGUnCT_uINOw6q9XyZwK1HoaP5vbMm9ISlUUFiJsLzc9dcUfvoinunQj8UsWepxULh10xhbeor2KWHI8hf4TB3otN6A3X4YOkfvEi5ENrmEehRFRfueOOBDHbD-gpntCG24DeB5qAdGujTTMq4y1NfIQzr-oMDR7EP8nuv1iZsseafR2nInp3k9rosoGIrmy0NqczmckPkyiHhVK-CnmmFhT55-Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8bef49689e.mp4?token=R6FBhehAk9PV6dl0Fsk2AjBUn4V2Kmc73vIT5tZgCmP8uwkXtyz2gJmkgbHh1aCRwaG-YgI8KGL0Sf8KuTKb2ofmmi3x14FmNCx-wu-ejqls4mdM8k9HFjsLQqSGUnCT_uINOw6q9XyZwK1HoaP5vbMm9ISlUUFiJsLzc9dcUfvoinunQj8UsWepxULh10xhbeor2KWHI8hf4TB3otN6A3X4YOkfvEi5ENrmEehRFRfueOOBDHbD-gpntCG24DeB5qAdGujTTMq4y1NfIQzr-oMDR7EP8nuv1iZsseafR2nInp3k9rosoGIrmy0NqczmckPkyiHhVK-CnmmFhT55-Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
مهدی تارتار خطاب به بازیکن پرسپولیس؛ پا نشو!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/Futball180TV/105370" target="_blank">📅 20:34 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105369">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4ae4fcc9a0.mp4?token=BME-G4-SJO-aHI2FGK4UwGUm3hX3-SlpMSTxYS0XLGkRz3tawf_-2iExmic-gucrixwZV3dgK6vfP_5jgaffydNs0-5ptW8-Lnm3rXsOD1osNfx0sp6YBB7eBi42lorSCDywL2brrVA9DXpnuB_GYzzVkUqOH9OSCqZJ2WG-4iUY-BHHXaUlPcUw0KUs_hM8KKL3klPX-ZxXrIq8KJn9trx_GS6hii4gOUD_pNlQLpAKRamsG1nWF3CaD0na5xmwVaGqkXWLXoYxH2JROBdVCt4OcfPdODVeE7K1viywgbTM0-rVtkQ-VFsw7IbKD4UkmIVd7oKNXV11upagGGJjlA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4ae4fcc9a0.mp4?token=BME-G4-SJO-aHI2FGK4UwGUm3hX3-SlpMSTxYS0XLGkRz3tawf_-2iExmic-gucrixwZV3dgK6vfP_5jgaffydNs0-5ptW8-Lnm3rXsOD1osNfx0sp6YBB7eBi42lorSCDywL2brrVA9DXpnuB_GYzzVkUqOH9OSCqZJ2WG-4iUY-BHHXaUlPcUw0KUs_hM8KKL3klPX-ZxXrIq8KJn9trx_GS6hii4gOUD_pNlQLpAKRamsG1nWF3CaD0na5xmwVaGqkXWLXoYxH2JROBdVCt4OcfPdODVeE7K1viywgbTM0-rVtkQ-VFsw7IbKD4UkmIVd7oKNXV11upagGGJjlA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
طرح هواداری دو تیم روی سکوهای نقش‌جهان
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/Futball180TV/105369" target="_blank">📅 20:26 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105368">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1a8cd40ab6.mp4?token=aVr2PdyfSYaiyOe-VTppd-zvSbtVEJlo-GBPvfvRWzF1-dtItRAPlAumwUvErMpZE1yx-s01ZD723fHbpnBbncmErbMj1tKkPcJ14QUJPHD-kmxnrlTonZNkrasWeF6ELCWhVDhM6-omvByjKruXfZzMVQdBOVzfHYW3bL28Jhm39yGpA2qa3bPDeH2lA-ksjXnB4EdxqX9QLsjwr7xJriXETSkcmdiB4jf8M5fECNZRApSgaWmr3GsMz-84yKDDMA0kgbfxZEmitL28Lqg-X3bB9T8gvZwFXMfLBpUeWqC2NRkoxT7PAa0yZC9-r4eHUzI1GquXIQs6t-sh4Wjn3g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1a8cd40ab6.mp4?token=aVr2PdyfSYaiyOe-VTppd-zvSbtVEJlo-GBPvfvRWzF1-dtItRAPlAumwUvErMpZE1yx-s01ZD723fHbpnBbncmErbMj1tKkPcJ14QUJPHD-kmxnrlTonZNkrasWeF6ELCWhVDhM6-omvByjKruXfZzMVQdBOVzfHYW3bL28Jhm39yGpA2qa3bPDeH2lA-ksjXnB4EdxqX9QLsjwr7xJriXETSkcmdiB4jf8M5fECNZRApSgaWmr3GsMz-84yKDDMA0kgbfxZEmitL28Lqg-X3bB9T8gvZwFXMfLBpUeWqC2NRkoxT7PAa0yZC9-r4eHUzI1GquXIQs6t-sh4Wjn3g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
موقعیت خطرناک یاسر‌آسانی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/Futball180TV/105368" target="_blank">📅 20:14 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105367">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a811272008.mp4?token=d_0YvEIH6yZYNXrmgUNF5sO0oAv9UvjB_pwYI0ZBbRFDbsIDw17HVMgEAtlLYTNc0JR92QxBKER592lvGv6uZx2j0Pv-jVQEq7-s4Z9J0dnBYwc8uNwsercFONrVFI5ijW0S3MhJxMuE9ItI6pinK0GcZnQ6HMoD4sbv5Co5fg0bdarqXDT2n_4JGoluwn_nsmHZfZ5-D9qaLSA3mXw9LQ7JpcSDnUVUW3hwV4q3folUT1agRg1s4Wj9ObFzXI2dqyJIPnwy6NTLAmTIb5Oqe5qtQRMpkhMFa2eAmtkve_9-Ta-930RsmPDixPaPxI97Er44n0CTPhVUg_8BOoDKnA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a811272008.mp4?token=d_0YvEIH6yZYNXrmgUNF5sO0oAv9UvjB_pwYI0ZBbRFDbsIDw17HVMgEAtlLYTNc0JR92QxBKER592lvGv6uZx2j0Pv-jVQEq7-s4Z9J0dnBYwc8uNwsercFONrVFI5ijW0S3MhJxMuE9ItI6pinK0GcZnQ6HMoD4sbv5Co5fg0bdarqXDT2n_4JGoluwn_nsmHZfZ5-D9qaLSA3mXw9LQ7JpcSDnUVUW3hwV4q3folUT1agRg1s4Wj9ObFzXI2dqyJIPnwy6NTLAmTIb5Oqe5qtQRMpkhMFa2eAmtkve_9-Ta-930RsmPDixPaPxI97Er44n0CTPhVUg_8BOoDKnA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
فرصت عالی علی علیپور به بیرون رفت
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/Futball180TV/105367" target="_blank">📅 19:47 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105366">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0a4f888f78.mp4?token=ZAebbSoYXBxu-sRed2S5nYM4iZaoJGCO43htYdNHxWdofcNT3H1QILNU4y0BPCLbMuF8_00SIwIyoVKHdjLJ459q_fUu4LLqyangIRW4dGKnUjoxKIiyUFC1dlz1kZLrJi8NZWEQU3EnD0WmSJLtmIZMyjZccZeluhjecppi3sh01t6WvZjE0r5XrWqb_fRUrl7j_qiWvNtSU8AtB1IXR7Kbg-UQD9cmSEG5codEURtHJrf9VcWk2TC0O4c71q_xpJetTVu0wyajhRWPXgr_rc6blsrP_Qk_eHEvzN_R16yO9WUYBihFlxyIJJ861aZvhT4c2v82kVQyTWtdzCdE8Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0a4f888f78.mp4?token=ZAebbSoYXBxu-sRed2S5nYM4iZaoJGCO43htYdNHxWdofcNT3H1QILNU4y0BPCLbMuF8_00SIwIyoVKHdjLJ459q_fUu4LLqyangIRW4dGKnUjoxKIiyUFC1dlz1kZLrJi8NZWEQU3EnD0WmSJLtmIZMyjZccZeluhjecppi3sh01t6WvZjE0r5XrWqb_fRUrl7j_qiWvNtSU8AtB1IXR7Kbg-UQD9cmSEG5codEURtHJrf9VcWk2TC0O4c71q_xpJetTVu0wyajhRWPXgr_rc6blsrP_Qk_eHEvzN_R16yO9WUYBihFlxyIJJ861aZvhT4c2v82kVQyTWtdzCdE8Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
🇮🇷
بهروز رهبری فرد: خیلی دوست داشتم که جلالی در این بازی باشد چون نقطه قوت استقلال همان سمت است
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/Futball180TV/105366" target="_blank">📅 19:28 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105365">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KYmWye0K-mxnIW4gdetwwifNFQXA-Vv2EPar0R5ZRqppqfpNPYMMdrZjansSrawdwzFn1ZsdY8JmV5vuhWcDoXHNCWMASdDZG2nm3CdOw-wKG2uxp_G_37KsE10XsSUvb9MBGevjCoUHzNnXCi0kJHaiABp6hVTjGezsE19gpb5SjFHZ4H4VC9nV11OmRKFPkVi1yVSxLoNUirDB3-0w4CBUFCwDt5kpPk1EqzZIS2ZWsmxhmipPO_BSOUikdBydJr97SSzqgx_yyhy5s40aeosy9ESYi1MzIvOH8jUmigNqEoe0uXysejr3M2CQK1v31j9Q5IiFr1fBtXEB0TmKKg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🇮🇷
ظاهرا جدید صالح‌حردانی در بازی امشب
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/Futball180TV/105365" target="_blank">📅 19:09 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105364">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/04c8c7c65b.mp4?token=dwWq4TYkgFXsZPUGBQXg7eoODHdXGuyvH7WLl3s9QD1iHsOXXBfPxvn3ng2wQxYlb1t5iW8Q2vmqPXpysLvvNI6qI4kLuPOMcsvoCwTk89qg0mEFvWFPXyUuRRnKCVpeyeWWMKrVIkVG3jfRo8h-dlUT8D1raZOvydVGaHGW7rCzd0s-OE-UddqoXZhysuYKVbE7j-YmrDBAG2191QkUxq2-Uczh7fkstgonMkrbVJh_eTTuu2cLMhby70tmldaUUg5BtdSBwfRVm1s2Bsakz4vAXOjYYWAgQCVDgDvc2sDMX6NrLUCUfvPoJfU1pvE6hOyHQHTIXdXs9b9v6XT2TQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/04c8c7c65b.mp4?token=dwWq4TYkgFXsZPUGBQXg7eoODHdXGuyvH7WLl3s9QD1iHsOXXBfPxvn3ng2wQxYlb1t5iW8Q2vmqPXpysLvvNI6qI4kLuPOMcsvoCwTk89qg0mEFvWFPXyUuRRnKCVpeyeWWMKrVIkVG3jfRo8h-dlUT8D1raZOvydVGaHGW7rCzd0s-OE-UddqoXZhysuYKVbE7j-YmrDBAG2191QkUxq2-Uczh7fkstgonMkrbVJh_eTTuu2cLMhby70tmldaUUg5BtdSBwfRVm1s2Bsakz4vAXOjYYWAgQCVDgDvc2sDMX6NrLUCUfvPoJfU1pvE6hOyHQHTIXdXs9b9v6XT2TQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
⚠️
😳
😳
به‌قرآن خاک کسخل‌خیزی داریم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/Futball180TV/105364" target="_blank">📅 18:57 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105363">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7da52ed6cf.mp4?token=ULOXbaXjAX7wEMOTSuqH8OOFVuTZOOztfbTEFJBEDIBTX_MXAJ42G8TUT4plEmYut5_luhDYxXTvReKyS4_7SJ8Ww1-7OqkAwfkrBwPY58oYCm8BvYrSR2EEvT2WAEl3612ZTXzwp2gQYw1Wl40vxVasHlwOAJ4atmsq13Uu7DNrphC8fY3nYAhgXk0mKbuOS53ZDLlZoQnPRY1RharkjBm94SHjK8_9kWaPA8-WAzvX3NWNixMqeN1OA3eZm9XglrOwfq4dflODeJxR12NmwQ5voTEbQza2yALagZVKt2pQP-rebxvaedG-T8dFJtJQBXJq0FGRGUjUvget27yEpw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7da52ed6cf.mp4?token=ULOXbaXjAX7wEMOTSuqH8OOFVuTZOOztfbTEFJBEDIBTX_MXAJ42G8TUT4plEmYut5_luhDYxXTvReKyS4_7SJ8Ww1-7OqkAwfkrBwPY58oYCm8BvYrSR2EEvT2WAEl3612ZTXzwp2gQYw1Wl40vxVasHlwOAJ4atmsq13Uu7DNrphC8fY3nYAhgXk0mKbuOS53ZDLlZoQnPRY1RharkjBm94SHjK8_9kWaPA8-WAzvX3NWNixMqeN1OA3eZm9XglrOwfq4dflODeJxR12NmwQ5voTEbQza2yALagZVKt2pQP-rebxvaedG-T8dFJtJQBXJq0FGRGUjUvget27yEpw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
⚠️
🇮🇷
🇮🇷
هوادار استقلال به سبک هوادار معروف غنایی در جام‌جهانی، با طلسم اژدها وارد ورزشگاه شده
😂
😳
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/Futball180TV/105363" target="_blank">📅 18:51 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105362">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4866011c8d.mp4?token=F5Kxk8AL_z68FQfb3fh6ieGSw70aEmtlwgK8Cct5znZ64KWDse-1WZOLDOqSPQqSi_QQTLItnRh4pOrmOd2dZ6yBDy1gpWn0RaKmjGRCnkFsVyWmHmNoFAgQcx_4ww_53b8CkAW8HGmzyD6qHDst8XWx9fO3fUDU0Nm99wsX_R8AtjwKBe5S8JdkOq0h-GCngUr5suwOOfzbaMLcpbVFzanjjQrpzFiuSDE1btLToZSSK0KdMyBqdAJpZ0o7z7H1s6BS7hrkWk9n-rwYVN1YNXsTk-GH1gv4hIElv0hLRsd-wa4YO_VakKFz45I2XeKVItBRNcfTShSfmy5c5d_IPFQCudC6I345GVD1BBuuk21ciyG5deR_1TexdDy7J9jjMRRMzDKLQTKqK_zrA7grIzd5vq-YHHuobXuv2NqlqjLmpSuO00kumPNHUAuKCyzWCvgA_fRrRXXIGHHlAAd1jBwouPFFxxV0YUiXai-TPnxhBu2UT6xtt_Ocmye__J291qpDVcTpqpEAtiappxO9cYdeTiSspmfuwOZGJxeNzukwbrvagpO4ZFhb-LmNyon8YdBX1-HYITffx4WFKQ1IbA-W_lqGsu9A_ZGQ2KPbMw4D1RU656jROt9Nu0PlZ7sSSekPwfaEpsoTLwbU6T7W5aZ71J3yfpjrhuw_dXKEzNo" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4866011c8d.mp4?token=F5Kxk8AL_z68FQfb3fh6ieGSw70aEmtlwgK8Cct5znZ64KWDse-1WZOLDOqSPQqSi_QQTLItnRh4pOrmOd2dZ6yBDy1gpWn0RaKmjGRCnkFsVyWmHmNoFAgQcx_4ww_53b8CkAW8HGmzyD6qHDst8XWx9fO3fUDU0Nm99wsX_R8AtjwKBe5S8JdkOq0h-GCngUr5suwOOfzbaMLcpbVFzanjjQrpzFiuSDE1btLToZSSK0KdMyBqdAJpZ0o7z7H1s6BS7hrkWk9n-rwYVN1YNXsTk-GH1gv4hIElv0hLRsd-wa4YO_VakKFz45I2XeKVItBRNcfTShSfmy5c5d_IPFQCudC6I345GVD1BBuuk21ciyG5deR_1TexdDy7J9jjMRRMzDKLQTKqK_zrA7grIzd5vq-YHHuobXuv2NqlqjLmpSuO00kumPNHUAuKCyzWCvgA_fRrRXXIGHHlAAd1jBwouPFFxxV0YUiXai-TPnxhBu2UT6xtt_Ocmye__J291qpDVcTpqpEAtiappxO9cYdeTiSspmfuwOZGJxeNzukwbrvagpO4ZFhb-LmNyon8YdBX1-HYITffx4WFKQ1IbA-W_lqGsu9A_ZGQ2KPbMw4D1RU656jROt9Nu0PlZ7sSSekPwfaEpsoTLwbU6T7W5aZ71J3yfpjrhuw_dXKEzNo" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
🇮🇷
شباهت گل‌های این فصل دو تیم به گل‌های به یاد ماندنی داربی‌های گذشته
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/Futball180TV/105362" target="_blank">📅 18:49 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105361">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MdICaVspJz0pJuSt-_lXaMH46ICIy1eRtjcVBHskwmBr44fIWmgXMvvolmpbCLGSbPwMr24-4Vymw_GfFPa92IiHYHK_k0jrwlG0tGaAcrysinfIrUF3_POq9aeyt0vMPrJlH-cc72lnx8vxSiM4Sf7FeNjFb0mQRDrsWBOygANgjhRqFaz3xv_2hd-m3kYyFwV8z4RdeHHubSkj7t0vVxdd6GJA8M4Gw3wsdC5iJ6hP0fiooHTtlIJ2izqPY3yLT5dFvKwKZe1-rch5sBtR8Opx850bA68OUJC_572Aj1lrDDzdh1lGl0P6iKmmC2E9uaNwFehKFVvyQ8jcWuQL-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
🇮🇷
🇮🇷
لیست‌کامل بازی امشب دربی پایتخت
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/Futball180TV/105361" target="_blank">📅 18:42 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105360">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e961f8ed7f.mp4?token=BjrOPPg3WMuZC7n9XoNLlEKm5MUtQFrTA0CDdnFcRBRnMlzOfLFVV5bwRrYP_9zmped5E4GGP3DxqTIcDoENz3FxYcNuSH44afBwmBjTAgdSRy3TdCgmyzTGylj5JFuVtt1Gz8n60Uhc_fPUY6Vk0Lwx0KV1vnAE50_RBF_WxHIuMdOeSUYNbkuHXJOG2tRDFoQnPDWgCJp6opSLjwvu9m7__udiL2R8q1tphh0Fo4KIlJVIp5zikG76M4kRYy4gsaC2RnyIsaEX6kB_f57mHJRteUIMW3OYO6D2l61naw6hxSU7oY4s0Linjyjh-nbIRFpxli4nOerR4KGUoRRM7g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e961f8ed7f.mp4?token=BjrOPPg3WMuZC7n9XoNLlEKm5MUtQFrTA0CDdnFcRBRnMlzOfLFVV5bwRrYP_9zmped5E4GGP3DxqTIcDoENz3FxYcNuSH44afBwmBjTAgdSRy3TdCgmyzTGylj5JFuVtt1Gz8n60Uhc_fPUY6Vk0Lwx0KV1vnAE50_RBF_WxHIuMdOeSUYNbkuHXJOG2tRDFoQnPDWgCJp6opSLjwvu9m7__udiL2R8q1tphh0Fo4KIlJVIp5zikG76M4kRYy4gsaC2RnyIsaEX6kB_f57mHJRteUIMW3OYO6D2l61naw6hxSU7oY4s0Linjyjh-nbIRFpxli4nOerR4KGUoRRM7g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
‼️
🇮🇷
🇮🇷
یاسر آسانی رو به هواداران پرسپولیس کری‌خوانی را آغاز کرد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/Futball180TV/105360" target="_blank">📅 18:38 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105359">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d420dd3220.mp4?token=Yol7NgM6wv6W0c2yuyrp9WWA_BQY0aK3QwgOas0pgG8qt4G2c3cYoON2MlzNWKwpGP084y_U5dGxKbTnEFGgl8tJIQAwhH9theHbcHShM1xcCRvU1Jr9j0KxQgi22tczAa-Vdm0wQCWUvI6VKseUpoeXtB3ahlKyIMYo-eW-Nt1P0uxDIGjMmkp0_EIBFP55wKi1o_b4r4p5z3-JRXnOp_hPERMK9wWMzvD4nMPHcgio6Cb7ZjfsuqscUr24P2_a6TDdtdF_pGOrJxlF2hnjkIZXe3hD4b62SByVjgCLin4Ah3xWSNMCXaI-t1wONs6VLOpphQ2tQmtCY6zI8cpyVIWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d420dd3220.mp4?token=Yol7NgM6wv6W0c2yuyrp9WWA_BQY0aK3QwgOas0pgG8qt4G2c3cYoON2MlzNWKwpGP084y_U5dGxKbTnEFGgl8tJIQAwhH9theHbcHShM1xcCRvU1Jr9j0KxQgi22tczAa-Vdm0wQCWUvI6VKseUpoeXtB3ahlKyIMYo-eW-Nt1P0uxDIGjMmkp0_EIBFP55wKi1o_b4r4p5z3-JRXnOp_hPERMK9wWMzvD4nMPHcgio6Cb7ZjfsuqscUr24P2_a6TDdtdF_pGOrJxlF2hnjkIZXe3hD4b62SByVjgCLin4Ah3xWSNMCXaI-t1wONs6VLOpphQ2tQmtCY6zI8cpyVIWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
🇮🇷
🇮🇷
سیروس دین محمدی: قبلا اگر مساوی می شد حداقل ما همدیگر را در زمین می زدیم جذاب می شد
!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/Futball180TV/105359" target="_blank">📅 18:32 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105358">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/if_5M0x9dD5muz43LlGJxE535o3uVrVNhf283hrZmLSdIgmIGCh_A6NEc0lI0Eb_0dnDb_Svak-NHlA8mP_yyCvhNH0M61Cstz55_L5PqdkvOMiqYES9_xKIx-FByxTCuF4Rm7ALlpv5t7fkU8i70HS0tZxj3EkDaQXtEro1v3uA6KyRXwQD4va3SCbYA-C2LmGYVJn7fkqDu5z4a2QomrS8_Ade0PZtVR4CPe5j0FxNx0OEYNpoQyGXL3EjdLGNlc7-NJRBrZYovLGA05Oz5y_qDO9pNdvlyfLm-i7EKmvuqPDsQS5HuUe5AFz-cfaFU2OQQY6vN0i-_a9J8yWq5Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
📊
مقایسه نتایج سرخابی‌ها در دربی پایتخت
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/Futball180TV/105358" target="_blank">📅 18:27 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105357">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/Futball180TV/105357" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/Futball180TV/105357" target="_blank">📅 18:27 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105356">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZvDtcX6W_A9T-zRTU37BryHD4AXZVdmjtYC80MsXilEaDVoqP89kEfha_vcQ4nmmEQxg5e6-9xSMyU08GOJ0vInHFcpP_LtI5ojwEDTZXaln4p3uGea8zcL4A7VxeA4kCVF9qJdwHdoC4TVFajEIpQarU5uL9d3AtY4x-QsFMk2xvYI7OWLuo30EbDRy_icHkGDL3uQfP8c3nfKWPMvMWtCDBApUERwdQ2OeI82eW5-nXeXb4c7SVTcSQT5vpYiOjgdtDAyCZ9GYHByl0-3KOoMUqTgcfQD9Yzm5lt_saOd1kki9FCuChIsAnNv9VCIRyhLRgoJXoI9e_TlQXB2kzQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
استقلال
🆚
پرسپولیس
⚽️
پیش‌بینی دربی رو در
TrexBet
از دست نده!
📉
نگاهی به 5 دربی اخیر:
2 برد پرسپولیس | 0 برد استقلال | 3 مساوی
4 گل پرسپولیس | 2 گل استقلال
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
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/Futball180TV/105356" target="_blank">📅 18:27 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105355">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ubF7A2_Z93X76rcojDV-9EBWiDwwHtXTfjp_aL-KCAseQj6G__GxfY7X0XVxZ9Rmsw6AJnZkjsbo5S61tJ7Hv1artdcBgMfsaKXxNeO25jiltR0AsbBgcpgvPGbjOJtISBSrCk9VnfB21av_hbONewxVm0BZk6FjIU7k573CRnwl7MNKwsnphZ2Ots0XknfXKsPZqpm9VLL_UrWlv-_5k3ptW-avHFZUjhxpysWFgQ6dwly_xkD9F3PQapTNgYZkijEk1dbiPbR9Pgdo_veTHBotU8y-9fg-UwXUgIkJebitzZ3UlknxSATY_msbwFjiOD7wNXRmkroBBjARQGC_1g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🇮🇷
ترکیب پرسپولیس مقابل استقلال
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/Futball180TV/105355" target="_blank">📅 18:24 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105354">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WUXskPEFUAetdW6yJEEl10jg6GUt0QRSUVHJNS8yuLyav98ywL_RtcWS2tmAopEiVnHMu-m_8BwZoVvBxFlAj5DJt9IHOMQqpsDHfRNqxKoD1tSYOYCDmBvojZ9BvZ0slLShlwOHHZkSYNfdMyrPL97dF1P5jhrT2PWiImdBwL6C6dcON5RTiPhIHf3G4o3kIBLLqYQZvhlRpYHuWk0FNgfhOLb68JF8ZA6fbwT2fCAQq6XmU9FtOUIsoI1NeYYf7BsY7RRGH2Ms447Y6DT60BsX2Qed2TRvdMaxN6Jhf9f62cmJe7spb4mpGsSy8g5qOEQxr3acSi1jQgBdEkd6lA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🇮🇷
ترکیب پرسپولیس مقابل استقلال
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/Futball180TV/105354" target="_blank">📅 18:23 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105353">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/T7n6w4dLHO0Re_1F6TcSe00Cf1xDWT-lUkWOebMneqs1uyzYiNyM_GLB-vQoyz7_0uwjfkzX8VlFONfu3UKlVq1RBW20Cit-M_jcwvswvxMBTrOm_K7HE3eMVUTIhcVZSsaQ0rvaCvUtSM7Jl3ALtkXBCPGDISHZgE-DsLS7sqm2c9e8njfKnRryxoSt33HyKbnO-J7zeLib26SNY-k6QOwLMf7uwpjbf4WZHwGeJIVAwsthjYX03kz9bCOMG8uC1gJsiIR05Usl9Uz9tbJh-DCbRyscP1MxlcWazNv2JJ-hhfOt7a4PR9UZB1yFN2F6wpIb-sKegdSFpS4NdpCtfw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🇮🇷
ترکیب استقلال مقابل پرسپولیس
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/Futball180TV/105353" target="_blank">📅 18:21 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105352">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CQmfDUMjbpviSz_ObESjxYkEqCK-V2WsOMu4-KniFysQy2FaCm5kQDGfO0i0M0d26nI9b793cpifBq51tZ6Ay9-Zzoh8aJjMuK2me1sRV_HFoTQjKCgMYiPw3jatA2rtyyk7Ed3PMFtCHlOYEoBBItVdhFmVknR0LHsUMlpLPdvPqCUw-SLwADx9xM6YHf9BWYH_gNHbfGfm2ZtysnDQOWGTP7yEp2ZjuL9zNeWVtHdWVPzyaU1n4uCtSyE4GG6vBorDKalAos_JVBQnofDmP8DzXjkUAnP3gk6aI3jD9Xopn8gSNB0YgaLQxn0Yt7fyVaNmuNrGOlwz9QsviF6VbA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🇮🇷
ترکیب استقلال مقابل پرسپولیس
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/Futball180TV/105352" target="_blank">📅 18:19 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105351">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d4a83d7c6e.mp4?token=ZN4mri0QanzYweMZlnZ_zw70RZtqHqWX1YhuAmjinw2Le6R4-RdVLcXt06ZX-kBdSfiCWPymTB8pjdxmfx3L6jKbk5lzXlLiu0YCkXbDuP6eYnOyzjZIXztSfy_-hwcUNWXkrp5baHdZfnumRGmnfupqjyjkMUkbDyfdoyPpBJC-B-g3rxavOQpJoifRpwcb5gOe8pXPdeLZU5AiZUZUyArRLSEoB0k68JZHrTjcimaKVUjf4aJdE_cxi9zC3hcA7ykqkMAOMo8SoDFPwWK3Al8WH5Nr3Ff7qgMrHOzvmJ9vBiFzLiWDYVj1U8CZe9cC4rYzk38PKjJZq7aS4g7Hpw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d4a83d7c6e.mp4?token=ZN4mri0QanzYweMZlnZ_zw70RZtqHqWX1YhuAmjinw2Le6R4-RdVLcXt06ZX-kBdSfiCWPymTB8pjdxmfx3L6jKbk5lzXlLiu0YCkXbDuP6eYnOyzjZIXztSfy_-hwcUNWXkrp5baHdZfnumRGmnfupqjyjkMUkbDyfdoyPpBJC-B-g3rxavOQpJoifRpwcb5gOe8pXPdeLZU5AiZUZUyArRLSEoB0k68JZHrTjcimaKVUjf4aJdE_cxi9zC3hcA7ykqkMAOMo8SoDFPwWK3Al8WH5Nr3Ff7qgMrHOzvmJ9vBiFzLiWDYVj1U8CZe9cC4rYzk38PKjJZq7aS4g7Hpw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇮🇷
😳
ترمیم‌ناخن‌های علیپور در آستانه دربی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/Futball180TV/105351" target="_blank">📅 18:12 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105350">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f9531a98f1.mp4?token=bvXP2pLcGqO3aWbNSx3ltpHHcVii5IIu0vGv7V-IOnCWCjVQqC1_tohGC1qyekVxenqxHmnlirmCqSSvGao4xgS-AW6qpLTGS546ZdOZ51QhgJlb7TnQB72N7t_kjo5DpUWds7Zrg3DBzP0nlWxqy1nfx_RB-qqaqrbgtNn8OtUU6cKuvkfJoJjeAlDJFTDZSEqGtOXraYXT_SkVN1-jGnAkCk7ngU5BoVb7DqLpQsqwqfn4VuMs8S7salmGJ9gEnyw2Q6SX6MgQzDPtgMrL8ITynaieWZ9B4ez94DT9MPteQO-_J0NC3ObXq1wvFxHt_xI1BMtJAmhiO-viJPfnKqgWWhYJw4W_LE7jAmDRYJRANwWzu4m2WHg-hvNr0CHvAZZmbLUcfCl8J6WpCYgx-dxsLVJwJhL19nr-1Xl8pNsrK5AyAqYgtofxRjs3KpGuFoOZTp49ea0Hm5PHxcLLijN4VBVLbO_8bkkGdZc56enzJcirmEe1Ry4M49cE93V7GYm87a6g5inOj6Hcd1KfU8WFdrgSDAJLHG5ggBGhWapYYd7vzx1-PFFLZE5R9GVgI2nK1Zxy8lkv8l1R-9gzzpw7CVFQGWlfnIBcDGjchM51YMYjlOtwlQVapmGFqdCKgfOsPgNaWhFdZynwWDOx38RzkvgGXEhD1hoQK9_rVww" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f9531a98f1.mp4?token=bvXP2pLcGqO3aWbNSx3ltpHHcVii5IIu0vGv7V-IOnCWCjVQqC1_tohGC1qyekVxenqxHmnlirmCqSSvGao4xgS-AW6qpLTGS546ZdOZ51QhgJlb7TnQB72N7t_kjo5DpUWds7Zrg3DBzP0nlWxqy1nfx_RB-qqaqrbgtNn8OtUU6cKuvkfJoJjeAlDJFTDZSEqGtOXraYXT_SkVN1-jGnAkCk7ngU5BoVb7DqLpQsqwqfn4VuMs8S7salmGJ9gEnyw2Q6SX6MgQzDPtgMrL8ITynaieWZ9B4ez94DT9MPteQO-_J0NC3ObXq1wvFxHt_xI1BMtJAmhiO-viJPfnKqgWWhYJw4W_LE7jAmDRYJRANwWzu4m2WHg-hvNr0CHvAZZmbLUcfCl8J6WpCYgx-dxsLVJwJhL19nr-1Xl8pNsrK5AyAqYgtofxRjs3KpGuFoOZTp49ea0Hm5PHxcLLijN4VBVLbO_8bkkGdZc56enzJcirmEe1Ry4M49cE93V7GYm87a6g5inOj6Hcd1KfU8WFdrgSDAJLHG5ggBGhWapYYd7vzx1-PFFLZE5R9GVgI2nK1Zxy8lkv8l1R-9gzzpw7CVFQGWlfnIBcDGjchM51YMYjlOtwlQVapmGFqdCKgfOsPgNaWhFdZynwWDOx38RzkvgGXEhD1hoQK9_rVww" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
🇮🇷
🇮🇷
کری‌خوانی بازیکن اسبق پرسپولیس برای امیرحسین صادقی: آخرین باری که استقلال دربی را برد، دلار ۴ هزار تومان بود!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/Futball180TV/105350" target="_blank">📅 18:06 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105349">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e8a801f0de.mp4?token=tz2Cdqw3Od6Ymj0cwJk1pp3aVVCyW0qNWI77MInITv751DpuFiaP6l6_PIP9bclqPebtrmW3LUUK8Y5Vgslt8exkIytWgPxzpWt-_NeRfscf9Q5Fy614qK2WM4iY5ghwsKVstNvbRy4jgw6kZRXinxaEhA_LmY9g3eiFbhsn7_7yjtcOl6uK-Wd0d1R5IldtKuC8zyO2E4pEGUC3tou_AJsNuQKbKJLINRQGnD09rq6f6Pn3VPQOoAqel_B80K-q0bPYnijhFBegBdn0KXCWAVpRzCVOdVfNd7IuGi96uOe3mmlNe41MRjbV5DogGuP7AWtHXbLD_mZK_kIFEWfzdC_A-ZWfPW3qHSK7i-ygEKMEwpV0T2FiVZzmra18qBCIF6PrSSGMlemGEhQZ4pHgztUUIhwrwm6VrstepnpoHxmrdJnQiVqgoV9uYk0zDrm6Y3tA95PzJGnWYrCK6iyHS18albVv9cNuOJm05fVagZ07pIo8vXDt_czgdFl2SRgOOJBBiQkTSPo1ytTyaW3wsBydhO-XOQARYkCesDRiubHcJ-DkR2IwzB503qi0HP64xgko6BuApTh7l0BlAo9wXY21wpTAhFCPgHaSUuaYK6NH_IThIHVEHc5uhqAkiVufeAVYJr0Z9u4xKnKJmKzZ1VMEwKsqNem2LcgRXlCK3no" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e8a801f0de.mp4?token=tz2Cdqw3Od6Ymj0cwJk1pp3aVVCyW0qNWI77MInITv751DpuFiaP6l6_PIP9bclqPebtrmW3LUUK8Y5Vgslt8exkIytWgPxzpWt-_NeRfscf9Q5Fy614qK2WM4iY5ghwsKVstNvbRy4jgw6kZRXinxaEhA_LmY9g3eiFbhsn7_7yjtcOl6uK-Wd0d1R5IldtKuC8zyO2E4pEGUC3tou_AJsNuQKbKJLINRQGnD09rq6f6Pn3VPQOoAqel_B80K-q0bPYnijhFBegBdn0KXCWAVpRzCVOdVfNd7IuGi96uOe3mmlNe41MRjbV5DogGuP7AWtHXbLD_mZK_kIFEWfzdC_A-ZWfPW3qHSK7i-ygEKMEwpV0T2FiVZzmra18qBCIF6PrSSGMlemGEhQZ4pHgztUUIhwrwm6VrstepnpoHxmrdJnQiVqgoV9uYk0zDrm6Y3tA95PzJGnWYrCK6iyHS18albVv9cNuOJm05fVagZ07pIo8vXDt_czgdFl2SRgOOJBBiQkTSPo1ytTyaW3wsBydhO-XOQARYkCesDRiubHcJ-DkR2IwzB503qi0HP64xgko6BuApTh7l0BlAo9wXY21wpTAhFCPgHaSUuaYK6NH_IThIHVEHc5uhqAkiVufeAVYJr0Z9u4xKnKJmKzZ1VMEwKsqNem2LcgRXlCK3no" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
🇮🇷
هوادار پرسپولیسی خطاب به استقلال: دربی اصلی ما با پیکانه، شما ده سال مارو نبردید
!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/Futball180TV/105349" target="_blank">📅 17:57 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105348">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7c2dc5b376.mp4?token=q4hnUw91OUXVWjvykDXaQwr14Y7kuvqhMgHwZzXUFNTNs8QklEnE8L4_KanzpRDNNglkEvLsjlQGSQpPYM3rK3rf1os539DImV5cFQGwBh6GvgM5yY9mFLozUd5wX9kTYW2u717YmQuckRdznrB0H-zEIsjNfvxTuHGrc0O_xjV9VRPod3QQAxVSm3B5LN8_FpzjAGzxLO1L0uUP__8TKOds_9wtBpky3QwlZNEisPwVDqiwRqBHpitm9T5WHLnEHFA4cRLWaxZ0Ft-REiGuNsOhqqLKxw63YSM35ptSrXjkURDQ0ImhvIprVJX9CXnxZUqtYxdOV5JFzt96vO1NDw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7c2dc5b376.mp4?token=q4hnUw91OUXVWjvykDXaQwr14Y7kuvqhMgHwZzXUFNTNs8QklEnE8L4_KanzpRDNNglkEvLsjlQGSQpPYM3rK3rf1os539DImV5cFQGwBh6GvgM5yY9mFLozUd5wX9kTYW2u717YmQuckRdznrB0H-zEIsjNfvxTuHGrc0O_xjV9VRPod3QQAxVSm3B5LN8_FpzjAGzxLO1L0uUP__8TKOds_9wtBpky3QwlZNEisPwVDqiwRqBHpitm9T5WHLnEHFA4cRLWaxZ0Ft-REiGuNsOhqqLKxw63YSM35ptSrXjkURDQ0ImhvIprVJX9CXnxZUqtYxdOV5JFzt96vO1NDw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
🇮🇷
کری‌خوانی هواداران کودک استقلال برای پرسپولیس: ما با پرسپولیس کری و دعوایی نداریم؛ پاس رفت آسیا قهرمان شد اما شما نشدید
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/Futball180TV/105348" target="_blank">📅 17:53 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105347">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4634665f37.mp4?token=Ypt8xhLYE6NDAk_b2j98Oxe0VElxQktWHPG4Zm2ZYEff2b9UI0JPlA02FGJnBF-D5Kj3BAN7eA9TFuATexg5SDEiSR7lz4uGnvohmoqRdlQLdPD8S6JaEqt0vqsqdoSAjUjSDPiUsm6P0-8VCs0eN1oN0j4fDx-sZBHJZA1dnwZ7sh8vHy7A7tqRTxj7iZBtKfCKQkGJDi1qXv1pKzbJ_pTCeiDUb0zlg_pKPBpUKaDwT946tghgWlH2jerOBzvT6mPQa18y-F1bVMDtTPAa7GvM1k3-ysrbZHn2DVl3bb3Bsl6c2fweN538Xor8uGsj5tmWymx_vTgLkK87YlKMmg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4634665f37.mp4?token=Ypt8xhLYE6NDAk_b2j98Oxe0VElxQktWHPG4Zm2ZYEff2b9UI0JPlA02FGJnBF-D5Kj3BAN7eA9TFuATexg5SDEiSR7lz4uGnvohmoqRdlQLdPD8S6JaEqt0vqsqdoSAjUjSDPiUsm6P0-8VCs0eN1oN0j4fDx-sZBHJZA1dnwZ7sh8vHy7A7tqRTxj7iZBtKfCKQkGJDi1qXv1pKzbJ_pTCeiDUb0zlg_pKPBpUKaDwT946tghgWlH2jerOBzvT6mPQa18y-F1bVMDtTPAa7GvM1k3-ysrbZHn2DVl3bb3Bsl6c2fweN538Xor8uGsj5tmWymx_vTgLkK87YlKMmg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇮🇷
🇮🇷
🔥
نمایی از ورزشگاه نقش‌جهان
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/Futball180TV/105347" target="_blank">📅 17:52 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105346">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1699b2c157.mp4?token=k07r2RXdRHXaglyGVe9OAS1i6levFz0u4-oFLVQz_q981ZPyJtrd8YfphTSookJv1WhN0W9GqdxcuuT0aQs6pqzLr1cSoFrrNLbPBh924EzWnj-NFUWJqk0N0VeNzssi0utSnhjKAonV24g73NyF1VVHw9Sg46U-9gTDBfU3bqzeQj8rafUtOjLsYkxQImWsXTIcJlOE9ry3zHWOrp2x6_ztOXQALdnTdzA1eaQfxSC_7bPfflhliRnSkzy9ITBG1xQ4PX5XuT9_pgnTbvHbvF0DNvH5h1XGBQCvHLB4JSw79fcwl1AnkMUJ3jpsrprv2zTzmGGI1wfaOd27v7wyig" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1699b2c157.mp4?token=k07r2RXdRHXaglyGVe9OAS1i6levFz0u4-oFLVQz_q981ZPyJtrd8YfphTSookJv1WhN0W9GqdxcuuT0aQs6pqzLr1cSoFrrNLbPBh924EzWnj-NFUWJqk0N0VeNzssi0utSnhjKAonV24g73NyF1VVHw9Sg46U-9gTDBfU3bqzeQj8rafUtOjLsYkxQImWsXTIcJlOE9ry3zHWOrp2x6_ztOXQALdnTdzA1eaQfxSC_7bPfflhliRnSkzy9ITBG1xQ4PX5XuT9_pgnTbvHbvF0DNvH5h1XGBQCvHLB4JSw79fcwl1AnkMUJ3jpsrprv2zTzmGGI1wfaOd27v7wyig" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
کری خوانی هواداران زن دو تیم پیش از دربی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/Futball180TV/105346" target="_blank">📅 17:33 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105345">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0ef377348e.mp4?token=SfjePOtvov_sehgC9fv9h8X4C_Ip5c-QNkU3RBBYHJkH2AXu2NDx-VgyocBatvC-Z_Ikk3UY5Mv04jpvEnSPbVHEIbR7M4QosqGXdnh-zC1sSR59diBxjAOsmWtqQ6mEJD4h6puCT8sgWKaLX_La1VBunq7Ikxe4oj8FflG8SutryHs8YMf8O8kiY8WftvPXvPttIJt1p8uXRZYF6hSFafEEdAzeZ1vyhaDCWWxCsZ8bfVKukkgmf3cPAVSOUGs7nUZU71_dJ09BAeDQUpkbEMH7qvOCH3Y64Mmcr1GjVsArkWWxW2hst39_ge3f9Cmhb2u1syIEotX9IXy4RnUL7g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0ef377348e.mp4?token=SfjePOtvov_sehgC9fv9h8X4C_Ip5c-QNkU3RBBYHJkH2AXu2NDx-VgyocBatvC-Z_Ikk3UY5Mv04jpvEnSPbVHEIbR7M4QosqGXdnh-zC1sSR59diBxjAOsmWtqQ6mEJD4h6puCT8sgWKaLX_La1VBunq7Ikxe4oj8FflG8SutryHs8YMf8O8kiY8WftvPXvPttIJt1p8uXRZYF6hSFafEEdAzeZ1vyhaDCWWxCsZ8bfVKukkgmf3cPAVSOUGs7nUZU71_dJ09BAeDQUpkbEMH7qvOCH3Y64Mmcr1GjVsArkWWxW2hst39_ge3f9Cmhb2u1syIEotX9IXy4RnUL7g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
🔥
و بالاخره جانشینان رودری معرفی شدند
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/Futball180TV/105345" target="_blank">📅 16:55 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105344">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Rz91KVlkDCogex0Sxu7giA14_yxwY0X_t33CUTgPHpVr3aBpPICyApklz6UasU_96jk_oHxpEaBo2cYq6CyWDOmJPDlosILHYHoe-6_pnEbf45LnDb4Q9pxDWeeyxIEcszkY5zczfc0jPVMWEXJU0jHK45EwHXSkyH67AG-MG7o13ALSRz-JXpJ2QYYIkKKxOCi6T1iK2OjrhI4wy4_yj4qPRAzVIOKQtcEqV2oztzOhbBX4A1Mpz2HFSKyawtO4fuI2THe2w41xOnddOPrbI1BQzMEFWk3awLizJj-4PJ7lEWHCiEmTnFvXCxgUUdgypHdnAHSnOIFjSiN_NteJFA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
🏴󠁧󠁢󠁥󠁮󠁧󠁿
🗞
رومانو: انزو فرناندز از چلسی به منچسترسیتی با رقم ۱۲۵ میلیون پوند
🤯
🤯
🤯
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
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/Futball180TV/105344" target="_blank">📅 16:30 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105343">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/A1Gg_3zuUVYPhyJLO56bASaZivXixyxJAvD5VN8GhuzgzjrCBexUaJBTppyyD1WVGsknjF3dt17mbkW8F9fixzqehLprdRxcgYn0SCRfMM47oAaLAdKnqh51c7-yvxvXt7q1jsKUK7dNn4FLD0qOYFM8fzKXgDe5e-mW8GRVd47DaLxSnv0HNi-0_klLDzYM3eduGQOsS8W4ONBrRmXZcZ1G8jcJO1crX0XtC3EUIeds1izGj3huF4d2mgQP6MMW_H2hjOOd54ax_4vFRk9wrn27xosIxoB8sFdURTkb1nRajLniidPNrGvLuGH68p-6PxsagF28JCx9jOXYyinCmQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇪🇸
مقایسه سن ترکیب اصلی رئال و بارسا؛ تیم فلیک فقط یه بازیکن متولد دهه نود داره
😐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/Futball180TV/105343" target="_blank">📅 16:05 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105342">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f91b6a8d69.mp4?token=SO18qqUj82OzAz-QECvhWP5nuHU2nnXasszKvHT6PffiegMo5RS3xIVji6hta02OEagwnyeMtqnKQJHUVwRGfjAlsu7SSbEpedqtnPhxz4kfjlj3YX51kf2W4T1lnNvo9SCsR3FU-0k80CvTykaoOhEztIU8dGO6HHT_QuPPoINtZPjRs5izDsmv-soHevkeOOtklQRp8onzVxlaJsf0C3ZSyG8oFk_zRchwGm8HMhsQJK7Nuh3c5T4CrJm_qGsMY-NoXoLDLQXAlK1pKJrEBEUaxxESQ5Z4yrS_4LKd2_CKygtGTZduaz9t8zT8c0wqZiNEywAqQTE5HWkdK_e6ZQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f91b6a8d69.mp4?token=SO18qqUj82OzAz-QECvhWP5nuHU2nnXasszKvHT6PffiegMo5RS3xIVji6hta02OEagwnyeMtqnKQJHUVwRGfjAlsu7SSbEpedqtnPhxz4kfjlj3YX51kf2W4T1lnNvo9SCsR3FU-0k80CvTykaoOhEztIU8dGO6HHT_QuPPoINtZPjRs5izDsmv-soHevkeOOtklQRp8onzVxlaJsf0C3ZSyG8oFk_zRchwGm8HMhsQJK7Nuh3c5T4CrJm_qGsMY-NoXoLDLQXAlK1pKJrEBEUaxxESQ5Z4yrS_4LKd2_CKygtGTZduaz9t8zT8c0wqZiNEywAqQTE5HWkdK_e6ZQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خداحافظ لئو. خداحافظ تا تولد یک اعجوبه دیگر در آرژانتین.
🩵
🇦🇷
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/Futball180TV/105342" target="_blank">📅 15:40 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105341">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9af28d1f54.mp4?token=XVrYjjaO7IV2TSd5KNPfwVds5yGVy62NilJBmM06gH-CCsVyFYEKrUtwt9X3QOOFJH7yDGlP_vowfgv21jtWIiDSYEPQoHMDUWpBp-hRKoSLz-lI5q3qfgZtLWIDTFjJLeTYY6mTj8T9BnYO9jUmaygdpa2uSvsOtK6nxGYyybzgBAwKIeRkAfSJQqn4dPH6MZGeKO0KC60NrfykoGHh7rHUIhGGzsc3MYC0seHWwiRp6dqAlwfxlK7Sxpr-e9SLvg-dCd1wJJ-TKcJqBJvtkKaL6vY2AgYBnzK9yFt-vBHeUiTTJ_oNnrS4_DCaUSyvZ0VPWPUL0ZJKW4INy8Z3Bg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9af28d1f54.mp4?token=XVrYjjaO7IV2TSd5KNPfwVds5yGVy62NilJBmM06gH-CCsVyFYEKrUtwt9X3QOOFJH7yDGlP_vowfgv21jtWIiDSYEPQoHMDUWpBp-hRKoSLz-lI5q3qfgZtLWIDTFjJLeTYY6mTj8T9BnYO9jUmaygdpa2uSvsOtK6nxGYyybzgBAwKIeRkAfSJQqn4dPH6MZGeKO0KC60NrfykoGHh7rHUIhGGzsc3MYC0seHWwiRp6dqAlwfxlK7Sxpr-e9SLvg-dCd1wJJ-TKcJqBJvtkKaL6vY2AgYBnzK9yFt-vBHeUiTTJ_oNnrS4_DCaUSyvZ0VPWPUL0ZJKW4INy8Z3Bg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👀
🇮🇷
🇮🇷
دربی فقط یک بازی نیست…
⚔️
یه حسه، یه خاطره‌ست، یه جنگ برای افتخاره.
🔥
۹۰ دقیقه‌ای که هیچ‌کس نمی‌تونه نسبت بهش بی‌تفاوت باشه!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/Futball180TV/105341" target="_blank">📅 15:15 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105340">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a3a4e2ac35.mp4?token=U9RpxwCgR0pAdyx008LJyhEiqxvowpx06FbqmyZVlnbB5VJZbBvZ-syazBY8oTNSEVf5wHj8-sC2Zb1c9_1uG7oIY3afv-4Y7K2TVHZniACJflfdf2TFkcqJzV7P0iJ8qOjZZXx0GuGnNuBHQjsx9cXjGHkwTJy67rCWXd8diOKaPQIjYvgexnwHBjZCQvXwXs4PIZH20PZy4RCZTCJ36LaNH_ccJ_xFyFcOolqexi5ckIGvD5hNhz5FnKWFd4MOu9UL2xCz0Jx-Zpo8_VPzIs_9e5CBT71cICI044_fkQHVtcqgzjnXddFkDrXOT1SbIaAJnk2wiH5VsbYtDA9OqW2kDTeY0Q3jHnNoXwcmm-36HluCbvidUzs91wdVxvNbmuyxtB2ffpRPuZUg1lQs4_ru4W8A6eRPyU5gzD8d17ZYwczOBfZP4REQqJriO0Tg6IM7L2fU-ihy2fUpGzwUdmsqiF3854gtPGDmqftumwz533LSP-r3nYKNO5FvYJ89IirhU0HLVUqqpQSBk8fQ6x5irL616MFyTIGI4RgETHqdnyYkNr87Dkh-kqYxSmVq1MAoAHpK44qZXrz1VH7xHqlSRehQ-GPuTgCRAbSoe0-uA0eKU1_gh3Zj8Tl9YcATQdFYnH2m97y0rEB5A73dQgA4Gk7K5Am2MqooyD_eKak" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a3a4e2ac35.mp4?token=U9RpxwCgR0pAdyx008LJyhEiqxvowpx06FbqmyZVlnbB5VJZbBvZ-syazBY8oTNSEVf5wHj8-sC2Zb1c9_1uG7oIY3afv-4Y7K2TVHZniACJflfdf2TFkcqJzV7P0iJ8qOjZZXx0GuGnNuBHQjsx9cXjGHkwTJy67rCWXd8diOKaPQIjYvgexnwHBjZCQvXwXs4PIZH20PZy4RCZTCJ36LaNH_ccJ_xFyFcOolqexi5ckIGvD5hNhz5FnKWFd4MOu9UL2xCz0Jx-Zpo8_VPzIs_9e5CBT71cICI044_fkQHVtcqgzjnXddFkDrXOT1SbIaAJnk2wiH5VsbYtDA9OqW2kDTeY0Q3jHnNoXwcmm-36HluCbvidUzs91wdVxvNbmuyxtB2ffpRPuZUg1lQs4_ru4W8A6eRPyU5gzD8d17ZYwczOBfZP4REQqJriO0Tg6IM7L2fU-ihy2fUpGzwUdmsqiF3854gtPGDmqftumwz533LSP-r3nYKNO5FvYJ89IirhU0HLVUqqpQSBk8fQ6x5irL616MFyTIGI4RgETHqdnyYkNr87Dkh-kqYxSmVq1MAoAHpK44qZXrz1VH7xHqlSRehQ-GPuTgCRAbSoe0-uA0eKU1_gh3Zj8Tl9YcATQdFYnH2m97y0rEB5A73dQgA4Gk7K5Am2MqooyD_eKak" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
▶️
🇮🇷
🇮🇷
سریع‌‌ترین گل‌های تاریخ دربی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/Futball180TV/105340" target="_blank">📅 14:50 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105339">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AKEEi9-58LbbkrJYFr-ligXTWyOMsyrrj4aQ4NMc9luoiu-NjaYSu5njTntoYXr_Unmyiw-wRm0dsMwgJlr-UfYYevoukcpglgWiAUOicf8VSglLRr1pel3vyFCVGxpT8hEHxEiT-b_oEchAiiWyDy3xOfBvKDOJiZFa5YToYJp_yzAg6TWcjk3Hc5UQ85GFdyCEv1VmkhvVG2SzaW6mal7ot0UVE5xB3h52MoflnPsr1m10pnmLqE3ZfFb-zBvk1QteQZMvssP_UqUxs8MC7kG1r6F_kG9Mr6YdSVqXnFNDAPeJA9gO6MKrA-lvcdr4BFbPVET_D9qqAS9HsaY7zw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
‼️
💵
قیمت دلار تو دربی قبلی ۱۲۰ بود و الان در کمتر از یک سال رسید ۲۲۰؛ قدرت گنده‌گوز منطقه
🙏🏻
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/Futball180TV/105339" target="_blank">📅 14:38 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105338">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e8d7c8fe82.mp4?token=T0NB2t9KM8lBqFIvuilTH-0iUbgnYQS65ro0q7c0hHH-giptMqcrFZAxanDGlju-47Dj_q8rOrOi7VO8bukxPCJrmullnKpv82DuoKLCdkE557WwHnVozE_A6-G3F43pJer3mGtAUnALTd9cmnn_-4Itaj3hIiDZatsevg3se19tmYQ5684RwHEl3pvanxKuOpRmzbCnDxor_UwM6oCAMncKR1xzQcUU0b0MHyhQI_y2uVi-PkrhViY2LSzIJfq25V7kGtbwCXLaKiCc5OTgdpdfFkj1Im7MNbapA5AfrT8AfG1VJGNOUGrskvYi5bw_hT4w5U2hSpJjcE1-jfvROjzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e8d7c8fe82.mp4?token=T0NB2t9KM8lBqFIvuilTH-0iUbgnYQS65ro0q7c0hHH-giptMqcrFZAxanDGlju-47Dj_q8rOrOi7VO8bukxPCJrmullnKpv82DuoKLCdkE557WwHnVozE_A6-G3F43pJer3mGtAUnALTd9cmnn_-4Itaj3hIiDZatsevg3se19tmYQ5684RwHEl3pvanxKuOpRmzbCnDxor_UwM6oCAMncKR1xzQcUU0b0MHyhQI_y2uVi-PkrhViY2LSzIJfq25V7kGtbwCXLaKiCc5OTgdpdfFkj1Im7MNbapA5AfrT8AfG1VJGNOUGrskvYi5bw_hT4w5U2hSpJjcE1-jfvROjzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇮🇷
🇮🇷
زنده از ورزشگاه نقش‌جهان در فاصله ۵ ساعت تا دربی حساس پایتخت
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/Futball180TV/105338" target="_blank">📅 14:30 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105337">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">🇮🇷
بهترین گلهای استقلال در دربی‌های لیگ برتری
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/Futball180TV/105337" target="_blank">📅 14:25 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105336">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">🇮🇷
بهترین گلهای پرسپولیس در دربی‌های لیگ برتری
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/Futball180TV/105336" target="_blank">📅 14:01 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105335">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/v64oJ9Tr_TE__iLc1vytCjkDseZ5tcBjo6mLvlonwmjNVGR2cl7K-FIlaSxV_Q61L2mW9jme_GCo7g3mlyjdA8xeLPQ6D3BmA5tJgKyXBz16VPiWvKV7dqTDLKjU_r9YnaLi98-2D-cWzZom6H4Kmh2vKTKJS1obYe6rRFBDEGMyjcfDxgOsN6auJ-ylS2x8nIVzyNWtXAO8IL2THoNJEaVeFY-E3iopFBB35pY4vxGX6xo7iPMPX-6AJamPUy-ZR9keNNEfjlkIuI5H4Vkgi3izsT__Wi2LH1bWBBlbYaosTFlXcsbcJXPfs3WqopfYtCTdDA7f9YzYKDTNTUKVsw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
😳
💵
خارکسده
افسار پاره کرده
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/Futball180TV/105335" target="_blank">📅 13:44 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105334">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/azTgbZMZxsJ9H59pFOfdJv1AzqimVcZZaKzmZFYZQI7o58ZiOxoMbiSKEqzB-GiLy5wbrmA1iZnlazR7fZX2YPXsEs7_np3zs0rm9PRGV89kh-in8C3cvGCESbbU5Pa-ptYbjUeuuFIZDPrza4d4h25rF_O-5QYdbwHKkLil-ckyzNa26m3lmaSFbleOPU3HYO3MROBNUjJd8mkHWu3BnyLPIfFuiX5dRbhypO6bH3U8NUVH3CQIFV5duNbLkyII_ekD07RVm2zfewaYMr3rcS_Jckdp2qrLHP-sbRQthH_HEdqqf96OjHBsv_hmZagfXnFo7JLZRVxEvnvt-c5Guw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🤯
مسیر‌ فوتبالی عجیب‌وغریب آلوارو موراتا!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/Futball180TV/105334" target="_blank">📅 13:35 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105333">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/40825ae46d.mp4?token=ETYQdf3_JvpSVrpi_t5Hl2_dsQ1KlNa2P7KRI493uzEH0xV_phXAkLsJ7aguiu5Kxo_-Kb23W1KwGPiwOQUxIJogDfH47upV_3rYBBNR_HT-ai7N97E6T6GGgcZ1GNHZZPQWPVyd6Jzx4R8SvNQklm-jJefe5UeJBBVGfjRayNJGHqYmjh3VIk_IYW1E2tKiZvSnUMSYIFvCcu581mwLozntFBcJCmFxELXfumXvDZlHHvEEXKTaE73-11tnqxLb20c0G2a6CTUDpY53bEft6OLeCTsmUIh4WyP3q6k4dThI0VJcK5DVk2IVhgWcLCGSdfFEYpWTF7tdwobrA80YeQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/40825ae46d.mp4?token=ETYQdf3_JvpSVrpi_t5Hl2_dsQ1KlNa2P7KRI493uzEH0xV_phXAkLsJ7aguiu5Kxo_-Kb23W1KwGPiwOQUxIJogDfH47upV_3rYBBNR_HT-ai7N97E6T6GGgcZ1GNHZZPQWPVyd6Jzx4R8SvNQklm-jJefe5UeJBBVGfjRayNJGHqYmjh3VIk_IYW1E2tKiZvSnUMSYIFvCcu581mwLozntFBcJCmFxELXfumXvDZlHHvEEXKTaE73-11tnqxLb20c0G2a6CTUDpY53bEft6OLeCTsmUIh4WyP3q6k4dThI0VJcK5DVk2IVhgWcLCGSdfFEYpWTF7tdwobrA80YeQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
🇮🇷
🇮🇷
امیرحسین‌صادقی: اگر همین‌الان میخواستم در دربی و فوتبال بازی کنیم، دستمزدی که باید میگرفتم بیشتر از ۱۵۰ میلیارد بود
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/Futball180TV/105333" target="_blank">📅 13:10 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105332">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ebc8f3b366.mp4?token=dMo8FY_GY8EsvcR1bRO7jhugW2yYPTVZBU9u7_7xvt6nKKrlreU9xUyHHK9XBmO7sNFM-sKOkGrD0JW9N3XxLapAZuDwHD41t_9E6kF17dIex3me3Aqkq7hx-fD7FNyr_0hH6loA4UPyP208ld1ilZZi9vHhRQBDcEBtqx3IzZbdpw8aSqhDh9JTkY8MRCkSYv_caBbXmDE9Ryyc736s9RIIzWHNtl9KBVwyPOZNKOeoxuvDjSi0s9nRSO0dA2767ZNZtihKtJby0j4aE54ATUVzi26n5SM1ct4HdiJJcks-p01rynD5JjiIk-A2URWUdi1jUW7LnKoN38YKibuYGQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ebc8f3b366.mp4?token=dMo8FY_GY8EsvcR1bRO7jhugW2yYPTVZBU9u7_7xvt6nKKrlreU9xUyHHK9XBmO7sNFM-sKOkGrD0JW9N3XxLapAZuDwHD41t_9E6kF17dIex3me3Aqkq7hx-fD7FNyr_0hH6loA4UPyP208ld1ilZZi9vHhRQBDcEBtqx3IzZbdpw8aSqhDh9JTkY8MRCkSYv_caBbXmDE9Ryyc736s9RIIzWHNtl9KBVwyPOZNKOeoxuvDjSi0s9nRSO0dA2767ZNZtihKtJby0j4aE54ATUVzi26n5SM1ct4HdiJJcks-p01rynD5JjiIk-A2URWUdi1jUW7LnKoN38YKibuYGQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
❌
🇮🇷
🇮🇷
حمله مهدی‌فنونی‌زاده در آستانه دربی به بازیکنان سرخابی: عارف آقاسی ١۴٠ میلیارد از استقلال گرفت؛ قیمت بازیکنان فعلی ١٠٠ میلیون است
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/Futball180TV/105332" target="_blank">📅 12:35 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105331">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/Futball180TV/105331" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/Futball180TV/105331" target="_blank">📅 12:35 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105330">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UzuB3kMlUmBnOeW-DuTds5mIKeJYJReOit6x_f2RXmllFmqS0feiPZODhp9EzHPWBfkc_Hq6qnEjdL-BshH6MjaYrQe-Q7buV0cCIepRv7tz_ijFkVjun8hcDZRjeR0QVdY7PT1wPWWg3cx5I1SnFfDcAaLZGuMYXIG9IN7uYrQdkYNf5-3OAN2Fj87B657uNEfZkqFLr-xUwR1nW7q3lWdNRiVPRqFNEZ6NouQvlBMyfKz4tizw1-QlSE_YrJoQlPCIAwKmLD_GYfhoAj2xiQ__F6sTqglemMAuMfjs68up_Y8PkgPxe6A3CkaPIijqIg-gBSl7HJOlmJdYctM9wA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/Futball180TV/105330" target="_blank">📅 12:35 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105329">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1137b6f537.mp4?token=Of9190faG-7bPvw-eHlhTRH6kzw7xnp14D2LQH3k8Wm3sqCDEKI_hz01eEfYDEoTLQk7a0dnkfHf6a79WghragcQ2nof4ESo5yF8knWYmsJNv9qwqKBFb_EBVukV6-dXv50qdKz08HDijgL0DTgyuQKRYzgSmfgnWdx5MPfh3qn0aAsyo_s3u9scxHI551turQZabRIvL9jxzMz0ytPNnRCroi8YPk-ikKhmGRZscZ27dmMbnuSvuRMGq20Qmsa5mvWKE-PdZmAVjjldm_FsiLQCZ-c-XshJIZKyP3-f3DWaaYcRo8n7bpKxPjuWHr7wubSNQql5kUm1a3kjW6Gi3Hi2ZxHjRK4NLVAyOy4jAPTpO66pV85xIDXpGvsqfDuj9ZASfzi9J5qVFhXNtXl-9cEoOcFzi9TPRi1kPP7ULahR_oC78-9QgOE_hJ5A3T5pIJaT5wdDR76B_WD1SGtmp6BcpRemwqnuG52I17viSzPuTCH1XxQxoaxiSj4U1VxFotKU5rMl_CqR8SmJqs9qXD0Cyqg8e9xq_LnfqNtl0xBQbL5Znd5x3Wg0KkzFrfYJKjc7oLS3T-VYUXj9PwMhpBaVMiKk11goEnyKVMYueMmiKvqMy6JeBFWQ2-FKJDINE3_7dw8ObTPcYJWj6AK82RyNzTAv2LeiWS7uYdbpiUA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1137b6f537.mp4?token=Of9190faG-7bPvw-eHlhTRH6kzw7xnp14D2LQH3k8Wm3sqCDEKI_hz01eEfYDEoTLQk7a0dnkfHf6a79WghragcQ2nof4ESo5yF8knWYmsJNv9qwqKBFb_EBVukV6-dXv50qdKz08HDijgL0DTgyuQKRYzgSmfgnWdx5MPfh3qn0aAsyo_s3u9scxHI551turQZabRIvL9jxzMz0ytPNnRCroi8YPk-ikKhmGRZscZ27dmMbnuSvuRMGq20Qmsa5mvWKE-PdZmAVjjldm_FsiLQCZ-c-XshJIZKyP3-f3DWaaYcRo8n7bpKxPjuWHr7wubSNQql5kUm1a3kjW6Gi3Hi2ZxHjRK4NLVAyOy4jAPTpO66pV85xIDXpGvsqfDuj9ZASfzi9J5qVFhXNtXl-9cEoOcFzi9TPRi1kPP7ULahR_oC78-9QgOE_hJ5A3T5pIJaT5wdDR76B_WD1SGtmp6BcpRemwqnuG52I17viSzPuTCH1XxQxoaxiSj4U1VxFotKU5rMl_CqR8SmJqs9qXD0Cyqg8e9xq_LnfqNtl0xBQbL5Znd5x3Wg0KkzFrfYJKjc7oLS3T-VYUXj9PwMhpBaVMiKk11goEnyKVMYueMmiKvqMy6JeBFWQ2-FKJDINE3_7dw8ObTPcYJWj6AK82RyNzTAv2LeiWS7uYdbpiUA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
❌
چرا محمودفکری مانند کریم باقری در تیم ملی فوتبال ایران موفق نشد؟
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/Futball180TV/105329" target="_blank">📅 12:20 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105328">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/d7p1kAJJgJHmeIT_Q0862ftWFXR11fCApKSeii7i9NvZ8N71RTGNyo40Lx5-P3STQv1kbfwOrrmtp_BFOd7ifLPub_PxBiOQrryTMECzYTjgiFFEglOGZP6kG_KqSh2uYx5JeuLSeJ4kmrddonhLheykoHMej9CymF3RgIuY21egJfSe7kjhlwnxcoD_u4sW3YmGk8cye7NGh8pF6GwOlxaILoksSBq2RkcTPk02VjJ4qnG7_6tI_TwuZOZ6eLrPC22EHmtBVKjeZ_yhOug4IPqUaimg0mr5SO_j_Hpd5n80-OwmBY1TH_lu3mF4NaQV2TrZXu0ClWZr7Hv3H4-xFg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
💸
🇮🇷
🇮🇷
ارزشمندترین بازیکنان فعلی سرخابی‌ها
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/Futball180TV/105328" target="_blank">📅 11:55 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105327">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4f75defa90.mp4?token=Umf8pElONTeWrnJqWsIqOzJzKUSVerxU9nEliATin2CU5bBdCe3NdeLerid2TZD01jbsoStqxwB6aCDwhON9gShd8KKMZdFZ7mdEZaUTGeMe-0OBe4ejGZjsoFXSo8-c-ISVcin4pee4H0krD_1MTQfYSj4_Z1fi3yaZ8wCbZeCYmI7HT5cJ-9cpHpF5VE-3IHAQvCwqm-BZVuR-BVs_yAE29-ygeEkXKNV2NQtQzmKIdXENXc0G7B5QSJvTTjd4qm97Dkn8uOQG6XTChWVrJe1tNfrzM9VPxFsfDjrphBpUF6DUP75jLzsbo-CCxnY6nsfI9HFpNn0bKb9g4M2CRUQbP-1ZVPbnubuRvXz5dUz26blESFxvVxXQfH0wRIBgB3y98-o-RIM6UODMQqZu09InPl63MMqUIZLlwB-YHXPeXYTy65O9nbLDV7ySn_ZWMqULOTSPSaDX0UD7JPhab_vhxUhRo0Urozw5PHSOHfjvRYSHzJ9AJfuIfuPpdwuR-IqN_CdfVxlD2Sge7f9h5yitmISymV6U04KRQ1OLVzw8MPp0pVoed4Myfd92pKsokIS_qPlrtilqO6M9L2Jr1q9XTEmCcS9i3ZorvyA0jEDRwg0J8Pdw_6dko_EdIAChu-Bpq1MZO4yF606bvHmT-PyHG3m381BEclTj3qE8SME" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4f75defa90.mp4?token=Umf8pElONTeWrnJqWsIqOzJzKUSVerxU9nEliATin2CU5bBdCe3NdeLerid2TZD01jbsoStqxwB6aCDwhON9gShd8KKMZdFZ7mdEZaUTGeMe-0OBe4ejGZjsoFXSo8-c-ISVcin4pee4H0krD_1MTQfYSj4_Z1fi3yaZ8wCbZeCYmI7HT5cJ-9cpHpF5VE-3IHAQvCwqm-BZVuR-BVs_yAE29-ygeEkXKNV2NQtQzmKIdXENXc0G7B5QSJvTTjd4qm97Dkn8uOQG6XTChWVrJe1tNfrzM9VPxFsfDjrphBpUF6DUP75jLzsbo-CCxnY6nsfI9HFpNn0bKb9g4M2CRUQbP-1ZVPbnubuRvXz5dUz26blESFxvVxXQfH0wRIBgB3y98-o-RIM6UODMQqZu09InPl63MMqUIZLlwB-YHXPeXYTy65O9nbLDV7ySn_ZWMqULOTSPSaDX0UD7JPhab_vhxUhRo0Urozw5PHSOHfjvRYSHzJ9AJfuIfuPpdwuR-IqN_CdfVxlD2Sge7f9h5yitmISymV6U04KRQ1OLVzw8MPp0pVoed4Myfd92pKsokIS_qPlrtilqO6M9L2Jr1q9XTEmCcS9i3ZorvyA0jEDRwg0J8Pdw_6dko_EdIAChu-Bpq1MZO4yF606bvHmT-PyHG3m381BEclTj3qE8SME" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇮🇷
🇮🇷
مارک‌کلاتنبرگ: پنالتی تراکتور در بازی مقابل شمس‌آذر گرفته نشد!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/Futball180TV/105327" target="_blank">📅 11:34 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105325">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/nYWfukZkcXVts6QEBGHoNl77Ll7sMPOmh7CISSVVtNtZH6W1ZgpbdUn-JRcv75IXSVky3pH3fR5g5w5nTPQpvL7dQvtXxWT1Q4wtbC4_pWf2x1liQ_5nMo4hyHbpSNo55sp5-xEQ7WEVAFfqljNTTYeaHAav1OsRFyYzSJez6j_T8XutWgzkHgaVgQQAIzXh1tIPgogSayXELJWUX0wuuvCtSt4QNVmryOWATGTnNv46O4EXzZjikDmZypRc7LdX8U-IJMe1VfgPHiGVkPIzY2dn9_Udh1MDzMnBwajNoiuSPRjESlM1UUrEF45DcY68Th3JKOHhnbaQfdf7Rhc_Pw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/MYkhuqKSk9GYeAoTRi4ceKmh0wYexmX8ZmUEgndghTGuUGX6_Os6najX6KWMf6Y4aYq19kGpG3-99Wr-qKZ7R5wqnP3keO1vg-QVULR1mpD2drU2zbNCUU3KSte9BVQocEFeIlGPVEYKccfudAAzPpI54EzeqBn0RLQMjFgG49vtNZ_yh7efZhhdV5VM0s4qbsErWUygaGEybX-GIdKK4fPjQxLB5cSZzZmDQo88qGwcaDn6H82wuArMb0tCBoY9r43JO-MoaVPY3vKdfllyC1E-m9i9Hv4g2zzVGQTY-Z8k_sJdxZ7aSPkAlyEHjR7Lr9qy9r6qeQC8NCGjarlPeg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚨
🇮🇷
🇮🇷
پوستر سرخابی‌ها برای دربی امروز
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/Futball180TV/105325" target="_blank">📅 11:21 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105324">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">▶️
👀
🇮🇷
🇮🇷
مروری بر دیرهنگام‌ترین‌گل‌های دربی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/Futball180TV/105324" target="_blank">📅 11:05 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105323">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OlcxhWe8Iyol64so8jKM7Fpu1iWEmu6YgeKSJhrlcVOnu6Jt6fmvq0bgAikv7bOeQTlAltJI_XYM3r8S0g5gS_regtdwGFkt1r5w8Oevsk9LVmJy8L8WMmnOrE-tV3SuV9hxWFtJQ8BpV76ovqMIwLlqKBDBiCGL4RaTGhgwMdBj1B8qkT1UJOZF0Or1U7PCceWY582Nt86XsHM1vq_sM2BM-Vf_Ft4-m3G5Ckp_yE7Ba5pgY6BSj45jhxNhZaaVikU9j7_u0kKoxYJX4IfwYBkPXYUFNUf5ZXJD5f1D1KO2xqQgBNjp-utkMz6jqIUHgDu2ZCAB0XD7Wk4LjlqJ0A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
✅
🇮🇷
🇮🇷
مقایسه افتخارات رسمی سرخابی‌ها
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/Futball180TV/105323" target="_blank">📅 10:40 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105322">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0a3bce317a.mp4?token=AKRlc4alDHs6EhFonHbFYbIHPPYHTas4Hnuidm4__jx1kygpUFVaisoo9OULZ7O6F7ZObXfDoJGnBYF8KgFG9DK1lO1BlCC8p5H2fY4ujYDTnrId01NgHpQECPRAID3EWkXfcf8Yc39UTRItf5Nq6G1SByam-GErK4gR160afXK9Re3T_hZ4grQdQb7nTNbr_4QU0X7H5uE3LbMxvDV-HYxwSoTP6APHqy6JD1GktXnMvYXm_EXCihgqP4yDWHfaU4QX5f589J5W0gewADYosfctK-V_amAVeyQ3j1Pd0IP41YvAi-W3hPKJcoA7CB5h4TEGhks0UjcasBw4FLA8vw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0a3bce317a.mp4?token=AKRlc4alDHs6EhFonHbFYbIHPPYHTas4Hnuidm4__jx1kygpUFVaisoo9OULZ7O6F7ZObXfDoJGnBYF8KgFG9DK1lO1BlCC8p5H2fY4ujYDTnrId01NgHpQECPRAID3EWkXfcf8Yc39UTRItf5Nq6G1SByam-GErK4gR160afXK9Re3T_hZ4grQdQb7nTNbr_4QU0X7H5uE3LbMxvDV-HYxwSoTP6APHqy6JD1GktXnMvYXm_EXCihgqP4yDWHfaU4QX5f589J5W0gewADYosfctK-V_amAVeyQ3j1Pd0IP41YvAi-W3hPKJcoA7CB5h4TEGhks0UjcasBw4FLA8vw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
😂
🇮🇷
محمد نوری سرمربی صنعت‌نفت در کنفرانس خبری دیروز تیمش بازهم شاهکار خلق کرد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/Futball180TV/105322" target="_blank">📅 10:15 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105321">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">✅
🇮🇷
🇮🇷
سه‌دقیقه فوق‌العاده شنیدنی و دیدنی با نوید استادرحیمی از دربی‌های جنجالی و خاطره‌انگیز
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/Futball180TV/105321" target="_blank">📅 09:50 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105320">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9ca6813881.mp4?token=euoIZTURkdsmUUcVAzKDJ31BPUKJ5He6MPxgHIOGPq9dD7W4BGL1qle4Ekb9iaIEqGjDehgey2Diz1qrTAMwROYNVfRMbXtxf87st5OQjSdv-n52RJWmJpafbc5YGDwtWJPPWSo5HOtlLierCyXZ0m9dfLnJQdahdC3bBp8PsFcZ5JwV30EhuDR_CRULkjHI1jr76_X0blw7iTkCUgSriTIIAM-9KO9Bu6DeOasPjXTfH3H7sPHh_isCxncNGRDBeb2WQYEizFFM7URHy0mAzSB0F7Zi_Hr1S_L0Vn8NY-EYtuuIauwD7DddqvlQqeTy3qjuoBDQ1AT1RgyCFRXt2Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9ca6813881.mp4?token=euoIZTURkdsmUUcVAzKDJ31BPUKJ5He6MPxgHIOGPq9dD7W4BGL1qle4Ekb9iaIEqGjDehgey2Diz1qrTAMwROYNVfRMbXtxf87st5OQjSdv-n52RJWmJpafbc5YGDwtWJPPWSo5HOtlLierCyXZ0m9dfLnJQdahdC3bBp8PsFcZ5JwV30EhuDR_CRULkjHI1jr76_X0blw7iTkCUgSriTIIAM-9KO9Bu6DeOasPjXTfH3H7sPHh_isCxncNGRDBeb2WQYEizFFM7URHy0mAzSB0F7Zi_Hr1S_L0Vn8NY-EYtuuIauwD7DddqvlQqeTy3qjuoBDQ1AT1RgyCFRXt2Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❗️
🇮🇷
🇮🇷
فقط اونجایی که صداسیما زیر نویس میکرد دیگه نیاین ظرفیت تکمیله
🥲
💔
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/Futball180TV/105320" target="_blank">📅 09:25 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105319">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">🇮🇷
🇮🇷
یه ایرانی رفتی از دربی کشور زیمباوه برامون ویدیو گرفته؛ به دربی سرخابی‌های خودمون تشبیه‌ش کرده
😂
😳
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/Futball180TV/105319" target="_blank">📅 09:01 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105318">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">🚨
🇮🇷
🇮🇷
#اختصاصی_فوتبال‌180 #فوووووری
❌
شورای تامین استان اصفهان در صورت تشدید حملات و درگیری‌ها تا ساعات آینده صبح فردا جلسه‌فوری تشکیل خواهد داد و در صورت ملتهب بودن شرایط قرار است بازی دربی را بدون تماشاگر اعلام کنند. هرچند تا این لحظه سطح درگیری‌ها به نواحی…</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/Futball180TV/105318" target="_blank">📅 08:56 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105317">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0ebf67c803.mp4?token=lSep54xPzH_tguciDZSNCxDSnRrHVxLvRudvJ1gqvG7vdOhetNIsENb05MpVq6c13NZSpPsQc6yJtoM3kJ7oe7P2vSPRB9D9HB0KgcxP2f1erU_il31Z0pq08XQC--uuzd_JocKwUZF2YmeBDHZKo-KXE1z_Q3g21NT_0bE3d17EkJd83fgI3V4ToBy7pxquFtnR2uv5S5zuR4RqbS-PKL6zBq_kx4WhxCDbf4WaXiWC0lN2Aa5w7k9TkTogAgc7DaDF9hIj-T1RvYg402lnenVvYVZ7ibdTvfiQuMlHHEO46NgL4GRSaqmiEZoaPqlf6cfiMQ_eTVhPB5JnrUhn6oudLTMQimdMhgBkIEh7CHDuV0v_4w1yl2EtAVgC1SE9Euk-8kNWyen2udKiwnhNVOgPIbo-NBs2FzmxCiHz5NX12lttdaVQTil3n3f2cViTc-jEDyLGai3jI4fK1MImij3ChqWgDrJGM3KJbl8mRR3Hu3giqbZl3fOycqUuxub2jHFiiFYoU2vgl5wyadboQXLWw6rhFH-CbBZOIXnZo9MV2i3TwGEcGUT8ovWzCuQOS362fdA9yQD8etyU79vtz5rDXmcKAhJ7V2RZqaSgl0FeR-BNYbWXfqqGWL5A4LQpV7-ZCDtXWoy0uDqtvhYqxjJ4Cetx-RxABlmKFhiJz5c" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0ebf67c803.mp4?token=lSep54xPzH_tguciDZSNCxDSnRrHVxLvRudvJ1gqvG7vdOhetNIsENb05MpVq6c13NZSpPsQc6yJtoM3kJ7oe7P2vSPRB9D9HB0KgcxP2f1erU_il31Z0pq08XQC--uuzd_JocKwUZF2YmeBDHZKo-KXE1z_Q3g21NT_0bE3d17EkJd83fgI3V4ToBy7pxquFtnR2uv5S5zuR4RqbS-PKL6zBq_kx4WhxCDbf4WaXiWC0lN2Aa5w7k9TkTogAgc7DaDF9hIj-T1RvYg402lnenVvYVZ7ibdTvfiQuMlHHEO46NgL4GRSaqmiEZoaPqlf6cfiMQ_eTVhPB5JnrUhn6oudLTMQimdMhgBkIEh7CHDuV0v_4w1yl2EtAVgC1SE9Euk-8kNWyen2udKiwnhNVOgPIbo-NBs2FzmxCiHz5NX12lttdaVQTil3n3f2cViTc-jEDyLGai3jI4fK1MImij3ChqWgDrJGM3KJbl8mRR3Hu3giqbZl3fOycqUuxub2jHFiiFYoU2vgl5wyadboQXLWw6rhFH-CbBZOIXnZo9MV2i3TwGEcGUT8ovWzCuQOS362fdA9yQD8etyU79vtz5rDXmcKAhJ7V2RZqaSgl0FeR-BNYbWXfqqGWL5A4LQpV7-ZCDtXWoy0uDqtvhYqxjJ4Cetx-RxABlmKFhiJz5c" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
🇮🇷
🇮🇷
روایت فرشید باقری از درگیری عجیب سیدجلال و مهدی رحمتی در دربی ۸۴
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/Futball180TV/105317" target="_blank">📅 08:01 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105312">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/Futball180TV/105312" target="_blank">📅 01:12 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105311">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">⭕️
⭕️
با توجه به نزدیکی به دربی پایتخت و بازدهی فوق‌العاده تبلیغات تا پایان هفته، اگر تمایل به همکاری و انجام تبلیغات مدنظر خود داشته باشید، با ×تخفیف ویژه× در مجموعه تبلیغاتی تیوا با بیش از ۱۵ کانال مختلف ورزشی و غیر ورزشی در خدمت شما عزیزان هستیم   برای هماهنگی…</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/Futball180TV/105311" target="_blank">📅 01:11 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105310">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">🚨
🚨
🚨
🚨
‼️
⚠️
یک فرد ناشناس در مشهد با خودرو به تجمعات جانفدایان ولایت حمله کرده و تعدادی کشته شدند
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/Futball180TV/105310" target="_blank">📅 01:06 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105309">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f42b196ef1.mp4?token=QZrqScOaOtA_34cdynlA2RNTa30UUM3lBPlXg_BJxV-rXOiZKzGMY17q5xhl9slSNruoiCtZcTfaqv4nHl720FtrKSqRGVTlcHnr6Hhw44iz7Fm-qBrhgNkBWvVVvjAhmMd3HlWceS6AgiGDOOmrT1a6Wdoe0p_5n-MWSNAsseJTfpOAHr3wYSQjktGd_0c-uufj6ViK0f27n-n0Gp3-41lXCdoXrW7eR0dhMTqRXlbzac7t7PigLiSLgXFqnXLSh8SLfEFYxjnCNsEATLQUqOsBvcj5VWz4GzSG7ozws8lUDYDNaa-pFug4ArAIQvkrfFW4uWYxT4LKBuMWtEbshA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f42b196ef1.mp4?token=QZrqScOaOtA_34cdynlA2RNTa30UUM3lBPlXg_BJxV-rXOiZKzGMY17q5xhl9slSNruoiCtZcTfaqv4nHl720FtrKSqRGVTlcHnr6Hhw44iz7Fm-qBrhgNkBWvVVvjAhmMd3HlWceS6AgiGDOOmrT1a6Wdoe0p_5n-MWSNAsseJTfpOAHr3wYSQjktGd_0c-uufj6ViK0f27n-n0Gp3-41lXCdoXrW7eR0dhMTqRXlbzac7t7PigLiSLgXFqnXLSh8SLfEFYxjnCNsEATLQUqOsBvcj5VWz4GzSG7ozws8lUDYDNaa-pFug4ArAIQvkrfFW4uWYxT4LKBuMWtEbshA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
‼️
⚠️
تصاویر دوربین مداربسته از حملات پیاپی به نزدیکی یک مراسم عروسی سیریک
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 28K · <a href="https://t.me/Futball180TV/105309" target="_blank">📅 00:57 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105308">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tkRrKayJzIQXQe0VddooB6Uye9pnyp9x-zRyDRE0ZPeUZIICP1BouFOicclsLkbQu_fRl0_EyUmqnE5U3uO5e_utPVzfz1DWQCDmjX0cSZUJjCUk4MGT-IzY95xZx4IjIt6_lNblz2qYvWCQZFaavjeoMMTOCLmKnJH6hVGjmp1nW4QawuZsB1ld3RYbNZoubdMPtw1gdTuFI7Tc5hFg7lTHQq9dbIa-5H41r37BcqVWjsZN8RnywM72AHD5O4t2Y9U3jonko6IxhToo6DENcbTOrueHl6mQBo3XlQkNrZpL8jdLlLFV3SZQKM3DXqDHgCZ1adVJgOqUPqXcScoD6w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇮🇷
🇮🇷
#اختصاصی_فوتبال‌180 #فوووووری
❌
شورای تامین استان اصفهان در صورت تشدید حملات و درگیری‌ها تا ساعات آینده صبح فردا جلسه‌فوری تشکیل خواهد داد و در صورت ملتهب بودن شرایط قرار است بازی دربی را بدون تماشاگر اعلام کنند. هرچند تا این لحظه سطح درگیری‌ها به نواحی…</div>
<div class="tg-footer">👁️ 29.5K · <a href="https://t.me/Futball180TV/105308" target="_blank">📅 00:46 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105307">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">🚨
🇮🇷
🇮🇷
#اختصاصی_فوتبال‌180 #فوووووری
❌
شورای تامین استان اصفهان در صورت تشدید حملات و درگیری‌ها تا ساعات آینده صبح فردا جلسه‌فوری تشکیل خواهد داد و در صورت ملتهب بودن شرایط قرار است بازی دربی را بدون تماشاگر اعلام کنند. هرچند تا این لحظه سطح درگیری‌ها به نواحی…</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/Futball180TV/105307" target="_blank">📅 00:38 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105306">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">🚨
🇮🇷
🇮🇷
#اختصاصی_فوتبال‌180
#فوووووری
❌
شورای تامین استان اصفهان در صورت تشدید حملات و درگیری‌ها تا ساعات آینده صبح فردا جلسه‌فوری تشکیل خواهد داد و در صورت ملتهب بودن شرایط قرار است بازی دربی را بدون تماشاگر اعلام کنند. هرچند تا این لحظه سطح درگیری‌ها به نواحی اطراف استان اصفهان نرسیده و این اتفاق تقریبا بعید است
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 29.6K · <a href="https://t.me/Futball180TV/105306" target="_blank">📅 00:22 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105305">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6cf9805271.mp4?token=k5YeWmixLaHXh9V4-1HwCnvPVOUD3HAAIX_81ke2Yqvc5a4ZViDfRX3rjk5FqBXFTwWoa8hc8HFNQpck_XlwQuxz1-hO223SP5yav3i3dIyYiVUK-9DfIJ5haAvNAqeD94U0yQ9wZ70I7z8DIhXLAA3MIUBzQOHiZojJ9FxyLx5Yo4dnCJKmNp2-LFVIMRfLjb-CZCPyRbanVgTqbJ9eB8P3v_YS41-OxaHKy6_EzlUEp_2EdaIKqu9IG3FhhL_NaWHZMbtXuhRXtv8Hjtcp8zb1-dgLLV4r7GDCoIUgnFfP7fV9jNwE4MPta7OR22Y73LkEo9G4qzszhxYcvMq5og" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6cf9805271.mp4?token=k5YeWmixLaHXh9V4-1HwCnvPVOUD3HAAIX_81ke2Yqvc5a4ZViDfRX3rjk5FqBXFTwWoa8hc8HFNQpck_XlwQuxz1-hO223SP5yav3i3dIyYiVUK-9DfIJ5haAvNAqeD94U0yQ9wZ70I7z8DIhXLAA3MIUBzQOHiZojJ9FxyLx5Yo4dnCJKmNp2-LFVIMRfLjb-CZCPyRbanVgTqbJ9eB8P3v_YS41-OxaHKy6_EzlUEp_2EdaIKqu9IG3FhhL_NaWHZMbtXuhRXtv8Hjtcp8zb1-dgLLV4r7GDCoIUgnFfP7fV9jNwE4MPta7OR22Y73LkEo9G4qzszhxYcvMq5og" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
🚨
‼️
⚠️
یک فرد ناشناس در مشهد با خودرو به تجمعات جانفدایان ولایت حمله کرده و تعدادی کشته شدند
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 30.1K · <a href="https://t.me/Futball180TV/105305" target="_blank">📅 00:19 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105304">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3fcaf59f19.mp4?token=AwT7Mnt5IVgRAkJk-_ttjwcOAI0NJKGwTL_OFF3gBLDfM56XcRt3OyhuG54ka6DuV64w-FxxVp8Q-8DtCTxmjJYx0rWCOlZLAE6gggt7DLig-CBpmjPqxiJHNafXWH_A3Yez4xaTZQYodVf4BwknnkkvUddW9SgdPFz7xWcgGFXyvtJmotlrSd6XnHCPT6SlmqQprRFd_nkYFlCid4TKgmTlS9qGboM-GPHqg-KXYFvJBH9tbS6dxmjLopM42UuYQHmujljtlHRRM3glKeVD0xVEuAecoxYfOBMHtKkY1cfR6mMCSqg1xmDBJFCgF1UMVdHsxtmAloUBZtgAb7eU4g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3fcaf59f19.mp4?token=AwT7Mnt5IVgRAkJk-_ttjwcOAI0NJKGwTL_OFF3gBLDfM56XcRt3OyhuG54ka6DuV64w-FxxVp8Q-8DtCTxmjJYx0rWCOlZLAE6gggt7DLig-CBpmjPqxiJHNafXWH_A3Yez4xaTZQYodVf4BwknnkkvUddW9SgdPFz7xWcgGFXyvtJmotlrSd6XnHCPT6SlmqQprRFd_nkYFlCid4TKgmTlS9qGboM-GPHqg-KXYFvJBH9tbS6dxmjLopM42UuYQHmujljtlHRRM3glKeVD0xVEuAecoxYfOBMHtKkY1cfR6mMCSqg1xmDBJFCgF1UMVdHsxtmAloUBZtgAb7eU4g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
جملات قصار و واکنش منصوریان به حکم انضباطی علیه الطلبه؛ از جیب خودم خرج می‌کنم رای برگردد! مستقیم می‌ریم CAS؛ یونس محمود ١۵ سالش بود من بوندسلیگا بازی می‌کردم
❌
⚠️
در شرایطی که دیدار الطلبه و نوروز در هفته سوم لیگ عراق با برتری ۱-۰ شاگردان علیرضا منصوریان به پایان رسیده بود، کمیته انضباطی فدراسیون فوتبال عراق حکم به شکست ۳-۰ الطلبه داده است.
😀
دلیل این تصمیم حضور همزمان ۲ بازیکن الطلبه با پیراهن شماره ۷۷ اعلام شده است.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 29.4K · <a href="https://t.me/Futball180TV/105304" target="_blank">📅 23:55 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105303">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mxlEwAw7dsG2VzgRk1pyzQFDwKZxwigo4Uf1mWKYESIqvyfivfjabiwRYG-Po3RlWKrYogq0W4CYzazZpY3XNWCURHb26Cm6Tl3XZmDcFi70DEhEOpqC0z2gfexeq00_lU6B6jLcsTbOVkvYEGjSrv9-XAIJBd3h7ZOhPT2eQwGPWZhhyt8jdi-mbuZAFMOqQ7mudcPriI0IcEpW15V3hY-1mjk-Qg6-jeKHQiq52f1T7UANslnwKs2XArRNCboFb5bMZAU8LUFTg8cAnXihWGQgDX-Vlz0PdEE8VM639vszDy9eEON3s8yp2u_8pEgOCoaaLLEORadQIavxtKJi4w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
رسمی؛ اندیایه با قراردادی پنج ساله به ارزش 65 میلیون پوند از اورتون به سیتی پیوست.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/Futball180TV/105303" target="_blank">📅 23:41 · 10 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>

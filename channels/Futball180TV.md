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
<img src="https://cdn5.telesco.pe/file/Rxp8Jq9QvP9p3SkvCpTHyogW1RcAwetaXZ9QozbjxXtqt2WklehWBWAZD0pXzBgQf38ftqx7Nf8zir0TntWrpp2iFvHyDW7NXhhVvNA0HBB1WJrdkMzSmJ9dDwAPaXDqOq6FSwcGnZxbjYo_wQD_H9099OR10x0oj5eR-Z-mol5l5qeALhCjH7mXw9ItxijRKKPM8pyCYESskuhdSAWglqCn2STWpxJUj4e5A-fBuJAbkSJsScdnUpMDlsDq-HKskEl0cXazeXG_H467uKlISMRKXfRuOWvVUBwcNFoz8IVSFYxwjLqBnVGSJfLNOvpb-vY-P66mry8nZe6Gszneaw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 فوتبال 180</h1>
<p>@Futball180TV • 👥 404K عضو</p>
<a href="https://t.me/Futball180TV" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 In the name of God; The only popular sports channel on Telegram: All for Iran...🖤We respect the copyright laws and follow the laws, Mr.@Durov...🙏🌹Contact ads:@TivaAds</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-31 18:34:28</div>
<hr>

<div class="tg-post" id="msg-107082">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2433cb0d35.mp4?token=fDbswZjmKyf0a6c4ngKyYoQFm-38xtRH_8fMAyElQxdKk3isO_BJkcsYSibQhIo5rXM1M4QqNgjf-fd3j2wT6u3h9eS8RpZ4Po_J2PQZfFnq7zQ0Bk2GivnO2-8ENvX-avW25oWdrJW6yME9Abhzx17X4ctbp4IiVhGg37FvrEOXGBhjSkkDqLoZBOTys4sibPpho3K94ngeRDAWL06vfOA7fAGo0E4zN3W-b6u5K500jCnm9dfDQ8YjcHIWlnrKZakVIIBrPIpDUviAs1Bjr8b6gB4iRemt4tfqpwXoVkt7gi0xuTUfYZbCHB4ruhz3uGWzKZisFGFfki7GxycT5w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2433cb0d35.mp4?token=fDbswZjmKyf0a6c4ngKyYoQFm-38xtRH_8fMAyElQxdKk3isO_BJkcsYSibQhIo5rXM1M4QqNgjf-fd3j2wT6u3h9eS8RpZ4Po_J2PQZfFnq7zQ0Bk2GivnO2-8ENvX-avW25oWdrJW6yME9Abhzx17X4ctbp4IiVhGg37FvrEOXGBhjSkkDqLoZBOTys4sibPpho3K94ngeRDAWL06vfOA7fAGo0E4zN3W-b6u5K500jCnm9dfDQ8YjcHIWlnrKZakVIIBrPIpDUviAs1Bjr8b6gB4iRemt4tfqpwXoVkt7gi0xuTUfYZbCHB4ruhz3uGWzKZisFGFfki7GxycT5w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇺🇸
⭕️
ترامپ: آمریکا و ایران قطعاً به نتیجه خواهند رسید؛ به هر طریقی که باشد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 2.14K · <a href="https://t.me/Futball180TV/107082" target="_blank">📅 18:27 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-107081">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6cae4c2a3d.mp4?token=INNuUvfiafSKiWbIw0vngbqI_K5XbQDC-Sq6PuWbKODhUipACbdkXor0K-EBsmOpXYZDlRozfUQzp9mt6GDtDX9weMegBwK205SGEHIJSOEulATvPqQWuP-Kb20rDMVjZqtFoveq550WHc9kUE0GFUp_ET86Ngzhyj7l14z5gp86fYyEh1RCbQcOjFWxDHdlFkHdmVmEJ7P4gpmeCvyGgOTu11fXMferCasJUVnKfWQc_ff1yQi68zpdrlIazlPnWtv0UNOuj5R7fcJnyS98I1jmj8HCJI1UDvgCdEX9AL6546g_nAcbIHidVJ1VKW-Mm255q7TNx3SZrOt6hEkf9w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6cae4c2a3d.mp4?token=INNuUvfiafSKiWbIw0vngbqI_K5XbQDC-Sq6PuWbKODhUipACbdkXor0K-EBsmOpXYZDlRozfUQzp9mt6GDtDX9weMegBwK205SGEHIJSOEulATvPqQWuP-Kb20rDMVjZqtFoveq550WHc9kUE0GFUp_ET86Ngzhyj7l14z5gp86fYyEh1RCbQcOjFWxDHdlFkHdmVmEJ7P4gpmeCvyGgOTu11fXMferCasJUVnKfWQc_ff1yQi68zpdrlIazlPnWtv0UNOuj5R7fcJnyS98I1jmj8HCJI1UDvgCdEX9AL6546g_nAcbIHidVJ1VKW-Mm255q7TNx3SZrOt6hEkf9w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
⭕️
🇺🇸
ترامپ: انتخابات هیچ تأثیری بر تصمیم من درباره ایران ندارد و تنها تمرکز من بر عدم دستیابی این کشور به سلاح هسته‌ای است
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 3.35K · <a href="https://t.me/Futball180TV/107081" target="_blank">📅 18:20 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-107080">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">🚨
⭕️
⭕️
ترامپ: باید تصمیم بزرگی بگیرم درباره اینکه آیا می‌خواهم ایران را نابود کنم یا اجازه دهم به حیات و شکوفایی خود ادامه دهد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 3.96K · <a href="https://t.me/Futball180TV/107080" target="_blank">📅 18:16 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-107079">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e271237b80.mp4?token=DmCkZtTyAdTRuQT--ms66eXgWooxIRg4MivA4olEXN_MFywlrofUbFkgxolW8LXdn2TG5tJquLslCR3e7SXzkeFfFQoq2eARJ-or61bL5RNVmNJQ-HYg7_mOBWLQbBaS2JtTPsV5VdTJb5wnYpbNKXTMtl15itjjLyU5EpOwybFkBb8DDc1woLPKYbtgvtL_tidlkhTC9CgsfuxpPnxjYliaNEyxmzFgjCdlUzWVTXvOrOfZPRuB68EWuAEeAWUQJmIdL640a1x7F6lP3ZXtkfQUSVk6O3BneAEEFdBZfJcRUS5qPh9NrIo6fjCfijIhmoK6KQK14SGWypsVpZlrNg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e271237b80.mp4?token=DmCkZtTyAdTRuQT--ms66eXgWooxIRg4MivA4olEXN_MFywlrofUbFkgxolW8LXdn2TG5tJquLslCR3e7SXzkeFfFQoq2eARJ-or61bL5RNVmNJQ-HYg7_mOBWLQbBaS2JtTPsV5VdTJb5wnYpbNKXTMtl15itjjLyU5EpOwybFkBb8DDc1woLPKYbtgvtL_tidlkhTC9CgsfuxpPnxjYliaNEyxmzFgjCdlUzWVTXvOrOfZPRuB68EWuAEeAWUQJmIdL640a1x7F6lP3ZXtkfQUSVk6O3BneAEEFdBZfJcRUS5qPh9NrIo6fjCfijIhmoK6KQK14SGWypsVpZlrNg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇺🇸
⭕️
ترامپ: ایران موشکی با قابلیت هدف قرار دادن اروپا ساخته بود
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.55K · <a href="https://t.me/Futball180TV/107079" target="_blank">📅 18:13 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-107078">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/380ee199f8.mp4?token=SCXsAgoaDI2e3qdcUkT4zANZxMPlkwCFtzS_QLqnAeqmLyZpX38e8SQVMYAsoch6fsQwZk5AIF3roUvl5nEEw2Osn9kLMqq48B42F9THLjGeHqKvuEM5HsFZNmBC62WFsZCYrgULyvFgpK-I98YNxiH6sGN43RlmdWMuy9UVK0FsMA8Hu-Cd9rxZvWq04lKSORp4ZowSD3LJpCgDTdhm4-E4bXNAYDMKcgM9ZctBxo0uu3tH1QzKbE_PXM4sFKDRZU_QdgwhC6rbHCDQ2_Y7KTwxz_FKH7vr9XgLHjb1pE4ny3-Y8rzFKKsVKf3nlASyFDkO-p6fqchVBJndpOiwWw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/380ee199f8.mp4?token=SCXsAgoaDI2e3qdcUkT4zANZxMPlkwCFtzS_QLqnAeqmLyZpX38e8SQVMYAsoch6fsQwZk5AIF3roUvl5nEEw2Osn9kLMqq48B42F9THLjGeHqKvuEM5HsFZNmBC62WFsZCYrgULyvFgpK-I98YNxiH6sGN43RlmdWMuy9UVK0FsMA8Hu-Cd9rxZvWq04lKSORp4ZowSD3LJpCgDTdhm4-E4bXNAYDMKcgM9ZctBxo0uu3tH1QzKbE_PXM4sFKDRZU_QdgwhC6rbHCDQ2_Y7KTwxz_FKH7vr9XgLHjb1pE4ny3-Y8rzFKKsVKf3nlASyFDkO-p6fqchVBJndpOiwWw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
⭕️
🇺🇸
ترامپ در سازمان ملل: به ایران در ازای پایان برنامه هسته‌ای و حمایت از تروریسم، همکاری کامل اقتصادی پیشنهاد دادم؛ اما نپذیرفتند
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.83K · <a href="https://t.me/Futball180TV/107078" target="_blank">📅 18:12 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-107077">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b4439db1dc.mp4?token=BK0fSH-g1Jt-Pw40hy3XKsYiguYgTzbdPBdL_jyn3SN_tHUentSTkju_lsJdpf26bITqzY3E5UMyrvjDU-AWrUuRjZzObJxjEMQIqeU3hJadwTxikFY4oIiF9l0XP64c34mI8Ih6JMI0SXZlrJdKj5WES7n6VXrE_QFlD7UoyJfaXL1BAsDPLxil8QFqkeRIdv1aPGDCXFC2m1VKBJOngrE1KiWaHnygU6IJLqNACKWtdxl8nJOMEKWIBKuBKLw7KkAVOmOaa6ZqHbBwB-hdA71YWXcPacx1f_g3fqr3iv4VGd719eWM1EbhpWd0zyHPcfgYiq9zKQFDJ8aguh_vqg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b4439db1dc.mp4?token=BK0fSH-g1Jt-Pw40hy3XKsYiguYgTzbdPBdL_jyn3SN_tHUentSTkju_lsJdpf26bITqzY3E5UMyrvjDU-AWrUuRjZzObJxjEMQIqeU3hJadwTxikFY4oIiF9l0XP64c34mI8Ih6JMI0SXZlrJdKj5WES7n6VXrE_QFlD7UoyJfaXL1BAsDPLxil8QFqkeRIdv1aPGDCXFC2m1VKBJOngrE1KiWaHnygU6IJLqNACKWtdxl8nJOMEKWIBKuBKLw7KkAVOmOaa6ZqHbBwB-hdA71YWXcPacx1f_g3fqr3iv4VGd719eWM1EbhpWd0zyHPcfgYiq9zKQFDJ8aguh_vqg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🎙
تعریف عجیب علیرضا علیزاده از نوید عاشوری که موجب پاره شدن دوباره عادل شد: گفتم ازدواج نکرده بودی، با هم زندگی می‌کردیم!
😆
😆
😆
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 5.31K · <a href="https://t.me/Futball180TV/107077" target="_blank">📅 18:01 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-107076">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3e179f3429.mp4?token=FsPVF0DODLQhfUuUk3SWSyLyYnips3_X-Hr1QKk3vD3XmOe9K8BBHp2YPG9XpVheGRODUquH3mGjabYHfzL-zl_9ZsbMxbyMkXLOmtNCfZNV6kSrvhdfzs7dQv_c4P1JNE30coHLzJ6khhlQJlH7PWFOYDGqhMt9_wxuNmdDw1Ccetc4nCxM76jq_Ejtz-gxDbtjHLyHBW0SzG24mKpr96V3G4WbV-nO1XCCT0iDYHaahKbxx5JJ4uShS72q79gDpLJBOlIlIBQyFLNKIS--oUVXnSji6RwY0b7dF9O_uZqTNGTsrfy2Z3PQTiHaioRIO41Oq-htuVpPXSoNsagT-Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3e179f3429.mp4?token=FsPVF0DODLQhfUuUk3SWSyLyYnips3_X-Hr1QKk3vD3XmOe9K8BBHp2YPG9XpVheGRODUquH3mGjabYHfzL-zl_9ZsbMxbyMkXLOmtNCfZNV6kSrvhdfzs7dQv_c4P1JNE30coHLzJ6khhlQJlH7PWFOYDGqhMt9_wxuNmdDw1Ccetc4nCxM76jq_Ejtz-gxDbtjHLyHBW0SzG24mKpr96V3G4WbV-nO1XCCT0iDYHaahKbxx5JJ4uShS72q79gDpLJBOlIlIBQyFLNKIS--oUVXnSji6RwY0b7dF9O_uZqTNGTsrfy2Z3PQTiHaioRIO41Oq-htuVpPXSoNsagT-Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
بعضی‌وقتا آدم فکر میکنه لیونل‌مسی تو زمین فوتبال بیشتر از دوتا چشم داره
😐
😳
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 7.17K · <a href="https://t.me/Futball180TV/107076" target="_blank">📅 17:18 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-107075">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/Futball180TV/107075" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 6.68K · <a href="https://t.me/Futball180TV/107075" target="_blank">📅 17:18 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-107074">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PbXdsNWAYzs41p9iduL7ZmBlkLm4UGFx2s8VK0AYO0gqNJ-n67jfEXn34NeU6aumiqwRBb5D_-TOtBQcQ2MzixV7D0lfGZOkHxQiOff1mOkadmFGl_mgn_2k5k2m82eL834Fs6ZmMUbriqbNhItSG3ymxWswey-XPRszcaSHzD9qygsjSBgMNnHYUA-ngajxm9aJ8bdrJMR8FYiKS9s1eBICCH904FX9Vo3lo1iatqD54iavgKUFtucTgNYsGMnnwFhhDC30SvOW2fd-OBVTTJsfQAh8AWB9rp9vHHrEMpBueeBr4eQNnbZPnDz9xo8vZeeAj3PFES5hdz0vbl2Uqg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🦖
مسابقات
UFC Fight Night
شروع شد!
🦖
یک شب پر از مبارزات هیجان‌انگیز، رقابت‌های نزدیک و لحظه‌هایی که نتیجه می‌تونه در چند ثانیه تغییر کنه.
مبارزات رو زنده دنبال کن، عملکرد فایترها رو بررسی کن و پیش‌بینی خودت رو در
TrexBet
ثبت کن.
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
<div class="tg-footer">👁️ 6.61K · <a href="https://t.me/Futball180TV/107074" target="_blank">📅 17:18 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-107073">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TvQTvCy-UGXTdYtVYWQCeh6EnyZOr7KUtYTZ2ntth0nSXh9Ktwi5ajMMiqMndLAS_bqzgt7wR4X_eDcS6uBUk8s_uAgnqzZcjGJhB4P1yDPtpiUzStMJEEqbCfpt6Y2cjdD0vKW-1A0GyyeRjfPk1QXfdcknf8AlKTGrQM2K2tNZdmZoW-rRIJcBJOwk3FL3qsTyuyfNP6ujV5KbGd3wr4KeHYW_i4veVbJOVromlBD-TdOKViGFms5lUPDGYAZal8IgXfaZU_KWpGnxypaon7T1viVa8tE3OaboDQZGVN7-Sei9PLTx-pM1k92aHNRtkUXTl9B7pnAFfRPhHUPCtg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏆
🇪🇸
لامین یامال :
🔻
به نظرم همون‌طور که می‌گن، توپ طلا جایزه بهترین بازیکن ساله؛ برای بازیکنی که متفاوته، از تماشای بازی کردنش لذت می‌بری و حتی فقط برای دیدن اون بازیکن حاضر می‌شی بری استادیوم. فکر می‌کنم توپ طلا برای همون بازیکن متفاوته؛ ربطی به تعداد گل‌هایی که می‌زنه یا چیزای دیگه نداره.
🔻
وقتی به توپ طلا فکر می‌کنم، یاد مسی، رونالدینیو و بازیکنایی از این دست می‌افتم. اونا متفاوتن و وقتی بازیشون رو می‌بینی، باعث می‌شن لبخند بزنی.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 6.35K · <a href="https://t.me/Futball180TV/107073" target="_blank">📅 17:14 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-107072">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rjjS0dshSJIOo3ewQoIK3lTSm0k9dvoKWFPbuIkj5m5HOjqywqTlOu0ZxnaxlFz6nS2g9TICRJmVucgJ6Fh6WDClm5Rx49HPD_T-IDH_fnaIbWvB4dG0_e4u84Mn4o9TAh514NwONk30N_Mo3cuypOJYEAePeIemkO_iTT6hiBJhMCBlcpUJnOQPEDpoXD__sUZ4Gt9laZ4oETcaS8WI6gKrFUJ4zh0_TmpOkRRFlNNnSXPmWgJ3wQvIWcD8bxhTyH3eUb1phV_igbD0VsY4B08gvXl0THt8nvCsG1N2CZRXbk9ln2y1a5KgCG_gJunqOohAyScIBYWJDFETMSsPog.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
قرارداد جدید آرسنال با آرتتا بزودی امضا میشه و این سرمربی به مدت طولانی قراردادش رو تمدید میکنه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 6.44K · <a href="https://t.me/Futball180TV/107072" target="_blank">📅 17:07 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-107071">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8ec90abeb5.mp4?token=GZ58PbUlv6UOPBqhEPuUd9msx_MLIdG7vRnD057r_1Tr0gdsfwsd0v02bmJ-Ou-Bf1xdgXR9Do88LW6OahqU05d9Q83PnlOpd1yuy64u3WQc9L5IiifVTmGXDFlWbsIkuoTKz_YU8RODoICGrv_luYRUcCpFIWRv6WI24F0oJ--RHnBZzixIlS2mHsK7HP0bIs7YWb79LbtRu_PJmd7_bdAbXIILklsRtwKcS8spr93Zbg-d41kKVpE3xKjF992Dg9tO0VYsZ5O9HyP6-K4oVzIugwDptYoTrLGqSgVIhsmDyBgX6XBIaDlwDlQSoZTt77HlVFSlX7zIPlOMQyFPcA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8ec90abeb5.mp4?token=GZ58PbUlv6UOPBqhEPuUd9msx_MLIdG7vRnD057r_1Tr0gdsfwsd0v02bmJ-Ou-Bf1xdgXR9Do88LW6OahqU05d9Q83PnlOpd1yuy64u3WQc9L5IiifVTmGXDFlWbsIkuoTKz_YU8RODoICGrv_luYRUcCpFIWRv6WI24F0oJ--RHnBZzixIlS2mHsK7HP0bIs7YWb79LbtRu_PJmd7_bdAbXIILklsRtwKcS8spr93Zbg-d41kKVpE3xKjF992Dg9tO0VYsZ5O9HyP6-K4oVzIugwDptYoTrLGqSgVIhsmDyBgX6XBIaDlwDlQSoZTt77HlVFSlX7zIPlOMQyFPcA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">کارلتو، نشون بده یه مادریدیستای واقعی هستی.
💀
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 7.16K · <a href="https://t.me/Futball180TV/107071" target="_blank">📅 16:55 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-107070">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/t9DIUVW5ZAcJe4nctCdvkT2ikBH20rz0WkkTbmi37YDi_ESPpl5kbAP1DuHsJlDYm6Jy7bsI2h5hJazrjdx01SO0xMhdAmGq6YzPNDz7XRFng-WY0UBXPQpkhmoSI571vIhCJ4IUTtcCh5SBGfXEwYdEdaoBt3Vu_wjMeqfhO2wU2bPqqstcOmzYY4t7cyWfMmd5Z397-YNZKeWKAUQ7a8ZejiObUCAUm1gNYiLkO6yrcLTK8W3CH5nQ8SwnjnNyM76-io90k-W1g-YSXQw_wdqSgt6WTHzTiP_lCjHob--qjnd4eAH2H3UK40l-cl0KSbW3VT6dFPWo9lCmKIfI8g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
✅
🇮🇷
سهراب بختیاری‌زاده برای نیم‌فصل خواهان جذب یک‌مهاجم خارجی، یک وینگر چپ خارجی و تلاش برای جذب محمد جواد حسین‌نژاد شده است. از سویی بازگشت خلیفه و گودرزی نیز جزو برنامه‌های بختیاری‌زاده در اعلام به تاجرنیا بوده
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.49K · <a href="https://t.me/Futball180TV/107070" target="_blank">📅 16:21 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-107068">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HsRslc9RyYkUCsyVjAGgRXDeTIYNqIcrEUA_O4s_geJLX2DFga3oucjt70xJgDbbkqNukWzr7xW42eZVXj_TW0F8AjD3QJQI81-IQ8yfSVFVSnvvpFuS-HiRbFh9L0tZO1eUNXlTcQGLr7gkNk-d9kHMGLbaNtzO8ZfihDZHA4H1trFFsHn_6rdGq79inC5rYKOouxvF6tEFH14dWHV2S9skiNOBm2LcV9tSSMjXyzh1x9TIJGBCU8VwGQX1hjZCrz5pTrhEcyUwEH1_pl_Cf0vVbv1rk2m75RWvj5RT6v9KGCTIB3Y72XOoO33JeAwxwmQFdABJrc-DOvMSa3J4Jw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
📱
اوج تلاش خداداد عزیزی برای درخواست بخشش از مردم بابت وویس زشتش
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10K · <a href="https://t.me/Futball180TV/107068" target="_blank">📅 16:09 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-107067">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EpQN2oX7RexmtbYgSpvpznSfddddxJY4meBUMFz9jobwewiJDlP5PZwpFMjHPa6j0zoyv56nYfhGcqz93UK0To2_tQgKqRP3fGsGEbYr92yfAB9-a2l2Ze4D-O6oQceiCiKNjcWduZD26Ri6y7sN7oOssiIBCt0cw7-fiqd89gnzlQd7hm4q7VytyrqRWuBikfcGvKmtYYWiakhGn5YnGPn-XiVTaJfIIboLb1n7SCr3nj-Y-6GvCg2WEhUiMEGKw_wVu2wgL7vfBsa68ZmY507e9AkRSqcu2XlwOdaD9rAuGujAF3RtHyVyOap9wtORQHZ7Vkqx3QLBIklwmwVetA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇫🇷
عملکرد فوق‌العاده موناکو زیر دست فلیپه‌لوئیز
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.94K · <a href="https://t.me/Futball180TV/107067" target="_blank">📅 16:05 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-107066">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ejWLkTb-fSAaBlH-QCuB9CVrIdKlJSZSlYLl7xF7qAiz51YfXL4iCnyDSThT4VWz0ujofc0hRbPo-Pj3ATJsXC4lFa1sPAsyl_QL0mpf3JPaWVm3yxREH33bryE5O6i6uelWGPyxhFw-YGfUePFsnU9-fLHN-4-Rx8_Ue1SyqoBsoMGCi9bxSWh6dwrJXkWd-Bq8_pVlFgKpnfA6IadVrGs7rhYv067vCgKERzHyKgjiZg1H_17Ng_2sPkbXMG8w3-ZgKprfbpG3WhIINZZRhXW72QnH_c8K_bo_JbCuorv_G1DoVCNf4emuuufF21sMXPwMaO1PKeYwjQ6Qkk5zKA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چهار
تیم با ۱۰۰ درصد برد اروپا تا پیش‌از فیفادی جاری
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/Futball180TV/107066" target="_blank">📅 15:40 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-107065">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/q_xtuGzSphCfLRbP4QuyWRhjObdm43cMVPcG7zk2pDbARgDySrf-I7m6D1vGHkKTw7KkrHgshCbB04pzPkFfMPD9m5_J-3BuWMELNsDLZj_QAyHOxNSqfmPfUr_ew_9vwqgKOGUEjabIMekRfoMZihnXsKbzOX9PmSaoKt5S5rQO9hz9ylzseYvk74n0-6PLv62RSIB7kAMGFh79cYTZ17gYhL6KsgjqWdLD8AC0otyLxHZwR9UNazMH49q5r9APl2_89rDwjx-N2ny335HO9zJEiz3PTd0m_SZkl13SBuhZX_GgZJGsQeOHKhb9DABDgKYQI_2BmZ8w6PizuWNWHg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
❌
⭕️
عربستان و چند کشور خاورمیانه در آستانه جام ملتهای آسیا با فشار به فیفا به دنبال تعلیق فوتبال ایران هستند.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/Futball180TV/107065" target="_blank">📅 15:15 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-107064">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/74cce70e5a.mp4?token=itsRfMWXP9X8O8HnDzXobvtWUdlKSTgS6LErx1XigfU0TBH6-uyo_90kTnSJDw8GPfJL_nB3p4yUJqkILgUBUwd4Ge_iZqs8CAFtK0BPVkEx4c09F9qO9CiptgIaavNDMZHBTXbDPydsWGwZHRD5ZGrKQPraBuX44BEu5k2Nl4a-1Rk3oEQ9FxkxHhqbOIzviwbxxFXWEMnMXz7M84NGdBxacrDlUZRqxFZgEXxMSY9RDTs-6sL1D9_l6xs9FNSDwKnCFHM_-thk5Akr4VmU2h-7XElaFarFzcHmiNX3Kn3yjVP0P1SqRpeb8KpG8hjY15AsJw4MZfPbJiky0343Dw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/74cce70e5a.mp4?token=itsRfMWXP9X8O8HnDzXobvtWUdlKSTgS6LErx1XigfU0TBH6-uyo_90kTnSJDw8GPfJL_nB3p4yUJqkILgUBUwd4Ge_iZqs8CAFtK0BPVkEx4c09F9qO9CiptgIaavNDMZHBTXbDPydsWGwZHRD5ZGrKQPraBuX44BEu5k2Nl4a-1Rk3oEQ9FxkxHhqbOIzviwbxxFXWEMnMXz7M84NGdBxacrDlUZRqxFZgEXxMSY9RDTs-6sL1D9_l6xs9FNSDwKnCFHM_-thk5Akr4VmU2h-7XElaFarFzcHmiNX3Kn3yjVP0P1SqRpeb8KpG8hjY15AsJw4MZfPbJiky0343Dw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👀
💥
مرور هفته‌عجیب فوتبال در اروپا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/Futball180TV/107064" target="_blank">📅 14:50 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-107063">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e1af88a540.mp4?token=TTph6eWjpYjAT43dPx04vTfHA0hIYEi4w0eUU3qKsRjxdiDGyBFI6djDYUUleEFtsozt3cXdZChhS1YgGZqoxNpoeiuD-bUoC2_ud1oOIjeAi9VKGfYIQ1dZe9qzD124X40mybIl0wT1_PaaxKRLwyleQ0WcXNma9_4UjOtstYHAbXRicPWTfIR5RNn4FJ-82-pV1cabX2hNJTEhGbFP4oRBGl2KcNcFKrIW-oeTsTwaT-gTMux-pCfpCZPaAN_XNq9nDUWZiVkJ-VyJT55WGtLFNi37nTrZ2pVgsT41nYla3dbYYPHbAQD-T3FpsFdJFSt9_8BSDzGXRY7ELVVbTA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e1af88a540.mp4?token=TTph6eWjpYjAT43dPx04vTfHA0hIYEi4w0eUU3qKsRjxdiDGyBFI6djDYUUleEFtsozt3cXdZChhS1YgGZqoxNpoeiuD-bUoC2_ud1oOIjeAi9VKGfYIQ1dZe9qzD124X40mybIl0wT1_PaaxKRLwyleQ0WcXNma9_4UjOtstYHAbXRicPWTfIR5RNn4FJ-82-pV1cabX2hNJTEhGbFP4oRBGl2KcNcFKrIW-oeTsTwaT-gTMux-pCfpCZPaAN_XNq9nDUWZiVkJ-VyJT55WGtLFNi37nTrZ2pVgsT41nYla3dbYYPHbAQD-T3FpsFdJFSt9_8BSDzGXRY7ELVVbTA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">😏
🇪🇸
پست‌سمی تیم رئال‌بتیس از جدول لالیگا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/Futball180TV/107063" target="_blank">📅 14:25 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-107062">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/068efa824d.mp4?token=GwPuKiL2pwf0EcasZo-5GxNGfJTLwZv-ehXnCrx28czI8AFpq4och-NXbMcTRQ2KW0fc3BM7Lp37h4u5P7rc6CKT9J7jhvsbXbx8lwtqlbVvwXXuEFlZ4LLGRAfR4SRxjjVPa2K_MHhs9cQy81nHE3xxbgJqG_7CfYOEu4sPekD-N7F9wpDqFYwfTPluvHL5CbW-5JxJEblYHwKWca0fB_D4C1NDWurXX1YqrDM6AeWovHklcZV1icPh5KPKMRd0QekSzw9a3jJAVXP5RAZW1LbQ1VWbnL7kwrAxIY-eZf72hnr82nh7GGXW3mgw1kHk88Bggwb-gfn5qwVGF-Yn1oi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/068efa824d.mp4?token=GwPuKiL2pwf0EcasZo-5GxNGfJTLwZv-ehXnCrx28czI8AFpq4och-NXbMcTRQ2KW0fc3BM7Lp37h4u5P7rc6CKT9J7jhvsbXbx8lwtqlbVvwXXuEFlZ4LLGRAfR4SRxjjVPa2K_MHhs9cQy81nHE3xxbgJqG_7CfYOEu4sPekD-N7F9wpDqFYwfTPluvHL5CbW-5JxJEblYHwKWca0fB_D4C1NDWurXX1YqrDM6AeWovHklcZV1icPh5KPKMRd0QekSzw9a3jJAVXP5RAZW1LbQ1VWbnL7kwrAxIY-eZf72hnr82nh7GGXW3mgw1kHk88Bggwb-gfn5qwVGF-Yn1oi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🙂
🇮🇷
🇮🇷
شوخی ابوطالب‌حسینی با عدم قهرمانی پرسپولیس در آسیا و ناکامی‌های استقلال در دربی به سبک هوادار مشهور منچستریونایتد
😆
😆
😆
😆
😆
😆
😆
😆
😆
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/Futball180TV/107062" target="_blank">📅 14:01 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-107061">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/709cbff54e.mp4?token=pQUJGSWD5tAVWNqLeE7GVWQFNlHMUyXuZBT635_gs7OR16EVhi-AmdTzYkweVGY3s23Gr6Ld3hHjPw215BuJW9Vh2eZ9Czfkdsixi-FW_eyP0CII6iP3FkxCJNaDcxm6eokWsbg_mmzGttLvna-jwdoUdB44j3OZzb7JiL5gfCSUEUwPVAbTeE_ws3CF3yBzq79cXPeJQj0E0TUmIANZcBEbj6l12O3n2NNpL72KGxIec7sl7MgKPCqonF4owbBrp6AhTJOyozXEFGjPo9vpU4QupQIZLFi6nVJQOCWzWmh3OrHeFwYgDQGDbMy_lGZo8UEr4tasbWouDSP1PE778w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/709cbff54e.mp4?token=pQUJGSWD5tAVWNqLeE7GVWQFNlHMUyXuZBT635_gs7OR16EVhi-AmdTzYkweVGY3s23Gr6Ld3hHjPw215BuJW9Vh2eZ9Czfkdsixi-FW_eyP0CII6iP3FkxCJNaDcxm6eokWsbg_mmzGttLvna-jwdoUdB44j3OZzb7JiL5gfCSUEUwPVAbTeE_ws3CF3yBzq79cXPeJQj0E0TUmIANZcBEbj6l12O3n2NNpL72KGxIec7sl7MgKPCqonF4owbBrp6AhTJOyozXEFGjPo9vpU4QupQIZLFi6nVJQOCWzWmh3OrHeFwYgDQGDbMy_lGZo8UEr4tasbWouDSP1PE778w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇸🇳
🇸🇳
سادیو مانه با حضور در زادگاهش در کشور سنگال، مبلغ ۲۰ میلیون دلار را برای احداث یک پروژه با اشتغال‌زایی بیش از هزار نفر، سرمایه‌گذاری خواهد کرد. مانه اعلام کرده که بیشتر دستمزدش در دوران فوتبال را صرف رشد منطقه محروم خودش در سنگال خواهد کرد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/Futball180TV/107061" target="_blank">📅 13:45 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-107060">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/548065ddaf.mp4?token=uhlI1_lKCjwriiVu4VDdjkVZz2LHSLABGN7l6vJWeo_wxssD-XSeKGsbB419yxNAjDkQW1fD2ghpRFFvena4ranGrsLQXeipv20hvJrRr91QUWn-YZPSUKU7kAbOUPIgU087m0bdxMAXv5ZiI-FErwpd6BQkgDDsBFzTG4w6TbKWXeNWOaGHgGGyhVA430TpXP0ab8uSAiDbXVjJFgXtjTiuxP1vkO-78yvFNJMJIL57aqo5x1oXe74Lp4bt1gc7OJl8OSAeAXDQgcjMCD-IoLCFMPqDrfpjTJDo9A3B46at7NbXk0ggxeMH2jjAr7rSN0wb5mnJrMH25ysXhACP0w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/548065ddaf.mp4?token=uhlI1_lKCjwriiVu4VDdjkVZz2LHSLABGN7l6vJWeo_wxssD-XSeKGsbB419yxNAjDkQW1fD2ghpRFFvena4ranGrsLQXeipv20hvJrRr91QUWn-YZPSUKU7kAbOUPIgU087m0bdxMAXv5ZiI-FErwpd6BQkgDDsBFzTG4w6TbKWXeNWOaGHgGGyhVA430TpXP0ab8uSAiDbXVjJFgXtjTiuxP1vkO-78yvFNJMJIL57aqo5x1oXe74Lp4bt1gc7OJl8OSAeAXDQgcjMCD-IoLCFMPqDrfpjTJDo9A3B46at7NbXk0ggxeMH2jjAr7rSN0wb5mnJrMH25ysXhACP0w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🙂
علت جدایی ابوطالب از عادل فردوسی‌پور
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/Futball180TV/107060" target="_blank">📅 13:35 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-107059">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b38289f78f.mp4?token=s0QGHYJcWSWaRk4KJg8BQ8DjdjFA-RLGvaHAzGpj8LCdVRpO_ZZs6c8O9ClK7E27KV0opBv6fTys1cvWl9YEd_z0GiWxu_4ZVn5yNibebqdDuJxvLB-MgsrVBF5LVj2QNnMU0TawSZAK64SeIjCixqHDE_0zd1axiSvS9hTId_q55uZ0BaRDJ6vPpsNOadW4n0pyTgaotHWZgWCgq5XJE5goxjZha4XKGS4jn7004tCTIwA7CgXYJFhOigHZKvknybERaDhwsBfCjNtPXBW4FM2aHF8WCcFM7wIAkJX4d7jm03nda2V4ssRDzsrcaENkjrJZaBZtLl-SAQTyxzs_6A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b38289f78f.mp4?token=s0QGHYJcWSWaRk4KJg8BQ8DjdjFA-RLGvaHAzGpj8LCdVRpO_ZZs6c8O9ClK7E27KV0opBv6fTys1cvWl9YEd_z0GiWxu_4ZVn5yNibebqdDuJxvLB-MgsrVBF5LVj2QNnMU0TawSZAK64SeIjCixqHDE_0zd1axiSvS9hTId_q55uZ0BaRDJ6vPpsNOadW4n0pyTgaotHWZgWCgq5XJE5goxjZha4XKGS4jn7004tCTIwA7CgXYJFhOigHZKvknybERaDhwsBfCjNtPXBW4FM2aHF8WCcFM7wIAkJX4d7jm03nda2V4ssRDzsrcaENkjrJZaBZtLl-SAQTyxzs_6A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
❤️
‼️
دیس سنگین ابوطالب به خداداد عزیزی: قلب آدم صاف باشه نه پاهاش، شما قلبت پرانتزیه آقای خداداد عزیزی!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/Futball180TV/107059" target="_blank">📅 13:08 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-107058">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/19fc9edd61.mp4?token=T4pWRefd2-auLeYzncGuQuGkTJoBLXoE5QdQv2KAhw_Nob8_wGKvMqn1SfETLMRTjcnUMrmJQgak5w0NVLl--0pFhQWfHqO-52ZAS7Hntb0LPipNjk0g5_PU7qqFb70jMqPblK1BDOADjL3VlgLLc0kWu1iwj652L1MBRVHUqjG1yr66x_1RnaZnQeBPvyXZ8NDWy5wd-wr20vsVyJGhrz2l9baK4X6OMYyWQw2YL0X6IQLwIov6U77HUIXAIJZZPSPoyY9bdClK_alFZKFYcck78BoUx8-o15CVHu0cjQzA_v1473kRmolXvzyzg-2YQV6ZHD7AUKey5dvqvPmgHQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/19fc9edd61.mp4?token=T4pWRefd2-auLeYzncGuQuGkTJoBLXoE5QdQv2KAhw_Nob8_wGKvMqn1SfETLMRTjcnUMrmJQgak5w0NVLl--0pFhQWfHqO-52ZAS7Hntb0LPipNjk0g5_PU7qqFb70jMqPblK1BDOADjL3VlgLLc0kWu1iwj652L1MBRVHUqjG1yr66x_1RnaZnQeBPvyXZ8NDWy5wd-wr20vsVyJGhrz2l9baK4X6OMYyWQw2YL0X6IQLwIov6U77HUIXAIJZZPSPoyY9bdClK_alFZKFYcck78BoUx8-o15CVHu0cjQzA_v1473kRmolXvzyzg-2YQV6ZHD7AUKey5dvqvPmgHQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
😆
‼️
ابوطالب حسینی ویس لو رفته خداداد عزیزی رو مودبانه ترجمه کرده
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/Futball180TV/107058" target="_blank">📅 12:37 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-107057">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Nxu1REMRxhqvMrVb4RafdpYlqSIjNtBkfU2o4cTAZALYlmZSnCuoG_dT6Mu7Eeo2jmWbF1JpZQgE0yCy-I5ebfYPA_3ty2myRc3fci4xkURdgdozyshiDMM7ROh5G82_MmuIzCMslfXfWP2G_y-gM6hoJEzozFgkmXk6mupXtrGF-RJyJ49EEH7MUT6YDkwN6htQVV2bMt0_L3gNpqAVy29jQjzR4ssduo4joPKEaRO6pKMzbKE52T3xSwqGQt64FBtw23Ije4bMDz5Y1so5zxMNMJ_2IGkoP5nRSM6-Lb69EW8Gvdk3JLoxQva-DXPKllx-5ECub_saIV9bOJ4Jcw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آقای ابوالفضل جلالی فکر کرده در عصر قاجاریه داریم زندگی می‌کنیم. چطور اینقدر راحت دروغ میگن
😆
😆
😆
😆
😆
😆
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/Futball180TV/107057" target="_blank">📅 12:30 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-107056">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/H_Se-SuPYTTCVElS_1Re-ngyhptFqgaMkqUtBbkkjO28pxnA7TMXtjFyMvuxZfAczfMd5TrEs_i3KgL-Fft5lnir1Pil6YllufS5ziTAkQswyoyaf0zpepVQ1HxMxoBiCbADQnI_lPJ-b_6wZlxGt_AjVT-6gUpXJE6PmxyvGeXvSMi4GJGoQtgjJhQyflXCWaiUG9CF2VhtpJu6NxVtPNgb0dXmw93_FLKWmHTRQYKftuPgklDhWtTZzfDo-LPSK7dchW7dzcPdlju8VPeIeTOLx0vS0IIdjyXA1jmAF4Dw_wE5xlhrxv3I-0dfV2TJBMUZRrcUB-SXDqHk21yudw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
جمع سن سه نفر جلو: 110 سال
احتمال فیکس شدن هر سه بازیکن تو جام ملتهای آسیا هم زیاده. جوان‌گرایی بی‌نظیر امیر قلعه نویی بعد از سال چهارم مربیگریش در تیم ملی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/Futball180TV/107056" target="_blank">📅 12:20 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-107055">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1aa420985a.mp4?token=h5QHsx2ApRpJMVR4BV5dM39c4Oju8AolqNLq7zqOPkBESCDWCheJ2BzVT_PKxR91H9qHy1033IZ7tEs7-n59j1OcL11RThkhHSJUBuldJ6er-6bkQd9ANDAfzL3dT0cs8Qwwxb5y1iX14XMuNQWn7MJxRwFM0u1EXU4H74h28bb_YhC5Amw1SgsVPOJTB7Dz4jZSTsLjj4qrn8XfwC8wNN9tu00KlaaWNg2NW_7GtANCjp7IoKAcMdEjIb7BcjIx_S8OQRvQCcAq4Yz55hvckxuVM8OpJTAkicjegCeSbXmNxLDcvlJNBwFvrthSg6FjSS_-qoCo17xkUKse_4DPUA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1aa420985a.mp4?token=h5QHsx2ApRpJMVR4BV5dM39c4Oju8AolqNLq7zqOPkBESCDWCheJ2BzVT_PKxR91H9qHy1033IZ7tEs7-n59j1OcL11RThkhHSJUBuldJ6er-6bkQd9ANDAfzL3dT0cs8Qwwxb5y1iX14XMuNQWn7MJxRwFM0u1EXU4H74h28bb_YhC5Amw1SgsVPOJTB7Dz4jZSTsLjj4qrn8XfwC8wNN9tu00KlaaWNg2NW_7GtANCjp7IoKAcMdEjIb7BcjIx_S8OQRvQCcAq4Yz55hvckxuVM8OpJTAkicjegCeSbXmNxLDcvlJNBwFvrthSg6FjSS_-qoCo17xkUKse_4DPUA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شما هم از فیفادی بدتون میاد
🙄
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/Futball180TV/107055" target="_blank">📅 11:55 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-107054">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3c092ad06d.mp4?token=SIXfExxcTp2Hs4NaJw8RHAY8suqzhj89IMgxlqkuovHmBQfr1mcDC1TOVVDBLjQpvTuVFJsN5TUDDUnNmOIhlIhEje0WbKEH_EP1PzbMRxzx_PhRJ2s2UmB1tzQb6Co-JJycIWIb30D4SYYpr3bnMXO0ls_WjfB52QAH-07XhES2HRusYywgeluKsbqBDDlo-_XW1QbG1141-Se5RwIB94hOak9ug9TNjTU23xCYnDkperogIuTePZ5iZde5XYx9rHh2-XUOCnxmc8f-jcUtH7eiLstgIodvwN39INBAHtK6WpJKoOK6JMQTxCdDPOIV6-lYYnhcK3kYl1QWuQdVxA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3c092ad06d.mp4?token=SIXfExxcTp2Hs4NaJw8RHAY8suqzhj89IMgxlqkuovHmBQfr1mcDC1TOVVDBLjQpvTuVFJsN5TUDDUnNmOIhlIhEje0WbKEH_EP1PzbMRxzx_PhRJ2s2UmB1tzQb6Co-JJycIWIb30D4SYYpr3bnMXO0ls_WjfB52QAH-07XhES2HRusYywgeluKsbqBDDlo-_XW1QbG1141-Se5RwIB94hOak9ug9TNjTU23xCYnDkperogIuTePZ5iZde5XYx9rHh2-XUOCnxmc8f-jcUtH7eiLstgIodvwN39INBAHtK6WpJKoOK6JMQTxCdDPOIV6-lYYnhcK3kYl1QWuQdVxA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
🇳🇱
اولین تمرین لاله‌های نارنجی زیر نظر ژاوی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/Futball180TV/107054" target="_blank">📅 11:40 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-107053">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/Futball180TV/107053" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/Futball180TV/107053" target="_blank">📅 11:39 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-107052">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pvs4FKoB-KAIoZCyB70qNE1-x6W1ImzMd05VYSNAKh5CCkqrdJ-AW_QkbtnLWerWZI0aWbPX25sr4QM31bkmPYN9vxdoufoLCSlX15W4frcT0pqZssXfkZ3npelpBgP8XbUI9Ayg18h3Pd2I7YhKBCSJhPgkVdAw10C0IdGecCG1mBGDw4UhNeP5G72m85I3A5j9Yxp1aCglZxB7ICj531BozJWoe075E3PVEvCZNcpKhihAnWTY6fjBevXgx54xiLVvopGpcwnJoIJR6_hHPktpNtDDgI7whZFKmOcK_ysWgFXJUfdqpCLKgiMNjXE5xbMMV_ejrlZrhI0xrMg80Q.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/Futball180TV/107052" target="_blank">📅 11:39 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-107051">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/O5JSOOLoajzxOpFU5rKmpViaKxE5gTd6UlD9HbdlUiBNsuYWajI9ihENo3f9sDQUmMHbS-MXRlUF_89gVjYxRpcfIZi1nYxc1jpWDsd8FuBnVndsRB-arpqtw6sWqZ1cx7WDMJc-PlQBZnp7xknQUhg5JbGHbrSzcO6FMM4mlbGfPr2jOnrZRcBDUuc-VCyvljfuZQrTtpMPWtbaKnr3Wi45beelz2K3fIHGl387x7Ug-XLiTHu3DOs-ikw1caM6APtFrzdSqbssXMgZ3U9tX7OGsp1wH63VZLPP52JaE-J5LILRQ-z18X4kwKCdCx1GfVa0HDcoRn4nX0J7av9yXA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👤
لیونل مسی ۲.۶ میلیون یورو برای کمک به ساخت مرکز مراقبت و درمان کودکان مبتلا به سرطان در شهر بارسلونا اهدا کرد.
✅
این مرکز تخصصی سرطان کودکان در بیمارستان سنت خوآن دِ دئو بارسلونا قرار دارد و ظرفیت رسیدگی به حدود ۴۰۰ بیمار در سال را دارد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/Futball180TV/107051" target="_blank">📅 11:32 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-107050">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b26eae7147.mp4?token=qRHopVpmjKRcGewJxQsDN-xPkczp8FmLeD0vgpaKM0wvMNF9Mu2mMgO3lh8qrVa3ETyjp82MJ90jksdwuchGyBdmcRpfWEY9iPHSqPh8sj54M5-3Emj1B9Rw6h_3783aeb3_S2evcblGY-fn5i0xQD97JvkH_cHq2vIPcFRpGle2MGkg3TEWiFGurMkycxc-1NYVtEnQsfmaDPKNqtwPEwhyeEU7Hmb-SvlV7tNMHg1maJq15sTh5s_N16ozbj3xgaWh8YgGfBVWcohpChS5UBt-TL6yY3IrEiwnQ2Xy193Usp7i117zTaI9iI6-yme-KNC7IEDi8uxkXo8SLztACA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b26eae7147.mp4?token=qRHopVpmjKRcGewJxQsDN-xPkczp8FmLeD0vgpaKM0wvMNF9Mu2mMgO3lh8qrVa3ETyjp82MJ90jksdwuchGyBdmcRpfWEY9iPHSqPh8sj54M5-3Emj1B9Rw6h_3783aeb3_S2evcblGY-fn5i0xQD97JvkH_cHq2vIPcFRpGle2MGkg3TEWiFGurMkycxc-1NYVtEnQsfmaDPKNqtwPEwhyeEU7Hmb-SvlV7tNMHg1maJq15sTh5s_N16ozbj3xgaWh8YgGfBVWcohpChS5UBt-TL6yY3IrEiwnQ2Xy193Usp7i117zTaI9iI6-yme-KNC7IEDi8uxkXo8SLztACA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
▶️
در این ویدیو پیرترین موجود زنده دنیا را مشاهده ‌می‌کنید، کوسه گرینلند که بیش از 390 ساله که در اعماق اقیانوس زندگی میکنه؛ این کوسه زمانی متولد شد که آیزاک نیوتون، موتسارت و چارلز داروین هنوز متولد نشده بودن؛ البته که گالیله 70 ساله و شکسپیر چندین سال قبل از دنیا رفته بود.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/Futball180TV/107050" target="_blank">📅 11:05 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-107049">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7b6b29a98b.mp4?token=pzo8_zY93H1vfF6hR7zCf068LMYJyyiSveYKA_cxB2BSNSVG6htfrAwiCq1UZACYfEQ6wr_5YcV5628ILwd2JDKyarNb8AU0_oo86i1uqQqrU0qtXynK_MpIZ1gHwhgALl873pM6uYOlDqaPKui-a0RgesLFQtMaXZ5JSj6IP2I8s-NWVJojZezDmKThrW-YJLXws4ewXrNEIeX9z6JYY9KpdbUZPSeSn91HOVYRNcePugK5bZrP2wtosizkbdMMqcpsh8QyE-EjrsHdtPu-qAAGFVjWwGEYaMS8yKCGm7dbjEJsthi5WIC-i16jbLGwup5NkSpjn2u4ZV5XSHusKQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7b6b29a98b.mp4?token=pzo8_zY93H1vfF6hR7zCf068LMYJyyiSveYKA_cxB2BSNSVG6htfrAwiCq1UZACYfEQ6wr_5YcV5628ILwd2JDKyarNb8AU0_oo86i1uqQqrU0qtXynK_MpIZ1gHwhgALl873pM6uYOlDqaPKui-a0RgesLFQtMaXZ5JSj6IP2I8s-NWVJojZezDmKThrW-YJLXws4ewXrNEIeX9z6JYY9KpdbUZPSeSn91HOVYRNcePugK5bZrP2wtosizkbdMMqcpsh8QyE-EjrsHdtPu-qAAGFVjWwGEYaMS8yKCGm7dbjEJsthi5WIC-i16jbLGwup5NkSpjn2u4ZV5XSHusKQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پاییز با بوی نو کتاب فارسی شروع می‌شه
🍁
✏️
حتی زمان ما، شروع مدرسه ها صفای دیگه ای داشت ...
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/Futball180TV/107049" target="_blank">📅 10:40 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-107048">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b6ef37fb80.mp4?token=gTAcPOsRnvuvX5d1ByEPo2UjkrDyyaLO4iYKdVjuv_nckHLUAKoXoEZVqwf7T7n-SN0MXqo3ySucQvz38N9gvmHyokEY-HuhNCh6iRvrqEvzCHc7924386dgFDLPwOL2RpQlHKeK9L_65xph4_PQcNM2FHctIAMz2JXyjr_OdS9gAh_z9rrgUmgOnx1brOlIGUxVh2obIAJEbb5IC8X2f1T-yHssYqYPri5f59RPNAHDmkLMTShfBEl-nvffLs7mFap3IsTAJYhC7Q4A1B12j2ZsbghLQ7neP4JYGmT0ZoGeWMc7P1FgYtcx9ULDP4gTBGEnabbh6g8P8KkeUbIEdA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b6ef37fb80.mp4?token=gTAcPOsRnvuvX5d1ByEPo2UjkrDyyaLO4iYKdVjuv_nckHLUAKoXoEZVqwf7T7n-SN0MXqo3ySucQvz38N9gvmHyokEY-HuhNCh6iRvrqEvzCHc7924386dgFDLPwOL2RpQlHKeK9L_65xph4_PQcNM2FHctIAMz2JXyjr_OdS9gAh_z9rrgUmgOnx1brOlIGUxVh2obIAJEbb5IC8X2f1T-yHssYqYPri5f59RPNAHDmkLMTShfBEl-nvffLs7mFap3IsTAJYhC7Q4A1B12j2ZsbghLQ7neP4JYGmT0ZoGeWMc7P1FgYtcx9ULDP4gTBGEnabbh6g8P8KkeUbIEdA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">آقای ابوالفضل جلالی فکر کرده در عصر قاجاریه داریم زندگی می‌کنیم. چطور اینقدر راحت دروغ میگن
😆
😆
😆
😆
😆
😆
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/Futball180TV/107048" target="_blank">📅 10:15 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-107047">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/090ef42156.mp4?token=mAydgFE1JTizWLCkyLKxzhF8IYegg7hkUZqXh7QVraci0TtA2G9Z56IerZiq_mMPeG6LKqLAld3sZFthcCw-4WPvLhZkyWnkJ3SzoJGr-YoL1fruGuQ09D_EPM05lUJH_z-QsmWGymNEYiiiFaXWZR6gsSFLBGGVCKSpO_68VEnqhVXiSuvOp5BwSmddmUgu3gtDGSE3g1jdOkMhleR864EhbcI0XZyL2a0YsjahYCe8Y_ei3uV4UT_7vJ__YHmqq40ZPBPSmA91OoZSeCjKZIioSu3Wt1zrdOMANXM9BShO6ED_3rWMYs1xHRKwQMc5Y5GdZILc0IEhe5KyFKbb5w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/090ef42156.mp4?token=mAydgFE1JTizWLCkyLKxzhF8IYegg7hkUZqXh7QVraci0TtA2G9Z56IerZiq_mMPeG6LKqLAld3sZFthcCw-4WPvLhZkyWnkJ3SzoJGr-YoL1fruGuQ09D_EPM05lUJH_z-QsmWGymNEYiiiFaXWZR6gsSFLBGGVCKSpO_68VEnqhVXiSuvOp5BwSmddmUgu3gtDGSE3g1jdOkMhleR864EhbcI0XZyL2a0YsjahYCe8Y_ei3uV4UT_7vJ__YHmqq40ZPBPSmA91OoZSeCjKZIioSu3Wt1zrdOMANXM9BShO6ED_3rWMYs1xHRKwQMc5Y5GdZILc0IEhe5KyFKbb5w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🎙
🇮🇷
بابک مرادی: مربی داشتیم (کمک فرهاد مجیدی) که آدم بسیار فاسدی بود. همه فوتبالی‌ها میدونن فاسده اما هنوز داره مربیگری می‌کنه
+احتمالا این شخص فراز کمالوند هست
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/Futball180TV/107047" target="_blank">📅 09:50 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-107046">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d781ba027e.mp4?token=R-zp3Vz_eeiZp99CCHJpI8wOiSPDe33b9ABQQEW-VOrI6lpImNKAR8b_OGt_RA1APmwE3bMWf-IHUUeq0MkclLLT0yKcs2966PJ_sDcyg-SU9QTsJOr7ZERaxKWalG7awR_RdAn7R2A0ebKVWHBQ1PpGFWcYUwXjt1EXL9u-ns1VmNABOFctJROvY4pqpeVz_ZrOxxH0upuMthy1lSoAha3i9LLbjQEN0EVuOGmJxCJkeEZbNymqDaS5jME9ywJ2t0byoPzkmAR9QCR-6rvRtJZax0S_R1hbc3SlEpEnzadDHVoCe49UuTe2V7p73tuVNaDoAqh2xSzz8XWRb4u1qw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d781ba027e.mp4?token=R-zp3Vz_eeiZp99CCHJpI8wOiSPDe33b9ABQQEW-VOrI6lpImNKAR8b_OGt_RA1APmwE3bMWf-IHUUeq0MkclLLT0yKcs2966PJ_sDcyg-SU9QTsJOr7ZERaxKWalG7awR_RdAn7R2A0ebKVWHBQ1PpGFWcYUwXjt1EXL9u-ns1VmNABOFctJROvY4pqpeVz_ZrOxxH0upuMthy1lSoAha3i9LLbjQEN0EVuOGmJxCJkeEZbNymqDaS5jME9ywJ2t0byoPzkmAR9QCR-6rvRtJZax0S_R1hbc3SlEpEnzadDHVoCe49UuTe2V7p73tuVNaDoAqh2xSzz8XWRb4u1qw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✔️
🇮🇷
🇮🇷
تعریف و تمجید حمید مطهری سرمربی فولاد خوزستان از سهراب بختیاری زاده
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/Futball180TV/107046" target="_blank">📅 09:25 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-107045">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5ed15f390e.mp4?token=TksvfNhaY6BqMBRtkEMl_0SVkOt2V_myxI9DiTNoOArQhyCPbrslsiFXHnofQFx8Qha7FBuAtnMHaH_SJa4lnnZc41BMscvVD2Y0Nv7hgy--Djy4A56dbjARUO5hPdM6W5eEXPDGl5qaKu0cnUMdKxutqNEi70dqL-nRJVgV2sJnus8FW-oXnskX3zkx0d-pmrA1-OWWATvxvDHJftOlvz0SsxjL6ZIDsiqFVtiOTCSytXu2_WU-SkJsMMRgXMMn_Z7RFnsSG6fA8jrEjH1zlEguxoh8s_Vhn5Xh2ntnIFuidOWhdYLfaECNS30ehnKGrqE-Alve5M4WxjPBdFCBnw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5ed15f390e.mp4?token=TksvfNhaY6BqMBRtkEMl_0SVkOt2V_myxI9DiTNoOArQhyCPbrslsiFXHnofQFx8Qha7FBuAtnMHaH_SJa4lnnZc41BMscvVD2Y0Nv7hgy--Djy4A56dbjARUO5hPdM6W5eEXPDGl5qaKu0cnUMdKxutqNEi70dqL-nRJVgV2sJnus8FW-oXnskX3zkx0d-pmrA1-OWWATvxvDHJftOlvz0SsxjL6ZIDsiqFVtiOTCSytXu2_WU-SkJsMMRgXMMn_Z7RFnsSG6fA8jrEjH1zlEguxoh8s_Vhn5Xh2ntnIFuidOWhdYLfaECNS30ehnKGrqE-Alve5M4WxjPBdFCBnw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
⚠️
فوش ناموسی بلینگهام به مادر داور بازی با اتلتیکو که شکار رسانه‌ها شد!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/Futball180TV/107045" target="_blank">📅 09:01 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-107044">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a69b72fb04.mp4?token=AqyI9jhV_bwvvhaxmlVfrIYt_SUPLgZrt_jO-EcPQ0KyslMzNoPldr0NR4dxVeTpvvLkN06WIh9IngphUnSsbXOlzGL-jYSAoczZpRrZOLeCI68RsYzovsbT5TFWiKsRmaeK0FOLTLBMoe-dM-2ehsPZrLLAHQFjhHTcGxKLFTkqP3XOdQ6eLmnC7Lw43EJpKflFUDtKejLxFprJp6P17YZ-DHx1jBLYxSUYvmVor9lq09z5JZj-tv2UiZq56lArjwZj4xA9KYzZKHLk0IRtDxNx4dzv1xJ-cGWszABCmXY6ilhdEg-tu7wtnpPtysTgPMySP1tyBx97paMQ-X1znQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a69b72fb04.mp4?token=AqyI9jhV_bwvvhaxmlVfrIYt_SUPLgZrt_jO-EcPQ0KyslMzNoPldr0NR4dxVeTpvvLkN06WIh9IngphUnSsbXOlzGL-jYSAoczZpRrZOLeCI68RsYzovsbT5TFWiKsRmaeK0FOLTLBMoe-dM-2ehsPZrLLAHQFjhHTcGxKLFTkqP3XOdQ6eLmnC7Lw43EJpKflFUDtKejLxFprJp6P17YZ-DHx1jBLYxSUYvmVor9lq09z5JZj-tv2UiZq56lArjwZj4xA9KYzZKHLk0IRtDxNx4dzv1xJ-cGWszABCmXY6ilhdEg-tu7wtnpPtysTgPMySP1tyBx97paMQ-X1znQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
🙂
شعر خوانی جالب قیاسی:
«مثل رابطه سهراب بختیاری‌زاده و صالح حردانی
مثل حال دروازه‌بان بعد از تک به تک شدن با یاسر آسانی
یا مثل حال اتوبوس تیم ملی بعد از جریان کنعانی»
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/Futball180TV/107044" target="_blank">📅 08:03 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-107043">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/Futball180TV/107043" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/Futball180TV/107043" target="_blank">📅 01:16 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-107042">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VPTJGHGRLoG3dZszpT0lGqNyHwEVeSbrk5Rn8MGwEj_Jp4EnvXyEcV_8I8TOwSq-JtmAMeRJttWKOfOxgdxMqTRI7y4e6Lo2d0CemLJs4Bq9IS5P0o7S-w0aZocvVOi6mnn5v2lwDMAlM7HGhSLk-Iwptl1hSp6F9MIbDfQgibnP5e9fJikS0zoeBafVm2tBfLn6oyAxeACC7DNPk8T6IChE4FuqLe59R9GzjB27BGrGH5Tulgegj3OnTxXZ3xS09x59b2CR250DpJEMzsP_FVG9tNvvJGG1rD3rhPQWCv7vbI-akwArAPhOLRE28v9G80gMq-NfM_tGn9TCee0uHw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🦖
آماده‌ای هیجان واقعی رو تجربه کنی؟
🦖
در
TrexBet
، دنیایی از اسلات‌های جذاب، بازی‌های کازینوی زنده و لحظه‌های هیجان‌انگیز منتظر توئه!
🦖
صدها بازی متنوع
🦖
تجربه‌ای سریع و روان
🦖
هیجان در هر اسپین
🦖
🦖
🦖
🦖
🦖
🦖
🦖
🦖
TREXBET — PLAY. PREDICT. WIN.
https://TrexBet.com
T.me/TrexBet_Ir</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/Futball180TV/107042" target="_blank">📅 01:16 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-107041">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a32c5c8c60.mp4?token=Bw8AT4cAuC-na5ivkPkPr9Has40BxGRP2Htp3LDQdgX9LQ1r46yUZfJ92bi1eKap66ayY7a8uWkXj1oFlmdIgslC0yHVFY2_eEnSuHFyqGzTVXs5dHQcy9Bdse54CzZHA6OpiVyJBJyt1g7tejV3CbEO8XtHBUGJrtakkwfBImKO4wMHa_6OFx99zzjgZwmq0_apdB0TPcuV3e1RwNGvJ6vQPMzZ8BF8sOARZGgHiE2I7Zsb8TZMkHrAiyzpVDsEv1dXZdGZ3pvvHPIF37F3uZSwPrGL5qVHV45e6t5P_9j_lnS9VSDL5eutx2_AP1j_i1aio4bBNrLsCdoco4JH_Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a32c5c8c60.mp4?token=Bw8AT4cAuC-na5ivkPkPr9Has40BxGRP2Htp3LDQdgX9LQ1r46yUZfJ92bi1eKap66ayY7a8uWkXj1oFlmdIgslC0yHVFY2_eEnSuHFyqGzTVXs5dHQcy9Bdse54CzZHA6OpiVyJBJyt1g7tejV3CbEO8XtHBUGJrtakkwfBImKO4wMHa_6OFx99zzjgZwmq0_apdB0TPcuV3e1RwNGvJ6vQPMzZ8BF8sOARZGgHiE2I7Zsb8TZMkHrAiyzpVDsEv1dXZdGZ3pvvHPIF37F3uZSwPrGL5qVHV45e6t5P_9j_lnS9VSDL5eutx2_AP1j_i1aio4bBNrLsCdoco4JH_Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🐐
🇦🇷
رونمایی‌رسمی لیونل‌مسی از پیراهن ویژه خودش در آخرین بازی ملی با آرژانتین
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/Futball180TV/107041" target="_blank">📅 00:55 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-107040">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0b37185041.mp4?token=n0YyOWsI4y-b1DY8WZTOwAlBDIJnDnFx88APASe8JHWag5fy6FzeJcXKxB8cgbdEevBC5A5Ls0c6oENM9gBSYmSWh_StVHYw80ysajTkyyoFjRMm5qaEohAdNNL6XtFr0gLEDVa_Z79gIBE1uRClb2U3LwF1beI2PhwfESg-1xQd38lXYEjbncqvIIqGKLn18NX1ZOqTPGGOKyR7fdNXm9j6XE7xZkCZPO7TS3C0AHzKkezGyhjTNvkmOFMng-QkkoKn8sz1tKjaxZ5zsJ5pdKoInw6lyE4fxNCavFwwnE44WC1fKxm7WbQU7mbqlido3BeLxT9so3X5hMVs9LTLWw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0b37185041.mp4?token=n0YyOWsI4y-b1DY8WZTOwAlBDIJnDnFx88APASe8JHWag5fy6FzeJcXKxB8cgbdEevBC5A5Ls0c6oENM9gBSYmSWh_StVHYw80ysajTkyyoFjRMm5qaEohAdNNL6XtFr0gLEDVa_Z79gIBE1uRClb2U3LwF1beI2PhwfESg-1xQd38lXYEjbncqvIIqGKLn18NX1ZOqTPGGOKyR7fdNXm9j6XE7xZkCZPO7TS3C0AHzKkezGyhjTNvkmOFMng-QkkoKn8sz1tKjaxZ5zsJ5pdKoInw6lyE4fxNCavFwwnE44WC1fKxm7WbQU7mbqlido3BeLxT9so3X5hMVs9LTLWw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
پیام علیرضا بیرانوند به میثاقی روی آنتن زنده: اگر نظام وظیفه اعلام کند من چه زمانی باید به سربازی بروم به جان 2 تا بچه ام فردا می روم سربازی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/Futball180TV/107040" target="_blank">📅 00:45 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-107038">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vNusIgU0QQjhz0w-KSLAJurBa2sWsKvUcMFij9ELBoDHq_F9_3evgjKb7oUUl4FFKPwA78j6HRMH1uxFk1gsRjo9b5ewfV3mSG_MF9bkS6_oerouexChtFotf_Bh000QBOUrfdW_F2XWkshOO04JrN10k4CIeOM33yaEwC6mLxVfCqfDV350zW-UZBlYKlM39hWMhpdHef1bWFyRnRnFRmBwyyumrUx9Q-One7XPl8oFsu0Tvul0Rk0zifHYc31JzHzXS6jXlwHowO7OGPAFR8FwGWpa20gihMjl0AnVMcyOOEaigHqVU0BwkwNPlQCrQpe1iC15_UwqgvD0yuzU4w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/BFOf0fSRuzABONVl6Ou1vJONZdLvc1ghq7Iv5cTJ58rx20qTAfX-fA7EtvE5VyczrYI97I0DsUuAYfgXlkieW4R2oEr3D23U64BnkztNvZozpzM7PBDzWtKjshobISmO7b1NsKDo6rWnBa-7U0QWmvGJXqurnbWVDyAbqenpRBa7TCJf00WQ03C6pJlD5iaOPKBsTwi5QiSj8GvqKRUtTI1hRSz7Vq3RSWNCJVlzNgz1su6wMgtz6t851Tw5OYNjT8ZkDSi0l1itUCZiQM3vUU_Aeb-yVATIpFN8ZZZ3OsKpVF64mqtzTMVNV8NQnkJ6GBvoDybxkt7i2aYOn8AKYA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚨
❌
دلیل عدم دعوت اللهیار صیادمنش انتشار این استوری در ایام اعتراضات سراسری دی‌ماه ۱۴۰۴ است که باعث شده حداقل تا چند سال قید حضور در تیم‌ملی را بزند مگر اینکه به مانند سردار آزمون دست به پاچه‌خواری بزند!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/Futball180TV/107038" target="_blank">📅 00:24 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-107037">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">🚨
⭕️
‼️
اللهیار صیادمنش: در اردوها به بازیکن احترام نمی‌گذاشتند. حرف‌هایی که جوان‌ها نمی‌توانند بزنند را می‌گویم. در این چهار سال ۱۰ بازی دوستانه روی نیمکت بودم، ۲۰ دقیقه هم بازی نکردم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/Futball180TV/107037" target="_blank">📅 00:22 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-107036">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">🚨
⭕️
🎙
اللهیار صیادمنش: تا این افراد در تیم‌ملی باشند حتی اگر بخواهند هم دیگر برایشان بازی نمی‌کنم. در اردوهایی که زیر دست این آقا(قلعه‌نویی) دعوت شدم هم چیزی به من اضافه نشد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/Futball180TV/107036" target="_blank">📅 00:09 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-107035">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">🚨
⭕️
‼️
🎙
گلایه تند اللهیار صیادمنش بابت ربط‌دادن عدم دعوت به تیم ملی، به مسائل اخلاقی: می‌دانستم قلعه‌نویی هیچ اعتقادی به من ندارد چون اصلا هیچ مسابقه‌ای را از لژیونرها نمی‌بیند!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/Futball180TV/107035" target="_blank">📅 00:07 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-107034">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SsfNAnx9uRnC0MNPmfqiVLkD5cEhks0mBnKENJ6FpOY9pPUP_Z_yFoTC5H86VNJrGNSRS5swbrgrILudS-dkgM5lQs5BRhHTgvKWDzeh-FsZzNMmMsGa59OMrAqmKOtOKD54jJcKIbVyMeR_1Q__Mn5p3MatGRWQwsleYrjThdIf9juGPy-7wbU-o1iOXxbkKcrvtIAo5JaqTDv7TjM091zpLisZlcklhEHD9CQAoWveBCIjs56ALGcAFbFbGj7SVbkeJ45F06YfljOGPIDrHFWsThAF5G4d9aYqhTU438Xo5-VJtlzqiXjfTo3Tqb5d2DE2f0PC4lH_JyxRQMBiSQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
🇪🇸
خاویر‌تباس رئیس لالیگا:
🔹
باخت دیروز رئال مقابل اتلتیکو صرفا جنبه فنی داشت. درست است که اخراج یک بازیکن حریف نادیده گرفته شد اما اینها بهانه خوبی برای باختن نیست. امیدواریم رئال‌مادرید واقعیت تیمش را ببیند و دست از جنجال بردارد!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/Futball180TV/107034" target="_blank">📅 00:06 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-107033">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8238d2e025.mp4?token=TUut6RswOxmo624kKraGk2sHmOfPMdFy-NqShg9JEeeVFj20KdrKej98qYqMIcyKQgilu84qlxO606ju8NPD6APFwGp4K0xeXbSVjkDiGfVXESJxEEfrQCUHeY4jHEE6mN3Kl64jRGAGNx2U3a2vpDF7bpWlR1yYH7BRyHWVMxUMZ6213Omsq37RTeTHWDwWronN59g5dfZu_9P-YWKJi3C1DZHdRRujw0gjteO_OKYAXMc_hdhpYZGndmTIj6wHo8NuuQD058fmKw9_Jzp-lyr_VwXdSLC-WRa3ZHYH5YVDCD2X-fEmErDe-_YTzKynV0tMBgo2pOurrgdEuNC4EA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8238d2e025.mp4?token=TUut6RswOxmo624kKraGk2sHmOfPMdFy-NqShg9JEeeVFj20KdrKej98qYqMIcyKQgilu84qlxO606ju8NPD6APFwGp4K0xeXbSVjkDiGfVXESJxEEfrQCUHeY4jHEE6mN3Kl64jRGAGNx2U3a2vpDF7bpWlR1yYH7BRyHWVMxUMZ6213Omsq37RTeTHWDwWronN59g5dfZu_9P-YWKJi3C1DZHdRRujw0gjteO_OKYAXMc_hdhpYZGndmTIj6wHo8NuuQD058fmKw9_Jzp-lyr_VwXdSLC-WRa3ZHYH5YVDCD2X-fEmErDe-_YTzKynV0tMBgo2pOurrgdEuNC4EA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
میثاقی: اردوی تیم ملی تمام شود سربازی علیرضا بیرانوند تعین تکلیف می‌شود
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/Futball180TV/107033" target="_blank">📅 23:58 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-107032">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/37e4355f95.mp4?token=i25aS632vrVFW-zzOVKdinnczfmfh4kHidpCqKB6n80RHeRLYd1iYOBljauMcvU0hBWOJnOVqMyRAtu8tKfAnlOI4gjOyGIbLDE-aHqEk33iNo1SwpXNRJTmZwizW_ykIoo9pEh1vke6cPjiAyPUamWB3w_kkvJp-TDMmGM6hjsvZDAMKaqZUoZrGOGaxQ1uj-zfWqdRxZ4euT4meHKL7QkOPXm4gohoSSFLZz0ZUsnUCEkyt6oSH5mIUSQZha7rn5eBYJPNoPj3HhvyUH1YD4Ykydt-yBQfAONesRV5_rxGLZHUzZ4MJevJegfeUjOfWywkeZGwrZJY7tn4E-a4UQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/37e4355f95.mp4?token=i25aS632vrVFW-zzOVKdinnczfmfh4kHidpCqKB6n80RHeRLYd1iYOBljauMcvU0hBWOJnOVqMyRAtu8tKfAnlOI4gjOyGIbLDE-aHqEk33iNo1SwpXNRJTmZwizW_ykIoo9pEh1vke6cPjiAyPUamWB3w_kkvJp-TDMmGM6hjsvZDAMKaqZUoZrGOGaxQ1uj-zfWqdRxZ4euT4meHKL7QkOPXm4gohoSSFLZz0ZUsnUCEkyt6oSH5mIUSQZha7rn5eBYJPNoPj3HhvyUH1YD4Ykydt-yBQfAONesRV5_rxGLZHUzZ4MJevJegfeUjOfWywkeZGwrZJY7tn4E-a4UQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇮🇷
ابوالفضل جلالی بازیکن پرسپولیس: برای هواداران استقلال احترام قائل هستم. آنها زمانی که در تیمشان بودم به من انرژی دادند. در استقلال بهترین عملکرد را داشتم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/Futball180TV/107032" target="_blank">📅 23:50 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-107031">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a19a96e43d.mp4?token=FjK60sAOHezjyPtzE3Qekhiug08DaJgMsFFIq36UtyvTj0TRy0eGNqKMMG8L64nh7PSjP2RtFw0x4i1N7q5E3FBjYyVbvTqa76JsQWFBi64lsbYOG9A_kqFwZo4QMZEzynKD0vkmashmmSbbTvKxkLbi2n7kMaQ_y0JX1brX6oTSFN0UhkjaSOvK7vYDPFTceGsEmpAf2039eILwNTEuD6Sd3QjiZnthH0tZakgxLWqqxGrhz-uvanfvPHpN6XoeDYBSzNHjl7P3ZiV8uUURdQhWCDqbKD9ZGwVMU4hZIQCc1fXB7Vk-q5h2LqwmKvaGvr-Y8_YG7uawwn27W4FL1A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a19a96e43d.mp4?token=FjK60sAOHezjyPtzE3Qekhiug08DaJgMsFFIq36UtyvTj0TRy0eGNqKMMG8L64nh7PSjP2RtFw0x4i1N7q5E3FBjYyVbvTqa76JsQWFBi64lsbYOG9A_kqFwZo4QMZEzynKD0vkmashmmSbbTvKxkLbi2n7kMaQ_y0JX1brX6oTSFN0UhkjaSOvK7vYDPFTceGsEmpAf2039eILwNTEuD6Sd3QjiZnthH0tZakgxLWqqxGrhz-uvanfvPHpN6XoeDYBSzNHjl7P3ZiV8uUURdQhWCDqbKD9ZGwVMU4hZIQCc1fXB7Vk-q5h2LqwmKvaGvr-Y8_YG7uawwn27W4FL1A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
🎙
🇮🇷
ابوالفضل جلالی مدافع پرسپولیس: الان طرفدار پرسپولیس هستم، عاشق پرسپولیس هستم و سرباز این تیم هستم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/Futball180TV/107031" target="_blank">📅 23:44 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-107030">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f6fa04dad9.mp4?token=aXxrK6rZzaTYjVR0UdtYkXuekXv83_dJn-4cmTrhItpEAcE-2weWLUcSpjNa0nyYqvJVQK7o6nS8mu4ZJDn4DkmdzCDMnP9nAnEhqnYCs_dmIp606Gpg6XfyKc3zJtKW2Lo_G6MsVj_JlKQ3rGiGnfu1xaH0-wpaXl1sAjb5dV1Kvz_WvLsnScsJpgW7l3YrxipE74FLTWuTrPuMMXMvyyC4z6PuHNFKSI5-SOnIdNoBOD_qH3ejb_1TV1KCgCFOsHiyHVdqR9zmxKd1uMqjCO9tKn-dcohyqDBDaj-IN2zAsFw5fuAtgaMujzHhHlQVMYE1GYc-66cmmAdEf6dtpA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f6fa04dad9.mp4?token=aXxrK6rZzaTYjVR0UdtYkXuekXv83_dJn-4cmTrhItpEAcE-2weWLUcSpjNa0nyYqvJVQK7o6nS8mu4ZJDn4DkmdzCDMnP9nAnEhqnYCs_dmIp606Gpg6XfyKc3zJtKW2Lo_G6MsVj_JlKQ3rGiGnfu1xaH0-wpaXl1sAjb5dV1Kvz_WvLsnScsJpgW7l3YrxipE74FLTWuTrPuMMXMvyyC4z6PuHNFKSI5-SOnIdNoBOD_qH3ejb_1TV1KCgCFOsHiyHVdqR9zmxKd1uMqjCO9tKn-dcohyqDBDaj-IN2zAsFw5fuAtgaMujzHhHlQVMYE1GYc-66cmmAdEf6dtpA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🎙
💙
ابوالفضل جلالی: ساپینتو شاید از قیافه من خوشش نمی آمد که به من بازی نمی داد چون از نظر فنی مورد تایید او بودم/ جالب است رامین رضاییان هم همین مشکل را با ساپینتو داشت
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/Futball180TV/107030" target="_blank">📅 23:43 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-107029">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/11cbab4a72.mp4?token=GHu3zOZtAHDAEjl3ND3QCNHQ0AtcFxYn4ugA26PfkqBmGZw2wn3fSYwttGnwOBCiiFrlhxWfolWMpoFqEIr-tGMBqtkoUXMlsFBJjwZ-thE7VkENvJmHYblNHj9RklolDnptyHxep0_oixUtgTTsoVV_WpqDNzOWP-OVeJOUbq4nDa-kk9rGeMzvDS97M66jXjC4f0RikR502t4n70RtIkZO3r4pQzJJdWJq4Kqzo9REw0dHBD0ZDSlfk94tALt5dvrplqdh0TkqG37qbMYMSnG6GzXBFnkLn99DCvVLhViguiGFWlLsMSqHV7x9Or33Dlo-vhiufsvJgtbOg6Sqow" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/11cbab4a72.mp4?token=GHu3zOZtAHDAEjl3ND3QCNHQ0AtcFxYn4ugA26PfkqBmGZw2wn3fSYwttGnwOBCiiFrlhxWfolWMpoFqEIr-tGMBqtkoUXMlsFBJjwZ-thE7VkENvJmHYblNHj9RklolDnptyHxep0_oixUtgTTsoVV_WpqDNzOWP-OVeJOUbq4nDa-kk9rGeMzvDS97M66jXjC4f0RikR502t4n70RtIkZO3r4pQzJJdWJq4Kqzo9REw0dHBD0ZDSlfk94tALt5dvrplqdh0TkqG37qbMYMSnG6GzXBFnkLn99DCvVLhViguiGFWlLsMSqHV7x9Or33Dlo-vhiufsvJgtbOg6Sqow" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
سعید الهویی مربی تیم ملی: درخواست کرده ایم که از اول دی ماه اردوی آماده سازی تیم ملی جهت حضور در جام ملتهای آسیا را برگزار کنیم
🔴
میثاقی: با این وضعیت بعید می دانم تیم های لیگ برتری بازیکن به تیم ملی بدهند
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/Futball180TV/107029" target="_blank">📅 23:26 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-107028">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/12081ba765.mp4?token=cSTIQdQBp64SmL12fDgUMuHhQGB3dhUqpTOWj7Glv8U5dFlURNP3Yod9h626NF8dgouW4AIEULLdF6iqrwE_PpMBE9F9FJ9sCsE7EuHJiuvkGYpMDKkW09NjAOuJGtOkXhRVX1KyH7Vm6pZ8YrSxsDNsqeaCPocEJ8XcHd77DP8EV-k5Fh4eXjYuTCAz08MWvaTV1RBCpcuj0fzXASn8s2bcVjYnSbLOH4-B19De_xswWGTQZfQVNYYubqHml8qd12ZUe-uvx4HYUCOq24COmtEiBP_Isl3yKFc4gpdaotyselcBFcAoXtURbicFc647dsxEgn7jL2EelhzDwDTAhQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/12081ba765.mp4?token=cSTIQdQBp64SmL12fDgUMuHhQGB3dhUqpTOWj7Glv8U5dFlURNP3Yod9h626NF8dgouW4AIEULLdF6iqrwE_PpMBE9F9FJ9sCsE7EuHJiuvkGYpMDKkW09NjAOuJGtOkXhRVX1KyH7Vm6pZ8YrSxsDNsqeaCPocEJ8XcHd77DP8EV-k5Fh4eXjYuTCAz08MWvaTV1RBCpcuj0fzXASn8s2bcVjYnSbLOH4-B19De_xswWGTQZfQVNYYubqHml8qd12ZUe-uvx4HYUCOq24COmtEiBP_Isl3yKFc4gpdaotyselcBFcAoXtURbicFc647dsxEgn7jL2EelhzDwDTAhQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
⭕️
سعید الهویی: پرونده حضور احمد نوراللهی در تیم ملی کلا بسته شده است و این بازیکن خواب و خیال تیم‌ملی با حضور قلعه‌نویی را از سر خود بیرون کند
!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/Futball180TV/107028" target="_blank">📅 23:08 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-107027">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tZXnogdWw_QxruUSfv20muOCbmpQmJNGP263iBzExdqlHBHjkGdaQZ0OtqmtojkgkI5xZlLZHAHnE6XL3zXdsfPTJmLYi8OuV2lMPNcdfs0aBPk9Dhjiaj64TnqML9thD6MtqT3cDpo6SfdOuzXDZOHoPcn9xzC6X6JE9c8UTa25fCAo8F4E2_UAF6483XyVKt5L9dOFU-bu3jUY8CdMjNsdETA0wBU8aik6Dk6jV_5RAmk7U19SEtPSuhWFkhQ3b7-PJX3oLBTjDuesSHY05nzwbs1WraFW2_T_HVLaYWUgutPipADI_Xx9k9jsZniNnbK5cBPXNNNf64NjTsry1A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
‼️
سعید الهویی: الهیار صیادمنش به دلیل یک سری رفتارهایش به تیم ملی فوتبال ایران دعوت نشده است
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/Futball180TV/107027" target="_blank">📅 23:05 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-107026">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c45095faec.mp4?token=T_M5UO0moSWZA-2k-_2HoKhbgXsUJc1fDB2S8YSXHCvgODP2PZUM4D2Ij-kxhQyBk8NvrEj4OIdz-dZyAL0HAUWjzo4_rvkS2Qn-2SwCmb43QJc9wmS_tfZ-d_BMq94XCsU_d1NjyR4OVEgnC0bdf3OnbEIHlRt2kc3sGfaRLPfwV9sj907DzdM1ZY7J5AvbOojNRAX0S--tcOUb9TEVvAN_95HSXmbgpcAEnJM2Hk9msdkIuOhWqYD4NKUaIJj-vj6YJhNdVl17aJP2GUgAdN8JOowaHUyor40T4Zl1UrglIZPgAfu7cPhB87BBEDPzcHq9KjwQ1bG_Qh8LE3YM6g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c45095faec.mp4?token=T_M5UO0moSWZA-2k-_2HoKhbgXsUJc1fDB2S8YSXHCvgODP2PZUM4D2Ij-kxhQyBk8NvrEj4OIdz-dZyAL0HAUWjzo4_rvkS2Qn-2SwCmb43QJc9wmS_tfZ-d_BMq94XCsU_d1NjyR4OVEgnC0bdf3OnbEIHlRt2kc3sGfaRLPfwV9sj907DzdM1ZY7J5AvbOojNRAX0S--tcOUb9TEVvAN_95HSXmbgpcAEnJM2Hk9msdkIuOhWqYD4NKUaIJj-vj6YJhNdVl17aJP2GUgAdN8JOowaHUyor40T4Zl1UrglIZPgAfu7cPhB87BBEDPzcHq9KjwQ1bG_Qh8LE3YM6g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
سعید الهویی: الهیار صیادمنش به دلیل یک سری رفتارهایش به تیم ملی فوتبال ایران دعوت نشده است
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/Futball180TV/107026" target="_blank">📅 22:58 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-107025">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">‼️
🙂
🎙
به مالکوم گفتم Bro, Easy Football!
کلماتی که از درگیری شدید علیرضا علیزاده با بازیکن سابق بارسا جلوگیری کرد!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/Futball180TV/107025" target="_blank">📅 22:46 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-107024">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">🚨
‼️
انتقاد تند عادل فردوسی‌پور: پدرمون در اومد این‌قدر با ازبکستان بازی کردیم!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/Futball180TV/107024" target="_blank">📅 22:11 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-107023">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5ee3019bfd.mp4?token=qtog0vlaxWBGycKsw6x7n7DPKORP-X0CiiWllL3EyV9yl2Ryoz9FY_qrEy6UN2jbFatZefJZn5XvvTZeGjHiHDxQTnFZ5TVU5AUa0BPhwPXN-9mBAlorNMF7ecQMRkh12aBum06LXbsuPPGu3PtCjRztSLhDAv8cBTjgzmAogJCDhQCVpAkEQyO2wu1s5BOBCQmrmVsTgLQ0DRgfEF2zkHBhdoN8ygUcIOy2z0nZPsJyB487Nja8-2cLVD6gUwWCUv3N0VTrIfwvN90Vp9R_UAi7mWpdEnjha2Jpd4IQ_2KZWdOMHU45TUpqWim9uITjnFGAl_hcMzZWc5xGHcghOA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5ee3019bfd.mp4?token=qtog0vlaxWBGycKsw6x7n7DPKORP-X0CiiWllL3EyV9yl2Ryoz9FY_qrEy6UN2jbFatZefJZn5XvvTZeGjHiHDxQTnFZ5TVU5AUa0BPhwPXN-9mBAlorNMF7ecQMRkh12aBum06LXbsuPPGu3PtCjRztSLhDAv8cBTjgzmAogJCDhQCVpAkEQyO2wu1s5BOBCQmrmVsTgLQ0DRgfEF2zkHBhdoN8ygUcIOy2z0nZPsJyB487Nja8-2cLVD6gUwWCUv3N0VTrIfwvN90Vp9R_UAi7mWpdEnjha2Jpd4IQ_2KZWdOMHU45TUpqWim9uITjnFGAl_hcMzZWc5xGHcghOA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">در ادامه شاهکارهای داورای لالیگا این صحنه رو هم دیروز داور بازی دپورتیوو و بتیس کارت قرمز تشخیص نداد!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/Futball180TV/107023" target="_blank">📅 21:30 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-107022">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">🚨
‼️
🇮🇷
باشگاه تراکتور با تهیه مستنداتی درحال رایزنی با نظام‌وظیفه برای کسری یا معافیت علیرضا بیرانوند است. تبریزی‌ها مدعی شدند که بیرانوند دچار مشکلات روانی است و به همین دلیل خالکوبی کرده و باید از ادامه خدمت معاف شود
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/Futball180TV/107022" target="_blank">📅 20:53 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-107021">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Y0JcNqL3JyxoBpwlbyMpawDxC80Y0-rl-VVqbbpqGEFkmnF09tRCYdpWgjEuCqDOgqPnceKUrAm-ro3-cVha3jHOBHjmTrYiulh-t7Z1p3C9l80WqusDnzmRW8G8QQAzis-BeD_7Qt1rJpcUuoXsTD9GZMhpJsGDnWHm85AaelN8-4bL_Z3CQiWjQ-TfUOiaemtQ2UHBR65jBsR4LxRbVVfwWubq4O3YpQ2S4WFrQCTxxSk6kAK-UBvXA4tdC00dxWVve5dMdMNkoTgrkSaV8Yfvi7Q35-Vu_taICaTTvE92ACegiurReyz-SN_4VFA_PmT5K1bP1jd5M6U95_WO2w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
📊
مقایسه آمار نیمار و رافینیا در بارسلونا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/Futball180TV/107021" target="_blank">📅 20:45 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-107020">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/690c7befaf.mp4?token=O45DNC4cTf3HxyTxydjtpXOdsjr8YRzm1juGjlUH8uUqtaD9bXuxgbh1g9V30qjfZrqbHUh8WVZ1om1Ze4s-AvxT4k2NHh1vc9OPJ60eQrnbAmF3ItVLi2iaQgixCdwIeQk5FbNS-nUgkIRVMx8vQwDI_fzNqSu1b4tnsSUc8zGb1kAUf3aGSOqY3bLMFDvMGmoOY7hjJIPyotgxgfOmdWQnClnYYGRlkSnfuuCe46C3yRBAyX4sBujmj158yvWFslKRJccfHiL12WSUm2wudJDkwH0ovb-wZjRylnaJIkYhZMXWqliMQSlxh30igI--errkKbbYaznp2gIlwLc14Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/690c7befaf.mp4?token=O45DNC4cTf3HxyTxydjtpXOdsjr8YRzm1juGjlUH8uUqtaD9bXuxgbh1g9V30qjfZrqbHUh8WVZ1om1Ze4s-AvxT4k2NHh1vc9OPJ60eQrnbAmF3ItVLi2iaQgixCdwIeQk5FbNS-nUgkIRVMx8vQwDI_fzNqSu1b4tnsSUc8zGb1kAUf3aGSOqY3bLMFDvMGmoOY7hjJIPyotgxgfOmdWQnClnYYGRlkSnfuuCe46C3yRBAyX4sBujmj158yvWFslKRJccfHiL12WSUm2wudJDkwH0ovb-wZjRylnaJIkYhZMXWqliMQSlxh30igI--errkKbbYaznp2gIlwLc14Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
⚠️
واکنش اتلتیکو مادرید به عکس‌های پرینت شده مورینیو در کنفرانس خبری
: «همین حالا به آزار و اذیت داوران پایان دهید!»
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/Futball180TV/107020" target="_blank">📅 20:09 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-107019">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0863a4f870.mp4?token=h6zM61MPML26WvrC2lWEsDwny3X1sh6G8VJOw51MKov18SH9KonbFtXWD3R3uLHTmINXTHmE84_Pag8r_DT12LA4LPwOdnWs4Tlv6ioX-_N2DHfPx3LXKwEwwynqYGKP45kgVqP9xbeCz29e5nk2EHSCP1jFxB5YRcFIv3kCFSmNhq7EorYFPsDVCXYAEflpYqT2iIgzulnQF-XqtcwTn028aQgltMOhiSkjJ6iVGuYNK9HQHjwzQqBHoYfsrXzQkefLMJuq2kxIWETBsyHqlMLhAuGq3RBjs3-ggNGPyNp6BEea4rFxyR87nV2ZPf0gowbWsm2cRJ_HYSZmTE9Gbg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0863a4f870.mp4?token=h6zM61MPML26WvrC2lWEsDwny3X1sh6G8VJOw51MKov18SH9KonbFtXWD3R3uLHTmINXTHmE84_Pag8r_DT12LA4LPwOdnWs4Tlv6ioX-_N2DHfPx3LXKwEwwynqYGKP45kgVqP9xbeCz29e5nk2EHSCP1jFxB5YRcFIv3kCFSmNhq7EorYFPsDVCXYAEflpYqT2iIgzulnQF-XqtcwTn028aQgltMOhiSkjJ6iVGuYNK9HQHjwzQqBHoYfsrXzQkefLMJuq2kxIWETBsyHqlMLhAuGq3RBjs3-ggNGPyNp6BEea4rFxyR87nV2ZPf0gowbWsm2cRJ_HYSZmTE9Gbg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇪🇸
وضعیت رختکن تیم‌فوتبال رئال‌مادرید بعد از شکست دیشب جلو اتلتیکو!
😆
😆
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/Futball180TV/107019" target="_blank">📅 19:45 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-107018">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/beecf6e577.mp4?token=cg1GGunHckK2has-S4CQH-_Mt6EftFfzNqyoRGxJ918dctJeWgLaK9hejCCfXlJ0vv2rw_8ykMSTuXso4BDAW2klS5CM0UCjrS2n2WFN7ZAgVxrewJZ_ZQ3dC4ZSowVYTs8OawCwH7QtQJsWrlph2BN8aetWnqOhWXiYY5470d7Cb2L3T4KYr93n2ipLnL8BKokmav8eqpeN_Br_qviciCLIL3FKI4PtIVDQYA2l5PiOZLRrqI7zLVEMApzQIRxeYXA2hnZFcnNYdsOM5rNO7p9xceUpQSopYAjK4fjn3M7QIl9kgv-0wiQBfTFLnHU3wLDtxLSOe7o5GamJkEAf4A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/beecf6e577.mp4?token=cg1GGunHckK2has-S4CQH-_Mt6EftFfzNqyoRGxJ918dctJeWgLaK9hejCCfXlJ0vv2rw_8ykMSTuXso4BDAW2klS5CM0UCjrS2n2WFN7ZAgVxrewJZ_ZQ3dC4ZSowVYTs8OawCwH7QtQJsWrlph2BN8aetWnqOhWXiYY5470d7Cb2L3T4KYr93n2ipLnL8BKokmav8eqpeN_Br_qviciCLIL3FKI4PtIVDQYA2l5PiOZLRrqI7zLVEMApzQIRxeYXA2hnZFcnNYdsOM5rNO7p9xceUpQSopYAjK4fjn3M7QIl9kgv-0wiQBfTFLnHU3wLDtxLSOe7o5GamJkEAf4A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🙂
دیشب «محسن نامجو» که به تازگی برگشته ایران، شروع کرد وسط خیابون با صدای بلند آواز خوندن که یه هموطن با دو کلمه «ک…، خفه‌شو» دهنشو بست و این شاهکار رو خلق کرد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/Futball180TV/107018" target="_blank">📅 19:15 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-107017">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c34f1b0314.mp4?token=BbcLWoNv0QzB9Hcydhm1K82Ee55_Usp_sIZ8aoRXUwLqn1rXzlY0B3TQDeDjldL33nSZJOiF2RP0D1BadrXDsjifc7G3m2BOkjkebjsIbvLqhRh3tkjJwcbsxg0vnlw-EqbmNy8hgL4qhomutX35nc-vNs3GreZ5AGde6uBsBPNABBS1oVOPirc0yxwU3Ml2cSNmstfra9lCpyRXhiRfKeLUzwf0mY6jIHMvnH6X0LFmANymO82sTYuJ-yXqUKEfUKz5KIB1oxGQVBhixMOYsB33ftnPLGZ7Nsb6Oh5FP0lNqFgzJYIrWk42QOwRXrNGJWGbaEgmyD4IW9hpOdqPgA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c34f1b0314.mp4?token=BbcLWoNv0QzB9Hcydhm1K82Ee55_Usp_sIZ8aoRXUwLqn1rXzlY0B3TQDeDjldL33nSZJOiF2RP0D1BadrXDsjifc7G3m2BOkjkebjsIbvLqhRh3tkjJwcbsxg0vnlw-EqbmNy8hgL4qhomutX35nc-vNs3GreZ5AGde6uBsBPNABBS1oVOPirc0yxwU3Ml2cSNmstfra9lCpyRXhiRfKeLUzwf0mY6jIHMvnH6X0LFmANymO82sTYuJ-yXqUKEfUKz5KIB1oxGQVBhixMOYsB33ftnPLGZ7Nsb6Oh5FP0lNqFgzJYIrWk42QOwRXrNGJWGbaEgmyD4IW9hpOdqPgA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
روایت هاشم‌بیک‌زاده از استخدام مربی خصوصی رونالدو برای رساندن مدافع تیم‌ملی به جام‌جهانی ۲۰۱۴ برزیل
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/Futball180TV/107017" target="_blank">📅 18:45 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-107016">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/beeb6137f6.mp4?token=e3aYzv7EMrXFiYZyubBoD2h28nBoqB4I3g4AyRXFNdUrk1rdL4kfvmkt8NxzAZowEnwrCvRbHA1VLswG-iRuOTKI1QMNYzjnFd2T25YOz5RvIecrbiWkoFpRb8YYRDPhgnI7Ac1e3HpMZu1WXsnDKYVvq1rS-uLwZQm7lS95G7f2NlLrVCQuVVDbgnifX47xma_EhlfJ9e5vg8_KYIqvNWUsTywlTatDa4qdaTuDRsOXmBtg1jA5ibghJo6w0MpA6HGUBFT8O7iDbMOyM6oPGTQsBojpQngLAjZLawXaCvBPD0L4R03CSA567m1fSZoZ7lTjFtnXwsZRojwr_iYS_A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/beeb6137f6.mp4?token=e3aYzv7EMrXFiYZyubBoD2h28nBoqB4I3g4AyRXFNdUrk1rdL4kfvmkt8NxzAZowEnwrCvRbHA1VLswG-iRuOTKI1QMNYzjnFd2T25YOz5RvIecrbiWkoFpRb8YYRDPhgnI7Ac1e3HpMZu1WXsnDKYVvq1rS-uLwZQm7lS95G7f2NlLrVCQuVVDbgnifX47xma_EhlfJ9e5vg8_KYIqvNWUsTywlTatDa4qdaTuDRsOXmBtg1jA5ibghJo6w0MpA6HGUBFT8O7iDbMOyM6oPGTQsBojpQngLAjZLawXaCvBPD0L4R03CSA567m1fSZoZ7lTjFtnXwsZRojwr_iYS_A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🎙
امیرحسین قیاسی: مهران مدیری برای حضور در برنامه من اصلا هیچ پول نگرفت
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/Futball180TV/107016" target="_blank">📅 18:12 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-107015">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/Futball180TV/107015" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/Futball180TV/107015" target="_blank">📅 18:12 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-107014">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dfX-nf5XycAcC55x4pUhMzIpccqmPJfISVL6SLMYsthyGitFbWjkpVZPGrVjo7jevK9Sftji-_B6dGMacc68gf9yP5B4EvjbzQX1iYrwFGHmODvzULQoiP7SCXVeHU_GMpSbxuAKBLNeNbmrH4FNy7wrOXJHwuWK2QM-l_yS6oK5VxlNoVdPsfkYSBUoqE7uKj7NEc_7s9IBsDpKb5lC0ZYpx_3FWTynmZsmnVgC93PDNOPm699NHbp336CP81VBxvfnLc0bWM7oJtO8OzWV7moLUPrrRiCemax2SCv2h5TBoZMr4LqEvgvzdsq6-MD7gGpayMMroyVrwhNmJgDtTg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/Futball180TV/107014" target="_blank">📅 18:12 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-107013">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/037abe05f9.mp4?token=vno0Q0-BMniMv9a2N7P95OfnqPEZW5sQMnM0XnJh8wILoc7Ji-9t7FygJKUYW49jBctWmCf7XSxOdiBO8TfqeYV763EnGb09A5SpUSchsDSN9fZlUV6WTnMN_rSuj0nAlqJQ3zKMWcmgljbh8skKuSv8xc0jeVapkhSUdVK3d1gve39qxBto13yOeTZj0sXYuj2hd3fUeW2m155wtZYLK6zcA-DMid9Q6lnwOZee5k2AMMxWtSsybBFx5X0siGuqBrpAyQp3sDSexIEMY0hIm_oafaeZppEkl3uufGK7nyyPCXxP8YcURXN2_XK4FKzmKX-PVGuifoa_L_v3EOwJ_g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/037abe05f9.mp4?token=vno0Q0-BMniMv9a2N7P95OfnqPEZW5sQMnM0XnJh8wILoc7Ji-9t7FygJKUYW49jBctWmCf7XSxOdiBO8TfqeYV763EnGb09A5SpUSchsDSN9fZlUV6WTnMN_rSuj0nAlqJQ3zKMWcmgljbh8skKuSv8xc0jeVapkhSUdVK3d1gve39qxBto13yOeTZj0sXYuj2hd3fUeW2m155wtZYLK6zcA-DMid9Q6lnwOZee5k2AMMxWtSsybBFx5X0siGuqBrpAyQp3sDSexIEMY0hIm_oafaeZppEkl3uufGK7nyyPCXxP8YcURXN2_XK4FKzmKX-PVGuifoa_L_v3EOwJ_g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⁉️
🎙
بهترین گل‌ دوران فرشید اسماعیلی کدام است؟
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/Futball180TV/107013" target="_blank">📅 17:45 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-107012">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gT6fjOs0_WMbnn-Mj-nV6NEg8tneoogrnm8ZYDHHBVrwHS46u3kkO6ZPqMU-Cyhd8GgdrF8FnQzngVDE0SU0RZV4hiktmlQohpc-We5v2ekkcdEYSo4qNJoZv2XxZPly_72ivPiAAvaq3M6B3seNYaHw5eVk1VVToJjQiDPcBZGwswzUeRD8uoUkN4q9gzpzAjo5h4w7XLcyWs49-Jdm6xNQGJNHPArO8GFkgVXJQGgX6XwAFECS4FK5E0OigMOfv07gKXNHFnk0Rryr2jw0kM9O6MXFqD1MB3010e2fBgIVAkBmrVgZZjPtRWWYZJ_hYxFOs9O_aHlvRS1n-AfrRQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
✔️
🏴󠁧󠁢󠁥󠁮󠁧󠁿
سه سرمربی آخر منچسترسیتی همشون پنج بازی اولشون تو PL رو بردن.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/Futball180TV/107012" target="_blank">📅 17:20 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-107011">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/226cc241a7.mp4?token=pTdYlIAZsnWhnKymOOExIp7IRYzVj-iKcn2tMX3-_zAB7ucfbJTqP9K5iW4snsfpV37xu7riQzI_8lRICLMKkyORNKHLNavXvUHcDZyxqrvfdy9InpDsFHRm2AFRGfvSjv-bSggDOqhfjfCXJrjrTFoZwJSqUB8nsgIsmClLwQwwh-lvF5KTO9-6ZHHzF1M6boZ1OI_h3HnJeOO0qHfjxo_tezHybH45bde_9F96hkwxVFHjRDJYO8CDI-JhjEuM2A9uIH86P-DUcGtgG0mku70V3cDrfdOHVmhQZkP4G8nQcRhbDo4qKPbBR55HNjqOqQEm9nZR3Za4tUOwclnhmg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/226cc241a7.mp4?token=pTdYlIAZsnWhnKymOOExIp7IRYzVj-iKcn2tMX3-_zAB7ucfbJTqP9K5iW4snsfpV37xu7riQzI_8lRICLMKkyORNKHLNavXvUHcDZyxqrvfdy9InpDsFHRm2AFRGfvSjv-bSggDOqhfjfCXJrjrTFoZwJSqUB8nsgIsmClLwQwwh-lvF5KTO9-6ZHHzF1M6boZ1OI_h3HnJeOO0qHfjxo_tezHybH45bde_9F96hkwxVFHjRDJYO8CDI-JhjEuM2A9uIH86P-DUcGtgG0mku70V3cDrfdOHVmhQZkP4G8nQcRhbDo4qKPbBR55HNjqOqQEm9nZR3Za4tUOwclnhmg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👀
🔥
چند شروع جذاب و یک خداحافظی تلخ. این فیفا دی رو از دست ندین.
👀
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/Futball180TV/107011" target="_blank">📅 16:55 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-107010">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">🚨
⭕️
⭕️
⭕️
🇺🇸
وزیر خزانه‌داری آمریکا: تمام شرکت‌های هواپیمایی ایرانی از ۲۳ سپتامبر فعالیت خود را در سراسر جهان متوقف خواهند کرد و از پرواز به تمامی مقاصد بین‌المللی منع خواهند شد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/Futball180TV/107010" target="_blank">📅 16:20 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-107009">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Tt4T3gk4VQrIGhX0L8DVebhdq4FlscP6H1fH2ySEkOIvUL6XJU-qbi9_yi-4wXNRPahmxM32qZn2D6BIjyc7oEy5d_5cfwd4yJ4tlRFea645GDSXvF7DIF66t-BLXZ3zSrSCBPAV7NcKtGjFuC2se2R3rx9ztg5TCiYTRUMHEAtI33aaVnb-Xm2YJmhW_ci-jHy8PmGaikgneYqXUNRI18uXWuXnnONpM2P3B6e73ooEkHifNXPGw8UheOvU-_lSTJCJG_ajyhlv180-CNs0PhpL2pewUbtrlkwC0DOSXj0_6YUPOzx9PnV0jSYk_9_4Kw5d22HFoV4q_Kp5bUrEVg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
📊
آمار درخشان اللهیار صیادمنش در لخ‌پوزنان لهستان که نتیجه آن عدم دعوت به تیم‌ملی بود:
🔴
۱۵ بازی؛ ۷ گل؛ ۲ پاس گل
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/Futball180TV/107009" target="_blank">📅 16:19 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-107008">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/12d7084572.mp4?token=L-Zl2sihtFtnKeCfhrp_0Ivk_wh2rdWRCvxrM2_Wr2Gp3KFZE8lgE3DzktkWrle_3VJc3XCtp4mqjUYxeae-r2yhHNteKCMwHJZX-Z23Z_J21Pk1SYGrR_JiCW-e-38nfrudGbT5TNiooiK5mrFKCzAQXksA2rtWYBl6AqWi7jCB5upPr9dHwgMosmXEtaWcGfw6_ZNV1f36UCuTJo6LURrjhRWOwULKUYW004Z02wKYqXcOfwomARYM1tOFTpdxEkMIXmahhGTBtC9IB2FZZ4seglf4ZeyX48LNwkF06gc4l3ZQJkYnQXgQ_rF-cqbQtjFCAZmW93HKwBDq21JuDw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/12d7084572.mp4?token=L-Zl2sihtFtnKeCfhrp_0Ivk_wh2rdWRCvxrM2_Wr2Gp3KFZE8lgE3DzktkWrle_3VJc3XCtp4mqjUYxeae-r2yhHNteKCMwHJZX-Z23Z_J21Pk1SYGrR_JiCW-e-38nfrudGbT5TNiooiK5mrFKCzAQXksA2rtWYBl6AqWi7jCB5upPr9dHwgMosmXEtaWcGfw6_ZNV1f36UCuTJo6LURrjhRWOwULKUYW004Z02wKYqXcOfwomARYM1tOFTpdxEkMIXmahhGTBtC9IB2FZZ4seglf4ZeyX48LNwkF06gc4l3ZQJkYnQXgQ_rF-cqbQtjFCAZmW93HKwBDq21JuDw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
⚠️
افشاگری یاشار سلطانی خبرنگار: روح‌الله رضوی کشمیری، مجری جنجالی شبکه خبر ۱۷ میلیارد نفت از ایران فروخته!!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/Futball180TV/107008" target="_blank">📅 16:05 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-107007">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EgKfiAVJyMYmFhOkvi4EcnwErf7Mi8P8IddMw_KuhLh4ilGxUKJqVZ-HENo_gxhS6TQUYd_6NzutFBznbn3fphazK3xOrTbQ-SDa0yWMCreEyJQrsFL8dndggMFekedSTNPAoDtyznuGLwU70_xZMK-sm88T3baJJDWauKOOpThbpt-gZo5ydC0jYSABgtEbuVTIjejz7wK6N4o2dy5CtaLXfUMMRNGzBp1StlQf3qi9l6fNj-A1F30Et2_K45_Njrcdgqbbm02M3caSBtIL7ZqYFa7le7AQ_6pmwdyihCQVjwFAmU6DlQP6KDwn15d1MiPHxLGlgIaxvStCQKM-Bw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
⚠️
🙂
دیدار دو اسطوره محبوب و مردمی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/Futball180TV/107007" target="_blank">📅 16:03 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-107006">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6e35b261cd.mp4?token=gV-mPBQPNVkhydIlwKT8gUO2s6-UexmI0OzKoMTUauUw9LTdSHq9gItz06XAozwrCf8VfKS88McDHRavIcNmixidyFTQJXTYlLYX9my5brpn-F0xeRWYBxashjwYA-D_HmA0VxqhF7esYafByBHhywrUjQW3Nzt7D3rpCqqJLbPkU26OxoQusGEdkvH8JXZZ_AMzx4Ptb5VXMTf5UiNWk09eCh0VNbhoRLlJK1AhwiIGsLwXAgyayRUw33mrUEzWRM7YjCHUPsL6mXxrh5IWLrthfPNI7hE5oHtYCv8enFb_8Ia3OZFHoaHAJ8BY4rB5Pe5ZU-brZYeLwsIf1CLMjDzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6e35b261cd.mp4?token=gV-mPBQPNVkhydIlwKT8gUO2s6-UexmI0OzKoMTUauUw9LTdSHq9gItz06XAozwrCf8VfKS88McDHRavIcNmixidyFTQJXTYlLYX9my5brpn-F0xeRWYBxashjwYA-D_HmA0VxqhF7esYafByBHhywrUjQW3Nzt7D3rpCqqJLbPkU26OxoQusGEdkvH8JXZZ_AMzx4Ptb5VXMTf5UiNWk09eCh0VNbhoRLlJK1AhwiIGsLwXAgyayRUw33mrUEzWRM7YjCHUPsL6mXxrh5IWLrthfPNI7hE5oHtYCv8enFb_8Ia3OZFHoaHAJ8BY4rB5Pe5ZU-brZYeLwsIf1CLMjDzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وضعیت مانوئل نویر در بازی بایرن جلو یونیون که انگار خودش رو دروازه‌بان نمیدونه
😂
😳
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/Futball180TV/107006" target="_blank">📅 15:40 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-107005">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4379faf506.mp4?token=KG2AyFZBP7cp77eE1xdqtanTf_-zSDKj4VgwJUavN_zsg_SHQwru4oRpmsRw-ic3bmAXN624mfG8q0uZSq8FyhhsORvs7lo31AVA3qlwlVtZEPBtMehvLDMiu4l9J5CRvI0N6hGCGD5aWMFV7hVWJsP7KLe6OAAnyFBdXWTMuXtUHfC9e57sbKkbWxtAeKK55IbcUSLUWiqps4S-2vqg0dxToGjDdam-mLDyfMK3FAROuj_03tEZPBfk8NPk98c_ManLUiTilUMncvQ00dm8qmdiTJ-AQTkeLF63oUbNhOdx_CIVlpOvoytdXKu1D1B3pYk4UDagf0XApnZ0jOwm_Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4379faf506.mp4?token=KG2AyFZBP7cp77eE1xdqtanTf_-zSDKj4VgwJUavN_zsg_SHQwru4oRpmsRw-ic3bmAXN624mfG8q0uZSq8FyhhsORvs7lo31AVA3qlwlVtZEPBtMehvLDMiu4l9J5CRvI0N6hGCGD5aWMFV7hVWJsP7KLe6OAAnyFBdXWTMuXtUHfC9e57sbKkbWxtAeKK55IbcUSLUWiqps4S-2vqg0dxToGjDdam-mLDyfMK3FAROuj_03tEZPBfk8NPk98c_ManLUiTilUMncvQ00dm8qmdiTJ-AQTkeLF63oUbNhOdx_CIVlpOvoytdXKu1D1B3pYk4UDagf0XApnZ0jOwm_Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
⚠️
تمسخر امید عالیشاه توسط مجری صداوسیما پس از فحاشی زشت خداداد عزیزی!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/Futball180TV/107005" target="_blank">📅 15:15 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-107004">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lzkkaD1wLG-lmpL-vGlh1u0hxCcIgWNDvnz7qj7ejeJjvPtPjCqNEd6IYEhqCo_rj0auvBvlmQcTNWPp1e2CnZwm8_YWtx9tj1rGJ0eAeg7IPpKFYfkQyDeVm4NNaSjQLM6b01AlIYXF6zVxCOLdRsnD7zXp_wN0bly7cO7TdfjBGA5J8xtoWNCPzseGSdR_Fv3lpPq3yi-2j7Ef7qXVInMbrTKykfEcMVxNZpAlfJzD8hk3oBxHOHl-eRQQo7rEcJoTA7uGgNLqQjmQq61-c9rveh2YW0StjY64HojaM52IyfEWQjIA6qiU0jfgv8fscoRea8kLBTVM3CplsXW1eA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
📱
پست جدید سردار آزمون بعد از دعوت مجدد به تیم‌ملی: دلم برای شنیدن دوباره سرود کشورم و پوشیدن پیراهن تیم‌ملی تنگ شده بود.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/Futball180TV/107004" target="_blank">📅 14:46 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-107003">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pBiS0YsKJpsBF6auYdTjlIjgcbA3dkYFhUT5YJrhb1PUXzGxtKHJ8uvHh4WSMW0jZb-NcwPbsccuZf7QqhMCzskrDf9XGbZKRZX-sPh36CVCfoOh3VUIksZDDFMla1Br5PgfaAT8-N1Yv4chM0yTDg7zaCKKiGVwgaxkwgWOCiRNtLiaPCAHgpRDzEqouSNgSAx4XsyuWbz4qFu643oWu3RuyughhcRuP6xugbd-GnO2ss3y0X-jDfxVSThXxZSY-twPgV1Upv--b27I103m-lx6CKAaIPppivJgVrQyfq7lHbniEuklHhB_yuObKIBLM--8DAjIrdArnSLxXCb86w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
قرارداد تیم‌ملی اسپانیا با دلافوئنته تا سال ۲۰۳۲ میلادی تمدید شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/Futball180TV/107003" target="_blank">📅 14:36 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-107002">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1b0213635d.mp4?token=HuO8B1Zvbm8SWV39ULldOr8I_vDN6Ck3hrQIByFbmCgGmfNLsEW8nYSFt5sc8sqBkOTaPWKmbDLWKYEaVbO3TToQM9vx_r537Z_CS5B8IsTKF6fFjRPJS8pXYWsPJzz9X3K7UrzbSaEQH16g6DH6TnTAtSf3lYMpKYgUbkrhI4HfmIxmkuI-Nzs_dd7JTkhhEUX1lXjhkEXRV7qq0y2v3yQS3Oi1FgMogD4uRUhXL5C0aTaF1zClozKf734-n_WUScAD2SUpeC1nMtR9W0IwhayMo5uBGF6AsaSIOki5EsbgWir710WLsfQmTiIIr53lohNPNXbEW8ULtVlbghjP7w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1b0213635d.mp4?token=HuO8B1Zvbm8SWV39ULldOr8I_vDN6Ck3hrQIByFbmCgGmfNLsEW8nYSFt5sc8sqBkOTaPWKmbDLWKYEaVbO3TToQM9vx_r537Z_CS5B8IsTKF6fFjRPJS8pXYWsPJzz9X3K7UrzbSaEQH16g6DH6TnTAtSf3lYMpKYgUbkrhI4HfmIxmkuI-Nzs_dd7JTkhhEUX1lXjhkEXRV7qq0y2v3yQS3Oi1FgMogD4uRUhXL5C0aTaF1zClozKf734-n_WUScAD2SUpeC1nMtR9W0IwhayMo5uBGF6AsaSIOki5EsbgWir710WLsfQmTiIIr53lohNPNXbEW8ULtVlbghjP7w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
💥
🇪🇸
بازیکنان رئال‌مادرید و زیدی‌هاشون
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/Futball180TV/107002" target="_blank">📅 14:25 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-107001">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/T2WrsCtePhGIwXs7tEt6wEPr5QdDjDpUnXJLkBreuVGYlPnnstheq3SPnFMxHA9kDM2FdvG5A9Lxu9GzYJQvhsYuYd9U0Z6mkJgnZcWpQvyFxFomLEfDFdSi_Wjui7IgYzDMF2HdRPmgBWzqEKkQSIOnFXYbSvlYVV1q2FPOnK5GuwFFfnyJtmiD0ahdQyXclm-Ti0Naz9W3RjTpstObotCZGeg06vjd1WBa3HaIlyTNiiyJDH6tfc5T6e3rr4wYlBm6ct2AAujUj8cnI006gAgYhytFKKL3l7-ctmE1UJzkbTjO3UCpP1qm_keh-nv7XYSeZH8xfosVeyjyfGB3Rg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
بیشترین تعداد گل رافینیا، مسی و کریستیانو پس از گذشت ۷ هفته نخست لیگ.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/Futball180TV/107001" target="_blank">📅 14:04 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-107000">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/G1KeS4Lf9EvAwTj0TzxuGn27eJJcHEza8XLf278UCPspmp5poaL9GGnp8lyTUeQCAQFz8IMdT_-gGNlgP0-ulQ5CNQh7f2VDZspip6V1bJSTxf5yIZk6TvPw1zxmeUYtt36YZarGov5X3yQkmKYiNE6uWXxK3UhM9kKwdUM-6QCyywFAOzx_Ru60r4GhPjKklUczh9tVeV98k7mRcCNtU5gpfZxYwk7DwwYQ8zgV2mYka9n94Yj6fwESmLIyLTuqyOHMRHA-ly7V-wWyHdZwE-s_-_KGNdqwqWAjAfdk7hRP0QJP9vKR169GsOna2IFJmfE2rM-uf_1yRGUdyKUlbQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
📱
پست جدید سردار آزمون بعد از دعوت مجدد به تیم‌ملی: دلم برای شنیدن دوباره سرود کشورم و پوشیدن پیراهن تیم‌ملی تنگ شده بود.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/Futball180TV/107000" target="_blank">📅 13:42 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106999">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bf7b6d21da.mp4?token=bu9s6YefjbM7Bg2qwWWKvbdT72C9xFep1Vn3djuWPjDjvK-jDgUUMnNKIEh2Fk56art0KydpVCbWECqJw2eCuhOQUnFdib6TOGLcYskjfXxMKtshofVa20Nw094vt_Sf7Ia9jipzvbktyPzMpY3wavWMyCiOAtBDp15u2td_Kn-jKyLWmLfeO9E9kGospgsWdgGAScDm3Z21gfyUj08fBFH05vS9upPQGZ8aTfats-KVHkpXfdZytqIy3WEuI8qI3au4m58lnIM5uq-KdNA-QygEwD4THPxOTatmQymqwEoVWiNB23l_63oWDgSzi4zZU-CcU7yRyupfFjsA9VyDZIWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bf7b6d21da.mp4?token=bu9s6YefjbM7Bg2qwWWKvbdT72C9xFep1Vn3djuWPjDjvK-jDgUUMnNKIEh2Fk56art0KydpVCbWECqJw2eCuhOQUnFdib6TOGLcYskjfXxMKtshofVa20Nw094vt_Sf7Ia9jipzvbktyPzMpY3wavWMyCiOAtBDp15u2td_Kn-jKyLWmLfeO9E9kGospgsWdgGAScDm3Z21gfyUj08fBFH05vS9upPQGZ8aTfats-KVHkpXfdZytqIy3WEuI8qI3au4m58lnIM5uq-KdNA-QygEwD4THPxOTatmQymqwEoVWiNB23l_63oWDgSzi4zZU-CcU7yRyupfFjsA9VyDZIWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🎙
اولین گزارش سعید زلفی در پلتفرم اینترنتی پس از جدایی از صداوسیما
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/Futball180TV/106999" target="_blank">📅 13:35 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106998">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VoBXuxoF0nCNnffUS-3IdhMnlAeVeGf3CRNV8ekHouwf0qAK1wvnDNunSlhybs3BflPquvLIgvK8SQG7oGwYH_d7l0C7AWbJu_jjJ12d4RvVKIs76A3qx3rWNPKZ6q8Dcfhy9h7z0jjgDMhjCitg-m9VcVS_FT0XTChh1gUXCpaiTHPvZ5NxtkylTYE3x2clIG3MP6HGroSDDikTdJMDJ-IGFZty6ivzw-BATIS6ZGztr4hxa4lzwrIcwB8fCj0EkJGEVipFg_3PPIoeK-icB9M9A3ZKRNI21Qld0ygrUfONa6YkmGqM2trUtn1_4WY5x4GgsPhC9rELtqUpPjeJEA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📱
🔴
اینو حتماً تو اینستاگرامتون فعال کنید!
برید:
Settings → Data usage and media quality → Data Saver
با فعال کردنش، اینستاگرام مصرف اینترنت کمتری برای لود عکس و ویدیو داره یه تنظیم کوچیکه، ولی اگه زیاد اینستا می‌رید، تو مصرف حجمتون حسابی اثر می‌ذاره!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/Futball180TV/106998" target="_blank">📅 13:28 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106997">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OcQqCR8NXczC51iwVfBWGjHRd3BfrJU_SQZo44GBQ3kjvcAjMY50PwT-mvhwB_tLERIbGN3sYpTZvNlrjTD5Xs3Pg8-jvGJp484rcfkVYfWQheKvuVH3imzjKoySpwelY4HIs9ZJ-xt6WaqXcOn9eQnTAm0wWbKR9_JWm3-s3QfyQr4kMF2jA-2A9lgjfTlx_9q90GXZjoWN5Jip7-IdcnUSIRhHetYkG_xtncUl6QOXEnBg6JuE4QCUU3o5z2WQpt1iJ26wS3sTI9Lh0jYI0L4CCIRCUqyivfljGbUdxJPUtyQ-m-NhcGiZ0N4HIg8-GVUuOuqdwd69az47X6oi_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
‼️
🙂
استاد گودرزی
: متاسفانه پارسال نزاشتن پیاده تا آرامگاه کوروش بزرگ برم؛ اما امسال دیگه میرم
هموطن راه در جهان یکیست و آن راه راستیست
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/Futball180TV/106997" target="_blank">📅 13:04 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106996">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/35dfd98213.mp4?token=mBBahUc7x3UKZMIb-h9vzX_ZWQM3n5zNoZu_yVZrT7pqkDwwFSNLmfyECbV8LeIG1V-4c_ik2hoHcxLGFbcR__5eHUcJBaEjbucFMs4We5IPofldtZBwWWUwzm9C8ZRqCO_m3cndjDVPe3_SzqLWtY7y0hhHaGoZfuYK5pl_y4swxItlSv_MAII85caE_gRodkeDHAO7PPNHMg51mMjfszzJo0ef754rStYn5Oxm9_ccUzt8fVUaTe2LHDijYcN9iaQ82x_SiJfAF_i5QRdvOHUsVaPPDO5yWdREA8j8UF-F4SGQvjkjXDbpxMvgUpTkzFC3IudXPYv9U8Am_-3rd4WOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/35dfd98213.mp4?token=mBBahUc7x3UKZMIb-h9vzX_ZWQM3n5zNoZu_yVZrT7pqkDwwFSNLmfyECbV8LeIG1V-4c_ik2hoHcxLGFbcR__5eHUcJBaEjbucFMs4We5IPofldtZBwWWUwzm9C8ZRqCO_m3cndjDVPe3_SzqLWtY7y0hhHaGoZfuYK5pl_y4swxItlSv_MAII85caE_gRodkeDHAO7PPNHMg51mMjfszzJo0ef754rStYn5Oxm9_ccUzt8fVUaTe2LHDijYcN9iaQ82x_SiJfAF_i5QRdvOHUsVaPPDO5yWdREA8j8UF-F4SGQvjkjXDbpxMvgUpTkzFC3IudXPYv9U8Am_-3rd4WOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
🏆
لامین‌یامال از مدعیان اصلی توپ‌طلا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/Futball180TV/106996" target="_blank">📅 12:45 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106995">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/r6c_a9nBOtx-31St34YaQSdFkE280TG8QDWvp6ypJH1vGSOVH5p7QuWFicwUr7NQrV6HNy5tu0ujDtPQY3BOaBcrk79OWKpIMFFi-Qb8tnUZwbyZrQwhemKtudownc8LwVJ68LzsC3I1u4perrM1FlHKRRUkJs-ymjyxJIibOKx00SbQ1foQGVOzASGpwxHcXTlquqhyAk7CH0eVI0GBA7JXYQA7Il9mvLi3Pe7LPOljUPVcHqXf-Ry7a5mm9t4_7r-tLP3mIFDiw-KBPY9372RdfLGPX8i4E2B8bSUSK8FM75X4ktFMrT7Hvknc4LoJMbRDqB6O_csLW2DMftQKDQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
‼️
🇮🇷
باشگاه تراکتور با تهیه مستنداتی درحال رایزنی با نظام‌وظیفه برای کسری یا معافیت علیرضا بیرانوند است. تبریزی‌ها مدعی شدند که بیرانوند دچار مشکلات روانی است و به همین دلیل خالکوبی کرده و باید از ادامه خدمت معاف شود
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/Futball180TV/106995" target="_blank">📅 12:37 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106994">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OHaH5iXAGjRPqjUbtPT5HQSMa9aQsC66aRZ2fD53dmTpc1gXTrwAD5IsYIIGH7HR9PVYDKqrTfnKKxKmbESETh8H4mbn3ls43ly9hBIpfwaKeRFIo2tq43HGh_gU8VGRg8bC_pdpwV7s6fnJuORCEYo8PHkgjnua3lN0t5jEVi7jcbrkR6GroUwJzQo-lVCju8SxJvv0dELNANQBlhJP9E0TdbCjzg0QSuZPFkT_TIFjBA_6zclfr_d4WYOxraOVF-E4XlWW8SqHkWFg9uea5b1l6RxCek48wdhsTq95H4Lu3ZOQzHWa1R91F_yia-4Ccgak9CrknFFeLKB7x-CoZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🫡
🔥
بهترین بازیکن فعلی فوتبال اروپا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/Futball180TV/106994" target="_blank">📅 12:20 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106993">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8c1dd2f2cd.mp4?token=mfCgjdUKBCRU8Dhncf0JuocmyXoZgrp0khkwMzf5K0w9bAKC8HhUCqvYtohTYiAwtf6_joWJlEINLPCJL4vVuCkBJM_sHkXdkMMU2whjwzMHMQLMBUuV30a-ETjo1ljD9LNWUNpKkWLM10msQEx4Zh0U7bwARfD-O_YWeDD3rKfD8eFQ92w1mTFlxcAHigSr4mPn30luDvYwjxN4AjkYfsV7SoFBR9KiyDHc79SZNWMvRB44ekIu_NlZziGdhjBCk-RZECJNwtLIJygAbBtiXk5srpHtt6h63PhV9ysg7BrPVit4lzPi2qmn17EC7uJn0ryFrd0MMuNFPpYZN4arMg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8c1dd2f2cd.mp4?token=mfCgjdUKBCRU8Dhncf0JuocmyXoZgrp0khkwMzf5K0w9bAKC8HhUCqvYtohTYiAwtf6_joWJlEINLPCJL4vVuCkBJM_sHkXdkMMU2whjwzMHMQLMBUuV30a-ETjo1ljD9LNWUNpKkWLM10msQEx4Zh0U7bwARfD-O_YWeDD3rKfD8eFQ92w1mTFlxcAHigSr4mPn30luDvYwjxN4AjkYfsV7SoFBR9KiyDHc79SZNWMvRB44ekIu_NlZziGdhjBCk-RZECJNwtLIJygAbBtiXk5srpHtt6h63PhV9ysg7BrPVit4lzPi2qmn17EC7uJn0ryFrd0MMuNFPpYZN4arMg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">هالند ویدیو معروفش که با هوش مصنوعی درست شده بود را بازسازی کرد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/Futball180TV/106993" target="_blank">📅 11:55 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106992">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JtZEiQlHOBOs1mYFF375SrVNWaq9aPZ3GeOoUe7LixYe-cEHCUQnwTPvG6qms3uSK0oIOm3qw0ExMiVMNIeK9pcq7rhlHsnhSB8bjuA6LWtlJWBAnWpwRQCYhYPMN3u6_aQx8gD5ticDmJIjqhSJPc3ZS7xWDOYIoRTQ8O33UjqbcZws36qJU0uW8ykXteLA8QI-C7lSzXN6GUu0B4oynJPvKF6Z6ZO3KKLVHHn5rIkE4giZ0GwLor9eT8fY2-i2DOuCL2HHAC5_vfKs3QIfhm3Ql7tIkH8InzFwj3X2IaDQVMLNg4AXsKa9Y44dhTk6jRwSZ8iS8Rh-HU5mv39KGQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
✔️
‼️
اعلام رأی کمیته استیناف:‌ اعتراض تراکتور رد و محرومیت 4 ماهه خداداد عزیزی تأیید شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/Futball180TV/106992" target="_blank">📅 11:33 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106991">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b0476c7864.mp4?token=a3qMoKbj8jw4eAadP_wh-eon9UWWgwD2-aXl4kEXDIKfggukpVraeZyjvwAcQXMnZbjIVm3R8MAOBQXotYzDuGafJpXfr4zNkp0b1Iq3Rw3B3CDuB29VP71HslCR1ZYg1JXxeTh1tL5vm-LTolPOzHnQUxle-48VwPN7ePS2KcO68M0bFL13btw_NBdgmXIBGfGO5AfBexeszmdXZBxHzJkjzFs_IcyGMZxlW5IUweUaCu6xZsJHpEI4rR5rH31itTzCm5HQBXwmhU6DLl9XM6p_67vq6jK1GLLCz3qBmf9LOu247dKHgtSolviYN_M2FdnHBjrReaxRmfQHB7ohfg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b0476c7864.mp4?token=a3qMoKbj8jw4eAadP_wh-eon9UWWgwD2-aXl4kEXDIKfggukpVraeZyjvwAcQXMnZbjIVm3R8MAOBQXotYzDuGafJpXfr4zNkp0b1Iq3Rw3B3CDuB29VP71HslCR1ZYg1JXxeTh1tL5vm-LTolPOzHnQUxle-48VwPN7ePS2KcO68M0bFL13btw_NBdgmXIBGfGO5AfBexeszmdXZBxHzJkjzFs_IcyGMZxlW5IUweUaCu6xZsJHpEI4rR5rH31itTzCm5HQBXwmhU6DLl9XM6p_67vq6jK1GLLCz3qBmf9LOu247dKHgtSolviYN_M2FdnHBjrReaxRmfQHB7ohfg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🗓
‼️
🇪🇸
ویدیو سال ۲۰۲۳ بارسلونا وقتی که یامال ۱۵ سالش بود و شماره ۱۰ بارسلونا به آنسو فاتی رسید و براش جشن گرفتن!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/Futball180TV/106991" target="_blank">📅 11:30 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106990">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/Futball180TV/106990" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/Futball180TV/106990" target="_blank">📅 11:30 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106989">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mhAGjMjGc36h3wKUPYJq8ptUCQ6EgLIIv0qCYynuOspu7K_U9Ntw-Fnl7pmSbQpTURRatdkyCxrmFCeSJk9TsOGY6n0QXMAZEnPVu1ntNs5V8JHM0UgCs-U6mSNlzBjuzf85h8xxubGraOmSERLuuuGZ9Lauvk9CPOFCCeO8F9i-KSgYdeplRkpArpHt6IMYAutw5TD1sgpOfI2ZDbhcWQFqG0KTU7CMz6CnTmXE_lKXJ0AbDLRHqr2iKwhsMYrdB2NbXyGeEkqhoKcrt6I334CdAbVe5vkHtMdKC3NdeXNGNgCqgFJdB8ImiNDyBnGyfysOkjA1nfiVhEYApMzUtg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🦖
مسابقات
UFC Fight Night
شروع شد!
🦖
یک شب پر از مبارزات هیجان‌انگیز، رقابت‌های نزدیک و لحظه‌هایی که نتیجه می‌تونه در چند ثانیه تغییر کنه.
مبارزات رو زنده دنبال کن، عملکرد فایترها رو بررسی کن و پیش‌بینی خودت رو در
TrexBet
ثبت کن.
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
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/Futball180TV/106989" target="_blank">📅 11:30 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106988">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/60ee4811fc.mp4?token=XE8T13vtHYx-7XbjZ8sDXbwAU8H1rBFOE1YL30z_TSIGtOKMj56K2TJt_Q1RzViNoncdTfL445fFevIBRK0xtOPNverIZ8T161P8YHOw5aPmOwTl-2CYz2UnzNf1XaZigL3iP44ZDrDog0f77BH6kj5RfVG0HgCmrSp49zyJ5rcxzH2H5jzTVFMoZ-FWG2fBslr7HGSg0cIDkQFYpFIETQgJTlIOSuuZl8X7KCEcL_8nG5p0PDb7dOeZWK5u0ZSAPuSYBGxdDy3tZN_RosyNw20-i2lkOckTCghOo1Bz8QqPENaRRMbj1JBDcaFOs8oVxiKWOwvZRdKihYudVhcqoA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/60ee4811fc.mp4?token=XE8T13vtHYx-7XbjZ8sDXbwAU8H1rBFOE1YL30z_TSIGtOKMj56K2TJt_Q1RzViNoncdTfL445fFevIBRK0xtOPNverIZ8T161P8YHOw5aPmOwTl-2CYz2UnzNf1XaZigL3iP44ZDrDog0f77BH6kj5RfVG0HgCmrSp49zyJ5rcxzH2H5jzTVFMoZ-FWG2fBslr7HGSg0cIDkQFYpFIETQgJTlIOSuuZl8X7KCEcL_8nG5p0PDb7dOeZWK5u0ZSAPuSYBGxdDy3tZN_RosyNw20-i2lkOckTCghOo1Bz8QqPENaRRMbj1JBDcaFOs8oVxiKWOwvZRdKihYudVhcqoA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">با صدای کم‌گوش بدید
😆
😆
😆
😆
😆
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/Futball180TV/106988" target="_blank">📅 11:05 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106987">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9186ccb478.mp4?token=MjfAvziof1ErLcUGZRlGhm2vfWEIJ6bbhJM7zOIB_Y3qaDu5YOVJeqZ_wlIG-Hyaa7RiLdKbySnTNCHOvWyZ_AQPkq3XGD8abpC3Oi6rIGto2wz3SyyyeYnzQU9ByL8OPA5PYs3v3eIc3KpkKmFxWZOOGf1DPr4tXITX8NSlxccXc5tgrj4OtBSK7zPXzkzz7VFd5rvvf8efftMdGG_jatQUOy_F-b5OLzuvEWynXsOgoQ7AayjGlHY-PykwGdImrnGLvzJfSmQoTopTxiDi1bnKdeE6QEGxnoJrwZxsapLE-ayjvhWdv4ooTeqtl4CWRSs8qt0q_9sFRmPyDSAnGg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9186ccb478.mp4?token=MjfAvziof1ErLcUGZRlGhm2vfWEIJ6bbhJM7zOIB_Y3qaDu5YOVJeqZ_wlIG-Hyaa7RiLdKbySnTNCHOvWyZ_AQPkq3XGD8abpC3Oi6rIGto2wz3SyyyeYnzQU9ByL8OPA5PYs3v3eIc3KpkKmFxWZOOGf1DPr4tXITX8NSlxccXc5tgrj4OtBSK7zPXzkzz7VFd5rvvf8efftMdGG_jatQUOy_F-b5OLzuvEWynXsOgoQ7AayjGlHY-PykwGdImrnGLvzJfSmQoTopTxiDi1bnKdeE6QEGxnoJrwZxsapLE-ayjvhWdv4ooTeqtl4CWRSs8qt0q_9sFRmPyDSAnGg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📊
🔥
تعداد‌گل‌های این فصل رافینیا در مقایسه با چند تیم مطرح اروپا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/Futball180TV/106987" target="_blank">📅 10:40 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106986">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GpgDx0Mfl4uhFDmzGZUBIX0VKS2fatf2Sn-mpDFXBwyHlkW_-1n2SUU77C__1nPR5C_mbZTOqOZ998ed_E-bj8X97hnuOJpKtL2iAt1NhPCG6i_fTGObvnw0F0Cy_R5Gni8MW7LOC1-9RydqOSzwoxQyPLaSMxvNFA04SSdQMffzHifYvmTccRpPw33k6o18U0PpLnlAt1oe_jFlNDQg1GiHeXOnLZhUfKr2uzB1pPzR5SXeKP_NMqgz1eYf07LRFMP922eJ3jvqlLOynXl3RBjlb3SV3qUavjcFxhOLPCzSM8W4H2XYdqyO0Pb43yU7bnFYnCVKBsXljs0auzOL6w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
‼️
⚠️
احمد ایراندوست از بازگشت شادمهر عقیلی به ایران در آبان امسال خبر داد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/Futball180TV/106986" target="_blank">📅 10:25 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106985">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4a7263425c.mp4?token=CZSUO6Nm9ys3pp1ZxPU9KQPP053MOfrmLfHDrHyvbhIncgDIchrFt2njJmM-rD9iHtFIEn2rQ-P_00JR2wWtniDpH6fb2PUYbmFOf0xlTUsG7Zgi9JIEY_7krbgqlg4Gj_82EQVEpsI9N6A9cgWZUoPvnuiPBx9g9D9USIdOfVMkvrMjxcPf7HVdTNsmJQSa9c_9ZingyEiy1e3FX-Suq36UrXVziRJytJhAGK2E-eHKVyFK5OOxDG5HYwo508q0NQRnLK151f1TxpmUFCKT_sakxHxRdCDsqOlsYE7GQOD9kNosn8cvMp-0uzDoyRfesxnqQoGZ79ttnmnKPgWjLA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4a7263425c.mp4?token=CZSUO6Nm9ys3pp1ZxPU9KQPP053MOfrmLfHDrHyvbhIncgDIchrFt2njJmM-rD9iHtFIEn2rQ-P_00JR2wWtniDpH6fb2PUYbmFOf0xlTUsG7Zgi9JIEY_7krbgqlg4Gj_82EQVEpsI9N6A9cgWZUoPvnuiPBx9g9D9USIdOfVMkvrMjxcPf7HVdTNsmJQSa9c_9ZingyEiy1e3FX-Suq36UrXVziRJytJhAGK2E-eHKVyFK5OOxDG5HYwo508q0NQRnLK151f1TxpmUFCKT_sakxHxRdCDsqOlsYE7GQOD9kNosn8cvMp-0uzDoyRfesxnqQoGZ79ttnmnKPgWjLA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✔️
🟣
گل‌تماشایی لیونل‌مسی از روی ضربه کاشته در بازی بامداد امروز اینترمیامی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/Futball180TV/106985" target="_blank">📅 10:12 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106984">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1a81f86f53.mp4?token=XDQBOQm-Op8doIkbtbGWqwknQbGVj605GTwVbEq-YVAfjq-6yABHWA3bGa5av2pp3CD6VlJoDhMo2gJHr8PQK74K23bejzsauD8dsb9oLqo_5cdsp9r1K1bqAF_qOcriGme-1bnzwdOyl1EUN86OAOONhH8ll3P0CGphVPtlQ-XhoNQ4obiDFVRW_Rmsl5_at23OT9rZdgQjWWdOtk1BQLGAT-kE1gAHPEbkYYUtJJFAvswN6OE0CRpUxS_h71K4vv0E7upnvaDwDQembAikkt51RP2YN_2AjVqsdovccuPyauwv9xQH3DKpHZZN3DRhjgPG5tvcvCr_rZl21carrQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1a81f86f53.mp4?token=XDQBOQm-Op8doIkbtbGWqwknQbGVj605GTwVbEq-YVAfjq-6yABHWA3bGa5av2pp3CD6VlJoDhMo2gJHr8PQK74K23bejzsauD8dsb9oLqo_5cdsp9r1K1bqAF_qOcriGme-1bnzwdOyl1EUN86OAOONhH8ll3P0CGphVPtlQ-XhoNQ4obiDFVRW_Rmsl5_at23OT9rZdgQjWWdOtk1BQLGAT-kE1gAHPEbkYYUtJJFAvswN6OE0CRpUxS_h71K4vv0E7upnvaDwDQembAikkt51RP2YN_2AjVqsdovccuPyauwv9xQH3DKpHZZN3DRhjgPG5tvcvCr_rZl21carrQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇪🇸
🇪🇸
لوئیس گارسیا پلازا، سرمربی سویا، پس از شکست ۳–۱ مقابل بارسلونا:⁣
اونا خیلی، خیلی، خیلی، خیلی خوبن. همین که تونستیم باهاشون رقابت کنیم، کار بزرگی کردیم؛ چون بقیه تیما رو جارو کرده بودن.⁣
توی فوتبال یه‌سری اتفاقات هست که نمی‌تونم درکشون کنم؛ اینکه رافینیا جزو نامزدهای توپ طلا نیست هم یکی از همون اتفاقاته.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/Futball180TV/106984" target="_blank">📅 09:50 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106983">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5061d27e31.mp4?token=WWh-UG2uNamPpXhOs9hZpB34FN7DQsViF9InXZJnZ-ViYF5YkGVuZjwPdGv-LsWgaz1zxU8zUMgNhq0QTbj8xH96TxGJ2hsFCoA4YtQFd5guUWsdZPTU2RzduGl8IF9wesd2tENEG0XRXDfYDhFZ55apPhnnXE-wDSewj0b-bM9i3fh5jEb4goJNIzR5285gLLzSHCfVrD5gQiiooJwCQLAo5YuCzfGeo05PkoqFH81OZ3Iq7qEQMLuKw8Y_HVCsmldAUhIKSiYoaErQAGfPQiF3PQafvX2jqCPA47uCze04HGwQ4TqibAbsWQSGwVLRZaf8zNZWP0IYWOMOZ-Ma-bw0zTzwNiZpuov-Qdf8cfHAJPCHvIBbHcLK54OPIrGA2ltkJXOoKbMSzTXxcMAXGki5Kk9KPtIRKK1esZoIUmLUxCgKnas1z2N10pbuxLiH2pmimSMq5DvPd3m9plVATJ8mB73WZNslENw9GZ7ZZr7LLQlU9SVoNKoH_sOrLNyD5E6E463274wkf9ngN14M1M8gZGZb6uzME87j6rBIq3UlfKts3An-1ap7lujs5xJdFvD7ZjhGzsheFWzgI8j44Uklo4avcd5_bLbxbDx_kFAAx5yg2tF0L-OueaQL69jWd7FvsNECZwVYjczz9wnGS8ilbVUMeGm06qqQi2mdHmo" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5061d27e31.mp4?token=WWh-UG2uNamPpXhOs9hZpB34FN7DQsViF9InXZJnZ-ViYF5YkGVuZjwPdGv-LsWgaz1zxU8zUMgNhq0QTbj8xH96TxGJ2hsFCoA4YtQFd5guUWsdZPTU2RzduGl8IF9wesd2tENEG0XRXDfYDhFZ55apPhnnXE-wDSewj0b-bM9i3fh5jEb4goJNIzR5285gLLzSHCfVrD5gQiiooJwCQLAo5YuCzfGeo05PkoqFH81OZ3Iq7qEQMLuKw8Y_HVCsmldAUhIKSiYoaErQAGfPQiF3PQafvX2jqCPA47uCze04HGwQ4TqibAbsWQSGwVLRZaf8zNZWP0IYWOMOZ-Ma-bw0zTzwNiZpuov-Qdf8cfHAJPCHvIBbHcLK54OPIrGA2ltkJXOoKbMSzTXxcMAXGki5Kk9KPtIRKK1esZoIUmLUxCgKnas1z2N10pbuxLiH2pmimSMq5DvPd3m9plVATJ8mB73WZNslENw9GZ7ZZr7LLQlU9SVoNKoH_sOrLNyD5E6E463274wkf9ngN14M1M8gZGZb6uzME87j6rBIq3UlfKts3An-1ap7lujs5xJdFvD7ZjhGzsheFWzgI8j44Uklo4avcd5_bLbxbDx_kFAAx5yg2tF0L-OueaQL69jWd7FvsNECZwVYjczz9wnGS8ilbVUMeGm06qqQi2mdHmo" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">💥
✔️
سوپرگل فوق‌العاده در لیگ‌کشور مکزیک!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/Futball180TV/106983" target="_blank">📅 09:25 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106982">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d9b6fbcb00.mp4?token=p8Ky_Gm9mfsGpTCNvqKi8s11z3zX68pvbamvAhk6RZs30B2qiho-Z6-WCIIZQ9XbzKFMp8kh32B6kYomGnaulgB9GF4ejLaEmE78yB7jnvPt-Vpj6B_5XFOlDXXwhPmNJKTBNZmv7Gdgzn33TaxMQa07eCN3ALesEHkWb9ad5GYTMyE-xwF7pI5nIfYHBUspdxYHMVyvbNUGu52mpfoAmnu9u3ft4BFiYL8jhBk4xsnvli5KAqLzJe7ttAJ7kuLhYEpZZR-3DGK81RAiAvjdg4Avt6jLA1XBQTsa_hshzJepx04qsXcYZvdjbK2iSJmFC_w6PyjLAFceun8JG_d4Eg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d9b6fbcb00.mp4?token=p8Ky_Gm9mfsGpTCNvqKi8s11z3zX68pvbamvAhk6RZs30B2qiho-Z6-WCIIZQ9XbzKFMp8kh32B6kYomGnaulgB9GF4ejLaEmE78yB7jnvPt-Vpj6B_5XFOlDXXwhPmNJKTBNZmv7Gdgzn33TaxMQa07eCN3ALesEHkWb9ad5GYTMyE-xwF7pI5nIfYHBUspdxYHMVyvbNUGu52mpfoAmnu9u3ft4BFiYL8jhBk4xsnvli5KAqLzJe7ttAJ7kuLhYEpZZR-3DGK81RAiAvjdg4Avt6jLA1XBQTsa_hshzJepx04qsXcYZvdjbK2iSJmFC_w6PyjLAFceun8JG_d4Eg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
فاصله بارسا و رئال به شش امتیاز رسید.
👀
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/Futball180TV/106982" target="_blank">📅 08:00 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106979">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pDAXwPLlZ2Wf5VPYg45VIN3Du5aTKqW2nJ5VFdBBxV_NGf10QwvLmG16_fynSVrLpsO076lT37HgVKDLzzSiM-qqPCM5CsHAwglGSnFRymJredV0OvR_NhAajYGu3Sq9fEyUMU9c-ljNOOqjXvfDHeNEn2rVoGMM-t8H42sUao-ER-tRWNe2UrpMqrxhl0HEtPMkLXQWxwK4yZBAvUwi00BBgrQ2XTwwkfs27_8sSU-V1g4LLMWH-WCxDhIdYu9Gz9Syh5V8gMQvMHqgOQZUih1X1Ej_AZSt4UFCgatkCmgzsa9fhhHx99MzD9J20hNbV5G33dIAViEecS_dhpHHYw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
‼️
🇪🇸
سیمئونه درباره بارسلونا:
🔻
انگار اونا دارن یه ورزش دیگه‌ای رو بازی می‌کنن، نه همونی که ما بازی می‌کنیم. مهاجم شماره ۹ نداشتن، ولی یهو رافینیا از راه رسید و ۱۲ گل زد. یامال هم اگه اشتباه نکنم ۷ گل زده.
🔻
توی زمین خودت بهت فشار میارن، زمان رو ازت می‌گیرن و از ریسک کردن و گل خوردن هم نمی‌ترسن. حتی انگار گل خوردن باعث میشه بهتر بازی کنن. اونا الان بهترین تیم هستن.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/Futball180TV/106979" target="_blank">📅 00:45 · 30 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>

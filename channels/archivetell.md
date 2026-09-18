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
<img src="https://cdn4.telesco.pe/file/ShabyjEJP9kJdgnLBIizG_httKWOyWL0bjkU_9vAtkBzT_YU_W_GmbDTJlq9eV7Kc6vZmdxm208JecINxnhnqX4zQEBV1ntHD3eveLtRlBQrdVdEkq-selQv_6dj7aC4cNe7c-lfmL7y0gmr6RSNh43N_Z7bB2WC-NmJBC5OPXDoWECn3ZsW_c5BQtdiKMmuSw-qzxjTS6E2uhEGhBgdqIr6wkZ_oiFOgq4Ab6mbPvIxi-wW8IU6JCf3CyPMPnIIqCQ7xxR97468NIpk0Cy8v20mkzalArLsgdyoaineONt2ldkhFTGQW6p3wp3iSYvF0llEkX_sVqUHKIFRFVlTAQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 ArchiveTel</h1>
<p>@archivetell • 👥 10.1K عضو</p>
<a href="https://t.me/archivetell" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ‌‌‏🚀‏ آرشیوتل‌‏مرجع تخصصی معرفی، آرشیو و آموزش ابزارهای متن‌باز و پروکسی‌های مدرن.🛠بررسی روش‌های پایدار برای دور زدن فیلترینگ و اینترنت ملیآموزش‌های فنی به زبان ساده!🌐تبلیغات دایرکت کانالwww.youtube.com/@ArchiveTell</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-27 16:01:22</div>
<hr>

<div class="tg-post" id="msg-7775">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QZT926GdBncDA33wg4Ta_rHCkf8W88JzUm-UNDLu2Dl-9mOaC18W6PJD3TEH7xmSAf5SewBzlrC0hlU86a01ojLMoQSmW7mz9bkOReW9cfdmw-YpmTiqkgu5961UolhUq8fz6TX5xUt3S3i9ZkUCKyGlwatUQetZzexJTAqDSR51RW1xE3g74b89nlLIpD-SYFga9jxfDeFusQTB1EvVibN6btFiexghuzn3ezmlO5rhh3UVXkRYCET9TtxlKaUwFsKSGgIgKHNV2sjOueAJa7iGl3gL8Knk9kkdL5Wge9_x12C17XtlN1t-hoG163VE1NB0skNoWqWpX4DF071q9g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎥
تبدیل خودکار هر مقاله به ویدیوی کامل یوتیوب!
بچه‌ها این اسکیل جدید کلود رسماً برگ‌ریزونه؛ با
Anything2Explainer
کافیه یک متن، مقاله یا موضوع بهش بدید تا تحویلتون یک فایل آماده MP4 با موشن و صدا بده.
✨
ویژگی‌های کلیدی:
🔺
فول اتوماتیک:
سناریو می‌نویسه، استوری‌بورد می‌کشه، انیمیشن می‌سازه و زیرنویس اضافه می‌کنه.
🔺
صداگذاری اختصاصی:
روی ویدیو با هوش مصنوعی نریشن و وویس باکیفیت میندازه.
🔺
کاملاً رایگان و متن‌باز:
با یک خط کامند راه می‌افته و خروجی تمیز بدون واترمارک میده.
💡
نکته/استفاده:
آماده‌سازی کل ویدیو با تمام جزییات حدود ۱ ساعت زمان می‌بره و همه پروسه صفر تا صد توسط AI هندل میشه.
🔗
سورس پروژه در گیت‌هاب
✈️
@ArchiveTell
|
#TOOLS</div>
<div class="tg-footer">👁️ 774 · <a href="https://t.me/ArchiveTell/7775" target="_blank">📅 13:02 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7774">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b6370f25b3.mp4?token=MVsd2FmVVzjAPTgOVOhN4yjfOve2J2PX02yq6bndHwMqjcx8qdpMFLVLyYqJj7JVW2jZw7zQKE8V9l45gZHb-2b7VCYGDqQdJV2uY-TVz9O7QP2m8XxwVvDHP_DLNzoSlCv3vJdYnu_6lcAuHRv5kAsva0AvYvCMKN6tsNRxM_eLzVm4slELmYoS9m3aVvKRWrr9FqN-3I30fgXZyqEgvRB8_XK-OmtuTtGZ5VBOf04_tFAe9z53YvmlM3aSKO3JOk_V5M5Fh-ZEANgRJOFQot_NaBLpYvnNBO65rKZF3o_m8CTszYt32wuxFujjjJsMgAkl2y-Yek42c0Ga2G7RtTWTCx3KnDmB4bIkVOs6UaDEGgwyWwuEiur0XFI_fTP4iQVXAPxJ3tX4Xlit7EDycodUZRP6sqULZWmr0XM3UBx-uKjWki7hRcO5iJayx8Y79WVBiCSK4At_FdhozAf6VXt0h_yyZ2OAcl6V0EycJDfFObtRkqF2lmWiJFaoxx_DGqynga2TYpUSxsaRM1y-Lg3VrtrIjK7iECDX9N8XhKamgXU7lxDzaGTanhteHAr9bXnpAicPgHUARARg-yolNS-_kUuswgV-FQOCw1BRN8nYbsRSZECHof0g-4Ne_xBdzRDwkEayjYKKeEiXzdnmTkGrqnMNBu_icsKseHh-4fs" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b6370f25b3.mp4?token=MVsd2FmVVzjAPTgOVOhN4yjfOve2J2PX02yq6bndHwMqjcx8qdpMFLVLyYqJj7JVW2jZw7zQKE8V9l45gZHb-2b7VCYGDqQdJV2uY-TVz9O7QP2m8XxwVvDHP_DLNzoSlCv3vJdYnu_6lcAuHRv5kAsva0AvYvCMKN6tsNRxM_eLzVm4slELmYoS9m3aVvKRWrr9FqN-3I30fgXZyqEgvRB8_XK-OmtuTtGZ5VBOf04_tFAe9z53YvmlM3aSKO3JOk_V5M5Fh-ZEANgRJOFQot_NaBLpYvnNBO65rKZF3o_m8CTszYt32wuxFujjjJsMgAkl2y-Yek42c0Ga2G7RtTWTCx3KnDmB4bIkVOs6UaDEGgwyWwuEiur0XFI_fTP4iQVXAPxJ3tX4Xlit7EDycodUZRP6sqULZWmr0XM3UBx-uKjWki7hRcO5iJayx8Y79WVBiCSK4At_FdhozAf6VXt0h_yyZ2OAcl6V0EycJDfFObtRkqF2lmWiJFaoxx_DGqynga2TYpUSxsaRM1y-Lg3VrtrIjK7iECDX9N8XhKamgXU7lxDzaGTanhteHAr9bXnpAicPgHUARARg-yolNS-_kUuswgV-FQOCw1BRN8nYbsRSZECHof0g-4Ne_xBdzRDwkEayjYKKeEiXzdnmTkGrqnMNBu_icsKseHh-4fs" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔍
با این مدل، هر عکسی رو با یک کلیک تا 4K آپ‌اسکیل کن!
بچه‌ها اگه عکس تار یا بی‌کیفیت دارین که می‌خواین زنده‌ش کنین، مدل خفن
Crystal Upscaler
دقیقاً همون چیزیه که دنبالش بودین.
✨
ویژگی‌های کلیدی:
🔺
خداحافظی با ماتی:
عکس رو مات و غیرطبیعی نمی‌کنه و جزئیات واقعی رو حفظ می‌کنه.
🔺
کیفیت تا 4K:
رزولوشن رو تا بالاترین حد ممکن بالا می‌کشه.
🔺
عملکرد جادویی:
خروجیش رسماً شبیه زوم‌های فوق‌العاده توی فیلم‌های علمی‌تخیلیه!
💡
نکته/استفاده:
نیازی به سیستم قوی نداری؛ می‌تونی مستقیماً روی بستر وب و از طریق FalAI آنلاین تستش کنی.
🔗
لینک تست و استفاده
✈️
@ArchiveTell
|
#TOOLS</div>
<div class="tg-footer">👁️ 953 · <a href="https://t.me/ArchiveTell/7774" target="_blank">📅 11:22 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7769">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/EU87ErMB0X_jXMCoW_oblEGmYXVu-51ZZ4kS5tshza6w2BLxGnF1_rLzV9Bsc0Vb1U07-nyvyNzEP2LX_OXifk-vBfSr8BZL6zNK8pfj596iOUckwyeaqr6zACJqAORlZDTfbX4vfcUL82p0_YnxwnCzRzh_lbGjdSrFn_puCAhwTGDin1ZSQa-mPOV8jskZhdcsdI57vAhJss6CXBTl8OWdWDveZNmvbGPCgiReNYrcH8U2mey9mfNALyd3VIlxcDMCNyfiW6C0NU5y22v7-t5iHpw1mt0EGUgYHCGKFB0VpQ0A80KjKli9nUIa2hfaF-R_R0_-r64l5GkKChnGiQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/d4FJIGGAjyP6Uu_L7d5-43AJT7Ky9kzkj_XNouSjXl2xAc_5vs8hpZUfZtr48cCNKrWS-pHae3GfAMa3_lTEqxhNDxM0XNkRrQ0xzmR20eCWgwdweNhVAvFqxvJ16zLjzlVJOpWpXlhhepdsEMzQWqySSGHrtJY8qyKB9dubnVRqBhl2Ckfu2T5vEqpaMGOaMmwAoxkTURC3rp9Ojtogo9Iw8Kmpd73Z18TTVZNgQYqcmFbAmaklHZw_Sq2wmXlPoa6V04BmAORQrUroB1gQK1XTr-4IxVBt0q3OLgPsW8Av_SBQv5iGQpW1f-NhG6lttKgqtgaww-qVKx7Hiy10JA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/mAnbvwry5uLpeKfqmtsVpwazs-S78kQjOjX7wjQVTL7vSWGkwC8cX3NVxDlEUyeG2auaj3JDBtUdbDaH6NJWLEZ4tOPTVbwYVrnDZ6otL_su467xeoebtRoheAwA_0G_nKeNllvlko58bcRcGTQ0LU95GpqKr7q8TmD5fegmzCTt2U86N3ul_ZRTx44OMO6KDOTisy0522p3RwcCrUOonN5fY_x0FTJEXWjipARPQlq18-J0b7isoPcSrOw1M83jcsMsaNkvy6d2BMDYT6Mmw0aTcEBe9dWWo7dH-Csec6bREV8PZ9jEguJLoki9Ycp8xll8d361v6_FshgMp3cnMQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d3248c435c.mp4?token=PRzLMxMfC0TmDN1thswtj2G277Pg_Xs3Dht43msxyUU2XlsTTPZ-hmEb3rcjkOOqp1q-jxsYsybXkNF_rX6uSrDJkcNKIYBtVdUNGzlWzpEVpTeEQQZWVv4PAWSrVdqlNNCw_KXH9mTYflUwYEs3iD9gyt3LzsF_TgYjKLS0zi3r1z4SU6LuiQtPWcLdkO2T0z1JzBBLwOZOq9BdSLzNudlAQsGiScZleRUgVDJFDtlQdu6Q3LCQeN-RYcM7VS2-uHJEBfD8Pecd9nMLihveE2XWLTWkv_CTRQBq_V1r0wZ74xuMCy84NVkP5CTCOoyLkDB5kWNa_o5XaCMvh7YW6g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d3248c435c.mp4?token=PRzLMxMfC0TmDN1thswtj2G277Pg_Xs3Dht43msxyUU2XlsTTPZ-hmEb3rcjkOOqp1q-jxsYsybXkNF_rX6uSrDJkcNKIYBtVdUNGzlWzpEVpTeEQQZWVv4PAWSrVdqlNNCw_KXH9mTYflUwYEs3iD9gyt3LzsF_TgYjKLS0zi3r1z4SU6LuiQtPWcLdkO2T0z1JzBBLwOZOq9BdSLzNudlAQsGiScZleRUgVDJFDtlQdu6Q3LCQeN-RYcM7VS2-uHJEBfD8Pecd9nMLihveE2XWLTWkv_CTRQBq_V1r0wZ74xuMCy84NVkP5CTCOoyLkDB5kWNa_o5XaCMvh7YW6g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏
Arrow 2؛ قدرتمندترین مولد تصاویر وکتور!
🎨
‏مدل
Arrow 2
اومده که کار طراحان و تصویرسازها رو خیلی راحت می‌کنه و ساخت وکتور رو به شدت سرعت میده.
‏
🤔
کاربرد متنوع:
ساخت انواع آیکون، لوگو و اتودهای گرافیکی با دقت بالا
🎯
‏
🤔
خروجی حرفه‌ای:
تبدیل پرامپت‌ها به طرح‌های برداری تمیز و قابل ویرایش
📐
‏
🤔
تست رایگان:
دسترسی به دو هفته
trial
برای شروع کار با ابزار
⏳
‏این ابزار خوراک بچه‌های طراح و گیک‌های گرافیکه
🔗
لینک دسترسی
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.39K · <a href="https://t.me/ArchiveTell/7769" target="_blank">📅 20:29 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7768">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">یه مدل جدید و قوی برای کدنویسی اومد و فعلاً رایگانه
🔥
‏Union Alpha امروز روی OpenRouter و OpenCode در دسترس قرار گرفت
✨
‏چیزایی که داره:  ‏
✅
Context ۲۶۲ هزار توکنی (تقریباً کل یه پروژه‌ی بزرگ رو یکجا می‌تونی بدی)  ‏
✅
پشتیبانی از تصویر (اسکرین‌شات و دیاگرام…</div>
<div class="tg-footer">👁️ 1.4K · <a href="https://t.me/ArchiveTell/7768" target="_blank">📅 20:16 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7767">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oBgVrhjuVGG5ORDuWaXCnHBWn2CAJwFgQyAUMnyYMpEwGQ8jFzMhcf7Ny1sIJEEzUxohzs1C3Cgek91y9b__oQ-gjdvswFzKw1GuzjxRW8PtDAIkRr1UrtAedM7ICAWezoDrHmDPOhjW-4ULQDNg91kGag__Iogwxi1bCqEBOVwDugYD8Dp1FcJodjfuxU_ukfJFOGloFbl93peIu300afw64q284pmLbR_VfsP5GYyA2f0Y3_DwMAUNTtMmpAu6uu_qyyv8BhEsA3KxROLNj2CV2oubf11zCpPKRYIkLmiOm0Hj9OXIQL4qB-iA6yz-VZxggLDANsqZBqtP15XKEQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یه مدل جدید و قوی برای کدنویسی اومد و فعلاً رایگانه
🔥
‏
Union Alpha
امروز روی
OpenRouter
و
OpenCode
در دسترس قرار گرفت
✨
‏
چیزایی که داره:
‏
✅
Context ۲۶۲ هزار توکنی (تقریباً کل یه پروژه‌ی بزرگ رو یکجا می‌تونی بدی)
‏
✅
پشتیبانی از تصویر (اسکرین‌شات و دیاگرام هم می‌فهمه)
‏
✅
Tool calling و structured output
‏
✅
بهینه‌شده برای کارهای agentic و کدنویسی خودکار
‏
✅
داده‌هات برای آموزش مدل استفاده نمی‌شه
‏فعلاً کاملاً رایگانه
🆓
‏
🔗
لینک مستقیم:
‏
https://openrouter.ai/stealth/union-alpha
نظراتتون رو بگید
👇
🔹
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.66K · <a href="https://t.me/ArchiveTell/7767" target="_blank">📅 21:47 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7766">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">😎
یک میلیارد توکن Muse 1.3 به صورت رایگان
به کاربران جدید، تا یک میلیارد توکن در Muse 1.3 ارائه می‌شود.
(این توکن‌ها از طریق API ارائه نمی‌شوند، بلکه از طریق وب‌سایت توزیع می‌شوند.)
اینجا
ثبت‌نام کنید (از VPN آمریکا استفاده کنید)
بعد از ثبت‌نام، در تنظیمات، کد تخفیف زیر را وارد کنید:
LYA0IL
+ در opencode، این مدل به صورت رایگان ارائه می‌شود.
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.56K · <a href="https://t.me/ArchiveTell/7766" target="_blank">📅 20:23 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7765">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">🚀
بدون یک خط کدنویسی، برنامه‌نویس شو
😱
(جادوی Vibe Coding)
دیگه لازم نیست ماه‌ها وقت بذارید کدنویسی یاد بگیرید.
الان فقط کافیه با زبون آدمیزاد (فارسی یا انگلیسی) به هوش مصنوعی دستور بدید تا براتون برنامه بسازه! به این کار میگن
Vibe Coding
(برنامه‌نویسایی که میگن الکیه کیفیت خوبی نمیده، حتی اونام از این استفاده میکنن
😂
)
برای اینکه مثل یک حرفه‌ای خفن‌ترین پروژه‌ها رو بالا بیارید، این ۴ قدم رو پیش برید (پست رو سیو کنید که به کارتون میاد):
۱. اول نقشه بکش (Deep Research)
همون اول نگید "فلان اپلیکیشن رو بساز". اول بهش بگید:
💬
"ایده‌م فلان چیزه. بهترین روش پیاده‌سازیش چیه؟ چالش‌هاش چیه؟ برام یه دیپ‌ریسرچ (Deep Research) انجام بده."
۲. گیرِ تله‌ی پایتون نیفت!
🪤
هوش مصنوعی عاشق پایتونه، ولی همیشه بهترین و بهینه‌ترین گزینه نیست! بهش بگید:
💬
"سبک‌ترین و بهترین زبان برای این پروژه چیه که اجرای اون دردسر نداشته باشه؟"
(مثلاً خیلی وقتا یه فایل HTML ساده که تو مرورگر باز میشه، کارتون رو راه میندازه).
۳. لقمه‌لقمه پیش برو (توسعه ماژولار)
🧩
بهش نگید "یه فروشگاه برام بساز" چون قاطی می‌کنه! تیکه‌تیکه پیش برید:
۱.
"اول ظاهر صفحه رو بساز."
۲.
"حالا کاری کن دکمه‌ها کار کنن."
۳.
"حالا اطلاعات رو ذخیره کن."
۴. ارور دادی؟ فدای سرت!
🐛
کد رو زدی و ارور داد؟ اصلا نترس! تو وایب کدینگ، ارورها بهترین دوست شما هستن. متن ارور رو کپی کن و بهش بگو:
💬
"این ارور رو داد، مشکل کجاست؟"
خودش باگ رو پیدا و حل می‌کنه.
🔥
با چی این کارا رو بکنیم؟
با همین مدل های زبانی هم میشه انجام داد ولی ایجنت های حرفه ای مثل Claude code و Google Antigravity هم میشه استفاده کرد.
👇
تا حالا با هوش مصنوعی چیزی ساختی؟ تو کامنت‌ها
معرفی کن رایگان تو چنل بزاریم
✈️
@ArchiveTell
| S</div>
<div class="tg-footer">👁️ 1.58K · <a href="https://t.me/ArchiveTell/7765" target="_blank">📅 18:02 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7764">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">پروژه bkup یک پروژه اوپن‌سورس برای اینه که فرایند بکاپ‌گیری و بازیابی پنل‌ها، ساده، متمرکز و قابل مدیریت باشه.
🎉
نسخه 1.2.0 منتشر شد.
⚙️
تغییرات این نسخه:
اضافه شدن
Restore
برای بازیابی مستقیم بکاپ روی سرور از طریق
SSH
پشتیبانی از
3x-ui، HM Panel، PasarGuard, Rebecca
برای Restore
پشتیبانی از بکاپ‌های حجیم و چندبخشی
➕
امکانات کلی bkup:
بکاپ‌گیری زمان‌بندی‌شده، ارسال مستقیم بکاپ‌ها به
Telegram
، پشتیبانی از بکاپ‌های حجیم و چندبخشی، مدیریت بکاپ‌ها، تاریخچه و لاگ‌ها،
Reassemble
فایل‌های چندبخشی و
Restore مستقیم بکاپ روی سرور از طریق SSH
.
همچنین امکان نصب خودکار پنل در زمان Restore، خروجی گرفتن از تنظیمات و انتقال آن‌ها به سرور دیگر و اجرای پنل به‌صورت
PWA
هم اضافه شد.
⭐️
اگر bkup براتون مفید بوده حتی یک STAR
روی GitHub می‌تونه بزرگ‌ترین حمایت برای ادامه  توسعه پروژه باشه.
🔗
github.com/AliRezaC-xrol/bkup
✈️
@ArchiveTell
|
#SHOWCASE</div>
<div class="tg-footer">👁️ 1.47K · <a href="https://t.me/ArchiveTell/7764" target="_blank">📅 16:06 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7763">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AhIvFlviCzJ61NG6xUmXVar-klgwPXuR-whjWkowmPLCmkXkmy4HjrlCwzpmhtAbE7olXFCvzbmKFUPdp2z3C873lnUCXuDlaScdXAykN-RBzQm3P_ODu1-eLp1jSzW5eiw1lZYuu_B1vSvmZSB_DZ5Scb52a6WxYKwdPtFxTC0Q55SQP2MGr2DZ6l8KKn-0z_nRwswJ_ohrwJMgbVGmDJnzTFyyptvSikjRKhB0OV5SVwWPo3Isi5EaKkkq60pkkS6RjiJju_RBqMpbMHkX0TOeHdD1-9dafJRJqP089TvSy0OYei_7ABTxtj_2NgC-DvrnlyBRKIyg-ubnLjfW6g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">😎
مدل جدید دیگری از شرکت‌های چینی با نام ATRIA عرضه شده است. آن‌ها 100 میلیون توکن را به صورت رایگان برای هر حساب کاربری ارائه می‌دهند.
اینجا
می‌توانید با استفاده از حساب کاربری Gmail خود ثبت‌نام کنید، یک کلید API ایجاد کنید و از آن در صورت نیاز استفاده کنید.
نتایج تست‌های عملکرد در تصویر نشان داده شده است.
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.44K · <a href="https://t.me/ArchiveTell/7763" target="_blank">📅 14:47 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7762">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">⌨️
آدرس‌های ایمیل رایگان برای استفاده‌های مختلف در سال 2026: یک فهرست کامل - بیش از 60 سرویس
▫️
تکنیک "نقطه" در Gmail - اساس همه چیز
username+anything@gmail.com
→ همه ایمیل‌ها در یک صندوق اصلی. استفاده از IMAP از طریق App Password. هزاران نام کاربری فرعی. محدودیت: سیستم ضد تقلب گوگل - حداکثر 20-30 ثبت نام در ساعت، تغییر IP. سرویس‌های Oracle/Webshare، نام‌های کاربری فرعی را در مرحله اعتبارسنجی مسدود می‌کنند.
؛ SmailPro - آدرس‌های
واقعی
جیمیل ایجاد می‌کند، با بیش از 5000 آدرس در دسترس. تحویل در کمتر از 10 ثانیه. از تست‌های تشخیص ایمیل‌های یک‌بارمصرف عبور می‌کند، زیرا یک جیمیل واقعی است.
▫️
تقریباً همه جا کار می‌کند
؛ SimpleLogin —
نام‌های کاربری فرعی نامحدود
(در اکوسیستم Proton)، فوروارد و پاسخ با استفاده از نام کاربری فرعی. متن باز. نسخه رایگان: 10 نام کاربری فرعی
؛
addy.io
— قبلاً AnonAddy،
رایگان‌ترین سرویس
: نام‌های کاربری فرعی استاندارد نامحدود، متن باز، امکان میزبانی شخصی
؛ Cloudflare Email Routing
*
@your
domain.com
→ فوروارد به هر جایی. رایگان، بدون نیاز به سرور. ایده‌آل با دامنه .pp.ua
؛ ImprovMX — فوروارد رایگان برای دامنه شما، 25 نام کاربری فرعی
؛
33mail.com
— نام‌های کاربری فرعی + پاسخ‌های ناشناس
؛
spamgourmet.com
— نام‌های کاربری فرعی خود تخریبی
؛
erine.email
— فورواردینگ خصوصی
▫️
ارائه‌دهندگان ایمیل IMAP (غیر موقت، در همه جا کار می‌کنند)
-
mail.ru
-
rambler.ru
-
yandex.ru
-
aol.com
-
gmx.com
▫️
ایمیل‌های موقت با API (قابل اسکریپت‌نویسی)
-
mail.tm
-
1secmail.com
-
guerrillamail.com
-
temp-mail.org
-
mail7.io
-
anonaddy.com
▫️
ایمیل‌های موقت بدون API (وب)
yopmail.com
·
temp-mail.io
·
dropmail.me
·
emailfake.com
·
emailnator.com
·
mohmal.com
·
tempail.com
·
getnada.com
·
inboxkitten.com
·
mailinator.com
·
burnermail.io
·
fakemail.net
·
tempmail.plus
·
mail.td
·
mailpoof.com
·
trash-mail.com
·
temp-mails.com
·
emaildrop.io
·
temporarymail.com
·
generator.email
·
mailsac.com
·
tempr.email
·
atomicmail.io
·
emailondeck.com
·
crazymailing.com
·
tempmail100.com
·
tempmail.ninja
·
boomlify.com
·
tempmail.dev
·
internxt.com
·
adguard.com/temp-mail
·
webmail.raoshahzaib.site
▫️
بات‌های تلگرام برای ایمیل‌های موقت
@e2tgPM_bot
·
@mailtemprobot
·
@hidemail_bot
·
@TapMailBBot
·
@botmail_io_bot
·
@temp_mail_bot
·
@fakemailbot
·
@etlgr_bot
·
@DropmailBot
·
@tmpmailbot
·
@TempMail_org_bot
·
@TempMailer_bot
·
@smtpbot
·
@SenthyBot
·
@TempMailBot
@telegaemail_bot
·
@hs_temp_mail_bot
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.31K · <a href="https://t.me/ArchiveTell/7762" target="_blank">📅 14:42 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7761">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">😎
دسترسی رایگان به FABLE 5، OPUS 5 و GPT-6 ASTRA
مبلغی معادل 1 دلار به عنوان سرمایه اولیه ارائه می‌دهد، اما با توجه به ضرایب، این مبلغ به موارد زیر تبدیل می‌شود:
🤔
Fable 5 → تقریباً 7 دلار
🤔
GPT-6 Astra → تقریباً 18 دلار
🤔
Opus 5 → تقریباً 20 دلار
استفاده از چند حساب کاربری (Multi-accounting) امکان‌پذیر است.
————————————
📝
نحوه کار:
1. به
وب‌سایت
مراجعه کنید و از طریق حساب Google خود وارد شوید.
2. یک کلید API ایجاد کنید.
3. آدرس پایه (Base URL):
https://www.rsiai.net/v1
4. برای مشاهده مدل‌ها، به وب‌سایت مراجعه کنید.
————————————
💻
نحوه اتصال:
Claude Desktop (Code):
- Help → Troubleshooting → Enable Developer Mode
- Developer → Configure third-party interface
- مقادیر زیر را وارد کنید: baseURL، api-key، model-id
————————————
♾️
دسترسی نامحدود:
1. یک پروفایل جدید در یک مرورگر ضد تشخیص (anti-detect browser) ایجاد کنید و موقعیت مکانی خود را تغییر دهید.
2. یک حساب کاربری جدید ایجاد و کلید را دریافت کنید.
3. کلید API را در کلاینت خود جایگزین کنید.
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.43K · <a href="https://t.me/ArchiveTell/7761" target="_blank">📅 14:13 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7759">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn5.telesco.pe/file/Zc5tjRwl9oM7NDWRvgr6p_X0-OgE78xDhFFLJVxHaF1m_x_RTjQ0FAQY3ICr2kxXEFHKEJplbUghh2qK5Fuhd465HdyRfPy0Vwi97lIvH2COOLvuDa8nSFR72MukcQN2AcG9Uaa5_uqK1QrmgnTwooylNIUkGqRqi8-SEPe8Tza3s7D4FQ0DsvfYwyE2mqGNThEYA4OJS8s5UsftriJhrIVRBDPbZbmwlnPDiP9sa9Pf60AeeMzEnWjFC2cLGtX6LPjM3pxRe-nlaXZcUPqwPhwL0GSnI2GfXN9bifPJmq8LmX4hlfwWdavijKTlYHZBQ_DQ1rY76_eguWRt1Z3wxg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn5.telesco.pe/file/sCsmPZRpimnHKJk15ZrEaewKdHOGkxCQqlUkiDxO4gO507P3Pa5RS_4_NK_78_7de5_zj_H36eJFSfsoKoPFwEferRWRR4VHOMBHqyu0TqGeZeyvAU5pbU7mA6-Hn8xRnFAjq8edLywHgQOhVTTnrZYGaCrtbQ4T_0SfC9b4Pi_w3nxPnPzD0IEQthBbZRn_wrYEnyeEEmnBNkiF-QAFXu2IC6GxzXgFToJiVkyzsq-YzChRiScgWr6JfCCpOPaS5jgY0wA5NHcJOc2l0GDkIN-nAu2IicRE_dW6LGM1B9STlcw9IoJHnzLrv8cFKLx0SGLD9JO55MHSy8NWbzbd_w.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">‏
🔥
کلونر اتوماتیک و خفن تلگرام روی کلودفلر!
‏بچه‌ها، این ابزار Serverless روی ‌Cloudflare Workers⁩ بالا میاد و خوراکِ کپی کردن و همگام‌سازی کانال‌هاست؛ بدون نیاز به سرور و کاملاً رایگان.
‏
امکانات اصلی:
‏•
🚀
دیپلوی تک‌کلیکی:
بدون دردسر و سریع روی زیرساخت کلودفلر بالا میاد.
‏•
⚙️
فیلترهای پیشرفته:
می‌تونید فایل‌ها رو بر اساس نوع (ویدیو، عکس، سند) یا سایز دلخواه فیلتر کنید.
‏•
🤖
چند بات همزمان:
هر تعداد بات که خواستید اضافه کنید و تسک‌ها رو بدون محدودیت مدیریت کنید.
‏•
⏱️
همگام‌سازی لحظه‌ای:
هم بکلایت تاریخچه رو انجام میده و هم پست‌های جدید رو هر دقیقه سینک می‌کنه.
‏می‌تونید سورس کاملشو از گیت‌هاب (‌
iamLiquidX/telegram-clone-worker⁩
) بگیرید و با یه استار حمایتش کنید.
⭐
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.52K · <a href="https://t.me/ArchiveTell/7759" target="_blank">📅 12:19 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7753">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn5.telesco.pe/file/N1_pFID8lGE3PKgqO4eXhW3IjTdQxn2psKlYLCRKi6sOV6tPqMxSlLmz1MlbxKbAx879vp5lmcRM6fiWD6ounxesu7dik0GYBiZBxtkPC4ZwPmv86G6DQx-D91okMtH709Igz5mam-1z-Qn1UcLvsRXfZ19Khej6B1zAzzcHU7keavgcQQE1daQ7aYDGVZ4bNu_biocySgVz7VgzHuO1CiDfk4R12mrTha4obMUzQmFHhRHPL99vIMkfJ4EpK8RTXWz8t40zktUTJ57shzb7LpImoBz8AllmMqaozkeGPy_qJrjfktV9551bU_ESS-w5n2ZwvKfgMJQeTBWbP9C9Ag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn5.telesco.pe/file/rAYRYKpVPRK84-No38-6G0CYk971QzIJWQEFVF3uUjr0VsI3SS782G1eMuEzdiB-7h7Lzwn6g-eGBVnydehf6PxE6PuSF-5Uo3ddUbYl4tfJWTtBsksczOlRmYYHyUzUxyolRkYndBWI51qyiRrkqCf5Dp-XQl5ewej_b-SAMo0CTy9lfgPFXGjdSzK4pc-iwpZPHugFKtQcCXdITqZmsEPCWLUcvO4ErONx7VK0ou-XqEG0uqahk8WftP-_Z5D55EjMv5fOEhHFwp0KbMgbNukOqt2hqoeuUrAYUugQCx4zBNoinumZAU7iDTkzYTEwN2g62dEdlSD_B_4JgqIPhw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn5.telesco.pe/file/dcpR2YtpxeUC6PFJwb-1WEsFjdNUX3rcu6YM-lj-SIiQtzEAHUOadPTzctS_aBZuy0J0y2Z4oj1VbCmGob_3k_z37S4dwSiXD6k8LplwObZB50r3L8rDO7RAOcJLLsRov2qHnPQGmxmke8UB1R7UzSwM3M1MHmfoCbTs0-82n5lkcJ5uEhA1d79ndsmUsECZ7jm9K7ne26GdCt3-APF_1fPr2cUS2Jt42MP19pHiFcTFjn4-CP2adwARJE4Qq1krM6E0qg0BKxIkjRpFf1LvYuhRqFZjySqVfh1O0mXh9aJZlbWoz-sADHnwYsziNWHUvTcPIPXAlPhlKCasw2yoLA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn5.telesco.pe/file/JL0MHpAWbnBlf3GujKMHabnnjeeBptkBvWshZSPWsT-YGq4xCOoo44bFj-ChBGBdNCJJ9ykI8zeBh3fKv-A8k4zeuy4G1ULbpLiF3Maq3uVc5X255d2cw_sLXQcM7u5pFA3RIX-NCG2-Hyk-AbZkr6jvrdaAecAvoBCg-AGQEchh1tdJ66bjM2LDSsfGu6gdYZDFpWuqIgfowjqlpvnpWbmDG-PfuwHFqI336mrjnOEJFfLVnKCYr8qsCxw4pnZkdY-if6GtxY8Ol4MV_02ApXIRSpwzZi2O01a44NP0hcgW3rw_frWhrlpWJyJZbMtb2CTv7h1i1EkjrGPz-kQz5g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn5.telesco.pe/file/saA-1BSpNoyILtZ2swQ5I3h3OzXYSYo4KooeYNPW7NT6CijC9u0jd3ID_feD8RsFPoEHx36vpNCaeeMwsPfK5qrzFrM0e_1DIm_uT-GEkFsInb1lZUJrm3bhxK1ZsjaBrwnxIyaXzNQOmYFikd5lqzoCnxBvAhdghIDnUR0bIEJm2VCu2b2IW1CU9jSgOe8XNPwPVCK-VBiWcB8prCVdKEIUl4x73PG5FCuVBw44sBymkXklZ4qt_f0_o65x_iVGmRbDCGxRyMlyPvOMbueh7EEiOXFqaIY-gL9UJEZuep7YzB34mdyPcpHW7BmBWWefgBn58GAnDePaPFHabAGGvg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn5.telesco.pe/file/do9TZt7M4Ljik1EOpKMV7WBT1kmkKWTH7d4DgKbxCo8xdcLHDrtldSCMwQPRDJ-pFuLAH36YzOWkeduKTWv6_8UhvTW9cliycaAg_Q4Jfw-BNDqPLZYZEJ01qkTze_mC93XB9Lgc4T8VRazSOdVC9mldGk3m5lIAzMBbum7srwKIOVIO5kYLTgLje5eTJhwAaccWKMpxiMQOi8NB4jnS5ALAnzdXN0lP6DJVxXAkkwC0G3wa1VFaYfLDlUF7nsemqYM3fkG9qCUHiPDApPDErHKwusxLDWhIiSzlsKxf8Do2fEbcqfhR6H5JwGqSankQCyKq2iizviHNjKh-Zjmw5A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">😎
از 265,000 اعتبار رایگان برای استفاده از مدل‌های برتر مانند GPT 6 ASTRA، CLAUDE FABLE 5.1، GLM 5.3، و غیره بهره‌مند شوید.
یک حساب کاربری جدید ایجاد کنید و فوراً 250,000 اعتبار دریافت کنید. با ورود روزانه 15,000 اعتبار دیگر کسب کنید و با انجام وظایف، اعتبار بیشتری به دست آورید. نیازی به کارت اعتباری نیست.
1min.ai
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.66K · <a href="https://t.me/ArchiveTell/7753" target="_blank">📅 10:13 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7752">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">⌨️
؛ DeepSeek V4.1 Flash، Muse Spark 1.3 و GLM-5.3 Flash به صورت رایگان در Cline Desktop
​تیم Cline یک برنامه دسکتاپ جداگانه با تمام قابلیت‌های یک عامل مستقل را راه‌اندازی کرده است.
​
📌
امکانات برنامه:
🤔
استفاده از ClinePass یا کلیدهای API شخصی
🤔
انتقال یکپارچه وظایف از Codex، Claude Code و سایر عوامل
🤔
برنامه‌ریز برای اجرای پس‌زمینه عامل
🤔
مدیریت سرورهای MCP، پلاگین‌ها و مهارت‌ها
🤔
مرورگر وب داخلی و ورودی صوتی
​
📌
مدل‌های رایگان موجود:
🤔
DeepSeek V4.1 Flash
🤔
Muse Spark 1.3
🤔
GLM-5.3 Flash
​
📌
نحوه شروع کار:
1⃣
دانلود برنامه:
https://cline.bot/desktop
2⃣
نصب و اجرای Cline Desktop
3⃣
ورود از طریق حساب Cline یا اتصال کلید API خود
4⃣
باز کردن پوشه کاری پروژه
5⃣
انتخاب یکی از مدل‌های رایگان از لیست
6⃣
ایجاد یک جلسه و اختصاص وظیفه به عامل
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.65K · <a href="https://t.me/ArchiveTell/7752" target="_blank">📅 01:44 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7751">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bm7jXtczaULbS0X9AC7zzTTJZ2Xq3MFx_GnZCYHtdIjlLSBjRGBzMTvdfz6mtvm7n2i-1hGpl-ZO_Ha74vc7mpCgpHJG2oGVJCAJMY7zcrLb4it4xuBHZGTF6lOVLhLvPR0hCk2NLKHVDH3VgozNjB2hX-gOhK6OG_jGJa0Ny9kr2DYVa4zKrefqjbIU_NVOawJYrhkiZHE4Fcydq-NuRntAtNADSyCjasmdt7DlbNg7s8N0uXC7oHLgoNj_P93WsUAn7Z52kWlkYsBDNLw9OBuk9Fa0OIdwQvh-hymuYNqDX5sfKVX-MDy4VeCUvYNyVdL0xjZih7sHlkJg9PcTJg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">😎
؛ LIGHTVELA - یک هوش مصنوعی رایگان که 24 ساعته در دسترس است.
4500 اعتبار و 100 میلیون توکن
مزایای طرح رایگان:
🤖
1 هوش مصنوعی
💳
4500 اعتبار در ماه
🖥
2 پردازنده مجازی + 4 گیگابایت رم (محیط تست)
💾
50 گیگابایت فضای ذخیره‌سازی
🌐
دسترسی 24 ساعته
📱
ادغام با تلگرام و سایر پلتفرم‌ها
نحوه دریافت:
به
lightvela.ai
مراجعه کنید.
یک حساب کاربری ایجاد کنید.
از آن استفاده کنید.
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.8K · <a href="https://t.me/ArchiveTell/7751" target="_blank">📅 22:06 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7750">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">کانفیگ مخصوص چنل -
سرعت خداا
vless://e4b11ac9-46f7-4cc0-92ed-bb9dfaaf3600@94.237.92.65:443?encryption=none&flow=xtls-rprx-vision&fp=chrome&pbk=lkMM9FR-o7Z6NwmmQVK8rLhCQR1mbJTgjY_0upeS2SY&security=reality&sid=0436301fb0178b&sni=google.com&spx=%2F442987454d44398&type=tcp#@ArchiveTell
✈️
@ArchiveTell
| S</div>
<div class="tg-footer">👁️ 1.87K · <a href="https://t.me/ArchiveTell/7750" target="_blank">📅 11:02 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7748">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/YnqGch1kSPFiyA5yybAiehBY8WRqIeWc3IWdkOnGoc2jbf04O8WDoQjRI85z8PqWoPNKC9tMrTH0Tm3cxcJQqwnWmVHhP42l8hgt3P31ShCnGZQA0Ln6FO2YgS1krfcmH1vEuEaXlOeAx2oFJ-dqZ26PW8KG9hcBmquG76-Go3r7XojSb6JwLlR2tCpp_VYlcpG6ae1WTfzToMTd-9fIVzAPjBB4igu4Ntwqeqrei6KvF0U0y1KHio6TWUh0Kujebq5qf_APx8S9eupE4ohKHl5V9sGaxAQWrGmll-CE4mlMN-j1t-gTrJfVURHOhjRsZ1pZtCBCVvNfQsnubYfP3Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">😎
از تاریخ ۱۴ تا ۱۶ سپتامبر، با ورود به
Z.ai
؛ ۶۰۰ میلیون توکن GLM-5.3 به شما تعلق می‌گیرد، بدون نیاز به اشتراک.
🔗
https://autoclaw.z.ai
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.06K · <a href="https://t.me/ArchiveTell/7748" target="_blank">📅 18:36 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7747">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/KqW3b1uj3BHpfON3JvLduLbA_DtMK0HfyHEvw3rQmmp4NAKripgLXK2JCRsuEmfZzA40Mk_YymEZOAjuC7BpvqE24WSvGvllHcpPeHkB7kjIfe-nAhdyjLDHWQ3juxafKmiwT5kWeozhZnHmZ2RYN41B9nkIIuQIeyArBmVMjKRiTslbiIOzwzKmXjUTwtM_ELN3slgV030I10fo45cWSmlL0J5TYSARN6AgXInmZOKhMpBpDGHZtcJ4NK2UnpTqB8J66QsfYxe8VBZJR8l_Ku_MXylzJsSzV2q9ivMLhg7UKu4u5OORFZHCs5U5qXtqtuz5ZXwSdTlr1JA4tJA96w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔓
رفع فوری خطای ریجن و تحریم Antigravity
اگر موقع کار با هوش مصنوعی Antigravity گوگل با خطای تحریم ریجن یا گیر کردن روی Eligibility Check روبرو شدید، ابزار متن‌باز
Open AG Patcher
در چند ثانیه این مشکل رو حل می‌کنه:
▫️
رفع محدودیت ریجن:
بدون نیاز به دستکاری یا تغییر کشور اکانت گوگل
▫️
پشتیبانی کامل:
از Antigravity 2 و Antigravity IDE و ترمینال (CLI)
▫️
امن و خودکار:
اجرای پچ با یک کلیک + بکاپ خودکار برای بازگشت به حالت اول
💡
نحوه استفاده:
ابزار رو اجرا کنید و شماره نسخه مورد نظرتون رو بزنید تا پچ در چند ثانیه اعمال بشه (سازگار با ویندوز، مک و لینوکس).
🌐
دریافت ابزار از گیت‌هاب
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.05K · <a href="https://t.me/ArchiveTell/7747" target="_blank">📅 16:52 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7746">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GXCyeoc-yajIr8o4ddZ-OxcdJmZPwCqJrPbqGdRiTfgKw5lVHsFzC55k1kxAHh4_0XCubkcHwQd0CwJr_RJewQgeAgB5Frx4R_s3JHLt-q99GnIih71dumS8KRGgoemBOu_vViLqeMT8-6RGoimiABxkix4pn9PSentNlyVwplrig0tYhuTLWRAHaTFnbhcf4ZzWu497DtIiqHK_AjGVHGvzOLTBDL1HDfuaP0oPaYuEpjZvr0n-3XCw_lzHB6ZvAnbDCEN3tVSO_jCfdnbA5m5wgqtvjkpLATOg2cE1zAzaiIgoLcLNw1wxDPLupwGUm6Ojf8jBfP0MEOekXy7gnQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎁
نحوه استفاده از Claude Opus 5 و GPT 5.6 Sol
به صورت رایگان
📣
حساب‌های جدید در
Verdent.com
، یک دوره آزمایشی 7 روزه با 100 اعتبار رایگان دریافت می‌کنند
💯
🆓
🎉
✍️
آنچه دریافت می‌کنید:
👀
🔍
☑️
Claude Opus 5 / Sonnet 5
✅
GPT-5.6
☑️
Gemini 3.1 Pro
✅
GLM-5.2
☑️
Kimi K3
📌
نحوه دریافت:
🔥
⚡️
☑️
به
➡️
🔗
https://verdent.ai/
مراجعه کنید.
✔️
برنامه دسکتاپ یا افزونه VS Code را نصب کنید.
☑️
یک حساب کاربری جدید ایجاد کنید
✉️
✅
مدل مورد نظر خود را انتخاب کنید.
☑️
از اعتبارها برای شروع استفاده کنید
🚀
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.03K · <a href="https://t.me/ArchiveTell/7746" target="_blank">📅 11:05 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7744">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">🔥
KiraAI
روزانه ۵۰ میلیون توکن رایگان
🤖
مدل‌های موجود قابل استفاده :
⚡️
kira-3.5-pro
⚡️
kira-3.5-flash
⚡️
kira-3.0-image
🔗
kiraai.vn
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.98K · <a href="https://t.me/ArchiveTell/7744" target="_blank">📅 23:09 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7743">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">🔎
scite.ai
— موتور جست‌وجوی استنادی برای تحقیق جدی
۷ روز اشتراک رایگان (تریال رسمی سایت)
📑
Smart Citations
نشان می‌دهد هر مقاله توسط مقالات دیگر تأیید شده، رد شده یا فقط اشاره شده — نه فقط تعداد استناد
🧠
Assistant
پرسش پژوهشی‌ات را می‌پرسی و پاسخ با استناد واقعی و لینک به منبع می‌دهد، نه حدس
🤖
دسترسی به مدل‌های تحقیقاتی:
Claude Sonnet 5 | Claude Opus 4.6 | GPT 5.2
🎛
Personalized Feed
فیلتر و شخصی‌سازی حوزهٔ تحقیق ، فقط موضوعات مرتبط با کارت را ببین
🔗
Custom Dashboards
داشبورد اختصاصی برای کلیدواژه، نویسنده یا ژورنال خاص + هشدار مقالهٔ جدید
📊
Analyses & Topic Classification
دسته‌بندی موضوعی، شناسایی روندها و گپ‌های پژوهشی
آموزش فعالسازی
🔗
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.91K · <a href="https://t.me/ArchiveTell/7743" target="_blank">📅 22:40 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7742">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bb73WUDGCa7_9wuSHeAqmA5ak01qfArtiW-M0RDsp3iUJRKYYtpYABwEyyeO00nrOS2sJikw7K4rse3gLEpPNNijMNsAW87dL3zCZ_doWq62wBHPNJaH0dLdpoT3QxTJqFLxj-5YOXpcdiL8G65FSR01wRE0i_0YK8bFoM0XILSpSX8aSChmloYuHTRphefWepY2p_dN6qeitQNmKKCwufuYoOfdIRi54JAmWBnsj5HwjAVi37jVolhehXHUEK3Ay_vjSxo8PpZZlvzbTIPWchIE3DcKRoKv01AYoFtd6pUxcAKEWRiIgJ-mgUgQw-mVUe6CaZM2xPMOKwOUVtwidg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">😎
دسترسی به Seedance 2.5 و سایر مدل های تولید ویدیو، عکس و اتوماسیون
آموزش
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.84K · <a href="https://t.me/ArchiveTell/7742" target="_blank">📅 22:31 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7741">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">keys.txt</div>
  <div class="tg-doc-extra">2.7 KB</div>
</div>
<a href="https://t.me/ArchiveTell/7741" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🎁
دریافت 20,000,000 توکن رایگان  claude-fable-5 | claude-sonnet-5 |  deepseek-v4-pro | muse-spark-1.2
✅
وارد ربات زیر بشید و api key رو دریافت کنید  @kiro86bot
💡
سازگار با همه سرویس‌های OpenAI-Compatible
🌐
base url: https://api.xpiki.com/v1
🔥
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.85K · <a href="https://t.me/ArchiveTell/7741" target="_blank">📅 22:17 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7740">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CcZbU1mzyGTBq0fEU4rXw-i8NwNwxa7oytlELM4kWWnLJ-DHVx-CcFWezgEOaIF2cV-tlP9ACVcyVSa-e21ZRs3uIoeyZuiTpj0Xb5mV9L5bjvRnfq7AbeqKC_DzGf64zyzOPituAHbhHVh79OemDbcg3KSWUy5jqLkWKcuDEbGfCPW4refLlP7tagd7rPaRi4gCTU31mLnj6RvJklSWjzthpj44wRxyWKyhzFH5S7LTUEHbP6k33hGA-LosAVqHySt7lnDSr03e8xJ4iyuNb6T7jF7oUlFjn8b18dIA1_Lpg5aPQgKNoYxLNDe4ggaPCEVA0SP-LoMySa-5shySIA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
🎁
دامنه رایگان همیشگی بدون کارت اعتباری!
‏بچه‌ها این
پروژه گیت‌هاب
با نزدیک ۲۰۰ هزار استار، دامنه‌های رایگان دائمی میده که واسه پروژه‌های تستی و سایدپراجکت‌ها کاملاً خوراکتونه.
🚀
‏•
دامنه‌های متنوع:
پسوندهایی مثل
.us.kg
و
.qzz.io
بدون هزینه فعال می‌شن
‏•
کنترل کامل:
دسترسی کامل به
Custom Nameservers
و تنظیمات
Cloudflare
دارید
‏
💬
نحوه استفاده:
کافیه برید به سایت پروژه، اکانت بسازید، دامنه دلخواهتون رو ثبت کنید و نیم‌سِروِرهای کلادفلر رو ست کنید.
‏
🔗
سایت پروژه
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.01K · <a href="https://t.me/ArchiveTell/7740" target="_blank">📅 18:59 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7739">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">⌨️
ترجمه سریع و هوشمند، بدون دردسر!
اگه دنبال یک مترجم ساده و کاربردی هستید که فقط به یک سرویس محدود نباشه، پروژه Translator می‌تونه انتخاب خوبی باشه. این پروژه با پشتیبانی از سرویس‌ها و مدل‌های مختلف ترجمه، امکان ترجمه متن، استفاده از قابلیت‌های صوتی و مدیریت تاریخچه ترجمه‌ها رو در یک محیط مدرن و ساده فراهم می‌کنه.
🤖
قابلیت چت با هوش مصنوعی؛
با استفاده از API Key با مدل‌های هوش مصنوعی گفتگو کنید و پاسخ‌های هوشمند دریافت کنید.
🔑
همچنین امکان استفاده از API Key و ترجمه با سرویس‌های هوش مصنوعی مختلف رو داره.
🌐
نسخه آنلاین:
https://codewave4.github.io/Translator/
🔗
سورس پروژه:
https://github.com/codewave4/Translator
✈️
@ArchiveTell
|
#SHOWCASE</div>
<div class="tg-footer">👁️ 1.75K · <a href="https://t.me/ArchiveTell/7739" target="_blank">📅 18:42 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7738">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/087627b2c4.mp4?token=FdPvC4Txx52uxJMODjQ2vTf0n8m47HNvhr0WfuCwaDfExQzIr4hezOaUdXOkqxwwK_CtfrQZOP3KUl8Em42TIJaMP_LDMdk_CLApTqoA96MjNFNLz0HfbOp3LpUTTKV9B6emE---U7pmzflHV8BobbPMea6A8xKc5JRmDoHLK9qeFo3Q-HGYy5124ADmXNR35SMSyu772HS8v9hZ2twPaTLp9d0VVfFNiAvk35vLED6FLXIkjqEXb6e--Wp8vYV-Yk50U3Rc4UnT-kiCPW9G3meomOt4Sf1KS1aCRhOBxsKZBfI0l6V6mJTuJynMr7l-iAY08zm3kxgGmHvPUK7D5Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/087627b2c4.mp4?token=FdPvC4Txx52uxJMODjQ2vTf0n8m47HNvhr0WfuCwaDfExQzIr4hezOaUdXOkqxwwK_CtfrQZOP3KUl8Em42TIJaMP_LDMdk_CLApTqoA96MjNFNLz0HfbOp3LpUTTKV9B6emE---U7pmzflHV8BobbPMea6A8xKc5JRmDoHLK9qeFo3Q-HGYy5124ADmXNR35SMSyu772HS8v9hZ2twPaTLp9d0VVfFNiAvk35vLED6FLXIkjqEXb6e--Wp8vYV-Yk50U3Rc4UnT-kiCPW9G3meomOt4Sf1KS1aCRhOBxsKZBfI0l6V6mJTuJynMr7l-iAY08zm3kxgGmHvPUK7D5Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏
🎬
ساخت موشن‌گرافیک حرفه‌ای با یه پرامپت!
‏این ابزار هوش مصنوعی کل فرآیند ساخت تیزر تبلیغاتی، از استوری‌بورد تا تدوین صدا و انیمیشن رو خودش انجام میده و خروجی رو با بیت موزیک سینک می‌کنه. خوراک بچه‌هاییه‌ که سریع میخوان خروجی باکیفیت بگیرن.
🔥
‏
⚡️
دسترسی به منابع غنی:
۱۵۷ مدل سناریو، ۲۱۴ استایل بصری و کلی الگوریتم انیمیشن آماده
‏
⚡️
شروع سریع:
کلی تمپلیت آماده‌به‌کار داره که کار رو برای پروژه‌های فوری جلو میندازه
‏
⚡️
عملکرد هوشمند:
کافیه ایده‌تون رو متنی بدید تا در لحظه ویدیو تحویل بده
😎
برای دانلود ابزار تولید ویدیو
اینجا
کلیک کنید.
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.79K · <a href="https://t.me/ArchiveTell/7738" target="_blank">📅 16:02 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7737">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">1.7B token MINIMAX
url:
api.minimax.io/v1
key:
sk-cp-k8fnOYl1xeWGiSNy7qWxNP3Gu-nkuMKLaAFl7ZoCnGiqA2sabKF30eMTQNurXcyGtgGdbM168WEvBhyTOo2WQaE9RoXzVPAyyG3CYwZuybXzDILyBEBc5nk
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.76K · <a href="https://t.me/ArchiveTell/7737" target="_blank">📅 14:09 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7736">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OV5DJ8a8lLM9DWQUuk_j6zZx0DW2QADbmgSF2ZveabrfoDp00RcasKwjGHyPwvUhmcQ6W2XFOVE0jkUkGLfoOSjZCwhEkFFiiDMyU8h-ZemIg0a2fiQpTN-o_T627gqQ0viGuLaRm2LO9cwssjJvyLTighgACze8AhUHRBZWKeVp1v21ytlMlCVLINE9GuXtkJJkZvGRLdiNJR5uF2fAIO216oJ-cKOTo9ud_n7EuNnz_c25-9qCSBhlYS11tLaDP2hJ30izrFPCipzMvxjvOMQ6uwmp9QU5CF2Tfv9B1m0im48UKOJHw2PS2Zcm_tQ6DIlZxg3Ux1SwIC6XgCbdvw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
🔥
مرجع خفن اسکیل‌های ‌Claude Code⁩ و ‌Codex⁩!
‏سایت ‌SkillsMP⁩ یه کاتالوگ تر و تمیز با بیش از ۳۳ هزار اسکیل آماده‌ست که تو کار با هوش مصنوعی کلی جلوتون میندازه.
🤖
‏•
دسته‌بندی جامع:
از برنامه‌نویسی و ماشین‌لرنینگ تا امنیت و کار با ‌API⁩
🔍
‏•
دسترسی سریع:
لینک مستقیم به گیت‌هاب برای هر اسکیل
📂
‏•
کیفیت‌سنجی:
دارای ایندیکاتورهای کیفیت برای انتخاب بهترین ابزارها
⚡️
‏خوراک بچه‌های وایبکودره که بخوان پرقدرت‌تر پروژه‌ها رو ببرن جلو.
🚀
🔗
skillsmp.com
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.9K · <a href="https://t.me/ArchiveTell/7736" target="_blank">📅 14:02 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7735">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">🛡
دیگه ایمیل و پسورد اصلیت رو به هیچ سایتی نده!
حتماً براتون پیش اومده که برای ثبت‌نام در یک سایت مجبور شدید ایمیلتون رو بدید، اما بعد از یه مدت صندوق ایمیلتون پر از پیام‌های تبلیغاتی مزاحم شده یا اون سایت هک شده و رمزهاتون لو رفته!
ابزار جالب
AliasVault
دقیقاً برای حل همین مشکل ساخته شده:
💎
این ابزار براتون چیکار می‌کنه؟
⚡️
ساخت بی‌نهایت ایمیل دائمی:
برخلاف ایمیل‌های موقت که بعد از ۱۰ دقیقه می‌پرن، این ایمیل‌ها
کاملاً دائمی و همیشگی
هستن و برای هر اکانت می‌تونید هر تعداد ایمیل دلخواه که خواستید بسازید!
⚡️
دریافت کد ثبت‌نام داخل خود برنامه:
نیازی نیست برید یه ایمیل دیگه باز کنید؛ ایمیل‌های تایید و کدهای ورود مستقیماً داخل همین برنامه براتون میاد!
⚡️
مچ‌گیری از سایت‌های متخلف:
اگر یه سایت ایمیل شما رو به تبلیغاتچی‌ها بفروشه، دقیقاً می‌فهمید کار کی بوده چون برای هر جا یک ایمیل اختصاصی ساختید.
⚡️
نصب روی گوشی و کامپیوتر:
هم اپلیکیشن برای موبایل داره و هم افزونه برای مرورگر، و خودش پسوردها رو سر جای درست پر می‌کنه.
💬
چرا این ابزار فوق‌العاده‌ست؟
•
ایمیل‌ها هرگز منقضی نمی‌شن:
هر زمان در آینده بخواید وارد سایت بشید یا رمزتون رو بازیابی کنید، پیام‌ها باز هم به همین ایمیل دائمی میاد.
•
سقف تعداد ندارید:
برای ۱۰۰ تا سایت هم می‌تونید ۱۰۰ تا ایمیل مستعار و رمز مجزا بسازید.
•
کاملاً رایگان و امن:
بدون هیچ هزینه‌ای، امنیت و آرامش صندوق ایمیلتون رو تضمین می‌کنه.
🌐
ورود به وب‌سایت AliasVault
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.88K · <a href="https://t.me/ArchiveTell/7735" target="_blank">📅 12:42 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7734">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hEc0i5VREn0_cnL2rULle-4Fn374L6iAi08k1lRbWRhEe7bZC2ms7G4JvWCRHfuSbVp7IOZ0wMYy-qEa_TDJlXqU1VcJ6vOMJU5_AmQdRJs6yFFUhznUzoUTMq-KTsAszdnSjE5tppWITgz6i8XPePjOZ0gh_vTFEGcBEeLehdcBVIPkkm-2PJ7tKgTPymbPmiTrKapnnTrJR3GtxZStEUB3XUGHnUkOKw0r-9TnoRL_V3u8Gp5sie8HDVTjoLrtlQvTGJsFIs4dLE7zalrG3koXXif7UK6EoXVr0j9NEWOcpP6OnfEnlJOq5wB9D2VKZbQx434PFEhRhkoVu8J6TA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یک سایت، ده‌ها مدل و ابزار با اعتبار رایگان روزانه
🎁
💬
Multi AI Chat
GPT، Claude، Gemini، DeepSeek، Grok، Qwen ، Llama
همه در یک چت، با امکان مقایسه جواب‌ها
🎨
تولید و ادیت عکس
تولید تصویر از متن (Flux، Stable Diffusion، Ideogram…)
حذف/تغییر پس‌زمینه، حذف اشیاء و متن از عکس
Face Swap، Upscaler، تبدیل اسکچ به تصویر
ویرایش عکس با دستور متنی + تولید تصویر سه‌بعدی
🎬
ویدیو
تولید ویدیو از متن و از عکس
Face Swap روی ویدیو
خلاصه‌سازی، زیرنویس و ترجمه ویدیوهای یوتیوب
🎵
صوت و موسیقی
ساخت آهنگ (Suno، MusicGen…)، Text-to-Speech با صداهای طبیعی
شبیه‌سازی صدا (Voice Clone)، تبدیل ویس به متن، حذف نویز
✍️
نوشتن و تولید محتوا
تولید محتوا، بازنویسی، خلاصه‌سازی، ترجمه، گرامر
تحقیق کلمه کلیدی و تشخیص محتوای AI
🌐
لینک سایت :
app.1min.ai
🔥
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.85K · <a href="https://t.me/ArchiveTell/7734" target="_blank">📅 12:24 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7733">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">🎁
دریافت 20,000,000 توکن رایگان
claude-fable-5 | claude-sonnet-5 |
deepseek-v4-pro | muse-spark-1.2
✅
وارد ربات زیر بشید و api key رو دریافت کنید
@kiro86bot
💡
سازگار با همه سرویس‌های OpenAI-Compatible
🌐
base url:
https://api.xpiki.com/v1
🔥
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.96K · <a href="https://t.me/ArchiveTell/7733" target="_blank">📅 11:16 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7732">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">🆓
هوش مصنوعی رایگان  — بدون ثبت‌نام
Kimi K2.6 | GPT 5 mini | DeepSeek V3.2
📌
امکانات:
⚡️
چت هوش مصنوعی نامحدود
⚡️
تولید متن و محتوا
⚡️
بدون ایمیل، بدون رمز عبور، بدون کارت بانکی
📌
نحوه استفاده:
🔗
وارد
این سایت
بشید مدل موردنظر را انتخاب کنید و شروع کنید.
🔥
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.01K · <a href="https://t.me/ArchiveTell/7732" target="_blank">📅 23:45 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7731">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SqrCniSN7RdI7CFslsWETrioNaIVQfKFo_K2oHXTm5dntYTJYLaGtQj_QtYW17jsCwrrSbTykH2D6vUsFiZ1WpuzY7puu9XeojtMEIwP_ktguSolr4-DhNwgSXinFu9APC0xK2nZwGgdhn-qsCur7xNvEsnhSPidWGOOETaA0Gn0Ou_P9qzXH6yZzxSGnS8aKefGyXgp0vbxAB3SOkrJEZCiUGzVLiRRF4v57vQokOtSWEoOD1hD8nDIR_mnNgrYoJa2K6XhSetJ0NsEAZ2kUGjoRh0HsBPro3mF3z9O-Npj783TdMYpXGU2CbK3_D9IZCdoVC6ZZ9eEPf1HPr5SJw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🆓
۵۰۰ مگابایت پروکسی رزیدنتیال رایگان (
proxyma1.io
)
یک سرویس پروکسی رزیدنتیال که با ثبت‌نام از طریق تلگرام ۵۰۰ مگابایت ترافیک رایگان می‌دهد و API هم دارد.
📌
نحوه دریافت:
1️⃣
وارد سایت
proxyma1.io
شوید و ثبت‌نام کنید
2️⃣
پس از ثبت‌نام، یک پیام برای استارت ربات تلگرام نمایش داده می‌شود که داخل آن یک کد هدیه قرار دارد
3️⃣
ربات را استارت بزنید و کد را برای ربات ارسال کنید
4️⃣
۵۰۰ مگابایت به حسابتان اضافه می‌شود
🚀
📌
ویژگی‌ها:
☑️
پروکسی رزیدنتیال (Residential)
☑️
۵۰۰ مگابایت ترافیک رایگان
☑️
پشتیبانی از API
☑️
ثبت‌نام آسان با تلگرام
🔥
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.9K · <a href="https://t.me/ArchiveTell/7731" target="_blank">📅 23:35 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7730">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dKkhnJh7DFe9B2st2JrBV8ELtEyrT7TS6Q8jHWXn0Wt39Oy6nZq81cWizl_5jfs2JW6v5URkEBVBXQiBTJliOdpA_9zkggEPBLvxafix3vGLmulqUUws2lHjg8hpfeCMbpULZsaoRy5x-uvScSPboHTwYHatgWQ1iiau8u6nEyGk6dcpt5FWsWzqTOJrOrhuvwcNxNlweffe7VJoVMpcU9VJKsuMVjVjf-DvZLIaSpQdItAKkj5aL_inG8ZOKTagUDjMTkF9UpMnkJfcSItfysh63BHFbp9BkxKXG9T_xVhK2IgIODuXgcG76NG3cx6sL2Kib-odoRPvbEjMGnh5WQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚡️
۵۰۰۰ اعتبار رایگان برای مدل‌های برتر هوش مصنوعی
پلتفرم جدید در شروع کار ۵۰۰۰ اعتبار به شما هدیه می‌دهد تا با قدرتمندترین شبکه‌های عصبی کار کنید: تولید متن، عکس و ویدیو در یک جا.
📌
امکانات در دسترس:
☑️
چت چندمدلی
☑️
تولید تصویر
☑️
تولید ویدیو
☑️
موجودی اولیه: ۵۰۰۰ اعتبار رایگان
🪙
📌
روش دریافت:
1️⃣
ورود به
getunikey.ai
2️⃣
ثبت‌نام یک حساب کاربری جدید
3️⃣
ایجاد کلید API در تنظیمات پنل
4️⃣
استفاده در رابط چت یا ابزار های واسط
base url:
https://getunikey.ai/v1
🔥
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.79K · <a href="https://t.me/ArchiveTell/7730" target="_blank">📅 23:08 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7729">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">🔍
Hidden File Hunter — شکارچی فایل‌های مخفی ویندوز
دنبال فایل‌های مخفی و سیستمی توی ویندوز می‌گردی ولی پیدا کردنشون واقعاً دردسره؟ این ابزار دقیقاً برای همین ساخته شده
👇
؛ Hidden File Hunter یک برنامهٔ دسکتاپ ویندوزیه که تمام فایل‌های مخفی و سیستمی درایوهات رو پیدا می‌کنه و توی یه جدول مرتب و قابل مرور نشونت میده.
✨
امکانات:
✔️
پیدا کردن تمام فایل‌های مخفی و سیستمی در همهٔ درایوها
✔️
نمایش نتایج در یک جدول مرتب و خوانا
✔️
خروجی گرفتن از فهرست کامل مسیرها در قالب فایل TXT
✔️
کپی کردن خود فایل‌ها با حفظ ساختار پوشه‌ها در مقصد دلخواهت
✔️
فقط می‌خونه و کپی می‌کنه — هیچ فایلی رو تغییر نمیده، حذف نمی‌کنه و بهش دست نمی‌زنه
✔️
ساخته‌شده با Python و PySide6
✔️
تم تیره و روشن
✔️
رابط دوزبانهٔ فارسی و انگلیسی
یه ابزار ساده، سریع و امن برای وقتی که می‌خوای بدونی توی سیستمت چه چیزهایی از چشم‌ها پنهان مونده.
🔗
لینک گیت‌هاب:
github
✈️
@ArchiveTell
|
#SHOWCASE</div>
<div class="tg-footer">👁️ 1.74K · <a href="https://t.me/ArchiveTell/7729" target="_blank">📅 22:37 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7727">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">🚀
اپلیکیشن Bifrost (بایفراست)؛ پل ارتباطی فوق‌سبک تلگرام بر بستر ورکر کلادفلر منتشر شد.
بایفراست یک بریج لوکال (Local SOCKS5) مدرن و بهینه برای اندروید است که ترافیک تلگرام رسمی را از طریق پروتکل TWP به ورکر رایگان کلادفلر متصل می‌کند؛ با پینگ پایین، بدون قطعی و با سرعت دانلود فوق‌العاده بالا.
🔒
بدون نیاز به VPN، بدون روت و با مصرف باتری نزدیک به صفر:
این پروژه کاملاً متن‌باز (Open-Source) است و برخلاف فیلترشکن‌ها از VpnService استفاده نمی‌کند (هیچ علامت کلیدی بالای صفحه نمایش داده نمی‌شود و اینترنت سایر برنامه‌ها کاملاً دست‌نخورده و بدون تغییر باقی می‌ماند). مصرف پردازنده در زمان عدم استفاده دقیقاً ۰.۰٪ است و امنیت و رمزنگاری پیش‌فرض تلگرام (MTProto) نیز کاملاً حفظ می‌شود.
📥
دانلود و نصب برنامه (از گیت‌هاب):
https://github.com/Qorvhex/Bifrost/releases
⚡️
کانفیگ تستی برای شروع (بعد از نصب، کپی کنید و داخل برنامه Paste کنید):
twp://telp.qorvhe-x.workers.dev?clean_ip=1music.cc#Bifrost-Test
🛠
سورس‌کد اسکریپت ورکر (TWP):
https://github.com/Qorvhex/TWP
📁
لینک پروژه و سورس‌کد در گیت‌هاب:
https://github.com/Qorvhex/Bifrost
لطفاً تستش کنید و سرعت و عملکردش رو بهم بگید!
✈️
@ArchiveTell
|
#SHOWCASE</div>
<div class="tg-footer">👁️ 1.73K · <a href="https://t.me/ArchiveTell/7727" target="_blank">📅 21:16 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7726">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">🖥
مرورگر ضد ردیابی Private Browser Pro؛ هویت جعلی و دور زدن بن شدن اکانت‌ها!
​بچه‌ها اگه نیاز دارید روی یک سایت چند اکانت مجزا بسازید بدون اینکه سیستم‌های امنیتی بفهمن همه‌شون مال یک نفره، یا می‌خواید ردپای دیجیتالی‌تون رو کامل مخفی کنید، این مرورگر اوپن‌سورس ویندوزی دقیقاً همون چیزیه که دنبالشید. این ابزار بر پایه نسخه فوق‌امن Ungoogled Chromium و Electron ساخته شده و از زبان فارسی هم پشتیبانی می‌کنه.
​
🎭
جعل مشخصات سیستم (فینگرپرینت):
شبیه‌سازی کارت‌های گرافیک قدرتمند (مثل RTX 4090، سری RX 7900 و تراشه‌های اپل)، اضافه کردن نویز به Canvas و AudioContext و هماهنگ‌سازی هدرها برای عبور آسان از سد کپچاهای Cloudflare Turnstile، hCaptcha و reCAPTCHA
​
📁
مدیریت و تفکیک کامل پروفایل‌ها:
امکان ساخت محیط‌های دائمی (Persistent) برای ذخیره دیتای هر اکانت در پوشه جداگانه، یا حالت موقت و یک‌بارمصرف (Ephemeral) که با بستن پنجره کل ردپا پاک میشه + دکمه پاک‌سازی آنی
​
✅
پروکسی پیشرفته و ضد نشت اطلاعات:
پشتیبانی از پروکسی‌های SOCKS5 و HTTP (با یوزرنیم و پسورد)، حل آدرس‌ها از داخل پروکسی جهت جلوگیری از DNS Leak و غیرفعال‌سازی WebRTC برای مخفی ماندن کامل IP واقعی
​
✨
محیط کاربری تمیز و دو زبانه:
کرومیوم دست‌نخورده بدون واترمارک‌های تستی، تم دارک با کلیدهای میانبر سریع و پشتیبانی کامل از منوی فارسی و انگلیسی
​
💡
بهترین سناریوی استفاده:
ایده‌آل برای مدیریت چند اکانت در شبکه‌های اجتماعی و پلتفرم‌های حساس، تست وب، ریسرچ‌های OSINT و حفظ حریم خصوصی بدون نیاز به خرید اشتراک‌های گران‌قیمت مرورگرهای ضد ردیابی.
​
🔗
گیت‌هاب
​
✈️
@ArchiveTell
|
#SHOWCASE</div>
<div class="tg-footer">👁️ 1.63K · <a href="https://t.me/ArchiveTell/7726" target="_blank">📅 21:04 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7725">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">📥
تبدیل فایل‌های تلگرام به لینک مستقیم نیم‌بها با ربات Leecher!
بچه‌ها اگه کندی دانلود از تلگرام یا قطعی فیلترشکن موقع دریافت فایل‌های حجیم کلافتون کرده، یا می‌خواید تورنت و ویدیوهای یوتیوب رو مستقیم به فایل تلگرامی تبدیل کنید، این ربات لیچر ایرانی حسابی به کارتون میاد.
🇮🇷
لینک مستقیم با ترافیک نیم‌بها:
تبدیل آنی فایل‌های تلگرام به لینک دانلود پرسرعت تحت وب (سازگار با دانلود منیجرها) با محاسبه مصرف اینترنت به‌صورت نیم‌بها
🌐
دانلودر همه‌کاره (لینک به فایل):
پشتیبانی از دانلود مستقیم لینک‌های یوتیوب، اینستاگرام، وب‌سایت‌ها و حتی فایل‌های تورنت و تحویل فایل داخل چت
☁️
اتصال ابری به گوگل درایو:
امکان لینک کردن اکانت شخصی Google Drive برای ذخیره و آپلود مستقیم فایل‌ها در فضای ابری بدون مصرف حجم گوشی
🎁
شارژ رایگان روزانه:
۱ گیگابایت حجم رایگان در هر ۲۴ ساعت بدون نیاز به پرداخت هزینه یا خرید اشتراک
💡
نکته کاربردی:
لینک‌های ایجادشده بین ۶ تا ۸ ساعت معتبر هستند؛ کافیه فایل رو به ربات بفرستید، لینک مستقیم سرور ایران رو داخل IDM کپی کنید و با حداکثر پهنای باند خط‌تون دانلود کنید.
🔗
استارت ربات
✈️
@ArchiveTell
|
#SHOWCASE</div>
<div class="tg-footer">👁️ 1.69K · <a href="https://t.me/ArchiveTell/7725" target="_blank">📅 20:59 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7723">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aWzonDykuvORZJIntf2LDlxnsghcPWZkjKOghwpHzFjEw45ClALCfs5CVyIy_WRqWuiiZnSa0NNSfLac8pADErXmAS8J75l34IfxAO5wGZ3tq2QbIQycw1Gi1Jy1RJoDVQieKJ5sj6GjaNiNsDdrTXMIHtIChsRARkz8yQvL9Xq9TJ_Tt_8meFo7bBdGzQ1ddusc5SNRpH1SvzB__C6xDzdGOeymiUsQts7nsOY9p9Qu6MiQySreEEB20TySzT-9D911RHRC2l0eGDF4h5ttrNiP_EPPV7fa5G00ouYDbyU1dyciKolQuajKCFj0OqI-V8JksawSXsT2c7wN5h-2Uw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نسخه جدید (1.8.0) برنامه MSN-GUARD منتشر شد :
💢
BOOM
💢
تغییرات :
1- اضافه شدن متد اختصاصی SHARD برای اولین بار
-_-_-_-_-_-_-_-
2- دسترس‌پذیری کامل و پشتیبانی 100% از صفحه‌خوان TalkBack برای عزیزان نابینا و کم‌بینا برای اولین بار
-_-_-_-_-_-_-_-
3- آپدیت هسته
-_-_-_-_-_-_-_-
4- اضافه کردن قابلیت Backup و Restore و Reset Factory از تنظیمات برنامه
-_-_-_-_-_-_-_-
5- برطرف شدن مشکل دکمه Reconnect در نوتیفیکیشن
-_-_-_-_-_-_-_-
6- اضافه شدن Theme کاملا روشن برای استفاده زیر آفتاب
-_-_-_-_-_-_-_-
7- برطرف شدن باگ اتصال خودکار پس از قطعی اینترنت و چند باگ دیگر
-_-_-_-_-_-_-_-
6 روش دسترسی به اینترنت آزاد:
1: متد Masque
2- متد Wireguard
3- متد Warp On Warp
4- متد Psiphon (اختصاصی و اولین)
💯
5- متد Tor (اختصاصی و اولین)
💯
6- متد SHARD (اختصاصی و اولین)
💯
💻
ریپازیتوری گیت‌هاب (متن‌باز):
https://github.com/mbm110/MSN-GUARD
📌
لینک مستقیم دانلود :
برای گوشی های 64 بیت
برای گوشی های  32 بیت
برای تمامی گوشی ها
✈️
@ArchiveTell
|
#SHOWCASE</div>
<div class="tg-footer">👁️ 1.64K · <a href="https://t.me/ArchiveTell/7723" target="_blank">📅 18:35 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7722">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">✉️
؛ Turbo Mail ایمیل موقت، سریع و بدون دردسر
اگه برای ثبت‌نام یا دریافت کد تأیید به یه ایمیل موقت نیاز دارید، Turbo Mail یه گزینه ساده و سریع برای شماست.
⚡️
ساخت فوری ایمیل موقت
👌
بدون نیاز به لاگین و ثبت‌نام
⏳
اعتبار ۲۴ ساعته
🔒
مناسب برای دریافت ایمیل و کدهای تأیید
🚀
ساده، سریع و بدون مراحل اضافی
کافیه وارد سایت بشید، ایمیل موقتتون رو بسازید و استفاده کنید.
🔗
https://mail.turbocenter.shop
✈️
@ArchiveTell
|
#SHOWCASE</div>
<div class="tg-footer">👁️ 1.62K · <a href="https://t.me/ArchiveTell/7722" target="_blank">📅 18:12 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7721">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">🎧
دستیار هوشمند و همه‌کاره موزیک‌بازها؛ دانلود با کیفیت FLAC با ربات MelodyAddict!
بچه‌ها اگه عشق موسیقی هستید و از دانلود تک‌به‌تک آهنگ‌ها، افت کیفیت یا پیدا نکردن موزیک پس‌زمینه کلیپ‌ها کلافه شدید، این ربات فوق‌العاده با پشتیبانی کامل از زبان فارسی دقیقاً خوراکتونه. همه‌چیز از شزم اختصاصی گرفته تا رصد خودکار پلی‌لیست‌ها رو براتون یکجا جمع کرده.
🔄
سینک خودکار پلی‌لیست‌ها:
زیر نظر گرفتن لایک‌ها و پلی‌لیست‌های Spotify، SoundCloud، YouTube Music و Apple Music و ارسال خودکار ترک‌های جدید با امکان زمان‌بندی ارسال (۳ ساعته، روزانه یا هفتگی با دستور /digest)
🔍
شناسایی جادویی آهنگ:
پیدا کردن نام و فایل موزیک فقط با فرستادن یک وویس کوتاه، زمزمه، فایل ویدیویی یا لینک ریلز اینستاگرام، تیک‌تاک، یوتیوب و توییتر
💎
کیفیت استودیویی FLAC و Lossless:
قابلیت تنظیم کیفیت پیش‌فرض خروجی برای گوش دادن به بالاترین بیت‌ریت ممکن، با سرعت عالی و کاملاً بدون تبلیغات
📂
مدیریت پلی‌لیست‌های ابری:
امکان دسته‌بندی، ساخت و اشتراک‌گذاری مستقیم پلی‌لیست‌های شخصی داخل تلگرام
💡
نحوه استفاده:
ربات رو استارت کنید، زبون رو روی فارسی بذارید و برای شروع کافیه وویس یک آهنگ یا لینک پلی‌لیست موردعلاقتون از اسپاتیفای یا ساندکلاد رو براش بفرستید تا بقیه کارها رو خودش اتوماتیک انجام بده.
🔗
استارت ربات هوشمند
✈️
@ArchiveTell
|
#SHOWCASE</div>
<div class="tg-footer">👁️ 1.68K · <a href="https://t.me/ArchiveTell/7721" target="_blank">📅 16:52 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7720">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/YPE6mdgIB17czJudAEG8jsAC7Uim34OIxZ4Q3sv6EtPgim4y0UTv4_51qySGiXtpvOe_AhreErNbclNKoLNcNlnG-fg_KatJCCGs5VTEz5RNfiX4_jQciG1-DU6TJ6UhDtJVoLnBoLH6r20MC5pUmF1_aYB1AYqzMCK9UVgcHlohKDj22EYMem1iYJDCZw6n3ajCMiO4C_WJUXEciN00wihPY1bQaq4xeVuSZM9BDg0VmVzzmgXsoM_Ic2Y-wrKGNNZQ_rQcOXpmLO6ko5Q6ckHLo8Yms9nM4NPMmGEMy_Ds1Vd4NWH4lbd3T-HE3Ib7RgP3g0DV4c-i6En2INxmNQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚀
آپدیت جدید ArasClient منتشر شد!
نسخه جدید با اضافه شدن بخش Free منتشر شد و از این به بعد این بخش به‌صورت مرتب آپدیت میشه.
📱
؛ ArasClient یک کلاینت سبک و کاربردی برای مدیریت و استفاده از کانفیگ‌هاست که تمرکزش روی سرعت، سادگی و اتصال راحت‌تره.
🆕
اضافه شدن بخش Free
⚡️
آپدیت منظم کانفیگ‌ها
📊
تست و مرتب‌سازی هوشمند سرورها
🔄
انتخاب سریع‌تر سرورهای مناسب
📦
پشتیبانی از نسخه‌های مختلف اندروید
🔗
دانلود نسخه جدید:
https://github.com/ArasTey/ArasClient/releases/download/v1.6.8/ArasClient_1.6.8_arm64-v8a.apk
🔗
سورس پروژه:
https://github.com/ArasTey/ArasClient
💬
نظر، انتقاد یا پیشنهادتون رو کامنت کنید.
✈️
@ArchiveTell
|
#SHOWCASE</div>
<div class="tg-footer">👁️ 1.64K · <a href="https://t.me/ArchiveTell/7720" target="_blank">📅 15:57 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7718">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/py-sZPTJbuCvh29xRs3pwcUI6NHNTzU3QkU96kp2kg63_XBzOO-laQBA0DQUoDBiF-yFd5Ddbc_ZxB05MTTprI5056gsZiLGqH28gRVYTYSvzIscdli9KZiJcB1uS4tfsniNSt10noMOWZsHapQU0zmvW6PO6pwtBG1wTXy-FW--ZVIzfxnfmyfsM0n0YZYd-Rzq3tudFbIETJdfLhpdw6SrykLgbp1yu2pXomVxwkfBzhVraEk9PZzz7r3E5sFdAoEu-FCi8WKhX6MWvvnz4z4BL6IH_EYf5oJpPeKf07mgaBqLCOZdFn6dE2sdgN85RFwv66bpLzhY8XZmJTvh2w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⌨️
اگر می‌خوای شبکه‌های کامپیوتری رو از پایه تا سطح حرفه‌ای یاد بگیری، نت‌داد دقیقاً برای تو ساخته شده.
از مفاهیم بنیادی مثل آدرس‌دهی IP، سوییچینگ، مسیریابی و امنیت گرفته تا شبکه‌های مدرن، همه چیز با پروژه‌های عملی و مثال‌های کاربردی آموزش داده می‌شه.
✔️
۱۰۰٪ پروژه‌محور
✔️
۵۳ درس تخصصی
✔️
۱۴ بخش آموزشی
شروع یادگیری از اینجا:
🔗
https://netdad.vercel.app
✈️
@ArchiveTell
|
#SHOWCASE</div>
<div class="tg-footer">👁️ 1.62K · <a href="https://t.me/ArchiveTell/7718" target="_blank">📅 15:14 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7717">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Dy36agL7qw7z6yOvDpaQT30Cu9QsUsssHsl_968ZfO6wMyNXGvYxhFvlpbtdWjct-QfvT-KHQoEIKJyyaoJ9SGj3fm9bV3m98mR9ibczrQl94s4UQNxFfS2pmAlhknnpRPQkDs37XvDDA_FS5qO4hkgXcddzMgCsPbZeYX0eUtt357qyRZqJ8OO3WtcAUXXDYGpoY3j3vYt1rwuxmMiINM-sN8zvTGuLCbX8KWC06jPkSDf-lum2zokZ3iUaWr9gU22ZVsIRd1WojwQkw4zHwRuATvaoZ4GIsTpRLndlc9ACQGvZAeYd09VtsuVXhVHQ1qnQ7_jj0cJr_v6y__Rhug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">😎
100 میلیون توکن GLM-5.3-Flash با ثبت نام در AutoClaw + ZAI
از تاریخ 14 تا 16 سپتامبر (دوشنبه تا چهارشنبه) 600 میلیون توکن GLM-5.3 و DeepSeek 4.1 بدون نیاز به کارت و همچنین یک کد تخفیف ارائه خواهد شد.
این پیشنهاد در
اینجا
قابل دسترسی است (در حال حاضر شامل ۱۰۰ میلیون توکن می‌شود)
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.79K · <a href="https://t.me/ArchiveTell/7717" target="_blank">📅 14:46 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7716">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QiByWHD2TOydKRkIu01B8hRlmxevgm4L3_MXAMzolX2uLhfUOwB3NxETVYWJBd9rJFJQIoE_onDI-fvlooS661jf0--6YxB90al3HllxaFA9uNyh2OC2vkPUuc0ytIRXpEHwdL9m1cBnnnxVq_7ueditpbHrwZ-FD188W5wbdOR8VfQmpfg3oivvJYq1648OOuCmmY6Fe8HEd5ElGxNML4L5YEH3-U8dCIVxS413IcFdhS4k1oKL_duf_eysP2uqf-JRqTNbOS5SSUHWe_isHmUJa2Hh27_llK1ri6oWkUTD5v-VSE84YLOWZupGibTv_FgWn3Xi1RMK73t0gCceAA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🥁
کیبورد لپ‌تاپت رو به یه درامز حرفه‌ای تبدیل کن
پروژه خفن KeyBeat یه استودیوی درامز تحت وب هست که بدون نیاز به هیچ نصبی، مرورگرت رو به یه ساز واقعی تبدیل می‌کنه
🔥
یه پروژه اوپن‌سورس عالی برای برنامه‌نویس‌ها، آهنگسازها و عشقِ موزیکا
🔗
لینک سورس کد و اجرای مستقیم:
https://github.com/faithsaly5-stack/Keybeat
✈️
@ArchiveTell
| S</div>
<div class="tg-footer">👁️ 1.92K · <a href="https://t.me/ArchiveTell/7716" target="_blank">📅 12:45 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7715">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PenwPTJh3ENi3A7OdD0r_maeuB_X-23PbKP3eUT6IBIc-n9cboLUaj7_NbyWN34DCyT2NCC0EW9lCb3UI30qYO3WLtT7b6CNbM9LGFfHY_FTW68_vhyiKDyzN7mAkqsXYiQYyBZHHaycDosjTF_apc0xwSvMMwcUamYSjZ-0_BMYsMgi8zi2-Xg7t_37785K02uVKAfvvn1ACDwxcTEMn-awwKL5PBBtk1LCvjFN7TvSgPH6LmgPyR5zrbilJDjFf91MT7OTp1Oy20pB1sCfIKbzJJh_bahwlkKsgcOp6_CYolCjnJwPH262jrDmSe8DdWxkQZ__PzPKU7j5G5zf1w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💎
دریافت آیپی رزیندنتال رایگان
💎
با گوگلتون سایت زیر بشید و روی claim offer کلیک کنید.
بعدش برید بخش proxy generator و پرش کنید و بزنین براتون 300 مگ آیپی رزیدنتال میده
🆓
http://rainproxy.io
✈️
@ArchiveTell
| S</div>
<div class="tg-footer">👁️ 2.07K · <a href="https://t.me/ArchiveTell/7715" target="_blank">📅 10:21 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7712">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/t2V-VPKFQ4si2GzKpdeMrxFmGsVzeVlr5t4VEbXEA2yqI883L_D9QBwHx1qCSyMThyIHDWhlH_0N2mTrkpQeWobsywSC0esgvdNF-vWTaaK4hwqo8Myg5B2vaKQiz5U3lLJzD6eacrIpCzqkNSWb0iW7yt4htF3eVnrv1L1Zy93cVUiPEBq1XObNioWHAzbdQ9jrUpw2QQlb9bUL8zj3263l1lVsLK5w3lOvqAxGVer-RWA3Pc1lv9nG_XWVrpgnvkXjWSFd5oafn5gjXUoo2diEoDWx_XR1Wh6IzuEvwOKSzTIEAUI-PEyOVzCibSKaHyrmntfy56foSGLFVpitCA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">😎
15 دلار اعتبار رایگان برای دسترسی به بهترین مدل‌های هوش مصنوعی
استفاده از مرورگر به شما 15 دلار اعتبار می‌دهد تا مدل‌هایی مانند موارد زیر را امتحان کنید:
• GPT-6 Astra
• DeepSeek V4.1 Flash
• GPT-5.6 Luna
• Claude Opus 5
• Grok 4.5
برای دریافت:
🔗
browser-use.com
با استفاده از حساب گوگل خود ثبت نام کنید و شروع به استفاده کنید.
برای دریافت اعتبار بیشتر، از چندین حساب استفاده کنید.
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.08K · <a href="https://t.me/ArchiveTell/7712" target="_blank">📅 21:20 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7711">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">🧰
جعبه‌ابزار همه‌کاره و فوق‌سریع تلگرام؛ معرفی آپدیت بزرگ بات Amir Tools!
بچه‌ها اگه کلافه شدید از اینکه برای هر کار کوچیک (هوش مصنوعی، استعلام قیمت ارز، دانلود یوتیوب و تبدیل فایل) یک ربات جداگانه استارت کنید، این بات همه‌کاره دقیقاً خوراکتونه. در آپدیت جدیدش کلی ابزار مدرن با رابط شیشه‌ای اضافه شده تا از ده‌ها بات متفرقه بی‌نیاز بشید.
🧠
هوش مصنوعی با حافظه اختصاصی:
مکالمه پیوسته بدون فراموشی کانتکست چت، سوئیچ خودکار روی مدل‌های پشتیبان و امکان ریست سشن
📥
فایل به لینک مستقیم و دانلودر یوتیوب:
تبدیل آنی انواع فایل، ویدیو، آهنگ و ویس به لینک مستقیم پرسرعت + دانلود مدیا از یوتیوب با بالاترین کیفیت
📈
نرخ لحظه‌ای و چارت زنده بازار:
استعلام آنی قیمت دلار، تتر و ارزهای دیجیتال (BTC, ETH, TON و...) همراه با نمودار اختصاصی و باکس High & Low
🤫
پیام ناشناس امن و دوطرفه:
ساخت لینک اختصاصی با آیدی تصادفی برای دریافت متن، ویس و عکس ناشناس با قابلیت پاسخ‌گویی مستقیم
🎁
سیستم قرعه‌کشی خودکار کانال:
ساخت مسابقات و چالش‌های گروهی با دکمه شیشه‌ای و قرعه‌کشی کاملاً خودکار و عادلانه بین اعضا
🛠
میکروابزارهای روزمره:
ساخت بارکد تصویری (QR Code)، پسوردساز غیرقابل‌نفوذ، مبدل ارز به تومان، هواشناسی و مینی‌گیم‌های کوئیز
💡
نحوه استفاده:
وارد ربات بشید، دکمه شیشه‌ای منو رو لمس کنید و بدون نیاز به رجیستر یا مراحل طولانی، به تمامی ابزارها به‌صورت یکپارچه و رایگان دسترسی پیدا کنید.
🔗
استارت ربات هوشمند
✈️
@ArchiveTell
|
#SHOWCASE</div>
<div class="tg-footer">👁️ 1.96K · <a href="https://t.me/ArchiveTell/7711" target="_blank">📅 20:52 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7710">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">🚀
دسترسی رایگان به Claude Fable 5 از طریق GitLab!
💻
✨
اگر می‌خواهید به صورت کاملاً رایگان از قدرت مدل هوش مصنوعی Claude برای برنامه‌نویسی، ساخت سیستم‌ها و توسعه پروژه‌های بلندمدت استفاده کنید، گیت‌لب (GitLab) یک فرصت بی‌نظیر ۳۰ روزه برای شما فراهم کرده است.…</div>
<div class="tg-footer">👁️ 2.14K · <a href="https://t.me/ArchiveTell/7710" target="_blank">📅 19:44 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7708">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">😎
دسترسی رایگان به GPT-Image-2.5 Sunburst به مدت 72 ساعت
📝
مراحل: ① به https://arena.ai/ مراجعه کنید. ② حالت Direct Mode را انتخاب کنید. ③ در لیست مدل‌ها، GPT-Image-2.5 Sunburst را پیدا کنید. ④ به مدت 72 ساعت، این مدل به صورت رایگان در دسترس خواهد بود.
✈️
…</div>
<div class="tg-footer">👁️ 2.13K · <a href="https://t.me/ArchiveTell/7708" target="_blank">📅 14:25 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7707">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">175 دلار برای دسترسی به بهترین مدل‌های هوش مصنوعی جهان
💥
🆓
Opus 5 | GPT 5.6 Sol | GLM 5.3 | Opus 4.8 | Deepseek V4 Flash
✅
برای فعال‌سازی فقط کافیه یک اکانت گیت‌هاب قدیمی داشته باشید و از طریق این لینک وارد شید
✅
🎁
با هر رفرال شما 100 دلار و شخص دریافت کننده…</div>
<div class="tg-footer">👁️ 2.21K · <a href="https://t.me/ArchiveTell/7707" target="_blank">📅 12:01 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7706">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lO_7Vt5YCAqoe8baQJRwv_vVT0yLmkLBqIqt5mCyEzL5-ppNnuOU0u2o53ZgLEGyInuyACsxY4bPcUy0PBThXGBog4LXTdAAAO5ip3j6WoP6pwsJKgErJEKv6fy144BkLMEx328oVMfpaXkVE4EXhQKsIYGJft_XxWdvVnc4gE0ouX4KgsT7YAc7nAJXgZ2ZX0DKRHZcIbWbI_hWIpP1ccVYxHq1pOtYizztmcouweC1yS1wbaavhC37I1m8Jsayb5sU5XDpgEYKP0jRHeQjz9LlTIRwpCPkUbNeybkEvLns8fbqsjWJxYKMhNiev8SyTEE2_IvCeejqIyEPj5cCzw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">😎
دسترسی رایگان به GPT-Image-2.5 Sunburst به مدت 72 ساعت
📝
مراحل:
① به
https://arena.ai/
مراجعه کنید.
② حالت
Direct Mode
را انتخاب کنید.
③ در لیست مدل‌ها،
GPT-Image-2.5 Sunburst
را پیدا کنید.
④ به مدت
72 ساعت، این مدل به صورت رایگان در دسترس خواهد بود
.
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.35K · <a href="https://t.me/ArchiveTell/7706" target="_blank">📅 21:31 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7705">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AFXJPnPkGwMdE5GLNLVRZHC0R0uogSXk5edZHXODN4XPSrPzMCU-y_qpzcKLmV304HyodRYsDghgpMESJXuBOKkEWa2KGSOUW9arx9i9ruFN2FYmpb5e0ctw3uHe7OY6d0EeW7Wp8Lws4JcmKOU6AyOlIYEWcYYyYCd4yq7yVwvjTdkX1Jilj6rTkRdIoOy-I3vvRYQB__eaLQxFXtXq9lZvt2hG9FBqoPVG356c8UODYGC6G9WOxRPS8EsgTmqzcgFU4g-rcmykJDI7t3U_btMibPwejBJH8Dlmo-R3qz2_tAOyXW6q9EZG-9s5irHlN_rSFazKwyO6aOuwmWjL3A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مدل DeepSeek V4.1 Flash به صورت رایگان
💥
🆓
این نسخه ۲ روز پیش منتشر شده است. دارای ۱ میلیون توکن متن، قابلیت‌های بصری پیشرفته و کیفیت مناسب برای استفاده در سیستم‌های هوشمند است.
🚀
🔺
رایگان به صورت روزانه
🔺
پنجره متن با ظرفیت ۱ میلیون توکن
🔺
سهم استفاده روزانه هر روز ریست می‌شود.
هنوز مشخص نیست که این سرویس چه مدت به صورت رایگان باقی خواهد ماند.
‼️
🔗
لینک سایت
✈️
@ArchiveTell
|
#API</div>
<div class="tg-footer">👁️ 2.31K · <a href="https://t.me/ArchiveTell/7705" target="_blank">📅 15:37 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7704">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TJZx9fyMbpKXG5rLHyrqJMwgjJpQNX_5ePSRQAIDS1fzNv_PzaVq8HCRqRvgM9DPI_lkCpaSf0LQ-IDlhjd0pi7myDUMW9joKECVxkUR46ZMSSUS8hpMC2Q1W63fqR-mDRBsCyjWYEMnx2dYbXM3J0UuxXUGh0rEjQkKu3YTXpJs4NlYUfvn07FOspdPCL6n3l1aNaA62EfW9uIH4ToYfoJA8Ab1EgF3canSC20EluprrCspm75xdbjdhLpjPCH35uJ6m8ICTqbJOTTeybmtgvKLzpTyrjyuIYg8206AyTJZ8KMFe4EYPOQgr3p9fj-YfOMlv_ePfQ8iqp2NylZK6g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دسترسی به غول های هوش منصوعی به صورت رایگان
💥
🆓
با این سایت میتونید 5 دلار اعتبار رایگان برای بهترین مدل ها دریافت کنید همچنین این سایت 3 مدل کاملا رایگان بهتون میده
💵
😎
Kimi K3 | Deepseek 4 Flash | Mimo 2.5
✅
📌
Base URL: https://tokenharbor.ai/v1  با جیمیل…</div>
<div class="tg-footer">👁️ 2.27K · <a href="https://t.me/ArchiveTell/7704" target="_blank">📅 11:45 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7702">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hNlfN2cFrJyfHdvhxgiR_lNn3qHIrFOJHUGux9kxasvQmCoE6RQlFRg8cX0ngAioRn7tTZl6wU-_EH3oEAOHG-bcGIqnv9Ux4wOwU812-1gyRnaNynD_g5scZ3PlkV82YP1TWskgckFi2OiCe_Ha1iYCrF7t6oZKjklfvc1JgJ0RnAb6LsyVjtPfLDj56-yWrERS4Q5LkP3Z2AY1lbiuJEpRKBN0y9bt8F2ItpKqNQZPdmQ2VgMzpV__JdlEyu13SGo0rRXXb6K4iAsQLLJuJnhkkz8THX_zm59xFz2eAjewAZXnky_fP4czHNipPxO3LiyGIuViz5IfWLJg-GCy-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">GPT-6 Astra
1 Day Free
⚡️
⚡️
https://arena.ai/text/direct?model_a=gpt-6-astra-medium
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.54K · <a href="https://t.me/ArchiveTell/7702" target="_blank">📅 19:14 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7701">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Fdb5YRahjzP8uNDLgtJFahDzAnjZyjdPe8Fn0iXqTbiSgjkwo1RLHnMBDHdJH2vGy0lcSNxs766v_J6twCpVXzcAueNLPDNaWDuYeEPnbDKxtl9sSYX794dewhRPoWcbiO9JqdNm1gd9QavM5tHxrjs6uVmgiKEzpVTXDf38MVrlq509In_wp6j-YOfeYxalOt5Sl6aH_V3IzocTK3IFfwhFNCuCRiDwqGhOVRsxEjShT8CUnurl12hjWLXdLXxHgK6sCDneqsDSMu4Ht1qWMS4YEEE1DeXWe5tHk_uQeuifYmahrYIMtcWzhooevucPmNyVMuNQOX9p92t2kyaecw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">150 میلیون توکن رایگان برای مدل های زیر
💥
🆓
GLM 5.3 Flash | Qwen 3.8 Flash | Mimo 2.5 | GLM 5.3 | Hy 3 | Qwen3.8 27b
✅
وارد سایت زیر بشید با جیمیل ثبت نام کنید سپس از طریق منو 50 میلیون توکن امروز هم دریافت کنید
✅
‼️
نکته :
از مدل های با پسوند Free استفاده کنید و احتمالا این دسترسی شامل محدودیت تعداد ریکوئست در دقیقه باشه ، همچنین ممکن هست هر لحظه اشتراک رایگان بپره
📌
Base URL :
https://kiraai.vn/api/v1
🔗
لینک ثبت نام
🔗
لینک گرفتن کلید
🔗
لینک دیدن مدل ها
✈️
@ArchiveTell
|
#API</div>
<div class="tg-footer">👁️ 2.25K · <a href="https://t.me/ArchiveTell/7701" target="_blank">📅 18:42 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7700">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">🧠
پروژه OXYGPT — یه ربات تلگرامی که هوش مصنوعی رو حسابی جدی گرفته!
بچه‌ها این صرفاً یه ربات چت نیست، یه اکوسیستم کامل AI روی تلگرامه: چند مدل هوش مصنوعی، مربی‌های حرفه‌ای تریدینگ، sandbox واقعی لینوکس، اخبار فارکس زنده و داشبورد مدیریتی. خوراک کسایی که می‌خوان یه بات production-grade بسازن نه یه دمو دو ساعته
🔥
↔
مسیریابی چند-مدلی AI
: استخر کلید Gemini + سرویس‌های سازگار با OpenAI، round-robin می‌چرخن و روی خطای 429/503 خودشون فالبک می‌زنن
🪟
پنجره‌های مکالمه مجزا
: هر کاربر تا ۵ چت جدا با تاریخچه و state خودش می‌تونه باز نگه‌داره
🧙‍♂️
مربی‌های تریدینگ (Persona)
: چهار شخصیت آماده (ICT، Quarterly Theory، Matrix/369، Price Action) با یه دستور سریع صدا زده می‌شن
📓
ژورنال معاملات
: ثبت و پیگیری ترید‌ها با قالب‌های اختصاصی، مستقیم داخل تلگرام
📰
اخبار فارکس زنده
: رویدادهای پرتأثیر Forex Factory رو با تحلیل کوتاه AI نشون میده
🖥️
قابلیت Sandbox واقعی لینوکس (E2B)
: مدل می‌تونه کد اجرا کنه، پکیج نصب کنه، ریپو کلون کنه و فایل بفرسته/بگیره
🔑
قابلیت BYOK
: کلید API خودتو وصل کن، از محدودیت پیام و quota عمومی بی‌نیاز شو
👁
مانیتورینگ کانال با AI
: کانال‌های تلگرام رو زیر نظر می‌گیره و پست‌های مهم رو تحلیل و تحویل میده
💡
دیپلوی با یه دستور روی Docker/Railway انجام میشه، و هر ۵ ساعت یه بک‌آپ خودکار از کل دیتابیس‌ها زیپ و برات تو تلگرام ارسال میشه — دیگه نگران از دست رفتن دیتا نباش.
🔗
گیت‌هاب پروژه
✈️
@ArchiveTell
|
#SHOWCASE</div>
<div class="tg-footer">👁️ 2.09K · <a href="https://t.me/ArchiveTell/7700" target="_blank">📅 17:57 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7698">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">دوستانی که پروژه تمیز دارن و نیاز به دیده شدن دارن بیان دایرکت یا کاملا رایگان باشه یا فریمیوم با کمال میل بدون دریافت هزینه پروژه اشون رو میذاریم اگه کسی رو میشناسین که پروژه اش دنبال دیده شدنه، این پست رو فوروارد کنین براش
❤️‍🔥
✈️
@ArchiveTell | #SHOWCASE</div>
<div class="tg-footer">👁️ 1.86K · <a href="https://t.me/ArchiveTell/7698" target="_blank">📅 17:19 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7697">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/F-ssUus-qhz3Qp8ilneVbF2INyHb6yzSY5fjfuwhyDyvLcRa-x8SONiHUdaXXRZRESAh3Q5Nc0KXhAF_VGoH5e1hV02kVuZGKHRsDPYGoBA8ewle-rWXGqUmvZYV03tDK1oQOQ-mlx6b_6xBoZ1r-tVEUIwFUzAD9p-WHhQiRCT2Gg1gHQCKHf0gdr1IkqY4TSr4SZdbR_f6sATm7qaI6GpwMh6lh_O8yY-fkzlIImCTjwE8fpPo_NAKF5FDMcx5ekeY0yp9iLq2Pr6-XsBrcHDDrBy9NC1n7i6IN-yoNfa2XZmXtqGFCF4l-GjQfdqYOGynx_NvzCYFzZzIRTp0uQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">5 میلیون اعتبار رایگان برای بهترین مدل های هوش مصنوعی
🚀
Opus 5 | GPT 5.6 sol | Sonnet 5 | Kimi k3 | Gemini 3.5 | Opus 4.8 | Grok 4.20 | Gemini 3.1 pro  همچنین دارای چند مدل رایگان :  GLM 5.2 | Deepseek 4 Flash 0731
🤖
|Minimax M3   به این سایت برید یک حساب…</div>
<div class="tg-footer">👁️ 1.85K · <a href="https://t.me/ArchiveTell/7697" target="_blank">📅 16:29 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7696">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">🚀
دسترسی به بهترین مدل‌های هوش مصنوعی به صورت رایگان    Mimo 2.5 Pro | Deepseek 4 Pro | Minimax m2.7 | Mistral Small 4 | Mistral Large 3 | Mistral Medium 3.5
✅
برای فعال‌سازی فقط کافیه یک ایمیل داشته باشید و از طریق لبنو زیر وارد شید و سپس لینک ربات تلگرامی…</div>
<div class="tg-footer">👁️ 1.83K · <a href="https://t.me/ArchiveTell/7696" target="_blank">📅 16:15 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7695">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/W74evXKn0Bmg7SO_LDaV5FOyymTjErchkutixX20gIIwPIq7XhlUbKB_R4FNAQJL49B0dU7_5k5QLyoIgBTdRIvm6kBgh_caN-l8QzXzzUuryErmsv64wQU7LIb34XkMJmhrga0IMmmFhbEsbZqKuKO-0SGQy-yYB_HIqO1lbIEhC7NSLn5cQY33ZUALBtOipXoC0w-ENtMmxcgTpjuK2poUnEEApcsWeSGf6KoEJ_d995iSfwjWGJdmVt_D5n5ITCvSzzlg1eEK5b0gBP0bOQKf9eaS_z6USg0YUH_WS1dcagn88I-XOFvt37vR1R9yrKm0gGVYi3DcjeOrQOq-bg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">روزانه 1 میلیون توکن رایگان برای مدل‌های زیر
💥
🆓
Gemini 3.8 flash | Muse Spark 1.3 |GLM 5.3 Flash | Deepseek V4 Flash | Deepseek V4 Pro | GPT 5.6 Luna | Gemini 3.1 pro
✅
وارد سایت زیر بشید و ثبت نام کنید و یک کلید دریافت کنید
✅
‼️
نکته :
با هر آیپی ۱ بار میشه ثبت نام کرد اگه میخواید چند اکانت بسازید هربار آیپی هارو تعویض کنید
📌
Base URL :
https://apinex.bond/v1
🔗
لینک سایت
🔗
گرفتن کلید
🔗
دیدن مدل ها
✈️
@ArchiveTell
|
#API</div>
<div class="tg-footer">👁️ 2.02K · <a href="https://t.me/ArchiveTell/7695" target="_blank">📅 15:59 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7694">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/J2_wx4Y6bKjKJqbHkVjAlFU90b9lAnhQK_sT1sKq_wV8x_R33x0ZamZ-lLmZs9KKs9I_vNuRBZRawOL4DNOtZuF-aHtubCKbTQKgZPwNAhT448wi5r6ZY3pmX46svn7MB0d4N0cQOKasNpLGapqPHhNG3chDBYmA_-Hy8q-5P9ww0ohEXcIOHwnLkUMunljqpHcyuxWgAKM7MJtBY3kpJSQLAjrAVCtQMuyIV9TQpFgjSom8MhtBH3b8lHJhkCWhEy0saJPbnLJzT2mV6Y28v2xmW8h85BP9Asfz89OADs47y3M9nj1kkiKf9Z2Vn-NLQRylj2jeFmX0g9XYb6qrIQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">100 میلیون توکن رایگان 1 ساله
💥
🆓
Fable 5 | Opus 5 | GPT 5.6 Sol | Grok 4.6 | GLM 5.3 | Qwen 3.8 max | Kimi K3 | Deepseek V4 Pro 0813
✅
برید داخل
این سایت
ثبت نام کنید
حالا برید داخل
این بخش
پلن سالانه رو انتخاب کنید و این کد تخفیف رو بزنید :
DEVWEEK
بعد اینکه تخفیف اعمال شد تایید کنید و تمام ، یک api بگیرید و استفاده کنید
✅
📌
Base URL :
https://codecraftapi.com/v1
اکثر مدل های جهان رو داره میتونید از Playground چک کنید ، چون سایت شلوغی هست طول میکشه تا ریکوئست ها جواب بدن
‼️
✈️
@ArchiveTell
|
#API</div>
<div class="tg-footer">👁️ 2.09K · <a href="https://t.me/ArchiveTell/7694" target="_blank">📅 14:52 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7692">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MJLr8wqv78MfNNOELUVu-P2WxM9KhK4vLs8rV-AZNL6jGzEujJPMw6gUM6HFQJ2Tz40RsoW5KKuaNGjHv0FVyBWP_imdsecOuCEwmJqduQT-Scb92XeTTcLkk8hViSPO51pJXgKRDhSGpBCTJuhpuaFcmDZNPcIb4UpLE9kRvvU-GEBBAIi0HyyfF2UpWyslML578ABzxwMvvthL8auUL5nMrYpkTTyEdAcqR_ZGDUUuUK0dyUSeUD_qH2kWMDDjeFUFo5-0hFtN4XsOGejq4lR_mAFa_D6N5Y3KlRevaQKuXJpC1SfT5HLtB_bXWiqg1RdTd2hB7hHwJh9RBHlmPQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">DEEPSEEK V4.1 رایگان
🙂‍↕️
🔗
alysiscode.com
✅
50 کردیت در هر 30 روز
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.01K · <a href="https://t.me/ArchiveTell/7692" target="_blank">📅 11:14 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7691">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">🎨
غوغای جدید اوپن‌ای‌آی؛ مدل ChatGPT Images 2.5 منتشر شد!
⚡️
۵۰٪ سریع‌تر با جزئیات خیره‌کننده: جهش بزرگ در نمایش طبیعی بافت‌ها، شکست نور و واقع‌گرایی رنگ‌ها در نصف زمان قبل
✏️
قابلیت جادویی Sketch: کشیدن طرح اولیه و ترکیب‌بندی به‌صورت دستی، تا هوش مصنوعی…</div>
<div class="tg-footer">👁️ 2.13K · <a href="https://t.me/ArchiveTell/7691" target="_blank">📅 00:33 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7690">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">دوستانی که پروژه تمیز دارن و نیاز به دیده شدن دارن بیان دایرکت یا کاملا رایگان باشه یا فریمیوم با کمال میل بدون دریافت هزینه پروژه اشون رو میذاریم اگه کسی رو میشناسین که پروژه اش دنبال دیده شدنه، این پست رو فوروارد کنین براش
❤️‍🔥
✈️
@ArchiveTell | #SHOWCASE</div>
<div class="tg-footer">👁️ 1.99K · <a href="https://t.me/ArchiveTell/7690" target="_blank">📅 23:55 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7689">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">✅
تغییر ریجن گوگل در ۳۰ ثانیه
⏱️
با فیلتر شکن کشور مقصد یکم برین تو گوگل بچرخین،
بعد به لینک زیر بروید، ریجن را انتخاب کنید، دلیل تغییر را بنویسید و ارسال کنید.
https://policies.google.com/country-association-form
حداکثر تا ۲ ساعت ریجن به جایی که میخواهید عوض می‌شود و ایمیلش میاد
✅
بعدش میتونین به راحتی از antigravity و سرویس های دیگه گوگل استفاده کنین.
از توجهتان ممنونم
🙏
✈️
@ArchiveTell
|
#method</div>
<div class="tg-footer">👁️ 2.11K · <a href="https://t.me/ArchiveTell/7689" target="_blank">📅 23:38 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7688">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">📌
Model :
gpt-6-astra
📌
Base URL :
https://api.eirouter.ai/openai/v1
sk-e76d452dff7eccef0a1b6bde4f8262c7f628f4f2991676cf3188d0cb68023b3f
sk-778bbaffd07397311260074542e405ab11833bf458e0250363ac1afd7db02297
sk-b028d3f23d96d0b0fc96a24985164437fcaf272276caf33548a664a0df424dc1
sk-1f153c31ccd2448b30c2f56287d5dc8fcc8ddafa579d12a797450321d86e9d29
sk-3334618935b09f67a70938d3379971e3ad350fec1154008d3abbaa07565c00b3
sk-242582ef9fc5e53351eb2fd67178b83033a450a61d048cf66be6aacf98a9e2bc
sk-db726cb7cc5b14160f9d8900455fcd34fd56cbb94f3afac65494a5161eee35b6
sk-7e85fc089be2d58f76c236c8ae1efc6062f68a459bdc9f87bcbe896c2d7307e2
sk-cca857a86f2c62b5d704f2234ed5632f8ef4dfbfcc0da509fe0e021516a0406d
sk-3c3eb497a104328775de0ddb333c7c8d596c20a89e25bbe7e204318f35e2b050
موجودی هر کلید هست 5 دلار ولی نکته اینجاست توی سایت قیمت هر یک میلیون توکن این مدل هست 1 دلار
😁
✈️
@ArchiveTell
|
#API</div>
<div class="tg-footer">👁️ 1.9K · <a href="https://t.me/ArchiveTell/7688" target="_blank">📅 22:55 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7687">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9374b9e092.mp4?token=jlMXJ3lNekgEHu44ZfPbLult95J6pHXSpyq9PN125KGgkh_8vEBZc-ZdfQERvJCSc5ZhgGF6eKdMvM-WpEKVC-lUvHq6XAt5sZUipeRm55rLppESNxL6roIatuUM_UKR2mJ2EYLtccMegSk57LYZ9DWUsXzscVOmkCwErUwpMLZRvjWmmfXro5AFCsuNvxcT7JTkDgW_dIdYjt0F3DHtp1sxfdE3L56KyMsHVX245UJ9GowDw3DQs_7G6hVe1FM6i04HzSzVlk-nwWJzFcpr6CwXha5C5mWVO0675N9kTCiSTuo0H0cKUrSf-kKxxpd9TOXtUT2N1Fz3P_RN43Ys51XKp7f8jZRPYmzuuwFQpR7MXnZYsBJa0oP3Ao0m5bRn7gFUasan6woymOLK_1UQJD8nQ8OwTnmIv0LfKCXFjXfGBBZq06fpBG2vLRuZW-Lzd0YZujPaxSEjkxh2xNrRj_N9SnbUraJJ1jbmkWa5idovuO_eduthS5JMzsHGn7slKxdfYNnsPpM4EtHe7X5u9-J6BO_vUSZ4_I92rdzCjSQgaqwJeRzUUNS4i3qu-QC9AKReduRZO0T0b7VwmziHBQiEG0gouBXT_A3YbRza1ddeg5H1MgrkrZiauo85yq9FYq6ZfXE58M3LP9XgkICzGb6mtE4TneyDXvGI3nhUsS4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9374b9e092.mp4?token=jlMXJ3lNekgEHu44ZfPbLult95J6pHXSpyq9PN125KGgkh_8vEBZc-ZdfQERvJCSc5ZhgGF6eKdMvM-WpEKVC-lUvHq6XAt5sZUipeRm55rLppESNxL6roIatuUM_UKR2mJ2EYLtccMegSk57LYZ9DWUsXzscVOmkCwErUwpMLZRvjWmmfXro5AFCsuNvxcT7JTkDgW_dIdYjt0F3DHtp1sxfdE3L56KyMsHVX245UJ9GowDw3DQs_7G6hVe1FM6i04HzSzVlk-nwWJzFcpr6CwXha5C5mWVO0675N9kTCiSTuo0H0cKUrSf-kKxxpd9TOXtUT2N1Fz3P_RN43Ys51XKp7f8jZRPYmzuuwFQpR7MXnZYsBJa0oP3Ao0m5bRn7gFUasan6woymOLK_1UQJD8nQ8OwTnmIv0LfKCXFjXfGBBZq06fpBG2vLRuZW-Lzd0YZujPaxSEjkxh2xNrRj_N9SnbUraJJ1jbmkWa5idovuO_eduthS5JMzsHGn7slKxdfYNnsPpM4EtHe7X5u9-J6BO_vUSZ4_I92rdzCjSQgaqwJeRzUUNS4i3qu-QC9AKReduRZO0T0b7VwmziHBQiEG0gouBXT_A3YbRza1ddeg5H1MgrkrZiauo85yq9FYq6ZfXE58M3LP9XgkICzGb6mtE4TneyDXvGI3nhUsS4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎨
غوغای جدید اوپن‌ای‌آی؛ مدل ChatGPT Images 2.5 منتشر شد!
⚡️
۵۰٪ سریع‌تر با جزئیات خیره‌کننده:
جهش بزرگ در نمایش طبیعی بافت‌ها، شکست نور و واقع‌گرایی رنگ‌ها در نصف زمان قبل
✏️
قابلیت جادویی Sketch:
کشیدن طرح اولیه و ترکیب‌بندی به‌صورت دستی، تا هوش مصنوعی خودش اونو به آرت نهایی تبدیل کنه
🎯
ادیت موضعی دقیق:
امکان هایلایت و تغییر دادن فقط یک نقطه خاص از عکس، بدون دست‌خوردن بقیه جزئیات تصویر
💡
نکته دسترسی:
تعدادی تمپلیت آماده هم برای تسریع کار اضافه شده و این مدل در حال حاضر به‌صورت عمومی داره برای تمام کاربران فعال میشه؛ حتماً حسابتون رو چک کنید.
🔗
ورود و تست در وب‌سایت
✈️
@ArchiveTell
|
#NEWS</div>
<div class="tg-footer">👁️ 2.07K · <a href="https://t.me/ArchiveTell/7687" target="_blank">📅 22:34 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7686">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">⭐️
۶ پلتفرم برای تست رایگان GPT-6 Astra
دسترسی مستقیم و استفاده از API مدل‌های پرچمدار و سنگینی مثل GPT-6 Astra معمولاً هزینه بالایی داره و اگه حواستون نباشه خیلی سریع اعتبارتون رو صفر می‌کنه!
💸
با این حال، یه سری پلتفرم کاربردی وجود دارند که اعتبار (Credit) اولیه یا سهمیه تست رایگان می‌دن تا بدون نیاز به پرداخت، بتونید قدرت این مدل رو توی چت، کدنویسی، پردازش تصویر یا ساخت ایجنت بسنجید:
1⃣
پلتفرم Vercel AI Gateway
یکی از مطمئن‌ترین گزینه‌ها به‌خصوص برای دولوپرها. این سرویس هر ۳۰ روز حدود
۵ دلار کردیت AI رایگان
به کاربرانی که حساب فعال دارند میده. محیط Playground، پشتیبانی از ایجنت‌ها و سازگاری کامل با فرمت OpenAI API داره و برای ادغام با پروژه‌های شخصی عالیه.
2⃣
پلتفرم Brainbase
اگر دنبال کدنویسی پیشرفته، تحلیل ریپوزیتوری و ایجنت‌های خودکار هستید، اینجا فوق‌العاده‌ست. بعد از ثبت‌نام اولیه،
۲۵ دلار کردیت رایگان بدون نیاز به کارت اعتباری
دریافت می‌کنید تا بتونید تسک‌های سنگین برنامه‌نویسی و اتوماسیون رو با مدل پیش ببرید.
3⃣
ابزار Roboflow Playground
بهترین جا برای محک زدن قابلیت‌های بینایی ماشین و پردازش تصویر (Vision). توی این محیط می‌تونید اسکرین‌شات‌ها، نمودارها و تصاویر پیچیده رو بدون نیاز به کلید API آپلود کنید و دقت تحلیل مدل رو با بقیه ابزارها مقایسه کنید.
4⃣
سرویس CometAPI
اگه مدل رو برای اتصال به ربات تلگرام، افزونه یا اپلیکیشن خودتون می‌خواید، این سرویس کار رو راحت کرده. بعد از ثبت‌نام کردیت رایگان میده و چون ساختارش دقیقاً مشابه API استاندارد اوپن‌ای‌آی هست، بدون تغییرات عجیب غریب توی زیرساخت کارتون راه می‌افته.
5⃣
پلتفرم Imaginode
یک فضای همه‌فن‌حریف با محیط تعاملی Canvas، چت، API و ادغام با پروتکل‌های MCP. بدون کارت بانکی کردیت اولیه میده و هر پیام با این مدل حدود ۱۲ کردیت مصرف می‌کنه؛ بنابراین برای ساخت سناریوهای متصل‌کننده متن، تصویر و اتوماسیون حسابی جوابه.
6⃣
سایت Vibany
ساده‌ترین و دم‌دستی‌ترین راه برای تست تفریحی و سریع. در بدو ورود حدود ۳۰۰ کردیت رایگان می‌گیرید و هر بار اجرای مدل حدود ۱۰۰ کردیت کم می‌کنه. یعنی حداقل ۳ الی ۴ تا پرامپت عمیق و جدی می‌تونید بهش بدید تا خروجی رو با مدل‌های قبلی مقایسه کنید.
✈️
@ArchiveTell
|
#AI
#API</div>
<div class="tg-footer">👁️ 2.13K · <a href="https://t.me/ArchiveTell/7686" target="_blank">📅 16:50 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7685">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">🧠
شیائومی وارد میدان ایجنت‌ها شد؛ معرفی دستیار همه‌کاره MiMo Desktop!
بچه‌ها شیائومی رسماً وارد قلمرو ایجنت‌های سیستمی شده و یه دستیار دسکتاپی معرفی کرده که مثل ترکیب Codex و قابلیت‌های کنترل کامپیوتر Claude عمل می‌کنه؛ این ابزار خوراک خودکارسازی کارهای روزمره شماست.
🖥
کنترل کامل دسکتاپ و وب:
اجرای خودکار تسک‌ها، کلیک، تایپ، کار با فایل‌ها، پر کردن فرم‌ها و امکان ضبط و اجرای مجدد فعالیت‌ها (Record & Replay)
⚡️
پیش‌نمایش تعاملی و ادیت موضعی:
رندر زنده سایت‌ها، گیم‌ها و داشبوردها با قابلیت هایلایت کردن یک بخش و بازنویسیِ انحصاری همان قسمت
🧠
دسترسی رایگان به مدل‌های نسل بعد:
بهره‌مندی تسترها از دو مدل معرفی‌نشده و پرچم‌دار MiMo-X-Pro-Preview و MiMo-X-Flash-Preview
💾
کشینگ فوق‌سریع تا ۹۹٪:
فناوری بهینه‌سازی توکن برای تغییرات مداوم پروژه‌ها جهت جلوگیری از هزینه‌های اضافی
💡
نحوه ثبت‌نام در نسخه بتا:
ظرفیت بتا کاملاً محدوده و اولویت با کاربران فعال اکوسیستم MiMo Open Platform خواهد بود؛ فرم درخواست رو پر کنید تا لینک دسترسی و مدل‌های جدید زودتر براتون فعال بشه.
🔗
فرم ثبت‌نام در نسخه بتا
🔗
صفحه رسمی معرفی
🔗
صفحه رسمی قابلیت ها
✈️
@ArchiveTell
|
#NEWS</div>
<div class="tg-footer">👁️ 1.82K · <a href="https://t.me/ArchiveTell/7685" target="_blank">📅 16:23 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7684">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2fc89182f1.mp4?token=Ad817uswo53HhEnu-HheY1CH3vQppYLgHgr8VlNJVaGjvWH7HD-PSkccFwQ2-bSfLZTKGt4pcc8vFqGsXfZ-Eujb2k2P_lYTuTDbgOeNp6it5nKwhj2mt5iacjjYxrNt4JyJxGi-bKH1al-zysS-uB-2OAo7tLWz_WJlY7yDqYqswoPipUmgy6Mk-JDfCJbknjagCX1YTfmm4p2pHM-m5K1w7QwEOSXf1muaMH6zWkQp2hKjAPwGaUENbXcat0u-ICRzFkHnRqxKu7V7PYneoaE84mxpT0lgqra9M9cEtdzZACk6vGajbTQRYmJAS_rqQs0S8SR24-lDKdrXTcCVvblBDgFpqrD0_WceF1b8f-w_C8ZAbD_1kEWwQr94EExHqWqDTF46woKnx05MAKm2KR96XvX-wduykNAgm5khe74k2YrPMFKj183BldYkqzBMMzAQSCZB3og4yDOc5ai7LM0SzL8Umiyf6HFBtnBY4w8iZ5fh5y_x983D76iGU4jUwofPjexWP-n9xqUOdaZR50KOSWkvqFtmOXs77HXE57grHBKOVhvW0jK-skb0A4fobYb2GUvm1NxGJO-VeDR0OzC_NYN12-HgzsGQZltqIlwlcEZXv-5avURxjl33YV8Ykqfblfiy4iPvQS6QEatGCQ9a9I_-oYslxC50Q-G9E4c" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2fc89182f1.mp4?token=Ad817uswo53HhEnu-HheY1CH3vQppYLgHgr8VlNJVaGjvWH7HD-PSkccFwQ2-bSfLZTKGt4pcc8vFqGsXfZ-Eujb2k2P_lYTuTDbgOeNp6it5nKwhj2mt5iacjjYxrNt4JyJxGi-bKH1al-zysS-uB-2OAo7tLWz_WJlY7yDqYqswoPipUmgy6Mk-JDfCJbknjagCX1YTfmm4p2pHM-m5K1w7QwEOSXf1muaMH6zWkQp2hKjAPwGaUENbXcat0u-ICRzFkHnRqxKu7V7PYneoaE84mxpT0lgqra9M9cEtdzZACk6vGajbTQRYmJAS_rqQs0S8SR24-lDKdrXTcCVvblBDgFpqrD0_WceF1b8f-w_C8ZAbD_1kEWwQr94EExHqWqDTF46woKnx05MAKm2KR96XvX-wduykNAgm5khe74k2YrPMFKj183BldYkqzBMMzAQSCZB3og4yDOc5ai7LM0SzL8Umiyf6HFBtnBY4w8iZ5fh5y_x983D76iGU4jUwofPjexWP-n9xqUOdaZR50KOSWkvqFtmOXs77HXE57grHBKOVhvW0jK-skb0A4fobYb2GUvm1NxGJO-VeDR0OzC_NYN12-HgzsGQZltqIlwlcEZXv-5avURxjl33YV8Ykqfblfiy4iPvQS6QEatGCQ9a9I_-oYslxC50Q-G9E4c" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎬
آرشیو ۱۵۰ پرامپت آماده برای خلق ویدیوهای سینمایی با AI!
بچه‌ها اگه با هوش مصنوعی ویدیو می‌سازید ولی خروجی‌ها تخت و مصنوعی میشن، این کالکشن خفن خوراکتونه. یه دیتابیس آماده از ۱۵۰ پرامپت تست‌شده که دقیقاً دستور زبان کارگردانی و سینمایی رو به مدل تزریق می‌کنه.
🎥
کنترل دقیق نور و دوربین:
پرامپت‌های تخصصی برای مدیریت لنز، زوایای حرکت دوربین، نورپردازی و دکوپاژ
🎞
همراه با نمونه ویدیویی:
هر دستور شامل پیش‌نمایش رندر واقعی است تا قبل از خرج توکن، خروجی کار رو ببینید
🎭
تنوع ژانر و اتمسفر:
پوشش کامل انواع سبک‌ها، سناریوها، اکت کاراکترها و فضاسازی‌های سینمایی
💡
نکته استفاده:
تمام پرامپت‌ها آماده Copy/Paste هستند؛ فقط کافیه کپی‌شون کنید داخل ابزارهایی مثل Runway ،Kling یا Luma و المان‌ها یا کاراکتر مدنظرتون رو با کلمات کلیدی دلخواه جایگزین کنید.
🔗
لینک سایت
✈️
@ArchiveTell
|
#TOOLS</div>
<div class="tg-footer">👁️ 1.8K · <a href="https://t.me/ArchiveTell/7684" target="_blank">📅 15:02 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7683">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sjW80VEbKEV5RUN5ZewTPvX-Vw5XmJCONAT5Nfwdd3LQhSch2QqY8AfA4JQT92I2uK5r9ba2c6phgWVl0qwinEGm5GIpvZi1Lmi9ALjG1MyLXG0uS_WNGpABT5vh85P0m-t7WDoYYyUwDSs0Qf8wRxFgK1N8mRve8KcEvfmMmnsLAwy5bIxE07BKo13anLR52gPBMN9pYCRZe9nbg-7PwLNmwdm1tLeg6OT6vcanHKbOkjrQEBxHc8-ST4vkteXe7QDUw1dc7CV0lbfU6TVQtmpkFwTfVZxzA6VBkCmSVPMxx-R0qGySfxZLSQWKkBHR4OstzPmBM5sxEtK0uO629A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
مایکروسافت آفیس رسماً مرخص شد؛ معرفی غول اوپن‌سورس GenOffice!
بچه‌ها اگه از خرید لایسنس آفیس یا برنامه‌های سنگین خسته شدید، این پروژه جدید خوراکتونه. یک جایگزین کاملاً رایگان و متن‌باز برای مایکروسافت آفیس که ایجنت‌های هوش مصنوعی رو مستقیماً آورده داخل اسناد، جداول و ارائه‌هاتون.
📝
پکیج کامل و همه‌کاره:
مدیریت بی‌دردسر داکیومنت‌ها، شیت‌های آماری، ساخت اسلاید و کار با PDF بدون نیاز به ابزارهای متفرقه
🤖
ایجنت‌های تحلیل‌گر:
اتصال مستقیم به مدل‌های قدرتمندی مثل DeepSeek ،Claude و Kimi برای تحلیل داده، نگارش متن و تولید محتوا
💻
آزاد و مولتی‌پلتفرم:
پشتیبانی رسمی و نیتیو از مک، ویندوز و لینوکس بدون نیاز به پرداخت حتی یک ریال
💡
نکته جالب توسعه:
جالبه بدونید نسخه اولیه این پروژه رو فقط یک مهندس، توی مدت یک هفته و با سوزوندن ۱۰ هزار دلار توکن هوش مصنوعی جمع کرده! ریپو تازه پابلیک شده و سرعت استقبال ازش وحشتناک بالاست.
🔗
گیت‌هاب GenOffice
✈️
@ArchiveTell
|
#TOOLS</div>
<div class="tg-footer">👁️ 1.91K · <a href="https://t.me/ArchiveTell/7683" target="_blank">📅 14:53 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7682">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e226c05d7f.mp4?token=Iyx-vT0jcSXeMqsxzkVqHB3qSqHSpJSu8hmrLMVuJRP4guy6v8MDBlbH8sp97E2bhIYPamoodatx1KuLLnf20IUk8bYyElZN3XArNIfRUPwNRJrVYJ6d_lZP5OyfKHHBDViMIduyX4B7B1YvgsJBsUzF9rfZvaSn2gSJFP0YzGZ8Qw_DdRtGK7EfyVNHBCXTeTnAh6uokqK0Jtx5nV4nWHCGKgZ-gkDLuLgJyFbfCsV19_l7tqFGw_eGHdi_91vmqS4nyIMcB3Q4P8ZJsDz50p2qs-Q95qrtldyWPY_iZNSoHTT6YZ7oMQ3QK8nSeUVs5Z7AfcrghDKHAeWjWhXQdQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e226c05d7f.mp4?token=Iyx-vT0jcSXeMqsxzkVqHB3qSqHSpJSu8hmrLMVuJRP4guy6v8MDBlbH8sp97E2bhIYPamoodatx1KuLLnf20IUk8bYyElZN3XArNIfRUPwNRJrVYJ6d_lZP5OyfKHHBDViMIduyX4B7B1YvgsJBsUzF9rfZvaSn2gSJFP0YzGZ8Qw_DdRtGK7EfyVNHBCXTeTnAh6uokqK0Jtx5nV4nWHCGKgZ-gkDLuLgJyFbfCsV19_l7tqFGw_eGHdi_91vmqS4nyIMcB3Q4P8ZJsDz50p2qs-Q95qrtldyWPY_iZNSoHTT6YZ7oMQ3QK8nSeUVs5Z7AfcrghDKHAeWjWhXQdQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حرکت خفن: تبدیل هوش مصنوعی Astra به یک بات بازی‌ساز حرفه‌ای!
🎮
🔥
داستان از این قراره که یه دولوپر، Astra رو طوری شخصی‌سازی کرده که عملاً تبدیل شده به یه ماشین بازی‌سازی. اصلاً هم شوخی یا بازی‌های دوبعدی و پیکسلی دم‌دستی نیست؛ کیفیت کار در حدیه که باورتون نمیشه کل این دموی سه‌بعدی خفن فقط توی
یک ساعت
جمع شده!
👀
⏱
سازوکارش چطوریه؟
🛠
همه‌چیز با یه اسکیل (Skill) جلو میره:
* اول Astra باهاتون گپ می‌زنه و از بین ایده‌هاتون، کانسپت اون بازی رویایی که تو ذهنتونه رو درمیاره.
* بعد طبق همون پلن، توی ده‌ها دور آزمون و خطا پروژه رو قدم‌به‌قدم کدنویسی می‌کنه و می‌سازه.
پرامپت استفاده‌شده برای ساخت این دمو:
📝
Prompt (high effort): /dream-loop Build me a graphics demo: isometric camera, voxel-ish art style with realistic shading and reflective wet floors, a character in an interesting scene. Fantasy setting (think Elden Ring, Diablo). Three.js in browser, >60fps. Don't download assets. Time limit of 1 hour. Controls: click to move the character, camera lazy-follows; drag to rotate camera; scroll to zoom in/out. No gameplay for now. World should feel alive: motion, animations, subtle environmental behaviors. Area around player should look expansive, but only allow movement in a limited space. No need to confirm the art with me or ask questions, just go!
🔗
دموی بازی توی مرورگر
🔗
خود اسکیل Astra
✈️
@ArchiveTell
|
#NEWS</div>
<div class="tg-footer">👁️ 1.71K · <a href="https://t.me/ArchiveTell/7682" target="_blank">📅 14:16 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7681">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VqBb34phgetpry0mZ0_gLIiAw7cu-X_uSiA23vDRWDVcbmxAR_tRVGy4DOot3CBM1OAp5g0qD6psfH7nxpBVJIj9iaYq2b-9XQaEeMsDFn-pJLOhvafp5iQlFIxmQU1bjkO4vXM7U0fBZwaGehVU6OhIaFPXcrXSxaBIAUol3uwSkbZMa9v-Tf2Lp5rp8OF1S6x0YjkosbvpSanbhLCHUD2o397tFFy7YZNsykVxjOyyIk0R-7JO_pi7063gZII5SQPcnPSe860FjUoxdLgzrjs-cPqCvCbdLO00ypMfO0PIyPEXxnum_1qt0mamKIfwBjJBtex-WHi7wXrHfM-SgQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📝
باز کردن بی‌دردسر فایل‌های آفیس روی اندروید با OpenDocument!
بچه‌ها اگه فایل‌های متنی یا اداری دارید و دوست ندارید برای باز کردنشون تو سرورهای ابری آپلود بشن، این اپ خوراکتونه. تمام اسناد OpenOffice و LibreOffice رو کاملاً آفلاین، سریع و بدون نیاز به اکانت باز می‌کنه.
📁
پشتیبانی کامل از فرمت‌ها:
خواندن بی‌نقص ODT ،ODS ،ODP در کنار فایل‌های رایج DOCX ،XLSX ،PPTX و حتی PDF
🔒
حریم خصوصی واقعی:
پردازش کاملاً لوکال، بدون اتصال به اینترنت، بدون ترکرهای تبلیغاتی و بدون نیاز به ثبت‌نام
⚡️
سبک، امن و باسابقه:
یکی از قدیمی‌ترین و پایدارترین پروژه‌های متن‌باز اندروید (فعال از سال ۲۰۱۰)
💡
نکته کاربردی:
بهترین گزینه برای کسایی که با فایل‌های کاری و اسناد حساس سر و کار دارند؛ با خیال راحت می‌تونید حتی در حالت Airplane Mode به تمام داکیومنت‌هاتون دسترسی داشته باشید.
🔗
گیت‌هاب پروژه
🔗
وب‌سایت رسمی
✈️
@ArchiveTell
|
#TOOLS</div>
<div class="tg-footer">👁️ 1.71K · <a href="https://t.me/ArchiveTell/7681" target="_blank">📅 13:49 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7680">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7c846b7bad.mp4?token=QDap8wepeGGPLEBlGcYECuWuKYds4KzjweHgTUW7EvYGglspySuDT7UhKt3H8bs0CvaPTjz31Ju6R_zpm_5MiaO-o_KXTb7uh8TholDWE_2o6WtDVhbkg8o-h_CGLOVcC3fzVQpUysn8h_tY1mauqVcQi-OY8_KFa2zF9qFJlxAC4XFIbqqitmDu8uenmR0FcXR2dxR2XP5gzhKK4vl9FQQlefuXdXzFFkxTs2TGb4LFMBTuDbw6hnO_cfBEBvIuYML3vNWawYsxhI4uQgLdmavVhCVdY8Njdg3iFve6izVRYgfhIKwsyDodNoPmYng-IDDgd98lnM33kyItL9gVVA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7c846b7bad.mp4?token=QDap8wepeGGPLEBlGcYECuWuKYds4KzjweHgTUW7EvYGglspySuDT7UhKt3H8bs0CvaPTjz31Ju6R_zpm_5MiaO-o_KXTb7uh8TholDWE_2o6WtDVhbkg8o-h_CGLOVcC3fzVQpUysn8h_tY1mauqVcQi-OY8_KFa2zF9qFJlxAC4XFIbqqitmDu8uenmR0FcXR2dxR2XP5gzhKK4vl9FQQlefuXdXzFFkxTs2TGb4LFMBTuDbw6hnO_cfBEBvIuYML3vNWawYsxhI4uQgLdmavVhCVdY8Njdg3iFve6izVRYgfhIKwsyDodNoPmYng-IDDgd98lnM33kyItL9gVVA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📍
با GeoSpy لوکیشن دقیق هر عکسی رو دربیار!
بچه‌ها اگه دنبال لوکیشن یه عکس رندومید یا اهل چالش‌های OSINT و ژئوگسرید، این هوش مصنوعی خوراکتونه. حتی اگه متادیتا (EXIF) پاک شده باشه، از روی خط‌کشی خیابون، گیاهان، معماری و تیر چراغ‌برق مختصات رو براتون پیدا می‌کنه.
🌎
جست‌وجوی جهانی (Global):
پیدا کردن چند تا از محتمل‌ترین کشورهای دنیا حتی از روی اسکرین‌شات یا عکس کراپ‌شده
🏙
مود شهری (City Search):
اگه شهر مشخص باشه، با عکس‌های خیابانی مچ می‌کنه و آدرس دقیق پلاک و خیابون رو میده
📸
تحلیل چند زاویه‌ای:
امکان آپلود تا ۴ عکس از یک لوکیشن برای بالا بردن نجومیِ دقتِ حدس
💡
نکته طلایی:
کیفیت عکس اصلاً مهم نیست؛ این ابزار حتی فرم شاخه درختا یا مدل آسفالت رو می‌فهمه! موقع ثبت‌نام اولیه هم یه سهمیه سرچ رایگان بهتون میده تا تستش کنید.
🔗
وب‌سایت ابزار
✈️
@ArchiveTell
|
#TOOLS</div>
<div class="tg-footer">👁️ 1.74K · <a href="https://t.me/ArchiveTell/7680" target="_blank">📅 13:38 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7679">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/W639mdezpjNnwZjn0PXkl3xH-J3Nv6IPwGS0udml7_sfIl0R_u6ZwZfH9JqowcNB0YVwxJMjfX_B5wOn_3XPWkTZXMK7gKYiPbNK_0ow4ohwMD3iFQpBPKBoMDjjzhMqVxjy8tK1l-TyHJ_UyxqspbiBUCcw6G0WoBprtt2PIDQ65LgorK5Q2RcEsry5MW8xvcQqt-YSw17lFx9T-5V5B107xEQU_6pBoM8sPMBpq4DEGL7LZrZmHxaq2z4ViRUTVbxfMwcbjlMX-3jatB6NmzncorxF_QrkpWuSO8H5UmuPh1nB7GZ8cWnBMrZKfB5_sm_G4za84r2nNPr9Txg24g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🕸
با SpiderFoot ردپای دیجیتال هر چیزی رو توی اینترنت بیرون بکش!
بچه‌ها اگه تو حوزه امنیت، تست نفوذ یا اوسیانت (OSINT) کار می‌کنید، این ابزار دقیقاً خوراکتونه. اسپایدرفوت یه ابزار متن‌باز و بی‌رحمه که کل سطح وب رو شخم می‌زنه تا تمام ردپاهای دیجیتال و آسیب‌پذیری‌های یک هدف رو دربیاره.
🎯
تارگت‌های همه‌جانبه:
جست‌وجو بر اساس شماره تلفن، ایمیل، آیدی توییتر و تلگرام، نام، IP و دامنه‌ها
🤖
اسکن تمام‌خودکار:
جمع‌آوری آنی داده‌ها از بیش از ۱۰۰ منبع اطلاعاتی بدون نیاز به سرچ دستی
📊
نقشه ارتباطات بصری:
تحلیل داده‌ها و نمایش گراف‌های دیداری از اطلاعات لو رفته و پیوندهای مخفی
💡
نکته و اجرای سریع:
راحت‌ترین راه اجرا با داکره؛ کافیه دستور docker run -p 5001:5001 spiderfoot رو بزنید و پنل تحت وب رو باز کنید. (یادتون نره، فقط تست امنیتی قانونی و اهداف آموزشی!)
🔗
گیت‌هاب پروژه
✈️
@ArchiveTell
|
#TOOLS</div>
<div class="tg-footer">👁️ 1.79K · <a href="https://t.me/ArchiveTell/7679" target="_blank">📅 13:33 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7678">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/P17W9uHfI6w_Wvwo4khvqKTxCUjGcq7Ho4YNXOUPRbGzhkXbpxduzKIB3uvjsjtssN-2gVGCFuayBR5eFKc_-13xd_qvHPSGyp5hsYQp1ojAEnv-rplsxgfVdVMU1hWR91hhJQv9cv8i2uffxGLfrSUguQySx3qV7e95kDD4VtA2qLzKGkm1Tdzn_daM47-_GAcaH-axY69Ra3bdEWrC5nv-YBAJDU9SPllmrP5rcxU9ePEtA-fZ0JsOJBEjCIvdZ6Yzgh6quMHAuS0Sq79j7S9INeahVlEoY9OhsCRTrONaEefYooMfnVDd8FqTgFDq5Qc1DW1KesaLpnsj3sFZtA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">توکن‌های نامحدود برای Claude Code با شاهکار مهندسان اسپاتیفای!
🚀
🧠
پلتفرم
Portal
مثل یک مدیر هوشمند عمل می‌کنه و با واگذاری وظایف ساده به مدل‌های ارزان‌تر، تا ۹۰٪ در مصرف منابع و توکن‌های هوش مصنوعی شما صرفه‌جویی می‌کنه!
🔥
🔺
تندخوانی با Gemini (bulk-reader):
فایل‌های حجیم و چند هزار خطی توسط Gemini 2.5 Flash آنالیز شده و فقط یه خلاصه مفید به Claude تحویل داده میشه.
🔺
کدنویس روتین (code-writer):
تولید کدهای استاندارد، تست‌ها و تنظیمات خسته‌کننده به مدل‌های کم‌هزینه سپرده میشه.
🔺
تمرکز روی کارهای حیاتی:
با این روش، Claude فقط درگیر کارهای پیچیده و استدلالی (مثل رفع باگ و طراحی معماری) میشه.
💡
در
نتیجه:
یک ترکیب هوشمندانه از چند مدل AI که باعث میشه هزینه‌های شما ۹۰ درصد کاهش پیدا کنه و خیالتون از بابت محدودیت توکن‌ها راحت باشه!
🔗
لینک دسترسی و پروژه
✈️
@ArchiveTell
|
#TOOLS
#AI</div>
<div class="tg-footer">👁️ 2.07K · <a href="https://t.me/ArchiveTell/7678" target="_blank">📅 09:34 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7677">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">ArchiveTel
pinned a photo</div>
<div class="tg-footer"><a href="https://t.me/ArchiveTell/7677" target="_blank">📅 00:16 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7676">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CWqFvhGqWuaS8L0yv5T-earNZ9OcXHTIkEnknEn6jc0mRZZwScwOB8rvvJm9_YyWaHh-40AS_L5u5L26HA58j3gV40y0y1OfnxiDLRXi5MoHvTOOSnJ2U7zFD9X95-dy11Qa_cxOM6ZgK8J9RdD2NVFVN4IWGyX4Tko-NXEmKrLryQUci0tuqIUJjDKTPdOFK9zWWXizhLvIBEFa1W9rwL-2x5bNvyTO9KFr1jdT4TtjGlQtFgrG2srUlyLjR0ph3OE-R9sA4wKTGRhxU4x0NO-WBSbhEjpBv7AbqzdHcxMXPqaqlAGBMJmBO1qo2TVY82GzQaQZrcZWXs4uy7U5dQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دوستانی که پروژه تمیز دارن و نیاز به دیده شدن دارن بیان دایرکت
یا کاملا رایگان باشه یا فریمیوم
با کمال میل بدون دریافت هزینه پروژه اشون رو میذاریم
اگه کسی رو میشناسین که پروژه اش دنبال دیده شدنه، این پست رو فوروارد کنین براش
❤️‍🔥
✈️
@ArchiveTell
|
#SHOWCASE</div>
<div class="tg-footer">👁️ 2.07K · <a href="https://t.me/ArchiveTell/7676" target="_blank">📅 00:16 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7673">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ny6_ehGyupkiLmP5umfOBFthBatSduRuX5VvYQEY9rJJv8SM3WBoBkDgINsbjyrcKWS-aKZZ38OKiok_IwUEnRNTE_YfbZMbE2Xt6O3cD-g9tCx1gOxY3ObA3WX5Xp3RwUhpyXRmHAiSz9AQO7IZyvgiw9gyx7POO6r6nhZVtck5tP4Tgg4aZuoyVp7tCpJK_UmPRktXQz1LIaf8YpA6_jFo5jCtWvUWMOWWAKxcpvFmPgCgY5wSjzhvJY7XCM53fCsUmF17zIOFnw8XRyr9l2jr4jwY2EifYlPWsrN5LAFkKSKy9a3m0NvhL7EMQFUF5Aza8qM3_uLFc1bnGvgn8w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/KjamA9P-DUaUhy73YicwCslOuvLDMEiqbhFJIGlZrBwAPGf-2irjwhQufaf9VAGOKTW9NlZjiE020KX8XisCD99yFTrXEnat7tuM-56CWfJdg0Q4jq5zzub34ouYG2b41C1G65MEV0ueVe5yKbIKx0rzqBkrOpvkKbLSD262UGL1R9fXGpyxXIQHeBs-L5oTq05HmIpfvmsfgPzu4-iydEZEeNYb9kKfeqKzUyuRnlgLhh1hfKGTHB4B1oSoeNblaCPdEjIYqOkh5QTKpj84FwlwpdZwJ7sI4kKkMSOAE7HzMYK69R8ljpzDo6T4B7cDkrELrFmI1jczZlMEN6YFMw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📌
مدل GPT-6 Astra بازم یه حرکت دیگه ثبت کرد؛
بازی Portal رو تو 23 ساعت و 43 دقیقه تموم کرد!
مدل به طور خودکار شخصیت رو کنترل می‌کرد به طوریکه هوش مصنوعی یه تصمیم می‌گرفت، بازی متوقف می‌شد. GPT-6 Astra با استفاده از تصاویر، موقعیت شخصیت و زاویه دید دوربین، تصمیم می‌گرفت که چه اقدامی انجام بده. بعضی وقتا هم تصمیم گیری هاش تا چند دقیقه هم طول می‌کشید، اما در هر صورت تونست بازی رو به پایان برسونه.
🔥
این کارو آقای "cozyblaze" با کمک اشتراک ۲۰۰ دلاری Codex Pro انجام داد.
🔗
سورس پروژه
✈️
@ArchiveTell
|
#NEWS</div>
<div class="tg-footer">👁️ 1.98K · <a href="https://t.me/ArchiveTell/7673" target="_blank">📅 23:35 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7672">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VjAHtYu8bkh18j_iKQmuzjac7AMZX_d5AL4wIXZNz60i7eVEJqXuAfyADc-3-SMVC68I4BxdRHWHVGQOYnosIjJH2RYx9uRZ1g7uDMCORGXkY2R2oXbtBIjOCyzSYUUlluC_D2cw9gcpUt_SX3kYTh3yiXGRKNsYcmYL6wIBUrNAqhlUpO30eAF4f8lGqO7J_DGdYd7BU8Bkns9bAWAFRh0KEBEw6bz_eKm2fGcalci31PRRFNrU9-S-xMMwCEEKMq-w53REOhjwUEKjLWzjR0JZFcCGqYfjqj9H7brxqmt790BdEeaDhHDqQFeW70aK-Cbs32JwYM1q4PvWLAIpPQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جعبه‌ابزار همه‌کاره برای برنامه‌نویس‌ها با DevToys
💼
اگه خسته شدید از بس برای کارهای روزمره (مثل تبدیل JSON به YAML، تست RegEx یا دکود کردن JWT) مجبور شدید سایت‌های مختلف رو باز کنید،
DevToys
دقیقاً چاقوی سوئیسی شماست!
👍
🔧
بیش از ۳۰ ابزار کاربردی:
انواع کانورترها، انکودر/دکودرها (JWT، Base64، QR)، فرمترهای کد، هش‌ساز و فشرده‌ساز عکس.
📄
تشخیص هوشمند کلیپ‌بورد:
به محض کپی کردن متن، خودش می‌فهمه چیه و ابزار مناسبش رو پیشنهاد میده!
🛡
کاملاً آفلاین و امن:
تمام کارها روی سیستم خودتون انجام میشه و دیتای حساسی سمت سایت‌های ناشناس نمیره.
➕
پشتیبانی از اکستنشن:
میتونید ابزارهای دلخواهتون رو هم بهش اضافه کنید.
📌
لینک مخزن گیت‌هاب پروژه
✈️
@ArchiveTell
| 𝔹𝕒𝕔𝕙𝕖𝕝𝕠𝕣
⚡️</div>
<div class="tg-footer">👁️ 2.01K · <a href="https://t.me/ArchiveTell/7672" target="_blank">📅 23:22 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7671">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-footer">👁️ 1.76K · <a href="https://t.me/ArchiveTell/7671" target="_blank">📅 20:54 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7670">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/786d6d3a9a.mp4?token=LeK8lHVOuXmfXXO-ikOHQJ0HVczmDd270HO9RAIntPJtvkiZn9Zy3CgF60BVcYuQ1YzwKtcQ2wCjzdDiLCgbgKwOhSdHyVod4jFoUnB7I0lk_fwFoUnVbIwGZbwNKmGEkRU2GAhny6sSeqSYWyxiaOPwzntIa-OJH59-HR1_HFlV0bg1mvbRRPY0I1qNTENn1sQXlOmnavY3Bst5YI_bMk0STerro4HSuRDNXCqythikpx4Y8ZdMm1qWuPB1bJXCopQO0_oDMti62PHhCACHWrvreIHaJWCho57epSjIUlI_gBcqwjbd3pyTwaOYGnK5QvWCDfgMScu3PmQ2Ory9ug" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/786d6d3a9a.mp4?token=LeK8lHVOuXmfXXO-ikOHQJ0HVczmDd270HO9RAIntPJtvkiZn9Zy3CgF60BVcYuQ1YzwKtcQ2wCjzdDiLCgbgKwOhSdHyVod4jFoUnB7I0lk_fwFoUnVbIwGZbwNKmGEkRU2GAhny6sSeqSYWyxiaOPwzntIa-OJH59-HR1_HFlV0bg1mvbRRPY0I1qNTENn1sQXlOmnavY3Bst5YI_bMk0STerro4HSuRDNXCqythikpx4Y8ZdMm1qWuPB1bJXCopQO0_oDMti62PHhCACHWrvreIHaJWCho57epSjIUlI_gBcqwjbd3pyTwaOYGnK5QvWCDfgMScu3PmQ2Ory9ug" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اینم 7 برنده خوش شانسمون
🎉
:
1.
@reza1629
2.
@mhti9
3.
@KIING_ZOG
4.
@Gogogrugo
5.
ＮＯＢＯＤＹ
( 6641463426 )
6.
@an_Y008
7.
@AshenOne2077
برای دریافت جایزه به دایرکت مراجعه کنید
✅
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.84K · <a href="https://t.me/ArchiveTell/7670" target="_blank">📅 20:02 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7669">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">قرعه کشی اکانت Gemini Pro 18 ماهه
💥
🆓
برای شرکت در این قرعه کشی کافیه کلمه ArchiveTel رو توی کامنت های همین پست ارسال کنید
✅
هرچقدر تعداد بیشتری از شما مراحل زیر رو انجام بده تعداد اکانت های بیشتری برای قرعه کشی جمع میشه
👇
1️⃣
وارد این ربات رو استارت کنید…</div>
<div class="tg-footer">👁️ 1.78K · <a href="https://t.me/ArchiveTell/7669" target="_blank">📅 20:00 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7668">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">🥇
رکوردشکنی دوباره از GPT 6 Astra
خبر رسیده که GPT-6 Astra تونسته تمام ۴۸ مرحله بازی «I'm Not A Robot» سایت
Neal.fun
رو بدون غلط رد کنه ، خیلیا جوری جو دادن که انگار آخرالزمان امنیت سایبری رسیده!
😂
طبق معمول، ته این هایپ‌های رسانه‌ای خبری نیست. کپچاهای تصویری سال‌هاست که عملاً مرخص هستن و حتی مدل‌های پارسال هم با یه پردازش تصویر ساده دورشون می‌زدن.
سیستم‌های امنیتی واقعی وب الان با تحلیل رفتار موس، کوکی‌ها و الگوی کلیک کار می‌کنن، نه با ۴ تا عکس چراغ راهنمایی و خط‌کشی خیابون
😁
تست کن ببین رباتی یا نه ؟!
🧐
✈️
@ArchiveTell
|
#NEWS</div>
<div class="tg-footer">👁️ 2.04K · <a href="https://t.me/ArchiveTell/7668" target="_blank">📅 15:10 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7667">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EgK2ViqRB5rpmgjjRFnoFPzi62r6M3SJAbMFmjiMFyQNmrBjcy-A_yiESm296Jd8ViJ027NDRxKTMQr9TrJn0wbDFU_Qv8cF8_PwAMBnKl9pQHRUSUQP9MmbnmM-ZC3Qw0x_xHufq91WhlynmlS87WMyL_a7j4YSS-ERFdo9lknuLg8e5K3fMzy-o0rb7uQ05H4vpAbL_5NRzZWaZWdoC8RAOra4upIQlYmafNAqjtDuwY0elP8_E5RHLATdT2yt4BsJ205ZL4XZXBbvlA9QiSkHaeO_TmMKXyVtbRxXg4UhzuDxJVwZLT3qBwuEAj0nMTH39mUA_cOIiPQHEetj6A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جداسازی صدای خواننده از موزیک با هوش مصنوعی؛ تمیز و بدون دردسر!
🎤
🎧
بچه‌ها اگه دنبال ساختن نسخه کارائوکه هستید یا می‌خواید صدای خواننده رو برای ریمیکس بردارید، ابزار آنلاین
AI Vocal Remover
دقیقاً همون چیزیه که لازم دارید! با استفاده از مدل‌های صوتی AI، وکال و ساز رو در چند ثانیه مثل آب خوردن از هم سوا می‌کنه.
✅
🔺
پشتیبانی از انواع فرمت‌ها:
هم فایل صوتی (MP3، WAV، FLAC، M4A و...) و هم فایل‌های ویدیویی (MP4، WebM) رو به راحتی قبول می‌کنه.
🔺
بدون نیاز به ثبت‌نام و کاملاً رایگان:
پردازش تماماً در کلاود انجام میشه، قبل دانلود می‌تونید آنلاین پیش‌نمایش رو گوش بدید و تا یک ساعت خروجی MP3 یا WAV بگیرید.
🔺
کیفیت و دقت بالا:
تفکیک دقیق لایه‌های صدا بدون نویز و افت کیفیت محسوس سازها.
💡
نکته:
برای آهنگسازها، تدوین‌گرهای ویدیو و یوتیوبرها برای برداشتن کپی‌رایت یا ساخت بیت‌های بی‌کلام، این ابزار سریع‌ترین میانبر بدون نصب نرم‌افزارهای سنگینه!
🔗
آدرس ابزار
✈️
@ArchiveTell
|
#TOOLS</div>
<div class="tg-footer">👁️ 1.91K · <a href="https://t.me/ArchiveTell/7667" target="_blank">📅 14:59 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7666">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DAGJ8kqKPux_WaFEhPH6Dmmghpq4DyTOQqFxDv-x45gFbHPJXSMJHDGTrmHigtfWWiGWpqJUQAoBiBWQGGtliT8eXh5I5Xbqb5cL8kcOHS7CP_KRFNMOhpUuw48lTknh8Tod8b5mlShaM7ECU_Yhm5xUln7sQNPMa4-2gm71EwhKiKIckmtsgP6tvHRqGLbxij99nK-i9CfYN8MdF97GepLYtEqzuQjQAy2dCpiQ-y9-xKYnPT8VPWJHB_aAAaPxNkkNMyz0YjNC6_rLklCN5S4u8Us69yNEdk-UzfvR-4L4zNkk7anX8AJQ9q8jWjMR5Aocpkq9yDfTl-WcfjZHbQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تبدیل گوشی اندرویدی به یک کامپیوتر دسکتاپ کامل با Android DEX!
🖥
📱
اگه از قابلیت محدود سامسونگ دکس خسته شدید یا گوشیتون اصلاً DeX نداره، این ابزار خوراکتونه! نرم‌افزار
Android DEX
با ترکیب جادویی ADB و موتور قدرتمند scrcpy، گوشی اندرویدی شما رو به یک سیستم‌عامل دسکتاپ واقعی با پنجره‌های شناور و کنترل کامل تبدیل می‌کنه.
🚀
🔺
تجربه دسکتاپ چندپنجره‌ای:
اجرای اپلیکیشن‌های اندروید در پنجره‌های تغییر سایزپذیر روی ویندوز، مک و لینوکس با اتصال باسیم یا بی‌سیم (Wi-Fi).
🔺
خوراک گیمرهای موبایل:
کی‌مپینگ حرفه‌ای کیبورد و ماوس، شبیه‌ساز جوی‌استیک WASD، قفل دید ۳۶۰ درجه شوتر (FPS Mouse Lock) و حتی شبیه‌سازی ژیروسکوپ!
🔺
دور زدن شناسایی امولاتور (No Ban):
چون بازی‌ها مستقیماً روی سخت‌افزار واقعی گوشی اجرا میشن، آنتی‌چیت بازی‌ها شما رو شبیه‌ساز تشخیص نمیده و بن نمی‌شید.
🔺
امکانات یکپارچه سیستم:
مدیریت اعلان‌ها، پخش صدا، انتقال فایل با درگ‌اند‌دراپ، رکورد صفحه و تعریف پروفایل‌های اختصاصی برای هر بازی.
💡
نحوه راه‌اندازی:
فقط کافیه گزینه USB Debugging (یا Wireless Debugging) رو توی Developer Options گوشیتون روشن کنید و برنامه رو اجرا کنید؛ بدون نیاز به روت!
🔗
گیت‌هاب پروژه
🔗
سایت پروژه
✈️
@ArchiveTell
|
#TOOLS</div>
<div class="tg-footer">👁️ 1.81K · <a href="https://t.me/ArchiveTell/7666" target="_blank">📅 14:51 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7665">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CPQJTLDzIWddc3IMvAkTIhkzr_b3D3nakseKSRN2fp3hC0n1qcsb94T987vdB0aWbFlboHpedOO3Vy22I3xoj1BS9iNJEZ9RgnX092XV0NNxPM4jo3rSg5jeHzWs0j2MMuhfKg99A6bM1aFly_52YjKovPY717Fams_OGgEl_3MsFuwUlGZyhQk_7Cx9Te1rlaHJs5CqzKxZL6OtPYePIkm_xKt2oNudQxZSet1IF7GbImzPLdZzAl2f2hiWy16btf9b_QjAjA20ERU81PV5nu1p8tuMrwJZQN28v8Urzms8eorZvceQsrdeez58r9y2G-77KwUIHmWpcfeoCsXvfw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">معدن مقالات و دیتای آکادمیک اروپا؛ گنجینه‌ای که کمتر کسی می‌شناسه!
🎓
بچه‌ها اگه دنبال مقاله‌های خاص، دیتاست‌های خفن یا پژوهش‌های پروژه‌های اروپایی هستید که جای دیگه پیدا نمیشن، پلتفرم
OpenAIRE Explore
دقیقاً خوراکتونه! یه پایگاه عظیم با بیش از ۱۳۰ میلیون دیتای علمی دسته‌بندی‌شده و رایگان.
✨
🆓
🔺
آرشیو عظیم ۱۳۰ میلیونی:
دسترسی مستقیم به مقالات اوپن‌اکسس، دیتاست‌ها و حتی سورس‌کدهای پژوهشی پروژه‌های اروپایی.
🔺
بدون لاگین و کاملاً رایگان:
بدون دردسر ثبت‌نام، پی‌وال یا محدودیت دانلود، مستقیم به منابع معتبر دسترسی دارید.
🔺
ردیابی شبکه‌ای پژوهش‌ها:
می‌تونید خروجی‌های مختلف یک پروژه (مثلاً مقاله + دیتای خام + کد نرم‌افزاری) رو به‌صورت متصل به هم پیدا کنید.
💡
نکته طلایی:
برای پژوهشگرها، متخصصان هوش مصنوعی که دنبال دیتاست‌های تمیز و رسمی اروپا هستن، یا کسایی که دارن روی مقالات بین‌رشته‌ای کار می‌کنن، این ابزار مثل یک میانبر تمام‌عیار عمل می‌کنه!
🔗
وب‌سایت رسمی
✈️
@ArchiveTell
|
#TOOLS</div>
<div class="tg-footer">👁️ 1.71K · <a href="https://t.me/ArchiveTell/7665" target="_blank">📅 14:43 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7664">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TS0RnKzHAynN7Kf2D8-VPRP5LGPxiHlK-hWcM_-ouJFvxZSDxyiyo7fLRAD3afE-fxXrTP54s4J4CYi1tS1qCfeEyrL1aaWuo7QF0p3xwR7W86-B5ezKnoEVVF3YRZIj2d4jylYAUctRF_-117qUqaYAe0oPSvxeWJGyVR39huFmmeUhGmHZQEyVKM20X340zULZr0kQVkt4p7nbs30y7L9FHfwVMm_TQ-bC7SaA2PWXb_qnTFQXfR1wRXPysp2uB2hLg3F2dBB9lMANsaORnPJ-lYm6GUVonJXNT0gBbXDN2d1zbuvEDadzQBDEjc-jJi6s583rcKBU1XSk8IiN5w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کیبورد «شریک جرم»؛ قبل از ارسال پیام حواست به جریمه و حَبسش باشه!
🚨
بچه‌ها براتون یه پروژه به شدت سمی و دارک آوردم! این کیبورد اندرویدی اسمش «Соучастник» (هم‌دست / شریک جرم) هست و کارش اینه که موقع تایپ، متنتون رو آنالیز می‌کنه و آنلاین بهتون می‌گه ممکنه بابت این پیام چقدر جریمه بشید یا چند سال برید آب‌خنک بخورید!
😁
🔺
کاملاً لوکال و آفلاین:
نیازی به اینترنت نداره و داده‌ها از گوشی خارج نمیشن؛ با llama.cpp مدل جمع‌وجور Qwen3.5-0.8B رو آفلاین روی گوشی اجرا می‌کنه.
🔺
سیستم دوسطحی سریع:
اول با یه دیکشنری سریع کلمات حساس رو بررسی می‌کنه و بعد مدل هوش مصنوعی جرم یا تخلف بودن متن رو می‌سنجه.
🔺
پروژه کاملاً اوپن‌سورس:
کد و نحوه کارکردش روی گیت‌هاب قرار گرفته و برای گیک‌هایی که می‌خوان اجرای مدل سبک LLM داخل اپلیکیشن‌های اندرویدی رو یاد بگیرن عالیه.
💡
نکته:
هرچند قوانینش بر اساس مواد قانونی روسیه تنظیم شده، ولی معماری استفاده از مدل‌های فوق‌سبک لوکال برای پردازش آنی متن موقع تایپ، ایده به شدت خفن و قابل شخصی‌سازیه!
🔗
گیت‌هاب پروژه
✈️
@ArchiveTell
|
#TOOLS</div>
<div class="tg-footer">👁️ 1.84K · <a href="https://t.me/ArchiveTell/7664" target="_blank">📅 14:38 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7662">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jynC3OSdHWEna3mqCtdGABGpPfZjnn_aFMksKA0Tm5BPmX3BWPLu-r6HduASi8R00p2Gsmjygbu4Djq3mWkMKWh2SQ-xJ2MXj80gtv-_IUb_i0_Gbt7FpWUY3BIaArkMtyf17auPJYe2BmjLS662NVVvuFrf3W9-s0_mlBEAe16DnB2dmTPnONGePA7cMGWhh4kVA7FBwNLjxqXpMDIOebD9vREZ8q3neAHSQTb3IwsfR0YqQBx0t7bARAZCNdktQifUrR6jC6tiFJ5GugSiGaM-nGoY1Q-VLq-LyrxPb-HbOuwFvm3PMObYRu1MQAUDIR5bXi3h-Kew0nBz4J9f2g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">طراحی و ساخت اپلیکیشن با M3E Canvas
🛠
📱
پلتفرم
M3E Canvas
یه پلتفرم اوپن‌سورس و جدیده که بهتون اجازه می‌ده با درگ‌اند‌دراپ و کمک هوش مصنوعی، برای اندروید و وب رابط کاربری بسازید.
🔺
طراحی سریع:
المان‌های آماده رو می‌چینید، رنگ و فونت رو شخصی‌سازی می‌کنید و همونجا تو مرورگر تست می‌گیرید.
🔺
تولید پرامپت جادویی:
جذاب‌ترین ویژگیش اینه که در نهایت از طراحی شما، یه پرامپت دقیق می‌سازه که می‌تونید مستقیم بدید به ابزارهایی مثل Claude Code یا Codex تا براتون تمیز و بی‌نقص کدنویسیش کنن!
📌
لینک دانلود / گیت‌هاب پروژه
✈️
@ArchiveTell
| 𝔹𝕒𝕔𝕙𝕖𝕝𝕠𝕣
⚡️</div>
<div class="tg-footer">👁️ 2.23K · <a href="https://t.me/ArchiveTell/7662" target="_blank">📅 22:17 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7661">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">قرعه کشی اکانت Gemini Pro 18 ماهه
💥
🆓
برای شرکت در این قرعه کشی کافیه کلمه ArchiveTel رو توی کامنت های همین پست ارسال کنید
✅
هرچقدر تعداد بیشتری از شما مراحل زیر رو انجام بده تعداد اکانت های بیشتری برای قرعه کشی جمع میشه
👇
1️⃣
وارد این ربات رو استارت کنید…</div>
<div class="tg-footer">👁️ 2.17K · <a href="https://t.me/ArchiveTell/7661" target="_blank">📅 19:31 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7659">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">قرعه کشی اکانت Gemini Pro 18 ماهه
💥
🆓
برای شرکت در این قرعه کشی کافیه کلمه
ArchiveTel
رو توی کامنت های همین پست ارسال کنید
✅
هرچقدر تعداد بیشتری از شما مراحل زیر رو انجام بده تعداد اکانت های بیشتری برای قرعه کشی جمع میشه
👇
1️⃣
وارد
این ربات
رو استارت کنید
2️⃣
در چنل ربات جوین بشید
3️⃣
با آیپی خوب ترجیحا آمریکا وارد دکمه بشید تا سایت باز بشه و دکمه وریفای رو بزنید
‼️
نکته :
در هر گوشی فقط 1 بار میشه اگه میخواید با یک گوشی تعداد بیشتری بزنید باید هربار کلون های تلگرام رو نصب کنید  ، هر 5 رفرال برابر با 1 اکانت هست ، تمامی کریدیت های جمع شده تبدیل به اکانت میشه و قرعه کشی میشه و لینک فعال‌سازی به شما داده میشه
‼️
شرایط : حتما باید در چنل آرشیوتل عضو باشید
تاریخ برگزاری ، فردا دوشنبه ساعت 20
🚀
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.4K · <a href="https://t.me/ArchiveTell/7659" target="_blank">📅 17:38 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7658">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gZF4u99FJt2IWJ8JEdlLu3QMhm0sC45tsCwmZUBTSyPJRAZTcUcPFgFaOzYYGriQuVTwZhLvjOs01hbyUbFTABPSLbuHbdz2qYtJSxFkkjrDKPxzodJzz1q_AVfs7tMookDacCCuVFdAyWh0G6Sqjk15G7RmYcmpMp2N0xhAN-aGEVg4T0TUPSKszfjnA03jGnzkpmil9Fjh-cup5fugCoh1nz1a-b8UCEJ52bC8BP5zDPI88H0bAagsbE2Rcugi4TJ0TihMLVAzkNJTY41ZhyDeq0k8H147lZnwjo2cmxrfvvF6LRgVbcGT1OcBIfGA7dfrdNrbyFsHMsJLKvfTsA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دسترسی رایگان به API هوش مصنوعی ها
💥
🆓
DeepSeek-V4-Flash-Vision-Exp | DeepSeek-V4-Flash-0731 | Qwen3.8-Flash-Next
✅
این سایت ثبت نامش کمی آزاردهنده هست بخاطر UI بدی که داره ، باید با گیتهاب لاگین کنید بعدش میره تو داشبورد و به ایمیلتون کد میفرسته و اون کد رو توی مراحل وریفای وارد کنید ( شماره تلفن لازم نیست ) حالا بگردید عقب و از سایت API دریافت کنید
✅
هر روز این سایت 1 PTS بهتون میده که معادل 10 دلار هست و خیلی زیاده برای این مدل ها
🚀
محدودیت هم هست 20 درخواست در دقیقه
‼️
📌
Base URL :
https://developer.amd.com.cn/radeon/api/v1
🔗
لینک سایت
✈️
@ArchiveTell
|
#API</div>
<div class="tg-footer">👁️ 2.25K · <a href="https://t.me/ArchiveTell/7658" target="_blank">📅 14:55 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7657">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">دسترسی به Deepseek V4 Flash به صورت نامحدود و رایگان
💥
🆓
به مدت محدود در این سایت این مدل به صورت کاملا رایگان و بی محدودیت درخواست قابل استفاده هست
✅
📌
Base URL : https://api.b.ai/v1
📌
Model ID : deepseek-v4-flash
🔗
لینک ثبت نام
🔗
لینک بخش گرفتن کلید …</div>
<div class="tg-footer">👁️ 2.02K · <a href="https://t.me/ArchiveTell/7657" target="_blank">📅 14:37 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7656">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/n26CQTBop4MbNGQ-RfvfFZxjHJaH8r0lVKRQAmV9QNyjmBpJwDIdfr0ljFDa5uglBryuCE4m9TgnL1sQVWaAEElhK0yJZuw1VLOQ6od7ZxGaSy9y-lyu3omJ_aWZpdArY1q8uqMmMccV3PRxMuZ_v9fzhdAG29D29AIvotTKzXsZ4WP31RUySkWHV9MgXKy4GTLhNn9XwY-kKYGmy5Ox2pscO5EpIrc00ssudTksYEBUXkUAkMfHpL1ZCHx-6KUvH01z1G4Sgr8HmKdt2bWOkEmR5F4Hxw1X9-_mo_FFHy9U8XWGEQ9wulheRJHOvxTlS5Lgv9oqDlr_2AeM77PhWw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دسترسی رایگان به هوش منصوعی های محبوب
💥
🆓
Opus 5 | GLM 5.3 Flash | Deepseek V4 Flash | GLM 5.3 Flash
✅
4 میلیون توکن میده که میتونید استفاده کنید از API هر روز هم ۱ میلیون توکن میده برای opus 5 ( حد مصرف روزانه هر مدل ۱ میلیون توکن هست )
📌
Base URL :
https://helyxai.space/v1
🔗
لینک ثبت نام
✈️
@ArchiveTell
|
#API</div>
<div class="tg-footer">👁️ 2.25K · <a href="https://t.me/ArchiveTell/7656" target="_blank">📅 14:08 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7655">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/L32ugxwxO59U24zvPfZ5hfUXpW2zq-kHRZ7X_88iIUMV91XtaY5nBvLLHRtEuztywLFq7YwfWGUuEr4X9KWzb70b9XBjuCkALSMOm9hNrH28jZVz2I0BHXq54KwY0Y7WYvQBYuIQ8vl5woN1YMUITuuznga9sdQuX4bOyX6YwMfgh48tuExKaROlObliiOrJP8NdWQNCvO2ewo3AU2SzqfSVDf67Ane7_YJ4Sy1Go90TXIUAdEoMab07rUofsHcAtVx-3QK3r6jgVrwCrAjyLmuDwY6Ifmy4WwjAvTePeDYYQvGaeGnCc_MTTlzBh1sSu4JOUIDKie599lIaCUMBMg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آموزش گرفتن ایمیل دانشجویی رایگان
💥
🆓
کلی از سایتا همیشه به دانشجو ها تخفیف هایی قائل شدن یا چیزای رایگان دادن مثل گوگل که واسه وریفای یک ایمیل دانشجویی میخوان
✨
‏اینم لیست مزایایی که داره:  ‏• جمنای: ۱ سال رایگان  ‏• چت‌جی‌پی‌تی: ۴ ماه اشتراک ویژه  ‏• جت‌برینز:…</div>
<div class="tg-footer">👁️ 2.33K · <a href="https://t.me/ArchiveTell/7655" target="_blank">📅 11:08 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7654">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">آموزش گرفتن ایمیل دانشجویی رایگان
💥
🆓
کلی از سایتا همیشه به دانشجو ها تخفیف هایی قائل شدن یا چیزای رایگان دادن مثل گوگل که واسه وریفای یک ایمیل دانشجویی میخوان
✨
‏
اینم لیست مزایایی که داره:
‏• جمنای: ۱ سال رایگان
‏• چت‌جی‌پی‌تی: ۴ ماه اشتراک ویژه
‏• جت‌برینز: ۵ سال استفاده از تمام ‌IDE⁩ها
‏• گیت‌هاب: پکیج کامل توسعه‌دهندگان
‏• آفیس ۳۶۵: نسخه کامل ورد، اکسل، پاورپوینت و تیمز
‏• فیگما: نسخه حرفه‌ای مادام‌العمر
‏• نوشن: اکانت پرمیوم مادام‌العمر
‏
برای دیدن آموزش کلیک کن
✅
✈️
@ArchiveTell
|
#METHOD</div>
<div class="tg-footer">👁️ 2.46K · <a href="https://t.me/ArchiveTell/7654" target="_blank">📅 10:38 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7653">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IZBKqvxvbEOXLK4XoQrBAA5FjE2yzDDsDWrpdy-S9ZV7fnCTw7rTbQm6XxkEmGA7l5CWtbCN1X0e297lumXA5lv4p01nKEMYCDgqkcHFp5ydi_XX0OzL_FYg3jzwlf84vbvsAJ0dhaZLtRbxyouKRAwOKZk5X4lDIE7ioUmmOZctpKfuIQAT1Uz6h_sQ4jmISEwS0nroYFCSIlBkPTT3R_pWD3gEGsc0VmJsk-VtPviQEJ97xa3PMHcqzqQ7jlpA82FFHBwMtWLEpSK6IeHq9hXCFeoMvEwbPLTXCQfX9Oe8fu_G98WcvggvGgnAQlLWCW3AembojUCU_nN-dr7s8A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💎
داستان GPT-6 چیه؟ انقلاب هوش مصنوعی یا فقط شوآف تبلیغاتی؟
🤔
این روزها همه جا پر شده از اخبار رکوردشکنی GPT-6 Astra و نمره عجیب ۹۹.۹٪ در بنچمارک ARC-AGI-3.
طبق بررسی‌هایی که کردم، این نتیجه تو شرایط کاملاً ایزوله و خاص ثبت شده و توسط منابع مستقل تایید نشده.
قیمت‌گذاریش هم به شدت نجومیه؛ هر یک میلیون توکن ورودی ۱۰ دلار، و خروجی ۵۰ دلارِ ناقابل
😁
(مقایسه کنین با جمینای ۳.۸ که ۳.۷۵ دلاره)
در ازای این هزینه سرسام‌آور، وقتی در کل حساب کنید، برتری خاصی نسبت به رقبای خودش مثل Fable 5 نداره.
یکی از معدود بنچمارک‌هایی که هنوز اشباع نشده و به نظرم بهترین معیار برای ارزیابی مدل‌هاست، بنچمارک Humanity's Last Exam عه
تو این تست، عسترا نمره ۵۷٪ رو ثبت کرده؛ در حالی که Fable 5 با قیمتی مشابه و حتی پایین تر، نمره‌ش نزدیک به ۵۸٪ عه
🔥
با دیدن همین آمار میشه گفت OpenAI با این Gimmick های تبلیغاتی، رسماً داره به شعور کاربراش توهین می‌کنه
😐
من حتی کاربرشم نیستم ولی باز به شعورم توهین شد
#طهلیل_ai
✈️
@ArchiveTell
| S</div>
<div class="tg-footer">👁️ 2.25K · <a href="https://t.me/ArchiveTell/7653" target="_blank">📅 23:46 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7652">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Tf80rdILTP1hhFYsEmgWt5vIiXMn_o03Gy08mt85BQIgkcFoV84JyRsoktgbfUWwI84P5Ys3cd2yPPsWOQUR_RUqKlUhJa4Nd3sWG0x80vZslsQ7ulDJKm-oZLIiI36HisRXLPd4oHlNAibDo_K1LuP1pq4JiSuF17cdEwzqY-fUM0IP1VP8dsA83zZA6d6LWhmqZFt5saA1bQp_oW3_QypfzapFXmKayYMNTN_Yi6WektRziuakDHXRlaV6aw4HYwKnel3r5ub2vsGDmK_PRyJC1z8xtInhEu0DwfAokufL_eCISR9JBtrI9tvx6uY_FoDzfzQe5z_ScUmKHuGqbg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">Free 2k$ model GPT
💵
📌
Base URL:
https://vip.9aws.net/v1
📌
API KEY: sk-g926rIr0SG7pfoD4WextkZwRRAgFOwYZDsG5hnDr8mL2ZH9d
📌
Models:
gpt-5.5
gpt-5.6-sol
gpt-6-astra
✈️
@ArchiveTell
|
#API</div>
<div class="tg-footer">👁️ 1.97K · <a href="https://t.me/ArchiveTell/7652" target="_blank">📅 22:54 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7651">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gSDAosXdzY5kaFGIF9gg6XH9MLiG3h3KPz5FnThFELwnylQXTGkMV1rj9FrYCXtgFArpr5lGyWMmAwuFYDo0IH828RJMV3CK3pfNuc1WDBCN5nkQ0KGkFNudnOUFNruJFeSiaYR42XioZ66LQtOFoZkBOhmLYr7j2y8ApiqJf0vYnKiyJ13AT1f-5SBs7Si70W3VPYvedknynH-8FLoESnXO5tC77DQ7Bm19L4MgZRMzYeocdJPvMib0Z62VaZbyc7yWHZaox5oOcse0sNvMXbq9tnRX9yCWwiTZxq5GUyzgmnlU86soRscLvXfwW33tJpi2C29ccuDA0Z3t2kwg6A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دسترسی آزمایشی رایگان به مدل‌های پیشرفته هوش مصنوعی
💥
🆓
Opus 5 | GPT 6 Astra
✅
سایت ClickUp فقط یک ابزار مدیریت پروژه نیست؛ ClickUp Brain حالا امکان استفاده از مدل‌های مختلف هوش مصنوعی را در محیط کاری ClickUp فراهم می‌کند. طبق مستندات رسمی، مدل‌های OpenAI، Claude و Gemini در Brain قابل انتخاب هستند و می‌توان بین مدل‌ها حتی در یک گفت‌وگو جابه‌جا شد.
🚀
🎁
سهمیه رایگان
در پلن Free Forever، نسخه آزمایشی Brain شامل ۲۵ استفاده برای هر Workspace تا ۱۰ نفر است. در Workspace های بیش از ۱۰ نفر، این مقدار ۵۰ استفاده است.
✨
⚠️
این سهمیه ریست نمی‌شود و پس از مصرف، برای استفاده گسترده‌تر باید پلن/افزونه پولی تهیه شود.
🤖
حالت Agent هم دارد؟ بله!
دارای دو نوع Agent است:
• Super Agents برای انجام کارهای چندمرحله‌ای، تحقیق، کار با اطلاعات
Workspace و اجرای workflow ها
• Autopilot Agents برای انجام خودکار اقدامات بر اساس trigger و شرایط مشخص
💡
علاوه بر چت معمولی، Brain می‌تواند روی فایل‌ها و اطلاعات Workspace کار کند، جست‌وجو و تحقیق انجام دهد و حتی Task، Doc، گزارش، اسلاید و موارد دیگر ایجاد کند.
🔗
لینک وب سایت
✈️
@ArchiveTell
|
#TOOLS</div>
<div class="tg-footer">👁️ 1.95K · <a href="https://t.me/ArchiveTell/7651" target="_blank">📅 22:45 · 14 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>

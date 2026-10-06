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
<img src="https://cdn1.telesco.pe/file/gF1sNwP0A5nzVO6lA5LZJ9k04-GhdP_t4zquSOBE2SaMZLjcqWWRLObKZtqZCJQMMME-KdZlIOKVCFusBwuoDbyPYybTqRQWH-R8Lv55X0vZBJaPzbHabiONC97s7dJXiNCqVjq4hrVHgoSrtDvavFS4DQNHRwj2a5clvofPvQw8QwOR2uXXrg_j46evyj3tx76B1nPdwgclYdj2bXMLcBtAXgnLoYw1IroTS4u_5mmswxcjEWpvpDhgNvtafP7Z_2RTjubZpLXGTBEs4a57lE3boDcTIqY4_qmJqC6KkuXHisGlH4J9USMCvB1LTdTSR7aFTvHboD2Jvb6GfyzTxw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 IRCF | اینترنت آزاد برای همه</h1>
<p>@ircfspace • 👥 96.6K عضو</p>
<a href="https://t.me/ircfspace" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 این‌کانال با هدف دسترسی آزاد به اینترنت «به‌عنوان یک حق شهروندی»، به‌دور از هرگونه وابستگی حزبی، سیاسی، تشکیلاتی و ... فعالیت میکنه!https://ircf.space/contactshttps://x.com/ircfspace</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-07-14 03:59:58</div>
<hr>

<div class="tg-post" id="msg-2652">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/dyg1GOIO4tTIISX2pVBJbHiA-ujU0Bniuo1qzLmgUnzZeODwLDzbCf3oolEY7Xbp-cI2q2KWtApLOmVJ4bf0t5PHHMvwPdAx-Hv4eLR6ox8nbPA1mHGi3n1AThulfc4qLbJujKntm0-kNpOyQIOB5wpZYNyZNhjE75D8hv1Y15C8feZShtiaPnMPkzJVuYLOzQCX0uS1OxCxdynLagEEzwT73fuH6jR7YcTLVfWxDsB2dUAiAFsNoBFvZnLqF4ZNwbuDjKFjhSr50UtEQSkIBdv8FFC7sAdwD6Fav9iHocGozhgXP08JtaO7E7Mjr8ay-oZuNQafu3HSyxWzVMBxiw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پترنیها در تحلیل وضعیت فیلترینگ ایران، جمع‌بندی روش‌های فعلی اتصال به اینترنت آزاد از طریق کلودفلر روی فایروال همراه اول و ایرانسل رو منتشر کرده.
بر اساس این جمع‌بندی، روی فایروال همراه اول میشه برای اتصال به CDN یا Worker از روش ECH با یک IP مناسب استفاده کرد. استفاده از IPv6 هم یکی دیگه از روش‌های فعلیه که بسته به فیلتر بودن یا نبودن دامنه، تنظیمات متفاوتی برای finalMask داره. برای WARP هم میشه از متد WARP-in-WARP در اتر روی IPv6 استفاده کرد و با اسکن، IP مناسب رو پیدا کرد.
روی فایروال ایرانسل، برای CDN و Worker میشه از متد F&F استفاده کرد که نیاز به تنظیمات مشخصی برای finalMask، cipherSuites و فینگرپرینت داره. WARP هم روی این فایروال قابل استفاده هست و محدودیتی برای نوع IP وجود نداره. علاوه بر این، روش MASQUE/H2 با اسکن IP و تنظیمات مشخصی برای فینگرپرینت و finalMask می‌تونه برای اتصال به کلودفلر از طریق هسته اتر مورد استفاده قرار بگیره.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 7.86K · <a href="https://t.me/ircfspace/2652" target="_blank">📅 23:57 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-2651">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ieaEOUj_zZNW0VEO8wHc6RloEtjSCXK3iIgUrbvyvKpEtbzckjB3Wuo6cchpzo3A16zPd5-44laUk4flqbTXxyZXQk5V4B15buhP6J8p4JDeiFdC2mkjU4AYMshHnWtxwex73NF2sxpOQh8oUuY7p3DzICu4ESr6PHLNGZZZY2Cx1YzUxD-EssTMvvkvJGNMpPAM_ixNXFDo_XDhjBP16ZkR9zJJZ59IzdVu2gMNEmrGf2h2GXsvzA_flRfEARqp--GJvh8EOWf9HobhZBshZsvAIBCYOHeDPz8jb8KkABSxJuE74YZ2UrVW0Wx42aK2fBt-6pQhJptb3NdMDVPVAg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فیلترشکن دیفیکس توی جدیدترین بروزرسانی خودش قابلیت تانل‌کردن کل سیستم رو بصورت آزمایشی برای ویندوز و لینوکس اضافه کرده.
در این بروزرسانی عملکرد کلی تانل بهبود پیدا کرده، مشکل نمایش پرچم کشور محل اتصال رفع شده و چند ایراد جزئی برطرف شدن. این نسخه درحال حاضر روی گیت‌هاب و گوگل‌پلی منتشر شده و بروزرسانی مایکروسافت‌استور و اپل‌استور هم بعد از تکمیل ریویو، در دسترس عموم قرار می‌گیرن.
👉
defyxvpn.com/download
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 9.31K · <a href="https://t.me/ircfspace/2651" target="_blank">📅 23:34 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-2650">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/KnKx62s3Jutx8JUaOj7AZlG38xCqBvwdz6ZOaoaVO1AXU_B5a7wKQOGcS15ZWRXIKw4FpdEBPKUSaiKZ6HvVMdlPfB2CeYI-xSrtkgQCfOiMoYXmDH3n_t88TwUI1NsllxGp_nh9V0xZ49uFhitrK8VhBQ5d9KJMhkLf10R8M1lSUhTLc2vVIfu8JlpFe8ZD-R8ZpABQSpdzFayb-YiOa04NFGQ4WKjAFKR3d6NwtDlYC7pHn7PIStAs7Q-DtEY7tFRX4xao0i3YFXd2o178ovb3qv1SakGVFDFZQYOLg7HNo98xDypBYANyv7Gn7ParL-6sgFQMXDIfYsnFSGzpIQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ادعای "قطع اینترنت کل کشور فرانسه به‌دلیل اعتراضات دانش‌آموزی" فیک‌نیوزه.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/ircfspace/2650" target="_blank">📅 18:02 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-2649">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/XpFhY611E5qSVwWRQQfe1CQ8qpCM7EjvQxgMIgkLPspH5obw8AomDTRrILBEd2XbQ6YOzj3Wa9inctK2FKzhEy_5Q20EeRf-vfstr33CC7jbLiHfHXsJ1SXnWe8MU04gTD9J03i3TcL1lVTSG4gyk29RLH8iEvC54aEtMjuacq7uki848uY2KJcTocWY1X-H4mSVCEZN2-R2qsUxDqBdmNmse05YjfmSU66RB8Nb0_9Cwu_hNXkoeCBkS9cTSodQYK2pRDIQhLp7n0v1aZ8x98Q3Hd0u4il_k6SpO6gQu74D9eNg0Uv4yx94kcSZNLoynsoZxrYhMoGgu4Fli9bf-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جمهوری اسلامی در جریان اعتراضات دی‌ماه تونست با جمینگ و GPS spoofing روی
استارلینک
اختلال ایجاد کنه و حتی تو بعضی مناطق کیفیت اتصال رو به‌شدت پایین بیاره، اما اینکه بتونه استارلینک رو کلاً از کار بندازه، دور از واقعیته!
اسناد ITU نشون میدن که با وجود این اختلالات، ترمینال‌های استارلینک همچنان تونستن به اینترنت بین‌المللی وصل بشن. حتی راهکارهایی که SpaceX برای مقابله با این اختلالات اعمال کرد، باعث شده سرویس در بعضی مناطق دوباره پایدارتر بشه.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/ircfspace/2649" target="_blank">📅 17:53 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-2648">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/VzM5oIWMwi9duPPFo29XgQFuAgtU3jS7rMjEZwdAOgKXbllLQugJGDmt3po860kKLWywMzQZPA4iHwfqrsAiRmSxl6sX6OZvxtMk_1TGke4PsDyTas4F7c-uEWIYV6vZKjypUcgE_qTPqAciOZy4CZTL_cwiF1OA8L1WDCeRIsLN-UrPX_H3Mp6IXvridRcD5B4OGCahE6SpokPQJJuWvZj2K7XBqp-upk6-9BOGOo-BsFOpQE93sRwRwqPU2iwiOiw4UnP69SBJijMHjbW0T2mlpajVaaWRaB4H0IZhPK5GkqWPUn2yhhJynKaYO1N67zv9C1Uio6VijsjyVKjZjA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رئیس پلیس امنیت اقتصادی فراجا: هر سایتی که اقدام به اعلام قیمت‌های کاذب ارز کند، باید بداند که برخورد قضایی و پلیسی با آن به‌طور جدی انجام خواهد شد. /انتخاب
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/ircfspace/2648" target="_blank">📅 17:45 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-2647">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/oblNkrM3b5bJeTcGgRIJIAqBJjfpNHxGhLqTlZIvy3NxhoEB8umwkm_bsSqR1b0RnLCDG7dPQ5RXLuXhV6BTpUje_auFP8Am2QZVape1ZUe1EDbhxPXNfXDzuove7ot66F4CffoKV82FYs2BatAVCvcS2qNnlHUGrpKQeXxEkThm2jpxodCZiFW8KAjMTLcVaRGk_fX_vGJzX5isFQfdKtb793lcpg8_AhcbhVmjhXO4lQWy78O6L66rMJ9V4jEsUsUd36zLZP_6brYpKNYmcWdR9ZfSF8emZhPNtq75GHlIbSqMgc3zDhYpkSdb4WwNXFAtd8TODC2jewBymJIO8w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آپدیت جدید از فیلترشکن متن‌باز و رایگان Aether-GUI با آپدیت هسته اتر به جدیدترین نسخه و اضافه‌شدن متدهای اتصال سایفون، تور و مسک‌این‌مسک برای ویندوز، لینوکس و مک در دسترس قرار گرفت.
👉
github.com/MatinSenPai/Aether-GUI/releases
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/ircfspace/2647" target="_blank">📅 17:41 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-2646">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/J_XoZ_4rcBg0PUEmAMpg4D7wKO9dWRFlCWj05lVrzZC7ejWgk2eqyGLFyyoAL58W5wXeEayiDJFvixmRrDhJB2QUc1kY5j2L3RQk9epE5EXp902Wqjcvm-F4DnmWDggsekNZOxCe-IOTgqraTRMmZzM381BIlgi-vORNn8wxNqZIXxAXNg1J-9DYtWoYIAnjJ01UvQYu33xGip-X7wdGzhAuASGQwGE00FPagSPNTzCpdf_7eTDtqmGvrAu5zEzq8I0gT_jyLmo0jy6hrvOKDiY__dVJ42OiZcyuNjay1CUpXMYt8tP8KOUURO_9kTUHWIhOAsU3e4hfIvfPDqiRPg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رئیس مرکز ملی فضای مجازی گفت: ایران برای اولین بار توانست با موفقیت پایانه‌های استارلینک را در جریانات دی‌ماه سال گذشته از کار بیندازد. /عصرایران
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/ircfspace/2646" target="_blank">📅 17:35 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-2645">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/sRGxolBtXgynYG38Qm5npGTnbEOXVP9LCzmfI9YueHjQF0pqQNgWwjvPu1E2ZBkUBdgZWwKnua8gVy-JXVQ_iZFKXl643UTLmnsj57bYKTOo3HqKnVh4_BYCw5MJol4bJQtd5oi5Urbp2Lc0v6ANVcnJ14mQnisAdGp5sm6HP6f6hD0kwqD1DgPOSpxDykYHRHzNkLqCBjDZ5ymurii1JBM8whVnE9IZeAtMSE3cpfRO92EydAHiq7t7-6CL_TYcF5PKgYSG8-MPrpOb64gLwe419RxBsRMUPGCDOgRHdPLrNjdlzDBazZeTB3xo23d6Jw2gTsaWHLIRJUeGJya7NA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">زومیت در گزارشی نوشته که در حال حاضر دو راه رایج برای دانلود فیلترشکن JumpJump وجود داره، که یکی از گوگل‌پلی و دیگری در گروه‌های تلگرامی هست؛ اما بررسی کارشناس‌های امنیت سایبری نشون میده هر کدوم از این جامپ‌جامپ‌هارو دانلود کرده باشین باز هم در خطر هستین. فقط خطر یکی بیشتر و اون یکی کمتره!
جامپ‌جامپی که از گوگل‌پلی دانلود نشده احتمالا یک فیلترشکن دستکاری‌شده هست و به نظر می‌رسه این فایل یک exploit یا آسیب‌پذیری قابل سوءاستفاده داره که می‌تونه دسترسی root در اندروید بگیره و رد پای دولت‌ها در نسخه دستکاری شده دیده میشه.
حتی اگر نسخه کرک‌شده رو دانلود نکرده باشین، بازم برنامه اصلی دسترسی‌های نامتعارفی از دستگاه می‌گیره که نشون‌دهنده ناامن بودن این فیلترشکنه.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/ircfspace/2645" target="_blank">📅 17:28 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-2644">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ORnksidqJ-APN29a8ccIOFWb7Q1WcMpWnZ6t_MyCHZkS3V6F3mLWgPZFxe5u-oMaSzPDY7RvEb9fZft6XnxIHh42Y0sBFmCbTiYDGffgPqHLnYgjB4Nbmr1ESMuVgCLE1yf2zAGrXbw9SSMe8f3M7HOrjj05cdQUsogNBE9ru5t8JG3ggDFLyEBolUPOF06ixkeA71G_xxkTrpT3m6B9d-P7_kctZZrU_j_5aNHdKbQJSvY0nnqoKWeXWJWJZ5xiG3OTUWLLciRz6_cm1lXeMBHZ1P0ESr5zbOjg7CndpWwdQWS0otvRc7q2JPYGTW14zmiO5Xm-jalGKU2FMLxtsQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نسخه جدید از اپ سایفون چندروزه روی اپل‌استور در دسترس قرار گرفته.
👉
apps.apple.com/us/app/psiphon-vpn-secure-access/id1276263909
💡
play.google.com/store/apps/details?id=com.psiphon3
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/ircfspace/2644" target="_blank">📅 23:38 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-2643">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Fdx1VMeSUn1rc9YrB8tBWQM-n_dASEuR9HSCkse7vjS0wsPMzPtT4SU6HAAeuse8522OXaYwoG5QPZuKwHsBfE1aluT6VifIQRXn2CGACjufZjVrqYLeG4sAb_TIMRUrfjI6nIKqaXNrV3q6lKJltITBBVgm8eg1wb7vOJ0JJEoiZbS_O33lnHHvZC_kxYMEUVQGe0X8KJFn6WXCuqiVCd_yauglK4H826225tTnJ7TiqKlEiSiBZpF83wW1moCvpPK_sUf7JeJuhT6XLYUMbqMn8gpZTmn7jlSZwaKdhLautQq8iNZGaUMOsRWXCI3CrVmkwhzkqpQTowyvARSXOg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">طبق آمار رادار کلودفلر، از ۲ روز گذشته ترافیک ایران به کلودفلر به شدت کمتر شده. اکثر کانفیگ‌ها و اتصالات به کلودفلر مثل وبسوکت و xHttp مختل شدن، فرگمنت روی همراه اول و مخابرات بسته شده و روی ایرانسل ضعیف کار میکنه؛ همینطور پروتکل UDP به سمت کلودفلر کلاً بلاک شده و اکثر رنج آیپی‌های هتزنر و OVH از بیخ بلاک شدن.
©
mahsanet
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 55.8K · <a href="https://t.me/ircfspace/2643" target="_blank">📅 23:31 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-2642">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/lXd8pDiVWP9kiJgfBwx-lIm_r6tdBFCLYBDMWcIth2kJaW7zUmo3I2jncTO5o1JY5RQsikjepYdHSgtbbrTJNBDCqDOPKZfaoOukYSp8eMGE9V4oJHFDi31xPF7LdRpNi4CYV-4_zs6D2R_53CmlQwbwDp5Zuix7hk1rj3admzfHJBO1a1SRKtWz9_GRLyuvH_Xu-8FInIa1LckMkAkWlbrO79O-6MYcR3mZaX3zEbq-T3ngaObI9GznyL5-WgexAjTBTipIVZqryi-nwJzcFBqhCMgBqFTu-n2-Ov5ldwsDDUL7CoeqjtpSuXcUY7yJaYXaWlkn0xcthEPg7D9rng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نحوه استفاده از برنامه‌های PattN و PattNG برای دورزدن فیلترینگ
📽
youtube.com/watch?v=CnEQipAJ2hE
💡
t.me/ircf_toolbox/25
©
𝐀𝐥𝐢
👉
github.com/patterniha/PattNG/releases
👉
github.com/patterniha/PattN/releases
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/ircfspace/2642" target="_blank">📅 23:19 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-2640">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/czy_xgtRBfEwZlooT5OHngIZ0rTjBUTvHj94VL9XOeNHuHPxAYi6EHXuPxkXLHGBc01Ck6k6VpkHnZl7GVqDr68NYABLJFp_sv_OM-IC4h4Lc46PZ4AVZHs1PEapE662cwfoHl3KquozI5Dchw0YbeIqyiLsMw3tOu1Ox3xjSyYFoSkEVlNBp_sAMzibKw07TXYUIkx4L_wFImjrM4R48q3KqY5Y89hViWCJqB6pjJtKW7JZPpX4iqOVFcOnmRpqjqmcDX8UOVHA57pS9SJ4NYZXTAhEl3Nja_TThjgsQxWNEzMvMANhpa1w2h4L4UfYNaLKyWTrDoZjrz8a78-Yag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آپدیت جدید از هسته Aether مشکل برگشت آیپی ایران در متد اتصال Gool رو برطرف کرده و محدودیت اخیر دریافت کلید وارپ و مسک رو روی بعضی از اینترنت‌ها دور زده.
اگه H2 روی سرویس دهنده‌هایی نظیر ایرانسل به هردلیلی ایراد داشت، میتونین طبق داکیومنت از فلگ فرگمنت استفاده کنین.
👉
github.com/CluvexStudio/Aether/releases
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/ircfspace/2640" target="_blank">📅 23:05 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-2639">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/RnT3izezx4khZVz-MTkEZQNXBJPbmzt9pfd-Raj0cyG3_qRHcNe_zbEruIuTQUjnboShzHv40u7rcQEVo20SKKJwaYh14ri5Uv9P2dkQ0IeVJz6L-6u07n6Uqf-o9W0b7T_zr0gKeqrzLiQfUT_qnFkB7OIv4yZK7CVSEKi-4fDLy7UuuYVoAUSa7aBFLauHg3vw1pOm3W6Y4meXjEcfpzkGaNysWXBP9rZPNi3VCjpDOlrMj6x2LN2E8F5fLqNmJn35Gbpwxh7kxwQSoXFOlpV1sYc7CbmoaY0jaD5nntstFILGAwNvBiSERe04SoiA0Fc6y0tT0647DWH-aa6eJA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نسخه ۱۸ از فیلترشکن اندرویدی MahsaNG منتشر شده و توی این نسخه هسته Xray مهسا آپدیت شده و پشتیبانی از پروتکل MASQUE رو اضافه کردن.
برای وایرگارد و مسک حالا یک اسکنر IP اختصاصی در دسترسه که از نویز و پورت پشتیبانی می‌کنه و میشه کانفیگ‌های این دو پروتکل رو با کلید Auto ساخت. امکان بکاپ از کانفیگ‌های شخصی، صفحه پروکسی تلگرام برای کپی و تست سریع پروکسی‌ها و بهبود Fragment و حالت Auto هم اضافه شدن.
چند نویز جدید برای عبور از فیلترینگ UDP، کانفیگ‌های جدید یوتیوب و پشتیبانی از Cipher Suite برای افزایش سرعت آپلود در متدهای پترنیها به این نسخه اضافه شده. FinalMask حالا روی پروتکل‌های جدید MASQUE و Hysteria در دسترسه و علاوه بر رفع یک سری از مشکلات، ابزار زنجیره‌ساز کانفیگ هم از Fragment، Hysteria و MASQUE پشتیبانی می‌کنه.
👉
github.com/GFW-knocker/MahsaNG/releases
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/ircfspace/2639" target="_blank">📅 08:22 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-2638">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/uEfrrhTtLN_AtZy1pedDNwp-JpaJAXi4b_8QPrC_BMFqnm3ukiZME8MnCN7N8IuE4Gpt5eEVEdfpkee1p2n8Ps9TXfBcePmj5HmnMNexGxZUpPWlqwzmt7f7Q4TIJV301i_eB3t-80vls0skY3kOZxaPx5GjeVk6cVOb278uOhsbXLD6TVmhmigbrOKm4xLPda2EcFkkCneAVxd0CSj3gVw_U5ELXK9NCHEqdAl9NAt3iWXPdDSubobRtTcOTMnJ5-Nh6916avgbTSs3XvNyoquDzm5z_GohxzhC7R8DWbEaDuhc3mMsTaNNoSad5xoQvkQd0LLHoee_q4nmoV5vnQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اپل از نسخه iOS ۱۸.۱ قابلیتی گذاشته که اگه آیفون ۷۲ ساعت آنلاک نشه، خودش ری‌استارت میشه. این کار باعث میشه اطلاعات گوشی دوباره وارد حالت محافظت‌شده‌تری بشه و ابزارهای فورنزیک مثل GrayKey سخت‌تر بتونن قفل گوشی رو باز کنن.
حالا شرکت Magnet Forensics که سازنده GrayKey هست، ظاهراً راهی پیدا کرده که قبل از این ری‌استارت خودکار، گوشی رو در همون وضعیت نگه داره تا مأموران بتونن فرصت بیشتری برای استخراج اطلاعات داشته باشن. این قابلیت با نام GrayKey Preserve و همچنین Evidence Preservation Mode معرفی شده. البته فعلاً این موضوع بر اساس یک ویدیوی تبلیغاتی لو رفته از شرکت مطرح شده و جزئیات فنی روش منتشر نشده. در واقع جنگ بین اپل و ابزارهای بازکردن قفل گوشی همچنان ادامه داره.
ناگفته نمونه مأموران توی ایران برای باز کردن قفل گوشی بازداشت‌شده‌ها، نیازی به GrayKey و این ابزارها ندارن؛ زور و تهدید راه ساده‌تر و دم‌دست‌تریه واسشون!
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/ircfspace/2638" target="_blank">📅 19:42 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-2637">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">پروژه Nexora یک پنل برای مدیریت چندسروری VPN هست، که تا ۲۵ کاربر و ۱ نود رو بدون نیاز به لایسنس و با تمام امکانات پنل در اختیارتون میذاره و میتونه برای مصارف شخصی یا گروه دوستان یا خانواده قابل استفاده باشه.
نکسورا مدیریت کاربران، نودها، اشتراک‌ها و پروتکل‌ها رو از داخل یک پنل انجام میده و از پروتکل‌هایی مثل VLESS با REALITY، XHTTP و Encryption، VMess، Trojan، Shadowsocks، Hysteria2، TUIC، AnyTLS، Naive، ShadowTLS، Snell، Mieru، MTProxy و SSH پشتیبانی می‌کنه؛ در کنارش پروتکل‌های کلاسیک VPN مثل OpenVPN، OpenConnect و WireGuard هم قابل استفاده هستن.
از قابلیت‌های دیگه Nexora میشه به تانل بین نودها، پشتیبانی از CDN و چند آدرس برای هر نود، همگام‌سازی بدون نیاز به ری‌استارت، Rule-set برای مدیریت ترافیک، مسدودسازی تورنت، محدودیت دستگاه بر اساس HWID و انجام عملیات گروهی روی کاربران اشاره کرد.
برای مدیریت و نگهداری پنل هم امکاناتی مثل احراز هویت دوعاملی، بکاپ رمزنگاری‌شده، بروزرسانی خودکار و Webhook در نظر گرفته شده، امکان مهاجرت از پنل‌هایی مثل S-UI، 3X-UI، X-UI، Marzban، PasarGuard، Hiddify، Marzneshin و Remnawave رو داره و از زبان‌های انگلیسی، فارسی، روسی و چینی پشتیبانی می‌کنه.
👉
github.com/nexora-vpn/panel
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/ircfspace/2637" target="_blank">📅 19:26 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-2635">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/tC061WigkhKzq1ESmVAsQmzX2cXeudliBr3pCcwPnXwMIwcL-velqCl_nzdBLqjkwYBY3CbSVC5bOhoqKgxgdwCxggvkE3cumO81F4ZQWQHYel64VMi21XS0pIghej2KX2ggNA0dmerRoGGxwb_Sq-4XxsJnjdWo8snP6a9k95lUIuESTqj1wogigySUNEcVJMrKFisFAIxPn3sOhqY97il1oGMD890g7sMofjEQW6oUGNLiwnlwSu817_7q-fT8pfhHj7qtMgmp2qhyE_QlQRSHcaA6TPYIKMbfuwiAZtqupEikH-zT99T0hjKL_OsTbj_qZ7KHRzxOYV7nX_IROw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حساب رسمی مایکروسافت در ایکس با بیش از ۱۳ میلیون دنبال‌کننده هک شد و مهاجما از اون برای تبلیغ یک رمزارز جعلی با نام $Clippy استفاده کردن.
هنوز مشخص نیست چطور به حساب دسترسی پیدا کردن و تحقیقات ادامه داره. مایکروسافت هم اعلام کرده هیچ ارتباطی با این رمزارز نداره و پیگیر اقدامات قانونیه.
©
theverge
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/ircfspace/2635" target="_blank">📅 19:09 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-2634">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/XbB63_hGIiXKTkpP79nB90jNwVfxidoEMHwxB-f3u6bDr2fNZ77s-bz_TRioauZmC_aUtrlZ0Y-urr9mrjT_sXA13PuDmPSl4SAZcOz6Tivh7_Hg6zXDI-NVSjxd3A8Ji7obFQ_NEX6VJImoDmkE8EST-GuqDdXMnjjrivipGkQjmNL1xKKONckbdfB9CI5U7BS2SqBOKcXJeVzedUenipGDSfMvRK47wg_PUr4LM064onqf2uXu_zc5dqnzVyol60I4lhpKe5bsNTNZ-eIPl1QZlpNMt1Z-U8Nd-C_Ses1IPeW62OtKxYhELWXjHtISxwMokSzrqniH9kFP8pfUqA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کلودفلر میخواد تبدیل به یک مرجع عمومی صدور گواهی دیجیتال (CA) بشه و در قدم بعد، گواهی‌های جدیدی به اسم Merkle Tree Certificates رو هم در مقیاس بالا صادر کنه.
هدف اصلی این کار آماده‌کردن زیرساخت وب برای دوران کامپیوترهای کوانتومیه؛ چون الگوریتم‌های فعلی مثل RSA و ECC در برابر کامپیوترهای کوانتومی قدرتمند آسیب‌پذیر میشن. MTCها کمک می‌کنن گواهی‌های پساکوانتومی بدون اینکه حجم و فشار رمزنگاری روی اینترنت به شکل شدیدی زیاد بشه، قابل استفاده باشن. کلودفلر گفته هدفش اینه که این گواهی‌ها رو از اوایل ۲۰۲۷ وارد محیط عملیاتی کنه.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 44.2K · <a href="https://t.me/ircfspace/2634" target="_blank">📅 18:57 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-2633">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/qT-aMpiUH2suui1h7Q1Q-Qxl4nXPmHymJfPzrusoI3nLz1sJrWeDpHgKocaaWmpQZiSalHVgT2veZndk_dpTyURoGeDwcuW7qRSn6SvGZHIPjmhv7kSyG89I5j2dnZ_1WDRYRIvg3qL9aHIjNN2NAgX7inCB_x8kj8GhtfExELYOT71hLBl98WBgFyiFTo4zIbUhAhpRG_wgfsxcW5eQ9CPKwljCxI-75ILjta1zR8w1bgUbQGBcJw0X_Mr-PkhggPW6V02en5bE-eoiUpMR5mz_MhnTDBdc8uy6Q1SQ0Ak9E2saCaEIC6zubhf4Xnk-NafpFuXnZejNq8DYd8t_iA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اگه از TeamViewer استفاده می‌کنین، چند آسیب‌پذیری امنیتی با شدت بالا پیدا شده که در بعضی شرایط می‌تونه به مهاجم اجازه دسترسی غیرمجاز و حتی اجرای کد روی سیستم رو بده، که مهمترین مورد CVE-2026-92370 با امتیاز ۸.۸ هست.
فعلاً TeamViewer گفته شواهدی از سوءاستفاده فعال یا انتشار کد اکسپلویت عمومی برای این آسیب‌پذیری‌ها ندیده، اما در نسخه ۱۵.۸۲ این مشکلات رو برطرف کردن و لازمه آپدیت کنید.
©
bleepingcomputer
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/ircfspace/2633" target="_blank">📅 19:03 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-2632">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ihvNZW2alpF1r2wfDNVq3NmEvyZhPHdjLVD8xY2qlwiL9OfBIdGBsKIUhY2YOX-n1gR9uOQdqYOmX_ZcQLESAXF2_lDgNry0UJaxY7Gf_7eqBe5EpBIeAMnuLlPt-OahWAmOkBNF_jK1tZWq4JQw7u6ZxSsWar7T7YRbwGVpq5GMpl88UVjGe9MOymaet1H4Z2FdPx3buv_iXdnjxgCYzrDNLl6Nc_a2dtZ_jIptFtHBYA6cz3fVQb9ZbHp4WTc54nyhwcUwkZIKShLNUjoqtyFnnI8LAtBfFGXuRU66vuDjel-thV5_rAlxj_IU6_TYD_Q6slC87yDl8xpsyDc2nw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ج.ا در سال ۲۰۲۶ رسیده به راهکار ماه‌های پایانی حکومت قذافی در برخورد با مخالفان: قطع سراسری برق!
©
ArminSoleimany
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/ircfspace/2632" target="_blank">📅 18:56 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-2631">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/rhjV7PCn_5oZ2yhgWg9--T0RrcOMjQO2rWAQD9TG-fKu8MBgvYGIl7OD2LmT0VL6RO9lSnnXtXkTCb24q3PF61onlURC2NyUzShGuaepjH59ESP197H8zA8TlglYJUI7zRYY10hcuj9iAAeWZubS9nqfwvoOA9DcPtOGhP-56cW8FFNRSxgk5JMi8Os8WjvB27g1MBa-9OGzsaNfHfNAWsj2wvwCJPLOmSOA-fg70KYmeyZ7_TLcNA269o8du81Ck6YjAakKHHzg7nCFkUyvtaRnS9pQsu0XPKk7Ch9_aEctqxEHaVReDNJjiBF5jxBUN1jx4_DL6dRe1mXMbgxhCQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نتیجه این و اون خبر چند وقت پیش در مورد تغییر شرایط استفاده letsencrypt می‌شه گواهی ریشه داخلی و پایان بازی. از مسائل فنی اجرایی صرف نظر کنیم، بحث‌های مهمی باقی است: «حریم شخصی» و «امنیت».
در کشوری که با مداخله در پیامک احراز هویت ۲ مرحله‌ای حساب کاربری مردم رو تصاحب می‌کنند و پاسخگویی هم در نبود قانون و ضمانت اجرایی نیست، امکان جعل گواهی برای شنود به خصوص برای موارد بدون SSL pin هست.
©
Hamed
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/ircfspace/2631" target="_blank">📅 18:51 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-2630">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/LqkHzuGTPRnOmAUG2BUYIk8zNDlGBQ1RRW7L2NYBV9LZzauvL_v-Xqqq8Vi_ddO7qb4jV0Et9W904lQlqm9T_fZxjpdY9b5JwQDQTVxJr34xQVTJJ7-Tbse-kWDkN6fkDM66AdRyRCeR24lHCwprv55FnXphe1tHTVUlXrXuPEkjG4v0naOogi88u5i5on5moiveO4JL_dPxw6tXuqXLoPnqMlW-eCjtTQQ1QPAixceTzRfYXNr_I5rjfsgmQDtaJJs6_1wiBcbXoD4kGV_M2hWMX12PuNv61QleEQgHzadCKrk8jmBcqA5lzpxHXCnbspbL5S4BY_zZBafDqorRNw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">راهکارشون برای مدیریت قیمت تتر چی بود؟
نمودار قیمت رو غیرفعال کردن!
🤡
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/ircfspace/2630" target="_blank">📅 18:46 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-2629">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">کاربران در چند روز اخیر قطعی، ایران‌اکسس شدن و اختلال مضاعفی رو در اینترنت تلفن‌همراه و ثابت گزارش کردن و میگن آشغال‌نت چندروزه که شدیدا اسهال گرفته!
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/ircfspace/2629" target="_blank">📅 07:37 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-2628">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/XVEb6wuyOw1mZr1K5saUhrVbUBXIaw_D5LHQvHUZeNrKEcfo3h14XFd0xM7zuwcZgvlkftHT2uF6FtKvWd_fawfiscaO7pPMAxb0leY1jE8Q3tj5XAsV5IrwD9tzYqpg-Q16ctm-x0oA0OeuqpPDmz8KqbFu2eh3Zk8MKkUL09l_jZ72_AurZdWLl6JIvdcRGw23_KwYatYSpgqw5AmAz3TpgbCwapfdYyKLJfsUcfi1V2WHMYEkREwWWDIynIam7mB1EEAQUC1CiXlVpjaJiWMK7otPvXczD3bQo5D0bItqt1p4goQZFeoD6poaK2qCRbS7vYT0mJ3tu83zhfeDOA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">طبق گزارش Group-IB، یک بدافزار ویندوزی به اسم HEAVYGRAM شناسایی شده که از تلگرام بعنوان کانال ارتباطی و کنترل (C2) استفاده می‌کنه. این بدافزار از پاییز ۲۰۲۳ برای هدف گرفتن روزنامه‌نگارها، مخالفان و منتقدان جمهوری اسلامی استفاده شده و می‌تونه از راه دور روی سیستم قربانی دستور اجرا کنه، فایل و اطلاعات بدزده و حتی از صفحه‌نمایش اسکرین‌شات بگیره.
نکته جالبش اینه که مهاجم به‌جای سرور C2 معمولی، از بات‌ها، اکانت‌ها و گروه‌های تلگرام برای کنترل بدافزار و خارج کردن اطلاعات استفاده می‌کنه. Group-IB در گزارشش ۲۹ نمونه جدید از این بدافزار و ابزارهای مرتبطش پیدا کرده و با اطمینان متوسط این فعالیت رو به گروه حنظله نسبت داده.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/ircfspace/2628" target="_blank">📅 21:06 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-2627">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">اتفاقات امروز و تصمیمات هوشمندانه‌ای که برای مدیریت اقتصادی کشور گرفته میشه، کله هممون رو خراب کرده احتمالا.
ساتوشی می‌تونست وایت‌پیپر بیت‌کوین رو خیلی کوتاه‌تر بنویسه: دست به دست هم دهیم و دستگاه چاپ پول رو در
ماتحت
بانک‌های مرکزی فرو کنیم.
حالا تقاضا رو سرکوب کن، حساب‌هارو ببند یا سلطان فلان و بیسار رو اعدام کن، این باتلاقیه که خودتون درست کردید، توش دست و پا می‌زنید و ازش خلاصی نیست. این وسط، عمر ما هم رفت سر ایدئولوژی شما.
©
GrizzlyBTCloverr
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/ircfspace/2627" target="_blank">📅 20:16 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-2626">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/POUw3n2emEwqhxFtRy-jBawyQDnybrxatLBQqyVCkrd4rQ1Zc-vhPy_TQ-LM_MKGrMShD5JFFEN2X0sXsRfpM6soLfvbUG8NaQZ5y9H6PoI8IXHJDVMY6h41Y5_q9kA1PbnH-9taEPClJnYhIb-eBGA9ceSMHJnyIAXVZQTDYz-yTlTAOTdg_rwHVq1l8grHRGOcbrPNRQEMLr1ojNyKqVzju7P2o_DHDeYT_9yGHskhyUpEMiPcqO-0jvpO3RBTNZSwj_jLOWFWaz_n6iMk_xJyBRAvgLJ5LR2NEBmEStNbxbUN5SR4TOxdeRsZeWKPxK6UAd4cJNK8Wpkj5I0vng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اگر از دیوار چنین پیامکی گرفتین، ازش بی‌تفاوت رد نشین!
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/ircfspace/2626" target="_blank">📅 20:13 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-2625">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/dpwcw7PdfeE9iubwX_z6E4D9AzNH3yRnPyKtZLbUccCwDIQM0j7E-GOJ9KPwfCU3Sa7mKgjO0M7DD5mfVnnZF_iY7omX2uybziqQAJMFm08Ofhl9cY3hqlIiF29b_V25ja7T4g_1M1XzGtGz-Ttfw696Hk5eJACDuc9qD--MHjOwuY8GWoibhZNqgxIHXvKDbrOwGm--TowopXs1TB36-gLjDf-bMBVyv74L2HOYu-BvOkEbcw7LAJrvQx8P8HVMU3JX1fljnjQNC-G9RnuAPi3cGi3CvPF5T77oYuiKwrkJ9k63-cCzZeild3PGtogLSbuYvsP4KjcCcqwSdiobdQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پروکسی تلگرامه؟
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/ircfspace/2625" target="_blank">📅 20:09 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-2623">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">مجموعه‌ای در حدود ۷۵۰ هزار رکورد از اطلاعات مرتبط با کاربران صرافی ارز دیجیتال والکس مربوط به سال‌های ۱۳۹۷ تا ۱۴۰۱، در فهرست فروشندگان بانک‌های اطلاعاتی غیرمجاز مشاهده شده.
این داده‌ها شامل اطلاعات هویتی مانند نام، نام خانوادگی، شماره ملی، تاریخ تولد، شماره تلفن، آدرس، ایمیل، اطلاعات مرتبط با احراز هویت و همچنین اطلاعات مالی از جمله شماره کارت بانکی، شماره شبا، اطلاعات صاحب حساب، آدرس و موجودی کیف‌پول‌های رمزارزی و سایر اطلاعات مرتبط با کاربران است.
افشای این اطلاعات می‌تواند زمینه‌ساز فیشینگ هدفمند، کلاهبرداری مالی، مهندسی اجتماعی و سوءاستفاده از اطلاعات هویتی و بانکی کاربران شود. به کاربران توصیه می‌شود در صورت فعال بودن کارت، برای تعویض آن اقدام کنند، نسبت به تماس‌ها، پیام‌ها و لینک‌های مشکوک هوشیار باشند و از ارائه اطلاعات شخصی خود به افراد ناشناس خودداری کنند.
©
leakfarsi
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/ircfspace/2623" target="_blank">📅 20:05 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-2622">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/d3mmQuI12QEMubqKGwA6enzOPTqErccIScDfb6snZhCucy7Lkmu1sXJfEddS-dqya64SJjNxdAJiwogCaoQEAnvZnaWy5FOvRNlPuzST7qDetosMTlURdrJGI2BmIh8lYJ7ubuvPL3jDyMt8Hr5jQLxckIfDxY_eOX1WZj83sHG-bVpcQmL3XRDKcQhF8YTb3NyARaTwunCjeSVmZQkMqergqXwtgfaT9aG1gaTvPHm5SjCPww1d8FpK-iIuqVH2KKIV_S9J-09sa93ASiEDgw5jSoHFuQfKWVrCbkF5nTLZCPDsDbmg70pC9YMwzBTnjwoljcVktAVu98TFJosyzg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">معاون وزیر قطع‌ارتباطات گفته "فراگیری استارلینک میخ آخر را بر تابوت حکمرانی فضای مجازی می‌کوبد".
۸۸ روز اینترنت رو قطع کردین و نگران حکمرانی فضای مجازی هستین؟ بابت ده‌ها هزار خونی که ریخته شد، باید منتظر کوبیدن میخ آخر بر تابوت ج.ا باشین!
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/ircfspace/2622" target="_blank">📅 19:59 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-2621">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/s0o8AIf9aw3oO3tEfXWbgWAhX9MQNT0KDLeyWhOMJs_QsdT4x8ZdBr7xTrzRkG0JAVyWDYNp1AFVR_ohW56M_JRToluNX28vh4PiQsSn0UYnXbVXjisPmDOdEQEHZgd6AMfU0EAQkXwaFTXQdEAA92ni4NVO26FNnlTqhZ0W9Len6R1RAB2gV684rwnIclZ2tHZ_Qda8ER6Vh52ZbYLFgDU7DpCjE1HubZbH-96Dv5xtaj5OTtSgwI7LNopekTguK6_cgrF7PRvFI-2Nm-x-57VvEkXl0rNJNzPdrprwj8BFXmugE92rEhz52F73fdwPFE-psDCMTkn81yL8e36H2Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بانک مرکزی با ابلاغ یک بخشنامه‌ی رسمی، ارائه‌ی هرگونه تسهیلات بانکی برای خرید طلا، ارز و انواع رمزارز را بطور کامل ممنوع اعلام کرد.
این بخشنامه بر ممنوعیت مطلق پرداخت تسهیلات، چه بصورت مستقیم و چه غیرمستقیم، تأکید کرده و مقررات یادشده شامل پرداخت وام از طریق شعب بانکی یا بسترهای دیجیتال برای خرید طلا، ارزهای خارجی نظیر دلار، رمزارزها و همچنین فعالیت در سکوهای مبادلاتی مرتبط با دارایی‌های دیجیتال می‌شود. /تسنیم
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/ircfspace/2621" target="_blank">📅 19:52 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-2620">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/KGGjjFOrLzIetpHKC_GZj9yX2f9L9PeTzqP0rmYumOioS3yshp8Hm88cfEHr9X0yYrjY6VH9Yr-kLIexdZhpqPVPWtwUTGz-y6ythZMHpW-1zcHW2WOjPWBo7Pu5cUUuC3EQbBpxtA90CoBQJBr55iQkT7GgBCAtRQu7ffsG4qg2osD6ZfUNzf_3Rm_dD49B64BZ-aIoUIL5L0sSh3ki6BYjeCG2Fkuq_amMRhH-8_-u32fx5Gf9NePdfzoSyPttXI_KGSEoFgDeC5ToJhEZOIT1193NFdDqfGNwxwH2Ix64szVjr7wXHcEbNTURhHLvZBFev2GQsebNMMyoEP_5Pw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شرکت تتر به تازگی اعلام کرد "به مسدودسازی نزدیک به ۵۵۰ میلیون دلار دارایی مرتبط با بانک مرکزی جمهوری اسلامی و شبکه‌های تحریم‌شده کمک کرده".
الانم با عبور دلار از ۲۵۵ هزار تومان، صرافی‌های رمزارز (با دستور مراجع) معاملات تتر رو از ساعت ۲۱ تا ۹ صبح روز بعد متوقف کردن!
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/ircfspace/2620" target="_blank">📅 19:47 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-2619">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">هم خبر تحریم ساخت ایمیل برای ایرانی‌ها توسط گوگل قدیمیه، هم خبر مسدود کردن ۶۰ اکانت مرتبط با صداوسیما توسط گوگل.
فعلاً اون لجنی که توشیم هیچ تغییر جدیدی نکرده
😄
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 37.9K · <a href="https://t.me/ircfspace/2619" target="_blank">📅 07:48 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-2618">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/mRzp5dg1MfJI98haqrR_ykxNoJBINrsxcWj38iEvWkicPIToIQJI2QIk4E9NLW3kuF7Af7zDmlHtFFMDEnfCrNPShZhEzOfv6VqiHDusUeAaGpFZiwceYwI-Oa7RJTe_osV2uxfBa1oAWqaslAPhl_k-niH86vJw069RIbOOsrzGdUKxPQEHOxPkfLuEZVDrNQXOicE7i3jvmEtXBkwvnFTfQowz8e6dz3TkybgLyF9yGRE7h4twN9bTui9mUAh-MoMDB3j0XfPRJEgQFGOvJ0MksCd639ITVYC1P73Se8Jp5AbgnfQqyrhb662xAFrqmco8s4CO8T3V_T-ZTf9wgw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اپ sushTun یک کلاینت متن‌باز و رایگان برای هسته ایکس‌ری هست، که از پروتکل‌هایی مثل VLESS، VMess، Trojan، Shadowsocks، Hysteria2 و WireGuard پشتیبانی می‌کنه و تمام ترافیک سیستم رو از طریق تانل ایکس‌ری عبور میده.
یکی از بخش‌های کاربردی این‌برنامه که برای ویندوز، لینوکس و مک ارائه شده، مسیریابی هوشمنده؛ تا بتونین مشخص کنین ترافیک ایران، روسیه، چین، تبلیغات و دامنه‌ها یا IPهای دلخواه از تانل عبور نکنن. امکان تنظیم DNS، فرگمنت برای TLS، Multiplexing و چند قابلیت دیگه هم وجود داره. حالت کم‌مصرف هم اجازه میده ترافیک‌های پس‌زمینه سیستم مثل Telemetry و آپدیت‌ها مستقیماً به اینترنت وصل بشن و از پروکسی عبور نکنن.
👉
github.com/soroushdeimi/sushTun/releases
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 34.8K · <a href="https://t.me/ircfspace/2618" target="_blank">📅 07:38 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-2617">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/K3afJhDMA8OtQ-K8igjotHygfr-6zJqdfBsSjCWIR7-y9eXGg3AzRpgRAwU4U20lOqkITeKC3KwIzk4FCbTH2-EEkhQ4VyNjdQHuHiSvOw5MZe_-E01x-9mSfDrKJdkyyuWeNZTmEdQSNWd9ZMZik52S6fcwSo6MIEKOM95UScUL6LRY4okZNauxLMO5dopdWWZWSRWd1k_HrvcRxKusVvc0lQx27YFNkaw61CrEiD3f8R1kfbTDetvlzRJcGHgintXFGWvOEDnjkRmrQqhCwooNRGVQeB6idVyT98f2NSo-rMJfJRp_EwnWYdaRMFxHfj8RYfwb__jVlI2UjIhCLw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کلاینت Satelite یک اپ پروکسی متن‌باز و رایگان برای اندروید، ویندوز، لینوکس و مک هست، که می‌تونه بین هسته‌‌های sing-box، Xray و mihomo سوییچ کنه.
از وارد کردن انواع سابسکریپشن و کانفیگ گرفته، تا Rule-based Routing، پراکسی‌چین، DNS هوشمند، System Proxy و TUN رو پوشش میده و یکی از قابلیت‌های جالبش، حالت Multi-Core هست که اجازه میده چند هسته همزمان کنار هم کار کنن؛ مثلاً سینگ‌باکس هسته اصلی باشه و بعضی پروتکل‌ها رو به ایکس‌ری یا mihomo بسپره.
انتخاب هوشمند نودها، تست تأخیر و IP خروجی، مدیریت DNS و Hosts، تشخیص اتوماتیک پروسه‌ها و اجرای دائمی در System Tray هم از دیگر امکاناتشه.
👉
github.com/zn0wii/satelite-proxy/releases
💡
github.com/zn0wii/satelite-one/releases
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 36.2K · <a href="https://t.me/ircfspace/2617" target="_blank">📅 07:44 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-2616">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/pGWXQW2O9p8NBYHwMOvmYxIH6ocLciS3fdDEWJWXcQ6GFOmzowLMU8EYJSqVm_eIPVZoDD6229myeYNxVuqS_g5V58EeHW-ct52sjwcEpEVIkz76q4H2zZfZN3NZlbD2uTNrB5vn-vhJFSXCQFYrKSfQp-b2GYwuZz9UnoH1dNxsrFID5GNeXVD05f66m9c9rLDm8UObRSu1VlXIMjOTuLaOps2SSwd_L8LH2FShCEf9eP3jYcjz_6cGFP5e84mFL_6r156yMHYyebm0VKw7LhlZKb6nuHlveJX_HLBziSXchPDXTSAKJ2HGk5lQHBq2XbPPR9D19JZbqkipsIOJHw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جمهوری اسلامی فقط دسترسی به شبکه‌های اجتماعی را محدود نمی‌کند؛ محتوای حساب‌های شخصی را هم زیر کنترل می‌برد.
شماری از کاربران با انتشار پرچم حکومت نوشته‌اند که درباره فعالیت‌های «غیرمجاز» توجیه شده و تعهد داده‌اند در چارچوب قوانین جمهوری اسلامی فعالیت کنند. پیش‌تر، انتشار لوگوی پلیس فتا در صفحات اینفلوئنسرها و کسب‌وکارها نشانه توقیف یا محدودسازی آن‌ها بود. حالا انتشار این تعهدنامه‌ها، نگرانی از تبدیل حساب‌های شخصی به محل نمایش اطاعت را بیشتر می‌کند؛ جایی که مخاطب نمی‌داند آنچه می‌خواند، انتخاب صاحب حساب است یا حاصل فشار بر او.
©
filterbaan
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 37.7K · <a href="https://t.me/ircfspace/2616" target="_blank">📅 07:38 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-2615">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">معاون سازمان تنظیم مقررات و ارتباطات رادیویی گفته "حجم‌خوری نداریم و بخشی از ابهامات و برداشت‌های کاربران درباره نحوه محاسبه میزان مصرف ترافیک اینترنت، به وضعیت ثبت اطلاعات محتوای داخلی در سامانه تعرفه ترجیحی مربوط می‌شود".
خلاصه: حجم خوری ندارن، ولی باقی چیزارو قول نمیدن!
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 31.8K · <a href="https://t.me/ircfspace/2615" target="_blank">📅 07:34 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-2614">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/s2NcM5yLKXsDnjBllkygy09efxnDgk_84bJ4kBnMuwlvNOfw4aIBARAs7EXiGuGuNMF3NuKHPl6lJYW7dpQQslFRDCVxENyn9ntOF4z6QGvd1qPC4ISaP32M8kMFUQ7xfkO2GVGRoNb11xsibIWeq-qs64dnsnSTU7-s5eCJLQSbPJSqSKpx2fIW5EmFmAL7NB36w4lkhMhkOcSztdD_houYV99kS2KgRiwf_fCmVbIJKxOfxgXfxECLR-jP6tLuFLnAFaNr4wZf6IZW4Dp4XFBw-6iByjNv5uX3FKGeTpMa41aAAW-ELXAIZABmThOj0ARyemJRZSM720EfJNjK5Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">طبق گزارش Qrator Radar، شبکه همراه اول با شناسه AS197207 در ساعت ۱۳ روز ۲۹ شهریور، بطور ناگهانی ۱۹۰ پیشوند شبکه رو اعلام کرد که باعث ایجاد ۱۰٬۸۶۵ تداخل مسیریابی با ۱٬۵۲۴ شبکه در ۱۰۰ کشور شد.
این رخداد که بعنوان BGP Hijack ثبت شده، در ۲ مرحله اتفاق افتاد؛ مرحله اول حدود ۸ دقیقه و مرحله دوم حدود ۱۵ دقیقه طول کشید و حداکثر انتشار اون به ۱۰۰ درصد رسید.
وقوع BGP Hijack میتونه باعث قطع دسترسی، انحراف ترافیک، اختلال گسترده و در بعضی شرایط شنود یا دستکاری ارتباطات بشه!
البته در این‌مورد مشخص نیست که بصورت عمدی بوده، یا خطای فنی ...
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 38.3K · <a href="https://t.me/ircfspace/2614" target="_blank">📅 08:01 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2613">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">بانک مرکزی نصب «گواهی ریشه داخلی» روی دستگاه مشتریان را یکی از راه‌های ادامه خدمات بانکی مطرح کرده است!
اما مسئله فقط رفع هشدار اینترنت‌بانک نیست؛ اگر این اعتماد در سطح کل دستگاه ایجاد شود، می‌تواند فراتر از سایت بانک اثر بگذارد و در شرایط مشخص، زمینه رهگیری ارتباطات رمزگذاری‌شده را فراهم کند.
مرورگر زمانی گواهی یک سایت را معتبر می‌داند که زنجیره آن به یک مرجع ریشه مورد اعتماد برسد. اگر کاربر یک ریشه داخلی را به سیستم‌عامل اضافه کند، دستگاه ممکن است گواهی‌های دیگری را هم که همان مرجع صادر کرده معتبر بشناسد.
خطر زمانی ایجاد می‌شود که آن مرجع برای یک سایت گواهی جعلی صادر کند و مهاجم نیز بتواند در مسیر ترافیک قرار بگیرد. در چنین شرایطی، مرورگر می‌تواند بدون هشدار معمول به واسطه اعتماد کند و حمله «مرد میانی» امکان رمزگشایی ارتباط را فراهم کند.
نصب گواهی ریشه به‌تنهایی به معنای شنود نیست؛ مسئله اصلی دامنه اختیاری است که به آن مرجع داده می‌شود.
البته راه کم‌خطرتر وجود دارد؛ اپ بانک می‌تواند فقط برای سرویس‌ها و دامنه‌های خودش به یک مرجع داخلی اعتماد کند، بدون تغییر فهرست اعتماد کل دستگاه.
پرسش اصلی طرح بانک مرکزی همین است: برای حل اختلال خدمات بانکی، چرا باید اعتماد یک مرجع تازه احتمالا به ارتباطات خارج از بانک هم گسترش پیدا کند؟
©
raaznet
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 29.6K · <a href="https://t.me/ircfspace/2613" target="_blank">📅 07:52 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2612">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/CyM0ggzdAKh5_HyssgalBAwupLK3Q25SLOghgnJFuacBQRivGW4Vlfz5Wpv7I3ruRWacF27rPrwFEnCcBQOgqT8d9igBvSeYP7QPYtjTnLMebCzgEwEnC69L2VjwSS9t8fI0PV3gxF7Uns89MHMaJTbWgQXHe8Hwe8EB3kc666XUrjWlwcZ9S-0haqtPmmSBVor0j7uC5XHLRw6g_BGW25awIxllmUhGpY4mLUj03XKCR3iXEJqatsx7j5aEIm9BGsJkdz9fBGkTg4L9qG9-sLx4n9S8HsmEi_LfqOPdBk0fXBlEozUFPFiXDVtis9A12Ml1IWXlEQ7OV02BsY8HDA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مراقب این نوع هک باشید!
یه صفحه جعلی شبیه Cloudflare میگه برای تأیید ربات نبودن، Win + R رو باز کن و Ctrl + V بزن.
چون شبیه تأییدیه‌های معمول کلودفلره، ممکنه طبق عادت انجامش بدید، اما در واقع دارید یه دستور مخرب رو اجرا می‌کنید.
©
milad_joodi
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 30.5K · <a href="https://t.me/ircfspace/2612" target="_blank">📅 07:45 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2611">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/BMolkjeVXW96P_WINnmhV1Mbx5nw4kwPyoroxZvZZmFZWf12Xe4x2qXBYHAMYXdqeaBm8uTkc8LQeAhwa0Xh9SiWO-6IN7ESkmeUvrHTJlwD4wPMccej63_3zcPO_zwD7Y640zQyj8Duh1vK4zy1UOWdZbFCALDg8uKWdkqeYZz-oZupXyTMTzCQbEwgG5O4L5HU-nxZeg_U-HSWvTjgiE2xmBLgYxKcCsnt8ZhouswdTNLCEueAA5TZjaTFJGHSWa_beoA7KM67vDAsLesh0kN-CY_ALGQxlyAh3BRht2ijjrkc8rESVuZhNdixRRh2BPjwWzlTsl09e3TnmQsL9w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">زپتون یه موتور شبکه‌ی جدید، متن‌باز و بدون وابستگیه که با Zig نوشته شده و برای کار با رابط‌های TUN طراحی شده. ایده‌اش اینه که ترافیکی رو که سیستم‌عامل وارد TUN می‌کنه، مدیریت کنه و اون رو به ارتباط‌های TCP، UDP و ICMP تبدیل کنه؛ بعد هم ترافیک رو مستقیم یا از طریق SOCKS5 در اختیار برنامه‌ی دیگه‌ای قرار بده.
پروژه Zeptun امکاناتی مثل پشتیبانی همزمان از IPv4 و IPv6، NAT، مدیریت DNS، مسیریابی خودکار، فوروارد ICMP و پردازش چندصفی TUN رو داره و برای Linux، Android، Windows، macOS، iOS و FreeBSD ساخته شده. طبق بنچمارکی که روی یک رانر گیت‌هاب گرفته شده، زپتون عملکرد بهتری نسبت به Sing-box، Hev و Tun2socks داشته.
این مدل هسته‌های مستقل، می‌تونه برای پروژه‌هایی که نمیخوان تمام شبکه و TUN خودشون رو به هسته‌هایی مثل سینگ‌باکس وابسته کنن جالب باشه؛ مخصوصاً با توجه به اینکه استفاده و توزیع کدهای پروژه‌های دیگه می‌تونه الزامات لایسنس و کپی‌رایت خودش رو برای توسعه‌دهندگان داشته باشه.
👉
github.com/Noisemux/zeptun
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 32.9K · <a href="https://t.me/ircfspace/2611" target="_blank">📅 08:20 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2610">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Pitky-guk0Mj55d-p5-YtlcJZvToIOKUvd_3R4hcpyDYDm8_r9AonOHXdvu_BQU12eGoOTDubib9Ln75OBBHjZIdTuyhltpwLyiHOL-_vLWBpccS11Q1VJVyyiceYFU5pEOYghKxlwJ9GgDaftJetgx7gU3QLBhxwXVQBXZeOcN5r6CNvNLkH8JyjhhH5KNu_PeswgGRksuB1r7pyAJCGw4piRYDM-q7P4n-sEvo3UUtCYkiX_UffRuno7134pygZWt3L8uIE7x7C6JgIIYTPxM--rDNMNzxMS5qwoyklYS7nbEVpob21Ihdgy7D2jAnXFwhzHIfYwqBpNz1KgTBBw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وای، چه گوگولی
😄
فرمودن "مجلس بدلیل پایین بودن کیفیت دسترسی، با افزایش قیمت اینترنت مخالفه و انتظار داریم وزیر ارتباطات از حقوق مردم و افزایش سرعت و کیفیت اینترنت دفاع کنه".
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/ircfspace/2610" target="_blank">📅 08:11 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2609">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/MX8Bf4pTT_qRX6sKdwKiTThOdA1cPmIb7yYP11UfhFSU35hn13Zfl3q_5QkSUG5kKT1gRvXR9-T-hOCG5peYR9pDc428D9YVzOgORsQjlFQ8dekbQNzx7b8KfqeRhPBQLrxnG3C-4WwufVNLI7bS1TPIyG2nv8vres8pEf0pHAA4ddhVPbRLamB2OwCCmhPnc7F-av1_82xDqsEMHCnJPUJV7ROemv7MZa25c2CgmFL4aVW_TwRsAfwRzKU5EuiYnclrka0qldWVnS7zwLc1oUD0CJ0acIREFwDhIL5ANFAwbXvka-DbsNFrbRJ-xp0q_E7SZJnSquZDvFbECXVr9w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اسکریپت Google Flow Helper برای اجرا از طریق افزونه مرورگر Tampermonkey ساخته شده و کمک می‌کنه محدودیت‌های دسترسی به Google Flow برای کاربران ایرانی دور زده بشه.
این اسکریپت درخواست‌های داخلی Google Flow رو زیر نظر می‌گیره و وقتی به پاسخ مربوط به تنظیمات و محدودیت‌های سرویس میرسه، یه فلگ مشخص رو پیدا می‌کنه و مقدارش رو از false به true تغییر میده. بعد پاسخ اصلاح‌شده رو به خود رابط Flow تحویل میده؛ در نتیجه فرانت‌اند تصور می‌کنه اون قابلیت برای کاربر فعال شده و محدودیت مربوطه رو اعمال نمی‌کنه.
این ابزار VPN یا فیلترشکن نیست و خودش محدودیت شبکه یا فیلترینگ اینترنت ایران رو دور نمیزنه. آدرس
flow.google.com
باید از اینترنت شما قابل دسترس باشه. این اسکریپت بیشتر برای مرحله بعده؛ یعنی وقتی به Google Flow دسترسی دارید اما خود سرویس بخاطر محدودیت منطقه‌ای یا تنظیمات سمت کلاینت اجازه استفاده از سرویس رو نمیده.
👉
github.com/maanimeisam/Google-Flow-Helper
💡
telegra.ph/Google-Flow-Helper-09-20
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 32.1K · <a href="https://t.me/ircfspace/2609" target="_blank">📅 07:59 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2608">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/NqJo4kuydwm5GYoKbp2blKp9QkdA-QjTUUeXcx_gwrmLlWRUoKCF9tNuKxFfXhL0yOSHlaozqxS6d8_usDzc7U1mcB7suORDsA3hEvZAo582xZv0vCnj7PvxdQG1inLoz0nmsryKOUzFqW72HJha1haOsUh4DBvG2xTWq5Af_L0yP7LUTi6QCXFUzXAhSV0JOcNgnrgNMAlwRIRlk3Q4IsyeggCC3pclwzNuvxuMkgoyCTnvJnVEs57M30JXWbj7ghANPlZ_jn-3JpSB47dgiMRR-hIBQQ6OKMEI2SyNUFG8AyAX26-MKzhMCENZuAurIWd0KvCZBr8lZuMYlTOg5w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تحقیقی از TechRadar روی نزدیک به ۴,۸۰۰ اپ VPN اندروید و iOS انجام شده که نشون میده تعداد زیادی از VPNهای موجود در گوگل‌پلی و اپ‌استور، اطلاعات شفاف و قابل‌اعتمادی درباره سازنده و سیاست‌های حریم خصوصی‌شون ارائه نمی‌کنن.
در این بررسی، ۳,۳۹۲ VPN اندروید و ۱,۳۸۷ VPN آیفون بررسی شدن. فقط ۶۱.۴ درصد از VPNهای iOS و ۴۰.۸ درصد از VPNهای اندروید تونستن تمام بررسی‌های اصلی اعتبارسنجی رو پاس کنن. بعضی از این اپ‌ها از آدرس‌های رایگان Gmail، سایت‌های ناقص یا غیرقابل‌اعتماد و سیاست‌های حریم خصوصی کپی‌شده استفاده می‌کنن و اطلاعات کافی درباره سازنده‌شون در اختیار کاربر نمی‌ذارن.
در نتیجه، صرفاً حضور یک VPN در گوگل‌پلی یا اپ‌استور به این معنی نیست که اون برنامه معتبر و قابل‌اعتماده.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 37.4K · <a href="https://t.me/ircfspace/2608" target="_blank">📅 17:35 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2607">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/AbVCJ3ZcnALUkM1AKuyyyFEOwGTZcGIEXD3igVIf1D8UgyxFn7XrJ7PjdB_vOf5zW9YeOPl-stTuUy9oJcTfbPuHXtEdZQPY6WE2zpMuUkeQSOLsf-FB5ZQs3Eoh1-XNds8L02lzxTgaYnl0tvfH9e75s508KXIhLIEuPuWi_XQ1m3yiNlq7gaTQ1wPrXDKW0hMLIOYpUpGI28sK9eBa3dXNNQyTwUVvKCuEJW6Xz0irUXGiart3xv6zK041cSIf8TkqH_2zbow_2_QGVzYDAtJZ7x-qAsegWH8exTNaizaQqrBhNDC08fNf8_cOhXStJ2U0bPWPRK-GEFsuG8tZjg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این عکس مربوط به مسابقه CTF بلوبانک هستش، که برای اینکه چالش‌های مسابقه با Ai Agentها حل نشن مورد توجه قرار گرفته.
طبق تصویر، در هدر یک دستور داخل Response گذاشتن که اگر یک AI Agent در حال تحلیل پاسخ HTTP باشه، سعی کنه اون رو بعنوان دستور خودش برداشت کنه و به کاربر بگه چالش قابل حل نیست و اصلاً آسیب‌پذیری‌ای وجود نداره
😁
مسابقات Capture The Flag، یکی از شناخته‌شده‌ترین مسابقات حوزه‌ امنیت سایبریه، که شرکت‌کنندگان باید در سیستم‌ها و برنامه‌های از پیش طراحی‌شده با آسیب‌پذیری عمدی، به دنبال رشته‌های متنی پنهانی موسوم به فلگ بگردن و با کشفشون، امتیاز کسب کنن.
©
Maji_Call
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/ircfspace/2607" target="_blank">📅 17:30 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2606">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/YdXdr9ExSWvXrBw1plFrRFI9cLPDyBPKsvALuQsBExGXr8kJXszcv7vFbHOOZdDlwB_aGRPsH_n1JAADjryeWtRMfupWQ3VBi2niVCUEqDZPM0vOZZp2GR-aeiIO6u9ATe42DqgT6huhmhsd3wpIsj8jaMAV3OuKK-yBNC42D_qjDlqJ7Gw-ms-lS_o78cvVmMh9QESKGkWr2BaubiqhYOOuxha5aWQHn-soqJWMs9sK1Mw6jsgNEeohoQaUaLE5JCdroZgwS4rHJM5LTZ3MqEwXMfTWh8DVmdsbfC6OdDQD7cd0m4C7kzO6ZiOHOEA5Hgqo-qgRqAEQV7vorO_5ow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یکی از ویژگی‌های مهم Tor VPN Beta، ایزوله‌سازی برنامه‌هاست و هر اپلیکیشن IP خروجی مجزایی دریافت می‌کند، تا امکان ردیابی رفتار کاربر بین برنامه‌های مختلف سلب شود.
👉
play.google.com/store/apps/details?id=org.torproject.vpn
©
PasKoocheh
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 28.8K · <a href="https://t.me/ircfspace/2606" target="_blank">📅 17:12 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2605">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/mP-IgTDwKmkxLUXqUaj_WVW2rUBCTi4qCtPe-shK5Qk3V9bCHye308WTwEtsR6_KewiIogM1nsrcbnno-fBbZFouVXgYRFLXWS7Wvza8BQPjtCib__h6Bjv0cmjJfHV6p9-E-heARww2p8ZStJcW8ipwN9cACpyt8kyhIaRKx5X85f73pjteVV7o30_aSIJrSTwnslCiU6LGrGkTSPy6ldr-w5qCuPPiO4JpvcY70bXjzrkYHrHPH4drv6XN8kBfpyk0aQsHGiN0KK47RE_RSnGU4nnC8zdZ5kOuu-hOKJiu1U5AQ1JrTBTFnoKqGcGTau5l3gvNXqCjHnKL3RxE1g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کپی میکنید حداقل اسمش رو تغییر بدید :)
تصویر مربوط به نسخه وب ایتا هست.
©
Ralireza11
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 32.2K · <a href="https://t.me/ircfspace/2605" target="_blank">📅 17:08 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2604">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">ایران در جدیدترین گزارش اسپیدتست نه در رتبه‌بندی اینترنت موبایل و نه اینترنت ثابت حضور ندارد.
تا ماه گذشته، ایران فقط از رتبه‌بندی اینترنت موبایل حذف شده بود و در بخش اینترنت ثابت با رتبه ۱۴۰ جهان قرار داشت؛ اما حالا در گزارش جدید، رتبه ایران در هر دو بخش حذف شده است.
©
itiransite
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/ircfspace/2604" target="_blank">📅 17:07 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2603">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/pqz9NwFlFSCGQGHvDAJJ9sEcrgrZrMbZDo_G9q6czBMlLEzKOAnlTjlhwb9h2zvN1jONfqp4NxVJfL1hsnzQI4cYemM-nLcy9RTNBucjVbXutJPcoYdL5Y2hTisTWfmYXse8lS_hFHao4u_wwpzC1imYF1OWvm27A_wf-iTITFoFbASp1fcLFlu_rV8NUrDs5oobymFgz4qibHDqyCOr5Km4IjyFRF2sN5pX-Ntk4Fq_Rr-xnP21HksQHN3ZwGeMzIhKI57OcSj_iQLvb-mS6B2GtTzKG5aeZHHOTMk1S9i27pVVv0I258ASlFtaMv581ndFEQu6WZbctnZC1TlQsg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">صرافی رمزارز کوینکس اعلام کرده فعالیتش رو متوقف کرده و کاربران تا ۲۲ دسامبر فرصت دارن داراییشون رو برداشت کنن.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 30.3K · <a href="https://t.me/ircfspace/2603" target="_blank">📅 16:51 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2601">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ToMDS5mYlWP_lTN9dU6GKYqJOZzP4Uo55xOZ4ovW3da31xSRrcon-OoEPoMhDV99FvwnAeareRPLrMbgCvUiw3_ZVJbOhnHfU1WEbw7vs1g9Q1VqACCfpUe-wYuEzmDNqdXRLtQZph6G7CPxyCuiWaJxBMQr2G-HS8nLY3OyZAg97qgrF8RyBcoUXf42aMhetBROYbjotIxzYrwSTnQNtGNn1UwCSTLY6NnnudJL8-W0V3eItJFLM6r1zg3mE04kF3dYQn9Q9LZPZHnx6rJAilMcqe4TWNCC_7JyM8LY1EUBBrQbook-gLaqGpTh6PU2vXoyvE7rQjnElCT1s_mFig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">توی خبرها
دیدم
که ساکنان روستایی در منطقه فتح‌پور هند، در اعتراض به کیفیت پایین و ناپایدار اینترنت و خدمات تماس تلفنی در منطقه، یکی از کارکنان شرکت مخابراتی رو به یک دکل 5G بستن.
امیدوارم برای وزارت قطع‌ارتباطات پندآموز باشه!
😁
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 38.9K · <a href="https://t.me/ircfspace/2601" target="_blank">📅 08:17 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2600">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/CoY2prUUpNA2U1u_MS1Yvq5UDyPbf4KwjYrGVqa1h-Xqnqt2Zrl0XCup0rAQDwnCKERZMy_DEBwnQznVXhjhle-ZqtRrDScN06IRum2oEPwpGPLu0DfH-q9EicPRwx-CfZTWO9DYGdWhyxZ-_b7onOgWgRIw1tN6QfII5-y4TWZIWiakOTzaHq4tNC-WsFHCcA01T0QUoVDLf5I6obRCdN-QuHYZmAue4j6pBr5i4VUR1uF8kyLONV1g6MBRJsjxBL0ebxQK_mv4KJnY-wGXSlEYtEUosL9l4y9_IkyiNLPxGNVtq-DDa1WrGKdOFSqpO0vdsW-sYINwuvLdS-EFxw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزیر قطع‌ارتباطات سرشو از برف بیرون آورده و گفته "اگر درباره محدودیت استفاده از IPv6 مصوبه قانونی وجود ندارد، دلیلی برای اعمال محدودیت در این زمینه وجود ندارد و موضوع باید با سرعت پیگیری و تعیین تکلیف شود".
به مناسبت همین دستور سریع، فوری و قاطع، از تصویر پیوستی اکلیل باریده.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 33.8K · <a href="https://t.me/ircfspace/2600" target="_blank">📅 08:09 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2599">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/HcxCsLJ3TXWJPGgsyGpu_RbO-saTp5grXstsiYfim9-Q7Rx63r8A5gaMRcErblLCkDfmx7gW68Ng38My1U3ahRWDeWxllrewTQMKHQn6UObFOygscp-EYaS1T-5DuMp1MHR-YE_GYA5PXZ33pr5evsglwW7hGnn_AUlKDPTXEHNrpZ-14yWEeVwD_VtWKsfFKNcQCA38yZLaVL-IvF0TiXOWTzFw4gs3e3E_qCF2D-jDjO7FHseYdiYcFx7NCBN1coKgj0QFl7v4Q1B1abIELlC6iHWxgHXW8R9UkF9a3mGQD8qSn98bOsle7aajfs7v8H7HN87EUhKOmJjmSH6rHw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نسخه جدید از هسته متن‌باز و رایگان Aether منتشر شده و این بار Tor هم بهش اضافه کردن. حالا می‌تونین از تور بصورت اتصال مستقیم، اتصال Tor از طریق وارپ و حالت معکوس استفاده کنین. پل‌های Tor هم بصورت خودکار از BridgeDB گرفته میشن و Aether می‌تونه پل‌هایی مثل Snowflake و WebTunnel رو امتحان کنه.
یه قابلیت جالب دیگه MASQUE-in-MASQUE هست، که در واقع دو لایه‌ی مسک رو پشت سرهم برقرار می‌کنه. این حالت باعث میشه برای خروجی، رنج آی‌پی متفاوتی نسبت به یک اتصال MASQUE معمولی داشته باشین و توی این حالت دیگه آیپی ایران رو از کلودفلر نمی‌گیرین و رفتار اتصال تا حدی شبیه متد Gool میشه.
👉
github.com/CluvexStudio/Aether/releases
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 44.3K · <a href="https://t.me/ircfspace/2599" target="_blank">📅 07:53 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2598">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/nNbjXfc4-KzCAIUK985F7Pbkzo2M9QxOSv0qE3A-djkyNujqKsrkKcpOTbVtyhXJilrM_fYVphrZ8i-T4JKo6mmJTITJbHVaSFCSnJuNpP_A1H71P9d_BF4cP97MyGYGDDi2AAOCMpAaW-Ryh3synRI9_H8GzdgpzoYymGcvGC82lFD9zMeM4-5P4DldAhgZGGWCtDJm_HfBEvPLR3ofBPEBr9hHlVqAwaMreKcwe4ZmOn_eOU_Ke72F4ADuFFfWAmszRIeREs8_frARAe9nqzXuNRsLimJ3-o8VWUbeQ5avgoIcgGfEqs8u9VsOE5UMEsGLP5VKqqnn3akiytquGA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آنتروپیک، شرکت سازنده Claude، در گزارش تازه‌ای درباره سوءاستفاده از مدل‌های هوش مصنوعی، چندین عملیات مرتبط با ایران را بررسی کرده است. در این گزارش، ۴ عملیات مستقیماً به جمهوری اسلامی نسبت داده شده و مواردی هم به سازمان مجاهدین خلق و یک عملیات فیشینگ علیه کاربران ایرانی مربوط بوده است.
در یکی از موارد، یک مجموعه مرتبط با جمهوری اسلامی طی یک سال اطلاعات ۶٬۳۸۸ ایرانی را جمع‌آوری و پروفایل کرده و برای این کار ۱۵۵٬۲۱۶ توییت را تحلیل کرده است. در عملیاتی دیگر، بیش از ۵۰۰ کانال برای جمع‌آوری اطلاعات افراد داخل ایران بررسی و ۵۱٬۹۴۴ پیام برای ساخت پروفایل‌های روان‌شناختی تحلیل شده است.
استفاده از کلاود به تولید محتوای تبلیغاتی محدود نبوده و از آن برای جعل هویت، پروفایل‌سازی، توسعه ابزارهای نظارتی و حتی ساخت بدافزار و ابزارهای فیشینگ استفاده شده است.
©
RaazNet
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 37.4K · <a href="https://t.me/ircfspace/2598" target="_blank">📅 11:15 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2597">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/bkQe74Meem_dxKP0cj9nkPLSVAQH2pID__zZvOG-7y6ZaTExuMKNJBHOrux6Q8MAAKMrHDLbYgBKeNCkvaO2XuFp_YiolZXplHFYyeyHGo-ADxdCMr2vsZa-ANhLcMV9bJF2hVJAwKpjz8glJhZOUIQl_X8U4jCXG_ove7XfO4OA6ISqjGd02sUXG29UuYvkzhW-jFRHVuWTLFmnH9NivfUSEaZtTASveqhWqvf3LwpLk8aPj2IpSxREMboCpNjKx3kf0frQkuYtIgrNXvBQN5pzC-Womd0zUjDmYN1UNHooBnbChHUd1fLt7eH4VLHmj4wOvRQInhgP0QPixg4NuA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">معاون علمی رئیس‌جمهور گفته "۸۳ درصد رتبه‌های برتر کنکور در ایران مانده‌اند. این موضوع نشان می‌دهد بخش قابل توجهی از استعدادهای برتر کشور در داخل فعالیت می‌کنند".
البته نگفته ۸۸ روز اینترنت رو قطع کردیم، هزاران نفر رو در خیابون کشتیم و خیلی از همون‌هایی که کشته یا سرکوب شدن، از استعدادهای برتر همین کشور بودن.
نگفته راه خروج از کشور رو برای خیلی‌ها سخت‌تر و پرهزینه‌تر کردیم، عوارض خروج گذاشتیم، ارزش ریال رو در برابر دلار به پایین‌ترین سطح ممکن رسوندیم و انقدر محدودیت‌های مختلف ایجاد کردیم که بخش قابل توجهی از آدم‌ها اصلاً امکان رفتن پیدا نکنن.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 37.2K · <a href="https://t.me/ircfspace/2597" target="_blank">📅 08:00 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2596">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/eezjxPs6ZQbH6JCHCBkjtprXKwxMT3ABPacf_1JXxchfS2cGmSrVwdQtx0U2sb38MtvlmE-eT_G5d7FtiokvmkRGcV1EFwDr5YcWZoRMcPf4iKsY-enE6Svmk7Co0hUMu57vvbvB1J_JRZLac5xRcdAiOKzy6UITAZUwfW-Ur5f170yOwqDywXdPmqH6-xOXe4ECQv1uLThoTNzCi2bMr3TKAbKK7_qC1eDKbCl_1Qp_CHBk_u-fshSu36jn7Y9QTFXp6OKVO1-8_aJ-B8S4jg1LeSDVJgUR9rtPZkN4HS7foOlUvLOrmj5hWhfEQ3Gja_b0EAp96Kl1T7rR7s3T2g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دیتابیسی که ادعا میشه مربوط به کاربران فیلترشکن JumpJump هست، توی یکی از فروم‌های دارک‌وب منتشر شده. منتشرکننده با شناسه leakhunter ادعا کرده این مجموعه فقط شامل اطلاعات معمول کاربران نیست و اطلاعات شخصی و نسبتاً حساسی مثل اطلاعات پرداخت، اطلاعات کارت‌های بانکی، تراکنش‌ها، موجودی، لاگ فعالیت کاربران و اطلاعات دستگاه‌ها رو هم شامل میشه.
البته فعلاً نمی‌شه صرفاً بر اساس ادعای منتشرکننده با اطمینان گفت تمام این اطلاعات واقعاً متعلق به کاربران JumpJump بوده یا اینکه کل دیتابیس ادعاشده صحت داره، اما درصورت صحت‌سنجی، همین اطلاعات نشون میده جامپ‌جامپ ظاهراً اطلاعات شخصی و جزئیات مختلفی از کاربرانش رو نگهداری می‌کرده، که این نشت می‌تونه برای کاربران دردسرساز بشه.
اسم JumpJump قبلاً چندین بار در گزارش‌ها بعنوان یک اپ ناامن و مشکوک مطرح شده بود. بنابراین اگر از این فیلترشکن استفاده می‌کنید یا قبلاً استفاده کردید، بهتره موضوع رو جدی بگیرید و حواستون به امنیت اطلاعات خودتون و افرادی که باهاشون در ارتباطین باشه.
©
hamedvpns
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 87.2K · <a href="https://t.me/ircfspace/2596" target="_blank">📅 08:14 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2595">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/etwdplUBnJdRcBrgaCoWJc0sTPnGtq2YtODVRC1Y3Kms8UldBNFRYt5XI26EE1z5bhQOgAcQqmxSTtSZeVB0ChznOQ7gRHdxeDPoVUc87NKtgoAQNLI4EIHxt-hF0l7FKzng9Lea3Zy7svJSR3poFDoyxwPy6m43EwtGrcI8eqkHBo2ObnmHexvlUbtQ0peLwoQ1Ahzz04sFo_kXA_tfvI7tPkY8O5qtfrgzExz8zVLUDo2MleTgYfUjHk7A455Y_VHde9-woMbMU68yvmv8JDiU-hxDd1ataD-aDWULHWoNozKgUM8g4E48A7EX9TmAOSvOL2u1Az6sMZx3vuUc-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شبکه پایدار است، یعنی به همون آشغال‌نت قبل از قطع فیبر نوری در ارمنستان برگشتیم!
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 35.5K · <a href="https://t.me/ircfspace/2595" target="_blank">📅 07:57 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2594">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/voKEeIi78KXSAEqHTSSCRR3puG3fKM6MxNW1lnsRys9GtwUU2lNRdhVVx09vbtMfXBMC4hbUeEWZuldkkspMjfzCO3FzUbbQ7crE0T1riQ47u2qoggVEAE7yTSt-pkji7h7J9beApAMJiyBYKGfuTwaqZO00OOpfG5EVo7TIa6joUWDm8o6zJVGcv3pNkDB1tMLgg9mCWfJ8OhTukAs7kUSd5TGtDefBxdacK1-f5ObYAUdkPiF-FY9-hAnY-3MJ_NHNpK6RbYyRTjEv5H1olQAGe-H5ZOhl1vhL2kUlreOQMdTOlXpgQoUkcVRCKdhF9hW0I-rX7MB6YMd-cvmFJA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بعد از مدت‌ها وقفه، بالاخره فیلترشکن Oblivion به مسیر توسعه برگشت.
در این نسخه که برای اندروید منتشر شده، هسته برنامه از وارپ‌پلاس به Aether سوییچ کرده، تا امکان اتصال و دورزدن فیلترینگ از طریق متدهای وارپ، گول، مسک و سایفون فراهم بشه.
👉
play.google.com/store/apps/details?id=org.bepass.oblivion
💡
github.com/bepass-org/oblivion/releases/latest
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 38.7K · <a href="https://t.me/ircfspace/2594" target="_blank">📅 07:49 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2593">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Gnhqab_Bq4Pv-juL1h6f_rD_jNb952cVOslxRNDXd11ey64t-p-WZ1fGS2_gOP__jdB2KKFgrlpvwWes7fLCXvtn1btxEmV70VEalGRu-kWg-m64p-gNlBJST3NLqnh2eGlfXKVMmsvKYUT8tpUwXnOpt1qydTrNAts-j0fGybQr_6R7PcN3_ytHiMnuoP9K4ZeveGMKj_H0uokDAdzX0h1SpIMQyUPLCePn5ke-V0tKpfGmdsrePdg0NUCXDtY23NKCrFZN11jY-dTD-4QiUAy_M20nwDgEYRbwKyrZKRgkEKwadisomlbcW97OR8swkB4s2gPH8z0aZC5-yFGfVw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">گوگل یک آسیب‌پذیری روز صفر با شناسه CVE-2026-85046 را در موتور V8 کروم تأیید کرده و هشدار داده که هکرها از آن در حملات واقعی سوءاستفاده می‌کنند.
این نقص ممکن است با هدایت کاربر به یک صفحه آلوده فعال شود و مهاجمان را قادر به اجرای کد مخرب، سرقت اطلاعات یا از کار انداختن مرورگر کند.
لازم است پس از به‌روزرسانی، مرورگر را حتماً دوباره راه‌اندازی کنید.
/فیلتربان
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 29.6K · <a href="https://t.me/ircfspace/2593" target="_blank">📅 20:10 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2592">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/sjVcH6yXlpcu19v5gUh-GypuwT50cLcd2p_njzCTNvsU5pO3udelvAAjqm9DqpmVXsKzDS1F-EgFNKU1nGthp7ANlyBfhJhOLNYF4AY8c6hTBelkwkSulQzYnSZNko7DQqLEi08EAOWKfRWDre2Qc-Fm5gILkRlyqsQZlKjVJ8O7wDkMS964NUmPPNwMJzyJpDteVukBDSpyQ-V_axh53njkWee58gaILnpHMHAt_OiQAfwzodJKX7AKoHTrgRh9WxbkR7aRGr_F6ox1tU3a7uD2JTLjmnu4KChkeMdwGacPzc80kczBmnYTkJooWCTVpgFmbn1DSvhqOzgJx_K6MQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دیفیکس اعلام کرده که این فیلترشکن توسط تیم امنیت
پس‌کوچه
مورد ممیزی امنیتی قرار گرفته و تیم توسعه درحال بررسی نتایج و کار روی چندین بروزرسانی کوچک و بزرگه، تا در کنار حفظ عملکرد و تجربه کاربری، کیفیت و امنیت برنامه رو بیشتر بهبود بده.
این تیم گفته ممیزی‌های مستقل و همکاری بین تیم‌های امنیت و توسعه، یکی از بهترین راه‌ها برای ساختن نرم‌افزارهای امن‌تر و قابل‌اعتمادتره. هدف این فرآیند، شناسایی و برطرف کردن مشکلات پیش از سوءاستفاده احتمالیه و انتشار خبر این ممیزی هم بخشی از شفافیتی محسوب میشه که به‌گفته دیفیکس، کاربرانش در چین، روسیه، ایران و ... که با فیلترینگ دست‌وپنجه نرم می‌کنن، باید ازش مطلع باشن.
💡
defyxvpn.com/download
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/ircfspace/2592" target="_blank">📅 18:53 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2591">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/NwfatTGXM55TW0-WAX71ZOJDfcDvDrqIBRqkQWQSolqGIYCs-c39Q2q_nTiSypq4aV_RrFRlzEKcQ7zozCGnZc5rwijkNifhYP1dStfdA8G6NOU7jB_Yx0BHoUoe-Fm_4RWdfVpaXdfglw0z9dwOhY6DFQVRXgvkPycxzAi7jodWYxpUJtNwyV4GRC-ZJ4EsPmHC_puujDcR9ZDmAJBwfINmbAUYNgAvZOiDJQaiE8mNyw7xBakeSy5vT0tDgflJZIMTloW3cXJ6PqkiR9hpdxsx_Y8GADrOOSa0OYpxhYs0nQBqnRaRx9up41U5R5tgjxMXk-BGf9f01UApjFk2Hg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اگه کد QR حساسی رو می‌خواین مخفی یا مخدوش کنین، نصفه‌نیمه رهاش نکنین. ممکنه اطلاعاتش همچنان قابل استخراج باشه.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/ircfspace/2591" target="_blank">📅 18:43 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2590">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/PrmbDXaPLC9fBjkTG2JRVHdP7haKBfyHAUdjMhyzylz9-iQaaOD_CbtNSBOpPLX265bR8HrzL7SUNzreRbW7Gx3J8ETGaFyPBG_k0uKJCbERRvvCQ1_L2ASuNXZ_cdzaO_iTdrlEk1PCirzh-nfidSw33muAhkIDzUj7La2nRuQG_IZjni-qur06o7lfA4GimPoPEAgyIHQnNs06diyHQUE94GRWRh_D9fWAnUv3Lm9qjef2I7FtoZay61Kyt5nJYXRaYMYHqFNi1T0yE2f6_y3rA1s2IDBkErmqQRerA3_nljrclgL97DY6CutA-Dv_aZFHDV0ZJhdU9k8_vD47Lg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سم جدید
😃
☠️
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 28.4K · <a href="https://t.me/ircfspace/2590" target="_blank">📅 18:11 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2589">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/D_Gun1c0ae7ZtCLD_EkKEiFMm9JNRNTaE-xjrRO9l_2XzQxQqaBH73ZHse-BBMIkYxFJztO3e853siLcs5IFYW5r-HkHsHhx2HXWsGT5zWCGszwvkmVdMa_rWY5a99Lw2qKO33JAGA0KLaIMqRRZl-LS37xE1g4R4ig1ZlmeRD9lIpcaEz8byZ8MpZaUkwpLXflfQ6yit-OCFy0q3-FJOob2YUQtzHhU6ecaZixG1tzI6i-55zap7GSqdhV9NDwuYPheCpEqpBSQvmfmsDTOre8_G2ZVsNI6UEMnLtsaoBfabD4ZvYPyVVZ05BSYoxAOiY5WgHICC0QhKA1abMlcTA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزیر قطع‌ارتباطات معتقده "قیمت
#ملانت
به اندازه سایر کالاها گرون نشده" و احتمالا باید بیشتر از این دستشون رو توی جیب ملت فرو کنن!
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 30.5K · <a href="https://t.me/ircfspace/2589" target="_blank">📅 17:54 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2588">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/EiLKVJ4Po2y1Xm-JyEZKjDfRmcVtDQhSnblZ7mRhZStFdQJHO-7k-aIfKSgHn2oNSBk0Gjepx4vSR3Z6eHLzPnV0oX-rlfJ28PMGg56GzrfXJJQizLxU0tt-cLl7ihcrYHCOIY5jiX5-imwBbBNms57JvVFlz5fo72bZwZraE1fCcj9vA4n37TkAp_13Gi3dP_MJmAjiSYIbrf5skLsR2IZBQAAeMotVf6ZfrVzmZI0qTGwn8u0XydlVljhNwvLIbUXNxHslxzLd2Joo_koLkO-YzGDA47Z0Q-lx9Ddgby83wBTl9TbOIGBQI5dZ9n-BRTv2_R48uI2DV969qU-pLQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">واحد امنیت تیم پس‌کوچه در ماه‌های اخیر حرکت حمایتی قشنگی‌رو شروع کرده و اپ‌های VPN متن‌باز (که در ایران مورد استقبال قرار گرفتن) رو تحت ممیزی امنیتی قرار میده.
طبق آماری که دارم گزارش این ممیزی‌ها تا الان بصورت محرمانه برای ۷ فرد یا تیم توسعه فرستاده شده. اکثر این اپ‌ها درحال کار روی بروزرسانی‌های جدیدشون هستن و بیشتر از نصفشون آپدیت‌های کوچک و بزرگ داشتن.
این‌قضیه تقریبا برای توسعه‌دهنده‌ها و جامعه‌ی هدف برد-برد هست. اون فیلترشکن‌هایی هم که نسبت به مشکلات گزارش‌شده بی‌اعتنا باشن، به مرور از چرخه اطلاع‌رسانی و توصیه به افراد کنار گذاشته میشن.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 30.1K · <a href="https://t.me/ircfspace/2588" target="_blank">📅 17:22 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2587">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/e0zaXPUI3MCUH7jjg7oZYA9o5haQCxZnRRYoszG_FIuIa_KBGh3hswhjRdwOcXcMxJaD6TqeT7ndad90PI4g8nsNgGgSy4unhphRZqB0Of6FEy4HQQqELpTuCFctDVWGt4LFubKfO-RzjPtbqDLhHiFvnfoG_g5G01fWT5X9EC-MQE3wdJ4pMx4V0JLmgsqaNcvaTYsZV9xxrIG9cLukpJ5dJMEPIXJBd88wmoxiDA4MIPWlTRs5MZ4Dj0yj1jk8Qhx_qJCjgKng2rzOVI6cDsZ-ATghxyMlFUsR6cX472XQzr4WzIrb0sJ0D-Ic23b_ISJlRdUOBWz02uMwaOU6bA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مجلسی که خودش کارت قرمز داره، به وزیر قطع‌ارتباطات کارت زرد داده
🤡
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 29.9K · <a href="https://t.me/ircfspace/2587" target="_blank">📅 11:41 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2586">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/j1upI0_tQBPB5wsv3NIw4PCYr85lueVGfjHrpdWn7qNTZreHwp9uzm46N090AY9YXwtniYi3tAUYLjo2TnAYfd3jXR9bnOSZ17KIwS3ITA1M0oKV_yNFrDKBAPClg5ukmFczioQwQwtpQevZ20_ANdXR9Koe9tEk5KML0ZbW0usigP3ap78el8UIhaknXzygu3e2ufnom4oxamCygO54DdRBMrTYb6J1zN5lrc6H93e0YeqN1NAQF2YdW6omKTaq73nrNVUT1ZsExtq8fCbX_rq0MnjevLdBktdIrOaaL7b_v28mHH2HxOxzUhmdejHkeq2D1_6ZV0kWtsCGFmAHmg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">معاون ارتباطات و اطلاع‌رسانی دفتر معاون اول رئیس‌جمهور: طی ساعات اخیر اخباری کذب به نقل از اینجانب درباره رفع فیلتر اینستاگرام منتشر شده، که کاملاً ساختگی است.
/اقتصادآنلاین
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 33.5K · <a href="https://t.me/ircfspace/2586" target="_blank">📅 09:11 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2585">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/AHts_CLxjzPikEgVCtJie4Mvao4wL5abtUhXzVX7gujpVpJCcGof51NAkpeFvJ1kmeTCblZhU_vk7UMsi234WhVBWuF7r_a_XMvlrpxwe7_d3BGvmU3FcAz9pOlwTeh4p7ZkhjDbj7vs7eJIisNyJxNlFsu5Nui1CXobHzm3KMJaodlM_L-HxPpHst5Ku_ACvumsnoHXciPGvAW2fSArNzfaJ2yx5UDDqhV4giNjUgIKYdoJG84BG0Ig8gRhRH_dWEHhfu4loeay2wS5C00bVmKYGY6fes5dSPFjtU_wZPBW9hmAPvfxS1sX4lrmZ59l_LJofrU3XdQzPx10UNPN4A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کاسپین یه ابزار رایگان و متن‌باز برای ویندوز، مک، لینوکس و رزبری‌پای هست، که دستگاهتون رو به یک هات‌اسپات مجهز به VPN تبدیل می‌کنه تا بتونین فیلترشکن رو با همه دستگاه‌های خونه به اشتراک بذارین.
کافیه لینک VLESS، VMess، Trojan، Shadowsocks یا Hysteria2 خودتون رو وارد کنید، تا ترافیک دستگاه‌هایی که به Wifi کاسپین وصل میشن، از تانل Xray رد بشه؛ بدون اینکه لازم باشه روی تک‌تک دستگاه‌ها VPN یا پروکسی نصب کنین. درضمن اگه تانل قطع بشه، کاسپین دسترسی اینترنت دستگاه‌های متصل رو قطع می‌کنه.
👉
github.com/Iman/caspian/releases
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 31.2K · <a href="https://t.me/ircfspace/2585" target="_blank">📅 09:02 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2584">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/kp_P5v_-r6NTlhgcVf_o1FIPYBPvwMdjofJcnZjgGvNSE7Rak0jY_nmld50uS4I2bngB6_l_U4h3HeO1r5rK8Zq3BdTo7brK_KfBzQpal_ZB7GslS0lvPXOO2GchhU4oEWC7IwUBobEP5cZgtlJz1E5cUhiv9bLA2ydQgNOA0DOXZH_7v6gLJztV7RTf3hJIs8US2imvRHhgVjZrBV47Ahx5DiPKTPpbGSiddZsm1bcxGr9bQEfQIVAk8320bBCaDcHvAcLED-cMUuCG0z6M5WiAolNhqg0lkX-u5IpGyro9tu6D1KUYIYm1PHN919vpmJjK3OYouCdy4mxRZPH9qA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اپ Misga یک پیامک‌خوان متن‌باز و رایگان برای اندروید هست، که به شما اجازه میده پیامک‌های اسپم، تبلیغاتی و کلاهبرداری رو بصورت دلخواه فیلتر و مدیریت کنین.
این برنامه چند فیلتر داخلی برای اسپم‌ها و کلاهبرداری‌های رایج داره که می‌تونید نگهشون دارید، تغییر بدید یا کلاً حذف کنید و فیلترهای خودتون رو از صفر بسازید. با Filter Studio هم می‌تونید با Regex یا متن ساده، قانون‌های جدید تعریف کنین و حتی از هوش مصنوعی برای ساخت الگوی فیلتر کمک بگیرین.
👉
github.com/mirarr-app/Misga/releases
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/ircfspace/2584" target="_blank">📅 08:53 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2583">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Jtg2eeVM6lCVx0Jh5BpdAD7dePzTYtK1DG51Ht_YkZmhf4ZvOfYTa-ULmh9AvrG2y6C8gc-cOhRDg8xZq4paRDRHRqVMyJ60tKxzc3iDQOwsi7-EOzpvJUypWDm24wLJFqOUvt5x1xXL0ndWDQozhfr5CVyk5OgsSn1ggyKf_FHa__0at29M_Ev0jSSz1MAzTQIX1VusMwP0YLZiixUgaRIzBiv8gzvjEPMBqxdLAWZ3maHPV3Hff4WedNm4fuaWoGYqmiaqD4LWUvH8l0qg9gArKnL8lHqoMK0_pYGyGqmQ3hKraL_ZBJL9HEFNL5QHv5OoTCdU6Bs0gfHvKqQQPg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چند آسیب‌پذیری بحرانی در RouterOS پیدا شده که بعضی از اونها در قالب زنجیره‌ای به اسم MikroTrick در حملات واقعی هم مورد سوءاستفاده قرار گرفتن و می‌تونن در شرایطی دسترسی کامل به روتر بدن.
از طرفی Shadowserver در اسکن اخیرش بیش از ۱۲۲ هزار MikroTik با SSH باز روی اینترنت پیدا کرده که حدود ۳ هزار موردش مربوط به ایرانه. این عدد لزوماً به معنی آسیب‌پذیر بودن همه این دستگاه‌ها نیست، ولی نشون میده تعداد قابل‌توجهی از روترها مستقیماً از اینترنت قابل دسترسیه.
اگه MikroTik دارید، حتماً RouterOS رو هرچه سریع‌تر آپدیت کنید و بعدش لاگ‌ها، یوزرها، Scriptها و سرویس‌های ناشناس رو بررسی کنین. SSH و WebFig هم بهتره مستقیماً روی اینترنت باز نباشن.
©
PingChannel
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/ircfspace/2583" target="_blank">📅 08:40 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2582">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Ax800FX2q-0I3zi0UzfDlKc56A2BnY91Mt3hn2Pc6NAl43YuRVf74TkR4cGhInjiluDBwpKuUg7mpzmaAdp59KhMHmI2qn2WGH1ieqGsOG0yQI0foVE13p0xD5hFgzSLK3WEcFdLpQLSsa_CBNi5sF4EDwgJtcIYh-zTuVsCFLZVeWJyPnr3o0G-dA_TudPHr-uakntXlRXzMum-I_FZ0JOV_v4ObxFUTGvdryGUeYcyZLhrnJxtVhgQzYxx_mGDSb5jhCmD89BXkTX-tAuiVIM1DcepbEi1_PeoN6Jf1XuW6J28amKpFpDXKL61GLzD5x8sOZ8GYxqfdlQar6oKTw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">به نظر میرسه یکی از زیردامنه‌های gov[.]ir به افراد دارای مدرک فوق‌دیپلم یا پایین‌تر اجازه ورود نمیده و حتما باید لیسانس داشته باشین
😁
©
SePeHr
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 28.9K · <a href="https://t.me/ircfspace/2582" target="_blank">📅 07:39 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2581">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/oIhu2-JzgG4e15VB-FjLV6MM1IsNak1i_wzbeOJpmYkesuk0Alr90vnV8vYQS3fGwlgOZETRBPNy7OZJ3aTooev6uoCtO_W_nqO7c5mxDjYX7q5rFZKnNAT9SKSINjXKihEIyF3yXZn8DOdwsMHeV7t4YeSivZPbG-YbVKz7VHvP406AeayJsE0hN1PJ5jL-PuH8UdvZQClOdiSG-qsgM4uLnm8_lNERSALcR0913KYlJ4GD8MluHrM-LIJNY_a89R2hwA2ho5COLlMxJz_FJtjxALjuKxAEhxOf9UB3aCC_fKGSSRfjr75kzK7GlmTW1dLvWICqxvjoZVEfZEnfDQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فیلترشکن متن‌باز و رایگان دیفیکس اطلاع‌رسانی کرده که امکان تغییر زبان رو در گزینه Diagnostics & Experiments مربوط به بخش "ترجیحات" این‌برنامه قرار داده و حالا کاربرانی که به چینی، روسی و فارسی صحبت می‌کنن، می‌تونن DefyxVPN رو به زبان مورد نظرشون تغییر بدن.
البته این‌بروزرسانی بصورت آزمایشی از طریق گیت‌هاب در دسترسه و بزودی از طریق استور هم در دسترس قرار می‌گیره.
👉
github.com/UnboundTechCo/defyxVPN/releases
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/ircfspace/2581" target="_blank">📅 07:17 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2580">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">ایسنا خبر داده که
#قوه_عاقله
بخشنامه مربوط به "ممنوعیت استفاده از پیام‌رسان‌های غیربومی برای اطلاع‌رسانی رسمی دستگاه‌ها" رو لغو کرد.
😄
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/ircfspace/2580" target="_blank">📅 07:10 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2579">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">حکومت در حال تهیه لیست IP کاربران و در قدم اول مشتریان دیتاسنترها است.
در این طرح شماره موبایل + شماره ملی + آیپی به هم وصل می‌شوند و بدون ثبت آیپی در سامانه شاهکار، دسترسی به اینترنت ممکن نیست!
نقض حریم خصوصی کاربران و حق ناشناس ماندن در اینترنت با قدرت در حال اجراست.
©
souzangar
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 29.8K · <a href="https://t.me/ircfspace/2579" target="_blank">📅 06:59 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2578">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/nJTvki_E-NV7jE5BbO6mHCQR9n3QGr9uxwBq51iY6tDptSam986qI_0m4Lx9wXCrXbTIyKUiDqQcONLavMGsdGWg7XW3pwAtKAK_yaY0XoLxgmEwZz9EjaBlPTrRBBWIsuSHUJS1ZAsItIO0to0zkKd9BLSigfaIlGZHh702ZdRPWjbqGYUb0AuwSlPP4Bo7-WorT_z65mX4y7tzcMhB9-HMYAPYzTNbuoB0ADjGIMGqPNi5XepG4jCeqR3gTq6UDSTa4jI-pBb-__tEhfaN6X-aALXgZmSq5fBqt3x-p1P2heT30JjMF0hSPil1NKeb_KhO0eW5lim92iBpjhGLGA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نسخه جدید از هسته متن‌باز و رایگان Aether با تمرکز روی بهبود سرعت و عملکرد منتشر شده و مهمترین تغییر، فیکس شدن مشکل سرعت MASQUE روی HTTP/2 هست، که حالا با اصلاح پنجره Flow Control، مسیر ارسال، فریم‌بندی پکت‌ها و MTU داخلی، باید در شرایط مختلف عملکرد بهتری داشته باشه.
از طرف دیگه، محدودیتی که بخاطر بافر دریافت TCP در Netstack روی همه ترنسپورت‌ها وجود داشت برطرف شده و این بافر حالا بزرگتره. ضمن اینکه می‌تونین مقدار بافر دریافت و ارسال رو بصورت دستی تنظیم کنین. البته برای WARP-in-WARP چندین دستور جدید هم اضافه شده، که اجازه میده اندپوینت‌های مختلف رو بصورت دستی مشخص کنین.
👉
github.com/CluvexStudio/Aether/releases
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 30.4K · <a href="https://t.me/ircfspace/2578" target="_blank">📅 09:57 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2577">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ZYcrkewkVRYXH38iWvjnhNqprJlWdW1CgATYzotZ_f2jxbIADi9zBl2LCBVMVNzvfsu8XP9rRF_dvwwiwL1b9su8TyQsvWs1hIXH19rK6k8ah1WybXqH-Wp5WTJmGIKFIPl2PnKKtfCoOWqGqRSlFE4fBKHAXo_-JGEqf56Ie1FGPRAJcO36H4_ZSH6zyDg5qb0LnlLWYcyGf1OB3WTV9otNUj88rTCgS-xEhX_dbjQIT90Pngoy7y7hho0L-0ZJUPo6OmpTV0vBEzX-UmUokCjKn0C2tLLp_jisDRJbsE4YaIb8f92SUty5EMiEoKG_GcP_xNtfGVurImH6KAnLXg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزیر قطع‌ارتباطات در مورد ۸۸ روز قطع سراسری اینترنت و بعد از اون اختلال گسترده در سیستم بانکی کشور خودش‌رو به اون‌راه زده و با سیس عقاب اعلام کرده "آماده انتقال تجربیات سایبری خودمون به کشورهای منطقه هستیم".
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 33K · <a href="https://t.me/ircfspace/2577" target="_blank">📅 18:47 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2576">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/jsRkhGtBTCGHcD9II3EWxXZ5VVM1L9Nbc5omM59OfMM2BqUgxKDaMc4FcRpO_KX_G8EuvWU9gKQYCf_3BhErKsa7m7h_ohR6FDnNNcfdwuiFa3SVQn6ybbQUm4SzcciqnV-l_45Lvkp3IDLnZlxksOyn_jDGfp_ZjH570xT0r5yg614unnpOVvTa55yb9iPTFwQ80WVl8bf56tBiO4qZ3yfkWH8wPnoDJvZnSzPEMNBY8yFOZSzIeb9XB2IQuQMapDLv2i1qABYv9uK0KjJEs3h6VJh50lpiQUIK17plrka7j1HV8zIeZ9CxgQ_Gi5gPr26AGv90v40_2QUGbQUdbg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یه باگ توی واتس‌اپ اندروید پیدا شده که روی بعضی گوشی‌ها می‌تونه اجازه بده بدون باز کردن قفل گوشی، به گالری و عکس‌های شخصی دسترسی پیدا بشه. این کار نه هک پیچیده‌ای میخواد و نه دانش فنی؛ فقط فرد باید گوشی رو در اختیار داشته باشه.
ماجرا از طریق تماس ویدیویی واتس‌اپ و گزینه‌های Meta AI انجام میشه و روی گوشی‌هایی مثل Pixel 6 Pro و Oppo K13 جواب داده، اما مثلاً Galaxy S25 Ultra جلوی این دسترسی رو می‌گیره.
©
notebookcheck
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 36.6K · <a href="https://t.me/ircfspace/2576" target="_blank">📅 18:09 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2575">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">معاون سیاسی دفتر رئیس‌جمهور گفته "پزشکیان معتقده دوره محدودیت و فیلترینگ گذشته و اینترنت طبقاتی و فروش فیلترشکن به هیچ وجه قابل قبول نیست".
حالا حدس بزنین رئیس‌جمهور و رئیس شورای عالی فضای مجازی کیه؟
جواب درسته؛ مسعود پزشکیان
🤡
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 43.6K · <a href="https://t.me/ircfspace/2575" target="_blank">📅 18:47 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2574">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/VwfSijdOWIN5bHS9-bwqAVNtMSQmc1UVIMOqIjpivHwe6noJTJBF9v56IyBAOyiR4r4HhSrxsFDubuSs4j_ssAiK_56wJzxHYMBEFzdNM-qDdrJ61UtRm6hk3zATEOSVT_5CZT9iRo4DXGIM-24Q6uTi7dGTTb43M4fpPfEQzODayyMxhnBQPw_50v9_5hI1jaDb-P7kNQB4Q3KNdlUIelUblNz69yHCVDsAyPvHoBvkr5ghTLBYXjucFGfy-eqoFvK_r12Z9MoAEITNqaa_3ON7ISmgU5jNWiAdes-pJZQFT2bMP-QLmB7LoYBN1yHjXKYJMyVatxDSzq_KlTDZUQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اپ Echoes یه ابزار متن‌باز و رایگان برای کارهای شبکه و توسعه هست، که چندین ابزار کاربردی رو یکجا در اختیارمون میذاره. از جمله امکاناتش میشه به پینگ، اسکن پورت، اتصال SSH به سرورها، بررسی اطلاعات DNS، WHOIS و IP/GeoIP، ارسال درخواست‌های HTTP و مدیریت DNSهای کلودفلر اشاره کرد. همچنین امکان بررسی وضعیت سرورها از نقاط مختلف دنیا و مانیتور کردن آپ‌تایم اونهارو داره.
👉
github.com/SinaXhpm/Echoes/releases
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 44.8K · <a href="https://t.me/ircfspace/2574" target="_blank">📅 11:52 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2573">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/p2UyXOhJwDTsVHczpQvfq02B4D-MzI2DR965m_2QzecGKnMasUKpKGNYSQlO7vNSs8926Jdpp1r1lsQcl2If8h8JbkBfCPOwKfjOpIm9q2hIW4nNOksaUgQXdneL73tcaWLZgJgxteVOoOzVROKM2mvOdIQT25K29z2OkZdp8QJ2sBPMBjnVaK465FyPNdSt41kPIUFYwMxNaTmKTzKquqwRBmz_ZRZRJabVUK6Qd725Y1skVkP9npRo8XLv8VnjXWtqSB5S8Sx08vQgt45kF0noA_L8BOzZyr1qpsw_BZoR-78ICwLRUbSji9-5jnzSnIIH-ThQWujwBuLVcz1TCw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وضعیت بانک مهر ایران!
©
PingChannel
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 35.9K · <a href="https://t.me/ircfspace/2573" target="_blank">📅 11:44 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2572">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/sY8ckagbr4QlYcf8URy_SlwoOU98YRtTD96wqc7CFTFJP5K6yV47op2T8OOKxKB064q7nJ6eg82ibUWbVVfQ9YzEgPzdWSNZNqIP2ob79gIvuT0M6se2kaQEPjF4ooq28Qz7jqpZtx3UiiWLXb81X6-NcGPgIXgYi7bHKVnU3lDJp4nhTzIC5PFXyhIHank4-tFtuPirDjnwXUU5Z_-2YuzSkVQjdmOLRHrbGfH5VgQFN33pgKbf2zewLweHt6otnl0Qk_krX9JsWrz1dvzNoEP9qpLhULv7HgWMXdh74y-52FlcEPpvNJNH3E96og3Yvo1kPfIxZpkPXHhEGbCJyA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">انتظاری که بانک مسکن داره، ستودنیه!
کاربران پیش از نصب نسخه اپلیکیشن همراه بانک لازم است، ابتدا هش نسخه دانلود شده از سایت بانک یا سایر منابع را با استفاده از الگوریتم استاندارد MD5 به یکی از طرق معمول محاسبه نموده و مقدار بدست آمده را با هش زیر، مقایسه و در صورت یکسان بودن مقادیر از اصالت و یکپارچگی نسخه دانلود شده، اطمینان حاصل و سپس نسبت به نصب نسخه اقدام نمایند.
©
alirazzazi
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 35.5K · <a href="https://t.me/ircfspace/2572" target="_blank">📅 11:41 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2571">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/mel1xj0SXKeRUWf-MKOIRkFtwoiPGo6lve3hd5mnrwm03qCY02X8qWV2feiEpZPU9tN6fjJ4d82JOk7mc1YH7vxUn3wZ_HmmENy3XytowzZw3Ay_GUFd7RZyA4uacuUoorRC2NSyO958CnrwST3kj1XmLYj815Q7T56SiuioTVmA1mP9EDZw6IdmNC429GLJhuDZmL9y7sC2F1H_5zer0OkTLJ8ZMckWB0ZPIpcDHN_rxrScDwa0dyI7ojOwZ2_Dl7maU56jalB8ICojyo1ePiBuaQN6HJab1yV2BSeCsjmUFIzAjawkXvLmQc7DvcxviYOc6tZGj0p-KqOvYj0BGQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چندروز قبل وزیر گفتاردرمان (و فاقد مصرف) قطع‌ارتباطات گفته بود "اگر استفاده از فناوری‌ها به نقطه غیرقابل بازگشت برسد، بخشی از حکمرانی کشور در حوزه فضای مجازی عملاً از دست خواهد رفت". در ادامه "بستن پرونده فیلترینگ را یکی از الزامات ارتقای حکمرانی در فضای مجازی دانست".
فقط نمیدونم مخاطب این صحبت کیه! اگر مخاطب مردم هستن، بدون تعارف بگه بیایم برای پیگیری و حل مشکلات وزارتخونه آستین بالا بزنیم.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 33.6K · <a href="https://t.me/ircfspace/2571" target="_blank">📅 11:34 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2570">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">دستور پیگیری فوری
#ترافیک‌خواری
اپراتورها به کجا رسید؟
چندبرابر پول اینترنت میدیم، چندبرابر هزینه VPN میشه؛ تهشم آشغال‌نت تحویل می‌گیریم!
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/ircfspace/2570" target="_blank">📅 11:30 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2569">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/tzl13E04dosP2NLy-VWKq048asJorXH6TYJfMNcgQQ46d5dpxqQ0n0zHUEPqua-kEbtLXXyz33LFmc_xB_lnUFX3J7SjtH8jF1O7hPXubMshAn4ChkuzOLYkfvYkYAqOsC8lUAJpf7LJD8SO8ZK-J4r3bR0Gg_jcwSAzGRhPquvmT6-Cq3Q4gtVMksHFpheix22l1Q3BCOKxrOEp9bBRC-S-rECqD7hWjSEHLDteXRnLN-a9Kj0Q1yJgBCDPhd0MXKbzpTT-Qo0difAzGmGSYRpusxes1BdlCRgNqw8hY6QrU44NGfjA84G3KBonausOUgRFSF6uB7T9X6GGmocABA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پانتگنوس یه ابزار متن‌باز و رایگانه که برای پژوهش و بررسی‌های امنیتی روی فایل‌های کانفیگ VPN و پروکسی ساخته شده. این ابزار بصورت خط فرمان و نسخه تحت وب در دسترسه و می‌تونه فایل‌های رمزنگاری‌شده با فرمت‌های اختصاصی بعضی کلاینت‌های اندروید و دسکتاپ رو بررسی و اطلاعات قابل خوندن مثل مشخصات سرور و تنظیمات کانفیگ رو از داخلشون استخراج کنه.
ابزار Pantegnos از فرمت‌های مختلفی مثل SlipNet، HTTP Injector، DarkTunnel، NapsternetV، NetMod و Happ Proxy پشتیبانی می‌کنه و برای تحلیل و بررسی کانفیگ‌هایی که توسط بعضی کانال‌ها و منابع مشکوک منتشر میشن، می‌تونه مفید باشه.
👉
github.com/FrontierTM/Pantegnos/releases
💡
frontiertm.github.io/Pantegnos
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 33K · <a href="https://t.me/ircfspace/2569" target="_blank">📅 11:20 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2568">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">از بین همکارا، اولین نفری که تغییر شغل داد و رفت سراغ آهنگری، شدیدا تعجب کردم! با اینکه خودم کم آورده بودم، ازش خواستم جا نزنه. اما بعد از چند جنگ، کشتار معترضین دی‌ماه، قطع طولانی‌مدت اینترنت و حالا تداوم یک آشغال‌نت پراختلال، آدم‌های ‌کاردرست و خفن زیادی رو از نزدیک میشناسم که سال‌ها در حوزه‌های برنامه‌نویسی، طراحی، شبکه، مارکتینگ و ... فعالیت تخصصی و رزومه قوی داشتن، اما در این چندماه رفتن سراغ مشاغل غیرمرتبط مثل نجاری، دست‌فروشی، مکانیکی، واسطه‌گری و و و ...!
لعنت به جمهوری اسلامی.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 44.8K · <a href="https://t.me/ircfspace/2568" target="_blank">📅 07:54 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2567">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/lWfvUCRXtXEwugOQYKSIgojpljaBJv5NeI-HnbdtaL4Rlu-rbh5tyOxcyYsPZ5cxWzLqI_6472tlMO-OoLIPC1MW_Chu9ZbL9Cj5H-dSJOJN3YgxoMvuJ5VoHVjRnBxx3tb6l6IBqfW-WWvZop3Ryd7kdjMzR6uisLRAtF5jlQPErkMfX7GjbgXsjmq5sC55nYxZh5mZkbv3dzXjg3whsDcamoT32Ovbm9Y_dl_6wyPNjBiur0qYYrKulQ9qafW9xBX0nRNKHJdftKadQB_B5ABF5_Rp0tyu2nxCFHRXWcxCuxJ56jnC3jRDlaGQ8rP--XfHrYFEGi3kEx_DKQIF4w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اسپیس‌ایکس می‌خواد Starlink Mobile رو به یک رقیب جدی برای اپراتورهای موبایل تبدیل کنه. این شرکت در گزارش مالی جدیدش اعلام کرده قصد داره سرویس اتصال مستقیم گوشی به ماهواره رو گسترش بده و در کنار شبکه ماهواره‌ای، از زیرساخت‌های زمینی هم برای ارائه خدمات موبایل استفاده کنه.
©
satellitetoday
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 48.8K · <a href="https://t.me/ircfspace/2567" target="_blank">📅 19:42 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2566">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/sgagLZqJaKO-PKb8BlLaG84x8MmQpMsG88V662RXpfucyFKSTWAo-Zkv62w_LoLmRRosDr4zzeebIl9DunOYSA_I1tNpukzIxBJzWX9rZV_XJSCxu_ouX6P-Vd4z34wBREDG36p82skC0Yg2eo1I9hpSqpmI7cwq-3_Y5Cyrt2oG4QSeUgwIp0UFy9drBZOKvsLO761vvAPUuDRVlngBSUiZEn1bcGY4itm0EYQyLed477D-e3fh3NMXBKGoBeBHzTwqHM3g2tYKY55s0NDwTQaJ5IaBBgjhCxMABImmf30rbixFqnF4l-L0ihBzwRZFuh_iSbqYcBxhH93JCzk3gQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رئیس پلیس امنیت اقتصادی فراجا از کشف ۹۹۷ دستگاه ماهواره استارلینگ در ۴ ماه نخست امسال خبر داد و گفت: در این رابطه ۱۶۳ نفر دستگیر و ۱۵ دستگاه خودروی حامل تجهیزات استارلینک توقیف شده است. /ایرنا
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 45.8K · <a href="https://t.me/ircfspace/2566" target="_blank">📅 19:30 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2565">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/RjJVSYBYGsPznJBwBM5D3WeldtN33kIf6oo6qdHt-CrrfhZPJJ4TCJNCUT8SsDTs_Ru8JROGeYrjzfassPHpBQbbjk4P-jLXZKoSY9UBkm6hCTFKdp4JSV-WnmmF4qm9CHSk5UhkaD9dzMMq3h9Y7lfIjZByhnhyEJyLyX1BUfblukjqpwnVQDstwcNYVTAlwABmmDT750N6sTUS5HxlRdX5gRg-tTrfyz583mUqMUjrS9u5dKSxF-NWGrJoIeQFMmVxo9cvhF6bsTNuAmkJtvwRa68sH-Pulkm2Hh6vhq8o_WVoBLi3-CpbqgraCxDFrqyUKJbAfKImK0WEQzKhFQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تلگرام داره روی یک نوع WEB Proxy جدید کار می‌کنه که ترافیک معمول MTProxy رو از طریق یک WebView داخلی و روی HTTPS یا WebSocket منتقل می‌کنه. در سمت سرور هم این ارتباط‌ها دوباره از هم جدا میشن و هرکدوم به یک MTProxy معمولی وصل میشن.
این روش به سیستم‌عامل خاصی وابسته نیست و نکته جالب اینه که دامنه این WEB Proxy مثل یه سایت HTTPS معمولی دیده میشه و فقط درخواست‌هایی که اطلاعات مخصوص پروکسی رو داشته باشن، صفحه واسط (Bridge Page) مربوط به پروکسی رو دریافت می‌کنن.
👉
github.com/telegramdesktop/tproxy-server
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 36.7K · <a href="https://t.me/ircfspace/2565" target="_blank">📅 19:24 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2564">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/s-LQj0II_t_8vHW0wAdeMNOXYci59Mzc9jf--u3bE6rotw504yUPTgqGXCLqxcHgk3e81I6txDufWkeQqZp9gyF0h_nbHNpCRm8cprBO5ZLBfQqeBoqFAzvfm6Bj8Xr1upEieZuxKu-qu_v-k0D-3v_p34Cm6WjQjJx92OJA78XK9yrC6Zbh4tkpvKcOgEeSQEAeTyCf0ZVokzcWGs6yAthIzx6it_sLLdUtpEVN4X_bwi42rsc7pQOYbz2RNlv9XcMRPJ-2q2qgjm7z41XwVbLrlNCfPHPH_awLSxoZaGO3o3kJvqxXX_Er1Jy8pyYVMlFj267yDbpOH0wbXvaYvQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در کدهای نسخه دسکتاپ از تلگرام نشانه‌هایی از یک پروکسی آزمایشی جدید با نام WEB مشاهده کردن، که از WebView و ارتباطات مبتنی بر HTTPS/WebSocket استفاده می‌کنه. این قابلیت هنوز در حال توسعه هست و مشخص نیست نسخه نهایی اون دقیقاً با چه معماری و مشخصاتی منتشر بشه.
©
telelakel
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 37.3K · <a href="https://t.me/ircfspace/2564" target="_blank">📅 08:04 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2563">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/KR2yMEOfq4i9vjK5gIX0NLIXeyI2OZ-U_oUHYe-lUySOWK44-4aYYnM-AB0bngguvo55s4L4Fr5LjRpYKxZO64-0cBPBkkQ6a--kbCWL1wbrbVQPUlr8ABZzH6hyy5YyJ5HWEYZGRwz-HKtAoN_3rDzW9HlP5BZrSrjgqlBTKgNGaN-OzyrSMDYBJusbRRFMjYjZWRPsh7fyl5ocheOFSdncSNqac9X5z91VFb9-vjVi5nBst80Gk0GefRZtLPxsVl4ollrJwqy_3l-wouoX_kQjA8506NFENhCmOw09zxNbYeKXKz_-G_szlNOsXgOs0-TZpIQslC-1HwR73GEXMg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اتحادیه اروپا با همکاری سازمان ETSI یک استاندارد امنیتی جدید برای VPNها با نام EN 304 620 معرفی کرده که در چارچوب قانون Cyber Resilience Act قرار می‌گیره. بر اساس این استاندارد، VPNهایی که در بازار اروپا عرضه میشن باید حداقل استانداردهای مشخصی در زمینه رمزنگاری، احراز هویت، مدیریت کلیدها و مقابله با آسیب‌پذیری‌های امنیتی داشته باشن و این موارد هم قابل بررسی و ممیزی باشه.
البته این مقررات به معنی ممنوعیت VPN یا محدود کردن دسترسی به اونها نیست؛ هدفشون اینه که VPNهای ناامن و بی‌کیفیت از بازار کنار گذاشته بشن و سطح امنیت سرویس‌های موجود بالاتر بره.
شرکت‌هایی مثل NordVPN، Surfshark، Cisco، Google، Palo Alto Networks و Airbus هم در تدوین این الزامات مشارکت داشتن. از طرف دیگه، ارائه‌دهندگان VPN باید آسیب‌پذیری‌های جدی و فعال رو سریع‌تر گزارش و برطرف کنن.
در نهایت، اتحادیه اروپا میخواد حداقل سطح امنیت محصولات دیجیتال، از جمله VPNهارو در بازار خودش بالا ببره و اجرای کامل الزامات این قانون تا پایان ۲۰۲۷ دنبال میشه.
©
techradar
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 32.8K · <a href="https://t.me/ircfspace/2563" target="_blank">📅 07:49 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2562">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/LaIDj8eYuRcjQ9lPCPnU7Mbr2d24EessxzGRvjBhH6Ox7ri7Ce4dCo6enKZYpwtcprvrtpxyuClTG2UhSPOwYtgwfkFP6hpcFOkrIurL-usN4IOrR_jyakJ36pZnYMa5caT1U0JEoMrfX1AI3Le3THmR2gK3w4J-_h19rKlo2JRjtoYRzqLA4U839P6b7b4KJmOYNdRqs7T4hZSJYn1XJH4OwK0kVAFGXmIt5dOgFyVY6RgNml5AIx3dn_9BVeAN0Oy2skOTAoNgKW0iJL1oUSW5yLGESjNXNEOBZ_e8pCPt4tXRsPV9LtHehGdcUrjWvTgBaY-9cdx7BMid1AkXOA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تیم پس‌کوچه با بررسی نسخه اندروید فیلترشکن Line VPN که تا الان بیش از یک میلیون بار از گوگل‌پلی دانلود شده، ۶ ایراد امنیتی مهم در بخش‌های مختلف اون پیدا کرده، که در سطح بالا ارزیابی میشن.
مشکل اصلی و مشترک در تمام این موارد یک چیزه، که اپلیکیشن در چند نقطه حساس نمی‌تونه با اطمینان تشخیص بده آیا اطلاعاتی که دریافت می‌کنه واقعاً از سرور مورد اعتماد اومدن یا نه، و آیا هویتی که برای اتصال استفاده می‌کنه فقط در اختیار یک کاربر مجاز قرار داره یا خیر.
پس‌کوچه این وی‌پی‌ان رو بیش از اینکه سپر باشه، به ریسک امنیتی تشبیه کرده.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 28.8K · <a href="https://t.me/ircfspace/2562" target="_blank">📅 07:39 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2561">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/qxFGb3xINJRvq8ZIld4ckNmc_A9JoxHal9sLTllOZobL3_H_BdsArxUR8xm00Du9pjfmCRkskywHhY0A_aN4mYRLUeWoCPdfWQAADsi9V65IZTW5uwWhMB90Chv86Yujw-gB0cT2jKSyRnbAJCekDpXYB8nWGxWMv2Qgbk9-6n9WdIk6KUc6I0bHyeZYq0p2meNgAlnGDV-sG0URrPbn48Wl9Uz-kKGZgkWnq2lftPZWuYpTMLv336SBK3V5vejqpNc7dMQXSrfP24qkqJ_YCfb9mPQzSQSdh-OSEnMmDkDg1KrhcKamgY3GocBh0M-lzckUFZEYZ21jJXECKMmi7w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پژوهشگران مؤسسه فناوری کارلسروهه روشی توسعه داده‌اند که با تحلیل سیگنال‌های رادیویی وایفای و استفاده از هوش مصنوعی، می‌تواند افراد حاضر در یک محیط را حتی بدون داشتن گوشی یا دستگاه متصل، شناسایی کند. این روش در آزمایش روی ۱۹۷ نفر به دقتی نزدیک به ۱۰۰ درصد رسید. این پژوهشگران هشدار داده‌اند که فناوری مذکور می‌تواند در آینده برای نظارت و ردیابی افراد، به‌ویژه در حکومت‌های اقتدارگرا، مورد سوءاستفاده قرار گیرد.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 42.4K · <a href="https://t.me/ircfspace/2561" target="_blank">📅 16:58 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2560">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">ایرانسل و همراه‌اول فکر کنم یه بسته رو به چند نفر میفروشن.
©
ali__m___i
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 38K · <a href="https://t.me/ircfspace/2560" target="_blank">📅 16:47 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2559">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">ظاهراً پلتفرم شنوتو، میزبان هزاران پادکست ایرانی، توسط کارگروه تعیین مصادیق مجرمانه فیلتر شده است. طبق قانون شش نفر از اعضای این کارگروه ۱۲ نفره از طرف دولت هستند. دولتی که در «ستادش» اعلام کرد دیگر هیچ پلتفرمی بدون تأیید رئیس‌جمهور فیلتر نمی‌شود!
©
hamedbd
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 50.1K · <a href="https://t.me/ircfspace/2559" target="_blank">📅 16:16 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2558">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/izS9CmPMPeEo-gdlXUmxxBrVIuGUNHhIpjeLXck0OwoIkBIH7cdkDHONp76ZnWpH_FhQ4sVKzZ-5hC44czvv_IgH2ybLUaY_VLFP3NNV4WoFZ1Ni1udQKGqebBiPlZlSRnh_ZdSX5VpjOIjzxUP68iIv9O8iJbrlrMSAjDTxItVpNEelgvI9pPiqgeDOWp_Z5DtMMTUaXfLEi5O0pqeEoApQvsIa5k6PLIA2TW9cQKNz8RMDyYArHdIBFIzzw9gSwi9YzC9TPSSWoQxlsYlOGF41Jbe4P_vLKs-fL6jJgCmGOIWmxHM11q0z6sB_gFUqwpU8BM2quFtJPMHmRiUJ_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پژوهشگران شرکت امنیتی Socket شبکه‌ای متشکل از ۷۳۷ افزونه رایگان VPN رو در فروشگاه Chrome شناسایی کردن که عمدتاً کاربران روسی‌زبان رو هدف قرار می‌دادن. این افزونه‌ها در مجموع ۷۵٬۴۸۶ بار نصب شده بودن و ۲۷۴ مورد از اونها با جعل نام و هویت ۶۶ سرویس معتبر از جمله Proton VPN، NordVPN، Surfshark، ExpressVPN، CyberGhost، Windscribe، TunnelBear و Cloudflare
1.1.1.1
منتشر شده بودن.
بخش عمده افزونه‌ها پس از اتصال، تمام ترافیک مرورگر رو از طریق سرورهای SOCKS5 تحت کنترل یک زیرساخت ناشناس عبور می‌دادن. در نتیجه، گردانندگان این زیرساخت می‌تونستن مقصدهای بازدیدشده، IP کاربر، اطلاعات SNI و داده‌هایی رو که بدون رمزنگاری HTTPS ارسال میشن مشاهده کنن.
©
thehackernews
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 50.8K · <a href="https://t.me/ircfspace/2558" target="_blank">📅 17:00 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2557">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/eKDP7QgHS3W_0PrHVNA2nUNDtr95qlclzADFnL8AcxY3PYkK1cW0naQO0T0z2HczuI4B04kMCnrYYjGbfv2jBu9Pkir0PsptuFH9Siyp2tkzDSusVXWU0JHcbgw_O_g1hS8COl3pm2BxqN8NwyDMDal17fNXs_YV_bYpj8uG-YQkI5mdehZiEBLlhwOpymMrt3ES52fJqNNObIgfKm4oiQo9-EOHN2c-0aIEsvhvhuX_6WWOWjhmFHrAx3HJbLcfm4-jhnv4_A-2yGBzHLLv_FnQyjN26uJWKmQJiL0uvoU-U_KsBcD2_YMJt1plXz7vIMj4tSQ4hhF8JAoXhfMLcQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اپ WhiteVPN یک VPN متن‌باز و رایگان برای اندروید، ویندوز، لینوکس و مک هست، که بر پایه‌ی هسته‌ی Mihomo ساخته شده.
این برنامه با پشتیبانی از پروتکل‌هایی مثل VLESS، VMess، Trojan، Shadowsocks، Hysteria2 و WireGuard، امکان اتصال از طریق سابسکریپشن یا اضافه‌کردن دستی سرورها رو فراهم می‌کنه.
👉
github.com/WhiteDNS/WhiteVPN/releases
💡
github.com/WhiteDNS/WhiteVPN-Desktop/releases
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 51K · <a href="https://t.me/ircfspace/2557" target="_blank">📅 16:57 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2556">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">قوه عاقله برای بار نمیدونم چندم دامنه
workers.dev
مربوط به کلودفلر رو فیلتر کرد و مشخص نیست بازم از فیلتر دربیاد یا نه. بهرحال "در سر عقل باید"، اما 404 مشاهده شده!
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 42.1K · <a href="https://t.me/ircfspace/2556" target="_blank">📅 16:41 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2555">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">اینترنت همین الانش هم طبقاتیه، چون هزینه بسته‌های اینترنت رو اونقدر بالا بردن که دیگه خریدشون در حد توانمون نیست!
©
Kiyas
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 46.2K · <a href="https://t.me/ircfspace/2555" target="_blank">📅 08:47 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2554">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">اینترنت ایران باید به لیست شکنجه‌های تاریخ بشر اضافه بشه ...
©
thepanue
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 43K · <a href="https://t.me/ircfspace/2554" target="_blank">📅 16:57 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2553">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7887a97904.mp4?token=KsDG-D9X_rxYg4urdxiNinNUycG64sM2aQd8FzSGuqxwmeGYAhXO2lIz28zKH3IBbI3Sr2kQlHh55KyqtFMXd89HIEP_w9lkaaVxV0yhmy05Y1PDQ8gWDhkccfTXGyG_juzfh6HUSf40WI9_C6UF-ba31Ohl6PMZGwBvKS6whM7ib4ddZ3raGpROqUaUGiI7t7aYOTdhQFbuBMmaQoXBD4xGW1x7gF2Bnvsh7D-p-trYWPrnTB2xbWfEm0sIwtjTilnUAtwZc8eRwcEtQE3WVWqsd0CWvXGpyEVz08o-TwQnBJm-2NnJuxaviHQTsGrZw1zO1uPj-stET9ekHipk8g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7887a97904.mp4?token=KsDG-D9X_rxYg4urdxiNinNUycG64sM2aQd8FzSGuqxwmeGYAhXO2lIz28zKH3IBbI3Sr2kQlHh55KyqtFMXd89HIEP_w9lkaaVxV0yhmy05Y1PDQ8gWDhkccfTXGyG_juzfh6HUSf40WI9_C6UF-ba31Ohl6PMZGwBvKS6whM7ib4ddZ3raGpROqUaUGiI7t7aYOTdhQFbuBMmaQoXBD4xGW1x7gF2Bnvsh7D-p-trYWPrnTB2xbWfEm0sIwtjTilnUAtwZc8eRwcEtQE3WVWqsd0CWvXGpyEVz08o-TwQnBJm-2NnJuxaviHQTsGrZw1zO1uPj-stET9ekHipk8g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اینو ممد ساخته. یکی از محمدها، که نمیشناسمش و قرار نیست بدونیم کدوم یکیشونه؛ ولی باهاش کلی خندیدم
😂
©
Mohammad
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 55.2K · <a href="https://t.me/ircfspace/2553" target="_blank">📅 10:15 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2551">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/VEXEBRzEBhMAN4yd2N-J8l0ccmcagObUYuQRJyPoDmEaxXtGTYGghZFJqh-7TkWu4Ida5YWAZVYiTBYiahwZLdTZ08n-w5Dt6j988U6-AhGChWvtLB1CeD48XOicIaEQftRjvcHxfGDOAFPBSQ4ZuJT10uTYdUbgbCdzVfoU9hNX5KvVswJpT0TpUqaV4VWegudAFO3oFeDSXdFH_4wG59jcU1Pgo5JNBWTnyPY7tpUJLlgrUQT4bsJKYx_JkeZoNuZNzQVXoGQVC7LluOY4BMMe46_jHTYtXDH5iTXvZZmtMixVCank0eaSbDlWwXlueWik1hUM6LVxHsDISta5oQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اکثر آنتی‌ویروس‌ها (از درپیت تا لاکچری) سایت بانک ملی رو فلگ کردن، چون سرتیفیکیتش منقضی شده!
©
Teeegra
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 42.9K · <a href="https://t.me/ircfspace/2551" target="_blank">📅 10:08 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2550">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/boZApR-SrOae2A49PmVD-BRV0DdWibOqwXC1ibImEonA1p74CPdmyZyUKSSOzEeeuiDCrtC3DiVp5F0nAhyzUweZHQKi0z2qRdnTa1wLebZqeYIEzIPkwaGKoTf524eYcog5ufZTu2mDkSkEJpUPUHjqbPp-rF0wK9DCsok7FM-3Hygt9IqSeNXQ2kcX2sI7zwOjN5GWcVPl9P2ng0DZTYwqI6nV1Q1D9mpSQaQFPB-Wv26HTxe6U2jAnfJglqgENQwW-4gKnbM_Ie1Fz2h5ei5kQ9BgWuOMRMkl1_wxmWRKhyJ33bX6-lDg1RHTjjsqOffjgXd801iyS2GYYiF52w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">معاون ارتباطات مخابرات گفته دستورالعمل جدیدی برای محدودیت VPN روی اینترنت ثابت ابلاغ نشده و ممکنه از مشکلات فنی شبکه یا نحوه عملکرد خود فیلترشکن‌ها باشه!
🤡
در رابطه با اینکه اختلال‌های اینترنت وضعیتی فاجعه‌بار دارن که جای صحبت نیست؛ فقط اگر بدون دستورالعمل دارن گند میزنن، یعنی دیگه خیلی کاسه داغ‌تر از آشن!
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 37K · <a href="https://t.me/ircfspace/2550" target="_blank">📅 09:59 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2549">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/eO_vEQ5DnDZANrK1YEsTduD67kIJIxmN2uB-u7wJqpDlCgGRrHMe0sFHzpGjl4BL03yq6SLYLN6ZptciLxIsFAx6XygmCINcfVseZ_0TEdI-H0FjfN-dLI58KTgLXzg3EKheZR0psaW6_ccesyQLU0uncum0v_8qSxNdx4I3qs1GYoFrPVMbUrUQKbsoPYPOsRrj-Bw3nyhx8qcJZtzQj7rEZcaUG7iDnwXZegy-BSa20CswwrE36mx6PlMfy4GqRCjIxslbOgON4Y0tofZI3EejWAqsI4F8ZYw2jncBAxcqrib2jqU38q9q-3mWybd4dzwLdMoH528BrTfz32na0Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">از فیلتر شدن فوتبال ۳۶۰ و دستور رئیس‌جمهور برای پیگیری مشکل چقدر گذشته؟
هنوز نه رفع فیلتر شده، نه کسی فیلترشدنش رو گردن گرفته!
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 33.8K · <a href="https://t.me/ircfspace/2549" target="_blank">📅 09:47 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2548">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/pey3py2Ea3HKswxNtTvpxNXXOIdVYOdDv14ATdIOwT1rR1jdfoI62IYtTvssW05a_NTLrw-XHUeU7G9aDoFZuG_eHtodAnEKf_VQZoakVY4sRtWaNwRIUOoXdvCVWAt54JB-7Dr1yylnVJfrrZeyB2TzycdZqBe6hFpI6UlRvykGjoAZHs5pJgmSCqa3c_DD33cTvfkqAA9XqtdkFS-zaK_mNZ1sEDHrwt3ZIo6olpL2N6OfpCdgzzSB09qgfbBOy35AXKHyurq051z_PmIdLg7gA4byAzzcUNQh3PMWxg5in5RPYmPTCYCxZx_hVw7Td5Sg5vPSteG0ajHiYGNsvg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پلتفرم لندین که برای ساخت لندینگ‌پیج بود، بدون اخطار قبلی فیلتر شد. بعد از یک‌روز که با تعهد در دادستانی رفع فیلترش کردن، اعلام شده دلیلش فروش آمپول لاغری در صفحه یک کلینیک زیبایی بوده!
یعنی هنوز که هنوزه نفهمیدن فیلتر کردن یه کسب و کار چه آسیب‌هایی داره. هنوز که هنوزه نفهمیدن وقتی یک صفحه محتوای خلاف قوانین داره، کل کسب و کار نباید فیلتر بشه.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 32.6K · <a href="https://t.me/ircfspace/2548" target="_blank">📅 09:45 · 21 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>

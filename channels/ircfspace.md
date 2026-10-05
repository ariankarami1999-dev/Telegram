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
<p>@ircfspace • 👥 96.5K عضو</p>
<a href="https://t.me/ircfspace" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 این‌کانال با هدف دسترسی آزاد به اینترنت «به‌عنوان یک حق شهروندی»، به‌دور از هرگونه وابستگی حزبی، سیاسی، تشکیلاتی و ... فعالیت میکنه!https://ircf.space/contactshttps://x.com/ircfspace</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-07-13 22:09:04</div>
<hr>

<div class="tg-post" id="msg-2650">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/KnKx62s3Jutx8JUaOj7AZlG38xCqBvwdz6ZOaoaVO1AXU_B5a7wKQOGcS15ZWRXIKw4FpdEBPKUSaiKZ6HvVMdlPfB2CeYI-xSrtkgQCfOiMoYXmDH3n_t88TwUI1NsllxGp_nh9V0xZ49uFhitrK8VhBQ5d9KJMhkLf10R8M1lSUhTLc2vVIfu8JlpFe8ZD-R8ZpABQSpdzFayb-YiOa04NFGQ4WKjAFKR3d6NwtDlYC7pHn7PIStAs7Q-DtEY7tFRX4xao0i3YFXd2o178ovb3qv1SakGVFDFZQYOLg7HNo98xDypBYANyv7Gn7ParL-6sgFQMXDIfYsnFSGzpIQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ادعای "قطع اینترنت کل کشور فرانسه به‌دلیل اعتراضات دانش‌آموزی" فیک‌نیوزه.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/ircfspace/2650" target="_blank">📅 18:02 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-2649">
<div class="tg-post-header">📌 پیام #99</div>
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
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/ircfspace/2649" target="_blank">📅 17:53 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-2648">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/VzM5oIWMwi9duPPFo29XgQFuAgtU3jS7rMjEZwdAOgKXbllLQugJGDmt3po860kKLWywMzQZPA4iHwfqrsAiRmSxl6sX6OZvxtMk_1TGke4PsDyTas4F7c-uEWIYV6vZKjypUcgE_qTPqAciOZy4CZTL_cwiF1OA8L1WDCeRIsLN-UrPX_H3Mp6IXvridRcD5B4OGCahE6SpokPQJJuWvZj2K7XBqp-upk6-9BOGOo-BsFOpQE93sRwRwqPU2iwiOiw4UnP69SBJijMHjbW0T2mlpajVaaWRaB4H0IZhPK5GkqWPUn2yhhJynKaYO1N67zv9C1Uio6VijsjyVKjZjA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رئیس پلیس امنیت اقتصادی فراجا: هر سایتی که اقدام به اعلام قیمت‌های کاذب ارز کند، باید بداند که برخورد قضایی و پلیسی با آن به‌طور جدی انجام خواهد شد. /انتخاب
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/ircfspace/2648" target="_blank">📅 17:45 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-2647">
<div class="tg-post-header">📌 پیام #97</div>
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
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/ircfspace/2647" target="_blank">📅 17:41 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-2646">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/J_XoZ_4rcBg0PUEmAMpg4D7wKO9dWRFlCWj05lVrzZC7ejWgk2eqyGLFyyoAL58W5wXeEayiDJFvixmRrDhJB2QUc1kY5j2L3RQk9epE5EXp902Wqjcvm-F4DnmWDggsekNZOxCe-IOTgqraTRMmZzM381BIlgi-vORNn8wxNqZIXxAXNg1J-9DYtWoYIAnjJ01UvQYu33xGip-X7wdGzhAuASGQwGE00FPagSPNTzCpdf_7eTDtqmGvrAu5zEzq8I0gT_jyLmo0jy6hrvOKDiY__dVJ42OiZcyuNjay1CUpXMYt8tP8KOUURO_9kTUHWIhOAsU3e4hfIvfPDqiRPg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رئیس مرکز ملی فضای مجازی گفت: ایران برای اولین بار توانست با موفقیت پایانه‌های استارلینک را در جریانات دی‌ماه سال گذشته از کار بیندازد. /عصرایران
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/ircfspace/2646" target="_blank">📅 17:35 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-2645">
<div class="tg-post-header">📌 پیام #95</div>
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
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/ircfspace/2645" target="_blank">📅 17:28 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-2644">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/iRNMis6MwNjJOeIwf_n6XfeErJecTC_kI3-p-1IMCk1Ce18QItaxbg2ijTLkHPFOl-6sqUrl91y9YqsjbLRMujWD8IkqXSSWdZ-fHwNtYwN1mMPLLr7uY8vENk_II2Z9EKln9R10wtVQklT5-vp3CLhXcp2S37AbA3oA0s11ckIgu_2GJ70HdCeS0ll9Y1u84rEWjFUHXhIBknISNMwZWEWj2xYCclYjwQ7fLOsp8Wmo2UZWXC_K7qehFfmWle6eTI-qm3TZdIfedieM5S2N-FLWZDqmycX-rG-lp34TumhpLKWfW2UUmY3oMcNPXZzWlmIU3akIvpNCrWMzPpzJiQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/ircfspace/2644" target="_blank">📅 23:38 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-2643">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/liMxvMn2OO-3Le5_zs_H0chLRPRbhzBeqBL_EcR7dPgsR0g7xz6JAx4NW5mFjdntI_Hr-G6rzERNfV6C0F2MRF3Qg2wARCbRuZSlHaD-SPupl27T2bhcksNlMYebTvHxro5S73gHTfmnH8WtdBgvPzIa6Q_dnREcpvjQmrQjqag-WyMSui_yrCzgCfu6SDioJ00gT8wUEJNtp-y7YcUgl0TcsH5TWcP3phbiuhw881X4MVUhXepWdTmpG-0t4F_LE8w7hEE8HRj6xP_9uxJKQvpdo37PFHhUON3PlRmzLqFtVJslb6sT9XVsJ8icgPgB0cFwnusAiTO7Eoq7f4HQ1g.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 51.7K · <a href="https://t.me/ircfspace/2643" target="_blank">📅 23:31 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-2642">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/U4FW7cVK4Si8dNvIZYomQYbZWHuXbJxN5JBMECnw5XHm-Ayq_bGPKH9zODdmtMD7_L43Dj67ab3SIXzVvmHocFeKs8Zgyko_vJboLbbQrzFWR9orsHWYulYCvw_0qjtwyAPWYm1G6bSc7igHFmyrv2dhJJFpqG4kDuaLyquVHMEZ2U6CbIfFlM1m72kgb4zR353N7uV7yCoMh059BE_W5BrrZozMav7OLUYONfoIMbTj6vHcV43kxtyEOv0D0p3UfD0wDs3mSS9cLqhUVPp_oliqfHdX1lG5aZ_ynj_JdWFwnjNRQWGf1ogTk22zmOzZ2elg2k3TVXJXux_py441Cg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/ircfspace/2642" target="_blank">📅 23:19 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-2640">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/a6nuZUnKr6RjQ0bzcH1kn6K-KH4UgcxU-DC9cwE7pAivr91QZZ-p09guGNYjq14WnC2vFv3ZUjeKNhrAGMDBMIQBdhNKGRQwYvxUJn4AN_mD-CDsJQnNxPt2_NFNXE3NDUrGH5ZATha8gEtykR85nx0KAP4zaBBgeaiCxefd_o4vgt15XxROSUh6z5bq4CCn6pnVJvGyMQIzuZ_t-a9jGSnqL2elgaIy58n9CmSRH1fZFAw0IIsHSQes_okaO-zHrVjbqpWnZPJ1qAyipynUfHjiLUoe5E7mfvJP8SPhV1yuPtdcCx2TeM0LRUzkWoX7vHe5ILMU-lGTnrCNE45AcQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/ircfspace/2640" target="_blank">📅 23:05 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-2639">
<div class="tg-post-header">📌 پیام #90</div>
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
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/ircfspace/2639" target="_blank">📅 08:22 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-2638">
<div class="tg-post-header">📌 پیام #89</div>
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
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/ircfspace/2638" target="_blank">📅 19:42 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-2637">
<div class="tg-post-header">📌 پیام #88</div>
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
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/ircfspace/2637" target="_blank">📅 19:26 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-2635">
<div class="tg-post-header">📌 پیام #87</div>
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
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/ircfspace/2635" target="_blank">📅 19:09 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-2634">
<div class="tg-post-header">📌 پیام #86</div>
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
<div class="tg-footer">👁️ 43.5K · <a href="https://t.me/ircfspace/2634" target="_blank">📅 18:57 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-2633">
<div class="tg-post-header">📌 پیام #85</div>
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
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/ircfspace/2633" target="_blank">📅 19:03 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-2632">
<div class="tg-post-header">📌 پیام #84</div>
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
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/ircfspace/2632" target="_blank">📅 18:56 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-2631">
<div class="tg-post-header">📌 پیام #83</div>
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
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/ircfspace/2631" target="_blank">📅 18:51 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-2630">
<div class="tg-post-header">📌 پیام #82</div>
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
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/ircfspace/2630" target="_blank">📅 18:46 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-2629">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">کاربران در چند روز اخیر قطعی، ایران‌اکسس شدن و اختلال مضاعفی رو در اینترنت تلفن‌همراه و ثابت گزارش کردن و میگن آشغال‌نت چندروزه که شدیدا اسهال گرفته!
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/ircfspace/2629" target="_blank">📅 07:37 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-2628">
<div class="tg-post-header">📌 پیام #80</div>
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
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/ircfspace/2628" target="_blank">📅 21:06 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-2627">
<div class="tg-post-header">📌 پیام #79</div>
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
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/ircfspace/2627" target="_blank">📅 20:16 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-2626">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/POUw3n2emEwqhxFtRy-jBawyQDnybrxatLBQqyVCkrd4rQ1Zc-vhPy_TQ-LM_MKGrMShD5JFFEN2X0sXsRfpM6soLfvbUG8NaQZ5y9H6PoI8IXHJDVMY6h41Y5_q9kA1PbnH-9taEPClJnYhIb-eBGA9ceSMHJnyIAXVZQTDYz-yTlTAOTdg_rwHVq1l8grHRGOcbrPNRQEMLr1ojNyKqVzju7P2o_DHDeYT_9yGHskhyUpEMiPcqO-0jvpO3RBTNZSwj_jLOWFWaz_n6iMk_xJyBRAvgLJ5LR2NEBmEStNbxbUN5SR4TOxdeRsZeWKPxK6UAd4cJNK8Wpkj5I0vng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اگر از دیوار چنین پیامکی گرفتین، ازش بی‌تفاوت رد نشین!
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/ircfspace/2626" target="_blank">📅 20:13 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-2625">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/dpwcw7PdfeE9iubwX_z6E4D9AzNH3yRnPyKtZLbUccCwDIQM0j7E-GOJ9KPwfCU3Sa7mKgjO0M7DD5mfVnnZF_iY7omX2uybziqQAJMFm08Ofhl9cY3hqlIiF29b_V25ja7T4g_1M1XzGtGz-Ttfw696Hk5eJACDuc9qD--MHjOwuY8GWoibhZNqgxIHXvKDbrOwGm--TowopXs1TB36-gLjDf-bMBVyv74L2HOYu-BvOkEbcw7LAJrvQx8P8HVMU3JX1fljnjQNC-G9RnuAPi3cGi3CvPF5T77oYuiKwrkJ9k63-cCzZeild3PGtogLSbuYvsP4KjcCcqwSdiobdQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پروکسی تلگرامه؟
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/ircfspace/2625" target="_blank">📅 20:09 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-2623">
<div class="tg-post-header">📌 پیام #76</div>
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
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/ircfspace/2623" target="_blank">📅 20:05 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-2622">
<div class="tg-post-header">📌 پیام #75</div>
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
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/ircfspace/2622" target="_blank">📅 19:59 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-2621">
<div class="tg-post-header">📌 پیام #74</div>
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
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/ircfspace/2621" target="_blank">📅 19:52 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-2620">
<div class="tg-post-header">📌 پیام #73</div>
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
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/ircfspace/2620" target="_blank">📅 19:47 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-2619">
<div class="tg-post-header">📌 پیام #72</div>
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
<div class="tg-footer">👁️ 37.3K · <a href="https://t.me/ircfspace/2619" target="_blank">📅 07:48 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-2618">
<div class="tg-post-header">📌 پیام #71</div>
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
<div class="tg-footer">👁️ 34K · <a href="https://t.me/ircfspace/2618" target="_blank">📅 07:38 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-2617">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/sqdVjKI4yce5j13aWOu2x4qyPw7CuvqbHuSgJaauZF5ymMB7A0lEugglwnoUwiTEA-yDH-_-277OATFi6NnpmbZCaFGTstMJ6JvJ0NZmintXQyLWK3pSwZC6nQb_cgwNK4e-HzVwQeVclqI4u5CU70BB3oatjF_FJC7Jw3Y0UY0bNuDiP0wwUT6NC_igOQ6cQY2jIHCPJGWPwKxMK3NxUM8QT-WHyPMDk_okS5X6sklKEAhXzsbDmx_Dt2_TrdPvrEr9oWlXBYmFj6Y4EJWWsMg4YedvTAMPCWSYdio293D968FPKbtlQbbmW4gJ1mnNXJtIm3_-nx0L9uXGJTu6kg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 35.9K · <a href="https://t.me/ircfspace/2617" target="_blank">📅 07:44 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-2616">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/lIhiKeuTuwEqcpJV85LqkCMrrSkWLNMcf4-U85gsYxcIcnHEWZIep5HfZ_A_eSQ2Ps6rkAWeGy23PIOmeSaTR1KFfK47ShXewSNTdJx1wKCMbxcFrXF_SGZ2BFUy_2LGgEJ-hjq8uYjPlQS-AYWgneV4_uAdvrQi8cf-zOwK1OZ7WOz0UwmHU8tZuYxj3WgiPYDZfQKOvi1GN1kqaT67owVvbE0FqcYrUUmH02J5iHnZyhu7JXXhJc5KuiNMbyu-F0UYjG2NKZZkRQwnm-ZYqPB2nZyXd8RARtS5aytyCVTnTRhLB9hwY5PjnGYeLSPflUK9i1Ejjw5qWWiFAHGzug.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 37.5K · <a href="https://t.me/ircfspace/2616" target="_blank">📅 07:38 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-2615">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">معاون سازمان تنظیم مقررات و ارتباطات رادیویی گفته "حجم‌خوری نداریم و بخشی از ابهامات و برداشت‌های کاربران درباره نحوه محاسبه میزان مصرف ترافیک اینترنت، به وضعیت ثبت اطلاعات محتوای داخلی در سامانه تعرفه ترجیحی مربوط می‌شود".
خلاصه: حجم خوری ندارن، ولی باقی چیزارو قول نمیدن!
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 31.7K · <a href="https://t.me/ircfspace/2615" target="_blank">📅 07:34 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-2614">
<div class="tg-post-header">📌 پیام #67</div>
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
<div class="tg-footer">👁️ 38.2K · <a href="https://t.me/ircfspace/2614" target="_blank">📅 08:01 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2613">
<div class="tg-post-header">📌 پیام #66</div>
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
<div class="tg-footer">👁️ 29.5K · <a href="https://t.me/ircfspace/2613" target="_blank">📅 07:52 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2612">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/fIlLuunby_EpQR8ZqzENc9HnQL2VNzUDHKWmu7sdIXMIrhjNW4FpY4-1bLjfX19YJnyEqmtwpkX5Dof7i3fFXjwuSYAIbDJdhoDINwN-jw_IJjVuBNxbU_treeXPLqbJEz6Apy3a8SqZb6rg-cc9Hyultwqs6iY0J1RqxO7_s4Lwuc2_hCE0t9popP7o-1yKfYCkeXKoqN29u71u9unHGtjFBmh2OidgoSh2YShawt5D8DA-cJRY9pLaGzHStJ9BFd58mt6OylqqCpTa5TxBUNikwIP09JMOMK2r-h5e6tHKL6FPEOEveunMPGwhytIbZaF7u-eDFU9f3nMeCNqMqA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 30.4K · <a href="https://t.me/ircfspace/2612" target="_blank">📅 07:45 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2611">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/VZtrIorrFObaXBenkcNyrws74cksjDn6Of-5Q-3_RvhWy0Nekrq8PlKkYaXdyorKZd-XR7Tf4Mrj2-mube2JNVea85q3g8cLGGf0hWSjldLa8bHtQvG_edSjtuYW3VNcS7lPLBlS0uecTABZs263n0fIt_-k3rz2h8U5Q6cIvSyF4_-LEosg58Ql87cKXLTbFQk4vyOE1M9eaf7l2sM5uFouNc1pS4Gb2It48UXsMEvCFwubeHHYo6F6_68YHGdRghEtPBoXZwBScYNPmUzPC1gIdP5tz9aK9Ez3sasN1t_eMRBFaIP9QVExh-1-NKGPtzh0zsyVNDWP8YkyRaE1vg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 32.8K · <a href="https://t.me/ircfspace/2611" target="_blank">📅 08:20 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2610">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/X7nVGOsDeDl9Wh8gvHvjjYRnKaWM1CNuLj-gJ7Cp4KAhOKx7zd-Er6mo6q2OEQFH5IzpAJ9V4utobBJVxR6JhPHyDUGyWOnokVPm0ImFoV4hScl3Onz8GIQDCzevDXD0D5GK-gjPeF3L1jEzG-seRQcMdy-PjxNpoK7sUoaquw5CAXmjgV-O9T89AyzzYLI6KfFfqDGqD5UbmGVkem7z1q0s9UDUJ6FpcrSwXbzGZAfS0Z-uM6vjlUKjGV0MGX-O9GBaRoL3YKrqCMEc73sI_iP5VfbxB0gwiBhC0EXDasOeh_YlgkcTHsYqZA9D0a7jbViEsj8OjTWp-YQ5se3sow.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/KpDz9nX1YgGJtnYWKughADz0eImM5xemY31vxK3hMyLKsCyphqgPDjgqF94JLqKxho0L6jWzSULaCB0dh-7fZ4yTLaXyKPUa08TuOj3YqYB3_pNMDypW15l1I7aATp0js3zHytbLlc4-C1HJqMVe6ii3v6D9vFU7MrG4IY7kvhPnKUnZaTqoZf4stp3BJcrLg2NS8FunmnfHaTS9k7vg-wyDxR_syjJYBs_w---FxX-Pa7ia2vzD1HO7d6iOAsLLM1ea9Hf0MZ04cZS01iGF7I6dne1b9n24wZrmmm1Y2dhfM_aqeDhPYH3IJHj9JiPITC38aFTJJyNSdi2ue9nMnQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 32K · <a href="https://t.me/ircfspace/2609" target="_blank">📅 07:59 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2608">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/knvnoxSK-G3uKXE-kighbRFTrlb8kM-ptghj9hDUXTOCiSUkmo0RQkcY5l1eHy8GcAoTuMpFfPvoQQrFx4Dm3b7A_mP_Pq0Rq6fRObet8ynO_lZwmrB9NG-PWr7-noDnGfHBBouWhWoPCjTIsx57avbGAiovjvTKFyDVQ3CDo9UfF8nh7WcJN4Zzh-1TNlyWRE5mkzVFx4xFdBEuna6hkR1ITzDoUu1k3RJOUetEJp7TPd858eX3q9F6j6F2_r0hPzLhhDC9iZnVeytuQtI7CvXj_JnM8NwKJ7iwExpp6ff7f2_rX7SBED0LS_xR_t1Pw9rD-Y5LKzm753hBjydIwg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 37.3K · <a href="https://t.me/ircfspace/2608" target="_blank">📅 17:35 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2607">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Z76zpmo43B_G4eqdBf8ZADWyou-eEUggQAhA3MqK-6fQagC0daOCDGYJlLd7ibUu_Mvy0tr9UA5zWHVC25uxGnxj0qog74Hx8smp7DoaWVpaslgoYUBNsfMXsQWllBoFxdw23MapTgg9KeD9pYfqr841H2Bzyp2Gi224BuK99-oeT0whduYIEphS4P-aTROZ0c9f1RHzp9r1aEClrt33KQXwL7mcxqE6uVYRiFVaRwrsuW_ogoXelK7Amqj5NJ52qxdRed0FPrb7OKOQNzEOWH0oi5hyXQEFP_LbF_YXkqU-kNg15FGiKMP1-T9SLIwQfk8bcuaLX3zYm1nVxAiEPA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/ircfspace/2607" target="_blank">📅 17:30 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2606">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/AETlEbIhCp5bCk10dPV6wrZShheMNG7t__WDgjIbPAkWQ3qLVpPzULT8ZeFQvy5FakRSxvTZOOwyRAPBpIb0UrtjUBb9Y8rrkn61UJfKbO6pzob-SRVNT6qdd78wKXc3eY10EO30eDvk2RHE8tymVdkPHoA-fW5g0Ow52ETw8cb9wu8x5kQ91oRsL1_4A4gnIJgoEJAB2vGlS7AxMKK3Kw3k0WHgWpvuc1F-Leob-q3dEF8urS97M13ZUTAKvMEgxDBYD_gC1QCb4OgPuBxmAaRJmnsfyEnO8UIwsovNlCnzGptPzNV-Cmrxk7ab-MtF9KAE4P6Hkzq5ogr002LlpQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/aE4mNwUqLDX7VYyvDpOW6vCuq06m0j-W8NJgAVKSwvRVXT3KBfOC-i9Amh5w0q3p5pa19_zxTpuAeC9j378EN-iAxMhlIA2VL8x7QSVkiRVekmXnM__Mf-bMjs7R7dmM8T5ozy4f3WLGiaQHb6qIi7k4kkmX-2HAwikgx6Jno7GcAWvdAV6CWpIeQQU4HVvG0s-0jc58tUPYU_NfoUh27Ok2aqns4d38aTJTrKslcMJh2-c-iS0HoqbTBv8pxd7Lu5rCsfFBwJRu-HFB_xV0kl1JZ0VTOBfPRUj_rwSPTD6oAsajiHa6vJETZrQGLct-pRIVvyHMrS1XX9LOml_sHQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 32.1K · <a href="https://t.me/ircfspace/2605" target="_blank">📅 17:08 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2604">
<div class="tg-post-header">📌 پیام #57</div>
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
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/ircfspace/2604" target="_blank">📅 17:07 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2603">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/qkRKpfJLm6G3wFkYyXkW9xDo-2N9WzfcmeNJdS6RfgWuvk9gl7rM7W4qAPCRxThf4eE0z-ELI65f1QL_3c2s8c5xKdPRINTFQc5k1TM7Vl2jheFTComyUE2CU_O9sSzUe3c69-1jKXVDsShKVJKf1pC5-8Uyf_x-pkL0JkT169fDkkguO3ZGIzHjAjghpEurRXlqYaMF0JChCbWfbmRh1bAA_OVtYT7XN6dH4N556HyxRVB98K89CNloU59Lmd710n5qd2zgvoWlQ43PNJlfj5WT-ftQsurzpZ2XdVMia-G5FSKE-Le2Atqb6wZfCAmvcvWXkPEN9AYqCJXtJKOk4w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">صرافی رمزارز کوینکس اعلام کرده فعالیتش رو متوقف کرده و کاربران تا ۲۲ دسامبر فرصت دارن داراییشون رو برداشت کنن.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 30.2K · <a href="https://t.me/ircfspace/2603" target="_blank">📅 16:51 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2601">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/sSYDMZ60d2cBYULJi-5H8Ll7vXibWpYOmEndcUrX5R6REvBtenv8FHqLN4rlqlOj054XmeKPnsZj4uWTuSTigZIWh0YosY9UlANAyN-7OM8-trXQISSBSBoq3_1zoYpHaXYIry9mvcSZbKyeqxjtUeT9_Ng6H57xsQb3MOI8LlZBRVsy9l9wyvyzFwfiKRyVnY77s03Rhpo6iY-Em-OVmgH6pQAKOngWGuZ10VKzXZxGKlzP3g0nI1rRk876WZpdX82J4QuTPk-diYv0D6-KFX_WrUH7DzrnbcoszybOeDJZKEQFi9xpAgLdC11pK2BOEFBKZzyT_fz4zja61tzOEQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 38.8K · <a href="https://t.me/ircfspace/2601" target="_blank">📅 08:17 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2600">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/A13SVkI43_FiWcYVv8vqPHgVOSs36G6QUrABhnurq7XNgIeP0fwB9Q_9gnF6Ecjxz-tsJzTLAFK22z2GVPIz_eMM13zjWot90KLiaIel_gEaMylo8hyhPRSlFupArjauBK8qy1BhWiJs2PxFPZz1XBOZIEySbRkL4xxyKHOVJ6ws7sGu0pIIZ3it6n5WNkEM6m9ap2Mj9mvkfLvAg-apcvIBEZVdgoaaJi60rW8xrb96aj5jEuFiW-4SQFtRszekUDrGDjvP4CtcwPXFDsFOHmWRcbnmvJAEOsrHjBSUhPtlcojA7R6lOEY407E7OUE-zwXkEHe0HXf2EaJ7zsAb6A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزیر قطع‌ارتباطات سرشو از برف بیرون آورده و گفته "اگر درباره محدودیت استفاده از IPv6 مصوبه قانونی وجود ندارد، دلیلی برای اعمال محدودیت در این زمینه وجود ندارد و موضوع باید با سرعت پیگیری و تعیین تکلیف شود".
به مناسبت همین دستور سریع، فوری و قاطع، از تصویر پیوستی اکلیل باریده.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 33.7K · <a href="https://t.me/ircfspace/2600" target="_blank">📅 08:09 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2599">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ptuajkA7pr-KTrfpptT-umG1GZ6U-F0fYy5Rp_ZDjt5cggUUlbb0ca0jvU97Y2fYcLs2M1ewq0xBO-E40UEDdBS7-t08i6b4n8rBZDy2fw8aaVQguE-5Dw-kuaT1KMeLu8keR7IA-rg08Ukvv2OUl17e9pK5OAJe1Fy2AS_Syx9cuHrEVIQrGouizbWb6e3AEhkXssMAqFCWTCJJmcmZGreaowfr91NbA3KR8dC9xADWwg5NWLg8AZFNdR2BKhMzRyuUSGDTAAxgEKalwjMGoBaaZ3cch01RwmDWXrAKioa3VFTdJk__pozyhflJkT0rihNxzDboup8Sxqm5IEoTSQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 44.2K · <a href="https://t.me/ircfspace/2599" target="_blank">📅 07:53 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2598">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ROlbEFs44Nvq_wSmaPIt3e0_Np96GL8BZgtoTKxo0ViauD1mQBvZcmeLwCjeLR9yPTOAmnc_iq1GkvSLJoj36j9bQkBzuHpCefmjxcG7JrezjKA4Sw0opk-OT7c_DRh-EmKj4o4ho5ow2IFAwj2zAS7wn5xabniwnAG3YOKSjBlhX62mOXEVwWcP5j-g7gOCVaQoOPsJLp33xbY_ZXsYpYo9BO8dAE6LLruNVtMbVV4GW4kIVUDGsC96Uhqz-nf1bS6K34EePBqP2z61iFCBDW0Vh_8w3HiiJSIm9JqJCVFwEfbcFFGbI1N5r7kjTkh2mkON5q539UILCWjbXMiEpg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 37.3K · <a href="https://t.me/ircfspace/2598" target="_blank">📅 11:15 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2597">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/iW44vYcv5Bvi8wkc9d56ZYTdT7S7I8cvcde4FHaBeRV8xcESTxvAWTmZOfg137Wozvw03bpUGNRCllamMKN4yMT997V4zEyOKY-zWUpCdmoG71N00AyDTGyr5FwPj3Zivqosp5IlrIp4-xdzq0chrA2_8zu4u-0mr09S_iV7qFCko6ppV7wrtAWCat0ZIjZAg4O-B9XFrD1_sp79o1bkPwJWxer00dFUr7Ty2aAGBHYWpRjDBeVC7hJL3wzm2cDzMPo_19faVHJAaW4D_iNvNgLJ8QNHSQT9CPCH54kbIXg3yoxcRK3za5Z6EW68d52HRFGSkQziBACvG2uPjnGzJQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/fFG0VqjBWOsr6mDc6aG-qzCrOUdvuWi_BwcIX98h3oLW7R06uK_dZw5LszB9mGgZkSWZfAuZaftDTAcAH2G-IuO1jlJhxXBWojB-RXmGgXIeyWoNJcY0fCUDo1hBNS8F7SnwFxSytnVY_9vkbXJRYyvB12PbxyPsfT2tWVk8HGjxGxsGhcptquZ6ovPBD4D1rXQLVzz51XCpZIYOsQ05Sqa3uu6UtGrcVsdlM1m6pYuErjLn0JnGqxVIqhW4N8zB8iDEDghLYdpFSdDDpINq54UOH-ivYUhmJk_18VvqVnk34H72vNtJOhqCE7WxYe6Yo4xa7Oj8EjvF8XRNQxIAmw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 87K · <a href="https://t.me/ircfspace/2596" target="_blank">📅 08:14 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2595">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/tn-GAr4cBW2euzCFo6ZdcA6vmyIVIf2MadIP4IL9bLqpJ6rqwnpM_G-Z59c4XAE2PpAuiivcH8oVCHG6g8uDgNo0JBn7Cf0poF_YwctjPfkbowEFShzZoFj2GaGvQv9lfp6yoArOqnjRFv1P0dcAawwrbkHF6GFyeu-3F4gBA-SEd2Yww3D1FF26vhBkiC2IeFA-kTUnj1RZz9Jl2j6uDTeLSL0QwQfI_QJo0cONG-ED0_vh9C8mgGoiw-nhJ-2w6WYR8JfiIAqWg9imECpOftkebemG1jcY1l4WehfrFEgPbhBpY531nM0pMzCFDL3yWFzGBksDgiL2dJOWvbvjiw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شبکه پایدار است، یعنی به همون آشغال‌نت قبل از قطع فیبر نوری در ارمنستان برگشتیم!
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 35.4K · <a href="https://t.me/ircfspace/2595" target="_blank">📅 07:57 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2594">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/cd7GWst32k0tZt4fXZSEA4dbm6pD15ejXB1MDq7eeCY3MUX7SoARb4PDIVT_N4NrckPWM6J57Jyf9H38FW2lHAs_wWoulgxQnApajqnojDx5arXmcr0Ciov-iaOrHnTVYxiYKLYLOnz-AP8yn2XD4vkEUb8Sv8urtbFops-nFXPgItwo6vbg0Xb0wKxjnEK2-wi6DdLKhGahmJTw21lIzGWiBLkr2Jq3bB3V0znQjbD6uqXkIzXwx-bAff9SqxgIpFc3vnhv9Zce6GbCy-Z7yW7IJhygLOPulx5qEwxmKaHjUCYHywzrEZ-u1v-lOt4zqakOG6h1ZS6XCQeqnVgdjA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 38.5K · <a href="https://t.me/ircfspace/2594" target="_blank">📅 07:49 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2593">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/k9Av2-1UUnDq3X1l5LQyPGnN_7X-XmHQoVxkVgfupggSzouvq2evihJijVs9eiaPwckqTE2rVqgXrNdHWPfyt4KD9HLe_7J2OSoVOLcHa5_eImW5ZTsPLRrExtupD0Qcr-geWjWCsI31kyl01uHTmDiVboNHiI3_uKu-BzZGyJWpY1xv-ZdRhMnaNkq1Y8WCvFxJEu5u1Pfff55XNigsA6jvaOa5n37wLWumkSYi-g9FyEUpcQJmbBUHnmqLg4X9O-pzJxRcRYqFLHHrH0HPMqVpTnH58EsghiDHQPH8W-nCSjWwxcO2TkOYAKUYnANPXqxjgkJ-6gP1l4KhXN6VRQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 29.5K · <a href="https://t.me/ircfspace/2593" target="_blank">📅 20:10 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2592">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Lr059MNtL2DFhsO6E700l_3CUYl0otRoDcPm0awn3FOvkFxJ8SZmwD_7sO5LrSB7egyo1CsZ47US8ARJYvpJHRU6zVa1HSZH2xk93TPAmcFgiFoyZaQX0Vpjf8-4MfzteOrYqZiFkcKIQbfEFj4gnjGofqdVIumhLOn_m7c140-v67dp28ki4AHD3L_B39B7n4Ke6paSNmbSw-eXx1i71Hn-_8xkB8vWmPfmBS2hYnm1ipHlD8y-8GhtrdLo1AeVT7OMMHyt8QgFMc2xJBDvpVWLvP8-ILNdyOkLuu4-G2Jb-W_Mjn-W50KwklhTal5AvTjRnSmA8RKEr6Mus9rl7w.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/E4OtsGLNdM8bWxo1NpKu8W7Ni-9VocQXZvix_eZmSkBcrtFGIRRELKdl3gsgeQG4Z69SaYnoNyqRSVdLh2JM4pl400vfEH9HXJzrgXLPgJAPYlZEDnJhOVbh7zlZk31qNG9WbQqYZAeDPveiv2-pcAeRnlwX8VYtF06WBfsDHdxUIuA61FXMTkQu_jyNalLuLPjBAJvrrw5vIVDMqz3_Mr0euYAgbhKJRE61IVeb095jyK58Soi2T1Rc56j2k927nJ82IOcz4ErbShw2sK83gWTsdcUGECpnxff2-nTxvoUn2opjeGzk9lURKu1-uYkbk9hjjSu0jinjd63pDsZl6A.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/mrk0C8ok29KRVaLDye4Qgs2nKIxUR348NtixaLJx38Vb2jk_zscIsKkoVBa0t4i4RotNHf9DYDRwEAPizUzTAUsXBMvVkWxyEoBHhyGhi_HqTU5iyKp3kloG6ub79kIWNDExpKEovj8cf9mSvQVWq_73Ck9D2k7pYtnjeSprqtpEjNkVFVjfLFSrfmvokjgtVXcwmMwqfK1AcpEQALtdtSpw21G-4kJuihiC1Pp5SZCWyaWkpKVcTWe_kE8xjC2qwAaFOpChNhPzs-WcZ7HiNg3yrNYltAiNyZy81y1wtkpAfaYUl42YMxw9-0tcCzPTyO2uwWJGyZxSA_c3CXjvcg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 28.3K · <a href="https://t.me/ircfspace/2590" target="_blank">📅 18:11 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2589">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/P05UPRimy_omMS_EA_3SIJDVwsmcPQ0R6sah03MiCUdRdDUShkT1IOhxu2PAn4boy83iOxzIl3Wvq8a6ASOw7A7cPmsbye9NifuMPTXuXgM0574rTkLlm7amm5gAcSdrRFAsXooWH_oAlCphdCsJekViJjx9rELmcsw_bX8aOX86OA0eeNqoAmvhKMjnoRkA7RT5FWrIm6Kom6pYjp_BUPajAM_s9t6b9W80A9y886sQfcbYtZzfi3aXFxmrLuGEKMUitBCpWF0mOKOos_UqpvwVazjtEkG_nXgHkntIneRlV0UfvmEM3gPD09EbSTKi9otRIVAP2xqXWImeMjGW5g.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 30.4K · <a href="https://t.me/ircfspace/2589" target="_blank">📅 17:54 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2588">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/JkWhVl1FbiSeE4MaLe4MUdvEZUWQI70G_jywNKpLyViViquId-XPNbXMxPzcv5eTQzwyfQFdr3AZHgefSGM0OL2o1MXWzGJazaCmW3YUCWwBUEMxKU2flVjJ5I_8FvTbYdXNR9jn1yAYC5Ppptjl1nleppKS0v-2QPmyLDS4E82X_IkqATLnrVF2GHMbgcoeZTa8jK2A1O3y5AlRoXtlPbrRpRuq1nrlNu2tuac5TRBvSWevwitai4a5xqFEW39JaMB9Sd-jgVY1SimUTFJ7sleZNoRAjw9zn8IUFVe3w-oPlUzQy9lTcgHnztTCwLbM7Pz0kiDdcCZd8vgVFPvyew.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 30K · <a href="https://t.me/ircfspace/2588" target="_blank">📅 17:22 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2587">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/NziqpC4eIXaqW76raZAJsrhbY1pj3znyEaYFqXUVCp5Wj1-lRSiLTYtGXSbSP90oRugUNMO7BABdTGEtSfBjxrsepN4Z2fFmHUTwX-e1HCHDer2kunUS6vc4cYEP0qTRCjTiMyyHDKjHT9-nseqSSAuwxQK8P_rnLYWwrjN7_jHMY6ASyNvWcIYipYC5qDcAJ2hMhZomj9F2ksGyqtJdCv38rwgJnWKG4aofO6SQfcOddR-mhAYsLi3kNv1MQ9cv-TeKYeIaRIAHyaRtzl65b7OOt50WR-i8phDaRgVL4H0h7YJ-dlPcXa_6KNjvJ5OSh7Rqg03Ca6UZ1DHhw1k9PQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/KcTh3sgy63V6o2idyT0lZGyig4gx-wzvm3XhjZXp9H_3LbQo35TFPTGB3NA2MDCWxle3ILe5ic8c5r5SmGYNU5MOftQzxDibnpIkv9K-UwXDd8YCtAV9hDkf1V1C4jwINWXMZP-f_hx9ndBOhfHXQBhEypk6mYXuUR6EuY5MkwSpXK83px_Uk8JQI6IMJqP9jpGqtAjx_Y2KqwxSR-LXp6dM4WmedPdo54LLcyn6cjMsoOSuDfmKtrBfHIowJN3TxrAHApwNqycNd7NhAInea1cDp_IwlQE_cpRx6pta5m1EPAjLM95nlPR8_FpSZkTcm_dx7FRkkeB9MurgFMqemQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/OdPhtyfVm7n8qfmYuxGol7eYE8i1VD3PorEhtlpLgnmbvNaX7-HrnJ_ThNJd3BSdRWAO9Tt4xkoZvSdhrrkbzbgXtPvHkM2CznQp2X0MfhCkzTWdtvKzE6zl1eY_MNxRZ2Y3NaZ3B5Pg6lUe3iy0_c7tROCLvPPBnbECJ5_WnvB65CM2Yn78HCqCwCxq6ZHXTE8JL3s7z8BCcjeJFjsKNbqMNl9K4FT60Rlm-dmdzJgZVdCwOBv4WkfA-ardoB7S5NPtv27i3e6kpu9AWckG8eWWo23stg-Hm6C8gzsVevKvGIt8FdVsTsjBAtARyaONugdgSrQo25CX0JwvleKIqQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 31.1K · <a href="https://t.me/ircfspace/2585" target="_blank">📅 09:02 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2584">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/inJqM51wgjnmuBEDNg5XQdXqcYmayKu9ED3rc0fXZBJe4a28I7_SZ47sOZj5qQd4ZW6jeAeqRbmcKdqfqMzhw27HUxztEFa9uWVgT6loFu75u5JM6hctThixFxRv6gcNrRZCDMgGK2z_K-qjtUmdpxi2Z-ty0QbHeiWakx0gduImn_DgfVKfwYWFX1snmk42JOsL6FknEPwMn4pysdYg7F1DoF4gdL_GV8qfly73vSQJ-pXIRtQ70b3Y5ZrPNEDJmAfpxHHFKt-X6MoNfSYo2rYh0KjNR2SsaZNl5KOf4K9I-V1t0JtpAnSAMM-hnE8DZ6sFmYp_hLvGJH8SGqNpUA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/kcxFm09rdWXPlthn5EGLttY4G1udPEghOmtibF_ini8Up1ifqKMfr_Q1lz5gsvp5ACFNcjdQmrWQdm5E_MBAIGMfeKM-gN0yDVe0MabNRh6lpy9qM3wOr8GgBRixX3Wy_YcfTZSGKnKFmlHcNk6BmPG2Tdr5ozLxbFa-Lioef5gzxQ6C_tql31Jz_7CCGEFVpPuNlqh1CB-k6NtR8snDNagmU0EwJTjZkULlM6n9MT-OdvnDMAFBOyBzM5PMESuQyvo5CrxkSmVPsxxfVvuBu3Zz2-26ME27lqn7BuhYqnwclL-inU4Vh7tUsEcc-LlWjZ17Cy84DDznwEQ8aqLMaA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/eBd0aloOFkSmBgBO5rbjjIqy9FPHYhv9qmWt1FOXJL8OywQDOC8b93ttFX5FGa2kXhAegCzMr4KQYOujkb5a_CveF53WcCWah_qgJixz6wV9jCMWytVrALjanAwpTVcsPFALtMwBZ7UsnIRIMsEHebrqu0S7NA39i0s-55OZqnck8BfBBuke6Gwe5HF75EhHAvrsGmBePGpNjFUYL-rR3vK0PUmlU7X3hsREtdwrJprpZWeEQ76P-UJkmIIKYGFOI8Rb6qUrJzXGKooiZhf2vYwDXjrlIUHuoMzcagG00w6FpMHUq8kMD_rq2bdwlEMCJPkZYD6tWJlVVnesNjwDIA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/BSrMntJVkJ6SHPONItq19wG_sYdknEwGJsaXl_4RER55UpD9uqdliO5JyFF7p_vBcMLfxAT7pnh8KWPZL66SCGwBGvZLEwMuTg_pgh_D4D8tVrWzM-Fh0iqlE4wfKm9E16eqFCgqK4WF0Us4hEJ_LQ7TCt8VIUh3OugCKO1O0NUbLXGgk5dhDfnKpTQHbxGvimGZjxuRehUB9eyFy0-JE6zzdrapUU568p49eal_Uc-MnW-zX_7a4pP4FUMPICDJAmpoSJ5kZ8USm0-VTqjxcmVvHUb1KxbGQgGieGV1TUzvEHg74JaY7PSUNNiFwBrFiCq2nhRAdTn2Dmfeu5_S-w.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #34</div>
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
<div class="tg-post-header">📌 پیام #33</div>
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
<div class="tg-footer">👁️ 29.7K · <a href="https://t.me/ircfspace/2579" target="_blank">📅 06:59 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2578">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/eZO_JXgzCxlXIswW3Rxpp2l4PdoMhIlkm6k8gdHOtcEMho1JDGOjGcMUMHCBVd6PeY6Jrj5gITFeZUoWpRFBVfUrOQ4VKOoi_Yx91d8zPRY62kaFyI3s7Exf_pxI_OLzDwXUxh0RLEVHu2Iv_WRhhM3v9e2bHpMlN-nL56gLcDkemNEYSrusGju3sxLwqMpEQMDueX7lWo7oYE0iK8gO2GOHJLSWFZf94innyOQn781wEpnZfR9ofIaHgH2tla_cxmtXCa-zXGF_c3Naaql5yxaM58T-cvWGJ-DPm6_HcydbXxF-g5Ha20RoR4KFtsb3ycWzJVKqzw-vY9d8TYTpLw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 30.3K · <a href="https://t.me/ircfspace/2578" target="_blank">📅 09:57 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2577">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/lPp50ZzROD_7H9A1IpvFx47Zo2NyFUPwgzZUpY_LnqDYTD9hJu-Q-lJaX_pppT0Z1xSpbVx-y0l5OuTu2L9YwFFLoNOU0LKE2N6E-GCHzEILgE5VHNvo_1BqBna1q1H-OkMSbpeUQpEbr5YZzoiXyNf-m9sGt25gvtDhFot21uL-798WhL9Ky6l2k9OfyMIqIQ88-qQhe87XR87rmfao6Acf_HkLydHd3jE0wdwVAvptUdW2TpYS75hrJYZrVSlNhRcWfwgEcC3MnchET5oUGFuFnP1aIIJOYoSM3iKI72Y64Jkib8Nz_lU2DMCkx-WGd0D8tSdeW32uwzXWVzAOIw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/KM5gDaN5Y4QW-W4HwEPgrzjj0VBz_j-Bzous8IurlA_MvoM_OsE276MY6aO4hDLeKylcTeymUPc2B739Ffwmo787SEtOeCfwd7UCabPdS6zMMFgu-iUeb7b2BfHhHlYF3Mj4T9Q3E-0pZhoq0RtsewMmhNC10_YF6_D8WddMkcnjri-GHHVqknp-19Bj0O_w-VAKdsInoOlXm3Tp1UGv19IdC1P24Rvi3odmUww0lj8mMxZvK2VhinDe5u4jMM8shyDWrtqMerI4RGbW4Inn-9-6kv270IF94sXJpp2RcFPkg9jgDSSkVqQu11U7bhn-xtopbVVqF8W-T7M-NQqBeA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #29</div>
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
<div class="tg-footer">👁️ 43.5K · <a href="https://t.me/ircfspace/2575" target="_blank">📅 18:47 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2574">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/T0ERW9q1g8QXqStzSPG86thWbbQ_DBml7DszjjJyTaGFDlHtb_-Bksnaqmu__c9zMSfv5ZBGG8H0QlIq3_w5U8WlJzqI_mnfwHgSk5piOoOlBq5bW5hWmRLpASFGYYav-KslIxNkV-oNDllIZI8ZOZAwrLYcOcjWh9XCyFcAxOHA40LuZcoSWF984_9KcG2DBW93yaZKZrGkBZhPRFw1cQ0FHspzbeOi3payKsF4kWmkGmYZsU8OJvPgWacq9rZR-lP5KLJZb2V7YPX_8tVcceBYXBC4kXvIdXyoUI3t22m1f9z24tg2SCHDYg9B2DFI8DORz995OJAWRWdbcVoIyA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/HWwF3ChMCen6Up2Dq3elUYzt1Vmf9eQQGeIbx216aH8pVG2TDeV9TwmSstG0J4sGCc1BY9mOCo9oVGfPCG2HaKJOClS7jDNb0hD6XBqYidahjDG9GvFX4QHJDq2ftSXq5BYdV78MlAENmCIOUGRoKuJvufvyITSZrfNizGYzLwjKpSQxkk3ysKluuzOa7gFtl8dV1Y3ncpnW25MkJVJ44tmRgDh5zDaY3-qXoO2dq2ku93mcwxD1en0M_EbLrbQM_leC_E76lRO5EgFwA5wosFqdc5OVr_QW6yZpERfroNXuXHkEkIck0VjP0liLJGVaH58xSrSEq4EqbjpG98cdwA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/FfnjknXaais7ijPKDfg97b3gn9uGlGOR7BrQfONL84jYGjs8oRkE-dc0ft8o15nTm9rBRdi8sQNLEPcDT2VUgpWt527esqPBnuUcwzG_TIWibQZPpSYc3T_kLKEimC3pgJN2Y5Gdk1AlQdeS4yOvSwSW2eFrnnMyhSSkjABE0DJ0IQyqEaUFqTZVw0OuX0cUA4oReswd-Ms9TQYLoDhEFNf361C8UJDDg4UKh15IqPjxccGLOm2pm0-aYM4AAZpDtgyPDAMuacrHsDAVijMdmGFmPiW5O4FuQhOYF36Ljic0cGvLw3lmYY5dwRDBu-pEcraEq4oPacbitqAXLoaZ7A.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/RDBCYkz5Pwt7kBoUvFSRglNoXp816u874k1IZKS0wGG3DaZ4WP51d0PE3Dzn9bHojqepFLQ4AY3k_LDPRB39gYX4XANHvY85ZQC-tWXgm0JpRuBvt-tKHwTycInmgZkAW646sF5z6NimC_ZenO2ekLiEZKoeb2jDLhlPCCEx_9TyyFdXp9-wjGdsRRnGRm4QN5omck9Wo5sPXDp1cug2-9OLpaQo4hV7eNjTXxIYZri_uBdrH8wIxe9qBbe44DzZqH9DvGPyLYLSCVJ4hT_-U3N6tBSTFN2-MLpqvsI3VWNgypu2juQxmkZ_eH5W21YaGP-0TVsp0xNHkVFwY2hqxw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چندروز قبل وزیر گفتاردرمان (و فاقد مصرف) قطع‌ارتباطات گفته بود "اگر استفاده از فناوری‌ها به نقطه غیرقابل بازگشت برسد، بخشی از حکمرانی کشور در حوزه فضای مجازی عملاً از دست خواهد رفت". در ادامه "بستن پرونده فیلترینگ را یکی از الزامات ارتقای حکمرانی در فضای مجازی دانست".
فقط نمیدونم مخاطب این صحبت کیه! اگر مخاطب مردم هستن، بدون تعارف بگه بیایم برای پیگیری و حل مشکلات وزارتخونه آستین بالا بزنیم.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 33.5K · <a href="https://t.me/ircfspace/2571" target="_blank">📅 11:34 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2570">
<div class="tg-post-header">📌 پیام #24</div>
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
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/oVf3tzoiG9XbMXE8RPz3mF60tyGLOOFarFj2al93mgJODLhuhsYFCUq84eeJP_cC2LnNKNtkyMlqXZkysIHl-oCroCECHBrW4MlyWMMRAm9ghkTSSIa8L8en_hvsAgR3d6bHA34gYuR2NTxtZYVWAcG0DkluxOOlyvcC8BKNKMl51qbs2J91PZyE0woyBta5o6eWyTMvkwutmBWJxIZC2V0tqBYARrezZu_olhGdjbMGrRHsO8XNIaVuCQR1MSZcZC9bguf9OHRhP8Ehk-yX0noOX-1UEdc7JL3s6-ShSaSTBHCEVwZTCFQVeSP6fPdjGqDfCqdQrxT1LX7DwyPDWA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 32.9K · <a href="https://t.me/ircfspace/2569" target="_blank">📅 11:20 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2568">
<div class="tg-post-header">📌 پیام #22</div>
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
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/n-kl7s_VxQ_t8uF0onnqgVocMLOwZG69bZ9ja8FEZUeIHRlXnwJ9cB-3LK3g08LjnRgyT-yYmkoFXJAxridRHnF0XjapdM_eMvncHK5wWa_TVo_yK_Gqj3xN6xotU1utZyU7dSZvb02dcs6BvjtqsryqU1ncvW0W4tIF3CNvaXbY_3sjKn-F0cdmERX4pQzPUxQvTyqSUWswnc_lGgPM2casde3jGrEpVWIzu9SfwOFHijq-F1DcQJQEykDlI_fWRLgK5vBr2nwOu-Lx2zXLhOcJ2UyEMH_Mdbf09AwU1HG11qIOzvuvPRCwGQfEgCjCKFrQacemzOL1YQEysdPaUA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/FZLPHK_RVqRUtAFhqH9EkC53UFgZZMdwP9AW4tuCSZsQAyYZu_cNKpyTBMpyCKiCoqCqXcaXzoLcSsmX6e6u3tnddZ8AqtYSUXA0O_o_9PpSCBPpMdAFvRaugQoUCRHyvmDmvSGLGgBLM3YX_75cS1YfyqN4LqArUbPZAauXkz-PXsqv8kAXh9hExCDXU6Vfp8Y5R7JVPAo_BiMfbIJOt8wJPnA78BFhUfZJcHNLr6jlQfqb9xvxp99xicStW4bMv_LFHTwwRgqo6vCn2n4UUY4GzBf3kTXkVnYGTvjzZRMBgE4ZLLlZ3Di3ZYRrK3yib40SOmoE2ko352fLbqdfaw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ic6zoHa8PxqrLXNYnQP_131p3aHDtyppkTj1fbs0KfQhO-zpaRXTsIZhPmIMH0n4ckh4Pu_1pCloeHlyi4J7MxgPywKur3gsdLGQiCNFI5eXVzj0f4Lh6VpgKwoyvUzbv4FeABt4Z_hsV_7S_0lKROMYv73KwZoeG6pTPnlODUGcH_XBV5ZZE0SE4I19AHcMo0dP9Ta-MjTmmf2wqBXngcAEF5PBFONrM8ybG5grWgTHUuge_f7T5t2Pf5Y15xVDJBIy8eE-6tNj7pNPJyXw5-NudsJ0Hwg_5NqJFCx9FBdLm4gzMNosOQWKzsOiK8beho2TiJVD_GxrOeDAzw9-bw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/lf_-_l5lDhuU5HmnkN5tbb66Uz6PQZdsoF2Bo_c9UVyGCxQ-ueRVAnFTCzXWFAhoWhZTdtZW9VMB6GsKqBa4-xfjrx-Ci_pC0ShW6PMdj1Xa6QIjzSgpKZL7T2uWV8X9EaTMnnv9Bfh3unBlyrAMbTYc-HznZIX2GoZqZw4EBlLPUzeqPk24cLpFs3PxPIYzh_bLEwh_6kx4sq0pL_iWlAKLIqTzCvI_s5AOFlI5_3dgro8kI9iiKnUl3lyi3zwquovGUY07TMtrFLTQjpB_dGvoL6C6CP4unQ9mmBYLEQUAaeb8RsQnygCe0ASUCDrWom_O0AtmTrM_v74jsTm9ww.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/GLkdPQBrYU6v9PTpzL6rTZm7kR-6TIlPrTI2qmdpYoiGl7OUwQr6XERc9TpexE7s-6z2r9EV5yAvq2No2JLveP3mQv4JLxW7fcd8f2EBxTHX8K7GbDQBumvGZG4qVavSN9ItwZtvzBScVWpv4DjEwslCMZbipYgCqMV2-fpfNdYKOWLojFi1NUEVnMi0pT9Urhkx2QJitEoPUS9wT0dmrOsg1MN47bD6x4INI730ek4I2norIhzZ1xCqbYxiZW-tJAQy6JC0rf07ix-98ony_NuhFuXu5dE4hpPr3C-rlGfIdYgxVb397oc-TZZtCwqZO9ljign9beh_UkFH5foA3g.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/b2O5J37M3G_xT83FY7vFokTGu8Y_6xXOXdbzBtKqD7P3JpmiYfTCufRm6eIXpaWdPhfp85RGDPFKrivQSuVNxXFSI6AOT3Rz1f2Lt2MuZbhvweiX9Nlo4B8cAoM28LXB9CICmb5ndV8uDSQCDspeq9yhhxqgak4H-5PhirAt6fCT2fmx9Tp1gw4516m5QOq1PEgnZIFVobZojsm6D3s-6qIuv5p59Zhr-dxW5zbvolJSDGRYkB9xQ40sbJnIz4rtkyFbiYZf8TbvsZ3qboh7yywoyVoJlYF0-Amz6GEsEF6vS_i-gxbn9-q54qDh_LqpMjI5Dl5gcuoervARKSxEvA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 28.7K · <a href="https://t.me/ircfspace/2562" target="_blank">📅 07:39 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2561">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/bZMjt1Bfi_n04ELsNjLl4SNTeMmf-rcB-1vRs_cPdYbO_AF_bWKFPxG81aiLaxtCwZlNrvQM08_GWmspPTtkrbduuIGAlSz4qqCICT-Zak5O8hoS_10TiFxcNqn2I-ZwapFEh-b5WBdHUlmM0fysoGzRszeR-HxZTv53aRy_Xr_f09KvHB1pzRylA54yhKFtf3TmgPnLqw-anBDzbNL03Xedi5gTJDeTTxI7O6J2LQprcttZ8SEYlZPmLjctgUq2pFXlIHQ0eWMTNs-Hc9iMl3ASMBKraKD83J4q9ZHgr5Y2Ocrblb6CBJsebDT6IEfXBfB9GNlA4JpRjVvYmet4Tg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #14</div>
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
<div class="tg-footer">👁️ 37.9K · <a href="https://t.me/ircfspace/2560" target="_blank">📅 16:47 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2559">
<div class="tg-post-header">📌 پیام #13</div>
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
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/R9pC4M8ug9KlK5OOdAjocu9auF-u15HKNAVJ6Qb2moWULudvzkQQ_N2Z8vdhP7oXL4i8hXfEHNELJxKbeOni1qu8xYFVllt4-q7dVuYv1jHLE0o7E-AO0UUvCpy-SgftzjNbIoH_UScHpq6nH3ZO1v_8XrZ5J-nkLQwitEMKJ39rdpcOHIJi-Zog4EcLUKJjXatHyA4EiX8-BPA6LUMVF-ijsAMubC5ylWhogbiQRXn3mnJMlIU5wYKBN2B0S1gA8lHSnTW7mdnBKFkdV1zatOYrDCM1okanHlVDMkIS058jvfscHdFGc5P7mHhaVk1dJ44xo7Sg58JJBmlq3r0x4A.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/fxWvMkp1Neaf3z5YM7r3-SXhmNKB3LaPHfOmVCEV0xa-IEPUCAuyDE7jBskrvoFl9mdLlWUuv2Rzsd_hU9x8QB85t8bfrG9TjakmxtdNHp8apgHuG8M_uDgzwu0gckbfXrXh_zgZflDxv4_EDcssZRn8Gz1J67RTWE_aJf9RdB4qkc_qrObHxSjVcQ_PXhQh-ZCfq2-h-lByk03mj9_6BC18PkTLC0kL34Hcz8n63_M8HlupD8GmrkuSCN8QxhEJ2fSw2vEFHCn3TS4IBFAPoct7c3o1G-6GUJu2UCwOeGhf7bWAagLAshBTaKr3GSrzpBzqyEH2KPsHohpkJRM9Ig.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 50.9K · <a href="https://t.me/ircfspace/2557" target="_blank">📅 16:57 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2556">
<div class="tg-post-header">📌 پیام #10</div>
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
<div class="tg-footer">👁️ 42K · <a href="https://t.me/ircfspace/2556" target="_blank">📅 16:41 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2555">
<div class="tg-post-header">📌 پیام #9</div>
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
<div class="tg-post-header">📌 پیام #8</div>
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
<div class="tg-footer">👁️ 42.9K · <a href="https://t.me/ircfspace/2554" target="_blank">📅 16:57 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2553">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7887a97904.mp4?token=B1v8xhGUn5RrgDVx1WnhdaXFq6HuSClMIQzjWccJ7Y5ZBu2eFSztDVTQGqFs7aH__vC21CW-Lf74kIDODthy8uP0eAHvN1Dvw6hNojNnPDGhJhEVuq5ev6gHEDEww-PWflAl-fz_h9yGsCM2Osn2HURu1izsJcSs7fn-tYyKsuR6GgdUO8y6Z6lBlRZQLvaccQ2qvPuxYF3NUFgvxCcjLoWBDbsTtrRLijHkeu1zKOWdwlen-m9WKMnZ4FyRGX-AtvzbWxFjHLLikK9y2ZYhQ0o0IjDKxJRA6OYttJA5BZzkLsVlv0Qg5XlzX5mxgCCmQZLQ5H6-p8TfIUy0RkxX9A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7887a97904.mp4?token=B1v8xhGUn5RrgDVx1WnhdaXFq6HuSClMIQzjWccJ7Y5ZBu2eFSztDVTQGqFs7aH__vC21CW-Lf74kIDODthy8uP0eAHvN1Dvw6hNojNnPDGhJhEVuq5ev6gHEDEww-PWflAl-fz_h9yGsCM2Osn2HURu1izsJcSs7fn-tYyKsuR6GgdUO8y6Z6lBlRZQLvaccQ2qvPuxYF3NUFgvxCcjLoWBDbsTtrRLijHkeu1zKOWdwlen-m9WKMnZ4FyRGX-AtvzbWxFjHLLikK9y2ZYhQ0o0IjDKxJRA6OYttJA5BZzkLsVlv0Qg5XlzX5mxgCCmQZLQ5H6-p8TfIUy0RkxX9A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Nq95qpdFqWP-js6hzZ8X1Jdd8aJzQXVpoo4N4j69i63u5dVjfS7ElC68_vVY3uMArDTRGu0VGbRrHvxjM5Muhx_PsLcW8tPNz-0-VSEwum5BF-Bve_yZeNKGyJlHoIM5c7Qa3Qv6WfxUmYiWLIS6yIb8KRwQ-k8fcyFvrC9OYCScV_S0L8nvYgOahqG2fgPZkkpx0tpV9Uzpl3ke5_6Pmgqc8yTwQZ81fCmjFKnuDEu4WJh_o6szx7zgduIOx1q3MX_U1cVz1PKKWCkWh_DDoDrWv5Gu1oY1UFzv6nhPb0c5D_RaRkvdknqBmCAfiPHz006RPU41s44h5v9ysT0cRg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 42.8K · <a href="https://t.me/ircfspace/2551" target="_blank">📅 10:08 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2550">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/QpGKOPxKnChQehl6bPrhbAlG-Jh99SYXyUceZCF5JayM_1H_CpCIjL9xz9Nv7b2wH8_6rxdvsOBQMSSItTxmEqscNBI_27VLbZHjbqaoKhUU3TS8zMc5IDCn7LUX7TGAJvNiG-UOswshrAsxuGcky5nzTUmogCfk46B-fAwuDCjEMb1pgDMs7U_9Kwb6IduabC8ZK_-ucmQBtDQXp3tkpDVn0Pb0PLj48tKOp7Nl5mhaB-nWZZcNZxas5jWPQuafE72CNAECbwQV8Ummmg9C2-_L6l_Dsj5Y7NeZoptx9S0LXTDsQ23xQdT9JEANYeOuV4yQFj9ETlMMD_3v_yI63Q.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/NJ8gsttFkRKAEJ6nYX72DwiVI9NngAru5WjnOw9a08tTR3FmKr7rwOr4Szmg4fVD7B97ssLanHGD-kf6Ni-E0DgCOXYtyBHARbnWjTCcuCEu56andLz_e6lvucpBi_qA1i_WNh1oy5dA8NVFoknF7YtAU_9ifPtcw0mmIx9QyLQQlSUcFOkzti2-7AG_sxzrOV5oMrkdzTLvj4yae9rNxfeL3uBaxQYXM0pJnkeUjXxitzDoDCBqyVhqTAcjKcuNfXS3c9HWxNBOCJrr2f6qqfZFQhC1f-nyXFL_inZ3boGaknXYZkaEuZeIIR0aXn2v8MJlU6Rt7NUYt-GEeBVBEg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/sWtP3EwwQVhSzXdUynN3i8TQaD4eCaBRZmmEn0O376l5f4qHEwDtm6Y7T9PLO5FyylrmzWS-Qqxw4MSFchEG_QSpEbw7_HGj3WTJT8Me3gj_N1vynghxMapQsYeoB0z8_Rwd5p3xHPuqlyvs7woost1xExieZGZXqJixhT6LlzPwv2FQKfoHli2ZO_1aYSItINdJ2_gtuSKGzG5lGJADukgq9kZB9mE69daR1zbn4EwW6OdrHkMIN01blH1lxay3U73_Etk4NgH21qOo0w5WHE4YA0fxdZiW4tf6DVHhhz-xfxtoQxU2xKRPgGfHTtjYRbpO9C5JR0low_P389AhcA.jpg" alt="photo" loading="lazy"/></div>
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

<div class="tg-post" id="msg-2547">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/TXR8j11AQPDfLw9-9I-GAOzW2l3XKAAvFWP3ZJFG-Vf10nkY3FFHyihZ5B5AYZGJRZNCiqWr5p6qNlFG8qrziaZpTuhqE9MUHTTWvifsENjl2j6eq-vjeArm6NxhewCkB9wynUE0nZiIaok-OnexHB1p5ht62TKbq-Cj9QW2azjytW5X4aLArNTE2nmvRoSy4yTK6Ut7sjtlRTYc6FjgR9a1M7y97fhu6Q2DGKLAQ0MWfvqiDGoztrryC9OsagYjDwDaXWXGT0MfT_IPGA3eRkpAquaPQGzBz22gq7VkJdmE1mUyeCl3z6_OMyYcrk6EEm5mmLJ3ppsWwpYYfK5gkQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">همزمان با قطع سراسری اینترنت و نابودی هزاران شغل، هزار میلیارد تومان به پیامرسان‌های رانتی کمک کرده بودن! همون پیامرسان‌ها در عین دریافت پول بیت‌المال، اختلال داشتن، ثبت‌نام جدید نمی‌گرفتن، محدودیت‌های تازه گذاشته بودن و چشم‌وچار مارو با تبلیغات کور میکردن!
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 36.4K · <a href="https://t.me/ircfspace/2547" target="_blank">📅 09:36 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2546">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/UkxVNI0lETUMonXbV7-XGdieGc72qB8gpbMyl7ilWerkRqtXoRJvYADnUcZ0iT_z-ze0OSrWXXRgIbUhGLDc1qtFUMO5HzlN8fK9zxFGHwq1u-ubYVnZgcog35ahGEdPM0YzF-Q6rua-hmr1mDtOInuUjNob5biK9W2StRj8NMWP1zgmQnqrP5swdIagm1QCWzvqJujSMfAOQomQIPhSD6ERxZ0xu8mGJJMKJIgl2kvGGEy2l4ZsprtKoKLPzN92tXhyVjpmHdWlidklgt8RpOKW51ToHeltpWZwWa2c4by4jMfn8GKpH1JmHmWclqYz0JhjxcshHViROC3Q090AGA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">متاسفانه عده‌ای از عناصر فرصت‌طلب سودجو عنوان می‌کنن اینترنت قوی و زیبای ما گران شده است. برای شفاف سازی میگم بسته‌ای که شش ماه پیش خریدم 1,348,000 تومان، الان شده 3,870,000 تومان. قیمت فقط ۳ برابر شده، گران نشده.
بنده هم با ارائه سند میگم اینترنت گران نشده، فقط ۳ برابر شده!
©
mrweb24
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 45.3K · <a href="https://t.me/ircfspace/2546" target="_blank">📅 19:51 · 18 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>

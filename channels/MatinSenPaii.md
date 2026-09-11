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
<img src="https://cdn1.telesco.pe/file/saKyz1vZE3_BN26axOTIYuC6kgbJog57axlfZSc3lb15_Cp5tkmC6RgJ3D3mbiY9NkZuw3i8CiClAx_N0cuo1cAph8B4ckHQ2_CTi5PBAfCfPWPelMVy_LwUskoMeueRquGesvytGf4OgrTWw-ZE4M4qBd6hZqm2sQfOLiOd3JhrCqMMnO1uFOUuvwRIZFpdXZWp9K3sgc3b1FbhzpKIS33zf_qqZ70aJSj39j7Tfdws71edf3hfjMvE4TRCPvhZ0KBLCrGmuq-Sv-4z8fXRnu7ZvCMVu9u0i3Ni2dj9DifReMeaU19M6Itwx9kt4hVC_mXvnzEMVg5MysjBQ-m0LQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Matin SenPai</h1>
<p>@MatinSenPaii • 👥 155K عضو</p>
<a href="https://t.me/MatinSenPaii" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 متین هستم و کامپیوتر رو دوست دارم! در حال یادگیری هستم و چیزهایی که یاد میگیرم رو سعی میکنم به شما هم یاد بدم اگر به دردتون بخوره=)•YouTube:http://www.youtube.com/@Matin_SenPai•Github:https://github.com/MatinSenPai</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-21 02:56:55</div>
<hr>

<div class="tg-post" id="msg-5234">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/bNIbQaiCuAu67LGpRL5TyT7o6b8zvh83V4ah6hYrcp3y-r8dPYpL1sbONNWP-N_O2Q-086pb3ilk5WSD80o9rH6m3Xy5yHIBC0UAgV3dZFcd38vAU2zePZ0zZmEbSwYK73gJbR7A38HgayhqRbqwaMANLqNZMG9A_94hgoNhrgHyvfQCDsSFO32YFUOy3ry5MYoyoUhfP9y8xwOpGzTlHHEdy4mPKKkOmjtpu75xj31hVGaGKH0MsRxxT_vFzzmr2XTSSXaC9anbeGS37mKGBjAvvchSBPn6D9NYqUiciCOGzgwoSCY_U9Z-yYPh8-Zc9evOpNSxII49LTkonHnlVw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">از طریق سایت Freestyle.sh می‌تونید یک سرور رایگان بسازید؛ فقط کافیه اطلاعات حساب‌تون رو وارد کنید. هیچ هزینه‌ای از شما کسر نمی‌شه.  برای ساخت حساب مجازی هم می‌تونید از طریق MPay اقدام کنید.  مشخصات سرور رایگان:  RAM: ۸ گیگابایت HDD: ۳۲ گیگابایت CPU: ۴ هسته…</div>
<div class="tg-footer">👁️ 8.87K · <a href="https://t.me/MatinSenPaii/5234" target="_blank">📅 00:58 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5233">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromRick Sanchez🤍ریک سانچز</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WKiekeOPkm-8vgd_J8svAbW_dB5Cmfo8bi4Ds2DVvO6Jj3FUHW3vSnzpD1D8LREKIXWxo-SLy1yP3lugo8iDIGdFRa8_vLiuHiB4Al-sYjNsNJPmv0oLq_xr3Q2xKrE1YCN7WzruUgVhzZ1VqGq1AuvZclFMoannd4CbPPB-1yWifMxx60jQD5Tu4_mqo25HcCTCOZ2gFvKA956Xb8t-tZsNIMDG4ydx0LgJl7uKe4Gs4GFxn9zwpRrfxSxDFYNVqyogKVAMwGjTyhDNxA3EfHPwWAdw61rPbiTZoRWF7e44iry5wMsG3Uco_K5sP4fwOxj7fuqy9J3f5QSqkIKcPQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">از طریق سایت
Freestyle.sh
می‌تونید یک سرور رایگان بسازید؛ فقط کافیه اطلاعات حساب‌تون رو وارد کنید. هیچ هزینه‌ای از شما کسر نمی‌شه.
برای ساخت حساب مجازی هم می‌تونید از طریق
MPay
اقدام کنید.
مشخصات سرور رایگان:
RAM: ۸ گیگابایت
HDD: ۳۲ گیگابایت
CPU: ۴ هسته مجازی
مناسب برای تست، پروژه‌های شخصی و راه‌اندازی سرویس‌های سبک
🚀
من روش هرمس نصب کردم
👀</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/MatinSenPaii/5233" target="_blank">📅 00:43 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5232">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">یکی از صحبتامون توی استریم با یزدان دقیقا همین بود که ما هنوز نمی‌تونیم سقف پیشرفت AI رو بسنجیم؛
برای همین اکثر نظرات به ظاهر کارشناسانه هم در حد حدسن. و نه باید شما رو بترسونن(حرف‌های ترسناک که ai ترمیناتوره و دنیا رو میگیره
😂
)، نه باید خیال شما رو راحت کنن(حرف‌های خوشایند که نه بابا ai جات رو نمی‌گیره)</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/MatinSenPaii/5232" target="_blank">📅 00:27 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5231">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">راجب این ویدئو که فکر کنم مال نیم‌چت پادکسته، حرف‌های زیادی دارم که بزنم. اما اکثر صحبتا نه کاملا غلطه نه کاملا درست</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/MatinSenPaii/5231" target="_blank">📅 00:12 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5230">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/dad69f2160.mp4?token=WV-Zl33AwgpN9w5VT8nnOyoeZVJORaf8laflhaQMnxwmunIkxiLxUh70zxisHwGV7KewwHTNOQ07Xifzxt_XZq7QXxBZli8V2QHt23MU1-U__MR8QiVSWhSo7f3UzddIssmaXj_onD5VzRC_H0tzr0Zeu8u0AT2X3nWQFvzbfWarH4jY-Dho92UNFC2iZpf6XGNxLxiAkmnb8xBnW03KRXTrANZwCbh7IzvhvUWlB7aUfVtzMO4t_TwCwrOd8lbP1gCud7k-cLaj5bB6WNEsYgxG_cM42IoufQ2voEZZjZfFHQIawWl5zwQxoUhEK3iboHmgevVS2cyEEOR721ATPw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/dad69f2160.mp4?token=WV-Zl33AwgpN9w5VT8nnOyoeZVJORaf8laflhaQMnxwmunIkxiLxUh70zxisHwGV7KewwHTNOQ07Xifzxt_XZq7QXxBZli8V2QHt23MU1-U__MR8QiVSWhSo7f3UzddIssmaXj_onD5VzRC_H0tzr0Zeu8u0AT2X3nWQFvzbfWarH4jY-Dho92UNFC2iZpf6XGNxLxiAkmnb8xBnW03KRXTrANZwCbh7IzvhvUWlB7aUfVtzMO4t_TwCwrOd8lbP1gCud7k-cLaj5bB6WNEsYgxG_cM42IoufQ2voEZZjZfFHQIawWl5zwQxoUhEK3iboHmgevVS2cyEEOR721ATPw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">راجب این ویدئو که فکر کنم مال نیم‌چت پادکسته، حرف‌های زیادی دارم که بزنم.
اما اکثر صحبتا نه کاملا غلطه نه کاملا درست</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/MatinSenPaii/5230" target="_blank">📅 23:51 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5229">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">زلزله خاموش چین در بازار مصرف هوش مصنوعی
🇨🇳
طبق جدیدترین آمار ماه اخیر OpenRouter (۳۰ روز گذشته)، ۷ مدل از ۱۰ مدل پرمصرف جهان چینی هستند و نبض اقتصاد توکن را در دست گرفته‌اند:
​۱. DeepSeek V4 Flash
🇨🇳
۲. Tencent Hy3
🇨🇳
۳. GPT-5.6 Luna (OpenAI)
🇺🇸
۴. DeepSeek V4 Flash (نسخه دوم)
🇨🇳
۵. Nemotron 3 Ultra (NVIDIA)
🇺🇸
۶. GLM-5.3 Flash (Zhipu AI)
🇨🇳
۷. GLM-5.2 (Zhipu AI)
🇨🇳
۸. Tencent Hy4 Preview
🇨🇳
۹. MiniMax M3
🇨🇳
۱۰. Claude Opus 5 (Anthropic)
🇺🇸
حضور قدرتمند Tencent، DeepSeek و Zhipu نشان می‌دهد جنگ AI دیگر صرفا سر ثبت بالاترین بنچمارک نیست؛ بلکه جنگ قیمت نزدیک به رایگان، مدل‌های فوق‌سریع سری Flash، و مقیاس عظیم توزیع است.
✍️
callitVer1</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/MatinSenPaii/5229" target="_blank">📅 21:53 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5228">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromxsfilternet | فیلترنت(امیرپارسا گودمن)</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qc3Q1_O7EoMqLeZnugukRHGb--H9VMtk6CaAf0QSI4bZMFbMMf9gZKSqcjoxp0BVG1lCiAt4CLpSafRY4drvi_rLy98vwyqPTX_I4ricZ_e9DekF62MtsYXJVxwlrL48BkhW_Mk9Bncf4Dn6zax0V6_oWp2GSWfROTShTGpRmjszXWHNijhxLQNtG7mv6_sZ0Q1e3MYlaVV7Ist1mIBfEwfIQn7qYcuZWXwjux9rfgoTR-ucLpA-nr1GKOlsaNB_97s40wGsoO4_h8sVeOa9QpGdO1cY6tE1nKrz9TJ7FWVLJnjRhe3JE_hXGUCrRmcJgbqMO_KU7I_JAGsOdVp8rw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بلاخره آپدیت کلاینت منتشر شد.  هسته شو تغییر دادم و Aether‌ آوردیم. MASQUE H3/H2 Warp/gool پشتیبانی می‌کنه قابلیت Chain هم داره با سایفون. برای شرایط سخت خیلی کار شده که راحت متصل بشید (حالت اسکن و Obfuscation رو تغییر بدید)  نزدیک یکی دو ماه فقط توسعش طول…</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/MatinSenPaii/5228" target="_blank">📅 20:45 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5227">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/QrEnYkgekLy_fukth4tJI8jPxFgRK5pkhZJMkPgatGtwvHYcSA4_n6DDYXCCEXv8hYaGc0wgTSnyglLnXfq-vwo-cELToA-64_MCn3AulXUBgDoc1j3zaMVD7fBZOn-zQHrkCIq33fQ44himPeHEh0jgo-OyBb7y2Mmla6qhmEa_rhDhpk7zDV5s3FrLS6NmXRLGC-L5e8PkSvEmfAAW4QtvYdzFkMrbTSjoTqgL210K4zyK0UvlGANUGvt_S7yJhz_6A86GmrHqn3P2Pq51zTJTmAvAuwmO9rfewaZnwXMQiBrrrpmPZ-BpODHW7x0nfXejLcGj_qF26w0GZS0nsQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اپ DreamBeans بالاخره فید من رو حاضر کرد خیلی اخبار رو تر تمیز بهم میگه. از اخبار تکنولوژی و ai گرفته، تا معرفی سایت فیلم و یه کم پیشنهاد آشپزی و سفر و...  انگار که جادو می‌کنه
😂
دقیقا چیزایی رو میگه که توی ذهنمن چون عملا دیتا سرچ گوگل، جیمیل، یوتوب، عکس‌هام،…</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/MatinSenPaii/5227" target="_blank">📅 18:59 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5225">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/mKUIdFoGxzdscDgRiPbm1vuDi8wy5mQrvD8AtUG0Idqvuma7nkGOT9eXrWLeyQDfWymnJGzdbHQp47o16_lp4X3BLEnoqlgkAXfd6He_lNy1nzkKat_n_8s6VfwxrSjSPNIsI27nj1AIwX3qrI70TL7Q9_N9tQ4wedZU7XmNDGH7vSs6IrpcYK6N8XXi1iBcSJ7UqZJHY8TTGVvF5INFk1MQy6urSvEVDen4oh_a6_jajEiUTFVz5sONHUTO-ficI5fNjYZQu2sSqg_R_z8psHe9FBI2kmJAZeAhXCvlW7kZq6Ua166GHqfSmUZ-gckQ6mBoRUj3qQmJfsbT3fJLDQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/R9v8qr67IHzYg9ZoDNPVNZ_nclREidIpvoOxy3bwfKFxbnvznW3_olpmN-oHc--2VrwZK7QMaTq9LR6BTs6a6uRzAfQDkTwdxado6wouAOyimswTZrGsAWZD5AQx0WGz1B2_PDYSJPgL-xEih3PbTHwfNMtNz9QSZaNWsZRgBRY8hn6yApYGYQAWbw5PEkvKt3evhtkBUH6IimYlwVoLJaYxzrLtaLxQklfUe_9FhylEbU0Wr7sTn7-MA-gbMSGpLxO269IRqw8BHAwuMaHcDW9tcA-KotfYd-OfTaAE3mEFheD6Ru0QpCFZshoIg07ezK4Bgrpud3jU8DLpdSN5Ww.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">اپ DreamBeans بالاخره فید من رو حاضر کرد
خیلی اخبار رو تر تمیز بهم میگه.
از اخبار تکنولوژی و ai گرفته، تا معرفی سایت فیلم و یه کم پیشنهاد آشپزی و سفر و...
انگار که جادو می‌کنه
😂
دقیقا چیزایی رو میگه که توی ذهنمن
چون عملا دیتا سرچ گوگل، جیمیل، یوتوب، عکس‌هام، جمنای و همه چیزم رو میدونه و همزمان ترسناکه و باحال</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/MatinSenPaii/5225" target="_blank">📅 18:28 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5224">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Tx2cf82-2fzfGWPBxAObMFnfu4-Argvlyi-AH4dTPUP7aCpjhby4QDxgulybG8MYiBqpNOIXKI2BxA-57qLqeLYTw8qMt0PKnj7EpbPz2ORCKcc89Wa_o40i-ADoSzhqsRO1IX6nXZBqThcYLeT5cfR7U_wZ4o2I_GGNKkD-16tdxNePnJYz_MhBFcpTiSI5q0CBCoAKuSX9SnGH619ndkdoIyp9Y7U2IhAcJvo_3LsMevHDzzUnblW3suzo6T48yOBoCorMJgQzWqDrtzUWaV8DTa0qPHqvMx5Mwp_15QmdV0sG-IVCtqxHApPIIvgyllI7EAVb2-mdvNvuOQ1HpQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بالاخره تصمیم گرفتم برای WhiteDNS یه Patreon راه بندازم.
حدود ۷ ماهه که این پروژه رو با هزینهٔ شخصی جلو می‌بریم. توی این مدت بیش از ۱۰۰ سرور ساختیم و هزینه‌شون رو خودمون دادیم. از Conduit و DNSTT شروع کردیم، WhiteDNS رو ساختیم و در روزهای قطعی اینترنت هم با MasterDNS سرورهای بیشتری بالا آوردیم.
این هزینه‌ها صرفا جنبه مالی ندارند. مهمتر اینکه با استفاده از همین زیرساخت‌، سرویس‌های رایگان و با کیفیت بهتری برای افراد بیشتری ایجاد کردیم.
امروز WhiteDNS حدود ۱۰ هزار کاربر فعال روزانه داره که در مجموع، هر ماه نزدیک ۱ میلیون اتصال به سرویس‌هامون ثبت می‌کنن. همه سرویس‌ها کاملاً رایگان‌اند.
بعد از راه‌اندازی سرورهای اختصاصی داخل اپ، فهمیدیم وقتی زیرساخت دست خودمون باشه، می‌تونیم کیفیت سرویس رو خیلی بهتر کنیم. الان حدود ۱۵ سرور رو هر چهار ساعت یک‌بار روتیت می‌کنیم تا احتمال فیلترشدن کمتر و اتصال‌ها پایدارتر بشن.
این مسیر با کمک تیم ما در ایران جلو رفته؛ از تست و پیدا کردن مشکل تا پشتیبانی از کاربران.
برای ما Patreon کمک می‌کنه این کار رو پایدارتر ادامه بدیم: سرورهای بیشتری داشته باشیم، کاربران بیشتری رو پوشش بدیم و روی WhiteDNS و محصولات بعدی‌مون وقت بیشتری بذاریم.
اگر دوست دارید از اینترنت آزاد حمایت کنید، خوشحال می‌شیم کنارمون باشید:
https://patreon.com/cw/WhiteDNS</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/MatinSenPaii/5224" target="_blank">📅 17:13 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5223">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">جدای از اون مسائل، اصلا یه چیزایی از این اسناد در اومده، عجیب غریب! ترجمه‌ی ai: گزارش نشون داده که یه کاربر Kimi اومده داده‌های نظارتی چین رو ریخته توی مدل تا براش تحلیل کنه ببینه یه آدم خاص رفتار غیرعادی داره یا نه. این بنده‌خدا احتمالاً فکر می‌کرده درخواستش…</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/MatinSenPaii/5223" target="_blank">📅 16:53 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5222">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/XB-0MBnR-khzRRLYhIlNeQO3R9Hz8Ui1zC7DFzrw86MRHtsSy--_RsICGni68EmUgTx2b4XuMNNi_tqYvPp9vGvv-ETzqJS3zyRUpl5G31Yez8LipuBFgBwai6yZ1Yx4TiV95ehnUV4AuNv3g2VTn4Kcr9mJHGhZmT4-9g2wPxOnpTsr4-vnbU4_wOctKBm6OR12jlBRmCGbAdK8JATsNH4Di9BtYmZSQuLDUt5MQwjbd1UEgdrUTNCi1BZEb64J_4w1gcBT9lt25Lj1HT1Saw52sENlANyUoO9lHIOrbvOf3g8bYL_YcqLY6pgEd12-P26FDCBjDUUGV4q6HpdP-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">متأسفانه من توی چنل نمی‌تونم به دلایل واضح چیزی بنویسم. توی این گزارش آنتروپیک، کلمه Iran رو سرچ کنید https://www.anthropic.com/threat-intelligence-report-september-2026</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/MatinSenPaii/5222" target="_blank">📅 16:40 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5221">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">متأسفانه من توی چنل نمی‌تونم به دلایل واضح چیزی بنویسم. توی این گزارش آنتروپیک، کلمه Iran رو سرچ کنید
https://www.anthropic.com/threat-intelligence-report-september-2026</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/MatinSenPaii/5221" target="_blank">📅 14:26 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5220">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/c2915137b6.mp4?token=oujb5G3MVpSlPhSgewh-y5gTiAYxgTEq4uKhHIcpNh7V2wqHOkDgtvGUZOlMp9xYEhmGdrkD2MQJ3Swivgo7C2Yd4TM0yqPgrtO9zygBfSSm_FV7vi2-fFfdmlYsyTpGl54a8uLQb5VRES_GdE4Zvtxk0bduh28a54NHAIa6FAAAmp8hQXGmoIAyFDH_fNTJqIkDOE5ZooOl0Txy9nezkJEkemNGtS9UzgKvRVIhsnLqI2IpiA-ZqYOfTPtN3XOTDcWksz-5CB7CAUgXJsty-vRUWjIjLuKQOuqfszMfa7hFznJFgzfDY9q-HHw_26yXL0PtbvGe1bmztMgAKhVJDg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/c2915137b6.mp4?token=oujb5G3MVpSlPhSgewh-y5gTiAYxgTEq4uKhHIcpNh7V2wqHOkDgtvGUZOlMp9xYEhmGdrkD2MQJ3Swivgo7C2Yd4TM0yqPgrtO9zygBfSSm_FV7vi2-fFfdmlYsyTpGl54a8uLQb5VRES_GdE4Zvtxk0bduh28a54NHAIa6FAAAmp8hQXGmoIAyFDH_fNTJqIkDOE5ZooOl0Txy9nezkJEkemNGtS9UzgKvRVIhsnLqI2IpiA-ZqYOfTPtN3XOTDcWksz-5CB7CAUgXJsty-vRUWjIjLuKQOuqfszMfa7hFznJFgzfDY9q-HHw_26yXL0PtbvGe1bmztMgAKhVJDg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ایونت رونمایی از آیفون 18 توی قم
💀
💀
💀
بدون شرح</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/MatinSenPaii/5220" target="_blank">📅 13:16 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5219">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/V-woGUZf8c0vYykYjYrMVSVPzPo0cpUWrrIfKxXCAVTEwxVUaJKhCcWMF174NVcxXIgXODJg0FbMGmdH3-5Zx_8O8U4FKPdShRORQtz4bD9-CHiP1EQjx0NmhRaWv0mz2XePFQPO5hhlk9KuuFq597amWesn3LyggSnh74u2CU03dXCEeakOG3CZ3usxZ3rlyY9_DYLKGaZw1s26o9O1sxn5HDYNZplydVOsXK-d7c4PZjR62lRAy2MOlfs18Chj3xXNkLOAEhZtSdvMqxBl2biZ5n8TfloA3aXEQvF4OVmwRlN2-GfHgd0-UdGVbyv-Kv8-bDo5skOQ2TRIcOThSA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">می‌تونید فید خودتون رو هم Tune کنید
که مثلا از فلان موضوع دوست دارم بهم مطلب نشون بدی،
یا از فلان موضوع دوست ندارم بهم چیزی نشون بدی</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/MatinSenPaii/5219" target="_blank">📅 12:50 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5217">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/h4u68F0kNWso6ApHEcHBPxx9uDPrNpek3hmMGhFUUWb3PkAC7eti52ayz2UhwkcLP5Wc0yE5Afx5sG0vxIh7jYdKa0RR5XTZGMZE908i8GSGF7FQuH6Kr1I6rJZoz-BSmGCPej8EkndAm0AgvAdF2g3ULbqsPvUyE2rP5r8ApRNnyoZNqQLZXEvlio43JSLdCpo7pUjz50yz5HTImgWnDJ55D9pgtXSfqm9tRpthqRFDs9Qvnsi-kxP1Dtt8lW2bfk0HQbI_fHgxZKMUptT5GIFTqv8MeNkc7rRAXSuwewzgi1IyAr7Bxv3_0_lSh4jgrVC3lzeOezEiGz19lDW7LQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/MC8xOqHOSfaGlLKlypNX0YUCpvsG6QabAgiHnZcQA4KnG6KJ1VLzjOuhXjUjXxAAzJmu3Do2eD8Wb6uhqDeX1pCmqjGIWsoiIzoQn1hk4aFakgFYIJHRQz--Wdb5CihbQwTelWIfTsPUma7PRxzMJlPtAfyRvvxw_r1Wj0LGLzOqmKfHZ0aR53A_YNNovnLBtOYzD_HTVvEHiyMZ69nnv85TW0a4H3IOfkdMryxmKjv_GoeHtKx3ROETvZ6SoPvta5v01CkGOAKJXwSxkA5Nbd6GCuEBrC2aYL176k3NNA9Xfx-1EN9hSN2wbOdHDcvQ9cnAh_uQ03x9a6g6R6_GMA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">من نصبش کردم. باحاله و تمام اپ‌های گوگلم رو کانکت کرد. چند ساعت بعد واسم می‌چینه و بهتون نشون میدم</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/MatinSenPaii/5217" target="_blank">📅 12:45 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5215">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromهوش مصنوعی | محمد زمانی</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/rzm77phY6L3_AKZOLXNRbsT7DhHpKLP0eyfCm9w6V1jTfltsPQMbjFXtbPD8j-bSiRPbF5OYzFrMGN4hykxoYkyKrbk3cxqWz-twajKl0lA6GHspaVGiY6kqY3vekbYFmF07y1eq3IheWNj1ys_olDGRqefJF9GvXgd73gOzwAayUMJM829eNcPRzD1vQ49hdPbbbdvSBbYvRk77rLuqOL_FWdvIBEMsHiH35N-O9b7yop9Xtzk-4mH-0r_N-8C5nT4jCkWgIM9J0cSdsXJRjBWwjW9yXPC6zVlWO5PUKRNouly7Dmnk4DJlk9i29QOnB1Zo4wMhIFRC53bzA0fO3A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/pkP-4-P6thsgdgStcKoPOqWriOHQU7S_Pfa4q30uZw0sQKeb2PQXKV4Mt2gQd_5amRB-sLfydmWur5zMdXWLWLK_fP0W7LOfbI4JjltvzHF_bkguwYt03LXLEa90TkNcNtlHB4rTuEaMFwG93_ItmcPyTcPHAEtjq9OBE2odbELjccjBqPszuWWgD_HRy1vdugbnIVD56BxXpqyS8cv2qrKxGUElSqTQxvXDpHiPqZ5GRZrpUE6MPWXRlWAH1hU-6eqB34ao-SvBuvnrSMdpBP4fJhhDneXYbXFxjiolk_eBRegxPnOXBLJWppYf0-dtBHZttn7rwbKh2p_DYeiENQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">گوگل لبز یه اپلیکیشن آزمایشی جدید به اسم Dreambeans ساخته که رویکردش کاملاً برعکس شبکه‌های اجتماعیه؛ یعنی به جای اینکه شما رو بکشونه توی چرخه اسکرولِ بی‌انتها و نویزهای تموم‌نشدنی، هر روز فقط یه مجموعه جمع‌وجور، حدود ۱۰ تا ۱۴ تا استوری یا همون Dreambean تحویلتون می‌ده که کاملاً متناسب با زندگی واقعی و شخصی خودتونه.
منطق اسمش هم جالبه؛ سیستم در طول شب داده‌هاتون رو سبک‌سنگین و اصطلاحاً پردازش و خواب‌دیدن (Dream) می‌کنه و صبح مثل یه فنجون قهوه تازه و غلیظ، خلاصه‌ای از نکات مفیدِ روز رو می‌ذاره جلوتون تا به چیزهایی وصل بشید که واقعاً براتون مهمن.
روش کارش این‌طوریه که با اجازه خودتون، از سیستم هوش مصنوعی گوگل (Personal Intelligence) استفاده می‌کنه تا اطلاعات رو از اپلیکیشن‌های مختلف‌تون بیرون بکشه و ترکیب کنه. می‌تونید اون رو به جیمیل، گوگل کلندر، گوگل فوتوز، یوتیوب، جست‌وجوی گوگل و اخیراً جمینای وصل کنید. برای راه افتادنش کافیه حداقل یکی از این‌ها رو متصل کنید و البته دست خودتونه که دسترسی کدوم‌ها باز باشه. این تنظیمات هم کاملاً مجزاست و تاثیری روی دسترسی‌های Personal Intelligence توی بخش‌های دیگه گوگل مثل خودِ جمینای نمی‌ذاره.
حالا این داستان‌ها دقیقاً چی هستن؟ هر دریم‌بین ترکیبی از ایده‌ها و نکته‌های روزمره‌ست؛ مثل معرفی جاهای دیدنی برای گشت‌وگذار، یادآوری قرارهای تقویم، پیشنهاد رستوران‌ها و تفریحاتی که ممکنه از دست بدید، یا ایده‌هایی متناسب با سرگرمی‌هاتون.
بخش جالب‌تر اینجاست که اگه دسترسی گوگل فوتوز رو باز کرده باشید، تصاویر این استوری‌ها با مدل هوش مصنوعی Nano Banana 2 شبیه نقاشی و اسکچ تولید می‌شن و جوری طراحی می‌شن که انگار خودتون و اطرافیانتون وسط اون ماجرا حضور دارید.
فضای این اپلیکیشن فقط تماشا کردن نیست؛ اگه روی هر داستان ضربه بزنید وارد جزییاتش می‌شید و می‌تونید اطلاعات وب، نقشه و راهنماهاش رو ببینید. امکان بوک‌مارک، اشتراک‌گذاری و بازخورد دادن هم هست؛ مثلاً می‌تونید بگید از این موضوع کمتر نشون بده یا «درباره این بیشتر بگو» تا سلیقه‌تون دستش بیاد.
در حال حاضر استفاده ازش کاملاً رایگانه و دیگه نیازی به اشتراک Google AI Ultra نداره، ولی فعلاً فقط برای کاربرهای بالای ۱۸ سال در آمریکا و روی دو سیستم‌عامل اندروید و iOS فعاله.
در واقع Dreambeans مثل نسخه جمع‌وجور، داستانی و تصویری از Google Now قدیم یا Google Discover جدیده؛ با این تفاوت که به جای پرتاب کردن خبرهای عمومی به سمت کاربر، مستقیماً از دلِ اتفاقات زندگی خودتون الهام می‌گیره تا هم به کارتون بیاد، هم به جای اعتیادآور بودن الهام‌بخش باشه.
▶️
Dreambeans
✈️
@mohammad_zammani
📱
Mohammad.zammani.offical</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/MatinSenPaii/5215" target="_blank">📅 12:44 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5214">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">اوپن دیزاین یه بنچمارک از Deepseek V4.1 Flash منتشر کرده که اگر نزدیک به واقعیت هم باشه فکر کنم آمریکا به زودی چین رو بمبارون کنه
😂</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/MatinSenPaii/5214" target="_blank">📅 12:26 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5213">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/BPGPrRbEv0uAdiWgUodCDgEcU6-JaZVtm4TzIvMqxjk_BXX2NRmo5jTsHUM6RGnU9tT67tGOJv1-ceDbECvc9TtZgnnNU76I0YoLViti-WTlAmZgui0hNocJ65QkhYpgYvyRishvqmP2qKNDA_8hE3aEHdFfaV1J5Pr5Nfh5HsX6fw923F4q_XhQpNs-MC6um0JlHGKDoMoHmoV1xbPfhp7cTHWrs1DldIYud0pJHB5agnkQyWFKj-Ro3jwOsUPh6jdm8RIO8ZQZKA0H5YqAs43AVkX6mQB1nmlXeldb_xeBeFXc8K97zLFspkyQOG8oHqVUhaFWm9H3ojvU0lywtg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اوپن دیزاین یه بنچمارک از Deepseek V4.1 Flash منتشر کرده که اگر نزدیک به واقعیت هم باشه فکر کنم آمریکا به زودی چین رو بمبارون کنه
😂</div>
<div class="tg-footer">👁️ 32.3K · <a href="https://t.me/MatinSenPaii/5213" target="_blank">📅 09:02 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5212">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">توی این چهار روز کلی اتفاق افتاد. از معرفی GPT image 2.5 تا مدلهای جدید دیگه‌ای که معرفی شدن؛
اما چیزی که وقتی دیدمش برق از سرم پروند، حل معمای 90 ساله‌ی وجود و همواری سه‌بعدی ناویر استوکس توسط یه مدل قوی‌تر از Astra توی 88 ساعت بود که هنوز در حیرتم؛ چون خودم رشته‌ی تحصیلی دانشگاهیم علوم دریاییه.
ببینید معادلات واقعی ocean circulation معمولا ناویر استوکس خالصی که الان حل شده نیستن.
یعنی تفاوتی توی اصل حل معادلات شبیه‌سازی جریان پیش نمیاد.
حل این معادله بیشتر شبیه اینه که بعد از 90 سال، بالاخره قفل یه در رو باز کردیم و پشتش یه راهروی تازه‌ی پر از مسئله‌ی جدید پیدا کردیم و رفتیم لول بعد.
فردا راجبش بیشتر می‌نویسم.
خارق‌العادست</div>
<div class="tg-footer">👁️ 33.1K · <a href="https://t.me/MatinSenPaii/5212" target="_blank">📅 03:06 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5211">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">دوستان من حالم خوبه
میام به زودی</div>
<div class="tg-footer">👁️ 35.6K · <a href="https://t.me/MatinSenPaii/5211" target="_blank">📅 11:17 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5210">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-footer">👁️ 53.9K · <a href="https://t.me/MatinSenPaii/5210" target="_blank">📅 00:12 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5209">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">توی تک کرانچ
یه مقاله نوشتن
راجب «
مشکل منوهای بی‌مزه‌ی ساخته‌شده با هوش مصنوعی
»
خیلی از رستوران‌ها با هوش مصنوعی عکس و توضیح منو می‌سازن ولی نتیجه‌ی همه‌شون شبیه هم از آب در میاد و مشتری هم سریع حس می‌کنه یه چیزی سر جاش نیست. مشکل همون یکسان شدن خروجی مدل‌ها هستش که تفاوت واقعی رو از بین می‌بره.
به نظر میرسه بالاخره داریم به اون نقطه‌ای میرسیم که خروجی‌های ai با یه ورودی عادی، یه‌شکل شده و کارفرماها برای نوآوریِ بیشتر پول میدن.
وقتشه دست به کار بشیم و از مخمون کار بکشیم
🙂‍↕️
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 53K · <a href="https://t.me/MatinSenPaii/5209" target="_blank">📅 23:40 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5208">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/G97sJAHKIVj9NugUzeNoU36k8RJQv1NRzuFClns_uuvVc-c9YWmgHIgkVZd00JROcj_Jj6m0G4tdOLjUqia80Ihg0w_GtqUggPSVd9OM6Viw-5DkAwJ7ndfTtWVhprY0KoRTdLDV2VIDlcuzzLXTuxUktWI7XPmoajWsGEjf82Kc4DV9JRQMUKGX6gRwxjSVDIeG70ligljMWTEoQSKL5LyCWYRajiXk4YxF7dUF2vMoMG5GtK7xDntE_XqL0Fsz5mWVp0npzWZ8yHTORv-Z4XBc9X556YYyjZm-WlCgAHelZ33CEZ-J0JeylJS8Yf5cQZH_ecQnLaS8VX90xNTKXQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جواب من به هرکسی که فنی نیست و سختشه که پنل بسازه توی کلودفلر و... :
Defyx
👍
https://play.google.com/store/apps/details?id=de.unboundtech.defyxvpn
البته WhiteVPN هم از لحاظ راحتی و امکانات برابری می‌کنه و می‌تونید ساب خودتونو هم وارد کنید اما برای کسایی که یه کوچولو فنی‌تر باشن مثل جمعی که اینجا هستیم خوبه.
دیفیکس در حد سایفون راحته، با این فرق که واقعا وصل میشه
😂</div>
<div class="tg-footer">👁️ 50.9K · <a href="https://t.me/MatinSenPaii/5208" target="_blank">📅 22:56 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5207">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">گویا گوگل Mantis رو اوپن‌سورس کرده
فریم‌ورک ایجنتی مانتیس این شکلیه که کل چرخه‌ی آسیب‌پذیری رو خودکار می‌کنه. از پیدا کردن و تأیید، تا بازتولید و فیکس. فرقش با اسکنرهای معمولی اینه که با ایجنت‌های منتقد و بازبین و... و اجرای سندباکسی، گزارش‌های الکی و باگ‌های توهمی رو فیلتر می‌کنه و مصرف توکن رو هم تا ۸۵٪ پایین میاره. پیشنهاد می‌کنم بک‌اندکارا و امنیت‌کارا یه نگاهی بهش داشته باشن:
https://cloud.google.com/blog/products/identity-security/getting-started-with-the-mantis-harness-to-find-and-fix-bugs
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 46.2K · <a href="https://t.me/MatinSenPaii/5207" target="_blank">📅 21:31 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5206">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">چند تا کوهنورد تو آمریکا با جمنای برنامه چیدن و جمینای بهشون گفته خیلی کمتر آب و غذا ببرن. و به خاطر این مشورت اشتباه با جمنای گیر افتادن و آخرش گروه نجات مجبور شده بره دنبالشون. عاقبت سپردن عقل سلیم دست AI
خلاصه برای جونتون هیچ‌وقت فقط به چت‌بات اعتماد نکنید
منبع
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 47.3K · <a href="https://t.me/MatinSenPaii/5206" target="_blank">📅 10:05 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5205">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/NZKzOyQpXv-K-fgQRybaeXTZoeoLPESV6jsHo4MyHTpteglScj0-5EizPhm7IGTO-pWLWBeYzVSQOSqQxmFjIs0ProgOZYmsUax1LIepLIHl39qazVpdFRdsbYW9Aa1hGLqQ9ABhHDBHT--Tcmbli_0C1upCtDK4l0te4XXu1hi_KIrFSCk_RdXg1miNDanaLIDLj7VGfpFc26EgTbFscIafft2xp6EY1rBZWEN08gNvXPuZn-vGl7BBJD6IhOJByRGPE53Iv4pdSn_tlNpUpDHHY49V4AuYAneo3TV2ENdMrUX5FPF08T3rofyf_NVZo-dcT1EfxTOeJPfcgWXxhQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تست
Pelican comparison
روی مدل‌های GPT به علاوه‌ی هزینه‌شون.
هزینه‌ی Astra تقریبا پنجاه برابر Lunaست</div>
<div class="tg-footer">👁️ 47.3K · <a href="https://t.me/MatinSenPaii/5205" target="_blank">📅 00:41 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5204">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/48fb2366c8.mp4?token=ikMMhJtAJkIM19gfrh09Hk4ahd330Qjyzi3HNJ0m2G6tsXQNsKD8GIZyLgCm8L90QkjbjWyvk6j1X0GhSX-O5HIe3otB4ZqeTvYlJqrzKyMjGsEzMIJdMdudcjktY8nQcV-AaShAJBB9xAmDblw7v0y8SJUMpkavfgSR2dlk2SA8Bh_6qbto1gHg_dzb1b9K-Jf7DevGUey3IzC3htOP2ajjJUiMO4s2cUk0e4LZ4C0roOAJswYkbIVDzMA0l6lNsp67c6dwVflNQm4p_CzXCxi6KxXmcCXhZcvasuXWSiMiG2H6DHjrVnY_zmEXiXEIetiqrUg3dcFebC5qrKsy4w" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/48fb2366c8.mp4?token=ikMMhJtAJkIM19gfrh09Hk4ahd330Qjyzi3HNJ0m2G6tsXQNsKD8GIZyLgCm8L90QkjbjWyvk6j1X0GhSX-O5HIe3otB4ZqeTvYlJqrzKyMjGsEzMIJdMdudcjktY8nQcV-AaShAJBB9xAmDblw7v0y8SJUMpkavfgSR2dlk2SA8Bh_6qbto1gHg_dzb1b9K-Jf7DevGUey3IzC3htOP2ajjJUiMO4s2cUk0e4LZ4C0roOAJswYkbIVDzMA0l6lNsp67c6dwVflNQm4p_CzXCxi6KxXmcCXhZcvasuXWSiMiG2H6DHjrVnY_zmEXiXEIetiqrUg3dcFebC5qrKsy4w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وزیر نیرو : خبر خوش برای ملت شریف ایران، قطعی های برق برنامه ریزی شده برق تموم شد.</div>
<div class="tg-footer">👁️ 42.9K · <a href="https://t.me/MatinSenPaii/5204" target="_blank">📅 21:09 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5203">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/SnN5TR6m8f4SkNBnB2THYnGiVzKfSpil07Pz9FJf_JEceY8I04qpCZ-hCCrA3r9o4L1X4VvgMdzdw6M2SFZQdpXx-VSXLWHULBSfdjHp9FjQmEQbBTeXr9Z8RFrAHYSdy2-IaEnBPBnk7B6eu9upnPklzCV6uF5_7MGehZteJH06tZb9ydNkxsuUpyd2Ba9aZWZZ11rcYPxN9RY929Etc2dq4ophQzL97dO6hwDUMYUn2PSR_uR7fvCzzQ1X7BSh7gWsdjz8-6T5PboLijp0gMFkEXJfm2h8wUndRxqI8ZpeaUddVu3-MQcyaJJlSz4eKCoNugY0tq1R_ia-_bBqcw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">از اونجایی که کلاد و جی‌پی‌تی مدل جدید دادن... به زودی باید شاهد دستاوردهای برادران چینی باشیم</div>
<div class="tg-footer">👁️ 44.4K · <a href="https://t.me/MatinSenPaii/5203" target="_blank">📅 20:49 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5202">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">آموزش خرید اشتراک Claude Pro با ویزاکارت شخصی و ایمیل خودتون  من امروز تجربه‌ام رو از خرید اشتراک کلاد پرو می‌خوام باهاتون در میون بذارم، که چطوری خیلی راحت و بدون نگرانی بتونید با پرداخت کریپتو روی ایمیل خودتون فعالش کنید. یکی از دوستانم دو ماهه و خودم هم…</div>
<div class="tg-footer">👁️ 42.3K · <a href="https://t.me/MatinSenPaii/5202" target="_blank">📅 19:28 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5201">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/WEB6IyHjk5oXbJgwYEFOxUb438wivIjSGVbFrLQ16PZDRzLjx0RV2qULVb59EnXSu5JiPSBCUHxCJ4YjyYjisxwMZjcxZK3T6bJlWu3XaJrTFySeMvk4PRZvysecccPdBFnXMfyVAmSKcmpOMYan1I8HLQfkDsTtfADqVgmdpervvxSpxiRgTasRcmspiYu89FyDm6fJW5p_nSvsYZwFwRQOZC8AMRj2AZb74DspyRXc4U3ukPM5LZOfcJ38yqE0kUutR6uKkEfd53CABgCVs3nqmuc6XKjcQPkQurIAY4XCizH5CWWLQtN2L-8R8lx2USzdL-68feDV6PxSmm2U3g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آموزش خرید اشتراک Claude Pro با ویزاکارت شخصی و ایمیل خودتون
من امروز تجربه‌ام رو از خرید اشتراک کلاد پرو می‌خوام باهاتون در میون بذارم، که چطوری خیلی راحت و بدون نگرانی بتونید با پرداخت کریپتو روی ایمیل خودتون فعالش کنید.
یکی از دوستانم دو ماهه و خودم هم از دیشب خریدم اشتراک Claude رو و مشکلی نداشتیم. صرفا باید ریز به ریز کارهایی که می‌گم رو انجام بدید
قیمت اشتراکش روی لایسنس مارکت الان 5.700 هست ولی این شکلی اگر بخرید با تتر 228 تومنی در میاد 4.800 که خب یه تومن به نفعمونه حدودا.
حتی اگر بعدا به مشکل خورد یک وقتی(که فعلا با این روش نخورده)، مبلغ رو برمی‌گردونن به حساب Mpay که ساختیم و مثل سایت‌های ایرانی نمیگن برو بیست روز دیگه بیا
آموزش:
1- اول از همه، شما باید یه ویزاکارت مجازی داشته باشید. آموزش متنی ساخت ویزاکارت:
https://t.me/MatinSenPaii/4915
آموزش ویدئوییش:
https://t.me/MatinSenPaii/5091
2- حتما باید حسابتون رو توی Google Pay اد کنید با این روش که دو دقیقه وقت می‌بره نهایتا:
https://t.me/MatinSenPaii/5092
3- توی گوگل پلی گوشی اندرویدتون، با همون ایمیلی که کارت رو روش ثبت کردید وارد بشید و بالا سمت راست روی پروفایلتون بزنید.
توی قسمت Payments & Subscriptions که وارد بشید، باید بتونید اطلاعات کارتتون رو ببینید.
4- اپ اندروید Claude رو از گوگل پلی دانلود کنید، وارد حسابتون بشید، توی تنظیمات روی Upgrade بزنید، پلن مورد نظرتون رو انتخاب کنید و خودش هدایتتون می‌کنه به پرداخت با گوگل پلی.
و به راحتی پلن واسه‌تون فعال می‌شه
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 44.6K · <a href="https://t.me/MatinSenPaii/5201" target="_blank">📅 19:22 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5200">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromPedi | پِدی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CQhd3UjYiGyyzW3PZsAXJGvGXUPzj-D71vk_Lt33wv9HpewC17v2nn1d5cCF6DT_q_MIh1XZOrl7l6JOKgqFAZHgBicNPrnC5lEKsRBOam5_Wu2dIk1rbFjTczRVrQMCxpKIUwmVSIqyVGA9-vVlKyI_AKMhFsp7yLaTYaCTeFbz0ulyJFcRgjeaBzqAMxmXIpEtJyJHFBzOmTFCITebIb0OllqicELBDvgqGbJPyuj8t6mlfJeYB2kQVY-Jssmo5al-we2dcslt9ji95muXRfmKG6LyAPHRYh2Tu3ws8lkNW71nAqvgZDqhbDWkqmr0tWzUk2yjsjx3dR6SthO3WQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📇
یکی از ابزارهایی که باید توی هر پروژه‌ای استفاده بشه، Codebase Memory هست.
https://deusdata.github.io/codebase-memory-mcp/
🟢
کاری که می‌کنه در ظاهر ساده‌ست: کل Codebase شما رو index می‌کنه و از ارتباط بین بخش‌های مختلف کد یک Knowledge Graph می‌سازه؛ از function و class و interface گرفته تا call chainها، dependencyها، routeها و حتی جریان داده بین functionها.
نتیجه اینه که Agent برای جواب دادن به سؤال‌هایی مثل:
«این function کجاها استفاده شده؟»
«اگه اینو تغییر بدم چه چیزهایی ممکنه بشکنه؟»
«این request از کجا وارد سیستم می‌شه و تا کجا می‌ره؟»
دیگه مجبور نیست هی grep بزنه، فایل باز کنه، دوباره سرچ کنه و نصف context window رو صرف پیدا کردن کدی کنه که اصلاً دنبالشه.
به‌جاش از طریق MCP مستقیماً روی گراف Codebase query می‌زنه.
✍️
تفاوتش هم فقط تئوری نیست.
توی مقاله‌ای که روی ۳۱ پروژه‌ی واقعی تستش کرده، Codebase Memory با حدود ۱۰ برابر توکن کمتر و ۲.۱ برابر tool call کمتر به 83٪ کیفیت پاسخ رسیده؛ در مقایسه با 92٪ برای Agentی که کدها رو به روش معمول file-by-file می‌خونه.
↗️
خود پروژه هم برای ۵ تا structural query مشخص benchmark گرفته: حدود ۳,۴۰۰ توکن با graph در مقابل ۴۱۲,۰۰۰ توکن با روش file-by-file. یعنی توی اون تست خاص چیزی حدود 120x مصرف توکن کمتر.
🔭
ایجنت از اول یک دید ساختاری نسبت به پروژه داره. می‌تونه call chain رو دنبال کنه، impact یک تغییر رو پیدا کنه، dead code رو تشخیص بده، architecture پروژه رو دربیاره و حتی ارتباط بین چند service رو دنبال کنه.
امکان Semantic Search هم داره؛ یعنی لازم نیست حتماً اسم دقیق function رو بدونید. مثلاً دنبال مفهوم send بگردید، می‌تونه چیزهایی مثل publish یا dispatch رو هم پیدا کنه.
ضمن اینکه همه‌ی indexing و queryها لوکال انجام می‌شن و کدتون برای ساخت این graph جایی آپلود نمی‌شه.
خلاصه اینکه به‌جای اینکه Agent هر بار پروژه رو از صفر «کشف» کنه، یک نقشه‌ی قابل سرچ از Codebase جلوش می‌ذارید.
مخصوصاً روی پروژه‌های بزرگ، تفاوتش خیلی محسوس‌تر می‌شه.
و بالاخره کمتر شاهد Agentی هستیم که برای پیدا کردن یک function شروع می‌کنه با grep و find و jq کل repository رو شخم زدن
🤢</div>
<div class="tg-footer">👁️ 37.4K · <a href="https://t.me/MatinSenPaii/5200" target="_blank">📅 18:52 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5199">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">تهران
💵
228,‌000</div>
<div class="tg-footer">👁️ 38.9K · <a href="https://t.me/MatinSenPaii/5199" target="_blank">📅 16:18 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5198">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">البته اگر می‌خواید برنامه‌نویس بشید توی ایران اول از همه بهتون تبریک میگم که با دلار ۲۲۵ هزار تومنی و بدبختی اینترنت و نامعلوم بودن آیندمون و جنگ و اقتصاد و فلاکت و بدبختی تصمیم گرفتید توی این حوزه قدم بذارید و شجاعت به خرج بدید</div>
<div class="tg-footer">👁️ 41.7K · <a href="https://t.me/MatinSenPaii/5198" target="_blank">📅 16:16 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5197">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">سلام، من پدی (پدرام) هستم!  همون‌طور که احتمالاً حدس زدید، برنامه‌نویسم و این اولین ویدیوی این کاناله.  اینجا قراره درباره‌ی دنیای نرم‌افزار، برنامه‌نویسی و ابزارهای مختلف، مخصوصاً هوش مصنوعی، حرف بزنیم؛ اما با یه تفاوت مهم:  قرار نیست با اومدن AI، هنر برنامه‌نویسی،…</div>
<div class="tg-footer">👁️ 42.3K · <a href="https://t.me/MatinSenPaii/5197" target="_blank">📅 15:58 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5196">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromPedi | پِدی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AOnFpavr96Q6ooxC6Rj9pYSzBGS3hp9IxDsWo5kJm9zv1ZorL8PJyGQ3XzKayQIrSQomSzh_TJrC24TlkWiRtM3QDjflCb0luZrsFQo87wWmQzxZAk4JkeSkEpbdsAnHmpPtZzr6EhxPjDETdXpAyTS-bbj2IzWH7zfApodOcIOWKplCxF1yOT7TSivrVKday7GPDQRiXoc2_k0WLeKXW4xzoD9KzSFcWLdXABqfbp_uPuuyaQjKB1gz5pRCkD4_QX5fam0XIYT68noOsw99TWHVel-sGzee86D6rY0YheWoy6QxCM3ljjHIEXLgjarOeC5Sa_ba_w5gk8fvsZ7LUQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سلام، من پدی (پدرام) هستم!
همون‌طور که احتمالاً حدس زدید، برنامه‌نویسم و این اولین ویدیوی این کاناله.
اینجا قراره درباره‌ی دنیای نرم‌افزار، برنامه‌نویسی و ابزارهای مختلف، مخصوصاً هوش مصنوعی، حرف بزنیم؛ اما با یه تفاوت مهم:
قرار نیست با اومدن AI، هنر برنامه‌نویسی، مهندسی نرم‌افزار و طراحی درست سیستم‌ها رو فراموش کنیم.
توی این ویدیوی کوتاه، خیلی کلی درباره‌ی دیدگاهم، دلیل ساختن این کانال و مسیری که قراره با هم جلو بریم صحبت می‌کنم.
📹
تماشا ویدیو از یوتیوب</div>
<div class="tg-footer">👁️ 37.4K · <a href="https://t.me/MatinSenPaii/5196" target="_blank">📅 15:54 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5194">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">این 25 دلار توی حسابتون می‌مونه دوستان. یه سریا فکر کردن 25 دلار از سر راه آوردیم بدیم دست هتزنر
شما اگر که استفاده‌ت میشه طبیعتا پولش رو میدی. مثلا من عموما قدیم از هتزنر برای استقرار ربات‌های تلگرامم استفاده می‌کردم
هزینه‌اش نسبت به سایت‌های دیگه خیلی اوکی تره طبیعتا نسبت به منابعی که میده.</div>
<div class="tg-footer">👁️ 37.9K · <a href="https://t.me/MatinSenPaii/5194" target="_blank">📅 03:05 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5193">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/FJbt7_Ibt4R0kn9w_AJpmt68s4bfSBqUpOmsNivpqM0wswdGCDbA_HcDK9MbI8ehd85MYND1_2srmeR9dt20e7iZAIAeZa5jZ-CIJViQsC2yLNXkad92CSfrv0RKt0LIwMElV2se4JiK3zF8oHK3QkZ4HZlzHnOenouBCtJQdRefPDEmyXnnZF1WMAQZy6YXqpdcm7CqYb8BnsC617QV7LPcfUOxllbdrCu5KwyPxELCafiZE25dkn_XXL_OPNbmTa2io0oWnB6TvqtheZHtDLB_4npM3UL8P_bqiAqMqko0fXnzBc5_BLzO3iBlupnuQaLwovuhv_4f37GCAEGGew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">لیمیتم رو پنج روز پیش تموم کردم. از کجا می‌فهمیدم می‌خوای مدل جدید بدی خب
🫪
(مدل Astra الان برای کاربرای پلاس بیست دلاری هم در دسترسه)</div>
<div class="tg-footer">👁️ 38.4K · <a href="https://t.me/MatinSenPaii/5193" target="_blank">📅 03:01 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5192">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/jCjvfnjQSE2ddbNTgroNP0Z9XY48MyddoD9lmbLQDQMr570g3io062322E7KiQqYX5JQI-5Wj2myiuBFEw91SfYG43Gc3tnPEjGp7zfBNhAp02NYZ-TH-cWIaQb5u6cXMFCp94e41gsurKHe87-XGM2iTfLCRBsRZ1qKgIT6HsbMJq0sG3xmeVpyw7frAPzVVoAvwtRG9cckXDZ92U722VlCOi4wmgyseqJu3KyYW7urmVHD7OqrZR73ZiI8h4aykv3Sklp5dPgmARB1VCGcy5aKB_akC87iX8p0FmZJhmG0V3ITsX2IcFnvMSn6miUJU8uOiTvvoFJzLGHEngV3iw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این سایت Nara خودش از اوپن کد api میگرفته
😂
😂
😂
😂
عاقبت وایب کد کردن سایت Api هوش مصنوعی</div>
<div class="tg-footer">👁️ 35.2K · <a href="https://t.me/MatinSenPaii/5192" target="_blank">📅 01:30 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5191">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/pInWW0h5CobpAS-AcA2kqI1PBoVqb-PtsJloAhcLf5AlEpjTN6DwWMuPHv04SwXufGmufyQ63f27HOpuEdg0_2DsBROO6h1Ao36nLhJ6F0E6ob8N0RwKj_77ZKm8wIM1XQAlnv4-pHZzeWbmK2hAKO1_izY1UfDfq3U_oVk7pY4oXTCWIvhgDXPHNHaykdZ6KVRonKK-cjA8YEVQu0cZxmKkEq8xcWCGstciyVlc7gI61x8mOaDl5SeeojvCqP6Vc0f91TR-OpqwqKYOtkPLwH7J9Hwn8wr-JUAQG9jZ7URqHsX_ccsxFMlMzZkSLUzRvDJmdJPgIFDF1g95ZRfmag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این سایت Nara خودش از اوپن کد api میگرفته
😂
😂
😂
😂
عاقبت وایب کد کردن سایت Api هوش مصنوعی</div>
<div class="tg-footer">👁️ 32.7K · <a href="https://t.me/MatinSenPaii/5191" target="_blank">📅 01:22 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5190">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">چقدر غمناک..</div>
<div class="tg-footer">👁️ 32.8K · <a href="https://t.me/MatinSenPaii/5190" target="_blank">📅 00:43 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5189">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">Kavinsky – Nightcall</div>
<div class="tg-footer">👁️ 34.3K · <a href="https://t.me/MatinSenPaii/5189" target="_blank">📅 23:34 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5188">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">Nightcall</div>
  <div class="tg-doc-extra">Kavinsky</div>
</div>
<a href="https://t.me/MatinSenPaii/5188" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">این موزیک برای من، خاطره‌انگیزه. من رو یاد برهه‌ای از زندگیم میندازه که برای مهاجرت به ژاپن هدف داشتم، مانگای yofukashi no uta رو می‌خوندم و شبایی که 5 سال پیش توی ناامیدی و شرایط سخت، برای یوتوبم تلاش می‌کردم
کاوینسکی خدا بیامرز، توی این موزیک یه شخصیت خیالی ساخته: راننده‌ای که سال ۱۹۸۶ با فراری تصادف می‌کنه، می‌میره و به شکل زامبی برمی‌گرده.
یه جاده‌ی خلوت و تاریک، فقط نور بنفش و صورتی چراغ‌های نئون که از پشت شیشه‌ی فراری تستاروسا رد می‌شن. رادیو یه آهنگ قدیمی پخش می‌کنه، دستاش رو فرمونه، فکرش جای دیگه‌ست — پیش دختری که عاشقشه و همون شب قراره ببینتش. بعد، یهو همه‌چی به‌هم می‌ریزه: صدای جیغ لاستیک، نور چراغ‌های مقابل، فلز که مچاله می‌شه، و بعد… سکوت. سکوتی سنگین که انگار قراره آخر ماجرا باشه.
اما نیست.
قلبش دیگه نمی‌زنه، ولی چشماش... باز می‌شن. بدنش سرده، دستاش بی‌حس‌ان، ولی یه چیزی هنوز توی وجودش زنده‌ست — همون حسی که قبل از تصادف داشت: باید بره پیشش. باید بهش بگه.
همون شب، با همون لباس، با همون بوی بنزین‌سوخته و شیشه‌ی شکسته که روی شونه‌هاش نشسته، راه می‌افته سمت خونه‌ای که صدبار توی  خیابونش قدم زده بود باهاش. جاده‌ها خالی‌ان، فقط صدای پاش روی آسفالت میاد و صدای دوردست یه Synthesiser که انگار از یه دنیای دیگه پخش می‌شه.
می‌رسه دم در. مکث می‌کنه. دستش رو بالا می‌بره تا در بزنه، اما یه لحظه مکث می‌کنه — چون می‌دونه از این به بعد دیگه هیچی مثل قبل نمی‌شه.
در باز می‌شه. اول یه لحظه شادی توی چشماش می‌بینه، شناخت، همون نگاهی که دلش براش تنگ شده بود. اما بعد، نگاهش عوض می‌شه. یه چیزی توی چهره‌ش، توی رنگ پوستش، توی سردی دستاش، بهش می‌گه من دیگه همون آدم قبلی نیستم.
می‌خواد براش توضیح بده. می‌خواد بگه که هنوز همونیه که بود، فقط… عوض شده. که باید حرف بزنن، که هنوز وقت هست. اما پشت سر دختر، از توی خونه، یه زندگی تازه دیده می‌شه — نوری که مال یه شب دیگه‌ست، عکس‌های جدید روی دیوار، ردی از یه زندگی که بدون اون ساخته شده.
سال‌ها گذشته؛ و اون خبر نداشته.
دختر نگاهش می‌کنه، با بغض، با ترحم، با یه چیزی شبیه احساسی که هنوز کامل نمرده ولی دیگه راهی براش نمونده. و آروم، بدون داد و فریاد، در رو می‌بنده.
اون می‌مونه توی تاریکی، زیر نور کم‌جون چراغ خیابون، با این حقیقت که تصادف فقط بدنش رو نگرفته — بلکه اون زندگی، اون عشق، اون آدمی که بود رو هم برای همیشه ازش گرفته. برمی‌گرده سمت فراری، سوار می‌شه، و توی جاده‌ای که هیچ‌وقت به مقصدی نمی‌رسه گم می‌شه؛ بین چراغ‌های نئون و صدای سینت‌ویو، بین یادِ ۱۹۸۶ و واقعیتِ الآن.
Take care of yourselves
❤️</div>
<div class="tg-footer">👁️ 34.9K · <a href="https://t.me/MatinSenPaii/5188" target="_blank">📅 23:13 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5185">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/njEc2SrUel4ygMD_-fkeHUvWaySJ9uBbIyoZQL80UzxBupWgv2R2vFL2veTqZWkzpqFRvkJoBEga6xHWTOAfe3v3pM09C0fnjjKS40xj3xBr9QczJ8Z3EuzD6v8SVnJct_TfR2S0WEJjdhTg-PM7kDYBvhQbMctH5bta7MEPf1hqM6YBAXW0436dYE042i-Xmjzc0BGzr16ocXRGAGrSSNN8NAT6L2gU4MQWGLCsP5Y7govjH7wHyqc0wkQzht6LX2jmWXXtJ1zLTsBboMnBYcV2-sulAABJfP_N0UyJuR9di43mmXVzmuo0143S-u4gQq-HdmeNTLbRtchwqV-jNA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/JjeCL_1LAmwZl5jM65ZAldWwtHkxKLrOnLM8DyUh-faM7WMgjN8n5BYkcrtt4t8WYvLh_9mZ9LJ8pjS64ahdghUO9GhXG4HH7HuwbSgaXgv2oRyNQqseJHAjMRfGvhoWSx57BeEdJTF-VNNCm9v5v-m3AdfkCMmBRgoADWg3udX5LjoQk5awP96Ll9QjilteXY24xPV27itBQubgebhfWBRr3AGEoHT-vX3Pzniz-cENaZVWUqDECHO4JWOlw7zZLrgWdZuFvfjBddB2n6cCrq9lzAW6xLl0IbwyWXdL0ku5qVs0VJc217bXfF9ad_S753PgC8YwJnjkTaBjH3uhTA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/kL3Fs56vTHeFrWbHIapuBPlYmyuHsCirFUeh-uxIxLrAiqmSzzbMtlgVFIkePGkX42Eja01JA6RpvtgqI_Zwezz_psQvjdWY3ZQpO62o18RnxaUm_6nkT0P2iBobmdD841VvJyposbpC0zf9yDAbCOYpsxMOTgnl1eoHqf_MZKjn673pGq6vnJ71lCLB7mMR7Tg54-FifaKvJI1YsI0_8L6GE5b88tdwzbXUbkxnagVNKFpr2qym97bjyoEDHgEL6qYCyEFOh0F-3alnZXD3coT_FHC3HW0BDyUJ9-Qf1CbBFS0Sopk6Z2XrEsnT45u73CMoMom82V6QXeYEDJDb2g.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">آموزش احراز هویت در دیتاسنتر هتزنر و خرید VPS ارزان‌قیمت
وبسایت هتزنر رو احتمالا اکثرا کسایی که توی کار فروش VPN هستن میشناسن، یه سایت هست که به خاطر سرورهای ارزون قیمت(2 هسته CPU و 4 گیگ رم، 6 دلار) و قدرتمندش معروفه. که توی لوکیشن‌های آمریکا، آلمان، سنگاپور و فنلاند سرور میفروشه. اما علاوه بر سرور، شما می‌تونید از Object Storage و خدمات دیگه‌اش هم استفاده کنید.
ببینید تا الان، مشکل احراز هویت وجود داشت برای ایرانی‌ها چون مدارک هویتی و... می‌خواست تا آخرین باری که یادمه، اما دیشب که رفتم ثبت نام کنم، دیدم یه راه احراز هویت دیگه هم آورده: احراز هویت با کارت بانکی و پرداخت 25 دلاری
پرداختش هم به این شکله که شما هرچقدر بخواید استفاده میکنید(مثلا 200 دلار) و نیازی نیست حسابتون رو شارژ کنید، و آخر ماه باید فاکتور 200 دلاری پرداخت کنید.
سرورها هم هزینه‌اش ساعتی محاسبه میشه و حدودا ساعتی 0.001 دلار پایه برای پلن 6 دلاری که خیلی به صرفه‌ست. و هروقت نخواستید میتونید Terminate کنید و سرور جدید بگیرید.
1- اول از همه، شما نیاز به یه ویزاکارت مجازی دارید که حداقل 25 دلار موجودی داشته باشه. آموزش متنی:
https://t.me/MatinSenPaii/4915
آموزش ویدئویی:
https://t.me/MatinSenPaii/5091
2- تشریف ببرید و توی
https://console.hetzner.com
ثبت نام کنید
3- اونجا از شما یه سری اطلاعات اگر خواست، اطلاعات فیک وارد کنید اما حتما با اسمی که روی کارت Mpay نوشتید ثبت نام کنید و خودم این کار رو با آدرس فیک آمریکا انجام دادم
4- به شما دو راه احراز هویت پیشنهاد میده. احراز با مدارک شناسایی، یا احراز با پرداخت. که شما احراز با پرداخت رو انتخاب می‌کنید و حداقل مبلغ(25 دلار) رو پرداخت می‌کنید و به راحتی حساب برای شما ساخته میشه.
دقت کنید که این متد همیشه ریسک خودش رو داره، اما دیشب که توی ردیت چرخیدم دیدم که 99 درصد مشکلی براشون پیش نیومده اما در هر حال، ریسک احتمالی اینکه ازتون مدارک هویتی بخواد بعدا رو توی ذهنتون داشته باشید. قوانین سایت‌ها هم ممکنه تغییر کنه اما فعلا مشکلی نداشتم سر این قضیه خودم
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 34.5K · <a href="https://t.me/MatinSenPaii/5185" target="_blank">📅 22:19 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5184">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/k4V_Oy-T231kVyEmwoA77vzOv9ViUqnZCUwdBVsN0Xd2fvL2efESu9PW6grz4nyGcvvr1SG9kc2E8W_it_0JohSoajAYD0GZ6aKmn9hhbvOi9DUVWFPxXenJTtVcIrFN-5sxJBSy_-2g62yrnz1v2gFhVN1enX8bhdBNla0KrcOSOzQYkWNALqPRax4qfW4RpeD9vP86tbcXyhrHPMp-OWKS4SgO2Dje9nsRaRSpPZv4vzvKnyjqbIGFoZtZddjJZ4vseQhsu1ejR2yg4xwvnleHDi9B8dUepzLCM-BkR4eHumdxkPq3juZ_SGnFmHuENguw5t1I0mTZqSDo5fzosQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قیمت و مشخصات؟</div>
<div class="tg-footer">👁️ 28.5K · <a href="https://t.me/MatinSenPaii/5184" target="_blank">📅 21:28 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5183">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">یه چیز بهتر از OVH پیدا کردم:) بذارید تست کنم ببینم اگه بن نکرد من رو، فردا معرفیش میکنم</div>
<div class="tg-footer">👁️ 30.4K · <a href="https://t.me/MatinSenPaii/5183" target="_blank">📅 20:58 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5179">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/c84957dbe3.mp4?token=SbrToKL5gVSQ7xVjSyNei6KhTO7J80Y7-iwmiZSdhoWstIGwjQlYKQWaFJNSuJz3FZ_TgoXF14-aiLdQ1Tvsak-VYuRu-ZtnyY7HtEjDua6_YFonRsR9c53xsJNFZ1D-oFyYg1Li5xXHoFZvOQkyMTuxWIotboYwpsbePyJJawkfReuGvTnhaN0XIbpeeI954FjbMmLEU71qb7P3cu_qwNuJqu1ew3-AXtZQVZT62AK5_0Aeu5fgcWZ-xp0cNdP-7VioTYQrkfS02WuiliuqKoNSqnuWqecSmAM1jGwSzmmB1nj3_5FhMWvP1FPzNzLdkHoDQPX0vJk65dS7PTuTkQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/c84957dbe3.mp4?token=SbrToKL5gVSQ7xVjSyNei6KhTO7J80Y7-iwmiZSdhoWstIGwjQlYKQWaFJNSuJz3FZ_TgoXF14-aiLdQ1Tvsak-VYuRu-ZtnyY7HtEjDua6_YFonRsR9c53xsJNFZ1D-oFyYg1Li5xXHoFZvOQkyMTuxWIotboYwpsbePyJJawkfReuGvTnhaN0XIbpeeI954FjbMmLEU71qb7P3cu_qwNuJqu1ew3-AXtZQVZT62AK5_0Aeu5fgcWZ-xp0cNdP-7VioTYQrkfS02WuiliuqKoNSqnuWqecSmAM1jGwSzmmB1nj3_5FhMWvP1FPzNzLdkHoDQPX0vJk65dS7PTuTkQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مدل
GPT
-6 Astra بالاخره اومد
💻
بعد از چند هفته شایعه‌های مختلف، OpenAI دیشب مدل جدیدش رو با اسم Astra رونمایی کرد. گرگ براکمن رسماً گفته «فکر می‌کنم رسیدیم به AGI» که خب فکر کنم بیشتر منظورش AGI ِتنظیم بازار بوده
😂
1- چی فرق کرده؟ برخلاف نسل‌های قبل که بیشتر یه چت‌بات باهوش بودن، تمرکز اصلی Astra روی کار کردن مستقیم با کامپیوترته: پر کردن فرم، کار با اکسل، رزرو نوبت، جست‌وجوی شغل، حتی دموی ساخت یه صحنه توی Blender و بردنش به Unreal Engine. توی بنچمارک OSWorld 2.0 حدود ۷۲.۶٪ گرفته (Sol حدود ۶۵.۷٪ بود) و کارها رو تقریباً با نصف زمان قبل انجام می‌ده(حالا اینکه هزینه‌اش 2-3 برابر شده رو کاری نداریم مثلا)
😑
2- کجاها واقعاً می‌درخشه؟ توی کدنویسی و کارهای عاملی طولانی، ریاضی و علم (توی FrontierMath Tier 4 حدود ۹۸٪!) و امنیت سایبری که توی ExploitBench صد از صد شده. برای همین OpenAI قابلیت‌های تهاجمیش مثل ساخت اکسپلویت رو برای کاربر عادی قفل کرده و فقط توی برنامه‌ی Daybreak بازه(فکر کنم همین بود که رفته بود Hugging face رو هک کرده بود)
3- داستان اون ۹۹.۹٪ چیه؟ OpenAI گفته Astra توی ARC-AGI-3 نمره‌ی ۹۹.۹٪ گرفته که واقعاً وحشتناکه. ولی وقتی خود سازمان ARC Prize با harness استاندارد خودش و API خام تستش کرد، نمره افتاد روی ۶۲.۷٪. اون ۹۹.۹٪ فقط با یه harness اختصاصی خود OpenAI به دست اومده که حافظه‌ی استدلال مدل رو بین مرحله‌ها نگه می‌داره، و هزینه‌ی تستش هم حدود ۱۹ هزار دلار(4 میلیارد تومن) بوده. پس این عدد رو نمیشه مستقیم با بقیه‌ی مدل‌ها مقایسه کرد.
4- توی مقایسه با Claude چطوره؟ این‌جا قضیه واقعی‌تر می‌شه. توی بنچمارک‌های خود OpenAI (کار با کامپیوتر، ریاضی سخت و...) Astra جلوتره. ولی توی Artificial Analysis Intelligence Index که میانگین چندتا بنچمارک مستقله، Astra نمره‌ی ۶۱ گرفته؛ دقیقاً هم‌سطح Sol
😂
😂
، و پشت Claude Fable 5.1 که ۶۶ گرفته. توی Coding Agent Index هم ۶۷ در برابر ۷۰ برای Fable 5.1. یعنی توی خیلی از تسک‌های واقعی استدلال و کدنویسی، فعلاً کلاد جلوتره؛ عوضش Astra توکن کمتری مصرف می‌کنه و برای خیلی کارها ارزون‌تر تموم می‌شه. (حالا اینکه Input Cache اش چهار برابر Fable هزینش هست رو کاری نداریم)
5- قیمت و مشخصات؟ هر میلیون توکن ورودی ۱۰ دلار، خروجی ۵۰ دلار، کش ورودی هم 1 دلار و کش Writing هم 12.5 دلار؛ تقریباً هم‌قیمت Fable 5.1(به جز Cache که فیبل 0.25 دلاره) ولی ۲.۵ برابر گرون‌تر از Sol. پنجره‌ی زمینه حدود ۱.۰۵ میلیون توکن، خروجی حداکثر ۱۲۸ هزار، دانشش تا ۳۰ آوریل ۲۰۲۶ آپدیته. توی ChatGPT هم گفته می‌شه سهمیه‌ی پیام Astra روی پلن‌های پولی کمتر از Sol هست طبیعتا(بله AGI تنظیم بازار)
6- دسترسی؟ فعلاً فقط سازمان‌های محدود (برنامه‌ی Daybreak) بهش دسترسی دارن(مثلا ادای Mythos رو در میارن). توی روزهای آینده میاد روی ChatGPT Plus و Pro و Business و Enterprise، از طریق API با شناسه‌ی gpt-6-astra، و روی Azure و Bedrock هم در دسترس قرار میگیره که برای ما ایرانیا زیاد اهمیتی نداره. ما اونقدری پول نداریم که پول api بدیم خوشبختانه
حرف آخر: روی هوش عمومی و استدلال سخت هنوز از Fable 5.1 عقبه. گویا توی طراحی Front و سه بعدی خیلی بهتر عمل کرده اما خب، متأسفانه اون هم نمیشه اعتماد کرد. سر Kimi3 و Fable 5 هم همچین مقایسه‌هایی میکردن تهش گندش از آب در اومد که اینا پول گرفته بودن الکی قدرت Kimi رو خوب نشون بدن و خلاصه تا خودتون تست نکردید، یا عمومی نشده 7 سپتامبر، اعتماد نکنید.
منم هیتر GPT نیستم؛ صرفا واقع‌بینانه مقایسه میکنم. وگرنه همین الان اشتراک GPT رو دارم خودم و میدونم اگر روی هارنس درستی باشه، توانا هست اما خب، چه فایده وقتی Ox Alpha انقدر قوی‌تر بود ازش:) متأسفانه
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 33.9K · <a href="https://t.me/MatinSenPaii/5179" target="_blank">📅 20:43 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5178">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromMatin's Dungeon(᯽マティ️️ン先輩)</strong></div>
<div class="tg-text">بچه‌ها من یه ده روز نیستم کلا و مسافرتم
بعدش قول میدم حتما استریم راجب دانشگاه و انتخاب رشته داشته باشیم و ادامه‌ی استریم‌های Rust
تا اون موقع مخصوصا بچه‌های کنکوری سعی کنید تحقیق کنید کامل. از بچه‌هایی که مسیری که شما می‌خواید برید رو قبلا رفتن، سؤال بپرسید.
دانشگاه دولتی رو بررسی کنید
دانشگاه آزاد
حتی پیام نور
ببینید هدفتون چیه؟
شاید دانشگاه نرفتن هم یه گزینه باشه
این وسط برای پسرا سربازی هست
و خیلی مسائل دیگه مثل خود کار پیدا کردن و ...</div>
<div class="tg-footer">👁️ 34K · <a href="https://t.me/MatinSenPaii/5178" target="_blank">📅 16:09 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5176">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/duiIuX0C28COqQLY9Fm1d0N88tMpx8jizgTk2TUjNujwg5ePcUerLoXLCnrBXqNPI5GhsRD6LrYWYkN4T64oVuNYAkXojxbIoFfa-EjDHVWgzjE6i3fbw4ld5_QAAy9hXVX5UMr9bu9PebEXUP1gSS3H96-p2JDstaFy6rHaEZziKqNfMMethEOAINJI_Nzn9GYDmlQqFfz8Eooi2iQWZ5Pby_de_JzF7tG_EwNWExFB8bLXIztyiXUx1UQKtaoQdJ5S7c8li9mTZQsxj_7fr9gSA1FL9i8iBY9XKodVt82iAkQKxerKUKifiF5G0cDffDXgb9G7dN880GhfSdCK8w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تلگرام شما هم شده پر این تبلیغات کریپتویی و ترید یهو؟
حس میکنم سیستم نمایش تبلیغات تلگرام عوض شده چون 24/7 هر کانالی باز میکنم تبلیغ روشه. قبلا این شکلی نبود
الان حتی روی این کانال کوچولوی من
@MatinsDungeon
هم داره نشون میده</div>
<div class="tg-footer">👁️ 33.9K · <a href="https://t.me/MatinSenPaii/5176" target="_blank">📅 14:04 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5175">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">دوستم دیشب بهم پیام داد و گفت متین، gpt 6 اومده
گفتم بذار بخوابیم فردا بنچمارکاش در بیاد
و الان باید بگم Wow!!</div>
<div class="tg-footer">👁️ 34.9K · <a href="https://t.me/MatinSenPaii/5175" target="_blank">📅 12:45 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5174">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">متاسفانه نشد
😫
فعلا بریم کردیت رایگان گوگل و آمازون رو استفاده کنیم ببینم چه میشه هرچند هنوز می‌تونید از سایت‌هایی مثل Aeza و Yottasrc و... خرید کنیدا صرفا OVH رو دوست داشتم بگیرم که نشد باز، اگر موفق شدم بهتون خبر میدم</div>
<div class="tg-footer">👁️ 37.2K · <a href="https://t.me/MatinSenPaii/5174" target="_blank">📅 01:44 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5173">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/J4ODl03tJ0OfMy3uDqPiguXrCuLj7_I8JcFsRo553-8EYYKCxbDAyC43Ly7vCUytv1ru6eDEna_Nj1Mz4dMTJTLTo6HvxB8M0_62_ZRh4BG6asa9loUQR5XdgLuUvI3muQqpHbEdGc943L5tQ-eUyWzUos34-qznim9W-FZI_CjdjVrNTikZN8OtA6xZmHlEhawQptynKe-fb3n_mQw8k1L6vKqNx0v8CBg_E3UfPl6Rm5dAY1crwYMG2F0JWMg4jmz-1lTIkqQC20jqUg0c79G2uf4flq8ovJgpiLcs9aEQWr3MaL634tAi31LXnC24RjE7sP9MSAoi3hodYWeQSw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سرورهای OVH واقعا به صرفه‌ان از لحاظ قیمتی و اینکه ترافیکش نامحدوده. 2 هسته CPU و 4 گیگ رم، 4.5 دلار. با دلار 220 تومنی میشه 990 هزار تومن اونوقت سایت‌های هم‌ وطنم پاره تنم دارن سرور 1 هسته و 1 گیگ رم میدن +1 میلیون تومن://  سایتش گویا یه مقداری روی آیپی حساسه…</div>
<div class="tg-footer">👁️ 37.5K · <a href="https://t.me/MatinSenPaii/5173" target="_blank">📅 00:02 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5172">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/GVOp716oe1AtYmWS_u2VbjWLgcK_T7XvsCt4G3GNhkQzjk0WEEYwzP1cxIcVMdoqEA1HuWtFQ3hkl_X8IcSqZSRgs4o9zIY3KYv5RopvMXMFY4gunVKlbaSYJzFMFDGzw5hAL8SrZWxsKbUmhqxB9jhk2S073gjmwz1wkld0mnp5mkmODimhMsb8To3RMGi-fxfJYl0hmrTS6qMLIYoTDPN3kSfxEfRdUH2feCEbqiiYgA05pLbbxqummn6hRmqg75NujreNmMml9NLShG6dIn3e9RTubmmhfTaN0E6Rp1HNNHglEcSxAKB4cMZP990PaIFER6OawdqREnZ6nDfSdQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سرورهای OVH واقعا به صرفه‌ان از لحاظ قیمتی و اینکه ترافیکش نامحدوده. 2 هسته CPU و 4 گیگ رم، 4.5 دلار. با دلار 220 تومنی میشه 990 هزار تومن اونوقت سایت‌های هم‌ وطنم پاره تنم دارن سرور 1 هسته و 1 گیگ رم میدن +1 میلیون تومن://  سایتش گویا یه مقداری روی آیپی حساسه…</div>
<div class="tg-footer">👁️ 34.3K · <a href="https://t.me/MatinSenPaii/5172" target="_blank">📅 23:48 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5171">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/LlutbcfkLxz0neWKebakLSNMY-etU9gmtP7GoxdzOcTp_cfV3_RXRY-w0Nwx3DGBByk-yzigVWQd0otFC777EIodUhnsIKx7633DwDN5u6QgN0bW6vauBg6XKVTClweass2TxCrfZFx1fcFQW3MdNTZY-2xAqAWsxJAcUF-yNhZq-d_T1FF1o76o3HyCDseGXa7J7L0rrsqR_qFVnrKekJE08qnaSLk3gLLJ_F9_iH2dTe4aHp_ZKIn59_Ydwh3e5Z7fiUpUU49YPJ5NkHKcspD6nYcqEZJZj4uvK0YmWYBmPZiRcPBPNT7BQRatgl8vYSnzbmfupn9YTb3rlOfSeg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سرورهای OVH واقعا به صرفه‌ان از لحاظ قیمتی و اینکه ترافیکش نامحدوده.
2 هسته CPU و 4 گیگ رم، 4.5 دلار. با دلار 220 تومنی میشه 990 هزار تومن
اونوقت سایت‌های هم‌ وطنم پاره تنم دارن سرور 1 هسته و 1 گیگ رم میدن +1 میلیون تومن://
سایتش گویا یه مقداری روی آیپی حساسه
من میرم تلاش کنم ببینم میتونم ازش خرید کنم با Mpay یا نه</div>
<div class="tg-footer">👁️ 34K · <a href="https://t.me/MatinSenPaii/5171" target="_blank">📅 23:45 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5170">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/dgrFKkZaINMtPj26aCi-Ix0JvonFRwr5L2j17TCFClVib2PRI3uSzFgFCdapcslQXveHdbMVHsxcsjox9tBHdL4aiigg-sKqOCYO6ZjfkLamQEr1NvAbPaV_MCuX3YBP875acGw7InMvBgDWBtIZiGM-xEgF3r_6IWWAsBzaorCjaQNJ1cY4EqwNqUBk2PCtN1J-G0QXuy1fO1z-uOD4kzVNpeuwa4Yk5geqr8GBB3OecNh4UOoJc4OJwUD5W6TJTHAiW7aOKfoRTy5u54Mm9zLdTUBVDzFaxYCqx1rnQu0t42kNXCp6oeTlXenB69bJSTzzRmawW3TFCMHe08s2Jg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دارم با همین Nara و مدل Muse Spark 1.3 یه سری تسک سرچ متوسط انجام میدم(سه تا ساب‌ایجنت ران کرده که قیمت اجاره و... رو توی سه تا شهر مختلف برام در بیاره و اونایی که ارزش بیشتری دارن رو از دیوار و شیپور و اینها لیست کنه) با هرمس، چیزی که چشممو گرفته سرعتشه که…</div>
<div class="tg-footer">👁️ 32K · <a href="https://t.me/MatinSenPaii/5170" target="_blank">📅 23:07 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5169">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/hk-Ew-899P_JCnXOdHq1yW0kojtDyBGIfAIk8dw9BMX6hEr0kuKK4maQuIRTkrtL-1SzT6Dp_pFhWGmfWjVJ6hqRCIkxJlkulBtiIAzUZsWtsgOhzVSmmLfJRwBA2Et-cFdYOg5cQlpSw5vnjB-j-mo7tRNIuf_juCFo2QOssq22SeMmlvmB0zKLQOAJSWFAkCgT9n8XhMMy9WGo7cDZO0Z9cly8srkGNF6-mtBoAn2FAJR_zjq6pV9RubI2sGN8lK_yII7O3iHHqb8GD9NDOENxrX9dwXHEv1n6GC7LJtEPxsCFBui08Na1M4tcELAg-oEA3P09tmd-A7meRYi_FQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جمنای هم تخفیف زده روی پلن‌هاش
می‌تونید خریداری کنید ولی حتما از اندروید + این متد که اینجا توضیح دادم:
https://t.me/MatinSenPaii/5092
استفاده کنید سر Google Pay</div>
<div class="tg-footer">👁️ 31.1K · <a href="https://t.me/MatinSenPaii/5169" target="_blank">📅 22:41 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5168">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/iebvdcQ6iOo-dA6wALceA405zADmcR56rfwUA0E-TVBLR9meHBR0ion0f74VqGDmYjWzShjCfLaXog8TwAusDTqz6yypUnMpzaX0VrVG7cOPQdLYrALUM0AKsFSQ-T8mVxn03dHXyctpfP4qXpk-cJPQE1dxsg3LNC1L02abH4LPsB76-OVU0RVj0BlTThMaioZwK5y8fezoH8vpv4TwfTd_iBxpPGKFsBqGX_evQjjH0Oi3v-O4pY3lW73JzeKxQTIxuatrsq_bTBcct7aqYqS4mMKmqY1lhYF4Vx-r6qNnyaX3N-pTJGDZSc0KSIl3T-ODGvt1VsBfWbvEp4icSQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دوستان با این سایت Nara که قبلا معرفی کرده بودم(https://t.me/MatinSenPaii/4061)، اگر که داخلش اکانت تلگرامتون رو وصل کنید به رباتش و توی کانالشون جوین بشید، می‌تونید نامحدود از مدل muse-spark-1.2-contributor-free متا استفاده کنید؛ بدون محدودیت ریجن و...  مینویسه…</div>
<div class="tg-footer">👁️ 29.2K · <a href="https://t.me/MatinSenPaii/5168" target="_blank">📅 22:01 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5164">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/GEC4dUWUxhrI6-GxjvUKenI22l-TQMbwbBBTIDCS0RAB2muiNC62H5XF9CX0UbMmoR_BaHRjYJd1RfW6d3_yKYEIxQAQ7z7v8CarVTj-uBrL3DfQ9ruPZOosExgW9y2UXd8XIGD0g3tTTAQCkfPAAYGic3FtwRVIbKrIVLPRg4d4oqH4Wjg2pgCxMa2NToQGa93UbCZ1hiu3tFidjclxO2U7s17bIu2NPAPsaJ8acNacIJ9g4rStB08UigiGrmM1-ymppYucWFl-1uMvjTH5GVF8D0qBtednaXHG9z6DlIHMx16RQL2admd92VAXc-kIEDdGoXnNZFg-wBTsj1WzSA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/t-q9G3xP3FVvtzqSSQYz-RThi5tWNxQ-u49BMds2Zi6pzZzKbU-fBb5NT7Q8wMk3tJiEFqTc4QBJTyr1CqKIr8DnPft8HC4kMnMs2riS5IoXK_RTGFTdq4_JKrWdQAlOA_9j2d-ykvSu3iXte9kxfZYoOqtZSqS440LufBhXAcILevSP0r8Em2NksqsQ5dI_nmw9Zmp8F5NX6R7pwjYI7iNpCQsFLbgFz3qqUQo88ri-uzAdgyCEBHIES-lQn-fq5qtO_8wuohHpHmFjHOvcRCl8N4Rl9vNtjJKcnRM-29gnFaIHp2LzKTbrQ9aBizT_fTaMLfhxRaPVnpVA8diqBQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/bYgqejprCGH95wmLKK7t6w-d_6R8FZeNYyYaxalDzflVVfRuSJ-GveTCaOwW_wTleNlfP0GVkF76qvf2VeoOCb8EcyDyisaJ_ucjLIzAXCdq-JGMtwl8kyTogOW7eRNovxUuQ4vPperEw-McybYvsNiJgiqQ4m-MSJi72hBbIhEMyY7CfL5xHKW_T9UQzNGmD8K4ItFpOzc75TkPz9n95cyil0PY5vi0Wd9pDgBOlSja8Jker5AB6JXleljduFSl8lLlDsD4EShFdL1gnHf3G6ZiAbSGvw6ds5O2Lfrpo2dEbXZCWdk2oSfTGBDGolGKprWzn6NGA1OwhmT05uZ5sQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/pYcm9fNWC1_XWUgWPwu_VfOzquOh_j1tm7HR9PyI_wb5nzgSg_BQ0KTTW_ijc1t1QmGZHFmtQuy6-r7oECintGPiz27YVwe0_hH9wTAxWXgvzuFU9veJV3GZHmgrYqxTE_d3UNAYSPiamqW0lpkS0M3h0PQmfE-A9BtFgYzFCN23btln0U2mmnG7L36xKP3jOxNCxr_u40i7j7ritwrPNSk8v2qF896wH3PmPtBYwF_GYKIyjG1lNkR-BHw5Dm3wHPz18zL-tR5kTLBHBOkAUi8MXiRydVOWM_LfmuHqYKW4wX3BDkdWzoV5MOA400sdrCKQgfcwUpctSKZKIAAqCQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">از سایت Nara Router که ریک معرفی کرد دارم استفاده می‌کنم برای ‌Hermes و چیز خیلی خوبیه! یه ربات خیلی کوچولو هم دارم می‌نویسم. دارم تمرکز می‌کنم روی این قضیه ببینم چطوری می‌تونم کارهای روزمره رو Automate کنم و چطوری میشه حداکثر بهره‌وری رو داشت از Hermes  خوبی…</div>
<div class="tg-footer">👁️ 32.2K · <a href="https://t.me/MatinSenPaii/5164" target="_blank">📅 21:43 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5163">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">نمیدونم چرا انقدر از مدل Kimi 3 خوشم میاد
زیاد هم فرصت نشده استفاده کنم توی تسک‌های سنگین
اما در نهایت برای کدنویسی، compatibility ای که مدلهای کلاد با خود هارنس claude code دارن رو هنوز توی هیچ ابزار دیگه‌ای تجربه نکردم</div>
<div class="tg-footer">👁️ 31.2K · <a href="https://t.me/MatinSenPaii/5163" target="_blank">📅 19:22 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5162">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/tGH9vaD2gpoNf1LkhOXdTGbVsHU_Oj0sYCPcrP000muWhJXP-tMQRzfLPQG5viujJQMCLpWqVlaNlK1SvQ7m-4EkuKjd-g-aGrZkMvCu3Ewu54ofRa_gfYKSLY8C7rPUlgMe7Iv8hX9n33KZfl7Nsg5dfdHknMmbk1Iv6fpmITsn1NLtMaLsdyYpzFdLiqo0fN366CPjTK4ypqKcbx9mniMdtEhKeyr9yilUzyaAS2QJ1uHWesYxwv8DW4Te3BsSh-XWvHIgcouNtURyj5LDOipQkEuZFD5hpW4sZ7cwauQ-ZhwfukzllxmKypWuohgjBDMSDhOnKBPmZo0MECfAXg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مدل Muse Spark 1.3 توی OpenCode رایگان شده اینم آموزش استفاده‌اش</div>
<div class="tg-footer">👁️ 32.6K · <a href="https://t.me/MatinSenPaii/5162" target="_blank">📅 19:21 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5161">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/hnq3uaTMhClNCi6j2M7CVWuSQPAmbfJX80v_bPvYBdg94Zy4Nkgxj1mDhZYQOD2_K2DPSKYpEzB6IHv34IOPcCVpBAZsadLB9-nBrR_SwqI8hEf661sHqnjswPqXpVEKHlG2T7Qh3dnYuBB8A57DxauSn_xktarOFoMQNlSD4AA81nGm5xs21M7uR7Bd7DhA2Ns-OyGnWrhiotf17IYuAlTSP6oUjyiW5AsyolIONuivOkg_hHPLPddzd6x-L6LN4msu7K7hzvUmiPOkpilLC6DLwFL7l2jIJttg2xBULURs1nRh_hV_tTY-RXSc4cgFGAoJ1dThToPsL_jVm0Wqow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این هم بنچمارک Fable 5.1
البته با هزینه‌ی سرسام‌آور
10/50/0.25
In/Out/Cache
که خب با Fable 5 یکسانه، اما با پرامپت یکسان توکن بیشترس میخوره(و هزینه‌ی بیشتر طبیعتا)</div>
<div class="tg-footer">👁️ 31.2K · <a href="https://t.me/MatinSenPaii/5161" target="_blank">📅 17:32 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5160">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/YDUuDPdWpmdURNAVhVrY9a_aZnjuEaK7ypl1Ak22VlZMPz6nnTxFWMVcaJfx_ccz7PjPP3KAZRQZEiwh-yrq1R5s435EZ5S2hp-tFtg5YsmtdY1oy1j2jRiKr7JE8lR7gCHml8wwY9BvUi0tSErU3DAP7kMPq96w0z_-vXQKOXBBj6r5b3Fdjj4-RQD8kuvoOSuADvfiKpYcif0vdipl7zl-FJL4Y7_2JnxJM1_Qpvksk3aaZRClDVEp-fnvzg-_O3eq7db24SA9wuWKuTddi4mFLSDtdDMQZIBpUcBMdq2Cs8A30xUILxlX0GrUOzKjHO-CSxsib9qIbIhIm3VyJg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آقا مگه میشه مگه داریم اصلا  حس میکنم خیلی اغراق و بزرگنمایی داره. امکان نداره قدرتش از Opus 5 انقدر بالاتر باشه توی این بنچمارک‌ها:) باید تست کنیم</div>
<div class="tg-footer">👁️ 31.9K · <a href="https://t.me/MatinSenPaii/5160" target="_blank">📅 16:30 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5159">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">کار کردن با مدل Fable 5.1 به قدری گرونه که می‌ترسم بهش سلام کنم لیمیت هفتگیم تموم بشه</div>
<div class="tg-footer">👁️ 31.7K · <a href="https://t.me/MatinSenPaii/5159" target="_blank">📅 15:21 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5158">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">امروز هم Muse spark 1.3 رو داشتیم هم Gemini flash 3.8  فکر کنم گوگل از جمنای pro 3.5 کلا بپره بره روی 4 مستقیم با این وضعیت</div>
<div class="tg-footer">👁️ 34.7K · <a href="https://t.me/MatinSenPaii/5158" target="_blank">📅 12:51 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5155">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/D7yf_DKbtPOmOIsF5f8k8E6V3X2OfVHWCeXRjst68pn1C--uCe7uE1VJBH1WfU2--S7Wi5ktXQN0Vk5nJbm0fWF5np9Z2GOGhIBR2ss9gPE-UCRfTH9xCUXxGFNhxCDaMezOp2Kb3JOfRo_AvLcNZyrYlaRMetWQPSE8rS0fOM7pPOo0iU6TgQ3mmhPXp3RNQ5Xl5NPx6TBKKIU-cQuEVQhgIC3DuNZwfFcwaQL1rHA_FVLoOAMxKbfR0LcPsT_a-tUHtyiSQEEYz8U8UqjaxP7ABQ8MzCt8kzitl-1_etPR2idTRgMtiRvtckix8puO7SAFKlli75SPG-VNLdicvA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/DuaT1Qm7upL1g2xAKIDq-UObR4AfOzvYsVXCMXj-htWpawa2NW9-5h6eMMLVbi4OQEpIdTRcmjrCHnHYfy0eyAcJ8Ey7vnoW2p5Y_aMqNQAvVyegObDrz83DVRi4Zr_m1WXgzHNtSSnfNc0JPxsPtZLJK9SlD1E8oDJDg0Fx_NFzcGFkPER4T4GaROTvYWUoY9MV4tuKdVxN07b43qy_vvWq4BnzcH9O6bkQ7s7OxzYlY1se0gTyIeRTeAq7kWte4c1pw0buw3RxAQ4mFfww7BtQB3SGvC1s4kNo8dea_5fIJ8LVA3jD87Xe1wRvpNFnDlocjLwBZ3hL3030f4ZjMw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/TdKP-VQCDslxdKtTHWxc-mfUL5OkP-_xVdcPJj334Y7jH-Y8_UWWePxeZMC5I3486SjwKluPYw8ehSH3uYdFRFaUlTR2-MTzcUt-tt_nom-Y68Vk0pl3SChiGfcIQQBbgJ5WqKNRjbPvb8vG_rntt9kZ0ttW_d8wB2pHHM9FXLI6t_iwZFrCTHXhblcL_eRt-_Ri7uxPnVR1YX0lSCU4hUfLD6LoMfcPgyCgCc0bjHLjEsATF3Yq1ofhl9CI8tQ3d7aG1NyUuBEB5vz3jQNRTT68a-hr6wMbtWi9E1uHCl6lqDwp4zlDf0Ae2SoI2yBDOgItqmuhbv0Rd0-lPW0ZJQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">امروز هم Muse spark 1.3 رو داشتیم هم Gemini flash 3.8  فکر کنم گوگل از جمنای pro 3.5 کلا بپره بره روی 4 مستقیم با این وضعیت</div>
<div class="tg-footer">👁️ 38K · <a href="https://t.me/MatinSenPaii/5155" target="_blank">📅 06:22 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5154">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">امروز هم Muse spark 1.3 رو داشتیم
هم Gemini flash 3.8
فکر کنم گوگل از جمنای pro 3.5 کلا بپره بره روی 4 مستقیم با این وضعیت</div>
<div class="tg-footer">👁️ 33.4K · <a href="https://t.me/MatinSenPaii/5154" target="_blank">📅 01:35 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5153">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-text">🔭
اگر نمی‌دونید Connection Chain چیه و چطور باید در WhiteVPN ازش استفاده کنید، توی این ویدیوی کوتاه قدم‌به‌قدم با هم یک زنجیره اتصال می‌سازیم.
📱
دانلود آخرین نسخه از گیتهاب</div>
<div class="tg-footer">👁️ 32.1K · <a href="https://t.me/MatinSenPaii/5153" target="_blank">📅 22:02 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5152">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">سعی می‌کنم آفر و... خوبی اگر باز دیدم که بتونید با این ویزاکارته بگیرید، بذارم واستون</div>
<div class="tg-footer">👁️ 35.3K · <a href="https://t.me/MatinSenPaii/5152" target="_blank">📅 17:37 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5151">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">آموزش گرفتن 300 دلار کردیت رایگان Google Cloud  این سرویس Free Tier دائمی داره. یعنی حتی بعد از تموم شدن کردیت، یه سری سرویس‌ها همیشه رایگان می‌مونن (مثلاً هر ماه یه سرور مجازی کوچیک e2-micro به‌صورت دائمی و رایگان)  و همینطور با این کردیت می‌تونید دسترسی…</div>
<div class="tg-footer">👁️ 35.8K · <a href="https://t.me/MatinSenPaii/5151" target="_blank">📅 17:31 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5150">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">💸
دلار فردایی تهران
💵
220,300 خـرید
💸</div>
<div class="tg-footer">👁️ 37.7K · <a href="https://t.me/MatinSenPaii/5150" target="_blank">📅 14:06 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5149">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/kPw_u9Fzzms_rn_WIjH9QT_EQIE8LCLkqKOZfeqbQlM3VQd9N2RHBCYDNVKnyxUiOvwau4v3I3aABK6G9x3qeLuCdPNCfauRx6y6Syyuqo7I0m3s0DHAk-ccTUCSW372ASrT31MuWGtKg7g1XoEyYPaTh12q2moSvLf5od2TmlgcPAU5w41bj-vth1t7VQy6y9QpPFc_joTNHFnYOa91Z5FCexQmC9jM53y5ojuFbbp0roCwTWfiVZzkpb8OYnaxK6noyuZRJ2zQP65haMyjXmEbh0FVzzXWR23PnCkHF_7s_qsDrXsJJ1EBB0s2bSgsWI5eVUqH6z-kFu0aQGy36A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آموزش گرفتن 300 دلار کردیت رایگان Google Cloud
این سرویس
Free Tier دائمی
داره. یعنی حتی بعد از تموم شدن کردیت، یه سری سرویس‌ها همیشه رایگان می‌مونن (مثلاً هر ماه یه سرور مجازی کوچیک e2-micro به‌صورت دائمی و رایگان)
و همینطور با این کردیت می‌تونید دسترسی به
بیشتر از ۲۰ محصول
محبوب مثل Compute Engine، BigQuery، Cloud Run و APIهای AI گوگل داشته باشید.
1- اول از همه، شما باید یه حساب Mpay داشته باشید که حداقل 1 دلار موجودی داشته باشه. آموزش متنی:
https://t.me/MatinSenPaii/4915
آموزش ویدئویی:
https://t.me/MatinSenPaii/5091
2- وارد سایت
https://cloud.google.com/free
بشید و روی Start free بزنید
3- این قدم رو من حقیقتا چون واسه‌ی خودم جواب داده میگم. میتونید بدون این هم امتحان کنید. ابتدا از
https://policies.google.com/country-association-form
درخواست تغییر ریجنتون به امریکا رو ثبت کنید
4- تایید که شد، توی سایت آفر گوگل کلاد، ثبت نام کنید با یه آدرس فیک امریکا از
fakexy.com
5- دقت کنید که برای این کردیت باید حدود 10 یورو موجودی داشته باشید. و این برای من کم شد و در عوض 257 یورو(معادل 300 دلار) حسابم رو شارژ کرد. برای یه سری دوستان یه دلار خواسته بود و نمیدونم داستان چیه
6- من تونستم بگیرم و تا الان هم مشکلی نداشته. دقت کنید من تمام مراحل رو با یه آیپی ثابت امریکا رفتم و لوکیشنم رو هم امریکا زدم با ادرس و همه چیز، تهشم با گوگل پی پرداخت کردم
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 39.1K · <a href="https://t.me/MatinSenPaii/5149" target="_blank">📅 13:57 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5148">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/cLXxwHxiRnh9vTc6xAp_YxI8BetsVHk8jsq4wCEOKKL1mIKcMLOJuFrRpSH6p0MvH8duCOKS2-uY1aTFptuXxtyII1tuNykfecOVChozxzURi_7sQX6DJkrY8oq6eJg78ujz15T8jN0jBi9rz98MbDTQ0oZylIIai3cFPfGqPlvR4vft9uR1UKV08S8VqDWzwcSE6eGnbV9ji2SIdurXHW6MFXyFNjfrZ6Ftp5OLU2mYpstKXX_NR7dsniduJywyA0FznOIZIeol2JlFYCJR_OWg8ecrjzd4A_A6ecqnvyqJSOy6zs99IH8KijN7l7U8SswT2iTHpk4vyHyoMH2ngg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خب بچه‌ها من وظیفه‌ی خودم دونستم که همه‌ی 210 تا کامنت رو جواب بدم. مخصوصا چون سر و کارش با جیب شما بود توی این شرایط داغون.
و الان تموم شد دیگه
لطفا قبل از پرسیدن سؤال جدید کامنت های دوستانمون رو بخونید</div>
<div class="tg-footer">👁️ 32.7K · <a href="https://t.me/MatinSenPaii/5148" target="_blank">📅 13:30 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5147">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">و گویا از apple pay ساپورت نمیکنه. فقط Google pay</div>
<div class="tg-footer">👁️ 32.3K · <a href="https://t.me/MatinSenPaii/5147" target="_blank">📅 13:22 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5146">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ld2SLq4Zu3iC_UodvIv0FV6l0lc1T7RZIlNCNc0i-9JTEMtZtM-NSL6m0IjGN1FlXcPTFvMMd3loRXyxELe8qAiqfexqcdcdoqDuL0tFeg11u071-MybbF_bsaWnIWZUQT-E0Lg3hqa9jUiHDVmUxShaArvMGEGIEyjsD81rdPS8mb0nM5oJlfCzbDU4vGZKF1C6YWMGpslxa8rak8NqgJ0YBYL_TyiAWoOOClGxc5uM3lfWojin9N6VmQkHCKR8BTU9AqfhC1-cqU0giYItGxWBpWja20dfNp4X2bwlu7Dwbd4FR-abxmA6Mm2bCQJINZXw0m4fU_VOS_srO5Y2hQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یکی از بچه‌ها هم تونسته بود با گوگل پی+اندروید
اشتراک Claudeاش رو تمدید کنه با
Mpay</div>
<div class="tg-footer">👁️ 34.7K · <a href="https://t.me/MatinSenPaii/5146" target="_blank">📅 13:21 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5145">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Ttgb1SyFcbOZcj-qKG0vhewIjjtGaBxyJM1ABFXG4_cYCcB5ydaIsJi7JhN5IQAJR1zX09EB4xPLoHBfEhLHXyQWfNYCVW2QbotPLO1WR49pxjN8UBFLh49rt7fS5b8HW7X4Z1UKxXHbwd4ZVDxOTA2rXDwf2MeXlx_Tu6FqeIR7q57c1CJwiGMUbtWBoZLdPurah9QFvvJwb-gDxaS5hF0n2CeOgc0EmAjiPxGKvwToTlcTZymffgSo97gsiHM_l1NRbF3XI9H7pev2UaiJvvr3Pik6R9ktwiMAXxsxxIU9a20WmqJKWZth2oLj0DAv1mumSjBnV47BXD-YRXjmMQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بازم مشکلی که خیلی از دوستان داشتن</div>
<div class="tg-footer">👁️ 34.8K · <a href="https://t.me/MatinSenPaii/5145" target="_blank">📅 12:54 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5144">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">و دوستان، با این کارت نمی‌تونید کریپتو بخرید. هرجایی بخواید کریپتو بگیرید نیاز به احراز هویت سفت و سخت داره
راه درست و خوبی برای نقد کردن پول توی کارت ندیدم من</div>
<div class="tg-footer">👁️ 31.4K · <a href="https://t.me/MatinSenPaii/5144" target="_blank">📅 12:42 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5143">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/nJCnMZVdvuECPZoF3q24ucbr-LjzraBQSqd1yH3D8mDRyEw33JfiRawo9D-L2ugL29-XLczs1kKfdXqrrC1ZSVzSBJMxQ23m7BY2HntR1BqC7tBz17sq4fMm762X5mrem9rSDJtsXBnHJCFpYbxpDGBW0RhnAT_LJnDtsBfN6KPua5BwRkWuK3nzy0QaCV3MYcRN7r7dMzfxivl_5AKq-hdrs-N9-wBsJAMz4ey5VUGJUOaxs0GAzorN77gyoQ7T56NT9eu7bdKK7XPz9CM0CghhXXwsBvf0coy6MrJ8Qfe0VelNWxkDLBTCC4UmQlwoHcJl-AhlyWTfJmj8lXNudg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نشستم دارم به کامنت‌های این ویدئو جواب میدم و دیدم ای داد بیداد:)
هیچکس نه دیسکریپشن رو خونده نه کامنت پین رو نه تلگرام
متاسفانه تغییری که سایت Mpay داشت این بودش که دیگه با پنج دلار و ساخت کارت، اطلاعات رو نشون نمیده. و من هر طور تونستم این قضیه رو اطلاع‌رسانی کردم
برای دیدن اطلاعات کارته باید ۲۵ دلار رو واریز داشته باشید و گویا این قانون رو برای جلوگیری از سواستفاده و سیاست‌هاشون گذاشتن
من سعی می‌کنم به تمام ۲۰۰-۳۰۰ کامنت جواب بدم که هیچ ابهامی نمونه.
این Ai جالب یوتوب هم که دورش خط کشیدم خیلی به درد بخوره</div>
<div class="tg-footer">👁️ 36.2K · <a href="https://t.me/MatinSenPaii/5143" target="_blank">📅 12:41 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5142">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-footer">👁️ 34.5K · <a href="https://t.me/MatinSenPaii/5142" target="_blank">📅 09:57 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5141">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">چشم روی هم می‌ذاریم دلار ۱۰ هزار رفته روش</div>
<div class="tg-footer">👁️ 35.5K · <a href="https://t.me/MatinSenPaii/5141" target="_blank">📅 09:31 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5140">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">بچه‌ها من می‌خواستم آموزش کردیت ۳۰۰ دلاری Google Cloud و پلن Always free اش رو هم بذارم اما واقعا خسته‌ام. فردا می‌نویسمش واسه‌تون.
اوراکل متأسفانه خودم موفق نشدم؛ به شدت گیره روی آدرس و آیپی و...
اگر موفق شدم روی لوکیشن خاصی، بهتون میگم</div>
<div class="tg-footer">👁️ 37.3K · <a href="https://t.me/MatinSenPaii/5140" target="_blank">📅 23:53 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5139">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/IazKpTGliPy_ippZ_uiVFFpbmUJybIW3eK2NGPpq8tW-XxWPik_6OjzCKbUsQYbCSbEuy7dNb9OhQgXBkBSDW4FhL2pz8lB9vZI_aTd31cYoQ9BacHSa3Bza1AG4fKzfVtzOFd2NJewySN8TRTsh83nFpEcmb5gtCN3tHSuxj9v9R3jbX_aozI35ABu3fI8TPom4K8l2WHdKT47LJE0cKeGmy0owLLI36j17_652LzvrRXogkxCPMyylm5htbgjxt5eaVpEU0hEaZ0JDXF3AHlnAskl5g_eZZp8_3vZ0Ao-EE7MD50U50AeYzNh-t0pZvxNIjfxnpQoDIrYNrk-hxQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تجربیات خوب یکی از دوستان واسه‌ی استفاده از آمازون</div>
<div class="tg-footer">👁️ 39.3K · <a href="https://t.me/MatinSenPaii/5139" target="_blank">📅 11:33 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5138">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">وی پی ان رو ساختم. باید از بخش Networking، پورت ها رو اجازه بدید استفاده کنه. بعدشم پنل سنایی نصب کردم و یه اینباند TCP+Reality ساختم به راحتی هم مستقیم کانکت میشه بدون تانل، لوکیشن آمریکا</div>
<div class="tg-footer">👁️ 36.5K · <a href="https://t.me/MatinSenPaii/5138" target="_blank">📅 11:24 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5137">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/qln4lHC-L-AhjqFpge0jAGK71-e-3671ejunSkdDLD5LFqgWL_D8HDFrpfNnI0U0YMxnRBBgLYVzP2M23q4AX5cBNDfUVMawEDhfZdqEdw0eMtxH3jhQjwA_R-oGDcRLIhFsQbvwSo-YH2FNt8aYvsZBcFrOtwKujo7giTiqsqqq5M8nofUYzytuefxFHv-qYbUE-X9CgdXPYyZvrMyHnK7niPyCVPdFAdgPkmYbISCNucts6Yp5RPZ3sOKBqDabPenZs_1neYCQHBjmaoLIsfg2m15SNeVpxIUODXd47VPyUITTNw4L-f3HBGPk7SLDaFa9i2YclErmsKqoXtgkyA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آیپی‌های باکلاس آمازون
🥰
بریم یه VPN بسازیم باهاش و یه هرمس هم بالا بیاریم ببینم دنیا دست کیه</div>
<div class="tg-footer">👁️ 35.9K · <a href="https://t.me/MatinSenPaii/5137" target="_blank">📅 11:20 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5136">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/LqD6bii2JfoSzF4n9hG7ztnEWYYEZYu01zLScNQVRoMZErl6FIDHJ084AsJrgn0VOCfc-UKQE08c2OclImSBAgm7jbCiC3m50RTmhnd8bzTm4IiL8WCxZe35jylPp2gCqKveNr5cCeF6bvBi_OEEyjgmW2zzxakQ3kfvKvvV2svKCbgFDn99QYN7LR1vaNgIx8kRymPU-xwyzYb-iYxCl4mfKlfyX4yBCH_CKIe8A37oRigD9M_o95sZJtXQoiBXAGjFmarPBUhFDwotleqQ6SpKvvF7jQYtTC96JnsXSSI1gpdWanblWa5ETUHxZyysPmTNxjGVJpu1vjgoFSleRQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یه سری از دوستان میگن که اکانت ممکنه ساسپند بشه اما خب.. خودم هنوز ساسپند نشدم این ریسک رو در نظر بگیرید رفقا</div>
<div class="tg-footer">👁️ 34.8K · <a href="https://t.me/MatinSenPaii/5136" target="_blank">📅 11:06 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5135">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">آموزش گرفتن 200 دلار کردیت رایگان AWS آمازون  با این کردیت، شما می‌تونید روی آمازون سرور یا Storage و کلی چیز دیگه بسازید. اعتبارش 180 روز هست و اگر تموم شد هم، اکانت جدید:)  1- اول از همه، شما باید یه حساب Mpay داشته باشید که حداقل 1 دلار موجودی داشته باشه.…</div>
<div class="tg-footer">👁️ 32.7K · <a href="https://t.me/MatinSenPaii/5135" target="_blank">📅 11:05 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5134">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/fUtynrp9incjzSFZOnph8CSwVijDXhePAoZqy-f8D0Aw-MOe0idnjFeb3I_6TGR659Lr4TZQJ8z3ZVM6Q_56htdQ3wLBvNqayUlawhaV0Uz9DJLFAVZYljXBUokqBq9jexjcVgN7AzSNvxJKI1__0U2KgtJDqbjjV_-8Af6tqD31IUWPR_VYsXPVN4s3GZhoN-_NbYjR4H5BE3w0MA66GPL6ucrENBxUAvf0synqGe4vATw6UTgySOu05nNUAMHs_Auw1MpbvZGNcI4VrCFf1Lmj-ju41cpHb7xJelDYb6Wk-prZn5PTcqF1J4TCXmteR3ZinVI0EaGltUJoSXR-Jw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آیپی‌های باکلاس آمازون
🥰
بریم یه VPN بسازیم باهاش و یه هرمس هم بالا بیاریم ببینم دنیا دست کیه</div>
<div class="tg-footer">👁️ 31.6K · <a href="https://t.me/MatinSenPaii/5134" target="_blank">📅 10:55 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5130">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/Nwjy6rW0Xwwc6GBYHJNzm4BiAelCQbKUGfDp8izkU1krNcYWcxtPx5B4Bcj1BWQOOcfXEsSh5cDbbfbaZfJjJEp9udlQ8RZQ6leok8q0syL9oV6cKb3XGmoIQJ9SdJLHzH5gej7QT_AQt1Kee4UQQgzVFUlRMBa05iLgXLIOo7OHf4tJSZZyM-1iThGgKydbTqG0yPBa9_r-sqq940xrz4deJ1-o5MjiKC6NWxtk9Epq-UGLLThbZMkEOerAC1b1lsKdjlZ3qk569vWNHDcFfWrgrHLi8gY5B_Mnq3g4Oo_QduR1NnExpcB2tNQ-rcuctzyspKEr3Lz7l68xCNZRzw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/KVm6WIGsHYjuJF7jE7Ml-o-VMZ6Uystn3WPAr8xmsBWQzKYFblwR-FuMEKdktThEwfzoIJ1_bwg9N33wAaRVGpBzjAzB5Graw_u8yYrDxwg6eI-gpRHRMwB2oSZZbFB7b809IwcLLGLQFapni_fQHw38xi1OTdIXwStHxDMfFi1SE5JeSdD8v9OLsTUEiVDsgba5TdPgBJ6T-NI0TZuJQtDD9SaN49MJKmAQ5a67pfxgvKGWK86PNrGQ6_8HtlHGy6B3eks6ZaFDtJS0qH0746fZaKq7cqwkkygBTzMp38vCQ45QYkn2vEU0M01jDfWhZ_TWlPO3WBp3em-LVThNkA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/O2lsTmMKMzdZyiuKDMmJFVpI_Pm5o3WVGXnLTpJkF3DtzqK48KrDfrvydWA16rReptfkTPlpJilE_6bKYgtQ8N5a9MZwY5SkgsQvI2hPD2-C9S2vaAqDBYJPZ255jB2rt84HgYLhs9S_GTMnoBF5W_zxNZF_a1sOac1j1_-QKIQmoTzOWUWlh34T2OEnUDLmRTXYS1flckJrXZoZDsUNmeJX5xMiY8srG2_JJKwiksGR30Ko5iVOdEJ0DtHWrqq2mq6Y4juz33B2i_eGz5mgjXWOAvYTiVBbd6g86VA5CAtQXyNnC1Enbx6QRyie6-TyX_1ycH_8fPDDECl1WvjFlg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/atEL94LKtsmc0HNVjJV-ux0tFAzvwi_FDlGFcC0WFyKzB4BGHnEjskXTSCq1so8xc8eW-ewm8D7XTPZFXVaOHbTCXe8sJKF5zK0s0GhPAEf8G3ATEkP6TXyqBVh-0k-IRE3eU9rHJR9d7O2ko0UjAe2wnYGMhR_RbkJ3Zg43e8AOF1Lm49aOnF_V0DNy55AvqFkx1Gt4yUUTQGH-1r_YYp4XmBdaZcLpuOD5XBkhaq0KPUic5uhuw2YPy0PZ_bM_6WjBPSA0jS_kIE_GvoVKG1YjFSSBHY6sONwX-J0FFpZilWNFD_xCdsgq7je5MgbpYmTD3QEdVK_xTNE-0tIDrg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">آموزش گرفتن 200 دلار کردیت رایگان AWS آمازون
با این کردیت، شما می‌تونید روی آمازون سرور یا Storage و کلی چیز دیگه بسازید. اعتبارش 180 روز هست و اگر تموم شد هم، اکانت جدید:)
1- اول از همه، شما باید یه حساب Mpay داشته باشید که حداقل 1 دلار موجودی داشته باشه. آموزش متنی:
https://t.me/MatinSenPaii/4915
آموزش ویدئویی:
https://t.me/MatinSenPaii/5091
2- وارد سایت
https://aws.amazon.com/free/
میشید، و روی Create free account میزنید. بعدش سایت خودش شما رو هدایت میکنه به قسمت ثبت نام. VPN هم زیاد مهم نیست چی بزنید. من با کانفیگ‌های BPB رایگان رفتم که آموزش ساخت اون هم اینجاست:
https://www.youtube.com/watch?v=iAbYpjXyLpY
3- برای آدرس، یه آدرس فیک از سایت
https://www.fakexy.com
وارد کنید. شماره تلفن هم من گوگل ویس زدم اما نامبرلند و سایت‌های شماره مجازی، همه‌شون برای Amazon یه بخش مجزا دارن و زیاد هم نیست هزینه‌اش
4- یه ایمیل تأییدیه واستون میاد و تمام! 100 دلار کردیت رایگان میگیرید، بعدش هم با انجام دادن تسک‌های بخش Explore AWS که تصویرش رو گذاشتم، می‌تونید 5 تا 20 دلار دیگه بگیرید.
5- ممکنه محیط آمازون واستون گیج کننده باشه. نزدیک‌ترین بخش به یه VPS معمولی و راحت، توی محصولات قسمت Compute، بخش Lightsail هستش. چندتا نمونه قیمتی هم واستون گذاشتم
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 36.6K · <a href="https://t.me/MatinSenPaii/5130" target="_blank">📅 10:12 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5129">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/MlmNCrsSwuEb-HPC-Q-tWST6ZMH6DdGpT1pVqUudyIG1zkA4utqRrnxdYbwXjVXOy3X7a2IWOTaCm81P7nCzs18fpm2c2pC3XCBVuRSnG-VU89Gu39DYDBJnhdr8iugrdbkeVvzalrDEgVqS62zzI1fvzpIpC1V0_gzUyy26-QwgBoDbVACLZwc1a_o-hnxo4SeFkJSiwGtSpBEZBYNb9rN5kfvFRBBSd8dKWjR4mXPX6J1f8DcbSSTXozalCNoq83C02Fnla-0n18b0wPjbxIA0chW_xf45C3JOTpJmlQO6ymRbnVZtAyJeaG9hObTtgQYZAx-X23Tkw5YS4SRiGg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">با ثبت نام ۱۰۰ دلار میده بعدش یه سری تسک کوچیک انجام بدید ۵ تا ۲۰ دلار دیگه هم میده
و می‌تونید ۱۸۳ روز استفاده کنید
به نظرم می‌ارزه</div>
<div class="tg-footer">👁️ 32.6K · <a href="https://t.me/MatinSenPaii/5129" target="_blank">📅 09:35 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5128">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">این کردیت ۲۰۰ دلاری آمازون رو هم موفق شدم بگیرم با Mpay
آموزشش رو می‌نویسم الان واستون</div>
<div class="tg-footer">👁️ 33.7K · <a href="https://t.me/MatinSenPaii/5128" target="_blank">📅 09:33 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5127">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">خب بچه‌ها من تمام مدل‌های چینی و آمریکایی رو تست کردم. فعلا برای ترجمه، رتبه‌ی 1 رو
Gemini 3.7 Flash
میگیره. رتبه 2 هم متعلق به
Claude Sonnet 5
هست
که خب فلش توی هزینه، می‌بره. رتبه‌ی یک و دو به جهت قدرت ترجمه هستش
هم برای ترجمه‌ی کتاب فانتزی مقایسه‌ی سنگین کردم تمام مدل‌ها رو(از جمله GLM و MiniMax و.. تا GPT Sol و اینها)
هم برای ترجمه‌ی متون تخصصی علمی
هم برای ترجمه‌ی کتب برنامه‌نویسی به زبان عامیانه‌ی فارسی</div>
<div class="tg-footer">👁️ 35.8K · <a href="https://t.me/MatinSenPaii/5127" target="_blank">📅 00:31 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5126">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromLinuxor ?</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KjwXDR4yj-NXrOf6GKXCaMCUIUJSa8Ewzgn2q7cpkkH5AiUivElE5HStqZZLmNb2x1rhg63qzhErEue4r_qPnIK_iAqNkg_z5XF2KVVHgdLV5YLRwW-4aXGxlEZIgLvFDFCOsmDFjO6D0ZI6lOZBQCkEsswxYoGxcxR04oQ7YjB2jaARNRT073p4ISu4VhbU285KI1jteJE-n2metOc5gFELgSK97pkYocaboxcT8sFuC_4Yya0mgZfBtRokWg0wLbnTaCm0BaQIuAq3jLdhmHybxjhywCGKChbsbuSF8-iabgyvzmUeBXKArAL-44pLbHTLtmLULfVo3B2yYiiS1A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اگه دنبال ساختن یه AI Agent برای کارهای علمی و تحقیقاتی هستید، این پروژه رو حتماً ببینید: یه مجموعه از 163+ مهارت تخصصی که به Agentها کمک می‌کنه کارهای علمی رو فقط با تولید چند خط کد انجام ندن، بلکه بر اساس workflowهای تخصصی جلو برن.
از Bioinformatics، Genomics و Single-cell گرفته تا Drug Discovery، Protein Engineering، Molecular Dynamics، Medical Imaging، Machine Learning، تحلیل داده و Scientific Writing. حتی برای کار با دیتابیس‌های علمی مثل PubChem، UniProt، ChEMBL و ClinicalTrials.go‌v هم Skillهای آماده داره.
نکته جذابش اینه که این‌ها خودشون مدل AI نیستن؛ در واقع یه لایه تخصصی روی Agentهایی مثل Claude Code، Codex، Cursor و ابزارهای مشابه قرار میدن. یعنی Agent می‌تونه بسته به کاری که ازش می‌خواید، Skill مرتبط رو پیدا کنه و از دستورالعمل‌ها و workflowهای تخصصی اون استفاده کنه:
github.com/K-Dense-AI/scientific-agent-skills
@Linuxor</div>
<div class="tg-footer">👁️ 33.2K · <a href="https://t.me/MatinSenPaii/5126" target="_blank">📅 21:16 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5121">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">WhiteVPN-V1.6.4-arm64-v8a.apk</div>
  <div class="tg-doc-extra">34.4 MB</div>
</div>
<a href="https://t.me/MatinSenPaii/5121" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-footer">👁️ 29.9K · <a href="https://t.me/MatinSenPaii/5121" target="_blank">📅 11:15 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5120">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sHFtREBMdZbHdJtWpDJDQENdNsZcPR2dfLZ1Eb--C2pOqFKpgB-iAMqdUxhw-1OfeaLltFMuhVQMKA8PuagsBB1jTv42ObqLuI1qXt-Bnn6RJrdYPCAyUsv6IDFM27XMF9UglhHFowdVFEg8jqFNp7meGYJijGyt-iGla_WkXt3tWquxS2RYNp_jHTGCsjYr6N8uE5Zs10Lm2TL38iDrdA-fHmXoOe_gNJVleqJ11Ti0YUGgko-fM02A4mf6V5Tn5uGk01_bYf1C9MImZlxiEEHCqli50TzkBY4ng3oUUcwmlXcLRoqAdmDkbN38QbHorQbwvETOvFnGby1StF5S8w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💬
ورژن جدید WhiteVPN  1.6.4 برای گوشی های اندرویدی
تغییرات در این نسخه:
🎯
اتصال و قطع اتصال پایدارتر. رفع مشکل قطع اتصال.
🔒
بهبود امنیت با رفع مشکل لیک با IP V6
🔭
افزودن کانفیگ با QR Code یا Clipboard
🎨
نمایش واضح‌تر وضعیت اتصال و بهبود ظاهر برنامه
📱
دانلود آخرین نسخه از گیتهاب
نکته:
⚠️
در صورت دانلود نشدن از گیت هاب مرورگر خود را به فایرفاکس تغییر دهید</div>
<div class="tg-footer">👁️ 30.2K · <a href="https://t.me/MatinSenPaii/5120" target="_blank">📅 11:15 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5119">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">باز دلار رفت بالا و این پیج‌های زرد اینستاگرامی در تلاشن پکیج کسب درآمد دلاری از برنامه‌نویسی رو بندازن به ملت</div>
<div class="tg-footer">👁️ 29.8K · <a href="https://t.me/MatinSenPaii/5119" target="_blank">📅 10:12 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5118">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">باز دلار رفت بالا و این پیج‌های زرد اینستاگرامی در تلاشن پکیج کسب درآمد دلاری از برنامه‌نویسی رو بندازن به ملت</div>
<div class="tg-footer">👁️ 31.4K · <a href="https://t.me/MatinSenPaii/5118" target="_blank">📅 10:03 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5117">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">آموزش ویدئویی رفع مشکل آنتی گرویتی و سرویس‌های هوش مصنوعی گوگل:
https://www.instagram.com/reel/DZ7NWUOMeHy
هرچند ارور ۴۰۳ به خاطر vpn هست و صرفا باید از کانفیگ‌های bpb استفاده کنید</div>
<div class="tg-footer">👁️ 32.8K · <a href="https://t.me/MatinSenPaii/5117" target="_blank">📅 09:38 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5116">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">زلزله به بزرگی ۳٫۸ در پردیس در شرق استان تهران
در عمق ۸ کیلومتری زمین</div>
<div class="tg-footer">👁️ 35.4K · <a href="https://t.me/MatinSenPaii/5116" target="_blank">📅 08:09 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5115">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">بازار کار جدید دنیا و هوش مصنوعی! توی 2026 چطور می‌تونیم برنامه‌نویس بشیم و رقابت کنیم؟  توی این ویدئو، با یزدان عزیز در مورد این مسائل صحبت می‌کنیم:  1- مرگ پکیج‌های آموزشی و یادگیری پروژه‌محور 2- دیده شدن و شبکه‌سازی به جای رزومه فرستادن 3- تجربه شخصی خودم…</div>
<div class="tg-footer">👁️ 34.8K · <a href="https://t.me/MatinSenPaii/5115" target="_blank">📅 07:27 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5114">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/qypH_fiphdx_G6VUXRQLYjEsJ3OHPN65eNuYMDij20t01tKXJzO0rta3_AoiicN6fnbVsBf0f4s7LxpAQbnjB1c_Ko8LjZmQFAZJVjuVzF1nXTanSPRXjnx1XFvZ2I8KXRTKbmJYd7zF8pKbNNPJPldXRoN1mxLvqwirAm7vjD1KAt6_6qr92yTk0RXTyKXTpX1KMZPeyxMTbOneW8uro_hRwkmNuUo6ugHyfHbvsDLuyWERXz83YXjQ8NRw1xb_1bf2cXNxBjm_Z0gft8R1Jbn7HaBQzhDVch9w3RamcFYaHIn2UObzV34CWKqXq2XlalQTLcxdroyQeL8K5QX6Zg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خدا کنه هیچی راجب
mpay
نفهمن
😦</div>
<div class="tg-footer">👁️ 34.5K · <a href="https://t.me/MatinSenPaii/5114" target="_blank">📅 07:01 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5113">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">مجددا:
این api های رایگان ممکنه امن نباشن پس توی پروژه‌های حساس استفاده ازشون توصیه نمیشه</div>
<div class="tg-footer">👁️ 34.7K · <a href="https://t.me/MatinSenPaii/5113" target="_blank">📅 17:43 · 08 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>

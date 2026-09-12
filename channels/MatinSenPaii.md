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
<img src="https://cdn1.telesco.pe/file/j-3tD8so65HjIBuB-Yty6V6_FnfTCe0wS-uFklroAgGTWjfqBXb252pleQolFCI-FeKKI1JniYaWjgyp0o4K_4V-rMskzaFzVHMrWxjt_Toh8w29Kjyh4-EUqg-O2bo8zbCIrgX_lHIKcentm-ync9QH_0YjgF2NUmuIh7QpxEzbfcGoMHYjBx4QhirKaQYN4nHVMQICv8OOq6szzN21owco3clenYKExALnZOFwicLNTTkoxno9Scmt51QNNH010cE5C5flgW2B2wJZGavtzMlSGJ64_baiYyhv_uUHPeGY_TXiz3Sw_9O11NBc1xL7YMoTNV7VoS-vLAAKHHRRjg.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Matin SenPai</h1>
<p>@MatinSenPaii • 👥 155K عضو</p>
<a href="https://t.me/MatinSenPaii" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 متین هستم و کامپیوتر رو دوست دارم! در حال یادگیری هستم و چیزهایی که یاد میگیرم رو سعی میکنم به شما هم یاد بدم اگر به دردتون بخوره=)•YouTube:http://www.youtube.com/@Matin_SenPai•Github:https://github.com/MatinSenPai</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-21 20:48:51</div>
<hr>

<div class="tg-post" id="msg-5236">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">این دیگه اسمش زندگی نیست... تقریبا دیگه نمیشه سیستم خرید.   این قسمت پلن های امسال هم ضربدر خورد.   فقط تلاش کنیم زنده بمونیم.
✍️
0xKaveh</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/MatinSenPaii/5236" target="_blank">📅 14:25 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5235">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/wBSfxVs1T7uijSxrLlFRxEWnMxszTAHIOoLywlfI1Rh7591xIB05Lifv8HdrLsCuTymUrRr4GqsZMkBADIa3p4P8VbzSb9IHsQcal7kLTBlaklC__YANphr0xHGSNNBSD_fW0D2u9ldSOVRv_xOk60dmXEopOit2e0PDNcWW73pkPbl8MU5N55wT_DNYOjQhw3GZyZNvlESB1_bF1MEd9LhGxBpr0Yy0j4NrjkMjkeZc-IKAoXxGerjerXezs_NAsYXVFfDAVi-ji1xarakygggFNPVyHcRV3voES2rshA9_A77suGYFOXhKa7egKts5LvwjstlKksszlRL4nCed1w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این دیگه اسمش زندگی نیست... تقریبا دیگه نمیشه سیستم خرید.
این قسمت پلن های امسال هم ضربدر خورد.
فقط تلاش کنیم زنده بمونیم.
✍️
0xKaveh</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/MatinSenPaii/5235" target="_blank">📅 12:57 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5234">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/bNIbQaiCuAu67LGpRL5TyT7o6b8zvh83V4ah6hYrcp3y-r8dPYpL1sbONNWP-N_O2Q-086pb3ilk5WSD80o9rH6m3Xy5yHIBC0UAgV3dZFcd38vAU2zePZ0zZmEbSwYK73gJbR7A38HgayhqRbqwaMANLqNZMG9A_94hgoNhrgHyvfQCDsSFO32YFUOy3ry5MYoyoUhfP9y8xwOpGzTlHHEdy4mPKKkOmjtpu75xj31hVGaGKH0MsRxxT_vFzzmr2XTSSXaC9anbeGS37mKGBjAvvchSBPn6D9NYqUiciCOGzgwoSCY_U9Z-yYPh8-Zc9evOpNSxII49LTkonHnlVw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">از طریق سایت Freestyle.sh می‌تونید یک سرور رایگان بسازید؛ فقط کافیه اطلاعات حساب‌تون رو وارد کنید. هیچ هزینه‌ای از شما کسر نمی‌شه.  برای ساخت حساب مجازی هم می‌تونید از طریق MPay اقدام کنید.  مشخصات سرور رایگان:  RAM: ۸ گیگابایت HDD: ۳۲ گیگابایت CPU: ۴ هسته…</div>
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/MatinSenPaii/5234" target="_blank">📅 00:58 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5233">
<div class="tg-post-header">📌 پیام #97</div>
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
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/MatinSenPaii/5233" target="_blank">📅 00:43 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5232">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">یکی از صحبتامون توی استریم با یزدان دقیقا همین بود که ما هنوز نمی‌تونیم سقف پیشرفت AI رو بسنجیم؛
برای همین اکثر نظرات به ظاهر کارشناسانه هم در حد حدسن. و نه باید شما رو بترسونن(حرف‌های ترسناک که ai ترمیناتوره و دنیا رو میگیره
😂
)، نه باید خیال شما رو راحت کنن(حرف‌های خوشایند که نه بابا ai جات رو نمی‌گیره)</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/MatinSenPaii/5232" target="_blank">📅 00:27 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5231">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">راجب این ویدئو که فکر کنم مال نیم‌چت پادکسته، حرف‌های زیادی دارم که بزنم. اما اکثر صحبتا نه کاملا غلطه نه کاملا درست</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/MatinSenPaii/5231" target="_blank">📅 00:12 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5230">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/dad69f2160.mp4?token=WV-Zl33AwgpN9w5VT8nnOyoeZVJORaf8laflhaQMnxwmunIkxiLxUh70zxisHwGV7KewwHTNOQ07Xifzxt_XZq7QXxBZli8V2QHt23MU1-U__MR8QiVSWhSo7f3UzddIssmaXj_onD5VzRC_H0tzr0Zeu8u0AT2X3nWQFvzbfWarH4jY-Dho92UNFC2iZpf6XGNxLxiAkmnb8xBnW03KRXTrANZwCbh7IzvhvUWlB7aUfVtzMO4t_TwCwrOd8lbP1gCud7k-cLaj5bB6WNEsYgxG_cM42IoufQ2voEZZjZfFHQIawWl5zwQxoUhEK3iboHmgevVS2cyEEOR721ATPw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/dad69f2160.mp4?token=WV-Zl33AwgpN9w5VT8nnOyoeZVJORaf8laflhaQMnxwmunIkxiLxUh70zxisHwGV7KewwHTNOQ07Xifzxt_XZq7QXxBZli8V2QHt23MU1-U__MR8QiVSWhSo7f3UzddIssmaXj_onD5VzRC_H0tzr0Zeu8u0AT2X3nWQFvzbfWarH4jY-Dho92UNFC2iZpf6XGNxLxiAkmnb8xBnW03KRXTrANZwCbh7IzvhvUWlB7aUfVtzMO4t_TwCwrOd8lbP1gCud7k-cLaj5bB6WNEsYgxG_cM42IoufQ2voEZZjZfFHQIawWl5zwQxoUhEK3iboHmgevVS2cyEEOR721ATPw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">راجب این ویدئو که فکر کنم مال نیم‌چت پادکسته، حرف‌های زیادی دارم که بزنم.
اما اکثر صحبتا نه کاملا غلطه نه کاملا درست</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/MatinSenPaii/5230" target="_blank">📅 23:51 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5229">
<div class="tg-post-header">📌 پیام #93</div>
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
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/MatinSenPaii/5229" target="_blank">📅 21:53 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5228">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromxsfilternet | فیلترنت(امیرپارسا گودمن)</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/prym-nfumx8oBr0NOPxEcl70J9OGYuvT52izPLsNAegTL_AT5a_kFmtOHo2WcPPsbY6Surk9aBZ-1GrwaKPlGCuee96oD6uWpkm7bqz829V5C9hcnMQCkt9KPFlqbzN1wqZEN8iAmAfAocUpt3Ow7StKQIpNnHZlyXD4B9T7e-trpdPMqVT4x0yQ1BsIWwpbxVTUZ-LdmuALPFvfYow-_bxYhFrZv3jCo0_b2kepygSaxfsHsn9Waj2NkuR_GdsrVcP7s4Mo4xQ2H3pM_ma1UqwQeK1pWWsa06xxMnWETDHPo_mPBWcih_qgfEt4482a5_cLCv2qzKf-cDZE085PbQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بلاخره آپدیت کلاینت منتشر شد.  هسته شو تغییر دادم و Aether‌ آوردیم. MASQUE H3/H2 Warp/gool پشتیبانی می‌کنه قابلیت Chain هم داره با سایفون. برای شرایط سخت خیلی کار شده که راحت متصل بشید (حالت اسکن و Obfuscation رو تغییر بدید)  نزدیک یکی دو ماه فقط توسعش طول…</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/MatinSenPaii/5228" target="_blank">📅 20:45 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5227">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/WX4UQRnCCqqAie5PLmbK_GUl2C9skBZ_BMQ5JLXlyjzUc9tnuXEAX_G-ioqreDsWgNEXGHUkzQZwNbvXlF4ejl2aRbNWRftHGCddJbu1WkqPibmOOVFWGIKZPvatNhURDDeQYu2LYuMfHC9bZ6F-Q7nog91ho1L1ApOkphS4QR9sxU7ZhK-OIPvBqoBXoNXIwtQxhwDXZ7EMoN-x6h0UY-QeRWg1cOtTH-jZ8bXt8Z4-ihekQ98cUwyFfNt4cgC4JeIdWj2SdoeuJke0XP2RDPuaK-p9aPdSGB2gDRqpv0gILxjoxzHui6JBUQhs-siGv6dk-s6RdVW5VN6KUNkWzA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اپ DreamBeans بالاخره فید من رو حاضر کرد خیلی اخبار رو تر تمیز بهم میگه. از اخبار تکنولوژی و ai گرفته، تا معرفی سایت فیلم و یه کم پیشنهاد آشپزی و سفر و...  انگار که جادو می‌کنه
😂
دقیقا چیزایی رو میگه که توی ذهنمن چون عملا دیتا سرچ گوگل، جیمیل، یوتوب، عکس‌هام،…</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/MatinSenPaii/5227" target="_blank">📅 18:59 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5225">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/BVeUmy1dwwILXwMpuqVs0hWTeWAOTp-hRaUt0L_aY_Vjn-WVp0ADZHngzIC1YNPhhfJ-HScPwCKeJ0BT8u8NLsqufg7mRg8CuGbFRhjLcVIVlbW1FLm9DQ5sQIQZbUK0MjDoiJoQ7CCfXMMB_0ByyWC2g9kXfUB8nL7BXubV30inQpZx30MMs8ATnXLhocZDiRx0ZeZif4WYdqBOw1bVB_BOjadygSYYotBqZbJsmbbunVOwmGbPgptf9EzQ7XR8pbd8A6Daz5-JaPp7AvEXpUZ6Ifj23LYtRhkrWwBCAiCK5zQ-QPufxVl3twuDsXP1mGayvPdTiM9Mi8SsUTMJgw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/C2KNOu4_l1fxs3aDDXYDAtb5tA-1W8kLtN1t4Excp8x9UTgr2v6_fItn4oesJE9FTVjNKyy3kFPzhQlqL6r6_aIYj23ZyjuX82GH2uT8jgmkzh1_bYPIrxMBaul3BKKpiBibvdWxNvoXj1D0BXEQk7WsE8yoi4uncI2u3GqHznWWjSeCxn_ilhzNaVWf5w8U6mWbkGRJHwbSeZoh6ZsscEtaFfletvq6EASBvJwjPdiIpwWJ7pnoL1aaQXL6dSDFiMAM754RZqHbyo3MTbXEEo33RWwlb-6KIgPRkqWXtCl9H79iYuMJx6VemSiCKHd6Aij3hEhcnzcSQbMOPYzAKw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">اپ DreamBeans بالاخره فید من رو حاضر کرد
خیلی اخبار رو تر تمیز بهم میگه.
از اخبار تکنولوژی و ai گرفته، تا معرفی سایت فیلم و یه کم پیشنهاد آشپزی و سفر و...
انگار که جادو می‌کنه
😂
دقیقا چیزایی رو میگه که توی ذهنمن
چون عملا دیتا سرچ گوگل، جیمیل، یوتوب، عکس‌هام، جمنای و همه چیزم رو میدونه و همزمان ترسناکه و باحال</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/MatinSenPaii/5225" target="_blank">📅 18:28 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5224">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SkE1kn3ocjB99XrtY6REN37drLLc8dkq_7xf4cy-kMLBF92KbcnYl6flhps20b8r0q9sG-WxsiONQHMa51tOKeXywNhMjwVDkiTKVBXnhH3y_5ZxBuI6FTGJsiSUODgAynfCWrHxbb-aw4gRMeR8WNhbQzH44sBDGZ4LUpqgRzqxkkNrXUrscVQXbIH-UM3lOd2FOEEmPkxsA2p_jb83oUXJXB6KcZr6T1WtGKUwZuuXY3vNwoNTLZbg_xIzN6iv3_OBt7d3Wnl8y7S--nmm5ivhkkf-G_tlZWtjwC0HvWCb86pFFNChWCjoeTOcyW6N_bVXKtCvTKvXx7fvc25OzA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بالاخره تصمیم گرفتم برای WhiteDNS یه Patreon راه بندازم.
حدود ۷ ماهه که این پروژه رو با هزینهٔ شخصی جلو می‌بریم. توی این مدت بیش از ۱۰۰ سرور ساختیم و هزینه‌شون رو خودمون دادیم. از Conduit و DNSTT شروع کردیم، WhiteDNS رو ساختیم و در روزهای قطعی اینترنت هم با MasterDNS سرورهای بیشتری بالا آوردیم.
این هزینه‌ها صرفا جنبه مالی ندارند. مهمتر اینکه با استفاده از همین زیرساخت‌، سرویس‌های رایگان و با کیفیت بهتری برای افراد بیشتری ایجاد کردیم.
امروز WhiteDNS حدود ۱۰ هزار کاربر فعال روزانه داره که در مجموع، هر ماه نزدیک ۱ میلیون اتصال به سرویس‌هامون ثبت می‌کنن. همه سرویس‌ها کاملاً رایگان‌اند.
بعد از راه‌اندازی سرورهای اختصاصی داخل اپ، فهمیدیم وقتی زیرساخت دست خودمون باشه، می‌تونیم کیفیت سرویس رو خیلی بهتر کنیم. الان حدود ۱۵ سرور رو هر چهار ساعت یک‌بار روتیت می‌کنیم تا احتمال فیلترشدن کمتر و اتصال‌ها پایدارتر بشن.
این مسیر با کمک تیم ما در ایران جلو رفته؛ از تست و پیدا کردن مشکل تا پشتیبانی از کاربران.
برای ما Patreon کمک می‌کنه این کار رو پایدارتر ادامه بدیم: سرورهای بیشتری داشته باشیم، کاربران بیشتری رو پوشش بدیم و روی WhiteDNS و محصولات بعدی‌مون وقت بیشتری بذاریم.
اگر دوست دارید از اینترنت آزاد حمایت کنید، خوشحال می‌شیم کنارمون باشید:
https://patreon.com/cw/WhiteDNS</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/MatinSenPaii/5224" target="_blank">📅 17:13 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5223">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">جدای از اون مسائل، اصلا یه چیزایی از این اسناد در اومده، عجیب غریب! ترجمه‌ی ai: گزارش نشون داده که یه کاربر Kimi اومده داده‌های نظارتی چین رو ریخته توی مدل تا براش تحلیل کنه ببینه یه آدم خاص رفتار غیرعادی داره یا نه. این بنده‌خدا احتمالاً فکر می‌کرده درخواستش…</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/MatinSenPaii/5223" target="_blank">📅 16:53 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5222">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/S7iWBVQWQEHaUaG8MwJ7eT4MeGlRXNryos7c4j4lZx6ak9jQ8nhxCQv8nVfxc2vp63tf_VuL6rZ6e8CxnysESazt0ka6LyeBBLSjupHxrNQVexLj1izFmra8dUWPzfxVq7TPuNm2ZM5wQnrPgbY1iNisykBS5fRFcbVHVjXMPfQAT8CIY8Fl4TZjRzUxdOkU8lTDK_EmZVXK8s5-3Zi_Iy0Qa27QbWT-KCBRLbwKiNvXpOEjNgVnG8rKzE8oPaHsKjxYGOAYVnIfcxKqOrVJliRBLNAC23RQa9TJ1mzpecB6vgioAwH5Unul4qP-tFdKxBLmW3KW4s-VC2VzFpDe5Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">متأسفانه من توی چنل نمی‌تونم به دلایل واضح چیزی بنویسم. توی این گزارش آنتروپیک، کلمه Iran رو سرچ کنید https://www.anthropic.com/threat-intelligence-report-september-2026</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/MatinSenPaii/5222" target="_blank">📅 16:40 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5221">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">متأسفانه من توی چنل نمی‌تونم به دلایل واضح چیزی بنویسم. توی این گزارش آنتروپیک، کلمه Iran رو سرچ کنید
https://www.anthropic.com/threat-intelligence-report-september-2026</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/MatinSenPaii/5221" target="_blank">📅 14:26 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5220">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/c2915137b6.mp4?token=iMLyhDTCO7E8jf7e8fXrYMZvMsx6bbs5UUwbzhRmGb8ddIDzgVb1_HMJoJ9hy1jrdzzPyk7m8HWHNAlhOoxyoTTWBSIsNTFD-ILQMODdfpWPdPaCR1WT0FHDU-3OLFskgbhuAY7cEvp5T4HYSkpV8B8cgxStZLwZPybsY7QPq2JeFaANDU0SGevfgcvJUH0aRsf8dKEx1gcLnPMXzznJFNUb1Ny-Shon6K0xTXgEF1AYL3Kmz-vFdOdfnfk7QkX6Dx1L7H3-Gx3nrpooMJFFagkEfzGKrgQ7qwWzBoNlMnAGOjogtNVoq9kV5rxXnjVrQXbXdf-yO-ux12eYDD_HsQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/c2915137b6.mp4?token=iMLyhDTCO7E8jf7e8fXrYMZvMsx6bbs5UUwbzhRmGb8ddIDzgVb1_HMJoJ9hy1jrdzzPyk7m8HWHNAlhOoxyoTTWBSIsNTFD-ILQMODdfpWPdPaCR1WT0FHDU-3OLFskgbhuAY7cEvp5T4HYSkpV8B8cgxStZLwZPybsY7QPq2JeFaANDU0SGevfgcvJUH0aRsf8dKEx1gcLnPMXzznJFNUb1Ny-Shon6K0xTXgEF1AYL3Kmz-vFdOdfnfk7QkX6Dx1L7H3-Gx3nrpooMJFFagkEfzGKrgQ7qwWzBoNlMnAGOjogtNVoq9kV5rxXnjVrQXbXdf-yO-ux12eYDD_HsQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ایونت رونمایی از آیفون 18 توی قم
💀
💀
💀
بدون شرح</div>
<div class="tg-footer">👁️ 28.9K · <a href="https://t.me/MatinSenPaii/5220" target="_blank">📅 13:16 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5219">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/DPTQNZZNPQzEJcmi9Vl8Phb487nM4qVW3Qxx0zAWmOEZfZUD7lisEOVRDYGxthjSuO6-AyArI3ySpyZNyDcDHXfAyqR9jbxrLxWTavrfaxcDZ60pZSWAe0etLuhXqeYz5ik8yjnTUjfFlNfrPJwsL_SvbgqoBIAfWaZGB19DBxyQHny3XCbNCosIHHjyLh29CorBz141bHCIckZdZemhCHZB0dkn7IFqkkE_y12DNYhCg-K8DtQCJTRRSxtKSzNrBdcSCN2aUPpW6nHb2qvfaYYNwk6VHJT2_dakFTmyvZ6Yq1fmUDSAZF8163YqbwBQFrMlMHNgnQAX3JmAZNjotQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">می‌تونید فید خودتون رو هم Tune کنید
که مثلا از فلان موضوع دوست دارم بهم مطلب نشون بدی،
یا از فلان موضوع دوست ندارم بهم چیزی نشون بدی</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/MatinSenPaii/5219" target="_blank">📅 12:50 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5217">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/mwmm6D6ciuZn3sBG5-pNkzGKxany_HW9vfXByk_0FME8Nn-LzztCw9SV8qS9w9s9RD1t36kPIPm-rrD4xRiUKOfyqusL-dxafUQmuWP0ZnVlkBoFe4-eoPV6-OJBxe3Bd8HrGbaMxCIpnrk2buBNx3fwIWtKjZLCf9Mj7Xx77oRTs8z5uhfEFJ3XArMHWljXkO_FCVfgLc-qhu11h2IxeXD2LzANBc6eKgYdSBvYPnIqryq86WXR4p2Yodl0b9GXwQV3z9ddpxYkARWc4-7gy1BljKWbSFkjkCv2Y068lw5FWdX2u2hT9wSqUnMn8xW1shnZAL2OV8SBmjE3xlwz2Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/GqIxy06f6XD3NNyHlY1GnhJzqF9Vi_eNDZi7ko1xpOjmNsflv_ZykafFG0gyBqurI1hvoYv_W3WiallD5CENHQQ3I5PQyCllLKhSehhJDbpVynQODWjtJHJmDnpilkYuMp2p52EXWvqaevEC0UGAecaWIMDcKW8_eSwHmFyy2qMyrY6mhFDtNNOA9Gwy_XXonsSz-SWtqSbwU87EJ_uvJ6wQmLvMJ1MW8lksvdahtEo_ABjioPpJ0XNNvZna1BHP2A3eIF8kyV482sUJ4e5yXEKQogYJkF8G61rHGTV9lJ0HiYoE8jYU6TovxbkzbjAycAEvPAHwqQYhj8hokaYnQA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">من نصبش کردم. باحاله و تمام اپ‌های گوگلم رو کانکت کرد. چند ساعت بعد واسم می‌چینه و بهتون نشون میدم</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/MatinSenPaii/5217" target="_blank">📅 12:45 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5215">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromهوش مصنوعی | محمد زمانی</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/o5Z9CaOOD9ihLYW7xS25Ke-kDw54epqT-hmpcQqrgodVNqAgUhQreo6MMC5LHwtkKROnOnJZBMwDJYqOg9Brl2b7_Bwkh7_paWmSU2C6NoQvqTPmYYE1BGGswIyMN2cEFoY8x8DZmBlKG7xEBDMjIYyoYAn8rHsoLGnCTYelMANr7F16wThjXWyKGPu-3kEB7qnpuuITRdWV3N6P8aFx-4so1aiAJISk_LZBi48GzGVT2AmOMzZNdvscSkLXAyQdtuKU_elk-EinNAAVtYydiZl2164bHNz-S5YKzEqJPX4hXPf4BrW38oW1_31mn04OWeLB4dTYPGZj25IZjLXjRw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/u8TyxESgo55ATwosPOnEkdHm3-E-YRMgQiiiEUS4_95gLYIJUJd_ukql4n3nOjKCOBDLVqf7dqkR2UDcEsmGtDSQ3hyl2RRANriQtCcoQfNhPmRQtFnouqH7JG4rSI2XaGZ2f5sWYDSCo-vWosvJK5S_Zchmi_ubKyo6d4kfVnGD4_ZovFMwl2msWKwgach7IJ9YOObR_YcBquBE4RrW5Cqy_AE_6Pv5wcNM16n6zth7fdjYOIHMJq2e3Z1HhkaOZXL3UEddsMkwkTrai2vHW96lJjEpyCed9INvic613bZsvk2zq_KwhMdBw9me4QlgKwE5V05BFlZx8Sxtvboimw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/MatinSenPaii/5215" target="_blank">📅 12:44 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5214">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">اوپن دیزاین یه بنچمارک از Deepseek V4.1 Flash منتشر کرده که اگر نزدیک به واقعیت هم باشه فکر کنم آمریکا به زودی چین رو بمبارون کنه
😂</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/MatinSenPaii/5214" target="_blank">📅 12:26 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5213">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/rn9w3xXIGLBUPW09VHc_54QFNcGNpQ0cUp7cfgCFVK92EGGoMlsfjU82NagBFnkB8jaI0c-bp9uRf8-M40UNwG6ZKoWtMMY1TZCtGdhrIIqtgbJC_eG-RQXEie7LqhNRgQpWlmJTZfLZeHn93eA94xn14zDA36r8j8vCIucX3qtI8QZdvLu_-MnR7u0xhc4QFPC6dm0pwKeNAN6XoZZlt-tC-q9TILaplUdEUERgbKQ2VgvOENc62x1sRIK6oFuWvzyjMOoOvOoaEHuoTdH-qO0J7f0MSor0zCsvKSkIat7RA4MBxCY4J8_8Hxi2r6V9eGQsHjxKoDtvNwrZQlyYew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اوپن دیزاین یه بنچمارک از Deepseek V4.1 Flash منتشر کرده که اگر نزدیک به واقعیت هم باشه فکر کنم آمریکا به زودی چین رو بمبارون کنه
😂</div>
<div class="tg-footer">👁️ 34K · <a href="https://t.me/MatinSenPaii/5213" target="_blank">📅 09:02 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5212">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">توی این چهار روز کلی اتفاق افتاد. از معرفی GPT image 2.5 تا مدلهای جدید دیگه‌ای که معرفی شدن؛
اما چیزی که وقتی دیدمش برق از سرم پروند، حل معمای 90 ساله‌ی وجود و همواری سه‌بعدی ناویر استوکس توسط یه مدل قوی‌تر از Astra توی 88 ساعت بود که هنوز در حیرتم؛ چون خودم رشته‌ی تحصیلی دانشگاهیم علوم دریاییه.
ببینید معادلات واقعی ocean circulation معمولا ناویر استوکس خالصی که الان حل شده نیستن.
یعنی تفاوتی توی اصل حل معادلات شبیه‌سازی جریان پیش نمیاد.
حل این معادله بیشتر شبیه اینه که بعد از 90 سال، بالاخره قفل یه در رو باز کردیم و پشتش یه راهروی تازه‌ی پر از مسئله‌ی جدید پیدا کردیم و رفتیم لول بعد.
فردا راجبش بیشتر می‌نویسم.
خارق‌العادست</div>
<div class="tg-footer">👁️ 34.7K · <a href="https://t.me/MatinSenPaii/5212" target="_blank">📅 03:06 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5211">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">دوستان من حالم خوبه
میام به زودی</div>
<div class="tg-footer">👁️ 37.1K · <a href="https://t.me/MatinSenPaii/5211" target="_blank">📅 11:17 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5210">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-footer">👁️ 55.3K · <a href="https://t.me/MatinSenPaii/5210" target="_blank">📅 00:12 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5209">
<div class="tg-post-header">📌 پیام #76</div>
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
<div class="tg-footer">👁️ 54.1K · <a href="https://t.me/MatinSenPaii/5209" target="_blank">📅 23:40 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5208">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/G97sJAHKIVj9NugUzeNoU36k8RJQv1NRzuFClns_uuvVc-c9YWmgHIgkVZd00JROcj_Jj6m0G4tdOLjUqia80Ihg0w_GtqUggPSVd9OM6Viw-5DkAwJ7ndfTtWVhprY0KoRTdLDV2VIDlcuzzLXTuxUktWI7XPmoajWsGEjf82Kc4DV9JRQMUKGX6gRwxjSVDIeG70ligljMWTEoQSKL5LyCWYRajiXk4YxF7dUF2vMoMG5GtK7xDntE_XqL0Fsz5mWVp0npzWZ8yHTORv-Z4XBc9X556YYyjZm-WlCgAHelZ33CEZ-J0JeylJS8Yf5cQZH_ecQnLaS8VX90xNTKXQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جواب من به هرکسی که فنی نیست و سختشه که پنل بسازه توی کلودفلر و... :
Defyx
👍
https://play.google.com/store/apps/details?id=de.unboundtech.defyxvpn
البته WhiteVPN هم از لحاظ راحتی و امکانات برابری می‌کنه و می‌تونید ساب خودتونو هم وارد کنید اما برای کسایی که یه کوچولو فنی‌تر باشن مثل جمعی که اینجا هستیم خوبه.
دیفیکس در حد سایفون راحته، با این فرق که واقعا وصل میشه
😂</div>
<div class="tg-footer">👁️ 52K · <a href="https://t.me/MatinSenPaii/5208" target="_blank">📅 22:56 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5207">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">گویا گوگل Mantis رو اوپن‌سورس کرده
فریم‌ورک ایجنتی مانتیس این شکلیه که کل چرخه‌ی آسیب‌پذیری رو خودکار می‌کنه. از پیدا کردن و تأیید، تا بازتولید و فیکس. فرقش با اسکنرهای معمولی اینه که با ایجنت‌های منتقد و بازبین و... و اجرای سندباکسی، گزارش‌های الکی و باگ‌های توهمی رو فیلتر می‌کنه و مصرف توکن رو هم تا ۸۵٪ پایین میاره. پیشنهاد می‌کنم بک‌اندکارا و امنیت‌کارا یه نگاهی بهش داشته باشن:
https://cloud.google.com/blog/products/identity-security/getting-started-with-the-mantis-harness-to-find-and-fix-bugs
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 47.1K · <a href="https://t.me/MatinSenPaii/5207" target="_blank">📅 21:31 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5206">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">چند تا کوهنورد تو آمریکا با جمنای برنامه چیدن و جمینای بهشون گفته خیلی کمتر آب و غذا ببرن. و به خاطر این مشورت اشتباه با جمنای گیر افتادن و آخرش گروه نجات مجبور شده بره دنبالشون. عاقبت سپردن عقل سلیم دست AI
خلاصه برای جونتون هیچ‌وقت فقط به چت‌بات اعتماد نکنید
منبع
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 49.5K · <a href="https://t.me/MatinSenPaii/5206" target="_blank">📅 10:05 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5205">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/NZKzOyQpXv-K-fgQRybaeXTZoeoLPESV6jsHo4MyHTpteglScj0-5EizPhm7IGTO-pWLWBeYzVSQOSqQxmFjIs0ProgOZYmsUax1LIepLIHl39qazVpdFRdsbYW9Aa1hGLqQ9ABhHDBHT--Tcmbli_0C1upCtDK4l0te4XXu1hi_KIrFSCk_RdXg1miNDanaLIDLj7VGfpFc26EgTbFscIafft2xp6EY1rBZWEN08gNvXPuZn-vGl7BBJD6IhOJByRGPE53Iv4pdSn_tlNpUpDHHY49V4AuYAneo3TV2ENdMrUX5FPF08T3rofyf_NVZo-dcT1EfxTOeJPfcgWXxhQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تست
Pelican comparison
روی مدل‌های GPT به علاوه‌ی هزینه‌شون.
هزینه‌ی Astra تقریبا پنجاه برابر Lunaست</div>
<div class="tg-footer">👁️ 49.8K · <a href="https://t.me/MatinSenPaii/5205" target="_blank">📅 00:41 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5204">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/48fb2366c8.mp4?token=hqiukEI7VlUU_458JJixT8IEkJ9Beq1QplMN3AejqBxR1ddN5IoIl31Uxiww2hbvqSncd2LYJKLzzUaYgkoBg6rJ0vvPBnZPQc7J2Rg8VHkUV2X7RSRUsaDBWpjMJi8NiT7JovlLpdTbNB0Aec7MJs9LjCmnKbhMuuBgh7bOd7qs6EhT46bZ72rWIPeH9DAF8MfbceyYUNdEoA1184gW7ZvD0DWLHMhBD81yx_AWnz2RKZ_aiP561G26nHTZu92Hu7J3s-eTyb1_vHXr5fUP6wehhboDVpPU1rdTomgqkRdqzYhYpzi_QhtoXGtuLRci1RQZWosBPckgPZH4Y-VMTg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/48fb2366c8.mp4?token=hqiukEI7VlUU_458JJixT8IEkJ9Beq1QplMN3AejqBxR1ddN5IoIl31Uxiww2hbvqSncd2LYJKLzzUaYgkoBg6rJ0vvPBnZPQc7J2Rg8VHkUV2X7RSRUsaDBWpjMJi8NiT7JovlLpdTbNB0Aec7MJs9LjCmnKbhMuuBgh7bOd7qs6EhT46bZ72rWIPeH9DAF8MfbceyYUNdEoA1184gW7ZvD0DWLHMhBD81yx_AWnz2RKZ_aiP561G26nHTZu92Hu7J3s-eTyb1_vHXr5fUP6wehhboDVpPU1rdTomgqkRdqzYhYpzi_QhtoXGtuLRci1RQZWosBPckgPZH4Y-VMTg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وزیر نیرو : خبر خوش برای ملت شریف ایران، قطعی های برق برنامه ریزی شده برق تموم شد.</div>
<div class="tg-footer">👁️ 44.4K · <a href="https://t.me/MatinSenPaii/5204" target="_blank">📅 21:09 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5203">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/mgpt4d6-Ioq1kxYe7efZk-TuTg13yrxZ10H9LaX84-ZsIT-zSrEouywPo0glYeFJolz_zFd2FoeKfcX0oo7_DhfpYeKV1NytCQYF70pzh-3D9b5XbiNTzb-noNdYEVS7uysikt8bN1-hxvIbHnoh8njWUZpTbsxqufHd2j89IbicYnbf6iMjJw0CGxmSXFByddyDpMoL0eQKbWCE3HQJgeacXpnPhDdT0qClleEnqKNL_-tjUHTQdCyvizRhQcmCzGDOWtfOVW-vQcQrNmmCvX-cgcKN_jdArTnFawEDrCwNhvaHWpAt_ZbOOROV8Dx4Rx0n054nvla2nbnBWsnhiw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">از اونجایی که کلاد و جی‌پی‌تی مدل جدید دادن... به زودی باید شاهد دستاوردهای برادران چینی باشیم</div>
<div class="tg-footer">👁️ 45.8K · <a href="https://t.me/MatinSenPaii/5203" target="_blank">📅 20:49 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5202">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">آموزش خرید اشتراک Claude Pro با ویزاکارت شخصی و ایمیل خودتون  من امروز تجربه‌ام رو از خرید اشتراک کلاد پرو می‌خوام باهاتون در میون بذارم، که چطوری خیلی راحت و بدون نگرانی بتونید با پرداخت کریپتو روی ایمیل خودتون فعالش کنید. یکی از دوستانم دو ماهه و خودم هم…</div>
<div class="tg-footer">👁️ 42.8K · <a href="https://t.me/MatinSenPaii/5202" target="_blank">📅 19:28 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5201">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/UjOWNcXibpBJCfqI8HF36fiQjXZW6e0ZZGtLRJFeYQMXU4ycZEYKHDhANxFgqz8_e1jvnTUfNHT3vyXXYG5qQnyp90saxjYybArftkTlajAf6lBGR1nXTTm8l-oJ423w_4P04y-0a07CpS48RaF_R3Ef4ljypHcLfujNxD7t0-TJZgYpZB6bD0HKy04M0KhmHEj8o_1DS51vD_3sgqMIY1Vyt94KzvqRWZS51627yfRtVr383u8sWeIUJeMpP8n5pPbhtZCqsWrwtSlULAvynAnbcU9Nac63pkO3jyZGG1OkkfhqOsdAvbBcYc9_coWy9oRyS0_18ERyyBQm-z5E1Q.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 45.2K · <a href="https://t.me/MatinSenPaii/5201" target="_blank">📅 19:22 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5200">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromPedi | پِدی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pBTSekYmfiFWHnloFllJXhvDOljUOipGThKjMowYceuX8Oep77ibuWqR7mkElAed7fnd2jIbSXLOvVX2SZEBCoJPW2kEYioOCyRezQS29pQfFvVOh8ZeWJDgBjfzY8xIJt2CHe9HCkfEmlFPNfn_khyNvYgbEhMKbjJ4UIytSF2gRct7VaE9-V6XVw_XKtycX5Si-qmylSA75cH0PI0x7_P66gEkMxstCkUnNebNrzAAmuBCmGsizL23XuyL0XbVkOzP-8V83vAAoRijhQF3lAKrifQC5A1s7BkLQe2YvarcMdV2a8Y2gGFOShJRzowVF5i8YJFovSaix0PSlWUScg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 37.8K · <a href="https://t.me/MatinSenPaii/5200" target="_blank">📅 18:52 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5199">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">تهران
💵
228,‌000</div>
<div class="tg-footer">👁️ 39.5K · <a href="https://t.me/MatinSenPaii/5199" target="_blank">📅 16:18 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5198">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">البته اگر می‌خواید برنامه‌نویس بشید توی ایران اول از همه بهتون تبریک میگم که با دلار ۲۲۵ هزار تومنی و بدبختی اینترنت و نامعلوم بودن آیندمون و جنگ و اقتصاد و فلاکت و بدبختی تصمیم گرفتید توی این حوزه قدم بذارید و شجاعت به خرج بدید</div>
<div class="tg-footer">👁️ 42.4K · <a href="https://t.me/MatinSenPaii/5198" target="_blank">📅 16:16 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5197">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">سلام، من پدی (پدرام) هستم!  همون‌طور که احتمالاً حدس زدید، برنامه‌نویسم و این اولین ویدیوی این کاناله.  اینجا قراره درباره‌ی دنیای نرم‌افزار، برنامه‌نویسی و ابزارهای مختلف، مخصوصاً هوش مصنوعی، حرف بزنیم؛ اما با یه تفاوت مهم:  قرار نیست با اومدن AI، هنر برنامه‌نویسی،…</div>
<div class="tg-footer">👁️ 43.1K · <a href="https://t.me/MatinSenPaii/5197" target="_blank">📅 15:58 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5196">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromPedi | پِدی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mygMb6eCAxPXdJdQUi5GLnOCKdAHJZSeI9cg-mls5Fd17l_EwUSzAT7zRzMleM6aKBX4BAP68RCQwpJL0V236bZ9MvHFoJHkvI_MiQdnHYvH9dt6d3mZGjFGmkGkXrHxAEXv-qMXqKqX5AgKOJJqWTZUwK2LU-HjFNJAOfbYbl7cjfxuvzUHkIdLfKCV2zdSdD5Phj-LFfPNL5kFCRLxYRRXh0WCh9p_qGyAF-4G47mFmH-GH6EvWH0HxQ7GmnOYKxwpCx6KyhKwwP3GVUqO2iKnch-JI9LMYAf_yRaBMYaao10dXaA9tXbpbgDtpGqlKCwVwBqUGBhfqUv1fOZlcQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سلام، من پدی (پدرام) هستم!
همون‌طور که احتمالاً حدس زدید، برنامه‌نویسم و این اولین ویدیوی این کاناله.
اینجا قراره درباره‌ی دنیای نرم‌افزار، برنامه‌نویسی و ابزارهای مختلف، مخصوصاً هوش مصنوعی، حرف بزنیم؛ اما با یه تفاوت مهم:
قرار نیست با اومدن AI، هنر برنامه‌نویسی، مهندسی نرم‌افزار و طراحی درست سیستم‌ها رو فراموش کنیم.
توی این ویدیوی کوتاه، خیلی کلی درباره‌ی دیدگاهم، دلیل ساختن این کانال و مسیری که قراره با هم جلو بریم صحبت می‌کنم.
📹
تماشا ویدیو از یوتیوب</div>
<div class="tg-footer">👁️ 38.2K · <a href="https://t.me/MatinSenPaii/5196" target="_blank">📅 15:54 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5194">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">این 25 دلار توی حسابتون می‌مونه دوستان. یه سریا فکر کردن 25 دلار از سر راه آوردیم بدیم دست هتزنر
شما اگر که استفاده‌ت میشه طبیعتا پولش رو میدی. مثلا من عموما قدیم از هتزنر برای استقرار ربات‌های تلگرامم استفاده می‌کردم
هزینه‌اش نسبت به سایت‌های دیگه خیلی اوکی تره طبیعتا نسبت به منابعی که میده.</div>
<div class="tg-footer">👁️ 38.5K · <a href="https://t.me/MatinSenPaii/5194" target="_blank">📅 03:05 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5193">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/bK47Ua0CD5jsGO5tQLR9FPqK1kuq3I9t7ItG1e-pts92mNC3RHiA1N9NMp-sOHg8_VFeZquvBI3uTpOPrUfv2i7nScxexxn3ZxK1hRx5-5-l-X1fe3jwdOApXVt2VwFrbGhqBFMma4hK9PuLALQ7AK6KOidKBO1lWAUs0I-aJ3lZ0wPuWS_zdn3uFIGCGQqdP734cTKsslxlEq9fFsgmfPdpdkBWGK7pENqCzqaacVIVwBu5kkwX02ylqy45AEmSmlP6LtIFil0l2NcEsRwagomqILmYrjZPeiM10HQ2rCcoAiIont1t9h3zYyLqZMnFjTqfBuyQlC3wpwk01B5_Ew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">لیمیتم رو پنج روز پیش تموم کردم. از کجا می‌فهمیدم می‌خوای مدل جدید بدی خب
🫪
(مدل Astra الان برای کاربرای پلاس بیست دلاری هم در دسترسه)</div>
<div class="tg-footer">👁️ 39.1K · <a href="https://t.me/MatinSenPaii/5193" target="_blank">📅 03:01 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5192">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/jCjvfnjQSE2ddbNTgroNP0Z9XY48MyddoD9lmbLQDQMr570g3io062322E7KiQqYX5JQI-5Wj2myiuBFEw91SfYG43Gc3tnPEjGp7zfBNhAp02NYZ-TH-cWIaQb5u6cXMFCp94e41gsurKHe87-XGM2iTfLCRBsRZ1qKgIT6HsbMJq0sG3xmeVpyw7frAPzVVoAvwtRG9cckXDZ92U722VlCOi4wmgyseqJu3KyYW7urmVHD7OqrZR73ZiI8h4aykv3Sklp5dPgmARB1VCGcy5aKB_akC87iX8p0FmZJhmG0V3ITsX2IcFnvMSn6miUJU8uOiTvvoFJzLGHEngV3iw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این سایت Nara خودش از اوپن کد api میگرفته
😂
😂
😂
😂
عاقبت وایب کد کردن سایت Api هوش مصنوعی</div>
<div class="tg-footer">👁️ 35.7K · <a href="https://t.me/MatinSenPaii/5192" target="_blank">📅 01:30 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5191">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/pInWW0h5CobpAS-AcA2kqI1PBoVqb-PtsJloAhcLf5AlEpjTN6DwWMuPHv04SwXufGmufyQ63f27HOpuEdg0_2DsBROO6h1Ao36nLhJ6F0E6ob8N0RwKj_77ZKm8wIM1XQAlnv4-pHZzeWbmK2hAKO1_izY1UfDfq3U_oVk7pY4oXTCWIvhgDXPHNHaykdZ6KVRonKK-cjA8YEVQu0cZxmKkEq8xcWCGstciyVlc7gI61x8mOaDl5SeeojvCqP6Vc0f91TR-OpqwqKYOtkPLwH7J9Hwn8wr-JUAQG9jZ7URqHsX_ccsxFMlMzZkSLUzRvDJmdJPgIFDF1g95ZRfmag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این سایت Nara خودش از اوپن کد api میگرفته
😂
😂
😂
😂
عاقبت وایب کد کردن سایت Api هوش مصنوعی</div>
<div class="tg-footer">👁️ 33.1K · <a href="https://t.me/MatinSenPaii/5191" target="_blank">📅 01:22 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5190">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">چقدر غمناک..</div>
<div class="tg-footer">👁️ 33.1K · <a href="https://t.me/MatinSenPaii/5190" target="_blank">📅 00:43 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5189">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">Kavinsky – Nightcall</div>
<div class="tg-footer">👁️ 34.7K · <a href="https://t.me/MatinSenPaii/5189" target="_blank">📅 23:34 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5188">
<div class="tg-post-header">📌 پیام #56</div>
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
<div class="tg-footer">👁️ 35.4K · <a href="https://t.me/MatinSenPaii/5188" target="_blank">📅 23:13 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5185">
<div class="tg-post-header">📌 پیام #55</div>
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
<div class="tg-footer">👁️ 34.8K · <a href="https://t.me/MatinSenPaii/5185" target="_blank">📅 22:19 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5184">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/EJfhpQZ4RgVtw-tQleAHP-3jP5Ei6xNgJMGWHCUSkeLKy2-9nIGLg8BS_quGSt2rEXHY7FehBS8-OKbxY07kAlq7QS7m6-D0pf4DJoIth_fU-pQF7dRYejCO69dq-XXoiR3ng_IuhVuzMgreGtkUdbk-e7pIV4tthi-MIqjafoLGHm2q74Hzt1qTSbZ_sjoqxNCBVmNYR-RGwTuB-3ZVaFN3k1ASgIosY3iQb0aj8Tc-6JrkptKUT0708o2SyaFYJPW3EfUPz9g-RZTkOrWfY-Lxzz_SmvvGaSQzVSoLxwJhnwzRM78PBYTmUiyyMt2oUKb9_mR106BomJvmFR8AnA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قیمت و مشخصات؟</div>
<div class="tg-footer">👁️ 28.7K · <a href="https://t.me/MatinSenPaii/5184" target="_blank">📅 21:28 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5183">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">یه چیز بهتر از OVH پیدا کردم:) بذارید تست کنم ببینم اگه بن نکرد من رو، فردا معرفیش میکنم</div>
<div class="tg-footer">👁️ 30.6K · <a href="https://t.me/MatinSenPaii/5183" target="_blank">📅 20:58 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5179">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/c84957dbe3.mp4?token=PHzu0q0qP3QnvmP0HvnXFVRh3x28_PHDX51Z3UZBbNZMMoQ7hrSAWCqMwISpagVV-24lhG1xtAYZCbgbkE2ExRrlTXgvamJl5dnM-MsC9BbAbyXf6AE2HE5GNgAZE7qggt7rCq0sp3ZzsanrpxyGBUt2ZptTqXDsOBpQ4GaIhYehncngnbKV6cpVGiibl5wflZR0SmbOb5kZP0My33zqFEWjXgjDuxFQOVxt0SmlBxsxOi4nBzI1SX7x-nrjjuZEjqT1oX8hfs-hHrhZsr4C-4NoGijCj9uT-p7K6byVbkWAdcR6aGpMcgnr8wZHiRkEClvVvueldw7k04-Q0M7qUQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/c84957dbe3.mp4?token=PHzu0q0qP3QnvmP0HvnXFVRh3x28_PHDX51Z3UZBbNZMMoQ7hrSAWCqMwISpagVV-24lhG1xtAYZCbgbkE2ExRrlTXgvamJl5dnM-MsC9BbAbyXf6AE2HE5GNgAZE7qggt7rCq0sp3ZzsanrpxyGBUt2ZptTqXDsOBpQ4GaIhYehncngnbKV6cpVGiibl5wflZR0SmbOb5kZP0My33zqFEWjXgjDuxFQOVxt0SmlBxsxOi4nBzI1SX7x-nrjjuZEjqT1oX8hfs-hHrhZsr4C-4NoGijCj9uT-p7K6byVbkWAdcR6aGpMcgnr8wZHiRkEClvVvueldw7k04-Q0M7qUQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 34.3K · <a href="https://t.me/MatinSenPaii/5179" target="_blank">📅 20:43 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5178">
<div class="tg-post-header">📌 پیام #51</div>
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
<div class="tg-footer">👁️ 34.4K · <a href="https://t.me/MatinSenPaii/5178" target="_blank">📅 16:09 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5176">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/HYH7Vg7XMZsczIk5Qb-5uR3Dbq8ps4yo73-NSFli7CXSP8uZfEd6wNUE5tq34kS_1CakZl79ByrP-1psFlh4-fj2GCv2dwlvI8TE4OcLlDrx8BNcvo6gdOvqu4uC61jKaUwmIUP41U0FmuVE2Q3YEf6pFBUFdi_8CMf14MQdqLzmAWvrRluZPkVR3cOvQskrrZxIZ0hjCKIEY_RtNcGjKSeqfGSphLJ0xKbCrkG2XfidPym5RyK0nKEAx_qWsp1gLIp7TPZ93lunDM_g9s2uzNpcG7PuEZ8Xik2Nmie6ccWjFoA1ybH8PvCtBZsCyPuChBQydYWJvsNejKWUM407Cg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تلگرام شما هم شده پر این تبلیغات کریپتویی و ترید یهو؟
حس میکنم سیستم نمایش تبلیغات تلگرام عوض شده چون 24/7 هر کانالی باز میکنم تبلیغ روشه. قبلا این شکلی نبود
الان حتی روی این کانال کوچولوی من
@MatinsDungeon
هم داره نشون میده</div>
<div class="tg-footer">👁️ 34.3K · <a href="https://t.me/MatinSenPaii/5176" target="_blank">📅 14:04 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5175">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">دوستم دیشب بهم پیام داد و گفت متین، gpt 6 اومده
گفتم بذار بخوابیم فردا بنچمارکاش در بیاد
و الان باید بگم Wow!!</div>
<div class="tg-footer">👁️ 35.3K · <a href="https://t.me/MatinSenPaii/5175" target="_blank">📅 12:45 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5174">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">متاسفانه نشد
😫
فعلا بریم کردیت رایگان گوگل و آمازون رو استفاده کنیم ببینم چه میشه هرچند هنوز می‌تونید از سایت‌هایی مثل Aeza و Yottasrc و... خرید کنیدا صرفا OVH رو دوست داشتم بگیرم که نشد باز، اگر موفق شدم بهتون خبر میدم</div>
<div class="tg-footer">👁️ 37.5K · <a href="https://t.me/MatinSenPaii/5174" target="_blank">📅 01:44 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5173">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/J4ODl03tJ0OfMy3uDqPiguXrCuLj7_I8JcFsRo553-8EYYKCxbDAyC43Ly7vCUytv1ru6eDEna_Nj1Mz4dMTJTLTo6HvxB8M0_62_ZRh4BG6asa9loUQR5XdgLuUvI3muQqpHbEdGc943L5tQ-eUyWzUos34-qznim9W-FZI_CjdjVrNTikZN8OtA6xZmHlEhawQptynKe-fb3n_mQw8k1L6vKqNx0v8CBg_E3UfPl6Rm5dAY1crwYMG2F0JWMg4jmz-1lTIkqQC20jqUg0c79G2uf4flq8ovJgpiLcs9aEQWr3MaL634tAi31LXnC24RjE7sP9MSAoi3hodYWeQSw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سرورهای OVH واقعا به صرفه‌ان از لحاظ قیمتی و اینکه ترافیکش نامحدوده. 2 هسته CPU و 4 گیگ رم، 4.5 دلار. با دلار 220 تومنی میشه 990 هزار تومن اونوقت سایت‌های هم‌ وطنم پاره تنم دارن سرور 1 هسته و 1 گیگ رم میدن +1 میلیون تومن://  سایتش گویا یه مقداری روی آیپی حساسه…</div>
<div class="tg-footer">👁️ 37.8K · <a href="https://t.me/MatinSenPaii/5173" target="_blank">📅 00:02 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5172">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/GVOp716oe1AtYmWS_u2VbjWLgcK_T7XvsCt4G3GNhkQzjk0WEEYwzP1cxIcVMdoqEA1HuWtFQ3hkl_X8IcSqZSRgs4o9zIY3KYv5RopvMXMFY4gunVKlbaSYJzFMFDGzw5hAL8SrZWxsKbUmhqxB9jhk2S073gjmwz1wkld0mnp5mkmODimhMsb8To3RMGi-fxfJYl0hmrTS6qMLIYoTDPN3kSfxEfRdUH2feCEbqiiYgA05pLbbxqummn6hRmqg75NujreNmMml9NLShG6dIn3e9RTubmmhfTaN0E6Rp1HNNHglEcSxAKB4cMZP990PaIFER6OawdqREnZ6nDfSdQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سرورهای OVH واقعا به صرفه‌ان از لحاظ قیمتی و اینکه ترافیکش نامحدوده. 2 هسته CPU و 4 گیگ رم، 4.5 دلار. با دلار 220 تومنی میشه 990 هزار تومن اونوقت سایت‌های هم‌ وطنم پاره تنم دارن سرور 1 هسته و 1 گیگ رم میدن +1 میلیون تومن://  سایتش گویا یه مقداری روی آیپی حساسه…</div>
<div class="tg-footer">👁️ 34.6K · <a href="https://t.me/MatinSenPaii/5172" target="_blank">📅 23:48 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5171">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/NNTxiGvdbojtTyxrlPsuxJf0eRqZWJN6O19TqEPw0Qlj3kiXHZEXzdEfWeOvUgAAv_xW-BkERiB_YcpcURGDx3eUge_iSqOIE7i_M6_GAq_gKl6q3Mrh0cJjJkvx3-Qz-NCm5YGK27OhYAeibwPEvJecMsXejMiJmgSwS-nvW3YsxLDGDMjAc70QpXwXw7o5tghhB4SlTsf0CBCjGnpHT7OB1qevKeJGOGx-4GIo039L2xI_ARYrTEEYphT_m7oqX7xzSy2NEKp0fN-HKBZBUhmDi8mNRy5PFz9CKdeZY37RdbuKlcvomzrA0bKgtdLE2JXu-dOSYXQW-m9f-cE1gA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سرورهای OVH واقعا به صرفه‌ان از لحاظ قیمتی و اینکه ترافیکش نامحدوده.
2 هسته CPU و 4 گیگ رم، 4.5 دلار. با دلار 220 تومنی میشه 990 هزار تومن
اونوقت سایت‌های هم‌ وطنم پاره تنم دارن سرور 1 هسته و 1 گیگ رم میدن +1 میلیون تومن://
سایتش گویا یه مقداری روی آیپی حساسه
من میرم تلاش کنم ببینم میتونم ازش خرید کنم با Mpay یا نه</div>
<div class="tg-footer">👁️ 34.5K · <a href="https://t.me/MatinSenPaii/5171" target="_blank">📅 23:45 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5170">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/U1UGRi_qfQux102UGp9MqrFX3mbv-A0z0z2rrqe2ynEKJIV2MJ7e6miBopaJAHbxkO9OE99SKAbZJuwuseY4S91LG64LdyXdgho_4j7hpcFI-2S1vlipWPmtMGsRmGGQaeFrZewmvMiNlVDHcwDKusqN-DET9DqSQjG3SLukfeDPrPei3HGe1obid3Xs0XwwJcjb5cruEZi19eWW9HCvPvQTOioxD2P_1gZVmH7r1coxekriem0DOYspRwQI3xzEONnT27o1PeNynTVGma6ycH0vOO4VWTUaPTb63tXEAgHWrbirix5sqxNw9NiNMAGwlBadgBnhvWY6RSJGgFAGwQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دارم با همین Nara و مدل Muse Spark 1.3 یه سری تسک سرچ متوسط انجام میدم(سه تا ساب‌ایجنت ران کرده که قیمت اجاره و... رو توی سه تا شهر مختلف برام در بیاره و اونایی که ارزش بیشتری دارن رو از دیوار و شیپور و اینها لیست کنه) با هرمس، چیزی که چشممو گرفته سرعتشه که…</div>
<div class="tg-footer">👁️ 32.3K · <a href="https://t.me/MatinSenPaii/5170" target="_blank">📅 23:07 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5169">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/oErnLYoAutcfrqH1mXEa3eUY6uno9So_8i5weeC_jFrIW3PdNrdAB88ugKucsY90LqgNjJYpXuyL9U3VZJkYKSDlQWOOHJbl-IaYIMibfAfgb4zEt2vufrAc_Pu_Y9ZpDrchy2T8qVwuQbBGMoq-dVmoX0eWGRPBka5tLcy_dY2yjoKSvwLEAjUgg1_cVhMN8DkteJKwX18ws-OyYTEnQVO7o7ldrtRIiG2qyuONmTTzHjFQGypCnEofNrDtXr8Di2NYLA6xVhy4o_Qj14pbCV8ju68dBnQuHgMy1MWr--nUqG1U0ZyRv1gy9h2ZP25d9GD5vyg0pnlgmG7sNM3sUQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جمنای هم تخفیف زده روی پلن‌هاش
می‌تونید خریداری کنید ولی حتما از اندروید + این متد که اینجا توضیح دادم:
https://t.me/MatinSenPaii/5092
استفاده کنید سر Google Pay</div>
<div class="tg-footer">👁️ 31.4K · <a href="https://t.me/MatinSenPaii/5169" target="_blank">📅 22:41 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5168">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/iebvdcQ6iOo-dA6wALceA405zADmcR56rfwUA0E-TVBLR9meHBR0ion0f74VqGDmYjWzShjCfLaXog8TwAusDTqz6yypUnMpzaX0VrVG7cOPQdLYrALUM0AKsFSQ-T8mVxn03dHXyctpfP4qXpk-cJPQE1dxsg3LNC1L02abH4LPsB76-OVU0RVj0BlTThMaioZwK5y8fezoH8vpv4TwfTd_iBxpPGKFsBqGX_evQjjH0Oi3v-O4pY3lW73JzeKxQTIxuatrsq_bTBcct7aqYqS4mMKmqY1lhYF4Vx-r6qNnyaX3N-pTJGDZSc0KSIl3T-ODGvt1VsBfWbvEp4icSQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دوستان با این سایت Nara که قبلا معرفی کرده بودم(https://t.me/MatinSenPaii/4061)، اگر که داخلش اکانت تلگرامتون رو وصل کنید به رباتش و توی کانالشون جوین بشید، می‌تونید نامحدود از مدل muse-spark-1.2-contributor-free متا استفاده کنید؛ بدون محدودیت ریجن و...  مینویسه…</div>
<div class="tg-footer">👁️ 29.6K · <a href="https://t.me/MatinSenPaii/5168" target="_blank">📅 22:01 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5164">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/ERZ0W0osPXHqpCPTnf7ZAMXnwALLR6YXfQJcnTLLydAR-IIT8f-78Ar8eKLc2S7nB8qt1P3gF_hik8XdHsW1YN50xXJ3vV5q3-jE9OW9bLGsBNAPgYoc1-_cjkYVyHg5cwC_7O1lMiBJV6DqNxAKxh-SoWdSjTP5TLWx3qNQIMDaCrlxPYWhErqiLDDtY8l4tlDaIGFtuDSBIMu3-wFB9s7rjXUQPDIVIFkywTlOhSFudsCPEARt4d1rEE0DBCDeRT3EaV13ROQ7PPsyHlsS9AwuyvZMntKnokUa1yWpTGalpVtIwW1wsGp3iaHaG25IB8ViajPlKKHPTduB-XavWw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/TDhkwpUcqPfXXgORRadoxOy0kIttCrP9PPjJa0vRnZX3C64NO2st6qDVVJXJSbRB4nO0k8F2y2qp6qXYmekUneJDz8n_BcL6pPZNoEfau8sQuLyrTo3TqT9Uag1B7GicJrFGuziF82t_cSGtURBW0URi-V2MD4uckwWBf8w0VK0v2jxWTHKEuOzuDUn8E6B6Q9lB0zZJgGpHCYvCx3fKHyS6Pd_XHd5iCWNgbGygiia3R42mKAo38T6ENj6rmjFDD5_B4FfpSskr5aIddWm1_Nlxh2NMF_uZF6uREKWYNfMjLMpvWYCYFpUn9iOyWtfJ1e7OvCWbwKwvrBjsu6E9qg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/r8yfBeTwgolLRsLimpuRsHYdppGJB96cGUA-2kHL9sDXxNMrec97Mt_zysRUNsZmhl_ZHxHJYE8OYMtXDIJfNjWl0v0kif5DnNFffvErVW4nuanrL-F0oByzQq0U4yftuet3a5r39BAjJ4xAk4mmrgwT1gv5ALHw-Kf81UKPMZLIbOQDS8ty2Ru7QJCSu8vkfu2PXYyv1T18gDSGQw8sWH738B841xT8tdyVLN3F_cC61gO8zr6h6kk0rhXkqgXbT3Paq6-XcowdKTNaIFE2Ql-PmtPUs9n-s0J1arVwZgM6y-rgHtBWHNqdQ6ALcpWuNkcy5hSHuIZULYE-odLlhg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/pYcm9fNWC1_XWUgWPwu_VfOzquOh_j1tm7HR9PyI_wb5nzgSg_BQ0KTTW_ijc1t1QmGZHFmtQuy6-r7oECintGPiz27YVwe0_hH9wTAxWXgvzuFU9veJV3GZHmgrYqxTE_d3UNAYSPiamqW0lpkS0M3h0PQmfE-A9BtFgYzFCN23btln0U2mmnG7L36xKP3jOxNCxr_u40i7j7ritwrPNSk8v2qF896wH3PmPtBYwF_GYKIyjG1lNkR-BHw5Dm3wHPz18zL-tR5kTLBHBOkAUi8MXiRydVOWM_LfmuHqYKW4wX3BDkdWzoV5MOA400sdrCKQgfcwUpctSKZKIAAqCQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">از سایت Nara Router که ریک معرفی کرد دارم استفاده می‌کنم برای ‌Hermes و چیز خیلی خوبیه! یه ربات خیلی کوچولو هم دارم می‌نویسم. دارم تمرکز می‌کنم روی این قضیه ببینم چطوری می‌تونم کارهای روزمره رو Automate کنم و چطوری میشه حداکثر بهره‌وری رو داشت از Hermes  خوبی…</div>
<div class="tg-footer">👁️ 32.8K · <a href="https://t.me/MatinSenPaii/5164" target="_blank">📅 21:43 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5163">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">نمیدونم چرا انقدر از مدل Kimi 3 خوشم میاد
زیاد هم فرصت نشده استفاده کنم توی تسک‌های سنگین
اما در نهایت برای کدنویسی، compatibility ای که مدلهای کلاد با خود هارنس claude code دارن رو هنوز توی هیچ ابزار دیگه‌ای تجربه نکردم</div>
<div class="tg-footer">👁️ 31.4K · <a href="https://t.me/MatinSenPaii/5163" target="_blank">📅 19:22 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5162">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/eELfmGo1OXCluRb6S7-jL7hdsys2DCYW0nym-2QjRTjnflOU89tNZx0cD07wVxBWpmidQARSE8Aw7mQYUcDtaFof-r8PpWNHzlGJvCf6GEubwE3aV4qF_F93c6Bex7VT4CTfyvY2FwDUsTsjallbkjetSEQ2J4s8_rfavsgQ2axaVYgLnZM1pSCWC4BCigLE2SlTOkHMf_AxRdUYWCcEMeiFsr8Ynr6Qax9UVOilsG9fh7fx0WWdiMDDG4g77af5CgYA22eqYxUF7c-dullAbPHFQfINQB3mPWunNLixY8D_w6rclkngcCrt9KMOw7XERNYCg-2ELl_KdQCRKudQZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مدل Muse Spark 1.3 توی OpenCode رایگان شده اینم آموزش استفاده‌اش</div>
<div class="tg-footer">👁️ 32.8K · <a href="https://t.me/MatinSenPaii/5162" target="_blank">📅 19:21 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5161">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/sx34gyZsm0qS5SaiMjuTJBOKzwSBEd16_UpQ97HqAiV2xcLdtOP35JSuGGSgz1AUeYc8cr6W7ARFuIrnzJUvBBC7J02hhXK_HocYXZc16b-kRtcNrMmRE4tEJ8a8s4-RN8I8t7dcRIi6Jacdwh7MEQAByLxhO6TREi1uLOcH70Uu0GoQXXH1y1i5satRnO39fVm6rYcl7KwK4bzsJ6JkMGbtjmdwG850Cf6a_bKALw-kjMtt0FxQeEauLpud2qXcDs8oqZ4U_SSqmP5anXCUSnTP6IGG5heDE_Fw5CjEOvu085Sc4QQvAL2tvMBjQF7hg0_RHJjwkQWkcNmi0Jj9uQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این هم بنچمارک Fable 5.1
البته با هزینه‌ی سرسام‌آور
10/50/0.25
In/Out/Cache
که خب با Fable 5 یکسانه، اما با پرامپت یکسان توکن بیشترس میخوره(و هزینه‌ی بیشتر طبیعتا)</div>
<div class="tg-footer">👁️ 31.4K · <a href="https://t.me/MatinSenPaii/5161" target="_blank">📅 17:32 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5160">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/YDUuDPdWpmdURNAVhVrY9a_aZnjuEaK7ypl1Ak22VlZMPz6nnTxFWMVcaJfx_ccz7PjPP3KAZRQZEiwh-yrq1R5s435EZ5S2hp-tFtg5YsmtdY1oy1j2jRiKr7JE8lR7gCHml8wwY9BvUi0tSErU3DAP7kMPq96w0z_-vXQKOXBBj6r5b3Fdjj4-RQD8kuvoOSuADvfiKpYcif0vdipl7zl-FJL4Y7_2JnxJM1_Qpvksk3aaZRClDVEp-fnvzg-_O3eq7db24SA9wuWKuTddi4mFLSDtdDMQZIBpUcBMdq2Cs8A30xUILxlX0GrUOzKjHO-CSxsib9qIbIhIm3VyJg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آقا مگه میشه مگه داریم اصلا  حس میکنم خیلی اغراق و بزرگنمایی داره. امکان نداره قدرتش از Opus 5 انقدر بالاتر باشه توی این بنچمارک‌ها:) باید تست کنیم</div>
<div class="tg-footer">👁️ 32.2K · <a href="https://t.me/MatinSenPaii/5160" target="_blank">📅 16:30 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5159">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">کار کردن با مدل Fable 5.1 به قدری گرونه که می‌ترسم بهش سلام کنم لیمیت هفتگیم تموم بشه</div>
<div class="tg-footer">👁️ 32K · <a href="https://t.me/MatinSenPaii/5159" target="_blank">📅 15:21 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5158">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">امروز هم Muse spark 1.3 رو داشتیم هم Gemini flash 3.8  فکر کنم گوگل از جمنای pro 3.5 کلا بپره بره روی 4 مستقیم با این وضعیت</div>
<div class="tg-footer">👁️ 35K · <a href="https://t.me/MatinSenPaii/5158" target="_blank">📅 12:51 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5155">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/c8tzvifKMRCjunGq_NUIhGqMRoa8NS6NT4P8icbMH4hfIvk2vIKDpPjSkRiByO1RCsiOOrEHjd2iBaYi246gYa1e2t0PkTjNyzgAknZjca9EaVoynxM7CbfT-IkAdNZ70_3rLkAI_2dzgJAYTQHw092DhiGT7IRqjX04bkqS4jlqNoJa-XfKZPZDWR5GG6plIMSDlDTp8g99CQa8hN_XRuk4Y8-hmDLmGWQFqC5-RYl4B7c3Uptl32IoJtKYq_39cfVTrKzWEKI4koeDk4gJ-ic-XkPyvhLdlwZPE7I4xRXOzGe0EaOtWRmdhByH2f6QIr2qNB3R8Tz9E9ItRU3LAQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/Xg_eYPRHHBayytupEnqXVSSKv4y2qVbvbP17B8P0AJYwKJ_mvp9XhhKLZbtl0Gp1KfSbgdaz3HcgxuGe91Bi-uy_JtZHjhFaMsvLY6WLFJJeJNVjslQZjJOFrjgM1vPj6LghaIBjFwaCz8H5GFXJD9JsqL9YP5h8eIvY0RYjxpd7CuzjgIJbyRE9zqq2Rge7_RORMLuNLOwNR0GkE4BQQIWaqqOWsb5B1mXeoKzqPQ0oPGaDLaMnhOZJ166-w3yYV-EvEDhX-eLqxclHC8z1flwN7O-IzR1h_CjXH-8XPw3xy1tLjzpSh1Kp6L_b9O13WFXltjo3HM5qfwXkJfPSkA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/TdKP-VQCDslxdKtTHWxc-mfUL5OkP-_xVdcPJj334Y7jH-Y8_UWWePxeZMC5I3486SjwKluPYw8ehSH3uYdFRFaUlTR2-MTzcUt-tt_nom-Y68Vk0pl3SChiGfcIQQBbgJ5WqKNRjbPvb8vG_rntt9kZ0ttW_d8wB2pHHM9FXLI6t_iwZFrCTHXhblcL_eRt-_Ri7uxPnVR1YX0lSCU4hUfLD6LoMfcPgyCgCc0bjHLjEsATF3Yq1ofhl9CI8tQ3d7aG1NyUuBEB5vz3jQNRTT68a-hr6wMbtWi9E1uHCl6lqDwp4zlDf0Ae2SoI2yBDOgItqmuhbv0Rd0-lPW0ZJQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">امروز هم Muse spark 1.3 رو داشتیم هم Gemini flash 3.8  فکر کنم گوگل از جمنای pro 3.5 کلا بپره بره روی 4 مستقیم با این وضعیت</div>
<div class="tg-footer">👁️ 38.4K · <a href="https://t.me/MatinSenPaii/5155" target="_blank">📅 06:22 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5154">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">امروز هم Muse spark 1.3 رو داشتیم
هم Gemini flash 3.8
فکر کنم گوگل از جمنای pro 3.5 کلا بپره بره روی 4 مستقیم با این وضعیت</div>
<div class="tg-footer">👁️ 33.6K · <a href="https://t.me/MatinSenPaii/5154" target="_blank">📅 01:35 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5153">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-text">🔭
اگر نمی‌دونید Connection Chain چیه و چطور باید در WhiteVPN ازش استفاده کنید، توی این ویدیوی کوتاه قدم‌به‌قدم با هم یک زنجیره اتصال می‌سازیم.
📱
دانلود آخرین نسخه از گیتهاب</div>
<div class="tg-footer">👁️ 32.4K · <a href="https://t.me/MatinSenPaii/5153" target="_blank">📅 22:02 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5152">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">سعی می‌کنم آفر و... خوبی اگر باز دیدم که بتونید با این ویزاکارته بگیرید، بذارم واستون</div>
<div class="tg-footer">👁️ 35.5K · <a href="https://t.me/MatinSenPaii/5152" target="_blank">📅 17:37 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5151">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">آموزش گرفتن 300 دلار کردیت رایگان Google Cloud  این سرویس Free Tier دائمی داره. یعنی حتی بعد از تموم شدن کردیت، یه سری سرویس‌ها همیشه رایگان می‌مونن (مثلاً هر ماه یه سرور مجازی کوچیک e2-micro به‌صورت دائمی و رایگان)  و همینطور با این کردیت می‌تونید دسترسی…</div>
<div class="tg-footer">👁️ 36.1K · <a href="https://t.me/MatinSenPaii/5151" target="_blank">📅 17:31 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5150">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">💸
دلار فردایی تهران
💵
220,300 خـرید
💸</div>
<div class="tg-footer">👁️ 37.9K · <a href="https://t.me/MatinSenPaii/5150" target="_blank">📅 14:06 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5149">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Z2fMyxpJHcCtfrUAc7272TAEIrrE0wdn4v3ZedWogyHX0ESqcF_KQYt-gu4z7f3IxSAEDXt2OIDCcbyvof2J6jOwQPtf28kQHxUISSwYYAgcEdx_FMKNN1oxFKAA0sNpzwLMmHT1dtvy34GdQpXkNWBS_v5rZBb_ojJCi7MtZwampBpnAptwcB-wJ64z9ou4V-EOnvnMZF7gKlcn_h25BufxosGOzB9pzlG87iU83nZdIpU1DdbQ1bJo140pVnp0zNpsDEh7MtgyMrgDC0YlenVlDyxYRnpSgSEExd822rVn3yTGqzKvCTWuiq-Nu_YHXIWjjdh5Uj9v4BzQfQlxYg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 39.4K · <a href="https://t.me/MatinSenPaii/5149" target="_blank">📅 13:57 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5148">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/lAMXCophu__M8pTldUF8590GXAKPoc3W95E9kZTRiVjacE_EUanplx7lzE0_t5AMisqGJC5Vi4fK_QXKv7gxQa1MwmXHNXReKrRppoj4poKp030NT_AWNQ1nGAqx5dt3w1JJZjA9KcQAffSyrhDTLB2piywzZDE7fbPHTNJSS9-XV5KJudZUqa7sdGSvJVLmtHmgagzp9FqzAL2T6YkVbUI_HedpHJE98F3pQHOF77FUu3cMJJMVxOICrwcEOPtCCCNA-rMkoVL5F7xKpFmGrvYvKRL0XR9Aj5Rm_zk-TXoYM5CcOOox_rYak0cLwC_0aaIDFy09F6v_ScFoqMowjw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خب بچه‌ها من وظیفه‌ی خودم دونستم که همه‌ی 210 تا کامنت رو جواب بدم. مخصوصا چون سر و کارش با جیب شما بود توی این شرایط داغون.
و الان تموم شد دیگه
لطفا قبل از پرسیدن سؤال جدید کامنت های دوستانمون رو بخونید</div>
<div class="tg-footer">👁️ 32.8K · <a href="https://t.me/MatinSenPaii/5148" target="_blank">📅 13:30 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5147">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">و گویا از apple pay ساپورت نمیکنه. فقط Google pay</div>
<div class="tg-footer">👁️ 32.4K · <a href="https://t.me/MatinSenPaii/5147" target="_blank">📅 13:22 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5146">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/BipojpSZJdDQgK8lsBIxXVfFjGJBCueRxChqYBsbNdx7YVPE5BnppaQ-zyZSZ5e0wwySt71sRlZ9sQhUt_jF1FcRYE8EOnDruhBitxFmttisojVXFXz8swXw7A_ACsxR5BhSEg1W26bw6vLTvSIlsTQtUtOdHR-IXSvoZ5hiXRAut3VT1RBsWgC2mD2movCUDdCrPwr0q61Gj1ppMa52zNJNhy1iq9OKJ3PnWwXQTTfh7CJxmBjmneVxT3VxFSrnsJY4fMgVvNNDoMF-YpNcO6qPvfQzP4UrjDft3tjt95FabdaMYQUBjlgEEEznFwpHYndM5tFProgUB1NzDRfPFQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یکی از بچه‌ها هم تونسته بود با گوگل پی+اندروید
اشتراک Claudeاش رو تمدید کنه با
Mpay</div>
<div class="tg-footer">👁️ 34.9K · <a href="https://t.me/MatinSenPaii/5146" target="_blank">📅 13:21 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5145">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/XBXPnnOoj-UlK6fUPp6LmPzfryIishkpoQlfyCQJkYLWb0txFc3r66319-3urNHOlni0sAGZHBVL6A5u78SW_jEYtJ637rqqiEs0YPR4qCjBtMvH-VGPYeXwxdmNm13ob8xg_tz0P4R_km9VpBQwwH5wPU6thUqh7gTl6gmmOn7vLztVtvi034GfOT6KY3iH5pkQinRT9LhRCMizE2GKyHxquHjFpDdRNhMDFETjdABOWII6F3DDZLGIomFdOHfVnTNT838ksgsmo5CcGgCEflxs3iLQSoHnZeb-MBWaJwGvJIB9O9hlElqypVM45rP1jNkM-Nz_7ILMogRY-zh6-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بازم مشکلی که خیلی از دوستان داشتن</div>
<div class="tg-footer">👁️ 35K · <a href="https://t.me/MatinSenPaii/5145" target="_blank">📅 12:54 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5144">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">و دوستان، با این کارت نمی‌تونید کریپتو بخرید. هرجایی بخواید کریپتو بگیرید نیاز به احراز هویت سفت و سخت داره
راه درست و خوبی برای نقد کردن پول توی کارت ندیدم من</div>
<div class="tg-footer">👁️ 31.5K · <a href="https://t.me/MatinSenPaii/5144" target="_blank">📅 12:42 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5143">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/e3JVfk7pF1fm8z5KfUxeBmH9d9CupPu2vw25rdTDrLLrlm-qADNcSY2XjxHq9wH8rWOX2EMwH4ZphVYwOW_aoLnWorTWXmMAxATLswZWvXOfnKAyk1FF86ApX0XT3SF_vL2gPenLmNk6JE0oQqk9C-csBUo0ygBPgOqINhneXvOQsho-vTBf_ZZYmENkrsoQ_U6UEXclpMePZpHjnQ3B7Tss590IIypmSEZ4IxPRGxZPbqTxBCj59hdkFtGFRsZeUmxjg9-WwfbxjvExK5Dv10WkWyiFD2krieBLu5j6hTzMnTkHgYXk-Xcc4azg0DGCsTOmc5P9r7kipd39duGUJQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نشستم دارم به کامنت‌های این ویدئو جواب میدم و دیدم ای داد بیداد:)
هیچکس نه دیسکریپشن رو خونده نه کامنت پین رو نه تلگرام
متاسفانه تغییری که سایت Mpay داشت این بودش که دیگه با پنج دلار و ساخت کارت، اطلاعات رو نشون نمیده. و من هر طور تونستم این قضیه رو اطلاع‌رسانی کردم
برای دیدن اطلاعات کارته باید ۲۵ دلار رو واریز داشته باشید و گویا این قانون رو برای جلوگیری از سواستفاده و سیاست‌هاشون گذاشتن
من سعی می‌کنم به تمام ۲۰۰-۳۰۰ کامنت جواب بدم که هیچ ابهامی نمونه.
این Ai جالب یوتوب هم که دورش خط کشیدم خیلی به درد بخوره</div>
<div class="tg-footer">👁️ 36.4K · <a href="https://t.me/MatinSenPaii/5143" target="_blank">📅 12:41 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5142">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-footer">👁️ 34.7K · <a href="https://t.me/MatinSenPaii/5142" target="_blank">📅 09:57 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5141">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">چشم روی هم می‌ذاریم دلار ۱۰ هزار رفته روش</div>
<div class="tg-footer">👁️ 35.8K · <a href="https://t.me/MatinSenPaii/5141" target="_blank">📅 09:31 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5140">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">بچه‌ها من می‌خواستم آموزش کردیت ۳۰۰ دلاری Google Cloud و پلن Always free اش رو هم بذارم اما واقعا خسته‌ام. فردا می‌نویسمش واسه‌تون.
اوراکل متأسفانه خودم موفق نشدم؛ به شدت گیره روی آدرس و آیپی و...
اگر موفق شدم روی لوکیشن خاصی، بهتون میگم</div>
<div class="tg-footer">👁️ 37.5K · <a href="https://t.me/MatinSenPaii/5140" target="_blank">📅 23:53 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5139">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/QsYw68ApWhHERO2cQA-5DpLLwoHe-KdSuqIzeiHvYd-2SM2vZW1GPKBHwPxciG_OtD9R-0yvQu47rg3zftorSLx5AjOKERX1PDZkZ1IobZ9BAqo_dfMav8iNuvPbg9Kk3efVd-lOM-UCSocp0JeBdbBegD7ofsYY0R9xrUbVlPDUDGECQO4xQITqpraye71g6IFLTsQ1Z8Js0kLA5yJ2T0pT919DJwGtCcB_XVZAM7h8NAFdpKwThflE-nmytl90J_XvV4yNDNjG8N8ttU2GKztAAnujxTTdrlr-nc6ooaY4zR1sMqCpTbHSyg3QxROCo3aLZM6eNkvjZa2Ico5KpA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تجربیات خوب یکی از دوستان واسه‌ی استفاده از آمازون</div>
<div class="tg-footer">👁️ 39.5K · <a href="https://t.me/MatinSenPaii/5139" target="_blank">📅 11:33 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5138">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">وی پی ان رو ساختم. باید از بخش Networking، پورت ها رو اجازه بدید استفاده کنه. بعدشم پنل سنایی نصب کردم و یه اینباند TCP+Reality ساختم به راحتی هم مستقیم کانکت میشه بدون تانل، لوکیشن آمریکا</div>
<div class="tg-footer">👁️ 36.7K · <a href="https://t.me/MatinSenPaii/5138" target="_blank">📅 11:24 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5137">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Cc-3VqTzekA60Ay6-0urK5imvJYxw89aKXCLmAo_kgxQVQPTtzk0C965tH3yX2vlZIZtYhSYqf1IdyxQwrgqK10ovy_7VHqpSOyHkmT5bsQVdwElTddkBl7AhnNzi0FxepWyb5E5i7JDz_qlzBl6CA2yH20a0cK-LxRswB9922XAfhs_-eEIQWtsQrNKgiNOPv7tns_oIAPhXGf6TIQIXi8KeyJhVQTAs7TUDLUoK0527UkeaIFBcUfrSHJsz_t6bp8brLdKXq7rXk5_YYWMHvnAoIpjPsSfmArdLrPJGT2cavP0zNjY0_W6O0AHvEpEMHqKe1t7M2PRvZ4_CYLD8Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آیپی‌های باکلاس آمازون
🥰
بریم یه VPN بسازیم باهاش و یه هرمس هم بالا بیاریم ببینم دنیا دست کیه</div>
<div class="tg-footer">👁️ 36.1K · <a href="https://t.me/MatinSenPaii/5137" target="_blank">📅 11:20 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5136">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/dF-gA5AOYRWmWict8_yx2SbH9XfqdzPwKSgfYWb_UhUAEqz5Jqhf_WTEFWo9csFXL76_q-hoQfgeLAfrzcWZH9CXod4orI1xOLBNeAdCZsDubf0OskTgsEpvzr-ZbzK0MDN5dSlvlTqUJU1l9fL6dDUN7xBiyZCbVrj5xSNVI-GVsB3gx2czpuIILrIX2sA9VizqrO2pd_A8bsu_1fFKScWFzQBrZ4ME3rIcNF7xUq5tfDVtyE_IzkOYZSphJ9vheK1PGmAuEARcR36HR3M7Z8GZfvaSNpabhc7KIbyuh_ycvu5zGCek-XHLpTQKYUbdoQUmssEcj8GxeO2DVDLZ8w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یه سری از دوستان میگن که اکانت ممکنه ساسپند بشه اما خب.. خودم هنوز ساسپند نشدم این ریسک رو در نظر بگیرید رفقا</div>
<div class="tg-footer">👁️ 35K · <a href="https://t.me/MatinSenPaii/5136" target="_blank">📅 11:06 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5135">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">آموزش گرفتن 200 دلار کردیت رایگان AWS آمازون  با این کردیت، شما می‌تونید روی آمازون سرور یا Storage و کلی چیز دیگه بسازید. اعتبارش 180 روز هست و اگر تموم شد هم، اکانت جدید:)  1- اول از همه، شما باید یه حساب Mpay داشته باشید که حداقل 1 دلار موجودی داشته باشه.…</div>
<div class="tg-footer">👁️ 32.9K · <a href="https://t.me/MatinSenPaii/5135" target="_blank">📅 11:05 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5134">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Fj7JOL5lZv6WgpZQooD77oBx9S8NuHU0WbRHtI6yY4hYKpe3qaN1nv8Sa36-oRZuPqW1szCkd7IY8UZk_SA8qXh8QeEqcjZk85bVN6vTzqYn9QR9yN0RgRrgkzjWWsXooFrbj3D9resPsd84bgSXEEhx5fUrHmezluaiMdtFnmPm-Iqh70kIPi6cdnsFWCY-4TO44SkpDgTQobGCQFvy7quoaCx-1Pqdpi08zQWL-OCBIQPUK_3YFb_cBm7eLQNpjPp5dIOOgyGop3GIQKMcI3nUF_OmxBW66y4ILRC09Tdudb1dsjObjhI6Gvs6L_2_razkj1LLyfY0JWyi5mcqGQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آیپی‌های باکلاس آمازون
🥰
بریم یه VPN بسازیم باهاش و یه هرمس هم بالا بیاریم ببینم دنیا دست کیه</div>
<div class="tg-footer">👁️ 31.7K · <a href="https://t.me/MatinSenPaii/5134" target="_blank">📅 10:55 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5130">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/hPgBeVC4mN45VB6I_ilmLcwegFNsz9PfvZ1l6ra5KMx-e5S_jifkPMgN3Mi38lTb4wObVVD_VSXFN4Ov2-pTxB2urhIBjUT04d226jld02Z8HbmT_8EmKqxNxOcI8ipJNPQER323uA5x6l_eIFFYm6o5g19mz8i9oy0U-OSfGMlxtSU8j9Fh0O9JFSfzw8xRJrdL1FSQ3Ko5ovKIdy1IfxWAjbgdmYw_FdPNaRYoOiWAACT_b_Lyb1h9byzzGlG9G6kT_oz6DgjalPZItjDk_3IRkcf9H6fhDvj7pIl43H4CfTJ6vDW4hpkA2Tg9bnxZfcLQSWuvPXeSGOyJrVv89Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/gzR4DCm0Gn71wMGdd1mj2-PvzzhuxTZ-h4czNNj0kQvraIRKcW9R-K9Bo8BwUFPLU4J92j_UjDjfzNgg_EpkXLQbDEku-Qw9J8xa0WnK4MJl9pR-JMbW7dxPlASOfhoMD4Vs2crBHeIuArHB0cq6zocizRZ4-lNfMy2x29THW1rMf_5TgN5EblIPP0BkwMKIQFe6qj2BD1OsQprlvSBxYyVwSUvURcY3eH_ZOz3xD9y9dtVMjkPCdCdm1dAith0DJFqBbGZL8n837yQnvgj8VTKxuz1wzf-fy4Lf_vdSU6yZ2xg1ahKObN-3KWXEiLwtkw2j9YL_MS-pzy9gyThBow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/BtTUXLm_erYMs8sm6m0oH1_u4WYk7Ru88J8D-__VahAEdBSNNOSCfJzj5TyEdfNaaPQNLzqKqW3vCThXlsjbfDQmqZpJLyi5bo5Rhmkr9k47yG34fQXRVLRwkDwyqHtPoWo6TqhLtRsmxWD_1noCjIL2NOsBz71hBAXrBZ47AHAzlExmblR-9X35YrfpeRDoxfZWwxq4lAVI9CKskqTOoS3Q3fCr1xl7b8hbzh3XGh6U4Wq_9fzrRseqiklCYEpQxCbgT7TuB--RPRwTcBPvyIXeVP7rmzaVb0v0Rd0rtm0puW7dTZjBJ_RNcJOCqmnPp32nmZMW7DR6Snf-tLwqvg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/Nj5RG87z0rROoeRIgxA4gMd14lSbQ60NCbFNI6ozyNMmYydhdXzSi1e9Dwb0J2ejTq3Fppvr_53vbIMgdpn5kp3gczFfwGcN5RkvsL-b1IeESb0TQUnCOidcS1QlFHvYy3wiR73GqSG2HbETQDWeTn6Hn3sYdh0n9DtRwtfc8YLWjgw3O26MYS92SwcaK-G4xq9W6tx5M--_kWajzRGqgcq8M_ImXUTEIZI5rcV_WPC3cfDoZAKMpxOVMScFIg5rB9zihLzhJs6fC0gtJPorCXbSGMtFUur9l9NJMT8P2XztnPKyNABLw9f0lAwKlY2Sh_QzFy_9FFvmCJwOAWmTgg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 36.8K · <a href="https://t.me/MatinSenPaii/5130" target="_blank">📅 10:12 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5129">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/AS3YfawITb06wM1l7Ix4OBV_VjffAA5kHrvx1Y_s9C27bxZcWAKtZdufQQSYoxoKBO81wdeq41xT3IcgcNVtr06F0xDInYwfkjHcjpReHJcXUq8mi6KRL05uZcD2qC1IEXwEWpZk6XVOGhne9RC3vcPwn_h3zKCkpt6X_8ptFMRw5IWre2rphwqNAvldlzZGuoY20GNlw5zYJE4rZT86oQsu4st_K_6s24gNOKDpIEFUkDTMF6oKWFPnJe6vPL-VMMVpP7vbyiMhtuaUnCrYxjE8lXCmoeK1aqGg6c_RK-As_AH9GnRYaHtH7eY47P5L8tg21EBGabrNByXPXnXR8g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">با ثبت نام ۱۰۰ دلار میده بعدش یه سری تسک کوچیک انجام بدید ۵ تا ۲۰ دلار دیگه هم میده
و می‌تونید ۱۸۳ روز استفاده کنید
به نظرم می‌ارزه</div>
<div class="tg-footer">👁️ 32.7K · <a href="https://t.me/MatinSenPaii/5129" target="_blank">📅 09:35 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5128">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">این کردیت ۲۰۰ دلاری آمازون رو هم موفق شدم بگیرم با Mpay
آموزشش رو می‌نویسم الان واستون</div>
<div class="tg-footer">👁️ 33.8K · <a href="https://t.me/MatinSenPaii/5128" target="_blank">📅 09:33 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5127">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">خب بچه‌ها من تمام مدل‌های چینی و آمریکایی رو تست کردم. فعلا برای ترجمه، رتبه‌ی 1 رو
Gemini 3.7 Flash
میگیره. رتبه 2 هم متعلق به
Claude Sonnet 5
هست
که خب فلش توی هزینه، می‌بره. رتبه‌ی یک و دو به جهت قدرت ترجمه هستش
هم برای ترجمه‌ی کتاب فانتزی مقایسه‌ی سنگین کردم تمام مدل‌ها رو(از جمله GLM و MiniMax و.. تا GPT Sol و اینها)
هم برای ترجمه‌ی متون تخصصی علمی
هم برای ترجمه‌ی کتب برنامه‌نویسی به زبان عامیانه‌ی فارسی</div>
<div class="tg-footer">👁️ 36K · <a href="https://t.me/MatinSenPaii/5127" target="_blank">📅 00:31 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5126">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromLinuxor ?</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Kw-psdAhodJvY5-yFW3hHvRYscOuA20MigvA6Nse_YKoz4ETw81tqybOyJXHs4SU7EoB5bpx5p2-SVme96rb-efIh8WViXF752xWNBcNHt5quEo_zA-STlqLP5PN7qCFMhci72_AUItZLm8tRL6PQvbAgWNKT0jMy9Q9x1kTkAOOy8e4tUWPtIp1EpKt1ot6kSQvPVIJdu-LcFHlMotHQuD8tDRCm2usqQ5fsZDGI6czuOqufN0xV8hvy-k0YCrizUX_r8hctLe9ICn9EGbEpB4Q2bzDzhzR0NjfnRav0SoUFO5lJVtWqC44ISN9oqbRKOghb-jcqk1qk3LYgOBDgA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اگه دنبال ساختن یه AI Agent برای کارهای علمی و تحقیقاتی هستید، این پروژه رو حتماً ببینید: یه مجموعه از 163+ مهارت تخصصی که به Agentها کمک می‌کنه کارهای علمی رو فقط با تولید چند خط کد انجام ندن، بلکه بر اساس workflowهای تخصصی جلو برن.
از Bioinformatics، Genomics و Single-cell گرفته تا Drug Discovery، Protein Engineering، Molecular Dynamics، Medical Imaging، Machine Learning، تحلیل داده و Scientific Writing. حتی برای کار با دیتابیس‌های علمی مثل PubChem، UniProt، ChEMBL و ClinicalTrials.go‌v هم Skillهای آماده داره.
نکته جذابش اینه که این‌ها خودشون مدل AI نیستن؛ در واقع یه لایه تخصصی روی Agentهایی مثل Claude Code، Codex، Cursor و ابزارهای مشابه قرار میدن. یعنی Agent می‌تونه بسته به کاری که ازش می‌خواید، Skill مرتبط رو پیدا کنه و از دستورالعمل‌ها و workflowهای تخصصی اون استفاده کنه:
github.com/K-Dense-AI/scientific-agent-skills
@Linuxor</div>
<div class="tg-footer">👁️ 33.3K · <a href="https://t.me/MatinSenPaii/5126" target="_blank">📅 21:16 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5121">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">WhiteVPN-V1.6.4-arm64-v8a.apk</div>
  <div class="tg-doc-extra">34.4 MB</div>
</div>
<a href="https://t.me/MatinSenPaii/5121" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-footer">👁️ 30.1K · <a href="https://t.me/MatinSenPaii/5121" target="_blank">📅 11:15 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5120">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ikP2DbXEMDob8MUqEZFRVc-FN0BCP45PPadwn4fcCYOV8UsTvPGld-TUlQTaeafRNwnZucByIWPNWYmhQcN5BRqCRAeOPnyo0zqpKZ6hy6XoiAxqB4U450A2vFfp_bg6piU8bu9DNLE6MQ6O-owuG9eUASDUWCIN4ps2wHRn5zIMpifP-4ROhMs2sHBp_q8je8pnFZH55BL2-JSpxpsybij5ndkdCf0YhQMe5OSK4ZDCYIbz_2e0GduiIVDDq5Vsctwze4A1X7BlIDrXFUhoHsB0XZBKINUdshgMviu0IqFZnA3NRCjc-engWFJANwA8CLrmd95FbHD01Of4NU7SnQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 30.3K · <a href="https://t.me/MatinSenPaii/5120" target="_blank">📅 11:15 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5119">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">باز دلار رفت بالا و این پیج‌های زرد اینستاگرامی در تلاشن پکیج کسب درآمد دلاری از برنامه‌نویسی رو بندازن به ملت</div>
<div class="tg-footer">👁️ 30K · <a href="https://t.me/MatinSenPaii/5119" target="_blank">📅 10:12 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5118">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">باز دلار رفت بالا و این پیج‌های زرد اینستاگرامی در تلاشن پکیج کسب درآمد دلاری از برنامه‌نویسی رو بندازن به ملت</div>
<div class="tg-footer">👁️ 31.5K · <a href="https://t.me/MatinSenPaii/5118" target="_blank">📅 10:03 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5117">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">آموزش ویدئویی رفع مشکل آنتی گرویتی و سرویس‌های هوش مصنوعی گوگل:
https://www.instagram.com/reel/DZ7NWUOMeHy
هرچند ارور ۴۰۳ به خاطر vpn هست و صرفا باید از کانفیگ‌های bpb استفاده کنید</div>
<div class="tg-footer">👁️ 33K · <a href="https://t.me/MatinSenPaii/5117" target="_blank">📅 09:38 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5116">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">زلزله به بزرگی ۳٫۸ در پردیس در شرق استان تهران
در عمق ۸ کیلومتری زمین</div>
<div class="tg-footer">👁️ 35.5K · <a href="https://t.me/MatinSenPaii/5116" target="_blank">📅 08:09 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5115">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">بازار کار جدید دنیا و هوش مصنوعی! توی 2026 چطور می‌تونیم برنامه‌نویس بشیم و رقابت کنیم؟  توی این ویدئو، با یزدان عزیز در مورد این مسائل صحبت می‌کنیم:  1- مرگ پکیج‌های آموزشی و یادگیری پروژه‌محور 2- دیده شدن و شبکه‌سازی به جای رزومه فرستادن 3- تجربه شخصی خودم…</div>
<div class="tg-footer">👁️ 34.9K · <a href="https://t.me/MatinSenPaii/5115" target="_blank">📅 07:27 · 09 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>

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
<img src="https://cdn4.telesco.pe/file/rMEG76iajonlWiNtrKEY-iWZS2msMguS0BxNsEoi--vUNeeqQjaWTP3R1bHHXD17OVHycY6NUxXwL5B7aF1Jef_G1JLbC3sOJdhiHlvtizLgr5kySoXnXgjgMGhff19vkN-iMe5Lj5avvCQIdXPK_mqp0BGnVivVCKP4sHnsDuqSKSrihYA1R6Y51_U3rkuaUEHG5qDiMwzXuhrFaDXlp5pDWet15AfRUUQvMCEFEIVJ4pJCBzFfSgEN1x4EwvW5IZIyUy94rc4bRdx5ePy50qS4e5miM-dLqdPrQKgMkSTosiFtR2Dk0_EWsUIkLhp6obUy2kLQPL-VC9il3EimaA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 هات نیوز | HotNews</h1>
<p>@news_hut • 👥 226K عضو</p>
<a href="https://t.me/news_hut" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 بدون هیچگونه گرایش و تمایلات سیاسی، همیشه سمت حقیقت و مردم.</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-21 22:11:38</div>
<hr>

<div class="tg-post" id="msg-65868">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">🚨
🚨
ادعای اکسیوس:
منابع ایرانی امروز به کشورهای منطقه اطلاع دادند که توافق «اصولی» در مورد یادداشت تفاهم حاصل شده است، اما تأیید رهبر انقلاب همچنان لازم است.
@News_Hut</div>
<div class="tg-footer">👁️ 7 · <a href="https://t.me/news_hut/65868" target="_blank">📅 22:11 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65867">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">🚨
🚨
خبرگزاری حکومتی فارس:
‌ منبع آگاه: ایران هنوز هیچ متنی را برای توافق تایید نکرده است
هیچ متنی برای یادداشت تفاهم اولیه با آمریکا تایید نشده است؛ این را یک منبع آگاه نزدیک به تیم مذاکره‌کننده جمهوری اسلامی ایران به خبرنگار فارس گفت.
رئیس‌جمهور ایالات متحده ساعتی قبل در پیامی در شبکه اجتماعی تروث سوشال ادعا کرده بود که ایران در عالی‌ترین سطح با متنی برای یادداشت تفاهم اولیه موافقت کرده است.
وی دقایقی بعد در اظهاراتی مشابه خطاب به روزنامه آمریکایی نیویورک‌پست هم گفت که متن مزبور جمع‌بندی شده است.
ادعای ترامپ در حالی مطرح می‌شود که ایران و آمریکا بامداد پنجشنبه یکی از شدیدترین درگیری‌های خود را پس از اعلام آتش‌بس پشت سر گذاشتند.
@News_Hut</div>
<div class="tg-footer">👁️ 4.93K · <a href="https://t.me/news_hut/65867" target="_blank">📅 21:57 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65866">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">🚨
🚨
آکسیوس:
به گفته سه منبع آگاه از مذاکرات، قطری‌ها و ایرانی‌ها روز چهارشنبه معتقد بودند که به متن مورد توافقی رسیده‌اند که آمریکا نیز آن را خواهد پذیرفت.
این منابع گفتند که اختلاف‌ها در سه موضوع کلیدی کاهش یافته است:
سازوکار آزادسازی دارایی‌های مسدود شده ایران - مهمترین مسئله برای ایرانی‌ها.
تمهیداتی برای بازگشایی تنگه هرمز در طول دوره آتش‌بس ۶۰ روزه.
چگونگی انجام مذاکرات بر سر برنامه هسته‌ای ایران در طول دوره آتش‌بس ۶۰ روزه
@News_Hut</div>
<div class="tg-footer">👁️ 8.63K · <a href="https://t.me/news_hut/65866" target="_blank">📅 21:38 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65865">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">🚨
🚨
🚨
🇺🇸
ترامپ به نیویورک پست : توافق «بلند مدت» با ایران تقریبا نهایی شده.  @News_Hut</div>
<div class="tg-footer">👁️ 8.32K · <a href="https://t.me/news_hut/65865" target="_blank">📅 21:38 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65864">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">🚨
🚨
🚨
🇺🇸
ترامپ به نیویورک پست : توافق «بلند مدت» با ایران تقریبا نهایی شده.
@News_Hut</div>
<div class="tg-footer">👁️ 8.63K · <a href="https://t.me/news_hut/65864" target="_blank">📅 21:37 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65863">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">🚨
🚨
🏆
🏆
بزنید افتتاحیه ببینید
🔥
🔥
Persiana Sports (بدون VPN) Bein Sports (بدون VPN)  لینک های m3u8 رو با برنامه های iptv player یا mx player - pot player - vlc پخش کنید.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 8.32K · <a href="https://t.me/news_hut/65863" target="_blank">📅 21:37 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65862">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromجام جهانی 2026 | فوتبال 180(ммd)</strong></div>
<div class="tg-text">🚨
🚨
🏆
🏆
بزنید افتتاحیه ببینید
🔥
🔥
Persiana Sports
(بدون VPN)
Bein Sports
(بدون VPN)
لینک های m3u8 رو با برنامه های iptv player یا mx player - pot player - vlc پخش کنید.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 8.62K · <a href="https://t.me/news_hut/65862" target="_blank">📅 21:34 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65860">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/gC20_C2FvuIPygLZOg80WYtCO0Uqd-vYhWkPpzlpbVu3rkVCbZB-Ro2hkTqahifmqCKkZnI_nWFVrjCXbH4eEORLcnhwwyCqF2dI0Z6SuNtZqcPmUT3uj3gEYfYI-fL1idnKl8yIfbkZO49unJgfxLrQJzuEP-lron-XMCyEn8icLVQrQt-r4uPFn_H2h6PvnwQBxGDkWJ7BINZl6yY7FtXp-3cb1F8TiXZJpFY4wM8wutVyvufT-eqPSUmiFJ1C8XUD9HLwa5W_WAbXs-qcsP8rqwLSgEWlPkCKKOWlv-KPD8Ja6lx1H48Axv5hmp9uj9Kl0P7k27oW9_8h7Eqgvg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/EOg7WzaRBQlsJOXkQWAn5EwnZgvrXZ24jQ45KhmEuDXjbruc3tOwFtvWrVGbXbWW3fb7Xo0P2tOi_2NqWCEFE9Y3hAin08CFRfglfEdmc7OwdRIg2cirfnzLfkSAl730UmO85hyMBkKUEoKYEq9TOAip1Q_ou1DOBtWsBPtQediv44F5YyaYWDgI9eGBvKUPHt1z8VhQv0cZNBDwZGe1YkwV_pPUZ_QX1d2HPXO9Y_ebg82BXU7bmucPyyB7GY83zZQ2cPPMb6zZMzF2PRHSMbz5bQOsHOIUltZ4TJXRv55aRJR2ttiI8AksxOJyxIXO7NlqzanLfcuCpa8b5dQzIA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🏆
اجرای شکیرا در مراسم افتتاحیه جام جهانی
@News_Hut</div>
<div class="tg-footer">👁️ 9.24K · <a href="https://t.me/news_hut/65860" target="_blank">📅 21:30 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65859">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DGFR7pP8oLLfcuVmTczp6czif2kKhOhsDU66_XxC1OF3CpaB1u8S-AE-8vBE9Xov1mDxfj7zA-I25Zli_8F0jyUa00W_xZjKCtjsIa3k0f08DI7Gl91v5Qh7wArl7Cjs43VjlA-9DmO8-rWT8CZ7Pa0cyJFT8YVKPRQ06RwI1umdjVYsR5xP7e-izeRVkTEKss-dOcH0LBnLnHwwEVjuZKIdpAiNoIvAvIYuEyLCLOqwuOG4vZHZWqdQ826TbJFaOtI70nkrX-KGT9Vn5PC3i1kPDGSem5dd_ONdNN9YGroKMPWiNQzafebYSkunvRfoBMIO1pEJYrgPeGSgLvvj8Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این سایت سپی هست داداشمون
که در تمام سه ماهِ جنگ vpn هات نیوز رو برای پوشش اخبار تامین کرد، هواشو داشته باشید و می‌تونید از داخل سایت بطور زنده افتتاحیه رو ببنید فقط کافیه یه ورد بزنید
🔴
لینک سایت
http://Chosefil.com
🔤
لینک کانال
@officialChosefil
#hjAly‌</div>
<div class="tg-footer">👁️ 9.55K · <a href="https://t.me/news_hut/65859" target="_blank">📅 21:22 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65858">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">ترامپ=حرومیِ کاکولدزاده #hjAly‌</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/news_hut/65858" target="_blank">📅 21:15 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65857">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">ماشالااا تراااااامپ شیردل
😤
#hjAly‌</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/news_hut/65857" target="_blank">📅 21:07 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65856">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rXOGXoSuTHw5R3slkwkHdQd2Ky3o4pl0zo7J89EALDG4W-wVBkyXUVsm23O6NhAtx9OVMYwhBfGczOii_SzUl3fcP9Eqse_PY6teKmsAEtAqw8e2FdZMD9gNmwIwtKUWMYP7FgwgJv0FE2LDnzlu5mN1CWOLjkCu7whlTPfYZI4jizoznPMFi8bnY-havekEtSXm4BkjRK_IG2LzRGndiLYIjHkLaSlrmpobvtc7A5LlGuqZDr0yTZM9Xd_E_ydFU1RuJPiKr7ghl9NFyQR5CrYKdjgYawAk-j5p3_W1LyBp12EnA_hmeO8kclljHXhqAMq4FlFhtp_5hozRHY-zvA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
ترامپ:
حملات و بمباران‌های برنامه‌ریزی شده امشب علیه ایران را لغو کردم.
با توجه به اینکه مذاکرات با جمهوری اسلامی ایران به بالاترین سطح رهبری ایرانیان برده شده و تایید شده است، من به عنوان رئیس‌جمهور ایالات متحده آمریکا، حملات و بمباران‌های برنامه‌ریزی شده امشب علیه ایران را لغو کردم.
مذاکرات و نکات نهایی، هم از نظر مفهوم و هم با جزئیات فراوان، توسط تمام طرف‌های درگیر، از جمله ایالات متحده، اسرائیل، عربستان سعودی، امارات متحده عربی، قطر، ترکیه، پاکستان، بحرین، کویت، اردن، مصر و دیگران، تایید شده است.
محاصره دریایی تا زمان نهایی شدن این معامله به طور کامل و با اثر باقی خواهد ماند
زمان و مکان امضا به زودی اعلام خواهد شد.
@News_Hut</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/news_hut/65856" target="_blank">📅 21:05 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65855">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">🚨
🚨
🚨
#فورییی
؛ترامپ:
حملات و بمباران های برنامه ریزی شده عصر امروز علیه ایران را لغو کردم
@News_Hut</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/news_hut/65855" target="_blank">📅 21:04 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65854">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">🚨
🚨
🚨
🇮🇷
علی‌عبداللهی فرمانده قرارگاه مرکزی خاتم‌الانبیا: صادرات نفت و گاز یا برای همه خواهد بود یا هیچکس. ترامپ اگر خریت کند تمام منافع و منابع نفتی و انرژی منطقه را با دستور قاطع پودر می‌کنیم
@News_Hut</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/news_hut/65854" target="_blank">📅 20:15 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65853">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b7e36d42b7.mp4?token=c6UR6fQZ6qVFWAC3k9lUWcpqOqOh-ZOy8cy9eKOBXfPZWRv0DIrryCJ-tdmRIPcWKDvuBK5N7Y_CapaoMnMOWTQBws-lZpdJ1uYazSketA9jNvzWHJLIMp2Qs2Tl4m9Z7lqBHMxpU8yqfum6NpnEO6X7DBicAhSIjR38Z3yh24x2TQilZwBKu4Wvj57OjRE2y7hO-YR2PMRCtaGV6l4AqYgWnG-16Fs8B4ufpB258m-OuQKCoR2ww5QAVxByZRsN7vNPAw2gZHcGP4E9XLUahqv5Chy6CNnV9bXYDgZZmfGgWdQ_PFGlfIQRzntav3rdd4bEk9Oo-wAdKI3O8z0o_w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b7e36d42b7.mp4?token=c6UR6fQZ6qVFWAC3k9lUWcpqOqOh-ZOy8cy9eKOBXfPZWRv0DIrryCJ-tdmRIPcWKDvuBK5N7Y_CapaoMnMOWTQBws-lZpdJ1uYazSketA9jNvzWHJLIMp2Qs2Tl4m9Z7lqBHMxpU8yqfum6NpnEO6X7DBicAhSIjR38Z3yh24x2TQilZwBKu4Wvj57OjRE2y7hO-YR2PMRCtaGV6l4AqYgWnG-16Fs8B4ufpB258m-OuQKCoR2ww5QAVxByZRsN7vNPAw2gZHcGP4E9XLUahqv5Chy6CNnV9bXYDgZZmfGgWdQ_PFGlfIQRzntav3rdd4bEk9Oo-wAdKI3O8z0o_w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
‼️
تهدید وزیر خارکمبه علوم: اون دانشجویانی که پرچم پهلوی گرفتن تو دست و پرچم جمهوری اسلامیو اتیش زدن تحت تعقیبن قراره مجازات و اخراج بشن
@News_Hut</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/news_hut/65853" target="_blank">📅 20:10 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65852">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/A4OHb_838sqMpNWkoI-k-_aG3kze_sL6rXcV4vsEUSC5yg_04mEIDNP99mI2CYV2C28QEedN4BDFCiLYOlWxtpS1Mu3QKYEmUCNA5ko_kXX13KgOD5oIrUmiSNgu0qtF1ELtJHy7qApAhr1wbCUGSHlcg5S3Imxee661Ia3XRbM8sY8ZAwqXLsPmi5ImcKmWjkfjtAkS4IN3eFX6A0y_cWMMbK9Y5bJlB6ZsoBHjT760WGKHutgL1_mYHRqeuTPxeiqvRY_1b8vX1VqpUwZs7edN-yTxh_NnbQnae6D58G28YuRjoC1xNqIEE-V9cexzhMql-5r8y4zX1IoNQgWPww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
قالیباف:
استراتژی‌های اشتباه و تصمیمات عجولانه، کل اوضاع را به سمت بدتر شدن تغییر می‌دهد، زیرساخت‌های انرژی و بازارها را منفجر می‌کند و باتلاقی بی‌پایان ایجاد می‌کند که سال‌ها در آن گیر خواهید کرد.
شما ایران متفاوتی را خواهید دید.
زارت
😂
@News_Hut</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/news_hut/65852" target="_blank">📅 20:04 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65851">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZLqFBpJl4g_hp5WBEEG_l8LmLuiieBoi51LqC2GQy2G1xXrWw9QPXPUNzapdlce169ZdLhc9Ue3DhkUFgpbbNVhvMj1cb0nLjfAcugSuF8SB2tekxi2k2Ow_oVrTt8KDvTKopxewNboE_hggboipnVqsx7e03BNgfdsth1iIl4DN8R5md-EWmPl70t4EyI5tfzIhW683GVMO16rjC3RNy2wdiV0FlhcTb2X6W4-rx8VqwTQvs3Ny48TrAftJjB5MRlPLEnez455aQZ2ON3zArIFVk2WmpdNuUXqa4U5OfIo98A5Iq1lIaabB1CSAMSxUduR6rz87rw7yrLJOJIenOQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
به‌روزرسانی عملیات در لبنان:
سربازان ارتش اسرائیل فعالیت‌های خود را برای دستیابی به کنترل عملیاتی و پاکسازی منطقه شمال رودخانه سلوکی در امتداد خط دفاعی مقدم به پایان رساندند.
منطقه رودخانه سلوکی توسط حزب‌الله به عنوان مکانی اصلی برای عملیات پهپادهای انفجاری و حملات غیرمستقیم علیه سربازان ارتش اسرائیل استفاده شده است.
این نیروها صدها سازه تروریستی را منهدم و بیش از ۵۰ تروریست را از بین بردند. علاوه بر این، چندین سلاح از جمله دستگاه‌های انفجاری، موشک‌های ضد تانک و موشک‌اندازهای ضد تانک کشف و ضبط شد.
@News_Hut</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/news_hut/65851" target="_blank">📅 19:55 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65850">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CL62qDOZhlSsrS2iw_7xaSOoUCfyj95WJgpa8l0ucaJ3bNBrizYThHjkpQL_iiSW6cClYRrksriJKZbKQfL07fR__A4i5_-Pz-tAXToy65pmvQh4dVHEo0xR_5eXs96ZEZR9OJPUVWsuc4aPNkDIEvTN9UtOIV1V0FsUaMb5uX1qHs9yp5kitnD-jI7y5uqo5t-KjNEFfqZDKBIgIQksYkzoaaAHj9-pD68ct5nAovsj3J9ndJDINLsPWBCxDVcQijPUSYZlDa6Q5gpSaZZzhBXEZNh9XRm9aqE49fxxl_rw_6O9PkvJAAtHm-IBP5oPfmYC_Z3hPXQT2DJxRElqsQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
پست جدید سنتکام:
تنگه هرمز همچنان برای عبور و مرور باز است.
@News_Hut</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/news_hut/65850" target="_blank">📅 19:42 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65849">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">🚨
🚨
🚨
⭕️
الحدث: ترکیه، مصر، پاکستان، عربستان سعودی و قطر قراره جلسه‌ای فوری برای جلوگیری از شعله‌ور شدن جنگ میان ایران و آمریکا و پیدا کردن راهی برای توافق بین این دو کشور، تشکیل بدن.
@News_Hut</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/news_hut/65849" target="_blank">📅 19:25 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65848">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">🚨
🚨
جمعیت هلال‌احمر اعلام کرد که در پی خطرات احتمالی حملات امشب، در آمادگی سطح بالا و کامل قرار دارد
@News_Hut</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/news_hut/65848" target="_blank">📅 18:59 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65847">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oKvmcAi0nMlyyaV4pTTbU9RxL9l3ZF0bfHK9U0NW92YKnLEivCP1ZBIn0yKaQvfHnqovI0VJnXS63A39k-tVWWFr79BT6oEk4dN5T2b1LUcozcMO4LjAdb_nXmJaHZnu3Dd67jb1ZdHmiu_sqJ3T03k2KlZB6ut8FOzi91W6XBZxgTer9_BrXv69OiOjAcnffStt8USnnOg13JPs-leF3v4tAk2VEh6UfV0WQ0zODwZi-gc5z9wdl9B72b1XeWVJNTNiEhTSt9JQSAk6kyKGOchaokzxhJfyzIj_uzOsnqWHrsLG0u5fZwEJGXc-NlZp2lC8-ibPImE5kHb7DE_3iQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇺🇸
پست جدید ترامپ در تروث سوشیال
@News_Hut</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/news_hut/65847" target="_blank">📅 18:48 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65846">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">1xbet_ir.apk</div>
  <div class="tg-doc-extra">53.8 MB</div>
</div>
<a href="https://t.me/news_hut/65846" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🔥
ورژن جدید اپلیکیشن وان ایکس بت بدون نیاز به فیلترشکن برای گوشی های آندروید
🎁
اپلیکیشن رو دانلود کردید موقع ثبت‌نام، کد هدیه 1x_1566529 رو وارد کن و تا
100یورو
هدیه بگیر!</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/news_hut/65846" target="_blank">📅 18:47 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65845">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cqTUB3g3fJc1HLE544rJsvebKHuYAsC-yEqdNCqAxl2j-kVW5G9N2c23TDPZKQ_UoYNOrNZCvPSEQOHux7n8_uyEiC6_liIDOCizYEpIvkCMgaGRJOA79sC0c-ks3i2B3EdnElDAUUJowEzHIWHgfn_86HT3ogSHIVCbY0rCMJJr252O1zOPq92KICiJ7UuLlMVzenNQUAKrxzO8g5h-dTwe-QIRA6i1PLIVsG-Ch5gf-3-UfuXyBanZYF7RewAkAkvgoLz9c-uHq82CajjsXfB-gJAHPd7wkBjP5oxGsZs_yrgF67qc1BaTy-HpP34c_yPh3WiysJaG0yuQEdV8KA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
جام جهانی ۲۰۲۶ فقط یک تورنمنت نیست؛
جاییه که رویاها ساخته می‌شن، ستاره‌ها متولد می‌شن و تاریخ دوباره نوشته می‌شه…
🌍
⚽️
از نبرد غول‌های فوتبال تا شگفتی تیم‌های کوچک،
دنیا دوباره برای بزرگ‌ترین جشن فوتبال آماده می‌شه
🔥
┅━━━━━━━━━━━━┅
🟦
آدرس وان‌ایکس‌بت:
🌐
bitly.uk/connect1xbet
🌐
bitly.uk/connect1xbet
🔓
برای ورود به سایت از فیلترشکن کشور های اسیایی یا کانادا یا ترکیه استفاده کنید
⬇️
فایل نصب اندروید 1XBET
⬇️</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/news_hut/65845" target="_blank">📅 18:47 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65844">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/14bcfc7050.mp4?token=IwMRiA70dzV-vBz9m2gli8C3h5kdxURr1okZn_DhDVd8Jd-1PXggRfarInKnEmQB_yhaWJIVtT3z1CMBqCvzCFyZOXjMxPy0RwuV3CxH2KPpYOav-4wigi1yQqd60T0oZoqVFpW3STB0LYzOXJczZQYms2pPNWqdlQvUsitGnD0iexJ7YcHgL6ULfwftI4xezEBUVUip4fTkIFYxiWILdFuvcdPaksxCOcG1mvSe61XVv1vgF-LCxDNbDpjbLIW91Ws0hN7mPfXjLEJ9Fqc8-bX5EsyB8jkNRIFHJXbPE0SG5-4QJ56oWA8G9vhRn0elzBN4SpknlkbeoTyp0XBq6w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/14bcfc7050.mp4?token=IwMRiA70dzV-vBz9m2gli8C3h5kdxURr1okZn_DhDVd8Jd-1PXggRfarInKnEmQB_yhaWJIVtT3z1CMBqCvzCFyZOXjMxPy0RwuV3CxH2KPpYOav-4wigi1yQqd60T0oZoqVFpW3STB0LYzOXJczZQYms2pPNWqdlQvUsitGnD0iexJ7YcHgL6ULfwftI4xezEBUVUip4fTkIFYxiWILdFuvcdPaksxCOcG1mvSe61XVv1vgF-LCxDNbDpjbLIW91Ws0hN7mPfXjLEJ9Fqc8-bX5EsyB8jkNRIFHJXbPE0SG5-4QJ56oWA8G9vhRn0elzBN4SpknlkbeoTyp0XBq6w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
'لحظه انفجار حمله حدود ۴ صبح به
پیشوا
در  تهران
@News_Hut</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/news_hut/65844" target="_blank">📅 18:29 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65843">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Gxg_6yXQiak7cz0_zxx_ii_VHwvnYy6XfXhYvuV77PARk7GuZS45pG9-Lbms0aJjIyeWPjmnYj1FBNngNJyH1ach8c5wMSTFc8rT-f3dDLH8bPHKLrKJb-aGjueDEPQvRXGHonWkJhd0bCmORHdkCCOL9uBm5hkvL_aV9w76K8ZfDw5Lpbm25z3b3XvhX51kIuqCsUavc5FZf5Kx13tlYICPJ2kIsFd_dl2EOfN-T3qz_sV2VEEBXkIHEKIbCUd3tdA055u2ATRwG5a23q8RpyUEfPwdCf5qXPoJ_Ra2GtqidI2bqLsLi0wVbsAZvRjaM93qws9n9z3BGAS1CSL07g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
پست جدید حساب کاخ سفید:
«رئیس جمهور ترامپ همه کارت ها را در دست دارد»
@News_Hut</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/news_hut/65843" target="_blank">📅 18:10 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65842">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">🚨
🚨
اسکات بسنت، وزیر خزانه داری آمریکا:
رژیم ایران در بازی مجموع صفر که در حال انجام آن است شکست خواهد خورد.
هر آسیبی که به متحدان ما در خلیج(فارس)وارد کند با وجوه استخراج شده از حساب های ایرانی جبران خواهد شد.
هر عوارضی که به مقامات تنگه خلیج(فارس)پرداخت شود با وجوه استخراج شده از حساب های آنها جبران خواهد شد.
هر حمله ای که ایران راه اندازی کند، تنها پیامد های مالی و اقتصادی را که با آن روبرو است عمیق تر خواهد کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/news_hut/65842" target="_blank">📅 17:58 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65841">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JPl6m7xu_QD4uMhB9mxoCgb3q2XQrj006BjQ2leMBd41qB-7Rnsnk4Mjpd73bGL-MoPN4fcv0H1EuXYwSpQugBy8kRSdDH66RNKHNWO1Zhtm4yyQ0XDloyTJpxe8t4PcWiJjp9Yv2LBjpWrnZWkJqTUoj7_dOK63LXO05f8vSeeGsv4RDUEDexa-bCbMbuTr2-_ZSVru_Syxa83ms0Q_i4yaBEOMweq2uva-q3MPvYZ96t-hPL3_a5sJWfABGnu2iL7MqOY0-63bGfVSeaeSh12i_gGbo9uuCGpd1l0W9MlBc0qEQwOvHOaMp95qU7Mb31U7ckH3r_4bBRMwKdS-MQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
ترامپ:
ایالات متحده امشب به ایران (که نیروی دریایی، نیروی هوایی، رادار، پدافند هوایی و تمام اشکال دیگر دفاع آن، به همراه بخش عمده‌ای از توانایی تهاجمی‌اش، از بین رفته است!) ضربه بسیار سختی خواهد زد.
در مقطعی در آینده‌ای نه چندان دور، ما جزیره خارک و سایر نقاط زیرساخت نفتی را تصرف خواهیم کرد و کنترل کامل بازارهای نفت و گاز آنها را به دست خواهیم گرفت، دقیقاً مانند کاری که با ونزوئلا انجام دادیم، که به طرز درخشانی هم برای ونزوئلا و هم برای ایالات متحده آمریکا نتیجه می‌دهد.
از توجه شما به این موضوع متشکرم! رئیس جمهور دونالد جی. ترامپ
@News_Hut</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/news_hut/65841" target="_blank">📅 17:43 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65840">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">🚨
🚨
ترامپ درباره ارسال سلاح از طریق کردها:
ما در واقع به آن‌ها سلاح فرستادیم و صادقانه بگویم از کردها بسیار ناامید شدیم. کردها ما را ناامید کردند.
من با این تصمیم مخالف بودم. می‌دانید، من می‌گفتم، «نه، باور ندارم که آن‌ها سلاح‌ها را تحویل دهند.
فکر می‌کنم آن‌ها سلاح‌ها را برای خود نگه داشتند. فکر می‌کنم این یک ننگ است. اما من این را به یاد خواهم سپرد، کردها. من این را به یاد خواهم سپرد.
@News_Hut</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/news_hut/65840" target="_blank">📅 17:33 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65839">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">🚨
🚨
جی دی ونس درباره نتانیاهو:
نتانیاهو کشوری را اداره می‌کند که به‌وضوح یک شریک بسیار نزدیک ایالات متحده است.
اما حتی وقتی ما شرکای نزدیک بوده‌ایم، گاهی اوقات منافع ما کاملاً همسو است و گاهی اوقات منافع ما ناهمسو است.
نتانیاهو به‌شدت منافع کشور خود را تأکید می‌کند. گاهی این بدان معناست که ما در یک صفحه هستیم و گاهی بدان معناست که نیستیم.
آن‌ها به‌عنوان یک شریک بزرگ در بسیاری از راه‌ها بوده‌اند، اما ما همچنین باید بر آنچه در بهترین منافع آمریکاست تمرکز کنیم. و جایی که این منافع منحرف می‌شود، متأسفانه برای اسرائیلی‌ها باید سمت مردم آمریکایی را انتخاب کنیم، که همیشه این کار را می‌کنیم.
@News_Hut</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/news_hut/65839" target="_blank">📅 16:30 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65838">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromromo heidary</strong></div>
<div class="tg-text">اسپویل
فیلد مارشال عاصم منیر، پادشاهان عرب به ویژه محمد بن سلمان از من خواستند که به دیپلماسی فرصت بدم و ایرانیا هم از من خواستن تا فرصت نهایی رو بهشون بدم منم گفتم باشه و حملات امشب که قرار بود زیرساخت های ایران رو نابود کنه و جزایر ایران رو از روی نقشه محو کنه متوقف کردم
از توجه شما سپاس گذارم</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/news_hut/65838" target="_blank">📅 16:19 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65837">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">🚨
🚨
🚨
🇺🇸
#فوری از ترامپ: آمریکا امشب حمله بسیار سخت و شدیدی به ایران انجام خواهد داد. ما بزودی جزیره خارک و دیگر نقاط زیرساختی نفتی را تحت کنترل خواهیم گرفت و کنترل کامل بازارهای نفت و گاز آنها را در دست خواهیم گرفت، همان‌طور که با ونزوئلا انجام دادیم  @News_Hut</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/news_hut/65837" target="_blank">📅 16:08 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65836">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/m7AH0lpI1NaTZ_-z31YtFe39_tnFYxSDbZuzu4btUM6XFz9Wb1KNyNiSMKQLd317yOVQoyO90PdAAYNVqJ4tIEzYciSkKwUK205dVIk-fZ1elrgV-Mm7Oj5ZrmswveRFJSVkPaE_KNoAJpLjo88BSbu1sq5loxmqGuMP7U9TDMomgZ4_yusNOGrVOezRbQ34KCfquT9slEU7u1XwnYku0pXicWHjuPYvJDquvcABAb03WyL2ycAPui1RX_zBfxd9EDL__uDgjuKc_qdNDHWX1NGa1C86bRaj33yOPutWF_cNJKS9ht_1IDj91A4f1Mb-pwiRoOo814U7dGYzZCQAyg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🇺🇸
#فوری
از ترامپ: آمریکا امشب حمله بسیار سخت و شدیدی به ایران انجام خواهد داد. ما بزودی جزیره خارک و دیگر نقاط زیرساختی نفتی را تحت کنترل خواهیم گرفت و کنترل کامل بازارهای نفت و گاز آنها را در دست خواهیم گرفت، همان‌طور که با ونزوئلا انجام دادیم
@News_Hut</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/news_hut/65836" target="_blank">📅 16:06 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65835">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MVdqpj55TIeN-3yOcWZlyrdxcHGDIEUsFTSILblUVimgcPBeSRQT07ksed2ZIsVdubqTH48D98Skw36UtF_lDrVwoixDdGzbXz3OEjUbWEMeUJaT5waJ2Klcun5XQ5jmDDv6kmUEmYWdIfLeFTZTeek7JiO-G6BlFZDjNLAJKo-hANG31uCKCDMIfTlTOyQuO29EAOqgsK2X8gH_Eb9BGggypQFbX2B_YZ5w7hYTucB7a3K6WtEB_kGPPD4KiueC4ylDhwvGG0TOntFfXQg7auPrVvSL8m5PB9dsiwML5DJeAaMZCOOUYYc9Xw8v6ynD_UDu5jYSqFiVax9zSwXQuQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
ایران اینترنشنال:
‏
محسن رضایی، مشاور نظامی مجتبی خامنه‌ای، در شبکه ایکس نوشت: «رییس‌جمهوری از تعادل خارج‌شده آمریکا تصور می‌کند بمب‌ها می‌توانند او را از باتلاقی که خود ساخته نجات دهند، اما موشک‌های جمهوری اسلامی او را بیش از پیش در همان باتلاق فرو خواهند برد.»
او همچنین نوشت آمریکا در برابر انتخابی دشوار قرار دارد.
رضایی افزود: «واشینگتن باید میان پذیرش شروط جمهوری اسلامی و از دست دادن آخرین بقایای اعتبار خود در جهان، یکی را انتخاب کند.»
اظهارات رضایی در حالی مطرح شده است که مقام‌های جمهوری اسلامی بارها بر ادامه پاسخ به اقدامات نظامی آمریکا تاکید کرده‌اند.
@News_Hut</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/news_hut/65835" target="_blank">📅 16:01 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65834">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">🚨
🚨
فاکس نیوز:
«ما آنها را بمباران خواهیم کرد.»
هشدار صریح رئیس جمهور ترامپ به ایران در جریان تماس تلفنی با تری‌یینگست، معاون رئیس جمهور ونس و نمایندگان ویژه استیو ویتکاف و جورد کوشنر از اتاق وضعیت مطرح شد.
دولت معتقد است که ایران همچنان در میز مذاکره تعلل می‌کند، حتی در حالی که نیروهای آمریکایی اهرم نظامی گسترده‌ای را نشان می‌دهند.
پیام ترامپ: ایران حتی نمی‌تواند آسمان کشور خود را کنترل کند. ایالات متحده ۴۹ موشک تاماهاک شلیک کرد که طبق گزارش‌ها برخی از حملات به اهدافی در حدود ۴۰ مایلی خارج از تهران اصابت کردند، در حالی که جت‌های جنگنده مواضعی را در امتداد ساحل جنوب غربی ایران هدف قرار دادند.
در مرکز این بن‌بست، یک توافق پیشنهادی وجود دارد که تنگه هرمز را بازگشایی کرده و محدودیت‌هایی را بر برنامه هسته‌ای ایران اعمال می‌کند. اکنون سوال این است که آیا تهران قبل از تشدید بیشتر فشارها، به میز مذاکره می‌آید یا خیر.
@News_Hut</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/news_hut/65834" target="_blank">📅 15:32 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65833">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JFMXRfP491veJV2y2McJYcjGLyrSeZ--A8YUhVL7qixjT5o7-e_zj-Lwjse_gfGkTtK2D6aajFEuUXoSUPQYFPbcPmHYLgCBP1mDbqcMQLzithYbiL80NKOa5GeEzoubJnTB6s2bNYxOeguRx1jc0ioxBU9tM1Kk4qyPPabAZ80frINIV6ZcuAQ2uIxm8438Hf8Lads6wAsS0BAtF_0ShReDqrPsn1UnB6Y7pHL5q-1_Iq5sGoFTp54cpv9uW5OHKfVwAp8hTJFTh9FsoH6In-0KIBF9W0sbNFhHwsJMvR0-uHVKIMHVSyc7iJMHMXrCXpQODy-e2L9mmMLwfynKyQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
فرماندهی مرکزی ایالات متحده:
نیروهای آمریکایی در ۱۰ ژوئن سومین نفتکش ناقض محاصره ایران در خلیج عمان را از کار انداختند.
سنتکام پس از تکرار عدم رعایت مقررات، دو موشک هلفایر را به موتورخانه کشتی M/T Jalveer با پرچم گینه بیسائو شلیک کرد.
اوایل این هفته، هواپیماهای آمریکایی کشتی‌های M/T Marivex و M/T Settebello با پرچم پالائو را به دلیل تلاش برای انتقال نفت ایران یا حرکت به سمت بنادر ایران از کار انداختند.
از ۱۳ آوریل، ۹ کشتی متخلف از کار افتاده، ۱۳۵ کشتی تغییر مسیر داده شده‌اند و ۴۲ کشتی کمک‌های بشردوستانه اجازه عبور یافته‌اند.
این محاصره به طور بی‌طرفانه علیه کشتی‌های همه کشورها که به بنادر و مناطق ساحلی ایران وارد یا از آنها خارج می‌شوند، اعمال می‌شود.
@News_Hut</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/news_hut/65833" target="_blank">📅 15:03 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65832">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">🚨
🚨
خبرنگار صداسیما: شنیده شدن صدای انفجار در محدوده سیریک
@News_Hut</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/news_hut/65832" target="_blank">📅 14:51 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65831">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ugzCfbz54v_MwOhGKetpoAhd1ASj_0rCiiQGLczZd5kxPNkEgBiYe3RdVMXfW0A2s7aL9c4dIzqowTHb7CnWnYUyczg3MwvD3A-c9o8wH4qm6i265506yQCvJBmN2Qfnxl_AIBdFAUDDO5mIlSBQkQ2bPOt-8hiSowT23Z_tM_-fYTO0CPGmGG1dgjMAHlUk0fTLH_fjM4sasSVDCvVCchIWiZEcT_6daOxmZ215yFas-IXuIYzf9gyUW88Rbb-dOIjG8yCoCtgo57ljYxGwboOdEnREL4i2sBtX0WexbDvVBN81rSb2sDtpDEOjwg1Aw6STiyyqYPJQL6NgerLqIg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚬
🚬
شاهکار جدید رستوران های تهران:
⭕️
پنیر+ گوجه+ خیار+ گردو= یک میلیون تومان وجه رایج مملکت!
@News_Hut</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/news_hut/65831" target="_blank">📅 14:32 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65830">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">🚨
دلار: 180.700
@News_Hut</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/news_hut/65830" target="_blank">📅 14:30 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65829">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">🚨
🚨
وزارت خارجه کویت:
حملات مکرر ایران نشان دهنده رویکردی سیستماتیک و تهاجمی است که کویت نه آن را می‌پذیرد و نه تحمل می‌کند
@News_Hut</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/news_hut/65829" target="_blank">📅 14:22 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65828">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XKRxloDdBtXu1bXvT0ciYLBqmRs0yjS5JgABtUxp3psuCneJKu7d0Vja0mInyLx3GsxaomstNrQrw1AMZkDZ6zaeySlyaZosut76eeywzfKHVl2qA31s7PTnIgHwpc6Ol_e8OlHjmJFEo-FKXcgoV0FYDot9NR5zsoFw9jTFajkQlFFbpsUSdvo9ZozwKRYSlpYmwjVUTZ96Bs8hUrSkAOSU47TDhAy6Yh6irfkCVLY8Ry_HANfQ1lWpy0hjVZP_VCfcE1sb0EmJfpGR5qgvcOvga9l1Ncd-8AtBs_vxu5IEgSzZ5ZNv-PUg80hjxC2eAK_aYdKq2kPTQvP5IjRfqg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🇮🇱
اسرائیل به فارسی:
دیروز عصر و دوباره امروز صبح، حزب‌الله، نیروی نیابتی رژیم تروریستی ایران، با نقض آشکار آتش‌بس، از لبنان به سمت اسرائیل پهپاد پرتاب کرد. حزب‌الله به لبنان خدمت نمی‌کند. در خدمت منافع رژیم تروریستی ایران است، در حالی که مردم لبنان و ایران هزینه آن را می‌پردازند.
@News_Hut</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/news_hut/65828" target="_blank">📅 14:09 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65827">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fPcqEGvBwDpAVSYCNBMxjBA--Bbk7OMYmtMABvPGoBlhNUe-NoiYJAjK_uCisWNxwYubOmZXx_19rLojynd8YHKTClq2E-zbvfY8v28Y_Ldg61CIQP_6FpQuZAD07mguypakOjvGd1PgEv3hoid1mKykx4VGzchWknrR-h8_8yTArN9JWV7IEMI7lyTVCNu06aUMIpTqzydIMHEWdgN1E03wzix-dhdbpYEmA-pFVJYhR9UWN6Qx-DK0SU7J2QzgFmH0v0mTJRpVvb3VDiSRBXusc8LQ1lHJKvpHpFB8GUbFfv6_c6XVgYoYmEvELEwuRZY-yDgAmO-3HfZsShQUwg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
سی ان ان:
هیئت قطری امروز صبح پس از برگزاری مذاکرات شبانه با مقامات ایرانی که با هماهنگی ایالات متحده انجام شد، تهران را ترک کرد، در حالی که حملات آمریکا به ایران در همان بازه زمانی مذاکرات شبانه صورت گرفت.
@News_Hut</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/news_hut/65827" target="_blank">📅 13:34 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65826">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1a59b3948d.mp4?token=YBB3k5sRUy2Eo6dQDvW-0-8s-vWjrvTbZTJQ__-Lo147xE4H51gmiOYKYSecQQ9LeKOeU2VvFU525_X-Jfx9nga9ddPDS8Cap1q2g-fJMhmQsa3Il_lgUXVIaE2cmZ7tNxzwPKeUYRMz_XzxpmvA-U0imt45YsgjGHrCwhGsk-AX7wwjMexiD7wzl1BCuumJFDTE6rhqPzw0nZXHVdXbw-uBqVI83ltbl5-kddujKjkHeZDkiyfkiNOAZv1ZUBciLcixFqOevzezC1-Hty712E7RrkhT6HkpH6WAzUe4kQwkM1OHd_i_3n476DcPDvwjoqsh285jWSR_eYuzH1xXvA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1a59b3948d.mp4?token=YBB3k5sRUy2Eo6dQDvW-0-8s-vWjrvTbZTJQ__-Lo147xE4H51gmiOYKYSecQQ9LeKOeU2VvFU525_X-Jfx9nga9ddPDS8Cap1q2g-fJMhmQsa3Il_lgUXVIaE2cmZ7tNxzwPKeUYRMz_XzxpmvA-U0imt45YsgjGHrCwhGsk-AX7wwjMexiD7wzl1BCuumJFDTE6rhqPzw0nZXHVdXbw-uBqVI83ltbl5-kddujKjkHeZDkiyfkiNOAZv1ZUBciLcixFqOevzezC1-Hty712E7RrkhT6HkpH6WAzUe4kQwkM1OHd_i_3n476DcPDvwjoqsh285jWSR_eYuzH1xXvA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
حملات امروز اسرائیل به اهداف حزب‌الله در لبنان
@News_Hut</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/news_hut/65826" target="_blank">📅 13:04 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65825">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">‏
🚨
🚨
منابع ایرانی به رویترز:
ایران و ایالات متحده هنوز در حال مذاکره درباره یک توافق اولیه هستند
تهران هنوز در حال مذاکره با آمریکا درباره مکانیزم آزادسازی پول‌های مسدود شده است
@News_Hut</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/news_hut/65825" target="_blank">📅 12:37 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65824">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d7dae3f50b.mp4?token=jIp6g-m93i5QqO8BeiJ9Q1Hdzt-YDqIFrN35Bd55fFsFRJQGMsDTvclMlCsu0udSVbd13f4QyQbF2TJFV0LeToSbPj_LzjFoHiebdSL7eoREfOysZ925cdVl_q0nz0H2-PYYciPWC-GeblK33M4aIJIjH9Ggmxb2j6blV-3GEH8k6m4S5-ZkglG1X2v80nuwX4Ut9mhSiEiFoq87_6VyG0lLM5Zp-0oYGpmv20_qbNcqzDeVZEyddfqukaBwuqTGp5zVQIctdJLA3vdLMLHRbcoagec259UZ9UteT-XOtVWpwJk6t54Sp9tH4kKn_UubEkaqeT5jA1heDxyLCloKbQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d7dae3f50b.mp4?token=jIp6g-m93i5QqO8BeiJ9Q1Hdzt-YDqIFrN35Bd55fFsFRJQGMsDTvclMlCsu0udSVbd13f4QyQbF2TJFV0LeToSbPj_LzjFoHiebdSL7eoREfOysZ925cdVl_q0nz0H2-PYYciPWC-GeblK33M4aIJIjH9Ggmxb2j6blV-3GEH8k6m4S5-ZkglG1X2v80nuwX4Ut9mhSiEiFoq87_6VyG0lLM5Zp-0oYGpmv20_qbNcqzDeVZEyddfqukaBwuqTGp5zVQIctdJLA3vdLMLHRbcoagec259UZ9UteT-XOtVWpwJk6t54Sp9tH4kKn_UubEkaqeT5jA1heDxyLCloKbQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
❌
واکنش پزشکیان به سخنان همسر سرباز ناو دنا که گفته بود حمله کنید: انتقام که فقط جنگیدن نیست
@News_Hut</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/news_hut/65824" target="_blank">📅 12:36 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65823">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">1xbet_ir.apk</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/news_hut/65823" target="_blank">📅 12:34 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65822">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">1xbet_ir.apk</div>
  <div class="tg-doc-extra">53.8 MB</div>
</div>
<a href="https://t.me/news_hut/65822" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">1️⃣
▪️
نسخه آپدیت شده اپلیکیشن وان ایکس
🎁
اپلیکیشن رو دانلود کردید موقع ثبت‌نام، کد هدیه 1x_1566529 رو وارد کن و تا
100یورو
هدیه بگیر!
• آدرس سایت 1xbet:
🌐
bitly.uk/connect1xbet
❗️
نکته: اپلیکیشن بدون فیلترشکن کار میکنه برای ورود به سایت باید سرور فیلترشکنتون رو کشور های اسیایی یا کانادا یا ترکیه تنظیم کنید</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/news_hut/65822" target="_blank">📅 12:34 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65820">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b88e4c73c3.mp4?token=qljSAGW8Bv5Gbsm8MDCK4FRDSNmbcenYyWLrlxl3iMganYoaFvfoNW_z_oDA_l8c6e3sag2FwVKSL5iGWqtxD_R8kPhT9jqIAG7BPKSUK92hZr86f5oD1ZUfIQQHRfLPx33WUO2ezr97dBX2kz4ZzKSWLInqNqYRKuHWf-n0nHohmB7P_Nhu_gQqnWdy_v04fEvuz81-v4k9-fgR9oFIPc-_bKLpSAkHU7qPhaMSaoIeoJk__BDpenx_gu8dA7eBjA189y4zo9NYlP9qWqxodzwrFpK4u1OVOW4KvXmV6RoRDftmKZGtvC36hc7A7pC0wW0fpzpqKTalVayNJSTCsw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b88e4c73c3.mp4?token=qljSAGW8Bv5Gbsm8MDCK4FRDSNmbcenYyWLrlxl3iMganYoaFvfoNW_z_oDA_l8c6e3sag2FwVKSL5iGWqtxD_R8kPhT9jqIAG7BPKSUK92hZr86f5oD1ZUfIQQHRfLPx33WUO2ezr97dBX2kz4ZzKSWLInqNqYRKuHWf-n0nHohmB7P_Nhu_gQqnWdy_v04fEvuz81-v4k9-fgR9oFIPc-_bKLpSAkHU7qPhaMSaoIeoJk__BDpenx_gu8dA7eBjA189y4zo9NYlP9qWqxodzwrFpK4u1OVOW4KvXmV6RoRDftmKZGtvC36hc7A7pC0wW0fpzpqKTalVayNJSTCsw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
ویدیو ای از کشتی JALVEER که امروز در نزدیکی بندر شناس عمان مورد اصابت قرار گرفت.این کشتی را خدمه ای هندی اداره میکند.
@News_Hut</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/news_hut/65820" target="_blank">📅 12:15 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65819">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hi7dR4p__CUJVQfmGYfs3YcCTtoiBJ0HAAvKmNC51Zyt2kDGT69B1-l74_29UqFMkDI45_3EJRDzgjN9MruYEXzxDmB9EXEamJVxZdQVzciFg92aIaZWinHHpf8AK9x5IeIEee7Zz6uMy7EBYnF7ctIeJqVDzGTIuGEeXS0Z4_OoipmPRRG59Uev_MT3TxRbIhbn-AvJTlbwd8EJ7p5Vp6mTP0z5Ylo_8-tPGYob2PULW1ycLKD02dBE1h78NeayM6StH53kBBzOtmP7TZFvdBRFrQPe7hYr9DPPg6u8ANkFr8mYIytRnasNBtBWYlOaBRoN-XttxkKDGbhNAxhPwQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
بیانیه وزارت خارجه جمهوری اسلامی در خصوص نقض آتش بس توسط آمریکا
@News_Hut</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/news_hut/65819" target="_blank">📅 12:00 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65818">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2bec45c0e2.mp4?token=aIGiTLtYJIcMCesfmXkYZ16f7UlcgfdTUBafEW2O6SWdgpEWlCpx72uxw6vGnwOrfVtB-LpmviS-NoOnajVa7yzjRUBOieJiuH-wPwIA4SHD0q9qrUF2fUOZtvbwEugpxVJHjCNuN38wvmxIG7yBb-9jROdNl_sraGREyLIVHDeNyi47efSErKGvCX_hCN482eKex_1coO8cIcDSMkvs5HnjeeiGrarLpq85smIjvZie5HFUdaTQxmNIdAXxnrhnec5Xr18_Hd7eNA1axVRfRmJlvhlPMR4s9crPDUCm8aG-vwUtRbvnFmOtkI1Mun_jMh4Q6LEy4IVVW8WqdNKVqw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2bec45c0e2.mp4?token=aIGiTLtYJIcMCesfmXkYZ16f7UlcgfdTUBafEW2O6SWdgpEWlCpx72uxw6vGnwOrfVtB-LpmviS-NoOnajVa7yzjRUBOieJiuH-wPwIA4SHD0q9qrUF2fUOZtvbwEugpxVJHjCNuN38wvmxIG7yBb-9jROdNl_sraGREyLIVHDeNyi47efSErKGvCX_hCN482eKex_1coO8cIcDSMkvs5HnjeeiGrarLpq85smIjvZie5HFUdaTQxmNIdAXxnrhnec5Xr18_Hd7eNA1axVRfRmJlvhlPMR4s9crPDUCm8aG-vwUtRbvnFmOtkI1Mun_jMh4Q6LEy4IVVW8WqdNKVqw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
لیندسی گراهام،درباره ایران:
اگه همین الان توافق نکنن، باید دست اسرائیل رو کاملاً باز بذاریم و خودمون هم از نیروی نظامی استفاده کنیم.
امیدوارم اتفاقات امشب باعث تغییر رفتار بشه.
اگه این فشارها باعث نشه که بیان پای میز مذاکره، باید استراتژی رو عوض کرد. باید با تمام قدرت وارد شد. کار رو یکسره کرد.
بعد از اینکه تکلیف ایران مشخص شد، به مرور زمان مردم ایران می‌تونن کشورشون رو پس بگیرن و مسیر صلح بین عربستان و اسرائیل هموار بشه.
همون افرادی که میگن زدن زیرساخت‌های ایران اشتباهه، باید بدونن که این‌ها اهداف نظامی مشروع محسوب میشن
@News_Hut</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/news_hut/65818" target="_blank">📅 11:30 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65816">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/KA8aS9UISkjk1z4YRHCzWVt3yqieO1cFDsUqwyTt_jIRltPHRLxh69bZUNv5N9HaBStgXlxNGjs4WaNDp91_yPD_svvtnhpO-Gg8iY8HsMYBoHcDtCFBtPehEK9kL75y-cgT_cmy3tRKp1BArdoqnhCzhsjsaW-0_KCG600DNBBuFWRqShTI0bMu9l8_A6LVfl5RCbOEIecDFCtoxQuFFLZg9GwlQEuGIBU09h1ilYw9bA6V1jT0aqsv-wYpYmEJY1fUrwwnQb-Fc0VsnAxpaHrzZn4Vt5iWAaOSftt8W5QfRjjqDIrrI24ZUCnmT9xrfX7oWCYxccvPQn_Uh0I_Bw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/PM_qxV8PvNL72aO9Axjbx1-sCS-qlcCVZ3xsEdoWMoj7avJ0iy1H_VuS3R6n20evzCot0M4OaTaaDbQyaaLrOOGCuip-hdlpgkJ4jnmTMth8Awr71mY4okNKxzS807hKUqOM523Zo0K2x5sgvp1fA7thMShx4LW6xbCJyM3v2_p8U50Eu59SKDgQQfy9UqcChPnaj0HkFEcb4vW5F6a9tLrICLCIUTSXRF0pMpzeUj05M0FIFc5irJ4BCCa3faiGdjVbpJIU_KF7RCbbVxz3OSEDQClSnAuoRekC4wLC5izTVc4qb35Jbtb0xM66U4HDDPVhhaZl6jymZ1aJWkdThg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">‼️
وزارت کشور بحرین:
این خسارات مربوط به حملات دیشب جمهوری اسلامی هست و دختر بچه ۱۱ساله ای هم توی این حملات زخمی شده.
@News_Hut</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/news_hut/65816" target="_blank">📅 11:03 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65815">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mf2UP1nqJ4EGb7SVwLWxLT8F_KmYx9Y5WTmDYZYI04uwKTfuqo4R1tufBoIcKKGwjSSkPOGioqA3Zuorlff6oGr3VmukdxH1bki7tIHt87TqOYlPU-OPAaOYypUK9WL68my4zpzLFhKfmxWmcNABW_hHH__fNYYMgmJU3TNY2JH5wHhqmoQGdLyNa6km-Ct5QXSzhRAACyxQxTesnnVf-X91J4BxY1gfYJor-3PHyFGUgmwV_U3G-4EZm2oJJMvxELGtJ6btTTus-x5opCH344e1TtTIsaiL3oiMkryK1TLlLRkengzHpFJfrJjTy2SzfI_DRQzpPa2LAr4TjyzKIw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
آلمان از پهپاد رهگیر جدید «کبرا ۶۰۰» رونمایی کرد
شرکت دیل دیفنس در نمایشگاه ILA 2026 از پهپاد رهگیر جت‌محور Cobra 600 پرده برداشت؛ سامانه‌ای که برای حمل و شلیک موشک هوا‌به‌هوای IRIS-T طراحی شده است. این پهپاد با طول ۶ متر و چهار موتور توربوجت، می‌تواند موشک را صدها کیلومتر دورتر از محل پرتاب به منطقه درگیری منتقل کرده و برد پوشش پدافند هوایی را به‌طور قابل‌توجهی افزایش دهد.
کبرا ۶۰۰ در واقع نقش یک «سکوی پرتاب هوابرد» را ایفا می‌کند و برای مقابله با پهپادها، موشک‌های کروز و سایر اهداف هوایی طراحی شده است. استفاده از موشک IRIS-T نیز به این سامانه امکان درگیری با اهداف مانورپذیر را می‌دهد.
این طرح ادامه‌ای بر مفاهیم قبلی آلمان برای ایجاد رهگیرهای بدون سرنشین مجهز به موشک IRIS-T محسوب می‌شود و می‌تواند لایه‌ای جدید به شبکه پدافند هوایی این کشور اضافه کند.
@News_Hut</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/news_hut/65815" target="_blank">📅 10:15 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65814">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">🚨
🚨
نیروی دریایی سپاه:
به دلیل نقض های مکرر آتش‌‌ بس توسط دشمن آمریکایی تنگه هرمز تا اطلاع ثانوی مسدود خواهد ماند.
@News_Hut</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/news_hut/65814" target="_blank">📅 09:40 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65813">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">🚨
🚨
ترامپ:
اگر ایران توافقی که ما میخواهیم را امضا نکند فردا(امشب)ایالات متحده دوباره آنها را بمباران خواهد کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/news_hut/65813" target="_blank">📅 09:26 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65809">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from[ 𝐇𝐨𝐭𝐍𝐞𝐰𝐬➕]</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/spmqb-7dPywI7kbsMyxHq7PrGUPZzsJRKUWuW75ATrut3wGp5Fmlc9tmbDC5Ds_usZbOaklKFcYsbt4cudcCH5OAl_SVrB1JUX_ECtRs1NeMbwkMk7cml_-lhE_WVT8_hC4yTwBbLXpjwuYve2QKcWlBgqD2WfBR4C7pu6ooRg8KSyFo4d5XsDtIJpqBjISJGl1WLoXAyw-SHF5NUav-mgCbX4tG_wRNo-xAt2VAWR33hgXCy1V1Gj2nSpwBTa2bTBO6h__S1mSijAJSCCVpgredxy61pZVt7cyX1U5hmUdtXgw5G6a5O0DOBxxdJCZey-ZF-EJNVFm66XgOTnCXkw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/TECsIBC7DxU3MXlI2EYNja3k80bweLis6N8GRZw62tykBDIfy6B8oDRpNebuzjLbiZKWh6YUcpR-MFYNHlxVYUsChhCE6grKJC4Tfv7gIZuawpJDJe1WqxVSkMaAiEmx7KmqE8SJ00p4qgSea7o1E0GeQ2GSKpTavCD6wVfcDwW79gyteNDxNh2tqL95DSQORcvdaGbeV7RSLTVOpy4K2-WUccccxCMxbh32AASo_FT-xlVHiA4xWgK67YDvJkeB-vDuKkhWRUbSAu5fnhA_IJvxBK41f5zsTvsJn0VGUYWZaWsPU_vPut8dIKCKlTbtofLvaEwRkGUSZnydSKUfew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/opoVvuW7rBya147_yOf_t7GQehYtiEL6pKWhNHojwZxB9seyJ2ku1L-x2lTFNg4kzszgBiRYtq7EB_58yRkDjRD6zdS7yM_r4o79i5GaLyqMsDrQOMYDnB9-aRX0esxyVSEoxTjxQRdYyqz8wEQx6f7tp1w_i4rlQCkWsdgqk6NNCAISYCEjFXFOIEwyvkBuzB8HX3-2sd3Q0r6ub9FkyWuBh7s5JOSWfYwrjtLBemJ0AB5IOh2BCrSANPLLpp2AIlhWexnkoIH2NdJktnxyIYeklz8pLWC5zdMUpI00dMlZcFsVVOkyE_tttF2gxxL0aBkNhpIFSJR4ci-E94CEDA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ad9bf04a71.mp4?token=QaXqcleIMzIc86elR-4zrfS_N61UX1ZBKkQhnqfeKIRiN6uPZZg5u5cun9i0Y__kLxPaT_p2numoahG92gHFLmU4QQ91ZcwVe9KQ9fz_Yg9r78a2VSCidRmkwGMJh_XVgUe6z9fqq2bN9XtUInljPDedxL_lIgSt8hW39ORreU0xLn5aeS1ofoxyxD47-Bdv7UwV_5cqM6W_aW1h8Ha_PatcWMZ0-KN0ZFjttrKyixIMXBdBRDPHQhyiLZP_UdbhvBFdx1yHj9G2M63PKbmupucfVoOcf_tHyzD1DRjba-io4hwhWs1h8PtNga67DAmXVMgOB3Ccsg3gqQVq7SC84A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ad9bf04a71.mp4?token=QaXqcleIMzIc86elR-4zrfS_N61UX1ZBKkQhnqfeKIRiN6uPZZg5u5cun9i0Y__kLxPaT_p2numoahG92gHFLmU4QQ91ZcwVe9KQ9fz_Yg9r78a2VSCidRmkwGMJh_XVgUe6z9fqq2bN9XtUInljPDedxL_lIgSt8hW39ORreU0xLn5aeS1ofoxyxD47-Bdv7UwV_5cqM6W_aW1h8Ha_PatcWMZ0-KN0ZFjttrKyixIMXBdBRDPHQhyiLZP_UdbhvBFdx1yHj9G2M63PKbmupucfVoOcf_tHyzD1DRjba-io4hwhWs1h8PtNga67DAmXVMgOB3Ccsg3gqQVq7SC84A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
بررسی وضعیت راهبردی بحرانی جمهوری اسلامی پس از حملات چند شب گذشته و فروپاشی بازدارندگی و چالش عبور از بحران
متنی که ادامه می‌بینید یک تحلیل جامع نیست و صرفا یک بررسی وضعیت است از راهبرد جمهوری اسلامی پس از حملات چند شب گذشته‌ی آمریکا و اسرائیل؛ خب جمهوری اسلامی در ۴۸ سال گذشته تمام تلاش خود را برای ایجاد دو اصل
#بازدارندگی
و
#بقا
انجام داده ولی حالا در ماه‌های اخیر با فروپاشی شدید مفهوم بازدارندگی و حتی بقای خود روبرو شده است!
استراتژی‌ای که بر پایه شبکه نیابتی، موشک‌ها، پهپادها و تهدید تنگه هرمز بنا شده بود، در برابر حملات آمریکا و اسرائیل به بدترین شکل ممکن آسیب دیده؛ من همچنان معتقدم که جمهوری اسلامی قصد داشته در دوره‌ی چهارساله‌‌ی ریاست‌جمهوری ترامپ مقاومت کند، زمان بخرد و امیدوار باشد که در انتخابات بعدی یک دموکرات روی کار آید و فضایی برای تنفس و معامله ایجاد شود. اما واقعیت میدانیِ چند شب گذشته این محاسبه را به چالش جدی کشیده است!
‼️
درس تاریخی و تأثیر بر دموکرات‌ها
من قبلا هم گفته بودم که سیاست آمریکا یک سیاست واحد است؛ یعنی حتی با تغییر رئیس جمهور هم سیاست کلی عوض نخواهد شد اما تاثیر گذار خواهد بود؛ برای مثال حمله بوش پدر به عراق (۱۹۹۱) ابهت صدام را شکست و راه را برای حملات موشکی مکرر کلینتون به عراق هموار کرد؛
امروز هم شکست بازدارندگی ایران می‌تواند پیامدهای مشابهی برای سیاست دموکرات‌ها داشته باشد. اگر دموکراتی مانند بایدن روی کار باشد، ممکن است بخاطر این ضعف، سیاست‌های سخت‌گیرانه‌تری اتخاذ کند یا حداقل نتواند به راحتی به سیاست‌های «تعامل» بازگردد
شکست فعلی جمهوری اسلامی نشان داده که «ببر کاغذی» تهدیدهای منطقه‌ای‌اش تا حد زیادی توخالی بوده و هزینه حمله به آن بسیار پایین‌تر از تصور قبلی است!
❌
وضعیت فعلی اتاق تصمیم‌گیری
اتاق تصمیم‌گیری جمهوری اسلامی اکنون در موقعیت دشواری قرار دارد؛ سوال اینجاست چگونه بحران را با کمترین خطر پشت سر بگذارد و همزمان بازدارندگی را برای حفظ اصل بقا، ترمیم کند؟
تهدید زیرساخت‌های اعراب
بستن تنگه هرمز برای اختلال در تجارت جهانی انرژی
واکنش‌های نامتقارن و کنترل‌شده برای نشان دادن قدرت
ظاهری
حملات دیشب آمریکا صحنه میدانی را به طور اساسی تغییر نداده، اما به تدریج در حال نابودی قابلیت‌های دفاعی ایران هستند و این حملات بخشی از الگوی گسترده‌تر فشار حداکثری و ضربه به تأسیسات نظامی، فرماندهی و پدافند است!
⁉️
قمار واکنش افراطی سپاه پاسداران
سؤال کلیدی این است که آیا واکنش افراطی جمهوری اسلامی (مانند حملات موشکی گسترده‌تر یا بستن کامل تنگه) می‌تواند چرخه فعلی حملات را بشکند؟ یا دقیقاً برعکس، خود سازنده حملات شدیدتر خواهد شد؟
تجربه ماه‌های اخیر نشان می‌دهد که جمهوری اسلامی در حال حاضر در موقعیت ضعف نسبی با استراژی های بشدت هزینه‌زای زیر قرار دارد:
تحمل و دوام؛ یعنی جذب ضربه، پاسخ محدود
انتظار شکاف سیاسی در طرف مقابل
در نهایت، موفقیت یا شکست این قمار به عوامل متعددی بستگی دارد:
انسجام داخلی رژیم
توان بازسازی سریع نظامی
واکنش بازار جهانی انرژی به تهدید تنگه هرمز
اراده سیاسی در واشنگتن و تل‌آویو
‼️
چشم‌انداز
جمهوری اسلامی در حال حاضر بین دو گزینه سخت گیر افتاده:
ادامه مقاومت تاکتیکی با امید به تغییرات سیاسی در آمریکا
پذیرش نوعی عقب‌نشینی راهبردی برای بقا
هیچ‌کدام آسان نیست. سیاست عملی رژیم در دهه‌های گذشته بیشتر «عبور از بحران» بوده تا حل ریشه‌ای مشکلات؛ برجام هم نمونه‌ای تاکتیکی از همین رویکرد بود
🔴
ارزیابی واقع‌بینانه:
بهترین سناریو برای رژیم: تحمل ضربه‌ها، مذاکره تاکتیکی، بازسازی تدریجی و انتظار تغییر در واشنگتن (دموکرات‌ها) اما شکست بازدارندگی قبلی این محاسبه را سخت‌تر کرده — طرف مقابل حالا هزینه حمله را پایین می‌بیند
بدترین سناریو برای رژیم: اگر اسرائیل/آمریکا فرصت را غنیمت بشمارند و حملات را ادامه دهند، رژیم ممکن است به سمت «همه یا هیچ» برود (بستن تنگه + حملات گسترده) که می‌تواند به فروپاشی سریع‌تر و یا حتی نابودی زیرساخت ها منجر شود
در مجموع بنظر من رژیم اسلامی ایران نه تسلیم کامل را انتخاب خواهد کرد و نه جنگ تمام‌عیار را؛ آنها می‌خواهند زمان بخرند، ضربه‌ها را جذب کند و با حداقل هزینه از این مرحله عبور کند تا بازدارندگی جدیدی (بر پایه تنگه + هسته‌ای پنهان) بسازند!
اما شواهد میدانی نشان می‌دهد این راهبرد پرریسک است و موفقیتش تضمینی ندارد و تحولات سریع (مثل حملات دیشب) می‌توانند معادلات را یک‌شبه تغییر دهند؛ بنابراین حالا رژیم اسلامی ایران صرفا در حال مدیریت انقباض است تا زنده بماند و در یک آینده‌ی خیالی به امید شرایط بهتر، بخشی از مردم را کنار خود نگه دارد
!
#hjAly‌
@HutNewsPlus
|
@News_Hut</div>
<div class="tg-footer">👁️ 28.2K · <a href="https://t.me/news_hut/65809" target="_blank">📅 08:53 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65808">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">در ۶۰ روز اخیر این سنگین ترین حمله‌ی موشکی سپاه پاسداران به کشور های منطقه بود  حالا باید از ترامپ پرسید، کدام نیروی هوایی و کدام موشک ها از بین رفته؟!  #hjAly‌  @News_Hut</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/news_hut/65808" target="_blank">📅 08:17 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65807">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">در ۶۰ روز اخیر این سنگین ترین حمله‌ی موشکی سپاه پاسداران به کشور های منطقه بود
حالا باید از ترامپ پرسید، کدام نیروی هوایی و کدام موشک ها از بین رفته؟!
#hjAly‌
@News_Hut</div>
<div class="tg-footer">👁️ 29K · <a href="https://t.me/news_hut/65807" target="_blank">📅 05:57 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65806">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/O9US2izG_4i_y7ZGxqenb7XG-cbkkIqkAaIu-J8rbJAtdCeQBEkdJyxZxElndx22CHJycuc0__N2bOcxecWv_JlgXDPWJq90u1p3hmfgm0JlY7IzvNi4EZaFWdB0z_Ik-EuECZ_0SYT9Igs5N03r3Mt7syDKM4O6UhT0eqkH8jTv9acUKbSXPUsXTncTxgu-5wcWKQKpqGycyZrBUlgp2HVSKfa3Z58p5V0diDPgcS8vXp_23KB4LUNsrOBghzT1dk3d9jPqu6qyCkAI5yS_FqBRH1jNSKcfEsqpZtttNN4VbPtsRdncqZadK7twRa3iQ1XABd1G0gFaUZtcmoXadA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
کردستان
@News_Hut</div>
<div class="tg-footer">👁️ 28.4K · <a href="https://t.me/news_hut/65806" target="_blank">📅 05:40 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65805">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GkIqi2emlNpPUaWsldX06S6Cz8bx4Sg7uCr9n7Fd1eS_ss3uFww03stY8_Bpwi-oaTIqigDtf3yr5fwfCYjmeFORcvqNPmajgMER2ppa2eeW0CyH59vJcbR1u_sx9e5HqcB1Fmk3c56-9SRFPGF6kNU7rlrlWiw7x855nKob1_Q0cVyCq0m2speGGvRvL2_d9gvKTsd0osQL3sf63ePDinelXMf0KKoFhzkS5p3fPbyDaO0zUqt-_Nin5bpHgdfcg0b6dj9mwc3EEEtVRsH9i9F5OvINYX2l_GYKgR2J6TOdYSeiKrtLK5cISIctF7nO9Vo66hve5LVAH-nD6yYk4g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
ارومیه
@News_Hut</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/news_hut/65805" target="_blank">📅 05:40 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65804">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cl63M31qi8rGcfupbYTFXAsdbl4n2lkHvLT-NLQsKxDAx-R-C_5KXiShVkmmaqdx9mjl5_S30NthBCA8SnfjDqrD_xNSjBV_Byc77zqguZUuo7_hZyAGwuMG3TRcwreoVzQN0U0tOXKvG5_VuiD-z2iPAxfNrmFHAgLSfGJqmVDn8QrLsaS2Gw6ucRIxCqTSkz-ZTp7Jm9aQ9U5t8zQ3HkkHOEELOvATMQ3vUj93jVAHG8Nt3uvQp-VFbRKJqovcvPn5rYHk7vpqY6BhflA_LqkAF0Xt26RPMFPBjLFpE8EkC74grOzQ6NmIZztOkKcqfdtUxK_oWh_zTLg_J1e4QQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
تبریز
@News_Hut</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/news_hut/65804" target="_blank">📅 05:37 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65803">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KL0PEaFbw0-yyLq8f3ncKj0-XAFpk78dk_bF39H-2pMG8fsFVnO0B84-u4gsyd9ssSywsrl3biTyE70aUos-b_YC2t4YdCCyX5vRi8X60lLMK9tE8p8QJ1NFBz8LM4PPVk37tSygYQZDO7-QzT7WhRVurXw9tvMD43EWWkaAUejsFRC3yKc2acNnVZWvdJuECS_j3BiDJpxJUZx3JLqFxOKECOZk4vzVGX_8cAoZS-a_Pm6Ch_iL2R0PztETiUTFv1rDclKf6XftV_uOXOHe_Rh90b2hmoW8NacbghCjj6F9qAxWCfDbinCCuRHpQurfegXJyNwIfu6lt3RAGaW4bA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
زنجان
@News_Hut</div>
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/news_hut/65803" target="_blank">📅 05:36 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65802">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AAx1SfjZjpf2Rm5S1DWBZSxwGJ7WGnC8M29_x661Szo5HBRPfkBCycH7xeFiVIILQj9AOvJzWApsuHASxsSNUIMS-dWOC4O0YPwVIE3H3hPJhX9OXhBka4GR0GZ_vYcUAAa_XYtNo9_9j3D_aFtYZHmMAp4uYrqMZLh_akquAi59xiNWSRrKom4T7RUMxtyVC44_Lmseof6XjvD4iRbFmNF7g65FQQvgZxtogdf9-hUOXwz91QuDtPL6LsBbfAnzYxfHotptJp8o8Xfija5q-K54ST03WKhDW-jmiyKvJYapn7gv1TFxdxubo_8JtSNGgfWjadZU-2dHs1Tmkitozw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
هم‌اکنون خرم آباد
@News_Hut</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/news_hut/65802" target="_blank">📅 05:36 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65801">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">🚨
🚨
🚨
حملات سنگین سپاه آغاز شد
@News_Hut</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/news_hut/65801" target="_blank">📅 05:35 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65800">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">🔥
فیلترشکن پرسرعت و رایگان اسگارد
• نسخه 3.0
متصل با همه اپراتورها
✅
کاملا رایگان
✅
بدون قطعی
✅
بدون محدودیت حجمی
دانلود مستقیم از فروشگاه گوگل پلی
👇🏼
https://play.google.com/store/apps/details?id=com.vpn.esgard</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/news_hut/65800" target="_blank">📅 03:00 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65799">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">فک کنم اگه هرشب با ۱۰۰ هزار تومن میومدین چنل بت ما ، شبی بالای ۲ میلیون سود کرده بودین مثل دیشب:)
😊
😂
میگی ن ؟ بیا تو چنلمون و ببین
🔥
@FutballFuckBet @FutballFuckBet @FutballFuckBet @FutballFuckBet</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/news_hut/65799" target="_blank">📅 03:00 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65798">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/IGbsaXyyv6d1bAyvb9BUmjE-jo0Fz4ilnO_TqKXdvvsm_khg_YdCZNcJtJsCEr0ZeHvMazF2KnZnrtlEsWVtn30C860oXntGpiP-1PPv84cbwgOjsQwuGPoCobxjvKJQ8-a3BMmz-eFtHRTlYYlZqOBTX8Uim9lP0_fgHFLBTi6RdLOo6RsL-B76BkQOy2Xqjk59j5D7-au1R2SdQlfwAw3HTmI7UeO0bsT8faNOBaekSs8-JncLEe7SIzGuyyIepUpwF4Ww5R3kZ-BNxXvpjNpLc49xquULwHlbTjvpdqYUXNX8RZrY5R5ac00qQ_AhchAZqHqZKpNiWyCdg6lgwA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فک کنم اگه هرشب با ۱۰۰ هزار تومن میومدین چنل بت ما ، شبی بالای ۲ میلیون سود کرده بودین مثل دیشب:)
😊
😂
میگی ن ؟ بیا تو چنلمون و ببین
🔥
@FutballFuckBet
@FutballFuckBet
@FutballFuckBet
@FutballFuckBet</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/news_hut/65798" target="_blank">📅 03:00 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65797">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">🚨
🚨
ترامپ:
اگر ایران توافقنامه رو امضا نکنه، فرداشب به بمباران آنها برمیگردیم.
@News_Hut</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/news_hut/65797" target="_blank">📅 02:59 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65796">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">🚨
🚨
ترامپ:
مستقیما با مقامات ایرانی صحبت کردم
«بمباران به زودی متوقف خواهد شد»
@News_Hut</div>
<div class="tg-footer">👁️ 28.2K · <a href="https://t.me/news_hut/65796" target="_blank">📅 02:55 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65794">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">🚨
🚨
قرارگاه مرکزی حضرت خاتم‌الانبیا:
نیروهای مسلح جمهوری اسلامی ایران به هرگونه تجاوز و شرارت ارتش متجاوز و تروریست آمریکا در منطقه، پاسخ کوبنده و قاطع می‌دهند.
@News_Hut</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/news_hut/65794" target="_blank">📅 02:48 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65793">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rlraOOpD_smhLHieFnv_wBsCJnTcdLnOgo_W0na0oEXoqBrw5Nj0hkVwuXCNKscV2P59xXfKbeKRyCSKIxUEdTiZOqBkK6bdfUQtDKuT62boFhejXvAwlQWRg8Qv8mZPHMBEvkIpvXjO9o3-c4Hh7PWBL29OVTU3HLQuD6Imb7EGM6f-t-oaxTwJHl5VFfmiJ8Ct_LBQm2E-COEec_Z_LIaVlmdN6vL0QUuM9rcC75i_F0xZ6tqcwM2W-exLgZy0MF_IsGMJz657QfS4bwbMQqaXPAF9iLOait0VspcL9oi4zSBMC9ar_0cCdGtQPxWvQbJa-zcV8qKEOfDmqNVTAw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
مارک لوین :
دور دوم حملات به ایران همین حالا در حال انجام است. من کاملاً موافق آن هستم.
من درک نمی‌کنم چرا حملات ۴۸ ساعت پیش اسرائیل، که در پاسخ به شلیک ۱۱ موشک بالستیک به کشورش بود، این‌همه انتقاد به همراه داشت!
@News_Hut</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/news_hut/65793" target="_blank">📅 02:45 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65792">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">🚨
🚨
🚨
گزارش هاازانفجار در بندرعباس
@News_Hut</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/news_hut/65792" target="_blank">📅 02:43 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65790">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">اگه لازم باشه آخوند حتی تا دوسال دیگه هم مذاکرات رو طول می‌ده، ترامپِ جاکش تنها راهش اینه یه لشکر ۱۵۰ هزار نفری آماده کنی و تو تاریخ جاودانه شی
🌂
#hjAly‌
‌</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/news_hut/65790" target="_blank">📅 02:30 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65789">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">🚨
🚨
نیروی دریایی سپاه:
دو کشتی که قصد عبور از تنگه هرمز رو داشتن هدف قرار دادیم.
@News_Hut</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/news_hut/65789" target="_blank">📅 02:27 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65787">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">‼️
بزودی  @News_Hut</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/news_hut/65787" target="_blank">📅 02:16 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65786">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1713aa9451.mp4?token=Td89Ph7yb2MbsLXnoW_MjN_9g3quoRbCkQoLxUFpKYUWwQrVBuRPN97hjcYPJ6dkBj6jPEq0ZUhmH0S-TXv5QRHfbVD1IpJ_6s6k2X0ID4gVqvai3jcbXhViwpp-V_i3f6fotIeRY9k_rjvgQfFQ8cpOkN28zTZrhnx384rVS7fixa9j7PCpGXmroVdqlJ_ttcOMIbMm6KXgW-lFdKmrQ1B2Y-NWp23mHjPxh50zhlKhMF8yb0SypC1D4nJilzXiPT_zCkxlQrsHBDHzml-j4ZerC5YS1eXjTzEV3X2FFP6FEjl6GP6uvZUETpwLwrSnAIvXzu0Y8TwvRrQ2YEK6Sw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1713aa9451.mp4?token=Td89Ph7yb2MbsLXnoW_MjN_9g3quoRbCkQoLxUFpKYUWwQrVBuRPN97hjcYPJ6dkBj6jPEq0ZUhmH0S-TXv5QRHfbVD1IpJ_6s6k2X0ID4gVqvai3jcbXhViwpp-V_i3f6fotIeRY9k_rjvgQfFQ8cpOkN28zTZrhnx384rVS7fixa9j7PCpGXmroVdqlJ_ttcOMIbMm6KXgW-lFdKmrQ1B2Y-NWp23mHjPxh50zhlKhMF8yb0SypC1D4nJilzXiPT_zCkxlQrsHBDHzml-j4ZerC5YS1eXjTzEV3X2FFP6FEjl6GP6uvZUETpwLwrSnAIvXzu0Y8TwvRrQ2YEK6Sw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
بزودی
@News_Hut</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/news_hut/65786" target="_blank">📅 02:13 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65785">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">تا الان ترامپ هیچ اظهار نظری نداشته و حرف هایی که بهش نسبت داده می‌شن فیکن
#hjAly‌</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/news_hut/65785" target="_blank">📅 02:12 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65784">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">🚨
🚨
شبکه ۱۵ اسرائیل :
موج اول حملات به ایران به پایان رسیده.
@News_Hut</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/news_hut/65784" target="_blank">📅 02:10 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65783">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">🚨
🚨
صداوسیما به‌نقل از روابط‌عمومی سپاه:
گفته یه جنگنده F16دشمن رو زدیم
@News_Hut</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/news_hut/65783" target="_blank">📅 02:08 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65782">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">کصننه هرکی نیروگاه بزنه
#hjAly‌</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/news_hut/65782" target="_blank">📅 02:05 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65781">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">🚨
🚨
🚨
#فورییی
؛فاکس نیوز:
اهداف بعدی نیروگاه های برق ایران.
@News_Hut</div>
<div class="tg-footer">👁️ 28.3K · <a href="https://t.me/news_hut/65781" target="_blank">📅 01:59 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65780">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">اسرائیل هیچ نقشی تو حملات امشب نداشته
#hjAly‌</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/news_hut/65780" target="_blank">📅 01:57 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65779">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">🚨
🚨
🚨
انفجار های مجدد در بندرعباس
@News_Hut</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/news_hut/65779" target="_blank">📅 01:55 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65778">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BRWFQYXmuWRooQqK3C0yZPLbbt6QJFRQXV6xYZmMOs5yW3fZ9Bkw1rvzbPAYquF2UsV7laT55BD2bvJYtwzfQ4JZbo9X9tPrVghByVmrq3MlGTotXiNYLR64_ykfiPoUVPB-utrOBr9JyhO6ggUAl1bqrsNFIzylnJrMPbe9mFWzN0i4uK7IZb6zD7frmt-jDHfuoiFc-PmZ3iB8fFnwz0PuVcYm5bcoNJmUoUzaikfLgfRlkVGf4mjmPrXtHqZErax4Xt3ihCNGi0DMveAV6WgdQhIznsaCGbPEi6mCGXSu2diXk5c09nh35tJw8Kft_Ku6HzyJX6b1VbjoIYSHug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
یدیعوت آحارونوت مدعی است که یک کشتی جنگی آمریکا در تنگه هرمز هدف قرار گرفته است
@News_Hut</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/news_hut/65778" target="_blank">📅 01:54 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65777">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XKi0vqQTVODOPH-f8IOdiCHyojkvtcwpcGLw3ftGI2_wWTMLTnI6F7Nn2IPtBm9c1JBX9yNYyCWMU_kR_ZUqL1j5IU8QBDxiSJnUhAn43oWk0DszWUNZ9O0v5JOI8ojy0Lhi67jFmXLVacBDxAn8KCdlvd4ikX5Mor5DiJKcBHnsspZyBjn6fNqgp3XLvBjhxc5qeH7FuL3SIRghJGWwIHpTNIMRikcJHV3rJMPLYrn4jTBr-SAIliRlIoky_LApVbm0nMYeWj3BE9QOcEnhOMqNRsuT-fd2Qbh7X3VuPYyzMFX99Jc4dPoXLKp8XeE6Iwglpv6uliqNTOvtVT3q_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
خبرنگار المیادین از درگیری و تبادل آتش در تنگه هرمز خبر داد
@News_Hut</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/news_hut/65777" target="_blank">📅 01:51 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65775">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/sqDjwxyqGx1fQBMcHxn1FeovWTorYmu1SvdSSOosByqyP_51DTUG9S2x11hyW9EYECVY_tBRiZFZe5ZBeBP5fF1cxYFxTZWO7ZG5hN-2m4ppXojp5huWkklvc7nBgeQekqlD64n5wxyrAHuKMGfNQvMR_mynL5GKh3JbjaV7_98QhY0GGfI4NDpqEWUH290qOvQl2QyOUD3yuh5XjN81jDxumaj8baxseB40llEfWSokzJbHGpe4iDeA9UUdsgaByHatH_Y2YTp5D0AAQCASvY6YMtNmTIyuNNOJHbSSv9D0hxi2FlEaZD4fF_aSxDVgSFAIrpTp7Z3u84W9bxzRwQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/sHPhoEGl2txAaaGwa7XHfQeMIgJYs7t9r4MgOvVyWC7SaupTqPpAlUDbQubTG60GENd6cywXIW3T4RB-n-DC5kCRFE67F23a28xHWJHlrmNqdaDhL94T9HxjeDxUGFqetacQcS-F4JIQF1z24isJXtn9aTNBADVYVSt6ZKMkOrCFUE8Z0-Ypvyyk40fAjd1PSwxc-dZnLOdah4GYTmTR3DZKpXyxOK-LeciDe2DbDTrXY9EizVqJzwVCXsdYNCUtYYznnjjAGQp9pqekOC2oSaqXD40i5YJCkiMxiLXddnBk6tja29tIm4Q87XdQcCJUM6pNNWoqsup-GWbf7NWKLA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚨
🚨
دو فروند هواپیمای سوخت‌رسان هوایی KC-135R «استراتوتانکر» در حال انجام مانورهای سوخت‌رسانی در جنوب استان هرمزگان، غرب تنگه هرمز هستند. این استراتوتانکرها از پایگاه هوایی پرنس سلطان در عربستان سعودی برخاسته‌اند
@News_Hut</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/news_hut/65775" target="_blank">📅 01:45 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65774">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iM3OMwWTcyqQd07evobKgXfDeSArsDhC2t-qwNYQ1XLNfuPb1c6sBnBzUNkrLgqTbJ4coOTlTZAV-E8gw5aCimaj5UItOTy1nITNXA77n1GfXQa78BuMjeACAcTK-9qlHB-gbUEhRBvvBTR3vMKSjbYoym4gsfQChzQTXL38vqBOYjvnmMXU07uV_wbuBrvEfICE-egn-PeahuPkqQyJMt_n95cl8y2DQxMnqoeN3A-8ZQWjIQM0Aa8ojaTY-kItiEyZAR78vVGG1JKbf5dKVe3xT-_PJvJIEUy-zEgTgXsFxY2aWU4WQQtu4wUnk00GfbxM4prb6knf6iz9_9_y6w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
دود انفجار در سیریک
@News_Hut</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/news_hut/65774" target="_blank">📅 01:42 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65773">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4bbd6f07ba.mp4?token=pz5oSzqpy-tE19hDwC4-kjC-Zrb43B8bpJDgAO17DT3kCjtBk6RNEO6_h3UDy9UiDf4lQF0FDfQRRgT66YjdMJK2JRWHz8m8Ny5gOitmIuR6gpWPkC6dNn3iqJkZeAxP5LuJFAC-hQu_NMje9Qlf9GWzj9BGI_w6G93Eq2xlGiBb77-3ZdOhgfu1ve9WzzK1LJRv_Y9WjsKzeLRUt_o_Oa7Vw2zu5stJqVyTs0nGeMDQmAEDZGY-wPVIlyX2dpSeESsR7uHKXqu8FB1UZtVCVHuTUx63QiUUBqyQBeUP8GkdKJ0txCblAacNdCCbv9_70cRzO6JnePQTdfRrxe9ejQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4bbd6f07ba.mp4?token=pz5oSzqpy-tE19hDwC4-kjC-Zrb43B8bpJDgAO17DT3kCjtBk6RNEO6_h3UDy9UiDf4lQF0FDfQRRgT66YjdMJK2JRWHz8m8Ny5gOitmIuR6gpWPkC6dNn3iqJkZeAxP5LuJFAC-hQu_NMje9Qlf9GWzj9BGI_w6G93Eq2xlGiBb77-3ZdOhgfu1ve9WzzK1LJRv_Y9WjsKzeLRUt_o_Oa7Vw2zu5stJqVyTs0nGeMDQmAEDZGY-wPVIlyX2dpSeESsR7uHKXqu8FB1UZtVCVHuTUx63QiUUBqyQBeUP8GkdKJ0txCblAacNdCCbv9_70cRzO6JnePQTdfRrxe9ejQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">#hjAly‌</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/news_hut/65773" target="_blank">📅 01:42 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65772">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">🚨
🚨
🚨
وقوع انفجار ها در قشم
@News_Hut</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/news_hut/65772" target="_blank">📅 01:41 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65771">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/redBu9KhjjxY0VNBkXwL6VD7ma8EPodVpx8tAdK_JhHINsADKRFDn75M4DqYerYBYDl-MYZgUJlUGTJYDUcoZM4ookHaSUKwM-F0VhHN8S20WErULOtyikygF3lqCu1eSiRqeHVNvhOmp3bs9Ph6ZsstP14_abRGoEeL8wPt7yKaInklF6wWmOAq8aYQnyKyJfpo6xRQeeSlxTlqyJGIhKZVQgKc9O24ZxAafqJ3SxNNhVL8jnMOdryn3ZXe99rGumPSO2DRbOSXhza03DfqkXraGZtCmcAuogozLSIwECdkSRFhdeOBNeqWcUrcnhOImqGoL3HLzKrtfipJgZvRlw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
توئیت جدید سید مجید موسوی
@News_Hut</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/news_hut/65771" target="_blank">📅 01:41 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65770">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">🚨
🚨
گروه هکری حنظله وابسته به سپاه:
آغاز پاسخ ترکیبی، قاطع و ویرانگر اتاق عملیات مشترک فرماندهی سایبری حنظله و سپاه پاسداران به دشمن تا دقایقی دیگر رقم خواهد خورد.
@News_Hut</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/news_hut/65770" target="_blank">📅 01:38 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65769">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">🚨
🚨
🚨
حمله آمریکا به پایگاه شکاری بندرعباس
@News_Hut</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/news_hut/65769" target="_blank">📅 01:34 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65768">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/OTkUOyTO1d0MDZYfs11gtJbSN8xdlB5S5z9WrU4-ypGxpDIlVr0pShqfLR9BU2pjfuXysYCA6l_WxiAlPsE-ZyIMqWXMkc5nz2UQZXmjoUpjqtly6D1KabIv3rzDc9JjE77hOywidSuwSda0VJVWD-iiKqOY54_9AlkrCDjApoNXwBuOA-TVvFwaNDK4UbyFCJ4sI6LhckwKKde-u_owmvcEonoRq9bYfc5KBybeazW2JuEoibExuxhZHR2q64OkNu1nmB11neIAr2Tqb3fA8Gm4L3by8ptQ8mSo6gDRS7mcuxk5GgAvzQcReJY_8-dVqfvG36S6lhzbQIPVdkWspw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آقا قدرتنمایی کردن برگردین حمله کنسله
😖
#haa4m</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/news_hut/65768" target="_blank">📅 01:33 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65767">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">🚨
🚨
🚨
خبرگزاری مهر گزارش داده که میان نیروهای جمهوری اسلامی و ایالات متحده در دریا درگیری هایی رخ داده
@News_Hut</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/news_hut/65767" target="_blank">📅 01:31 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65766">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bVKEUG23IIwMYacEkIYSt8HxV0o9ATZP64Kf7rh3A9VZhZPdVp_1mU7Hh7TcDXaiav73zwz5DXZOVqwX-PeNZk5WIKdZIGiZgkUMYiXzUtvhbYTZoYhwjOrtvBjjtjZ4h_QBtAVRgv3nCAJ0Y_AS6fpl51Lih-DYCsYMlt-PJP7SW3BDgS01JQya6vBRK4P2x079G7lq7wmhQ2ZPREtsRKOipkIiC6Ln90Du8UbJjv_2ZA6nDoAEEkqt9X2ZS1SwyO6nH7EPrzg7Y6had3_4uNJeyEcvlbK1A_RBUrg73QP-X5YRGQ0R6u7jCtvB_LFYmeZ8W6SfQwcHJ0MMyAQRgA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یه مرد باید با موج انفجار کوبیده شه به در و دیوار، نگرانی چیه آخه
#hjAly‌</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/news_hut/65766" target="_blank">📅 01:31 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65765">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">🚨
🚨
گزارش ها از حمله به جزیره هنگام
@News_Hut</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/news_hut/65765" target="_blank">📅 01:30 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65764">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">🚨
🚨
منابع داخلی:
تا دقایقی دیگر پیام سخنگوی قرارگاه مرکزی خاتم الانبیاء در پی جنایت آمریکا و نقص آتش بس
@News_Hut</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/news_hut/65764" target="_blank">📅 01:28 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65763">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">🚨
🚨
وال‌استریت ژورنال به نقل از پنتاگون:
این حملات نوعی اقدام از جنس «دیپلماسی اجباری» است که هدف اون وادار کردن جمهوری اسلامی به ارائه امتیازاتی در میز مذاکره‌ست.
@News_Hut</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/news_hut/65763" target="_blank">📅 01:26 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65762">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">🚨
🚨
فاکس نیوز:
موج‌های دیگه‌ای از حملات در راهه و درگیری فعلاً ادامه داره.
@News_Hut</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/news_hut/65762" target="_blank">📅 01:25 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65761">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">یه انفجار شدید تو بندرعباس همین الان رخ داده #hjAly‌</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/news_hut/65761" target="_blank">📅 01:23 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65760">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">یه انفجار شدید تو بندرعباس همین الان رخ داده
#hjAly‌</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/news_hut/65760" target="_blank">📅 01:23 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65759">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">🚨
🚨
🚨
شنیده شدن صدای انفجار در بندر کنگان
@News_Hut</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/news_hut/65759" target="_blank">📅 01:21 · 21 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>

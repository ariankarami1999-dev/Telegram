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
<img src="https://cdn1.telesco.pe/file/szKxsa23Py-3OhHntADxWHwd6xAzOvkz989j51tKlNca2OTO3Wtzf4etzy9z4nGKGS7XxGqqnPDbajQ-lfEcRmWEVFREr9xQfg_FVbhAUE5aLu0KY2tr7bJRIDhF2GUEYuEIRNQ3iZqG4Vs0cN0jc9u_-OFI8eB1yX_-PYTUic0HT6QQ-MABuqoa954FH5CBS7b7cCfAFW9nmSSg3Evhql0QCfSbvOE-tFNKpomaJbGpg9qyY_y10hBRqjHuUHbkODNuKScKHeZXADLFeQk1kZZj4T_p3qwvXHNenVMVnG3WHbc0krvGj8qLlrmTGFpIVp7c4bVGkDlHeehoDx3WKw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 IRCF | اینترنت آزاد برای همه</h1>
<p>@ircfspace • 👥 97K عضو</p>
<a href="https://t.me/ircfspace" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 این‌کانال با هدف دسترسی آزاد به اینترنت «به‌عنوان یک حق شهروندی»، به‌دور از هرگونه وابستگی حزبی، سیاسی، تشکیلاتی و ... فعالیت میکنه!https://ircf.space/contactshttps://x.com/ircfspace</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-07-21 03:10:30</div>
<hr>

<div class="tg-post" id="msg-2672">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/BDHWKh7lzEsKrCHtwDDfMyi2gkvfF3mKprVlwqjWbip5uSPhTMxzEotx8DaSMbBw6pGyRFBRSLJXaw_Uq-BEOJ8clmc42J_df1aTK-DQkPDgNK1cfqlV4GD0pjEQCUYw-1THKUAz8Jlvq6m-hh2wwltO7qvxF5OZNkRlSFw2znSMnF7mjwacwWlDxwMPTcxcZd4D5_s7Y1pFHzvIR6B5RjKQnLDpEMZFl4RXHqpx0mo5lqhCvKlykuBOXDcL8TD9xB2ZbWary6NG9oKOrlzuCm87avejFdivxgXTXIHHuSUCdzwdn4qLR3gkAi9DH8ByrMqPUJdm6Ca0y4i2spBJBg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فیلد مارشال محسن رضایی: در صورت ازسرگیری جنگ به کابل‌های اینترنت و دیتاسنترهای خاورمیانه حمله می‌کنیم /انتخاب
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 9.92K · <a href="https://t.me/ircfspace/2672" target="_blank">📅 22:12 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-2671">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/B2VXfNAFNIsyjrodY7LSclJNGjzK0nP5sAcsd-FWjm7VpGCHi7LTdRMQarVUR5FUR9TofWuroB7DcHKdjFny7VcEdg-qR3ZPNOfmJTltqS8RwW7N1lDl3GA9MhjK7b09TUOF2lfzkI4bQ9qG_TecTqD1m3sFiYEYCz7KIVhvgnib5GwDukzDtyslTu3zah4Y7EfyP-3p0XlILuYf5w6ETwn0iQmd3AN-l95CmYQ2i7VVLSJgOByQMFjGRKa7VQzA4zGiMvqJEFMpx_1_muxcDDCs0AvywbHzkRO4v-1h-XHYE9wOgXlmkvmKKsmIfH7x-26DGws7Yl0IbozDTHfkmw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نکته‌ای که در زمینه
محدودیت
دسترسی ۵ پلتفرم رمزارز به خدمات برداشت غیرحضوری بانکی وجود دارد، اختلاف بر سر نحوه دسترسی نهادهای مسئول به اطلاعات کاربران و ضرورت مشخص‌ شدن هدف جمع‌آوری داده‌ها، حدود دسترسی به آن‌ها و مسئولیت حفاظت از این اطلاعات است.
پلتفرم‌های فعال در این حوزه پیش از این گفته‌اند که بخشی از فشارها و محدودیت‌های اعمال‌شده به پافشاری بر حفظ حریم خصوصی کاربران و خودداری از ارائه اطلاعات بدون شفاف‌ شدن شرایط دسترسی مربوط می‌شود. /زومیت
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/ircfspace/2671" target="_blank">📅 22:03 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-2670">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/R9gogQ0n4xEhzBQYfSilNhH2PsisI9G1b50pfV4Jm5DVHctvPFAOAkpMUMKB5ETNqXXpBWBUtApxMXSnu9fCBE_BDvOEJUCMTxeHW50xvuinPyS_C14TD-FJBz0nYrqBL6q2hIbWIQ0rgG16m6ijp9qGSfQhqdro6c2FgU5AD0hmGTzWNm8_E6Bf2oBzh3sNCvdxFBXlW9zBOcIwza5Z2hOg5o1aJDG4MzeLN3aq4SJGiozygr1E7sL_IdZ8GjztZOl0bzAYyXb0EpYar408IYw7G01urFaxbWoc0YCPF7e3uUVh3KAQ8R5XCMOTm2Rakzcw2E6NGr6O0RxknGehXQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‌بانک مرکزی تسویه ریالی ۵ صرافی رمزارز نوبیتکس، بیت‌پین، رمزینکس، ارزینجا و تترلند را به مدت ۳ روزه محدود کرد.
دلیل این تصمیم تخلف از ابلاغیه مربوط به API اعلام شده و می‌تواند فرایند برداشت و تسویه ریالی کاربران را با تأخیر مواجه کند. /شرق
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 9.86K · <a href="https://t.me/ircfspace/2670" target="_blank">📅 21:59 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-2669">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/UTm7pKuQumdXJxt56RC10nD5ErJ1voTLvTSD5M119SJ82IEJd0c9fLIACJyPuROb3R0KZoIWK68-vRQfK8vqaL9ZsKPRMwmaI1p-Yb65BgeHTd6zqtbbp-213HvG4TBAXQpQ6wcfnpwfkXK_shXZKx5liR14d9ShwM4WJfJaZNAyeyblbRwmw5Mjs9Ys01s4wa9EAjfEXK44i_aIiLiark1sBVYL1i_WZNvj_yp-3PXrRG9weeMn6R7ykwPAKbI9lgiJSnmqs5JdY0S8mCjiBnagbwE5EeWWCj3rgpaFcHB0kY-RyAJB-NFcbJ5Nn42885Pk2F_wsnZXReK2tvuNTg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در آپدیت جدید از فیلترشکن متن‌باز و رایگان PyWarp که برای ویندوز، لینوکس و مک ارائه شده، امکانات بیشتری برای مدیریت اتصال از طریق وارپ لحاظ شده.
حالا می‌تونین بین پروتکل‌های وایرگارد و مسک سوییچ کنین، مسیر اتصال رو هوشمندانه‌تر مدیریت کنین و از تنظیمات پیشرفته برای سازگاری بهتر با شبکه‌های محدود استفاده کنین. امکان مدیریت حساب‌های شخصی و Zero Trust، مشاهده کیفیت شبکه و بررسی خودکار بروزرسانی‌ها هم در رابط کاربری جدید این‌برنامه قرار گرفته.
👉
github.com/saeedmasoudie/pywarp/releases
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/ircfspace/2669" target="_blank">📅 21:52 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-2668">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/mKW-bKdcyc8bkTj_st5rMseGjii0E6_7CIyLYiKAoF7erk_gtJYWWb6GXeq49neG_7l9cYCojzSRlw7Y47uGd3jhHz-uJ7lsKA6OsTAqtIrFNW8zJBWbhUmPa9N5471kAyFLCH417Gekd0rdI52op7vXNiZZNTc-GmbdAroMGf6m4s6VZMtVDk_xU9I4T3my2QCAKbSVLpXe6VltFbQwXyjkUss2MOAT0VFAmnAXYSXoExJC1rU2RnvJ38lOUkhmkbSfjY4FJTHX4VW-0uCkwUyy4QvqYG76qbQq1uez2VJZ57dXOLtzGSS-4_VkdDy-LHf8vAwFmodnIDNaDVY4xw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">روی حماقت امثال شریعتمداری حساب باز شده!
حسین شریعتمداری مدیرمسئول روزنامه کیهان: آیا حق مسلم ما نیست که برای به زانو درآوردن و قطع نفس این جرثومه‌های پلیدی، مانع عبور کابل‌های اینترنتی از عمق آب‌های خلیج‌فارس و تنگه هرمز بشویم؟ کابل‌ها برایمان دست تکان می‌دهند و با هزار زبان می‌گویند چرا نقش ما را در این جنگ فراموش کرده‌اید؟ /اکوایران
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/ircfspace/2668" target="_blank">📅 21:44 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-2667">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/jtW2W0gRiC0V1OOCqC7LfifowcDCVYX2f7Gv3AMrHBndSNXOaEC0a1YT8zZLyeED2jdOqQ9C3Q_pscmjXcoDBw95R1EcU1e5l40nMX3nFSeJVTjPh3zhscPfrehQ9ZchiYFph4jtPa8ht8ajgNihE2vn0I0lYJufhwsGC3y2cnCilWpBidt4QuQZWcbJ2wA7JgQyILeOKKTjaZFEb5wjq-xZVDu5xhUyFcPNwdT6JaBcHIcOWHrSnEkbNTT6HOEesg4JdfSdY3wrYbvRvAvDNBS9gI1UQVnqKXKWRf47OCbpB_xcsXDY1pyAuz7fxVfPtPoIu0x9mF2Ruclqt9MBag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نسخه CLI ابزار متن‌باز و رایگان GNet برای ویندوز، لینوکس و مک منتشر شده. جی‌نت که قبلاً بعنوان یک اپلیکیشن اندرویدی شناخته می‌شد، حالا با نسخه خط فرمان، امکان اشتراک‌گذاری اتصال VPN با دستگاه‌های دیگه رو هم فراهم می‌کنه.
با GNet CLI می‌تونین سیستم خودتون رو به یک سرور پروکسی تبدیل کنین و اتصال VPN رو از طریق پروتکل‌های HTTP و SOCKS5 در اختیار دستگاه‌های دیگه قرار بدین. به این ترتیب، می‌تونین ترافیک گوشی، تبلت، تلویزیون هوشمند و سایر دستگاه‌ها رو از طریق اتصال VPN سیستم عبور بدین. این اشتراک‌گذاری از راه‌های مختلفی مثل وای‌فای، لن، هات‌اسپات، اتصال USB یا ... امکان‌پذیره.
👉
github.com/frank-vpl/gnet-cli/releases
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/ircfspace/2667" target="_blank">📅 07:47 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-2666">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Y-8NwBcAaI7Y12dWPDNNSjAQ1Tcftj21PXoUNiETItWz_UlNgdwl5SBkqgR3NEaaJbbSb7TxnRDK_ModItq_hmHt0NXT8MkojWfRFWUzT1KauBwST9z61aHtdqR5gyj4lF2zpYsKLeE07rXu5M2m0Q-Y_rK96d_EwggVg_2CEdSU_C7Mz0IOmvC0PV2XFsyawG_61IaVsSE2PjxnTFj9QX5zfoS8BBap5Q-rq5zXG4KNhLaQmqm5y1wU9hYdFTbKomi_A1CrPgglRD906ED7PZVQ1LskWkza4rha3fx5gVK-HtIpFaz7wJIaXTMmE6dbUJpsfwbDv7rxAyxkh8u7cw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">واشنگتن‌پست در گزارشی نوشته افرادی که از داخل ایران به ChatGPT دسترسی داشتن، با استفاده از هوش مصنوعی و هویت‌های جعلی، نزدیک به ۱۰۰ مقاله درباره جنگ ایران و آمریکا تولید کردن و تونستن بعضی از اون‌ها رو در رسانه‌های آمریکایی منتشر کنن!
این افراد خودشون رو نویسنده و تحلیلگر سیاسی معرفی می‌کردن و از ChatGPT برای نوشتن مقاله‌ها و حتی ایمیل زدن به سردبیرها کمک می‌گرفتن.
طبق گزارش OpenAI، هنوز مشخص نیست چه کسانی پشت این عملیات بودن و شواهدی هم ارائه نشده که نشون بده مستقیماً توسط جمهوری اسلامی هدایت شده. این ماجرا نشون میده هوش مصنوعی چطور می‌تونه برای فریب رسانه‌ها و انتشار محتوای ساختگی استفاده بشه.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/ircfspace/2666" target="_blank">📅 07:31 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-2665">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/XrFJ5UjVxADWIqkm5HMB55gsNwbHO9RGTtzOfTS0nG1BRFJq9jIQmJdI23oEDELtVnKQ7KN__NTZIrcwtbM_KjXjNlmGZCjGyNQhA6IW_kDPAdrIORHVVPpwv2Sh2_UAYjgQH1PLIucliL7GXWL2GGYLYrU1MTC_DOFSDABnhH9maVozI_5341Z27FAdF4P71Vq6w1lUgK8r15VR4UpvWLr9E8M9DpZ2Z6zSwc5mTODU54BlCVbTb8ChSMwV14meiXzAeiMMWElKDyTS3LcYhkfWVhveuxyoVU6Z_NqAuXlvRlZ7OEXwVryK6nBdBqR1ek9npC6X1064kI46kXGTlQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تانل WatTunnel یه اسکریپت متن‌باز و رایگانه که برای انتقال ترافیک بین سرور ایران و خارج طراحی شده. باهاش می‌تونین پورت‌های TCP و UDP رو از طریق یه تانل رمزنگاری‌شده منتقل کنین و اگر این پورت‌ها مختل شدن، ترافیک رو از طریق ICMP عبور میده.
این اسکریپت از روش‌های مختلفی مثل ICMP، TCP، UDP، TLS، WebSocket و gRPC پشتیبانی می‌کنه، امکان استفاده از کلودفلر رو در اختیارتون میذاره و مدیریت همزمان چند تانل، تغییر پورت بدون قطع اتصال، پشتیبانی از ICMP معکوس و داشبورد مانیتورینگ از قابلیت‌های دیگه‌ش هست.
👉
github.com/JohnWatsoon/WatTunnel/releases
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/ircfspace/2665" target="_blank">📅 22:33 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-2664">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/oLd19QYFGhlwIjRYRrGYOw0wjc4dfGZrNyLLVf7dJMlGMs-YxRJ8A7Kr1zqeSkhWG17BM3zGxrhztx4cgJo6maEjbLRdfjrNv43l51aEq10bxuNC1QXvt1xQ_g8-e7OWGdLMcWJ6SfIwHjfp2UUiRtwDwik9NxB3yipcS-qZCtszlwoJ-PtB8H1p86732xNtt9uw-UNEE4CqkPizIa7QxlrAJQLJZf_RYmMJ3eshAkay4DrTiIXp62z3jHRf83-n6OgXImKaImbwVL1htcVgv5omB0Z8EwBw0OEq8jSISGewiCAmvtfmSQ-WU0kduE2dmDIJ4wIFnShEoj7N0xaclw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">معاون توسعه شبکه ملی اطلاعات وزارت قطع‌ارتباطات: اگر جنگ یا ناآرامی رخ دهد،
احتمال دارد بار دیگر شاهد قطع اینترنت باشیم
؛ اما مشخص نیست که این موضوع در چه سطحی انجام شود. /سیتنا
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/ircfspace/2664" target="_blank">📅 22:14 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-2663">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/nEFxeNskdBUC31r4F6eIxoD_zBIW6fEskX0TW1QpQlz_-0h68Lrf5u0eam5x8tUf1dyEaltFRyB2xt0mqKMBrJt17M4Fcn1NEeHG9Lkn2MhT-_OVc4LAlmliQ6XYzRy5C7T5qID2xiBV9UG2AvN3VBkZTD8uL5FBJgwoI8_mxhHTsykpNJ8B-2nH6XOcuGYBEqohk8Eu6B1c6C0fNiar_KBhGvEOS8Iy0CQApZpisyVatyMZ5rHqcnZx_GeFb10p5F5ljEATsORS9EdYT4LkTtUSjkkDC2jBNG_rPnDV4AJ4fm5W-AdnKutbvG_FEvJzyGBB90E3Bbx3A8RVvFenMA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اخیرا یک آسیب‌پذیری امنیتی مهم با شناسه CVE‌-2026-‌107181 در تلگرام دسکتاپ شناسایی شده، که باعث میشه در نسخه‌های پایین‌تر از ۷.۲.۹، با کلیک بر روی یک لینک مخرب خاص، امکان سرقت سشن و تصاحب کامل حساب کاربری تلگرام فراهم بشه.‌
تلگرام بی‌سروصدا این آسیب‌پذیری رو حدود ۳ هفته پیش در نسخه ۷.۲.۹ رفع کرده و لازمه حتما اپ دسکتاپ رو به آخرین نسخه بروزرسانی کنین.
👉
beaksec.github.io/posts/telegram-desktop-one-click-account-takeover
©
MilaDnu
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/ircfspace/2663" target="_blank">📅 22:08 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-2662">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/oF-q6hkCwBYOBUBmc97BRE0tfXfJ5IaeWEChTiSeAHhysvqn2THLzrQK2iu4hpVIIW3IgGgDkgCttlbpcXN9xNAua9d8NP69nyulnSEba826P1pd-d6_PI0reNaRmxjkki3hx4nc1u_YbI1bmMzcdscvWwz22IHN9pBigiUYXWU5Wmwwk57voFOV5m7Zl4ksh856yvgyc5sufWVmBa5zpmOwOY5XJI49Ak-CsHja49wqQcj30R5QzJLFxqbdIxGgUtOGy_ObzN377YqyvCpz6yNaJ21UBxp8Rq-RdwF65KxmLNCfDL9BELt7YoeNzMZ_MZ5R4_psHegJf-OQSWi5sg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پنل NoRoot VPN یه ابزار متن‌باز و رایگان برای راه‌اندازی کانفیگ VLESS/XHTTP روی هاست‌های اشتراکی معمولیه، که فقط با PHP کار می‌کنه و برای نصب و راه‌اندازی به دسترسی روت، SSH یا باز کردن پورت عمومی نیاز نداره.
این پنل از هسته واقعی ایکس‌ری استفاده می‌کنه و ترافیک رو از طریق یه اندپوینت PHP عبور میده تا حتی روی هاست‌های محدود هم بشه با هزینه کم کانفیگ VPN ساخت و مدیریت کرد. اگرچه باید سراغ هاست خارج از ایران برین، اما این روش به معنای ناشناس‌بودن یا تضمین امنیت و حریم خصوصی نیست؛ پس بهتره برای مصارف شخصی و محدود ازش استفاده کنین و مراقب اطلاعات هویتی، آی‌پی و ردپاهایی باشین که ممکنه از طریق هاست یا سرویس‌دهنده قابل شناسایی باشن.
👉
github.com/mr-r0ot/NoRootVpn-Panel
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/ircfspace/2662" target="_blank">📅 15:16 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-2660">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/dfwheETfG5Aod80QpzF98pzFhEjFH5mY-MSqdjUFGNg3gzh1jANKeIvGt9aMcfT6yU5nd8OBBgpBazn8vg9-hmk1mHQUR8d47b4441vFIhQdC9BAQPwFHO1eSDPlLFAORf-N7WMt8-3h1KrjZx_daJ-24vTAkOxM9c36iqniuxblb2TcWl3cea1XYIwJohmj8rnss8M3wTQxTuhbzm2w6H77MYCYOkiyLleJt8vhtrlHpbZy9kSZp5AUqf6RCPOnUwFm0pVPn7awlhFbULEKoOzhCd2XrvP-_mQgj7NJIS76t4XiKhSzwZDNYkiyOE_hawVcxxLqw4mOVbkietIGtw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پس‌کوچه در مورد Jet VPN که بیش از یک میلیون بار از گوگل‌پلی دانلود شده، گفته معماری این فیلترشکن دارای آسیب‌پذیری‌های امنیتی، با شدت بالاست!
این گروه قبلا در مورد خطرات استفاده از JumpJump هم به دفعات هشدار داده بود.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 33.8K · <a href="https://t.me/ircfspace/2660" target="_blank">📅 15:03 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-2659">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/a7eNmdQai4CqZoy_GgaScbH_V4A6J9Igotqs0yk3xptzDgglbluGh9fGw1ssIdiyDLVStgVvGK4qMI67_zx63FB--bGFjU4b4Wvjf9MdWtLl1sTlUo97KHidBQMIrNT1lyz_mzii_g0SMOkbDI59yaWfhDkvN4qJR5IEZl6VClkSKVY1HMq_-Pdh5gHPgBcDEeNl-1LyQWyEr1nxsX6YI_4ChCZxq1UaOEfT1Y23APD-NfwEZHG5v2oVuotfFHVofast90OorQrDqmcexQJdy2-O5fRhd8Vupz_9P7knC_lPip74eF6fWcdMMEq1AR2029N4RLifurB7DSGeFOxSag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">معاونت توسعه بازرگانی وزارت صمت در نامه‌ای به پلتفرم‌های خرید و فروش آنلاین طلا، از آنها خواست اطلاعات کاربران و میزان طلای تعهدشده به کاربران را به‌صورت کامل و صحیح، در قالب لوح فشرده (CD) به این وزارتخانه ارسال کنند.
در شرایطی که شرکت‌ها برای حفاظت از داده‌های کاربران و زیرساخت‌های خود هزینه می‌کنند، مشخص نیست اطلاعات کاربران پس از انتقال روی CD چگونه محافظت خواهد شد؟ /دیجیاتو
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/ircfspace/2659" target="_blank">📅 14:56 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-2658">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/hcp3ZshloA0x2fpJgoDlD89ZMx7EQLfTLOjwNBqmORcslhZSpumFaOwUqW8eZR-8dxi9sXUUlljMW_8NImLfrl4B-pswJv9CZ-3D3EJ2U6rOb6oAr9Jxtk5PVUNo1DQghNdD5DD7oiEV7qOzKQvhZTwqf8vYuiyJEORizTaq9y_SSU6wdNXwsM-ElJ0n7fY8jhL4u6s9vVYEalMXICpGdUjBihYTwsqf5QlCC67VvD-CDSO7_MgRXDpGGYWB12sAIwZl8P3i_YnginBF_tggkXEokC6y5oHNi5Pdy4r5Z0kJeLGEFAvALT-NkcrnFRuGYjcqy32Ycv-rTBzWU1pTAA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">گروه Void Verge مدعی شده با توجه به تغییراتی که دارن توی شبکه ایجاد می‌کنن، اختلال‌هایی که روی اینترنت و همینطور اتصال VPNها دیده میشه و مهمتر از همه خبرهایی که به گوش میرسه،
شبکه زیرساخت برای قطع خیلی از پروتکل‌ها آماده شده و فقط منتظر مجوز برای اجراست
!
روش‌های مبتنی بر کلودفلر، ایکس‌ری، سایفون، DNS و حتی تور جزو روش‌های اصلی اتصال فعلی هستن که فینگرپرینت شدن. تجربه جنگ‌های اخیر هم نشون داده روش‌هایی که عمومی شدن، زودتر شناسایی و مسدود میشن.
این گروه معتقده در چنین شرایطی به جز استارلینک که البته دسترسی بهش محدودیت‌ها و چالش‌های خاص داره، به مرور باید پروتکل‌های ناشناخته و ایده‌محور جای روش‌های اتصال فعلی رو بگیرن.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 70.9K · <a href="https://t.me/ircfspace/2658" target="_blank">📅 07:51 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-2657">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/lwZ3bpgP3OfRQ2Sv8cmLsYc4xVXWh6ecjuXHYL--lAnzEfI5hEllCNgtDBqEbmTkFA_y_BsQwHyMbc_Bk8dwpQkDZtAn33ZiI_qg6Tyhp7Sw9u5s4Ojt0qULnv9G-bU5t23oX52PYEWoP0o0VI8oQJI3_pp3q9zi_Zl0ec3tGaKK8Meb8oSlWoXo-Ib3mmQfTQHly-FZ5RqqrDxtcrnF9wVVvwriyjX8ME7pzGypmlWz2y93dOf_b26hhE-vOSiNyG4BmCXxOn-JoViXX15qYUzWA7agTQ_5NmlXrBB-ziu9TZJJMfg5Cxdg5T_jhxMbhPHJXIwU2XPqtJccoOcRjA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کلاینت متن‌باز و رایگان ZedSecure آپدیت جدیدی برای اندروید، ویندوز، لینوکس، مک و NixOS منتشر کرده. در این کلاینت از هسته‌هایی مثل سینگ‌باکس، ایکس‌ری، اسلیپ‌نت و شیروخورشید پشتیبانی میشه و در کنار پروتکل‌های DNS، امکان استفاده از OpenConnect (سیسکو)، IKEv2، OpenVPN و AmneziaWG فراهم شده.
همینطور OpenConnect روی دسکتاپ بصورت VPN سیستمی قابل استفاده هست و امکان اجرای زنجیره‌ای روش‌های اتصال مختلف اضافه شده؛ مثلاً میشه سایفون، تور یا SSH رو از طریق یک کانفیگ Xray اجرا کرد. روی اندروید هم قوانین مسیریابی میتونن بر اساس نوع شبکه (مثل وای‌فای، دیتای موبایل یا اترنت) تنظیم بشن و با تعویض شبکه، بصورت خودکار تغییر کنن.
👉
github.com/CluvexStudio/ZedSecure/releases
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/ircfspace/2657" target="_blank">📅 20:13 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-2656">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/uf5HdX6F-CU1E24xN_OFOvJr9C6OWmf0uXlOSHFV-kZ-vQu-8sLbgmTYKAwDEmXqXnkwfHQ2z14pCgkvCnM5hvyEbF6thTJvJH4AaRMrhZ-55b_Hd2K9AkhNlp6-XWnlfXXsrGNonpXcsL21HH3WduNwnOPegiNSyu2SvlNa5zv7sRSbVR_NIg80GMt7uWH_AgN9OUVZU2qTwF872xlJ3-pyTWhf2n7Wm7zfh1TaV1nljW6H3YLraZsbf0DWk6hJQcoCY23C2lYEpWDUsfib7ca9A5zq9Id_Za9LVcqgpufj5r9A294_h_dB_P2SiZIGrdx90bCiPn4Mm2I3SBr7tQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بر اساس داده‌های رادار کلودفلر، از ۱۲ مهر یک ناهنجاری ترافیکی در ایران ثبت شده که همچنان ادامه داره. ترافیک اینترنت بعد از شروع این اختلال بطور محسوسی کاهش پیدا کرده و حوالی بامداد ۱۴ مهر به پایین‌ترین سطح خودش در این بازه رسیده، هرچند بعد از اون کمی بهبود داشته.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/ircfspace/2656" target="_blank">📅 20:03 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-2655">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/oUjvkdTxuTAMl2oBoRtSebBqAIPHIdZsx85Kq9WuzjtniLvgizvUUfznUfiKrDS_XDCDiCWnfxfnA67m2CXaGMT-VsIUOwlHQpbkkUDmDeeDVmCUqttL0B5n9KwqmVUhtDLTws91IPhy47itJYhBnrxvwflmx6Q9_2UNh7GAaQkodujNR2NkyaapjDonraeVBwhwg-gS6h3uZ5zvzn15mbQnJAjx-7_BoUR12pMOMZ81BXVBpmcAQzC_eMMgmu-XfxVamfYLWqY3S_nDszADfxonbRq6xisDhmPD7DJOHagFsb0faEKEnlMzKRNLP2L6T8KhT9Um7VfyKMHpND6WXA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزارت خارجه جمهوری اسلامی در واکنش به سرکوب اعتراض‌های دانش‌آموزی در فرانسه، سفیر اون کشور در تهران رو احضار کرده!
با در نظر گرفتن کشتار ده‌ها هزار نفر معترض دی‌ماه و ۸۸ روز قطع سراسری اینترنت در ایران، ممکنه فکر کنین طنز باشه، ولی منبع خبر تسنیم بود.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/ircfspace/2655" target="_blank">📅 19:55 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-2654">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/AnFdfvMG5SZehKLfXYgNwM-IuNpdjj69UgQ9tYvcxFfhu4IbCKA9QYHXHM6NnEYv4paWBxzIpC42v1M3EU2YHKJbjhDLFaMghh1y1tuV9AZ2-3OU3N3qnG1kmbTlw8ZtcwbkxyFXWBgjIMxTWqJSsyKM1Meay0GFtLwtUQDmbk1lReFo9ufDmINmn1o-pIDeSyeXHpyGYrki2ngXMaRDNMoL1azbnDzplFrAoZ6C_lTC10xrdL7Foh4b6lzGyfeMMf1j2aVfN2boC1O3-SUY6tLPrbWqgwXhXZ-CjEM5BUWxoG5BVXlce-ZI87Jj-tyMc0zUA3kx6ibBvxiWqN7a0Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نسخه جدید از اسکنر متن‌باز و رایگان SenPai Scanner برای ویندوز، لینوکس، مک و اندروید منتشر شد، که توی این آپدیت قابلیت Anti-DPI اضافه شده و با تکه‌تکه کردن ClientHello (مشابه چیزی که در PattNG انجام میشه) امکان دور زدن بعضی از محدودیت‌های DPI رو فراهم می‌کنه.
حالت Gentle هم برای اینترنت‌هایی که وسط اسکن آیپی‌های تمیز کلودفلر قطع میشن اضافه شده و حالا می‌تونین آیپی، رنج یا دامنه رو مستقیماً وارد کنید و اسکن رو از فاز دوم ادامه بدید. امکان ذخیره اسکن و ادامه دادن اون بعد از قطعی هم اضافه شده.
👉
github.com/MatinSenPai/SenPaiScanner/releases
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/ircfspace/2654" target="_blank">📅 19:45 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-2653">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">شستا ۱۰۰ درصد سهام رایتل و ۵ کرسی مدیریتی این شرکت را به مزایده گذاشت. قیمت پایه واگذاری ۱۳۰ هزار میلیارد تومان تعیین شده که با نرخ امروز دلار آزاد، تقریبا معادل ۴۸۳ میلیون دلار است. فروش به‌صورت نقدی و از طریق مزایده دومرحله‌ای انجام می‌شود.
©
stup360
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/ircfspace/2653" target="_blank">📅 19:38 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-2652">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/UnPjFCZnh94wh5z5ZJGV5pBIzE33GpPE9aHrEQQt03lbdnN9R0Cy70gfNtIrCC3kQH_t30__rvj6LVZywQ_ak_qn9I_GsPpso4N63epmZgRsb4LojO_WujYRuQ1ju8FeOx_FjaqqKmqrQnfbQG42IOyVSg8tM24_Hhx4SsVY2Wf0YBVufkhNk9vfSV3XP0xBpdcqsM-WpQ38HSVcyfFSUqXdUlBHj-LX3VnRpps552BDOQLKBxG2a_Bf8tkWW3k7Q_PhT9z4FGYLPa752jouzargGU9RFMwZyoU20W5GKQMVK4UrVcgLe8IL9kP1gVOUdNyhb6fj_Y3QBjecL3hTkg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 31.7K · <a href="https://t.me/ircfspace/2652" target="_blank">📅 23:57 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-2651">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/HCWybxD6SxHtKuq4jyR2IqEAixfK--icKLiDqQQTkMZOlqvd7w-gVX_7At9SH1SrT9vStBi0D6jcsyZbV7o8IxFO7XSmJy9yKrmPeKhHZQAW8Ic--p8GJpMC-ZCIH_8R3LQnd_GGX8x_UXbr69vNFK9LC4_hOXFKg9wpvPDrYaSuSlFdHMpyUGmYXcrlFB7xgiIRswhe6nY96s7ah0E2CiYgdHZxj490gykknvzIq00vYIgj7_bJLAT2zfx7iaGydikpOyqs5IVvCj6gf1M_5Jp_e9o0vVKmeDPEl3rc_KXwhKcBdK8EC9bT4ldM1tI4ql2PfgB7xPwz2pMEISuffg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/ircfspace/2651" target="_blank">📅 23:34 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-2650">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/NlgqmVQKxqBTWSR4blBDmMZqvF4LlkE0vOn_rlc3v_c3Dm9OGUCUSoUeUoM_CSW9b88F4rWmpfe_SQyCFUD06_E4IEwK7p7It1dduFtucFTMcpxT9OV_tsU28F_5FFM7Tua8y8Zj213WaKuWCvCO5DILVC6w3OuG5CFbxwkAFJtyZJCyhHp-in6eF_92vgFsBRpbESQumOni6YDpDnmJpu6xSn43mGrp6u7dhrJSD_EF5FmcqOGRd4D96aDSsaUf_YQDGVJqC5GGDGPi4RQgyzGlz8JiMuQ08NwbTIOVWd5TgqmafBHabhzvXLOUQ8-Wp52CLTzaBV4iaKSN10hj2Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ادعای "قطع اینترنت کل کشور فرانسه به‌دلیل اعتراضات دانش‌آموزی" فیک‌نیوزه.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 29.4K · <a href="https://t.me/ircfspace/2650" target="_blank">📅 18:02 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-2649">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/N5ENOm5aLjqR4ZfvrRG0jw2DpgxplIoScxkNpIaUqcMJDBznvHNVTXEWnCpXeCgvwQo_rVv6vh76920MBqfmajAYqW7OxZrKpz5EjWSSGWbrmOhxJpsH7dW-3s9fLopvqqZmUIMrDoiBXjrTPePiRV9CiA6mmhzUlLH4cA_q6ojt5KkeWKRsAr4MHSXUqyVGZP3HAmYDARwXm_kaJkpnmsbW6U6HNOy9PaKmMMc5siIKZuhYk0vGZen3xzhGt18HmvMJl-artv1stgr-PlAqBqlqIl6qKdWY8ecxFuhNFZGjphaj48Lqf_PylHbSYNVKMfJeWykcenbHG9cK70ZjwQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/ircfspace/2649" target="_blank">📅 17:53 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-2648">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/aNG8Ju05wmFAEzThqZzuYRubKSw6YGsiHv8ABEUkaKhFhaVVDNTJgPKuD9rOk_FPZZKVtasQgk8DwZbVrUcrZE55gpjADL-R9ZKwk-tzMCYe1DFwXFd8ZSPmyOTxote2iKWQTez3mJn4rzzSlhCi3dfSYRaaJPGPihvNCGGx97h8Krw-IVMuwIIwddbhA1nqw-1pOu0MMgeqmknWjXaaHLFAjg-oQti9ei3fjLI7HOHUlPyLEFrWg2tfNHqqnUPCagB0C4neWt9ZXT5ag_I3acHs5SaHsBljpTdlx8LtZcT9a6KV_eSmH-miCcxXqVAma2MiisoId6WMQf8ppWbTPQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رئیس پلیس امنیت اقتصادی فراجا: هر سایتی که اقدام به اعلام قیمت‌های کاذب ارز کند، باید بداند که برخورد قضایی و پلیسی با آن به‌طور جدی انجام خواهد شد. /انتخاب
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/ircfspace/2648" target="_blank">📅 17:45 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-2647">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Q-ayiZ24xH4kZUQ7ZWoKyoLXaHmoH1MjTWOsOwGjHCT-Cqyvecv_sKEsEDQ6zxdysOlbY70HB3_G1w_jx9fwF1GLtck7C5tfVekBdQp_54xul0IyS2QaooRLJUHYWPIz-JJmUSEWdQH2-FyACiCFpJ6YtF-mHcbriZrcaoLzJAlW-9noeXifzL8K8GeXw-AGXeo6lMTXkKHbjc5x0WxcxMNjpbL7G9igoUHFHfMfCdH5O1sDlpF0-_cD5A2GFysmkTHFAtciMclntAFFiTmefXIjPHpaCHAcY4dUkfTHfYnquXYa7mG18XAadVvXzio0iYoYX0pQ_lV2zUW4_H1NFA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/ircfspace/2647" target="_blank">📅 17:41 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-2646">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Gxpd9xHWrC1dkVhH5zVe6fwjVk8PwQWtVGl9fm0L2uXwapxKn4fKRlH10WsJbG6sM6orJhH8sPI5H17iPcWuHkMRlHAmKm6HAbb574TVcbO7psfZUSGubRHFS3Q-UrAoHfCsKRb6VQIF2ON_oCwqQMFDhbV4OOEaG0ADiK_olQHnwywkkJP3-Oq6YWQHoaLkaNm6zRxbUBPeT8Q-PWoV-o4X7W6I6gU17mBpYIZ-lnJiT3CytcypP7qZOz63pe6lXGa6yzfoi39-cOXHWx5pMVPRQVvEK27hx2p0oKR_BdadCn_mE-oO_FAKcWo5TYke73qibC-0P9WohbTa79Dxcw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رئیس مرکز ملی فضای مجازی گفت: ایران برای اولین بار توانست با موفقیت پایانه‌های استارلینک را در جریانات دی‌ماه سال گذشته از کار بیندازد. /عصرایران
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/ircfspace/2646" target="_blank">📅 17:35 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-2645">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/mPjIk5LbuYfrQbGQPlRLycq5pZ71X2cFnqLvhU1oBmMDX5bJAFrm7LOiqZ0g7WB4x-4FKFjkF-jibgC6klVZjmGVhihyPjNCYm27Y7LdGL0kEk_rriwEhauo1lSArDRWZcXsaQQMd__QEiKzqHf_izYhGXMplotJzfhJMuMcJCcFRe6P2p1b0rFgzoIRCVZr0M8x3dkyrY9285MSFEWxDvvG_wr6M2K4MnLsQxVxqSQjq1WjutaFujl9-hzbid6pzUPl-fG88jKGO0I5HML7wusAl7QhapNVF3KEqZXmBVXsWFmYU571dGy-baC7Pn1t0P9LRs52zpEvWOm5yZPYaQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/ircfspace/2645" target="_blank">📅 17:28 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-2644">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/PpCCVQJ23UEiC1qdJufXrRrLC7H9-5Yl2bngnzVxCjqxjXh22xyueSBL3xgOuoNQ1b5bdDbvxuTpYBrZnUEo5B98tiUj-wduMNjiYsSODmxHjR7AyCV6f5HNVaJAdvhrRONh4SUctnFihLdAwToy4R54WTeZmvix1GpMdGjGvbFkhdoM_xP-uuCkq27P29X-F3JIZTcKd9gSPFz-mA8w9lJ-nv6NfAQp-SkgIPfgDHkA2W6uT7Xn4mWDlSaXt5tuBaP92ZlgGlL-4tKvC-LXIzFzRxxH9wnnd_D14chyG6MsmprjYBy4bNCb8Z9H8LWPoL2EjfBRTWVvEEXzrtU0BQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/ircfspace/2644" target="_blank">📅 23:38 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-2643">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/V_qqrFzvRf8Zde7S7MhSXwUmm9mgUF0ZqMocv_Lv1WvexyQix2kM5wgDKds-kX8HtvdV70peGwQpjKGcMopznWOLt2e-tFxK_qRNWohwB8vNZ0Uc9FC4Z4fbN7tv2Db9O6uyV6i91SwI7P_WWNaDlqXZmp6VhI5KO4cDm8nAMr6vzetRSumKzTtZomDGfOXs5hJd8Yg8mY0WAvg3lVZqEjuXMHZrcu9EVuICoC3n9aKlpL5vtEkUVeKqnZZ2kziQxBYyw5ukXlvnEDhTYqKTltsnENCscoNZOJAMbuQT1bLS1EV9nDxUDoNruQ1LeccOSmi3GjjDzCTIQHnh1hHiIw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 76.5K · <a href="https://t.me/ircfspace/2643" target="_blank">📅 23:31 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-2642">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/a2kaXiKeKvkT_69BEXZPYFsY8R8nKCT-H_SPd1aR1nWwr_Ohm3bVRSNPMmtTifUKHUjspmyc2RJHCf4oNUDKzT0dLgJTv_LO9q-7xXQs-z4uL3mtReZbXqw0cu-H9syg1spHSK9Hw7dsgExaswFnMMzUJUtvwtNiEPaEsD5-1AwrK6F1aJ3-GMOhKxf_otj-sPaRCsgujYchU9BqZNF0-72gOgNG8sSsty_8hESOG726vEGdxXNX6I0nCPnnCdaKZgRLDLgSDN0yQ5jAypdal0bFkI8ee0M6KQj6yZcCMiihsKA_KnWEm8eaWtM0TOw0Kw9XRv8lL3qmNcw0tGm6zA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/ircfspace/2642" target="_blank">📅 23:19 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-2640">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/aEU6S400Jb8nwMG5w3hNL9RGmV10aDR4DSDg8Y42VDJAwL5I5WwSARC_bRgpSV5FEc-PZdQMvYRsQYJNdo-F2FiZZdNwVFvmeXoMgkncPznXXRXii8BoTuEv_bSaPrUI7UKGU44ANsCQ54IKIVQHryFuyk-n1Yh7tZgSl51onQpSJPR2MSGrIcWjovli43Rf_n0NoTYcx7L6uTjFK8Q0gezyps7jtyjCJ98QWBViFgWouGurSc30gFkk8cxEewcJC8utDYHA99sbCuJTjCc_QH2RokmgtRxlqMtedVEv_Zpjb2y3X28KIpkw1SFlIC4Mhtu_P4G-r-S3YrnP-J1WXw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/ircfspace/2640" target="_blank">📅 23:05 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-2639">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/RvKb_gJDyMVZWeJGv_6sYzg7zrzz1JgnPNjWo0TUhmowgoSJRZbrEXSppbawc5szpcFRWLc5L8hhfK_yH6gEpycfbJTaee2aGHrVdZEDmwfnOllHIWwZMczds9lj42s5gFuTE1gb4YQKgg8YCH0TAwCh_Rd1cmes7FCWZg4iDXRLlVZeSlDCb6a8k3Jp0Smazvg19WGzv0ckuFvqKK7IghOaVxDfUgv3e7Tycjk5GXF_8WaIfiO4sie5Nrj3VEjKZrCq943Q2JacGG-p2uG613oEoDCs2NQcRVRb-gGqAL2r3tBhhTDAXv4Q0PP1T_lapynnijLiwmoG_xHgdvm5dA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 29.1K · <a href="https://t.me/ircfspace/2639" target="_blank">📅 08:22 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-2638">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Qj0K2zyBwhjmtROQC5hKpVJDE7EW6UrIqnDbzxa7XV5MHx-J20TKVYXymO0LF--T7iPB2M6Dee0cbnxt7rpRUdBMhfjUC0xqYUvs3u94CYajFZl9dPMHiyYiUhiwvheyd-Ga4GxZ_Nqk1_TuGHf1uocusoqndUB_JigmsvHEjPJlw2WCmaZ2beM5UAy2yV4o6xfc07x0IOK3hNjQw4vzfCpGe_kMAYei-Oz91ueDa7nJ4CMT6nGI2I0WggbickyDWl1HnL1k--jxlMM4GYFUPextIAq9AtbjHI-HbGXaMCAw6__zjr5GoiffHVwxASE6qsxyOhkQtsi9OHQsN5vwRg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 31.6K · <a href="https://t.me/ircfspace/2638" target="_blank">📅 19:42 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-2637">
<div class="tg-post-header">📌 پیام #67</div>
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
<div class="tg-footer">👁️ 28.1K · <a href="https://t.me/ircfspace/2637" target="_blank">📅 19:26 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-2635">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/reJpRVcbZaDFkafvH6bNkRDW2z7fdsNeVCzEAoTB2mw1aM2yLFop4Lez6SqCCKYStAPEctQf7_Y6M_PJOQ-PwxzgY_AJsWZ-hXf5-pE7Hq7avz87FXinYETsR8nIz8EoVEh_yFdAlXMABdnV6aV3CHMIHBSUNSzNda7TVQiHVcFs-bX26ptuRQGuo-MqfmBtIJa1IK6J5d-kzgPVx9F910cHOd5MbQgdUDcekFShufjX4v-1TYNhPERdUnH5LEItLjnc8Jpi9jvCe19PRbQ92sf3N8tYhtoA6XDnGyd9qSj_umLYI2yWHSiWVCJ7bSYOMvXZqNhFpCqoq15tROc3-w.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 28.3K · <a href="https://t.me/ircfspace/2635" target="_blank">📅 19:09 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-2634">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/I2MvgkCYc_1vPXKwtq73jhDA1lhyblgFPA3oRoDuKniFoTYZLG-Fd1LXmpYrZ2Fd-kgkHDpg--7Kby9sbdfVVA8z4GWyPTt-O3d47Q67wGORCH56GAjJWCxzrZk5WheGelP85WANmyGWyiz0e3pkV5pXqPaT22RK8T3OhLu8sp9DOz0p5hu3RGUPmMO3htEQgzVBymhaEvj4mZLe7hKNwiU9PdF7Bnj8XI7PAnOQmF-rzXjT8f8tlazskYGn94d_cSxAO9zy9zpsq-_q5TZUME8yp8s7CtdVplXTUAyiQbdM4B434pRgpFI_dHOn3s_XjPuN7PkQbzG0DcA3-kVmDg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کلودفلر میخواد تبدیل به یک مرجع عمومی صدور گواهی دیجیتال (CA) بشه و در قدم بعد، گواهی‌های جدیدی به اسم Merkle Tree Certificates رو هم در مقیاس بالا صادر کنه.
هدف اصلی این کار آماده‌کردن زیرساخت وب برای دوران کامپیوترهای کوانتومیه؛ چون الگوریتم‌های فعلی مثل RSA و ECC در برابر کامپیوترهای کوانتومی قدرتمند آسیب‌پذیر میشن. MTCها کمک می‌کنن گواهی‌های پساکوانتومی بدون اینکه حجم و فشار رمزنگاری روی اینترنت به شکل شدیدی زیاد بشه، قابل استفاده باشن. کلودفلر گفته هدفش اینه که این گواهی‌ها رو از اوایل ۲۰۲۷ وارد محیط عملیاتی کنه.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 49.4K · <a href="https://t.me/ircfspace/2634" target="_blank">📅 18:57 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-2633">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ptBuWBo-NZ7eS0GTOJezkgHK-nNkxkdfC_kITKAvEtg1_MI5pAzVhrQQknjChPDtJFjgw3GCyXUUKiFjvaYyWUyQeYnEZ7h8rf9Ho1ljA9c22Ql7PfVnJ5jSY8kPLm6GJ2EqN26xYKmoY6IOnBbgSMXYJ9p2M63XLc-XpefZiBOODNE-RPIKNAWtZNBzUghXFiCgGBRtIy1s4gLFDJcu1kLiX-dgiardZImeI69eM_rCdR-qtBxiFPQ2Mn6sKrqAbDlTZYSQes7pa6yrL6rPrxXZmg0quQyr9ZlaZAzpGtTmqg2YqpU9tHtHNvLAYyVhMUoGm_7wiDD6Bea0HYNWMw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 28.3K · <a href="https://t.me/ircfspace/2633" target="_blank">📅 19:03 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-2632">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/C_DXJafBA02VFNY4va4fjnZ4W1mAeGqs2mUGoZDEGn5pmha8GGhqQzEKEPETFQaUtGuO-UdSTkvVHA6KZqTrbkL_W-oE3nXywG7cph2fh7AcZ6aTjv1lFSeIrcTxpkwqt7se_SpDT__luelLrefEvOMf4UUWyM8rLQTvFMdFEkQVlULI7ru_sSkiy3UegF52QwwR72-dHcLzrMVUjG98ktMkz3412aEdD8dLKZJL8XgCsDjVeCv_6AbxkqVHRiXOPXDYotnRp0_q9Lz8yJh7IaPjxLl8v5a69Inmma5hu39Eyzlv_oqBesQqmPtMeuJcKmY5h-yOkkRvsVpsSHmvUQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 29.1K · <a href="https://t.me/ircfspace/2632" target="_blank">📅 18:56 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-2631">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/hpeWUrXAvIRl_AUVU3Kk_VndbTt2Rf6Wno56hzNug2YynzCSLVjR8v6NWldU9ig_gvy1j1S0FIMP0LTip-59ZfUaDFOCw7_Sr0eXxKLBcrwk_KsfzUPVzWOsRmUHIphzVxly8wRjs5jf-93_6rRVQy7gkZ_GpEnXLGM1yRkDyOkdBwVD3_an2fXda1vMuGBSKn_F7g3IV4A2VeJe9rEi2SmRx24uu56Jd8paMaBjEMZWJxlEvpG8PzLendxSBIgFcCo5fLMxkWtVWJ3sKW6L03nF4QmUvJgG2rgSVCSZ-Y7pD_4QtGq-c2yvaX2LINUarpF0-DS05V4wMu1dixwEHw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 29.7K · <a href="https://t.me/ircfspace/2631" target="_blank">📅 18:51 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-2630">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/TuHRCL0ZDlKEBy0Fit2SwLhb69QmmxXirzwh-z15Wu6o658x6LeAx_FOJQamHH5PPZ1oJbQODgKmOyK7Ri4eQvjNo-6qF1vpf23ee0UvMeZKx4SvyvFZbjFINgHxsVdvLfCOhtdobUwakZeX1gcWsB1zjlyH2mj7ul5KRWP-rpwVOnCypI5aG_LHCtTuknn8_76MszOOoRPaeYbVANFv8BqgLPNit6HqnMQ1GZAQPteSFyY6xGuuxluF41VXA_dD3D7h-OCYijXLOURPwO1RhlRBBG5I62f--Q-jV3ARNuu7PI1P-I_-LewbD0EehublEMOnSsVu46kFLg2LogmGfg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/ircfspace/2630" target="_blank">📅 18:46 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-2629">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">کاربران در چند روز اخیر قطعی، ایران‌اکسس شدن و اختلال مضاعفی رو در اینترنت تلفن‌همراه و ثابت گزارش کردن و میگن آشغال‌نت چندروزه که شدیدا اسهال گرفته!
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/ircfspace/2629" target="_blank">📅 07:37 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-2628">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/bOoDlMOG3JUSa-eYhAjKp3rnUk9-nbs_rPSTNogvyzzeaGp7eT2wTECW7EpA0sWLM8JD-AmDCi7HE42tnFpau_fmKJPUhNxJ12kS3nPgQNBoPP_xdD6UJH4u_I_teKuf3VTcuAFvLBrOA_7SnMUTJ6dqnrCWoHkZ2oWwTrVF7vxNwA2eq4gBWcCbCDeU7Oev7h-NGrz7ER1XUHMKZb_xiSPWWt-BGqd0BXjxAImQ3_QiZGdW9h7HVXkhrNTD_ozD70S4r2SKGqfIM3Ls2koJxk4pKJ-nrNuIZ6JS5RLbyg5dX8-VaQw85vSJ7SOrtBhoaTEUD0AfHldyENpUjgfcQA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">طبق گزارش Group-IB، یک بدافزار ویندوزی به اسم HEAVYGRAM شناسایی شده که از تلگرام بعنوان کانال ارتباطی و کنترل (C2) استفاده می‌کنه. این بدافزار از پاییز ۲۰۲۳ برای هدف گرفتن روزنامه‌نگارها، مخالفان و منتقدان جمهوری اسلامی استفاده شده و می‌تونه از راه دور روی سیستم قربانی دستور اجرا کنه، فایل و اطلاعات بدزده و حتی از صفحه‌نمایش اسکرین‌شات بگیره.
نکته جالبش اینه که مهاجم به‌جای سرور C2 معمولی، از بات‌ها، اکانت‌ها و گروه‌های تلگرام برای کنترل بدافزار و خارج کردن اطلاعات استفاده می‌کنه. Group-IB در گزارشش ۲۹ نمونه جدید از این بدافزار و ابزارهای مرتبطش پیدا کرده و با اطمینان متوسط این فعالیت رو به گروه حنظله نسبت داده.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 29.6K · <a href="https://t.me/ircfspace/2628" target="_blank">📅 21:06 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-2627">
<div class="tg-post-header">📌 پیام #58</div>
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
<div class="tg-footer">👁️ 28.4K · <a href="https://t.me/ircfspace/2627" target="_blank">📅 20:16 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-2626">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/kPPUHr_GzqIQD6fS3vEppG9L0_0GiXuLPeXnAt2ulm6m4VGU1dCem9fmPTSpcM7dsp6h7lCDUkB5_x46MKVLsOBcTkjnP1yga83L4TG_UlnPlnoqoQlyzoH_eROGw_Ir7MTTG0XK1TNSsFgRwiXa1fMR3y6rYOwaCzQCwbUH5VxRZsz3bjFAwxdJIjZpK6ps3kLBTaekcz0kkp-yMQcijcPLmxP3pRN3fakc6k5xPNPnwcRW_9YsRrVd_3TgArRg1IYK_5I8jccxrHZUA61X08K70-Y_IpGTJtot_iNSvJ9873uz9uQflN4hJAWWQ3QinxCnKa2y-MfOOouj40lzjQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اگر از دیوار چنین پیامکی گرفتین، ازش بی‌تفاوت رد نشین!
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/ircfspace/2626" target="_blank">📅 20:13 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-2625">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Y-VCkroJzVJAXOBMU8LuUcaq95IWmLSHNGoe1pd2XIFYJHJ9Cp_iWt65tH1wJdhibNOhPs_QyeYe64STXCn62eL7cs7f4JVzNAhK1cmjzhPfgbHguPYusRhYyWvJmrfdJZG0FzD-Fv1auUvX_Yy56pvSonrefu4qO2LEXZI76VqvCgTLpgx8IYlm5S57s4TS60CBTMxdOITfM3qOCY30ZUvkOiDQtbhWRbmYLOoICr4JwBobuxlS_yv3Pbj9cWt0bOY5xXx5Wm7kKgDxG-qfK_3FdMN8g6YE2pu-VnDvx9-ePB1Zkxp-ysvfByzCW7ptJz6dPQQNKaABgaMHIy2TtQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پروکسی تلگرامه؟
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/ircfspace/2625" target="_blank">📅 20:09 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-2623">
<div class="tg-post-header">📌 پیام #55</div>
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
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/ircfspace/2623" target="_blank">📅 20:05 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-2622">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/NWAfPwKmfDEDksySQFV93a6kmf2j2Cb625B_FIjw2VG_l1k4HMB2TjaioG4m0vBSsKaROG7GaxqTN700stZeNJEQArGDtp4JHe-GFmiFx1JhEK-0GS77j_FWzdVUxdqEJEP2G6DqxlN321rYA5a6piSZ1LAWBUB-x1kJof2TvirYHh1-09NtbRVx5k8fb7ubfgmySrwrFA7hqQFCFUACqlYU4IIT2CKXYl6om7HV2KO5P2BNumzZFDUFAt_6fVgEO-mmeVui3zEZAo-7V00XUIg_sFIEvFSctg8ZahAJdzmUetM71CAlEnRUBrdk8jPh6X8IvhThqMj3jm7IyWSogQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">معاون وزیر قطع‌ارتباطات گفته "فراگیری استارلینک میخ آخر را بر تابوت حکمرانی فضای مجازی می‌کوبد".
۸۸ روز اینترنت رو قطع کردین و نگران حکمرانی فضای مجازی هستین؟ بابت ده‌ها هزار خونی که ریخته شد، باید منتظر کوبیدن میخ آخر بر تابوت ج.ا باشین!
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/ircfspace/2622" target="_blank">📅 19:59 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-2621">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/mMGObkLJDZWD53MBiCtrTh1Ern0rejIqjSiphG-FjyMjECrPQfC51HGs3GDIytS6KOwYirjs8qtGZQ2BFmRhv2D2LPFGc-khbn94AUmMQdXshAQjmbFbdpWil866mY5ayMQWgS-6iFSRhFL6Lj8yDe4MfiYytGP5Sc2TFDSK2-3AyLBU_H2QhtWSg97yQjyemcKgUPt-5ejaUEEJsuLDTeRma1SRPa3bb_ouv0-ADsKyalAp5SyDjQqTToxpQXJthCJk29P3aI_0LMJoNhzJZKI9lpwlB_S0h88dqAuZKucxKpA5EuSv1BGUIP-gh7EmeLAzWjZZHXQ7bafAzeAFzg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بانک مرکزی با ابلاغ یک بخشنامه‌ی رسمی، ارائه‌ی هرگونه تسهیلات بانکی برای خرید طلا، ارز و انواع رمزارز را بطور کامل ممنوع اعلام کرد.
این بخشنامه بر ممنوعیت مطلق پرداخت تسهیلات، چه بصورت مستقیم و چه غیرمستقیم، تأکید کرده و مقررات یادشده شامل پرداخت وام از طریق شعب بانکی یا بسترهای دیجیتال برای خرید طلا، ارزهای خارجی نظیر دلار، رمزارزها و همچنین فعالیت در سکوهای مبادلاتی مرتبط با دارایی‌های دیجیتال می‌شود. /تسنیم
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/ircfspace/2621" target="_blank">📅 19:52 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-2620">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/kdqCScRGfg6FMGBCTV4xNN4gan7ArabYBxcYRit1hUxJ13r5UcX3R3HbotnlwWfj7Lit9f5TAdrm0le8rLO81MhnPBizu6ALnXbka6yoJm5jSDM83VSfn1eMYvl1dfHiN0n8DUMpw9DPEw614OH9BQRlQ8dyinZ73pxQKf_s_jBtth6CuP6w98ypMdQAkwRl41tOOU8RSaurKVaYkscevwJKTTTUt_ZPhXnC7IpzasrQ0QNXMSAY4glpnYNECh97_c-9QVJzD51yvvz-Vtqx7PLd0otl_VkFafN6jr83FjnVug1MsyBs5IqdoyrMPWOkiZayIh3_6UGIQdnvY8Cgkw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شرکت تتر به تازگی اعلام کرد "به مسدودسازی نزدیک به ۵۵۰ میلیون دلار دارایی مرتبط با بانک مرکزی جمهوری اسلامی و شبکه‌های تحریم‌شده کمک کرده".
الانم با عبور دلار از ۲۵۵ هزار تومان، صرافی‌های رمزارز (با دستور مراجع) معاملات تتر رو از ساعت ۲۱ تا ۹ صبح روز بعد متوقف کردن!
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/ircfspace/2620" target="_blank">📅 19:47 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-2619">
<div class="tg-post-header">📌 پیام #51</div>
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
<div class="tg-footer">👁️ 39.6K · <a href="https://t.me/ircfspace/2619" target="_blank">📅 07:48 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-2618">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/l8199UAzFVugeBVexDtKs3XExCwuvZKlODi7zj2D9RCqeKtbn0SPF14epZIh-pqKLA6LMsCnK3YhgjZQoS_rfFMZwXBinDPvYmMDdGglcgWOSjLlDpf1PKRH5FSKK5uyCviqr3J5W5Tzb7dvMhd5S5-6Hq_GZrdmC3YYAkjg4cx_l4MKY9BKCQi1MO3bxChJK5hp5VvbbGHbNeR3rLtbEeRNXx7dh1fiLCCkYuFBPz0OakmPic8Rs_VDmWIoM0jITtVCi_qKGjaiJA4FlvukyB1YI8DPDjhAJb8zXLo_DQlaBkenPsfTF9gIENr3QU31LYCfetZl-eEZ71VNPnxy3A.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 36.5K · <a href="https://t.me/ircfspace/2618" target="_blank">📅 07:38 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-2617">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/fyApudGCAmq0MfrPM9aHwrfplvvGe6BhkdHcMP6K-xuUqDVxT0t521fX6k6Gc8U0y1uUD_3vKvv3mjFJb3jvtDD_1xEmy7YcDZGSVBpXKBlMKYg8Q25FNWhUHVeMq7rw1g6tDuzyxht0XT-g-5UJQ3DQVLOKnXcXN3FvCQICYAwJoEd0aqWAItFo-twuCBxpz9EetClBsTbrSUWyzvjSWs1hg3W296nUtpF8zg2X3QWLgJHhSwtTUWpp7o4FceOERvWSZyI-KLR_0iGv3r76SKGOj0KGdO0EcVW7A8HYEQ9OHLK8Vevg8TvL9_zxUldadEPnew9n3mF_1s9mq9kC7w.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 37.6K · <a href="https://t.me/ircfspace/2617" target="_blank">📅 07:44 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-2616">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/csL42qKe7E4WO-5WYaBFjKAzH8QIw6PWjZlMC-UFKkRP8QruHfEJci_E3g_SPe8GZGa5mdAIwEipQijE9EZjPrEjhukdlPNAV0-vWzUlrz3Jy8AYMyQK3fZSt4-EtN1DxfyjF-cMYm7XJOjwDkOMr4hInrUv-XO-GJ06HF7Q_24CnaRzauoDPQG7JzNzUrSqHrdDdPkjWVJ7dzIcW0ng_c2XyLSnPU6ZTr2pSf4E0pWjAPIKM3n4oeGdG0ihNwIrnYmMUKdOJO-yyeSlWVUVQcykIp1xuFEG-HlD-d29nqOx0eGkti0A60F6apZeX4ifWkGJJcVDvAZXANTCFXjSnA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 38.6K · <a href="https://t.me/ircfspace/2616" target="_blank">📅 07:38 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-2615">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">معاون سازمان تنظیم مقررات و ارتباطات رادیویی گفته "حجم‌خوری نداریم و بخشی از ابهامات و برداشت‌های کاربران درباره نحوه محاسبه میزان مصرف ترافیک اینترنت، به وضعیت ثبت اطلاعات محتوای داخلی در سامانه تعرفه ترجیحی مربوط می‌شود".
خلاصه: حجم خوری ندارن، ولی باقی چیزارو قول نمیدن!
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 32.5K · <a href="https://t.me/ircfspace/2615" target="_blank">📅 07:34 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-2614">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/VXD3k7E_cg377MQsif_p194_ImLKGZ89F2kIxVe0GHLZyv2MfeiMfRT0iKEbWCzm8cHOmK0BDjsnNFyFyELyFYG7O7sxS3gOjL8LfCWVjF66zwMq6UvIK9vlihZfPlLixaPx9f2W_t8gJMdVllcYa6hKzuxQOXSOXK0uTbxx7dysDa7OEozwmdv7LtZQvb2wQR5mWRHoH-G3upiDIyxUvH6WUzpLZBGL6_zUU2fgAL8E1OlHlsQaanjIIyL5-f5h-C3spBeIs9uKyO2ttGv4bX7E2AWi0U9ajpPK1MH15TQSy66rZjvlltaN3SNNQ5Z2NEw6_VeL3Yu_erS1AS7erA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 39.2K · <a href="https://t.me/ircfspace/2614" target="_blank">📅 08:01 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2613">
<div class="tg-post-header">📌 پیام #45</div>
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
<div class="tg-footer">👁️ 30.1K · <a href="https://t.me/ircfspace/2613" target="_blank">📅 07:52 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2612">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/sboXPgquNbUsn4wtan3JJ4_hPO38xiBAVcvZ7l0_i5MeNoua03mEoL8QRv3Vwfaa9S2bQAokL_2E6k_Ear3suoP9jOp8MUtFlyKGOs-_9Cu7Px9DCxJ8y0AqKtpvkLchAOJHjIh0Frg-Iid0JBxu0k7xlhxvPXmukrR3T_U6spJyETceRg9uHwHhfGHchpAKak4y4Nq9wNwX3EgniLkJbrDToWiYSsOdixLahLzzaF872x1S7mDWaMXOGkNCj1jsIQLZ8BKdWpCagZbA8tD7FIES-ydSTq7982ETOnjleS-0ZsPoG73Wa0mfGtBA2O5WbH7ayzRrqZLkmQxj2Y-nsQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 31.7K · <a href="https://t.me/ircfspace/2612" target="_blank">📅 07:45 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2611">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/S0XxwLUFdJVwPO70Hnn2OK1tWcdgemCxOPFPvcm_9YVlTt4lj3rFZSy7npJyfo27IvUdrrWqXfRmy5Uh5EAPwGkVDFk3u2RE63QGhKeWt24s3OzLvQfYRxOJqRxoOxVjFwZbfIB7Q4rDBUjkIXPNRTvG9TtVLQSu3byDeBSvvFsFSqzg9OLsT3AV6MqOG3seC8z_j8Qj15eN4-zuK-5fh7xHE9rm_MjeTZNFXeSUhb7_Iuo-sBrS-bEz34SrOyC0t2aWTrxrOf0620fBFmrSqgFedxBi6HRKaJ0M6Le6LWJrYq2O3OWPQv0O88k3zR1LGywXhbiam6sgUQsR7emp4w.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 33.5K · <a href="https://t.me/ircfspace/2611" target="_blank">📅 08:20 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2610">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/DYK-dGWN06oFe74wKF6jLjYzb7gsdBg3QJose_-fmJ8ZAtRv9WJ7dR3NlD3horI3q3wncPY4hEUEGxNPwnsTMuhG3cHDx9GuJ0dkaTh15-tJPPCq9hng9xfiRYESZ5UetxyqbkieB04_Y6q3v_h0p5dqxXPCOE3qLDWTZYYvUfPalXOYdda85DSt-5NqEykijQ-5vN9fEsts2XyiHVA3xTWp7J6Qfe61j9sRmu9qANjiANcngY03t0V8Ws2dhenmqi_AVcdQKYoWhMHyjbaLT0G0FqQPkwcGSzyZrsgMP4nhrdjubb7gHvVwgObR8-WoFuCe8JOtaqdk9Cn6sl0O0A.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/ircfspace/2610" target="_blank">📅 08:11 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2609">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/c3RCmNPQyIAALkGTXFi9xZoDQICIlW9aT0nup1U658HCIWLYESeAG3OZmcp48kOD1bUkkv6Hix-wbPWWdO5t7GpcF-kmYbUh8qjxqG3A8jKrPlSYr2SFNb1EB4j8XTBpY-2zi_LRib37tI0B0YVl11-G7obDJTkqJgVoDPmDVGC5GU7ck6sNIJV1la7Qd7VyZQqU4Rbc62NND07Qf7ERpNSKKbZMjcqKthNRufN0FzDhkhlLOpgjWZzFOfUTxT0uEkqtEup_xmfZAiiE74M54EVwhsD--0qnsOrIq0BHa-v6rvDE0lVUw3Z_Ys2R-HRb2yDmDrkRP765BGJvurJGxQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 33.3K · <a href="https://t.me/ircfspace/2609" target="_blank">📅 07:59 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2608">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/vuScnbRfBEP4wbnZHbo_--8X87xzKLVeg0ikWrTl6-z3KLUhfi6lpORfZTVKuXixNWzmbptumwOBmj3tP-SoYuqaYO9TOymhbl7cN2EG_WHlNjjWyQF2rblAmJTyqkW6-BmnwubS1SzHUKRxEIz1X68aaEqlEtTvG8JWJwyne0O11beQY__kU8d-uVPlzQKXrnmvk-rPyk1N2yi60UelQ6y8_qdthN7Wj_2e0YVTKJ5VvO8163TbcHz8EonejABU6ahJ4Puy3xsKPUgcPOWB8lcOVnoOPP-5A46OBqESXLaae_HUHT1tCw-Tt8cUxRVVgF-YF_vm445i2Rs5oMZY5w.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 38K · <a href="https://t.me/ircfspace/2608" target="_blank">📅 17:35 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2607">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/QtMgGA5vW1aQ5ser9EBROEAgBVSF7PIdczx2N2kUES1wGrpIQ_Gbm5Woq9pOnf0jnGaJ6S5LlpUqTVBCc3pzQLtoZn_D49sJHcot_9SG_uMVThnzKYC14oO2mzNYmOyAxseOd_GxL5xAQqxofsWOjECQV6BLpbNG9qkrz_YmPLzmZZL9t4cz_zxziaHRDEFR3kQJ22jPSBtckvMC_c2AD2zS2gbjBIguN5hRd-KfY39h_N4EXYqUVDUMDlfnCNqIMZRu2S-OWyAv4RBSZxnKkiECH1fdmBtWTuw-3xA_9kc_XFmNkZWQW6GauZBI7ezIYRBDT0IN8PHHqeRFJBF5SA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/ircfspace/2607" target="_blank">📅 17:30 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2606">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/k7_A8aZRwyzz8zQlMUp7Cat8AbX3hko_E0pB_mDZkh8CoHC-ZfylC4IT6L00StM9u1bwO1snV8jfZIoa_F6lBLo3PAWNW9MPBW2M8EUpmq8naX3LacuxvsmJYUECIiMMVBwapBPkxUfis6pIIktRiQ3CbgybB1hVP-fL3pR9Vodyq-_1uZ6WPlKtrs0J00JViWwjkPl2OqIsAeBL8p3mtUdt-25rVI6m7rAArGuJjqYnWOwUSr2f2HnBSbO83kXQfnj1rEmuioplB9mFseOwoD0ztF107U_nmOWb3ATzlOSDZyJtDVIC2_mDauOGSdYdvF2SMxh_PyiC30NSzNLKpQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 29.4K · <a href="https://t.me/ircfspace/2606" target="_blank">📅 17:12 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2605">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/uCK5TWuENMF5_wxOWmqbqjJZ6OtsOnYscvrRhmDXnx6SuKeXCUCBLlxkQFRCmFmtnKnq9ejHas0NTK8Kue3ooMzXuI4Cmdxb2nkxmWwc51dJu6u8Ydv1I09Smt5ED7DHAqcNByiUa7xY7KnvDwv6jjpADU54ZN-ZqkEFY95VMvo3hzc-WTT9MoJpMt6srCwySROLqjcyAJN3n6KUXbQTMTrlxr3nzSW2Nnsn4DoxVHUaF2d2iLQnj0Z92SpTunuHU2mshG_l5nk3p7Mck0bLGlq-uk5MoCh0i9NitB3w_j_okKvPgMVwlGEksLRqyRZQlpNqbIgzm6JoAC39WlWkhw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 32.9K · <a href="https://t.me/ircfspace/2605" target="_blank">📅 17:08 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2604">
<div class="tg-post-header">📌 پیام #36</div>
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
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/ircfspace/2604" target="_blank">📅 17:07 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2603">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/sEGHcNL2m4_flY1jj-lmqTTFiWglZUB68mOgIJUtuAJ_yoZ8ddULYImPpOeLZ6jHWfwdymOPGiIENg-Ni9NQ8epHFmCAq9Okt9ZOdHYiQeH9HoRtsCe_JNNjwYGcUzY0RlXhfiphT6IfQYda_attKxjIhWG2S8Wb4Ps8IwizgNxE1grXbMXF-g-xoxupwwXjMBmPqeomktuzii5Y33-2_qACMoANxUXtqYEbcL2W3qakksjsr_NGwmxUtDj3czZgAH8e5OMiVrMD0MvrVbwHDIg14l-30wu1Sk1TzhuwJNwoJU6Rvo-ovbva2JEG9PBz2qOCrDU4-6QkpD8iuibzpQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">صرافی رمزارز کوینکس اعلام کرده فعالیتش رو متوقف کرده و کاربران تا ۲۲ دسامبر فرصت دارن داراییشون رو برداشت کنن.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 31.2K · <a href="https://t.me/ircfspace/2603" target="_blank">📅 16:51 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2601">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/rpHKcfR6PwDP0xnTkWdajSWbhqqeebUfBnZSmzMgVBwOtUFWtThQteVtNWuTBGsp1ZP4MwvDMR3b5BKzEn2Do2YBqXY1jSiyMITtVDuWod8HxAxkFLwVJvWMbG-uNHftqYztM-uO0x6Ukm7rGGjXJvYhQ4nxrsk5m_RL1LaEHeE_SHrLMEJryznjR3WZrEiae8mX8c3EEPGTsKicnvo1jTz4ZDyvMLeOz71ZTDPJ9HYhuRis9E0f_nnjJCQEj8kTJkvh8SyDG9pi1oD4isqQegidebQqmi8zQEzi-Zkq0EPjHlw2XD6DrVrqz09p2Q7mgTSDFFfX11q9V71m2vGtRw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 39.6K · <a href="https://t.me/ircfspace/2601" target="_blank">📅 08:17 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2600">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/LU8l29J1MzEAWBxjwZ5Knpo8jgDqy9K0xc2T6wTD7gwaFgC-hYqeIko0Z9k6iirhDO62nGFq8upaa_jXOAzxtNn3o8vvsliPiC892Iw1GULMDpD4RZpW6ndpl4yAhKiNuCeWcUpQoXrYyQZ8ZU-nV6J9wLkX8lpGXEpTcQf9PwV5lGjuYWMFAS8XaGGpjfkeK6NFkC-DoDFXT16gKxwTOZQs842iUw3oyx1HWgYr103BKkpuGsr5hPn54lU0WhUyRWn3DLuT8aV8Mch64kVwqvi2-loBhntosFcUhHkjLjMitu6lQmJ8M2C42lZzy6TZQ3E4c7gNMuKfp8jux92C4Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزیر قطع‌ارتباطات سرشو از برف بیرون آورده و گفته "اگر درباره محدودیت استفاده از IPv6 مصوبه قانونی وجود ندارد، دلیلی برای اعمال محدودیت در این زمینه وجود ندارد و موضوع باید با سرعت پیگیری و تعیین تکلیف شود".
به مناسبت همین دستور سریع، فوری و قاطع، از تصویر پیوستی اکلیل باریده.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 34.4K · <a href="https://t.me/ircfspace/2600" target="_blank">📅 08:09 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2599">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/b0HE8hj0Vho6MtbqKiDsH8aB4zF-cqg06TyGg-M-Iv1PUuBhRm6BBD8GSIHLamrIzrXXYGWrHXykLeFQMZeVHjHin8fyhqlayXqOmx0Pa-drGoSBdNnjo6YownmVijP-8VXc_gD1aisIlwTkwT6-41RB0rPIMYOYjIeig0o3Aa7R55YCMga8zyMQaKXtXZ6MtO61gnrgVRGjM-xREOCfOjhXo3NTN9sXUepMNFuEyYRhSjlPLtn01Ur3hgV58J5tcFJPw5eo4p_7dGdavxQf9VZuGJUrgpfzwGA9mHhOk8k_RammH3mDeRgbLbPhxH1YXXWTf2JBN6s1pjCYeCsAvw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 45.2K · <a href="https://t.me/ircfspace/2599" target="_blank">📅 07:53 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2598">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/RRqVArPRHetr_SB9eujwEtbLkqhKKoIG7W1WPI-NrDc_k63azZZihRAkSGt1A8USePLTxrGaQ6RVuz1H530e7VNKqbCa_d1aSRrMQ_xPsgzE9in5RCE3clzBR47UFozHmkOZMzOC6Y3cBVOlKGuwSDXQkWsL8hzm9PAXa7Hk6pE13wz7KBK17fNW2hGI2Khop9WlXFehirFy7hQVZS_HV8JogEdXACYFRVJ50WhglHOUA4WOM8TVdYLbmh4PaPiOYTXETnZ4L6_9F_USkIWXC9noxV_Gn4dwcngKCOHU3g4pDE_vulKZ2o3b7UrJcfwySpneQzsbx5hH4h-FTnPgkQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 38K · <a href="https://t.me/ircfspace/2598" target="_blank">📅 11:15 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2597">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/vs9g7EPvIvJTKtlvxFag1HWplxX6CErJKAd83TohqgNtBHpphtH4JWsqRWc3SFcaX9pXTTbt068OhHp-9uRndYHnRIMLULrDWOLUUauXKX4jCxMDKv6loPCwuIegnfAUJ3ZRCgvZKju2yUTKnYzqTlrgjrhfUvVOVAvcvEkWje5P-S7ZEgkxtvZWn3gJi17wrbc6jBAnzOLN2NuofpormbWbbCmPgaf_Qx6qpg0YWIT7H3QiBH-bfNHlEJWip7bvHZoPNzPv41uFHFzxnS24SnweV2aO621HVvR7cqSN9UJ6nMBvEZMtNoRz_wS4qlpTisZ8rzZ7b3skXI7q_IfjUQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 37.8K · <a href="https://t.me/ircfspace/2597" target="_blank">📅 08:00 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2596">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/kW8caYD2j61zIrFA3MVnNtOTDMTLuwvxa6gQ0TP0V3pf3U4Ad_bh73-cPKtNJrub8CEdcaj1Yf8j-UNQCrJMswyhy2cTTOeMnELS5T2BYV2f9bnHZfq88R9EVIMN7xmQyO97TdQ0vHcMM-EJ0zfJY8D3PAKWCBMa0abhFHRGTPIUZrKjEv-TPyKd2z_s0cmD4KJ2UAIQlvlwfYlAvtTWqR8nhM2BZtLBxf-VKkzbmJdmUtOgUieV8gEfUsLH216NYZVf-WJyI43hvRzbpndXW2IfuUYT4a9bnGQzj8WKSRo_kEZmZlPLcdGTeYIqGMbAA2rRF78tQYT3R3l7vylOig.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 90.4K · <a href="https://t.me/ircfspace/2596" target="_blank">📅 08:14 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2595">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/tJSz_UcXGLg-QELt7cmgYSaqOUoHfXE54qSmlOYtvQ9SeoPiR-gK65jUWOdXJaYJkMn-_W7wCyOopDk_7BNVS3fuglabwCoTERDKEOlQMbUXCX6IVmSMdgi3kXaamUE8isL7eoogEfziiKz2JWfkmoswr-tZifS7xu5vQZiEZ1X7OYv_2iipomCDGyEE-WsOfT-pwUagNE21lnknVzypuJ26_KNSct78V7iGCH5jNCzbjjuVz_2DMqv_S8XlWO3VNXDltw9euGSSbi-xLjGV13xrCOy8uDKukVIWeQLpZO62d_egA-O94iPuZ1lXVliuVETaB7JrHnbA6f_zm4w_gw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شبکه پایدار است، یعنی به همون آشغال‌نت قبل از قطع فیبر نوری در ارمنستان برگشتیم!
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 36.6K · <a href="https://t.me/ircfspace/2595" target="_blank">📅 07:57 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2594">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/sHfOvMQKuOWQg_lljqic8B9OODOI1fExYcJkp0mnw1jRmWeM9rX20J-4muSPNfIRdx45Fk5kJu5d-YykMgcBKPPYnMKZjkcIcfR8geSvUnqO0vM_SOTImG6ulabFUSVLHQqVkbCKJeezoCp8-c25xNVudxvyA9xBjI26DaDU1f_fjs1Q3XqdJc2IHF_9gAoHVgs_omqdOZXfFdbpOE1MPATxi1tMqA1yqg8PoD5ATa4InafJZN_I3kIIg-9B1Fy_MvEzmtYaObHNKtCiNZ8lVV5eYgb3dpfptKpDqScs7llMRm_jVGMyvHPLxeHApERP76F14X6CkpJBItwAwWw6Nw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 39.7K · <a href="https://t.me/ircfspace/2594" target="_blank">📅 07:49 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2593">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/i89Xehn4tmzmn6KajApepahOzYWtzTHiJgd8Rf5_V4l7MjBQJEa-uLIuoVk0O6sLgwGaYVemckc4fhuJYIeKrpAT6UnKl1Bq9Kbw1-ZhgIaRHYQJK_Qett_sFat5n0ErdgyJn6IkFZC096y9RhWh7C4TcbSfpvVofQi-WtV1ojFTuTgimraCyBRNfFiJ2n98Fk8Vbj-GyPWX6VT1LNRRBqpK4shpMiTwjHKHl04SiL2y8-TKhwTCVBcSeW0f79n0Be8JehbZ26wmVbNbj7yHXLCJSXeTqexfQfO1Sayd69Wv2fkbfwyCmK0NmXizsceoXMTJQrA0msXFlsheS53rZw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 30K · <a href="https://t.me/ircfspace/2593" target="_blank">📅 20:10 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2592">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/VZXK67K_R5_cOe3cfpDLaB7awKb1DMCQmGy45pEvtdKslkqT9exxhnUABeWA5VsAKVYGGbKas7Umlctt8nZcBi0W2ladxAYME6J0JqCpiRNOiGEXNL7tzu7HSv8f6UWZb57SkoTRf_oBV7288D4XpbFcvzRUKBqJycJAXyQ-YiWuFvN4gs7tpC5I-cwb8LX4n3sGH_d5jneM6xeguSyof3TUe-MycHPwuN_FhX3lq_l4VhpjwLU13ImDKGpJHs-aa0TyuBOFFSYXpcxifQASsI7WY1fgSJJwrn84jR8tfqcNaTvLzlNEMu5SsxGvTMtFktRx34_A3uhnQBqNnMrUHA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/ircfspace/2592" target="_blank">📅 18:53 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2591">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/IzTvBxefddW0ONqQmGQA8WYsoRre9FNQA5U3q5jpz3TlyHn12845WufDjyaJfs-gWuPkGHIoXx2ZZoiy6YI-v3Hg4FEf_FHnA-upKB3Hg10gnzlHiZvZ2jHpVX-rEvS7zv4t1oh0R0d40K8spAt0k9t3i3VfLLb3S5ZbfZsPdjF3UY8kUv2M6bISPzGsDhJKf98fKCBfhPyIRU-OHgAPPKMLkK2iXTwffLz6OOIj9H3AE2jlwvjxfzOmsx8ThnPSY-etK724whmanSaR0p6RrtiJOfAPKyGYIHjVFipA7CfGfnyxsvWhwxBEIfQhcU-RLnn061O9M_A-KFeoGVP3AQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اگه کد QR حساسی رو می‌خواین مخفی یا مخدوش کنین، نصفه‌نیمه رهاش نکنین. ممکنه اطلاعاتش همچنان قابل استخراج باشه.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/ircfspace/2591" target="_blank">📅 18:43 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2590">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/f43VcpTPynYmspSYkDUzFXiSmjsnfnApesoV6oE9D3UTXPleZY_zqEnF9U6GMjWzP7lxFPEaw_QRGaPswCfOQT-Jb_6PdIGQL0i-rjJimfL7VwBC5ZXh3u0HxPVuLyJpCupGuAO6Xb0HAOqI3hhgFp0SqvmeqMm-N9znz6fp4uI5Hoj2OjiDbG-nzf-fVPXRdGQ7MWCXn96s-3nQBehG2dgRdH6T7hLGmSNnLqDA8OJ7lRj0QVtuzjdeVAnXJUslYRHg5SIyGF-RvYrv7atjExFdIfiMwccxk5gyZ_It1vJM1jlceaeFNAyhvyVz9yPyN7s9uqUiKRF1pwbzbF82sA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 28.7K · <a href="https://t.me/ircfspace/2590" target="_blank">📅 18:11 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2589">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/K3UYUhElO1DvNPpKacFpTt44WcuH6KSy711l9Aex4pJv5S7T1KNN3k59UTbbtCbHslbj_t71RTO97Opv31uasykUkJObvmipPsf9jrEE7ENDObiNfA9CniHFzki0AQT94pijs3ojOfcn1DQzjYpekBhQZEutzmfuvRd58HlMENs8ghqLTA8Z_9VTy9PxHHFGOcKeFlhmQhrNfc91CvA3PZtyIDStw4VvJqpTPyLM4PZKp6qOTqojo2KXOSMwyUi_usHxzi7cG4OZGlDlL5J-iMEEkZMvem2jWNEYxEB2CRSg4wc8TmgYzOztURaQHwTNRmMkVLKWf5GKjmRW7yFiKQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 31K · <a href="https://t.me/ircfspace/2589" target="_blank">📅 17:54 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2588">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/YHzGUIavTlTrc6v2lYiQKEadGWNKmCUeL_vCvBMpQ_keQHvUhuFwEwBpSEtozj4V_FMiLEKp9RFP95TQR6No0Ybrl-m2vGqyp71HXKEuxUZJMPpzE4pAYqvuRMZ6pa_k8pCFJoR5Gkb_NHrUbSt85-bUg0DE-1TydA7X2ZX3XGQxl8ljojado40omL2LBsQhkOL5gtoN_nHHaRoRloNQYMuLr_eFMdegnhP3mWetVCBbXYuIbFy3BrjaAEm4fBaVy63lVHik5DGAP61ZTyGOr3YoBMHHmR9IgEUteAmwVIkNdhzmW1ae5NkLmxvTkRkf03sJwmZ95dwJmqfB9SaJ5Q.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 30.4K · <a href="https://t.me/ircfspace/2588" target="_blank">📅 17:22 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2587">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/TfEnKCgUwiv04lSWBLngBZr8dhF3xnb204ET1cTyxvgTNlRJqYK7HoDhkuU1wOYCDyZokpRlVsXtICfXfe5AJrQWSlYycRHESO6m4X-T-2EfspAtKxUPumtOjnY91plQg8lcMGurVJ0lO33YRBl6jIWmukzCx5PLUCnpuxZp6DVxBC-vd2rt9P8xEojAJOvK-a6pMqThpy6-gJPaOxywJD7-FjOOEcKt16Jog5qBVkL8gI589PA7KCrhC7V2Whr3W9fj75m_GuYdXo5Xy5hCHVPRBWvFRHARBVuC_VBgZPocGHgtY5t5VzuxUaF4hIxbyiWe_jVqdZp65WsGPo7s-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مجلسی که خودش کارت قرمز داره، به وزیر قطع‌ارتباطات کارت زرد داده
🤡
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 30.4K · <a href="https://t.me/ircfspace/2587" target="_blank">📅 11:41 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2586">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/rDAkZ7TbblP-vkb_EfRDM8fSEH6zGRutoGIAe1FfVRlQm9D7_W21u4GUjy8zOOwE8NSKZRxuF7NWk-x1Sn4j19DgkEGcS_5Q4rHtXCUTFVnbU0QWWGaSw0l-dD9l8JNM61F4QPo_B-aj8CRm4tDkpJF7L0S5erlgtmNrX_QvIFR0RuinlMaVsOYYewfMBgcwWUl_9___Negl0CBV6pLtuhazG_9UfitsgSFvC6q07S4cbUCWf0UGGwzOoy20-qIv7y9ksV5PLidY_KQwxlOqU-_YflxjYF56xV0iRJ5jkzz2T9HKL40d0ts9rJNV_FQsyifwSpKTMRd3Bd-XDBZUJA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">معاون ارتباطات و اطلاع‌رسانی دفتر معاون اول رئیس‌جمهور: طی ساعات اخیر اخباری کذب به نقل از اینجانب درباره رفع فیلتر اینستاگرام منتشر شده، که کاملاً ساختگی است.
/اقتصادآنلاین
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 33.8K · <a href="https://t.me/ircfspace/2586" target="_blank">📅 09:11 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2585">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/EudMFSSSD7M52uZtYOPIubezWENfCWnuddh1dopgTK_fGkROu7fcK9daIZK7-603iwL0kU46fvhL-DqoP0AHlcn3acEwsAeSSmfSU0M99trj4MlNgx7s4mN0kqDFw_YTC90xEAlmFgJSwgXK0Vv69Acui_C5ph_M8LmWcwCb26tbuMGTxBjF0GcrfYy0lTRjMnXlypAvHdYfq4TFL3mRrCSPKpvMybfGfvebcG0xEzbCbIPMEMIYNH5Eyb0NiDJclr3UCk1n3wrf5Mx8_sCtw1sMtVX45Bm05E7m6nUOlpQP9O-tKYbP2-4vCNq001dIFRWP8edz-61x8hqIQfRiTg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 31.8K · <a href="https://t.me/ircfspace/2585" target="_blank">📅 09:02 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2584">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/IGC0a0qIOUEUQfh15A_K0-hlucKd4GSHMjXzA7ZPaCAfQMKP-isar-JjGjV9OYBDd5a_I0EI36u3t7HcYMBVupuncqSBcNn4-lX3Inp0VR0j0JzvOotWeygvmlj2lIpzrHwM2j9d1hdHpnaXuNArqR1AydWvuYlzehM81huzRklPcCbbBohm81MaCheAyfFfF3s8f9cZPSUA5mrlKhyyyDC51uaEq0fMg7Bt4N1spPK9oZ39Ow67G0tuj1h0k0hNI1kCOwzbzPxn_dDeeuAfPgF5dvJBgXNE4dB-q-O15UAhH4nCRI5wmd_mpD3Br5KGNo_evg2SqJCGQOCxyc_JSA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/ircfspace/2584" target="_blank">📅 08:53 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2583">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/cB0hmgDonh439J2j1VnYLXs0h4QxKEWfRJ9iH15scg0vm-tqe5GJu2vblVv8l1GtEb8f0tUOgixdGZq-PXIEBbr97HtM9IXr_UfBGWzoUumPmJABvIWUelNr6oWIG8N6P7r9OAzWUgfRmLocvAFOw2ZWJ3yZxsRlcIdlg_VW1n_WtfmYrlImLu8pheSx0FlBIzdV_NpC9M7wFBZ5_1V6ktsymCCAinBMTThkWb-daQOnQt1njYepoK4nxMQI3cQsRBRVZTK01gsVrkIHHsUwBqJ_LkEExehj0v2dtbwvxyz-SRQv-Ezo_kiIv109IyUleZEn5UNzx3RxXhKZ5pY6YQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/ircfspace/2583" target="_blank">📅 08:40 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2582">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/e3zKtW1vVGwk4Eu0tVO5sehHza0yC2tD4Z-9oPC0BohylIUKi1EtUOUI-el4sPyLOd4uEAV1tX0PK9xt0wJuzm0n4kLBC0AW3Fikc00nSvwi2IYLrtlxqs6p8OCpRSyva-X_tzv9tydbUbBq4kE9IyiQrDLLzEWniAwtuT1BYd494oq-pQCX5-dLkMZrittqUG9J0fBgWBNDhGd08sec25UwgCFzWWr1enC5cwiZro_f45e2uU2uc_-FFpAHbRF1XY0DA7P1R2iIu6ZJtAHMx7wIFI-oxaPDZ7KeXpO7Z3_OEBycFN_pumHvV95XGKmG5AsLoqaTUljKu8vy65Ekmg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 29.2K · <a href="https://t.me/ircfspace/2582" target="_blank">📅 07:39 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2581">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Ld7J0saw6d2CiwLs4cdqybChgY_aFIToVfgtHi8RR9kSp-lZ9WV0_h1XWDTqacQcwetQELcmqy9eGHxJHSG2mnz-IQfugXaU8JPsNNGjPDsPOAmUpvu_3gqXzrCy5R26I0sLO4WTGHb5bF4xFZvVoLFOvmzGaJ-6xMSNYkOsW5HoQzXdUH6D6CL6VsLyEFrU7riOaJCOydKGDuz6ahzDKwvAAQq9COufvUHGvrNm28XAGjkvxDtWpEAPLuN1sLdE2WusAEKtFEVckc4iNg1dV1ORuazbP_w9RSQILx8xJF5fFvatpKhLcJ4o_TH6ExPd1jd2DKNvNF-z70cW5cnmBg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/ircfspace/2581" target="_blank">📅 07:17 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2580">
<div class="tg-post-header">📌 پیام #13</div>
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
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/ircfspace/2580" target="_blank">📅 07:10 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2579">
<div class="tg-post-header">📌 پیام #12</div>
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
<div class="tg-footer">👁️ 30.2K · <a href="https://t.me/ircfspace/2579" target="_blank">📅 06:59 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2578">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/WNnllzziHCRLdswjIU4o4KEDH1Yr3pDujYao0iWEUuD9XW3W3vv7S55gLEoqJVMFbSVo0rqunNL9CwA_YybBq5Mw0ylhjmla0K1xtQFu3mTHLTxwymL9vnwUlcXoZF2prA5mKGs83skjono0GNQ3-Vot54BL5gX92oWr5fG79Il8f_gkCJpY1-tS4X-724PEjzkNocCDTcr0geS46DbGBYbXCeCIK770N_aSbep56XGSagOpXERBdiiTEvj6zfz4m4oCMPFyKSSjPJJH64Rsr58CbB3mndCoVYBeO5m9E9EhH9S8o1WQLXAPqwotsr2fmD4qsdciBbwZmBawWFaWcg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 30.7K · <a href="https://t.me/ircfspace/2578" target="_blank">📅 09:57 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2577">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/K1JL93AIT-Om_nhJcqW6NDVYQ4o2opoiS7UhPoAC9OtLM7IlSmo40iMvZ-bUqFK3nnSjArskPfYlKLtEFtMKT_ah8APxz6tz3y2uvQtKu1qFnio9IdYmIkX2UTR9a9ydVtefxLVf-ClMbRSteuGDLhqV4bp21cd_GHh5gkjpEDlSf_-w__1IjSdF2071U7YwjxvdAWPeV2xhAKTUYv6cTHx4_U9ImOWeNOb1n-ZLpyzRCopcocGYaSc7e_G96eHnRWrGnDIdzGKOCBV1_lxD2FOOxy0giehRgKdamq-BgTODTTjlHFHCjKaki0YIy6BRinyfl5SeXPzWruY_XctnOA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزیر قطع‌ارتباطات در مورد ۸۸ روز قطع سراسری اینترنت و بعد از اون اختلال گسترده در سیستم بانکی کشور خودش‌رو به اون‌راه زده و با سیس عقاب اعلام کرده "آماده انتقال تجربیات سایبری خودمون به کشورهای منطقه هستیم".
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 33.3K · <a href="https://t.me/ircfspace/2577" target="_blank">📅 18:47 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2576">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/afJV4Sg4iOUib8gVpAodoT8AnbVQbYKI92s-7NyP3VgJ_w7qBZ8AlxUfAoFFt9LR4Y2waAfZ9QyNlwfnWccnbIZXMk28y4BY_T6xrI5GL4ZF7BjdcVE395x6qvGUs2lo8ipM9PujxpJOrVb8i_B9lFE-Zfp1b6FEyWqmTPgceBE85-E_Xwhjr3Cg0N1L671NCoH-P8hDl68hkvrW3KEscR8-XaAO33VsEJ_tjv_4jCl_YUiNz5-QXXCuBBTyLgBNDtW0LgbyJmA2KhFaKbWaJFYj41bWh1fsRgALrYI0LeCZhdH_LAFr3YKZUDvivQBy4tx5HptkVUofmfh_ZF0mXA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 36.9K · <a href="https://t.me/ircfspace/2576" target="_blank">📅 18:09 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2575">
<div class="tg-post-header">📌 پیام #8</div>
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
<div class="tg-footer">👁️ 43.8K · <a href="https://t.me/ircfspace/2575" target="_blank">📅 18:47 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2574">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/DUUt0GCncoVTMUn85DvxuEEVEtl2DgUHqrfd2ncqmHYMkl4Cgtf3W3b8g0MrVz_or3R8RsAlc4f6nwdBEtAm6kBl4OuQxksLPqD5yY6m3yRkUc0r9em1mJ832YXwszos646yYzyr2wDMAZU-4wKRNrre1dKjLc-Oc6FHQNDghHyLAwsOqE92JPIxBklXSHzn-UDkm_lAcb4Mkh3fMInCxVv4j9wdXOskBeEy9oKuozm2YG_fNRBLfDYqjj_Klm8pLeJ2JQzvFMJwlswk_MgZfCpucHzrIZOMLqC_17rCyLM5tvhL6niQenQrIRm9rCk7pg5LogZKuc76XfOgYholhw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 45.1K · <a href="https://t.me/ircfspace/2574" target="_blank">📅 11:52 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2573">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ISCGHxX8zdPWbEu7fWgxFgh6QlApnVmonnN47MyegbnWjQZtLNqlpAfqr4_XcTQ-CdRRkiLGRw2VIpy5HFrK3HfozM8kwCNL1ZNBBeJhVukMYBjOiHUkrb74SfRQwzrY7jD6fNcuHw1bNvcfiDCwsxm_tzEvxRhq9gWj_g09iTEu8FGUlAEZeikQM4JNzdE03LP27fxlw-5tJW0aYMgnaSVdCyB2PDaMVZRn0-dbdS4jLhQmX1Xi4rif2eEd2HRoxebuORxI4TvPm-yegwJgt4UMxV9VJOElVXHVDaIn-mJE2FdFKjRXUv9WDZnxQ02KGJtkaITg_goJ8dFlmKnFkw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 36.1K · <a href="https://t.me/ircfspace/2573" target="_blank">📅 11:44 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2572">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/jgHJ9MaXie7SCi-yJP89hy3Id9UQWf0fW3DM-phLLCcUKInxtaFhvPGR0YlsICE3IOBC9leF7t97f2HeW7YRK3w-XJBsntYrxPmPDCvYKpQ9AWQRAbTCY_UmU5CPKxFqlzwHRz79Kb6BFpS_gA0CyIP-gyTFEub5ay99PdhGgVe8lUhHiGLUHEbvRWTH522XgdomqJ21JGMeqx87MH5fZtskaJtegbVEAk-b_EGmUQQCwtI6NDfxigjkCJm-QJZ0304O92mfqcRUjqmXy7mt1KA2keWneZ8QUmyG7JxP9A5lb6JuqBvWfegaNxkkbnC9TBqKvrJ-FQnhx5kutocdQA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 35.7K · <a href="https://t.me/ircfspace/2572" target="_blank">📅 11:41 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2571">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/S4UPe6OgYeB9fFPR0m1YulDo_DCGpaAExBKk8zphtJ8QFFKQCVDl9ll3Nba6gxH7QaBaPLzUaC4aITG-VmUr9PeVYvCygexNbo23ss1a6jixcd9Rf9WABn4Vsx12l_FuLsZDWsHeVFHYqByNXBJK_wpavdsse5tAR7sLgYTiW3QtfIsGLj0geqpnb5qwiAu-jy8Yai57y_VzWUuMdZclyt6HakHWIxSzBgri4ic3ZR_f4tIiBoOrHbvJXUSq4oT4GGZyjMjq4kz-xC5ihUkV35F-J6dwnRIiPVtgDy6Pw-zQLAZ4wzscEoizY2t4zU0dN6sTLyTd5Q9X3SlSkQqvaA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چندروز قبل وزیر گفتاردرمان (و فاقد مصرف) قطع‌ارتباطات گفته بود "اگر استفاده از فناوری‌ها به نقطه غیرقابل بازگشت برسد، بخشی از حکمرانی کشور در حوزه فضای مجازی عملاً از دست خواهد رفت". در ادامه "بستن پرونده فیلترینگ را یکی از الزامات ارتقای حکمرانی در فضای مجازی دانست".
فقط نمیدونم مخاطب این صحبت کیه! اگر مخاطب مردم هستن، بدون تعارف بگه بیایم برای پیگیری و حل مشکلات وزارتخونه آستین بالا بزنیم.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 33.7K · <a href="https://t.me/ircfspace/2571" target="_blank">📅 11:34 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2570">
<div class="tg-post-header">📌 پیام #3</div>
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
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/ircfspace/2570" target="_blank">📅 11:30 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2569">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/v35qXBTKFe4_Ki7MiPMEDDhrmW3Pg77FW28dPg1f5RVbfXf3ovgxA_VJH0HDTTCDRW2_daS5Hj6VRbjFvmJA_3ORUPUTUZihEJPKnjraJmzWHz8tUgp8auADrPMTtHbICJUizIkQIpLAfG-nRUML0LkrBdxisctQvt31NdiJzkLtWuM6QLFdxhiTMmd8e3UX52B9OSId7fzBkJ2vPVNdhP7YLuqoS2kS3K8jpF72_khg46rLHIdsjJX-8_qGAGWDrgced14cJrOXU2DVeTnni8WueQRu9PkQnVT-qafuk7gqVAaCPW-axo1DXcpubu58X3BmKMCCSB9FbOpkSdeHaw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 33.3K · <a href="https://t.me/ircfspace/2569" target="_blank">📅 11:20 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2568">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">از بین همکارا، اولین نفری که تغییر شغل داد و رفت سراغ آهنگری، شدیدا تعجب کردم! با اینکه خودم کم آورده بودم، ازش خواستم جا نزنه. اما بعد از چند جنگ، کشتار معترضین دی‌ماه، قطع طولانی‌مدت اینترنت و حالا تداوم یک آشغال‌نت پراختلال، آدم‌های ‌کاردرست و خفن زیادی رو از نزدیک میشناسم که سال‌ها در حوزه‌های برنامه‌نویسی، طراحی، شبکه، مارکتینگ و ... فعالیت تخصصی و رزومه قوی داشتن، اما در این چندماه رفتن سراغ مشاغل غیرمرتبط مثل نجاری، دست‌فروشی، مکانیکی، واسطه‌گری و و و ...!
لعنت به جمهوری اسلامی.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 45K · <a href="https://t.me/ircfspace/2568" target="_blank">📅 07:54 · 03 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>

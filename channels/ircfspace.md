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
<img src="https://cdn1.telesco.pe/file/IeQgqEogaksF80WOKKXkerdwfUT4-8mIdB-1LEne5UztoflPwAaWgdO-8MKD-ECRpOt2Y82H81s05k1xfzvHFBOPD3k-t2cYNPJ4UNmIVKEvaoqN_E_6iYKhD8o0dOM5QVIg2LLzW9q9zfIIY1wKrt-TPk9wBSe2lD1UKJIuLkdRowR7MKpO8OgIhdoJ0u1r6ipMbQZuuXuU6wUTcMyaljMpd5dOdeyI9B-nFGdi4Rf_sSBCw7-IFT4MMJAxgkwEUtquou3dErfpBOfoHhWr40doVSKFT2SVQljCek2GTXFvUAYI-0hHW2g3IsMhw3-KrLJzRobgabTpNRxCmhOzkw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 IRCF | اینترنت آزاد برای همه</h1>
<p>@ircfspace • 👥 97K عضو</p>
<a href="https://t.me/ircfspace" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 این‌کانال با هدف دسترسی آزاد به اینترنت «به‌عنوان یک حق شهروندی»، به‌دور از هرگونه وابستگی حزبی، سیاسی، تشکیلاتی و ... فعالیت میکنه!https://ircf.space/contactshttps://x.com/ircfspace</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-07-21 15:51:52</div>
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
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/ircfspace/2672" target="_blank">📅 22:12 · 20 Mehr 1405</a></div>
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
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/ircfspace/2671" target="_blank">📅 22:03 · 20 Mehr 1405</a></div>
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
<div class="tg-footer">👁️ 13K · <a href="https://t.me/ircfspace/2670" target="_blank">📅 21:59 · 20 Mehr 1405</a></div>
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
<div class="tg-footer">👁️ 13K · <a href="https://t.me/ircfspace/2669" target="_blank">📅 21:52 · 20 Mehr 1405</a></div>
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
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/ircfspace/2668" target="_blank">📅 21:44 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-2667">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/CPXzPMPW4-AyUkAE3womFefdk8DKAizxeURZoZmCBVtCHyWKr6eii3sHGyMNFfHDe5dreLUrH9HD6oj5VJa2P_u6PP-pLoge8aTpMFArMovJbO72-KxDXiVPJekInI2TbAbJPtnAFDpRNI8Hf0zmlpuR1t3fvi6g66jWFHcts329GWdPTJMKhn2X_ZYlLOu5-46nNK2vJlVl-7F7QNZaXY3LbNJ5xCTUukmWf_-B4kZW-M6ZksolxQopnVUVFt21m_UkKl3nvpdXeC7coTwcU_AwkVeZsn1gGnCRCLuEtJ8ZawA3byw_WcLSE-Zc-0fvdA8qSCRf8fEIUdSVK3UFDA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/ircfspace/2667" target="_blank">📅 07:47 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-2666">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/bOE11UDgjEAEIwqdd6vYaMG3vzL4KHHcZ3plDf37UoxZ8OjWygshiL8xd2HGZmUMKFThA1EytgK82npBKiN3nvhGAOtMgR68Q664axrg5zf91hSexRs0qRht6JMQ0ez-rmMIcpLruh5FcUye6iKhq01gBnFVRyg_zd4uhnfrUe0s_u0nmYRD32b0BaHbij4v8Zt7wFwK7y81McskbShUtnyz9shEZD0tGI2T1vOxBwCVhOPMig9_eis3M7bCKHCNeumYhSXxFhIuaE5OhSxJXYOH0ZP-omoeiC8Lm7NPlwSgxc641s8ljkRA_YlEJAkbiLzu2mP41ekLY_KKuutMlg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/ircfspace/2666" target="_blank">📅 07:31 · 20 Mehr 1405</a></div>
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
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/ircfspace/2665" target="_blank">📅 22:33 · 18 Mehr 1405</a></div>
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
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/ircfspace/2664" target="_blank">📅 22:14 · 18 Mehr 1405</a></div>
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
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/ircfspace/2663" target="_blank">📅 22:08 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-2662">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/j8fd6wsNTzDrsgCrrbUvm3DiXIm2FiyYP9DYCz7eekHtoJCHiW2oD82P_O10-Gv6HWKrjmIhwO3sCIjsTcvz1XeF8F15PGJ3x5AGQjIClcBmwkRo0wZU0JruJXd5S9eSqhYORffh6lISanes6sRDp-hJgv3_BaBhUTECE11sCBmG2T6h0TvjC64DvoOGKygAl19M6t6ntCjEgIZ16fVFhLTlXYrFGQqygLb3ph7zmCU8xWgo0JhdJsI-VLdPvWxzXtpx73U1sU7inwCUQvqDol-OK-mFaewzbjlkK5pXgLk1IvUlIOqEuwaXL9lzQLrE2gq4Vij909_ZvqujWNJMLA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/ircfspace/2662" target="_blank">📅 15:16 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-2660">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/RcvEajRPMLUE3NDYXvl3z8M4Ip935NEFh4ZTJy1tlNGFbMwe2Y7HThTEFwKJ_bneJalSdER5OgmUf5ZCCPupg7PZJ1vd5dtLxWfh8tAMXP1Q_vpjkt6P3UlM30-PTbuvGph-TC8DKb1-NO34ONiXEBzUuSrjJGGM53Q-ILmnxKUNi3zc33NJeTUqF_JhfTQ3y-k-aKFtcpxvC1XkWJq16vdBD_WTBT4lCXfbhlmbKZrQFjI5kAFajN-eU-vSw2JyrpNyTgqHrzQDwCJ_ajA9sb2mCnacdAalOAetlo_W1WdMG_D1XzhwyJmVEb5FRHqGQYDzDy7jzx2RYlgvRsHIOA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پس‌کوچه در مورد Jet VPN که بیش از یک میلیون بار از گوگل‌پلی دانلود شده، گفته معماری این فیلترشکن دارای آسیب‌پذیری‌های امنیتی، با شدت بالاست!
این گروه قبلا در مورد خطرات استفاده از JumpJump هم به دفعات هشدار داده بود.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 34.5K · <a href="https://t.me/ircfspace/2660" target="_blank">📅 15:03 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-2659">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/k-MBZobXl5LHDIDaT2qD1npV_0vRCPmVXd2xTG0k-ywd2FfZHACc2u7yOef_BVMf-6azigdmbZe2jXGp_Aa4HF_ggvgvfWCI9TITl1tLZ1vvfJIYkmlHscyn4jnv-IiQXUtz6_B5bzrzbJj1nLp_-L9uHP93UBugt8AfmA0wFEniD73Y5EkICU5rZEGOZHEYXA_C1YYfTZDwe46IA67bM1Hu6PtC0EbJJ6n-Hk52nimUtaXhFg70V7k0sOsHwo9syrl_e_OJXNdRbYiamqUYyv6kcXlH8u3Utn5dL2_rwdeWNKuGWUjOoZ-gGFdISpBxhqAUXX4GKxjY40kKoFzjzQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">معاونت توسعه بازرگانی وزارت صمت در نامه‌ای به پلتفرم‌های خرید و فروش آنلاین طلا، از آنها خواست اطلاعات کاربران و میزان طلای تعهدشده به کاربران را به‌صورت کامل و صحیح، در قالب لوح فشرده (CD) به این وزارتخانه ارسال کنند.
در شرایطی که شرکت‌ها برای حفاظت از داده‌های کاربران و زیرساخت‌های خود هزینه می‌کنند، مشخص نیست اطلاعات کاربران پس از انتقال روی CD چگونه محافظت خواهد شد؟ /دیجیاتو
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/ircfspace/2659" target="_blank">📅 14:56 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-2658">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/VrgWqFIzbbxboeJfDch_ZnZ3OkvPDU_lOnqaguCpV5WJfkLaUOQa8s8bSMNb3NZMaQbEacJrsVqcF6K7dniF8CYqHfE5LmQZHFOqNdazuxR1a_53WIUckQdiFy4Y3lsJ02GLY3eLwE92f8DAXyivvbXCc8QkwtKbnWy_lyI26-r_zhsrfvEnXWsY2rn1e0qJMTocHML-xaz8tLClGpgBk3243kPqGHG3CF6DzZ9nzQsMJ9bQylDxeA6g37jQXUOhaIQXP0XK0cfi9kHxtyAw4Wu-DG31HlY-QxP57mrMWc-zqFD8VRMgyyLe6kWVJzm8UNNvsq_wDnyIAkrJSwLHvw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 74.1K · <a href="https://t.me/ircfspace/2658" target="_blank">📅 07:51 · 16 Mehr 1405</a></div>
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
<div class="tg-footer">👁️ 28.2K · <a href="https://t.me/ircfspace/2657" target="_blank">📅 20:13 · 14 Mehr 1405</a></div>
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
<div class="tg-footer">👁️ 28.3K · <a href="https://t.me/ircfspace/2656" target="_blank">📅 20:03 · 14 Mehr 1405</a></div>
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
<div class="tg-footer">👁️ 28.2K · <a href="https://t.me/ircfspace/2655" target="_blank">📅 19:55 · 14 Mehr 1405</a></div>
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
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/ircfspace/2654" target="_blank">📅 19:45 · 14 Mehr 1405</a></div>
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
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/ircfspace/2653" target="_blank">📅 19:38 · 14 Mehr 1405</a></div>
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
<div class="tg-footer">👁️ 32.1K · <a href="https://t.me/ircfspace/2652" target="_blank">📅 23:57 · 13 Mehr 1405</a></div>
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
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/ircfspace/2651" target="_blank">📅 23:34 · 13 Mehr 1405</a></div>
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
<div class="tg-footer">👁️ 29.5K · <a href="https://t.me/ircfspace/2650" target="_blank">📅 18:02 · 13 Mehr 1405</a></div>
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
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/ircfspace/2649" target="_blank">📅 17:53 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-2648">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/vco74nvQ0CzG7u8a_pdcapGjKDks4sJqpdmlpowQM4aTzXCHn5jKXlG9NeTD_q_NQcE0XmwoP_MSZYhS5CSh-2_d_S99ZmBJKxlXqkfXehcfxJy02UfxY97prtRZfGW7MillCIY9YKoYMQqEa0MaZYloaoD8xpVacaxb-ixoIOiCKa8EB9X0UKQ9E9ckcp4QL27P_JdC6RJ8f3piy4bJkuqU2VZRx9LoUArY-qWJE7ngzE2XGdbPsrdEbeqiDoh6WrpFChvgwEoSo6t6_djg1wk4Tbnwyc-djI1vkehM7CDmNtRA1bzFiKXrVXVua7G0-b1I1vaR8EvkuHfCzEaI_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رئیس پلیس امنیت اقتصادی فراجا: هر سایتی که اقدام به اعلام قیمت‌های کاذب ارز کند، باید بداند که برخورد قضایی و پلیسی با آن به‌طور جدی انجام خواهد شد. /انتخاب
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/ircfspace/2648" target="_blank">📅 17:45 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-2647">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/igdEBONpOkXBjW2MqRSBT3X-WXpRvltiA2H-M6fAh2Azm22v5mqvTwU6E-fmD8KRIsztkn9_Y5AHvE3WnnE0117MtBhWEnSnhicQK6c6QjMp_g5RyCXK0_0HclpfbbaDtYNwnw2OOazg3DewxhIbwHT8FAk54K2zRcty4LD1KOU-pj4VI1wK8GbroFHOpNsnUr4mGZvQuIMeOeVxHIh5IY41lv70S1263RqJS1eCDBRNnn2UgGY6F6YA6youvHIE-iyxwcdpC1kAHa_rjtHt8SnZ9b5cEA2UIOZv5RMGglzM2mgW1Obrk8IMWkyoj5aS2ZtVZJRoCi6wcNYVdikOYA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/ircfspace/2647" target="_blank">📅 17:41 · 13 Mehr 1405</a></div>
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
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/ircfspace/2646" target="_blank">📅 17:35 · 13 Mehr 1405</a></div>
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
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/ircfspace/2645" target="_blank">📅 17:28 · 13 Mehr 1405</a></div>
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
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/ircfspace/2644" target="_blank">📅 23:38 · 12 Mehr 1405</a></div>
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
<div class="tg-footer">👁️ 77.6K · <a href="https://t.me/ircfspace/2643" target="_blank">📅 23:31 · 12 Mehr 1405</a></div>
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
<div class="tg-footer">👁️ 24K · <a href="https://t.me/ircfspace/2642" target="_blank">📅 23:19 · 12 Mehr 1405</a></div>
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
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/ircfspace/2640" target="_blank">📅 23:05 · 12 Mehr 1405</a></div>
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
<div class="tg-footer">👁️ 29.2K · <a href="https://t.me/ircfspace/2639" target="_blank">📅 08:22 · 12 Mehr 1405</a></div>
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
<div class="tg-footer">👁️ 31.7K · <a href="https://t.me/ircfspace/2638" target="_blank">📅 19:42 · 10 Mehr 1405</a></div>
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
<div class="tg-footer">👁️ 28.2K · <a href="https://t.me/ircfspace/2637" target="_blank">📅 19:26 · 10 Mehr 1405</a></div>
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
<div class="tg-footer">👁️ 28.4K · <a href="https://t.me/ircfspace/2635" target="_blank">📅 19:09 · 10 Mehr 1405</a></div>
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
<div class="tg-footer">👁️ 49.6K · <a href="https://t.me/ircfspace/2634" target="_blank">📅 18:57 · 10 Mehr 1405</a></div>
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
<div class="tg-footer">👁️ 28.4K · <a href="https://t.me/ircfspace/2633" target="_blank">📅 19:03 · 09 Mehr 1405</a></div>
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
<div class="tg-footer">👁️ 29.8K · <a href="https://t.me/ircfspace/2631" target="_blank">📅 18:51 · 09 Mehr 1405</a></div>
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
<div class="tg-footer">👁️ 24K · <a href="https://t.me/ircfspace/2630" target="_blank">📅 18:46 · 09 Mehr 1405</a></div>
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
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/ircfspace/2629" target="_blank">📅 07:37 · 09 Mehr 1405</a></div>
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
<div class="tg-footer">👁️ 28.5K · <a href="https://t.me/ircfspace/2627" target="_blank">📅 20:16 · 08 Mehr 1405</a></div>
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
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/ircfspace/2626" target="_blank">📅 20:13 · 08 Mehr 1405</a></div>
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
<div class="tg-footer">👁️ 22K · <a href="https://t.me/ircfspace/2625" target="_blank">📅 20:09 · 08 Mehr 1405</a></div>
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
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/ircfspace/2622" target="_blank">📅 19:59 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-2621">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Cop7inLMBtTAQD0U0joJl2v4DYBTGo_5Ha4CV8i1Ca_sOovsQg605FLoGnTWC7wPDAkE6EUjo8nTbturyTo9g8IBWc4_N_wFtKgYUXVzlzbqTvMA1vbioQpvnYYzGlN2yuJoNL1MUOd9Mdhq8JARKw-KSkA9QlpmzzzbFWiC5D9VuSsEL-C5m2gqiiMsy0FnhEh5uO8EgV_IGG89amQU13s4ZYxl1edLYloosTEb0gJzthi7LZc-J0pckDYekK_Zy6_mmgUkGnAczQa-3PtkYoLjk6hCs3jSHsP_p__dad9LMLREXCYbkT8gq1zbWLb1RNMoGedL2c4X1HbhMc1qvQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/ircfspace/2620" target="_blank">📅 19:47 · 08 Mehr 1405</a></div>
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
<div class="tg-footer">👁️ 39.7K · <a href="https://t.me/ircfspace/2619" target="_blank">📅 07:48 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-2618">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/u0xmfVaV9PIn_fSLevWU_HbtfErV-cvAvuOv8YaMvOCL1Yl7YhQ_ruVJkpDNViRK6DMCysL2zZLLsIyJm5SMg2o9vh9O6VkLhlcp9yeZIQL1OvG_O0c5YRwBno8sFW8IIEAyXo1KOnZ2-oTa_Zb3p3Sg_soFbOE10J9nEXreCKfjTGsogP90-Q1u40hY6461U3lKFlZG4RWpHgT5s0S8K_hqteufwPp_XhFr5EQKEqnBTtshTwvLuplw27f7W9m6mIefOOwIz-JENH2eeqIMWVZx9q6RljJNydxZ6jO6tdhVuc5A1iPDe0xkmYw5IPIO5CW0ye-zCZd3hHIDuRdmYQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 32.6K · <a href="https://t.me/ircfspace/2615" target="_blank">📅 07:34 · 02 Mehr 1405</a></div>
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
<div class="tg-footer">👁️ 30.2K · <a href="https://t.me/ircfspace/2613" target="_blank">📅 07:52 · 31 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 33.6K · <a href="https://t.me/ircfspace/2611" target="_blank">📅 08:20 · 29 Shahrivar 1405</a></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/rAg7mYZ4TTILiDZ7lojX0_r6rvTQWYQOpJYBypQh_eQH-AWVBo5wJ8CsDTSvx83HAy32M4U4tdgsYB7YAIMg9JpsJoXmU90qVrJtc46hOPSRnMiMw8QKzEfoQbWBUEx35PZxfXS3p-0npxwO2yfaEJTEnhVNgRpt6ROjDJ4aQ6-u2HtfhWvr45CQGvfuqmkHDGsL0KKon9C_1kC0-wIy9GvwjVdg7pbE_R7qOkABsYQUIxXTV1qzvTxJN18z5P2_fz1r0wR-23IyXYTBvRLVW_A7kNCWke1rrCCsa22KmJL63ZeK-soya66RHJd6RVp2fq5NAkm2nCK26kj3IxtFTA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/imWT5HTRqblrz-Fkc6S7TvtibMBfKyzWQLknhal8j-dVMAX5DHmobjLLicyODbGFoBGLVnW2baWMuZQRx1uQ5TiNK4v1cg9w5YiqBi5n4Pmrui-U8TDAVIT-ckc6b6E4CDUGssyfUhN0ul63RnUpLGUEJhQ2V8_nGGL9ssEZWocR9UsNsx1sRtMfDsETd2FZLwldXQdox44dMxeO1ewBtt8abKKSaTlQWiQ-6QD65qOBqKFiYz4HfNG5RiKQmLw9cycq5Kk9S_OvzqEPuQNuuuflbs6LnM-_0P596sD6co39VyBkOAHA4JeEw0o2xBtc3YQeVmpWY8AtG6xVasmQEQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/cmFo9JP1KnBC_u8jwVgYG0fqOWfEt4_M-GQNV18zSNBVD8AMa1A8xfzD4wZ_2x11qJ3I9fU_7UCL2UmdJt7P31MeipfBPbqVr-t9OSfi4T6JZlzJK3MppPDhsfA4SEU7V-PvuxVI1rcxx_C42mWslKpnslAKL5hSAz3MhWcrp4zZ1KIRvb1H97bnkHu059xgt0NnGB5zH702t4eAnYd6PWleEQvoDWdALSMwMumZISn_sZHVk9HOTh4bXWT22y1usvlcpui1CzihyJI5LUjbaN7jBJP2EyGI6FYWCvkVKeJLJpSitERYHWnXFgz4ZYs8Mctdjtob1GYwLIno38anIw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/ircfspace/2607" target="_blank">📅 17:30 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2606">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ubDY6oFPt7KPcgFWu4qJvWZmek23ATBgVfi8ktjIXJ80Ijz4XT7HhGMoUoJ85Y3dBSdRJd_EXCSGi2BDGsl1Lu7VnIOVWwLxyxSD04m9e549_ZZnaufzxyJSrfijq40n9sX86YnfhF3xyYCL1YDYS9HIdb2KAEj5ezpF9voJdA_nzfK58lLoB8ltqS3Y7THu_pUZpVNWyarO0dPllUmLm9ydHwBGVlUE1QNJJGrc9mJ5XDn3s6e6yWycuGNZPaXrCQjekqLSsLEGnyMQ7y9L9QywBaykcqWVd1CbILmvSxXQvQkW6wB9ghMIA53AM56wMHnDE63OUMVXGPhnmGDwcg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/vY-oXAzYmy2BYWoLby9OmrKlZ54lLOBpIcDwtK6C0LVjp1C04l8-9RG8JqrXsE7HMhUXvGN5eW3gjLE0_8ceoAtgHn_Uoh5mpKmLdUNY3i72i-6DHIO0qcLmKNE_560VGq6hLFmkJQz4m01uND5KRH96POQkkoANyk_eFGYrrNdtP-rojQ5dxEVq5AYyJ8BysUGQag0Lp91p5jaLWdowgHkTpJy_HXZ6lsYivsU7Tlb8aGMnogJaX2UdNH4wD_GZvCNGodCfy94CA3Oh1hZSBOvFY08kAk-pmCcV61QfHfZWDkcNg_cYp9NxY5ZM_df0jejuLKgJcxIVMqQcU4qQfA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/GsE7U_HnykGkHQdIcYbzMRWFFZSj8O8-tRiGAyz7UqxwDRCsnXVsFRQKPRL5fqnMSAxWeq_IDPhfDNxD-BUbEJAvcZJ89csmcdIMbNOp6y0c0uDjMd8mufriAvhLX52JeRi1bTlEvLNlwxesq-DoY6EyKPP3iN_ik5CrVUIgCxwwmkkWuYZKArUcdmaYRAx60J1x7CRiL9dr-m4mjkIrbfDSuFDQ18PT1iSD7kmZWLinSaGGOdaB0KUv-uwE2jKlAMGjUt1yYCTtVYQDfAFtx2tyDPGMcxHbaJ4ybiCnRH3OSg4Do4C1oalMXAK5GI9xRd7rtIbmwp-Wqx_VUZuOmA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">صرافی رمزارز کوینکس اعلام کرده فعالیتش رو متوقف کرده و کاربران تا ۲۲ دسامبر فرصت دارن داراییشون رو برداشت کنن.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 31.3K · <a href="https://t.me/ircfspace/2603" target="_blank">📅 16:51 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2601">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/TyysYXIIhiy6xv8d9JxW5wYMrIGHS48xVGNADASDAhM7DcL-rYZkPVeAs0fvYtvuXEl0V1MeNNPSL46_ZBbyMsqTQYZN0tPuBhkKx7Uk0OMdMEUBWYYm8uHxaoMBUyWqL3O8629DaRIcXQGqD5rhHQVMiPfkX9uLjNawf5zD2g0ewdCtQz6qz3YXbI5HwEc9IfbNnBlxHwO3vLvomOSnGNVOoyKgKQ2_FU8yua-QmjsSDlJHexN4hulq4xhT085fOz3rjxqAqdKPmcAzPQxv-ZRosGEaOOC3fmgU4ERPWj1lOAZny7LUNm8Jdjk0fyekoLzT_wtmBhHo4q6Qxa0fgA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/JAkNYOe3fU6orEJNVKMGlxtL6m_UwAtL6FLXGkjAKzoYGeggRUev9KmQGZ8cV8-1xnSczJO3Lop3H9obKPsKSnzg0AmCfYshVsExcK_m_rzPihUBeys2U7OIuN-5P1-9_GTwXqdG5UGZ57qlS1vHSE2gMlmuSVjAz6at0-V7gdlqD2NjRz7axhh69Bim4RAVHlgu4fKDVAOLES3ZSH7_QXrnPNr7O0MwHS3u1hZox4v4fQbaNAkG2Tb5X-VaUqx-rBRNsQcsq-iTZdDelbnQsTjABVdQ9vdLiRlIuSOoO_atLR8tyeb83NMv4eGSkbDbFljZGaEPxNwGhcOs1rOYDg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/geDozepQMUtAjrcguyBdjwphEqC7VeABiZi3d-C7fymFzWkq6Ri8vlMvhcnZlBano4aK3qldpNdYt488EqWmqPMulvERE5XmDNPuTD7JqnHIefajHHAdEUGwgzsE7aeCC8LtVN77mqNDSKD55-LN5OykTL2EuAoBYP335wM62tQFXAPvEZBufZizQayNp4JDQe0RG3dXdVBHwtSTLo8TFdWD__x5013yaUpychoJ2zU0nLHn1ey1LKUkCCDIzE5RThdeCVKoFf-W_CFSI2dWUfyLIZeDc84x6mNcnb7MEBdQR71NfzMcscmkuOJBrgxMVgDb3nGIeK5z2iHkhDvydg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/jKAcZCe6CGmhXVOz5gKz48-fit2LfO08AF8BfLcAgQptfuXbL2WP32e60p_lCieC1MC_KJUQ1bNtfvPdrw-zCQI80qAkOyDPxEhsP54rgqptW9lgs52h_mwc04v8wlvP0HItC2oJYcHHurJKQHRCj9FFoUtI-8XjUxkLCevmEfO522vwRnzqVBXXPpHU7rDgj8b_evU4d7ISLaTM-xHEJWeehDU7GCidsBvEfgUcXaDIPHvBzyh8QEt5GuRxPuj8jEXIJIQ9o9tLhoDvRiAI6NDaDxTh3NCv5I3LLerqJIPhbLjXqQnVcYrbvX38t0Pe95o-UpsnkT4YkkSrthukcA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/edLqQqDAED-HpZ1xwvenvaOgIG1XQ9Fxe3Sp0Cc91t81ywNDMbTU7fxetKSSNb_1rA2YT6ddbFuwdQd-jNM7LpGMPEcwlWRzJMhpCsidYRtILzktkY3438e2f53jVHIuyqwGLNI7Qmk-w3EXxkaVaXHOCpayWS2WkGlR5hHmgiG7g_ZAwzcvtxssU4Qkr7aaNXuV03FwRjMUDl08n7RtO1cSucvoQpcgiz2YYBO5HVKM5XiZRXjqHSqNvRzWFqzX7FeuWrsc1e8eFk48oL--rb32CQJHKh9AlzaPNKTZdKiEZM4rRqU4xS5zfkLKE-9uS2Tzk2lS4ZTfmOBgx466-Q.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/vr0VKlOsBoqlA-tsH-nUCwaJENb2pvhgvqWJw9mVpwwVox3B95lucQsmNXclmrHouswDJXakENMS44bUBU9bWOd2vjtvTNzMKgit_if35dZ1GvISWvA-WG8SRnFpPLm8paJ7LA5ifytaXbh4MfDvuwnhGm0R2EB5Z8oaRbvYMrZMoqpeANXHUnjsXJNkIq9HOc9-3btWWEh-D1jypJczVPoeSxEqdMvCCMrHwi_1qz14jKxa4IfnbwbxynnSl8MoTcl4T6rZyzCGPAf1H15UyXacg3uEIBrVy61ajmc-8tj38CeP7XtawmK6Tt6uvboo77Tx927I_mZ9z1ZX9JRO8w.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 90.6K · <a href="https://t.me/ircfspace/2596" target="_blank">📅 08:14 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2595">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/eNPk9ndP1IvBGmPOQQS_lqsjzxh8IvOVQ8-MjfsQtl2Kl2AuATh4EgNwZ5ZbZor5MciGMh64fG8L-Rci11WATBdr2wU4Z-qevcP35uCZbw1F3p64jJt0aHt65voHnqRv7qIDmCvLqwLrReIWqRsZowmxDEeIPYV0a4vW-0fQBw-_dXXJ6bJOtak6qGEgzfp_tU9d_Fr3JkObu2dBafDZDa_GkdJ8uyXheXAz5N2NqwTQUFdtjS8KHAKUtdigPA778b5zsl0yfDLWKPlELlSNNd1mqkzXwSg1cPrl_cb_UneRV0nIOyh3-WjLNgKjsvDCnyZECrzM_IUGlNCCIrR_Zg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/YTvmnzH3ygRA84_mVK06wcmTklkMCCReHbRWlw7QNdNRWhmf5tOQCc_wZ_jxOJKgb7Ho_LdbHvGVtiqOmhoakntQnkdT9hOhaqouXvH3C7veLVQVq-k6zP4QK63995uOg4gPYb308c_MkJc9ZCbSkM8yYVLbiAREnixNr5a6PSg01VXYxD-UcvyT7EgSY2hMxPjmxTb2j_N5tHFOQeDn4Fr5qk21HZvMCL6pKAyoavibMHquFWCAk_YnFh_Low_1kZFw_ugBm8fjsMl0EuVPJKvudjcnEDbcoSFZatz4PJqi44G30Qe6tZwNvijbkgtmPMXdA_NY8g10Yeo9bgdJOg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/digmG_52AfK3YLsMCOUT3UKWzQ1RrnfoDMygqqZLXdL6GG6MGLta-Fq_z3it2-Pq3T2Ew9gGqeefkWvZ9zXJpTvMwP8UnTIWFfDTtgOe6I28z2S01v11fcOsa7m_iYNNSbWl7bGvRb4fxe-IXdQTGoKEGIPqmqDajNMso7RNLUyRcjm7W2JXMc1eh1dK5L9nuHHOrQB1cLF-w9WoU0NkqQ5aao3ZsNpnG81KxuRPTggrBjljdTk-hRXAsbyNwSXt3reUVKoqynM265EfA5Ku1wGIyghZ3mMCE1--y8xMWvKa1fZCEdj1UMMvCPKdFW3Ek-F1MCrHgu2Buv7_z2dcmQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/q5DocIRiYhvgifVlxWP6C0_Sp1FFL5sU9cKoXO4roAQGx9tTPfggW_hIrY__MMyh9YGNLykHtYqFzbKz5tvx52KjUtc_jaxvLr2cQSNl4XzFLo6VCXzjkdTIPyo-9n5D4wCactUZWk2DTzQnS0rFUthqxMTn_cM6hXkPhzoJC379plNXqTP7WCzfzuFWVhjdCkGEnyVCfq69udP7RZMevieRfEdwIK0XhkHAl8YDvqLfJ1xXTf5JpiD8YfSWTEBs1kVwmSB-sjxbrL1zDv6sNEtogdZ0lJz711XE-cl92ruzOeXf1Erl67sj4Wvdtb58VUu4zi6dzMdoc2wGiTqyFA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/ircfspace/2592" target="_blank">📅 18:53 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2591">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/BWDlrsGEpPMNHAUNAklcyX666AoUOcfqR-i321y1qLf5omx8KOIZtBbMfwQiEwhB0nIFC5RkHrPt1LcRKvqEnVZgKDlN2femEEBEeYWtTxzGPQG81rLIGcmdh3S3NsywrUSDvPlzk2IEWydUvTPH_CKRapYubXD--u56FAmp9QBXZ2BCyRWmshJpgmcqYRzzgrZjojIopCi1PQffZr9twr6KdCFiGwtZBXjts8LC6wFCGDOI-YGRDWSJhqhh1iEUxZ2bFtN-alZhW4zc8P8r61ZX57BlwgX1lWq2Oy_1tPHpBPhre38RurnTsaWwylmOJvJyzLlskK4PDoTnB0dPWQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/fAIVltNHyN0CiTfW-cOpchNxU-z4iFLNYK9yqpVyOsdK7pSqNFqWIHmPxTTjAjf_XObXx1CuAgi4YXuiSAXBzWXIQmP4KHxLE65XIAB_MwPobFdwqA0CdXOd6fSLc5dd-I2vt1FZFjYf0xGHGGMQgu5IQe316CZ6urVjnoQ2lG8mlV6yWw95pdEStZ4Vc4fxaLhsAB43ySNo1DVTymcjqPHYYXhmCDeBiFLULBQykFLXPptioGP0OxeKZpwYueXplcmggeJqcwry4Tp0-cFGMOGvZBioa1azS1NI377CVizJbvxHXmIJ76KdRtiqUq5QnW37j6pTHdXNTlKycAo5Dw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/iVaHwDqDsi3_Uef5TI4Q6g4P8Zt5hM8KG_bEHpHmY81B3KnuT4WvUCrv7VdDCicACXNyYxXQe8fJ-pLUgybk0ZkMcLbsW2aJegAzwQXv5Jj7XRFF6Zw_B2ruCfTKTx9ECW9UKMP14wuHa5jACqaxcOP8b5liR9Cm8POiNMFfiVkaSWIO_bcOyqDuBAS28Fkd5qwtwPE9YY3eobJUnQmTSXA1X3Q0lbZVFt753AaQhHZSWjwFCwTBsg0aXR3dwFBJEeRNfLJTbDQXVVwlXRhXuVK5-pfaSTFinZ-dIsqeDX4nd5vjRffnaIv6SQYMtQP9ufo4C36gAWPzq5pGFDxW9A.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/h4TcBh72UM-Nv59Kxig_HrVllFDccnhLKnnZqugJNlGvLg24hxqhbwbP6DP_J343TC1AZmSDi_H5YMo54oJFwEQfJZ2duP8UtA8RqEXJ_OMfp9sf3kxeMQ_kcByx2E3VYq5fQY4o7T36PxrfGLds1WdIvGC8R2RmqcsucBMFKeEWHmlGASKKEVYdW7vjmKZ82Bkj_nVjEIntFXPFxKuIWUCByRZhSp9Et4147WKLVXnlmKh9stsZfeOnfbgd3q1n-2bi6JnrGq1T56W-IsYeHSvSpDTuMHMDXtD2fJ84_FJ3F_hSrv3sVkgvElJD1G1wXDQWyzm6AtMGK8VAezKgDw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 30.5K · <a href="https://t.me/ircfspace/2588" target="_blank">📅 17:22 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2587">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/W6BOpUEBzZb6XPblUnE2ek8e_Y7DdIP25JhoP9UJ0_toZ5Gmgeq8FU-aoTZ52AXI29gjnHv8BotOAT8fDvReX3SfkaHMcdKK2cbRcfeGlqyvB8aH5NqYLRJ2nt9Hp7vSxgNhWyFGcmkb2AUl-DIOgLCfiuCnKWGBq29pZ2sJjwq8mpFHuK1YeR9LLICLLJurv7usCkHGQcwSm_crQXsXlYNFrzMhuvOpy9RViVzuik1zOM5Zj1FPdCOhrIFlqrbes1LWOQupeT01ZzFxjVlKMKgR009bR1lf-r2WylrY7VwP3P_zx6q6wqfTD5-43Nnwn162M46DGfdeNteyTSGWRw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/SzWXC2jEjcQOBnNYtQXLevxB5FMzvY-7Gw4gOMYlqCMYizP93c-VfsIGFlsvS-oMPZF7OWai05VhFQkAucbYm2iyEKRC1GnxVuSSCYysQ5JxA9alR5YUimrh9gsnigHWxylJcNro-ur1XxhHvWiFfTn38Ibt5zqYT4tM1XB_aN0tmBAg4Gcdl7lpCqDDnVy1H4Wd-EbYlblUrwn85f_dHPozCzTTst9C0ygOTyzqTDc6HfU7PjR_LCeVI5AQbWbNiuqj7aRCWaxk71psSwxII92SYPYZBWO5C7L4cPM9msPWmgzL90fjxC9JVE6i8TTXuCbu562EnBy8BCamgJeaJA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">معاون ارتباطات و اطلاع‌رسانی دفتر معاون اول رئیس‌جمهور: طی ساعات اخیر اخباری کذب به نقل از اینجانب درباره رفع فیلتر اینستاگرام منتشر شده، که کاملاً ساختگی است.
/اقتصادآنلاین
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 33.9K · <a href="https://t.me/ircfspace/2586" target="_blank">📅 09:11 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2585">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/kH2nslGWcJ2QP9foTqR7IG-It3sKHimJpYVT2z_GUGzFvahJIWYgM21SKmVou2-jdJaGMj7fmE4Dtr_9x15EVc-UqqXkn4nZxopSo2WESV8xAaI8S9qyMTh2fRia0NbI4PZFUO1piqdBSc3AJ08H4lf54Tc2BopsELC0Z7otoq1okAvag7sKy6Q6LfMWpuoUEQvSjKMFesix3ykYDhVFPEMJCK9ZUGl3dY3_1LLSMLTdBHc8qm0prJHEGiAapJGl3UH_jkEbpQsgNMrnT2pLcHsc4w6Z2KNUhAVYu7XdD-k_YQ25_RulrmTr42Fa6-h_OuakFEGsXKJlDoy2rc6osg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/FGvKAoydLDH0TLdCqfW-gd5DAFbCWRI4i8zP18nk2NR5J14_e8DFRHidQYTp_pRqMm1hw_ejlrfFGRMZraBRZlPsfS0_TmitwiErRsUsNZ_mANkhsZqSLOQXAH5KuxtDhvband4pR8zvR0ZOTTtJtrS7orvZSooqzma3JXONFDBHLPL88y1_kCbuWS52CMIkea7FSAV0V5EJeWHeTxd3mFAFynD-KFgfdScXId2gAnHaPlBugVPGDC2cC-Fkb_mGbtquEfuhc8a9mMO3Tg6HlenIQzIl-lcS_mRtuveBnpUBUAMonFlsMujBqGl3y4h_KlRHVFC-KhnchH-qEbgnaQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/HRzPy4fQcbzdlvvzQgUMgbiuuuH0D_Dgf5jlwmEc5ViQA0MjPAtxBmZxFzXGKrBt-KD1YbW1K0nv2dU7q_pH15xgaItRAeUwe6t6PPDx8ITYYrx9CAk1zCVuJC8ITt8FkcQlLNPvWjePyLbSE3mxG9t-mB7pHzmigfni3pCGtwUdqqNm3EHQORJkt485gVrqAL_GoFZptNqfzHOJ03QCsZT6LBA8K6q5g9k9xNgoSyH7a8h2xMnauo5HeNmOR_O1zEoqJ_vaZl_QRfMDrju8LcyUCYx_KUUMyfNlUabbnfk-txziyk-iJLpdxUSD99j53gb0COtCWPycpSgGTCIQMw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/vYQZImryVAzFW6X8FgMjyDKyPcZOK0dltRwLiGl8ErtiNQm_grPx-KmpSOpZqh12_cKM8OG8SNEoIUhj7s3EYNO4EsV-2Iatat-nyJfBDlL-4VFYkbGtobStkVRMPVzZ0TY7lCIfrMlY7b3-2d3o55mCcXRZTymtNPBP0G6pn5JlFdOQVnZyGDhuHWxbhFslWcMDUh30DuJbpFnUWPITIRMT4WUD9ifynn6aohccmcKj_FrFLM90OGRCO0MUsGRZEGdq8uL3e2tXG-KYLcLukdimh-aDETGZr78xWqbtrTkR-adxOeku2WS4yJXxznR8Nww-VigNRWC876gttCv61w.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/kH0uXT1q1WsE6Agzz1kPUeWrcdx4SXZJjkt-1u95aB3ECnUvG9rAasl64wKVXm5-Zvz8u9xjfEsLaWqnDJzi00i2fv_2EEKeptgubedQROSZY5J52U9Ffnqlxt6Desr8z2Ps1e7fGm66jKK_S8iTFO8D6KgZI7GhD_LSsxjLM8CJvBkrVaRA3oW53brR6oK0tn7VH7uqu0dpeEX5NmV6sGinSgNHVAqxmsbW56KCHz8HWim84sJH41NfRBAkhCfGn_pqiMcTsWteDW0sFosQ3KkzjY42KabVf532kxlJk3x7DM-51BSH8WtLI8aNNtrL9EL7iLq2JgakJ7A8mM7a2Q.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/WQp9uOdLcJtdE3ZTPoHXoE8WO7fvUwMFzmWrrKqOcP16LMDMkQlApumK3fvacGcb_57hyTutM-xHfWTN7_Wdcbjk5ejugHl_V2IHHHDZzX0wQ9YDPUKYJEYPgdK7mP7C27nThpZrEFsKkEQVe7Hleny-i7eCUSqLwWk269XRrcM38yA2xjJlrIaqqI3R8eH5wodQ41kGelbko0vwINGobnV_U9ealudDzLMULRD0g74Z7nT8JbOkSR5AtZ9A9XNHpiThYmAURgmGy6i1TjGPldUEzBloSSiexy2HdcBnfrs11hV9J48Ka4vxryrLkfogC8XQvH6QDzPU2nEUqCr2TA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 30.8K · <a href="https://t.me/ircfspace/2578" target="_blank">📅 09:57 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2577">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/cii_TnS46Uy058lMz18ycOpg3HxsDKZKnFSQQW4_Ii9dr-J5VqTu3ylFP8LDwuHDs7sUQNRqRE58X2NRij9KNMg8F8EFsdL-blw9bz3iJPmwC5TRG019lUhdW_zeyfXnvxnWEodmtI9jQKGFNjASnAXjK8zI5Qb-kvDfLZJGcD2efqKXq6vwcMVF4ZHoRkBbmup8VpL7Wu-QrDvI_epzpUYgOCXOiZLI-DCpF4R61SXt32Fh1XOEr9t5NbhJwR-k-SdIgVsGw3Dxo_T_8nNWwE25YUwlIEjTN2g55tkUx0Ac3H23OdvZQUrvSmlLFDHWzvL8dMDg_wSv3u94gCdSlw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزیر قطع‌ارتباطات در مورد ۸۸ روز قطع سراسری اینترنت و بعد از اون اختلال گسترده در سیستم بانکی کشور خودش‌رو به اون‌راه زده و با سیس عقاب اعلام کرده "آماده انتقال تجربیات سایبری خودمون به کشورهای منطقه هستیم".
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 33.4K · <a href="https://t.me/ircfspace/2577" target="_blank">📅 18:47 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2576">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/mf2rfKZRk-cdRtn8Vue8BXMyy0HrtcyCUjtfpbBdxWQFF6GWDjnZf6NBHqRLftVYpUJODVTWmI5axiww6FeCsuju4sOjkwSWhH3kxtfdo6OvuHGghCnjWhuReeDH0OJ8QliFUOPc--BptKx85wrSwUgigkUXYmjseYB6yzpW6HyS6bZOiUvXct-r8FG3E0BnIMyn-KzyY3h0peMo30S1_yYH5RxK4WwvhiHyh8E4g9c7zFyAn1GVebjnrX0kLephD7fDZg94gRsx19pZjL7n1LJWt6yyHx0ZcgUfKkPnzIbN8HCWuCFr6oMkQcFFEBrbC9-jppHfQV8Pg8Wuyd99rA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 37K · <a href="https://t.me/ircfspace/2576" target="_blank">📅 18:09 · 12 Shahrivar 1405</a></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/VxqWoKavsKl6oCedJzxn8TXMK8pjNMJ8lTnfEoRpEgSJi0VSFpY3wcX5iuzTHSX1sD75mdzYS7XBGfiPhJHTGtgjs7Ha8A3J-ntHFDM9_Qxcb6UFYS6-J0MT49Ff6P17xbt9jHfF3gQfEZGA0wXD7SveC_vJa8bPZ40nuz000MigOFpNoG9IYtL9hpa-Kx4qaq7KSit9C81vWQe0glacNKuYrdSAdIebFSYHx0NPKVdFDqaGOigqBNbf1htsgS8SsrYvQp8yyCa-41_IAtRIhmS85BpbH1UyQpp59UpTCEZbRNXv61GukIEIkv6irQRq1r38ZlIY4kkDg7UqcM5SwA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/mlCl-oZrmdKjSflBPX6LmAUlaKTLXuTtADtF44ETQsEnfMyLbKSeCXpPO0te7Np6jjCzPvkqAyVcXYn3tjmBrk7nHZGJogzF3kDuRI47bS1UY6xBatV9PwlzYBC3QA8aJn-L80WL1AXKXQu3Bjl5nb_hk19exwMIK2CyqAQiynkj2DiduRd01-aQU2FtZXbV3nzsTmGrqyFnOwxhyKI1MdDbciKrCg-t8E7anJQcV8yGUB6s2PUNE52naPnjTyEjCnYDDVRoQsJ-8mOFvaueqyORHbkhpfwoEPNFOhZtwUGV4jIo5yHC7j2ehBcLvENIC4G4WgIkMV5Lwy8i5McRdw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/m5EUaHq47EXd4Zj5h5endFOG2eiRn9UJPurOe4_NkwQRc6SX_VVTGJq-aTS8szvuSrn0JcNwCrsp2VjL1y0SuRGvkQhDuYL5Ah3QkTDRRQio81S3EogppxTyBhThN-UrMvgaBJIkbcOWDpN4cERZTdzM7BkhEojtvoBbICInvqepGRgkqMrdhcNfZFQBvXNXCOlmTnaw6KPkpObitIUzZ5o3KiExuxHM0zWiFkv7B3aauapGJxjJ2IA2mLafaXyIECZB2GWHLmzn9ilstnCVAkSiUntv8uJ03FYVfpLMYj8qRiyeBNW3ArtzkLHktIawEQ3OfPDujd2KcL4aHyuHHQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ktgAPIC8_tBXlgQ3SVrWG9eLljoNBUxPPWCQq6H0FWzC7I25fhIfeO3ss-G_DJ8v8ngJo4aQbhdzFD6sellcoT8cyN6ShziL1anOTonYKLjaAKmo58306LbsILel4LP3G7757qiT5ENFkkzPDOO1Vt_UPK2fHGsEJnHiKDrWTfPmYm6SI5O9XZOnGTQX6JWbfryE3CKTFiFKjfyDMBaz8_m5mhG9znUUuuEjq0fqMkFowzjB9-MucPT_TMf8qcfm5CcQxM6S5zn7d2jwgKvazX_nsxCsHiwdU4MU45xXnMb0DcxV6ahTc7mXJ63YJEi9k5NmAxlFHx3CrW6k_dSYaw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/QuDL8YBSK5Qv8MgVS4ltsbvI1TnzPoMwX0CMlBUkF2gcgcUc8aBHdxCbAkCnmx0wnAU3sCP4WA0PyDEEef1CSxZAbKvth9jz76f2XT0GSANjGevPIcJv9Qsnq3b5_ClHTuEzxRjZ8HQsqD7pfTN8LRXZWbBQORxGYi_23-u0YfC7aVCCZokeWHTtAg0W3oBAyCMzQDtOq8Qt7AqcFJmZqu-gO3LyQfdBkYCqEQRGty3RfhiyQyWYC5UtYceDqUtK0ZfnZOyd5hhQXJwnnytlf1op9MPp-eIX_TGItikUMJtNtEMWm_wjelcObiyvzv9f1X-4UMQ3nRtjkJRkSRs3DA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 45.1K · <a href="https://t.me/ircfspace/2568" target="_blank">📅 07:54 · 03 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>

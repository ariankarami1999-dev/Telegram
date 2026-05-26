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
<img src="https://cdn1.telesco.pe/file/SLh7G4vLCkAXwK5HBxkdPIZxvuYuw1WP7jE1WSNtcPzha_Cd2JDxKHlJcQM253Yt5Yc8o0-c-6xLQuLb4qOBnjjFipWI_naB5CyFu5dH8ccuqfq47lYUBRA5_rvCZHBDKJtPZMDkF4YH-RqQXgtvfldRMofI_LdWzqUHpmmADL7gtSbVJopcVa4yHYSRIHe5pRh52hOw54-xvbGiCx-avDnV55KwLhsIotZoyj_NCi0xlvo3QIJOYGHXFvZEb8YT4wIpsVbKe1YaPkns3SfdetX7L5EqShjPDPJOoNMjSeyCMVAo4sUnzfxIEcfCE2kEso1QGDid7wReXDZPRP_q1A.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 IRCF | اینترنت آزاد برای همه</h1>
<p>@ircfspace • 👥 97.1K عضو</p>
<a href="https://t.me/ircfspace" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 این‌کانال با هدف دسترسی آزاد به اینترنت «به‌عنوان یک حق شهروندی»، به‌دور از هرگونه وابستگی حزبی، سیاسی، تشکیلاتی و ... فعالیت میکنه!https://ircf.space/contactshttps://x.com/ircfspace</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-05 21:10:54</div>
<hr>

<div class="tg-post" id="msg-2388">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Eip9CvphSpDygiBDoBYMlDP1e0sSWtyPABVs_pZJttaEYzVuZ8iViLa8XiqUw6lZlqNLJyCADzOKFBt5pwj9Gl2HKgnXjVRNrbD8w-jrVaJA5XuwWRfDqrtr_Tx1ywHHER0P9r86b7loy3yPRwCBGqwoZkIFa6HH_99_SFsHe8A_EKWj6eegBcI69oF2vwsoo1ZSgbNU0ysrzzDhH5FaJI0Nl_zGnPFIHdLqpGdY8Ms5wfFfps0kV4hKjj1r9P_0EYCFQCFmrDRiyfimj6q9q8NNjakxN19UPnmFjvfgtTrgBCHMyfYgN9ihIHuVZM-p4w7HOG1rsY0J5zom7hqXpw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">برای اینکه از وضعیت این روزهای اتصال نسبی اینترنت در ایران آگاه شوید، لطفاً نگاهی به این نمودار زمانی جامع بیندازید. ایران هنوز راه درازی در پیش دارد تا به همان سطحی از ترافیک بازگردد که قبل از ۸ ژانویه داشت.
©
nimaclick, DougMadory
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/ircfspace/2388" target="_blank">📅 17:30 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2387">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/YkmtyP676Y9cALyQmnkPq3bD0HV1Ub1UUOpcmuQ5Rqld_jkhF-KkMjF0U6lkvBNLVStnw0EGv3UpQvCWO7c-a-qbjNstXlNV_KriIOZhIjdeAYcMAqBenaFlvbSNRkAvanj4K40wo3hMNLEXIk7r47AXrcF7BIAWNr1QFvnantRiACIV-OUF0SedbISic_GMS82YvGEQP5glhfqyaJ7iTzPY3CBsKNq0oLAKKomLCXyTtnEAJNNCJH0oeMwwym32liq-AbwLNvk87bqu5tNpHVqNQxDH_fhgk8tYuvdGIjlooLOv4btffTXgxTJu06vpgnl7qAsPh3d6FkyNgRiisg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نسخه‌ای از تلگرام اندروید که از طریق سایت APKPure منتشر شده، ظاهراً یک نسخه دستکاری‌شده و آلوده بوده و محقق‌ها متوجه شدن APK مربوط به نسخه ۱۲.۶.۵ امضای دیجیتال متفاوتی نسبت به نسخه رسمی تلگرام داره، که داخل اون کدی با نام DataCollector قرار داده شده و میتونه پیام‌ها، مخاطبین، فایل‌های رسانه‌ای، موقعیت مکانی و اطلاعات دیگر کاربر رو جمع‌آوری کنه. گفتن این نسخه به سرور مشکوکی در هنگ‌کنگ متصل می‌شده و داده‌ها رو به یکسری API ارسال می‌کرده!
©
vpnreviews
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/ircfspace/2387" target="_blank">📅 17:24 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2386">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">بازگشت اینترنت به وضعیت قبل از دی ۱۴۰۴ را با ذوق و شوق تیتر زده‌اند، انگار فتح‌الفتوح کرده‌اند.
کدام اینترنت؟ همان اینترنت ناقصی که UDP و QUIC و IPv6 رویش عملاً بسته بود؟ همان اینترنتی که نصف سرویس‌های مدرن دنیا باهاش درست کار نمی‌کرد؟ همان اینترنتی که برای هر کار ساده باید ده جور VPN و تونل و کلک می‌زدی؟
اسم این چیزی که شما تحویل مردم دادید «اینترنت» نیست؛ این یک شبکه دستکاری‌شده، محدود و مهندسی‌شده ا‌ست که هر روز بخشی از استانداردهای جهانی‌اش را قطع کرده‌اید. بعد تازه اگر همین شورای جدید واقعاً قدرت تصمیم‌گیری داشته باشد و فردا یک نهاد دیگر همه چیز را دوباره برنگرداند!
این‌همه خسارت به زندگی و کار مردم زدید، حالا برگشت به وضعیت نیمه‌خراب قبلی را هم دارید مثل دستاورد ملی قالب می‌کنید.
©
iSegar0
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/ircfspace/2386" target="_blank">📅 17:19 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2385">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/riKFLFvPfWaLPSaVKxJjQEX4qaEcnspC0JZp8ovwooWW_em88HKK4IejPCbJgldjMy_MCtxgFVaQsB6RiC_T65DoV-i3jC5VHGxswcUvD0zbiahbNzJj4GzXtDFMRIa59JWK6Zti1k1vnOrG9Z7tk9m9zib3qP2P1GJodZKdn4ksd66KNbMuxzZzvJ7UbTwF38Q9AsmpkrsSR36s5NDK-bqzy0TI98h9fWFgEBHeA_8Cu577lum-44UZIJH8tCNHy6qdqybPtBCdQ50ABGHpLsfdLMhM4l8xMCgkKTcd6Uotoopl2IY2PB3IidGXCFDUy9O3drxbCTGIuR8Mj2_uRg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">۴ فردی که در دیوان عدالت اداری نسبت به اتصال اینترنت بین‌الملل دست به شکایت زده‌اند، کامیار ثقفی، رضا تقی‌پور، رسول جلیلی و محمدحسن انتظاری بوده‌اند. /انتخاب
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/ircfspace/2385" target="_blank">📅 17:12 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2384">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Rmz6ykbVaei8itlTfUt9M3-bx5vBlZTLKaJd4tre_fytvbpphwOGgwoCQ7Ygbeu6JuXK-SJ0i2_ppat4sc_LKriTaBE_UrmASehBc3Wd5ALk5mPJGpIceMUAVxMnM9spDMkIbsqUqmmU1dbWpmqvfKNikCKpFj5XXO8IcuEPRJHYhUgR8c-z3g5MN3wxB6Xi-WYDvHVHpKsY_PRWJy_I08SyjHQJWxs6iORKKKdnb5us_jNGr1AqyEuldD6emTsf0TwFHjzYRVfLB9UQS8TsJgBrsXJyMgRM42MtpKjY1hgSXXNZgw71-E2YBiaT_V1FmL5AmF3EFiVcHCjfr1sQOg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نت‌بلاکس: داده‌های زنده نشان می‌دهند که در روز هشتاد و هشتم از قطع سراسری اینترنت در ایران، اتصال تا حدی درحال بازگشت است. البته هنوز مشخص نیست که این بازگشت اتصال پایدار خواهد ماند، یا خیر.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/ircfspace/2384" target="_blank">📅 17:09 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2383">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">دیوان عدالت اداری به مصوبه تشکیل ستاد ویژه ساماندهی و راهبری فضای مجازی کشور ایراد گرفته و گفته مصوبات و تصمیماتشون تا زمان رسیدگی به شکایات، قابل ترتیب‌اثر نیست.
فعلا اون نمایشی که پزشکیان و هاشمی واسه وصل فیلترنت اجرا کردن به دیوار خورد و شرایط روی ملانت باقی می‌مونه!
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/ircfspace/2383" target="_blank">📅 14:43 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2382">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/FnDZowGAQ8wLQ0sRckghIrsJYEYl6c4abB-DK24LNUiI38F_xGRg9s2wG5aqMzqum8TBMp2wmUcxXN9I43fm9SG_m_VF-5P8daqL3QLHzx8gN6-JST2qLy_BbnbDgDUec2wUFFLAfaAwcsuHJI8QAXUIiQVbMpnpgr9SjMXFwSQzdR5shDFhMYUCWZuVnBT1N9AfMNjGaI1bGqlb3wlQK5dSOFk45n53J-pbRPwQakSPUcjhpOdIQnmuRfV1oVBtbEvsLl9ZHoS1KhpeBwfHDpz-Y-B5VeN6SyR0jIZskmnCl_EOdepE0mGb1HsAyipQy7r7eRJFV1TUtXoB1ZNbRQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رسانه‌ها نوشتن که مسعود پزشکیان مصوبه بازگشایی اینترنت رو امضا کرده و بعد از ۸۷ روز، بزودی فرایند اتصال مردم به شرایط پیش از کشتار دی‌ماه برمیگرده!
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/ircfspace/2382" target="_blank">📅 23:19 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2381">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/CkZL2Nxd-1o8jSu42PkWXGYQwZ7TmWJvffhPzv0cnv01FOU-s2IoBUOGnJCBfGHav1PgyXRKgSSbJU7YXan_ljfOy1WP11wfAUIcsP_dF9NIMsyDXMKNjgiPIXaZfA2d_Upenk8rWPVsPb2H0XZAkRJOIVYqKWv0wasEE1LP-FF1Ks-njL_7uCC4nRBJCP8qT2teNIu5xAuVwBzoJp4eWsbSYPyBZRdKWQrL5w6hrMVGjzNevSH-flaeQYBx-RBl7Ra8tlOvXg2JYSQQJxN13_aIHBRuKXENSWCflxv5_1_2dFMzG_eh2DJX5UTWJwG-9eeGXEC7-lPOysdlrbo2zw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نت‌بلاکس: اکنون هشتاد و هفتمین روز متوالی قطع سراسری اینترنت در ایران است؛ محدودیتی که بیش از ۲۰۶۴ ساعت ادامه داشته. این اقدام هرگونه شفافیت درباره اعدام‌ها را از بین برده و به شرایط غیرانسانی و بلاتکلیفی روزمره‌ای که منتقدان زندانی، مخالفان و حتی گردشگران بازداشت‌شده با آن روبه‌رو هستند، دامن زده است.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/ircfspace/2381" target="_blank">📅 11:23 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2380">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/W4yo7fD7RBE1SsN_4tEWE5xzAmoohSg9nbVAA98MVsOAscZH-h7lZ-IfdiDoIYLaYkzpG6VT42rqzA4kdrmOnDpMXj0FXOwv89A3QlcV4SZRsMB9K4IC6IZuXC-ouyZk6v1gajP35lNJ7rHc1CKcS6A1OuBVa4x7f79EAEM3R8X0zwoG5o5YAo9LGu185r7k61AVJKCtJ1nbsYtkyhCuKD_5LEbTVrAGo-LGgXw-8XGT5yaCYQwmd_MKn26bPveoJTwFA3uis7f0QuGddzIb0PuHmxB-wz35AZp7HNNw7hl_qFC9ajBnd-6zW3wcfuBKWaC5oHI3dEJPXJOgHuVx6Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">توی آپدیت جدید از اپ متن‌باز و رایگان
#شیروخورشید
کار خاصی نیاز نیست بکنید! حالت اتصال رو روی CDN FRONTING بذارید، اگر قبلا آی‌پی و SNI ست کرده بودین، پاک کنین؛ بعد روی اتصال بزنین و برای مدتی صبر کنید تا نرم‌افزار خودش آی‌پی تمیز پیدا کنه و وصلتون کنه!
👉
github.com/shirokhorshid/shirokhorshid-android/releases/latest
💡
t.me/PersianGithubMirror/5515
©
yebekhe
آیا این برنامه امنه؟ قبلا
اینجا
توضیح دادم.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 30K · <a href="https://t.me/ircfspace/2380" target="_blank">📅 17:16 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2378">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">مامانم دچار آلزایمره، از وقتی اینترنت قطع شده و نتونستیم ویدیوکال کنیم، فراموش کرده من ایران نیستم، فکر می‌کنه باهاش قهرم و نمیرم دیدنش.
©
MaryamA89323145
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 29.2K · <a href="https://t.me/ircfspace/2378" target="_blank">📅 08:57 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2377">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/f96L882xgra6UaoIR9mf-i53G2BgbeiqRqj64zFEIcFGmK_3tgLYVVuNOxTEv0ATbVG21e2S823wx-De99ZOz2XO5GLuMS5EyofMve81XVghT1FEhNBR5U0slE6fEXWn02MhRW7LM6N5LUS3nxAMMGD4aGuedHSmK7LhXaJhB06BIzzowFkI-qUCGuvvboluFeKqii7kADv1L295SfeiJwdvXwPksaougJxiZ12mlWQjM7lt1bP807PgFK3NtmMTyGdMYyDB3yyVjd1UG-xwk5lj_lbP3IYfmeyk77qGFLT4Z144IkoW0jKW4g23QyoCzuoY-eN9MY0j8FvtiupITA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قطع سراسری اینترنت در ایران به روز ۸۶م رسیده و همزمان توجه رسانه‌های جریان اصلی به این موضوع داره کمتر میشه. انگار دنیا معمولاً به رنج و فاجعه‌های طولانی عادت می‌کنه؛ مخصوصاً وقتی قربانی‌ها صدایی برای دیده شدن نداشته باشن.
Iran’s nationwide internet shutdown has now reached its 86th day, while mainstream media attention to the issue continues to fade. It seems the world gradually gets used to prolonged suffering and ongoing disasters — especially when the victims have no voice powerful enough to keep themselves visible.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/ircfspace/2377" target="_blank">📅 08:51 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2376">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/a874f4f669.mp4?token=gb-radLV5jTqudK_OsOIDi_WGJhzWRRcrOUo-_IkrnaP5aRW8b7_0a3gURLHgBuRUwkno_uY2zS2aaEHvgUQFRuFvyZtlqBSis9EbqmqwBJdwN_YkjLzK3ZOkfHusOBf-WaFljmnt5GkzL0nFVFIi0sIgObG4UKr5HrSzJjSS05pU3DEHVz3rCaCU-BqnX_EDkHssyh83hN6rCrH0JYtvDP-joEDnuvynqUACOaRhbuypZ2s3d3FtRGVKMx3RfwHtboTkq-itvJdYAiOfsHSe6wX5OrOTekoJ4CFgN49kX_RxeUdF8H6RY24cHLQYpng0gB3XNPnqSOc1aIOZ85kvQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/a874f4f669.mp4?token=gb-radLV5jTqudK_OsOIDi_WGJhzWRRcrOUo-_IkrnaP5aRW8b7_0a3gURLHgBuRUwkno_uY2zS2aaEHvgUQFRuFvyZtlqBSis9EbqmqwBJdwN_YkjLzK3ZOkfHusOBf-WaFljmnt5GkzL0nFVFIi0sIgObG4UKr5HrSzJjSS05pU3DEHVz3rCaCU-BqnX_EDkHssyh83hN6rCrH0JYtvDP-joEDnuvynqUACOaRhbuypZ2s3d3FtRGVKMx3RfwHtboTkq-itvJdYAiOfsHSe6wX5OrOTekoJ4CFgN49kX_RxeUdF8H6RY24cHLQYpng0gB3XNPnqSOc1aIOZ85kvQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بازم خداروشكر كه الحمدالله، وگرنه والا به خدا
🤡
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/ircfspace/2376" target="_blank">📅 08:40 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2375">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">رئیس کمیسیون تولید سازمان نظام صنفی رایانه‌ای استان تهران با انتقاد از تداوم محدودیت اینترنت گفت: پیام‌رسان‌ها و پلتفرم‌های داخلی هنوز نتوانسته‌اند نیاز کسب‌وکارها را تامین کنند و مشکلات فنی و محدودیت‌های ارتباطی همچنان پابرجاست.
حسین ریاضی اضافه کرد: راه‌اندازی اینترنت پرو و اینترنت ویژه برای برخی گروه‌ها، نشان می‌دهد که خود سیاست‌گذاران هم پذیرفته‌اند محدودیت‌های فعلی، فعالیت شرکت‌ها و کسب‌وکارها را مختل کرده است.
او با اشاره به آثار طولانی‌مدت اختلال اینترنت بر فضای کسب‌وکار افزود: ماه‌هاست درباره آسیب‌های ناشی از محدودیت اینترنت صحبت می‌شود اما هنوز مشکل به شکل اساسی حل نشده است. در عین حال، ایجاد این محدودیت برای اینترنت باعث حساسیت و نارضایتی گسترده در جامعه شده و بسیاری این وضعیت را تبعیض‌آمیز می‌دانند. /دیجیاتو
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/ircfspace/2375" target="_blank">📅 08:36 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2374">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/QyI8sit3YtpTaRyQZ3nve_zhKBcrVq60zMTVV309FYBmjc6cLxtGhsEVVH3nUgP714Iw2seQOWpjA0kA88a1VX-SH9z4r8VIFDiB4vjRK41i3SwAs115BVmXjVLdFpqUNBgLJUtil_8RpJ95YaQrRTEOgPvdfDWWQtoJfFb1h2uNuxCk9Sebo8VYduP681rsEBECYB2GOxHwbtCDZf36X_qPGyTK2n9nuiIkWrNNspf25UgfjdEs6O4XbJ6ZjtDDcPm3ESKcTUahkPxdHPv8n4bat6tl1Aya0NYq2NewxI8cFjfGEII9GDuv0r2j14TclO1Q94ci03pMkpCnCEqKag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">۸۵ روز از قطع سراسری اینترنت در ایران گذشت!
قطع اینترنت در ایران، یک پروژه چندوجهی است. قطع شده تا بین "هواداران پهلوی" و "پهلوی" فاصله ایجاد شود و همزمان عده‌ای بتوانند روایت جعلی بسازند.
صدبار دیگر ایران بمباران شود، نظام با بمباران تغییر نمی‌کند؛ چیزی که جمهوری اسلامی را ساقط می‌کند، آن مردمی هستند که شعار دادند "این آخرین نبرده، پهلوی برمی‌گرده" ...
با تمام دشمنی‌ها، سرنوشت محتوم ایران محقق خواهد شد.
©
AmirHadiAnvari
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/ircfspace/2374" target="_blank">📅 08:38 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2373">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/YOLFrJcUROPyEvNOKrV4YZqIX-p-SdGNYYvp1uRUY1eZX5Ip-IKHHkSVvJJmT6ymwjSiyxl3Jingte9yCwod5mYfSTFuh7J3Gf5fjNWRsvbK9wMu25ufW4sD1CIE-Zw-GhKeSFgB-8aNpBr146hkuS8TsoIIvTCBvEn1qi8o1UX1lS2pZnys6GBJ7cwPn2bwNEO4vkicxO-yfVlzeVZx5rxkqH0VwwveQCznZ6S4ZjKUBbWF17lmgGyc9xm5JEO4P4u6S-pcfBMdhdz2potZyxVoe1LrqzzW5Nv9WTY8lb_tMprpgFP5E8MSU_WmbeSrfS0u3quu-xW9fPFzH5Srzg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">طی یک عملیات بین‌المللی، سرویس VPN موسوم به First VPN که توسط مجرمان سایبری، گروه‌های باج‌افزاری و هکرها استفاده میشد، از کار افتاده. در این عملیات بیش از ۳۳ سرور توقیف شده، دامنه‌ها و سرویس‌های Onion بسته شدن و یک مظنون در اوکراین هم بازجویی شده.
مقامات میگن این VPN در تقریباً تمام پرونده‌های بزرگ سایبری یوروپل دیده شده بود و برخلاف ادعای بدون لاگ بودن، نیروهای امنیتی به دیتابیس و اطلاعات کاربرانش دسترسی پیدا کردن و هزاران کاربر شناسایی شدن.
©
eurojust
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/ircfspace/2373" target="_blank">📅 08:15 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2372">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">جمعی از سازمان‌های مردم‌نهاد و فعالان حوزه حقوق کودک، با انتشار بیانیه‌ای نسبت به تداوم محدودسازی و طبقاتی‌سازی اینترنت در ایران هشدار دادند و آن را عاملی در تشدید نابرابری آموزشی و اجتماعی، به‌ویژه برای کودکان و نوجوانان دانستند.
در این بیانیه که به امضای ۱۹ نهاد رسیده، تاکید شده دسترسی آزاد و برابر به اینترنت، بخشی از حقوق بنیادین شهروندان، به‌ویژه در حوزه آموزش، دسترسی به اطلاعات و رشد فردی است. این بیانیه، با اشاره به تعهدات بین‌المللی ایران از جمله پیمان‌نامه حقوق کودک، محدودسازی اینترنت را در تضاد با این تعهدات دانسته و همچنین با اشاره به نقش اینترنت در آموزش و معیشت خانوارها، تاکید می‌کند که اختلال در دسترسی بر شرایط اقتصادی و امنیت روانی خانواده‌ها نیز اثرگذار است.
©
hra_news
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 28.2K · <a href="https://t.me/ircfspace/2372" target="_blank">📅 19:51 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2371">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Ro5MZP8-FcEvuyr8qkaiNz7o9_VIeXd57-OIyylt8_PJXqoXkSQWN8nX3l2EzQTYlopQWhD2tZw0Qecpj28NJmc4Iw_Jf3UWoHpDl6Ia86k_viex32OVA_hrBWVEk1a7WAOGHoq07cqbGXVTKRYyCVapjOTXy-xnjYRNklrtMzgSR1dCLLA6SuIj5XBuEF7BPg5qMjRuyqLxsum_tGPp2lk2oYfP_93KoVgU1yWquP5uBDIIu0-jqlJ_vdktIvXvYrjHg0GsDC9ZMlsNRMPncnX-Lh5ZYE1xzayiVwSJQv3Oh1gVHOtiefdPolKv5PYBLlh_m6rocOFOioRfNTp1IA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نت‌بلاکس: قطع سراسری اینترنت در ایران با ورود به روز هشتاد و چهارم، از ۲ هزار ساعت عبور کرد. هر ساعتی که می‌گذرد، شکاف‌های اجتماعی و اقتصادی عمیق‌تر می‌شوند؛ به‌طوری‌که هرگونه ارتباط با دنیای خارج به جایگاه، تبعیت و امتیاز وابسته شده است.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 29.1K · <a href="https://t.me/ircfspace/2371" target="_blank">📅 19:45 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2370">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">خیلی راحت آمارسازی میکنن و میگن ۹۰ درصد مردم با قطع اینترنت مشکلی ندارن؛ به همون راحتی که احتمالا قراره تعداد ثبت‌نامی‌های سامانه
#جانفدا
از کل جمعیت ایران بیشتر بشه!
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 34.5K · <a href="https://t.me/ircfspace/2370" target="_blank">📅 20:18 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2369">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">کسانی که قبلاً کانفیگ می‌خریدن، الان ترجیح میدن دیگه نخرن، دلیلش هم تکراری شدن خبرهاست. دنبال کردن مجازی دیگه اون‌قدر براشون ارزش نداره که بخوان بابت هر گیگش خدا تومن پول بدن.
از اون طرف، کسایی هم که سیم‌کارت پرو گرفتن، خیلی‌هاشون توی کسب‌وکار خودشون موندن. چون درسته اونها اینترنت دارن، ولی دیگه کسی نیست که بخواد تبلیغشون رو بخونه. تقریبا اون چرخه‌ای که باید بین محتوا، دیده شدن و فروش می‌چرخید، به بن بست خورده و کل سیستم رو از کار انداخته.
©
NR2OH
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 37.3K · <a href="https://t.me/ircfspace/2369" target="_blank">📅 20:12 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2368">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/JLslXqmFCEnV3J6mc5JTHFN43ERwud4qe2ZBuaqtu42bX_qzR0b_-yTQsUIdAXZJwb24y6l7C_gm2DYzZrARniKC9PLaFQtih3MKQjs57tp_kx0O5LUMEzvXtQUY4x8tZetg-HRiJXGRa9I2R_W642gh7iKwu8ECZT3amBZV1ObioN7nAvZ72AmGwbQuvq_eOGtRmdZrcZmcG_8P9Q3215bGUTvoSbSXmSt5pbLI59XbvV2VCZKw5W2A39TJfc__CevnipPFZLuHdeBF4-sAl4PwOjrR36awaM6sSqcsAZcDghjdYW25NBPgEFRVgkDmemOeBXNVD2U2dC3UHvADqA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">محمدرضا فرزانگان، اقتصاددان حوزه خاورمیانه در دانشگاه فیلیپس ماربورگ آلمان، گفته است حدود ۱۰ میلیون شغل در ایران به‌طور مستقیم یا غیرمستقیم به اقتصاد دیجیتال وابسته هستند.
او به وال‌استریت ژورنال گفته محدودیت گسترده اینترنت باعث کاهش بهره‌وری، تضعیف اعتماد کسب‌وکارها و افزایش نابرابری می‌شود؛ زیرا در چنین شرایطی تنها کاربران ثروتمندتر یا افرادی که به ارتباطات بهتر دسترسی دارند، می‌توانند اتصال پایدار و قابل اتکا داشته باشند. /دیجیاتو
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 33K · <a href="https://t.me/ircfspace/2368" target="_blank">📅 20:09 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2367">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/tH4JxNxy4AChnkW5YNNC6F2Sy3IvS36PRQH4ormyNsWR0Xi7vfLAAHwx7jBsFtQu3Un4N6iyYC_3mefwtFG7LeiLkslkP7OHQR3xwOR7HNqY59e3F6H4YleNE5iegMTr06g08WvycjaoYLrkBvupjYMUWASDaHAZdY-gb8MKHKFtbuOvuqdVhQmjK-SxuKbJUegx14aZNUcLwn5HY75fgH4o-YAuQJ_4iXf4BRilaiaSIrTH1FLgoXGvDxXt5i9UzFsBcaDQKT_gkdkXZNp6kOO7xCmRchEaxxxKEyt3D8mv22iOfEVQt0hN89G1E_QyCdBu9MUm0THkmvlsDJC8QQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">زارع‌پور، وزیر قطع‌ارتباطات دولت قبل گفته "جمع‌بندی رئیسی این بود که اینترنت به خاطر هیچ‌چیز نباید قطع بشه"، ولی یادش رفته که رئیسی با ۶ کلاس سواد حتی جمع و تفریقشم افتضاح بود.
جهت یادآوری واسه
#قوه_عاقله
، اینستاگرام و واتس‌اپ توی دولت سیزدهم فیلتر شدن!
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 28.2K · <a href="https://t.me/ircfspace/2367" target="_blank">📅 20:04 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2366">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">یزدی‌خواه، نماینده طویله مجلس گفته "در شرایط فعلی تصمیمی برای بازگشایی اینترنت جهانی وجود ندارد" و "با قطع اینترنت، کسب‌وکارهای مردم از جهت ارتباطات بانکی، خرید و فروش و بسیاری از سایت‌ها همچنان در حال خدمت‌رسانی هستند و مردم مشکل عمده‌ای ندارند".
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/ircfspace/2366" target="_blank">📅 19:52 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2365">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/v9-sQ19dJCXmz_cipNKr_s2tCh8yCFDMhY1Z288_9B5azDdjmdnKEfknH7zq3hT4hk2YUHsx6iVNX11oZsIJ5gJKFt_Wiw5ONmJ3b32cVsoq4uMff6wwLNs-KRgK2_lKBqbb5-kft7OnUUxTbbwJxSpUPgzC-cdqFKhv_qy2zYHw5lVQzjMY5kK5KZ1xfHSZxp3kEQWTWejj2sAHQRxnN9oRqkNUqnXQyXDz1blRSD4JJ5feAdD4yjk0gB2PEaGiJV_jkpcMN3-Enn00_9JA45pucAYSJcOrcGInon2H_Kb3JM2olzzwJVSllaopR4J8S-ghqQ3Rb5vDRI8y5C6cKA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قوه عاقله در همراهی با سایر قوا، قطع سراسری اینترنت در ایران رو به روز هشتاد و سوم کشوند.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 28.7K · <a href="https://t.me/ircfspace/2365" target="_blank">📅 08:39 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2364">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">گیت‌هاب گفته دستگاه یکی از کارمنداش از طریق یک افزونه آلوده VS Code هک شده و مهاجم تونسته به تعدادی از ریپازیتوری‌های داخلی خود GitHub دسترسی پیدا کنه و اطلاعاتشون رو خارج کنه.
فعلاً میگن شواهدی از دسترسی به ریپوهای کاربران یا داده‌های مشتری‌ها پیدا نکردن و موضوع فقط مربوط به ریپوهای داخلی خود گیت‌هابه. البته دارن لاگ‌ها و میزان دسترسی مهاجم رو بررسی می‌کنن و گفتن بعد از کامل شدن تحقیقات، گزارش کامل منتشر میشه.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/ircfspace/2364" target="_blank">📅 08:31 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2363">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">عضو هیأت رئیسه مجلس: تصمیمات مربوط به اتصال اینترنت فقط با امضای رئیس‌جمهور انجام می‌شود؛ تشکیل ستادها نمایشی است.
این هم خبری دیگر درباره اینکه مسعود پزشکیان نه‌تنها مخالف قطع اینترنت نیست، بلکه در ساختار سرکوب و محدودسازی اینترنت کاملاً همراه و همسو با حاکمیت عمل می‌کند؛ تمام نمایش‌های رسانه‌ای درباره «بی‌اختیاری دولت» فقط برای فریب افکار عمومی بود.
©
alirezaer
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 29.7K · <a href="https://t.me/ircfspace/2363" target="_blank">📅 08:27 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2362">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/bYgcLrC9tnsWzMNejAisWCH8-MCp1gmHtYH0c3Cl_-bm5DYgPyrnR164bXwgx7YLlsjZ9VLxTMzxdywWNz8t5EUxVQ6CbEIlKUuF0TVbYtddG5XSDlOQuX9RGsjdzYJOvmt71fbtAB6ltiU2elmlPcJzOUB5ePEcgRBUK5EVdYz7pZmvpLXEF5yadFWgWCazZZQ-3fkycI8Kq6vIwoPYgUVY-z-0ZopoquYj7p6eMV5hmANqnIpR62GnlE-mT1UoY3b8q2H1FZFjPdfbD9a7hVLomIGO8Yf2gfLdk_Zv8B4PweVIvgtXMPjuo7iMd94f5d-JEezx60XEyOrLhuu97Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آمار نشون میده در ۳ ماه گذشته یک پاکسازی طبقاتی دیجیتال در ایران رخ داده. در این مدت سهم اندروید از ترافیک اینترنت ۲۵٪ افت و آیفون ۱۸۰٪ رشد داشته. این به معنی خروج میلیون‌ها کاربر طبقه متوسط و پایین از فضای آنلاینه. اونی که آیفون داره (احتمالا) از پس هزینه کانفیگ یا اینترنت پرو برمیاد، اونی که نداره، اونقدر دغدغه مالی مختلف داره که عطای اینترنت رو به لقاش می‌بخشه.
©
arashzd
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/ircfspace/2362" target="_blank">📅 08:24 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2361">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/dR3cR5K_vcE1ll5eNpHGnJVJHbkArj8AStjsyZDKsZw7igcvtVvh0D6nk_9mp07axKkGSadbZeF9t8gQCKJ3bY1Guk1pjOhgUtznw7Yo0FmQtkAHokDBYybMrQ0zqU9E2caOjFBvnBG5KJWyJqwPSp8eh1pf_LF5XZt_sYgB_t79oPNAfiYOd6IOStFctINiNd-WZ8LG01ZeifUA65tOwMEZ9hAGxAfdzugKY4plHKI4IRIKfrPMC1_FbWG2QUKXMbId0wikHhMDEpSXXRXHXGKeOAEg9B37gjTAWBMZ4n_UeItpsU0Ab75RuHh89Bkjb32nfWzQSDRuoqMoZI-WVg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هشتاد و دومین روز از قطع سراسری اینترنت!
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 29.9K · <a href="https://t.me/ircfspace/2361" target="_blank">📅 09:00 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2360">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">قطع اینترنت به خاطر تأمین امنیت، یک دروغ بزرگ است
گفته شده قطع اینترنت به خاطر تأمین امنیت زیرساختی، نرم‌افزاری و سخت‌افزاری است تا کمتر مورد حمله‌های سایبری قرار بگیریم، در حالی که این یک دروغ بزرگ است. حمله‌های سایبری و ناامنی زیرساخت هیچ ارتباطی به قطع اینترنت ندارد. متخصصان به این‌گونه دلیل‌تراشی‌ها پوزخند می‌زنند. البته نه به این معنا که زیرساخت مخابراتی ما یا زیرساخت شبکه ملی اطلاعات ما در حال حاضر امن است؛ نه، ناامنی وجود دارد، اما قطع اینترنت کمکی به تأمین امنیت زیرساخت نمی‌کند، بلکه لطمه بسیار جدی‌تری هم به امنیت زیرساخت می‌زند.
در همین مدت دو ماه و نیم گذشته ده‌ها آپدیت امنیتی برای باگ‌های «زیرو دی» یا اصطلاحاً باگ‌های روز صفر داده شده است. این‌ها باگ‌هایی هستند که می‌توانند دسترسی بسیار بالایی برای هکرها ایجاد کنند؛ روی گوشی‌های مردم، روی مودم‌ها، روی شبکه‌های صنعتی داخلی. این‌ها هیچ‌کدام آپدیت‌ها را نگرفته‌اند. آپدیت‌های ضروری‌ای که حتی یک روز به تعویق انداختنشان گاهی باعث ایجاد ناامنی می‌شود، الان بیشتر از دو ماه و نیم است که دریافت نشده‌اند و ما با یک بمب ساعتی در ناامنی زیرساخت شبکه کشور مواجهیم.
من فکر می‌کنم وقتی بحث امنیت مطرح می‌شود، بیشتر از اینکه منظور امنیت شبکه و زیرساخت باشد، منظورشان کنترل افکار عمومی و جریان آزاد اطلاعات است. اگر با این چارچوب امنیت را فهم کنیم، بنظر می‌رسد حق با این آقایان است؛ قطع اینترنت قطعاً باعث جلوگیری از جریان آزاد اطلاعات می‌شود. دلیل اینترنت پرو هم اتفاقاً همین است. اینترنت پرو نهایتاً شاید به یک یا دو میلیون نفر ارائه شود. یک یا دو میلیون نفر با ۵۰ یا ۶۰ میلیون کاربر فعال ایرانی خیلی متفاوت است و باعث می‌شود جلوی جریان آزاد اطلاعات گرفته شود و در واقع کنترل افکار عمومی و کنترل جامعه راحت‌تر شود.
چطور اینستاگرام یک پلتفرم آمریکایی است و ممکن است لوکیشن و اطلاعات مردم را در اختیار مثلاً نهادهای امنیتی آمریکا بگذارد، اما سیستم‌عامل اندروید که متعلق به گوگل است، نمی‌تواند چنین کاری کند؟ اساساً منطقی که مطرح شده، پر از اشکال است. وقتی شما اینترنت را قطع می‌کنید، عملاً یعنی تمام زیرساخت‌های رشد و توسعه یک جامعه را متوقف می‌کنید. به یک معنا، ما با این مسیر داریم گام‌به‌گام به عصر حجری نزدیک می‌شویم که در آن از فناوری اثری نبوده.
©
hamedbd
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 29.3K · <a href="https://t.me/ircfspace/2360" target="_blank">📅 08:56 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2359">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">امروز هشتاد و یکمین روزیه که اینترنت ایران بصورت سراسری قطع شده، ولی پروپاگاندای حکومت بدون لگ داره کار می‌کنه.
امروز هشتاد و یکمین روزیه که جمهوری اسلامی داره
#روز_ارتباطات
رو با قطع اینترنت جشن می‌گیره!
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 45.1K · <a href="https://t.me/ircfspace/2359" target="_blank">📅 08:59 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2358">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Wc5uTD931GU06EW0VgithLi7NM-p13IdfX7fzWUSk_g8wunCC3gRkb5bwpl89oowzq2Eo7VoRS-A88HvglARyQ2g9yHttOx_u5QHFa1LwmJXHLkoKgXCY7IlcPx8-x0XEAmhHbVL2zPESCRw_NFGiAaKAfVNxC6Xxz1T5qtgvootvIupK5p9_ltsJxS3Vz3PZlOnL644Q5eguRoMabAebHPFVaO3janQlhWYBnUv6vTdiWx0puA8_JEGXe5qOnesqiJsOJAcVcNhbUTtfkIFOhFHapqFioblZt9gTKXu12q1LtD38tihZTXzSwj3G55ICiJFEgA4ejsHk4qi2e9sbA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در بروزرسانی جدید از اپ Network Checker برای اندروید، ویندوز و لینوکس، قابلیت اسکنر آیپی Akamai (جهت استفاده در اپ
#شیروخورشید
) اضافه شده.
👉
github.com/mirarr-app/network-checker/releases/latest
💡
t.me/PersianGithubMirror/5227
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 35.5K · <a href="https://t.me/ircfspace/2358" target="_blank">📅 08:50 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2357">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/CR8r6wDlXHcZdAPBLQe0CAsytUX65sw0AiLsebjTxOrrz1LcjE29Uj42Ahl2IeOdOIl_fU2d-0PR4Yg6LVB3tCro8RuEZFwikoVN-osOr6RgZH8J8UenPUY-0e-TUqs4pb6LL5hjmcQd93urOOEeE1_VDILoVTilU_HzuTnmcw2gqwn4fcOkuqr2gA0SeHB2z84c33zIFfUMVmqpPFqjXjyG5xBU478R4GgEZrBbn-gJQA7xzj_IjXYKzocvp_xGO6TZeCW7tj1Z_PPHMuB2wlc1vmR1Zo1apTeoJ6vuYDFbAiiSP7WoY8MwI8uPhwFx9W_Y_bnIKkZCEgTF7K-d4A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اپ NexaTunnel یک کلاینت رایگان برای مدیریت تانل‌های StormDNS در iOS هست، که به شما اجازه میده کانفیگ‌های مختلف رو وارد و مدیریت کنین، وضعیت اتصال و ترافیک رو بصورت زنده ببینین، DNS Resolverها رو تست کنین و خیلی راحت بین پروفایل‌های مختلف سوییچ کنین.
این برنامه با رابط کاربری ساده طراحی شده تا بتونین وضعیت تانل، سرعت دانلود و آپلود، پینگ، IP عمومی و سلامت اتصال رو بطور لحظه‌ای بررسی کنین و مدیریت بهتری روی اتصال‌هاتون داشته باشین.
👉
apps.apple.com/us/app/nexatunnel/id6766783641
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 29.6K · <a href="https://t.me/ircfspace/2357" target="_blank">📅 08:38 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2355">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">توصیه اکید من اینه که برای وصل شدن به اینترنت سعی نکنید از سرویسهای ایرانی (خصوصا سرویسهای متصل به نهادهای امنیتی) که شمارو قبلا احراز هویت هم کردن، سو استفاده کنید.
به هیچ وجه حتی برای امتحان کردن هم ارزش ریسک کردن نداره. و به هیچ وجه هم روشهای مربوطه رو معرفی یا پروموت نکنید! اگر کردید بهتره همین الان پاکش کنید. از سر دلسوزی میگم، بچه‌هایی که از چندسال پیش در ایکس فعال بودن میدونن دارم در مورد چی حرف میزنم.
©
aleskxyz
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 34.9K · <a href="https://t.me/ircfspace/2355" target="_blank">📅 20:07 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2354">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/tZXCYVRifigVOpbltbYCqsF_P96YAMM_fJY-nQQNyLvV8k_kHzvsHq7tNQWPsbXvLgICpB8M5AFGBANxvx1yHiYKiOPmbhdti9F9D33Y1Kfb0W0YdRt52NUCzqLFzLMkvWr9bW8Far2LCf27HyJ6DH-2uT56oYT5CkFXFwhEeYMyyMD5MJym3ni1MI1OtUk_2-LQ_xRhCoW5OJ_XCHMpW2HF8pdQYNOaYxEMYtInIlSqaPNcPHh2-wEjBMdT38ZOnTbhFh6_GaH6PFDOefMBCkm6TyT4DPjrD5eo55GOCnx7cnhntyYkMi41i4GYjHNPdJUdS79u_1LW2GKAdci_oA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ما در انجمن تجارت الکترونیک تهران تجربه واقعی کسب‌وکارها در زمان اختلالات ارتباطی را مستند کردیم. از میان ۹۴۴ کسب‌وکاری که به نظرسنجی پاسخ دادند، بیش از ۸۰٪ اعلام کردند در زمان قطعی اینترنت، فروششان بیش از ۵۰٪ افت کرده است.
اما یک نکته مهم‌تر در داده‌ها وجود دارد: حدود ۳۳٪ کسب‌وکارها گفته‌اند در زمان بحران، «پیامک» مهم‌ترین ابزار ارتباط با مشتری برای ادامه فعالیت آنهاست. پیامک در زمان اختلال اینترنت، یکی از آخرین مسیرهای باقیمانده برای حفظ ارتباط، اطلاع‌رسانی، پشتیبانی و فروش است.
حالا تصور کنید پیامک هم قطع شود. بیش از نیمی از کسب‌وکارها گفته‌اند با قطعی پیامک، افت فروش جدی (بیش از ۳۰ درصد) خواهند داشت. پیامک بخشی از زیرساخت تداوم اقتصاد دیجیتال است؛ نه یک سرویس فرعی.
©
NimaQazi
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 31.5K · <a href="https://t.me/ircfspace/2354" target="_blank">📅 20:05 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2353">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/RqTZ9X-f1RNf21k5gF8fj7P79foy2PJMIM2uOeXX3a3kxwDgIAw_GnYTQpCGKDrCQYgrjb5sQk2vqE8mt89QQjtYFBj4KBIkmK_VAmzZDBrHfDCaK_lt5izvFugPiyqNdKWcMDqfTYr6wE7WWath9kr04k8tRVrBiBNhsBVh5xigAqkjJbl6CyUPNzr6vPQ8SsfGcRkUQ2m6hlgQaz3dF7NkK4r2hyxIQafY9HtlEnZrZ7H9Pg7XeX2EYk0ByaBDVN6gctfzgcVUX47A1ZgWZ5009Bdc_GCRCp6dlwy6V3psVhXqi5yci5ZCErJ_KrfayHyfj1jzXCIkmZIfFW6E-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">باید به افتخار وزارت قطع‌ارتباطات ایستاده
شاشید
!
آیندگان در کتب درسی از تمامی دست‌اندرکاران فیلترینگ و وزارتخونه‌ای که اسمش ارتباطات بود اما ۸۰ روز متولی قطع‌ارتباطات شدن، بعنوان
#قصاب_اینترنت
یاد خواهند کرد.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 35.6K · <a href="https://t.me/ircfspace/2353" target="_blank">📅 16:24 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2352">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ij0U1IE-QBhw8UT4YqsKZmqYzQ884ENF0Et3ORNLSFLo8hOuc-VpyG4oloVhgtZWvaAaYD0SrFeyrMOUuZf_KSAf7t9LqlmwP8Z_dwuqnmUX4zZXIbBRdGWKNEVi8tYb6a5JNgJ1AGSRbyyq8XnTDgQS6MyLY0VqwPWP5u-oqMUVwJPgg1nhTbtVoD4jlL0iuTro-BO06l5KCx9WsrNr1FERuVddY9Hpn-uHkWiBoVs5xs9kWhk6c8rsSHTJVVvSKDmmXXyA_kCiLLnp0rHidnecjIzg5gH99HMjo2mSillbF5Q7FZ6cpUIXQfkVMmJz6AahUS-PgKC-uXVWeWnVpQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ستار هاشمی از پایداری شبکه ملی اطلاعات در دوران جنگ تمجید کرد و گفت: شبکه ملی اطلاعات کارکردهای متفاوتی دارد. در شرایط جنگ شاهد پایداری شبکه داخلی کشور بودیم تا ارتباط بین مردم قطع نشود و خدمات مورد نیاز مردم ارائه شود.
وزیر ارتباطات افزود: در دولت چهاردهم نشان دادیم شبکه ملی اطلاعات ورای یک شعار در میدان عمل کار می‌کند. این اتفاق بی‌نظیر و شاید در دنیا کم‌نظیر است. /دیجیاتو
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 31.5K · <a href="https://t.me/ircfspace/2352" target="_blank">📅 16:21 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2351">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Rw4hhyBfIgkRNaoRUZl7HNGhVMibZAoqQS6luJn__kCgEd6BJqxNEmvI2S-cvK3WS1fKOXqQsf75Lc4Vj2JhJ0xCywdFEWcV50RPKR-R4JTdqpgJfcGwppcQ6ZApwdI8uM5mz0NyazdTdVwEF32DlFjPLhE4nagv5TxFr72fjpDAizhgW3kh2xmUGBdQ8QLd0c49Qe1KbPlbnzbZxexj3dx-GiEO2YjP4_Np0vk79ePwQDcLfna3nPZ2COl4C_pluAPGP0-BViJjlO7Y5CvKga7PhdvFXi1Ipu3USDfIb9JdXoYZy_yPVceW_b5JO_qNwQw9DHdrub3Z2JAwzpMSjQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اپ اندروید
#چشم_عقاب
نه فقط یه خبرخوان، بلکه یه راه آفلاین برای دسترسی آزاد به اطلاعاته، که بدون اینترنت، بدون VPN و حتی بدون داشتن مجوز اینترنت روی گوشی، خبرها و اطلاعات رو مستقیما از ماهواره روی دستگاه شما میاره.
کافیه کانالش رو روی فرکانس 10762/27500V ماهواره ترکمن‌عالم باز کنین و دوربین گوشی رو سمت کدهای QR که روی صفحه نمایش داده میشن بگیرید، تا اپ در چند ثانیه اطلاعات رو بخونه و روی گوشی ذخیره کنه.
اپ فقط به دوربین دسترسی داره تا QR Codeها رو اسکن کنه و هیچ عکس یا ویدئویی ذخیره یا ارسال نمی‌کنه. تمام محتواهایی که دریافت می‌کنین، قبل از پخش با امضای رمزنگاری‌شده Ed25519 تأیید میشن تا اپ فقط اطلاعات واقعی و معتبر رو قبول کنه.
👉
play.google.com/store/apps/details?id=com.filtershekanha.cheshmoghab
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 68.1K · <a href="https://t.me/ircfspace/2351" target="_blank">📅 10:02 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2350">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">باورم نمیشه قطع اینترنت به ۸۰ روز رسیده!
وقتی حکومتی برای حفظ خودش حاضر میشه یک کشور رو وارد خاموشی دیجیتال کنه، یعنی مردم هیچ اولویتی براش ندارن؛ وگرنه امروز وضعیت اینترنت، اقتصاد، مهاجرت، ناامیدی و زندگی روزمره‌ی مردم این نبود.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 31.7K · <a href="https://t.me/ircfspace/2350" target="_blank">📅 09:21 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2349">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/T25R-Elt876yrxip0DZAu78oycLmpw7c8hcuhqp5fdqE72o0AyzfhKAyfT80qTJ_DDgqsT7UwY4DZ6Ll9NQtwRD3MppCwfjaY1unjRIGXii1et5VwP5FF_LBKVYnCP9yryaeorYChrm7PQCmrbOVEvWQzykhrXCg-7vq9Cqf6Aq7dKNKL2McvY02XaK2vWJfjEyp8tEgFYK-sNv4VeF6bR_JLphHMYVCgbDR0TNxlHhRe5z4tacQMml0XVI1k-o-tBBaCAfo5YrrtMgT3r0JrK-g66UP1hVUl-vINS3B-ejzaHVo9C_adAm11k9TwjuK_oAc4kUDz7advIrU52gSrw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مسعود پزشکیان بعد از ۷۹ روز قطع سراسری اینترنت در ایران، روز جهانی ارتباطات رو تبریک گفت!
🤡
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 39.9K · <a href="https://t.me/ircfspace/2349" target="_blank">📅 21:08 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2348">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ql3jtq29hhUN9SKKaQnNQrvKJU12wKT9eU-sfWy1UIzxxVkwnB3OUERKo-lyaCnlXgKWR0ZnmPbLkDiKdudEUL54_cnU-UuQgxgFk0QB7HJy1dbZTvekEtNrd_gBzB-onCHgadw8hGSpQ_u9lR2RsAY_uaLuEyNxznMlxzP4XjHq95sZhFmHWU0D-7WrizRIGtk1HKgrJ1ZKfdpDiHfk5WvP-fJ6iKVPymLZZq8ySwugYqErwxWjc_MB4IJWsROmyD4wQL27uk9I18rJwwpS5bqIIAd30lawd9nU0kBejXhrAArQ0Q4lYt3WNWY6NAuf5YQpnvsJc4lGRaajD4gtJg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سیمکارت‌های بدون فیلتر، حفره‌ی جاسوسی برای مسئولان!
در رابطه با قطع سراسری اینترنت به بهانه امنیت و اعطای
#سیمکارت_سفید
، سیتنا در مطلبی نوشته: طبق منطق فنی، وقتی با سیمکارت سفید و بدون فیلترشکن به اینستاگرام، واتس‌اپ یا سایر پلتفرم‌های خارجی وصل می‌شوید، هیچ لایه واسطه‌ای برای مخفی‌سازی وجود ندارد. یعنی دقیقاً در همان لحظه‌ای که یک مقام مسئول درحال چک کردن دایرکت‌های خود است، اپلیکیشن‌ها لوکیشن دقیق او را با کمترین خطا رصد می‌کنند. اگر نفوذ و ردیابی، خط قرمز امنیت ملی است، پس چطور با دسترسی‌های ویژه، عملاً موقعیت مکانی لحظه‌به‌لحظه خود را تقدیم سرورهای خارجی می‌کنند؟
تناقض وقتی اوج می‌گیرد که می‌بینیم مردم عادی برای اتصال به همان شبکه‌ها، مجبورند از کانفیگ و پروکسی استفاده کنند. این ابزارها با وجود تمام دردسرهایشان، حداقل یک لایه پوششی ایجاد می‌کنند که لوکیشن واقعی کاربر را تغییر می‌دهد. اینجاست که بوی یک تجارت کثیف بلند می‌شود!
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 37.4K · <a href="https://t.me/ircfspace/2348" target="_blank">📅 08:49 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2347">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">اینترنت برای عده‌ای خاص، محدودیت و خفقان برای بقیه مردم
امروز هفتاد و نهمین روزیه که جمهوری اسلامی اینترنت رو به روی مردم خودش بسته، تا زیر سایه‌ی خاموشی دیجیتال، سرکوب، اعدام و پروپاگاندای خودش رو پیش ببره.
چندماه هست که هزاران کسب‌وکار اینترنتی لطمه دیدن یا نابود شدن، اقتصاد ضربه‌ی سنگینی خورده، تعدیل نیرو و تعطیلی‌ها بیشتر شده و مردم حتی برای ساده‌ترین ارتباطات روزمره هم با مشکل مواجهن. با اینحال هنوز هم بهانه‌ی امنیت رو تکرار می‌کنن!
این قطعی تکان‌دهنده معلوم نیست قراره چندروز یا چندماه دیگه ادامه پیدا کنه؛ اما همزمان جمهوری اسلامی با پروژه‌ی اینترنت‌پرو هم جیب خودش رو پر می‌کنه و هم به رفتارهای متناقضش ادامه میده؛ یعنی اینترنت آزاد برای عده‌ای خاص، محدودیت و خفقان برای بقیه مردم.
در این بین، عده‌ای در شبکه‌های اجتماعی تلاش می‌کنن با فضاسازی‌های ساختگی یا حتی ری‌اکشن‌های فیک، تصویری غیرواقعی و عادی از وضعیت کشور به دنیا نشون بدن؛ رفتاری که علاوه بر نبود بلوغ فکری و ناتوانی در درک عمق بحران و رنج واقعی مردم، برای خیلی‌ها نشانه‌ی هم‌پیالگی با ساختار سرکوب یا فعالیت‌های سازمان‌یافته‌ی سایبریه.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 37.2K · <a href="https://t.me/ircfspace/2347" target="_blank">📅 08:31 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2346">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/uqIbWOmLfBRDor81ar6GOLkIeVTqei8OnjrUmCwAhrbFWLkTuovj6pQ0IOMEAQ98tcVdEXaNlG6YTVzbQeSrpJ3r6LCOevj5g-OHXXORlij7XLik6WPFGo3JaZqFLFCh8a59_sWrQ87nOZj5U1zMDaiByZh5XgNheUWHDkX4rUaWXZA-Cr6eDwGJrvh6ujBkRqhqUmJ8mC0yxKp8O5bFyv7sCpe7Qql29QW7LGUlAxKRl1foZFMVD8O6ifPxlfXCx1C7jBkpzOkn95Rhly8S6a5TYRpFCcaFChOQtHSJTTCRcUdNr4PhTgWCFI2Djv3oZNbynoPRydxA9Tpkuo86Pw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نسخه ۱۶ از فیلترشکن
#MahsaNG
برای گوشی‌های اندروید در دسترس قرار گرفت.
در این آپدیت هسته‌های MasterDNS، GooseRelay و FlowDriver اضافه شدن، قابلیت CDN-Fronting سایفون تعبیه شده که میتونه شانس اتصال رو در برخی محدودیت‌های شدید شبکه افزایش بده، امکان وارد کردن دستی HTTP Type لحاظ شده، یه سری از مشکلات رفع شدن و اسکنر DNS حالا IPهارو بصورت تصادفی بررسی می‌کنه تا نتایج بهتری ارائه بده.
👉
github.com/GFW-knocker/MahsaNG/releases/latest
💡
t.me/PersianGithubMirror/5051
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 38.8K · <a href="https://t.me/ircfspace/2346" target="_blank">📅 23:40 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2345">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">اپ
#شیروخورشید
بعنوان یک فورک از اپ رسمی سایفون بصورت متن‌باز ارائه شده و توسط گیت‌هاب اکشنز بیلد میشه.
آپدیت جدید این برنامه تونسته دسترسی هزاران نفر به اینترنت رو در محدودیت‌های شدید فعلی فراهم کنه و همونطور که انتظار می‌رفت، افرادی سعی کردن برنامه رو به حاشیه ببرن و برای کاربران نگرانی ایجاد کنن.
علاوه بر متن‌باز بودن پروژه و امکان بررسی کامل سورس و روند بیلد، متخصصین حوزه امنیت و افراد فنی آشنا با ساختار این نوع ابزارها امکان تحلیل دقیق رفتار، ترافیک و عملکرد برنامه رو دارن؛ نه اینکه صرفاً بر اساس برداشت‌های سطحی، حدس و گمان یا خروجی‌های بدون اعتبار AI، درباره چنین پروژه‌هایی قضاوت بشه.
در رابطه با تفاوت این روش با MITM هم توضیحاتی از طرف توسعه‌دهنده برنامه منتشر شده که پیشنهاد میشه مطالعه کنین.
روش کار کلاینت شیر و خورشید کلا متفاوت هست و اصلا MitM انجام نمیده، که نیازی به سرتیفیکیت داشته باشه! دلیل اون روش این بوده که بیرون هسته سایفون میخواستن ترافیک رو در v2ray تغییر بدن، پس باید از سرتیفیکیت خودشون استفاده میکردن (که در صورت بی احتیاطی نا امن هم میتونست باشه). در شیر و خورشید تغییر تنظیمات SNI و ... که روی ترافیک ایجاد میشه در خود هسته سایفون اضافه شده. در واقع اگه کد رو بررسی کنین میبینید این قابلیت Domain Fronting چیزی هست که خود سایفون در نظر گرفته بود، ولی تنظیمات و قابلیت تغییر درستی رو برای فیلترنت امروز ایران در نظر نگرفته بودن، که الان در شیروخورشید اضافه شده.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 39.4K · <a href="https://t.me/ircfspace/2345" target="_blank">📅 23:28 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2344">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/plvGVfXHJrLrnDgXLvvceAV2f4Hd81ccOp7j5MT5cIUsy0-G6GQkQmm39EwxBZBQVgE9aZTTdZMJSij_YHFYIOuqBaPqyrjWUSLx9A7DgmIyAPtaNhXB-ZKCTa1aKqzDUJwHcUSJh4GTftushm8wc0IlBprIdswCMohE21p7xoWjt9qHxnmFomoSYoqrGX_jBDH-HTC3xjBJrRsjI_vLneK-uiPT8sdySZtHnUcJPJVV6ZyTK77BM-1wPKJ01O4cGb8Vd3rjE1EfxGEVAxBUvckWtYJB87W7rflI0IEF9np9Vqild1VW_u9N9yDLFGzpgVYtw4iwWYEVqzZfb624LQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رفتن هرچی که تهش Hub داشته فیلتر کردن؛ حتی گیت‌هاب.
قوه عاقله‌س دیگه!
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 43.2K · <a href="https://t.me/ircfspace/2344" target="_blank">📅 09:21 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2343">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/YzUHiBnP79BDNg6dUSr8Bz8bLECKvAzYpsSalfjYwRssNhFoneZTPpTPKuGGyJbNIfDBQkgm65oXkCmLklMUshx_lP9ukQkngHeOrQC2Q5B8IOgeAoDxMQq4h-3s-7639sgJkMaqrqXRoZl9PZB6N7VbfNLSRBvVPrJKUDLMiiVTIdRhaEZSFr1PjPWroiUom18HKxoigoilw0ZPZVYSjrwJCFrlcmiPS8dl7B3MQQA5ZOnNrBxcGXKqbyaX4tTEpDKFbckS_8KCN5LusFmxzXSsf1_92L66ZI-9KN6WSEwrch1Hb5E-npAbMctbM4CvzBfppkkku9-fUAYJ86qsLw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اپ متن‌باز و رایگان TunnelForge یک کلاینت L2TP برای اندروید هست، که از امکاناتی مثل حالت VPN برای کل دستگاه، حالت پروکسی با پشتیبانی از پروتکل‌های HTTP و SOCKS5، مسیریابی، پشتیبانی از چندین پروفایل همراه با ذخیره‌سازی اطلاعات لاگین، بررسی وضعیت اتصال، امکان استفاده از DNS سفارشی و تنظیم مقدار MTU برخورداره.
👉
github.com/evokelektrique/tunnel-forge/releases/latest
💡
t.me/PersianGithubMirror/5008
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 37.6K · <a href="https://t.me/ircfspace/2343" target="_blank">📅 09:11 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2342">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/XKDGnL_d9lmI_bjUf-fIU0ANpbe_pE1KdET-e4EXD4NN5dhqkzOzFeIZidyYx2d6mIgl_OoJK6s7vOMpV7C-BTII8ffEC4-0DKR2m7Y22P1LPkNPaMoR4yF3dSlkfRhlNR_3_PKHOlY3tdNgrj0QhllOgXGczJ6u58X1UDVVkjuFxl47hbOnW80tRxgAuTzNvdq7NyuL3_WemeezzdkwfoPFvz0DuYn3esmH7q7em1XzLD12Q4FBa4Ilw9u2lVNa98jvxpThOESLVAW9q-wb9GXfZBNrZ0ScTlyNZ-_6FpndV9__Z1QC0LtFLbFhQDZQlJAn5dMHPM4kJv-VbvJI8g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یه آسیب‌پذیری جدید به اسم YellowKey در سیستم‌عامل ویندوز پیدا شده که توی بعضی شرایط میشه BitLocker ویندوز ۱۱ رو با یه فلش USB دور زد؛ البته فقط وقتی مهاجم به خود دستگاه دسترسی فیزیکی داشته باشه. برای کمتر شدن ریسک بهتره ویندوز و BIOS آپدیت باشن، سیستم کامل Shutdown بشه نه Sleep، و برای BitLocker رمز یا PIN قبل از بوت فعال بشه.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 32.6K · <a href="https://t.me/ircfspace/2342" target="_blank">📅 09:03 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2341">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/pFF6RYbO8qhDvQ2i__rJKS5yVhcds9_Aj3GagumLbxgLfxHo-YHdTK77J6mMNQdG-YJK7XEjmwI3wzPFgciPUHuU-DgjkYEy9BdUDklwsyXPjqk4R28FQvmuwjL7cSTMdPk9iEO89PXaHEHdXAPFuSmxg12QmWMuh_0qcSzgxNXwteFS0soKBFY8iVU2Klc18J-pwnVO3dR1BfXsfrm4FnsAEfVIxiXwUu3mk9cIDzmMuV0sae_wkcmtc58DR-X71zZ8mvEDHFPKJX6s0WgB7i_cwKr8SivSUZwWT7sfsv8CooLf4gEUlY51M8_RCNur5vCiRJIIX56fgVVEeehukw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قیمت استارلینک مینی به ۲۰۰ دلار رسیده که فعلا اشتراکش هم رایگانه. کنترل اینترنت با اینترنت پرو و قیمت‌های کذایی یه توهم زودگذر هست!
©
imanraisii
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 30.5K · <a href="https://t.me/ircfspace/2341" target="_blank">📅 08:44 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2340">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/d18tQqV9WlZkRYSrjB16xHeiZmSo7cw7__KD5SfzhisLCSvy4wtLJUGACHtgzNAxM7fKcQqG_e5KLpl5V6T2ttNtNGuo0ik7mU5dPsqe2LUXt1jycfty5qUizoFPt9Q9r3DZvDsvKTDS6RqDaZzji3e2TRzVkeQjgDYQfFcMXOcME70g6yI5dTFJemJAgK_Xm7umIgLMdEnrW2TKZuwTKPdZfRVAkmKdPZsAIIxaLkNZVXTyjq08VZ4To3cgrB-3NWgkxKeRtARigWAJ7GIYiB1FJzR0rk7NQnJyxC33P6660jN9WWVFiIAKy9X8IxNX3ockqx8E2k0hNKuy9Hb1vw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در هفتاد و هشتمین روز از قطع سراسری اینترنت، از جدیدترین روش ترکیبی عبور از فیلترینگ با ذکر "لعنت بر جمهوری اسلامی" رونمایی شد.
😁
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/ircfspace/2340" target="_blank">📅 08:38 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2339">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/jjBbLzSNplLBYaJAtrxclwqbN3AQXZ5udf60r3WK52PePYrsu2MpZz-d8kmBKxbrQgW076jpHfYbn3fxTAcJtHbTuUBBpZ4cJ0XLnhn8XgZRnUSRXEo0XFnFTFzHxhBdCHYUe4_SIXsRt8lEO5c_i1G73QG28EkE5wIXxz_8NA2AiIpsM6-kU88bxb1hV0SKMbyjOEJs7Z9FIIRNvbv2deslJirF6JADN8EfCQF4AmuFMNDtA7BVT-cO6K_dMQdHLKzWxdEMWnOoZeX7ilSYj-rQRzp3mm5JcbRV-4JAWoifyhN2vBThVuJ90hPcgolXsZZ_IaFNfmEVoirlM9GPUw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هشتگ از تبعیض بگو!
اینترنت غزه که قطع میشه، اتحادیه بین‌المللی مخابرات میاد محکومش می‌کنه، ولی وقتی که اینترنت ایران برای نزدیک ۳ ماه قطع میشه، سکوت مطلق! ۱۰ ساله در مورد ایران توییت نزده!
©
markpash
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 28.5K · <a href="https://t.me/ircfspace/2339" target="_blank">📅 08:28 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2338">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Ki0RtoWhRR6S6JYAZFjoSoaaOS8-L9AXTmxOELmxSsOzEOvnoMm6b6cYuND2_Y2-jVcfBZZe6qXrgylO7ln8yt3VS8JfR3oL1wP6WaCQGx6TQuwRWhHPb9x5Kx7Ja4uY7DzKWmJkBkJmUK5B0Ej3RjhDn2dm58QPeXQyy-1YGG266LxMDUtI7Wa4FMlVrfyvkgCzYzrDsgkMO55WUu0C_yvQo_uSEUhuqL8gpS3hwuDw7D-BHMy-BhoZ26o75BX2PZY2XCIkVi1_EUhJ0Y_XUHz7c6eqmzXr3vPiAtCX2KcL_X6wh897IGwo4SvL8gNc5PJiDs_x3NA20L43Bygm6A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بعد حساب این الاغ [توی ایکس] بسته میشه، داد میزنه که آزادی بیان نیست...
©
AminSabeti
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 28.7K · <a href="https://t.me/ircfspace/2338" target="_blank">📅 08:27 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2337">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">تقابل اینترنت و امنیت یه دروغ بزرگه. مردم نه‌تنها  دسترسی به اینترنت رو به امنیت کذایی شما ترجیح میدن، بلکه هر چیز دیگری که خلاف ترجیحات شما باشه رو هم به انتخاب و تصمیم شما ترجیح میدن. شما هیچوقت جسارت برگزاری همه‌پرسی در هیچ موضوعی رو ندارید.
©
vahidfarid
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 29.2K · <a href="https://t.me/ircfspace/2337" target="_blank">📅 08:25 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2336">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">ستاد فضای مجازی با مدیریت دکتر عارف در اولین روز کاری برای افزایش رفاه مردم و تحقق وعده‌های دولت وفاق ملی، گیت‌هابو فیلتر کرد.
©
pey_74
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 30.6K · <a href="https://t.me/ircfspace/2336" target="_blank">📅 08:25 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2335">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/YlumsEL7iVZpb_RewzbRZkujcqT7oJAA2byleBs7kTzG7NfXGzeGHZFXGEY4Pp75WWkprXrRjMkB3oBmnu17uVFWam_LbXC5P49jP4Acdg4ANQrKPTYf0wcN8cxf1V3s9ionvMucr89hCM_JtxeZ_AkOFTqdJ1v5uvsq5XAVHxIe7K1zXcSdOrdA53M2oZXsNHKm9DEALltMTBCucCWY4PXy1-RWS4AiNljBoAdJZDL53QFu82Ck2kjxztjOeQWYxVF0yEcPJEyD6XSQyBTin-XX5_gyiC_KXj61SpEnxsKPvLvvy8U7ylX6GoSH-yTDod_mC_mLisMmp754fE5icg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">روش
MITM
در آپدیت جدید از اپ اندروید
#شیروخورشید
گنجونده شده و می‌تونین بدون دردسر ازش استفاده کنین.
برای استفاده بعد از نصب یا بروزرسانی، باید وارد Options، سپس More Options و بخش Connection Protocol شده و CDN Fronting رو انتخاب کنین.
همینطور در قسمت CDN edge IPs اگر IPهای وایت‌لیست شده
Akamai
رو بذارید، سرعت اتصال بهتر میشه.
👉
github.com/shirokhorshid/shirokhorshid-android/releases/latest
💡
t.me/PersianGithubMirror/4954
©
PawnToPromotion, mahdavi
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 50.3K · <a href="https://t.me/ircfspace/2335" target="_blank">📅 16:26 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2334">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">نحوه اتصال رایگان و نامحدود به اینترنت آزاد با متد ترکیبی MITM + Psiphon
👉
github.com/patterniha/MITM-DomainFronting
©
patterniha, MatinSenPaii
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 40.4K · <a href="https://t.me/ircfspace/2334" target="_blank">📅 16:18 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2333">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">روز هفتاد و ششم از قطع اینترنت.
معاون دفتر پزشکیان گفته "درصورت برگزاری همه‌پرسی، مردم امنیت را به اینترنت ترجیح می‌دهند".
وقتی گفته میشه هدف از قطع سراسری اینترنت و خاموشی دیجیتال مسئله امنیت نیست، دقیقا مطرح شدن همین اراجیفه که به جای نظر مردم به افکار عمومی تحمیل میکنن.
زمان زیادی از کشتار دی‌ماه نگذشته. به جای این چیز خوریا، بهتره یه همه‌پرسی بذارن تا وضعیت مشروعیت جمهوری اسلامی دستشون بیاد!
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 36.2K · <a href="https://t.me/ircfspace/2333" target="_blank">📅 09:19 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2332">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/qSE-dPXjTofUstE6vpc9YEei3bOUQdBlIkLNZCyolFkheEDoLUu9gFnygKiA7yna4I7PebsiOslRxtpLwKUnYI17Y-eNKA0BemwK5bcOM2cI4cTZKk0qo9J-rzzZmr9jT5zh-42fQ1dp7pE92m8ipXUVWMHaRtQuvC30oqNZ3Ohzux0LakXGWJpotIEgZrdi0Ygpv9lwsnQAsoFSjMY3qdSx0mqjPP8XY-eqfDcwidDBbZeuwdPsZagl9DDXakseD6MsI3G0oLUEbdLUYOlUdLyvUXtMRtjOCU1jzp7cML_L220v6pQ8EunbcbvY9pH_-6JXidYNRGy-rE9BynBmRg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سخنگوی کمیسیون فرهنگی مجلس: امروز پیامرسان‌های داخلی گوی رقابت را از پیامرسان‌های خارجی گرفتند.
🤡
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 36.4K · <a href="https://t.me/ircfspace/2332" target="_blank">📅 19:39 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2331">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/n5L0JOaSYTir21yX-RQhtoZmutvo1S__b8jrwbpyVuBh0osXAEY37O1QnNk7yS-2HcQYJ4Q9OWLiD0feYwmfMOl-Rma34XuGb0FtKSFZijxz5k05eawSuMrALhDMa7tk8jg0GkmNwvRC5RL3u2vuYnT1ygwGGbtPgMHhqfjVoBfRj3wi3nnJKpSQNdKvd6jYa_PdGEYbfd1paVF6W-5qY1--OckcKPBk9GPxlonZl4CouiC-0ruQWB5yjygH9QKpzatWbzTNTBg_yTJJb0yui_MbMOO7528s5MVzdsecZ0aA3wzIvHSuHDfjd2FsKF6fny0a956gQS6OvlZz_HWQQg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">۷۵ روز از قطع اینترنت گذشت؛ همزمان درآمد یک کانال فروش فیلترشکن از ۱ میلیون دلار گذشت!
©
mosi115
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 32K · <a href="https://t.me/ircfspace/2331" target="_blank">📅 19:36 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2330">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/MAumcI7E5TJ63SjAhwg4HGR8T4XakLhMNAOcZj2SRaU6pWFirVwNXemaBgbgnVjaYWeNLwqtH2zzVG0FkJlxfxleWqRpyhnzpqIFKNCK6hY4YAOMpVvAbq3iwd1niiy88k8mmWzWMomQ0iuXsbKwQJAHB1N-Bun7TESljnZitw-yGQ5wNygP8LTgip-WDthiWU5qKHPYr9GauP4NJ_ELZ3RKRA61NHmsnwmu7-MIgYJK07U6a15V0OkWwhP5XRiKgIv3jQBZpfDJvmegmU2oUyPhVDvCxY2Zv1a0E-cGSeXxccApUDrtIwf-9fzQzXxBLRlrWcs0Kmfgrsgm7qifrQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">به نظر میاد مرحله‌ی جدیدی از
#اینترنت_طبقاتی
شروع شده؛ دیگه خجالت هم نمیکشن. قدم به قدم دسترسی برخی افراد و کسب و کارها وصل میشه، تا عموم مردم به عصر بدون اینترنت و بدون هوش مصنوعی برگردن.
©
vahidfarid
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 29.1K · <a href="https://t.me/ircfspace/2330" target="_blank">📅 19:32 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2329">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">سی‌ان‌ان در گزارشی نوشته
#اینترنت_طبقاتی
در ایران خشم و نارضایتی عمومی رو شعله‌ور کرده و به نمادی از نابرابری ساختاری در جمهوری اسلامی تبدیل شده ...
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/ircfspace/2329" target="_blank">📅 19:30 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2328">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">قوه قضائیه در یک کشور مردم سالار آنجایی که حقوق مردم با تصمیمات دولت یا نهادهای امنیتی نقض می‌شود واکنش نشان میدهد. در ایران رئیس این قوه نه تنها حق مردم در دسترسی به اینترنت و کسب و کار مردم برایش مهم نبوده، بلکه چندبار شاکی شده چرا اینترنت پرو را سختگیرانه نداده‌اید!
©
alirezashirazi
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/ircfspace/2328" target="_blank">📅 19:27 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2327">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d9e9b1e831.mp4?token=b71-d1XHEPKJKNLpfPH91HR-0seYJ5yTyN9aKd6gUExEtNVIzkHyqjQOCg22wpiUXnEjgfbK9ccWEOSUsDFq2CeZSYfCF3pavLWtwxtFUCIgvmWSSd0RvVuKWYU71Ni0x_51QNVgiVB-nrUDxQWtz4RAgrDmHLPVZJx6fLa_-ukkvkcG38HMYpP9CNYFri7HmDYnslVCaBCxtoM83y3KTel7nRnffKeeYc86U7cE7Z7EFQg_amMjSUeTNGvFKX-V2TtfCHZpYWyc4NME6pzBNtvyV9qmYDLYe31JEttfOtpIYF73zH4qzbc6TM7zjfrcJU-rZuGCxzqaGZttmpxDAw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d9e9b1e831.mp4?token=b71-d1XHEPKJKNLpfPH91HR-0seYJ5yTyN9aKd6gUExEtNVIzkHyqjQOCg22wpiUXnEjgfbK9ccWEOSUsDFq2CeZSYfCF3pavLWtwxtFUCIgvmWSSd0RvVuKWYU71Ni0x_51QNVgiVB-nrUDxQWtz4RAgrDmHLPVZJx6fLa_-ukkvkcG38HMYpP9CNYFri7HmDYnslVCaBCxtoM83y3KTel7nRnffKeeYc86U7cE7Z7EFQg_amMjSUeTNGvFKX-V2TtfCHZpYWyc4NME6pzBNtvyV9qmYDLYe31JEttfOtpIYF73zH4qzbc6TM7zjfrcJU-rZuGCxzqaGZttmpxDAw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اگر هکر بودین و میخواستین بانکهای جمهوری اسلامی رو هک کنین، سرورتون رو کجا میذاشتین؟
علی کیافی‌فر، متخصص امنیت اطلاعات: در جنگ دوازده‌روزه، نوبیتکس، بانک پاسارگاد، بانک سپه و بانک مرکزی از داخل خود ایران هک شدند. مثلاً نوبیتکس توسط یک سرور زامبی واقع در یک مدرسه‌ی علمیه خواهران قم هک شد.
قطع اینترنت امنیت رو کمتر میکنه و نه بیشتر. سیستم‌ها نمی‌تونن آپدیت امنیتی بگیرن، سرتیفیکیت‌ها expire میشن، ابزارهای دفاعی (فایروال، آنتی‌ویروس) از کار می‌افتن و هکرها (داخلی یا خارجی) راحت‌تر کار می‌کنن، چون نظارت و لاگ‌گیری مختل میشه.
©
farhad_mottaghi
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 28.2K · <a href="https://t.me/ircfspace/2327" target="_blank">📅 19:25 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2326">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/k_n6ydEImlOF5Ky8PQ-rFeG_4-53y5FirlsYFDgjTpSUTfwVRETFqD9YbfwG1YQ2bEG3Asp0ksp2RybsISkregU_HXUGoRLZi1F2txvuYHcwudhzBcLXOaljZ46UJtzy8jUP4cfPA5DkxJJDEtjn_aE8NrG39VgxTWnjn0vZfKPt3-UXEVgi9gmoaCH3XSUGJOcQm0U_C10t1dN0HCUrCTuTtAV-NGSGsckvjRoDPPLa7fiMs6xrIOxdG0SCnUgHy922u3pgU2Tjj1S5R98mNdFbWyDIQwLy7kV3Qds8m87IxE74umzuat3S6E_RuVFnIYo7LF04lRuJyNSgLQc8cA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آگهی یک دفتر پیشخوان دولت برای فروش
#اینترنت_پرو
©
mamlekate
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/ircfspace/2326" target="_blank">📅 19:21 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2324">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/uKOeMYIWTezWf2OrD4inOBgTCxnqCxfYWpvcb-NuSmcMaIrG31jQ3KzzovNSWUcaWpefTSj9LZoAJo9MVZCiuWhVazGSoRLVKRg5GANcouAqqopt4jXZhzl8DafytXFKbDEAN59SwLLAR9qggTeJHr6UiFMp4JolIWDw_q6oShUu2T6O4VkrcUJPYb17OWnXDTKkN3_k6f_ezWQd93zhG_HCxfBAkUNXpYluIrSeK4K_d2fTJrL0OqQZcAC9cT4pWGIKCwZyrNR__OqxOe3uY0X5AGhrXc14Ue8Jrlyldrnpx7PlLPr0s-gGr3j4cBBFoMFqyfTKle0I2QOjTQ0hgQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فعلا دسترسی آزاد به اینترنت در متن سخنرانی‌های رییس‌جمهور و هیات دولت برقرار شده!
🤡
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 30.4K · <a href="https://t.me/ircfspace/2324" target="_blank">📅 10:54 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2323">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">تعداد کاربران اینترنت پرو کمتر از نیم‌میلیون نفر است!
تا امروز یک اپراتور با ارسال بیش از ۴ میلیون پیامک، برای بیش از ۴۵۰ هزار سیمکارت،
#اینترنت_پرو
فعال کرده و اپراتور دیگر با ارسال بیش از ۵۰۰ هزار پیامک، حدود ۴۰ هزار کاربر پرو فعال دارد.
©
aghplt
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 36.5K · <a href="https://t.me/ircfspace/2323" target="_blank">📅 08:55 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2322">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/a8ltcmDozblaiAxkocMe3kkQLcYstJx0Vo5cZvwQMCp-UMdOwdQn-PT6QZUK9PQZrvaR-JXt4PEMnGZWWyPDbjUnnZO3VCyIYam6YVLC9WYTxjgT1KVT11-Ns8wnXWlkU8jbuVMVdvf2kMRnB9Bg5Zl6kuyELnPpXs2QqMkX2Ro6Tv3n0MLBp_FAKCj-rxLkZI4hXUywhWZg-gJf1odq4HP4QdFwGr5MSw44WgyLpTW2yBXND-NIt8t2HSPW07aCeH8btQGAiHAZXjyjBZmLqS-bOcIi9xvXocEUQoOKwvQRJfmaLaQ95Y-T03baj7S7hFE2n4HgwdfykDR_iCT7Xw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">انجمن مهندسان نفت برای دریافت
#اینترنت_پرو
واجد شرایط شد.
۷۵ روزه اینترنت رو به بهانه امنیت به روی میلیون‌ها ایرانی بستن و هرکی که کار و زندگیش به اینترنت وابسته بود به خاک سیاه نشوندن، تا
#اینترنت_طبقاتی
رو اجرا کنن. مدیونین اگر فکر کنین کیسه دوختن!
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 32.4K · <a href="https://t.me/ircfspace/2322" target="_blank">📅 08:47 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2321">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">بدتر از قطعی اینترنت فکر اینه که سالها درس خوندی، دکتر و مهندس و محقق و پژوهشگر شدی، بعد واسه کار علمی دسترسی به اینترنت بین‌الملل نداری؛ اونوقت حمید رسایی با حول و حوش دو کلاس سواد برات تصمیم میگیره تو اینترنت نداشته باشی، تازه خودشم تو ایکس وله!!!
©
NiHa_Mehr
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/ircfspace/2321" target="_blank">📅 08:38 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2320">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/QHn4tDZZGvffhpdCp6umNv2DA7d9umr_jeLOWb2vr91ODGv_Yko7hqcfkQ48HyUvLwG4-mHB9De8iAZTUIcy3E0g1q6GpPw3x2NBPT5zp-CScyfvn9uQLA3IO5J1Hw1NW1HWTffyKHhuUDBWw7gq8KfIw-JlGeNPL13kHCA-OQeFMRMyVrrv00fg6Zg_KRstNy969ofB1oqn9lJ_O-vHKBeQNAJ9BEQQzgWMomqvliHpt6snKDTpM9iNenKpE2F6xmDK7ST8iU2lXMmIntQV_uxIsvD0GoscWUwtUKHSMkE7-HR6U0sJNxYOhVMEkSyibobjiT99KjgYbjNKymi14w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پس قوای سه‌گانه کشور در واقع ۴تان، که یکیشون به نام
#قوه_عاقله
نه توان قانون‌گذاری داره، نه زور اجرای قوانین رو، و نه در جایگاه قضاوته. مهم اینه که قوه عاقله قصه ما با
#اینترنت_طبقاتی
مخالفه و قراره نقش اپوزیسیون داخلی رو در این مضحکه بازی کنه!
©
nimaclick
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 31.2K · <a href="https://t.me/ircfspace/2320" target="_blank">📅 18:06 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2319">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/OlCKr70VRetvo5BU1XotugF7GELUjNJPwM3-lotq7Ax7NRANjW9VfNVzWOyTDKPa_z71Fb8B5oWTGNESBGfgk_hKC8d17tm9UhimtZHVsHXT7erKoIwhZ8BkbOxFxgrQREHliK-neHxlPbc_1-XhZGDcqO-zqrFAoc4Eob9y7MhAFHL_KdyJ93xeBARa98tbf4__-21utweBTDkOhgU_qZIDx-EwFdHSvR0VtHZYUPgsJJ0TmUp0_zpFGu_dITORTRBT-DcQzDPSOAP_jV6GRYQHaYjHb1kxmiuibKNQgskHIOTULo_lp-9aqtuXoKVgAjFUmt0-hLfjPae6xreHkg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پای
#اینترنت_پرو
به اتحادیه صنف اغذیه‌فروشان و مواد غذایی باز شد و حالا با ارائه پروانه کسب و کارت ملی میتونن از
#اینترنت_طبقاتی
استفاده کنن!
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 28.7K · <a href="https://t.me/ircfspace/2319" target="_blank">📅 17:04 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2318">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Aw9J1U1qnGcswf-V4sZPKacXG5Ve-76O8xLMLjrX8H6X-dHv03N6hjjzT1b93_kXi3g0jWeSbjyzWPaqxam0RjUsQOEYnygwix0JFR_IyOlFUCPcg8zHT0L3Gc1DRVX68J5cvmcJAB9Syut4tbDQrTr5cHo1eIs1Wp9BJDHJb4eDEJpKS1pffOZ-zMd-xeztkzJBZ62k3HqdcLMfVBe64AcAT8W48MR9PhgBXinb452mulqsX3G8xmiDIW27Opdl0mpx31avMp45QXZzMl46iBPC9oCUmAS-FNMhVyOR_HwzkRqrwSwc7uUmYMYTyBl64Vaox13hBTpZfunBHZraKw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اپ متن‌باز و رایگان TunnelX برای زمانی ساخته شده که کاربر نمیخواد تمام ترافیک در سیستم‌عامل ویندوز از VPN عبور کنه. با این برنامه میشه فقط برنامه‌هایی مثل مرورگر، تلگرام، ابزارهای توسعه یا برنامه‌های مشخص دیگه رو وارد تانل کرد و بقیه ترافیک سیستم رو روی اینترنت عادی نگه داشت.
👉
github.com/MaxiFan/TunnelX/releases/latest
💡
t.me/PersianGithubMirror/4816
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 33.9K · <a href="https://t.me/ircfspace/2318" target="_blank">📅 16:35 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2316">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/D8zvA7xreJOUQW406WJyZVEoXZZ-s1JvV4VckQ_s7QcKh7vZSlPv8kVFe7UL5_xkykZDmRNJ57rBeILDX5jjlES0GUieKc01b3NiOVMlnm58c9fGEbXDwvPDpOryPBAjpgP4Cuq_fdSqvjsUz7FzBJcFQzebx7WW6qb00Y7tk1JfF0seQ_uxOvb9mWA025Q6MfuwQAmXxzH9NPGTxToN--NqwYHuxkepi0VubQldVloJ7OY5r-W6glT26QHlnLHqOz3k3iBxivFob7w_OzyrHFLE5ERY86iNmER5qlNSDWLf1TjAtRBVkHicw7F9RfOYyZgwGKnl4gE5hwSEhG-4OA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اگر اینترنت غزه، اوکراین یا هرجایی که حمایت از آن برای حامی‌نماهای حقوق بشر "ویترین اخلاقی" داشته باشد فقط ۷ روز قطع میشد، دنیا را روی سرشان خراب می‌کردند؛ اما اینترنت ایران ۷۴ روز است عملاً قطع شده و آب از آب تکان نخورده است.
فکر می‌کنید اتفاق خاصی افتاده؟ خیر.
ضریب دسترسی واقعی به اینترنت آزاد در ایران به گواه نت‌بلاکس به حدود ۲ درصد رسیده؛ میلیون‌ها انسان نه ۷ روز، بلکه ۷۴ روز عملاً در یک زندان دیجیتال گروگان گرفته شده‌اند و همزمان که جمهوری اسلامی در پشت پرده به سرکوب، بازداشت و اعدام مشغول است، آشغالی به نام "اینترنت پرو" را به‌عنوان راه‌حل به مردم می‌فروشد، که عقیم‌سازی عمدی دسترسی آزاد به اطلاعات و نقض آشکار حقوق انسانی و حریم خصوصی شهروندان است.
ظاهراً برای جهان مدعی آزادی، فقط آن دسته از رنج‌هایی دیده می‌شوند که موضع‌گیری برایش هزینه‌ای نداشته باشد، یا چشم‌های مردمانش رنگی باشد.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 40.2K · <a href="https://t.me/ircfspace/2316" target="_blank">📅 10:26 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2315">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/aL9qngqHJwbvFM4wBLLVUqchgq3gwiAONJNaXwkxCmMyG_QDVopCACaJYmS_KQ-hwEiSQxNmAkbXtc6GBGcSuQnCqNky21itS0dvOj_0NPvqu9bWND40ZjjQXS8DTd81ReIKvLmBzApGj78hgagL3-Bzs35DUQWpgVfZp22dCYL0SwLYQtbiTUG6sedCWFzLgLPgPz_Oh6RrylsmjQ6c_m8jJL4HPMGjdBfepoWZqsKcZVbvW4RS9UplMwF1ATmPyorun2EUzGA7aerTHGevWLjuRLIA2utSCtk1HvDVjXbt1iXEwYFidtQNCXpH_Y8f7X0rNNLfuUDvKk5rutmhBg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در روز ۷۴م از قطع سراسری اینترنت هستیم.
وزیر قطع‌ارتباطات گفته "در تلاش برای برقراری اینترنت بین‌الملل در اسرع وقت هستیم".
نتیجه عملکرد و تلاش ۷۴ روز اخیر این فرد از خروجی عملکرد یه مترسک داخل مزرعه هم کمتر بوده و جالبه با اینکه از بی‌خاصیتی خودش آگاهه، حتی بصورت نمادین دست به استعفا نزده!
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/ircfspace/2315" target="_blank">📅 08:55 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2314">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Rth4V6Aj23634RHqkURDCQPsgvX3bt_GdWz5OX3ppilggOgQfseiE5Zak0m7XgQiWd519S_7nbFe_KwKT3uEX9fyo_8e6jAazsQ7VWfxf0JFDyywyB0ydDp4aAnL_sd9Tvvi3CrWcZBZunPpxIN76mttHNivB7kGVt8IQ0Umy6P1LPCL4on7550Rz3s0t90L05MTbJRKJ2JoyGgiKIuhsxzyWD3mL6msPMqefr7vJ630NrJVNpoN3tvr0rACQG8D-1aKggQbpTneTP42gGCS_zsVWjDCTxdd609D_KHsIBYH2AuTzmYKehn67DaB82ChC_gnfdAe40YsKFLct4zKFg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در ادامه روندی که نشان می‌دهد تصمیم‌گیری درباره اینترنت و سطح دسترسی کاربران عملاً از دولت خارج شده، وزیر بهداشت برای رفع محدودیت دسترسی به پایگاه علمی «پاب‌مد» مستقیماً به رئیس مرکز ملی فضای مجازی نامه نوشت؛ اقدامی که بار دیگر نقش کمرنگ وزارت ارتباطات در سیاست‌گذاری اینترنت را پررنگ کرده است. /شرق
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/ircfspace/2314" target="_blank">📅 08:46 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2312">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/r3p_i_xJdVmmP-V0U8xPEyBcnCJOKuCoZ5MQ4tjW_3s1h7Pg0sSp__5AAbRt9GSjlrn2gexm5RzRD4m_xeO6CM5EnGCArTAvkKaa3PgKHBTKVvkWwZ13sKWtIlfKHkoN9IPDneSj9iOFM0FE8ADYw6acVADgJYuzuiB6D-7Psd1gg1EdjFhsZWSgKLJvItZRksECrKro1aCDu-pYYJq0RTx22YbBcyO9_RIL1rSjOdchnm65Kc9vchzP9AxdE9kJyZ4GhGhs7l-l0T5X4WYyq68m6-IesAi9o30h4TxaH_35zIFOSfeZ3xRRIivlXXADYHasbPlLkB3JS91deSXRAw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اسکریپت AIO Downloader یه ابزار متن‌باز و کاربردی برای دانلود فایل و محتوا از سرویس‌هایی مثل یوتیوب، گیت‌هاب، اینستاگرام، ایکس، تلگرام، گوگل‌پلی، تیک‌تاک، پینترست، ساندکلود و ... هست، که فرایند دانلود رو از طریق GitHub Actions انجام میده.
این ابزار طوری طراحی شده که در شرایط محدودیت شدید اینترنت و وایت‌لیست فعلی بتونه بسیاری از فایل‌ها و لینک‌ها رو دریافت کنه، بدون اینکه نیاز باشه سیستم یا سرور شخصی برای دانلود داشته باشین.
با توجه به اینکه این پروژه به GitHub Actions متکیه، بهتره برای استفاده ازش از اکانت اصلی گیت‌هاب استفاده نکنین و ترجیحاً یک اکانت جداگانه بسازین.
👉
github.com/ProAlit/aio-downloader
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/ircfspace/2312" target="_blank">📅 08:37 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2311">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/eiaD_57YRXMgjlTwSdU_pbdnmo-oTBnrcq9MArURp1WsJqbfq8xl6G-a4F7OdS6PZZMoDPj4SaonLh4vJ_vFk1LFao9vtgIQcnj8EP1zS0UtnONr_XswlznQqufaNlf4cQ28D6T6qF0MpIlLve0CaviUm8I803M3lSiNeDzThHb6g84seubekAWdTkZhCUMMcWxDYXcwyqf_gqGwwORi7E2ze6hLsOlkJHoZ5lRGJdN35cuyQ9Q_ox21ODwIYnY5WzBvu58mN7FDJlj93Wu0sUveyWNFc9l3MDWz7HuoC-bomNMPuYsXIpuChVxasxmJo7f0fMD6PZUhbjl2_K0HVQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#پیامرسان_بومی
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/ircfspace/2311" target="_blank">📅 21:33 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2310">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/hBfewI6LyojxQEnZezNJMpZptUpqXusDDcQ3Vo1a2JH0f5q3OUra0uiYIKL0XrVuXlnBQT8pkiRgZT0g5O3IKutsavsOJO473tMhTauDgNr2JvbwrMeWC3jSMbvRUS5HR9-Esm-jlK8duta2rQIqQ7tHFatD8sX0B-fzQiE41p5GEI9vFdi_7sAtGZM5xW2KTC637zMHQ3SP6DWRTmzEUGnZwf35AqE-2bn8ms1e_Dcxk7IW413gIILMdYjYLR_aMds1yxxXs20KKNLP9r5jAzNYLmZJy-gmnIY0AyzvCmhdJkzD5cg6C5IHUeg3bQVE2BqHHoevK5ha6CYKC4_3uw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دیگه رودربایستی رو کنار گذاشتن و بدون ثبت‌نام و بدون احرازهویت، بابت پیوستن به پویش جان‌فدا ازت تقدیر میکنن
😁
کی به کیه؛ اگر آمارش به ۳۰۰ میلیون برسه هم تعجب نمی‌کنم.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 29.8K · <a href="https://t.me/ircfspace/2310" target="_blank">📅 21:28 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2309">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">تا الان توی هیچ پستی نگفتم که به پروژه‌هام دونیت کنین، چون حس خوبی به مطرح کردنش نداشتم؛ ولی شرایط همینطور پیش بره احتمالا سر چهارراه نشسته باشم
😂
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/ircfspace/2309" target="_blank">📅 21:25 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2308">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">قبل از شروع جنگ و قطعی اینترنت درخواست فیبر نوری دادم و حالا اومدن نصب و فعالش کردن.
با تشکر از شاتل بابت سرویس خوبشون؛ در واقع قبل از نصب اینترنت نداشتم، ولی الان با سرعت خیلی بیشتری اینترنت ندارم.
©
itsmralii
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 31.2K · <a href="https://t.me/ircfspace/2308" target="_blank">📅 11:45 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2307">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/MbmeCNrsMzKxdSEjLVD_Jn0-jR1Fxa7awzBG75SPJ7pTIGRQm5i0B1QRXornkk3ua9mLwdfWhwwp8qjPC6xpon17U8wrVvSGlQUZ5Ui_NuT8a3MIA2FPEB2iZwpNYPWE0FzmQzZCVC97jam_uwVIzOV37wlB6re9YNJjA01jXIgz8jNTUEurkMUfL2eRtznh4z-55k8hxiReI40E0XCieKCpCnNgFwroE6E4jFlJ2feHTZVdBog_mDbHbo3zw8J_AW_iE-UV6JAbJ6S9BlFQnRGJFi-Jj-QClT_B4Z3PF3mOn0lpVIlHXPgAAT-atONEIuB1kA2DVqNpv3RHFcWpWw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">معاون رئیس‌جمهور از وزیر ارتباطات بابت هیچ و پوچ قدردانی میکنه، بعدش همون وزیر از رئیس‌جمهور قدردانی میکنه، بعدترش همین بدردنخورها دسته‌جمعی از مردم قدردانی میکنن؛ اما تهش می‌بینی ۷۳ روزه که اینترنت قطع هست!
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 35K · <a href="https://t.me/ircfspace/2307" target="_blank">📅 08:13 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2306">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/E5_y5ajr7NTtWdsHoqr8drhMwg4MXDeHZyLaBYmx92zkSdOKlJSWzhn0hcsDswHWuRKLS9jAfZXsmriWHyRDie9M3Tp3Qt2HXxhDKyrCBCiwk_yBX2K5rmgYiPRw4KT0scoYJH3IK-U8rrrkBTcqHr-54U82GdKpmBG7_ssEqxqORbaUchZgh3gh9G_XkqRjudIHZmxIZWF6-yQxjUgKN8uIltJuamMoTjHmkUh9pweKzIv-Mjm1owOeKcDd6xuTQIP9MUytZ6CsszZdzbMjZ0LUMxQFwM78bNwFM65RUlokxWbUxOenv2Nv1JRLS3x7ZWDedMATgmlzqDp_PVTvAw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اپ WhiteDNS یک کلاینت متن‌باز و رایگان برای اندرویده، که امکان اتصال از طریق DNS Tunnel رو با دو حالت Proxy و VPN فراهم می‌کنه. این برنامه با تکیه بر MasterDNS و StormDNS طراحی شده و میتونه بدون نیاز به تنظیمات پیچیده، ارتباط رو از طریق تانل DNS برقرار کنه.
👉
github.com/iampedii/WhiteDNS/releases/latest
💡
t.me/PersianGithubMirror/4637
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 32.4K · <a href="https://t.me/ircfspace/2306" target="_blank">📅 16:30 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2304">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/QNEBQn_Le2ZVjha-nBNQ6cYRd28v4sFh4jwprThyyCabcxcyUsedR8RnfhujtnbI5loQgu1tSi6n4xDpexHAdNaB6EQPhY8NJKWWFqXCUFb2z29eSguHkf42dJjZvT6O4w0swW9vAPS0Jj4yvqgbQvAnMs8pTfQTLCM9NwWrO5hD2rCfFYMGt3M3VP-_PP3-RwPkR4IvdE9uRnCs_yazZAva7dhgA7oMO7muNcr_Q4KUYbxrEupo8kKTLV3XWZWv8WFgVcJ6Jg_-hUVwzkOa8cyjBjddR7dXlKaKU_fnEy9lh5F5OenIgF0iQk3V9ASVrz40oLhbqqmMlkKOC4uMMA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هر روز که نت‌بلاکس عدد روزهای قطع سراسری اینترنت در ایران رو اعلام می‌کنه، یه عده میگن "خب شمردن که کاری نداره، خودمونم بلدیم".
ولی مسئله فقط شمردن نیست؛ مسئله اینه که نباید این قضیه عادی‌سازی و فراموش بشه. اگر فکر می‌کنیم راه مؤثرتری برای اثرگذاری وجود داره، خوبه؛ ولی سوال اینجاست که چرا تماشا می‌کنیم؟
۷۲ روز گذشته و هیچ اقدام جدی‌ای برای کمک جهت اتصال آزاد به اینترنت انجام نشده، کسب‌وکارها نابود شدن، آدم‌ها شغلشون رو از دست دادن و سفره خیلی از خانواده‌ها کوچیک‌تر شده. مردم برای یک اتصال معمولی باید میلیون‌ها تومان از جیب خودشون هزینه کنن و در عین حال بخش بزرگی از نهادها و جوامع حقوق بشری نسبت به تداوم قطع اینترنت، سرکوب، دستگیری‌ها و اعدام‌ها سکوت رو ترجیح میدن.
در فضایی که همه‌چیز خیلی سریع به حاشیه میره، استمرار در اطلاع‌رسانی خودش یک کار مهمه و همین گزارش‌های روزانه امثال نت‌بلاکس حداقل باعث میشه موضوع قطع اینترنت در ایران کامل از توجه‌ها خارج نشه!
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 30.9K · <a href="https://t.me/ircfspace/2304" target="_blank">📅 12:30 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2303">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">این هفت کابل اینترنت جهانی در خلیج فارس رو اگه قطع کنید خیلی خوبه، اونا هم مثل ما اینترنت نداشته باشن، بلکه دکان‌های حقوق حشری صداشون برای اونا دربیاد و یه نگاهی هم اینور بندازن و دل ما هم خنک بشه!
قطع کنید.
©
ehsan_369
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 28.7K · <a href="https://t.me/ircfspace/2303" target="_blank">📅 12:21 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2302">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Jsm-lAdB7dAyf-RgNAf0cg_aOoIqot-GrS86jxiu_avImgTSNhk37fo1lnuz6sxu1ypLjlTFxsFE8NcItp09DzNCrABQWPh3bkuIlNky_NCUXqJveLzlJYXAfcUhlujR3Y0SPR319zt59LUgIV9TjQJGri6gvkbCLyQroQ_jSRyOAj_vIDtP7anCOYbS2gxs9JtGZgYt6ypjfja8mKC-tvNL4YbTxk5mGazfY36TMSLD7jxWvJ1bZCjjNLHJCCPGJRWnHY3nDyp3fQy-OpaUuSaCSpkwB9MKyVyhSM1GOPPYpFAZGlMTdRgMeG8ctqzpk88vfvPZPxnFC6wHcJaJMQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تسنیم نوشته تنگه هرمز فقط مسیر نفت و کشتی نیست؛ بخش بزرگی از اینترنت و تبادلات مالی دنیا هم از کابل‌های زیردریا رد میشه، که از اونجا عبور می‌کنن. پیشنهاد داده ایران از این مسیر پول و کنترل بیشتری بگیره؛ یعنی برای عبور کابل‌ها مجوز و هزینه تعیین بشه، شرکت‌های بزرگی مثل متا و مایکروسافت مجبور بشن تحت قوانین ایران کار کنن و تعمیر کابل‌ها هم فقط دست شرکت‌های داخلی باشه.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 28.5K · <a href="https://t.me/ircfspace/2302" target="_blank">📅 12:17 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2301">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/SItLZLoLNxB7eg1u1eQGGo1pTz_TRojasIQTKUvpB0z2wY3IvG8yAemb2IK3Y5ed8Q2P5H2ZUqJQrSmBU-jSdwsrEoOsa7Sr3PhOy8q6VCIRUYJLyObPfnKZFPEdETGvpYC7ApQiEwQhRN2MXyWMG9RbCShY6IPN9644-qVlvnhEZZFI_m1mFZullfwUq23aqVHYJF_GQG37HAh40mRaii1epCzVOayDvpnq3j18oSd4wRxCKY8MIH-66KCfn4fN_BXrfCkG9WT_WB-YSHdoki7nNnm-00r-HJSnh3hcwUnVnP9DtMhG2cGsfw7_kUYv44yXrBWpD_wQzBjqbnWuDA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نت‌بلاکس: قطع سراسری اینترنت در ایران وارد هفتادودومین روز خود شده و هیچ نشانه‌ای از بازگشت گسترده اینترنت دیده نمی‌شود.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/ircfspace/2301" target="_blank">📅 12:07 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2300">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/G56vn4ISVbLwgElgQEwAcHEJrg0WG00gZnlzQL7qAayo5DnP-c8ZYSfYLrYVAJPL_Tnoq4k_GKj-H2lmLOdqizGQKdlEfVWdnXdRM3cS5jpYlGnZ-7MZZditcA0OMvnJrojLs_wVikWy_R1eQ50ds5FE6tMq0oNeVmtNl_O0az6ckFW4ziObKAi1PaCQNENFSBOit0VuQYiBT0fjCvuD67c8o2CGzgzjSbjIzU0Wl6hxyYgxtjDFRKMAlSeGKR1CPZhlvQ7exmsvsxH990I5LzkHkO82GXkM8XHRChZVRCR4TAXc0d0uuQHbG7-qs4CWbjNqUZiu6HoI5CV8yc7Mzw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نسخه ۳ از اپ متن‌باز و رایگان TeleMirror برای "دریافت آخرین مطالب کانال‌های تلگرام در شرایط محدودیت شدید اینترنت" برای ویندوز، لینوکس و مک منتشر شد.
در این نسخه نمایش پست‌ها بهینه‌تر شده و مشکلات مربوط به کش تا حد زیادی برطرف شده، بخش تنظیمات به برنامه اضافه شده و امکان بازگشت به تنظیمات پیشفرض فراهم اومده. لیست کانال‌های پیشفرض افزایش پیدا کرده و علاوه بر نسخه Lite، یک حالت Normal اضافه شده که تلاش می‌کنه در صورت امکان تصاویر فیلترشده رو هم نمایش بده.
این برنامه فیلترشکن نیست و بر پایه دسترسی‌های فعلی وایت‌لیست اینترنت عمل می‌کنه، بنابراین ممکنه روی برخی از اینترنت‌ها قابل استفاده نباشه.
👉
github.com/ircfspace/teleMirror/releases/latest
💡
t.me/PersianGithubMirror/4599
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 31.1K · <a href="https://t.me/ircfspace/2300" target="_blank">📅 18:57 · 19 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2299">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">افغانستان تست خدمات اینترنت 5G رو در کابل استارت زده، عراق تلگرام رو رفع فیلتر کرده؛ اما جمهوری اسلامی تا دقیقه ۹۰ درحال آزار و اذیت میلیون‌ها ایرانیه!
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 32.5K · <a href="https://t.me/ircfspace/2299" target="_blank">📅 17:52 · 19 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2298">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/pgfLBT15XBSO2X4q-nLVd_6NJv4_SDVxFUy_LuDJ3eNrrEGvdcXURrdrYpurf6hGIlmpcCwsb5YgFu0-b3Pa84DOG1GQqiTU1KxntEpShEF3mydS30mweS3cx3r1Bcr3oRZo3K0vDYPQ-LBrkXjxpWwxLXmZKCnOww_s1KUfJEulbPaqze46KXV6h_wSwIT-3-4fd1_RVJDhtHnNNeal_zeavVkJ2FQ8VA199XVrGTuBlpnTcoRPgwUiuUO4M33pOqHvWupYPthiI38OHiFo4V5-kiQKZBx0jhI9Xx7FjaVENFduVtnsu-3yzDYSzCWb1FDqQhEwkrx3oXQfK7MViw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یعنی خاک بر سرتون (پیامرسان‌های بومی) که با اینهمه حمایت و در میدانی بدون رقیبِ جدی هم عرضه ندارین کیفیت خدمات دهی، پشتیبانی و توان زیرساختیتون رو ارتقا بدین و بعداز اینهمه سال سابقه، آدم نمیتونه ۸ مگ فیلم ارسال کنه.
بعد از خودروسازی، باید شماها رو هم دومین فرزند لوس و بی‌خاصیت کسب و کارهای داخلی دونست!
©
kamran_falahati
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 30K · <a href="https://t.me/ircfspace/2298" target="_blank">📅 17:48 · 19 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2297">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">جمهوری اسلامی ۷۱ روز هست که اینترنت رو به روی مردم خودش بسته!
روح‌الله مومن‌نسب (تئوریسین بارداری با ۲ گیگ اینترنت) گفته شرایط اینترنت به هیچ وجه نباید به روال گذشته برگرده.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/ircfspace/2297" target="_blank">📅 17:45 · 19 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2296">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/hXGF-qFmWmRpMWDHchxP929PgRjfh_4NmqRB7lkhIPrTcDhdGBDOKlyPqC8Ge0wIgqOG1XTrH-gRZtSbKhmxYyqnw67XaFx3upBn17WbCO3jrG_eQEo5KFclMWdnPQLIVcFVaANB7SdvFldXFRc8gIAR80V89jhiZ6YRokHjHAJRpvMgj0Wmcq1xYogTXbLdizR_gPV2zc2_3Vly-PnoVLwdL1VxKONTa7xQhxHf37_3pqzYGtcaOH3jcd-cbZqTGQ5lYDI1tjtSv8zS1tfXYaLfProfhoZvp8wPJP6g02K9HWfakBk6Djhnz4uwZv8RUtkcwTgL-HxwqiEep8f1xg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اپ متن‌باز و رایگان Pigeon یه فورک از پروژه تله‌میرور برای macOS هست، که از طریق اون میشه بدون نیاز به فیلترشکن یا لاگین در حساب، به محتوای کانال‌های عمومی تلگرام دسترسی پیدا کرد.
👉
github.com/MaroMushii/Pigeon/releases/latest
💡
t.me/PersianGithubMirror/4500
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 34.7K · <a href="https://t.me/ircfspace/2296" target="_blank">📅 17:45 · 18 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2295">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/EOVxObkSX9-tv46wGh9oTPUFBTSqmVXTEc5jNJp312TSj0QHLQy5cL7O_gTcTBix4FTfFlVMIwJvkCBKTD6giQWbr0rAeS3w_M3-IcSqitRy9a25sN27zK7--x75X1njWF9y8JVlbTYaVHxAWq9rgEHqdjDMsP_2tbgiRoKjtoSbWK-o3yBVwxnv6hJ2XnDaCxL1eb3HCHC7q4O0z1m9Ou63MGSyh_wvmvWuLPfhjKZrBbxIfAm6dYCSMeEN7iwAlCZw4LY6NMxOX39VYya9f0ovEXRthCdcpJc-ru_8ZBC-GZUtg5hey-Bm_eAlsYxnMz2Lev0vDOd6MK75ZK-ovw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پروژه Youtube Sandbox با استفاده از GitHub Actions بهمون اجازه میده که فقط با ارسال لینک یوتیوب توی کامیت‌مسیج، فایل ویدیوی موردنظرمون رو توی فولدر Downloads (داخل مخزن) ذخیره کنیم.
👉
github.com/iphoenixon/youtube-sandbox
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 32.8K · <a href="https://t.me/ircfspace/2295" target="_blank">📅 17:36 · 18 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2294">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/T1kT8oZEDNeca8KFhciWaqOd5Z9Vs27hjakxI3v7e-ofgu5EQ0SgP8z5ZJ9RVRp1MtmiTto9vSdH80dkDEKN0fVulKoF5J_jTtFcv5Nkm4Lh7h6sWyvtPZT1WL7LYj7FWPEy1HQVvo5fi9OwGjQ_bvk5y5PfUBQqzl8rUKqdXsI-BUol3-rBCQnx0hNMc95rQ9rY6Ux_QPNyJ9-orjxNcbcEd1RK5E_3prBGjkov98j5ZjaaSYquOlK_ZUob4h38jYKq9b4k9wNa7To-JwLIx8-HAK_0OpJG6I3IXboGI1mRCuSZZ51df8i9db3eN7SabfWanskgFt9pf26wg8LLMw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اگه گوگل براتون باز میشه و در وایت‌لیست اینترنتتون قرار داره، می‌تونین خیلی راحت با نصب این کلاینت اپن‌سورس به گوگل درایو در اندروید دسترسی داشته باشین.
👉
github.com/aleskxyz/Round-Sync/releases/latest
💡
t.me/PersianGithubMirror/4489
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 28.1K · <a href="https://t.me/ircfspace/2294" target="_blank">📅 17:26 · 18 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2293">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Q_CaQfbzok5Ire-rvfHbGrsJBKo1APtWC6BfzrkuN7O7IJYD04tP6CArKMnkPzRtszaffjNMlt-y9o_lrRaTG3losllM5ABQPZw1HOeWD2XMOfSzfcaEpAnYtO0kOGmtJSzZGw6WdLlCMgEoUcRLy0Gn3PqBCrZcgFDPhLbpH6CMxSpqrZPC80rEhIttfGZPB703xGDK6C8FtTqEXqpH57SZkmjufpozIx_b0j-x9C02nWr2kCK-j6HpbIVCix36jNVRv4K3WnfScx7ufY4lJaQlzpQ7ioE_WFNrIEeeKOXjLcRrnlBXheeu2Z1GdQnLxjyrXhyJQ3c4m2jcyh4azg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آپدیت جدید کلاینت ZedSecure از طریق گوگل‌پلی در دسترس قرار گرفت.
در بروزرسانی جدید این‌برنامه پشتیبانی از پروتکل DNSTT اضافه شده، هسته ایکس‌ری رو بروزرسانی کردن، بخش تنظیمات تکمیل‌تر شده و یک‌سری از مشکلات برطرف شدن.
👉
play.google.com/store/apps/details?id=com.zedsecure.vpn
💡
t.me/PersianGithubMirror/4496
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/ircfspace/2293" target="_blank">📅 17:15 · 18 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2292">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">۷۰ روز است که جمهوری اسلامی با قطع سراسری اینترنت، میلیون‌ها انسان را عملاً گروگان گرفته است.
این یک اختلال اینترنتی نیست؛ حمله‌ای مستقیم به زندگی مردم است. کسب‌وکارها نابود شده‌اند، معیشت خانواده‌ها آسیب دیده و ارتباط مردم با جهان قطع شده است.
در سایه همین خاموشی، بازداشت، سرکوب و اعدام ادامه دارد؛ بی‌آنکه صدای قربانیان شنیده شود.
اما بخش بزرگی از جامعه جهانی همچنان ترجیح می‌دهد چشمش را بر این فجایع ببندد؛ چون واکنش نشان دادن هزینه دارد و سکوت، ساده‌تر است.
For 70 days, the Islamic Republic has effectively held millions of people hostage through a nationwide internet shutdown.
This is not an internet disruption; it is a direct attack on people’s lives. Businesses have been destroyed, families’ livelihoods have been harmed, and people’s connection to the world has been cut off.
Under the cover of this blackout, arrests, repression, and executions continue while the voices of the victims go unheard.
Yet a large part of the international community still chooses to turn a blind eye to these atrocities, because taking a stand comes with a cost — and silence is easier.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 36.6K · <a href="https://t.me/ircfspace/2292" target="_blank">📅 16:29 · 18 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2291">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">قطع طولانی اینترنت تحقیر اکثریت بزرگی از افراد کشور، یک‌جا و باهم است. اما این بین، گروهی که شغلشان به‌هرشکل به اینترنت وابسته است، تحقیری عمیقتر و نفس‌گیرتر را تجربه می‌کنند. با آن‌ها طوری رفتار شده که گویا شغلشان "مهم" نيست. حرمت ندارند و می‌شود با زندگی‌، زحمات، اهداف، آینده و برنامه‌هایشان بازی کرد.
©
DevYara
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 31.4K · <a href="https://t.me/ircfspace/2291" target="_blank">📅 16:19 · 17 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2289">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">بر اساس گزارش جاب‌ویژن با عنوان "تاثیر جنگ بر بازار کار"، محدودیت در دسترسی به ابزارهای اینترنتی موجب اختلال یا کاهش فعالیت در بخش قابل توجهی از گروه‌های شغلی وابسته به اینترنت شده و بیشترین کاهش فرصت‌های شغلی در گروه شغلی دیجیتال مارکتینگ و سئو (۸۳ درصد)، طراحی گرافیک (۸۲ درصد) و ترجمه و تولید محتوا (۷۹ درصد) ثبت شده است.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 33.2K · <a href="https://t.me/ircfspace/2289" target="_blank">📅 12:07 · 17 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2288">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/nsFgzKAzEc6Hw4os3q9Qgs783RTi2hXbr_8lMbamr17fzXYowMonvj6L0FfQau2gj_Zfdjss0AXNO5Od2h4tzni3-2JB7pgISRfvBc0J65r1XiKxMN2X59Dyf02aeGTjYJiGMl1VxtiV_JsCtJEg6P71ehic7Ix0gbjK7LjeYrtQPDAF2dd1gA-LJdmWUV3dV-1sH8rAcPqobmYsbgWI-z878hMSN_Fmwar2duuCLbZFPwY9FJcgHoJ7nqoetQLBEP_6HYEQiYLFwc4oc7AZ9B7nIcageccOnVrHujpYI8Jl8uj614yrfDkC9fJ3ltLTOv-QLlg1CkaZn0JmWTWOvg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اسماعیل بقایی شاکی است که چرا با وجود اینکه که پول داده، تیک آبی اکانتش حذف شده و ...
در همین حال میلیون‌ها ایرانی پول اینترنت دادند، اما بیش از دو ماه است که یک شبکه داخلی که فاصله زیادی با مفهوم اینترنت دارد بهشون تحویل داده میشه و از دسترسی به هزاران سایت و سرویس محروم شدند. سانسور اینه!
©
alirezashirazi
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 35.1K · <a href="https://t.me/ircfspace/2288" target="_blank">📅 12:02 · 17 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2287">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">وحید فرید، کارشناس اینترنت گفت: ما تجربه قطعی اینترنت را در دولت‌هایی داشتیم که به ظاهر حامی اینترنت بودند. خود پروژه شبکه ملی اطلاعات یک قدم به سمت ناامنی دیجیتال است. کسب‌وکاری که اینترنت می‌گیرد از نظر مردم رانتی است و روی حقوق مردم پا گذاشته. حاکمیت با قطع اینترنت به جامعه سیگنال ناامنی می‌دهد. /کارزار
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/ircfspace/2287" target="_blank">📅 11:58 · 17 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2286">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">سمیه توحیدلو، عضو انجمن جامعه‌شناسی ایران، قطع اینترنت را از منظر اجتماعی خطرناک توصیف کرد و گفت: در زمینه قطع اینترنت حاکمیت هزینه-فایده انجام نداده و متوجه نیست چه میزان خشم تولید می‌کند. آنچه در این وضعیت تشدید می‌شود، شکاف دیجیتال و محرومیت نسبی و شکاف حاکمیت-ملت است. /کارزار
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/ircfspace/2286" target="_blank">📅 11:37 · 17 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2285">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/uWQTCs-nfshFY1rE1GGInNjqwmKcxQ4RwUeMhuD70aPOvhjmvGSoR3MEMXRx7i14ey-xHlCBA0WpRDhlLovZ0ubeq3c9rv4OWa5R6lNtwZW6zulXC4P9nWpyUSDJLzkG-9r16EbayzvEmWxcFBAJAM_yPJFkGghdWvaKHy89S-PlUguyXE7r3bUGwBJ6ySvgkr4sj2n1D9posJwLe4dgMyxJbDTxc0iy-VIW1-pnCWHsNQ0M-E7RZUHfuC3CTvQFmJOwAr7UqWnA8MPc3EHXWAWWimU32F9gXCtXSf0emdL-sg5_F-lMmN9cvvxYX9nkqAHNwoNE1BvsZkGOzYTQug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">برای شرایط فعلی اینترنت ایران که روش‌های عمومی دورزدن فیلترینگ عملاً کارایی ندارن و اسکمرها و کلاهبردارها زیاد شدن، مدتیه یه مارکت‌پلیس برای خرید و فروش کانفیگ راه‌اندازی شده تا خریدارها و فروشنده‌ها در یک بستر متمرکز و نسبتا شفاف با هم ارتباط بگیرن.
طبق توضیح تیم دیفیکس، خودشون فروشنده نیستن و تمرکزشون همچنان روی ارائه و توسعه سرویس رایگانه. این بخش صرفاً برای وصل کردن فروشنده‌ها و خریدارها از طریق این فیلترشکن و حذف واسطه‌ها ایجاد شده و فعلاً هم برای تراکنش‌های رمزارزی مرتبط با ایران کارمزدی دریافت نمیشه.
در این سیستم، مبلغ پرداختی نگه داشته میشه و برای مدتی بعد از تحویل آزاد میشه، کاربران میتونن به فروشنده‌ها امتیاز بدن و تجربشون رو ثبت کنن و کانفیگ‌ها هم بصورت رمزنگاری‌شده تحویل داده میشن. البته محدودیت‌ها خرید بصورت رمزارز رو دشوار کرده، اما افراد خارج از کشور میتونن برای خانواده یا آشنایانشون داخل ایران خرید انجام بدن و فایل کانفیگ رو براشون بفرستن.
👉
market.defyxvpn.com
💡
defyxvpn.com/download
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 31.4K · <a href="https://t.me/ircfspace/2285" target="_blank">📅 11:26 · 17 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2284">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8fb8db45e7.mp4?token=rg9lU1ndtpgAebsnMxB0n2zrIxB-H9n5oINb3HccHw0d0hczBnncqZ9l2V-jcZ8YE2NF3o3H7JoP9GkbEwJr63pBPRW2UqqTXUfKJylkIXr1aRBtzclbKTYHdmgM622ZtQmSmvcfXPIJJc5UKo_3WYfD-P97LM2vMwEhIMJYv4Aa8sVirN7YBRguRmBhJ_2yjJffs3vRQw1S8qVvkC0K4qrQLeRd7u16NThav4MY85H-FrP-GekCxf9MjhOnzTEnEd8q_tHepunxj0GCgBv0VtQKxdybq-ARW0RWO8lVd7vtLKcWQ_0_WQP2xSieHeNRWvxMk47Y1aw12olAVFf8sw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8fb8db45e7.mp4?token=rg9lU1ndtpgAebsnMxB0n2zrIxB-H9n5oINb3HccHw0d0hczBnncqZ9l2V-jcZ8YE2NF3o3H7JoP9GkbEwJr63pBPRW2UqqTXUfKJylkIXr1aRBtzclbKTYHdmgM622ZtQmSmvcfXPIJJc5UKo_3WYfD-P97LM2vMwEhIMJYv4Aa8sVirN7YBRguRmBhJ_2yjJffs3vRQw1S8qVvkC0K4qrQLeRd7u16NThav4MY85H-FrP-GekCxf9MjhOnzTEnEd8q_tHepunxj0GCgBv0VtQKxdybq-ARW0RWO8lVd7vtLKcWQ_0_WQP2xSieHeNRWvxMk47Y1aw12olAVFf8sw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">طبقه اشراف و طبقه رعایا
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 31.5K · <a href="https://t.me/ircfspace/2284" target="_blank">📅 11:01 · 17 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2283">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">وارد روز شصت‌ونهم شدیم. میلیون‌ها نفر رو با قطع سراسری اینترنت گروگان گرفتن و بازداشت‌ها و اعدام‌ها در سایه خاموشی دیجیتال ادامه داره!
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/ircfspace/2283" target="_blank">📅 08:16 · 17 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2282">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/UYsMMl7xDd3CpgZO_RpjjlKRMdAjpacfCgZNYhI770uVNi88zW6Z1gjHAQum8sVsXOynFDRsZ13NJEf2Rj_MlAdT020L_8Mq7AkVmxflai47zjC8k-ktoix1mGFJ6fbY5iY6R9PjwqAsjZ3t6jIbaEHfbyv4s8H1DBqneOMglo0Td9hLWnX2IbKS4u31FtejwSePddxHmEWqyasGu3ipjg612_oxYHD-S5p4p9GP6hrjBUWiJBdwTOUjR4UogMb2RZBIU9jDNKhe6z2wXuOmTNhWeBUNjVbAHTTizVlaYE0J103m3XiWEvgPOIRyPoOnm1mrQmxusr43wIIIEHvsUQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در آپدیت جدید از اپ theFeed امکان فراخوانی محتوای کانال‌های عمومی دلخواه فراهم شده و پشتیبانی از اندرویدهای قدیمی‌تر، حل مشکل رندر نکردن نظرسنجی‌ها و ...، بخشی از تغییرات جدید هستن.
👉
github.com/sartoopjj/thefeed/releases/latest
💡
t.me/PersianGithubMirror/4273
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 30.2K · <a href="https://t.me/ircfspace/2282" target="_blank">📅 18:20 · 16 Ordibehesht 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>

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
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-06 14:04:32</div>
<hr>

<div class="tg-post" id="msg-2390">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">عدد ۸۸ برای چینی‌ها نماد خوش‌شانسیه، برای موزیسین‌ها نماد پیانو، برای فیلم‌بازها نماد سفر در زمان…
ولی برای ایرانی‌ها، یادآور اعتراضات سراسری سال ۸۸ بود و حالا ۸۸ روز قطع سراسری اینترنت و خاموشی‌ دیجیتال!
جمهوری اسلامی اصلاح‌پذیر نیست و بین اونها و ما دریایی از خون فاصله هست.
از فرصت استفاده کنین و دیوایس‌ها و برنامه‌هایی که دارین رو بروزرسانی کنین.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/ircfspace/2390" target="_blank">📅 21:56 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2389">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/KxmLLyWCHgqQvjPp_OXdjC8kviPMb-ZgU1zVeceHI0ZvgjKmjBshcqZ0Sqy4P1u8B16MIu9Sl7FoNDkWG8CSVn69h1GYTkXjqAAd8vRr2WJipNgeydi50NcWh46U5gjw656ZvFVAllU5z1e3j1Fj72v_81Mgu0rLmPnT7naVMZg6DISmHQbnG3HNPOrz-Iw_JJZ90LAOJrVMdycpNdbsgYyoQ8RRUdSjijZiVzYkXCw6wUo444409y-a6qPAyMtXCG1_dpOS1eqtYgsKLUxbpV2G47sPZxTum6aPcfWLXU4CjZlgfmUsHGHLf_eYVCD6Wbvaf3edjxtAc7l3K0drxQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نت‌بلاکس تایید کرده که میزان دسترسی به اینترنت در ایران افزایش قابل توجهی پیدا کرده و به ۸۶ درصد رسیده؛ هرچند فیلترینگ به قوت خودش باقیه ...
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/ircfspace/2389" target="_blank">📅 21:31 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2388">
<div class="tg-post-header">📌 پیام #98</div>
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
<div class="tg-footer">👁️ 34.4K · <a href="https://t.me/ircfspace/2388" target="_blank">📅 17:30 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2387">
<div class="tg-post-header">📌 پیام #97</div>
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
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/ircfspace/2387" target="_blank">📅 17:24 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2386">
<div class="tg-post-header">📌 پیام #96</div>
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
<div class="tg-footer">👁️ 36.1K · <a href="https://t.me/ircfspace/2386" target="_blank">📅 17:19 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2385">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/riKFLFvPfWaLPSaVKxJjQEX4qaEcnspC0JZp8ovwooWW_em88HKK4IejPCbJgldjMy_MCtxgFVaQsB6RiC_T65DoV-i3jC5VHGxswcUvD0zbiahbNzJj4GzXtDFMRIa59JWK6Zti1k1vnOrG9Z7tk9m9zib3qP2P1GJodZKdn4ksd66KNbMuxzZzvJ7UbTwF38Q9AsmpkrsSR36s5NDK-bqzy0TI98h9fWFgEBHeA_8Cu577lum-44UZIJH8tCNHy6qdqybPtBCdQ50ABGHpLsfdLMhM4l8xMCgkKTcd6Uotoopl2IY2PB3IidGXCFDUy9O3drxbCTGIuR8Mj2_uRg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">۴ فردی که در دیوان عدالت اداری نسبت به اتصال اینترنت بین‌الملل دست به شکایت زده‌اند، کامیار ثقفی، رضا تقی‌پور، رسول جلیلی و محمدحسن انتظاری بوده‌اند. /انتخاب
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/ircfspace/2385" target="_blank">📅 17:12 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2384">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Rmz6ykbVaei8itlTfUt9M3-bx5vBlZTLKaJd4tre_fytvbpphwOGgwoCQ7Ygbeu6JuXK-SJ0i2_ppat4sc_LKriTaBE_UrmASehBc3Wd5ALk5mPJGpIceMUAVxMnM9spDMkIbsqUqmmU1dbWpmqvfKNikCKpFj5XXO8IcuEPRJHYhUgR8c-z3g5MN3wxB6Xi-WYDvHVHpKsY_PRWJy_I08SyjHQJWxs6iORKKKdnb5us_jNGr1AqyEuldD6emTsf0TwFHjzYRVfLB9UQS8TsJgBrsXJyMgRM42MtpKjY1hgSXXNZgw71-E2YBiaT_V1FmL5AmF3EFiVcHCjfr1sQOg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نت‌بلاکس: داده‌های زنده نشان می‌دهند که در روز هشتاد و هشتم از قطع سراسری اینترنت در ایران، اتصال تا حدی درحال بازگشت است. البته هنوز مشخص نیست که این بازگشت اتصال پایدار خواهد ماند، یا خیر.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/ircfspace/2384" target="_blank">📅 17:09 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2383">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">دیوان عدالت اداری به مصوبه تشکیل ستاد ویژه ساماندهی و راهبری فضای مجازی کشور ایراد گرفته و گفته مصوبات و تصمیماتشون تا زمان رسیدگی به شکایات، قابل ترتیب‌اثر نیست.
فعلا اون نمایشی که پزشکیان و هاشمی واسه وصل فیلترنت اجرا کردن به دیوار خورد و شرایط روی ملانت باقی می‌مونه!
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/ircfspace/2383" target="_blank">📅 14:43 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2382">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/rFgbOjat40YmS_t8XEPlnnMf72Ef-2ilTy4km3i89_yoDatXHrJb2mwJatu2MX-yvPvVxf3sqhdXC3vx2xJ1jFQWCFzboPjT3TctpbjB0UxXLEg1mq0sDZj6vwzgvq6hyefpgTnEVKNrZlzXiToiS0WgXYJm7iLck8LTgwA9JqJJbh4g75LEmFWnV7RJttJnj66NThrOSOfTfGIsVblIiKx_joKxs-lVgSaGd4uvbY0WdUx26rCpQ6M6xRjpZg-DIGaEqwTvYGHyv6i_2e5IK6D8S8QPLJ6zdyZwf348jppv3mLV2Xm0nw8aGImY2ZW8NzM7LqjLWbqw2SR7CnM5Rg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رسانه‌ها نوشتن که مسعود پزشکیان مصوبه بازگشایی اینترنت رو امضا کرده و بعد از ۸۷ روز، بزودی فرایند اتصال مردم به شرایط پیش از کشتار دی‌ماه برمیگرده!
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 28.9K · <a href="https://t.me/ircfspace/2382" target="_blank">📅 23:19 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2381">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/XW-zdO6gTdvEYfQEHR_ymZQpZVC4XuinOsvrb93RAuES_feYyZgJckhZQr_yQbIBW4qdEIVgn42-ZmP_VPEvtoxUV_ykfJMidgMnvZKOvKbIg-c6vjCnFZW98BTIa1d3TOH8YtReTD1dd0RZfxUTmxIBx9vSoW5URCEOw5E15iJ1zWtq3KaZXVYjYqGQo2GdO2bsaAq5G_kXodAXYHrKnFDVW7Bu4ZLrJAk1fMrb0iyfkzgTSGG-6B1BdVK-zfXj19numBA8VT5wVsF2tWFBnr8WX0clM1WNlVeOi36A5sB_uc8tXzZvNDVJkoUQJDM2odwqtZeojnCUh93ygRbcJQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نت‌بلاکس: اکنون هشتاد و هفتمین روز متوالی قطع سراسری اینترنت در ایران است؛ محدودیتی که بیش از ۲۰۶۴ ساعت ادامه داشته. این اقدام هرگونه شفافیت درباره اعدام‌ها را از بین برده و به شرایط غیرانسانی و بلاتکلیفی روزمره‌ای که منتقدان زندانی، مخالفان و حتی گردشگران بازداشت‌شده با آن روبه‌رو هستند، دامن زده است.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 28.7K · <a href="https://t.me/ircfspace/2381" target="_blank">📅 11:23 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2380">
<div class="tg-post-header">📌 پیام #90</div>
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
<div class="tg-footer">👁️ 32.4K · <a href="https://t.me/ircfspace/2380" target="_blank">📅 17:16 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2378">
<div class="tg-post-header">📌 پیام #89</div>
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
<div class="tg-footer">👁️ 30.6K · <a href="https://t.me/ircfspace/2378" target="_blank">📅 08:57 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2377">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/NmhjNeBERAi_i4rfHtcRiEixC9u7ZAwXbGZEixsvnIr2d0_8OGhWhCCF1BFg5iOcsrb1nR-sFwkK1ZOuik5afv5iMkBjFOStBVWkls0tbYPn5x6zsxGy4ntJlW35ZVUoyhR2Zr9OGOvcLbYqvpeCnkBqAObmmDJwRcoNbDZDypaXNOsl8qSRUry_0WI3gwJsjPYJTUq5QMrpTgnaKvalmOe4_-acyGauh7fH1BG94GrLdfhtj2fFEriFc5T8Eqytk8QPVK4EhHxmd-DgX18fNgauAXK19CAghdIIEdXg1RLjENdOBND2I1K0SykS_ul9gE_wNkyPqe9jEOn0rQp67w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قطع سراسری اینترنت در ایران به روز ۸۶م رسیده و همزمان توجه رسانه‌های جریان اصلی به این موضوع داره کمتر میشه. انگار دنیا معمولاً به رنج و فاجعه‌های طولانی عادت می‌کنه؛ مخصوصاً وقتی قربانی‌ها صدایی برای دیده شدن نداشته باشن.
Iran’s nationwide internet shutdown has now reached its 86th day, while mainstream media attention to the issue continues to fade. It seems the world gradually gets used to prolonged suffering and ongoing disasters — especially when the victims have no voice powerful enough to keep themselves visible.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 28.5K · <a href="https://t.me/ircfspace/2377" target="_blank">📅 08:51 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2376">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/a874f4f669.mp4?token=kAuDDIlKMUb9kKEzYPS49SeB9pIEHe0HyT3FlCAm-jfFfZAVrDohzPfesnT2dtFfON5_dKhOyEnpDmcMKa-AUcm7luxhk6wRYVlCkqPgdnzLBZqKINjn8GNCEHlfumVDCtycIZiaWsRFrdQ7lfOQwgO_6X0abY2PeL6qsHeP35B5g4h-3ZJ_mfyxvI-pfmf4XMxEgRfjAvZ5EBrugVUnwV2621etaAQdBrChqmFJBG5XpZgcETJj8mVtmnjfmUEYl4Qc4WvJxw4Ya3Y56wgjp2yakagEaeS4p41rQFbetS5CLLbv_QXR9vb6n1KQ23PHvfhRJy_BNPry6pkjaImtNw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/a874f4f669.mp4?token=kAuDDIlKMUb9kKEzYPS49SeB9pIEHe0HyT3FlCAm-jfFfZAVrDohzPfesnT2dtFfON5_dKhOyEnpDmcMKa-AUcm7luxhk6wRYVlCkqPgdnzLBZqKINjn8GNCEHlfumVDCtycIZiaWsRFrdQ7lfOQwgO_6X0abY2PeL6qsHeP35B5g4h-3ZJ_mfyxvI-pfmf4XMxEgRfjAvZ5EBrugVUnwV2621etaAQdBrChqmFJBG5XpZgcETJj8mVtmnjfmUEYl4Qc4WvJxw4Ya3Y56wgjp2yakagEaeS4p41rQFbetS5CLLbv_QXR9vb6n1KQ23PHvfhRJy_BNPry6pkjaImtNw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 28.8K · <a href="https://t.me/ircfspace/2376" target="_blank">📅 08:40 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2375">
<div class="tg-post-header">📌 پیام #86</div>
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
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/ircfspace/2375" target="_blank">📅 08:36 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2374">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/WRih6s8IQd9S-MykwJ77hbE1tQ0KTXH9ftMuPdDVyYG9FuH4Hv9vzW38S7Xcu1JtYhq5eByfhxlm8Heh9Ncgo0HYbe2xHuxqwacHVqmmd9qiLLeeBSUXaF97jUuF16-FKL0JgMuQvAvoCbpD6E076ixddqRo4Yi3vJvuY7ZtVR-6BZXJr-TxSCl3lRhZL6gVS1EfcmbnIQIyFhKxISsb3B7ZBTBziRcmwzbXHe0i7CqmNl-XSHVn9LdDilVNUePxOOjSXslXOQczXAn1lhXAJ7NZ8UxvUu83AwSNX3AvbuxVJU9ZLIl7PK5OF7cvwqWRbXpfp9nD7dqGlvmBgMT91w.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 29.3K · <a href="https://t.me/ircfspace/2374" target="_blank">📅 08:38 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2373">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/OQVpatMiBgxl8wshjJQDy4xsQknAPXVPnOdfB2I2FCzpouimFFgxQ6KS1U14lk7L9g2trpbCchyHZfJWfMfXy1BvY9zFEyErobWDcZzPBt-d-dDhp39m04ABDrOruTXa9bAmuVp0XZfqzhPPexpiQ_1HAEhjhAvmjDl0NSKYUlh3tOyStSfCGHNSCKGiGXycbYxkJOIFurw-eaizyIdzfQVd0PyvccOD702XwUQJa91Jq71LvbJK1hpVQs3tb1LR7hdcn7aWWhkk09mj7c-fwa2sy5lM7AUKmtfKcPLh3FMf8wBwNw1BOvI4xYw9-a2FaGFS4BPGsgg_uvuhmvM0gw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/ircfspace/2373" target="_blank">📅 08:15 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2372">
<div class="tg-post-header">📌 پیام #83</div>
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
<div class="tg-footer">👁️ 29.7K · <a href="https://t.me/ircfspace/2372" target="_blank">📅 19:51 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2371">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Ro5MZP8-FcEvuyr8qkaiNz7o9_VIeXd57-OIyylt8_PJXqoXkSQWN8nX3l2EzQTYlopQWhD2tZw0Qecpj28NJmc4Iw_Jf3UWoHpDl6Ia86k_viex32OVA_hrBWVEk1a7WAOGHoq07cqbGXVTKRYyCVapjOTXy-xnjYRNklrtMzgSR1dCLLA6SuIj5XBuEF7BPg5qMjRuyqLxsum_tGPp2lk2oYfP_93KoVgU1yWquP5uBDIIu0-jqlJ_vdktIvXvYrjHg0GsDC9ZMlsNRMPncnX-Lh5ZYE1xzayiVwSJQv3Oh1gVHOtiefdPolKv5PYBLlh_m6rocOFOioRfNTp1IA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نت‌بلاکس: قطع سراسری اینترنت در ایران با ورود به روز هشتاد و چهارم، از ۲ هزار ساعت عبور کرد. هر ساعتی که می‌گذرد، شکاف‌های اجتماعی و اقتصادی عمیق‌تر می‌شوند؛ به‌طوری‌که هرگونه ارتباط با دنیای خارج به جایگاه، تبعیت و امتیاز وابسته شده است.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 30.9K · <a href="https://t.me/ircfspace/2371" target="_blank">📅 19:45 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2370">
<div class="tg-post-header">📌 پیام #81</div>
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
<div class="tg-footer">👁️ 36.7K · <a href="https://t.me/ircfspace/2370" target="_blank">📅 20:18 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2369">
<div class="tg-post-header">📌 پیام #80</div>
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
<div class="tg-footer">👁️ 39.5K · <a href="https://t.me/ircfspace/2369" target="_blank">📅 20:12 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2368">
<div class="tg-post-header">📌 پیام #79</div>
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
<div class="tg-footer">👁️ 34K · <a href="https://t.me/ircfspace/2368" target="_blank">📅 20:09 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2367">
<div class="tg-post-header">📌 پیام #78</div>
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
<div class="tg-footer">👁️ 29K · <a href="https://t.me/ircfspace/2367" target="_blank">📅 20:04 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2366">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">یزدی‌خواه، نماینده طویله مجلس گفته "در شرایط فعلی تصمیمی برای بازگشایی اینترنت جهانی وجود ندارد" و "با قطع اینترنت، کسب‌وکارهای مردم از جهت ارتباطات بانکی، خرید و فروش و بسیاری از سایت‌ها همچنان در حال خدمت‌رسانی هستند و مردم مشکل عمده‌ای ندارند".
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/ircfspace/2366" target="_blank">📅 19:52 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2365">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/EpE1Cq9cWL5UAn44ugaooqJENKy3AdLKHnUksxCDYR_6956CY-Xe-faion5yn8lTO-2Hf9ItOrd57QojYtDSJ7s6nUCfQeOxlQqkcgWC1aYAJiBpMi_qNezgiKyx8b1gQUVZpBRe_ODSJr_9H0mH_mUKvtIWWQHfYn9DwZTAIK9HsbhQYaCL3QwhrZWI7ju5l-dFnwb42G8zbBcP38WvNrYhjxWic661YaxkCrthhtwn23HXnVgpulRGgXxfgbRQAuSYO-GyJUoNLFTx5xjYEmS0XerTxfGaOYIhjx-R6_Mw0U-d8AWqewTpbjruQhisDc2CmC_LkfCNp3PLhoaCXw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قوه عاقله در همراهی با سایر قوا، قطع سراسری اینترنت در ایران رو به روز هشتاد و سوم کشوند.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 29.3K · <a href="https://t.me/ircfspace/2365" target="_blank">📅 08:39 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2364">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">گیت‌هاب گفته دستگاه یکی از کارمنداش از طریق یک افزونه آلوده VS Code هک شده و مهاجم تونسته به تعدادی از ریپازیتوری‌های داخلی خود GitHub دسترسی پیدا کنه و اطلاعاتشون رو خارج کنه.
فعلاً میگن شواهدی از دسترسی به ریپوهای کاربران یا داده‌های مشتری‌ها پیدا نکردن و موضوع فقط مربوط به ریپوهای داخلی خود گیت‌هابه. البته دارن لاگ‌ها و میزان دسترسی مهاجم رو بررسی می‌کنن و گفتن بعد از کامل شدن تحقیقات، گزارش کامل منتشر میشه.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/ircfspace/2364" target="_blank">📅 08:31 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2363">
<div class="tg-post-header">📌 پیام #74</div>
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
<div class="tg-footer">👁️ 30.5K · <a href="https://t.me/ircfspace/2363" target="_blank">📅 08:27 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2362">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/m9uyuyr1JFWdm8IWT-r5nXmXlMg2HoRceb_kKg0_zDLAq2flOKwJFQ4mMgSldGoVYGOrWJQhwi_8NGZGEIVd0l-Q0nw90fzjELfMF2cj4D8MqnPcr-6ZfbYQrPOzZpZxbpsloRKBMJNkYCeAoSi9BRCO75ZlibFUqZZOzuJDEtWZ1RmWO6jU8_bU6ErQfduLyJfe8BDapUrajImQBsY0h0QTUI-w_eMsOSLBybdEOG6SsYNNagAxYIiQs9VRLAwm6ggEWe2pya5csby-_hsG9ujnsZ6oSQ2TCBPAY2bbDo2fhVm-ZhpCY5y-XJKGcO2te05QNbp79FbgXuUI-Mvhmw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 29.3K · <a href="https://t.me/ircfspace/2362" target="_blank">📅 08:24 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2361">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/YkuIPcXwY5sXfL_Gqy0NCMQu9Q2lgkLrvM46gauNKtHnHSVThb0SvkE-cs_UJAQ18A5rIYUFEDftJ7iRMPGnSYCpX7p3Z2Ymlk1TRZKwQOcuW4qQ8L5GD-6vG5wG1S4i5kcZ9qss4e6cuOgC5Q4GWlCCIN94E2HNLowwwwOU5XVEsBChQN59Te-bxkp6l4uOaCzsuoo-DzjQaarPJNF-hKgptI0bKRtG-ZpztqdLUMQT635VDqmbD3nH6qG_3oJn98zeruKvoxpcXNdv_2Mbs11oJJX1L4RukdY4yPooppMuteTRdUbFfkcw9bL2Vm3JFEHrC3hC7PAPpkfK-lPK3A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هشتاد و دومین روز از قطع سراسری اینترنت!
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 30.4K · <a href="https://t.me/ircfspace/2361" target="_blank">📅 09:00 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2360">
<div class="tg-post-header">📌 پیام #71</div>
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
<div class="tg-footer">👁️ 30.7K · <a href="https://t.me/ircfspace/2360" target="_blank">📅 08:56 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2359">
<div class="tg-post-header">📌 پیام #70</div>
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
<div class="tg-footer">👁️ 47.2K · <a href="https://t.me/ircfspace/2359" target="_blank">📅 08:59 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2358">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Nrf79QuSH4-f2N9CKHpqAc1o_unwZdqJuUHsTinOAH37litkibL27oXEKviRzQUH25FVZdx9RYfVpFdX8BsaeDOY8Ynn0LYpIih_8BeW6wZpfef_3non2HCre76zs1-i06QwFeLhnVHl6cG45VcUtdYV1P-1XY_UsuSt_xYt89hbPh2ZK_UuJd2Dn74w0No20ctgA2jThfGyBOGnB6vcl2LfbAGLjsd6Veg0Cw6Qn8UCKjiJj6ITqixXz4KcWJSorfjUU5-GqXILZ3OHLqD8wtYEmogICVXHyjoiogFUtsoYnwKO5RB4CzFwuKY8pXIfyreVRp9laJ53D21_oJ8J6g.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 37.5K · <a href="https://t.me/ircfspace/2358" target="_blank">📅 08:50 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2357">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ApmMlA2_FmzwLL9OcsV6QChjZcMWwQMnFLcjV2UUMsvkYYV1PDug9qPS9DlxoeoCzS9X5wuKtxCAjdRJi_pIHLcoEfv4hMD1Fcv4Jca7QPoPOeHHGv_f17nd3bgKSNNOzIhvxdxx3MVkV0Ju64t11BdTV_COENXADoV-Ni5Xr60OpVCPx_WFfua2pdzxpe5YxKwi2GhETRdOpHcCDJlZNKZ4qylKqu5t52UHBv8eLHcqWWEZXD5cY7MRxNv2NS1y5rebhO7WqxvRz33qFNt5L0L4nZKc_LS1DfrKRAWECClGRglfHotSagU4r9XFufIk0-VIbRcpcIM_qqQDsSKwqQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 30.2K · <a href="https://t.me/ircfspace/2357" target="_blank">📅 08:38 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2355">
<div class="tg-post-header">📌 پیام #67</div>
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
<div class="tg-footer">👁️ 35.4K · <a href="https://t.me/ircfspace/2355" target="_blank">📅 20:07 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2354">
<div class="tg-post-header">📌 پیام #66</div>
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
<div class="tg-footer">👁️ 31.9K · <a href="https://t.me/ircfspace/2354" target="_blank">📅 20:05 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2353">
<div class="tg-post-header">📌 پیام #65</div>
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
<div class="tg-footer">👁️ 36K · <a href="https://t.me/ircfspace/2353" target="_blank">📅 16:24 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2352">
<div class="tg-post-header">📌 پیام #64</div>
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
<div class="tg-footer">👁️ 31.8K · <a href="https://t.me/ircfspace/2352" target="_blank">📅 16:21 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2351">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/WEA7qJ86kR8ymb_w5JxfMJTY6mfrUy2WWvAfvlrEOmRieXw4opZeMP8NtCxu_W1PpNSo-z5RMqtAKHq4ghP_jACyRPLhBoKqIj0LqycB1_Ov-7s34yxYj7-XUoyQJ8nxD0jpjb6Eain9iBtqLHgkE3B3pGgVGM6Is8xc7mh3YDbvzTAwGLoHK12XWG3Lmdqtro7ap_XHiKODe-blMt8jB-OoFEGGomMHUgKL0h7aheCUs_YXCvimGqDdDU9Bdrh1j1zq8JjpnNqQl5n1ygUANLQgV1Sf4NkjvFwvo05-Xetlm4tx9PjHaRYaVtYZWfElC_w7lErpSB2uhDJ15hZtog.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 73K · <a href="https://t.me/ircfspace/2351" target="_blank">📅 10:02 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2350">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">باورم نمیشه قطع اینترنت به ۸۰ روز رسیده!
وقتی حکومتی برای حفظ خودش حاضر میشه یک کشور رو وارد خاموشی دیجیتال کنه، یعنی مردم هیچ اولویتی براش ندارن؛ وگرنه امروز وضعیت اینترنت، اقتصاد، مهاجرت، ناامیدی و زندگی روزمره‌ی مردم این نبود.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 32.1K · <a href="https://t.me/ircfspace/2350" target="_blank">📅 09:21 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2349">
<div class="tg-post-header">📌 پیام #61</div>
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
<div class="tg-footer">👁️ 40.4K · <a href="https://t.me/ircfspace/2349" target="_blank">📅 21:08 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2348">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Qv7ictC4NL3Wsmd8Ozek4GKfzZ6ARfG3iOEqDOTWTEJM6nmB3TI1JFWedbwS4-D4V8iNrTT6Z_0JYUPrF6G5wlTE8UPSdPkkpbBwzoNtTPLxQ-5atm6VQog1iLA3d6rbRxdKk6_y42Pw6Gg4vdkTzY5GWoXm1n_iI2eFL4mYAtPlNPECqvwPxlJIgnHBFwGDklEkMXMqJQmVEVEF41okH55GmWyGHEB_pVWM29F62N4qlsHKyWB1SwqxFAHQx3-NgiCScELvM_K1u_rDBIIAOY-CDv1-wSirT0MQrWJMmknVfqhkpmTax5erh9Pq-P3y6AUXHrKy5vaHkfn8SyZTZA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 37.9K · <a href="https://t.me/ircfspace/2348" target="_blank">📅 08:49 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2347">
<div class="tg-post-header">📌 پیام #59</div>
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
<div class="tg-footer">👁️ 37.5K · <a href="https://t.me/ircfspace/2347" target="_blank">📅 08:31 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2346">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/SVlEmxH5ayXRDMF0c9amYwIxdGIL9u9y_zCFpz7XnkTmJ-fxGgRMhABCF6Du5aBmPHKBl3mBX7G-G70wuAgXGcy7BTk3BmOr0NVv9YfgEKD7zOGs9SDKEMupwDKmqbY0vPtuU_gtDZxeInvma_e8W7uWPE0n73pC4hvpDgYlKp98tAEffmG7wUVvU-5j9fl-Wt8ouy1VWq6k-914dDYvUfqS2a-3Z2mR6fHrei6BO7OZcCQdnO0GO4x-0Q2knAcy_8rPpSTbpa5vhwhr3yLTKy55mYBqZ6uk4iUEkVt1-ScOkD4krg_PqKw6k0p4RzrhP4j5NXITR7aGKWhX7avj0A.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 39.4K · <a href="https://t.me/ircfspace/2346" target="_blank">📅 23:40 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2345">
<div class="tg-post-header">📌 پیام #57</div>
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
<div class="tg-footer">👁️ 40.2K · <a href="https://t.me/ircfspace/2345" target="_blank">📅 23:28 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2344">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/SJT77xfQvuu-ePraZy0UrCNBnc3giTF8ufcDcnE8mHQlorgHJc2VShDgS0iTVCPnptx6BlOpAwJCLkIsWBsSZAeNKq5CoZ4TiD9KV1-1EryyquJMzBeM7XeCIROv69o6cLTG_kW3IiHaGnxDvdTg9eszuktMWh5Xb3YSu1gH-6aX-nVNngL_CUnOz1KvjNuRblbX8JwVRttlIA9EsZ5nIjc59KNIQdouBJ6YmjkDZjwvivgzfnuNacDr_LfTlMVeLa1mMsIuPPJQrqci9rjCMUt1fUpK6VHCY0MVaGJEpDRXuZGfEY5sOoBwfRdbi3_0is0DlmVABPxb7x-_335Dew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رفتن هرچی که تهش Hub داشته فیلتر کردن؛ حتی گیت‌هاب.
قوه عاقله‌س دیگه!
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 43.7K · <a href="https://t.me/ircfspace/2344" target="_blank">📅 09:21 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2343">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/g3P__OyC3tX5EnGq5f64BFyoYOf2JVOe17igVk6tPGvFt7CWE0d_fvWeMWZDUBu0x9TlWFPr1VgWEmLkni6G1CnPDlRewuyMSa95N6EtWnX7hwwd-v0osgmlu0YeYwHDrIMv2Hl9WgtVPcVYToraAd7CIA1z2jJXikhCG0ppnXbUwuDGSUa4C7fRdxXjzDiN_gNuD2zPfkUwF9UBhqga4ZkCJdmFUsbgcCJJBAeblaf_B9TFqTQ6HNs93xG2rk_pR-NpVvk5PkKFvjnhLvGn6ZxlbiKvmS1iCsqZHT96aLmmbAx-e66jOFfqfqF793PDPiviz9IjTjctG21VKQykMg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 38.1K · <a href="https://t.me/ircfspace/2343" target="_blank">📅 09:11 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2342">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/TdsdiPqPTBfNME-lP8h-E1nquUiWkvgLZOOkYDgQqQtGCY7AqwQ-B7P8_QUZ9kIdTiFEN6LFejUWjeFf3HEoFtH0-voJHfqJmpsvA54iVdW3GPI2y_NmaWg3Z8bchlw72YCY0OMNY6tGUWE7OVJckdIaovPSwWgJUFC55XBIFXlSL56v91i8PbNcjjHuWw3uMSVm6DgyHxl3h2IGriTFRiuFv0UYs2dc4MqIrUBL-HbnkYTcU1zBm5W1Z9D2YONlz09fcjhWazV7NyRdKjIQwVhUqgO-QAYAoVqt91ghsrf9Ulhkm3jrqIur8ADywbGKDIYXib2BTbzkjE4d3_sqgQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یه آسیب‌پذیری جدید به اسم YellowKey در سیستم‌عامل ویندوز پیدا شده که توی بعضی شرایط میشه BitLocker ویندوز ۱۱ رو با یه فلش USB دور زد؛ البته فقط وقتی مهاجم به خود دستگاه دسترسی فیزیکی داشته باشه. برای کمتر شدن ریسک بهتره ویندوز و BIOS آپدیت باشن، سیستم کامل Shutdown بشه نه Sleep، و برای BitLocker رمز یا PIN قبل از بوت فعال بشه.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 33K · <a href="https://t.me/ircfspace/2342" target="_blank">📅 09:03 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2341">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/k6un78QnyuJtJXDI4rfCzEzjKr3OpL3cgurzk4vvmIsw1H6ogY3MVzuF0rS2tZUmULABYMbSQO0eVOjgo9Lwt3YwcCD2BxV9HSOXmpOMluutwSTKiuuiFTLulemUg4PYUy3iZRg_hT-V2KPszuVkB1ho5f7wV1G8gK6qdWcbVdPwXdNV8Rasx7TqKmnkNiVsEmJHx567udc1DoeYAMZMW0chOxrOUi7vcfxLutKbGb-3CX6AsG4LatDfu461dSZX9qmgSqn_amiTje20BQnrcmtyceqxXA3FQl3r-ojijIfXaW-ID3P6jafwachxklhWnoCkfb6IeGxl3XjdkuALAw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 30.8K · <a href="https://t.me/ircfspace/2341" target="_blank">📅 08:44 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2340">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ss_PFncWOxmJUZm6cJ9uU4PWQEcUtzhVhm3cWhDJYi7ROV5-3tABjtbnwA-J_u4Vt8wO-F3e0A59b3mkz5m1i51hb-4OMHu4CkNoBFy-Y8PQnFDQx4hrQRn25CRrMGd_V2EOMM07d4sNQXRiXI4oFzMo3yTGuDduXoHm7LulBXlLR3rvmCK2l6u_ksb0pZQkXrLmWT0VkzYbOkyg5-mQ6IcxY_uIPSqSF3iE7uLD_iT2LS4-rGCWCY125jsvsaMylm1e9txr4brRnaSZVsFnpiRFH8nn1seL7DDKyPS07MGUJ-X2Ucnv5fGyRX0Vjrcajrur4wxAXRoJ6S081mX-lA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در هفتاد و هشتمین روز از قطع سراسری اینترنت، از جدیدترین روش ترکیبی عبور از فیلترینگ با ذکر "لعنت بر جمهوری اسلامی" رونمایی شد.
😁
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/ircfspace/2340" target="_blank">📅 08:38 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2339">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/U_VQplGE2rKuAOX7iHIWctbMJi_RP-hxzfNhLiPe4tlY-a9dGX4EYf4xCJ2w0yUU0uBrbTtldAijL9GphZJ1ZstYN4MjxbsYE90LRfJtkROjxs2yD2KxjnGp4XQjO46igLetTB7B46w00RDLeRc0PWrtuVNHmNCkFYdk21U5ed3WgfUo1kAQfytlkIajxFzR-d2L043vQwfr5401s1ajmDwtQPZQgAuLdJiiNMH1TfshaImos2tsNrvPtRc2emYTwN1uKXCQS6Qiioqcg9JIkCvS8rPAmrhrt5_8eTtGt4UhaOj4VTJWuJEPWl5De6qlQtsl3yWxo0mscqaR6r0-Gw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 28.8K · <a href="https://t.me/ircfspace/2339" target="_blank">📅 08:28 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2338">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/T6uGASGZMJw9me9uXxgYLE93MbM4vWljKLzHvbzBDwy1WXoEBixCOBeRR0yu9U8-gnt9fjPtC9Qz9ptgGWo6qxCSVH20Vg4S7BTk8ubI6MULqEFSuODkvw0pXFaHMZGqrRN3WoNs8MuHOS1ihsGBo4IcvfnnZbVzsnQQZZTK54UOpz2wDwsH3A5-tiJpfe8Iit5sxvbn5w9zrJ-TAD9nrRVwXL1yXGvhkLieo4QLu7UNyfizfYajxnTPB8n26QVEzWCSgYBzB7GFGBWKsu4pYumtx7a1j-MFJJOVKUpHgpC7WLLDw6fVvCvGe4wzoNFyZa_g0jfNj6QeyWBwtmANSA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 29K · <a href="https://t.me/ircfspace/2338" target="_blank">📅 08:27 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2337">
<div class="tg-post-header">📌 پیام #49</div>
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
<div class="tg-footer">👁️ 29.6K · <a href="https://t.me/ircfspace/2337" target="_blank">📅 08:25 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2336">
<div class="tg-post-header">📌 پیام #48</div>
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
<div class="tg-footer">👁️ 31K · <a href="https://t.me/ircfspace/2336" target="_blank">📅 08:25 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2335">
<div class="tg-post-header">📌 پیام #47</div>
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
<div class="tg-footer">👁️ 51.1K · <a href="https://t.me/ircfspace/2335" target="_blank">📅 16:26 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2334">
<div class="tg-post-header">📌 پیام #46</div>
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
<div class="tg-footer">👁️ 40.8K · <a href="https://t.me/ircfspace/2334" target="_blank">📅 16:18 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2333">
<div class="tg-post-header">📌 پیام #45</div>
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
<div class="tg-footer">👁️ 36.6K · <a href="https://t.me/ircfspace/2333" target="_blank">📅 09:19 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2332">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/cTWgguGDTy1hCbLT8Dil1Z70SMVTypsdpFnuYVfOsNhnX9_t0Sud-gXa6RFLzp6lv-pSOeHVP97IeDBX-QGUgM4odqXXrSs4qWgCdykJ13WxHVsBQ6x57jT2uJRG2D4ubwDVAj7_XzaTge2DuLq0RriFCP4qFrF8uJBG5oUwfrfjC2HMYXSYSdl2pG4k0dVPM9VDuy_FjKK5uOY6n6KXVHiiy1-zMomnsaQP2culsJWaqlOyWz3212aMLLlqkT03mjX13rmhuP3-rH7GRRYrIbyCckY1mp4GfTd-rnIDiFXLXDwlnH7udZoX_4KF_Pm8gZOHnP423fzga-ritzCIgg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سخنگوی کمیسیون فرهنگی مجلس: امروز پیامرسان‌های داخلی گوی رقابت را از پیامرسان‌های خارجی گرفتند.
🤡
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 36.8K · <a href="https://t.me/ircfspace/2332" target="_blank">📅 19:39 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2331">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/lqBVJz2OgnDcY3CoaKyVf0FsKPA8dY0NnD4xx3mv0XF89Z-t4FnIs8gwR8zIAzfWc-UJepET-Di_oB_GZvbWYP9gG8950u_ciD3c35HjIBM1fJHoiLyum5Izi9ndBwd70EiRsJHA61mCUTywh9mZvbyuh0RX14taKTIJBeYSIAqIQtsIyhrxXklBuy7wk7ucF3zEnJ5kTQ2L4nkw0uoqsnGZ1xgE4AU2e8acbczPpsduczgUY0wnnc0hu1x7p9Qyg6bVThHPGWYw6JBqIhh4UYUY_OBjG3YxhuuDWQMPhfiNS9EWYOtMhZqmp8cw14cHXftT8Ys6bl-LUGBDIKLtjg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 32.2K · <a href="https://t.me/ircfspace/2331" target="_blank">📅 19:36 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2330">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/uFZ-fMb9n0l8fPumL2afQWEc8sveGIoXXQ7qAXopCxuwKMAfJf4hibtQdZ2SNHGsVCdXxBMCO2IB3NkcveHb5xiXB-XUHxQCkxK_FcAOVOhqmyuM6GxDluywOghgoJ4ec_lD0_avzJK28sGAkqQ0BmZJxhGMdXsSvycFQPlnQwJm0jr998nQQwp2U2HpruHiagVkEIvh3iM_Ag55QQdjzoHnx-Jp7BM4SfZOt-YXC9GcYyGTF3WmwimeKefimqB-EADBt863dIuUkl5PpXrKNSLf93krBdjaOQ19kDY7iay9HuNnm9njFdCtJ24N9zk_u9qGuq9PssagUGQOi4Ztog.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 29.3K · <a href="https://t.me/ircfspace/2330" target="_blank">📅 19:32 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2329">
<div class="tg-post-header">📌 پیام #41</div>
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
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/ircfspace/2329" target="_blank">📅 19:30 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2328">
<div class="tg-post-header">📌 پیام #40</div>
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
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/ircfspace/2328" target="_blank">📅 19:27 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2327">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d9e9b1e831.mp4?token=UbhpAq8x3b5S6hmkyOOtgpU1o0aP-Xwkxpsx1N0dIqjtO-d8xTxKVVx66vyjWZPeNJ6KgQfRg_aIhW1vLISNxR7bCQJzuR1ANunxJ2bDPG7lEMO4nlRCNQcfqmVkTpWYrwcURgsB3p89MR3hJf80VFipcPe4oZtSwohJyalvJqB2Kie37LhRyLxXSB6DtPp3OE9eBODAkybBaWozRqkjV8GUk5yccpWdP4V3gpi99vFwIq8tP__IwAMsJ1PQb7lKVewiB4KbLH9CStR8IiWCHZFfHx1E3WBd_VQJe7NZrSKQm7v1sGW5jCtzhJK0VGK7yP1j3ZtEy2j6zhznQiZNnQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d9e9b1e831.mp4?token=UbhpAq8x3b5S6hmkyOOtgpU1o0aP-Xwkxpsx1N0dIqjtO-d8xTxKVVx66vyjWZPeNJ6KgQfRg_aIhW1vLISNxR7bCQJzuR1ANunxJ2bDPG7lEMO4nlRCNQcfqmVkTpWYrwcURgsB3p89MR3hJf80VFipcPe4oZtSwohJyalvJqB2Kie37LhRyLxXSB6DtPp3OE9eBODAkybBaWozRqkjV8GUk5yccpWdP4V3gpi99vFwIq8tP__IwAMsJ1PQb7lKVewiB4KbLH9CStR8IiWCHZFfHx1E3WBd_VQJe7NZrSKQm7v1sGW5jCtzhJK0VGK7yP1j3ZtEy2j6zhznQiZNnQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 28.5K · <a href="https://t.me/ircfspace/2327" target="_blank">📅 19:25 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2326">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/TjxlDZbWrc69Tts-gdE7HAe2yuhaoLQiB6_htL2GsWOEabSKuBolBQcuazJbpUJQcX3uNBGTkD7TOQ7389yDxaNrqpeKZaomqiJ5Mf54rBB9kmF5sOF7M_aNJ_ePSkgsBMHloN2Vu-DgR9k41WmjtJJvUfwLAmQU9yPTXiXLlxEEXi4OvqkCfXBnKddwnURjb0q-Ky-07Z4FRrMWr5AsXdacZ0rv_wun_GnAaPBEFmyKWixGagWXInYf0U-ho1r2dAdAS8p2NyOX65HPZwu-6KGt3x6lic6559F6RYqtP35zImb49rBSfjjANF21uIwUlPv0ZylYJ6Gl2M3VfJ4V9Q.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/ircfspace/2326" target="_blank">📅 19:21 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2324">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/pcgSaFH5GklMr_5pjxFmJT_q7VVJlDC5DWeogDa8zJgE8DfLlrM8jrC9jAaWr8SMv8a3UwxN06sKa0Qtq2-1fxzps0OVZUOyjOcR2w-u-IkuLaAfIH9YURuKPq8yEXkt9x5M8gJxX2n91arghRm6Q98UHcXz2qrZq_quXYBK-m4t8Vddk5DgotZ-F2tI60uBxEtl53-MTaMuCstdmrCoEtkeR52mvnZnksDOo6hiXg-LHj7kCDBQkZMuLO7hXd-t86qBBLKP0r5meBx21NYVg1JC7P2rJv7vEPr2y_Qjt9GkvV0TVs_aK7t3AcsTBXllKgfk5ODpct4UjJ0oX3gJGQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فعلا دسترسی آزاد به اینترنت در متن سخنرانی‌های رییس‌جمهور و هیات دولت برقرار شده!
🤡
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 30.6K · <a href="https://t.me/ircfspace/2324" target="_blank">📅 10:54 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2323">
<div class="tg-post-header">📌 پیام #36</div>
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
<div class="tg-footer">👁️ 36.8K · <a href="https://t.me/ircfspace/2323" target="_blank">📅 08:55 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2322">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/abYiInKXpAKGueLDhCHlEIKKJOi2A87jtSpXv65VHeBQiIQblMuK0gFy_YLb2i7WKvr_2UNhIdgUwzgjQzhMUIpwQYMrrbmisL3BmDvN4kQ3UCjY-AlaMGeMvdOXy26wWXu1py5WXhmq6lsGzGGZ4ZmCugBkvE05cvIhLgOIIXeJR3Xz_XKocMrh-MzTit8M6myBCstYQ0WHBigNv7kSOzvRVdi1XetZOLRCuhja9aGnb78aoB6XLNf-f0M6gc0-wFPBv--jmpYabX-rGrGX0rEPVV4e2dqPb3NZ0Hf_oGJHhFgXXVMpAZMOKtHgA6_1oWTlmfCVa6Q7uxrOCZGmSA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 32.6K · <a href="https://t.me/ircfspace/2322" target="_blank">📅 08:47 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2321">
<div class="tg-post-header">📌 پیام #34</div>
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
<div class="tg-footer">👁️ 29K · <a href="https://t.me/ircfspace/2321" target="_blank">📅 08:38 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2320">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/m_RnPW2Vm8eouokigWANjKdkQoHULJzYb9ltalvUcIb_cYAvNAdgc8i5zzK6QtYRa3Jq03qJJECueSsrXxhKMPecdNMMcXwRahvzvSMDV0IrT5FXHCogHC5lt1r6wGkFf8EJgW7ux-xPXr_7EVZmLb0ZZyH86MspBsFs5GLvr_4k6mi472c-a51CqdL5FhEVR_PqHEoYBHHGy4742WJAuKFtS-ZsbbcUH7jiPv3S33RvMwfVhqgQ7a0cUtkt_lqO-To1UPGBYEPcfyMI_iyO2cAofNq5HujqG7V455Wr0-yHD8vR03da2dracy_nyMQLb2a2dSur6vHzQkcoEQ2Awg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 31.4K · <a href="https://t.me/ircfspace/2320" target="_blank">📅 18:06 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2319">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Flc9C22KGQ2EZ1cZLLI_SjfDrISUPv2XEPASTNMS4P-CrUYTX2Bv16w6qA74NNz7LMqkbhrVWd1Lv2RklZjUiaLht3BQuxfUlb1paNbQ-dzIbaX0BfiHVtzCMqQZnJn5aPpDstLVmNgCY-ltyyhc9Ot6hiY19AK5zqodtjfC7Sh21CjVjivKrfCUc-a1PQsczyTMGrdnmaj4MxDVmrskQrOxMXbvn2hEiakXD_EZVSKE4Y6KdVU2X_iqbbnCzppXmiTpag8bx0z7M9LwY9mTC0m91FPwisC6z5MRcOzgX4dugui7h3pBXsI0u3rcj2jQfLEQRtBpPlc2dZ9MY0d8Lw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 28.8K · <a href="https://t.me/ircfspace/2319" target="_blank">📅 17:04 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2318">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/s6XCck-brYAxJvRAEvQgMzvA00C7MExqWuIu4LheqrS5ubhmTDuVpgr3-ZAN5x8nRXxMFJCvhavK6SehROuhsqCbqkclVFwXVZhr01HlGq-X1uWcC1AyxuYl8OaPQt6BUtW37sQPpCHp5FCt6xUAYIdhRbQ4Zlz1tYFa-975DbzG-ENGORdl5uCrDHJc_4GBzVE2usXPngtZ-GBpid6WENR216LTpp2Al24EJlOTLf1sKMPIQFnxiibxQjnNktQiHOCnpGZUoFYyhytWu_BQJyncOtN4ZUXVE6auXmNYIBde-0y8fCpcuYVMLI4kfgshn63Q3fBXSVjVoDf-4EXlhA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 34.2K · <a href="https://t.me/ircfspace/2318" target="_blank">📅 16:35 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2316">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/C0bJDpaAwf9JAVD3nlEsjD5_oIHaYkZ0Lc2TCJwY5f7Gc1XvaooJfFcfTSOQzkxRC2Z2S0GtFhXPowS1hg_5Y4Xu9abn21alufZnzvSnVUsUBjIIwFOnD7Y3EYWsi34NP2ChURSHezs02_aAVecWB0KjNBojXuwPi4wMzLARIU9BpMa8v4UdjD9wDh3mblARwV1xQb0eATmUf2TgfKkvsYL-aj8XCKc225DfcYt2UmslcuE4GafZLGKCUIavOGZvU3MPQI65j36K9X6P2PvqkFpoVRsjqruIeATnuYUvOAs7ivW8X6UYW2_rD8Jb2Z3BR3TnsRoOYZJwK0XmxsmOcw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 40.6K · <a href="https://t.me/ircfspace/2316" target="_blank">📅 10:26 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2315">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/aUueK6jd8mtCYchYw8pXKWh47iAUnZScROtoL9DgTGzuUC10k9KzoQ3WGc-McluCtCQdFUpphME8vJZaPLLgO1Y5BWsZIfCju95lgp0TUdxJBBUMqum7yF1nU0wgBIsZ4uBPDKUgXI9NU9b5_xf7k8ATNEfS5Cm2BQ0DrTtcS4rU2AFga7xQE5W56KYgcIh2VDaiERiBZ2rykizT9ijy_V-u_Xrj6-4-3lkYU6sJDjljCSaJ6MFCdJfFj2YaxNFpeA_E3cLbccQMEpTVY54tSGxOI0xRvdzim8VQST6P-b4vu7k5ycpFFsJa99ixRWboWs24ALZK-_zLKlSZAMxhOA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 25K · <a href="https://t.me/ircfspace/2315" target="_blank">📅 08:55 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2314">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/EY6L34baphm-EHNFhItfmOu1SIxUj8SatL-nKJbFnEe7mUCnt3VC2GbLttgCZw3eyK7SnVjOXsmmWIxAhEjeW1rP1LgydhGBGfUic746rl5znsyQUIhD0Flh26t1dHAa3hSKxh6_-cZSTfqeZrPp-omk5zAGyv3IFN-ndpBt3i-L40u6d-sqEOZko6RgYulgpxifwugn6JQOhKtXT8-EPhMukbOSNF--X33CWsYkuTiWgjjsp-rgM5YjwVzEu0MAccGCmK4xHLgqWRgZFlrGqrzrhERXEmZHIQJBj3dq7lZro7Xks0pH7qsPewmA5aE_vPf_JQAnPPHcYxN0Z_1DlQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در ادامه روندی که نشان می‌دهد تصمیم‌گیری درباره اینترنت و سطح دسترسی کاربران عملاً از دولت خارج شده، وزیر بهداشت برای رفع محدودیت دسترسی به پایگاه علمی «پاب‌مد» مستقیماً به رئیس مرکز ملی فضای مجازی نامه نوشت؛ اقدامی که بار دیگر نقش کمرنگ وزارت ارتباطات در سیاست‌گذاری اینترنت را پررنگ کرده است. /شرق
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/ircfspace/2314" target="_blank">📅 08:46 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2312">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/r0p8PzfZ-rSwMiw3OLDvjJH7wo5lQzfF0GJMTgxBnNgSyhKM5cgEA7bkf6IR5Y7rYm69oT2CIQRMDzq7lNTXiH_t35E78tRW_C5grRoO2P705c9_JoTMJSvDKtEcBc5Vf0b8b_XZe0-bmLyGV_75zgWIDZpDuD1q1swlzSmdYnqRobZILnd2PwS1q3nD_vjlAH3eVp9irbvtz6l-DqL3K89wIafK2-Lb28QpGcyihj5NNF40RCrAmNBmtLFdOxwN6VdUVPniFyszU0W9vpsVb7YUNDbHQdBAs9sb9-OwrqzCLI-18Afhtfb8GzqnogxhCXZRJL3KOYN8pUDdyQV1WA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/ircfspace/2312" target="_blank">📅 08:37 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2311">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/L_dE7PHF-a8atHkTGrgqKBYrki9N_cAWhwPc77nmvqp0VxuPWjBrH5HHlr6TzMYworEwPxP4kKM4Z-El5lNPEre7vqn1hT5h9lVJL6UAShuqFRUtYj0Nlpju2CxcCHZYYFTZ9k8mc6o8v9RqL7m_AqATRqanmBlwvUQhmoA_k1vL_VqdthEUf9mrbW7QzibYiQwgDD3GlhTo72Ur73xvUYEyYqYt2ZonSEY0miJU3qfcOYSdDeijVYN2oFtO6hJlCncshDlr0-6uimAMqwsfr_ByEyMgGZrlcw3cQBs3LBLpGb3ZnbTorazD4jZlnS2fdfi-5uLi2QEsAGicOqSdHQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#پیامرسان_بومی
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/ircfspace/2311" target="_blank">📅 21:33 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2310">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/inHz1Fuk8tnGls3aTX_AfpuTqg6h7OvoKQqPndL-SqEA70Nh2yaUecNiNBoMSUDxzb6yTCAIqMkY-PKVt47skeHZU5kphogWD7N8VAijkShXU4AabGOce9gknU6sGTY1Nhl3k5EYUiqkpHtjeF6VVzLs5rMuiThO0oaaziYeJfYufIhZ7UNyPVM85hulXOtY2Y0iQsd16xuaVm11Rb3Qcczby-0M_izsfCwUvU5t-csPX9Zj6nVKwSZALocXmAPynxeKZycrUdVfHlqdXZcHcAvJ0Y8Bcz1rWTvNprAfe3gnQUpsLinRdE0ruEk9L5eo5oIXg5gC4FBqtkIdjR40MA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 30.1K · <a href="https://t.me/ircfspace/2310" target="_blank">📅 21:28 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2309">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">تا الان توی هیچ پستی نگفتم که به پروژه‌هام دونیت کنین، چون حس خوبی به مطرح کردنش نداشتم؛ ولی شرایط همینطور پیش بره احتمالا سر چهارراه نشسته باشم
😂
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/ircfspace/2309" target="_blank">📅 21:25 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2308">
<div class="tg-post-header">📌 پیام #23</div>
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
<div class="tg-footer">👁️ 31.4K · <a href="https://t.me/ircfspace/2308" target="_blank">📅 11:45 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2307">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/pgmgcSAiJaRlZGsbjiPBFJnqMeOgOcwJsCSb0Vdpofauot5oaN_65sY03ACO_kFabXSo4blNniTKDvXclLZODCBLCPvOjQK97Ftvc8fdje0zcUSp7PjqTrtiPDFR1dEUYkXJpmAgZoPyu9bbAoeOTMQM-jQm46DFVn8lp6gTpuN2nuTmXHjm5hmkiYYG1qXjmrIYDJOmCwrkZtLgoUkVYrMDa2baXLI9r0sZc2TVrYIRmW-fWqCVNeqS-ma1jKkA5jleuPgEKTNhgXksKfn4Rrzgvzz3P4aJAjqKtuWCzN9AAASc88dN6MV54T-uiHN2Mve_qyZ_DSPYmbPJDe8k6A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">معاون رئیس‌جمهور از وزیر ارتباطات بابت هیچ و پوچ قدردانی میکنه، بعدش همون وزیر از رئیس‌جمهور قدردانی میکنه، بعدترش همین بدردنخورها دسته‌جمعی از مردم قدردانی میکنن؛ اما تهش می‌بینی ۷۳ روزه که اینترنت قطع هست!
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 35.9K · <a href="https://t.me/ircfspace/2307" target="_blank">📅 08:13 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2306">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/K2KX6569S5gXrx7Wz368fThxNzJmBZ1vyP7Sd7b5yQqexaL26zdzfr8M9YJwH8_z3s81t9loq6DIN5PRbYKf3e9dHfzRktK4QZq2VwhDng02JlDktULfBjZ_xPagDrY1qtdQuRcR4pXkEaj_s0FPWyRHvug4ZIYlwPfSz-4B7Iv9MKDJ--knd-mLhQySV1zZ3gcrUL5sfTiY16yTrsl0KEgf2gNSX5nwCtYNHBZJmcc7Qlu4Mdahiw1yzlxW2Mcv1uyQ9ZwLbeNb7-5KED8zwI8elsn0E9qdhqkikuhbaFHeNdCyEeBlSf36T3cP21nGcgte76YqMPo8l6TjWrnkiQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 32.6K · <a href="https://t.me/ircfspace/2306" target="_blank">📅 16:30 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2304">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/dGGGdFpkTKs_W3J5W0ZTBIpbEYkcWl4clN5cxOLBW8XFJQHkOEnb0BNUF1oJ9HZvClCEBi__VyZwa8kMW62Wtq6myKUjL3kas5ERiW9MZBuWxs2wOr8WlWC1FshGbUaOS7gnadlTI-vekElfL-Q5O08_4dkVUtYYMdYbElq5ZaBLiG7O3wljv-Ph79Koi-lRr1-Be0JkCUKwDOqgW_YekXkBsIgTfEYU2anSRc3j3wh3usm-qCiogIHdBdmbcRgoz3Zm4SHONrzMWxhzTkdf65D6xSKHanRzxezkagspmaNxw4RMRzRs_PSoFUU4af120mevAfC-sDDm5QNwcyfYmQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 31.2K · <a href="https://t.me/ircfspace/2304" target="_blank">📅 12:30 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2303">
<div class="tg-post-header">📌 پیام #19</div>
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
<div class="tg-footer">👁️ 28.8K · <a href="https://t.me/ircfspace/2303" target="_blank">📅 12:21 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2302">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/I0b9vxLIbJF5hSja8vq-lQGkyWmkfZ-wMa7b32aSzYQnHf1wAp741lk2hdUUYhW4QwDpUqG7RuQKT9nX7UNOjIseAWvf-WwvA5wSHzN_figaOmIAbgN6YsXrDBiRgRyuIrQ6FrkkYBZB0rD8ksPaU7QJ8Rd9NUn3Vme1G2P3xd2Bv4V5IH9Wxu_c90LomDdZ7F6i5XlfCvr6vUEZMWlzb3-YPrA4Zzm3-gOYyxT5pWUqx-3VFs5tPSUO1sjfpXOc9Rn_g0bdBtuzuoDhOXlYaAyqEDO47b5Jl-Nr4KVjt4iJQ0rorSBUYDUSaWLOJqU5LrqUHmOP9xqvc3do7VbJxg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تسنیم نوشته تنگه هرمز فقط مسیر نفت و کشتی نیست؛ بخش بزرگی از اینترنت و تبادلات مالی دنیا هم از کابل‌های زیردریا رد میشه، که از اونجا عبور می‌کنن. پیشنهاد داده ایران از این مسیر پول و کنترل بیشتری بگیره؛ یعنی برای عبور کابل‌ها مجوز و هزینه تعیین بشه، شرکت‌های بزرگی مثل متا و مایکروسافت مجبور بشن تحت قوانین ایران کار کنن و تعمیر کابل‌ها هم فقط دست شرکت‌های داخلی باشه.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/ircfspace/2302" target="_blank">📅 12:17 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2301">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/jXHz9th3pwQTuxsqfkbjm9aa9_5uLoMIdW_S9Z78JLRlsKJZw4bRjeMz7RazhzztIoXc7UdiMC8q0r7_YEQVRYU6IuIjW7MOa9Y2o11bLR6sIYhSHZ7eFOyhCh4QxCz3R7bHPVLSmDDTsWPymr-MYT-xL2h0GlHj7tE-m77HOhO34_l422wTYKyJm8eId5MX7LDOB8rY1OReoefVRMWxOYnqYeBcHFFiVKFH8hBq-5peRa6hHg32FJsjZunVlXTMSYNzGp2DfufHlJ86MathI52VMxHoW4ZtOKkRlFw0RNVAYr55xMaoW21gw2viscLv2VvElOCj-K6MVWy7081gXw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نت‌بلاکس: قطع سراسری اینترنت در ایران وارد هفتادودومین روز خود شده و هیچ نشانه‌ای از بازگشت گسترده اینترنت دیده نمی‌شود.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/ircfspace/2301" target="_blank">📅 12:07 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2300">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/YY1iHMvApQtRDx9R1Bhc38ylHVCq5UKfXds_FdetClZ5hrHxdy4mhTvJmDtDqPcS2-GDFqkiAt8mxKRfPgp-fH4JVliJFjlrMqBMKlrDrCZgV7ps2Tv-6-mZuc-K9JQRL5Q5pjEJyOI1LEFVabCRdPwBXJIpsOGcrwOTJEzqdwDR6S7cL9IEiENhwMkezNG8t8zNiLZaVsTVICznPx-hT6AgX2gD42VqK7wHkjggGOCkukCHbmfjvOHTtBQfBEgUtCOIc8BsNF7buF5214fqk32vWfIhZ9FlZ_KhhZckMZPQWRzk6bPd4YgbBnNrnfCz2LM9jHRepKbMQwpMnGA_jw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 31.3K · <a href="https://t.me/ircfspace/2300" target="_blank">📅 18:57 · 19 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2299">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">افغانستان تست خدمات اینترنت 5G رو در کابل استارت زده، عراق تلگرام رو رفع فیلتر کرده؛ اما جمهوری اسلامی تا دقیقه ۹۰ درحال آزار و اذیت میلیون‌ها ایرانیه!
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 32.7K · <a href="https://t.me/ircfspace/2299" target="_blank">📅 17:52 · 19 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2298">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/d7oNChqQBYJaoTxkAb2bcCDGWNml5v7TDtqAsN7pQmLO8xSRJ3qQItd1ssmIbiL-Vtm8TVf2I887QVRl-DPwVk55zguGcKt0VBAlPEQITnx4LmDyhmjp1mEvrtdakmtEoJBJ4sl2M_9ENLGVMY4XzZ0W4lLUx_RLPPOHwLBadID5KUoXF7EzkCX96sGD2EDTANOC5n49XKgu5x7PFTuXfWGOavA8qAPQsWQbhHnNNg-SSTT6EQT2snW-RqTd31-Qh_hXUFnfzo9H2bY5EcgItizP7yPGIR9QCshQcmVfGbdfNt2yuVz75u9hB63BUsujcaDKp4e9lWWZA5vA15XtEA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 30.2K · <a href="https://t.me/ircfspace/2298" target="_blank">📅 17:48 · 19 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2297">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">جمهوری اسلامی ۷۱ روز هست که اینترنت رو به روی مردم خودش بسته!
روح‌الله مومن‌نسب (تئوریسین بارداری با ۲ گیگ اینترنت) گفته شرایط اینترنت به هیچ وجه نباید به روال گذشته برگرده.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/ircfspace/2297" target="_blank">📅 17:45 · 19 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2296">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/sGPZct0_hZipLYpST1BGEEt7t-RR4f7Szgist2Chgl93S_u9SCLpXAh5JrNRodECinB9xBFB4M0A5ID2p0y-oFvi_cH8Lhv46wdFeNKUs9csmjmKeMw0GU4mCBKHw8QCRy8pPIHsEjvxdeVC466rcKf60vqjB5Y2ZIi2qIqedcmghfLNU0jM-NUq-w_SvHgmSAQoD5laDmxsemk9y0qirZZCMl5RvoP2xUCHQNR_WJhbF8j-3wBQY4rfl-R5eojRfWRbQFnIUbQNrmdJAK5UR-1ZCXH8uptf-fOBW6QpVp1K9OjqDJ_SgHHg0TFMO4Hsy1aiVeDgI5yqttX7UbSi-w.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 34.8K · <a href="https://t.me/ircfspace/2296" target="_blank">📅 17:45 · 18 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2295">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/uhi82bSdDyaYMikzf9v2kXMpPy9KS4phV17H8AIkPi0QGMtKlKHWMcqHVp-mAI0UduO6tEKqTgn5_hCA_05Zi3YaEm7VchfU_RrW3NnOO_VPkcH_9jJETS4Xoaw4KCjONNfxppsLz7JldwKA7Q_EETBSOYbwLFy0oYSIL-Z2MY4U4fa90E5AGhfLyQJySh1puq4cToSEBNbhaoBWv6_shC-hRP7rD-pZr_67fc54g2cgRHVGHDGeOGzC_vOzWpHnvB5xfu8s7CKOh8V-8rJmK9NLdLzjQeB5GtaVXsPzfEbWHye_gThzPNBH_Br8CGc5Sjza5nqwz8zrUfEcXcfHjg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 33.1K · <a href="https://t.me/ircfspace/2295" target="_blank">📅 17:36 · 18 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2294">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/poOK5kh4pR9I_QWI6CbfrgDeQyGFZRP10oQEOxQGBnB2yB-Qntd9HiVV-PSuiep_XaV7yYLoYFZBhT8eaUqyTRO7qBuKRDP_J7EKiYRJAdlAsyBFMRsOCJ6gmNUMNFDI877nW-ZVKV-5hfLk_ngiiwEjTkQX7eq607yASHeI8lB1K_GETn_JWxHYuDuVk6z-K2dI4OVBPj8RQrAGQNMU7nAEiwShC3FeX-jhVQQwTZGjjqlnTlXKdtjAQAk-HMIyo9tr8Hs-mBC31jlBK6uAC0fXJ8gHu5mHi7RdzCEJcAP-ntie8_CW4ZSicscUfN89vmxDL-IHs6ww5zWdqMUpyQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 28.3K · <a href="https://t.me/ircfspace/2294" target="_blank">📅 17:26 · 18 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2293">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ai5H0lGtuVo0aqUuTjccWmogKzeLEwik54h0vsaalQ3us0VNWnyyZ-wu9Af79hyYignx9yOGzhAOMCF3QorjB_UIKjaj7jcyW83zj8uBDEK-ifRJFMOmT34Z2yWlJs8tQnmYcUENJZEqQeJvPzPn18gRvevW06-Q0IPXt_EM040TUrp3Qydp_S0YhRhudYhkCcIF8bgPysJhbI7V3Q-OJf2ZdeclBobjWUxsxwCugod3s7q6gSPr0LZqV0bW-UhEkkKxlbWD75ezHkCAw9xUr0cCMN1hJ1hvAC-fvwunOuFRbgqXERr4lD5959Ihu_9hlIrAvUuqCCx0yjWryeiM6Q.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 28K · <a href="https://t.me/ircfspace/2293" target="_blank">📅 17:15 · 18 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2292">
<div class="tg-post-header">📌 پیام #8</div>
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
<div class="tg-footer">👁️ 38.6K · <a href="https://t.me/ircfspace/2292" target="_blank">📅 16:29 · 18 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2291">
<div class="tg-post-header">📌 پیام #7</div>
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
<div class="tg-footer">👁️ 31.6K · <a href="https://t.me/ircfspace/2291" target="_blank">📅 16:19 · 17 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2289">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">بر اساس گزارش جاب‌ویژن با عنوان "تاثیر جنگ بر بازار کار"، محدودیت در دسترسی به ابزارهای اینترنتی موجب اختلال یا کاهش فعالیت در بخش قابل توجهی از گروه‌های شغلی وابسته به اینترنت شده و بیشترین کاهش فرصت‌های شغلی در گروه شغلی دیجیتال مارکتینگ و سئو (۸۳ درصد)، طراحی گرافیک (۸۲ درصد) و ترجمه و تولید محتوا (۷۹ درصد) ثبت شده است.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 33.3K · <a href="https://t.me/ircfspace/2289" target="_blank">📅 12:07 · 17 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2288">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/IYqHPMbeq6kEmSU7at7I-Ikuq7BOOVBDSXV7x2JdB9Wocf5TSdtyl4FR4TZEgNSjpThM2kzUVXSOO96vp68UPkv62gUwwlNcA0EqvCCACp3q3gZKlFd9M4_DBlhpuNdp0gPekQTgBBkyBesgvF1JuY4ar6jWX75nWso6aLNazfvFiFjAo_KFWzYYZxYk_chQq1K4AB6PW3EUr2ypxTEqlOC86tLJDm9__Omjaj-Du5ojQi4vxJXugYlEYi0nJxHqTTD9V1xnx2NzuDAAQSnMgvNqcIJbxxI-i-ft5FoUBYpaJo_IGPRh1OWuEo_PCCRT0dkshL7psnynlmcf93uiwA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 35.3K · <a href="https://t.me/ircfspace/2288" target="_blank">📅 12:02 · 17 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2287">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">وحید فرید، کارشناس اینترنت گفت: ما تجربه قطعی اینترنت را در دولت‌هایی داشتیم که به ظاهر حامی اینترنت بودند. خود پروژه شبکه ملی اطلاعات یک قدم به سمت ناامنی دیجیتال است. کسب‌وکاری که اینترنت می‌گیرد از نظر مردم رانتی است و روی حقوق مردم پا گذاشته. حاکمیت با قطع اینترنت به جامعه سیگنال ناامنی می‌دهد. /کارزار
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/ircfspace/2287" target="_blank">📅 11:58 · 17 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2286">
<div class="tg-post-header">📌 پیام #3</div>
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
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/PhlZ02BWVAHthPMhKtTCBRkHT_bYEQEaQQyyUloG_WS3V9aoCFbsg3P_99dMuCV5j7H2BUrfWx1QRc89Ko3vDsNBzQ8y3p8u2v9UZzcwgTcoNhmrop7Qr9NLdj7PAmY0DhrehYdYNVEYLXRplGzp7DpLGPAwEd09Azt4ss-FHgXCtbGdEBkpMZfNESzZpKN2Rt_UCgX1FKsk6DpTxSFFer8DjpM6S51uAPZdaEAixAcNIuS0nVJkh86kfVQoTmGXQOCiGH7RqsZNaxF_27ytt4jjv9eWGWa-IYUTj__5rBN1J7oWjTup80D22MYa-CCJfUrqM6CoI7feu-uLhbFEvw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 31.7K · <a href="https://t.me/ircfspace/2285" target="_blank">📅 11:26 · 17 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2284">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8fb8db45e7.mp4?token=d-m2fa2ByPWX-qoDyybSof_f8HWhjjFoNNjk2aspmtgcncvOY9VNxxkKqd0W_fYVpaQZBh7dwAisOalbLDQVJj6rKTKcrDW944yvjeV6qSzu1Chj4hpVVq5Dz6GUtuaLnXDRi49XpAzhyvCfWYk7b_qmHRwExrJPRVa4Drg33eQC6Q4bQcOaickMzKs2-U4of90YDyHpIXZXuXLGwxqT59cBLZvnAscHFi8RUYNTOQKGnR0hTRyaSBRATYd0LobmM7ZMVrWkdvWMsc2InrCf_ggQFU-q3qOTwbaGgErvikfU4Cj5r061fdGdStpvAXgOo4hM0djdKHeTrzghrhERhw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8fb8db45e7.mp4?token=d-m2fa2ByPWX-qoDyybSof_f8HWhjjFoNNjk2aspmtgcncvOY9VNxxkKqd0W_fYVpaQZBh7dwAisOalbLDQVJj6rKTKcrDW944yvjeV6qSzu1Chj4hpVVq5Dz6GUtuaLnXDRi49XpAzhyvCfWYk7b_qmHRwExrJPRVa4Drg33eQC6Q4bQcOaickMzKs2-U4of90YDyHpIXZXuXLGwxqT59cBLZvnAscHFi8RUYNTOQKGnR0hTRyaSBRATYd0LobmM7ZMVrWkdvWMsc2InrCf_ggQFU-q3qOTwbaGgErvikfU4Cj5r061fdGdStpvAXgOo4hM0djdKHeTrzghrhERhw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">طبقه اشراف و طبقه رعایا
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 31.6K · <a href="https://t.me/ircfspace/2284" target="_blank">📅 11:01 · 17 Ordibehesht 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>

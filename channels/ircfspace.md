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
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-06 05:01:38</div>
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
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/ircfspace/2390" target="_blank">📅 21:56 · 05 Khordad 1405</a></div>
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
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/ircfspace/2389" target="_blank">📅 21:31 · 05 Khordad 1405</a></div>
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
<div class="tg-footer">👁️ 30.1K · <a href="https://t.me/ircfspace/2388" target="_blank">📅 17:30 · 05 Khordad 1405</a></div>
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
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/ircfspace/2387" target="_blank">📅 17:24 · 05 Khordad 1405</a></div>
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
<div class="tg-footer">👁️ 32.1K · <a href="https://t.me/ircfspace/2386" target="_blank">📅 17:19 · 05 Khordad 1405</a></div>
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
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/ircfspace/2385" target="_blank">📅 17:12 · 05 Khordad 1405</a></div>
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
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/ircfspace/2384" target="_blank">📅 17:09 · 05 Khordad 1405</a></div>
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
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/ircfspace/2383" target="_blank">📅 14:43 · 05 Khordad 1405</a></div>
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
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/ircfspace/2382" target="_blank">📅 23:19 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2381">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/CkZL2Nxd-1o8jSu42PkWXGYQwZ7TmWJvffhPzv0cnv01FOU-s2IoBUOGnJCBfGHav1PgyXRKgSSbJU7YXan_ljfOy1WP11wfAUIcsP_dF9NIMsyDXMKNjgiPIXaZfA2d_Upenk8rWPVsPb2H0XZAkRJOIVYqKWv0wasEE1LP-FF1Ks-njL_7uCC4nRBJCP8qT2teNIu5xAuVwBzoJp4eWsbSYPyBZRdKWQrL5w6hrMVGjzNevSH-flaeQYBx-RBl7Ra8tlOvXg2JYSQQJxN13_aIHBRuKXENSWCflxv5_1_2dFMzG_eh2DJX5UTWJwG-9eeGXEC7-lPOysdlrbo2zw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نت‌بلاکس: اکنون هشتاد و هفتمین روز متوالی قطع سراسری اینترنت در ایران است؛ محدودیتی که بیش از ۲۰۶۴ ساعت ادامه داشته. این اقدام هرگونه شفافیت درباره اعدام‌ها را از بین برده و به شرایط غیرانسانی و بلاتکلیفی روزمره‌ای که منتقدان زندانی، مخالفان و حتی گردشگران بازداشت‌شده با آن روبه‌رو هستند، دامن زده است.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 28K · <a href="https://t.me/ircfspace/2381" target="_blank">📅 11:23 · 04 Khordad 1405</a></div>
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
<div class="tg-footer">👁️ 31.6K · <a href="https://t.me/ircfspace/2380" target="_blank">📅 17:16 · 03 Khordad 1405</a></div>
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
<div class="tg-footer">👁️ 30.1K · <a href="https://t.me/ircfspace/2378" target="_blank">📅 08:57 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2377">
<div class="tg-post-header">📌 پیام #88</div>
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
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/ircfspace/2377" target="_blank">📅 08:51 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2376">
<div class="tg-post-header">📌 پیام #87</div>
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
<div class="tg-footer">👁️ 28.3K · <a href="https://t.me/ircfspace/2376" target="_blank">📅 08:40 · 03 Khordad 1405</a></div>
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
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/ircfspace/2375" target="_blank">📅 08:36 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2374">
<div class="tg-post-header">📌 پیام #85</div>
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
<div class="tg-footer">👁️ 28.8K · <a href="https://t.me/ircfspace/2374" target="_blank">📅 08:38 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2373">
<div class="tg-post-header">📌 پیام #84</div>
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
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/ircfspace/2373" target="_blank">📅 08:15 · 02 Khordad 1405</a></div>
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
<div class="tg-footer">👁️ 29.3K · <a href="https://t.me/ircfspace/2372" target="_blank">📅 19:51 · 01 Khordad 1405</a></div>
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
<div class="tg-footer">👁️ 30.5K · <a href="https://t.me/ircfspace/2371" target="_blank">📅 19:45 · 01 Khordad 1405</a></div>
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
<div class="tg-footer">👁️ 36.2K · <a href="https://t.me/ircfspace/2370" target="_blank">📅 20:18 · 31 Ordibehesht 1405</a></div>
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
<div class="tg-footer">👁️ 38.9K · <a href="https://t.me/ircfspace/2369" target="_blank">📅 20:12 · 31 Ordibehesht 1405</a></div>
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
<div class="tg-footer">👁️ 33.8K · <a href="https://t.me/ircfspace/2368" target="_blank">📅 20:09 · 31 Ordibehesht 1405</a></div>
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
<div class="tg-footer">👁️ 28.8K · <a href="https://t.me/ircfspace/2367" target="_blank">📅 20:04 · 31 Ordibehesht 1405</a></div>
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
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/ircfspace/2366" target="_blank">📅 19:52 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2365">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/v9-sQ19dJCXmz_cipNKr_s2tCh8yCFDMhY1Z288_9B5azDdjmdnKEfknH7zq3hT4hk2YUHsx6iVNX11oZsIJ5gJKFt_Wiw5ONmJ3b32cVsoq4uMff6wwLNs-KRgK2_lKBqbb5-kft7OnUUxTbbwJxSpUPgzC-cdqFKhv_qy2zYHw5lVQzjMY5kK5KZ1xfHSZxp3kEQWTWejj2sAHQRxnN9oRqkNUqnXQyXDz1blRSD4JJ5feAdD4yjk0gB2PEaGiJV_jkpcMN3-Enn00_9JA45pucAYSJcOrcGInon2H_Kb3JM2olzzwJVSllaopR4J8S-ghqQ3Rb5vDRI8y5C6cKA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قوه عاقله در همراهی با سایر قوا، قطع سراسری اینترنت در ایران رو به روز هشتاد و سوم کشوند.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 29.1K · <a href="https://t.me/ircfspace/2365" target="_blank">📅 08:39 · 31 Ordibehesht 1405</a></div>
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
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/ircfspace/2364" target="_blank">📅 08:31 · 31 Ordibehesht 1405</a></div>
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
<div class="tg-footer">👁️ 30.3K · <a href="https://t.me/ircfspace/2363" target="_blank">📅 08:27 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2362">
<div class="tg-post-header">📌 پیام #73</div>
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
<div class="tg-footer">👁️ 29K · <a href="https://t.me/ircfspace/2362" target="_blank">📅 08:24 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2361">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/dR3cR5K_vcE1ll5eNpHGnJVJHbkArj8AStjsyZDKsZw7igcvtVvh0D6nk_9mp07axKkGSadbZeF9t8gQCKJ3bY1Guk1pjOhgUtznw7Yo0FmQtkAHokDBYybMrQ0zqU9E2caOjFBvnBG5KJWyJqwPSp8eh1pf_LF5XZt_sYgB_t79oPNAfiYOd6IOStFctINiNd-WZ8LG01ZeifUA65tOwMEZ9hAGxAfdzugKY4plHKI4IRIKfrPMC1_FbWG2QUKXMbId0wikHhMDEpSXXRXHXGKeOAEg9B37gjTAWBMZ4n_UeItpsU0Ab75RuHh89Bkjb32nfWzQSDRuoqMoZI-WVg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هشتاد و دومین روز از قطع سراسری اینترنت!
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 30.3K · <a href="https://t.me/ircfspace/2361" target="_blank">📅 09:00 · 30 Ordibehesht 1405</a></div>
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
<div class="tg-footer">👁️ 30.3K · <a href="https://t.me/ircfspace/2360" target="_blank">📅 08:56 · 30 Ordibehesht 1405</a></div>
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
<div class="tg-footer">👁️ 46.6K · <a href="https://t.me/ircfspace/2359" target="_blank">📅 08:59 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2358">
<div class="tg-post-header">📌 پیام #69</div>
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
<div class="tg-footer">👁️ 37K · <a href="https://t.me/ircfspace/2358" target="_blank">📅 08:50 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2357">
<div class="tg-post-header">📌 پیام #68</div>
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
<div class="tg-footer">👁️ 30K · <a href="https://t.me/ircfspace/2357" target="_blank">📅 08:38 · 29 Ordibehesht 1405</a></div>
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
<div class="tg-footer">👁️ 35.3K · <a href="https://t.me/ircfspace/2355" target="_blank">📅 20:07 · 28 Ordibehesht 1405</a></div>
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
<div class="tg-footer">👁️ 31.8K · <a href="https://t.me/ircfspace/2354" target="_blank">📅 20:05 · 28 Ordibehesht 1405</a></div>
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
<div class="tg-footer">👁️ 35.8K · <a href="https://t.me/ircfspace/2353" target="_blank">📅 16:24 · 28 Ordibehesht 1405</a></div>
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
<div class="tg-footer">👁️ 31.7K · <a href="https://t.me/ircfspace/2352" target="_blank">📅 16:21 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2351">
<div class="tg-post-header">📌 پیام #63</div>
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
<div class="tg-footer">👁️ 71.2K · <a href="https://t.me/ircfspace/2351" target="_blank">📅 10:02 · 28 Ordibehesht 1405</a></div>
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
<div class="tg-footer">👁️ 31.9K · <a href="https://t.me/ircfspace/2350" target="_blank">📅 09:21 · 28 Ordibehesht 1405</a></div>
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
<div class="tg-footer">👁️ 40.2K · <a href="https://t.me/ircfspace/2349" target="_blank">📅 21:08 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2348">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/X83VwmtMXchwHYR1pg0i-l6SU-wJM4FWk46RAP0Dli-cVguwAEaBhvnOGiq2PyuQyVh34KUWvbRbr-x5Yk4CHAmPjbe6blf-4t6aDmOGKW-N9JDK8OtGp4lxB748TCIIbQ4o77A0FPehj--reOOjoViPzsdw8MYVT7ugNQymnVaSP6vk24CNWSUOCWp8-mO1ERdbmqeHPpn6ycskMVpu8Cfo3xYaQMb_qO5JDEwyc65s6sYyUSUPkRkw0Airh4twaSwx9kGQpWwAKPy08JbP3I3LgncAejVMo7ZLe6E_gD_CuD6F3W92BnHyr60ANAI-DI18tFZSI2LEbwC9FGMaGA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 37.7K · <a href="https://t.me/ircfspace/2348" target="_blank">📅 08:49 · 27 Ordibehesht 1405</a></div>
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
<div class="tg-footer">👁️ 37.4K · <a href="https://t.me/ircfspace/2347" target="_blank">📅 08:31 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2346">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/BNR0beoK18Ivw1qCiaS8cDa1FbVRX-OksCtix8pDseMS08QLn68rZ__uOP2qosVgxL_8IeNjrpbfHfbp6OVwj-xHdIcAQgNOm_maE5U3DuNS44itEBvlmkTA8ROFWeu4xpj7KufGDh6ImKKaKk5HXH_xMHLiC5RV-4fJGvTNxd2LHNKSgFXtx5a1u89Lvn-G4qlzjk2agMSP-KHUhxwHt-60ZILEecpeDfeAsEWzTtPOpH5f67yYYxH1uD1tNajYsCJYJ4Epkj_cXtyP_5t8S7O2hVTpFDZbuTVYSgyvjekcuHIxYaZNKm3QcQQphLggytnIpK0Awt8_R9TqYoxENQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 39.2K · <a href="https://t.me/ircfspace/2346" target="_blank">📅 23:40 · 26 Ordibehesht 1405</a></div>
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
<div class="tg-footer">👁️ 39.9K · <a href="https://t.me/ircfspace/2345" target="_blank">📅 23:28 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2344">
<div class="tg-post-header">📌 پیام #56</div>
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
<div class="tg-footer">👁️ 43.5K · <a href="https://t.me/ircfspace/2344" target="_blank">📅 09:21 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2343">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Cy7vp3f7DmWCJd5_ugV8CKZKflJiRg991MdW8Jv7GXFiDyqYeBbl5h8H3pSc58jVu_XPxMNcVg42uQJwsoW0mfS6G-5u1UvKfQ6kpwHX0Q2k84hRYFYr5DFUyy3sluR1HIXqHFky8eXlS6LodoTQ5NLdfftaNS5ldGNkEVkT_JO7h9cUYw2qW8EchZM-dK9l6ywoWFSAuP0EhRRsDbMvVnTT1U2r74G7_VaucJ6NCqA2Vk-GUWYteyZIGrIT60bnBPW5Mf91tiwjriwCFWAdSqxjEZcxJzviC3mOfPZ3XgrwZuyUOYYXE7L70YPWoF0PjBf5vETsJu2KympkXUFEzg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 37.9K · <a href="https://t.me/ircfspace/2343" target="_blank">📅 09:11 · 26 Ordibehesht 1405</a></div>
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
<div class="tg-footer">👁️ 32.9K · <a href="https://t.me/ircfspace/2342" target="_blank">📅 09:03 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2341">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/fnXljceQqCP_9N2fQR9jn4kCQmklKgGW70dKT_wormP9djkO7zFyXU6nd_03P4i0A37LKhPHhcJYBqIy_-_kik6BZcP3OHRWT7cmzahqKEgrWL-NuHxFejxVaBSd7At5PLVSJVDqD2bOLHsFsetuMREEpYj7cZ7TEN2zpw1KB9BJKME8R-MKkvFbeyRKJMFx4XZV6F4XEV5GHd-zXl2Nnhw8adR-dqBwEGUSkdZjIXWIX2gRLeZFRCbWYbKEHS6fh2HG-5bcMUrb6Om6N1vDUApaD6wotHnP9cFN3pF1L_0VVMG6dhUrtrR07HZeTHBtcTSyNHTNiQbMCxjwWiy_OA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 30.7K · <a href="https://t.me/ircfspace/2341" target="_blank">📅 08:44 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2340">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/MwFeNm-woOjSA3_TidkG5s0EFPR9Lh_QUEcx-tfE-clxU0XZwEHle8Uw8_ddfRgb-7ZWpLgj8gRav0wWyR1cgAWRgeRiY4dIzbSUSJxAunA1MKNqYlSyg3GP4dl8-pl4jit8V39dxu01gaFgs5u_AsUuWpI5c-McyzyQiCMb09deyVPGGkjkJgsCJ_u46PBhqXvyq6QrWWi7qP96NfXa5uzdGjDW-gG7kN8x2drEYeCdnP2XqJW9uIAxPYKYjEknhYQXmnnwST0FDCRft_EPpC-tGvB_T3agkUahXCuipgPxJrh2xsEvuW3w9OY4PoNoygiHZofGjNBbB4OjZzDxJA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در هفتاد و هشتمین روز از قطع سراسری اینترنت، از جدیدترین روش ترکیبی عبور از فیلترینگ با ذکر "لعنت بر جمهوری اسلامی" رونمایی شد.
😁
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/ircfspace/2340" target="_blank">📅 08:38 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2339">
<div class="tg-post-header">📌 پیام #51</div>
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
<div class="tg-footer">👁️ 28.7K · <a href="https://t.me/ircfspace/2339" target="_blank">📅 08:28 · 26 Ordibehesht 1405</a></div>
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
<div class="tg-footer">👁️ 28.9K · <a href="https://t.me/ircfspace/2338" target="_blank">📅 08:27 · 26 Ordibehesht 1405</a></div>
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
<div class="tg-footer">👁️ 29.5K · <a href="https://t.me/ircfspace/2337" target="_blank">📅 08:25 · 26 Ordibehesht 1405</a></div>
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
<div class="tg-footer">👁️ 30.9K · <a href="https://t.me/ircfspace/2336" target="_blank">📅 08:25 · 26 Ordibehesht 1405</a></div>
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
<div class="tg-footer">👁️ 50.8K · <a href="https://t.me/ircfspace/2335" target="_blank">📅 16:26 · 24 Ordibehesht 1405</a></div>
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
<div class="tg-footer">👁️ 40.6K · <a href="https://t.me/ircfspace/2334" target="_blank">📅 16:18 · 24 Ordibehesht 1405</a></div>
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
<div class="tg-footer">👁️ 36.5K · <a href="https://t.me/ircfspace/2333" target="_blank">📅 09:19 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2332">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/WIi3U_-vTj7ZzXa3f0OVWxfrTZbFn2q4wfOPX75wh5XT2ac1aQbAeNdwjQ9lndnAOEWLDlQYafh1RQ4OoT-pAezBEy7us5wYS37KfYEjBdfxHQ-r7fx9D9siCOz5VL6SkvErE5LnXs5s3SIqOpSnMg3e7altp9rv_uhO8wH-lDgcrxpXmtjxxupdC543LeDA3ZpCQgoLwPQZwiu5iZraZWy6-Yo2n56ryL8Mc1iZeZDcXcb7VRkKioFzSj5rQAvmmukUlgeCRoPOSscKJKut2ZjSKkWx803JHlrcEMmR5UIdNYVcm1NAkeTD8pNdpesoamYHyWJvhO1zy4oRxoPToQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سخنگوی کمیسیون فرهنگی مجلس: امروز پیامرسان‌های داخلی گوی رقابت را از پیامرسان‌های خارجی گرفتند.
🤡
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 36.7K · <a href="https://t.me/ircfspace/2332" target="_blank">📅 19:39 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2331">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/mAlS1hzg0q8dr5arH-ykQFM5otpwCSar7cAYl4ytIzPt7gEAXjPHqKo_ohFZjlJ9RZLMtufKLuyguGe12vV_CqRLpAIogS8RW1xFZb2VgyeFbY_tF8sd1371-qpeB6Rhrr7-ZXz6aSx0xLK175VipWcKmCK6Hwui76b4bm4pLAyyClxKYAUyIbLRqjjrY8inj4VYNvJL94QO51R0rOQxjfNWq99QH94n9meEWASzRsRcpR41YrzgERTOYY7dtdi6FyWUmz3dHMLhX7aNVQKLpTpxO1NMo727esmAc3rX3DO3ZHYs4uBWF44XD6YKbJ_aUr9DmKDgfuXq4vx6HcMKpg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/OBgjjZ3fLdDXvS8nhjPotQoqPWCbovazu0h3KaIqNXq2iYR74ZUvPaQGmPzrVO0Kt4kJJEKUVVnuxZCy_TPx71Ki86S3ZIFZ5MclPMEkWyqx2wJHhcsCiEbBaulcQB_JwnqLtp4rdZ9rR7wSCHDvY7iVq8jVvI-7b7IraaqCMq_S1ZxDsKgqQy8w0FPzy031y1zFVP2oTrCLGgTvgi7kOdVLyZi0jAmEsnerdsDszHcL9amVbJpxq-XiInmcWdcOHusn-09BYUdnqIjegSZXu-3skNriMwWtTOl7pW9ZH7c1VWMeeh7NyZmoliNb33KPurpXsY6t-haf-zFtiGvGVg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/ircfspace/2329" target="_blank">📅 19:30 · 23 Ordibehesht 1405</a></div>
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
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/ircfspace/2328" target="_blank">📅 19:27 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2327">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d9e9b1e831.mp4?token=YW2ZJ08QSqJ1TjEMf8PW4_qujdC0mlJHN_yFCRG9QnGmnC6r4eMnQq216TMautBO4HNOXj5Y2HdL1uTeAqUZp3jlJBCw2qokqdJTydf2TYQjc9AFfsDQtLZZt0K9xeYq36MwDvkaK_lIEupce5yJ0TbonRqU3m4r56g6gJst3C016Yes9JoY6YFHHbdOr-duIct4NgAbhuZPQ6JDt4vSM3LBiLl7cXiQ4VIGzdbk53TALTgJP-i6ZocY4ST9DNZngFICi1CrP6Ikejq2QGUOfKsN-SUjTE3IqG56_tyZlDQU70YNhMlIeIu9sXIk9HDj8rLQ60pbaT6v649_js4qHw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d9e9b1e831.mp4?token=YW2ZJ08QSqJ1TjEMf8PW4_qujdC0mlJHN_yFCRG9QnGmnC6r4eMnQq216TMautBO4HNOXj5Y2HdL1uTeAqUZp3jlJBCw2qokqdJTydf2TYQjc9AFfsDQtLZZt0K9xeYq36MwDvkaK_lIEupce5yJ0TbonRqU3m4r56g6gJst3C016Yes9JoY6YFHHbdOr-duIct4NgAbhuZPQ6JDt4vSM3LBiLl7cXiQ4VIGzdbk53TALTgJP-i6ZocY4ST9DNZngFICi1CrP6Ikejq2QGUOfKsN-SUjTE3IqG56_tyZlDQU70YNhMlIeIu9sXIk9HDj8rLQ60pbaT6v649_js4qHw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 28.4K · <a href="https://t.me/ircfspace/2327" target="_blank">📅 19:25 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2326">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/dzOkJnnr52woNQxigc9TYp93UvNZW_uyW-YPYuYonw40uKCy578oIK1GTcW8IYgDk5_wUDj2krQSI_yRpkoEnGa7R5QCDhdG3wLTxHF72uc3p6rG-y4Su-B7kPBsfAoVBF7Cphsk6G4qBsPjscc8Phyv63NOBPIgQjg3Z1eVWjWd7_MI3l20LuKoTHcgGOSVX6vRX_BSUIi6dOEEimA_8x-192vrx40GYtlfwknGPA0ab0d8azNkdYHO_Q9T9dDuaOLnJr3QqG-1y1S5vv6Wcw-Mjlc7_pbaFYzpWRuRHcCMNVVhfzk1ofLlxrhcYYlltghPig8zUtzT8du5uveKRA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/X1V1lwBJPX8rqGpuKBE0tGX2joFUwNksOOGJdphz7wofYKsFjwmGzNIQFnLm4BEa4ORcbHPAXHIZquXR1RYcaSbyq0n748VCxkBvwXduAM9wObvCcRHh8pEN_l5tzthKULFOxrBIbn5EPfPCXT1fqXAZnnMqmrNT2meK_3WNkhXnjnDlNrwSSZbfYcETLpffRV6fE8eeZbEt_xHqbKskfrK-s47ui8-p_qDtXSSDTdW8Jd8pkRmSsueb64gL3xB4nOOpLn8YS33wzrLIfpLWtZJnpSwQSMGiAQg2Uh793U3EDRwGvyMy-TSzfkZTjlh3aIKUx2FNjtUObNrYaDkmwA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فعلا دسترسی آزاد به اینترنت در متن سخنرانی‌های رییس‌جمهور و هیات دولت برقرار شده!
🤡
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 30.5K · <a href="https://t.me/ircfspace/2324" target="_blank">📅 10:54 · 23 Ordibehesht 1405</a></div>
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
<div class="tg-footer">👁️ 36.7K · <a href="https://t.me/ircfspace/2323" target="_blank">📅 08:55 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2322">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/W6XxDupdz57VcnHZMbPjvJzsKB3vhwClf-Pw2-62BMXzpZzhNULloy030tmM5l0pv2MCOcuqGp-rk3Q_tZ_O7fVRigFPbgsJxiqicTNuOU1ikEeq217cH9aUxh4__hn-mFbUzeYys3LZbQSp2fo9_b27vtwBQm0gJd5DfOEyxzkdRMZ23OPH7ztGBNtWSSTlPWZII6Lrtyjpg8aRj_qFO3vLjw6VpeZUWCR1MD3BdSGT1B-iHCqwwajo_aFpBs2Xkl6YOQopx8Z_W2R8oKPFU1s8WG_8b_Pqt2UD3QJEhF1TufrYgmjwoTWhpN4q5LPgmN8K2TUfCdESEsh9WpfVdA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 32.5K · <a href="https://t.me/ircfspace/2322" target="_blank">📅 08:47 · 23 Ordibehesht 1405</a></div>
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
<div class="tg-footer">👁️ 28.9K · <a href="https://t.me/ircfspace/2321" target="_blank">📅 08:38 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2320">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/V1TZfcpWLYYLDr8r04SG54nR9PvgrWRZ1XldSZJyp1I85g-56IaJbldE9ypBddCDi7C1g2WvEZBMOfnhB7409mYYCdegskKREJcAPzaQN3byZNfKs07CZM5RHeNPM5Ke-3Lr1ojl_581x7GatmGyhGJobOD06vBre7ubItrW-r9NdxS0T1ensOSDbLo3qEabiZYtITbUhSmqN34VraAzKKmNIv2VPPF-FGVMaxTOTUmUBFcfetCfObkBUOttnfgUQotyD84losakOQCuYmMNvn2jtJ0QWOnIPva4vSjCd4aATrhWsDn9yieKEifEF-MhWz3ynW3V_z_SFJiE4k_Mlg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ZbtEngcuwY5A-U0G9IEn7Xg7z9gtJeIOz-_jeWkXGXMkwIdufmkTnmJR8OyW_R4XmRoWXRpjqFfEY4w0vY2qwyptYqS7R8xV5UprQZVHHqgC6BaZNIPahFtEtUU8GhBalz5Hf1OB6J-a4mVdSyySUuufk7a-NlHzwZay-hR0Z47TLpSDvod0RMmhdFBDoKDsXJTcAB7WvY_oRzSU5Djyi-Bea4TLWHv2Lc_Va7c9h7OQSrNe79anJKBSzPzHiny0_vFlWOIpktPtbpngETPKKC7egDJXqrZJnKRXqQoSm9hYYyKKu-J73V0b9k2kAqQOqLwL_I04qIJ7G7Kr967U6Q.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/V1CLI271_BPFGLzrv2MpZxM5xl9_QebawMoD9O5A6fYE-PG3jxKZ0OydK5Sa5P9iXhOxnx7reMXvR1TVHbYuVy98xYhjUB7CWvo2M48vKf6SvtggqWoFFCimtPrwQ0t8rh82UD13ujU4FnxmEu0BQLeSCvFi8knxtI211wtYdDT8TKfTSai88ehEY-PB34t8qRmp9ZC6goZ5SttTaInHbJO6LLczV8xEZa1DEejha3f7h0UWZ6B40Lrb5KkUYNkzgiiPrD0BroI6BfXbj7XzKjvHpxlWvWj99P_Dbp98nmaDzmqTc17mLX8NpmT5oj1PrwtplgpyukFp4TgWwpwEeg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 34.1K · <a href="https://t.me/ircfspace/2318" target="_blank">📅 16:35 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2316">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/JtkFXT7Iw5iPTNb-3sHS2U-AQ2Tqm6mDL373s4ZSlrG26D8qwcThPwhxaEBhtXpIZvaFezkzMWcc8u_x5wbqZYrl4hko0yVkA26i_QeEq80udyvdM4W3hemi4yn3LYpXpbpoX7NM6QL4futhoKTXIjcFdY6K2cO-V_XB8M9jc56fXHw0UmRpzBOb1u3BBl78ydLmSWHrxKi4dQ9Egflw0jpc-_ZVsyoJ7P74IjtUbuasjAAUDVxrb_7e_mCqibHbZ7IODcp8wTcwnhoS-2H2kO7EOqlYDmA4gX9nvfCMUXIvPy5Anys2UJG_Mqd2SDDOp3jhLs0kMea7J3WrAQEYNw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 40.4K · <a href="https://t.me/ircfspace/2316" target="_blank">📅 10:26 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2315">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ESAX_2VO-OlaCYWd-TnS9NtisXqH7WS9umC3-pRdLk7dFA3mawGVwQSlDEOo4jYdOKsbZeJYu08VsAcJbGGCS6u-bC94OhnSi_LnoDzhBSZfmSnzul-qmHO1eP5dGBgLGFG79w1HhV7vSh_-WLQyJ67cJyT1bszfPCB-kUqlTtMUHTJYjJ0mwwZg2ckmMClPJ6fGIg9VAcM6g3hszUvWitouYSrOJ27JRPNeedSzrmcQd8KjyGCfDkCZVQCxgIZIk2XssGBGFD9eCoH5LU-9fQx99P9fJf6wRVmXARdjteFHvZ2rHGuYSLFkDJLnkvtQ3GvE6JMV63jRVRHka9lr9Q.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/TBn5XuqbompjLDhJxn5MmAzujBEpPn4OVviV1tcSraMtuRmnadHzfDVPWiKO_J2rGucNjxY3QiOQhBhxabbgHwhtnWBtcmqxNndYkvZmOvvdtOM-FLEHwA3eWrYbvQuvjbyO8KBcr5JQ5lQztgcnLYlGHOJHsxz2YFKVjWE0hdupOQqtRDI2LWBYbyBU9ebO5aC9veBsbZWZmcU0gA1iOphNJA3Y_v0cnYCn-lbb4Yc-oiLh0B2RzGid-3Kh1w2P8Hmx2Z7ESumnrVUpfv6TeRlSN75yjIHQv4CwYZI51KJZMEWEe9k1CLn1SM8vRh29p9Nw6AySg2Cd6XnS1IiNdg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در ادامه روندی که نشان می‌دهد تصمیم‌گیری درباره اینترنت و سطح دسترسی کاربران عملاً از دولت خارج شده، وزیر بهداشت برای رفع محدودیت دسترسی به پایگاه علمی «پاب‌مد» مستقیماً به رئیس مرکز ملی فضای مجازی نامه نوشت؛ اقدامی که بار دیگر نقش کمرنگ وزارت ارتباطات در سیاست‌گذاری اینترنت را پررنگ کرده است. /شرق
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/ircfspace/2314" target="_blank">📅 08:46 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2312">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/tJWt5Twoq-vAu2c2H6C5eMbyMEKYlBef7E-J5O_MCYWZTj7JcWf6gUvOOIg91byRYud3us6Gkzh_o_n5zcUjoy--ITmUpVPdDMLJTtAxV6SvpM5gHvUKzsO4Sl0PZt4TV0NPD73GHxK_iWIuVJNHhlBhmKjeWgqonInrMRIwrQZreMOwdbv-5uSoYaEliSxnvOhDUH6_uvO2l1rglFvNuSdZKTCE68QgA1hFtYLyY0LOfh625mofHgtlIuT8VJZnbxBI05r6UkajKYFNJSPY8xsFz_2jQk5HHu3pss6OlpfjrGfr4W1ABztrmWm_gyi74WP1xyt83X6hW78bLkhOeA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/ircfspace/2312" target="_blank">📅 08:37 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2311">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Lc-5fcadnU7qmCBwcSPNtycXsywT_LGLODxuYd4YqNmXD_KRi8BaaZ0UHjXrf7c65xRiMMYJYjNE4bC1jcswsk0GasH-hlfSeDygS9CP-XmF7HGkqLEh48nrNCbim58CTsi487yCZFVbiXkzfXrvU-d7yW11GnSVZwB5KJueY_HCdNpzRgVl67oGC95E5muacIqhkyN1WliqUJGk9vwLXSRQPz6svHz_Br30zpQ5sT1TbdGWumzYEb-9iqNeTdsOjtdunnVmpsB5mUPjsTgH6E8PsPizOsYfbwbqXlrZLuoJWDGLVB3acfbVfWp7vDdC_oXxkWl9YGs54VLdhKNTeg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/sZIPfxaAIMZUSydeg2kMX3IrmvDwbxVtVX02BpcqCYoKeuZj48FN3R3qwLK0shaOcVEDeNnUlfV_-xtbJBmtU0Om_Lg98mIMqXMBNMmJrr7zOyTH0HMGGJUBwcGu0o6ZOMG1V0kV_ZoCETQwDgKEH8qpmeJKt2-r2vkmPPiUAxnCkZcuO8v0iiPvCAZez1KhZSwWer3RBJZf3zNC7qAD8P6LS3o_mQcKB-H4QpyrD7sAet6DOwF7eBZ63G_cx25aBOV7GK-ea95BNVoo_YoJH_4h3aJC5wSk1w_82QMFH1Of_JXX3Ff5Ge4OiuUvBu7IQ4P-cAxjiySRbL_avcOQIg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 30K · <a href="https://t.me/ircfspace/2310" target="_blank">📅 21:28 · 21 Ordibehesht 1405</a></div>
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
<div class="tg-footer">👁️ 31.3K · <a href="https://t.me/ircfspace/2308" target="_blank">📅 11:45 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2307">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/pyw_O-dtZaBufLsBy5HX-M-lO85Y39MDDNf6t4T-HNEKTc_JBuBDzq73RzK4enWby2hDny9UXi-Tr9vkq0cwOhcOe3S_bAKbNRvk7DX2YvsJH2mWTTYRUMszkabITPToKwGeaTxZzEhD7XlMQ1xtXpz784_mqY9nyEUiQ61Ek2QUFJIE4CFfj8fx08fFyk-V9HmFEsfsx_deLXJFByqHwDJNnbAyBheL1GGzezKCNxsLWtFGsGCTWCkBacWYqdqxl0IyVmJ18I_bYGlwo5IcsNwyKnBbCUG7ixCVmT5TNSeHmWmUwH1zz_eMqOXgjdn4mPYfx05a43mUwNKt74CAIw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">معاون رئیس‌جمهور از وزیر ارتباطات بابت هیچ و پوچ قدردانی میکنه، بعدش همون وزیر از رئیس‌جمهور قدردانی میکنه، بعدترش همین بدردنخورها دسته‌جمعی از مردم قدردانی میکنن؛ اما تهش می‌بینی ۷۳ روزه که اینترنت قطع هست!
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 35.5K · <a href="https://t.me/ircfspace/2307" target="_blank">📅 08:13 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2306">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ITmJyb3R4SfgoQkXS8gvidYphMWSaDC4iubYKYM3wb9mvV8gWikrmdu3POKE2_cj1n2zDvL9XOv3bzLc0GCduO-vk0ZT9epkg2ulICpNDTdqNNGE7lyeexNTsxfqpQAQQEr4JWA1BK6gxvYUQiGpaerF5J0dS4lHctsap_LZXCsxhyBG0YZ7rCkFd4qlYuQM7s1FQVhQ2ahJzSvTfuYf3NqMfYlxIivb8ltUWZ_8_twj35rJdWCKpQ-ghzzmSpzJf1b5-j5eW3DdZuI5bHnXy5PsewIhCUpkO2d_Dko2zTD1PBhpwmJGLmrQoUHD7r1uoJ0KKRlr994PXRXn1GLbtA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 32.5K · <a href="https://t.me/ircfspace/2306" target="_blank">📅 16:30 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2304">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/QVDshC97f_751n3hugyKy9NQb8TwaN0n89byUa7-plwagmq_U0m8hzl4Wodj52jv-c-vgSNz3qR9Z8d-nIPjZ9EwaTw5mhC6JGblybsqmezCENqTgKBNDeCQP-osBGi-WCSKhlitja8CXVIpvCSXfiO_1eL6FTSWzs5qpPbXKzcqbJgGvf56iyCK0cyI2sUF31sZuYkt5EH1yhJtbkJG7VT4kEM8lWOC2H4p00jTzdvPbpr_A9UjFT4d5M0YakU3wHEsMj60yh1pMJd-_jfcfJtfEjHEBqgvD0IE2p0HkpO3J17V9dYthgSuEzs53aO0Qa7GAllH4k71dh50KleSBQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 31.1K · <a href="https://t.me/ircfspace/2304" target="_blank">📅 12:30 · 20 Ordibehesht 1405</a></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/KX_HFDaExCvSMVJWhgyMN9NTMfuCg2KZdqRUWIXL04xLtkcMB7EWqZSD3wED8jNHJRjvsMj9fgB7kY4RQmA3LrCCberZP3_Jy_W8b330RFpoAW2suSzBozeeMl2Jb3GFF3S8AlbZ0phCs-COiY0DsboblJsV3Xlahiy5p5hsXADu6ypGaznTzN4w6mDlOcUzUVvZbpcGgbXa09VCVSSjsd3cOkKljtli5qLPTtO6OLVIfvdZA_Y8Wnhe51oLSLEsmjgsJvokaZzqZRO4vpisgE-G2CVPdbeCdlgUqxEOwV3j9y9OnbHWtcbtqY-GFPCJEWeit_ZT9wZwX3HJ8LhfPw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/dQDyZNWojD8YGGhNzuDsQg-xH6eMXAnOaDjudaIAkRtqYBrAHhch70BUL-yF9_VfWu4tiUktZ9duUiTUkb8Ov-PWpW6Y5oGIjW14a8A_J57jstvZb0PlLzN1D6XgjfpgW02nmOCA2FR7rjvTf7l2O1ar_8-el0YDcxXMssMI0Cznssx-i4mSy82pbOwYT6dcFL8dXYGT-6NLXd-BdbEtD9OUziqTli4Ey_fU4zKarTy3OTXHLahovZFDu2S_qL35tubJRGoMUmMw_JGmZQA3NhYhJB00KQ3UUNK1dPTLTVAbL1P0nG3VBukjeiPHBsBvTy3hqVO3bgYCDc1AtwIjWQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Tvnhn5XVqvZvajQPV0W36127j_a5J1-13r6GyhUAP5UN9StLlF8L-xCyC26h30U-BRubkZumRT0wTMeYKLUbifR8qw9lNI9gEKmADrzcx7VA0IU4MgO6tn9OTn9JRp2olWqJFIu2Rd8gZwThqMgfmiXisNgQ6403eao76JIhMPKB2Hk6yUQMixwLAYEizS3kYyCWxY5h4_dKM-vyASBV8l_lauVBUW2nGUJ61Q68T3AxBdkBDI5DBofk-c701s-kDjZC0WeZfL3JX_ay6HlWw6UI6jXgBE3266nQ_ur6jeUCgApgRyYUG9bp5pfJbK3JzfsLCVOdqZZNyCrhA7fNDw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 31.2K · <a href="https://t.me/ircfspace/2300" target="_blank">📅 18:57 · 19 Ordibehesht 1405</a></div>
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
<div class="tg-footer">👁️ 32.6K · <a href="https://t.me/ircfspace/2299" target="_blank">📅 17:52 · 19 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2298">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/pDRnIv6Z_lEshsnj_nXVSpRrnygs-skDHAQ7q28rtrJhfO5_NdYydOEjQP3gpG_soaqXinbI_190mpTw_tQimJVDDdUn7OvYPgMK78-E-yj1ASvAd2dg6uBOo4YfX2YEo7LKt7kBpwS7f82CHLEcRqPk0saF2AIBmMG8hLtRt3C17kHobijvwY7z7SZkt7ueJwDQUyU6dmTqg6fqt8dx847jhlWREsybIGavSqwD4MWQ852ypq_GSG2vBRD9b4u6g69lTr1BemkWqY4DB7MRHJFjcdhusWu7h5sEcD4FY5bv9p3F8CzvnyA48yaH0_5PrkYap-R40uskp0dLu-lTPw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 30.1K · <a href="https://t.me/ircfspace/2298" target="_blank">📅 17:48 · 19 Ordibehesht 1405</a></div>
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
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/ircfspace/2297" target="_blank">📅 17:45 · 19 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2296">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/me5jQxw3zz5yDUNJVrG6U2vX945gXIYfB9hHTyIMUso6qnppi_04R_wQNVhrCErVel4dlS5JMA9mZV6SZJEa9u7-fyGKyb2GFl3Z05MRM2DMo4SuzE0hr7SPMAAV6617uzZxu5tEPk5h0BIm703DLk9-W1jF8dLrPn5BoGCpmqspWFa8vfseQxoxnuB3LDniiqxay3iVY8O52hPKdvSqfvZseqZ3an7XiiR2n1o8wXVPtTMWTX-A6QB246PV4AGZwmPPCvg0r1cxN7KgYgQ0P8VqY_gZ7Gkb0ABOZkE2HRhh_siaIJcxvwHhixhjmTtr3VgfYKvyCWGNEAjKX6EOaA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/NAyc6dAJIAusL9eyh90Va2o_HqAR73NmsPydwZv9jgmc4h-15ug6VLx4UKcADAUijvmt-5xCTHh7nKDAsmqBGx38za0_TLb9fkIPycFQXX_i9LBhqMiF-yCcoTFttQyf6fXiOMjssOusCiV9C6G0ZfI55esn3UKKrm1u4YQnUvZ1vl-S_To6gbbHhfhGcLZnHVK-iF4x-asKmbPuNTQtq8lZY47gHhJcpsYYj_jyjbNMP4l603AGtJyyG358LvMa2MApoZs7z4r3Py2IoFPoUUruwb_0a5TNVFH235kom6xqtjCEyB9u1U6OPuffDKgScL7chHmkR5QK_YI61iW5jQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 33K · <a href="https://t.me/ircfspace/2295" target="_blank">📅 17:36 · 18 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2294">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/pmjrau3CFIxKkmAEJ4BVmBypU2nTEhAUCWOzoLhX42tD0LkMIWm5BmxwgoUmeLNvZVjzEkAhS8nGAHQGibMK6rWZix3cu3CtSjlMYCKXM9zVmsmIIQh8z6LAuao0VOBHkKVKWtJa12qA9vByW0Nbod9KxGU_7mMSdImkZ7QVC9RRRdGYUpffnh3v-yuEOX5MQ-zEGGmtueFfiyoXXkAWAkU7P4r-r1_0zdFel24w1_toYZB2sUJeV2JG9qUpfKzv-TWDBVnWx_2JkpIw8lkd375s9eBm4yX5xu1v69EhsvTLyzPpVYsitBC3qvSOSdZ8B1tLDV2OCQpMbUrRtALtZg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 28.2K · <a href="https://t.me/ircfspace/2294" target="_blank">📅 17:26 · 18 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2293">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ABUc64BrmUV95UlewawwkXHzCg8sVGj1YjXvyZkZA7prMqixyJ4H_FDK-GD5bOYl-VwLvzB056CO5yqtn0Jd5sXVjwysELSL3JtHvIcrdLhZJlWOGUFkcw5O9DID-I39y2nU54m0QDIK9KCLzYn4zA0RhOh5dbhMCwoeR8C64gTAAcPBFQpg3Prpyr5MC-xzxCYnTIL0Mu3_H1Vq6uklVEHlGyhwPnD70okJwF3lo5VYNjrjlYO6S6p14hkxkF4x9WJXyhbDmIy1wHFPgNQuqBQoGcnhkaMMs7Zc11Qd1aWmvohbnKFW3O4P8dDztoOpk8zPZNq82Az1eowLx-Svwg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 38K · <a href="https://t.me/ircfspace/2292" target="_blank">📅 16:29 · 18 Ordibehesht 1405</a></div>
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
<div class="tg-footer">👁️ 31.5K · <a href="https://t.me/ircfspace/2291" target="_blank">📅 16:19 · 17 Ordibehesht 1405</a></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/VvcQTS021Crmahc0-379Ms1B1VD9I56DP1ue2JlhOkQ0bwCnZFf8y2DF5wVNxHjshiGqU_LJeHp5pWpVK7VtCBSHBvN-HzTVIFGap8bBhlU2-MKFHZvZYm542YU_FmY5i-KLoRrwKSfW2nr_aziMD0EaxUOYLdU3qEnXZVOYCcJIorVfByQlwUaJuOLgES2QIItKasTIgkwfxdPmZgGtzQkhIiV3wIH3SYKG-hO0Kkd4KOrxGtAIV3BrSvvpcx2ZrxvA_VWUiPIqm0ZCz5MeOYvnDZeXa-kWpAO_CFiSMVzzZYIOM2Lu0L8XWn8l2SsHHTHvQMzkphHTn3kbBrSnQw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/lT5bMYkL8-Ku5iaMZP3cLKB_0qUaDRa1VGbvMzJcjuCJF5UTH8KahmFlXpud0Ms5GkyfhUBzlLvCYFQ2SBwgVehp7btj_yha-Gb_MR6RfK1LQu74Gy-05lrSGAfJSEL2KR-8vdE7MqCjIZUqnl2J5A6fjaDsiZo3OqjmzO0wWig5EUUrakAPeX-sAyneE29OXm7uKXENnFRs_zerv9REALUZrAP2pnnGSg2gcZ7-dykLgqLIIkJ-nifq9YLrN_OoZWTLAucwZMaYFKV5Now7FZ8qDC-6PxAYfo620tZowJaFxReThA3MN2b0hRPUL7jhX0C71t4tRLdHV2H5_bIhbg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 31.5K · <a href="https://t.me/ircfspace/2285" target="_blank">📅 11:26 · 17 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2284">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8fb8db45e7.mp4?token=r4odUdahAyNcCWf6dRehdAyD10aCZGU8gAkthClia8KLZ63iKwKnQL2kuqRzwmEh2qommK_HQtDY5kSDZApvhgGc-gYUeEZowz3tUGtQlkcZzwZiDjp2zI1O8jNlVTfg2PBquMMOgFWFtFrwtHOhVv-C_jFxbkAKAeZ0NrDcEh3nSdUXMOVCgR7syBDjXBw0Rh34sn75pYmbQwdY31AUsTmNBEuGJJdzpiED5ugtJ5e8xwIkZhib5gd8fx_3mmaYcmrQeeeob_ngg_1XdWtXLkgQ9iWT_yfTt9iJatocwPMTYxJIvDlwXpr5LQ54aXZwsuumt8624YCbjFjpsNBBDA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8fb8db45e7.mp4?token=r4odUdahAyNcCWf6dRehdAyD10aCZGU8gAkthClia8KLZ63iKwKnQL2kuqRzwmEh2qommK_HQtDY5kSDZApvhgGc-gYUeEZowz3tUGtQlkcZzwZiDjp2zI1O8jNlVTfg2PBquMMOgFWFtFrwtHOhVv-C_jFxbkAKAeZ0NrDcEh3nSdUXMOVCgR7syBDjXBw0Rh34sn75pYmbQwdY31AUsTmNBEuGJJdzpiED5ugtJ5e8xwIkZhib5gd8fx_3mmaYcmrQeeeob_ngg_1XdWtXLkgQ9iWT_yfTt9iJatocwPMTYxJIvDlwXpr5LQ54aXZwsuumt8624YCbjFjpsNBBDA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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

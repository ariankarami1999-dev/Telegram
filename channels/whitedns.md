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
<img src="https://cdn4.telesco.pe/file/FD-znG9gFERL6JvNq7er2Dj-TlHyNGYOmW99a0S7mNM1s1QEAEDIgvWK4pp8pbUkARhoPRKp4ab2VJH393-dswirss1ArlSC6kpz82Pe7OEdAFDzRNvxvHsYkMpTxeiBTQiyWGIBuZ3Yqg5lOCfUrRDNZnnU3z4A7qbUwPZcAgHlYSWjExuOa8Du4Ci-j0H4KXmQDRAQYFx5_JplYoB9DcAbqfnwnLuzTrF6HHxu8jnBB96ZFcmuf_seCtqHqwqMT7dBoRNoJo_DCnNTPevvx3qasdKu_uROKwThmFLvsQXQIzkrueDvekwPZYw03M1Qe-ZPByPZ6jGTpEB_ka3z2w.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 White DNS</h1>
<p>@whitedns • 👥 108K عضو</p>
<a href="https://t.me/whitedns" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 گروه :t.me/whitedns_groupادمين :@WhiteDnsChatBot</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-09 12:35:56</div>
<hr>

<div class="tg-post" id="msg-1676">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">خرید و فروش کانفیگ در کل گروه های whitedns ممنوع است
⚠️
بلافاصله بدون اخطار = ban</div>
<div class="tg-footer">👁️ 4.16K · <a href="https://t.me/whitedns/1676" target="_blank">📅 10:46 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-1675">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">💬
ورژن جدید WhiteVPN  1.6.4 برای گوشی های اندرویدی
🔼</div>
<div class="tg-footer">👁️ 6K · <a href="https://t.me/whitedns/1675" target="_blank">📅 09:08 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-1670">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">WhiteVPN-V1.6.4-arm64-v8a.apk</div>
  <div class="tg-doc-extra">34.4 MB</div>
</div>
<a href="https://t.me/whitedns/1670" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/whitedns/1670" target="_blank">📅 09:08 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-1669">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BzYKsPhy0ajv0a0FbwQ1RHzS9ibtozcQWIQIpubdepbZlsw0_3tQeiW5NGRi54Gm7GKbb7n_WjbhrSlRpjOxRJjjU4naUGPmMowBf3a7oVVir6oYbtz8P5nIqUWaQDkyGdJhDNdoyHr4D8Q4e4K5LRu9xSSgPmyu4Uom_XAlpNeIhUgJx8XQAeVZYznLl-MG0eTeHQ4HytvtqRfmdW5krv3ndXBVAv5fAvkgmg_HJS6MMIo-UOrItcrqj0x3LrF92kBiBfuVrvwTDHy2RAwnO-91IWrI6H8a7Kk5L6cZw0FH3GphjlguB4JJ-YxB5Xz28_Zn2bUoVDI80jQo3AdF3w.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/whitedns/1669" target="_blank">📅 09:03 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-1665">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/WmHMsvFFTWBcWevhINQqnuCl9w5rJbu-9_Lcuxu_UO_ESMtiO8PXls5BY8Ehv0-0JfNl8iE2WqZuP-dDFqUD0KMTMEqKq7Mt2Z-XgtxKBf0EI_uksDzTxONuP6nWszdVf_FjhPeB27DKC0O6ULHEJwSyJ86AdjqJuqIdDGUygARerk2ouYC8Xu_l1D4seyazKudg6-E8Y7--SznSAekCA4Ya1Mln3girbVGOQh7VpL23nmogRzpCz0lvi3UNhTn54fFqHKOYT77d86yCWvaYKd9Fc982CWtjzWx_HH_mlu8thxoojvhnRSzqcFTkMtBmEkuj7MQTTCAOVZH3xfqSzA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بیانیه رسمی و شفاف‌سازی مجموعه WhiteDNS
دسترسی به اینترنت آزاد، پایدار و امن حق طبیعی هر کاربر است. مجموعه
WhiteDNS
با هدف تحقق این هدف و تسهیل ارتباطات، خدمات و زیرساخت‌های خود را در اختیار عموم قرار داده است.
بدین‌وسیله رسماً اعلام می‌گردد:
۱۰۰٪ رایگان بدون هیچ قید و شرط:
تمامی خدمات، سرورها، کانفیگ‌ها، دی‌ان‌اس‌ها و آموزش‌های ارائه‌شده در چنل رسمی
WhiteDNS
کاملاً رایگان بوده و خواهد بود.
عدم وجود هرگونه اشتراک پولی (VIP):
این مجموعه هیچ‌گونه اکانت ویژه، پولی، پلن VIP، یا سرویس اختصاصی فروشی ندارد.
ممنوعیت کامل خرید و فروش:
هرگونه خرید، فروش، واسطه‌گری یا سوءاستفاده مالی از نام، کانفیگ‌ها یا سرورهای
WhiteDNS
غیرقانونی، غیرانسانی و نقض صریح قوانین این پروژه است.
هشدار نسبت به کلاهبرداری:
اگر فرد یا گروهی تحت عنوان ادمین، نماینده یا پشتیبان
WhiteDNS
به شما پیشنهاد خرید سرویس، اکانت یا پرداخت هزینه داد، سریعاً او را مسدود (بلاک) کرده و موضوع را گزارش دهید.
تنها مرجع رسمی:
کلیه اطلاع‌رسانی‌ها و به‌روزرسانی‌ها صرفاً از طریق کانال تلگرامی ما منتشر می‌شود:
🔗
کانال رسمی تلگرام:
https://t.me/whitedns
❤️
حمایت شما تنها از طریق معرفی کانال به دوستانتان و اشتراک‌گذاری اینترنت آزاد با دیگران و تماشای ویدیوهای ما در
کانال یوتیوب
و دادن
⭐️
به پست های ما و همچنین boost کردن کانال و حمایت از
گبت هاب
ما  امکان پذیر است
کلیه خدمات  WhiteDNS همواره رایگان در کنار شما می‌ماند.
@whitedns</div>
<div class="tg-footer">👁️ 8.67K · <a href="https://t.me/whitedns/1665" target="_blank">📅 06:37 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-1663">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">🔥
درود دوستان عزیز :
با توجه به رای گیری که شد و نظر دوستان عزیز
مقدار حجم روزانه کانفیگ های ربات به
4 گیگ
تغییر کرد
❤️
اگر از این خدمت استفبال شود احتمالا به زودی سرورهای بیشتر با لوکیشن های بیشتر در اختیار شما عزیران قرار خواهد گرفت که هر چه بیشتر امکان دسترسی رایگان شما فراهم شود .
بازم تاکید میکنیم که این کانفیگ ها فقط و فقط برای استفاده در قابلیت " exit chain " در برنامه های whiteaesther و whitevpn است . متاسفانه هنوز یک تعداد زیادی پیام دریافت میکنیم که دوستان میگن چرا این کانفیگ های توی v2rayng , hiddify و .......... کار نمیکنه
.
⚠️
لطفا تمام مطالب پست زیر را با دقت کامل بخونید
https://t.me/whitedns/1608
لازم به ذکر کرد در صورت مشاهده هر گونه سواستفاده از این کانفیگ ها لطفا به ادمین ها گزارش دهید
درصورتی که مشاهده شود که کانفیگ ها توسط افراد سودجو  در حال فروش به دیگران است این خدمت به طور کل حذف خواهد شد - پس خواهشمندیم خودتون در حفظ این امکان کوشا باشید
ربات :
@WhiteDnsChainbot
ارادتمند
تیم وایت
@whitedns</div>
<div class="tg-footer">👁️ 8.78K · <a href="https://t.me/whitedns/1663" target="_blank">📅 05:56 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-1658">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-poll">
<h4>📊 محدودیت حجم کانفیگ ربات را از 1 گیگ به چقدر تغییر بدیم که برای انجام کارهای روزمره کافی باشه ؟👀</h4>
<ul>
<li>✓ 1.5</li>
<li>✓ 2</li>
<li>✓ 3</li>
<li>✓ 4</li>
<li>✓ همین خوبه☺️</li>
</ul>
</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/whitedns/1658" target="_blank">📅 13:46 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-1656">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/Or6mr2PC3hbdkumOfe_r3Ep-7kL-E1LZ_brZ0j3UlocvQjMVzi4Dgfig2JPCfYnNCiLLZov5D_Ogv8_nxeg5NP8Knsqbm1NORu7gSMOecp9MCyqGGaJlnhmc3dj3ygoeNwnNj4RmfVXjRzveBPLpAso5Tp6iZL7-7tTmzuEo8ZcxUelHSWhrmpvfr9TzGhHxKFtB6eDjDPgh30kA_yebA3lwJJkuR2gfwc2_Qr9nROh7zrSrOIQpSuaj1E-Ap_hvbZk6KP8ONsSfS8BcB2tayhrn-x7QyZXr5geQ6oUha3ttJRVrJIsHCNkc2H0ImOaB8tDEyMtGWohzPqLae_8mig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#آموزش
اگر WhiteAesther mobile با یک بار زدن دکمه اتصال وصل نشد، یعنی هنوز باید تنظیمات درست شبکه خودت را پیدا کنی.
📡
این راهنمای کامل را قدم‌به‌قدم بخوان:
📖
https://github.com/WhiteDNS/WhiteAestherMobile/blob/main/docs/GUIDE.fa.md
@whitedns</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/whitedns/1656" target="_blank">📅 09:21 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-1654">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/WWbIJXoHZW178uNdYY7hN0-KIO9wI1ijcO2nC10qa1MEPTPsUabbBcnxHDfe4t7zMkSVfTUpEs8801ww19NDIb_yedtABo0YvV2joJwoxCxUUwQT7kCU9uTLRlJ1IFvwT1ILayvBBIBrezzcCZv5w7b34L9Mbk8jvugOmDUCF-T3VX3bnpmQdHqTmLDWdXX21ykkZJeMUJ5xQTNq6HeKtUZycf2nE7lzzrbsKvIjFf3v-4VYn9mZZBVfJNUqp4pvNlLjwYQV9p1guxM2vZdEN6oijQaijjJKG7rIJLzwddjRRUi32h2G_-gKmbZBp6jC0CeAjbALZ5BslhbxoYxvpA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">درود دوستان عزیز
👋
چند تا کانفیگ جدید به ربات اضافه کردیم  که شاید بهتر بتونید متصل بشید و برای سرویس های خارجی مشکلات کمتری داشته باشید . کانفیگ ها تست شده است و مشکلی نداره
✅
از حالا به بعد شما میتونید تا
3 کانفیگ
را انتخاب کنید
😃
❤️
لطفا برای اطلاعات بیشتر حتما پست زیر را مطالعه کنید
⚠️
⚠️
https://t.me/whitedns/1608
Bot
🤖
:
@WhiteDnsChainbot
@whitedns</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/whitedns/1654" target="_blank">📅 05:53 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-1653">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/F-zsVD6f9gETdhc2V9xJPicnkepjexGF0tnpvKOdY_4o0zIC4ncXLpeueLegM0tEx4mMEP-Mkzmg-3CYtzKtqTuAvw0tyDXMF8fW_GQs-l8l3nmp-KRGvkMB7jXOlE4vO7Wkn4fZ_TBuJOyV2T75PryHfjwnpC7jnfBhcFeU4tVFwktY3RSCTuVOj4ycidmBNcIijkgjBzu_ELZJCaQJCIqqZRhbmqudd0--H9Kx-uVvttwQ8fpnrE2BtjFIFGBRVakyhqZAlu2o9ziICYdX-bLzoEG1Y7Qa9lMKx-EPC4oHNATSAEGLWI_oXaGbp2cxfePE_DvAhRM397y30cnscA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📢
راهنمای کامل استفاده از ربات WhiteDnsChain
(کانفیگ هسته x-ray )
نکته : این ربات یک کانفیگ اضطراری برای شما ایجاد میکند تا در موارد خیلی خاص از ان استفاده کنید . کانفیگ های این ربات برای امکان exit chain در اپ های white ایجاد شده و هر گونه سواستفاده از آن مجاز نیست
🤖
آدرس ربات:
@WhiteDnsChainbot
برای دریافت و مدیریت اتصال اختصاصی خود مراحل زیر را انجام دهید:
1️⃣
شروع و انتخاب زبان
- وارد ربات شوید.
- دستور /start را ارسال کنید.
- گزینه «
🇮🇷
فارسی» را انتخاب کنید.
- برای تغییر زبان در آینده از گزینه «
🌐
تغییر زبان» استفاده کنید.
2️⃣
درخواست کانفیگ
- روی «
🔐
دریافت کانفیگ» بزنید یا دستور /config را ارسال کنید.
- درخواست شما برای مدیر فرستاده می‌شود.
- پس از تأیید، یک پیام اطلاع‌رسانی دریافت می‌کنید.
- دوباره /config را بزنید تا لینک اشتراک و QR اختصاصی شما نمایش داده شود.
3️⃣
اضافه‌کردن کانفیگ به برنامه
- یک برنامه سازگار با V2Ray/Xray روی دستگاه خود نصب کنید.
- لینک اشتراک را کپی کنید.
- در برنامه گزینه افزودن Subscription یا «افزودن اشتراک» را انتخاب کنید.
- لینک را وارد کرده و اشتراک را به‌روزرسانی کنید.
- یکی از سرورها را انتخاب کرده و اتصال را فعال کنید.
4️⃣
مشاهده وضعیت حساب
از گزینه «
👤
حساب من» یا دستور /account استفاده کنید تا موارد زیر را ببینید:
- وضعیت فعال یا غیرفعال
- تاریخ انقضا
- حجم مصرف‌شده
- حجم کل
- محدودیت تعداد دستگاه یا IP
5️⃣
دریافت دوباره کانفیگ
اگر پیام کانفیگ را پاک کردید، نگران نباشید. با /config همان کانفیگ اختصاصی دوباره نمایش داده می‌شود و کانفیگ جدیدی ساخته نخواهد شد.
6️⃣
پشتیبانی
- روی «
💬
پشتیبانی» بزنید یا /support را ارسال کنید.
- مشکل خود را در یک پیام کامل توضیح دهید.
- پیام مستقیماً برای مدیر ارسال می‌شود.
- پاسخ مدیر را داخل همین ربات دریافت خواهید کرد.
7️⃣
دستورات کاربردی
- /start — شروع و انتخاب زبان
- /config — دریافت کانفیگ
- /account — مشاهده وضعیت حساب
- /menu — نمایش منوی اصلی
- /support — ارتباط با پشتیبانی
- /help — نمایش راهنما
⚠️
نکات مهم
⚠️
-درخواست ها توسط ادمین دونه دونه بررسی و تایید میشود پس لطفا صبور باشید
- ادمین کاملا مختار است که به هر دلیل ممکن از ارایه کانفیگ به شما خودداری کند پس لطفا اعتراض نکنید
⚠️
-در حال حاظر کانفیگ ها با محدودیت 1 روزه و یک گیگ هست
- لینک و QR کاملاً اختصاصی است؛ آن را برای دیگران ارسال نکنید.
- هر حساب تلگرام فقط یک کانفیگ فعال دریافت می‌کند.
- ارسال چندباره /config کانفیگ تکراری ایجاد نمی‌کند.
- برای امنیت بیشتر، پس از دریافت کانفیگ می‌توانید پیام آن را با گزینه «
🗑
مخفی کردن» حذف کنید.
- در صورت پایان حجم یا اعتبار، از طریق پشتیبانی با مدیر ارتباط بگیرید.
@whitedns</div>
<div class="tg-footer">👁️ 9.41K · <a href="https://t.me/whitedns/1653" target="_blank">📅 05:06 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-1652">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/Sx7atuUTrJWpRpKrB9TQ_oON_pJAo2F6ZAudtV1GQrIA5Jgr1nXhiTqVfajP014PAezP9MCOW1k-jyKyVvc7XaXVZaKsbZ5atCJuUbLLF9NLcp4R_K7IvGrX_h-2MJBNLWXcInu-qbGZiKK7xsX8BdY03LVYa860_WeDtzT2g3OG_kuo7ThR1hTzjrM5kKEWGYRwTmahh4M7thKwRcbYblYATdlbV2RcZZbDbYqLPnmz-jDmmT2fjV5PzbEPTWlvoKYVGOFeIm3Y0_Q5vB_rXHyGcFPej6a8KjK92EtRQmTpodZe4q-911ZBidcaPLG89PXLT2MgcBtdumP8Sejcww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">Whitedns Chatbot V4 (جدید)
🎉
🎉
🎉
@WhiteDnsResponder_bot
راهنمای استفاده از ربات WhiteDNS
سلام!
این ربات به شما کمک می‌کند پاسخ سوال‌های مربوط به WhiteDNS، ابزارهای اتصال، DNS، نصب برنامه‌ها و رفع مشکلات رایج را از میان مطالب منتشرشده پیدا کنید.
آموزش :
⚠️
👇
### ۱. پرسیدن سوال معمولی
💬
کافی است سوالتان را مستقیماً برای ربات بنویسید.
نمونه‌ها:
- چطور WhiteDNS را روی اندروید نصب کنم؟
📱
- آخرین نسخه برنامه چیست؟
- چرا DNS وصل نمی‌شود؟
🌐
- تنظیمات ویندوز را چطور انجام بدهم؟
🖥
برای دریافت پاسخ بهتر، نام برنامه، دستگاه یا سیستم‌عامل و متن دقیق خطا را در یک پیام بنویسید.
ربات ممکن است همراه پاسخ، دکمه‌های منبع را نیز نمایش دهد. با انتخاب آن‌ها می‌توانید مطلب اصلی کانال را مشاهده کنید.
📎
### ۲. عیب‌یابی مرحله‌ای با /diagnose
🔧
اگر مشکل فنی دارید و نمی‌دانید چطور آن را توضیح دهید، دستور زیر را انتخاب کنید:
/diagnose
ربات از شما سه مورد کوتاه می‌پرسد:
1. نوع مشکل، مانند وصل نشدن، سرعت پایین، DNS یا نصب
2. دستگاه یا سیستم‌عامل
3. توضیح کوتاه مشکل یا متن دقیق خطا
پس از دریافت راه‌حل، این گزینه‌ها نمایش داده می‌شوند:
-
✅
حل شد — اگر مشکل برطرف شده است.
-
🔁
راه دیگر — دریافت یک راه‌حل جایگزین.
-
👤
ارسال برای مدیر — آماده‌کردن گزارش برای مدیران.
برای جلوگیری از طولانی‌شدن مراحل، ربات فقط یک راه‌حل جایگزین ارائه می‌دهد.
### ۳. ارسال نتیجه عیب‌یابی برای مدیر
اگر راه‌حل‌های ربات مؤثر نبودند، گزینه ارسال برای مدیر را انتخاب کنید.
قبل از ارسال، ربات پیش‌نمایشی شامل موارد زیر نشان می‌دهد:
- نوع مشکل
- دستگاه یا سیستم‌عامل
- توضیح شما
- راه‌حل‌هایی که امتحان کرده‌اید
- نام تلگرام
- نام کاربری، در صورت وجود
- شناسه عددی کاربر و گفتگو
- زبان حساب تلگرام
درخواست فقط بعد از انتخاب تأیید و ارسال برای مدیران فرستاده می‌شود.
### ۴. جستجوی مستقیم با /search
برای پیدا کردن مطالب کانال بدون ساخت پاسخ جدید، از این دستور استفاده کنید:
/search عبارت موردنظر
مثال:
/search نصب WhiteDNS اندروید
ربات نزدیک‌ترین مطالب را همراه دکمه مشاهده منبع نشان می‌دهد.
### ۵. ارسال پیام مستقیم به مدیران با /contact
اگر موضوع شما با عیب‌یابی قابل حل نیست، دستور زیر را انتخاب کنید:
/contact
سپس تمام توضیحات خود را در یک پیام کامل بفرستید. بهتر است پیام شامل این موارد باشد:
- نام برنامه
- دستگاه یا سیستم‌عامل
- نسخه برنامه
- نوع اتصال
- متن دقیق خطا
- کارهایی که قبلاً امتحان کرده‌اید
مدیران اطلاعات حساب تلگرام و پیام کامل شما را دریافت می‌کنند و می‌توانند از طریق ربات یا گفتگوی مستقیم پاسخ دهند.
شماره تلفن شما برای ربات قابل مشاهده نیست، مگر اینکه خودتان آن را داخل پیام ارسال کنید.
### ۶. ادامه سوال قبلی
ربات می‌تواند برای مدت کوتاهی ارتباط بین سوال‌های شما را تشخیص دهد.
مثال:
- پیام اول: «روش نصب WhiteDNS چیست؟»
- پیام بعدی: «برای اندروید چطور؟»
این زمینه گفت‌وگو حداکثر ۳۰ دقیقه و تا چهار نوبت نگه داشته می‌شود و به‌عنوان منبع واقعی پاسخ استفاده نمی‌شود.
### ۷. شروع گفت‌وگوی تازه با /new
اگر می‌خواهید موضوع قبلی فراموش شود، از این دستور استفاده کنید:
/new
این دستور زمینه موقت گفت‌وگو و عملیات نیمه‌تمام را پاک می‌کند.
### ۸. ثبت بازخورد
زیر پاسخ‌های ربات دو گزینه وجود دارد:
-
✅
مفید بود
-
❌
مفید نبود
بازخورد شما به مدیران کمک می‌کند پاسخ‌ها و مطالب ربات را بهتر کنند.
همچنین می‌توانید برای آخرین پاسخ از دستور زیر استفاده کنید:
/feedback
### ۹. لغو عملیات با /cancel
برای خروج از ارسال پیام، عیب‌یابی یا پاسخ‌دادن به یک درخواست فعال، بنویسید:
/cancel
فهرست دستورات
- /start — شروع کار با ربات
- /help — نمایش راهنما
- /diagnose — عیب‌یابی مرحله‌ای
- /search — جستجوی مستقیم در مطالب
- /feedback — ثبت بازخورد برای آخرین پاسخ
- /contact — ارسال پیام به مدیران
- /new — شروع گفت‌وگوی تازه
- /cancel — لغو عملیات فعال
محدودیت استفاده
برای کنترل هزینه و حفظ کیفیت سرویس:
- حداکثر ۳ درخواست هوش مصنوعی در هر ۵ دقیقه
- حداکثر ۵۰ درخواست هوش مصنوعی در روز
دستورهای ساده مانند /help، /search، /contact و بازخورد شامل این محدودیت هوش مصنوعی نمی‌شوند.
نکات مهم
- برای پاسخ دقیق‌تر، همه جزئیات مشکل را در یک پیام بنویسید.
- پاسخ‌ها بر اساس مطالب موجود WhiteDNS تولید می‌شوند و ممکن است برای مشکلات خاص کامل نباشند.
- در صورت حل‌نشدن مشکل، از مسیر عیب‌یابی و سپس ارسال گزارش برای مدیر استفاده کنید.
@whitedns</div>
<div class="tg-footer">👁️ 8.71K · <a href="https://t.me/whitedns/1652" target="_blank">📅 05:05 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-1651">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/DrcZjIH_0LarVKYF8MrvAaQaP_qeK2u583RvVglWyOEhVQot3kS-sa9K7rirw4kcRIFFbCgbwTqp8FrQGuLo_M44IC3nQNdIBGsM2Ox0w7hiAXO1wnsbMz2p9xLseYK94wwT7aeSvLUkerBY2kEyY7BZPo_eHiomAzU9zagHDUBK4-vlNf5GB8ieuBQTvXrd8Nf8HnRYeJMgQrV2B_4-uOnQ2l2UGkgwmM0kQjgg1QvgK0NUjXHfrb_C4E8YQh2DcKLCB2R3y_X5beKSLdDFGb01hJ0sPtPxG-AVTfoClQ_c8dfFxhP-HpA2k568dBuVAlfv00RAugw4FS73SPpJng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📢
آپدیت WhiteAesther — نسخه 1.2.5
🔥
⚠️
⚠️
⚠️
در این ورژن رفع باگ Android TV انجام شده است و دوستانی که روی گوشی استفاده میکنند لازم نیست اپدیت کنند
⚠️
⚠️
⚠️
مشکل کنترل با ریموت در Android TV برطرف شد. پیش از این، بعد از رسیدن به بخش «Connected for»، امکان حرکت به قسمت‌های پایین‌تر صفحه وجود نداشت.
حالا با دکمه‌های بالا و پایین کنترلر می‌توانید به‌راحتی بین تمام بخش‌های صفحه Home حرکت کنید و اطلاعاتی مثل آدرس، ترافیک مصرفی و جزئیات اتصال را ببینید.
این تغییر فقط مربوط به حالت Android TV است و عملکرد نسخه موبایل تغییری نکرده.
🔗
دانلود رسمی از گیت هاب
@whitedns</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/whitedns/1651" target="_blank">📅 16:25 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-1650">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Fxsdpf6ndZZ2_-UgUlJcK0U2ddUt1cRmOH5wl9_BPEql0OYRHw_5MT4keFuM6xa0yDCGxOFJHri4D0wlmR-1cYe0Fbui9biwdBVZ12s73wWnuGfCnPRwEknCiqAn54pdQwywAOjoDANxCyYeyBhlwp1v1MEe2YmT_TTakg7jNo8IRrvoZNGnp5AyPt1MmdBmlkV6WfMD_R3NPsv5DbmvSGsyggbwhwNG14hT8bDwl2IKQoFJBAFiWft1wMKP56cUgxUxef58Z2KKLoiGBuTU-aD4lbEH7UvxqL3zx7o50nPnxVX5z0oDtAm_8mHzFiUaf3wfVD2m7ShdJD0N1JKrSA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📺
نسخه Android TV و Google TV برنامه WhiteAesther منتشر شد
از نسخه v1.2.4 به بعد می‌توانید WhiteAesther را روی تلویزیون، TV Box و دستگاه‌های Google TV فقط با ریموت یا دستهٔ بازی کنترل کنید؛ بدون نیاز به صفحهٔ لمسی.
حداقل نسخه موردنیاز: Android 8
🔗
دانلود رسمی از گیتهاب
⚠️
برنامه را فقط از لینک رسمی بالا دانلود کنید.
🦢
🦢
🦢
🦢
🦢
🦢
📥
کدام فایل WhiteAesther را برای تلویزیون دانلود کنیم؟
برای بیشتر تلویزیون‌ها و TV Boxهای جدید:
"WhiteAestherMobile-1.2.4-arm64-v8a.apk"
اگر مدل پردازنده را نمی‌دانید یا فایل بالا نصب نشد:
"WhiteAestherMobile-1.2.4-universal.apk"
نسخه Universal روی دستگاه‌های بیشتری اجرا می‌شود، اما حجم بیشتری دارد.
گزینه‌های دیگر:
• نسخه "armeabi-v7a": مخصوص دستگاه‌های قدیمی ۳۲ بیتی
• نسخه "x86_64": بیشتر برای شبیه‌سازها و بعضی دستگاه‌های خاص
• فایل "AAB": برای نصب مستقیم مناسب نیست
🦢
🦢
🦢
🦢
🦢
🦢
🛠
نصب WhiteAesther مستقیماً روی Android TV
۱. مرورگر تلویزیون یا برنامه‌ای مثل Downloader را باز کنید.
۲. وارد صفحه رسمی انتشار شوید.
۳. فایل APK مناسب دستگاه را دانلود کنید.
۴. فایل را باز کرده و Install را بزنید.
اگر اجازه نصب داده نشد، گزینه Install unknown apps را برای مرورگر یا Downloader فعال کنید.
این تنظیم معمولاً در یکی از مسیرهای زیر قرار دارد:
Settings → Apps → Special app access → Install unknown apps
یا:
Settings → Security → Unknown sources
بعد از نصب، بهتر است این دسترسی را دوباره غیرفعال کنید.
🔗
دانلود نسخه رسمی از گیتهاب</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/whitedns/1650" target="_blank">📅 10:59 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-1649">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/g9kEd0_ktxWmPUh9f1UQHkfBoDrXw91bxFL3Ig87qctA29zI7RcUHu3338hcyDW182qqmFWgnDl0T8L6cNs2v_6VuOu3wl1Fz2Vio4q4rwhrQrZiVA3eG3Lk5ARYBu9jzdofvlR8DmiLX13cGoRrifmKeOnanAtaX6MX1Gikw9LP8YUQblLiatEkX_DgiLHmBQTQPagiYCVJA21msrTucGHmvuDTKStYopplubII0BeHgRCZhL0_BJE2ToqT2aunfDJp5oOhjO-GkyR7q0KfkCFBf7pJRGidf3swTd3i2zaVadtFjDnCVUNBb10Z7u12w8CRG8R-q9HmDCgclXv3YA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔭
داریم تست های نهایی رو برای WhiteAesther روی AndroidTV  انجام میدی
م</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/whitedns/1649" target="_blank">📅 19:14 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-1645">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn5.telesco.pe/file/o99UD0Gra0xDe59OSfd3LEYE2eyh-dSCnHRXqjSfJRNoR7PTBTa8732eimqx0R_qdtBuS8ZVTbDVLHgyIUxHUrYoiH0yxmn4OwkeWIWA7O_BElHGmD7RfqfkzwQlMfK5_244sS1EJRdpXvZ43RY5pBCR2zSoysFtR37Igo4Bl2FOZutBqOqweof5N_aElYiwsDkOHmNcvXdZrI3Wel6LdmGDPNrqFrz9pPIVG0jJ-4lRObP4pESIxgTep1k002SrNEY1g1zN4soTsCUH6Kz0xsgr9-pPnAPCNugiw2OmExjIHVscIGw8mwjag9kOn4P0y-65V0QtE_8-cnCD_VmB_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn5.telesco.pe/file/Vt26Skj1kwUCzioSy507CAZdk_pRpz9yPdAxC-N5A797b4NNMepHeicNLdnohQ87Vd5CxjjTBf67nxoRMNZY2gR2wMUcFoIb0M-2rEHVLVIEJtOo2wNx68zY2D5GJGL3GC5Q-h42I_tOTHcyG_QrIB3_gIwdW83RLkI-1fxnSrbry9xm6_vKSpkAVvvtR1yayOqOsjN384zmZ8SoCcmK2HDy18rvrW3SSNGsAvvvqx9-ZXGZGfDJLh8q106H8Srf70hdD2ZumQK4Wnhd3wxuqrWupLrZ6r8iMYry0ab6_64UZwvsI7CBVDf6MVUQqshNWVmEl-UiJwLnZanduJKxcw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn5.telesco.pe/file/cKTW22YKmH-qYxic83GeCGUDlZhdDRmgurc_KWRELDiQEalchgyQpPLuQcGhRdcnKXdZOTvxDgRgvy4YnCAFwE9G20dTZwEJTY4tn055xSncci5h8jZuyJUi2vV1lKGx5D_Loe3J5MAvmybleNV1v8OLVXsDY_tneknMkyRWgTyY4P8x728nl-Pnr1ZH6bihANA0MowJJBbabtulBRcTaoGk-AyL8nonX40-7vW-xcbMTflHKqo2QjygNNqE_A0pMCh_Vh4FgSmHcuRDG1LB9gKkZGrhShmNas1P_ufDPg_QumqvJApJZQCOs9hed-xuHo4B_Tn8oX4sE7KMisJnKw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">راهنمای زنجیر کردن  Psiphon Desktop
با
whiteaesther
Desktop
🔥
🔥
اول Psiphon را وصل کنید.
در تنظیمات Psiphon proxy محلی را پیدا کنید. و یکی از پورت های زیر را وارد کنید . توصیه میشود از ساکس استفاده کنید
SOCKS5:1080
HTTP:8080
WhiteAesther را باز کنید.
بروید به:
Advanced
→
Routes & transports
→
Anti-blocking
در فیلد
Dial through a local proxy
یکی از این‌ها را وارد کنید:
socks5://127.0.0.1:1080
یا:
http://127.0.0.1:8080
بعد
Save profile
را بزنید.
حالا Connect کنید. مسیر  می‌شود:
App traffic -> WhiteAesther local SOCKS -> Aether/WARP -> Psiphon local upstream -> Internet
اگر میخواهید که whiteaesther سیستم شما را تانل کند روی Full tunnel و اگر نه از پراکسی whiteaesther برای نرم افزارهای خاص خودتون استفاده کنید
نکته : قابلیت exit chain را توی تنظیمات خاموش کنید
⚠️
⚠️
تیم وایت
@whitedns</div>
<div class="tg-footer">👁️ 40.2K · <a href="https://t.me/whitedns/1645" target="_blank">📅 15:13 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-1644">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromxsfilternet | فیلترنت(امیرپارسا گودمن)</strong></div>
<div class="tg-text">اگه حوصله خوندن توضیحات رو ندارید، فقط ساب زیر را وارد PattNG/PattN کرده و لذت ببرید !  https://raw.githubusercontent.com/patterniha/Free-Configs/main/configs.txt  ساب هر ۲۴ ساعت آپدیت میشود. /// توضیحات:  پروژه های خوبی وجود دارند که کانفیگهای رایگان را جمع‌آوری…</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/whitedns/1644" target="_blank">📅 06:16 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-1641">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">مطالب اموزشی نسخه 1.6.0 دسکتاپ whiteaesther
🔥
🔥
خلاصه :
🔧
تغییرات و قابلیت‌های جدید
▫️
حالت
Full Tunnel
یک کارت شبکهٔ مجازی ایجاد می‌کند تا تمام ترافیک سیستم از تونل عبور کند؛ حتی برنامه‌هایی که تنظیمات Proxy را نادیده می‌گیرند.
▫️
خروج سایت‌های ایرانی از تونل
شامل ۲۹۰۶ رنج IP و ۴۱٬۷۲۹ دامنه ایرانی است که مستقیماً داخل خود برنامه قرار گرفته‌اند و نیازی به دانلود جداگانه ندارند.
▫️
دریافت خودکار دسترسی Administrator
هر زمان دسترسی ادمین لازم باشد، برنامه خودش پیام تأیید ویندوز را نمایش می‌دهد و با سطح دسترسی لازم دوباره اجرا می‌شود. دیگر نیازی به راست‌کلیک و انتخاب
Run as administrator
نیست.
▫️
اطلاع‌رسانی نسخه‌های جدید
در صورت انتشار نسخه جدید، یک نوار اطلاع‌رسانی بالای برنامه ظاهر می‌شود که با یک کلیک شما را به صفحه دانلود می‌برد.
▫️
چهار تنظیم جدید موتور
تنظیمات بیشتری برای موارد زیر اضافه شده است:
Local Proxy
Domain Sniffing
Identity Re-registration
Keepalive
مقدار پیش‌فرض
Keepalive
نیز از ۵ ثانیه به ۲۵ ثانیه تغییر کرده است.
▫️
عبور مستقیم ترافیک شبکه محلی
ترافیک دستگاه‌های داخل شبکه مثل Printer، Router و NAS دیگر به نود خروجی فرستاده نمی‌شود و مستقیماً در شبکه محلی باقی می‌ماند.
▫️
رفع مشکل آیکون‌های مرده در Taskbar
حالا در تمام حالت‌های خروج از برنامه، آیکون آن به‌درستی از Taskbar و System Tray حذف می‌شود.
▫️
حذف اتصال خودکار
برنامه دیگر بدون اجازه کاربر به‌صورت خودکار متصل نمی‌شود. زمان اتصال کاملاً در اختیار شماست.
▫️
باز شدن صحیح پنجره با کلیک روی آیکون برنامه
مشکلی که در حالت اجرای برنامه با دسترسی Administrator باعث می‌شد ویندوز فرمان باز شدن پنجره را مسدود کند، برطرف شده است.
🛡
۱. حالت Full Tunnel — جلوگیری کامل از DNS Leak
تا الان دو حالت داشتیم:
▫️
فقط همین برنامه
▫️
کل دستگاه
مشکل حالت دوم این بود که فقط برنامه‌هایی را پوشش می‌داد که از تنظیمات Proxy ویندوز استفاده می‌کنند.
خیلی از برنامه‌ها این تنظیمات را نادیده می‌گیرند و مستقیماً به اینترنت یا DNS وصل می‌شوند. در نتیجه ممکن بود بخشی از ترافیک خارج از تونل عبور کند.
حالت جدید
Full Tunnel
یک کارت شبکه مجازی ایجاد می‌کند و
تمام ترافیک سیستم
را از تونل عبور می‌دهد؛ حتی برنامه‌هایی که Proxy سیستم را نادیده می‌گیرند.
این حالت بهترین گزینه برای جلوگیری از DNS Leak است.
🔹
روش فعال‌سازی
۱. برنامه را باز کنید و متصل شوید.
۲. پایین صفحه اصلی سه حالت وجود دارد.
۳. گزینه سوم یعنی Full Tunnel را انتخاب کنید.
۴. ویندوز برای دسترسی لازم از شما اجازه می‌خواهد. گزینه Yes را بزنید.
۵. برنامه به‌صورت خودکار بسته و دوباره با دسترسی لازم اجرا می‌شود.
دیگر لازم نیست روی برنامه راست‌کلیک کرده و Run as administrator را انتخاب کنید.
✅
برای تست
بعد از اتصال، سایت زیر را باز کنید:
dnsleaktest.com
سپس گزینه Extended Test را اجرا کنید.
سرورهای نمایش‌داده‌شده باید مربوط به کشور نودی باشند که به آن متصل شده‌اید.
━━━━━━━━━━━━━━━━━━
🇮🇷
۲. خروج خودکار سایت‌های ایرانی از تونل
دیگر لازم نیست برای باز کردن بانک‌ها، دیجی‌کالا، آپارات و سرویس‌های داخلی، هر بار VPN را خاموش کنید.
سایت‌های داخلی معمولاً نیازی به عبور از تونل ندارند. عبور آنها از تونل فقط می‌تواند سرعت را کاهش دهد و پهنای باند نود را مصرف کند.
حالا می‌توانید کاری کنید که:
سایت‌های ایرانی مستقیم باز شوند و بقیه ترافیک از تونل عبور کند.
🔹
روش فعال‌سازی
به مسیر زیر بروید:
Advanced → Traffic & DNS → Routing Rules
سپس گزینه زیر را روشن کنید:
Iranian sites bypass the tunnel
لیست موردنیاز داخل خود برنامه قرار دارد و شامل:
▫️
۲۹۰۶ رنج IP ایران
▫️
۴۱٬۷۲۹ دامنه
است.
هیچ فایلی هنگام اتصال دانلود نمی‌شود؛ بنابراین این قابلیت حتی زمانی که دسترسی آزاد به اینترنت ندارید نیز قابل استفاده است.
━━━━━━━━━━━━━━━━━━
📱
۳. اشتراک اینترنت با گوشی، تلویزیون و دستگاه‌های دیگر
حالا می‌توانید کامپیوتر خود را به یک Proxy Server تبدیل کنید و دستگاه‌های دیگر را از طریق آن به اینترنت متصل کنید.
بدون نیاز به نصب WhiteAesther روی گوشی.
🔹
روش فعال‌سازی
به مسیر زیر بروید:
Advanced → Traffic & DNS
در بخش:
Share with other devices
گزینه اشتراک‌گذاری را روشن کنید.
برنامه یک آدرس مشابه این نمایش می‌دهد:
192.168.1.24:1080
بار اول ویندوز ممکن است از شما اجازه Firewall بخواهد.
گزینه:
Allow access
را انتخاب کنید.
اگر اجازه ندهید، Proxy فقط روی همان کامپیوتر قابل استفاده خواهد بود.
📱
در Android
وارد تنظیمات Wi-Fi شوید.
شبکه متصل را باز کنید و به بخش تنظیمات Proxy بروید.
حالت Proxy را روی Manual قرار دهید.
برای مثال:
Hostname:
192.168.1.24
Port: 1080
همان IP و پورتی را وارد کنید که WhiteAesther نمایش داده است.
🍎
در iPhone
به مسیر زیر بروید:
Settings → Wi-Fi
روی علامت (i) کنار شبکه بزنید.
سپس:
Configure Proxy → Manual
را انتخاب کرده و IP و Port نمایش‌داده‌شده در WhiteAesther را وارد کنید.
🔐
نکته امنیتی مهم
اگر Username و Password تعیین نکنید،
هر دستگاهی که به همان شبکه Wi-Fi متصل باشد می‌تواند از Proxy شما استفاده کند.
در شبکه خانگی شاید این موضوع مهم نباشد، اما در محل کار، دانشگاه، هتل یا کافه حتماً هر دو فیلد زیر را پر کنید:
Username
Password
خود برنامه نیز در صورت خالی بودن آنها با یک هشدار زرد به شما اطلاع می‌دهد.
یک Port برای هر دو پروتکل استفاده می‌شود:
HTTP
و
SOCKS5
بنابراین همان شماره Port را برای هرکدام که دستگاه شما پشتیبانی می‌کند وارد کنید.
━━━━━━━━━━━━━━━━━━
⚡️
۴. پشتیبانی بهتر از Hysteria2 و TUIC
اگر در Subscription شما نودهای Hysteria2 وجود داشتند و همیشه علامت — نمایش داده می‌شد، این مشکل اکنون برطرف شده است.
مشکل از اندازه Packet بود.
این پروتکل‌ها Packetهایی با اندازه حدود ۱۲۸۰ بایت ارسال می‌کنند، در حالی که تونل قبلی فقط ۱۲۵۲ بایت ظرفیت داشت.
در نتیجه حدود
۲۸ بایت کمبود ظرفیت
باعث می‌شد Packet قبل از ارسال حذف شود.
🔹
روش استفاده
به مسیر زیر بروید:
Advanced → Routes & Transports
سپس Protocol را روی:
WireGuard
قرار دهید.
برای این نودها از MASQUE استفاده نکنید.
در حالت MASQUE این محدودیت از سمت Cloudflare وجود دارد و برنامه نیز کنار نود توضیح می‌دهد که چرا قابل استفاده نیست.
━━━━━━━━━━━━━━━━━━
🔔
۵. اطلاع‌رسانی نسخه‌های جدید
از این نسخه به بعد، وقتی نسخه جدید WhiteAesther منتشر شود، خود برنامه به شما اطلاع می‌دهد.
یک نوار اطلاع‌رسانی در بالای برنامه نمایش داده می‌شود.
با زدن گزینه:
Get it
مستقیماً وارد صفحه دانلود نسخه جدید خواهید شد.
━━━━━━━━━━━━━━━━━━
🔧
سایر تغییرات
▫️
نودهای REALITY حالا با برچسب Not Supported مشخص می‌شوند.
موتور فعلی از آنها پشتیبانی نمی‌کند، بنابراین بهتر است وضعیت آنها واضح باشد تا اینکه نودی نمایش داده شود که هیچ‌وقت متصل نمی‌شود.
▫️
Subscriptionها کامل‌تر پردازش می‌شوند و مشکل جا افتادن بعضی نودها برطرف شده است.
▫️
مشکل باقی ماندن آیکون‌های قدیمی برنامه در Taskbar برطرف شده است.
▫️
برنامه دیگر به‌صورت خودکار متصل نمی‌شود. تصمیم برای اتصال کاملاً با کاربر است.
▫️
تنظیمات بیشتری برای Local Proxy، Keepalive و گزینه‌های پیشرفته اضافه شده است.
▫️
موتور برنامه به نسخه زیر ارتقا پیدا کرده است:
Aether 1.7.0
@WhiteDNS_Laurie</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/whitedns/1641" target="_blank">📅 05:44 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-1640">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/cg0mTX4-KoLKFM9tVnQDP8JmGkCniOBeoj3I-lillSOEcoRbGBVmAMKB_baiu91ZuntaukbLDUiQUwZwJeQDTcywS5z65t849o9BE9cxkPkKQcGFo6PZb3nE7yjRmis1i-frIMLzD0UhSWCuUBh91CO8ojGRWuxWZvTrmS62Zv_geK9s3u83mBkkTzj6x9NUYvxM8UZvFosB8VwUgvebRJax1wquKfs-7y_f9Evl-xS8NF7Uy_M1xfap0ObXro5CneKQaCdWF8Rqt2F65QnaHQOu05vEYR4MKZrDjt95t8wjksmklFWvmjbDlD86zXpnNGYdDNuDYZgO-lej2c_7gQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚀
نسخه 1.6.0 دسکتاپ  WhiteAesther منتشر شد
بزرگ‌ترین آپدیت WhiteAesther تا امروز.
حالا می‌توانید:
▫️
کل کامپیوتر را تونل کنید
▫️
سایت‌های ایرانی را از تونل خارج نگه دارید
▫️
اینترنت را با گوشی، تلویزیون و دستگاه‌های دیگر به اشتراک بگذارید
━━━━━━━━━━━━━━━━━
📥
دانلود
github.com/WhiteDNS/WhiteAesther/releases
نسخه‌های موجود:
▫️
Windows
▫️
Linux —
deb / rpm / AppImage
▫️
macOS Intel
▫️
macOS Apple Silicon
━━━━━━━━━━━━━━━━━━
⚠️
نکته مهم قبل از تست
اگر برنامه رسمی
Cloudflare WARP
روی سیستم شما نصب است، قبل از استفاده از WhiteAesther حتماً آن را کاملاً
Disconnect
کنید.
اجرای همزمان دو VPN روی مسیر شبکه می‌تواند باعث تداخل، قطع اتصال یا نتایج گیج‌کننده شود.
━━━━━━━━━━━━━━━━━━
💬
اگر سؤال یا مشکلی داشتید، همین‌جا مطرح کنید.
@WhiteDNS</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/whitedns/1640" target="_blank">📅 05:43 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-1636">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromBlue Knight(𝑫𝒊𝒂𝒏𝒂🍓)</strong></div>
<div class="tg-text">آموزش تغییر لوکیشن با Exit Chain
داخل اپ‌های WhiteVPN و WhiteAesther
🔥
واسه gemini و بقیه AI هایی ک نیاز دارین عالیه
https://youtu.be/yx-jFqv9pYM?si=VuY0qqm5qbFUJOO6</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/whitedns/1636" target="_blank">📅 03:01 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-1634">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">🔗
نسخه ۱.۲.۳ اندروید WhiteAesther منتشر
شد ......!
در نسخه جدید سه بخش مهم اضافه شده:
🛡
قفل ایمنی
🧭
قواعد مسیریابی
⚙️
چند تنظیم جدید برای موتور اتصال
پایین، همه موارد را همراه با آموزش توضیح داده‌ایم.
🛡
۱. قفل ایمنی — Kill Switch
چه مشکلی را حل می‌کند؟
تا الان اگر تونل بعد از چند بار تلاش وصل نمی‌شد، برنامه تسلیم می‌شد و گوشی بی‌صدا به اینترنت معمولی برمی‌گشت.
حالا می‌توانید مشخص کنید که در چنین شرایطی، به‌جای برگشت به اینترنت عادی،
تمام ترافیک اینترنت مسدود شود.
آموزش
۱) وارد بخش Traffic شوید.
۲) بخش Advanced را باز کنید.
۳) گزینه زیر را روشن کنید:
Block traffic if the tunnel fails
تمام! از این به بعد اگر تونل از کار بیفتد، هیچ ترافیکی از گوشی خارج نمی‌شود.
🔸
حالت سخت‌گیرانه‌تر
بعد از فعال کردن گزینه بالا، گزینه دیگری ظاهر می‌شود:
Keep blocking after you disconnect
اگر این گزینه را روشن کنید،
حتی زمانی که خودتان اتصال را دستی قطع می‌کنید، اینترنت همچنان مسدود می‌ماند
تا خودتان آن را آزاد کنید.
⚠️
توجه:
در این حالت گوشی واقعاً اینترنت نخواهد داشت. اگر فراموش کنید این گزینه فعال است، ممکن است فکر کنید اینترنت یا شبکه مشکل دارد.
برای برداشتن قفل دو راه دارید:
▫️
از نوتیفیکیشن Traffic is blocked
▫️
یا از صفحه اصلی برنامه و دکمه Lift the block
اگر دوباره به تونل متصل شوید، قفل به‌صورت خودکار برداشته می‌شود.
🧭
۲. قواعد مسیریابی — Routing Rules
چه مشکلی را حل می‌کند؟
بعضی سایت‌ها و اپلیکیشن‌ها با IP خارجی درست کار نمی‌کنند؛ مثل بعضی بانک‌ها، اپ‌های داخلی یا سرویس‌های ایرانی.
قبلاً برای استفاده از آنها مجبور بودید VPN را کاملاً خاموش کنید.
حالا می‌توانید مشخص کنید که
فقط بعضی سایت‌ها یا سرویس‌ها از تونل عبور نکنند
و بقیه ترافیک همچنان از تونل استفاده کند.
آموزش
۱) وارد بخش Routes شوید.
۲) در کارت اول، گزینه Routing rules را که زیر Exit chain قرار دارد انتخاب کنید.
۳) دو کادر خواهید دید:
🔹
کادر
Never connect
هر چیزی که اینجا قرار بگیرد، اصلاً اجازه اتصال نخواهد داشت.
مناسب برای مسدود کردن تبلیغات، ردیاب‌ها و دامنه‌های ناخواسته.
🔹
کادر
Skip the tunnel
هر چیزی که اینجا قرار بگیرد،
بدون تونل و با IP واقعی شما
باز می‌شود.
مناسب برای بانک‌ها، سایت‌ها و اپلیکیشن‌های داخلی.
هر قانون را در یک خط جداگانه بنویسید.
مثال:
bank.example.ir
digikala.com
snapp.ir
نوشتن یک دامنه، زیرمجموعه‌های آن را هم شامل می‌شود.
برای مثال:
digikala.com
شامل این مورد هم خواهد شد:
www.digikala.com
حالت‌های پیشرفته
▫️
فقط همان دامنه دقیق:
full:
example.com
▫️
هر آدرسی که یک کلمه خاص داخل آن باشد:
keyword:tracker
▫️
یک محدوده IP:
cidr:
10.0.0.0/8
▫️
یک پورت مشخص:
port:25
▫️
کل شبکه محلی:
private
▫️
هر خطی که با # شروع شود، به‌عنوان توضیح در نظر گرفته شده و اجرا نمی‌شود.
⚠️
مهم:
هر چیزی که داخل Skip the tunnel قرار دهید، با
IP واقعی شما
به اینترنت متصل می‌شود. بنابراین این لیست را فقط برای موارد ضروری استفاده کنید.
🔸
نکته مهم درباره دامنه‌ها
در مسیر زیر:
Traffic ← Advanced
گزینه‌ای وجود دارد با نام:
Match rules on domain names
این گزینه به‌صورت پیش‌فرض روشن است و بهتر است روشن بماند.
اگر آن را خاموش کنید، قوانینی که با نام دامنه نوشته شده‌اند ممکن است کار نکنند؛ چون برنامه در اندروید معمولاً ترافیک را در سطح IP دریافت می‌کند.
در صورت خاموش بودن این گزینه، خود صفحه Routing rules نیز هشدار خواهد داد.
⚙️
۳. تنظیمات جدید موتور
تمام این تنظیمات در مسیر زیر قرار دارند:
Traffic ← Advanced
🔹
تنظیم DNS داخل تونل
گزینه:
DNS inside the tunnel
می‌توانید DNS دلخواه خودتان را وارد کنید.
مثال:
8.8.8.8
,
1.1.1.1
اگر خالی بگذارید، DNS پیش‌فرض موتور استفاده می‌شود.
آدرس‌های نامعتبر نیز به‌صورت خودکار نادیده گرفته می‌شوند.
🔹
اتصال تونل از طریق یک پروکسی دیگر
گزینه:
Dial out through a proxy
این قابلیت یکی از مواردی بود که کاربران زیادی درخواست کرده بودند.
اگر ابزار دیگری روی گوشی شما در حالت پروکسی فعال است، مثلاً
Psiphon
، می‌توانید اتصال WhiteAesther را از داخل آن عبور دهید.
مسیر اتصال به این شکل می‌شود:
گوشی ← WhiteAesther ← Psiphon ← اینترنت
برای مثال اگر پروکسی SOCKS روی پورت ۱۰۸۰ فعال باشد، وارد کنید:
socks5://127.0.0.1:1080
پورت را باید با پورت واقعی برنامه پروکسی خودتان جایگزین کنید.
پروکسی HTTP نیز پشتیبانی می‌شود:
http://127.0.0.1:8080
🔹
تنظیم WireGuard Keepalive
این گزینه می‌تواند روی مصرف باتری تأثیر داشته باشد.
سه مقدار قابل انتخاب است:
▫️
۵ ثانیه
▫️
۱۵ ثانیه
▫️
۲۵ ثانیه
مقدار پیش‌فرض در نسخه جدید
۲۵ ثانیه
است. در نسخه‌های قبلی مقدار پیش‌فرض ۵ ثانیه بود.
هر بار که این زمان می‌گذرد، گوشی یک بسته کوچک ارسال می‌کند تا اتصال فعال بماند.
در حالت ۵ ثانیه، این کار بسیار بیشتر انجام می‌شود و مخصوصاً روی اینترنت موبایل می‌تواند باعث مصرف بیشتر باتری شود.
مقدار ۲۵ ثانیه نیز مقدار رایج استاندارد WireGuard است.
⚠️
اگر بعد از آپدیت متوجه شدید اتصال WireGuard بعد از چند دقیقه بی‌کاری قطع می‌شود، مقدار را دوباره روی
۵ ثانیه
قرار دهید.
🔹
جایگزینی هویت ردشده
گزینه:
Replace a refused identity
این گزینه به‌صورت پیش‌فرض روشن است.
اگر Cloudflare هویت ذخیره‌شده روی گوشی را دیگر قبول نکند، برنامه به‌صورت خودکار یک هویت جدید دریافت می‌کند.
بدون این قابلیت ممکن است تونل ظاهراً متصل شود، اما هیچ ترافیکی از آن عبور نکند.
📌
خلاصه محل تنظیمات
بخش
Routes
▫️
Protocol
— مثل قبل
▫️
Endpoint
— مثل قبل
▫️
Exit chain
— مثل قبل
▫️
Routing rules
—
جدید
بخش
Traffic ← Advanced
▫️
Obfuscation
— مثل قبل
▫️
Local proxy port
— مثل قبل
▫️
Share with this network
— مثل قبل
▫️
DNS inside the tunnel
—
جدید
▫️
Dial out through a proxy
—
جدید
▫️
WireGuard keepalive
—
جدید
▫️
Block traffic if the tunnel fails
—
جدید
▫️
Match rules on domain names
—
جدید
▫️
Replace a refused identity
—
جدید
⬇️
دانلود آخرین نسخه
https://github.com/WhiteDNS/WhiteAestherMobile/releases/latest
▫️
arm64-v8a
— مناسب تقریباً همه گوشی‌های سال ۲۰۱۷ به بعد؛
اول این نسخه را امتحان کنید.
▫️
armeabi-v7a
— مخصوص گوشی‌های قدیمی‌تر
▫️
universal
— اگر مطمئن نیستید؛ حجم این نسخه تقریباً سه برابر است.
اگر با مشکلی مواجه شدید، از مسیر زیر گزارش بگیرید:
Settings ← Diagnostics
و برای ما ارسال کنید.
@whitedns</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/whitedns/1634" target="_blank">📅 19:13 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-1632">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/gij49MPc6pmeG3w4N35fR9ck1QjS8jqEJUfUGch7gilfatlaPOBkjc0HDxO02ckb3tJAjbhHGZy_b1yeI6Qa6ZXhYq-t8wvZj7ubUjIV3VohugtC5vr-eYrIhCKnV8ByMGUZHmrShlOJUQaRWpdQXSlBDn4Zn_cjQL7KLtlw1eIPT9zfm-we96TB28iphL6ZAy7Njwe8KMRuF8tYzmo0Vi-lO6XN211r8zYkAO6SN5PgrRnIsPffZmVTTvE471Sl3OAsoO8pEG8apBwgWRp594BxU7NvCD-pJ2lZ9sw-n6tFTdtadA_XqKnhmemX2AQWn_uD83TQ2Ux5MAQjs98h8Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔜
به‌زودی:  WhiteAesther  اندروید نسخه ۱.۲.۳
🔥
🔥
🔥
▫️
قفل ایمنی (Kill switch) — اگه تونل بمیره، ترافیک بی‌صدا لو نمی‌ره
▫️
قواعد مسیریابی — بگین کدوم سایت‌ها بدون تونل باز بشن (بانک، اپ‌های داخلی)
▫️
اتصال یه پروکسی دیگه (مثل سایفون)
▫️
امکان DNS دلخواه داخل تونل (برای کاهش پینگ)
▫️
بهینه‌سازی مصرف باتری روی WireGuard
@whitedns</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/whitedns/1632" target="_blank">📅 16:12 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-1631">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/DL0fDopsSNJnWNHG-H1gdgD4Rx0h-Be613OXZFRuUQ-xkyFoghzsz6lATEarX6Tlbz_S8rGOEWSVJ8UeIz-OAM88duOqBxAz5RTMsza0mmGRuI1uYL5GOy2RWzLjUYIdYIt6MUIeEvjbTQ3p-_lscSvP75dAmiprlmoPbgQnQFA6GBFP9G-NA3T6ryGytTOHpA0d4NPpm9mBkUIgZDy4mG1yMkhY56AbASbQ1Us3biCxRdlB5ZtjScjV9Dvkp-Rt76nwMSDd3GDIIEJPWoxNTRyBeWZppT1KplTp2wPf9BPt3nID9jNQ8B3FGUnlDdgXl5St5NMZjY6ej2kY6aoRIg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🌐
کلاینت WhiteAesther
(دانلود همزمان برای اندروید و ویندوز / دسکتاپ)
اگر به دنبال یک اتصال فوق‌العاده پایدار، سریع و امن با پروتکل نوین MASQUE H2 هستید، نرم‌افزار WhiteAesther در دو نسخه دسکتاپ و موبایل در دسترس شماست.
✨
قابلیت‌ها و ویژگی‌های کلیدی:
🔹
مبتنی بر پروتکل پرسرعت و مدرن MASQUE H2
🔹
اتصال سریع با یک کلیک (Zero-Config)
🔹
پایداری بالا و پینگ عالی مناسب وب‌گردی، گیمینگ و استریم
🔹
سیستم محافظت از کل ترافیک دستگاه (IPv4 + IPv6)
🔹
قابلیت Reconnect خودکار و Killswitch داخلی
🔹
رابط کاربری بسیار روان، تاریک (Dark Mode) و مدرن
━━━━━━━━━━━━━━━━━━━━
📥
لینک‌های دانلود مستقیم آخرین نسخه از گیت‌هاب:
📱
دانلود نسخه اندروید (Android APK):
🔗
https://github.com/WhiteDNS/WhiteAestherMobile/releases/latest
💻
دانلود نسخه دسکتاپ (Windows / PC):
🔗
https://github.com/WhiteDNS/WhiteAesther/releases/latest
━━━━━━━━━━━━━━━━━━━━
💡
پیشنهاد: این پست را برای دسترسی سریع به هر دو نسخه ذخیره (Save) یا پین کنید.
🆔
@whitedns</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/whitedns/1631" target="_blank">📅 10:37 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-1630">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/quTzI3fM5QSOWcQpcfEC4P7ihAUjTSoTLSduSL3Am4ac0OkyzLCROanzmtRxLifi3qB-UwPCG_Ln5awmuoXz0Dccj4yPGd5ge8rzW4_15AadrxQEOAV5pb_Myix6aIP7Q0KgwZj8tIyQTiWVNr-UFSlUMk4ZzDNWPmrakra1OSqfQbkrkSU7ZTa8ZKCcu4scrbZlZWXbRk5Fv07G64gQW2aEUaDfS7_8l9HPpRL-_lLIyjkTsSpsRhw8Ua7BWQ4HXkfOnDki1OlgNHICnbZISJ-knKiYNmYeDXCyOBoYPOcDkdVw9EwdqwF4JjXO5eV9btSVzJu094QYmCHeIpxn6A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚀
دسترسی آزاد و امن به اینترنت با WhiteVPN (نسخه موبایل و دسکتاپ)
اگر به دنبال یک کلاینت یکپارچه، سبک و حرفه‌ای هستید، WhiteVPN با رابط کاربری مدرن در دسترس شماست!
⚙️
قدرت گرفته از هسته Mihomo:
این برنامه بر پایه هسته قدرتمند Mihomo (مشابه کلش و متا) توسعه یافته است که بالاترین سطح پایداری و سرعت را در دور زدن محدودیت‌ها برای شما فراهم می‌کند.
⚠️
توجه مهم:
این اپلیکیشن کاملاً سورس‌باز (Open-Source) است و در Google Play یا App Store منتشر نشده است. تنها منبع رسمی برای دانلود، مخزن گیت‌هاب پروژه است.
✨
ویژگی‌های کلیدی:
🔹
پشتیبانی همزمان از ویندوز، مک، لینوکس و اندروید
🔹
رابط کاربری ساده و اتصال تنها با یک کلیک
🔹
سیستم پراکسی جامع و تونلینگ کل سیستم (System-wide)
🔹
مدیریت پیشرفته سرورها و پایداری بالا در اتصالات
━━━━━━━━━━━━━━━━━━━━
📥
دانلود مستقیم آخرین نسخه از گیت‌هاب (رسمی):
📱
نسخه اندروید (Mobile):
🔗
https://github.com/WhiteDNS/WhiteVPN/releases/latest
💻
نسخه دسکتاپ (Windows / macOS / Linux):
🔗
https://github.com/WhiteDNS/WhiteVPN-Desktop/releases/latest
━━━━━━━━━━━━━━━━━━━━
💡
برای دانلود، وارد لینک‌های بالا شده و از بخش "Assets" فایل متناسب با دستگاه خود (فایل apk برای اندروید و فایل‌های نصب برای ویندوز/مک) را دانلود کنید.
🆔
@whitedns</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/whitedns/1630" target="_blank">📅 10:37 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-1627">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">سابسکریپشن WhiteDNS برای اپ های WhiteVPN / Karing / Clash Mi / Clash Party / FLClash :
https://raw.githubusercontent.com/iampedii/whitedns-sub/refs/heads/main/mihomo.yaml
@whitedns</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/whitedns/1627" target="_blank">📅 19:05 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-1626">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">Live stream finished (1 hour)</div>
<div class="tg-footer"><a href="https://t.me/whitedns/1626" target="_blank">📅 18:35 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-1618">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XmwD-wFbbgZPn7-_9LgFYQHDRWJuPYjIsJsveuKf1JajRgN2KB9ojdpUem63ftbM0rcer3oSf649zs4qUqgvP_2C3DSCa_Wv7zf_nWyar0dMQSNVDIoUBr0STaLILKleSJg8zssOEsk3cvpldNinU99FOhQ_4r09sVW4zqIMQ-7ygSlbbCZUnEP3QMCP3rNZPnqbeBqJni0FxqKGASUR6-hJqWR0MYW0wYnvwCEq5kPvyxWoJeLUzibnHELuCyeEXu7TfwjOk6G-4Fmij9pO77BTPHuZAxmMRkS4h8DUq_zoKsOBmGlz7gravWqro06177_BkeWsB5QS_E0-svAFXQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👑
یک پورت برای حکومت بر همه!
آموزش نصب و راه‌اندازی CottenRouter
🇺🇦
تماشا در یوتیوب
https://youtu.be/N725_-A_-B8
اگر روی یک سرور چند DNS Tunnel مختلف داشته باشید، خیلی زود به یک مشکل می‌خورید: همه‌شون پورت عمومی 53 رو می‌خوان.
سرویس CottenRouter دقیقاً برای حل همین مشکل ساخته شده. جلوی تمام سرویس‌ها قرار می‌گیره، دامنه هر درخواست رو تشخیص می‌ده و بدون دست‌کاری Packet، اون رو به Backend درست می‌فرسته.
یعنی می‌تونید CottenDNS، MasterDnsVPN، StormDNS، thefeed و سرویس‌های مدیریت‌شده با SlipGate رو هم‌زمان روی یک سرور و یک IP اجرا کنید؛ بدون جنگ بر سر پورت 53.
✍️
توی این ویدیو می‌بینیم:
• سرویس CottenRouter دقیقاً چه مشکلی رو حل می‌کنه
• مسیریابی درخواست‌ها بر اساس Domain چطور انجام می‌شه
• چطور چند DNS Tunnel روی یک IP اجرا می‌شن
• پشتیبانی از DNS، DoT و HTTPS
• تفاوت نصب مستقیم با Docker
• پنل مانیتورینگ، محدودسازی ترافیک و قابلیت‌های امنیتی
• نحوه نصب و اتصال Backendها
سرویس CottenRouter هیچ Label یا داده اضافه‌ای وارد Packet نمی‌کنه؛ پس فضای قابل استفاده Tunnel و MTU رو هم کاهش نمی‌ده.
🇺🇦
تماشا در یوتیوب
https://youtu.be/N725_-A_-B8
🔗
سورس‌کد و راهنمای نصب:
https://github.com/TaJirax/CottenRouter
اگر با DNS Tunnelها کار می‌کنید، این پروژه احتمالاً کلی دردسر از مدیریت سرورتون کم می‌کنه.</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/whitedns/1618" target="_blank">📅 15:13 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-1616">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">🔭
یک خبر خوب برای کاربران WhiteVPN
🟢
یک فیلتر جدید به سابسکریپشن
اپلیکیشن ‌های
WhiteVPN اضافه کردیم تا کانفیگ‌هایی که هنگام استفاده از ChatGPT و سرویس‌های OpenAI خطا ایجاد می‌کردند، به‌صورت خودکار از لیست حذف شوند.
🟢
از این به بعد، با تمام کانفیگ‌های موجود در سابسکریپشن باید بتوانید بدون دردسر به ChatGPT و سایر سرویس‌های OpenAI دسترسی داشته باشید.
🟢
برای دریافت لیست جدید، کافی است سابسکریپشن WhiteVPN را یک‌بار به‌روزرسانی کنید.</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/whitedns/1616" target="_blank">📅 11:52 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-1610">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/M1hWinW0GwkNvjDlMVTr4jgAa456rw_RAtaaSMMVZbkesBWnHZNYWkZPG0RpThJry5DHH9h3OkJo9S0J8Q6mo_U-_JsaCevHwLaFID-U0vA59l6PXVbdBTSIMRRK2vI9mz5dbMl2O1MOne-7OkVbiZEsnzhdhzf6-xa9KsQSr3kqmstu_07_zzCKcSP9XQlgIzADhUJhGyVJYUScx7M0bwFtc56CvDuPkDV3T97ByHeXR9oOpTe5lBXmIgR7FACPZGGrl5WB_E40XUL0IWMNiP2XLF_ssZYetPfq_Gc2fVRFIsI_ap-j99TAt3sZGvUkECXkqymExfHbGXS6S5zj1Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">Whitedns Chatbot V4 (جدید)
🎉
🎉
🎉
@WhiteDnsResponder_bot
راهنمای استفاده از ربات WhiteDNS
سلام!
این ربات به شما کمک می‌کند پاسخ سوال‌های مربوط به WhiteDNS، ابزارهای اتصال، DNS، نصب برنامه‌ها و رفع مشکلات رایج را از میان مطالب منتشرشده پیدا کنید.
آموزش :
⚠️
👇
### ۱. پرسیدن سوال معمولی
💬
کافی است سوالتان را مستقیماً برای ربات بنویسید.
نمونه‌ها:
- چطور WhiteDNS را روی اندروید نصب کنم؟
📱
- آخرین نسخه برنامه چیست؟
- چرا DNS وصل نمی‌شود؟
🌐
- تنظیمات ویندوز را چطور انجام بدهم؟
🖥
برای دریافت پاسخ بهتر، نام برنامه، دستگاه یا سیستم‌عامل و متن دقیق خطا را در یک پیام بنویسید.
ربات ممکن است همراه پاسخ، دکمه‌های منبع را نیز نمایش دهد. با انتخاب آن‌ها می‌توانید مطلب اصلی کانال را مشاهده کنید.
📎
### ۲. عیب‌یابی مرحله‌ای با /diagnose
🔧
اگر مشکل فنی دارید و نمی‌دانید چطور آن را توضیح دهید، دستور زیر را انتخاب کنید:
/diagnose
ربات از شما سه مورد کوتاه می‌پرسد:
1. نوع مشکل، مانند وصل نشدن، سرعت پایین، DNS یا نصب
2. دستگاه یا سیستم‌عامل
3. توضیح کوتاه مشکل یا متن دقیق خطا
پس از دریافت راه‌حل، این گزینه‌ها نمایش داده می‌شوند:
-
✅
حل شد — اگر مشکل برطرف شده است.
-
🔁
راه دیگر — دریافت یک راه‌حل جایگزین.
-
👤
ارسال برای مدیر — آماده‌کردن گزارش برای مدیران.
برای جلوگیری از طولانی‌شدن مراحل، ربات فقط یک راه‌حل جایگزین ارائه می‌دهد.
### ۳. ارسال نتیجه عیب‌یابی برای مدیر
اگر راه‌حل‌های ربات مؤثر نبودند، گزینه ارسال برای مدیر را انتخاب کنید.
قبل از ارسال، ربات پیش‌نمایشی شامل موارد زیر نشان می‌دهد:
- نوع مشکل
- دستگاه یا سیستم‌عامل
- توضیح شما
- راه‌حل‌هایی که امتحان کرده‌اید
- نام تلگرام
- نام کاربری، در صورت وجود
- شناسه عددی کاربر و گفتگو
- زبان حساب تلگرام
درخواست فقط بعد از انتخاب تأیید و ارسال برای مدیران فرستاده می‌شود.
### ۴. جستجوی مستقیم با /search
برای پیدا کردن مطالب کانال بدون ساخت پاسخ جدید، از این دستور استفاده کنید:
/search عبارت موردنظر
مثال:
/search نصب WhiteDNS اندروید
ربات نزدیک‌ترین مطالب را همراه دکمه مشاهده منبع نشان می‌دهد.
### ۵. ارسال پیام مستقیم به مدیران با /contact
اگر موضوع شما با عیب‌یابی قابل حل نیست، دستور زیر را انتخاب کنید:
/contact
سپس تمام توضیحات خود را در یک پیام کامل بفرستید. بهتر است پیام شامل این موارد باشد:
- نام برنامه
- دستگاه یا سیستم‌عامل
- نسخه برنامه
- نوع اتصال
- متن دقیق خطا
- کارهایی که قبلاً امتحان کرده‌اید
مدیران اطلاعات حساب تلگرام و پیام کامل شما را دریافت می‌کنند و می‌توانند از طریق ربات یا گفتگوی مستقیم پاسخ دهند.
شماره تلفن شما برای ربات قابل مشاهده نیست، مگر اینکه خودتان آن را داخل پیام ارسال کنید.
### ۶. ادامه سوال قبلی
ربات می‌تواند برای مدت کوتاهی ارتباط بین سوال‌های شما را تشخیص دهد.
مثال:
- پیام اول: «روش نصب WhiteDNS چیست؟»
- پیام بعدی: «برای اندروید چطور؟»
این زمینه گفت‌وگو حداکثر ۳۰ دقیقه و تا چهار نوبت نگه داشته می‌شود و به‌عنوان منبع واقعی پاسخ استفاده نمی‌شود.
### ۷. شروع گفت‌وگوی تازه با /new
اگر می‌خواهید موضوع قبلی فراموش شود، از این دستور استفاده کنید:
/new
این دستور زمینه موقت گفت‌وگو و عملیات نیمه‌تمام را پاک می‌کند.
### ۸. ثبت بازخورد
زیر پاسخ‌های ربات دو گزینه وجود دارد:
-
✅
مفید بود
-
❌
مفید نبود
بازخورد شما به مدیران کمک می‌کند پاسخ‌ها و مطالب ربات را بهتر کنند.
همچنین می‌توانید برای آخرین پاسخ از دستور زیر استفاده کنید:
/feedback
### ۹. لغو عملیات با /cancel
برای خروج از ارسال پیام، عیب‌یابی یا پاسخ‌دادن به یک درخواست فعال، بنویسید:
/cancel
فهرست دستورات
- /start — شروع کار با ربات
- /help — نمایش راهنما
- /diagnose — عیب‌یابی مرحله‌ای
- /search — جستجوی مستقیم در مطالب
- /feedback — ثبت بازخورد برای آخرین پاسخ
- /contact — ارسال پیام به مدیران
- /new — شروع گفت‌وگوی تازه
- /cancel — لغو عملیات فعال
محدودیت استفاده
برای کنترل هزینه و حفظ کیفیت سرویس:
- حداکثر ۳ درخواست هوش مصنوعی در هر ۵ دقیقه
- حداکثر ۵۰ درخواست هوش مصنوعی در روز
دستورهای ساده مانند /help، /search، /contact و بازخورد شامل این محدودیت هوش مصنوعی نمی‌شوند.
نکات مهم
- برای پاسخ دقیق‌تر، همه جزئیات مشکل را در یک پیام بنویسید.
- پاسخ‌ها بر اساس مطالب موجود WhiteDNS تولید می‌شوند و ممکن است برای مشکلات خاص کامل نباشند.
- در صورت حل‌نشدن مشکل، از مسیر عیب‌یابی و سپس ارسال گزارش برای مدیر استفاده کنید.
@whitedns</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/whitedns/1610" target="_blank">📅 11:03 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-1608">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">"exit chain "
⚠️
✍️
راهنمای استفاده از
#exit_chain
در اپ whitevpn# اندروید
ساب را وارد کن - برو تنظیمات - برو زنجیره اتصال - برو افزونه بعد - اشتراکی که وارد کردی را از اون بالا انتخاب کن - یک تست اتصال بگیر - یکی از کانفیگ ها را انتخاب کن - وصل شو -
تمام
✅
راهنمای استفاده از
#exit_chain
در اپ whiteaesther# اندروید
📱
برو route - گزینه exit chain را روشن کن - یا ساب و یا کانفیگ را وارد کن - برگرد صفحه اول و وصل شو -
تمام
✅
راهنمای استفاده از
#exit_chain
در اپ whiteaesther# دسکتاپ
برو advanced - برو exit chain - ساب و یا کانفیگ را وارد کن - برگرد simple - کانکت را بزن - تمام
✅
👨‍💻
این سه پست را مطالعه کنید :
https://t.me/whitedns/1601
https://t.me/c/3869114465/152008
https://t.me/c/3869114465/151806</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/whitedns/1608" target="_blank">📅 10:19 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-1605">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/F9p3l3oxHRpFu63r-bOzva6ZVpk6XezV54QWJCqgi7X5P0IKDwHv8O6Ypc4F9w4cD7lXRxxpX-oi3zVHJbSM_hMyIA0Z_XfayeIj7jIIez6If2HeLmdo5hXUyTGUwlWX3A6Tzl18EYJ9-nQ6FTB7yZwrT7s2f3ZOzObj5OsuqTHpbY_ht2UzPLtQBeZ4l6_2-OIuWYo1YroM9Nx0ygZIRwYcG8u3V_xaVoERFbeURVzd12-vxxv4TyllIXOwOWwRjwSriAii-hBFQ8O6FzsSda4XxipG0DleNuu_jwRsMUCyN93Z712vmshin5rBRaETHcEA3WydJH0fPCllvS56yw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔗
Wh
iteAesther
✍️
نسخه ۱.۲.۲  برای اندروید منتشر شد !
— موتور جدید و چند قابلیت
این آپدیت موتور تونل رو عوض می‌کنه و چند چیزی که کاربرها خواسته بودن اضافه می‌شه.
🟢
⚡️
موتور جدید (Aether 1.7.0)
▫️
مصرف حافظه محدود شد
— قبلاً هرچی اتصال طولانی‌تر می‌شد، حافظه‌ای که اپ می‌گرفت بیشتر می‌شد تا جایی که تونل می‌افتاد. حالا سقف داره.
▫️
WARP in WARP وقتی یک طرفش قطع بشه دوباره وصل می‌شه
به‌جای اینکه کلاً بمیره.
▫️
پیام خطای واقعی از Cloudflare
— اگه ثبت‌نام رد بشه، حالا می‌گه دلیلش چیه: آی‌پی علامت‌خورده، یا ثبت‌نام زیاد از این آدرس. قبلاً فقط می‌گفت شبکه مشکل داره.
✍️
نودهای hysteria2 و tuic توی Exit chain کار می‌کنن
اگه توی ساب‌تون نود hysteria2 یا tuic دارین و تا حالا هیچ‌وقت بالا نمی‌اومدن، دلیلش پیدا شد و درست شد.
✍️
ولی یک شرط داره:
باید پروتکل رو روی
WireGuard
بذارین (از
Routes ← Manual ← Protocol
).
روی MASQUE همچنان کار نمی‌کنه و این دست ما نیست — محدودیت خود Cloudflareست. اپ هم اگه ببینه روی MASQUE هستین بهتون می‌گه.
🟢
نودهای REALITY حالا مشخص می‌شن
اگه توی ساب‌تون نود REALITY دارین، قبلاً یا اصلاً نمی‌اومد یا می‌اومد و وصل نمی‌شد و معلوم نبود چرا. حالا با برچسب نارنجی
not supported
نشون داده می‌شه و قابل انتخاب نیست.
نود سالمه — موتور فعلی هنوز نمی‌تونه باهاش احراز هویت کنه. وقتی بتونه، خودبه‌خود دوباره کار می‌کنه.
🟢
اشتراک تونل با شبکه (LAN sharing)
می‌تونین تونل گوشی رو با بقیه دستگاه‌های همون وای‌فای به اشتراک بذارین — مثلاً لپ‌تاپ یا تلویزیون.
از
Traffic
حالت رو روی
Proxy
بذارین، بعد بخش Advanced رو باز کنین و
Share with this network
رو روشن کنین. اپ آدرسی که باید توی دستگاه دوم بزنین رو بهتون نشون می‌ده.
⚠️
رمز اختیاریه ولی حواستون باشه:
بدون رمز، هرکی روی اون وای‌فای باشه می‌تونه از تونل شما استفاده کنه و ترافیکش با هویت شما بیرون می‌ره. روی شبکه خونه خودتون مشکلی نیست؛ توی کافه و هتل و خوابگاه حتماً رمز بذارین.
🟢
صفحه اول: آی‌پی و مصرف
•
آی‌پی قبل و بعد از تونل
— که ببینین واقعاً عوض شده
•
سرعت لحظه‌ای دانلود و آپلود
و مجموع مصرف هر نشست
نکته: آی‌پی «بدون تونل» فقط وقتی خونده می‌شه که اپ باز باشه و وصل
نباشین
. اگه مستقیم بزنین connect، اون خونه خالی می‌مونه — این عمدیه، چون خوندنش وسط اتصال یعنی فرستادن آدرس واقعی‌تون از کنار همون تونلی که قراره مخفی‌ش کنه.
🟢
کلید روشن/خاموش توی پنل سریع
از
Settings
دکمه
Add a quick settings tile
رو بزنین. بعدش از پنل بالای گوشی بدون باز کردن اپ وصل و قطع می‌شین.
🟢
مشکل «Allow background running» که نمی‌رفت
روی بعضی گوشی‌ها (مخصوصاً شیائومی) هرچی اجازه می‌دادین، اون کارت باز هم می‌موند. دلیلش این بود که این گوشی‌ها تنظیم باتری خودشون رو دارن و اجازه رو فقط اونجا ثبت می‌کنن، ولی جواب استاندارد اندروید همچنان «نه» می‌مونه.
حالا اپ خودش می‌فهمه این اتفاق افتاده، شما رو می‌فرسته به تنظیمات درست گوشی، و یک دکمه
I've done this
داره که کارت رو ببنده.
📥
دانلود
https://github.com/WhiteDNS/WhiteAestherMobile/releases/latest
▫️
arm64-v8a
(۵۴ مگ) — تقریباً همه گوشی‌های ۲۰۱۷ به بعد. از این شروع کنین
▫️
armeabi-v7a
(۴۸ مگ) — گوشی‌های قدیمی‌تر
▫️
universal
(۱۵۷ مگ) — اگه مطمئن نیستین
اگه مشکلی خوردین، از
Settings ← Diagnostics
گزارش بگیرین و بفرستین.
تیم وایت
@whitedns</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/whitedns/1605" target="_blank">📅 08:01 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-1603">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/Qr_Oug8qM_XyrWrRXO1uRR7xSqKSkQZ8rhaBE-Zz_13tN5Pe_77vZMSVdDUJM183DOm08w4609KRivk1TwM3Qdo-oUj5e0uRGi9CfkFt-p303rxvsv7kNIn0ElKi9_aRcgF_T7Kleda_zp3IFRwJGN0PcG1grzfiCOEvijym8tw4lWJwiokmrTJ8JSvFV1i9Id1660qDLmKgXACdFkju6KBfNVGRbD6YVHJWQ_AbKwjlBXSREr7i4zb0eIQkr0SozWxhpUrZi8LuC0bjRBsYPKojYLppFVzH-kBvZMrd0dO6UbsEqzSghanyNjx6DWdxnOjeLIVpfDKUpK8dmqsLkw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✍️
آپ
دیت جدید وایت‌استر برای دسکتاپ (WhiteAesther) منتشر شد!
نسخه:
v1.5.4
در این نسخه تغییرات بسیار جذاب و کاربردی برای راحتی بیشتر شما به برنامه اضافه شده است.
🔭
تغییرات این نسخه:
🟢
اشتراک‌گذاری اتصال در شبکه داخلی (LAN Share)
از این پس می‌توانید اتصال VPN فعال روی سیستم خود را به راحتی با سایر دستگاه‌های متصل به مودم یا شبکه (مثل گوشی موبایل، تلویزیون هوشمند یا لپ‌تاپ‌های دیگر) به اشتراک بگذارید!
🟢
نمایش هوشمند وضعیت گره‌ها (پشتیبانی بهتر از Node ها)
مشکل عدم نمایش وضعیت یا کار نکردن بی‌دلیل گره‌ها برطرف شد. حالا گره‌هایی که برنامه به هر دلیلی نمی‌تواند از آن‌ها استفاده کند (مثلاً نیاز به WireGuard دارند یا از پروتکل REALITY پشتیبانی نمی‌کنند) با
رنگ نارنجی
مشخص می‌شوند. با نگه‌داشتن نشانگر موس روی آن‌ها، می‌توانید دلیل دقیق عدم پشتیبانی را ببینید.
🟢
بهبود مسیریابی کل سیستم (Whole Machine)
(تغییرات نسخه 1.5.3)
حالت System Proxy حالا به درستی ترافیک کل سیستم را از طریق مسیر زنجیره‌ای فعال (Active Chain) شما عبور می‌دهد.
🔭
راهنمای استفاده از قابلیت LAN Share (اشتراک اینترنت با گوشی و
تلویزیون):
۱. در برنامه به بخش
Settings
(تنظیمات) بروید و تب
Traffic & DNS
را باز کنید.
۲. گزینه
"Share this connection on my network"
را فعال کنید.
۳. برنامه به شما یک
آدرس (IP)
و یک
پورت
(مثلاً 1080) نمایش می‌دهد.
۴.
امنیت اتصال:
در همین بخش می‌توانید یک
نام کاربری (Username)
و
رمز عبور (Password)
تعیین کنید تا فقط خودتان بتوانید به آن وصل شوید.
(
⚠️
توجه: اگر این دو کادر را خالی بگذارید، هر دستگاهی در شبکه وای‌فای شما می‌تواند بدون رمز از اینترنت آزاد سیستم شما استفاده کند).
۴. حالا وارد تنظیمات پروکسی (HTTP یا SOCKS5) در گوشی، تلگرام یا تلویزیون خود شوید، آی‌پی و پورت نمایش داده شده را وارد کنید و روی اتصال ضربه بزنید.
(نکته: در اولین استفاده از این قابلیت، فایروال ویندوز از شما یک تاییدیه می‌خواهد که باید روی گزینه
Allow Access
کلیک کنید تا پورت شبکه باز شود).
✍️
هم‌اکنون می‌توانید برنامه خود را به آخرین نسخه به‌روزرسانی کنید.
https://github.com/WhiteDNS/WhiteAesther/releases/latest
#آپدیت
#وایت_استر
#WhiteAesther
#پروکسی
#تونل
تیم وایت
@whitedns</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/whitedns/1603" target="_blank">📅 07:11 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-1602">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/qdjYTYJMDPCEkb0wyvrkB86V8yAsDazHAhHR0mo56CKJfWrswN9mnyYN9tpk_NyI7A7DBizRrAsmq2YF4WQqvPBriJ7moN2h2S-WWcUM_wCnkc4qr26ggUE1-coZjXuE9BSvl3pCmmTkr9BziWnl-3N8wztGULp5F7V_IfIRDF2tHtuJ5diKljTOUU4oArUAuSH5ZHqAYx5MJcbuxyIvC68LQjJZP4pIYBU2bjIHmbDvKlixzo5je-RYNIl-GxZfphZiF3BxJyEYHhuUgZ8lKITrxl2DUoLKGBA1nhzgTqwER0Zm3lU8zYg9osTDU6YdNFUTj_d9YeGmsZAOwx5-Xw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🌎
نسخه جدید موبایل و دسکتاپ به زودی منتشر می‌شود!
این نسخه‌ها شامل چه مواردی است؟
🟢
بهبود عملکرد اتصال برنامه
🟢
ارتقا موتور به ۱.۷.۰
🟢
اضافه کردن امکان LAN sharing
🟢
رفع باگ
🟢
در اندروید امکان اضافه شدن به Quick setting
🟢
استفاده از wireguard و hysteria exit chain برای داشتن حداکثر سرعت
ممنون
@WhiteDNS
🔥</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/whitedns/1602" target="_blank">📅 19:51 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-1601">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/MSe9xQXL93swqq6rk8CNLGjgPffPcFyVIHPhpMM2k90EF8ndQf9m-Rp1RuZc2Eu-p7f0hRRMbb9AfhmiXDDqMO5vhvJfDWcr4KCcYHWbA73x73CV1ABIk6L11QQdqGhoKnpogR6mKG1KBs1H5NE1m64yYKx0o95s7-tmT8RzitpZySvfXXVeCiFZsO8_H_PEaLGxXDdZyXZrw0vPEElp-aASl_GGODS8p_x-QTtX_hOu0KDKpK3LuAM_lj0o0HasUN9P8pbaYauv8wcrnxwhdtkuofpvlfKvCFHi2mACdI169mAGQU-19B8Iy5FPdyK-9cgN-vFAGgGc5oSRoR5bRg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مهم
⚠️
⚠️
⚠️
⚠️
⚠️
دوستان :
پست  را با دقت مطالعه کنید
https://t.me/whitedns/1568
این کانفیگ های برای قابلیت "exit chain" توی اپ whiteaester و whitevpn هست - که ip شما را ثابت میکنه و یک لایه امنیت بیشتر به شما میده چون TLS هست
چون خیلی از دوستان کانفیگ نداشتن و یا نگران امنیتشون بودند ما این امکان را فراهم کردیم .
این کانفیگ ها برای استفاده مستقیم در اپ هایی مثل v2rayng و غیره نیست، اگر قصد استفاده مستقیم دارید لطفاً درخواست ارسال نفرمایید
تشکر
@whitedns</div>
<div class="tg-footer">👁️ 6.49K · <a href="https://t.me/whitedns/1601" target="_blank">📅 17:15 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-1600">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/nkjEC2KjT7rvdf71nVXUs6ymTxCfN5Nmu1xvkQwp-gaSt6OdOb7TvrY3hMQbNMB4ShsJlYAioWKCCO7edqCbKIDKbdMeTgx-kmwB-gU84AvN4u9il9kFqgi4w6PY0DGeoxHB1EwzLzdwAYE9-udsUYG_wBAonXHHdKsMfbjRkLec0IpWlIDf70wYttLHTqAcY6E6OKIOAYY8AmPJ8OestQQirf4t1bGITk3UHKKkJB5qydc3nys6FZ1cFJtM0t-QnJEtFYRAv49FjIpEdW-PG7BEYUZpqLQ6tWwWvFJVLyq37Oqe--B0BDdVeTDbbj_loRoxfhWibhhyWsOS9IiGAA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📢
راهنمای کامل استفاده از ربات WhiteDnsChain
(کانفیگ هسته x-ray )
نکته : این ربات یک کانفیگ اضطراری برای شما ایجاد میکند تا در موارد خیلی خاص از ان استفاده کنید . کانفیگ های این ربات برای امکان exit chain در اپ های white ایجاد شده و هر گونه سواستفاده از آن مجاز نیست
🤖
آدرس ربات:
@WhiteDnsChainbot
برای دریافت و مدیریت اتصال اختصاصی خود مراحل زیر را انجام دهید:
1️⃣
شروع و انتخاب زبان
- وارد ربات شوید.
- دستور /start را ارسال کنید.
- گزینه «
🇮🇷
فارسی» را انتخاب کنید.
- برای تغییر زبان در آینده از گزینه «
🌐
تغییر زبان» استفاده کنید.
2️⃣
درخواست کانفیگ
- روی «
🔐
دریافت کانفیگ» بزنید یا دستور /config را ارسال کنید.
- درخواست شما برای مدیر فرستاده می‌شود.
- پس از تأیید، یک پیام اطلاع‌رسانی دریافت می‌کنید.
- دوباره /config را بزنید تا لینک اشتراک و QR اختصاصی شما نمایش داده شود.
3️⃣
اضافه‌کردن کانفیگ به برنامه
- یک برنامه سازگار با V2Ray/Xray روی دستگاه خود نصب کنید.
- لینک اشتراک را کپی کنید.
- در برنامه گزینه افزودن Subscription یا «افزودن اشتراک» را انتخاب کنید.
- لینک را وارد کرده و اشتراک را به‌روزرسانی کنید.
- یکی از سرورها را انتخاب کرده و اتصال را فعال کنید.
4️⃣
مشاهده وضعیت حساب
از گزینه «
👤
حساب من» یا دستور /account استفاده کنید تا موارد زیر را ببینید:
- وضعیت فعال یا غیرفعال
- تاریخ انقضا
- حجم مصرف‌شده
- حجم کل
- محدودیت تعداد دستگاه یا IP
5️⃣
دریافت دوباره کانفیگ
اگر پیام کانفیگ را پاک کردید، نگران نباشید. با /config همان کانفیگ اختصاصی دوباره نمایش داده می‌شود و کانفیگ جدیدی ساخته نخواهد شد.
6️⃣
پشتیبانی
- روی «
💬
پشتیبانی» بزنید یا /support را ارسال کنید.
- مشکل خود را در یک پیام کامل توضیح دهید.
- پیام مستقیماً برای مدیر ارسال می‌شود.
- پاسخ مدیر را داخل همین ربات دریافت خواهید کرد.
7️⃣
دستورات کاربردی
- /start — شروع و انتخاب زبان
- /config — دریافت کانفیگ
- /account — مشاهده وضعیت حساب
- /menu — نمایش منوی اصلی
- /support — ارتباط با پشتیبانی
- /help — نمایش راهنما
⚠️
نکات مهم
⚠️
-درخواست ها توسط ادمین دونه دونه بررسی و تایید میشود پس لطفا صبور باشید
- ادمین کاملا مختار است که به هر دلیل ممکن از ارایه کانفیگ به شما خودداری کند پس لطفا اعتراض نکنید
⚠️
-در حال حاظر کانفیگ ها با محدودیت 1 روزه و یک گیگ هست
- لینک و QR کاملاً اختصاصی است؛ آن را برای دیگران ارسال نکنید.
- هر حساب تلگرام فقط یک کانفیگ فعال دریافت می‌کند.
- ارسال چندباره /config کانفیگ تکراری ایجاد نمی‌کند.
- برای امنیت بیشتر، پس از دریافت کانفیگ می‌توانید پیام آن را با گزینه «
🗑
مخفی کردن» حذف کنید.
- در صورت پایان حجم یا اعتبار، از طریق پشتیبانی با مدیر ارتباط بگیرید.
@whitedns</div>
<div class="tg-footer">👁️ 9.43K · <a href="https://t.me/whitedns/1600" target="_blank">📅 17:14 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-1599">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromMasterDnsVPN</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/f1ZRTyymXdHHaLkwCAIDx1C24e6j8huNGJzlHt2v1YrkcDAIlbXU7QH8TJ6oL4iwm-DKCBABM31Ugaa1TCIhthBbliUV2KN9ZIGbiUL9xYX6RJhtxAmq9_8Z3VwKv8YkKcTySrqI4UmqBfn_hzzmCgaWsE7nycPK7R4YacnJGg1rwnESQHmE4c7GEcDH56vegxluu-hDedroucrFqRXj1q2iWT-BbzVv0-PrYe70o5clgF2Am8268fR261anVZWw5itmbqGR3lcGrHU3m1ZX9Aq0v7dncW_AhKyMsISllpgSn0PfV-AVg82ysw7t8GP-KiU3sMiWijmcu7YiaBHiOg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👋
درود،
◀️
آموزش رفع مشکل خطای
Sign-in failed: failed to start login server: An attempt was made to access a socket in a way forbidden by its access permissions. (os error 10013)
مربوط به برنامه ChatGPT در ویندوز
◀️
ابتدا در منوی استارت خود کلمه cmd را سرچ کنید.
◀️
سپس روی آن راست کلیک و Run as Administrator را بزنید.
◀️
در نهایت دستورات زیر را وارد کنید و Enter بزنید.
net stop winnat
net start winnat
✅
مشکل شما رفع میشود.
❤️
پیروز و سربلند باشید.
🤨
با تشکر فراوان،
امین محمودی
🗓
3 شهریور ماه 1405
🛡
کانال:
@MasterDnsVPN
💬
گروه:
@MasterDnsVPNGroup
#chatgpt
#هوش_مصنوعی
#رفع_مشکل</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/whitedns/1599" target="_blank">📅 16:03 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-1598">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromMasterDnsVPN</strong></div>
<div class="tg-text">👋
درود،
⚠️
یک پروژه هست، دوستان معرفی کردن، من تایید یا رد نمیکنم، فقط منتشر میکنم، خوب بودن و نبودنش با خودتون، من خیلی چک نکردم.
◀️
پروژه واسه جمع کردن کانفیگ های v2ray هست.
👩‍💻
0xRadikal/Free-v2ray-Configs
◀️
تفاوت اصلی پروژه با بقیه ریپوهای کانفیگ رایگان اینه که صرفاً کانفیگ‌ها رو از منابع مختلف جمع نمی‌کنه. کانفیگ‌ها وارد یک pipeline چندمرحله‌ای می‌شن، duplicateها حذف می‌شن، ساختار و endpoint بررسی می‌شه، اتصال TCP تست می‌شه و در نهایت کانفیگ با یک درخواست HTTP واقعی از طریق proxy در ۳ دور مستقل تست می‌شه.
◀️
در حال حاضر پروژه از ۲۱ منبع تغذیه می‌شه و در آخرین اجرای ثبت‌شده:
🔴
۱۱٬۴۱۵ کانفیگ یکتا جمع‌آوری شده
🔴
۲٬۴۰۳ کانفیگ در هر ۳ دور تست موفق بودن و وارد بخش
verified
شدن
🔴
خروجی‌های
verified
،
fast
،
secure
و
top100
تولید می‌شه
🔴
خروجی برای V2Ray/Xray، Clash و sing-box ارائه می‌شه
🔴
کل سیستم هر ۱۵ دقیقه به‌صورت خودکار به‌روزرسانی می‌شه
✅
به گفته ناشر: هدف پروژه اینه که این پروژه تبدیل به یک منبع متن‌باز و قابل‌اعتماد برای کانفیگ‌های رایگان بشه، مخصوصاً برای کاربران ایرانی.
🔴
نمونه همینکار رو هم WhiteDns انجام داده، اینجا میتونین ببینین:
👩‍💻
WhiteDNS/subs-check
🔴
اگر از این پروژه خوشتون اومد میتونین با
⭐️
دادن داخل گیت هاب از ناشر این برنامه حمایت کنین.
⚠️
نکته تکمیلی از سمت خودم: اگر از Vless/Vmess و هر فیلترشکن رایگانی استفاده میکنین، اگر امنیت اطلاعاتتون مهمه، حتما از حالت Chain و ... استفاده کنین، یعنی به وسیله اون VPN به یه VPN دیگه به سرور خودتون وصل بشید و Vmess/Vless سرور خودتون رو داشته باشید، از سرورهای رایگان برای فیلتر نشدن و ... استفاده کنین (البته که من کلا پیشنهاد میدم، VPN رایگان تا حد امکان استفاده نکنین و سرور خودتون رو راه اندازی کنین، اما این سرویس ها ممکنه، برای بعضی ها کاربردی باشه)، اما برای امنیت بیشتر اینکار رو انجام بدید.
❤️
پیروز و سربلند باشید.
🤨
با تشکر فراوان،
امین محمودی
🗓
1 شهریور ماه 1405
🛡
کانال:
@MasterDnsVPN
💬
گروه:
@MasterDnsVPNGroup
#v2ray
#معرفی_پروژه
#اینترنت_آزاد
#فیلترشکن
#vless
#vmess</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/whitedns/1598" target="_blank">📅 09:55 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-1597">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JbmGneUw1ZVg5yDVmWjA_IgNTcQLWtv8LsyoLunWzc4WJnWwHEtlojemxbgII5PdkP_hLw-RsEY4Auifbgl0SD3YuStLI1U4GvU0UTr9NK5vRlWWyPwXDqcBsXFz-Ee0UV-kszJ0ir9thCrkxkyB21fV4aJ55ZGoz-JLFyHGORkqLy8O7D2ska0ks60bJ7cK-DUFlGcdTaCjAIvMdurzoKWW8p3pM1PRNYyP02XMx0Zz6E7WPcJStrWOOGxby2IL8EyoY3C66IWEcWvwJmpON7HLqDX6_Cysq9krNUIv090RYmBk6R4y6keGFd57ZUf2G6JcPhGgIe5Rkwkdt8MQIg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📱
برای آیفون اپلیکیشن نداریم؟ چرا، داریم!
اگر از کاربران iOS هستید، می‌توانید از اپلیکیشن
Core Forge
استفاده کنید؛ یک اپلیکیشن کامل که سه قابلیت اصلی را یکجا در اختیارتان قرار می‌دهد:
🔹
اتصال VPN
🔹
استفاده از MasterDNS, CottonDNS
🔹
اتصال از طریق پروتکل Aesther
دیگر لازم نیست برای هرکدام از این قابلیت‌ها یک اپلیکیشن جدا نصب کنید؛ همه‌چیز داخل
Core Forge
در دسترس است.
📥
دریافت Core Forge برای iPhone
🎥
تماشا ویدیو آموزشی در یوتیوب
🔥
لینک ساب WhiteVPN برای استفاده در اپ</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/whitedns/1597" target="_blank">📅 08:00 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-1596">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">📹
آموزش اپلیکیشن WhiteVPN کامپیوتر و استفاده اپ داخل
🍏
آیفون برای کاربران IOS
https://youtu.be/tm0ls3r4ppw</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/whitedns/1596" target="_blank">📅 01:40 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-1594">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">🔭
در ۳۰ روز گذشته، بیش از ۷۰۰ هزار اتصال موفق در اپلیکیشن WhiteVPN ثبت شده.
خوشحالیم که در این مسیر کنار شما هستیم.
🕊️
به امید روزی که همه به اینترنت آزاد دسترسی داشته باشیم و از WhiteVPN فقط برای حفظ امنیت و حریم خصوصی استفاده کنید، نه برای عبور از فیلترینگ.</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/whitedns/1594" target="_blank">📅 14:42 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-1593">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">🌎
انتشار نسخه ۱.۶.۲ WhiteDNS برای اندروید</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/whitedns/1593" target="_blank">📅 14:36 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-1589">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">WhiteVPN-V1.6.2-armeabi-v7a.apk</div>
  <div class="tg-doc-extra">34.2 MB</div>
</div>
<a href="https://t.me/whitedns/1589" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/whitedns/1589" target="_blank">📅 14:36 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-1588">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jtgKppRzTAVrI8Oawbza4tKWSXZsoK6vaMCF01-7KsOgl53CD3FoA7xKNW2X_mEe-9-1N1I3iAC-b8bKb3NKwskKoyIdB5Qjmenz9f-qJF5OGj6GjLuYgTKtsJOSXgO11nDWdrRnC4iSadY9U3MXuCbgSV0B8-jpIg6xZJZD_GoWCTzCqItpXzmqVPM90EBNli0hMG2OxwbO1v4wEEL2b3bxGbkBFGgXLsVO2E_mwd_-FpEvhnlEQ_j0-N8Lspq1eZT65ClQBU-EOnEFbEqNgJ7AxRGTh0jwv-n4X_aMnkOMwlkYbiLEbFAPiXjJnG_4dsDGHy_LA6OJL5CUjkFAbg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚀
WhiteVPN 1.6.2
✍️
این نسخه اتصال WhiteVPN را سریع‌تر و پایدارتر می‌کند و چند بهبود مهم برای سابسکریپشن‌ها، تنظیمات و Split Tunneling دارد.
✍️
تغییرات مهم
• اتصال مجدد خودکار، سریع‌تر و قابل‌اعتمادتر شده است.
• در صورت بروز مشکل در اتصال، برنامه بهتر و امن‌تر آن را بازیابی می‌کند.
• بررسی سلامت اتصال و مدیریت تغییرات شبکه بهبود یافته است.
• هنگام قطع اتصال، وضعیت واقعی عملیات نمایش داده می‌شود و برنامه تا توقف کامل اتصال در حالت «در حال قطع اتصال» باقی می‌ماند.
• مدیریت و ذخیره‌سازی سابسکریپشن‌ها پایدارتر شده است.
• فایل‌های خراب سابسکریپشن به‌صورت خودکار شناسایی و دوباره دریافت می‌شوند.
• آخرین نسخه سالم سابسکریپشن برای مواقعی که دریافت نسخه جدید ممکن نیست، حفظ می‌شود.
• پشتیبانی از لینک‌ها و کانفیگ‌های SOCKS و SOCKS5 اضافه شده است.
• تنظیمات سابسکریپشن، زبان و ظاهر برنامه به بخش جدید «تنظیمات برنامه» منتقل شده‌اند.
• گزینه «بازنشانی تنظیمات» اضافه شده است؛ بدون حذف سابسکریپشن‌ها، نتایج تست‌ها یا قطع اتصال فعال.
• در بخش Split Tunneling اکنون تمام برنامه‌های نصب‌شده، حتی برنامه‌های بدون آیکون، نمایش داده می‌شوند.
• اسکرول فهرست برنامه‌ها در Split Tunneling اصلاح شده است.
• ذخیره نتایج تست اتصال و به‌روزرسانی صفحه سریع‌تر و روان‌تر شده است.
• حجم نسخه نهایی با حذف منابع اضافی کاهش یافته است.
📱
دانلود از گیتهاب
https://github.com/WhiteDNS/WhiteVPN/releases/tag/v1.6.2</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/whitedns/1588" target="_blank">📅 14:34 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-1587">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">✍️
دوستان، فعلاً سرور ساب WhiteVPN با یک مشکل فنی روبه‌رو شده و بچه‌ها در حال بررسی و برطرف کردنش هستن.  به‌محض اینکه مشکل حل بشه، ساب رو آپدیت می‌کنیم و همین‌جا بهتون خبر می‌دیم.  ممنون که صبورید و شرمنده بابت اختلالی که ممکنه براتون ایجاد شده باشه
🙏
فعلا…</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/whitedns/1587" target="_blank">📅 13:18 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-1584">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/SU_0paalnnV62PJQMK0rPmbbVE8tLTW2NlFSMZrH8T5DE8kqTfpH857MQi9FC2Clxpnv1egL8V1a6LKXlH4ii44sra2RqEdnk151jt-sROQwE-tLT3SKW7hPva8L0IHHUP8bKMJZUQmKo-412MYTHUrhFNFSNmCaGW67CCBcfU27bTt2BigVAlkt2pYIq2e8ZlfMlN0IwAejmtV-yDisiaNiGPRe9vPWkIqceXBRLhxfw4l33kLoSgf8YLvM9Qo3p_VLs8YiPfrtSgKyjaamrVSyG7U1e51x-mLgrUAuPjVQv9WMnldDLxfvKvT7u8sSKl6lTdVLuYuqVMWMjkZVlg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مهم
⚠️
⚠️
⚠️
⚠️
⚠️
دوستان :
پست  را با دقت مطالعه کنید
https://t.me/whitedns/1568
این کانفیگ های برای قابلیت "exit chain" توی اپ whiteaester و whitevpn هست - که ip شما را ثابت میکنه و یک لایه امنیت بیشتر به شما میده چون TLS هست
چون خیلی از دوستان کانفیگ نداشتن و یا نگران امنیتشون بودند ما این امکان را فراهم کردیم .
این کانفیگ ها برای استفاده مستقیم در اپ هایی مثل v2rayng و غیره نیست، اگر قصد استفاده مستقیم دارید لطفاً درخواست ارسال نفرمایید
تشکر
@whitedns</div>
<div class="tg-footer">👁️ 4.44K · <a href="https://t.me/whitedns/1584" target="_blank">📅 11:12 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-1582">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">✍️
دوستان، فعلاً سرور ساب WhiteVPN با یک مشکل فنی روبه‌رو شده و بچه‌ها در حال بررسی و برطرف کردنش هستن.
به‌محض اینکه مشکل حل بشه، ساب رو آپدیت می‌کنیم و همین‌جا بهتون خبر می‌دیم.
ممنون که صبورید و شرمنده بابت اختلالی که ممکنه براتون ایجاد شده باشه
🙏
فعلا از ساب موقت استفاده کنید تا اون مشکل حل بشه
https://ns1.rmft.tech/top300/sub
https://raw.githubusercontent.com/paranoideveloper/CoreForge-Sub/main/subscription_base64.txt
ارادتمند
تیم وایت</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/whitedns/1582" target="_blank">📅 07:09 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-1581">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/DR0PIbDAlchIJt96WYg0fdFpM6-kL2vdjSxP8yfvXBimEFGK5xpehNj_9pajdfH_o3CjyQkmobAGTEglYnn2RuZCI82Yag5PB-MXSqhmAVbEpsTSVe57bBWUW0tEfv7qgiYx7R5wkodcmeeR0rH-yvpzTPk0EMsr5LD83FmpxUY8pM-KlDURDqA7tpT9T1ycbQOovrCbUfAYLPxEmHVno1_7fButoSooqvUp1uLkcxfW4OL13gKBm0FO8i92gUsa5Rgbqo6nckhOKn1vzVEAGexWvsD9FD1_DIa7wqyKDlRb0AiEU83EEkATMh-gTMNndsLoubAowTWdZK1fk1OxWw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🌐
کلاینت WhiteAesther
(دانلود همزمان برای اندروید و ویندوز / دسکتاپ)
اگر به دنبال یک اتصال فوق‌العاده پایدار، سریع و امن با پروتکل نوین MASQUE H2 هستید، نرم‌افزار WhiteAesther در دو نسخه دسکتاپ و موبایل در دسترس شماست.
✨
قابلیت‌ها و ویژگی‌های کلیدی:
🔹
مبتنی بر پروتکل پرسرعت و مدرن MASQUE H2
🔹
اتصال سریع با یک کلیک (Zero-Config)
🔹
پایداری بالا و پینگ عالی مناسب وب‌گردی، گیمینگ و استریم
🔹
سیستم محافظت از کل ترافیک دستگاه (IPv4 + IPv6)
🔹
قابلیت Reconnect خودکار و Killswitch داخلی
🔹
رابط کاربری بسیار روان، تاریک (Dark Mode) و مدرن
━━━━━━━━━━━━━━━━━━━━
📥
لینک‌های دانلود مستقیم آخرین نسخه از گیت‌هاب:
📱
دانلود نسخه اندروید (Android APK):
🔗
https://github.com/WhiteDNS/WhiteAestherMobile/releases/latest
💻
دانلود نسخه دسکتاپ (Windows / PC):
🔗
https://github.com/WhiteDNS/WhiteAesther/releases/latest
━━━━━━━━━━━━━━━━━━━━
💡
پیشنهاد: این پست را برای دسترسی سریع به هر دو نسخه ذخیره (Save) یا پین کنید.
🆔
@whitedns</div>
<div class="tg-footer">👁️ 7.63K · <a href="https://t.me/whitedns/1581" target="_blank">📅 06:48 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-1580">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/NWKqNgEk5Dw2r3I0GQkYyMxkZY9ZqDkhAM6KlpvBisnyBUM29WXtQGOpgmjsSZgKjQgA91CIbAHIKE30bx9wYOrpUPuaZgTKuC_eBOzdyEyqXh1IPxAg67sQI2KPl3L972JnoIXuV9jGpphDnDMDB4StYt5BwiCjtosD4FGniXHb8q_oakfsOluy-nSA16xpC8BsRpRsInz59alw4Zb1w8_yZdqjfM_DRKtnRMLrXKlv4JoufqMHnrA-lKbtghHR9HreLs6e8XAkoQBNhcWuA-nl9p2RdA8VfPz_0cu6VLpPHmYdBsqYf0i1TYaFBcHTOsqt1uFz6NNJt4-4OZ27tw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚀
دسترسی آزاد و امن به اینترنت با WhiteVPN (نسخه موبایل و دسکتاپ)
اگر به دنبال یک کلاینت یکپارچه، سبک و حرفه‌ای هستید، WhiteVPN با رابط کاربری مدرن در دسترس شماست!
⚙️
قدرت گرفته از هسته Mihomo:
این برنامه بر پایه هسته قدرتمند Mihomo (مشابه کلش و متا) توسعه یافته است که بالاترین سطح پایداری و سرعت را در دور زدن محدودیت‌ها برای شما فراهم می‌کند.
⚠️
توجه مهم:
این اپلیکیشن کاملاً سورس‌باز (Open-Source) است و در Google Play یا App Store منتشر نشده است. تنها منبع رسمی برای دانلود، مخزن گیت‌هاب پروژه است.
✨
ویژگی‌های کلیدی:
🔹
پشتیبانی همزمان از ویندوز، مک، لینوکس و اندروید
🔹
رابط کاربری ساده و اتصال تنها با یک کلیک
🔹
سیستم پراکسی جامع و تونلینگ کل سیستم (System-wide)
🔹
مدیریت پیشرفته سرورها و پایداری بالا در اتصالات
━━━━━━━━━━━━━━━━━━━━
📥
دانلود مستقیم آخرین نسخه از گیت‌هاب (رسمی):
📱
نسخه اندروید (Mobile):
🔗
https://github.com/WhiteDNS/WhiteVPN/releases/latest
💻
نسخه دسکتاپ (Windows / macOS / Linux):
🔗
https://github.com/WhiteDNS/WhiteVPN-Desktop/releases/latest
━━━━━━━━━━━━━━━━━━━━
💡
برای دانلود، وارد لینک‌های بالا شده و از بخش "Assets" فایل متناسب با دستگاه خود (فایل apk برای اندروید و فایل‌های نصب برای ویندوز/مک) را دانلود کنید.
🆔
@whitedns</div>
<div class="tg-footer">👁️ 7.61K · <a href="https://t.me/whitedns/1580" target="_blank">📅 06:48 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-1579">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/KZd2ohjDDKZEkCaZIQoCuBU0S0ycOFcSNw3VbHRmgEL3FNfIdYX_Y18E5R05wldcZn_9-8IG-1oDzcfLB1VmIpK-M5FVva9VXf0l6EKItBhsHGzbuNDqWpi4cV6u5BWOL--Jarkl4EIYOqh7utsKZm6IDKfunXUDwccRwpsXSXMIWr0FFMn_yUtvaG0XSVQodz6UB_L3JWfrv8lHGg5u3NTPS1n9wIaf1bbWRtKcbwaZQ1bSeu-z5nncKZ0nXKOj_VPjyyzh2q53G2CJ7dRPE-jxAS7Vvik6HgsH3hToG8Uo-Xcy0AsX2LjfOcPd24hGyyaljHZ2Hdgjo9oSrEo04g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مهم
⚠️
⚠️
⚠️
⚠️
⚠️
دوستان :
پست  را با دقت مطالعه کنید
https://t.me/whitedns/1568
این کانفیگ های برای قابلیت "exit chain" توی اپ whiteaester و whitevpn هست - که ip شما را ثابت میکنه و یک لایه امنیت بیشتر به شما میده چون TLS هست
چون خیلی از دوستان کانفیگ نداشتن و یا نگران امنیتشون بودند ما این امکان را فراهم کردیم .
این کانفیگ ها برای استفاده مستقیم در اپ هایی مثل v2rayng و غیره نیست، اگر قصد استفاده مستقیم دارید لطفاً درخواست ارسال نفرمایید
تشکر
@whitedns</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/whitedns/1579" target="_blank">📅 22:52 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-1577">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">📹
آموزش اپلیکیشن WhiteVPN کامپیوتر و استفاده اپ داخل
🍏
آیفون برای کاربران IOS
https://youtu.be/tm0ls3r4ppw</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/whitedns/1577" target="_blank">📅 17:33 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-1576">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromLordofCinder</strong></div>
<div class="tg-text">🚀
بالاخره ‎CottenRouter‎ منتشر شد!
چیزی که خیلی‌هاتون بارها درخواست کرده بودید، بالاخره آماده شد.
🔥
اگه روی یک ‎VPS‎ چند ‎DNS Tunnel‎ دارید، دیگه لازم نیست برای ‎Port 53‎ بین سرویس‌ها درگیر باشید.
‎CottenRouter‎ امکان اجرای چند ‎Tunnel‎ روی
یک ‎IP‎ و یک ‎Port 53‎
رو فراهم می‌کنه و هر ‎Domain‎ رو به ‎Backend‎ مربوط به خودش هدایت می‌کنه.
⚡️
پشتیبانی از:
‎CottenDNS‎
‎MasterDnsVPN‎
‎StormDNS‎
‎thefeed‎
‎SlipGate‎
🛠
امکانات:
• ‎UDP / TCP‎
• ‎Multi-Domain‎ و ‎Multi-Backend‎
• ‎Port 53‎ بین چند ‎Tunnel‎
• ‎DoT‎، ‎DoH‎ و ‎HTTPS‎ بر اساس ‎SNI‎
• ‎TUI‎ و ‎Control Deck‎ برای مدیریت و مانیتورینگ
• نصب مستقیم روی ‎Linux‎
• پشتیبانی از ‎Docker‎
• ‎AMD64‎ و ‎ARM64‎
🛡
بدون دستکاری ترافیک ‎Tunnel‎
‎CottenRouter‎ چیزی به پکت ها و تانل اضافه نمیکنه
بنابراین قابلیت‌هایی مثل ‎ARQ‎، ‎FEC‎، ‎Compression‎، ‎MTU Discovery‎، ‎Record Channels‎، ‎SOCKS‎ و ‎TCP Forwarding‎ بدون تغییر باقی می‌مونن.
🔥
خلاصه:
یک ‎IP‎ + یک ‎Port 53‎ + چند ‎DNS Tunnel‎
🔗
‎GitHub‎:
https://github.com/TaJirax/CottenRouter</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/whitedns/1576" target="_blank">📅 15:13 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-1570">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/q2tJ5qMTzKjcbMTl1Q4SAzBGgMQsb5ZB71t76BTvbKbObBu2SSR-lw9WAQFORFfzRjuoBYB1M-EvJXJ_CyGDCKIUb7X248Cp4nHuGE8nAyeSQjgUWPr-KJYiRlXepOCXT0p4YF7U7UqWWnAnq4kXH-4r0CklhhG-5ysAPE69dMyLu_FZJNxNTjqfsVqexoiambNx_P-5L2UxrjuVTTlVafe4aZ73T50IuToqZMy6v6K6wKz8nGE_XkFSqaANGAUVA-XQEXO6rIqS1N6GI7L-vGN3-7a2rNVWu9okeHwuwv3IJavIq9O4UU_B-5FYZcCOcR5-ZySXMOcMy1GGSKObBg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">موقت :
یک سوال خودمونی :
تا الان نزدیک 50 نفر کانفیگ دریافت کردن
چرا حتی به خودشون زحمت ندادند یک لایک کنند ؟
این فرهنگ عجیب از کجا اومده ؟
اون لایکی که شما میکنید یک انرژی برای این تیم هست که شما دریغ میکنید .
😏</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/whitedns/1570" target="_blank">📅 06:36 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-1568">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/I8019LwFlf6ntkqjGhJ9nNWbTU0wboLaJp9_odoQXR-oxUDk6USvAvPFVIBEzF79EcPqfKVZ2OSwYixYBVulo556mgEbSNgZkqYLRAZtb3qtBDJT6a_FsMxnlwD3NyW_nESyIu0KOrPn7ShlwNt4f_E5e0_WvvT3CRwYP-9bYGrGiWL5e8iSv1NGe-ziJ1A816zYbxSfe5w5wNnC6E2xYfF-LV5PniZ32E7J4cZKRRTOv3ypu0NDr1Ef1Zo_As7l4h0yrBJ8dI9V4LcYqXNP2O19Ws0DnFiGbMW7F0o6JwSvDxlSWXaYt3YwzZanub-bkzrC_txeyGXBZ7EAerob3w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📢
راهنمای کامل استفاده از ربات WhiteDnsChain
(کانفیگ هسته x-ray )
نکته : این ربات یک کانفیگ اضطراری برای شما ایجاد میکند تا در موارد خیلی خاص از ان استفاده کنید . کانفیگ های این ربات برای امکان exit chain در اپ های white ایجاد شده و هر گونه سواستفاده از آن مجاز نیست
🤖
آدرس ربات:
@WhiteDnsChainbot
برای دریافت و مدیریت اتصال اختصاصی خود مراحل زیر را انجام دهید:
1️⃣
شروع و انتخاب زبان
- وارد ربات شوید.
- دستور /start را ارسال کنید.
- گزینه «
🇮🇷
فارسی» را انتخاب کنید.
- برای تغییر زبان در آینده از گزینه «
🌐
تغییر زبان» استفاده کنید.
2️⃣
درخواست کانفیگ
- روی «
🔐
دریافت کانفیگ» بزنید یا دستور /config را ارسال کنید.
- درخواست شما برای مدیر فرستاده می‌شود.
- پس از تأیید، یک پیام اطلاع‌رسانی دریافت می‌کنید.
- دوباره /config را بزنید تا لینک اشتراک و QR اختصاصی شما نمایش داده شود.
3️⃣
اضافه‌کردن کانفیگ به برنامه
- یک برنامه سازگار با V2Ray/Xray روی دستگاه خود نصب کنید.
- لینک اشتراک را کپی کنید.
- در برنامه گزینه افزودن Subscription یا «افزودن اشتراک» را انتخاب کنید.
- لینک را وارد کرده و اشتراک را به‌روزرسانی کنید.
- یکی از سرورها را انتخاب کرده و اتصال را فعال کنید.
4️⃣
مشاهده وضعیت حساب
از گزینه «
👤
حساب من» یا دستور /account استفاده کنید تا موارد زیر را ببینید:
- وضعیت فعال یا غیرفعال
- تاریخ انقضا
- حجم مصرف‌شده
- حجم کل
- محدودیت تعداد دستگاه یا IP
5️⃣
دریافت دوباره کانفیگ
اگر پیام کانفیگ را پاک کردید، نگران نباشید. با /config همان کانفیگ اختصاصی دوباره نمایش داده می‌شود و کانفیگ جدیدی ساخته نخواهد شد.
6️⃣
پشتیبانی
- روی «
💬
پشتیبانی» بزنید یا /support را ارسال کنید.
- مشکل خود را در یک پیام کامل توضیح دهید.
- پیام مستقیماً برای مدیر ارسال می‌شود.
- پاسخ مدیر را داخل همین ربات دریافت خواهید کرد.
7️⃣
دستورات کاربردی
- /start — شروع و انتخاب زبان
- /config — دریافت کانفیگ
- /account — مشاهده وضعیت حساب
- /menu — نمایش منوی اصلی
- /support — ارتباط با پشتیبانی
- /help — نمایش راهنما
⚠️
نکات مهم
⚠️
-درخواست ها توسط ادمین دونه دونه بررسی و تایید میشود پس لطفا صبور باشید
- ادمین کاملا مختار است که به هر دلیل ممکن از ارایه کانفیگ به شما خودداری کند پس لطفا اعتراض نکنید
⚠️
-در حال حاظر کانفیگ ها با محدودیت 1 روزه و یک گیگ هست
- لینک و QR کاملاً اختصاصی است؛ آن را برای دیگران ارسال نکنید.
- هر حساب تلگرام فقط یک کانفیگ فعال دریافت می‌کند.
- ارسال چندباره /config کانفیگ تکراری ایجاد نمی‌کند.
- برای امنیت بیشتر، پس از دریافت کانفیگ می‌توانید پیام آن را با گزینه «
🗑
مخفی کردن» حذف کنید.
- در صورت پایان حجم یا اعتبار، از طریق پشتیبانی با مدیر ارتباط بگیرید.
@whitedns</div>
<div class="tg-footer">👁️ 35.3K · <a href="https://t.me/whitedns/1568" target="_blank">📅 05:58 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-1567">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromPatt's Channel</strong></div>
<div class="tg-text">اگه حوصله خوندن توضیحات رو ندارید، فقط ساب زیر را وارد
PattNG
/
PattN
کرده و لذت ببرید !
https://raw.githubusercontent.com/patterniha/Free-Configs/main/configs.txt
ساب هر ۲۴ ساعت آپدیت میشود.
///
توضیحات:
چند تا از پروژه های عالی که کانفیگهای رایگان را جمع‌آوری و تست میکنند و سپس کانفیگهای سالم را فیلتر و در اختیار قرار میدهند پروژه‌ها‌ی
https://github.com/0xRadikal/Free-v2ray-Configs
و
https://github.com/itsyebekhe/PSG
و
https://github.com/Delta-Kronecker/V2ray-Config
هستند.
اما این پروژه‌ها دو مشکل اساسی دارند، اول اینکه تست کانفیگها باید از طریق اینترنت و فایروال ایران انجام شود ولی در حال حاضر تست کانفیگها در این پروژه‌ها از طریق گیتهاب انجام میشود، دوم اینکه روی نت‌های آپلود محدود (ایرانسل و ...) عملا اکثر کانفیگهای این پروژه‌ها آپلود محدود هستند و کیفیت بسیار پایینی دارند.
از آنجا که با روشهای زیادی میتوان محدودیت آپلود را روی کلودفلر دور زد، من در پروژه‌ی خودم اومدم کانفیگهای کلودفلر سالم را از پروژه‌ها‌ی اصلی جدا کردم و تغییراتی را برای دور زدن محدودیت آپلود (و همچنین دور زدن فیلتر دامنه) اعمال کردم (در حال حاضر متد fragment+fingerprint اعمال شده). بنابراین کانفیگهای نهایی سالم و با حداکثر سرعت در تمامی نتها قابل استفاده هستند.
برای دور زدن محدودیت آپلود در نتهای آپلود محدود در حال حاضر فقط باید از کلاینت
PattNG
/
PattN
استفاده کنید، بزودی در سایر کلاینتها نیز این مورد پشتیبانی میشود.
https://github.com/patterniha/Free-Configs</div>
<div class="tg-footer">👁️ 7.96K · <a href="https://t.me/whitedns/1567" target="_blank">📅 03:55 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-1566">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IyThTW1aPYpz61AlxABJ9ix8gE3brXCNktshPK6l8RclegrwfwnIY8ckBlhbq3yisB9gjex_Ngr0dmcVkcCe7NHTehKLCqat9jrQmUOcBtPlpo4WEZOJS5BSteF4BgVPtNA8gWst03S4juO46j5AqwS5Cpb4VptfoCL3VMOd4RkjrjMg9uX6lp1hd9TrwJP8oAxLKj9skwzpgbKavfR1VnYDzspKNozYPTblgL8dy_4eO8pBpzDxXyA-LknnAECAc6l4mvYyA98SNGwJ-VvuYqJ589GRbxgqad6rFOxtjPlOhkxc9V_BPIq2GMNk7nqu14BlvGvl6npm3GVQn-HlHQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
WhiteDNS
مسیری که قبل از روزهای قطعی اینترنت شروع شد
تیم WhiteDNS از مدت‌ها قبل از قطعی‌ها و محدودیت‌های گسترده اینترنت فعالیت می‌کرد. از همان ابتدا تلاش کردیم ابزارها، سرویس‌ها و آموزش‌هایی بسازیم که رایگان و در دسترس همه باشند.
در این مدت افراد زیادی به این جمع پیوستند؛ بعضی ماندند و بعضی مسیرشان جدا شد، اما چیزی که ما را کنار هم آورد همچنان پابرجاست:
حرکتی جمعی برای دسترسی آزادتر به اینترنت.
تیم WhiteDNS تا امروز کاملاً مستقل و بدون هیچ منبع درآمدی اداره شده و تمام هزینه‌ها را خودمان پرداخت کرده‌ایم. با این حال، این مسیر را ادامه می‌دهیم و همچنان ابزارها و سرویس‌های رایگان بیشتری را با کمک همین جامعه خواهیم ساخت.
حالا تنها مسیر درآمدی ما کانال یوتیوب WhiteDNS است. اگر می‌خواهید از این حرکت حمایت کنید، کانال را سابسکرایب کنید و ویدیوها را ببینید. همین همراهی کمک می‌کند WhiteDNS مستقل، فعال و جامعه‌محور باقی بماند.
📺
https://www.youtube.com/@WhiteDNS
ممنون که بخشی از این مسیر هستید
❤️
تیم WhiteDNS</div>
<div class="tg-footer">👁️ 8.86K · <a href="https://t.me/whitedns/1566" target="_blank">📅 18:48 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-1564">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/Y7RGBVDeBLzWlt219yorsxjc7uq_-lh4HWXOaYbceZcNtBFDNxjpYIh6axcExyq8Bpg4NtX7pI7Y1qkXQUHNtHzrJskN4crTkjl5DOV2tHJVfBJjVxLSBSG3Nj_psGpDYT5MFJkJwNq0wcy_xkAUhVekWcdtqSMHuFpVujwSa_8xwOkQfN4R6TekWxn56qtGqWWjEnpN1I2rSQTnzu82iQv1u23zYy3XMN5xXOg6c1jU1YoS6PKx-kPmwJlGBUTB2N1v5LyYh3BPN21Cnl-CTAOEzWTgEC3irQaorW9GTZJBlZ2iAPbNSdtvsbGqQGMEm8KqgkGqQNLoU7pR3cYWnA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">Whitedns Chatbot V4 (جدید)
🎉
🎉
🎉
@WhiteDnsResponder_bot
راهنمای استفاده از ربات WhiteDNS
سلام!
این ربات به شما کمک می‌کند پاسخ سوال‌های مربوط به WhiteDNS، ابزارهای اتصال، DNS، نصب برنامه‌ها و رفع مشکلات رایج را از میان مطالب منتشرشده پیدا کنید.
آموزش :
⚠️
👇
### ۱. پرسیدن سوال معمولی
💬
کافی است سوالتان را مستقیماً برای ربات بنویسید.
نمونه‌ها:
- چطور WhiteDNS را روی اندروید نصب کنم؟
📱
- آخرین نسخه برنامه چیست؟
- چرا DNS وصل نمی‌شود؟
🌐
- تنظیمات ویندوز را چطور انجام بدهم؟
🖥
برای دریافت پاسخ بهتر، نام برنامه، دستگاه یا سیستم‌عامل و متن دقیق خطا را در یک پیام بنویسید.
ربات ممکن است همراه پاسخ، دکمه‌های منبع را نیز نمایش دهد. با انتخاب آن‌ها می‌توانید مطلب اصلی کانال را مشاهده کنید.
📎
### ۲. عیب‌یابی مرحله‌ای با /diagnose
🔧
اگر مشکل فنی دارید و نمی‌دانید چطور آن را توضیح دهید، دستور زیر را انتخاب کنید:
/diagnose
ربات از شما سه مورد کوتاه می‌پرسد:
1. نوع مشکل، مانند وصل نشدن، سرعت پایین، DNS یا نصب
2. دستگاه یا سیستم‌عامل
3. توضیح کوتاه مشکل یا متن دقیق خطا
پس از دریافت راه‌حل، این گزینه‌ها نمایش داده می‌شوند:
-
✅
حل شد — اگر مشکل برطرف شده است.
-
🔁
راه دیگر — دریافت یک راه‌حل جایگزین.
-
👤
ارسال برای مدیر — آماده‌کردن گزارش برای مدیران.
برای جلوگیری از طولانی‌شدن مراحل، ربات فقط یک راه‌حل جایگزین ارائه می‌دهد.
### ۳. ارسال نتیجه عیب‌یابی برای مدیر
اگر راه‌حل‌های ربات مؤثر نبودند، گزینه ارسال برای مدیر را انتخاب کنید.
قبل از ارسال، ربات پیش‌نمایشی شامل موارد زیر نشان می‌دهد:
- نوع مشکل
- دستگاه یا سیستم‌عامل
- توضیح شما
- راه‌حل‌هایی که امتحان کرده‌اید
- نام تلگرام
- نام کاربری، در صورت وجود
- شناسه عددی کاربر و گفتگو
- زبان حساب تلگرام
درخواست فقط بعد از انتخاب تأیید و ارسال برای مدیران فرستاده می‌شود.
### ۴. جستجوی مستقیم با /search
برای پیدا کردن مطالب کانال بدون ساخت پاسخ جدید، از این دستور استفاده کنید:
/search عبارت موردنظر
مثال:
/search نصب WhiteDNS اندروید
ربات نزدیک‌ترین مطالب را همراه دکمه مشاهده منبع نشان می‌دهد.
### ۵. ارسال پیام مستقیم به مدیران با /contact
اگر موضوع شما با عیب‌یابی قابل حل نیست، دستور زیر را انتخاب کنید:
/contact
سپس تمام توضیحات خود را در یک پیام کامل بفرستید. بهتر است پیام شامل این موارد باشد:
- نام برنامه
- دستگاه یا سیستم‌عامل
- نسخه برنامه
- نوع اتصال
- متن دقیق خطا
- کارهایی که قبلاً امتحان کرده‌اید
مدیران اطلاعات حساب تلگرام و پیام کامل شما را دریافت می‌کنند و می‌توانند از طریق ربات یا گفتگوی مستقیم پاسخ دهند.
شماره تلفن شما برای ربات قابل مشاهده نیست، مگر اینکه خودتان آن را داخل پیام ارسال کنید.
### ۶. ادامه سوال قبلی
ربات می‌تواند برای مدت کوتاهی ارتباط بین سوال‌های شما را تشخیص دهد.
مثال:
- پیام اول: «روش نصب WhiteDNS چیست؟»
- پیام بعدی: «برای اندروید چطور؟»
این زمینه گفت‌وگو حداکثر ۳۰ دقیقه و تا چهار نوبت نگه داشته می‌شود و به‌عنوان منبع واقعی پاسخ استفاده نمی‌شود.
### ۷. شروع گفت‌وگوی تازه با /new
اگر می‌خواهید موضوع قبلی فراموش شود، از این دستور استفاده کنید:
/new
این دستور زمینه موقت گفت‌وگو و عملیات نیمه‌تمام را پاک می‌کند.
### ۸. ثبت بازخورد
زیر پاسخ‌های ربات دو گزینه وجود دارد:
-
✅
مفید بود
-
❌
مفید نبود
بازخورد شما به مدیران کمک می‌کند پاسخ‌ها و مطالب ربات را بهتر کنند.
همچنین می‌توانید برای آخرین پاسخ از دستور زیر استفاده کنید:
/feedback
### ۹. لغو عملیات با /cancel
برای خروج از ارسال پیام، عیب‌یابی یا پاسخ‌دادن به یک درخواست فعال، بنویسید:
/cancel
فهرست دستورات
- /start — شروع کار با ربات
- /help — نمایش راهنما
- /diagnose — عیب‌یابی مرحله‌ای
- /search — جستجوی مستقیم در مطالب
- /feedback — ثبت بازخورد برای آخرین پاسخ
- /contact — ارسال پیام به مدیران
- /new — شروع گفت‌وگوی تازه
- /cancel — لغو عملیات فعال
محدودیت استفاده
برای کنترل هزینه و حفظ کیفیت سرویس:
- حداکثر ۳ درخواست هوش مصنوعی در هر ۵ دقیقه
- حداکثر ۵۰ درخواست هوش مصنوعی در روز
دستورهای ساده مانند /help، /search، /contact و بازخورد شامل این محدودیت هوش مصنوعی نمی‌شوند.
نکات مهم
- برای پاسخ دقیق‌تر، همه جزئیات مشکل را در یک پیام بنویسید.
- پاسخ‌ها بر اساس مطالب موجود WhiteDNS تولید می‌شوند و ممکن است برای مشکلات خاص کامل نباشند.
- در صورت حل‌نشدن مشکل، از مسیر عیب‌یابی و سپس ارسال گزارش برای مدیر استفاده کنید.
@whitedns</div>
<div class="tg-footer">👁️ 36.9K · <a href="https://t.me/whitedns/1564" target="_blank">📅 17:41 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-1563">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromBlue Knight(𝑫𝒊𝒂𝒏𝒂🍓)</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/776e6fda95.mp4?token=TYpXZ-45hAO8Vnybm_xjEzQ_GQ9nlv5d28-Eh3Zqw2c6klmFYFHIP6i2Ten4pfoOw7XT7oJHIImoU2s5pCwoNI77YFNrbAuZqa6vFInt5wmho78WtqqS2jd_ivs0V7yWB4slxv4Dfa9aU8-ezlnRXEqnVrExTxfvtn_WdrqojI3zp_7nW0JI0bo8d-zW2MqkifM_8avtza2Xa1p6H1_zXmyYuwMY0pGl1QEcDGHJZju7jd3gAxcm_F1dWAlJ0oES4wYDx8bBKEqwJbPGZ-9xgTU9eeXIYTPHiqvKTTXzPsvtSOj_bLPeoTM_6iS1MJhdjlrLaipgA5G7dNWrPOJ2mA8ALDhjxbMDvW19l0-p3C4fU3HQPANt3Pv4ldq7vFjXd6N_AQtFf84voc3qt7Xd9kp0Ozal6WrZu3jnv7CLgQaInYSxsrzZZx79TqHbOkslt4OZVFvmBjKbbKHBToxgqAc0uIF4zivPDTqh-sjdDl63op3EFLEmraFXh3CvN-lUJJqCYlHA6BLAc85roRtvReJlOpz8Iejs1zrULT72g5Jf2DlRimw0Cimc2VML6COZQm_kddJPX2Qs9etsiH_QwznaKPG80CtcqIzLnSjxb1pz1gm3wepgbPUVnPM7EJAD1yUvzzhc1NVef5DvKI7VgxAQo-GlOWmUJKa1VwPpVx8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/776e6fda95.mp4?token=TYpXZ-45hAO8Vnybm_xjEzQ_GQ9nlv5d28-Eh3Zqw2c6klmFYFHIP6i2Ten4pfoOw7XT7oJHIImoU2s5pCwoNI77YFNrbAuZqa6vFInt5wmho78WtqqS2jd_ivs0V7yWB4slxv4Dfa9aU8-ezlnRXEqnVrExTxfvtn_WdrqojI3zp_7nW0JI0bo8d-zW2MqkifM_8avtza2Xa1p6H1_zXmyYuwMY0pGl1QEcDGHJZju7jd3gAxcm_F1dWAlJ0oES4wYDx8bBKEqwJbPGZ-9xgTU9eeXIYTPHiqvKTTXzPsvtSOj_bLPeoTM_6iS1MJhdjlrLaipgA5G7dNWrPOJ2mA8ALDhjxbMDvW19l0-p3C4fU3HQPANt3Pv4ldq7vFjXd6N_AQtFf84voc3qt7Xd9kp0Ozal6WrZu3jnv7CLgQaInYSxsrzZZx79TqHbOkslt4OZVFvmBjKbbKHBToxgqAc0uIF4zivPDTqh-sjdDl63op3EFLEmraFXh3CvN-lUJJqCYlHA6BLAc85roRtvReJlOpz8Iejs1zrULT72g5Jf2DlRimw0Cimc2VML6COZQm_kddJPX2Qs9etsiH_QwznaKPG80CtcqIzLnSjxb1pz1gm3wepgbPUVnPM7EJAD1yUvzzhc1NVef5DvKI7VgxAQo-GlOWmUJKa1VwPpVx8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✨
یه آموزش خفن و کاملاً رایگان براتون داریم!
✨
اگه دوست دارید بدون هیچ هزینه‌ای با
پنل Netra
کانفیگ بسازید، این آموزش دقیقاً برای شماست!
💗
بدون هزینه
🎀
کاملاً رایگان
✨
آموزش مرحله‌به‌مرحله
🎥
آموزش کامل رو آماده کردیم و می‌تونید همین الان توی یوتیوب ببینید:
https://youtu.be/qluhGfGNbwk?si=oTLkVuC1z-5L03fy
💌
اگه آموزش براتون مفید بود، حتماً لایک کنید و برای دوستاتون هم بفرستید!
·:¨༺
@BlueKnight_Net
༻¨:·</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/whitedns/1563" target="_blank">📅 15:59 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-1560">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/iLUxEX9RfsI8V3m-kX_TR0Qz6mP_zsJ_lNfwnqzgF8CfHFXQ2LFd21OXl3gK4JG6E59NPswvQ56mj_T0dxlELfnnah4Th0gb4H5L6sBNEzAZPyy06UVV87je6Rj4ufptdOmRu5oBgFHoBKSjJopMkAkndMK5qojhsjnSyCmjv0A2mOalMHzF27MODOxPLJt28sYdPxiBZT3c_BWY50h174mMAF9gbqlSHEULVYuaakBCj3R6Mb4-ObsVnAokOkqdlSBxytuJrHZnrf3bZFLk-Q1TD9dvmbIkbHb5T6Dqo9SzItz5yhXWtiygdh5FkjmECcWTAeDqG3s1_RF50Ej34w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔗
WhiteVPN Desktop v1.0.18
زنجیره کردن اتصال (Connection Chaining)
از این نسخه می‌توانید ترافیک را قبل از رسیدن به اینترنت از دو سرور رد کنید.
اتصالی که در صفحهٔ وی‌پی‌ان انتخاب کرده‌اید هاپ اول می‌شود، و سروری که در تنظیمات به‌عنوان هاپ دوم انتخاب می‌کنید جایی است که ترافیک از آن خارج می‌شود.
چطور فعالش کنم؟ تنظیمات ← زنجیره کردن اتصال ← هاپ دوم
پیش‌فرض روی «خاموش — یک هاپ» است و اگر دست نزنید، همه چیز دقیقاً مثل قبل کار می‌کند.
چند نکته که خودِ برنامه رعایت می‌کند:
▪️
سرور هاپ دوم از فهرست هاپ اول حذف می‌شود، تا هر دو سرِ زنجیره یک ماشین نباشند و بی‌دلیل هزینهٔ دو هاپ را ندهید.
▪️
اگر هاپ دوم WireGuard یا Hysteria2 (یا هر پروتکل روی QUIC) باشد، فقط سرورهایی به‌عنوان هاپ اول پیشنهاد می‌شوند که بتوانند UDP را حمل کنند. زنجیره‌ای که هاپ اولش فقط TCP باشد ساخته می‌شود و وصل هم می‌شود، ولی هیچ ترافیکی رد نمی‌کند.
▪️
حالت Automatic همچنان کار می‌کند. اگر هاپ اول قطع شود، خودِ گروه جایگزینش می‌کند و نیازی به اتصال دوباره نیست.
▪️
اگر سروری که به‌عنوان هاپ دوم انتخاب کرده‌اید بعد از به‌روزرسانی اشتراک حذف شود، همان‌جا در تنظیمات به شما گفته می‌شود — نه وقتی که دارید وصل می‌شوید.
⚠️
توجه: دو هاپ طبیعتاً کندتر از یکی است، چون هر سرور باید ترافیک سرور بعدی را هم حمل کند. اگر سرعت برایتان مهم‌تر از لایهٔ اضافه است، همان یک هاپ را نگه دارید.
دانلود: ویندوز (x64 / ARM64) · مک (Intel / Apple Silicon) · لینوکس (deb / rpm / AppImage / tar.gz)
github.com/WhiteDNS/WhiteVPN-Desktop/releases/latest
@whitedns</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/whitedns/1560" target="_blank">📅 16:34 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-1558">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/fz-7gAJyHUcvCFs8xcLlvYq8qBt9BbDLdVoyUqg0jeP6jAZj7fGHtvlg6VFQTstLgOZR3snmWZ67XRXw0MiscCCvOUR9DqZJoyP0SN2PKYF0W3Cq1G1gCe7V7wzoGO_8xwgufmk13UqzmV2K4gRfe_7QSzW0mNnnK9aoDi_j_9q8LMLUjsavaW30UT2fjEb0WibpIOYlVCajCXI0qXAPD9QnNkoXCnzWTtyYxnn5BixjSyokDGRp-DveOHGGt2ENNbwFGZLgqTqE_AUjaEZ8E0CERJ5AN3G-k8yebea7p8STiTbilEHr7grwj4MyupvHU2pojz7hX5zqDDAoPxcnmQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔗
WhiteAesther Android ورژن جدید
🔥
🔥
🔥
🔥
🔥
نسخه ۱.۲.۱ — رفع سه مشکل اتصال
این نسخه قابلیت بزرگ جدیدی نداره؛ سه تا مشکل رو رفع می‌کنه که باعث می‌شد اپ روی خیلی از گوشی‌ها اصلاً وصل نشه. اگه ۱.۲.۰ داری حتماً آپدیت کن.
🛠
چی رفع شد
1
.پروتکل های wireguard و warp in warp برای خیلی از دوستان اصلاً وصل نمی‌شدن
توی ۱.۲.۰ «ثبت‌نام مشترک بین پروتکل‌ها» رو به‌عنوان یک بهبود اعلام کردیم. اون کار اشتباه بود: وقتی MASQUE هویت رو ثبت می‌کرد، کلید WireGuard روی سرور Cloudflare پاک می‌شد. بعدش هیچ اندپوینتی جواب نمی‌داد و اپ می‌گفت شبکه بسته‌ست — در حالی که مشکل از هویت بود، نه از شبکه.
حالا هر پروتکل هویت خودش رو داره. اگه از ۱.۲.۰ آپدیت کنی حسابت از دست نمی‌ره.
⚠️
در عوض، اون کاهش سه‌برابری احتمال rate limit هم برگشت. اگه زیاد نصب و حذف می‌کنی، حتماً از
Settings ← Identity & access
یک بار بکاپ هویت بگیر.
۲
. عوض کردن پروتکل وسط اتصال، همه‌چیز رو خراب می‌کرد
اگه بدون قطع کردن اتصال پروتکل رو عوض می‌کردی، جستجوی اندپوینت از داخل همون تونل قبلی رد می‌شد — یعنی هزاران درخواست دقیقاً به جایی می‌رفت که قرار بود جایگزینش کنه. نتیجه: هیچی وصل نمی‌شد.
۳
. گیر کردن روی پروتکلی که شبکه‌ات بسته
پیش‌فرض قبلی H3 بود که روی UDP کار می‌کنه. اگه شبکه UDP رو بسته بود تلاش اول شکست می‌خورد و اپ دوباره همون رو امتحان می‌کرد. تا نوبت MASQUE H2 برسه چهار دقیقه و نیم گذشته بود، و عملاً هیچ‌کس این‌قدر صبر نمی‌کنه.
✨
چی جدیده
حالت Automatic — از
Routes ← Manual ← Protocol
گزینه اول حالا Automatic هست و پیش‌فرض هم شده. خودش سریع امتحان می‌کنه ببینه شبکه‌ات چی رو اجازه می‌ده، از H2 شروع می‌کنه (چون TCP روی پورت ۴۴۳ هست و شبیه HTTPS معمولی دیده می‌شه)، و هرچی جواب داد رو یادش می‌مونه تا دفعه بعد از همون شروع کنه.
روی نصب تازه: ۱۴ ثانیه تا اتصال، جایی که قبلاً چند دقیقه طول می‌کشید.
گزارش خطای واقعی — قبلاً اگه جستجو نتیجه نمی‌داد فقط می‌نوشت «اندپوینتی پیدا نشد». حالا می‌گه چرا: بسته‌ها از گوشی خارج شدن و جوابی نیومد (مشکل از شبکه‌ست)، یا اصلاً خارج نشدن (مشکل از مسیریابی خود گوشیه). لاگ خود موتور تونل هم از این نسخه داخل
Settings ← Diagnostics
هست — اگه مشکلی خوردی همون گزارش رو بفرست.
⬇️
دانلود
https://github.com/WhiteDNS/WhiteAestherMobile/releases/latest</div>
<div class="tg-footer">👁️ 40.9K · <a href="https://t.me/whitedns/1558" target="_blank">📅 14:35 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-1557">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/FOA9YPv_3nxSrktEkhqxzn_tk93qxL25rJTuAwU5-1Ha-9U6-fIk0S8jxKu3G6FMPI3tG1nNixZK0R4Gh2xu_j-VkyAPrrdCm08VdY2LOQCxdF3vT9MEnlSOT_CHHVj0tQDsxbR4KJ75KnjKeAKm1-Ak0ocztW5LSxO2KYZCQ0lsSzuxjlose56oEekQL8AsYNufD0HllRWzviKJsjwyVmusQhDq6XfMAkufM5JIHmQUZ1yTAzNb_DzQUVuWJ1j6PQqk41JnB5hGz5-M__2eYq3Wd3AreMK0U4-UewTrjyYrmYZyt3zwDilErR6wgIVFfH7CKtrzZiveM2KwPM9Dxw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🌐
کلاینت WhiteAesther
(دانلود همزمان برای اندروید و ویندوز / دسکتاپ)
اگر به دنبال یک اتصال فوق‌العاده پایدار، سریع و امن با پروتکل نوین MASQUE H2 هستید، نرم‌افزار WhiteAesther در دو نسخه دسکتاپ و موبایل در دسترس شماست.
✨
قابلیت‌ها و ویژگی‌های کلیدی:
🔹
مبتنی بر پروتکل پرسرعت و مدرن MASQUE H2
🔹
اتصال سریع با یک کلیک (Zero-Config)
🔹
پایداری بالا و پینگ عالی مناسب وب‌گردی، گیمینگ و استریم
🔹
سیستم محافظت از کل ترافیک دستگاه (IPv4 + IPv6)
🔹
قابلیت Reconnect خودکار و Killswitch داخلی
🔹
رابط کاربری بسیار روان، تاریک (Dark Mode) و مدرن
━━━━━━━━━━━━━━━━━━━━
📥
لینک‌های دانلود مستقیم آخرین نسخه از گیت‌هاب:
📱
دانلود نسخه اندروید (Android APK):
🔗
https://github.com/WhiteDNS/WhiteAestherMobile/releases/latest
💻
دانلود نسخه دسکتاپ (Windows / PC):
🔗
https://github.com/WhiteDNS/WhiteAesther/releases/latest
━━━━━━━━━━━━━━━━━━━━
💡
پیشنهاد: این پست را برای دسترسی سریع به هر دو نسخه ذخیره (Save) یا پین کنید.
🆔
@whitedns</div>
<div class="tg-footer">👁️ 8.45K · <a href="https://t.me/whitedns/1557" target="_blank">📅 14:05 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-1556">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/LMsLKfRVKjGDblCrYh4DF52edSWjN1KEOSs8zDIAq-lCKLTrvH9BSuNnQu8xFt5atoIX7nQkpgrP1i3NQYBP1MYQe_nZOlCHjURGT7IQLGPZc_dL7xF0FQwubFiDhG3F_rS8-cqDprLE7X5hBLrSFZaYssepMuaFdpxhDHuCgZDKtmJ_VJgruTyE9hcmRdmy-KzEXcPoIvzwt-YqAMaOTinbD981FzTr7xh_OW3APciIdsH64PCovXbcZiPfEoP0hcQ95YUCb0NhrtILWv2qAnBYsYPT3c6QZJNHTjK-2PRrw_Jff0Ne5tXBdnPr6cUFyHiVLEpl149fcx7d0S3Flg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚀
دسترسی آزاد و امن به اینترنت با WhiteVPN (نسخه موبایل و دسکتاپ)
اگر به دنبال یک کلاینت یکپارچه، سبک و حرفه‌ای هستید، WhiteVPN با رابط کاربری مدرن در دسترس شماست!
⚙️
قدرت گرفته از هسته Mihomo:
این برنامه بر پایه هسته قدرتمند Mihomo (مشابه کلش و متا) توسعه یافته است که بالاترین سطح پایداری و سرعت را در دور زدن محدودیت‌ها برای شما فراهم می‌کند.
⚠️
توجه مهم:
این اپلیکیشن کاملاً سورس‌باز (Open-Source) است و در Google Play یا App Store منتشر نشده است. تنها منبع رسمی برای دانلود، مخزن گیت‌هاب پروژه است.
✨
ویژگی‌های کلیدی:
🔹
پشتیبانی همزمان از ویندوز، مک، لینوکس و اندروید
🔹
رابط کاربری ساده و اتصال تنها با یک کلیک
🔹
سیستم پراکسی جامع و تونلینگ کل سیستم (System-wide)
🔹
مدیریت پیشرفته سرورها و پایداری بالا در اتصالات
━━━━━━━━━━━━━━━━━━━━
📥
دانلود مستقیم آخرین نسخه از گیت‌هاب (رسمی):
📱
نسخه اندروید (Mobile):
🔗
https://github.com/WhiteDNS/WhiteVPN/releases/latest
💻
نسخه دسکتاپ (Windows / macOS / Linux):
🔗
https://github.com/WhiteDNS/WhiteVPN-Desktop/releases/latest
━━━━━━━━━━━━━━━━━━━━
💡
برای دانلود، وارد لینک‌های بالا شده و از بخش "Assets" فایل متناسب با دستگاه خود (فایل apk برای اندروید و فایل‌های نصب برای ویندوز/مک) را دانلود کنید.
🆔
@whitedns</div>
<div class="tg-footer">👁️ 8.07K · <a href="https://t.me/whitedns/1556" target="_blank">📅 14:05 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-1555">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eFOATiHL4X3P9kqJIjh-EVs321OZivxCZF_f9_pHYiu4ho7RLe8YLP5xObSwourIVfqHaGyZnaUXCgWgr_YQplObvqmIKLLun9khgX6AYI6TszA2CyyaRlC6OPIPdbtFD00Lboc4Qrrys_uxyvdD-Qm5JYlmbWv4CRWzLnsrInXTFfACZAAul92q6vA9O087oMBt09k9pStefgidfqa_FdIUYHtTUGZ-fExak2TalhKOIXZYec0BiEvgIl88O1hUqkaeQ2AD_x3GflNHTxX_fWO8-8q7ztgRgzMFukIReO6jtNRCHh-ZSQ_E_Lk8PPize_ZlIJnGKJY9OPUocTfoAA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
WhiteDNS
مسیری که قبل از روزهای قطعی اینترنت شروع شد
تیم WhiteDNS از مدت‌ها قبل از قطعی‌ها و محدودیت‌های گسترده اینترنت فعالیت می‌کرد. از همان ابتدا تلاش کردیم ابزارها، سرویس‌ها و آموزش‌هایی بسازیم که رایگان و در دسترس همه باشند.
در این مدت افراد زیادی به این جمع پیوستند؛ بعضی ماندند و بعضی مسیرشان جدا شد، اما چیزی که ما را کنار هم آورد همچنان پابرجاست:
حرکتی جمعی برای دسترسی آزادتر به اینترنت.
تیم WhiteDNS تا امروز کاملاً مستقل و بدون هیچ منبع درآمدی اداره شده و تمام هزینه‌ها را خودمان پرداخت کرده‌ایم. با این حال، این مسیر را ادامه می‌دهیم و همچنان ابزارها و سرویس‌های رایگان بیشتری را با کمک همین جامعه خواهیم ساخت.
حالا تنها مسیر درآمدی ما کانال یوتیوب WhiteDNS است. اگر می‌خواهید از این حرکت حمایت کنید، کانال را سابسکرایب کنید و ویدیوها را ببینید. همین همراهی کمک می‌کند WhiteDNS مستقل، فعال و جامعه‌محور باقی بماند.
📺
https://www.youtube.com/@WhiteDNS
ممنون که بخشی از این مسیر هستید
❤️
تیم WhiteDNS</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/whitedns/1555" target="_blank">📅 10:10 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-1553">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">WhiteAesther V1.2.0    دو پروتکل جدید، رفع مشکل قطعی، و مسیریابی اپ به اپ  از این آپدیت سه تا قابلیت جدید اضافه شده و سه تا مشکل قدیمی رفع شده. همه‌شون رو اینجا خلاصه کردم.
✅
چی اضافه شد  ۱. دو پروتکل جدید: WireGuard و WARP in WARP  تا الان فقط MASQUE (روی…</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/whitedns/1553" target="_blank">📅 09:15 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-1552">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IsXx1OJI_TwnDKIG-OxJjGuVGnK0qOk9RqwSUnKo7zDQ6JZKRvhKVbclj3auS20p69nNQJtplUfpQbVHs-2nsJeU3idxAwmb9BaY1SDe3RqygKYjy7kBkNiFMORRtKkSQJCaC79q4wi8rWdiV4OJCv-erLJEUvS54irDy_Cc51K_wTW4kqJzswm40G0lgtF2XZiZkU9qq5jnZmiV8Hfz-yvoNjmGRYBLg-vJX38Uj6puEF_ywh3FiRXYqteP-B4gB6NuST5PQRLQGSG2AbJ9QRcIVvNXFbGJQxXTyphfkdm7fc4VQGj3mlQ74L8ygxGKgLquMZHBIHqPtRqZr4Lt6A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سلام خدمت همه دوستان عزیز
✍️
از دیروز گزارش های زیادی روی WhiteVPN روی گوشی های قدیمی گرفتیم که بهمون گفتید نصب نمیشه، یا نصب میشه ولی میزنید روی اتصال، اررور میگیرید.
ما سعی کردیم توی ورژن ۱.۶.۱ که از لینک زیر میتونید دانلود کنید این مورد رو حل کنیم.
حالا گوشی های اندروید قدیمی‌تر هم میتونن بدون دردسر وصل بشن.
همچنین مشکل کانکشن هایی که camouflage داشتند هم توی این ورژن حل شده.
تغییر دیگه،ای نداشتیم  جز این دو مورد.
دانلود آخرین نسخه
https://github.com/WhiteDNS/WhiteVPN/releases/latest
با تشکر
تیم WhiteDNS</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/whitedns/1552" target="_blank">📅 06:55 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-1550">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/FC4o6mLJFWIJ4cO19kZ22z7tAwpA8fzj1INwUsqQR14zu4DS-yXOyhovugI-7mFfrVKze49ubGC0i7LWL_5Syo3Lwua88wtjcJKv-rGNJGQWjADvQDvaa5AHpFVQg8zsx-_8mlo6oOcP7Y2AdCQTArifHj5GOEtRiHm_YgyzFXYg1CvF60a8ViQ2OgoORN_p9SsFS6zeinYyLnCd6Dr0YgRh6rr2_8sCjRltm8iAhFZynPcZE5Izt0JKFEa2y5vOiJXxgtlaH_oK-gqzA-WdppK68LhTQiabaValk80KtNCxavsQh0aJl518Vwp125sRdQus8XxtGaI7CXA4DaCW3A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/U0JyOZFG1L2q20I_lhbscrjzhTQalBaGHaO5h0_7xZpMWBFQVnH2mbw_Ddg8j2KGqZuwk-6NrpQBrEhmEHkNWga0j9nDG6j2DyxMhEeY677vqjgAglP5_XqfNo3dmlRbxpqLS1Bolh0bBQSPlxHDzeYmU9uU3xL8xGYivrwZtqF3lRXRmMTwA7tUvwn7Lt6stgk8qUygKvi6HK1xk05kKxBpPsqAk5_c-c3SM7B7p5X21wRbDgg0ErqUdqzBV46IuwovULMLsHtywQ-IP7LWEIVa4aoUR6D6ZyVwaPoI5YiHNbIxZe8XSO6VZmRDgaPqpHOrdVwpXGFMAufra-R6oA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">دوستان عزیز
لینک ساب رو باید بعد از کلیک کردن روی دکمه Raw مشابه به عکسی که گذاشتیم کپی کنید.
لینک
صحیح WhiteDNS Sub
https://raw.githubusercontent.com/iampedii/whitedns-sub/refs/heads/main/mihomo.yaml</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/whitedns/1550" target="_blank">📅 05:26 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-1548">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromCore Forge</strong></div>
<div class="tg-text">🚀
CoreForge Build آپدیت جدید منتشر شد
https://testflight.apple.com/join/DRkT6zny
این نسخه یکی از بزرگ‌ترین آپدیت‌های CoreForge تا امروز محسوب میشه.
از Build 90 تا Build 100 طی حدود ۲۰ روز:
• 214 Commit
• بیش از 411 فایل تغییر کرده
• بیش از 86,000 خط کد جدید اضافه شده
• چند Engine و Protocol جدید از پایه اضافه شده
• بخش بزرگی از سیستم Connection، Routing، Failover و Config Management بازطراحی شده
###
🧩
پروتکل‌ها و Engineهای جدید
🔹
OpenVPN
* پشتیبانی مستقیم از فایل‌های .ovpn
* UDP و TCP
* AES-GCM / AEAD
* AES-CBC برای بعضی سرویس‌های قدیمی‌تر
* TLS-Crypt
* Multi-Remote / Multi-Address
* Username / Password
* Client Certificate
* OpenVPN Subscription
* پشتیبانی بهتر از ProtonVPN، VPNGate، SoftEther و کانفیگ‌های مشابه
🔹
Tailscale
* اتصال مستقیم به Tailnet
* انتخاب Exit Node
* MagicDNS
* مدیریت Account داخل CoreForge
* امکان اتصال به Exit Node حتی بدون انتخاب Config معمولی
🔹
Cloudflare WARP / MASQUE
* WARP به‌عنوان یک Outbound واقعی
* MASQUE روی HTTP/2 و HTTP/3
* امکان استفاده داخل Chain
* WARP Endpoint Scanner برای پیدا کردن Endpoint بهتر
* تست Endpoint با handshake واقعی MASQUE، نه فقط TCP Ping
🔹
mKCP
* پشتیبانی از mKCP مربوط به Xray
* همه Header Typeهای اصلی
* قابل استفاده با VLESS و Trojan
🔹
ECH
Encrypted ClientHello حالا به صورت واقعی داخل CoreForge اجرا میشه و برای بعضی Transportها از جمله Hysteria2 هم اضافه شده.
###
⚡
Load Balancer و Failover
Load Balancer فقط اسم نیست و حالا Connectionها واقعاً بین Nodeهای انتخاب‌شده مدیریت میشن.
همچنین:
* Config فعال داخل برنامه نمایش داده میشه
* Exit IP بعد از تغییر Node آپدیت میشه
* Dead Server Detection سریع‌تر شده
* Backup Node از قبل آماده نگه داشته میشه
* اگر Config فعلی از کار بیفته، CoreForge می‌تونه بدون Disconnect کامل به Backup منتقل بشه
* Backup Pool بعد از Failover دوباره پر میشه
###
🌐
Routing
سیستم Routing هم تغییر زیادی کرده:
* Routing Profile شبیه Shadowrocket
* Rule Actions
* Iran Direct Preset
* Iran 2026 Rules
* category-ir
* Import کردن Routing Rules از فایل
* Fragment به‌عنوان Routing Target
###
📂
Configs و Subscriptionها
مدیریت Configها تقریباً کامل بازطراحی شده:
* Swipe برای Ping / Edit / Share / Delete
* Drag & Drop برای مرتب کردن Sectionها
* Groupهای Local
* Bulk Actions
* forge:// Chain Links
* Tap-to-Ping-and-Connect
* Import QR Code از داخل عکس
* Subscription Folder
* Rename / Reorder / Export
* Auto Update جداگانه برای هر Subscription
* Plan Status
* تقویم شمسی
مشکل فایل‌های OpenVPN بزرگ هم برطرف شده؛ برای مثال اگر یک فایل شامل ده‌ها یا صدها Profile باشه، دیگه همه‌ی اون‌ها به‌عنوان یک Config خراب Import نمیشن و Profileها جدا میشن.
###
🔧
Fixهای مهم
در این نسخه تعداد زیادی Bug مهم هم برطرف شده، از جمله:
* Crash روی تعداد زیاد Config
* مشکل Import بعضی لینک‌های VMessAEAD
* مشکل gRPC پشت Cloudflare
* مشکل XHTTP که Connect می‌شد ولی Traffic عبور نمی‌کرد
* مشکل REALITY و extra
* اصلاح UUIDهای VLESS
* Lag شدید Config List
* Writeهای اضافی Keychain
* آپدیت نشدن Connection Details بعد از Failover
* UDP برای VMess، Shadowsocks و SOCKS
* UDP Associate برای Trojan
* gRPC MultiMode
* pinnedPeerCertSha256
* PattNG Fragment / Cipher Suite / Unsafe Fingerprint
###
📱
iPad و UI
* پشتیبانی بهتر از Stage Manager
* Split View
* Resizable Window
* تغییرات Liquid Glass
* اصلاح Light Mode
* بهبود Tab Bar و Headerها
---
⚠️
نکته مهم درباره Build
این نسخه تغییرات خیلی زیادی داشته و طبیعتاً
۱۰۰٪ تضمین نمی‌کنیم که تمام قابلیت‌های جدید روی تمام Serverها، ISPها و Configها بدون مشکل کار کنند.
بعضی قابلیت‌ها هنوز در مرحله‌ی تست واقعی توسط کاربران هستن و ممکنه روی یک Server عالی کار کنن ولی روی Server یا Network دیگه Fail بشن.
به‌خصوص قابلیت‌های جدیدی مثل:
Tailscale / WARP / OpenVPN / ECH / Chainهای پیچیده / بعضی حالت‌های VLESS و REALITY
هنوز نیاز به تست گسترده روی Serverها و اینترنت‌های مختلف دارن.
پس اگر چیزی Connect نشد یا Connect شد ولی Traffic نداشت، حتماً گزارش کنید و در صورت امکان Config، Log و نوع اینترنت رو هم بفرستید.
Build بیشتر از اینکه «نسخه نهایی بدون باگ» باشه، یک جهش بزرگ برای CoreForge ـه و Feedback شما مستقیم روی Fixهای نسخه‌های بعدی تأثیر می‌ذاره.
🛠️
CoreForge Build
⚒️</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/whitedns/1548" target="_blank">📅 15:07 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-1545">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/Zy0bXCVBjcITqYw7BajCP0gNi7fNM9-cM7M2STtZzFthQqXYX_paRBEwdlR5xw_rzcppRrRgsr-gyhKSux9lfy-_Hj8v45ILnJ-kcr_9-E9x-elcz81U5b9gRb1ccpPPHNRib81m6MuT8Bpl_jK9nZgXmIP6-BmIDMPIK62bLKHR2eqpF31-zEqOHU7JQjuf5VaQHyEPgD0Ksvi_XZo8GewxzxK7cWes_JNpdzsrTbXwCzYWr0VIBFlIJk1SfWpt1hWM7A6yvTwpQIM9DU-hvc2-nz8IDvF544NRNZFlV8kqEFfVchsw6tWtTVQXAKwd1eT9s1Kf11NLNJkO9cJbQg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">WhiteAesther
V1.2.0
دو پروتکل جدید، رفع مشکل قطعی، و مسیریابی اپ به اپ
از این آپدیت سه تا قابلیت جدید اضافه شده و سه تا مشکل قدیمی رفع شده. همه‌شون رو اینجا خلاصه کردم.
✅
چی اضافه شد
۱. دو پروتکل جدید: WireGuard و WARP in WARP
تا الان فقط MASQUE (روی H3 یا H2) داشتیم. حالا از Routes ← Manual ← Protocol می‌تونی این دو تا رو هم انتخاب کنی:
▫️
WireGuard —
سریع‌تره، ولی روی UDP کار می‌کنه
▫️
WARP in WARP —
یک تونل داخل تونل دیگه، کندتر ولی شناسایی‌ش سخت‌تره
⚠️
هر دوی این‌ها UDP هستن. اگه شبکه‌ات UDP رو کامل بسته باشه (مثل همراه اول این چند وقت اخیر) اصلاً وصل نمی‌شن — اونجا MASQUE H2 که روی TCP کار می‌کنه انتخاب درسته.
۲. بکاپ هویت — راه‌حل قطعی مشکل «چند بار نصب کردم دیگه وصل نمی‌شه»
دلیل اون مشکل این بود که هر نصب، یک هویت تازه از Cloudflare می‌گرفت، و بعد از چند بار ثبت‌نام از یک آی‌پی، دیگه هویت جدید نمی‌داد. حالا می‌تونی هویتت رو قبل از حذف اپ ذخیره کنی و بعد از نصب مجدد برگردونی.
۳. Split tunnel — انتخاب اینکه کدوم اپ‌ها از تونل رد بشن
از Traffic ← Apps: همه اپ‌ها، فقط چندتا اپ خاص، یا همه به‌جز چندتا اپ خاص (مثلاً بانک یا اپ‌های داخلی).
🛠
چی رفع شد
▫️
ثبت‌نام مشترک بین پروتکل‌ها — امتحان کردن هر سه پروتکل قبلاً ۳ بار ثبت‌نام می‌خرید. حالا یکی مشترکه.
▫️
WireGuard و WARP in WARP دیگه روی "trying" گیر نمی‌کنن — از تا ۹ دقیقه بی‌نتیجه، به معمولاً چند ثانیه.
▫️
باگ ساب عوض‌شده که نودهای قدیمی رو نشون می‌داد — درست شد.
📌
آموزش: Split tunnel
۱) Traffic ← Apps
۲) یکی از سه حالت: All apps / Only these apps / All except these
۳) با سرچ اپ‌های موردنظر رو پیدا کن و سوییچشون رو بزن
برای بانک یا اپ داخلی: All except these بزن و همون یکی دو تا رو انتخاب کن.
📌
آموزش: بکاپ هویت
Settings ← Identity & access → Save a backup (قبل از حذف اپ) / Restore from a backup (بعد از نصب مجدد)
⚠️
این فایل مثل رمز عبوره، رمزگذاری نشده — جایی نگهش دار که رمز عبور نگه می‌داری.
https://github.com/WhiteDNS/WhiteAestherMobile/releases/latest
@whitedns</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/whitedns/1545" target="_blank">📅 12:31 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-1535">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IikZ_Tj2DfOq6kPuyfalFkgbpYU0CDJLwVoPzA_t3YjVNTELqPYzUPMzFhEnZPjh-C3aHmV9HK1GVvmm7j7_Mm7so5BEW6q9drir4inNASULIcqQYUOKE2ZdQ_OXgu9-sSD0mn0oP5qOQ-WybYGBH59IxA_97C0LB2GHJ4CKNomD3CjEJdeoCsnE6GBZA0fWXIuKu5h806luJuNJLyn6RzAqXopn4crXEUgonzXfpaHmamez6-R9SUQ_JYryjgNKNCSQ9XwPKsE0qjZW4FrCd1BeyZKzA1bGBGqNWrDgzlKGdjbLq8kjO3d8nemxt9DpsbrPRJsJSwTHUn1JHsarTA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">WhiteVPN v1.6.0 منتشر شد
🚀
یکی از بزرگ‌ترین به‌روزرسانی‌های WhiteVPN آماده است؛ با امکاناتی که اتصال‌ها را قدرتمندتر، انعطاف‌پذیرتر و قابل‌کنترل‌تر می‌کند:
📺
پشتیبانی کامل از Android TV
🔗
زنجیره کردن دو اتصال برای امنیت و انعطاف بیشتر
🛡
پشتیبانی از
AmneziaWG v3
و تنظیمات پیشرفته WireGuard
📥
وارد کردن مستقیم لینک‌های
Hysteria2
و
WireGuard
⚡
تست اتصال‌ها از تمام سابسکریپشن‌ها
🌐
بهبود سازگاری، پایداری و رابط فارسی
اگر از WhiteVPN استفاده می‌کنید، همین حالا به نسخه
۱.۶.۰
به‌روزرسانی کنید.
این نسخه با کمک بازخوردهای شما ساخته شده است. اگر مشکلی دیدید یا پیشنهادی داشتید، حتماً در گروه با ما در میان بگذارید.
🤍
WhiteVPN v1.6.0 — دو مسیر، یک اتصال قدرتمندتر.
📥
Github Release
https://github.com/WhiteDNS/WhiteVPN/releases/tag/v1.6.0</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/whitedns/1535" target="_blank">📅 09:06 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-1534">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">از این به بعد کانفیگ های بیشتری داخل ساب ما خواهد بود.
هر ۳۰ دقیقه بیشتر از ۲۲۰هزار کانفیگ جدید تست میشن و خروجی اونها بین ۲۰۰۰ تا ۳۰۰۰ کانفیگ با کیفیت و سریع خواهد بود.
تعداد کانفیگ های حاضر: ۳۳۵۳
تیم WhiteDNS</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/whitedns/1534" target="_blank">📅 07:49 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-1531">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">https://github.com/iampedii/whitedns-sub
لینک ساب برای استفاده در برنامه های white</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/whitedns/1531" target="_blank">📅 18:40 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-1528">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">👆
whiteAesther  android V1.1.0
در این نسخه از اپ اندروید شما میتونید با  قرار دادن یک کانفیگ ای پی خودتون را ثابت کنید و احتمالا خیلی از مشکلات مربوط به Gemini , Chatgpt و بقیه هوش مصنوعی ها و وبسایت هایی که روی لوکیشن حساس هستند  حل خواهد شد
نکته  خیلی مهم برای نسخه اندروید :
⚠️
⚠️
⚠️
⚠️
⚠️
⚠️
بسته به نوع کانکشن و موارد دیگر ممکن هست 1-5 دقیفه بار اول طول بکشه که شما موفق به اتصال بشید . ولی در دفعات بعدی این موضوع خیلی سریع خواد بود .</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/whitedns/1528" target="_blank">📅 17:47 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-1527">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">WhiteAesther
android V1.1.0
🔥
🔥
🔥
🔥
🔥
🔥
قابلیت Exit Chain
از این نسخه می‌تونی بعد از تونل، یک ایستگاه دوم اضافه کنی.
یعنی چی؟ تا الان ترافیک تو از سرورهای Cloudflare بیرون می‌رفت و سایت‌ها آی‌پی Cloudflare رو می‌دیدن. حالا می‌تونی سرور شخصی خودت (یا سابسکریپشنی که داری) رو آخر مسیر بذاری، و سایت‌ها آی‌پی اون سرور رو ببینن.
مسیر ترافیک این شکلی می‌شه:
گوشی ← تونل رمزنگاری‌شده ← سرور خودت ← اینترنت
به چه دردی می‌خوره؟
▫️
سایت‌هایی که آی‌پی‌های Cloudflare رو بلاک کردن (بانک‌ها، بعضی سرویس‌های خارجی، بعضی بازی‌ها)
▫️
وقتی به آی‌پی یک کشور مشخص احتیاج داری
▫️
و مهم‌تر از همه: اگه شبکه‌ات اصلاً تونل رو بلاک کرده، می‌تونی تونل رو دور بزنی و مستقیم از سرور خودت استفاده کنی
پروتکل‌های پشتیبانی‌شده: vless vmess trojan shadowsocks hysteria2 و بقیه — چه لینک سابسکریپشن، چه کانفیگ تکی که دستی می‌چسبونی.
📌
آموزش — ۵ قدم
۱) اپ رو به نسخه ۱.۱.۰ آپدیت کن.
۲) برو به تب Routes ← گزینه Exit chain.
۳) کلید Exit chain رو روشن کن.
۴) توی کادر Add a subscription لینک سابسکریپشنت رو بذار و Add رو بزن. اگه فقط چند کانفیگ تکی داری، از Paste nodes by hand استفاده کن — هر کانفیگ توی یک خط.
۵) برگرد به Home و وصل شو. تمام.
⚠️
سه نکته که حتماً باید بدونی
۱. لیست سرورها فقط بعد از وصل شدن میاد
قبل از اتصال قسمت Nodes خالیه و این ایراد نیست. سابسکریپشن تو از داخل تونل دانلود می‌شه تا شبکه‌ات نفهمه داری چی می‌گیری. پس اول وصل شو، بعد برگرد به Routes ← Exit chain تا لیست سرورها رو با پینگ‌شون ببینی.
انتخاب سرور قطع و وصل نمی‌خواد — روی همون اتصال جابه‌جا می‌شه.
۲. گزینه Dial nodes through the tunnel
پیش‌فرض روشنه و بهتره روشن بمونه: شبکه/اپراتور تو هیچ‌وقت آدرس سرورت رو نمی‌بینه، و سرورت هم آدرس واقعی تو رو نمی‌بینه.
🔸
ولی اگه اپ اصلاً وصل نمی‌شه یا خیلی طول می‌کشه، این گزینه رو خاموش کن. اون‌وقت WhiteAesther تونل رو کامل رد می‌کنه و مستقیم به سرور خودت وصل می‌شه — دقیقاً برای شبکه‌هایی مثل همراه اول که تونل رو می‌بندن، همین حالت جواب می‌ده و خیلی سریع‌تر هم وصل می‌شه.
۳. Coverage باید روی Whole device باشه
توی تب Traffic. اگه روی Proxy only باشه، Exit chain کار نمی‌کنه و اپ بهت تذکر می‌ده.
💾
حجم اپ بیشتر شده
از حدود ۸ مگابایت رسیده به ۴۷ تا ۵۷ مگابایت. دلیلش موتور جدیدیه که این قابلیت رو اجرا می‌کنه. اگه Exit chain رو روشن نکنی، اپ دقیقاً مثل قبل کار می‌کنه.
▫️
arm64-v8a — تقریباً همه گوشی‌های ۲۰۱۷ به بعد. از این شروع کن
▫️
armeabi-v7a — گوشی‌های قدیمی‌تر و اقتصادی
▫️
universal — اگه مطمئن نیستی (حجمش سه برابره)
⬇️
https://github.com/WhiteDNS/WhiteAestherMobile/releases/latest
اگه مشکلی خوردی، از Settings ← Diagnostics گزارش بگیر و بفرست — از این نسخه لاگ موتور Exit chain هم داخلشه.
@whitedns</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/whitedns/1527" target="_blank">📅 17:45 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-1526">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">📺
خبر خوب برای کاربرهای Android TV
در ورژن بعدی WhiteVPN پشتیبانی کامل از Android TV اضافه شده. تا فردا نسخه جدید اپ اندروید هم ریلیز میکنیم
❤️</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/whitedns/1526" target="_blank">📅 17:34 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-1525">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">👆
whiteAesther V1.5.2 desktop
در این نسخه از اپ دسکتاپ شما میتونید با  قرار دادن یک کانفیگ ای پی خودتون را ثابت کنید و احتمالا خیلی از مشکلات مربوط به Gemini , Chatgpt و بقیه هوش مصنوعی ها و وبسایت هایی که روی لوکیشن حساس هستند  حل خواهد شد</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/whitedns/1525" target="_blank">📅 16:54 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-1524">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">whiteAesther
V1.5.2 desktop
🔥
🔥
🔥
🔥
🔥
🔥
🔗
قابلیت جدید: Exit chain (زنجیره‌ی خروج)
🔥
🔥
🔥
تا حالا وقتی وصل می‌شدید، ترافیک‌تان امن و رمزنگاری‌شده بود — ولی آدرسی که سایت‌ها می‌دیدند همچنان نزدیک خودتان بود. این ایراد ما نبود: WARP کلادفلر عمداً کشور شما را عوض نمی‌کند، از نزدیک‌ترین نقطه خارج می‌شود و همان‌جا را هم geolocate می‌کند. برای همین خیلی‌ها بعد از اتصال موفق، باز هم به سرویس‌های خارجی دسترسی نداشتند.
Exit chain یک هاپ دوم اضافه می‌کند. ترافیک اول از تونل رد می‌شود، بعد از داخل تونل به نود خودتان می‌رسد و از آنجا وارد اینترنت می‌شود. آدرسی که سایت‌ها می‌بینند، آدرس نود شماست.
دو نکته‌ی مهم در طراحی:
▫️
نود از داخل تونل شماره‌گیری می‌شود — یعنی شبکه‌ی محلی شما فقط یک اتصال عادی به کلادفلر می‌بیند، نه آدرس نود و نه SNI آن.
▫️
به همین دلیل، نودی که از ایران فیلتر شده باز هم کار می‌کند — چون از شبکه‌ی کلادفلر به آن وصل می‌شویم، نه از اینجا.
━━━━━━━━━━━━━━
📘
آموزش
۱. بالای پنجره روی Advanced بزنید، از منوی سمت چپ Exit chain را انتخاب کنید.
۲. دو کلید را روشن کنید:
• Route through a second hop — خود قابلیت
• Dial nodes through the tunnel — پیش‌فرض روشن است، همین‌طور بگذاریدش
۳. نودتان را اضافه کنید، به یکی از دو روش:
• Subscriptions — لینک ساب را بگذارید و Add بزنید (خودش به‌روز می‌ماند)
• Configs pasted by hand — کانفیگ‌ها را خطی یکی paste کنید و Apply بزنید
vless · vmess · trojan · ss · hysteria2 · tuic همه مستقیم پشتیبانی می‌شوند؛ لازم نیست چیزی را تبدیل کنید.
۴. پایین صفحه در بخش Nodes نودها ظاهر می‌شوند با پینگ واقعی‌شان از پشت تونل. با Test هر کدام را بسنجید و با Use یکی را انتخاب کنید.
۵. بالا سمت راست Save profile را بزنید تا دفعه‌ی بعد هم فعال باشد.
━━━━━━━━━━━━━━
⚙️
کدام حالت را انتخاب کنم؟
• Whole machine — کاری لازم نیست، پروکسی سیستم خودکار روی زنجیره تنظیم می‌شود. برای اکثر کاربران همین درست است.
• This app only — مرورگر یا برنامه‌تان را روی آدرسی که در همان کارت نوشته شده تنظیم کنید (معمولاً
127.0.0.1:1820
).
برای اطمینان، کارت What websites see در صفحه‌ی اصلی آدرس واقعی خروجی‌تان را نشان می‌دهد. اگر برچسب Through your node را دید، زنجیره برقرار است.
@whitedns
https://github.com/WhiteDNS/WhiteAesther</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/whitedns/1524" target="_blank">📅 16:51 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-1523">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/aWiIcQ6bDRE60swwr6g-Uy6XYB_W8TJPx0-D1WLIGDxvuAwK6QadegZX6a9xG52DZgkpGcVbZuRWMpDiHqqsI3vAjdu4n6bsKA6i75XaiAwwaJA8aMQYSu_yqf0W00EaQCG1YJDBgNOBM_OhtMk_8qO8AA2R7qlrulKUWOerA4JwGeVfCEuW9H6E4Bfxj9yVkspP8cQCzaKYfe6Dn2NuQrVFFaugBDh3KikCDGTQP0VcocmlHlGEF3SpA9GnU7yJLVXwHivltcUOue1Do3ZlLCKMh44J2vG-RxSgbK-WfGPTR5N7kOcAwJN85KjhS5CUw5XKPlWD9Qm7YU4SJmkdDA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🌐
کلاینت WhiteAesther
(دانلود همزمان برای اندروید و ویندوز / دسکتاپ)
اگر به دنبال یک اتصال فوق‌العاده پایدار، سریع و امن با پروتکل نوین MASQUE H2 هستید، نرم‌افزار WhiteAesther در دو نسخه دسکتاپ و موبایل در دسترس شماست.
✨
قابلیت‌ها و ویژگی‌های کلیدی:
🔹
مبتنی بر پروتکل پرسرعت و مدرن MASQUE H2
🔹
اتصال سریع با یک کلیک (Zero-Config)
🔹
پایداری بالا و پینگ عالی مناسب وب‌گردی، گیمینگ و استریم
🔹
سیستم محافظت از کل ترافیک دستگاه (IPv4 + IPv6)
🔹
قابلیت Reconnect خودکار و Killswitch داخلی
🔹
رابط کاربری بسیار روان، تاریک (Dark Mode) و مدرن
━━━━━━━━━━━━━━━━━━━━
📥
لینک‌های دانلود مستقیم آخرین نسخه از گیت‌هاب:
📱
دانلود نسخه اندروید (Android APK):
🔗
https://github.com/WhiteDNS/WhiteAestherMobile/releases/latest
💻
دانلود نسخه دسکتاپ (Windows / PC):
🔗
https://github.com/WhiteDNS/WhiteAesther/releases/latest
━━━━━━━━━━━━━━━━━━━━
💡
پیشنهاد: این پست را برای دسترسی سریع به هر دو نسخه ذخیره (Save) یا پین کنید.
🆔
@whitedns</div>
<div class="tg-footer">👁️ 9.71K · <a href="https://t.me/whitedns/1523" target="_blank">📅 16:38 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-1522">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/WXTdoGI6VSfs9JRpotMEpXZSPeuDuT9sRlKOOpJgCPF4QQq7b_sgOJi5bNvX7oZUIBPtfYg9VFVHM1bUsGfvwGWaUUCxjiLCytPZAkPgscap53UNV1UeL7fBPd6Gli2foo8AhmSpgRItfUQWQaTMrxHgCYRtkvpHuwurgtox9-Q2OZrnQTQt_NSO9AeNwP5F1ZCA0MSSVKgEVWas9XWbD4MMpkNA-ClrV1vVQt_0RTbtcr2z6ua2slqgym9xsymrc1sR2hAddI4y4GvqUVUKcAtgUxl_cCIVPGymsYFvix_B7_E4wWFfD43NoVGAxh9Xiop5qoXjlOovCMOOGPfjyQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚀
دسترسی آزاد و امن به اینترنت با WhiteVPN (نسخه موبایل و دسکتاپ)
اگر به دنبال یک کلاینت یکپارچه، سبک و حرفه‌ای هستید، WhiteVPN با رابط کاربری مدرن در دسترس شماست!
⚙️
قدرت گرفته از هسته Mihomo:
این برنامه بر پایه هسته قدرتمند Mihomo (مشابه کلش و متا) توسعه یافته است که بالاترین سطح پایداری و سرعت را در دور زدن محدودیت‌ها برای شما فراهم می‌کند.
⚠️
توجه مهم:
این اپلیکیشن کاملاً سورس‌باز (Open-Source) است و در Google Play یا App Store منتشر نشده است. تنها منبع رسمی برای دانلود، مخزن گیت‌هاب پروژه است.
✨
ویژگی‌های کلیدی:
🔹
پشتیبانی همزمان از ویندوز، مک، لینوکس و اندروید
🔹
رابط کاربری ساده و اتصال تنها با یک کلیک
🔹
سیستم پراکسی جامع و تونلینگ کل سیستم (System-wide)
🔹
مدیریت پیشرفته سرورها و پایداری بالا در اتصالات
━━━━━━━━━━━━━━━━━━━━
📥
دانلود مستقیم آخرین نسخه از گیت‌هاب (رسمی):
📱
نسخه اندروید (Mobile):
🔗
https://github.com/WhiteDNS/WhiteVPN/releases/latest
💻
نسخه دسکتاپ (Windows / macOS / Linux):
🔗
https://github.com/WhiteDNS/WhiteVPN-Desktop/releases/latest
━━━━━━━━━━━━━━━━━━━━
💡
برای دانلود، وارد لینک‌های بالا شده و از بخش "Assets" فایل متناسب با دستگاه خود (فایل apk برای اندروید و فایل‌های نصب برای ویندوز/مک) را دانلود کنید.
🆔
@whitedns</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/whitedns/1522" target="_blank">📅 16:38 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-1521">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RLnUgLMcF2ioj5-SCW6QAUZe0JOpQ3xSqJ5N5TSQhW7KwHp5fSSJkWMbhRo_VZBRrnrvbDv-66sLq9kK5I09ClibSKdD9OPoJ2h_NKKKcBo-aqYDauNpA64xrUhrDAV6tAeB9O4E6ONsyV9ZPFjNaKfOS_AEKbsEswlnSaAYpifOU2O1PFwEJnThO41N_toy6dIvJNi3Bh0VUvA5_dAwG75eVp8ac7NRwYYf2dJlLmT2p3Ledz5AR7TJc1vOxkJsP25DIw4ZZcom22J99kEGTPDANftEfRVcWNB3BvwXSGSEDNxOPD8PwOM-u9KvF-FckeLTY9cYvRk3KwHw7jFShg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏯️
آموزش کامل اپلیکیشن WhiteAesther
📍
تماشا در یوتیوب
https://youtu.be/cRfqxbDY1Dg</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/whitedns/1521" target="_blank">📅 18:15 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-1518">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">نسخه جدید WhiteVPN v1.5.0  توی این نسخه سعی کردیم پیدا کردن یک اتصال خوب و سریع خیلی راحت‌تر بشه. اول همهٔ اتصال‌ها بررسی می‌شن و بعد، اگر دوست داشته باشید، می‌تونید سرعت هرکدوم رو جداگانه تست کنید.   حالا می‌تونید زمان، تعداد و حجم تست‌ها رو هم خودتون تنظیم…</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/whitedns/1518" target="_blank">📅 14:41 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-1517">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromBlue Knight(𝑫𝒊𝒂𝒏𝒂🍓)</strong></div>
<div class="tg-text">آموزش نصب پنل رایگان StanNg روی Railway
بدون VPS و بدون هزینه کانفیگ V2Ray بگیر
🔥
از صفر تا صد کامل توضیح دادم، مناسب تازه‌کارها هم هست.
لینک ویدیو:
https://youtu.be/sdiGXCDsDvQ
سوالی داشتی بپرس
👇</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/whitedns/1517" target="_blank">📅 11:57 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-1515">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">🌎
نسخه جدید WhiteVPN v1.5.0
👆
تغییر های این ورژن کاملا روی فیدبک های شما بوده، و به نظرم از لحاظ تجربه کاربری تغییر خیلی خوبی داشتیم.
😆
ممنون از فیدبک هایی که به ما میدید.</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/whitedns/1515" target="_blank">📅 08:08 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-1510">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">WhiteVPN-V1.5.0-arm64-v8a.apk</div>
  <div class="tg-doc-extra">35.7 MB</div>
</div>
<a href="https://t.me/whitedns/1510" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">WhiteVPN V1.5.0</div>
<div class="tg-footer">👁️ 60.1K · <a href="https://t.me/whitedns/1510" target="_blank">📅 08:08 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-1509">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iAOUGRYu5BGphUeTyx5ETFUDMrUmkQdtvzMLTC3t-FcKrUhHngFoj9Wq8_LYHs-sd9_eK2CQM6MbB3kyluL-mDc0FalWQU0N_E_tRPxRfrQdTsSmbFXQcToA5nbopWweMpFIPBKFBi2h_oongUgC9w8b38PbHMsBu36URP4jZCZWlMh-vgC_8M6Bx88ekXwz_xMSaacfeCKCipRO5VgKXjn7_kk6SERgniJLqlhgh9Vto7XGepCKEid65CrhuRhj4gnzCQsbD5xXhZb-DckRu02vUioBg8IEsDfm6LvkgToqTkOOrD9y7TlCnV9U87OGm77jn_0hBgyjfFbJMEbMfw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نسخه جدید WhiteVPN v1.5.0
توی این نسخه سعی کردیم پیدا کردن یک اتصال خوب و سریع خیلی راحت‌تر بشه. اول همهٔ اتصال‌ها بررسی می‌شن و بعد، اگر دوست داشته باشید، می‌تونید سرعت هرکدوم رو جداگانه تست کنید.
حالا می‌تونید زمان، تعداد و حجم تست‌ها رو هم خودتون تنظیم کنید تا هم کمتر منتظر بمونید و هم مصرف اینترنت دست خودتون باشه. ظاهر و بخش‌های مختلف برنامه هم مرتب‌تر شدن تا انتخاب اتصال، عوض کردن سابسکریپشن و پیدا کردن تنظیمات راحت‌تر باشه.
⚡️
تست اتصال‌ها سریع‌تر، دقیق‌تر و مطمئن‌تر شده.
⚡️
برای گرفتن نتیجهٔ بهتر، تست تأخیر حالا از سرویس پایدار گوگل استفاده می‌کنه.
⚡️
تعداد اتصال‌های هم‌زمان، زمان انتظار و حجم تست سرعت قابل تنظیمه.
⚡️
تست سرعت دیگه خودکار انجام نمی‌شه و فقط برای اتصال‌هایی که خودتون بخواید اجرا می‌شه.
⚡️
تست تأخیر و سرعت از هم جدا شدن تا خطا و تداخل کمتری پیش بیاد.
⚡️
می‌تونید چند کشور و چند نوع اتصال رو هم‌زمان برای تست انتخاب کنید.
⚡️
انتخاب و مدیریت سابسکریپشن‌ها راحت‌تر شده و از صفحهٔ اصلی هم قابل تغییره.
⚡️
صفحهٔ تنظیمات، تونل تفکیکی، اطلاعات اتصال و چیدمان فارسی مرتب‌تر و ساده‌تر شده.
دانلود آخرین نسخه از گیت‌هاب
https://github.com/WhiteDNS/WhiteVPN/releases/latest</div>
<div class="tg-footer">👁️ 47.6K · <a href="https://t.me/whitedns/1509" target="_blank">📅 08:01 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-1508">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">نسخه جدید WhiteVPN v1.5.0
توی این نسخه سعی کردیم پیدا کردن یک اتصال خوب و سریع خیلی راحت‌تر بشه. اول همهٔ اتصال‌ها بررسی می‌شن و بعد، اگر دوست داشته باشید، می‌تونید سرعت هرکدوم رو جداگانه تست کنید.
حالا می‌تونید زمان، تعداد و حجم تست‌ها رو هم خودتون تنظیم کنید تا هم کمتر منتظر بمونید و هم مصرف اینترنت دست خودتون باشه. ظاهر و بخش‌های مختلف برنامه هم مرتب‌تر شدن تا انتخاب اتصال، عوض کردن سابسکریپشن و پیدا کردن تنظیمات راحت‌تر باشه.
⚡️
تست اتصال‌ها سریع‌تر، دقیق‌تر و مطمئن‌تر شده.
⚡️
برای گرفتن نتیجهٔ بهتر، تست تأخیر حالا از سرویس پایدار گوگل استفاده می‌کنه.
⚡️
تعداد اتصال‌های هم‌زمان، زمان انتظار و حجم تست سرعت قابل تنظیمه.
⚡️
تست سرعت دیگه خودکار انجام نمی‌شه و فقط برای اتصال‌هایی که خودتون بخواید اجرا می‌شه.
⚡️
تست تأخیر و سرعت از هم جدا شدن تا خطا و تداخل کمتری پیش بیاد.
⚡️
می‌تونید چند کشور و چند نوع اتصال رو هم‌زمان برای تست انتخاب کنید.
⚡️
انتخاب و مدیریت سابسکریپشن‌ها راحت‌تر شده و از صفحهٔ اصلی هم قابل تغییره.
⚡️
صفحهٔ تنظیمات، تونل تفکیکی، اطلاعات اتصال و چیدمان فارسی مرتب‌تر و ساده‌تر شده.
دانلود آخرین نسخه از گیت‌هاب
https://github.com/WhiteDNS/WhiteVPN/releases/latest</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/whitedns/1508" target="_blank">📅 08:01 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-1507">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">دوستان عزیز سلام
اپ CoreForge از تیم WhiteDNS ظرفیت جدید اضافه کرده برای کاربران IOS
https://testflight.apple.com/join/3htm1Whc
آموزش استفاده
https://youtu.be/filwdiPKN90?si=O-hvgeNw43t4BUmR
@WhiteDNS</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/whitedns/1507" target="_blank">📅 01:59 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-1506">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">💬
لینک ساب تیم WhiteDNS
https://github.com/iampedii/whitedns-sub</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/whitedns/1506" target="_blank">📅 01:54 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-1504">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">سلام دوستان :
❤️
اینقدر درخواست برای IP ثابت برنامه های  whiteAesther و whitevpn اومده که دیدیم بهتر هست ، یک پست براتون بگذارم
در حال حاضر  این امکان توی آخرین ورژن های این دو برنامه وجود ندارد
با اعضای تیم داریم روش کار میکنیم و امیدواریم طی روزهای آینده به دستتون برسونیم ، یکم به ما وقت بدید و صبور باشید.
ببخشید که انجام درخواست های شما گاهی طول می‌کشه، چون ما هم مثل تک تک شما درگیر کار و زندگی و مسائل خودمون هستیم و گاهی وقت کم میاریم
ولی مطمئن باشید ما همه پیام های شما را می‌خونیم و تا جایی که بتونیم ترتیب اثر می‌دیم ،
ارادتمند و کوچیک تک تک شما عزیزان دل
ویسپر</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/whitedns/1504" target="_blank">📅 16:18 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-1502">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">⚠️
موقت
به نظر میاد که دامنه
workers.dev
کلادفلر رفع فیلتر شده است</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/whitedns/1502" target="_blank">📅 19:19 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-1501">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/pfkj3GhaSSmpUXUAbfryASgWsFWceRrdAbkTXWwh6iYigfKZ6yTxIzL9-PzbNRtiPmPkEcAqLyjIpRU9v6WG8K6MyOTArkjGXJgDyqlLjt7Z1BTMqOCQb7t7Yt7cBle4xpMuoLeibeyAVmqXVwjlsv9bzR5NqWLgm4JWB4g1J3Jb6R6Ef9xlDv3j60PTdzNwvA_7j1L9c5KyjHPoo5WtH-EzibD09PZJeBJAqjD0dTe8s4oaiYLDAO5jZCckdAlYJLGFL5v4rPU_qOW2v4KryFADuxVQzASOEajA1NQtjxoJQp42jze34I22miobBuLGrPI7pbQlqzXFRfL52jk5SA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚫
چرا موقع ورود به Gemini با ارور ۴۰۳ مواجه می‌شویم و چطور حلش کنیم؟
خیلی از کاربران هنگام باز کردن
gemini.google.com
با خطای معروف زیر روبه‌رو می‌شوند:
403. That’s an error. Your client does not have permission to get URL / from this server.
🔍
دلیل این ارور چیست؟
سرویس‌های هوش مصنوعی مثل Gemini دسترسی کاربران برخی مناطق را به دلیل محدودیت‌های منطقه‌ای و حقوقی مسدود (Geo-block) می‌کنند. اما اگر از ابزارهای تغییر آی‌پی استفاده می‌کنید و باز هم این ارور را می‌بینید، علت معمولاً یکی از موارد زیر است:
1️⃣
نشت موقعیت (DNS یا WebRTC Leak):
با اینکه کانکشن شما وصل است، مرورگر از طریق درخواست‌های DNS یا قابلیت WebRTC، آی‌پی واقعی شما را لو می‌دهد.
2️⃣
شناسایی آی‌پی دیتاسنتر (Datacenter IP):
گوگل بازه‌های زیادی از سرورهای عمومی و تجاری را شناسایی کرده و مستقیماً مسدود می‌کند.
3️⃣
کش و کوکی‌های ذخیره‌شده:
مرورگر موقعیت قبلی شما را در کوکی‌ها نگه داشته است.
🛠
راهکارهای سریع برای رفع مشکل:
🔹
تست نشت آی‌پی (Leak Test):
ابتدا وارد سایتی مثل
ipleak.net
یا
browserleaks.com/ip
شوید و مطمئن شوید در بخش‌های WebRTC و DNS هیچ نشانی از آی‌پی واقعی یا DNS داخلی وجود ندارد.
🔹
استفاده از حالت ناشناس (Incognito):
یک پنجره Incognito / Private باز کنید یا کش و کوکی‌های مربوط به دامنه‌های
google.com
را پاک کنید.
🔹
فعال‌سازی حالت TUN Mode / روتینگ کامل:
مطمئن شوید کلاینت شما تمام ترافیک و به خصوص درخواست‌های DNS را هدایت می‌کند و ترافیک دامنه‌های گوگل به صورت Direct رد نمی‌شود.
🔹
تغییر نود یا کشور سرور:
اگر آی‌پی سرور فعلی توسط گوگل فلگ شده باشد، با جابه‌جایی نود یا تغییر لوکیشن معمولاً دسترسی بلافاصله باز می‌شود.
💡
اشتراک‌گذاری برای دوستانی که با دسترسی به جمینای مشکل دارند.
@whitedns</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/whitedns/1501" target="_blank">📅 15:31 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-1496">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/X8B8E-jt40MUa-7c2DPf89qGYsXSZdSdnyl6hfV5rNf3fpoBTJyLlrYUl7KQLN1KrWq1cNM591IPvs0wxOoCmHGDlfISW6ESCR_5ULnD67c_WbJtu7OwVl0Lj4rLcIFGL3psBzXRzcTH450AnHfQ3v6RANtxBm0_zaKUCfy_jHJWmJgJwl5pqFKQRUEKR5MC-eN9q8ThGASYFIGp-HNqAVMCnuhgEC8Y7JRM5qok8HkPQ3_V_uUDELZNzepFX_qIKZ7BUZCQYP_0jRuoUsoG-NiGGxqsak2CsUweRNNrLIEbB4r7f0Lbokl4PygassrLVV0A9Lvo6jPiFC7D0NJ5Lg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🌐
کلاینت WhiteAesther
(دانلود همزمان برای اندروید و ویندوز / دسکتاپ)
اگر به دنبال یک اتصال فوق‌العاده پایدار، سریع و امن با پروتکل نوین MASQUE H2 هستید، نرم‌افزار WhiteAesther در دو نسخه دسکتاپ و موبایل در دسترس شماست.
✨
قابلیت‌ها و ویژگی‌های کلیدی:
🔹
مبتنی بر پروتکل پرسرعت و مدرن MASQUE H2
🔹
اتصال سریع با یک کلیک (Zero-Config)
🔹
پایداری بالا و پینگ عالی مناسب وب‌گردی، گیمینگ و استریم
🔹
سیستم محافظت از کل ترافیک دستگاه (IPv4 + IPv6)
🔹
قابلیت Reconnect خودکار و Killswitch داخلی
🔹
رابط کاربری بسیار روان، تاریک (Dark Mode) و مدرن
━━━━━━━━━━━━━━━━━━━━
📥
لینک‌های دانلود مستقیم آخرین نسخه از گیت‌هاب:
📱
دانلود نسخه اندروید (Android APK):
🔗
https://github.com/WhiteDNS/WhiteAestherMobile/releases/latest
💻
دانلود نسخه دسکتاپ (Windows / PC):
🔗
https://github.com/WhiteDNS/WhiteAesther/releases/latest
━━━━━━━━━━━━━━━━━━━━
💡
پیشنهاد: این پست را برای دسترسی سریع به هر دو نسخه ذخیره (Save) یا پین کنید.
🆔
@whitedns</div>
<div class="tg-footer">👁️ 91.3K · <a href="https://t.me/whitedns/1496" target="_blank">📅 07:12 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-1495">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/a5LXdmUmurOhnYuVR0gi9TcIgSfmhHmYLMjIDGCy22shj6DPhTlJfCxwly63hKI2YVCxkl2ql49i3NA4D5ygpnGSIOdpjo9iWi8F6oa1r_VZXO3eRf7CZkJs4HWEdZwHFa0KQLGeeA7lGoP3jIxMNeq13IZpVqrjBqwhztdfGQfMlvJSuxFmt27J8M72BVeWEP3AflUBgmGAQ7_Is8zU4WwIGPA-EdkRYAAPNtQusKEg5a254OZuuLb59qsCq2HaDyJq3yWLsSQpPQXGESxpq86kJpDAeDiBNzvEawMmsWXTqe3TUHkSK5ieS6JfTgwHTfEVAJOGwLRGY4j-Ztr2bw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚀
دسترسی آزاد و امن به اینترنت با WhiteVPN (نسخه موبایل و دسکتاپ)
اگر به دنبال یک کلاینت یکپارچه، سبک و حرفه‌ای هستید، WhiteVPN با رابط کاربری مدرن در دسترس شماست!
⚙️
قدرت گرفته از هسته Mihomo:
این برنامه بر پایه هسته قدرتمند Mihomo (مشابه کلش و متا) توسعه یافته است که بالاترین سطح پایداری و سرعت را در دور زدن محدودیت‌ها برای شما فراهم می‌کند.
⚠️
توجه مهم:
این اپلیکیشن کاملاً سورس‌باز (Open-Source) است و در Google Play یا App Store منتشر نشده است. تنها منبع رسمی برای دانلود، مخزن گیت‌هاب پروژه است.
✨
ویژگی‌های کلیدی:
🔹
پشتیبانی همزمان از ویندوز، مک، لینوکس و اندروید
🔹
رابط کاربری ساده و اتصال تنها با یک کلیک
🔹
سیستم پراکسی جامع و تونلینگ کل سیستم (System-wide)
🔹
مدیریت پیشرفته سرورها و پایداری بالا در اتصالات
━━━━━━━━━━━━━━━━━━━━
📥
دانلود مستقیم آخرین نسخه از گیت‌هاب (رسمی):
📱
نسخه اندروید (Mobile):
🔗
https://github.com/WhiteDNS/WhiteVPN/releases/latest
💻
نسخه دسکتاپ (Windows / macOS / Linux):
🔗
https://github.com/WhiteDNS/WhiteVPN-Desktop/releases/latest
━━━━━━━━━━━━━━━━━━━━
💡
برای دانلود، وارد لینک‌های بالا شده و از بخش "Assets" فایل متناسب با دستگاه خود (فایل apk برای اندروید و فایل‌های نصب برای ویندوز/مک) را دانلود کنید.
🆔
@whitedns</div>
<div class="tg-footer">👁️ 60.2K · <a href="https://t.me/whitedns/1495" target="_blank">📅 07:12 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-1493">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/HYvQbUXul71AbXARjWpgsUAub-L55Qjw1k98h1aj3WtJiczdD7xSjYit3AiwELiWpTjom7tZDmXbSM3kljE0NmfD-n2B2tMhYV1fPETg-AuNxwf5v4PDWZsmPQMhWwYy3aOuNBpjrxLKw5e9jPplA7gpGTnDu6dh4xNwmMb0-hEljzdBCoU1U9F03TxgZCFCVzYm2aPeckMUHrU_mHbF92trWaxU1rwtC0lAHqCKva4GuK6z_rPiuSZL5H1kc8a9TQmzvbtFpDAUq1Jc168gJLKtTm2LAKq2PAPffR-t3hyC26zSNVs8Y9t0oK8h17-Xq9ku_rW_J1NGV7VLNVikpA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دوستان سلام :
برای حل این مشکل توی ورژن دسکتاپ و مبایل whitevpn لطفا ساب زیر را دستی وارد کنید
اگر به هر دلیلی ساب برای شما اپدیت نمیشه اول یک فیلترشکن روشن کنید که ساب را بتونید بگیرید و اپدیت کنید بعد استفاده کنید
https://raw.githubusercontent.com/iampedii/whitedns-sub/refs/heads/main/mihomo.yaml
@whitedns</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/whitedns/1493" target="_blank">📅 05:59 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-1491">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromxsfilternet | فیلترنت(امیرپارسا گودمن)</strong></div>
<div class="tg-text">🍷
درود به همه رفقا...
تمام
#نکات
واسه مشکل فیلتر شدن worker رو داخل این پست میگم:
👽
💻
طبق آموزش هایی که قبلا دادم با اپلیکیشن pattng و همچنین v2rayn در ویندوز میتونید مشکل فیلترشدن ورکر رو حل کنید و کانفیگ های -1 رو مجدد متصل کنید.
آموزش مروبطه:
👇
https://t.me/xsfilterrnet/3642
📱
داخل ios هم طبق تنظیمات یه ip تمیز پیدا کنید داخل کلاینت incy یا hiddify بزنید و فرگمنت رو روشن کنید متصل میشه.
یه روش دیگه بعد از بالا اومدن پنل استفاده از کانفیگ های فرگمنت برای bpb هست که با مقادیر low (1-1) رو متصل کنید
🔥
🔗
در مورد لینک ساب های raw هم به گفته خود bpb:
بچه‌ها اگر ساب Raw و کانفیگ TLS استفاده میکنید از این روش در v2rayNG/pattngاستفاده کنید، معلوم نیست تا کی کار کنه، اگر پایدار بود پنلو تغییر میدم.
این رو دو جا وارد کنید:
https://8.8.8.8/dns-query
۱. قسمت Remote DNS تنظیمات برنامه.
۲. ویرایش کانفیگ قسمت echConfigList.
با Mux خاموش
یه نکته دیگه از بچها اینترنت آزاد که جواب داده:
با ECH و استفاده از آدرس udp://1.1.1.1 میتونید فیلترینگ
pages.dev
و
workers.dev
رو دور بزنید.
💓
نکته ای هم که متین سنپای گفته:(همراه با ابزار جدید)
https://t.me/MatinSenPaii/4960
@xsfilterrnet
👑</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/whitedns/1491" target="_blank">📅 22:11 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-1489">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/T2PzUua2y1rRg4sOarEipJS4YEyaZZLrTujI9XL50JAbylUEr5Cn2NFX6LXbJX4P3gequc9zX_VHdv_SJpmbvfPsQeoBdL7AoavxdeD1KahBGLU3Hxjh8EErZiIKWBcZ8v3MUrl7QUfJZm2E4h1K8UekKi-DObXbKUHocjO9GYs2vbs_fO02k7vtdfJscoFTx4mPrTD3MULIBKvTLzkM0MMf7rnlX6tyjMtC_CYQeuvub7i0i4Iiiwg_8gkv1kLB6QRf_bBBDMdMNvoHKmLBrF9RlKyUmIhANypZ7RPRxCGfpWicigp_f0PAGzLySwNOh2YzqhE7iuL0tdHa78ahvA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💬
چطوری فیلتر شدن BPB و Workers رو دور بزنید؟   میتونید با رفتن به منو تنطیمات، فعال کردن گزینه Amnezia Noise فیلترینگ ورکر رو دور بزنید و به کانفیگ های ساب BPB Warp Pro و باقی Wireguard ها وصل بشید.  این مشابه گزینه فرگمنت هست برای Warp pro و Wireguard داخل…</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/whitedns/1489" target="_blank">📅 21:02 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-1488">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CCxi4Wl2Pv2S2fifuBTwLjacG_zBKAszCnq2iIrJys07eTP9cGf4Py4DRJA-8-isuL9JREWgsx5bRr4NC_yu_G07Vi_xnTJjR_7q2BYwtRoF1ssfPVW_lGS2i0ku3q7IHv49cmZpfmQ51EzNblfS6UtDzsfTXNDSTrEdCuRLUk2UWgEA2pulDOOO1rC7pSe1bs2mSi78ha5WE3_6YhvCAvqGVNQOR735V8G-ZXQ4cPmFMkAi--1_ZOqd9h4wRf359wYMgwq3Mk259JT3e3tEr2Q1myslwtP27SmaV4rAw1lCmuGnuvw9KmhcZFb0SKs8q1XCtctlvj38R5I2f6jpeQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💬
چطوری فیلتر شدن BPB و Workers رو دور بزنید؟
میتونید با رفتن به منو تنطیمات، فعال کردن گزینه Amnezia Noise فیلترینگ ورکر رو دور بزنید و به کانفیگ های ساب BPB Warp Pro و باقی Wireguard ها وصل بشید.
این مشابه گزینه فرگمنت هست برای Warp pro و Wireguard داخل اپ WhiteVPN
لینک ساب Mihomo رو داخل WhiteVPN وارد کنید.</div>
<div class="tg-footer">👁️ 49K · <a href="https://t.me/whitedns/1488" target="_blank">📅 20:42 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-1487">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1dc224c1a1.mp4?token=YAqcFBl4LZYpgoFKZgLgBj7pIUYiYSxOV9PyrKQXN73hbwEADwY756DWuaCY4UMDmOGPZ7kVTY_gE5Oz6M0gB-ywEWw-DVPeAkyKkAYBfHigV2zuei2ekka18Xo9qhmj1v4Cbb02fK9fK1-kNT_p5Ja7xgbjK6ohy-ZEFQRb77HdTlF6s07LHt9kqJcX3lEns5vXXiduG07pgF5-_JQmp0b3Bd6ajgX3amD1qriRPgT8tGvNySOxnGfX5TLH-i-_1LN_-hhxzN-E2uGzcQm_PDhm66fS0k_geGj6_QGlb0Hf37wmvmYkFYK6T4a8vx50_O6aSGtbgeddOfch2SdbSQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1dc224c1a1.mp4?token=YAqcFBl4LZYpgoFKZgLgBj7pIUYiYSxOV9PyrKQXN73hbwEADwY756DWuaCY4UMDmOGPZ7kVTY_gE5Oz6M0gB-ywEWw-DVPeAkyKkAYBfHigV2zuei2ekka18Xo9qhmj1v4Cbb02fK9fK1-kNT_p5Ja7xgbjK6ohy-ZEFQRb77HdTlF6s07LHt9kqJcX3lEns5vXXiduG07pgF5-_JQmp0b3Bd6ajgX3amD1qriRPgT8tGvNySOxnGfX5TLH-i-_1LN_-hhxzN-E2uGzcQm_PDhm66fS0k_geGj6_QGlb0Hf37wmvmYkFYK6T4a8vx50_O6aSGtbgeddOfch2SdbSQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">💬
دوستانی که فقط با فشار دادن دکمه کانکت براتون وصل نمیشه یا سرعت کمی دارید، از این روش میتونید تست سرعت بگیرید و بهترین کانفیگ بسته به اینترنت خودتون وصل بشید.
توجه کنید، هر تست سرعت ۱مگابایت از حجم شما استفاده خواهد کرد.</div>
<div class="tg-footer">👁️ 47.1K · <a href="https://t.me/whitedns/1487" target="_blank">📅 19:44 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-1486">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">🌎
انتشار نسخه WhiteVPN 1.4.0</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/whitedns/1486" target="_blank">📅 19:36 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-1481">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">WhiteVPN-V1.4.0-arm64-v8a.apk</div>
  <div class="tg-doc-extra">35.7 MB</div>
</div>
<a href="https://t.me/whitedns/1481" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-footer">👁️ 51.3K · <a href="https://t.me/whitedns/1481" target="_blank">📅 19:35 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-1480">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Je9Wy0ekqAxuFhzoJ9yVtyzgSvoP9qWA2YJTgwZEGQfQnHQb854MsDaHvFiMvk8fmEV5R9qDmZ3RB4lHomOU1nq9KBdKQ-G_aUs1fXU7xf5tMKTQxerQQn-dJUbsExIEA7IqVhNVLDWfKy3v__tmcymNsf4M3WiBBRaObRZQwOEcYWkllxG8fybFycaC45N7ezUKxR50VmYDAqqmVil5upSLOMx1K9q7vS4YedbxaaAWs4_VwDB33lJRK8xcb8BToCeG9O27BVWucY9egJS2gp0wl-ids7QI4A76CWhWIWorKP9-8-4ORrdz-tF-9KVPLz-RB5JMFu3RpA0Rb6ZyTQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🌎
انتشار نسخه WhiteVPN 1.4.0
• ظاهر جدید و مدرن اپ
• بهبود اتصال بعد از قطع شدن
• حل مشکل VPN Mode & Proxy Mode
• بهبود تست اتصال. حالا میتونید کشور رو فیلتر کنید و بعد تست کنید. تست هم به دو مرحه real delay و تست سرعت  تقسیم شده.
🌎
دانلود آخرین نسخه از گیتهاب
https://github.com/WhiteDNS/WhiteVPN/releases/latest</div>
<div class="tg-footer">👁️ 48.1K · <a href="https://t.me/whitedns/1480" target="_blank">📅 19:34 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-1478">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/ZZQS1Y1WAyWjW7_Ey20-xVavV_0c0kbBBatK3wxtoqXit4Ps4lQ5DIBvq0sJcrZcBehodiRPk8J2BlOG6SCHigU_Ft48yLmvvoCJ68xoa54e7MreJ5Hnx8iq7vNHuYgQADA5ZWmQ7kpegkry5RLSfWz5ZSbaa29lNYAsBKR0ILSbklB5eoJEDq2ePD94VkNaVgadYrpZgWwvTssz2Gg6tw_QT6UK6mUPPWJnMohx4BMzD1DSogRUtLXXXDtRjwazZ68GISno-Oz8qF11Tyb6F4mG9lTEtP99gXsbw4CsjE1kO1aZnJAX0x0qDhPGHUs-6WQwXeaVvII85dCI0ogQsw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🌐
وایت‌استر  —
نسخه‌ی دسکتاپ بتا
WhiteAesther Desktop V1.3.1
یه کلاینت رایگان و متن‌باز برای عبور از فیلترینگ، ساخته‌شده روی هسته‌ی Aether (همون هسته‌ای که تو اپ اندرویدش هم استفاده می‌شه). برای ویندوز، مک و لینوکس؛ کاملاً رایگان و بدون نیاز به کانفیگ دستی.
✨
امکانات:
🔎
جست‌وجوی خودکار مسیر — به‌جای اینکه شما دنبال کانفیگ سالم بگردید، خود برنامه بهترین دروازه رو پیدا می‌کنه (با MASQUE H2/H3، WireGuard و WARP-in-WARP)
📊
نمودار سرعت و تأخیر زنده — تست سرعت واقعی داخل خود برنامه + نمودار پینگ لحظه‌ای
🖥
دو حالت اتصال — «فقط این برنامه» (پراکسی محلی) یا «کل سیستم» (همه‌ی اپ‌ها از تونل رد بشن)
🛡
کلید قطع اضطراری — اگه تونل قطع بشه، ترافیک رمزنشده لو نمی‌ره
🔍
جست‌وجوی تنظیمات با Ctrl+K — هر تنظیمی رو در چند ثانیه پیدا کنید
🧩
چندپلتفرمه — ویندوز، مک (اینتل و اپل‌سیلیکون) و لینوکس، هم x86_64 هم arm64
📖
متن‌باز، برای همیشه — کد کامل زیر مجوز AGPL-3.0 روی گیت‌هاب
⚙️
نحوه‌ی استفاده:
1️⃣
از لینک زیر، نسخه‌ی مخصوص سیستم‌عاملتون رو دانلود کنید
2️⃣
نصب کنید و برنامه رو باز کنید
3️⃣
دکمه‌ی Connect رو بزنید و چند لحظه صبر کنید تا مسیر سالم پیدا بشه
4️⃣
اگه خواستید کل سیستم از تونل رد بشه، پایین صفحه گزینه‌ی «Whole machine» رو بزنید
5️⃣
برای تنظیمات پیشرفته (پروتکل، DNS، حالت جست‌وجو…) روی Advanced بزنید یا Ctrl+K رو بزنید و اسم تنظیم موردنظرتون رو تایپ کنید
📥
دانلود:
github.com/WhiteDNS/WhiteAesther/releases/latest
💬
نکته: چون برنامه امضای اپل/مایکروسافت نداره، ممکنه هنگام باز کردن هشدار «ناشر ناشناس» ببینید؛ کافیه روی فایل راست‌کلیک کنید و Open رو بزنید (تو مک هم از System Settings اجازه‌ی اجرا بدید).
#وایتاستر
#ضدفیلتر
#متنباز
نکته مهم :
⚠️
⚠️
⚠️
⚠️
⚠️
⚠️
⚠️
⚠️
⚠️
گزینه whole machine همان system proxy هست - این گزینه فقط اپلیکیشن هایی مثل گوگل کروم که امکان ان را دارند پراکسی میکند - برای همین ممکن هست بعضی از اپ های شما پراکسی نشود
تلاش خواهیم کرد در روزهای اینده امکان TUN را اضافه کنیم
@whitedns</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/whitedns/1478" target="_blank">📅 18:31 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-1477">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">دوستان عزیز سلام
مثل اینکه آدرس های ورکر کلادفلر فیلتر شدن. و آدرس ساب اپلیکیشن ما داخل ورکر ها هستش. تا آپدیت بعدی، میتونید ساب مارو از لینک زیر وارد اپ WhiteVPN بکنید
https://raw.githubusercontent.com/iampedii/whitedns-sub/refs/heads/main/mihomo.yaml</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/whitedns/1477" target="_blank">📅 16:52 · 24 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>

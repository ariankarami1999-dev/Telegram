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
<img src="https://cdn4.telesco.pe/file/fOCRKWYsUfP9jhYCw6nx3FyMikGFe7UGkly7JjJ1DNkjzNfCmkF3pfahQKw0USrxLebIufd_cNILv9Gdo21DNipAv-tg5HeEZFz1QH1x8njNgsTCY9WwdoC08XY7ejX1xKGU2oz1VVKaa7XaAqAjhiNRb5gZPq7Jec0c13L439srqoj7YRebCC0V33s6RGMxu3LSPwDLXQTvipdedgQssh-ow-D6X7CcC5mFBi3SsSEs6CeViG8qiyhLLPaGm9m6rnyEHB8lQcX0V_U5qTQqpX-8u-711mVo751gym8Kd6CHP6V9QLnt4dDPbIh8OAwLsr3MDsGpvrxDUZxGw5Y0Hg.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 فوتبال 180</h1>
<p>@Futball180TV • 👥 131K عضو</p>
<a href="https://t.me/Futball180TV" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 In the name of God; The only popular sports channel on Telegram: All for Iran...🖤We respect the copyright laws and follow the laws, Mr.@Durov...🙏🌹Contact ads:@TivaAds</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-02-31 03:15:52</div>
<hr>

<div class="tg-post" id="msg-90114">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">تو چنل بتمون هرشب داریم به سایتا تجاوز میکنیم
😄
ما هیچ فروش فرمی نداریم و نخواهیم داشت و کاملا رایگان فعالیت میکنیم که کنار هم به سود برسیم
🤑
🤑
🤑
@FutballFuckBet @FutballFuckBet @FutballFuckBet @FutballFuckBet</div>
<div class="tg-footer">👁️ 1.06K · <a href="https://t.me/Futball180TV/90114" target="_blank">📅 00:59 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-90113">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/cTC-gIQ-IjxRbGOvmiLBxpIUlDOijI_rkt0-3M_bfJd6yPnZvGrhJ-ctIzzYangQM4gwL_j7XpIQv6lBWR7zEbSOpIeuyGyO0oVDp6EdUJ5EiOwQd4CWKmT9-5IceI-DCEB6kVIUBPYSfrUsbIjpUVUTirlEJfCQWO_14Dl9u_ssS-r7nVLhMAnQT3iKm7QHnU38cOrdQU6b49VDhklcyPg2yEtkONsUC0JL3GeKpZSHa5SLjMsD8S4WEENVaEJNzbQGqoiBEUFco3c1TX91IKRSMqHPD2igP4guUMkfSvqL3VRM3i_N1cR-dvX_Pa_-3HHfuDwjApKrong2TdIpxQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تو چنل بتمون هرشب داریم به سایتا تجاوز میکنیم
😄
ما هیچ فروش فرمی نداریم و نخواهیم داشت و کاملا رایگان فعالیت میکنیم که کنار هم به سود برسیم
🤑
🤑
🤑
@FutballFuckBet
@FutballFuckBet
@FutballFuckBet
@FutballFuckBet</div>
<div class="tg-footer">👁️ 1.07K · <a href="https://t.me/Futball180TV/90113" target="_blank">📅 00:59 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-90112">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NwhSzVL6FhaYUDoMRW7KNxtK0RwFUwyH63zu_1UDERuAg5UXjYiCYyliwFuHah13GjzOvcKIRY4kfrncJ2XBoJpvUH_eYZrVlWKw1tvqXDKSAE-jb7CBhNgH4NlkvjGVsCNAhO1cAYrWg0vMzEFJUNtZxrvyTPRa8ckPgV7_wtyF42yAk5OHCNgE851i-ZKqH8G40-QiMR66BqQCO15QB4KC4JsMk5L8777tCcnHZ4EatcVt5XynPI3iNPxZv9TLioJwNQhBGAADKx4ky5qYTVp_LfqcuvSf5kQD69eo5tfQc8F6u4HkA1zdswl2ccxYwjEKs55PWX6060npEVwMDA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🚨
🇪🇺
🏴󠁧󠁢󠁥󠁮󠁧󠁿
استون‌ویلا با برتری قاطع مقابل فرایبورگ قهرمانی لیگ‌اروپا شد
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 1.36K · <a href="https://t.me/Futball180TV/90112" target="_blank">📅 00:48 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-90111">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">🚨
👤
برخلاف اخبار منتشر شده، سردار آزمون بزودی قراردادش با شباب الاهلی تمدید می‌شود و‌ این بازیکن قصدی برای حضور در ایران ندارد
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 2.35K · <a href="https://t.me/Futball180TV/90111" target="_blank">📅 00:13 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-90110">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">🚨
🚨
ترامپ: منتظر پاسخ مناسبی از ایران هستیم تا از تشدید بیشتر جلوگیری کنیم.
چند روزی منتظر پاسخ ایران خواهیم ماند.
تا زمانی که به توافق نرسیم، هیچ تحریمی را از ایران برنمی‌دارم.
در ایران افراد باهوش و بااستعدادی وجود دارند و امیدواریم معامله‌ای خوب برای هر دو طرف انجام دهند.
اگر پاسخ‌های ۱۰۰٪ صحیح از ایران دریافت کنیم، زمان، تلاش و جان‌های زیادی را صرفه‌جویی خواهیم کرد.
امور ممکن است خیلی سریع پیش برود یا چند روز طول بکشد، اما ممکن است خیلی سریع هم به پایان برسد
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 3.67K · <a href="https://t.me/Futball180TV/90110" target="_blank">📅 22:21 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-90109">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LFJnkdaBbh926OJXj6rnGitaBWojLpOZf9EUIFU4_vrBpzX4KfDAqbz8tozWqTlN4lI9hJdQtUHKlzYn6_gu6rKrL996G3cVfYyXNFDMEDpUtt4rOHI8UrJdRAR1gmRUKOVdFxXy7DxW80XSlq3rVkiihSGBD-_s-Rd4Ny-bXonapPV-42rh3GFuMQT8CqGa9H55SBBZvfWTk9UE1QE52iRCuqKxJJtIXmBbVF4JF4Z7vWdQIi-Cnyab8izJoW2fKKQvgg-nC4nTqwJDBSnA6qZ8O_M9WQvt9bgml-lcSuSvFQqrRnyjoufQKjXozYI0m32cEx8hhDMBc2mZq2dalA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سردار آزمون: ایران هویت، قلب و افتخار من است
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 3.54K · <a href="https://t.me/Futball180TV/90109" target="_blank">📅 22:20 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-90108">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">🚨
🔵
مجوز حرفه‌ای باشگاه استقلال برای حضور در لیگ‌نخبگان آسیا صادر شد
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.3K · <a href="https://t.me/Futball180TV/90108" target="_blank">📅 19:43 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-90107">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VBaAhb8jEDcLPUDN-av_4vAemq8Bi1JCRs-IGjiyiJ2wexNaVFN8mnK0zBUG6Myb5FLBRyey1KH6LR1Xx1B22-bFVlQAlfrCmVwZMmHw1S7_vzeqTTGcKtZJJ7YmgVuQIw0BV6rRVY5QGo5tIQgFfGzBLDEttr4zh3Tz4Imzt0vVe6sVmS95QmsKaWkBHjW8LwDDvXfKzBSn4F2aSHI8AkEijWucOKLPDUrd9C76pjiHwgF_X2FUhe8oDCziAq_lty6wGYGKwW48WFTxzVr848zE6aQP2ryD4faJmajsEZZNCKUN_F58wOkxyT9zLwAr_SMx0ARXjJ0RmKQHYAFkUQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پست جدید کریستیانو کریستیانو؛
همان شور و افتخار همیشگی؛ بیایید همه چیز را برای پرتغال ارائه دهیم
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.35K · <a href="https://t.me/Futball180TV/90107" target="_blank">📅 19:18 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-90106">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">1xbet_ir.apk</div>
  <div class="tg-doc-extra">51.9 MB</div>
</div>
<a href="https://t.me/Futball180TV/90106" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🔥
ورژن جدید اپلیکیشن وان ایکس بت بدون نیاز به فیلترشکن برای گوشی های آندروید
🎁
اپلیکیشن رو دانلود کردید موقع ثبت‌نام، کد هدیه 1x_1566529 رو وارد کن و تا
100یورو
هدیه بگیر!</div>
<div class="tg-footer">👁️ 4.05K · <a href="https://t.me/Futball180TV/90106" target="_blank">📅 19:18 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-90105">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Mn99hGe70xPzH_M-yctB_AqIGwCSzIqajhiZsS3R7wday6pleUdfTX7IHqCkZzHh7BjJ-j6Lux-bCVeP0EZuwdqKRtG2-7cFFLgJrlsu_gLeT1aeH5RxJirONMAMlmnfWFRt-zt4-ubTjJAgJMbkefssU3BY8CF7PYPn4N4cjZY9H3wgoTWnKo-W5JONE_Dv2gmK38Usy1w_JPBvCwKZLrLvvQEgzeUF1lGnbQtR2r5cY3KwFwhinLiKMq9aO8Irs_YnbZY25Vg2fvESg310USTdmWxLn4Y6FGv0FCwVFcQViTpHH8R85csaZT-FKjkg4BM5z1cKtnyIgKOQDCZwTQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🤑
پروموی Crypto Freebet
🤑
💠
حداقل 5$ با ارز دیجیتال واریز کن (حداقل 5 بار در هفته، در 3 روز متفاوت)
💠
هر دوشنبه
💎
یه پروموکد می‌گیری برای 30% بازگشت وجه از میانگین واریزت
💠
سقف بازگشت:
💸
تا 300$ در هفته!
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
<div class="tg-footer">👁️ 3.85K · <a href="https://t.me/Futball180TV/90105" target="_blank">📅 19:18 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-90104">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7ca121cc7d.mp4?token=ozcrwKpzhmaz1gqOn7qUcVXYTIb-G0q3HDlvDaFKBizIbAmDuhMHQ9z50E2_imVwdn0exkRY90_rv4O8q4GEHRaw208akAmpkEjsKfM5W8aM3QVa2lynRX09DvbqCtorX2t-teUZKs_j8G_6JledTGpMu_VNzXv5xE6LwDkqqRJaCNXVANTnErn46nWg245-kn5sgxZE6RAZQ4h3JadjCQn28HiNlGxpnf14Yw0R-g7nh9PMgr7TLIfjT5H6cFnFJZqEl6EgAZ5w45KsF5ezNxawMguM2iYfVvz3r5M8kWg6nAsYKY2nSIku5rrZPZFvmDAlFaGqGai6reFRcUVwfw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7ca121cc7d.mp4?token=ozcrwKpzhmaz1gqOn7qUcVXYTIb-G0q3HDlvDaFKBizIbAmDuhMHQ9z50E2_imVwdn0exkRY90_rv4O8q4GEHRaw208akAmpkEjsKfM5W8aM3QVa2lynRX09DvbqCtorX2t-teUZKs_j8G_6JledTGpMu_VNzXv5xE6LwDkqqRJaCNXVANTnErn46nWg245-kn5sgxZE6RAZQ4h3JadjCQn28HiNlGxpnf14Yw0R-g7nh9PMgr7TLIfjT5H6cFnFJZqEl6EgAZ5w45KsF5ezNxawMguM2iYfVvz3r5M8kWg6nAsYKY2nSIku5rrZPZFvmDAlFaGqGai6reFRcUVwfw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">😂
ترامپ : الان تو اسرائیل ۹۹٪ طرفدار دارم. می‌تونم برای نخست‌وزیری کاندید شم، شاید بعد این ماجرا برم اسرائیل واسه نخست‌وزیری
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 3.88K · <a href="https://t.me/Futball180TV/90104" target="_blank">📅 17:19 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-90103">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6dc000d4d3.mp4?token=n4szDc61vm4bWqn6Z7kRfuRy-nM5bATR4V7bonHLNRfOar4JNxTXP4x4jdeAFY47dO-kv0cbyz-RRfgQu4sArYW0_9D0GphfQTVfp0pIwJAPmUzBlcYcuXh9IOxxPtXBxUSTLJRyg7Nd7wDNj5p4Bn4Bu5NWcf5g-0xZ20SkMVBwRxCIzKMHuo7SYhyUDNqkFGrtq7gl09uTXSGY8xq_6vip7kVkGFhz2Q1Wabe-oHVhJFG8nzBVoHumLSrq49CRrQgAx1anXTSM0BfE2rVWdfrhFq4UlpEzljqVXxm6xRSjH0RE-2Hotv2Ojksa3g1axBmqyPfqIO9qJVMacDRcuw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6dc000d4d3.mp4?token=n4szDc61vm4bWqn6Z7kRfuRy-nM5bATR4V7bonHLNRfOar4JNxTXP4x4jdeAFY47dO-kv0cbyz-RRfgQu4sArYW0_9D0GphfQTVfp0pIwJAPmUzBlcYcuXh9IOxxPtXBxUSTLJRyg7Nd7wDNj5p4Bn4Bu5NWcf5g-0xZ20SkMVBwRxCIzKMHuo7SYhyUDNqkFGrtq7gl09uTXSGY8xq_6vip7kVkGFhz2Q1Wabe-oHVhJFG8nzBVoHumLSrq49CRrQgAx1anXTSM0BfE2rVWdfrhFq4UlpEzljqVXxm6xRSjH0RE-2Hotv2Ojksa3g1axBmqyPfqIO9qJVMacDRcuw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
جدایی رسمی برناردو سیلوا از منچسترسیتی
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 3.88K · <a href="https://t.me/Futball180TV/90103" target="_blank">📅 17:15 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-90102">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/252c545abf.mp4?token=kcng7yw_F4Gb1hRXiGbAsbeR2-KLlD_3xFuvbyJTpSackoez1dD7pV6EdVvNjmVVZaJaLSPFuo5rzSbNjslmlNE5HDhn7oFZC4M1i7IuYAwhHlj1PvIZWHqDkUux8QbKR3gLf02HEWkYaFeBzH_YP6WPrHC6xEjFtGamzyFfRDxznaqdmsc0UILIdyEaWKcz0olrgQM8NwEsCYuprxXKxoaWhfnKQO4aZ6XMuCYmbE1ioy6_96y7V4jjr-Wlkz-sDDQB9Xg1O7GtV60RW9218WmNG7Qq9neItlOYSdyZqkXrU6wasQnHNt1lXM_hnKmtvi38hjcvntbC0pObMHI2-A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/252c545abf.mp4?token=kcng7yw_F4Gb1hRXiGbAsbeR2-KLlD_3xFuvbyJTpSackoez1dD7pV6EdVvNjmVVZaJaLSPFuo5rzSbNjslmlNE5HDhn7oFZC4M1i7IuYAwhHlj1PvIZWHqDkUux8QbKR3gLf02HEWkYaFeBzH_YP6WPrHC6xEjFtGamzyFfRDxznaqdmsc0UILIdyEaWKcz0olrgQM8NwEsCYuprxXKxoaWhfnKQO4aZ6XMuCYmbE1ioy6_96y7V4jjr-Wlkz-sDDQB9Xg1O7GtV60RW9218WmNG7Qq9neItlOYSdyZqkXrU6wasQnHNt1lXM_hnKmtvi38hjcvntbC0pObMHI2-A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">چنتا شبکه‌اجتماعی غیر معتبر روسی با این ویدیو مدعی زنده بودن علی خامنه‌ای شدند و گفتند که به این کشور پناهنده شده :)
❌
سطح اعتبار این ویدیو : 0
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.01K · <a href="https://t.me/Futball180TV/90102" target="_blank">📅 17:10 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-90101">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">🚨
⭕️
⭕️
🇪🇺
تمام باشگاه‌های لیگ‌برتر ایران بجز پرسپولیس و گل‌گهر سیرجان با ارسال نامه‌ای به مراجع مرتبط خواستار لغو ادامه مسابقات لیگ‌برتر و مشخص شدن تکلیف نهایی تیم قهرمان و سهمیه‌های احتمالی شدند
🔵
این تیم‌ها با عنوان کردن مشکلات مالی و ...، موافقت خود را با قهرمانی این‌فصل استقلال اعلام کردند
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.28K · <a href="https://t.me/Futball180TV/90101" target="_blank">📅 16:16 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-90099">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/D-sbYKsiqZSBqoJ52RZ3PdbnIYqecYoyQ8RqJ_XACc1Mc7hSOTlW88YCompuiNMgX0HsktlPBwK1c9lzxsrQ2GN8a3lC7gRvsadQOtT_f2ba5mmCVi5xafabZrEGnl6FW6cwW4CQYwcotk8ZzfdvZZX0lKNwyhwaAyhxn_6TiKvFe7HeXC9Ry0Crh7-yJxorG_6JkAe5uVQhxqCfd82vuYR8ESh0fjdv8voMxWoXXR5RbPX87VPx-79ATXFsYD6QUmPsKNQPFz93jJ3i2TZsto7lWv6uDTRffBaJXMl2mZ8GN_YQN-ahGycTC2LDrYnNIBjdaNn3Be_yKthV_oqJtQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qqnM4AXEl50TRxWXuuIPYKSE8rV2E4qNCNbDqVbj_0dz_Hv7OaAubWGY6CwhlwxDWnesW3TTm78hFufYDEAUm45dEsJLj6a0J3OF3NiOS7Ch2q5ta1q3snmWpW9bOCGRjVif-eLCAp4ddhRmHET6blq3Z2GokC6Frq8kycUWHsoWL4y1MVYXB7w3-Vf3GAH7tZpNzVHqHkm5lGsCOnAPiXpsv_4B7i3xGkqX8XgZ-9QI3W11QlrYRyz2-t7iiL8mzK3r5hGqi8nCtEPKOy-KYK2noKcKpup5PXJprE5UUeh-BN-xnmNxuqCdDKSmQdFXNzZ1MzrwAVAHN_xlheX64g.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">اینس گارسیا بلاگر ۲۱ ساله اسپانیایی و دوست دختر جدید لامین
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.53K · <a href="https://t.me/Futball180TV/90099" target="_blank">📅 14:27 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-90098">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">🚨
⭕️
رشید مظاهری سنگربان شریف سابق فوتبال ایران در حین خروج از کشور در فرودگاه بازداشت شد!
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.51K · <a href="https://t.me/Futball180TV/90098" target="_blank">📅 14:00 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-90097">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6ece86e352.mp4?token=UsMqrwHoYbCgL1DEWBFGEqZlKpXXQ2D0ny07Q_uVqmRqbL9ABS7QRXyrhWdJzmEpAbrYHPcDKBhRisKT45JGXK1zbpAjQPfuw-t05f5YhBjQm_OTvh0xpjOa3-ByGDOmA7Qg_fXq9rWmwfb59Uh-WIEzNoG5ygHkYNV_35aHcCn3xcnscfbXKGLhef1kezTx_vksqpFbCiGzmZ6QmnOUdJ4a3BtJ6uiBK4TBfW_DyYQzqqPcsb21_hPPTykEOBM1svKyROOgd59W42Iu4EsQXuTcQvArLvkLqIolMVWpzTZDeS3MB8r8PM-Xmceprg7I1pV9InumW_dxuygzLRA4bw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6ece86e352.mp4?token=UsMqrwHoYbCgL1DEWBFGEqZlKpXXQ2D0ny07Q_uVqmRqbL9ABS7QRXyrhWdJzmEpAbrYHPcDKBhRisKT45JGXK1zbpAjQPfuw-t05f5YhBjQm_OTvh0xpjOa3-ByGDOmA7Qg_fXq9rWmwfb59Uh-WIEzNoG5ygHkYNV_35aHcCn3xcnscfbXKGLhef1kezTx_vksqpFbCiGzmZ6QmnOUdJ4a3BtJ6uiBK4TBfW_DyYQzqqPcsb21_hPPTykEOBM1svKyROOgd59W42Iu4EsQXuTcQvArLvkLqIolMVWpzTZDeS3MB8r8PM-Xmceprg7I1pV9InumW_dxuygzLRA4bw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
شادی گابریل مدافع آرسنال با خانواده‌ش
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.51K · <a href="https://t.me/Futball180TV/90097" target="_blank">📅 13:58 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-90096">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">1xbet_ir.apk</div>
  <div class="tg-doc-extra">51.9 MB</div>
</div>
<a href="https://t.me/Futball180TV/90096" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🔥
ورژن جدید اپلیکیشن وان ایکس بت بدون نیاز به فیلترشکن برای گوشی های آندروید
🎁
اپلیکیشن رو دانلود کردید موقع ثبت‌نام، کد هدیه 1x_1566529 رو وارد کن و تا
100یورو
هدیه بگیر!</div>
<div class="tg-footer">👁️ 4.12K · <a href="https://t.me/Futball180TV/90096" target="_blank">📅 13:58 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-90095">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pNQYExDck-hWQN4ovxv3o_2cwInu7PIyOLJv2eAP_rnjE_eGPss-5ri76GSxvNCYyi1iau9KRYopQrDMo5tme8oz073LkYcUl_KrjHABx58b3TnAsTL10BlNTkrGwsc0lv7fZ3kldtPOusOOEwg7u8NXctq5Ejtb_-pqGiFG18ErrJcz24VswNKXgVHl96MHCBM3bn4_8908vB1foUnTq2vLL73lU8my_kg14YIF_vjUgWDN2Joo7JR0W4-QB0jORaBkJVafiha0a2QZ37OxkwGLekOhSb7CCJrujaiIzQttvkrgms6wZVEPzeL2r14DswKv9ur5pMpVL35miIz9Gw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
Ole, La Liga:
بر روی رویدادهای مسابقات فوتبال لالیگا پیش بینی کنید
!
💰
در ابتدای هر هفته، یک پیش بینی رایگان دریافت می‌کنید.
✅
هرچه شرط‌ها بیشتر، پاداش بزرگ‌تر!
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
<div class="tg-footer">👁️ 4.27K · <a href="https://t.me/Futball180TV/90095" target="_blank">📅 13:58 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-90094">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gulqV-Zp9Ww5kbJqIkfT1xVb0q9Cqo70pUQ4z4hTl5u5QfV1Z4PpeP8KXxHn9ZTk0rCnscnxGP3gWkSHAM-LS9nplJ14xHkWiG53x5MC7uv9TfT-UVoTo3kdPGNK2X0fx_VyZXuMasC0rhVElRt9Gu2eG7PVFzf0dJGS7G5bSZ1Wmdl3vQ5wVCMmoML0mR0K-1STmdWJxqhUsugiTixF82SozTnhTf8Kw0PPf0m3EFtAiSzccL1LP2NOoGFEaOkbbvzK96UABvAZUHkGPMU-dgaQcttXkgaQiuDEWLA8N99pSATdzm8xUqNX_xTIxbSekP3Tb4CjBw-AYmcVQ6tT7A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
توییت تاجرنیا در واکنش به شائبه‌ دخالت غیر فوتبالی در تعیین تیم‌های آسیایی: ‌عدالت یعنی سطح دسترسی به قدرت سیاسی، تعیین‌کننده نباشد
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.17K · <a href="https://t.me/Futball180TV/90094" target="_blank">📅 12:07 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-90093">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e56d546629.mp4?token=TW8JHkIFYsA6Mn6RZNOxErRK8DsTL-ZlSWRQtTcPMyiSnU2o18AgIzS2fDjHSj27eWF0FEyfg095P6kM7fn0GxA94i_xuElTtxk4bUNA6gIca_DSJMEzf0LqJ40SzCoU2NfzysG6YQgA8Za5rHA7b2y5BnB7TdjtAiIUqKtCgjDPIhgjkY59D3UgiCIVI_gTbfAGS_vFB7ccV6EAQjj7q8e8bViYiBGhrDbY6beCQyXlLTLgi9pz_IrVfeOQzPIB19lNLbUL33_HMwJmlv-mwt2lVUcDBp9Vkrmii0rJpxRDuexWlp5GUDyHXBvT7aJX_DwOW8xoj7JZ5nzPqbIdlQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e56d546629.mp4?token=TW8JHkIFYsA6Mn6RZNOxErRK8DsTL-ZlSWRQtTcPMyiSnU2o18AgIzS2fDjHSj27eWF0FEyfg095P6kM7fn0GxA94i_xuElTtxk4bUNA6gIca_DSJMEzf0LqJ40SzCoU2NfzysG6YQgA8Za5rHA7b2y5BnB7TdjtAiIUqKtCgjDPIhgjkY59D3UgiCIVI_gTbfAGS_vFB7ccV6EAQjj7q8e8bViYiBGhrDbY6beCQyXlLTLgi9pz_IrVfeOQzPIB19lNLbUL33_HMwJmlv-mwt2lVUcDBp9Vkrmii0rJpxRDuexWlp5GUDyHXBvT7aJX_DwOW8xoj7JZ5nzPqbIdlQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
صداوسیما: هر کی جنگ نمی‌خواد، جمع کنه بره‌‌‌‌...
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.31K · <a href="https://t.me/Futball180TV/90093" target="_blank">📅 11:31 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-90092">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">🚨
🟢
باشگاه آلومینیوم اراک بدلیل مشکلات مالی در آستانه ورشکستگی و انحلال قرار دارد
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.12K · <a href="https://t.me/Futball180TV/90092" target="_blank">📅 11:00 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-90091">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7e96fba692.mp4?token=L2wokmcRqlbBzrDG_HJgFYbrJ3M10Xc8HdNIN2OQmVDoT0HwNr1wtyJZcuzoiQ0Mzv2w6_CjNRKR_VivmUNldI6JiuboSJKkvpB-MLH0tn-lBDx07P29Xq7Vv7veBeQqWBRY8Icx1f33hLoB04kcU9b7SMJKxCuNgS4FU_d0HZZOAYFIOCuSEkMZYWG8DQBuvHOKV6E06c0RNBxUbKbO1bpV-fGYs3CWS-z7xMCMP_SwCPAKEfzF0MO8OanrU4CAxe4rAeyeY3ze0abhJFSCUMASiaZTyhEdCq1r3VrCeAzjjvPDtIoYdRZmgO6HbRUR_hnEn9VpUTokCY44haCYD4i-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7e96fba692.mp4?token=L2wokmcRqlbBzrDG_HJgFYbrJ3M10Xc8HdNIN2OQmVDoT0HwNr1wtyJZcuzoiQ0Mzv2w6_CjNRKR_VivmUNldI6JiuboSJKkvpB-MLH0tn-lBDx07P29Xq7Vv7veBeQqWBRY8Icx1f33hLoB04kcU9b7SMJKxCuNgS4FU_d0HZZOAYFIOCuSEkMZYWG8DQBuvHOKV6E06c0RNBxUbKbO1bpV-fGYs3CWS-z7xMCMP_SwCPAKEfzF0MO8OanrU4CAxe4rAeyeY3ze0abhJFSCUMASiaZTyhEdCq1r3VrCeAzjjvPDtIoYdRZmgO6HbRUR_hnEn9VpUTokCY44haCYD4i-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
❌
واکنش تند مامک جمشیدی، خواهر پژمان جمشیدی به خبر منتشر شده درباره صدور حکم پرونده برادرش
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.31K · <a href="https://t.me/Futball180TV/90091" target="_blank">📅 10:50 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-90090">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">🔥
خیابان‌های لندن در تسخیر هواداران آرسنال
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.22K · <a href="https://t.me/Futball180TV/90090" target="_blank">📅 10:34 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-90089">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GOe3xo_JCca-p02d2ir1ttBnT51L_DF_XEAh_eQc46OGzpFDKkeHpoGnzYw18TYsZxkOJWich_Z-XY6fxufBsYzxVPBKTsk5pyu-QHO0fICz5OwUQjvFTX-DsMe7M7pIq4u9bClD7eMrq0tfek9ll-nlvbi0Hyjrj2ZmyIzg1NL_bTK7lD4OpGPSTCECTeyhWVVPky5dCgPMlCgfM4zeGqcgckIBkpaM0kl-Meclp2j-MJFmzPEk4i5OQl7GkzFA2rFevCg23rDW9E0hcNa9xzDkaNbfKnpJPFn9ITl2juds1M4Yp4lazXxiWiUa5d8n2JIBf6HexmBdaO18Z2C4gw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
عملکرد مسی، نیمار و رونالدو در ادوار جام‌جهانی
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.24K · <a href="https://t.me/Futball180TV/90089" target="_blank">📅 09:34 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-90088">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a4f7578a72.mp4?token=tfnOJ1VopKrapfjKbueciPvUmuAOWD8hRai-ILE_Ulud6ZEgmGvldR8Xr3N-pkdtHtzW_rYsyXnHvHDFlj-cw8pz_run6KVgeSmboldrHHq6fTS8EKNk90AAXipP2uFSBR_RHJ-UfRe-ulSWGRrvpWdmjqwv95mVfSGypgLg0F9Fdp-LWuK4lqZczDpg9_hpLtv1h_NjmYSIB69nKOJsMLE9ciS34Gmy1c5X1YDQ5etEVaDLBp4Wk9amdNptTga1oB4HJQYekeaeYSVU-NG8q_McOYfzrW46bVnvHgJXFrt--eX_RFEjeMofrBa-M09_KkVV2OH0HN4X7JlOJVBoTg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a4f7578a72.mp4?token=tfnOJ1VopKrapfjKbueciPvUmuAOWD8hRai-ILE_Ulud6ZEgmGvldR8Xr3N-pkdtHtzW_rYsyXnHvHDFlj-cw8pz_run6KVgeSmboldrHHq6fTS8EKNk90AAXipP2uFSBR_RHJ-UfRe-ulSWGRrvpWdmjqwv95mVfSGypgLg0F9Fdp-LWuK4lqZczDpg9_hpLtv1h_NjmYSIB69nKOJsMLE9ciS34Gmy1c5X1YDQ5etEVaDLBp4Wk9amdNptTga1oB4HJQYekeaeYSVU-NG8q_McOYfzrW46bVnvHgJXFrt--eX_RFEjeMofrBa-M09_KkVV2OH0HN4X7JlOJVBoTg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
🔥
🔥
🔥
رختکن آرسنال دیشب
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.1K · <a href="https://t.me/Futball180TV/90088" target="_blank">📅 08:42 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-90087">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">1xbet_ir.apk</div>
  <div class="tg-doc-extra">51.9 MB</div>
</div>
<a href="https://t.me/Futball180TV/90087" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🔥
ورژن جدید اپلیکیشن وان ایکس بت بدون نیاز به فیلترشکن برای گوشی های آندروید
🎁
اپلیکیشن رو دانلود کردید موقع ثبت‌نام، کد هدیه 1x_1566529 رو وارد کن و تا
100یورو
هدیه بگیر!</div>
<div class="tg-footer">👁️ 4.27K · <a href="https://t.me/Futball180TV/90087" target="_blank">📅 00:30 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-90086">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/t41ysNQ1emU-o-hrj10OhqYViyQpvdD8CC_3eviwXNKRrqIW6oaM5-n9czOdNKEEgBh6NKeWMRMhVyBZA-cZpq8kkaHmtGthyHpvVaVCq45EAOgyJ46al5KPWiNf_cy9v1is2r67O0YVdw4NsX4k_Y_-WTusX79naOTFNHkEaHeN9RQ5bTMQI6hFNDClDWmM4d_1vJXofCo09pm4VS9gUyNcUywL5zJfiO_GzUdlEHA4CDIAQRaEsUNf6R0KGxR_aogx13QxItYJz59WlnygbL0KJnluni9WwwPob6UWHYVqP6vyE6e87AZ0mPC5gwliwHE1ctE4tjGX4WNb5AgOhw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
فینال لیگ اروپا
⚪️
فرایبورگ - استون ویلا
⚫️
را در 1XBET پیش‌بینی کنید.
💥
بونوس صد درصدی 100% اولین واریز
💰
پیش بینی تکی برای بازی پیشنهادی قرار دهید و در صورت باختن پیش بینی بازپرداخت تا سقف ۱۰۰ دلار دریافت کرد!
⭐️
با پیش‌بینی بدون ریسک در هر حالتی برنده باشید .
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
<div class="tg-footer">👁️ 4.31K · <a href="https://t.me/Futball180TV/90086" target="_blank">📅 00:30 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-90085">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4b4882a411.mp4?token=daVYXGh1cfSkeRB-hBbx-Qfe35MHjQ2Eav6U6v6AXaWVvQnNrP5xTiwy_PKd2kSaWycB7jZDL1ahXmY5is1gQpaVa7w_OIIoA5ulxJrEd2yBN8UWgE6K0VvqMYeC3tEd-q6BgCvWOXzctsMR51hojQnRv8jXyBp4riGeSmxDvFT7woHnpF3vbI3m9GwXG2joDOdEEuJmkNkbCVheN3S205VUlJDcUkHnfXHEmUX4aeWZZLjuVwwyXDGuApwQ5YndbNTYd_ewAy9pfNMUDvDKeY-7jQA_wu7CGQhSCg4Jb5ZGwAsZaq7z2yJB3_2SL_vCUL4AqgJUG0A205JGM_2S_g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4b4882a411.mp4?token=daVYXGh1cfSkeRB-hBbx-Qfe35MHjQ2Eav6U6v6AXaWVvQnNrP5xTiwy_PKd2kSaWycB7jZDL1ahXmY5is1gQpaVa7w_OIIoA5ulxJrEd2yBN8UWgE6K0VvqMYeC3tEd-q6BgCvWOXzctsMR51hojQnRv8jXyBp4riGeSmxDvFT7woHnpF3vbI3m9GwXG2joDOdEEuJmkNkbCVheN3S205VUlJDcUkHnfXHEmUX4aeWZZLjuVwwyXDGuApwQ5YndbNTYd_ewAy9pfNMUDvDKeY-7jQA_wu7CGQhSCg4Jb5ZGwAsZaq7z2yJB3_2SL_vCUL4AqgJUG0A205JGM_2S_g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">کارجدید حمیدسحری با کپشن:
تاج‌گذاری میکل آرتتا در لیگ برتر.
🏆
🏴󠁧󠁢󠁥󠁮󠁧󠁿
آرسنال قهرمان لیگ برتر در فصل 2025/26 شد.
🥳
⚽️
Channel:
@Futball180TV</div>
<div class="tg-footer">👁️ 3.94K · <a href="https://t.me/Futball180TV/90085" target="_blank">📅 00:13 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-90084">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lezbHPqck4ug9kiFIX2FbKSx5M07PNm0LMeTAlnXFCuH8myJEjpX9h8iNOnVT8ooRCbPOj8erTPS5CFT2jxK5gpZxRboIF8VnXVoKHGRvcAXvqxi44In9MJZ6r6uBZSsvGgt-3zvUvvJOYtQpJ4jsvfF_QNAOWK50jdiGGilfG0TmDU8bVPyFQgmz4feaO4CpKTK8EN559NIluvr6I7BZvk7PhC1RC8s4B_EOgOTUF08MUJYkJKVHK8z88SjGISp7EAgOjd8m2T4xpigGlneS_R9T-2bqefclbske36Jwq-GaA0nbsy8VjvwAb7eM71uo-TXUFHm1ywCbAUUFXnXEQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
فرایبورگ - استون ویلا
🏆
فینال لیگ اروپا‌
🇪🇺
⏰
چهارشنبه ساعت ۲۲:۳۰
🏟
ورزشگاه بشیکتاش
🎲
با بیش از ۵۵۰ نوع آپشن پیش‌بینی
⚡️
با بالاترین ضرایب پیش‌بینی
📊
نگاهی به آمار دو تیم:
✅
فرایبورگ در
۸
دیدار اخیر خود در لیگ اروپا مساوی نکرده است.
✅
استون ویلا در
۱۳
دیدار اخیر خود در لیگ اروپا مساوی نکرده است.
📈
میانگین گل در
۱۰
دیدار اخیر فرایبورگ در لیگ اروپا
۲.۴
گل در هر بازی بوده است.
📈
میانگین گل در
۱۰
دیدار اخیر استون ویلا در لیگ اروپا
۲.۸
گل در هر بازی بوده است.
🧠
وقتی پیش‌بینی برای فرار از فکر است، نه برای فکر کردن، خطر شروع شده است.
🌐
ورود به سایت با فیلترشکن
کلیک کنید
BetForward.com
کلیک کنید
BetForward.com
💻
@BetForward</div>
<div class="tg-footer">👁️ 4.18K · <a href="https://t.me/Futball180TV/90084" target="_blank">📅 00:09 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-90083">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromAmoAdmin</strong></div>
<div class="tg-text">⚠️
مدت این آفر 3 روز هست
⚠️
💎
پلن حرفه ای
1 گیگ : 280,000 ت
5 گیگ : 1,150,000ت
10 گیگ : 2,050,000ت
20 گیگ : 3,900,000ت
40 گیگ : 6,900,000ت
💎
پلن اقتصادی
5 گیگ : 850,000ت
10 گیگ : 1,600,000ت
20 گیگ : 2,800,000ت
40 گیگ : 5,100,000ت
🟢
کد تخفیف به صورت خودکار روی ربات فعال هست و نیاز به وارد کردن چیزی نیست
✈️
آیدی ربات جهت خرید :
@AmoAdmins_bot</div>
<div class="tg-footer">👁️ 3.41K · <a href="https://t.me/Futball180TV/90083" target="_blank">📅 23:09 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-90082">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d7eae73a44.mp4?token=tHU6RMop6Yms3hhAwJnLf0mCYzfA6jv4iXQ8IYL8CdN4z_ggyY8h33FjE70HkUxbMLLkN1KtD10RqPd97MnlVUJgq84FszAw5IDkv3jtglerllSDUb2MHPAqEWTgVaMGvHHaA0UtkZGRe07YQHGHV5H7zifA4a6ezKpdpHVtHW7genGvcpv901TY9AUJ4BjXU5ZphPz2i20wriL00YvUZmTMh9gexJL9K_DNJGanLrUlgM1UW73PinXmmdfmHX3R5E_L7I-zJFt-xTn65chz0_h_TJRwUY5nvZqPA0QbSTjALZUsMJWAV1z08u1H04YycLiy99YC2pM-pMjUTXH2JQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d7eae73a44.mp4?token=tHU6RMop6Yms3hhAwJnLf0mCYzfA6jv4iXQ8IYL8CdN4z_ggyY8h33FjE70HkUxbMLLkN1KtD10RqPd97MnlVUJgq84FszAw5IDkv3jtglerllSDUb2MHPAqEWTgVaMGvHHaA0UtkZGRe07YQHGHV5H7zifA4a6ezKpdpHVtHW7genGvcpv901TY9AUJ4BjXU5ZphPz2i20wriL00YvUZmTMh9gexJL9K_DNJGanLrUlgM1UW73PinXmmdfmHX3R5E_L7I-zJFt-xTn65chz0_h_TJRwUY5nvZqPA0QbSTjALZUsMJWAV1z08u1H04YycLiy99YC2pM-pMjUTXH2JQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
💙
سهراب بختیاری زاده سرمربی استقلال: یک ذهنیت به وجود آمده است که پرسپولیس عادت کرده است که بعضی وقت‌ها با فساد بازی را ببرد یا به این عادت کرده است که همیشه دستش را  به نحوی بگیرند و کمکش کنند
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.66K · <a href="https://t.me/Futball180TV/90082" target="_blank">📅 20:07 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-90081">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SgCM2oCPjInhmp0Ki21_MNqOtNUkBdiPi2tBh8-vwLfxG6wi4KwmYQ03WMUyYSCwfoj-sn0B60xyd8q0KT9ROrOv_Ib5feKUMMOzmS9_09ZPrLhX3TuUYx1H1liua-78bxjPYGg58MszyMsLq9eJm81-y4kjt6M1ZOiVMn3Ppy1CdqAxh7tyzcxlGCTg84vDsPjLARcQF_q-P4kw03mXWFMvw95-WnR9oYrSs-tYDPDfkiAei-tZoSp66vwIwLyk2e0TFPuzEPuiO07PKz7KhvqsbBpptTYkD7zbabnZHlWCZBVHGJKzxlFbsfSmQsuIYV5FU5MBaCCCQj6irDs4PQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👀
⁉️
از این منظر نگا کنیم؟
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.74K · <a href="https://t.me/Futball180TV/90081" target="_blank">📅 19:29 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-90080">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">1xbet_ir.apk</div>
  <div class="tg-doc-extra">51.9 MB</div>
</div>
<a href="https://t.me/Futball180TV/90080" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🔥
ورژن جدید اپلیکیشن وان ایکس بت بدون نیاز به فیلترشکن برای گوشی های آندروید
🎁
اپلیکیشن رو دانلود کردید موقع ثبت‌نام، کد هدیه 1x_1566529 رو وارد کن و تا
100یورو
هدیه بگیر!</div>
<div class="tg-footer">👁️ 4.48K · <a href="https://t.me/Futball180TV/90080" target="_blank">📅 19:29 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-90079">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kotMfy8GdWbVAseG6c3BeqOGq-85Xo1H2PrjAc6P4Cj63Md-blzoTzAnfl3GSvUy4pByJ2OYNQuTEGZFGCfgqO1WOWnn3-jPlH8fXC8JxjwxCw_Dmj36kLmr-j7ugSwI-tzrbgGLiO9lMTGXsYcutH2z6q6uZoBxYPsCuVZUEyoFyNpICjb-tpAH6FoBEEjfHvgNpVjh2kM7IM4VEkRd4Pmt_3g6pCaB1UJzvVMOOJOstmvWIqemd9elA2w7nvrW5BuxEXAwOifUCPQCrqxrtV7QbKgI0OF--yyj18Dy6DPPrlHLrvcGQM6ocGPeQko7twpnhJGvNsMrwE2gMHSheg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✍️
قرارداد «PSG: Champions Contract» خودت رو امضا کن و با قهرمانان واقعی یعنی پاری سن ژرمن و 1xBet درآمد کسب کن!
💰
پیش بینی روی PSG — جوایز تو در انتظارت
⚽️
🏅
شما در
Level 1
می‌تونین AirPods Pro، کیت خانگی PSG و جوایز دیگه رو ببرین، و در
Level 3
نینتندو سوییچ 2 یا حتی iPhone 17 Pro Max در انتظارتون هست!
😎
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
<div class="tg-footer">👁️ 4.71K · <a href="https://t.me/Futball180TV/90079" target="_blank">📅 19:29 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-90078">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6dd848eb99.mp4?token=b75An3GqSObJcFSIiPin5JPCLbF62Sg-mjGCxPiUa_NARtQvJAhvT6BJKbsaNp6QnGoLDuBI7ILVmywcamH6Me51tcD-ojD2ykh7TmPIDgv7KyiGlUDfUhKefOEBlima15xuk20X29ZuRk4bBUgXzqJwntC0NSWrV_hm39xKrV9VH7bRNbJ6mjGhO2PUDfcBdhjmmtTkFi6fJ7kcOy8T2x4xhugxvpGQt4U0MnQx6O0iBH1RHIgPBE4Gft3GOnM00LmC12bCzNrRiqGUIk0m-Qre2xP0a-XTAg3Ok73Ulhrc5oO1qIkU3Z2MqhiDPWasgA4QlMhS1pO2wzlXl_WypDzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6dd848eb99.mp4?token=b75An3GqSObJcFSIiPin5JPCLbF62Sg-mjGCxPiUa_NARtQvJAhvT6BJKbsaNp6QnGoLDuBI7ILVmywcamH6Me51tcD-ojD2ykh7TmPIDgv7KyiGlUDfUhKefOEBlima15xuk20X29ZuRk4bBUgXzqJwntC0NSWrV_hm39xKrV9VH7bRNbJ6mjGhO2PUDfcBdhjmmtTkFi6fJ7kcOy8T2x4xhugxvpGQt4U0MnQx6O0iBH1RHIgPBE4Gft3GOnM00LmC12bCzNrRiqGUIk0m-Qre2xP0a-XTAg3Ok73Ulhrc5oO1qIkU3Z2MqhiDPWasgA4QlMhS1pO2wzlXl_WypDzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🙂
۵ صحنه بامزه از گزارشگران عربی :)
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.58K · <a href="https://t.me/Futball180TV/90078" target="_blank">📅 17:31 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-90077">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c2bf46e469.mp4?token=phVQkV8qj4VUBYsWSZrtVkAev7Y6w-ZXDaqMYdeTfXlNy2b_j2dVmpG8REzu_x_ydHRWfvecAwDxcuZiQsbumEtc4iAmPtgg7ZDkALnbBsehTTrmkCLPT4eaIOmCze_D4Yud2uQjVpN2mLrwpo8TQz6RnCptv30gwMnJpA9apuwpGsGjt6wnAaQTunXNJQVX8urersgSJHe5gfxvCh01MKvb58_PnDIwZ_w5IuvigWHE5Q-1qyfvuUG1VXxc7vm1RCgCYMiIedERZ1ly2ZlrhnZgWRTei43YmFSVbZVNCj6XvtqzJrD6l_3hJIASlolLP4y41zemMkdko3bBUhMsQA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c2bf46e469.mp4?token=phVQkV8qj4VUBYsWSZrtVkAev7Y6w-ZXDaqMYdeTfXlNy2b_j2dVmpG8REzu_x_ydHRWfvecAwDxcuZiQsbumEtc4iAmPtgg7ZDkALnbBsehTTrmkCLPT4eaIOmCze_D4Yud2uQjVpN2mLrwpo8TQz6RnCptv30gwMnJpA9apuwpGsGjt6wnAaQTunXNJQVX8urersgSJHe5gfxvCh01MKvb58_PnDIwZ_w5IuvigWHE5Q-1qyfvuUG1VXxc7vm1RCgCYMiIedERZ1ly2ZlrhnZgWRTei43YmFSVbZVNCj6XvtqzJrD6l_3hJIASlolLP4y41zemMkdko3bBUhMsQA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👍
شادی نیمار از حضور در لیست تیم‌ملی برزیل
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.33K · <a href="https://t.me/Futball180TV/90077" target="_blank">📅 17:18 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-90076">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/f1aTHQuAKPQWDzMiU9dP6dR1KoqoilheLD7OjSwzMr0TlvvSk5vWjUZp7RBbTogNJl3s583sMzy02udUpmIP4YqBYBPexuSi0cbLAHqUlwaY4u-NyzbN9ddIRklGGAIQmpTStye7bO97EeQyQyKxdAOBMWiMXxzJhaJEYj_0PD0tHacv8tAlidV7OcgekZALYACDD9set_ENI0HEzx8NocLyVejL7CrfhGNvZM8zJmve50VxbwPc0UWjMtTr9hIvi0t3ATTDnrvbaS2TmO8FKOt6dSpLtb_i-Q744P5ZQYmTaWPlN7HU2q9tZBhpSR8XANRWu-Z8GiiAwjjKiqC_Ew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇵🇹
لیست تیم‌ملی پرتغال برای جام‌جهانی
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.48K · <a href="https://t.me/Futball180TV/90076" target="_blank">📅 16:29 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-90075">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ebe3576e35.mp4?token=QcOmrfL9Vk0ws6tU912uhQe9IQANvOQbNvd6bvCAplCEhdemjp2gAgHXVTtaIQuS5ioBLg00gbbWaP8B5hKrfWGLLry4M-3yedJFfgbO5uP7fivVnZoIBWKl48W0qIOp3gFzxN_h7fdMPjfq9ysijUKrRQDe6iszR7jBgBLV1fivdZCz5YTDUbgNiTHOO830YC8voAx34kHEckNezboVfZipo9we_QOdwXMTR8xZKyHMx6Uw13o7L8PAxHN8D45iC9qYcsZzIK7INFZh2wCGG4j5IowPE4wNv2d2-dzcojTOd2dEVnI0tLzs-UfDDfwGyTpt_Awmg3snGLilqhCIoQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ebe3576e35.mp4?token=QcOmrfL9Vk0ws6tU912uhQe9IQANvOQbNvd6bvCAplCEhdemjp2gAgHXVTtaIQuS5ioBLg00gbbWaP8B5hKrfWGLLry4M-3yedJFfgbO5uP7fivVnZoIBWKl48W0qIOp3gFzxN_h7fdMPjfq9ysijUKrRQDe6iszR7jBgBLV1fivdZCz5YTDUbgNiTHOO830YC8voAx34kHEckNezboVfZipo9we_QOdwXMTR8xZKyHMx6Uw13o7L8PAxHN8D45iC9qYcsZzIK7INFZh2wCGG4j5IowPE4wNv2d2-dzcojTOd2dEVnI0tLzs-UfDDfwGyTpt_Awmg3snGLilqhCIoQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خدا رحمت کنه زنده‌یاد علی‌انصاریان عزیز
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.43K · <a href="https://t.me/Futball180TV/90075" target="_blank">📅 15:30 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-90074">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1631168f15.mp4?token=lzpqfON_eRDj_sPR6j5L1MiYf2EBRrZPrTKPCWDYqI7wBrSF5LkSRThlyAsKkMAP_dxD-0xXnndCxQhH6DO86OSya_86AcAWBmKfuhjxyHShi2nXBTCaQe2-4hwcScmM-sffsGnOb37TCcV-FQwdCQhd_ycZjc2tHUVISD3JcCt-3dsuNov9Xo1jNC3focnLmmWHzyhwqjbtMV5a-og_KlpphrgiEUie4d79Q48u173RbHN8AnHx2ssaYauuwhrebCnCwS2em69xuLY6lBu0XlLufHurq0Fmxy0BpRfEck1XKi-KXSW8Zvkhg04OmjvnpMBwlnZaSyMxCd7dWJPbcQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1631168f15.mp4?token=lzpqfON_eRDj_sPR6j5L1MiYf2EBRrZPrTKPCWDYqI7wBrSF5LkSRThlyAsKkMAP_dxD-0xXnndCxQhH6DO86OSya_86AcAWBmKfuhjxyHShi2nXBTCaQe2-4hwcScmM-sffsGnOb37TCcV-FQwdCQhd_ycZjc2tHUVISD3JcCt-3dsuNov9Xo1jNC3focnLmmWHzyhwqjbtMV5a-og_KlpphrgiEUie4d79Q48u173RbHN8AnHx2ssaYauuwhrebCnCwS2em69xuLY6lBu0XlLufHurq0Fmxy0BpRfEck1XKi-KXSW8Zvkhg04OmjvnpMBwlnZaSyMxCd7dWJPbcQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👀
ناراحتی شدید خانواده ژائو پدرو ستاره چلسی از عدم حضور در لیست برزیل برای جام‌جهانی
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.56K · <a href="https://t.me/Futball180TV/90074" target="_blank">📅 14:33 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-90073">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/n8eVfyl9QteFGVsSI6oLzUH-mCZvJUzCA45QwzFhd9CZ2s3EsH03Xc2b8Aa3PKKNypxVpHRR0hDOVGm0De_d0vbMTdcw36nlbejiYqFq-_6MgxHfUUYchdWKLxmMfXvT6WXvuKFb5CefPWLPINqLbzFW7wHuu_aflIrx_eB45GdTPR7_ESSZvxcznP-LyjpdGkex0NBdQEJ24Qa5YbPXBk3RCg78del_GAptM2y8yEtdQdG5rJDc6xtlpva1ZpTcXNejJtpkCmd0BW9IBtw7zADvbBYp7ANrFLWWt9JsKti3rK1VkedsCgR2zMuOKJmJFprrC8vYhFouEIdLmyaKbQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
رئال‌مادرید با ارائه پیشنهادی خواستار تمدید قرارداد یکساله با آنتونیو رودیگر شد
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.49K · <a href="https://t.me/Futball180TV/90073" target="_blank">📅 13:40 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-90072">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SdUQA4PQ1Mzk4jfdfPB9L8ELmf_jrV0TH04CGURnz_I9jx-G1d15kH1aRV5d4TcmZ3jWWXWxaqWkhbZADg3roUbURdxY4pxEVpcKsRJiXqHGZEoudPRMSr-Bs7Rz7dJunWIZtSfMuJG8wEqLycWQzIBTEfZQxISEmP_YZAZlyaSSea-VlXNpmfzexRA06ytZz4DeJyqL4o8wjV87dW1hbukLk8P2-gDKO7XAXcaH7hY8tiDWDS1RZ1vaakeoF-R7tL6k2oRhEDbCSxxnAMd8IGOPUPxfViCcPA124BSlhWpgCqfV8J3cYNw7xYQcM7Gd69vrMW3oPXkntfd6_HEJow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
منچستریونایتد قصد دارد با ارائه پیشنهاد هنگفت با لوئیز انریکه سرمربی فعلی پاری‌سن‌ژرمن قرارداد امضا کند اما در عین حال این مربی پس از پایان‌فصل قراردادش را تمدید می‌کند
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.45K · <a href="https://t.me/Futball180TV/90072" target="_blank">📅 13:11 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-90071">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c098031df0.mp4?token=H_43JgEqzztSQvq5c6D3Ywdka9huvpyyKMHAN7awO7NcPckNiwJ465aJAMr0lx_ydPyZKDvmS7rJMgu7wJ5uDeiRXinr9A9xSqrElsCeSyMV8kVmW7aghuJv104o0ZbOF11gRKlVMrfrM4VSo_dgDHrwB88EF18S02RBoc6tSjQU4LGHEI1sVi9Xs3K1FHSgZincS7dERzc8DeG-5s8BvPhnpp_jsRjb0UU3R7QiyLQaZOPzDqz11mdbIHuyT6m4m4nHYoQkooBpyTTlYckrgD8l_drTxW6HpJeAE0HIm-8xnC82UC-N1q_KlOf2wub3vCetsw6NRTR1d2kI-Hj5MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c098031df0.mp4?token=H_43JgEqzztSQvq5c6D3Ywdka9huvpyyKMHAN7awO7NcPckNiwJ465aJAMr0lx_ydPyZKDvmS7rJMgu7wJ5uDeiRXinr9A9xSqrElsCeSyMV8kVmW7aghuJv104o0ZbOF11gRKlVMrfrM4VSo_dgDHrwB88EF18S02RBoc6tSjQU4LGHEI1sVi9Xs3K1FHSgZincS7dERzc8DeG-5s8BvPhnpp_jsRjb0UU3R7QiyLQaZOPzDqz11mdbIHuyT6m4m4nHYoQkooBpyTTlYckrgD8l_drTxW6HpJeAE0HIm-8xnC82UC-N1q_KlOf2wub3vCetsw6NRTR1d2kI-Hj5MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✔️
پاکتا هافبک تیم‌ملی برزیل و دوس‌دخترش
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.51K · <a href="https://t.me/Futball180TV/90071" target="_blank">📅 12:58 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-90070">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">1xbet_ir.apk</div>
  <div class="tg-doc-extra">51.9 MB</div>
</div>
<a href="https://t.me/Futball180TV/90070" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🔥
ورژن جدید اپلیکیشن وان ایکس بت بدون نیاز به فیلترشکن برای گوشی های آندروید
🎁
اپلیکیشن رو دانلود کردید موقع ثبت‌نام، کد هدیه 1x_1566529 رو وارد کن و تا
100یورو
هدیه بگیر!</div>
<div class="tg-footer">👁️ 4.31K · <a href="https://t.me/Futball180TV/90070" target="_blank">📅 12:58 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-90069">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fc9QvriIc2djAtqlI6mj70pHtFMCBWEsNto1LycNJEAxL2GfU0ppgxMlZzsYM9sWafVKDqIZz6356x8JfN0QwxyWDbBEJJB4gmKnl8ybbSlwVHcGzFP--8VdcCZcAQ_RrXgqKwI_5fXYpGwXVTTeMCrEd7O8YFPaV8BMwibwggtrDOXHk4SCK7kIwIYfo6H9TEt4N5wF-7Gxm3OQ1qnZIcPf74QSHKJdW1zxFVtzoYEebN6yNlkoKYkxxNUR8cN4nhBNJvjvR4w7yrPKjH8aOKMqOWhj__FV7FUzFggP4FlLe8ZBCFyRBKU0hgVxNaNQiJhSXqPqZUtkYeQdeg6Y1g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
Ole, La Liga:
بر روی رویدادهای مسابقات فوتبال لالیگا پیش بینی کنید
!
💰
در ابتدای هر هفته، یک پیش بینی رایگان دریافت می‌کنید.
✅
هرچه شرط‌ها بیشتر، پاداش بزرگ‌تر!
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
<div class="tg-footer">👁️ 4.44K · <a href="https://t.me/Futball180TV/90069" target="_blank">📅 12:58 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-90068">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DFOpthyRl4GYRtcXI6MPdEMg4vt13paQNeHSVCpe5dIODDNznOCXE2IPkwJx6UNEWKUy5mW8UGcRsRqhydgd-5Cq8MWx2_df2dH5z5H20L_Fu8BYe7khCI5RRQErxf8GjXv-Icq9CruKlXzcVA_NpTlTrKSXGHMvEejoF7jInsdgnC2ZZ8kZFMIQ7bdOTyy2zPrc_mlxds5t5A_6mX40mVBL8M4QloKXRI-ocfkghOEBZW-r5JQK5PqORICHLhLSmhLYFdCfjoV_tE0oXeT739FcR-OYDbqD8vKi75-pKQkcSG4mSIwp4yhAp2B5VHQwic0rnPNe9PAs-SZklhhYCQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇮🇹
کیت‌اول باشگاه اینتر در فصل‌آینده
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.36K · <a href="https://t.me/Futball180TV/90068" target="_blank">📅 11:56 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-90067">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OFGcMP1wAiYRZnsQ12uYUikcejIvshDkWfzNHRiTEjEZbEtqPEbK0gJZtzc3vaC4jVz3WXOylwbQK2VwiTWnpeQsT3qfcd40h09IOFHn9QMR68YLs6Ei0Lgq1I43UVChZh8DhthqZdfGm7sOsRos1iayX9EqUgT8SLdR9m863bsdwShP4TSpoVc8PqOFicodmcmNKhFIigCf4mVewx0cqt2EwJhc10wJNDW9yns3gEgA4znAg9a4-oPWv999dNLkRG4IGljtyGDQeWSkMrNgD5FoRhcHuYZeEAmN_1Ko6TpIa-0z0awg_i2vmqcgcDaymN9S1QPCiv6AGhl78ZQNAA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
کیت‌اول فصل‌آینده لیورپول
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.37K · <a href="https://t.me/Futball180TV/90067" target="_blank">📅 11:24 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-90066">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f1fd62d6ae.mp4?token=NLsobhJJl5iKH-unpbjgsKNLea_WjycErdF29-k81yuT9Hm_JbM4dLb-IsLqeIQm4yABPMD1Qk5kEePXwSDlv5W_SJY_-yJh8gTaVsTvqP4fxu9hlirYmUhqt4F_IVJwlQexsSQkmqIByx8GcRCVgIM2eFjAoLXq9gYWsuNz7qNoz_pWpH-Xv8dhPIPhiKTmcxZKHafxkRiSJ_C4rAyhZFRB7duPiZ_0kiclI2xowJ3PxDFus4KSZdHTH7cT8n9o2XMzhZrS-Wq42diT-dvqYAuB3vmvF0X-Lw9_tty0Pl9M_Vc9Q--Yq_feDKqF-5yEpJ2DZmTt1hNzaTebIq5w2w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f1fd62d6ae.mp4?token=NLsobhJJl5iKH-unpbjgsKNLea_WjycErdF29-k81yuT9Hm_JbM4dLb-IsLqeIQm4yABPMD1Qk5kEePXwSDlv5W_SJY_-yJh8gTaVsTvqP4fxu9hlirYmUhqt4F_IVJwlQexsSQkmqIByx8GcRCVgIM2eFjAoLXq9gYWsuNz7qNoz_pWpH-Xv8dhPIPhiKTmcxZKHafxkRiSJ_C4rAyhZFRB7duPiZ_0kiclI2xowJ3PxDFus4KSZdHTH7cT8n9o2XMzhZrS-Wq42diT-dvqYAuB3vmvF0X-Lw9_tty0Pl9M_Vc9Q--Yq_feDKqF-5yEpJ2DZmTt1hNzaTebIq5w2w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سوپر صحنه بازی دیشب آرسنال
😂
😂
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.25K · <a href="https://t.me/Futball180TV/90066" target="_blank">📅 11:15 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-90065">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
قرارداد آرتتا با آرسنال در پایان فصل به مدت دو فصل دیگر تمدید خواهد شد
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.26K · <a href="https://t.me/Futball180TV/90065" target="_blank">📅 11:06 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-90064">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BTzCPDUHpK3jtDaiFi_zOX0Wrd_dmXby4Y20vCuwLNFRR19ZK5YkrK_MIf5MYF0z0akQThIPSHEl7qto9dt5wAv6-w5wPAjuFMrF6bKuF9HnsxyYA8FOzEeJvhEWV6qX2qAOPyAj2H8DC94X4tj8R-walq-bQHiOAliXM8pNblwyCX0HajnGx-kPdv0uAUDcTh2gxzQNtwxmUOc4NSQmeN14IAzgVIdO5rjeZ-zgx-6p8Sday33U0awTO7cokgECj5zgscoPrJBezE_JF67f8lS7jJ2BeLxBNr_v06hqnO34o1MwEtlxOfCm0aZB6YqRnADVEsKxZrsL5EUdKb-K9w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🚨
با اعلام‌فابریزیو رومانو، انزو مارسکا با عقد قراردادی سرمربی منچسترسیتی شد
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.62K · <a href="https://t.me/Futball180TV/90064" target="_blank">📅 10:50 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-90063">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7a4a423232.mp4?token=GqZWAlj-1w6OyTCLtmiNnG10WVTi6ZIQYW3xNxB8VsuBz1K1yVoOybvTTaGHf-LNLyD0CQiZ_ktVWxEl1zsKjbd7gA7zC8YV3teqWbCxy6dk8K3aQOAv1wpxWNwyGSECo6uHP6xNV5fbbRonPLysAh-7TEGIwcbsrrTyUqfu115WB7T_Qz2FXj9UXXNQmE7ZweZyQZvO0h22roXasEdetC2trD7MkEj6ZTskX5agarYszp7uNNDcbJ6r0VuwjkfT1Gx-kdRRV1KAxVbrBMQdKXnbwBPBqU7-WOavHL8YHkWCcEqWQwHumRq7rBGzEIfaj0zDheey4X83VqpZskoVhg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7a4a423232.mp4?token=GqZWAlj-1w6OyTCLtmiNnG10WVTi6ZIQYW3xNxB8VsuBz1K1yVoOybvTTaGHf-LNLyD0CQiZ_ktVWxEl1zsKjbd7gA7zC8YV3teqWbCxy6dk8K3aQOAv1wpxWNwyGSECo6uHP6xNV5fbbRonPLysAh-7TEGIwcbsrrTyUqfu115WB7T_Qz2FXj9UXXNQmE7ZweZyQZvO0h22roXasEdetC2trD7MkEj6ZTskX5agarYszp7uNNDcbJ6r0VuwjkfT1Gx-kdRRV1KAxVbrBMQdKXnbwBPBqU7-WOavHL8YHkWCcEqWQwHumRq7rBGzEIfaj0zDheey4X83VqpZskoVhg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
🤯
شادی فوق‌العاده برزیلی‌ها از دعوت نیمار
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.42K · <a href="https://t.me/Futball180TV/90063" target="_blank">📅 10:00 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-90062">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2da1d08628.mp4?token=KZ8HlqZ4d4tbxKhKQDCJSJPoFLNFy1VgIP5-92PKnmIbE_xXc9ne4PyRkxbBl6B_VA_Nxkt-pSHU6GiuByVxodgk7amJoyVrGvrQGJQI7Dhc9F4ZKy7uueq-kvOFPZzkpajlCigsS7nWkkabMijy4rTF7so2EEv75LnaH4FPpdC5fdR5ZwCVTHzz1TZfZRtdn3bsFyRMvMErqBcSWvwMbj2O8q-B6wp1GQHHsmF5Fwg5m6cl_MAN0563OxctxhZPwRMh4VkQSByPHYMnwkgygOTtZcytx93QObeC6yRaXoGRMUr-4tWbJu13gcfvnTUlgKOr5HWxhn1wHvKgM-pFdw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2da1d08628.mp4?token=KZ8HlqZ4d4tbxKhKQDCJSJPoFLNFy1VgIP5-92PKnmIbE_xXc9ne4PyRkxbBl6B_VA_Nxkt-pSHU6GiuByVxodgk7amJoyVrGvrQGJQI7Dhc9F4ZKy7uueq-kvOFPZzkpajlCigsS7nWkkabMijy4rTF7so2EEv75LnaH4FPpdC5fdR5ZwCVTHzz1TZfZRtdn3bsFyRMvMErqBcSWvwMbj2O8q-B6wp1GQHHsmF5Fwg5m6cl_MAN0563OxctxhZPwRMh4VkQSByPHYMnwkgygOTtZcytx93QObeC6yRaXoGRMUr-4tWbJu13gcfvnTUlgKOr5HWxhn1wHvKgM-pFdw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👀
خوشحالی اندریک در کنار زیدش پس از حضور در فهرست برزیل برای جام‌جهانی
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.57K · <a href="https://t.me/Futball180TV/90062" target="_blank">📅 09:02 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-90061">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1bf11ae109.mp4?token=LVuYJIeWp6HrAexW_IT4VASrLPDNFnYN5b6HLxkO14YI3tpOdtJCDblGqrLRZ1xPxu82b2KAr9FxKyH6trOP-eB1LrnEmSTYC_QBpwDsxASYV8IGESXY21tkZiyxYde3LRsNLWpckS310kWdhl0dJ31sYLAuA_uMCsPOkvqyAd6MVOxspz2CMI-e6p2oiZG-73A2ZaQD1OOKQKS_cxLSFOmifp5bRqi6xPXy3ZE-Ynh86OHw90XzPBSJnAfESqlTYRXAv-Rl2UxzHiE1nwOPzFgHOWndyOIIpnfYb7NmpB69I3xwIuA34ma7JaGrN2bWWgums_Qq0cLUsN6OztjtgQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1bf11ae109.mp4?token=LVuYJIeWp6HrAexW_IT4VASrLPDNFnYN5b6HLxkO14YI3tpOdtJCDblGqrLRZ1xPxu82b2KAr9FxKyH6trOP-eB1LrnEmSTYC_QBpwDsxASYV8IGESXY21tkZiyxYde3LRsNLWpckS310kWdhl0dJ31sYLAuA_uMCsPOkvqyAd6MVOxspz2CMI-e6p2oiZG-73A2ZaQD1OOKQKS_cxLSFOmifp5bRqi6xPXy3ZE-Ynh86OHw90XzPBSJnAfESqlTYRXAv-Rl2UxzHiE1nwOPzFgHOWndyOIIpnfYb7NmpB69I3xwIuA34ma7JaGrN2bWWgums_Qq0cLUsN6OztjtgQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🥲
پایان عصر لواندوفسکی در بارسلونا
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.55K · <a href="https://t.me/Futball180TV/90061" target="_blank">📅 08:00 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-90060">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">تو چنل بتمون هرشب داریم به سایتا تجاوز میکنیم
😄
ما هیچ فروش فرمی نداریم و نخواهیم داشت و کاملا رایگان فعالیت میکنیم که کنار هم به سود برسیم
🤑
🤑
🤑
@FutballFuckBet @FutballFuckBet @FutballFuckBet @FutballFuckBet</div>
<div class="tg-footer">👁️ 4.65K · <a href="https://t.me/Futball180TV/90060" target="_blank">📅 02:08 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-90059">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ueMBEPU-PtyPdKT9I1XuJoYD1mWcZckKJRQhFOtpJCZVd5bicbpOWXBX0jtqsFgpjvm2khPjkW6CSGYpi5XrJR3Ws5tC1J5e5EdL3YvN_rFVNmEghgVaxyDEzsPFBsqo6POlUmVvjQBVTR31qgKdOskG7O08NrYMfsTfbcx6vpeTHlkwLcMq2cSQNbfWFeOPkXTmrseDodfC4PUygSLMxndX00PCrk3id3PFI2FWz8N7IugvVwZWjOfkhDlJpWAdoo5E9kj8AWPZ5xrz61YcXo-xblIaRHkp3g9YWqqnhZI99Rs8y0RIBNnxGNsO_hU2bu4b8pejyIFOt2oqdr9duQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تو چنل بتمون هرشب داریم به سایتا تجاوز میکنیم
😄
ما هیچ فروش فرمی نداریم و نخواهیم داشت و کاملا رایگان فعالیت میکنیم که کنار هم به سود برسیم
🤑
🤑
🤑
@FutballFuckBet
@FutballFuckBet
@FutballFuckBet
@FutballFuckBet</div>
<div class="tg-footer">👁️ 4.8K · <a href="https://t.me/Futball180TV/90059" target="_blank">📅 02:08 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-90058">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/de7e2f01eb.mp4?token=Iz5lCzPob--6bC8iOdfEKLXQi2ofcMDSrd1K-c0ufoEDv_0LX84ajtir5rrJ7VFeilYBS_fsZGUvNeFLen_GMDcRH2l5H0IdjdB72_QhFj9zlP-sM14IenUR_vrGIFzX3LfEAl8Dh1B0pk_aZ64g0jgdGSfTKSV900CvXhQDur7LltnX9-2IThufRRIAPzTcETD3R_TUIaKC3RRzYj6d2knBCbddtrGmaqWxzQ6ABulaE2Z1un8EfW6XU5fImq1mqOP2n8_GFnz5y5Pf54iITGNRqlXe8LbRWSi8CMZRft0cyz2AnT7PxIv6shG5rZmPgRSeUYUipsW4aMZ1fOqOOg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/de7e2f01eb.mp4?token=Iz5lCzPob--6bC8iOdfEKLXQi2ofcMDSrd1K-c0ufoEDv_0LX84ajtir5rrJ7VFeilYBS_fsZGUvNeFLen_GMDcRH2l5H0IdjdB72_QhFj9zlP-sM14IenUR_vrGIFzX3LfEAl8Dh1B0pk_aZ64g0jgdGSfTKSV900CvXhQDur7LltnX9-2IThufRRIAPzTcETD3R_TUIaKC3RRzYj6d2knBCbddtrGmaqWxzQ6ABulaE2Z1un8EfW6XU5fImq1mqOP2n8_GFnz5y5Pf54iITGNRqlXe8LbRWSi8CMZRft0cyz2AnT7PxIv6shG5rZmPgRSeUYUipsW4aMZ1fOqOOg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">😍
خوشحالی مارسلو برای نیمار
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.64K · <a href="https://t.me/Futball180TV/90058" target="_blank">📅 00:49 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-90057">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/b-Ak6FKx-VAnr792151-xpnBPnfZrekOlLkQo4oTccY0KGa5rFEi34nOI3-aDjanAf6xPRhBJmLksTCdzemFVGotEEZjCWN2Wre53LUkf_yvfDhWx2JDP7TZknpfbSlSNJV_FfztKRGnyfkFxq2_p_sGcpGfr3IfYfD9473BLhi8aq7x2wDI0kzg49OK2b8l9fXVTsblCAUZYFBgmgq_4cdcmLiZNVt4z85kwiFFmPRXxSs4K3hlHfZCgNmQCkucUnG60Q8tFOsEDr4b9GKpiDjHanMw1sKHYTzpROqb4xLmmR8e0lenuJuQAvDxXpDiCEW1zaxxBwW282do5-qyzA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
جدول لیگ‌برتر انگلیس پس از برد امشب آرسنال
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.59K · <a href="https://t.me/Futball180TV/90057" target="_blank">📅 00:40 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-90056">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ABHyYXEehJkOzfesrjueAbtsgf1Ov71THaNJPpFcBxv0O2_LoSaUYuHmDQpcPJx2lPJyEHJsb4BCyOlqdFiJaOWRhynWwPNyUfUMP0qB6aG3FAFNi-A1lDGvxIMD2-JNfmV0jOnzt_BN0jb7E33QtN-vAtF14eWD3zogDOmw0yf9lOqy-8cJptCFG2w4m92baGreUrVHeABYdKJyVCOZVphaAdlpd74meFu5StcMoiBVYEhnItwj9Np-VdR35wejWmjgJ_2Ffa_kIjq62LdI1NqI6JC3xp3NctQuKG7UvYW8Ocf1PtB-I61gsw3tLssJXVrqfNs1a5i67HHpcvgvFw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇧🇷
لیست‌نهایی تیم‌ملی برزیل برای جام‌جهانی
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.54K · <a href="https://t.me/Futball180TV/90056" target="_blank">📅 00:37 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-90055">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VDWkSv_em99CHbBYqE-MKmrOBJNQQRL0MBariq-48hCzFcYm0j_fhxcdJHSnaDbQ4DN2UtTiE4ZgmnBdVjqgPyancfuP8JbQfhEEfYXBmadEh5Bccyz8hCsc0gEcmQy3VW8OK_SKXp9EbgbJi598QolOHGZikKVwoILRP8F8T-QDKoQhDlS0ghZW7qi6JGJgHb2YOKRHaP0AK6s_9S-ft4NvrbQ2IRrUHc66yvtOegrjvLBExzJKC5CMKCNkwDjIlh-tHS0RFTD332E_XvHaDU_HviaV4ai_iNfvnNwbe8_8KVXmlHMtW5n2WGzUEQ3pCJ1GQNOIvyhlanMKGYu9sw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👀
نیمار بیو خودش رو به پرچم برزیل تغییر داد
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.57K · <a href="https://t.me/Futball180TV/90055" target="_blank">📅 00:35 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-90054">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6072fc8645.mp4?token=k8YXDL6DSAUSMcuGQ6D6weitl31tjRb9vZZ38z-k-HJhYJVQlICuWM83GssPSnJukJWiK1gUNkyHnyQmdSRO-YnTJ0yALXbdSNOuam4DzDxKRZ9bNfLxDkLz4lpxGfoPzwcdFyRqxrwJseXm8kMql9m32F2y79-h0FroFhsQdPDa4oOhUauG5kqxZnZamM5sJ11rbpwR92OKQxAgLhZbTFuZpsmiqSC7gZQbCDqp1-yd4SnjSsGyZ3-Jt8E6AA0OobBaAB6ywPbnL2YCigSiz07_hb2-OuwFDsAZq-3vtao8WnjA1Tr4xfNK_gnBs68da-d7sMAG9RlvVa770j-omg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6072fc8645.mp4?token=k8YXDL6DSAUSMcuGQ6D6weitl31tjRb9vZZ38z-k-HJhYJVQlICuWM83GssPSnJukJWiK1gUNkyHnyQmdSRO-YnTJ0yALXbdSNOuam4DzDxKRZ9bNfLxDkLz4lpxGfoPzwcdFyRqxrwJseXm8kMql9m32F2y79-h0FroFhsQdPDa4oOhUauG5kqxZnZamM5sJ11rbpwR92OKQxAgLhZbTFuZpsmiqSC7gZQbCDqp1-yd4SnjSsGyZ3-Jt8E6AA0OobBaAB6ywPbnL2YCigSiz07_hb2-OuwFDsAZq-3vtao8WnjA1Tr4xfNK_gnBs68da-d7sMAG9RlvVa770j-omg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">😂
🙂
شکار لحظه‌ای صداوسیما از بازی امشب آرسنال که با برتری یک‌گله این تیم همراه شد
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 5.01K · <a href="https://t.me/Futball180TV/90054" target="_blank">📅 00:28 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-90053">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uj4eSxIX4UPvvYJogqwaonXEq6cdjM_II8GrIo2JziGzYuWUg2Yg0hyElvMvXa8aMBhtETVmCrYkLB5DQUWC2xPbJZkwAX6ASRMXQz9ny742XdnKX9sdYo7SMfvblZ6zBrENa2wCNcUsR8rvqoqgVKyGYRwNXfMtUlOwOSN4aOKTdnTBo27FknVKpAFlvPanNTFZx31lDOHS5PffXAd3o5FuXTrVdEPkqUxczNIm3pjjes7prg-bfuG1eTr_YgpAQZnHfqKTJKjNRPvZsx3JtZFfFXNYsDbRD-TNhtLjKhNc38YgcDNBRFyeZAudSR0l2zwu-AkVpr1tFCTpQ-3D3A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👀
نیمار بیو خودش رو به پرچم برزیل تغییر داد
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.88K · <a href="https://t.me/Futball180TV/90053" target="_blank">📅 00:19 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-90052">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">🚨
🔵
🟡
🔴
با اعلام سخنگوی فدراسیون فوتبال، سه نماینده قطعی ایران در آسیا در صورت کسب مجوز حرفه‌ای، استقلال، تراکتور و سپاهان خواهند بود
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 5.2K · <a href="https://t.me/Futball180TV/90052" target="_blank">📅 23:40 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-90051">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">🚨
لیست‌نهایی تیم‌ملی برزیل تا دقایقی دیگه توسط آنجلوتی در نشست خبری اعلام میشه
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 5.08K · <a href="https://t.me/Futball180TV/90051" target="_blank">📅 23:38 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-90048">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
❌
پپ‌گواردیولا سرمربی اسپانیایی و پرافتخار تاریخ فوتبال از منچسترسیتی جدا شد
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 5.07K · <a href="https://t.me/Futball180TV/90048" target="_blank">📅 23:32 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-90047">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mDGgVppSVjb9B3jleDEgrPLHr21aNAigkrqHRqhadh_Q6uwZEwtS_l_n29XcvBW7JJ70cEYBh8Qu9SXOSsgAvgVrEIi8gPY6EzD_t2Rv8ZJwU6029hZjXxLPEwVkyVRNNyWZGMwNrxVjIHd9itsMIExg9cPCtg4WuMvh-bcsjqXIDT8Dmo3smta4_fyCAsUfz34N8Mv_FYY0PKTRWzRPd6bZZue2lqE7aKPLiHf0-h2zZ8a_k8lGPxMH8CZiduxEJZqbU-6jYbDH6VYjQv_oQqUPSmB-ph4VewFp0l-bPiSIG_TGgLLJGDTOYIBVvxK42yrkThIIB6RL0Ujc1h94iw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
❌
پپ‌گواردیولا سرمربی اسپانیایی و پرافتخار تاریخ فوتبال از منچسترسیتی جدا شد
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 5.13K · <a href="https://t.me/Futball180TV/90047" target="_blank">📅 23:25 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-90046">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">🚨
🇺🇸
‼️
فوری از ترامپ: امیر قطر، ولیعهد عربستان و رئیس جمهور امارات از من خواستند که حمله نظامی برنامه‌ریزی‌شده ما به جمهوری اسلامی را که قرار بود فردا انجام شود متوقف کنیم، زیرا اکنون مذاکرات جدی در جریان است و بنظر آنها، بعنوان رهبران بزرگ و متحدان، یک توافق حاصل خواهد شد که برای آمریکا و تمام کشورهای خاورمیانه قابل قبول خواهد بود.
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.95K · <a href="https://t.me/Futball180TV/90046" target="_blank">📅 22:38 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-90045">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c28244d9b4.mp4?token=vmc7h8caSkJZ5sAUieZUeqfzDAzy6xaGRwdAkQlycHMAzZ7AomsH9hJ4CULL31JGeGHYZIexdi00UpMQBZ7tklIT9euFM09PpO6DunowBO4uKGH7WCd3r8Y42p7xoImC0soQef6KDpJgBtAKD4HyGIKJPZwcy40qQiZpnAjgMB_-39dBablcMBuajVjWt2th6O-iow56qZFYfheJRC5Ur1pyHm91gBJCXlQ0Ofsg9qZA502n3Z1DHOv6NO1l8uJeXS9o78tGRRsGJQYIdwFWtMUA3mVG9gwm4Fto8qBw0BKyHq_YxKhm1A07pD4N4Rsw9jaeCJcptVvJlWHSZdiDng" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c28244d9b4.mp4?token=vmc7h8caSkJZ5sAUieZUeqfzDAzy6xaGRwdAkQlycHMAzZ7AomsH9hJ4CULL31JGeGHYZIexdi00UpMQBZ7tklIT9euFM09PpO6DunowBO4uKGH7WCd3r8Y42p7xoImC0soQef6KDpJgBtAKD4HyGIKJPZwcy40qQiZpnAjgMB_-39dBablcMBuajVjWt2th6O-iow56qZFYfheJRC5Ur1pyHm91gBJCXlQ0Ofsg9qZA502n3Z1DHOv6NO1l8uJeXS9o78tGRRsGJQYIdwFWtMUA3mVG9gwm4Fto8qBw0BKyHq_YxKhm1A07pD4N4Rsw9jaeCJcptVvJlWHSZdiDng" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👍
لحظات احساسی لواندوفسکی در رختکن بارسا
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 5.07K · <a href="https://t.me/Futball180TV/90045" target="_blank">📅 20:12 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-90044">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RN8Uw5oSVyK92jYoc_PyNQaXOT__XaRnvxvcDJgORYTrNhg_SJWAiVjPksGh6eFma1X6uURcLltEXDejaffKrUfEQm5wPhY_ZPOuebquzLmfEE51UNjmBDewAbOapS9KuZ7y2G6BJ_ixMKRFBL0PemdUIl5tpyaXzKYIF_CZ7mr7D8liBvLqOZnm2s7WPCjAS8vHzM_8i6f7iED2gmy5ptzzc0lPvxexVU-_aikjrNKB9zRS81QrgqbjA3bY1FU2eXANdWCY3-f5Nh-tnQbfN5SuIEO-bop3gV2VXwGaKMMZHp0H2UfMeP4SMgeZY7tK8zhGj5--9y9FjeWNRiXi_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
🔥
عملکرد ژوزه مورینیو در رئال‌مادرید
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.46K · <a href="https://t.me/Futball180TV/90044" target="_blank">📅 19:57 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-90043">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">1xbet_ir.apk</div>
  <div class="tg-doc-extra">51.9 MB</div>
</div>
<a href="https://t.me/Futball180TV/90043" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🔥
ورژن جدید اپلیکیشن وان ایکس بت بدون نیاز به فیلترشکن برای گوشی های آندروید
🎁
اپلیکیشن رو دانلود کردید موقع ثبت‌نام، کد هدیه 1x_1566529 رو وارد کن و تا
100یورو
هدیه بگیر!</div>
<div class="tg-footer">👁️ 4.13K · <a href="https://t.me/Futball180TV/90043" target="_blank">📅 19:57 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-90042">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dHXDErNfjFDQL9Jek5TCC8Gwtv52Lal57_W6yr6EwHlpWixoUNJ2juindwqsXRuTraImoY_feWuU59CeMpno5J7Qbd-deSbMVRxdCjaCIk9zSgKHk3gozl_D2snNQgGBQ2i23sIO2dUmccln7CgYe_V3pyuPjr8QhbReMRUv2Dc-lBxz5uxv0p9mvVTmejE0zrYse1b3oXchjYr5pr-BVzETkUy44mK9bWn3r0c8NdzM-AQ1fD3_l4TtiLOjrB6DAuKTSKWyMoQfFXcjfMBjgiWXNHwz7uji0TYzowlMov02GHWIyIf9faLW3mhef8RKcwRCEQ-hLEsWq9HOYqjjcA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🤑
پروموی Crypto Freebet
🤑
💠
حداقل 5$ با ارز دیجیتال واریز کن (حداقل 5 بار در هفته، در 3 روز متفاوت)
💠
هر دوشنبه
💎
یه پروموکد می‌گیری برای 30% بازگشت وجه از میانگین واریزت
💠
سقف بازگشت:
💸
تا 300$ در هفته!
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
<div class="tg-footer">👁️ 4.39K · <a href="https://t.me/Futball180TV/90042" target="_blank">📅 19:57 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-90041">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CJb370y8F7L6xHWpvS7xsdW_eHZVMPE4x7cR9VSK-9JNrpt_8eH1roOIv0HYF1ZQXNNMLsbkR_HSM8uhqtGnkq5wKNou-Wb-LC5zl3LyGOABhzAt0oIK3UmCeaDPp-Qglj3uXYsrXrZMEYcmjhzvHwSOsi4ueR9HW-r2S3Tc6jEj0R5zoLR9VtOWNKXARG2gjYCQp4i4psIJkncEeNyzKjvPZ8yiv-6zHUa3A5JGWj07Drb--QsBi4VabB5VHOwhxSLfcZ4XWR4q6ummLF2v_jVu0l7GyQnc5DeTC1j9UF9LodHfeHhYOIov3aDX15PlqaJARxi7CvExAacbGuqLpw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
تیم‌هایی که تا الان سهمیه حضور در فاز لیگی لیگ قهرمانان اروپا 27-2026 را کسب کرده‌اند.
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.09K · <a href="https://t.me/Futball180TV/90041" target="_blank">📅 19:46 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-90040">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/OFDrkFiBiIL15GWWuF8Eo0MhqT31cMx1slWVUs-ce3w88WIfboMKC9c8hxoch2bQaRa80LnzZB0D3hHp32fvSMtb6hgnKkp4vkZQgTiC9dn19xvmkf6yl3AwEJuZaciWIiRzozAVtnVwqQlJwBlmo37Ja_M0c_B9HbqAD6ESt5j8mXK_U5RfvPNNCV8cDUWMnXUZZmPTyZzJrLvL8QyUoid77TbkUeF7PEosr9x8ypPNhlVEezvywYKhaRXSMzUewmSK8lHlrod_zaCrMo9ZjlZuoOOh9sqNJ4SaoQPYYMQ4YN6d_N7PWd5BjKEXGeoxw9QZMv4SG1lx--dFeJHYyA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تخفیف فوق‌العاده - ظرفیت محدود
سرویس اقتصادی با کیفیت موجود شد
💥
10 گیگ فقط =>> 1,700,000 ت
20 گیگ  فقط =>> 3,100,000 ت
40 گیگ فقط =>> 5,600,000 ت
سرور ها  v2ray هستن کاملا با کیفیت بدون قعطی
خرید
@amoadmins_bot
@amoadmins_bot</div>
<div class="tg-footer">👁️ 3.99K · <a href="https://t.me/Futball180TV/90040" target="_blank">📅 19:36 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-90039">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dxTu4iFa2SWQWVaXBNJLynRRC0F87-gMcEAiWSGIkhaZK04dkjk1O-xfp8IQaWSmoNQitLZ2QA2ZhLhXiFU4c4ERvg74mhI3Go9EtItc_XUHdLyeqf7OVQ9DC_Ftcj_Z40RXxSY9qnSpanxb3I_K6exI-dR8CgW0mGQZpUyXuAAE_a4Ja8rapGU45JozfmCgTbE8INGiH5KBaWKCAz7MnEyxf6Y-0rXaNcxqnEdzlQySrFYNr640LlTDvoDVcm--llAbQK699vgFoNiLP_ILX2s5sxz4uk2fXoeGSAfD4Lfs9iUL7tKMarCWgsQLjnGFs_hkAPjX7ScsueGcftU6xQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇭🇷
لیست تیم ملی کرواسی برای جام جهانی 2026 و پنجمین حضور متوالی لوکا مودریچ در جام های جهانی
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.05K · <a href="https://t.me/Futball180TV/90039" target="_blank">📅 16:21 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-90038">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Z_ScWnH5O75kYVK3xzPKyfb6SHDpsnpg-d3ulp7VUz87ZTjrr5BUT1WmSrp6VsiBtwkZRerye2mIsAnx-Hmh2FVlBOKPKsaveqnIK2DKVyaY8y1uU_amV1XeIZWy2jSHAdcVh3xWqwoq7f0j7pq9RfBaoXApQ7xSx1gwhzMJi35syo-fvA-8v1cxZuYP7Wa5O5tY-XoAofPTVWS4eGd6qd1AMRY1LUjb_Ubgrwxbx3CvkuTm9_Kg-fjnwV2e0DLFiN1iCKmL8jwzi1mqGoDgtbPXgruHZEkzUUdTxz_umfx6gWUPPmLf0foulyEKTevr9AT2rnFToH5sCHi90ss65w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
رسمی: هانسی فلیک تا ۲۰۲۸ تمدید کرد
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 3.75K · <a href="https://t.me/Futball180TV/90038" target="_blank">📅 16:20 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-90037">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/UL3d2HI2c_-36TFwegKc4JIjYrtN2RL6uZitbL3HglHCGd7QEkSGqYOFYxCaM-2dciComO-cML9eAKtRat57xkp5Kg2C6V0zBKOMF714YpSzZGoAigZRo7mKOXv_0jVpgEgjkKImB9idbOx3CsKGEvXm-8MosFGo2twUkfPg5f1aiiSeP7Hf2YrIyKzjX_VAzWIvDtxEOBCXbmbloSfDsLDnzDxhwA9NoNg9k8PXz29knQWjh4D08LMo8BWRCw7Lm6pTG7b3trYkh1yIQ97tZNupXfUpDUT0GyophSbW9Dw6lboi7xioBBMSPL_rwYqvHtpDde1wrVtc6Vqvdu7ZmQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
رسمی: کارواخال از رئال مادرید خداحافظی کرد.
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 3.75K · <a href="https://t.me/Futball180TV/90037" target="_blank">📅 16:18 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-90036">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JOQNv24Hryc0b-5xKICmTcs_WCJXxoAUnS6jm25RTiWu4gLy8zjDbI2TFetiS_ZTAKCUEH-bycgZRN_zxMj7QANNS5iC3KcJnzk_pDXL5EprlXI7P0WbLSXfV7kL1rUtx44iJT1isgKdTNlpyU0dH3UWznDiw1hdLyqZ7DNWdJPTfZjWso3fhuALTCZXoHiiZH5rWXKR-RfbcVOWgyGONa1XXIlP7xk2eLdi-fRWbdFd-cbvE4P8AJe_RP4DGsANZBzAJq2Z8IrhM8znQgcv06hT3ZHM1FXLVbiinehQ6UhjqzP_luxvHIhQF7OcS1gG_9QHaiiynsQF4lb4DpGzqw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎁
هدایای ویژه و شگفت انگیز چیتابت
🎁
۵ درصد شارژ اضافه قطعی
⚽️
بونوس خوش آمد گویی ورزشی تا ۳۰۰ درصد
💹
صدرصد پاداش خوش آمد گویی انفجار و کراش
✅
ورود به سایت و دریافت هدایای ویژه
📱
@cheetabet</div>
<div class="tg-footer">👁️ 3.83K · <a href="https://t.me/Futball180TV/90036" target="_blank">📅 16:18 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-90035">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XlwQ9wN_SRAF5YoZPsu8WthLdZUdIkZrBPkYljD-SKHA5NHqEwE-k76_NoopI6O3J9vBHtP3510GnTtBZ_aasef9CQkYhTchz4icqoNSPU6DFaZi7Z14s7tKGqF4HZ6iLWJmfvMGPFqw3_t0ecJodnmS8pDV1xfuMgmiD8_4sVyMe4cTv2GKlCWhG_o1Jo6u4msf2uCW8lHi5QhKvIZJ0OdY5_fbebdg-aZOTePJCu-ywK77h8X7ra9PKdR-udWaAYLfb7OL3x9ZaUyy_RgtZiVaj6PvUB7xC2zXdNTwROftQsjDsoj5lJUPkMh3awkvLJfpOtDXKx44Zyry9fCWVQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
رکوردداران بیشترین بازی در تاریخ جام‌جهانی
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 3.95K · <a href="https://t.me/Futball180TV/90035" target="_blank">📅 14:14 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-90034">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8afcf96866.mp4?token=EbkS2y9s7g38bUlAkMeBJrv9OjxTAriOLheXLKAotZMt1Nbw9RTZVZkv1H65dHPaCMRHh2XjC99CZq9oY06Nmm0qouSgsMV-RduSILEnyoxFZdaAWejkPJFOjUJ547AsMAnYhhL-zjb9RLEHUOv3fYzD2Ens1zmveDTKWx3ZBlfqQIRkUa9HrdbZHH7eE0Vh1APk96kmr_eEJ4UxXk_w_X_Mz7rltSQbhOasg94jjHrRbZ_BOUvpAF_RU-LVGM-qwPE7oPPMrwb_MJSapEq30iE3vMo6dyVjFWP5Sw1LeIb-8J5-EIsWQFzIQ-HUy-XGmPR3yDBR-0tHhiUvTVy-JA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8afcf96866.mp4?token=EbkS2y9s7g38bUlAkMeBJrv9OjxTAriOLheXLKAotZMt1Nbw9RTZVZkv1H65dHPaCMRHh2XjC99CZq9oY06Nmm0qouSgsMV-RduSILEnyoxFZdaAWejkPJFOjUJ547AsMAnYhhL-zjb9RLEHUOv3fYzD2Ens1zmveDTKWx3ZBlfqQIRkUa9HrdbZHH7eE0Vh1APk96kmr_eEJ4UxXk_w_X_Mz7rltSQbhOasg94jjHrRbZ_BOUvpAF_RU-LVGM-qwPE7oPPMrwb_MJSapEq30iE3vMo6dyVjFWP5Sw1LeIb-8J5-EIsWQFzIQ-HUy-XGmPR3yDBR-0tHhiUvTVy-JA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👍
📍
Tehran
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 3.88K · <a href="https://t.me/Futball180TV/90034" target="_blank">📅 13:30 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-90033">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/r4hFBvN2cSGF3IRWCXEInhoKjBA2Qu_ChUKEbg9NA9v4YOwWIfXtC5a8sn2IkdJOF_Sj9gEJu4yMkN6enKz_Jvsdcw3PcYukLDZW-DJAGCkPkk7EqyAY3VKzb_V03nWZ-btHPDRlNAe5Rcd_BVg7tS14PYenoyCR5Jh6N6Ee4POM3JOoZtlbTm5nkta7QiYLPKNHGFcSSuDjqfg7T9qKqGL-oQhQf32QZpTkI1OsAox2ZTlkKq4BWu4mzIn-AMmJ9IJxCAuDJT-GeclboQ7-lMwnbvSshrrK0FuIulqiLLmGqFmlYqOHinOUQP2adejeIq2a-PsZd1rcsTB0D3peNw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👀
روبرت لواندوفسکی بعد از آخرین مسابقه‌ خود در ورزشگاه نیوکمپ، عکس نمادین اینیستا را بازسازی کرد.
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 3.66K · <a href="https://t.me/Futball180TV/90033" target="_blank">📅 13:14 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-90032">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">1xbet_ir.apk</div>
  <div class="tg-doc-extra">51.9 MB</div>
</div>
<a href="https://t.me/Futball180TV/90032" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🔥
ورژن جدید اپلیکیشن وان ایکس بت بدون نیاز به فیلترشکن برای گوشی های آندروید
🎁
اپلیکیشن رو دانلود کردید موقع ثبت‌نام، کد هدیه 1x_1566529 رو وارد کن و تا
100یورو
هدیه بگیر!</div>
<div class="tg-footer">👁️ 3.66K · <a href="https://t.me/Futball180TV/90032" target="_blank">📅 13:13 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-90031">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mP7JnVkHrEY7iVtzaFsmipIItzh3eDN5gdHPFR8IzFLJ-UwS2-Te1_Q57jTAvFniMIBWGZVVlLbcX_6YSjFLD4ZN18TqKXCRyI4y8VVcd0I_z3AHoX-SkHsCGn3tcCnQKDPCIGRhwCCTt4_RwbUGQh9I2FA6IBu_iA2_ZDW1Bzh9sjm07aRvJ3E4yqSxkTxJxF_nYqJtyiIhg7FywgiWuKpJUT8sentDt4uAM2wKLcnReHSaH206SQGa3z0qRZ4O1hcWglYnQRB5AjUVAPzs6uGNKzxWIN3lXULTXgWhe5P0lT8Rym_6_uprDLcwHY_Vs451d4Wpd5iHpHAHwBDNDA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بازی جذاب
🔵
بارسلونا - رئال بتیس
🔴
🔴
🔵
به Barça 1xFamily ملحق شو و با هر پیش بینی درآمد داشته باش!
🏆
فقط این جوایز رو ببین:
📱
آیفون 17 پرو مکس
🎮
پلی‌استیشن 5 پرو
💵
4,000€ نقد
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
<div class="tg-footer">👁️ 4.15K · <a href="https://t.me/Futball180TV/90031" target="_blank">📅 13:13 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-90030">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2c9bd4b703.mp4?token=qdzyvj1gwBYhw_iFOz2iQHFp-noYZSWqU0Q_aAlgYSlwSS6waYrJ4z1iRWiEDb2P0hw_IG3kq1J3O93GFCladSCmODSiJXvtL8bRT3bZgFd4Y922zVEqvgSvAIHnWXDbyueVxQmRUnonL6TOqJbx2PM5fOXKJyFpAx0muFWzoMGzLbsvUboBTjryMxci8vFZbZfugdWOVXxXAY6uWGEp_CrYPC4OXpWdoOKYqqoegDhM1Wb3YXNrxibLf0dmQyCem_80I5_92k-_V4p6dalGkZW13sDaiOg0T8rKYCfdWI-oQOzsZRrWY2er_9HzFfQQSzGfo3CDs8Ks9drOBDWdhw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2c9bd4b703.mp4?token=qdzyvj1gwBYhw_iFOz2iQHFp-noYZSWqU0Q_aAlgYSlwSS6waYrJ4z1iRWiEDb2P0hw_IG3kq1J3O93GFCladSCmODSiJXvtL8bRT3bZgFd4Y922zVEqvgSvAIHnWXDbyueVxQmRUnonL6TOqJbx2PM5fOXKJyFpAx0muFWzoMGzLbsvUboBTjryMxci8vFZbZfugdWOVXxXAY6uWGEp_CrYPC4OXpWdoOKYqqoegDhM1Wb3YXNrxibLf0dmQyCem_80I5_92k-_V4p6dalGkZW13sDaiOg0T8rKYCfdWI-oQOzsZRrWY2er_9HzFfQQSzGfo3CDs8Ks9drOBDWdhw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">استایل متفاوت جورجینا، همسر کریستیانو رونالدو، با موهای بلوند شده، در مهمانی جشنواره فیلم کن
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.28K · <a href="https://t.me/Futball180TV/90030" target="_blank">📅 11:47 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-90029">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PunxsqivyoShKJI4nGAzIRCn71n0gczOye5llgPFzG4hIF1mkB8dH0bPckqZg27J1V9wdln5o4TnEy8As317trs389LOhTBVCgEu-sopflC-lM5v4KX0WcsRKCZokygkb_NgHa628Ja4X3hb0LJAgAwurYPK6AcfPUH39L57X684PXMiWUNMg2_lGPhnljcB2GxSymc5UAdtQvAlnRmncxKIiFT6t5o0Ut2wd5fDSV7HFhlfUv_IQ-91NWesckmcUFBX-ikiMjO7ycWKPLa112VORL0E2gxl_YNB4xz9qPmYzIlj2eZSHbwDt23a3UoRIqzgcC7suI46eDHcljSJgw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⁉️
سرنوشت تورنمنت‌های رونالدو با النصر
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.64K · <a href="https://t.me/Futball180TV/90029" target="_blank">📅 09:35 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-90028">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/441c980280.mp4?token=huDcVsiFlsEe4JbL1EGDpCSt33Qqfq2AAy3REFNlFe1dfy96ZyPdULknU4iNcRaHWr4YQSvoWRAYCQs4uq0Hjsynr9-LESUDYsIiJ6E0hIefJRqsDNsPlHnyLAUIdc7B-n6uFlhyH2tE8lifh7yOlrFlCNIp40N3SjPEsU_9cIQAp2xLlADcw56vjnpJRj1X-auYwqnbafcVQ_4Sj40lIwUdKCL4Hun-w6k-4L5vWL33-lRkDt5s_iPYcUNk56g2OdKssLf38O9Ftaewm1SOW9q2KpO4Y19-V6_nk0SljFhuOr7_iw0FdgjsO3bG9diHpfYjj_GUHQBaQeHl0MRkgQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/441c980280.mp4?token=huDcVsiFlsEe4JbL1EGDpCSt33Qqfq2AAy3REFNlFe1dfy96ZyPdULknU4iNcRaHWr4YQSvoWRAYCQs4uq0Hjsynr9-LESUDYsIiJ6E0hIefJRqsDNsPlHnyLAUIdc7B-n6uFlhyH2tE8lifh7yOlrFlCNIp40N3SjPEsU_9cIQAp2xLlADcw56vjnpJRj1X-auYwqnbafcVQ_4Sj40lIwUdKCL4Hun-w6k-4L5vWL33-lRkDt5s_iPYcUNk56g2OdKssLf38O9Ftaewm1SOW9q2KpO4Y19-V6_nk0SljFhuOr7_iw0FdgjsO3bG9diHpfYjj_GUHQBaQeHl0MRkgQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🤯
جادوگری بامداد امروز لیونل‌مسی در آمریکا
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.81K · <a href="https://t.me/Futball180TV/90028" target="_blank">📅 07:41 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-90025">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nzmlDXanDhyvWbJ5SUKKxw9TzUBsbEZjmf_NO1iA16iepRQVp0cavXzNoMWfIjUisseXyehc6kGZnwQ8H9Yx6BJSGTraBNPDx_dKQPWq8c6cBy94uqNL9n-gtExAJOj3P_PZ0EnbKaKdX8G95wdkiiSnLgyBzb0bP9PkjccfvhpKAb0JiRPWsz1TxnT-dyF8A5N2oh9oH8_VfGdRdLRnbQPBRDJ4GlYH5CvTIH7QTRzus-1kj3STye1JETGqVK6yqaxS1DYC5kD2A760X9NI2NiYfwSUdBjtLi11J4aE7lwPC9_QMV3lACnbyWpkQBUI6r9k7TpJyqcjdVSBJ0izjA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🫪🫪🫪
🤯
برای فهم‌اینکه لیونل‌مسی چه اعجوبه‌ای هست کافیه بدونید که این بازیکن سال ۲۰۱۲ موفق به زدن ۹۱ گل شد و تیم وحشی هانسی‌فلیک پس از ۳۶ بازی لالیگا این فصل موفق به ثبت ۹۱ گل شده
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 5.09K · <a href="https://t.me/Futball180TV/90025" target="_blank">📅 19:27 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-90024">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1af6bf0b38.mp4?token=XYZolgjMe2XIKLwAkMyWf-UxK521DR04miOB6usyWsfx31nhedR6OmducADYx9mqpvqumkyY40uaF-2QL6NLjzAhYBH01xp-WusFouKXTReawVWLmwz1zeP6r-53GdVGVmtLqSOTY-fg9adfAPsSj25J_dvQN9oJFrRmDiGd_2SqmtrRnl__LhlzEW--6RyjWAkF8QXpb5Gwbf1JuBIDL8vHL3Rygycnn2RxJaYFbaHt-Cgss2XSLJR2yzR-12Owi47Mnvuwzk9Nv6x436EVgtg0pn5qF6K8mcEVcUeJeCRkrrT418-RBV1WFo2KTOqqjy0hLbhonVcRXUbOSx3SHg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1af6bf0b38.mp4?token=XYZolgjMe2XIKLwAkMyWf-UxK521DR04miOB6usyWsfx31nhedR6OmducADYx9mqpvqumkyY40uaF-2QL6NLjzAhYBH01xp-WusFouKXTReawVWLmwz1zeP6r-53GdVGVmtLqSOTY-fg9adfAPsSj25J_dvQN9oJFrRmDiGd_2SqmtrRnl__LhlzEW--6RyjWAkF8QXpb5Gwbf1JuBIDL8vHL3Rygycnn2RxJaYFbaHt-Cgss2XSLJR2yzR-12Owi47Mnvuwzk9Nv6x436EVgtg0pn5qF6K8mcEVcUeJeCRkrrT418-RBV1WFo2KTOqqjy0hLbhonVcRXUbOSx3SHg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👋🏻
پایان عصر کاسمیرو در منچستریونایتد
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 5.23K · <a href="https://t.me/Futball180TV/90024" target="_blank">📅 17:35 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-90023">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/109fc9f803.mp4?token=gN7Gxvzt5V5nqTtSFQHKii8si9AdzNutHBoH_w3nxDcTYEhIUH3-bq1w716AqrAhgT9rKiIyXomEc_qZX-SL_tHIzMEtKImwXnCIJ91HBojk0w0dSMES_kDMcVHezNjBdtNVyNwmfWKe5NxNVsIHCe7CZ26bDmyBHOW-krOdu0vhWe4Cf1Cgbyp7QXVZm0_cNeC3PfTnwa_B4yoKOfYdjvHTXZ9g25O2TtO9x03PrAUblfhnzNwIG-yijtcJJKRbi1Hr_6Hb4_LLjFYm6RCkjO7L8Syg8NNHRW7frizc7BhvTJLK209jLCcnQq9PEk1cLrocNdi7ucRVDMbS_N0phQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/109fc9f803.mp4?token=gN7Gxvzt5V5nqTtSFQHKii8si9AdzNutHBoH_w3nxDcTYEhIUH3-bq1w716AqrAhgT9rKiIyXomEc_qZX-SL_tHIzMEtKImwXnCIJ91HBojk0w0dSMES_kDMcVHezNjBdtNVyNwmfWKe5NxNVsIHCe7CZ26bDmyBHOW-krOdu0vhWe4Cf1Cgbyp7QXVZm0_cNeC3PfTnwa_B4yoKOfYdjvHTXZ9g25O2TtO9x03PrAUblfhnzNwIG-yijtcJJKRbi1Hr_6Hb4_LLjFYm6RCkjO7L8Syg8NNHRW7frizc7BhvTJLK209jLCcnQq9PEk1cLrocNdi7ucRVDMbS_N0phQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">◀️
لحظه شکسته شدن رکورد دوضرب دسته ۱۱۰+ کیلوگرم دنیا توسط علیرضا یوسفی با مهار وزنه ۲۶۱ کیلوگرمی
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 5.13K · <a href="https://t.me/Futball180TV/90023" target="_blank">📅 16:46 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-90022">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">🚨
جزئیاتی از درخواست‌های آمریکا از
جمهوری اسلامی
عدم پرداخت هرگونه غرامت و خسارت از سوی آمریکا
خروج و تحویل ۴۰۰ کیلوگرم اورانیوم از ایران به آمریکا
فعال ماندن تنها یک مجموعه از تأسیسات هسته‌ای ایران
عدم پرداخت حتی ۲۵ درصد از دارایی‌های بلوکه‌شدهٔ ایران
منوط‌شدن توقف جنگ در همه ساحتها به انجام مذاکره
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 5.42K · <a href="https://t.me/Futball180TV/90022" target="_blank">📅 12:54 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-90021">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/J4PUbtM5wKvtwrObPyXOV4XDRkXK5XZw0c8sUeW8MaCRIjAmzcezKNveik1zOhCjDgltsRS8AzzzcCT1i5R7jdYg-Pkf0Dha2KzML6GBtk0nPoeY4HLzZkvfn4vW-8LB3zp8b8O21XLwd0WAJI7OZkqv8c5HBsBbQToOxJ2cNKfMGjrDIo_YPxqFWHgh81NBy8MR5DSJlbOC31nu8-K4VDshSCdKrNQkfEmDFOl-oAySr-q2VhSWqv0kvEEQu6EW3Pw-qss1pMYT9bwr9TUukmbbcT8C_fPoqu8rNwVLOLqSLIEvParIBYSeh9QKcjOWsqAlURWmtT7Lx_9TWQuj4w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👤
لیونل‌مسی از سال ۲۰۲۱ کسب ۱۱ جام
👤
کریس‌رونالدو از سال ۲۰۲۱ کسب ۲ جام
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 5.15K · <a href="https://t.me/Futball180TV/90021" target="_blank">📅 12:52 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-90018">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">🚨
ژابی‌آلونسو: ما می‌خواهیم تیمی بسازیم که قادر باشد به طور مداوم در بالاترین سطح رقابت کند و برای کسب عناوین بجنگد. چلسی یکی از بزرگ‌ترین باشگاه‌های فوتبال جهان است و من بسیار مفتخرم که سرمربی این باشگاه بزرگ شوم.
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.65K · <a href="https://t.me/Futball180TV/90018" target="_blank">📅 11:50 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-90017">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tTW78y4W9SFRuwnMrNOC4vJubbqrQ2yRMPrsDNd7I_HaYQhtjrjjJVS90wTzxLKnMLIL1wrziQEOv55SM-2l-K5-QrmqGFVWuYBxPLskTmCRnuZ4J3ldF9Rl1vw8zuj2wAr3biPLuOlFLNmbioKGhpnMqsDqQ8RkKs1mN74RcvQZki2_RBGzIoX6TPsAQYLeS4XWVbXjpyOXvMFDGgqnR2hBRVEMmgiRmwx-6w1TdeaLDuIzVKveRVa12B2ELMLf63BfmX3tcTGKTflKoEHMaZIxesQ1BYrMbUhXjuf7OsOE63OBP5648bYaFekYu-TL0OhR17dN8fqbOvWo3uK_Yg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
ژابی‌آلونسو: ما می‌خواهیم تیمی بسازیم که قادر باشد به طور مداوم در بالاترین سطح رقابت کند و برای کسب عناوین بجنگد. چلسی یکی از بزرگ‌ترین باشگاه‌های فوتبال جهان است و من بسیار مفتخرم که سرمربی این باشگاه بزرگ شوم.
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.89K · <a href="https://t.me/Futball180TV/90017" target="_blank">📅 11:46 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-90016">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eAJeFv2pjaACVMBIpcIsoZajUG7hxLYIdHE3veVCAYraKevpG5-fBzIUuDDipenxcCVvM-PE4z0NzBtaM96HwwL6_QsTg7HMx287gb7S19hBGgemuzVCt6KEVWL8I2FE7fbhv51NXtbmFsuGwq5e6id-Sb1fxfb-vyB-b9g-R8nZXrptdDVJjlbWIsHFmGsXwILb1jKJg7JAPURgugSNIctyIFXg1tHBdsG2eOY-vlt4kTNrpgSu7zD46buZ8zdFg8UwfFS9Fv-YkwFsAlWdR2bUVZ9NVai9kc411Bvjd_zNJbX0M4ucYzgt_5srQ6Z4HFbdzPOvsH8vfMyPthP1Fw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
🚨
#رسمی
؛ ژابی‌آلونسو با قراردادی چهارساله سرمربی تیم‌فوتبال چلسی شد
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.74K · <a href="https://t.me/Futball180TV/90016" target="_blank">📅 11:45 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-90015">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">❌
⚽️
تیم‌فوتبال البطائح به سرمربیگری فرهاد مجیدی در لیگ‌‌برتر امارات به لیگ‌دسته‌یک سقوط کرد
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.48K · <a href="https://t.me/Futball180TV/90015" target="_blank">📅 11:30 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-90014">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/553b8556ba.mp4?token=L_BahZgHQQLvvlytD87BSIkjR6Bmp3VJi4a0p2wA-iAP3CnP8wCv868Wrk0_aVHSanBsHrn1TsWW6TUtWpqWFek0jBfBmicmk37-ixHNE0xYGPVZGRCZsSVHQc45lNZFbJXioJe8F2o6q2ZdMoSAAXr8T37kC67KJKeWvoWQnQ9tqXCVzdBCFlMjJlPSiakg5x-qrSOBHHcF_ERON0Kra0AtmYFzh__Tq9gMjpguOn-92MrI7t6TVP9HmRa3JXBjT3wVxXrgMupDUjkMI94amZs-0s5BFFnXWKBNiWMvelJiJSaNfB1IR1HlVVnQmiRACswW7e0s_AUPEt77cK80Bg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/553b8556ba.mp4?token=L_BahZgHQQLvvlytD87BSIkjR6Bmp3VJi4a0p2wA-iAP3CnP8wCv868Wrk0_aVHSanBsHrn1TsWW6TUtWpqWFek0jBfBmicmk37-ixHNE0xYGPVZGRCZsSVHQc45lNZFbJXioJe8F2o6q2ZdMoSAAXr8T37kC67KJKeWvoWQnQ9tqXCVzdBCFlMjJlPSiakg5x-qrSOBHHcF_ERON0Kra0AtmYFzh__Tq9gMjpguOn-92MrI7t6TVP9HmRa3JXBjT3wVxXrgMupDUjkMI94amZs-0s5BFFnXWKBNiWMvelJiJSaNfB1IR1HlVVnQmiRACswW7e0s_AUPEt77cK80Bg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❗️
علیرضا بیرانوند: سرود جمهوری اسلامی رو با صدای بلند میخونم و مخالفا هم هیچ کاری نمیتونن بکنن.
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.82K · <a href="https://t.me/Futball180TV/90014" target="_blank">📅 10:27 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-90013">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c75de85542.mp4?token=bb1SscTNuZ1hflp9QyeyJ7Hx9BK3YmefQ-OlEFYhBkRMxJLoi_Js92A45JPMSvg8jPL-6BhmR37B7pmzzj5XxrnvqZo76zcYEA0i5pmHPNSSUKAmIoHJ8VD3O0NEFIGVA0siM-S9BXqLSQX3bMKZPmaXAQ4g7lwnKHlO0YyqbQThLvI-xuNhTvkYIb2Pcka6U0t1-RdaOgzX8ybrEp9enl9e03M9V3ieye9ijLX8YIBG-9iVAxzJyj5mrbGajYDC5l94hM983e5VP0K0BQ43Sn40ITUlHm8w_YKprwfYHctxCeRleVPpHxXof4B3LP9Y70cIr8Won47__dcL4qB2TGI61UgEsH8qjIY9eA4-uL9yLeBzPr5vAFMsCgEBfJ2E36s5abUUq5cXELh4705i5kkQR2_O4nIZnCjDofu78jDq4Y0TO0OC3fZVtsk0jBt6iFdyLv2DZ9vzKh8SoYalvu0MyQCcUv19iJctPeuim7fI4kBECAv9r_OLcNEIjGypFyTVsO3_h4EHoVhcGZM22POqM4ei0Bt5kzdNdCj4uHhzqiURFv1PPMBVBjGk1Igbzae6trV8J2CK_QnzcEPkkTwRJDdnHGf9ZgBIa5w3tE9_VLPAkb-zZiaS3S9RVtStfHRW5sPX4Wi-U5MzJ77K2wL5rIbYWnMRJh8gXGnaUE4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c75de85542.mp4?token=bb1SscTNuZ1hflp9QyeyJ7Hx9BK3YmefQ-OlEFYhBkRMxJLoi_Js92A45JPMSvg8jPL-6BhmR37B7pmzzj5XxrnvqZo76zcYEA0i5pmHPNSSUKAmIoHJ8VD3O0NEFIGVA0siM-S9BXqLSQX3bMKZPmaXAQ4g7lwnKHlO0YyqbQThLvI-xuNhTvkYIb2Pcka6U0t1-RdaOgzX8ybrEp9enl9e03M9V3ieye9ijLX8YIBG-9iVAxzJyj5mrbGajYDC5l94hM983e5VP0K0BQ43Sn40ITUlHm8w_YKprwfYHctxCeRleVPpHxXof4B3LP9Y70cIr8Won47__dcL4qB2TGI61UgEsH8qjIY9eA4-uL9yLeBzPr5vAFMsCgEBfJ2E36s5abUUq5cXELh4705i5kkQR2_O4nIZnCjDofu78jDq4Y0TO0OC3fZVtsk0jBt6iFdyLv2DZ9vzKh8SoYalvu0MyQCcUv19iJctPeuim7fI4kBECAv9r_OLcNEIjGypFyTVsO3_h4EHoVhcGZM22POqM4ei0Bt5kzdNdCj4uHhzqiURFv1PPMBVBjGk1Igbzae6trV8J2CK_QnzcEPkkTwRJDdnHGf9ZgBIa5w3tE9_VLPAkb-zZiaS3S9RVtStfHRW5sPX4Wi-U5MzJ77K2wL5rIbYWnMRJh8gXGnaUE4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
عملکرد رونالدو در بازی دیشب النصر
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 5.05K · <a href="https://t.me/Futball180TV/90013" target="_blank">📅 09:34 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-90012">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FMahp-CupOvBCTFK_dtl6a1tCX57taR8uDqc1vrvhmZrK2yzs_XVIG-IWFmVnMC_0NSOEOSTP9c6a6hIf--06cAlUczzavaVq2TBOMptQm8c1zYwAJHPOgXA7KbV1hB311NBii8QcriAetS0iS5k_ewbKyCKBfKRSCVZpxWXZ_uvP6KLIud75fMuPUGrgYl5pS0wztUZHlshMQ0rZ1hHhGwHYnONHB6YCIpk_fAT3WJofla4trkMwgP9qhnLWevJrA-FTfUBmB_JtriNNSQqYb0fKFFwmMT2fSBprwdF6OJBfwJuOS_D7Ri0km_0mh0n3a55cb5pyLPWg7UUzBnu9g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">واکنش رضا غندی‌پور به عدم دعوتش به اردو تیم ملی
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.84K · <a href="https://t.me/Futball180TV/90012" target="_blank">📅 09:12 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-90009">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6d4fe02d07.mp4?token=UGlKFY7f1Ytc8juzfZss_Zfef5MK8CrjgqyCBu6QZrKb2O98elzFAkiXY90NdBrzeE-cYAY7nW3hye3mZpvuyFaXrNEnigfCxi5BjNgjXXtToYqOTrtquZZ_20ViQcdWlViqUMppIgKTcTBc-NR8JObU8geJdpFMVngD9XAuFz57Du9FaJILeptB5PrllBYmGxov29nkw4MX7maBMIAbCRTkYh20ZhT6NRlmI_N3ueLXx7Gr3WPnYuAOD6u7_RW5zUu1elfdHJhUG5ZtoIi6C8WzZG_AjWfbJRPFYXS9AntbRCdAPorWvHcGlr7Yvk046wlkG8P0AA6oW9TWsP6EQg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6d4fe02d07.mp4?token=UGlKFY7f1Ytc8juzfZss_Zfef5MK8CrjgqyCBu6QZrKb2O98elzFAkiXY90NdBrzeE-cYAY7nW3hye3mZpvuyFaXrNEnigfCxi5BjNgjXXtToYqOTrtquZZ_20ViQcdWlViqUMppIgKTcTBc-NR8JObU8geJdpFMVngD9XAuFz57Du9FaJILeptB5PrllBYmGxov29nkw4MX7maBMIAbCRTkYh20ZhT6NRlmI_N3ueLXx7Gr3WPnYuAOD6u7_RW5zUu1elfdHJhUG5ZtoIi6C8WzZG_AjWfbJRPFYXS9AntbRCdAPorWvHcGlr7Yvk046wlkG8P0AA6oW9TWsP6EQg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اوضاع اصلا به نفع رونالدو پیش نمیره.
🙁
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.93K · <a href="https://t.me/Futball180TV/90009" target="_blank">📅 00:44 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-90008">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/b37QLhqDUE87g_7T7tGHHtPNZ0PyOvP7Y-EyQpC7lb63u_GOTKDzAu38YCOWkQMdzmN83Uc-bUwKnoF9BBLYtV6b-MxP1GOig0Mr0Ts5-rm_Xio2litxiDS0sK0A_cNRWZijeted8m23AK_X07oeeTjtgp0Cwqb9hLT4gebDTI99yzbtL9r0rwiR7k6WGew8A1OU64uDuX5G9nYQLC_IK21ZDpR__IHoqVDhZi6UOakiTdByu_S7h6gvqUHtfIFnj6q58sooyrbHM0jL3pwVlilOWMF5RnA_EnkD6gVoTX7gpeNC7u_Is8Upxe3cu-20hX6a4d2wLN83nuewAafq9w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇺🇸
توییت‌جدید ترامپ: آرامش قبل از توفان
!
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 5.2K · <a href="https://t.me/Futball180TV/90008" target="_blank">📅 23:40 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-90007">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RxD67iVkImfj4dkLtkNETMEogtzsczpTwFayBfnbUlavw6BR7mFBPUhxLQ0yMyCRRhPrSZw_sZCgYW2RBuGIhuzifiNYGvOvU8v7Ejzjxy2iFHy9qiDK6Ox3rQgg_hzHfmHRy76Q9hpnAlZJ8sVqlqzDMwzpeczBr2fBu0rrw0MLqgPaN3gsQNwuvCBnaqvmRUPZjkSlbM_f_yiZcOl2SjgAWXZ7Oyc89L1-Q-BfOoaCSX-vqC22jErJP8Nc6I7TqTih_faTQggx1Ai_oGL4ipkoWpjeVH2HQ80WgtiiKhLlq-Oh4DStqgZ9MagKHFIAi-eBiixXMMNiOmhIWrAAhQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
❌
🔵
النصر در فینال لیگ‌قهرمانان سطح دو آسیا مقابل گامبا‌اوزاکا شکست خورد و رونالدو بازهم نتونست با این تیم قهرمان بشه
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 5.08K · <a href="https://t.me/Futball180TV/90007" target="_blank">📅 23:22 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-90006">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BMqu9xUvpXBOgjrHMQmwWTAO0wAxLpbbvbUAfbhaXnNMhzv4Yja9REw9jnQYjhJTpkf6MPQVSCJIdb-xTOglX4-UBlnl1sJ4u8dSeGNrxg0vQDFr3frhu0gwYfYQ3UtP6uj6yd338BxFca60XUKQoHbPyaebd3gGIKzZtdV2mMtsg6x8x5qCuY45vT86Hckgx_OFUei3uelvzK2uuOAvXVm9RjJEuKRD5iLibLs2as1dnlU8zzOnbny0XSwLbqftlwQideRqZ59ODTCrb_at18CfGRoM_1lwRPb_YuxvttxbYk3b1tZ5_GTmWwkqowBSFml6Rt0jxqKlD8XMRnzOZw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
به نقل از منابع انگلیسی، توافق‌اولیه چلسی و ژابی‌آلونسو حاصل شده است. قرارداد این سرمربی دوساله است
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.95K · <a href="https://t.me/Futball180TV/90006" target="_blank">📅 21:05 · 26 Ordibehesht 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>

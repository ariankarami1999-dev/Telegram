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
<img src="https://cdn4.telesco.pe/file/CGvn32ygBpzMVJUiNGt3bd1yWe5_UnTBWu2THQEO5JA3ljS1wqXVpRbbNF7uHzRf4mReuSBzcKqk--P32L6XAGxWcYzyCfV3kWp5JzXYbczCHFMIjIadyou9NEFGqXHhaaTSmiGtoFkzEsIBP1zI3xWdNxUzUrrv_Ybe9OY7JY5bxudMwCgxUtENMaJgqL-T4xW8TF7eGq3VrcFkmiHzohQvmlaS36-sKP3og545z7nrFIiJYdA9vjsqltD-LLIZfSV0ydIUMadOPFXdz2MVEcObtfZZ5EBvvjbylv0fxve9_Q39o8EJIgxIk_F-tpJ6pgjrVIGGUZQE2pnH47gIlw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 🚩سرخ تایمز🚩</h1>
<p>@sorkhtimes • 👥 21.5K عضو</p>
<a href="https://t.me/sorkhtimes" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ﷽ورزشی نویس پرسپولیس👤🎗️«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس.⛔رسانه سرخ تایمز مسئولیتی در قبال تبلیغات ندارد.</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-07 07:44:06</div>
<hr>

<div class="tg-post" id="msg-139139">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AZ_b3DFBnQ3lRPnAhZmwf9vjVdbOL2hvrrlgqit0R56F43nfjBsxKPNR931qwjuNsGagAtZCB8zZudKlDUZXiIuzdbkN9JnY2Cm0m4jxaJPrFYaWNKLxgEuN7p3euKIoaGOIm-CyN3fGz5Mh-79KRntA8SWJFzRb4bPrCEya2bUdUrE9TwdRTT9Jk-HnkmLr1D7PObMA4tuha80CBOEfGha7qKCXm-pAK2NUKRc86dHeLzIF7FLUklR6cWuMdWtKJ04TXlhzKycXNeP9KNDHtP6jjVsazdB8zYKamyqIYxsJt1EeqSwl2oQV1XALr9tmm9c2tt_lAGsEgdBs0cvR3g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
ورود به اسپورت‌نود؛ ساده‌تر از همیشه!
🔗
دنبال یه راه سریع و بدون دردسر برای ورود به اسپورت‌نود هستی؟
🔵
با مینی‌اپ ربات رسمی اسپورت‌نود، مسیر دسترسی ساده و یکپارچه شده؛ بدون لینک‌های متعدد و مراحل اضافی، مستقیماً وارد محیط کاربری شو و از امکانات سایت استفاده کن.
🔗
ربات رسمی اسپورت‌نود:
👇
🔵
@Sportnavad_bot
🔵
@Sportnavad_bot
🔗
کانال رسمی اسپورت‌نود:
👇
🔵
@Sportnavad</div>
<div class="tg-footer">👁️ 1.78K · <a href="https://t.me/SorkhTimes/139139" target="_blank">📅 02:24 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139138">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/241731bcb2.mp4?token=qmPsaYKMYhZ8jDHIkHfP-AWQYqM4vBBCZnnveEWOwmjfa0XSvSqK1OGy8p4ntxZOPJ9BFG9-ZzMi3zs4bGdUwvuMv2tj7tBaaombnivPJYZ01aaJYeAoBv8zkLwq4N-2VX2FdH3bjSOvgsl6alTe6mYRtmxtDuc3PZgWhOSZaba_Bo8DGutRhqydSRydGdYyrMvpwRktC25Z16cKJxPWwKIC-ZHmvhBKrEvrWVX4OJ3wXRLO3c4qckAt-zjpPmJHLLm3E4oZwjuEse16EEplwfk3gluq-XbbO4sNzbaRKfZnb0Rl7HvsTV23xWmNFjv7pPIfeuXNM7b-YW7LAAHnQDTCkwnvS4IcAEArTRliVZCiH3z5nWjIchwLr5hmaJW6W_WyA4AXlZ3IsMEKG80hrYoleJFCgNOVzrA5tvh28ggj5tor4UrKSLEgiPqUwMZRSLwnf1vLoRucFjWY1zA3LjxkIoimjY95qGlwsP30e5QjTd-84DDsjO-L2TBa2bj98JUX8vlSlBfws6e3nvc5W3gbzmFxHcIz-i341QyI84idSqky29vqYHWGTRQ37e58KsxxvWXRwxlKHQiiH0IlvkhMUKoZ18Ust-UorHpe2zVcvor4gTqWs3DwGFQqKEWaXp6btzLUGS6jKcmS_hjehDHAWqJCfPKDKSDHevu8Mpk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/241731bcb2.mp4?token=qmPsaYKMYhZ8jDHIkHfP-AWQYqM4vBBCZnnveEWOwmjfa0XSvSqK1OGy8p4ntxZOPJ9BFG9-ZzMi3zs4bGdUwvuMv2tj7tBaaombnivPJYZ01aaJYeAoBv8zkLwq4N-2VX2FdH3bjSOvgsl6alTe6mYRtmxtDuc3PZgWhOSZaba_Bo8DGutRhqydSRydGdYyrMvpwRktC25Z16cKJxPWwKIC-ZHmvhBKrEvrWVX4OJ3wXRLO3c4qckAt-zjpPmJHLLm3E4oZwjuEse16EEplwfk3gluq-XbbO4sNzbaRKfZnb0Rl7HvsTV23xWmNFjv7pPIfeuXNM7b-YW7LAAHnQDTCkwnvS4IcAEArTRliVZCiH3z5nWjIchwLr5hmaJW6W_WyA4AXlZ3IsMEKG80hrYoleJFCgNOVzrA5tvh28ggj5tor4UrKSLEgiPqUwMZRSLwnf1vLoRucFjWY1zA3LjxkIoimjY95qGlwsP30e5QjTd-84DDsjO-L2TBa2bj98JUX8vlSlBfws6e3nvc5W3gbzmFxHcIz-i341QyI84idSqky29vqYHWGTRQ37e58KsxxvWXRwxlKHQiiH0IlvkhMUKoZ18Ust-UorHpe2zVcvor4gTqWs3DwGFQqKEWaXp6btzLUGS6jKcmS_hjehDHAWqJCfPKDKSDHevu8Mpk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">#منهای_پرسپولیس
👤
فراز فاطمی سرپرست چادرملو:
❌
آقای حیدری فکر کرده ما خریم. قشنگ بگید میخواید یه تیم ببازه دیگه اینجور قضاوت کردن بخاطر چیه. امیرحسین حسین‌زاده با تکلی که زد دوبار باید اخراج میشد ولی حتی صحنه به وار
هم نرفت
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 2.93K · <a href="https://t.me/SorkhTimes/139138" target="_blank">📅 01:20 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139137">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">✔️
✔️
براساس‌صحبت‌های‌مهدی‌تارتار؛ سرگیف از بازی فردا مقابل ملوان به ترکیب سرخ‌ها برمیگرده و تارتار میخواد زوج علیپور - سرگیف استفاده کنه اما اوستون اورونوف همچنان نیمکت نشین خواهد بود.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.39K · <a href="https://t.me/SorkhTimes/139137" target="_blank">📅 00:57 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139136">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">❌
❌
استقلال فولاد مساوی تموم شد.کیسه خیلی خسته و کوفته شد و واسه دربی قانونا خسته میاد تیمش امیدوارم استفاده کنیم   «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.92K · <a href="https://t.me/SorkhTimes/139136" target="_blank">📅 00:29 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139135">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">🚨
🚨
کشاله‌درد دوباره شجاع خلیل‌زاده در بازی امشب مقابل هواداران یزدی
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.21K · <a href="https://t.me/SorkhTimes/139135" target="_blank">📅 00:15 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139134">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">🚨
🚨
کشاله‌درد دوباره شجاع خلیل‌زاده در بازی امشب مقابل هواداران یزدی
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.24K · <a href="https://t.me/SorkhTimes/139134" target="_blank">📅 00:13 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139133">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/32fe7cb793.mp4?token=nX66md2mEsmMa0jgqaT4Hnvrv8fsOUNr8fP8Q6-4HDVJmCrG22bVdT-DvFpuZcLmkuFTgAUF-VKLACIBTGjRu9VIqsp69yby5PankxYxTH6fghEWGdQqmEUn99RoBXdQXJeuMOFG2bu51AvjvrJq2KpTmJszmQCkDQcZ0EMF9qyixFZSE5VUEddEcPZqSlSAKXxzzDcB6tlQmUQYFgEL4yb_tDgUrdlSzJBdf48T3GRv7Ggi8NMTKlQA4VtySNjULSTHwmY2qYB8usmwlu5vYozrMMEe5j6zvvixN98OzxGHBhcg3WrNtRcPkn-QFS6nsnV0XgS4PSvCxzMIyueWPg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/32fe7cb793.mp4?token=nX66md2mEsmMa0jgqaT4Hnvrv8fsOUNr8fP8Q6-4HDVJmCrG22bVdT-DvFpuZcLmkuFTgAUF-VKLACIBTGjRu9VIqsp69yby5PankxYxTH6fghEWGdQqmEUn99RoBXdQXJeuMOFG2bu51AvjvrJq2KpTmJszmQCkDQcZ0EMF9qyixFZSE5VUEddEcPZqSlSAKXxzzDcB6tlQmUQYFgEL4yb_tDgUrdlSzJBdf48T3GRv7Ggi8NMTKlQA4VtySNjULSTHwmY2qYB8usmwlu5vYozrMMEe5j6zvvixN98OzxGHBhcg3WrNtRcPkn-QFS6nsnV0XgS4PSvCxzMIyueWPg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
کشاله‌درد دوباره شجاع خلیل‌زاده در بازی امشب مقابل هواداران
یزدی
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.19K · <a href="https://t.me/SorkhTimes/139133" target="_blank">📅 00:13 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139132">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/867c2d8104.mp4?token=YT2W3kdDVbTARlzJdUMoEv0H27F7Tdz2vpPtmLiz_uIXzHsnuhMLD4HWvOeSldWIi7oWAd9eihYvyJ8fmoaqEwEYh73jT45dvDWmG23Exd65jlKMCEPJRPwB_xiYdpu_iN4CGkv3iOrFySM7ZwqMkyu6-r6w8GI9wj5IQEAAjDzuI-nmcSP88Cx9xGOxLK1lxQOUb4My1DCqYWkmzbty1rF177I0wBx2QRKQwT31t0J6OKeitH7ihScLrnggeuYNP0tWhg3rnSeTi0h7gNfYdL8Da5yhMKK2Jlacb7-paxs4w5z_ig_C9vwxCxFqzyXB3cUlM2FdCURfceq94BttIUiNeiiN-6zl4Hy77fcVv5tud0L4YVXHKm6aVFAsFbsYmUTlu30_ZgJh-kZ5zD87ouLGg4mXO6QItjGvBrURn5kDRiL7K28vX7uS-A4b2bahnqJ6bqqHoQGaV9oODXyKEjOVSGxvSOIlLsCmLk8FwSsI9BemIgvTdlk4L9wLgrGeYLGJOCauvToN_a5iEB3uXKiPWA5547eD6H8H8NbEqas0zGf1WCqF9YMgjjJOejA5mayXyYugruor9W1b7P43yG0JMKkmy-NFdYhF_qdxp6VWTh4ax0W8jv_e31LPCq3m_235r4FQrIcDBsvQnIAOqRyHyM6EgE59Ex27zTXDht8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/867c2d8104.mp4?token=YT2W3kdDVbTARlzJdUMoEv0H27F7Tdz2vpPtmLiz_uIXzHsnuhMLD4HWvOeSldWIi7oWAd9eihYvyJ8fmoaqEwEYh73jT45dvDWmG23Exd65jlKMCEPJRPwB_xiYdpu_iN4CGkv3iOrFySM7ZwqMkyu6-r6w8GI9wj5IQEAAjDzuI-nmcSP88Cx9xGOxLK1lxQOUb4My1DCqYWkmzbty1rF177I0wBx2QRKQwT31t0J6OKeitH7ihScLrnggeuYNP0tWhg3rnSeTi0h7gNfYdL8Da5yhMKK2Jlacb7-paxs4w5z_ig_C9vwxCxFqzyXB3cUlM2FdCURfceq94BttIUiNeiiN-6zl4Hy77fcVv5tud0L4YVXHKm6aVFAsFbsYmUTlu30_ZgJh-kZ5zD87ouLGg4mXO6QItjGvBrURn5kDRiL7K28vX7uS-A4b2bahnqJ6bqqHoQGaV9oODXyKEjOVSGxvSOIlLsCmLk8FwSsI9BemIgvTdlk4L9wLgrGeYLGJOCauvToN_a5iEB3uXKiPWA5547eD6H8H8NbEqas0zGf1WCqF9YMgjjJOejA5mayXyYugruor9W1b7P43yG0JMKkmy-NFdYhF_qdxp6VWTh4ax0W8jv_e31LPCq3m_235r4FQrIcDBsvQnIAOqRyHyM6EgE59Ex27zTXDht8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎤
بخش دوم صحبت های تند خداداد عزیزی
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.28K · <a href="https://t.me/SorkhTimes/139132" target="_blank">📅 23:59 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139131">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">🎙
درگیری شدید خداداد با خبرنگاران یزدی
!
پ.ن باز شروع شد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.26K · <a href="https://t.me/SorkhTimes/139131" target="_blank">📅 23:58 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139130">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">✔️
✔️
✔️
منهای ورزش :همراه اول تو جدیدترین شاهکارش، سقف مصرف بسته اینترنت ۷ روزه «نامحدود» شبانه رو از ۱۰۰ گیگ رسونده به ۲۰ گیگ!
✔️
اینترنت نامحدود تو ایران = ۲۰ گیگابایت!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.31K · <a href="https://t.me/SorkhTimes/139130" target="_blank">📅 23:53 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139129">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">❌
سپاهان از استقلال شکایت می‌کند
❌
❌
باشگاه سپاهان به دلیل استفاده از یاسر آسانی در دیدار مقابل استقلال از آبی‌های تهران شکایت خواهد کرد.
❌
❌
این در حالی است که چند روز قبل سخنگوی سازمان لیگ استفاده استقلال از یاسر آسانی را قانونی دانسته بود.
🎗️
«سرخ تایمز» دریچه…</div>
<div class="tg-footer">👁️ 4.57K · <a href="https://t.me/SorkhTimes/139129" target="_blank">📅 23:39 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139128">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">✔️
✔️
گل‌گهر از سپاهان به خاطر کسری شکایت کرد   «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.53K · <a href="https://t.me/SorkhTimes/139128" target="_blank">📅 23:36 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139127">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">📷
جدول لیگ برتر پس از پایان روز اول از هفته چهارم  «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.6K · <a href="https://t.me/SorkhTimes/139127" target="_blank">📅 23:31 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139126">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qyJ1Sk0Z9TbBc9Myh-5YE1jtcrD9m_hT-7NRU8XHvtXg_DB9c8KWL44ExolbADWQG3-xg1Wr9845TviD8KvdtnSOTLQNPIz9Qn47UMmclSjxAWu0gAuvnMyfX98g6ERDiVU9jwaRTYGUNteBJv9YSV8wWHB2D3s3bNjR0F2yCSa0kyf5rkubzlb1TtGUTh9R7K9b6U83_qYioj5YRGZJXuOIbiT48AhiTZ9mKAcdRGCwiD8Rr88szpxd6-ipxExCzbYnj3OvaTgYmVA86AaW-D3_qDGHOwwVDYstwTfKD0UvH1PFyIYHkRWTkR3g5kReWnjzW3J5quE9Nnf1FxXsjQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📷
جدول لیگ برتر پس از پایان روز اول از هفته چهارم
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.59K · <a href="https://t.me/SorkhTimes/139126" target="_blank">📅 23:29 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139125">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QfGjkzPwE4jrZgz-3QllHFv-T-Y3cChQn1V1t88EiMdsY2DXbZ08ru3bwe7MzH1-FJOsnmhsnZLJmeOvz7fOdAamL6SJmX8nHLYAV_neh6kxiCCepK7Af5unGxLNOf59WeqUYrQJi-zsl9Wme752VbWSkxu8GGkzWpxJWzlCe9ZPHzPdXp5duUzv8A7JJ7-PKCXIcXAzhHok3BPo4-7TP7nWLca_Sk29y7a7a0RZoeEPBB_Y9GBGiImQzo987-zPCM_Xb8MTvLLRpYNiEXOeCZO00B6wNmQYsMEoaOxZC161RzowWK3Coq0CEY-unMW0oisVuMa_F4hXr_jke83bfA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
شرکت یوسف جامه اسپانسر جدید پرسپولیس شد و قراره ۵۵۰ میلیارد تومان در سه مرحله به حساب باشگاه واریز کنه  «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.62K · <a href="https://t.me/SorkhTimes/139125" target="_blank">📅 23:27 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139123">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">✅
✅
سپاهان هم با دو گل کسری طاهری .گل گهر و دو هیچ برد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.52K · <a href="https://t.me/SorkhTimes/139123" target="_blank">📅 23:25 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139122">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">❌
❌
❌
آغاسی اخراج شد ولی قبلش آفساید بود و شانس آورد که دربی و از دست نداد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.55K · <a href="https://t.me/SorkhTimes/139122" target="_blank">📅 23:24 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139120">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">🔴
آخرین تمرین تیم قبل از بازی ملوان؛ با حضور محمدحسین صادقی
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.12K · <a href="https://t.me/SorkhTimes/139120" target="_blank">📅 22:24 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139119">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">✔️
✔️
بند 500 هزار دلاری در انتقال بازیکن پرسپولیس به نساجی
❌
❌
در بندی از تفاهم نامه انتقال قرضی براجعه از پرسپولیس به نساجی عنوان شده است در صورتی که باشگاه مازندرانی خواستار دائمی کردن قرارداد براجعه باشد، می تواند با پرداخت 500 هزار دلار به پرسپولیس، قرارداد…</div>
<div class="tg-footer">👁️ 5.07K · <a href="https://t.me/SorkhTimes/139119" target="_blank">📅 22:22 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139118">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">🌬
پایان بازی
نساجی
0⃣
-
2⃣
شمس آذر
🔴
👔
اولین حیا کن، رها کن فصل در قائمشهر؛ روزهای سخت در انتظار مجتبی حسینی!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.03K · <a href="https://t.me/SorkhTimes/139118" target="_blank">📅 22:20 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139117">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">🔴
🟡
احتمالا طارمی و سردار امشب برای اولین بار مقابل همدیگه قرار میگیرن.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.96K · <a href="https://t.me/SorkhTimes/139117" target="_blank">📅 22:17 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139113">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/aw3YJ1TiZ4WmoLRPWMGD0tOMemA3WqBVx2aN_C3gPty_Z9aReUOtTp0mPr4-tfyZY0YEtfaA7_IXzLsqzTjNZ5Ui5zFgvTnPZRAagew7e801Y1EBDVxIs669WMayKRURDNzF6Jy8HhMXgcASiUN3hamK3rJZHHO7KfB3LHmtEsas-2VbI50jnfrjSHZ3jwwiMpJG_dSeJe4-wxsmyz7aSTb0YoOy8a62-m7KuGpA41xIIUUwhp-cEd6hL5gtHpq_950oYuL7-_uwCBVLiDRV_dxyNjx_Z68ihPXVYJpeSLkNQqiFH2xlQiwH-WjdTHQkHCuJxwBWAd3iIz00KsVlkw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/VXPBWuAjU7FBDlJE7RC-pf05UkrnwSKzx19DeyeNhE74jonNd9VBZovshfdDWYbLGMJaalLbVgs74iKZRUTuEbvc8RJB1cE4_nDFy6dexWf0b2KErTHDlpkwj5H7DRiw3gRg8yaXc5l_dGb1gVHEEtC_xs07vMF1CGNLndb_qbTHjClyxYHYGfF9nrMCr6GoRLqV68TTymZc46v6YA00ATnN0MokIuUhZp8qpowUnfY9Hr5_3alHkkaz5z5rb43ke7PzWL0VJX0kHBFHTHWKkFBy_hmQcsfawCQP8h2HubRNqULn9c12B7BiVWJixCIcGWkVoHTYhro61374TjDkkA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/MyJgblZjkqiKWs2-5sSOTrIirrhDO0Qa5vesdE6AQpz4DcmU-zaY4KJnK8CYVD2jgVkHAJyk9WW4bx_Gcgi3OIesxyLdvKh-TREUxYfNLl8FiZGG56za8JtUtwqKAyuIBErtUoSllMeLBoR28GLrQmcuBEdQqdtuLcPlxEKhtIgVXhEdkeNR8RcLSQvw811C4rng_ZnJLXHUm7V-zavlk-qD9ChAYUMEkK3v3hPBftFjg5deYg45bJBV8VoM8kZwgwI9-P9ELCb79lD5z7WW_ksVJeRWuENsaJQztOt-7EDDOFEMuVaCVVMEaB57fohLyVVplhjN2EEE7I2Qj-s6PQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/SH72ttDBv6-z2LlNvwCFvssmEDnHOt6VReAF-b1ABGdNvKJaktqe72xHpqFzCBq9bF5HCJ6-9CuHjV519ge2qgKGkeracIwtA-jmkbz_8SYLsUy5hdkEPxa2N_mKJqhH95FYpMBcsimVbqGkAbxasS4f4XU_Ovk_tbQsSYnavRnMIPXdZP_B5rcJHcul_4vyuaJAvu_ODWggrM7jwiu5xyM-Ot-HABcl_0XpSGmeSK-762j5rVNzAencpfjEiuivY4W2vVVrMbf8EQAJDGEDlVYaLQrxZgxsOMmSXA72tzdX4xTiCbxZzzdyc5ehDO2Er2Rz0LqukFMpu1aiNh_4Kw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">⚽
🤩
پیمان حدادی، مدیرعامل باشگاه پرسپولیس، به همراه ناصر محمدخانی، بهروز سلطانی و مرتضی فنونی‌زاد رفتن سر تمرین امروز
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.02K · <a href="https://t.me/SorkhTimes/139113" target="_blank">📅 22:11 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139112">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">🚨
خبرگزاری فارس: تارتار دلش می‌خواست سرکیف رو جلوی تراکتور بفرسته داخل ولی تو ذهنش یه تصمیم تاکتیکی گرفت و فکر می‌کرد شهرآبادی می‌تونه بازی رو دربیاره
🚨
تارتار همچنین علاقه‌مند به سبک بازی سرگیف هست اما تعدد بازیکن تو تیم‌ باعث شده به همه بازی نرسه
🎗️
«سرخ…</div>
<div class="tg-footer">👁️ 4.85K · <a href="https://t.me/SorkhTimes/139112" target="_blank">📅 22:05 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139111">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">✔️
فرصت‌سوزی باورنکردنی فرشاد احمدزاده مقابل کیسه
😐
😐
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.95K · <a href="https://t.me/SorkhTimes/139111" target="_blank">📅 21:53 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139110">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TTU-Wh8mk0z69ixzXZoxVD5pmpD0YuPim1wOPAUW_tVyw9o9YQv7uikwc0EHMXWU4xNWC2MusOfOSKU2JGeRRq_JqdkYgZ_jnuAcZ-EuarRR-gK_LRLTeQZSTC5yqGT0QgSs530MrHftmKJpndL_USJJA6qe3XLI8MOQgsWXIzbXnKsnylCcXPlHuTkuK-7W8UVWx0A_KDnFGwYDGG624Qx1AvCZVqCJs0RTZRkP2WNKNmNr0SCR2HU84KcsjSnoSJLQxwzbn7V4UCdhrLIO7xdcYAk5xyxnrVwM4EVtHSCyRWUHlqsowf-Wbd3klP_sohh9Z9UNU_ebkrOyQ6cexQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
حسین کنعانی ، دانیال ایری ، مجید عیدی ، پویا پورعلی و محمد عمری پنج بازیکن تیم پرسپولیس که سابقه پوشیدن پیراهن تیم ملوان دارن
✔️
فرزین معامله‌گری هم که برای سربازی منتقل شده به ملوان تنها بازیکنی که سابقه پوشیدن لباس پرسپولیس داره
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.16K · <a href="https://t.me/SorkhTimes/139110" target="_blank">📅 21:36 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139109">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">✅
✅
تراکتور دو بر هیچ برد و چهارمین برد تراکتور رقم خورد ...
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.01K · <a href="https://t.me/SorkhTimes/139109" target="_blank">📅 21:35 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139108">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YPzJDhj5E43vsALnEvUfyi3ktH5i4RpvkNOSKcGqzHDxw32DLrmW-GpdhBkJcbu6AuJHpTKL5CNEwnrZmwXTKxZNbU4QnL7asJckQBNaagsWsCN3LsfI78eswt0qvLTJPZ9fywhObIqGjoMI1T0CSnlGClnBDdQ-NQj9SvU54XvRM0W1n9cyxx-Lho6c-vdYNeOr7FFDypZqypLrmWZrrhOhgmHMFPivoEefBlBxyQGvxBG6KFCsqQ2b3EqqVHH7wb8QltgLAS2eP7bmpz6z33LeIVDPxHo4YI34Q6wFf6w3crXBua2rdEYXoRz1AOEa9UQjfcLmnW3b2UaWHPt8iA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
✅
تراکتور دو بر هیچ برد و چهارمین برد تراکتور رقم خورد ...
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.2K · <a href="https://t.me/SorkhTimes/139108" target="_blank">📅 21:19 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139107">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1cbe495b77.mp4?token=UZM11F3Rhg8JxEfZuUKaem6xyssHpE9NZXz9cSlPdAEqJNmIVTbDZtYGAfMx8F2a_C5fRDlzeedAzyxXTgoQFUYFQ6CU3aBj88lxHrXyBZkfAkc57JQo71n0xEDlZiNVpHEkOA3k1JDCzEMeXMNR2KE5LffcOduEKpggNuYJTD9eP9Wf4YkPetMmPbu89PB4pG__VaVHYwrn0bxqGErIC7p-4rXkm0npv56cfW6RMlspDW2vzXhHNndS56cHkDsghQxA-lXubNi9wBdzk2uQ0Fvhr0QSZVg-_sdJwHQ8UZHB494PJjvEHMC1SUGZ70tj4yRIuvm4SPBNYQyG4wZoOA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1cbe495b77.mp4?token=UZM11F3Rhg8JxEfZuUKaem6xyssHpE9NZXz9cSlPdAEqJNmIVTbDZtYGAfMx8F2a_C5fRDlzeedAzyxXTgoQFUYFQ6CU3aBj88lxHrXyBZkfAkc57JQo71n0xEDlZiNVpHEkOA3k1JDCzEMeXMNR2KE5LffcOduEKpggNuYJTD9eP9Wf4YkPetMmPbu89PB4pG__VaVHYwrn0bxqGErIC7p-4rXkm0npv56cfW6RMlspDW2vzXhHNndS56cHkDsghQxA-lXubNi9wBdzk2uQ0Fvhr0QSZVg-_sdJwHQ8UZHB494PJjvEHMC1SUGZ70tj4yRIuvm4SPBNYQyG4wZoOA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✔️
فرصت‌سوزی باورنکردنی فرشاد احمدزاده مقابل کیسه
😐
😐
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.01K · <a href="https://t.me/SorkhTimes/139107" target="_blank">📅 21:11 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139106">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">❌
❌
❌
ترتر گل اول و زد و الکی الکی سبک مجیدی یک هیچ یک هیچ داره می‌بره همه رو
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.14K · <a href="https://t.me/SorkhTimes/139106" target="_blank">📅 21:08 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139105">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YmPzF6mo-BVvVb4ue1ybqFQVanvTII2mgAQCwm1jCnXKMRTCNl88mOhN8SAa8ntgriEzDy5WL-Q-T0qLJeC_67clNvvRukIu1n8zGFM2jxMp16NtMqk4PgDRPh6bdjCP6ipm-tsWS5-Nrcppn6uipI7leNbOTEJcSKwlMPZdHNnnw4JIL5ANXvdMk7UgM3MJLyBPQFaFbl3P-3I2Vnq0Pf1_4FxlyIyACI3L5d7wvDFW_p2aAkIMtQW4plsTR6Eyph1bIvFM079BxANR5eqOAUyVHue5LOT5_m2wgAZ-oCqVopkdUUQrMDs73d0YSfQaKdg4fNbqPuvNhNWFAJK4MQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
آخرین تمرین تیم قبل از بازی ملوان؛ با حضور محمدحسین صادقی
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.14K · <a href="https://t.me/SorkhTimes/139105" target="_blank">📅 21:05 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139097">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">✅
حالا که حوصلمون سر رفته تو عصر جمعه میتونیم بشینیم پای بازی ترتر و چادرملو رو ببینیم که انشالله مساوی یا باخت ترتر و شاهد باشیم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.11K · <a href="https://t.me/SorkhTimes/139097" target="_blank">📅 20:18 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139096">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BvDSRCp79LAsNVN4g3HyjID8Qe5qAhDWsos50t6c6LawGS8SIzIaJkRJgeo--zK24ZHRBAga4V3G5N8VoabNz8NXc61fzac7Cegng3BqARVwLIg0wUWrkjX-7ZSqDYcg5AKQrf88HjNRDDm6-gH5Z795343vY2V6iv-iTmYDL-lkziH6FPwpjwnlvRfsOyFgQvT7tv0mb-Ap_M6cNdpEnEUXA7Prbh0ljn2Uh7CqetE8eT5TsWYepY4DUjO2pwmlorlTZWPMwnAbk9_SH0aNP4V-ytfaOe2hsLuaICKCK9KrM_Lpkh_d1xQQvZJWRIbPdrB6a0Je2P2ttTJ1EAklbw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
دو مدعی، یک زمین، ۹۰ دقیقه نفسگیر
جنگ امشب در اهواز کفه‌ی ترازو رو به نفع کدوم تیم سنگین میکند؟ همین حالا میتونید این دیدار حساس رو در اسپورت‌نود پیش‌بینی کنید.
[
فولاد
🇮🇷
🆚
⚽
استقلال
]
🔵
بونوس ویژه ثبت‌نام برای کاربران سایت، با شارژ حساب از طریق کریپتو ۴٪ بیشتر از مبلغ شارژ حساب دریافت کنید.
🔗
برای پیش‌بینی این دیدار همین حالا وارد سایت اسپورت‌نود شو و پیش‌بینی خودتو ثبت کن:
👇
2⃣
نسخه جدید سایت:
Sportn5b2.com
2⃣
نسخه قدیمی سایت:
Sport90.bet
🔗
کانال رسمی اسپورت نود:
👇
🔵
@Sportnavad</div>
<div class="tg-footer">👁️ 5.31K · <a href="https://t.me/SorkhTimes/139096" target="_blank">📅 20:15 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139095">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">✅
حالا که حوصلمون سر رفته تو عصر جمعه میتونیم بشینیم پای بازی ترتر و چادرملو رو ببینیم که انشالله مساوی یا باخت ترتر و شاهد باشیم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.21K · <a href="https://t.me/SorkhTimes/139095" target="_blank">📅 18:58 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139094">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">✅
حالا که حوصلمون سر رفته تو عصر جمعه میتونیم بشینیم پای بازی ترتر و چادرملو رو ببینیم که انشالله مساوی یا باخت ترتر و شاهد باشیم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.3K · <a href="https://t.me/SorkhTimes/139094" target="_blank">📅 18:57 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139093">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">🔴
بازی تیم های مدعی در هفته چهارم
❌
چادرملو - تراکتورسازی امروز ساعت ۱۹:۰۰
❌
سپاهان - گل گهر امروز ساعت ۱۹:۳۰
❌
فولاد - کیسه امروز ساعت ۲۱:۰۰
✔️
پرسپولیس - ملوان فردا ساعت ۱۹:۱۵
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.29K · <a href="https://t.me/SorkhTimes/139093" target="_blank">📅 18:54 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139092">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">⭕️
⭕️
فوری/ آکسیوس : طبق گفته مقامات آمریکایی فشار اقتصادی به ایران تا بعد از انتخابات کنگره و سنا آمریکا (۱۲ آبان ماه) ادامه خواهد داشت و بعد از اون دوباره میرن سراغ بمباران و حمله نظامی
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.22K · <a href="https://t.me/SorkhTimes/139092" target="_blank">📅 18:50 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139091">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">❌
❌
فوری/ با اعلام مهدی تارتار باشگاه تا 22 شهریور بازیکنی به تیم ملی امید نخواهد داد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.36K · <a href="https://t.me/SorkhTimes/139091" target="_blank">📅 17:36 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139090">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">🚨
فووووری/ با اعلام فدراسیون فوتبال بازیکنان دعوت شده به اردو تیم ملی باید تا پایان روز شنبه هفتم شهریور خودشون رو به اردو تیم ملی امید معرفی کنن
😐
❌
❌
اگه پرسپولیس بازیکن بده عملا ایری، شهرآبادی و لطیفی فر رو برای دربی نداریم
🎗️
«سرخ تایمز» دریچه ای تازه به…</div>
<div class="tg-footer">👁️ 5.46K · <a href="https://t.me/SorkhTimes/139090" target="_blank">📅 17:35 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139089">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fa7be285b4.mp4?token=igSxu8AMagboEO_HCCxqDB8ZhglDTeuNV25crYfKe86yZe8OXG5LjGW0H-W0V7mXY5QXqSSmGXTNf4tNJ2dBcxXIA4fAGKcSKBVi5BmmJft8pOD2jhPbuh3xESALIbraMBXMVcDBRgzlwQQZvWqNRE_kVngWDzFtc3_4bqyiyWb-20BL_1rmy2e6D31IY9VnoiXk0MMNFIyWuKNoSKIiG6iJ1_n23bm4r75buQ5ITLZ85XEINrjSanBiGCkS61g6KNzEKEzjy6QkD3VtHA28DXmrAZLFqSBbvf0w2q_1yroYN96IJzpHP7JtTK-_gm3qqWpRFLBpLxCRECvwfIn5Hw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fa7be285b4.mp4?token=igSxu8AMagboEO_HCCxqDB8ZhglDTeuNV25crYfKe86yZe8OXG5LjGW0H-W0V7mXY5QXqSSmGXTNf4tNJ2dBcxXIA4fAGKcSKBVi5BmmJft8pOD2jhPbuh3xESALIbraMBXMVcDBRgzlwQQZvWqNRE_kVngWDzFtc3_4bqyiyWb-20BL_1rmy2e6D31IY9VnoiXk0MMNFIyWuKNoSKIiG6iJ1_n23bm4r75buQ5ITLZ85XEINrjSanBiGCkS61g6KNzEKEzjy6QkD3VtHA28DXmrAZLFqSBbvf0w2q_1yroYN96IJzpHP7JtTK-_gm3qqWpRFLBpLxCRECvwfIn5Hw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
مهدی تارتار: واقعا یک تیم نمی تواند 90 دقیقه تهاجمی بازی کند. ما باید طوری برنامه ریزی کنیم که بتوانیم به شکل خوبی 90 دقیقه را به پایان برسانیم
. زمین چمن یادگار امام تبریز واقعا استاندارد نبود و کار را سخت کرده بود
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.47K · <a href="https://t.me/SorkhTimes/139089" target="_blank">📅 17:08 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139088">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f04141bbb0.mp4?token=RCedKYR1Ay2IEQl227zgXrcgzdOCkw3AK_WJHtelqmiimKTLtId9aEa9pSdMCCgR6w-3bdSzsSiDNvIQ1A7X4lPfHhJffnVm1Gfjn-wfUmdbbL_CXl9ioOTwR9mg6vbeaSNgY-Be6p98tr4BcGO6Hqn47P7IG1Ko0yWTv2iDnk4gJm3yzj-aasJUFjuol5ZpUgt-XBhUXPN_4d38feVWFyUMiTRmTlDXezogVGfzhxrBWaL6ntlHi1Pfn5sXKSQOrpl-4i9MrGMJzGnGY4et1JCThgXsR0MW-l0s1PyjmI6Wmk6MFTTw_9qmaIKMkRMwaox4VIXvlogRuesPZQh67w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f04141bbb0.mp4?token=RCedKYR1Ay2IEQl227zgXrcgzdOCkw3AK_WJHtelqmiimKTLtId9aEa9pSdMCCgR6w-3bdSzsSiDNvIQ1A7X4lPfHhJffnVm1Gfjn-wfUmdbbL_CXl9ioOTwR9mg6vbeaSNgY-Be6p98tr4BcGO6Hqn47P7IG1Ko0yWTv2iDnk4gJm3yzj-aasJUFjuol5ZpUgt-XBhUXPN_4d38feVWFyUMiTRmTlDXezogVGfzhxrBWaL6ntlHi1Pfn5sXKSQOrpl-4i9MrGMJzGnGY4et1JCThgXsR0MW-l0s1PyjmI6Wmk6MFTTw_9qmaIKMkRMwaox4VIXvlogRuesPZQh67w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
مهدی تارتار:واقعا از شکست پرسپولیس مقابل تراکتور ناراحت هستم اما این هجمه علیه ما طبیعی نیست. ما اینقدر در ۲ بازی اول خوب کار کردیم که رقبا ترسیده‌اند. احساس خطر کرده‌اند از بازی‌های خوب پرسپولیس!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.05K · <a href="https://t.me/SorkhTimes/139088" target="_blank">📅 17:00 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139087">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4ef45c0a06.mp4?token=ajyiL3iOUYeKXW_L-n0aR3Z9TEIOIh3-YpfuSpLm-klkeXLKEDAaJSLtryrTu4sLOGtIRPwfwVx0hzIOHN4ZWj56Z8363PH472p4dSqHQfv_RdZhAPV3mOAhLXSHCBpFDasAoiSKkvPw-oGSwzD1DWSjjPcsAXUgnXKQM3FP1uur4BDBkGCKssS_mV-SBAaDrVXKTdWwmqCDku-Ramy3stUNfOmmGVYwVSa0p-V1zgclmULOT_YFMM58bhv1mKk4peTeeO3f_BOWwB6Hrng4yLV8_uNx6vqJAflvr7yBmedNjbXH3oRR4RRZ_e32yKzlozCCkBqLVaPUslTybMl7vw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4ef45c0a06.mp4?token=ajyiL3iOUYeKXW_L-n0aR3Z9TEIOIh3-YpfuSpLm-klkeXLKEDAaJSLtryrTu4sLOGtIRPwfwVx0hzIOHN4ZWj56Z8363PH472p4dSqHQfv_RdZhAPV3mOAhLXSHCBpFDasAoiSKkvPw-oGSwzD1DWSjjPcsAXUgnXKQM3FP1uur4BDBkGCKssS_mV-SBAaDrVXKTdWwmqCDku-Ramy3stUNfOmmGVYwVSa0p-V1zgclmULOT_YFMM58bhv1mKk4peTeeO3f_BOWwB6Hrng4yLV8_uNx6vqJAflvr7yBmedNjbXH3oRR4RRZ_e32yKzlozCCkBqLVaPUslTybMl7vw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
تارتار سرمربی پرسپولیس:
🔹
ارونوف یکی از بازیکنان خوب تیم ماست اما دیر به تمرینات اضافه شده است. بحث مصدومیت ارونوف جدی
نیست
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.1K · <a href="https://t.me/SorkhTimes/139087" target="_blank">📅 16:59 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139086">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f7eb7a5402.mp4?token=dCvSZbVWrLVgbBrtrPxzOH2OsM5R4mjNIdt1MigBtFktBzo9HKpr7XICwvkPtkSX8V7G8AJUTOyKE9_uPDQhyehg-tELgQXehlOz8WoY70ZRWiBHZbS77qjFJKw-ka_YZJv4yOkRSgtOwQg6dg6Wv0bvFD4jKGV7z76tCLpSx-Pqrm_-D6r_89LioR5FlT3Ho2dUwLhLVc0h5302wmgjYgJOEfdAdTVIPcIyOSXypaBXUXyLMO4wfgFDe9f5jTpVdmeV3sbKgrW2Lv314Rb3738J0W6vhHGnRHmhijJHjFG3AJPVtsR1eMgyX4bVa4OcjEXkMwuKvK58s_tZVpRYqw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f7eb7a5402.mp4?token=dCvSZbVWrLVgbBrtrPxzOH2OsM5R4mjNIdt1MigBtFktBzo9HKpr7XICwvkPtkSX8V7G8AJUTOyKE9_uPDQhyehg-tELgQXehlOz8WoY70ZRWiBHZbS77qjFJKw-ka_YZJv4yOkRSgtOwQg6dg6Wv0bvFD4jKGV7z76tCLpSx-Pqrm_-D6r_89LioR5FlT3Ho2dUwLhLVc0h5302wmgjYgJOEfdAdTVIPcIyOSXypaBXUXyLMO4wfgFDe9f5jTpVdmeV3sbKgrW2Lv314Rb3738J0W6vhHGnRHmhijJHjFG3AJPVtsR1eMgyX4bVa4OcjEXkMwuKvK58s_tZVpRYqw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
تارتار
:
❌
• وضعیت ابوالفضل جلالی بهتر شده است/ بازی فردا مقابل ملوان را فدای دربی نخواهیم کرد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.1K · <a href="https://t.me/SorkhTimes/139086" target="_blank">📅 16:57 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139085">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/587e6b7701.mp4?token=j1HMcZShvx1X1B2uFNNU0NezZ-Iss3IEZrocObf7TUJyK2Q21F4aXk-1RjdkdvogP0VfeFL05BeYDAtZ5YkChxE-AUxe_hHtAsYn_yDIR6ysID0Da6mH76-YAY6AgOavlGl7L3Gmk4F9rdl5zlpkAAaDxdgfVWFAZrH4a4TOsQ5qgd33RitsEG_CfSajSJfINHnPCEZSf7-cv8RrJnH36ovsMHmHVKODteoOhO2D_OZcI2QQgbeIZvREb-o3WNADpBrsaS8uFVsvR-lmKtlI9PE_OiLsGj3E9FkhZ8YRY6QyK3h2ag8sD6JfGR-NQfSvp1XeBIEzKntLOdOGm0lKUWcYT7eMKjUgfngzof96G5DFHclxl3bm9f0bSk0VMyzrmDOmZFO-5cdUGzTlRO9YRKyltYS0_bvxtHvVpiv7MbGyVivgjJ9LqcTT-MawpKCEKXgtDkcwHAgziEHLhqDZvc1kMYJtNAgodD1Zh-7IjQuLG7Nl9CLB32UQqHkeQKxjkI_SRITrlfVX51Exd_aRICL64NoeojylrhhcYIbsm86jIpkMrenazaVvOwnUgdIlnBc4xqqoJukoVvn46KR8m_oNnFXYdZdCzZ4rfNNwUIzKIGsNb2wGQsZPuC6HXtJQzWhJs3IenTaaftcVZgJ-B7l9KpkZPRAIpsEZ1SMHwwE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/587e6b7701.mp4?token=j1HMcZShvx1X1B2uFNNU0NezZ-Iss3IEZrocObf7TUJyK2Q21F4aXk-1RjdkdvogP0VfeFL05BeYDAtZ5YkChxE-AUxe_hHtAsYn_yDIR6ysID0Da6mH76-YAY6AgOavlGl7L3Gmk4F9rdl5zlpkAAaDxdgfVWFAZrH4a4TOsQ5qgd33RitsEG_CfSajSJfINHnPCEZSf7-cv8RrJnH36ovsMHmHVKODteoOhO2D_OZcI2QQgbeIZvREb-o3WNADpBrsaS8uFVsvR-lmKtlI9PE_OiLsGj3E9FkhZ8YRY6QyK3h2ag8sD6JfGR-NQfSvp1XeBIEzKntLOdOGm0lKUWcYT7eMKjUgfngzof96G5DFHclxl3bm9f0bSk0VMyzrmDOmZFO-5cdUGzTlRO9YRKyltYS0_bvxtHvVpiv7MbGyVivgjJ9LqcTT-MawpKCEKXgtDkcwHAgziEHLhqDZvc1kMYJtNAgodD1Zh-7IjQuLG7Nl9CLB32UQqHkeQKxjkI_SRITrlfVX51Exd_aRICL64NoeojylrhhcYIbsm86jIpkMrenazaVvOwnUgdIlnBc4xqqoJukoVvn46KR8m_oNnFXYdZdCzZ4rfNNwUIzKIGsNb2wGQsZPuC6HXtJQzWhJs3IenTaaftcVZgJ-B7l9KpkZPRAIpsEZ1SMHwwE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
مازیار زارع سرمربی ملوان:
🚨
پرسپولیس پرمهره ترین تیم ایران است و کادرفنی خوبی دارد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.2K · <a href="https://t.me/SorkhTimes/139085" target="_blank">📅 16:04 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139084">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">🔴
بازی تیم های مدعی در هفته چهارم
❌
چادرملو - تراکتورسازی امروز ساعت ۱۹:۰۰
❌
سپاهان - گل گهر امروز ساعت ۱۹:۳۰
❌
فولاد - کیسه امروز ساعت ۲۱:۰۰
✔️
پرسپولیس - ملوان فردا ساعت ۱۹:۱۵
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.31K · <a href="https://t.me/SorkhTimes/139084" target="_blank">📅 16:00 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139083">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">🔴
بازی تیم های مدعی در هفته چهارم
❌
چادرملو - تراکتورسازی امروز ساعت ۱۹:۰۰
❌
سپاهان - گل گهر امروز ساعت ۱۹:۳۰
❌
فولاد - کیسه امروز ساعت ۲۱:۰۰
✔️
پرسپولیس - ملوان فردا ساعت ۱۹:۱۵
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.25K · <a href="https://t.me/SorkhTimes/139083" target="_blank">📅 15:57 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139082">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/L6LlLOvr6ffyGca_fMVXg_rzjLsUWG1hlJvtDRwKDPLIKLRAgCss9ZNbQnB8yW9PjO1eFl7YTr5AnvhVWwWRlY5RuLzYDhsO4bUFKXeySr64SMxaoswPp-VS4cbw1zVuCcWiP7pWenRDlyRxr-NhVTmiTtkPjyyORFu5xJrAhNDT5iuFPodxrEfaXz-r5KwuQCzJ4uZSPnkVUqRfep2W5yfFdt4-OOT8RcCTDgu_rxi9FnLgybe2iun_vHBPMrgqFSsYYXFlbCIK7Z8Bhn81d17-0c0vPa1IXjzk-cmAAWptsxTVpu7WlVd0lFUh0ZyNIp7O-0aXPfxvo4YPXd8qjg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
خبرگزاری فارس: تارتار دلش می‌خواست سرکیف رو جلوی تراکتور بفرسته داخل ولی تو ذهنش یه تصمیم تاکتیکی گرفت و فکر می‌کرد شهرآبادی می‌تونه بازی رو دربیاره
🚨
تارتار همچنین علاقه‌مند به سبک بازی سرگیف هست اما تعدد بازیکن تو تیم‌ باعث شده به همه بازی نرسه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.35K · <a href="https://t.me/SorkhTimes/139082" target="_blank">📅 15:52 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139081">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/etTHqKXkB3WaYSoLdjbDYtO6iDG5Esx0nV8tfh1a7VX5J4qBNJdp3XHcZ7HnXshVMbyT9O09M4cytX5kga1GKIde71G5h_n-PLlWPGi9BeTdhrkHL-5ZwJ7BBqViCk2jfKjEjNxkDSvQQGJouiIYoppVEkDKprlFA9Le1EneyMXueB3fJsKJPoXI4OREHPDGWV7AHnjtF9nRPyDy88ZQnNVCUnE12vXoFKecS6FV2uz_kZRMGkj98eHFphEk4z2sg0dzuh0muyCas2bRZhKWnVOqw6XlXA9PquAHrxLPD07S07oJn7GajXfFtF1Y0Ek_4FTEL4JtV1-6XCx1nB0M9g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
🟡
احتمالا طارمی و سردار امشب برای اولین بار مقابل همدیگه قرار میگیرن.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5K · <a href="https://t.me/SorkhTimes/139081" target="_blank">📅 15:52 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139080">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kEUopIdI8pvhd0ErWEMe6HlaJyVB2JWu4lYX_k1oLs9ddKhvuv6IjYEpbl4F2MiXTpDbfVi1znux7qAoawySugnwWQNAfnIF-zH8llinhBCZpP0briu4aWScRBlypGfkLAPy2CatNV1wH2D4jl2_QVjxuQ5KXOdyyu8AfCzFl5LWyGMRovJJPnOMOqgPyPmfSczAgvM6Roq8otjhKgbY4KkJaPwarGuwvgmCqRuD198JwXaUYC_pqEM4FxIa9h2XWF-ncC5rcYWeg5-7gotkSsI-SSnVwfiePRHNowx0nnxx0NCYP7Q971uD3AiSrzVo--3iHN2JrHnU0zGVsXqSCw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">😀
💵
مهمترین بازیکنان آزاد ایران و ارزش آنها در ترانسفرمارکت تا این لحظه:
🔻
محمد محبی
- 2.5 میلیون یورو
😀
مجید حسینی
- 700 هزار یورو
🔻
رضا اسدی
-  500 هزار یورو
🔻
فراز امامعلی
- 450 هزار یورو
🔻
علی کریمی
- 350 هزار یورو
🔻
مهدی مهدی‌پور
- 350 هزار یورو
🔻
ایمان سلیمی
- 250 هزار یورو
🔻
امیر عابدزاده
- 200 هزار یورو
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.97K · <a href="https://t.me/SorkhTimes/139080" target="_blank">📅 15:51 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139079">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BnhZwMujuhRT9f6nFyty4SjhsWuPSd4ZJJvNYVm6XWeiSpxA82IzqBL3otidfjJpU6sC4wCF3YYn-7czhbxTCIqt3ZlE_JGqes4HOcBn3vzyslORPop4VdDLXUsYLFS3uc5QOKKutrSF3DgmlN2GmUd_zrvCwbNK7B5CDmepaHgPH4nsG91X5vzYpaOoU4vVjAfQGI9ARd0jyzSiB0PDkYmxBKRPB_S9i8ghj54sgjrVa88qAqBriEUsufrVc97Fy3GvFMxTaCV2mJivwKdKvLehef1FRTBcSud9oFj05l-EnMLcMW2RAe4vtgRJfa8ep1NzXeVa9sqp8gp1pnQkrw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
چادرملو برای فرار از روزهای سخت، امروز باید مقابل تراکتورِ آماده دست به کار بزرگی بزند؛ تراکتور با شروع قدرتمندش، برای حفظ روند خوب و اضافه کردن یک برد دیگر به کارنامه‌اش به میدان می‌آید.
[
چادرملو
🇮🇷
🆚
⚽
تراکتور
]
🔵
بونوس ویژه ثبت‌نام برای کاربران سایت، با شارژ حساب از طریق کریپتو ۴٪ بیشتر از مبلغ شارژ حساب دریافت کنید.
🔗
برای پیش‌بینی این دیدار همین حالا وارد سایت اسپورت‌نود شو و پیش‌بینی خودتو ثبت کن:
👇
2⃣
نسخه جدید سایت:
Sportn5b2.com
2⃣
نسخه قدیمی سایت:
Sport90.bet
🔗
کانال رسمی اسپورت نود:
👇
🔵
@Sportnavad</div>
<div class="tg-footer">👁️ 5.21K · <a href="https://t.me/SorkhTimes/139079" target="_blank">📅 15:47 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139078">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">❤️
فووووووووووووری
🔴
گفته میشه محمدحسین صادقی دیروز تو تمرین پرسپولیس با یک بازیکن درگیری لفظی داشته و توسط مهدی تارتار از تمرین پرسپولیس اخراج شده / هفت صبح
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.48K · <a href="https://t.me/SorkhTimes/139078" target="_blank">📅 15:43 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139076">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">❌
❌
تصاویری از تمرین امروز عصر سرخ ها پس از یک روز استراحت؛ارونوف بدون مشکل در تمرین گروهی/گرا و جلالی مصدومان پرسپولیس
❌
کنفرانس مطبوعاتی تارتار و مازیار زارع فردا ساعت 16:00 در هتل المپیک
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.77K · <a href="https://t.me/SorkhTimes/139076" target="_blank">📅 14:22 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139075">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">✔️
✔️
✔️
بی انصافیه اگه از عملکرد خوب مهدی تیکدری نگیم!
✔️
برای اولین بار تو عمرش اومد پست غیر تخصصی دفاع چپ بازی کرد و هم در دفاع و هم در حمله موثر و خوب بود
✔️
✔️
پر تلاش و انگیزه از دقیقه اول تا آخرین دقیقه ظاهر شد و امیدوار مون کرد
🎗️
«سرخ تایمز» دریچه ای…</div>
<div class="tg-footer">👁️ 6.02K · <a href="https://t.me/SorkhTimes/139075" target="_blank">📅 11:42 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139074">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">🚨
امید عالیشاه به علت مصدومیت چهار هفته از میادین دور خواهد بود
💔
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.08K · <a href="https://t.me/SorkhTimes/139074" target="_blank">📅 11:41 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139073">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">🚨
🔵
🔴
کشوری فرد دبیر سازمان لیگ فوتبال ایران:
🔴
سهمیه هواداران در دربی استقلال و پرسپولیس ۵۰-۵۰ است.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.19K · <a href="https://t.me/SorkhTimes/139073" target="_blank">📅 11:39 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139072">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">❌
❌
ادعای هفت ورزشی: محمدحسین صادقی به علت درگیری با دو بازیکن پرسپولیس از حضور در تمرینات منع شد!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.38K · <a href="https://t.me/SorkhTimes/139072" target="_blank">📅 11:38 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139071">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">🚨
مهدی تارتار سرمربی پرسپولیس، محمد حسین صادقی وینگر جوان خود را به صورت کامل از تیم کنار گذاشته است و هیچ قصدی برای استفاده از وی ندارد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.38K · <a href="https://t.me/SorkhTimes/139071" target="_blank">📅 10:26 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139070">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">❌
❌
هادی چوپان مستر المپیا را از دست داد
✔️
✔️
هادی چوپان، پس از غیرفعال شدن ویزای طلایی امارات و از دست دادن مصاحبه سفارت آمریکا، از حضور در مستر المپیا ۲۰۲۶ انصراف داد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.54K · <a href="https://t.me/SorkhTimes/139070" target="_blank">📅 09:17 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139069">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">❤️
صبح آدینه تون بخیر و شادی
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.36K · <a href="https://t.me/SorkhTimes/139069" target="_blank">📅 09:10 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139068">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">🔵
ورود به اسپورت‌نود، فقط با یه کلیک!
📌
هنوز برای ورود، دنبال لینک و مسیرهای مختلف می‌گردی؟
📌
وقتشه راه ساده‌تر رو انتخاب کنی!
🔗
با مینی‌اپ رسمی اسپورت‌نود، همه‌چیز یکجا و آماده‌ست؛ ربات رو باز کن، وارد شو و مستقیم به امکانات اسپورت‌نود دسترسی داشته باش.
1⃣
-  بدون لینک‌های سرگردان
2⃣
-  بدون مراحل اضافه
3⃣
-  سریع، ساده و یکپارچه
🔗
مسیر ورودت رو کوتاه کن؛ اسپورت‌نود همینجاست:
👇
🔵
@Sportnavad_bot
🔵
@Sportnavad_bot
📌
کانال رسمی اسپورت‌نود:
🔵
@Sportnavad</div>
<div class="tg-footer">👁️ 6.53K · <a href="https://t.me/SorkhTimes/139068" target="_blank">📅 01:23 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139067">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">❌
❌
تارتار با حضور بازیکنا در تیم ملی امید خارج از فیفادی مخالفت کرد!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.48K · <a href="https://t.me/SorkhTimes/139067" target="_blank">📅 00:47 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139066">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">⚠️
یایا امپرور بعداز نتایج درخشانش تو عراق میخاد برگرده ایران…سپاهان هم یه نیم نگاهی بهش داره؛فورا باید اسپند دود کنیم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
𝓣𝓲𝓶𝓮
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.53K · <a href="https://t.me/SorkhTimes/139066" target="_blank">📅 00:39 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139065">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">🚨
🚨
فووووووووووری
❌
❌
یک سری شایعات پخش شده امسال بخاطر فشردگی تقویم لیگ خبری از جام حذفی نیست و قراره سهیمه آسیایی جام حذفی به چادرملو داده بشه
😐
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.65K · <a href="https://t.me/SorkhTimes/139065" target="_blank">📅 00:35 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139064">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">✖️
✖️
بهمنی رییس سازمان لیگ: فکر نمی‌کنم بتوانیم به خاطر فشردگی بازی ها امسال جام حذفی برگزار کنیم
🙁
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.36K · <a href="https://t.me/SorkhTimes/139064" target="_blank">📅 00:34 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139063">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromشــًٍـٍؓـٍ۪ـ۪ؔـٍ℘ًًیــًٍـٍؓـٍ۪ـ۪ؔـٍ℘ًًد۪ؔاٍؓ℘ًً</strong></div>
<div class="tg-text">تا میتونی اورنوف تشویق کنید و سرگیف اینا ستاره تیمند ارزو هرتیمی ک این بازیکن داشته باشند و ایری هم تشویق کنید روحیه اش برگرد</div>
<div class="tg-footer">👁️ 6.23K · <a href="https://t.me/SorkhTimes/139063" target="_blank">📅 00:34 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139062">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from🅼🅴🅷🅳🅸</strong></div>
<div class="tg-text">پاس هایی ک باکیچ میندازه رو هیچ بازیکنی نمیتونه تو پرسپولیس بندازه بعد کلا یارو رو نیمکته</div>
<div class="tg-footer">👁️ 6.04K · <a href="https://t.me/SorkhTimes/139062" target="_blank">📅 00:34 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139061">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WKntvmrIHsvHiqod2tCPHPeE96S4VQIOEW-Z23Iz0WJlOUD3kkM2NaVaCtSSxy8c84ZfwQI-GOf8J7CNNmH5odhThBm3OCv1WiwAPhLUpvSDQ8j-BFKQuipsYW_6eiZhawC3_cNB73_zmHp9Mne4Xr3QSNerH8oQlVqve-hmpAnmwv4a9VzBKNKA9ZoJlwuP8yfYfDJ1SwCPHhIsZGk5yW4whd2KdbQ9YCQQsCIxSrzzjd1_8j-gN3dkDqBsWS8IosIUk-ePLcrsQZCvXoawWpIowEDwrqF4ZuHggb_UsfBCo9r_ii7K8ZQSTv3W9W97NElbccNVZY-NkiU3PJVXpw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
فارس:
⌛
مدیریت پرسپولیس تصمیمی برای تغییر در کادر فنی ندارد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.26K · <a href="https://t.me/SorkhTimes/139061" target="_blank">📅 00:30 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139060">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d099f34763.mp4?token=SUp2PyRGNo2RLTKwnqrmyz0K40uoKu7DKSItX5drSFJ7i8968j4CwRPDg2e8FD9FaSY3DvTok1TT0GZ71IiMfJ2iauPyFZNbNnJu6T5zMYMZ4ZkbkbzNKxF4BmCaM1V0c4dxXYFDFvjrssvf2V1noIUhN4-6RWfeOBGh4ehFtN_LwAvuFswwd4FXPT6SXOrSj4JkK7u-DvpuoMU0Lb8ZktOX4WQoRHBeP0R4Dfue37I-J1P60xy_8Mnj_-1VTBFsoFJhfzRGBeYjOW26uPxFK5AJX_GQagHKdWm3zRxGD3qvJQhN0PjXTSjlBu46LW8hf8VIommIHIZRALQQsPxwkA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d099f34763.mp4?token=SUp2PyRGNo2RLTKwnqrmyz0K40uoKu7DKSItX5drSFJ7i8968j4CwRPDg2e8FD9FaSY3DvTok1TT0GZ71IiMfJ2iauPyFZNbNnJu6T5zMYMZ4ZkbkbzNKxF4BmCaM1V0c4dxXYFDFvjrssvf2V1noIUhN4-6RWfeOBGh4ehFtN_LwAvuFswwd4FXPT6SXOrSj4JkK7u-DvpuoMU0Lb8ZktOX4WQoRHBeP0R4Dfue37I-J1P60xy_8Mnj_-1VTBFsoFJhfzRGBeYjOW26uPxFK5AJX_GQagHKdWm3zRxGD3qvJQhN0PjXTSjlBu46LW8hf8VIommIHIZRALQQsPxwkA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
انتشار تیزر رسمی سریال کمدی «مرد سه‌ هزار چهره»؛
آغاز پخش از جمعه ۱۳ شهریور از شبکه سه.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.16K · <a href="https://t.me/SorkhTimes/139060" target="_blank">📅 00:30 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139059">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">‼️
👤
آقا مهدی فرمودن دستیار خارجی نمیخان
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس 𝓣𝓲𝓶𝓮
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.17K · <a href="https://t.me/SorkhTimes/139059" target="_blank">📅 00:03 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139058">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">‼️
👤
آقا مهدی فرمودن دستیار خارجی نمیخان
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
𝓣𝓲𝓶𝓮
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.97K · <a href="https://t.me/SorkhTimes/139058" target="_blank">📅 23:51 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139057">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">✔️
✔️
⚡️
⚡️
⚡️
علیرضا همایی‌فر، یعقوب براجعه و محمدحسین صادقی از جمله بازیکنانی هستند که احتمال دارد در ساعات پایانی نقل‌وانتقالات از پرسپولیس جدا شوند و به صورت قرضی راهی تیم‌های دیگر شوند
✍️
🗞
خبرورزشی
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس…</div>
<div class="tg-footer">👁️ 6.14K · <a href="https://t.me/SorkhTimes/139057" target="_blank">📅 23:29 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139056">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">❌
❌
قدوسی: اورونوف تو بازی با ملوان هم روی نیمکته!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.23K · <a href="https://t.me/SorkhTimes/139056" target="_blank">📅 23:06 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139055">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">✔️
✔️
✔️
✔️
ارونوف از امروز در تمرین پرسپولیس
🔴
اورونوف که در بازی تدارکاتی پرسپولیس مقابل امیدهای این باشگاه بار دیگر احساس ناراحتی کرده بود، با پیگیری کادر پزشکی و انجام بررسی‌های لازم، ظاهراً شرایط مطلوبی پیدا کرده است.
🔴
این بازیکن از امروز در تمرینات گروهی…</div>
<div class="tg-footer">👁️ 5.91K · <a href="https://t.me/SorkhTimes/139055" target="_blank">📅 22:59 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139054">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">🔄
❌
اسماعیل کارتال با فنرباغچه در مجموع 3-2 تیم لیون رو تو فرانسه شکست داد و به لیگ قهرمانان اروپا صعود کرد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.99K · <a href="https://t.me/SorkhTimes/139054" target="_blank">📅 22:55 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139053">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/r2cxiYl-yWejOzU3bUjZliycMIPeoZWzyhFApk2SMM7zdxOXfX_5rzQFEqehz0ed77R4IMeTgS1kmh5NWhnB-hm3o1THsR2_XKw0Gic7NSxwywo7uze7n9D4jYQW953I7BcU3nJGJWFSHQLK3WC9TYYpAVKMW1mSqUD2zCIf02CAKupokDt8Vy1Va4TLBS31NrVCImzP2V5OXZt1NTmvNKLpqYKG18SIX_JoK8LH02gtpTiyiEL_8clg7fOiFWd1YYmktMIQid0l5HXq1zHxLfd4XvLKHJ56wjG805SbZsUdUbIUQG7GlQnnHcO4_8sr4LhAm1U9C3M_zqStA9io2w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟢
آبی‌ها آماده‌ی شکار؛ لوتون سد راه چلسی!
نبردی که می‌تونه از همون سوت اول بازی غافلگیرکننده باشه.
[
چلسی
🔹
🆚
🔹
لوتون
]
🔵
بونوس ویژه ثبت‌نام برای کاربران سایت، با شارژ حساب از طریق کریپتو ۴٪ بیشتر از مبلغ شارژ حساب دریافت کنید.
🔗
برای پیش‌بینی این دیدار همین حالا وارد سایت اسپورت‌نود شو و پیش‌بینی خودتو ثبت کن:
👇
2⃣
نسخه جدید سایت:
Sportn5b2.com
2⃣
نسخه قدیمی سایت:
Sport90.bet
🔗
کانال رسمی اسپورت نود:
👇
🔵
@Sportnavad</div>
<div class="tg-footer">👁️ 5.97K · <a href="https://t.me/SorkhTimes/139053" target="_blank">📅 22:46 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139052">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">✔️
✔️
✔️
✔️
ارونوف از امروز در تمرین پرسپولیس
🔴
اورونوف که در بازی تدارکاتی پرسپولیس مقابل امیدهای این باشگاه بار دیگر احساس ناراحتی کرده بود، با پیگیری کادر پزشکی و انجام بررسی‌های لازم، ظاهراً شرایط مطلوبی پیدا کرده است.
🔴
این بازیکن از امروز در تمرینات گروهی…</div>
<div class="tg-footer">👁️ 5.48K · <a href="https://t.me/SorkhTimes/139052" target="_blank">📅 22:42 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139051">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">🔹
🔹
فووووری
🔹
فراز امامعلی : به عنوان دفاع چپ با پرسپولیس به توافق رسیدم و منتظر جلسه نهایی عقد قرارداد هستم. دفاع چپ و وینگر چپ میتوانم بازی کنم. آقای تارتار و باشگاه پرسپولیس به من لطف داشتند و برای پست دفاع چپ من را انتخاب کردند.
🎗️
«سرخ تایمز» دریچه ای…</div>
<div class="tg-footer">👁️ 5.47K · <a href="https://t.me/SorkhTimes/139051" target="_blank">📅 22:40 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139050">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vAIojNpCxnDiov-DQv0Ui6-E-FynbRtnLkA_A-efR2G8RZE4G4HIwsiKEN4bJtuDhhhF4grbUIc9oIIPKPIcrqA-a0b6TLeV_rY95EI5t4yYVxeNfW1ZbEp_ljcFU77q_mmby_vuUu6OhgZRGVSgkMR7Pq0in3bi1--VKqT5GEZMmh7TeXiI-LCe2q4Qf5NIrFKNSNuQdl4dJQMfVxHUz2t4rOfZVGwH33jJalKHJ3AKjiQ8OosroInGWTV3Y0VHjbQPBkxBqMAN0BqhDzYLK53voJBM2zFKRSyu0lkeQgmsr7-HqxsJ4NGNproJM-qKicT4C2bHJEZPZG9u7Wtsvg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
❌
تصاویری از تمرین امروز عصر سرخ ها پس از یک روز استراحت؛ارونوف بدون مشکل در تمرین گروهی/گرا و جلالی مصدومان پرسپولیس
❌
کنفرانس مطبوعاتی تارتار و مازیار زارع فردا ساعت 16:00 در هتل المپیک
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.71K · <a href="https://t.me/SorkhTimes/139050" target="_blank">📅 22:30 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139049">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">✔️
✔️
مدیر پرسپولیس: فراز امامعلی مدنظر ما نیست.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.66K · <a href="https://t.me/SorkhTimes/139049" target="_blank">📅 22:29 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139048">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">❌
فراز امامعلی: پرسپولیس یکی از تیم‌هایی است که با من مذاکره کرد. اتفاقا به توافق نهایی هم رسیدیم و منتظرم ببینم جلسه عقد قرارداد برگزار خواهد شد یا نه
❌
❌
راجب پست‌هایی که توانایی بازی داره گفته: هم دفاع چپ بازی میکنم، هم وینگر چپ و هم مهاجم نوک
🎗️
«سرخ تایمز»…</div>
<div class="tg-footer">👁️ 5.93K · <a href="https://t.me/SorkhTimes/139048" target="_blank">📅 21:08 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139047">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IY90h0OMCHvTZqkidCR5L9QyLggCdnrAYk-SlhPmhPcemMBcyYNGE31banhhpve2s0Kr1dZMaXeXKGmT_52VxcKgVUm_wf7qI3cFP5vhHV_EGoBugEqWMcVYshWLS1JhVsH6ynRf_px7ymj_eT_sTqZsNIFux3ZL5oriNYb51Ir7MUu_Ft6q7sCjmETzhBcsMMiJ6uBLKqu8btjHr13t2-kFxLprEl8QA14FgvjaNkXNuHPPOlYuXQqGtYU_HA7lb2M7PhuEgWuZfK8-d2jXvvzk_dUTQs1omRKIyGbCdIIEjyMmvHnSq8H4BJ_HF4jLM61zVcVX_G9N4t2HyyNbIA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
✅
اسکواد پرسپولیس با ۲۶ بازیکن برای فصل پیش رو بسته شد
🟪
۳ گلر
🟪
۵ مدافع وسط
🟪
۲ دفاع راست
🟪
۲ دفاع چپ
🟪
۵ هافبک وسط
🟪
۳ وینگر چپ
🟪
۳ وینگر راست
🟪
۳ مهاجم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes
﻿</div>
<div class="tg-footer">👁️ 6.16K · <a href="https://t.me/SorkhTimes/139047" target="_blank">📅 20:40 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139046">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">🔹
🔹
فووووری
🔹
فراز امامعلی : به عنوان دفاع چپ با پرسپولیس به توافق رسیدم و منتظر جلسه نهایی عقد قرارداد هستم. دفاع چپ و وینگر چپ میتوانم بازی کنم. آقای تارتار و باشگاه پرسپولیس به من لطف داشتند و برای پست دفاع چپ من را انتخاب کردند.
🎗️
«سرخ تایمز» دریچه ای…</div>
<div class="tg-footer">👁️ 6.35K · <a href="https://t.me/SorkhTimes/139046" target="_blank">📅 18:11 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139045">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">🚨
🚨
🔹
🔹
🔹
🔹
🔹
🔹</div>
<div class="tg-footer">👁️ 6.48K · <a href="https://t.me/SorkhTimes/139045" target="_blank">📅 18:00 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139044">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">🚨
🚨
🔹
🔹
🔹
🔹
🔹
🔹</div>
<div class="tg-footer">👁️ 6.34K · <a href="https://t.me/SorkhTimes/139044" target="_blank">📅 18:00 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139043">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">✅
✅
عادل فردوسی‌پور: فدراسیون لحظات آخر تصمیم گرفت سردار آزمون رو برگردونه و به جام‌جهانی ببرنش ولی یادشون افتاد اسمش تو لیست اولیه و ۵۵ نفره نبوده برا همین نمیتونن ببرنش
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.53K · <a href="https://t.me/SorkhTimes/139043" target="_blank">📅 17:13 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139042">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">✔️
✔️
✔️
اورونوف و سرگیف هیچ مشکلی با تارتار ندارن/برنا
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.56K · <a href="https://t.me/SorkhTimes/139042" target="_blank">📅 17:03 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139041">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">❤️
📊
نقل و انتقالات کامل پرسپولیس در فصل جدید
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.51K · <a href="https://t.me/SorkhTimes/139041" target="_blank">📅 15:55 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139040">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">✔️
✔️
✔️
آقا کریم باقری به عنوان بزرگتر تیم این روزها خیلی حواسش به دانیال ایری هست و کلی با این بازیکن صحبت کرده تا روحیه اش رو برگردونه و داره کمکش میکنه تا اون اشتباه مقابل تراکتور رو فراموش کنه و بجنگه برای جبران اون اتفاق
🎙
امثال آقا کریم برای پرسپولیس نعمت…</div>
<div class="tg-footer">👁️ 6.62K · <a href="https://t.me/SorkhTimes/139040" target="_blank">📅 15:11 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139039">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">❌
❌
❌
مصدومیت اوستن اورونوف جدی نیست و جای نگرانی وجود نداره
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.48K · <a href="https://t.me/SorkhTimes/139039" target="_blank">📅 15:09 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139038">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YpQcDXVldaoRjzFDH4NF7kkcDlTcDZEiltKLiqRGfkLAH4AP4v3WUUmJ4gD-VT86aiew0mGDonvLckTWUCck3VyqKqhIBTIYtnVyiz-PELIeJCxbv6LSMyjMXb6yKtxGC2bIeFwV8-1f1jygZBOL_9F3Jv9Gk0uSnGeq9nUxzBQEdJ9SwNWXDm8ebmFK1zXjlcUWyDKs2Z1arh-Al4b8g0dmfP58vem9lSQnyuxuIKFg51ATfKXdx4wpTTBcmInLQ6beI3MNcpMAtQa5oGDssjM12rxwMdNSHCuU29L4m96Km8Aau3ZIazTHcwnt9i9gftCafHuc1fEEV2VvXzVmAA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
❌
با ‌درخواست تیم ملی علیرضا بیرانوند تا نیم فصل اجازه بازی خواهد داشت تا در جام ملت ها آمادگی داشته باشد سپس به سربازی میرود.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.33K · <a href="https://t.me/SorkhTimes/139038" target="_blank">📅 15:05 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139037">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/J0DADCx3wc8bgKq2bzAmLP6tdNLG5wkcfZRu63HDAXoHItBi-JkwYEqaXwZkpUgAwq7mzOye5kwNlAdZm1aDVNwLNTA6rMKgAgLIhnFBE4IJZH6fugvm7XXvtWtP0-PLivj3ITp9NTLBvks9rowrRV7mdNgdnsKLI-XiwAVNc7ZjuHn2rrgVzemTrUYfFVPuyii_tNKUJDNLAQUOVCrpkK2bVG_IeX3WXmnru3hhpOAAkXz4Pgqw-XwV0qERtiIO1O6mJhfiwimvFNCTbqLWRXX6TUN_I8yrvuoLWKNAeARBIo8pRtUCr3nOn_mtWD5uIg-ivU9adjucV6cMWzBORA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
🔴
دو گزینه اصلی قضاوت در دربی 107
💢
کوپال ناظمی و موعود بنیادی‌فر، دو گزینه نهایی کمیته داوران برای قضاوت در دربی تهران هستند.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.31K · <a href="https://t.me/SorkhTimes/139037" target="_blank">📅 15:00 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139036">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">🚨
ویلای علی کریمی توسط قوه قضاییه مصادره شد!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.04K · <a href="https://t.me/SorkhTimes/139036" target="_blank">📅 14:04 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139035">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">✔️
✔️
✔️
مدیریت دوباشگاه‌پرسپولیس و نساجی مازندران امروز بر سر پیوستن قرضی کوروش اژدها کش به جمع شاگردان مجتبی‌حسینی به توافق‌نهایی رسیدند و اژدهاکش با عقدقرار دادی یک‌ساله به نساجی  مازندران پیوست.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس…</div>
<div class="tg-footer">👁️ 6.1K · <a href="https://t.me/SorkhTimes/139035" target="_blank">📅 14:02 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139034">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kgNAg3B9_QguPeChXQYX7FrOuzXk3-qJB9_3XS50uRy2d8HZQELCBvzkNKVVbNR_1A1I8A6VGGtWIMHHfWsNkMqVkC6xG-W6ICC6pxDoL3__EaPa1X8M_ou0II040dlDoHMEbBMTJ5I6rXs5VEdZK4edmiask4rMT6qMoSlkjGVoPb7bDBj-Ifi8jLnH-U0Mna84U5IBiWW6wTMwPtptB-NdZ2Zinx4Ijyk7WMbLz4e7XRXnuP0qrO7OJgyYidG6DBG9A5RRmRp2vEaw4WiA7hPCb1h8V1VH0PyCZkAsoWg7xnxGBRotruntz6n4xlepV5FlRxG5m9qd0wYm2B_dLg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
امشب در نیو‌کمپ؛ زورآزمایی آبی‌واناری‌ها با شیرهای باسک، بارسا به‌دنبال ادامه شروع قدرتمند، بیلبائو به‌دنبال شگفتی بزرگ مقابل کاتالان‌‌ها
[
بارسلونا
🔵
🆚
🔴
اتلتیک‌بیلبائو
]
🔵
بونوس ویژه ثبت‌نام برای کاربران سایت، با شارژ حساب از طریق کریپتو ۴٪ بیشتر از مبلغ شارژ حساب دریافت کنید.
🔗
برای پیش‌بینی این دیدار همین حالا وارد سایت اسپورت‌نود شو و پیش‌بینی خودتو ثبت کن:
👇
2⃣
نسخه جدید سایت:
Sportn5b2.com
2⃣
نسخه قدیمی سایت:
Sport90.bet
🔗
کانال رسمی اسپورت نود:
👇
🔵
@Sportnavad</div>
<div class="tg-footer">👁️ 6.13K · <a href="https://t.me/SorkhTimes/139034" target="_blank">📅 14:00 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139033">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iaS1zz6IiqrxTsvx5TNJBp8sZSakuGKKTycvAItlrGA3xxKp-uHhKdb3PSbMCJiIH4qdBQqqO9Bwb_d0Pql7y4DQgseVKDL5UFezbLIlKcFefjTIt2wnrUS-76T5F9Y_i-grP-jnjAmefqBvqku-4Md1IFzgjVle8uX-fZESgKjvbvaOy7aPEnp0GVHMuEcSeWv_NhUiCCPWOcEv6tDlttKjLOqIxYtQyIg8nWXuvr0_YYdRijJFlBl8EvG2HpnaICEDS8vBTxHlaMB9M-I_KmbzNCDnCWztuACn_uXTofQiTllhSjqWwJGw4UF7xUc5yfTfiFgpstHksS4mcZ8wdQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏅
باشگاه پرسپولیس درآمد خود در مردادماه را ۴۶ میلیارد و ۴۰۰ میلیون تومان اعلام کرد که با احتساب این رقم، مجموع درآمدهای این باشگاه تا پایان مردادماه به ۸۴۱ میلیارد تومان رسیده است.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.11K · <a href="https://t.me/SorkhTimes/139033" target="_blank">📅 13:42 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139032">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">🚨
بلیت فروشی بازی پرسپولیس و ملوان شروع شد
http://footballeticket.ir
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.2K · <a href="https://t.me/SorkhTimes/139032" target="_blank">📅 13:41 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139031">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">❗️
❗️
با اعلام ترانسفر مارکت؛ سروش رفیعی ، سرژ اوریه و ابوالفضل بابایی از پرسپولیس جدا شدند.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.39K · <a href="https://t.me/SorkhTimes/139031" target="_blank">📅 11:20 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139030">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">🚨
فوری؛ فوتبالی: علیرضا بیرانوند هیچ راهی برای دور زدن سربازیش نداره و اگه تا آخر امشب با تراکتور فسخ نکنه نمیتونه در یک تیم لیگ برتری « ملوان، فجر» بازی کنه و باید بره لیگ یک و در نیروی زمینی بازی کنه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس…</div>
<div class="tg-footer">👁️ 6.47K · <a href="https://t.me/SorkhTimes/139030" target="_blank">📅 11:18 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139029">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">❌
❌
یعقوب براجعه به صورت قرضی و با بند خرید ۵۰۰ هزار دلاری به نساجی پیوست
❌
امیرحسین طاهری به صورت قرضی به شمس اذر قزوین پیوست
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.54K · <a href="https://t.me/SorkhTimes/139029" target="_blank">📅 09:41 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139028">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">✔️
✔️
وحید فاضلی:
❌
❌
متاسفانه ترکیب اولیه تیم مشکل داشت چون عمری مصدومیت داشت و نتونستیم از اول بزاریم تو زمین و تیکدری تاحالا دفاع چپ بازی نکرده بود
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.48K · <a href="https://t.me/SorkhTimes/139028" target="_blank">📅 09:38 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139027">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">🇮🇷
صبحی که هفته دیگه این موقع داریم درباره برد و باخت دربی حرف می‌زنیم بخیر
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.53K · <a href="https://t.me/SorkhTimes/139027" target="_blank">📅 09:36 · 05 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>

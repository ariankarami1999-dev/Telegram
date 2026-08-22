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
<img src="https://cdn5.telesco.pe/file/C4yyA_OGXzxTMD1TbEaZwocKFwSyDm-JML8txVZlMWwPQx41CX0TvJCWT1QAafIgJWrG-bUTKgRTaPFat7Ulkam3wnCWNuOC3CuSivyRS85_AqxCmWZ5XTXNsmNk2zhxnhGa4cf7LRRkNPSt7mAmodJQfhouFU6o0d9QTbW8xGJyPKrz6FPykaVfzb5-U2wPWWml-xTfwquAun_X4CtsrDguOmtf58u18XzULFi9WTEMDjZSQx_6ehwLLSwy5yfU4iWw0NW2KOi0Nvt05bItTFxSZK4PU-_-x9a8Dqghx_McmOQ_ts4QHQNOsNipWxlaG62xpdI3aPBRWM32AJBbnA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 فوتبال 180</h1>
<p>@Futball180TV • 👥 449K عضو</p>
<a href="https://t.me/Futball180TV" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 In the name of God; The only popular sports channel on Telegram: All for Iran...🖤We respect the copyright laws and follow the laws, Mr.@Durov...🙏🌹Contact ads:@TivaAds</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-31 22:25:11</div>
<hr>

<div class="tg-post" id="msg-104400">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fc1145503d.mp4?token=H9fD3xrS9vDsGZEj_YsL5u5JsEQX5h07e0CTxQ7ZCNRoFC6JxZnqR0vdIAFHH8qHEqc2hbXXbOjoa0A7ao2tfI6OMGFXTu8B-WoavLDZq3Hoah_8YlVDjhJZ0WN2VRHCSluuICFfy_-P7B2qZcZV7pHY_sh6tnQ9-e2lZPjqwH60v2owYt8KNfUDAOOza7AFpAN56GenTR_qt5NvVoDD1oj1NRg2lAQCgi2d2I-JuMvs62jl-orDciCG7n2zkIMeu0Lms487GHeI3qzW69MoBTx9d69Ykpvxr_PqqrHdTkJ60mJHnRZ2qOqeZ1KGDRTZRJxhURYLRA_F2V-SFuISUw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fc1145503d.mp4?token=H9fD3xrS9vDsGZEj_YsL5u5JsEQX5h07e0CTxQ7ZCNRoFC6JxZnqR0vdIAFHH8qHEqc2hbXXbOjoa0A7ao2tfI6OMGFXTu8B-WoavLDZq3Hoah_8YlVDjhJZ0WN2VRHCSluuICFfy_-P7B2qZcZV7pHY_sh6tnQ9-e2lZPjqwH60v2owYt8KNfUDAOOza7AFpAN56GenTR_qt5NvVoDD1oj1NRg2lAQCgi2d2I-JuMvs62jl-orDciCG7n2zkIMeu0Lms487GHeI3qzW69MoBTx9d69Ykpvxr_PqqrHdTkJ60mJHnRZ2qOqeZ1KGDRTZRJxhURYLRA_F2V-SFuISUw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
🚨
🚨
🔴
علی قلی‌زاده: امیدوارم سال آینده در پرسپولیس باشم
💬
فصل گذشته تمام کارهای انتقال من به پرسپولیس انجام شده بود اما ناگهان ورق برگشت/ باشگاه لخ‌پوزنان امروز یک‌رقم می‌خواست و فردا رقم رضایت‌نامه را افزایش می‌داد/ به هرحال این ماجراها بین باشگاه‌ها طبیعی است/ امیدوارم سال آینده در پرسپولیس حضور داشته باشم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 611 · <a href="https://t.me/Futball180TV/104400" target="_blank">📅 22:25 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104399">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/t8yz5H6oUWZKolgQpvLvSsQsPanMwFFNCx6oFKin0JLY7XqQzGbqtapBWhTmD9r75ag8_NivnQI_tzR8fHyyDhc6ShqEEXp02Tk6SULmdAKnHhnfQ28AUZhWZIYqg_IJ8khmoAerntTLwchoCdZgujXBQFzCtYwYb6LMrv0y_U3kpQC_0tGQkmq6JfFos1zB5ux2ikWEKlA4tSLHVqG4T249SrGIDyKK0LA63ksU6dqgB59ipRWB5LXSIwhq7qwL2kAHLF-C0qQV8extGcxk836DvYoUMv5IG_8xPL65Hf93-iguyXAoyCp61h5lKEHXHgxiUsdgRyCyjSt1-ZQrfw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🗞
🇹🇷
رومانو: فابینیو به ترابوزان‌اسپور
HERE WE GO
🔥
🔥
🔥
🔥
✅
✅
✅
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 2.13K · <a href="https://t.me/Futball180TV/104399" target="_blank">📅 22:21 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104398">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e6d7144def.mp4?token=B2970oZBbPusszyXiQ4HdRtweb3AIvdCZatCuwfBdDHGOu6XJ6nI0shP0tpWaDHaUICoO9udJmepMwBY_cmAw4w4pNHvBFfOr8r6XDUdq8gA7kYgAD6aCdaXTZS_USh6EGAF81bYTlsT_oYHLdcRdS3BB6bQ7XvtEdD1JsYWvfPT7qhMgudWGKR226J009KhZPhWyhoQzt8iF905NobGvghB_9hfgrwIgbJf_czLPGo4Zguwgvxqdrw9kUWvgKbPnAKJxdyqYQw6bSOUDMI6j5d9eJZA-9aRgLtT52eC-U9qjFbC5HLCylVa92-k_Oc3ufdOGTwVf39mfIFo9E9QDg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e6d7144def.mp4?token=B2970oZBbPusszyXiQ4HdRtweb3AIvdCZatCuwfBdDHGOu6XJ6nI0shP0tpWaDHaUICoO9udJmepMwBY_cmAw4w4pNHvBFfOr8r6XDUdq8gA7kYgAD6aCdaXTZS_USh6EGAF81bYTlsT_oYHLdcRdS3BB6bQ7XvtEdD1JsYWvfPT7qhMgudWGKR226J009KhZPhWyhoQzt8iF905NobGvghB_9hfgrwIgbJf_czLPGo4Zguwgvxqdrw9kUWvgKbPnAKJxdyqYQw6bSOUDMI6j5d9eJZA-9aRgLtT52eC-U9qjFbC5HLCylVa92-k_Oc3ufdOGTwVf39mfIFo9E9QDg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
🚨
🤯
🔥
🔥
🔥
سوپرگل تام بالارد بازیکن بریستول سیتی به بیرمنگام
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 3.66K · <a href="https://t.me/Futball180TV/104398" target="_blank">📅 22:05 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104397">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Nc7vuFu5bRSk9yjEZKTfNVdMESzpk3I2eJCJUmYoXEKVQwt452T4nb__B4GM0qZnm0Lmk5j2hB6nPjyRKDB0JwwrdXYmPNux_QKXduwQDQxEh2fk-WuaC4E08NY0_mR3tGH03GFcmk-ucvslCAitbYbDsM6fPOFhqin2B4WszpdHDfabBG_PNCqWTs1bJjXvPm7aN-9aJe9M34yEHl1uATWPHL4S9Q0jOOJtcyx3s329ox-V6eqIged4dQgI3mKydxHDsuVeAN-wY8un8sALuvQli2Tx6RVHclji_ixpSQ_gFZ0rCMymO5HZvxeFsZ4yRw2eEx5UX5surj2weN4Y1A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
🇪🇸
هفته‌دوم لالیگا؛ ترکیب رئال‌مادرید مقابل اسپانیول؛ ساعت ۲۳
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 6.1K · <a href="https://t.me/Futball180TV/104397" target="_blank">📅 21:49 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104396">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/e6JkBcYMcETTqyDwFUgS67Mfg9ff-m7RyQDvmqi3aRc7KXNTHYXIUEHyGEJDP6-MdPkfEpx9WA6WqgVvUXnwSjAaqGnWin0Y0xnPAy5c56C3oLmnBRkg0Aj9csGY0zw3kZjCzchUylMLRrf0IWQmmHYpCSIz47P99YqE2kGUF6dXCvmO5_teJ10oFbXCxYrOoj4NOHXn73YoksftD0TtJjKxlWm3zJAcDJDv40Vi7l94o3R7Nbu9W7FceuevKtxksSKuhyBn4WOza2ED9nm6O0bNCGM0inER3ZGFjjyMyGDa631DS0xUoT5TBNbBLxJ6zVwjY87KhR295nOr2JLZKw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
🇪🇸
هفته‌دوم لالیگا؛ ترکیب رئال‌مادرید مقابل اسپانیول؛ ساعت ۲۳
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 6.1K · <a href="https://t.me/Futball180TV/104396" target="_blank">📅 21:47 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104395">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/usDS8M-ieiWb6EGifjBzggAo677Cvwhao8Lm1mzfnQJKtyt72tKAZDQjhe2xnlaqhW7xBOh58ZwZSlRK0zFU2bmfvTfdTSMIvPElsfBW-ZkQIOwYbbLayX4zZawtfI1LSI2Mr0_ZAi7yricMV0Jd4657lCKcy82f5Fba--RTZ_NKEXtxHgNmbS7tI4e_pvrhOK7DfCgRbNxDDxwYB8G9FQCq2ZZm3r4s3l5Zi0Q3JUAo5kwjb7-ysJaa8lPzXLwAFfX5TKBn2iazJLiSlfELfiMtK6HXbqS6VK-WuV_M24Wesnkq8whfiG3QlPLPhoeJu08UsKLaoj33nC-1B02-gw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
✅
🇪🇸
خولیان آلوارز در لیست اتلتیکومادرید برای بازی فرداشب مقابل ویارئال
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 7.19K · <a href="https://t.me/Futball180TV/104395" target="_blank">📅 21:38 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104394">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dauRg_y5b7HDAQggnknT_bEvN68lrFhXHQ_Zqor6B5WiA9oxALVV158rmLjgwnqwVR76QQfCDBHz2JW3hcPrmoaw_mMkfLLISwJdmGjhVUDV8CgDd57h8e7igzsnWkKCLouv6OSNkFvJirSV_YcY2dCgQrXZX_U9F7Q7iuWi2TX4MVkVZ_iJ2sopvqG2jKlLiVFqHet4B9fUL6VgOHhJYDjblBIt6C9wI1NNOvW622mfaiZF4zWW12zBq1wau1VK2X1gT3Ap9zucKaTsSBBmsy1CuF7rnu8-XjF7I28qAeWLmxfTh3AIqeh4D4L_hp9jY3lLGrid1etTkStZvRYKTg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
🏴󠁧󠁢󠁥󠁮󠁧󠁿
آخر و عاقبت تیمی که مربیش کصشر باشه و با ۳۰۰ میلیون یورو هزینه بازم بگا میره
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 8.84K · <a href="https://t.me/Futball180TV/104394" target="_blank">📅 21:12 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104393">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IOSQov7Qdt0SLYZHgyJaNBMLxNAkYE9DfGrIA4jI64uqNgGad1vcl2Ym0pTL1AtCexh38hoSA7p2fOnTAdKOCQdUF96g42iMw7_otiwEs4nypwxH0xFYCuyIizSL7_kMWltpdv46wXll2UFFmzQhA4gXjrdY0bZX3lnuLyfKW1dW4WOnJ9TS-PvT6iAHUX_5LbEisv_IBYBWUG81VHOjGOvvKngIaJteUNN6U3Xs0RHxIL5bz3Vx6l75wJUmHAW4RzxNIb9Y6pdCiHUSxLG8n5xhINJxSnSm-7UjF6wJqeYrvDYWIozleEwEDim_lbpzt28qPlV46FFtzuN1G-WlDA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇩🇪
سوپرجام آلمان؛ ترکیب دورتموند مقابل بایرن
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 8.85K · <a href="https://t.me/Futball180TV/104393" target="_blank">📅 21:02 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104392">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Lz9qAKRApH_PfkxtZgbYEz6Pl3IWQLr7XVNaGjoHYNthKLLcrrq2jZ6FtRmL9aUOgCB4LxDrDIRv3CqnTgAdYgsNuiQj_XUwaFXulsB_W-apBcVkr_CiYr1a_GKGn8vMeORKoKfA12GXrI33wEq7zY62SHRIazLvCmXTmAvIU4h31BG7t98Vd5WmAeLyEEcGlmWVntUhWbzlvWzRLVCUPZFTF7aK9-IitV1pI_ercDcBfORlOUDguwon-aU0_CmdYrfQfytXNSyQn7SJMdQk-kDDZqbPlkKtQdNtUHVtX0tkLDHgFEc1Z53drQOOL26FHmCLCAT3UoU0GjTB191Gxw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇩🇪
سوپرجام آلمان؛ ترکیب دورتموند مقابل بایرن
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 8.82K · <a href="https://t.me/Futball180TV/104392" target="_blank">📅 20:58 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104391">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8f25fa8009.mp4?token=K0NtIVz-5quC4vXCplkFSIcEIvmhklHvOd-rYTiOHz6sMe0fd0LEBMMAPWT-QnrjvQpe5kdF6pcV261cGGNy3zL28nrxFQnqOznFz-Sk1QjEdKsz3M6Xs_IHTSqVMIABBecHZ626EKo3GYs0ub_SMHEbQOvEL5O4TpbYmzKhLD-D47RQUUI0weYOXJllGy8SmfYGZDW5Y_nkyGZTUqsPkkki5PFhdtM9ee55FyzTFIZ4aDEsByxQ5cnW26vSfDGLkG2vLbDTexScCJ3nOK7zZIAjffMW8ZdLpW33yC5Y01Ufx3QDMNemH58DSP64TJTiDy5U2ZZBA35fFzPBhJN4oA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8f25fa8009.mp4?token=K0NtIVz-5quC4vXCplkFSIcEIvmhklHvOd-rYTiOHz6sMe0fd0LEBMMAPWT-QnrjvQpe5kdF6pcV261cGGNy3zL28nrxFQnqOznFz-Sk1QjEdKsz3M6Xs_IHTSqVMIABBecHZ626EKo3GYs0ub_SMHEbQOvEL5O4TpbYmzKhLD-D47RQUUI0weYOXJllGy8SmfYGZDW5Y_nkyGZTUqsPkkki5PFhdtM9ee55FyzTFIZ4aDEsByxQ5cnW26vSfDGLkG2vLbDTexScCJ3nOK7zZIAjffMW8ZdLpW33yC5Y01Ufx3QDMNemH58DSP64TJTiDy5U2ZZBA35fFzPBhJN4oA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">این حرفای گواردیولا رو گوش بدید و عمل کنید
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 8.89K · <a href="https://t.me/Futball180TV/104391" target="_blank">📅 20:56 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104390">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/V4ecEwD6StIrpt8XbFP8B90Tjl_ICBd715USYqAW3Bgksc8Y4jminaWS3edJ38BGuS6A_NvJgK4oJBEnMS6Z06AWShNRYWGmBhOgrqsocvnoyJ6VXMdinzLuIj5sN2qfm7RY6wj7UQW9DkGaktl-4XDAFpkJ25NmHMBdiEhFk03JVnEMwEJJaqNdfEPiKwAy-kbN_j7hdu8YFT77wv-EDEP958bcXhumhfOvYrT3MT_ZC4RPqnM4JKES28ACQAvNT2B_87S9fYEz3XxOsz5Xe8wfaetWhGMwvqvsdN9SZ7_bPeNzwQzHdbq0PTeGzPM37iXN7JxCPIenCnj5vpI2sg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🇪🇺
لژیونرهای ایرانی حاضر در اروپا:
🇳🇱
علیرضا جهانبخش: اکسلسیور هلند
🇵🇱
الهیار صیادمنش و علی قلی‌زاده: لخ پوزنان لهستان
🇷🇺
محمدجواد حسین‌نژاد: دینامو ماخاچ‌قلعه روسیه
🇧🇾
میلاد محمدی: ویتبسک بلاروس
🇷🇺
نادر محمدی: دسته دو روسیه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/Futball180TV/104390" target="_blank">📅 20:14 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104389">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dba53081a0.mp4?token=a3WQ-JTuweHlqa77sHDdIu_5B2vGbnJ-M43Qi6d1h0tSg4jLqxxC_hdvRYdqS6T4wzmzMsY5hFv-Y_LDDM1j_kqrVTb2PdRWyaa18Y2MhoICrtmOhJ5br0kF96ywUtjfuzAAUhOhu2FNVFKcrQi6y99O13nDorIweYzrCawzCvwM-qkuE1ZdjIhseYoMVjBHq4ELg7PXuObNOQaKRS3mvjNxT-yf276SezfS4JINOq012Yi_H8QHMD9nvcSbeJ9SDIAK32R_F-S1umkeIGrU6ufWLOQQPofRDpGRg1ZYtmUD20Qi_Iv5tckwVMLrNTtSekqYUFp2jl3LpRASbI5KyA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dba53081a0.mp4?token=a3WQ-JTuweHlqa77sHDdIu_5B2vGbnJ-M43Qi6d1h0tSg4jLqxxC_hdvRYdqS6T4wzmzMsY5hFv-Y_LDDM1j_kqrVTb2PdRWyaa18Y2MhoICrtmOhJ5br0kF96ywUtjfuzAAUhOhu2FNVFKcrQi6y99O13nDorIweYzrCawzCvwM-qkuE1ZdjIhseYoMVjBHq4ELg7PXuObNOQaKRS3mvjNxT-yf276SezfS4JINOq012Yi_H8QHMD9nvcSbeJ9SDIAK32R_F-S1umkeIGrU6ufWLOQQPofRDpGRg1ZYtmUD20Qi_Iv5tckwVMLrNTtSekqYUFp2jl3LpRASbI5KyA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
❌
🇮🇷
حمایت جانانه بهتاش فریبا عضو کمیته پیشکسوتان استقلال از رامین رضاییان: این‌که چه‌قدر پول بخواهد حق طبیعی اوست
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/Futball180TV/104389" target="_blank">📅 19:58 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104388">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f2fde5e301.mp4?token=poaZx5bOshnLl8PHQYjDLoIKuyPF0EQeimAhF4rn4MEsa8tqzzS6k0SYAUASgx0lFyKoY2oP97xhz_GbltlWPxwPDlGnC-IMu6MEhyAVq1Q0EbEi53AxL4wjWaZ7BkJoaCzcNDmycRaHX6_GXUpszGhAPEBKzkt9YUk7g-DCMQPlbOeosFV5wxK1x5t5SsVURUGWFlwPb0RDoNodLJObVZFV2mboEOywiL0A5_HK4Bhto-HstquLtJPIyEvWC26qBlnBSYo3apb_zFMunw7vLYgNw1rAUYl96GonXynDlaLMWApKB5NvjAaf9-VqVzTOwS8toE2qHFzM_7CVc2J8DA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f2fde5e301.mp4?token=poaZx5bOshnLl8PHQYjDLoIKuyPF0EQeimAhF4rn4MEsa8tqzzS6k0SYAUASgx0lFyKoY2oP97xhz_GbltlWPxwPDlGnC-IMu6MEhyAVq1Q0EbEi53AxL4wjWaZ7BkJoaCzcNDmycRaHX6_GXUpszGhAPEBKzkt9YUk7g-DCMQPlbOeosFV5wxK1x5t5SsVURUGWFlwPb0RDoNodLJObVZFV2mboEOywiL0A5_HK4Bhto-HstquLtJPIyEvWC26qBlnBSYo3apb_zFMunw7vLYgNw1rAUYl96GonXynDlaLMWApKB5NvjAaf9-VqVzTOwS8toE2qHFzM_7CVc2J8DA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">عملکرد ریدمان محمد صلاح در بازی اولش در ترکیه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/Futball180TV/104388" target="_blank">📅 19:58 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104387">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromBetegram</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SbEzuPs-Rj1dgOtAw3r14mz-PWU465w9xGqLQ84eu2taom5rFtfuz9gsTXl7l3bxOBZDtWFd5QI15Mc10XJ46w-k_6CWj9V4SZZePK0egjEoTLpVmCcc3_edg90dqG9szLdgi6jk6isIGNtWHy31WX3lKT6BJpQPb9AuuY97gaAnLKucbsS14qjahxtZrtWzUhi0Vg1-lHH2lD5soRMzCN8wUbF-tFtMyFtTP3mGzP_nz5lqCqO17OyJNk1cFqV_Y84aFd6EroxzQkI61LctQIX0hFLfnCOkkZOYRLXxjKt_lRCDXYEMm_SYIYZn91GdoiOWjOoPdtgFQARe_e8vqg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
هفته دوم لالیگا اسپانیا
🇪🇸
اسپانیول
🆚
رئال مادرید
🇪🇸
⏰
ساعت ۲۳:۰۰
🔴
بیش از ۴۰۰ نوع آپشن پیش‌بینی برای این بازی در‌‌ ‌‌بتگرام
🔼
با بالاترین ضرایب پیش بینی
💵
واریز و برداشت ارزی و ریالی
❗️
🔥
۱۰۰٪ بونوس رایگان اولین واریز
❗️
🎁
فرصت را از دست ندهید! همین حالا پیش‌بینی خود را ثبت کنید و از بونوس‌های ویژهٔ Betegram بهره‌مند شوید.
🔴
http://betegram.com/affiliates?btag=3_l7</div>
<div class="tg-footer">👁️ 9.35K · <a href="https://t.me/Futball180TV/104387" target="_blank">📅 19:57 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104386">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/54d02a0a5f.mp4?token=pNoEEctvo8OFTq-eO5pdxpz3Mxh8D3nL0JPnrZw6v7LmyiR6fr2nOZcU9ddM8M3PLozu0kLYwp1erR-8mh451WB3Qyoajez1NeHIgZ2_4uKy-4N6m0oga1I1_zz_8LubORSq9d7Z5fFUtZ-EJrR-DhEIbSiSzOnZ4Q2KYJSnbrPlEPiKt6uEX8EuSmKJ6qVwucl1fhejadwdN6QwyHsjz1YxRjx_r_vVwccOpmAalrBm-ocMaYrgSbtyYRdRdwvIX3M3yOn7ignPnUYQ5PDUi8f6I4At43jP0fneK7uE08n5-W0lqYuxQ2sRAXIz7N3NeIzmX4sk6mH6lDBTqDba1g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/54d02a0a5f.mp4?token=pNoEEctvo8OFTq-eO5pdxpz3Mxh8D3nL0JPnrZw6v7LmyiR6fr2nOZcU9ddM8M3PLozu0kLYwp1erR-8mh451WB3Qyoajez1NeHIgZ2_4uKy-4N6m0oga1I1_zz_8LubORSq9d7Z5fFUtZ-EJrR-DhEIbSiSzOnZ4Q2KYJSnbrPlEPiKt6uEX8EuSmKJ6qVwucl1fhejadwdN6QwyHsjz1YxRjx_r_vVwccOpmAalrBm-ocMaYrgSbtyYRdRdwvIX3M3yOn7ignPnUYQ5PDUi8f6I4At43jP0fneK7uE08n5-W0lqYuxQ2sRAXIz7N3NeIzmX4sk6mH6lDBTqDba1g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👍
اقدام زیبا و تحسین‌برانگیز بازیکنان اولسان کره
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.86K · <a href="https://t.me/Futball180TV/104386" target="_blank">📅 19:52 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104385">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/UDh2pgpSk5T3U_syxEk6bSZ_DRSTxRuRHg12Bv0qtdFcbxY68W2hFhh14KKxJaE63BYi7PnTVcgVxEzNXAlYy6nVaCb9FDTb0sd0ipfN1goGx14E3FjdcSGhrl09gphCfxjNOmCJ3WnQ0Fkp2M9-l-4Mu4BqK32imaVsBMyDMfMvG5cFfIj1AXTLHVA8oCwYHyo_Sz3Yx_0ppq0qrAT9pKLxIUUHZ9I9hZUVDuaLM6Xe3-wPdzmz6n2ddcTET1KJEXBAy9Yt0aNX5UEpjPFw3b9_-VHGflLj1StR4SstG9We-LUbw8_dPKisRq90v4TephV_OUY9QWoSYhgw3yNzPQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🇮🇹
🇪🇸
#فوووووری
از رئیس باشگاه اینتر: بهتر است بارسلونا خیال جذب لائوتارو را از سرش بیرون کند چون هیچ راهی برای فروش این بازیکن وجود ندارد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/Futball180TV/104385" target="_blank">📅 19:40 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104384">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f33114edb2.mp4?token=Kuzg5hbW0eTFX4_CeWQRyGhqdHGfVNtBoH6EwkXLGzVYqnpqrsJKnBoGGhSARywOINrkfykjEsxKRWVm8VcJvAXYmLZ1UoGwuTnzM7qd92vdq0OjTMBnPRtjWLlLSjs_5j5SIFVN8aigP-CTxvRFVZRsq0_v5e5A5y3yMH7DVnbZSnlDoerm1szFDg5xaYQ-8aOioKRsu3lwnx2WMjk8hto7_oS8G3f4XglOoRs7qo2C2Oq2jweUdV3ZUNznRV4hM1a7vFy_R1_EKEY0LjSaMF-AlcCEFsbdqe5pIAAI6hBfOsF2UbLw75bqg4EPiNWdWCFTCx05vO3CKcQG1PMPow" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f33114edb2.mp4?token=Kuzg5hbW0eTFX4_CeWQRyGhqdHGfVNtBoH6EwkXLGzVYqnpqrsJKnBoGGhSARywOINrkfykjEsxKRWVm8VcJvAXYmLZ1UoGwuTnzM7qd92vdq0OjTMBnPRtjWLlLSjs_5j5SIFVN8aigP-CTxvRFVZRsq0_v5e5A5y3yMH7DVnbZSnlDoerm1szFDg5xaYQ-8aOioKRsu3lwnx2WMjk8hto7_oS8G3f4XglOoRs7qo2C2Oq2jweUdV3ZUNznRV4hM1a7vFy_R1_EKEY0LjSaMF-AlcCEFsbdqe5pIAAI6hBfOsF2UbLw75bqg4EPiNWdWCFTCx05vO3CKcQG1PMPow" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚽️
گل‌تماشایی ساندرلند در مقابل ایپسویچ
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/Futball180TV/104384" target="_blank">📅 19:34 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104383">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AjvZgtMAFNlHIG5zatMfh1xbiUffuB7RrX9RxuzlBPr_FQm93exU_wgD-D0p7dDNaKc1fsse-okt__-2CSyqlHxwM_Rm1kDQ1PaHqi8WOA_MXW437KpXTGe9MOjZ4EnaOjPqgcgjo3PwSH8d6elhLyvdPo-PQFjNwBTpb1pxtmfxlwM4SybTrJMxMUWKOZNoo38V6n4lv9XF5IfjkQWBtZ7kjMIG_EIbv6T-o_J9lX9y_dq_nR1A0zuGCpAxPYVGjdKff48iT75IeCHHQNoY0Db-G3_FVMQ4nUYtUmu0LT0ooo7MPcwIao5mAhLXPyLs5665QOPt4B68Yt-zkyextg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
🏴󠁧󠁢󠁥󠁮󠁧󠁿
رومانو: دو تیم شهر منچستر به جذب بالده بازیکن بارسلونا علاقه‌مند هستند
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/Futball180TV/104383" target="_blank">📅 19:33 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104382">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aqna2Y4Q3Y5CfdxUHZWzpKBKSOfKOoTo1WPrT_xNezo0pgoBT8EyFvaRZti0rn3Tg2YKt3q3w70kbTGRcKSZa5y2j0DhEVIYx43yH5jd8EIKEMqodKm-bza1CQydEJgPBiZBABb5vcWxFzUP9USJ33pAkcD9xOy5JCTqnc6nVmzG-A28YzgdvXBAOvWbl8qiAFL4mKoJmJmLp9vuS8EY3Tza7Oyy23Hcn6wCfR6B4SD_ulrgVKK5jNtu-L3xF5EwgCW-egGOo4bRT-Y4Zu4Z3FeqU5p5bAlv_tswTgopdqmxcRgTtDaWmATRVTX5053Hjrh6JkCdJZExS8RHlWz0eg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇹
هفته‌اول سری‌آ؛ ترکیب اینتر مقابل مونزا؛ 20:00
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/Futball180TV/104382" target="_blank">📅 19:23 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104381">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/45250f7e28.mp4?token=sQ6T9-x1aSmiBs1ihT3ZmoP2rsR6NAdB6_SlXGgEVjdN5fjzmaTh-XR03Wztzn9lqSJCUCiWFE9aRmFfNxms8Wz-lcY1gWRe6WpWo8fYi1TFBK1i3sPwB7Y-jbC0T1KNjBd2NSOP4evxEZiCJo4niUI01aNdSvFY8kVPTnzclYqQ_xO_hR50B8B_WJH9-LhwuSYZ5eNpj0qoysOrFWnHSZpeW97quZnF8IcIg4LjuHs1YCZa1Fg3_LRFuQy8OlZNeRl4Ow5a4oKkalAGHjAn9bpNMVfCWA0GWHhUn9kyboJLiiGAKtco0LrUBJBkVp8P21gp-2t6WimCLBwojmWmWA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/45250f7e28.mp4?token=sQ6T9-x1aSmiBs1ihT3ZmoP2rsR6NAdB6_SlXGgEVjdN5fjzmaTh-XR03Wztzn9lqSJCUCiWFE9aRmFfNxms8Wz-lcY1gWRe6WpWo8fYi1TFBK1i3sPwB7Y-jbC0T1KNjBd2NSOP4evxEZiCJo4niUI01aNdSvFY8kVPTnzclYqQ_xO_hR50B8B_WJH9-LhwuSYZ5eNpj0qoysOrFWnHSZpeW97quZnF8IcIg4LjuHs1YCZa1Fg3_LRFuQy8OlZNeRl4Ow5a4oKkalAGHjAn9bpNMVfCWA0GWHhUn9kyboJLiiGAKtco0LrUBJBkVp8P21gp-2t6WimCLBwojmWmWA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
🇮🇷
فوتبال روان سپاهان محرم نویدکیا که با چاشنی بدشانسی همراه است...
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/Futball180TV/104381" target="_blank">📅 19:22 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104380">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-text">کانالی که همیشه در مسیر ورشکست کردن سایت های شرطبندی حرکت کرده!
😈
آمار ثابت 90 درصد برد
✅
فقط کافیه چند روز فرم هاش رو دنبال کنید...
⚽
@Tipster_Mafiaa
@Tipster_Mafiaa
⚽
@Tipster_Mafiaa
@Tipster_Mafiaa</div>
<div class="tg-footer">👁️ 9.54K · <a href="https://t.me/Futball180TV/104380" target="_blank">📅 19:21 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104379">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from𝗧𝗶𝗽𝘀𝘁𝗲𝗿 | 𝗠𝗮𝗳𝗶𝗮</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YdSIgaAj6J6AmZMMR-CB_tl-Vm595zMsPz34tLSxF_L4AMAxs41HVvniWUVSyc_YY3a6LQt7hWMXfqdgzK2lqc7wDh7ivxe6QC6gBcMCMk57uZnurvXEwe4oQHbJSQtFDsmbPC0jNZN7pBLTfgz7v8iPxV1obdJ30UVpB2VJ71Y4afMxIv0opn_KA-qfnahoHe_xneGnglqIOCt23lDa7DRiv0YQn23mUo-ZMM_gmEEFBquW8BiOpQn7hSlQtA9LDpmDGGOBu2QcnrTLHpybUodvy0a7pchSGJIvPCN-RZSCrQLupECzEE1Dxrw11D8YX_em_Kg2Zamd-Mw-PoseMQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">میکس عالی برد شد
❤️
☑️
✔️
@Tipster_Mafiaa</div>
<div class="tg-footer">👁️ 10K · <a href="https://t.me/Futball180TV/104379" target="_blank">📅 19:21 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104378">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/86b7ad297b.mp4?token=uyCylxNiF9cUFPbSaHJmBXFunfkrSia8KDgF_aKVIhnrHyhYACZp3BFNi70QAQrtrLQnVOZly3ilq4DE-cicq7Z4xluPNddyd1m5UwPprjAXGEahXY58e5xRkwUWJ79nQD6cKcC98_sYWxEwCSyIswIeBKAldr2t8vovkbQUaaI0qPwxFZSYM-ON5-6pH-PbHN2JWn6-VASwb7u3crPyG868E7HZ8rdEMFUwOzVQvHle4Tl7AXPbcBdiUa3vYQkDTaAvI2q9zQXDgMvhfZBsiWqF_OnqKHmqG8oVXm4POUg4Dw3WCmisHTkY8WaEDcaAluMKeWcyzRueBlbCLIfViw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/86b7ad297b.mp4?token=uyCylxNiF9cUFPbSaHJmBXFunfkrSia8KDgF_aKVIhnrHyhYACZp3BFNi70QAQrtrLQnVOZly3ilq4DE-cicq7Z4xluPNddyd1m5UwPprjAXGEahXY58e5xRkwUWJ79nQD6cKcC98_sYWxEwCSyIswIeBKAldr2t8vovkbQUaaI0qPwxFZSYM-ON5-6pH-PbHN2JWn6-VASwb7u3crPyG868E7HZ8rdEMFUwOzVQvHle4Tl7AXPbcBdiUa3vYQkDTaAvI2q9zQXDgMvhfZBsiWqF_OnqKHmqG8oVXm4POUg4Dw3WCmisHTkY8WaEDcaAluMKeWcyzRueBlbCLIfViw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🙂
هیچوقت این صدای تاریخی استاد مرتضی فنونی‌زاده از ذهن و خاطرات پاک‌نمیشه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/Futball180TV/104378" target="_blank">📅 19:05 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104377">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lGgS4fEfouQQHswEYHcC8vGuSCtEOnUWuzBX1yCnr_nskby_U0byJguRzN_SDwigLMtPtLcGJYQL4lImub4rNHOiL4Gq--GkI-nHzT22nPKyeQCEV00gTFxL_HhzkcTVnUF4J9IbLlYYBgoeUiDhTh_eJUPKeAwm3n_QwjE2u6XtdVGghYMOsqsCjDXIMLFKBmCYH0qd7fg7rtKMNYma68t6XltccBQ6Xt34V4oY0u4CFkHp_PidZ4KlLSzgVG4mzBKZXjKIL6ub24EhtHFE0YVNEow48azknl1-V8VtIOeYNgiKIz_Is0QDu2s8bPcYOpp-0AxInQKoh8GxeU9_eA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇮🇷
🇮🇷
پوستر کنایه‌آمیز گل‌گهر سیرجان برای دیدار فرداشب مقابل چادرملو اردکان
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/Futball180TV/104377" target="_blank">📅 18:41 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104376">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1ed1c9346a.mp4?token=leGHl_LZQMPo91GRcyviMer9KnF-ERF8rLCW9sCOI4Jho_v4Q_PUxMzEJZVCeglPL7ZH-dR6fHD6q0eclU1JDBZGeE1TPqDyaVy9GE8DBcs3f8pcK6pXdRVuu99Xwbnm9e-u5ZCwFFuRScE3wsllGbKf-9EoLa8jNNBrAke_J1pJk5leb-zJYZn-6oYOhmtAd1BVlww2liYPeGShLkQCDFEC26y8KDT_gBujpSbjgmnFrsTSXVf0ni1JwniEjqC_2x-6mi0jTYb-ylEczeyIl08kbKSOtO5EECR-UtSff9CMpewXHYJ9LPZl6j1n7WeaWjVLrJjnzZaie_gdek9CMA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1ed1c9346a.mp4?token=leGHl_LZQMPo91GRcyviMer9KnF-ERF8rLCW9sCOI4Jho_v4Q_PUxMzEJZVCeglPL7ZH-dR6fHD6q0eclU1JDBZGeE1TPqDyaVy9GE8DBcs3f8pcK6pXdRVuu99Xwbnm9e-u5ZCwFFuRScE3wsllGbKf-9EoLa8jNNBrAke_J1pJk5leb-zJYZn-6oYOhmtAd1BVlww2liYPeGShLkQCDFEC26y8KDT_gBujpSbjgmnFrsTSXVf0ni1JwniEjqC_2x-6mi0jTYb-ylEczeyIl08kbKSOtO5EECR-UtSff9CMpewXHYJ9LPZl6j1n7WeaWjVLrJjnzZaie_gdek9CMA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
👀
از حواشی کمتر دیده شده بازی استقلال و نساجی؛ عصبانیت سهراب بختیاری‌زاده از حبیب فرعباسی بابت انجام حرکات خطرناک!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/Futball180TV/104376" target="_blank">📅 18:32 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104375">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6820414d13.mp4?token=sfqJN0zpvsehJDy-quZ8Fao7iWPKcCYB2JXS_rRPJ9XRWAKYEAoiJAT6tACGIiD2RH9lH6YCZEzwz5dNgA-8-a9K1aTPU2v3IM0JW7pE0qtzwNPKNyEEp_cx17TUj-YPyf8ipT9x_yXrQ8fZW9ehI8v3fqhqAiIA-E_JMCooxOp9h9ZW8rRnKgt9CBjXQ52WuMJzF0jwljCq5pPYlknmpClR0gnj7IKn_2StU5eGBtFkqkIBEBWKtpghfeRoYNrS5KvV361vT945k2VOESJfU9Ck9jopJdP2HL0IfRlRqh0BOofsaoBhGYfr9nzWviNTA0ksQw9kaLkUNOUeQ4e2wQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6820414d13.mp4?token=sfqJN0zpvsehJDy-quZ8Fao7iWPKcCYB2JXS_rRPJ9XRWAKYEAoiJAT6tACGIiD2RH9lH6YCZEzwz5dNgA-8-a9K1aTPU2v3IM0JW7pE0qtzwNPKNyEEp_cx17TUj-YPyf8ipT9x_yXrQ8fZW9ehI8v3fqhqAiIA-E_JMCooxOp9h9ZW8rRnKgt9CBjXQ52WuMJzF0jwljCq5pPYlknmpClR0gnj7IKn_2StU5eGBtFkqkIBEBWKtpghfeRoYNrS5KvV361vT945k2VOESJfU9Ck9jopJdP2HL0IfRlRqh0BOofsaoBhGYfr9nzWviNTA0ksQw9kaLkUNOUeQ4e2wQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🤡
🏴󠁧󠁢󠁥󠁮󠁧󠁿
آغاز قدرتمند منچستریونایتد در لیگ‌برتر
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/Futball180TV/104375" target="_blank">📅 17:47 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104374">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/L2QGpjKjmFf2G6mpcUVQatJwk-xR4ZZ7Kc70MwKj74D6LAFIt8-OKVvueFjsi7logdBlH5XPVNHD0WomhqC5UKKwBRSspgkiSC8BD6sBIrIPPi_GTOata6byF6f6OqII2KpCtOUooGQy1kYU59NY3V8hfLCJ2MZDs81d0-SnrY9r7TbdT1yUaNt53grnNtQWtgIv0QAfrLZ7tkAFFGnl4aCWjV6QJtLghhj8-5Z0LFzM7gVED10Aic6odNClpB6RHxn9oyePa2K83OjmJAfR4jPwKfSfY_bp-Yc18uYvlPk1Ui7Zrc7E8oeAaTglNSFRb_3Va3fktqqeig6L9Hltgw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🚨
🇪🇸
#فوووووری
از جرارد رومرو: آلخاندرو بالده مدافع چپ بارسلونا طی روزهای آینده از جمع شاگردان فلیک جدا خواهد شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/Futball180TV/104374" target="_blank">📅 17:27 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104373">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VyJ1lDPoOUYJpYAvnEF3ZV3xbQBwZje1PGL1Nj2oJ9GH8h1HVCFm54nydpD9XnQB6nshpofEvL_AQJp0xBiBfUB_5MlCGTRKFIUjobHNEYjdvSvsH88WhkCNH7Hs8HNnOwiIHnMvxHB72iZu-FeTEHXAmRENQI3Z1oVk_eNqznSOJ9Q0B_y-mrNgqYu6j1uIAhZYt9hk_LdnRSdQPufbPnbQqqKQIuJg1L1gA4FPhWwH-FdEPvl6lMZsIrhboGq1_qG4W_-UR8i6vwPlWFQMYTuWcozx3kIS3bRyKmxYRG49DaCtyhF4bjHCGfQXSteDWzSwe0t0AJTG8zY9OT_v7w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
‼️
📊
آمار پشم‌ریزون بازی منچستریونایتد که با شکست شاگردان کریک همراه بود!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/Futball180TV/104373" target="_blank">📅 17:21 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104372">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CO_DYQPwagZcU82Xr7qfy47Ry2UYnRMKULyAcPwDwWM4AwCU8ZHCE8EUwK429TUA_8q8xX9HjhO8t8KV98KekS775Fz-TiIwwvxVOBXWcuiDZtipk0a0Vdvv8H0V0OwXS4g_cbD87YuJ-_uaMP1LSdW-fzsqeQZIs-4KNnSIeH62qjHVPeFzBsFxnKZMoSjcu1LDKSCnswMj1rWjghCAwm-XrRV2nVLQqBX5VNGCSCMAOkqHPpbV9hKkzzHfNwiQ-6Rd5nfbtIjxry6theW2Pz8vaWyHv0r8IH0p1uXw_kKcX4ax4EZBJvO_nUWAbtW-nlAzj1yMr78R6oa_7cEnhQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
‼️
📊
آمار پشم‌ریزون بازی منچستریونایتد که با شکست شاگردان کریک همراه بود!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/Futball180TV/104372" target="_blank">📅 17:12 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104371">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uCmppvx27nUZ0iDE3NrzrNrrYfAqty5cjOT9Q6bLqNG9xVWamswtFOKt2dgoTycincDjvzE7rV-aenIh1OORSUztix8yXzjL4xUMNzGgTQAXg6tFq_4HXXqwrQBrjXunFEFnt9VC_9kfvm-78lYaTWHcLQ8b_xdP0x3mCto2__UzZ59xbo2Mm4dwyrbwH_RZjuiLO4Qw29HchHzLLjhvLhSO7DpHBxApLHpJR7N3AVgJ_pr60eq8Eo-y1SZIuqzX6ORuqu43rPYFW5P3LF-t5qh1Xtis66QgDVhawl4VQazrHsrs3SQMOzJw-YpRLfmeHYuGYeXn3oP-Ow_XIYnudg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
علی‌علیپور مهاجم پرسپولیس و همسرش
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/Futball180TV/104371" target="_blank">📅 16:55 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104370">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UaArx1f21MIqvSSw0bNqd7nI6JkFW4Op0UJhKpD3EQazJh74aBLlRu2GX43f3cJ9f2LCrrpEKt6UJB_wecT7y5EKZwAseR33ecn0Hwjo9XuQcS146778R9Awiwx-1mNFK16tT2qsW_V3BQmUB5rxvXnVwzBVSFpZvlqc4ueIjxJH4B1qSa4dxB22yFlIGknBlg1DwrRSbAQV4BxMt53ji5yLgZa18rj04IcOf5MJttRoj-hFHF8fNdAODd6uYrp8IJ03-J0-OkvSE3BQa085dTD3L9-ptvJZJEiuH-socVZI-QJ4fuBJbYHwLg_Ge_mJt2tJpl02RNK_LEj7d_5ECw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
⚽️
تغییرات شگفت‌انگیز سرمربیان بیگ‌ سیکس پریمیرلیگ تنها پس از گذشت ۸ سال
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/Futball180TV/104370" target="_blank">📅 16:34 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104369">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1a75f897a8.mp4?token=gmEqO8ckQKsUBQU2V7O6LazDlH7wyOPBRequVdXWgBIqiE5hUdncqU5P4-dTfP-P3q30ToQtn_a2HdD27I8hNOQshtPDL2_ZU1n1cRXmiT5_ETxRcE_WC8lEyWq2yXb7AiBS6dMP377ZjpNg7yZZhtIrIqTa4aX2XeUXhqUcnXOFsqOFYH0dzf78UF8jmEAkXgSrLwKVChPfe77UniuQ7C_qL672nvdvFjgs6tCe5y9zc3hzXWu71bm5jxK5XVLpGoChbl_6QV6GLimWPkmZOLjpd4MnfmK6kjjqqzoUFRmBKrNNqtOMnqXQLQlZiYFi-kXYJopnWuFI-lGOgIJ7ww" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1a75f897a8.mp4?token=gmEqO8ckQKsUBQU2V7O6LazDlH7wyOPBRequVdXWgBIqiE5hUdncqU5P4-dTfP-P3q30ToQtn_a2HdD27I8hNOQshtPDL2_ZU1n1cRXmiT5_ETxRcE_WC8lEyWq2yXb7AiBS6dMP377ZjpNg7yZZhtIrIqTa4aX2XeUXhqUcnXOFsqOFYH0dzf78UF8jmEAkXgSrLwKVChPfe77UniuQ7C_qL672nvdvFjgs6tCe5y9zc3hzXWu71bm5jxK5XVLpGoChbl_6QV6GLimWPkmZOLjpd4MnfmK6kjjqqzoUFRmBKrNNqtOMnqXQLQlZiYFi-kXYJopnWuFI-lGOgIJ7ww" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🙂
دوتا پیرمرد پرحاشیه سالیان اخیر :)
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/Futball180TV/104369" target="_blank">📅 16:05 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104368">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bc446632ea.mp4?token=HhEpvr9VxH6e-0V5YzVMEeXgCb0UBS6NmtPhqpAJ8di_9M83l1tfY-zU0KAIO_RKeQNeVJv41ljE_giOzrQryG_VJtFG1HxDJfBgJ9g3C0bcHY1IzE-DgNrDYkzsl6Qy06WiCgu_7GTNvQMV2XOW82tR7GlputCjiuuh9OBJXdYK4OUoHrOgbXfe_1zSp_XWD7_1slpq9NzOBmoaIEI0sIVdt22UefT6XyrwX_sBkolHSwIfCpsIwPNQWkbDp6uBxH0YDZr2Yy_Iq8eH5Y7zmGUJDN8XMiDBC_EexUUH1__tSePPSIYR4Jfc41eS4Te5gZ05LHhb2FT-nrLXRDw0Pw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bc446632ea.mp4?token=HhEpvr9VxH6e-0V5YzVMEeXgCb0UBS6NmtPhqpAJ8di_9M83l1tfY-zU0KAIO_RKeQNeVJv41ljE_giOzrQryG_VJtFG1HxDJfBgJ9g3C0bcHY1IzE-DgNrDYkzsl6Qy06WiCgu_7GTNvQMV2XOW82tR7GlputCjiuuh9OBJXdYK4OUoHrOgbXfe_1zSp_XWD7_1slpq9NzOBmoaIEI0sIVdt22UefT6XyrwX_sBkolHSwIfCpsIwPNQWkbDp6uBxH0YDZr2Yy_Iq8eH5Y7zmGUJDN8XMiDBC_EexUUH1__tSePPSIYR4Jfc41eS4Te5gZ05LHhb2FT-nrLXRDw0Pw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
▶️
این ویدیو بسیار کاربردی برای زمانی که در باشگاه، دستگاهی برای تمرین خاص وجود نداره و باید از راه‌های جایگزین حرکات رو انجام داد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/Futball180TV/104368" target="_blank">📅 15:50 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104367">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0deddd0d6c.mp4?token=ZpvKUYq15MGih6olatWyDRbhFlZJKfWFgPBx_3-7Ww4L51s63Q7RF-l18scxMTnyC8sRCApyiAP4mueFVr2c-0_T8B9layP0zHfCLVldBOd7t48Iwnx5RvhfPZfEuwx4YcWY1nd5OAEZp4jeEb09nGEzDNVyzXlZgOW85vuGHQ97cDM9L6cliltAeaHvlaEynckLdoWrybsYxhrpcoIyDSazIBm8oI5ZzaubS_eh_DTybcwtnM7g9Lpq86w2vuG6saApHoi7A2WGiTSXwkV83lUhmPs3ZYYD013L2dkVeahHg1xGEib2YhXn5BneMNEI_0Zx9HWw_jqVDwJeW8O_5g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0deddd0d6c.mp4?token=ZpvKUYq15MGih6olatWyDRbhFlZJKfWFgPBx_3-7Ww4L51s63Q7RF-l18scxMTnyC8sRCApyiAP4mueFVr2c-0_T8B9layP0zHfCLVldBOd7t48Iwnx5RvhfPZfEuwx4YcWY1nd5OAEZp4jeEb09nGEzDNVyzXlZgOW85vuGHQ97cDM9L6cliltAeaHvlaEynckLdoWrybsYxhrpcoIyDSazIBm8oI5ZzaubS_eh_DTybcwtnM7g9Lpq86w2vuG6saApHoi7A2WGiTSXwkV83lUhmPs3ZYYD013L2dkVeahHg1xGEib2YhXn5BneMNEI_0Zx9HWw_jqVDwJeW8O_5g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🙂
‼️
هیچوقت این مصاحبه تاریخی مدیرعامل ابومسلم روی آنتن زنده با عادل فراموش نمیشه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/Futball180TV/104367" target="_blank">📅 15:40 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104366">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b033bca880.mp4?token=aKy5ZyXrSm4dqDDTuhjEWqYzzaDtVTsaY7sqa8Y_sWQsjVinen212OEgu2emVewbGk15zKYoMBX-3SCM2qoEOEq4Cp3-ldO86KNFM--NyUxGey52LpN4Q3gOxIB7jOdD7lyfj1Lx4h25hG8jcUecmzxrCfDprLLUYyzphjY2CUBzlwH3MICI6rnDe57V4Lz5d2qixYB8lEkKV9hsSD25kHcxK0eo2Tiz3DNUFg3OOBHypkGo5GHFupHgwXBVu8DbrGFs12t_Un7P-QPvmiPUSXRxeplAdVhnulYNN-glh6lO0X1y2EwLBgDhRLcuQL6OGewo-84AzJ4Kj0kPjE0kjoWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b033bca880.mp4?token=aKy5ZyXrSm4dqDDTuhjEWqYzzaDtVTsaY7sqa8Y_sWQsjVinen212OEgu2emVewbGk15zKYoMBX-3SCM2qoEOEq4Cp3-ldO86KNFM--NyUxGey52LpN4Q3gOxIB7jOdD7lyfj1Lx4h25hG8jcUecmzxrCfDprLLUYyzphjY2CUBzlwH3MICI6rnDe57V4Lz5d2qixYB8lEkKV9hsSD25kHcxK0eo2Tiz3DNUFg3OOBHypkGo5GHFupHgwXBVu8DbrGFs12t_Un7P-QPvmiPUSXRxeplAdVhnulYNN-glh6lO0X1y2EwLBgDhRLcuQL6OGewo-84AzJ4Kj0kPjE0kjoWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👀
💥
لحظاتی با لائوتارو گزینه احتمالی بارسلونا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/Futball180TV/104366" target="_blank">📅 15:15 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104365">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9536e07d63.mp4?token=Gt8nb-qAJJXkANMa_pDbOYLpY5vkcbGV2ASXgoanRVeRsjwXk82qqUvDraIv49sYaTJcY8pGJi2Mp9ygzwWZEspi1OccRmGUIW0l9X7iIrfkVQx9VP0buc1MUyWMTXIpcOo4xrIiP2sWNaxOb82a2yp9v7xiUZotc2LEot63CI2vYE2BcdUFyyjoMhIRop-NrtPPFetBjh0fF53fg_m8QBp1fSJbj0OluW2WqQe-OtiU2CnacQ22iQ34I5dtAeop8altQQlbOpP8d_4dSbSplGi74TJu5Z7fKLIoGodhciW3IbzUMFRiVZ46dut1dSK4W9wtDutxG1UwnpiCDGaoOw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9536e07d63.mp4?token=Gt8nb-qAJJXkANMa_pDbOYLpY5vkcbGV2ASXgoanRVeRsjwXk82qqUvDraIv49sYaTJcY8pGJi2Mp9ygzwWZEspi1OccRmGUIW0l9X7iIrfkVQx9VP0buc1MUyWMTXIpcOo4xrIiP2sWNaxOb82a2yp9v7xiUZotc2LEot63CI2vYE2BcdUFyyjoMhIRop-NrtPPFetBjh0fF53fg_m8QBp1fSJbj0OluW2WqQe-OtiU2CnacQ22iQ34I5dtAeop8altQQlbOpP8d_4dSbSplGi74TJu5Z7fKLIoGodhciW3IbzUMFRiVZ46dut1dSK4W9wtDutxG1UwnpiCDGaoOw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
🇪🇸
توصیه های دیدیه‌دروگبا به دیامونده
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/Futball180TV/104365" target="_blank">📅 14:50 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104364">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a301749a37.mp4?token=NSAaKF_qCNDExGodvqiQO3Pz-151uj3lgNcWX0ODC3NSesF8RTNKlaQNftxlTbuS-eMtWMDAhi680H8hPwb3ykXIPoMhGCMfOUk4fcnNiw9BTJc3oGMk3H5dzXVLCBU7kCCsROHtC4nIo2SjHF4OmN9Xd9BP0oBErEtqbOonnGYElmXKcfQ_rqHfnlJRH-u6HA-xr8VD835fV2Q-sJ5gX2GAC4nJZYtHtf_Y_fw9hGzbrIfWGjM5EFDR5a4BFgfzbgfi5n8twgrjlvaE-xTM15sqfs7Nxl4vva3l7-3tpjWrJSYBn59YbscnhNCqcEt6lGP3Dnil0GkJf2ew1UJ67g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a301749a37.mp4?token=NSAaKF_qCNDExGodvqiQO3Pz-151uj3lgNcWX0ODC3NSesF8RTNKlaQNftxlTbuS-eMtWMDAhi680H8hPwb3ykXIPoMhGCMfOUk4fcnNiw9BTJc3oGMk3H5dzXVLCBU7kCCsROHtC4nIo2SjHF4OmN9Xd9BP0oBErEtqbOonnGYElmXKcfQ_rqHfnlJRH-u6HA-xr8VD835fV2Q-sJ5gX2GAC4nJZYtHtf_Y_fw9hGzbrIfWGjM5EFDR5a4BFgfzbgfi5n8twgrjlvaE-xTM15sqfs7Nxl4vva3l7-3tpjWrJSYBn59YbscnhNCqcEt6lGP3Dnil0GkJf2ew1UJ67g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
🎙
بهنام ابوالقاسم‌پور: برای پژمان جمشیدی سند گذاشتم و او را آوردم بیرون ولی هنوز نرفتم سندم رو در بیاورم.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/Futball180TV/104364" target="_blank">📅 14:25 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104363">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0a5d5ff55a.mp4?token=LqitNLK6qmz1RxlSpB-IUTvjI-vi0J2qwM3W_WEh0HoqyD_kSnhuxKmluJltzBqwVIvjq0JFCB_RqpHoEFh2VrMnIHDhT5lic90aAymKTpYMSa_7ue3x4d6RA_NuszGQ3xEsf3yKdwub608tbAag5diUOJ2gbAATt6L4U7ad1H9W3KJD35Blyp05Sw_nTI-lRee5ftMIXlRh2ovT4c7KWZHReo0TrxK2j5iJQwrN6dOqjt2Kcx8gFfzrvc_9pn6fB-U3doYtxxfVw1f0NEAZ0qoehXD6wEe67MK6fcj9te3WXH9ZcvkIFTXzf8EpS35rdpro_q1HwceMr0B4n-VEAyOnsOvnBRLlqfe24AAOIt6OOQQWr2HcAeJd4h585aT_KhFcFsj8lAeW4orsHaa2M8rCCMxKvgq734WLFIyIaS1zTAtp9t0qong1h-R1Wa4K8AJQTgudxNrnvI9Wm-UfINqksMpzpCcElyqePsuMKiPI5VXnxDv_odHA3ZTk3TUHlEi3RmziMooiGQVSMdEu0yUZRuUnzhtsUnPBLoIiHyyrKisbVIbDcPTHFDHj8-kz5Gp7cWyiaJxij0xHaBMBoGcr3VBS49BdDy3VqNBbw1iXGwYJEDkDHjsX6xBGkApQw2e_VVt-FNnv6yCCm41BWbO9tSMXK5dLtDcZSkWqJcs" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0a5d5ff55a.mp4?token=LqitNLK6qmz1RxlSpB-IUTvjI-vi0J2qwM3W_WEh0HoqyD_kSnhuxKmluJltzBqwVIvjq0JFCB_RqpHoEFh2VrMnIHDhT5lic90aAymKTpYMSa_7ue3x4d6RA_NuszGQ3xEsf3yKdwub608tbAag5diUOJ2gbAATt6L4U7ad1H9W3KJD35Blyp05Sw_nTI-lRee5ftMIXlRh2ovT4c7KWZHReo0TrxK2j5iJQwrN6dOqjt2Kcx8gFfzrvc_9pn6fB-U3doYtxxfVw1f0NEAZ0qoehXD6wEe67MK6fcj9te3WXH9ZcvkIFTXzf8EpS35rdpro_q1HwceMr0B4n-VEAyOnsOvnBRLlqfe24AAOIt6OOQQWr2HcAeJd4h585aT_KhFcFsj8lAeW4orsHaa2M8rCCMxKvgq734WLFIyIaS1zTAtp9t0qong1h-R1Wa4K8AJQTgudxNrnvI9Wm-UfINqksMpzpCcElyqePsuMKiPI5VXnxDv_odHA3ZTk3TUHlEi3RmziMooiGQVSMdEu0yUZRuUnzhtsUnPBLoIiHyyrKisbVIbDcPTHFDHj8-kz5Gp7cWyiaJxij0xHaBMBoGcr3VBS49BdDy3VqNBbw1iXGwYJEDkDHjsX6xBGkApQw2e_VVt-FNnv6yCCm41BWbO9tSMXK5dLtDcZSkWqJcs" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🚨
بخشی‌دیگر از مصاحبه اخیر و جنجالی حسن روشن که‌ کی‌روش رو هم مورد عنایت قرار میده!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/Futball180TV/104363" target="_blank">📅 14:00 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104362">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cdb917925e.mp4?token=efj3kfxpsQylKXAbBVH_8bEvmaL6hL_dukAGxt52JCCm6dR2lE8dsyXtLhctF9BBeZuJfDFosiJ5fZzrFqc6Ki1XQyOjXsShPz43oxlNJcqygMqY5KFvpy0q_ZgNfR1WAbNyOJYlEMwzJXiLKVjaxWbdttAdmz9B_nchKpzoio1MfmyIQRX4oSb8lwtvxfCuyGCV6xeBkE0zU0Z3mZIcOhg8mwxS2O1VDY22BgPCbcVUQj7sh7zRJBNScnOIONsoBRL22W5SxsFsjuqov1w8pyyA0ch7zjttvhl2nHFczevQhEENirtANj3iDE4ye9NjiaNcefUIVg2NDQ4-UAl0yxpBZoGDMH2iX02JTD7AZvZXtjuMwpbm3zg3g6Hd9t5gg1L1GxRSu0S01-zGH9_OrYwiE2nVlcBlSsjnaWGOU5sN3Iyne7U2uO8tU6lCrRBPvjHWlOnGFBJng9vj45D7DIJWQtUiIyqrbp3RV-T5W3ncfBeHlNqfGTBHURoMicQQGjZGsBihlN_cVIGJVo6SFfY2VRNGJMtmBEla4WcHZfPiF8ZLjPt0EpjJH-QaWyTmghaO3CEVIY2ddV1xcBM9zNBCq3F_NRi2aBpTasTiXnOGVXjjxkiCmEwPIiA576A6x36wArGSLBTeBDNMFDpmcJOw6o9AUS484B_Jhi5UWA0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cdb917925e.mp4?token=efj3kfxpsQylKXAbBVH_8bEvmaL6hL_dukAGxt52JCCm6dR2lE8dsyXtLhctF9BBeZuJfDFosiJ5fZzrFqc6Ki1XQyOjXsShPz43oxlNJcqygMqY5KFvpy0q_ZgNfR1WAbNyOJYlEMwzJXiLKVjaxWbdttAdmz9B_nchKpzoio1MfmyIQRX4oSb8lwtvxfCuyGCV6xeBkE0zU0Z3mZIcOhg8mwxS2O1VDY22BgPCbcVUQj7sh7zRJBNScnOIONsoBRL22W5SxsFsjuqov1w8pyyA0ch7zjttvhl2nHFczevQhEENirtANj3iDE4ye9NjiaNcefUIVg2NDQ4-UAl0yxpBZoGDMH2iX02JTD7AZvZXtjuMwpbm3zg3g6Hd9t5gg1L1GxRSu0S01-zGH9_OrYwiE2nVlcBlSsjnaWGOU5sN3Iyne7U2uO8tU6lCrRBPvjHWlOnGFBJng9vj45D7DIJWQtUiIyqrbp3RV-T5W3ncfBeHlNqfGTBHURoMicQQGjZGsBihlN_cVIGJVo6SFfY2VRNGJMtmBEla4WcHZfPiF8ZLjPt0EpjJH-QaWyTmghaO3CEVIY2ddV1xcBM9zNBCq3F_NRi2aBpTasTiXnOGVXjjxkiCmEwPIiA576A6x36wArGSLBTeBDNMFDpmcJOw6o9AUS484B_Jhi5UWA0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">از آنفیلد تا پاپارا پارک⁣؛ ایزاک، هوادار سرسخت لیورپول و محمد صلاح، به دعوت ترابزون‌اسپور مهمان این باشگاه شد تا بار دیگر با اسطوره‌اش دیدار کند.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/Futball180TV/104362" target="_blank">📅 13:35 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104361">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kwq4ZgrDIfny8uTuDN1uTQZS3pQNexDc4RJMIJ0R-OyXn0r819qXf30T1svQlZwHb0zYn7JppDgCSjCJkPlVCj9W8awM54cPYsoItGtuRn26qFI7jp1Xh1LeYP60awRs9aZcbYYR_1YJHx9DJ7ZadZ4rxeT8Ck6qbypVgX_5TJuWR86zHprNclz9pqvkciSv-1NwGzw7Qnc6yDZUMucgbRNnmpaVtbPa1GB-YJBfNGTPb43C8bQqyc51fWfnREbCOJv2Fc7zL9yeHLr8UECFYnoyWlqrDoXQczl2UF9Y0hVpv_oLANXLyjbtPFpwdH9vLu8RG8faU_-67OGKy-aU4w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
شماره پیراهن این‌فصل بازیکنان منچستریونایتد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/Futball180TV/104361" target="_blank">📅 13:15 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104360">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/57b5cc35a2.mp4?token=N4Y-imwv2L35jKXuq_abKzJ740f-cq6SQh-AQb9y-IdE78a6HnXSsD7-lHKnQKQ-JW1dIWB_IwUJjtor_nf9uxjIrfetaHWPROZTVVoz88M8UgN3_pqpprL61ftbeCiGpXeuetGiQFzuYtJV5BnoH0gWMjdDPZwLvtKjN_VgS3bDPqFbs5gstuH7EC793hruBcvPYjz7sbDcIhQJm1MRD9apPfwAtFQsNMl0rG26WFuczaNZRcf8IknnXR0eZ-W60bjNpDaHncoGpsEPD2dQ1a7eIKReMolJLZyUqnEmMAos0-KGWF_1JPxJJkPeUPcINHqGtOPA136i2CUb0TsuVQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/57b5cc35a2.mp4?token=N4Y-imwv2L35jKXuq_abKzJ740f-cq6SQh-AQb9y-IdE78a6HnXSsD7-lHKnQKQ-JW1dIWB_IwUJjtor_nf9uxjIrfetaHWPROZTVVoz88M8UgN3_pqpprL61ftbeCiGpXeuetGiQFzuYtJV5BnoH0gWMjdDPZwLvtKjN_VgS3bDPqFbs5gstuH7EC793hruBcvPYjz7sbDcIhQJm1MRD9apPfwAtFQsNMl0rG26WFuczaNZRcf8IknnXR0eZ-W60bjNpDaHncoGpsEPD2dQ1a7eIKReMolJLZyUqnEmMAos0-KGWF_1JPxJJkPeUPcINHqGtOPA136i2CUb0TsuVQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
ویدیو وایرال شده از کنسرت خیابونی در تهران
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/Futball180TV/104360" target="_blank">📅 13:11 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104359">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vjWx21_cbCRvffczX05sdwfEvj0dnLrDKzb1i_tC-cwKurXAUPudJaAFuii-5xjSHGHliFl_5IgFXv94tp1P24-bayoWHXQiB_AcA4MzkHe2QJkeKDOCDz6ZrVraxiM8USCqf-W6yIGxy-ZU-n2ZBmB1KNjZgp3i__7AwpN0ff-mcbzEnIHfj-XTJ8RqDPO2jr6XyYrwbavc8lze57K0FhSEyI3qb0CBcRah65Fu-Ka7la-PZX4cWC_peuXlOM2cKY38VTfurGshff1gLBzbVVCvGyMU5YG0dG18P-7dHUUyK-cRAhtBdl79B1wXEzwjWms7esfvQ5WgyWI_fnlpxw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🇮🇷
اعلام لیست نهایی بازیکنان تیم ملی امید برای بازی‌های آسیایی ناگویا؛ امیرحسین حسین‌زاده تنها بازیکن بزرگسال این لیست است.
🇮🇷
بازیکنان استقلال: محمد خلیفه، رزاقی‌نیا، اسماعیل قلی‌زاده، سعید سحرخیزان
🇮🇷
بازیکنان پرسپولیس: دانیال‌ایری، فرزین معامله‌گری، پوریا لطیفی‌فر، پوریا شهرابادی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/Futball180TV/104359" target="_blank">📅 12:55 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104358">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2fc7ebac37.mp4?token=G3JHJNL3xBxLwr8FUzTiJZAKLvGoOPm-3OV-2w121GQUgKVRmm3D7xfv6NmpWnPzsahJ97QQmjZCjDiHRWhr8WmNySpzcOH7kIMTyRktRPn24_QcFHHgRLJoBpHjLh1AF_0OAebyw0tr_QTFjFne0gn0l96gLmdulp4hQnSinSokxM9ZCXk1WsqGAh0cIkdKvo8c1CRJ8UbagY18iPz2sCxorUA-eV6OUFbL23MPaz7rSaiK__ZjrdzMQmubeNLQkhwyfWvVbCs084elPkEHOOZTKfI-6tLKbOEjzG6M9-dRyRjrUAl3r2-Y0FH_1nQ0RYL4_-mmeSNlQaDlWIDwUVpPRfr8DiZxt47oTBAALlQkcf6eKbrFbrEu8eUWMNJUHQDVfAGz5qZVW3MkIIHn9S3Kp6hhouu267_DGgdBgDT9eAdvMhOshu9BCUoIjdAmLSXRCssPEZc57YB9v-w2zsKvpR8kH1tFJT79W-nC4SjfUTYhq4CukQ0miPH34dvOqb8SqApb6iVgH8nxvvSBT9f8jOd-vX7Tab5ZHxOUU1Naz_3JYfyefwGxUhb1_oEagrnxUFX-upiSAy9S2aeFHC1vG15mzuPAze0EJYggRlQbj9TugkmtLnOeQy3EWOAGrsIwfFQXypca66WvT8eEczWFkXKL6qoEQGs-XkkewcQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2fc7ebac37.mp4?token=G3JHJNL3xBxLwr8FUzTiJZAKLvGoOPm-3OV-2w121GQUgKVRmm3D7xfv6NmpWnPzsahJ97QQmjZCjDiHRWhr8WmNySpzcOH7kIMTyRktRPn24_QcFHHgRLJoBpHjLh1AF_0OAebyw0tr_QTFjFne0gn0l96gLmdulp4hQnSinSokxM9ZCXk1WsqGAh0cIkdKvo8c1CRJ8UbagY18iPz2sCxorUA-eV6OUFbL23MPaz7rSaiK__ZjrdzMQmubeNLQkhwyfWvVbCs084elPkEHOOZTKfI-6tLKbOEjzG6M9-dRyRjrUAl3r2-Y0FH_1nQ0RYL4_-mmeSNlQaDlWIDwUVpPRfr8DiZxt47oTBAALlQkcf6eKbrFbrEu8eUWMNJUHQDVfAGz5qZVW3MkIIHn9S3Kp6hhouu267_DGgdBgDT9eAdvMhOshu9BCUoIjdAmLSXRCssPEZc57YB9v-w2zsKvpR8kH1tFJT79W-nC4SjfUTYhq4CukQ0miPH34dvOqb8SqApb6iVgH8nxvvSBT9f8jOd-vX7Tab5ZHxOUU1Naz_3JYfyefwGxUhb1_oEagrnxUFX-upiSAy9S2aeFHC1vG15mzuPAze0EJYggRlQbj9TugkmtLnOeQy3EWOAGrsIwfFQXypca66WvT8eEczWFkXKL6qoEQGs-XkkewcQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
🚨
🇮🇷
‼️
#فوووووری
از بختیاری‌زاده: ناراحتی کوشکی؟‌ حرکت او حرفه‌ای نبود و فردا مقابل سپاهان نیمکت‌نشین است.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/Futball180TV/104358" target="_blank">📅 12:51 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104357">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5711b4d86b.mp4?token=UKPFfNRVhDopdQDlHBDdcK-juMoZEDUB690afTjKVDet89V-RIMhTZkvYQcuU2h-pNu8wtPSAjTPuRJ2zbupeZweZmPsQXzBR1b7AGfjRs0OC5HG_HQ_zFSlCKrtgLtvw_pRuMFRpm1NuDBpM6x_GbbsXUDwYkaJOAcHXAjlPz11QwhI8VojbDuowiRLd1XnSMyB9Jt5kZMoT6Eay1LFyYmGXCw98oBtzxXGTHSj40gjguhALkIlQnI1aBbzc4qZbZ7l_1PG4nVAFuj4QO7kA9dZRnlRo5YvaTRGcmy5Y4mRXK6RYU8v3YHLR73GtdxIYtX_ssM29BTQpmXZ7eSOQQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5711b4d86b.mp4?token=UKPFfNRVhDopdQDlHBDdcK-juMoZEDUB690afTjKVDet89V-RIMhTZkvYQcuU2h-pNu8wtPSAjTPuRJ2zbupeZweZmPsQXzBR1b7AGfjRs0OC5HG_HQ_zFSlCKrtgLtvw_pRuMFRpm1NuDBpM6x_GbbsXUDwYkaJOAcHXAjlPz11QwhI8VojbDuowiRLd1XnSMyB9Jt5kZMoT6Eay1LFyYmGXCw98oBtzxXGTHSj40gjguhALkIlQnI1aBbzc4qZbZ7l_1PG4nVAFuj4QO7kA9dZRnlRo5YvaTRGcmy5Y4mRXK6RYU8v3YHLR73GtdxIYtX_ssM29BTQpmXZ7eSOQQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🎙
نظر جمعی از هواداران اتلتیکو مادرید درباره ماندن خولیان آلوارز و واکنش دیگو سیمئونه به توهین برخی هواداران در استادیوم به ستاره آرژانتینی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/Futball180TV/104357" target="_blank">📅 12:45 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104356">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ONUPX3Ydo2Q0g7rDo2Pzp7vsYu4ShNftyiBg1a7-YDHa4noNUv94hGX6ctqMlKrIREAS0D-Kqn8bvvi3sM8d2lwxdNUQBzrbzl2BWS25iW1iMfD-dgANz-UWv9CadTlD2DXe_4DCMKmETzhq3C-sOV6kaYQuh8y3GxaOs63twt4DWdHXio8Q72w-U-Wjxea8mxzBTn7UcdDCmh_H5g5zeUf5nh4Y_854s3NhNyn34pUGHXak4r178pj_4B1oStLhq78dbqnL6YqOEqVljz25IrBPCbowZvq3CTDIBu-y-DPnZNUqBNwcCqUAbXm1baTnKQK_cknYRh_-XrAmSy4SSQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
🚨
مالکوم با عقد قراردادی پس از جدایی از الهلال به تیم‌الجزیره امارات پیوست.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/Futball180TV/104356" target="_blank">📅 12:25 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104355">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EpHnLkSIeEiJWKLDjP5Ccxo6bCGrUIPTKDWWDdH9OL9ED4wGPf_WK1_uHuq_0QjciUho5SYrcbcoS9dnnNpa93OI5DAcdUb-zEz4Dcnn3oySglFHbabYxIgxafoz8vMlXFHHHTz4niYuZvVBA3bVOdgiEcbXm5wejIVdkyuVz0gSGqHITwBFAEWp8loU4-4mG8EhCNo7ufMQMUhDO1L9Xr0quWUHGr-XUStfTbhN5AdQW_MwKiAbXp1_YeayW9N1eaxK4uCGMIm6HZ4KW_CbBwXXMf7iwhOAmRsdfYhCmZVwMl21YyN6ynKhJKj5g0E8Odr2wIZDBFaVE3xabXeKiQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
✅
سایت برنامه عادل فردوسی‌پور پس از گذشت چندین هفته رفع‌فیلتر شد و در دسترس قرار گرفت
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/Futball180TV/104355" target="_blank">📅 12:06 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104354">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ab7bebaf5f.mp4?token=l3rJAGwO6b8BVUdilEjZUjL-L8kJDptNPKwfEZXrf9Ld3LAij4fRxCl-Qkn7rYLNBEVOTHoHgSrF_lhpPHpwzyE2_z7iu7NRgpPPSfQ9s9L36qDmu-a-EHlSPvGS_nlzY5aDjGtCuMC7_Kaql0-DMJVD0-IODByoG0joZd3fzogQL1rSdaXo3hNj81qdCDXMEsIfbM1VuCd8_ehVsOcXENlzHcyRU_keQDsIR6aX0ys3X17-15v0Hz5c0qQgicqhwV9H5iy4p6ZUDN72X9qEPL_dpMOpSdoyZdYTEq7baGVQro_tZFIJAshqjB2nix3uKPosnsxR8LiRu2-ytogZ6A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ab7bebaf5f.mp4?token=l3rJAGwO6b8BVUdilEjZUjL-L8kJDptNPKwfEZXrf9Ld3LAij4fRxCl-Qkn7rYLNBEVOTHoHgSrF_lhpPHpwzyE2_z7iu7NRgpPPSfQ9s9L36qDmu-a-EHlSPvGS_nlzY5aDjGtCuMC7_Kaql0-DMJVD0-IODByoG0joZd3fzogQL1rSdaXo3hNj81qdCDXMEsIfbM1VuCd8_ehVsOcXENlzHcyRU_keQDsIR6aX0ys3X17-15v0Hz5c0qQgicqhwV9H5iy4p6ZUDN72X9qEPL_dpMOpSdoyZdYTEq7baGVQro_tZFIJAshqjB2nix3uKPosnsxR8LiRu2-ytogZ6A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نگاه طنز به معروف ترین دعواهای تاریخ فوتبال.
🙂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/Futball180TV/104354" target="_blank">📅 11:55 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104353">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">🚨
🚨
🚨
🚨
🇮🇷
حجت‌کریمی مدیرعامل تراکتور: متاسفانه قانون ورزشکار قهرمان برای معافیت سربازی شامل علیرضا بیرانوند نشده است و به احتمال بسیار زیاد باید این بازیکن راهی سربازی شود
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/Futball180TV/104353" target="_blank">📅 11:35 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104352">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/c4qlsL5NmKDJ0FhB0YS6aseB6iuoQF5LTyz0eQnOjzBbj7bCWLgmpM-yf0sySW57XgdMjGbTC5XrflJwMkeOb63OOUa-fA7rSg1UCb2noWYqJX_xZX4pIaqiFIDTJS8KrM1Yv9x9JNOBm9y8Pxnajmc4YPDOUFyoRulvXyKtzJKe4JG-naKMfdDxD5EIkUBldgPLexGN-Pi1K8HTxDa30Lea8l9_X5fkVQE53BNpgin_iby9hJdmmxcvcN4ByHTvoJ1aXBG6VNaIS31Vh9tXKcUWCe74-kQSqSNQ7u6PIIYWWonuXJIeAnLbQix3SXwRa1NCRonqUlD_HOI1LBM0fQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🚨
🇮🇷
حجت‌کریمی مدیرعامل تراکتور: متاسفانه قانون ورزشکار قهرمان برای معافیت سربازی شامل علیرضا بیرانوند نشده است و به احتمال بسیار زیاد باید این بازیکن راهی سربازی شود
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/Futball180TV/104352" target="_blank">📅 11:26 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104351">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UJNK-hCM2IHziSi-nrXk6TS3piHZTdI0-MxyhLL_v_Ut__iDr6wTr7kbnKkHvBwLCceX5okRGkdrJhIVRJwK-71QlHC4mcto73BgYhuVk5ltDEmh9xwR4t7oGmZIz7Md647ctiA11C7IGTgu93hanmZn4lQpLCvCu8gv3stykoMRz-x81ZpE01jii2IHXqCgIA19029JF4ygP3zmVGfbIJa4rQIHRoGgbp8mQKj-umechDJ8MXXjuVJVzjFOFAXRhupzjlgFVM_k7hUHo9FV-bdXXp48g0CelhSrDT0UotUmY3U8QPBn-ARHHH7nQ6VA0d59c4LidmrjhhMOBveOlQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇮🇷
✅
اعلام اسامی داوران هفته‌سوم لیگ‌برتر
🇮🇷
🇮🇷
استقلال - سپاهان / پیام حیدری
🇮🇷
🇮🇷
پرسپولیس - تراکتور/ امیر عرب‌براقی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/Futball180TV/104351" target="_blank">📅 11:23 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104350">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ehP6u837aUXxUvujHS0le1n9HS0Uz_Z3Iwj0S0QZJKtuCl4NR0E8T3Th7sriFVpOBZ-Kmx0P6xR-8kK3LJivCkD-Rhigtw1r36nNG8qiWTcLdmZR4-XthajDivABWlJNMXPDfv8CUjRpObaLbMTcIu-TqsWEd0_rZBRqvUXNdLDxr4hAzBwSWE5HfL6HQOd2SipQy90fSpREXtdS3WisnQ14ec8jBeIHeivOKgn9oxG6jrpsjGSlF7jrH-JemGUaz7JqVldovC07Ne1RBDgwlvPHopkrd-fdDr38rRrg0X6w_Rq6SXwy8O_bAOHA1_4ZAfBsFldaoJNFFrAJH9i9LA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
🇮🇷
پوستر باشگاه استقلال برای دیدار با سپاهان
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/Futball180TV/104350" target="_blank">📅 11:17 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104349">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">melbet.apk</div>
  <div class="tg-doc-extra">46.2 MB</div>
</div>
<a href="https://t.me/Futball180TV/104349" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🇩🇪
آپ اندروید سایت جهانی Melbet
💥
🎁
بونوس ورزشی هر چهارشنبه
🔥
💸
واریز و برداشت متنوع
💵
⭕️
بدون نیاز به فیلتر شکن
⭕️
🎁
کد هدیه ثبت نام Melbet90
✌️
✔
https://t.me/+x60dZGAgXTUxM2U0</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/Futball180TV/104349" target="_blank">📅 11:17 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104348">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cEoopY6RrQlGXzHIQYxhBSNnjKFfajsUMHRgVWdrB9aaTqI5eeOIRYJPpyBC1-r57bulqnAVKWXKBWd3hk_4NdQaFwO7dwDCJ4pFu5GHyHCdo7mcABmKnhkZIAYUUbnye1QBU-hi6Qpc67nHIU3Z23UBolc2YkwkcPtxOwDhMkA7_N1ZsbfffZULwZy0Fl5oW2EjNt_Q2yvqNj7yqsnNrHntUobBXiwsV6y_45IwcOWa4BYhwsHxKiNrkU55GGHT220tn5mT-1eoNgC1Hj_kST_rP9BWiNOZiaYFzPU6hA5Bn8FPFzU-3L8b3Hz1cp3VddZel05LgJXTRm-DgI0_Qg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👀
دنبال سایت معتبر برای شرطبندی می‌گردید
⁉️
🎲
سایت بین المللی و معتبر Melbet
👍
😁
😊
🙂
🥇
واریز و برداشت ارزی و ریالی
‼️
🔥
بونوس 100% اولین واریز
‼️
⚽️
بونوس ورزشی هرچهارشنبه
‼️
🆗
کازینو و انفجار با ضرایب جهانی
‼️
🎁
کد هدیه ثبت نام :Melbet90
🇩🇪
دانلود اپلیکیشن MELBET
👉
🔗
لینک وبسایت
👉
⭕️
جهت استفاده از vpn از IP های آسیایی یا کانادا استفاده کنید.
🇨🇦
🇹🇷
a31
✔
https://t.me/+x60dZGAgXTUxM2U0</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/Futball180TV/104348" target="_blank">📅 11:17 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104347">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6eb94b21a1.mp4?token=vKj8T_cTkxNoB3YZXPejKWTWAVHO5dQuK3cMDLPDM6UhgZ_4DjhnMx-uYTa4DvstNSTdyL2G_Tk35VcrcxsyAx8qMOW_pqXx6IpevoQALVedmZu7Dd4Aokxr2oXzPH1hnjjyThshU45YDtB0x_JmM09vhWu50zsWrdHZ9HV1dE8Y2v_fz4yOmN1VY-M8e4UtGrapStLyfShscU9NJBCFmqVClMvuExj921Dh36So2336dXP-azs4d5QIj9czYvbG5opR8hEGztE-eqQSVSrWvsc7tKmSqUeH2jLQHM7tzlESdfDTz9ErtIR1q7YDbwCSxnmcYvJ8TxvL_OFdH23SRg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6eb94b21a1.mp4?token=vKj8T_cTkxNoB3YZXPejKWTWAVHO5dQuK3cMDLPDM6UhgZ_4DjhnMx-uYTa4DvstNSTdyL2G_Tk35VcrcxsyAx8qMOW_pqXx6IpevoQALVedmZu7Dd4Aokxr2oXzPH1hnjjyThshU45YDtB0x_JmM09vhWu50zsWrdHZ9HV1dE8Y2v_fz4yOmN1VY-M8e4UtGrapStLyfShscU9NJBCFmqVClMvuExj921Dh36So2336dXP-azs4d5QIj9czYvbG5opR8hEGztE-eqQSVSrWvsc7tKmSqUeH2jLQHM7tzlESdfDTz9ErtIR1q7YDbwCSxnmcYvJ8TxvL_OFdH23SRg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
🎙
روایت امیرحسین اصلانیان از خوردن حکم سرمربیگری احمدرضاعابدزاده توسط آقای مدیرعامل و واکنش علی پروین به این انتصاب پرحاشیه.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/Futball180TV/104347" target="_blank">📅 11:05 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104346">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/80db36926b.mp4?token=nS2UPvO5SO3qzjdHJArWmUUlzxbYPUisFJmYrpmDLdU1XfgC5-jVY6P1Qs60HB_S7Zjh_wtN6wSk23r1fVHI8T-Np7mE8-UWeLXgHhc7F8nCBPhXNg5o5T84mSxkCVtSDZvIV7KK7ybQMJiTXxSAbmQfYP5lA2sbEydjiN72uE41Oe3HSHwmBOuDSZ6KepY0SpCS1AJ6r8M3p9NjQrDUa6gsDqIv5NezPRiaymViONfHHgHOf_z75-Q6wW5quy3LcBYoZbCXu9t42wwV_tPeU4jk3HdqULSI2jwfOvCQK6nSjhCQYGbWXbCmDh7sbQLzAMkDKgUOliCp7dnGJVCuIw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/80db36926b.mp4?token=nS2UPvO5SO3qzjdHJArWmUUlzxbYPUisFJmYrpmDLdU1XfgC5-jVY6P1Qs60HB_S7Zjh_wtN6wSk23r1fVHI8T-Np7mE8-UWeLXgHhc7F8nCBPhXNg5o5T84mSxkCVtSDZvIV7KK7ybQMJiTXxSAbmQfYP5lA2sbEydjiN72uE41Oe3HSHwmBOuDSZ6KepY0SpCS1AJ6r8M3p9NjQrDUa6gsDqIv5NezPRiaymViONfHHgHOf_z75-Q6wW5quy3LcBYoZbCXu9t42wwV_tPeU4jk3HdqULSI2jwfOvCQK6nSjhCQYGbWXbCmDh7sbQLzAMkDKgUOliCp7dnGJVCuIw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
تنگه فلوریدا را هم ببندیم؛ ایده کمتر شنیده شده از استاد خوش‌چشم، کارشناس ثابت صداوسیما که متاسفانه از سوی مسئولان لشکری و کشوری اهمیت داده نشد
😂
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/Futball180TV/104346" target="_blank">📅 10:40 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104345">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0566a44cfc.mp4?token=qslj7xAF7EXkLJ6DSRBdUO_COM0oWagujs3ksSGawRzqMc2O9kOTCafg3N1bp9YTGaG0iPxiUdAU8lJifPljrAtZIAFgbusVmQcrtfOGXU2VaemnyGKzVqxA0IGnjtjIKkFjAu9NViU2aZqzMVd3fozry2uaSFNlgibhCOUd8ZqjIoesPUgpUs4q0dNd_shTlF_L56-6p1icSvswkjUrb_cSGlEx8byL5xxZP3CJUOSslZkPL_0VTiJMpmgP0crF5bvoELMMH8xb82QTb35wZmvSrgSKEuxECsCrznbNorzDLbrgCqb4g9DJdo-e_yyWfnpjUbv14TwVDMRdgAs3Sw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0566a44cfc.mp4?token=qslj7xAF7EXkLJ6DSRBdUO_COM0oWagujs3ksSGawRzqMc2O9kOTCafg3N1bp9YTGaG0iPxiUdAU8lJifPljrAtZIAFgbusVmQcrtfOGXU2VaemnyGKzVqxA0IGnjtjIKkFjAu9NViU2aZqzMVd3fozry2uaSFNlgibhCOUd8ZqjIoesPUgpUs4q0dNd_shTlF_L56-6p1icSvswkjUrb_cSGlEx8byL5xxZP3CJUOSslZkPL_0VTiJMpmgP0crF5bvoELMMH8xb82QTb35wZmvSrgSKEuxECsCrznbNorzDLbrgCqb4g9DJdo-e_yyWfnpjUbv14TwVDMRdgAs3Sw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👀
💥
جانشین سرخیو بوسکتس در بارسلونا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/Futball180TV/104345" target="_blank">📅 10:15 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104344">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d65173b5bd.mp4?token=sFw3GekdiCkhCuX6uY22MPGUftvhu5vzjxAIm63aS2XDUNZcrhXjbLaiqULUdEJaspy9MVnnmGUhFArOsTQ1USA9s548mR103N7OrxwdrFiycTQ-I_BLMpqx04R34666eaVcehynR8FwpchQ7Njs_N6B7Eo7pezWo1HbXuqBy0zfitMESz7u93zA8SVxm4vCAC0a8S5-o-emz1cnYwrNh0zMfqlbB7jd1OG4ujvlumjtvp3uCj9jd3I8f_7i_zi5EiABQsypXl8JXLugBvoXOyqa92zQtPOV-a76QRmaCFQf_MoEH3O_m9h8NQbhy9qudpfZWXMxbgfoX79EUghdxA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d65173b5bd.mp4?token=sFw3GekdiCkhCuX6uY22MPGUftvhu5vzjxAIm63aS2XDUNZcrhXjbLaiqULUdEJaspy9MVnnmGUhFArOsTQ1USA9s548mR103N7OrxwdrFiycTQ-I_BLMpqx04R34666eaVcehynR8FwpchQ7Njs_N6B7Eo7pezWo1HbXuqBy0zfitMESz7u93zA8SVxm4vCAC0a8S5-o-emz1cnYwrNh0zMfqlbB7jd1OG4ujvlumjtvp3uCj9jd3I8f_7i_zi5EiABQsypXl8JXLugBvoXOyqa92zQtPOV-a76QRmaCFQf_MoEH3O_m9h8NQbhy9qudpfZWXMxbgfoX79EUghdxA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
✔️
پیام‌کودکان جنوبی خطاب به‌خانم‌مجری که میگفت جنوب ایران فدای لبنان و فلسطین: اشتباه نکن خانم مجری ما جنوبی ها فدای هیچ کشوری نیستیم ما فقط فدای کشورمون ایران هستیم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/Futball180TV/104344" target="_blank">📅 09:50 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104343">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9bde2485a2.mp4?token=vK1MQisMR_u563iNdixZ4Y4O-D7zV1fmI0AfViDQ5hXOWG3s4OuBhuFohFMVzA36r__T-qXBOf8Y0dXvCLbSCFKxhUByAr9xE0sGcPlti2rrcr7gBKU1NG_xhe1Hd3gNDhLEi33kK6QtaunREJRjQvdQMhfWfGUH5aUErVya8aEi0PN7_HJaU7RnJMdVQl5p9hbczluDv2SG2iWQJVGAN6cb3D3_oxzPS-wDCP8GzY-kPRqWeF3hBrb-b3ADbhVCCUZKtQ52baMBQdLFyKfJpVGvZal0hQtX5qVxG9edr8eyJVK2zV3h8wOqeiwD_k_YrxITk073C8VyvH-c3E4Snw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9bde2485a2.mp4?token=vK1MQisMR_u563iNdixZ4Y4O-D7zV1fmI0AfViDQ5hXOWG3s4OuBhuFohFMVzA36r__T-qXBOf8Y0dXvCLbSCFKxhUByAr9xE0sGcPlti2rrcr7gBKU1NG_xhe1Hd3gNDhLEi33kK6QtaunREJRjQvdQMhfWfGUH5aUErVya8aEi0PN7_HJaU7RnJMdVQl5p9hbczluDv2SG2iWQJVGAN6cb3D3_oxzPS-wDCP8GzY-kPRqWeF3hBrb-b3ADbhVCCUZKtQ52baMBQdLFyKfJpVGvZal0hQtX5qVxG9edr8eyJVK2zV3h8wOqeiwD_k_YrxITk073C8VyvH-c3E4Snw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❗️
نحوه آموزش فوتبال در کشور متخاصم آمریکا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/Futball180TV/104343" target="_blank">📅 09:25 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104342">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/l24BOFWI9tBjHmN1yfX6YBqOT5VJV7UBeXDfRIxAyupArXnb6DNFIm-I89IqV6uWnXoporfBuW_Fbc2ft1WX2vjhyKKs1N89bWRSO-yceWTH4tlBj8zE7NKuQuB2oraoXapkNa0xO9MkFMjp5uueqcZbcWeJuDmPblCL6We2s_aE2p_-65X1kr_Zm1QelRATPaI_Ad91CiqUjXv2VYFahKFZl5cCxRrg3vIp2Bvw37JFPkK6X99d-K7UhlaNREp72ncpapm4fObXMvqs2NM8SmRYlDvvgzgfrxXhZSP9-6wH8v0V4h_5uNcjLAbcBIERej-1ETy0KHlAbQgu0vQbsQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
🇪🇺
شانس‌تیم‌ها برای قهرمانی اروپا‌بعد از پیوستن رودری به باشگاه بارسلونا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/Futball180TV/104342" target="_blank">📅 09:03 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104341">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Fb4qOLl0Z2pc08g0_JjGp2nnB5-cFWsm7rOvY_Z7jQCXBKqEEIPem2CZI3lHAo90ZF7jSjFx8WMn0wQNM-mDs6AzNuLjfc3GdAcK2XAQc4gKQm6TQ2ZnTtJDf6MyC-QgJAYGrZru4i0aLnAEzGaro_GMFfLCj3n-G2VpdUzHTehNTuTUtgrJzmslRjbk935kPHsnlJalv2EOuvh0I9VylWB_fb-7XCRNOR1pLdH_waA590p1IRPYVmoQy1EKzF7Zk9QgpGJATtLPSyntBTCf8TC4jKs39thzFIScMtTGk7elpQrsEcpPvU7yS1MKxXO1XR7h0GQ1U58ZDbIukjNI0g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🚨
🚨
🇪🇸
🇪🇸
استوری هیدالگو، مدیر برنامه آلوارز  «هرگز از یک دروغگو نپرسید که چرا دروغ گفته است چون برای این‌که دلیلش را توضیح دهد، مجبور است دوباره دروغ بگوید.»
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/Futball180TV/104341" target="_blank">📅 02:53 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104340">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">🚨
🚨
🚨
🚨
🚨
🇪🇸
🇪🇸
استوری هیدالگو، مدیر برنامه آلوارز  «هرگز از یک دروغگو نپرسید که چرا دروغ گفته است چون برای این‌که دلیلش را توضیح دهد، مجبور است دوباره دروغ بگوید.»
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/Futball180TV/104340" target="_blank">📅 01:32 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104339">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tE8QQP1R3FyjsrmktKuICsEh6F2-CyJPhGkd7O49l7sLv66V_bREm7X9DMg7JBniYjyD7MK91Pc0P3eRdfdUpXmUgK_5PdezkfaM_Vvh09NzJqnRJFiCD5TWakMvEEwy2zi4Qk_SAgFzlSUgfqO3CWAcTOW1rYCCop8XAz1nhISjsIlox1MeqP8N3jkzUVEEwVcDoWZER4-J2oQJgg9_BmVDQxAS_kpVrQYT0OO4-LHsJ341pGx03F-pG0C3ErH42RCtjnxS_JMrWX-IkhYNtPkRrUkTcBhetUrAq7Y39e7SE1WyLo6VUsf6nGtYcdyvVdF0-E6uZsWkz8ECUlqqGA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🚨
🚨
🇪🇸
🇪🇸
استوری هیدالگو، مدیر برنامه آلوارز
«هرگز از یک دروغگو نپرسید که چرا دروغ گفته است چون برای این‌که دلیلش را توضیح دهد، مجبور است دوباره دروغ بگوید.»
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/Futball180TV/104339" target="_blank">📅 01:20 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104338">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rZwuwrzQvDuF1YqaJH-UmUN8z8wAbejOe33OpWMYx4hC3g2sSfW7jEj7V0AmOC1IlB0By0lGtsm8UpLdoWHdV5yYFe0SNTUIgCTBVF2ppYaUwaP2ziNoG8o9V_WhrLUsJE48OwPjXtOGmgIx3Vl3eocwPhIgO41bWSxTiZplQfPDMMxEcvAA4LnDmppflKDGLYPcheEL1YVu8NjuqjDFBfIwYo4A-VR1yagUf2aQfYGm_8R5laXkwE-rsbbSz_S2mRiBGdjajm4HjC8cTaDV4WT3Gq0pTENeZyJuand2AjPwjMYGKIkg7yoSJfJC_cDVlqA1tAVohM4V2pRx4Laoeg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
📊
پس از پیروزی آرسنال مقابل کاونتری سیتی، میکل آرتتا به پیروزی شماره [150] خود به عنوان مربی توپچی‌ها در [249] مسابقه در لیگ برتر دست یافت.
🔥
⚽️
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/Futball180TV/104338" target="_blank">📅 00:43 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104335">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/e4cd1601ff.mp4?token=HbHZQyhRMpuW5bhgZ2ca6DPZrbjUDJyfHrgHm8Iw2iH0XAetWrYkOEP1wocBSYpRnJAHLOKbo4Mc6PWGWRAzvLGxJ4KuM36CA77_nubcgGfzGgq39mpS9u_EyMjZFgJrNfIYTwpJKczaSZ9_cmvvo9H9vY7bISU-8JJlHEj1YTzqphvaiOaf9XJbZj_b-RRlvDbFcObiR3uC-U3TssYXHL6bF0huDAhPT2HasVz3eBUQZuqwE3_PzRPaM2X7QnHCVn5A6_DqKCYb7LlW8L67VQn1yEPAT7nNFPusDt4EQ6XgYuiA83zH8QlHHwYYTAvh89_PY3Od4nQk7InOGEc3BJ-3RlWm8xCie134OHjc0bEFKsncQ0ZXXDWj3UXJrx593x0a-lrGy8snUvrDbQ4BkXq0wumOiO0MHNHod3N-kI7652RVTlNBN1pqLQXi38TeAJH8d8HBxQBIwGoXD4xCZ6degy0K62BLx4_OgGLYlqYl7lehhzSZSYYSNouVgX2saYS5zxt7PXLNnPGjNpRIXtfifFzU7l-nneFHKL3y1pmvgYrgToy8mPzo3NGOaqXOWsrb5uKw9C4A8t7PpZZar9LPsM7XIqPWYXSo6u06CsAhQj_YLGeLq2EVMAro-zj_viv9PJwWg7X5tMzjEPcK7nY2_wUM60DNK4dfk6gsjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/e4cd1601ff.mp4?token=HbHZQyhRMpuW5bhgZ2ca6DPZrbjUDJyfHrgHm8Iw2iH0XAetWrYkOEP1wocBSYpRnJAHLOKbo4Mc6PWGWRAzvLGxJ4KuM36CA77_nubcgGfzGgq39mpS9u_EyMjZFgJrNfIYTwpJKczaSZ9_cmvvo9H9vY7bISU-8JJlHEj1YTzqphvaiOaf9XJbZj_b-RRlvDbFcObiR3uC-U3TssYXHL6bF0huDAhPT2HasVz3eBUQZuqwE3_PzRPaM2X7QnHCVn5A6_DqKCYb7LlW8L67VQn1yEPAT7nNFPusDt4EQ6XgYuiA83zH8QlHHwYYTAvh89_PY3Od4nQk7InOGEc3BJ-3RlWm8xCie134OHjc0bEFKsncQ0ZXXDWj3UXJrx593x0a-lrGy8snUvrDbQ4BkXq0wumOiO0MHNHod3N-kI7652RVTlNBN1pqLQXi38TeAJH8d8HBxQBIwGoXD4xCZ6degy0K62BLx4_OgGLYlqYl7lehhzSZSYYSNouVgX2saYS5zxt7PXLNnPGjNpRIXtfifFzU7l-nneFHKL3y1pmvgYrgToy8mPzo3NGOaqXOWsrb5uKw9C4A8t7PpZZar9LPsM7XIqPWYXSo6u06CsAhQj_YLGeLq2EVMAro-zj_viv9PJwWg7X5tMzjEPcK7nY2_wUM60DNK4dfk6gsjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
گل‌سوم آرسنال توسط اودگارد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/Futball180TV/104335" target="_blank">📅 23:41 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104334">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/ecf24c9409.mp4?token=A1PaCy21dWDV_wTc81bKQfdFcj4qZr6fPdUI7B_NCEZfXkeKhkbSKzludvqM2IsugG7ItIlAf90dLNRZU3wb37gyiQdLQKhTRrNyyYLO55FO1DbEaabLBdiFSIzOIlCFrWeXfN04fmXVXhPlrBF1XemaE9JyLJSa73TkjGDX2Zsw1DRwjq0nglbzMT6KZTzt7Pu9Y-VWzYWO1YglNbaHzMGfwgfSNTSTWw5rUUo2zbb_6wfJSfZyeGHwQ7VVFlAtMXddFM2nG5c9uJEUyWKnvvkEOTwySUNs7t9OW3jb6ZsMiW64s7h1p6GCUznukEpWdqSdxMKy9IC1MnMUC_CSWLBSKsXimAlUjUVcKu1Foyy_oEBNfQb6BX7vgx3Ddy3drSK_Mc1VaSkoEF-gfJnXI3nJL8w903EQFdM5ZHBDGSmFMOEZZl0dnMUMs8ahiIiTfeKguQkbDJ5rj-jGzUTy5xXQZzequvkFMt5JiDm2Dil65Ng5LCD2n_wgHjljc5SVgEQ_Iw2twqeBceTI3z4G5rbNp4HhSZpsJw0Qn-c3jtB7wDHI_UrtzEAP7VzBeupdNT26NOqVsRgKXl1VS-qYmdMKoeYQ2GaonlIvGAIcikA2wZXPqLVpCuosHuggD1yEOd9EBTvZ8QeZfk57S8MMJPOQBo28zouiNN3QK2nmycU" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/ecf24c9409.mp4?token=A1PaCy21dWDV_wTc81bKQfdFcj4qZr6fPdUI7B_NCEZfXkeKhkbSKzludvqM2IsugG7ItIlAf90dLNRZU3wb37gyiQdLQKhTRrNyyYLO55FO1DbEaabLBdiFSIzOIlCFrWeXfN04fmXVXhPlrBF1XemaE9JyLJSa73TkjGDX2Zsw1DRwjq0nglbzMT6KZTzt7Pu9Y-VWzYWO1YglNbaHzMGfwgfSNTSTWw5rUUo2zbb_6wfJSfZyeGHwQ7VVFlAtMXddFM2nG5c9uJEUyWKnvvkEOTwySUNs7t9OW3jb6ZsMiW64s7h1p6GCUznukEpWdqSdxMKy9IC1MnMUC_CSWLBSKsXimAlUjUVcKu1Foyy_oEBNfQb6BX7vgx3Ddy3drSK_Mc1VaSkoEF-gfJnXI3nJL8w903EQFdM5ZHBDGSmFMOEZZl0dnMUMs8ahiIiTfeKguQkbDJ5rj-jGzUTy5xXQZzequvkFMt5JiDm2Dil65Ng5LCD2n_wgHjljc5SVgEQ_Iw2twqeBceTI3z4G5rbNp4HhSZpsJw0Qn-c3jtB7wDHI_UrtzEAP7VzBeupdNT26NOqVsRgKXl1VS-qYmdMKoeYQ2GaonlIvGAIcikA2wZXPqLVpCuosHuggD1yEOd9EBTvZ8QeZfk57S8MMJPOQBo28zouiNN3QK2nmycU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
گل‌دوم آرسنال توسط بوکایو ساکا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/Futball180TV/104334" target="_blank">📅 23:11 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104333">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/889cf6b1f7.mp4?token=jBi3B7bJqjjPEfoFx9xQrog0uUGKV_9szuOnxwdNMExzPgbnC9Dp-6dLLZ_qJARpELvIfejIzpCQRKP12IBftDn1H3OINfHzeyki0DR_hTEloExPWfyrY4zFduBx7Ikpzkt08uXdpH_1bL_JpNDCfwZFVbXbeyL1G_3leFwZK3Oww_t5QqECebwh-xJbIM3FwIdwUFGMYZCTdMbq_wso1mfE1r6LR12ZIXOL61dbw5xksHzZlWpWRcnu2GVR10Dz1_y1cKr4OARRQbmv1RBBwUM8epH6h_x1hyd4qjpYVWzu7SDruBWwPqh4UIaiUezB6itQJP3-FmPPvmdsl8EaZmfzkN0q6Q3BTiQIWyCeEE6MRCAhLNQx4zo7aGZ0ZTTd8grxLSbTiN9bQEuKLK1WbrUdr0HGOusKOsqsshwCcVTVGya17LhtSPVNBDqt8_TQ5N-G9AmnljjBc-xUJ4Qw7Gt0Cx-Lk0f2Wz8FTDQFYbwpDpOqVFmfyPy_FpiURIhP2FqedXJ2Rlz4PyRXdAoaVLzprK2UVD72GyLc0WrjjxtDqcjJAo6mCnLLhcF9ZbUfwUuXh-Spzh2-VfWUZhWGDUBUxFEZsUXAzhSrkadV4UIN5t5LszNBWDByx_pKLr98jKQ1gRwJhgm5R6Umgfk2hX8QAmo04HnGjYPGodtyLT4" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/889cf6b1f7.mp4?token=jBi3B7bJqjjPEfoFx9xQrog0uUGKV_9szuOnxwdNMExzPgbnC9Dp-6dLLZ_qJARpELvIfejIzpCQRKP12IBftDn1H3OINfHzeyki0DR_hTEloExPWfyrY4zFduBx7Ikpzkt08uXdpH_1bL_JpNDCfwZFVbXbeyL1G_3leFwZK3Oww_t5QqECebwh-xJbIM3FwIdwUFGMYZCTdMbq_wso1mfE1r6LR12ZIXOL61dbw5xksHzZlWpWRcnu2GVR10Dz1_y1cKr4OARRQbmv1RBBwUM8epH6h_x1hyd4qjpYVWzu7SDruBWwPqh4UIaiUezB6itQJP3-FmPPvmdsl8EaZmfzkN0q6Q3BTiQIWyCeEE6MRCAhLNQx4zo7aGZ0ZTTd8grxLSbTiN9bQEuKLK1WbrUdr0HGOusKOsqsshwCcVTVGya17LhtSPVNBDqt8_TQ5N-G9AmnljjBc-xUJ4Qw7Gt0Cx-Lk0f2Wz8FTDQFYbwpDpOqVFmfyPy_FpiURIhP2FqedXJ2Rlz4PyRXdAoaVLzprK2UVD72GyLc0WrjjxtDqcjJAo6mCnLLhcF9ZbUfwUuXh-Spzh2-VfWUZhWGDUBUxFEZsUXAzhSrkadV4UIN5t5LszNBWDByx_pKLr98jKQ1gRwJhgm5R6Umgfk2hX8QAmo04HnGjYPGodtyLT4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
گل‌اول آرسنال توسط کای‌هاورتز
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/Futball180TV/104333" target="_blank">📅 22:48 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104332">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">🚨
🚨
🚨
فابریزیو رومانو و متئو مورتو:
🇮🇹
برای مالکان و همه افراد حاضر در اینتر، لائوتارو مارتینز فقط کاپیتان نیست؛ او نماد باشگاه است.
❌
هر پیشنهادی که ممکن است برسد، بررسی نخواهد شد. موضع مالکان کاملاً قاطع است.
✔️
با ایجنت او تماس گرفته شده است؛ با این حال، تاکنون هیچ تماسی بین بارسلونا و اینتر وجود نداشته است.
🚫
اینتر قاطعانه ایستاده و پیام‌های بسیار واضح و مستقیمی ارسال می‌کند مبنی بر اینکه لائوتارو غیرقابل فروش است.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/Futball180TV/104332" target="_blank">📅 22:39 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104331">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/m4KGAyHoeuwsoLkifaykMcoUKTgjtHAPClayzYm9jfFNz8k2LnHjol-g7xt84jvO2s2n1Uw-cOVWtwWyUXMsoQLOVj4DeNqw_DgMjisd8VI12IhPKdcuVcNk9d385AxiiNb_gQCn88V_8s8RMhN2KdF-CHQQfnX6lz4ze6CLg_g0ptuh6lOszf0__AelAJJPI-MeDghsRLBNShg7_4XU2UjEhRVCKVl2yQh2XqU62JS4BwalIR0Y0WUNH8xFkt970oVyXTBmCV5Slvf-fzwY26QTguttfI55E3pp6_ihBHlSfjx26wG0G-r2tnoy0usU9u6a3r4uaRJ7Ydr08XtSmg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
❌
🔵
#رسمیییییی
؛ مالکوم از الهلال جدا شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/Futball180TV/104331" target="_blank">📅 22:09 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104330">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZWVkORlNBdd2IqkQarfEQIO0FfaJr8t-OvV8iBCJ3rkZsOkLia7Abl4r2kVZR-qnz3goh5Xd7cJIwJbLKRSokdNslvbimAlUf44n7xzp_XUgC_X6D1drdRU0GkWD59ZB5K9mghnC2bDCUz1pgkkDbrH_XfpYZv6VbmaRZwyd9Sbu1JjxGOVYy5Qgh-XNuKDmiH9ajdNYGTt1KImMKtd6IaJzPd_PpbSdTK6_jLuSOnPX8lxdsqGw9hiKULKXcIHMPNclyASzSu3Gdq0liwINQDaV_0gyYiYishKCOffGkwq4sHyr_eLml-7_JUtrVMMcQUt7Qka3ehBQDh4yzIBirQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🚨
🇪🇸
#فوووووری
از متئو مورتو: بارسلونا از انتقال خولیان آلوارز دست کشیده و این بازیکن رسما از برنامه‌های فلیک خارج شده
.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/Futball180TV/104330" target="_blank">📅 22:05 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104329">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f670f0bd57.mp4?token=WaPWF8XUb7X88-hEG9jjxyFOfYRtlCoglbPFpNs6TnqO6d3DA0KMFd7llHHyE2PEZeu5zHdHNwG6zXd_gZRfDcwpq-qZ4os8xgjZ2fzfVNrhXfEsqhvSDP-kcEcq4g5Pyc3e6CvLW8ML5hZiLkcSWDxzAv1ttgO644b6YgaB2q7UJ3T-uAKom2GM1O4k3rGAcX5f2uihMP3GKHU02rER-VfBPGr0XaJ5SQnbKFOaI5kLiM0L5NlrQltxgvMCIClmJl6zzAm958aWestzRs0HA5EB_NYuq0cf0hNRcT5zDEDIl6luEKSq31f16LufXxMpwUMT3PbM8Ja_Zw-DwMeROw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f670f0bd57.mp4?token=WaPWF8XUb7X88-hEG9jjxyFOfYRtlCoglbPFpNs6TnqO6d3DA0KMFd7llHHyE2PEZeu5zHdHNwG6zXd_gZRfDcwpq-qZ4os8xgjZ2fzfVNrhXfEsqhvSDP-kcEcq4g5Pyc3e6CvLW8ML5hZiLkcSWDxzAv1ttgO644b6YgaB2q7UJ3T-uAKom2GM1O4k3rGAcX5f2uihMP3GKHU02rER-VfBPGr0XaJ5SQnbKFOaI5kLiM0L5NlrQltxgvMCIClmJl6zzAm958aWestzRs0HA5EB_NYuq0cf0hNRcT5zDEDIl6luEKSq31f16LufXxMpwUMT3PbM8Ja_Zw-DwMeROw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">😆
حس و‌ حال مردم وقتی مسئولین درباره افزایش قیمت بنزین صحبت میکنن:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/Futball180TV/104329" target="_blank">📅 22:03 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104328">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IFSvVusiKwC8mM1Gtzgb7iHPrL_cl7CUmvWNHlJTQR3ySjXRaUkWoqtycsaBpfTW-HgriMhl-RnXkAgND5QqVeQyktB_VLNd31HmLUoS2TY0gNQyzwvdQY5sS3HKdz7vrY5A9SMPA-8hNDTf3CuoJddL7xWEsoxHOjtVg9hLMo6kKNWPmqPYYkAFwVrbH9gLhCcMQQZGv9pz0HVlb2lnixpxQxVh7FGrV76aMOFICKePO7vWsrKXQ_uaZOf6qveOd6VbqIkjEJE3MnncWsgW6RA7q5qHLkOH0Ko9aCyzYcW5qiZLW1TqxcHIeCh5Ze_xbN8e2VPu68K7Gbw_KD15Jw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🇮🇹
#رسمیییییی
؛ کورتیس جونز بازیکن لیورپول با عقد قراردادی راهی اینتر شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/Futball180TV/104328" target="_blank">📅 21:55 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104327">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DXtoA93BbKkukEHuCWf10-KEDOxVYB0MZd3TFLI8oqC12PTG_saZucjtrz5U0mLw_5vYG9TxUCDq9qONPlf21TOo7rjCubpzE3aM8H0sN_PULXXvKpHbZRU001gDKZs_6pFd9vGogeNPHuxy2bE2-qMPdnJIQOM0Sago3IsUZpEmM_9HZhj0dbEIUllueB7lKEY3S1hqHGuwdgm8JZpZDN2L18CFRBxfRtYA6NWzUS-FqLw2pfTzwgRlTrj914ALPy8B0zluDRQGD30RIBXXxdnl3CW74RRGbmwMSWN05gryFQ3WkcLeo8VQ17nPQ8nQz3TEnnUcxPnOJUzywsDtqw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
گلزنی رونالدو در شب پیروزی 4-0 النصر مقابل الریاض
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/Futball180TV/104327" target="_blank">📅 21:38 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104326">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/91919c1481.mp4?token=OQtXpiTbmgdXPCpSwO6naG2pQzn3Xwmuxc6jN3-V3tLRd9jno4XmRm7oNWRyWJXYvyKsG317TTypoNCKXkvIQYiY08WWFn7fi9WxXJpWrIvZHEEU9EjRhHlrp1NRIWztBMdxFZJa1OeiVb0j-3Ul33px0eFLVE2SI8iCqxXzbratgeOeIeXD0ndBShXaQcOf6PSUz_HS6tqe2bOC10Nol5qzRBAQMGksI1uYkZKUwcQDy5v_0yWTtqjSC0q8Xm_XHW4TzW5mJKYXqdc7QWKFP-M5LgCISKZUY8Tny-mg9x7z-v24vo7-gYQ_T5MmzMUub66Y2fB1DL3yZjaDtY6uFA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/91919c1481.mp4?token=OQtXpiTbmgdXPCpSwO6naG2pQzn3Xwmuxc6jN3-V3tLRd9jno4XmRm7oNWRyWJXYvyKsG317TTypoNCKXkvIQYiY08WWFn7fi9WxXJpWrIvZHEEU9EjRhHlrp1NRIWztBMdxFZJa1OeiVb0j-3Ul33px0eFLVE2SI8iCqxXzbratgeOeIeXD0ndBShXaQcOf6PSUz_HS6tqe2bOC10Nol5qzRBAQMGksI1uYkZKUwcQDy5v_0yWTtqjSC0q8Xm_XHW4TzW5mJKYXqdc7QWKFP-M5LgCISKZUY8Tny-mg9x7z-v24vo7-gYQ_T5MmzMUub66Y2fB1DL3yZjaDtY6uFA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚽️
گلزنی رونالدو در شب پیروزی 4-0 النصر مقابل الریاض
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/Futball180TV/104326" target="_blank">📅 21:31 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104325">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5e061ffb68.mp4?token=pQDfMqViz049cOnJyojQa4rveg7cCSKL1-whKZ0mDYv7rgth1h5We_JMR96aztG2bIgcWfZiS8_kvg0zr0QD-stnSL87cRVB11xHwngeQ1hoBJmKIRUtBPLobDzfFx9OAcaPbsVBJmv9PxPAK5plZeVsbw_Q5b20QMsMqkrHM9Ss8HQrBPORvmfxLFnnlUIAXM92l3qF8wL_8EbQiDWZTXk_F34jrlspL7BluIkuVnIx6lfmsp16NitKxnkd3NE_tLeqprovyvk_ew10LHclmttk6b31FGGH2ljz_Dt7l89bMHJWw58lnzznXA3ndris4mvWZTEWYrJhmN8jAfhxnA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5e061ffb68.mp4?token=pQDfMqViz049cOnJyojQa4rveg7cCSKL1-whKZ0mDYv7rgth1h5We_JMR96aztG2bIgcWfZiS8_kvg0zr0QD-stnSL87cRVB11xHwngeQ1hoBJmKIRUtBPLobDzfFx9OAcaPbsVBJmv9PxPAK5plZeVsbw_Q5b20QMsMqkrHM9Ss8HQrBPORvmfxLFnnlUIAXM92l3qF8wL_8EbQiDWZTXk_F34jrlspL7BluIkuVnIx6lfmsp16NitKxnkd3NE_tLeqprovyvk_ew10LHclmttk6b31FGGH2ljz_Dt7l89bMHJWw58lnzznXA3ndris4mvWZTEWYrJhmN8jAfhxnA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
واکنش دیدنی و واکاشیزومایی گلر الریاض روی موقعیت تک به تک کریستیانو رونالدو
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/Futball180TV/104325" target="_blank">📅 21:27 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104324">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dpG3BXhfGzElG1fmpQ5aftfSpnv5GRxe2Z8bV6edD5hlYaA2dzMV6w8YmOhmSBGjk0_2jgeRNGAQtX8rETwJutLsuwp2y3YSqnhsd53t3JlEuYaQQ5q_RBw3NwAXeOZMpb2pQOZtkzhHSRXTboUobkGQncPcGyENVHxgA5-_v23veFJEdfYGqqPdyYJDxV8jHnug-QqeddzpftDZzQ4cvSDNxC5Ry7lhzJG_yyp5VyF-xUuO9BrcEB8s0WGA_HvKptRvGsKB0p7KSY8c91S7GKVVrok1yxGsJYigVcnyUE4gb644xyF5DpOht0lsueaUVo3UxW3dGva1Oh0ybml16g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
🏴󠁧󠁢󠁥󠁮󠁧󠁿
ترکیبببب آرسنال مقابل کاونتری‌؛ ساعت ۲۲:۳۰
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/Futball180TV/104324" target="_blank">📅 21:23 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104321">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d5c212597e.mp4?token=M8jEGy-trPMjam-15lNDUKnctVjQ4AT518DNSUhcMzIGl8MbckUi94BbR-cXtVOAiVQa1zy-3hve7GY4dxNztBrZdPUKWC3ePF5v8NCX_0SYKxxl55WrS_MMYVY5qICFNzgPsmmsJ-YMyuhHI5pRCRTQiB44-ByXrwcFV9_M7qkw7Gmqti9ayLZLarZE6K-T_6peI4rDRstaheHtoqo4ah4zAe6frsf23hzN4GePDbTXV-sWWQyH8JztQb1MF-gUYXufXmA0R82LVOFqP6hmY75-tcppxKh7k9C6ZsWBhKqut7OnUV_yfrvPQIMi1icgL6x_685nDVXSiSjA4oxdVQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d5c212597e.mp4?token=M8jEGy-trPMjam-15lNDUKnctVjQ4AT518DNSUhcMzIGl8MbckUi94BbR-cXtVOAiVQa1zy-3hve7GY4dxNztBrZdPUKWC3ePF5v8NCX_0SYKxxl55WrS_MMYVY5qICFNzgPsmmsJ-YMyuhHI5pRCRTQiB44-ByXrwcFV9_M7qkw7Gmqti9ayLZLarZE6K-T_6peI4rDRstaheHtoqo4ah4zAe6frsf23hzN4GePDbTXV-sWWQyH8JztQb1MF-gUYXufXmA0R82LVOFqP6hmY75-tcppxKh7k9C6ZsWBhKqut7OnUV_yfrvPQIMi1icgL6x_685nDVXSiSjA4oxdVQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
🚨
🇮🇷
‼️
تاجرنیا با کنایه به پرسپولیس:
🔺
اگر استقلال قهرمان اعلام نشود از طریق فیفا و AFC اقدام می‌کنیم اما مثل دیگران با لابی های سیاسی پیگیری نمی‌کنیم، این تبعیض باید تمام شود، آفسایدی که قهرمانی را از استقلال گرفت از ذهن هواداران پاک نخواهد شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/Futball180TV/104321" target="_blank">📅 21:07 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104320">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BUSNfbuxDFI3MRANzcK0LsMATTulkW2D3uEKs_mVgsQghNiFHcFCJFIBa8x0opG7aJMMIL5fDieJGvjIcWBng-wDi1KL2uK4wgCb-oVP2ULicxWCrmdBOrNzfyEqoQo2G_jV-rYttbC9T6JBKrrNQvZwHsdD86Bp5YZsd1SC-Wmc0oVPnKNa_6zhB_-E8jNzBBIzMtYAcSnNJOvG6-aSVeKBRLtZ1q_STlofo5aSBp5BYhcDJSKmycLefa9oeyV0G9KRLJQ6L6VLPe9BpSaggZvLrlGpF_RuyyZ-5rafXhuSDI3JuJnCWzya7gXhw5e5b_NLKSysT2RzhIh5-8lAqw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🇪🇸
🇪🇸
لائوتارو دل‌کامپو (El Ninee)، استریمر آرژانتینی و فرد نزدیک به اطرافیان خولیان آلوارز
:
🔻
اگه بارسلونا مجبور بشه منتظر بمونه تا اتلتیکو اول خولیان رو به آرسنال بفروشه و بعد سراغ خریدش بره، اتلتیکو هم باید فکرِ خرید بازیکن از بارسا رو برای همیشه از سرش بیرون کنه.
🔻
یادتون باشه یکی از جاذبه‌های بزرگ اتلتیکو برای بازیکن‌های سطح بالا، موندن تو اسپانیا و مدعی بودن تو همه جام‌هاست. اون‌ها با در افتادن و جنگیدن با بارسا، دارن پل‌هایی رو خراب می‌کنن که قبلاً باهاش امثال لوئیس سوارز یا داوید ویا رو جذب کرده بودن.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/Futball180TV/104320" target="_blank">📅 21:01 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104319">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ZxDEBtFjLLVbZcccyCUWti8K8fwpM0A_5iUnWcH3Xk7GEmpB-dFwqiHSsyJOI515KpMo2tFnOMLkqZb2Yf_Ri-QjiE814qg5JgVfiE44OrSB0lGBKKxLdiJmMvCWvW3en1GlWl4XKaJZfapmtTMtO6oMgxIFKFUYY6H7zZSKMhWoyEQnvI9d6dy4zmoKGtSJsaY6y6qpm81BSTGfsTFvQWd-ARzhKZEDMOW5KUvxzJrEONuWB8lg3Kw0e2PrkwrAIOUL8zeYxxgmfIr3bX5_dbpttvMsi3HzkYqRz8giPBN7x9Yf8bKBA5WnxXbgKVkhW3rHXHFxeqpyhwNTqUHduA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
#فوووووری
از بن‌جیکوبز: باشگاه تاتنهام بزودی قرارداد خود با عمر مرموش ستاره سیتیزن‌ها را نهایی خواهد کرد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/Futball180TV/104319" target="_blank">📅 20:40 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104318">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rTosNLufTjqVjRc7GcRFI2KY01JIoQ11Ie34xfqha4_D4zqiLCpZ3d3Pxxqz6dfABQaEJTnYH6BhlfYbdNKnY6vtJkml-liFGs3UtfnKEyzGTbiTvnQ00apoZZpzrips8NdsYK4_yshQhff1vEJnfVpjMxv5QQelkBmtzoPs6kVY0jRhl4mDU9_z61yMG5zJgXNjy8zF06alE1r9OnVo97h4eeYSLKeGckJaT-LSAraEAF4NmSI6YkxCjRDe3pj2hp2KrjxZRjQykSlRHZtE7QtIVylOJCsbCJwtowZ6JoNHgnCVN62awxxQ29OEK5Rix6F_wvTrYRzQZsgQbpdQ3Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">از بازیکنان لیگ‌فوتبال بانوان پاراگوئه
👀
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/Futball180TV/104318" target="_blank">📅 20:31 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104317">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/C9a3-IwxwLgC1kxHKN1uyVJdMcljZIaqqHt6qLvt7KQLMotCEAc3Aaao3YldaU-8tW8rCAPR6s99YhIJhzq-xSIPK6dIzMWiMO5A6pfOesESm9vxrwqfwq_1KkV0u2BOHdgubu5SqbBT8_uugRPsJDe9FdgCTvJ3_Tfb8KgFWdRmaHbXDwPIDVvMr3YivIhoLlQRZQZXMHGU2ZiZq8fI9TRjPcFJzNIeVbPv3DuISC9_u18JyBHkGac-1Q-f-GIVTBU9XjkEfQ7eXiq32FFhuZ6aByeGqAFLGPcJRbU14ZWRytq1N6JaL9NhdfjvYGHUE-own_xLlkL2PDCX6-ONjA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
میگل آنخل خیل مارین:
🔻
اتلتیکو مادرید به حمایت از خولیان آلوارز و کمک به او برای ارائه بهترین عملکردش ادامه خواهد داد. این باشگاه اجازه نخواهد داد باشگاه‌های دیگر در استراتژی آن دخالت کنند یا تلاش کنند تا تیم را از هم بپاشند.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/Futball180TV/104317" target="_blank">📅 20:26 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104316">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3c62d1ca0c.mp4?token=Qd6SqsiZeA3n1pm8XNQyKqVSQxjfRjEP4fSDkqLs-hmxoTl64S5H5DChUkLn8oVHaw2c2-3m2kd5drpwlRbAqkw1aIG4sEJaAIrrzsf7uURRQZQRolFU9ug7HZMfrn41TulChRhiJbHIvWrmPTpIGEdlzyRxpRZXT22QzFpyqrkvQckMJIl29cqL__ORBSItPcMVPd29AVu8MXro_IcceBEOFV4d8Opt7pN3DDhqAIvdAbWWIEySERlUo1rzsTU5OAwDyGienohuAVkiufjqb6BNW0C2BUPEzvtH4uYXlrLI_MhJ8ZGZvxw-NXLM83Gm8Hvm6Ee7lLVfbdYfupGH6Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3c62d1ca0c.mp4?token=Qd6SqsiZeA3n1pm8XNQyKqVSQxjfRjEP4fSDkqLs-hmxoTl64S5H5DChUkLn8oVHaw2c2-3m2kd5drpwlRbAqkw1aIG4sEJaAIrrzsf7uURRQZQRolFU9ug7HZMfrn41TulChRhiJbHIvWrmPTpIGEdlzyRxpRZXT22QzFpyqrkvQckMJIl29cqL__ORBSItPcMVPd29AVu8MXro_IcceBEOFV4d8Opt7pN3DDhqAIvdAbWWIEySERlUo1rzsTU5OAwDyGienohuAVkiufjqb6BNW0C2BUPEzvtH4uYXlrLI_MhJ8ZGZvxw-NXLM83Gm8Hvm6Ee7lLVfbdYfupGH6Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
🇮🇷
🇮🇷
خاطره عجیب حنیف عمران‌زاده از شکست سنگین استقلال در دربی
:
🔺
آرش برهانی را پرویز مظلومی وینگر گذاشت تا رامین بترسه ولی رامین در محوطه جریمه ما پارک کرده بود
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/Futball180TV/104316" target="_blank">📅 20:03 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104315">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2950ea1958.mp4?token=FWE1Y64LMnjCFlOowyet9yunmTNFoLtvHX8zASl--oeHDffWgJQ5mY-CZkT0JZOTvyR7csYU-UgY_o7NDIfcg5UL06FMgDGFMYrt1qQBE3nBe97CRgyhm87IShV0c-wgJJHiIMLpwsK82RjVK8VakRkA9bQqMhJdeA52yloK88Sn5YI1BmFN-703aRLfPyY7b3vxtiys1h_oCUYs4lb7lNQDSBf-Da60ORddZwzsognIFXahbpU13U1UivBzC8-tTc7eLibxpTm4dLR5Xbw5v9gGZjVWBrvavrs95RginxH6AWJUFsTuVwUNgU3ymANA0pIsksSWYBgjPYoRWYS-NyzZqKvh2EAoul_XIqgoGxV1ekjtZrRfZK_i9JUAwoM5pSYl1MykFGI5lWzOzjb3nrczIBSY1OoaZuMxSFSAJ3l7Ez6D9sp9RqS5RXChuOPyi3yA9OJc7REMocCMX7JsLVF8obLXgq9q5UkIPttPqH1LV0ZF5A57N4cK0RJa61aNJl5qWyqF1dq-0T_8ggrrw59JRXU1VqLB92jwfdHI8XLRBkizc33GjzACerheNUzJyHQ9YTm0R9XU7DtQ8oh_m1piiJGyecH8DOT11LDeVgxMSzj5dwDkPKycmtH3NWsv9yP_mjzdI8UlzrThOteSAbrMjxoO4AadAIoeFrtDIOQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2950ea1958.mp4?token=FWE1Y64LMnjCFlOowyet9yunmTNFoLtvHX8zASl--oeHDffWgJQ5mY-CZkT0JZOTvyR7csYU-UgY_o7NDIfcg5UL06FMgDGFMYrt1qQBE3nBe97CRgyhm87IShV0c-wgJJHiIMLpwsK82RjVK8VakRkA9bQqMhJdeA52yloK88Sn5YI1BmFN-703aRLfPyY7b3vxtiys1h_oCUYs4lb7lNQDSBf-Da60ORddZwzsognIFXahbpU13U1UivBzC8-tTc7eLibxpTm4dLR5Xbw5v9gGZjVWBrvavrs95RginxH6AWJUFsTuVwUNgU3ymANA0pIsksSWYBgjPYoRWYS-NyzZqKvh2EAoul_XIqgoGxV1ekjtZrRfZK_i9JUAwoM5pSYl1MykFGI5lWzOzjb3nrczIBSY1OoaZuMxSFSAJ3l7Ez6D9sp9RqS5RXChuOPyi3yA9OJc7REMocCMX7JsLVF8obLXgq9q5UkIPttPqH1LV0ZF5A57N4cK0RJa61aNJl5qWyqF1dq-0T_8ggrrw59JRXU1VqLB92jwfdHI8XLRBkizc33GjzACerheNUzJyHQ9YTm0R9XU7DtQ8oh_m1piiJGyecH8DOT11LDeVgxMSzj5dwDkPKycmtH3NWsv9yP_mjzdI8UlzrThOteSAbrMjxoO4AadAIoeFrtDIOQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
🔥
🔥
🏴󠁧󠁢󠁥󠁮󠁧󠁿
Premier Legaue is Back
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/Futball180TV/104315" target="_blank">📅 19:32 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104312">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tgZhOIJhp1fRI9WrkNfuQy51PEIajKG0YEYrYVlboBpwk-ubAJErLYZUmttsaaLvie4W6HHX_k9T4af815QV3aIrVqbLin74H56g0Bd1Cm9uSTM65cahp9xMWFfKIVGGYGiQ5KuyHqBMV9GtJgrVULr8WgeWgd8dNsRZ2BIQPONT8H3UDjlfiG7nhIE_e4541ipZYowIQv_q8tJQ3Vy4ky0tkIySbF9AkAAK9tfg0mSzpoMo4Mp1-eAx0WNJBBWMeX9TwgYQOmOEVTfvYXDNH5gXOY1tsIMxH0uYnjPwoue9OQiCl9uJiODiNqyDAf49kVORLbCsZ9AYS5sc-46whg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
#رسمیییییی
؛ قرارداد رودری ستاره جدید باشگاه بارسلونا در لالیگا ثبت شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/Futball180TV/104312" target="_blank">📅 18:41 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104311">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">👀
🤯
یکی از سخت‌ترین مسیرهای مانع جهان ملقب به «Obstacle Course Racing» به اختصار OCR
🔻
ایدا ماتیلده، ورزشکار حرفه‌ای این رشته، وارد مسیری می‌شود که برای عبور از آن فقط قدرت بدنی کافی نیست.
🔻
بالا رفتن، پرش، آویزان ماندن، حفظ تعادل و عبور سریع از موانع مختلف؛ هر بخش، ترکیبی متفاوت از قدرت، استقامت، چابکی و کنترل بدن را به چالش می‌کشد.
🔻
مسابقات عبور از موانع، رشته‌ای است که ورزشکار باید مجموعه‌ای از موانع فیزیکی را در سریع‌ترین زمان ممکن پشت سر بگذارد.
🔻
بعضی از این مسیرها آن‌قدر دشوار طراحی می‌شوند که حتی ورزشکاران حرفه‌ای را هم به مرز توانایی‌هایشان می‌رسانند.⁩
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/Futball180TV/104311" target="_blank">📅 18:23 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104308">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lZMcmNOEBZPYqbuozxhxdQ8-EHbuoNV87zYvCdEXXdZ0R6lFLuxz9Y9iJRZEr7oFxX6O1L-sNudp4nyWY7pvL3tiOgf9ayDG-zEMPDj28uowK6AdIkgQoQwKyONsxZSuz9RbEVUUmLTr0iZPeaI31OF0V6UyGpfZT_OZGLh69DzbPd8SA30fbkoiQigXAJN5IjWEqlLBEYdwGqtVIw3Jn4SzJ5yWYR-R_jwBVx0B4WJ2rV0oT9SPo5zP9XpSQC546uLiXFZETanFcRS7E-6FR6XgVc-TGZamA3b8OY4wV5NgdaKTOQBoZKQ3lfC3Nk_MNnvB5RWim4WoT0U1UPrSlg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇮🇷
#رسمیییییی
؛ باشگاه سپاهان اعلام کرد که سعید واسعی و امید نورافکن بدلیل مصدومیت دیدار روز یکشنبه مقابل استقلال را از دست می‌دهند
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/Futball180TV/104308" target="_blank">📅 18:20 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104307">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qoc9IFcFVhPcHDTvTi7H8_cKgkzE1YCBIy8TZ36lRoGPm4WrfRRvs0IWmwvSS1HVPFSy70JKTg6ugzFxcdWXb0rw0qb8Yhk6h7XWkKTMGsuRUSi1SOi-u7SZ2H2W4eVkZ_BnVV7d0J9TcKTezNMCUxjssHehFxnjdoITYm90tBF4RD411CM4vKWgBm2h-WGY8XXYQ9PVWvJNM9MWFbtu5BFOpfRqOB_6z7uhViTY7mQcV6pT11AqqVguD899g8MQPqNey0pN8PyQtcuE4_96M4_SUvbwTALRm_uVo4_zeeMCGkFAncUItfIPqX-xX6jSAMhfFIVE_UhZwaAMcsrgww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
🇵🇹
نیمکت‌نشین رونالدو در بازی امروز النصر مقابل الریاض در هفته‌دوم لیگ‌عربستان
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/Futball180TV/104307" target="_blank">📅 18:18 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104306">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/nqg45sNiECcUggbEHUcuDR115ixyglrBP9o3wB_DdbDWc-PIyubuGd_fUP9iFXc4upbyd-8xigiG86yB8wZHxjiAXvzbtaWtPB5Q-CzY56gVbQnUXMrKtNfrMxAb5qeI8KVdZt7pnYiOvEdjWNPS1LA_V8DTLFGNSTljwj-F6NxNPBCt21-tSi6D3vihpIoJzQKNaTpW-J85vvFy2YcEu3zubwy4UXGGg5xEkbORycIxAgXVQAYuQ4gDAjz-W5kOEFYpyCr6_H_-Yn4_row_m0L2zjW32jKdwYJoLPHQtRc5HFD5SjtRLjhzgRcFBhRmrCNqBD550wLqGxog60sObA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🚨
🏆
#فوووووری
؛ جرایم انضباطی فیفا پس از اتفاقات فینال جام‌جهانی فوتبال:
❌
لئاندرو پاردس: 10 مسابقه محروم شد
❌
مولینا: 7 مسابقه محروم شد
❌
گاوی و آلمادا: هر کدام 1 مسابقه محروم شدند
❌
فدراسیون فوتبال آرژانتین: ۳۲۰ هزار دلار جریمه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/Futball180TV/104306" target="_blank">📅 17:45 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104305">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Y7aFej_mcsJj9_h27QttjQUGUhYcFZDlva4vT3T1fj1MW8oj8QY1mww9McLLYefgV1KZ-L7KtFClo4zh_nECu_ArW88EDvgJAssnzq-zBtl5r5xGVS7bwspMd60akp-lmXoH5_HL-bSYEF3snYr1X_Ty39FMkfH5l_vEUxZsfS0uO6yfFPEiQX4TowayuobGWqTCz0hVN4RRG2UKfIcuj-AAt7y8uK7qlrGKLQ3hKHm9dTww80y_F2whZL0aojPYK7qBsqpM8huyiACLPdvyMTVRUD4xbdynJPeDmA3HuIcqAHa4PoKZiUXjhxWBZ7u2Uk3Gu0Pt4hcGvcZPLFaVLg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
🇪🇸
لیست تیم‌فوتبال رئال‌مادرید برای دیدار فرداشب هفته‌دوم لالیگا مقابل اسپانیول
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/Futball180TV/104305" target="_blank">📅 17:33 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104304">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bP1B5095_haA_Y6XuK9Z5mYKZMw0VoWhISwv8mljS7GifjpnL7IV9dthY-eB9WnwxOe8pIahBbJQFPkEUZd1E9HywiHq5LWqf59YrnvxgREXjvtvhKy9jUzAEEDml9_r3dIq5pikczhV4_2b0yrv5SzDmSJw1dOkLJGuRiH2zT0NCxc-o--0y2SoyzsIdbukgcJd84rxaFDSSYawLMVqRcNTxllwZ3NjNIYKc2FRf9aK1C_Fpvs-kCVFvQGEb3zHuKlrN9XK-gLjjdg5uxclTZr7br7-QHuyAZiM2qhjvL2XiH4LufK_DjTKjwaLB2wz2HMFwjrsfY9PD9BrQ4BJag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
اتمام حجت اتلتیکو با آلوارز با سه پیشنهاد:
🫱🏻‍🫲🏻
تمدید قرارداد و عذرخواهی از هواداران
😡
سکونشینی تا پایان‌فصل در اتلتیکو
🏴󠁧󠁢󠁥󠁮󠁧󠁿
مذاکره و رفتن به تیم آرسنال
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/Futball180TV/104304" target="_blank">📅 17:24 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104303">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2a482d69c0.mp4?token=FuNoOcQ01Jb-qEEXwzhHree0Y3yAkaYV2D2mK7liayAIpK1LvA-2PA-tkjQ7AWX_n2fIEPF15nH_unYQSqHdZ8wGkOlX8E4P5U4GM_1lebo7CParLjitqoSouSfDZkTyvRnUItLjuS_8HwQK5pRqV8JSkGbtJsw5RLrv4MuQJS9-ei3VFaayqV3dccLoPdvKxIqIzFAJQE1RayYR08AYPmpRVZq4KXbqWm37lFXD36uaXzgPBga2UnTxE9BB4_0j3dacebX71xCNQFHoClOtSpKP-1_SAdwNxHY_FL8Z7y2Qq7PM541ck8p59Fk6DZAOCHfJ4Mecf0SDAfC-Z4VVvg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2a482d69c0.mp4?token=FuNoOcQ01Jb-qEEXwzhHree0Y3yAkaYV2D2mK7liayAIpK1LvA-2PA-tkjQ7AWX_n2fIEPF15nH_unYQSqHdZ8wGkOlX8E4P5U4GM_1lebo7CParLjitqoSouSfDZkTyvRnUItLjuS_8HwQK5pRqV8JSkGbtJsw5RLrv4MuQJS9-ei3VFaayqV3dccLoPdvKxIqIzFAJQE1RayYR08AYPmpRVZq4KXbqWm37lFXD36uaXzgPBga2UnTxE9BB4_0j3dacebX71xCNQFHoClOtSpKP-1_SAdwNxHY_FL8Z7y2Qq7PM541ck8p59Fk6DZAOCHfJ4Mecf0SDAfC-Z4VVvg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وقتی توپ، داور را از بازی خارج کرد!
😳
🏐
🔻
در جریان یکی از مسابقات والیبال در سانتو دومینگو، توپ با شدت به صورت داور زن مسابقه برخورد کرد. ضربه به حدی بود که او دیگر قادر به ادامه داوری نبود و در ادامه، عوامل حاضر در سالن او را از زمین مسابقه خارج کردند.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/Futball180TV/104303" target="_blank">📅 17:03 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104302">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">❌
واقعیت‌های فوتبال امروز و‌ ۱۰۰ صدسال گذشته
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/Futball180TV/104302" target="_blank">📅 16:34 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104301">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7b4df9ad5e.mp4?token=L62vUZ7GlGvUulCdqo0BOBsPKk5n9Cz6JLGnO1WjNav9PyCIEDLEZwe-xmig0r4_KoyJZsVpfvvqxr7PFQCijE2UDLPtPBUGNbQB0BqboefPY_-kViOxHhJUJu_r-L6oh9i0YyPHSV9Gmq5CUWuo21RQCHPDODtjUjP5t2waJyg2rovdxIorg9RRRoqWFhnhKDKuJ4Zlkrzls7W2sarJRmund8EfWBE4LZb0vfDNuUmpqNX1CAZpIkAq0v88IjW-SwNqgiLr4BOYEJGM-9xCHonhOOhhiuooOmBPge6Fo65OczRwkS3sBeBbIv-gTcBKmtk-QNN8X5VPkNoUJTwj3zIzq6_ElohpWEP_zkzeLP77PCpbV5RoPGbrTdZsQUb_ibWwgEgYFu28kGcCCVylxNDZql5w1Fnqbu20Jwhb614MFtdUZ-eXwia9BUZwpHVpGTtuM0PHKTCPsh9SOHqtCQv8DqWsUR5pCdNnIh5IsoQvKrB7Q-YmVKy-fWcNyLUGNo7XD7-lK3pIwHrCLuHhUeWUMaJg8VzLPyxyrZjidEwrW9nqq-YgKI7AbrAXFLT0CoOALkgufwgEmlmg-CF_QNaN1YO09KvulJsSQY4SeVlsPqbWXH05GfBjjMI5lDCP1O6cK15i0KoEsPFm8ul4mIZtvKnIDyl4y7QY3KZ2KDw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7b4df9ad5e.mp4?token=L62vUZ7GlGvUulCdqo0BOBsPKk5n9Cz6JLGnO1WjNav9PyCIEDLEZwe-xmig0r4_KoyJZsVpfvvqxr7PFQCijE2UDLPtPBUGNbQB0BqboefPY_-kViOxHhJUJu_r-L6oh9i0YyPHSV9Gmq5CUWuo21RQCHPDODtjUjP5t2waJyg2rovdxIorg9RRRoqWFhnhKDKuJ4Zlkrzls7W2sarJRmund8EfWBE4LZb0vfDNuUmpqNX1CAZpIkAq0v88IjW-SwNqgiLr4BOYEJGM-9xCHonhOOhhiuooOmBPge6Fo65OczRwkS3sBeBbIv-gTcBKmtk-QNN8X5VPkNoUJTwj3zIzq6_ElohpWEP_zkzeLP77PCpbV5RoPGbrTdZsQUb_ibWwgEgYFu28kGcCCVylxNDZql5w1Fnqbu20Jwhb614MFtdUZ-eXwia9BUZwpHVpGTtuM0PHKTCPsh9SOHqtCQv8DqWsUR5pCdNnIh5IsoQvKrB7Q-YmVKy-fWcNyLUGNo7XD7-lK3pIwHrCLuHhUeWUMaJg8VzLPyxyrZjidEwrW9nqq-YgKI7AbrAXFLT0CoOALkgufwgEmlmg-CF_QNaN1YO09KvulJsSQY4SeVlsPqbWXH05GfBjjMI5lDCP1O6cK15i0KoEsPFm8ul4mIZtvKnIDyl4y7QY3KZ2KDw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👀
🙂
بعضی‌وقتا دیدن اینجور مسابقاتی‌از فوتبال دیدن پریمیرلیگ ایران جذاب‌تره
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/Futball180TV/104301" target="_blank">📅 16:05 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104300">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">🚨
🚨
🚨
🚨
🗞
🇪🇸
لیواکوویچ سنگربان تیم فوتبال فنرباغچه ترکیه به باشگاه بارسلونا   HERE WE GO
✅
✅
✅
✅
🔥
🔥
🔥
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/Futball180TV/104300" target="_blank">📅 15:31 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104299">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/K6jcCIpZHdmnJ847hyxzaa64woINE_IIZbamz-LNcNG-FxySArcWm8uhXSBKGOvn9xZfA-Q8WOj2eWjo3DQx7dKkSU6PJGjRBSb-TOY4Qm4CUuBQ3wtdS07ikaYQxa7YO0sbUz9sFhG03Bd_go-U3s2W3xVe0Y3It1_KXYX71V8LxWax0Qf-gDGwRiARnWdqd1e_AZg58vEApZgrtlBGjqVPU_FDzvC4e9A5Wko0U-OuOoDSysm1R2enSd7RFWI7fenlECyjp7xiNztt9BD8_kNbN-ooDONQ7nnW2Hvxi3idNU3jZwZo_5XEJAhndNCRasM_IBE2ZLOPfAefm_faiA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
🇹🇷
#فوووووری از روزنامه اسپورت: بارسلونا و فنرباغچه برای انتقال لیواکوویچ به توافق رسیدند
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/Futball180TV/104299" target="_blank">📅 15:27 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104298">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fuGU0PRFEoEduhtDai4oYVn2rELKRWx9VwAv8KegKXi7uRpM3eRmRnSxNjU_HWHGp7crq1rlZpADACSaSBvO1RHWjdGqsLKhNEhXfxlMmUJkVnsNYn1qWRh5_Fgz81gMtyR6K1P4xevycor2-0Vv3ngiH-Q9m2i2EXvDQkkVFN5G7acYwQUaCxgnXqbzLgkwXk3i_OAGVmu4onYrladss2xMRij4Smz6IxzjadQKXylgU3K0byLYLQk6ATNfvnT7UC5DA30ZbJwZmVMWlnEK_Ap3tIkYxUeCLGDDueA0_3nH0GCmdcIUGfmf5GVXKKUdm7PsCMtYja0Y8pDuIZjlkQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
🇹🇷
#فوووووری
از روزنامه اسپورت: بارسلونا و فنرباغچه برای انتقال لیواکوویچ به توافق رسیدند
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/Futball180TV/104298" target="_blank">📅 15:21 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104297">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sP9cfiqGMkU6QBY5r5B8lRi5p-i_6ug2vM1yH3Dk6BJBJcgTQBQ48IjMqq7v11SQ7ycaDkOCWXHeUcsiWksFtPlJQ8LcQt29E2phZyNiNupbAvNaCJ4hix0t2VONNC8aPUwvbMXaG--nA_69VPdTFsnHK71VIjm06xpw3DINuJnDjtZN62aYSvPb8HDjZW4E6lhdL-IpIT5kiwwX27FBadWeEuODG3hZZPEU4HiXUdjIic4X5DwEQWl8SjNchFRFyQuv8Q9r6sEvA-I-P1KRC4pLT-yGEiZezDd6P-fgtCtb_B1EWKXTVyq-hmA0fEevctPnaqWDVWYkEoygJZ3h7A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
اتمام حجت اتلتیکو با آلوارز با سه پیشنهاد
:
🫱🏻‍🫲🏻
تمدید قرارداد و عذرخواهی از هواداران
😡
سکونشینی تا پایان‌فصل در اتلتیکو
🏴󠁧󠁢󠁥󠁮󠁧󠁿
مذاکره و رفتن به تیم آرسنال
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/Futball180TV/104297" target="_blank">📅 15:19 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104296">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FXG8V-OYOjhXwUu6f-Y5iN5pIljCU_K4Mk5X63bFCIh1lkuFSMkBy4SWBpLw9l61Mo7vpfyY-0_wG0lB8O14mw2J2GkP_ySsLp18MRnQGvMoLqy0nJY-LwIWnGO5CPIBe7dKBKBZavXqdLieqKSAOeiVdk0K-QixMBwUJX9sGILeKjnWncumG3KFiHMDGthFFXeNDQlb4XKBK6iLWvr6Y9KsHLE_wUN6vgrMrI77284L4oLdBoW8oEEyXuYA7fc1kyik4tXP3cWf2DJxZKYGrzFlHjfB5RhwDJl-On_O3vION3qUdcJ1YxTJXZE5Fu97DQbCWnruZiJ7hBtji77c8A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
میزان هزینه آرسنال برای بازیکنان خط دفاعی
🇳🇱
یورین تیمبر — 34 میلیون پوند
🇫🇷
ویلیام سالیبا — 27 میلیون پوند
🇧🇷
گابریل — 27 میلیون پوند
🇮🇹
ریکاردو کالافیوری — 34 میلیون پوند
🏴󠁧󠁢󠁥󠁮󠁧󠁿
بن وایت — 50 میلیون پوند
🇪🇸
کریستین موسکوئرا — 13 میلیون پوند
🇪🇨
پیرو هینکاپیه — 45 میلیون پوند
🏴󠁧󠁢󠁥󠁮󠁧󠁿
ازری کونسا — 51 میلیون پوند
💸
🤯
🤯
مجموعا: 281 میلیون پوند
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/Futball180TV/104296" target="_blank">📅 15:14 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104295">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XsDBhvJ0GfaepJPAtPXF_-JE4jBgzYmNqRRBKH-nc1qPb6SEovnS4XhQUqhRQX7ginG-uwFb-a2MaVJotNwxE4LFqyHzNV4rRf8VW2jtQmFl1hAzc0Qw2QQ0FGcaVeKjoVfLXq0lGMdcELaOX-emxjTomFdxuZDWvsdA3vb9-DFjVi6J5vEGlxX7lp3pnU-hTJWvVB0Eil4pa01evWxdHNSaZHQtr_nNqIlBcu0kPVyPdIVmjw8bsK0vuKm_7oI3LcKkrTUL8_w2COAfPJc36y_Z90ThV_yrteEas43mHV2RrloZzuaGbkFuq6lVi3YnlvQzvPUnEbZZXJHwNHLx1g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
ایشالا آلوارز تا ۴ سال آینده دووم بیاره
😂
🙏🏻
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/Futball180TV/104295" target="_blank">📅 14:50 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104294">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b326cd073e.mp4?token=pb3SxEXFnqh1CB7XXwgrJLOqvkdUa7Reov58P_Vrkx0cKmnfCODma1xHbKEf_-F7sNWxcGZ_Kv-ZENpd4aznawEGlXRMTSQBbAAddRzIyuucULY-GdDSy29VVRRLijlR4Jk3BacPe_GKZDOoK4z7UnsZMfoFZHeyG52JdkHGtfNElmNNW47qmtFGRlOlwRozHdgp0pzbsqFVYAj99jokSXAdoGKOzU8QQX9BwxxYQE4qC04ugdKKE0mJPhlxuNxG4UcYZfvlGMEvZfBYoP4m_2Ne1Tt096PgDOi6PV0HT2p_gZ54c88CB_3QkMtZ6M9ps0HzZ94-f4bEjsu2uEwv2g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b326cd073e.mp4?token=pb3SxEXFnqh1CB7XXwgrJLOqvkdUa7Reov58P_Vrkx0cKmnfCODma1xHbKEf_-F7sNWxcGZ_Kv-ZENpd4aznawEGlXRMTSQBbAAddRzIyuucULY-GdDSy29VVRRLijlR4Jk3BacPe_GKZDOoK4z7UnsZMfoFZHeyG52JdkHGtfNElmNNW47qmtFGRlOlwRozHdgp0pzbsqFVYAj99jokSXAdoGKOzU8QQX9BwxxYQE4qC04ugdKKE0mJPhlxuNxG4UcYZfvlGMEvZfBYoP4m_2Ne1Tt096PgDOi6PV0HT2p_gZ54c88CB_3QkMtZ6M9ps0HzZ94-f4bEjsu2uEwv2g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
🏴󠁧󠁢󠁥󠁮󠁧󠁿
وحشی‌بازی آرائوخو تو تمرینات لیورپول
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/Futball180TV/104294" target="_blank">📅 14:25 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104293">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/R52IU4I4pelMCvKX-hVy3IhcA7GgiW-_8c78hjl3og2g7y7i5Vk0SDM-eh40jk6nk_L7u95jpF3R6YqNA1fICkeWwRO9GP3bnfzQHKB17J7NwG_8wj0WjTLfBidWZVrSeiIyt-Q7DIjAwjp_VgolbK-6Yn7mEYZKBOsdGpD1niGvPlZuzuf-Tm43XYkf5qbvMVYgRac9cP7_CgSVu41q-eCZGcnPDyzM2uqgOUcPQs7tx7fUDv72VyWA3AF67gI3QPEHiTVBPjQcf_Ld1ABCMFrjGgk00bAyR6PivreqbulrViNuXRuvgqLnU2rE3VVI_rEBhTcYT-N0Q7QYQv7IKA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🤯
تمام تیم‌هایی که ژائو کانسلو در اون بوده!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/Futball180TV/104293" target="_blank">📅 14:04 · 30 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>

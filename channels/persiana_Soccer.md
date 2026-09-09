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
<img src="https://cdn4.telesco.pe/file/GE3yq8bkQ16p5KfNgI1Kp4BiaWvo7k82pOjoAtIfgr7CN_3e-D_u626RTinhoyhxxvIOD37Xu5BTiOoHmluS7jeCeiZScrC_OIWsiB2LHY6f3UKXcLef9kLtd-TJiE3VbtxzSmat7FKUqHvjkh_SS706tejLDHlzq6WVutfTtiLr1_5g-5V2_PeDSER3hsoW5zVw1CGif_BMggM3R24N5QGKJoNHJvFiJDmQzjS2RFOcBTlIAaHrUbpIW7YBmEtddo1HbPqGmqv6om9zPC1otoRkCS_IKZtBgLmxg1Xl8kybYdnXEaPoCOMMZC2sVA585RyybcvPRUf0hPI9dG2gZA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Persiana Soccer</h1>
<p>@persiana_Soccer • 👥 550K عضو</p>
<a href="https://t.me/persiana_Soccer" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 پرشیانا ساکر دریچه‌ای تازه از اخبار محرمانه و داغ فوتبال ایران و پوشش اخبار اختصاصی نقل و انتقالاتهماهنگی و رزرو تبلیغات:@adspersianaکانال دوم رسانه مردمی پرشیانا:@Persiana_Plussپیج اینستاگرام:Instagram.com/Persiana_Soccer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-18 19:06:53</div>
<hr>

<div class="tg-post" id="msg-29384">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rM8e0Be2-z8LOx4_Y3KNjqhaI5sU-X3NHSKau5wa0D2e_-zdDBdIbuknhN3XgXsVdelmGaePbpbtqm1HN_JnST609OnsgxaHeM9L8EI2QDVf0pu41Mmd2wTY46NbURlxWFXSSTVL5q1GTn39A-uWkWysDq1EaJMc4hQB55Nsfuf_i6bAx9k22kRgFBzxNP6swvtp5xkrXDH-kRnsZqPgKK-QJ98I_rudF_RjN431D_NYKFJ2mdpsdx_CiwDAuAlphkVgvQzrTLVTW3i4hB5shUw8lphET4ydSLofP08Vrdqk1WtHzm2MZyzH54VfcyY3hlGvaOq931HrV5o-dqr8Rg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇺
هفته اول لیگ قهرمانان اروپا؛
شماتیک ترکیب بارسلونا برای دیدار مقابل فاینورد؛ ساعت 20:15
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 2.13K · <a href="https://t.me/persiana_Soccer/29384" target="_blank">📅 19:03 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29383">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/s3hv0ywSTFqRLo99mNobN8dk9BXD1ztau3aFZz_tx_F312MZ8Xvhyb2gtpulKqCWF5oUYo3UBDG8e2zgUZhpFNOkU84ii8so5u2ecBiGiGh90tXBKta9xBm1Kf051-ZqDGL3ictaXf_lQUQ1U_82NBzlQR1zKuIszq78FHmbcJDmSfmUvBSOwegdz78jgCbtnXJOGZ27GzMcsXXXE7XGVJNcAcG1obwi5lmhKYYGMj8pDADhAM5XS2Vnr-hoHq8Rlp-DET9_5c7QXTAC9zYccRpYUGzhq-Gal571Xw5WYrgCbD2GR0mCyLw4cVglgIGI-QmZ_NNchq23tipjvDOoiA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
👤
فرصت‌های‌برگ‌ریزونی‌که‌بازیکنان رئال مادرید در بازی امشب و بازی مقابل بتیس از دست دادند تا اولین شکست کهکشانی‌ها در لالیگا رقم بخوره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 6.68K · <a href="https://t.me/persiana_Soccer/29383" target="_blank">📅 18:49 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29382">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mtUYFPErhWm_buH4AOvM3zYJ-XL6AO_JZAm8BV8bjkVqvHXM3It8ZjAnvGuZc9CBMd7R97YRNMyDoyRI3djsiVLCXW0X68HSUIzi6IoNyLfCF2zBg6FSCSDuRApi28fz2BEUWo7OdIglfu9rd8vsMyTWnJGRq2hRRjqgssvOm9mLEQhnxrTFQN45_WBD-96Qbxm9NSmhXRfhCspncwP691yhOSOkOZKKm-KIDoS3e78T3sq-juC-iLju5qcFxE6RNOWLmXe7816wjDzdjTrZ24L9oyhInJdE0l29DyxetcFq8RfRFQFej4KelySnJJNpysrfhwBFG0ZehHpV8xKQ8Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
با حضور لیونل مسی آرژانتینی؛ لیست 30 نفره نامزدهای توپ طلا مشخص شد، مراسم اهدای توپ طلای 2026 روز 4 آبان درلندن برگزار خواهد شد.
⚪️
Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/persiana_Soccer/29382" target="_blank">📅 18:26 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29381">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Gnwlu6dqFI2QsWQB_hwdSsiOcUrKzx_8poFjv_zH36tl-aPqD6LPU79to6fCswh1j55-s6LPfomvbWAQ0kenjxectfnVK8zCzRb48y9v3b2DmQI0Abx-RlrIJF7LY3N9DZ5euwxKenNpVRAX9Qbt623TuovsArgjJe9PNh1V04Cp0OVVJ6HeSa7KXiC2JKLXgPMm1fQIwcT6WNck8b9CWwb3-XZsp0CRWAzG1jY5OPd0ahG9dxvtjNH-RHGcM9baG2oQbU0OKcLfSQQcADeB0ffHAXohUH0rA-rjNDk5N_LXH6PP7PsIjOgAYBWHwT6HC6DvQArzp4E4grn8XReo4A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👤
👤
لیونل مسی و کریس رونالدو آمادگی خود را برای حضور در مسابقه خدافظی کارلوس توز در تیم بوکاجونیورز اعلام‌کرده‌اند و بالاخره بعدِ سال‌ها این دو فوق ستاره در یک تیم همتیمی خواهند شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/persiana_Soccer/29381" target="_blank">📅 18:26 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29380">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromBetegram</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/n-4YbP9ZnEDj1iw4EfHWY4yGRmLNp51pt6Kbdy0s1kJQK5ALlIpMReKhSHZ8_GM0kr1teVYKeKr0kH4GC7w-Inu1wZi8oJLQXBuJFvHFpxneShMspDzjU5t0DHRZ4_2Ez-nJTkJCDEs5H977jJtCqjNt9pNScKYufSDclm_RffeiUvehSIY65XAOKAN3tX84FOKKepUoUq1k_-zFbkQaIWDydj4Df1zVqECsZWgkiFqI6QX_blQ1UPRXIbQyjrTBwkr9PTKi8awDriDowLnSjxfQmcRuVTH3nE1Ascl294YdXgGfUh2gFZQaMgwCVMD5u_TZu8BlhBxF9rrYIQyfsA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇺
هفته اول لیگ قهرمانان اروپا
🏴󠁧󠁢󠁥󠁮󠁧󠁿
لیورپول
🆚
اتلتیکو مادرید
🇪🇸
⏰
ساعت ۲۲:۳۰
🔴
بیش از ۵۰۰ نوع آپشن پیش‌بینی برای این بازی در‌‌ بتگرام
🔼
با بالاترین ضرایب پیش بینی
💵
واریز و برداشت ارزی و ریالی
❗️
🔥
۳۰۰٪ بونوس رایگان بر روی اولین واریز
❗️
💸
۱۰٪ بونوس روزانه واریز رمز ارز
❗️
🎁
فرصت را از دست ندهید! همین حالا پیش‌بینی خود را ثبت کنید و از بونوس‌های ویژهٔ Betegram بهره‌مند شوید.
🔴
http://betegram.com/affiliates?btag=3_l7</div>
<div class="tg-footer">👁️ 9.56K · <a href="https://t.me/persiana_Soccer/29380" target="_blank">📅 18:26 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29379">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CYQIM1eO7SdjJV1ZyICbXxxIBdxncsSDIQtZ2rINk2lpI6Cd9t1tMUR5amUldexCuWlWhlTUP4RLJTuV2U58tG0dFBpByN8i5JiSMBnhJebFXdgVTvuvhkXVYLKRUiu8S5ntz-olcqhebk3i01iGHWTkBHfQUz-v69RUf8wwjNCFSSGM3Fv0oYgjdsuWoIC0IgDW8rI0z2JEKg9Is4L2F2jfcfxp9c4OMixHcMUfK-7Ui3guGPITHwmDHASr5hAlH7LS3isjAVlT_yuqnKXSCy106d8Ka_8ssmNUbvCRuqB9zpMc_OSqZqBW_s9PjRVjhNR0UT8GeXgMhJ-yKZf8EA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
بهترین‌بازیکنان لیگ برتر تاپایان هفته ششم از نگاه سایت متریکا؛
مدافع مغضوب کادر فنی آبی‌ها در رتبه سوم! علی علیپور بهترین بازیکن لیگ برتر.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/persiana_Soccer/29379" target="_blank">📅 17:47 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29378">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZbDLfDpqlCN94zk4rOL6THLo2liDQaQ4Kbt5hIJZY7O3KEZYwzltb6vzJH3mKkhy5Z2VZ4E-NAsF9D9k3EOowbHtArzvWtKQTjuHda_fysTcyiV3DI-E9EFcYPcAKk_OwZcaZL8uFocOF7hHwkbWqQ53UNLnlFxDhi7DiyT_RK_zt6bkgzxBH62SUprSJYGxNKqxs7INf-zr7awA0DFeBh1OUxxCjK5a6AutYm0TdD2wYc69ZlKepF1dQ-CNC_W8qYQm2MNn2YtPCsjeZfmT-y8Nycd7YWeGH7m7eUkh-Obq1VzJKQ65_DhExUcJAylMhPuwXI-ukBrhQHTgHWB_XA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🍏
💵
قیمت‌های‌احتمالی‌آیفون 18 که قراره امشب حوالی ساعت20:30 بوقت‌ایران ازش رونمایی بشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/persiana_Soccer/29378" target="_blank">📅 17:29 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29377">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EaCCu9F7l1kicBoy-qmvcZ1hjXUjjpN0TcWlqFxVDG1U5mkbqEi2-2LW_QARR8A1g_hXNleb8aJPtAaOI5bF5y-_mW9KiKzezlInDlrmZWATt3MxPmvEFtj1b6LM575u2Zil6dXEU8AgEo7RRh6Vvp2lzeUccagjkQaX_tP1m73q56fLL9sfDVBCwjZtoH9zHuSuSWLqeESJDvIxaGUjES3916aEkJZzySf6TRYoVbMdo2RZUc3fx55N050wtGpdDOFCBIP7GleLRuipvAVGmRSgxK0htnvcmTDSuoHFxs4ZOsOdJd3laSOkc7hPOOWMHGDfSVMn0ir-N0euFW32HQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
رکوردشکنی جالب پاریسی‌ها در تاریخ توپ طلا؛ نامزدهای نهایی کسب‌توپ‌طلای فصل گذشته فوتبال اعلام شدند و در اتفاقی جالب، پاری سن‌ ژرمن، فاتح لیگ قهرمانان با ده نامزد رکوردار شد. تا کنون هییچ باشگاهی در یک سال ده نامزد دراین‌مراسم نداشته.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/persiana_Soccer/29377" target="_blank">📅 17:12 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29376">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pHg3cQjnbwa9t8qWQEXAAv5S6uuuChatlWO-1YpFMmV0gEVqDRkpHQsEBE9J484WDwF8sn959G0K_nFXx-GlsdWj1zF7VC5YHWe6xDjOF8UPiyYIxihjXHFYR8lUx42ZVbPTkbG0zZMXt3Rpia78Dl5yJHMMX3fVz5eqxuTx6GnM2RqIzJH1SRZv9bxzxF8ZBvMfPp_6ZnfhYuDfSSTbfsDRMkfPyLYupbL7dMb8KmJ6iuqYvdNpxPNv1ejRXu81hyF_VYkoUWITlMyw6-rhruCJiKl-RaAQX9ETbiVxNL5UbfhzPH8uwmXz70_HK02XJrwCATN_wYMwGQEeUSUNNg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
👤
فرصت‌های‌برگ‌ریزونی‌که‌بازیکنان رئال مادرید در بازی امشب و بازی مقابل بتیس از دست دادند تا اولین شکست کهکشانی‌ها در لالیگا رقم بخوره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/persiana_Soccer/29376" target="_blank">📅 17:01 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29375">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jH9G88Q6QFQx62by5HAlzbzZ6f-V7nnW2X83jrPV0IC9Gy5IkKg1iwT3Jgj_hUq2ehx46YaVLJLM_Axmff6QHwfWp8RP6KXls9XFuCfpVoyjVM-ODjpWFoOQKUCvSgPyQKrYVDx2q72JOUlRFKEm7Q-Iylvjqgad4dUa8NYgq9A-IaK3nAWmeGcbtt3B-NayAxrWaI_qSj3ueSeup3Ap0mcD2Esam5kO26k6Aj5ythENkfUQLspZnZmuo1SKgtXZ-yUaXQyaJvz6ofIvZJxriK-rX8eORZF7TkVRa4xK0DIwvV43kvK2QMg3c0Y1qvLXw1cBL2TigS1OxD4K1qqkPA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#تکمیلی؛همانطورکه‌پیش‌تر هم گفتیم؛ بانک شهر بزودی تغییرات‌مدیریتی‌درباشگاه پرسپولیس رو انجام خواهدداد. باگزینه‌های مدنظرخودبرای مدیریت باشگاه پرسپولیس درحال‌انجام‌مذاکرات‌هستند و بعد از به جمع بندی نهایی تغییرات رو انجام خواهند داد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/persiana_Soccer/29375" target="_blank">📅 16:36 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29374">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SotgEW-pUm-wf93PlyD5xb4Wn4RYDgkp8eqXNbTdu6A1_oKQVcc1iz9veb0KO4PywkmOawHKL57GEXjEmHCoW-tlG-BJjUiQ5GgLKo4zyLVV0czg8AI_UEAmD3crP3DFomydtAlwFBbClT-Zft8QFmfA8OHpL8tmNjeaLtN3NcSiEP8bo16GSnTnJ1KI5mppyKXeJA56BjN2it592HEzzrK0rQK5-4TgXD8BgCO-N8uefXkOovzTZ2FUyJdRrbhdzwDy8vfXEOXGXIMqbD2LEbjlkifCvjZPYn8xbVeEx0kOzXbCW_O0bFTeUleBQRe7rQmfrv74w2IFM4XS5MJ4og.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
#تکمیلی؛ برخلاف صحبت‌های امشب پیروز قربانی سرمربی تیم آلومینیوم؛ باشگاه استقلال مبلغ رضایت نامه محمد خلیفه و بهرام گودرزی دو بازیکن جوان‌آلومینیوم روبه‌حساب این باشگاه واریز کرده و بااین‌دوبازیکن قرارداد پنج ساله امضا کرده‌اند و نیم فصل به جمع آبی پوشان…</div>
<div class="tg-footer">👁️ 28.8K · <a href="https://t.me/persiana_Soccer/29374" target="_blank">📅 16:20 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29373">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/B1N-WbMqJloSquF5SiUO4flBZSpOgCN5jg6V18610qJRNc4nka_bIVm8lienD2RO6a6gWIiVN_nwRahHtyEBD6H3qR6sv28bqan5Z3rLpbSCxWzUANDlu2-FcanWl0ksFMTfxaMOB0XdRuCQwlDHxlCWYiR6OO2WXQ6bD-KSNcCbKFneGjmOXGC1KTI9dnf7ozsd_ZD0Yz8yE0Zb8OTwQFimvmDT9e5KD3Q-VphIekTvZO_wJkDU1bvQ0ZAI075I8MwN1Z7LUFg0-zpFKrryeXMVDATtjo7IYUenVuaX2WjfqANN3KljEoxOG7lcqzhPYGzXUnuK0EekoxhC3FVKjg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇹
خبرنگار معروف و محبوب شبکه DAZN ایتالیا که مسابقات جذاب سری‌آ پوشش میده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 30.3K · <a href="https://t.me/persiana_Soccer/29373" target="_blank">📅 15:57 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29372">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ALJQZybElMpwd5QFOEg_psp8e9MvnwAbyPTw2rWoAnvuAjwJPg_3Fc_UXuQ90O8PyjVdTsxJBD7dOQOV_Y0hQ7yjdfmG0fx3JTebdW02Oe2FLg6Qn6JWBdbQ--ksvHrg0r71ehcv-12ukD7Jz4jxYi_noivbE39M32XXx6hpr8xD0vKIko_Msb9G7gN4mn391YeAbzC1rwI5jnCxLlV9Vy8ZqMj_99_dTSgBhV-NpuVvQUBqbVRthlD7D_Y3tPicRocj3jsDSx2lRY1ZhFHrcyCKJDnRsZSoVhb8Vw9AG1L7hfJCInHL3V_ckkV0Tlgwy-sDDYLwy7nbR9Sx9m0-pg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
داورهای هفته هفتم لیگ برتر مشخص شدند؛
وحید کاطمی مسابقه استقلال
🆚
پیکان رو قضاوت خواهد کرد و بیژن‌حیدری‌ مسابقه روزیکشنبه دوتیم پرسپولیس
🆚
خیبر در خرم آباد سوت خواهد زد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 32K · <a href="https://t.me/persiana_Soccer/29372" target="_blank">📅 15:32 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29371">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/d8CmskSO4_CNZbZZJwQk-5NXT6Ll-baGFHkPkSB3R6FoL4rxLPcohvhfCZibb163VftDi3-jpgjnemaO8tNEp5W0MO_Z8fl2wbr3kweTY1wSABeMo3BTRsdEob4WT0NV4yUPhdh4lRldfOFK7ZmpHrVCaiH5zxxciNwwIfqDZqEpSaY6eqE6ium6dhiCgwY4L6nxSktuhGqPfoTXLCcQUjQyyT3OZYPrvm9F3hGK9142775TRi-vUe7FDz-TILKp9IahWA7I7K-S3zC_SrH8VBWTUtEkTvdMI6JhJCKV27_z0RmuwVS_0j5nXtuooZtxgrhdrLV_BtRZl6EBNKtBCA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇦🇷
خوزه‌فلیکس‌دیاز:فلورنتینو پرز رئیس باشگاه رئال مادرید بعداز فروش نیکو پاز به کومو با رقم 60 میلیون یورو به‌اوقول‌داده در تابستان‌سال‌بعداو رو به رئال مادرید برگردونه تا برای کهکشانی ها بازی کنه.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 32.9K · <a href="https://t.me/persiana_Soccer/29371" target="_blank">📅 15:25 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29370">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MijTpV-ZllLVmPN3u-o2Sr8LxkWzuCrTjfUEMbaEgXOMnV4kCs6YJthmewK8H95UL_NQJB9HXFM2mo8heow8o1Y_rWt6mMkaRQabw7cd_FFUqpLz9A0_58iXnBW6AuXjECmPrtcY_d5XI4kBWCRl9ywl-rYXuC1sndDvHb8fNiz3oKd6xapAZf3KgbE2Hk8Y2K922vFDZT_0iDL-gK1xJvd7h4RKaxHIVT1w8Yra_1TwV0g1bbEJSafYViHv9QHAb8YHwB1SmmNCchwR8S-g167OqitLmu2_tpyvTaYy5J01UPbXTzyO6rF-ZenKJ42EmYLiGX2AJ74947BHGgWgBg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
با حضور لیونل مسی آرژانتینی؛ لیست 30 نفره نامزدهای توپ طلا مشخص شد، مراسم اهدای توپ طلای 2026 روز 4 آبان درلندن برگزار خواهد شد.
⚪️
Persiana_Soccer</div>
<div class="tg-footer">👁️ 33.6K · <a href="https://t.me/persiana_Soccer/29370" target="_blank">📅 15:15 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29369">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SMyhKNpUvQvlV7kFdiN9wYhmx2NC0zQMP8dwKIYlT_2WxOngRvZMQVcScJ2gW7N-zfJ6vkd_tYFp0rEanrZ9vQjxWgqh1rdmgiRY35fP4-_Zg8VIdSD1a-SBu1Di1p--beGsmBnHOrRTj2X3o_y_tJCqu6YWa0KUvQgMKRwnRHqnNA8BAunmZX3vBq36OBiJ_Y1pelPLOSbh8_xNlQV1VGJRJJtCSmJR1D_lV4pI6PNr_gACeGZ11V3a19lWc21kwMXSOvxxZFT8RqlJDVldm5atEXmr9K7FHhM9_qFn_yqjyeOsqxxJQ_33t4L7_AYtLN1yJeFslBBB-RV1O3310A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
#تکمیلی؛صحبتهای‌پزشک.پرسپولیس درباره مصدومیت عجیب مهدی زارع درپایان تمرین امروز!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 35.4K · <a href="https://t.me/persiana_Soccer/29369" target="_blank">📅 14:59 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29368">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PpTHxnBnfOoqDJ1wHgg43uwSpbjUUYF2EBdfbqVuMh4hfkV5bsekDuu1Ec_r_1LN_9qrAvm2X50oX8bLwq8b9Go6GIzQ1PG05u0pYpVEq8AOCJpX0obx2tW-YEN8KFWaDA4qkUuX5_zLuP-OUgRLrpWgXzOMU6odsqxiBilc897jYM55qhKY_BwxTVatiMO2gPwK8CVoBcZhTyTGI5n7bmDw5f3nPI006vtcFmS2WwZ9Nuxod-yjS4PyrAjbAsjVVeCRpEvYHqSrgf9M_TltB-yyE4j5mIczER2XxCHn7AwX-bOuCMSn5zOVwVnnzO1s9nHAVY4l9bKCsxuLPNfXmA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇦🇷
لیونل مسی آرژانتینی ساعاتی قبل با خرید 100% سهام‌باشگاه‌الدنسه‌مالک این باشگاه اسپانیایی تو دسته‌دوم لالیگا شد. چقد لوگوشون‌شبیه بارسائه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 36.4K · <a href="https://t.me/persiana_Soccer/29368" target="_blank">📅 14:44 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29367">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hBLWHRP1dxenIIdX4L9fQVpI9ch25KdTXa5M4ZkXK25TMP1tT1NBm1egZB2rVxkq_M2JBjYOyNJ8a6rvlT96nzVM3Gjj37hmHS2W8OO74rij1DwDk5fEceqMFoHO4swLLV0YNmP-grJ_De3QduTicPVjZ1FjFaRJtpKxW_Q01FXNdEoeuh7l500aW5Ql8OtB6kMgdzrzgHPDAah1luuZzdPIfuvjU7BWnf4Pcls9_vBclqmrdkqn_6fj7ClHPASe0GWhbAqbT4xilvf10DaU8hU6N911iJQM_2nth-jdcsEhbm1rTsVcYVEWYYvWg1LxvrZncz4ZqzVHHFxSPH8D8A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
ویس فحاشی برگ ریزون و باور نکردنی خداداد عزیزی به امید عالیشاه در پایان دیدار امشب؛ میگه منتظرم بیاد بیرون کارش دارم!
⚪️
@Persiana_Soccer – ویس فحاشی خداداد</div>
<div class="tg-footer">👁️ 39.5K · <a href="https://t.me/persiana_Soccer/29367" target="_blank">📅 14:13 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29366">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/l0TnUsdWqDsnhUtRa60Vo1mqedV06iZ3JSue6lX1O0wkUmqapoB2HvtwNn7WcHIuG5UHJmDzbQiAiYWnFgsn4QdDwCM3Et4OERulCZmPJY1N-ckosEEWioSsjb9C6EQhJf_fHwTVh-Z7kRdr49AE_HLjUCsJ7ijc_Ij_Ici2i9jP5jMPIBpRi497GMeNrHxdvmGa-oDEeWuNNiFIftVG85Kk8fxqvot3j83rawMP4DCWdPpBSCUZK6_EN2aMYVuhtXb-b73nTXysNgEGdlH4n7rgUMZWDlky3eJPTLFEeS3otKBj2mniixPjbnvSMZCUg25Bl-AMUdBvIYX53aFuBg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
جام‌‌ملت‌‌های‌والیبال‌آسیا؛
تیم ملی والیبال ایران درسومین‌مسابقه خود درقهرمانی مردان آسیا 2026 بانتیجه‌سه‌بریک موفق به شکست چین شد. شاگردان پیاتزا بااین‌ پیروزی درجدول کلی‌مسابقات در جایگاه دوم قرار گرفتند و در مرحله یک چهارم نهایی رقابت ها به مصاف تیم ملی چین تایپه خواهند رفت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.2K · <a href="https://t.me/persiana_Soccer/29366" target="_blank">📅 13:44 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29365">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/765da8fbb9.mp4?token=Fvjxa76m1RhC2paxc6CVA9Ms4i5TgdOMmXhE8vEHJuuaxN9P4BEGUufvfEP9WFLSd4hZPKntq-u55thHIjiuok5IaI7tYhlREhAXMZ3BHKh6Hd-AjfMYR_Anz5qvuNFY071GsI1HzJbDqpwHGzM0Gp__RY39nJcyB4yekkERVg1CuMtiEYVPVUjZ-TUdVXDvedQU9KP9XmcHgAgswZT_n7DPm9okTa9sCUFhBAQg8nIxMtWjD8bIsmxuoMiri_vZp5QLxk2bgTgQ_QBWximlvZv9-P4wSzTxMipr90JhWz5I4nb3Vmlx12ik7u_ToPMDnwlSgSq23TlCPRa0Hv_yFwI7YgImeSv_I9mXez78C03c9PYjnrnkaaytYC8h-Lk9-QYEn_wuTr3Emg7BjL8AdbXgPfQoPB0t6XX-BGiO5-5ISAv1ILVkyEZRjUt_n_xvPYuBcBSn9ImcLNZvWlMSpgh0zmz2n8Se6FjHU0_hCUHo4ixaUsps-0eLJ6OFvo7DbvxN2rvO52fnPly1Z8Smbs7KkRUnO5RmNZ5x_QrUPUnyCXg2WliZPAQmhmlQL6fOj8fx2K8ZXHpwkQ3fRxHeDFLcUoV5UrMFpOZ2HeMffnYvv77-Fl-EfQ58DwVOi11fKz_BIcG8YgvxQNOvjFy8SyYA1TheLAFwbSAu_tnMo9I" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/765da8fbb9.mp4?token=Fvjxa76m1RhC2paxc6CVA9Ms4i5TgdOMmXhE8vEHJuuaxN9P4BEGUufvfEP9WFLSd4hZPKntq-u55thHIjiuok5IaI7tYhlREhAXMZ3BHKh6Hd-AjfMYR_Anz5qvuNFY071GsI1HzJbDqpwHGzM0Gp__RY39nJcyB4yekkERVg1CuMtiEYVPVUjZ-TUdVXDvedQU9KP9XmcHgAgswZT_n7DPm9okTa9sCUFhBAQg8nIxMtWjD8bIsmxuoMiri_vZp5QLxk2bgTgQ_QBWximlvZv9-P4wSzTxMipr90JhWz5I4nb3Vmlx12ik7u_ToPMDnwlSgSq23TlCPRa0Hv_yFwI7YgImeSv_I9mXez78C03c9PYjnrnkaaytYC8h-Lk9-QYEn_wuTr3Emg7BjL8AdbXgPfQoPB0t6XX-BGiO5-5ISAv1ILVkyEZRjUt_n_xvPYuBcBSn9ImcLNZvWlMSpgh0zmz2n8Se6FjHU0_hCUHo4ixaUsps-0eLJ6OFvo7DbvxN2rvO52fnPly1Z8Smbs7KkRUnO5RmNZ5x_QrUPUnyCXg2WliZPAQmhmlQL6fOj8fx2K8ZXHpwkQ3fRxHeDFLcUoV5UrMFpOZ2HeMffnYvv77-Fl-EfQ58DwVOi11fKz_BIcG8YgvxQNOvjFy8SyYA1TheLAFwbSAu_tnMo9I" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
آنالیز جذاب و دیدنی دیدار هفته اخیر آرسنال و چلسی؛ میکل آرتتا به‌این شکل تونست ژابی رو ببره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.8K · <a href="https://t.me/persiana_Soccer/29365" target="_blank">📅 13:35 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29364">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ea3eaf66e2.mp4?token=QMs5pO3rS1XCaU1aQKaSwkZ_Ib0op1XlUeJ2yohQkkL-3L_OkW12mFMeAT1AS7wQvmMDYEIxCsB4ciCUv-fE5OoOHBvLZdcY0UXjCwZHjHE0-lkaUQM93wza0wdBHQnE3kD9Xu4RlvtPsTqox4e3Uh80BeZILfswA4ewoMdk_50Qiq3e5kTuKMng6FUTmrXve3vpYoHp6EKXG608ZXsqrqemMsoUieH084ulD1DfkLIrajJZhqg2A-NeWXcNGQkI49LpWvroqLP_5jgi6yrBbPqiJYtFhsg2NBG3ar_RSEWWX-L7XKUs3LFfJoq6f7m8OaPVQHDmfvbzh1SiIqt7Ug" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ea3eaf66e2.mp4?token=QMs5pO3rS1XCaU1aQKaSwkZ_Ib0op1XlUeJ2yohQkkL-3L_OkW12mFMeAT1AS7wQvmMDYEIxCsB4ciCUv-fE5OoOHBvLZdcY0UXjCwZHjHE0-lkaUQM93wza0wdBHQnE3kD9Xu4RlvtPsTqox4e3Uh80BeZILfswA4ewoMdk_50Qiq3e5kTuKMng6FUTmrXve3vpYoHp6EKXG608ZXsqrqemMsoUieH084ulD1DfkLIrajJZhqg2A-NeWXcNGQkI49LpWvroqLP_5jgi6yrBbPqiJYtFhsg2NBG3ar_RSEWWX-L7XKUs3LFfJoq6f7m8OaPVQHDmfvbzh1SiIqt7Ug" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔵
🔴
فاصله‌امتیازات دوتیم استقلال و پرسپولیس در تمام ادوار لیگ‌برتر به‌کمترین حالت خود در تاریخ 25 ساله برگزاری این مسابقات رسیده است؛ تا پایان هفته‌ششم لیگ بیست‌‌ششم استقلال تنهابایک امتیاز پیشه. نکته مهم این که در محاسبه امتیازات، کسر امتیازهای انضباطی اعمال نشده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.3K · <a href="https://t.me/persiana_Soccer/29364" target="_blank">📅 13:35 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29363">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromBetegram</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/U1hBmY0jk2Pjge70LqQEW7METLk-9SBZ6zdQDEpFBlXrc3vPrOMsCoZu6JBGphqd7uTr361Lx4nOr8BbgeVYoaVD4BKppeYjJrANNNGMsM1hqlkVWMKbyI5PCpak70pZnQYQyyQBFpgdw1I46tNrVXgxPzmtfUw69YuzZ1f6fUB24ku6R5b2d_kymZ_SEbBPEBO4tK7ODS1kOaiVWUuXX_Aj7MbD4pQVrdP_JVCdytHPI1cJs3NAvYf4we79fV8kBwGDARFogXDUeY-_RzTTKdVuUlR5Ro43QHC0PvQ1tYnDoTmQOxpkdDWCN7BNf2DG-aQVEvvZfY0p9n7lGTNr2Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇺
هفته اول لیگ قهرمانان اروپا
🇪🇸
بارسلونا
🆚
فاینورد
🇳🇱
⏰
ساعت ۲۰:۱۵
🔴
بیش از ۵۰۰ نوع آپشن پیش‌بینی برای این بازی در‌‌ بتگرام
🔼
با بالاترین ضرایب پیش بینی
💵
واریز و برداشت ارزی و ریالی
❗️
🔥
۳۰۰٪ بونوس رایگان بر روی اولین واریز
❗️
💸
۱۰٪ بونوس روزانه واریز رمز ارز
❗️
🎁
فرصت را از دست ندهید! همین حالا پیش‌بینی خود را ثبت کنید و از بونوس‌های ویژهٔ Betegram بهره‌مند شوید.
🔵
http://betegram.com/affiliates?btag=3_l7</div>
<div class="tg-footer">👁️ 34.9K · <a href="https://t.me/persiana_Soccer/29363" target="_blank">📅 13:35 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29362">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1617cce66f.mp4?token=r0TZlDKuTJkTz6-9tqifLQT7fVHXpP4ODJfVVL2cq4oZC__kWuqYV2g2rditdd2O6KumtHZC0QYkTd2WQxWsduckm4sPqKq4vQzf7EMZtxtmn-Nat-w_joHiDvy40ouHIxuFdkH2Y2FxKd3ZRcEf6l9MSijUOKoHV5ip-1DOXawoC4xZ5Tq4hiFSS-xbUPAxaab2InJByk8rrib0FECgxN2noTx7-3HmiDupLRvm8E6NE46Ng0Mx2yR96Vor7ciFkS6w7bRSnby6EzNL7Ay1blhn0PkzN4uTufgzL3FrPWTXQ-Xc76DSbwDHGsX4Wz45JySIGp1FjcDmktm0GIkqsUdzGgrQnpi1mQ976WGgVaiMWrXaV2JvnZDZuiYdNASAFWnEg09RLPZveVnolFJdsL2vyiLOUhbeQ6g8lQR07FZlF8Z8UOjM6PelNU8NbtPTgQ3y6uzx4G079uKKfb30z4YqKr1rfEUhMe_MmrOQDTN774_opohZxWthI7xJEUtHGCsPNGBziONylmwVRa4ios-aJfN_pEZ8PbL6hhPtNYusV-aqtmgjlVrdOVzdVKDYUhZq_q9vEcxJ43XOrAyEw_vX7FxksnE5nae207IB8N754D-jhklUqpCgWx_8W_zZg7UO8bbqOrDiGN6Ub_KpNfshfpOb_-zCl8UvPcfdeqs" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1617cce66f.mp4?token=r0TZlDKuTJkTz6-9tqifLQT7fVHXpP4ODJfVVL2cq4oZC__kWuqYV2g2rditdd2O6KumtHZC0QYkTd2WQxWsduckm4sPqKq4vQzf7EMZtxtmn-Nat-w_joHiDvy40ouHIxuFdkH2Y2FxKd3ZRcEf6l9MSijUOKoHV5ip-1DOXawoC4xZ5Tq4hiFSS-xbUPAxaab2InJByk8rrib0FECgxN2noTx7-3HmiDupLRvm8E6NE46Ng0Mx2yR96Vor7ciFkS6w7bRSnby6EzNL7Ay1blhn0PkzN4uTufgzL3FrPWTXQ-Xc76DSbwDHGsX4Wz45JySIGp1FjcDmktm0GIkqsUdzGgrQnpi1mQ976WGgVaiMWrXaV2JvnZDZuiYdNASAFWnEg09RLPZveVnolFJdsL2vyiLOUhbeQ6g8lQR07FZlF8Z8UOjM6PelNU8NbtPTgQ3y6uzx4G079uKKfb30z4YqKr1rfEUhMe_MmrOQDTN774_opohZxWthI7xJEUtHGCsPNGBziONylmwVRa4ios-aJfN_pEZ8PbL6hhPtNYusV-aqtmgjlVrdOVzdVKDYUhZq_q9vEcxJ43XOrAyEw_vX7FxksnE5nae207IB8N754D-jhklUqpCgWx_8W_zZg7UO8bbqOrDiGN6Ub_KpNfshfpOb_-zCl8UvPcfdeqs" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
عملکرد 9 فوق ستاره‌ درفصل‌گذشته رقابت‌ها که در لیست 30 نفره کاندیدای توپ طلا قرار گرفته‌اند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.4K · <a href="https://t.me/persiana_Soccer/29362" target="_blank">📅 13:10 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29361">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/732028b756.mp4?token=PDNrRf11q2ZBXaWZYfy-8XRGW5pbphpymsHMIk1Pw1yoRaD87E2ACy7S0spePj1dHAr3wNKNnRlrEsVqYXwe0ufUoTb6sfplgV2tvfHqkt0YwexPkyeW7r4mCMLfpyor64lKGfWBvuDp8IjLB6jg2smg1ufh095A5m6qlHiMftldMM9un-5uJCG434kNvcur9qVzgwlucZ0jKd36pvxlKYDV871KqiRu4HyNzq5Jun8TtSFBKFMw1HFrvfrc1F4Qcr7cMDSYnGXHgQMHVfxO-DaaLdYoVqR67JRpHyegZwKZTgkXMJoNMd9veMtuWd7V2xt1o9hVk15H-MxHyAarog" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/732028b756.mp4?token=PDNrRf11q2ZBXaWZYfy-8XRGW5pbphpymsHMIk1Pw1yoRaD87E2ACy7S0spePj1dHAr3wNKNnRlrEsVqYXwe0ufUoTb6sfplgV2tvfHqkt0YwexPkyeW7r4mCMLfpyor64lKGfWBvuDp8IjLB6jg2smg1ufh095A5m6qlHiMftldMM9un-5uJCG434kNvcur9qVzgwlucZ0jKd36pvxlKYDV871KqiRu4HyNzq5Jun8TtSFBKFMw1HFrvfrc1F4Qcr7cMDSYnGXHgQMHVfxO-DaaLdYoVqR67JRpHyegZwKZTgkXMJoNMd9veMtuWd7V2xt1o9hVk15H-MxHyAarog" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📊
از پس‌فردا دیدارهای هفته هفتم لیگ‌برتر شروع میشه. تراکتور دراهواز به مصاف استقلال خوزستان خواهد رفت و آبی‌های پایتخت با پیکان بازی دارند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.9K · <a href="https://t.me/persiana_Soccer/29361" target="_blank">📅 12:45 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29360">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TbJB32RuWFjkBqfaAillMrChO2QFEuPpxZ6cLliFASON2WaH_4FM7kIsxUFm6TaR215fdrJ7lveytKkKd9fsIMwSLB-xj8bJ8koBsr4eVTSlRY70xRSjdB3q09uLh35t-N-vTJ5np6iORlaxq2F50OdDrc4bk3kfqe_9c7AcB1c4gQMKJO_IoiXAF89-uXdMJUJTMDhvhwNs_gV_a3wBt48145sepmDbKCrlQw59SykvlZDTH8jF6tmC6H4lpbmrOmZ_bWn_mSAzmjp_UNsKpzmfiPEdnA9WVYi4ZDmE7vsyCPGb0urPCTamHJZCXa4BSiui_E-cBL-RVe1MOb_y-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇧🇷
برسی عملکرد خیره کننده رافینیا دیاز ستاره برزیلی بارسا درفصل‌گذشته‌رقابت‌ها که یکی از بزرگ ترین غایبان لیست نهایی 30 نفره کاندید های جایزه توپ طلا در سال 2026 به شمار می‌آید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.7K · <a href="https://t.me/persiana_Soccer/29360" target="_blank">📅 12:26 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29359">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nVU117DTbP8f3puMKuaLHssGOkNXvGaEoni964X1RqGPgxjD3b__KxacX8ur3IQUrNAePqed3STnMXIODlNK-pfWSgAsqCDEztEg1KojNXji33jb4wHu4uXeuhfQK-UnM7e4g--TrDIawmoMmIjvGyheVAiMcdfpOxMzTHHVU-AnKKtdPUYexbzsEPXGCA-wI-kGsDMby4TPpGX1IrRNBiayls9u7xLUNX-lJnAyiZu7m5wih24O1noamt2hWDPYns_UdrEsfr7mx3UW5E5bM6Gu0YYVnKT5XjfyaKn1vbycQxMAByKirTHc0zgcfL9clzNhVgTWOQpVuMI9F9_wZw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
با حضور لیونل مسی آرژانتینی؛ لیست 30 نفره نامزدهای توپ طلا مشخص شد، مراسم اهدای توپ طلای 2026 روز 4 آبان درلندن برگزار خواهد شد.
⚪️
Persiana_Soccer</div>
<div class="tg-footer">👁️ 42K · <a href="https://t.me/persiana_Soccer/29359" target="_blank">📅 12:14 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29358">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jXcAmMisysnLgSDmzRndW0if9iG65AhZ7nEwSrQSO-LsUaDu5ojI1MpT6-u09B-_n49NCo9CU9P27-2D8qEC-jbWR2MHMzGISK0w8JKLbFrgpHG69gMfxbxxoZE60x2KIFuMiBRi_e5sv5W2N0PO_SyRj0G5MRN8CNBBebFO5Q0tIskDCQ6rve0KggmEF6VvAgzL0znr0UhBoelQVsa19s5OqTjO6IRlOIZdDhDmUlwv85G24hTeUCBPEUMKItxNxJcU5evIw0A5AMNB1SPviPNjXd09s81Hr9MRSfqZSbHG9hibYeJtRhzDmsj_G2uQicT2-7wryW138qu_Q_j0Ww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
دو سوپر گل دیدنی شهاب زاهدی در بازی امروز جوهر دارالتعظیم در حذفی؛ ضربه سرش رو ببینید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.7K · <a href="https://t.me/persiana_Soccer/29358" target="_blank">📅 11:40 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29357">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Nwb8Zu4cv4bfnl-vGjRQdk5Wlp_iH91r6t1v3ea-cLUemXQgWSTNXumJqIBrstAmTeb2KdR3joplBNll4mC95kqmsUosuGg20Wp0XWU8sn-BOz-a9N3NLrjNVYRndRpSx27INmZaoO0Sp4EsNAy1yQv0qXeSUwcU_2BDAjseRoP6vM6DFRQ_aVTbFzibOkNhGnQOBZ7-z1us9_w7aSgqEXpTk99sV3bAfbXyvE-O_M9VzQtmCqZlYs69xrIF9i_6ebPd7-XPwbc1wQ6OFIIAaLEY0RIr-datd27eR-1F13aLXZGolr8datmgpVtbw97A40f4wV-hpDVf7tqPBiR57w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇫🇷
رکورد خاص‌امباپه باگلزنی به اینتر؛ کیلیان امباپه در اولین بازی چمپیونزلیگ در دقایق ابتدایی به اینتر گل زد تا با رسیدن به آمار رائول افسانه‌ای، پنجمین گلزن برتر تاریخ لیگ قهرمانان اروپا شود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.6K · <a href="https://t.me/persiana_Soccer/29357" target="_blank">📅 11:22 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29356">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vKO9mOEOyOpco4o7022whIKhJawkCxIC3TfvlzvUVu4kiYfvogZenF-KosAAlo--y4NHhGKEZo5MGkNujN2wLk1QnS2mhe914QWv5EibQCHMAxA0D6V2MRC-YC594oB6G9o_sWt0zSmPKTzg4pRmKupFtP4Wp5QmisVcFudgjKZgcNvyzUB5zLf-0E8CewmwBj9NzVlxoomIzR4oaBXSHjyN3rdpsrtoWXe40-YSB8-IktREH24LUVMk0ow8fcuzZI_UijnAflN7EUUHWgFT05jf-UqBxOCpx-7zFLdMTtJe-FmrvBLhjywKI7R57KCEs4iWgZkDVtz7f2-X4sYV-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇹
🇨🇴
با اعلام‌ رومانو؛
خامس‌ رودریگز فوق ستاره 34 ساله تیم ملی کلمبیا در آستانه عقد قرار دادی یک ساله به ارزش 650 هزار دلار با باشگاه آولینو در لیگ یک ایتالیا قرارگرفته است. شرایط‌جنگی کشور باعث شد که خامس از حضور در لیگ ایران پیشمون شود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.1K · <a href="https://t.me/persiana_Soccer/29356" target="_blank">📅 11:05 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29355">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jokmiuiDdNFdE4qcMuqL67dm0duNbQ5aXkbbl-iYcJyxRBMfbZdJIAPFvtdrKBHSc9CWriCvDa4V3hOizhpCfl6xXzcnhIgt1WZoEluvF5u56ZoytMQUSJt7WthpuAGJXiPU2PXM-G72uUQzHBhw2ufYNzRHJjQED446L8VIEjf5s_JQzcSd3Haq_F9smezTr4Gp65snz4QuOJjfMGGFdTD2XKBimw6YY55ahSSgRFOCWLjmfz8meB8OcuKUp_SYO1o1gvmP2NBfMa7JFjlOys3bnRRzESlnpNU-Zxsu3UAcLQ1DRFtxMzjmHlDHPEwHrex1EsWhOKwZkn4eN3Xw3g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
پوریا شهرآبادی مهاجم ۲۰ ساله پرسپولیس با دو گلی که این فصل به ثمر رساند به دومین گلزن جوان تاریخ این باشگاه با حداقل دو گل تبدیل شد. مهرداد اولادی با ۱۹ سال و ۶ ماه و یک روز، تنها بازیکنیه که پیش از ۲۰ سالگی به ۲ گل برای پرسپولیس رسیده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.1K · <a href="https://t.me/persiana_Soccer/29355" target="_blank">📅 10:44 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29354">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0b6f5a93d8.mp4?token=OOwYtWjrGT6_9lnFmrB4kLOzO6IdJbvp-ainwDKd99fTEDKbebYcr_o-wRVjHUXP7IGsG1hAdmbPkG9uU1xEsk8YOZkyHpw_K-aijykEVbN8QqFIcIGvGuk28Mwf6KqHNhMsnowaxXgotaC4UfpKFPNwsfFCp1y4BbiGIw-jwQ7nrJBqw0Ot0fc2s1NJRmzntCymsTJvJT7Wtn6W-TWrCTvJ5_a9--M0gHklDquoBPEp7gMamy0mruWmptnRaepYfV2SXd0NLSABAfKMBk74sXtituGEYYw8oOHNcJeKx-IqqqS7hXdpbp-vCGTgiaY-ndkjjSnN8qdueeZcs2v9Ug" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0b6f5a93d8.mp4?token=OOwYtWjrGT6_9lnFmrB4kLOzO6IdJbvp-ainwDKd99fTEDKbebYcr_o-wRVjHUXP7IGsG1hAdmbPkG9uU1xEsk8YOZkyHpw_K-aijykEVbN8QqFIcIGvGuk28Mwf6KqHNhMsnowaxXgotaC4UfpKFPNwsfFCp1y4BbiGIw-jwQ7nrJBqw0Ot0fc2s1NJRmzntCymsTJvJT7Wtn6W-TWrCTvJ5_a9--M0gHklDquoBPEp7gMamy0mruWmptnRaepYfV2SXd0NLSABAfKMBk74sXtituGEYYw8oOHNcJeKx-IqqqS7hXdpbp-vCGTgiaY-ndkjjSnN8qdueeZcs2v9Ug" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
حمایت تمام قد خوزه مورینیو از فده والورده؛
جایزه‌بهترین‌بازیکن زمین باید به‌کورتوا میرسید فک کنم اهداکننده‌جایزه گل والورده رو دید و بقیه بازی رو خوابید با این حال فده هم خوب بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.1K · <a href="https://t.me/persiana_Soccer/29354" target="_blank">📅 10:31 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29353">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/H5zA04yFAgVi3zeAZ4YpXIJyS4XEPrKEuDPLnbprrbqbka-jjt8MnSjOCU8FvBuGIJrSXnUY2KmDUdRc72AjXS-Bj7ptMuFJEZzO4eP57mIm0_-rGznMMZXQzLb7ynmn73RCyP4KmGVNIiuYf-CjZT5GKnj8fIawam1_Uh5PMwua5vao3ZsU68Dqnp8-WoaeY5XXrIoQ5HC7Z5Fbo9XrDqq-CehKxmnOffH9fc5P_Og3XWeyBJyYr9mz6SG0_puriRI9e5O4TBF9WuAHKwNNQEmtDAG-aX4o5wLLfzAyXJ1Jn0RzZR2FUtWNvIw6Ye8wQB2ZriRJfyZ0_2aqCruQvQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛بعداز درخشش ادامه‌دار نادر محمدی در لیگ‌یک‌روسیه و لینک‌کردن او به آرسنال توسط رسانه 433؛ این‌بار نشریه سان گفته میکل آرتتا اگه قهرمانی UCL رو میخواد باید نادر محمدی رو در ژانویه جذب کنه! قطعا درهر بازی 3 4 پاس گل ثبت خواهد کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.4K · <a href="https://t.me/persiana_Soccer/29353" target="_blank">📅 09:49 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29352">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Kib3UUM0B5J7VQ8-RX0UCxtX_4AfQN9NoPcoziLwsbBlTQe8A_wDNCM-byy3YAHzDnfzey3QSZIxKkXlAGJd-0ucBSwxFEDnhuiXZdHvJ59OV225AZVrRJ5COxfuM0G6BRP2gvnZrgOGwTukCkUT9ujjyFGdAq61Han78oxYcvXXwh0uv0JGP83smKyhGsbapr-AlBDFFnfJi9YcOdaxQhHOq4qhqXsJ_Yd6ckwC5sHu_RxAZccR6KhE5DnLb2Ye2OglqEvfvOfe7diRLiIccrfcSQDF9d6eW3OxQEhaxqTSm6eGFP1jRm5cjN33nSL3fmP7Ok_lQVbaulSXXDV-nw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
👤
فرصت‌های‌برگ‌ریزونی‌که‌بازیکنان رئال مادرید در بازی امشب و بازی مقابل بتیس از دست دادند تا اولین شکست کهکشانی‌ها در لالیگا رقم بخوره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.9K · <a href="https://t.me/persiana_Soccer/29352" target="_blank">📅 09:44 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29351">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/h783phW4ZZZ5QLbAew2wB1vjinSN0tOGDOAEsJzBWuQ0G-n9jPBOiaWijrs5W9LkVfy8e1MALW_4AovuJpc_wYz6MhMD7SzW8VyUkv17pWAkzg3uUVYUgaCv_itrRaCIzQ2YWCahaFBF87b1NT5FRnviY7r6yX_F3HW22ViOIrEt23Ph7rd4ZFlsGtEfQhNBtRwueHyzn4PtrggpZUuuaCzgi6lI9E_A3Q9cqSZafGh5QkBiBndwU-_ArqZHwy6f919TLetRSKA61vKzeZaQJWM0qdzOII-gshxPWntckzEbyqXPJ9yyzKxxPnAbYLpsbVuFqxWC8RTsv8F8LJK0Aw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
تاکتیک‌ این‌روزهای کادر فنی اسپارتاک کوستروما درلیگ‌یک روسیه: نادر اوت پرتاب میکنه یکیتون بزنه توگل؛ نادر محمدی چهارمین پاس‌گل خود را با پرتاب اوت به ثبت رساند. چقدرم خوب میزنن تو گل!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.3K · <a href="https://t.me/persiana_Soccer/29351" target="_blank">📅 02:03 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29349">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BJCim-h1z4QmxU9PRNgLXeMBlKuHLYhdvl_uvtBjTXP7YejcyFzdyfdVRQKHcXban33TtZrYVj5OV8IlnjcMYw0VNKNYlpR3LYvVYlqrYr-2hyVMMUSbqlfaV_gHoZvMMkDXNrQST4Kptj1IPllZuam3Jo3ag_Qx1-oRITbAgfYSn3PsAnXJx105EvB8B2vgdCnQ4__KcoqpDfqUyJt0C9ziuGfndq5VpmazgKK4EYgl_0-Gg2gkiXyrurk9AyVz0td2p4c231cWNCHek9Kl5mcV4xIHTRPAkjPWPeMs-Y5IJ_UU3uesdZA7bsqdPwV1Y4z57kLpFwySr0j6-9iPmw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌‌‌‌ دیدارها‌ی‌‌‌‌ امروز
؛ ازجدال شاگردان فلیک با فاینورد تا تقابل لیورپول و اتلتیکو در چمپیونزلیگ!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.9K · <a href="https://t.me/persiana_Soccer/29349" target="_blank">📅 01:20 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29348">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BKRLGigxJBiqSpdcnoLemXVE7vgcltk3HKRG2XHbzU88-tStzJo8F5Kd2Hrb8Tr4KC1hwNF1k5Kb-Muf_dEaXN4dR7ljyfR3nLe3xXwUtW9lWjwyLOxL-OxTo6UOP8oxXKEce3IDUOflndRTAEMNmUT0xHQ0htw8zAMDUJFkRZokEu5ZfgHY4WE0rDCnHX_wNKIDgxaQvreP0rcZutH1y1QSwA6RrK89QuGq-50pfcrknyMqO0B8_9M5k5yrLLGOTmaLFFzLMmCS9dzMHKBU-P8Wu-lVH5kQLSMZVpZBSFF0fa7ElAmCNIJjvCkkZjHlSe_JVMOmd-X1cm2LilUdyQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج‌‌‌‌‌دیدارهای‌‌‌‌دیروز؛
شروع سه امتیازی رئالی‌ها در UCL و برد آبی‌های منچستر در شب دبل هالند
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.9K · <a href="https://t.me/persiana_Soccer/29348" target="_blank">📅 01:19 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29347">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QN611fX3BYSLP9gwCdGo3BOiX7NS3Mv6EyxiuhfJlUAoc-jqa-RRL24sCjr07WZwJ2PU-2TQO4da_Q1UyKJXThgdXZhP5ywkKaAYWHmReRWNz9Tano22f-cDHSF_Tdgm7z7gj9YdRK78mHt8Y0cToDPdp29PsKq4L-MD7x8SPDpkK7Bh-4s6Mu8hLQ32Gqv5zusYHz7W3jskIjz6DFHX3U22Z7vZekv6FNhDMVvzPmhxI1OK9eBcVZtUnuiObBADt7FmOdGVP_R13239CgQ2jWUFZEeHvwz_5oFzP1uLMNCU-Qipdofww5VvaxR5W_Pe88WsIjzmXpvRt_utdBFCyQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇺
در هفته اول لیگ قهرمانان اروپا؛ رئال مادرید با درخشش کیلیان امباپه دو بر یک از سد اینترمیلان گذشت. جالبه بدونید مجری شبکه اینتر که در تصویر میبینید گفته بود امشب‌چهاربرصفر رئال رو میبریم!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.4K · <a href="https://t.me/persiana_Soccer/29347" target="_blank">📅 01:04 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29345">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/iDG-gClj7cNBsCbHbyvVAMApWB1qVKKUuifNYbRuLTWaX7K4p-k83utXg-8pLEeVZJULCkhTl26bCjAlFRooMQ4FDkgjz1HPRXv_YIo_F-1HH_ziRUK378epC7-wH6S5LjC0QB4D2gDZbJkkCX6MqqsFhYFFlgLPfB_dTWRNNQiAc9wfxQO3uq2z9qn4YIQvoYRcIiUaWUMSHqJJx4g2Qu4zJ6zqGgXpjA-WULvmRwSqnltENBUoyfN7FQf1bSJlngNMquADHo2I6bQepmPEt3eG5eD2Ln5hU8CCEh_sTzyyBFxrJWE8CUwXqVo2LImXeRryHOVre6tQ3JPEfMSYgw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Y6ILYtxTDyveZ_ivrJEo4hJC5M-NSsrR9Qgea3D5BFPwXviFl7pBoSSMUyUZRJWO5PuAtyliAJ6YV7BMplDxCFMdaI_Bf1acf0sG-98pdeRHYojXbUDrQ1pgMx9Oqt_yV0Mt0sV_KJCHDYQoAkK4vLPkI2fjtm0mI0KYLnWopNscLq9tCBA7nKMlgvopKE1ryh_MBGFj1-yZMeHzHYc9c9NX3LtiYkCyYee9-C_ko8sp39ox1IEbS0ux53ja4XIvV8jFSZdVtTKXG1fM4Dj9a2xrHZiowZ-oBL1pOVywm47Upnpe2umVx6Ih4n8Ij6a3fKYblXdJ0yqgfCpR0SSsnA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🔵
🏴󠁧󠁢󠁥󠁮󠁧󠁿
جک‌‌گریلیش‌ ستاره‌ سابق منچسترسیتی و فعلی اورتون در کنار پارتنرش؛ اون اوایلی که تازه اومده بود سیتی بیس چاری مست میکرد فوتبالش رو به چوخ داد الان باز بهتر شده!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.3K · <a href="https://t.me/persiana_Soccer/29345" target="_blank">📅 01:00 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29344">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/odYA-oqOu3VSZ98wVP31XHnxfQK3YWYG5XJ2LQwDY4yO-vfSQDjiGmzH6Ie3zsMJ7kvxXyNWnI-b_k2lzNItq4z8dLSr-EMx3qDniWbNb2ng6PDD8qKE4vwXYP-ogVRiaCPBPEjdegz7a5z2qouL8E50K7Q43A9H_iEWB7IxWP-05j8p1mowvY5BnhF22Yi8xBg11XSqyvZQrqnw2IADE-MJVsLsFbZxatFarx7ify0j5H6gDPFhr_KpHgezmh971NcRacdz8iAlIvV52-2UUCOzikjDK3O-UlScApTMX-AK3qwr1zZNmMogCTvhYEOHU1u4GlFXzVPQsNnOQONpnQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇺
در هفته اول لیگ قهرمانان اروپا؛ رئال مادرید با درخشش کیلیان امباپه دو بر یک از سد اینترمیلان گذشت. جالبه بدونید مجری شبکه اینتر که در تصویر میبینید گفته بود امشب‌چهاربرصفر رئال رو میبریم!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.5K · <a href="https://t.me/persiana_Soccer/29344" target="_blank">📅 00:37 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29343">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kJJOudlv0NdhEPI4cq0qvq06CGwS47jpwU5jGo1MHL2MWtJsifgfuQV1RFNFjqRGUDjEHbIab6HNhY8bwzo5B9V_louMVvDQW8jt4Ym4XBiW2DOZEgjOoG2ypfORlBTD1OqqWtp6DrtpDE72fARnU-MlT1HUhu259anpxft181TxRGxsnGIQDnN-Elw4u7fE0slH9sL9bk5TmAIEKywrNHlKNSwQS0kWezeLcF1Kk0hBX_9xqgepICLYn63KlAn-xDLLsIm2mcP6ANIyaNn8V-u_pw0N__yO7C37he1dAX8Xs596Y7BrcvKqgFuaW7HJX1CzJpbkSznZ30cyLVO4qg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇫🇷
رکورد خاص‌امباپه باگلزنی به اینتر؛ کیلیان امباپه در اولین بازی چمپیونزلیگ در دقایق ابتدایی به اینتر گل زد تا با رسیدن به آمار رائول افسانه‌ای، پنجمین گلزن برتر تاریخ لیگ قهرمانان اروپا شود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.2K · <a href="https://t.me/persiana_Soccer/29343" target="_blank">📅 00:28 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29342">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/m5ZUVfix09KmZNXqAAkkPKaprVRMjZjCLNko4cM_5Unm6fpkEpZ5dKYhTUgVMmeKdxhgZc3iNrmA91zuODi7yrRlt4dIphX-iDzBU7yQPRn75VJiSC8_nJh1GoRNCL_eWJIJBUmqqGnieWl0Ntjw-sD5m6Sknj0C4lUQoGNF6G2tLSgDWfBL4OAdmcsG-drgxVjld5B8MuywfXOOdOyo-tRsGO9tPknHE6-jHRcfZMn56RbI7E6UuYDhAUbXhYAFU8UxBdC0nOUBVT6F1dtDil07e5Bys67G7mbDMBfXzaeIPA-nUKPWYDV4wZvdA1440ribHrYHQiXWCmMP1n_3FQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
هفته‌اول‌چمپیونزلیگ؛شماتیک‌ترکیب رئال‌مادرید برای دیدار امشب مقابل اینترمیلان؛ ساعت 22:30
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.7K · <a href="https://t.me/persiana_Soccer/29342" target="_blank">📅 00:11 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29341">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/51b900e940.mp4?token=kRHHbLprySyHDRP-CvT-FpXGPuoA_2uP_MLCEvVZ6iypxdIoq-2ZDV5Grc--Q7CAAzpQIgwrTRGazcZ7XcRSNtEd4sYzIb_Btmp2lRKQ8WtD6ElfjM29RdZTbr2MJW2ngjlBnIizoyQ1aJBKQpBMo3FR-Co-GY5c91_84m-D4r6nMgyFlaBywL77d_srJ36JKIc0JjSiyjJ1m-dRVCHOJzPEwuGgH7qGtqaJ7qjoEGTtum2ibK-ZiEz4wjomEJc0DhM01tTkwf9Xyk1H6124icm-t48_XTyH8NZs01fNRAhdhv8TZEtfgNpq-hATEvgc4KDAewH2P18k_JEG9rXEgw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/51b900e940.mp4?token=kRHHbLprySyHDRP-CvT-FpXGPuoA_2uP_MLCEvVZ6iypxdIoq-2ZDV5Grc--Q7CAAzpQIgwrTRGazcZ7XcRSNtEd4sYzIb_Btmp2lRKQ8WtD6ElfjM29RdZTbr2MJW2ngjlBnIizoyQ1aJBKQpBMo3FR-Co-GY5c91_84m-D4r6nMgyFlaBywL77d_srJ36JKIc0JjSiyjJ1m-dRVCHOJzPEwuGgH7qGtqaJ7qjoEGTtum2ibK-ZiEz4wjomEJc0DhM01tTkwf9Xyk1H6124icm-t48_XTyH8NZs01fNRAhdhv8TZEtfgNpq-hATEvgc4KDAewH2P18k_JEG9rXEgw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
دو سوپر گل دیدنی شهاب زاهدی در بازی امروز جوهر دارالتعظیم در حذفی؛ ضربه سرش رو ببینید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.3K · <a href="https://t.me/persiana_Soccer/29341" target="_blank">📅 23:50 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29340">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gtIVccgzJO7TFRneekJOQDZjjUmu0WdD90ToktTs-KDwbfj9EDco4QWSJ9a7BdeUiB1TaHzfLm0T8BcLO0fxzt-hP3wOzWp266pq3wmpSJvFn4qy-QwXq_KgJMIg8qSgnYWf0YCW8rcefKgrSZtdpE7Wv-kpwj8YCap8LwKKWzADXZM4hjSu4c5GhZDPYNQUQnyb_IIuA9ZuxPX486y-BOKfu2aPnKJ0zAvW_W1s6o71Q95VKtLZoFMFYAeWXYo8aUq7ejDp1y2lGMCHgFdISCtYb7vSxRYvrs0ffl3PmNzuwA18DczU25bNNXetBTBfcxxeDHRcFxTfbE5i6SDpGg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
وضعیت برگ ریزون بازیکنان السد و الجزیره در آستانه دیدار با استقلال و گل‌گهر؛ السد امشب چهار بر یک الغرافه رو شکست داد و الجزیره نیز سه بر یک تیم پر مهرهه و پرستاره شباب الاهلی رو برد. تمومی بازیکناشون آمادند. العین امارات هم حریف هفته اول تیم تراکتور در…</div>
<div class="tg-footer">👁️ 50.7K · <a href="https://t.me/persiana_Soccer/29340" target="_blank">📅 23:36 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29338">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">🚨
🔵
#فوری #تکمیلی #اختصاصی‌پرشیانا؛ مهدی تاج رئیس فدراسیون‌ فوتبال عصر امروز به مدیرعامل هلدینگ‌خلیج‌فارس قول‌ داده که روزچهارشنبه باشگاه استقلال روقهرمان فصل گذشته لیگ‌برتر معرفی کند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52K · <a href="https://t.me/persiana_Soccer/29338" target="_blank">📅 23:03 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29337">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">🔴
👤
#تکمیلی؛صحبتهای‌پزشک.پرسپولیس درباره مصدومیت عجیب مهدی زارع درپایان تمرین امروز!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.5K · <a href="https://t.me/persiana_Soccer/29337" target="_blank">📅 22:53 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29335">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/sFibL4_wOkF9V30_VjIxA97niEN2Muj7T5yA06AGK6dNtfugfS30e8FFRmG-BfYHbHTQLFu24jE5IkxQmZyCJTxPd5OoztgSlycB1oSEk7bwmy9Pjg8D4GEx_GcWI59Xdjv02KrDsdBqL0HRlDqiiVCSMA9VnPLjRvd9u2wlMPSAs7QqlLOykgCpWKvsnumdf0PqJT8gQwnRxw8x2rfnQg-QfDlM_bddA4hzgUS_K_VbaWh_0ehyU4tlLpbSxUnT1dZEqPmCIAMZBVEiRtt09_77NUTLOaKBinTc-GIc1f2GUqr_5SFycTJMNNzUK_fXSi-OzM0kN6k_KAPYOOr2NA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/pWFqWcAPAvf5QU2D-MfIeZk1mt3fd4VRobLHFxeu9p5vcs6q2XDBD68438kjAZrk5BwRHwvIZLHHdso3VgVbQFI9R17nLM152f8R6DTEAMOqWRKWgBvB1F9NTH8gWPWY0QRePV9Ne0auSW6qsKvhCNDN5ADFVOFwdWYX5fltWwQeXKwfzgpkVI55Pr5BrhJtlPGIPJCo8fFT-A3u40AqAAPqZ49hk7cGxRMDpZ5MQKLBIf1xSK2eseVJTrQPdR9z9jb2nPvbR8qDwsdxE66biYO_x7_DS0-6NW5zw38IUEy3B5347YwwnEQj2tpbsDsRslJwq03w658MpoaG8uXLuw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">‼️
زهرا گونیش ستاره تیم ملی والیبال ترکیه که بخاطر علاقه‌اش‌به‌کشورش پیشنهاد لژیونر شدن و حضور در رقابت‌های‌لیگ‌برترایتالیا رو رد کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.5K · <a href="https://t.me/persiana_Soccer/29335" target="_blank">📅 22:40 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29334">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0e83f3f081.mp4?token=ifBAVHnHyRVAs6jf1CEZT82Cqe8d4LdG-Dkdq6A2RRMKKa9EaHf-R5vj4iYr-d6qkBsANdLmGzLZrA9cUMtRF4pZ8ctUmAmRZmTnF5GyO02p0WC22qRjh_L7gJUalgtXUi0m66fLzwj3PtgAMiDE53bSOkBDAYPmPTXCZrROtaE9_V8k0X8VyExwqThQJmnIzIHTelO2UsYxfylaydint6aRrVJ-NJCeq52tvH-lSn4OM-78YVFXnMVOjy6YAi57z1ADPZ131Gnc1IQnjrTDBxRvm5iWS3K40UxlO7cVcMd5LB0pZz44h0A03us2a7afnyDzdMSC-8whRZPKAzbnPoH0ImREHW2Mo0IyIljUfM15vVukp0kFG9AwPKZKq99mIruRNJfZYW0xhEWQievZJVhV_WI6xSquV5ptnj12bhxfgcERKotwlggoAXvvfPLn57WYVwlJ9QOypQiQVcwjpG_veL5vMiu8ggbKQf7F-8LGeWxpznxej-OXQHb3FwcDP6n5maIoSeBWMm2G8CSLuFD-XhYVwK0Zp2whW96d7jzkx6pC_u4Z9BHs6Pe7615uA0vU-_1wjTN2U4BQGuCvyA-BWX0PDAWVUBInnnhYt9rl-yk4QLoM4ogPclZVNvn2NqSlqPSZt10wjioeI_Icf-XG-EqPH8OIc5Z4JvzjJyk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0e83f3f081.mp4?token=ifBAVHnHyRVAs6jf1CEZT82Cqe8d4LdG-Dkdq6A2RRMKKa9EaHf-R5vj4iYr-d6qkBsANdLmGzLZrA9cUMtRF4pZ8ctUmAmRZmTnF5GyO02p0WC22qRjh_L7gJUalgtXUi0m66fLzwj3PtgAMiDE53bSOkBDAYPmPTXCZrROtaE9_V8k0X8VyExwqThQJmnIzIHTelO2UsYxfylaydint6aRrVJ-NJCeq52tvH-lSn4OM-78YVFXnMVOjy6YAi57z1ADPZ131Gnc1IQnjrTDBxRvm5iWS3K40UxlO7cVcMd5LB0pZz44h0A03us2a7afnyDzdMSC-8whRZPKAzbnPoH0ImREHW2Mo0IyIljUfM15vVukp0kFG9AwPKZKq99mIruRNJfZYW0xhEWQievZJVhV_WI6xSquV5ptnj12bhxfgcERKotwlggoAXvvfPLn57WYVwlJ9QOypQiQVcwjpG_veL5vMiu8ggbKQf7F-8LGeWxpznxej-OXQHb3FwcDP6n5maIoSeBWMm2G8CSLuFD-XhYVwK0Zp2whW96d7jzkx6pC_u4Z9BHs6Pe7615uA0vU-_1wjTN2U4BQGuCvyA-BWX0PDAWVUBInnnhYt9rl-yk4QLoM4ogPclZVNvn2NqSlqPSZt10wjioeI_Icf-XG-EqPH8OIc5Z4JvzjJyk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🔴
#تکمیلی؛ مهدی زارع به دلیل مصدومیتی که امروز براش رخ داد2الی4هفته دور از میادین خواهد بود و دیدار با خیبر خرم آباد رو رسما از دست داد!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.9K · <a href="https://t.me/persiana_Soccer/29334" target="_blank">📅 22:25 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29333">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vJETy_o_58av2T9icVchyurzheYnf3lBEB4c8ocDMm5Y21CvD2_Pb3A5qDnBt8JbQw2g1WkVoNd-RSoIvN30s-ftnU5Q2UxyusPMhfnK6o2tSm7qW_LaEwHK9Wom2NYkj_kQFW0UdA0IcMIN8PYLfunvCgn33Ys77Pr3F2XRs1LiRta7R88cLpeJ_Kys3lX8nqOw2R_-yxRZZiZHke4CCsNFxjeaigxeQXtzi4Q0s005a-VIj2FTyPRMa4gaTMP4roA0TCKbYZrXQknigMlJq0M9tc2f9GdMpZf-t2OYfCovoujdEF_50M8U_PZ7usqDvHhGYt9E1KLcGVWgmUkoJA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
ایننرمیلان هم امشب بااین ترکیب تهاجمی 352 به مصاف‌رئال‌مادریدمیره. مورینیو هم برای چندمین هفته پیاپی یان‌دیومانده خرید 140 میلیون یورویی کهکشانی هارو نیمکت نشین کرده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.3K · <a href="https://t.me/persiana_Soccer/29333" target="_blank">📅 22:18 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29332">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DWTqj80PLfmdxpgWXtYwdOa5PbfuOn01AdDE_-0hmQzho7E2nW4r9Jp1Iuccjm_7dimPRkfaJ2pofBoPOhyITfj8LIdgcNMN9HvkRAD4M8K0bkj9f5PP4q8SUXpCMbQ3P0YVYv3SJ-GRgGLhxKTeea6ezhAd_Yz-hsYZWiLCCTAwYb0f6dIiYXWvyYoDlAt0T6HwJLx7a3hq7_NNXwkmT_l4KQFew9IpurqtkV1P7lu_1xZnZVh6JGqJJhghf4Z0SQuu9l7l9towpNQYnlN2w74nruB3dqc22y6Ud6YVVbvvGUKdtH7TOxtsUH5JVCyl54VwIM-b3et_s3gEXONF9Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
با حضور لیونل مسی آرژانتینی؛ لیست 30 نفره نامزدهای توپ طلا مشخص شد، مراسم اهدای توپ طلای 2026 روز 4 آبان درلندن برگزار خواهد شد.
⚪️
Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.3K · <a href="https://t.me/persiana_Soccer/29332" target="_blank">📅 22:12 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29331">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UQH6slCBmqdAHD4nCar0VfGKs4F69aJRBeQ6GKpbjNg38xE_hpyIqj1yy9Rl5c_TQoVKbReqCKOiOGBK_uh4o5AR9ofsrnyWgONyAVwuOGyAR0z5yFJAz0N7nL3dAzScRF4fV3plipMNWOzqDVINjIde_cXnkbrfnQJRpTCXhPvoC0i7q7IgIczwjTm02jIpk_j0Gw0uzI3jQO4Treag2blhkxFY1ufhhFbkK_pxvDH_athONgHhc94SPhTCz0lAsTH6VlOlVKWaKOR5rWGItVoFB6qLA9lG4ziHRtswysQr6p0PZvC7YKALs6vl6LQXWBzf4u_kOfLURJPAE2vD4g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇶
👤
عملکرد تیم دهوک عراق تحت هدایت یحیی گلمحمدی درفصل‌جدید لیگ برتر عراق: 6 مسابقه، 5 تساوی، 1 پیروزی، قرار گرفتن در رتبه هشتم جدول!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.2K · <a href="https://t.me/persiana_Soccer/29331" target="_blank">📅 21:57 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29330">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uRZnwmb_2X1XeQ6B_wL1htcguFt6R4-C45x4nt0Mfi_cc_4lQtENWRXAIuA6a7dXbQuQN1Ww3TvNw870IOIJJqd3YULk2Jgt5QxbmKzGfMB2EdXwCmTm0fNH5A-K-iDUInFoaVZJRFw9BesaBaIdL3t3N4c82r8Wm_rkueFV8rihrXVHD4bpPW5ZxV3qharnWkD9ue7jktbe5b_HKaHXPpOWr_K7jHkx30dAWrE4ZMbmgtGA7BpACTzvAH7zFcdeLWX0hoROX5NJCrQz5Rim8pX61Yzk4kEJ1oj0kn-CtWN87q5N_YboSjY80P3CaPMdIldg1dpVmCQFFnQn2d2acA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
هفته‌اول‌چمپیونزلیگ؛شماتیک‌ترکیب رئال‌مادرید برای دیدار امشب مقابل اینترمیلان؛ ساعت 22:30
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.8K · <a href="https://t.me/persiana_Soccer/29330" target="_blank">📅 21:45 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29329">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/la9LsLflzugHgFC29ZaAfSnduy9nK27Cev5WANOybd6N80s3-5lva8c8eJNNsttDIZhMh08XVPj6DcvH1M3HoZu1TcCAJEax-JBTfTpmSYliEtJOKInQgDNUScSNi52rtqD0LYX22xEEn9DBZCnf0z9c79nEp8dXaVe53TIoPbtQB6zHurF0_r-AWXOEaErhERqk7u7YqKYP48hl7VNS5tQYRuvTOLtpQj3caoUEooYyC1i7gkR-obqR-d0SOlz-qKOKxThIEw2RZ9OJ7aPfPD0orHe6nUvNkgjgaxJa2qLTHok145i-8aSjhYek0t1x6eGztzHgjAUY91eQgXBJ6Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
هفته‌اول‌چمپیونزلیگ
؛شماتیک‌ترکیب رئال‌مادرید برای دیدار امشب مقابل اینترمیلان؛ ساعت 22:30
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51K · <a href="https://t.me/persiana_Soccer/29329" target="_blank">📅 21:18 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29328">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/939eacf7b5.mp4?token=hih2Xy_TkY4Vuiaij76QKZzF-TTMAuFhLKLtAP_D50nxlublY0PCmagouoLjFgRh7NraF66dkPbBuwJYnHkmBbB0AJ4CT4_qMk217784MEW2sEQESXFjQEH4OQBS1xpphx5ZwlYEgZIZFZEBu0dq39tvIuU04LFeUr1OyxZAVDJPaQLJuKyhAzRDr_8Eqprp-pc0IcXctSKZSgKrRp3h1-xPzsmJV1yfWuVOZZOfyrxv9I3B57-RS5BLPA9JtjQs-xCf_KhH80SFol7DnwsxYuAw0YYIl54aD7Mk_EotuL2_q0kkIET7aplm_jXzClEvmLpF0XkILfNN6zbCp1ipVw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/939eacf7b5.mp4?token=hih2Xy_TkY4Vuiaij76QKZzF-TTMAuFhLKLtAP_D50nxlublY0PCmagouoLjFgRh7NraF66dkPbBuwJYnHkmBbB0AJ4CT4_qMk217784MEW2sEQESXFjQEH4OQBS1xpphx5ZwlYEgZIZFZEBu0dq39tvIuU04LFeUr1OyxZAVDJPaQLJuKyhAzRDr_8Eqprp-pc0IcXctSKZSgKrRp3h1-xPzsmJV1yfWuVOZZOfyrxv9I3B57-RS5BLPA9JtjQs-xCf_KhH80SFol7DnwsxYuAw0YYIl54aD7Mk_EotuL2_q0kkIET7aplm_jXzClEvmLpF0XkILfNN6zbCp1ipVw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📊
به بهانه شروع فصل جدید چمپیونزلیگ؛ نگاهی بیندازیم به تموم قهرمانان این رقابت‌ها از گذشته تا کنون؛ رئال مادرید با اختلاف زیاد درصد جدول.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.3K · <a href="https://t.me/persiana_Soccer/29328" target="_blank">📅 21:01 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29327">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d64e7feb91.mp4?token=CQNwFk2oOiaA4N2k7hi95rFGvWeUm87G9mVwLO5xrLA61Uk0n6snrY3sqM8-8AakDD8Cdj4XWJouf7IttlgxchyiQyUBSSgVn8X-NhnXloD8PQK4F0HSzUXS2kUMig8pnoyHv0y2SSYJoF7BNxll35a9fyzIY8SCYakPOQ-DUwOekmeSJJChxoaiK5mJ3n3zcF-9YxvYIDrqg8F5Xm1NJ4f8OZbWRPgisALDVtgXYbj7zwQtOCXCHNEvoMjAlfsJkG87Mpfe-IdGC6i_bQNSGsWGC0LXIZyH1H-O4IZ1-zgNxnZ0VwUCcBjprfD7ZUKQ_nxU0EHDFXr3sYFfDMf_WGv8rcLc7npRppIuBV4dxnEUulPF4iCreQrDei9G_Dr5PEEsbkU51pu4cjNOlAfoJoFRS3U_7ftnPrnm4oBuonPY5j0jVjk_ydXQVfksH3IIlIpvUKBNRF5KH_zgmn3h1SAf6kyXO3LncsV_dmnHnn0OHFw220CEMUxiL-7-H0j4XUPFfaroo4KfmE8rAE5ZujXRtvbxN2ErzW6Xj0i1glipjHnzSxYKf16fvUQrQCMq8bIUhO-mdEt9EptUmSvsktEvgrVJeUJpgX-thTevvXUMeYg3PehVXSN_HoepJKPKFjFzM5cNb_8iPlO119qD_atnoaau3JjINTHe4qsSH6Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d64e7feb91.mp4?token=CQNwFk2oOiaA4N2k7hi95rFGvWeUm87G9mVwLO5xrLA61Uk0n6snrY3sqM8-8AakDD8Cdj4XWJouf7IttlgxchyiQyUBSSgVn8X-NhnXloD8PQK4F0HSzUXS2kUMig8pnoyHv0y2SSYJoF7BNxll35a9fyzIY8SCYakPOQ-DUwOekmeSJJChxoaiK5mJ3n3zcF-9YxvYIDrqg8F5Xm1NJ4f8OZbWRPgisALDVtgXYbj7zwQtOCXCHNEvoMjAlfsJkG87Mpfe-IdGC6i_bQNSGsWGC0LXIZyH1H-O4IZ1-zgNxnZ0VwUCcBjprfD7ZUKQ_nxU0EHDFXr3sYFfDMf_WGv8rcLc7npRppIuBV4dxnEUulPF4iCreQrDei9G_Dr5PEEsbkU51pu4cjNOlAfoJoFRS3U_7ftnPrnm4oBuonPY5j0jVjk_ydXQVfksH3IIlIpvUKBNRF5KH_zgmn3h1SAf6kyXO3LncsV_dmnHnn0OHFw220CEMUxiL-7-H0j4XUPFfaroo4KfmE8rAE5ZujXRtvbxN2ErzW6Xj0i1glipjHnzSxYKf16fvUQrQCMq8bIUhO-mdEt9EptUmSvsktEvgrVJeUJpgX-thTevvXUMeYg3PehVXSN_HoepJKPKFjFzM5cNb_8iPlO119qD_atnoaau3JjINTHe4qsSH6Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇸
🇧🇷
ویدیویی فوق العاده از دوران درخشان نیمار جونیور فوق‌ستاره سابق تیم ملی برزیل در بارسلونا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.2K · <a href="https://t.me/persiana_Soccer/29327" target="_blank">📅 20:52 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29326">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/u9Rt4lz8_UfX7A_6uVSZE6l7k8SLZUAmFeaRREZRJ8by-5dUAdMECOo0Ria9JaMa51sTzgL9eLsXEcj0JyWphIwKpoQ_GeNEemBbhqgUDaxX_FOqSqlJPVCqZ26r5YlSoUXr1xlJERkEEclN8rUZamU9YzBpFVzI8_rJyyMZ61Ua24aM35xdvi8TAc2ikew_zNf2EfOJ0VS4tcMFLvJs_miOkqDRfipI0iMqWlDD4AW6BQeUdsu6DMKukvSoZQPfEDPq6UKof8OqDAgv1W3oH7iQnvVhWmjaFOQp6blh8ZjtPZsR9qzsj7oedUV7Uv_NN8fJ6jwu6v0SAwS9mrnrYQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟢
🔵
سامان تورانیان مدافع راست استقلال که در اواخر بازی با آلومینیوم مصدوم و تعویض شد امروز درتمرینات گروهی آبی‌ها شرکت کرد و مشکلی برای دیدار پس فردا مقابل پیکان نخواهد داشت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.9K · <a href="https://t.me/persiana_Soccer/29326" target="_blank">📅 20:34 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29325">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bBZ5y9JoI6fUu1pn1B_pJIOVeGhGtaSbTESjfg88AgDlJaU2jaeJpeloQ5SEJSuEGAMbEuCNqmXmGYCX1UHCX2-2IIXHRLj-yvNFNUTNLu7nJMyGSkzL_TmxgMSS-c-SLFhiOtcvSwCN2UykNnhLHl_Ca5CbbYyx1CWoGuEB2KiKH5UEGzG_SkLyRc_YLtBLuu9TfTL2vYbmRkip5luZzqGaQbpdLk1jMA74htotyjMOsvosfCb7-usKMI8c4CPtK6sxqVShblbMR56xLHu-iw5ZBNA9Tq-IGzhYnwjWQSVd12b6lohI0xwK-ukw7WLRM5QplgUcKZdnDnAfEiqIgQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
در فاصله چهار روز تا دیدار با خیبر؛ محمد مهدی زارع مدافع‌میانی‌جوان‌تیم پرسپولیس در پایان تمرین امروز سرخ‌ها هنگام دوش گرفتن پاش به طرز عجیبی دچار بریدگی شد و حدود هشت بخیه خورد. احتمالا خواسته که موهاش رو بزنه پاش رو بریده!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.5K · <a href="https://t.me/persiana_Soccer/29325" target="_blank">📅 20:24 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29324">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/M3bqobfMntnHE_MjHPmUDU2lzW-lsGdNaknSBIA3zRz3dEmDxBUm3ZLm4Cjofb93ebpFuXTENpKbdF-A024-B2UhM9Pga5tL2zrTMYE1d5kD6SXueUEwAeEBz8s0fm7H7paQfa808hnOAmQaEfMM6_h8YmCEw9JwxLPMrR-z-hP9RGbwjA_aIDYzOLxKovjuV5W6jEK4fcXi74HCGvQZNqu5DK9B-pKuH2v_H8ilIUHmNb7ANanvR5xz3HHzimdzSwI2Uk0-8nxgnwBJAlAi77Exn_Y01EdDjiNI2KuSnrqCgZsO0kmPNt4hf4DLVJ0bY2TCyZZq7atG-5MnAcESQA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
تاپایان‌هفته‌ششم‌لیگ‌برتر؛
جواد نکونام، پیروز قربانی و سهراب بختیاری زاده سه سرمربی هستند که تیم‌ هاشون هنوز متحمل شکست نشده است.
⚪️
Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.7K · <a href="https://t.me/persiana_Soccer/29324" target="_blank">📅 20:10 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29323">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mgDRXzImh-lDfH6OSHViznzeDwHwBoAarv0AbQRv_0RQ_tYIvJX_VmxdsLUvougAkarcGEiqheq_BcTuv2XrMqipH2Pmfrl9EXzQ5Lsi-IgFkKuvUhAdepQer35EwxAvlp10P5mE0JFt0KPFGd26uO7pbhGJ8agXkeqbx87tRuHFMt4U3W0vYM6mBc_-EQEBKfL18I4lsVuvx06vfDvQlRJDRSTDkQLzBTdkIyxdd6cZpkjgEvGbUrZCOB12EwPxpKT_Gj0BLO7AKbtGd6e8Vy32wuf3vkxn_icwp6GifhQfqpxKNR4ZlwNBys9yQonD3Y9KxFy0Z-0yFcYtRbnJbQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
از پس‌فردا دیدارهای هفته هفتم لیگ‌برتر شروع میشه. تراکتور دراهواز به مصاف استقلال خوزستان خواهد رفت و آبی‌های پایتخت با پیکان بازی دارند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.2K · <a href="https://t.me/persiana_Soccer/29323" target="_blank">📅 19:41 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29322">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3830a1509c.mp4?token=dcH3x6Uu2TJ0piOZznHZDea1SkNkkpHl1WBg7HC6K8Y9E8CJhZM8EoefyERhcjX7vNhA3Jel-Z1KfL9JztJtl3P_Z35ZP86wpiadI_Icul-Wfq3DUdtquiE_6HKVBmNzs53bqm5DqEeIIMfnVkbLlg3lWmgplp6o2A8Dinu5CppRtKrhNPm2sggcd5rfW5iSv3IafMuWV3D9eWPYulE65DEs-xUUJsfnxiok5Lo3_73vDUXcHfIWv7i1rO1S6tb_Xpu5bOdjmDTIyobqvnTTGoD9FK3M2ZBJJQoMLWULrniamq495OSZu_m102KLOyxDPy1nBwFBw6P6yYnpWXsjAw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3830a1509c.mp4?token=dcH3x6Uu2TJ0piOZznHZDea1SkNkkpHl1WBg7HC6K8Y9E8CJhZM8EoefyERhcjX7vNhA3Jel-Z1KfL9JztJtl3P_Z35ZP86wpiadI_Icul-Wfq3DUdtquiE_6HKVBmNzs53bqm5DqEeIIMfnVkbLlg3lWmgplp6o2A8Dinu5CppRtKrhNPm2sggcd5rfW5iSv3IafMuWV3D9eWPYulE65DEs-xUUJsfnxiok5Lo3_73vDUXcHfIWv7i1rO1S6tb_Xpu5bOdjmDTIyobqvnTTGoD9FK3M2ZBJJQoMLWULrniamq495OSZu_m102KLOyxDPy1nBwFBw6P6yYnpWXsjAw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
به سه پاس گلی که نادر محمدی روی پرتاب‌های اوت خودثبت‌کرده‌حالارسانه‌های خارجی معتبر جدی جدی‌ دارند او روبه‌آرسنال و میکل‌آرتتاپیشنهاد میدند که‌در ژانویه این بازیکن رو برای توپچی‌ها جذب کنه!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.7K · <a href="https://t.me/persiana_Soccer/29322" target="_blank">📅 19:29 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29321">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FIal_3JajKN3obbTIg9afDwqmP7QYr6bemF0kgmSnFU7oqnqzjVZiYXf3jhXoSjHFJMjf9UbAYH03gZdfU8w_buAdlORw2Vd6FwQsl48wYVsuHem9mDRJV7rb8il4n2ejmd5oYgEMgvqpF-iZJsO4PzHj2Fp_rHS0oAE6Dodp8_mQtvXgpKioRQRwcE15cL2V35jzCFREjzXv31iwuCdbAdX8l1bhP4J6BpoUwCNnjurWebssfSlk3zFo2tkjWksEbblFtk3aR9HZphSchKLXkfbCNswowzCzlOA7IX7eduNVBQLoJntdFnDCYxon05pOPrdFxtg_6Z7WOoxGQ20sQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
با حضور لیونل مسی آرژانتینی؛ لیست 30 نفره نامزدهای توپ طلا مشخص شد، مراسم اهدای توپ طلای 2026 روز 4 آبان درلندن برگزار خواهد شد.
⚪️
Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.3K · <a href="https://t.me/persiana_Soccer/29321" target="_blank">📅 19:29 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29320">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromBetegram</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XBnN_tLMyqRr1_JfDqa6yz4J1wFk0QpGB1epwZx3tLTrJj2r8_wOzj0MIedEOim1WrUiTX23opluA0WcXofQP3joFDN0mu-HzKC3gxUBF4GBBo92g30Tpp0eRwfcJOeHuW2iG6l00HVZ6E2QLV6XPjZx49J_8FnkVyNq5cBEEGrYW7wvnwksn9neo9xaF84TOuRX0EIQzJYrMLA-JKe3LUOpKLas9FctvkM8WTS02sL7eSXmy8D56Pkvk4WBJlOua8Enhi5u6Obl0Jq-Y2bWy7dVHhXTIkUir9Uex-rAnfeMPPLt1rKJcabQ6ShIhWZsVSRmO4rboHCI6YEPPHLBzA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇺
هفته اول لیگ قهرمانان اروپا
🇪🇸
رئال مادرید
🆚
اینتر
🇮🇹
⏰
ساعت ۲۲:۳۰
🔴
بیش از ۵۰۰ نوع آپشن پیش‌بینی برای این بازی در‌‌ بتگرام
🔼
با بالاترین ضرایب پیش بینی
💵
واریز و برداشت ارزی و ریالی
❗️
🔥
۳۰۰٪ بونوس رایگان بر روی اولین واریز
❗️
💸
۱۰٪ بونوس روزانه واریز رمز ارز
❗️
🎁
فرصت را از دست ندهید! همین حالا پیش‌بینی خود را ثبت کنید و از بونوس‌های ویژهٔ Betegram بهره‌مند شوید.
🔵
http://betegram.com/affiliates?btag=3_l7</div>
<div class="tg-footer">👁️ 49.7K · <a href="https://t.me/persiana_Soccer/29320" target="_blank">📅 19:29 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29319">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/197500367e.mp4?token=GA63JsFfhZXRMRm89ILGQqNRyG2HTYjh4YxH54985oLAYsRZbiaFXmooUqn5GTb2mc-TsBknAJK0jNFndteLd3wbvfaUxPcmVag9eLVEsKVG_HsUGRCybc8mfKMXu7Ztc56WHxsVIsZlLqYkJ1UvGTkv5gVnoVHBgdLPA7mBNsl0hd4_vog38IgFYwzStSqR_ZdNcrIbP9X8S3v3P5SV6-vt4paFq4yB6B0cUd2QCdtZFrsXb9DhdH41H-gBpFwYEAZ-xBaUVjoqsG53P0tRVY_B1JEpfOM8i_sH_KoIQdJBz_K-CRDax9SPKy0yVZzpJbWNgXutMgIJmHOyllfzdma-9tFpYzMPbclPHN56KPwgDa465GvbtUMtmEkFXT9xOzSagT_YnsIMy2Is6MbcA5FZSZDJDa_B0Fgkrup87phF3CFfzqn6rI1iTMkLZR3OMSd0bITr9KPO2QsTQ1cZjeXNd9lSxFUy0qCMBuqhD9_9T8VP70G4mE38mkk_nHLtIcp4L8Fbh_W8S-G1N8Io3v1pDEHlAlCT6IdOmUHS2RzkyelWYR0c6QGrU4-zaAK5rHdZ9U0m_WjH21vcZEfJqcfxLaKnM7iR5Wj6k8R5h_TiZCUCEp_KOrLm2shselDuIb9WT8FgXsQrldGn5w3vQU72RWDUMY1xs02tc7vrzA0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/197500367e.mp4?token=GA63JsFfhZXRMRm89ILGQqNRyG2HTYjh4YxH54985oLAYsRZbiaFXmooUqn5GTb2mc-TsBknAJK0jNFndteLd3wbvfaUxPcmVag9eLVEsKVG_HsUGRCybc8mfKMXu7Ztc56WHxsVIsZlLqYkJ1UvGTkv5gVnoVHBgdLPA7mBNsl0hd4_vog38IgFYwzStSqR_ZdNcrIbP9X8S3v3P5SV6-vt4paFq4yB6B0cUd2QCdtZFrsXb9DhdH41H-gBpFwYEAZ-xBaUVjoqsG53P0tRVY_B1JEpfOM8i_sH_KoIQdJBz_K-CRDax9SPKy0yVZzpJbWNgXutMgIJmHOyllfzdma-9tFpYzMPbclPHN56KPwgDa465GvbtUMtmEkFXT9xOzSagT_YnsIMy2Is6MbcA5FZSZDJDa_B0Fgkrup87phF3CFfzqn6rI1iTMkLZR3OMSd0bITr9KPO2QsTQ1cZjeXNd9lSxFUy0qCMBuqhD9_9T8VP70G4mE38mkk_nHLtIcp4L8Fbh_W8S-G1N8Io3v1pDEHlAlCT6IdOmUHS2RzkyelWYR0c6QGrU4-zaAK5rHdZ9U0m_WjH21vcZEfJqcfxLaKnM7iR5Wj6k8R5h_TiZCUCEp_KOrLm2shselDuIb9WT8FgXsQrldGn5w3vQU72RWDUMY1xs02tc7vrzA0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
دبل‌دیدنی شهاب‌زاهدی برای جوهور دارالتعظیم در بازق امروز این تیم؛ زاهدی در یک ماه اخیر بعد از پیوستن به جوهور دارالتعظیم موفق به زدن پنج گل شده. شهاب زاهدی این فصل فوق العاده آمادس.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.6K · <a href="https://t.me/persiana_Soccer/29319" target="_blank">📅 19:14 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29318">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aPxgujWMLI8VVjecNCpMI4BqGYhBY-qXSvDgbC9QlpWHGutuGsMZ-1RpOJSoeeEyuVFoseuMIZe5RRkjehZkHwrWr5VdQ8BHX2NIn3SnD8rOJXiPBJD6IK_FJPwGvmGQYD_xJJNEVIJo8SajvSz8qnqxhVz0iKGdKHPS8P1L3NlBZs3_UjVahKP5j2JLp47jgMA9mZNjd0czivVHMU_9L8AuEhUtyP1CrqKzHUhSLUS7McRBT51sJj7YyScBNsNLuhHhrM0k-E-XMp3uCV3SIKS10QM_wXkjVW0D3CyMPKvDQTqyJwmBaSYerpmJqhvzJu0X7vAKNVRFk1qq5aSZ5Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
به بهانه شروع فصل جدید چمپیونزلیگ؛ نگاهی بیندازیم به تموم قهرمانان این رقابت‌ها از گذشته تا کنون؛ رئال مادرید با اختلاف زیاد درصد جدول.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.4K · <a href="https://t.me/persiana_Soccer/29318" target="_blank">📅 18:55 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29317">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IymOn_3O_i_3LcQkBdFFYY6HnwZAUhw-gv7G6jMPWoOLad79HRt35azH0fsnc0J09NE7OrDLxgl8Q_VMlnwd_K21jv29IKo2JtJrmZOE9JWizA0Wc9HiWRRiF1uTLbdNuqN_BBPJqi92NaJrrSF3B3lLj977_4a76No0F-1RVZHADCkorAPAt0qkdL5ODufFieA71Ll8mk6zLeCr0qmGnwed0iCWfvuIuSprFeJktQA0jd5zDk-KAV7D-qFcrnutbEyZ36W9EMRDRlhOWbHGTzX7x04TKHiUrbFJ2emf_mUh03QcZmhFyyHvozXRDR30XLBudmyIiYJUbVLmcWi4Ag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
رکوردداران بیشترین نامزد کسب جایزه توپ طلا در تاریخ؛ کریس رونالدو در صدر جدول قرار گرفت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.2K · <a href="https://t.me/persiana_Soccer/29317" target="_blank">📅 18:26 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29316">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8ba4575c98.mp4?token=U9Yt0EAQF9Nx4zfiHlJ0YM089ZJcMc2by76H_1VWXeIK98VvZSoFI19Pb-ZVR7Q4BF8Gu6oMs0az_0h3XeZT7Cy6llrVdEyLACjRb8A2FVVbyRoCVOsRvEjMGvZnnQDbEiPD69G0r3a7meQCwWV0Hgvk5jxUN7GwzgbWPjMmGVYaQMEz8ccrotVCgcSiJbcVJXtWRGa34ZxND__2EZyZuc-rE3JGMDPOQBFxnN4_P0anqP7tCKq6jnz56-h1bfmR-zWEIJfJlxERtynq5ciXyNMaGXpj92gSPPhVugbF15exb-Pqye3q5ggP3CHEDwusS8sLcshMMhIQLjPFpevDoA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8ba4575c98.mp4?token=U9Yt0EAQF9Nx4zfiHlJ0YM089ZJcMc2by76H_1VWXeIK98VvZSoFI19Pb-ZVR7Q4BF8Gu6oMs0az_0h3XeZT7Cy6llrVdEyLACjRb8A2FVVbyRoCVOsRvEjMGvZnnQDbEiPD69G0r3a7meQCwWV0Hgvk5jxUN7GwzgbWPjMmGVYaQMEz8ccrotVCgcSiJbcVJXtWRGa34ZxND__2EZyZuc-rE3JGMDPOQBFxnN4_P0anqP7tCKq6jnz56-h1bfmR-zWEIJfJlxERtynq5ciXyNMaGXpj92gSPPhVugbF15exb-Pqye3q5ggP3CHEDwusS8sLcshMMhIQLjPFpevDoA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
وقتی بعداز مدت‌ها پارتنرت رو راضی میکنی که باهات یه مسابقه فوتبال ببینه؛ هیجانش عالی بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51K · <a href="https://t.me/persiana_Soccer/29316" target="_blank">📅 18:11 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29314">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/aaa9ce7068.mp4?token=ttEV92aTVqEOry7YTP3vzeu4rTYwLKbW3nZPVy0zqC_9A8oWOppkmhKj3jMXgbMVcisq7mf7FY_DPXWUbAJasCWY_FiotywiB7olXa1S4PpiMUr_ZxTLSHVMuE78GGb_04y6_a8wZ5bAx7_hgv8HIzASrVrYj_IG0tpXyeQN8b6QSgo9yWY1SkYONglmZjULuIKhrCGpcuJY49gMfkAi22oJ0MvYxwKkaw4OK7OrjwoOLZU0mi_X1rztMpg8RjthZPPOjmCZhv2v5nJz7k0F4RjUqLdO84qYL6ZJK9yeFeDP-qXh6JrkLn-9BRcD9gnvAhgyq0Tar7ltuJfcLi_hQw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aaa9ce7068.mp4?token=ttEV92aTVqEOry7YTP3vzeu4rTYwLKbW3nZPVy0zqC_9A8oWOppkmhKj3jMXgbMVcisq7mf7FY_DPXWUbAJasCWY_FiotywiB7olXa1S4PpiMUr_ZxTLSHVMuE78GGb_04y6_a8wZ5bAx7_hgv8HIzASrVrYj_IG0tpXyeQN8b6QSgo9yWY1SkYONglmZjULuIKhrCGpcuJY49gMfkAi22oJ0MvYxwKkaw4OK7OrjwoOLZU0mi_X1rztMpg8RjthZPPOjmCZhv2v5nJz7k0F4RjUqLdO84qYL6ZJK9yeFeDP-qXh6JrkLn-9BRcD9gnvAhgyq0Tar7ltuJfcLi_hQw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇸
لامین یامال ستاره بارسا:
"فقط کافیه تیم‌هایی که این اواخر جام بردن رو ببینید؛ تو پاری سن ژرمن همه پرس می‌کنن، اینجا تو بارسا هم سعی می‌کنیم همه‌مون پرس کنیم. در نهایت تو فوتبال امروز اگه ندوی، هر کسی هم که باشی، همه تیم‌ها میبرنت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.5K · <a href="https://t.me/persiana_Soccer/29314" target="_blank">📅 17:50 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29313">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/V9Lz2dIfC5yfavTGsPwFDGiks8gNiJ_HUAaIHwDG9COceFRQTDhAjao2VRaKnlAVyktQAwbF0aHc9NJvHnxVOa12t04hZxmHoyzjEAOFoOlY_5fOyTnvX-xSm6nXN0iGvzpUslJ1UjVHiOCQFDziJsZRsh2j2o5_NLtwg-zaUfrYRCw0uP-yW9Q1XY6MEomF6Hbc2Vi9Yqyy1TABDfuV_HmoFLiuE4SUQ4HnEjhdmM3fUu1w16lWAckk4L-S6JtQy7aXjdrhpQ1C3-NosTA16Q7vZz1Vhd7YViQMyhTdR5a7RsFR-PSbuUf3XqumeqQn3CNh058H-nYB-JRhYl_KHA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇧🇷
🇧🇷
پارتنر گابریل مارتینلی ستاره تیم ملی برزیل هستند که پزشک هستند و گفته دوست داره از بین برزیل و پرتغال یکیشون قهرمان جام جهانی بشن.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.1K · <a href="https://t.me/persiana_Soccer/29313" target="_blank">📅 17:17 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29312">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QHRUnKpJG8xgjQJejlrRwMu6B6QUy2UasJJwWkj01vm0Z832L9qVqNA4vbZ5S9yUTxadZF8_soAr4vDeelLfX4kfk2q4jb0rBIFXETVTL9lAXn90WIJ0Z6GamHo8GB9qGQUyr0MoQHnw0zeJzcOTtBA4lgipoKXXJnmGS4MJqLeYK7uMIjdqKeZTGbaXKnVPZdJnfxvWJcm_jqJWEuj2S5vBmEb7vrPLfpOuq9mUxBivainklzZx2xvx3Oy2o_-tIxLUzpOpL6SM4I5Q1lurW_xoZt_eLS1iR2Va8f-eld9iB07uTk03wN2u9OwQHRvN-keRsD1jq0EgvlzgnofoOQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇹
ترکیب‌احتمالی و پر ستاره اینترمیلان برای دیدار حساس فرداشب مقابل رئال‌مادرید در هفته اول لیگ قهرمانان اروپا؛ ساعت 22:30 از شبکه پرشیانا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.2K · <a href="https://t.me/persiana_Soccer/29312" target="_blank">📅 17:03 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29311">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/v8M_UvC7LJPxGXoBatAsA3pMzq6BUbRRXJEzEPFdKflCZuwS72nw6fTYOSuRmUN6oKdlwD2BcGpE8vUa4gg6foQtc0nEODg7TrxXQwMqkcWj41dxh_8lp9eSecfDofR5h-WDi3x9uge_XYcsOaYLspIt5KV7uX-cWNfInWKMIeg1A_IK6sXvh6_b0VeykEkS7hE187UbSZGjKerMwT0DPHXo3UHHDGBTyC1g5vElpGi9cHrjUEUemxIfvi1y9ybGNkvVkjWxvAhXFudaQm-kgj2jJNzcvgV84oPaa1iZrgDbQwYWZFvP7OQqvDymDBb6gZl4VHDQ1PeI3nl2mlB-eA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
#تکمیلی؛ اولویت بندی هلدینگ خلیج فارس برای مدیرعاملی تیم‌استقلال مشخص شد: ابتدا علی تاجرنیا، دوم شهاب الدین عزیزی خادم و سوم محمد رجائیان. از بین این 3 تا یکی قطعا بعنوان مدیرعامل جدید آبی پوشان انتخاب و معرفی خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.9K · <a href="https://t.me/persiana_Soccer/29311" target="_blank">📅 16:48 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29309">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/D1oBVTV7jvTlXZX7hJ9rSsbBQhr6JeTZguGTDjt_MB-zk3pmC7cOiwZpatsSyOIHpw2_1P4OCZc9hQsRfifZ05zmY8geL3-jSmEaMXDjO2fFGXgES0TB3QRyVjLK6_ru3kDSS0EsnljP2rxUJJCfbYVVUkMEiuvSHo-pRw2lbSxUkSkjeIPjBnwl3ZM9uvPjVtmWEnMgyLWYcfUzCOpfuGE1Ma15UlhW-mhf7ss1xoNUcOKr7lqWEi_y65qFBqljC08ZBSODWf2s-bBcUvLu2P-3e2CETEwERxftEbZoAvZc_wDevyZKR_SOJVrq4euHXa9M-CXywiOSdisUlrj-Yg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
مادر کوبارسی‌مدافع‌بارسلونا:
اینو حتی خودشم نمیدونه ولی اون هرشب تو خواب حرف میزنه. یه بار رفتم تا ببینم چی‌میگه دیدم داره تو خواب به مارتین میگه خط آفسایدو نگه دار بازیکن تو افساید باسه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.1K · <a href="https://t.me/persiana_Soccer/29309" target="_blank">📅 16:32 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29308">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">‼️
هایلایتی‌ازعملکرد موسی‌چنپو وینگر مالیایی سابق استقلال در تیم جدیدش پانایتولیکوس
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.5K · <a href="https://t.me/persiana_Soccer/29308" target="_blank">📅 16:19 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29307">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Y1wd5cRIMlZVRgBf07aXQ5oSCotpI0P4hFUPtzziSN2nPKcsT7UfSMC0yoO9yqpw0mOORf_Zrb9VyRK3KdPXfGaWuoZz0rMQptcqE6cPSc6aw5THngNiTnm2MiuVLBpGaVtj9SZLYQS3d9mw_IKZIrKsrhWoQtFTC2K4tOye7K3nHvj9QnkfzEBABp1YkFnxnCU-dypDa3oSDBaL_B17qGORmKXiElAcZDebMlXL9C5P8ePjRY9l3ACdZHzO1b6aWyA-tTb1rsz7hIHHFhxX2duvl95w8Otwkxk1PqV3p4WJWm_-ZmxcAQQGN1Y4DzRaydhU2a92ZLdSf2flx0jFGw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
بهترین‌گلزنان‌تاریخ‌رقابت‌های لیگ قهرمانان اروپا به‌مناسبت‌شروع‌فصل جدید این مسابقات از امشب.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.9K · <a href="https://t.me/persiana_Soccer/29307" target="_blank">📅 15:42 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29306">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/h3Ih8DjQLZ1vKWBwoh5yZErSDV-ecCyGdKgrzKEJ09lHPEEb91quYWVbh8OqCs2gKW7B731NNnTefasWHV5EkqXsgnu7XH3GxdRzYt4KL_JkTwHJbiUUJVCc5_PFy9j2guzynm66uNn9zbJazywiAdqiFCZTNyaUisYugV83prFA12EHsgq_25LWkCgApcNIXwXIRrFQFDSCBgOXTy745_3AsDOklVAzwXa-qUgLQCI8fS_h_s7aMtDcbxIfxrAQPBX6d1V1sKwAYnomqa1rI53xQ54pN069NQT7f_Q4vkNY6EPTpI9piFmrNNK61W_MXSK3iT9dZshSjb4j9sRsnA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇺
👤
به مناسبت شروع فصل جدید چمپیونزلیگ؛ نگاهی بندازیم به‌عملکرد کریس رونالدو بهترین گلزن تاریخ این‌رقابت‌ها با وجود دوری چند ساله از UCL.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 50.2K · <a href="https://t.me/persiana_Soccer/29306" target="_blank">📅 15:24 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29305">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cfa4b6c3a4.mp4?token=Hp-s4TyhnXAoD8DQANsQ4Tp7ZeDt2ZsKPdA8-egb9B1iTYqek9HSqsmvbEuQ-BP-6k5TqXCEI860SL8mGjr89X4hLljVIUIJd9tBgodVNjNRrWG5m2kHpuRrf0DoDYm0EFG3HSP2_hqwUTdhjEMbhN20PZ2v4jbBNrIp0kuztYiQVa7TKzFziw4DUqFS3pJhFYvR3aV5BwfAfrkR2tJ9sGz479o5OJRqO4Sfw5NKp2ukH37f48TeB0f6fr6EO9nQ9f0sPB1e4UG563q6XBuImhJkGy7dZi7VbXug8mdKfud8Tegx_TgMzxmaxJK6ZC8Dml0EPZ_JOb70T1cAHBj1hw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cfa4b6c3a4.mp4?token=Hp-s4TyhnXAoD8DQANsQ4Tp7ZeDt2ZsKPdA8-egb9B1iTYqek9HSqsmvbEuQ-BP-6k5TqXCEI860SL8mGjr89X4hLljVIUIJd9tBgodVNjNRrWG5m2kHpuRrf0DoDYm0EFG3HSP2_hqwUTdhjEMbhN20PZ2v4jbBNrIp0kuztYiQVa7TKzFziw4DUqFS3pJhFYvR3aV5BwfAfrkR2tJ9sGz479o5OJRqO4Sfw5NKp2ukH37f48TeB0f6fr6EO9nQ9f0sPB1e4UG563q6XBuImhJkGy7dZi7VbXug8mdKfud8Tegx_TgMzxmaxJK6ZC8Dml0EPZ_JOb70T1cAHBj1hw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
وقتی‌از لیگ جزیره به لالیگا میای؛ برگای رودری ستاره تازه وارد بارسلونا از سطح بازیکنان والنسیا ریخته؛ پنجاه بار گفت داداش اینا خیلی ضعیفن.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50K · <a href="https://t.me/persiana_Soccer/29305" target="_blank">📅 15:14 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29304">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Coz6qO3Vg-FMnvMneCP3QWd9LcRe46t57-jFDj15_6b-8LB_5IdsBHynMGeX8hWWqnAIqSGtSi5KuNN7cwNunSUfSgsxlBRIh639bSWkYdmvCUnKqY4BI_nfP4Vw0HeG65Oy_17StX47QE9hbJh6eBFgFnmRT9eM8MaHRVB3uOuvDGZwTvb3ZeCSfHaOlBXG9gR2LPuHJ2Ff-TfmDTx6M36DR0QG97UcReJrLwCakMKMA_lDINxdi9zJgrzjbF0PB8rVJLm8Xwq_uBPTg4-8uxlI2k2zYPEDpGYPuMd_nFqlOXaQi-YPOotu6yC6N-9Zev_nidUMehCVx0uonXDzig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
محمدرضا شایع به این شکل جواب میثاقی رو داد؛ تو خودت مفت‌بری. دیگه‌از مفت بری حرف نزن.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50K · <a href="https://t.me/persiana_Soccer/29304" target="_blank">📅 15:01 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29303">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uwtt5QamZmeLQ1DEK2bPY8vtaiZWQssXYu14qcN7TI5rUWQFcc8ILawHA0EwQGA46OAGs9jO6IER4JIWpFrdMMO-kXw7fbJVJBacAa73phr_dUq5QFypP8281FQb5ZTSmPZ91u6auOnNEixXTEOdteIyr7IE3TH8mFOrMIonAcaX2s_QLHLiMQlTsXM_3Xj1I2zu0ohTr2fEpFraC9PiURnMwLKQ3Xl34tal12VuEl4rkcRh3ss39Tu9cXb7BD7BSznOuDorL4u9WhNLM37NXwcPoaLlST86ViD4R8MHzoRy_0W1t8znGEcz-gidwDRrjitU7_MhliX5J_TmKMED0w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🗓
دوتیم بارسلونا
🆚
رئال مادرید روز یکشنبه سوم آبان ماه ساعت 23:30 در ورزشگاه نیوکمپ اولین الکلاسیکو این فصل رو برگزار میکنند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.9K · <a href="https://t.me/persiana_Soccer/29303" target="_blank">📅 14:27 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29302">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gt3PihLNJJ_kCYmwnS49THmC9VW0BEY1EdvI2-VG09gRNRbUj3nfCipAkq4GvFaalgoTODTysRUSKp-0JYchubP0D9VXnk6jI6hKx2MsQ0Tjs3G8neYIGkaj9_IcVJRyO25r8gKYDaH7zCkzPMsDOs86n1k2VxwoTvp0qXg1AGZKnpg_o8rUfBgmbRYdu5UlIsgFoW5WUsLQ5ZtVq_h7nYATfa8HU8af201EHBLb3s_vG4AGfqX_jqTvYQT9DyLG3I4ggQyGRAuo9xyztiLF_M4QHEBrQ15hiYYHRApqIR4QuRmOreEQp_FupJH2Xg21a9J3sa0bzJwGaePcn3hkuQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
هواداران باشگاه فنرباغچه بعد از شکست این تیم مقابل تیم بشیکتاش خواستار برکناری اسماعیل کارتال از هدایت این باشگاه شدند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.2K · <a href="https://t.me/persiana_Soccer/29302" target="_blank">📅 14:08 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29301">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d011bda7dc.mp4?token=SB2uKSqyC_sffE49ZmxXcK5YjeDz68hoefXbBhukYZ1oUAqGC3HxsA3Ie2dQH2Uqg58O0XIrwWkbe3FD4t8DiJ4Pz0n57KNj-zROY7BhiCDuXgVMCPfNL6NWAdr658WxJADFyeXcKoVT-UYDScRYBPJUjxdRoTNtkiw4-GiuGuAaSnKPqnvIzoWgkxJGUB4mj8fisqwI8epvKot5bjUs_WWy46LxkH06X5rgQ_D5wTzSIvRspItI2shKxpPuN6HaciJuSFnIQ5RlZmJxceMFC45tl356TSDgNQVwJJbWpOLJA9dmGyCziu8GowY90ERM6v-l_QHizW3qeJsHgekXjA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d011bda7dc.mp4?token=SB2uKSqyC_sffE49ZmxXcK5YjeDz68hoefXbBhukYZ1oUAqGC3HxsA3Ie2dQH2Uqg58O0XIrwWkbe3FD4t8DiJ4Pz0n57KNj-zROY7BhiCDuXgVMCPfNL6NWAdr658WxJADFyeXcKoVT-UYDScRYBPJUjxdRoTNtkiw4-GiuGuAaSnKPqnvIzoWgkxJGUB4mj8fisqwI8epvKot5bjUs_WWy46LxkH06X5rgQ_D5wTzSIvRspItI2shKxpPuN6HaciJuSFnIQ5RlZmJxceMFC45tl356TSDgNQVwJJbWpOLJA9dmGyCziu8GowY90ERM6v-l_QHizW3qeJsHgekXjA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇸
🤩
خولیان‌آلوارز
🆚
بارسا؛انتقالی‌که‌بالاخره‌اتفاق خواهد افتاد؛ رسانه‌های اسپانیایی خبر از تلاش آلوارز برای راضی‌کردن مدیران‌تیم‌‌اتلتیکو برای پیوستن او به بارسا در پنجره نقل و انتقالات نیم فصل خبر میدهند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.4K · <a href="https://t.me/persiana_Soccer/29301" target="_blank">📅 13:53 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29300">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/U_o2NiDuHGoNr4h8-OG0DkxelDgAihB2wE9HCaqlBP3t6iOfQDKqBXhoeM4lg-fsxZjuPE2pnHtE1JLPGcYLCNpXt5n-svpxFS_X8eeXLnJthFK-eUoGWGAcTCUvIMBNRN2A2jlqijspcIy_jmOZe8ojPkwne-Z6qTasnB09vd5QPHPR9EMGsdfoO75QOmqhlg16H3B1yM5zr6oKjgcA6xTHPYnjmht-hq7l-h7KKywUgDuFJZjaAbcqdJu1p59JNXiWWmnfizNLfxngiPrnlJHB0ouVN6j-GUaQjnTAdf_wDTY5JfaBxqaeHPo9GbVYvwW2E92CEFhA23452z3O4A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#فوری؛‌ کارلوس‌ توز ستاره‌ سابق یووه: کریس رونالدو و لیونل مسی قبول‌کردن برای بازی خدافظی‌ در دسامبر 2026 درتیم بوکا جونیورز هم‌تیمی بشن.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.6K · <a href="https://t.me/persiana_Soccer/29300" target="_blank">📅 13:09 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29298">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/g7k2woLhkPhiuza7r8VHBDIeKv7e6O3K62N9aTsb3IcjC7nA-x9vleiQ80bKA9olR50cPwH9ax-fi8k-hjcPfJYOD3y8eYqyWFnTZFq0g-CnVHfs9qwo_YmJKHDtCPxc6VoKhxtsCAvhxwBR8axg_IB2lDpV3vk1ZGjuHKj70mFxAsX2OCxEy1T8UbU_fSbZjClpnUm4HjhNfFRX6MfmftBY8go9qL9ZJzTNg3iX7FmuBWKDa-XFEP-fmgRkMhDUU2LwXc5VYC4tnhV_1UuXB_49GAL6C4b5okb6twcAtohKodRpBkPMH0MDN8SP6GhylfP3JrzRqtCuBrxI3fJoiA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ZBTwu2S2d8Ka1i5MOWWX5dFjQo_HCt_SvMgInd9WeGvI961hr5dVyAm5eYD4vme6puGSqTZeUaFnEbtyx4KQV1jw09KtQy8h0ScDfDy4BF4Hmlra52BkHKSjdYkQgdOFYvzJYuv4JSjGZRfFTHMRqP9nMndCAycOcsLndATm9wjMjU0NJy2iisR6S9fxtjqL9mzlk4c2Z2fY-cRaaCHfNnIBmCSzpOn_UiRSSyWRkm-ucKhMei7btUlB1RmT7Z1E6b0bP_iA2fnLS-WslUc5kfqFzhtYucvixca_X32F4_K6v7Iu-1E1qbANhAg_7E6WmM-kjGl1okhIkIwO2bn5xw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">‼️
اسماعیل کارتال امشب در دیداری حیثیتی و با ستاره‌هاش دو بر یک به بشیکتاس باخت. ولاهوویچ که درجریان‌بازی بااشکرینیار مدافع فنر باغچه بارها درگیری داشت دقیقه 73 گل برتری تیمش رو زد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.4K · <a href="https://t.me/persiana_Soccer/29298" target="_blank">📅 12:41 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29297">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NI7sDv9uaf6AXxbdzQHjtU6xEcc2fiCayCy2m8RJPwBQwaV8W0l47xDvJgGYUlEiG1eAlWrqXTIhsFQ1HaVo9at52wOn8Wfib25P_KvtLk1IK8IXooO3YR256DF_b0xe_mcaxvdZm39-DPzq_H3FeMXTZvyovthCSVTk1StioEbn7k_s_coQSFkDOYFUhrQ759f8yzOshZSYZhI2TOdXXNUL8QcZMZjElndFvmOBU5khl5d1X0ufavW8L4MrFxVt87yQve45xJ7ZXpmtpCVQBn6koth2JpjRF_gTnaPnmknI9wWHpJxTqp49wAlN1V_CHGCyjlzbpiptp48BXQYN1Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛ خولیان آلوارز تمرین امروز اتلتیکو رو پیچونده و گفته دل درد دارم نمیتونم بیام تمرین اما یه‌کمپ‌دیگه‌رزرو کرده و انفرادی میخواد تمرین کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.3K · <a href="https://t.me/persiana_Soccer/29297" target="_blank">📅 12:41 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29296">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromBetegram</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pHK_J7k0T8PScy2tQEQkhAdmzY3Xo6qmXji-etQJ0gbvTKhYIxeQj0AEwOe4hACzsqqRx5KO9TGN-co-pjFICWawCdasdPqWsI4n1kqMJ_m31XshLo26Jm_27ADtdQ9_lWPFbNTSgrIhjuFq-whGVHx2dIihn0cFwRm6ripvqs5avwCBjOi5OBLqTbv9w3Ys4ySWz-fCzh5Lg_aCma2w68w2ZIARfvkoowyAz23WAFxl0QxTBKxS73ql0QG7W8Yo6QOrBcW2s311riWhOsFYnsxsl5J_mGxYkLx_wyjCxPsEkIQ6nw_ldtg0xDq_o9eZCWfj1EaRTmVU0GTwF8MeQg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇺
هفته اول لیگ قهرمانان اروپا
🇵🇹
پورتو
🆚
منچستر‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌ ‌‌سیتی
🏴󠁧󠁢󠁥󠁮󠁧󠁿
⏰
ساعت ۲۲:۳۰
🔴
بیش از ۵۰۰ نوع آپشن پیش‌بینی برای این بازی در‌‌ بتگرام
🔼
با بالاترین ضرایب پیش بینی
💵
واریز و برداشت ارزی و ریالی
❗️
🔥
۳۰۰٪ بونوس رایگان بر روی اولین واریز
❗️
💸
۱۰٪ بونوس روزانه واریز رمز ارز
❗️
🎁
فرصت را از دست ندهید! همین حالا پیش‌بینی خود را ثبت کنید و از بونوس‌های ویژهٔ Betegram بهره‌مند شوید.
🔵
http://betegram.com/affiliates?btag=3_l7</div>
<div class="tg-footer">👁️ 47.7K · <a href="https://t.me/persiana_Soccer/29296" target="_blank">📅 12:41 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29295">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cSqVRO5AJXeFsjFxowHf-8ZvfGpI5qmOQJdEXE0IurhNoUofFYK0fWarIgz-DhC109Gm-I0Ccdyho0xIJRiRyDtIPBjMTFW4KHFoa4A5NqdINdHfQKi_BxJBbqU2OL7M3eob7p2WhILZvW6V1yumnpxNXzt2A2JY6fos73QXop9wG3ac1kQWygEnUXUfc3_f5e42Hs4cSFvVDMy2Uy5HBa7VIaX249AfHp-OQeJq6fRIymz8fvfDNha1hRGogWxIcZ58_W4p_JWxHgxDddNWjEl-D31phzZrJBmA7lIDKNVXm_pbi6ApTNltbBhTsMcYkCyqF69IP3WVCFGVUaNnTw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
مقایسه عملکرد نیکو ویلیامز، کول پالمر، لامین یامال دزیره دوئه در کل دوران حرفه‌ایشون؛ یامال هر همشون کوچیک‌‌تره از لحاظ سنی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.8K · <a href="https://t.me/persiana_Soccer/29295" target="_blank">📅 11:40 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29294">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HYxkYgsy0epBzLgfZGsF6njeTwVuiz13FCpFaHH5AReggvD9N6SVzVersbRMECb-2MxOVbucaKRRbtDqzQTocytavbcgLXj8zf3jWyBe0EhtRRTcWcPdwdIsEx3fLUM6I4Fhr_Ku1FT7ZiIH5Kd19BPritc_wPO6RBpdvgn7Y10cZ_aG4cCt6d6rnePK0RjsNbqRTO8Wf1CPSX0IGN-kPyppqym1Hoov_Dy46Rri1LYc2HwRqXAsgQhV2qTukIS7ogy0YOyDY9Oji5_bdXMkN35C0xFFqYiFCg7IAD7UrNl6VSAfEgBX1LNaR2TYuU9-1OIfAWxWYtxkpxxRrshulA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇫🇷
امباپه در پاسخ به اینکه آیا باید در کار های دفاعی و پرس بهتر عمل کنه یا نه و مقایسه اش با عملکرد عثمان دمبله و رافینیا در PSG و بارسلونا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.2K · <a href="https://t.me/persiana_Soccer/29294" target="_blank">📅 10:56 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29293">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CJICD0L8J6wSYD8eqjIsX9rC7OBR77hTmrhvSDkFCJU800zhvngIYvdNgJ9bZ-tTYppK70M4zZCISL_KqOdlUjJX6urO24jXEnvbZhnHorY2qJ7ZFfID28rtxw3BokvnAIJmOMHNoFKKcExsFBd5uEhtCJLWrSCySlKdDVwMdNC12OsQZzkqmEsWtTmgSHFLJtct9lt2pjWirYsfqe_elgHBrC-b91S-zO_nVymzTPmRFZ0tdooSoLWKuDTB2c4uIC7Eo_CDchLwtyzVSWW7u_AL_jGafZchAlXkSPG_wdGTr0T0MMcYt3WOohBYVJwlWe8LUNTmUgA3JMf-dxOf7g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
منظورعادل‌ازاینیکه‌گفت خداداد یه کارایی کرده که فکر میکنه هرکاری کنه کاریش ندارند یعنی این.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 52.9K · <a href="https://t.me/persiana_Soccer/29293" target="_blank">📅 10:38 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29292">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PC5UN2d8rsBNfCsh3U8vJ58JZtbeWQ-4PMtql4sswtD-Nh5F1Wu35wZjP40gToJFtM-D51yRQBAklBCSuZOb4wi895JfI0unI2b0u4looVCrhbF_Q12DfpCSs82D6s_lGXYdl0uOKiPx5AyNtXbQX81mMsPS47dFaJe5iww8H-ljMuxSwPaB-7Kj2rR-XlbMbkfUkO3vV-G2CjW5G1bq2n-6ZM6YpgeWx6L4wsZJinOs7Zf8euWE6Pu7FB5BhDScckfM55jKnrK0CCzaCr8_YgdkWVn2x5yFeBVxnGCELJIf3i_SZNvjkHuwStyExC1gQ78UOykoZXlP22N8AhntPQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛دنیل گرا مدافع‌مجارستانی پرسپولیس به مدیریت این تیم اعلام کرده با دریافت 400 هزار دلار حاضره قراردادش رو با سرخ‌ها فسخ کنه. به احتمال فراوان بزودی گرا فسخ خواهد کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.5K · <a href="https://t.me/persiana_Soccer/29292" target="_blank">📅 10:16 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29291">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tTx4B8ODSrmnky9Ggv5AOZ85JBot6aqb1jesUm_X-VA9FcjwRkq_a5nWfXu1yDa_L1CV5WHEW1eqGQClOgQ5iE5lquS_OKdnsOT0dA3iQDjsHUyvslzbMmPqZ-oek8L8PZbesmDXYJ-mH-PjNyb-t1z5FZ5l8ioM9WDVoxNEgFGWoVVNPjhrgQ5TaYpb4if2gnqGTEhVBhEy7aACZTilNIw3Aaujxipt3YBceZyJF8LxPzCXTghrrlz-GBbreBhLfXLPcNRggi5icq556wM2R7i_l0VNg_7AMIGDVdrN8KR-zdV0shQnyNeemptO4hGUKlJuVRwuSmzOK0Ay95tXWA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇹
ترکیب‌احتمالی و پر ستاره اینترمیلان برای دیدار حساس فرداشب مقابل رئال‌مادرید در هفته اول لیگ قهرمانان اروپا؛ ساعت 22:30 از شبکه پرشیانا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.7K · <a href="https://t.me/persiana_Soccer/29291" target="_blank">📅 09:50 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29290">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JeWyQi62magop9HXKhqWjhQjc7S6t1VJTLrXbhru43YA4FOsQW0Mt_HS55V31z39FjBO1Q4OjsKeNnZp35v-jbrzHIqcOT00HmjC7vkNAkdn0RPluieH-Ea71BwyF-8lEaln3W9ru-cs0ZMahZmtIpYjRbENBWbhAHHMXus7XNQf6DXf9AAYempdiiMxzqg_COoI5g44WQa0iTBaKlT9gkEQkfr-Oym7NqtWnaVo0KumQHChc-4MzVyKy_6Pksr9R_2oyHAXS_xfZmlEQgYGuOb-OwQe3I-ri6jiORrLIYvrrVtwV3FUWY2bGk2gAuN493Cr4ip0jsl4zHkEZvrydA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇹
ترکیب‌احتمالی و پر ستاره اینترمیلان برای دیدار حساس فرداشب مقابل رئال‌مادرید در هفته اول لیگ قهرمانان اروپا؛ ساعت 22:30 از شبکه پرشیانا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.2K · <a href="https://t.me/persiana_Soccer/29290" target="_blank">📅 09:22 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29289">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">🔹
👤
ویدیو کامل ویژه برنامه جذاب امشب عادل فردوسی پور با برسی کامل اتفاقات این هفته فوتبال ایران با حضور دو ستاره جوان فوتبال ایران.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.7K · <a href="https://t.me/persiana_Soccer/29289" target="_blank">📅 01:43 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29287">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/r2dp6kDfrXW9slnNZnQIKjS5m8tQZL6WrxG_x8BPJ4K2YCvrJLlSzGQKm0-DsJIqZPneO1n6DsADrCwOidWi0G_1fLiBWBPTMqQdfWQcjN8-jXARwTpKzez7HDQ78qoj7CvyQkHpQqoaeRjaSZgh2a3Zk-3NbS5sH2OrHQ5sE_9h0MUEX3k-Yu-j6LpVWWzD4byBrFoHDXzYtONEQi4g1sxh736PXQE0u2mUGJBBb3hneVjiOO-66HAD3OpWAIaUJd98YspgZALiF2TI3UgRIXLgg_h26lf1_oUeidhCSrh-tjaDMavh0xAoeq6yjVOVkMi2JugRDZT9aazBaizEsQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌‌‌‌ دیدارها‌ی‌‌‌‌ امروز
؛ آغاز فصل جدید UCL با میزبانی کهکشانی‌های‌مادرید از تیم سابق آقای خاص!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.4K · <a href="https://t.me/persiana_Soccer/29287" target="_blank">📅 01:35 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29286">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gd_Fo-QvtQrygIBqAPv5vSpgySbLug2q0N5OD5rbga6BfMEITcuSBM05Crqf-_VdXBDFQcHVk3kkbJpx1Zm7NLth3a5_o3SB6zO0r0_zBKPHcDUkE3jp2s230s4ilZLbWijdYA3a9I7lguKPhngdyhVOSEZq0pYheyadM5Kb9nM0NjjAsFdCvFiXge9ovlVYjtbFlOD3fNwyWds-Qsbcxg_Nl1aDYIDcYhydid8Z86DMj88z_Ciyx-Y88SaouuE8MYh9rC9XUSRqDJTBh6teyBQDBVGdUp5erYkO07fSihZXRW-ra1dMCRzKwKo4kNah5roaciLpGZ5_PomrOJ0Q1g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج‌‌‌‌‌دیدارهای‌‌‌‌دیروز؛
برتری‌ارزشمند پرسپولیسی‌ ها مقابل ذوب‌آهن در پایان هفته ششم لیگ ایران
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.5K · <a href="https://t.me/persiana_Soccer/29286" target="_blank">📅 01:35 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29285">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gmeIQcgIddGlJQpY-rGY1PTj_7kTniKDMAHwpyIqzwdydYRREztvI2FbslrXeB73T3vCcFDXmJVJlJcbBz3AMeWH1QiqZuK0NkjUZxu3thYZLxf_po8IedrDzSBUndAjNqZ3ZolH8OAMD8uHHir4QGQRt-l4zp1C_utBkh8JAfd-5VdAlAOSK0qn5twZ6KD6Chbc5a99L99l9E46Z4JkZp5BH16c9MRTylvxrDHzsWaUZFP5kuxBjA_9IntJTRWfpCBYZZuh0cGB32nVtLvZ8u7EgdlAjKJne_FuxgYT5DN8zrH0w2bK5kC4GLYyIbBG536yvg2FPyxXjsYjMnOdEg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
طبق‌شنیده‌های‌رسانه‌پرشیانا؛مدیریت باشگاه پرسپولیس بزودی‌جلسه‌ای رو بانماینده دنیل گرا برای فسخ توافقی قرارداد این بازیکن برگزار خواهد کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.9K · <a href="https://t.me/persiana_Soccer/29285" target="_blank">📅 01:24 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29284">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Fv_aB5ujad8znPbVqkKdxgI9ENIzcQ-fvjU_pzU5ot8Rz5v9G83vHv450lalrPqUzPT4YZMgDAAMNtJ_fbL6WYur5WKNjzz1Tq66UbTnw6m18OqIwezHVrDswCK2F-2fmhVYzaarlOWqz-EN2c0rjHBSc4daGxTzzgQj77Ac57ajy_V33Ie35US6WI5YfOgtoOpzcmqS-C0KtF0ERw9TwxjysNp98pJo-97BlsNeqqw-XIqtdZ-tSl8tDvTxAbZ9nInS5Hh9U10SklQVMEMPDvLqVlUs_Mm90_SC6siJ0Es0nAgc9tR5Gr4PUCklmU1hki4nmJqVqUYGhLf7MwLhsw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
از پس‌فردا دیدارهای هفته هفتم لیگ‌برتر شروع میشه. تراکتور دراهواز به مصاف استقلال خوزستان خواهد رفت و آبی‌های پایتخت با پیکان بازی دارند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.5K · <a href="https://t.me/persiana_Soccer/29284" target="_blank">📅 01:11 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29283">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4c1c191903.mp4?token=UEfSX7lcfQR9Anp0HsHGiOU9uE6q11n5tMOVpWA1lDZsMrxn_4ZR1_2oOeHh6SIQsGYrsuHt-wUz_umzYS15PjAA7LWBuFufCop4EJ1sxkLUIgtSuKguuHIizs0KkloiL_5ZXsRcPC4OP9yjNq3nigdkSUdqk92fWEaH0UOlTzcKdkR2K1kN6tTBLzdSzbgeVCm3CyUNNkaHtx_g9aGZ8TXtDdbTfptDlcvFbph5raOrBusZKkuLjSDwvuRH_49l_wOWelDXQxZv4JUzt-FuGq9Y6a7NTs7WXYuX5VtVttBQyvyptKEMh0lvYFDEWXhbRh9lO0KDusyvcg1u2MrnDg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4c1c191903.mp4?token=UEfSX7lcfQR9Anp0HsHGiOU9uE6q11n5tMOVpWA1lDZsMrxn_4ZR1_2oOeHh6SIQsGYrsuHt-wUz_umzYS15PjAA7LWBuFufCop4EJ1sxkLUIgtSuKguuHIizs0KkloiL_5ZXsRcPC4OP9yjNq3nigdkSUdqk92fWEaH0UOlTzcKdkR2K1kN6tTBLzdSzbgeVCm3CyUNNkaHtx_g9aGZ8TXtDdbTfptDlcvFbph5raOrBusZKkuLjSDwvuRH_49l_wOWelDXQxZv4JUzt-FuGq9Y6a7NTs7WXYuX5VtVttBQyvyptKEMh0lvYFDEWXhbRh9lO0KDusyvcg1u2MrnDg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
این‌ویدیو رواصلا ازدست ندید؛ خنده‌های عادل وقتی عضو هیات‌مدیره‌تراکتور کلمه "بی ناموس" رو به زبان میاره عالیه. تلاش کرد سانسورش کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.3K · <a href="https://t.me/persiana_Soccer/29283" target="_blank">📅 01:11 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29281">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7672fe1ae4.mp4?token=U4FUwOfWvhtBUCHeJxZGYXGJHJ8gwflJYSwK0gWtXGFNIgSZLPh7z9Idfm2qvHWLaIO0qCHa0tXJy9Cznk_D82PVKkcbd7Nkoej8LDrvcrbJA3hQzGQTnkDAGPuv7OPk958VuZ4NZyMV8l8LowM_ZvaBCiSCFC_fMDIFZsMcT1BJiPWYJ74Fj7n8XeQzsjkzor_m_OnxIoP64Sfuv-ZJ3C7GDjZ_qLWB_8g2IhbN2_QWsauRG9SjqJQzelNICQHx7tBwOGqwg6wE9dEjZsez-PZGfdmuEgRYYF2tuyn1DupfUwhFkCX3v7LCMzOOh5PTfXeRb47pbjXD2UiSTuP6qQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7672fe1ae4.mp4?token=U4FUwOfWvhtBUCHeJxZGYXGJHJ8gwflJYSwK0gWtXGFNIgSZLPh7z9Idfm2qvHWLaIO0qCHa0tXJy9Cznk_D82PVKkcbd7Nkoej8LDrvcrbJA3hQzGQTnkDAGPuv7OPk958VuZ4NZyMV8l8LowM_ZvaBCiSCFC_fMDIFZsMcT1BJiPWYJ74Fj7n8XeQzsjkzor_m_OnxIoP64Sfuv-ZJ3C7GDjZ_qLWB_8g2IhbN2_QWsauRG9SjqJQzelNICQHx7tBwOGqwg6wE9dEjZsez-PZGfdmuEgRYYF2tuyn1DupfUwhFkCX3v7LCMzOOh5PTfXeRb47pbjXD2UiSTuP6qQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚪️
🇫🇷
کیلیان‌امباپه ستاره رئال‌مادرید:
من بهترین بازیکن دنیام؛ و با اتفاقاتی که این تابستون رقم زدم، حس میکنم امسال سال خوبیه برای بردن توپ طلا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.4K · <a href="https://t.me/persiana_Soccer/29281" target="_blank">📅 00:32 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29280">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/932bc654da.mp4?token=gsmNHobqWlvyuU9W7cV1iaN86T65eC82NbU_MES9kHW1JZIa_wJBq0vtcMh4-SaTIsYFNbfInxV6XO6uRPxjYv0TwrTRBCB2h0cGJzcz0qPpbh0jJwh-pBc-wfwUh5Ul6PVl8VMEsNddnd1OLLkdv7CEFHrCIwBtUoJTmyM0QPFGET_EieqQzcp7ozqRFPtUMFsI_r4kM3JAxUkq-mt2Qq3ghUrxW1HCLC302pMOv9DGri0SDDjG5G-pl6c75Miazbi_cr-kPKq0ey2WiaCqcVezd75kbMcuY8hFK0V5wsRgg5cNK4KjDXbUH37USrkLG5EmLYfyzEL0IN8j3_0Qkw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/932bc654da.mp4?token=gsmNHobqWlvyuU9W7cV1iaN86T65eC82NbU_MES9kHW1JZIa_wJBq0vtcMh4-SaTIsYFNbfInxV6XO6uRPxjYv0TwrTRBCB2h0cGJzcz0qPpbh0jJwh-pBc-wfwUh5Ul6PVl8VMEsNddnd1OLLkdv7CEFHrCIwBtUoJTmyM0QPFGET_EieqQzcp7ozqRFPtUMFsI_r4kM3JAxUkq-mt2Qq3ghUrxW1HCLC302pMOv9DGri0SDDjG5G-pl6c75Miazbi_cr-kPKq0ey2WiaCqcVezd75kbMcuY8hFK0V5wsRgg5cNK4KjDXbUH37USrkLG5EmLYfyzEL0IN8j3_0Qkw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
چه‌دردهایی‌که‌ بافوتبال‌فراموش‌کردیم؛ ویدیویی زیبا ببینیم از یکی از زمین‌های خاکی فوتبال ایران!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.1K · <a href="https://t.me/persiana_Soccer/29280" target="_blank">📅 00:19 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29279">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/l4POQP5oXZUR8-kWUXYptxzj3uk4p0zLLfr5zQrwop0Be8hTx5JY8P-1ukBQWNFHbHTS9idmDSASYV4-RgoHHjAsw4EEKwQXTwn-Exu3uqWY0KVpExDJH9iCWAIjE4CbP4gzIGMxn5MWusZHvd2K_VOL9OQWR1wFLDUuZJWH2oKkOfZfpHSJWGlzg-HJrfUh7xEfhYvf8fLZqJyEf3x9RByT7uDVfw_Ng9ue2CkvJEDVP3PsXRxLXgpVG9vD_4XA8dgfXnWTZWjYYg6NUKt6hlaE_6byvP-OTPO3Xrltlq8SLHDJu3ZBjhFSqPoKyxjDZT4x_OCZ48QGrwv48oTaXQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
سه نرخ بنزین در جایگاه سوخت به این شکله که در تصویر مشاهده میکنید؛ نرخ سوم که بنزین لیتری 10 هزار تومانه از 12 امشب اعمال خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.4K · <a href="https://t.me/persiana_Soccer/29279" target="_blank">📅 00:02 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29278">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HvSGh2zRP_roVvW3EGdSTpD1DMwRsD8XMgctcZzpf7aB93TRfc4HcV7rHCNjHGD5GMoOAR9Fl5U58OR0xjGz0kY224B7c_E9VlLhE55Nj_itzWuDGeQ5DGiZksLjo8Jxqf7LOCe50hmbCuzpF3AEpg54ISpxVdEI-W6Ej8zJLf7vfTlkKYal4aWPXwICBeZRSjnjTpQIcMdphx62L7sM2pztDHyDD9EMBpaigLEzLRtyZbW2p5JxAfsQAjUiQ3v-EldDAd3dS3cwy5c_opqP6EtxR4_qVnyMeorUg_zNbaMhYCGbG2O72t0Ko86bIG5zzOg-HYPp7uTeYBD_GyRFmg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇹
ترکیب‌احتمالی و پر ستاره اینترمیلان برای دیدار حساس فرداشب مقابل رئال‌مادرید در هفته اول لیگ قهرمانان اروپا؛ ساعت 22:30 از شبکه پرشیانا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55K · <a href="https://t.me/persiana_Soccer/29278" target="_blank">📅 23:56 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29277">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qEQfqonnxEcFGGjXuyphxdnqDHGCopgmYRDfXsmjKIFaFnwlnZz-KtHfl3hUKobC_FJtf0k1TDsNIPJx0GqmDP7JGyVO3AMvHse43Ps4uMnzaX3XTFXxqcCi4hxaIeSP3XbiFuTxxG1sxd6ACR9PtgwFOpYwbl15ukBJprB6RbgGqUQTg0FeTk3r-v11NJddGfAe8-jFNX-D03akAYGcSFA_TTU8rOBRukEO9Eae53d-2OQVmfzAzr4aETTuJk0JQGp6pNfun1f15PuAHmWujoXZ63kLLeMh6t3zWhnspaTuU8zJJDT5PxELkqTjfL0C5C6rCOrU-Feg5bKgTrEHsQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
وقتی‌میگن‌فوتبال‌غیرقابل‌پیش‌بینیه یعنی این؛
الهلال اینزاگی امشب با تموم ستاره های گرانقیمتش همچون مارتینلی و واتکینز اونم در خونه دو بر صفر به‌تیم نئوم باخت. حتی نتونستن به‌این‌تیم گل بزنند. نئوم تا پایان هفته ششم  دومسابقه‌باخته‌بود و چهار گلم خورده بود اما امشب کلین شیت شیرین کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.7K · <a href="https://t.me/persiana_Soccer/29277" target="_blank">📅 23:35 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29276">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c4bb9f937c.mp4?token=oZ4Qc3rRl8dUJE_b04POkCbT13E5iDGb2d161BIvgfkEDTc-LH1b1G-vcZXLDHv5ogDA2C8IRRH_ANTXG9hho-foll-4nx7aKy9dblDHpkFhmzOMVuLNr9A6sbP8hipv0OwelXC5CsvEaWvT8tsr4AvzMb6IS2XLpZyBXFpcdojZUUrUfXvJz9yQ8awJW26rEbHlYCqp7xECQZLNV4RPylbmTjXEO5iOrL3su3buqmAhEag0iovo7yYmz_jo_xGs0mRudPQJp2_BbngZ3THMcZx9aVuc9qADV_LjuIgiJ_RpZHf4nsklIqydBzpkJiZoJe-wp82wJ7kO1QTSX4tHNQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c4bb9f937c.mp4?token=oZ4Qc3rRl8dUJE_b04POkCbT13E5iDGb2d161BIvgfkEDTc-LH1b1G-vcZXLDHv5ogDA2C8IRRH_ANTXG9hho-foll-4nx7aKy9dblDHpkFhmzOMVuLNr9A6sbP8hipv0OwelXC5CsvEaWvT8tsr4AvzMb6IS2XLpZyBXFpcdojZUUrUfXvJz9yQ8awJW26rEbHlYCqp7xECQZLNV4RPylbmTjXEO5iOrL3su3buqmAhEag0iovo7yYmz_jo_xGs0mRudPQJp2_BbngZ3THMcZx9aVuc9qADV_LjuIgiJ_RpZHf4nsklIqydBzpkJiZoJe-wp82wJ7kO1QTSX4tHNQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
سخنگوی هیات‌مدیره‌باشگاه‌تراکتور در گفتگو با عادل: عالیشاه به خداداد‌نگاه‌کرده و گفته خفه شو بی ناموس. فحاشی رو بازیکن گل گهر شروع کرد!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.8K · <a href="https://t.me/persiana_Soccer/29276" target="_blank">📅 23:22 · 16 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>

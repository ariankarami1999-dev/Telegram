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
<img src="https://cdn5.telesco.pe/file/c1-UUzRPDMFrpp37Aitenah-07p7dfFkpTx1A6kUPIDn7JMtW6-bjggYRcZZXi85beImwQcNEQ1e8q76v7bf-662xcH5Q_IH2fEDp781lsSLpw6F9EUrPTj8H7xVj9fHtCE1v1S5LZCQD8Im712MoA2JZyjhRWq88mpcxG5qRY8Qf1zoQxUy1bsfbMzNkWRQG0Y-TzN4rDYsp8d0eZJS2ZBSfLY32FudILw2B4VqOrEVnHvH4J5AI7w46ENNiP63GhiN8VLUKCQ-x2xg1LUsWAL7zo4au_PF2GVaeh3sV4taxUZpFpJRrHQWC7U1Dk496tLjxxhSJUQMNPOM_EJ8sA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 جام جهانی 2026 | فوتبال 180</h1>
<p>@Futball180TV • 👥 546K عضو</p>
<a href="https://t.me/Futball180TV" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 In the name of God; The only popular sports channel on Telegram: All for Iran...🖤We respect the copyright laws and follow the laws, Mr.@Durov...🙏🌹Contact ads:@TivaAds</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-30 21:20:10</div>
<hr>

<div class="tg-post" id="msg-101489">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/II4kIKQvIPvvlbbnN-r67njtU2yH2RB-vVHvFXMqzpxw5RbXdwDghDXZWj3yxlkKIOqXkPA7lgfCQJ1AQ2SMinYt3sFjlY8zOjmSwQN-QqvbPuECcIKi_fSP_cr0vGmpVk5xFWKWeqnJKAj9ZX7J4GiwS19kzFtgI0SkK7utN0s_XBiAemg6X5BNqR7qFNaBiMMNbZEAL-jwd1uXKLrG6DU0ElVMkWVJRa5oZqwd6uYAB-MJQ_fwked7t-ljqUq2zgj-J4sMloGkJhX80lpY6xPp52RuIgAa40OzqgCV2Hm-DpyUoBlN2xnKljwThLcQoJ8DNr7UzfTL43Hqt4VCwg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شات جدید وینی با چونه جدیدش.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 1.53K · <a href="https://t.me/Futball180TV/101489" target="_blank">📅 21:17 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101487">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pEhFpFCZLQOOKX0MdYBezieU3pSbCMS9f_4XM5OBW9BPejh43OVqzjgBSHif0z4FPIk7PbPw_-Z4ftwvnsYXAT7LidybZ0TgZjXLqjCF_Me0Y0J10j-2gvBv9XAnKpl8FXbVQxXwnr0_yWHFADCfw5q4SF0ZQAhM41FlPNI4S89yRT99JSPdP-bwQrcAEn2EQHZe6Wk9XA8aa5RoPKHVIqbHahEDMevp2BFmHUV-O3gLbGrVKuT_C_OUiQQTxlgSxDD_mYVsHi4QopfA7EIl5oDKMfVdNDUekwwZ5Ng-8JX4dA1pALjIxY_PsJzaNop0irHMK_jaemdMkCu99k83YA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
بهترین گلزنان فصل 2025/26 در میان باشگاه‌ها و تیم‌های ملی در پنج لیگ برتر.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 3.66K · <a href="https://t.me/Futball180TV/101487" target="_blank">📅 21:01 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101486">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CjUMoFYzeTuFZ7b_PQWwza-vI4Hnis15MwOrrCeRGWBGfm5g9jawDYaNIaYlaF5J2nu1X--YoHlGxGodZ7Aw1oRd-ccm-7gGaaYA0R8rHM9juLB2rqKZNQNu4ZVfGracRkaefdbrPCIOzD-9lRMNIZPXtfz9IlwmoFMHE_n8fO7r76dum8y6-9ol1AQr2rOtdzO-q4s3EAVNjCP7aJCiTqrzvEBqPJYxiYgKToKCQzqAwg8j8_MaCqscPzPoIuu0XjHhEPZl3MsQZKqTj2gBSWG_aqmexjssAhj0ipSFaw0Hv97vRKR3BHv8ILz0wrNRBxCl5UitMuZVxCw07Z8FMA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
رادیو کاتالونیا:
🔵
🔺
🔻
لاپورت جدیدترین بازیکنی است که خود را به بارسلونا پیشنهاد داده است. عوامل مربوط به بازیکن با لاپورتا در دالاس ملاقات کردند و ایده حضور در بارسلونا را مطرح کردند.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 3.66K · <a href="https://t.me/Futball180TV/101486" target="_blank">📅 21:00 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101484">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/duvjz3_WyE6LyJ-uaQFPvNHvO1RbBv3RaNMBAk909MDBoaCmqlgrrbWSPQ-MhsfHHnMxIMkpkZrkP_522geXQVGulnpnvpL7ASbto-cEV5XIuer0saOgAxG0nZDWncN108fGPjuoY9a7_iGSuWgp3UCGg2pzHTKRyt-OjEsRN7DDb0Jk6MA6h8pACI0JWdEK42WXfntx91cBb54foWOhL7ctomOCRpiI5NHIEoUdO0YEc3zeyFK9k64LJZzmFdkle1z8xdAkq931qU-EsXmGayeIRlW8fY-k7IUV9rjPpkMFDKrh2Y1s1pOA5Nkbdj1oLiy5Cc02oHxR492KJ3pDWw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/oYteRxsCKP-aCCrHDmqfiKarcLulxm8anXv-xZtrqJFUWhp6R4gsMcKRbS_EgabiJoDt5BWGf21Ga4U3hRyHbxngCpMIkapvvpzboSv2YB7FRzxcFWTx1msVHFsPLqA8WQax4J_lJsONPgk7VISID1beHe-H2LejdZA2L6asOzfCXxrtDljdm2zgAjHiVzKqSH1zrFTPEPgnDnSRpCDXkkhU-WsEALEORupGc5pSMlEgfFAKNl9ycncrA8jro8oSX-Q7RrlE6rTbd6QVdAlnXcAzgPNgbmel5WTJ6mtEJgEFUl3hNGtTVnT4uAAnpplIFpZDyJd543__HiX8RLaI7Q.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">😁
زیر بغل شکیرا از آینده‌مون تو ایران روشن‌تره.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 6.11K · <a href="https://t.me/Futball180TV/101484" target="_blank">📅 20:53 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101483">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WebFrH-oYJ4ZY2rbwJgT59g1cZfXdaLg_xJFazj5jCdtzSxM6AcdLEY-9nzt9IyT-xIvSKLr_hqtNH_avQ4rEUuUgA2Hdnr4POCWcUSdlK3ELZwCMBZohHmKRbtbWf5k24-Qf1p7z9uvnhytfInCaf70Muh61MpVlVhHCHnU3VcraKim4vD3Ze4OQ7d2clDdqh9_DUbrCFbHKGRkKhbq7pux7LynOsFlfPyDn8nnviSeXCqSPUVjdd8K4qH42zzocRXstr8sEKc2pwGEiIaqNcR1E_syorii5a2drHj86-_cPrTTwQEqZmKqrKdkHxVpAG8qs84r7URrzmDS9cnf7w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🔴
فوری از فابریزیو رومانو:
🔻
لوکا مودریچ قراردادشو یک فصل دیگه با میلان تمدید کرد.
𝙃𝙀𝙍𝙀 𝙒𝙀 𝙂𝙊!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 6.72K · <a href="https://t.me/Futball180TV/101483" target="_blank">📅 20:48 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101482">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oMPYEotr22u0ypxw143waU9IUAxJrWpBQ5qC5spBgQgxxqepvpC5jiPuRK0XqRIF5qftmFKHO8cDjEkoNIxBMtqCrsyAsfFYqD3eGDt7JQJavMW-D7qpkNOZu06wM8Vr04khwkLXsYq1CbCyXM1a94kjZI1m6JTrz10yxwDCNyd96mw61xKRr3Lbgr0iveHypWvfYXlT_vOaxAP29_zwDYqBVGpEadYMDsA5yrZ7bB6Bi4CeTdB2d6epbJu2du3jx-VGBLgelGJZVP0DP_WvyCJdAnKl_F74Hn0QeS6F5-kIF8cHq0OJiazkschKfom2neOGKKj_zAS3gyo9anorBQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏆
||
بازیکنان جوان با بیشترین تعداد دریبل‌ موفق در تاریخ جام جهانی:
◉ 27 - لامینه یامال (2026)
👑
◎ 22 -
کیلیان امباپه (2018)
◎ 19 - جمال موسیالا (2022)
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 7.32K · <a href="https://t.me/Futball180TV/101482" target="_blank">📅 20:41 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101481">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/it1XcWBp1cb0IyLBAZKqjmL8P-LQYcn5XNdeGV80SBXwynH62tTz_WGKrtNcgYNUmgNtXl7IC5hk_ittmOoH4Gs7LUSJHBKtS7BboK-0heRtvgbFvQMTZ6I1cSt7Yb3D2wC7uhJri3siW7YqVQJVchPJif01uOpcTWYwyQfc_0IUhPfj9vs1OS368JrA1TSABYJf4eV8AsxvEUUVzfwWYAa-wBkQncYzXYyv3IBa4SLGQKZyRxHfWRGzQvkDKfw_AFJe_JTPKS_LR2kbo_9u-ytmPFQgaNO6K6ovdF5Qzdn2nyLoRvzS8wyBDX8evkKliGYEwmqT4UjcRe3NvNbQBQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کیلیان امباپه کاور EA FC27
نوجوان و جوان ایرانی باید ۱۱۰ تا دلار ۱۹۰هزارتومنی برای خرید این بازی خرج کنه. تازه اگه فقط بخواد آفلاین بازیش کنه.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 7.32K · <a href="https://t.me/Futball180TV/101481" target="_blank">📅 20:39 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101480">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jFdSzR5A90hHtl0-bZgPMkC1cdnovCyH-5kc3hxM_FwzrR46yGT72Ws6L7yBqyoTVxmIUvYIC4WnrPF45m7rX9c-_UwlplSP1v_GinolZbKj0DWmCgF4sG0L27GsR9AjObW6I5RRJWsygdxlCpe3OrptJ4c4ppopCGRtsjWzDK1zjFawlX9zu7cLzhEFY9pkv2VtJLtMgxX_0KMaojohXrn8Iq3wBrLVk3iqPkTrzNAHpukBWNfpqU1LroK7O-0gzkP0zg27LOhMjYTs_2mtqNWVIHZ42RTiFvzv-Y5TMSsFwPlewllKu_5wyT7Qmy3zM-fmmJY7ot9xJzeEip6_Cg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🚨
گلوبو برزیل
🇧🇷
:
🇧🇷
• نیمار تا ماه دسامبر در باشگاه سانتوس باقی خواهد ماند تا قرارداد خود را به پایان برساند.
‏• در پایان سال، یا به یک باشگاه جدید خواهد پیوست (اگر پیشنهادی دریافت کند) یا ممکن است از فوتبال کناره‌گیری کند.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 8.54K · <a href="https://t.me/Futball180TV/101480" target="_blank">📅 20:27 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101479">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/33ffcc2a6a.mp4?token=aXC-dCy7iU7miIEiPF9dkGRQVTCW1UNAnQAlxNgOU0W0peGmfrjrn8rov-1bcyduw7BwyB-DX9tJTZDwDuigCwwjKxcZcR4dEv1Max7V0TMCJJibMZKjdEz3Des2c3O7oZ_WGxNrOn7n9hmnWyghv50touS84-Sf1r3cHUDJZYSq2-PBoIQSDr1RtoNwqp_pONU-nHp8S7wHLaRQbhLk2QwsBral3ZD_1A2To-o3Hi5whxXu7Dp-S3udVWlD8RtdAH2bbmslQXf356vI_8Q0Z0g9y8VKwOn1zl2F0thZXkxCtQyEHacbA4Y4ph-Q_Cye8hbDP5papOzt-msxxS29LA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/33ffcc2a6a.mp4?token=aXC-dCy7iU7miIEiPF9dkGRQVTCW1UNAnQAlxNgOU0W0peGmfrjrn8rov-1bcyduw7BwyB-DX9tJTZDwDuigCwwjKxcZcR4dEv1Max7V0TMCJJibMZKjdEz3Des2c3O7oZ_WGxNrOn7n9hmnWyghv50touS84-Sf1r3cHUDJZYSq2-PBoIQSDr1RtoNwqp_pONU-nHp8S7wHLaRQbhLk2QwsBral3ZD_1A2To-o3Hi5whxXu7Dp-S3udVWlD8RtdAH2bbmslQXf356vI_8Q0Z0g9y8VKwOn1zl2F0thZXkxCtQyEHacbA4Y4ph-Q_Cye8hbDP5papOzt-msxxS29LA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🤣
شیرین‌کاری لامین‌یامال در جشن دیشب اسپانیا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.15K · <a href="https://t.me/Futball180TV/101479" target="_blank">📅 20:20 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101477">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ba1111b268.mp4?token=MPv5J6X7cqnX29PGW08xG36MqrwX7tDr-Ze5Ce_sg67ceTqx5xAijK8WV8RegUX_VKbiolglB4G5WwrFO0TX8iHnwJ2krXZiBN8ucYU_mrBZLfr9qJw-rPXkBujZ6Ucr3pdfzjb5PIorTHpLohT1T823RpsWCnPUZ_wguTUzsI3ZOcaEOQOybjrkwF2FJXdJE1px7Cxr4SQ4E4rubRYfVwEnLkmxl0oEJwm-wrO0CmjhpTFk8TKBvCHNqn5ybFAmpLUhbnNHbQk84PGoflfSQuzkojcnvZCj1_sbjlISSmak6pdmBwIG8IFNqDt75WH-3x5JXt_fxUTFQvccwOaE3w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ba1111b268.mp4?token=MPv5J6X7cqnX29PGW08xG36MqrwX7tDr-Ze5Ce_sg67ceTqx5xAijK8WV8RegUX_VKbiolglB4G5WwrFO0TX8iHnwJ2krXZiBN8ucYU_mrBZLfr9qJw-rPXkBujZ6Ucr3pdfzjb5PIorTHpLohT1T823RpsWCnPUZ_wguTUzsI3ZOcaEOQOybjrkwF2FJXdJE1px7Cxr4SQ4E4rubRYfVwEnLkmxl0oEJwm-wrO0CmjhpTFk8TKBvCHNqn5ybFAmpLUhbnNHbQk84PGoflfSQuzkojcnvZCj1_sbjlISSmak6pdmBwIG8IFNqDt75WH-3x5JXt_fxUTFQvccwOaE3w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
تایید دریافت پاداش میلیاردی از سوی قلعه‌نویی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/Futball180TV/101477" target="_blank">📅 20:01 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101476">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VgBAhKjzdk3l1JHce5eUaI0UFzqOo00tDAAtciGWHA7lWztdBJbKQxfpjkhwTPKd_gyS7i0qaQXvXOf-c04BiLrLuhEqnTndcKW2qgk3iIx01n7RZMgrN8e90eJG_Cik3q6s0UKsZ1lokrdqjC7rLGy4p04Qu7NlE03PXz_SvaMJguZkq_mm6Ui-n6CMQW5E0iCXJdqbEQ2pJ1xw4ZFHtNwgTZi0c7knL8tsDbF61Y7gBM4wZQIOUNZwD4ACKgJjW92W8Pfh7HXJOfMaufJP865grMqYKK3IkyZvgjHVfnBVpMBefnI8IwWa7rJPa7wQg0VfJDYMGEKBzWrQED-Hxw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
بازی های پیش فصل چلسی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/Futball180TV/101476" target="_blank">📅 19:48 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101475">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/04bcfb9b29.mp4?token=mn0FRZ6PmHsDv82ul5AP0tJ8NTXCPFkXrc9oZvVtgrpYnCbroM1iRe1MxHL67d02I-EJtBrxIYAIhcuYycqKfrSJLW_fLjmQeObsxYBOonXSCX-ZI4tbuYy8xb2egD3JOMAk0tVtpMaawZqcM1copcOVXUS-GIc_dgGSHOlfi7-IMP0BkzmbvsEqFtYqCMMRIbmAOFLk1XFyvZpShFkXgnkF096WVYKO534AWGIa6WPYaI7Calzh6cXSmws7xZIYQG4r02jmSMYp5dxVZyQCK4IkJK8nA2q_M3rS49Ec_uCHFjkm4P2GhvT7nwAeKuUwly9mPZ8zZwpPVegf2b9AmA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/04bcfb9b29.mp4?token=mn0FRZ6PmHsDv82ul5AP0tJ8NTXCPFkXrc9oZvVtgrpYnCbroM1iRe1MxHL67d02I-EJtBrxIYAIhcuYycqKfrSJLW_fLjmQeObsxYBOonXSCX-ZI4tbuYy8xb2egD3JOMAk0tVtpMaawZqcM1copcOVXUS-GIc_dgGSHOlfi7-IMP0BkzmbvsEqFtYqCMMRIbmAOFLk1XFyvZpShFkXgnkF096WVYKO534AWGIa6WPYaI7Calzh6cXSmws7xZIYQG4r02jmSMYp5dxVZyQCK4IkJK8nA2q_M3rS49Ec_uCHFjkm4P2GhvT7nwAeKuUwly9mPZ8zZwpPVegf2b9AmA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گفتم قبلا یه جایی دیده بودمش‌ها!
🤣
🤣
🤣
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/Futball180TV/101475" target="_blank">📅 19:38 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101474">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">🅰️
🅰️
🅰️
🅰️
🅰️
🅰️
🎰
لذت بازی در کازینو و کازینو زنده با 30% کش بک بدون محدودیت سقف
💥
تسویه سریع و آنی جوایز شما
💯
اسلات‌های داغ و جذاب از برترین برندها
📱
اپلیکیشن اختصاصی با سرعت بی‌نظیر
🎊
وقتشه با کازینو یک بت، برنده‌ی بزرگ بعدی باشید!
1️⃣
لینک بدون فیلتر
1️⃣
ورود به سایت با فیلترشکن
••••••••••••••••••••••••••••••••••
💠
لینک اخبار و هدایای سایت
👇
👇
🔸
https://t.me/+ioIBrQfqMLtmMmEy</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/Futball180TV/101474" target="_blank">📅 19:38 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101473">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/G_1XW61mLLOUWRSWfRaR-SlOmAhMu7Eado_h8paXapd7vcEz537gG9Ir84Q9ujxnrjd0UEOwqfhf21mJx71QXXP1dAXPaGW1m1pTuJopW44AYZuXPhgl-tbzhjvlZg99GG6xwvmJegSb2tCCReDE4WocdCpTPGOc2O7d4y4PCHw9SGmTYhxwC7eM9nMlztl9AD4KlEIGiLYjFgUqRuAe0eQ1y5UqjpDpPYBgt5xBeeAop2W4cnd12GDUK7mjxTjDs4Al1rH7c28hAF8ktxf7vMI6hTAGC3eZckLjgouj1l0RNhcC4aEfk3Xiqyeo6Q-b-9rqM0Z5NvyHwTf6bOatew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💎
سایت پیشبینی
YekBet
💎
🌟
کازینو آنلاین، دنیای هیجان و برد
🌟
🎁
100% بونوس خوش‌آمدگویی به مناسبت اولین واریز
تا سقف 100 میلیون ریال
1️⃣
لینک بدون فیلتر
1️⃣
ورود به سایت با فیلترشکن
📲
@yekbet</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/Futball180TV/101473" target="_blank">📅 19:38 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101472">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d0fe520f72.mp4?token=i90N-d2zlHotlEG5IBb621GKVL4-ScLHmaqIp4M2a56PA-Na_Fy_NTpIX7FlMRxy4NrDcnlWKriIzl-LM8GJzTnR4N-dhzkcZor4JTZzdhK6fF2dgs04gSae0aw2rvYOXjYWyaqBCFTzcC3W8bU0awLX6ecQonkt6IUxPXQY4Ck5NVQ4oYZll41K6H0Df5hrp4YslwTTSQXtfa3FuNs-yBmhFOEJRF45M27eQplqwczEyaAXU-7DMPYnlnmhMKHIiuOR9QTLkbGef-KH6oWQqZCbb3Q5ChxplRpRO36XLKJUmVBHnSZ4SSCxYrew4mDkI7lCnU4iRk2x6Lg6-sFb4g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d0fe520f72.mp4?token=i90N-d2zlHotlEG5IBb621GKVL4-ScLHmaqIp4M2a56PA-Na_Fy_NTpIX7FlMRxy4NrDcnlWKriIzl-LM8GJzTnR4N-dhzkcZor4JTZzdhK6fF2dgs04gSae0aw2rvYOXjYWyaqBCFTzcC3W8bU0awLX6ecQonkt6IUxPXQY4Ck5NVQ4oYZll41K6H0Df5hrp4YslwTTSQXtfa3FuNs-yBmhFOEJRF45M27eQplqwczEyaAXU-7DMPYnlnmhMKHIiuOR9QTLkbGef-KH6oWQqZCbb3Q5ChxplRpRO36XLKJUmVBHnSZ4SSCxYrew4mDkI7lCnU4iRk2x6Lg6-sFb4g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👀
👍
حمایت رودری از فران تورس در جشن قهرمانی تیم ملی اسپانیا: "شاید بازیکنی که بارها و بارها، ناعادلانه ازش انتقاد شد، ولی امروز... امروز بخشی از تاریخ فوتبال اسپانیاست!"
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/Futball180TV/101472" target="_blank">📅 19:20 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101471">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/74d5cadcb4.mp4?token=IH9bXX4uz-pcJRhNbVMplZCg4VMcrGf_qpxvOs6saOMuU1eTjWb14sXdb__aJNGcaDu7cZxIWkVBvi26WWgIsuJTkEHvHKtOgqEKXyJxg2mT-8H2ZQW_HWeEUBxELM3m_W2Hi-Q_gv20sN0gDC7UIeBsPXcE3CN6r7GZGisshErsS3Cs7PNu4TDy5uQe_b1CRcwMiQLTWnbfwdAyFrzSHMx4D_xTMzO6_epNTYfs6-FT0MXmxFhzUNE3JxP5qpuWBAk3TP6XowaH3ehEe5Eez7UaTS4LXgPjlSALDJ2hbmmehT0TpZJqyCWelmC34SX1NlkWFgGnoQuxjUgAXCaNtA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/74d5cadcb4.mp4?token=IH9bXX4uz-pcJRhNbVMplZCg4VMcrGf_qpxvOs6saOMuU1eTjWb14sXdb__aJNGcaDu7cZxIWkVBvi26WWgIsuJTkEHvHKtOgqEKXyJxg2mT-8H2ZQW_HWeEUBxELM3m_W2Hi-Q_gv20sN0gDC7UIeBsPXcE3CN6r7GZGisshErsS3Cs7PNu4TDy5uQe_b1CRcwMiQLTWnbfwdAyFrzSHMx4D_xTMzO6_epNTYfs6-FT0MXmxFhzUNE3JxP5qpuWBAk3TP6XowaH3ehEe5Eez7UaTS4LXgPjlSALDJ2hbmmehT0TpZJqyCWelmC34SX1NlkWFgGnoQuxjUgAXCaNtA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👀
💥
امباپه و اکسپوزیتو در میامی آمریکا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/Futball180TV/101471" target="_blank">📅 19:03 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101470">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/f1SJEK-AL9M5e3moAli5pPv9aCb8ceVu3LAmOCRP4_iUmlnOU3LODgZ0EeQpoWNtdSuVCJG4siuTuQ7HBTnoIn-Hzwp5_xpxqnxIhw8CasVSr4uo4QoFm96jvBqSWPbfY3650dbKQYnTS8nu3Bn4wSaYl0Ru-MJUyvozEKMfleBEnhrzZ5elgc0tL6UuDCJXXb16W92vSJSE1SF8WaMwPtQ3vthAKZPeakyUhFssgzF-lzuXQADE_MIgXoxiZqKVEVC57Os5Y1_6prN2AXSAHNpwayki25e93QGB1aZ3dmEeERRme_3EwQ3Qlq1pFPPbvYoOZuVeN8lS6nyUdMBq5A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اولیسه حدود دو سال پیش با دختری به اسم فاطمه وارد رابطه شد، اما بعد از جدایی، فاطمه باردار شد. اولیسه اول پدر بودنش رو رد کرد، اما بعد از تست DNA مشخص شد بچه متعلق به اونه. با این حال، گفته میشه هنوز مسئولیت پدری رو نپذیرفته و فقط از طریق وکیلش پرداخت نفقه رو قبول کرده. فاطمه هم پیگیر حق و حقوق خودشه و این ماجرا باعث موجی از انتقادها علیه اولیسه شده؛ تا جایی که کامنت‌های صفحش رو بسته.
👀
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/Futball180TV/101470" target="_blank">📅 18:56 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101469">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b8a52816cf.mp4?token=Zp15kol6Asidzxm6N5-w2zbS2POil1FnT2fZyebRGEvgIFRSU_kdafvOwrl5xbqkEdtVxZdWryR_-1N0JIRaqiioFZqWKmJOdqKu2t43CPWiubsUC2nuf6MHZahgEzziPAOodj5If1IpB7RUQOaiX6sXhtYuubQJnVbZ72HhS1XxgbTVprtAROdwTCRaOIJsiEsrmPN3afICyiXklpuojKeYz6KQVCv6dLrcg8Z0SHMQOy14Dag9gzEjDkyVJEkbSvZLbZxANkK9q9QwCyZP2NtgVHTlMGvPgrO8_QgcV75gO6FkpUlWIVvdA3yaIgI0on8RNmnTtPOtYnFmJbbYlw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b8a52816cf.mp4?token=Zp15kol6Asidzxm6N5-w2zbS2POil1FnT2fZyebRGEvgIFRSU_kdafvOwrl5xbqkEdtVxZdWryR_-1N0JIRaqiioFZqWKmJOdqKu2t43CPWiubsUC2nuf6MHZahgEzziPAOodj5If1IpB7RUQOaiX6sXhtYuubQJnVbZ72HhS1XxgbTVprtAROdwTCRaOIJsiEsrmPN3afICyiXklpuojKeYz6KQVCv6dLrcg8Z0SHMQOy14Dag9gzEjDkyVJEkbSvZLbZxANkK9q9QwCyZP2NtgVHTlMGvPgrO8_QgcV75gO6FkpUlWIVvdA3yaIgI0on8RNmnTtPOtYnFmJbbYlw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
کنایه‌ریز دیشب رضا جاودانی و عادل فردوسی‌پور به محمدحسین میثاقی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/Futball180TV/101469" target="_blank">📅 18:40 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101468">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/k3BeFVtf-s7bfqxMNtE0CtVx2sZ0-b5I4Uvk2Ikd8zznP4N2zbdxoAzxI3gEr0hlDaXecc2M8HN8Q5HvOf6B3c3uceWU7gpROKtUfePWqVZGUBuTZVY4jP9YK8V7lh_FDc9mtJLgTb9xkf5Hzd6QehXEVyx_ai8YsfLMiod3kPrKKt4G1EShENSAnKs9nJ7XyuQNAnWVfoUhZxmA9EAXwSLAXNU_B9SN4hzZlILe3Tbiw923ongD877o74xwKzWZSlQs97BPbdKElRUrTlWgWb4ipOuWAnutjvBWmVGTaCKAfuuwyoHfGtU_yiDQh8HfKTGxDmisjR4YPPVgXcDumg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کیلیان امباپه روی جلد FIFA 2027
🔥
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/Futball180TV/101468" target="_blank">📅 18:36 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101467">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Pk0L2h2lbKy9HVFpv4hLP0GD3I_upzTfFoHr0x6AFmQlwL31m6TVIKjY7LHuSj-2jJqkXxP1CXedOpnTHIj-Puasnz5AN6sMIDbiROCndtKYJCvRw7JGpkGB3nO5F0rb2zXjnGiqFD_19EKBup-uXwfSQ6TxRH5BINIyPbakyCLHOiXe1J5GIygxFELWJbpH7bPgBf5hjUlWbqlN4eEE19Vcc3W5sgh8e2Z_R3x-y7p1ynk6avpTZdrL7fa1CHlM9E9Gs7Or2nfZKzvV_vPSAn7hLx5rVe5H2U9s-89_X-JnzvPbbh7Hy5vpTWDIk4JGDyzOgnruFUufDWZfFGBkDQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
آنتونی تیلور، داور انگلیسی بازنشستگی خود را از داوری اعلام کرد.‌‌
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/Futball180TV/101467" target="_blank">📅 18:33 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101466">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mhpWQxbCdqsUPqed0prjxvaGc8jNZoDPLpCDC1BMuHq1UNkOb5eeDvxP9RnckeWQhE7UOdIiY6eWPaPPi1sv45fOXO7g57xRoFHW-uarkQzEQLnBq5-RCqg6IP7gA-KwbLg0BIR089qbClux1IDOXsL7zV2EFoIUs3odytac0XnGOJvKOobzGCShwezxnTYscMI1zWdCYg4Mbg9A7pouHUbU9dV2PEpXCRVsfs_0YcKSq-QRF-0f2lEDs8N-DMUgk8jrXD13snj4Zvv2K_GBim4as-Gp1ZbHkM4GzRwxelQiDPTujuO-i6mD6r5gTl_wAY3BFEePlK8dWlu1WXB1iA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
ماتئو مورتو:
الهلال در شرف تکمیل قرارداد سامرویل است.
الهلال معتقد است که پیشنهاد بی نظیری ارائه کرده است و امیدوار است در ساعات آینده همه چیز را به پایان برساند.‌‌
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/Futball180TV/101466" target="_blank">📅 18:32 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101465">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kw6d0w71nAk9EwNt9MAFkRjHGoUvD0j4aWdCW7zU3NTC4gNh-Ed8GBe_BsYPNRUgRPd0RnUCz_TV9C3nEK6Y1T9o2NTpiINAZWP5iHCACAKpxHP-naVLpm4Y_xlggb35CupEHIuKxBtmQmvWWieN_Y--GfQXGqKVzAqjON5nRJDlyvxs8M9J1JzMjrHkJvjwkiW6m7uKXX8_wbRtNskF_fPa-nHK_n2RV2A5_N3j9c6RQ8rt2WQxWKdBiNF4HPzzF2cKzd0jIsdX5KJMD1qB1PBoRmtH3D454tL6PVwm6A48MWAPKIDLdygeIixcuVE9aTIE4nxbqVVhzzT0tRgSSw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔥
📊
تیم‌قلعه‌نویی پس از درخشش در جام‌جهانی با دو رتبه سقوط در جایگاه ۲۲ جهان و دوم آسیا قرار گرفت
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/Futball180TV/101465" target="_blank">📅 18:18 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101464">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f21557090e.mp4?token=BAAc91it5rXzN1vYTc8NkcfPgF8I332CbhKiSpjyU1cC3hTh2-YYRZRZAbpxzlC6F7GgTHU8cbp8njG6M7TuZBiMT5wbCjSlg8KCW1jDvQDoDd6PDfm2Uvb7lnEPBU37EJU_4B10-gmFeOBuq6plmk-HcRxtoB68l3Tub6g2LrrsX6txvXiWMYwIyTQuDJlJUiLqH5Zh-i4Mced8fcITfiZZzRIKQvpJug_elQIlzzzsEB3MHxdLKsCdZXGSlo-2dYuKKt1sS-1Im_fFTpIocjebaRY0JGY6_FJzKNDzlLu4ZX10z0bkDtRV3GkcK7y3f_74uj5EVbMCZw1zmbBRXg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f21557090e.mp4?token=BAAc91it5rXzN1vYTc8NkcfPgF8I332CbhKiSpjyU1cC3hTh2-YYRZRZAbpxzlC6F7GgTHU8cbp8njG6M7TuZBiMT5wbCjSlg8KCW1jDvQDoDd6PDfm2Uvb7lnEPBU37EJU_4B10-gmFeOBuq6plmk-HcRxtoB68l3Tub6g2LrrsX6txvXiWMYwIyTQuDJlJUiLqH5Zh-i4Mced8fcITfiZZzRIKQvpJug_elQIlzzzsEB3MHxdLKsCdZXGSlo-2dYuKKt1sS-1Im_fFTpIocjebaRY0JGY6_FJzKNDzlLu4ZX10z0bkDtRV3GkcK7y3f_74uj5EVbMCZw1zmbBRXg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پشماممممم چه حرفایی علیه مسی و آرژانتین میگن
😐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/Futball180TV/101464" target="_blank">📅 18:05 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101463">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">😢
تمامی سفرهای استاد اینفانتینو در جام‌جهانی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/Futball180TV/101463" target="_blank">📅 17:40 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101462">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/u4ba1VhD2iGzdlO0CD2YXypc_nsdiiCJkbqjPBecIb8SqS7tOpEuJPTnp3wgX65BSqQ27s6tfe5i6GOlNniG0pCuVgegRWvWV3pfzXTqiEgU66ULRTSSCh9j6uowFPlbmGJj0c3f0KyVDcvhqzQP2VQjmmfLoEK-ZOjbBPHQYK-790a745viBQXxwiqjol6PiL6pGtGfPVRx4pODBUd8O-fQjJPdBae-Q07nfe60mxdJLF5Cbn4yHs5dAIxZVHngWSL9c14UTsYw6GFOcJEanoekqeD06oy4iQXs1IfQ2ButBirZhuJX8T3zFPB9Orheo9_ch0wf2Me4bd1OsPDhRQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
🏴󠁧󠁢󠁥󠁮󠁧󠁿
رومانو: استون‌ویلا با ارائه پیشنهادی به چلسی خواستار جذب قرضی گارناچو با گزینه خرید در آینده شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/Futball180TV/101462" target="_blank">📅 17:35 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101460">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/W-KWVnA2YIXGLDdul_ADCdunqTzLBt9jB3D0TxtkkTMD_UPRLSPSWkhwCRY_yhOhMLlnnntw_qG-IZJQBzUFFucZzVSzaFDqVk65P3v4RX9rwZxzBm0PK3RnPgO74nZRRY7l8cGCG0N4r2p-Nm7fOq0d3jLn-Tl9bijbJsqx7vHsu0B-0v_wRQSkTvxH3b2Jw3eFJvtQy03jR7rH35W4F0JLERajZsyni65AWSFR9X8-54ju3xzX-utwGHZUIAgEL9a1yJnWKxoTWDxqvENlAwEjf5tPYonsgZjDwp8k7wpDHrNgrRtcQCjM9UBanlX9k3PoYgWJfV83TiBsWXCq4g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/cJXjEuvfUFYWQIHhVj8Ev5JHBDfNBboq88zrHouifXYhGtT-qvZMVUtzmLPIgBMcVx0Off45NJGfsUQ3bKgK0KT40E5UmT_UfqKquOoWSBp2zTw-gplGoeCb1KlF8-W6lNd-wdCeK9UxbOgrUVG3wkCZTvXiQeIk0BUV1HJCyt284yd8DY4NErdz3R7k3dkIjmQIwwcf7xsMOeu88XrPEIpasN6GRmBumblO7R3GZRCV-Iv8R5EUWcChgl9R7kiAdxclbHYf68yOxSW-0Zcvqe4OaPHYkm0ZlP9bmpWE2Lv8LMlkhkpWcDdN7uIU4hp5H9HZj0RqhyMzOFXJ2nrgeg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">‼️
تصور کن ۵ سال کنار یه نفر زندگی کردی و خاطره ساختی، برای آینده‌تون نقشه کشیدی. بعد یه فوتبالیست با ۵۰ میلیون فالوئر، شهرت جهانی و حساب بانکی چندصد میلیون دلاری وارد زندگیتون میشه. فقط دو هفته طول میکشه تا اسمت از روی صفحه چتش حذف بشه و جای تو رو یه نفر دیگه بگیره. چند ماه بعد، تو از پشت تلویزیون داری جام جهانی رو میبینی و اون، کنار همون ستاره، تو جام جهانی از کنار زمین لبخند میزنه. اونجاست که میفهمی پول واقعا همه چیزه..
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/Futball180TV/101460" target="_blank">📅 17:30 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101459">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/523aa1e339.mp4?token=Dhy_QojMM-bbyXnz4qVLA3ZNPFKBPmX3k4YigPBLXG6lhlq6FB9rYSWyB6uOP-sbnS4HDtxj24LUgyTnx3LIEXhz9TNBGFikDXQeEeCdANyL9oi_NfxGWM-y_6XoFLeZfkXYG2Sm5S2CF3c1RXcmiDt2kT4KS2JHag0lg27jeSQWijLYJXb9XBhEZLnuxWTJBXOodf4dgq7XCPF8rLOwwfYzlYYXYq3ltxaTdNADEH_NWchyrBBvbbAaPAZTT0hlCZHGqovK9k98UrZA0nEd0zczvuKus7jt9zSV47h-EhUgj9bk1yNU2oMeR6e39_jGB0IwnEpJHAC91mfhIk28BwaTGbv4DhUK-Hf6PkNIeYUON3fYdU-flYl4Ebfdz1zJvSG3K5kSon4fRwY4JaOCA1bGcKBSMXWqXhXecA1uA2CFjwGerh-xOkKpW8KdCsh2m96-XMBF1Gs7N8uSy8MomRarynvFdj7Te2ZTecDW32Epb0mTAiU6kRgWeyQawjsDeQB7ycov_tbbCeIPFUkIZXZ9L3CMSpRX2wjKZReaFHsVmUPyCiONYJIb3X1odGRQ_S51Tr6VJD7qYMXz3ch65sg6Jv06R4hSLUN-rfWM7CXh3a_D12isgc1-DIDLXE9rGJt_3xpkAgMPtsYNqewibF35NBmQXvYnILLyusw_3RA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/523aa1e339.mp4?token=Dhy_QojMM-bbyXnz4qVLA3ZNPFKBPmX3k4YigPBLXG6lhlq6FB9rYSWyB6uOP-sbnS4HDtxj24LUgyTnx3LIEXhz9TNBGFikDXQeEeCdANyL9oi_NfxGWM-y_6XoFLeZfkXYG2Sm5S2CF3c1RXcmiDt2kT4KS2JHag0lg27jeSQWijLYJXb9XBhEZLnuxWTJBXOodf4dgq7XCPF8rLOwwfYzlYYXYq3ltxaTdNADEH_NWchyrBBvbbAaPAZTT0hlCZHGqovK9k98UrZA0nEd0zczvuKus7jt9zSV47h-EhUgj9bk1yNU2oMeR6e39_jGB0IwnEpJHAC91mfhIk28BwaTGbv4DhUK-Hf6PkNIeYUON3fYdU-flYl4Ebfdz1zJvSG3K5kSon4fRwY4JaOCA1bGcKBSMXWqXhXecA1uA2CFjwGerh-xOkKpW8KdCsh2m96-XMBF1Gs7N8uSy8MomRarynvFdj7Te2ZTecDW32Epb0mTAiU6kRgWeyQawjsDeQB7ycov_tbbCeIPFUkIZXZ9L3CMSpRX2wjKZReaFHsVmUPyCiONYJIb3X1odGRQ_S51Tr6VJD7qYMXz3ch65sg6Jv06R4hSLUN-rfWM7CXh3a_D12isgc1-DIDLXE9rGJt_3xpkAgMPtsYNqewibF35NBmQXvYnILLyusw_3RA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
🙂
نیکبخت‌واحدی: ۵ ساله پارتی نرفتم و الان دیگه با وجود هزینه ها نمیصرفه!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/Futball180TV/101459" target="_blank">📅 17:20 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101458">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/67a168b4f7.mp4?token=pKfFL_RkIonJ_9EEH13DMjBoBzRSEHh0TlXhwhYJBRkJAuc4vIjo64wufvOCNZn0swJukx2GdAGxMt2ARECcQn3f3Kfa7BBk4Ij50XTfALlaA0atnahWjzZ7UKsdsISTyxs8qTtM8X9_nheVXGegntySpEz3BP-EyPeUtZgKdGWBtZ7KSFAldoTx48JkKOxJJ5HRCXLsw5VIkEeMlb4WCrdXoyKZgQM-wy3R_OhOdOpa_zRHS-FuLvBxkJNGDeYEVgHooWfjt-OrbzMFIF8XD4tJxU77RnRNCyOe7qbnQF6gOzDGLoq7y9BGIIxe-6s8cC3kRvZYIIHTzKN89FlkHa0-ytl43CERasALwFNTAu6l6omzO4n187rfEC1vd5UDkheI31FC8VFWqk_rPfcfjuZrOBZyx9CCpo0i8QohN9Gs-pvNyQjLiDiUp_urBNJnOKZNkUwmzUtZjYL8bGSkuemrY0UU5V2bTomZptcRJebEkMNy-VBOu5lTZIq32UiUY-BwwBnooP2hyLWyxNdHhP3gbJ-uou1H3k4fSrRvQU_QAcBSfKhGdRgcKJtUP58YUYOzw_vIUz6WoSUsOGxvTtNNm0SwI5lQezIEV_l6ezkf2UVJIYTuwFz1Bx9wWLhRohiToYxzl2L_S0vopUB1ZT9ZzrDoVz_43t5kH3djIWg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/67a168b4f7.mp4?token=pKfFL_RkIonJ_9EEH13DMjBoBzRSEHh0TlXhwhYJBRkJAuc4vIjo64wufvOCNZn0swJukx2GdAGxMt2ARECcQn3f3Kfa7BBk4Ij50XTfALlaA0atnahWjzZ7UKsdsISTyxs8qTtM8X9_nheVXGegntySpEz3BP-EyPeUtZgKdGWBtZ7KSFAldoTx48JkKOxJJ5HRCXLsw5VIkEeMlb4WCrdXoyKZgQM-wy3R_OhOdOpa_zRHS-FuLvBxkJNGDeYEVgHooWfjt-OrbzMFIF8XD4tJxU77RnRNCyOe7qbnQF6gOzDGLoq7y9BGIIxe-6s8cC3kRvZYIIHTzKN89FlkHa0-ytl43CERasALwFNTAu6l6omzO4n187rfEC1vd5UDkheI31FC8VFWqk_rPfcfjuZrOBZyx9CCpo0i8QohN9Gs-pvNyQjLiDiUp_urBNJnOKZNkUwmzUtZjYL8bGSkuemrY0UU5V2bTomZptcRJebEkMNy-VBOu5lTZIq32UiUY-BwwBnooP2hyLWyxNdHhP3gbJ-uou1H3k4fSrRvQU_QAcBSfKhGdRgcKJtUP58YUYOzw_vIUz6WoSUsOGxvTtNNm0SwI5lQezIEV_l6ezkf2UVJIYTuwFz1Bx9wWLhRohiToYxzl2L_S0vopUB1ZT9ZzrDoVz_43t5kH3djIWg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
❌
🔵
محمد خلیفه سنگربان جوان تیم‌ملی با عقد قراردادی به استقلال پیوست
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/Futball180TV/101458" target="_blank">📅 17:13 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101457">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2a7dec4fc2.mp4?token=U7BYIXwL8-mrF0ClEwTNC_0TAxhf74-GR7XovpHtl1bHBHOoiacdS3zc8PKntpmoIYaBIEfQCka5P49RNi3flv9-t02_ZuwVluea70g0MhfeXlUmmbd6bg_7aKft23Yf9c6Hs0LWT9Wanq9ay3ZQKfQVg4NX15wnZPQuTqyzQF9Xgn0HpqNonzpY2C1_4P0GIcioRAYw_7b3wwVrSj43jS2IhJo42Gp9D3WLT2_nSJkBl7MKZIkJJJsDua5y_CpliU-OiE-34eoYMWAnFIb0LW5-ubvJUY27fHz58vrEkxZ4-GaBlCY7MGz8x1D4tlbA_E2AqCKzSk058bMDUhf-tA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2a7dec4fc2.mp4?token=U7BYIXwL8-mrF0ClEwTNC_0TAxhf74-GR7XovpHtl1bHBHOoiacdS3zc8PKntpmoIYaBIEfQCka5P49RNi3flv9-t02_ZuwVluea70g0MhfeXlUmmbd6bg_7aKft23Yf9c6Hs0LWT9Wanq9ay3ZQKfQVg4NX15wnZPQuTqyzQF9Xgn0HpqNonzpY2C1_4P0GIcioRAYw_7b3wwVrSj43jS2IhJo42Gp9D3WLT2_nSJkBl7MKZIkJJJsDua5y_CpliU-OiE-34eoYMWAnFIb0LW5-ubvJUY27fHz58vrEkxZ4-GaBlCY7MGz8x1D4tlbA_E2AqCKzSk058bMDUhf-tA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">😂
😂
😂
اسطوره وینیسیوس بعد عمل زیبایی در برزیل:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/Futball180TV/101457" target="_blank">📅 17:04 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101456">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/48b2d769e6.mp4?token=i5OebZxyyO0q7df_tkXi6mKn5YqSODP7kiry4jUR3aR_yw7Ax0hcrhzmnRjv2heQMY4XoNk59Guf6mC9EGPbfwdzMyCLDOcQk8MtdsdV5HV5dlQ4PyD0ZxnMFq8mf9oC1iwVk3FiKtbQ-16jd_zdcWM0_32eyNpZBiPFvmhtwBNNA0WeDSMVhyFAGP5edg3Q1iaRhAmpE49pHbZ4Xp1iQLbz-Mulv4zgILQS8iMR7i3wZxglYdko8MhzC0RGdYRpjTsH_AWmxm0d64TRyNDUq8f_aPUIN1-aEEzIbG5XpzMnzVQL4UPdiS-fb7NpQfXrER3qaU5Ng9L5TDbWnealKiNQ2vppX1JDhquMAAT4SQzuzVuqHyS00R39aTqBGlZyhPwck18F2Xm0X1imHZ5k4EtgxHTHCLOO9u1eHrAZtE6GoLZOAggSNyStrWWYNim6ZkIoWEpyCLk9TcC8ZyD7sa08uTxhg26STXMFeivxUhPLn5R2fzG5ao80RRVGq2XswUknrOfgJNsr0fHR_U53xrD5WTddUIpvPu7V3pck8l1s1NA-VQXEmTF0CQcE9GZUEftdCoWM6vQrwAfU-Z5KYK1-r-GOPx9fyib2c7APOu07CNs0hs9gCs9lc45fj5SgeoVsYQSuXeU_ao3HVx96rWHivDBBMiUw6I_s--dOZqE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/48b2d769e6.mp4?token=i5OebZxyyO0q7df_tkXi6mKn5YqSODP7kiry4jUR3aR_yw7Ax0hcrhzmnRjv2heQMY4XoNk59Guf6mC9EGPbfwdzMyCLDOcQk8MtdsdV5HV5dlQ4PyD0ZxnMFq8mf9oC1iwVk3FiKtbQ-16jd_zdcWM0_32eyNpZBiPFvmhtwBNNA0WeDSMVhyFAGP5edg3Q1iaRhAmpE49pHbZ4Xp1iQLbz-Mulv4zgILQS8iMR7i3wZxglYdko8MhzC0RGdYRpjTsH_AWmxm0d64TRyNDUq8f_aPUIN1-aEEzIbG5XpzMnzVQL4UPdiS-fb7NpQfXrER3qaU5Ng9L5TDbWnealKiNQ2vppX1JDhquMAAT4SQzuzVuqHyS00R39aTqBGlZyhPwck18F2Xm0X1imHZ5k4EtgxHTHCLOO9u1eHrAZtE6GoLZOAggSNyStrWWYNim6ZkIoWEpyCLk9TcC8ZyD7sa08uTxhg26STXMFeivxUhPLn5R2fzG5ao80RRVGq2XswUknrOfgJNsr0fHR_U53xrD5WTddUIpvPu7V3pck8l1s1NA-VQXEmTF0CQcE9GZUEftdCoWM6vQrwAfU-Z5KYK1-r-GOPx9fyib2c7APOu07CNs0hs9gCs9lc45fj5SgeoVsYQSuXeU_ao3HVx96rWHivDBBMiUw6I_s--dOZqE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
❗️
زد و خورد شدید مردم بنگلادش پس از پایان فینال جام‌جهانی
🤣
🤣
🤣
🤣
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/Futball180TV/101456" target="_blank">📅 17:01 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101455">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ba5d859c20.mp4?token=pABTumjlXpsFqnvM1gJ9kr2JFxo6mrQkEgQJGflvqZ1Z09xsIN0ZU6O7r497VEwMETkg5dUVIbDW823pNxqbB1fnRSY4csSG8JvbIh731JL4czxID-1CsA_sw-Nrzlx7GUFugRrGs1rkDLq9VwREpEksO2TvjnUQw7ibntfxFGs167_w6JjoE7ZFKf72n3byehjUnvs2DiOgM_XslnRu3uRGML-3mxtvN65abI3em8gz6T3VVYgr5G5RTidtDFw46izm2_xS3UpUCr_ogT2j6qsKPnz65RSdUTA2KbQZbjetqZosvwJQ241nSVhRNkfrZAKr8nsaJSE931_536U8nw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ba5d859c20.mp4?token=pABTumjlXpsFqnvM1gJ9kr2JFxo6mrQkEgQJGflvqZ1Z09xsIN0ZU6O7r497VEwMETkg5dUVIbDW823pNxqbB1fnRSY4csSG8JvbIh731JL4czxID-1CsA_sw-Nrzlx7GUFugRrGs1rkDLq9VwREpEksO2TvjnUQw7ibntfxFGs167_w6JjoE7ZFKf72n3byehjUnvs2DiOgM_XslnRu3uRGML-3mxtvN65abI3em8gz6T3VVYgr5G5RTidtDFw46izm2_xS3UpUCr_ogT2j6qsKPnz65RSdUTA2KbQZbjetqZosvwJQ241nSVhRNkfrZAKr8nsaJSE931_536U8nw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🙂
سرگرمی برادر لامین‌یامال با نیکو ویلیامز در جشن قهرمانی اسپانیا بعد فینال
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/Futball180TV/101455" target="_blank">📅 16:40 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101454">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9a645c836f.mp4?token=cg4x7QiQsbU5ZNP1o6UzNyC-3OeIrTYZR4D0z_w9pLsQqcvXsMt3wJENNSR_2Onjy4VjipUGM2zT9xQTprp93bQHZ4rKxdMjLBFR2dIM2dzfX4yJlbd90BLkxfcTNbQHHc4khBPwghn5minTzotPM4X9WlaKJkjyaunjeMU-RMKuUo1EsGsqltcPf70hVp7TdOkgsmbdGaJB5lEVLOhZfYzCmROrpQysAB-qqprKpWOsAaN7NKcMrojAMVpenbG46X9jj5cgIjwIipigX5usCQ3kMX4GAJuULKE7cqWfZWSIbxquE36hnr5vIWVDyfewQZPKCLt3RqTuhxtSQmUHTg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9a645c836f.mp4?token=cg4x7QiQsbU5ZNP1o6UzNyC-3OeIrTYZR4D0z_w9pLsQqcvXsMt3wJENNSR_2Onjy4VjipUGM2zT9xQTprp93bQHZ4rKxdMjLBFR2dIM2dzfX4yJlbd90BLkxfcTNbQHHc4khBPwghn5minTzotPM4X9WlaKJkjyaunjeMU-RMKuUo1EsGsqltcPf70hVp7TdOkgsmbdGaJB5lEVLOhZfYzCmROrpQysAB-qqprKpWOsAaN7NKcMrojAMVpenbG46X9jj5cgIjwIipigX5usCQ3kMX4GAJuULKE7cqWfZWSIbxquE36hnr5vIWVDyfewQZPKCLt3RqTuhxtSQmUHTg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
علی‌کریمی بازیکن سابق استقلال: استراماچونی در حق ما استقلالی‌ها ظلم کرد. نباید تیم را ول می‌کرد و ناگهانی از تیم جدا می‌شد…
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/Futball180TV/101454" target="_blank">📅 16:20 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101453">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PFCG6Rq6nSAuPypwT7GBC8ye_4xeWvPSlyhQGOhtrqf0SzzxlIphZeT0xaos3vjcH-sIw5Q3-b2M7d9rJyT2PSsg7zkLszv_WviL43HiBUVmb7RDiDNWeD-xKJAzHW5IvlIX3oFYokb12TkHxuZRvufcOt9UMPPJvLTTDcXi9y_yfMIIVY_a7iCImKVTSVdoL9Px925UNj4NsfpzmgSZ4Iv0DdyD0-FsJk8q9B69bUPxEmEVwzhGjmtEJIYli0aA6gNgqft5WedysFCLer7sBvn-QAYKXpRSQD3j2bphbT5whBURxXbi0O06SgI-u1AbbGahXwRa8M6w2ac8eivGKA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
بند فسخ قرارداد آیمریک‌لاپورت با بیلبائو ۱۵ میلیون یورو است و اگر بارسا برای جذب وی اقدام کند، به راحتی موفق به امضای قرارداد خواهد شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/Futball180TV/101453" target="_blank">📅 16:05 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101452">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2c9c58dc1c.mp4?token=Wg_XBjcSnlhSwLB0b4rDOQZ2AO8SLDSjWxSPV9pVG4kUstdwBTJwxT5bJUETmFL7YJtJMCC8z4KJ1dq98qFJlmzonUMCmA0j2Qv1-HMykNrxPszA5OdMRzfeQK-Se8SpYKenj9lLzFCqnqCKP3hjWfNCa5EzUmpgwzakUkjp8faHWaWrAhkn-MfoTGirqLiWZVedd0SSc6rXJejuNxB-Av9DvOMr0mZXtN6yDbO43jBacnD4Qj4kmj_8lAkA9-lrPKYQJs-fmMKPbrsjAQwzVR9rdZItH4lxorSj0JA0mQG3lJP2WgJTJe8ZtTPOXAuk16g1Qtkec7N7dmSpE2k1uDI1Uudgsc9Ocf5KY5XyGywTV4hIMcqecjyzXtSVnSHpO0IOMMPGutRRJvHjxH53fn6P-KOROSu4kE9r819gjNG7_NEUFDJQVLka2IGQ6mzXj2h9iO_2H-bCp6v10UhzXfr8SREzwsFMSuhENLJMiCn0N2keSvupQHZ6S_BS-vpajcwE_V35sgTdJHwe21MWTAIf2jksGL8-YVoZZ9SrsWSxcYWJ_XS183a89Gn2OEoWBWww-BclRQ2XI7VgcTbyXizVe3owzfO9ljQzA8RTkrlDbjImvIEyy41dkUDL16zLELwBpUwfIt66EySJoh34wjEtxYjYvgfjkZ_I3iWVWiA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2c9c58dc1c.mp4?token=Wg_XBjcSnlhSwLB0b4rDOQZ2AO8SLDSjWxSPV9pVG4kUstdwBTJwxT5bJUETmFL7YJtJMCC8z4KJ1dq98qFJlmzonUMCmA0j2Qv1-HMykNrxPszA5OdMRzfeQK-Se8SpYKenj9lLzFCqnqCKP3hjWfNCa5EzUmpgwzakUkjp8faHWaWrAhkn-MfoTGirqLiWZVedd0SSc6rXJejuNxB-Av9DvOMr0mZXtN6yDbO43jBacnD4Qj4kmj_8lAkA9-lrPKYQJs-fmMKPbrsjAQwzVR9rdZItH4lxorSj0JA0mQG3lJP2WgJTJe8ZtTPOXAuk16g1Qtkec7N7dmSpE2k1uDI1Uudgsc9Ocf5KY5XyGywTV4hIMcqecjyzXtSVnSHpO0IOMMPGutRRJvHjxH53fn6P-KOROSu4kE9r819gjNG7_NEUFDJQVLka2IGQ6mzXj2h9iO_2H-bCp6v10UhzXfr8SREzwsFMSuhENLJMiCn0N2keSvupQHZ6S_BS-vpajcwE_V35sgTdJHwe21MWTAIf2jksGL8-YVoZZ9SrsWSxcYWJ_XS183a89Gn2OEoWBWww-BclRQ2XI7VgcTbyXizVe3owzfO9ljQzA8RTkrlDbjImvIEyy41dkUDL16zLELwBpUwfIt66EySJoh34wjEtxYjYvgfjkZ_I3iWVWiA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🎙
ایمان صفا بازیگر سینما: با کری خوانی‌ام دل خیلی از استقلالی‌ها رو شکوندم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/Futball180TV/101452" target="_blank">📅 16:03 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101451">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">🎁
بهترین اسلات‌ها با چرخش‌های رایگان یک بت
💥
تسویه سریع و آنی جوایز شما
🎰
لذت بازی در کازینو و کازینو زنده با 30% کش بک بدون محدودیت سقف
💯
100% بونوس خوش‌آمدگویی به مناسبت اولین واریز
تا سقف 100 میلیون ریال
📱
اپلیکیشن اختصاصی با سرعت بی‌نظیر
🎊
وقتشه با کازینو یک بت، برنده‌ی بزرگ بعدی باشید!
1️⃣
لینک بدون فیلتر
1️⃣
ورود به سایت با فیلترشکن
••••••••••••••••••••••••••••••••••
💠
لینک اخبار و هدایای سایت
👇
👇
🔸
https://t.me/+ioIBrQfqMLtmMmEy</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/Futball180TV/101451" target="_blank">📅 16:03 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101450">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CIL7gNGbDwzmImp7suZtqYlRlko1REKrZ2qexoMTVQZf_jtgegF3H9_WeawGXeOA4zd5QZ7BtosYxbygHVjWQIWjwYcsJTNr6a8M_3-Bdr2_wWEdVZTWkIjqNgXkMaAluCEJtNQIJN91S9c4N2-qCHtCR6v8NEPPfgo7y7Pv_1SaPsib7_8_iGS7T3pf4BMUl73NOMoEiTQUzF5PvVciI_jKxNS-omFtmk9N_o1k8cS7iVXwbA1gicipYaIX6UEXj-x0scf01cC1TFsskzlSz8bjhpPmv91YZ-f3XZcg2mIWKs4yx7UNPBoBlIdi6cMfr3dYS7nXGj852n57h894rw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💎
سایت پیشبینی
YekBet
💎
🌟
فری اسپین‌های بیشتر، هیجان بیشتر!
🎰
با واریز از طریق کریپتو، ووچر پریمیوم، ووچر اتوپیا و اتوپیا، بیشترین پاداش را دریافت کنید!
✨
1️⃣
لینک بدون فیلتر
1️⃣
ورود به سایت با فیلترشکن
📲
@yekbet</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/Futball180TV/101450" target="_blank">📅 16:03 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101448">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/68a6db964c.mp4?token=BwrFby8CsjapsrwkAuY2nrVFRjutI1tgw5yzjMGjn5EsrhAm3T9FqKEo8kbUAZdF2gRSkKjZJRxHSWmEEUNMHhR7EhfBHTDEyvj_ujjdFKQA0S3yL-6di4BaHutC1Sui-yckc6-6AAnGW9Ujm8Bc_Se6-0OWVdqFZ04iRl3pPUH3UQ5QaPLT5cgBFCirOUeOBYCiiZkXmyOubrsfetnd-cQeo43aEVZKJFquWLOaVUvC8f-TXDSycgCsXQRXayLP0Luhl1SN3KnBkOlOYwMoM5xMHtbtkOxlbyoWTE7_MAM2YL-YrjCc7VXg3ekFRzxpoGpP2p3PzfZZ9mRbh-Tzjw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/68a6db964c.mp4?token=BwrFby8CsjapsrwkAuY2nrVFRjutI1tgw5yzjMGjn5EsrhAm3T9FqKEo8kbUAZdF2gRSkKjZJRxHSWmEEUNMHhR7EhfBHTDEyvj_ujjdFKQA0S3yL-6di4BaHutC1Sui-yckc6-6AAnGW9Ujm8Bc_Se6-0OWVdqFZ04iRl3pPUH3UQ5QaPLT5cgBFCirOUeOBYCiiZkXmyOubrsfetnd-cQeo43aEVZKJFquWLOaVUvC8f-TXDSycgCsXQRXayLP0Luhl1SN3KnBkOlOYwMoM5xMHtbtkOxlbyoWTE7_MAM2YL-YrjCc7VXg3ekFRzxpoGpP2p3PzfZZ9mRbh-Tzjw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🎙
🙂
خاطره علی کریمی بازیکن سابق استقلال از اسپانیایی صحبت کردن میلاد محمدی
😂
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/Futball180TV/101448" target="_blank">📅 15:40 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101447">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/53a9000335.mp4?token=Gd1KFX4R-pBIKVvzS3NgPWQOGzKiVdFHT23_6Enxir_WjbEXkTyG1s4W45ocB68pHvclchc_1f5Z4misLPtU8-9dEGj6-SaFOJwyZcb166CDtSHsZtKQfUF7E02PfR3NxAfURVDa3m1tjdFbUMs2yQv_oA2tOVGTr0C50K94DXwbDFwUDd-ZAdglmjSZKCEj6woiuFjCG19as6yumr6jnch3biJfZJuFXv7mg_JxuHdva5o4jFB1ThXCKPJmYRU-jaAs24DnYkjAY0qPupT9GH8tZuYTcqxoI2MzVAJ9uKkFDDNcJh_Tmby4o_kwmu2UnVLOgqwH6x830MJAmqSi6I6QxeFowWluH3BDPB4bQQImpy_EEeMZt8Iey0FHM537pmK5rwASxuPTJg-rv_fOzyCxfxDSwlttNWkJbhDeSNmJs9xQVR5az69W2d4PjT5crMiPcWUJ8ba3PSZ0FAr0kL4xkKArJePgBr-cObrenETI_I5c4nSwHMEi0Q2_SXHHvfr6aJ-qKZwhpDyjHxW3jrSERT_A3olqO_sFb3UgG95j5Kd2XUhodPuxrxemltIIYofuFeoV7_Q7EdxyB5Bd6s1qesx0WDsrpZ-1k1yAex_wtwo-G824pKoGFL8aoTyw6D9u_Avxvujzh6bakLWzUU8fQg3-PXYodeMGDgt9vzM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/53a9000335.mp4?token=Gd1KFX4R-pBIKVvzS3NgPWQOGzKiVdFHT23_6Enxir_WjbEXkTyG1s4W45ocB68pHvclchc_1f5Z4misLPtU8-9dEGj6-SaFOJwyZcb166CDtSHsZtKQfUF7E02PfR3NxAfURVDa3m1tjdFbUMs2yQv_oA2tOVGTr0C50K94DXwbDFwUDd-ZAdglmjSZKCEj6woiuFjCG19as6yumr6jnch3biJfZJuFXv7mg_JxuHdva5o4jFB1ThXCKPJmYRU-jaAs24DnYkjAY0qPupT9GH8tZuYTcqxoI2MzVAJ9uKkFDDNcJh_Tmby4o_kwmu2UnVLOgqwH6x830MJAmqSi6I6QxeFowWluH3BDPB4bQQImpy_EEeMZt8Iey0FHM537pmK5rwASxuPTJg-rv_fOzyCxfxDSwlttNWkJbhDeSNmJs9xQVR5az69W2d4PjT5crMiPcWUJ8ba3PSZ0FAr0kL4xkKArJePgBr-cObrenETI_I5c4nSwHMEi0Q2_SXHHvfr6aJ-qKZwhpDyjHxW3jrSERT_A3olqO_sFb3UgG95j5Kd2XUhodPuxrxemltIIYofuFeoV7_Q7EdxyB5Bd6s1qesx0WDsrpZ-1k1yAex_wtwo-G824pKoGFL8aoTyw6D9u_Avxvujzh6bakLWzUU8fQg3-PXYodeMGDgt9vzM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❗️
علیرضا جهانبخش: در مکزیک زیاد بهمون بد نگذشت
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/Futball180TV/101447" target="_blank">📅 15:20 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101446">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f60626ee05.mp4?token=MEJ7exygErkyjO2cPn-LMnU6oa3goN6hu3J7cnTZ2A2Iutw4TrU-voFqeFXDY4yIjECoTWQJgP9_o_UyHgvK6JkU6ztFriUqVSd7xKn3EHVZQdJSCFqxOgRKOodv7EKg5tmHCfP8DSBa5XkZ384bm9WEwEQw96M6xsqhbkgAV1_EaYNGbFEkBPr4WVB_rmDpB7LXSrRGYze123yWpC3W5jEsMh2wHFZ8ZX_JMouOWzAxjYMEA11I8mu9Gh82XxMVZcYjqwZdxdJS1dCIYM6w-sSHsTld8bWor3SG1HqO1oWGuVBehc_08bfpPj9k4G7C5t7DR3-ku5jBgdlA78O8Xg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f60626ee05.mp4?token=MEJ7exygErkyjO2cPn-LMnU6oa3goN6hu3J7cnTZ2A2Iutw4TrU-voFqeFXDY4yIjECoTWQJgP9_o_UyHgvK6JkU6ztFriUqVSd7xKn3EHVZQdJSCFqxOgRKOodv7EKg5tmHCfP8DSBa5XkZ384bm9WEwEQw96M6xsqhbkgAV1_EaYNGbFEkBPr4WVB_rmDpB7LXSrRGYze123yWpC3W5jEsMh2wHFZ8ZX_JMouOWzAxjYMEA11I8mu9Gh82XxMVZcYjqwZdxdJS1dCIYM6w-sSHsTld8bWor3SG1HqO1oWGuVBehc_08bfpPj9k4G7C5t7DR3-ku5jBgdlA78O8Xg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👍
👤
محبوبیت خریدنی نیست...!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/Futball180TV/101446" target="_blank">📅 15:02 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101445">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/V_YeiiLTyWmaH4X-4Pp40TK58SvpC1FwYmasRiL5vky26KBl1VHSRAZgoWJc4Iqn76iFh0Malplc4jxOSJE7V7kWgpZNAhCbRKn0-HnGPa2g_Au64Jo4f4AuyXtUDVggmOyCDLuJgYTu5athBfloyKWLwPxhpVHAsx_GhsdULAqgsQyfZzftQS_gnULgNJ4c8_ZBzW6LmHR1NJCRhJdlVhtN1Wk1kxnatV5QDpG4QTIVffGwkdege6sQluIvcR7gDFoMc_oNZn6MhEUqZEy5os-4lOHqzIWx0fsR2WssppZDWiEpSuTupAxtCioYLrKSN6qP0P_Kak3Y1R6ZcB8xdg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👀
💥
تعطیلات تابستانی رافینیا و زیدش
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/Futball180TV/101445" target="_blank">📅 14:40 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101444">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Hag7ki8B7t2PcGfpUqBZEPw0VwcwqlTlF-5lZUEqtoJGyqVAYAe9JgnLhDUZ5n4OkL0REOS0aa4_qgptFdEyI30e4sZTdSIKLwGs98vRnAv9_ykjKjqp1e9pMqRQUrhziZV_XxdkZbCUuD3a48pEIBm6_Hq4x5htGQvjbXuMqwZBqTUW0dTtOcVFfSDZMvpYaNRpXA48EY5H7UADXYBrlcrVNSFS3Cu-5a4h8oWN_ua_O8CW_gV6aTw8jM7AW5IjFde_7v-EoE6KXqD7Z4fjczRNt-NOTLzI_huNpRG20HGNeMGba5KjzJhL5hfunxfr0Y2qXbBfQ9q50jte8rH8bg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
✅
🔵
علیرضا کوشکی دقایقی‌پیش قرارداد خود را با استقلال تمدید کرد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/Futball180TV/101444" target="_blank">📅 14:29 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101443">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bd8a4b410a.mp4?token=B8M6Bf6QyO22vL3GZpiScB0GU_S-i2y5C3J4hD1oigH0xAYWtoYHLURYNymH1nPGuKYRBjHBAt0mlPMTHGiulYcw3vdrI_ndWWv2IZg0l6uD3-_FYsErqv7xb5PSD6CPJHX7ruNJZ9JXu3ABc93zrjVU5N_pOVFBnlRUIn1756hTctmoxMGlPfsnWMe9QCkMlO7NSpc8HRglLaS4huNmf4Yf0SaRqk_D1ASX6rKFIwcJH0gx7H1HpYCdFbRjukq9fselPeuTagfS3scjvuBqQ4ie7pdNWvg8ufXoagQtLepaneFiO7PeZlouIz0WtI90eY8QowXJNgKrACagWuU85g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bd8a4b410a.mp4?token=B8M6Bf6QyO22vL3GZpiScB0GU_S-i2y5C3J4hD1oigH0xAYWtoYHLURYNymH1nPGuKYRBjHBAt0mlPMTHGiulYcw3vdrI_ndWWv2IZg0l6uD3-_FYsErqv7xb5PSD6CPJHX7ruNJZ9JXu3ABc93zrjVU5N_pOVFBnlRUIn1756hTctmoxMGlPfsnWMe9QCkMlO7NSpc8HRglLaS4huNmf4Yf0SaRqk_D1ASX6rKFIwcJH0gx7H1HpYCdFbRjukq9fselPeuTagfS3scjvuBqQ4ie7pdNWvg8ufXoagQtLepaneFiO7PeZlouIz0WtI90eY8QowXJNgKrACagWuU85g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
عکس یامال روی پهپاد انتحاری شاهد قبل از شلیک
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/Futball180TV/101443" target="_blank">📅 14:25 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101442">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aD6oYlT3Nm_lBiTb6btSHhjodKvsPH81tp089KsqiccI9hDIPn5GlgGqYcHWmlZnSB4fxhqrNIV-CVmH90GdWq4zJMOL0r5YmG4P22J9n3R0VZgcpHOfM4entr2hHY98sNplSxitIjE7ukpErU9dsY3gGx9USPlE7kM2zhR0TmPse4S4vSPm7kXCpMcueaRdOxsHXd6XDqvZRopp1Rb_Dyg-H50EchSvIGuY9EvMO4yq3VHe3b9B768yRlWXvPqePzlBC_E7rD1Su8qnGmfdb9kjnviokLDHe2F45A6cN8An9t43BmM-FIiSNtwxW0NCkgbLr9c-VKrypIwaqLquUw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
رامین‌رضاییان با انتشار این استوری تقریبا جدایی خودش از استقلال رو اعلام کرد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/Futball180TV/101442" target="_blank">📅 14:17 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101441">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eouL5Z5Ji27Gig83aBAXLqQlDbOp6aX9g_GBsmtoHx7x5cWxj46B35nC043M9pSANAHb5CAsRYoqzPdY32MfyfafYAgJyk1BycTw1IW1V5Pdm3-77MLHf3oQzhEVEfz_Zl9h_AmjPUp4RoEhyhkvh0vTfd3OW4zJV0Ku1ieoImgpc-VNIOMQWRFY3lnAw3gpWYg2BHj_AfaVLfRCvpwhHTJJDPLl8cUCcs4dRv9Fkk1N7Crih4dDzdTRbHxfbu4Ql9s27vplSH9-G5CZVe00fvLa13UAUdP5nkP54NLtmNyvX3e_KdoHpP7cLYyXXZ2wFbKOaQf6QW2PS2GBszq0_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⁉️
🔥
لیگ‌های بزرگ اروپایی چه زمانی آغاز می‌شوند؟
🏴󠁧󠁢󠁥󠁮󠁧󠁿
[31] روز تا بازگشت لیگ برتر انگلیس باقی مانده است.
🇪🇸
[25] روز تا بازگشت لیگ اسپانیا باقی مانده است.
🇫🇷
[33] روز تا بازگشت لیگ فرانسه باقی مانده است.
🇩🇪
[38] روز تا بازگشت بوندسلیگا آلمان باقی مانده است.
🇮🇹
[33] روز تا بازگشت سری آ ایتالیا باقی مانده است.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/Futball180TV/101441" target="_blank">📅 14:08 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101440">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0f0fd702ff.mp4?token=CAMNrIBEL9bVxfqy7D8a4X4fd-9N7bQcu9cxOF61VvBV3fjhATgYL4ZNpud_RA3DMAc8CEzaaRjHMh98KWYOtmC66M-Y6U0LeOwjlkFoaHQ8hhKn6zcqqIev3g_bwQnqoc1xBdo7XqaOAqc409-t_kLzXtW35DL5R42R98WWaV90dYRJdy3T-ThmVPYTulWovUdwgflT3N8AALqhgiGj7AQQ1NTufJX8pBY-wHyYESCPEoAqOxrtfQq72djk6VMQuUzvQZBO3TsHROcCN25UG_OHJS3Hep1pBiHrRxM0eFeutTbBCBw-gAu5SwyM8Wvs3rvB3djQBXJuHbyC6YImnA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0f0fd702ff.mp4?token=CAMNrIBEL9bVxfqy7D8a4X4fd-9N7bQcu9cxOF61VvBV3fjhATgYL4ZNpud_RA3DMAc8CEzaaRjHMh98KWYOtmC66M-Y6U0LeOwjlkFoaHQ8hhKn6zcqqIev3g_bwQnqoc1xBdo7XqaOAqc409-t_kLzXtW35DL5R42R98WWaV90dYRJdy3T-ThmVPYTulWovUdwgflT3N8AALqhgiGj7AQQ1NTufJX8pBY-wHyYESCPEoAqOxrtfQq72djk6VMQuUzvQZBO3TsHROcCN25UG_OHJS3Hep1pBiHrRxM0eFeutTbBCBw-gAu5SwyM8Wvs3rvB3djQBXJuHbyC6YImnA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👀
🇪🇸
خانواده سلطنتی اسپانیا در مراسم استقبال
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/Futball180TV/101440" target="_blank">📅 14:03 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101439">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">🚨
🚨
🇪🇸
#فوووووری؛ متئو مورتو: برخی از اعضای مدیریتی رئال‌مادرید درحال پیشنهاد به پرز برای بازنگری در مسئله جذب رودری است. این بازیکن از سبد خرید پرز حذف شده و حالا با درخشش فوق‌العاده‌ای در جام‌جهانی مجددا نظر مادرید رو جلب کرده!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/Futball180TV/101439" target="_blank">📅 13:52 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101438">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e455125710.mp4?token=srurpYpFxij1ZDcAdXRD2QFW8i9HDVVMJanSUKfC9iumg8sMiXzzEnZd4TG4-PMt3e96YOYpwavzUUExrvewHFXsNSQDsFGSvZzEPknjNGeTpjNLGXftREOMTqeUx3EYv8y8gmfYwE0j8Gip6VQUcg5_93szuQly_zZMsl02-3KyWlfz0eW8BTQY1bB3hUOaJ8Uemaz8EvOVglphnsaV_296FM95uq-2UAlW5uSjC5t0VCbj2FhaOu3Ei8mJw9RSg01MUjgTld_D9Si1MS-p4HHfLfmWA9AhbgDrLEmZ6PNKG-FiNr1Yk9q22JCAQp3HnaeDk3AEZV-A4H2rJYEnHg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e455125710.mp4?token=srurpYpFxij1ZDcAdXRD2QFW8i9HDVVMJanSUKfC9iumg8sMiXzzEnZd4TG4-PMt3e96YOYpwavzUUExrvewHFXsNSQDsFGSvZzEPknjNGeTpjNLGXftREOMTqeUx3EYv8y8gmfYwE0j8Gip6VQUcg5_93szuQly_zZMsl02-3KyWlfz0eW8BTQY1bB3hUOaJ8Uemaz8EvOVglphnsaV_296FM95uq-2UAlW5uSjC5t0VCbj2FhaOu3Ei8mJw9RSg01MUjgTld_D9Si1MS-p4HHfLfmWA9AhbgDrLEmZ6PNKG-FiNr1Yk9q22JCAQp3HnaeDk3AEZV-A4H2rJYEnHg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
‼️
دیس فوق سنگین ابوطالب به قلعه نویی: ما تو غار کنار عادل فردوسی‌پور هستیم.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/Futball180TV/101438" target="_blank">📅 13:38 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101437">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/f7wpS2OZL6i2F0a0rfSOnjmHDXz6ZRHxYIkxEkVKOxMhGtngEm9eumt6RN91AAD4ikPB_Q_KNczWE1am24UjrfN4a1iW4DPV8dMUaBTP9zbEGeWp0ey8m0MqokPVBgpI-jkkxngRR3bPOi1GwNjtRbT0yHxrOrDvNN-V9Kwasfjwxy6OKrOFkRBasTbZqH3sm6EO0j9DGUl3RpFfapWpqSMuc770YpO6tUqt3oejTOwlyPF5xX9Fxw-PdU3jl2D_h_KCaNhWWhEYyGGc-OZux9yttV12jpFDqe1hCg2EwDcJHVIBfB3oza6wldwpOf9NNPjcy0mus-kyrimlqI8TfQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🇪🇸
#فوووووری
؛ متئو مورتو: برخی از اعضای مدیریتی رئال‌مادرید درحال پیشنهاد به پرز برای بازنگری در مسئله جذب رودری است. این بازیکن از سبد خرید پرز حذف شده و حالا با درخشش فوق‌العاده‌ای در جام‌جهانی مجددا نظر مادرید رو جلب کرده!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/Futball180TV/101437" target="_blank">📅 13:33 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101436">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/b01qnqpWiSJtGe76zuSFxho60ebc_nIlXhWIjxd_nJbgBMCSQRZAIgUik5NBuN98xkbMr8IEd-28p6ZiLYzd43Oys7zItVN4wfNgLxuLEvdIT4cT-C75fImpDeRv_6gDRIsKV5H-dl7_JZbpMWXz2la_kkH_aZy93vHUOJ1cj09KVneQbThACrmOSiNpqwVcbUCFW3xhwnvZnM4KZvV5SZawC-MZHgw6EQnESuzbXD40Bn7tKTmEgUYSQgy8n0r5tXwK-QEuvD5Xl9VuoZ5shbYaqnQPcm9cxKUpQ_FDYf__yZMsmxQnhvgeaQLRs7pVQIJ4_i6sdPU8oFmYkwyMGw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🗞
🇪🇸
جسی‌بسو بازیکن جوان تیم کلوب‌ بروژ بلژیک به باشگاه بارسلونا پیوست
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/Futball180TV/101436" target="_blank">📅 13:24 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101435">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">🚨
🔵
🔴
#اختصاصی_فوتبال‌180 #فوری
🔴
🔵
برخلاف اخبار منتشر شده در دقایق اخیر، باشگاه پرسپولیس تا این لحظه هیچ مذاکره‌‌ای با کوشکی و اسلامی دو بازیکن استقلال انجام نداده و این اخبار برای بازارگرمی و مختل شدن روند تمدید قرارداد این نفرات است. گفتنی‌ست که آبی‌پوشان…</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/Futball180TV/101435" target="_blank">📅 13:16 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101434">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2b5cbab8fd.mp4?token=VSRsO1WpEoqJ7hTxJgXfDf7919QmqCHqQpct49MVyJPpx6wEZu45IVniWoWpyO51BaF8x8jarVBP8BuY2koYynN1ASkxz2enRJeE7sWTfV6zXxnZsapR6M4Xlcjy9m_g2Q5r5yEcOWpqJzFfAsKhwmxBYwAl70m75m0T8z5SA8skojL5l3Be1XLDyjrStQkRx8dtvNGmmbOx4s63jYu4AFfUeSYivZRt7sHHgi9ASXfft_2gI_5wFbQveqkd6Axfqs4oUPr9Sd7tG9jgTmO4hR1B5KdnCqE8LlAj4eh3a0ThywmjgS1tATjWd6QFmgUMYqyo2sNRzc8utpW_I5yE2juIKFHLZTtwZwKT9ha_U8bgEXvAXnTf6GhElcSnwLyCDqACOsxLtn1MLa7uqZ14Ph9IP9_jOPVWkVQ_-jsOZV80yWJGVMC8MiHMq81Kd39IqbmzCg7ti6Ov0jqmIjdqFR4C3JJ3ydCdLAN_RSav_5O3WSdRBS3fCpQs10vqPyz5KQdRHo8ndT63ahcufiD_e1P9k4Ejf2DNRDWTtin-6AsaiheVWBHaRStloZoGOVI5Sp71qs7Q2R-BQ47iC1uLVevV3hQPssNdCgTjwDAL-olqzF0gQtlPV7fCPdDs5ZSzX-f7_SuqGhOi83vw7aq-KvT3OxELK_t6MorlRt4IGhk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2b5cbab8fd.mp4?token=VSRsO1WpEoqJ7hTxJgXfDf7919QmqCHqQpct49MVyJPpx6wEZu45IVniWoWpyO51BaF8x8jarVBP8BuY2koYynN1ASkxz2enRJeE7sWTfV6zXxnZsapR6M4Xlcjy9m_g2Q5r5yEcOWpqJzFfAsKhwmxBYwAl70m75m0T8z5SA8skojL5l3Be1XLDyjrStQkRx8dtvNGmmbOx4s63jYu4AFfUeSYivZRt7sHHgi9ASXfft_2gI_5wFbQveqkd6Axfqs4oUPr9Sd7tG9jgTmO4hR1B5KdnCqE8LlAj4eh3a0ThywmjgS1tATjWd6QFmgUMYqyo2sNRzc8utpW_I5yE2juIKFHLZTtwZwKT9ha_U8bgEXvAXnTf6GhElcSnwLyCDqACOsxLtn1MLa7uqZ14Ph9IP9_jOPVWkVQ_-jsOZV80yWJGVMC8MiHMq81Kd39IqbmzCg7ti6Ov0jqmIjdqFR4C3JJ3ydCdLAN_RSav_5O3WSdRBS3fCpQs10vqPyz5KQdRHo8ndT63ahcufiD_e1P9k4Ejf2DNRDWTtin-6AsaiheVWBHaRStloZoGOVI5Sp71qs7Q2R-BQ47iC1uLVevV3hQPssNdCgTjwDAL-olqzF0gQtlPV7fCPdDs5ZSzX-f7_SuqGhOi83vw7aq-KvT3OxELK_t6MorlRt4IGhk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
👀
🔵
باشگاه استقلال با انتشار این ویدیو نوشت: برای بعدی آماده‌اید؟!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/Futball180TV/101434" target="_blank">📅 13:14 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101433">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/g8rJE5AzDhndZeZsdo3Zcps67huw-S_idOX0pknW8fO5qgHFkWKpA7JDaPbUq3bIQn7cLlG9V-2QA21zoJMJYR7D62ZodnRvvJOQRn0VWRR3nDzqRwFrLwE--8yKnfIXyJgXtB7QLr6g8IA1WFVnRL1hFnXZ6v8ukdt5N4l2afmcRTJbLLr__jsC2bu48lgnqlvbSQhnSjhNUTEScaCTaFB8KchhMdgPm8g32VGVce1YNTQuRrhn_YATGDEgeAWJLs_1C5rTUT69RqZ-slTV6W_AWBWuG_SxoZ8f7t53V4I1sk7YB_PZ5um_0O1bSe7LPrjXZimX4gAdaLqR4b5NQA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇫🇷
🇪🇸
🚨
نشریه(L’Équipe): رئال‌مادرید بدنبال عقد قرارداد با فران‌تورس ستاره بارسا رفته
کاملا جدی این خبر رو زده
😂
😂
😂
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/Futball180TV/101433" target="_blank">📅 13:12 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101432">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7351cc80a0.mp4?token=LfC_jrK7efy3tOx1p9JZLm_NTJL-jCOZKlznUOlrhx91KZmR2ekkvq25yWEEqtL0E2D4VypRvpKbxtyQfw4J6gm7XUuQuuZw2j4l6yxHvbItsMQfzKzlLGeSJFwKQ1rznvA4eRtwolHEo0-QRDB_Nf600ZZNOjA4tvKM74F6-H4WvlEHmUuEq1ZC-1oxohjiCm53L5qoFZ8qMvt-TD-0vwsdShYk6zBQg81Kaf-sKQNubVrXSiyishF8u4e6vSm9V65AN0KOODaBv1ZhUy8dKvk08FslqoOvteoZN7fVS0Z-FFRKmxSeWSMFkg6BDJ6GMS46E3Qpqy_URlKIDPXjKw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7351cc80a0.mp4?token=LfC_jrK7efy3tOx1p9JZLm_NTJL-jCOZKlznUOlrhx91KZmR2ekkvq25yWEEqtL0E2D4VypRvpKbxtyQfw4J6gm7XUuQuuZw2j4l6yxHvbItsMQfzKzlLGeSJFwKQ1rznvA4eRtwolHEo0-QRDB_Nf600ZZNOjA4tvKM74F6-H4WvlEHmUuEq1ZC-1oxohjiCm53L5qoFZ8qMvt-TD-0vwsdShYk6zBQg81Kaf-sKQNubVrXSiyishF8u4e6vSm9V65AN0KOODaBv1ZhUy8dKvk08FslqoOvteoZN7fVS0Z-FFRKmxSeWSMFkg6BDJ6GMS46E3Qpqy_URlKIDPXjKw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
کنایه نیکبخت‌واحدی به ممدحسین‌میثاقی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/Futball180TV/101432" target="_blank">📅 13:04 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101431">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d0edf1184b.mp4?token=ESHoVIKt3QWZj8XLEL4fXzGsTSwxwH7blDTQfDwqSK-v3tGOxJjijz-FPXO4y544kI2qp8HXYEv4Tb7WhsC2AhOrAGsFwBG9QCV9sSsSqQwziOrsLB7gvb-vJC40PDzgAgWUCH62kbsCKoYcEYyTpF3ahmxhK2xvBa-y31KkxSx0o3VwgnlWmk4Y7MJ5x0RmEje1fBSy2zZOBhZPKHj_B_WQ55xepCwflXRh0HOmTbwuNQjtEKzadlrU7VDHX_1YPGA-VqE200RPILkfkvlmqRIf9inoA19iH1X1A-pYhplUVDnljq8nnchnlmecbgMyawwT2xQWmtImsfsZ1zSPAg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d0edf1184b.mp4?token=ESHoVIKt3QWZj8XLEL4fXzGsTSwxwH7blDTQfDwqSK-v3tGOxJjijz-FPXO4y544kI2qp8HXYEv4Tb7WhsC2AhOrAGsFwBG9QCV9sSsSqQwziOrsLB7gvb-vJC40PDzgAgWUCH62kbsCKoYcEYyTpF3ahmxhK2xvBa-y31KkxSx0o3VwgnlWmk4Y7MJ5x0RmEje1fBSy2zZOBhZPKHj_B_WQ55xepCwflXRh0HOmTbwuNQjtEKzadlrU7VDHX_1YPGA-VqE200RPILkfkvlmqRIf9inoA19iH1X1A-pYhplUVDnljq8nnchnlmecbgMyawwT2xQWmtImsfsZ1zSPAg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">💔
داغ‌عشق پرنسس لئونور به گاوی دیروز تازه شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/Futball180TV/101431" target="_blank">📅 12:40 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101430">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/556a03bf67.mp4?token=uC9mfc1wkSnTpEu90ZSAo-4Si046-kpYnpRsuw04Mjtd1weA3AD3omRN4cB8Dn4buT9rGse66j6yt1FaK0EiUUwZMVcSR0stDIvcsK1TT_SnJS3-04oIZlJJFutKwys4twMS9wvaY34ATeJlOmbkt_4AYJ8eOmgb6K3Id8TbisAFJX9tULS1taNFkarpXEIOVMO-DNbgmnh7bXQ9WOcvZGLaM9wbu-bJrJ2DJvO_S39kGFGUtcuZUNHnnKhkUVODpS0TQGcwEMxmki5J1L0o1P6io_ZTqmEf9Jt0rci94rASw0xtdt4LI77GHQcZbMsUwiDO0HCJ_oAYcVK_YgMIpg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/556a03bf67.mp4?token=uC9mfc1wkSnTpEu90ZSAo-4Si046-kpYnpRsuw04Mjtd1weA3AD3omRN4cB8Dn4buT9rGse66j6yt1FaK0EiUUwZMVcSR0stDIvcsK1TT_SnJS3-04oIZlJJFutKwys4twMS9wvaY34ATeJlOmbkt_4AYJ8eOmgb6K3Id8TbisAFJX9tULS1taNFkarpXEIOVMO-DNbgmnh7bXQ9WOcvZGLaM9wbu-bJrJ2DJvO_S39kGFGUtcuZUNHnnKhkUVODpS0TQGcwEMxmki5J1L0o1P6io_ZTqmEf9Jt0rci94rASw0xtdt4LI77GHQcZbMsUwiDO0HCJ_oAYcVK_YgMIpg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✔️
🇦🇷
استقبال مردم آرژانتین از اعضای تیمشون
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/Futball180TV/101430" target="_blank">📅 12:18 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101429">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/44603a4d54.mp4?token=NFL2bOO4kKRXRWGmNIE9QvZYVQtTmt8f8VsFcO7uSuEol4tBuOEFXoNxAQCs6EnUxvsVqk-5UyZhrArc-JQ7kblmsXd6hUnBvyFbMboWJp0ZmaOBwkpezaVvDWBSNbnA6-y1H1t4yK8xZ9CedTpz6uTPE4TsXFkMl1ewALnvqpUObe0c0Smfc-Uuthd1mUqXSJRhRxVOeKSH9rdgg2FNTKoxo6o20VW6MqNEbXN4PxhpcLy9jQG6GqIpy5TwUZqQyk4cH9-p3pz0HHOCE8vFtW7B928y6pgGcOt7vfQSSRNmgnU3mqyGmU-XGGC3yGV9GgZnKprzm6q3ADWUgexAwg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/44603a4d54.mp4?token=NFL2bOO4kKRXRWGmNIE9QvZYVQtTmt8f8VsFcO7uSuEol4tBuOEFXoNxAQCs6EnUxvsVqk-5UyZhrArc-JQ7kblmsXd6hUnBvyFbMboWJp0ZmaOBwkpezaVvDWBSNbnA6-y1H1t4yK8xZ9CedTpz6uTPE4TsXFkMl1ewALnvqpUObe0c0Smfc-Uuthd1mUqXSJRhRxVOeKSH9rdgg2FNTKoxo6o20VW6MqNEbXN4PxhpcLy9jQG6GqIpy5TwUZqQyk4cH9-p3pz0HHOCE8vFtW7B928y6pgGcOt7vfQSSRNmgnU3mqyGmU-XGGC3yGV9GgZnKprzm6q3ADWUgexAwg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
حضور ترامپ در فینال جام جهانی، ورزشگاه را به یکی از امن‌ترین نقاط تبدیل کرد! از بالگردهای امنیتی و نیروهای ویژه تا تدابیر حفاظتی چندلایه؛ همه‌چیز برای حفاظت از ترامپ در بالاترین سطح آماده شده بود!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/Futball180TV/101429" target="_blank">📅 12:00 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101425">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/co-DkvzbSi9KWK-ZQknG6a5UHIQI0HNYlFbZlEFBYuzBNJ0HxNED3AUfO6-QjEmrpXuRL0yJDHyksx26D2AkSRLN_PhWoGzrMoUjYP5ZTR0ADuPSNrKS3mh2urJGUAlsQxuObpZlRQjObZeZtUgsAs0tHw-vKfsGb5qBci30CDsBC0VhoBX6QnZlAelWL0IxK3blcTtdg9t6BEQFIAMu52MWYWa7LbYSJmR_u7LjPyqEkFgJWA7Amq-f4ggESJkYB1xa538FHezwC-0aLLzvl7HGDP2Nl0x3__Y4_D0zOlHo9I2soc60xzT-2Mnzo5c9asR1EQZh9gncJbWmUPvI4g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/IfTeh8xssZa_5JIwUYX8sfGCVkn95cn-wQKEI1TH0sIfLUPBK0Qh-YFIybDFbOYNxmZv2ZfMy21JxONU7LyQscziPilL3h1wfp2vpDYYg32ftq1jXDFfOgUqw74hHtjH9lQKYndOnjFe1hGsdpeLWU_RzwvsyMb3XIbbL2-VO9-mEVi_cpy8avdrlh2Tp-GHWznvIQZtcoBpv3PPrYYMR1eNv-nVH1TTYn_xspSK0Hk6GQmPgasx7YcCLH0oGgfOfRG6eWRzLtNZq0fLZVT0suWSZxP3D_HOdp-3P0Np-HuJrHMOwVObcpDM4S6UkOsFB1ZBXvhQ9fgYx-y-KyEjFg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/CpYu8YF4UTIcDaMqTcvI7jJjS_VchmoFb2LqmMmRYQYIlh3WrZdJ5K-PPkTfxJEf2QIKte-P-B08ufIjBn5gjjlBWsfTnh7si0Sk6EMmKqKKOkYULm8MbQlG3AMu-xv_GdfxsAmecJ_DLKFTFcU7sslaT0rvz-CrKrVwernlD795U7ceTAe72_71Lc5iLve5uxbAfBm8e8iF_l0ujaHuVPddjXxt0tvHGp9BjT2C5wFcXfSgjEvsgJP4Sqfgd1qafssxY3-ystmP5qRrZYBNp-wSA-4wGcZOFOxvKjx3Om_OzA4oT0CLh8EfgViN0My6yW7D_J_u5po-WO1bUwp76w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vcKw5U-jYvB2IuHlxWq1WDNBdOzWi0NVY_tT4gQiK1f0u9aIe7lW6K1s3fQgSZqHsGoFyQjky8aRyrfKuzlqnD52T_pR68doYMglrerkZpgE9EZIQn9TWt-GIbDry0sT0rfca0rse006lQmR4vQI1NtFL-N9trP9p-YrCS9ODO7BIgDo_Yl9OQg4JcssJNeTT56nVbLLT2fixk8YrmDnOuZgHW7nukZJkkII5ESV0qd4sXCTxEKNHYqGckwTrXf9-tmsEZzBjuRY1tZ2htxT8c2ltXlrjRnXj4sZbwvqdcaK3yJbvYXgBcT1F-VOUFswHcPz2bmY6i2hxxGWhsmHRw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚨
⚽️
رونمایی باشگاه‌میلان از کیت‌دومش
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/Futball180TV/101425" target="_blank">📅 11:56 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101424">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JfPbzucTC6EWk_j21DEQMrrG2FmQ4irsRRTqDFBJ9HJCxVCx-m-ij442a1_s5q87juU3XJqi6oK8MA8gdO48TTQ5fSwbeJ4n2Gqgs_rDPWtCnDs5pT0Ja25L5yXiomUR661wi6z-1awR7oydY-nXVqAD6eO2AQTA2kaLlwzLM4nnordTDfaFeCdq_SocdL5fZo3L4QK0yg7zHkOIpekeSmz3UCtJ8jKcgNVPzL8FohELk6c9FwUJaSvqbUaVeOfDGsLaMGpEYQpxTPNHOl3svudyKFviAMNLqJXtm1yrvyszty2PzPw9XlH_aH8Nii1xWvgNf7s_yEReqpOAiyWBCg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
✅
🔵
بهرام‌گودرزی مدافع چپ جوان آلومینیوم اراک با عقد قراردادی ۵ ساله به استقلال پیوست
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/Futball180TV/101424" target="_blank">📅 11:53 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101420">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/gTLprskefeT8Ogoi_acF0TuRkefYEL4YdZYZ_v-DD7THeFsOOg2MfNmFiAahN0s9ez2sNp3XtIpLyfMN4QKVi2HDAZuxzuwCBWwtRGG25hoDgXGjuByElZ37CAn7rqRmT0I0kgGYod8x-U8NBHi6NVIi2Kw4VPnYQFzI4rTDgsjOpsoj8QrghXxSq53AVunOA1dI4Yn_lg2my0MBJ83N9P1nZEVS4Mi6Vn3XIEMqbP4tM8Pr8OUfQeF8JbASRsF_H1Tx3Uycwoy4uiv7GW-4gJxVc3ETaePTdm9ZQGypZz7HdpLVGmSpl-FmX8-tRtW-ZD1MaOEPKAGyl7kMMKVYiQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/gG2FARAES4YQJCUeBlAfcscc5vkuEJP4fsqjjmb1rNR0DDAMR0NHtNU5p-tuKvgXcCgLxRpVKQTZ163UOKn2dFqgL7NoJRXbYXUnxSyAPtgxrGoQcnx663E_pKANshmff1zHK1B4F9FwSF1mZxYEMRAHI_JX8XGxQVBnnC87shECR24OQnyL_unWQ6T2A8A9jaJ2tb3Got823YbGmZZ2ud5NTrZv5tXNiW1rmznDaLM53kxGYwv4RpDYAhqafyvEzfO0LByt0C9rI2AHORUgWd_sEzY4cYyXvOn0EgcWb8PZHD8dQlBRU1feN5HimBuvzxqFO5i1dtxAzGK9jNXrYw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/WGsLTsol-q77C0kbafmi2yUnvqkxgfLKiwEw0WzdBf33kM2lJJLPR0L9zLK0z0aZ7IMcMxuGsz4JD6F8j5khLJZAv8HzChjjsA_b04yT2onpnIOExXF3FPZLiLrm90cXQCbZEYXbTysVHLXMkzdJyZx2dmeXL-DwcGacQhfs9EbN4NByfwGOM7MpONTOui-T5mwvL39FlICeY61sbu5G2ia-4HiZ76QkFtV58ZFnFaSiWwpgW6aIbUFtXlRLA2KwBK-EaFTe_YkmsWDT0pmfFxsLcLxRC5AMQChUbiZhEY2rVXzxnOGxe_sVlJUAPQW4mxBGulQoSuAfDKZEGrZmzQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/O8fYHrtYVviBeGjJopBai7LbxG0f7FU9jZZxiSqmqRj3-0yBogThxVuY9oVHUS0gaFOXTqK9RRNxOh_1xti0jGbs22bQqAfGjwyauIwbKOu9HQElUpV4j6zdo9RiLqvPNmYZretvBfJgptli1a75NwyJ9oChNKwQii6haquDhKt6qLvYEm_JMlT_F1VbTBdO4tY_bJCJeCH-RlIACOGtqCL9QeeiFo1PuPWv9Uo1YdgUFNsiXuGoKuSfmqXoV8HQBmiGp8EfpjA5PD-hENvHpH_Gyi-k7x9_mOkmqlJIozyldUuWejITtSaNnNjXdULtvBwgvb3efflCUapjKB156A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇮🇹
رونمایی باشگاه یوونتوس از کیت‌صورتی رنگ دوم خود در فصل‌آینده مسابقات
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/Futball180TV/101420" target="_blank">📅 11:48 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101419">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CznmxYODxTAuoEckl03pDq3Zxt6eWCKkhjWt7sfWocSCPQHkPPl6u6JkVv4FBBHHIY8TZnmC2QVJWDW6NbkNj-QRYInRhoK04BCRGwPaKXvODk2DSivt7Ds0BeJ3rogkl1tnnT1m5WXid_5ZN01ry06U6gZj5dznytvH7MPwAFDWF3IRfmL9tvmeRfEeqY90Ueno1UNW7sSsMzf__SVk4ApyQBO5OMqwhVghQoBDv1xXloTdfZYCYym2jaGGZKD829FvH0KqgXBwhp-gmFlD_NpP0odv0LG2b6qWnMduEytNSqu6JqMh32vJo8EEjDxE_x_wnWxEZlPrNZLNpjlL6A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
#اختصاصی_فوتبال‌180 #فوری
🔵
باشگاه استقلال با چندین ستاره‌جوان لیگ‌برتری به توافق نهایی رسیده اما تا باز شدن پنجره نقل‌وانتقالات آبی‌پوشان، هیچ امضای قرارداد رسمی صورت نخواهد گرفت. هرچند شانس بازشدن پنجره استقلال کم است اما پیگیری‌های وکلای خارجی این باشگاه…</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/Futball180TV/101419" target="_blank">📅 11:43 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101418">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4e1b98bea2.mp4?token=p6XadId7xVZnaMrDN4NPy3Zqhn2-0HZoluIZ6Vd3ErDift6qNTHFDpAp_GdFQkBs2Ty78HRPoSb0sfNLNohsYefoxO0tJjpdvSgBzUhe88tBs6IjDbH7RqO-XhAQiLxS2szvb7OkYP9HdqCbMsnnBBqo6mbxx-TbC0HZgg6QutYdvi6Za5xg1MYp3AMf1dvMCskDpABYHOIZ0Z2kyBxYaNK40ITbNbJ1P6VQinvHcDr295LSJevi_kipG5kSA-vpw8uaFPNrwv953zyRLPfzdLv5SdGHUBSczRo08sKG8MbH3syqWjOOoGCXf0CMYgJu5j5j4PdWcKmU8FF12DUrQg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4e1b98bea2.mp4?token=p6XadId7xVZnaMrDN4NPy3Zqhn2-0HZoluIZ6Vd3ErDift6qNTHFDpAp_GdFQkBs2Ty78HRPoSb0sfNLNohsYefoxO0tJjpdvSgBzUhe88tBs6IjDbH7RqO-XhAQiLxS2szvb7OkYP9HdqCbMsnnBBqo6mbxx-TbC0HZgg6QutYdvi6Za5xg1MYp3AMf1dvMCskDpABYHOIZ0Z2kyBxYaNK40ITbNbJ1P6VQinvHcDr295LSJevi_kipG5kSA-vpw8uaFPNrwv953zyRLPfzdLv5SdGHUBSczRo08sKG8MbH3syqWjOOoGCXf0CMYgJu5j5j4PdWcKmU8FF12DUrQg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👍
پایان‌یک‌عصر طلایی از سه‌اسطوره تاریخ
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/Futball180TV/101418" target="_blank">📅 11:40 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101417">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e3c9a3d75e.mp4?token=sY0wotF99L3hbP4wSQvHL9PXYD55TN6f3x3t_jDxybRHpLD5EASbqF-YYJOsK-qBQ9Qlk8FfoVz09Ea-LzPRjoDlWWzC6zRreHS5l-2fv4KDMJQc0vlNCtXmSyv_804ukvNLEjELG5zni9Yc-ya2jakRkS30kWPGQljqAVz-KHxxDG3lhhSClyMJV31yJkybPGRTLLZHo8EZpKj6UmuRSDF2stvGoKmxncQZE1Y_AnOuqpowWe8kdb_qHCxjzNn5_ObP-eJycOgl2-FWxUXizOZ--BB3lbHqp_9n-OVMq84H1NtYiKpprKrl5qOcsUikA6ezPTEma-IehDG1aQ860Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e3c9a3d75e.mp4?token=sY0wotF99L3hbP4wSQvHL9PXYD55TN6f3x3t_jDxybRHpLD5EASbqF-YYJOsK-qBQ9Qlk8FfoVz09Ea-LzPRjoDlWWzC6zRreHS5l-2fv4KDMJQc0vlNCtXmSyv_804ukvNLEjELG5zni9Yc-ya2jakRkS30kWPGQljqAVz-KHxxDG3lhhSClyMJV31yJkybPGRTLLZHo8EZpKj6UmuRSDF2stvGoKmxncQZE1Y_AnOuqpowWe8kdb_qHCxjzNn5_ObP-eJycOgl2-FWxUXizOZ--BB3lbHqp_9n-OVMq84H1NtYiKpprKrl5qOcsUikA6ezPTEma-IehDG1aQ860Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
تک‌تیرانداز‌های مت‌لایف برای تامین امنیت ترامپ
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/Futball180TV/101417" target="_blank">📅 11:20 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101416">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5fcd52d97f.mp4?token=mrI1EvxVnaZd2l-Ma2Vz16i1nwddPBNXhJyBGdwuyltEKlA-QKi2DHHBW5FQDv09iVMwz58N1E7xBeFUHRq3B2RvOtAxm19zT45rqQC0OtlR64xRww6OP7Gk6PhrjEPZfmVN7ELUdNaUI_1Sif9A826RXHJCtvdrHUwT-wEBK870nipUVlfVQ4L_SZqjo_cGlRXQjFU2Nh9PCz2JBgRcizL-Kp4s9Otx4qqDHIzDUZpDsrwSIe4djSQvlWYne3l0WDDurlEETb_sT0YuO9ZRe7UYfCshlCuHId4EeHm-95z5zoFaikyI6UN_wRhmceqYt8ptOamwtZqFW3TRz6rb1ZlpvSH8cD0dNf7BBz5eqiv_zF5PMuAluwC1yRxv8-6OB79eyBaUn5TSv7YJbv79aeGVk607hx73xxcSyyjPxA0oBqQu1yxIMbM39rR7iIxIzIiMWreNoPLJrer6CyBQzP92GK8B6cojdes5MYJXw9E7-8vrnWlOidW9OdnNDpGwNAX2FtdDJ1twYm4QjB1yaZmCAnWy_Kt_XDkpgnoQ8gYJF1jUJqR0zGT9AOhYF3DsPrwZQ5K2n8Ouf8wMKOeJMsszlrpQRDZ8iVwwj5-7C5liXc0CVVSLqrbOMN4Z_a_0rahA5H5nseisTHsxwGq81apxyTs__8xbXkWbaqJ4sME" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5fcd52d97f.mp4?token=mrI1EvxVnaZd2l-Ma2Vz16i1nwddPBNXhJyBGdwuyltEKlA-QKi2DHHBW5FQDv09iVMwz58N1E7xBeFUHRq3B2RvOtAxm19zT45rqQC0OtlR64xRww6OP7Gk6PhrjEPZfmVN7ELUdNaUI_1Sif9A826RXHJCtvdrHUwT-wEBK870nipUVlfVQ4L_SZqjo_cGlRXQjFU2Nh9PCz2JBgRcizL-Kp4s9Otx4qqDHIzDUZpDsrwSIe4djSQvlWYne3l0WDDurlEETb_sT0YuO9ZRe7UYfCshlCuHId4EeHm-95z5zoFaikyI6UN_wRhmceqYt8ptOamwtZqFW3TRz6rb1ZlpvSH8cD0dNf7BBz5eqiv_zF5PMuAluwC1yRxv8-6OB79eyBaUn5TSv7YJbv79aeGVk607hx73xxcSyyjPxA0oBqQu1yxIMbM39rR7iIxIzIiMWreNoPLJrer6CyBQzP92GK8B6cojdes5MYJXw9E7-8vrnWlOidW9OdnNDpGwNAX2FtdDJ1twYm4QjB1yaZmCAnWy_Kt_XDkpgnoQ8gYJF1jUJqR0zGT9AOhYF3DsPrwZQ5K2n8Ouf8wMKOeJMsszlrpQRDZ8iVwwj5-7C5liXc0CVVSLqrbOMN4Z_a_0rahA5H5nseisTHsxwGq81apxyTs__8xbXkWbaqJ4sME" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇦🇷
پشمام بنگلادشی‌ها بعد باخت لیونل‌مسی اینجوری حالشون کیری شده و غش کردن
😐
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/Futball180TV/101416" target="_blank">📅 11:05 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101415">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aorQHkk2Yb56wKu7ircHW_v3cDb8eH460u9MBJsEXw1Kl4X_56Re52DvSz1X-PN8X42x1k6hBMWvzu6YC83A1oFjscT999N1SIPZVJKut2IlJyrGfyvh-JMcKcy2MIkpQF5q77uWCt5l5IYvc3J2nCFnonZJcUZRvSNA88KVetdtXXDMD9_dwvYE7EIzHlUXlP85fVO1XuCdDDISAIMiOGZnNiM2QGcIC3HsiZT0UUjrvWdGmducBqFGPoggn6A8rsCFwAKN87WOwfVlLwj4f2hYyfeFih7XF3MeNC6YhUMFRvwu6bHZ6z9jSwDQE4LsvhDJz3-0JzHDp2KSlgV7pw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
استقلال در فصل‌آینده لیگ‌نخبگان آسیا در سید اول و تراکتور در سید سوم قرار دارد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/Futball180TV/101415" target="_blank">📅 10:59 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101414">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7a52a115e8.mp4?token=WFj6Sq3fg1mO3yS3orqYvwHwx4W7l6PrsgwfWiCahYBJEscxZ7jgJLtFgGSqhzjkf2QCfyPADFwwI-huZPLdDCAn09sexL2u9vHK1yQO5LYEX2ukvcoEufQ1Ysxt7fFOQGF-WDwykaIAWbz0YJjgN1tlj5B4jCTST77-PZOAlhXygXuIiyF-SMTx5EVkHSh4KlvTvdho14V4imd4Ebf-4bO7CPO0yl-XkXAJqPI1i98i_p1B6GQdrXUFYHkE-E9W_MW3rGrUySQdpDf88ND_cDhxkruFNB8YDlpJ63eyekaOqH-GYf7BcEtNcEc06JlDxEhSjjFZ5pHf6SqhRX8JUA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7a52a115e8.mp4?token=WFj6Sq3fg1mO3yS3orqYvwHwx4W7l6PrsgwfWiCahYBJEscxZ7jgJLtFgGSqhzjkf2QCfyPADFwwI-huZPLdDCAn09sexL2u9vHK1yQO5LYEX2ukvcoEufQ1Ysxt7fFOQGF-WDwykaIAWbz0YJjgN1tlj5B4jCTST77-PZOAlhXygXuIiyF-SMTx5EVkHSh4KlvTvdho14V4imd4Ebf-4bO7CPO0yl-XkXAJqPI1i98i_p1B6GQdrXUFYHkE-E9W_MW3rGrUySQdpDf88ND_cDhxkruFNB8YDlpJ63eyekaOqH-GYf7BcEtNcEc06JlDxEhSjjFZ5pHf6SqhRX8JUA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
مراسم ختم مردم ایران برای لیونل‌مسی
😂
😐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/Futball180TV/101414" target="_blank">📅 10:40 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101413">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GYyv7M5xCgEgbUSdE2YWyniTTNZ_0ZNyouxSRz8V8hKfDfjgvBR4NWdJDRkXGuc4WYrWwUqCqowd-O0O6tULS15Uzu5RQ97Pc7HSx_GbTnS8ZBAgmAH7IYOy0b2HXDRW7R3kDQ-iA5zmYvcB25AbQdA2h4oRhK31Tcq1Z-3egTDlppPeeykZAT0WNS9UaUz24l1Oad07yRuA99k65GJkqmpGjiufm1Hj46Tj3fMqMzV9pQMTEKfhxykBmqHTafHEP8yvedDVDi4EGSYNyYrvWFqRBWyMCGJBsheOliPilxKooxQhf8uxxJq4Df3PPim34KnCGbRnyium2qrX9T4VOw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
لوکا مودریچ در ماه اکتبر از فوتبال ملی خداحافظی خواهد کرد
بازی اسپانیا مقابل کرواسی آخرین بازی او خواهد بود.‌‌
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/Futball180TV/101413" target="_blank">📅 10:28 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101412">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/342ba6a359.mp4?token=bbKfR2PG2bqkBK9E3clwfF564qYsLYlRnqbvys0XWCah72nQt1yDQtTT21lQWi8pOhEQV78-GH32XDwzWiuDgvLuf4F-veXIdply9_CV6rXk_BVhuVYJ90kfyDZ4pOHepOBo2_9ASGhV7GEzU_BOHTEEPNfFRAJHpS6coz0xd6X4JKFu8o-VTxgTRu5sY02HCUzKBe3JIXOUarB1Z42tPXc1GqZU6oFr8RKN6oz42XyLKIM6Oyv64NX8YbdcWzIASNhQGBy-C-GFjRuBJMI5JUfkTfk7pqa2P7CTrwBMeMNJFhmS-dZs2z-kURhRfAphZeEVOget9iDnb3i_uVGWTA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/342ba6a359.mp4?token=bbKfR2PG2bqkBK9E3clwfF564qYsLYlRnqbvys0XWCah72nQt1yDQtTT21lQWi8pOhEQV78-GH32XDwzWiuDgvLuf4F-veXIdply9_CV6rXk_BVhuVYJ90kfyDZ4pOHepOBo2_9ASGhV7GEzU_BOHTEEPNfFRAJHpS6coz0xd6X4JKFu8o-VTxgTRu5sY02HCUzKBe3JIXOUarB1Z42tPXc1GqZU6oFr8RKN6oz42XyLKIM6Oyv64NX8YbdcWzIASNhQGBy-C-GFjRuBJMI5JUfkTfk7pqa2P7CTrwBMeMNJFhmS-dZs2z-kURhRfAphZeEVOget9iDnb3i_uVGWTA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
همزمانی شگفت‌انگیز عصر مسی و رونالدو
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/Futball180TV/101412" target="_blank">📅 10:20 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101411">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/061bd5d306.mp4?token=ecxoMq8mIhwLJzwJbHfzTmRb6bsEIzXjEJAxkHNYDvJeJqKvCdegjwbqyrlAyJfrSYRtr_GyKv8-N7YoFtqf4csv4zBm2JNZB9yrSCUTFKFJ6snyAjW6dFcuzIXF2G1iRV9coTMBRRMfSCmAEvxl-w_LWSosQ0OxBzE1ILM30YHfzg8JeR3MwpvyLLQisbxwmWkbEWnAVloqYUIKHtLZUknKgmPi-2W7aQYWg3OaPegDRurqEu2zQKPB7ouiaNGjYGaRkLNpy73Z6W5FIBB4UqAfL6285_rPBXFwLtad9V5A5p9jig-q4M_0anVYkzemcgOaieTUMmpw3gk3y9kToQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/061bd5d306.mp4?token=ecxoMq8mIhwLJzwJbHfzTmRb6bsEIzXjEJAxkHNYDvJeJqKvCdegjwbqyrlAyJfrSYRtr_GyKv8-N7YoFtqf4csv4zBm2JNZB9yrSCUTFKFJ6snyAjW6dFcuzIXF2G1iRV9coTMBRRMfSCmAEvxl-w_LWSosQ0OxBzE1ILM30YHfzg8JeR3MwpvyLLQisbxwmWkbEWnAVloqYUIKHtLZUknKgmPi-2W7aQYWg3OaPegDRurqEu2zQKPB7ouiaNGjYGaRkLNpy73Z6W5FIBB4UqAfL6285_rPBXFwLtad9V5A5p9jig-q4M_0anVYkzemcgOaieTUMmpw3gk3y9kToQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
🇦🇷
استقبال مقامات دولتی آرژانتین از تیم فوتبال این کشور در بدو ورود به بوئنس‌آیرس
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/Futball180TV/101411" target="_blank">📅 10:02 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101410">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">🔥
▶️
اجرای زیبای شکیرا از این نمای دیدنی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/Futball180TV/101410" target="_blank">📅 09:40 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101409">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">🚨
❌
⭕️
سروش‌رفیعی با انتشار ویدیویی رسما از تیم‌پرسپولیس جدا شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/Futball180TV/101409" target="_blank">📅 09:25 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101408">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EvrkVjX0EUlAyW4NPaAsaTg7QLvoL2T3LDTUUBye7VIQSpzE9Rji4YuukM8Ob-lOjuD8wpVLQMlgB29FNC8od6uxxXlFaFzuYyAQkSZncgv9bJCKWjb4lSp379oWKZKJRGo7uA4saIBYzacQaj6o4TX2d4TSI_VKGgOa33VHQ5UfVjOzMlaVrnv3gwtjzEW0q4kB33b6bE67LZ5-YVVB7wzUNBm1jYiMR9kNHoohvt5guxn3twLcETqXvptFTZljS-5EszeFTO7wFlbE57R5ailhR_iPgES2zdrw4XgzCeaj1bHe3Pjffq6JO8pX6meXj6eNU8gYf2PBGxGcNMBneg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
برندگان جایزه توپ‌طلا جام‌جهانی از سال ۲۰۰۶
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/Futball180TV/101408" target="_blank">📅 09:20 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101407">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/18768f80f3.mp4?token=K-gTZvsVY7gdczN9ITwCKO4LkzWnNrPNwkGE1oTgrJBRJdzdjksz_5t0dSsDE4qAk48wnq46jwMsiMCmDanaYy1Vd_8-0xjeTCW7wKuXi-qSOf6BaFMdB8JtJYm-U-Gbc7GjMu5tarp6LQb9NqdvkvJ5647R97ZEkSQjHxOzwx0krwRsZ6ilDMzFFmGYfTSqP3d0xEkCnISu8O3MlSvR8mF3UBvcwc_weLdlkPBro7NPXUp6_tCfEOSOLlxjjBlJfv0MnXcgkQQZau_3he4nFaRKQRk87gZeN9g5kUWjEcscSKIILN3aO1oneL8pOIf1y3L9rXsdVciHIfOks7kQOg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/18768f80f3.mp4?token=K-gTZvsVY7gdczN9ITwCKO4LkzWnNrPNwkGE1oTgrJBRJdzdjksz_5t0dSsDE4qAk48wnq46jwMsiMCmDanaYy1Vd_8-0xjeTCW7wKuXi-qSOf6BaFMdB8JtJYm-U-Gbc7GjMu5tarp6LQb9NqdvkvJ5647R97ZEkSQjHxOzwx0krwRsZ6ilDMzFFmGYfTSqP3d0xEkCnISu8O3MlSvR8mF3UBvcwc_weLdlkPBro7NPXUp6_tCfEOSOLlxjjBlJfv0MnXcgkQQZau_3he4nFaRKQRk87gZeN9g5kUWjEcscSKIILN3aO1oneL8pOIf1y3L9rXsdVciHIfOks7kQOg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
‼️
بسیجی‌ها گله‌ای ضد مسی شدن
😂
😐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/Futball180TV/101407" target="_blank">📅 09:04 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101406">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/33df2c440b.mp4?token=Jsp0cMMSzoxYt5aMKZp9GWMOvWZz3Y5vIQDmQJli02rj7EYmvOqfmL4IiU1hgrYvbUBPElKT-vOiCOEtmFnXSCRF5lKEyMSu_1uNec0Yqld66cPVZSqm85QcjwA597JsoAoH_u9r7WY5ilPZre9r4_FduJgL7y5nzK3CemER6XssTg0YtwL85k5YfDBReol5ME8DHrHo8XT3jbc2OlzifLMNKm9hZfWu6WfwIfGaIZGRxlozXJ1AozizBZ8k6s8Tm4wMLNSwMjV2SUIDa0dWbCVrBhwF1Ljma0RnO9BgYrG5EDrAQZhIjwfvrwbpEBmQw1naz7TY0iHK1YrrgBLUWA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/33df2c440b.mp4?token=Jsp0cMMSzoxYt5aMKZp9GWMOvWZz3Y5vIQDmQJli02rj7EYmvOqfmL4IiU1hgrYvbUBPElKT-vOiCOEtmFnXSCRF5lKEyMSu_1uNec0Yqld66cPVZSqm85QcjwA597JsoAoH_u9r7WY5ilPZre9r4_FduJgL7y5nzK3CemER6XssTg0YtwL85k5YfDBReol5ME8DHrHo8XT3jbc2OlzifLMNKm9hZfWu6WfwIfGaIZGRxlozXJ1AozizBZ8k6s8Tm4wMLNSwMjV2SUIDa0dWbCVrBhwF1Ljma0RnO9BgYrG5EDrAQZhIjwfvrwbpEBmQw1naz7TY0iHK1YrrgBLUWA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یامال وسط این همه آدم تو جشن قهرمانی اسپانیا شرتشو کشیده پایین و میرقصه
😐
😐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/Futball180TV/101406" target="_blank">📅 07:58 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101405">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/30588621a9.mp4?token=MxPt1CW2-8n2sxzP2_UVBLkiepBJgT5hjBpql59jwWpnheHz539D8mceV1MyG9oEpSFHUuJzuqSHBVeBD7OwsyUmy8xw2pS-QQQ23JYPF_5sQYDd0Bt5PTEEcEQG-DsIo1Vi31wv1j-q51Ze0gtBIdBkObj1RELNQ0Lu0QLY5CFXWvsyHEBY3izUq9ome3lhaNUiVK1z7zBoCZ0I7VHRk78GpfzqCkg4Z2zsW57eR_oxL1ZaN5MeiNv7k8o27kWnOWity8bHA9wSi2Oz4zwamev1B2DwAPEDx4DzFZuAu0E7pV26xGrsVXCq1osou6JdHKAnkcW88bCHwkA0ExqXuA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/30588621a9.mp4?token=MxPt1CW2-8n2sxzP2_UVBLkiepBJgT5hjBpql59jwWpnheHz539D8mceV1MyG9oEpSFHUuJzuqSHBVeBD7OwsyUmy8xw2pS-QQQ23JYPF_5sQYDd0Bt5PTEEcEQG-DsIo1Vi31wv1j-q51Ze0gtBIdBkObj1RELNQ0Lu0QLY5CFXWvsyHEBY3izUq9ome3lhaNUiVK1z7zBoCZ0I7VHRk78GpfzqCkg4Z2zsW57eR_oxL1ZaN5MeiNv7k8o27kWnOWity8bHA9wSi2Oz4zwamev1B2DwAPEDx4DzFZuAu0E7pV26xGrsVXCq1osou6JdHKAnkcW88bCHwkA0ExqXuA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🤣
ناراحتی امیر قلعه‌نویی؛ برای اسکالونی کلیپ ساختید اما برای من نه!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 28.2K · <a href="https://t.me/Futball180TV/101405" target="_blank">📅 07:25 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101404">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gmD_LisH3KNIivEzD8UYeabt66EtFlDVJEIPeu0_ZmJTb5ThSJom8eNsP3l1mJJMBlOlZNTEqgMxBQR2tcpZzSQY9nvku08JN2TtR8V9oafiz873FOIOBC3xNJnZBEJ5bVW8UwVowypXvTU6blHYas51jaIjlkBdDjb2HN3QI8BZyUsYLAOSzseLjlDN3JPXQfMIVTC_nqp8n-eicnpYxzBBD2OzWUVz620ngqvOFOnC3VWiy3THUchXY89w7u_dNoCAbd3sQrUIZVuVX9xyR7noujTFPhTB0pdC2c1NX2sAq-feqhem6_dAxNKYhf5tWhK0F3GmJVJnMHEg5yZ9uQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🇦🇷
فوری از هرنان کاستیو، خبرنگار آرژانتینی:
لیونل مسی به هم‌تیمی‌هایش گفته که فینال جام جهانی، آخرین بازی او با پیراهن تیم ملی آرژانتین بوده.
😬
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 30.2K · <a href="https://t.me/Futball180TV/101404" target="_blank">📅 03:08 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101403">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HoMc8foaLwIXcuDEF-WaYGFowf8AwBVv4g-gu_B4hXK4fALX4zJV4N07PoxvL2IWOIuyQf9__69lbVap8ghND84Y31jGcZGaL43P-aZ9eyWV905DS0a5dglzAVe08NSJ-N20i4YCoeDEZtZct2Mtu9mGgEo0JwvM7MhxSW1Ylftm-yG5EQmQoYI4ErmpwTD8pANkYkzwmZQ8hiCTg4yzt8u_a7t7QDBUOG0d1-MaoySstJT_0kDyXHGpHvOc40TpG-U15aSx5bJ6zgHCHSjm-uyVGevWrjEZkqr2xQWMHbUaahh9RT4rd5torR6U2bKvMggKw_cSYSIdm3uDHZjKjw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇳🇴
||
آمار و دستاوردهای ارلینگ هالند در دوران فوتبالش به مناسبت تولد 26 سالگی‌ غول نروژی:
🏟️
[419] بازی
⚽️
[359] گل
🔴
[66] پاس گل
🏆
لیگ برتر انگلیس [2 بار]
🏆
لیگ قهرمانان اروپا [1 بار]
🏆
جام باشگاه‌های جهان [1 بار]
🏆
جام حذفی انگلیس [2 بار]
🎖
کارابائو کاپ [1 بار]
🏆
سوپر کاپ اروپا [1 بار]
🏆
جام حذفی آلمان [1 بار]
🎖
جام خیریه [1 بار]
🏆
لیگ اتریش [1 بار]
🏆
جام اتریش [1 بار]
🏆
جام اطلس [1 بار]
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 30.5K · <a href="https://t.me/Futball180TV/101403" target="_blank">📅 02:47 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101402">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Z7MZDHDh-puiwdRXyDt6WW8eW6vH1RuxwH-M2iVXMbSvbFwEhnl4J9I8591e8-m5QH1mlnW1rOZ7XCK1qj_of7hISx1qU63TzpRM0BpadvUAshBUU0lcVk9zD3Ldc4ApT5fKV1t63CF_aQxjmsKsjWd_3TH7BdRN9ZZV55xHwffM2g__TGBGfGao8buDAwKzbqH7jPa7EV_mp674WrtchsLXcOrlUyMafsTlqqx0BzHjS1LaprdQE0rAU4xnAa1_VQbza0edIHrJsQqpIJ7R7PvgIJ6O_f6MiJ0srm7ytpGZ7dmG44aGbFvkxrdWztYEaU8Gp6Mlqckhs9LsXLP36Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
‼️
گلوبو برزیل: ترکیب بدترین بازیکنای مطرح جام جهانی 2026
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 30.2K · <a href="https://t.me/Futball180TV/101402" target="_blank">📅 02:29 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101401">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">🚨
🚨
🎙
عادل فردوسی‌پور:
افتخار می‌کنم دایی و باقری با یک تماس آمدند؛ یک ریال به هیچ میهمانی پول ندادیم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 30.6K · <a href="https://t.me/Futball180TV/101401" target="_blank">📅 02:09 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101400">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pmt1740n5rk8kSzKyK3dFXnunnnkKOe7YGM2yDEPMYdiyqxgy265xTsWidxCqiiwdjEfdMTlj5bnxL5caSvWHrV7sbQPdYLosRYzb4OfDmqp3gbEJ6A1eFKUJAfVnIgVo3e1SzJ20Z8mo7QpyRFcX5C4ng15pk4rdTFXYELz6gDlK54bC2g2rxfNKdDuQZJdNOhcvmcMIhUloO-bYJRQwoCI8TLZJ9k_ve6JnF6QziP3_htwq9AHQwK1GDlS8apg_o7z6dsHvlXQ6axPzRZH9DtFqwnW85rix9PmMvv_vJ6t69U7TgXCRxfjwhKtwRkP-3G0QlWmpo3jrraCIMmXZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">😂
😂
😂
اسطوره وینیسیوس بعد عمل زیبایی در برزیل:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 30.3K · <a href="https://t.me/Futball180TV/101400" target="_blank">📅 01:51 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101399">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">🅰️
🅰️
🅰️
🅰️
🅰️
🅰️
✔️
آپشن های متنوع پیشبینی
💥
برداشت سریع با کد پریمیوم ووچر
🩸
هدیه 100% برای اولین واریز
🎁
25% فریبت ورزشی برای واریزی‌های ووچر پریمیوم
🔝
با ضرایب بالا، بردهای بزرگ را تجربه‌ کنید
1️⃣
لینک بدون فیلتر
1️⃣
ورود به سایت با فیلترشکن
••••••••••••••••••••••••••••••••••
💠
لینک اخبار و هدایای سایت
👇
👇
🔸
https://t.me/+ioIBrQfqMLtmMmEy</div>
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/Futball180TV/101399" target="_blank">📅 01:51 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101398">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lrHDN_wv5TyR_UKpkj1zJXocIfJOeUJmZIddO-nEJ4u-TE9pk69XQFz1lRINYwKACMcTX8leGoHtqbIHOiod9MzXGhLg7w3vksBpoLJs1y0Uklo0xSZ808oHzrOZVe4bpbbXyjwKD9vvpTf8KsMcoMU1l5hUufj3Sm7XAu2nSquXOaw4dy66xVr0VuNDlttYbMDUtkR5wDvIjzFBKVQCRXG4ZS3bNyYEhZpNv0LNDJPA-TDissHeb8KXiw54MqnfqNCr7Y8df4N3G1qG-f77JIQIPQyh0qm8gjZ0PDTGsikFC9bW3ETJjowWQX5Uvc04RqnLUbZoi6r21K1ZY2Z76A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💎
سایت پیشبینی
YekBet
💎
📣
یک حدس، یک برد، یک قدم تا برنده‌ی نهایی
💶
تورنومنت
صد هزار یورویی
گل یا پوچ
رقابت های بازی جذاب گل یا پوچ در کازینو
creedroomz
⬅
️
برای ورود به تورنمنت کلیک کنید
1️⃣
لینک بدون فیلتر
1️⃣
ورود به سایت با فیلترشکن
📲
@yekbet</div>
<div class="tg-footer">👁️ 28.3K · <a href="https://t.me/Futball180TV/101398" target="_blank">📅 01:51 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101397">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e202619a75.mp4?token=N6kOLUoS9JVSJKtG0EyTcPDOaC7RypwLDENedpxCnFHW27Mho0d8n0JMwqHkghycmEBkvNA8BIoAjUAsvkLQPaNKKY5gwXvlRPnOdiMzWMYrY5f0J_uXMqAMyAotbY2z3VNeUAy4z9afubK17yRPLYcIREB41IzJdrOyg9OOyj4EYuvHWVUXczOomzRXzVBzErBdcINknUVN30aWF--LNBR4fSLY679vipnGf77WTUXe-H4MdpklCs9dJ9XMcFSBr9Lo74WzWwg-uP_JWfLsWyIaMWjy3ZPhF_gaCrSBvRIyrDxNdk1k3q93EWKj2KIMXn090Lk5PybzNQmHz0Ap6A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e202619a75.mp4?token=N6kOLUoS9JVSJKtG0EyTcPDOaC7RypwLDENedpxCnFHW27Mho0d8n0JMwqHkghycmEBkvNA8BIoAjUAsvkLQPaNKKY5gwXvlRPnOdiMzWMYrY5f0J_uXMqAMyAotbY2z3VNeUAy4z9afubK17yRPLYcIREB41IzJdrOyg9OOyj4EYuvHWVUXczOomzRXzVBzErBdcINknUVN30aWF--LNBR4fSLY679vipnGf77WTUXe-H4MdpklCs9dJ9XMcFSBr9Lo74WzWwg-uP_JWfLsWyIaMWjy3ZPhF_gaCrSBvRIyrDxNdk1k3q93EWKj2KIMXn090Lk5PybzNQmHz0Ap6A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🎙
عادل فردوسی‌پور در ادامه: من بله قربان گو نبودم، نخواهم بود و نخواهم شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/Futball180TV/101397" target="_blank">📅 01:42 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101396">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fbYNLj5LJEbGOqkWJ_57qQF1u0rzIzhehvx_zH8F-M8zPH_hmYSsIBS4shogS0JYRXumTVRh2ZmAJcuZbN4Aej7MjvMmu62bOcxYkV16sA3HxfW3B0l9n8-CER_BgepbAOsUtVQz-hRneO06KoQP5lf1Ild5lea40-Kr7hq9db_RXAecRjJI9wnUkmrISP9zx8H0b51pUpAtVI90W8QeACdR_VUcZazHYkcp9TqjX-ryGNz71CdnmOggi9FguBmnmwV4K4p6wHFifZEx7NzF0j7S0YEVXjdfMYj0Bp8W-qVfX7oOVysysDv-HUpwsk2D3EOxjP-OyjfXlrDwPkBRBA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مسیر قهرمانی اسپانیا
🇪🇸
✅
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/Futball180TV/101396" target="_blank">📅 01:36 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101395">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/135a7fe008.mp4?token=CH3bkQqlLtoOpK6kGjQURfXwwpZT6R-zv62PDIopPaxbncJJJOmFUx7xKNPeeVsVt-qY9jvMDQUXbpAC5MkhoO-CvKESQp1WD8igy9BWtbwwayf1HEi59aIhJPlFIOyCB6LmVOSqVzCiYtj8i0fi3L0jiuRAFKJ4rLgKsiXkX2pg0bz6EkV2EaBoTjz71DlZUhC7WhV-PHQbj95s3P8r6LAqHoHg6t1HDf6y_685x9jFClCLmgwLhXT0mhYq7HyKKm817KYk8odJaSrXPCKEmFHLXDHPJRNBl1BgW8H12ZfY4uJvob4on1VROoLRLptY2FaAODPvmiG0YWh-9zNplw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/135a7fe008.mp4?token=CH3bkQqlLtoOpK6kGjQURfXwwpZT6R-zv62PDIopPaxbncJJJOmFUx7xKNPeeVsVt-qY9jvMDQUXbpAC5MkhoO-CvKESQp1WD8igy9BWtbwwayf1HEi59aIhJPlFIOyCB6LmVOSqVzCiYtj8i0fi3L0jiuRAFKJ4rLgKsiXkX2pg0bz6EkV2EaBoTjz71DlZUhC7WhV-PHQbj95s3P8r6LAqHoHg6t1HDf6y_685x9jFClCLmgwLhXT0mhYq7HyKKm817KYk8odJaSrXPCKEmFHLXDHPJRNBl1BgW8H12ZfY4uJvob4on1VROoLRLptY2FaAODPvmiG0YWh-9zNplw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">لطفا هوش مصنوعی رو متوقف کنید.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/Futball180TV/101395" target="_blank">📅 01:32 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101394">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">🚨
👍
بغض عادل از صحبت‌های حاج‌رضایی: جایگاه اجتماعی با پول خریدنی نیست. در آخر، تن شریف باقی می‌ماند
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 28.1K · <a href="https://t.me/Futball180TV/101394" target="_blank">📅 01:25 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101393">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aWmc_qgKZT2qy75gJKDy9rQhoGCxd2KdjxupNnpRWwoBlncZLSEgxNo9aa2PX5yuWU5J1OReJAD4Th-408B8oP9mQAqqUcppmC5x_OYqz9vtePC_1T40pc78gordb_cIxtxi5LRIAg7P8kBMqX6bb66_xAkgryUEX362it4h03gbbKg7qiF1ulWDP4SxMMrVHoO5ciuQQzwzULiRiJ6RFv_Qg0TKKr1aF_0ItvUvP0VEtE7leETpUnAmO2Tfhd_jgYzwGa9rw6aKhM622TJzG6OjPnKVyn2KyLFgfdXDUTtzBWMrrwrh-Vb3UxXKSTh9C-kBrL9VTr0Ze4XBRNF9_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
‼️
توضیحات عادل فردوسی‌پور در لایوش در ارتباط با فیلتر شدن 360: بدترین راه رو برای ساکت‌ کردن گروه من انتخاب کردید!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 29.5K · <a href="https://t.me/Futball180TV/101393" target="_blank">📅 01:13 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101392">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WKGAKfueCBxj4x6mczwQYNCn57AVqKezVGW8m4yaZQQCwW9MQeeZZQJh746Y7A8QZx9u592V-c6c2O24cKZ33UWovkFmmMsnIJudLYeEoaAv4JORZm3eSDvrgxHWt53i00i8YlUo6KWnLsU23U6uM8NT7630Hgm_X7j9A6EfHxhGK3k0LxSfxQp89xDhPxerhwpUihO2Bse6YCmxapKLw-Xv_w9uWzSBYNjqSdWdDHmSSOyY3J2a0AXaq6d_bxFuieeLIumbQ7dXNKy_XdMWlx_C_V_caBbhddm8g-bynFwsJgeZo8nrTEBoaYFGam0xEvrSflJjdMFn2_a_qvbyDw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
دی مارتزیو: لوکا مودریچ و میلان در مراحل پایانی تمدید قرارداد هستن.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/Futball180TV/101392" target="_blank">📅 01:11 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101391">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/MdsyWjjvutLP7opQ84MnOAE598IEtpMAj4hH324qv8zHC2lMWGHqsMF_NGSmjXrmvBd48IZ7NkSA9G-lN1AUpc-4TQ4O9H8biX6iSCGRRQEXxBRN23p0d--YBporkXGafd9SVQHiK_dfmFcbEfhdh5S24F-XiOgpdz4O2snRz_fab292e2QObpFcjg9sAJIBMTj5VKNPJ4qtlhsKR7IJQuL1NOGslzyYYc99RyG3tVj8bba9bXO7aiDoMqoRRYnNOT1_uJlhcoDUxo3IAEK3Rd6iLngny31PQcCXJPubAB7JClBxVVpAN2VcSfktX8TiWZHnbi__giVb78yDJgC2ng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
کیت جدید اسپانیا با دو ستاره
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/Futball180TV/101391" target="_blank">📅 01:06 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101390">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8d1fa4b0ee.mp4?token=D-bXmhgHoboxXEwDX-m8H-1H8XUHPEnYtFj19TuI-rzCnk_LoIktl16aDFf9vOXWvWPjbr-KyRjsGHRhPm6WYOkSP2LfeE9_NZs3A7jK3F_8yQTP5Qh_Ij0dN7z8Ge4wnLSlxaz5Ts4b1k_a8jrO92gmBwcUJ3Ln1Fgn60O3CB-BASjrv8N-ivMxeenjkA6Jo9p-QkHa62l2A1_ekm8ClUCxa6Zk0Sas3azTJdX83qTDciQ5ctCMiJ9N_gDlhN6WZTNrc5ylC0j03pxGC-L-Yw8AA1crOEYOIfBvNqypvgthpBSFCunD_Rd02k6Cq92L1BYhqxuBYq8DL-U9Oxw1Eg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8d1fa4b0ee.mp4?token=D-bXmhgHoboxXEwDX-m8H-1H8XUHPEnYtFj19TuI-rzCnk_LoIktl16aDFf9vOXWvWPjbr-KyRjsGHRhPm6WYOkSP2LfeE9_NZs3A7jK3F_8yQTP5Qh_Ij0dN7z8Ge4wnLSlxaz5Ts4b1k_a8jrO92gmBwcUJ3Ln1Fgn60O3CB-BASjrv8N-ivMxeenjkA6Jo9p-QkHa62l2A1_ekm8ClUCxa6Zk0Sas3azTJdX83qTDciQ5ctCMiJ9N_gDlhN6WZTNrc5ylC0j03pxGC-L-Yw8AA1crOEYOIfBvNqypvgthpBSFCunD_Rd02k6Cq92L1BYhqxuBYq8DL-U9Oxw1Eg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">کوکوریا با صدای معروفش در جشن قهرمانی
😂
😍
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/Futball180TV/101390" target="_blank">📅 01:00 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101389">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">🚨
🚨
🚨
⭕️
شنیده شدن صدای انفجار در شیراز و اصفهان
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 29.6K · <a href="https://t.me/Futball180TV/101389" target="_blank">📅 00:53 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101388">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">🚨
🚨
🚨
🚨
⭕️
گزارشات از حملات ارتش آمریکا به بندرعباس، قشم، سیریک و چابهار
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 29.1K · <a href="https://t.me/Futball180TV/101388" target="_blank">📅 00:48 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101387">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bfTBQ8B8MSLDhenPeUz82CxPWvrb-B7myXcLw23uUQQiPeZIpeO-TODIypqaxjAPA-gnar1LrUN21pewybjbHWRT6Q55qs4Hfpv56hjxTTq_r-lHv3KBfoO-Y3BGoR7Im8-DlsqNNghT0lJl6scEPnDZ7uT-EFF7ba8MJvgkK0gHdr9bdxabOcx9H8XLQAx4fW6OknRFpyW2uC3yQAddd5S4iqGNDEOmygyo6MArTM4-X_7EOqE4QB3m8DPFoY2wmYRoAmP1BIyvc4Fxef3QT7pu91wb6CHxc0myLPO0Q3iCtKmxLJ97TAc6zTmRVnck5P5jR0FhOlUi6Au9ernacA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
تی‌ان‌تی اسپورت: فینالیسیما بین اسپانیا و آرژانتین در ماه نوامبر برگزار خواهد شد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 29.1K · <a href="https://t.me/Futball180TV/101387" target="_blank">📅 00:37 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101386">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IP0a22ImTMx0dWtiS4MU2UVx--LJ4L1u0UtENZgrlpFsw50EuKKkqEDTm3Ag4n9KPjloQLuQ6dSOdve7YtfbAHmKF-b8KeG8OJYFQ-YKf5iwqfPc9pySnmeRg7rFh7GNxA68cFS6NrTwAePmV3VdKh99NbVzXmfgJEIoIka9dz9zUELMSH-leox7l06mioawOHEZiXqQLUwMqPVppDWh6LtX9y8-DJqokGqIu_pSGpguG5D4YVeJ9Huy_36dH-qXkVvsd5bQWa2R-ipKone7dhLK7QGY29RhmlTo4_N1JRvK7M6vld_p71bt6ElcWqR0M3XN_lqK5tLnMpDxYNL1rg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
📊
🏆
#فکت
؛ پشماتون از معجزه خط دفاعی اسپانیا بریزه که اونای سیمون در کل جام‌جهانی 10 تا سیو داشته و کلا هم یه گل خورده درحالیکه مارتینز فقط در فینال مقابل اسپانیا 11 تا سیو داشته
‼️
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 28.1K · <a href="https://t.me/Futball180TV/101386" target="_blank">📅 00:29 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101385">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/VUPV2J3V8NovMLsvsYVC3h2-fVDXYARXpZuWt_8yMtoWsUwUBvCtWouqRjHjEoAcc_mK_tKEcsDUMSNZWmbdRlVUib4sCuqWHuSbLdlf5qZz-5zmT887Ut8hO9OuJcpkYf1HyCKiNsNrFjroIi9spwrYo0YEpBfT7iwHpURLDZS9uE2MwNUM_w0okI_hlBW1U7qLA_ebTs3kOj-JjeF92qK_K7xt7prEphnQkVWub8-2xgsy4jUsQcTxD96_hABoJhZ60WTEcKaLj3ZyuaPmYVZSyuKez3v10UWzXwrFDCkb4TGddBlFf2V1jKiCl-i3XNyJapr5jB0HAMaPo57UEA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کوکوریا تو جشن قهرمانی اسپانیا
😂
😂
😂
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/Futball180TV/101385" target="_blank">📅 00:28 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101384">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/qLe3jeotdcqn4s59M3QfZ8trIyoCWyuZJGwRXAVLlLcogkVzsNJv4PYMmn5bCF19cxt3-NLpIIrIxiNdDjr_CkwTLi_wljVF0yd2Y11rhiG1jZl14Q2ysVRWzWlasQCZgFJew0fBdX2SI9BPVml7DYCZ-ZIo546Qj-DsmUyD7xyi8ZuuIwaINCKjZeQJBDUZ_ZO2mztZjJgaVOAV0OMYl30JDuX6vBMyH5K-Zkg7MCGElZP5vPCfyvgrsDJk9Dd90NFh4Wa0CUmvR69fwc6I8BVkG8xFZ4nar6YiKZE1crQQ01Ol5HAl7HhPoeIIiUSx4679QM7L00gEmpzLkjyJQg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بانو شکیرا با کیت اسپانیا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/Futball180TV/101384" target="_blank">📅 00:27 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101383">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2968949297.mp4?token=NfmrTx9AxKTKBw9c8INftioJ9lw126JHXBHdtqmqTpFxzfjwdMR5q_IZOkXoOpXa3sd8b6JA5dY6nPUoXC8zfgKASRFZiaMRtAgsYUhLGUQ1FEShB2HHrdrQO6YmrhUxe_9QJzRBmmM_SdpUq0Tm02lndWuilLh6EYSDKOSw5p_O6WKSykxUXWNKpTe55asFzH97Quk6RMgLN6hL-MOSDhsYNZCjipNEBHl0tL7SfIaW6b6bALqmXU7s2WSi3O2AasSpjdzKXYUxH30mUh9eZ8zBwfd98PXlDA2APy8NbNzqnzh81We6FSmqpgR7djXsZ1VFniI_Kuk7bUaQPrBpxw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2968949297.mp4?token=NfmrTx9AxKTKBw9c8INftioJ9lw126JHXBHdtqmqTpFxzfjwdMR5q_IZOkXoOpXa3sd8b6JA5dY6nPUoXC8zfgKASRFZiaMRtAgsYUhLGUQ1FEShB2HHrdrQO6YmrhUxe_9QJzRBmmM_SdpUq0Tm02lndWuilLh6EYSDKOSw5p_O6WKSykxUXWNKpTe55asFzH97Quk6RMgLN6hL-MOSDhsYNZCjipNEBHl0tL7SfIaW6b6bALqmXU7s2WSi3O2AasSpjdzKXYUxH30mUh9eZ8zBwfd98PXlDA2APy8NbNzqnzh81We6FSmqpgR7djXsZ1VFniI_Kuk7bUaQPrBpxw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
‼️
توضیحات عادل فردوسی‌پور در لایوش در ارتباط با فیلتر شدن 360: بدترین راه رو برای ساکت‌ کردن گروه من انتخاب کردید!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 30.4K · <a href="https://t.me/Futball180TV/101383" target="_blank">📅 00:19 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101382">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0990cab9b2.mp4?token=uwzp_4EVO8yIZ_CGSH8Ug7xlvjuTzWT47zpqjjzk8Vu54OmI7UL-h9BPWy5HS1jMklG14sFJmcCC6gOU_mETExY1VIoQkle2PLAs9OBaIkVPDi4yQFw24Ybi_zxIqy1Bda-WSsjaaAVVj0xzcavG5wSBggbBxMjPdocfnVdG68FSchPaUPuyMLcWvedGt6nlqpPod18CGqhl2JtXuuCPM6zMI64P67zfAItpaFe3VvjcVRjcJOwDnsjaEiJ-m0IvXh7i4zWpf6vr3IQ-r49exHOAOo_4wuZGKGj0oNCfNM9PCoPMw_Wr3ePvNzLSvoZzEAaHIbEGIlIMRldNFzngBA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0990cab9b2.mp4?token=uwzp_4EVO8yIZ_CGSH8Ug7xlvjuTzWT47zpqjjzk8Vu54OmI7UL-h9BPWy5HS1jMklG14sFJmcCC6gOU_mETExY1VIoQkle2PLAs9OBaIkVPDi4yQFw24Ybi_zxIqy1Bda-WSsjaaAVVj0xzcavG5wSBggbBxMjPdocfnVdG68FSchPaUPuyMLcWvedGt6nlqpPod18CGqhl2JtXuuCPM6zMI64P67zfAItpaFe3VvjcVRjcJOwDnsjaEiJ-m0IvXh7i4zWpf6vr3IQ-r49exHOAOo_4wuZGKGj0oNCfNM9PCoPMw_Wr3ePvNzLSvoZzEAaHIbEGIlIMRldNFzngBA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یامال با آهنگ معروفش رفت بالای استیج
🇪🇸
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/Futball180TV/101382" target="_blank">📅 00:18 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101381">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">🚨
🚨
🚨
🚨
⭕️
گزارشات از حملات ارتش آمریکا به بندرعباس، قشم، سیریک و چابهار
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 28.1K · <a href="https://t.me/Futball180TV/101381" target="_blank">📅 00:09 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101380">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0fdecc8438.mp4?token=q7G1ZrVF4ocBNsDy4nbW-BdQJs2HEzI76_arG6iHfyAcVgs4Xb-yQWLwXWczxERSWkAPM-6_U6RRiQJj8ISV-hWkw7FgZkxJAjl0pnmCMFttc4pWcsOFGAdh-nxqMZfr35rrf7Pu4_QbcKAjGplPBmF1fA4QLK2bp2NtGlhZLAYJUyb6gzLDEVDRcTf8vyor9yiekAUxbuLz7zMrDHFG1QzdmQIkhOw2zsuP_7mFTW5ZYWU4qb7zZ8btWhga71KzYaegvyX5WqVYT2FrTS_QX9d57IXgg-kNIw4xyL8NijjiH3DU6ljK83OYk0Y2-YVRknu_jw1CObykj7I7eXkqsg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0fdecc8438.mp4?token=q7G1ZrVF4ocBNsDy4nbW-BdQJs2HEzI76_arG6iHfyAcVgs4Xb-yQWLwXWczxERSWkAPM-6_U6RRiQJj8ISV-hWkw7FgZkxJAjl0pnmCMFttc4pWcsOFGAdh-nxqMZfr35rrf7Pu4_QbcKAjGplPBmF1fA4QLK2bp2NtGlhZLAYJUyb6gzLDEVDRcTf8vyor9yiekAUxbuLz7zMrDHFG1QzdmQIkhOw2zsuP_7mFTW5ZYWU4qb7zZ8btWhga71KzYaegvyX5WqVYT2FrTS_QX9d57IXgg-kNIw4xyL8NijjiH3DU6ljK83OYk0Y2-YVRknu_jw1CObykj7I7eXkqsg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
🎙
قلعه نویی: آمده ام بگویم شرمنده مردم ایران هستم می توانستیم مردم را بیشتر خوشحال کنیم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 28.5K · <a href="https://t.me/Futball180TV/101380" target="_blank">📅 00:01 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101379">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/N-dZS_eq8Icyp_U84GZ_DaWYA1D7hDPMYmVt5S3Imdcp2AqnwYTuaMR782HykAGds8Ht-vrW6P0Z0rDRDEB2WNt7d4kazmMMxUkeNhBGrtKnmvPgbmXZixVf7r574YwgRX5v1fu5l9jOtQAI3I6r0ZEdY6tAa_bo_zZstcI3VuuVSu6i25heCQjXzokbmLNYljoxaWuKcO7E5c1PQp6DWeOPCoqqv7gncVZj6unRWyKOFvcpMhmsaescv-WxRxCtS79cIo2lxxvuZcyzErXlNeLxg5c0ogRI_vX-9uz_8FrENhXqTy_IRmZDVZYcFBT_aqML5IojiXiEWD12vKHL1A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
به گفته آاس نزدیک به 1.8 میلیون نفر در جشن قهرمانی اسپانیا حاضر بودن
🔥
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 28.4K · <a href="https://t.me/Futball180TV/101379" target="_blank">📅 23:56 · 29 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>

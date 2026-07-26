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
<img src="https://cdn5.telesco.pe/file/tRDeUf4nd-Hd2dQli_4ieI5g3K2y7QIDthao4l0wpJEiRhAPgQmfqD0tQpclN2B8KMteoXTmcIFCWwQ3rYFWJX7kBPaSpOyUIuWt1xLsSkYi6DTpx1W6gLgcJbY5Y314h_tjhRgvrwLW8mdkmYD2gChVXAN0XDwEWnH7NgMQ9HeNCnwwsAw3xWG6f1jBCyCtu37CDRltWicqak5h0aLXisJdgJ-C8jLcOAaOUyd0kYAONl5x354HcM6ejViEfo-jH3w9Wz4Xi8IGvmySLS-aZobiSoomXW_wlsTVkTK8pIvarPN2p7so0LG1kkgZrnAJamWvjI8gTaRJUvlreJ7mXQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 فوتبال 180</h1>
<p>@Futball180TV • 👥 526K عضو</p>
<a href="https://t.me/Futball180TV" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 In the name of God; The only popular sports channel on Telegram: All for Iran...🖤We respect the copyright laws and follow the laws, Mr.@Durov...🙏🌹Contact ads:@TivaAds</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-04 22:28:22</div>
<hr>

<div class="tg-post" id="msg-102023">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9274ecf947.mp4?token=BbDyRDe2uaPqO9h_XTou3bFQrZ4JUgHDPZdBDaTVkPAxalp9waXzT0xoB3CacwpV2XNSQZ9UJqS_azxz7pVDSw7z6R7PjF8EzwuJ7nFK2dUVvsaHbw0SJ7fUA62T08kmED4XHITlmySChw9bx4dVGtWbW_rn6i_jXeq0K91NQhAf6giXZrj9OJ5v-EOqJY4MSyvuqWoWYWcYm3lnE5I3S1I8hLTMqX1Z413MZhqfmSvDpLYWcsr8TBKFMHr6A3fGsWEHppFmFUnMl0FHsjjg0yDCMPyKnr--Mt8aEVVaUBRl44kdYUmoBF-tJtOlUMlQ1wtcw__jh1vk_LgnKWoWYylSb-5XafBgReHqfHyBKfeYI5QbHWo3HW_ebK16Zg5PI6ZlPZNBtueQHRtcoEjVWluY_SM0IHmuIhJEz9lKLk_z4BpMkfV0hGQpNyFtZZ5v4oOOz6JjVoF2T2RjIyrj9crX9Q8AVCZlTdIqNah60COUJh25AhQIMeSE1pWZQHxlKGw2tUuOSc6e438LT4dSUzC6ktSGMeTc85YwBRkTBP3PvHufrlkVQsTQppEdS-X3cG-rEXYiy62eirBy3FMsJ-PWk6AoNf8MRNziO_fqzLhaaoGn8pLVctv6QZdToSxhn0pfh0j0x2xN_V42pah-Qkl-SVNVGLHMJ1RJmr08dQM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9274ecf947.mp4?token=BbDyRDe2uaPqO9h_XTou3bFQrZ4JUgHDPZdBDaTVkPAxalp9waXzT0xoB3CacwpV2XNSQZ9UJqS_azxz7pVDSw7z6R7PjF8EzwuJ7nFK2dUVvsaHbw0SJ7fUA62T08kmED4XHITlmySChw9bx4dVGtWbW_rn6i_jXeq0K91NQhAf6giXZrj9OJ5v-EOqJY4MSyvuqWoWYWcYm3lnE5I3S1I8hLTMqX1Z413MZhqfmSvDpLYWcsr8TBKFMHr6A3fGsWEHppFmFUnMl0FHsjjg0yDCMPyKnr--Mt8aEVVaUBRl44kdYUmoBF-tJtOlUMlQ1wtcw__jh1vk_LgnKWoWYylSb-5XafBgReHqfHyBKfeYI5QbHWo3HW_ebK16Zg5PI6ZlPZNBtueQHRtcoEjVWluY_SM0IHmuIhJEz9lKLk_z4BpMkfV0hGQpNyFtZZ5v4oOOz6JjVoF2T2RjIyrj9crX9Q8AVCZlTdIqNah60COUJh25AhQIMeSE1pWZQHxlKGw2tUuOSc6e438LT4dSUzC6ktSGMeTc85YwBRkTBP3PvHufrlkVQsTQppEdS-X3cG-rEXYiy62eirBy3FMsJ-PWk6AoNf8MRNziO_fqzLhaaoGn8pLVctv6QZdToSxhn0pfh0j0x2xN_V42pah-Qkl-SVNVGLHMJ1RJmr08dQM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🎙
آنخل دی‌ماریا: مسی نشون داد که یکی از بهترین‌های تاریخه و تا وقتی که خودش بخواد میتونه همچنان ادامه بده.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.21K · <a href="https://t.me/Futball180TV/102023" target="_blank">📅 22:02 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102022">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/D_ita4ixEJYZOJq6yoLCs--evlJZ_dMw23E7cT2kcRVbaeC5U2EtQHUlmSIOkE57bbkwvdBn8wtEaOdkuO2C88fSJHN4AsqTQq2MElKTinqm3R5-AQyWXiwH0eEc-D7DkiX8444cB-0qBTW-PVkxE7w43-FOjgE3RNa33oxn0lAgeBib_FWyRvqp7KgFAtrqiE7VIBCNUUUJqYvTmEe0RG6jPH1kiPGr4JM0c2sDZechUq6IZ9locLS8T_TQ4TlMKQJzXAcbyJ2V0_6cEcXCVfQf5ButoCwHRXB44SGisQqvcHOJvFt2igOvtT55pRdZj4iOXaWdzEnDgn8ueVSAnA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👀
⚪️
عمق اسکواد رئال مادرید برای فصل آینده
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 7.49K · <a href="https://t.me/Futball180TV/102022" target="_blank">📅 21:33 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102021">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4e76692a40.mp4?token=joDSwv7XweHfsH3poL_bUo1BRbFi8ysrlWRHu8nWMf8E_Sdd0TPrt_NDW-tkqUviEKd3SEzG4a3iEhaugWQid-tYm6560WMLQpUXpAp5clRHJqvQSJTTvTgShs5K3ick14nHYzYWmKp1yBYsktJZ8lZ-Zd906pgp2SpT-J6HLniqH6uuST2bouZbd73E4SQFqO9GYINZBR3aITKOV89UBMQZMIm3bDTI9_NoLjYOAQMSa-ZuWgCfrZ7SLUnGlZpa7QxjxEHvqkl43FpzOs0jItsr4hPrTqX-BL-c62Dc-f1TAQ70m9_wsfdXNwUyvd47Jl_xvIOYGzQ-BzSH57c7KC-GqpSn9n8otiyt60-JC8T44SBQrJVBimRxUpRw18xz9cV3Zt7pMy3LuzfsarNFbqJBkyK3_Z9-U0I8uawpK6xq-d2eSilQSgS_8zWeN1fRQCt_pEaPpUC19khUOEkNjB5z4Fgbchn00xu_T_Q7RiegBxW-2QNJWsnm3f1tgISlgCNt5vOVzcSDQ7z-oI2ssgunDUJkKBvwRlo_HyEhP-B5Ik_Xwt16Mbug5jZ74vRzcUE3Y4DDHcW2skb5wOv4HUy3RuETqLbV6Z7UtfsXjrz1jWX5IfqyoZVbI41zTjqLajYY4YrD4OdAk-VyjFWyQAhgDXxt3Z0XBGWIVG22F2o" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4e76692a40.mp4?token=joDSwv7XweHfsH3poL_bUo1BRbFi8ysrlWRHu8nWMf8E_Sdd0TPrt_NDW-tkqUviEKd3SEzG4a3iEhaugWQid-tYm6560WMLQpUXpAp5clRHJqvQSJTTvTgShs5K3ick14nHYzYWmKp1yBYsktJZ8lZ-Zd906pgp2SpT-J6HLniqH6uuST2bouZbd73E4SQFqO9GYINZBR3aITKOV89UBMQZMIm3bDTI9_NoLjYOAQMSa-ZuWgCfrZ7SLUnGlZpa7QxjxEHvqkl43FpzOs0jItsr4hPrTqX-BL-c62Dc-f1TAQ70m9_wsfdXNwUyvd47Jl_xvIOYGzQ-BzSH57c7KC-GqpSn9n8otiyt60-JC8T44SBQrJVBimRxUpRw18xz9cV3Zt7pMy3LuzfsarNFbqJBkyK3_Z9-U0I8uawpK6xq-d2eSilQSgS_8zWeN1fRQCt_pEaPpUC19khUOEkNjB5z4Fgbchn00xu_T_Q7RiegBxW-2QNJWsnm3f1tgISlgCNt5vOVzcSDQ7z-oI2ssgunDUJkKBvwRlo_HyEhP-B5Ik_Xwt16Mbug5jZ74vRzcUE3Y4DDHcW2skb5wOv4HUy3RuETqLbV6Z7UtfsXjrz1jWX5IfqyoZVbI41zTjqLajYY4YrD4OdAk-VyjFWyQAhgDXxt3Z0XBGWIVG22F2o" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
🔵
امیرحسین صادقی: وحید مرادی من و فرزاد را در هتل المپیک آشتی داد!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/Futball180TV/102021" target="_blank">📅 21:03 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102020">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bZD3ijjJ1aTS24mY_Rygmr4WOXMKvks_TS8LiZB1HPwvMrUGGCAIRcE4dK_LydXoB9vqP9JYK0PHYDsBU-FuYI_DVyy06rQVHvkq4EQmeru2oNqjH_jm9fdWfVVKqiFMgGmiQxT7NW0HDrCBwDd7CuoK1jCHGup2wMGjpWlSMuyryOLj4WzhKrybr3oWdz-jXRD4oqH5MWvgizyh5v4JSg58CbLXZRpb-6j6tZj5ZA4wjMRrNKzuU5YLbTWedS9NUeUOtY543W6Dw5YDJrztmpnnEigaO9wFMGUOPhQEM4WRjA-eBFaqq59CTX_r0apZlS5GEPdqwq4Der2bocmcBg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
🚨
پژمان جمشیدی که به تجاوز متهم شده بود، در رای نهایی دادگاه از این اتهام تبرئه شد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/Futball180TV/102020" target="_blank">📅 20:57 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102019">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vPw1aOMjox-UMnzZshTqh9WMW_7YcLHigq86U-jGYCeJuwmqGBzEhcB8DmhQhMQJAlOZOyRAJSDg7y-6N-zHA5fwa8hm8UVHZTsPljXGilaqkkDPCdXgAovtxUeu1Br3ZqXJqF35bVBG7OZqp7CFvVIw62JuwkvQPF9MYK9zTEQjNDvFguJ1jtVNkvbNAXu2pUrSQfB37nEaUET-TL9BDGRJeYZNsT9kfV9P3pjeseHQD4Uny-MTEcBGFKrlx5tdbWtGNl4P9CDnzNpym1mKUDLuZT9v2YcZALJV0xX1Il3cSgYidJ0PmmbDSrQO5lncA7f4ZtH32PAvVGTCFF4r1w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
💣
آرانچا رودریگز: انتظار میرود که یان دیوماندی این هفته به تمرینات رئال مادرید بپیوندد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/Futball180TV/102019" target="_blank">📅 20:43 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102018">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/260d53f1d3.mp4?token=O72gAn2RjfWYhG2M3dj7t2ecKmlz7nBypTsvLfzPmyB7-wZLda1x-_zjJksLc5otzl8FLbXLYV5vZ-1eslf6Xb7Egw-yI1aFOjg4YmZE5EBiyR2v1momHunw4ZsTMiVvcLcufZexvrnWM_hzo_KJIz-46F97INcUBn5QVeOLiMRblr_fGAD0M0OoArlDPNj2Ufd9pLAEOac2TOhOgNXZ054mI-MnjqFamXNz96ORCp78U09ONnCyWk3nCblpeDhtrNhuHizNn1r1hco1gm2LpOYIxg7ZK_WbFNDNSM4NkGI-CJkoEjj7Gchr5jyFn-cb9SOgizJcQ3Ab4CewacaHb3DupinzCjKs9RTEj2uFaUU6B86fV0jz-5D2WGqLU7Z1rT6eoGCI-4Dpf-eiaVJeMfRKTQgguYxnZDupNMX_W1Tf9V5l4OAzQBJQbUt6bsiXsNJjAuLHogAZLIFV6vtsSTsfRZqXpGtRU7ZNgskp_u1wolQwJ8W2ly-QcvPGpzMaCVZKgi6Gc0y09BGZA6ogHmK9P9Ui2QLfKFdU7OnLG9EZ-R_JF-NYlIxThsOtPe9iQ1N0Nk103Z9FPhobfkgvtPeu8-FSsdM3IB-8AOJh6p2FgaCWX1p5A24VlDFddhGp2b1YT0Yv9cM7iGkbNkRXJgEhRHD4YBw67eoA_KgtEuY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/260d53f1d3.mp4?token=O72gAn2RjfWYhG2M3dj7t2ecKmlz7nBypTsvLfzPmyB7-wZLda1x-_zjJksLc5otzl8FLbXLYV5vZ-1eslf6Xb7Egw-yI1aFOjg4YmZE5EBiyR2v1momHunw4ZsTMiVvcLcufZexvrnWM_hzo_KJIz-46F97INcUBn5QVeOLiMRblr_fGAD0M0OoArlDPNj2Ufd9pLAEOac2TOhOgNXZ054mI-MnjqFamXNz96ORCp78U09ONnCyWk3nCblpeDhtrNhuHizNn1r1hco1gm2LpOYIxg7ZK_WbFNDNSM4NkGI-CJkoEjj7Gchr5jyFn-cb9SOgizJcQ3Ab4CewacaHb3DupinzCjKs9RTEj2uFaUU6B86fV0jz-5D2WGqLU7Z1rT6eoGCI-4Dpf-eiaVJeMfRKTQgguYxnZDupNMX_W1Tf9V5l4OAzQBJQbUt6bsiXsNJjAuLHogAZLIFV6vtsSTsfRZqXpGtRU7ZNgskp_u1wolQwJ8W2ly-QcvPGpzMaCVZKgi6Gc0y09BGZA6ogHmK9P9Ui2QLfKFdU7OnLG9EZ-R_JF-NYlIxThsOtPe9iQ1N0Nk103Z9FPhobfkgvtPeu8-FSsdM3IB-8AOJh6p2FgaCWX1p5A24VlDFddhGp2b1YT0Yv9cM7iGkbNkRXJgEhRHD4YBw67eoA_KgtEuY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">چنتا سوپرگل قیچی‌برگردون ببینیم تا روحمون ارضا بشه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/Futball180TV/102018" target="_blank">📅 20:05 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102016">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/disIQeNdOJg7MHZUyC71gJkw-IapSdHKNQA7-rTZTOQQSKu9G_wfZGDAi6uESJvWHxH31-_4k5ZX4uba45v_N6Rhf0txg6ypDf5j6fktDinaXmnBNAFjbqOlSJpfi33GadOBQpfoUPoTVTE2C-DHW7WEJyzZ11YvejWdSCTv6xDUq0xNpVPZrny9kpIIfJ4PbEdcEJpAA17WEjRNAm3_veFOotF16FnABl6fZM4DmFjb88oTNVEF8A3b__TQ5GcuYCHRQK6FWFOr0y8tQuIG5ih7y87D-9wEqho1fOAZn6yCDl67mUZvoj-k7ZOPLrrgWSjCQEaNiA0M0oCPnRiYuQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ZiSM61rNXzVDBm_uDKlBrFmk7_tJl0MRr2HWVR5dT2VzGk5loe0lIPOmJJ1z7q4XJ9cV-2EuzSfSmHXyH-M6B8raGmvoUrRriB3StyCPPy6KSv2DV4SV709MOwyxElcifDwqLF0OYgjRtKGyAoieZWqfeC00ulob5xp2OcFEbhD3yPZFwb7ln73iLe9BI684_DOudqAoxFspmtLAAs6qJyDT1ev6j5Ea1YcNM0nqA4RvUFCoBtHWnMLzjRITedFlV1ONshKhmIFTc5Ct_V07H40OYV7fWcr5E0DplQDf92L5FCi8L333Dbvg8EUc91s_zJKLb0RNJHk6zeIWwdg7CA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🎙
لواندوفسکی:
شاید مجبور باشیم ۱۰۰ یا ۲۰۰ سال دیگه صبر کنیم و منتظر بمونیم تا دوباره بازیکنی مثل مسی ببینیم.
🐐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/Futball180TV/102016" target="_blank">📅 19:58 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102015">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XGaumk_K7w6fdIlq76rrHnLn9LhL-UNL70VNkEXLuO0JiK7WGNqjU3uMO07uhSXFb6viZWDVJSjwed1nhy1N_1sAthqQhZyBQjCTnHEm7jpTzLpLgN-W3VpWQEAYg1qfSCX58X1WfrpAsGhl16S_YoASvbIN2k8ngXjidAWTxySq-Sy1IK_KSY-CrBGFQNlIrJWlLqihHv2FcExslHtvcz0SsPR8nhOsrq-StYzJ5ZpcfASgDDtPT9ZjyNgrvCyCf2CSeZxa9wUhhSNYqcMmEAPlG_8LwztaSq3CqznQi7mB54V2EgzBdpfjvpumyNtsGGqBxRVzMJk8WXDZ0twAJg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💰
گران‌ترین انتقال‌های تاریخ فوتبال با در نظر گرفتن تورم:
🥇
رونالدو: ۸۰ میلیون پوند → ۲۹۲ میلیون پوند
🥈
ادن هازارد: ۱۵۰ میلیون پوند → ۲۴۵ میلیون پوند
🥉
آلن شیرر: ۱۵ میلیون پوند → ۲۳۸ میلیون پوند
نیکولا آنلکا: ۲۳.۵ میلیون پوند → ۲۲۶ میلیون پوند
فیلیپه کوتینیو: ۱۴۲ میلیون پوند → ۲۱۷ میلیون پوند
پل گاسکوئین: ۵.۵ میلیون پوند → ۱۹۷ میلیون پوند
مارک اوورمارس: ۲۵ میلیون پوند → ۱۹۶ میلیون پوند
گرت بیل: ۸۶ میلیون پوند → ۱۹۲ میلیون پوند
استن کولیمور: ۸.۵ میلیون پوند → ۱۷۹ میلیون پوند
ریو فردیناند: ۳۰ میلیون پوند → ۱۷۵ میلیون پوند
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/Futball180TV/102015" target="_blank">📅 19:49 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102014">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/eb3e14eaaf.mp4?token=qGdI5Tc5W7dCEEp78-c4_BH9LiLoqcflXId0tLsRI0mGwAKmwcKctEbmKcsj53B5svpWCxxie_PzhmRapNza5eox99AxxWyIDIUVt1GQzPevtdhRaG7a-mrDZI3d_7cuEzC7niE2LNG_MWGxWCC_ZiGU0aoEcidTCwAoMN1g0cep0ngGSJJP1PEW9-yg9pen0cgjvw2IWEIp2KA7rZO9_4F01ryLmUglevmknJ2y2M6cZKG8W9ehTeIQ0nPwI7vHLPtKEi33EjYHXFcFSPbjR6Tk3dSPv94Is32WQIiUrUvrYUhBM02hRouxT25-TD7w073jZdKM4YR3rVidj-fbAw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/eb3e14eaaf.mp4?token=qGdI5Tc5W7dCEEp78-c4_BH9LiLoqcflXId0tLsRI0mGwAKmwcKctEbmKcsj53B5svpWCxxie_PzhmRapNza5eox99AxxWyIDIUVt1GQzPevtdhRaG7a-mrDZI3d_7cuEzC7niE2LNG_MWGxWCC_ZiGU0aoEcidTCwAoMN1g0cep0ngGSJJP1PEW9-yg9pen0cgjvw2IWEIp2KA7rZO9_4F01ryLmUglevmknJ2y2M6cZKG8W9ehTeIQ0nPwI7vHLPtKEi33EjYHXFcFSPbjR6Tk3dSPv94Is32WQIiUrUvrYUhBM02hRouxT25-TD7w073jZdKM4YR3rVidj-fbAw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">الگوت کیه؟
دیومانده: رونالدو
رونالدو یا مسی؟ مسی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/Futball180TV/102014" target="_blank">📅 19:39 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102013">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromچِشم به راهیم</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8c1d6e560e.mp4?token=rRa6muO8xH7zo6sJudkRl7_bXI1ZAYvYtGf1ONPrHxkoeqXHbY7aOevxdRlP0np9QX6Fdxlndp732Ez_Dl4HUb6sklyx7eshA53glxS1pwDDqr6oLZu1G-cqSZUF5hloZ83HPhGczh2D-6FsMy91VWYyJ_U6wtUIp7cFjtw59UImFhCNT7ND5jEQxF6TuervxPdWcjBCH6JKwk8G-WePTN6kB73aC3QDFkunpvewXe3nAyVD8bgm0YxilIWIe0VvQcqrIDaohzqUCL46IjLiSo-WF5hoAsrN3JKL9fOrSFDGN4dg_YbGOwwEabo-aDW2SlI6BUIDPGN39418mSblzotd_ofi-LdkOYYqtvj4WPz0B48WF__T9CTzPljqUC7ZP4EbGuZxgNzXk8325H4fjuqQqBBu2264k1wdDdvtoDTEGadXg5mdC0k7usphs-IiJyKc_OU2Byj1MxNDB92BY3uCXFHExYyvhfmLeVLSKgowMo4j1Fr4wxKnRkIAPeVjxP4ipKYnVY8MLxLFQEq8wd66ChR1n7kyrW8y3TgB7LvYyl-Gb17PUy9F2mnKy024IDW30y7EuWGG80HnbjUbdhFDKGMLzrIgtTjHOoNgKRRW0c1ZYfBUpP8YuIKjZLaosrXbIECmKvuzdDwHzBCv1bF_LQ2ghXCzsUMB8g3nVAc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8c1d6e560e.mp4?token=rRa6muO8xH7zo6sJudkRl7_bXI1ZAYvYtGf1ONPrHxkoeqXHbY7aOevxdRlP0np9QX6Fdxlndp732Ez_Dl4HUb6sklyx7eshA53glxS1pwDDqr6oLZu1G-cqSZUF5hloZ83HPhGczh2D-6FsMy91VWYyJ_U6wtUIp7cFjtw59UImFhCNT7ND5jEQxF6TuervxPdWcjBCH6JKwk8G-WePTN6kB73aC3QDFkunpvewXe3nAyVD8bgm0YxilIWIe0VvQcqrIDaohzqUCL46IjLiSo-WF5hoAsrN3JKL9fOrSFDGN4dg_YbGOwwEabo-aDW2SlI6BUIDPGN39418mSblzotd_ofi-LdkOYYqtvj4WPz0B48WF__T9CTzPljqUC7ZP4EbGuZxgNzXk8325H4fjuqQqBBu2264k1wdDdvtoDTEGadXg5mdC0k7usphs-IiJyKc_OU2Byj1MxNDB92BY3uCXFHExYyvhfmLeVLSKgowMo4j1Fr4wxKnRkIAPeVjxP4ipKYnVY8MLxLFQEq8wd66ChR1n7kyrW8y3TgB7LvYyl-Gb17PUy9F2mnKy024IDW30y7EuWGG80HnbjUbdhFDKGMLzrIgtTjHOoNgKRRW0c1ZYfBUpP8YuIKjZLaosrXbIECmKvuzdDwHzBCv1bF_LQ2ghXCzsUMB8g3nVAc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
اگر قصد دارید سفر اربعین را با اتوبوس راهی مرز شوید، پیدا کردن بلیت را به سپاس بسپارید
🔹
سامانه پایش آنلاین سفر (سپاس) با اتصال به همه درگاه‌های رسمی فروش اینترنتی بلیت اتوبوس امکان مشاهده و مقایسه ظرفیت‌ها را در یک سامانه فراهم کرده است تا سریع‌تر و آسان‌تر بلیت مناسب سفر خود را پیدا کنید.
🔹
از ۲۷ تیر پیش‌فروش بلیت سفرهای اربعین آغاز شده است. برای برنامه‌ریزی آسان‌تر سفر به سامانه سپاس مراجعه کنید:
🔗
sepas.rmto.ir
#چشم_به_راهیم
#اربعین_حسینی
#سازمان_راهداری_و_حمل_و_نقل_جاده_ای
🌐
rmto.ir
🌐
141.ir
@Cheshm_Be_Rahim</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/Futball180TV/102013" target="_blank">📅 19:39 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102012">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">🚨
⚪️
فوووووری از خوزه فلیکس دیاز: انتقال دیومانده به رئال مادرید نهایی شده و بیانیه رسمی فردا منتشر میشه.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/Futball180TV/102012" target="_blank">📅 19:27 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102011">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SCUjXKE_6QSCWDkO5tZ_u1_scJEimc7zdcjulMuLpXlFqhUvxaxyoNiJfFCZob7uJg7qK4LGYIBCAVmpSa3GwpuHnwhzBVCdnHFVYv6F_A5_uiN5ZOG8VrCscwq-QEX330_UiBPKJanuO8AobDNUlSIkVvPDdxakwGYKBRKzIH4rCvL-4KlFvGDxBhpylUJusIfiXacSjiQuskwOmxJExlZmZI_z3bp1iSTpfU6ZMt0WZ6lRYU4KBWXNMKPmn-eQHaYSR-q7u3AUnDAA-akMQfL1ThJyjGMAJbEfqx44FpWYLecCIRXYD8E9rDg1alqiZFN10zrI-U-Xa6t5F1rgog.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
⚪️
فوووووری از خوزه فلیکس دیاز: انتقال دیومانده به رئال مادرید نهایی شده و بیانیه رسمی فردا منتشر میشه.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/Futball180TV/102011" target="_blank">📅 19:23 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102010">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/746abba13b.mp4?token=mqYdcIYIzVyM9bDqsdKHcKy_xjiGNA7B_L5y_PpEEshQsO6F2aB_Gy7aLImwU0QDoXJy00e8DPqtXuLIF9ZgLcjWojmAMebyEWKrp4lN3UdNP33b3i1Ky-tEFBP0tl5DSVJZKdrl5nXxrIIm-Yr6JrTX_oal_YOji5Bn3m1b_U3Ov8iJ9oj0hY40NiS3nL7ZY8922BnY4k2HRnKlZz1eJbx2koxerZ9hYF2w7YGakhhk6MKWvH7bSTt6fwrldsVnfao0lDmARpmLRLvOJqOa8RhXKrrNdBWEJq1NWalGar5YsSeYTCnJ7OfbRcSUhsnWFtsroakwfH1f-TeAlGXY0kGiVdNHGYr_uHyUkfN0VmJtZSa-3ZdZ2bcvNilky1kx-pWIPxMjkan_Zd_KI3A58bBcwZxWZ9P8oK7QjcDp82-s5b_j1mnd4MOrGtnaXbzYV6FCZOj-E3eavlnkovqOV0apEquP-2t5XAmBErCB2VzeV2eH8lGCeWym3oGjVpb2d0X02sspiA_1xwaypu50f_s66BAb2cuEHWqcI-1v9ra1qqv310j8DJfwdfDdMGS0IEXX0S5KrXjGCzJve3xa31LPKajVab5wNtFXdYJ0sCJL9zzEAcnyETcWMrxw6LyMs6X5OHhhnWJmJ-OisZy1M73sWzMMO78T7FLdFA50Z5Y" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/746abba13b.mp4?token=mqYdcIYIzVyM9bDqsdKHcKy_xjiGNA7B_L5y_PpEEshQsO6F2aB_Gy7aLImwU0QDoXJy00e8DPqtXuLIF9ZgLcjWojmAMebyEWKrp4lN3UdNP33b3i1Ky-tEFBP0tl5DSVJZKdrl5nXxrIIm-Yr6JrTX_oal_YOji5Bn3m1b_U3Ov8iJ9oj0hY40NiS3nL7ZY8922BnY4k2HRnKlZz1eJbx2koxerZ9hYF2w7YGakhhk6MKWvH7bSTt6fwrldsVnfao0lDmARpmLRLvOJqOa8RhXKrrNdBWEJq1NWalGar5YsSeYTCnJ7OfbRcSUhsnWFtsroakwfH1f-TeAlGXY0kGiVdNHGYr_uHyUkfN0VmJtZSa-3ZdZ2bcvNilky1kx-pWIPxMjkan_Zd_KI3A58bBcwZxWZ9P8oK7QjcDp82-s5b_j1mnd4MOrGtnaXbzYV6FCZOj-E3eavlnkovqOV0apEquP-2t5XAmBErCB2VzeV2eH8lGCeWym3oGjVpb2d0X02sspiA_1xwaypu50f_s66BAb2cuEHWqcI-1v9ra1qqv310j8DJfwdfDdMGS0IEXX0S5KrXjGCzJve3xa31LPKajVab5wNtFXdYJ0sCJL9zzEAcnyETcWMrxw6LyMs6X5OHhhnWJmJ-OisZy1M73sWzMMO78T7FLdFA50Z5Y" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وقتی فوتبال تبدیل به یک فیلم و اثر هنری میشه:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/Futball180TV/102010" target="_blank">📅 19:05 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102009">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XIJgcZvLa0gMwKEiZAkvr1tMRnw1Ltcr_u4hwmDGtYL65hCHatdAshi1vS5X4ttHwW4I7nkuPZ2wMR6VDipfn3x-S4F-Ynv3Sp4O3WJbHCclm_7_VFXuCa8AQENUmSOSHqH8IILfBh5bGveaa1E6ItjE1iNhRQo-9M-9k-fKjsqEC7qO0UlPEKn1gihBHdOq7X91s-LJ77QEw68WvWfdjTui3aZw3XVMcz0YIdoIgDC7bKddCXUX_OAxvGoOBdNLlupsQD2Ervj9FScK4eBO2UDJZJId9lxTB1xndfXX5sOvS0gr0L0QGFKbMn-HGV_YDcEu1F83iZPXCTaMvRhCyg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🔵
اشرف بن عیاد:
کار تمامه، مدیرای بارسا متوجه شدن که موضع اتلتیکو برای فروش آلوارز تغییر نمیکنه و نمیفروشنش، حالا بارسا منتظر واکنش آلوارزه!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/Futball180TV/102009" target="_blank">📅 18:52 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102007">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/UIHnPOoptWCncUchqpThs5Th1LLaMpp_xeIySa6rIc4R9r3CzKHiINeANATFJtvioauaLJo92eIDyIJ39x5d4YPIXON2EnMFtqkrnkvL-oD2bKpmRGabgbu8KE1qq-Al2J-j-w4aJj8kgP6pVvVwkImfu9OzxEi4kYoPZh7YvlXsa3wCgybqQX4k9INCe6OhqfGcpfkUCQ_HQ2GY1miLCmqyxxZ0RCSjQ5-V2TWQZ0RxuLNrVt2z4iQa70HK9yV_OPf7wKI2Mn7TCRowmPzmL4tyvo0ezHet_f8Tri2nanPWR4eW8Pe_PatZAmFcY483CgDV7svySWzlOTKDPxB1Sg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jsKEf_NYZme9rf_0-dsh36F5Slz5nMVo8VSz4uInH-0-8Rv-4OAS0wTyZqVPNCgChR0cxuTUqIrK-D4DcbTm3nbkOLwgevj7ZyjG3CB-EnA7lCXgAwOLXcF0UO9hea2YkAwy-paOq0MwUNZu3R9rdqSqfSNxDCBo8G46Rtdrbk9cG0EHQ7EtnpNGHDu5VkatNDsSOOhH3mP_EmZkfOEVATP3q5w46Ib1IlD3n1koR2Uhkuf4_z0vyEaecVfR61kym1voUBG-6iQr16bJ832AJAv895UntqEtPNerWfYWcvA8CF9gca1S0zs8WjFfn-4m4tSl5eyKP8G2K5m4z6G4Pg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👀
تاریخچه رابطه‌‌های وینیسیوس جونیور:
• 2021 —
🇧🇷
ماریا جولیا مازالی
• 2022 —
🇪🇸
اِستر اکسپوزیتو
• 2023 —
🇧🇷
لورنا ماریا
• 2024 —
🇧🇷
جولیا رودریگز
• 2025 —
🇧🇷
ویرجینیا فونسکا
• 2026 —
🇧🇷
ویرجینیا فونسکا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/Futball180TV/102007" target="_blank">📅 18:28 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102006">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ac77f90860.mp4?token=TbismWjMyqEiiJN8Yu29KIYBGDT8iLFKBBHlJBiIJpCKEmLfHAWW2fzsXGCdkfxQe4FInrAl_MusLkeT7fkNwEkolMZytqcAioAD3A8RkuT_eHdxiaxP6C8LcHrv4MWIECFvH9Jf6RjOdVqYrGNH7E9tFQlLKswnHoEin6q8AmJudF7zhfv2phfhS8IM5NLO27jpfC1VWU42VXP0yutIkeMegdFPRmusONEQS-IJ8IkJiadMKVgoZ0ZwygEsZ3T6Gk-QA_xJJYKh0yEJ9oXbifkzCmhvL6jrOoUUix_9ccdfIzFT5O9c18SzEw0PmtmWWX1wkLp7DFzypBQjcF2I1w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ac77f90860.mp4?token=TbismWjMyqEiiJN8Yu29KIYBGDT8iLFKBBHlJBiIJpCKEmLfHAWW2fzsXGCdkfxQe4FInrAl_MusLkeT7fkNwEkolMZytqcAioAD3A8RkuT_eHdxiaxP6C8LcHrv4MWIECFvH9Jf6RjOdVqYrGNH7E9tFQlLKswnHoEin6q8AmJudF7zhfv2phfhS8IM5NLO27jpfC1VWU42VXP0yutIkeMegdFPRmusONEQS-IJ8IkJiadMKVgoZ0ZwygEsZ3T6Gk-QA_xJJYKh0yEJ9oXbifkzCmhvL6jrOoUUix_9ccdfIzFT5O9c18SzEw0PmtmWWX1wkLp7DFzypBQjcF2I1w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
خشونت بی‌سابقه در لیگ‌فوتسال بانوان برزیل
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/Futball180TV/102006" target="_blank">📅 18:02 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102005">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/b8T0-m3-l_47fWziFMWHtMvtcAR6O7hoOSBXkZqsUJfEjHipSMULu-hRUMdy19PgiiqPxKlPwNk_uUsOnrV7sXbdoZwWbv7jimu2BP7D4_SVEhZWZA3hlk5sSx29udpBVfZX9xvCXrt3cxCxS0p9f1dCRLIl5X-MoV5OjcmN3XwOqdLZ1-TULp9oHgVN9jZD3ZFLDTMGoVvzzHigzVoEP6wGHh7x0HOnUqQ4PYNYPjpj3l-5D6iBq7DlQ2E00IBLTGrDvQTspHCjkL7urO1-yON78CyJwPrYlNrqLKoLZOYGUMV1JJgzQB5TrrsawBSigDzvbKhNTQPcfTgo5YYCLQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👀
🔥
🇪🇸
رقبای احتمالی رئال‌مادرید در سید یک UCL که با دو تیم از این تیم‌های در تصویر بازی میکنه
🇮🇹
اینتر
🏴󠁧󠁢󠁥󠁮󠁧󠁿
منچسترسیتی
🏴󠁧󠁢󠁥󠁮󠁧󠁿
لیورپول
🏴󠁧󠁢󠁥󠁮󠁧󠁿
آرسنال
🇩🇪
بایرن‌مونیخ
🇫🇷
پاری‌سن‌ژرمن
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/Futball180TV/102005" target="_blank">📅 17:50 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102004">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Aeu3x3LqecIwWT5CJHUg1J-s-O0Z_08mobO6ZZM7BhAj0zefduRprtXOccwn-plaR8zEw8ubMX8VH61-_8MJm_vyAWCnC2QBpTNxPkbKGmTa8UIzoD4_bwPKRM7NLMeZfZ4EbKK9T5C75dNvwzYkKEtf5F1Wv9n64YFZ0Eh3bzX83VqR6dtmtJ7UshprpkyFuXGEuuCXvITRQbIO-GD6SbRpGEOwYDo9WhymSxvM8lrk_PSTB3jhFXAztOS7VY3kmOfDTRDJ7TiovZ6aU1caShm76FWXmfvMV8YEQKjEmM94DHt54nuZN4oNcs2nrbMON9UhW05ZJYmKAppLUPRITQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
متئو مورتو:
فولام قصد دارد یک پیشنهاد بزرگ به رئال مادرید برای جذب گونزالو گارسیا ارائه دهد. آربلوا می‌خواهد او را به تیم خود بیاورد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/Futball180TV/102004" target="_blank">📅 17:41 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102003">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fYTjPaOmIPquHLUJGz5qNnMC5n-y5mUOjOzdUBNFSc8arN9gmBi2mfoFgnh84ocRgUoW16D3LCyBkDIcX-ox-bGNcyjZnaTBYIrZlaagEmdMAIxXKPS7boHiZKYzemVyFU6tDtVieARS2v-uB_TZ2JXOsG9NQjQqIWwu41t1IMXbaxpnC_8bqsU4kdLd5hix8Ham7vVqD3-D7NCrPguaPhUU4SwfUzGHZPT45geQR59vge3YuISUsY2PYhEErYg1rllHNV2YrfwmYl7_4RBJgDfQIJqsLh0QG4Mpc0-2nylt679yiRGNdCEG7emy6L7dVPVNcTLnEEAq5ezEOz_ulg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
سانتی اونا:
باشگاه الریان قطر پیشنهاد خود برای جذب جیدون سانچو ارائه کرد
باشگاه قطری در تلاش است تا وینگر انگلیسی را متقاعد کند.‌‌
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/Futball180TV/102003" target="_blank">📅 17:22 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102001">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">🚨
🏅
فوری؛ لینک پخش زنده بازی پرسپولیس و پیرامیدز مصر گذاشته شد
💬
@squadify_ir</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/Futball180TV/102001" target="_blank">📅 17:20 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102000">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9608d1c2fe.mp4?token=rcAVThDAyXT1yIy4rjoackv0hfVqOAWKpDbDEdg4dgqsh1sOWrZxcStyBUPH3O7ODSuq20-k_Z0h9qhtwujZwtWOcRhc8zIAyTcuL4lrt0BEUvEzA64SHTl0nu6DQDoicTSE5Pfat-px_iJIcIzwsTyY2Jb7l3GAJwv7ANXub2ionw0YpdhwEa3SyY6TKaJI1VjgcHYeFdZayL_3fhHI0V68GYnqXdkerlm-bI4YBs50Zm5V1alAqnXXGlScNOa38ZA2p5bXoQ1k8BN9ghe4PmmCMRQjAi17g07u8jOfvDqTN6ghOzbZRloGjiPP0Fr3T3BKdH1aj2LEB5Tvecz5eg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9608d1c2fe.mp4?token=rcAVThDAyXT1yIy4rjoackv0hfVqOAWKpDbDEdg4dgqsh1sOWrZxcStyBUPH3O7ODSuq20-k_Z0h9qhtwujZwtWOcRhc8zIAyTcuL4lrt0BEUvEzA64SHTl0nu6DQDoicTSE5Pfat-px_iJIcIzwsTyY2Jb7l3GAJwv7ANXub2ionw0YpdhwEa3SyY6TKaJI1VjgcHYeFdZayL_3fhHI0V68GYnqXdkerlm-bI4YBs50Zm5V1alAqnXXGlScNOa38ZA2p5bXoQ1k8BN9ghe4PmmCMRQjAi17g07u8jOfvDqTN6ghOzbZRloGjiPP0Fr3T3BKdH1aj2LEB5Tvecz5eg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👀
آنتونی جاشوا، قهرمان سابق بوکس سنگین وزن جهان، از آهنگ سیاوش قمیشی برای آهنگ ورود خودش استفاده کرد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/Futball180TV/102000" target="_blank">📅 17:06 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101999">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/57f6f418b4.mp4?token=Ha5UTnkC93OXRQ-DqbtW1aMn3qvpwxXAo1NY1sNg8sqZg3Pz4yW4UsTpFtEC8AwmpH0yEy6G9ZFvhOeVYIjcDK6bxBhwzVor0qzco8CWLWRhBEyDOIo185Kb4dKxQpH2GT0xUF-f6zXGZKb1M5iUvf6v3YCC66oltJdDk6eVof1dP6g869gxdM_5koSVwuR36zI6MGJkYZ8L4Oaj7XpgXJgTwHYi2Jxb5wwnOMY633_jWbUeBP7JBE7gmDk9o1G0eVn7aenlNMQaniD5aUYzbyYJBDD_y3lawC29JveOlU3DVGYyb0a0vrRvdICHBaNNNtsgcUt5Iaj-6T-1EIcsAw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/57f6f418b4.mp4?token=Ha5UTnkC93OXRQ-DqbtW1aMn3qvpwxXAo1NY1sNg8sqZg3Pz4yW4UsTpFtEC8AwmpH0yEy6G9ZFvhOeVYIjcDK6bxBhwzVor0qzco8CWLWRhBEyDOIo185Kb4dKxQpH2GT0xUF-f6zXGZKb1M5iUvf6v3YCC66oltJdDk6eVof1dP6g869gxdM_5koSVwuR36zI6MGJkYZ8L4Oaj7XpgXJgTwHYi2Jxb5wwnOMY633_jWbUeBP7JBE7gmDk9o1G0eVn7aenlNMQaniD5aUYzbyYJBDD_y3lawC29JveOlU3DVGYyb0a0vrRvdICHBaNNNtsgcUt5Iaj-6T-1EIcsAw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
❌
قلنج‌گیر معروف ایرانی که با درودافای مملکت ویدیو میگرفت توسط پلیس بازداشت شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/Futball180TV/101999" target="_blank">📅 16:40 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101998">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3a860d22dd.mp4?token=YTFs1ga8mOOWX2hR-qtbHiQaoL2m-MoNb97gR4e5aXRoHpq1UyvTxV8N9Mx_WGSb2OuQPd_7DzQ_Eks3LrjoGD_QHBN3fRIbU-RN9pMtYS7yTLjV2YGKblqqhAZmm01PCvl5vQARYSg0OBpwNCbjCcsKHzb4Ot-ai8Jl-kBFhgTImNZKqDQPYPlyay7NSZ7OSeYMNxZ757b_jrt3LTjB_CWRxzmqEhf13ucue-S4im8o68XVDxIu0IOyyQ3wTaTbi3wtaSVxVhxp7Sv7z9cGsaknL7FQ6hNStdJm5LpeiKP34X0KwDCyF9bofZ-WSlskXwWctPl2E4ufaaEVrZIUaA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3a860d22dd.mp4?token=YTFs1ga8mOOWX2hR-qtbHiQaoL2m-MoNb97gR4e5aXRoHpq1UyvTxV8N9Mx_WGSb2OuQPd_7DzQ_Eks3LrjoGD_QHBN3fRIbU-RN9pMtYS7yTLjV2YGKblqqhAZmm01PCvl5vQARYSg0OBpwNCbjCcsKHzb4Ot-ai8Jl-kBFhgTImNZKqDQPYPlyay7NSZ7OSeYMNxZ757b_jrt3LTjB_CWRxzmqEhf13ucue-S4im8o68XVDxIu0IOyyQ3wTaTbi3wtaSVxVhxp7Sv7z9cGsaknL7FQ6hNStdJm5LpeiKP34X0KwDCyF9bofZ-WSlskXwWctPl2E4ufaaEVrZIUaA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
⚠️
اسلحه به دست منتظر آمریکایی‌ها
صداوسیما: مردم بندر جاسک به صورت خودش با اسلحه در ساحل قدم میزنند و در انتظار ورود نیروهای آمریکایی هستند
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/Futball180TV/101998" target="_blank">📅 16:20 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101997">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ABp-pRvAxC9MfXrpuRZ_Yoo3p3FXoRok4mP0oGP7kKFdT7CrmRNqdzyVwZongLv95toTghQWfAPXPUW8uIVdenzZR1WeU0fI64THI-zA-rvyh9L_sexaqKKQ0fNS0SR8TgDVtb7CWLvEESFP4bstqnDz3KAwNUNRK60lcfYq6xzATUOq53CClkwXn4wYOVRdy0dZ1lDrC03HF1VH4ro-2o-PPf4VPAIF8rGnC43hBwSw8DsbU8E4HsAc9dKbSxi8MzSZDRD0JdR4WpkbsLo2fZ_dUw5bVfeVBXRCnDI8Spu0qpVPGQ7G-bahO4n2AHyqzSChBvzhIJNzG3uhxbtUQg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
بازیکنانی که با همسر یا پارتنر هم‌تیمی‌هاشون وارد رابطه شدن:
🇦🇷
مائورو ایکاردی و همسر مکسی لوپز
🏴󠁧󠁢󠁥󠁮󠁧󠁿
جان تری و دوست‌دختر وین بریج
🇩🇪
مسوت اوزیل و دوست‌دختر کریستیان لِل
😀
تیبو کورتوا و دوست‌دختر کوین دی‌بروینه
👀
💔
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/Futball180TV/101997" target="_blank">📅 16:00 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101996">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/58250e2a71.mp4?token=GBshSmjeV4PYubMCaplOfvWid7iNU-N_B9iFMqXKVGb8dPDA43Ks5CSF6PlMc4g7909P4tMA3CGAbwF6x4QP-PKM3S4hJKMEfsA3YXgjqRQnxUf4hjWHh0_rwfHmQm-8eSRszH0LfB1RU-imSWwoEjmTdt0Q70jabG482CSCUryQOfgACFUd5v1Z6ppF4BHhBGQCrJ1xQ_Vti4CYxvua8kLf9rRvtKwwnUpkRukGFmyqB1qhkGjOeYozBcbFahW_NHa0GvFuBalZcKKp6Blm8TnD3xc8zpRyfi6dagOL5LDvVdY-n6eUe6-QXdhsZfL6gKno-hCgkvKgQWmW14o0jw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/58250e2a71.mp4?token=GBshSmjeV4PYubMCaplOfvWid7iNU-N_B9iFMqXKVGb8dPDA43Ks5CSF6PlMc4g7909P4tMA3CGAbwF6x4QP-PKM3S4hJKMEfsA3YXgjqRQnxUf4hjWHh0_rwfHmQm-8eSRszH0LfB1RU-imSWwoEjmTdt0Q70jabG482CSCUryQOfgACFUd5v1Z6ppF4BHhBGQCrJ1xQ_Vti4CYxvua8kLf9rRvtKwwnUpkRukGFmyqB1qhkGjOeYozBcbFahW_NHa0GvFuBalZcKKp6Blm8TnD3xc8zpRyfi6dagOL5LDvVdY-n6eUe6-QXdhsZfL6gKno-hCgkvKgQWmW14o0jw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
👀
🎙
علی علیپور: حتی خود پرتغالی‌ها هم کیروش رو گردن نمی‌گرفتن
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/Futball180TV/101996" target="_blank">📅 15:40 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101995">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/A4Qi7qBDCosFh9mQDSgLEVG46ZPfLyniBSxV65GvYdqKrYVlZodmwuGgBeTPXiJVCn0ri9EOoi5K-k--esPw92VlU9sc2CiuV_3GDSW5AkPhapy6lUHDnjiASwz54vi72m3gfyjQmt90JLF11ZCpcFBjjkiUtIIJo-VpqohctZjzUzq-apegTfuZ-9YuDYDfscbX4BFPx0b5-6kXtQuKx8y4oJiCyrP0eG7svtAHx1ffWXJ3iXDOZPm60_zlHElIj-n8PlnP3XW6jdjSj2DKzOcojZ3wMN0tUfwPa5RvoMg_kU4jGiPNHlYdE_6goDRFC994heCZnff43_0wB6ItGQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
📉
می‌دونستید؟ فقط چند هفته قبل از جام جهانی، اینس گارسیا، دوست‌دختر لامین یامال، حدود
۲۵ هزار
فالوور در اینستاگرام داشت. از زمانی که با لامین وارد رابطه شده، تعداد دنبال‌کننده‌هایش به
۴ میلیون نفر
رسیده است. فقط در روز فینال جام جهانی هم حدود
۱.۵ میلیون
فالوور به دست آورد. همین رشد انفجاری باعث شده چندین برند بزرگ برای همکاری تبلیغاتی سراغش بروند.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/Futball180TV/101995" target="_blank">📅 15:20 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101994">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">🚨
🔴
فوری از رومانو: لیورپول در حال تلاش برای تکمیل انتقال بارکولا است. این بازیکن تمایل به انتقال دارد و اولویت خود را به لیورپول داده است. لیورپول منتظر اعلام قیمت مورد نظر از سوی پاریس است.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/Futball180TV/101994" target="_blank">📅 15:04 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101993">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gZnE2pk8xWfK8kaX1EUhJxXjaFdzzCvaXZhWlo7UrULxUEoPd3XMxlMYXw7DPjqH0yryv1HPIsJY8DTbzJ4eH4VLz8tSZVjIbcFFswFIEW5ngY_44KuS45pz9qkPCPjfiU-V292VaxQL_qqT5yP7WnjONzyJWtqlaH0o_Emtf5Hk-wXGYj__oTVbdq3ufOzBm8r_mFsOvEtSvgsexVmoRFEBi2EW-f-NNIzQqRSwRkV751EQsDG_cZK9aIWD2sY-jI_BQNmxzqxmmEMmV4qoFnRK_Mo8IOiLS-TaHV9-BnqlGWa2PmShTBULP-ruFNiGkBE-dSesgKnLQ3I6k7jLqw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
فوری از رومانو:
لیورپول در حال تلاش برای تکمیل انتقال بارکولا است. این بازیکن تمایل به انتقال دارد و اولویت خود را به لیورپول داده است. لیورپول منتظر اعلام قیمت مورد نظر از سوی پاریس است.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/Futball180TV/101993" target="_blank">📅 15:02 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101992">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/45e9d378eb.mp4?token=Zx4z_I_QaQRpEqemvT-zEO7CIpyT6oHuQk3i3105fRggopLN6tXN_D0LNdRCAJsTPLaFjVbLPEr3u3n7uVlCjl9KxC0dUlVTsg0ZS-zB3CHMEvKL65Wxl-7p6Ne6D2sYOWSM3muW_onSZwOXEvsNv4m-FA0HZuJgCA9_VorQOwV_r6k1qIsRs2qNPKhif2JnUsLWptvf2v5ygXyx7wpMv5Q0wLDwF-TKUPX_aP8IjgJ-9QASPpmjd-RWN1lGtvijpmbq_tCFjkjMuj3vVrmV1zlkTWTAHx61EF49hoDL0rzwM9DsEfjkGhfkrN2L8xyjEteb3k7YBOZU1OiNTzV1YC4r8kea-dzDDUtMe3GhVg4ANqxlZBh9qLsBetfNkuapLiQkVh7q2_RnKprPDEbxZeFSMomceF8kwlBOT6lIVfVzAL0R5ES7yM8Y6sR4DLxe3XIA2lx7byqW0IoWSHpMVYfjwVbZY_pS3Fy-6WuQ5Xqm0nfQrytqgf9lDHNwMwgcy50oJSCSZtwDxNT5wVc-XmfhIS2y7FQOjmk59tNMsREkU5m6EUP-K5gQMuAv83gGa1_psYdtr8kv4EeIlNmzHNDM6tR_LczZOfjQysQ5DcnnSpltjZKQvfMgX70JahX_PE5DrIjaTdGvibbSt7alL5m6xnXA2SFSbR1Z_awDX-U" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/45e9d378eb.mp4?token=Zx4z_I_QaQRpEqemvT-zEO7CIpyT6oHuQk3i3105fRggopLN6tXN_D0LNdRCAJsTPLaFjVbLPEr3u3n7uVlCjl9KxC0dUlVTsg0ZS-zB3CHMEvKL65Wxl-7p6Ne6D2sYOWSM3muW_onSZwOXEvsNv4m-FA0HZuJgCA9_VorQOwV_r6k1qIsRs2qNPKhif2JnUsLWptvf2v5ygXyx7wpMv5Q0wLDwF-TKUPX_aP8IjgJ-9QASPpmjd-RWN1lGtvijpmbq_tCFjkjMuj3vVrmV1zlkTWTAHx61EF49hoDL0rzwM9DsEfjkGhfkrN2L8xyjEteb3k7YBOZU1OiNTzV1YC4r8kea-dzDDUtMe3GhVg4ANqxlZBh9qLsBetfNkuapLiQkVh7q2_RnKprPDEbxZeFSMomceF8kwlBOT6lIVfVzAL0R5ES7yM8Y6sR4DLxe3XIA2lx7byqW0IoWSHpMVYfjwVbZY_pS3Fy-6WuQ5Xqm0nfQrytqgf9lDHNwMwgcy50oJSCSZtwDxNT5wVc-XmfhIS2y7FQOjmk59tNMsREkU5m6EUP-K5gQMuAv83gGa1_psYdtr8kv4EeIlNmzHNDM6tR_LczZOfjQysQ5DcnnSpltjZKQvfMgX70JahX_PE5DrIjaTdGvibbSt7alL5m6xnXA2SFSbR1Z_awDX-U" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
لحظات خنده‌دار از زنده‌یاد اکبر عبدی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/Futball180TV/101992" target="_blank">📅 15:02 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101991">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d63baf35c4.mp4?token=fqowHwKHJzDdSFMuW2DST2-RWwL-lbAhOicYnBiwYML6fJnEn-aDLi_JkmPiu5N2eATO3-1nQ_5dyHwq7V8F0y2SaeXvL_7w9oCTnMtjxObF_UX7YkyirmZZ38moMS-8OsrfYxPnwqMjumAKyFaRDXME2evT_eSQK3IZ2yPl1UiY4H3i7p3N4LJ_wP8FN0WeOZi8cv2E2-QibXVFCcMMXES9_JDgDdskPjyLU3--HJFqU7gFgZyMR4Feuoi7oFeAhP8jJN8BL1HXXw3xhj3OxBMhIPCoKlGAH88oRVF-F0WU2qFprhDW58hx-8pEXYGAOXAEXJ7Fx26S9vOfugjJTQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d63baf35c4.mp4?token=fqowHwKHJzDdSFMuW2DST2-RWwL-lbAhOicYnBiwYML6fJnEn-aDLi_JkmPiu5N2eATO3-1nQ_5dyHwq7V8F0y2SaeXvL_7w9oCTnMtjxObF_UX7YkyirmZZ38moMS-8OsrfYxPnwqMjumAKyFaRDXME2evT_eSQK3IZ2yPl1UiY4H3i7p3N4LJ_wP8FN0WeOZi8cv2E2-QibXVFCcMMXES9_JDgDdskPjyLU3--HJFqU7gFgZyMR4Feuoi7oFeAhP8jJN8BL1HXXw3xhj3OxBMhIPCoKlGAH88oRVF-F0WU2qFprhDW58hx-8pEXYGAOXAEXJ7Fx26S9vOfugjJTQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
دستاورد دیگه تیم‌ملی در جام‌جهانی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/Futball180TV/101991" target="_blank">📅 14:40 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101989">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/fmD6Qk8V2gG-pD0ClVilVwV04PY7XZ7wE1iV5aOOckLY_MPwOa3tvyNbYYGlGZrHkHaPiJ7Bn8PF3w2bcKYyaf-zdYMd03mANFJStqY2Di_kmvBSV34H46274NXbPSq3-twu4c5vdGHF-8geU3dyyNNdJrLInKup05srcL8T3jGdTRHZUqjy2_ip94u_EnzdjmRtdBA86ydOe35B56STmwZQJdFPJBPJpPOAjYba8oVJkOiEtkUBFV6vrL8Tgn2y4FsMSVLSqO77P_b0iSg4Kz7G3s73nidvA2hjbFY_FmOzwMv9vobgN_OsVjjFNGNzp12s4UDb5cYYUn1YPyHYEQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/GGA_jezv4vipmckUzCKPoZPRMIlaggerESym9tsewcirkp-pxL4-YIkkcD2aFl2vNDFniF_owAa9IjRMXSr6NTQlDc5T2tXc7-9tDTcn6cmoy3QRnWBUmsVJ1fKnCjUsm7xUIY5rBboN6UFhoLrRT5FUD3QjnGb7rvBRHwU2zg5A6_njwO0vWdX7QQ-ut9-TMMKGNOmWvIW5hyRXF_pxRpmNz6PWaV5k-j94i382AKiHq4N8Le9JdHPe728ZC4MgGISEMSJKYlN46-nxXTy_oka208JhUzitHbGoiJAJY1nukIcEAOn1h6j8SMWp7ne8-KUdW61kfc2wixO_VfpUBQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🎙
اینس گارسیا، دوست‌دختر جدید لامین یامال به این موضوع که گفته میشد باعث جدایی او و نیکی نیکول شده، واکنش نشون داد:
من به کسی آسیب نمیزنم، چیزی رو از دست کسی نگرفته‌ام؛ فقط دارم زندگی خودمو میکنم!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/Futball180TV/101989" target="_blank">📅 14:20 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101988">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/310ebc00ec.mp4?token=H_HMFxGVqIXEFlNoye9rX7UIW2rSD4pNtvkjXqBjzpHLKqf23VMBhvTdXtnnItdy3VMIEeeokNaEx0VS3Abc_fFPF3PuTZ7ri2-j9LIhMtAxGpmfxwiSBCneFxO9XK-jnSh3gKfHveN69jhPUoRaeXGmut1lc5H0JZgCko_cW-LNy2kpf4Wop5cNvxRAHC7rShKexIemSpDxnGye0LkzZYFT4naxiZQgFj0cH1chTa4vnyl-Y2pQL2ftDK1yGpfVAEYVxrQl7lTxzPssUNfq9_F6k6aNhR42p1nU-gnbeeRShbE9vJpLCrlXF6C6LMB2UhCPYNJAsIJVJITLe8Dt3SI1EdBlPVRXrARGrxKNzgeZ3LmJipO04veYfjavJONFCW4sztI-JGUPCfhOpEm1tAr7duOfpNRWG3dbKibQaCydebLU0SF6smoD6z9VVBIEiLWHqj_i2PtHxnQDCV7f2YBvG_LM-hz686xITJnaAysJnrKZnCiCogcN7sRbKSN4oUuemaiTs0KZiQ-nwIPcydkZqI6cBPFAP3jxH60Dt0YkESggoviU7hUcrewHcIqsSM9iBXrR-0W0jvb_7V72c9J-DUMhTeL8SCPniJnTTNx5m8V8Cpr0vPUyKqlWTCaMANn2QGI56dG3wNgutLAC3Bug9MHTqp3oMPKW3MgFR38" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/310ebc00ec.mp4?token=H_HMFxGVqIXEFlNoye9rX7UIW2rSD4pNtvkjXqBjzpHLKqf23VMBhvTdXtnnItdy3VMIEeeokNaEx0VS3Abc_fFPF3PuTZ7ri2-j9LIhMtAxGpmfxwiSBCneFxO9XK-jnSh3gKfHveN69jhPUoRaeXGmut1lc5H0JZgCko_cW-LNy2kpf4Wop5cNvxRAHC7rShKexIemSpDxnGye0LkzZYFT4naxiZQgFj0cH1chTa4vnyl-Y2pQL2ftDK1yGpfVAEYVxrQl7lTxzPssUNfq9_F6k6aNhR42p1nU-gnbeeRShbE9vJpLCrlXF6C6LMB2UhCPYNJAsIJVJITLe8Dt3SI1EdBlPVRXrARGrxKNzgeZ3LmJipO04veYfjavJONFCW4sztI-JGUPCfhOpEm1tAr7duOfpNRWG3dbKibQaCydebLU0SF6smoD6z9VVBIEiLWHqj_i2PtHxnQDCV7f2YBvG_LM-hz686xITJnaAysJnrKZnCiCogcN7sRbKSN4oUuemaiTs0KZiQ-nwIPcydkZqI6cBPFAP3jxH60Dt0YkESggoviU7hUcrewHcIqsSM9iBXrR-0W0jvb_7V72c9J-DUMhTeL8SCPniJnTTNx5m8V8Cpr0vPUyKqlWTCaMANn2QGI56dG3wNgutLAC3Bug9MHTqp3oMPKW3MgFR38" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
👀
چنتا سوپرگل نامزد پوشکاش ببینیم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/Futball180TV/101988" target="_blank">📅 14:04 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101986">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/KrHqV0Tg68Un3shsf_WJkWdaM9zgKeJrcGgWQggleuV6pSWHZc4yFHBnSSEIlVAuNawgRCXCRxjb89MkcJhf0qdqdQxDtJ-gLZLNK4E0GISkD-yMmwYgYRxQiwabAPAEOc3kO99VFfa-A76XenDHTfIUGHBf5ZjOtJWAYUXvNrFaSi8ToPOwHMq3uz9fBkprwoGGeM4SQZluWMe03pLWfmsEgJCwsiggBnjYV1gG11W5GznhRnmRJ6JmBEgVu5HgtHHUvaxoUg2F27TpdI8BIZNSbp13Lm_Y1p6MSwUm67urw9ddU5hGJpMkekm466aNl_GFzv1Ytv3F5mgaCfH5yg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/uialL1mv6dUXR2_hWVGJEUci8y2wRm-b78GTXyUKSn6MFmNsJQ_asxsqkIFPYmGIJeb5eY5wqznPf-ZXrOYhzlpi9dDxGp3xNoCNyXFFHLydeb7PdPwQegxVOmdUkALgvnX4icJDQnR1r91loefS6qfk0C9_cnhzTrGDWhgxhfxEYJsrsN08lKSGUFU7iypbZRmKJaaUzPFWXOmZF1hn7wq6bBO0HbO-samXmMyGUcbNQz3vw9ZC4MocIq-EDftk-RRhabKCCsRLqkjTna2R6BU7LuwIOEW-YdeY4lRmKupTach-lhoZ5OhevkCXtVdqpExCjorTL6VO3TwhaMA01w.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👀
تاریخچه رابطه‌‌های لامین یامال:
• 2022 — سینگل
• 2023 — آلیسا
🇷🇺
• 2024 — الکس پادیلا
🇪🇸
• 2025 — فاطی واسکز
🇪🇸
• 2025 — کلاودیا باول
🇪🇸
• 2025 — نیکی نیکول
🇦🇷
• 2026 — اینس گارسیا
🇪🇸
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/Futball180TV/101986" target="_blank">📅 13:40 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101984">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/CjzplorUJdOOeL3o-seugnWW1WsTP83233W5YuDO2P43MSRE_n1r_r-0tAou42RE2m0KRLtX4N1HPeGF-vMls6RBP_qETS_nrpJ0lTqbtTdQOlEjYNE086Gbsfs5zzmd_ylaG3MqPIvSR9hXC6xoD7XDf9a4d6QgvRYNb5vqIENEJV3BQzg9gx2QoO5GyoeRgr2CXyToIWy5kWZqG5wFyyiVgCv_qrEUbrBwFQdPPhLqBJRFgfl0eZ6YLhybA5PM8hh2eR0D1a6VnDTRcyPKqkta7wniK1zx-dhqIyzSKZmtWrs3xN8daN_YARHyq7JQYk5M4eTNnKKfjBZTkgGFGg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/QEo4Q1luxdVPcb1LBbhh2AJPmDr5DYt_M_kGELCvhnff8dKPlPXA42bXw31WRwT175gGLBiGEyXYzVvU1ymW7V5RdHPrum32Va6B5RrKZa-j_65vntPhPL3lfC8w-XN3RUd7hX0vNJ8uhsLRaUzx2q5WzS1DgR6I-JoKPwoHgqNa-DnN_3bRPJO2uqHvrKP2uYt6MVtddCiIj7NONfgA44gWjAXV7ZDS1LwGpWP7V6KC7zKm_eNqzd469bP4lWtJyvI8tnZVg8a0XizHcdKCkwBwBiWGm_0sGLTrwXcufAaui85ok62CKAHimfdpYQ5LpbqCrGbGy1TN9ioDYo9TPQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🎙
جسیکا توگا دوست‌دختر سابق وینیسیوس جونیور:
این فوتبالیست‌های سیاه‌پوست فقط از نژادپرستی شکایت میکنن ولی همیشه با زنان سفیدپوست و بلوند وارد رابطه میشن. اونا هیچ‌وقت با یک زن سیاه‌پوست وارد رابطه نمیشن یا چنین رابطه‌ای رو علنی نمیکنن دلیلش چیه؟ جوابش واضح و مشخصه! خواهشا این سیاه‌پوستا فاز آدمای اخلاق‌مدار رو برندارن!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/Futball180TV/101984" target="_blank">📅 13:20 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101983">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">🚨
په‌په‌آلوارز: دیومانده به رئال‌مادرید تا 2031
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/Futball180TV/101983" target="_blank">📅 13:11 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101982">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GgAGmWD0E5qLy7cmqgUfVKo3ukMbsBO1PWvpyI-0xTSQSPqho_J2GGdJ1DAvFTXUGGVurpFrpMbyHFsbR922xugLrZH1Q9U7EdOIsPaKtEFSw9BluxOl2TCnhIRR4NQ7mn4s0I9LAB-tlWxix1ZJ7qNcGw5VBOG3KU9PZX4_sOPLcJl3Lvolvd5o7Df2GXsNLxh35XmLBJIX_vaHBX9_bUuCVdwpPKs4Zw98WxSahd0V8gvTp0e0GNtp3uvJFweLYHrP3P5ZIti1oReliKRfnSUwJMF6cnZjCyTTQ-_-ZcDvHP9zkU4hWPS5rz4-P9cbeZ914xEvSIObipNkagBQvw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
په‌په‌آلوارز: دیومانده به رئال‌مادرید تا 2031
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/Futball180TV/101982" target="_blank">📅 13:10 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101980">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ShcSl3clP76t2Frq6l39gbD6wX4pk5d2TxT7wUhrX8HKwc-V2bRssWtInPgGRYRFC_sQPPFuakeHDeUYhk0dq6WfvS5eLbWkXuGs4FX9goew_uDvMKWG4G2Ic2vCXrdZOk0Ac8OY9fHh7KCYixPA057rtFBWM5jNo9Y8GhavU4TIYWDS5F6kvQYmtm5vuf0PlPz0DP67aiQ2Lx3hoKXu1YdvbF9yfiM4ovTO5k08OU5OkBT8aq3_9q0DPDJZ-kXmwdSoPZc4G4aGrlf3YNwkJMZJ71bi3bwX5dZvsd9YLIRUs2hWrMLotH9fGtzoXByMW2mlau6NCtnff5FHaUwGiQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/dLgNzB-yr20cdVU7GNVZlrokvxBo-_vXjM99n9U_A_x6JCQV5fvCbuQJPmF1cUeAz2Rd_d0JssueIKnTehBGkaItIeL_Dncbw_SzxbcoFyj5h-I3f7dxY1tywnZqW-LNUyOxk2YMhUoq54wtLXOaK3_x9Ez2CO-ovTvhscRKdT5KnYYlzxMyIRY4uu2jcQFpXvsBX0wca0tpdd0e7_0pluCpCOgETtJqHHXNv0UXpf71tgXUMbTii9ePuavRPk6r9CPzt0lQODZL-X-l7HSYNwGC-F1kVjFm36NnB3ZHEY-0BRnqkvp6cRICGwYc2jOcby_DsFbkbFFcPBU7X0j_vg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📅
🔵
17 سال پیش توی همچین روزی بارسلونا 46 میلیون یورو + اتوئو رو به اینتر داد تا زلاتان رو از اینتر جذب کنه.
🔵
🔺
فصل بعد اینتر تونست با حضور اتوئو یکی از موفق ترین فصلای فوتبالی تاریخشو رقم بزنه:
🏆
سری‌آ
🏆
لیگ قهرمانان اروپا
🏆
کوپا ایتالیا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/Futball180TV/101980" target="_blank">📅 13:04 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101978">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/iWdVSJPqE0zOVoKbsOgrpYeB-ceXhHFbFAr6gk-Y4E8-DrhfTIS1hKXvopq_76Zxvv1K7awC0fsEIXdjnh-c0dCgERFll7nGRdA0gbRjO2b7Me2lz2X46SxeDYs2CEPAiIoW_SPnM5_nSE-NdHoAu_NJj8OOyCUSkGyJ6Pre0zS0Flyl2LM_aNqWAuEaiRiVx20UJI_s_Lbgb92joOSuM_6k69v6Cn2joXIUPMTu0ANonOya6DrHwZjdApGFrzeE0DjtVTTnU1ieTk0oV8NEcFQ3bvvLbQQGaz61V2XNPIyXG_Ux5-Ai91D3EuX9QK_FKWagHzUheXwCc3ykfYANqA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/kQgCDL9ANL0rWnjkQVE4vfe6_t32VQVq8nJEmdPzd0FMwHSEFxO4GWL37xVzW9Ctrraulm70RfhPfol7yeF_AnGFLQMe7xd44HSmCWys4Ax2nUfgVp0BoLHeThuinNPKk3SWJ6xAiCQD9psNFu3c0CREu2UWsZjg8fNIQIxUvJsRPPE2o_6xEBqpKaY_T3qOVhQtoEu6nJvpuZ82KRhr0cSPRtL8C7IG7lOVwPjGEj1veOPfgowfDlYgeOvH7dPqgRW0PemuPAdnA8Q47Eoq7CnPrqDG_E8d3-p7zcn8byAFhQKDPIWiU2Vtu-ZPUq-crzPCf8iLOrI78e_KJ4UHpQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🎙
الساندرو نستا درباره غیبت ایتالیا در سه جام جهانی متوالی:
باورنکردنیه! پسرم تقریبا ۱۸ سالشه و هیچ‌وقت ندیده ایتالیا توی جام جهانی بازی کنه. وقتی بهش میگم ما واقعا جام جهانی رو بردیم، تقریبا باورش نمیشه. میگه: واقعا؟ برای نسل بچه‌های امروز، دیدن ایتالیا در جام جهانی انگار داستانی از یک دوران خیلی دور و گذشته است.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/Futball180TV/101978" target="_blank">📅 12:40 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101977">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GJ2Tpu1mSUo6lUGoRt4zOU4RLbRPzTgRD_kmDYoRMJMtCziXUfihPJUm1mTe-XdnzQVnlBlq6UO--QzosV69Zyd3rFQth5AX_pLisyKqQGHckHNFOlJXh5pY7l1goE978bow6FPLWK2F-2dd1lBsQEKQRniAtpnDqwzPlCD57LCqBB4MMvEzKUFGTbVc_wmfo5MLs8OstIBh2BaNuymKtGWzCDGJ-1YV8c4oHEgWFiSZ-jBPi_npHLE0P0yF2c9Fsurps6b3ZOtageK5h5YkucoXdscrmfUKVe_oEhUZ7HGMKYZ6lnjzMZtyugeW3LA35whjH9Ssgp1stfHdCVO09Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👀
🔴
ترکیب آرسنال اگه همه شایعات نقل و انتقالاتی به واقعیت تبدیل بشن:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/Futball180TV/101977" target="_blank">📅 12:20 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101976">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AKgkDaKvEYeRHrCTmvFXpUUakjUge5VkcxevSTvVoZmvYJTgCb9Bu7Hs2XpN3UKldu5TTYfHRuhM4bjpmVl4hZ_zwpHKmGMm6JHNw8pjmb60iMdQU2WrNkFFgvOuNFHNLmlUceuPxiiOJ6S8bc-8yNDqCGbS_qD51uFRvRPWRLIEIJkVv_qFSw9JbksFDCg5jIgz8h6viISWVgoW-vkt8rz1kbBidI1vY3VE1SAWXwPMaoStR9NnI6yOz68ulG8xTQbJT4s-Q4kQ0UJXHg9G49HVLEGQdK2R6WI4vs92pMaR4smSpwsnqk1Rn0c-fAki2m0M8AQf_g6S8WlxsGKp7g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🟡
طبق گزارش‌ها، بدهی‌های النصر عربستان به حدود ۱ میلیارد دلار نزدیک شده و همین موضوع توانایی این باشگاه برای جذب بازیکنان جدید را محدود کرده.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/Futball180TV/101976" target="_blank">📅 12:02 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101975">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7ddfc2f853.mp4?token=cfcLKdvSY-48oI6jcBc1Mub76I2ALfX9QtoO88GH0thauFtJ1j_XETAiorEMCtUGwN6hQyCprO_Bo1KmjG0gkzoQwsIrgmXx6WU_00nDTxBTXsdMt9LdHU5niPeW_gUR77xcIRRFTPqImeiWrZRayeMUWOVdAgp4Uvqvm8okLWPvTG9fwWLZyXm5XAKE3UOdJkVLHGsFqGk8i7965Z8JxPobUE3n7frT7fecbGba89uRcSH2kZkoIHsOr7bR0uEm-2EYXWOJRf9hnR8RhAODs4QPr6Im8cS9I0UlI_a2lvHCSdGYtKWjKAv5G0NmT1bjoQOjKFYi3hGaBtSlF5_blw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7ddfc2f853.mp4?token=cfcLKdvSY-48oI6jcBc1Mub76I2ALfX9QtoO88GH0thauFtJ1j_XETAiorEMCtUGwN6hQyCprO_Bo1KmjG0gkzoQwsIrgmXx6WU_00nDTxBTXsdMt9LdHU5niPeW_gUR77xcIRRFTPqImeiWrZRayeMUWOVdAgp4Uvqvm8okLWPvTG9fwWLZyXm5XAKE3UOdJkVLHGsFqGk8i7965Z8JxPobUE3n7frT7fecbGba89uRcSH2kZkoIHsOr7bR0uEm-2EYXWOJRf9hnR8RhAODs4QPr6Im8cS9I0UlI_a2lvHCSdGYtKWjKAv5G0NmT1bjoQOjKFYi3hGaBtSlF5_blw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
خارکسده جزیره برا ایرانه
✔️
خارک و سه‌جزیره برا ایرانه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/Futball180TV/101975" target="_blank">📅 11:38 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101974">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/v2mV_9QhXFdwEIgJfAzZioqbZuKQnR7Toukn0PHXzEEtc2HivFbLh8acj7BMYkpfWMf9Ttuv1tLUxIKGlnw2EmXlP3jEXs8AE27gouimJ-rC0b5v-W3HScL4NGSRumcrG4YVvolKG2YOZ_xNhadMwXCSBHjbki6cC-Ly2rSh7cUUPusLA0HMLNZa5U-QJC86Ui092hAgbCBz7OA5_3jnhKi4UF-C7iTwYLoII7CgJiUXtMvjwkZIOCBT8hNz5Fcbf8nDOt7f38uJPAmtI8cjUv2FHyirlIUsve8LkAhfKkMShJSVZqDIxfsGREFvqfr7vpXcf47QqeJluDPXEZGj-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">انزو و خانواده تو تعطیلات
❤️
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/Futball180TV/101974" target="_blank">📅 11:20 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101973">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/M47Vw51N1dQPJDn875Ba05hH2UpEjsdXLsat51ixBpwmmxABHzxa5obEfwkZP9L8Wk92Z9YEWtcmlNX6OjHZTeyJT6wymmR5zZu5x0gV4KKBgkv-kX7asqXBMsxzEewiCVjKl1weJvlvO8Bo73wkssUHjnv3NC32jjlNEkIGlaJFIlyNB_kxKQuOMpqq64yV0Bijceenf2d8VL_zok7ILxSEiAcbHHVoHCtF4dj4KG306XfdQe4tJf7-UPjSmuPY6lz807D6razqEOut3F_5jw6PaFzHlZmSy4ozrAvkOFYK6tV5rOQJoSTEmu-Pmu15hW8CG-MMqtKt1krtw9Bu3A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
‼️
مانوئل نویر:
🔺
هرگز آن لحظه را فراموش نمی‌کنم. مسی بواتنگ رو رد کرد و درست جلوی من گل زد.
🔺
بعد از مسابقه، بواتنگ شوکه شده بود و گواردیولا به او گفت: «احساس گناه نکن، این کاری است که مسی با همه می‌کند.» سپس به ما گفت: «حتی اگر صد سال هم مربیگری کنم، دیگر هرگز مربی بازیکنی مثل او نخواهم شد.»
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/Futball180TV/101973" target="_blank">📅 11:02 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101972">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9c941f7e49.mp4?token=B5QWDPxZD3DiuNOsnf53BE-l6isjE92ayER6iO6mwwzsAafF2GXiriZkSNe8DWOCTaLyWwelHau1IicMsGGGpnwK5pHIbciATQohMqtbI6-Iagy1NvWRtwlJvWJp0yDFuAJeBUsK21nOBZ3ihqYSyzQVrdG8xCmWE76MSjaUAmxCvNZVzgXjzQV9qtrlYsQqSq1XBBlMXYtCtgAQKSnyf1OTtS5Cg5XSg-1js_nwDeYmzCF-fKYdqsD4tY7nxTwkDaPRsDqFQuQWhiuOb2ycu9we71oi8AuMH0LlRoDS07efTR28TQrJhRpNhUr3BcmHHrMf1dAigxiq61f4SQxAvQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9c941f7e49.mp4?token=B5QWDPxZD3DiuNOsnf53BE-l6isjE92ayER6iO6mwwzsAafF2GXiriZkSNe8DWOCTaLyWwelHau1IicMsGGGpnwK5pHIbciATQohMqtbI6-Iagy1NvWRtwlJvWJp0yDFuAJeBUsK21nOBZ3ihqYSyzQVrdG8xCmWE76MSjaUAmxCvNZVzgXjzQV9qtrlYsQqSq1XBBlMXYtCtgAQKSnyf1OTtS5Cg5XSg-1js_nwDeYmzCF-fKYdqsD4tY7nxTwkDaPRsDqFQuQWhiuOb2ycu9we71oi8AuMH0LlRoDS07efTR28TQrJhRpNhUr3BcmHHrMf1dAigxiq61f4SQxAvQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نیوزلندیا اینطوری از بازیکنای تاتنهام استقبال کردن
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/Futball180TV/101972" target="_blank">📅 10:54 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101970">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/RkPXN9SzHnQRwCQnKcZDpTv7-iAtaMMTf3PzSt90UH6jrWkq0Xny9_wCs1oodyn0CuIomf4oNZNE1ejLu9HZfgn0zmZMLdUTWUxSkexIAsWH82TLAn0JIvmeaTqJszEftc_ONv5xnpVUhLvXSdpcNoczufRGbHeCl1cpjcQcLi-Y3PbxE1clNCNWu3VG02EhFECeoTkedyLJ7ucW5lgH2EyqnW4E5rHWZwdUuixVt-vnj22k6Q7srVDxZyyVIxwe4Xxc9ebfgWq3g-HtpQMSUqbQzGnm6pIF_0sAWW8g6UlnMPqDnzTiDKFtmpc72mzpUZFSQ0Gyw8bAw5j6E5biBA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/viXOTRu5jdHJnqiGEJQPt9gBFcH1u4d7t1AEIF-C1VIJvfln3x9gUn2_oIaI1frnc8XovIX7GzOQvTr4Pn6e1W6LiutNwt2_7DZrqMnVx1WX0LSRu_omEA7mKDhjGkw1wz8hdnmVZb2T5uMZiRfD5iFDm6qn7re5pcn2w1kIsst8pXcXcyVTqQcaE5kDpUHzVM-2PZ0KCdnIwu536guCApgtZY8-3mnqjwIspPLD1CVR5V_tB_o2u5VwNWYlzO9fkSSSdx8V8XC5mW8JFTqTObtEHCOJRThrh11yS9HjZn3btP90vuOP4Eg_fV2uxCtxQ3qnvloFf1a0uJD6jrxXoA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">پدری داره تعطیلاتش رو اینجوری تو اسنپ چت میگذرونه
🤣
🤣
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/Futball180TV/101970" target="_blank">📅 10:40 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101968">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Fhtj8042-wWOTEFagiuNAFLiaM8hJUEYN4C_DbZfJBw9HEHIUgvxzpo-K6II7LGEKaJ4o5-C5V7KBGTydXCryj9YrDMR7egieFZCYBNmsVVcXmYT6GHpMUS7kklWJeCCZCc8l13VmUTC68f7uUaH0hKm86jUNgz5TfQMd05cfGC_XfyC7jUjvm3MG9dbhHNpMMT4Tgen5JQwHvFLfOrFYURMJZLvJ1uti_iJFqyV_gg_cqHdkYZrMRaWyMGp1RlGC6MQ1Uq3uVU4M1HiAKelOGKgsKG2P1UJ6chq4yyPgOlrCqcGEmCs3eGXx2KLiWxeuxAWSKSLBEIsT6Qvk1oURQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/abDS_snCkCRU0q589IJHVcUHU_C0s_rNqqTy2OY_V9mcnoZjtbomFnALU-wgDKn39mOZAvcMBf6MEKmGPIldi1zBXAEL_v-4qj-AwUtBHAKkXUg11fptRFhJVUPpZOIOCCwIN5Y2Tov0N82S2UwxfGcy8zaG9UxFWPVcSJIta100KDqQ9njy8YrYUKHPLZm3HETJ7_zdanAJgFY-4sRKcWQGKxiQZMLtf0Ahlb27lx8j1iGFibfnwsty2JEFiHttpjh2ulpdZYbIbhhGMg_DbPeI8WtFhPuku7ewIrrpR2MB8ispA9lX7xIK4p7BgRv8QyUy0Ut5avn3cd83ia7-Tw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚨
😞
میگن نیکولاس پپه بعد کات کردن با اکسش تیانا ترامپ ( پ.ورن استار ) الانم داره با لانا رودز وارد رابطه میشه.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/Futball180TV/101968" target="_blank">📅 10:20 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101967">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cMiCH2TCtkoApRf6gQSDvwbjBO9sIuUa__wLqOZtjPbtW2RnhDFTcpY6bHBk61bo7pShdNMldmKWyjkk_9fp_KDDBqOGC9kYKt4twI1ypZUX2SWTsN3ZgPG_QLLerVHmtgL65USiWnaEGhvYU6srCK8qaCpTYl6SETuYwzXauCCSvuXgedSrEtRdrMFuaJ-LbMfXuf294Nav20pI_ZopvK0peTfYJoM5uOwZivCZrs0hnPj19DWGwebTk9DF7B3n_GRtV6bRkHjr1FvrSd8Y4MuqEYcRI_f9WwmXq4u4z39t3j5Rbk4ekYjHv0mgoZByNcIFSqUm5QCfsoBBmOo9fw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
موندودپورتیوو:
اگر بارسلونا نتواند خولیان آلوارز را جذب کند، دیگر هیچ مهاجم نوکی هم نخواهد خرید. بعد از جذب آنتونی گوردون و کریم آدیمی، مدیران باشگاه احساس نمیکنند نیازی فوری به خرید مهاجم داشته باشند و معتقدند فصل آینده فران تورس، دنی اولمو و رافینیا هم می‌توانند در نوک خط حمله بازی کنند.
❌
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/Futball180TV/101967" target="_blank">📅 10:02 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101966">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/trmEaUZDSm8rsUnKdgdX7RHkPwgsPdsuavnQ-bMhcJDaconnKCFNoiqMsYWk8v40qsvH6xWj1V7MxAfs1pfI_X0nWNSIkTBYU14fAQPLS7YIfUawZrvsVKDPB_uVU8xHyGOBsvcTozTJ2zDTVPEjPGvGcD4jZLbciM8HdfcFpP-oez1ZsHQHXYPmKHM_fJwxa8U6GF7YMH1ICYi0L0kGsH8le99cKBLQ57DDnDFb81a82OiMzsZlEPfakiooeWV3IwT7EcnsaT4PkywGw30ZSHJ-yqAWB8gumCJdxd0zLQ4w29pjaqNhT0Pv_1E_VcziPcGyLR7JLmj5lG2s3DYMyA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🇮🇹
–
فابریزو رومانو:
⚪️
در ساعات آینده، باشگاه رئال مادرید یک پیشنهاد جدید به باشگاه لایپزیگ برای جذب دیومانده ارسال خواهد کرد.
🔻
این پیشنهاد از 100 میلیون یورو بیشتر خواهد بود!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/Futball180TV/101966" target="_blank">📅 09:58 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101964">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/FE_u4F8rSuMDxfqW71Pw-W4T_SMC0lZENltR9bVV7KtUPpG030SC2IsnRuE_FGWfs3rNsGSe0yv25z1o7HM4LuscYyF4ta8uVyJnh955xEs6EItVLMhBF9WqK79ODFXqRMWcmBOw8oW4daD7yrgQVzMUSAcyxFZ_K7_uOnt9-JsZWY86hvMuO6v6oRe2ndQZXmDDDYeoy2XRbKLpqN9ihLO9qCNTzCJoLzD7tS76wnoNdp-1QbT6jkL6glG9QzJrdJE_xFABI8j-xr9ysT_5mZ5XPxUYDCiAZrPS3USF3rLrRqk7HPnz-hcN9b490uCItUC7rOk_4LFgiXKWFJeYsg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hkixUSbYIaIYcEZH0i1l2VpcEDs5VGJkDASA6Wl1cSEqg_VwybQ1NCqrwKCQb-oFtSP1z9yvTOljmIq0aFPMlAJ7yNHHI8x0PYt3OuBvzCqxBZTehYPbqiWXTvEkirHHMybSjoXOSqSvfrI_xLis-Bh6thaqJV_mId2rMstkWgiPQvgEsKQc_RCY00n_-OkRaskMMzuaud8DhFKhzaODNiHOKZYqYNrryIGVNoxXmnn49xaGR1f9mj4xxIGC9RTIU5JXqunfROduGz5eniIeph0h_SNl9hUOqaPiEW2x1iHQuZB7iBWqZUVeMoD8IawgxFv9XO6MVbkJSmruNkskcw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🎙
سوفیا رین شایعه‌ای مبنی بر اینکه حاضره شبی رو با کیلیان امباپه، آقای گل جام جهانی، بگذرونه رد کرد: من هیچ‌وقت با امباپه شب رو نمی‌گذرونم. هنوز باکره‌ام و خودم رو برای همسر آینده‌ام نگه داشته‌ام!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/Futball180TV/101964" target="_blank">📅 09:40 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101963">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/G7DDqU2xJxNjGS0c2jA80ItM7_CuJ84JDM98rwwhMRkZA_MKjzqtxLI9WLyoQYb78lEtUP7VhvLxHSNV12mwVNU2m1ggs-hjoR9rmFNZNMp56gK_AIt7vbG-r8WrRvmnIwXSQr1PJ2GNOIV5d_8ji-0pJVciqzcdGqKb7jEqKU99bJuEC7WZUP6MXGTzSRrt9Pmzgg8LbSbvk5svlbwMO_jTJFp5bXCQfrVAMLbbHBERPTJa8QyyZNnuxTv1reXJ6vd7tUxBVlOye_jy-6a6i3udDKDbEXIdKQiOnyFLrNrQEDhlUQsf5lvoyQJmrOjOWtiuXDo0kB-6ZXJ0JZjKSw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
رونالدوی برزیلی درباره کریستیانو رونالدو:
فکر میکنم بازیکن‌های خیلی کمی مثل او از بدنشان مراقبت می‌کنند و این‌قدر اشتیاق پیشرفت دارند. من تمرین میکردم چون مجبور بودم، اما او تمرین میکند چون عاشقش است.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/Futball180TV/101963" target="_blank">📅 09:26 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101962">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9f0d0985c7.mp4?token=HiuT2WjGQrE_ee_0_0kBXIxNrg_2iDuIYm02Np71QrR9hVI2v-fmfE2LUccULQmn7H3GW3NpbHjgk7yyoHk7Uk-Bg8DZvmnB88xYN4yq7yuUWSe2cp2fnKPnunNHYWIq5db_Xy8qWt-pb52zLSDnJebXlD4dAxcOG2V08RWjzTdHDFzpRVgXCy6E4SdflRpxQQEaLERI3sZSD8dYZVwuDH0Bo7yGYbzWeUQMYPf1hX7Cq0TOE_xxfxEBk1FE2vAsRBq0g4EHIVzPMJhbDsbMzJAQzzyaZR4cnyidQH5VvHoLBUGhjfVi8Bp1Oxa_QB3iUTWIWyCHs0B3E9mnDltRHA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9f0d0985c7.mp4?token=HiuT2WjGQrE_ee_0_0kBXIxNrg_2iDuIYm02Np71QrR9hVI2v-fmfE2LUccULQmn7H3GW3NpbHjgk7yyoHk7Uk-Bg8DZvmnB88xYN4yq7yuUWSe2cp2fnKPnunNHYWIq5db_Xy8qWt-pb52zLSDnJebXlD4dAxcOG2V08RWjzTdHDFzpRVgXCy6E4SdflRpxQQEaLERI3sZSD8dYZVwuDH0Bo7yGYbzWeUQMYPf1hX7Cq0TOE_xxfxEBk1FE2vAsRBq0g4EHIVzPMJhbDsbMzJAQzzyaZR4cnyidQH5VvHoLBUGhjfVi8Bp1Oxa_QB3iUTWIWyCHs0B3E9mnDltRHA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
⚡️
بخشی از گفتگوی جذاب بکهام، زیدان و زلاتان
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/Futball180TV/101962" target="_blank">📅 09:01 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101960">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/pHm3MhgRiLeWhdiL9vOi3FrIiInoc9Jlg0A9xCQ20FVuvEfS1VdqKVNzNxgq9unRWCa36NEA5phA93yG_JJBQWQQtTgqn8crXoY7CdvRnc1NkCCqz7xvRBw1miUCkpmBhzRFdqW8AJXQ9-SeoMlpkYx4aC76ZHoy1EXpWxvmEkmZyN-3yB2UJDSkZtdKtaMha_dl4wSx4PXnsJ4DoERI-pEXT9-X6YXMYS7mwXm1iJ7j4r0xEgYy9z5jT09BNSWEaP6mr1H2BcYeBOW0Jy8Yw8-G7T-BtoV-gcUCFTaitxt7LEeIceZ-S-IUQhgG-6kSq4k8DHFNmH7uya_cd5joBA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/b8H3EUEXIuAEvuGPJbXKbPhfDQEGlF7QsKyu8I2yhvtPxkBdTQzxXZD92MJHTwAyDxTdPJv_pd800p4XMp62AeM5_rBIvqhYZpuoxZauYiBpDiM6n7CTW65G1PV70NO_IfB-ZW2maSAbiBvCPs5uJbXX8V_sBy32cWaXADW-JkAvTOdPT03yHm48yYN7nBhhJ3SW_Qe8s3nT1Fhzm0T6R9q-rVOqgK9UV0wvQxlevtYY_JS31MerCLFkyhoJytq9W0tTDa2SubkQrxK6xEh8z6mwWnZuo-HIpA6xwGz2JFrxgXCwJs0CUe9zs3tfumoP9Xxp5As9rpBneoJxTmXLbg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">کریستیانو و جورجینا قراره ۱ آگوست با هم ازدواج کنن بالاخره. تبریک به این دو نوگل دیرشکفته.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/Futball180TV/101960" target="_blank">📅 07:32 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101959">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fq4T72jm-5qDFGMp8BrjrhRVv--vT_bieAd-D5i6XZsKQXmcEzZVk-WxaROyp6R1yNx9mKVI2Sep5gnXH0wn_0Two7A6Nu_nW_c_SdmLSPigN0JKZqAxrCl2gGMb0t4vb-IJ3WAIghbyZE5Gn9SZGokGSzowyF7bl5X5iyddPgfvnXXXeYuYB_d1l1r14zOjGJfmQjt3A5Y_VcHpM_m27f3fKegE9DmkAs2Vej21Hbg8O6RrodzKwrrc1IvUWAEwXjrsUUx6I4wFdcW-SVGn-c0o166ZboOHRgL0aZqB4MKMx1vc2saJxxdiBAgE2GjLhzm3KAj3hNpeZ5-jFD2shw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
👑
موندو:
تعجب نکنید ولی احتمالش زیاده که لاپورتا پرونده نقل و انتقالات بارسلونا رو بدون جذب مهاجم ببنده
‼️
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/Futball180TV/101959" target="_blank">📅 06:56 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101958">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/85d2fa751b.mp4?token=Y4Ma5ggHT5LxEVdd9Kp3ei3vndqJhPe4efGfmuTJhv_F9pg823U-0XLlg4rVvikdCHVrJuoMqTgcq35Jl6ziQihUwOZc486JpuYNfk-d46eb3D3y4NpVahqxhWa1JLql75A5mCWPTF4piZhjI-lhcvE9ut82Iph1ZzP-hW6kXGXXyHY0bDMX1RoiFFPGceL0K1iL6t2PR_tHWrT9uh7MwBaM5_rPrSCbS6WnJibZctei2m8j5jVH_l4eNUSMI4Zmu_kBkwDtpCdUaIEzjRMX2PW2T3rWd2HeECLQy9WYqzzH647skt9OvAqlCNUgIvDJW0FlcbIPg-5oYd-NgelMoQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/85d2fa751b.mp4?token=Y4Ma5ggHT5LxEVdd9Kp3ei3vndqJhPe4efGfmuTJhv_F9pg823U-0XLlg4rVvikdCHVrJuoMqTgcq35Jl6ziQihUwOZc486JpuYNfk-d46eb3D3y4NpVahqxhWa1JLql75A5mCWPTF4piZhjI-lhcvE9ut82Iph1ZzP-hW6kXGXXyHY0bDMX1RoiFFPGceL0K1iL6t2PR_tHWrT9uh7MwBaM5_rPrSCbS6WnJibZctei2m8j5jVH_l4eNUSMI4Zmu_kBkwDtpCdUaIEzjRMX2PW2T3rWd2HeECLQy9WYqzzH647skt9OvAqlCNUgIvDJW0FlcbIPg-5oYd-NgelMoQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📊
🔥
نیمار تو اولین بازیش بعد از جام‌جهانی با دبلش کون سانتوس رو مجددا نجات داد و با نمره 9.4 بهترین بازیکن زمین شد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/Futball180TV/101958" target="_blank">📅 06:36 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101955">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/DipzqYctYKguLMXg0YCGnkvfceh32ZfZX2pWJksh4nI4m9QfcwVDdmj72QoxC_QLEJoH2I-Jg4b_jCJWlDMtlLiJXfaUAwwsPA9JWZeKzaNwBGD2zW9dBVJlkgKpNWGCvl-ZkQD4cDZ5fGsfxuQKkmuwfDFDciRUJSkIdimReab0J-smKz0lvYc0b6bCCMIkgwWQcm44Lm1k0FuJO3zhlKd98kBNy47tSONoTdoDxKRW5uL594d1G9OtrDk3uFK5-BVHl3BjTzjk7FhNFQJBOzexREyQfthAod01I6UJwOqGb0JHHCVq8NHGiSf3thqbFpN4CYqTJGQwlveaI-gy4Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/mJMio9IJjvtp5hj-fvDIbj3tCpR54C7M40m1uzwt3fuCQylHmbXGfdXGuVjYA0UTtIEdnSkSSxD0yNurEPcEnKy1QYWjZodTJjs_Tz1y6M0B4lzNkCeQsINWXGxZnAHQRpiPP7r_mlBN-xYK7Axg9E1Tkmi-yEP1VYx8jxuR1vw5BNzOINhgOyNcmxuzNjR7iSbiV-fabdMADmVNvmlMDwxH1iQXm20OnC-0MLpwbi8Emz99rNvqXNP6rQiwXKwhFusHGWzouSiB_IKUMJQh8-0ZJQ9OX0Vld7xbvOXcFxUi6GBSk_mP05wBZJgH_ExG2hQXkH6-mvioQn8s1MwwUQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/953a60dfac.mp4?token=sbQ2i0UU9SAsLh2nHepAnUA2bwymvq-N5ByCPc9j_jFrAw8FMDiuJbvlBxDZyB82PQ_hLOXJzwFotmnSnrEkb2snk8F6chNY873NI623RIRZecpDkECy0cqvsq8MiDJUYrYremG7IFAbnUU5flfujkjaPx8-b_ibIVKJUHDLbvJPSYj6E9jwphnOAkKE0DwIQSol2H26txV6MOlv8bR807Q8pgkNojDYKtjtIbXrJqHQu6xUlEwCyvs-jz0qktB34-rlWInLR05LuwXTu-7GOQhXskp_Da3tKjtqkijhDGG3Vx6-MI9Tzp2jV-6EKEqPYVdSVAtI4c0aTfuAA3VkUQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/953a60dfac.mp4?token=sbQ2i0UU9SAsLh2nHepAnUA2bwymvq-N5ByCPc9j_jFrAw8FMDiuJbvlBxDZyB82PQ_hLOXJzwFotmnSnrEkb2snk8F6chNY873NI623RIRZecpDkECy0cqvsq8MiDJUYrYremG7IFAbnUU5flfujkjaPx8-b_ibIVKJUHDLbvJPSYj6E9jwphnOAkKE0DwIQSol2H26txV6MOlv8bR807Q8pgkNojDYKtjtIbXrJqHQu6xUlEwCyvs-jz0qktB34-rlWInLR05LuwXTu-7GOQhXskp_Da3tKjtqkijhDGG3Vx6-MI9Tzp2jV-6EKEqPYVdSVAtI4c0aTfuAA3VkUQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📊
🔥
نیمار تو اولین بازیش بعد از جام‌جهانی با دبلش کون سانتوس رو مجددا نجات داد و با نمره 9.4 بهترین بازیکن زمین شد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/Futball180TV/101955" target="_blank">📅 06:23 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101954">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RsPe9EMHS2NHpWvpc_bj15aLJy9hmbN75LYxLa-91dbxxJBVW0dIk0mg3fgPHU-1W1Hl_BcuepDuJ4XaheY6kV13NPmV2ZKhSsxh3fz1g-q2kF2KBSevloYI8ISHHR4yNQj-ExNwTkMn8275cvmJQB4hkuLZbaUv9GJvZWzQR79ywDpt03GqZjS-WGrmsTaoI_fr4y8THdF-kZp5R95HqY_i7K1DoUBjkFHTnunNKt_AMUFY0S5IHpACCm-V3zrCbMFX3VNR9BXJPZPWHkGzSuAPTN2ZfB5KOjgyWL4g6f3I2q9pnyAFonzKR1LoYZXWwBNCeiqgo8OS8Y6l2GuiwQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👀
مسی امروز اینجوری تو روزاریو شکار شد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/Futball180TV/101954" target="_blank">📅 01:41 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101953">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/44643cb150.mp4?token=SpQoi2w9TpKb-pSuqkyb9CEJ-3LpC2dZg6-sH11m6vwW6IvXKp2YmC3jo_2RmioeMyndh9dLxJleaGj2Sn90KRF8UTDbjmicXRuinFDl6xtyRh9ydpo9r8uc2TpH04H5unqBzGbfkI5TWO_LdJaCoyw_M-wGYP39cun4sfq_KHnQjmF3lnqrwdV86B-diC9BsBAe_Iwjf6M7Wj54Lwm-e1hmoKBDI2gYaADtJaI1qy1xWws6OIeTF4wmt7o18bRzz0BsPU_QlES9rNbSSvK8Nw9QG67RBxLVc1HdwwdLsOmW_GVwySv9UV_AbGS8tCeibe_eyXT7VUARGse78zyu3zgoR6wYW6moRiZ1m3-Cwb07N7H0yNuH-FoeoHRBgIQeAD87iUqTESiQzfMFjTNW_oXP43NQhP74LuIWSR8KarQ98adNLfHra7Ir0kvnhKpf2nLKpNy_6gYIP4k1kx1-ja_HKo04_25goippuaKCtYH7-r9GC6X_obPeNrWYflSUoMc1AdHoyi6aYqPPmRad4T2pGgVeD7oEQPNpTdll-TdgZiLTJKGgSkboH4VHGb9kkHSUqgbs6nFarD-R-NWwbtIVKd4wic6uZJGLoOn4VJcBsLZ-94UD1T68nMPduhXMDT0seAYD2uRl-GIzANfaF0suEusM5YxQ00bEf01jaUc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/44643cb150.mp4?token=SpQoi2w9TpKb-pSuqkyb9CEJ-3LpC2dZg6-sH11m6vwW6IvXKp2YmC3jo_2RmioeMyndh9dLxJleaGj2Sn90KRF8UTDbjmicXRuinFDl6xtyRh9ydpo9r8uc2TpH04H5unqBzGbfkI5TWO_LdJaCoyw_M-wGYP39cun4sfq_KHnQjmF3lnqrwdV86B-diC9BsBAe_Iwjf6M7Wj54Lwm-e1hmoKBDI2gYaADtJaI1qy1xWws6OIeTF4wmt7o18bRzz0BsPU_QlES9rNbSSvK8Nw9QG67RBxLVc1HdwwdLsOmW_GVwySv9UV_AbGS8tCeibe_eyXT7VUARGse78zyu3zgoR6wYW6moRiZ1m3-Cwb07N7H0yNuH-FoeoHRBgIQeAD87iUqTESiQzfMFjTNW_oXP43NQhP74LuIWSR8KarQ98adNLfHra7Ir0kvnhKpf2nLKpNy_6gYIP4k1kx1-ja_HKo04_25goippuaKCtYH7-r9GC6X_obPeNrWYflSUoMc1AdHoyi6aYqPPmRad4T2pGgVeD7oEQPNpTdll-TdgZiLTJKGgSkboH4VHGb9kkHSUqgbs6nFarD-R-NWwbtIVKd4wic6uZJGLoOn4VJcBsLZ-94UD1T68nMPduhXMDT0seAYD2uRl-GIzANfaF0suEusM5YxQ00bEf01jaUc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
لوکاس هرناندز: «کیلیان، اگه قرار بود یه تتو بزنی، چی انتخاب می‌کردی؟
🔺
کیلیان امباپه:
فکر نمیکنم هیچ‌وقت تتو بزنم. دوست دارم مردم من رو به خاطر کاری که توی زمین انجام دادم به یاد بیارن، نه به خاطر تتوهایی که روی بدنم دارم.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/Futball180TV/101953" target="_blank">📅 01:19 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101952">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vt5bwYwpp_NcrRgqgOstHDy37fot0e_lG_OVPYkEZliNUwZXfn-Z1juPjG6fCMy3c3EIQJK7J423b88wtInGsRv7upiULdgGPFb6uHm3y81hM7_7JR6A5Zu94v37_7zi0Fq8NoFEXSufNfdferubApWZxBfvSOsIbYBzwQgdXXndu4n267GdnpxRWFJJbe0_Vw1nVLJS8Atfz0_jtryBBunHl5rMAPRCmVpakoQedn9E7SM5anBaIXPlFqTdehysAogXfP9jryuzlDnQoar9YwRbeiZYMvPYi7ezjAYOi8-INVcTfN7e6PuzuyyVSdkFfczhb04U9RSQZ3jFIqkn6g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👀
امباپه و پارتنرش بانو اکسپوزیتو‌.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/Futball180TV/101952" target="_blank">📅 00:58 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101951">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/irn3lMnwmx92Nov_H6Q7-GADMt6n_viZNPJiZ8k7KgGFogLTQw36ooG8taa_B8Qu-VcgfESPChkP0MboijFNnBH4WmheRfwh8EMi-qdar82e0TnFhVvun3nzep8113mCPH2oxrIAeJR-bCWr45tCyduLWQk0lToOXbOeIpmPDPEVAqDf_fQ3UmNKkTQeWMjLm6NMZQ2GLVTZHo9QeRZGvzE_S7VnhA6Ye2ULedhnVEDp2v0qhc-8sHD8KAbcqLLA36CAtVwRvUlpJNCN1qOU5VhGyw0Dttb5WwstaDKd99fmGNXUfbbHGoQO7sB2DbFxOOSsxbve4ddf4gIrkIVhuQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وینی خوشتیپ
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/Futball180TV/101951" target="_blank">📅 00:51 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101950">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/63dd42dc4d.mp4?token=Z4p0SpqqzCIxtsyXxypOVel9BjDLJ5u3PlIWD7JhNGEtUo-3q-6FIUAmqheGyS3GLBrYo6ehYovPntsTwW6oIYqKjnZVVaMK5KdMQ-YphE669SdgAFNEpw2zo6LuNbWc2fjXVjdO_NLndM_s_Lj8WAoGNjKk_vEYeesIzcPvHkI1vgZKUjD8u6F7vWCo7W8yEZM0XUWcjstGwGqwnFdypgoHhCl6HnBJIjN1NpDyCbGDyRI8l-8G8ANTVQ1D4SnTEsfngB2sW_8kkrYjNXQufL0y5IgR9_yyo_v9GU5WTvsjhx40HkB3DVwr17Hxyg9hZ_NLFnZx8VwkQoBjFACGiA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/63dd42dc4d.mp4?token=Z4p0SpqqzCIxtsyXxypOVel9BjDLJ5u3PlIWD7JhNGEtUo-3q-6FIUAmqheGyS3GLBrYo6ehYovPntsTwW6oIYqKjnZVVaMK5KdMQ-YphE669SdgAFNEpw2zo6LuNbWc2fjXVjdO_NLndM_s_Lj8WAoGNjKk_vEYeesIzcPvHkI1vgZKUjD8u6F7vWCo7W8yEZM0XUWcjstGwGqwnFdypgoHhCl6HnBJIjN1NpDyCbGDyRI8l-8G8ANTVQ1D4SnTEsfngB2sW_8kkrYjNXQufL0y5IgR9_yyo_v9GU5WTvsjhx40HkB3DVwr17Hxyg9hZ_NLFnZx8VwkQoBjFACGiA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ری‌اکشن هالند به میم هایی که ازش ساختن.
🤣
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/Futball180TV/101950" target="_blank">📅 00:06 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101949">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/k8PqW72NY3VBer5XpgINkS0OGIqKSIoVrUYgAECOsGaofGMaSctMjYjadGlgLHaZJ-azmk7zigGzX9seVN0eUodJwhBd_SjyXUr2Ldr890VEK4JtquI8KFedTlj0onWTph8IkGHmSNor_iF_FPSoQ-HyminnVbGrHB_LhGXJaQBxUci7A5UZuO6ts2MBstCLGuZLavJJngHDkNbQyGSh8nPfU99pfACBonz3Ej33K8uzOjMgHo4qXDgzE5HsGtCoEVnSXtixVNwSAYuRNI8aoZpF8tQehl4AUz4-51DopWVIS8MUghsq12KtBpiY_FEtjzhVAq6kE-J8zqL3SR_n9A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
فابریزیو رومانو: رئال مادرید و دیومانده بر سر قرارداد 5 ساله تا سال 2031 به توافق رسیدن.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/Futball180TV/101949" target="_blank">📅 23:59 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101948">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Iase3SUsnKF9pZK9CAR4mKw_WjXGXUqZfqs4NgEtpIga0eNdR-E7hRC2icmNbIhijB0sOZ6owOb1J9tkdSse_fQeIpIMIhAxCnS-nAAvVUSVAJCPoUmUtFmC-hVP78U9TanAMoFFzRHL5STJH5KzQX-QiWJeNww-M8yTyaJUP84DcFbR7bbwu9-KPfCx1OmQhu2KJK1oMtdjahrBRmLf5iuVfIiSVBRjTxlnjMngd73Ly89VTkQWdRhhy52Q8o1m1sHANTUK-Muf4Av9ONVtRNaVmwz7LkHsmPi-exwU5QeQGACMyuLUBrmKd9lXp7HrrOqRD_PZUI4_7Au03taVWQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔹
ساشا تاوليری: باشگاه الهلال میخواد مبلغی در حدود 120 الی 150 میلیون دلار برای جذب لوئیز دیاز هزینه کنه! اونا بودجه 350 میلیون دلاری برای نقل و انتقالات کنار گذاشتن و این تازه آغاز کار اوناست.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/Futball180TV/101948" target="_blank">📅 23:37 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101946">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/fj2jLjQTB8BAbMknf3BnvQ1HwnN4wFmcVTz7FQHvfszlArE0fE0O4MyETzoRCRbFoyV7lS4ScDv2XezmAXNYkByTmjo_OxCmpN6R8WxWV1VnCwG8IW9m_A8B0Zp3wvVld_btEpE8ovtbznRErSvLXZUzCoor0BQJvec1ytAs1_pH71ZMGakOnydz7YPNtpsjuyqkpp_9PDclBYiTRp_yiG_LEcgAiXfGXuMCm0M_MyHmVEQacrKheFD3VW3LKp9TQfEJmNMaRifISpZxcdA2HtbL13W2U-Cq72pVERMVqd2-jemfx3Q_xtj1j-WWxSaRrVusNBTE5GKEAuLvvjnBjg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/pMD93ptwkpHsXnKZ7mzHU_aAxzZn6pACygJ50LhlD0wp9O9Hlhp3p_zO_w0kP8ws-Z7kG7iDk_Om2eDfrumW6oP1yFomgPB8m-lcSMi0ggwuvdW4HOIUPetrKMJyjn6trVAz-dbeItTSSDIHQwTd172iTU8jocErmlC8hD5qpIKC6LSPIuwLnAd3ay1p8t2aS80SydKbXWq6do3x2D3FJy-UGmQ8qv8T095PB7S1aACN5EeD9LnzFhGKJILHo6OgB8ODaa-rhhLJ6qVpn8-G7rDy6WuSoje2awTyRFoeOXvwUzgwBzw15Kq__TcUCXuf7ncdJYG4fuuBrDs3iNUhSQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🎙
سرخیو راموس درباره اینکه بین کریستیانو رونالدو و لیونل مسی کدام را انتخاب میکند:
برای من جواب این بحث خیلی ساده است؛ اگر فردا فینال داشته باشم و فقط بتوانم یکی را انتخاب کنم، کریستیانو رونالدو را برمی‌دارم. مسی لحظات جادویی خلق میکند که کمتر کسی قادر به انجامش است، اما کریستیانو این حس را به تو می‌دهد که فرقی نمیکند بازی چطور پیش برود، بالاخره راهی برای بردن پیدا میکند. چیزی که بیشتر از همه تحسینش می‌کنم همین است. استعداد یک چیز است، اما در اوج فشار درخشیدن چیز دیگری. وقتی کریستیانو در تیم تو باشد، همه تا سوت آخر به برد ایمان دارند، چون او بارها این را ثابت کرده است.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/Futball180TV/101946" target="_blank">📅 23:31 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101945">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OdSRXUeHFLHfSm42UAeEfXi_pixIRQz_HiVBja2x4g5QIpCTZsGNKPTQteS92dn3M8-ijQVKOS5GUj3Ov--X6lmzxCaInOmQzyVqMvcgoG1KjN75iXjyP556qlIVZl-p8IHKionGTX4mr-V2wu-IvOPtZSyCWwu0-NXnhW4Wf1Cjaejb4aTfeO-IXoaAy8iWUKJNg-mmn93hspcb-8RSGl_gBFMc0s-u8Nj5xLwvXYoHJA9uRgdcrVRav2R9VZBIaRlC5_IaHUE1eEMrmytSnU9sqPyMg9PMZjk4UrZAJb7WpzMKrqyhGlN49maj0vY9gin2fQqjy77oQMmK0C3I7w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
⚪️
به نقل از فابریس هاوکینز:
مایکل اولیسه تمایل دارد به رئال مادرید بپیوندد، اما بایرن مونیخ درخواست او را رد کرده است. رئال مادرید تمایلی به درگیری با بایرن ندارد، زیرا رابطه بسیار خوبی بین این دو باشگاه وجود دارد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/Futball180TV/101945" target="_blank">📅 23:20 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101944">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kMEzxtJKITcaoaUwMjtBOl91qyEV_w_RPAnZacKMQcpQa0pyq2-021JnB9iu3c0p8HWLp_nZ0hzwleGY2GsfEF8gU91BufcG2MOT6PiwEElVLFrQ0Ta5OrFWD6Iol2w7fa5l0sMRS0OFqlIOsOh2qHCHtsxSB2FV8A8_6X_wwX8wbhyYlbnztcH5rbKghDJfIn_R5B4BvjN_hyo3MH29MncWYSae8cBLExORG2tgs6axQIaYxpQih12x8FAUBSMQUgMLwyxUiG7xFHviQF92g16Z3GLwdFBlSB5tU3gohpyL4k9GZXLYTJ9I0bMo7R9-EVKmeOdXfXxV6NQIL0b8QA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
فابریزیو رومانو: رئال مادرید و دیومانده بر سر قرارداد 5 ساله تا سال 2031 به توافق رسیدن
.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/Futball180TV/101944" target="_blank">📅 22:53 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101943">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dtJ7KWUzevCoIlOGOonKoKPlS4qTtKL8XvYRNBo-jgp8Y3hTk7AleEVbuzDyNPL44cHYnET2goLLbihOd1RqGEqgkzJ1mQaHHMEktTcnRsBIaBEAAinIjhTELjaRiLb4TiNwuLaWaQbFf9ppg2HKXdXtq9KHeGBwS4BB7WetAs6fw_CaHGp3SVwpwPXkO0wy3utuVCeY0O_Gqd7Mg-b-jcAqVzRyHqKlyXadWWkMQspIxlsYfBVumo5g3FZZetKfFcR5l8FGdFaQO_MjxbijU4OFd5cn_AnzdhDTqUH5vPCrliSbedqCtZrz-ZVv0G4cNm32OkHIId5kI-SeNkIeDw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
⚪️
فابریزیو رومانو:
رئال مادرید و یان دیومانده به‌ صورت رسمی بر سر شرایط شخصی قرارداد به توافق رسیدند.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/Futball180TV/101943" target="_blank">📅 22:42 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101942">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Bh91kHPRgzXgs7evHLu_349X6OO7XnXcR0XPkkjiJyys5LvLZxSB3csS0xmMIP_glWVoELZ4b9YnHVSTazE2RGwQkSCqK4g5gtcREmtG7Ye5nzgmLWTsO0KWT4mzDAFZ42coSibPrTzYGczfmpGfxSXCiHqrPSLDLWgPg295qls2oFTS1MXH0xb5za8EVTLjkH4AeGVtr5o1wLl8tGK4_YAITI-dkbTDGv5_ILHXgdqqD4bjitYpg9VoLJqYJxuQMYEk6WGMyBc3r6lJvVhoUBPSgC_8vvkv5MLYcdbUaheLDmL-5wFkW0MGamb6Fs0z-UMO5Jk_EWMxbH0OMpzflg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚪️
👀
ترکیب احتمالی رئال مادرید برای فصل بعد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/Futball180TV/101942" target="_blank">📅 22:32 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101941">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rAEzyKG2KveHEJQx8GEPl1a3M2lenUuVydYE9d0Kj_ONwqU-fl-70TITFrR-UQhAxHDavB8q9pF6pQDZHwHA-FdHiElZcgDn77VLu7piiWZXZrlE9D7MWXRsM0NiykwA0H28L4dypNmvP5X277MyrT0WizlZwb_h2fYLHjS5TpSMWElq1bdm0jzOrOwz1R3k6FyV2tKQU6tTttt5xUdWPjXG5XCvpr0GmEPjNJIiUzny5sj34G9G4dNIp6kRWhUlrq7vJfD6Tr7Iz_uY4mzWAYxdB_YaMnza3M3wnsQJ2LcmywyY9iSxllOe7P987GmzqD8OXiaz38puImNWbYRNfA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یکی از قشنگترین تصاویر جام جهانی؛ مارک کوکوریا قهرمانی رو در کنار پسرش متئو که مبتلا به اوتیسمه جشن میگیره.
❤️
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/Futball180TV/101941" target="_blank">📅 22:10 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101938">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/dcjt12D0z2OvBfrQRSRPXfyVrMCYfaJFrBeNMHezs1EG3zo-3ItD1pXCENZNTuVTU2DkdqUzRhNC_DVGqFpAxwzZjQGZxFswkPPGP5yy4-B3s-ykt1ZAyarkuvCkUCwx46kQJZO-ILmwxaEejxG4AnHyHU-fG0Smwlmujv2AixXIZlnO6IfANE58ufHtfmc9P9_tGuRH710W_BtIj1MO-53xJ6Iq6k8-8XQ8-B6sJYHNDnPx8EUSXWYMmOl2x5x7_drjkyxUxK1CFMxRCiH7fFmbkyEe3oOWKZhVQ8_MmFUOfUAHZ4bgnuCKhUAZS2M0DMPFHf9fhuFXc_Bv3xBiNQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/SRxHS_2FS3XLL9Ko5Tayq8Ggy8_1tiHlV0B_uXVKFrWXFfypv9SS5MrBJQAEwjI_cnIIRodfySSBx31F35x_zqTg4bW6BgXTru2MPmjRMj5hhB5fwQ3NpAZFimEONrrvzFYDOF5dUudrKyAsyCCZJSIyERUxFGFCyjQNRqJ9QiIyvA228S_w3NMCTH0Hua-d_zUtViTqwxxIir_yRQ3cnkSparDOR7BNrSZFHXkULkInZRTl9GZPRk6HgH4LOcwB4ZJhsTK3knh_T7K1e6HKdt2krzAX6a9Wq3DVVmTw0RH5w0XzdXeFmOa5O2MmHvvyCAJq6ir5ztxae0T1P7BJkg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/X4x2_HRhLIG72xVS8KJY5St1wO5YgQBYSBQCa7mP7nwfNPzylysnZZu5gy3jCiGEZueGvbgojamrORa1p7JpueSiBIpyTftdkRl1QcM0GczzYaPMj_oQEDIY031gxGxozMAi2DhVFnCcEqLZZfY9bGyBnGmVOIZVm6xzu_AtbBZMnfNcFSyaT0HOENfacTMrw-pDFxECshrj8qdP3oFITBDqfbfeUc_V2R3W5YRHFfQWWI_8IDgvHWOZi_IzBmjcicY6IUGGgxa0WleOJ-v5qP22Bz4rhQFp5vx3u6K6UMDAjMekmJl8YVipBHmEnBvMrokzJJFUSl4jtUoK8EHmbw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇮🇳
😆
امروز تو یه حرکت پشم‌ریزون دانشجوهای هندی تو اعتراضاتشون ضد نخست‌وزیر هند، عکس امباپه رو هم آوردن و محتوای بنراشون هم اینا بوده:
«دیکتاتور امباپه شکستِ سیستماتیک را تحمل نمی‌کند. همین حالا استعفا بده!»
«۱۲ سال در قدرت، و تمام چیزی که از مودی(نخست‌وزیر هند) نصیبمان شد، نسخهٔ پرمیوم امباپه بود.»
«دیکتاتور را پیدا کن.»
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/Futball180TV/101938" target="_blank">📅 21:59 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101937">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/r_BI3KODOp-VjSruQ6243rVP9BM_YAwWz57QG73bkHoodyj01t0bi7P1NPtm9YgoBxzWJ6yrpFBUy1FepsCBzx5Wuts_urkmzQjfh2o4wj1QAphMm-zKXThs1JYcPEVeYKPxg38vFi1kU-eoXREQjsCULgvZL88AnrxfO6vkKBzCxLvL2OI-jNohZvBIq4_Rn0ljFzA3Wbk0XokKoMC0mpnAnBw28hkOdE4NdNdJ6akYqjHRkDf8Y7KlJgCw_UB3EmPTt248NnaKnzadfE56WGPqHLMqZVxXVKK00GF3ZkOrQvvmipYX3pTmA9ByF8s9WWAzvrxRZlvQ7XDNMrI-LA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">زلاتان ابراهیموویچ: "بین این دو باشگاه، این سوال پیش میاد که کدوم یکی احمق‌تره؟ لایپزیگ که پیشنهاد 100 میلیون پوندی رو رد کرد، یا رئال مادرید که 100 میلیون پوند برای این بازیکن معمولی پیشنهاد داد؟"
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/Futball180TV/101937" target="_blank">📅 21:48 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101936">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FEimw0hJ0TkSKb6pzu_861RfosU1G2f3Od0f2RRT-otgv8_F_PRttud7Az7Y0XvoDjKIiFU4c4VRo_u9Af-RcdoLNrcH5T3_Pr0gsw9TqImCs4gjSn3KFSHpyTxuLdOdELhVMbDW-XuwoX7Ai6y_6OJek67j4p0mKFQIjRf6aHgd8hDVzydS4TAcXPJF1qhmZdxwVGgeMPipFz6GZmZV9Uy5RdK7P0Hw3iydbpkpEq8nAumIjRPfZ2FflaSNnxtCGTV3AJhDbMrtkLpB8zafxb7fN18KDL7fIffmxi8zlHmJDj_P8MWVftOmaNs-yi5IvAP2Lg4h3SF1FUqSutRdeQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
محمد خلیفه، گلر جوان و ملی‌پوش آلومینیوم به استقلال
پیوست.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/Futball180TV/101936" target="_blank">📅 21:31 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101935">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IsBWmPwg0PdTMjWLkBpSMme4xi4v1Jo0VzFJ8XNaxieYKF6lPpdFGIx12_lI4TUqE83C2XV2mc_Ceg00hWXJgca31Hln6qc4E1SG-ajJKRNGkwNs8Osxh1zDQGVSRlYFzp8txHjwYYuDYLOeZ0wVx2-FfE7bfuyqOM-ZcwvJHiYYT2L9a1mEvu0h40yLYdGRWDHsrIafj-7MARKX8rRllZ-jzTOtzomDrZv4kqZVq9nfhuhTssgYkJWzKJ9Y8KeijwFvZnsBhLzQZBKnG6EmeLOjkIqJJaCqsoQCinxrZvhCmEwN8Ii3ugjHS-vh5sMaNS-dFralg5u3qasjXrS6HA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
ماریو بالوتلی:
یه بار زلاتان ابراهیموویچ منو با رافائل لیائو مقایسه کرد، ولی جوری حرف زد که انگار می‌خواست بگه بالوتلی بازیکن خوبی نیست.! منم فقط یه عکس از جام قهرمانی لیگ قهرمانان اروپا استوری کردم و زلاتان رو تگ کردم!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/Futball180TV/101935" target="_blank">📅 21:21 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101934">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/B5BdOWd8H-zyUgrGt_Rhw58D3l1Ki46xOTB0lSvxs4YSqUVpgJd_d4KnjCZGkABnatdr8LGXqI3I4_GNrZWaFbRdyWi6oMYyYrCwU-OZKL1duEPMmTrDsA2K3QJuqOW2PC2ROhoNlqukpHcTED4vs_ZQFegrxozr8DMyIbyuL4ErUf2o3uButQe2gDlyBVFKs5rPD1wIt1X0KEvSiGTipcbfWpa_xmngFSXZoTmx-2cbt4qvusDRjY1zSqekvhu4AKcanmCZ4wH4g24YVangk9EcHze2lTlrVpjF0jC7FyFLx3DEo1fcK6DQpdatN6kOS-plICQInbXHGt-5Ke8T_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
کریستوف فرویند مدیر ورزشی بایرن مونیخ:
اولیسه به رئال مادرید؟ این موضوع اصلا برای ما مطرح نیست. او این فصل هم نقش مهمی در بایرن مونیخ ایفا خواهد کرد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/Futball180TV/101934" target="_blank">📅 21:15 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101932">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/gA5fis5mbjI-M5C0_PwtF1BSVgOKvEQ06sek1f2bQtXCx9Cgq9sO9xM2OWoyubdI5j0_tN1CUGEqIn5W-kmwL5gv-aCMsucrpkBSYoxF5JleGAk46xDZ0stqD09QHLupB6CzGF7xeglLfFGB6vIFP6sl1STRIM1orRdnlX8CxclI-S3h6gn3e9z-PEWLHzL5JQ1h5HvAF0ybeB0iBfz9EfMJr4uwh3Ae30SujuLtDpsgx40D0XnxWRMCVDcePR0Qx_rvcijkKe6ssU3zSWoo1OS1NkkYwY4Frva_ihup6lwl873rKuBIUetH0hveaEYBZp4_R6G_Zsa9TdriPfFiCg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/kk9tmLgqvhp-B8x9y-oTHVSyYzDKxgod6sLSH5hHxt9luRkCtbcDCuq_iAfD8FMn23pulAK5fOyby_lEnZiN65ceQpzoTKjPHGKn7ldRAFsW9NhFxqXLSx2tmIqJwX5mwBIy9g3TJilxOk1EF-7Oz5pyMQP3PYHFZeA2-E2C6gsc9U8A1MPnfzxhMKU9jyRvYRTSbW2V4tJ48RtI2d27FBDkOyccE66Dp8NH_o2tX8smt8LxIjbMsZae-hH3oynT2r4LyTRq3cbZ3uXfz7o8areH03EiB2LOwx3SdrrF1OyWnWHsC50C5KlFsBHqFhOzY0ibLKzqa6RnJSTi2Zn4NQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👀
براهیم دیاز هم از پارتنرش لوز مندز خواستگاری کرد و رفت قاطی مرغا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/Futball180TV/101932" target="_blank">📅 21:07 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101930">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kuK0jLK6U1iC8wE1L_PCWfv7-tJToWJIvTUMjkgRLVdBsK84DsrgRkDeIiYl9_gQcmGaMKtNohKnao_6dooR-wcEJmXQ1tDbD-T6C4yTrDIUmypfTDQTXWBlyBLHkG8a-JYA6cTyt2uS7brOGgByoy5OMTbW3--0JiP8A8EQsVov_y4m_bOYIj4uqd_tLVsFzbpNSRTpOjjt54lPs7DYVAXq25VlTJffP9jWiXJnTkRzw8lhGrbrKoY7UFLu-Vz41ffbCZ1VO_VXiwag6t5g9_pG5WVXKhHP4b4qF0GGbMWw6lVSGoTvwGgrbl6HqqvKTrxIQkaq7Tpu2ke2qsInKQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f2c2dac8e5.mp4?token=aUY1D2ZKazVjcORR5JJKzdfcPmxuDkpAS8yXjTE8_jfACsFDNF7o8-saQIwDMvTMvwv5NU7jv6BY01ZYL3Z36BeGo344wLssuf56-vBEgFh7AiujUsLjw-ktdqWGstlWwsa3RZyrR8ZA2j6iYX9-lRvy5ffBb4rG6O8mXU6lNp-lafFSVQqg-sUIPPnOJAEgVvGJAAdusD9VZdCJ9WrWSlNHoUeoPdJ3moOi0muGNf_MG2O1xxucLKzRgX0olRfPGLQn8Xp1NL53rFnIGnwB_ShZIomsHYh4DPQJ50NUzRc1dar56gsi5jTSRnUJ6xo5_KwUorbHoKaSYdGa9FfqMg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f2c2dac8e5.mp4?token=aUY1D2ZKazVjcORR5JJKzdfcPmxuDkpAS8yXjTE8_jfACsFDNF7o8-saQIwDMvTMvwv5NU7jv6BY01ZYL3Z36BeGo344wLssuf56-vBEgFh7AiujUsLjw-ktdqWGstlWwsa3RZyrR8ZA2j6iYX9-lRvy5ffBb4rG6O8mXU6lNp-lafFSVQqg-sUIPPnOJAEgVvGJAAdusD9VZdCJ9WrWSlNHoUeoPdJ3moOi0muGNf_MG2O1xxucLKzRgX0olRfPGLQn8Xp1NL53rFnIGnwB_ShZIomsHYh4DPQJ50NUzRc1dar56gsi5jTSRnUJ6xo5_KwUorbHoKaSYdGa9FfqMg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
برگام عجب سلیطه‌ایه این! اینس گارسیا دوست‌دختر یامال، بعد از موج انتقادهایی که به خاطر جدایی از دوست‌پسر سابقش گرفت، یه ویدیو منتشر کرد و گفت:
من به خاطر پول یا شهرت لامین باهاش وارد رابطه نشدم. خودم درآمد دارم. از وقتی با لامین وارد رابطه شدم، بیشتر از چیزی که اون برای من خریده، براش هدیه گرفتم. کلی وسیله گرون‌قیمت براش خریدم، ولی اون فقط یه جفت دمپایی برام گرفته که حتی ۷۵ دلار هم ارزش نداره! بعد هم برای اثبات حرفش، کتونی‌های گرونی که برای لامین خریده بود رو نشون داد و در کنارش دمپایی‌ای که لامین براش خریده بود.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/Futball180TV/101930" target="_blank">📅 20:53 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101929">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Qr2Za40fcUD1o5kCqVHtqNTxpd77IdTvlr3pWP7aqE-cpMqtebr2e49ws8fXeawWuyHIQlUX63ndZHn2DNw253SbRITrYYJO6d7EPdSFLg4KwQ72A2F06aq-RztBEJ-4CJZJYJefYBs65lXRFrrhxe51OZ_fVe4uhD4SeKJyWGBrNqed30HcsMAtCUQINp2DWO1_XUMS-DCXmUzVWvwWcZjsQJHaWamwXZS7fIhda0rzIFQPUaWtz_VLETBoUOAqn9H2SP9G_F5C5RBFGYV8oNh1nb1H8unmNLtMuYGWF-2wwxumTl-X-uY4JKfEeaCv4ka44PpeRefo4D88tHdwDw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
پوریا لطیفی‌فر هافبک گل‌گهر با قراردادی ۴ ساله به پرسپولیس پیوست
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/Futball180TV/101929" target="_blank">📅 20:39 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101928">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/62941770b7.mp4?token=gyHE5HH5oVhn7rOWSzn__qEzKjEOWQT_lEqyEGKCmgwsRKRaAUJFkhHDAMyHzpOtSKG3f0ub3N_hMTTSQ2sFuXMRwKn7xuI1H13DOikOy2FjiCD3aW1VR53gFbAvuO_4ySSN2XEWnCViRYjaIMRdjz2i8Otoy5JGETVP58Ps-O7Qp4Nj_0T-O4dP3Q0wwIIWiaF-XbqDi2Gfyg-gcij9N7DVV12UW3xr2MGEenZemvyUpYcyiFj89mCKZXA-k0EzfuMagJfCztTDspVC2pymWIEzM6Rk0X8KEdqaxtqf40XXdveh2746YF4cSz2FH-BOhr1xzklwvYmz8hhUosB82g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/62941770b7.mp4?token=gyHE5HH5oVhn7rOWSzn__qEzKjEOWQT_lEqyEGKCmgwsRKRaAUJFkhHDAMyHzpOtSKG3f0ub3N_hMTTSQ2sFuXMRwKn7xuI1H13DOikOy2FjiCD3aW1VR53gFbAvuO_4ySSN2XEWnCViRYjaIMRdjz2i8Otoy5JGETVP58Ps-O7Qp4Nj_0T-O4dP3Q0wwIIWiaF-XbqDi2Gfyg-gcij9N7DVV12UW3xr2MGEenZemvyUpYcyiFj89mCKZXA-k0EzfuMagJfCztTDspVC2pymWIEzM6Rk0X8KEdqaxtqf40XXdveh2746YF4cSz2FH-BOhr1xzklwvYmz8hhUosB82g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">💎
استمرار، استمرار، استمرار تا رسیدن به هدف
این ذهنیت منحصربفرد ترین بازیکنیه که دنیای فوتبال به خودش دیده.
👀
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/Futball180TV/101928" target="_blank">📅 20:20 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101923">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/teZK2r3HR6zCW2MS30M9feuvrYQq6dFI2QQTIVrXt_w4L_dr-YVYLj6rTbGGfIc9vmZwtwMGqDpsfMWQqrMalbApgdtQphtUSioGC49lp4Zy2VDgH1zl21HWJb-4tO014zqmVZc0lM5_6n4isMhQLkM42J1W40fXOXdLsC49ifWBG7JCwB6hrmC_r_r_3RjdoonhcX8C-KxxX45olnhDy0sOazGRq_UUDddRAZWPirdYCbh7OMnNUwtaiKxH3aa_EMMBABNREef7Lb03TUBey2rLH044Lg5Pih7lSai-9MHvCs2-Pce2wDEWP44hfrnWVlDmBDGmNe_QOZtV-TC3Xw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/L3QoHgdYGcST4l1cqTMUaXpRqwwBbUXfoWa-kenHJOllr_mZwGLImeI_Nycfp8ptU2R5ZrnVLzAzST47aK8GUEEdOj7Pyos7TrURQ9n84tcbUpsKdjEZDmcAHj3--lu0qcf-rsRc9Lui0lpQyn-04wCBT6HdxhBLnPsv3J_1_b9IIzvbpKQK6Xgf4ynPh1-hnKExJsGcjB5cZdzVu7gXXxns3wgn3b_bFnO0LHVSsh1MhxyJLgYNs74_lR2WV9-TIjSpoDIhtIbc_ixSHbCiT30JfNXrxWCH2pls_v8P9XFDUezznTaCxbGZ-im-o58Dgd06BN_fj8qZyx5tqbK1TQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/dYXm_YW5A8ItymqYL8kXFP1iBZGAUfdXoxfoT_2xg4Kve5BOQKJ1Mko0ggKJmZYCrqztVpp2D47sqnd4QrinsVlgduK6rPfprlnfapmEeckdNYMBSRi6Q-wbmTsZVSADsy28YDzva8aU0WwxoNJbfcm5RTa0mS6cyX7wXCCvRjV30wqBRcYh-6b3_7xWvrpy39KzrIZlMomeAP6N_fZyOCVF1S_sURddokZQVMKM_T3TsPs6-tJJ7OIcNhyHSA_r5AijkLqIkGDrX5scpDkLBMmnVmS7TETZAqqZtFBh-gwVlJTm6Ccisxh7dtYZ56vj9-dCtwTEgZX0WUAxTVurjQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/91c7199c9e.mp4?token=U1PvBp5bztZ6ltR8n458N3WBg4IL3ra02dr1p6ThJ9o3qPaKLwuiqMAmG2_hx63H8bJG95NU4nl3Wza1Qs4aPDrymubhtmUnlo5c9Ihuz7LY5YegKCuSG_cXb4p1L6tpifpaH6LPJfGzHT0HVp4fnvIwdI6WXxKmSnu3U9gkCjKU4oYwNw82NEBDbjk3ketjC2luCyv0D4vWHx0TOym5F20nPM5Tk74kN_eeWg1ySE9vfgYDId1m0CEZiWy-ABou6clK5jIVEO_wKrEGJQa63HUVEfCFMEaih455zzwW45KJCnUNpl5zRu1VX2zJVsZLwRIkROHWGkkc9KgqRApM_w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/91c7199c9e.mp4?token=U1PvBp5bztZ6ltR8n458N3WBg4IL3ra02dr1p6ThJ9o3qPaKLwuiqMAmG2_hx63H8bJG95NU4nl3Wza1Qs4aPDrymubhtmUnlo5c9Ihuz7LY5YegKCuSG_cXb4p1L6tpifpaH6LPJfGzHT0HVp4fnvIwdI6WXxKmSnu3U9gkCjKU4oYwNw82NEBDbjk3ketjC2luCyv0D4vWHx0TOym5F20nPM5Tk74kN_eeWg1ySE9vfgYDId1m0CEZiWy-ABou6clK5jIVEO_wKrEGJQa63HUVEfCFMEaih455zzwW45KJCnUNpl5zRu1VX2zJVsZLwRIkROHWGkkc9KgqRApM_w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پدری تو تعطیلات در چین
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/Futball180TV/101923" target="_blank">📅 20:17 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101922">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/W4LKlVuyiG7Sb2ThA13oFCGYlcN7jgIwu1agXqtswT-etObnblIFPt5aQIPrvvRoyahENbzsPB44_58yrA6QUagOwQwHnWnp6BcaV3VLEAMt58qZVbONjxtQiNT2AG7xkwMwaRu4GLrYAs33zikChn_CyAARncrmLMZ6Pg2CJzPpcb6_h3CgfLZi26ocsTxLVkuCo8UgQrpMwRF-Clfop1PlKn4m1KEW62xxEJt3xuFsDWQHtBo5scrf0jN64LwjtoawTxIBnlZRnpeUs_NPqomvaEPzID1xJyZpEKrCJzF2z-Pqsb-Lm0rRajyW9pikc4VRhRvdzeL7KQBYhp1EHA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
🔥
همه مدل کیت فوتبالی فقط 570 تومن!
🔥
⚽️
از کلاسیک‌ترین کیت‌های نوستالژی تا جدیدترین کیت‌های باشگاهی و ملی دنیا با قیمتی که هیچ جا پیدا نمی‌کنی!
😮‍💨
❤️‍🔥
👕
کیفیت بالا
💰
قیمت مستقیم از تولیدکننده
🔥
تنوع فوق‌العاده از تیم‌های محبوب دنیا
✅
دارای نماد الکترونیک
✅
امکان خرید حضوری
🚚
ارسال سریع به سراسر کشور با کمترین هزینه
اگر عاشق فوتبال و استایل فوتبالی هستی، این فرصت رو از دست نده
👊
⚽️
💚
کانال تلگرام برای دیدن مدل‌ها و سفارش:
تخفیف  ویژه  برای سفارش از طرف ما
👇
👇
👇
عضورت در کانال
https://t.me/esportsofficiall</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/Futball180TV/101922" target="_blank">📅 20:17 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101921">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5fac07199b.mp4?token=BDEqTSoTLOD0yPi36E8w7UNJe-TKN28FuBFfHyQf1DXNX42V4b3wP74X30C1voMq1punaOEU3HYQbqa4sAYYeQBXsSgejgEw86CZkAg205vAVBIL_GYalguj0jshKR7_7YSeiBoUdd7rSSvEKTXDcvLAm59xn1k1b_bioGRMHkz-ODw57cjpEEPc9153GI6CLuOewb3rUZq-R9em8iEvgIiqIZlB2smIfzEKPyP8nP8SAtJLaplfgAuAhk1N4Ic8W-1wiH1xt0MFXtgxsSw5oDyRzAobhZOH_8MuK7azikK_-iJCHlGhxsn0NS-F77mW074gpMisgUF0IoZfv8fqRQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5fac07199b.mp4?token=BDEqTSoTLOD0yPi36E8w7UNJe-TKN28FuBFfHyQf1DXNX42V4b3wP74X30C1voMq1punaOEU3HYQbqa4sAYYeQBXsSgejgEw86CZkAg205vAVBIL_GYalguj0jshKR7_7YSeiBoUdd7rSSvEKTXDcvLAm59xn1k1b_bioGRMHkz-ODw57cjpEEPc9153GI6CLuOewb3rUZq-R9em8iEvgIiqIZlB2smIfzEKPyP8nP8SAtJLaplfgAuAhk1N4Ic8W-1wiH1xt0MFXtgxsSw5oDyRzAobhZOH_8MuK7azikK_-iJCHlGhxsn0NS-F77mW074gpMisgUF0IoZfv8fqRQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
😐
تو شیراز یه ایونت ورزشی برگزار کرده بودن که چهارتا کم عقل سر دختر دعواشون میشه و طوری همو میزننن که کم مونده بود بمیرن‌.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/Futball180TV/101921" target="_blank">📅 20:07 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101919">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/NroTNdZ3q2lzQIb2jxKTFT5Fu4Ls_eB8y2faCCKXRCwDOji7BIYrxzNL6cEc0Fgb3G5wCbeL_H55XlQkNTMpSP4NUQ66nKqM-E9OSIL9f94uxX2sn199390lfH84x2VvcPf6IQSEhzLnECCmIYa0w6LrIITWx_-nNaYZn-re2KKqWG9absPnX-5VwbOaPpCd4oFlSnCAtV-yhYSzw1j120XQ7KJKhTjHgsDCxoTG2lg4RD1s5e62JfB_xY70Zupes0UUmp-ndLowgvrKKoOoyQh-HPr6xIHyLJds81_DVBfLx18toUP-UDWm6QQuz5ETQQEgSbCD6VNgKrdKo6_OXA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/b6rLIbmXODxhwMez0ydkMwxPi7uZQWP_Qevu_5u7AvsSbnOh5Qsp7NVj9q5R-lOVglD8xB4B-muQiM3mhb5Oz6KzVzwzqVKo7Ss2rLeqo4GrgZC-QLuym7XqkOEpBOFJSoDUDnWKmxLIuAAzkflUKJXDnX4JROIS7F2dF4q-vfmedPxBUbIPl39RBRVjDDFKLppdmjtcmBJVFabfdAH6-svJ6X2XEtW-VSnfEr9pbxhGxU_L9JQ-S8hzhvezVDoGcaTWiHzpJU79Ro-E1UEPHOc7FwYpZmLVbpuxBpNZBsx1T1v-FzHJSTTBO4t42F4FttzXshWHGD75HZ8BtolE-w.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👀
🇪🇸
فرناندو تورس یکی از آندرریتدترین فوتبالیست‌های تاریخه.
افتخاراتش شامل:
🏆
جام جهانی ۲۰۱۰
🇪🇺
یورو ۲۰۰۸
🇪🇺
یورو ۲۰۱۲
🇪🇺
لیگ قهرمانان اروپا ۲۰۱۲
🇪🇺
لیگ اروپا ۲۰۱۳
🇪🇺
لیگ اروپا ۲۰۱۸
🇬🇧
جام حذفی انگلیس ۲۰۱۲
خیلی‌ها دوران سخت اواخر دوران حرفه‌ای تورس رو به یاد میارن و تمام چیزهایی که به دست آورده بود رو فراموش می‌کنن.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/Futball180TV/101919" target="_blank">📅 20:02 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101918">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HneJlCWUa-gT5mowjDImeUdh0HuhLaA3wevD4bmrewCbuhyDmkhifVP5jRPzL2x581N0_71Q52OlGooKKNUmL82nQk07o0ITt9jY9NJA3774vD9ytGvAY0u8odcAblVVmxoopbdxbtNaw_JG9-UctU1iREKm5jKIv3b7WcYouZ6zVOKXo4YrvXlBTv_zzR7gd0zN8QTUvEvFer9vJmppENl4i2Ne5WRV-COlp0XDdQXfj3-jxk-70DCvjqmAiDMyhkNwDQ8FJShYYFcg6owvRdTjpYMGkHeckq4Ol-EkEb5w-APMf_irlSmiMF-KdtIGXA2slrrEfpgfv5wDTd6ezg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
اسکای اسپورت:
هری کین بلافاصله پس از پایان تعطیلات تابستانی خود مذاکرات را برای تمدید قرارداد با بایرن مونیخ آغاز خواهد کرد.‌‌
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/Futball180TV/101918" target="_blank">📅 19:48 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101917">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/779a683584.mp4?token=niaFVOzvq_1VlHOqaCr4fkJfYhbU1_3RumDdNJYVwOYVB8NgdZgzvFXcJ283LLs6nT-x6tm1Yd3huUzvNDs2OUX-M1s5PcHpRzMV0MDON9-Y1-qS7GfkSs0VmrVsiWYjoRq_FdqF4SNrLvKQ_sxjfeSF2GiUr-lZVlbhlTWwa5Qb0e_kRPQ4Qn6xuLsW1BSxgqvtW814BNzCc11C_zV-LjgD1RZuXjsGVeRVTpNc3hkg50MK8CA62AlRcYCVVbMKdj0oPZqWY2o1uxCT6mnIounzmvHW41g1Bk_mDOP1u-GkfYxaMbEbFU6yByiAuTai8NZN1xrRNckTKcNmjW8P5g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/779a683584.mp4?token=niaFVOzvq_1VlHOqaCr4fkJfYhbU1_3RumDdNJYVwOYVB8NgdZgzvFXcJ283LLs6nT-x6tm1Yd3huUzvNDs2OUX-M1s5PcHpRzMV0MDON9-Y1-qS7GfkSs0VmrVsiWYjoRq_FdqF4SNrLvKQ_sxjfeSF2GiUr-lZVlbhlTWwa5Qb0e_kRPQ4Qn6xuLsW1BSxgqvtW814BNzCc11C_zV-LjgD1RZuXjsGVeRVTpNc3hkg50MK8CA62AlRcYCVVbMKdj0oPZqWY2o1uxCT6mnIounzmvHW41g1Bk_mDOP1u-GkfYxaMbEbFU6yByiAuTai8NZN1xrRNckTKcNmjW8P5g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👀
رونالدوی برزیلی سرعت یک وینگر، قدرت یک شماره ۹ و تکنیک یک بازی‌ساز رو همزمان داشت.
🇧🇷
🐐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/Futball180TV/101917" target="_blank">📅 19:40 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101916">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/aa3ffe3c02.mp4?token=dYf0wyNUk0KO8h9_UK7CkzY0cvRY9t4-a03ht5IXGIj2uIOYNkLbZE0PpaiVPgFtBXbNvz5Gr9drJCQhbCK6FXPB24xzAsG8HnZr_mK82nuHiSaR194yjocgkENjYA0YD8RnIpiJBwidIdeK1Xd2WnT8mKUJhdCXsX-6yUGR47adxUbmHp4_XpGECecw2SLs6qPTVCsferkYF9WDAMgEW0hQVehW3FXoZuPciID63Grs4mslDGrQcKUZFyPltWcbtc7d_VPswxeysJJgFY8vNuXGsrQyFybj0Gq5F45lfScAR2Xffyc7OALUMorcuR7UjaG4d8E8UBxvrIXeA-LUXm3z_QN5nPQ-WwFeCJeeUHiO2JeXNqcx79p8uZv27u5VInb6ezb-X1ll8yODoNOJmpxrIuAKpq41RBWXBXkqp9YMWnAPM9YlD0u--vjtBWBwNQuXECBpHKN0LLRpANzADrMRW_mTAutmdncjSEdT65tJkxTkjceCJg-oQf2ElCTjkCU1aG7dBrTmc4WH6-2UrMfe2NnLLOsd4ruTPfiHdRrK_nf787jAQ0SZg6Epsz8xFjdhJOMKZ6m1V7BW5f-BaKGEiwlamZFMnFSDr9p_z2Y-D0_tLmD3IJf7GIGd5PAXvy-mgj2ClRijm9QGhFx7SF03RGaznu7PY8FZBeJt_C8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aa3ffe3c02.mp4?token=dYf0wyNUk0KO8h9_UK7CkzY0cvRY9t4-a03ht5IXGIj2uIOYNkLbZE0PpaiVPgFtBXbNvz5Gr9drJCQhbCK6FXPB24xzAsG8HnZr_mK82nuHiSaR194yjocgkENjYA0YD8RnIpiJBwidIdeK1Xd2WnT8mKUJhdCXsX-6yUGR47adxUbmHp4_XpGECecw2SLs6qPTVCsferkYF9WDAMgEW0hQVehW3FXoZuPciID63Grs4mslDGrQcKUZFyPltWcbtc7d_VPswxeysJJgFY8vNuXGsrQyFybj0Gq5F45lfScAR2Xffyc7OALUMorcuR7UjaG4d8E8UBxvrIXeA-LUXm3z_QN5nPQ-WwFeCJeeUHiO2JeXNqcx79p8uZv27u5VInb6ezb-X1ll8yODoNOJmpxrIuAKpq41RBWXBXkqp9YMWnAPM9YlD0u--vjtBWBwNQuXECBpHKN0LLRpANzADrMRW_mTAutmdncjSEdT65tJkxTkjceCJg-oQf2ElCTjkCU1aG7dBrTmc4WH6-2UrMfe2NnLLOsd4ruTPfiHdRrK_nf787jAQ0SZg6Epsz8xFjdhJOMKZ6m1V7BW5f-BaKGEiwlamZFMnFSDr9p_z2Y-D0_tLmD3IJf7GIGd5PAXvy-mgj2ClRijm9QGhFx7SF03RGaznu7PY8FZBeJt_C8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
یکی از مصاحبه‌های چندوقت پیش کریستیانو رونالدو که اون گفت او قصد نداره یک‌ روزی مربی بشه و بیشتر به مالکیت یک باشگاه فکر میکنه. او همچنین درباره اهمیت مراقبت از ستاره‌های جوانی مثل جود بلینگام و لامین یامال صحبت کرد و گفت باشگاه‌ها باید به رشد و آینده این بازیکنان توجه ویژه‌ای داشته باشن.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/Futball180TV/101916" target="_blank">📅 19:20 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101914">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YCseXYcR7YP48sQTtKafwBDsRKDQICC0AtSnn5vjZ4d4ect-opDbIDz7NxyxPbxPcJy-NaIou7SSPxXrXosNMxUhiydrsliU4puJGAENGCBIuzwFcn3WO0PnV3EeLHyMyPNwUtWM24MZTpaXAeVBJVTpb09RhI_sAcwrm9gzMuBOcAuzl65Dkgm3l_Y_iAE0YPA4ZENkinjEhbW0Wqb3oHausWG39EBlPMlkHVSNlv_B7wgN5zxfHBcqWEuFEEVm5JOh-Zx0DizrRRkdikpYsFkjO7pBl_c5XFVLog3uqipENzW02U8__1ksc0pRPuKoAX-leo_VLVf1LdTYUVvxfA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b9c742e9e0.mp4?token=UlzoomImlyf7l5BKgsSjiNYZ5cxInQsAz39llr7i7Fi8rH2fcGA9G2JlsM7UV8lpZCatEIcDKqxjO1T8QpVUzY0KAFmstMtx6rfDZcPVH9RBqUx-r0lc_JT5eVz2GBp2m-ZI-mOgXqoZYx0EUECqb7AIOIlarwzxGE3SB-aL0dNWMGsPZaf0GxO39awUT5DVv2RmN7YLxjxoZfavq__2MGCa39rEKJv_IcWSR5yJWOASDdej6SCoK1L9xLqJbwmWHn6I7rfBXD3FZVDxZSl9FHj9NjxcBnG0JXvOLLXB53NIzOE0X0PDgZ0FjiME_FYqcjGtEAE6Bg61-FAWd5FqGQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b9c742e9e0.mp4?token=UlzoomImlyf7l5BKgsSjiNYZ5cxInQsAz39llr7i7Fi8rH2fcGA9G2JlsM7UV8lpZCatEIcDKqxjO1T8QpVUzY0KAFmstMtx6rfDZcPVH9RBqUx-r0lc_JT5eVz2GBp2m-ZI-mOgXqoZYx0EUECqb7AIOIlarwzxGE3SB-aL0dNWMGsPZaf0GxO39awUT5DVv2RmN7YLxjxoZfavq__2MGCa39rEKJv_IcWSR5yJWOASDdej6SCoK1L9xLqJbwmWHn6I7rfBXD3FZVDxZSl9FHj9NjxcBnG0JXvOLLXB53NIzOE0X0PDgZ0FjiME_FYqcjGtEAE6Bg61-FAWd5FqGQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🎙
طبق گزارش‌ها، لائورا ایگلسیاس، دوست‌دختر رودریگو دی‌پائول، گفته او حتی ۱۰ درصد توجهی که به لیونل مسی دارد را به او نمیدهد. او مدعی شده بعد از شکست در فینال جام جهانی، دی‌پائول دیگر حتی کنار او نخوابیده و رابطه‌شان به جایی رسیده که به فکر پایان دادن به آن است. گفته می‌شود او معتقد است دیگر بازگشتی در کار نخواهد بود.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/Futball180TV/101914" target="_blank">📅 19:03 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101913">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/c_FqCJPYhvaqM7TmFH-jLt61omuYbOO1S1JU_ls64Hv02otT4m5HvTE_DR4wm0WCM-cobF-rQvHEgpvG_ob9muF7OuH4QP1o82bnLj3fRY-xQJFbE4e-JkQ-RdOpKIANx8IPUcFpopRN37Bo55v9zwEUDSX_wFemrD12HrUtfXPCRajq6E8g9o5n1MjylngGJ1ncoND1XUA0CupNMzCxDmSA9zZ0AaN08cuCsa6U79ZEhYanlCmwb0GjaHvMEEc8XRExVscv_C4Mq2HtG6oGtlWTCqxm-jCgUE8KUbRb8kgEnuDaK6hwU1O01IWQ286RRHLwSDNKAN-woOdrwxhKSw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
⚪️
تلگراف: ژوزه مورینیو با انتقال وینیسیوس جونیور به آرسنال در این تابستون مخالفه.
❌
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/Futball180TV/101913" target="_blank">📅 18:44 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101911">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/PUMRqiAXHg5836hZiiagBhN0_kQznpdbA9n8DmpgJRdKE5eRt7Un9Xpxqdwx1g5P9_mGHppqa3WP7cSkolLCU6NRbG32Ljy11gT-Pu-tNstnMbYCqX3U9ryCqIBzCN9x_Vd9Wn3VCkQJKodQRi81yqRYhbT963EXYnPAdP-vkkSJFYHPB3mtYw8FOw8YrKAQjvSgyhEN8wnaxjuJTg6_14Cd_1ZVFviBVZ9UDhPXXILGWCqUNj9Q-YyrDAJdqIHgtJpgSuL2io69qa5cE5Rf4N5aP9sVUa0JTYEu0XJZVrUHCTUymtzUdNvWycXKVIP0MaOoBZS6PO_wu6H2O1irPg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/MyAZI2vdaJ9sMidKb-sbaIU976xbksyc-8vQtfxu13J83AzRIFpWXZK4NAH5ohycZLMGvaKWAWQDLWgNVJX2xVguZdEwqGHQNA6mEK_To1HDw52kWQCxDxYC2MnKlv_UjU8-xsnXe-qH2P_BkFQNuBcwCRD69upgTJSqi-Jaaz99G6MGeH1RjEawXea_vPM7IJzNC5No4L8RhGmK1WlfPB3-mg-ACuS9aOylecQH1zlkgKVFAJesF2aC7yQeYT8guXoKYACNwRAbXAnFr2a5RaQmCt9uaLWVfIe--5ZlI_fjFNgsFGORdAoJKO7t9mKODh5F7EeMHYJ4pCEC4iwabA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚨
⚽️
رامون آلوارز:
اگر انتقال رودری و دیومانده نهایی شود، رئال مادرید ۲۶ بازیکن در فهرست خود خواهد داشت. در این صورت، باشگاه مجبور خواهد شد حداقل یک بازیکن را از فهرست خود حذف کند تا با محدودیت تعداد بازیکنان مطابقت داشته باشد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/Futball180TV/101911" target="_blank">📅 18:43 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101910">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JFA6ILH9bNZUwCqF0TDE-FBb2UUz25EZGC-06Oxvom0_e88MQYbRF--qQOaprBzT_RdpEsNfH3mIBduPAuTaQnaFtt_YvibO3qi4w_AElAKEy5zcAf_roIVVW2fHj4HzjHbBfQ704GUS4L5YbRSqPZTs607Etd3EXmsB7odcgjyZpNlcLw7A1ISZgimcK7-vD7zluv_ETpD6C5WXdPKulOIlaphZWZ0qjshAhVrBDJnsOWsAjX8hr1Y6V6MkOGZ3MBh3DLoQPZTckg0FmBj1wEMVQJ6GRSAOiT6sihGHKBpTwI0W_6mj53Ii720-LfOe9Gg91R7UrFHgDof_ScgXYA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">با ربات هوشمند تهران پی تو ۳۰ ثانیه خرید کن
😍
فروش یووچر، استارز و تلگرام پریمیوم بدون احراز هویت و ثبت نام.
تحویل فوری زیر ۳۰ ثانیه.
درگاه رسمی بانکی و مجوز فعالیت
✅
@Tehranpay_bot
@Tehranpay_bot
همین الان استارت بزن و راحت خرید کن
تلگرام استارز با ۴۰ درصد تخفیف
😍
یا داخل سایت رسمی بخر
🔽
https://tehranpay.net/utopia/</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/Futball180TV/101910" target="_blank">📅 18:43 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101907">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/tks1EehBbaGt25MIrxGyhh0P_YUXfpBMMcqBPIhun9B925ihZpiOxsuQMsLD0zG1kihrU5p7xeQVLmO_Ru-NRiHF8NQCkuJTeTWWZIBYLcppkykNxnCb53b6UfxvodnaaKLZeTiDIoD6qThxKHneVHa0cKw1GJ2egDMek5LuyJvaSJfAzyEEikTA6OcPGCfOAQqZRC3r6oeyTRq-j1PvXMhRxOL3i3lUX1O4qPKRjhzphsdb2L9aZPITIrDVQDejPytS-J78NZ1rHsSGe3SkatcYp_pEGPKsZmYMeCZ0jYgO-u4304VczrzEhrV2lOS2H_dxvGFupuuKS0_1UWw-Jg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/sCNGcLUdZkPMB0yALTHYE5C0DmxBxT9vnH_VYNUcOBDEJcR0u1WUjuV8euJ_NAVhl-FerbOlHwsFXh54f2LwkJgfd67Q8H9OvqeA3X61p9HXrN23ff0FyrHA-mpIYrltaq90pPwCGBrQc5ki6nzjhepjQ-0BEdgl5IT0-kCqIs-HpcSwWKnnWxbcgTIz62Y4FWK-uYdg76d_UR7ZOU6O33o9WJ4-tM3Wdvq0njKjSxrXr_47cMswWTqvnmpdOOK-CG2kFyKTiziV2Pp0CRLp7PlO3OJkuPSBu-rlwpErVSEqfHKnZY588M1-H_3KoW19AVPtlOFwieNEjmoZ2tJ4Qw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9d05827d11.mp4?token=eup1z5j1sz4bXhzWXOzFNCxM44EozUxOKzevPmdeC2ThxQg6PNbzrfASQQH4vieeqQZs1TAFBWnf3C1lOAnxDgiZMhqfSiT8tNdWmDunnq042jQ80QaZG4vNfIUkGHXoamulnEo3Mv98XEN5aTD3F03sgmBe0weoO3MHdkqCUvhUvi7Aej4nqu5PNFeIHjPsSRb1_DCgM_RY0t2j0v9NexxtyFBhkFbaR3Gu6Nf7hfzPkJf-NR_TX1ttQEvXkkr1keoPzi_cv4Mbxxk4nRtrUe4WezPYUnh2tYGs_SUvcJPVav4H4VhotEZjH3i9WWox1ZDUyflsAFjF5drMWKMlwQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9d05827d11.mp4?token=eup1z5j1sz4bXhzWXOzFNCxM44EozUxOKzevPmdeC2ThxQg6PNbzrfASQQH4vieeqQZs1TAFBWnf3C1lOAnxDgiZMhqfSiT8tNdWmDunnq042jQ80QaZG4vNfIUkGHXoamulnEo3Mv98XEN5aTD3F03sgmBe0weoO3MHdkqCUvhUvi7Aej4nqu5PNFeIHjPsSRb1_DCgM_RY0t2j0v9NexxtyFBhkFbaR3Gu6Nf7hfzPkJf-NR_TX1ttQEvXkkr1keoPzi_cv4Mbxxk4nRtrUe4WezPYUnh2tYGs_SUvcJPVav4H4VhotEZjH3i9WWox1ZDUyflsAFjF5drMWKMlwQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🎙
رودری درباره جنجال‌های جوایز فردی‌اش:
فهمیدم مهم نیست چه چیزی به دست بیارم، همیشه یه عده هستن که میگن بازیکن دیگه‌ای شایسته‌تر بوده. وقتی توپ طلا رو بردم گفتن وینیسیوس باید می‌برد، حالا که توپ طلای جام جهانی رو گرفتم میگن باید به مسی می‌رسید. این بخشی از فوتباله. به نظرات مردم احترام میذارم؛ مسی و وینیسیوس بازیکنان بزرگی هستن و مقایسه شدن با اون‌ها خودش افتخاره. اما بابت جوایزی که با سال‌ها تلاش، فداکاری و ثبات به دست آوردم عذرخواهی نمیکنم. هیچ‌کس نمیتونه ارزش زحماتی که کشیدم رو زیر سوال ببره.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/Futball180TV/101907" target="_blank">📅 18:40 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101906">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4cbd3d9241.mp4?token=SZqKUwXp7LPqkz_hzSAmlxB97nmgxzCgIBVtPdvkDzW-tXJYO5MlBunl2mJXXCM_jCuaskxkQXahpHJS4D0zr_sV7RadwfoE9gh4RbsSvTVDZh-PQ607uAksQ9qs98LgDZhOeNGiEj-afozMKHfQF3bHGG2GxTmVixRfUSBu-Q3U0T0NkdKT4Up2x9OsdOBBcQcuIFYCM14f1P7zgFkZL8KzWlhnw0ZwMkCEhh0O8bJsNDDV2hn3cr7FuLIgBW2dayfpoJgbE2tDugiWTQAxZhTJoimYVYy3bZtxsS2Jf-WVQOKXsU3Mgy9kSj-aytxdBQd1aLhbHiOXBw-KlWGyQw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4cbd3d9241.mp4?token=SZqKUwXp7LPqkz_hzSAmlxB97nmgxzCgIBVtPdvkDzW-tXJYO5MlBunl2mJXXCM_jCuaskxkQXahpHJS4D0zr_sV7RadwfoE9gh4RbsSvTVDZh-PQ607uAksQ9qs98LgDZhOeNGiEj-afozMKHfQF3bHGG2GxTmVixRfUSBu-Q3U0T0NkdKT4Up2x9OsdOBBcQcuIFYCM14f1P7zgFkZL8KzWlhnw0ZwMkCEhh0O8bJsNDDV2hn3cr7FuLIgBW2dayfpoJgbE2tDugiWTQAxZhTJoimYVYy3bZtxsS2Jf-WVQOKXsU3Mgy9kSj-aytxdBQd1aLhbHiOXBw-KlWGyQw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👀
حالا که اینقدر امروز دربارش صحبت شده یه کم یان دیومانده ببینیم.
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/Futball180TV/101906" target="_blank">📅 18:31 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101905">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ff6a2da2fb.mp4?token=IG7Ee_TWo2r1i4ItE7Adf8clezEaecAzDKmGBmXvXW25cuUdQ8Wp3-DS1pjKsdme9gRlBx2ovZ-14L5KGHUa_vDHNHIqUz5fj9z6sclK0YGrgkWBLq0GtIua10tK7rjNsAr0-kH2KMzAw7AACS2-syeHGkeiC23hWVIL0o4geYRpgWQF3BEXcfJQigI_6Fpamoa-LLvlZVH7EkyKyDWLLXGpdFnKQz5uLdf6u13tUgmJ9igkfaVC3KK7ZjeSrZ3TY9QqI8Wwx6V2MDBeVUz4zOXFLElzoVfOC9o7IQldCYS3_YWpvleJtcSPRechPrE-V2V_EgTi0ECCYw72b46gAn9mRVs7E3EcqYmEGC3p6gMvN5O5Pqy1e9YrfheR3RGXXbMqvFmuZGooHj3Woem-0rpaYinIlZSSoQDz16QkPxu58GfbYeTXpI4IKddp_QkFBma8WI9I6n8g3ppfi-oPmXoGotbjpGZUUSa_VmvmsKjD61-nr071c6aUeJiex_Vk-oVUem_1hJcBjUROj4rwpGvDoVW5_ErSjg8yFNSUhjI4PiduLkBBVV_XRCdK83rhXZgslFRSEkU_PPUBR81hvoTt54IzTvKIOXunZi4V6_KxnzhK9O97MK8s3qwt8pHcZXqSmS05dZcVZl1HHjat_YdVq4TRM2E4hO3G6btadGc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ff6a2da2fb.mp4?token=IG7Ee_TWo2r1i4ItE7Adf8clezEaecAzDKmGBmXvXW25cuUdQ8Wp3-DS1pjKsdme9gRlBx2ovZ-14L5KGHUa_vDHNHIqUz5fj9z6sclK0YGrgkWBLq0GtIua10tK7rjNsAr0-kH2KMzAw7AACS2-syeHGkeiC23hWVIL0o4geYRpgWQF3BEXcfJQigI_6Fpamoa-LLvlZVH7EkyKyDWLLXGpdFnKQz5uLdf6u13tUgmJ9igkfaVC3KK7ZjeSrZ3TY9QqI8Wwx6V2MDBeVUz4zOXFLElzoVfOC9o7IQldCYS3_YWpvleJtcSPRechPrE-V2V_EgTi0ECCYw72b46gAn9mRVs7E3EcqYmEGC3p6gMvN5O5Pqy1e9YrfheR3RGXXbMqvFmuZGooHj3Woem-0rpaYinIlZSSoQDz16QkPxu58GfbYeTXpI4IKddp_QkFBma8WI9I6n8g3ppfi-oPmXoGotbjpGZUUSa_VmvmsKjD61-nr071c6aUeJiex_Vk-oVUem_1hJcBjUROj4rwpGvDoVW5_ErSjg8yFNSUhjI4PiduLkBBVV_XRCdK83rhXZgslFRSEkU_PPUBR81hvoTt54IzTvKIOXunZi4V6_KxnzhK9O97MK8s3qwt8pHcZXqSmS05dZcVZl1HHjat_YdVq4TRM2E4hO3G6btadGc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚪️
تیم رئال مادرید در دوران پرایم خودش یه شاهکار واقعی بود؛ به طوری که تقریبا هر بازیکنی، کاپیتان تیم ملی خود بود.
💀
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/Futball180TV/101905" target="_blank">📅 18:20 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101903">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lmHdUX9eop1s8F54cEsNmRQ28OR0vCHmlfHM2PPEoiabJNBtwk2cjX6eEvcr1jSbPexUDBSKNnpZMMoa8Ofv_B6WNKyxzOj8BtqKI2LMp0kDBr0CjrTuq9AkEbhxvWDO57yDf29_qO_Vq-7FHse8zDahf5GFJMOdmekwucmdZwU_SoFa4gOOhKQ56IngvI1D4WST7yiwrLKJsbPK39vhrhVZRdV7e4ny0fhnESPhlaIC4me3NKYDYvQOYKwEwXl6hQn76D2Ho9DAm4vSzIqKkw2kbklWd8xd0PmvDI3zhBANg9aqP9g8w_Nz8pl5GWiEKBxHjKaPCDgdvPbgsdFr2g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
⚪️
کاکا درباره دوران سختش در رئال مادرید:
من از میلان آمدم تا بهترین بازیکن جهان شوم، اما مصدومیت‌ها و رقابت با بازیکنانی مثل کریستیانو، بنزما، اوزیل و دی‌ماریا باعث شد کمتر بازی کنم. حتی امروز بعضی‌ها من را یکی از بدترین خریدهای رئال می‌دانند. اما آن دوران باعث شد خود واقعی‌ام را بشناسم. کاکا می‌گوید نه بهترین بازیکن جهان است و نه بدترین خرید؛ بلکه همان سختی‌ها او را به انسانی که امروز هست تبدیل کرد. فلورنتینو پرز هم هنگام جدایی از حرفه‌ای‌گری و شخصیت او تمجید کرد.
❤️
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/Futball180TV/101903" target="_blank">📅 18:00 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101901">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/lEudmUkZBcVTBlpTNinQ-BP6haR7_KiPXKCoB9KB2wmccfw0YUkjWgbKU55ZiC0ffEn7BhulfSHBAqvbBpC6ZRvi9DoZqOeOUdJyCjOlyUP4bIXnNZ4pOSWjRuSwJ1jUx2tdzurCvuwk0qTU2JrsnAhpMEFcKl8IMbGGUC_DFPcRgxEAa4WxYOSLkSYrPkDWat6Pv8xRyAac5nx0EdnpZ6BIFgmpSC2kk9sCYLr8L7U0yf3U3Yub81ukxTkgxaoiek9mPi4_QRBNW0WcvREtRi_q0NZ_yMZi-pF5fkFefkiCYtuCYI6Z1n7TA7YUaB7yGywMXS5HhVC0ZUD55dOumQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jR_mhBEWuELVLZeSpXqmdy77QJEYUyd0tPfZNkQ5rzYbBuP0IrB68PBLYh96gtabMRPKIeDyZkOiKqJaV2YsB_isph_Hq96E2mpMrUoqaS7FF0UZQl0qjCiU72UJu69lYaSg8U-G3vGnGw10czZql8FtzoZOvVSnFgS3FSJq8OUJAufHfisT5YoQhHsNPTWaNvzkzYTaDzBkpXRkCBbF-9ZDXmxCL8D2C3Siz6_fPv_FLUtMJ-2baWZmp2e7kdkS90D1_HVTETSKVKCMrHQb9pcZ88mn1NLLVULRLQyIriFehQJ4x-mJQIU3EMqF-nyz8MJRGTIt7R4PK1pEzxx1Ug.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🎙
یان دیومانده درباره گرفتن یک پیراهن تقلبی کریستیانو رونالدو در منچستریونایتد به عنوان اولین هدیه تولدش:
اولین هدیه تولدم یک پیراهن منچستریونایتد بود. توان خرید پیراهنی با اسم بازیکن را نداشتیم، برای همین کاملا ساده بود. خودم با ماژیک مشکی پشتش نوشتم "کریستیانو رونالدو" و شماره ۷ را هم اضافه کردم، چون می‌خواستم به خودم انگیزه بدهم. هر بار آن پیراهن را می‌پوشیدم، تصور می‌کردم خود رونالدو هستم. فقط می‌خواستم از همه بازیکنان دریبل بزنم و تا جای ممکن گل بزنم.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/Futball180TV/101901" target="_blank">📅 17:43 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101900">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b492c31a81.mp4?token=maFOLdcUXr_DlsFTOQ0qw7-IOBUN0pU9aNurNxQbQLE-E4Wfw7DCrHhqeMFDmIRjT3UTSisVRRbgQMa3NmR_-GczBzKWxWk4uGDFLoa3uCwT8BFOCUvHlohZJ12LVwtR0vrV9oa88zvK1FR0UT2dudxW1vTnYOFAgsqSUNV4UnrvtQSIQdAp4lIU1VwiDIszaAP-XAi4FJZl9es2yKhQ-OdZIpl5PLWYKYvSwhoTD9lLl3z-6GN1mLkyk5xTLVbB67IYm5iXN0xHiBSGJyZpHTUFwoWBVdoo1NWU6q2OCCbweI4d4KhPwWpHFU9cp0WE3SHpgoOJ6uCr4prN-S3gNQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b492c31a81.mp4?token=maFOLdcUXr_DlsFTOQ0qw7-IOBUN0pU9aNurNxQbQLE-E4Wfw7DCrHhqeMFDmIRjT3UTSisVRRbgQMa3NmR_-GczBzKWxWk4uGDFLoa3uCwT8BFOCUvHlohZJ12LVwtR0vrV9oa88zvK1FR0UT2dudxW1vTnYOFAgsqSUNV4UnrvtQSIQdAp4lIU1VwiDIszaAP-XAi4FJZl9es2yKhQ-OdZIpl5PLWYKYvSwhoTD9lLl3z-6GN1mLkyk5xTLVbB67IYm5iXN0xHiBSGJyZpHTUFwoWBVdoo1NWU6q2OCCbweI4d4KhPwWpHFU9cp0WE3SHpgoOJ6uCr4prN-S3gNQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">فران تورس تو تعطیلات در کنار بکهام و مایکل جردن
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/Futball180TV/101900" target="_blank">📅 17:32 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101899">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/51f2886d75.mp4?token=IKKy1kHqE64PW-j0hh8MTleVxrMUomXT3TvIK7jf7TP1_UbH1ilcBgBk8RP1d_u44eUXNi9H4ckonTTfD-X7tWs_zOk_BqiOe9NCdOL1uy_SvzjTjZmvL8ejQaXHivDOwArT94KzEitz0Ly0xOLiFEF5Y5Dj81s_tLG1XX9X0qr61Z0wKIZiy7xhdXkrHMffKZqUlic8kr7ba5uWJnphToTabbYkO9daE6fCi0FtpqpNZ-cJssh1smeGt6k0TEkAZA4u0MobJ8SuVWxhGEdK5J4aj1LMLsUqZ0OsvLkNYb2q2LjP19TNrcjZRxfLNwX2iPggqI47jOJ3gTEiMZ6IZQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/51f2886d75.mp4?token=IKKy1kHqE64PW-j0hh8MTleVxrMUomXT3TvIK7jf7TP1_UbH1ilcBgBk8RP1d_u44eUXNi9H4ckonTTfD-X7tWs_zOk_BqiOe9NCdOL1uy_SvzjTjZmvL8ejQaXHivDOwArT94KzEitz0Ly0xOLiFEF5Y5Dj81s_tLG1XX9X0qr61Z0wKIZiy7xhdXkrHMffKZqUlic8kr7ba5uWJnphToTabbYkO9daE6fCi0FtpqpNZ-cJssh1smeGt6k0TEkAZA4u0MobJ8SuVWxhGEdK5J4aj1LMLsUqZ0OsvLkNYb2q2LjP19TNrcjZRxfLNwX2iPggqI47jOJ3gTEiMZ6IZQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">هر شاهکاری یه کپی بی ارزش داره
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/Futball180TV/101899" target="_blank">📅 17:30 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101898">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5fe82274ba.mp4?token=ps9852CgkQguOh7aQe7nh5jFFdd5o4xg3rv1w1_ypts7dE4Mv3LhNYLPHHrJ6G8vrKwkem71shh0kco4bP3m1J5408br0GgsEH3CBB7NkgmPDq1joL5MtC0kphNhaoM0Qpw2eElFIm5RuiQUsCk31j4yk3fxPgBCjUhvJwOxFQ7E0HZ69gwbouBdSie8EqB8d83qKl86rCCpLzTVZqjQvrJ9gDVodJCTun0vQdtaGIo72qFtlBXPFHYJhCpPO3HUoWU4e2m_OHDIbKa1FgAldSY_IRw68EIl0Bqwd9Ff0nPoImJLMC15ycfsjpQ52A5IwcSUfjv5zlWh88q9Xr8HsA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5fe82274ba.mp4?token=ps9852CgkQguOh7aQe7nh5jFFdd5o4xg3rv1w1_ypts7dE4Mv3LhNYLPHHrJ6G8vrKwkem71shh0kco4bP3m1J5408br0GgsEH3CBB7NkgmPDq1joL5MtC0kphNhaoM0Qpw2eElFIm5RuiQUsCk31j4yk3fxPgBCjUhvJwOxFQ7E0HZ69gwbouBdSie8EqB8d83qKl86rCCpLzTVZqjQvrJ9gDVodJCTun0vQdtaGIo72qFtlBXPFHYJhCpPO3HUoWU4e2m_OHDIbKa1FgAldSY_IRw68EIl0Bqwd9Ff0nPoImJLMC15ycfsjpQ52A5IwcSUfjv5zlWh88q9Xr8HsA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">زیر ۲۹۹ هزار تومان با ارسال رایگان!
🥳
با سرویس سفارش
یک نفره اسنپ‌فود
غذای مورد علاقه‌ات رو با
همون کیفیت
ولی ارزون و به
صرفه‌تر
نوش جان کن.
😋
🔥
از اینجا سفارش بده
👇
👇
https://i.snpf.ir/wopv1
https://i.snpf.ir/wopv1
https://i.snpf.ir/wopv1</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/Futball180TV/101898" target="_blank">📅 17:30 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101897">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6e5e82a980.mp4?token=QmoD2KK0oggNMgLwzLsWNtKL9Ge4pyEVGGug1Sd3Iby3QpXqU2qtRbCjfcHG7Ux3FSOk6Rf5KjEz_Pu5q6aeb1jceJ9t6BEjYDLcYyLQU04lJ76Fsxwy5fw4m-HuRk_iWbMMDYpCAUg1YZ9LKRkAp_pyfxqNMagus3YWqSCUtdw0cbkDQSRQN5mHkf8Eooa52PKHGeBSL-Z2UsxVFEcqm6GPjSHdXszYLi24ZoimOpJQQyy8bwUpa7CSyAIiobWpDPnpB3wzZcl5u_vBUDPscMITo5UdfDVlQ7Xu-8SUONdQwEfUihUH4LHOUBWLq2zPUQZU_Q_VwULaRg_dgqPNgoWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6e5e82a980.mp4?token=QmoD2KK0oggNMgLwzLsWNtKL9Ge4pyEVGGug1Sd3Iby3QpXqU2qtRbCjfcHG7Ux3FSOk6Rf5KjEz_Pu5q6aeb1jceJ9t6BEjYDLcYyLQU04lJ76Fsxwy5fw4m-HuRk_iWbMMDYpCAUg1YZ9LKRkAp_pyfxqNMagus3YWqSCUtdw0cbkDQSRQN5mHkf8Eooa52PKHGeBSL-Z2UsxVFEcqm6GPjSHdXszYLi24ZoimOpJQQyy8bwUpa7CSyAIiobWpDPnpB3wzZcl5u_vBUDPscMITo5UdfDVlQ7Xu-8SUONdQwEfUihUH4LHOUBWLq2zPUQZU_Q_VwULaRg_dgqPNgoWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ارلینگ هالند از مزرعه یه پیرزن استیک، عسل و شیر تازه خرید و بعد رفت خونه تا خودش دست‌به‌کار بشه و غذاشو درست کنه. فک کنم هالند بعضی وقتا یادش میره که یه فوتبالیسته با میلیون‌ها دلار ثروت.
🤣
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/Futball180TV/101897" target="_blank">📅 17:23 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101896">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PgFN5JOFHVa-7yN2Kh0yN5eqYJBz827bU-VR3tQlAOdakxZYPQ6iF0L3dgkp0HO8KTTaGu8c_hNrOm3uwZmz7z6xap0pMhsFPLFZfW5GzNoZKy4mPVt5E9eLeHiQI5M73a-gyv-djTB9jZIoSuKyBl6E9e9vSDNFmt5YyoUuJ2m53nDz9myrViwN4z9ahFAMlN2EELofEK3-RKWhqIRj4LmpneKHyLn48p5DI6-gpaQIFQkZGzYV1N2hs22GYuoLDMn7z_17vQfDGfAoE9T2Xt30ot1Iih-uZL8JpyZePOZ2McBi_KCs3GF2A0q4bF0srmGmezAA8PU1IBE6vDNdtA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
دیوید اورنشتاین: آرسنال در حال بررسی احتمال جذب وینیسیوس جونیور است!‌‌
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/Futball180TV/101896" target="_blank">📅 17:17 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101895">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ri1sOi3lpI8Phs3u4XNmvKia1QVCMnQOmGRP9TXQ2jJ9r4l8EmcZMXCmzJQZmRiX-xoBfQpVW-1GlI4po2LXEdV409CuGdwtrZZAIXurzHY1r7M9kqkQXga0e_JWP4ArupN0Ozenw20swRa7tHICz2GznYvKonPd9b2b2YeojSP6VNAtjE78D4WIw4UIejP4mFdTR4lg7UVwtj0flrxqHOvCZm0bdUUZwm_dT4QpxKlbaP59rTDAfyEjjvfznyTlt4WSCU21aoLjbDQcwEnzaXU-rQizf3hGqYYnrhwI3lzgQiASFKTO_9GqAhCnBUR_v_B18NLf2g5zVtlh9n-wDg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
بن جیکوبز:
نمایندگان وینیسیوس جونیور، این بازیکن را به لیورپول پیشنهاد دادند، اما باشگاه به این پیشنهاد توجهی نکرد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/Futball180TV/101895" target="_blank">📅 17:08 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101894">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/36c582a64e.mp4?token=gClpTm9CQO7ewkTQw4h7eyEg0s3eAxGjz4TRfpaqY1G0oOWMFTR64OmAeSIi8DH57IBSPr4zbGLTA49WP6bV279I3ltNpgRaSYGE12-sBzHCLkv-aeIhzXAi8W_xWpcwmHiX6XV5AXXnAXZAdBI9kI5pd37v1flyegTVEo7ayjghUj_6vqDoGfMWLWEsZchRcdJiokSRpzRtLqB59-N9n_qmc8vWdnzOew_iZ4pu2GuiSKUiWoWUw34SDDCoM-G9EzktWnZ4oJ1i1zX-z_qeO9hr8g9QRFJXnZwdPqqHZj_cWu8Gjo-SqpyKRY_WMXPLZwqm8w8xMCK2va3jUnNKZTu2_elIA95RCAeBpJk1VovIeRai89YTyc6BHUrNLvaDXEZqKRADe_sCkgXlB_VaJSxjm_8ApmghQ5uaEkHvp9kOHu7pgpAcB-q2X9I3DBKyjvaJjoEtpXwRVJuH5Z_g2yz3G5d4ahReKGxl3-4Tb7AyOY05tuMhWcE6FwF-3CYoJhlmI3OdStad3zgQE-i_5Pamh5QPrK2Ey8iknMXqPzenJQbAliLT2G6Mm14Kp_ZrNpaj-wkjXNuFv6wSbV9dg_12ZlphxRYmGQ7n171iaWNv1OkAvM_W92yB8MnkEq8odwD29tUa79FMaW-l3QaO4ZNG0_xjOYvTN0XFxDjJgBE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/36c582a64e.mp4?token=gClpTm9CQO7ewkTQw4h7eyEg0s3eAxGjz4TRfpaqY1G0oOWMFTR64OmAeSIi8DH57IBSPr4zbGLTA49WP6bV279I3ltNpgRaSYGE12-sBzHCLkv-aeIhzXAi8W_xWpcwmHiX6XV5AXXnAXZAdBI9kI5pd37v1flyegTVEo7ayjghUj_6vqDoGfMWLWEsZchRcdJiokSRpzRtLqB59-N9n_qmc8vWdnzOew_iZ4pu2GuiSKUiWoWUw34SDDCoM-G9EzktWnZ4oJ1i1zX-z_qeO9hr8g9QRFJXnZwdPqqHZj_cWu8Gjo-SqpyKRY_WMXPLZwqm8w8xMCK2va3jUnNKZTu2_elIA95RCAeBpJk1VovIeRai89YTyc6BHUrNLvaDXEZqKRADe_sCkgXlB_VaJSxjm_8ApmghQ5uaEkHvp9kOHu7pgpAcB-q2X9I3DBKyjvaJjoEtpXwRVJuH5Z_g2yz3G5d4ahReKGxl3-4Tb7AyOY05tuMhWcE6FwF-3CYoJhlmI3OdStad3zgQE-i_5Pamh5QPrK2Ey8iknMXqPzenJQbAliLT2G6Mm14Kp_ZrNpaj-wkjXNuFv6wSbV9dg_12ZlphxRYmGQ7n171iaWNv1OkAvM_W92yB8MnkEq8odwD29tUa79FMaW-l3QaO4ZNG0_xjOYvTN0XFxDjJgBE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔙
🔵
۱۲ سال پیش در چنین روزی، دیدیه دروگبا برای دومین بار به چلسی بازگشت؛ اسطوره‌ای که نامش برای همیشه با آبی‌های لندن گره خورد.
👑
📊
آمار دروگبا با چلسی:
🏟️
۳۸۱ بازی
⚽
۱۶۴ گل
🎯
حدود ۸۶ پاس گل
🔥
۱۰۴ گل در لیگ برتر انگلیس
🏆
افتخارات با چلسی:
🇬🇧
۴ قهرمانی لیگ برتر انگلیس
🇪🇺
۱ قهرمانی لیگ قهرمانان اروپا (۲۰۱۲)
🇬🇧
۴ جام حذفی انگلیس (FA Cup)
🇬🇧
۳ جام اتحادیه انگلیس
🇬🇧
۲ سوپرجام انگلیس
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/Futball180TV/101894" target="_blank">📅 16:57 · 03 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>

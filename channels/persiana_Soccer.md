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
<img src="https://cdn4.telesco.pe/file/JzTTUbvcODRElHB6mqxVtr5M-zb0m6b2628DqRrHgBUIyveZQ2muFMyUOvjzm5YUF4kCm0ZiTNvhdt7IZLfUsUI1h2TWuTF5qarq7hRqmPCUJ_g4w6-NAOQ-5q0_RVRrAqTLRkiOXjudy1WCSfsXsKtVRIOyXCfRaqQxX7yUJjd8fU6fEtgQRVLHb_Zs3WXgRX12ag8JfJgyqPFKNPRrhALBCQPK_S4ZqYWPaxeJaRu70xJOL6J0IHJd6ROvAUtqJJmJSR4AYdnmN0acNzlRQXMfm3z38DjQarkm9xI2zBHAkO0HbsoloYZSVxQ0Ws2tzcZQ8M1nUF3Z2RkeMeV92Q.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Persiana Soccer</h1>
<p>@persiana_Soccer • 👥 452K عضو</p>
<a href="https://t.me/persiana_Soccer" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 پرشیانا ساکر دریچه‌ای تازه از اخبار محرمانه و داغ فوتبال ایران و پوشش اخبار اختصاصی نقل و انتقالاتهماهنگی و رزرو تبلیغات:@adspersianaکانال دوم رسانه مردمی پرشیانا:@Persiana_Plussپیج اینستاگرام:Instagram.com/Persiana_Soccer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-07-02 19:06:26</div>
<hr>

<div class="tg-post" id="msg-30361">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/401621b710.mp4?token=GdEE62e6LyayvXVG4SycWIuGSTt_tfufq9q6j_mnFxiVxCWPuce0ht6gGHHHlMq1INn0IrWmnA-IIrEi8iJ1ZqqnQ9KKZWDjFqWfpP2ONXKQiZnxDs7qN6hnkj8aWnR0o7hw2RKpQrhCYUrwfe3235UYD46cJLJgQz-NdEHpBv8W1ajRAL2p__777a_1CRELQVT00ZUyTVO7unU0Va3kACF4ay07iRhYGNaMP1Lr33AE1ZJx3Cpy7LSStnhUd45AuMy4YAsHhmixsmre0CAeEh3Mokry85TuVG_I35BW3n-C4olRZ7Pz-mA6UBdqKZXl4wyHCS7XDzzb5eS69jO54g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/401621b710.mp4?token=GdEE62e6LyayvXVG4SycWIuGSTt_tfufq9q6j_mnFxiVxCWPuce0ht6gGHHHlMq1INn0IrWmnA-IIrEi8iJ1ZqqnQ9KKZWDjFqWfpP2ONXKQiZnxDs7qN6hnkj8aWnR0o7hw2RKpQrhCYUrwfe3235UYD46cJLJgQz-NdEHpBv8W1ajRAL2p__777a_1CRELQVT00ZUyTVO7unU0Va3kACF4ay07iRhYGNaMP1Lr33AE1ZJx3Cpy7LSStnhUd45AuMy4YAsHhmixsmre0CAeEh3Mokry85TuVG_I35BW3n-C4olRZ7Pz-mA6UBdqKZXl4wyHCS7XDzzb5eS69jO54g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
👤
کاشته دیدنی ستاره 36 ساله ایران؛ گل اول تیم ملی ایران به ازبکستان توسط رامین رضاییان.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 5.78K · <a href="https://t.me/persiana_Soccer/30361" target="_blank">📅 18:53 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30360">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a6b255c08c.mp4?token=H67f-grpHFTMQ6NFgSYypc55L--t-i3vX2MQVa2qZpNbEXQ7MF8jjiDBPHrOXt2p9CYbZa6Al-u6W8mLozsA7LL1BU343GOsncDe14rOkMLescVum6J6ltrQRfkgEfQ1UoFHUEWbHgpL4Y8n5jDySL3Mdk0BqXbzoAy1PJkuNAb6h_zh01lVGywNUDprlDZQXiDxKFIZTzYYrew3bRWX0SIFkis9Dht2HSHbllrmGM0v0Vw46jhPtlB-vwuxbPpSldXASq9Xme5PTyUb5Zo_r-vnKkLineXiXU3S_YYYwhkUs76xr8ol57BvKCuoLsB6hTgu3UfSlywePo1-Psk5jQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a6b255c08c.mp4?token=H67f-grpHFTMQ6NFgSYypc55L--t-i3vX2MQVa2qZpNbEXQ7MF8jjiDBPHrOXt2p9CYbZa6Al-u6W8mLozsA7LL1BU343GOsncDe14rOkMLescVum6J6ltrQRfkgEfQ1UoFHUEWbHgpL4Y8n5jDySL3Mdk0BqXbzoAy1PJkuNAb6h_zh01lVGywNUDprlDZQXiDxKFIZTzYYrew3bRWX0SIFkis9Dht2HSHbllrmGM0v0Vw46jhPtlB-vwuxbPpSldXASq9Xme5PTyUb5Zo_r-vnKkLineXiXU3S_YYYwhkUs76xr8ol57BvKCuoLsB6hTgu3UfSlywePo1-Psk5jQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇿
شاگردان امیرقلعه‌نویی اولی روخوردند؛ گل اول ازبکستان به ایران  توسط شومورودوف در دقیقه 10
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 8.81K · <a href="https://t.me/persiana_Soccer/30360" target="_blank">📅 18:44 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30359">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rK6Bqorp6N8pAgRrmFcvh4vWCBLada4WVbX-EKnmYFVdClBrGM3opnRuwGT6XLBQijgwz63-t_9DzAw2C2pCLenpaCQ9H8lblpMdyc6CLNMYK74baHYFPHJznbCcYOFTHMEPcm1RHY2-c52y-i9UtjFj8SRcTG1NWqAfcDGLoIbWWLhLc_8ydJCyoNBR2eT4mZYc0Fk9HK01YWD338yRkSlo5unqq-DrwCUEz3LASDhZR82F89we94AiNEEkotxGCCCNSLEzQzuRsUwyq2BsmykNaGKBQHnjyksA10wzpegiQdoD9hG9mMYxebB2shAfj06hGgf-yVTcdiBbbaSnhA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇿
شاگردان امیرقلعه‌نویی اولی روخوردند؛ گل اول ازبکستان به ایران  توسط شومورودوف در دقیقه 10
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/persiana_Soccer/30359" target="_blank">📅 18:15 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30358">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1995a5be8a.mp4?token=XoiNzG29mhNLH9IJ-sgM6pVNNWRQiOsi2vW4qY4ZAUEDAuSh_dtM6bSrQzdY461hn9OoEMAsiNHXMzUJEmUq2r0u_7uWSO5o1EfnQkMieRL66kpDmh0chPtSHWmK9Ky7F1AYs0Ejwmgxq7Ds-HvypNOi-8IS4xlytBolt1i38jyFBijXlxxwIV2mfpv558UCnw9Nw92LUb_f1F_Y8fUgM0ckkUcZltG4xTP4zaVU-yimOgYyeVN0Re-NeO3XUEVPuxE4o5-3mjVYzGQX0INXcMY_HlsniMSW8mdPSw3O5dtlYwHfTdRGPyOa5NwVFUYPczU2x8qB20pD-rTeceEAZA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1995a5be8a.mp4?token=XoiNzG29mhNLH9IJ-sgM6pVNNWRQiOsi2vW4qY4ZAUEDAuSh_dtM6bSrQzdY461hn9OoEMAsiNHXMzUJEmUq2r0u_7uWSO5o1EfnQkMieRL66kpDmh0chPtSHWmK9Ky7F1AYs0Ejwmgxq7Ds-HvypNOi-8IS4xlytBolt1i38jyFBijXlxxwIV2mfpv558UCnw9Nw92LUb_f1F_Y8fUgM0ckkUcZltG4xTP4zaVU-yimOgYyeVN0Re-NeO3XUEVPuxE4o5-3mjVYzGQX0INXcMY_HlsniMSW8mdPSw3O5dtlYwHfTdRGPyOa5NwVFUYPczU2x8qB20pD-rTeceEAZA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
دیدار تدارکاتی؛ ترکیب تیم ملی ایران برای دیدار مقابل ازبکستان؛ ساعت 17:30 از پرشیانا اسپورت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/persiana_Soccer/30358" target="_blank">📅 17:47 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30357">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5e3181370a.mp4?token=KwrZdLPbTe4H1SUYd--K-WQ66Fq_ktRFZiZxD6O_SWOJBmBCSfZ1SzfyzqN37C27tcuSpbTKdrEJfjQheZZWegZxhsI3BRkfTQqO8Y0f8KT59jFZjNgTENFMhBt9ummVodr96wK1YC9lwXrQg3ty55IUp5FLo1nbGZzl_ntvA20hjgW9lZsz_1XfMYIlnyPX6qLMoTvj3Jk73PJDRCbBFRw__1dRuNtdwiKnqw9ScfU01IbdlbCOAHvWrGzUVqyCH4ExhqSppGkX3OZnefT4mdCWzbJkg9oG4rMruWdQPfthawZh96kTw2TDfEDE8tv4MxIOLO1MWs2Tz9yc7zZY4g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5e3181370a.mp4?token=KwrZdLPbTe4H1SUYd--K-WQ66Fq_ktRFZiZxD6O_SWOJBmBCSfZ1SzfyzqN37C27tcuSpbTKdrEJfjQheZZWegZxhsI3BRkfTQqO8Y0f8KT59jFZjNgTENFMhBt9ummVodr96wK1YC9lwXrQg3ty55IUp5FLo1nbGZzl_ntvA20hjgW9lZsz_1XfMYIlnyPX6qLMoTvj3Jk73PJDRCbBFRw__1dRuNtdwiKnqw9ScfU01IbdlbCOAHvWrGzUVqyCH4ExhqSppGkX3OZnefT4mdCWzbJkg9oG4rMruWdQPfthawZh96kTw2TDfEDE8tv4MxIOLO1MWs2Tz9yc7zZY4g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
شوخی‌های‌ بامزه عادل‌ فردوسی‌پور با لهجه های مختلف اللهیارصیادمنش‌فوق‌ستاره‌ایرانی لخ پوزنان.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/persiana_Soccer/30357" target="_blank">📅 16:58 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30356">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jC7VuNo2YjuJOh7E_NCUOWTrKj-at4lL6zbEaU0tMJ1sPINdbHD8qz7dMHmvyuBs4T1BIYTj5RHrzbJuNMorSWbMDjYlWUDcEPQ1m_2Dg3RaWRkQwCzVW7Pe46U40irvNTIT7ZbEfjsrcVCL4mXYMP2uLxaHd7UJsa16Ye56L2hh41VAP-Ud1Fg3BjsOTkDfXfV7AVPH3uQZ4WVYbmPfe1YsfaKrmm1mJvpplRCx6UNem0bjUBi5RgRtITTwgZy25oVWH3HVYx-_Hzz1nh7HjNVTB9vYv1v71ba_Gj6AqLe1taecAAJWN9H8yDjdnOWO3QuXfQP5U3kD7Wmdpfot-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
باشگاه استقلال قصدداره که برای پایان دادن به حواشی پیوستن بیرانوند به‌این‌تیم؛ قرارداد حبیب فرعباسی گلر28ساله خود را در نیم فصل به مدت دو فصل دیگرتمدیدکند. محمد خلیفه دیگر دروازه‌بان 22 ساله نیم فصل به جمع آبی‌ها باز خواهد گشت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/persiana_Soccer/30356" target="_blank">📅 16:40 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30355">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/j9LmcpZun5H_AE9mzqVR2p2Uo1LL0AP5dNcKWfUQRUxnox5pc4x0xpekNeKP99XLiKfuN1MBGpRxn0aJFLsBBdrQ0f-0dTHJlBjaiR9ZqPWmPv4EUT2XjLWL6kUmraTEMweAUkMydIx5jnTfl74opRO9755S7hEL5oMMuwEY-rJBOsxnPnqhlDfSmVlt6KjPPL2U0W7CWUAP_01pZRER18eRrPCNqtCZUjKCCD3-PJRxKqxJ64aGy5hICIQ4ZV6rWMCHrnf13o4CzWY3etDjgsLa24Qz3eErbAB832bDO0KM8y8dpwu8iPxtxVp-Br3VND_O5QwrkBRxJnDu75VP1w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
دیدار تدارکاتی؛ ترکیب تیم ملی ایران برای دیدار مقابل ازبکستان؛ ساعت 17:30 از پرشیانا اسپورت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 28.1K · <a href="https://t.me/persiana_Soccer/30355" target="_blank">📅 16:27 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30354">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c61f1d20ce.mp4?token=VF8R1kcwF80K-L4aITLTEASqRMEcRmxUhnGm3IdvCyKKW9YFArv4hGVcer91ptrh7fwqDywkJU-zIIOD6AFELZ_hpMIsp09Wmlm1vcm27dXcYBVZqnBf6TWW_MXrgvlmmjTZGy6N2xZao5b_DNOhnBMmYE3UyAwiPxlZQ6IsLFsQZ-0B35e9PeLuOka9Gx9LFLC6BUSpp7aZDNh4vgnzb4yNRNZMAswPdXZomuaKEdRLl8aYGJPFE-hMZX-JPrfgxwwTzAmZdlFTED5BUENML_K5heOJJG8UstGwn3BbtbfUmf5V8iRTw4yUNBb0YLAgTf2jGGvgOLZ-BBU9vY5D2Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c61f1d20ce.mp4?token=VF8R1kcwF80K-L4aITLTEASqRMEcRmxUhnGm3IdvCyKKW9YFArv4hGVcer91ptrh7fwqDywkJU-zIIOD6AFELZ_hpMIsp09Wmlm1vcm27dXcYBVZqnBf6TWW_MXrgvlmmjTZGy6N2xZao5b_DNOhnBMmYE3UyAwiPxlZQ6IsLFsQZ-0B35e9PeLuOka9Gx9LFLC6BUSpp7aZDNh4vgnzb4yNRNZMAswPdXZomuaKEdRLl8aYGJPFE-hMZX-JPrfgxwwTzAmZdlFTED5BUENML_K5heOJJG8UstGwn3BbtbfUmf5V8iRTw4yUNBb0YLAgTf2jGGvgOLZ-BBU9vY5D2Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
👤
انتخاب قابل تحسین آموزش پرورش برای مراسم آغاز سال تحصیلی جدید؛ خداداد که الگوی خیلی خوبی برای بچه مدرسه ای هاست امروز تو مشهد زنگ آغاز سال تحصلی یه مدرسه رو زد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 28.2K · <a href="https://t.me/persiana_Soccer/30354" target="_blank">📅 16:24 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30353">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">✅
برنامه‌‌‌‌‌‌‌دیدارها‌ی‌‌‌‌‌‌‌امروز؛ دوئل تماشایی هلند - آلمان باتقابل‌تماشایی ژاوی و کلوپ درهفته‌اول لیگ‌ملت‌ها
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/persiana_Soccer/30353" target="_blank">📅 16:12 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30352">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ogSbrcjZh5Sy-QJwC5RyA72NA9_0n3UOPj-SZyiUmv7tiXZAa2OCeCH3cOpB-iF_mX0rFTY1Xie8tmiESW2jW6rUs3AQMBxGt229zrHLYqiZRFxBZksihqcYy2CdKxRJ5ju52jZcqZ5pGIc3sWOcD1Z2Fch6YG4NtegLFLJ7qRbQrD0IFkeoBqePo_aFwJuBHXyQyyOAdWe09N-Tkgp74XwcY5gM7or0Tvi_E4U4XQNeKyAFiBF-MsTzXnz9O3_9tQwWcqF-ZkISySUF3Z3VSORLcbusNJM0Iamq6LxoaJfV5Ba8Td_Br-i2yHOUezocGfXwCg7wUMWvvEZ8hMG5GA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
دلیل خط خوردن قایدی از اردوی تیم ملی توسط قلعه نویی رو میتونید تو ویدیو ببینید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 29.3K · <a href="https://t.me/persiana_Soccer/30352" target="_blank">📅 16:01 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30351">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eCpapDqbWBQJeiraQc2tH-hAAVRuX4YzANYL5OPazFzhaQ3SrivIYA9pdQ8WzSVh0ckSURuT5hkoSOOiUgD0g6ZOJHD838EONBHl5CbSgtQQuTBnHvIcsiW5dc1TQnQntUiXE7U3hYbjP_ruQN29vV8vFh39MhV6sUAgHJ8YC67leQtTX3mnDtuQmgoIMaUPUYXYjzPaHvLDOVvGXahQZFBH05SDLCSaTomO64doHfHtGqwmJjpDhou840K0PN08f04EK5zWIG4GLx8xW5cl_3LQR3oVFfgyxz6D0Ye_uxN53QNjCy5KlklEVzPKB5CMryvB3OvYrv4_q7nLxJMq9g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇪🇸
یامال که قهرمانی‌یورو و جام‌جهانی داره:
من دوست ندارم برای بهترین بازیکن تاریخ با پله و مسی رقابتی کنم، همین که سال ها بعد بگن یامال بازیکن فوق العاده ای بوده برایم کافیه! ۸ قهرمانی لالیگا، ۳ قهرمانی‌پیاپی درچمپیونزلیگ و ۶ توپ‌طلا برای پایان دادن به فوتبالم منطقی به نظر میرسه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 29.9K · <a href="https://t.me/persiana_Soccer/30351" target="_blank">📅 15:48 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30350">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/A57RYLGqEV-MX9eKoGVxSBBgTwYpHWZbgXHcGcOxqwKzP-1JYlP_MMSussjaXRkicd7p1-HCBsN0sfPUxRAtmsp5S1zY7kdOn3tNFH_faxFaaB3SRzCJxDS1it0oN91ijIw4ZfOazOhXfw37C61q0LEVCPXDyULD9SNPY5Q58RZpc-ObZjgDO4maTtfMYI3Q884UXZgg-C7o5nNOU1B68WF-GVHDFb0EUZ4e4Qwp15VnaVgrTI7C-aKYs0Ie6IbWm42GJH-ovUjiYq4cEbSy3wnH-M4zF3MRUFx0ghSUij6chuUMAGWjVINpKir8CbNTQxKx_oR4wK0NWGd0G4z9BA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
گروه‌بندی‌ فصل‌ جدید لیگ ملت‌های اروپا که از امشب استارت خواهدشد. این فیفادی با فیفادی های قبلی خیلی‌فرق‌میکنه. تقابل‌های جذاب یورگن کلوپ، زین زیدان، توماس توخل در پیش خواهیم داشت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 30.7K · <a href="https://t.me/persiana_Soccer/30350" target="_blank">📅 15:24 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30349">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SPGPTlRPbLFRvQeLY6Ig9HCjbsmokBJlneRWLliF2VvcomPL0nsA5JotEp_jyyqWIRnnM-lImLd2mb5XhBjmaCLuCqdvolPWy6wjuuuO6asjbMssqaVV5XqKdSx7qkWH_1jO51XgjbBZc0ppepxvBSOcE_6oioNmWuU8IKvP3kl9eZDrjo5Zru3FRkjYdcss_zvcTx0Vspb48gRQdwhjwgmLSlkDByraMQWYV9BIBGtgIUh4Yo1uglhEf6fNl9Ret6ts92BiHOqsBUwcvLRVfcYMk4rArBdDubRXztIKx6J23aT27knMi6s4xGHRiF1mJ9nWKrSgNnF1OWZLvek4Lg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛ حسین خان عبدی بعد از افتضاحی که دربازی‌های آسیایی به بار آورد بزودی بعد از بازگشت به ایران هدایت تیم ملی امید برکنار خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 31.4K · <a href="https://t.me/persiana_Soccer/30349" target="_blank">📅 15:04 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30348">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/N9Qr9r0m6tf5g0lvcZVcyFKsFkK1YTcQOs_oYbGlT5EvK-tySPFaPsgBullrduVlvTAXIoyUpnLP66_3PyoGoSawNc7t_3Jnx4JG0pgIagilAePXCbS2X6mLwR5fZOcY0Dn_GkQ2-5C8Y0KY1MSIwTlH8mN0OzyjB6WDIa1kv0IMBm6U335eKILnEjycNRuYbSkCiSL8qT0A2AzcElxMKCEZ-Ukas8EhnCb4yfQlFlgcFinBt7_qPnD9dX7WUkg2K9bF8wHIJI09PEZpSXd41lvTMAs796ntjJpbyd66ON8plLndVUGWQUlls8S0O1VtNQkRiJSXonuiGGc7_pH9HQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
فصل جدید لیگ ملت‌های اروپا با یک رقابت جذاب آغاز میشهه؛ ارلینگ هالند با نوزده گل در صدر جدول گلزنان تاریخ رقابت‌ هاست و کریس رونالدو با پانزده گل او را تعقیب می‌کنه. رونالدو برای رسیدن به صدر به دنبال هالنده؛ اما مهاجم نروژی هم فرصت داره که فاصله رو بیشتر…</div>
<div class="tg-footer">👁️ 31.4K · <a href="https://t.me/persiana_Soccer/30348" target="_blank">📅 14:57 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30347">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sAIfCOoi8v61TLDooYVAiwbdCW_v9-swBonw86EhMl-HADh08aVSeJqOfewT0-QxRCnbnQ_z8qdgIi1Kh7ixgceg1Uu6e1UdP6-LNV9TLRhIa_5O1KyB7wfWac611XltiidpJO9gAlRzwWYxG1jwZaym-d3yyFpG9lP6VsBUziW2_76uXOpAnnql49Xn__e96n9ei_iB9rWnfDjdO1a-9Y8VG4WW2jCbTx3-Z_gWd4OKxdZ3DcKb697m3UL5RPZ70GLUl9nPCpqvKPdebjMEXo_jJlBGUhF9oPHapNS1PwudHm4d5c5wIHcVkMDa5vy4T-YwFOBfnLUc7MMYCiThdw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
کم‌تر از دو ساعت مونده تا شروع بازی ایران و ازبکستان
؛ ایران توپنج‌بازی آخرش با ازبکستان بردی نداشته و ۴ بازی‌از۵بازی‌قبل ایران و ازبکستان‌مساوی شده. الان‌بیشترین ضریب روتساوی بازی داره که اگه ۱ میلیون روش شرط ببندی ۳ میلیون برنده می‌شی! احتمالات هم میگه تساوی ممکن‌ترین نتیجه هست با توجه به اینکه قلعه‌نویی‌هم‌بعد انتقادات سعی میکنه محافظه‌کارانه بازی کنه. توی سایت زیر در عرض ۳۰ ثانیه ثبت نام کن و در صورت برنده شدن به صورت آنی برداشت بزن:
لینک ورود به سایت
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 31.3K · <a href="https://t.me/persiana_Soccer/30347" target="_blank">📅 14:57 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30346">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/a3LIYguDFK42BRzU5TlwvXXLuC3Tz3P1UCNNE-Jo_vAIurQHuFh-kmhyf7tJs4XjAzzDKQilXEGav3E1Pl0qWQsaa2FqTMI97ROmB0Vp33ohAEzi2pMwzvGXzyPo_YWLBi4htmdIuD7xkG9ZCw_pBQvtRTBi-EnAasxhXmkQqRopmi1nXLqUL-3mDgLVdk0hvu96LLyL-asZZ0-wPXNyCxpcFWZIf2tMnK1t13ZO9C9682RY3WVOeI34ciT6MZwhB3T8JeGkUfcYOfdcjaRHsvjIBBcgRxoqh4kUc9mznQakrgP5BSOJ3arrYsAa0QoMBeYwf4_sS6ETykJmGgrzIQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
عملکرد خیره‌کننده‌وفوق‌العاده کریس رونالدو در سن 32 سالگی‌مقابل‌تیم‌های‌اروپایی در چمپیوکزلیگ.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 33.7K · <a href="https://t.me/persiana_Soccer/30346" target="_blank">📅 14:26 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30345">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ft67o6_JyNJBVqq81AYE38__37wKcw99jiP_O3QUBAYp4sqDVoxHRD-ty6NGQWe_o5TCBsT0vhGa3LcSRVmS7-4q-rCukcr0eSHMYyHyCblHBcfr2mS-eB0_BojY_tBjEY4oLeT99hWdxCZaXEyUy7SaHXyFgBFkcbRv6_4MGP6PvF_lKn2YaWx2_nm49kVUAim4JFR8NifnIhfYNmc9W6t7B2_rM-qDyXpTz5rC2L5n2mHP62pkw41jJJU4EsTYalsyA8BvAysxuQxp3a3TfyxSp6JpNdWTOOUEnk7HkC92Aq_1pgJocmI0WwRBYKS5CoT4guYr_bnu2eqdIbETfA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
موعود بنیادیفر بعنوان داور وسط با کمک بهمن عبداللهی و فرهاد مروجی نماینده‌های ایران در جام ملت‌های آسیا 2027 هستن. علیرضا فغانی هم به عنوان نماینده کشور استرالیا حضور داره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 34.6K · <a href="https://t.me/persiana_Soccer/30345" target="_blank">📅 14:08 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30344">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kImhB8l5yhIB5xhx22Uyw1-rETSup4beDHGq-tTGxi7_idLQagCQv1oSV3oAiqtGYw_wPp4nIJZ4NUAiux5MpbwpN4j7I_ksLFfTyUOGXl0JaC-a-VPlQyQIFVa0TrurlvB_kZPZW_I_eEbbJxbzqKTZ6b0HRHITZIm2-v-8vF4TZqp_HZHD8KoZeaslePywsrLxTD_Huwxx3_iKjkB9d9PbNNi_YUayOq8Iu1a9xcDRQ71rALr0KZKsiuhwhdstEtPVlQiUER1M6nfUps82AOQklMKdan-btdJpb2s9aj4k28IvHLP8C5bfC35nLhKe1Knf_qpnHyKatO9VCQGZ-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛دیدیه اندونگ برای‌عقدقرارداد 2 ساله با باشگاه تراکتور درخواست دستمزد سالانه یک میلیون دلار کرده و اعلام کرده هیچ مشکلی برای بازگشت به ایران ندارد و حاضر است با تراکتور قرارداد ببندد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 36.4K · <a href="https://t.me/persiana_Soccer/30344" target="_blank">📅 13:44 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30343">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fxNxfVuH0Z3MhzY9OTu9HQfWt_ft_tIxj4aDw-GElXjq0rpLrme5ko_Ce6p133U239tDLPZV2pnYBTZymB-Rlb7CU-d_NtBil8SCZo2DxecZ-XVDxz_Pe9afwaKD8nq6KYflm0LMWzNbA3TV13TZbzJnvOkQRYEVLsujBPtQM-7cY5WJ5AjIHxDSFI0Ze84r8Yg5lk-zlv11Oi_-PEPnNKM_0md1tiMWJiliN0hdRHGb7FT8nCoqj6AqMIUxdNtz7ECqKbJkr2k80OjOBHvCuVgZ4-IWRVLx9oiIt_ALRf43WS9kwgSpf2UNLnnuwKj_RvFkaQwqXcEh2Pm-1Pwq7g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇫🇷
تیپ و استایل متفاوت بازیکنان تیم ملی فرانسه برای اومدن به‌اردوی‌تیم‌ملی این کشور برای فیفادی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 36.6K · <a href="https://t.me/persiana_Soccer/30343" target="_blank">📅 13:31 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30342">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tXHQI3rwzIVntOE2VYiT9qfmG_nSOYt88_ZLwh78t2A2BstfV_PGwe-CnJhwQCP2dsZdnPKwHEsYb4L0Pdc4NyGypZcKFjZvZOZWHdme5NWFOTnKrHA_zPPsd9hkPXYpmBs44XIZTXVsXdiUnrCwRQZWcMD3AH9kAgyOEISOcUZnR46czSB6z8-e9oqQDfnuQoX3TUcEcdR06TbrBpS7xCH1PZ1BES3QlF_lQnPErd4OaPvDPS7u8Uwd3MMtWpteGNgKU83F0WKwDdJiJEMRv8DdRffjAoVY9-y7q12sxLQgZ7iYBFhNBD18i_2tx32C-u5y69Rg856W3re4nvI4lw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
باشگاه پرسپولیس امروز مدارک جدیدی درباره قرارداد یاسر آسانی به کمیته استیناف ارائه کرده و قراره تا اواسط آبان حکم این کمیته اعلام بشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39K · <a href="https://t.me/persiana_Soccer/30342" target="_blank">📅 12:59 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30341">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fdp4qWhbV19fq0xJqzGD5KrnJ_dEbWmBV-yAq2R2TzRrmu7GJ-bkrqNgZ9HJ_5K5bgfDoIT5zGV-ZmKhOXr0gXfdIaMe3Dz1vBSnr047K29pnMm42caBt89jTzTfWSYYgq6l_oHxn0dC6HSk2BBxzYwU30PDfgGtjG_TlQPCI6MORfuXbqL5f8IN8cfnvYqRkrC1jWs21X67EvgAfNDz4u4eh6S3ZVzmmC-PXB4cwT_HmnAfipgbqqpwbWgjI7k6GRnXOmCFxQA3pRqzkYM3-g2TP4TxFeujBnO-PjOzbg2Tz156lnVvSXz65ebaHV3Qe8LUO4NJN7eqF9_9gmFCUw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
رئالیا:
چهارتا مربی عوض کردیم این همه بازیکن جذب کردیم پس‌مشکل تیم چیه چرا نتیجه نمیگیره. مشکل تیم از نگاه کارشناسان و پیشکسوتان رئال:
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.2K · <a href="https://t.me/persiana_Soccer/30341" target="_blank">📅 12:53 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30339">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UvL0fVMbd3rBp8i0S6p50QEWfiEwZypOfGu54OKyuNoSetYSrxH15CI_xG2LsueuBwAsiwBf0t3gSjSsBlLtQ0WQO6mWZk0WSuDb9cXgmo7Gbt-aw-wkkIPK6JGXFNZ7ZkNzcT44hQLzj2ZUdPUsfxge6QjCeO7bSkL8Y4KzsBK715WYsJ6JOaKA8r4t0mmc-MWcAwUYZi9Z9Iw_5sjLHLHlL83EblTFMwhkW1cT1uZ-f62kuVUAUvUf49E1GODeEdGtRW-aysG9amQa8TiGMe1X9OI59Yrq4lOKsJgKa5WpbSpiaRkkxdjKYUa4GtbqjvrDHiXdWzM7ftIpIT7kNw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
طلسم باورنکردنی تیم‌ملی‌ایران مقابل ازبک‌ها؛ تیم ملی در شش دیدار اخیر خود نتونسته تیم ملی ازبکستان رو در هیچکدوم از تورنمنت‌ها ببره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.5K · <a href="https://t.me/persiana_Soccer/30339" target="_blank">📅 12:03 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30338">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/P-8gQYirwy62f_37GxM_Oe1JRtjCMDj2fM5yyovrfxDPTrTf6Xnm6cPCLg5kQc3EFRTYBgKwu0vDWa56BSbo5eoBOCkAJ3l0kGjMekAvhz_MvFyZTZ8P5uLCl9JRaNjhV1H8wWr8WfgXqimUApmagSNeQ0BweDRQsrcihqiF50PjLj2k2vNlQ1sMtjp9FSyX_vwSwrPDCWqzebKMjuaP53Ed6h2rFEefXsNIwsS1oD3KI2-h-71jS91KJ1spd3zqmfccJ2CfmgRrfSQcMMwEq63wnuQli6sgYEGx1KhYsO9WBsmn8Z6nUc6gtiM6kq1Ss5hjchKJFCfMBEdelUcOJA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
طلسم باورنکردنی تیم‌ملی‌ایران مقابل ازبک‌ها؛
تیم ملی در شش دیدار اخیر خود نتونسته تیم ملی ازبکستان رو در هیچکدوم از تورنمنت‌ها ببره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39K · <a href="https://t.me/persiana_Soccer/30338" target="_blank">📅 11:58 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30337">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/P24_0pES5NMJNJboSXm57oWSzXIo8eCyfjjvWAS_Ar-ogSqgA8kTfsuvvtpWEIaA_EoW24OUvdl-UL4gBhNwulBWS-1FdHfUfsYpFGKta-Au9OK1tjYSo6jowcVndbRuyKQ-Tu36yPcSi7HqxVUHO7IkxzkwcYqJFJ2qtNvhp6FZd6sOqgIVdy_UtGKb5JHH0H3I3jmZCmcR8DjyI90syzFBANDYfBbFxbR5WsrjpJiGeXwPqK8HmOxR5KpLb1sYb4366iqKnV21Tyo2CetNhivddBhrHgIvnx2AaW9wT1qHoa6dkTkv1O4s-XNhMGj-YH0n-OyyfmkUcblc8yFTww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
👤
#فکت؛ رونالدو 101 بازی بعنوان کاپیتان تیم رئال بازی‌کرد که رئال هیچکدوم ازون بازیا رو نباخت‌.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.5K · <a href="https://t.me/persiana_Soccer/30337" target="_blank">📅 11:58 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30336">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FPvIfhgN8voHYeKwT1VVnIxyhHiv6w3UzCgDrZugUmduLl6rKOIi36l4ee8HInKPYvw9SgJ2hegSxkybe5xTlNxe9XZ2ssg-YP31BeFGNT1fz2xgKbW61Hfvch924daqCvRI0ghrQyv7TcP4X4atk-wthPdpWVUzCsx7H6dV1HxOmCmH0WLCSktpzklAKW7kcQfFDYVZ5Hof-L0lnjCPgmysDugsGwEmvRwmhypK7ugcaOfu7_D6vGdCQtujoaZh95YhbcOFOVwUzXubIn0YqHUMqPnXJqYsdXfcFpl3y2sqr5cQghZNCZ97Dwt_RlNzxe3ghU0qqzeMqWwbHUx07g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🅰️
🅰️
🅰️
🅰️
🅰️
🅰️
🅰️
🔔
میدونی تو این اوضاع بد اقتصادی تنها راه رسیدن به آرزوهات چیه
💵
💵
💵
🔥
سریع تو کانال زیر عضو شو تا با استفاده از
فرمهای آنالیز شده توسط یه تیم کاملا حرفه ای
یه قدم به آرزوهات نزدیکتر بشی
🔥
⚠️
توجه داشته باشید که تو این کانال به
اعضای خودشون همیشه‌هدیه‌ی جبران
خسارت به صورت کاملا رایگان داده میشه
⚠️
✔️
پس سریع عضو بشین چون عضویت
محدود میباشد
⬇️
⬇️
⬇️
⬇️
🌐
https://t.me/+KoqkzqAz7CszZjlk
🌐
https://t.me/+KoqkzqAz7CszZjlk
🌐
https://t.me/+KoqkzqAz7CszZjlk</div>
<div class="tg-footer">👁️ 38.7K · <a href="https://t.me/persiana_Soccer/30336" target="_blank">📅 11:58 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30335">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Nw2DgXT2vSL2XfM6E1HlRrsOQhKdFkRye9SgNANgO5Az3a7LM0OgpYmmmccgp7MHypNI-U7MryHhXnIF4pogkqTYa_3QU8VBQqP0eE5fzioDMe04kfPXB1IHImnkfwp9k6Q1D2MYLbsnLbDe5GsyEi4EimaIur4jysghTXupGAimvX7z7M8DTzI_1CzsrdwnkZ1Mbjms_llsadG5-MtXzrTsROyZJL0Y4FrdfcTIBKiOJJ1-l4D8r-TWoRd_DljRF4-S9zXHQnZJsCrB5h1XrH-LkTaWXQbOWg3z0i7R90Smu9-n2UF_ChRhXr8etsdED6T3patXtVWtYq6nShxRBw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
همسر سابق سپهر حیدری: من زیاد اهل فوتبال دنبال کردن نیستم اما در حال حاضر بهترین بازیکن ایران چه ازنظرفنی چه شخصیتی رامین رضاییانه.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 40.7K · <a href="https://t.me/persiana_Soccer/30335" target="_blank">📅 11:36 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30334">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uL9n4w0Osj0hbYxCPWKkTbhQxUXNDuIBa2ixQFjsA35mU2sV1b83hvqivHG8z8iDc-yasCYJmeeDZnmIF5q_Z76DnK0pQUPwZZsfBSG3RfWvOezH_ouiFLa3rcJRJcXt7fGL29c9EfpPVkIJEMq8DEclE-Af6P8YfbcskL0jlmTqFuYBVuEAkLIUq5mXMp-Vgq4LA6CqCgY9QzNZzAgJx_6V6TARe3144R_s5WGh2mxdFvItKUvZ_eAzXzzSjh2plmu2WIuFbVkrUIxuRo2FElOqqdhOmgZlFDOhCrps1zClLRYefPxyK_DUBNWOaiMrMyDR3cON75RKe_mpraZlFg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
#تکمیلی؛ بعد از عدم علاقه مدیریت باشگاه استقلال به برگردوندن دیدیه اندونگ به جمع آبی‌ها بخاطر مدیر برنامه پر حاشیه اش؛ حالا از تبریز خبر میرسه که ایجنت اندونگ این بازیکن 32 ساله رو به مدیریت و کادر فنی باشگاه تراکتور پیشنهاد داده تا درصورت توافق با این باشگاه…</div>
<div class="tg-footer">👁️ 42.7K · <a href="https://t.me/persiana_Soccer/30334" target="_blank">📅 11:01 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30333">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d3db773d12.mp4?token=WTe69SpMlDwbf6JUloreDX-lcdzgrp-7YKCLeA5SQivLTRYa1AgBo7o8dsgilVhDNxNFM2-6FjRrCNXMHxjhWkmyOjmodPS9pzeBs3gKaN9kqjS4bLzyFixv47rCP5K-ZJjD8crlwbXKw0J-GHA-luiMe-ropcf76cfyzBnzN-aIFCs0w6LV4FEZk7QnxTSZ409QGH9Umf3DOusDgWlIR86GLOgCAEoTDKQdSE4y4yokeVZkbId4qB_7vMU92eDYdMaNcVaDZV_mnDAPVOnhqrF4Al5jCkCIrjIlrQhWv77NgsIM1L-ULQZyceq4x4Yk0Gnq1uIXBQqUKBPFy8fkcjZAgNuyYfknVQg5bv8vY5uPvl4v1_GUf25Cub7yIbavVoelF0w3vSZpeTmI9BJSG0BZ9rgFpryFo-UnHS_fwUyO-zcNBOOEqvSJA_BN8hNdIK5ygzIlE5FvPE9slcqzsZov92Bh9dMFxerOZAXYocq3-YxVqLTWgOSy-tn33ZQl2A5kkYXB_evCgJG1v50YYdV59-rYbNetjxVzSXt2Hl9TA9XV5wr6FMASsJPK6_4cB-loA8GTLrBoo8Io4pqYD7oCXuYE9bWaq9hRrtKp-pEIaCVrMkzigEY1HW4mpcNikJhTLkdjN5gd5Tb3jFYzFyAciFqz15IwtgLYzlGZJbY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d3db773d12.mp4?token=WTe69SpMlDwbf6JUloreDX-lcdzgrp-7YKCLeA5SQivLTRYa1AgBo7o8dsgilVhDNxNFM2-6FjRrCNXMHxjhWkmyOjmodPS9pzeBs3gKaN9kqjS4bLzyFixv47rCP5K-ZJjD8crlwbXKw0J-GHA-luiMe-ropcf76cfyzBnzN-aIFCs0w6LV4FEZk7QnxTSZ409QGH9Umf3DOusDgWlIR86GLOgCAEoTDKQdSE4y4yokeVZkbId4qB_7vMU92eDYdMaNcVaDZV_mnDAPVOnhqrF4Al5jCkCIrjIlrQhWv77NgsIM1L-ULQZyceq4x4Yk0Gnq1uIXBQqUKBPFy8fkcjZAgNuyYfknVQg5bv8vY5uPvl4v1_GUf25Cub7yIbavVoelF0w3vSZpeTmI9BJSG0BZ9rgFpryFo-UnHS_fwUyO-zcNBOOEqvSJA_BN8hNdIK5ygzIlE5FvPE9slcqzsZov92Bh9dMFxerOZAXYocq3-YxVqLTWgOSy-tn33ZQl2A5kkYXB_evCgJG1v50YYdV59-rYbNetjxVzSXt2Hl9TA9XV5wr6FMASsJPK6_4cB-loA8GTLrBoo8Io4pqYD7oCXuYE9bWaq9hRrtKp-pEIaCVrMkzigEY1HW4mpcNikJhTLkdjN5gd5Tb3jFYzFyAciFqz15IwtgLYzlGZJbY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
افشاگری درخصوص دعوت‌نشدن برخی از ستار‌ه های ایرانی به اردوی تیم‌ملی توسط امیر قلعه نویی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43K · <a href="https://t.me/persiana_Soccer/30333" target="_blank">📅 10:45 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30332">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8f00468324.mp4?token=V7xgzg-c6_wyy3OljSieqO_7tb86lXrPytOfTHVlpe42eAucmP-e5hrxQ_ne5c1h_-P8rf3X8EVJ9OgikeSWmPdLJvvEMzO2rA-FTFBCZ1gPpnSsnWcfMyumpmPCkrjCchFQ6f9f37f-YkgKTLC59Paui6FTma5Tk6LC0ZPVjh1MxkKL_YecDIJAdO1YC52uWOTOEbTxjYKwYy5VMFu5KHHlYMIcz1LA0qouyxfpxO79hgtIX2Z_MfW7uJya8JnZ5Ety_uPS2vSlIQr3UB4RxngKGU5pRseKooZAx78sMQR30TjzFEbD5AISU0lrNE2yzNijl9VAErnZpOzvAnri1oYdfxREfTIoHcFKoys1EN0rJjFeZOB2zn4Aib2vwSwA4k6lgbodk9H6Ex21o4NLbCwqQEhuVfWt7Rpuk4rlwJHTXYU9C4jxXKbuKXd9vwZ9276pFDJEsasDDQaiLjEpjfcjAer5Eh62zxMjcPgqjOt2NiyO-IB5oPzeEU6rElb6MCwSihdsWu9gsjMwNNrrDXJmAZoYC1aC_SeKGRveWtXxpFqmZEzArvTWqYflARflUkuiA5SVbxgqCYYOO3CVE5OIdUrlMAOLZIWBHCwAmD7JbD4ykTDRanBHd7CxAYyPfLEx8k9NqMXy6ZtcTJy9RSnfj4lw9mYZm_YU0HTnAkY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8f00468324.mp4?token=V7xgzg-c6_wyy3OljSieqO_7tb86lXrPytOfTHVlpe42eAucmP-e5hrxQ_ne5c1h_-P8rf3X8EVJ9OgikeSWmPdLJvvEMzO2rA-FTFBCZ1gPpnSsnWcfMyumpmPCkrjCchFQ6f9f37f-YkgKTLC59Paui6FTma5Tk6LC0ZPVjh1MxkKL_YecDIJAdO1YC52uWOTOEbTxjYKwYy5VMFu5KHHlYMIcz1LA0qouyxfpxO79hgtIX2Z_MfW7uJya8JnZ5Ety_uPS2vSlIQr3UB4RxngKGU5pRseKooZAx78sMQR30TjzFEbD5AISU0lrNE2yzNijl9VAErnZpOzvAnri1oYdfxREfTIoHcFKoys1EN0rJjFeZOB2zn4Aib2vwSwA4k6lgbodk9H6Ex21o4NLbCwqQEhuVfWt7Rpuk4rlwJHTXYU9C4jxXKbuKXd9vwZ9276pFDJEsasDDQaiLjEpjfcjAer5Eh62zxMjcPgqjOt2NiyO-IB5oPzeEU6rElb6MCwSihdsWu9gsjMwNNrrDXJmAZoYC1aC_SeKGRveWtXxpFqmZEzArvTWqYflARflUkuiA5SVbxgqCYYOO3CVE5OIdUrlMAOLZIWBHCwAmD7JbD4ykTDRanBHd7CxAYyPfLEx8k9NqMXy6ZtcTJy9RSnfj4lw9mYZm_YU0HTnAkY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
صحبت‌های محمد احمدزاده سرمربی‌سابق ملوان درباره سختی‌های عجیبی که در زندگی‌اش کشیده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.2K · <a href="https://t.me/persiana_Soccer/30332" target="_blank">📅 10:02 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30330">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/FpV5xSGqbFCY8qLPh_z8WajL-4xPP9ODVmTW3Wrrwg_nNNikMm_WajcLW5qeh-6oI0U-7r-U1mWWPWLtcD7xpMkVf7BsTjAZC1E5F_fXUlhP56KB39jrBaJP02H_89Qo_ytz-Sflb7DBY925mlbfpWf8xBbMukWxEYF9yBe_Scu6ud0pqZU7jDg81uCx-NqYVG9-_1vFevhiirtHnoJM75npHG9YY2gmDiP1VtfZNZ4ynK5iLXe3RhmWr41b5Aywym8a3r-t_P83taz6w3dTjIHh0CclhVEweL88w97dnmkxIZw0UG-0U4SowBn3VZCXtnebIEVI8S8BUvKG6COYMQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Nysgr97jgw3bbgA98_sT5eJxEv8C9u7k7ee3Vj-w_zFrMnxe5Ka7SaXeu4zCYOkSi5RxKDYgJ3Np7apnAFZ5lNvUhALuJae-6deUOzY_qAWNn5hUIFS_Nuwhwbcji5vmevcXYg9T73mTaEum3rzKHSsIgRzIYqCZChEhEREAZi707rVPYeLIViVLLzFjeqK6hdoMKFflWYgLa8RtFypYNaCg4iwXQy90VtWglg9gEL1s3S1YctElinFKumUcishleWKENZ66irQoYWKC1pG_WmeEuVTdKdvOowFB33aQoVbTSc2lFL8UFqvZPZ_ZWjlxgp36_2PSn7lU9wYt6MjYsQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🗓
فلش بک به سال 2012 زمانی که:
🏴󠁧󠁢󠁥󠁮󠁧󠁿
منچستریونایتد 85 گل به ثمر رسوند.
🔵
پی اس جی 86 گل به ثمر رسوند.
🔵
چلسی 87 گل به ثمر رسوند.
🟡
دورتموند 88 گل به ثمر رسوند.
🇦🇷
مسی به تنهایی 91 گل به ثمر رسوند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.7K · <a href="https://t.me/persiana_Soccer/30330" target="_blank">📅 09:50 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30329">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d79121e6f5.mp4?token=rb0602vtO8wFqzhToBzi9XiaiQfwPWR2wmOBGbg-7jWziT5Cn9S9el5SXZMyHfLLTcL0UFvSQyysIJ41N78Kvb4L8iieVAKZ9n7CokBvFs1HQhSZdxS5Px1tGne7Vjiul5tFGW_gvxJh4Q_PVpFh-ph-DNvZsDIdF9YW-ybKdfu8JQNB59lEKnhdCn6BYOf7LQBK54fNeUYW4_LUOu_m7AbKozbu0ryvDByd7I4YUCdC0k732ZbvesMJoWBTfnIJHhl_JvTv38-VAc-KvZS8u3RN3cUrTovIOfHsDLnf3EuVuB_QZ3aDdxaKcIfnYVM87zG1b3mnuq3HAhKnePaKgQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d79121e6f5.mp4?token=rb0602vtO8wFqzhToBzi9XiaiQfwPWR2wmOBGbg-7jWziT5Cn9S9el5SXZMyHfLLTcL0UFvSQyysIJ41N78Kvb4L8iieVAKZ9n7CokBvFs1HQhSZdxS5Px1tGne7Vjiul5tFGW_gvxJh4Q_PVpFh-ph-DNvZsDIdF9YW-ybKdfu8JQNB59lEKnhdCn6BYOf7LQBK54fNeUYW4_LUOu_m7AbKozbu0ryvDByd7I4YUCdC0k732ZbvesMJoWBTfnIJHhl_JvTv38-VAc-KvZS8u3RN3cUrTovIOfHsDLnf3EuVuB_QZ3aDdxaKcIfnYVM87zG1b3mnuq3HAhKnePaKgQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
لیست‌بازیکنان لیگ‌برتری دعوت شده به اردوی تیم ملی در فیفادی پیش رو: علیرضا بیرانوند، سید حسین حسینی، سیدپیام‌نیازمند، محمدنادری، احسان حاج‌صفی، شجاع خلیل‌زاده، محمدمهدی‌زارع، عارف آقاسی، سامان فلاح، صالح حردانی، رامین رضاییان، آریا یوسفی، میلاد سورگی، حاجی‌عیدی،…</div>
<div class="tg-footer">👁️ 46.4K · <a href="https://t.me/persiana_Soccer/30329" target="_blank">📅 09:24 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30328">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vWE7e7L1rIWXmKj2QzlvqRPjDjta7gZ2-rUBU9UwMLx28zaZHxIGo9BwZ63MKEUtfXP6wXW_mT1RXp27VeeDVDAK3lNGEhWfBOiWZTa8t86HteuYDMScE2S9ZNsmUJi6cx9YE8xMyWJYszj9j-fIK_o2Xg8zGh3hLp-LSnloN78irKq4lgAwQnBQHqX_4H4wd1R0Vz7FX42xYu6ENU_D6-nGn3Yc9WU0fVcs5OZ-Q34QOFXJ6ryLwmk7QAPjqVZqu8vaRk0P3nuUuYbCedh8WpT9CgGG19-mI0gqIgaBQqmse6plzAgpimQgSTPmIrkBcfgedaHqbOXbZdx1VPb3vw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
ترکیب‌منتخب ستاره‌هایی که علی رغم درخشش خیره کننده در دوران حرفه ای خود توپ طلا نبردند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.7K · <a href="https://t.me/persiana_Soccer/30328" target="_blank">📅 09:06 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30327">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ky8pdZlFdpikM5YYFFJAwV1L1soiCfFc1pcCsB0Nl-Gi9eEvVOfR5ZkLaNo8UX2aIF7k1rdXnHJA14zyCbIZQNSnKMhjtmKJsXwvsmFlXRbxiFVHoBTosqHmI2WT53IJJbVCPrdxR6IyYeN1J227VdmSpJAh7OtBQYw9B5ZD6aiQ3P0hoEaxbSCzNlUFzR8YzL3n63lZ4TE4bWxf1ddrkft7NDLMDz7LCD5TWS256F_qR5qqSQwcVSgWfu0npTshTKob4bnWp1hjsx0LR3u2Sp5lysqaOUiZKqbwJ8BJFJ85CD_z9rDVRpg1kI7USg6J-7DQ9c2KDfBsAt4AjIIRCQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
برنامه دیدارهای آینده استقلال، پرسپولیس، تراکتور و سپاهان در تمام رقابتای لیگ و ACL.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.2K · <a href="https://t.me/persiana_Soccer/30327" target="_blank">📅 01:29 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30325">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/rPIjtwh7uEHvnAtencPEl-eoV5nYoKoimUZhD-CCdkyp_EX-VDVjAop1IJFOFshQ2ruE3K-FvQaDfZ2F4BygEhp9BW3hKRZhDuMwDrp_YwAyDyvGS1sTqRaQdWe3DRzyJe6Pa-dq7zVFEb5-p_qJWRFqkkmwnfwBzgfGJGT4dbpiWuOhhjyR3iDWLqX8c3374jfaG47_RRgR6aQZJ921OSBjEvK_dbzX0X7bnlPDdJUU6BCwWops8AAhBR8zOCZ6HBnGiSs0lWyMdwj8OljZF_QlwrTBsBDXFSb4obCV_PlG1xUYMluG2e0ofZ_5G8SbqrZtzqta0PuXf35zktjUkw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/JV35uMZa3OBfdZHfkAhRMuwyNDUPGJmbgCziJUfJznQIbvpxpEwpBI06aRL4JpD_KRR0nnJA_JlueXqgY0RWe26mME5gxlKTXIir9H6uZi0JjSkBClifixUzUBr7ILiBashO75a91fW1X1_IjbmnZftqgvBY9HgMWtI6ielDoheY5GhvHi8bm7eQZ6rVs2SpCdnvsVSRIFMcE5jsgXgl6JG9zEIWkgCB2C-zCPXPDE6xydgTAwlhocw1sHpSZskqRPAoHTWhABLEbtNqDo8kYycOkDMhRJgBZSoZ4Jt03qcdQ1kkCx8oNjrtvxpeb4tQJlZgPSaiVQscqPLeOHucnw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📊
آخرین رنکینگ بندی تیم‌ های ملی پیش از شروع مسابقات‌فیفادی؛ اسپانیا بر دنیا ایستاد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51K · <a href="https://t.me/persiana_Soccer/30325" target="_blank">📅 01:20 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30324">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bbc5ec9105.mp4?token=TgZZFMLNBdt3Ed5Ptj-GmwXRjSMQ_COhYhndRxoU4wkpEkZDo_08wejYK-5a0vJO17SJSKNcEjXRVUYy_ES1F5BC1AjCrOVKTmsLj0qw2Jfk3KflD7sa2h5uGO8YHD1C2zYQqIHJD5vQdMkRRc5Lrs3lAwYLhm7z3nnDpOU8ba119iiikqR7wyXv3BpvhCSHsMx76smfnu5I1lnfz2HcRTgUuJHxFH2hoz5E_z2zRf11EVpdmM6VEhBZIOojAngS8uNayWsDfTGntkuPBqJn96KAbOJfJYmK6G-YNWtZwwlQuNfVP3dH1n6gKmqy709AR3AG7zh-6ToZGncEkX-spg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bbc5ec9105.mp4?token=TgZZFMLNBdt3Ed5Ptj-GmwXRjSMQ_COhYhndRxoU4wkpEkZDo_08wejYK-5a0vJO17SJSKNcEjXRVUYy_ES1F5BC1AjCrOVKTmsLj0qw2Jfk3KflD7sa2h5uGO8YHD1C2zYQqIHJD5vQdMkRRc5Lrs3lAwYLhm7z3nnDpOU8ba119iiikqR7wyXv3BpvhCSHsMx76smfnu5I1lnfz2HcRTgUuJHxFH2hoz5E_z2zRf11EVpdmM6VEhBZIOojAngS8uNayWsDfTGntkuPBqJn96KAbOJfJYmK6G-YNWtZwwlQuNfVP3dH1n6gKmqy709AR3AG7zh-6ToZGncEkX-spg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
صحبت‌های عادل فردوسی درباره زندگی سخت یان دیومانده ستاره 19 ساله رئال مادرید در بچگی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.7K · <a href="https://t.me/persiana_Soccer/30324" target="_blank">📅 01:13 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30323">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d3ec3996d3.mp4?token=a2IPuXUHjYFTgs7KLUWiiwo4NbDpqXfH_WXVD_PAKgejupotX_D3uGnpbFP-a_WTzccUashlh15gB5QqW3IBjwvIenqesJlqVJxrzz5-YyIAG1wQLGwCJiRm7bXdS_Ot9Wb38mmajcYajT1unXeKx4wxZbN8yCaF2qHzm2BmjlP5wu9pFsdstQ50ttn0AvFb9gBJBikWYHs5RbZhBx8K8wAp0nNj3eSXiknkPZhkReo9RhNb8_dWDCm1gVeEIfZ7lGHynftgbgtxUgCd8m_ACd4-AszG88f3ZavMrnFV82jXK0WCwTp-arCRdJ_Wb6vrZU_mfmfwN8478iuKz2Vw0Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d3ec3996d3.mp4?token=a2IPuXUHjYFTgs7KLUWiiwo4NbDpqXfH_WXVD_PAKgejupotX_D3uGnpbFP-a_WTzccUashlh15gB5QqW3IBjwvIenqesJlqVJxrzz5-YyIAG1wQLGwCJiRm7bXdS_Ot9Wb38mmajcYajT1unXeKx4wxZbN8yCaF2qHzm2BmjlP5wu9pFsdstQ50ttn0AvFb9gBJBikWYHs5RbZhBx8K8wAp0nNj3eSXiknkPZhkReo9RhNb8_dWDCm1gVeEIfZ7lGHynftgbgtxUgCd8m_ACd4-AszG88f3ZavMrnFV82jXK0WCwTp-arCRdJ_Wb6vrZU_mfmfwN8478iuKz2Vw0Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
چالش‌عجیب‌وغریب‌امیرحسین‌قیاسی در قسمت دوم برنامه جدیدش با خوردن آبلیمو با غلظت بالا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.2K · <a href="https://t.me/persiana_Soccer/30323" target="_blank">📅 01:13 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30321">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eXbLZHmv2oNoLuDyiW2eqb8b_XRnHzvKvxWmS6QBpvfeN3ZpVC5EpzQYgxUj-Cfy8AKeyoDkE5bBHUo6_eyooyJovQaAa8bOCjrYnf9CuznChgsw7SYV8xqPB8eQbjUPK7e_1vV0J1lhlE6PagBmhx27yTlrhdmCmKjHfKDfEwlqvr-2QTXnQGnGz82RM7T0DdUkpU67dP9-0r3PAKkKNuxxwHoPsKfalbMn55Tmr9RBunv3BMzwmohig4i58p0pdqSwcbw7b24XNhN6rgI0dqWW6Plzv1zJeXSbTZuk1Z0rpkDpFqckHBTqZ3KWKWeYneNHuX2Oa3wPZT-3FUdKTg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
شهریارمغانلو مهاجم‌تراکتور توصفحه‌اش این ری‌پست عجیب رو درباره سربازی بیرانوند گذاشته!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.1K · <a href="https://t.me/persiana_Soccer/30321" target="_blank">📅 00:38 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30319">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bY37bJT0LjFJWQEvaCJkMefm0IjdiFDbWpehMKdrtZ36DzP9s160-0vQ8rqXRAAJv132J3cWmYsY74UgtiArcRnG-IXflAKwabRRUc7XnqjOD0KOnjWEzMyCTnZsAIiTfgvlCwTKbJwn_fhoLmojImoq9RbFlcEJer-kink-eOo9qQiSkFcZ7UZ4MuOzb9dMNlMoYz1ZCkk2UQU3hlYaOAvfX8njzf8RC8-F7jPUJXseoKbwcO2m4ZJZWhjQp7Qs4N8qkCk0wutkk6UtPlq7PDlwwQrNLY4Efl6WcXd8XtchmxB6K_5a2Wvb1s_ZOYzdRwYaO6ED7n1llJw8NH96OQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌‌‌‌‌‌‌دیدارها‌ی‌‌‌‌‌‌‌امروز
؛ دوئل تماشایی هلند - آلمان باتقابل‌تماشایی ژاوی و کلوپ درهفته‌اول لیگ‌ملت‌ها
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.7K · <a href="https://t.me/persiana_Soccer/30319" target="_blank">📅 00:22 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30318">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/T8eN1SJxjFQzHdy23r21Qf78KrUc2B7vHjATcaSiJ7mHkadZyWHXtvMLW6FAdS03UwcwKgyZ8_ciQYPhpT2etL5jCepPbKZvE_qpna2sZFX4v-PXDAJBKpwempjxVSMFjmJ-aXlR-8kpJfoj2eA5LYCu9W_ykrUOLMQSZaAAfAy4qBGRp6EKhgpiJmvNzwR3LkNn406JKGILgbzLWhgwXj7nNBl2pP30zFXK72kd3TdwtGjaqn4FhZabiGriEAj16U1sJSvBQON30nzaTfR-VdZ5Qft13osX-_bunSklVOFn4trV1KgKCweVi053PaGHAWoqDLe7FdcoYhzyQBKN-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتیجه‌‌‌‌‌‌تنهادیداردیروز؛
شکست‌مفتضحانه تیم امید مقابل کره و حذف درمرحله‌گروهی بازی‌های آسیایی
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.8K · <a href="https://t.me/persiana_Soccer/30318" target="_blank">📅 00:21 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30317">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KkqWrJhRADvI3RkCq6vo9VG6fKY6AJ1ke0xmEMxSBan6vMfL-ap0J0b6HdgBug6vnRz7xeCf7EbAoDP0lQKAr0HqnW7Bo7ZIH4uFQEtvXtOV08mg8sF_Z3nj46EavjZfEVPjonhuk3-5Giild7v4ihcUkVWxngs9kAymp8j-GAcooMfrEuUHme7Dj3hsMTrzUj_RtkUFURUIA63eqFQouEUwLTEN0HviyCHkYeFYYBxjYlJf_WxNEUa8quNwbiF-Npa8jWZk71-QG2w8qlwrb8ksGDwJpHmlTtD01y9GMG8PEOlySeoTCcihMAJotWYiDRKV8Awj1xwIxv631RwRpw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🔵
گل تماشایی ابوالفضل کوهی در بازی امشب نساجی مقابل استقلال خوزستان روی حرکت انفرادی خود؛ کوهی درآستانه پیوستن به سپاهان قرار داشت اما در نهایت شاگرد مجتبی حسینی در نساجی شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.4K · <a href="https://t.me/persiana_Soccer/30317" target="_blank">📅 00:13 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30316">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/991e17f20e.mp4?token=wAnzQ15Zsu3Gc67BrykscggyzT8TWfMR4NKhhurMr446WcW-yFQJZrHl2REJtDc-bGTDXOrR-Fh8WEAwmdSjugwGbihzWstqgO_QUtQCIhrwgxegKmJqHCjsSAFde6g6MvwE_lbD2XTKn8JzFktYaMJ0PymXJ573slDEC5TscXpHMJ6Wjbuf9NjAAxZ0TTKxG7TTeZ48lj5lOzmHBW8Reyor_9awe_OKIdNHjC7bbpmKoy26a2ZMjPmHmT6chKDKww6nHpM9ofPEDiboYSeb_Y40jCsQ5WXx4U_rv1WoYut3TRKA8f2hAxy3r_F68nEB8S4a1YtqVEmnsaBtre8fZY-W70ZovSOapHMRBY-d9awL9cN9PlCL_QIfazhiy8H7f3Dyy84Rn3koFGSbvoRnGzZZFV23IseL87TcLHLb4NRmRXjL5BhZ2F2qAxa4AnV3Kd3qeInU26WADxETb-Z5PIHWd2mIIQ_NhzjMCKo6xzKZIYoU8SejXU_eW72PBSY2qJ_4JsveQPe97U2LiZ2WX577JodMZ7Rj6CzvZQR6i3KR6vddIw_0_wx_vYECStEUn3VCntqFwuBMTYF7tUCmKobLpIeAyRjEPUzX5Z-0ZK0p9kFEq7izZ42BHdoyi_jI2MtiDaRDZQRAfNVpBRGFwT7TFX267M3hFTiy2P-5fd4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/991e17f20e.mp4?token=wAnzQ15Zsu3Gc67BrykscggyzT8TWfMR4NKhhurMr446WcW-yFQJZrHl2REJtDc-bGTDXOrR-Fh8WEAwmdSjugwGbihzWstqgO_QUtQCIhrwgxegKmJqHCjsSAFde6g6MvwE_lbD2XTKn8JzFktYaMJ0PymXJ573slDEC5TscXpHMJ6Wjbuf9NjAAxZ0TTKxG7TTeZ48lj5lOzmHBW8Reyor_9awe_OKIdNHjC7bbpmKoy26a2ZMjPmHmT6chKDKww6nHpM9ofPEDiboYSeb_Y40jCsQ5WXx4U_rv1WoYut3TRKA8f2hAxy3r_F68nEB8S4a1YtqVEmnsaBtre8fZY-W70ZovSOapHMRBY-d9awL9cN9PlCL_QIfazhiy8H7f3Dyy84Rn3koFGSbvoRnGzZZFV23IseL87TcLHLb4NRmRXjL5BhZ2F2qAxa4AnV3Kd3qeInU26WADxETb-Z5PIHWd2mIIQ_NhzjMCKo6xzKZIYoU8SejXU_eW72PBSY2qJ_4JsveQPe97U2LiZ2WX577JodMZ7Rj6CzvZQR6i3KR6vddIw_0_wx_vYECStEUn3VCntqFwuBMTYF7tUCmKobLpIeAyRjEPUzX5Z-0ZK0p9kFEq7izZ42BHdoyi_jI2MtiDaRDZQRAfNVpBRGFwT7TFX267M3hFTiy2P-5fd4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
برای اولین بار در 47 سال اخیر، یک ژیمناستیک‌ کار زن ایرانی درمسابقات‌آسیایی شرکت کرد. هنگامه هادیانی؛ ایشون درمسابقات رتبه خوب 13 ام گرفت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.3K · <a href="https://t.me/persiana_Soccer/30316" target="_blank">📅 23:48 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30315">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PIRtoz-P3TNbusXQegTm-fofbC_PzG4W6_fjj-3liYqTeHWOITsg30JGFd42w1e_aftbjWCwf_0k90qsoNqKuj9rV1E77n_-1VmDufJet9ldoLxpH4QceW5f_grneaCri-eYsJgy34VvncsVN_X7vpceAT67WlN_JoeB6Ri4DdEtBBKA58NL7WuEX-m3QCqm8YKMpUIh6KZHbfN-jJjX637FdE7-IyHURTuD69BVX6_3SYxxSdsegMouW-2f73kG7EoPBR3liHzUTGSyUjHFE8h77Fc7d-0lCgD_nXWDLuyNet11wKmsGb2cfyPZNy4sfzi5L0PSaiBIVhBJdwSKww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👤
صحبت‌های کریس‌رونالدو کاپیتان پرتغالی النصر درباره زدن هزار گل زده در کل دوران فوتبالی‌اش.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.5K · <a href="https://t.me/persiana_Soccer/30315" target="_blank">📅 23:38 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30314">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vpk-ckfddWqn0SVJ49mFkm7IlcuclJ8K5qoNxTaDdpw_37R15SPGW8MjBzTCO-aW36mRiBsdDp7wVqozPUjaQHqDCbMRzY_vLnzXWs7-pBNCzps08WSDnBzDeJfD3cnYFGYIOjONYLQg3R3i8P5AauS3OTx8Mm8LvsY-APS0gPEcbv3Z6SbWsFQDscgwBbVTwyx0F2iEZdIzBzUI6xv-fWQLcSGl6cDiAqpP4Uxpbr6EVLZixf7Q15QGkbt6qojJ2YPgVZB2qpyYHbVlxeVALxr4ZmQiJHxmSmBq2YCwSzWeYvyA2tvgHparmtLZbb8NtV5LJuDu8tiYYxBOmIguRw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
تاییدشد؛بااعلام‌فیفا؛ دیدیه‌اندونگ هیچ مشکلی برای عقد قرار داد با تیم استقلال ندارد و این بازیکن بزودی قراردادش رو با آبی‌ها تمدید خواهد کرد و از هفته اول رقابت‌ها در خدمت این تیم خواهد بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.1K · <a href="https://t.me/persiana_Soccer/30314" target="_blank">📅 23:11 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30312">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/v6C4ewsx1jMvVZfEFBufbolFa6MATw8TbRCifLmwm5iB-wNw--hpkcG617DXwjAeFqOnvEN9GkxD_xTHnyPkgDUDuHw1AUfPy5FJe3CdB-BzJJM5qq4pHecivglKqYneml0XkljPYIaKLZWRNCQXl3alu02TQsYG2XL_YIx7gMl3sftw8YRC10BZQfihswEeLiQutpYay9ouP5na0D9KBlMm4KOfIYzZYcf65j02eDQYR6-wdw7GsXZGQEFDGksNjrGnzOZnq3EqCrAtexel2udKSW4CLfeICvZXoBiRPSguLB0J1E_g7ojnpHPdTHMO0V1f9_4EA-mpgWC-PuWrhA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
اسماعیل‌قلی‌زاده ستاره 19 ساله استقلال: باشگاه سپاهان به من گفت یا قراردادت رو پنج ساله امضا کن که دیگه حق تمرین با تیم رو نداری و حتی اجازه حضور تو تیم آکادمی سپاهان هم نداشتم|قلی زاده در دو تقابل اخیر شش‌امتیاز از سپاهان گرفت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53K · <a href="https://t.me/persiana_Soccer/30312" target="_blank">📅 22:44 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30311">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AI3okQLUpKvBDEXx5ZFq2ws74Vv-T0Vfu2yDFK_i8ES1QhnR28dmArTebQlNVqxb5ZInlof8AUIshCebOSp79OkfhkzXNVtBNYzAgfuf7D8Ja5LHrtbXSWcouot2j8gzDW18ZCuWtcc895MScCJLqqPNMbHCkL52YEcejpatkgRWrAeqfwvv3YVNElO0M-1G2QBW8WSB6hVN7KiucXmm1cwtoQgxjVhXDRXeRDh70PUZRSUgdNH5ph1_914RYlbbyYRzluIPTn0ZQzxLsGHTmXpqN3dyESDAzC5KDG_hi7c_YYBeEYXN5a6DbmGJLfFdRDHxFXJ7hhPj3EavUI9CAw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👤
👤
#تکمیلی #اختصاصی_پرشیانا؛ درخصوص مهدی‌طارمی و سردار آزمون چیزی که ازنزدیکان این دو شنیدیم درنیم‌فصل به لیگ‌برتر برنمیگردند اما این فصل‌قطعا آخرین فصل‌حضور این دو در لیگ امارات خواهند بود و درپنجره نقل و انتقالات تابستانی سال بعد به لیگ برتر خلیج فارس باز…</div>
<div class="tg-footer">👁️ 53K · <a href="https://t.me/persiana_Soccer/30311" target="_blank">📅 22:26 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30310">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ec82d980b0.mp4?token=AqYlFfS-igmH97qa7HOEHjZVgT0brqrqih6TFM7SKU2vVU2ouEvjG9XdMLOVaT2GBwDiELkDMdJ28XLEiwUvbggnpw8Y52hbqYWyrG2rSjoFYqeP47WYVujDOxHU4NZRWxvbnGK4eaqLmFXWosp3u69Aw-QhGJSPCSgE-tDKF9DQQzTl1V3l_1QC3qUWFNUarSe4JP9wBsfDycBsorujJsS2puVl_EoHVYCxS_3843HCO3IVgGgUJBCG1mTMQB_x3OQoV0Me1PDP2xgMtbhiLDOfCtPJcWKROPQLrgSZLjWhIc0pBE_yj9N2dIN7NAzN6HaAeCF2fEDtrYTV7A6b2DzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ec82d980b0.mp4?token=AqYlFfS-igmH97qa7HOEHjZVgT0brqrqih6TFM7SKU2vVU2ouEvjG9XdMLOVaT2GBwDiELkDMdJ28XLEiwUvbggnpw8Y52hbqYWyrG2rSjoFYqeP47WYVujDOxHU4NZRWxvbnGK4eaqLmFXWosp3u69Aw-QhGJSPCSgE-tDKF9DQQzTl1V3l_1QC3qUWFNUarSe4JP9wBsfDycBsorujJsS2puVl_EoHVYCxS_3843HCO3IVgGgUJBCG1mTMQB_x3OQoV0Me1PDP2xgMtbhiLDOfCtPJcWKROPQLrgSZLjWhIc0pBE_yj9N2dIN7NAzN6HaAeCF2fEDtrYTV7A6b2DzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
صحبت‌های خسرو حیدری کاپیتان‌سابق تیم ملی و باشگاه استقلال درباره حضورش در سریال پژمان.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.3K · <a href="https://t.me/persiana_Soccer/30310" target="_blank">📅 22:26 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30308">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ETe4zAZsiuf8XA50eZ7n2UayqnpYFpOF06ljJ-pdGJunD-dfKJr8fyybwUyrQhSBitKBeRDvnaTP1q9vG3dG6UQKgnn2XxkwmwHZGVq5QCTlTBI5mwM_fYcfZXTrVYfdLdP3vGPC_4Isn96pwjz16PN0Oye-8ecaV6LZZ5PxWpR0XRtnK-Y9XnW7trGOXGWt3590b-Dj2SfdRSrUEYm7ThbNHtIAJqsBzqBTMdhHniayR-a6NxXMKRpezezSoWGMMZPzN-bYvsMVnzIEYKZI7D9hJHMyyWV9eC9cS8_5MCY3239zCFHmscnwqFMCek_7Fy0aI2pATT4YlTPJBadnYA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
پیرامریک‌اوبامیانگ‌مهاجم37ساله‌لاکرونیا امشب به‌این‌ شکل گل پنجم خود را در فصل جدید لالیگا به ثمر رساند. انگیزه‌وچارچوب شناسی‌اش‌خیلی قویه. این 414 ام گل کل دوران حرفه‌ای اوبامیانگ یود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.7K · <a href="https://t.me/persiana_Soccer/30308" target="_blank">📅 21:56 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30307">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fa37c71dc1.mp4?token=Y1DDz7Knckk2OuYD1Cexyu5EP6E-IG_o5_f-PxnHiHWJOpuZFfzs8oraXggcl5Pzh5MVLsDPEkXsBE2AnnFaGzWgbp0KBycQanu8-K53OjhzPdmI7pw5Y3uSdNF9rav0bOrQPuv6YAUOb9er8Sf-g5ctq37_4K7_XNRSwRoYRDqBDblpFWAs0ITVRO5budP44s5u7Z6KJhD6hSMvFmoYRCN1GbwmGrPexN7MW6MZsfNRKQi2UOUArb2d7o2dKxr25liVhH92v5noVx4ijznFchjxiftrXIy8preyV3lGtnx0zRf_cMp2id-3PI8HeO6IcNeB4g9KDwUBUSmCBW99Fw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fa37c71dc1.mp4?token=Y1DDz7Knckk2OuYD1Cexyu5EP6E-IG_o5_f-PxnHiHWJOpuZFfzs8oraXggcl5Pzh5MVLsDPEkXsBE2AnnFaGzWgbp0KBycQanu8-K53OjhzPdmI7pw5Y3uSdNF9rav0bOrQPuv6YAUOb9er8Sf-g5ctq37_4K7_XNRSwRoYRDqBDblpFWAs0ITVRO5budP44s5u7Z6KJhD6hSMvFmoYRCN1GbwmGrPexN7MW6MZsfNRKQi2UOUArb2d7o2dKxr25liVhH92v5noVx4ijznFchjxiftrXIy8preyV3lGtnx0zRf_cMp2id-3PI8HeO6IcNeB4g9KDwUBUSmCBW99Fw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🟡
👤
کریس رونالدو: ممکنه‌این‌آخرین‌‌فصل حضور من در مستطیل‌ سبز باشم اما تصمیم نهایی رو هنوز نگرفته ام. اگه شرایط همون چیزی باشه که خودم میخوام ممکنه در مستطیل سبز باقی میمونم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.2K · <a href="https://t.me/persiana_Soccer/30307" target="_blank">📅 21:46 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30306">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Sr-IiGRDXsf7xhxFE5caFRPUqGvlFwM554QaKSOf4FO65iHMH6CnkCsiLdJHr28GnjqJxS1EXbfQHyhatmB13KCHpEmZK59GJ0EXOkXvQYnEV8XwbHgLK_k6ucOtcl_kCZ0UuGe25027dOjOYwXLVbWI9gXxzn7EqjC2ZNL7B8RLKSze7Z9D6gYeFpiVaFIFeajsBpSu-9vf0fHDUMYOLITb8CyMpyyqHyM37GPLKnuwzFg70z348BdvPSSdpUlgXqso3rb4GLSyZZ-RL2R6I1qVDXqoNMaKYadx8WgzgFZmVTqMRffAVQdGX1J6wuVNDdxlzBygCGIWc9HxX-8K3w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
بهترین شروع مهاجمان بارسا در تاریخ؛ رافینیا با ثبت ۱۴ گل و ۳ پاس‌گل مجموع ۱۷ مشارکت در گل درفصل ۲۰۲۶ یکی‌ازخفن‌ترین شروع‌های تاریخ بارسا روبه نام خود ثبت کرده و مستقیماً پشت سر شاهکار لئو مسی در فصل ۲۰۱۱ با ۱۸ مشارکت ایستاده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.9K · <a href="https://t.me/persiana_Soccer/30306" target="_blank">📅 21:17 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30305">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cb8e0zelytJ4mMqmGsaOEmEiQbkVtUKuymjq6Z5Dm_88rTFBz4WhwCrRfhlQdmkVhFDTuNIU47qZrcyjbM5guER_75OI7imhxiVi25x2B76MEK3kdeY27egArbmDjroz0E62sUt47uORqx4fYD-8krpA61lFNrPdpRtZkd_FzvgBoB9JEdnNqRVr9glQUUkLUDk9dVs3i2El0bEsQV2xFTWip_6aNCUs1p4dvezgJ60cGuHHC7-3wD-Od0Kvn_pwGdH9q7EyBgSQ-XdJWO6FnDD1BkmYWJ3RwM75js7844oVobEBjdyYkeEr21IrTDw41dpZEVenqmVWXBBKRXSpNg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
👤
کریس رونالدو:
ممکنه‌این‌آخرین‌‌فصل حضور من در مستطیل‌ سبز باشم اما تصمیم نهایی رو هنوز نگرفته ام. اگه شرایط همون چیزی باشه که خودم میخوام ممکنه در مستطیل سبز باقی میمونم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.5K · <a href="https://t.me/persiana_Soccer/30305" target="_blank">📅 20:58 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30304">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">‼️
موزیک‌ویدیوجدید ابوطالب حسینی با بیت کاگان منتشر شد. خیلی‌خوب‌میخونه لامصب حتما ببینید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.9K · <a href="https://t.me/persiana_Soccer/30304" target="_blank">📅 20:48 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30303">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5e4918be83.mp4?token=Z16NiLsKlxZzaLouKnIHLfUoz29lZ09VDUwnhBB4RgqjHxAl8L_iSnApgOQGqhWpDK8sgAgpQrtdwuUKm0ljE9Wy4HJcbe1x7VGmDYQptXl0cntIMt5BIYtyGQ32qT5zr8zqaEwMwWCiQBkyz3v8jUvilW1uf2jCJ9bYhFEuH4kSSleu3E3ha8ACQ82cWu2vc6HfON5a3sxJhSVvJB1EyFEi8Fy2FDnDQVQrlCyAtqJsm6U9dXlu45QCw7G6CauPexHsLAfuzzvhM-oFzVqwvTu5Zcg6IN9PwyMYilSWU8PdrsEwrgahqMFhkF0aPYFcmtsBrhMc0GnVXP0XE-zJQQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5e4918be83.mp4?token=Z16NiLsKlxZzaLouKnIHLfUoz29lZ09VDUwnhBB4RgqjHxAl8L_iSnApgOQGqhWpDK8sgAgpQrtdwuUKm0ljE9Wy4HJcbe1x7VGmDYQptXl0cntIMt5BIYtyGQ32qT5zr8zqaEwMwWCiQBkyz3v8jUvilW1uf2jCJ9bYhFEuH4kSSleu3E3ha8ACQ82cWu2vc6HfON5a3sxJhSVvJB1EyFEi8Fy2FDnDQVQrlCyAtqJsm6U9dXlu45QCw7G6CauPexHsLAfuzzvhM-oFzVqwvTu5Zcg6IN9PwyMYilSWU8PdrsEwrgahqMFhkF0aPYFcmtsBrhMc0GnVXP0XE-zJQQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📊
نتیجه10دیدار اخیر ایران و ازبکستان در تمامی رقابت ها؛ تیم ملی ایران فردا و از ساعت 17:30 در دیداری تدارکاتی به مصاف ازبکستان خواهد رفت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.5K · <a href="https://t.me/persiana_Soccer/30303" target="_blank">📅 20:39 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30302">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8fecddff57.mp4?token=U6n3sKQblTp906xmupJr0Vhy2SA0yni7iNM0A4p1RW91gW6Zc1kcW9kb1tAOB-2ASNsEsIoUL3PAtR3kk_qrguigbCmIa2Exlk5cxTf7FPnSVcrkt5WH7VdeVRcpOfRvCRjA1R1tnE_jyZ5NRpVoL39gff3K1oEgvGHuf4dpameH3P1-z0OsGUDBRmxQuDJWlRexkECMj3QdwmEfPiENVeJRVhY8psPGy3yfxhhTXPBb3Lrn_5ux1oiO8XhEKbP82Geml4EFHbzNcKbgWPiee1Ri_zJfL_IftPNJ060aH48nipe16cghY9czQHUaaDtqF3Kmr7V4kJjrODps2QlbDQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8fecddff57.mp4?token=U6n3sKQblTp906xmupJr0Vhy2SA0yni7iNM0A4p1RW91gW6Zc1kcW9kb1tAOB-2ASNsEsIoUL3PAtR3kk_qrguigbCmIa2Exlk5cxTf7FPnSVcrkt5WH7VdeVRcpOfRvCRjA1R1tnE_jyZ5NRpVoL39gff3K1oEgvGHuf4dpameH3P1-z0OsGUDBRmxQuDJWlRexkECMj3QdwmEfPiENVeJRVhY8psPGy3yfxhhTXPBb3Lrn_5ux1oiO8XhEKbP82Geml4EFHbzNcKbgWPiee1Ri_zJfL_IftPNJ060aH48nipe16cghY9czQHUaaDtqF3Kmr7V4kJjrODps2QlbDQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
خاطره مهدی مهدوی کیا از قرارداد یک میلیون پوندی اش با تاتنهام که بخاطر سربازی او لغو شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.7K · <a href="https://t.me/persiana_Soccer/30302" target="_blank">📅 20:11 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30301">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cfe814a720.mp4?token=jvITuig-2B-OcVBKQPeaACGQQBbswBZrewl8Nhqipyl9fBQUuCAIWogO_vu7dfqleLw-UggOewgE1kehjCGFRlYoTM9ozpctUM9EZu8tnGFf5zlrkSw5n-WSO6J-mYu6ciM2DcjbJ0m_bMxbBsis6EA5V-JcX93t-DOPNUKn_uh-3FlnAtH_uZ2yBFMoOGlanw63us7m7cM6tsukj8vUctajl2icHjff_n_z4184NBjDKeztNSrDit98SQ3_XTMuhYv6H5BAyLgH5iX5DBlEWbH9pqDuhsaLyHxIWUVqMdusj_WcGDcdiJ9wE2nMVdAJCvnR-miQ_XJOwkUhvV9SewZagqgV2ovRRRKvj-g0UOd9g7bYAjYAETXtnPgChBH51Mh_VAE1nZhQa5byRUPp3UZZVrRwJV4C0hfCMkg3TBwZSsRaG3fShiVpUI1me46EpxLRlwhy00yZqEuqQQh1gWzsTIavnJfejGbqn206l18g2JwQSITd0U7PkvNPNB4-WukM61loI0zy0w5pgWcgVfm1q4IWGxaBL_IyuSMTnp1E-5IIswc0QZW2raC-TTREtgx1jSxKGSgt84T_u0cL3yl1PbGPYiwsXkooZRYJgi3CQy7q5jQro_L-I3rdUwYBh2o7hS2Lh_Jr_5gTy5jlNagueWtd9LSjNL0NedA-NlU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cfe814a720.mp4?token=jvITuig-2B-OcVBKQPeaACGQQBbswBZrewl8Nhqipyl9fBQUuCAIWogO_vu7dfqleLw-UggOewgE1kehjCGFRlYoTM9ozpctUM9EZu8tnGFf5zlrkSw5n-WSO6J-mYu6ciM2DcjbJ0m_bMxbBsis6EA5V-JcX93t-DOPNUKn_uh-3FlnAtH_uZ2yBFMoOGlanw63us7m7cM6tsukj8vUctajl2icHjff_n_z4184NBjDKeztNSrDit98SQ3_XTMuhYv6H5BAyLgH5iX5DBlEWbH9pqDuhsaLyHxIWUVqMdusj_WcGDcdiJ9wE2nMVdAJCvnR-miQ_XJOwkUhvV9SewZagqgV2ovRRRKvj-g0UOd9g7bYAjYAETXtnPgChBH51Mh_VAE1nZhQa5byRUPp3UZZVrRwJV4C0hfCMkg3TBwZSsRaG3fShiVpUI1me46EpxLRlwhy00yZqEuqQQh1gWzsTIavnJfejGbqn206l18g2JwQSITd0U7PkvNPNB4-WukM61loI0zy0w5pgWcgVfm1q4IWGxaBL_IyuSMTnp1E-5IIswc0QZW2raC-TTREtgx1jSxKGSgt84T_u0cL3yl1PbGPYiwsXkooZRYJgi3CQy7q5jQro_L-I3rdUwYBh2o7hS2Lh_Jr_5gTy5jlNagueWtd9LSjNL0NedA-NlU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
آنالیز دیدار هفته‌قبل دوتیم اتلتیکومادرید و رئال مادرید؛ ژوزه مورینیو به‌این‌شکل‌بازی رو واگذار کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.4K · <a href="https://t.me/persiana_Soccer/30301" target="_blank">📅 19:54 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30300">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7539f4c8be.mp4?token=Pkt8NG_JHNCXVqEG5gQtvMHwo8GW0g4wgogRi559MHEgPKw_0SPK1BUBsJJePoTv4dAifwfqqpjDOv1DGlEt3ZPQwP9kre-6aQFzWaHp8uq3tueg1r6UtRmr7_QhdMEjwzRohxV-Hf7PdgmqHYerYvfUegvBCP0WYCjrZ-wFTYuVU-QouyzdTq7dn5dCffaKmXdvzZeGClYla95fILP9j2wqT3DsQWAUtrur6BJ2_4M7lMULtI8sS1VxRPEVGumdnEN1DVTF5Hp27-U9sr0yApGOTv5ou5dnLWdiWbHYG3e5kvPZDbjeM4AfZ0LwNd75d7jFcnkffXH6-yiKHuIErWr43nWAsPgzYIvbZ_ng5zQrLJzSvFoqKNd6nt2AP1E-GVthocd3Qq0dg9mTDP_aV1gkSJ3IGu0uMu9Svxf60M13fC--TT0gnJSKGnqf9dsehihLig2EKlHBQSFgD3oiMzy0vt461knstEWhfh6I-KXMW3iW2tjatMQbaaE_BmZzzgwO3J4k4v__RXhTJVaC5Ag77_oAFFyjK-igWGRXiM1sFJADtj-7Z_7R7SCHjXwm6fElm9xNnxJq2UMPewewEjd56PWiGdKTkf8RK4yW7CiiKfLnD1LHqbZKe768fyJAr4-d8OGSbkJKgl6U0yIvlo1IsG9CS8bESf3FInWA2yQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7539f4c8be.mp4?token=Pkt8NG_JHNCXVqEG5gQtvMHwo8GW0g4wgogRi559MHEgPKw_0SPK1BUBsJJePoTv4dAifwfqqpjDOv1DGlEt3ZPQwP9kre-6aQFzWaHp8uq3tueg1r6UtRmr7_QhdMEjwzRohxV-Hf7PdgmqHYerYvfUegvBCP0WYCjrZ-wFTYuVU-QouyzdTq7dn5dCffaKmXdvzZeGClYla95fILP9j2wqT3DsQWAUtrur6BJ2_4M7lMULtI8sS1VxRPEVGumdnEN1DVTF5Hp27-U9sr0yApGOTv5ou5dnLWdiWbHYG3e5kvPZDbjeM4AfZ0LwNd75d7jFcnkffXH6-yiKHuIErWr43nWAsPgzYIvbZ_ng5zQrLJzSvFoqKNd6nt2AP1E-GVthocd3Qq0dg9mTDP_aV1gkSJ3IGu0uMu9Svxf60M13fC--TT0gnJSKGnqf9dsehihLig2EKlHBQSFgD3oiMzy0vt461knstEWhfh6I-KXMW3iW2tjatMQbaaE_BmZzzgwO3J4k4v__RXhTJVaC5Ag77_oAFFyjK-igWGRXiM1sFJADtj-7Z_7R7SCHjXwm6fElm9xNnxJq2UMPewewEjd56PWiGdKTkf8RK4yW7CiiKfLnD1LHqbZKe768fyJAr4-d8OGSbkJKgl6U0yIvlo1IsG9CS8bESf3FInWA2yQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
حدود 88 روز از این‌ویدیو تاریخی از خوشحالی مجریان شبکه دو روی آنتن زنده صداوسیما گذشت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.8K · <a href="https://t.me/persiana_Soccer/30300" target="_blank">📅 19:54 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30298">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qPufOWyrNYxBjfUgQKhEnyxqrIiNe6JPbDJ8b4Z1CHenU7q2jnmeZmc-TyUlaKLDiUv7xR6b65S44sB4E_Q9MJhYChEJOiL-PyhlTk_IJeaY6yTAD7Ykw8P1t4qIt4-aKLkASzVQuAF_l56HXW1kWASiS47RYr3BuD7luSq3SuuD_HEc2NdygXZlhBPRsImbGbOXH_GlxJ6FuthX_xkFLpDobsFApijsB_JIezdQyTbLePCyC9xTsiF4U_NLclWJLgEBun3PUuR9dlZ5Js57-ISOJpfv2-4x1imYHzaonb6FQT9-ihuXcVehX6BltjziBY1KpT2eXd8Cyeba2pi_Gw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
تعدادگل‌های کریس رونالدو و لیونل مسی قبل از جام جهانی 2026 با بعد از این جام تا به این لحظه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.1K · <a href="https://t.me/persiana_Soccer/30298" target="_blank">📅 19:40 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30297">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lbQ6mamsydrF48lmLl32XcaQ-x7KS2kQrt4hqDfu5FkcRY0GO_fouNtb44gnD8YePC7BOlW02wCqIUYxZMcwI6U4b_gIGjSzfvp3MLYnVDjv9bzTFNCSIrxah9qbyUypeJnY8cHSSUTInzY6RpQAeeVtS1rrG9m_FpZb89Fft8OvJC9Qff0HeVj80XaKvdVfuXBcZHGilx8wLkIBP8aaR8q08xvnXdUBDMC58ERQRj5jTRA-cIZgvH0y8PKYj7wYcXUVoSDki2w-6MrsuAKw4u64kgUFQ0J3LjnbnrvSGUbNHFqsDdng79XdzWCD581tVrqi_RLRdLej4r51pKC6OQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
#تکمیلی؛ طبق شنیده‌های پرشیانا؛ مدیریت استقلال و شخص‌علی‌تاجرنیا رئیس هیات مدیره آبی ها بعداز انتخاب‌مدیرعامل جدید آبی‌ها با مدیربرنامه‌ های یاسر آسانی برای تمدید قرار داد سه ساله ستاره آبی‌ها جلسه برگزارخواهدکرد. درباره مدیرعاملی هم چه فرشید سمیعی انتخاب…</div>
<div class="tg-footer">👁️ 50.9K · <a href="https://t.me/persiana_Soccer/30297" target="_blank">📅 19:22 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30296">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qg2TZI3vNZ1NbHSIAaJK2DxlX9znCT8eXBmcXXVJUiPapeYFW6logRYNicRoecAWYnlYkZRjaoQvKoE_Aaqiyi0pzHW6z4aKD-6m2POxOlPou3tOWxhPI2pBhxPj4B1D1E3yuEUSdzN8-wlJl70sa2_ZR08Xni3Asl_Es32tNxcWtXWYNyPahWi49nrQr4Tx6xnv4AyymAkGVcQ08P8DyOCMSpp_ibQ1jUGToTTd7dVd-ilOjO6tFBCp2VibUNEP1f4Q8k8VtcPCkhdjIILCb0rCvwXnOWoNpQF_4lcxFag0QOuYOzce-vAqMSkUXXtS7A-O_ravUV-7o7V0d0PpmQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛ طلای‌ناب ورزش‌های الکترونیک بدست آمد؛ قهرمانی‌تاریخی‌پلی‌استیشن بازان ایران در آسیا؛ تیم‌فوتبال‌الکترونیک‌ایران در فینال بانتیجه 4-2 برابر مالزی به برد رسید و برای اولین بار در تاریخ به مدال طلا دست پیدا کرد. گل‌هاش تو کانال دوم گذاشتیم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.4K · <a href="https://t.me/persiana_Soccer/30296" target="_blank">📅 18:45 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30295">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YYz-uKNQN2a2MfKKjrxb1c-CNGuuGvSZp-W-raNfIH-bQJxU12aLl8GivqJTn2Vjk7NH1D797jq8-rC87VuQXHfDl0Ojmcpzlrg24lkVrfcRebztuveAzGOdca6zuiArnD58dFKBgSiMjhr-801UkdGqtTc1Anx5bbS87Unw0HSsSWWKT_wYM1NQWw_dN-Ke8sOCF4IMnr2uTwfXIJqAtq8bvkQhf-fB_JEMcxuVgHExEWXjFRJdM6wNGoQ9ehUx1qHY1hRKfwj5S0ZDWTScMSAVlMrzDJld0XmwAQs9niI1wyaKyQQXf1dtOBs3K4Yy_YxHFCvjKq-gwMEFDnHf0Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتیجه10دیدار اخیر ایران و ازبکستان در تمامی رقابت ها؛ تیم ملی ایران فردا و از ساعت 17:30 در دیداری تدارکاتی به مصاف ازبکستان خواهد رفت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.4K · <a href="https://t.me/persiana_Soccer/30295" target="_blank">📅 18:10 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30294">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d65d70b248.mp4?token=mdKd2fFdzIeg601LbwUDyR5jW-wCy6MlP7XifNpky616TuT_4whhtfwqZCXdCp3J2S-75JlvzQ4C5oTUD1S7lFhP9bHRBqOlhV_WJ2M4gI28QbH13DyxcusKn4b-6b5gjuhk6WI4rfHlfGYG5aet5YeA2rfjQXzbMr6YoBiPcFv9-oCwjuk3VOI_rAmSWRUK2m0sB4dR2KpxfMZzunlro6_hVDeyQ0GsEE0w5eiEyarJVr-JecR0OE9QW5lF9Eb9RM6T8d8uFIsRor62KmmG3CzzJrfjR0fXYpz2c8pBqPpYX1z-yETUDr1prP8CpDo3RCVXf9eBLRSLXF965tv1HQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d65d70b248.mp4?token=mdKd2fFdzIeg601LbwUDyR5jW-wCy6MlP7XifNpky616TuT_4whhtfwqZCXdCp3J2S-75JlvzQ4C5oTUD1S7lFhP9bHRBqOlhV_WJ2M4gI28QbH13DyxcusKn4b-6b5gjuhk6WI4rfHlfGYG5aet5YeA2rfjQXzbMr6YoBiPcFv9-oCwjuk3VOI_rAmSWRUK2m0sB4dR2KpxfMZzunlro6_hVDeyQ0GsEE0w5eiEyarJVr-JecR0OE9QW5lF9Eb9RM6T8d8uFIsRor62KmmG3CzzJrfjR0fXYpz2c8pBqPpYX1z-yETUDr1prP8CpDo3RCVXf9eBLRSLXF965tv1HQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
👤
انتخاب قابل تحسین آموزش پرورش برای مراسم آغاز سال تحصیلی جدید؛
خداداد که الگوی خیلی خوبی برای بچه مدرسه ای هاست امروز تو مشهد زنگ آغاز سال تحصلی یه مدرسه رو زد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.9K · <a href="https://t.me/persiana_Soccer/30294" target="_blank">📅 17:40 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30293">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5801a724fb.mp4?token=K1gQUEhtphPVi49YKmeJ4EJyj5PxyW1CNzc-lYfSrHJtxz_ZX5Z8j4ECbriL7y2dV46btvw5eDzsEg6ekFWGhJIW9ub2trshLQGX51t0LHA3pWQAvHLpGbZvUIY6sexAl0QRSXGvqtkj7-vJ9Y1kWHtK4Y3m5qHfJ9OtWxIktJ6GmjRovRk3EC4xR7G7q0tKYM6cKDB9Z07-By6OAXUrmtFmVrQJO2QBPXjgoTQbXTCr5fu58KNm0X_PWd5HqQh6OUc_-RXrPfhMCWiUcjpqK_iwDdLfD2hioDeUoaD5W0SbWWYtY6TvJIy8fi5FPa31aGWzv_26Jcrcw5lBXMdy9A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5801a724fb.mp4?token=K1gQUEhtphPVi49YKmeJ4EJyj5PxyW1CNzc-lYfSrHJtxz_ZX5Z8j4ECbriL7y2dV46btvw5eDzsEg6ekFWGhJIW9ub2trshLQGX51t0LHA3pWQAvHLpGbZvUIY6sexAl0QRSXGvqtkj7-vJ9Y1kWHtK4Y3m5qHfJ9OtWxIktJ6GmjRovRk3EC4xR7G7q0tKYM6cKDB9Z07-By6OAXUrmtFmVrQJO2QBPXjgoTQbXTCr5fu58KNm0X_PWd5HqQh6OUc_-RXrPfhMCWiUcjpqK_iwDdLfD2hioDeUoaD5W0SbWWYtY6TvJIy8fi5FPa31aGWzv_26Jcrcw5lBXMdy9A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
حدود 3.5 سال از این‌گفتگوی تاریخی علی فتح الله زاده با محمدحسین میثاقی روآنتن زنده گذشت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.6K · <a href="https://t.me/persiana_Soccer/30293" target="_blank">📅 17:28 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30292">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/an28A1o6AxMkP-GX4gXiwc1CgSpClaxrsissSYFvPvvLJjsj78wdRK4wlLsDBdbrzp7HX8HWYu5oGHI7drIrrvM9pxHhc2Tf81kWpfCWXGba3Sxz7Dyjy8T9DRctjrfIpNe-EiEvtgrsnUhfX5A82zRR9VzFjfXf5Ut1NNmxjDtx3aLLEmuX6p4_aR7wFc-E7MZGuWT9XU4zvXQMxxEocWeXcUKanlRiyC7EXaqomAKDedNBI_4ohiy0kisKjrc5bVE8eriGjVWcnHChcWo5SkgR3vOpllQQw9WO-Z9O1lP82u1-JcMSk9p4ppTOIb74vn4-JomX9LmyK9HEK_Z1Cw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اشرف حکیمی، ستاره‌ی پاریس، با رد اتهام تجاوز، مدعی است که این پرونده یک سناریوی ساختگی و ارتباط آنها فقط در حد بوسیدن بوده‌ است. در حالی که شاکی بر ادعای خود پافشاری می‌کند، وکلای حکیمی می‌گویند امتناع او از انجام تست DNA و بررسی گوشی، نشان‌دهنده‌ی دروغین…</div>
<div class="tg-footer">👁️ 51.8K · <a href="https://t.me/persiana_Soccer/30292" target="_blank">📅 16:47 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30291">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VMlQm0E_ewWjw8jJJeuPq4mwnfjnK307R8g6q5ntDpySI_oBTRy5khXs08_HnrC2jcvj09bqi1UlLb50s_5zA9mzTvEUf3frP4yrV4kJJCP2R4yRhhElud__CG5G8iSOGkcDB9sPXZmeU0G517woGJrhU9omA2mzgjkBROdPbG1Epv6dDpvGakCex37cJ978wZSsVsgV6RQV1JyCMcZwlaCQf_p494A_l06y_cNx5H9DkGetZJVnH_htBfOAxdZImkQIE1PQfU0DKJS7StfTgKDWNN2mCcFVJPe-9I3oIrj8il5_3EK_mFpr7THRhWOWlG0fKc2U98g9RS2gM1J-mg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛ طلای‌ناب ورزش‌های الکترونیک بدست آمد؛ قهرمانی‌تاریخی‌پلی‌استیشن بازان ایران در آسیا؛ تیم‌فوتبال‌الکترونیک‌ایران در فینال بانتیجه 4-2 برابر مالزی به برد رسید و برای اولین بار در تاریخ به مدال طلا دست پیدا کرد. گل‌هاش تو کانال دوم گذاشتیم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.6K · <a href="https://t.me/persiana_Soccer/30291" target="_blank">📅 16:34 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30290">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nEzoHJoTqV8jmYqqW2aTSR0FOTbBEbkSblMMTHGj-KWZLd764lh--GIf6-ms5LB5a45oaC5u3ykVPt8qAy3slwVnrZQ_gD4NV4PUagW_YWuv9x3EiPTyXOQ17sZZsEhAIyh522hK-D5UpGTM93XBrwTXCg1rXigQjzK48iu8jUjNh2bRBrJJtRUjwdxFEOzNJmu-UJbwW9KUI-QU1q7S4KuTMrnB0d-u73-8YJsIcKxBGjSxZbaPWLzRfSlLtRonamIW8KawnLHOXseYi--4oo25EQE3TokbYMgtoyujYSR02Jo8isj-J3rHZQETViLj98cB_chn4ZCX9GxnOetoVA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
ظرف24ساعت‌آتی رستم‌آشورماتف، جلال الدین ماشاریپوف و یاسر آسانی 3 بازیکن خارجی استقلال برای حضور در تمرینات آبی‌ها و دیدار حساس مقابل تیم تراکتور در هفته هشتم وارد ایران خواهند شد.
🔴
اوستون‌اورونوف و مارکوباکیچ دوبازیکن خارجی تیم پرسپولیس نیز تا پایان هفته وارد تهران میشوند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.2K · <a href="https://t.me/persiana_Soccer/30290" target="_blank">📅 16:13 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30289">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/h9ojf0RpD-qah0zTZbdIH9QzuMOrdyEt_BESBbxg7RjSidAlUMSvPBp1OHTH_tIyDWSLo4Bw0YvIqrbJUiEdzyiVl9ozM17QeSCGG0xb3AcnDiwHowEU1-N5r1AVFeP-fVVsvD92ZVmWkGBdB5V4r0gN07Tm_YTYOfmfEEpNorPdFnsBja2fG_O8pZWDhb8gp9_fZZmKt4sSMy7CvLPpg3rLaBRrj6ix7Zu_J6mcTiA8g71EG3byx509zQri1qNJFABb7StHWkndNhYXnsLkSsqzqixw9J1GjqNO6SFjLWSXbZXS12CaKCHYRdtgZiqFILapBO60DZ1KPefXis5AjQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎮
تیم پلی استیشن ایران در فینال بازی‌های آسیایی مالزی رو دو بر یک شکست داد و قهرمان شد.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 52.9K · <a href="https://t.me/persiana_Soccer/30289" target="_blank">📅 15:35 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30288">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/euYZgC3GAdTjVNWLkmcH9SA_l9wY6BnlrQq1ZmkMKneYLdPP2xJNSQ4UYKBXETyTFFhm-SPg6ckeN61ZX5pKJG4HA0jwYzn-GGH-gfBpa6yBLTOMU6CIIgt1ocwCJdcsTnZgP923xbOyRA7YIzOJhJR1qtj5TUKXlcjxsEQ6AjGptvVYcdsH8Q5DfdOl8kgbWMizf8PG9RF2aLl-QtpeOaOfaybSLx9ebkimSSo5AGWxW-m8SC2EcQOWtozrX9uoX_kkMsliOOPhDYEsHPARDa1fnTDmorqDGwN1fZV4kEQzl7b_FCxekflhA41HBWrjDxMffQuoqUrtrLuIkeBB_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
مقایسه.تعدادگل‌های‌کریس‌رونالدو با مجموع گل‌ های رافینیا،امباپه و هالند درکل دوران‌حرفه‌ایشون.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.7K · <a href="https://t.me/persiana_Soccer/30288" target="_blank">📅 14:59 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30287">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/joKI4RLoR5a08dYvJYtlRvoBkNbO_JqSo15ub6QgY5CBDvtKTjJU4CzpSb2gJy_hL3S4BXpQyV6vJx4A4uyyrq2EqZdTiEN9SaBfyoVUBai1-zDpZgtFGUxrzJy3ugPO-wCQBU0gzpgFomfpdZIThxLgotsrjFA8ivgDQzPp5Z4XLAID6DVXc5vVAQx6pol0js3KxYYUxsQkrQv4DGgtJwzRFCzs1HOpUCo4R4sXY4kjQbUAzDXUzupQ2TFVdGr515v92jNe1IHgRJNmoAj9s0TUS7Lnng_e4Bax7pF9qbnyIdZmk-IoyKwwR3wbb2xkHlR6-5VCscGYeSW5RYx9eQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇦🇷
دراقدامی انسان دوستانه؛ لیونل مسی 2.6 میلیون یورو برای‌کمک‌بساخت‌مرکز مراقبت و درمان کودکان مبتلا به سرطان در شهر بارسلونا اهدا کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.8K · <a href="https://t.me/persiana_Soccer/30287" target="_blank">📅 14:42 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30286">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cTRXSli2PniUJm0Y5pGFUnhxC8Wgz8CS0HsOnxVpWRQWuvoTRtunkpCZXQ--T59T1RVIdRYkO3FluDE_QnzBta15uMCOQ9hUnZYESUv7tPw4Nx-LYBchTw53sfzPXSlf_Ql3fDVDp4WI0HrIZtaZBnb9yrlkPko0HYgExpMOgNQ8dppyiPhIRk5-mGo6OM2XP2DNFHw7Sgc1eXDuIsNzywfUNoOP7LpUnLlo-T5x1EG3ViuAVhso_rKdd6nW4YhtizD63_-RdW3G-uiKg5r0nShop6IOuJ7D0esrFTBeZMburPuZcyt8OLyBg0i4wgCgeNa7Osh_yfA3fRDum2_mxg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🇪🇸
🇺🇾
نشریه اسپورت: مصدومیت مچ پای فده والورده تشدید پیدا کرده و او 8 هفته دور از میادینه. بدین ترتیب دیدار حساس با بارسا رو از دست داد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.3K · <a href="https://t.me/persiana_Soccer/30286" target="_blank">📅 14:31 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30285">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jcoRs20sO24iV-Av9efdlfVrujLWpb83Q6xHJNDGbRl16etAsn6kyXzpnIwZ8DQqeJie1gvRdVXQP7rtRVGBKoSQhghdc_j-hKZTzt_hUffgj6f5OJA01cfXqPmU0swnGUIOBD2fH4C4Ys_sPrB4k_PImTqaBcGoqIjK2hFpQPx7OT5Fz-bU8PuEzUiaG-VsFqMXvFUuIGHT6PNH-pcDXhju8VY0MRSQ0JHN5IUQ3sbQEGVgzlfbXMnUaiGKKbmAMUUPdIjpb3_UeEmP332F-2b5XS1JXrlVt4s3ctnAqqxsiGRBbIEakNZLbLQ3GNya4NovsJ3KzghuxPFVa1QlSg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇳🇱
🇳🇱
تیجانی ریندرز ستاره هلندی تیم القادسیه:
نمیخوام وقتی فوتبالم تموم بشه باز کار کنم به همین خاطر تصمیم گرفتم به عربستان بیایم در کنار کیفیت بالای لیگ این کشور آن‌ ها دستمزد بسیار بالایی رو به من دادند که زندگی خودم و کل خانواده ام رو تا آخر عمر تامین میکنه و نوه‌هام بی دغدغه میتونند بهترین زندگی داشته باشند. یک‌سوم‌رقمی که باشگاه محترم القادسیه به من پرداخت میکنه هیچ باشگاه اروپایی پرداخت نمیکنه. از انتخابم بسیار خوشحال هستم و میخواهم سال‌ها در لیگ حرفه‌ای عربستان باشم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.9K · <a href="https://t.me/persiana_Soccer/30285" target="_blank">📅 14:00 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30284">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1454042688.mp4?token=pfZ4h2bUoAoEdYi-pdvOsiTbkouhQ6tfcnyiuuYGySMd1XyE1qZVax_ls1rmhQAZa04AyJlDhvpypnne-UElqewx1qMCHpiEiii8IJOk6CxZ_xvxjVsVeXEWLQGmYGetLyjecBcCmluXK7DeFerT2EkgCzDaE2s1_0ojs4KU8W1g-GJxkLM-zEJgNdTAYmKuMpXf2xOUjhp8Et068bT8Wy8f6ArVJbcd5sptMoEhGDKGAylTR1kGaAksr1RJUZQ_1s7DwhQ8kSppKmpUbMSOeK0ZCEmD35rYMItcS23LWtQg_et50vlXzcO3eg68y6RLQnxN2SeZ0IcO4dPW33mSBg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1454042688.mp4?token=pfZ4h2bUoAoEdYi-pdvOsiTbkouhQ6tfcnyiuuYGySMd1XyE1qZVax_ls1rmhQAZa04AyJlDhvpypnne-UElqewx1qMCHpiEiii8IJOk6CxZ_xvxjVsVeXEWLQGmYGetLyjecBcCmluXK7DeFerT2EkgCzDaE2s1_0ojs4KU8W1g-GJxkLM-zEJgNdTAYmKuMpXf2xOUjhp8Et068bT8Wy8f6ArVJbcd5sptMoEhGDKGAylTR1kGaAksr1RJUZQ_1s7DwhQ8kSppKmpUbMSOeK0ZCEmD35rYMItcS23LWtQg_et50vlXzcO3eg68y6RLQnxN2SeZ0IcO4dPW33mSBg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
کنایه‌گزارشگر به قلعه‌نویی و حسین عبدی بعد از شکست مفتضحانه مقابل کره شمالی در بازی امروز.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.9K · <a href="https://t.me/persiana_Soccer/30284" target="_blank">📅 13:36 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30283">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">🔴
🇫🇷
صحبت‌ های جالب و فان ابوطالب حسینی درباره مایکل اولیسه ستاره فرانسوی بایرن مونیخ.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.2K · <a href="https://t.me/persiana_Soccer/30283" target="_blank">📅 13:13 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30282">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/eef1cb476e.mp4?token=OeJi_QnzULbI2YYQKXl9L-YQhNYSqoOPPlVDn39mJlaMDnBgQBO3_hSBXs1l7iphkHMc-1-bIYgiECGIBweOuK_t-ZY5eGa4UPV07U2gZr_4Ys_lRjNMKX0oGrjdoqhZBYFoSJ1a6zCIgeS2Rd5ockfgrSFV1o-tMBdxl1YvD5mN1MY-6nCXvuPOOwoayAdCupl6PPFT3kMV_D9F0MBC3YdvGsm_Mp-1G-0lgySHiKP90q3V8qNYx-fbTLYGimgROr7mt3zq783fmO0z_s4aGvFgDB2GqMJhz5QNwwXOO2Ehe-lVdCqqS5yF9tqOfr8YLvGK9R5g6xRdSkK4bjDW2w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/eef1cb476e.mp4?token=OeJi_QnzULbI2YYQKXl9L-YQhNYSqoOPPlVDn39mJlaMDnBgQBO3_hSBXs1l7iphkHMc-1-bIYgiECGIBweOuK_t-ZY5eGa4UPV07U2gZr_4Ys_lRjNMKX0oGrjdoqhZBYFoSJ1a6zCIgeS2Rd5ockfgrSFV1o-tMBdxl1YvD5mN1MY-6nCXvuPOOwoayAdCupl6PPFT3kMV_D9F0MBC3YdvGsm_Mp-1G-0lgySHiKP90q3V8qNYx-fbTLYGimgROr7mt3zq783fmO0z_s4aGvFgDB2GqMJhz5QNwwXOO2Ehe-lVdCqqS5yF9tqOfr8YLvGK9R5g6xRdSkK4bjDW2w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
ایرانی بیخیال هوش مصنوعی نیست؛
این چه سمیه که از مریم‌امیرجلالی و حمیدلولایی ساختین.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.1K · <a href="https://t.me/persiana_Soccer/30282" target="_blank">📅 13:08 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30281">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/C47V9OaNAfpDwJ3wAW4DIYtaWlxwlXfXVN2VvEJt_YiTJsx_ydcf6IEEFoW4plhjXD7gz7g0xZC1HG79NL1RvcQdwtuq6z218zJPP_1TB7xLHs3M_XC2GqWAiNfiH7sIxaWhW7mylqIC513HvhbuQlcWnVsRt5HilapGmtOC0sg7mELH11-tMFKf3SXSNCnFEMFY5BhaRZJtPP4zKlzCfmGIDuaWdsmunVeh_vPscba_lluOrMxhjRCLhfS9QYTX9R13D1PkrzkCbJPea3EH24BNnPzV6yolnBQhhGppKjQAStWUAEPPf8xHsswRnEsCKjC19Z8nGGg9HZt6RGzPBQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
ترکیب‌منتخب بوکاجونیورز برای دیدار خدافظی کارلوس توز فوق ستاره آرژانتینی از دنیای فوتبال.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.8K · <a href="https://t.me/persiana_Soccer/30281" target="_blank">📅 12:58 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30280">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CDU8DyC0VN52xdClDI4-dRucwtVINMYJbOvGvjwAE1rZM1uQ11jnRJc4m6-gPWDQRKrPU-g6dSj_9_y9sEB5IWowTHh9EwDGRIb7QIHD7jrtMalfj3388Yh28sjdKZRy-x06SMnfnPMOjXDuMlf2D6rfUyBDSt4LRcH4FmbfiR8qdWgJFs-EG75R7J5fzannvoSZveJWXHcjVp4MEVAKgPKmSCq5LywfCGddFgrYfWVMtT8v_Akv55Kdc8xv-mkZb7Yq920K6y93wa3zA9rIcn0zRXG6mbt6pg0PLN3UOtCP-nEt5CDpOyZvqWdDStQCxf7hodNP2XqCMdjyFKnd6Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
کارشناس شبکه CBS ترکیه:
«رافائل لیائو فکر می‌کنه برای‌تعطیلات‌اومده ترکیه. اون به دید حقارت به‌فوتبال ما نگا میکنه انگار ۵ بار توپ طلا رو برده.»
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.4K · <a href="https://t.me/persiana_Soccer/30280" target="_blank">📅 12:30 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30279">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NyXJK18TYCNkyOJxX_SUARxfD0O1zLzeDaGHhzKvqQ4hgEJPxHz3gD7wfGh84coAjZSCvCfmU-Zl-xDjfxZgoW89s3dnsN0x3_cWBgLh3mvFPfAm7F2_QUR0CGJn3BWYUziiBlUDHRn9rDTLg4dPPnWIHLbjnGHTr8LiwO7QjP15ZoYFZv3L3OSdPp1P29rg7wuyHbLRvEt054TucEuTcHZCFt2fDj_x22GjlsqWOv9GURdShMpQW9XNAK6jFWC49Y333gn7fUf_aVzPfxIbIElkj9IQ4D7KH9UF5UO1nGz4shyTjFxfQS1oBunePNxBIWZWxR84yJprR19q2txcWA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🤩
آندریاس کریستنسن مدافع‌میانی‌بارسا به دلیل مصدومیت دربازی‌شب‌گذشته مقابل سویا، شش هفته دور از میادین‌خواهدبود و به احتمال فردا دیدار سوم آبان مقابل رئال مادرید رو از دست میده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.4K · <a href="https://t.me/persiana_Soccer/30279" target="_blank">📅 11:56 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30278">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CbizGMu8-TP8J66Yf568kk1JAJQfhSxWlJC8YASIc3kOjI01tGy7znIY7JpULSb1fIpGUi7BKFvp7qbn-NG-k3dUq71Sl8zVNvdNFsBCfT_omBnVMCpHCl1zw_-dGQVb1DXNAC9kH5GQ13NDi_m2_RhcylzgbVinxG7pRmzoYgCCgrkdgI2Ucpp1euVHYOB6GqCmk1T7EDFhcNEQbemsECZIk3MKPxx0G46SvUBdms-RJTmQagEAIcF_FAhMdtQYKZhM5iyFu6BUTC7xwW5ihIWfJyEcxHsBIqPiRaHAneeAl9G77aMRurf9nRsr5s_lQbaLo1RajBFXk9ivVkOeVg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
تیم ملی امید ایران تحت هدایت حسین عبدی مقابل کره شمالی تحقیر شد و با قرار گرفتن در رتبه سوم جدول از دوراین‌رقابت‌ها حذف شد و بازیکنان بزودی به تیم‌های باشگاهیشون باز خواهند گشت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53K · <a href="https://t.me/persiana_Soccer/30278" target="_blank">📅 11:29 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30277">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/P9yICC29VFfsRsCyK2ujg1zPclhizOVBx6kcz_TMBoWHHvNVQ0KxNlTq5uZ-7_ETc7sAawLWNxxyKrlytj55NJEf4EyGaVX3eLz-4yLHHNPUJR0j9oUaxEYd14HrcZKjzA6rhKnbDBBqppL0fLr9610kRH-4mPCaXSbzZLrdcKmMniRsT-29T-vbaRE6DaH6CkfBzVK8atyU9Bx_XapnWwrSZor6E91Fo9qUlPXmoQLcBCH0KDVQeo_GAP9tsvVQ2zH2ERnhOF4P3th28i8KDZFgmImCf1egnmIjrb4vLUGI33Sb6w6YQ61OldaPpg7OLXYIfaoit0k_3wLWms9b-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
تیم ملی امید ایران تحت هدایت حسین عبدی مقابل کره شمالی تحقیر شد و با قرار گرفتن در رتبه سوم جدول از دوراین‌رقابت‌ها حذف شد و بازیکنان بزودی به تیم‌های باشگاهیشون باز خواهند گشت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.8K · <a href="https://t.me/persiana_Soccer/30277" target="_blank">📅 10:53 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30275">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jW89XF0TzPZr7J-l6rcIiA-Z_BerLTzthsuD75JJ_QRV769MtrG2fAnAM4q24IEqwZrauW511-9jecTDIcBhF4PFZQ7c9oGId7Vatm7P0eL-4IZPqDTocxz8Fx1tZ9jtWqij3Bm4UOhvwEtYOuRAQMgPt_yikxKrFs1Wb56SmSKpaLBO4GHnn9MfapYECv-8y20-w47xnfwCRyid46lWNkTLQSfuT8jYDdz_ATXCnEMWtNCuv8VwpQ2lDj_pF4nzsQSU5RXzuPd48PaP5aFmjpLip5_-7WJCtUpJXTs-26osiRKIdlqXzm8e64_nDcix-otgvJji1NT6Kbuzg_uMow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/V8KQopt3Avc3KDBK4agiTizTmt4CjmU6qx0oTf8hGgNkPTVsnsyaN5Bd6wqUQ1bR5rDTRQuIJaaT3hOKR9ks9IUVza9ajMVUXtLyUtmr_KTMHP_edLCOIZj4A-JWrhkIqJMoD0Us5eB5PCsyPcfVRk5lff9Z1wfwXJQ8makqIqFu0fV-jxEprJsmcLyFXxixLHqqAe59yy3m6cjSKSRduzhNSp7Cl7cAqaKTgDHejur5vJwxVH1aGsula74AIFk0WfpluZRi3ZZYzkrABDKj6lsoDn0zhkqZzhUvdewBNFmXP2vAHsSvAjIsePaFkrgdulgdW9HwktFwIG51BZ2xfg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📊
فصل جدید لیگ ملت‌های اروپا با یک رقابت جذاب آغاز میشهه؛ ارلینگ هالند با نوزده گل در صدر جدول گلزنان تاریخ رقابت‌ هاست و کریس رونالدو با پانزده گل او را تعقیب می‌کنه. رونالدو برای رسیدن به صدر به دنبال هالنده؛ اما مهاجم نروژی هم فرصت داره که فاصله رو بیشتر کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.7K · <a href="https://t.me/persiana_Soccer/30275" target="_blank">📅 10:52 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30274">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GK3IAIGVnLKjdIorWp5RvZqO8Lyb6D8ncVukbswoeSIddChQszzHTMVE_e7OkKbVJ1NXjIBlSw4f70B1tr76O5EEVIV2xlreXDvxXP8tT4OEnYRrwatAUzPgXepYVSJ0hPgMlpgew06LlLYEKaMz5ImUSkCuTF8bGGo1YFr-5K93CdlZaAM8QOPKR3Ch6rdfGtU4tqWibenoFRRDU7nMnp6s5DPMmRFOLNpW1Kr5s5ED-7jlKq5kPfkMjyQ9iMd84A8BON5GntCCL-7nAPcIZCR0CxFOmARKJ8h2xkSv_r1r--wcDKc1OIfphPlpi_R-xcasxp7ckqn8ULd9y7W1yg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇵🇹
🇵🇹
تاریخ‌فراموش‌نخواهد کرد که کریس رونالدو فوق‌ستاره‌پرتغال تیم ملی کشورش رو با این اسکواد و در خاک فرانسه به قهرمانی یورو 2016 رسوند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.5K · <a href="https://t.me/persiana_Soccer/30274" target="_blank">📅 10:52 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30272">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ehJoy2GXZS_AYlbYGyuW6PkocHodoj39a3zjCyt_b6d1VVXJoqxSiMFdm1yboJ8z1xe3TjlMhp-dfdrMcMi3LStzjHhVJ3DC6ek6fYb-qLldzXnJybEv8XI07q54mcP4DERkijVcPuxlLPveNnuamaa-drb2hL2axTM-2-i1cBJMb5Pdh5mAtfeMgOBxnFtASGPZ56tcKCbRxP-3ODOkIXFU78Z16MQzAdx61witCAN7drW3oB36vdP0GXBsuwyhcOumJVThLNb_JgaNzaGl0nDy9MuVgnonb_DbIbwWp0Cz0HRKGcZPkixT_jcQcUZrbiQU6MDsiokw3DhS-QcHHA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
مثلث خط حمله بوکاجونیورز در بازی دوستانه خداحافظی کارلوس توز آرژانتینی از دنیای فوتبال.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.4K · <a href="https://t.me/persiana_Soccer/30272" target="_blank">📅 10:17 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30271">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a1f64463b5.mp4?token=cb6JD6IKooLO5Ja5ElbIbsUTpmiRH6V8GFiDvjVTRSn96WDZVIB3en9i05_RlrkowmoBwP2lodJesS2A3IXZjw8mSHMCpDqKhpXWXswYkvNLWtPGxCpxbe5wpxAf0LVcuzAScpGUtKVL5RP-WCRPNdM-ABQnPJcPK66-MTAEJ3GYnXRlesToBLPG9nHQMEc5dKFWg9Sv0A6Kq9ShI3RlCA49BYJU0ub4rOQmAtMe1WH8ZleUz_m7TibxXvX7pC2p5xiNkxm61qN4MH16WhS9g3IdUxfCe0c901EQJbrsutAtxvTIXcOyP8aiRfY2-s_r85070xyJZm9sGAlaUsE6CCho1JRi9czbrOcUWM4B2Lh8FUVhn4NUbloM29Ad9idyTfmb4eKMUHjX7rgQTPVnGsyJOTLJCjOtpz85BFiNj75Jmz_tO9dHNRm4gOnBOhzWgqFhkWScJJc7QUWS8phUvTi3Pu_jJRl3FUCfbBPozh9uoRIGJyt2BgWXpdbfwvF6Wq4QR31UarZ9uVrWXZI2vlXFTZysc_V9ACkQBcVOOI0u3Jhtn3Jo4mYmgSoWdIchwYzzyHC4IIIJ28baBSZP5Om30kAm7yllg7vDmC0XCM_Li3etvMj_WnBdSOFeizKxVbC2QDIGOyH36qWBff9eNzFhI6k2Iwhzg8GnzeT_xMs" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a1f64463b5.mp4?token=cb6JD6IKooLO5Ja5ElbIbsUTpmiRH6V8GFiDvjVTRSn96WDZVIB3en9i05_RlrkowmoBwP2lodJesS2A3IXZjw8mSHMCpDqKhpXWXswYkvNLWtPGxCpxbe5wpxAf0LVcuzAScpGUtKVL5RP-WCRPNdM-ABQnPJcPK66-MTAEJ3GYnXRlesToBLPG9nHQMEc5dKFWg9Sv0A6Kq9ShI3RlCA49BYJU0ub4rOQmAtMe1WH8ZleUz_m7TibxXvX7pC2p5xiNkxm61qN4MH16WhS9g3IdUxfCe0c901EQJbrsutAtxvTIXcOyP8aiRfY2-s_r85070xyJZm9sGAlaUsE6CCho1JRi9czbrOcUWM4B2Lh8FUVhn4NUbloM29Ad9idyTfmb4eKMUHjX7rgQTPVnGsyJOTLJCjOtpz85BFiNj75Jmz_tO9dHNRm4gOnBOhzWgqFhkWScJJc7QUWS8phUvTi3Pu_jJRl3FUCfbBPozh9uoRIGJyt2BgWXpdbfwvF6Wq4QR31UarZ9uVrWXZI2vlXFTZysc_V9ACkQBcVOOI0u3Jhtn3Jo4mYmgSoWdIchwYzzyHC4IIIJ28baBSZP5Om30kAm7yllg7vDmC0XCM_Li3etvMj_WnBdSOFeizKxVbC2QDIGOyH36qWBff9eNzFhI6k2Iwhzg8GnzeT_xMs" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
سال 2010 درچنین‌روزی؛ مایکون مدافع راست اینترمیلان این گل دیدنی رو وارد دروازه یوونتوس کرد؛ دروازه‌بان بیانکونری بوفون افسانه‌ای بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53K · <a href="https://t.me/persiana_Soccer/30271" target="_blank">📅 10:05 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30270">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dc2f2dad5c.mp4?token=Yk78XHPWIzujXVh6cBCHBvv8m45Tpvvb2j2i2-HKHN1Y1i-NEaLos-tP-1HksF1TIhJmGfMPKKqfxsn0VFvpkzEqp1jWUb45fIbrWsNo7BbP5u3aFqAnZ0sx_-8lv3I_g-XPwTYAPScIaPKObjUn0Ki6q11JjgtJYGE55geUJDPppTuP3unWVSKcnuELDnCIyQWTsmLC9r5n8KiAHsLqoRn2av4YFUEUT0rw4gz_jXXjwnNJcWSvtCFqCl_84Nz8sb0BcRD6acaI0rCZs90s-NbhiuQKieFq_aG0_FjhfKGHpfurG7L2Vssnfs2eryum0NseJZBOuupgtAkbm9qqUg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dc2f2dad5c.mp4?token=Yk78XHPWIzujXVh6cBCHBvv8m45Tpvvb2j2i2-HKHN1Y1i-NEaLos-tP-1HksF1TIhJmGfMPKKqfxsn0VFvpkzEqp1jWUb45fIbrWsNo7BbP5u3aFqAnZ0sx_-8lv3I_g-XPwTYAPScIaPKObjUn0Ki6q11JjgtJYGE55geUJDPppTuP3unWVSKcnuELDnCIyQWTsmLC9r5n8KiAHsLqoRn2av4YFUEUT0rw4gz_jXXjwnNJcWSvtCFqCl_84Nz8sb0BcRD6acaI0rCZs90s-NbhiuQKieFq_aG0_FjhfKGHpfurG7L2Vssnfs2eryum0NseJZBOuupgtAkbm9qqUg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
سال 2010 درچنین‌روزی؛
مایکون مدافع راست اینترمیلان این گل دیدنی رو وارد دروازه یوونتوس کرد؛ دروازه‌بان بیانکونری بوفون افسانه‌ای بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.7K · <a href="https://t.me/persiana_Soccer/30270" target="_blank">📅 09:51 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30269">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/204e06fbc9.mp4?token=kJHr1KmYePsSMxYnbaCREjQAMqYidK8GUg73z4XAFl4L6c9BjyKOnP5j3vzZUtkDA0JtKWkQPoaQe4JWUYy6BMihmxhGb61QKnWDNcRkRj22y9okUqk0BXniTu2N4P9pQFTxa30hMi1ApwCoPNwLQq3DXfWob4nT3F0sR46ISJdL-gwunj_EQbTvkYTMu1n19lc1GxZeAgKyfuoWLwsUlTSmKvslwwrnEu_z4QnmNysE1VWrd3Ri3qAEtqh-jNr4ThYywayDGUrWTiIJGyrrDmMlGr0Bb0YswbI3UGcS2VmTm99_KMyF_anX3y0cCh7QGudP5LYnHXqTCrXKjjTIUw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/204e06fbc9.mp4?token=kJHr1KmYePsSMxYnbaCREjQAMqYidK8GUg73z4XAFl4L6c9BjyKOnP5j3vzZUtkDA0JtKWkQPoaQe4JWUYy6BMihmxhGb61QKnWDNcRkRj22y9okUqk0BXniTu2N4P9pQFTxa30hMi1ApwCoPNwLQq3DXfWob4nT3F0sR46ISJdL-gwunj_EQbTvkYTMu1n19lc1GxZeAgKyfuoWLwsUlTSmKvslwwrnEu_z4QnmNysE1VWrd3Ri3qAEtqh-jNr4ThYywayDGUrWTiIJGyrrDmMlGr0Bb0YswbI3UGcS2VmTm99_KMyF_anX3y0cCh7QGudP5LYnHXqTCrXKjjTIUw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
تیکه‌‌های ابوطالب حسینی در قسمت اول برنامه جدیدش که هر هفته سه شنبه ها قراره پخش بشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.9K · <a href="https://t.me/persiana_Soccer/30269" target="_blank">📅 01:04 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30267">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YJfgQH3kRHTyrwAJxgfRiK1Ck-QZk2omeFQnmmpRysfGQ-GaHMi8OvIoUJUZi0acpDhJzWXWwYZ94V8OnLRJPLy11NccCDNs7Sz0qCnLUw5zHBp5balLihQKNHaF6ubfQBbWuWwh6N9ZZTx8kTUvG1NDKmqNC8lbC3EdlhwsQlX7Y4JHHh1myAEeVQgwy0eugwbLYJJro46OxoJ0lhnuhwxdSIhaf5fpIN7ki9xd3Mnx-CymMBXfXZUz9QLdkfPZ52Fn8TgLjSAxMMUyhXUNi7d5Amlp6t-ZK3a63pZvpGwarwq4N0HIR8U9f9d8ra6fFM3G-7FKrYb7BI5jG4xy9g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
تنها ‌‌‌‌‌‌‌دیدار مهم امروز
؛ بازی تیم‌های امید ایران و کره‌شمالی برای صعود به ‌عنوان صدرنشین در ناگویا
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54K · <a href="https://t.me/persiana_Soccer/30267" target="_blank">📅 01:00 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30266">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8e0067ddce.mp4?token=kjWxVeXL8Fhx05ag2UWDD5akV8ay1aouRqWRH8Hut8d_UDv1fiykj-S5FOJrOhMg_bUU9hUZUkF7aBZ53OPpXdzxpirhZ-Tqe7fuQWxAm2dQG-tuCit9vfIx5xjfZgr7pCSkTTVPnmT4F8iTxt2FMxgpFn_u7mpqU3ZJnglPGb0lZZonR51QxjTKZ08thv4cj8V0JK0p8FhI_0c3Gw9JSDxrTFoK_akwawT1OSX9VMc7PSJqSSqTVHSgpU2S3jJ_MAXOW0G07MDA2UlDTgsdVOB9DHUh3m1XWERqEqqVSDpWHF0FG5cR1Q7YH9xPzPXFYPRZ0-X9UjPPv8Ej7NBveg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8e0067ddce.mp4?token=kjWxVeXL8Fhx05ag2UWDD5akV8ay1aouRqWRH8Hut8d_UDv1fiykj-S5FOJrOhMg_bUU9hUZUkF7aBZ53OPpXdzxpirhZ-Tqe7fuQWxAm2dQG-tuCit9vfIx5xjfZgr7pCSkTTVPnmT4F8iTxt2FMxgpFn_u7mpqU3ZJnglPGb0lZZonR51QxjTKZ08thv4cj8V0JK0p8FhI_0c3Gw9JSDxrTFoK_akwawT1OSX9VMc7PSJqSSqTVHSgpU2S3jJ_MAXOW0G07MDA2UlDTgsdVOB9DHUh3m1XWERqEqqVSDpWHF0FG5cR1Q7YH9xPzPXFYPRZ0-X9UjPPv8Ej7NBveg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🟣
🇦🇷
توصیف‌های عباس قانع گزارشگر مسابقات فوتبال از لیونل مسی فوق ستاره آرژانتینی تاریخ مستطیل سبز که تنها یک بازی باقی موندهه که از دنیای مسابقات ملی برای همیشه خدافظی کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.9K · <a href="https://t.me/persiana_Soccer/30266" target="_blank">📅 01:00 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30264">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jqgiv-L1r1OnZ9mvWX1bTf8VrD6ubiTmHOoOGX_OMaqRwTPXCYy676pq4-1NXnmxeJtGlWFnU5lLNh1f5UIyU8ZEQ1vdT-HZ7z81s__WOr-nmthx78SAqPMYYSS2jYK6jQMHD9xrPDYbjddk06xYgUTqFooHvICK2on91meqm8IR76a_JBVsABc6eausKECrCVXUn8uBSJoe0svTfjR2mqRX9rAARUOz9pw_IIzRFEkvIMizhAyx7EBqjUFLJXiCHSjsDICLsvS674SBe60JV8xcMXEqF_UOExbl_tJJIYZfRY48WvTx28uekiaqSrWlmPz34bFxfKktXbklfzNMgg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
مقایسه عملکرد رافینیا و وینیسیوس جونیور در این فصل رقابت‌ ها؛ جالبه بدونید وینی سالانه 24 میلیون یورو دستمزد میگیره درحالی رافینیا در بارسا سالی 16 میلیون یورو حقوق میگیره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.7K · <a href="https://t.me/persiana_Soccer/30264" target="_blank">📅 00:32 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30263">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/896a798b5e.mp4?token=tlbAS17cx2TDW4BeXSHPATz6nH7IHnSBpeAayXH4WjH-ygrX1DoFemRhKV9Lq2Ue7Pt0MyE2aaQJ79AMc4D2xReFEnTREWy1ojdzWhiuXBaHIdilonle5kD93sI7KthKKiEUWyUiuzRtv6ysYYvdX_J_Yb_Q3nzv-s2i3t6wVhmu6Gqv8fp4vGetzmMwUcxDY0PcF-90P_OEs-M5nSPua2HvgGaUPJ4CKKgx4lw2eYhK8gfMHpyMT-HVZc72JU9YKCImNKpui4f_hq7x6tfbLIGZsBcpWuiVbNY5IEQyjHYJTEZ5mz2Vkq6ltfK0RnLWb5FJYK2G6OwSIj1UrgDLmA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/896a798b5e.mp4?token=tlbAS17cx2TDW4BeXSHPATz6nH7IHnSBpeAayXH4WjH-ygrX1DoFemRhKV9Lq2Ue7Pt0MyE2aaQJ79AMc4D2xReFEnTREWy1ojdzWhiuXBaHIdilonle5kD93sI7KthKKiEUWyUiuzRtv6ysYYvdX_J_Yb_Q3nzv-s2i3t6wVhmu6Gqv8fp4vGetzmMwUcxDY0PcF-90P_OEs-M5nSPua2HvgGaUPJ4CKKgx4lw2eYhK8gfMHpyMT-HVZc72JU9YKCImNKpui4f_hq7x6tfbLIGZsBcpWuiVbNY5IEQyjHYJTEZ5mz2Vkq6ltfK0RnLWb5FJYK2G6OwSIj1UrgDLmA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
بالاخره‌تابستون‌لعنتی با گرما مزخرفش و قطعی برق پیاپی اش تموم شد و وارد فصل دلنشین پاییز شدیم. باشد که روزگار هم روزی به کام ما بچرخد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.6K · <a href="https://t.me/persiana_Soccer/30263" target="_blank">📅 00:25 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30262">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hyj6CchMYTHZBw5rR-T-GO5qi5oyNCpuNZQjqWhgUSDVoEqwBg9Wd_0be83FoSHWnqnE88rr4dLxi3Q5W13Ni0vjONhNo1XctIy1ynHP3LSDBg65X4kJr-1O-5m-VuiqfK5jZHiAKPqJVBxIN3_T9b3KKsC1CR7UjPBo45ouhPxlfTiYrFtFWgCY3Y2Xzf0hRzz_NREOvFLKtA3ToqTAxuj3d9uFVQrQ7QeHmTYRsQLcwa98_rjKF5AKmLhi2jR8DFGmPxDBkBkRHo1TXy_BxdanwXR3YY-XgXeHjWXIwE3ii_Q1Gj57zlLslZ7jU8RxZwLmEi7u-JQtS0JxbxyD9Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
👤
شب گذشته تیم زیر 17 سال النصر در لیگ برتر عربستان با نتیجه 2 بر 1 از سد الاهلی گذشت. هر گل النصر رو پسر کریس رونالدو به ثمر رساند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.3K · <a href="https://t.me/persiana_Soccer/30262" target="_blank">📅 00:10 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30261">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YMAbp27UCEy1jlNavot-NMFKRMpOlr0rTPO63lhS6S9q0FiVp7YHWNUO4f7pW8rdqQcSEGl3nRy85GbBp-8cTgR35JvOkDH0Wc6SGQaiUZFur9Vj7pUE4KsDjm1QH4qOC8SIC7J99t47OrTQiqThANjTGMq6KFOCjEzr5vBOgIkpmgD-pbpVRFX8tlV4HK3eCZqSNliMPU5Kl2DrllpMuRWr1kZm8B8UUdbV-JRPH9r7Uxffjac65CffYv738NP0yqpdiJN9vmeLzbkFcDtb6tgOreezKLOndJUf_r1KsbNA9ZbquVYdWVhtcBaQstmf9x2jcMfAyT7k_luDBwgypQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
بااعلام کمیته داوران لالیگا؛ لی کانگ این ستاره کره‌ای اتلتیکو روی این صحنه خطا روی فده والورده کاپیتان تیم رئال‌مادرید بایستی اخراج میشد که داور جرات‌این‌کار رو در ورزشگاه متروپولیتانو نداشت. به احتمال فراوان مسابقه این بازی محروم خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.2K · <a href="https://t.me/persiana_Soccer/30261" target="_blank">📅 23:55 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30260">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TNuJPIovNTNLz5DA_5d48v3Q1Ch28O2GAy8c36Ija_pXe_eDwCJVp6zWWvW3fpZtPwtif0uOtFpTgSWwkH1gfRFAS4eQ1Ds4Sn4qEeOso7PcR3b7ymIvqWOrDc7HrKDk6bfKrK0JwxaqT9Bxcnf-xadFmDqNkTVYE_EzYEjokE8ToMyVyfctywDNCrEtH7nG5mcKzo0OhzoPpbMPMO-3UA56j_vXxstIAgZyNqrUdnHv_c9qrila3jfd98RvRpFAaIXpV2iCa14ocgUnjHqQY3t9UdjHurKrjt5GYgrAk_uaX36SDWuMZ-D_8pH9raak2YbqLmcfr5_2BK1RMoyQNQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
رقم رضایت‌نامه‌سه‌فوق‌‌ستاره‌ایرانی ماخاچ قلعه، الوحده امارات‌والنصرامارات: مهدی‌قایدی: 2 الی 2.5 میلیون‌دلار،محمدجوادحسین‌نژاد: 1 الی 1.5 میلیون دلار و محمد قربانی؛ 1.2 الی 1.8 میلیون دلار.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.6K · <a href="https://t.me/persiana_Soccer/30260" target="_blank">📅 23:40 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30259">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">‼️
چالش فوتبال دستی بین تیوی بیفوما ستاره تیم پرسپولیس با زهرا خواجوی گلر بانوان پرسپولیس.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.2K · <a href="https://t.me/persiana_Soccer/30259" target="_blank">📅 23:23 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30258">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BsVxIAp-PhjKJ28n2DDvQ9_Tf2zpvhtRxpwnP0Xqgx5JWCLTiJaLL7okvDf0IrSLikVwt3Mfb9jyrF6SceDDGwjofKIi3yLSyrmpisjZpBLq8DLpELoFK-b9ECiItqBo6BLFSfpz89ER1xVljeAx1u-pMWkrLgUMl2XtiRbkNOjR7KpHxcV3zMb98M6jJwil5mBsUrdakHkjOJdHHRTPXxX2Ykc0cP2oicdMaAlcqfWt5D6bilxNBTvOv9rUNWFdYnZNiLy5tNd8oO9bLdRcA9TtgzmVbTm1VIKPfhSrMEueH7AsPuK5SYjXSNs_7g_m7lfElxIeozzs-JU59MTE_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🔴
🔴
در جذاب ترین دیدار دوستانه امروز؛ تیم منچستریونایتدِ مدل کریک مقابل شاگردان روبن آموریم در آث میلان با نتیجه چهار بر شکست خورد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.5K · <a href="https://t.me/persiana_Soccer/30258" target="_blank">📅 22:50 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30257">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/g99etHXL5LUkNdo_DM27Bhzxo1dYAF14y9sD-LHCr-QAPSaDMJQQxfSpvkHYVMxD8zkbhsHoyKygHMVk1tcbg2-2lga6WygLvZypbepm1mzlJK4KAcqwMJj9-8rj8rU_IyrB1TPpqacww4krF63vH40gDKCuGzicP5vCHqfp9Ly5ZfxUkEJyxQrvp5Jl_K-ezm27_LoP0Eqg1eTUKYJS-Ys1gcLvreAIrPVYjdN639k3M88k3oeIIWmrDjORDxe86IJz-Ycd9kifUBLVU7oZB7ds_TCfi8DWb4UYjAPLcse0sTeqB3IjE7iJFOvnKTOZPnByzQ6Dechwm7QgWbcOww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
#تکمیلی؛ باشگاه‌ماخاچ‌قلعه‌روسیه به ایجنت‌ محمدجواد حسین‌نژاد اعلام کرده که در پنجره نقل و انتقالات ژانویه "نیم فصل" بادریافت یک میلیون دلار رضایت‌نامه حسین‌نژاد روصادر خواهند کرد. سعادتی این موضوع به مدیران استقلال و هلدینگ رسانده. حسین نژاد درپایان فصل…</div>
<div class="tg-footer">👁️ 53.9K · <a href="https://t.me/persiana_Soccer/30257" target="_blank">📅 22:33 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30256">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9eeacd25b6.mp4?token=M0l2c2PsbCIXdcSyW-TBnQzhK6jowLEjLzNi25URi_BcGzFyScJ_RlN86BUIeD8WORWbzATX5czqToY9z421NNlujlKhMY90QjURMItyG0mLReq5vMrylFftRQfrxFYX-vamvra5yz2-jNvruOYNoDJmhPmFaSzDNAyn4gXXD8T1qzI-H-nzfbObyHhG0oDadvO4y-Qzpi0GkEOR8eBSyvucIY8DWy2QhdA0qIe81Bpx90zlTjtEgxtMLHPAiZlh1DJw3BGjlVAPMnmK5CuctCHaGrS-GD2GXH2Sigl-rN_lptLprgPgrwQPEx55eBO4xF-wTXAcLE57BDRy3KM8qYj0ZmXoDfH3tyIGzqPXxkKkgLgxpPLF3-7bMig3J24D9xyvAFb973kr4bFj26v_fiudYZ0U4HUBf4DgT9V6YLLjy9R1QXz3F5JUpYeYtMzGAUvpP68J19bpDDJ-JwbDiJmDuy3YNUVOaFDAQ2Ia7P2FRWtISOmvlql2bPCDuTbjCb21C1bBo8mKDhYfS-lFy_si9bycfUSqspGwz4AuRt0lVgJOPsgX6C0AdLRA-4qR2ABEmu3g25wZP-cewCrF8Sv2J_on0ULgWw55c6YL81xaGKm9LTLzQo_GWEgPDFWRSn3gfldaGLaCyCXesbiAW9ig8kKE4_t_Lttm001zxNY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9eeacd25b6.mp4?token=M0l2c2PsbCIXdcSyW-TBnQzhK6jowLEjLzNi25URi_BcGzFyScJ_RlN86BUIeD8WORWbzATX5czqToY9z421NNlujlKhMY90QjURMItyG0mLReq5vMrylFftRQfrxFYX-vamvra5yz2-jNvruOYNoDJmhPmFaSzDNAyn4gXXD8T1qzI-H-nzfbObyHhG0oDadvO4y-Qzpi0GkEOR8eBSyvucIY8DWy2QhdA0qIe81Bpx90zlTjtEgxtMLHPAiZlh1DJw3BGjlVAPMnmK5CuctCHaGrS-GD2GXH2Sigl-rN_lptLprgPgrwQPEx55eBO4xF-wTXAcLE57BDRy3KM8qYj0ZmXoDfH3tyIGzqPXxkKkgLgxpPLF3-7bMig3J24D9xyvAFb973kr4bFj26v_fiudYZ0U4HUBf4DgT9V6YLLjy9R1QXz3F5JUpYeYtMzGAUvpP68J19bpDDJ-JwbDiJmDuy3YNUVOaFDAQ2Ia7P2FRWtISOmvlql2bPCDuTbjCb21C1bBo8mKDhYfS-lFy_si9bycfUSqspGwz4AuRt0lVgJOPsgX6C0AdLRA-4qR2ABEmu3g25wZP-cewCrF8Sv2J_on0ULgWw55c6YL81xaGKm9LTLzQo_GWEgPDFWRSn3gfldaGLaCyCXesbiAW9ig8kKE4_t_Lttm001zxNY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
#تقویم
؛ سال 2011 در چنین روزی؛
وین رونی فوق‌ستاره‌انگلیسی تیم‌ منچستریونایتد این سوپر گل دیدنی و به‌ یاد موندنی رو وارد دروازه سیتی کرد‌.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.2K · <a href="https://t.me/persiana_Soccer/30256" target="_blank">📅 22:26 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30255">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/i8QAHuZYDs-Po-v_pkb7oYro2R6U1v09KaRk07-1zO6eL93sVg8QksYluA9VENkizlL6lVVAbCBgRQ4y_XHCpH9rtLc-lcA0Cadajka8Bwyl_EvA5mqvJPZxB2z78p8t-ZdGLXnVwSjxxi8lbjS2nSp79QVeUOnJ3FdQbuhcvSRmqvCoUiZj-Pe1I6bWfA04bEiLUU5JSBzvC53V-4wYSORTB6ViyuKyIqxwyCKiBz2kSopRLwSPmrolACToubwCiRMHlHAJQJ2UVsx2f5mn9M0bS0KH1o1qgk3wzBwN6rCg3wLpJ1-wuCzlQ79BD0o7kcIXRz6K2IY1-Dh1AFm80A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇵🇹
🇵🇹
تاریخ‌فراموش‌نخواهد کرد که کریس رونالدو فوق‌ستاره‌پرتغال تیم ملی کشورش رو با این اسکواد و در خاک فرانسه به قهرمانی یورو 2016 رسوند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.9K · <a href="https://t.me/persiana_Soccer/30255" target="_blank">📅 21:55 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30254">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GxqK1BeQ0jv9RLiCGd6WBHERQtoBoZoScdRwckuy2wbx8vHaBHmYC8HP2qfsVvy0YsrnwPj8xrwI5UJrvcSeNeml3puRtdEnV8lk0TYPg_Aez0Gdrg7Dyg9VPicPehWVp8UT2BYnerAC3dFvdTx7R87BiVBGu2VYEX6UERKwl5o5UJigjOPd8lv9-2iy_XwZURJCqhtAuSemmS3O66V_yeu4ZPYea8hE5Hhg0aVYyMXmHlm8SH4fD0ftwYxtTXhQUV1-2dHhApuJhvyB_NnJt_qsKj7AeVlfRl3-QeMQQCaFRO959ky1zib_B7FO9ijgC1hQDOrvUkO0d1OPERm1-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇦🇷
دراقدامی انسان دوستانه؛
لیونل مسی 2.6 میلیون یورو برای‌کمک‌بساخت‌مرکز مراقبت و درمان کودکان مبتلا به سرطان در شهر بارسلونا اهدا کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.3K · <a href="https://t.me/persiana_Soccer/30254" target="_blank">📅 21:40 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30253">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/u61F_x8ZxFGlsmY3Rq-6f1eroYS-dEJu8-rzP0UAWNfcFh5uI40S2HZlDbvZ8dQ0ccPD3UO3tMwnurPmlQWIsBPZATbf-PWFZose5VchbO8k4GnrevHndJ1RO8IDq2EMAe9kMh739xZz2XSkDT6GmddgcWxOw9sMg-YIIUmV74IdrFVMCRLU8RIqqjyDTi65BIR8ZzLbII2V6dkKLphcrL5XNDFe4n0iwrfTHep6OFRdGe6ojG0LCeGRBGdTfgkYmWNh0iUz1TE78x9fHnElkI80R9pTH7woUCEaqjdpTeGQiq3VOuyYBqPPSFvnECUP1UInlHAdLKiQf2RtPfzSGQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇺🇾
نمایی‌واضح‌تر از خطای‌شدیدی که باعث شد فده والورده حدود یک‌ماه دور از میادین باشه. تموم کارشناسان گفتن اینجا اتلتیکو مادرید باید دهه نفره میشد اما داورمسابقه بازیکن‌حریف رو اخراج نکرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.5K · <a href="https://t.me/persiana_Soccer/30253" target="_blank">📅 21:26 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30252">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/d_xtwzKDCZ3HhfxXLX67aPHVCMCssi0gRNtcU-VkxF4rxEevSuwWijrzOhmuig4thpFkcDgIwWS3N0xggP70_PBNGkMxwB351Y_xIvMhYxpYne1S806a8Xd0-ZVqr1qWrKe-Fkxkqkf4JgsrJCDLEH7Sr_yhbNzv2IdjeKjQH_bnWsgT7a8F3xejr6Yi6iO57OhCzivyEB6tExOrHy_NeRLAROy_5wgcxqjRf1UZtYHnV2LzCHbbR3ObuwG6-1IhLF4J65sIL9-soZ8iYdB6xKP65LgJe78ptM0arsiKfzMa59g2LscUU45WZsFHDAiNiuLnFE9oIsQeElJmcjwEdw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🔴
#تکمیلی؛ خدمت سربازی فرهان جعفری 28 آذرماه به پایان میرسه و با شروع نقل و انتقالات نیم فصل از ملوان انزلی جدا خواهد شد و راهی یکی از دو باشگاه پرسپولیس یا استقلال خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55K · <a href="https://t.me/persiana_Soccer/30252" target="_blank">📅 20:45 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30251">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e95eba0c95.mp4?token=r6X6KWxn-6wApK9TQNMhKMrrgGkSlaOkw5WwZ9hsrCWgDLGctdlplz3aQYU1_k0qoIXlc0wocLNDnX30ZdUvaQ_2xhWbm-917OzAe5h4Ed8n9asIWTHYlfcbP_4hB0lSUuYCY4fYNnibTl6mSghZ_Ami9hTyeXRJhM4IJdRcReDKiRpPQ7hL7nwKlwYpFqmqz7fgC6HO9z68H_666Kflw8IL1XXyMf7zlkss9ERsYYVBX77J9ef1sMJjHIrOx850iX4tVz2auatfuyxACQocIl3Y6Ia2tZ-1iSeEV7gbD3ZCykWWxWbOg4ka6fN8ScMk5BcfCG18g0W-zrP29V4y6Y5cK0Nh_kLrnalg5nSM2_QwMSNznlNW4Fogg00dKcDjfDjrRZUs9ptpcj5hJZckIoXYldqkuzOpy-iJxTE4257ICqcOOh1moY3I2a_q92Le8NotBgQlp1pxD3YGuOt8YVH1xGd9ys-bOAy-bdtUWu37rfwy5QnWcJLY0An1Ds3kdl_ZcB5iFSNBL00FE8-aTjtyCv6u205VUONQ9Y5AQ5hZmYZHHp4qiLCIno5wN5neK-VlFrqbSpL_qdO8l0xlkwk2b-F8Qr5okLsZnR-Ul6jprPa88Wi0AD3gzvV9S-kSxuxX3-5bXG-yzqdI7zKJmq9DdIJ0pIxSsieeHQAAcRg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e95eba0c95.mp4?token=r6X6KWxn-6wApK9TQNMhKMrrgGkSlaOkw5WwZ9hsrCWgDLGctdlplz3aQYU1_k0qoIXlc0wocLNDnX30ZdUvaQ_2xhWbm-917OzAe5h4Ed8n9asIWTHYlfcbP_4hB0lSUuYCY4fYNnibTl6mSghZ_Ami9hTyeXRJhM4IJdRcReDKiRpPQ7hL7nwKlwYpFqmqz7fgC6HO9z68H_666Kflw8IL1XXyMf7zlkss9ERsYYVBX77J9ef1sMJjHIrOx850iX4tVz2auatfuyxACQocIl3Y6Ia2tZ-1iSeEV7gbD3ZCykWWxWbOg4ka6fN8ScMk5BcfCG18g0W-zrP29V4y6Y5cK0Nh_kLrnalg5nSM2_QwMSNznlNW4Fogg00dKcDjfDjrRZUs9ptpcj5hJZckIoXYldqkuzOpy-iJxTE4257ICqcOOh1moY3I2a_q92Le8NotBgQlp1pxD3YGuOt8YVH1xGd9ys-bOAy-bdtUWu37rfwy5QnWcJLY0An1Ds3kdl_ZcB5iFSNBL00FE8-aTjtyCv6u205VUONQ9Y5AQ5hZmYZHHp4qiLCIno5wN5neK-VlFrqbSpL_qdO8l0xlkwk2b-F8Qr5okLsZnR-Ul6jprPa88Wi0AD3gzvV9S-kSxuxX3-5bXG-yzqdI7zKJmq9DdIJ0pIxSsieeHQAAcRg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇸
🇦🇷
هایلایتی‌از عملکردخاطره‌انگیز و فوق العاده لیونل مسی درتقابل‌خود با منچستریونایتد و کریس رونالدو در فصل 2007/08 لیگ قهرمانان اروپا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.3K · <a href="https://t.me/persiana_Soccer/30251" target="_blank">📅 20:21 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30250">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5bea7e3926.mp4?token=aAw7wKRqDWn9K8UyQyaUR7G-yVFlwDNpIJ450-iwVntq4LWypUP7cti6pS_gcjIcnulZCuaFStI0533iH7k1bVPEPucNfKd3H5hNHk7KqwM25332TgktCcm6SNx0-nWLJLoTF-uo0aGKrzHZ2aFOlkrKe7FV4GHIiUsYV8igHIfM7KjKRgzWDyD8Ax1XZtZB-kt09CaYcmB9IoIj5474cb7NO35we9m2U2o1R1G2e4HODUP7oHOl6mHBqPAlZVhlqozHLqeUrgoe_ivCOXqQl52KtKDcp4aTzsO26YMVMs3yp0QXnY91xtuWdzHxB6MVuhlVT5nuaJ2kd1laCumQYDzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5bea7e3926.mp4?token=aAw7wKRqDWn9K8UyQyaUR7G-yVFlwDNpIJ450-iwVntq4LWypUP7cti6pS_gcjIcnulZCuaFStI0533iH7k1bVPEPucNfKd3H5hNHk7KqwM25332TgktCcm6SNx0-nWLJLoTF-uo0aGKrzHZ2aFOlkrKe7FV4GHIiUsYV8igHIfM7KjKRgzWDyD8Ax1XZtZB-kt09CaYcmB9IoIj5474cb7NO35we9m2U2o1R1G2e4HODUP7oHOl6mHBqPAlZVhlqozHLqeUrgoe_ivCOXqQl52KtKDcp4aTzsO26YMVMs3yp0QXnY91xtuWdzHxB6MVuhlVT5nuaJ2kd1laCumQYDzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
یادی‌کنیم‌از اولین‌مصاحبه‌کریس‌رونالدو 18 ساله با زبان انگلیسی بعد از پیوستن به منچستر یونایتد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54K · <a href="https://t.me/persiana_Soccer/30250" target="_blank">📅 19:57 · 31 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>

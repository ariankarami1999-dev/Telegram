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
<img src="https://cdn4.telesco.pe/file/h3vM_fUKgUKpaYxbpR4uK3RHcnHD6gfZFd0MdUIGVbVKyiPCU1QOIJlRPfwDa3Cl7pSzNGw7e4-PTuGx6moAxfaKLlhxqipOaMScn6vU6ci-B_ievdr3zyha1HTl3bVWxaEUB7Vi_Nk_2G7z4YtzgvvfDPpuOYAdio9ff4uhIxYUGszKBNcB2nDbOhNzhnzdfZCocpZCenho0Qyo6We8gONAvMo2IXwbRopfcQK7MOr1CCTLD1xAZSKwKK9wLOeo2LevY_38PzUKankYA9mZpkigkaf_MqpWTxfwT46w7HCx32jfqMA8h06ZtwTCe6xal9Qy00a5E_8ypvGCStsQzg.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 هات نیوز | HotNews</h1>
<p>@news_hut • 👥 219K عضو</p>
<a href="https://t.me/news_hut" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 بدون هیچگونه گرایش و تمایلات سیاسی، همیشه سمت حقیقت و مردم.</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-04 00:37:27</div>
<hr>

<div class="tg-post" id="msg-66789">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5fa6495873.mp4?token=V0GAlOEIq9jq-SEJiXwIGSy99YC-37u4jDgL64fTIrEOFDX8qfM04qqd-89gx7Zds6G-dacLDMqzejIiRnnvSinrm0iEOF61fbRie8h4K8Enix46xjReMGOygEQ4By5v6bgzNZSLXT08ezooJk5XI6gio6U4AhkJr6vS5MoFzHWs-wUz9hsgpJ3-I7G-QPdGWoSAjv_4oFlqAkYpeJkJkY4zyF_-yo6LIqNhnh9zD2HUUVgR60NF6ijYIQp_2LfVWrTUqYgSq4TTVBJcr2t7HjMXLc9nbqwk3Y3gQS4Hm0CVKGnjYLFWfBRtkRCKoaWLFw6HA8W7KYHGhjB_UBwGoA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5fa6495873.mp4?token=V0GAlOEIq9jq-SEJiXwIGSy99YC-37u4jDgL64fTIrEOFDX8qfM04qqd-89gx7Zds6G-dacLDMqzejIiRnnvSinrm0iEOF61fbRie8h4K8Enix46xjReMGOygEQ4By5v6bgzNZSLXT08ezooJk5XI6gio6U4AhkJr6vS5MoFzHWs-wUz9hsgpJ3-I7G-QPdGWoSAjv_4oFlqAkYpeJkJkY4zyF_-yo6LIqNhnh9zD2HUUVgR60NF6ijYIQp_2LfVWrTUqYgSq4TTVBJcr2t7HjMXLc9nbqwk3Y3gQS4Hm0CVKGnjYLFWfBRtkRCKoaWLFw6HA8W7KYHGhjB_UBwGoA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
پرچم نروژ فقط یک طرح ساده نیست
🇳🇴
...
@News_Hut</div>
<div class="tg-footer">👁️ 3.4K · <a href="https://t.me/news_hut/66789" target="_blank">📅 00:18 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66788">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a6390fb697.mp4?token=enpSl44m1ZaFIt0n5K5rEm7JQ0tWY99TNlCqghFjt1XBVmSRZWwJFkwAvFrz26_iPkwpyPqO7wl5Lkr-YdNpK9lnIBkJWAVkcsIbkm1yUtJ1-d_v31pPvGtUVd3Y8ADHIWO9ptLwrMzQnA4_9zxFNkuUruHRU5j8NwaVzW80fyAAgt-SgHIIRr5xrh9s-7TfeIdeQeepb4_Qc3AKQMpAsF8EVneApAr5jc3PjpG8KfrVEOzbo6IekGW4dXj4ttcPrLskobAO9Ut4VdCIiCGEo8h04EUwHpY8jCvrF2CdQcuXAurMH7bRhCqukoLG66H9jkV6-RkxayVM251VB-PSYB7BW4uuTsDt-KEHZrntFA7KdmRnaWsNZWGqfNeRvVJoSVxbZg0KvtWNEShbZ8uZ7xCEevT3g59ZaOxSH7tx__9nSKT-PpEQZOPTK6SgN_l3eO88zqp5fSKWiRk62KJf0k6WTbRSpkhxNZo1JNINdsgMKn92OrIn51tFzAQUPHF7QWG3HhBZLBF1dqLQsi7RKnPxrx2hnMp57_gU9Ix4yTNBg1Cwgf41BKdby3OOsgBObblxCWsNR-iGFMeW2SyzaELwsjXAhZc8vUqHGe-8p_ivZsO9SjsriHqlk66331RAk1gtYI1Tn2UU9P74D_qwo47-3xewyrhA47DqhRp4KfU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a6390fb697.mp4?token=enpSl44m1ZaFIt0n5K5rEm7JQ0tWY99TNlCqghFjt1XBVmSRZWwJFkwAvFrz26_iPkwpyPqO7wl5Lkr-YdNpK9lnIBkJWAVkcsIbkm1yUtJ1-d_v31pPvGtUVd3Y8ADHIWO9ptLwrMzQnA4_9zxFNkuUruHRU5j8NwaVzW80fyAAgt-SgHIIRr5xrh9s-7TfeIdeQeepb4_Qc3AKQMpAsF8EVneApAr5jc3PjpG8KfrVEOzbo6IekGW4dXj4ttcPrLskobAO9Ut4VdCIiCGEo8h04EUwHpY8jCvrF2CdQcuXAurMH7bRhCqukoLG66H9jkV6-RkxayVM251VB-PSYB7BW4uuTsDt-KEHZrntFA7KdmRnaWsNZWGqfNeRvVJoSVxbZg0KvtWNEShbZ8uZ7xCEevT3g59ZaOxSH7tx__9nSKT-PpEQZOPTK6SgN_l3eO88zqp5fSKWiRk62KJf0k6WTbRSpkhxNZo1JNINdsgMKn92OrIn51tFzAQUPHF7QWG3HhBZLBF1dqLQsi7RKnPxrx2hnMp57_gU9Ix4yTNBg1Cwgf41BKdby3OOsgBObblxCWsNR-iGFMeW2SyzaELwsjXAhZc8vUqHGe-8p_ivZsO9SjsriHqlk66331RAk1gtYI1Tn2UU9P74D_qwo47-3xewyrhA47DqhRp4KfU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
ویدیویی که یه عده از طرفداران حکومت با هوش مصنوعی از «مختارنامه» جدید درست کردن
🤣
🤣
@News_Hut</div>
<div class="tg-footer">👁️ 6.01K · <a href="https://t.me/news_hut/66788" target="_blank">📅 23:55 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66787">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/B7AvCv_PpXyOpZ1OhHftVcAqTR2gGUOFk5ok1UlFF_3b0woVLToo2gd6XH_CZVVh9MnxSIIqncx68J1rcLpRisTidybVj5Rb-mPeBJJzY2fVmiDhn-7OesWyecFheN5vBCTGDLye0oF_plGIU2cTIc6ZHXKtPtpB1sJTcHvnNwYIl1nzFlTaQtSOhs9HVeIu0XPLxMNcqEweInJUVj-gr1MeFY-63DWgb-pOSre0GIguPG8YSgyhnPAcf0LGcZEZlC6a1G5zd7i0mc4kTehAcr2S16i8ZP-uvkxrEwYDzigS7upM-mWGiSHSFjCNN1qJc4H1y2YQBRQv3ducR8_wzA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
سخنگوی وزارت امور خارجه:
اظهارات متناقض آمریکا درباره یادداشت تفاهم برای پایان جنگ به کاهش بی‌اعتمادی ایرانیان کمک نخواهد کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 5.96K · <a href="https://t.me/news_hut/66787" target="_blank">📅 23:53 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66786">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">شایعه شده ایلان ماسک قبل اینکه میلیاردر بشه تو فاک بت جوین داده بوده
🔥
با آنالیز حرفه ای ادمین های فاک بت ، بصورت رایگان از فوتبال دیدن پول در بیارید  با فاک بت ، حرفه ای تر شرطبندی کنید
❤️
@FutballFuckBet @FutballFuckBet @FutballFuckBet @FutballFuckBet</div>
<div class="tg-footer">👁️ 5.87K · <a href="https://t.me/news_hut/66786" target="_blank">📅 23:53 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66785">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/IRgMS3NMtSBAkJeRBFZUlzZx_IE53OIZ4cOCYWYlHpI5oNKiom6VwWr6hUrjyAme8rDOjz_hx6vyuwgy5w3pCmcxE4DTEES8zuYf9uraAy6MP_PGJ9VgxHg7sA5m9pKdbxutXQc0kvbUEjasDiu0NWC9iG8gqSBQCvC82LD89uh53X8vUP24kZkqkF1WLGG8_COdzplBGp8rbIJD8Fiko2LyRBAb3hBmEOBp6iJexwiSlFfmEI39rNbYKZwSoki_16yscuZgNUE_UP4_FenjEWSe-K4m16IMPnsu404abrNBRhMa9Mj7tFyzZc0Q3RIY25MqMgYmfbcShbE_mY8rdA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شایعه شده ایلان ماسک قبل اینکه میلیاردر بشه تو فاک بت جوین داده بوده
🔥
با آنالیز حرفه ای ادمین های فاک بت ، بصورت رایگان از فوتبال دیدن پول در بیارید
با فاک بت ، حرفه ای تر شرطبندی کنید
❤️
@FutballFuckBet
@FutballFuckBet
@FutballFuckBet
@FutballFuckBet</div>
<div class="tg-footer">👁️ 5.89K · <a href="https://t.me/news_hut/66785" target="_blank">📅 23:53 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66783">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8f56950043.mp4?token=m4xis0tNkJH4KtG6lTcVjEf5602uOUyW7GZ-WTJPyH9MgpiUFrv6_syNKnOnkh3enamdnNLd6XzMvNMR8Jkya3gPcrON6cI6Xp-b_nmsoggSqXkrzAYtkwPu943_pgLIVyE9JJrQkzpcinzqitg4TnRdncUq6o13VPSoOTRj3vxaTDyZzXuYL839GrLFQmvVPRG3bKQel4JwD6BER-az3UlcmnIzgH_y4A7AFk9RELJLf4NSu6jcwmYUMDJhPBzjf31_4iVA6Nm7w8VzxGhZvdNmMPWtBlbRJ5yG18_154SuHi81QYwlXlHp1vhcqDG1QA72rqbgOXPcdCwoJfy7dA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8f56950043.mp4?token=m4xis0tNkJH4KtG6lTcVjEf5602uOUyW7GZ-WTJPyH9MgpiUFrv6_syNKnOnkh3enamdnNLd6XzMvNMR8Jkya3gPcrON6cI6Xp-b_nmsoggSqXkrzAYtkwPu943_pgLIVyE9JJrQkzpcinzqitg4TnRdncUq6o13VPSoOTRj3vxaTDyZzXuYL839GrLFQmvVPRG3bKQel4JwD6BER-az3UlcmnIzgH_y4A7AFk9RELJLf4NSu6jcwmYUMDJhPBzjf31_4iVA6Nm7w8VzxGhZvdNmMPWtBlbRJ5yG18_154SuHi81QYwlXlHp1vhcqDG1QA72rqbgOXPcdCwoJfy7dA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">در ازای شهادت مقام معظم رهبری چی از آمریکا گرفتید؟
قالیباف:
@News_Hut</div>
<div class="tg-footer">👁️ 9.25K · <a href="https://t.me/news_hut/66783" target="_blank">📅 23:15 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66782">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/78f387d3e0.mp4?token=Pwxb3rhip5iRBX2OqYsBNyavQqLhTnNlRteSjnrxPmllCHJxbg3W568rPvhNr0jsqXkAwsMULadhHSj-rZGtkxFZj_X98PSYisDdBsPs7DYvidzg_0MZhVE0kzH7S1JAHtXjt4YX03qKDMDkwHokhd2sCyl5eUo_ejZKJewh9hT654fbiQ9OuD14H3znSuVRI7D5MTPGqNSs4TFxRM0DwSSpZ9t7yOkmUVU61nVgnatfOfgesBvM1pWLMKPD_0_hI4Lme3E-0Wx26NrrjkelWvI9wmXntDgzc4lCTni1RF4rPnm5yCIlyuKx9Q_gQvEJybwM9AnSv5KcAfSFy0wUPg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/78f387d3e0.mp4?token=Pwxb3rhip5iRBX2OqYsBNyavQqLhTnNlRteSjnrxPmllCHJxbg3W568rPvhNr0jsqXkAwsMULadhHSj-rZGtkxFZj_X98PSYisDdBsPs7DYvidzg_0MZhVE0kzH7S1JAHtXjt4YX03qKDMDkwHokhd2sCyl5eUo_ejZKJewh9hT654fbiQ9OuD14H3znSuVRI7D5MTPGqNSs4TFxRM0DwSSpZ9t7yOkmUVU61nVgnatfOfgesBvM1pWLMKPD_0_hI4Lme3E-0Wx26NrrjkelWvI9wmXntDgzc4lCTni1RF4rPnm5yCIlyuKx9Q_gQvEJybwM9AnSv5KcAfSFy0wUPg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🇺🇸
ترامپ در مورد ایران:
ایران خیلی خوب رفتار می‌کند. آنها با هر چیزی که من می‌خواهم موافقت می‌کنند و باید هم موافقت کنند.
در غیر این صورت، ما فقط برمی‌گردیم و کاری را که باید انجام دهیم، انجام می‌دهیم
@News_Hut</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/news_hut/66782" target="_blank">📅 22:53 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66781">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/98a05f2cc6.mp4?token=A2aVlhA8ss566fOqZQV6NrVdQZNcxDOsgfN7i00hs9lIZdCGKNc3ZqNbGcxu1UadwDqUioclkfY0FLXYj9G0T3CC_NA1DkAOOULpZ8mxhkP6FmlO1s1bGtc-RUIrtMbqpJGnkR-isFn5v5cr0QmOYuubJ37QLXR4zjVXTnKuUqqbipHJFcKnT67RhrQGcRGYjR0PBRCNCPr3x2_ZaIcErj5aYRPZl-kZlgYo0-Kl8zLIwEM1a1da91aTRq3UM_MwRoV_KbLKrxsuRhdg981Z3T95MYQy-piUwNOmgqz3bk0_Gle6hsddDos62fGAFXqE-hXpCvWoH_viPxwbR3rg8g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/98a05f2cc6.mp4?token=A2aVlhA8ss566fOqZQV6NrVdQZNcxDOsgfN7i00hs9lIZdCGKNc3ZqNbGcxu1UadwDqUioclkfY0FLXYj9G0T3CC_NA1DkAOOULpZ8mxhkP6FmlO1s1bGtc-RUIrtMbqpJGnkR-isFn5v5cr0QmOYuubJ37QLXR4zjVXTnKuUqqbipHJFcKnT67RhrQGcRGYjR0PBRCNCPr3x2_ZaIcErj5aYRPZl-kZlgYo0-Kl8zLIwEM1a1da91aTRq3UM_MwRoV_KbLKrxsuRhdg981Z3T95MYQy-piUwNOmgqz3bk0_Gle6hsddDos62fGAFXqE-hXpCvWoH_viPxwbR3rg8g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🇺🇸
پرزیدنت ترامپ:
«جنگ خیلی خوب پیش می‌رود. همانطور که
می‌دانید، ما با اختلاف زیادی در حال پیروزی هستیم. ایران امتیازات بسیار بزرگی می‌دهد. خواهیم دید چه اتفاقی می‌افتد، اما بسیار، بسیار، بسیار قدرتمند بوده است.»
@News_Hut</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/news_hut/66781" target="_blank">📅 22:25 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66780">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/00a25b4d46.mp4?token=bxzKzsw6Bj4ewXknONmVFsMLsP8a9jiqai2jB0hQLnz0eLWXBafN7HGbH_eijs-0qAQife1sSGTdAHU1z-a2ERdI7Qnu5SpynfjYZcHFyJliKfJZ_bEypMws-b4QQqD_55aXtylicwmZnHiOIt3X_hvctkX5RR3Yf0xztE-28XgqupHOHnG22cHfwGSLhXA8tXSVTNlYgAkSv1JdOUEfd7ODxJf0Bup_R2CahPw9q7QOlnP3CjkcnxSwyJrbOIk7SV5XZ1_58LtjdTjVgmfY5qO5u9tamK58Hn8pH-wOdZ2dXoTt1jhILPeX2NLauKpMq_eJQODh6ef5BfsyScpqVw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/00a25b4d46.mp4?token=bxzKzsw6Bj4ewXknONmVFsMLsP8a9jiqai2jB0hQLnz0eLWXBafN7HGbH_eijs-0qAQife1sSGTdAHU1z-a2ERdI7Qnu5SpynfjYZcHFyJliKfJZ_bEypMws-b4QQqD_55aXtylicwmZnHiOIt3X_hvctkX5RR3Yf0xztE-28XgqupHOHnG22cHfwGSLhXA8tXSVTNlYgAkSv1JdOUEfd7ODxJf0Bup_R2CahPw9q7QOlnP3CjkcnxSwyJrbOIk7SV5XZ1_58LtjdTjVgmfY5qO5u9tamK58Hn8pH-wOdZ2dXoTt1jhILPeX2NLauKpMq_eJQODh6ef5BfsyScpqVw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
عبدالناصر همتی:
اگه کیفیت ذرت و گندم آمریکا خوب باشه ازشون میخریم.
@News_Hut</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/news_hut/66780" target="_blank">📅 22:04 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66779">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Bf83llMcxzFzCG1JUl28AxVsqfDU6LsnH5QzxyykXH6Za9oDc7f35TmVF1dL2VDcmRg7TyTlj2b_VjROmy7_dBTiyPTHoUTUKBq7-Q_TLSDjExVKNX3uPRJfyPKZwzd5A7kud1Lo6Qj8SekGSjyNyskjlBocDL_eVBo7BTXLLAn4FPnpjLDbcgW_r9uc3m5bEUmohilHLBDTD6GgFlr-jT7aQ8xbC43cvg-nPI4Zr7iWDjlBK_DxBuMyJzArzVoQWSr0tsVZS035zYnpMPnTarzApSwunbhysEbKnspwF3ent2jrzcNIaNUAJ-5vIiUpzHpc0PYBZLXFdTFm1FLtNg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
اتاق جنگ اسرائیل به مارکو روبیو:
رژیم جمهوری اسلامی و حامیانش در عمان در تنگه هرمز هزینه دریافت میکنند.
@News_Hut</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/news_hut/66779" target="_blank">📅 20:47 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66778">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dd80a69999.mp4?token=ILYYpWdax5JWwEHwoxSlcNlrsoOWAVLPbjE2CcTM3LsAohSsor2TgxuuNFH7ywdbu3lrUzG18DG7PS_ZPN6JrrfkK5G9QboHkzZRmWb4hwKiA1NGwpCAvkCq4n7vqlOlltZdSThnP5xVXjk87_a_2xUafz-Tu_vQ9yeznyiuyADx-j5ltttMfB0T8BfP1LOQWR8tbQw2X_DjzosVxergnMg1ARG8G6N1TEvNvFW-ip_1vrD6KudExelaOl_Y3mL8K23TNKGWcmu8lNyM1qNU-D0ZlWDNZhZ_qItSNK0Jw47OPxUxbShK7pq4884wD0aDN6yDs6NlbEBfKomWEclclg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dd80a69999.mp4?token=ILYYpWdax5JWwEHwoxSlcNlrsoOWAVLPbjE2CcTM3LsAohSsor2TgxuuNFH7ywdbu3lrUzG18DG7PS_ZPN6JrrfkK5G9QboHkzZRmWb4hwKiA1NGwpCAvkCq4n7vqlOlltZdSThnP5xVXjk87_a_2xUafz-Tu_vQ9yeznyiuyADx-j5ltttMfB0T8BfP1LOQWR8tbQw2X_DjzosVxergnMg1ARG8G6N1TEvNvFW-ip_1vrD6KudExelaOl_Y3mL8K23TNKGWcmu8lNyM1qNU-D0ZlWDNZhZ_qItSNK0Jw47OPxUxbShK7pq4884wD0aDN6yDs6NlbEBfKomWEclclg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🇺🇸
مارکو روبیو:
توافقات اخیر با رژیم جمهوری اسلامی بخشی از یک روند مذاکره‌ای و یک اقدام موقت ۶۰ روزه است.واشینگتن انتظار دارد تهران به تعهداتی که در سوئیس پذیرفته پایبند بماند و در غیر این صورت، پرزیدنت ترامپ ابزارها و گزینه‌های مختلفی از جمله بازگرداندن تحریم‌ها را در اختیار خواهد داشت.این تعهدات به صورت روشن و صریح مطرح شده‌اند و ادامه مسیر مذاکرات به میزان پایبندی رژیم جمهوری اسلامی به آن‌ها بستگی دارد.
@News_Hut</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/news_hut/66778" target="_blank">📅 20:09 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66777">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0ffe99615e.mp4?token=XxKrqCvFtvcHdz5NmPtPR8KWYEQMq2jQtEqhQw67M6GsfGrHFsIlAv-9qa59n1uMeBQuw0qYAfUJUQ3JbE-j5oE7mzcI5-Q607X8r-6mx4NAveNeNHEEp8aB65QOdFHM2T3wN6L7vKEHHEavzHBVDeJAkT4ly3lRwUvV6EeYwjnDnOcAXPc1CXs3p83LoQm3AE6x-rgltr2Meoj2ha-RoBBk_UA8cxDoHuNIgBxw3qLTMHEGbYyzN8jOx8Wgs_FupEZLP3eXadH92pfWv2At9cuCpnftYVUEiojyAwq3ywNzBDASP-MNN0Z_53RFQ58A8UDZImQ4cNxc_Qk38slaTg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0ffe99615e.mp4?token=XxKrqCvFtvcHdz5NmPtPR8KWYEQMq2jQtEqhQw67M6GsfGrHFsIlAv-9qa59n1uMeBQuw0qYAfUJUQ3JbE-j5oE7mzcI5-Q607X8r-6mx4NAveNeNHEEp8aB65QOdFHM2T3wN6L7vKEHHEavzHBVDeJAkT4ly3lRwUvV6EeYwjnDnOcAXPc1CXs3p83LoQm3AE6x-rgltr2Meoj2ha-RoBBk_UA8cxDoHuNIgBxw3qLTMHEGbYyzN8jOx8Wgs_FupEZLP3eXadH92pfWv2At9cuCpnftYVUEiojyAwq3ywNzBDASP-MNN0Z_53RFQ58A8UDZImQ4cNxc_Qk38slaTg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
خبرنگار: برخی از عناصر اطلاعاتی ایالات متحده ارزیابی کرده‌اند که اسرائیل علاقه‌مند به تضعیف تفاهم‌نامه فعلی است.
🔴
روبیو: نمی‌دانم در مورد چه اطلاعاتی صحبت می‌کنید. نمی‌دانم این اطلاعات را از کجا می‌آورید.
@News_Hut</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/news_hut/66777" target="_blank">📅 20:04 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66776">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4b8948b47d.mp4?token=fsnHCGPqu-ufAhM3lAs0fAuRU390l5uGskFeMMxNXI8vuaBv5LNc77bmxIkMUCZA60qSPJpXnNimVGjqzsgEOLYa-8vVOTtlW7MoSS8O8ubWiPwGzP33b8TzYA4MER-fYaEO8pa7X_I8WeFUfT4buANHgQIRJ0pvIk7K8apo16hfeT3edZlZSo3XQ0I49wdrOBLEOiz77VGCVievlfCoPWeDv1L1nQcwFMwLnHroLrRESm3JracDWs7r5N0RL1CTgnKN4cu7E5IAuZfWaP1Z2yAq41XpDwEPYl70Xxc6J83x3GBdUlNl_9cYbLyQZIq_PXG-SyaU3OJ6NL_1wK50TQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4b8948b47d.mp4?token=fsnHCGPqu-ufAhM3lAs0fAuRU390l5uGskFeMMxNXI8vuaBv5LNc77bmxIkMUCZA60qSPJpXnNimVGjqzsgEOLYa-8vVOTtlW7MoSS8O8ubWiPwGzP33b8TzYA4MER-fYaEO8pa7X_I8WeFUfT4buANHgQIRJ0pvIk7K8apo16hfeT3edZlZSo3XQ0I49wdrOBLEOiz77VGCVievlfCoPWeDv1L1nQcwFMwLnHroLrRESm3JracDWs7r5N0RL1CTgnKN4cu7E5IAuZfWaP1Z2yAq41XpDwEPYl70Xxc6J83x3GBdUlNl_9cYbLyQZIq_PXG-SyaU3OJ6NL_1wK50TQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🇺🇸
مارکو روبیو درباره ایران:
وقتی می‌گوییم تنگه‌ها را باز کنید، منظورمان این است که تنگه‌ها را آزاد باز کنید. آنها آبراه‌های بین‌المللی هستند.
هیچ کشوری روی کره زمین از گرفتن عوارض در تنگه‌ها حمایت نمی‌کند. این اتفاق نخواهد افتاد. ترامپ این را به روشنی بیان کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/news_hut/66776" target="_blank">📅 20:00 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66775">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/50bf8d5d6b.mp4?token=Wn2vAI8zT-A4J_ecncluU4NSs5gu7FIxXkGaNv3ZXR76uOGtYzGKG5WURI_JPjvBHixl3YhqQ9O79jpt1eoKFodYWj9EAM-vX-Tge0Lg5DCQqbGaKcODic8HtxsGT4RwU_Zn4BAcBG-YpKMzxeVIKCcqOFtnLqBBrRBMYUOROhHyasOyohN6lW1WpmI84XNVZKBAtkrrbwtVgbnRaTcBunvXTRplp2Unbq2-7Vn9LdSRSs6w41DrpfPJ0TC2nxuwL2Gmw-dp1OdAd_iHDEyalZsRWXsYRrZTDDpsR14kTbfU0tdF8XlHtrwcQmQeWv48DLjmbiG_2qU_iEhUpn2hOw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/50bf8d5d6b.mp4?token=Wn2vAI8zT-A4J_ecncluU4NSs5gu7FIxXkGaNv3ZXR76uOGtYzGKG5WURI_JPjvBHixl3YhqQ9O79jpt1eoKFodYWj9EAM-vX-Tge0Lg5DCQqbGaKcODic8HtxsGT4RwU_Zn4BAcBG-YpKMzxeVIKCcqOFtnLqBBrRBMYUOROhHyasOyohN6lW1WpmI84XNVZKBAtkrrbwtVgbnRaTcBunvXTRplp2Unbq2-7Vn9LdSRSs6w41DrpfPJ0TC2nxuwL2Gmw-dp1OdAd_iHDEyalZsRWXsYRrZTDDpsR14kTbfU0tdF8XlHtrwcQmQeWv48DLjmbiG_2qU_iEhUpn2hOw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🇮🇱
نتانیاهو:
به من گفتند: «وارد رفح نشو.»
می‌دانید چرا این را گفتند؟
چون رئیس‌جمهور ایالات متحده گفته بود ارسال سلاح را متوقف خواهد کرد.
من گفتم: «احترام زیادی برای او قائلم. او در آغاز جنگ کنار ما ایستاد. اما ما چاره‌ای نداریم. وارد رفح خواهیم شد. و اگر لازم باشد، حتی با ناخن‌هایمان هم خواهیم جنگید.»
گاهی باید بدانی چگونه حتی به رئیس‌جمهور ایالات متحده هم «نه» بگویی.
@News_Hut</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/news_hut/66775" target="_blank">📅 19:11 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66774">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cf7873635e.mp4?token=LflIxP9SAN2TSeGk7J6vF0l9u_TrOKhEt8RJfIw1CMQOepXEn9Esq9zjBI7yUAgtoHJ7ls9Ne0y70HMsXQZw-on8iWDxLDDsBQpTmnKIkHrNXTlgRCTU9qYnoDb8P4fQLx9ivbDzIGYr9oS_ACXso9aM-FGvx2-rLHOLR1uNEWM2gjwOLPFwQDI6oyMtTfuukZKIgSxQGfEcTLCuspaIj-pTh6G4haRBHLi1aghpPhXCyBL00GMTJPCAK2NT3nBTtEmkPj0MLa3qBFYXEPsb8XpgGAGyB3DOstVlEaoylf2r-EvRGhS6f7W0umt8vfYlFMTy7dxfu9c-lXLefxdC9w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cf7873635e.mp4?token=LflIxP9SAN2TSeGk7J6vF0l9u_TrOKhEt8RJfIw1CMQOepXEn9Esq9zjBI7yUAgtoHJ7ls9Ne0y70HMsXQZw-on8iWDxLDDsBQpTmnKIkHrNXTlgRCTU9qYnoDb8P4fQLx9ivbDzIGYr9oS_ACXso9aM-FGvx2-rLHOLR1uNEWM2gjwOLPFwQDI6oyMtTfuukZKIgSxQGfEcTLCuspaIj-pTh6G4haRBHLi1aghpPhXCyBL00GMTJPCAK2NT3nBTtEmkPj0MLa3qBFYXEPsb8XpgGAGyB3DOstVlEaoylf2r-EvRGhS6f7W0umt8vfYlFMTy7dxfu9c-lXLefxdC9w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🇮🇱
نخست وزیر نتانیاهو:
در عملیات غرش شیران بود که من به ترامپ حمله در ایران را اطلاع دادم و هیچ اجازه  گرفتنی در کار نبود.
@News_Hut</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/news_hut/66774" target="_blank">📅 18:45 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66773">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1071e13e2a.mp4?token=Vqz7GmxMfop6bm6xnw73n3I_kfbOzAn5xD0f_707IbkwPxMIz9hWWl49MW-vUuW0cRBon3AOJzvBuzBVYnhMkw-icEg6WazeSBxabkoonexAgk1aLAeswh5BE10-0slunEQpfZe3QpafxMG5uMUpT_e5RlQ1r7bz4n2JrmOTpF3kMEVhNWpk1ZY8gvx6dRgXTHlIJ6urll-CQk1jiE-QJhwvGc5egN8VlTKYeASXrI522CJgN2B92GDGERaZbTwh6-3EA22aF0MeqrIuoQJl8sWix8clhnsSdB8kTHmb_ksaw7IHuMQ0eiL-stx9919oy8ZQJHulIoOkgTNLgf0d5w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1071e13e2a.mp4?token=Vqz7GmxMfop6bm6xnw73n3I_kfbOzAn5xD0f_707IbkwPxMIz9hWWl49MW-vUuW0cRBon3AOJzvBuzBVYnhMkw-icEg6WazeSBxabkoonexAgk1aLAeswh5BE10-0slunEQpfZe3QpafxMG5uMUpT_e5RlQ1r7bz4n2JrmOTpF3kMEVhNWpk1ZY8gvx6dRgXTHlIJ6urll-CQk1jiE-QJhwvGc5egN8VlTKYeASXrI522CJgN2B92GDGERaZbTwh6-3EA22aF0MeqrIuoQJl8sWix8clhnsSdB8kTHmb_ksaw7IHuMQ0eiL-stx9919oy8ZQJHulIoOkgTNLgf0d5w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
مارکو روبیو در کویت
@News_Hut</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/news_hut/66773" target="_blank">📅 18:43 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66772">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">1xbet_ir.apk</div>
  <div class="tg-doc-extra">53.8 MB</div>
</div>
<a href="https://t.me/news_hut/66772" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🔥
ورژن جدید اپلیکیشن وان ایکس بت بدون نیاز به فیلترشکن برای گوشی های آندروید
🎁
اپلیکیشن رو دانلود کردید موقع ثبت‌نام، کد هدیه 1x_1566529 رو وارد کن و تا
100یورو
هدیه بگیر!</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/news_hut/66772" target="_blank">📅 18:43 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66771">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/17bdf5f245.mp4?token=faMJHgXKGAIzOj1nP3DUmbjvEFKwlkhmF489_4zgeibM0bsx0GNmrQa86UkBGxNr9iQyPc8c4YznEvR0bESs2-SOGms7IWAuQtkhNGXme_BWXz9MwEhoXjIBN3IKAzHZE31WkOwJVukzPruOQwXeBlIKJrIbgfIdQjs3u0e-sdtZxOY7vl_3fnRS_BXcbb1E6hmdUIAHOQgRRz_be6SSK6T8MaAqbZkiXwDo5yXLPEEmtbHV5tVValvOHhyWqwP0FPFHG25TAmKRqvl50_Uap6O0RSiqvD5W41EAeO-id1XS-gkqsxS78PudNMmXttH0ih68LADcZEvSWOdMgv9z0q5Lgxu_M2KQMYYT0IWfABcjgdbS6iEH59hHlWz3DrRknZ07Ly_rRSUegFglCiAyueJ4plHoNBUddy1hj2HQ3MZOeGZlWysI5CjpMXkokkBp-gsJ0lm_fiwJOHVUIgQO99FnApZA6t4ULtZgzVUox9AE1BeWIgfRGbXz-yImqWVY8g93oRFUR_SA3C77m0iDDk_zEsQ_yBIg25V6y3npspGwRNYMukizgdx8gM0VkYUeo34ijLkIM2O3ktjhiWywvem5lpLSdAOeMyVHXE-wA2ttHplxwnEsCESbP1_iyIQ9tmc7PiaYMe_vNQaQkBJkHwze-iuUS5WIW45nsPwuKUY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/17bdf5f245.mp4?token=faMJHgXKGAIzOj1nP3DUmbjvEFKwlkhmF489_4zgeibM0bsx0GNmrQa86UkBGxNr9iQyPc8c4YznEvR0bESs2-SOGms7IWAuQtkhNGXme_BWXz9MwEhoXjIBN3IKAzHZE31WkOwJVukzPruOQwXeBlIKJrIbgfIdQjs3u0e-sdtZxOY7vl_3fnRS_BXcbb1E6hmdUIAHOQgRRz_be6SSK6T8MaAqbZkiXwDo5yXLPEEmtbHV5tVValvOHhyWqwP0FPFHG25TAmKRqvl50_Uap6O0RSiqvD5W41EAeO-id1XS-gkqsxS78PudNMmXttH0ih68LADcZEvSWOdMgv9z0q5Lgxu_M2KQMYYT0IWfABcjgdbS6iEH59hHlWz3DrRknZ07Ly_rRSUegFglCiAyueJ4plHoNBUddy1hj2HQ3MZOeGZlWysI5CjpMXkokkBp-gsJ0lm_fiwJOHVUIgQO99FnApZA6t4ULtZgzVUox9AE1BeWIgfRGbXz-yImqWVY8g93oRFUR_SA3C77m0iDDk_zEsQ_yBIg25V6y3npspGwRNYMukizgdx8gM0VkYUeo34ijLkIM2O3ktjhiWywvem5lpLSdAOeMyVHXE-wA2ttHplxwnEsCESbP1_iyIQ9tmc7PiaYMe_vNQaQkBJkHwze-iuUS5WIW45nsPwuKUY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
جام جهانی ۲۰۲۶ فقط یک تورنمنت نیست؛
جاییه که رویاها ساخته می‌شن، ستاره‌ها متولد می‌شن و تاریخ دوباره نوشته می‌شه…
🌍
⚽️
از نبرد غول‌های فوتبال تا شگفتی تیم‌های کوچک،
دنیا دوباره برای بزرگ‌ترین جشن فوتبال آماده می‌شه
🔥
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
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/news_hut/66771" target="_blank">📅 18:43 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66770">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/caCvNyyKFqsy76GYzl04zVFmewxcsaej-Bg7Incf45UhzepV-Riz2cAHXpQALWmg7sGeH8DnZbzztcAPlKLWEyB56RDO6uo6OndGVhpHe75kbf0aGiaGd9eLoHhIgjdy3pQZdarP8NUHydkQKqoPR_mEXkGWWG3CqJWaXmSi4Tv6umqsEqZq8JicmxTGTvJhXUAAE-FhRn4tNyE6WxljnVSDSXy0mqMN7mrZqNCqGofxzyUQAsi82iLATCZ0Z8rZfFWDL1HD4kWWQoFaMacymgJeNwiLFYbcMAao6maDcX7e-A9TzUs3701dSpir1g-hcfx74ILCr-_daOb4vc_pTg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🇺🇸
پرزیدنت
ترامپ:
ایران به آمریکا اطلاع داده که، برخلاف گزارش‌های دردسرساز رسانه‌های فیک‌نیوز، «هیچ عوارضی، هیچ هزینه بیمه‌ای و هیچ نوع هزینه دیگری از هیچ کشتی‌ای که از تنگه هرمز عبور می‌کند، توسط ایران درخواست یا دریافت نمی‌شود. اگر این خبر نادرست باشد، مذاکرات فوراً پایان پیدا می‌کند!
همچنین، آمریکا هیچ پولی به ایران نداده و هیچ بخشی از پول‌های ایران را هم آزاد نکرده است. ما بخشی از پول‌های ایران را که کاملاً تحت کنترل خودمان است، برای حمایت از کشاورزان و دامداران آمریکایی آزاد خواهیم کرد تا با آن ذرت، گندم، سویا و محصولات دیگر خریداری شود. ایران به‌شدت به مواد غذایی نیاز دارد و ما این مواد را منحصراً از آمریکا برای آن‌ها خریداری خواهیم کرد.
از توجه شما به این موضوع متشکرم!
— دونالد جی. ترامپ
@News_Hut</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/news_hut/66770" target="_blank">📅 17:52 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66769">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6cc755f3dc.mp4?token=utVNQ4sY6eiF4SWrWWcFkjjLsWXhCNtxL-qy5-O9B9V_CEFxf9o16bCo93pvR_Co96qGtLSwWw6HfkGNCVpVNuLq3ZE2N_v7Sjer_6M3imWjtFhM4r2RBYr_eO8FkNXoi2FLfq4sOTWIuhFIbMOnL8iOA5YtySUWupt7q-3zRmasziRnQq4zUDspVHy7keIsXWUh4n8Msx6u6e3sdNh5fGiTl7Yx13NbFF5akawRosds5c-OkrjeQpt2Qb7P2JqIhkgGoL-j45OajYtr6CUP1ylM6DYHJhAqbuUVSZdJ0OxqfrT3LotKVOCYOrPt3WA4o5uqTrcc1GNbP1mfcJEHFA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6cc755f3dc.mp4?token=utVNQ4sY6eiF4SWrWWcFkjjLsWXhCNtxL-qy5-O9B9V_CEFxf9o16bCo93pvR_Co96qGtLSwWw6HfkGNCVpVNuLq3ZE2N_v7Sjer_6M3imWjtFhM4r2RBYr_eO8FkNXoi2FLfq4sOTWIuhFIbMOnL8iOA5YtySUWupt7q-3zRmasziRnQq4zUDspVHy7keIsXWUh4n8Msx6u6e3sdNh5fGiTl7Yx13NbFF5akawRosds5c-OkrjeQpt2Qb7P2JqIhkgGoL-j45OajYtr6CUP1ylM6DYHJhAqbuUVSZdJ0OxqfrT3LotKVOCYOrPt3WA4o5uqTrcc1GNbP1mfcJEHFA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
اگه
فکر می‌کنید قراره چیزی کسشر تر از این امروز ببینید عرض کنم که سخت در اشتباهید. فقط کافیه موزیک ویدئو شاهکار صداوسیما برای تیم امیر قلعه‌نویی رو ببینید تا بفهمید با کیا شدم ۹۰ میلیون
😐
😐
😐
😐
علی بیرو تو دروازه یا نیازمند ، کنارش شجاع و کنعانی میشن پدافند
تنگه هرمز ما تو دستای سعیده
شوت‌های قدوس و رامین مثل خیبرشکن، مستقیم به قلب دروازه‌ی دشمن میرن
ترابی دریبل‌زنه، نعمتی هم حامیشه، مثل هایپرسونیک از لای دفاع رد میشه
یه طرف میلاد و ازون طرف جهانبخش، پهباد شاهد رو روی دروازه میکنن پخش
حاج صفی ، حردانی و یوسفی مثل شیرن
توپ‌های علی علیپور از پاتریوت هم در میرن...
@News_Hut</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/news_hut/66769" target="_blank">📅 17:43 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66768">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8f90bbfd79.mp4?token=fQ1iwztyKWkzZoNox81DEwlIgJaY8aUZtfGxrR_Ul_BkEzLC5HNqb2dnwAPpWxPxyc-dnjUIJkQoEng7D_xnBrSSGItZR2s_eCg_G27JY6Qcdno2RglY0iZJQwpuW3GHJpfX5AJ6lYlWCDN9Ih1zgFY7U3k6eU7ea1ag96YGf6VucjRLgTvbeXdScQ5zlGepl52tIYyyiE7YP6WHF3bEonapHnUlh6iedNXGNoNhptM4_FtD7kFZ9VfZoVqJVTnAfoL9JYZB_ELiIXrRMih6KAWA9XwDU52vV1SvxIE6iivaVIrmYiM6TYa6YsyPimZeWjO6Nw_O66bvy34ssV0TVoNUstuInkQlo5YrzNUncCd_qHSjnLLQP8zM563lpR1K4UnbBkEbOfBI9-OV2ZCT6Fjng85veu60KLmcfp2DNGUV2rhXXZfWVFu5UgUwbBpoXxqHFq6eTCgwMyJyIPj25sMaF3fn3jEXniUyvF0nr8sAU1SLBdbi5r4z_j0r904yUdr5zgghZ14IkXJox4y6MTGMfd0japz5FWY-X_Da9ZPv6Yrvimj99C0j_xTu2CcBJRPvjw-D-TsUoUvCHl3eocefYgyorBvJOuh8VwinQq1Aq-hgN4TF823v3EylL8kQ2zG4IXTsKotFMGLQTpUAqvlja6uCkmKP3EBIXf5d2ww" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8f90bbfd79.mp4?token=fQ1iwztyKWkzZoNox81DEwlIgJaY8aUZtfGxrR_Ul_BkEzLC5HNqb2dnwAPpWxPxyc-dnjUIJkQoEng7D_xnBrSSGItZR2s_eCg_G27JY6Qcdno2RglY0iZJQwpuW3GHJpfX5AJ6lYlWCDN9Ih1zgFY7U3k6eU7ea1ag96YGf6VucjRLgTvbeXdScQ5zlGepl52tIYyyiE7YP6WHF3bEonapHnUlh6iedNXGNoNhptM4_FtD7kFZ9VfZoVqJVTnAfoL9JYZB_ELiIXrRMih6KAWA9XwDU52vV1SvxIE6iivaVIrmYiM6TYa6YsyPimZeWjO6Nw_O66bvy34ssV0TVoNUstuInkQlo5YrzNUncCd_qHSjnLLQP8zM563lpR1K4UnbBkEbOfBI9-OV2ZCT6Fjng85veu60KLmcfp2DNGUV2rhXXZfWVFu5UgUwbBpoXxqHFq6eTCgwMyJyIPj25sMaF3fn3jEXniUyvF0nr8sAU1SLBdbi5r4z_j0r904yUdr5zgghZ14IkXJox4y6MTGMfd0japz5FWY-X_Da9ZPv6Yrvimj99C0j_xTu2CcBJRPvjw-D-TsUoUvCHl3eocefYgyorBvJOuh8VwinQq1Aq-hgN4TF823v3EylL8kQ2zG4IXTsKotFMGLQTpUAqvlja6uCkmKP3EBIXf5d2ww" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
‼️
⚠️
پشمام اینو داشته باشید. تو عراق از معاون وزیر نفت سابق این کشور حدود ۸۵ میلیون دلار اسکناس نقد از زیر زمین کشف کردن که دفن شده بوده!! فساد سیستماتیک تو کشورهای اسلامی ماشالا خوب رونق داره
@News_Hut</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/news_hut/66768" target="_blank">📅 17:14 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66765">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2c68737622.mp4?token=io1bu-xR-vR69_ij_TpOB6aWN2dnKgBW4i1SO27ArLLRvoH8kuXyDclIUWFwEFGHQq71kV-6WzBJxCanuIQ1BpeoDK5GhfXet0m5xenHxLCNluxm4HMyo-s_LpSVit3hFH7wmBgbMs_o3iF1XBnuDo2OzYz1kHrtRLQ8OAYvuXN1aMTm4Wku6ZiEvykdPDAAUMXYoc4-BMn5issHoBPa0gEoPc2LUllLb33tSNkmKaf-8ytx30xpuPQn0agx_ZbuVEU-Jq_Du9JLBK_5esqHdrLTc_qrUErjxJfIszaiiuX0t9zf6sSCN4NVQ2hWE-bRk0Lyy5JsI1XAwdGWXn05LQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2c68737622.mp4?token=io1bu-xR-vR69_ij_TpOB6aWN2dnKgBW4i1SO27ArLLRvoH8kuXyDclIUWFwEFGHQq71kV-6WzBJxCanuIQ1BpeoDK5GhfXet0m5xenHxLCNluxm4HMyo-s_LpSVit3hFH7wmBgbMs_o3iF1XBnuDo2OzYz1kHrtRLQ8OAYvuXN1aMTm4Wku6ZiEvykdPDAAUMXYoc4-BMn5issHoBPa0gEoPc2LUllLb33tSNkmKaf-8ytx30xpuPQn0agx_ZbuVEU-Jq_Du9JLBK_5esqHdrLTc_qrUErjxJfIszaiiuX0t9zf6sSCN4NVQ2hWE-bRk0Lyy5JsI1XAwdGWXn05LQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
‼️
⚠️
ویدیوهایی که خیلی از دیروز  وایرال شده از کربلا؛
دیروز کاروان شیعه اسماعیلیه که تا امام ششم امام صادق رو قبول دارن، واسه زیارت به کربلا رفته بودن.
از اون طرف کاروان ایرانی ها هرجا اینارو میدیدن واکنش نشون میدادن..
تو یسری جاها هم نزدیک بود دعوا فیزیکی بشه که پلیسِ عراق اجازه نداد...
@News_Hut</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/news_hut/66765" target="_blank">📅 16:47 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66764">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dbff1343a7.mp4?token=MqH8d-7tv6easOV-eHfl9ljVqsX9htBQAhDAGYjSwrX2RlZxNq4FQkPaZOP9oSty5CPoWvoxuRX4oZSj_cS0HB3GV-2oYMJyvsdVGCuRCL8o8NZjZjb9l7a-OfcNKjzhdzy3bTR5Iu41S89YoThuFW9g3Cl0-YrymQB6b4emc0GFtXKJuGb66M0GMQw8si0K4l-OYSHkYTSLw3VveJCxwLMkzJ_WvlBqBId45hCxccPQrm4sJIlT6HHL_G2SA_PcKz6WTKJ49bHNzsVPqyG4Gi6Fp5m1wdd4KZIS-WkdcACZToU4FEMhVbYDJ6pGkTtyBCYlRd_O4AzU17-rdTyDhw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dbff1343a7.mp4?token=MqH8d-7tv6easOV-eHfl9ljVqsX9htBQAhDAGYjSwrX2RlZxNq4FQkPaZOP9oSty5CPoWvoxuRX4oZSj_cS0HB3GV-2oYMJyvsdVGCuRCL8o8NZjZjb9l7a-OfcNKjzhdzy3bTR5Iu41S89YoThuFW9g3Cl0-YrymQB6b4emc0GFtXKJuGb66M0GMQw8si0K4l-OYSHkYTSLw3VveJCxwLMkzJ_WvlBqBId45hCxccPQrm4sJIlT6HHL_G2SA_PcKz6WTKJ49bHNzsVPqyG4Gi6Fp5m1wdd4KZIS-WkdcACZToU4FEMhVbYDJ6pGkTtyBCYlRd_O4AzU17-rdTyDhw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
مترجم: «ما هرگز در مورد توانایی‌ها و تجهیزات هسته‌ای خودمون توافق نمی‌کنیم.»
پزشکیان: نه!! موشکی! موشکی را گفتم…!
مترجم: ببخشید موشکی.
😂
@News_Hut</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/news_hut/66764" target="_blank">📅 16:25 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66763">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn5.telesco.pe/file/d59ef82aac.mp4?token=c7sCowRcMexMYFRQMA9VOTvqyrNBvs817Tui2mzDrvx6LEbhlzlki3ODGlMPYieMyie-9qkNJJ_t9HwZnY7yaGPLxKzOAmBlsFA4vBHWs1JVgt1fpPZ46RZdQKINAY79vmU2dl6j8pfXLL8Ku8h7lxmU2GhzdnM_Jm5qvNESBDmpgcTG1wT8jYdjc05zg-8T_5To-JLgDYtsVzVaZqxOdTdPKSsDY_gmDvj4KxbLrUZZ5dCvz7ONqN-0uPtuztYdS7P0SRJUMN_QTsdzk0INlbsL1Tm1i0p-mNGQPSR0LlbIj5H_bjwXY0hGG3q84lGacq1HmH4sJWtfTfBWb9TbZQ" type="video/mp4">
</video>
<br>
<a href="https://cdn5.telesco.pe/file/d59ef82aac.mp4?token=c7sCowRcMexMYFRQMA9VOTvqyrNBvs817Tui2mzDrvx6LEbhlzlki3ODGlMPYieMyie-9qkNJJ_t9HwZnY7yaGPLxKzOAmBlsFA4vBHWs1JVgt1fpPZ46RZdQKINAY79vmU2dl6j8pfXLL8Ku8h7lxmU2GhzdnM_Jm5qvNESBDmpgcTG1wT8jYdjc05zg-8T_5To-JLgDYtsVzVaZqxOdTdPKSsDY_gmDvj4KxbLrUZZ5dCvz7ONqN-0uPtuztYdS7P0SRJUMN_QTsdzk0INlbsL1Tm1i0p-mNGQPSR0LlbIj5H_bjwXY0hGG3q84lGacq1HmH4sJWtfTfBWb9TbZQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
⚠️
مراد ویسی: با توجه به تضمین آمریکا، که گفته در جریان مذاکرات ۶۰ روزه مقامات رو ترور نمیکنیم، احتمالا تا ده روز آینده از مجتبی رونمایی بشه.
مجتبی قراره احتمال زیاد تو مراسم تشییع باباش شرکت کنه. اگرم پیداش نشد، یه جای کار میلنگه و مجتبی حالا حالاها پیداش نمیشه.
@News_Hut</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/news_hut/66763" target="_blank">📅 15:55 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66762">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e65be3ab63.mp4?token=To4u-jvVDYHzQoDDnANU81aIzh20obBBZHnyLhK-WdM-wXP1FnuYEt-3cMY-AOUWQDOiebtg4kY9ErIcXAOeqLe91ywSzqoYXloTNlMk0rnWP_hOpy8E0FRR48OwpLhOnzPUM5GbNwouLsr9K8pKzWzm9fKVSPgCkN_Kxnkygyhya7c5t1mQluriZZ0JZiw6z5VHPVY3Y2wbpC5kr8RJ7vWpSN9DlkWp4dlZ8Tq5D9i-QpfFMqZGY91YhZsGpXDOcxtoA2eYypLAmpSOZXzQr08GNI0Un6blElmK3oTQSxL9i6gxENWgMek4HGBWqkEJUkBAnFRJ3uU83YboV37qkA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e65be3ab63.mp4?token=To4u-jvVDYHzQoDDnANU81aIzh20obBBZHnyLhK-WdM-wXP1FnuYEt-3cMY-AOUWQDOiebtg4kY9ErIcXAOeqLe91ywSzqoYXloTNlMk0rnWP_hOpy8E0FRR48OwpLhOnzPUM5GbNwouLsr9K8pKzWzm9fKVSPgCkN_Kxnkygyhya7c5t1mQluriZZ0JZiw6z5VHPVY3Y2wbpC5kr8RJ7vWpSN9DlkWp4dlZ8Tq5D9i-QpfFMqZGY91YhZsGpXDOcxtoA2eYypLAmpSOZXzQr08GNI0Un6blElmK3oTQSxL9i6gxENWgMek4HGBWqkEJUkBAnFRJ3uU83YboV37qkA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
مجری شبکه دو:
کاش قبل از جلسه تفاهم نامه یه سر گلزار شهدای میناب میرفتید.
اگه محصول آمریکایی کیفیتش خوب باشه میخریم یعنی چی؟! یه کم بهتون بربخوره
@News_Hut</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/news_hut/66762" target="_blank">📅 15:33 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66761">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/do2hMvulqIdUaDQY9EXOPIqMEvqmk_yHohOAjHYmeYR2lxk7NU-QWWJtMKK4wrHR7r-9ooiehceB3NlTsvsdvjjqtDZk0o54OdbtK0j3s3BkxevdnWnYB8khkMjWpv66P_3Eq1jr6mscPdTTdnthScLZ5qf2R1gm91UJ5GNRKBAY7WrFbVqaMu3BdEsSX2eAgOKktEWYuzvAbuxAKLg7v1ZS9ZjZ9pA3pwASsoHMsPpqsVyvdx0DZ3A4Zrsoelrww8xzBzzUxE_YH2RxvUs429vPp4OTGkUH7j8qmjdTSYUmWSGzRXuYexV3j_uKKi9VUGTVpNcPoVxIH3xMLe0rnw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خاله دنیا جهانبخت پاشده رفته کربلا عرض ارادت به امام سوم شیعیان
😐
😐
@News_Hut</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/news_hut/66761" target="_blank">📅 14:35 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66760">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bcTN8lp9HAn4rgKtG_kdqimJETHVUzWGje00fVLmwunaek8yMPZinYpqBlzqydPJqXJ9uc3KZP5GihvyAlCLZF2nl6iV5YZ_mNm7nIkLHyRdePfXA0S7A6K5lC08Xk0klgwTl8AA03b6HJGbFKgUuQODcicrepMmsmBLhlMAT-vdBHzXspnKGJaNi2bp03oy7N4a1UQ8aUYV6Qg9o8q0pnyBysP4YLj4fbtLEXPB-CWtH-3FaRgEPQ021T_eMdO3d64WitWuVmqHLF7SYVLxTZ1pxwmZERY1Y_P0J_DEFd_BhE2IVIP63sT519-a2xPnTm3goNRmUD_eWOBZ-g9iyQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
مرندی:
ایران در آینده‌ی قابل پیش‌بینی به آژانس بین‌المللی انرژی اتمی اجازه‌ی دسترسی به سایت‌های هسته‌ای مورد نظر خود را نخواهد داد. چنین بازدیدهایی مشروط به پیشرفت قابل توجه در مذاکرات است. تبلیغات و تاکتیک‌های فشار بر محاسبات ایران تأثیری نخواهد گذاشت.
@News_Hut</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/news_hut/66760" target="_blank">📅 14:32 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66759">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3f6644dcda.mp4?token=accH_xErJr1oezP-sKHkfgdZr4SrBnkvBy2JTMalEuvP4aSYAZcrL7F4jUVVD5XlIGego3PqSpa6Ga-4Oi9rtw2THbxaXK70abbWnxeitftisQ4zUWOLi7EAMXQZFSD7B6wTHc_1pkqO1m6Luj7zqC7evg7aBw0gO2jjw4xjaMf_4EO8TAx-oLOFjyaQQnU6OsKj_rVdkHaqMtVWnQ16fi62tjdvjsi5fFf4CzR7yzk9sLpYVo4N2rSUqfX0eDtzHfMyZJqqkzVCHrcc7Q1x32qj4YZ2MRI_4OtDslNtmK4SZ9NAx_Z_Tr1dVW7VSZyABqSlXPA3anSYRxm1nEdakQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3f6644dcda.mp4?token=accH_xErJr1oezP-sKHkfgdZr4SrBnkvBy2JTMalEuvP4aSYAZcrL7F4jUVVD5XlIGego3PqSpa6Ga-4Oi9rtw2THbxaXK70abbWnxeitftisQ4zUWOLi7EAMXQZFSD7B6wTHc_1pkqO1m6Luj7zqC7evg7aBw0gO2jjw4xjaMf_4EO8TAx-oLOFjyaQQnU6OsKj_rVdkHaqMtVWnQ16fi62tjdvjsi5fFf4CzR7yzk9sLpYVo4N2rSUqfX0eDtzHfMyZJqqkzVCHrcc7Q1x32qj4YZ2MRI_4OtDslNtmK4SZ9NAx_Z_Tr1dVW7VSZyABqSlXPA3anSYRxm1nEdakQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
قالیباف:
یادداشت تفاهم اسلام آباد به اعلام شکست آمریکا تبدیل شد.
@News_Hut</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/news_hut/66759" target="_blank">📅 14:08 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66758">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fn-x7ttPWc_9zpRzCeH1oxNGFxad5rfy02hrc284azN-7SblDg0agTWBm9k9jns41yhlM1erbER8NWCLsNk5s3zGluQNJKbhQ9lYdTElJiT5YQkrJH_x6VpBlq7e-uBTUSJi5ymGk0LcVBM_daBQHQUioALnUjQvXvM8ivGsRkcxo_k0guNhjphZa_iNoU3EfM-LAqDv-TlxAZKfjPI8F2yEsMSRod4SSxWfQEHjEgzq1uvvzwkcPU2ZU1FuYwuHcUrXClE277uyw78451gjtpKDNxA-QwqT7LiXwBlcSBE15YV_00F6DcL-ZJOJZ-Bxs4jcFlcAOUlJm_egl8XyIQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
قیمت فست فود برای دو نفر، قیمت سال ۹۶ !
@News_Hut</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/news_hut/66758" target="_blank">📅 13:28 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66757">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/768fbbdd1e.mp4?token=BflolI967nIQzh_rIdc1T9NSeTeAkRqNdfuopfLs4Id7tlsKomDEcKDTc4LDFK_0Pxn8s4MXwoD2vgYzV_MIMg10YAiuHXkNYJbqASSkr1V6o3sA7Iq_m-YnHJ_6hcqLG7cEV1HblggCG54WecF8bC9rfW5p27dV3RC0g7JINGVWa-ll9SHt3_irK9fZ6yTVetnttgTD3XLDfwvl-W-3i3NbE5ZvJcMhbd7IXBFa909QusL8qVRJTbc_n1gzznDclid4HHZssEk6qCHVl2B2ljDOV5aUxqGshdbyDnA7ST0xODEcWnkKPfwgSXAsby8aOFidrGHzPtn5rhTb_Pj4Pg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/768fbbdd1e.mp4?token=BflolI967nIQzh_rIdc1T9NSeTeAkRqNdfuopfLs4Id7tlsKomDEcKDTc4LDFK_0Pxn8s4MXwoD2vgYzV_MIMg10YAiuHXkNYJbqASSkr1V6o3sA7Iq_m-YnHJ_6hcqLG7cEV1HblggCG54WecF8bC9rfW5p27dV3RC0g7JINGVWa-ll9SHt3_irK9fZ6yTVetnttgTD3XLDfwvl-W-3i3NbE5ZvJcMhbd7IXBFa909QusL8qVRJTbc_n1gzznDclid4HHZssEk6qCHVl2B2ljDOV5aUxqGshdbyDnA7ST0xODEcWnkKPfwgSXAsby8aOFidrGHzPtn5rhTb_Pj4Pg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🤯
بلندترین پل جهان که به یک آبشار عظیم تبدیل شده است؛ شاهکار تازه مهندسی چین
تصور کنید روی پلی ایستاده باشید که صدها متر بالاتر از کف دره قرار دارد و در کنار آن، دیواری عظیم از آب از دل کوه به پایین سرازیر می‌شود. این دقیقاً تصویری است که این روزها از پل «هوآجیانگ» در چین توجه کاربران شبکه‌های اجتماعی را به خود جلب کرده است.
@News_Hut</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/news_hut/66757" target="_blank">📅 12:31 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66756">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/76a52e8497.mp4?token=cHQw80rxd1LdbuYfApsV7rQPle6d9cI5quEoBlmMTTUeoo7fP6IZkZVfu1lfzUWr3gqeCNNkrFj8epkJVx_apjxw7Sad-Rmz2qF90RKh-e02IMO-_K8F9zZZWqgfhTG-1hLGX9yQZAgtP_9V4xsVATvB4csCdw1bF8XbjZ_388nowcDyDOvyFJiXWQKXirIuvtnDtsr5wyyHJFsNnEz7NwwimTSbk2qDNM6PZW6q_UWmODZhtzRjM7vSxpkFmzx_JXmHaYaLm-WwWMjSAFYicRdZJtOQuXX_7bYalAUrWpzapB91FxLHDwo8FaqV1YPDadd661HrDZPTNU7dzGEo0g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/76a52e8497.mp4?token=cHQw80rxd1LdbuYfApsV7rQPle6d9cI5quEoBlmMTTUeoo7fP6IZkZVfu1lfzUWr3gqeCNNkrFj8epkJVx_apjxw7Sad-Rmz2qF90RKh-e02IMO-_K8F9zZZWqgfhTG-1hLGX9yQZAgtP_9V4xsVATvB4csCdw1bF8XbjZ_388nowcDyDOvyFJiXWQKXirIuvtnDtsr5wyyHJFsNnEz7NwwimTSbk2qDNM6PZW6q_UWmODZhtzRjM7vSxpkFmzx_JXmHaYaLm-WwWMjSAFYicRdZJtOQuXX_7bYalAUrWpzapB91FxLHDwo8FaqV1YPDadd661HrDZPTNU7dzGEo0g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
یه سرباز روسی که با پهپاد اوکراینی روبه‌رو شده بود، از اپراتور درخواست کرد که اول دوست کنارش رو بزنه تا بتونه سیگارشو قبل مرگ تموم کنه
اپراتور پهپاد درخواستش رو قبول میکنه، اول سرباز دیگه رو میزنه و بعد سربازی که درخواست کرده بود رو میزنه.
@News_Hut</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/news_hut/66756" target="_blank">📅 12:04 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66755">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fd2607379b.mp4?token=E9IuapouxA0JTYPsz15wEvyKLvDVZKQOtIipiqRzibgOiSrcbHt47VPeW3CW-c1yOk2BKuKlLMQ9bmAFEbgFid2cl-FbEWQuQye3WbJ9mdtAGBD5fvQeDT7-z3WAfbSqJtNeZQKcIuxt9ZcfFkqn9AMx4kDLPss71XSY5i5wF-LG_p-jhypayhCmNQPS7sLCcABKmASeEc7ou-3tIH376ttnjm67GAAM9waGNZ82WJn5lAiU8QGJYieGZDVdBoB9KgcMbPVGNBbpzP4Occ47FtPSSRHRJNcBg7KWmfdOpqoHqQsTUvUEhjxhna8GNvzXLAHb6iscXUbfshQHE4b7Eg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fd2607379b.mp4?token=E9IuapouxA0JTYPsz15wEvyKLvDVZKQOtIipiqRzibgOiSrcbHt47VPeW3CW-c1yOk2BKuKlLMQ9bmAFEbgFid2cl-FbEWQuQye3WbJ9mdtAGBD5fvQeDT7-z3WAfbSqJtNeZQKcIuxt9ZcfFkqn9AMx4kDLPss71XSY5i5wF-LG_p-jhypayhCmNQPS7sLCcABKmASeEc7ou-3tIH376ttnjm67GAAM9waGNZ82WJn5lAiU8QGJYieGZDVdBoB9KgcMbPVGNBbpzP4Occ47FtPSSRHRJNcBg7KWmfdOpqoHqQsTUvUEhjxhna8GNvzXLAHb6iscXUbfshQHE4b7Eg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
😐
دیروز تو دولت اسلامی عراق یه مسئول دولتی حوصلش سر میره و اینجوری با منشی‌ش کارای ناخوشایند اسلام از جمله
لب گرفتن و ساک‌زدن
رو انجام میدن. میگن که این یارو اخراج و بازداشت شده
😂
😂
@News_Hut</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/news_hut/66755" target="_blank">📅 11:35 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66754">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b320081976.mp4?token=fRKENXmgk54rUn1F9qcWTbDZF5IvArXEsRfd7X4xAGM_Prsdqy9Inuc6AF4J5NnXbcrvv0dwOUo35VkX0wcbyuO5w18sO4GRWy4rl4ACGsPSgqzT1G_Q--TSyRwmeYlL8Sq_2MF1kv5G_KYmN-h-tFZ4JuH0xEreBMQLOqWZNWQdzlQJd_Y4MxIa4GUsy--RcMh7TGp2wEh0oR7fqinDclV0Iy-J6Cc9sxJfCjNxVm26pFpG0-7_9uGvnaKgpKy3EmsL6xFmXRGNfYvt5TvjPVNvywXiIEAtMRiT35CyQompUL28tVAp2cEfxQbUT7g2uATnBuE-_QDwOGfyIopDkA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b320081976.mp4?token=fRKENXmgk54rUn1F9qcWTbDZF5IvArXEsRfd7X4xAGM_Prsdqy9Inuc6AF4J5NnXbcrvv0dwOUo35VkX0wcbyuO5w18sO4GRWy4rl4ACGsPSgqzT1G_Q--TSyRwmeYlL8Sq_2MF1kv5G_KYmN-h-tFZ4JuH0xEreBMQLOqWZNWQdzlQJd_Y4MxIa4GUsy--RcMh7TGp2wEh0oR7fqinDclV0Iy-J6Cc9sxJfCjNxVm26pFpG0-7_9uGvnaKgpKy3EmsL6xFmXRGNfYvt5TvjPVNvywXiIEAtMRiT35CyQompUL28tVAp2cEfxQbUT7g2uATnBuE-_QDwOGfyIopDkA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">لحظه ای که مسعود توی مراسم کاشت نهال در پاکستان بیل رو ول نمیداد
@News_Hut</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/news_hut/66754" target="_blank">📅 11:04 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66753">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/44438818f9.mp4?token=V8OFxeh42cQhjainkNwMnyd2-Qx8NcBeBmk22MrQ_rXAUAFvgbcyTHOVRJiVA-UNs4f-b7IX72tmjljIm6yMk0Dk-irARmoEpIPqNQuz10qrPrlMuOdMAYZmxmw-RHxaYhFRfvqmOvRopzIIzOw6uCM-5UHxHtOGW4wPCy-rT8sUVrF9S9vqEeAfTLr88yoAHpXm_gGEV0qVJoydCGhxiYkrd9hzrELWbwYnDwSe5VMQ10D4oQb4eZ1-u4xbVwwkmuula7znGfzV_ExfFAauVjMr3VCGPbT8xud9QbHDVUmX7ZJ5BMxnO7-X0hQF_z0AUaHifUmVU53SPiKoVROEO76NLfrU-pSzrOY2Z3DLXxkpDksBjcLzDoeVga4_HC52qnfnsEn4b5PLCnOXwXeTJ85PuFZsNm2SNbFlmhAcUNT6kN4J7n6DCuPme8qopM5NYkuuBcRZKKOIxxjMS-_ODG2I13WXt038iEiAbMTY2o3hNzciWTGatygejWs3-p5JEYKmowYGw5a0jwLBbDJbY4ck9_waLXiWJf2DCFGmqVyJYS0iTW6boZ7IleO4ke433_4QwrLNEU8CPYjpoeVdoO14rhDS_zUJvpEiyy8fGVSKJ8gG1fWyQM1rTnpAuAu7lVgUWerY9zAZ51g44yZ0EPiSQveV56tS753mf_w8CaM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/44438818f9.mp4?token=V8OFxeh42cQhjainkNwMnyd2-Qx8NcBeBmk22MrQ_rXAUAFvgbcyTHOVRJiVA-UNs4f-b7IX72tmjljIm6yMk0Dk-irARmoEpIPqNQuz10qrPrlMuOdMAYZmxmw-RHxaYhFRfvqmOvRopzIIzOw6uCM-5UHxHtOGW4wPCy-rT8sUVrF9S9vqEeAfTLr88yoAHpXm_gGEV0qVJoydCGhxiYkrd9hzrELWbwYnDwSe5VMQ10D4oQb4eZ1-u4xbVwwkmuula7znGfzV_ExfFAauVjMr3VCGPbT8xud9QbHDVUmX7ZJ5BMxnO7-X0hQF_z0AUaHifUmVU53SPiKoVROEO76NLfrU-pSzrOY2Z3DLXxkpDksBjcLzDoeVga4_HC52qnfnsEn4b5PLCnOXwXeTJ85PuFZsNm2SNbFlmhAcUNT6kN4J7n6DCuPme8qopM5NYkuuBcRZKKOIxxjMS-_ODG2I13WXt038iEiAbMTY2o3hNzciWTGatygejWs3-p5JEYKmowYGw5a0jwLBbDJbY4ck9_waLXiWJf2DCFGmqVyJYS0iTW6boZ7IleO4ke433_4QwrLNEU8CPYjpoeVdoO14rhDS_zUJvpEiyy8fGVSKJ8gG1fWyQM1rTnpAuAu7lVgUWerY9zAZ51g44yZ0EPiSQveV56tS753mf_w8CaM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
💢
سنای ایالات متحده با رای ۵۰ به ۴۸، قطعنامه‌ای که توسط مجلس نمایندگان تصویب شده بود را برای جلوگیری از اقدام نظامی علیه ایران مگر اینکه رئیس‌جمهور ترامپ ابتدا مجوز کنگره را کسب کند، تصویب کرد.
«همچنان ترامپ میتونه وتو کنه»
@News_Hut</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/news_hut/66753" target="_blank">📅 10:34 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66752">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ea291f4b71.mp4?token=gajycXfOgEzNIffoD_v3hSCP2uehV9vfNQuQw3HJVVtu6Q7EuPyAwR79HI3KFCsoqJRx_Q0VKP6_H-JrQtRTrR8yyKj0QPpBBSD54dOKGtJtTOzIQVRx2Zpfyvaz5MuTF4KKWOyleg6DQM3uvMURnGZgB8_AWf_s9D9xuIm2qx2tEYOlVQyssF6_izhTrJKpbeNBQpb0TKRs-CaTdcarAMh0SL_ou1iwVUengEJwnh062RBQ0Ce6qncK2TiOONoRG7YhWEm565kdaqOj9oIxXtRYLtZhBnFhW7izhu-5fxAkIa6_KtEQe7X15b_fSU9MRE5MN7oDb8n09nvP6JrvZg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ea291f4b71.mp4?token=gajycXfOgEzNIffoD_v3hSCP2uehV9vfNQuQw3HJVVtu6Q7EuPyAwR79HI3KFCsoqJRx_Q0VKP6_H-JrQtRTrR8yyKj0QPpBBSD54dOKGtJtTOzIQVRx2Zpfyvaz5MuTF4KKWOyleg6DQM3uvMURnGZgB8_AWf_s9D9xuIm2qx2tEYOlVQyssF6_izhTrJKpbeNBQpb0TKRs-CaTdcarAMh0SL_ou1iwVUengEJwnh062RBQ0Ce6qncK2TiOONoRG7YhWEm565kdaqOj9oIxXtRYLtZhBnFhW7izhu-5fxAkIa6_KtEQe7X15b_fSU9MRE5MN7oDb8n09nvP6JrvZg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
جورجیا ملونی نخست‌وزیر ایتالیا:
نمی‌توان اجازه داد ایران به سلاح‌های هسته‌ای یا کلاهک‌های هسته‌ای دست یابد، به‌ويژه با توجه به اینکه ایران موشک‌های دوربرد دارد و این مسئله را به وضوح نشان داده است.
ملونی تأکید کرد که این موضوع تنها به ایالات متحده یا کشورهای نزدیک به مرزهای ایران یا اسرائیل محدود نمی‌شود، بلکه مسئله‌ای است که نمی‌توانیم آن را اجازه دهیم یا تحمل کنیم.
@News_Hut</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/news_hut/66752" target="_blank">📅 10:03 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66751">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3361863344.mp4?token=Kn3DO2pA3ve2WcAIINnjM6eGVGPlwmAvfUjtS8tUyXjzs2R-KqcaVUW99H8zgvuYinfaA_xeow7pJEOsrnqOY4WL4o0aamK5xVkZG07nnQzu2a4Xj7eW3xjzIdQjhkyYWVOSwXOnMplzO7IS_sRZK957XY4-kuTWldIYSLk_vigsIAouLK-RQgnPVwjbqU59ghJ9iFsotjVsWnkqUhZVFLSKu8CLq1gjDoU4o-4xyIikIM0JNiQHijPoVamB497qGSlMj2ubgyD0w6fPuvThUTF74jIItNy2S5tbdXKQzZL81HwFqdDkx0wrdugqkqfHyKvrEKgLi_vI15r1YjcwKw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3361863344.mp4?token=Kn3DO2pA3ve2WcAIINnjM6eGVGPlwmAvfUjtS8tUyXjzs2R-KqcaVUW99H8zgvuYinfaA_xeow7pJEOsrnqOY4WL4o0aamK5xVkZG07nnQzu2a4Xj7eW3xjzIdQjhkyYWVOSwXOnMplzO7IS_sRZK957XY4-kuTWldIYSLk_vigsIAouLK-RQgnPVwjbqU59ghJ9iFsotjVsWnkqUhZVFLSKu8CLq1gjDoU4o-4xyIikIM0JNiQHijPoVamB497qGSlMj2ubgyD0w6fPuvThUTF74jIItNy2S5tbdXKQzZL81HwFqdDkx0wrdugqkqfHyKvrEKgLi_vI15r1YjcwKw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
سر دادن شعار «مثل رهبر ما مخالف با تفاهم‌نامه‌ایم»در هیات
@News_Hut</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/news_hut/66751" target="_blank">📅 09:33 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66750">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8f22d87ed3.mp4?token=k-xH3gUsnBoYRaPYKymTlbLW5KEQBcf7a2UVFHoXgtY5Ve5TxE-yBgM287F1M6-6H9YFmGCHLJFseazkUsRIpqDQGRMs9BIK4HNl6_qF3KEeSkFRRF-yuL4_YzTql6Fx6fP3FP3QWA5tUGFKOakYM9-xcJRFhZY_aIAyg90zCywp36yRRlUCTV6c4KR4EtMxi_v-s6JUsoIjIx2FFfKig50QaJBKdXQVJL25Of44kWu-NlciPx8Yegmg4GQ1GFnKyb2eqYjmmnZODyEhQzjgKU5EUDNJmRQe6uYfqQX36VCcRNeBamEmT95HuLvo0-lu8P-ILDRq6p1XClHREOUkJQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8f22d87ed3.mp4?token=k-xH3gUsnBoYRaPYKymTlbLW5KEQBcf7a2UVFHoXgtY5Ve5TxE-yBgM287F1M6-6H9YFmGCHLJFseazkUsRIpqDQGRMs9BIK4HNl6_qF3KEeSkFRRF-yuL4_YzTql6Fx6fP3FP3QWA5tUGFKOakYM9-xcJRFhZY_aIAyg90zCywp36yRRlUCTV6c4KR4EtMxi_v-s6JUsoIjIx2FFfKig50QaJBKdXQVJL25Of44kWu-NlciPx8Yegmg4GQ1GFnKyb2eqYjmmnZODyEhQzjgKU5EUDNJmRQe6uYfqQX36VCcRNeBamEmT95HuLvo0-lu8P-ILDRq6p1XClHREOUkJQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
ویدیو ای وایرال شده از خوشحالی تیم ملی نروژ به سبک وایکینگ ها
😂
@News_Hut</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/news_hut/66750" target="_blank">📅 09:04 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66749">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">فک کنم اگه هرشب با ۱۰۰ هزار تومن میومدین چنل بت ما ، شبی بالای ۲ میلیون سود کرده بودین مثل دیشب:)
😊
😂
میگی ن ؟ بیا تو چنلمون و ببین
🔥
@FutballFuckBet @FutballFuckBet @FutballFuckBet @FutballFuckBet</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/news_hut/66749" target="_blank">📅 02:00 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66748">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/pWC8tVNL1QbL3OWpsyFatW1Wellno3JBNiCONWZ8B9U_MuxGemDE-41gd8meBTwGOVpzuzIESByrDoTjQ4dmuUYKX6LgaxSiMNC-to1YWe5Z8ykQFO4RmXTZrA0jMVr4KIOnFfYIgLh4f7cIdhpal5P7AGINbEolhsKCG_bioTY7tKxLLJg_Axstc5RAVYaMeWH7BMNs3lsnUAPrOLg0rWVekYZ_Hwqz5S03kQflRSOK6rNuLzUMMMpCG0BQ5wE1p7d9gmE4kMAVMtCTxfbb07JDLAc6dGCK253bzPN4y8ukaE34ov1zrHlAy3_3kU6nB-hzHFaouQTymOo_AQNNmQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فک کنم اگه هرشب با ۱۰۰ هزار تومن میومدین چنل بت ما ، شبی بالای ۲ میلیون سود کرده بودین مثل دیشب:)
😊
😂
میگی ن ؟ بیا تو چنلمون و ببین
🔥
@FutballFuckBet
@FutballFuckBet
@FutballFuckBet
@FutballFuckBet</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/news_hut/66748" target="_blank">📅 02:00 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66747">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f89b5dc5b2.mp4?token=MHxGDpPlIiM2NTQ9CeXAp1vSva5VGtEdychrQGv8h9KJYKx7THMs_pJLh-wgqNZuZ1GqOksh99MkWNr_hg1YMIYkHrm3faYx1Vhkub9SZyJuGJAny0pB6OFiVb7iCfTSNvJ621HafIJO8sQOA1ZuWBXBSipO_Pi9fz-nKULoXjkwOveuQ1wVKJQKnRStFsR0WH4uv-l6JY9ssWPOb1hDMTVNrOrX_BYYQk5M8wfGHKJxG0GixTA7KTqjeVYgLtFX8GtUPcuVCdMKueqLmhrNoteSiDnbY0eWNfOI21dCiOIoUxI7S8120-ouBZfuFqNmX646mOSZ4RELYX1jXShQIw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f89b5dc5b2.mp4?token=MHxGDpPlIiM2NTQ9CeXAp1vSva5VGtEdychrQGv8h9KJYKx7THMs_pJLh-wgqNZuZ1GqOksh99MkWNr_hg1YMIYkHrm3faYx1Vhkub9SZyJuGJAny0pB6OFiVb7iCfTSNvJ621HafIJO8sQOA1ZuWBXBSipO_Pi9fz-nKULoXjkwOveuQ1wVKJQKnRStFsR0WH4uv-l6JY9ssWPOb1hDMTVNrOrX_BYYQk5M8wfGHKJxG0GixTA7KTqjeVYgLtFX8GtUPcuVCdMKueqLmhrNoteSiDnbY0eWNfOI21dCiOIoUxI7S8120-ouBZfuFqNmX646mOSZ4RELYX1jXShQIw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🇺🇸
پرزیدنت ترامپ:
«ایران عالی بوده است؛ ایران منطقی رفتار کند و باهوش باشد. در غیر این صورت، مجبور خواهیم شد کار را تمام کنیم.»
@News_Hut</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/news_hut/66747" target="_blank">📅 01:25 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66746">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f7d99b64b2.mp4?token=mTo2PT0HYK2O4cfERqOQWysosquXJzehb9MZGpvARBnHn8RvQeNitEyKlKWS2zbCAy0WgbrRpBOLet9awwuOqJmgbLMbasHOhEwbx82q80x2Cz83RvEwOgQ6WgYbtfkKOnULscp0NUFuJXq2mmCnT6MTHNRGLk7hdTAjDbL3GQ6Vjcfo05ND8PK90gAP8EzmvDJtx1qtExE50MXwWP3HWEY5jFkI3rC66rd-RxJFecHz2mYJDchtOciQNdoGo0i8IeGpHNdrHBqom6XJpxEsdD9KBNQvNJD5XV_FoO-TwfYdXOau_4H48yCDzrLaew0vl32qseDEzA88RHKarx8NbQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f7d99b64b2.mp4?token=mTo2PT0HYK2O4cfERqOQWysosquXJzehb9MZGpvARBnHn8RvQeNitEyKlKWS2zbCAy0WgbrRpBOLet9awwuOqJmgbLMbasHOhEwbx82q80x2Cz83RvEwOgQ6WgYbtfkKOnULscp0NUFuJXq2mmCnT6MTHNRGLk7hdTAjDbL3GQ6Vjcfo05ND8PK90gAP8EzmvDJtx1qtExE50MXwWP3HWEY5jFkI3rC66rd-RxJFecHz2mYJDchtOciQNdoGo0i8IeGpHNdrHBqom6XJpxEsdD9KBNQvNJD5XV_FoO-TwfYdXOau_4H48yCDzrLaew0vl32qseDEzA88RHKarx8NbQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🇺🇸
پرزیدنت ترامپ:
ایران ایدئولوژی بسیار متفاوتی نسبت به ونزوئلا دارد.
ایدئولوژی مسلمانان تا حدی با ایدئولوژی کاتولیک‌ها متفاوت است.
@News_Hut</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/news_hut/66746" target="_blank">📅 01:15 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66745">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0a9dbdc564.mp4?token=Gvph5-i2PZQgZiVo4Gybcw2l3cEaxGn3TGFNJ5ddrCwxnTVy1Shwbr_2E8CgYAdbBgk_TbDJAzSUmc7knP4aSN4jKZBFwWTcoD1pEbsfkzk50DCgxX9kRHYUZBHDR-DZ7vpPpXso05wSY_Pvr5mMM2EokpsgE1XQJ1WZtX80bcy7ISIOoA05uHg8OWRFnZyWEUWKMNVz0C9hUnyhW9m_iDKyLZOfuPpZBEbehtqRRfPUK_OsCXP7vEQhH1WvfBXVTBHFqZrWJbMZKB40qWmrzsDwEB_YexiQxfqRxQ8vU-P30a7O8amFfFZw_FhJR3RrUhRzjCI1noxNh5WKfGdQ2w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0a9dbdc564.mp4?token=Gvph5-i2PZQgZiVo4Gybcw2l3cEaxGn3TGFNJ5ddrCwxnTVy1Shwbr_2E8CgYAdbBgk_TbDJAzSUmc7knP4aSN4jKZBFwWTcoD1pEbsfkzk50DCgxX9kRHYUZBHDR-DZ7vpPpXso05wSY_Pvr5mMM2EokpsgE1XQJ1WZtX80bcy7ISIOoA05uHg8OWRFnZyWEUWKMNVz0C9hUnyhW9m_iDKyLZOfuPpZBEbehtqRRfPUK_OsCXP7vEQhH1WvfBXVTBHFqZrWJbMZKB40qWmrzsDwEB_YexiQxfqRxQ8vU-P30a7O8amFfFZw_FhJR3RrUhRzjCI1noxNh5WKfGdQ2w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یادی کنیم از این میم.
@News_Hut</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/news_hut/66745" target="_blank">📅 00:03 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66744">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cacbd8e2b7.mp4?token=JZVRtmpNM57LWWn3cX8HqMHCU08BI-uxlOu9yoj3KeeWGuIPq54s7M00sLMnLKuZWqr-SMyEqcXzUm3jmj1Iu5HsV_QJczzhVYtaQn3RJnu_f8UHE1eZCnBruhMkwNenQUOrhn4rwq46yvGwtSFX3CEBhTXbXVY6bJ62SfG8JNLNiRPnPetSbDm9EEMGt98yLCEn7IpLzLWWPIfVdgRBsTsk10IQ4hHq4pj83mzA_m5dSfF2bd7P3GR9QKWrHec9boCPa23d_4hpsOVYHgT5YUYAmiBAwCLDhFYV2HNBoJXhYzKFE0iqZiINuXRPsnpbzNY4DjlYqnCEfj1W1u9hpw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cacbd8e2b7.mp4?token=JZVRtmpNM57LWWn3cX8HqMHCU08BI-uxlOu9yoj3KeeWGuIPq54s7M00sLMnLKuZWqr-SMyEqcXzUm3jmj1Iu5HsV_QJczzhVYtaQn3RJnu_f8UHE1eZCnBruhMkwNenQUOrhn4rwq46yvGwtSFX3CEBhTXbXVY6bJ62SfG8JNLNiRPnPetSbDm9EEMGt98yLCEn7IpLzLWWPIfVdgRBsTsk10IQ4hHq4pj83mzA_m5dSfF2bd7P3GR9QKWrHec9boCPa23d_4hpsOVYHgT5YUYAmiBAwCLDhFYV2HNBoJXhYzKFE0iqZiINuXRPsnpbzNY4DjlYqnCEfj1W1u9hpw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
پزشکیان:
​
اگر ما موشک‌های خود را که برای دفاع شخصی‌مان است نداشتیم، اسرائیل و آمریکا با ایران همان‌گونه رفتار می‌کردند که با غزه رفتار شد و هیچ رحمی به پیر و جوان نشان نمی‌دادند.
​ آن‌ها از حقوق بشر سخن می‌گویند، این یک دروغ بزرگ است.
​ اگر نمی‌توانستیم از خود دفاع کنیم، آن‌ها به کشور ما رحمی نمی‌کردند و قدرت ما را نابود می‌کردند.
​ بنابراین ما تحت هیچ شرایطی با هیچ‌کس درباره توان دفاعی‌مان مذاکره نخواهیم کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/news_hut/66744" target="_blank">📅 23:32 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66743">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/26c20ba7fc.mp4?token=aiIB1dzEGQS5L61d0haJhAkcsZOVXH8bchBFhUTnWL5T13dHK8jJG3nhm6tNApqBees5BHAaGbCmzvU-OhVYzOISpZ-lmpI7Kbwnbnh-P-KqIGxayLRp1ciVyccZItnUw46X0Vokt15fMLOYXS8Nbdrjohllv-duodlvn_eYt_uP_xqy2yr47xfI-ttgeKPX-9IZ4Hqib3-snhO26K69VgN1DHrsa9OM8TzDv76RJPzSd9W-Df3BPTGZVMd_nBlV2a2IK2isu1XgpY6ZZx0bwuQMaMWruosxR0PNOJcavV20--CXntYIMxWpbTARvjMDm1yGtBRtwvEPU5HwqMt2cw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/26c20ba7fc.mp4?token=aiIB1dzEGQS5L61d0haJhAkcsZOVXH8bchBFhUTnWL5T13dHK8jJG3nhm6tNApqBees5BHAaGbCmzvU-OhVYzOISpZ-lmpI7Kbwnbnh-P-KqIGxayLRp1ciVyccZItnUw46X0Vokt15fMLOYXS8Nbdrjohllv-duodlvn_eYt_uP_xqy2yr47xfI-ttgeKPX-9IZ4Hqib3-snhO26K69VgN1DHrsa9OM8TzDv76RJPzSd9W-Df3BPTGZVMd_nBlV2a2IK2isu1XgpY6ZZx0bwuQMaMWruosxR0PNOJcavV20--CXntYIMxWpbTARvjMDm1yGtBRtwvEPU5HwqMt2cw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
مارکو روبیو وزیر امور خارجه آمریکا وارد ابوظبی، پایتخت امارات متحده عربی، شد. جزئیاتی درباره دستور کار، دیدارهای رسمی و محورهای مذاکرات این سفر هنوز منتشر نشده است، اما این سفر در شرایطی انجام می‌شود که پرونده‌های امنیتی و تحولات منطقه‌ای، از جمله موضوع رژیم جمهوری اسلامی، در کانون توجه قرار دارند.
@News_Hut</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/news_hut/66743" target="_blank">📅 23:01 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66742">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a4552ac245.mp4?token=kBppxhsdJilPqr_-z4tRHHi71RXMclDdguXosVLybuCpitP919mjeCPj3Qsv5bH6sktquGSZKopOg498JLatOZqa4Sx1ESRmsQ_PCxghAzepPUVd2GaRRTgKygFKDfa5CMtLn1bz9m-lORr1DWNoZaC44PICloggYrFKJkwSep8r2GT7h0S02PExbUMQAz_Frgkue_tRYUlDoAFTOHA1YUc5UPWrDDJG5wF1ZPVuWKkpzzEu_MTATHSEaygdODQuY7WIDryuKe7quKAxGSG8oyHGTjUV3gzdwG-6OmFzXuU2SJByTSE4ZmR4HDO1JoHuhuj2aUMDOVK00xACdY0hWg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a4552ac245.mp4?token=kBppxhsdJilPqr_-z4tRHHi71RXMclDdguXosVLybuCpitP919mjeCPj3Qsv5bH6sktquGSZKopOg498JLatOZqa4Sx1ESRmsQ_PCxghAzepPUVd2GaRRTgKygFKDfa5CMtLn1bz9m-lORr1DWNoZaC44PICloggYrFKJkwSep8r2GT7h0S02PExbUMQAz_Frgkue_tRYUlDoAFTOHA1YUc5UPWrDDJG5wF1ZPVuWKkpzzEu_MTATHSEaygdODQuY7WIDryuKe7quKAxGSG8oyHGTjUV3gzdwG-6OmFzXuU2SJByTSE4ZmR4HDO1JoHuhuj2aUMDOVK00xACdY0hWg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
شعرخوانی جالب شهباز شریف به زبان فارسی در حضور پزشکیان
@News_Hut</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/news_hut/66742" target="_blank">📅 22:31 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66741">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">🚨
🚨
🚨
🇺🇸
پرزیدنت ترامپ:
ما ایران را در وضعیتی بی‌سابقه قرار دادیم که در ۴۷ سال گذشته هیچ‌کس موفق به انجام آن نشده بود. اگر ادعای ایرانی‌ها مبنی بر عدم اجازه ورود بازرسان آژانس بین‌المللی انرژی اتمی به ایران صحت داشت، نشست با آن‌ها را فوراً لغو می‌کردم.
@News_Hut</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/news_hut/66741" target="_blank">📅 21:05 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66740">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1918a30d5e.mp4?token=KPfl1cdHWLA93sD0n1QHJLMR6D7YlkGEqVnFT1AUWuxbWzoIsszCF_jUxMkAyLxRHj6VQeLuEYPf4xtFZ84yyiHjH2aoZ3_AoV7oriP6Djjvjg7er4XYIvIFIwhjljFfbyZBgsGGCERoMnXKjmP0mbloabS265MabqZIEc_EuZrm_pJqNpt7143PX7dVzDDszVXDbPngaFEc9uFyBDexamM4ITqPYGH8rjJm32e8FgiPbOJZEoBGF4s6doSemitOr7FV33yBRL2FTIe3ZDRFE-JDwzooqB9wMIlgJyEzxTsRBV26sBwhsH-Q2rALALL3-1R9OAI83yp-Ivg0-gyU2w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1918a30d5e.mp4?token=KPfl1cdHWLA93sD0n1QHJLMR6D7YlkGEqVnFT1AUWuxbWzoIsszCF_jUxMkAyLxRHj6VQeLuEYPf4xtFZ84yyiHjH2aoZ3_AoV7oriP6Djjvjg7er4XYIvIFIwhjljFfbyZBgsGGCERoMnXKjmP0mbloabS265MabqZIEc_EuZrm_pJqNpt7143PX7dVzDDszVXDbPngaFEc9uFyBDexamM4ITqPYGH8rjJm32e8FgiPbOJZEoBGF4s6doSemitOr7FV33yBRL2FTIe3ZDRFE-JDwzooqB9wMIlgJyEzxTsRBV26sBwhsH-Q2rALALL3-1R9OAI83yp-Ivg0-gyU2w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🇺🇸
مارکو روبیو درباره تنگه هرمز:
این یک آبراه بین‌المللی است. هیچ کشوری اجازه ندارد برای یک آبراه بین‌المللی عوارض یا هزینه دریافت کند.
این همان قانون بین‌المللی موجود است. در تمام آبراه‌های بین‌المللی در سراسر جهان همین‌طور عمل می‌شود و ما انتظار داریم که اینجا هم همین‌گونه باشد
@News_Hut</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/news_hut/66740" target="_blank">📅 20:55 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66739">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8deb9fca75.mp4?token=R57XgiUWYmUqC2nd0KFCvvmaeNEdLjm1ugEeF2fPCtbzzrhhSIJvavq0SjfzyK7W4VoDHQqOJ1spKhy-irlaCOkORq_-cQrHyS7dePj5h5q0EVJUW-YBvukKf_8NDjBwk__4WyyI0CLV_RSbpo8kSJVSw9PiytoGSJiHe7ox9l-4FBmLMsDDmQND7gU-rwS69Oe9YIzP10FCkz0eBSvdkLN4QiTBQvysZAOySHd3ajN0Gcuv1qsc8lYQWEOuxbOlf2xCwURjtjidvRRV2Sxzwn8mdfZ2s1CPV26XerDabFqN8HR1H8eVerqRf3rfRIpS13RnZ7KkYP5OaCXU3_5KHw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8deb9fca75.mp4?token=R57XgiUWYmUqC2nd0KFCvvmaeNEdLjm1ugEeF2fPCtbzzrhhSIJvavq0SjfzyK7W4VoDHQqOJ1spKhy-irlaCOkORq_-cQrHyS7dePj5h5q0EVJUW-YBvukKf_8NDjBwk__4WyyI0CLV_RSbpo8kSJVSw9PiytoGSJiHe7ox9l-4FBmLMsDDmQND7gU-rwS69Oe9YIzP10FCkz0eBSvdkLN4QiTBQvysZAOySHd3ajN0Gcuv1qsc8lYQWEOuxbOlf2xCwURjtjidvRRV2Sxzwn8mdfZ2s1CPV26XerDabFqN8HR1H8eVerqRf3rfRIpS13RnZ7KkYP5OaCXU3_5KHw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🇺🇸
مارکو روبیو:
تا زمانی که نیروهای نیابتی ایران از داخل عراق موشک‌ها و پهپادها را شلیک می‌کنند و در اقداماتی مانند تروریسمی که حماس و حزب‌الله انجام دادند مشارکت دارند، نمی‌توان به پایان خصومت‌ها و درگیری‌ها در منطقه رسید
@News_Hut</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/news_hut/66739" target="_blank">📅 20:38 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66738">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f28eade01e.mp4?token=dabTK4un7rh9muPVFVk5IO0HV2P-xUTUL3eR_qFBy7rlfUfaWyNBgRiNVuj3UfG9Jjh5AD_j9zZTCw3G3H8ATFoRrVDsTEL3gsrpHk7PfjXJB9D1d13ft0etwnxgHnG1Ww6c_oBttkKUHNtiBnFM2UDz96lsnEA-UFK15qwU142mT1DimKbMmvYs_2Ate6m3MQ7e_UNS59QxFdszFjZuog27l-LMcvLKV3RkA29fYyfPRlzB277HZYFeQaGyE8HBzEB6xPvuXoQbNqFgDP0cie0q2-8agbvaT83CQ0QA7v7ENWxPGJtSzGH8SmULaQlyvb7MKBF7ndL2QP3bKCtRIQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f28eade01e.mp4?token=dabTK4un7rh9muPVFVk5IO0HV2P-xUTUL3eR_qFBy7rlfUfaWyNBgRiNVuj3UfG9Jjh5AD_j9zZTCw3G3H8ATFoRrVDsTEL3gsrpHk7PfjXJB9D1d13ft0etwnxgHnG1Ww6c_oBttkKUHNtiBnFM2UDz96lsnEA-UFK15qwU142mT1DimKbMmvYs_2Ate6m3MQ7e_UNS59QxFdszFjZuog27l-LMcvLKV3RkA29fYyfPRlzB277HZYFeQaGyE8HBzEB6xPvuXoQbNqFgDP0cie0q2-8agbvaT83CQ0QA7v7ENWxPGJtSzGH8SmULaQlyvb7MKBF7ndL2QP3bKCtRIQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🇺🇸
مارکو روبیو درباره ایران:
اگر رهبری ج ا  تصمیم بگیرد که می‌خواهد یک کشور باشد، نه یک جنبش انقلابی که ترور صادر می‌کند، آن‌ها فرصت خواهند داشت کارهای فوق‌العاده‌ای در ایران انجام دهند.
این فرصت‌ها می‌تواند شامل سرمایه‌گذاری و سرمایه‌گذاری خارجی مستقیم باشد… این پول دولت ما نخواهد بود.
@News_Hut</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/news_hut/66738" target="_blank">📅 20:33 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66737">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/966e7cdc8b.mp4?token=ENayKoDmYKVdrC_SzTErAybYB7gBWTB2UiCXhqq7CJH-7TKvTjJfnXHjdKxiT4-zzkdEyTK6RKg_h1gAk0mrLhUAWmUHywBF0QPSJAVJWXhUX2Mg1izAnC8nJWZBsVTGa_qMwF_9d0IV9uYZ0LCdglAtNrwKKT0wwrce7P4pXPReD40lYDzYC7vVtpD1VjSyjuox664xZT3yFUpX4FTw8qqFKUwqYY5LVNfxKsh33uU8bL_r3ozAylQW5L9WIZYfiYbUI1x9uHBVjUlr3ZvE7LyoYkqXqGJ32LWLbTBH2t7FTO7wn4rU2W4b7rxIC8VJ4Q-DfyYJocMPlyiPUS0Bcw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/966e7cdc8b.mp4?token=ENayKoDmYKVdrC_SzTErAybYB7gBWTB2UiCXhqq7CJH-7TKvTjJfnXHjdKxiT4-zzkdEyTK6RKg_h1gAk0mrLhUAWmUHywBF0QPSJAVJWXhUX2Mg1izAnC8nJWZBsVTGa_qMwF_9d0IV9uYZ0LCdglAtNrwKKT0wwrce7P4pXPReD40lYDzYC7vVtpD1VjSyjuox664xZT3yFUpX4FTw8qqFKUwqYY5LVNfxKsh33uU8bL_r3ozAylQW5L9WIZYfiYbUI1x9uHBVjUlr3ZvE7LyoYkqXqGJ32LWLbTBH2t7FTO7wn4rU2W4b7rxIC8VJ4Q-DfyYJocMPlyiPUS0Bcw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
شهباز شریف، به پزشکیان:
لطفاً گرم‌ترین تحیت‌های خود را به مقام معظم رهبری، آیت‌الله مجتبی خامنه‌ای برسانید.به لطف رهبری ایشان، ایران توانسته است این تفاهم‌نامه را به دست آورد و در نتیجه، آتش‌بس را با کرامت و افتخار به دست آورد.
@News_Hut</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/news_hut/66737" target="_blank">📅 20:16 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66736">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cbcf82c8e4.mp4?token=WrRhd7nhB01hzetxngxWLLiGSLR83NwsGIM2IM7qU_dbc9J99KN-HdZT3Mb0D14WxcbuwpwE4orpwAEk8H8H3Zqx26Di1IukgWME0DeIs1Ej4xAmapWY5kLt9JjfQXUpTxkV0CVOcGpxUWvzmf_nq30prXmBbdxG8ZbFoM6uUsv1fHwOdQBknZgkwXvaqKmPduYyNAmt8hgMPJ5Gd3obCUBs9wCYVEFkSd285Ltj4LJ6h55ZVrsCPfg0f6kv2BH6XBOyzGjKqnIxCXQ8aIoDSANBq81uYjZynm0xe7Fnb5UCpWNri6KcnpuDsVwpCcr1nhq8KXykEllTkRR-_ZIvOg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cbcf82c8e4.mp4?token=WrRhd7nhB01hzetxngxWLLiGSLR83NwsGIM2IM7qU_dbc9J99KN-HdZT3Mb0D14WxcbuwpwE4orpwAEk8H8H3Zqx26Di1IukgWME0DeIs1Ej4xAmapWY5kLt9JjfQXUpTxkV0CVOcGpxUWvzmf_nq30prXmBbdxG8ZbFoM6uUsv1fHwOdQBknZgkwXvaqKmPduYyNAmt8hgMPJ5Gd3obCUBs9wCYVEFkSd285Ltj4LJ6h55ZVrsCPfg0f6kv2BH6XBOyzGjKqnIxCXQ8aIoDSANBq81uYjZynm0xe7Fnb5UCpWNri6KcnpuDsVwpCcr1nhq8KXykEllTkRR-_ZIvOg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
شهباز شریف:
این تفاهم‌نامه هیچ اشاره‌ای به موشک‌های بالستیک ندارد.
این موضوع هرگز روی میز نبود؛ هرگز در دستور کار قرار نداشت.
طرف ایرانی هم اصلاً نمی‌خواست درباره آن بحث کند
@News_Hut</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/news_hut/66736" target="_blank">📅 20:15 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66735">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/he8szQizXHGmeB2A9KpzPDv12MNyBFgyzqyWD9PTWGJ2Jw44BXDTQQGqgx3PfjgBiJsKQbhlVwdaayEu75ApkrjN-ai8u07XoFqTk139GGt-PHma7Sy5h97RTKDUrN4PwDZOtZnq4qybAoRlc7eaiLGwZdFNO2dUm0VYR2Gw3_iYoEfRvKhYJcVxp2M7MALFrW7VyHlKkHzDlk73I_9k22gmt4ryeQ8eJxkR7tsAYBEdXCOO52GIt9KniXnoamjvYRvsYLIfsmc4osypBQqG49EEulgn0OU56JMnx9pr3h2v_wr1GWjoO2Cu9GAQPU7vn9wT9POqt4GQBV6XxoY72Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">استوری پسر پاسدار کشته شده علیرضا تنگسیری فرمانده سپاه که معلوم شده اینم طوری زدن که فقط یک دستش جا مونده.
@News_Hut</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/news_hut/66735" target="_blank">📅 19:51 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66734">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">شایعه شده ایلان ماسک قبل اینکه میلیاردر بشه تو فاک بت جوین داده بوده
🔥
با آنالیز حرفه ای ادمین های فاک بت ، بصورت رایگان از فوتبال دیدن پول در بیارید  با فاک بت ، حرفه ای تر شرطبندی کنید
❤️
@FutballFuckBet @FutballFuckBet @FutballFuckBet @FutballFuckBet</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/news_hut/66734" target="_blank">📅 19:51 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66733">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/d_hSKcBo_sBoDZODdTyQDWnB2fUXE73ER_3ckDnDzKqcw41uvFlEdd2O38VTm9t0-QWPjffoWwBTG5D0U0flqNZRgnb3MRHUzjOL76-RaJ8GOgQfp8P67lHtYGB4qE7iCNa0RcjrIA1hPjKXgicz5Y-TIynKE-XpUcE0TtvmeBIQC_77b1J8j7vtpnma1qaolJ0Obijwbug0ziAnZmylTl3MyHrio3KTRs0lhIrkUTOuY8S7SrLfAyPB1YY5dJ2i19SRPILKVG7yCURiUBydJYrEfATunqMP7Q-Gz9VrP5B-_CyD4MjxaEkKiU3pdH-l1xoT0iwTEe5CAYG1LvEkhg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شایعه شده ایلان ماسک قبل اینکه میلیاردر بشه تو فاک بت جوین داده بوده
🔥
با آنالیز حرفه ای ادمین های فاک بت ، بصورت رایگان از فوتبال دیدن پول در بیارید
با فاک بت ، حرفه ای تر شرطبندی کنید
❤️
@FutballFuckBet
@FutballFuckBet
@FutballFuckBet
@FutballFuckBet</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/news_hut/66733" target="_blank">📅 19:51 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66732">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/aee9776a17.mp4?token=qv5pG0cpoqT3Lz4ybGtPmywPfsbdopJuuRYstv2IV8i17ajtfl0wYxXK70nEpS-NTt32eVlwuw7z96JrkgxW_iTJRcjN9VNuk8TvJLitgSZoGyCHd4YOv86uaimD8OMFABstM8Wp3qsvjryjvvsJfner-D4WBUuDXDnyLF5k_yj0DGPR_Tqdxtokt217fnYeVd82WCJftWixq1VEdABTQPxxpdShYlEydAMkuDLmc3K0bqtCv2f1o1YEQRmz-2jhmXUnPnJd93eR5edumdOe_nxjKAXev_RfE0w-Hd_irVXQEqlQLsw2GG379CHXY-8tU11t0xAmvDXLtrJpp79_RQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aee9776a17.mp4?token=qv5pG0cpoqT3Lz4ybGtPmywPfsbdopJuuRYstv2IV8i17ajtfl0wYxXK70nEpS-NTt32eVlwuw7z96JrkgxW_iTJRcjN9VNuk8TvJLitgSZoGyCHd4YOv86uaimD8OMFABstM8Wp3qsvjryjvvsJfner-D4WBUuDXDnyLF5k_yj0DGPR_Tqdxtokt217fnYeVd82WCJftWixq1VEdABTQPxxpdShYlEydAMkuDLmc3K0bqtCv2f1o1YEQRmz-2jhmXUnPnJd93eR5edumdOe_nxjKAXev_RfE0w-Hd_irVXQEqlQLsw2GG379CHXY-8tU11t0xAmvDXLtrJpp79_RQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
ویدیوی منتشر شده از عباس عراقچی و همتی که وسط مذاکرات با آمریکا پا شدن رفتن بازی ایران و بلژیکو تماشا کردن.
اینجا گفته بودن مذاکرات ترک میکنیم اما رفتن فوتبال ببینن
😂
😂
@News_Hut</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/news_hut/66732" target="_blank">📅 19:05 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66731">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/df51f5307d.mp4?token=hjk--ZkO9qMmrvor5BmGZ8RX60XVI1Q9JCFEfb-yilr2eSDsWikStv-cu9X9L-sFT0zYat48Ir_3MVvcbRjTqXx75D68NkDzvlrrHfAyrBfNP8oBU4ss1AB1k8Y6e4OCmtJuhgfpuEb5NWaC1T1Pbzh-ZMS4pOtMwAIwQgmVz_CMJERazzaY02c_BagZfO46Fjltrmj7bVv4PlBie-lg8t0oNdyxtGWiKvL3stG6zunY_sWp9i3L0rc4BMrrhroDnutj2qsPlFXsCZk09oYonBvZ2QZT9fcROGA9ZFh1qHHMogluPRFqaAy6FNbcqLsv_ShJlcN2eTo6i7zX-hiNJQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/df51f5307d.mp4?token=hjk--ZkO9qMmrvor5BmGZ8RX60XVI1Q9JCFEfb-yilr2eSDsWikStv-cu9X9L-sFT0zYat48Ir_3MVvcbRjTqXx75D68NkDzvlrrHfAyrBfNP8oBU4ss1AB1k8Y6e4OCmtJuhgfpuEb5NWaC1T1Pbzh-ZMS4pOtMwAIwQgmVz_CMJERazzaY02c_BagZfO46Fjltrmj7bVv4PlBie-lg8t0oNdyxtGWiKvL3stG6zunY_sWp9i3L0rc4BMrrhroDnutj2qsPlFXsCZk09oYonBvZ2QZT9fcROGA9ZFh1qHHMogluPRFqaAy6FNbcqLsv_ShJlcN2eTo6i7zX-hiNJQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یک روحانی : اسم بچه‌هاتون رو امیر نزارید، ریشه این اسم بهایی هست
😐
@News_Hut</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/news_hut/66731" target="_blank">📅 18:34 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66730">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9028c70792.mp4?token=F7iOyRm06kcSZfeAmtXOoYPW3TIsG4jHWuI-pKyI1U8CqDtEttubAhCGN58GuhQPRK4VR78TwERONmkq2Qtl12Xf4O6XcqLkZUQBjZDLvnynyPTaRf-ECLeXKdMB0x4ylmsW_PgXaJl6xsbU4pfOBsPfAS5quOtrHiQxYnSpYoRO3EN-BncZ_kHYyWIc0WFP9CmMykyMAVWn8nXF7yDq5a0RDl3zp9jOXFjHo_KrRynEojpB2FuwE3qFci8NBCJr8ThBhmrkr9YJzo6ywByDHMiA8JKewxS9MJiNnb83K6zj_C8xiCbLGdxYT0p3nN8J__hKXMCcibCAqMADCgGhWQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9028c70792.mp4?token=F7iOyRm06kcSZfeAmtXOoYPW3TIsG4jHWuI-pKyI1U8CqDtEttubAhCGN58GuhQPRK4VR78TwERONmkq2Qtl12Xf4O6XcqLkZUQBjZDLvnynyPTaRf-ECLeXKdMB0x4ylmsW_PgXaJl6xsbU4pfOBsPfAS5quOtrHiQxYnSpYoRO3EN-BncZ_kHYyWIc0WFP9CmMykyMAVWn8nXF7yDq5a0RDl3zp9jOXFjHo_KrRynEojpB2FuwE3qFci8NBCJr8ThBhmrkr9YJzo6ywByDHMiA8JKewxS9MJiNnb83K6zj_C8xiCbLGdxYT0p3nN8J__hKXMCcibCAqMADCgGhWQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
ثابتی:مذاکرات به رهبری تحمیل شد وگرنه نظرشون چیز دیگه ای بود
😂
😂
@News_Hut</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/news_hut/66730" target="_blank">📅 18:02 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66729">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ed1cc8a0c1.mp4?token=YSt1IPeNAW74Xmiew4OXaql29Tu39T3ZLIbuip8qte9Ik0pmK62LW_bBZnSPiXKPMq2tE68AsjrX6gL4XhpfVGWxK1-eW5CTdlZ1CAfUpVyiz32oXSAHLrAj4J3VBD5qsgnRR6lgRA_cWCQj7actTwRZTzQE8KRvFdviaIjII80xtIUx34707xR-lxueRDyef75Chbwi5ZY-KjO_Jy1v9eUZluXysDIOspl-rE5I2Qkej0Ur1DTlErs-9C_oS2pSwtgNz9byx3g4jqc4W5_v1R24p1ElBpVhsIWM5tJi1uwDThjKwN3ecD8fAHZGREAsJonp8-o6G1K3HB7X5mQ-0w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ed1cc8a0c1.mp4?token=YSt1IPeNAW74Xmiew4OXaql29Tu39T3ZLIbuip8qte9Ik0pmK62LW_bBZnSPiXKPMq2tE68AsjrX6gL4XhpfVGWxK1-eW5CTdlZ1CAfUpVyiz32oXSAHLrAj4J3VBD5qsgnRR6lgRA_cWCQj7actTwRZTzQE8KRvFdviaIjII80xtIUx34707xR-lxueRDyef75Chbwi5ZY-KjO_Jy1v9eUZluXysDIOspl-rE5I2Qkej0Ur1DTlErs-9C_oS2pSwtgNz9byx3g4jqc4W5_v1R24p1ElBpVhsIWM5tJi1uwDThjKwN3ecD8fAHZGREAsJonp8-o6G1K3HB7X5mQ-0w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
انتقاد مجری صداوسیما از رفتن قالیباف به مذاکرات
@News_Hut</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/news_hut/66729" target="_blank">📅 17:33 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66728">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HEHcGIt8DYqqESm6xpURPEKSwgZSfusts9VntHZLys5Pc27A6kVQNLg_wNAOfsskAxszdu2DZEcf04J7826_T9gifarqf5X8oAcxDwvk5r0gKoiy_7EYMGxcRFLaQGEXEjCAgJ2nrO0260Sm6gZHWhdkWVQsXYr6QveYQbbI_1_Q7BmW4uaLmq9zoe-Fls3aagmMn2RRsoPNt4F7l-E72DJMsrl5QHpKAxgalNOV2y6ViaeEZ_d-l9teUK_MIOTsopRLl3ACDZlW7E4IVdQly9lmTeBcShc8ttk7_6VAx67qoNHGeD4LnFBmrh1PIgJinmTI2RQVG2JwyOYeJh86XQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
آناتولی گزارش داده که شهباز شریف گفته قراره درباره برنامه موشکی جمهوری اسلامی هم  مذاکره بشه
@News_Hut</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/news_hut/66728" target="_blank">📅 16:46 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66727">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VJJ7W47Bq-AKOz-xuSIpEJ3FHGuOuBsb6pT7c_9NFqp6CVwTKMV1FYmf66JXed36x5aoGM_8BfR-RB3FNviSC3KZNzmZHnfKMmH4ey6VeJRlnXcVjJu-uwtTew3F5nCzUydVLZNZbp8v2U7S9XNfS3-PFkHONzn-MSDoZ8FXGMbgFaEusRWR8M8a1PRyc9YZ9qrHa8fKV2dnknChOUG4t7cbsADm0UK3V7Ay22fVV6CqaGMPzKaSQSah-X5ugkT7H4-sl8OB6ZG2ykxU0Gg3acOKVDwg6DM5uSIjZ0oKVSLW8cRTjOly9vBcHBZp9OwwkBl86rqiIsvzy2Lc9Udnrg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
ورود عاشقانه مسعود به پاکستان
@News_Hut</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/news_hut/66727" target="_blank">📅 15:29 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66726">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dM4DKY2OfXD5WWzTZUFID658G8WHhPbChFEOHPQ9ooCZeKhjP5V_JiNgsnefWG-r_8dcxBD-09SRJxOYiLB8pPmgYRuLl__f8NoRIRczLjnczRzpkVCspmSA0MES8QdhH65evLA7Ca0MDTKRvFRvgrCTQQqq7UbK4G5LI3Tx3mL9Pm_el0sGvyH5qplygZPpEWPX6kHgSZUuUFDpoNoa7_VyZlJo3B4mAOEj9rMqFMs1ucK5F0SKhegnNM5r6oYsyV_9F17YpsjsW5_WR4PqfVqjPUK6snk-YQm93oaIUOOVenYcujXcA6IaSkC1bObZ7v1Efv-8H55_2iT_NN6_9A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🇺🇸
پرزیدنت ترامپ:
«با وجود اعتراض‌ها و اظهارات نادرست آن‌ها بر خلاف واقع، و همچنین هیاهوی مداوم رسانه‌های جعلی که تمام تلاش خود را می‌کنند تا پیروزی آمریکا را تا حد ممکن کوچک و بی‌اهمیت جلوه دهند، ایران به طور کامل و بدون هیچ ابهامی با بازرسی‌های هسته‌ای در بالاترین سطح و برای مدت بسیار طولانی در آینده (تا بی‌نهایت!!!) موافقت کرده است. این امر “صداقت هسته‌ای” را تضمین خواهد کرد.
اگر آن‌ها با این موضوع موافقت نمی‌کردند، دیگر هیچ مذاکره‌ای در کار نبود! بر اساس این توافق و دیگر امتیازات مهمی که ایران در حال ارائه آن‌هاست، من موافقت کرده‌ام که تنگه هرمز باز بماند و هیچ محاصره دریایی دیگری اعمال نشود.
با این حال، تمام کشتی‌ها در جای خود باقی خواهند ماند تا در صورت لزوم محاصره دوباره برقرار شود؛ هرچند در این مقطع چنین چیزی بسیار بعید به نظر می‌رسد.
پول‌ها و/یا منابعی که وزارت خزانه‌داری آمریکا آزاد می‌کند، در یک حساب امانی (Escrow) تحت کنترل ایالات متحده نگهداری خواهد شد و صرفاً برای خرید مواد غذایی و تجهیزات پزشکی از خود آمریکا استفاده خواهد شد؛ از جمله ذرت، گندم و سویا از کشاورزان بزرگ آمریکایی ما. ایران به شدت به این اقلام نیاز دارد.
این یک بحران انسانی است و من احساس می‌کنم که لازم است همین حالا کمک کنیم، پیش از آنکه خیلی دیر شود.
گفت‌وگوها به خوبی پیش می‌رود!
از توجه شما به این موضوع سپاسگزارم.»
@News_Hut</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/news_hut/66726" target="_blank">📅 15:01 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66725">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/70e35e4556.mp4?token=XSnYG7mSba_zZQrnSabTi7qabjJQQs3ix2pNyOKvGWAf4qSFx6WNoec4Nebev1onUZ80e3aUHJGuqNxYpTP7q0zRULdEoL3-ZAfVmzQ1wOVHkFKHHA76XfMCmJms1RPsV0ScJOC9zTb3NsoEKtfd_NoefERVePQnaPlFOEmUCIB_lM4cAsjoi9spXDlTIjEC1P7a8elwGFvutBRTBdrKGCq7NjoKRNKjKZoo62Ws0M46TVPKzFqgJIcXvY9F3rUfu3V0n_IWDAw5zWFHGM8KgZwJS75K3NfiLTeFU2S0mpa0mcol4Cjt3xJCaBEvXCucN8x-B5RlXGM0irHlectMpQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/70e35e4556.mp4?token=XSnYG7mSba_zZQrnSabTi7qabjJQQs3ix2pNyOKvGWAf4qSFx6WNoec4Nebev1onUZ80e3aUHJGuqNxYpTP7q0zRULdEoL3-ZAfVmzQ1wOVHkFKHHA76XfMCmJms1RPsV0ScJOC9zTb3NsoEKtfd_NoefERVePQnaPlFOEmUCIB_lM4cAsjoi9spXDlTIjEC1P7a8elwGFvutBRTBdrKGCq7NjoKRNKjKZoo62Ws0M46TVPKzFqgJIcXvY9F3rUfu3V0n_IWDAw5zWFHGM8KgZwJS75K3NfiLTeFU2S0mpa0mcol4Cjt3xJCaBEvXCucN8x-B5RlXGM0irHlectMpQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏
‼️
ارتش اسرائیل در نبطیه الفوقا به افرادی مسلح که در نزدیکی نیروهای این کشور شناسایی شده بودند حمله کرد. بر اساس گزارش‌ها، ۲ نفر کشته و ۲ نفر دیگر زخمی شدند. این نخستین حمله ارتش اسرائیل به لبنان پس از ۳ شبانه روز بدون هیچ حمله‌ای در این جبهه محسوب می‌شود.
@News_Hut</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/news_hut/66725" target="_blank">📅 14:11 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66723">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7f0020b71c.mp4?token=f8Xh1_ICz2TNboj66pvWZ9NXYUIry7y1DIH8tBslO-X8Q-hYLZIxGzPI2oXMs4yqfq52vxK8I8XuVownExxtSFbft9wv-KJPXHFv4v877trgDywpEgHdQsozZcxiz8ehRsRme3UieAs6jCjw5SR4tFVaPWWMmLRLQAJq1IwotpyGkYOE_m6rtE6wQ87xosW2KGBtqqeUgPsXXWbcleTodM6FeDNpuaSRvS24GatSwA31sPW4JkX0KpyjThFVU1SK4jLXZY4_lU8y63S21LswO6HPJx_paZwGUOkOtvbJn9RMEiSK76nFFRObDtMjdPu4vQWpb7gl1a16cBjzcYwekQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7f0020b71c.mp4?token=f8Xh1_ICz2TNboj66pvWZ9NXYUIry7y1DIH8tBslO-X8Q-hYLZIxGzPI2oXMs4yqfq52vxK8I8XuVownExxtSFbft9wv-KJPXHFv4v877trgDywpEgHdQsozZcxiz8ehRsRme3UieAs6jCjw5SR4tFVaPWWMmLRLQAJq1IwotpyGkYOE_m6rtE6wQ87xosW2KGBtqqeUgPsXXWbcleTodM6FeDNpuaSRvS24GatSwA31sPW4JkX0KpyjThFVU1SK4jLXZY4_lU8y63S21LswO6HPJx_paZwGUOkOtvbJn9RMEiSK76nFFRObDtMjdPu4vQWpb7gl1a16cBjzcYwekQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
اوکراین یک پل حیاتی را که به ارتش روسیه کمک می‌کند تا تدارکات را به نیروهای مبارز در منطقه اشغالی زاپوریژیا منتقل کند، تخریب کرده است.
@News_Hut</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/news_hut/66723" target="_blank">📅 13:52 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66721">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VFn1R7aoA0U4tywkoTuKEDxoU34t-BuugnKnuz7EEAi-n05v5pQtldK49qttLqNZTQYqkYNX0SpfF7yiwL9ka9wnif2ri3rUHtFJCZ5BvoJ-bs8VCN9UGUA8fE6DLt5r5QYQKStxnmk-ri_Mq9I6XP8cZYvbXOVNJS5IanV2BI_AlTHPoMDKpJI8cixH12J1ewSI7t9NQVS_LuaMPtH1kiwtN_0CY2Rwrb7LbqIZ0pOcaRhCDEEK9MQwlHCUiXSy8HIibxC1o-pg_J5nXmQ6uVPIVhOish9N7VRWM86cVuvnxTvTdk2rz-qpkW-dGodf7LsX48xIplCrouOZ_0Kxsw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
پزشکیان:
اثربخشی مذاکرات به پایبندی کامل به تعهدات توافق‌شده و اجرای دقیق آنها بستگی دارد. پیشرفت در این مسیر با پایبندی عملی به مسئولیت‌های پذیرفته‌شده سنجیده خواهد شد. اظهارات خارج از متن توافق‌شده کمکی به پیشرفت مذاکرات نمی‌کند.
@News_Hut</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/news_hut/66721" target="_blank">📅 13:38 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66720">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">1xbet_ir.apk</div>
  <div class="tg-doc-extra">53.8 MB</div>
</div>
<a href="https://t.me/news_hut/66720" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🔥
ورژن جدید اپلیکیشن وان ایکس بت بدون نیاز به فیلترشکن برای گوشی های آندروید
🎁
اپلیکیشن رو دانلود کردید موقع ثبت‌نام، کد هدیه 1x_1566529 رو وارد کن و تا
100یورو
هدیه بگیر!</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/news_hut/66720" target="_blank">📅 13:38 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66719">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/17bdf5f245.mp4?token=n_WG6mLXFY8Zu47D_BofLYT0dMpiiUOkG4VItSdPIVoHJXD_yyOWktuOtQo53xHbitVLE3JXlctbbJloDSwmPYsVOzP_zfRMezc1zUlth4brAsG83O6QfVmpC0PKoxjFXEX1nvJ0zVs03koIn3eKhT8GDFInbk6ZLKyMh9_zdUDnKL-HR7zUk--DuIM80n0uYZyClJspKjJmgkAX5l1C7VGXaRFJyyXGINFSk2HuR7mIDn0QaQvWZOeooCinNYb_llnBd9ZLz6Ra5pKeJ04B7Jq0ftpVar28bfFP2bPVobpbYLgbAow8UzdZIc_yl1owd8Bu4x2PDpcX-EU3wvQb6IWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/17bdf5f245.mp4?token=n_WG6mLXFY8Zu47D_BofLYT0dMpiiUOkG4VItSdPIVoHJXD_yyOWktuOtQo53xHbitVLE3JXlctbbJloDSwmPYsVOzP_zfRMezc1zUlth4brAsG83O6QfVmpC0PKoxjFXEX1nvJ0zVs03koIn3eKhT8GDFInbk6ZLKyMh9_zdUDnKL-HR7zUk--DuIM80n0uYZyClJspKjJmgkAX5l1C7VGXaRFJyyXGINFSk2HuR7mIDn0QaQvWZOeooCinNYb_llnBd9ZLz6Ra5pKeJ04B7Jq0ftpVar28bfFP2bPVobpbYLgbAow8UzdZIc_yl1owd8Bu4x2PDpcX-EU3wvQb6IWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
جام جهانی ۲۰۲۶ فقط یک تورنمنت نیست؛
جاییه که رویاها ساخته می‌شن، ستاره‌ها متولد می‌شن و تاریخ دوباره نوشته می‌شه…
🌍
⚽️
از نبرد غول‌های فوتبال تا شگفتی تیم‌های کوچک،
دنیا دوباره برای بزرگ‌ترین جشن فوتبال آماده می‌شه
🔥
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
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/news_hut/66719" target="_blank">📅 13:38 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66715">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a715ded5e6.mp4?token=rwr2QmGNJsl6ehh995QIG-bkgUyqe2x3Azx0aFxFf6JDpaGXg4IPk57CBOrp0szlCVb8ZLqRPoEhOmZ6NeKXIvXZa-A1cq03KAI0WUdcLxW3sch_h8hQ-PI_3UhNq9H55cRJ6MnlIGX6Y2BmNVava4kwVtnyhj_HhA6_VENMVioL-pXQ10GWkZNef1Tsmko83pH7qa0H16pw0T78gUi0ny03YBE2S8S3-SrWcnhddWmpRzd3T2O_Em0QU6n1DHPbi4MpeEVW8KCHlElXFU1R8N1U_83qz7NzRtK5Z0jDk2yNSQM0ukOuWVnt8EsjZlGAqw0kuFqDoMlOIXVrp08jQg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a715ded5e6.mp4?token=rwr2QmGNJsl6ehh995QIG-bkgUyqe2x3Azx0aFxFf6JDpaGXg4IPk57CBOrp0szlCVb8ZLqRPoEhOmZ6NeKXIvXZa-A1cq03KAI0WUdcLxW3sch_h8hQ-PI_3UhNq9H55cRJ6MnlIGX6Y2BmNVava4kwVtnyhj_HhA6_VENMVioL-pXQ10GWkZNef1Tsmko83pH7qa0H16pw0T78gUi0ny03YBE2S8S3-SrWcnhddWmpRzd3T2O_Em0QU6n1DHPbi4MpeEVW8KCHlElXFU1R8N1U_83qz7NzRtK5Z0jDk2yNSQM0ukOuWVnt8EsjZlGAqw0kuFqDoMlOIXVrp08jQg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
نخست‌وزیر قطر در گفت‌وگو با الجزیره:
این نخستین بار نیست که نخست‌وزیر اسرائیل با ادامه اشغالگری، گسترش حضور در مناطق لبنان و سوریه، خودداری از پایبندی به خروج از نوار غزه و همچنین عمل نکردن به تعهدات مربوط به توافق‌ها، موجب تشدید تنش در منطقه شده است.»
اقدامات دولت اسرائیل بارها به افزایش تنش‌ها و بی‌ثباتی در منطقه منجر شده و اجرای تعهدات و توافق‌های پیشین همچنان با چالش روبه‌رو است
@News_Hut</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/news_hut/66715" target="_blank">📅 12:03 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66714">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c71cf4b742.mp4?token=oTfAHXnswuOYGB2vN6WtGpNtj1YM9J-NH6Dt1eCGLcve9W-hQRkXKJASCc13DLO8U5myvZtT3Q5dI-KR1Vg5vLrAos-X8_mykhZ3Fz-Ct6PfUTFp6fy-_Uuwh28mMqpBFzR0ZYU0H86_5qXqFAUMqF3RHXg6yP0F__EdDCHVv8UfVwRfYT5QcJSTWYsjTfo9P0yRdbMhdnQF7qK85QHzoH9cihlWfVzHUphZ2XHIR-3El66S4hWTRv5T2oOqQyNYZ86jtFs_7jFpNmIbDKEI3J8GbUWqLvF5Ty8EU2ErS_16qz3v-MVOul5FlTf7NjoBKW3JmfKn1YGMTchinlgQWw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c71cf4b742.mp4?token=oTfAHXnswuOYGB2vN6WtGpNtj1YM9J-NH6Dt1eCGLcve9W-hQRkXKJASCc13DLO8U5myvZtT3Q5dI-KR1Vg5vLrAos-X8_mykhZ3Fz-Ct6PfUTFp6fy-_Uuwh28mMqpBFzR0ZYU0H86_5qXqFAUMqF3RHXg6yP0F__EdDCHVv8UfVwRfYT5QcJSTWYsjTfo9P0yRdbMhdnQF7qK85QHzoH9cihlWfVzHUphZ2XHIR-3El66S4hWTRv5T2oOqQyNYZ86jtFs_7jFpNmIbDKEI3J8GbUWqLvF5Ty8EU2ErS_16qz3v-MVOul5FlTf7NjoBKW3JmfKn1YGMTchinlgQWw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
رسایی:
قالیباف و سایر اعضای هیات رئیسه باید پاسخگوی چرایی تعطیلی مجلس باشند.
@News_Hut</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/news_hut/66714" target="_blank">📅 11:30 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66713">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/09d36c0712.mp4?token=NixxxvMQEu8gA6g40sK5m8OJxSp2Mq4zMz3YLe1fS6gCkNxS2Ofjv6Gp0nOSY9PHJRadU9Qt_ENV18vGhEZAAeyrX-6zjfR4rRPJCrcXi1sTpF6CTRaiF3Yv5cURrpJEbaYou8lZhAIxHWEzS9XcD8g0HPkRL8Zq2imPPWHJL7h7mCQ62P1PGNqWrR5I2uXCzeBjOhorQFGOYFa9ZXHcOlD2sb0lMKoC-M47Ft6cppghDQcHQE7m6sIvyYNCeyxX8nmEzisIBCz-wGS7WHB4WiqYTQqWmTKQP4bGicrYMlQhLQQCb2tpJiCXW2iYmixjPaZUP5kFofKI0vkAFUWTVg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/09d36c0712.mp4?token=NixxxvMQEu8gA6g40sK5m8OJxSp2Mq4zMz3YLe1fS6gCkNxS2Ofjv6Gp0nOSY9PHJRadU9Qt_ENV18vGhEZAAeyrX-6zjfR4rRPJCrcXi1sTpF6CTRaiF3Yv5cURrpJEbaYou8lZhAIxHWEzS9XcD8g0HPkRL8Zq2imPPWHJL7h7mCQ62P1PGNqWrR5I2uXCzeBjOhorQFGOYFa9ZXHcOlD2sb0lMKoC-M47Ft6cppghDQcHQE7m6sIvyYNCeyxX8nmEzisIBCz-wGS7WHB4WiqYTQqWmTKQP4bGicrYMlQhLQQCb2tpJiCXW2iYmixjPaZUP5kFofKI0vkAFUWTVg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
حضور سر زده ناپلئون بناپارت و درگیری شدید با شیر تعزیه
😂
😂
😂
@News_Hut</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/news_hut/66713" target="_blank">📅 11:00 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66712">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/312bd6815a.mp4?token=F6OM4Yy58wqI2pRKcDEttBHe9HyiTGB3KOO8iCy2pGIWrGRINWXrbSIcN9Uv8pX8hJn_prxsv92Im_7jX_nyWMkcoEOnS_36fv-nbgHBDnbtNk5p30lr_tr3PallmkUGuRYtQA_iK94YnLGKmEIge8mKamozc7byjy7ziFyISdHNqESh3HPMTFS8xGySN76jPYp5KuaWInRqdl74ZDZCayswDjxGg1lz_gMbiAjolbJRsCVwAQKCGD39VOlPE1OAo8Ye8uLVYSNque1OggK-e_NFgEGzojnDksWUtf6v18pubPLj9MBT-Zb8Z240NPZLk6v7mDIvbkaBUXxDOjqVHA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/312bd6815a.mp4?token=F6OM4Yy58wqI2pRKcDEttBHe9HyiTGB3KOO8iCy2pGIWrGRINWXrbSIcN9Uv8pX8hJn_prxsv92Im_7jX_nyWMkcoEOnS_36fv-nbgHBDnbtNk5p30lr_tr3PallmkUGuRYtQA_iK94YnLGKmEIge8mKamozc7byjy7ziFyISdHNqESh3HPMTFS8xGySN76jPYp5KuaWInRqdl74ZDZCayswDjxGg1lz_gMbiAjolbJRsCVwAQKCGD39VOlPE1OAo8Ye8uLVYSNque1OggK-e_NFgEGzojnDksWUtf6v18pubPLj9MBT-Zb8Z240NPZLk6v7mDIvbkaBUXxDOjqVHA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
کریس رایت وزیر انرژی آمریکا: آلبرت اینشتن ۱۲۰ سال پیش مقاله ای منتشر کرد که...
🔴
ترامپ: برای هیچ کس اهمیت نداره
😂
🔴
کریس رایت: به نکته خوبی اشاره کردین قربان
.
🤣
🤣
@News_Hut</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/news_hut/66712" target="_blank">📅 10:32 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66711">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0082fda5e1.mp4?token=A2fLMifaX1Xm5ftt4YhaATU9deUnawdbTHtll5QkJgcU1KURriAhzvFaw_2uXPICEdS04P26p1ScFVAMzEX_hT1632y0XGrb4kr7YwXWxY-HsMy2yrjzoypF9k0NkLxevzpgjxGN3bzw_mBgZnf-DsN_5e5lFEpvftuEQdsyj8drUXenXMZlVG8qeR-TtIbq1DGElKTPymOV1VeCcF1EqJ5Way8_vtOp1RRSxEkfJcj96HgyBylATb7on8yjBrsOdk9gcnJ3B049-_GW5nyunkAlkN4afjKjF3Jt0KD78NRrqz2fnVpIjKM7JFBrUJlXRWD50wWLRxUmJxpxkfZDgjD_UFnEHbIFa7L0b_oVRCass1tPkEzxYQoOjGbB4Whq_Vxo3f9cLGazURDRwcSsIDeBUoNjho8N8qYlAqKotENLacI4ZVb1U9f3jKJS3Depfu1M-IR8UYNnwaKJFEBYTGsAeUWo0ZFbImZSfZ6ieUYQJwj0Fn87UIbfgfKGzZr_TfQNt-oNwEQSGcPuUT2A4cwjVlDI_PaDpIyPE5bTaGjExD2Vb09scuMVcSns61R0uZEh9GRucQjtTfKo76A0poJJRmWTreti-Kmu78o4VjNn9L_tRRKS9GatGNOgY8257kSX_MnoHdcWTk90cLxCnB2a-y9LU5cjXUycXIssaWY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0082fda5e1.mp4?token=A2fLMifaX1Xm5ftt4YhaATU9deUnawdbTHtll5QkJgcU1KURriAhzvFaw_2uXPICEdS04P26p1ScFVAMzEX_hT1632y0XGrb4kr7YwXWxY-HsMy2yrjzoypF9k0NkLxevzpgjxGN3bzw_mBgZnf-DsN_5e5lFEpvftuEQdsyj8drUXenXMZlVG8qeR-TtIbq1DGElKTPymOV1VeCcF1EqJ5Way8_vtOp1RRSxEkfJcj96HgyBylATb7on8yjBrsOdk9gcnJ3B049-_GW5nyunkAlkN4afjKjF3Jt0KD78NRrqz2fnVpIjKM7JFBrUJlXRWD50wWLRxUmJxpxkfZDgjD_UFnEHbIFa7L0b_oVRCass1tPkEzxYQoOjGbB4Whq_Vxo3f9cLGazURDRwcSsIDeBUoNjho8N8qYlAqKotENLacI4ZVb1U9f3jKJS3Depfu1M-IR8UYNnwaKJFEBYTGsAeUWo0ZFbImZSfZ6ieUYQJwj0Fn87UIbfgfKGzZr_TfQNt-oNwEQSGcPuUT2A4cwjVlDI_PaDpIyPE5bTaGjExD2Vb09scuMVcSns61R0uZEh9GRucQjtTfKo76A0poJJRmWTreti-Kmu78o4VjNn9L_tRRKS9GatGNOgY8257kSX_MnoHdcWTk90cLxCnB2a-y9LU5cjXUycXIssaWY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
خبرنگار:
دیروز یه لحظه بود که عراقچی وارد اتاق شد و به شما سلام نکرد. شما هم دست ندادید و بعدش رفت. آیا احساس کردید که به شما بی‌احترامی شده؟
🔴
جی دی ونس :
نه... باور کن، من چند ماه اخیر رو خیلی با ایرانی‌ها سر و کار داشتم. بعضی وقت‌ها واقعا برام گیج‌کننده‌ان به عنوان مذاکره‌کننده
@News_Hut</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/news_hut/66711" target="_blank">📅 10:02 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66710">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b3a355cf81.mp4?token=pREACt7xyqPLDE0UDbKjkLKlE5xEEE9YyquXcjGt_f7WbosBppb8DVzDkERroGaeukx8LSe0uqOrlapExG8IBFWM7oI_ZPOGR9hj2HwrIecifCyyMZjtNOeETEQdbNbgo30V4OJ7xidsTFWTEj8G8tXoKnOnuVMNL3bRhUN5L0fbGHazxsIsnuy2zse5-opzq0STiSSdFtOXLuocuXyw4UjcQ9Y3b0WzWHbfgbAQmJHv9ybEStiXV6-VBd0X3tB9_LPbT6khX-NdFHw9eEAUiRLBiWawlXwezSeNaE4VUec8_UpT2v9AnizaZDl_f98mZJ1rg5zwLHNU7di9nU1iAQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b3a355cf81.mp4?token=pREACt7xyqPLDE0UDbKjkLKlE5xEEE9YyquXcjGt_f7WbosBppb8DVzDkERroGaeukx8LSe0uqOrlapExG8IBFWM7oI_ZPOGR9hj2HwrIecifCyyMZjtNOeETEQdbNbgo30V4OJ7xidsTFWTEj8G8tXoKnOnuVMNL3bRhUN5L0fbGHazxsIsnuy2zse5-opzq0STiSSdFtOXLuocuXyw4UjcQ9Y3b0WzWHbfgbAQmJHv9ybEStiXV6-VBd0X3tB9_LPbT6khX-NdFHw9eEAUiRLBiWawlXwezSeNaE4VUec8_UpT2v9AnizaZDl_f98mZJ1rg5zwLHNU7di9nU1iAQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
شهبازی، مجری مفعول صداوسیما:
طبق تفاهم جمهوری اسلامی و آمریکا؛ از این به بعد شعار «مرگ بر آمریکا» ممنوعه و اگر کسی اینکار رو بکنه دستگیر میشه.
@News_Hut</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/news_hut/66710" target="_blank">📅 09:34 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66709">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7ce9206e1d.mp4?token=RVYqCLZq7PimtI1OVSreht88As8wlfjjvtfARssSMm4ak2zOaQvuHowbwY7V1qbeUfv5Ghy-6EqUgbxoFSheHMBeu2yx3OWsXD6KC2vpQoKxHa85l4S5vOVDWraNJfxD1ujFabUqbtywoC57b7C22alq2S1Be3s32MKIARw-N5TjclyUmFE5Jhz9o1sEe8GNw75rawfsWhEH7v8uUS4ttAP4e5Yks7-qkUNs9tVuj2VCeD4nUndogGli5L_5WKE7CrQWpdNYLqGXQSLFerE-jUJfPfsK09cH60NY4eobkzR6Zf6fLOvhwi28rddUaeXrNBFwwz-Kkqye1Z-QZ7hmgw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7ce9206e1d.mp4?token=RVYqCLZq7PimtI1OVSreht88As8wlfjjvtfARssSMm4ak2zOaQvuHowbwY7V1qbeUfv5Ghy-6EqUgbxoFSheHMBeu2yx3OWsXD6KC2vpQoKxHa85l4S5vOVDWraNJfxD1ujFabUqbtywoC57b7C22alq2S1Be3s32MKIARw-N5TjclyUmFE5Jhz9o1sEe8GNw75rawfsWhEH7v8uUS4ttAP4e5Yks7-qkUNs9tVuj2VCeD4nUndogGli5L_5WKE7CrQWpdNYLqGXQSLFerE-jUJfPfsK09cH60NY4eobkzR6Zf6fLOvhwi28rddUaeXrNBFwwz-Kkqye1Z-QZ7hmgw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
قالیباف:
ما هرگز نمی‌خواهیم با آمریکایی‌ها در یک قاب باشیم
میانجی‌ها خیلی اصرار داشتند و ماهم گفتیم در آن قاب حاضر نمی‌شویم و ما فقط برای مذاکره می‌آییم.
@News_Hut</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/news_hut/66709" target="_blank">📅 09:00 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66708">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">فک کنم اگه هرشب با ۱۰۰ هزار تومن میومدین چنل بت ما ، شبی بالای ۲ میلیون سود کرده بودین مثل دیشب:)
😊
😂
میگی ن ؟ بیا تو چنلمون و ببین
🔥
@FutballFuckBet @FutballFuckBet @FutballFuckBet @FutballFuckBet</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/news_hut/66708" target="_blank">📅 02:52 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66707">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/X6AS-gZBrfpQeSdpEopre9OsC-WBlhaxTIWAIYTpPbhzOT51zIXBvvPpwh8gxwtkUbX_ngdCoi8--o2vzDutUyAqwVtJBEdI6gxdnSPRcHzfT7EqPd-Pg5IGTps8dHjwY_LlLXh3SDgUycsrPIFW9jLUlNR4OGMXgCyyLiLDW0dsT35w4uWJ_fIui_8ouFqn7QbmkQpdPI2-uFhLEjHdpXGkC-8UdLPEEGOFIHyXC1VPsa3XL_pl39sSCDn0fn3n6LXWTIuwD6vm8mBdBmFr8-furZUGZ1TiFs4nULVbibLRxB6OGGJkpHs8h1AWVhzkz5KXqRF72nHSppLLv39OaQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فک کنم اگه هرشب با ۱۰۰ هزار تومن میومدین چنل بت ما ، شبی بالای ۲ میلیون سود کرده بودین مثل دیشب:)
😊
😂
میگی ن ؟ بیا تو چنلمون و ببین
🔥
@FutballFuckBet
@FutballFuckBet
@FutballFuckBet
@FutballFuckBet</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/news_hut/66707" target="_blank">📅 02:52 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66706">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/299b9a2567.mp4?token=iDOHaYHPRU09xZlMTtMBx1Uli8AaRio5K5HTmE0RDBxRZGswa4yY7DgZaSaCDxMr-XbOYsBgIT3NjE4CdGJnW2aJWxMqzXOzjZSnAk39q9AgoyRxNDk8z-eqXX9HjCi-onpMqPu51JTHVKELpFiyoVBaAbmY4RUpyAOWgbJL0tPXudZ_71OYqfYqHqWymYz_N8T3KCvciWvwXqP-55ZSxqTpXjq2ZF6XTyY7CkMW8EFbefizycT1SC1nKpy_m_2yENjhkUcOGA2EhMCa8ue5Smd-tTK-OX0TXSyH_9H0fuMhBSzO_z0_haVg-6QxGFVg4uAQweGiX-yLOlaA6dg3cg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/299b9a2567.mp4?token=iDOHaYHPRU09xZlMTtMBx1Uli8AaRio5K5HTmE0RDBxRZGswa4yY7DgZaSaCDxMr-XbOYsBgIT3NjE4CdGJnW2aJWxMqzXOzjZSnAk39q9AgoyRxNDk8z-eqXX9HjCi-onpMqPu51JTHVKELpFiyoVBaAbmY4RUpyAOWgbJL0tPXudZ_71OYqfYqHqWymYz_N8T3KCvciWvwXqP-55ZSxqTpXjq2ZF6XTyY7CkMW8EFbefizycT1SC1nKpy_m_2yENjhkUcOGA2EhMCa8ue5Smd-tTK-OX0TXSyH_9H0fuMhBSzO_z0_haVg-6QxGFVg4uAQweGiX-yLOlaA6dg3cg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🇺🇸
پرزیدنت‏ترامپ:
پولی که از حالت مسدود خارج می‌شود برای خرید غذا استفاده خواهد شد و غذا منحصراً از طریق ایالات متحده از کشاورزان ما خریداری خواهد شد.
@News_Hut</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/news_hut/66706" target="_blank">📅 01:39 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66705">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/91eda4547b.mp4?token=oAhNY3n9bYnpS_zPaGARs3EVhVKKkZCa_CP8jNR9BQXgU0RGXCP1mFgZ1DtckvwtqCpOKDV6K2jrpgZS4dgsQLvkl8p6aNYIccGxzwYXPiQItjlhMibUf0_qy7jLBT5-EjPDKPoLuEqUm8f4Bur4iJcWT28JJo2jxKwPga0Xgqes8XM-bq9J6WhHVJvdobFDwF2UgJiMgkABtUOGLGYTWCoewluiuJfyjY8r4xoarBo63bFGrwEowLYSNPae1gjVbe0lJW1GDK6PqTmmOKPpLDknbkIlP57FFuiS0GmzNipXiLxt840mREyy_JJOa2EKTjsH_J1Q-Ri5B5z2j5_7YA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/91eda4547b.mp4?token=oAhNY3n9bYnpS_zPaGARs3EVhVKKkZCa_CP8jNR9BQXgU0RGXCP1mFgZ1DtckvwtqCpOKDV6K2jrpgZS4dgsQLvkl8p6aNYIccGxzwYXPiQItjlhMibUf0_qy7jLBT5-EjPDKPoLuEqUm8f4Bur4iJcWT28JJo2jxKwPga0Xgqes8XM-bq9J6WhHVJvdobFDwF2UgJiMgkABtUOGLGYTWCoewluiuJfyjY8r4xoarBo63bFGrwEowLYSNPae1gjVbe0lJW1GDK6PqTmmOKPpLDknbkIlP57FFuiS0GmzNipXiLxt840mREyy_JJOa2EKTjsH_J1Q-Ri5B5z2j5_7YA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
‏خبرنگار: وزارت خزانه‌داری امروز تحریم‌های نفتی ایران را لغو کرد؟
ترامپ: خب، من باید دقیقاً وضعیت را بفهمم. تمام آن پول به صورت خرید مواد غذایی برمی‌گردد. آنها ۹۱ میلیون نفر جمعیت دارند که نمی‌توانند آنها را سیر کنند.
خبرنگار: مطمئنی ایرانی‌ها از سود حاصل از فروش نفت برای بازسازی ارتش خود استفاده نمی‌کنند؟
ترامپ: قرار نیست آنها این کار را انجام دهند.
@News_Hut</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/news_hut/66705" target="_blank">📅 01:34 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66704">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RUnrG1XI3vQBYP6QjLxyIbqki5oVS6V6MClixmvKWjSLvzscJkUwZGLjHyLeQ9CBQuc88uAreSCQXigTZiikIGYsAJEHQV6d-P9uhxUEkEMjT1MBe_MRqbF0nfcnmoCLrOeV48FGqaM-YAsaAgI18eIFgZQfRmEWfCHAl5JIZTGDTt5ehCciV-sJq3yXfFUCluiqPnoPT7oAq6LZtPAtp8jflo3OAv-j-vhOSn4dYtfyW2-9Rz63LwOUqqLD00snvXiXNOOvrISPCM2YkShacIVnntoAUxmCmToSBR8gHCGjA2HhfAWGXsdY8Bdw5IJGANQWpv-wswEgmiIw9sJqKQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
قالیباف: اگر به سوئیس نمی‌رفتیم خون بیشتری از شیعیان لبنان ریخته می‌شد
@News_Hut</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/news_hut/66704" target="_blank">📅 00:49 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66703">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e034e891cb.mp4?token=kZyV9DF6QDYIkTF6Lg_QtYa8tZqgoPlrBK-8gD1ltabKYZOJTiCoSOk5yFxYqNiFXoqYAgPjmuveaKQQrkoV-tf2cre2cMu4GNy9hG7dlu7xoBWPfx8IwKAjzMo-nuZp78aoMDfq_uK09jvBavBFAHMNZsou8T5FYbSK4koUxvgu5D6JyQSTZ1XNAstYbliVtJXpmNDaPaOJnFt8mrYtgsnqf2ZSnl6H5GfX5p9WfzbMb2BEPAO5n2M9xQzJJ7EfnxAqqSMmQA10LywjHbP7Wyu3jM3rKma6BQLriXEukdW_lDXyUZJdryFdz0hNXlMDT_IuHAdUr9enF5L-UIPTpQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e034e891cb.mp4?token=kZyV9DF6QDYIkTF6Lg_QtYa8tZqgoPlrBK-8gD1ltabKYZOJTiCoSOk5yFxYqNiFXoqYAgPjmuveaKQQrkoV-tf2cre2cMu4GNy9hG7dlu7xoBWPfx8IwKAjzMo-nuZp78aoMDfq_uK09jvBavBFAHMNZsou8T5FYbSK4koUxvgu5D6JyQSTZ1XNAstYbliVtJXpmNDaPaOJnFt8mrYtgsnqf2ZSnl6H5GfX5p9WfzbMb2BEPAO5n2M9xQzJJ7EfnxAqqSMmQA10LywjHbP7Wyu3jM3rKma6BQLriXEukdW_lDXyUZJdryFdz0hNXlMDT_IuHAdUr9enF5L-UIPTpQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
‏قالیباف:
به خواست خدا، حاکمیت ملی لبنان بر کل قلمرو خود در این مذاکرات به یک راه‌حل نهایی خواهد رسید و تا زمانی که این اتفاق نیفتد، ما آنها را رها نخواهیم کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/news_hut/66703" target="_blank">📅 00:08 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66702">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/acf0726b2f.mp4?token=NYiwC18f4StKDzkTOuQsuDNWttMo6z2j_3p1e8bNCM7yjQvyp7Eh47UPfNode9v46jV31jcnHEraF53kKXwkwqEgTbzEIrWIz_8EMLZsOVXal26QQqvUR2n-v2McvFq_F0Ki7xtGQgCr6BrVPThzwiSnOVcYTPloXQtMXesKRq1TxJTb0EEpUO5_HnHKzuCcKVi_0bOXjcCypLTXnJgKFzVdPsjYQPkvhczzNt2a8Vn0kncEryM1fXreOxvhZ28RpOk1WdcRdTWg48UH3-Ob_lF_emomJZ7ozSDgcTjppBHg573ZRopflCsIi2spKXLFdXEmqumi-g7MpQzG_FKS-w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/acf0726b2f.mp4?token=NYiwC18f4StKDzkTOuQsuDNWttMo6z2j_3p1e8bNCM7yjQvyp7Eh47UPfNode9v46jV31jcnHEraF53kKXwkwqEgTbzEIrWIz_8EMLZsOVXal26QQqvUR2n-v2McvFq_F0Ki7xtGQgCr6BrVPThzwiSnOVcYTPloXQtMXesKRq1TxJTb0EEpUO5_HnHKzuCcKVi_0bOXjcCypLTXnJgKFzVdPsjYQPkvhczzNt2a8Vn0kncEryM1fXreOxvhZ28RpOk1WdcRdTWg48UH3-Ob_lF_emomJZ7ozSDgcTjppBHg573ZRopflCsIi2spKXLFdXEmqumi-g7MpQzG_FKS-w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
حضور تانکهای مرکاوا اسرائیل در حومه نبطیه
@News_Hut</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/news_hut/66702" target="_blank">📅 23:30 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66701">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/146941c66e.mp4?token=jhrZioCuoWHQqttP1wxtd1nB8aIwQaot3LX0UkWouaG_5xsWwmNnVCbrc9AFC8-8oVaoqcRecA9GF7VrHLeyRxKP4zBL5OzRhCntR50__zHftmFYXOlXjlRNZezSC7au-_VLGfQS8TW0MGz5yTBLaBxzQyI4BSMLnVuZ9k4usT84fd-vAyT1PVtK3KZjZH106heVc48IP-YCBY_JiPrCwREzhOzz0eSYH1aeix3rd1bLGRnCzhT4ZES5-gKr8OQZUYWpWVMU1pdDDhOXhi8MdFebDBq-69eWydcIgHlP8bmhJNYEJo9nYM2NntbkFzczGn0qkD5YYWF9MwGT8C_7DA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/146941c66e.mp4?token=jhrZioCuoWHQqttP1wxtd1nB8aIwQaot3LX0UkWouaG_5xsWwmNnVCbrc9AFC8-8oVaoqcRecA9GF7VrHLeyRxKP4zBL5OzRhCntR50__zHftmFYXOlXjlRNZezSC7au-_VLGfQS8TW0MGz5yTBLaBxzQyI4BSMLnVuZ9k4usT84fd-vAyT1PVtK3KZjZH106heVc48IP-YCBY_JiPrCwREzhOzz0eSYH1aeix3rd1bLGRnCzhT4ZES5-gKr8OQZUYWpWVMU1pdDDhOXhi8MdFebDBq-69eWydcIgHlP8bmhJNYEJo9nYM2NntbkFzczGn0qkD5YYWF9MwGT8C_7DA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
اعتراف
کارشناس صداوسیما: نتانیاهو خسته نشده،این یعنی مرد»
@News_Hut</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/news_hut/66701" target="_blank">📅 23:03 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66700">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ff06705953.mp4?token=AQQlbv_WdyjIkjrYzmsuf477ypbXhXyZt7_lw6dp-SZBJFxdeATLWZyxD8fgSPZkDqjdNmtg5_m4A0SIw3p_xxs-OlvelOEfXWapxc1l7lT24zkymjIYPIBtaqh6-LJfU-X8Gfc6iBll4ceDSUx3wT-DjT9TVRL_Ka4R55Xz5JhIppHUeB-ja-pjZsbM-0t7HG7rNttqn7mo8FHtQVVrjsjoYoaYhEuoaQWdY4Q1t4syzavdt_6TU1KBpdeCwAEr1-3OO2XCrfdeKRY55WD3dokfn8el5VWbDuXxfETPDbwsjZ94pD-F6GV1syGG5-TRciM8uLE7FYnkQroVc7z9Bw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ff06705953.mp4?token=AQQlbv_WdyjIkjrYzmsuf477ypbXhXyZt7_lw6dp-SZBJFxdeATLWZyxD8fgSPZkDqjdNmtg5_m4A0SIw3p_xxs-OlvelOEfXWapxc1l7lT24zkymjIYPIBtaqh6-LJfU-X8Gfc6iBll4ceDSUx3wT-DjT9TVRL_Ka4R55Xz5JhIppHUeB-ja-pjZsbM-0t7HG7rNttqn7mo8FHtQVVrjsjoYoaYhEuoaQWdY4Q1t4syzavdt_6TU1KBpdeCwAEr1-3OO2XCrfdeKRY55WD3dokfn8el5VWbDuXxfETPDbwsjZ94pD-F6GV1syGG5-TRciM8uLE7FYnkQroVc7z9Bw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
‏اوکراین یک کارخانه تولید تجهیزات الکترونیکی نظامی و واحدهای تأمین انرژی سامانه های موشکی و راداری روسیه را در شهر ورونژ در جنوب غربی روسیه با موشک های بالیستیک هدف قرار داد.
@News_Hut</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/news_hut/66700" target="_blank">📅 22:33 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66699">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ee51609a91.mp4?token=L9K0Hq69pDmwiIT6FS77kcJ4tAJ4QAXNXwgh7NcYuNbvuSBZAACM_4lsPxGZO9sOrgeX6ZRoXEqlDeOaq09iKTD1n3Mwl7A1TG_SVjpmmWPL94ih7Bw-TnD7q1eS9bSbkfKS8N-Yv_C8jONREYXSwPm2-Zn6wYINppWfWM9HIEWXqq3T6_qEmpTbxOT4oxFgeyKkLjHvlR9uJPIjyK_e-e5Rg-qyqyfR7TvVybyP6NF0zxWL58oUs0DKnNfXEK8QHjEIY_V4jJhX4OJb6xHk8DWlInDMNKg73BhrOVG_gKb_anv6er3xKa2-BRtUly_z-0qkW6M6cMj0hIWTLg3WWw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ee51609a91.mp4?token=L9K0Hq69pDmwiIT6FS77kcJ4tAJ4QAXNXwgh7NcYuNbvuSBZAACM_4lsPxGZO9sOrgeX6ZRoXEqlDeOaq09iKTD1n3Mwl7A1TG_SVjpmmWPL94ih7Bw-TnD7q1eS9bSbkfKS8N-Yv_C8jONREYXSwPm2-Zn6wYINppWfWM9HIEWXqq3T6_qEmpTbxOT4oxFgeyKkLjHvlR9uJPIjyK_e-e5Rg-qyqyfR7TvVybyP6NF0zxWL58oUs0DKnNfXEK8QHjEIY_V4jJhX4OJb6xHk8DWlInDMNKg73BhrOVG_gKb_anv6er3xKa2-BRtUly_z-0qkW6M6cMj0hIWTLg3WWw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
کارشناس صداوسیما:
نه تنها از کشتی ها در این شصت روز عوارض نمیگیریم بلکه قراره آمریکایی ها بعد شصت روز بیان و عوارض بگیرن.
@News_Hut</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/news_hut/66699" target="_blank">📅 22:04 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66698">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PC5T-U2SSMWZ30LPNeVto0vFgJPAg4p-FK3mhM92v8n09CKhlrOLuou8YNVbOFFh32BQaqJpKl_ohiTcL0q4xH-xqEs-UCbDJmGViCD7WpdJP0wmc7Sld3jqQteHCzc0UwU01zLoI3S7LxCw1elqT2FXj7M5GMJm2b6A-7jrkK3p70LEgF6ZuKcfgogDu3Wp9pebWy1BELmaGyHldAxqIHsyhTYeuVyEe-YUYCiJBtY9ETO2l_TjS1xUgGulUh5rBQOz2TiBN4RiFoi7LJFyMS4YnV7Zyi_Yxw4wrb1I9FlIqaNt7M9HMML1FlVSUYBb0CPQV7oxvadrrAUXcciYuQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
باراک راوید:
وزارت امور خارجه آمریکا تایید کرد مارکو روبیو از ۲۳تا۲۵ژوئن به امارات، کویت و بحرین سفر خواهد کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/news_hut/66698" target="_blank">📅 21:34 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66697">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/K9do-Jn6wUuvC_aQwGNp_iOLUx-3BAkz_8cUy4JCZ23nM5ak7hWataJCFm4EpEAL5UiUmaLNUOQabJh6PXgmnzEzPWz3XpQZCsVwwB1hdAWJQ6_ckAOLwVIhDrH6KNw3k0G93PBZsTVShXeCm_qJK8b_Gjf3lJ1BWsVmN4aE4gRTIUx2cNMRe8YJUl2S6Euxnc-Ge5Z8AD1itKW0HqL7v60HsM1lG6FhTINxg06dxt9d82rifDrKx4AYqzkV94vCiP8KXRwojdJ4VdhrS35KBxemORhgM1E5ikC26iOhkI0iBhnSen9jRwPcThshBFYaubBzFhp1IuFM4PyorZO6Yw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🇺🇸
پرزیدنت ترامپ:
همه کاملاً آگاه هستند که ایران با بازرسی‌های عمده تسلیحاتی موافقت خواهد کرد تا «صداقت هسته‌ای» در آینده طولانی تضمین شود. رئیس جمهور دونالد جی. ترامپ
@News_Hut</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/news_hut/66697" target="_blank">📅 20:34 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66696">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ok8DVcLwljf4pMbGn0TTCQHdonHE7kuM_Cp5HDQ-M4QixFZuKBARhnd-QEqiM2USeQZUECcjmdis7wrDBzxszEsVneuRVrB58AxVeFD4f_qfruWWCV_ezDbIOllNZhgFBC1dqT7ZYdtRaKC1oKCzchFJK9W50QzJNOqcWJTXy9vt8lb6obomd3rqOrGrKDkIuOvGJDXPFvNkwdOT_m2QN44ZdaOegYRCoSSJTEJLfXbrIEAqgvjzkX_oadnVhsN1IVgNbSztRpModMbnEFg0XDXpRTuY0rQw89CTVlPhPMcwiM4d1iHeCIop0wDo-gWpnYGoyAmKeKLIwfXbcqfJ-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
‏رجا نیوز:
در حالی که جریان رسانه‌ای حامی تفاهم‌نامه اسلام‌آباد تلاش می‌کند آن را یک دستاورد تاریخی معرفی کند، اظهارات «جی‌دی ونس»، پرده از ابعاد فاجعه‌بار و تحقیرآمیز این سند بر‌می‌دارد.
سخنان ونس نشان می‌دهد آنچه به نام «آزادسازی دارایی‌ها» به ملت ایران وعده داده شده، در عمل یک سازوکار استعماری و نسخه به‌روزشده همان طرح «نفت در برابر غذا» است که این بار قرار است عزت ملی را به گروگان بگیرد.
ونس با بی‌شرمی تمام، مکانیزم طراحی‌شده را اینگونه تشریح می‌کند: «اگر هر کدام از دارایی‌های مسدودشدهٔ ایران آزاد شود، ما روی آن حق تأیید و نظارت داریم، قطری‌ها هم حق تأیید دارند... سپس آن پول عملاً صرف خرید سویا، ذرت و گندم آمریکایی خواهد شد.» او با وقاحت می‌گوید با این پول قرار است جیب کشاورزان آمریکایی پر شود.
مشخص نیست این توافق چه نسبتی با پیروزی‌های خیره‌کننده ایران اسلامی در میدان نبرد دارد؟ آیا خون شهیدان میدان، باید پای میز مذاکره با وعده «سویای آمریکایی» معامله شود؟ آقایان مذاکره‌کننده با چه منطقی پذیرفته‌اند که حق حاکمیت ملی بر دارایی‌های خود را به «حق وتو» و «نظارت» آمریکا و واسطه‌ها واگذار کنند؟
@News_Hut</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/news_hut/66696" target="_blank">📅 20:15 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66695">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">1xbet_ir.apk</div>
  <div class="tg-doc-extra">53.8 MB</div>
</div>
<a href="https://t.me/news_hut/66695" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🔥
ورژن جدید اپلیکیشن وان ایکس بت بدون نیاز به فیلترشکن برای گوشی های آندروید
🎁
اپلیکیشن رو دانلود کردید موقع ثبت‌نام، کد هدیه 1x_1566529 رو وارد کن و تا
100یورو
هدیه بگیر!</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/news_hut/66695" target="_blank">📅 20:15 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66694">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Xds5cEL6uu40TAjV-OLg9pJQRMhhMMUePI7MdLLqQqst74FhpDT0l1PogM36OMeERfRHxKpztXqlWTXQ6l8P0C0Zz5NKncIhWfFBM1v4Bsh7C_3MG4nST-1F4slL9yeM9y1o3pBH01XP_afgAxBXmOgieNq-djCCdgDt1SRR169-js2vCZOwYtbSyKc9D44rCMK6K5E1pQacu44rYmMV7qSY1tMG0CXtrfK6yjDw1ovYRSIw86cTR0k1RAkcf4LSZJxOeQH6vgttMkifKwSVyv7e7D27sKxrb77AJ9qm7mNDlwc0ODhaXgfAC3JXrZnSkiF1u29yoOeBN9adcmAN7A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏐
پرومو بزرگ والیبال Ace Arena با جوایز تا 5000€
🔥
🎁
جوایز اصلی هر مرحله:
📱
آیفون 17 پرومکس
🎮
PS5 و Xbox Series S
💻
مک‌بوک پرو M5
⌚️
اپل واچ سری 11
🎧
ایرپاد پرو و هدفون سونی
🎟
کد تخفیف تا 50€
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
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/news_hut/66694" target="_blank">📅 20:15 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66693">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sFBla7GMJjI4hS4V-1mm98EZJgxMpvATSS-agKT_BbRZ48VHe2uqfmQ9205YFk6lSPSB3a4rg7z6t-5_t1e2wjhM5lrogwfrnr0Nwkukry8buYabixDsUpJjIJoSVed15VtAiZ6TetwUhZ4yfkgtBbX_-GU0H-J6e_fKJNQZoWT82xqFZ687a5sBTZHj54M0MduwTw9sfUIAlBFGyERLpk4fDlceAuv5yo7Ik8Y0nJAuuL7torZQm9LXxqeTLNU2WeCU2lq1fmsqCZ-QnkC6D3MBDEBK0ubElQ8cIFUbb_uPosSsA9WISlkO2eEt-ak7-MSkf8xrc3v0fYODa0LkhA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
مرندی:
ایران قصد خرید کالاهای کشاورزی آمریکایی را ندارد و دیروز هیچ بحثی در مورد آمدن بازرسان آژانس بین‌المللی انرژی اتمی به ایران صورت نگرفت. تبلیغات غربی را نادیده بگیرید.
@News_Hut</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/news_hut/66693" target="_blank">📅 19:53 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66692">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f18d416253.mp4?token=dpMWSsbMDm-63AD8WP9QpzqhdSjlvUAtu8V_wkp87SEY0OAOzOwg_LNJsBjR0ZvbGBHkEmxfex74lPJYoti0qYuDtNdrsfep9aClSaFEP8TyXWCWYzRdbuuIbZ0GwUJ5bNa5om6Uc2Ik8QWh19WRL8QnkXZiRsZxZkR373W6VXtxjH0bN04R7jNdJCnMUrkrtIzhjovRnaGfbTXv3r-hFadhjo4Ltco7sP4jBuE8fWMcWXbzZAU4QSy1h1tq9Ez84bhNu6b7r0Dxwj8Zkjrupvju699R2aPDASY5Bra93pVnvEDc1tANXanGnLE4IiBuTMtutMYOQtxXaArAZuFCLLCo03jdpn5eEKLGsJkquLbefuGRvLgPv9VahIZS7j78DGbnlx5Rqg8OQgGDJw1CNntGMjpV6I9vSsvCNbT785Au7UoksBtIQsRlhWamD5g1Hs9N1kt9be-k2e7CQ9o39iIffCZrtBMPdGYkTvz60xpDap1RXnj8PVNjzF-mL5A8HJ4uMWKsqtdK2eKimMVs6Ok1MiT-5cQckeR18p8Nc4Mt9MdKBPLZfiona6ToYyKwCWK2_D78mH5WzDuyCsE08PrP5Tv2lH_AP44bAzF4iJ7dX4gPNjdsSWm79rKHqJDmmJluKNbczxIRIYy_8cySHM0ho-EAjTrcvtBsL5Zahy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f18d416253.mp4?token=dpMWSsbMDm-63AD8WP9QpzqhdSjlvUAtu8V_wkp87SEY0OAOzOwg_LNJsBjR0ZvbGBHkEmxfex74lPJYoti0qYuDtNdrsfep9aClSaFEP8TyXWCWYzRdbuuIbZ0GwUJ5bNa5om6Uc2Ik8QWh19WRL8QnkXZiRsZxZkR373W6VXtxjH0bN04R7jNdJCnMUrkrtIzhjovRnaGfbTXv3r-hFadhjo4Ltco7sP4jBuE8fWMcWXbzZAU4QSy1h1tq9Ez84bhNu6b7r0Dxwj8Zkjrupvju699R2aPDASY5Bra93pVnvEDc1tANXanGnLE4IiBuTMtutMYOQtxXaArAZuFCLLCo03jdpn5eEKLGsJkquLbefuGRvLgPv9VahIZS7j78DGbnlx5Rqg8OQgGDJw1CNntGMjpV6I9vSsvCNbT785Au7UoksBtIQsRlhWamD5g1Hs9N1kt9be-k2e7CQ9o39iIffCZrtBMPdGYkTvz60xpDap1RXnj8PVNjzF-mL5A8HJ4uMWKsqtdK2eKimMVs6Ok1MiT-5cQckeR18p8Nc4Mt9MdKBPLZfiona6ToYyKwCWK2_D78mH5WzDuyCsE08PrP5Tv2lH_AP44bAzF4iJ7dX4gPNjdsSWm79rKHqJDmmJluKNbczxIRIYy_8cySHM0ho-EAjTrcvtBsL5Zahy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ایرانی‌جماعت حتی کف آمریکا هم باشه بازم دست از کسخل بازی برنمیداره
😂
😂
😂
@News_Hut</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/news_hut/66692" target="_blank">📅 19:16 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66691">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e9af9079d6.mp4?token=Gg56ngCQ-IA7VvQhHr15R-WLQdn8aH2XMYnw87mzYK8eOa0lbubcIUYoHHgr5ZUnepmiOOW1OjABgpaD2kzLZeBDdLqWwJGLmeJLcLlmWkG2Y0CEN0gwHOdEqQ8SIsSoldJ0RY98ZbRGH-JmGz2Z0GF7z67ascHz6OgOVlf3YEZGg1BoOEOaHClE252JxVmU1U9QCp6OVYcd8sXiS_xTfQVlGB2QJFY8ZUS8G79kAnge8rnxayevLC_WQkUrsqdjibgqWOh_dzo6EsQYHG-KRzO-4sZOw62stIcfJ1n6lBVl9RJorJrtdaS0TntD8HsAJJKCZIzuRUMcVQEFsgwkRQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e9af9079d6.mp4?token=Gg56ngCQ-IA7VvQhHr15R-WLQdn8aH2XMYnw87mzYK8eOa0lbubcIUYoHHgr5ZUnepmiOOW1OjABgpaD2kzLZeBDdLqWwJGLmeJLcLlmWkG2Y0CEN0gwHOdEqQ8SIsSoldJ0RY98ZbRGH-JmGz2Z0GF7z67ascHz6OgOVlf3YEZGg1BoOEOaHClE252JxVmU1U9QCp6OVYcd8sXiS_xTfQVlGB2QJFY8ZUS8G79kAnge8rnxayevLC_WQkUrsqdjibgqWOh_dzo6EsQYHG-KRzO-4sZOw62stIcfJ1n6lBVl9RJorJrtdaS0TntD8HsAJJKCZIzuRUMcVQEFsgwkRQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
😂
یمنی‌های فلک‌زده بابت گل مردود تیم قلعه‌نویی اینجوری دیشب خوشحالی کردن
@News_Hut</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/news_hut/66691" target="_blank">📅 18:45 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66690">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/63f4a6b399.mp4?token=FcExbNC3Tuw-n4n2pcXiGCSglCuBUke54yVtXWqcTzwFXZB2Ovl6-BRt2JlMc6iDb3vfBwxvrihuPiPpJtGHQegAyjgnyt4oaoGke3i12m8lyipiFOd2Ri-HqZza6Rly-bcqczMnoYpzUb4hJipNWWECemZvUcM8DVgpaR9A6NcqxQV22d50_sUcIPo5iWbG1ucGHytn-CX1_CGMaQq0F-O2xRmr5eZN15WaTfeCzCWVb2gYFsFuJzVAks30tqEl8Yfkr_onMBS9c-iskNTb5_DI3xoMcqZ5Bwy3ZorOl5EEevna3hCeoa5f7yoCN0nkL_N_x5kSlI8vAEro1mkmNzzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/63f4a6b399.mp4?token=FcExbNC3Tuw-n4n2pcXiGCSglCuBUke54yVtXWqcTzwFXZB2Ovl6-BRt2JlMc6iDb3vfBwxvrihuPiPpJtGHQegAyjgnyt4oaoGke3i12m8lyipiFOd2Ri-HqZza6Rly-bcqczMnoYpzUb4hJipNWWECemZvUcM8DVgpaR9A6NcqxQV22d50_sUcIPo5iWbG1ucGHytn-CX1_CGMaQq0F-O2xRmr5eZN15WaTfeCzCWVb2gYFsFuJzVAks30tqEl8Yfkr_onMBS9c-iskNTb5_DI3xoMcqZ5Bwy3ZorOl5EEevna3hCeoa5f7yoCN0nkL_N_x5kSlI8vAEro1mkmNzzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🇮🇱
نتانیاهو:
دستور من و وزیر دفاع به ارتش اسرائیل واضح است و تغییر نکرده است: رزمندگان ما در جنوب لبنان آزادی عمل کامل برای خنثی کردن هرگونه تهدید مستقیم یا نوظهور علیه خود یا ساکنان شمال دارند. ارتش اسرائیل هیچ محدودیتی در این زمینه ندارد. من پشت سر آنها ایستاده‌ام، تمام ملت پشت سر آنها ایستاده است. من قاطعانه می‌گویم که تا زمانی که لازم باشد در منطقه امنیتی جنوب لبنان خواهیم ماند تا از ساکنان شمال و همه شهروندان کشور محافظت کنیم.
@News_Hut</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/news_hut/66690" target="_blank">📅 18:13 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66689">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3ad4cb70b1.mp4?token=bXuCyszZ5-6d3VoK0ZmRZ_Ke4qvnhvnwLove89FeSKjiLG6vJULeiff1YlnlBW7-UN1qrwIiEqOwUfs4YppWwvuxSw8nc3aKeZBLjExTi9Y3D5E0oUej3_mkcg-HS82qcWKPScwbhW9egHjwVQrVMJNw-Rlu2I1EGb0cu8x-ABomx1GA21z3f47B9bjRUDfqyPh6mCRhXLTaY0VKID9a3i_eehGIbDZ-cCRB36PJzLlN_YH2gs01VsGQ9k2dRwFafsXzKmuI3nnQTlUllWl_TeHUWktzyHNTKfVo1Szbxv4cBNxSzx1Mnzc_ctGFFX4YFim_NtrClSULEZxV-mCJsA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3ad4cb70b1.mp4?token=bXuCyszZ5-6d3VoK0ZmRZ_Ke4qvnhvnwLove89FeSKjiLG6vJULeiff1YlnlBW7-UN1qrwIiEqOwUfs4YppWwvuxSw8nc3aKeZBLjExTi9Y3D5E0oUej3_mkcg-HS82qcWKPScwbhW9egHjwVQrVMJNw-Rlu2I1EGb0cu8x-ABomx1GA21z3f47B9bjRUDfqyPh6mCRhXLTaY0VKID9a3i_eehGIbDZ-cCRB36PJzLlN_YH2gs01VsGQ9k2dRwFafsXzKmuI3nnQTlUllWl_TeHUWktzyHNTKfVo1Szbxv4cBNxSzx1Mnzc_ctGFFX4YFim_NtrClSULEZxV-mCJsA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇮🇷
اسماعیل بقایی سخنگوی وزارت خارجه:
ما یک واحد کنترل درگیری‌ها برای تثبیت خطوط جبهه در خاورمیانه، از جمله لبنان، ایجاد کرده‌ایم.
یک کانال ارتباطی اضطراری (هات‌لاین) ایجاد شده است که از طریق آن در صورت بروز مشکل در تنگه هرمز می‌توان با ایران تماس گرفت.
یک کارگروه درباره پرونده هسته‌ای تشکیل شده است که بلافاصله پس از اجرای کامل بند ۱۳ توافق توسط ایالات متحده، کار خود را آغاز خواهد کرد.
ما با قطر توافقی درباره آزادسازی دارایی‌های بلوکه‌شده ایران امضا کرده‌ایم.
ما اسنادی از ایالات متحده دریافت کرده‌ایم که به ما اجازه می‌دهد به مدت ۶۰ روز نفت، گاز و محصولات پتروشیمی را بدون تحریم به فروش برسانیم.»
@News_Hut</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/news_hut/66689" target="_blank">📅 17:44 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66688">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Dbb815C21cwyLy3FabxTaDT3uK91_N5ZG3ji02yHfMSVPg0guk00E8cSFOKLrirebaT6RuON7-PiC_UqPX3JfAnD5xCGZj83sSysQ2MhW5U7Hw4X_aHNwXrjvko4kloTDYtGPePWOtzWp79UEn5y9bWQue1fUlMWdhUEyh0jfP3Yryf5svcKXODbq28QEQc3nmD19iK_Mkx86xcblRg-F14AM4RYzZCDST7qfg2hKCKJ6H6cBOoOf-rUltcizx6gAtVtY5HDnTcwUEhqfayu92VHVz7nsP2hEO5OCQIhNyQMDexDwxx982MTVF5BzMOo9HwRdTspQnCPut2t7-z9fA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
اسکات بسنت وزیر خزانه‌داری آمریکا:
تحت ریاست جمهوری دونالد ترامپ و معاون رئیس جمهور، ما همچنان به امن‌تر و مرفه‌تر کردن جهان ادامه می‌دهیم. در راستای مذاکرات سازنده جاری در سوئیس، ایران متعهد به ترانزیت آزاد و باز در تنگه هرمز و اجازه ورود بازرسان آژانس بین‌المللی انرژی اتمی به کشورش شده است. به عنوان بخشی از این چارچوب، وزارت خزانه‌داری یک مجوز عمومی موقت ۶۰ روزه صادر کرده است که تولید، تحویل و فروش نفت ایران را مجاز می‌کند.
@News_Hut</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/news_hut/66688" target="_blank">📅 17:16 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66687">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e8d2962b2c.mp4?token=bFBdICsWmqeu_8kuz4JBvmGIiHV0ybL0spBWx7784BJRiUXWLP3XVdaX-HSr_G8Aiq3TrtLGwL3Y6gE-9IirXWk7_GDTV0SluyUcZExjP_ov8z7-6wgRfO6DhzoKFtLOuAawY3IWO8dRjQ_TvRRTOSTB1yGlTEpwnp5U_JqWcxKxnt-EPE5EGLyjRaIgu7eNfXGekWy-a2xyJQCQjEceuZuzQWc9RbhdhdDqcLnnTiofrkFztsKwlNDiP_wOXgxVS_yHDpxSuSXl87nxalYr_hCgQ1my5xUWY4WfiuUmiHCnLGNX-au68ZocgmJacTl_xn4IlbwD91kEZQHyYuL_Ig" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e8d2962b2c.mp4?token=bFBdICsWmqeu_8kuz4JBvmGIiHV0ybL0spBWx7784BJRiUXWLP3XVdaX-HSr_G8Aiq3TrtLGwL3Y6gE-9IirXWk7_GDTV0SluyUcZExjP_ov8z7-6wgRfO6DhzoKFtLOuAawY3IWO8dRjQ_TvRRTOSTB1yGlTEpwnp5U_JqWcxKxnt-EPE5EGLyjRaIgu7eNfXGekWy-a2xyJQCQjEceuZuzQWc9RbhdhdDqcLnnTiofrkFztsKwlNDiP_wOXgxVS_yHDpxSuSXl87nxalYr_hCgQ1my5xUWY4WfiuUmiHCnLGNX-au68ZocgmJacTl_xn4IlbwD91kEZQHyYuL_Ig" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">😐
استودیو آیت‌الله BBC رو مشاهده می‌کنید بعد گل دیشب طارمی به بلژیک
@News_Hut</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/news_hut/66687" target="_blank">📅 17:05 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66686">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dea331c08c.mp4?token=Ji13e4YtiBi9HbjnsqtZwnrRzuiEUxqIjXpPRjD-QQYeb6m3XN2QCkdSZmkl6CcxDz-HTWj2NJDCUh2Xvjee1m5xiPeTb7iKYCRIOzgJM_PIg01VgjcuKOpjDCUIRwD-i7b-Tzcfpvzq85m4X4lI-t9HCYMmW4k7Egf_De3WbqmbG8sBdx0IRezmuYtNITqaQUqE6S2yBr0tK8wPg4vhO9vQUPOjGmfttZfULRQ_PjLqLv2WpCsz8PKs83qvF7g5wvLeVXsQ2sf23_W5d-trMh1qcE6BDtCqHO16RiZyF0LtB-8C_zFBYqHqeCbisA1XkO3d94yyGD2RJ5dKabzc4A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dea331c08c.mp4?token=Ji13e4YtiBi9HbjnsqtZwnrRzuiEUxqIjXpPRjD-QQYeb6m3XN2QCkdSZmkl6CcxDz-HTWj2NJDCUh2Xvjee1m5xiPeTb7iKYCRIOzgJM_PIg01VgjcuKOpjDCUIRwD-i7b-Tzcfpvzq85m4X4lI-t9HCYMmW4k7Egf_De3WbqmbG8sBdx0IRezmuYtNITqaQUqE6S2yBr0tK8wPg4vhO9vQUPOjGmfttZfULRQ_PjLqLv2WpCsz8PKs83qvF7g5wvLeVXsQ2sf23_W5d-trMh1qcE6BDtCqHO16RiZyF0LtB-8C_zFBYqHqeCbisA1XkO3d94yyGD2RJ5dKabzc4A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بیعت با رهبر مقوایی
😂
😂
@News_Hut</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/news_hut/66686" target="_blank">📅 16:32 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66685">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a0c0474e6a.mp4?token=R37gt-M6ybDzaaFqq_f7ZwF8rUZIsfDqxyjTZqOmmb-ORwvpbNSR5RFr9AsEYvINzr38Svl6lofcwvCTzN62-5ulSd1zvpXo1aqurqounkXmfZeJSysxDuTlkkguN11yVWCOMrYs6qyKjQS9FtBgiVSV3d3fnd77StdnTp7eJBXKDep-t6uDoGqSvM479qdnH03iwFOw4qa6gBzLd9mwjz7zKJtJwWED5BraEPKJmY58FjlZnEws3Vhl2up-zBuzgut_8fHCTrBWZCHS7twfRuGEXgtSkoKcRXe4_MfFAH-WpW4gzbHkcunubOdq6TsHWJ6rtQ8n14m77uu7EgCOzg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a0c0474e6a.mp4?token=R37gt-M6ybDzaaFqq_f7ZwF8rUZIsfDqxyjTZqOmmb-ORwvpbNSR5RFr9AsEYvINzr38Svl6lofcwvCTzN62-5ulSd1zvpXo1aqurqounkXmfZeJSysxDuTlkkguN11yVWCOMrYs6qyKjQS9FtBgiVSV3d3fnd77StdnTp7eJBXKDep-t6uDoGqSvM479qdnH03iwFOw4qa6gBzLd9mwjz7zKJtJwWED5BraEPKJmY58FjlZnEws3Vhl2up-zBuzgut_8fHCTrBWZCHS7twfRuGEXgtSkoKcRXe4_MfFAH-WpW4gzbHkcunubOdq6TsHWJ6rtQ8n14m77uu7EgCOzg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خوش‌چشم کارشناس خبره صداوسیما بعد اینکه عادل فردوسی‌پور بهش رید اینجوری واکنش نشون داد
😂
😐
@News_Hut</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/news_hut/66685" target="_blank">📅 16:00 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66684">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2a12930d87.mp4?token=nZUb8bjpn-pV92daHnbtfEPufcd0vHWSq6CfkUD-cpt1ywAQ5uaZjZ7WHBtv-umweJaVlgjBCYYD0rco48BE2FSsRWiyPYSzUV2hGmsnswJwcngDLT6fU7z-IUCvkgFNW25b6xxeLUtIYDmdugk5sBew6mdYfYwF84e3cbthrRYY_84se7MtCZmmx4wxGGZTJW2Nmpj-mEu8yWzyuP2bJ0yEbyoIwaSIK8zJqJvih410LuzKfH3_HCZCeAudRGJF81qbrpQ-65RyQ92KidXKJ3PD09wYIr1fdQH_uiCozXuBIGdH5IYKmhNirEPeUgTb1eYQUhA6fdg5lbS6p7YAlA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2a12930d87.mp4?token=nZUb8bjpn-pV92daHnbtfEPufcd0vHWSq6CfkUD-cpt1ywAQ5uaZjZ7WHBtv-umweJaVlgjBCYYD0rco48BE2FSsRWiyPYSzUV2hGmsnswJwcngDLT6fU7z-IUCvkgFNW25b6xxeLUtIYDmdugk5sBew6mdYfYwF84e3cbthrRYY_84se7MtCZmmx4wxGGZTJW2Nmpj-mEu8yWzyuP2bJ0yEbyoIwaSIK8zJqJvih410LuzKfH3_HCZCeAudRGJF81qbrpQ-65RyQ92KidXKJ3PD09wYIr1fdQH_uiCozXuBIGdH5IYKmhNirEPeUgTb1eYQUhA6fdg5lbS6p7YAlA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دیشب تو ورزشگاه بعد بازی دخترا اینجوری قربون صدقه بیرانوند رفتن. حیف دوربین رو صورتش بود وگرنه معلوم نیست چیکار می‌کرد بیرو
😂
😂
@News_Hut</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/news_hut/66684" target="_blank">📅 15:32 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66683">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bad11430f2.mp4?token=KymMqQzXz6Rxl0wxQgwq3KG4v0sRpMLqtIgTlU1Iz126xnaSHKP5qfifHqMed7M8wkGrlFTlk-zz858Ziu82sHnkg_J5MSZJ7OhDEyAIfyGzBuyg8bnJ0_KRA3k0z0FSZGKq0M4QdO_abfBXWCyQXMHAg3ha8ZpE2Y959d77LhOQk4qF8XMenfUlZpUjoadlMLSAralb6m_Xm4AsDLMRhxqg4eb6ls8h0IpXg9n7g50oenpMgtPKqyPeEsqZ2aeXRJdMS4HmZqlwdw5DmcLqI2CagNlMP28s5YfYHCXnrvWYXJV2DKwQQx-XSpRB-N9jehz7pAcHoMOICOtV0J2J-A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bad11430f2.mp4?token=KymMqQzXz6Rxl0wxQgwq3KG4v0sRpMLqtIgTlU1Iz126xnaSHKP5qfifHqMed7M8wkGrlFTlk-zz858Ziu82sHnkg_J5MSZJ7OhDEyAIfyGzBuyg8bnJ0_KRA3k0z0FSZGKq0M4QdO_abfBXWCyQXMHAg3ha8ZpE2Y959d77LhOQk4qF8XMenfUlZpUjoadlMLSAralb6m_Xm4AsDLMRhxqg4eb6ls8h0IpXg9n7g50oenpMgtPKqyPeEsqZ2aeXRJdMS4HmZqlwdw5DmcLqI2CagNlMP28s5YfYHCXnrvWYXJV2DKwQQx-XSpRB-N9jehz7pAcHoMOICOtV0J2J-A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇺🇸
جی دی ونس در مورد لبنان:
گاهی اوقات یک فرد جوان پهپادی را شلیک می‌کند که از فرماندهی عالی تأیید نشده است.
البته، اسرائیل باید به آن پاسخ دهد، اما اگر اسرائیل در چارچوب گفتگویی که بین حزب الله، لبنان، اسرائیل و سایر شرکا در منطقه در جریان است، پاسخ دهد، می‌توانیم وضعیت صلح‌آمیزتری داشته باشیمما معتقدیم می توانیم به جایی برسیم که
حاکمیت لبنان و همچنین امنیت اسرائیل حفظ شود.
@News_Hut</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/news_hut/66683" target="_blank">📅 15:07 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66681">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/83f7af385f.mp4?token=nphCDVDc4w4pJa7pt92WDomc_doRyjtWKWZTPwvvEJLJ1XIW7cyGxL1sG2fk8YVUdPyPd113jJAW7aM_xksrlrrfKnOpUx7LOiTMmPz3uao8AmzX6Zx8sYkBFbDFTyCwX-JLbSUn-cU8lCg8TS8AG2JIZbv7olOx3B6-UWTh0pnay18e8MzNWxEROngQN5XeqyT2VKBjonBfT6TMCVKyavZR3KnJZScMcRSjeeEoslTTCFHAx6P-Rv3d498SU4X-p6UFgJ31lLuZxGc5oBXyUoZm1mZhyWW8mczJbvZyDslusuI6nIIDxsHODrMyGBfLeuVEeTmdGmIXMfY-LK781g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/83f7af385f.mp4?token=nphCDVDc4w4pJa7pt92WDomc_doRyjtWKWZTPwvvEJLJ1XIW7cyGxL1sG2fk8YVUdPyPd113jJAW7aM_xksrlrrfKnOpUx7LOiTMmPz3uao8AmzX6Zx8sYkBFbDFTyCwX-JLbSUn-cU8lCg8TS8AG2JIZbv7olOx3B6-UWTh0pnay18e8MzNWxEROngQN5XeqyT2VKBjonBfT6TMCVKyavZR3KnJZScMcRSjeeEoslTTCFHAx6P-Rv3d498SU4X-p6UFgJ31lLuZxGc5oBXyUoZm1mZhyWW8mczJbvZyDslusuI6nIIDxsHODrMyGBfLeuVEeTmdGmIXMfY-LK781g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇺🇸
جی دی ونس:
ایرانی‌ها تهدید به ترک جلسه کردند، یا حداقل تهدیدهایی در رسانه‌های اجتماعی مبنی بر ترک جلسه وجود داشت، اما آنها ترک جلسه نکردند.
@News_Hut</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/news_hut/66681" target="_blank">📅 14:57 · 01 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>

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
<img src="https://cdn4.telesco.pe/file/TXNBNQRc6frjViDaGte9s6azp1OI7zp-L1HLog_f53A7QpVH0kZK7hN41K5XLbwsz4m2QZ3H7OJvwU19RP5UwhsgELEu2d2knr9QzHJDpaH2sqa4DV6xgk8lLmjFqkwSSyXKIiEPv_fsFJqAPxbsJ8_y0jIShcHGTvvQfpsyb7xXBNqicFAEHtWJjk7AvKigkJQRdDIy2dkoEgCHBL98e6u3MBEO_GfCk-HnPE2eKSEWARoiZEDaq18id5Frvs46_JvACpMGiytKYqoLbRicV3l3fu9iCVGLtlPxx6wuTVBZWDDoUXwFwtn7uWS-nDdnJouWclWYQ5PdSk9pGVNl6A.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 [ Fun HipHop ]</h1>
<p>@funhiphop • 👥 206K عضو</p>
<a href="https://t.me/funhiphop" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 «قدیمی ترین اجتماع فانِ هیپ هاپی»🟡صاحب سبک🟡Tb :@FunHipHopAdsContact :@Chaman_Dar_KhakFollowing Copyright Laws©</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-01 21:23:04</div>
<hr>

<div class="tg-post" id="msg-81149">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">ببخشید ولی برا خنده‌م گزینه‌ی تحویل هوایی با B2 رو انتخاب کردم هروقت دراپ شد قول می‌دم بخندم.
🙏
🌹
@FunHipHop | Nima</div>
<div class="tg-footer">👁️ 586 · <a href="https://t.me/funhiphop/81149" target="_blank">📅 21:23 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81148">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">سپاه پاسداران انقلاب اسلامی به کشتی های توی هرمز موشک شلیک کرد
@FunHipHop
| Reza</div>
<div class="tg-footer">👁️ 2.58K · <a href="https://t.me/funhiphop/81148" target="_blank">📅 21:08 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81147">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">سپاه چن ساعت پیش یه نیروگاه برق تو کویت زده
@FunHipHop
| Reza</div>
<div class="tg-footer">👁️ 3.97K · <a href="https://t.me/funhiphop/81147" target="_blank">📅 20:59 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81146">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/J5dmSyYXFetQJux9MmsOCVdl04Znmj1vXgCwtdF-e-At-rn3aocGxKJjcsquus_HXl-TgO5Q9VrZ2xTsD65dYGl1bJ5M-NR1OjwdehqDygPOT4Z9peBMJiqZTJ6tMkcwYQNezR-0oEgBMWdAyyYo9B1nemMIBdTB9Yqpeucy9tqnHZHOzu0FxTGVw3yAhekOQlp4SqAPzvea6_8vx5-xiMarMigxKly38hAMSl9bnSkxgMHG4N-a8ErtLHrzt238mWIQSt6-uZ9TAyfy8ER50Rsiip93n_p51KBzjvR1-9GgVkFg_Vx39gAhrhqWEDq3_GrTNYGpcz19OyIRWzEKqw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یامال جقی قبل از معروف شدن :
@Funhiphop
| TemSah</div>
<div class="tg-footer">👁️ 6.03K · <a href="https://t.me/funhiphop/81146" target="_blank">📅 20:40 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81144">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/lRKOt_SkqoIpBzoWBKHgGQJMtvTML_DTqWWx6mrcxCxTgHMkYGtsxNq5o9Dg_wHgHYU7pJDB-mqbSe-B_8BQoCuzZOmote3rT4GfcKJrdvDryG-lZiImNYSIqk65gB50_rHA237AKytG83XV3qddZ4bieTPaZSAhnOtxqo67SrjzQRBRkN3--UJAjfa1f-TXRZnNednmzXmFQkqH3uVhy1DBRFi2qzf5IKLM8r3Y_--Y1sRdixZyz6DQLFWsI_w-aqGi4k8Rv2vx1px54sa1WNBODPBspCR07HkVIsm3EJIb2FTeNYg2qpRzenre1KgLxj-TkDFT4w9XeVQhxvJkdw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jo1mj88rusKepi3pIMf4nmRpaIGJybPKj7JijcMlnasIw4cuzx7M_x8kx9WypadBRhO3nJUVnGr3k1cXaRkHI6dCprhnuwX5H_rQf2d1JuZc-Gi9UTRxN2TF-cCmCOEfc19tg20vmlFWiin9Ge2ek5rFZ6ap6lxFwjEM_5FSCn1GW94p6h_Olg6tqLy7Bh43muIP96BzlAaWesN71Ckf-6ntM08GZ9-YdZGByBbdlEdhZA2_v4FqDko6guwLyX8pOkEbwSrRi3QrW95NudKgC3-wpyvHpsIDItzDK39wDu-vnakuJTdI7RgLMVW2urFbN8cVZaWRO7I1pjF8OZPb1A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">شات های جدید جورجینا :
@Funhiphop
| TemSah</div>
<div class="tg-footer">👁️ 6.24K · <a href="https://t.me/funhiphop/81144" target="_blank">📅 20:34 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81143">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uG8I9TU-FjfHcQK8Pn0iLnj-9_bDucbsypFC-6vKb9CwVmtd1m1ZjEYEdFAu6ThlTwaIWHFgz2rT52dK8I0veIm4JiBZYixTv89XaMJ2qphOsAzSqTD-hyMJqisDdYfb9IXvtFl0kqPmiqeZYAN_9uyYECyA5890bk-dTldAoGWOL9-KG5xMcwDr2jLXmd479Uv7d55BAEcjiNivb8VLnDfC4xY9wOffjq5ogB3Tt_smzzSXW1QbyN1WsT7Z6csUhPjUNV7JjvCd29pn_7k_Ddm6BlQfJPuodRo1gkcRNPVC6InJDhUiNr6_jUrI2DILF2J-T8HusXMnsMVmba45Yw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترک جدید ایسین به اسم دارک منتشر شد.
📷
YouTube
@Funhiphop
| TemSah</div>
<div class="tg-footer">👁️ 5.89K · <a href="https://t.me/funhiphop/81143" target="_blank">📅 20:31 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81142">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">وضعیت خزانه کشور.  @Funhiphop | Menot</div>
<div class="tg-footer">👁️ 7.45K · <a href="https://t.me/funhiphop/81142" target="_blank">📅 19:38 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81141">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vDKgwXEqhN8u06-B_VfdvqoD0oeI5lWy2L2VDkf8K9qeXSgXDqIO3IA9cbAt6DQLs90O9ZbtCxqQSosoT3ZFEN8S6jyZ9esKkeSaqmLAI8c54YbS4_usg6sAq6sBFS7HZV5pNpFafrQlGfaZlyXE1y1-3Stjg7VT7C8_9O7ZCfGgE8-Hn5qoXWsuJGPUH7o3ZI5BISDELRXdw3DDbJaWer5U-DSv8RPQk4aoqE6dpMkVZeYIXVYuD8Y9Ut1ZN188HBNcwVsH8_xgwNG0VvIIhUAYjgx12QuUGf1lsRxuHwmY4yZPq9mO18ifQqe4gC3TKlY5aBYZLn2AUgK24vj9iw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وضعیت خزانه کشور.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 7.91K · <a href="https://t.me/funhiphop/81141" target="_blank">📅 19:35 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81140">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pDoVidxHHiyJaS5pumG_FS8IEPNssEh0Dcljcz5bSCMZ1vmcR6nOM3g8ZCkVJMoFVL7Z1CegQ_1TMnqoZPMvn143tXZFQEkjlh7eW2JbsTXvG2L0B1qK0cEUQ2PmttrUB8rVtubhVWvSB3emAdYLkpkXvE8VXmmv9RainnNRM-VG2mOt0Xk4jOJ_ctxAAPlKiaRz6NK0lIUPMGB7PztWgEdZ5ATL53mqjfP18pVgd04KDfXJBQXhZY3vx-_W9lgxXGvrfoVsHyPFSa27MrZxukshJ5N1MeR6Sknh0JnMzCQPrlZjgdOBjFQHbqVUl9HNqJFRU36jc1Wjggb5ccMHRA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">برید کنار بیناموسا.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 7.44K · <a href="https://t.me/funhiphop/81140" target="_blank">📅 19:30 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81139">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/t6LN_fnIIpKJ93Du9B4IaATmOGnAjhvgYdXQYTGq4tDwmUmVCcWfkc_FDY5yDBym6eAxswSh6nXZj2AvE76iltvMPhmL_s14jRJPM_SiOklWDuPxpW8JviXplH9L_81JD20xkyUyhv2ah0g5C0yJSGMeA1D6sOtmc8bbBSZnFhA5hrDs8xRM8YUzCa49yarvJZHsTcVfAsUIQDk_4cdJ9FFbXdgeoiVFsW1tk0DhnzeqDNTN_pXQMtDq_chNd64TIX6e39dPCic7kDvsB3aKgAlb9psgLVSQzZZf0wIZMhdFfcQX7YuZQqpWkpNNw7E_W25GqH4TOhLHPIl0uuSZEw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎁
میکس روز به همراه ۳۰ درصد هدیه در بت‌فوروارد
🎲
⚽️
با استفاده از برگه‌های پیش‌بینی پیشنهادی میکس روز، میزان برد خود را افزایش دهید. با ثبت پیش‌بینی بر روی این گزینه‌های پیشنهادی علاوه بر مبلغ برد،‌ با توجه به درصد تعیین شده بر روی فرم پیشنهادی تا ۳۰ درصد مبلغ برد خود را به عنوان هدیه نقدی از بت‌فوروارد هدیه بگیرید.
📝
اطلاعات بیش‌تر و قوانین:
🔗
bwrd.link/EXP
👍
ورود به سایت با فیلترشکن
کلیک کنید
BetForward.com
کلیک کنید
BetForward.com
🅰
r1
💻
@BetForward</div>
<div class="tg-footer">👁️ 6.75K · <a href="https://t.me/funhiphop/81139" target="_blank">📅 19:30 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81138">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">آکسیوس:
ایران آخرین پیشنهاد صلح ارائه شده توسط میانجی‌ها را رد کرده است.
میانجیگران تمام تلاش خود را برای همکاری با طرفین ایرانی به کار می‌گیرند، اما ایرانی‌ها همکاری لازم را نشان نمی‌دهند.
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 6.95K · <a href="https://t.me/funhiphop/81138" target="_blank">📅 19:19 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81137">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/b2a53fe9f8.mp4?token=Wlez1sW3cGfIJT3Si5HTFYmstY4uVbmDSIZWh5H-cdLK1sr7sF2C1HBe6U7NpqOvkyBzFOngH-_bc_wgMpFBqROTyyvuOMK8nkZ5z36NTE3mCE2-rgYUvPv53ig9i6G7VnjoLStCNcg8MIzOVH8zuYCy5JCttIyK8VxFZeaPXc9ENixSAvdo6ae7OCMCA6zuYUKRoCiE-OGWTSFmZjXoQKgopVD5I7KK7ObxARI-QPjTCMaC0zIpVhbOf332OD4fSk859W-gy3W6K8ZGJPA1EX3jaOOYTRiJZ0Jjk_FhysenbD-lH8OLWVx3ZkQ07dj5crwAjHGgJE6tYn3QZdcmiw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/b2a53fe9f8.mp4?token=Wlez1sW3cGfIJT3Si5HTFYmstY4uVbmDSIZWh5H-cdLK1sr7sF2C1HBe6U7NpqOvkyBzFOngH-_bc_wgMpFBqROTyyvuOMK8nkZ5z36NTE3mCE2-rgYUvPv53ig9i6G7VnjoLStCNcg8MIzOVH8zuYCy5JCttIyK8VxFZeaPXc9ENixSAvdo6ae7OCMCA6zuYUKRoCiE-OGWTSFmZjXoQKgopVD5I7KK7ObxARI-QPjTCMaC0zIpVhbOf332OD4fSk859W-gy3W6K8ZGJPA1EX3jaOOYTRiJZ0Jjk_FhysenbD-lH8OLWVx3ZkQ07dj5crwAjHGgJE6tYn3QZdcmiw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نماینده کنست اسرائیل و عضو حزب حاکم لیکود جوری که انگار از دهنش در رفت گفت:
ما در حال نزدیک شدن به یک حمله علیه ایران هستیم، شاید حتی این آخر هفته.
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 7.35K · <a href="https://t.me/funhiphop/81137" target="_blank">📅 19:09 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81136">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">رسما و شرعا توافق شد آقا
ترام به کانال 12 اسرائیل:
من در حال بررسی یک حمله گسترده هستم.
حمله‌ای بزرگ‌تر از هر چیزی که قبلاً رخ داده است.
من نزدیک به اتخاذ یک تصمیم بزرگ هستم، آنها هنوز به اندازه کافی درد نکشیده‌اند.
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 8.36K · <a href="https://t.me/funhiphop/81136" target="_blank">📅 18:59 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81134">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OgFcIGSi23D-Bg1PIXjVziD4OSgV_MGLuTIM7ekra7ng7K4fK5Af5FiSuovfHvGFmnvWqGbCSfwlg4RoujryDcXa8fgIVeARW0XkYww3iRRszB3iPwYtfeGizg4NSuEkFo6dOZJEeAsLk8FusDMrZRAafTzCld8v0FSPOKrOCuio7Lno60xFA8ISusPWIZBSseQKP1Ba26Wlrh8AAGl3SXvbEyozGNcaGN5osp20vJzC7iipHnr7FMKeo7X9jeLpGx8wyhU9n0LT03RasYL5RrAdOGMFFw3Rf_2VWJwdVLokdyTWFXw_NAbIk43Jna1UN1H09Tsz7L-aE0fZXu97Vg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">احتمالا d4vd بخاطر قتل و تکه تکه کردن بدن دوست دخترش با حکم اعدام روبرو میشه.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 9.64K · <a href="https://t.me/funhiphop/81134" target="_blank">📅 18:48 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81133">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/V7dbdOKgkrfeMCrJdOFLm7wgRbKudVnxS_-ysFFjKLxedH1f_cmr2cMhH3gsamOoyMVmcFmxjKPQ9QoaM_72YbZhR5qtV65UP3IfMxQaU9_KUlozhpC2pgK48gBW4GKIIAybRSiFn7JtOE1-tG3kgbC4UwtvE3RJooVZ1dMTkZq-IA0GFM9taAmfx6kKCbhUSG5-GxTWqUndbzKt6RS9631gBmzyM3BEA8L-5U517fHS_QvnCZu14aOg5Xfuo5Z7rmCV6239_DOfzR_4UCB2jNQLVwJ1tzSiWk1tyibDT8t29BdSnCjsWmuFGIKKgS9RgVLrHlDOMby3fEBlWLz4AA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ادعای روزنامه صهیونیستی جروزالم پست:
موساد گفته این افراد زیر نظر وزارت اطلاعات ایران و با همکاری سپاه پاسداران انقلاب اسلامی قصد ورود به اسرائیل برای کشتن مقامات ارشد اسرائیلی و انتقام گرفتن رو داشتن که دستگیر شدن.
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 8.81K · <a href="https://t.me/funhiphop/81133" target="_blank">📅 18:43 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81132">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7c71b69ee2.mp4?token=E3_xIj1r0q_G8cM9oJiE-DdOuD99fzDyWfTueGukM0uysERq4sOA9NATH7MEiZqB40DYCV4-_xoqgKaB7Af20cZVNlazTtn7TU4T3CvfIlC8hM717w-QbFO95Eo8RuRARxyycI0OpTNTLdeMMqM4pN7VEDe6dJ8wD5tLn9cxt6ZqaJLQou00-GrSNVGA8RYmJupjzLKFu66qSKL4pYJwliidB26eCApGw1V763rEqqsOPzHnMzW7a4b4LPsBX6Noz2lw1r8phzYYD1rpEoMPaL7R2777sb5UGD4eQY3o0orQe8UNyKY58sDFixukV0YuHh1nlqEEI6YY7rqO5LWXdw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7c71b69ee2.mp4?token=E3_xIj1r0q_G8cM9oJiE-DdOuD99fzDyWfTueGukM0uysERq4sOA9NATH7MEiZqB40DYCV4-_xoqgKaB7Af20cZVNlazTtn7TU4T3CvfIlC8hM717w-QbFO95Eo8RuRARxyycI0OpTNTLdeMMqM4pN7VEDe6dJ8wD5tLn9cxt6ZqaJLQou00-GrSNVGA8RYmJupjzLKFu66qSKL4pYJwliidB26eCApGw1V763rEqqsOPzHnMzW7a4b4LPsBX6Noz2lw1r8phzYYD1rpEoMPaL7R2777sb5UGD4eQY3o0orQe8UNyKY58sDFixukV0YuHh1nlqEEI6YY7rqO5LWXdw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نتانیاهوی جنایتکار کودک‌کش:
به نظر من بهترین بازیکن فودبال تاریخ پله‌ست؛ ولی اگه بخوایم این زمان خودمون رو بگیم به نظر من مسی بهترین بازیکن فوتبال جهانه.
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 9.3K · <a href="https://t.me/funhiphop/81132" target="_blank">📅 18:33 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81131">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JPVNg5-n7RpDoa8pe1agZ-DwUfhM1_HHoChRPPr_K8eGb2M3pfn_zoMGMvKtfJ7hMHkRVlUVhEPiYpRNoNJwBL1cpMArQZgjqrPKsbTGkQzDnEX0WnAdEBJmBDAh9mV-VhTtPmC4J23dixATc_vWYpeGS9B8GTz3efwBtIvPEaapHNanLn3Rtv9wRzw7kFypZDtiorFyjaIeXIDU_IFKsWyYHAj5J6FguNdkMKC30SfJLWD0lYc3HqHqEPJuGyByYf20a_UKvEf5cijBiiMwA7v48Sx1p0DurkIPGqDNvcltKBYHkJIyxT2LAT6QZtPwPPRtdvx7eyk2mxiUs_9ItA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ببخشید ولی برا خنده‌م گزینه‌ی تحویل هوایی با B2 رو انتخاب کردم هروقت دراپ شد قول می‌دم بخندم.
🙏
🌹
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 9.63K · <a href="https://t.me/funhiphop/81131" target="_blank">📅 18:23 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81129">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">همین مونده بود نسخه مناطق محروم اسپید به قاف بگه کیری.  @Funhiphop | Menot</div>
<div class="tg-footer">👁️ 9.5K · <a href="https://t.me/funhiphop/81129" target="_blank">📅 18:09 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81128">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/72878dd77c.mp4?token=qQtsnHk4v9L8A-AqdTifmC2iWvTjQL4ORgDqhHPMndN7SJLycRudqQP0u-h58iymuHNS0qYWN4rYVamTaB2wICZo4kY2m4zwUDuvRtxag-DG6sIWfPgjFaltm8bYOZy_NIXVSzBASUtSZLbr4Ss37v1wyx0AS79R5SAxRVfBRFteUt9tB0mmEqNAlewrR5Job39RucJ4rLO5DU5Tbw8ocf5DAKh8TXtVeC4_g6AGmSIhN5AzZTZs9mEIC4l04pe6xEstHdDh-Wh7BJeIj5agmEEpkxihXStyIPWo35vQJqIvL8Ll4KXj-CjSjKJf52iY4KNYSgsXkGzOhrWEyGPZYw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/72878dd77c.mp4?token=qQtsnHk4v9L8A-AqdTifmC2iWvTjQL4ORgDqhHPMndN7SJLycRudqQP0u-h58iymuHNS0qYWN4rYVamTaB2wICZo4kY2m4zwUDuvRtxag-DG6sIWfPgjFaltm8bYOZy_NIXVSzBASUtSZLbr4Ss37v1wyx0AS79R5SAxRVfBRFteUt9tB0mmEqNAlewrR5Job39RucJ4rLO5DU5Tbw8ocf5DAKh8TXtVeC4_g6AGmSIhN5AzZTZs9mEIC4l04pe6xEstHdDh-Wh7BJeIj5agmEEpkxihXStyIPWo35vQJqIvL8Ll4KXj-CjSjKJf52iY4KNYSgsXkGzOhrWEyGPZYw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">همین مونده بود نسخه مناطق محروم اسپید به قاف بگه کیری.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/funhiphop/81128" target="_blank">📅 17:56 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81127">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0183a12a61.mp4?token=kRNN1-ZYzNJJpjmNXxZyqL5lUvviWHf5ML6fpVbz_UeGKNrt18tolU0jxZ0TEWeJ1uaacap2auPW9LH3UtXwN3bmWCt-PMnICSgIbhquiKbw7G_XzNdkr3MoumORjpBqcdumeR0rD9p__9n2jltvjx-ysHIyQBRYTZXb7VHeDkiP0v5j9gGvLelMeP0k3XEjlbNVCsgPrQJLF2jFY8uV3l7Db7aX_M4kuapBQarj-fMg7nXP936GIQfq9Whego2CeYwFzQLzSrfiadOymbPbzDiinClYfHEY7S5C9aR4vuezhquskRJGp5326S_rR02io67FN3zsuLvTfDySAw3Jsg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0183a12a61.mp4?token=kRNN1-ZYzNJJpjmNXxZyqL5lUvviWHf5ML6fpVbz_UeGKNrt18tolU0jxZ0TEWeJ1uaacap2auPW9LH3UtXwN3bmWCt-PMnICSgIbhquiKbw7G_XzNdkr3MoumORjpBqcdumeR0rD9p__9n2jltvjx-ysHIyQBRYTZXb7VHeDkiP0v5j9gGvLelMeP0k3XEjlbNVCsgPrQJLF2jFY8uV3l7Db7aX_M4kuapBQarj-fMg7nXP936GIQfq9Whego2CeYwFzQLzSrfiadOymbPbzDiinClYfHEY7S5C9aR4vuezhquskRJGp5326S_rR02io67FN3zsuLvTfDySAw3Jsg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">آقای شهریاری
❤️
💋
💘
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/funhiphop/81127" target="_blank">📅 16:30 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81126">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">ترک جدید ممد به نام فول فورس منتشر شد.  SoundCloud  @FunHipHop | Arash</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/funhiphop/81126" target="_blank">📅 16:07 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81125">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MdJGHU3xUQHYvxfGgywLVUUeDHx2N7TzOvwCt8bNmgJhtJDBIqtb3RqWxB5_WAAXb-F5ubAPWNFWGKuzVe4PA2HGiaR7JAxKOqm96BqgYC6ePqcl-0F-bD74GO0vk9qTmoVrqesgcVpA19QWXo2UmnAiTa7gPDx81nEXv97aMa6Tjg-XDcvB5wHDPHgpyHVd2Z5eQe3NQahRbC5JNSn37dgevPVc89nNT1N50cQRmmagyPiZcI7xo8B-tZrDs0jRRVaI0ygCg-e8vSUexxMCwL_QEYFSakzfEmJ0kLwUykGhJLRoHHSdEWhteuxdCpVR4NEhJxJ7dWqSNnCDWbTi2g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترک جدید ممد به نام فول فورس منتشر شد.
SoundCloud
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/funhiphop/81125" target="_blank">📅 16:06 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81124">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">امباپه هم دستور داد کارکنان سفارت فرانسه تو تهران تخلیه بشه و کارکنانش خارج بشن.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/funhiphop/81124" target="_blank">📅 15:46 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81123">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">متاسفانه با اذان صبح، رومینا و ترانه رحیمی خواهران دو قلو اعدام شدند.  همچنین مادر خواهران رحیمی می‌گوید به یکی از دخترانش قبل از اعدام تجاوز کردند.  @FunHipHop | Arash</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/funhiphop/81123" target="_blank">📅 15:13 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81122">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZkBFeErV2L7ExUMjy40UC6XxyOX4X_-dLYmHCAfwA4ueV1frJYGCqDZ88BdHJidPmiyvCKYKPk7GObwANDrNVV9XHLiafdm4ZmbJwNFdH3QefooPLyPhwO5fwkFQMcfLOV2JPvaV7xyw6EHZzvXsFMfMcm7FSgGOxFcCc2FGyHvfaH9glO7HD8Pl-FgpGZTLBw35v7z-C5Q5Kts-Cnxnxdb-DqbduwIsqVSR659_2-CEg8dSnQ7OHFF3tKYruABnUwOlNUMbVEt0vWkJcTgw0aoiYPoUXvSyeVBjzKRY11f0Y-iouaViNxcwOixb21MzaNwKjYMwQ2M-vyUMeHiA1Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چه بدنی ساخته دو رو.  @FunHipHop | Arash</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/funhiphop/81122" target="_blank">📅 14:59 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81121">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aZBbyawtqRHd1fZTJ_NZSyoX5NDxKA9HWohm3yEa9EAcN-rPk17NnvacJ8-AabvMWxaU6BuSSRLPM73akSyNNJkMtqVWZC-Bshfdwd0fdX8aw_DBSUl0HSDMc2ySRXLFbs7H9iYUFlsHoauS3MFn5_qwvqBXFFWuV583z3kYydu1Flp0mKJAgTQKUqDqmRiw7Zt3AW02RGWzyaK-Y1kXnWIeIhMPs31uowBz76h_wsi7T2-m2pTljBV5FIqyl3LiLWt6rYXXk1qyTpgJDuz4z516dM4WWgnJ207mun1MGiP_xCCZX9i3o_qm_pcJGr6hXXA-736KLxuSNd8EK7L6-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کیتای اینتر
😂
😂
😂
😂
😂
😂
😂
😂
😂
@FunHipHop
| Jenayi</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/funhiphop/81121" target="_blank">📅 14:24 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81119">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/r4V9c1XJfDGXTWyMN72TokZqripO7Tde1GQ9ijjbhrqvUkeO7Z2v3K2GJ-6Oy-I4Zdg-fqI8tkgT4MuBsREaqcn_tGWOPNZRMp6YFFSXvlqEptDVi2GMM6VB6c_6nS2U7Yq7jRbuDzpJrXCRy1H8rO3PtWJ9ZzTAkABCkuCUaMAQ7rR-fDnbZl5Ca57ttHDY1WldkI0fYodKEOtFBus9r83erddyQAACUdWAXPubSWcHwqmzp_QrfIRC2Kq7ezSCEoSwqhzABc6ehCRoh1bhBchs0_OuZaVoYJvAlcyS8uK-NfUFUG6ke0shKYTt8rtO4MtUbG9noRNcajJ9GT6E8w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/tEBOO1HjylOdmGzBDgywK9bBn8JpX7tt2QrQ01L2D3rD9Vz6O-U5rDuO2X6YAFVJDS24Zk6GuNwvLi719JD2zVDEHPPIrQmbn7x5xzgEoORX42xstnNGXKrZJM8s13_To4yQ7WYP8KiIAgwtQyAysIt9PQmaTF0RrXmclL_w1SEhN-62WtfjeohrB0665llDHeyohvcyOErP3UUCnBGwBPFsOJTQSYeQe0NShYkYjzhc0Cdzf0dcsGaE89f2FGLHdx61HHv43XhyIzb1CfUZQJjqLS_0bPn5VbWJ4EQXB4pfvQHr-Gm7Zlpsq6m5PVzLb0qZV9inEtEavixiQLkcRA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">کیت دوم رئال مادرید چقد کیریه.
@FunHipHop
| Jenayi</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/funhiphop/81119" target="_blank">📅 14:14 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81118">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FIBJVxAZVfEbcenxcU2twoyLVChUpQsTDp0ZEhI6bors1-d6st23iJ9cgt4d8D5WFvjlGZh_IHNGDlA_3uv4obHPPfdzQtFlBPV0RmYHmCvrmbHCEYGUiXeVDChdmjcoR74Pfu14PaNdmChYNl6R6v7Od6Eh1eYRxPkiqUe4KPm7Rkhd_9Dx2UZWKMBo80nsuF0p53CPJzT5XLEWVFI7pyx6-DVkmoEJk5LmDZSl9Kx2Ffh_8mSlzmdnROvjoD0zuJEf1kH8MYzqhTP7OtPdqYJNJfAIGXIQF8kkaFtgcjpJe2QpiD3PNocj_bOiTuij2v9xFh0nMQz7bsGD62PjBA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎁
میکس روز به همراه ۳۰ درصد هدیه در بت‌فوروارد
🎲
⚽️
با استفاده از برگه‌های پیش‌بینی پیشنهادی میکس روز، میزان برد خود را افزایش دهید. با ثبت پیش‌بینی بر روی این گزینه‌های پیشنهادی علاوه بر مبلغ برد،‌ با توجه به درصد تعیین شده بر روی فرم پیشنهادی تا ۳۰ درصد مبلغ برد خود را به عنوان هدیه نقدی از بت‌فوروارد هدیه بگیرید.
📝
اطلاعات بیش‌تر و قوانین:
🔗
bwrd.link/EXP
👍
ورود به سایت با فیلترشکن
کلیک کنید
BetForward.com
کلیک کنید
BetForward.com
🅰
r1
💻
@BetForward</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/funhiphop/81118" target="_blank">📅 14:14 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81116">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jjEsQfOoQZ3LL2-NvQvzPWf5LXmEIxknMSMs8iYHMs1vV1N3idft9NQFMHbaLPFNH951Lj3xghpEyOVYsg7SaP0ZP8oASGBBZE_ByOe_rMahnDCVr4IXd0VLjQLyx9aENVFn9aPr_qd3metlwR981DJMsq9hlV4ja0m-Bh352SGdbzWM_1Pkv8SML4pamZmN85iKZAcMBItNAPYDpXYKsgTEhplMBpgXntKCBaIf9stugMSVE_mJVFTCB40-4MeHhBcbHWSjAUufdOefjxE1gmWwGb0AVa8SNo-3LxFeP9LudcihrJAN_AL2-AkdMQpWh1HLt6qZGY2vAuamIYZeXQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فرصت ها مانند ابر میگذرند.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/funhiphop/81116" target="_blank">📅 13:51 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81113">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/juSqvG3znjuRKp99dZlvP6Na2shX8orYY11wcJD4u5j9-QSSG35wXyh-DHSEEJ8gddf2zduYMCWVUFVZjlJ9rpKHN3Qhd0ySkybuVf1Piv2177o1DNcAqFZe06I-rUDnotVdDUSNYXn2bi1bwI97XBmDat_DY2pryTpBQZK4E8XJbBjESYXI8--vRCB_jXYYeIJiRJRi60fgxCgjZjcPzELS0HZL7gHUzKOJBH5jgBsVT0O8o_LcI9yp_PyHdr2vIBuC0HgQKDefLbPH2tcgaMRkcLOGdTdunRmAEgYDQ_CxtyZubbXjxqkQAl_543OnuNPvo1BoByhbBekzC5Fysg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ATjO2MA4vhqVsL25fmAwO_yHqWa7StI15Aa0rByW1cbGkJPHXuC8Ttharb-8As3dYpWoIobLgw_uCX0WsLxUP1rSziBuEJvyrN-_qyQIc6ZKMPgc07_RbP0gDQRD3RMpVl2NRaCxiFAlYPnEk62Lg5QM5cJTwiVCczssobQ7sB-xEQ9S2nejbnIqDDUoZdvmAYsYnFROgKK99IHTrM8o_1ilm6W5bCW7pOtFJsRohf1QWkhsCu-ybRvreqPCjyO9dUwtP_mHBtWYJerJi1SmiycZ2O37Yw9Qi2fV07QHB770dRxsLo0USPk-c1MBDvLDoRsrFnBwrsDEh91b_g2VYQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">اندریک بچش به دنیا اومد، اسمشو گذاشت کندریک.
@Funhiphop
| Arash</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/funhiphop/81113" target="_blank">📅 13:33 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81112">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/b0W2EZ3DMfo5PxlYI3TqdtxngNPFlFMjg1pfNMtYApUGr-P8KiotnTCVqTpArm3t4ZzXlW1LnIQ6c8y0Q6Yyva2l3EJsEH00G5jYtBMClKvOo5aGlTkLJq3GktlZ78BUdmINs2ASEjGbMevKPfoh_P4aEwExL-5Axpa0tXzj00mWzIUh1yHklB41W-j7OfrQuIr3QPUfHQGYBDnleqJ8DAf1sr8I5gkqAq-0YXrG-yLjX9BCr2S_Oq1_Otw7aWbFUPDVrKKog6XhL4CBn5T_yWLawtu1J_Dn5yEPHJLp1TtBIZ4pRxDcqOaRye9hn1dAuWIofyWFjGGf3KHu383i0Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بانو شکیرا در کنار جوادسیوس.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/funhiphop/81112" target="_blank">📅 13:13 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81111">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">ترک جدید محمود به نام اما تو میگی نه منتشر شد.  SoundCloud  @FunHipHop | Arash</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/funhiphop/81111" target="_blank">📅 12:59 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81110">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nO0F83G997ZNtEMr4foal9DNqZFf5WYWcqaDqKf199744mhjFuVTPRMzq9XBMzDAWl3AyCp-gJ-chmr9KLthXCGlj9DjqRkX7MierRCkoUqfcTlswJ4Q84um4x2GKJIfn-nEQisuI7kMnPjzdoJHpFE3sIZ4_K6HshkiOgr2bJOPajV6JwgbEFfE0lb5je5WAFaYFj5WkT5hZsWjTWlbkNOU_RK6I40T_ODSKMCPMp6xbSA2ErZxuKjMsAOZ7qAOLTbjodO_1zEe3sT1j9uG3sFJcOI-BLT1XpDlGE4qL-KTEf_omuzSOegpJO8dt8vklk2ltFMf5wHf8Nq1IfWfRQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترک جدید محمود به نام اما تو میگی نه منتشر شد.
SoundCloud
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/funhiphop/81110" target="_blank">📅 12:58 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81109">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TZN0--V4rMXPS_oay6UyRcH7liEW37jFbTWt99dLNPVVNwMf9VNf_ZsnZQhWtFaGARzW8mIyyH2cKs0-5-7RqdxX5koiA5ioS-lvn0y0IG-feBA9mq_OyVAdXbSJk4-6boWCx84ASiZpW-v79_Ls_8yGIAhCREX8pHiBE5IvuSgplK7JEosdMhcPlowhpaR07XNC0UZgfvS8NyTKSxkgx7b4Q67ANDKVqwCERDJAWV4ylD1FCKbWuYPItv51NdUT3pXUschPvQHLblQjtQtClhoeHSvsQd3XUgpirji1eUcPH_qL2jGvNKN-DKVnqFB8KvzUhMfgPR0PUZJ3LzVK5A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">متاسفانه با اذان صبح، رومینا و ترانه رحیمی خواهران دو قلو اعدام شدند.
همچنین مادر خواهران رحیمی می‌گوید به یکی از دخترانش قبل از اعدام تجاوز کردند.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/funhiphop/81109" target="_blank">📅 12:27 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81107">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">مارکو روبیو:
عراقچی می‌گه سیاست اونها چشم دربرابر چشمه؛ درحالی که من معتقدم سیاست ترامب، سر در برابر چشمه، اونها بهای سنگینی رو پرداخت خواهد کرد.
هر شب بهشون ضربه می‌زنیم و این ضربه‌ها قراره هرشب قوی‌تر از شب قبل بشن تا جایی که ممکنه به یک درگیری گسترده منجر بشن، این اوضاع تا جایی ادامه پیدا می‌کنه که اونا عاقل بشن و بخوان معامله‌ی خوبی انجام بدن.
@FuunHipHop
| Nima</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/funhiphop/81107" target="_blank">📅 12:17 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81106">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">ازونجایی که فارس بیانیه ای از رادان پخش نکرده پس قطعا ترور نشده
@FuunHipHop
| Farid</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/funhiphop/81106" target="_blank">📅 11:36 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81105">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cs6-pNjBmjJmVxa_P9jf-iuOt1NlayHY2WhJJnmjYU9HCREZdcg-8Gek9kvpQ1Yybi78cKXgQPCgb2a70gfPX47PWUDMLZ-ppWlT2k-DIYwDA6ALbUCctJG20y823LumyP9uW-EOZThWPmWDMS9r7o0FQp8O1597MbThjCmRmNfz2uotR_vlOHfHcqWZ1ww209cFrAt2HCyN-rxarrq8tHCaKflC8LlP4XBU_xY8_n9g6oel_OGr8lfUgO7lHBht9vLBGqcxu-Y8BFWJIESczs5hiNyr53Fj8L5FW6lpFeDwshvkQCudM2UdD6MAPNrW-DZAvqYYbRmTbrMUBjCnxQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عشقم میدونستی ایران نباید هسته ای داشته باشه؟
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/funhiphop/81105" target="_blank">📅 10:55 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81104">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1aacc4be5b.mp4?token=Ao-HU-gaTLSujHEQKzvZlTI2YlB6jDs09lFQnsVYTP4s9-0zigoU2ZAZ0NtR9JxHf_FP6XgLA5AMFOICnWBa1Owkct50CR5HTu_trxqOAVgPft8CERKb4aapLDFUbOZtpVomHns4c0Smoilwe-AF7M5KEZAisWlTyTl4iEUODVzym1oL9f4xBikVl2nemQUKOhtHqhseQy0skk_iRjueD7z3SixE8ECXSbPTrFW2U77bECEzmpFF7l2EJruxV1IxCkrZfWvt_MveknB5rXADRF0qOnGaNxewwvuoEFd9svWHgI1v0fwwqaDiuxAPu2yz6i6KuZnJZupLaisqY7DwMQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1aacc4be5b.mp4?token=Ao-HU-gaTLSujHEQKzvZlTI2YlB6jDs09lFQnsVYTP4s9-0zigoU2ZAZ0NtR9JxHf_FP6XgLA5AMFOICnWBa1Owkct50CR5HTu_trxqOAVgPft8CERKb4aapLDFUbOZtpVomHns4c0Smoilwe-AF7M5KEZAisWlTyTl4iEUODVzym1oL9f4xBikVl2nemQUKOhtHqhseQy0skk_iRjueD7z3SixE8ECXSbPTrFW2U77bECEzmpFF7l2EJruxV1IxCkrZfWvt_MveknB5rXADRF0qOnGaNxewwvuoEFd9svWHgI1v0fwwqaDiuxAPu2yz6i6KuZnJZupLaisqY7DwMQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدیوی مربوط به حمله شلمچه
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/funhiphop/81104" target="_blank">📅 04:45 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81103">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Mv9Z5uo4tOeCEWkUAzOM9lOM4e7rPfXKhleHXxEe1gR14lmjUWTx60uq2WK-nMz6nkIot32fRVKi5G5_MltV6PRcAmg6EWcusVrgvyZUMIqWSThribWyDxMpt6QVLQ1tOZWmqo3aI6C4uIVpQONhdj9aljPDQUoovZtjZ2WH9FVC15l8tx2QQBDYGa_tLvBcAMOtZOXXA6cAR1Msn8-R8GMNBFBxXVgbm-cJCRARawugirDcPF6PKcZbZleNAowUGiYGTg1YGKfXND5vIV-UoqO72vfWfB_dY-PN6grZ-FMVnXWXqCrnbtd2gNZMrkfNNqTDKTgpLuyfI2hwiqrHqQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عکس امروز از رادان تو شلمچه
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/funhiphop/81103" target="_blank">📅 04:40 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81102">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">امشب امریکا پاسگاه شلمچه رو زده و رادان هم امروز رفته بود شلمچه پس این امکان وجود داره که هدف رادان بوده باشه مگه اینکه قبل از حملات از شلمچه رفته باشه  @FuunHipHop | FaRib</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/funhiphop/81102" target="_blank">📅 04:37 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81101">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RFYujEzM0McQHuEMph-ms-ZTlY-irNN63PRSbW5EEXAygayGAX1SjDjeoK06CWYacPHrLnDFENJ5mP1Wc6pkWs7460blF71F3faNHbiWv2aGjzivC7S96aTwWAGO7rI3HQ84KEz2hVAeJAh1N476k7Q786qXpTXehbScHGNhRi8nJ_OeK9tOgv2XO8oo6Iomazgh1sA-2s9in-hvDPyiYWI0jiENiq_mMpV7fK1xBAXiuDBkbUe9cFZJDDKag-sD36iU5USorU2mNuyOPw2bgK4dMfM1Zh-hSWBefQTSElSoMhbX1sCbuGNpVEvGXDS4yhmZt4l7FG51sxuumZE8iQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">امشب امریکا پاسگاه شلمچه رو زده و رادان هم امروز رفته بود شلمچه
پس این امکان وجود داره که هدف رادان بوده باشه مگه اینکه قبل از حملات از شلمچه رفته باشه
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/funhiphop/81101" target="_blank">📅 04:34 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81100">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">بیدار شید فک کنم رادانو زدن
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/funhiphop/81100" target="_blank">📅 04:32 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81099">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">کرمانشاه
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/funhiphop/81099" target="_blank">📅 03:54 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81097">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/06dd48cfcd.mp4?token=s8_WnDxuRYa3P_yT_gP8YRwSlclpn3F6kecjsC8XR0LRWIJNIbrzyaFjeXu2W5Ggg2MhA6Jg__ecznLOMWjk9k7HTbcD-1UeRCjB0zVRI3ihYhBIAXmxO75Kt5glz3MT6XiR6wEO2Uje7KnHMmwVARKdr5Fwx00bKFjCkLytXPJEjFxfgrqS6JCV37UcjOLFPEHF5nV2oSokBNgBq6AkGwhbPPD55lbMMppK8Ix7Eqx7v5viaEz9YlclS_YaJo6reB4_DNN-u1RwhsXWpkzL7rYtOG0mCRX50g6NvgTxtbCNWwahcz5uK5JAh-lrH2KOiMY_L43PxzWfJmE-Rq2BUw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/06dd48cfcd.mp4?token=s8_WnDxuRYa3P_yT_gP8YRwSlclpn3F6kecjsC8XR0LRWIJNIbrzyaFjeXu2W5Ggg2MhA6Jg__ecznLOMWjk9k7HTbcD-1UeRCjB0zVRI3ihYhBIAXmxO75Kt5glz3MT6XiR6wEO2Uje7KnHMmwVARKdr5Fwx00bKFjCkLytXPJEjFxfgrqS6JCV37UcjOLFPEHF5nV2oSokBNgBq6AkGwhbPPD55lbMMppK8Ix7Eqx7v5viaEz9YlclS_YaJo6reB4_DNN-u1RwhsXWpkzL7rYtOG0mCRX50g6NvgTxtbCNWwahcz5uK5JAh-lrH2KOiMY_L43PxzWfJmE-Rq2BUw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">فردا:
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/funhiphop/81097" target="_blank">📅 02:21 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81096">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YgJin_AOMWK5vYocRzGI7gg2I5ZrjPp1R1toOMPpp6ix5AIedtOJmqMBNOFZymWW2QQ09t7C1i4ln-qEZH6bzhGN8J1MO-x8_N_PsTuMMd_QhVmQTNKiMAXIF7m2y-L9asrMUK2Wqe2-3iYdaIMwn3doWWaXM9NblOQxeEpDHEiP11U-EMVyfhVglwAglZEukg5x9kiK7NYPx2gUk0s0c7mP5shuP3jjT3J1_c_m_CS7SZHzM8bVOAd5JIlz-4Q4LfuBFpLkuUPj9U1LretZ5fPF9v2KDdCL_aj6ZTGkLBECQXExGP1PNHCNkolQsuKTjMg4vKPhdlGPJccFeBT_tg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مجلس نمایندگان آمریکا بودجه ۹۵ میلیارد دلاری تامین هزینه جنگ با ایران را تصویب کرد.
پ.ن: به گفته امریکا حنگ 40 روزه براشون تقریبا 38 میلیارد دلار هزینه داشته
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/funhiphop/81096" target="_blank">📅 01:42 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81095">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">سیریک
@FunHipHop
| Reza</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/funhiphop/81095" target="_blank">📅 01:27 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81094">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">پرواز جنگنده های نسل 66 کوثر بالا سر تهران
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/funhiphop/81094" target="_blank">📅 00:52 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81093">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Cxa2hRy0eW5cmfS_sRjG-zaGsqDNyKP_-WBVIAKRc70epDGB64qOsDrJs3_POHSPAOzbvJRF6UvGc62EySTqwZl7a1xHJ_ATGyVjQHMGCQ0mJRscrRiKAzV2eArfQM7hAOxtjKmn-y9AsxC8UvsmcIGUUUlbLoA6c6ZTvvoM6W1pt4X4rQ1MBxFwHhmidjzIUAhdO2D2tD92q1y-8AVVH6337IKVfVE0oVWhhHpkuZ9Ya0v_6eFiyELY5L9PF6koaB35vtNzHEev34VIumlW8N1xX__wrG6TrVNVe0lVuhzOmhQ2hb3DR3Uh7KqKWOzZ1U9uAVvZDV63jUgole2xMw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">طبق مقررات جدید چین، استفاده از برنامه های هوش مصنوعی عاشقانه برای افراد زیر سن قانونی ممنوع اعلام شد
دلیل نگرانی سیاستمدارن چینی این بود که شاید افراد وابسته‌ی ربات شوند و تمایل به ازدواج رو از دست بدند.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/funhiphop/81093" target="_blank">📅 00:47 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81092">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">حالتون چطوره؟
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/funhiphop/81092" target="_blank">📅 00:40 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81091">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">انفجار در ماهشهر.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/funhiphop/81091" target="_blank">📅 00:16 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81090">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">ترامپ میخواد در های جهنم رو به روی ما باز کنه نمیدونه ما خودمون تو جهنم زندگی میکنیم.  @FunHipHop | Arash</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/funhiphop/81090" target="_blank">📅 00:00 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81089">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">ترامپ میخواد در های جهنم رو به روی ما باز کنه نمیدونه ما خودمون تو جهنم زندگی میکنیم.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/funhiphop/81089" target="_blank">📅 23:50 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81088">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">کان نیوز:
ایالات متحده به اسرائیل اطلاع داده است که قصد دارد در روزهای آینده حملات خود را تشدید کند، از جمله اینکه برای اولین بار در این عملیات، از بمب‌افکن‌های سنگین استفاده خواهد کرد.
@FuunHipHop
| Nima</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/funhiphop/81088" target="_blank">📅 23:42 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81087">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">چه بدنی ساخته دو رو.  @FunHipHop | Arash</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/funhiphop/81087" target="_blank">📅 23:32 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81086">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/e6MhMyS6DltV54cEoXTlDIapJ5M-SAVMXRSkL63eh7CSZWFMM4icvgmJm4PxcdwKvF3hMwHTC5eiBt0zcCFt-Vv_fe316780uFoJB_ujS0Mqd1ac7E6zN6zGKWz0CmjyX1hLpTyj6gtEMjq2Or7NsWv-gxULI3ULzPLx7cWTZjTK0TI180qjJoSBs7sA3M4AEmyPU-zOvb7hCuk7BcsxIUWWbb43tsnJ1UoO0ezAs0auTU01u_u9eBt_hELBaLlr72q7XfFr2eT0pkFs2uge7rEqjIghWegdO9FkzQqVJPwW3L-9DHFS4LG9EQ5jD5vy4Ek7s8KfJ3KUitvPEgF0MQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چه بدنی ساخته دو رو.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/funhiphop/81086" target="_blank">📅 23:31 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81084">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EB5VcLMEUvFhkVNsNzmMj4bVWneS8su6xDuzI88GB-Z7cXgavDB0yzNUhxldnfLz54f4meG3RSCPl6G_VNAEhM__hUGehx1cO97CFQcOQhM8M8R6Iy3TQSvQ9TQTSCwWVwbvn1x_JB65vv2GTHbjeLK6hcjGBFsi_ywFzZYYUfvdJ-UOplV2awIVz0DyeYW_sWOLOtnePix5q0LvblJCGtgcKHudG6CaonQHtt_aF57O5wECvXGyf0hx1UyZIvYWJodfrVfljT_yeEvJWZR5joaySKaQphqxAwSRIClpitq4E5u4CuRk_uqIdL6sMgldM6vls5ZVMs5sQDRSE6x3BA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سردار جان پس اون پلا و نیروگاه‌هایی که کودک‌کشان تا الان زدن چی؟
اونا جزء تست رایگان ۷ روزه حساب می‌شدن؟
@FuunHipHop
| Nima</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/funhiphop/81084" target="_blank">📅 22:55 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81083">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OW3oxx8rLWmOKlBJUNZVRLV2rB46sYcgfDOft4E8tAlefW1bTiVkyvngTwE8naoSgh144CkjtwbRDoRjkHcRKmWPqgxZsbb7KxLD7HNBAR9LyJOsynUK5pOyTQlB03MCRV_iQ07G9nkhjPKN977Inm1GGhkrcT9-EThBW5VrHag7sHlrAFJ9vqpPOtWVELnvSNL5FP-alYNbLw5fdLqAyndCQuGPRG7_6QsjiFVW9gbpbz_AxToNYD-mndlI6rURrqUHoh6fFeZcnwkj_QBJ3zmcwItK_QDNX4_NKWfWUb8QmAff8E1Evhj-xgXzT5YO9SOWQY1mBw62_6dbwhpXbQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آقا نخوابید خیر نیست مثل اینکه
انگلیس سفارتشو تو ایران بست و کارکناش رو هم کامل از ایران خارج کرد.
@FuunHipHop
| Nima</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/funhiphop/81083" target="_blank">📅 22:40 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81082">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fORfO-kHGgX2Qn4DXRsek2jAV5ceR-27jvRlmCCEjViPpmVxO7nYuh_xr8Js4H7wFwj04ZvC5QyK1u8ETqXmU2xUC_xyCnKSpEw6I1pI20VBzmFPUOR85Ype0jWeQoMmDAJV5ebmdfIGWAo3Y80nIVtspPfXf8EwOs3FdzbcS2xt2PIazVomeM9aG_p749y6ltgSd0GPSeNCMWKSLWbuUxIqFyMN4UTcCjZkB7jH8-_veF_aZgrYLaHp2OScX_xbGTvssibuTQRpqSaN419raEr0UhCbQHIP6g5mheVGdQuM2y4l8K66Pe4XRzaPdgXaQNiZDZp3k_v_yVTTksCSgA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حسینکوسمادر فرمانده گردان القسام حماس
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/funhiphop/81082" target="_blank">📅 22:28 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81081">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a367c7357b.mp4?token=HwFn4vlRYb8OxE6UkxV-dQQMOECOGej8VtKPw82q2fRF31w4CZ45fLxIO7OTMHGl2mIOCNt5L9It6leEpNbZDnIRPWSjNejX-v4QVkQCIbIrjpy8NCinWe1PkuOFXh1wYVVluAad09VfmYp0LJgtc0PQ2c4_7Ok64CDcRtiWV3YkLv_9vvtzJ54FEbfdh2lUJ30lq_UNBhtwqaqoyZm8SmuaNM10LoJ0-sMa-f7xWq7Nfjghfbs5YW2hlnIectUUmwQkVIN2S7ngk9vc2QBkb0e2yHBeWYtL-Bxuus0XC2jHjJAc-tVJhE5WQVd94j54SrE9FTXPoaDsyKOM0RiWQA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a367c7357b.mp4?token=HwFn4vlRYb8OxE6UkxV-dQQMOECOGej8VtKPw82q2fRF31w4CZ45fLxIO7OTMHGl2mIOCNt5L9It6leEpNbZDnIRPWSjNejX-v4QVkQCIbIrjpy8NCinWe1PkuOFXh1wYVVluAad09VfmYp0LJgtc0PQ2c4_7Ok64CDcRtiWV3YkLv_9vvtzJ54FEbfdh2lUJ30lq_UNBhtwqaqoyZm8SmuaNM10LoJ0-sMa-f7xWq7Nfjghfbs5YW2hlnIectUUmwQkVIN2S7ngk9vc2QBkb0e2yHBeWYtL-Bxuus0XC2jHjJAc-tVJhE5WQVd94j54SrE9FTXPoaDsyKOM0RiWQA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">هر بار که با خودت می‌گی که خب خدایی این دیگه آخرشه، این کشور یه پدیده کاملا غیرقابل تفسیر رو به طور معجزه‌آسایی خلق می‌کنه و مثل جامپ‌اسکر می‌کوبونه تو صورتت که بگه گوه خوردی که می‌گی آخرشه، تازه کجاشو دیدی؟
@FuunHipHop
| Nima</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/funhiphop/81081" target="_blank">📅 22:03 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81080">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">راحت بخوابید که شدیداً خیره و توافق نزدیکه  پست جدید ترامپ از تیتر یکی از خبرگزاری‌ها: پس از کشته شدن سربازان آمریکایی و حمله‌ی ایران، ترامپ به سنتکام دستور داد «دروازه‌های جهنم را باز کند»  @FuunHipHop | Farid</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/funhiphop/81080" target="_blank">📅 21:17 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81079">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EnOZJ9XZxuBpt5DWiUtZHymmO4FarWB7ZWyhn0Y2yJczW7wemxo2uM5YcUGBQaNLzsi6qmVMhERFxJaZNF-TVLL51AjhUi5Erj0kiKgZSnzcAoiSCfbW0iB_N4jiF-fWD388fziDYrsCr-ZvVhKiVZv4Rll4QIIb6JH7bJeLe-HZuXbuyWnZ6hKF-DaBFfjloBcvoT-FbHqW-NnIDSQ7pkFDI1RFfRYTAxeitJIx152WAlc6Mu96rarhDT8PtOLow8c9WrBt-3bBSvU54lT6w4wKip5ejvLIKBubuAZmBZwH0PQqtB0srwNqDpHdSn_1KCUx0VGu-lbpV-KDzbKgRg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">راحت بخوابید که شدیداً خیره و توافق نزدیکه
پست جدید ترامپ از تیتر یکی از خبرگزاری‌ها:
پس از کشته شدن سربازان آمریکایی و حمله‌ی ایران، ترامپ به سنتکام دستور داد «دروازه‌های جهنم را باز کند»
@FuunHipHop
| Farid</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/funhiphop/81079" target="_blank">📅 21:10 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81078">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">حافظه تاریخی پرداخته ب فردوسی پور
برید ببیینید</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/funhiphop/81078" target="_blank">📅 21:05 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81076">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">پزشکیان دستور رفع فیلتر اپلیکیشن و سایت عادل فردوسی‌پور رو داد.
😂
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/funhiphop/81076" target="_blank">📅 20:59 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81075">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">صبح امروز، مهدی خانکی، دانشجوی ۲۵ ساله رشته حقوق که در اعتراضات دی‌ماه دستگیر شده بود متاسفانه اعدام شد
@FuunHipHop
| Farid</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/funhiphop/81075" target="_blank">📅 20:23 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81074">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">خودکشی جوان ۳۰ ساله پس از شکست آرژانتین در جام جهانی.
«سیمون حسین» ۳۰ ساله، متأهل و دارای دو فرزند، تحقیر ناشی از حذف آرژانتین از جام جهانی را نتوانست تحمل کند و تصمیم به پایان گرفتن زندگی‌اش گرفت و همسر و دو فرزندش را تنها گذاشت.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/funhiphop/81074" target="_blank">📅 19:39 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81073">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">وینیسیوس عجب کراشی شده.  @FunHipHop | Jenayi</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/funhiphop/81073" target="_blank">📅 18:54 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81071">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/RXriwEmyvFuCOh3Opb0EAKpkII8DAeCC4mIUQuSKaIvSVY1n2N4LZg-zEsZKhFMaq0rm8gTVhIP1_OlUu_0i87TAduBeLt4Lts6zgM_hxoDzQ1w9Hb5YPuzwPwVDhXqaRua4muQVpV7A83LVGJnFPn3FhfpVyPZAMj68yy0iLbRRE4mBCoK0mkS1jDCTWtLWKMafzJz_A8daNQIGkeUePhKYPJiHdTqZ8PSus8Q4yJGJggN4iwYoGk4E5o5EZipwH0GWmQw2DEflozxCXzQR89AXLt-7WxYq27kVeETBZI9Oipjqd9SpQVNfojkTxiY0tq3a-dY5hDJt5rhQHlMZaw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Cvo1hStT-Ij07qft3siR1cjFyVpUW0Wnj275XDxJvmEeU-0h4DHmgFNEkDl3tPgMLPuZb1oFPbnCScoCV-DNLIgbnubmYeACbHAKbbkRIcn5EtbRvaBQY78G4e7a--Vs7cHTN7c_zLziM869_g41qca_pOMtHZ4_xZjEpNdh-wwhWycvzYOiN5PYVaOsv3yUllcLSTqIo2FWyYrpnXXQpIgWOZUS62tOxLY9uqccMZE2GZ5k0dgmEq_mRukkG27MODJTFeE1uai1vtH58qpL4hfwzijkR0zS5clqiskV02GoSlecZJRDwxUEKX5639P2I4PlVJa3qlsrF2nMQWOEaQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">وینیسیوس عجب کراشی شده.
@FunHipHop
| Jenayi</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/funhiphop/81071" target="_blank">📅 18:50 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81069">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">ترامپ: از این به بعد، هر زمان که جمهوری اسلامی ایران در تنگه هرمز به یک کشتی شلیک کند، چه با موشک، چه با پهپاد یا هر وسیله یا سلاح دیگری، ایالات متحده یک پل یا نیروگاه را بمباران و نابود خواهد کرد، از جمله آن‌هایی که در کنار یا در شهر پایتخت تهران قرار دارند.…</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/funhiphop/81069" target="_blank">📅 18:00 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81068">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">توافق قطعی شد اکسیوس:  ترامپ در حال بررسی از سرگیری عملیات نظامی گسترده در ایران است، که احتمالاً شامل عملیات مشترک گسترده با اسرائیل خواهد بود.  @FunHipHop | Nima</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/funhiphop/81068" target="_blank">📅 17:50 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81067">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">توافق قطعی شد
اکسیوس:
ترامپ در حال بررسی از سرگیری عملیات نظامی گسترده در ایران است، که احتمالاً شامل عملیات مشترک گسترده با اسرائیل خواهد بود.
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/funhiphop/81067" target="_blank">📅 17:44 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81064">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/mGUSPUOKKN30x69GatUQ4lAz2vp063kScwNL1sFj4Zq0b7rUXhnAbsLlVCzIJCFvw0s6tD1WqIL0ZoyQ2EwHwH1fY9bEWGk5Rkw4taE0mlXx_WbPG5Bhc7lZ8__USA5F4BsysEK-505sS-guzzAxqqVrbd1dlir4i4aM0KtoKF9NCJXUOKlG8QGk-pvYb3Xn-NAvWNsr29JVbbOFvisF2k2OzAjCwv-NZ6B_GmDmCUPWCN_Py3fNT4aLxGB8AVUU5SkZWSnVOcPNgATepf9paCID2OE_mFA5f_or2td91Mx4lzq3UbPI-npuxihU5cXXe-ud-5o2s8l3GjIcVsCa2w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/mU7VFklwOZ4j797o7wsRsBldjkE2v-pRw6UASpBJwarTFumgD0-yw-tO87mmiaagwP07tiwb3NH1irh2ggaFDD2plhYDgHkH46E594PIuSI-LQqCtawDbjnOd3lYkQKPoGyCkBGlF7V4JBUzyTYwSvogPVnruy5ihdzjEBZkXw0og0ZLKvR7UlhFU3IHWthLpysMwrtFGysvD1m7228A3eKKVZG8Asfiy-sRsmWShMguWN2rrfaOfX6dRNcEY50k4bU2cexth-Up4Viq4UutgpqWnfHl8qa6CLOsiX08ogMOww3iZLZUaSr6bnYGvmI70szN-hxDjJm9lPaUtdjxJw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/SgKkSCDrp6VYNlGmC3dLmdL8cHEmd19hIUqK50cRLkDye4tpaHldPPo9yIlPH51yxtoTQ8jiR7giiIA2W8y8_KFFvskQ4SMn6XwqNbWGL_0OMXH_rsOCGn60kM8-fqeuUQJ9tnmOsbw5NNRrYDXKEZWT36lYyYXSOlVq_BW7alCOvDsp8WUjO08waTLia2nVLajW3C6CSy4_kMTTCAns_w_b5NNEPdYKuVHgEvbltX4Vg6-5ynwqWXcm_jze83re0pz3kKZar856ZxmJwPH0TTWEsHusU3Hy552c1aHQprjWwran4Iqsjo-vGsFpXT-6xOc9ku9tMOc37XiEqBF5Pg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">حالا ک بحث عادل داغه چنتا شات قشنگ ازش ببینید
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/funhiphop/81064" target="_blank">📅 17:20 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81060">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">دلم برا رها وانتونز زیبا تنگ شده، چرا عکس جدید از خودش منتشر نمیکنه؟ شنیده بودم این اواخر ترکیه زیاد طوفان می‌شده امیدوارم باد نبرده باشتش.  @FunHipHop | Arash</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/funhiphop/81060" target="_blank">📅 17:05 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81059">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">دلم برا رها وانتونز زیبا تنگ شده، چرا عکس جدید از خودش منتشر نمیکنه؟
شنیده بودم این اواخر ترکیه زیاد طوفان می‌شده امیدوارم باد نبرده باشتش.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/funhiphop/81059" target="_blank">📅 16:54 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81058">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">ترامپ: از این به بعد، هر زمان که جمهوری اسلامی ایران در تنگه هرمز به یک کشتی شلیک کند، چه با موشک، چه با پهپاد یا هر وسیله یا سلاح دیگری، ایالات متحده یک پل یا نیروگاه را بمباران و نابود خواهد کرد، از جمله آن‌هایی که در کنار یا در شهر پایتخت تهران قرار دارند.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/funhiphop/81058" target="_blank">📅 16:39 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81057">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">این یعنی تعویق؟
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/funhiphop/81057" target="_blank">📅 16:07 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81056">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/S2v-RQ1tirt1XNuvUIb4bEQXqwGsNCMAsDLDXa9XRz5FSBXXFdvP31-NX11J-eZRVxT3YmFXTVTzEOVkoVgIdhmoatqsq12W_Npoi-rMdeRV2d9M5-kiKTcInKOHO14MngJH52RZIKltcGRGBwWWPqI7pU5lk6UPSlVc3rPBIWC7qTQqRMkSiutM464vIK9_KQDyTEE5Nx9nAiPMSAcAYdWRK7MN-uZpfRWnhoPlcW-rjR0uI6etX1Un0C2JPbaLTXmZpSmyqgO8MAMMLXTjdoHh1ZIXuIO2peeQ7KySl_h3GqdWY5A3ysfAQgZvSOM8cGAOVT5vh7hvwkZpJFCHmg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هیچکس گرفت رو فردوسی پور
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/funhiphop/81056" target="_blank">📅 15:43 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81055">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">داریوش بالاخره ترک کرد، شات جدید داریوش بعد خروج از کمپ.  @FunHipHop | Arash</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/funhiphop/81055" target="_blank">📅 15:15 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81054">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fmxtMhvOmfIqUjshLkLcKYZweAWhwsLr8mFT5TsWwjm1R8kXZ-8nphhLxRyUMfz_4ssQ7Ac6Esj4Tc6ijrs4zknDfItZPcSeq6Aqxv3_UpcLKO6lvQZznWeJUN3cpj7wwhc44B8CY1Ks-3Uh3qdHsn7b2cmPlhgM0NMFjKE5b5b9xzsEvz55vNIOtiPMW18g9iCOv7oKmUqGijF_hr85K9k0QngoWeTVDLLTrLm7pxleYpITCnlZKe9qeRahrx_mgIS5U7rkBvqgnpjeMKp7OrLY0J-RKo_yxDptAnniRMejJiQ0PPlOqvnagOfQTTUroaoJErZUHEodbVUXQnPlgw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">داریوش بالاخره ترک کرد، شات جدید داریوش بعد خروج از کمپ.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/funhiphop/81054" target="_blank">📅 15:03 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81053">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">سپاه: اگر تجاوزات ادامه یابد، آماده عملیات پشیمان‌ کننده‌ ای می‌شویم که اعلام عزای عمومی در آمریکا را به دنبال خواهد داشت.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/funhiphop/81053" target="_blank">📅 14:54 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81052">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">امتحانتون چطور بود؟
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/funhiphop/81052" target="_blank">📅 14:26 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81051">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">توضیحات مراد ویسی در مورد فالو کردن عراقچی
@Funhiphop
| Farid</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/funhiphop/81051" target="_blank">📅 13:44 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81050">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">ببخشید چه؟  @FunHipHop | Nima</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/funhiphop/81050" target="_blank">📅 13:26 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81049">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">لیونل مسی بعد ناکامی تو جام جهانی اینفانتینو رو آنفالو کرد دلیلشم به خودش مربوطه.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/funhiphop/81049" target="_blank">📅 13:14 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81048">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uMdSKtmjmsS_ez0Suc5sktk6BVMRtb5iTCVyEgd2UABDK_n_ELNbPWTEORlxYhFLrvtJX-Zn0HvZFSX2S51MZ0wBWHbkruqyfDTnxW9hpdRnJdTRHR8bcHNoDI_xkX4VYRU9EdF020We4uan_BYFrEP1rYua0LJItYyyXvHLg8Qta0757c-F2THwJ-bwOAt0DQf58U6_N6F3GXKyS2r0gAmV9m40gOn5MRjZvOs_QWuWViCdNAb6biuTbceuUxXWBcj0Ck6aCXRaF8JsxKiNq2GbQKP9n4eKOX5jcTlpqabMWPzhIQmZD4Ws3Caqr5LxLouGIqdm7xo7Jl6__U1nrg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حالا من در سطحی نیستم که راجب این موجودات نازنین نظر بدم ولی ناموسا سینک جای بچه نگه داشتن نیست.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/funhiphop/81048" target="_blank">📅 12:30 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81046">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">سجاد شاهی این پول ویناک چیشد</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/funhiphop/81046" target="_blank">📅 12:05 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81045">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">قبل اون قضیه نجات خلبانا میگفتن نیرو های آمریکایی خایه ورود به ایران ندارن بیان سلاخی میشن و فلان
الان میگن خایه اومدن دارن ولی خایه موندن ندارن، بمونن سلاخی میشن.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/funhiphop/81045" target="_blank">📅 11:54 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81044">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">ویناک چند روزه به دکی نگفته پول منو بده دارم نگرانش میشم</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/funhiphop/81044" target="_blank">📅 11:36 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81043">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">سپاه صبح ها نمیزاره عربا بخوابن آمریکا شبا نمیزاره ما بخوابیم
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/funhiphop/81043" target="_blank">📅 11:08 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81042">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">تو دنیایی که ملت با سهراب ام‌جی لاتیشو پر میکنن دیگه این که فران تورس جام جهانی داره و رونالدو نه چیز عجیبی نیست.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/funhiphop/81042" target="_blank">📅 10:01 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81041">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">زهران ممدانی میخواسته نتانیاهو رو تو نیویورک بازداشت کنه.  @FunHipHop | Reza</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/funhiphop/81041" target="_blank">📅 09:12 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81038">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">زهران ممدانی میخواسته نتانیاهو رو تو نیویورک بازداشت کنه.
@FunHipHop
| Reza</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/funhiphop/81038" target="_blank">📅 08:28 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81037">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">همین بین که شماها مثل سگ استرس امتحان دارید رفتم سنگک گرفتم دارم املت میخورم
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/funhiphop/81037" target="_blank">📅 07:28 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81036">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">ولی بیدار کردن پدافندا الکی نبود، حس میکنم امروز صب یه تیزر از اتفاقات فردا بود.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/funhiphop/81036" target="_blank">📅 07:09 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81035">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">سنتکام اعلام کرد عملیات امشبش تموم شد.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/funhiphop/81035" target="_blank">📅 04:21 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81029">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">تسنیم: دشمن اومده رو آسمون تهران ولی جایی رو نزده و فقط صدای پدافند میاد.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/funhiphop/81029" target="_blank">📅 03:50 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81028">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">دانش آموزا بگیرید بخوابید فردا امتحانا برقراره.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/funhiphop/81028" target="_blank">📅 03:43 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81027">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">نصف این گزارش های انفجاری که میزنن فیکه، تا الان پنج تا انفجار برای شرق تهران زدن ولی هنوز خبری جز صدای پدافند نشده.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/funhiphop/81027" target="_blank">📅 03:36 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81026">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">Ginza</div>
  <div class="tg-doc-extra">J Balvin</div>
</div>
<a href="https://t.me/funhiphop/81026" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">کوبارسی اینو بعد قهرمان جهان شدنش گوش میداد من وسط بمباران
@Funhiphop
| Erfan</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/funhiphop/81026" target="_blank">📅 03:36 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81025">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">انگار پوفیلا میترکه</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/funhiphop/81025" target="_blank">📅 03:34 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81024">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromZahra</strong></div>
<div class="tg-text">انگار پوفیلا میترکه</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/funhiphop/81024" target="_blank">📅 03:33 · 31 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>

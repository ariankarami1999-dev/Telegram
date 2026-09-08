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
<img src="https://cdn4.telesco.pe/file/Urx7n8UWhVMfZoJwOgc_v5teOhSn6CsOE07iV0gXBPUDTHYLWJX_ZUetCqltDU9VgrEBrtWu5SRfoGNVqGZfRnrZ5iBLLIcjPmYNPamFCu9XtnM2XgqokC1luBD-ya4atwGc9Hv1_QOFn-NB0lsRrzGVadVlErQmMwPPMGWNICHbkpfq_bgAz0p5_r6tBXfdz5qC6jvK-_Uiqve79MdiO7_LI3AESVvMqfqFYr-xUk5cx8YoPQRKd9N8ZLS3BzWIl2Y82kd1lsRzFnfZK5WW_0dS__mPLR5aRXdzaCqdOSamGfrt47UMjunl501yYriktjtC7rjqcxh9MtB7sISsrA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Persiana Soccer</h1>
<p>@persiana_Soccer • 👥 576K عضو</p>
<a href="https://t.me/persiana_Soccer" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 پرشیانا ساکر دریچه‌ای تازه از اخبار محرمانه و داغ فوتبال ایران و پوشش اخبار اختصاصی نقل و انتقالاتهماهنگی و رزرو تبلیغات:@adspersianaکانال دوم رسانه مردمی پرشیانا:@Persiana_Plussپیج اینستاگرام:Instagram.com/Persiana_Soccer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-17 08:58:33</div>
<hr>

<div class="tg-post" id="msg-29289">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">🔹
👤
ویدیو کامل ویژه برنامه جذاب امشب عادل فردوسی پور با برسی کامل اتفاقات این هفته فوتبال ایران با حضور دو ستاره جوان فوتبال ایران.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/persiana_Soccer/29289" target="_blank">📅 01:43 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29287">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ig7dbAWluVnBqrmsd2BhSn78L1df2-M4Xqm_jbo02rWdiFRtxfva83_GDl9pXc5mFWKETG-ozGs7I_bq9e2cTTfKk53kHXJsixFpuGlqJ5CZhECC-YTziVf6EcpUEzm9EjT22LpIseWERQAvMnOOzz1l2F4aBFqUhYWNBHr7dixQL37xFJ08KRuwiyw1xqz6k4RsUC3EYvcHngB1MCaeBWMiUuqEQUCytykZ8bu739AsELcfjAq8RmLh-kr_eVNz4VIC6sWrCaEjptWZxvtmpAztTRE9nXaZWd_Rl80lWIuGUtq36uV2XbqkX-FgqpbOHSfG8VL96LcvU_rSRIpSiQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌‌‌‌ دیدارها‌ی‌‌‌‌ امروز
؛ آغاز فصل جدید UCL با میزبانی کهکشانی‌های‌مادرید از تیم سابق آقای خاص!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/persiana_Soccer/29287" target="_blank">📅 01:35 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29286">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/prRISydCrGW-yIRv8sqRsQjNKvSS-80LA-oygw9zpXVqU2emTYEp40AlqcpDF83T3eGRv8J9SFIAeI7Ea9C9Z2e_E2-ParLD_fx718AIgAjN1J38vfmwgNWmGo5_ejZKjRLtCuQymqsnMk2FcqEZqTs1OID2A4x1gHCwEv7bKjnHXIkuB3OFnVObMdVMv9cz7nDyCk_gLR5yYC_TICS1BCHyapQrGc8IeafYplrwdN8_BtaOu2fC8FPsWCqFTEwbNZ2hL86KUr6XDBu3_niykSY4mhmS7cz_vgZuWQJ0a3UItW4qj0V4WM5p8Gf23DGyUJxgOEEuPP-wKFzGSrfM1g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج‌‌‌‌‌دیدارهای‌‌‌‌دیروز؛
برتری‌ارزشمند پرسپولیسی‌ ها مقابل ذوب‌آهن در پایان هفته ششم لیگ ایران
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/persiana_Soccer/29286" target="_blank">📅 01:35 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29285">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/E-Mtrjab160LLJT04DkgcJKn4vHRRBE2ai_nd-zzMOg8Ql-UaALpgSVM-TXZ1a6dxhz_6fetH9tY9ffiqIlZn5LQDqca3OSwGufUjzfUngKs1xM7JJDRLRYkBRUdM0Sy5bSF2CmFylmO-P0Q-v070bQm2IxgrTkYgUjomuCgcxH8HUSd-7mFYF9HAJvSPx7WR85QgaGmFnqD6lEynkrQM8CNsZnodLJLLbgtcTlZl6eBQFNO7fP72wsluvWg2wYsDknvTYSiMnL1UQRwrFcHrCwyBGy8RnddWVx9_1R4HOTEcXiqu2fhIgCJEoZECYENUyYQREAq8eRuKRMsgmHibw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
طبق‌شنیده‌های‌رسانه‌پرشیانا؛مدیریت باشگاه پرسپولیس بزودی‌جلسه‌ای رو بانماینده دنیل گرا برای فسخ توافقی قرارداد این بازیکن برگزار خواهد کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 29.3K · <a href="https://t.me/persiana_Soccer/29285" target="_blank">📅 01:24 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29284">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CQCQul8tfod6MqiDN_vYbGdQI6Pw0X6b8ZXMctyZ24DXFNULlSuDmS2aaArsH1eAJJ7es-FsCT1HBaCXlfeV4SCow8nux7CXT-wAXHlEFOF85Z2x5IXIHOa5Di_GVmqimI1pCZgxXg4vagIenLYm14KkqRxNf2CASD1C-Fe_DtK07RgPa-lP2FwN6EFw2qqXSmkSz-aGmuFpxzlCn2FN57xyeGFzQF3iz-iXcUqxZnhnsDTDS8cifD2n5sUneYbnXLf4V2Mm_eRzCpu8-pJMABujnU8I0zs20aCmvSzVm4Uz24N8-sA5AL2rnjjMda9D2gcRWwlLcpvKjB64qDUMrA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
از پس‌فردا دیدارهای هفته هفتم لیگ‌برتر شروع میشه. تراکتور دراهواز به مصاف استقلال خوزستان خواهد رفت و آبی‌های پایتخت با پیکان بازی دارند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 30K · <a href="https://t.me/persiana_Soccer/29284" target="_blank">📅 01:11 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29283">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4c1c191903.mp4?token=BC6qG-D58NKl_4-dj7Amp8lQkSGZOdBXBFkURalj_0JzGgEFpmvWDfVX8G5A1jNugWKXCEFWXfXrr38AVddYLKf_Pq4JwQq6jpFbhACFjGmJHhbJ4NxQuR2vJ_DK3BRX8F6IDGxUQdoyXhRzaBhsngrow6XMpa4FuvZsF-fkHjvAj-iUdmzcq8svszzUMxQT4uhtcCzFgpN9eZOWtXM6IOB6Ogy4XxHtAn3O5oPzad6xXp-5tbnTKEOoRrqYC7HcfvOMRgzsL3aTqNHvZsOSLZARDEaEExXRoDgUNGN35s2baPCEUfOPCzJX_z0g-lQmh8ecZZVs_dOvWVYWWR9bwQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4c1c191903.mp4?token=BC6qG-D58NKl_4-dj7Amp8lQkSGZOdBXBFkURalj_0JzGgEFpmvWDfVX8G5A1jNugWKXCEFWXfXrr38AVddYLKf_Pq4JwQq6jpFbhACFjGmJHhbJ4NxQuR2vJ_DK3BRX8F6IDGxUQdoyXhRzaBhsngrow6XMpa4FuvZsF-fkHjvAj-iUdmzcq8svszzUMxQT4uhtcCzFgpN9eZOWtXM6IOB6Ogy4XxHtAn3O5oPzad6xXp-5tbnTKEOoRrqYC7HcfvOMRgzsL3aTqNHvZsOSLZARDEaEExXRoDgUNGN35s2baPCEUfOPCzJX_z0g-lQmh8ecZZVs_dOvWVYWWR9bwQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
این‌ویدیو رواصلا ازدست ندید؛ خنده‌های عادل وقتی عضو هیات‌مدیره‌تراکتور کلمه "بی ناموس" رو به زبان میاره عالیه. تلاش کرد سانسورش کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 29.2K · <a href="https://t.me/persiana_Soccer/29283" target="_blank">📅 01:11 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29282">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Q3OT7ShPdKBmO1y3kYMnrIwsth6aWS367_t-IjhEuYpgrilH91F-e5i0QNgL3ADPtP_ZMGmq6bhUsHuqCSriIwo8NtmV2b4t11FkT6JwFhZSieJpuAdlzJw-5B14_BeLpmYdqN18Xn_RDhDTerxZ7hdKBgGiVOIHp9Igv_9GST2BR99tObDQ2WO0hokSB1xGIsxnswlvyvH9ytMl9EjwKo-5_LGUTPHThNQfpm7k8cr0UeepULPU010UaOtQzTCAU7TGg_xDo3plty5YCZKHiZ9-mjRqXlvcxzazxRqm1B8QwSmIa0gT2vFdqxs6qarWcQkwwmCLFEQfuT5MlhQ8PA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
سایت جهانی WePari
🔥
😃
😃
😃
😃
😃
😃
😃
😃
🔥
بازگشت باخت به صورت هفتگی
🔥
پرداخت جوایز سریع و امن
شارژ حساب از طریق ارز دیجیتال و انواع ووچر
┅━━━━━━━━━━━
🎁
کد هدیه ثبت نام: Wepari2
👽
ثبت نام کنید.
👇
📱
نصب اپلیکیشن اندروید کلیک کنید
💳
آموزش شارژ با کارت بانکی
💸
آموزش شارژ با یو ووچر
💰
آموزش شارژ با ارز دیجیتال
🌐
آدرس سایت
👇
til.ac/0L4vyJf
til.ac/0L4vyJf
📲
کانال تلگرامی
#وی_پاری
:
✅
@Wepari2</div>
<div class="tg-footer">👁️ 28.9K · <a href="https://t.me/persiana_Soccer/29282" target="_blank">📅 01:11 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29281">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7672fe1ae4.mp4?token=pPCsFgbKDQKqcrE-9aLTEdUK2Oq34a4ODPjVsiuUDWx8hiwPFbscUoh2NIm0JqVeauQm4oukVQK8Ct6ho25HA6m_Vs55jZ5Df0KCK6y5bjr-G9OU-Eg_Hlpfhs955oSriF5Q1QWRzDNEDbsh4ajPh9ija07jSjNGTJMj9FzZvMIHQST7wj-NTNpvg78bQ5MtI_XZ1yfw7eWTDfwZwi94OmDKJQa0_AwgieyA1sOgAe8IhevkBKGDXbp2iKZ_HNhVJSObEUDqyn-fxIAHxIxstiyEEpr91MFfJOQKn039gWVDfRT9Rt83PkPbN4rZsZKcAX6oU1l286YJ3J-Ziehsrw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7672fe1ae4.mp4?token=pPCsFgbKDQKqcrE-9aLTEdUK2Oq34a4ODPjVsiuUDWx8hiwPFbscUoh2NIm0JqVeauQm4oukVQK8Ct6ho25HA6m_Vs55jZ5Df0KCK6y5bjr-G9OU-Eg_Hlpfhs955oSriF5Q1QWRzDNEDbsh4ajPh9ija07jSjNGTJMj9FzZvMIHQST7wj-NTNpvg78bQ5MtI_XZ1yfw7eWTDfwZwi94OmDKJQa0_AwgieyA1sOgAe8IhevkBKGDXbp2iKZ_HNhVJSObEUDqyn-fxIAHxIxstiyEEpr91MFfJOQKn039gWVDfRT9Rt83PkPbN4rZsZKcAX6oU1l286YJ3J-Ziehsrw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚪️
🇫🇷
کیلیان‌امباپه ستاره رئال‌مادرید:
من بهترین بازیکن دنیام؛ و با اتفاقاتی که این تابستون رقم زدم، حس میکنم امسال سال خوبیه برای بردن توپ طلا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 33.1K · <a href="https://t.me/persiana_Soccer/29281" target="_blank">📅 00:32 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29280">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/932bc654da.mp4?token=mGhWRW-jQCKSr81aZ13rLeGqNSP0QVHkq65650ahSH-fhAj_zoKTRyjTqMw3cUGdNPJsufAU9QaZBXTSDHBF3uw_sGZ9icfe-bWYAFdnOnRnTlbEofzM7tpM5l7mbvdaH7IU3HM8STzFgUzK0mlbXekOzsVWp_FJDBi8vxccbvYfCMM8P3ucw9PrCmtL_RL8T3TcZwKS924_0jpuEop962jmOwiRnGLhgxoon7dAqNpLgBJELgNEjWrPBVcIAxjCRwF4c0VUK_-m9c2cRzt1awu69Tj5ERugBYjLAybRV131BIwYE5HgeCMvYmGTEe_D6rJQLk2VKksQCTv8hmBFKw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/932bc654da.mp4?token=mGhWRW-jQCKSr81aZ13rLeGqNSP0QVHkq65650ahSH-fhAj_zoKTRyjTqMw3cUGdNPJsufAU9QaZBXTSDHBF3uw_sGZ9icfe-bWYAFdnOnRnTlbEofzM7tpM5l7mbvdaH7IU3HM8STzFgUzK0mlbXekOzsVWp_FJDBi8vxccbvYfCMM8P3ucw9PrCmtL_RL8T3TcZwKS924_0jpuEop962jmOwiRnGLhgxoon7dAqNpLgBJELgNEjWrPBVcIAxjCRwF4c0VUK_-m9c2cRzt1awu69Tj5ERugBYjLAybRV131BIwYE5HgeCMvYmGTEe_D6rJQLk2VKksQCTv8hmBFKw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
چه‌دردهایی‌که‌ بافوتبال‌فراموش‌کردیم؛ ویدیویی زیبا ببینیم از یکی از زمین‌های خاکی فوتبال ایران!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 34.9K · <a href="https://t.me/persiana_Soccer/29280" target="_blank">📅 00:19 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29279">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oQkjXTB364Xx2QDRLraocKFY3jDpOhvabPdoLhNJ-0pqv3l5t0QJai89Vy0ezgBWNQEUzdDhHmzkzaxk7PR3_NirN_j7Zkx4gzX3K1rk91qzvGTY9wbCQ5tB3nI5Ni0gi3QX1f-WQICimX8oSaEc84xJjvCCora04WT911Mwgfa3YtXDcbkMT_jexF4aV_C3wum6eVO7bbBdq_qLU0g1Sn-A0CPONhOwkSKzsnQ2oPgv0MIBulw2TjAks9SWjGtOFDV18OxaJe21Kvv0zgOAwfsm5gqOj2p0rCmFp26u2Q2J-cRcR5JLAAZcbAQFWCVapOv2pdtt1rJKzX0hpNpvyw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
سه نرخ بنزین در جایگاه سوخت به این شکله که در تصویر مشاهده میکنید؛ نرخ سوم که بنزین لیتری 10 هزار تومانه از 12 امشب اعمال خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 37.3K · <a href="https://t.me/persiana_Soccer/29279" target="_blank">📅 00:02 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29278">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iHMoMtx1yij-mJb-O750eGXGyF6ZEUyKunIV7xMAQ3lR28bGXLciYJU88cbTybpBJ_cGmDGl2q2mcGrSG4ascDC7AMJUln2ubjd8PESzovmw02-ITdupNhKstzsYm7IKaudXT_t7We62pbMg_2_ADQvoVPuIAz9_h_fiy_VHGGZGRPxTLjHwkddVulqSuiFDQZUZNWLSF4DVLdPgaW678Z2EyqU1jwaD30ke6rqg3qv1B_Cmfq5P6j2iaCSjjssROEFJqlB3RoPfIdg8R5KTASXMLKuQ7nKNCCiRH8krerLSnziI1xZjKm5NCSvNA49w-G-boU5XakIlLT5O711_4w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇹
ترکیب‌احتمالی و پر ستاره اینترمیلان برای دیدار حساس فرداشب مقابل رئال‌مادرید در هفته اول لیگ قهرمانان اروپا؛ ساعت 22:30 از شبکه پرشیانا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.1K · <a href="https://t.me/persiana_Soccer/29278" target="_blank">📅 23:56 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29277">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/W1WKL7hhYwrCafDEGoC3HjonwuJhhmaD9J_C5Rz-r9iceBslPVxWKCjjHwlA6CFWJqO5UXsjcGzNchiObtzLVu350OtSHJHeumwaFY7oYzfL5EzJjAnQAJ8XJ-L63O7noto5aikSDC3sQtyGLFBLKfjC6HsPZMlPjoU1NUMY1mSvXOaaRU-NDbzK-nRaa-17ZGRod6EulpMip-VFkLMYA5vspowtQ96XQ5ON0tRxxfhCyoeBEq5e4OGlA3AlqDqgyhrrMrGFwPG-yiqtWnhFFEZmt5WAfyzuD2Rtui6tpZbE0OUxWIjUs4zNJqydXMXwZEX7PJ08BdGIPQ-gSiK2WA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
وقتی‌میگن‌فوتبال‌غیرقابل‌پیش‌بینیه یعنی این؛
الهلال اینزاگی امشب با تموم ستاره های گرانقیمتش همچون مارتینلی و واتکینز اونم در خونه دو بر صفر به‌تیم نئوم باخت. حتی نتونستن به‌این‌تیم گل بزنند. نئوم تا پایان هفته ششم  دومسابقه‌باخته‌بود و چهار گلم خورده بود اما امشب کلین شیت شیرین کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.6K · <a href="https://t.me/persiana_Soccer/29277" target="_blank">📅 23:35 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29276">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c4bb9f937c.mp4?token=ED8UtDrbDDt5erE1MJz550eJ_cLmkp94SFlZfnCMrsxLHeOFwrEiAQB05waobPHo-Npp6osDfScm7ffCyL0VdUxj3C1hKr5AZKMc-lZ8a_W2LDVon7lOTirCQtJi-788e2XVa6ZmFr9PK3dDrRpx5BOLAmfq76_nl-4LN822CwzZVVHtvUP2NqVILPJ7KsF09Plv6VyAdSmQPM3RW6zw4ha2NhPiETgNMovvkZ8oU08A70VpYmviXkzT8xB2c6jIKnoc5HIfRieA-BH2Z6e81CE934ZVv9F44wV4MftjLQn1w2SjYShp0Sl-bbqdvJ8MlLgz1ef3qlVrDu8lF1zfyA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c4bb9f937c.mp4?token=ED8UtDrbDDt5erE1MJz550eJ_cLmkp94SFlZfnCMrsxLHeOFwrEiAQB05waobPHo-Npp6osDfScm7ffCyL0VdUxj3C1hKr5AZKMc-lZ8a_W2LDVon7lOTirCQtJi-788e2XVa6ZmFr9PK3dDrRpx5BOLAmfq76_nl-4LN822CwzZVVHtvUP2NqVILPJ7KsF09Plv6VyAdSmQPM3RW6zw4ha2NhPiETgNMovvkZ8oU08A70VpYmviXkzT8xB2c6jIKnoc5HIfRieA-BH2Z6e81CE934ZVv9F44wV4MftjLQn1w2SjYShp0Sl-bbqdvJ8MlLgz1ef3qlVrDu8lF1zfyA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
سخنگوی هیات‌مدیره‌باشگاه‌تراکتور در گفتگو با عادل: عالیشاه به خداداد‌نگاه‌کرده و گفته خفه شو بی ناموس. فحاشی رو بازیکن گل گهر شروع کرد!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.2K · <a href="https://t.me/persiana_Soccer/29276" target="_blank">📅 23:22 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29275">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2ba75a2423.mp4?token=EiPaP7trcOQCZt1c2MmavA6DZzOzWHI4_uI_Sz9vYN2KrGTDz17_D8PXgmyHH28TcjZ8bD3l_GmocF7FcuzUug2wVsUjsMslzS-5eYkKCfJ-wSEhgvakDWkhQbbKMCq1G_rbvc93_KXAJAts78BezGHIRxeTQtnBi01329_FZ3IciOw-VPwvCwlBvqU0ryWjxqalJEreZtA_bWPqQXgQ5w3YsYAy6ZA255P0bZ-K0prvbUamcJVE173X8rn6wVy-nGtJ-4ios1AvX1ZQ0bOD_ybHsdP0ykyo61sGTMG0YQgxvC3RTpR0jWii6ZaUFwXujnp0Qx-J8ylQfbG0J2ON2w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2ba75a2423.mp4?token=EiPaP7trcOQCZt1c2MmavA6DZzOzWHI4_uI_Sz9vYN2KrGTDz17_D8PXgmyHH28TcjZ8bD3l_GmocF7FcuzUug2wVsUjsMslzS-5eYkKCfJ-wSEhgvakDWkhQbbKMCq1G_rbvc93_KXAJAts78BezGHIRxeTQtnBi01329_FZ3IciOw-VPwvCwlBvqU0ryWjxqalJEreZtA_bWPqQXgQ5w3YsYAy6ZA255P0bZ-K0prvbUamcJVE173X8rn6wVy-nGtJ-4ios1AvX1ZQ0bOD_ybHsdP0ykyo61sGTMG0YQgxvC3RTpR0jWii6ZaUFwXujnp0Qx-J8ylQfbG0J2ON2w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
ویس فحاشی برگ ریزون و باور نکردنی خداداد عزیزی به امید عالیشاه در پایان دیدار امشب؛ میگه منتظرم بیاد بیرون کارش دارم!
⚪️
@Persiana_Soccer – ویس فحاشی خداداد</div>
<div class="tg-footer">👁️ 43K · <a href="https://t.me/persiana_Soccer/29275" target="_blank">📅 23:07 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29274">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CBgkVgHf2XvgSfoYnc8CWBy_5GLaHZG0pijsZTHoF07ZHhWJxbWz5i7dmNfTCx8UTw2zaxonhmRuqrBRabna5jLRewd0ja9Bda-_Ww7fqYeFxSJadBgnNXn9_Uyz0eyReVGskVg8SNLJJ3v9Lwemso4J_n5kKWL-jSVAiHpD0Yqrgisfcn2UrB9-Havs1uciG6Hbs36DYTh4mLJUWTn_FW2Z7v2Fojq1Xm168gBtfeYdQ7-Xv0crHlQjl3x0N5ZBmVfv15sTnMF4NGqiy1ERwko8UzqmZ7xAGugUM7Lnz5e4h5mpaGcIQS7VQcYD8axT30KBvfBjbXjeJm58csTpoA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
خبرنگارشبکه DAZN ایتالیا که روی برد اینتر در بازی با ناپولی شرط بسته بود و 650 هزار دلار برده بود. پست‌برگ‌ریزون ریپلای شده هم حتما بخونید!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.7K · <a href="https://t.me/persiana_Soccer/29274" target="_blank">📅 22:45 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29273">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cuodZ54gXhxJEq3fX6Y1laKsUHJg_ufhQYKUsHOvmSivTxF8vd2-GEGD6hwgw8ay6cC9-bBNjY6a58JsbW696bn3AfVRX-yiZlN54iiHOcu61f8HbbhHXLTKpfNw4mokurmIExxRRXMcqJFqih-RoI3hAGyQ81-PDTYlsH1EXfAmeBO-BAH9M7FZ_aTzSwbuKnN5QgZNmFMRFew6sC93JEA3SQz5BB_ZihTmL8dxbHsTUtv_oTcuEXZ3GRbiag8cEiXL0BrPKVwcpkF_iSklw4IjywH9d_WAtT2bUHatVEMObmV0kbvldJ7P3ksU8QRaMgul5360xhgzXL-1rQXviA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
تایید شد؛ با اعلام کمیته انضباطی؛ خداداد عزیزی سرپرست‌تیم تراکتور به‌دلیل فحاشی به امید عالیشاه چهار ماه از همراهی پروشورها محروم شد. عالیشاه هم چهار مسابقه گل گهری‌ها محروم شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.1K · <a href="https://t.me/persiana_Soccer/29273" target="_blank">📅 22:35 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29272">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">📹
خلاصه دیدار امشب دو تیم پرسپولیس
🆚
ذوب آهن در هفته ششم رقابت‌های لیگ برتر خلیج فارس.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.8K · <a href="https://t.me/persiana_Soccer/29272" target="_blank">📅 22:25 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29270">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hjPFfdiVus_robR9KlK95LSvbn5hRunptDKp4b8TGrrouctz-onedL7ne4rNv0S_S5o3kjBOahRs10cMOvwiKDzaeO_it870tVlFBQfaB4jGTnIaLq_lTc-6U70tVZY_khS4nyeSpdsP_94srz6x2f-UyWvXawPtSCNGjNwx1-K2itEyj9fJUdYCk46mvUspI-YdPgmxplOp535YdQt1mvqsuYAklf6Y19jZClWJ9RvdnRSgS--Tl97sQsfv4nVzF4XbQyfh36Gqzf_T4N3gtou0-9RGaEujqSEea4DPfhv1glFyrhZYFoXr6oUQy3NzblKtzX8atwd6kofKlOXm5Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/r7eU02SDgtbckqd6G5n8hi8Tsf6FtKXHk-051RbvDV9d-I-y0y7RVYN7Ptf4IpZCB1bjOqby5xBeX5bOKOB8qJP8GYQCJ0IjJC1pXPmW_tEhP4Qccf8S8ZxZoRH6hamgESabo3wZOUW9_TfsjeHxFXAfixGXUJ_Sb3sAAFdW7TJK50THuOjwQTQJZ6C6QxQdM8qcQBGYFgewwIx1RnfBw9vRTFwsCI3SFMdtUjDn8PoRU3UfaKWkKSMelzSJqZ2tteWoL9J1TBm5kFGqf45f4JdZTzUbDOy-U8OLUVv_JVyHo35zuT8PBa8RsyO4xT3DOpiQ9O4SarmetKf4MGaKFA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">✅
هفته‌ششم لیگ برتر؛ دشت سه امتیازی ارزشمند شاگردان‌مهدی‌تارتار در دیداری‌خانگی مقابل گاندوها.
🔴
پرسپولیس
2️⃣
-
0️⃣
ذوب‌آهن اصفهان
🟢
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.9K · <a href="https://t.me/persiana_Soccer/29270" target="_blank">📅 22:09 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29268">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/dzN6GASkOoxPsUfuT0MleUyB1Q0PlrZdSOZajEg8u83YYQH4QtbF2lnZxRHN5CMezfuviXQgJymhPQAZ2M8WQ_pilOcaYsnDVVtZCZNAdRgBIAb0cEPeQh76in4JZgS3WG1HHGQtz-YoiKtDJ-7d-YCsR_yeO8JYVUmmypok97aRlLYGijBSu-1ZCxXBS2Ge31qmaTEiUYPSbUa3zLcvRhsb24AfpHHq0EgW2GeWCFE-HPo7iXXYFAMQfj105Prv3ZsYWD1CwadrDKG_QLTM_qXdDLZBrq0lGgX_gXYwvCrNJea_m3a_VN2ZqniD1LH9Z5TDaDDAQ2XOikCmi7kg4g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/fM7-8zrNX3QRtYqbV9nPh0o4xCxW3RSli2GKIg63AllWs_ExirIstq0gfJl8jjT1wJODqOOy_pxKsjHh0f88BwzYubbLMwz04_jVRUylyaAd5IMoYuYdze3uuMl_OgMPh48U1j_iSLryZvgRFPCxy9abLUjgtsaLQrdJDHXvX-Qy4XbY8trkEFb5u9EZTp86J5SgqdNCxPOUDLkrMHR97eO1Hv-HbaG5ayfqSFaAgL2kax5Y39pUT0j9YUbP3h3B2WkVi_GLvvSYj1eRpvkM3Gd-rUMZkizWJiA0BhW0PmcZnKLes_i5bHEjoQM9MRUJOCcaXPQ8Tfm2hN6pAPWwGA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🟢
🔴
بانوان هوادار تیم فوتبال پرسپولیس در جریان بازی امشب سرخ‌ها مقابل ذوب آهن.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 46.2K · <a href="https://t.me/persiana_Soccer/29268" target="_blank">📅 22:00 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29267">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/93952feaa3.mp4?token=bo-VZYMwYYWDMS5SKyY6HVm5njM1PvRHNyK2Xu3pploKwM_3ZMisrTJ9fj2mfdQBo1jojjUh1JJu55j8r3PpmuKrjLNsNg-x3oDw0sa770siRITeOPc14lo4s9ez4EC09-mGX1EGMLVN68J7b2SHL2x0NarNqCmiS_nTU8vHVTiINTcWxfuPiRURyVRT89ZVcMlM4cilUZaS6SvwxKZuYWZzm56P4FOKuJnN7wuxztzaWZWTZ7zk9Vt-Ly_CCD-ReVEAAPU3rhekoHjelt1ItqnSUoahAvGwzH18qpGbhbRDh2Sq1BpNq70u7TskCsm7eGYRDK-qhbh4SJkFjaj67wSbNv3aYFpEobJ23aU5Z2bMQjSjIJv9aVebLyu_ajzzNtkfng73_ZTT1QgBZRHJWfgTEYEzcPrW1iray8qsV6UIGobWkYSO38kAVFvqUct1OCYJfjN1yxJp1WveyxfUhaY8cf21juKYtjThb2xM1fiKt4UM4YjH5b322dwpOLuXynoSM4SEJs1Cwr38S4pqJcmKw_HEkftoq_QaZKBRGon_1JkMyzXtL6mpEcXUxKLIaFc2jbM0DGzjR7eBzFm0aJYd_nzwGeVLfHe_BrXNjJnJFwoxWP0prN9FPym_q1C219_mLYCsQNS2q9WzwExYNOWL_vVHYIKEImvBBa0sdU4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/93952feaa3.mp4?token=bo-VZYMwYYWDMS5SKyY6HVm5njM1PvRHNyK2Xu3pploKwM_3ZMisrTJ9fj2mfdQBo1jojjUh1JJu55j8r3PpmuKrjLNsNg-x3oDw0sa770siRITeOPc14lo4s9ez4EC09-mGX1EGMLVN68J7b2SHL2x0NarNqCmiS_nTU8vHVTiINTcWxfuPiRURyVRT89ZVcMlM4cilUZaS6SvwxKZuYWZzm56P4FOKuJnN7wuxztzaWZWTZ7zk9Vt-Ly_CCD-ReVEAAPU3rhekoHjelt1ItqnSUoahAvGwzH18qpGbhbRDh2Sq1BpNq70u7TskCsm7eGYRDK-qhbh4SJkFjaj67wSbNv3aYFpEobJ23aU5Z2bMQjSjIJv9aVebLyu_ajzzNtkfng73_ZTT1QgBZRHJWfgTEYEzcPrW1iray8qsV6UIGobWkYSO38kAVFvqUct1OCYJfjN1yxJp1WveyxfUhaY8cf21juKYtjThb2xM1fiKt4UM4YjH5b322dwpOLuXynoSM4SEJs1Cwr38S4pqJcmKw_HEkftoq_QaZKBRGon_1JkMyzXtL6mpEcXUxKLIaFc2jbM0DGzjR7eBzFm0aJYd_nzwGeVLfHe_BrXNjJnJFwoxWP0prN9FPym_q1C219_mLYCsQNS2q9WzwExYNOWL_vVHYIKEImvBBa0sdU4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
اتفاق‌عجیب‌پس‌از پایان بازی امشب دو تیم ذوب آهن و پرسپولیس؛ اعضای تیم ذوب آهن به خطا روی بازیکن خود درمحوطه‌جریمه‌تیم پرسپولیس معترض شدند و VARهم‌صحنه را چک کرد اما داور در نهایت این اعتراض را نپذیرفت و به رختکن رفت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.8K · <a href="https://t.me/persiana_Soccer/29267" target="_blank">📅 21:38 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29266">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LlbJMxlor0VYGRh_ChBqhmEbOH4uOy8HRGCHXoypK9fAFsC8W2dDI8VI82etVBf46TueVsrWg7BROCNdlKDP99p5zBxVLaSfCqzg45zkTUK_ww2nnIMdFQ-nkM1U8EaVkczGt-BIA5OTcgdwJWTthdaJWi_SdW2x_49VUpVchiDREtAw1zYof2fvmnUYffnWLvlFrffL0OjeCp12y5pEm_-GQvX-fyUBruKcYCWEIeMkfZnHzsN4kB9yIjnAi0Z5mULjiC-x8he4yDQZ3W9CNlzMABm0GZgt9__cQBpX6IPtAhJl9FOjLeV9qYlWc7DZIplWLFcv6jqj3OJO6P1LnA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
برگاتون‌بریزه؛ یه‌پسر ۱۷ ساله اهل مکزیک بوده و بعدِ اینکه دوست‌دخترش گردنش را مکید، جان باخته. شدت مکش به حدی بوده که باعث تشکیل لخته خون دریکی از رگ‌های گردنش‌شده‌ست. این لخته به سمت مغز حرکت‌کرده و باعث‌سکته‌مغزی‌شدید شده و پسر تنها چند ساعت بعد جان خود…</div>
<div class="tg-footer">👁️ 47.3K · <a href="https://t.me/persiana_Soccer/29266" target="_blank">📅 21:34 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29265">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KcFeBaf6PRyRKwAeJd6nj1p_D2SUqJuDYdbBQ3pphHs9D3LfcIPtbc5znAfxKuzT-xE4rCPO9DFB96aiqRB4EJVv4ie_Py3M7aLGYpNRRWMYS1OD6BMItHS4I1qG_kx-UIhAqQ3rC7RIe_ZwDTL5DLd4wupqMT6CfLXTCY-9RJwiTQRJQwVLTue_d85TZMHLsIaIH5jpCciYltCLpGo0gHV8ZHms85Cfc_2kfiRRNo-ywfk2KTq6LmLZAROg991GZkuADL-Xv0Coi3dDAFHLYA2XP6U331DSdzOGviS7soZTaYGhB7QJhDun35cHwPMdoI26X4wcWfSues8XpSa6IA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
ایساک کونده هافبک‌شانزده ساله لیورپول با عقد قراردادی تا سال 2033 به منچستریونایتد پیوست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.4K · <a href="https://t.me/persiana_Soccer/29265" target="_blank">📅 21:22 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29264">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a7f001dc45.mp4?token=gQElSuWCTm7pJBhSXn8mwhhONsUeavficUW8AN1xWXZlTByNuo-d_X7dqGHczku5_zFvyyiyC14MoN__HCtPc2if--6SvXPAYEVHUEACmk8BhQAgY7npTGXtTkqc76S9UDFj-Bhz3ZAdYrmNg9tiMT5UkZv7xIgH5d_piUb1UALx-LwHVX1KRVVtj1ZA12Y-aQbWM2V97ZyFV9X2C7twC5EPfOyxDt7sVEG0_5U_2oKVSAvIiP8C4j4NtFTL2QdbtJ_cl9d6pgrbXfGqwreO0baExJ82thacRK93qrg4mUHIJrX4DVNBC9UsmhNObVBw_RKZyx9Iz1Ty6Nkndw3LSg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a7f001dc45.mp4?token=gQElSuWCTm7pJBhSXn8mwhhONsUeavficUW8AN1xWXZlTByNuo-d_X7dqGHczku5_zFvyyiyC14MoN__HCtPc2if--6SvXPAYEVHUEACmk8BhQAgY7npTGXtTkqc76S9UDFj-Bhz3ZAdYrmNg9tiMT5UkZv7xIgH5d_piUb1UALx-LwHVX1KRVVtj1ZA12Y-aQbWM2V97ZyFV9X2C7twC5EPfOyxDt7sVEG0_5U_2oKVSAvIiP8C4j4NtFTL2QdbtJ_cl9d6pgrbXfGqwreO0baExJ82thacRK93qrg4mUHIJrX4DVNBC9UsmhNObVBw_RKZyx9Iz1Ty6Nkndw3LSg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
هفته‌ششم لیگ برتر؛ دشت سه امتیازی ارزشمند شاگردان‌مهدی‌تارتار در دیداری‌خانگی مقابل گاندوها.
🔴
پرسپولیس
2️⃣
-
0️⃣
ذوب‌آهن اصفهان
🟢
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.2K · <a href="https://t.me/persiana_Soccer/29264" target="_blank">📅 21:16 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29263">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qohXO_p7WW1irmjSQ_4n4TubYOyqcYl6FhaBZVu8B0XgvSWbWaoQB9vwR2Z8mBtHaVPrub-cGy8FBpIF1q2qMhSIl9hf7ZMRPkRqWZ4fdvw3L90s_uIkm3siVto9DcDAu_oHHFD8_JMG7IkqkISNT1iJgzsjOw7L2hhGu1Nfs2pYwRSFTd7QVtnsPn8QWH2zd13HjRvbaARzu6qeFhyREdL22yb12fW179JeGH3A6q6LNzysJix521XOiWObxpnKmio9L3v9qLV_YHv_3mII7sTchUSfPOjlBk1Y-qOs_aiYqIADELdS3wLJyzGKVlRNsbt3Er40mpDuw64BZ5b2dA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
این‌بار علیپپور پاس گل داد؛ گل دوم پرسپولیس به ذوب آهن توسط پوریا شهر ابادی در دقیقه 63
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.8K · <a href="https://t.me/persiana_Soccer/29263" target="_blank">📅 20:59 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29262">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fBRdvb1fEmKbgaZvaPVsDe-PIkoGfkph0__2lLDT4wK7sxiTsF7PGkzveG5Bxtd3Z_2fNrKgCKSVhiF6oUoaR_ysdS0RpyQu1zQE4P3cgLorXfdXFDWUgoNTPU-TtLnYy8kwf_bRoG-rYeLz4tS7zHTGF3CYztp-mSh2r7bJSgF1hIFQDxenjSHz0OYfQu0wehiylxzT-BDuSf0oMUC4X9ESGu_cnO_lPZi2fJTFkpDp1hVX0V0pLN4de8iWp4SaXCvVvDitFWXEavfBMftzxQ8zQNOtcJKdImJ8czXnOOyL4ba9ZkusXiMu6ijwU0P5rUyYAHA148tMKl3PHkat7A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
این‌بار علیپپور پاس گل داد؛ گل دوم پرسپولیس به ذوب آهن توسط پوریا شهر ابادی در دقیقه 63
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.6K · <a href="https://t.me/persiana_Soccer/29262" target="_blank">📅 20:58 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29261">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a13ac35bb6.mp4?token=PRYi5vJV85-Sm94TbmpiVsF2mNjuUdwDQHBXbwk2AeNpwTLUevB5j6toxEx6_QgLMyELg9KsjYOFgtpg-KD2mecAFDqnuDg-pIjHqONNcqL7uVsDcnQPHfFfpJGXRC-OgF_cVhSKCFemauriV243w0D7NDApoa7_oXpEveXXmX_MvSl6UWNzP_lFtXeig1tpPYbkEVfrEvpHua3a7Xw0bGYc6H505-TVQ_fYq9WlIMYuK57X1kZFRn4wEV39RsMF-Le73ivPeyUH98XUODRUNurxgPk-1nXA4wxmmlcOrzB22QP_MuZjpSyOoo-W0iux313zUmczSKbQGeK4K066pg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a13ac35bb6.mp4?token=PRYi5vJV85-Sm94TbmpiVsF2mNjuUdwDQHBXbwk2AeNpwTLUevB5j6toxEx6_QgLMyELg9KsjYOFgtpg-KD2mecAFDqnuDg-pIjHqONNcqL7uVsDcnQPHfFfpJGXRC-OgF_cVhSKCFemauriV243w0D7NDApoa7_oXpEveXXmX_MvSl6UWNzP_lFtXeig1tpPYbkEVfrEvpHua3a7Xw0bGYc6H505-TVQ_fYq9WlIMYuK57X1kZFRn4wEV39RsMF-Le73ivPeyUH98XUODRUNurxgPk-1nXA4wxmmlcOrzB22QP_MuZjpSyOoo-W0iux313zUmczSKbQGeK4K066pg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
👤
روی پاس هوشمندانه مجید عیدی؛ گل اول پرسپولیس به ذوب آهن توسط علی علیپور در دقیقه 41؛ این 96مین‌گل‌علیپور باپیراهن پرسپولیس بود و باعبور از پروین به دومین گلزن تاریخ تیم تبدیل شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.7K · <a href="https://t.me/persiana_Soccer/29261" target="_blank">📅 20:30 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29260">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZSVP_i9B0W_HlHJ129TsBwrqRyQxtdzYfE6Buf5k1_uBV3O1GrkCsNIlw00IGKRfIut5n-rcy-FSrBjaPr6pMnEwp0gXXNzR3842AP1kiPkzkAQqaWLDtvddV7Vgf2XpThMOxvHdZkSoaCbpbhmYEgGUSY68WDowMyaZ_WGrQBFFYasJ-y7PdPSgQdhZNDhm-mLVnIkw2DlndbNcKZg_lIIqTojmdykvs2j1ijxNEfrf1epUSLrHHASY-qPA3crWVb7UdSrjmauaZcqt9F78LZ3zFV6BgwWhY56MUndiq7zzETWyAX0jDlFT-O6mFbT4CpaD_TkaAITdYaIKjnP2Bg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
درپی‌اتفاقات‌دیشب؛ به احتمال زیاد خداداد عزیزی سرپرست تراکتور دو الی چهار ماه از همراهی تیم تراکتور محروم میشه و امید عالیشاه یک الی دو مسابقه گل‌گهر رو به دلیل محرومیت از دست میده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.1K · <a href="https://t.me/persiana_Soccer/29260" target="_blank">📅 20:10 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29259">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f02306a280.mp4?token=PZVxO2YQZ1_aex_aQa_NRMo7Sq_e8Kd6XwfbtpFt9q--Nc7KL1R15hK3613Mamu0XYMuzF-GMnIuHMlm_Sb9JhjTHcjdZqFzrGadrnJVmvNoU0Qc_e3Mx-c5oJQmCgfpPd6O-j5xThcC24yST0hjkjvL6HFqruuk0PKo2Ve9-F0UMxxuo-xh-Uht06QbXzR3YRQeYWLbvq6R4LV4eGwPv0YGd7bvlvdy296rhhJSK6Vuf61CPbV71iU0ocVS5YGxi0FSW_Lf_izwmeSkoNiv_cLOi3264hXZSuTgcDze79EqHeLc6VNhb9McuHzKMGx8Rgh_N96zcR75hUv6asWmBg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f02306a280.mp4?token=PZVxO2YQZ1_aex_aQa_NRMo7Sq_e8Kd6XwfbtpFt9q--Nc7KL1R15hK3613Mamu0XYMuzF-GMnIuHMlm_Sb9JhjTHcjdZqFzrGadrnJVmvNoU0Qc_e3Mx-c5oJQmCgfpPd6O-j5xThcC24yST0hjkjvL6HFqruuk0PKo2Ve9-F0UMxxuo-xh-Uht06QbXzR3YRQeYWLbvq6R4LV4eGwPv0YGd7bvlvdy296rhhJSK6Vuf61CPbV71iU0ocVS5YGxi0FSW_Lf_izwmeSkoNiv_cLOi3264hXZSuTgcDze79EqHeLc6VNhb9McuHzKMGx8Rgh_N96zcR75hUv6asWmBg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚪️
🇫🇷
حرکت جالب کیلیان امباپه درنشست خبری قبلِ‌بازی بااینتر بابرداشتن نوشابه روی میز کنفرانس خبری و جایگزین کردن آن با آب به سبک رونالدو.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.1K · <a href="https://t.me/persiana_Soccer/29259" target="_blank">📅 20:03 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29258">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2e921c3810.mp4?token=XY2Bgpwh6q-VRCyR4gZdR3RPfnVc8iyugfJss10pdqPJb0gnKsZk_GBeVgdeppD6R2wIJ14Sygp1ZU2WxN5Qpd-2h6pNzp1heqFjX1F1YAya7kHhpqdHPamJDaI-qdQEys0YoSHbeo9bhNI_7VYYsmBg6tA5ubc6bH-awqiK0QK5Tdgct7qZfffr8auBwJ86rowdljVxu8ixPU4HT1cGod3iLIEXj9-GsrIPkAZPzUg28Mi1iQ6ZqgWM6MOM7dahDGk3kiwUZ4S3ZYRBrUiRFDAMSqeDvk-AUVAcUO-xsf36MjTHOQjQHnMnkT1SL81XuRDltNL2gCoSkuXttGHtyg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2e921c3810.mp4?token=XY2Bgpwh6q-VRCyR4gZdR3RPfnVc8iyugfJss10pdqPJb0gnKsZk_GBeVgdeppD6R2wIJ14Sygp1ZU2WxN5Qpd-2h6pNzp1heqFjX1F1YAya7kHhpqdHPamJDaI-qdQEys0YoSHbeo9bhNI_7VYYsmBg6tA5ubc6bH-awqiK0QK5Tdgct7qZfffr8auBwJ86rowdljVxu8ixPU4HT1cGod3iLIEXj9-GsrIPkAZPzUg28Mi1iQ6ZqgWM6MOM7dahDGk3kiwUZ4S3ZYRBrUiRFDAMSqeDvk-AUVAcUO-xsf36MjTHOQjQHnMnkT1SL81XuRDltNL2gCoSkuXttGHtyg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
تاییدشد؛ لیست‌بازیکنان پرسپولیس و ذوب آهن برای مسابقه‌امشب؛ بازگشت محمدحسین صادقی به لیست هیجده نفره و غیب ادامه دار دنیل گرا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.9K · <a href="https://t.me/persiana_Soccer/29258" target="_blank">📅 19:49 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29257">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7e05ba1529.mp4?token=kR9rZ_fgAHYgKHtEt_e2g1PYe6MxZV3Bg2yanTVouMzAs4xvNBgZAmSANUUut6FjfrsmY4DnjiJufH-u3Wmfse-ZtgN5FdOpBS7t9P2AHhLZN9HbwkO0QKQHvgVkYxf8WifVkbis5tyC1ylVNq4mrrt8ZcRiQDwUehs9U53UaelWk_xULg6jIUT8G1DmWYlt9ZeH0n0iwIOlEgPJ7TnSdem9-UiLya3SXjGq7MUjZ9St0dCqwMOrQfs8XQN4BOwJaC7h-x8lukEu8pzlP47qXJiDRGTj-LijP8HZSdood8Q2puQI5CBhvGkwHeqWPxzv63aLEkcDdkHLvQ12tAXHPg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7e05ba1529.mp4?token=kR9rZ_fgAHYgKHtEt_e2g1PYe6MxZV3Bg2yanTVouMzAs4xvNBgZAmSANUUut6FjfrsmY4DnjiJufH-u3Wmfse-ZtgN5FdOpBS7t9P2AHhLZN9HbwkO0QKQHvgVkYxf8WifVkbis5tyC1ylVNq4mrrt8ZcRiQDwUehs9U53UaelWk_xULg6jIUT8G1DmWYlt9ZeH0n0iwIOlEgPJ7TnSdem9-UiLya3SXjGq7MUjZ9St0dCqwMOrQfs8XQN4BOwJaC7h-x8lukEu8pzlP47qXJiDRGTj-LijP8HZSdood8Q2puQI5CBhvGkwHeqWPxzv63aLEkcDdkHLvQ12tAXHPg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🟢
🟢
مسعود محبی مدافع میانی 22 ساله مدنظر استقلال درنیم‌فصل لیگ برتر باز هم با این ضربه سر استثنایی و محکم‌برای‌ خیبرگلزنی کرد. خیبر درپایان مسابقه رو3بر2 به پیکان ساکت الهامی واگذار کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.3K · <a href="https://t.me/persiana_Soccer/29257" target="_blank">📅 19:38 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29256">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">🇪🇺
🇪🇸
🇮🇹
هایلایتی‌خاطره‌انگیز از بازی فوق العاده تماشایی و مهیج اینترمیلان و بارسلونا در استادیوم جوزپه مه آتزا دو فصل‌پیش درلیگ قهرمانان اروپا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.5K · <a href="https://t.me/persiana_Soccer/29256" target="_blank">📅 19:34 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29255">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nT3fc5egLOKfKri6qvz0dmlP41oM8eNaE3cW9rU3olDl3XSbUob8rh1Jfy4runRFHdqqowdqHEiAWvAUf5pSiRnZinTbll0bhdycmx5-2EX3q5ui9CpQB9Kwfk1E0nSkP26sFn20EQ8xpm3neai7Xu3DgFTqYacqbP6DMKI3JjvwxKVNIDmlikckDY_cLPRPuZcKlc-kw4x265F6ooH3CH2YZxTQZ_l9CThS1X0barv3UAXc5DM1l5hk6XGw-WDtpxFj_sH8ok_2FQyddWJiJcI2z34t4Z4yD6HYUCMVZaTcxaAy8MtDGgqgxnSWqjyB_2i0kqMENs06_GfWQMUJkQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇹
🇮🇹
دلیتا گزارشگرمعروف‌شبکه DAZN ایتالیا که مدعیه امسال‌نیز اینترمیلان قهرمان اسکودتو میشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.4K · <a href="https://t.me/persiana_Soccer/29255" target="_blank">📅 18:59 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29254">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/69cf7a72c6.mp4?token=vp-7cCvI704ETp933MbNIEVe9M5QfTfym8q0O5Bypk2QENtIvPuAgopma-R-rEAvMUX-6W3n-v_-g-oxUEpegWYlKyQ1y-tiUmZFxvUVmWR71oUljhe6n02pvq2m4jzT4zBb5Zr8wu2SUOvwVl_sQG82xkIdLa7kMMFlbzNNEuFSzc6ZCRLhdffqTZrOsEKS_MB4cdzuCxVcK6ORC5B-bCkIl-wejyJ-_JjZYALHBXWxtpTUc8nMK7rSvPmzPbQ2VDw94GzRn6WEeU5-hr3MRB1g8AZgT5QjKc4z-6M3g-PNcvQYQ5kUBTnyMhLrmZ0XnGqgAwnFSkrcycp1RKJFKQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/69cf7a72c6.mp4?token=vp-7cCvI704ETp933MbNIEVe9M5QfTfym8q0O5Bypk2QENtIvPuAgopma-R-rEAvMUX-6W3n-v_-g-oxUEpegWYlKyQ1y-tiUmZFxvUVmWR71oUljhe6n02pvq2m4jzT4zBb5Zr8wu2SUOvwVl_sQG82xkIdLa7kMMFlbzNNEuFSzc6ZCRLhdffqTZrOsEKS_MB4cdzuCxVcK6ORC5B-bCkIl-wejyJ-_JjZYALHBXWxtpTUc8nMK7rSvPmzPbQ2VDw94GzRn6WEeU5-hr3MRB1g8AZgT5QjKc4z-6M3g-PNcvQYQ5kUBTnyMhLrmZ0XnGqgAwnFSkrcycp1RKJFKQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
عملکردبرگ‌ریزون ادواردو کاماوینگا در فصل اول حضورش دررئال‌مادرید؛ سال‌گذشته و در بازی امسال عملکرد فاجعه‌ای داشته این ویدیو رو ببینید باورتون نمیشه کاماوینگا تو الکلاسیکو اینجوری بازی کرده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.5K · <a href="https://t.me/persiana_Soccer/29254" target="_blank">📅 18:56 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29253">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c9e3cf516a.mp4?token=Ana-AAM4-xw3KJcJLzxCHebmMD1BpDcuyV9nRtoqXi07lDpbx5GNm_jnR7FfJv1-bOwhSu3iTXypl-V_hAo-t72VOPkRiaP6Wwz8yIlz_ImwyN66WVZrdRfW-LFCUD5_HgtMxQd0oxj5HU87uSMcimyx7Na5Yum2I_co92JXe-RESc1NRIMAsbd7880aTmH1pT0dLEOuDhTkpcj83qFTrHOCD1ubG6z4EVEx7j5F9Ikp_f840GlmcQVqHO84C-TYl6uZEMQ4IIVcjpzs7JhrFfZQvqSBlDQUt5qRwzU0J0zeI-vS7SPB_p-tUvhKtZJoMd9CW8BTNKN2NQx8SflHqEZesSopHVQSPrPOorg1f45PoqVKXbfaeoQefDaUg9JoBDQhtQePf9us17madQP4U5mIe83LZo_5EzvzbcDvha9AQDnbvPkxH4YKgU2nF0sW1ouIbs3ncaBiQhp-_9qYeP9upiUPIT2zZrh9_IwtGFKOmZE_gCY_HEGRSOvqCg8r4RCmET5slrLdyrqJ6CaqsZCc_9QzRDkePewI7Aupcg0KAXFSlGaJ-qpp09_y6_GB6K4PiysqEdrTQ6ptiw4h3m0N0bs4m_Y_7V8Cq1uc11AD_7V4Eisp8RTlXMSxY7lTvTziuWXN--el8jgy5yLq6uDdV8WBDCNS2XJtApbgu3U" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c9e3cf516a.mp4?token=Ana-AAM4-xw3KJcJLzxCHebmMD1BpDcuyV9nRtoqXi07lDpbx5GNm_jnR7FfJv1-bOwhSu3iTXypl-V_hAo-t72VOPkRiaP6Wwz8yIlz_ImwyN66WVZrdRfW-LFCUD5_HgtMxQd0oxj5HU87uSMcimyx7Na5Yum2I_co92JXe-RESc1NRIMAsbd7880aTmH1pT0dLEOuDhTkpcj83qFTrHOCD1ubG6z4EVEx7j5F9Ikp_f840GlmcQVqHO84C-TYl6uZEMQ4IIVcjpzs7JhrFfZQvqSBlDQUt5qRwzU0J0zeI-vS7SPB_p-tUvhKtZJoMd9CW8BTNKN2NQx8SflHqEZesSopHVQSPrPOorg1f45PoqVKXbfaeoQefDaUg9JoBDQhtQePf9us17madQP4U5mIe83LZo_5EzvzbcDvha9AQDnbvPkxH4YKgU2nF0sW1ouIbs3ncaBiQhp-_9qYeP9upiUPIT2zZrh9_IwtGFKOmZE_gCY_HEGRSOvqCg8r4RCmET5slrLdyrqJ6CaqsZCc_9QzRDkePewI7Aupcg0KAXFSlGaJ-qpp09_y6_GB6K4PiysqEdrTQ6ptiw4h3m0N0bs4m_Y_7V8Cq1uc11AD_7V4Eisp8RTlXMSxY7lTvTziuWXN--el8jgy5yLq6uDdV8WBDCNS2XJtApbgu3U" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
👤
ویدیویی‌از آنالیزعملکردخط‌دفاعی تیم جواد نکونام که در این فصل با وجود گلر 33 ساله و دو مدافع میانی 33 و 37 ساله گلی دریافت نکرده.
⚪️
Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.6K · <a href="https://t.me/persiana_Soccer/29253" target="_blank">📅 18:56 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29252">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromBetegram</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/J8S88B8frreMUYoU-qg0avxDkxITMjySPnisK8nIkG7WjYF4JsN4C_I4zomA7kfFJyZyZoQHJ3Ik8qO9n_ZKTtLmRNy-mv8TVAXKUM6xoD6rhGuIZy5ETm3qQ5Ei_pjv6adNlzjgmrMg8QiPtB81_qsBbmvZLjFVjYSIXZBfNKgOigPHpC2TRRJLzF9MlFTMLci7SXuxd2g-e_-Sf6nTaJckNoXs9MvSlv8HcD3ZZ8PvE_JbpcPi6CMg3nWgYnAiJeiGKR5BMJah2Fv0i7fXuB8pppUDOIwzwH-pSDrF8G_B4c_X0qfhX5D1pFbioFe-cSwalqc2FigbHjMHdXiUZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇹
هفته سوم سری آ ایتالیا
🇮🇹
اودینزه
🆚
لاتزیو
🇮🇹
⏰
ساعت ۲۲:۱۵
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
<div class="tg-footer">👁️ 40.1K · <a href="https://t.me/persiana_Soccer/29252" target="_blank">📅 18:56 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29251">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Z2v9BT1Gakdbg9XKq_6rdz00C4urCH1bVbmRlwzDdW7NkGj7RyJFudwEzJ0GOkJQpUQ7TuRUOYlixWOj5FlibdFdU49i-fXGsiyb93lw7b5TsKDSVJ_Le_rZV36ci1zPfwIfnX35mGOe-iB0sPoVcO5gddDrURHnCP8rvRXgrhCFtTs-eedaUx5BYo9O5XzDBs6PoiZlLRpBd4Xoa7yJx6bT5maR7psJrTYO-haAA4fugojsqZb_yoLN8--MyKoQBI5nf6EZ48VaSpLLum92ht-tzXnr2vAKfXF_RdjB7KvRU9pJpl4SrjvOqEhj8erAR6mixZm-tRaAxhxqmyvzfg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
محمدحسین‌صادقی وینگر21ساله پرسپولیس که در پنج‌هفته‌ابتدایی لیگ از لیست سرخپوشان خط خورده بود درتمرینات‌این‌تیم با انگیزه ظاهر شده و از کادر فنی سرخ‌ها خواسته که به او یک فرصت بدهند و در بازی پس فردا با ذوب‌آهن به او بازی بدهند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.4K · <a href="https://t.me/persiana_Soccer/29251" target="_blank">📅 18:14 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29250">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/i2t-v0NaqIf3SKTyCPQtvqeuMoK9opEhPu3czwfLotdjk970GJ-M-EcL-RKk8dtrPnO_S2qkIwtaLT80coIC9V7GiEDlYUbBqRiy5pmdX7lG_GcEVGlHq2-wXsnE5as_CgzOTkiILvXDaRwjit7d0n7uyheShPjCAr0mx46B5B6SiKc_2IH2MI4mvFiXMMdvxnNWCp1lvPco_3tqk02XtC4QoQMgnQr1ULbKxP2giIjJih6VwI1L76etvbWH7ISiNvQjPWSyoLeejBIaMdYO7mbAEkgO0d_tyy_q6m8ryYTdOqk8iH7Scoalf1J3GUKGRsvT08H43_QcHzP3IfjRCg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
#تکمیلی؛ شماتیک‌ترکیب احتمالی پرسپولیس برای دیدار فردا مقابل تیم ذوب آهن اصفهان در هفته ششم؛ به احتمال بسیار زیاد ترکیت تیم تارتار همینه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.1K · <a href="https://t.me/persiana_Soccer/29250" target="_blank">📅 18:02 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29249">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AouSs_yRPFP9cZOBHf1fc1wU2rnGX1FCLiqfl6OX3R8yq3VE2pHGDOSmh1Q5b15pRJXm-91ekXNofaaBJQ-OCVXGwJySJhv3iidFi7wXmsGGncjq-YBkHgnMLANsyoGm8obWB__5micht3FCztOuHlF5qynF440gcuG8ImKcVl939e3sFt3J5bs-AAQOEk6otqHu15UYAHuN1tmO6exu78EmfkiCeMhRap_ND9k4DMOdUysnbL8d9rpOev82LFVH9YyKu4acsqYi-Tynoh1qZ9FSTvz28QlI6D047B6jl-ot5i8AnP7vl4LDMipFQe42eGskUaIo6W4nPPdevscewg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
#تکمیلی؛ شماتیک‌ترکیب احتمالی پرسپولیس برای دیدار فردا مقابل تیم ذوب آهن اصفهان در هفته ششم؛ به احتمال بسیار زیاد ترکیت تیم تارتار همینه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.2K · <a href="https://t.me/persiana_Soccer/29249" target="_blank">📅 17:58 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29248">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JuGkYHl8dJh_-oM3xOvIuvIvvjnb6NOfV24cbk7fBkOz_gRWYC4KQp3JEHnph3Bh2aGVtjtc8kP_i_owAzqKZFJJBoPk-ENaMPW_qLku8T3UZDCJsVUUj21BlWuXVsc3ON3IkYh6mCgbAl_9DhFjBMU-G8VpCKIvETjrzkH-xGbytFrdED0KAPB_bNblpQWpS6wYSamMNhjVfthcR-j1VQZbodP_Ruvkbtlam8rhvKvpSgYgVJVzzS9A8kCNOm7HdKiHQ_YQLTmI_BiLMrOr7_TBVaonZgoTgvn0sRv4TUVzRLnbIvidncHsu18mJzxRJIwt1Ia3m33doKPw0u-Zuw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
👤
ادعای‌نشریه‌کوپه: براساس برخی مطالعات و نظرسنجی‌ها، هوادارای بارسا تماشای بازی تیم هانسی فلیک روبه‌رابطه‌جنسی در زندگیشون ترجیح می‌هند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46K · <a href="https://t.me/persiana_Soccer/29248" target="_blank">📅 17:49 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29247">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/db6979e1d0.mp4?token=SAGRZhoYdm2jA3vDcHcXveRDEakPwl3hbylIbCrcknJ7z8LKEWEKqBImtz_1HH1mtSNvU653LZ9yZGgjTFjnDWVPjQZEB07iPrLMdN1XmJkyRBYtHoTUUjAf5gBHpKsGwfVNA6Wzu0pgCoaZ7x81Tj1OqSRP2qpydmq7kB4YTIqnhqIILC1v_X6IKNi8C9NoKrLWXAlqdTZSEmC9oQYsh2q3SPwdZlyq5adwFaM9QxqZKfXTh3Fgt29MLkgc2EbXrVkvI0YkMJlQRnedPiJ5NnEkxVVQAzAohE5xcqxmql2jadvsJdE4dMgnLOpHuHeWNiK0_JsbaDq-jAS-_W43SA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/db6979e1d0.mp4?token=SAGRZhoYdm2jA3vDcHcXveRDEakPwl3hbylIbCrcknJ7z8LKEWEKqBImtz_1HH1mtSNvU653LZ9yZGgjTFjnDWVPjQZEB07iPrLMdN1XmJkyRBYtHoTUUjAf5gBHpKsGwfVNA6Wzu0pgCoaZ7x81Tj1OqSRP2qpydmq7kB4YTIqnhqIILC1v_X6IKNi8C9NoKrLWXAlqdTZSEmC9oQYsh2q3SPwdZlyq5adwFaM9QxqZKfXTh3Fgt29MLkgc2EbXrVkvI0YkMJlQRnedPiJ5NnEkxVVQAzAohE5xcqxmql2jadvsJdE4dMgnLOpHuHeWNiK0_JsbaDq-jAS-_W43SA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇸
👤
پاسخ‌کوبنده مورینیو سرمربی رئال به سوال خبرنگاری که‌پرسیده‌بود درآستانه‌دیدار با اینترمیلان با کیوو سرمربی افعی‌ها تلفنی حرف زده ای یا نه؟!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.5K · <a href="https://t.me/persiana_Soccer/29247" target="_blank">📅 17:26 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29246">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UFRGl1kwvy8kspW149UpwFGpJDEnerF6nT-eKgDrL2BgCwE8ltgKlEliOMCEZrA9uExDuxSpANVJia6APf7wDfizgwZEEdwZagqU9H6n__G30V3zchDJz3LyMib3XRozdms4ASHEAwiePBiaWJyKiX-RkF9KHqFbKZU1BCc-SN0LCY_sHnmz5uR5hLcyzPMxL_7sEBG-bvPWgv3GNiHFuZn1Ma28Jojk9E5yrgCmL9SRyoW0PfIKFcoZwEBclG8BKPccpZsKNhjSaIx_29r4teYgwYpXvXJCtqLyL2ZupFm4p-2hSOigf8l3oZEMLu2yQZA6F-XEM_NpCCJ-LMjrTw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
کیکه‌سانچزفلورس سرمربی کهنه‌کار تیم آلاوز به عنوان برترین سرمربی‌ماه‌لالیگاانتخاب‌شد. سانچز در دو سال گذشته بارهابااستقلال مذاکره کرد اما بر سر مفادقراردادبه‌توافق‌نهایی نرسید حالا با درخشش در آلاوز بالاتر ازفلیک و مورینیوشدبهترین‌سرمربی ماه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.2K · <a href="https://t.me/persiana_Soccer/29246" target="_blank">📅 16:55 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29245">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/08ef1daff4.mp4?token=InzmYvz36QuGfdJBm746z76hULChSd48b2DmEL532O6m0oybl_ZdG45cX4nEi2oX9WtvJW-J5EWLkVBKDL6w3d43lNk8wAkuu2DqDOE-877nxSgAQVZ6fQYGi5fBumpm-FSjQTXQxCh76Fv_mLsezQkfut8nuqwQNV9lvf8EBLbzIRWedbePnSfQ-8A-IVyty09yKqfNOO0UW8PfBAu_Q2r2FINlzP3D3nUCIDaKw7wpMIvVBcO6mktfWfSzFw7J_KpvDq6U-gvXYkqWwBGEmRgVQ6PInTQHY9ko83Ywaw7C5kVjBxd8Hp9SANrey5wGXiwZOvQyMkGBpsCm-eLy0Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/08ef1daff4.mp4?token=InzmYvz36QuGfdJBm746z76hULChSd48b2DmEL532O6m0oybl_ZdG45cX4nEi2oX9WtvJW-J5EWLkVBKDL6w3d43lNk8wAkuu2DqDOE-877nxSgAQVZ6fQYGi5fBumpm-FSjQTXQxCh76Fv_mLsezQkfut8nuqwQNV9lvf8EBLbzIRWedbePnSfQ-8A-IVyty09yKqfNOO0UW8PfBAu_Q2r2FINlzP3D3nUCIDaKw7wpMIvVBcO6mktfWfSzFw7J_KpvDq6U-gvXYkqWwBGEmRgVQ6PInTQHY9ko83Ywaw7C5kVjBxd8Hp9SANrey5wGXiwZOvQyMkGBpsCm-eLy0Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇸
🇫🇷
امباپه در پاسخ به اینکه آیا باید در کار های دفاعی و پرس بهتر عمل کنه یا نه و مقایسه اش با عملکرد عثمان دمبله و رافینیا در PSG و بارسلونا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.8K · <a href="https://t.me/persiana_Soccer/29245" target="_blank">📅 16:37 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29244">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dqcSUNvtObRTnT1oxXVO4JUvlufU27l4bGoRWpdQ19wQ1Y04n_Un14F6Vuv8Zbj2LXI-4INDZABKbuEPt3V6IsL5TW5CVxLOOOURfOSATN-obkn00gGfq_ttnTPttBEdGDNYRGmti9ooOrd38YgoDHR2GG-P1Q-rQLlnsgts9NRncir8_OUNpD2ivIFGQkMTuEQiQs_NLRUruTwO4asIWSlsfm6WhXDvKiNv90VN9g766p1WG67vj6dABlldhdLb6-kUXXJCb52936fiQL0rQS-XKeKPWrNRPp4SrshkhL0V6mobdLeaatXV9UwA_MiFdDeE5hsTaSouxk8wCx3uTw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
عملکرد خیره کننده خط حمله بارسلونا در فصل جدید لالیگا؛ به‌ثمر رساندن 17 گل در چهار مسابقه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49K · <a href="https://t.me/persiana_Soccer/29244" target="_blank">📅 16:21 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29243">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tJ7Ev_rpKs7Ai6e9cy2mcz12pKA-vmFpsS1AnvMZe2OJyBcxUcqSzvVWrR47CvcWSeZkq48Ln1orej8LY6Gf_5jNMwgfhgNn06vfk96__S_Oht3GtGpFD-rIe--DjytoUx2urx8v98-SjMW8dQVJCAd6c6Co3TL88ceo01jiAlGl67sf92aVeKLeU8TxpnRvZ6zmo_ZSWKKJjieGPEeYoRbVyAI4opc2Fpbec57KnaESU4xS25iCOVA78syexCQ9yT_tyNOnNBj4MeIEsX7g6gQfvaw7dA0DexpJATG77mqDfHfR4VVE6hRi7uX06aIN6YwdSqG-Iv0Mqtr0pQniZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
آمار تقابل‌های مهدی تارتار
🆚
عبدالله ویسی به مناسبت بازی امشب‌دوتیم پرسپولیس
🆚
ذوب‌آهن.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.5K · <a href="https://t.me/persiana_Soccer/29243" target="_blank">📅 16:10 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29242">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pMwLTk8le80D1mXLDHkW_LQw_CPVIRAM3ckmC4PdJ8Avaxx6fkBP2tCQ4gSGa_VJB_I-d1Z4dEYLBUmOTPb30EGDVkGURcVv2gGALbsgTXBthgLxYcrzkbbssgbWk3EbjiMbc9CrZIUw_TExMa7oBlcDJQNQzxeFk2SR8ZaScXIg23NHWMj5ndr_ciuinm5B8CsNnR0MbeDSmiFgQ7-k_7S4II-gc1fuCWLdSuPkJ0ezkhkzfIoha4eyMkCAYV4BAx9cD9DFviJpEK5p6aZiLWo2CS_XrsET2kk2OBGHMRgdTlkTd3gMw1NeFMbSHvBBwEscnf4EPNgQxui57SCyow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
میزان هزینه لیگ‌های معتبر اروپا تو فصل نقل و انتقالات؛ لیگ‌جزیره بااختلاف بیشترین هزینه کرده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48K · <a href="https://t.me/persiana_Soccer/29242" target="_blank">📅 15:14 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29241">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3910e6991d.mp4?token=psCkIW7zgUn3FAfTi143eef1yijUnRHlvmcIMW6zuHOZGCyHJCP7UmXXyGpzvMxNEtYT3gFQiktc3n5nLuPBAZeG-vKurx1tpOFXLofdVmvTKJd5jsg-h7-Fwy8WesIwFAY6pSvnSNbGQbt-u-5dBWUBgMHDZ8ryNZfKNuUjU29ElHZjGqqTXYRJpcgqr-D5IJpffptFW_UnQ4wJhsAcsZ_rCD51ujfLV0gMvD7ldNE2Dk1erz-wGNUtIWeZIOquQOeXUAZY2qsj9gMAZvpVEzoQaKERFmlG254vEnCKYy6WgktlARVuqUDb4AfOFe_74c4KTnMZWCIzSHSn86p2Lw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3910e6991d.mp4?token=psCkIW7zgUn3FAfTi143eef1yijUnRHlvmcIMW6zuHOZGCyHJCP7UmXXyGpzvMxNEtYT3gFQiktc3n5nLuPBAZeG-vKurx1tpOFXLofdVmvTKJd5jsg-h7-Fwy8WesIwFAY6pSvnSNbGQbt-u-5dBWUBgMHDZ8ryNZfKNuUjU29ElHZjGqqTXYRJpcgqr-D5IJpffptFW_UnQ4wJhsAcsZ_rCD51ujfLV0gMvD7ldNE2Dk1erz-wGNUtIWeZIOquQOeXUAZY2qsj9gMAZvpVEzoQaKERFmlG254vEnCKYy6WgktlARVuqUDb4AfOFe_74c4KTnMZWCIzSHSn86p2Lw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
جورجینا رودریگز همسر کریس رونالدو قبل و بعد از آشنایی با فوق ستاره تاریخ فوتبال.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.3K · <a href="https://t.me/persiana_Soccer/29241" target="_blank">📅 15:00 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29239">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jNA0hKm98XOjkEPmL2yezeWD7KfEwjPsSKMDyITYACfzdVmUGJNrReIfTW38j31wuYCQO-WnnhwqtwbEWKO6pauebQwEQGL3DY-8Mb8xpeIV9-jvqNFUKeWuIEI2unVBeGg1ZbV9AbGE2beL41mi8ntvsrJJsrKF0BenUlarQBqg89f-lmExvl6ZhhjIBa3IZIo8C4cB0CaNi_4ecK9DSWwCPVetdrmawc1SRfzH0MWer41qAnHszOVIxSM0YMq6xdq2zvHH-J3vZxvJmx_FmuEf9Uis7d5PiH5LEUhZwGnnzNPwyWa-RLnS8jGUKOhYRUvsOgzTQljJTCcBSvQBiA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/KbZ9Vc0R2sDwoMZMTpbYrlR6jtDF9vwbQm8n6H2xepZf2kM68Ju-fnPm8twBR3CGrpF8bKs_Lspg9rvuhfFxJQoDn0cdvXhvLIPl9YCH5c92Goo8o6KjaiKVVZTG5hZyuNktVk1dCuwaHmZ3yUHXn6NdY21j4g51-bgXhDZMYh_qQ7wSUlpVQhx81L1PUi3PndjUMViBoAnx1B-_827cyyCn2GOCNN3wr1ggF98cLSG7ltouDyX6tc13yEGi7VIs8N89RQoHoikyOkjAIEDzXLLqfp5WrGwywikZ-yRWPcwIoIKaWNUTnAu5-8KYPiNBNECqBr5fL26d5MT-h3-FAA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇮🇹
هواداران سه باشگاه اینترمیلان، آث میلان و یوونتوس که مدعیان اصلی قهرمانی اسکودتوند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.9K · <a href="https://t.me/persiana_Soccer/29239" target="_blank">📅 14:37 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29238">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UEpL_iXzGbSbghExOkKK80cQ279raCF_bVuqzE2tmUqF-HjDf05eZh727vYiZ6nNbidk8KmXGFderbDC8oBpMDfqDJzOFLbhbJG9bTfR_lLZ59sGh5GOcwRm1NTEuE8S0q-dK76FTapmKo1Pkl1aAEngi4F8_2EcM9X5nz0BnOWQ5xapcXM7LT7rEdBZMdTQiHFhmEIEsIiSot3qFx_7w-Iene45DVrmgxGmKcsgo2mWHh0mA1lJsKt4DKMxx93dPH5DwnUqc4ocktrOqrnn7eli8qaewuMFxy2Yn3lgpcHsSQJTH0tOguiFJ4IuT9b18GCwypjiEPqh9J1bNSBaIw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
نشریهTYC اسپورت خبرگزاری معتبر آرژانتین: لیونل مسی و رونالدو به‌مسابقه خداحافظی کارلوس توز دعوت‌شدند و ممکنه باهم‌همتیمی بشن! فکر کنم این‌آرزوی تمام هوادارای فوتبال جهانه که یک بار هم شده دوتا گوت تاریخ فوتبال رو تو یه تیم ببینیم.
⚪️
Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.8K · <a href="https://t.me/persiana_Soccer/29238" target="_blank">📅 14:30 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29237">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YPXJ6FJ_Pwc1lKvw5RU2RyRcXwWNdsmiVeGppgYINP_EkfsKwkiO8mXMj6e613PyXWUTSBUDGFHF9GqTUFvhGqugT3sp9RFW9ARsGtrccPdM7ALHyZLBXYRa8eql9jU82lJ6bDI5XJE-Zf_L7QaxAEFR_mFWsUFaVd5Vh5IB7epzWQVwNseStSldyD-gRH3f6J2kmxtldHIS5ov2mxY195KXg8eBV23JgO_W8cKkZwNO5RVcZNDKG2tY3Eu0Wsj1Qi9HQscCf8A-knbRnOJrSy9Iq6lpAnKP9S6cVuyRs7i6ZYf-hEYUpe7BMEKxPB2D8Uqqzd5npEnQ1ptHhVYIXQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#نقل‌وانتقالات
؛حکیم‌زیاش ستاره‌مراکشی سابق تیم‌چلسی با عقدقراردادی دو ساله به بوتافوگو برزیل پیوست. دستمزد سالانه زیاش 700 هزار دلار خواهد بود. سال‌گذشته‌ایجنت یاسرآسانی‌تلاش‌ خیلی زیادی کرد او رو به لیگ ایران بیاره ولی شرایط مهیا نشد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.6K · <a href="https://t.me/persiana_Soccer/29237" target="_blank">📅 14:13 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29236">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VOZiKJnovxWfeqhV8WMUPUW3y6hvF4ov5_fpX-vBsoqkcJe1d95w9AbLTmJLCg5c3sLoByAIvBXzYW7z7RO6VGXk3_-Rc8DiPcmdmTVfri-cV4k1CdRLkwtbJkM1wRU-WEkTDrn6CqqpE5OfHZnT_ikbS6igwIwdlohmD4H1awm28HgFHpw7DiHpwBuZB5P9OZebB-3oywxH2fCHhdWCBzOFmfVrQsPXWNUQE7NmXojblxvYBaOOBubXV-nPn9ekJ8J8ZtDdzgpOcA87KVn3JTtw_RwTS3NxICdr45GxKOUVGP0ihLuRGi0kta0FH5qqhT2elZBG1ENrp6pk76NNZg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟣
بهترین‌ترکیب‌تاریخ‌لیگ‌جزیره از نگاه نشریه سان باحضور کریستیانو رونالدو فوق ستاره پرتغالی دنیا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.4K · <a href="https://t.me/persiana_Soccer/29236" target="_blank">📅 13:54 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29235">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jX1bmDak7KBbDC-pWi7072iOwHXYlDHRU3IwmhaWweC26s7c25cZgjva-rEIRw2puIRyi9Oa5jXVrD2a14wGkefq0h91HAsDbxquSZLIDq9j9O1y4SmMkbNIr1AJ0h6ON7tn0W08jDrR-1xnPZWbJzj0FNoxlYLUOQXRyQzyq_KTSadjMoI1gyooCsjyNhplzGRGnA652sLoKfncbVsC8IGnCSIAoXyTLxzYnvrNSvC-cbdJj24AZ48dw2ZQfeo24iAU1-P4hRYVWkVLYm4j6akCuZPb8OaN9dvx0ZCTPsX9oGgZTeDKi6sumQZ6bdw33PUGtjzDRSkqDGBd8TiytQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
مهدی‌‌مهدوی‌مدافع‌‌راست‌20ساله‌آلومینیوم یکی‌از بازیکنانیه که قطعا در نیم فصل راهی یکی از سه تیم سپاهان، پرسپولیس، استقلال میشود. مهدوی چه در فصل گذشته چه این فصل عملکرد درخشانی داشته.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.1K · <a href="https://t.me/persiana_Soccer/29235" target="_blank">📅 13:24 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29234">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Zg1TfS2_X37UlrwQoOyEXG5Lz6t0Mo2u-kIDPztvgxoyX3i2cs5Vf9svM-AFpCUPr0-iPjRNuNo5yzxtCTzH3c5oY2eA8SIanAauV35be0f8A-Snv5U_BUttMieecC5s2dC4DoD9Fm0Jwze-l6p5YzGtT6V2H10vTxpQf1VMIpQYiOOFw6XTL2sLV6oU3XBDbHYxpvIYVBzuM63yuLHArgmsyffTzEThhRlnX1ZPqnDeN80JStXMCSF1sXlU55U5U3bzV3lqIR5PZpxiV_ZkOUiV00MCiHZELfs5cQrs4DwbiRQ2eU2ZfSosN2mkKU_Ak42J_dNkylpwuUBtFX1jDA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
آمار تقابل‌های مهدی تارتار
🆚
عبدالله ویسی به مناسبت بازی امشب‌دوتیم پرسپولیس
🆚
ذوب‌آهن.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49K · <a href="https://t.me/persiana_Soccer/29234" target="_blank">📅 13:08 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29233">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/536549697c.mp4?token=shKyeXOB8NK3kqQ814UoJ6M8chAzp7MCr9it7nbVVP9-9-Zi5efLF2s8Z2aNVQZXWELnI1mtzfHfkc5CNS5ZqIqdrhYxNzpGI5qKxo9TEsyWmIiVQO9I7K9m2lvFqdKRG-OOS3gQC7UHcvXC446_Xt-k7hS4OawR1Q-0MwegBDYBsiGXtYjux7A1-wBfnldvinmEDsObMNqxvVxq-DSipSKhStIjSf6pILihvtZtcETOoXo95Fn3TmW88NX79kV7M_HZvkQ1CnSRrBq52UDxz8ZReXqee5SIF7SXRaAKcwvQrXYNxgWfzGQhtXWXl_uFTO3ZGnGjCv0GLc3J0kfMTKQAEesqIrI-QSv93cNyh-pFn8sLYbkhJ8T9c-HmjihNWCQK5tzT8gb5oKmBe5BQPu8bAL0H3u1K75RWvkFF_ynw6pv9IDxm3rgMkTBEjl_pOHKWEmLwXwEKBzOxuEGisXwyx7QdlrPeBWJ7OA1CPuGoKswn4hM-TrbgmxDCAFQEe42_VfyL36Q-1-3UMZqrA8rbbG6YDODzyYLGKVaoJSqvSxI9iZbOLFhwaW2uKM0PeMmLJGvSFozkiBpAvfoC0lcw4jcStsfF7ISnbtCqL4TVh7fSzfN4v6__SoFFzPyt9zpunCUf-gUfFXHO8LtuKbv4Gw8mUArIgjU52YRq0Vg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/536549697c.mp4?token=shKyeXOB8NK3kqQ814UoJ6M8chAzp7MCr9it7nbVVP9-9-Zi5efLF2s8Z2aNVQZXWELnI1mtzfHfkc5CNS5ZqIqdrhYxNzpGI5qKxo9TEsyWmIiVQO9I7K9m2lvFqdKRG-OOS3gQC7UHcvXC446_Xt-k7hS4OawR1Q-0MwegBDYBsiGXtYjux7A1-wBfnldvinmEDsObMNqxvVxq-DSipSKhStIjSf6pILihvtZtcETOoXo95Fn3TmW88NX79kV7M_HZvkQ1CnSRrBq52UDxz8ZReXqee5SIF7SXRaAKcwvQrXYNxgWfzGQhtXWXl_uFTO3ZGnGjCv0GLc3J0kfMTKQAEesqIrI-QSv93cNyh-pFn8sLYbkhJ8T9c-HmjihNWCQK5tzT8gb5oKmBe5BQPu8bAL0H3u1K75RWvkFF_ynw6pv9IDxm3rgMkTBEjl_pOHKWEmLwXwEKBzOxuEGisXwyx7QdlrPeBWJ7OA1CPuGoKswn4hM-TrbgmxDCAFQEe42_VfyL36Q-1-3UMZqrA8rbbG6YDODzyYLGKVaoJSqvSxI9iZbOLFhwaW2uKM0PeMmLJGvSFozkiBpAvfoC0lcw4jcStsfF7ISnbtCqL4TVh7fSzfN4v6__SoFFzPyt9zpunCUf-gUfFXHO8LtuKbv4Gw8mUArIgjU52YRq0Vg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇸
🇪🇸
هایلایتی از عملکرد درخشان و خیره کننده لامین یامال گراقیمت‌ترین بازیکن حال‌حاضر فوتبال جهان در تیم ملی اسپانیا و باشگاه بارسلونا.
⚪️
Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.9K · <a href="https://t.me/persiana_Soccer/29233" target="_blank">📅 13:08 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29232">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromBetegram</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/e15DdND2eGL7Lk_VkwazpS81x6dtWIFHwwTEwumyHMm_RAZAqf-Ah3lW5r0rIdqohZ0XL9QBTU2iizjCC1BuEpY1wm73vDnbcZynn3OmS1CphxdoiZ9EM9lZhe3cpWEsYTeh0q_oQhH2GF27V_LExiVr2l_nC3YKZ2kxnBZhR7JQAC_XJzskuz_UU4q02H7mM5BLi6XB-4C7ZKCoQOJXajwyCK1wUzhxP530v6355IJHnFToGmwggB5jO82VmTivmPWyUnWErUuFf83piMjZpNxzf_Ue_xhYjpCH6QQL1g29-tvD46tBx5YqZmyJCc-rcx1kY7U0NBEFDLTr6PwrcA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇺
هفته ششم لیگ برتر ایران
🔴
پرسپولیس
🆚
ذوب آهن
🟢
⏰
ساعت ۱۹:۰۰
🔴
انواع آپشن پیش‌بینی برای این بازی در‌‌ بتگرام
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
<div class="tg-footer">👁️ 41.9K · <a href="https://t.me/persiana_Soccer/29232" target="_blank">📅 13:08 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29230">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/T3RTz5WxX5zol0P34WZ-pH2QtrUVyZfv0XQIT9HH1CUh9nrQjSdvl1oCS_KAE4pmy3lp_BnAh2c2gdFaYp9VF7pwV3goA9dzofKMS4ZmxqGl1VTzO0S_IsCZ0iOyVXNxvK_I7YwixvpQfXS6rxKhy8yqrCXUjWBeSd5o_SpRLgDVbVZ125QjGW-KCYz5qwE7Kjnl0KcjoL5wS2dzGn7WrAbitLELC4B9AQlyM3T1v-YzIJqx5PUMR3t6OGFk1f5Fx2DB5lIMqUB1HQDkNCk_OcWGf3Kto_eVhXlBuWxl9Ka_Dg93boXmlAZHKPpOwkn7BCgPfIrp4aoehUpXdimcRA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/gSxpTk3c-tXQ5GkeE4nswxIYNXrD8-wjzV0ny67pnUgyVINWsmaPJn-L8IpJEvdbcHxYPaupdLzRp7BKtIl8ouMJDVxN6zax6CqNy-WuaKVll_pqVTVi1rkARqgr-tdvh-bpehSS8OehEAZTmqemYcYkPi6zJbYa7yy1wliwZwRxwh4wV3I0AnpTsvje9gpAUXnowbDph7dNseZ9ikSIXK8MXULy6J626nSkDyGawViwz2H3iPA6LLcIPEXguv3Tz1755WMOvI7JF9y69QDQqVMuC_nGaI1trvz3NtmRNXzsmgTOEZjV3UTKxIby11MpqXd0ojAsAiPWFLvCh_5dzA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇪🇸
هایلایتی از عملکرد درخشان رودری ستاره جدید بارسا دربازی‌روزگذشته این تیم مقابل والنسیا؛ وسط زمین با حضور رودری و پدری بسته شده برای رقبا!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.5K · <a href="https://t.me/persiana_Soccer/29230" target="_blank">📅 12:44 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29229">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LysngS0pVBxwzDapt0kkJNnpFtJqF7wk8KWpvTT4rzUvEut8FNRcMX78dY_8VbymclS1vWoGoFL7FtXyKV5hbYTqVvfUVnXzSR7kvMHPYpVwqznCdyGT1dTg3pTLvn8UNwTEhGt4WB4kBt_Wjr48dyhUCSbbnCRBX2ONXHqP5gOGO7ED759tirpeD8J7iUc5bCvSLGPkb45veMHgfj8Y41BUip1I_yibXLXdjsAu1xzwNKniuzOnuc3py4LwvT21l8wF0RnspeGy1NNpbBEvTAW3dkGJsnh_VRgARe8T4qvLSMqM8E51h6NlAXQVmhm37qPDxRuDIHkRuQTlifQ94Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
#تکمیلی؛ برخلاف صحبت‌های امشب پیروز قربانی سرمربی تیم آلومینیوم؛ باشگاه استقلال مبلغ رضایت نامه محمد خلیفه و بهرام گودرزی دو بازیکن جوان‌آلومینیوم روبه‌حساب این باشگاه واریز کرده و بااین‌دوبازیکن قرارداد پنج ساله امضا کرده‌اند و نیم فصل به جمع آبی پوشان…</div>
<div class="tg-footer">👁️ 50.4K · <a href="https://t.me/persiana_Soccer/29229" target="_blank">📅 12:22 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29228">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LN7HTglgwp1zqS0Mrb7VFbyEtF3n6jpEP5QN1MrJN7HaKYsO6aK4_xvBbyCeOchPy0mcj-AJeUO0ZCJATvRKumMlMnOwYGeUuo02tbExSdHJBxAXD87KLvXn1t1wb2s29OUqq9qNlaR2s9fKnX2o-ksNZ4OwpzTDmiHNHyL7Br4ieMFTuQAD42tuUkP4-KSItF095ENi09GiYOa_kbH7iNqDm_G-45qLR2-xVv46aINDhhnttfIZqI_CHlvUB5py1-Y7kP6rMns0DovB_Mruc1urFS1q7OINt5k8wEHVZmHZpTAZp4q8yUbqU3R-RoshqJAuGT2n5T-IcYB5p_t_vw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟢
🔴
آخرین برد ذوب‌آهن‌مقابل‌پرسپولیس به هفته ۲۸ لیگ ۱۹ برمی‌گردد و این تیم در ۱۹ بازی قبلی خود با سرخپوشان تنها ۲ بار پیروز شده. از آخرین پیروزی عبدالله ویسی برابر پرسپولیس هم ۱۱ سال می‌گذرد و این سرمربی با ۱۱شکست‌مقابل‌پرسپولیس در لیگ برتر از هیچ تیمی به این…</div>
<div class="tg-footer">👁️ 50.7K · <a href="https://t.me/persiana_Soccer/29228" target="_blank">📅 12:03 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29226">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">🇪🇸
شماره‌لباس‌خریدهای جدید بارسا در فصل جدید مشخص شد: آنتونی گوردون شماره 17، کریم آدیمی شماره 14 و رودری هرناندر شماره 16؛ شماره 9 آبی اناری‌ها همچنان خالی نگه داشته شده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.6K · <a href="https://t.me/persiana_Soccer/29226" target="_blank">📅 11:46 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29225">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CNkHjwA_RQY3_3vRdsgNIMwQ2SJywpwoSzbKwUFkyKpFiobA2y1Vy6plnKo7I2ASA-AmrSZ4i_wFVFW-9dB3GxHWiN7xYqD-1lkI4Hv3WhHUOy4q5g9qGB52vGyB3Ue34SIsRTCxb9Z_0l5cUbK-5CBFPySSsxwOQWfXwdpIQM6HLB2jIeEoGtbnycxRbrfJkLRGlP-_lOZBX5PFpxDIshsoxWiJIrQBtJA6xy3jnzM3DYgsjjvCgk_cg0AvQ_3H1kwZM_fwJnYGq8dItcIHNoocOeempvB7a9aIxGvDtCaCF_mthFaKEnG5YsSn4iWW1fEVI_C_Bu5yTxxuux51tA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
خب‌رسمی‌شد؛ ازساعت 12 فرداشب به بعد بنزین لیتری 10 هزار تومان به مردم فروخته خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.5K · <a href="https://t.me/persiana_Soccer/29225" target="_blank">📅 11:29 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29224">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jsgA9cGdGgFAX6Kf_nakR8Rt4tvnNfQAeTijQDpql36zl-MJ8vL3bqCN_aZWONSla99KYriHyzYon-MZY1wC5bMyQDi7oUqjaCOVbO3falJuIh-H6VsuhlJbfHAAr9xVjY4DQrCNzeinRVRooWqvum3a_7lLWJhiy19w6KBzpq7tA_4kaarY6xr8slZaslc70RlkxmiLmdzh1yhTIpYHW8YeU3DHZqCQTsOZB5Oj40p_ExhCMV9BGzkR455-J2q6A4IC2cgEGGIen7K2TUN0rZJokc-CbB3XYCKPq4GTDSBjJHUUFnOyn9qCeYp4g4CnHZ53ESmPeFtu5XoF7qQEEw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
گرانقیمت‌ترین‌بازیکنان‌حال‌حاضر فوتبال جهان بر اساس جدیدترین‌آپدیت سایت ترانسفر مارکت. لامین یامال و ارلینگ هالند همچنان با ارزشمندترینند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.3K · <a href="https://t.me/persiana_Soccer/29224" target="_blank">📅 11:14 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29223">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/md7uE9EX-pXYOW6207Drs4vPAtKKFXCJWTczvTbBZcJMR2CvyoF6cDR2753EAQ7NFb_t9FKmqMFbVn1vaYFq3Af98VtSHEGpt2isUjmI2L8NNOYO6dILpQhWZjU-AbVOb-6uEliHIN3_r85MEC2SGeHTEa4XEuju3pxRfBAytp-u4NKjuZndZsLYggwMUsnZj8B5vgt6OVOmVf7aNAhGkyqmwvTRhlD6EZGZXBTDAQPJnepcUYQzF5TOnQaRV2owqk1tYWJ3SEq3x3Wh_utBAyCS9xke0anW86kKS_VTF_jnWhxuqhUqK9EvamcMn1h--F051-f4FzpgBJ-pJANxBw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
اردوی تیم‌ملی امید به دلیل کمبود بازیکن لغو شد و شهرآبادی، لطیفی‌فر و ایری سه بازیکن پرسپولیس، محبی بازیکن خیبر و صحرایی بازیکن گل گهر که تنها نفرات حاضر در اردو بودند به تیم‌های خود بازگشتند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.6K · <a href="https://t.me/persiana_Soccer/29223" target="_blank">📅 10:59 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29222">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vCjYtUW10Tdy-gMp6V5B_Xnm9yjba9Hx3zSg6VsUGm-8Jmd245XqpCoqtyYb5w26aBxG1Evygdg90gw_wxcw0Q5Y57e8GfqIzJe1m27Jx7-M1SzJtckmNQYrDx8ZjiUSmZAXehCWh8SeqQgpbB4LhuIfp50swxf8btmMd8C9unJW_VhYAgxjld8GVQkCe2fIBXqmFxzvpY2WBD283tq0wLxdjckKeXSq3Gpk081zL5R9otSYYGzQeoF9h9sRMT4dZeJwJJXGOP4AccKPmiKgBiZPsNoTmYFpMQJQGKrEM7adZiMmWlq45X4zQSMXcOcoTMMg7WCknQ7O6vLn0wvISA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
#تکمیلی؛ شماتیک‌ترکیب احتمالی پرسپولیس برای دیدار فردا مقابل تیم ذوب آهن اصفهان در هفته ششم؛ به احتمال بسیار زیاد ترکیت تیم تارتار همینه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.3K · <a href="https://t.me/persiana_Soccer/29222" target="_blank">📅 10:50 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29221">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qlXSQ3zgu0dS-Zh2-XTNQR2I-C1yOaz4cLzHxjgoWkJtpDBu0OCU_GyDDTd3ShBRE20QTVvSzSxUSv1Kb_baJXVV-g0EBRZPqfLSTqKYEdryYWHfp3veBW8Lt2B6MsZxqKGLo0uN7v4niCkjnt3DDSTb9xeJAmkOVYMtQ3hjoNT70BScnORM1JUbPt6fo9vtmQGPy_cwy_HipTcugvSwxSnieWr0PWpNYINoM5ST0XHeymG7HU2SLdrcKyrk9951UdSHMdjjkyxLUNXZ_h-RTxpLUmN3pyM8oG95zVC-dkGJCda0_v_7Qc0mh4cjorVf6k6c1Rn1wQOGbRkwhZYblg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟢
🔴
تاریخچه تقابل‌های دو تیم پرسپولیس و ذوب آهن به مناسبت بازی فردا: 77 مسابقه، 35 برد برای پرسپولیس، 16 برد ذوب آهن، 26 بازی مساوی!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.2K · <a href="https://t.me/persiana_Soccer/29221" target="_blank">📅 00:50 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29220">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/swSY8VE3Urt0_xNhwAc2oTna_V7vklMQ5K207XLNPvhwjaZBa5tV6ZnTEkdJ_jJYvdJGAsm-dnHf0gW3txoO10R4PB27EXWimzvrt1nRncfK-jau3qJ3TpT55IMYHyu-c113fHVOCZTcExiaqv5tCsCE2M9sNBUvkSloiHndDTtQT5WBNwPr9NN1Ulr0SB-XIpR77Jr4_tREWUZeQLWNxZU_wc4vEB_PD3GX9SMfYnboxMNeI-q44-6DAlu7b4qfVaiWWb0QlbGP7JsK3VZOtwYgTEIjbD_n4C-d3x-CdTGQ3SxOeoY9ucQPiBX0-KTFf_9D00xLvMSXSoYrEsjA3Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌‌‌‌دیدارها‌ی‌‌‌‌امروز
؛مصاف‌شاگردان‌مهدی تارتار با گاندوها برای باقی‌ماندن در کورس صدرنشینی!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.2K · <a href="https://t.me/persiana_Soccer/29220" target="_blank">📅 00:43 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29219">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IDD1LN-GX5fh9lPMILJpNchQq1PpLN2QSHVIaBluiozofDc4t5XmC36IKOfhY_TRmtGn1DMlmZcWjoqLPgv_6L8WzNWOg-0EX8JBprB9-U9TQ50jqEqtKjiH_ZynGFsKHgUU7Zb7JCAqllMLIe1EGntb50CUrP9ZTNbTVtpIm06nYShZ1mXGDhW9jwPJkK7RV_57jv17oj1FIpysdjK1K46sx7hg6GU1eZSJ8ST0hKVyN89nwBrYtgHzSUZHxHeGTkISvNXxF7BBHjTuh4S2LST6zT7CWnmugHU5Qc-KlcQ2TQqrwvYRJ9hAs75kw_jfx7Ew1HQl3ekUb86OIBmoig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج‌‌‌‌‌دیدارهای‌‌‌‌دیروز؛
توقف‌آبی‌ها درشب درخشان خلیفه و شکست‌ناپذیری‌ادامه‌دار آرسنال دردربی‌لندن
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.7K · <a href="https://t.me/persiana_Soccer/29219" target="_blank">📅 00:43 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29218">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YX2DTT3rONCxTTT139sFTjTYFgCFMxYDAnwJiVyFg2K8A_Mlw2U8DNKYABUgYBVJ6QZVVT5iPTZDHrXJOc1E5U5vZpi5YwGpO7b53vThNwSNmJJxEt7sJFagpwMjxUgpJqS3YB27wLapsYr9kCybQCO36y3njQbEVvdH5reIafmcOGCqcCOpQ7EGp5dO8htcPmd2i5Ez-wd8JsMDbzng_7nvUOiFmTdp_R-1bKs3N8yc4QAri_zHbT31RIptDU7KmWu8lY7A5QRTJYemef-QYXGZrVWH7yZxsv9eHDQtc7Nqp32Ij6r4fFO8po4pmZfDJce7IDzJjXJQxS2tIz5iZw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇹🇷
🇪🇬
بعداز نمایش نچندان دلچسب در بازی اول؛ محمد صلاح ستاره‌مصری‌ترابزون‌اسپور شب گذشته دوگل‌خوشکل‌برای‌این تیم زد و سه امتیاز رو گرفت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.1K · <a href="https://t.me/persiana_Soccer/29218" target="_blank">📅 00:30 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29217">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nyo2Z4N1zjTnqBhIyWyMqwlVtWIa5D0CT0CUTO1nx44Pam8XftFj3eQL0JR0YrRjOFNoniLeupvqhTtdh_m8ZjtJID_SU3MgOnctoqqA9PqWqdgoaX4OOOfVWk1wYsN2l4UCLe03Jvm4LQCW6xgN5hga5l3BpjUBlC0OTPkSYT90Gr8FV2S0qdtlVKCUF4h1RxKuoXgRoPh_5YChXPy6661QHX2pT_Pc4TNcebwaTMuxctM7fU8GESEGIvnRjly9dRzsfcTTic3K2UFPCe4mfxkf8FzFOeNMewieMwd8IA692oENerS4Q20kf1dPieTZLPXtp9kq4Og3IlxEbIWBOw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
درهفته‌‌سوم سری‌آ
؛ شاگردان آموریم در واپسین دقایق بازی گل‌مساوی رو از بیانکونری خوردند و سه امتیاز شیرین بازی رو با یک امتیاز عوض کردند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.5K · <a href="https://t.me/persiana_Soccer/29217" target="_blank">📅 00:18 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29216">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SgbF43lvs3faeoOVaZo7sspLbwzQESIPxICf8bFd_f40EmAIfZZJs6ykrLZlNVW-xOXwQuN7wc0Hz3D11KMdV2U9_QaKsFCscEzVNH5wFzk0atsJrkKjJwFU4hW_KyrbSwxlCExuGkaOla2qC33OyPwNe36nr05oladpkcg_-FfkxdfOb1kI2_yc5-lR38zVq7zwUCQeCB07CPTTft7f-_hcKGbMDkUC448Bxbq1IgWJDFJjb_jN3mE4T5VUXtsZDLbfEOf8i5kwbSI99CeA4HDWnuvywajhYV9YXYqB6zsYOA1dyo-ZG1hCQVcQhjB4T74CyOXmU4mWvlbOnw4y-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
مسابقات لالیگا برای بارسلونا به یه جلسه تمرینی شده! ۱۷ گلزده در ۴ بازی‌واقعیه پلی استیشن نیست.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 57.8K · <a href="https://t.me/persiana_Soccer/29216" target="_blank">📅 23:50 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29215">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ac032e583c.mp4?token=fwwWpYaCLvKgGl6W4LRFAtNBqWwsaEJMtoYwL28CsmixEbv0Kt4aoOmgWa2KfrGLEVumZWa--OEFqS7QoR37BZ62s7J0KhFbrRPUcA1Uk9jtjf9wWXiJuoTnuJq_a8ZPKPvQXhIl9ammJasuYMw1nUB9xC2DO-DgwxX_jejJXYDLmr2OPIuo4qpFf_Rg6V4YWWaYM9VJ8PrbuMkE_SjWoXw7oJzY5km9V6QgMPrf5gBhF7-MxYrdNfJmtMpNwrJj6IvHPYY93xs3bPhZ9ACrZRsDlm986jEZ2FZvxq7iPBM-cBvO9oPjxawDVjgdPVYfLR0cuUpmRwUrokTucOUHQQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ac032e583c.mp4?token=fwwWpYaCLvKgGl6W4LRFAtNBqWwsaEJMtoYwL28CsmixEbv0Kt4aoOmgWa2KfrGLEVumZWa--OEFqS7QoR37BZ62s7J0KhFbrRPUcA1Uk9jtjf9wWXiJuoTnuJq_a8ZPKPvQXhIl9ammJasuYMw1nUB9xC2DO-DgwxX_jejJXYDLmr2OPIuo4qpFf_Rg6V4YWWaYM9VJ8PrbuMkE_SjWoXw7oJzY5km9V6QgMPrf5gBhF7-MxYrdNfJmtMpNwrJj6IvHPYY93xs3bPhZ9ACrZRsDlm986jEZ2FZvxq7iPBM-cBvO9oPjxawDVjgdPVYfLR0cuUpmRwUrokTucOUHQQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
علی آقا دایی هم عصبی کردین؛ واکنش اسطوره فوتبال ایران درباره درگیری خداداد و امید عالیشاه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.1K · <a href="https://t.me/persiana_Soccer/29215" target="_blank">📅 23:40 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29214">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/G4LXVinv11ZO7U0aXSIqXjtF3NRKMOnyQZ4p2Jnp9RfjkZTya-41_jwcGz7chR-_HOqO4X7TexVdGi6AdM5FoQ1nuYBCMCG8etAcUGq16HXPn7nmS776_mpL9QsB86JO9kCYoj4b0TIfZcq7Z1s2uBQ3DhXCFQ2IqhXN1Y1jtApIP2Hb5hIBW3rp3pTkasIzrwU0MMR2RFf_T9HN90ZcVfAOlHBto-m9P30JuBS7zcRMi5tmA0FHQmg4vZ8trOecRAxhEOD0nUGrjWu7EEEtduDwtlJaFjoLXHA7YAs-EO-L5ClDHBjeUfFWx660CMnJUx_ww1dZ0XDJyS8bFdTP7Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
پیروزقربانی‌سرمربی‌آلومینیوم: کاری به توافقات بین دو باشگاه ندارم و اجازه نمیدم خلیفه و گودرزی دوتا از بهترین‌های لیگ نیم‌فصل از تیم ما جدا بشن.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.3K · <a href="https://t.me/persiana_Soccer/29214" target="_blank">📅 23:19 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29213">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XMrlH5jyc0vIm_yc4PEwYFw2XojywUdrkbeHyq0zPo9bPmJWLG-hSEoIqV0wdBFkV_9OOmiaEtAWueI-Xkhn5_lDhbHQkaRhREPPXtsLlzqvBdDyZc3zhuRad07rnQVFiucUzWB21QpWjz_RHsj33wF79RofvOsAAoxUI-P0V-tiamlEB-drdVmqtGjUGs3Z67PWCKVGkKIkU42sgZ2aWDZk7lbXjg-X1585ael51Y8IP43soA_O9OAe7d7DB0_ztFkA5fKNnrCTHy3mIA79KL8AwAfzOd61qA1gh7rhfp1iWvXASCa9-KmkkQorBx3mKqtf5bWsx-29ey9WAk4JZw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">▶️
موقعیت‌های‌دیدار امشب آلومینیوم
🆚
استقلال؛ محمد خلیفه با نمره 7.7 بهترین بازیکن زمین شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.6K · <a href="https://t.me/persiana_Soccer/29213" target="_blank">📅 23:01 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29212">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c32a03f776.mp4?token=jp6SHBltkq5SuY5cx9RXGac4T5IWOA4iblNx4Uhb6eFeU155tjx5GvjWqi7qo28-h1CfT8nNqB-rFfsmzqPA3gcybA0zeZuv-BAQ8mSSGvQHonfDvxiYZHXBtpDIUIY0r5xjfkDoW2f_mGOSDzx3YbjV3-gfKVeXqqlsgBhfWGLtTKruqs400-E2XeH0seC7bAv0Sa2iQ2EzozgINL0JxJ5sjsQGwV9eJ10Rz58xXczmuYaI3Wj0re1d6TktYLAAsedJTUrW0LTX5wEuGvS6clKN7Vm1eMaQ4l-leFpEsgQ10EPszkqvukASgb5pQkagjU6fs6TVgMgK7Cx1mWkoZg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c32a03f776.mp4?token=jp6SHBltkq5SuY5cx9RXGac4T5IWOA4iblNx4Uhb6eFeU155tjx5GvjWqi7qo28-h1CfT8nNqB-rFfsmzqPA3gcybA0zeZuv-BAQ8mSSGvQHonfDvxiYZHXBtpDIUIY0r5xjfkDoW2f_mGOSDzx3YbjV3-gfKVeXqqlsgBhfWGLtTKruqs400-E2XeH0seC7bAv0Sa2iQ2EzozgINL0JxJ5sjsQGwV9eJ10Rz58xXczmuYaI3Wj0re1d6TktYLAAsedJTUrW0LTX5wEuGvS6clKN7Vm1eMaQ4l-leFpEsgQ10EPszkqvukASgb5pQkagjU6fs6TVgMgK7Cx1mWkoZg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📊
جدول‌رده‌بندی‌لیگ‌برتر درپایان دیدارهای امروز؛ سپاهان با همون تک گل لیموچی سه امتیاز خانگی تقابل با آبی‌های خوزستانی رو از آن خود کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.5K · <a href="https://t.me/persiana_Soccer/29212" target="_blank">📅 22:43 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29211">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/I47y57qhpDWlY8MSD34HtoKO1wPgX8Tv0HtPqGJVj5d8h86iBf5i0mcWQSjQRKV4ANUHqbfEzuYAYoSexKuLD0ok0GT9QYuXpOwpcf1-EdhhgPDEqEBWtmdUp9cSBgseSMiRAMl85Tsy8Obre1pPZI6OpxEdvJUcBHOzVE884iUWKm4qfCe-GX5MRHwVhpWEMybkVGrcYXEjA-0gwYM06kX0sNf3zfG2GKX3rXbyRM_p2f2UJbnqFkrmnuMyEnCJ03wV24a8SV5QfqL1Ivp1WZkyBF9VakylzTsO2N6BDzYpifpBAbYTuBBzff4f0CAbzXzR0VS0QvnhVO44HwkCXw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
ویس‌جدیدخدادادعزیزی: بله امید عالیشاه به من فحش ناموسی داد منم به بدترین شکل ممکن جوابش رو دادم‌. من‌ خیلی باید بیغیرت باشم که طرف پاشده اومده تبریز به من فحش ناموس میده و من جوابش رو ندم. بله من صدتا فحش به امید عالیشاه دادم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.8K · <a href="https://t.me/persiana_Soccer/29211" target="_blank">📅 22:34 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29209">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HKeXGMpfNhita-LhSTm1Gjx_kGfE_JDpp1I9OBfUIu5zOYOo61AsDlYEwuUZ56UTywVixh4dX7EVjBjrfcBGTriepfyRlnyULJxmSqWjfz7ZJYybZX492vOhCwErgU7ojwq9MwSyLbs3Cv-eCA45-7e-r-1v4QBdDxuTvo6PZ_IZbHNLSVjgubj4w9ITgEGMn930gxmDl6hQa9nyQu56FFyoxSszSu3jrYtqCDXPXugemnJg_suorR7Rv5DzugVHGqSxshseJWVb9dPajFULHKjX_Rme8vYflPdICB6u9jvA22RIEA7lqvYtyLO8xm2S3iDtGRN10ihnfMvfCRq03g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">▶️
موقعیت‌های‌دیدار امشب آلومینیوم
🆚
استقلال؛ محمد خلیفه با نمره 7.7 بهترین بازیکن زمین شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.3K · <a href="https://t.me/persiana_Soccer/29209" target="_blank">📅 21:52 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29208">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/664fdddf46.mp4?token=ayuorjSZnmQYVdjhDVMbVTeNPbZuAGT4ShVnFMK5WJNOWV2QvybsPrrC5KbqpQ22IociUeNAZiPtlmOymDIycyE9TvyyBfnB7boMokna_QWuEAyvteFSnuFBUi5_UifYrrRBEUzuSOPC1qlZR77KFcU7lRo5BExM80eGlz4JYReD1PAlrYHIRICVIVs41bHhXpAQFX5jQIhhfS1jIaNIcNXjknHxqF-kAl-VeFA_Rpxg-yT-2MfHzG1SYTg8fq_O7ukWjAvJlPU_Ylc3qHV1_UjjUwqk7BMI1u0rAGlZkhwbdHXCm2rmVcjJNRB0dhQJjx5PstwCdyPV9d_D_ZH4XIWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/664fdddf46.mp4?token=ayuorjSZnmQYVdjhDVMbVTeNPbZuAGT4ShVnFMK5WJNOWV2QvybsPrrC5KbqpQ22IociUeNAZiPtlmOymDIycyE9TvyyBfnB7boMokna_QWuEAyvteFSnuFBUi5_UifYrrRBEUzuSOPC1qlZR77KFcU7lRo5BExM80eGlz4JYReD1PAlrYHIRICVIVs41bHhXpAQFX5jQIhhfS1jIaNIcNXjknHxqF-kAl-VeFA_Rpxg-yT-2MfHzG1SYTg8fq_O7ukWjAvJlPU_Ylc3qHV1_UjjUwqk7BMI1u0rAGlZkhwbdHXCm2rmVcjJNRB0dhQJjx5PstwCdyPV9d_D_ZH4XIWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
موقعیت‌های‌دیدار امشب آلومینیوم
🆚
استقلال؛ محمد خلیفه با نمره 7.7 بهترین بازیکن زمین شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.1K · <a href="https://t.me/persiana_Soccer/29208" target="_blank">📅 21:38 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29207">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oZZWRkn_KsVqMgW-W0YtvRIZpTnCb-qcp3QddUa8g_n7P6ZFLbnGb3GgO8F3uv53KRLS2ZHIaQRzvRA1LdbAdLNGWkS-hBRfIehuO_69_mtWK14TkCSERAMv-XajIts7Lnj1ZmRMpAL6VgFoDTRA1TrIgyEiwNH6SbNY5lduLEZRrS9qKpdKov6X2MhJR0pTvztSx-mSyOFK-dm-eeiLxiALBhd88lgkSSYzO1jQgGL_KedU_jGE6E_9y1rZA-42I2aoe3QpPakicjZY_EgMf3rIeaVYP13gPWIxh7ZvwVSPmXlNKzMcR21z3QffeYNmWpdHd-8rFhTQzqAo5YTTkA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
برخی‌از خبرنگاران نزدیک به دولت مدعی شده‌اند که از امشب بنزین لیتری 10 هزار تومان خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60K · <a href="https://t.me/persiana_Soccer/29207" target="_blank">📅 21:25 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29206">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ei-b7yQ8tg9VStm3dSykJG_wQSRxbQJBwisdKWvAUQmG8nVowLrXrhGppfiN8PDMnw92LIQ2SzkMLtpjwfrKQa9WwEWpBb8xCkEyasUVxRvGlS8_CLzQakG-CA532GZ1EN9112HVyFp2uMoY3lf3yCqkHHZ-6yZF2IX1TT7YLNST4Hzn7N9g1IhyN8-ezxfJ8F-71EMYhmZb1h8sUWR2y37j6zXWzSeWOWTUantNo8raY3OIy_R6FgnbppjF470naZ4XZaBGwIcZdgoZNOq5aQG9t6VdIQh3vAUKrw7wRZdjM6QtvyqCpq2kQRCS1sJzRvqyQIhSsCI-PUVbU3carw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📱
استوری جدید یاسر آسانی که نشون میده عزیز گانیف ستاره تیم‌ملی‌ازبکستان هم‌اکنون در تهران به سر میبره و به احتمال فراوان تا پایان این هفته تیم جدیدش رو انتخاب خواهد کرد. اگه استقلال پیش پرداختی رو بهش بده 2.5 ساله آبی‌پوش میشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.1K · <a href="https://t.me/persiana_Soccer/29206" target="_blank">📅 21:12 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29205">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fEq5KeDWAmqWrlOd3bgf4iuWbgYdlpbd5vbOrV595OaF-XRB7nGO_eVQ-hA0Bz3cOKD3qPHj6qPiGU0AQcRgoSN1PjpsowuvBN2HiyXsuqcNdf_jAzGZWL0s2RMJ9g_qkOp-U5OUq6NPkxLkvGA9gQtPFh75Su4rcLkt_T7Vruvr9dn1ey2KlIO18wuDt9hPkJfmHD6jdJTTYGjTP8Aksn9KN-ToxuGchtMs5f1wgY4oFyincKYOQdl-S0k_2KINfBBUWBCxCOgGdzBlkcuYlKL3064N2ToZKt_YEN1h_rKarRCMkTLQTKHPZ4vc8gbaMOYBhPCQskLkhog1xH2ccQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
هفته ششم لیگ برتر؛ توقف شاگردان سهراب بختیاری‌زاده دراراک مقابل یاران پیروز قربانی در روز درخشان محمد خلیفه دروازه‌بان جوان ایرالکویی‌ها.
🟢
آلومینیوم اراک
0️⃣
-
0️⃣
استقلال
🔵
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57K · <a href="https://t.me/persiana_Soccer/29205" target="_blank">📅 21:03 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29204">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iBqpR_OoH-xtjWTTY_i-rOb795X0FeRzDeC7NRDaz2O0r9w4CSALun-GKyDwOj3eOoIFNygWKDLnumCoYoC9j2zlFtarCxqkIaOeepQvFq9_3iAJBMr2yF-BBliN2_4MHcVXaQvHF5woPdrzVtoXMi6L3usvEfwFyNXFdEarle4YV7L8Dxv3RHq49pnGDILXA-642QSkFmqtJY0E7jbOXeWZnKYsyqiTse7xY7FolzBQS-VwnQvXF8qCu5tT9McpgY5CcDKmbl_5zEWuSrnV-ygSuYRpIpZx6UwwPge4U2k0MWqhl3EnsYwjr0Y2yuc_5kVZGhz5S4G4Jr2JZJvtEg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟣
هفته سوم لیگ جزیره؛ شماتیک ترکیب دو تیم آرسنال
🆚
چلسی؛ساعت19:00در تاریخچه تقابل‌های دوتیم‌چلسی 66 بار برده، آرسنال 87 تقابل رو برد و 62 مسابقه هم مساوی شده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.6K · <a href="https://t.me/persiana_Soccer/29204" target="_blank">📅 21:00 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29203">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aJ9C2LmH_WrrQQcQy8HiI6Vbgw6YZsXRSQeE-nylR5yHsPZUL5ruMSh9jPx_ET3Cw9PAfVlZQlvtkpiq-5KMDPKW3pUt0IUBiru4uv3Min12K_VZDy-rbvL9b6oK0S6Ea1XfX6H8EolP4Dix80H839VZbSdIHKztqI7gsIDU2415_P51cxo3cURqTHQozTlvxVkcc9k3WqWTr15aBYrUoyza8lJoTvX2wqHZrcvODP95beyaJzyTkj-q2W62Mo5Wa3elAsR6AX0YrgxwiLUaGkn-xXf3jqfahJAyr5Gb5gL5qfSqlLii_kjUV8K6JoCShhRDMdKzXCBZjqculksd1w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
دبل‌سیودیدنی محمدخلیفه دروازه‌بان استقلال که قرضی در الومینیوم بازی میکنه مقابل حملات آبی‌ها.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54K · <a href="https://t.me/persiana_Soccer/29203" target="_blank">📅 20:54 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29202">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SIjuSB7CBkDx2IHJaPQfmvsNEFYFX2BEkMg4voaXbW7BW1IuUvg9_xI6d4FRp5h6_EjlKqcDPGdGVj8uAxxfwqn9thRUNjATVyVMKb7xWXhN902LLBkrBSNx1y9RZuezoweGTz9AD-Qp_S6r4hC0XgiNtCh78Ag044lHLsg0A5m9bNr6AMLkL43X7dP-vpLIqPOwKQwnkkTeq7gNFHvDCnjKVVdPZEqlKfFXT1hx5fJWWypR_yOwMa9Z9bSlm0SnQJA9VZsOWvyJggqCZLLhe9rpvypX2apTcH9NW4KoDYh7SbRVtATfXmBsYloZU5Xor9L_4MNb_mnUe9cJh_auZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
برخی‌از خبرنگاران نزدیک به دولت مدعی شده‌اند که از امشب بنزین لیتری 10 هزار تومان خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.9K · <a href="https://t.me/persiana_Soccer/29202" target="_blank">📅 20:54 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29200">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a30be494cb.mp4?token=AFvZspfsfLL1D1ATuAHw4mGK5nW-dLJVzDUZYYCaPD4yEmYuM5kVt2dYsOVyhdqraqEDNr_vkyrAq0JgUn5uy9PcdAuLMsqtbVyUFBiNpj_U6AHWomnAZXilhu_qVz1liBVIuhC4J1CUVlfG_IJEGlf1TZKDVjj0sYiGDu1RLIX-0xJluqkYNxthjbIsqU4FwxtmsOfHl3jpmECaHvjH7vBM3irTH6-qdPkBz7AtTbF9cGqRR4y23CbD4PovhzOHSS22ekjYlTPiqAI-yviHMK7OwJG_zvebtssNJCZjAc6qQz055ietOp130fgNphXzro2vUx87VCqRW0Uu2B-reUznM9ZlEkDT7pbHnj7WGea_fnjkEfG49_az_7ck0ZiBCgZ1BamN2qAUX_EAocNQhIk6j0MeikKqKUQMWIBV_sdV834TmPtAxVE-YHZj9ofs9Nmgl_g9LcuGpyVcjvijVvZ_1UfKqf5tKiu31SdL6wlrrr-W_dWqFQOP1F3cEtCJld6JAV-4ZUquNnfHoZ_GzhkZqb4iH4j-7nFh_ILB4QoZmOebBMTGisPfTu2p4oQIX0hrK27kNdiRjsCqxHQNnIPxLanzFdDxmkA9y8JDB8ok-5cpNGWIQbP9hbHbEtpxym0HA6pl9yBvGaxWzTpVZlbdVMnIJ4aPCN5Pa2X24Cg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a30be494cb.mp4?token=AFvZspfsfLL1D1ATuAHw4mGK5nW-dLJVzDUZYYCaPD4yEmYuM5kVt2dYsOVyhdqraqEDNr_vkyrAq0JgUn5uy9PcdAuLMsqtbVyUFBiNpj_U6AHWomnAZXilhu_qVz1liBVIuhC4J1CUVlfG_IJEGlf1TZKDVjj0sYiGDu1RLIX-0xJluqkYNxthjbIsqU4FwxtmsOfHl3jpmECaHvjH7vBM3irTH6-qdPkBz7AtTbF9cGqRR4y23CbD4PovhzOHSS22ekjYlTPiqAI-yviHMK7OwJG_zvebtssNJCZjAc6qQz055ietOp130fgNphXzro2vUx87VCqRW0Uu2B-reUznM9ZlEkDT7pbHnj7WGea_fnjkEfG49_az_7ck0ZiBCgZ1BamN2qAUX_EAocNQhIk6j0MeikKqKUQMWIBV_sdV834TmPtAxVE-YHZj9ofs9Nmgl_g9LcuGpyVcjvijVvZ_1UfKqf5tKiu31SdL6wlrrr-W_dWqFQOP1F3cEtCJld6JAV-4ZUquNnfHoZ_GzhkZqb4iH4j-7nFh_ILB4QoZmOebBMTGisPfTu2p4oQIX0hrK27kNdiRjsCqxHQNnIPxLanzFdDxmkA9y8JDB8ok-5cpNGWIQbP9hbHbEtpxym0HA6pl9yBvGaxWzTpVZlbdVMnIJ4aPCN5Pa2X24Cg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇸
👤
درهفته چهارم لالیگا؛ شاگردان هانسی فلیک در در دیداری خارج‌از خانه آتش بازی به پا کردند و با نتیجه پرگل پنج بر صفر والنسیا رو شکست داد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.6K · <a href="https://t.me/persiana_Soccer/29200" target="_blank">📅 20:29 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29199">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1e23364253.mp4?token=TglGDxTc3lJKrxmcWwVDLkWn5R3urJA-paskX73hcjNiQxpqsvzFYZIXp3w-q9cTVg4kV0UIRANaaGdIEAQwsGhXaulSZER5XiiM7F49iGdtuNyK5BCU_9X8KH6tf9D5fPOS8INAY89UcRyu3sftKG0-hcguTGPHv7i-fV7f7NnMzeBMTdIBEBHWbAYvELXRFvdalxNKILPfdNlS1HBx4VWRVFyGgahwu0tRrn4touVxt3ON3Bo2oXDxnGSZLAtcnY2-DWQm36IJHszFqKfjLmOeatFTE2o5baQKLvhFSfkvx6--ga2f6r9QXeakHjYka5C1qRhZJA3KK2yN9YNAgQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1e23364253.mp4?token=TglGDxTc3lJKrxmcWwVDLkWn5R3urJA-paskX73hcjNiQxpqsvzFYZIXp3w-q9cTVg4kV0UIRANaaGdIEAQwsGhXaulSZER5XiiM7F49iGdtuNyK5BCU_9X8KH6tf9D5fPOS8INAY89UcRyu3sftKG0-hcguTGPHv7i-fV7f7NnMzeBMTdIBEBHWbAYvELXRFvdalxNKILPfdNlS1HBx4VWRVFyGgahwu0tRrn4touVxt3ON3Bo2oXDxnGSZLAtcnY2-DWQm36IJHszFqKfjLmOeatFTE2o5baQKLvhFSfkvx6--ga2f6r9QXeakHjYka5C1qRhZJA3KK2yN9YNAgQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
هفته ششم لیگ برتر؛ کسری فیکس شد؛ ترکیب سپاهان برای دیدار مقابل استقلال خوزستان؛ ساعت 19 از شبکه استانی اصفهان پخش زنده خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.9K · <a href="https://t.me/persiana_Soccer/29199" target="_blank">📅 20:21 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29198">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ERMgMv0LKmP8CLMrNV4ONaL2Bz7w67vyx1G1DkgFQNG0s0cVW1l9P4BMcUP6zfOTE6maraJAtFzYglzrT94AvHNXO6bZlTGzSHtKA1xVi9x3Njbiq0Ex_g0uypDqXhk5axGv8lWTY8x2GIXk-KDisYoh7XYCJXgYUJ-7HlzBevQA9bpeTmPvwpgfjGjE3MEby7-pgqVKw-TATxWJIJ9Zu0o5nid4yKhLtLJOP3lAyXlNQebMe0Tuqu7XncWkVNlv6Qa0ApKpCaDHX1yGcN2lvn5-quMEX15JM-H1OYdmYiRAZTkmQl2tS5xRpvdMg8yiwIebtbhLdudvTzBYUOh1oQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
طبق‌اخباردریافتی پرشیانا از سیرجان؛
مدیریت باشگاه گل‌گهر به سید مهدی رحمتی اولتیماتوم نهایی خودراداده‌اند و درصورت شکست دربازی هفته آینده با شمس‌آذر از هدایت سیرجانی‌ها برکنار میشود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.2K · <a href="https://t.me/persiana_Soccer/29198" target="_blank">📅 20:12 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29197">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EFYxOeDNE8BZog0xtqV8C-NGdCo6-sBaGN_l1DsAf6Jh9nz2kX2S2obsCTm3hhln5KC1f0cqw6xF0uEmcPutbs2atP_wcrv5pOqtba4b2m4yV8zUEksaNFCou5-mE0aUOzBteboBPvE9MvgPoh3HhHNCZFdM_S1nvkO-J4SWxlIps5Al_exO-Owx433-7QYuVqFMsLigL-xjuWfqmtGCJsPhfnkSqf2QtQsYXEvDkUwNXY9h90X-1kDiDCRDLaSvwY7TICVAHel7KgWF1_0qaXEc9_maa9G8YWRXG2-NHiw1qEqHA4dyoGfmTm8_RwEgtZGz-KKC4MLSinA6bkwFzg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
هفته چهارم لالیگا|شماتیک ترکیب بارسلونا برای دیدار امروزمقابل والنسیا؛ ساعت 17:45 از پرشیانا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.4K · <a href="https://t.me/persiana_Soccer/29197" target="_blank">📅 19:48 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29196">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/de348f7d17.mp4?token=MNSCFMzCuedN-WEDwn7pHA-QQwnp6LTByI5_o6vvfeAZPFZAUL7iReYgzk2FOV1AqHS5uhTGtkfKFjYe8GsBy9YIMZGpUMVbFhkAdVOAprSdbxJtpQ06xdYuXOyCqpc7Ujt2PbmViHKctivsKy-YElmenlddHHprCrMPJWor0EPWo6zM3qOYW0a7NZ6FL6v0sdWLaSRdB5WARYTgN0fYbVEsdyfgUes9LfZb91O5sQ_jwfo_65zhvjQUu1pZh5VA_l8ysv7MnxoW8xXUGreUVkYwtVbtNyOAXmzS3szVeV6YzorsWE491nslEMmqQA3rmchtb-copEErKTYEv-1yjw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/de348f7d17.mp4?token=MNSCFMzCuedN-WEDwn7pHA-QQwnp6LTByI5_o6vvfeAZPFZAUL7iReYgzk2FOV1AqHS5uhTGtkfKFjYe8GsBy9YIMZGpUMVbFhkAdVOAprSdbxJtpQ06xdYuXOyCqpc7Ujt2PbmViHKctivsKy-YElmenlddHHprCrMPJWor0EPWo6zM3qOYW0a7NZ6FL6v0sdWLaSRdB5WARYTgN0fYbVEsdyfgUes9LfZb91O5sQ_jwfo_65zhvjQUu1pZh5VA_l8ysv7MnxoW8xXUGreUVkYwtVbtNyOAXmzS3szVeV6YzorsWE491nslEMmqQA3rmchtb-copEErKTYEv-1yjw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
مدیریت تیم آلومینیوم به پیروز قربانی سرمربی آلومینیوم اراک اعلام کرده دربازی فردا با استقلال از محمد خلیفه و بهرام‌گودرزی استفاده نکند که قربانی اعلام‌ کرده که محمد خلیفه و گودرزی از بهترین‌های این فصل تیمش بوده و نمیتونه اونارو کنار بزاره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.7K · <a href="https://t.me/persiana_Soccer/29196" target="_blank">📅 19:34 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29195">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kPeKBYGWQq6xBRLTxHlKwtQZiY4Grc2KfTqyZA1SWybqHj3bxIa4PVoZsbFB2sZiVkir7I0A0niCggcv0oCTQFMSkm-o7SX9vQMV20o5uYU5VBl4XkRslKNjkibAbksdmuX73_sMFqo1l67o5UVtMxA3RXMmsW3vjRtOQG5Fba2LXhIAi8e39wKLNMOMQhYhb1UngntWE3qIqH8aHCkP58flVQkK0dW2Wdzj0v4HGCM6tzH3fLuXf46b0JR1HslhYxLSvd4a-vwtepc987091smOTCzPJrFrjh4LuleWwmLTxfNUS7ArF0t_lbYMabJQ62xpDbJWMIUxLwp1uOfA0g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟢
🔴
تاریخچه تقابل‌های دو تیم پرسپولیس و ذوب آهن به مناسبت بازی فردا: 77 مسابقه، 35 برد برای پرسپولیس، 16 برد ذوب آهن، 26 بازی مساوی!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.9K · <a href="https://t.me/persiana_Soccer/29195" target="_blank">📅 19:10 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29194">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/f7O2V47lQU8G1CLaXFISqhk_fMAWcISRsyQwAFumqiTTTTRWXpx58YCHhvotIQIXIdfN0WSzCh-roZaBKg-gRi9W07bYRJ4xLkh6XTeSYQSHsmFI22S79viFjRrNdjaV_SWuHxtCfTRzwQPvexFJQyLnDTzPcRqzD3oYBYSHUYfjGK37koFhTo_uaV7NDpfObLrpQbBoXZI-C7BDBFZ4jfq9iQUGWSIShC-h3T5oHW_4izQ0PK1UIwT0LDVikPTr1KaFof6dhQCyFn_CVb1aNt-1epoLQcLPRBhpZR6HX9MtZomY4pPgEoT0KrjUKRUU_9fFDvjOaLkUgUnrtXK0gg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
هفته‌ششم‌لیگ‌برتر؛ ترکیب دو تیم آلومینیوم اراک
🆚
استقلال؛ ساعت 19:00 از شبکه سه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.5K · <a href="https://t.me/persiana_Soccer/29194" target="_blank">📅 18:36 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29193">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">🟣
درهفته‌سوم لیگ‌جزیره؛
شیاطین سرخ در حالی تا دقیقه 96 دو بر یک از اورتون جلو بودند روی یک غفلت گل مساوی رو خوردند بازی دو بر دو به پایان رسید. گل‌های دیدنی این مسابقه جذاب رو ببینید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.8K · <a href="https://t.me/persiana_Soccer/29193" target="_blank">📅 18:32 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29192">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/U17Ft9PuI86RvJGlVsNxFn1RBNbwfFk0sRApAbc4Pzcp7ZrKd-sv4PYEZovImALajVtXJtA8Juck_tVjQEgGgD1wJfnqpRDjenGmWktvsDOKEfhuLOgyOdO999TslolfzXUQz6YaauEXPKX0cqRX3MkPEJ_s_DCdC_DOBv-0xYdmHFHbI2TbdmYDUBF7PSM3YuUlabVQw6foJDT3KAbzAQlNcgUHusp17CjJ9dJHRKa3iCk83AuVAHiLqQuMH-Pj5nmNiVN7JRLsbEM_X0Qbiwj3Tax520twMib1VJOre-ieJQ4ZUu0Zs3ZSrllEgHAr5jgG6PytkP-DZszrZJohLA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
طبق‌پیگیری‌های‌رسانه‌پرشیانا؛ صالح حردانی مدافع راست تیم استقلال بعد از دیدار با آلومینیوم به تمرینات آبی‌ها بازخواهدگشت و کنار گذاشتن او برای همیشه توسط کادر فنی آبی پوشان صحت ندارد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.4K · <a href="https://t.me/persiana_Soccer/29192" target="_blank">📅 18:18 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29190">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/fg7kfAb3uUn7uw3jznTasVlXg2PQi_4eK7fJW_seGB2M_JgnjjgSQYJWJALPXECwi09Dcm53GjHW9RzS9J6GDcjQzTgxRR404twwFO2sCihD4pU6OJfps3uOHXaWCB5y5ZZcVO49c41rbkH80OOyqIXoatB0zq5xEs30CZDlZvn5ap9wRo12AwzDgJfhmvOy9bhqxERV5WB60pJPyJ4kYj3BSRTgKhFu9-5B5xBVNcAEWbgYdP-GrGGiVtYzp-GFoNYDGcDLhfBrQ3ulW_tsudyTw_YY1941ojbj30xIGOIAISaIcJEoRZ_Gq8u_UVdsfNDZHzS-Xf_v6TBpJcTtmg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/sjXZz0xN6kxjV1AVDQ1gJcz2VA8kdh9Nt-VFM6zs-OKOPiJVkuhlkiSfVMD5pEncczxgYJIFOfY3p5bReP484DEoVViUxvvm0tPhoGnjWEb2qHOD2HLqWICpvJPioTBVcnetvdlFNtGPGQi3FdAzyBvUwdcyK6GOCF0t-_W5NaHfoAjeLS4frRviNhaw8qqLeOEAZZ_HNMTWoj3GCYlRLeEWMojzgCUOoo3YWe7yleB5zdGRr__xrVqCwJTFte4lunpaTKsMn_6BaAgzqwDewoOqaoLhZUOpcdOzV6PPzVn2tHWBV-SnKNS1nrrfyzvbX1Jdrbt7-NNt9MS7CWRH4A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🟣
هفته سوم لیگ جزیره؛
شماتیک ترکیب دو تیم آرسنال
🆚
چلسی؛ساعت19:00در تاریخچه تقابل‌های دوتیم‌چلسی 66 بار برده، آرسنال 87 تقابل رو برد و 62 مسابقه هم مساوی شده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.4K · <a href="https://t.me/persiana_Soccer/29190" target="_blank">📅 18:11 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29189">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YVVCKUKTZ4wjax4MFPfqsBZF7nPvIfkTzHtIUmWkg32u6svJRvGKoq2SwgQ0YVbBz8CyiV2RovBmpMSQEZfA--a4Vx9GBUiUrpLSRnQ-7YXLvJxlZrJArl8Y9dkPDMUWTzc5QjKNqv2MV6_LeON4P7gB8g-_BHUcupfrd40gtQf31tF0rzXCgmKuP_hfgTkvBU8lOT3RAlL1R_k1AC0ZcMZzGiUAXg5aUpHIw2ZVt3IIFNMzwXYc5bpmygAG3QQAUVSlkuPs1ALi1bZYD5ojfEppqa_K5jyG0JSF7H4ddworUgCNJrAf4U8_67YPNZtYi7dLggH0ZTL4aeTXahqvXg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
🇦🇷
رئیس‌باشگاه‌اتحادعربستان:
سال2023 قبل از پیوستن لیونل‌مسی‌به اینترمیامی ما پیشنهادی دو ساله به‌ارزش 1.4 بیلیون دلار به‌اوپیشنهاد دادیم که اعلام‌کردبخاطر آرامش خانواده‌اش قصد داره ادامه فوتبالش رو در آمریکا پیش ببره و پاسخ منفی داد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.3K · <a href="https://t.me/persiana_Soccer/29189" target="_blank">📅 18:10 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29187">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uad_OPtWjzSMjAdOJGRIrzLRdONFexCwJC_8MX8I8x6wC_DsIUND5gFPC3pAL39Js93wtwoARFeUm6X7MCvr3LNNaOw081SkowZBuUCrCRbghNmZJ8uTc9dE-vwN-5JwkEZSEooUyhNfzM0ojKaz-rmnRKWKOdkhnwMO4Zb59DYBrswEAjdRu6It4uW7DRDd4LbLwvn6CDupYsFNLJaskZX0yFwwE4CqBnqIoQ8vTrEFK6POV-bekCFp31axpJHGg_YwZnTgdeR_FasSgQEBELxvgZrWNGHwhEa0VJd410NpzY_-vDZpPF3XLMKsOV6GHmwXUB8fjo6hsGK4a0AK3w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
ترکیب احتمالی استقلال برای دیدار امشب مقابل آلومینیوم اراک در هفته ششم رقابت‌های لیگ برتر.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.1K · <a href="https://t.me/persiana_Soccer/29187" target="_blank">📅 17:50 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29185">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/MXpGTdIs9B0tMV2h8h5eE94-970mSRn0uKLVf0lQSY8X9PO2P1irjWca7GAS9Ew8DBRVbUm_BDYWPUH60Q1AkViiBFNSf5OYH1VK6-uRUY38-4hb7uxw3KSKsQfwS3BXdyuebJhvs5oGOZpJTEJ5qZRK8QR3eSDcNb2swFlzU-3HUFlFdzV-jGMNxOCsuqexUx89uqkmjnq4pkL4KR8IrwFNau1vTB2-MrxglyL1J4VAdamXxuQT5CKYCriqG3Ot4mgHRMnAfGUPkcvfSPZMY_4ir7QbtcUnhFp_SilFhCoRe-3Lu34r3LbjAvkq82GTzYCbW6zhSOCFJ1pFyhMHTQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/UZwvPdNuH2K3HxfMfPcZEGZS-kXpdaj8UDXq6AaOoQTdMvT3trWiLkzlgUNI8LCIwxB6HP_HorSyg7atR0189s08cdi93F06rz4bffENtc2mBwZ08Ws_Aehuis7Mgel08jCddeZhAQd4cVPmw39Y4GPwq3nWLVoeQIhXTJmYx7OiItCrF8KuYRgoJ1tN4IHLImZw2ANP77MHRHr1WHBpB6F-m8LVTOxOlBko8Ispk_BTvbr1jmEpJRKqJls4up97PL4E6UHkmgRm63Y3gff616Iz9XZmvWjZXgvOEcYPIVDjt_pQCZ_E6uqtheEfeKuokXwPW1-9ombevqz9wiE40g.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">✅
هفته‌ششم‌لیگ‌برتر؛
ترکیب دو تیم آلومینیوم اراک
🆚
استقلال؛ ساعت 19:00 از شبکه سه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.3K · <a href="https://t.me/persiana_Soccer/29185" target="_blank">📅 17:46 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29184">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EhzrcpAU_FJxRgEbJ2-wZtl5LTl18Q7_FIPrWx7xWSj-GfsF0VSzckW_m3ltR6H8wLyPJpDgYId9TXbFRhVPBWvBaX3FKmhuw6ZCYBnVoHpxIduoCONxF6_BIss-ERBRfxrs3D8Wpi5jWgGahlDkg0FfRXAif54Wv9MM44T4AfWnpGoxh9ZvQmmE4-TNCYx5_sfBePSpyIEsghV24jYV-hCqgiiy2QU5ITNk7YSwUFYFmVanp-p0cbUchBCL4W92RVINeiaIUVk0DZUQSRr4anAsklDV4wJmMZwcFDaG1Cxbn98mf2qedY7gxFOFfPMNYcI6S3U-1QnEBX7OGzmGFQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
باورش‌سخته‌ولی توسال ۲۰۰۲ تیم پیکان یه اردوی ۱۰ روزه توی انگلیس برگزار می‌کنه و اونجا یه بازی با من‌ سیتی انجام میده. بازیم یک یک مساوی می‌شه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.3K · <a href="https://t.me/persiana_Soccer/29184" target="_blank">📅 17:21 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29183">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ae3b4709ec.mp4?token=fIpN8M4uZJlBSzdhxDRs-uUGV_UATOnHh5udmym1BlZ0816GE6R2eNFBhpAtxEZR3PSgPwTgpzewU-lTuzdZv7sq2RVLIVTrjbWnMiL-jprDQIwBw8bx1gw3XY-YRgjjbRF6SGLqsWKrwqGlku2Je6RhE2FJ5Cw0DjS0ceEqBvWD8D4NnClbXem-K81fJqCH4iLkS7ei64wrFqUYLc0cNHgkv2-ZZkKsg8A1os6YdTwdU6uEUOY65mvAY0y8WefF_9jjS8KVzKjKppYW6JlGURVSgAfVkb2nBPf_ast_KCGU-x2wfIyzexjJhEbylo1gcVLL3SEH1NZ4agqbhmW8zxy-l3QJGBQfqDLTbAis7ZZGvGE1m4-M4ddHpZ7Eje3toXECi-WPtpiKxVHTYOHVIl6B0jpPe1UJazTcNDZl1wZwu7dgvVcEGVN4zuPFheIMb-gPlPnbU814vvAkkxbgAVL9UUTIAx2_-LhzeKnSGvmreG0ikSET1-HG5PfqJi_MT4OeWADeFGFx9c3Rm-SSU-x97-yrg1KWz2DoeOUUqAY5SwR0CP3DH4jGs7dNa9VUkKVOuOnU4Ca4XFOvummUEgCuCHWjRVRcZIah6oX2det032gY8LAPCfFJpAg0w44FvPvZ2bm3dBG2MpNSvTEK3wPs3iRqF7BQaWxGRvS0ItY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ae3b4709ec.mp4?token=fIpN8M4uZJlBSzdhxDRs-uUGV_UATOnHh5udmym1BlZ0816GE6R2eNFBhpAtxEZR3PSgPwTgpzewU-lTuzdZv7sq2RVLIVTrjbWnMiL-jprDQIwBw8bx1gw3XY-YRgjjbRF6SGLqsWKrwqGlku2Je6RhE2FJ5Cw0DjS0ceEqBvWD8D4NnClbXem-K81fJqCH4iLkS7ei64wrFqUYLc0cNHgkv2-ZZkKsg8A1os6YdTwdU6uEUOY65mvAY0y8WefF_9jjS8KVzKjKppYW6JlGURVSgAfVkb2nBPf_ast_KCGU-x2wfIyzexjJhEbylo1gcVLL3SEH1NZ4agqbhmW8zxy-l3QJGBQfqDLTbAis7ZZGvGE1m4-M4ddHpZ7Eje3toXECi-WPtpiKxVHTYOHVIl6B0jpPe1UJazTcNDZl1wZwu7dgvVcEGVN4zuPFheIMb-gPlPnbU814vvAkkxbgAVL9UUTIAx2_-LhzeKnSGvmreG0ikSET1-HG5PfqJi_MT4OeWADeFGFx9c3Rm-SSU-x97-yrg1KWz2DoeOUUqAY5SwR0CP3DH4jGs7dNa9VUkKVOuOnU4Ca4XFOvummUEgCuCHWjRVRcZIah6oX2det032gY8LAPCfFJpAg0w44FvPvZ2bm3dBG2MpNSvTEK3wPs3iRqF7BQaWxGRvS0ItY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
👤
درپی‌اتفاقات‌دیشب؛
به احتمال زیاد خداداد عزیزی سرپرست تراکتور دو الی چهار ماه از همراهی تیم تراکتور محروم میشه و امید عالیشاه یک الی دو مسابقه گل‌گهر رو به دلیل محرومیت از دست میده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.7K · <a href="https://t.me/persiana_Soccer/29183" target="_blank">📅 17:06 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29182">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f8cb4f04a7.mp4?token=B_YZrhKVh0SUyvD5sV06ktLU3PWZik4ZSqE_dPkEZNujt8C205VBCcD1YhWB6xMbyIGYP5XZs6NqL0BuisCCVFarpQgbUhgKZ6UXJlhaTzSSBVFq_3h-jq8nJ9SSPHP-nLOt1zdmdTIunsN2XrMdhhvRVTK1Sfd2-yUYXto4iukx44Y0niF_hQ6TCTCeuEecyZ6Dc8ydUyoUBOgi5H25BIGyGI2VTDKjDavd7kDQxtSd-xCY1W0bOZclnijVi59-j342TAbiaOXw3U0HdZHWCX0u6waQlVNsyJv1llpizCWM5XlRHeVKvF2eZMyOx9hnyVuOJYx4TfctqMqdra60hg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f8cb4f04a7.mp4?token=B_YZrhKVh0SUyvD5sV06ktLU3PWZik4ZSqE_dPkEZNujt8C205VBCcD1YhWB6xMbyIGYP5XZs6NqL0BuisCCVFarpQgbUhgKZ6UXJlhaTzSSBVFq_3h-jq8nJ9SSPHP-nLOt1zdmdTIunsN2XrMdhhvRVTK1Sfd2-yUYXto4iukx44Y0niF_hQ6TCTCeuEecyZ6Dc8ydUyoUBOgi5H25BIGyGI2VTDKjDavd7kDQxtSd-xCY1W0bOZclnijVi59-j342TAbiaOXw3U0HdZHWCX0u6waQlVNsyJv1llpizCWM5XlRHeVKvF2eZMyOx9hnyVuOJYx4TfctqMqdra60hg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
عمرمفیدقطعات‌مهم خودرو؛ این پست رو ذخیره کنید و برای دوستانتون هم بفرستید بکارشون میاد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52K · <a href="https://t.me/persiana_Soccer/29182" target="_blank">📅 16:45 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29181">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YTplXhgGBH_Oup7n3zgKS6qOZvit_0b8MXcbCaDya0Pl1BPQa6c37DcCBe_4eyWDYUS3a2Y_YDI0Ok72FMoeLLA5T8WAtGC5pfsSflsdeMo5KwJm6B3a4tZlAXP-S0GPLByNOVR3AwadS_6C1zP3v__gJ0Fxk5ARNyBFuj4fwo7z0qtAbMkEet5jbfccxotjBoEZDVyUGN0d-FpPJs8zEOmy6_H8B7hDuVCYvKjz3c_i8PABKpuO76ZpzyLkNeIZeJn2-Bl5OZ3547ieb9Xc1VkPu1InZCqJXu7zw5Dp-_oeGAXRZb4PSxMFHHKQgaHm4Y6vIXcwQykO8eLFIzzk5Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
هانسی فلیک سرمربی بارسا: یامال یکم از ناحیه خصوصی احساس ناراحتی‌داشت و امروز جدا تمرین کرد، اون مشکل خاصی نداره و با ما برای بازی بعدی سفر میکنه، فردا تصمیم میگیریم بازی کنه یا نه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.2K · <a href="https://t.me/persiana_Soccer/29181" target="_blank">📅 16:36 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29180">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/B_wTJhUyssrVRrutuzTv7hRpFFffKixVBGnmyn7vmKpftQjHarb0_CIJldYyEabEQBsDVElKFa5ZNWmp8xyz1VvuxD64lAnr4-Ho_Tt0N3-TCTkx6Q-JHQtxDFaxM_Nzpoj7hsplBQdD7Y8xxlmcf1fJ_8SQ_rI4TsHl63JhyFDh1CXTsDCHV8_F7W3f6f_kSlUtzxCLCX1NxF-gEh61hSscTacld8Iv-n4tB01mAhPCnHJPBqbm4DO0c3deneSNqE2AwChGf1m9MecEzMu4Vfya7DtFxO0lf28iuHC7_TL3SSa-LknWdoQZO7nDRvRqfEn05HhPM09NTTYCg47Wlg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
#تکمیلی؛ باشگاه‌ماخاچ‌قلعه‌روسیه به ایجنت‌ محمدجواد حسین‌نژاد اعلام کرده که در پنجره نقل و انتقالات ژانویه "نیم فصل" بادریافت یک میلیون دلار رضایت‌نامه حسین‌نژاد روصادر خواهند کرد. سعادتی این موضوع به مدیران استقلال و هلدینگ رسانده. حسین نژاد درپایان فصل…</div>
<div class="tg-footer">👁️ 52.1K · <a href="https://t.me/persiana_Soccer/29180" target="_blank">📅 16:18 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29179">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kjlcbaUQffq2q9k24A9gQB-GNajczzIHZ4kL5FdS8OWWU8DRsc1lLhQLpE79alEoOLrZuQ1TCKXAFnVoNDFM6qCLyROibgDZ5R6YTt6xw8_3Ar4LmBerh9RPL26F5xRXVG1g87kMCDdMXpXchrhrMrc7yrjymmyCFzlNdghgZrAzylA016EgBPHHa33iqs6boU-q91NrHsunw2kwt3hf7PwlGUzPCJcMBT-LtyCOVB0PQ87Wqdlhu15sP_ZBCwnxm5OAMgYKc8oS49MnhFqe9mKHins1i307B_N7I6HsZwFXosQXb2BQBziB3CxtfTIwDfSfpTaiB-v0AmYjZvqWUw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🔴
دیدار برگشت شهرآورد لیگ برتر بین دو تیم پرسپولیس
🆚
استقلال به‌احتمال‌زیاد 20 اسفند ماه در ورزشگاه صدهزار نفری آزادی برگزار خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.1K · <a href="https://t.me/persiana_Soccer/29179" target="_blank">📅 16:10 · 15 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>

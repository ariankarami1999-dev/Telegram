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
<img src="https://cdn4.telesco.pe/file/FloiBnAlff_ltE4z97atjFzytzVqwArVVCGCNmy7ewBXzpfF1bmYR_mT9YOK2qy435b4GwvFlrNUzXsfFh-Q43Nmfrg12GVJfAWawQvWByqJtxT-CKUaR9PdlqovcQAJErEWcz05ZgyZ8mqkK2mKXADBOG6zKKqzpIlXImbdCab3eo-wS_ytqC1t-G3Ns5U6vCgIDO6vkzctoP7mRSe0_jaH8DAlKkaJnXTjOWXPGHw40jgq8tBaBmxcvopNmJOBFElDkuLRF77DojB2TagV-SKlSX3kDi-8St3phBQr0hN_aikQXxMfp3VAP16e4eP-nu0rXczt_LyYmJu3HhxSEA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 هات نیوز | HotNews</h1>
<p>@news_hut • 👥 105K عضو</p>
<a href="https://t.me/news_hut" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 بدون هیچگونه گرایش و تمایلات سیاسی، همیشه سمت حقیقت و مردم.</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-07-11 17:51:23</div>
<hr>

<div class="tg-post" id="msg-72679">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4323337b42.mp4?token=Mt2I6NRUexHkIdBFHCHhN3HJzTaC0hsX_5_Kmv2EjBxs58MQMsZKAbul4OHbXPRhz46sLuTuHuEntNrMjyPrLFcZPT3kP4jPnfnJIyxxKnhnynCcRrR7FgGHeeCQLVR3Nqfh-OOqkK8vD7AyQpx9_FE8PMaQfhXm1XYEeFvZOynGKkj571ZqtuvhsHrPPqpBpTLS3yR3JtGU4L-xn0vaDhPurOlRGl6uSwMJv0SXRapbIVZj_2YY_WtMx-EP9-Kpa8VP9tuw2fe_26sQCq1nF5X0Arxl9xgEuGnlsBzHuv-4IBHyqT79FNtqE04rh588crafHj5I9iRaZ4mvfEg_qg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4323337b42.mp4?token=Mt2I6NRUexHkIdBFHCHhN3HJzTaC0hsX_5_Kmv2EjBxs58MQMsZKAbul4OHbXPRhz46sLuTuHuEntNrMjyPrLFcZPT3kP4jPnfnJIyxxKnhnynCcRrR7FgGHeeCQLVR3Nqfh-OOqkK8vD7AyQpx9_FE8PMaQfhXm1XYEeFvZOynGKkj571ZqtuvhsHrPPqpBpTLS3yR3JtGU4L-xn0vaDhPurOlRGl6uSwMJv0SXRapbIVZj_2YY_WtMx-EP9-Kpa8VP9tuw2fe_26sQCq1nF5X0Arxl9xgEuGnlsBzHuv-4IBHyqT79FNtqE04rh588crafHj5I9iRaZ4mvfEg_qg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حسن مرجانی، رئیس انجمن صنفی تولیدکنندگان شیرآلات ایران:
اگر این وضعیت اقتصادی دو ماه دیگ ادامه پیدا کنه
کل کارخانه‌های شیرآلات کاملا تعطیل میشن
@News_Hut</div>
<div class="tg-footer">👁️ 2.49K · <a href="https://t.me/news_hut/72679" target="_blank">📅 17:32 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72678">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">ناو هواپیمابر USS George Washington  در حال انجام عملیات پرواز در آب‌های منطقه در خاورمیانه است.
@News_Hut</div>
<div class="tg-footer">👁️ 5.14K · <a href="https://t.me/news_hut/72678" target="_blank">📅 17:05 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72677">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1c0fbd5c19.mp4?token=AsWpsfs9GwRn9dc_AkWzTsikuIk0uGLZI8WCWe7XUjK7j_TUTxCX6W96PJ_ZO3qp4h1aYJbUCNY3sFFyXaJdJ2jMgwuxd0985fhYjI7lV8DGVFC37B-6ybmUjJAwXOWUVVrHSUjK2kK2al6DReofp7e0FGFaIW-zFVoP5Ke3wpaJVPWSZCSAjkfQaDGXFxPm_M5lyIJN0J1ZmbomCWiwKd6LO_H2jKZ_Xnt82VmqdX0usObbIe0imZ-gbEpR4CCg0FRwRHePrHQ3iNoMmj7hNRN2HpVqx0i_lQgw4ivBgpdsbCMhnMiaK5ZB4fsumKcdKTR42c8UY5cdNfU9bTkLKg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1c0fbd5c19.mp4?token=AsWpsfs9GwRn9dc_AkWzTsikuIk0uGLZI8WCWe7XUjK7j_TUTxCX6W96PJ_ZO3qp4h1aYJbUCNY3sFFyXaJdJ2jMgwuxd0985fhYjI7lV8DGVFC37B-6ybmUjJAwXOWUVVrHSUjK2kK2al6DReofp7e0FGFaIW-zFVoP5Ke3wpaJVPWSZCSAjkfQaDGXFxPm_M5lyIJN0J1ZmbomCWiwKd6LO_H2jKZ_Xnt82VmqdX0usObbIe0imZ-gbEpR4CCg0FRwRHePrHQ3iNoMmj7hNRN2HpVqx0i_lQgw4ivBgpdsbCMhnMiaK5ZB4fsumKcdKTR42c8UY5cdNfU9bTkLKg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">#فوری
؛اسکات بسنت وزیر خزانه‌داری آمریکا:
برای نخستین بار در تاریخ — از زمان آغاز استخراج و صدور نفت(ایران) — آن‌ها در هفته جاری هیچ نفتی روی آب (در حال حمل‌ونقل دریایی) نخواهند داشت.
آن‌ها هیچ درآمدی نخواهند داشت.
@News_Hut</div>
<div class="tg-footer">👁️ 8.29K · <a href="https://t.me/news_hut/72677" target="_blank">📅 16:26 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72676">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">صدای انفجاری از سمت دریا در قشم شنیده شد.  @News_Hut</div>
<div class="tg-footer">👁️ 8.36K · <a href="https://t.me/news_hut/72676" target="_blank">📅 16:24 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72674">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/kWo3MLBoJlLaqk657NyWrma6CHqFeWuHr4OuQa_1qquQLqPHW-Q4P_GDMVRJnz5-oWJSUlGxpyaQvAiQ-AS05YUtRWqIER2pYavd9spyflrOeJM2ndWlnilLn8WH1rLRsw7seuXntOqFs3ztZqXc_x5EFO_7OrHTjac5UJPWEMEdgQ4bVrG1KNcdvAc3xq-Smoz094EQUoLXXMbYlDi69HuP97lMS3XmLWgLDSivE1_eD9c-dwi98N92GjcQlEos4Ag5PgvNG-an1SX-5qMQaV0erxfUPrGRWqlzhCLc4ZblLpApElTwhgT9nuVJtNdFsnWqdEpCPwqbils5-YErjA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/MaoFcsOpEMS_ghTwfZI-8CNbUQjL2QtRV304VMwH5IKgwAfPJLySOeVciHLshzscsDoWNN6yJXvgEJ4yj5l1Ykcy_xvA2GT94d0fd4hyCQ54t7i6_nPmIr5DcGmHUSVOzroMKqFqDdvbecDhO8L16upCa87CqKJDNp74SEd6OCp1j3SQCNruHddTYPMPue5oG0PyF1ewtPxSQ7ey8b_1qaSjfDZXixwootGVuabC2r4IYAFwqPTShbWutwKkexCIVGa0_S0LnBNT8WGrFV4sIOr1m7NVfMBmQnpkRDNchjhoBNpljTDUtLxoGsZRV7MOzzEFB-uzGUjHd-ImcS2RbA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">نمونه کار:)
@News_Hut</div>
<div class="tg-footer">👁️ 9.72K · <a href="https://t.me/news_hut/72674" target="_blank">📅 16:04 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72673">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nqSPpzwDdqKNWHN7TTmwnoV9HKjAP2xw7-WfZ9Jipg2rXo17J2dj7AkSWloQ-3VOEyDqDwKHIqauyrpKXLIxJQQGsvNUvr541sAi-hyCu1CQGjGi1I4G4uxTlhUDsPrvxbfwdOsvhP8J1I3sTazB4_URyednQJkeS-a3Gi4pZZFBpc1M3yUPUoJ9DUYfM7pyNTPJRJk-sj9hmQzXoOJFHaDcwuQZLuaq3NTtkWslM2YuIliJx6JnzVdoUA0XjUHk8oOF5I5KoecossoXzYT-jCG6hWXOunF7UjZzxwB8mbtvU1z6jryMi3x05NUv3Q9u-hvhDS7CfHxSQhWpmYb3Fw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سلام به دانشکده 05 کرمان
✌️
@News_Hut</div>
<div class="tg-footer">👁️ 9.72K · <a href="https://t.me/news_hut/72673" target="_blank">📅 16:02 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72672">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">#فوری
؛نتایج اولیه کنکور ۱۴۰۵ اعلام شد!
با ورود به پنل شخصی خود در سایت سنجش میتونید کارنامتون رو مشاهده کنید.
@News_Hut</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/news_hut/72672" target="_blank">📅 15:37 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72671">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c967ea5781.mp4?token=uDs_hMw5MvYVAi6oFUlFNIvBJy63HoFNIWek2438XhOK2iC2bsEV6IvS54wxXfOaFVkvVkmgN-Kx8_Jk2HxoxHsWQT94YC6PkhF2JBHpwMPn9-Mr9c38C7_nfFlsSjnSzybS0k6o6XykNB1y_ZfjZuuU1HiqgrJxXJXmNSgtZPWvgmZx8rsIByWdt3mSii_xvcx3J1_8MLuW6wLj-8sWwJErBx_tvXeY0wQ9LMd9bpY1j8uTsO_6gJS1IPKRUQI74wcSwb5-EgHgPA7XkIzvcIb0ZNBmsN2Wdo9h61sYrqoqYfOb8u5sLB0SoszXSrFwnOkC5BHKAOaaqIJe_8ViLA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c967ea5781.mp4?token=uDs_hMw5MvYVAi6oFUlFNIvBJy63HoFNIWek2438XhOK2iC2bsEV6IvS54wxXfOaFVkvVkmgN-Kx8_Jk2HxoxHsWQT94YC6PkhF2JBHpwMPn9-Mr9c38C7_nfFlsSjnSzybS0k6o6XykNB1y_ZfjZuuU1HiqgrJxXJXmNSgtZPWvgmZx8rsIByWdt3mSii_xvcx3J1_8MLuW6wLj-8sWwJErBx_tvXeY0wQ9LMd9bpY1j8uTsO_6gJS1IPKRUQI74wcSwb5-EgHgPA7XkIzvcIb0ZNBmsN2Wdo9h61sYrqoqYfOb8u5sLB0SoszXSrFwnOkC5BHKAOaaqIJe_8ViLA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بسنت، وزیر خزانه‌داری آمریکا:
ما از این مناقشه با ایران عبور خواهیم کرد. به گمانم عرضه نفت بهبود خواهد یافت و قیمت‌ها به‌مراتب پایین‌تر خواهند آمد.
روند افزایش دستمزدها ادامه خواهد داشت، چرا که شاهد رنسانس (احیای) بخش تولید هستیم.
@News_Hut</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/news_hut/72671" target="_blank">📅 15:26 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72670">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">صدای انفجاری از سمت دریا در قشم شنیده شد.
@News_Hut</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/news_hut/72670" target="_blank">📅 15:10 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72669">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b2fafdeb0b.mp4?token=Dy6HyaZeFOgJ7xoi2cPdwU2wqH29jEwUerY4SFIpcl-vMKL2f2WBIVfxQ0_dlvN1rPIYKBRJuRJaqSyyuQeHmenCL69kUHek717T_Die2m6tpr8dR4vlGjKna0LIaCTeynqIRQq6y3z0VtMQPUcnyDoDAZa0U2n7FGuZPCZRc4fU-82yAjyaZh-UwB6Mw_WYkLNDrQZVOSgME5gpKCQ46B3b1EXUkMNUpJ70gpX0V_xSkO-IcLqI0ExH6Ce-o2GZv2BnWS3e51RvY9efgDtpxpzQuf3BoTQ7Y9gaZsWIqN0Xp6UPEUiW_koroZJy_JO2ce9mElkpvaQJWf_WPvYZKQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b2fafdeb0b.mp4?token=Dy6HyaZeFOgJ7xoi2cPdwU2wqH29jEwUerY4SFIpcl-vMKL2f2WBIVfxQ0_dlvN1rPIYKBRJuRJaqSyyuQeHmenCL69kUHek717T_Die2m6tpr8dR4vlGjKna0LIaCTeynqIRQq6y3z0VtMQPUcnyDoDAZa0U2n7FGuZPCZRc4fU-82yAjyaZh-UwB6Mw_WYkLNDrQZVOSgME5gpKCQ46B3b1EXUkMNUpJ70gpX0V_xSkO-IcLqI0ExH6Ce-o2GZv2BnWS3e51RvY9efgDtpxpzQuf3BoTQ7Y9gaZsWIqN0Xp6UPEUiW_koroZJy_JO2ce9mElkpvaQJWf_WPvYZKQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">واژگونی ترسناک کمپرسی بر اثر ترمز بریدن در کازرون
💔
@News_Hut</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/news_hut/72669" target="_blank">📅 14:57 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72668">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">پشماتون بریزه!
ایران‌اینترنشنال در گزارشی درباره مهدی نادری جهرمی، رئیس هیئت‌مدیره شرکت تهران‌اینترنت و مؤسس و مالک اپلیکیشن هف‌هشتاد، ادعاهایی جنجالی درباره ارتباط او با شبکه‌ای مرتبط با موساد مطرح کرده است.
نادری جهرمی با نمایش چهره‌ای کاملاً همسو با جمهوری اسلامی و حضور در ساختارهای اقتصادی و تجاری، به تدریج به موقعیت‌های حساس دسترسی پیدا کرده است.
ارتباطات و فعالیت‌های او در حوزه‌های بانکی و مخابراتی، در اختیار شبکه‌ای قرار گرفته که با عملیات موساد در ایران مرتبط بوده است؛ از جمله انتقال اطلاعات، شنود و نقش در برخی عملیات اسرائیل در ایران.
این گزارش بر پایه اسناد تجاری و قضایی، مکاتبات بانکی، قراردادهای شرکتی و روایت فردی با نام «کیا» تهیه شده که ایران‌اینترنشنال او را مأمور سابق موساد معرفی می‌کند.
@News_Hut</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/news_hut/72668" target="_blank">📅 14:14 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72665">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/K1jXhcYJ4FY-62Y1EDt47Uwfe0M0KpKsAFEmyBZRbcLgPRK0GiAHPlJ67A6EhruGxIgOpPAmHlRZX4nEZuLRcblCjucjHnMMmIl7ZhcwfQSOXY_7mfBAE0EjwC7GOaHEGpP9SI7RBEd3jdUjNp1kIGi2fPXBBCs3Wz8pD5PMiueZgznBw7TxgtNjLHkrce5xho6wXnwr9Own_Fb7v0ZNepnvwLaLf7AbZWJPQzEeqgZcETSbz4nsjGHKrAP1SGv1QeVZOCE23S47kxBW7gNL_BVaTPJY56xvwIAPtG89LG6eR3cD3FEp-aeV7ApIjapguQwK4e21lkq8GhSU0MB5sg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1908d250d4.mp4?token=AodPMVCX0R5w0ldoYkrWVw9576f1gYMNQJiOl0VJQ3S3QM-fya5bdOCKLHjbOA3G6-ZbZnXrSyxcB_9kU7ADNUGAb17XKLn8ChXG3cv6l_NB-YEr64tZMjCo4NVwagHQXxtErhPLx2eQcAzjVx_xo8pQ7-ijpASRgLkEikby5c1LPI-PlLiBKJi5UgwdREs8npXSkF2FRFyKoYJU3miuNzcQ8UC7eTI3K0T6v-lhMIgxGOfEoUiPKXmyQiaYdKHSCJ8EGe5IIuIXAvitEUbL3maBhnPNjiSFw9KsxVibNtN5h46PkZp-s3AihNo3nGgLhNMiyW0xkurr5zrNJSWlAg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1908d250d4.mp4?token=AodPMVCX0R5w0ldoYkrWVw9576f1gYMNQJiOl0VJQ3S3QM-fya5bdOCKLHjbOA3G6-ZbZnXrSyxcB_9kU7ADNUGAb17XKLn8ChXG3cv6l_NB-YEr64tZMjCo4NVwagHQXxtErhPLx2eQcAzjVx_xo8pQ7-ijpASRgLkEikby5c1LPI-PlLiBKJi5UgwdREs8npXSkF2FRFyKoYJU3miuNzcQ8UC7eTI3K0T6v-lhMIgxGOfEoUiPKXmyQiaYdKHSCJ8EGe5IIuIXAvitEUbL3maBhnPNjiSFw9KsxVibNtN5h46PkZp-s3AihNo3nGgLhNMiyW0xkurr5zrNJSWlAg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">هزاران دانش‌آموز دبیرستانی فرانسوی به دلیل کمبود معلم، ازدحام بیش از حد و ساختمان‌های در حال فروریختن، مدارس سراسر کشور را محاصره کردند.
@News_Hut
| Clash Report</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/news_hut/72665" target="_blank">📅 13:42 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72661">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7b9ce8d805.mp4?token=M6RNUzYQJSqzpEXK2EIq5TvtimRDD8oPUQZmJVnqLOf_-GGOqnsmz5d5QkYEqh9E1gL3T7WzXHxYzoRNBcnVc3T1U0wG35F8uY1XeBShWZcHGk1ta-WNYHVWWYy9X50pTn0MY3pBWWx03hoaOr4gMEeanzc1MXavKia_HZ_J914GncIMAdSiFLMVsdQnAKGMQ1VjhY38kl7U5Y-50cWzPwgroHvDHxmEiNod1GGvAwr5iVc5jkXDSICugpgyBIvXo7YC9IHmCDgFVC8FFOCnlGoLkaDc9mPM8kxoHSeIVua9Bf0L3CZjzRduk0DQP1AxskI4g9aG1HrMZrId4esQLQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7b9ce8d805.mp4?token=M6RNUzYQJSqzpEXK2EIq5TvtimRDD8oPUQZmJVnqLOf_-GGOqnsmz5d5QkYEqh9E1gL3T7WzXHxYzoRNBcnVc3T1U0wG35F8uY1XeBShWZcHGk1ta-WNYHVWWYy9X50pTn0MY3pBWWx03hoaOr4gMEeanzc1MXavKia_HZ_J914GncIMAdSiFLMVsdQnAKGMQ1VjhY38kl7U5Y-50cWzPwgroHvDHxmEiNod1GGvAwr5iVc5jkXDSICugpgyBIvXo7YC9IHmCDgFVC8FFOCnlGoLkaDc9mPM8kxoHSeIVua9Bf0L3CZjzRduk0DQP1AxskI4g9aG1HrMZrId4esQLQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تصاویری از انبارهای نفتی آرامکو در ریاض که هدف حملات موشکی حوثی های یمن قرار گرفته‌اند.
@News_Hut</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/news_hut/72661" target="_blank">📅 12:51 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72659">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Ef95Nu4HOMghwLTOlxkGknIJ-gRAFXgNS0pzoVPNAHrrEJo9IQzDLuBa0c0IS6vffQT7GdN82KvujCOooWGWH6EQDqWPlX0m3FJvmttGtqTVkrSX4Z0zAQCbGGkGMvTcXTh5QAIQauoo9CggCJWsDbNl5ZIekxQYeDLkwcrgN6vnvlJjtbEMtnkoGiuXKfPrcOCUPGvfpPjskyFAijcFuJIzuYk5mwJcGSKMl3bKOADEUlNT9oR1U32qJsmy4i1eETjAUJvW2eDl3qNnj41iBt4t-dcNtwbWgmjucnPl2nlLgTkJG1y91AJy_dXzZcYoHp-tmgh2dEtvKq64j3clfA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/cc83c2d7b4.mp4?token=ofLQutWYocIOGQ1HcsJgl1v0xb0QIuqHghtKJx8x4vcWXfL86tUzpdYlF9d_SppVxj7wwZatawP_6Tk7GAqTm7-cDjrvsZx2BtKV9kpyl44p-KXvSi8qXWBah1kVOqwkn9Ja7nfU0gI5NC0rHjktkSdd1MxJ2M5WHR4XrJtsEnHEwMEs-a74Oc6kstQJZzfzAkhqQCr44RpSf93B0MqfqJZ12IeJdH3bzZj8ww2HO6tChxXZbErnqXl2sbr3BoSNyr34Glc14hdGyL33tt-xw6Hmkcs5lw-Cnn-lav-L_0wIVvQ4tGmvOnzlCHX8zBb9Fo_5sKJpCIMoUrsg3FOvvw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/cc83c2d7b4.mp4?token=ofLQutWYocIOGQ1HcsJgl1v0xb0QIuqHghtKJx8x4vcWXfL86tUzpdYlF9d_SppVxj7wwZatawP_6Tk7GAqTm7-cDjrvsZx2BtKV9kpyl44p-KXvSi8qXWBah1kVOqwkn9Ja7nfU0gI5NC0rHjktkSdd1MxJ2M5WHR4XrJtsEnHEwMEs-a74Oc6kstQJZzfzAkhqQCr44RpSf93B0MqfqJZ12IeJdH3bzZj8ww2HO6tChxXZbErnqXl2sbr3BoSNyr34Glc14hdGyL33tt-xw6Hmkcs5lw-Cnn-lav-L_0wIVvQ4tGmvOnzlCHX8zBb9Fo_5sKJpCIMoUrsg3FOvvw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">فرماندهی جنوبی ایالات متحده فیلمی از عملیات شناورهای جنگی آمریکایی Saronic Corsair نیروی دریایی ایالات متحده در پایگاه دریایی گوانتانامو بی، کوبا منتشر کرده است.
@News_Hut</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/news_hut/72659" target="_blank">📅 12:11 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72658">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">ترامپ:
باید با چه کسی طرف شوم.
کسی نیست که بتونم باهاش درباره ایران تعامل کنم. هیچ‌کس نمیخواد رئیس‌جمهور بشه.
من می‌پرسم: «در ایران با چه کسی صحبت کنم؟» تق‌تق(در میزنم)...اما کسی خونه نیست.
@News_Hut</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/news_hut/72658" target="_blank">📅 11:47 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72657">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/news_hut/72657" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/news_hut/72657" target="_blank">📅 11:47 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72656">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/q6-hk9kqnac494h7rZ_igKR6EMxlgh1Exv5dJljPOX4aqp0NsmywfmqGVLVCnYPDrlzzceQ5nSqCoF0aQLqn4wHWCWAtTsienQjl0uU417UPUO7PV3rkRaL7KXDCqBaWwaPi3lraqVyzswkESBZUtkCI1IsphYAsL1mPMFxgibnLaiB6AJlAazKHdUFaBd6tNtofJnAeAgJPkQwuN6l-jMsqxiYLXXsOQDmOTcidvXyOSFIL98TyC4LJ9yIFCWQGnv9DyAOEGLiXMhrd3UtgevTqjykXnJ48mtPQa4BI3TsgOQzDEl1ID74qsHInfRtMSU-vTukwOXsS7v8PNRu28A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🦖
مچ‌های مهم امروز در سایت بین‌المللی
TrexBet
انگلیس
🆚
کرواسی
چک
🆚
اسپانیا
اسلوونی
🆚
سوئیس
لومتزانه
🆚
اینتر
یووه استابیا
🆚
لاتزیو
برزیل
🆚
هند
🦖
🦖
🦖
🦖
🦖
بونوس اولین واریز تا سقف ۱۰۰ یورو
🦖
بهترین ضرایب بین تمام سایت‌ها
🦖
واریز آسان و امن از طریق کارت به کارت
انتخابت رو انجام بده و آماده‌ی هیجان باش!
TREXBET — PLAY. PREDICT. WIN.
https://TrexBet.com
T.me/TrexBet_Ir</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/news_hut/72656" target="_blank">📅 11:47 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72655">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c533100ff9.mp4?token=WjRnHUgH4K4P0yukQvQXTb0_N91yQvdrAjJ5vnH21Yds3ADJgcfxUv46i76D8wcWFRtg-ghzswH7iqDk6JgJ4b6i2wuG0-LPxnve9bJw_J07tPDWNdrT2iIp2KSljiSFai1rNcc_RkZ4JJ-j_G7uRUEfUVu5-mZwoKhQFyL8XJ1SAojnM1OKbVAwKluLN9CW_apf8yEJsnojS-BPIbRfVvpH7_DxvCUCwjWMIfKrdptRVsO7Qa7B_oAV1uMPdk996EZK5ynYXtf0qso79aS8jCF6u7xCVurUSS62bLhNPFuQ-JjTxfJ1zfVctUGsllAUGzuxBTdyF7ZMOc2ZMUK9zg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c533100ff9.mp4?token=WjRnHUgH4K4P0yukQvQXTb0_N91yQvdrAjJ5vnH21Yds3ADJgcfxUv46i76D8wcWFRtg-ghzswH7iqDk6JgJ4b6i2wuG0-LPxnve9bJw_J07tPDWNdrT2iIp2KSljiSFai1rNcc_RkZ4JJ-j_G7uRUEfUVu5-mZwoKhQFyL8XJ1SAojnM1OKbVAwKluLN9CW_apf8yEJsnojS-BPIbRfVvpH7_DxvCUCwjWMIfKrdptRVsO7Qa7B_oAV1uMPdk996EZK5ynYXtf0qso79aS8jCF6u7xCVurUSS62bLhNPFuQ-JjTxfJ1zfVctUGsllAUGzuxBTdyF7ZMOc2ZMUK9zg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ:
گروهی از افراد را دیدم با عنوان «هم‌جنس‌گرایان حامی فلسطین». بیایید یک روز آن‌ها را برای مذاکره به آنجا بفرستیم.
دیگر هرگز آن‌ها را نخواهید دید. آنجا کارهایی با آنها می‌کنند که باورتان نمی‌شود
😂
@News_Hut</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/news_hut/72655" target="_blank">📅 11:26 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72654">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">اسامی نفرات برتر آزمون سراسری ۱۴۰۵  @News_Hut</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/news_hut/72654" target="_blank">📅 10:57 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72653">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hLM6BklISEcab15dvU8Gzmi0iQPen1ORsncBQNp-fpK9eA_43gU7vDgHKUIDNJpijoV15eQBOEcO06jIoJsfzqoomoUcFLp3XpLHd-0xYnN_uloc5hRDEcjjIeIbXUDBSyazVhpTJzFZJawPdnlKNxpxGET4S_kMSsN5EvhOG7iNjN2mDA_xcJrWC5iZWZhIADaAtTbRFPABhBoytm5nL-qDJzCvMODjxLvzEULjjDnU390udFeqa6Dz3tMgOCLmYU4z-MISoGAy1TvtUY4Ir3fADsEdar2Vr-IdY7d_FsGlL5sX0_2dPNjwX8281SQ8eoiLEozqyzTu5i4PbyqHvg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اسامی نفرات برتر آزمون سراسری ۱۴۰۵
@News_Hut</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/news_hut/72653" target="_blank">📅 10:53 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72652">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">نتایج کنکور سراسری برای عموم کنکوری ها فردا میاد!!
انتخاب رشته از دوشنبه ۱۳ مهر ماه تا ۱۶ مهر ماه ادامه خواهد داشت!
@News_Hut</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/news_hut/72652" target="_blank">📅 10:39 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72651">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vV9dgCWiUbOLPk0fPddZn0kJikAfOdN7xoQIvenViTsqkfxZm3C_X0AjRwx0dCx3EoYTZSMb8bEvFI9navLC_Opxz18mapCjkDWgbkRFgGfNzWpGWwxEKP1Yn74xzPzKWM8_mhkDrfIhJfU9QKvkQchOYzkqmZ-NE-ag3qDp9FqspqIUa3Wz20j0N0lzeFti9P0KVE7zWP9KIZ0je0KiO19uPE-4pZfvintMf7DPCG8y7A4f0pbJOwmXLai3cViePcsSZIyBGTzH6RaXrxk74eUo8J-ShKT38UAxrPwEil85QDq_JOkWShXBPYk0y_95TdVqm2Qg6MehquM0iZRvbQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نشست خبری سنجش تا دقایقی دیگر!
@News_Hut</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/news_hut/72651" target="_blank">📅 10:28 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72650">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/l52JGgqcO9vMjtHLSdws7PoBCi3IWA_VIqs0AOfM2ZYiBrOBPPoj5Kh7BdWOuD7IOTv7wkuXIX0-m6_uk_zxHFitwY8cX_HMtazljKmFH0CGcsh4SCc5zmHkV12N0oQSbf4dyj7LIdofJbuorlvuKBUhdD4HQhSja7CfUpupVh7nr-gXOAwPJjblpzG7YDWX0SvUkKVqNxFTt3Gg4Qis0g-7Qt_7v8qVOYsVQe_KUnAUr0hrZSsWFoaCNc59xcnHhE6YxW2lwAiKBwxTkCGZe6PWhz0WFzQ5PiH6bTqhoba0aoHBQXzI7r_K3Ckmtjvt8n9jPwUq1zEhHHAYLf2nyw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#مهم
؛ اکسیوس به نقل از سه مقام آمریکایی:
مقامات ارشد کابینه ایالات متحده در «کمپ دیوید» مریلند گرد هم آمدند تا درباره گام‌های بعدی در قبال ایران و انصارالله گفتگو کنند.
یک مقام آمریکایی اظهار داشت که در این جلسه تصمیماتی اتخاذ شد یا دست‌کم بحث‌های عمیقی پیرامون این موضوعات صورت گرفت.
ریاست این نشست بر عهده «جی. دی. ونس»، معاون رئیس‌جمهور بود.
«مارکو روبیو» (وزیر امور خارجه)، «پیت هگسث» (وزیر جنگ)، ژنرال «دن کین» (رئیس ستاد مشترک ارتش)، «جان رتکلیف» (رئیس سیا) و «استیو ویتکاف» (نماینده ویژه در امور خاورمیانه) نیز در این جلسه حضور داشتند.
آخرین باری که نشستی مشابه برگزار شد، به ژوئن ۲۰۲۵ و پیش از آغاز «جنگ دوازده‌روزه» توسط اسرائیل بازمی‌گردد.
@News_Hut</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/news_hut/72650" target="_blank">📅 10:07 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72649">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4f04d52dbe.mp4?token=DWhFkpc9TuVudTEfsLZ50tjF6ayJm-nPdLtV0KKUxcgCrRAvnLlCSUoXuSlnqoRf9AUZVkwVHNk3w5DBjkEnHIuQYsdLHr5kPXED4G3gKdlxR_yg7ZZsI3qZl3V7OvIfk6kN8I2Q8EzqNXMEvtnsLLEfImGe4dsRHg-tHsI7he2TxJoyGyyuTL_esdW7eYX0E4NaulNmWQxoY6lPJHx4jsX3efw3X99qIesjr5tyVqWp1dXfhkaT9dA-qbb9YjNkn1A2EKJzsokFUy8WiM0yfNEI3t_h4jtwVM4cyjSvVNQQxonIXec-VAAV3vyVEvBTvClvaTAnodgb24POlXuIaQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4f04d52dbe.mp4?token=DWhFkpc9TuVudTEfsLZ50tjF6ayJm-nPdLtV0KKUxcgCrRAvnLlCSUoXuSlnqoRf9AUZVkwVHNk3w5DBjkEnHIuQYsdLHr5kPXED4G3gKdlxR_yg7ZZsI3qZl3V7OvIfk6kN8I2Q8EzqNXMEvtnsLLEfImGe4dsRHg-tHsI7he2TxJoyGyyuTL_esdW7eYX0E4NaulNmWQxoY6lPJHx4jsX3efw3X99qIesjr5tyVqWp1dXfhkaT9dA-qbb9YjNkn1A2EKJzsokFUy8WiM0yfNEI3t_h4jtwVM4cyjSvVNQQxonIXec-VAAV3vyVEvBTvClvaTAnodgb24POlXuIaQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ربات‌های چینی با لباس‌های سنتی عربستان، برای شهردار ریاض و سفیر چین رقص محلی اجرا می‌کنند.
@News_Hut</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/news_hut/72649" target="_blank">📅 09:24 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72648">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LKuLmUmo-UaY5g-hILQ07g1RicI6nQWlYm-bw4WAatmqC_Bfq37CR80eGdhjEyxBVhtD810X4D5PtqyKzwu0mPmddQM1oIhz7L3P8gGWzPeAh3pF9AaeBjiGLiJdxhtGixdXRSBBFwN9tY3Z1OU5lY-1BO9Rau1rFgt6gQ7ZyrxE1U2u8L-A3dxJ7lOHcJaAIzmYAaOdmIEHCORjNQqo6ucllouFPGWTfur6EzM_fnbhPUGeBExYzC8EZ_RNRYRTXpS8YmZlK5A-I6dxfV35R9DWEIbJdaE5zHxlIc5MmQ4sCSUWJijnoaVab7PvQqeXbBvFkmo5FGyLn851Oyvfvw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">به گزارش «ای‌بی‌سی نیوز»، کمک‌خلبان شرکت «فلای‌دبی» که به خلبان حمله کرد و قصد داشت پرواز شماره ۱۰۷۳ این شرکت به مقصد اسرائیل را ساقط کند، «همام الحمامی»، تبعه ۲۹ ساله اهل عمان شناسایی شده است؛ او اذعان کرده که قصد داشته هواپیما را در اسرائیل سرنگون کند.
الحمامی در سال ۲۰۲۴، در دوران آموزش در شرکت «عمان‌ایر»، پس از کشف مطالب افراط‌گرایانه نزد وی، از پرواز تعلیق شده بود اما همچنان در سمتی اداری به همکاری با این شرکت هواپیمایی ادامه داد.
بازرسان در حال بررسی چگونگی صدور مجوز پرواز برای او در شرکت «فلای‌دبی» و تعیین وی برای مسیر پروازی اسرائیل هستند.
الحمامی با بازرسان در امارات متحده عربی همکاری می‌کند.
@News_Hut</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/news_hut/72648" target="_blank">📅 07:20 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72647">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tC6vw3mRqzpC4V5hhosXKEeGjLSRfZYDmQsT5tQkdwvA6-Ia8CgqB2CStGkUvgyxY1aBCDxDR2OMf4CWw-h71FG_LXN5vL48di6bN5GmrHnLFAbEjGx6FWp6vQkMtdkjOALCMsTsb3JsDTEhMhy6TtiVRkskcyxE3OPFQ7zcRIAx_yksGBWGKFfmd5bbIw5vO6h1yAaelVOFnss5RwUr71JEjFY45yYgAzkiS05qDm-zRQa5CRquxLA0RWb4jrE2RvopQFPvD1THfjY1cMnFAMjckEwZRc9sxVCqYCkYpvKEfabXeVKIY7bbp4_CIBKdMMoVNziMCEwv6i6JGWKXQw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرنگار: گام بعدی شما در قبال ایران چیست؟  ترامپ: خب، اگر به شما بگویم، خبر بزرگی برایتان می‌شود، مگر نه؟ اما خواهید دید؛ اوضاع دارد خیلی خوب پیش می‌رود. وضعیت ایران خوب نیست.  @News_Hut</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/news_hut/72647" target="_blank">📅 06:04 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72646">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/news_hut/72646" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/news_hut/72646" target="_blank">📅 01:38 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72645">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BvMfrXc7HIJy84Tik6EuotH_x9DJRYqj_kxN2CC0AjJDG-JJj7YwTFAEzCW2DC7-aWI4oUQkwHfdFNevnE2_V2O-Lwsa_1aWDwB1bNtC_Z65G7ACUieeDUGHNx1lAuYt2pcCrno1RR-YnPIe_DWHq66XKV-3gA4FZLliWaKkM0YHlIKursW0pGpx8xgf3Eudhn0laR5kjdXH-ig9HwHCzA_BOJwuaBSiURR6B_B-4t4qSzVz1kDRHTl2y6Wd_8sz4y5Y_WU8jJAVh6gLvL-OrpnflGRC066Fm91hgCFvN3PtbowtaaHRdzLJTsAefX1jBK29V0IYoAivbekXY4IgrQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🦖
شماره معکوس تا رویارویی بزرگ
​
🦖
دیوسون فیگاردو در مقابل پیتون تالبوت
🦖
تجربه اسطوره یا طوفان پدیده جوان؟
​هیجان واقعی و پیش‌بینی بالاترین ضریب‌ها در
TrexBet
!
🦖
🦖
🦖
🦖
🦖
بونوس اولین واریز تا سقف ۱۰۰ یورو
🦖
بهترین ضرایب بین تمام سایت‌ها
🦖
واریز آسان و امن از طریق کارت به کارت
TREXBET — PLAY. PREDICT. WIN.
https://TrexBet.com
T.me/TrexBet_Ir</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/news_hut/72645" target="_blank">📅 01:38 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72644">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b49a7f3128.mp4?token=c15f8iOf8LM0erx4egQP7WCCrapndw4yXhKcEXe4ZTCwVDNvuKHRP6xtMTG48lfimtxmctsrEp67dZ0iUOYia4yAY1_uVjbu9hVuhpOVW59yOXjbtQkHZj_VqoV4VOSLtg6qbHr9ClHrSrd0Ym22zX1O7MTIwzKmrISTXMQh14Maj-cp91JXVWs2mKX_jt_vtgAfIgEw_vivy7z69NLJAR7zCfNIVL-9FVcujR6Mnap-rReG13J2h4zINcICVrKnYLm1jEA-2R2gp5lBYyIsiGmilDiXbPvEFDihPIQk7YNS7K_Ly92AJQ5QzF5fs97y_4ZoT-g79wUnUAGdw8OpMA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b49a7f3128.mp4?token=c15f8iOf8LM0erx4egQP7WCCrapndw4yXhKcEXe4ZTCwVDNvuKHRP6xtMTG48lfimtxmctsrEp67dZ0iUOYia4yAY1_uVjbu9hVuhpOVW59yOXjbtQkHZj_VqoV4VOSLtg6qbHr9ClHrSrd0Ym22zX1O7MTIwzKmrISTXMQh14Maj-cp91JXVWs2mKX_jt_vtgAfIgEw_vivy7z69NLJAR7zCfNIVL-9FVcujR6Mnap-rReG13J2h4zINcICVrKnYLm1jEA-2R2gp5lBYyIsiGmilDiXbPvEFDihPIQk7YNS7K_Ly92AJQ5QzF5fs97y_4ZoT-g79wUnUAGdw8OpMA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خبرنگار: گام بعدی شما در قبال ایران چیست؟
ترامپ: خب، اگر به شما بگویم، خبر بزرگی برایتان می‌شود، مگر نه؟ اما خواهید دید؛
اوضاع دارد خیلی خوب پیش می‌رود. وضعیت ایران خوب نیست.
@News_Hut</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/news_hut/72644" target="_blank">📅 00:02 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72643">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">ساعاتی پس از معرفی رتبه‌های برتر، کارنامه داوطلبین برروی پنل شخصی هر داوطلب در سایت سنجش قرار خواهد گرفت.
@News_Hut</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/news_hut/72643" target="_blank">📅 23:27 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72642">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">طبق گفته حسن‌پور خبرنگار خبرگزاری فارس، فردا در نشست خبری رئیس سازمان سنجش رتبه‌های برتر کنکور ۱۴۰۵ معرفی خواهند شد.
@News_Hut</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/news_hut/72642" target="_blank">📅 23:21 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72641">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3d476b5a95.mp4?token=PXgZcnyxiQSRgSrMRYkcsA3jI6Lvr2iFpqFaeKtANIsvXLW0WfLLR7Jto8LMqGK9a_5Je3JgTnhNrWBhG-2Oz0I7iVjkbA93lf5rfDDhmtlhpulsfHOC7v4Z0on9bRdx3WW9RU_-2nPQ2nzVGcYIxbvM3r5Oo2U2d0UfWaxt9Vxc4ieXZ-vQkP6NJ2gX0LZyJSkeC-UgU_jXPXGryIHlNaPHieusMSwn2bvpLAGdJU7VctiI4f9hPYBblkaLkZDi_0oGoN5iuzF-HnprCYWIXPwg8SoZ2a28Zz6SMyLtZFo1PiLJJr5zv6kqhDNCei2KkwtU7C8VLtL71c2jaes23Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3d476b5a95.mp4?token=PXgZcnyxiQSRgSrMRYkcsA3jI6Lvr2iFpqFaeKtANIsvXLW0WfLLR7Jto8LMqGK9a_5Je3JgTnhNrWBhG-2Oz0I7iVjkbA93lf5rfDDhmtlhpulsfHOC7v4Z0on9bRdx3WW9RU_-2nPQ2nzVGcYIxbvM3r5Oo2U2d0UfWaxt9Vxc4ieXZ-vQkP6NJ2gX0LZyJSkeC-UgU_jXPXGryIHlNaPHieusMSwn2bvpLAGdJU7VctiI4f9hPYBblkaLkZDi_0oGoN5iuzF-HnprCYWIXPwg8SoZ2a28Zz6SMyLtZFo1PiLJJr5zv6kqhDNCei2KkwtU7C8VLtL71c2jaes23Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تصاویر گوگل‌ارث با مقایسه وضعیت در ماه‌های مه ۲۰۲۲ و ۲۰۲۶، ابعاد ویرانی در اطراف مدرسه «القادسیه» در رفح (واقع در نوار غزه) را نشان می‌دهند.
@News_Hut</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/news_hut/72641" target="_blank">📅 23:00 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72640">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/06f0ca8354.mp4?token=FWL42siEo2I262MnxvMHnGnUMWN03wVd9vYO8-0C_FzRqIKe41jIfvX5J90YbIlWpGJXpNXUFDq_VmpNfds1ZNAmUk8qs6butiLftaWM-Gg1DXub6IOIy8AacJHirFdfL2GJm0nW8bIGCpsiRvD6i0vfI11eL5IfXRwq2xblBvU0TiwTUoZnEiQKArkfynOEwynHfMcQ7A39XBr1K1V2M584kLISZWQsJJJ_jnY9XoQHRucwYKgK4jktX8z83KMeUbQwUr-sL0NP45k9u5Ah2zIYuk4RCJAwPFZLVvr5cVscHkj9pI2S7J5jmO6R5HE4ZdtnXTPksLuSDUAdgA6Tkw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/06f0ca8354.mp4?token=FWL42siEo2I262MnxvMHnGnUMWN03wVd9vYO8-0C_FzRqIKe41jIfvX5J90YbIlWpGJXpNXUFDq_VmpNfds1ZNAmUk8qs6butiLftaWM-Gg1DXub6IOIy8AacJHirFdfL2GJm0nW8bIGCpsiRvD6i0vfI11eL5IfXRwq2xblBvU0TiwTUoZnEiQKArkfynOEwynHfMcQ7A39XBr1K1V2M584kLISZWQsJJJ_jnY9XoQHRucwYKgK4jktX8z83KMeUbQwUr-sL0NP45k9u5Ah2zIYuk4RCJAwPFZLVvr5cVscHkj9pI2S7J5jmO6R5HE4ZdtnXTPksLuSDUAdgA6Tkw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">این خانم میخواسته بره مهمونی و لباس درست درمون نداشت؛
اومد تصمیم گرفت یکی گرون ترین لباس‌های آنلاین شاپ که بالای
۱۰ میلیون
بود رو سفارش داد.
حالا چیزی که به دستش رسیده :
میگه این چیه لامصب؛ من با این برم مهمونی میگن خرم سلطان اومده
@News_Hut</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/news_hut/72640" target="_blank">📅 22:15 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72639">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/62412d8d06.mp4?token=e-r8bggTmkZ3pm52xxkezNkjPn0mY8QJMEVgNGIbxf60-9jbXDixdxaGXtDavA77AA3Js5BOGP_mrZF_W8ZTWdBB-xiOlV2gjFDXP7m7DqcAMCTgZARmFulvfWF0e8JocQuCZP23WpwlqOQI2vOgvZ2ZnssByB2eX2pF9a5VtUJyif5VSqxewIOcuGm08BPvnfSnAfL8jm5O6knbCkPsTHYpKPk05UqH_sx3TN1rUf5DYE7grsebZXi_kwQ0KuZiuMvLW7GZlEBQitxQdkxS86naMQwQeXbHBjuAVzv4zfBQ_n5I2KcX14oJoZgGyWss_oX0ijNqfeRPLHL3VXr_8g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/62412d8d06.mp4?token=e-r8bggTmkZ3pm52xxkezNkjPn0mY8QJMEVgNGIbxf60-9jbXDixdxaGXtDavA77AA3Js5BOGP_mrZF_W8ZTWdBB-xiOlV2gjFDXP7m7DqcAMCTgZARmFulvfWF0e8JocQuCZP23WpwlqOQI2vOgvZ2ZnssByB2eX2pF9a5VtUJyif5VSqxewIOcuGm08BPvnfSnAfL8jm5O6knbCkPsTHYpKPk05UqH_sx3TN1rUf5DYE7grsebZXi_kwQ0KuZiuMvLW7GZlEBQitxQdkxS86naMQwQeXbHBjuAVzv4zfBQ_n5I2KcX14oJoZgGyWss_oX0ijNqfeRPLHL3VXr_8g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پسره سر صبح رفته گوشی داداش ۱۱ سالشو چک کنه که میره تو پیامکا و با همچین شاهکاری روبرو میشه:
@News_Hut</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/news_hut/72639" target="_blank">📅 21:33 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72638">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/uNJMUVyhBJuzH6wDOiz9amLH2uwxg-FzrhNXv0FC_JBI9vEPixRpXJ85PTI0ARtCt3KGMChO2NCdgfGWKx3xpUwR0BgmReLsS2Nnr4BhjZGMPkEjFHujFpg8YPoudGLhWIFgM_xZwckwr5QAh0SUxdZYWRT7jiee9fYX8T1P7STK-4kN33pm0S0jmz2227Jj6_5t1kllf6XEWpTraOGvd7ZOoHHzkX2YhBEE_j95W08DBOCZ8jt-9jaKh6kYV0r0iztjcjuf-uQA4kC7bDBW4xdxAh6M7VdejwqRRdJSfpY3zubY0b39n_T522BFQzvoEEC6PsyAm5JghtGRujW9pQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سازمان عملیات تجارت دریایی بریتانیا (UKMTO) اعلام کرد که ناخدای یک نفت‌کش گزارش داده است این شناور هنگام عبور از تنگه هرمز مورد اصابت یک پرتابه قرار گرفته است.
در پی این حادثه، آتش‌سوزی مختصری رخ داد و برق کشتی برای مدت کوتاهی قطع شد؛ با این حال، آتش خاموش شده و شناور به مسیر خود ادامه می‌دهد.
@News_Hut</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/news_hut/72638" target="_blank">📅 20:58 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72637">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">دلار 265
😑
#hjAly</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/news_hut/72637" target="_blank">📅 20:51 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72636">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">دلار 265
😑
#hjAly</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/news_hut/72636" target="_blank">📅 20:48 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72635">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dd07c4e807.mp4?token=R8MXJa2FX84Ti20IHmAPhZsp2ZDpd6--8SZ14cbT-5c46G1eDEIkBeMOtU7_7UHt1efQit1bnd-iwVA6znQ5KQSqyk9FGllD_jlfAdMY0XlzhbILkoCQ6N0knzY-0NKmmnVfosBTBM-UpVBuSSYIggntJY4KuiVMpGBc8yXtYkXrlF5M2BbEN2fGqQ3zWgqMSpeYER98wYnAPYD5xtrykr0Mcwty0Y8MN6uonX-CIExmQZf3BCe9vCXv25ZOjtohw49-xcDGRv0Lv2-yAEhT1KLVkO3IrxMdyZN6avbl4HkRUpUu9VmyRTBumojvevEmqvfb8D0j97k8Zjts-snPfA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dd07c4e807.mp4?token=R8MXJa2FX84Ti20IHmAPhZsp2ZDpd6--8SZ14cbT-5c46G1eDEIkBeMOtU7_7UHt1efQit1bnd-iwVA6znQ5KQSqyk9FGllD_jlfAdMY0XlzhbILkoCQ6N0knzY-0NKmmnVfosBTBM-UpVBuSSYIggntJY4KuiVMpGBc8yXtYkXrlF5M2BbEN2fGqQ3zWgqMSpeYER98wYnAPYD5xtrykr0Mcwty0Y8MN6uonX-CIExmQZf3BCe9vCXv25ZOjtohw49-xcDGRv0Lv2-yAEhT1KLVkO3IrxMdyZN6avbl4HkRUpUu9VmyRTBumojvevEmqvfb8D0j97k8Zjts-snPfA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">داداش تاییده خیالت جمع برو بگیرش.
@News_Hut</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/news_hut/72635" target="_blank">📅 20:32 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72634">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">شبکه سه اومد بازی جودکار ایرانو تو مسابقات آسیایی رو پخش کنه که جودکار ایرانی تو ثانیه اول بازیو باخت و حذف شد و گزارشگر اومد سلام کنه خداحافظی کرد
😂
😂
😂
@HutNewsPlus</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/news_hut/72634" target="_blank">📅 20:10 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72633">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">عراق اعلام کرد که مجوز معافیتی برای انجام روزانه ۴۰ پرواز توسط شرکت‌های هواپیمایی ایرانی (به‌جز هواپیمایی ماهان) به مقصد فرودگاه نجف و بالعکس دریافت کرده است.
هدف از این معافیت، تسهیل سفر مسافران و تأمین نیازهای بشردوستانه و پزشکی است.
نخست‌وزیر عراق از دولت آمریکا بابت موافقت با این معافیتِ درخواستی تشکر کرد.
@News_Hut
| Clash Report</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/news_hut/72633" target="_blank">📅 19:43 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72632">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2b2fb6f9cd.mp4?token=Cedfw9k-2cMBJEyxmhnsCEuJAfs5ALopCtTJjJufhCQE6CdDukcTC3XOsnQISOQgEWaVfhSX-803Ko9K3TuzUsgyLraAvDElAcgIOWj4LL0F4e_F2Q2UIhzXyc28b8CZ_DIcyKKLxu92THUw4vO10qvKXxcDUdllMWJQc8VQCviQqaOp8gMohB4sxjmJ5myKp2yCKUrH9ICbrYxtUiJngor8UdyBdcNX-MexrleslLYM9PIj4oV2abKqrFyGMC-WWssWlsPf5xdEbiSpuFFQu18u-guZQGb9KEgDq9XII0ZDBdFI1BqHVXc2qHpQiJHyI_Ein9YmdU4kzI8uLXy46GW7xRTnFViy-y-CE3V8xISjxiQ8dfobg0kXlRe250ae-4poaqRN6mM1NMpyH1hUoDT1SEyzV9AXaS6XFu7QyLVbnDtnKtUNxOeSniIZFTrgqWE3quQQlG50FCnmiA6rVds7SDwl_x3Wja8eGT6CUfF3wKZyfDrMUl6RUp8C96uowMDm3gc8hIymJOPvlb0C8UaGtD_HjdeS-X2NBVn-6SPmwPmfSOI6i7qhrTw5-BeVpDAAqdOd3wmtvnQrCPyN3InGW42cvzKDD8LSD5SSYMrYBCr6YTISnj3owNabJr_bz_GpxxWbs43ZwE2PMuhp8Wh8lEbf9wHT7TY2gOo2uP8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2b2fb6f9cd.mp4?token=Cedfw9k-2cMBJEyxmhnsCEuJAfs5ALopCtTJjJufhCQE6CdDukcTC3XOsnQISOQgEWaVfhSX-803Ko9K3TuzUsgyLraAvDElAcgIOWj4LL0F4e_F2Q2UIhzXyc28b8CZ_DIcyKKLxu92THUw4vO10qvKXxcDUdllMWJQc8VQCviQqaOp8gMohB4sxjmJ5myKp2yCKUrH9ICbrYxtUiJngor8UdyBdcNX-MexrleslLYM9PIj4oV2abKqrFyGMC-WWssWlsPf5xdEbiSpuFFQu18u-guZQGb9KEgDq9XII0ZDBdFI1BqHVXc2qHpQiJHyI_Ein9YmdU4kzI8uLXy46GW7xRTnFViy-y-CE3V8xISjxiQ8dfobg0kXlRe250ae-4poaqRN6mM1NMpyH1hUoDT1SEyzV9AXaS6XFu7QyLVbnDtnKtUNxOeSniIZFTrgqWE3quQQlG50FCnmiA6rVds7SDwl_x3Wja8eGT6CUfF3wKZyfDrMUl6RUp8C96uowMDm3gc8hIymJOPvlb0C8UaGtD_HjdeS-X2NBVn-6SPmwPmfSOI6i7qhrTw5-BeVpDAAqdOd3wmtvnQrCPyN3InGW42cvzKDD8LSD5SSYMrYBCr6YTISnj3owNabJr_bz_GpxxWbs43ZwE2PMuhp8Wh8lEbf9wHT7TY2gOo2uP8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تایوان نخستین محموله شامل دو فروند از ۶۶ فروند جنگنده جدید F-16V Block 70 را که در سال ۲۰۱۹ به ایالات متحده سفارش داده بود، تحویل گرفت؛ تحویلی که پس از ماه‌ها تأخیر — که تا حدی ناشی از مشکلات نرم‌افزاری بود — صورت گرفت.
این قرارداد ۸ میلیارد دلاری، شمار ناوگان جنگنده‌های F-16 تایوان را به بیش از ۲۰۰ فروند می‌رساند.
وزیر دفاع تایوان اعلام کرد که انتظار می‌رود پیش از پایان سال ۲۰۲۶، تعداد بیشتری از این جنگنده‌های F-16V تحویل داده شوند.
@News_Hut
| Reuters</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/news_hut/72632" target="_blank">📅 19:11 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72631">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/b7C_5W0SH0RmISH5DFcCZPZMWE-7A_sPePmgk8tFT4eEDh89rBL7GtgN383l7x6m8MpbojOVpiHNvhjKnEu9Ts7Iq_KpZW-xaS-0qhCO0sLJkAO7S_YQaKco0n9AQfRnLSPveHS3aFL2s2Db2UKVB4aGSpYvPEHkqqSp3-rSYShhhYxRGXsc4tPlLw1PmLCnw8yAGZywOc2kJD5rgKuozaIC18l2MVlteVfT5WBqpF4NJ6wo2lC7Kn_29pBDUn4JRPmBZFtd3kDDBwXDGhKdda2JEsnWXodBNcXaJy06Knb0Z8oyGwDvi3HjugvMYT483SVMc_eMNpr7Ub1SWUsqNA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">به گزارش «اکسیوس»، با وجود اینکه هم دولت ترامپ و هم تهران علناً اعلام کرده‌اند که خواهان پایان دیپلماتیک مناقشه هستند، دیپلماسی میان ایالات متحده و ایران همچنان در بن‌بست قرار دارد.
رویکرد دو طرف نسبت به مذاکرات، تفاوت‌های بنیادینی با یکدیگر دارد.
ترامپ خواهان دستیابی به توافقی سریع، پرسر و صدا و احتمالاً فراگیر است؛ در حالی که ایران مذاکرات طولانی‌مدت و غیرمستقیم با تمرکز بر ترتیبات محدودتر را ترجیح می‌دهد.
بی‌اعتمادی عمیق نیز بر پیچیدگی‌های این روند دیپلماتیک افزوده است.
@News_Hut</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/news_hut/72631" target="_blank">📅 18:26 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72630">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">ترامپ در تروث:
اروپا به‌تازگی موافقت کرده است که حجم عظیمی از ذخایر کلان گازوئیل خود را آزاد کند.
این فرایند بلافاصله آغاز خواهد شد.
@News_Hut</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/news_hut/72630" target="_blank">📅 17:39 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72629">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bd453b2fe8.mp4?token=XgbqOgQZHLP07i4g45xRAp_jNp0c9TsTXXEce7sprWDQA4RYRnpLvXk5XfY5LivBG4NH5NEyr5S-pMrqJPXOgdEZB_0nXNW0qxFK5mJ_mx7SDHkYiL92zotkMwyMeYtafxQQDIZguLIWaVI1IDA5xgxnbXvckLyIxmFwNaz5bKDFDHHWaE3ctA-16B5iyb1QXwT5k0b_msiZlLIuv-Q_i_iYBLlIzvt6qadST0zJ-uejKHGPsy4g4Ur1VDCmOyJjtgJ1ItitXsvsizAVMEp91cmlViG6ozw4qB2voMoDBTjx2OnthVmP6abTMKK-WWAmp4j-BgqpW7hS9EKj0_j5dw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bd453b2fe8.mp4?token=XgbqOgQZHLP07i4g45xRAp_jNp0c9TsTXXEce7sprWDQA4RYRnpLvXk5XfY5LivBG4NH5NEyr5S-pMrqJPXOgdEZB_0nXNW0qxFK5mJ_mx7SDHkYiL92zotkMwyMeYtafxQQDIZguLIWaVI1IDA5xgxnbXvckLyIxmFwNaz5bKDFDHHWaE3ctA-16B5iyb1QXwT5k0b_msiZlLIuv-Q_i_iYBLlIzvt6qadST0zJ-uejKHGPsy4g4Ur1VDCmOyJjtgJ1ItitXsvsizAVMEp91cmlViG6ozw4qB2voMoDBTjx2OnthVmP6abTMKK-WWAmp4j-BgqpW7hS9EKj0_j5dw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یه دختر لینک کلاس مجازیشو میده به دوس پسرش و پسره هم با دارودسته رفیقاش میپرن توی کلاس و همچین صحنه ای رو رقم میزنن؛
این وسط یه کاربر با نام عباس عراقچی هم دیده میشه:))
@News_Hut</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/news_hut/72629" target="_blank">📅 17:37 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72628">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/news_hut/72628" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/news_hut/72628" target="_blank">📅 17:37 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72627">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/H0Aodgw5KfTfkO7IBidSHlmVq_sSsB_Z6vn3nPsEmqM12p8bU-f95gXNYQn1RhUG3UCna6WnWkNcZNukNJ4Oo-QVMLdJV8V9OrbWlOiA5U0san6hQgxWFy4JP_dlOP_I0N2yWdSi303wCAA02vMkq3m8ye_z3vNoeI6pSoM1rQBMgRLE9vJRDpGXbLIrQG5BigT7r80bM3m0QIExI-eqgcCbww4vD10Ac-Co6jdcpbAYg0sfV78o25jhkiUyqEJh_RVoEayjjTgFrkJZvt71AtVTj8pRNUupSZF5IXb2woL-g4Nn4W7zNV1RySFJOAgZ7-xpUjlNdTLRI1e6e16OEA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🤩
نبرد هیجان انگیز ایتالیا
🆚
فرانسه
را در
TrexBet
پیش‌بینی کنید!
📉
نگاهی به آمار ۵ بازی اخیر دو تیم:
ایتالیا: ۳ برد، ۱ تساوی، ۱ شکست و ۷ گل زده
فرانسه: ۳ برد، ۲ شکست و ۸ گل زده
🦖
🦖
🦖
🦖
🦖
بونوس اولین واریز تا سقف ۱۰۰ یورو
🦖
بهترین ضرایب بین تمام سایت‌ها
🦖
واریز آسان و امن از طریق کارت به کارت
🦖
هیجان بازی، وقتی بیشتره که انتخابت حساب‌شده باشه!
TREXBET — PLAY. PREDICT. WIN.
https://TrexBet.com
T.me/TrexBet_Ir</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/news_hut/72627" target="_blank">📅 17:37 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72626">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/11e067ea31.mp4?token=kLbYjnBMmaHadLLnXyAuTOWs-uuLN46JuEqntifSXAwPy6cAMsTf7gWK0xHF98nLG5kj4i7R59HbZJoZRoMAYmtyWCJCXiT5UNIw9xYU_QQdzAXXrtVBMpI_CY52HbA0D8Xr3feHr8X4UVqOs2DdapAfQ16f3WKFK3NuzHIlTsQdWrkGh5vuG5Fmysp7WVEH2OyMInuxeVu70YGIhck2YCrduP1Q_D9Nq7LbQkf6k2J3WZy7dXnO4BGsOZUWxYqMkl73KU25UCCkbR_LA6tsvfsUAxHzMOPnDd8zpsgUUnidTdOS2JMWCNfCRdlKDkAgaWVN6EF-5kWq2cV0nnnqug" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/11e067ea31.mp4?token=kLbYjnBMmaHadLLnXyAuTOWs-uuLN46JuEqntifSXAwPy6cAMsTf7gWK0xHF98nLG5kj4i7R59HbZJoZRoMAYmtyWCJCXiT5UNIw9xYU_QQdzAXXrtVBMpI_CY52HbA0D8Xr3feHr8X4UVqOs2DdapAfQ16f3WKFK3NuzHIlTsQdWrkGh5vuG5Fmysp7WVEH2OyMInuxeVu70YGIhck2YCrduP1Q_D9Nq7LbQkf6k2J3WZy7dXnO4BGsOZUWxYqMkl73KU25UCCkbR_LA6tsvfsUAxHzMOPnDd8zpsgUUnidTdOS2JMWCNfCRdlKDkAgaWVN6EF-5kWq2cV0nnnqug" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">احمد مجدزاده: آقای پزشکیان این اخطار آخره، اگه استعفا ندی، استعفات میدیم.
@News_Hut</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/news_hut/72626" target="_blank">📅 17:03 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72625">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ad77de0b54.mp4?token=vQlKVh__eXdvlsH9VbfbCjpvaKhZQIn7feuHi8Qa58JaqEKDvA298RnwGmT1XpWw4m0qrhUtQQacuCrjMsZ-RMNJ_SBZTG5uN_c8s_VNeHqJ_F76xnTfWEmlf7FCJfBwPceWSIatS0lnVUqB-pTV3eaO5HCtEkiFSIXsiQJcMTxEaILKI3xuYzbiFou5mqURMj0y3uHpKScYQRvA2m8Y9DMv4kavx6jlTK5VlKSm4Zuew0QvcHIzUnMDGPuPN3pU1FGOKCKBLjscdE8odHYITXMNPLIOif-aIYcQ16n7mqxOlE8YjAjNVTwWovp-3RYg0Nn9s327GZuHUS9qFq1eiQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ad77de0b54.mp4?token=vQlKVh__eXdvlsH9VbfbCjpvaKhZQIn7feuHi8Qa58JaqEKDvA298RnwGmT1XpWw4m0qrhUtQQacuCrjMsZ-RMNJ_SBZTG5uN_c8s_VNeHqJ_F76xnTfWEmlf7FCJfBwPceWSIatS0lnVUqB-pTV3eaO5HCtEkiFSIXsiQJcMTxEaILKI3xuYzbiFou5mqURMj0y3uHpKScYQRvA2m8Y9DMv4kavx6jlTK5VlKSm4Zuew0QvcHIzUnMDGPuPN3pU1FGOKCKBLjscdE8odHYITXMNPLIOif-aIYcQ16n7mqxOlE8YjAjNVTwWovp-3RYg0Nn9s327GZuHUS9qFq1eiQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدیو وایرال شده از بانوان پولدار تهرانی که میرن توی یه سری کلاس ها شرکت میکنن پول میدن تا برن اونجا گریه کنن و تخلیه بشن.
یسری انقدر پولدارن که نمیدونن پولاشونو چیکار کنن.
@News_Hut</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/news_hut/72625" target="_blank">📅 16:30 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72624">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/aa3ebce38d.mp4?token=sH4J0DTTzgGLTF4RnZclj8PEHRR5aBPQ8gfEDBgUuQHCvWnYNkTFwhv0i94zRmSyfWiEDK1LfWVEIuR5eAmdNn5cOWYIKcErU-5Coj2bmVt5Dv94CZtLp-YWF1kWkPtyBpkgvK0BJmsoRTLo8Hhv5y95Hoq2WCVNnc92FrNoWABEGXyBdfp9mQZSx_XgfZMTm_Xw4qAe6AwvpdeL3unslPdAumFPBSW9yJzTuuageWTDQfEeRtG621zggZjQ-o6ozbV2C3K-1Nqx9RjxhRhiBMhzzz6V-6RHXTkHs0HhIWt_DkDbndo9gvRPEPz69QEVh6PBejEJkY3p-g_6Vz2z4Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aa3ebce38d.mp4?token=sH4J0DTTzgGLTF4RnZclj8PEHRR5aBPQ8gfEDBgUuQHCvWnYNkTFwhv0i94zRmSyfWiEDK1LfWVEIuR5eAmdNn5cOWYIKcErU-5Coj2bmVt5Dv94CZtLp-YWF1kWkPtyBpkgvK0BJmsoRTLo8Hhv5y95Hoq2WCVNnc92FrNoWABEGXyBdfp9mQZSx_XgfZMTm_Xw4qAe6AwvpdeL3unslPdAumFPBSW9yJzTuuageWTDQfEeRtG621zggZjQ-o6ozbV2C3K-1Nqx9RjxhRhiBMhzzz6V-6RHXTkHs0HhIWt_DkDbndo9gvRPEPz69QEVh6PBejEJkY3p-g_6Vz2z4Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دانش‌آموزان دبستانی در قزوین، در مقابل مدیر و ناظم مدرسه که آنها را با شلنگ تهدید می‌کند شعار می‌دهند؛
«این آخرین نبرده، پهلوی برمی‌گرده».
@News_Hut</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/news_hut/72624" target="_blank">📅 16:03 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72623">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0d885465ad.mp4?token=PK5syG83PyhTnBRNrZtbs_kJNnZ3ivM_a9PclBlsXQKmSy67uYuHycrnjDEde9HB9TtxsvLI_wdIBBo6YKqOyt4U1e1qWEYkHZeDtZsrkiMLWWt27khqMbdQhyrtCg_8eDRDU1VdviPTvk4NqLsCo18-ESOl5o1e-w-NZEuvbg8DY2G5LN3eR42fe29NvkjPISAcwQOIgZRWVQydFHNesmumTerfifCQGUTryXYM8zBmuYZSSlCH0VQ6mafLJ5ZqaPPewD6dWBJ71qtfm5VJYf1hYS5E9kMiY_J4G1-LgBSeL7HTHHcgxXApP7hQHEnFx2AjjNYKwaMJanshT6sJlA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0d885465ad.mp4?token=PK5syG83PyhTnBRNrZtbs_kJNnZ3ivM_a9PclBlsXQKmSy67uYuHycrnjDEde9HB9TtxsvLI_wdIBBo6YKqOyt4U1e1qWEYkHZeDtZsrkiMLWWt27khqMbdQhyrtCg_8eDRDU1VdviPTvk4NqLsCo18-ESOl5o1e-w-NZEuvbg8DY2G5LN3eR42fe29NvkjPISAcwQOIgZRWVQydFHNesmumTerfifCQGUTryXYM8zBmuYZSSlCH0VQ6mafLJ5ZqaPPewD6dWBJ71qtfm5VJYf1hYS5E9kMiY_J4G1-LgBSeL7HTHHcgxXApP7hQHEnFx2AjjNYKwaMJanshT6sJlA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یه دختر ۲۲ ساله تو تعویض روغنی با دوست پسرش در حال سکس بوده ژل روان کننده نداشتن بجاش از روغن ترمز استفاده کردن، روغن ترمز باعث خوردگی شدید پوست گوشت آلت تناسلی دوست پسرش شده و‌ بر اثر سوختگی درجه ۳ پسره فوت کرده، دختره ام بعد ۲۰ روز تو ICU بودن اومده پیش دکتر!
@News_Hut</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/news_hut/72623" target="_blank">📅 15:35 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72622">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kc7rTJh4rkjk5cFk-ICMxTA5_n2WwoOKkw_jhyWJN5s3Hl-QHWCP9Ew3i7GT6hmUPN6jtzUtn80nxmZPhfHMp-3UvozTPvZydJdo7b8DSlhcdNW_j_F0ff_qMbPpsn6pVgAMoqFCzkXkMid9iLAKjflc8P4EmQ60-5lnlSO4jAAXsS3Y5rhHynVpzJvU9YQuuDQhKxKZTDqG6Ni73BpwLNyLB8mS51DIQI34Z6fbdLOl_IjUo9i-CAavvxtT845m6wLxHR9ptvJseQcZvb8woBNo13GFenNrteNtQB2hHfvQekHe-R1CCnlTELUcIrYNEGF1rKcrZ8cBpkjZBqj6oA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کارشناس رژیم، علی قلهکی:
ماجرای «پروازِ فلای دبی» هم چاشنیِ اتفاقات آینده است!
@News_Hut</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/news_hut/72622" target="_blank">📅 14:59 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72621">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/d8bb7d42b5.mp4?token=J7OIshfjMNtkG_rP09xrMWHaYWbm2MZ3xnWvZ9JAuoHRrAh2G1mZQ296VrwT6nXUgoS7zP9hupwXkhrM1zq0RVVATeMGp22nuGBqcHeeLkeV4gmXY5sTg6RFxo3pUZS8Ws0uRKwnBEz6BpN6uav8QRD0FHwe1ewqXDqsNSHuxhMOmb1dpp5DpHit3d0_OeMTbaFrBbugHlFcHIRIH0CEynkizLMMKKVbPpL3zwPWmP99vkreVw_DLhximDisOCmZVNKOyb3IlaTbYKvKFJED_Wu54fX0_59Nkcwe7A7w4N82GmLzw1DoaDaFyyRu_dnF3DeRcczMZJM70E3fej_WMw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/d8bb7d42b5.mp4?token=J7OIshfjMNtkG_rP09xrMWHaYWbm2MZ3xnWvZ9JAuoHRrAh2G1mZQ296VrwT6nXUgoS7zP9hupwXkhrM1zq0RVVATeMGp22nuGBqcHeeLkeV4gmXY5sTg6RFxo3pUZS8Ws0uRKwnBEz6BpN6uav8QRD0FHwe1ewqXDqsNSHuxhMOmb1dpp5DpHit3d0_OeMTbaFrBbugHlFcHIRIH0CEynkizLMMKKVbPpL3zwPWmP99vkreVw_DLhximDisOCmZVNKOyb3IlaTbYKvKFJED_Wu54fX0_59Nkcwe7A7w4N82GmLzw1DoaDaFyyRu_dnF3DeRcczMZJM70E3fej_WMw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">این دو خانم محترم، آبروی ایران رو خریدن و باید سر تعظیم جلوشون فرود آورد!
یه توریست و بلاگر خارجی اومده بود ایران و با دوچرخه میخواست بره یه شهر دیگه.
دو تا خانم دیدن شبه و خطرناک و تاریکه، برای همین تا مقصد، دو ساعت تمام اسکورتش کردن!
حالا این بلاگر پستشو گذاشته اینستا و تمام دنیا به مردم ایران افتخار میکنن!
@News_Hut</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/news_hut/72621" target="_blank">📅 14:31 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72620">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b6c59bf1bb.mp4?token=AlRLRPySOtj4WeVZ4qp44Ps8h7hQuQZhKxeas2i3a7FioxzO2b7owFnhF1EWSshItp6O6mJLvFN6oEr1p2SQ-OQq1lbttKhxUy939OC6LgmHF0J99srvq4v0ybUy5nOad88IKUnMeVoaNWZ7arW1fL_qjJhPFCgqI8sQrpZJWpvL2E0LXWWcdvS0KYZ0cRXCIE1eUc5FefdIesq3pjCnSP1n-f6LPScuzeHGAQQsDjZhtAEONCC9X8mmCtytSynU1kXdDShi1ZbNr9tYZ5sEFHPW8swCI3IEn4NftDAzEfQhxqaznhFD_qygT1PK5jAX8FkwxgAijV3fdrY7GQhfsaZ3W6MYJ29fIggcDw1lxqma8TFQ7ZwLWIokxZj3p3yUQ-uLkIDKczL4zie_cEXjYtD_TSbTCQuC4xEOnMoI0jCfmep2uzNPPsl6gTLMI0Vii88ZwdN86hL-68eAYTNmZ0ANyPzEsWMzhO1VC1e5gbbsgng8Ppr1L0jwxf0Kho7AcHNabFoufJRsERKaXetVKEIX7xXc3aI8cakmiBQUfT1UCi3H5cmbqaQVc0TOg5PAI9YjabqQ4HaHeF5XJzz55eb86PPlBPfFM6ZczY11GBELvOHeCVJA0dcnasPeXc0sQ2KjwFjD4LZsXti1IfIdhzJFRUZcH12UnUviJNYpY7I" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b6c59bf1bb.mp4?token=AlRLRPySOtj4WeVZ4qp44Ps8h7hQuQZhKxeas2i3a7FioxzO2b7owFnhF1EWSshItp6O6mJLvFN6oEr1p2SQ-OQq1lbttKhxUy939OC6LgmHF0J99srvq4v0ybUy5nOad88IKUnMeVoaNWZ7arW1fL_qjJhPFCgqI8sQrpZJWpvL2E0LXWWcdvS0KYZ0cRXCIE1eUc5FefdIesq3pjCnSP1n-f6LPScuzeHGAQQsDjZhtAEONCC9X8mmCtytSynU1kXdDShi1ZbNr9tYZ5sEFHPW8swCI3IEn4NftDAzEfQhxqaznhFD_qygT1PK5jAX8FkwxgAijV3fdrY7GQhfsaZ3W6MYJ29fIggcDw1lxqma8TFQ7ZwLWIokxZj3p3yUQ-uLkIDKczL4zie_cEXjYtD_TSbTCQuC4xEOnMoI0jCfmep2uzNPPsl6gTLMI0Vii88ZwdN86hL-68eAYTNmZ0ANyPzEsWMzhO1VC1e5gbbsgng8Ppr1L0jwxf0Kho7AcHNabFoufJRsERKaXetVKEIX7xXc3aI8cakmiBQUfT1UCi3H5cmbqaQVc0TOg5PAI9YjabqQ4HaHeF5XJzz55eb86PPlBPfFM6ZczY11GBELvOHeCVJA0dcnasPeXc0sQ2KjwFjD4LZsXti1IfIdhzJFRUZcH12UnUviJNYpY7I" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ناو تهاجمی آبی‌ـخاکی USS Makin Island (LHD-8) یک یگان دریایی آبی‌ـخاکی آمریکاست که هسته اصلی آن ناو تهاجمی آبی‌ـخاکی USS Makin Island (LHD-8) است و در مأموریت فعلی، سیزدهمین واحد اعزامی تفنگداران دریایی (13th MEU) را نیز با خود حمل می‌کند.
این گروه از سه شناور تشکیل می‌شود:
USS Makin Island (LHD-8) — ناو تهاجمی آبی‌ـخاکی از کلاس Wasp
USS Anchorage (LPD-23) — کشتی انتقال و پهلوگیری آبی‌ـخاکی
USS John P. Murtha (LPD-26) — کشتی انتقال و پهلوگیری آبی‌ـخاکی
چیست(13th MEU)؟
13th Marine Expeditionary Unit
یا سیزدهمین واحد اعزامی تفنگداران دریایی آمریکا یک نیروی اعزامی تفنگداران دریایی است که برای عملیات و واکنش سریع در مأموریت‌های خارج از خاک آمریکا سازمان‌دهی شده است.
در کنار ناوهای ARG فعالیت می‌کند.
ترکیبی از نیروهای رزمی، پشتیبانی و عناصر هوایی
تجهیزات و هواگردهای همراه:
همراه با 13th MEU، هواگردهایی از جمله F-35B Lightning II، MV-22B Osprey و AH-1Z Viper را در اختیار دارد. F-35Bها متعلق به اسکادران VMFA-211 هستند و از ناو USS Makin Island عملیات می‌کنند.
این گروه تا پایان نوامبر به منطقه می‌رسد.
@News_Hut</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/news_hut/72620" target="_blank">📅 13:55 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72619">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d2a1a8f77f.mp4?token=plgr3y4kC4YspfhM7zsr6AF2-dr0YSHiU20V0rVnfpCRqJ0EH4i6ZaJS7q3RKOtQa-d62eFoCEAoY9_WwR-aHqo2TVPBB1gbWo0XPdI7sMPE5OTfRHNola9NNEi6OPNMhqs5sq6uDVfm1IQNUS2bK_jm-DnoA-KoPxf7PXDtKOXLUjLd2N2hGgkFzgamZXRXLCz9RC-1G9PCZYnQl16ptyTz-W_4amlsEbFeMt8R9cNjQN79ANkmzvBXVaAe0dY1ZM2KdvhdF5I4SeSc0sTQrLFYCk790Lw5omIScBc6ZVMn2w3KjKyPIzJvmDtXrf_z_bj-iqYrlyBX35H4oPF6Ha86VOyPrvG0KOWNmmy4JlpoeD6CiQXCJxTbIvKe4JjmkYU9cOmkX2F74KGkK1nnTnLYlJBfmGJKLhd3EXC70zaQgIXJuHtmSbf4JVd9ZIUkK4UUQqaGJJBcHmxqfZIDXId90jfvmOklSRkDj8MeAVj8hPricTz76rPCZ7Ks-_svmRlAYN3ZzwbUd4SeZENzyaHMYZOOOPbIf0adxw7AdHyNufR-9zW8-koVdEvbzkRpZJoAXpcIkqZ1ykvLQqVrYnlCZ1LDxJki8INdhGH0wIzFnFd79iFzdXx1kyLSefwMVqGL_fIvfmI7R0Gu8CNnXBjUnX6GY3QdLXyFuWJnHhI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d2a1a8f77f.mp4?token=plgr3y4kC4YspfhM7zsr6AF2-dr0YSHiU20V0rVnfpCRqJ0EH4i6ZaJS7q3RKOtQa-d62eFoCEAoY9_WwR-aHqo2TVPBB1gbWo0XPdI7sMPE5OTfRHNola9NNEi6OPNMhqs5sq6uDVfm1IQNUS2bK_jm-DnoA-KoPxf7PXDtKOXLUjLd2N2hGgkFzgamZXRXLCz9RC-1G9PCZYnQl16ptyTz-W_4amlsEbFeMt8R9cNjQN79ANkmzvBXVaAe0dY1ZM2KdvhdF5I4SeSc0sTQrLFYCk790Lw5omIScBc6ZVMn2w3KjKyPIzJvmDtXrf_z_bj-iqYrlyBX35H4oPF6Ha86VOyPrvG0KOWNmmy4JlpoeD6CiQXCJxTbIvKe4JjmkYU9cOmkX2F74KGkK1nnTnLYlJBfmGJKLhd3EXC70zaQgIXJuHtmSbf4JVd9ZIUkK4UUQqaGJJBcHmxqfZIDXId90jfvmOklSRkDj8MeAVj8hPricTz76rPCZ7Ks-_svmRlAYN3ZzwbUd4SeZENzyaHMYZOOOPbIf0adxw7AdHyNufR-9zW8-koVdEvbzkRpZJoAXpcIkqZ1ykvLQqVrYnlCZ1LDxJki8INdhGH0wIzFnFd79iFzdXx1kyLSefwMVqGL_fIvfmI7R0Gu8CNnXBjUnX6GY3QdLXyFuWJnHhI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">رئیس‌جمهور ترامپ درباره عملیات «چکش نیمه‌شب» (Midnight Hammer):
آن‌ها تمام بمب‌ها را فرو ریختند؛ بمب‌ها مستقیماً از طریق مجراهای هوایی به داخل این... خب، کارخانه‌های مواد مخدر فرستاده شدند؛ واقعاً کارشان همین بود.
هم بحث هسته‌ای در میان بود و هم مواد مخدر.
آن‌ها مشغول تولید مواد مخدر بودند.
به این کارخانه‌های مواد مخدر و تأسیسات هسته‌ای، ضربات بسیار سنگینی وارد شد.
@News_Hut</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/news_hut/72619" target="_blank">📅 12:43 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72618">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/vwf4WxdE22HgHnEe8XdDrSkaD8MI3734_HcZ2uHUsRlaZlTiPkYcCv09YPE_o7TCwTnT0aQClSCb3D7DuhLX-h4BzoX9Klr0dSkGEndu0qLiqx2gnggbuWgmRFayf5qNva4b8t52GH3LZZWTm-30mvYqLg0PLXI-aLfmuzqquwhqj1Li7UHvqko2j33Zekq4aBCzsiLQr9RGda5y9oVehFq3GeTMRDktcUbXAGHWURsmqXdwxEMb4ruqHCqy59olW6Qwh8GG8vHu_9ayeVcR2TfEHtu9B0yacgVzqzyLT-kqqA9OSFQ2X5ybwONmY1_3hPOyWKe0m2OwiKoC3zNzfw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#فوووووری
؛ آکسیوس به نقل از یک مقام آمریکایی گزارش داد که گروه آماده آبی‌ـخاکی «مکین آیلند» (Makin Island ARG) و سیزدهمین واحد اعزامی تفنگداران دریایی آمریکا (13th MEU)، پایگاه نیروی دریایی سن‌دیگو در کالیفرنیا را برای استقرار در غرب آسیا ترک کرده‌اند.
انتظار می‌رود این نیروها تا پایان نوامبر به منطقه برسند.
این گروه شامل سه ناو است:
ناو تهاجمی آبی‌_خاکیUSS Makin Islandاز کلاسWasp
ناو ترابری آبی‌_خاکیUSS Anchorageاز کلاسSan Antonio
ناو ترابری آبی‌_خاکیUSS John P. Murtha از کلاسSan Antonio
این گروه همچنین ۱۰ فروند جنگنده F-35B Lightning II و حدود ۲۲۰۰ تفنگدار دریایی آمریکا را به همراه خواهد داشت.
@News_Hut</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/news_hut/72618" target="_blank">📅 11:53 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72617">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/news_hut/72617" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/news_hut/72617" target="_blank">📅 11:52 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72616">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Kk9qizWyj9IKKFrETfp3kTFEFuEvUuy-KOJsmcfV5V6YoA3u4KJdpxADrUSH3d_FTDuRp-huxmwxEWdd1a0D55kMysaDrAbZHotRV9h3Rtfzoletku1DtV0y6DcPpC0l646PiQU6i7IHhmk74AmcEmgFW-kbJuvuN7hv5vzaufXaOVCoajScHH04pqpsLOJaD-aoHcqjokB_J0Ju4BgAZO4zZgHjuXLhIgNjI0bdBBSulGbMyJisbUvkjuQAXhmEw3DoWQ19UAio_yHmslMBBDnEVUYJWulhggP7gLQkclCMbLs4pl_EqaZruHU3-cYb8z0ijetSTkquK3j8Ei4YJg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🦖
مچ‌های مهم امروز در سایت بین المللی
TrexBet
ترکیه
🆚
بلژیک
ایتالیا
🆚
فرانسه
سوئد
🆚
بوسنی
نروژ
🆚
ولز
ونزوئلا
🆚
کره‌ی جنوبی
🦖
🦖
🦖
🦖
🦖
بونوس اولین واریز تا سقف ۱۰۰ یورو
🦖
بهترین ضرایب بین تمام سایت‌ها
🦖
واریز آسان و امن از طریق کارت به کارت
انتخابت رو انجام بده و آماده‌ی هیجان باش!
TREXBET — PLAY. PREDICT. WIN.
https://TrexBet.com
T.me/TrexBet_Ir</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/news_hut/72616" target="_blank">📅 11:52 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72615">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1127789805.mp4?token=BpfW_YUdVyhr2uEob0WPelTHAnFVJvvsWoAjSBAEM5ZRJK5b21gUprutdVNyYIjQKhlMqnOV1LzT_pdAnHT1pCtQsmxtXAZ5ULGn-UcgBgqWBNyelLmOhtayTQToc25rtkPcoYSMO6TYtQkw1TFnDQezaunuNbgt0bpfFDjjB6ZBsEf8WHSraf-UfpRe9OnHy1cJ_cxSnWiXT0MEoBGawSS_8gQG1lSAKbraaMdR3uv8v64T8Jj3ezpkSu5UiLRjRYsLDB-cAqIy8fkEGgDH5LAOiZ_Z30XhZM_2DC8JfmfnwyTwmBiXXVVQFsPX1L81gF6hlLVTWELvJBBy_rkKtA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1127789805.mp4?token=BpfW_YUdVyhr2uEob0WPelTHAnFVJvvsWoAjSBAEM5ZRJK5b21gUprutdVNyYIjQKhlMqnOV1LzT_pdAnHT1pCtQsmxtXAZ5ULGn-UcgBgqWBNyelLmOhtayTQToc25rtkPcoYSMO6TYtQkw1TFnDQezaunuNbgt0bpfFDjjB6ZBsEf8WHSraf-UfpRe9OnHy1cJ_cxSnWiXT0MEoBGawSS_8gQG1lSAKbraaMdR3uv8v64T8Jj3ezpkSu5UiLRjRYsLDB-cAqIy8fkEGgDH5LAOiZ_Z30XhZM_2DC8JfmfnwyTwmBiXXVVQFsPX1L81gF6hlLVTWELvJBBy_rkKtA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">توی هند یه میمون یهویی وارد مشروب فروشی شده و انقدر مشروب خورده که به این روز افتاده :
@News_Hut</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/news_hut/72615" target="_blank">📅 11:00 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72614">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gC8KSIa5F08F2UYHPdzd_p_Y6R_f1_RtLgxvbpuqbesyW3AyCTpzN0D509NjeIVvKTaw8EVYWF0w9IkPYYcHEZJ7YYF520QkZROxRFvlBNIovQ2K-8p8D84SL7X8ZeUKRqWF0Fr0pBVwXHo0oV8gonu3MdswVhT0kOdtPhZhZqvoQWT8taVI6oFMSPCmmFo1cQ9Sy4Lm8avAygBWl9BUc823WaY1XpspE8Z7mGVZVT_VqUcIiJhvf63vg2-Z9PS0_6wcbx_S4HtUI-lCyui7juJP11iBIVSgohLY3vPxCbuuCN4uVztLTkMBaxjm8HBjYi8EMLjeLl-Q9xSQpojsAQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بسنت، وزیر خزانه‌داری آمریکا:
ایران در ماه سپتامبر حتی یک بشکه نفت خام هم روی نفتکش‌ها بارگیری نکرده.
دولت ترامپ در حال قطع کردن مهم‌ترین منبع درآمد حکومت ایرانه.
عملیات «طرد اقتصادی» در حال قطع کردن شریان‌های اقتصادی‌ایه که به تهران اجازه داده برنامه‌های تروریستی خودش رو تأمین مالی کنه.
@News_Hut</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/news_hut/72614" target="_blank">📅 10:31 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72613">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5c00080542.mp4?token=GjU3nBscD34YQVOOWCafXqIh1n71vYiaLpFt4TqOFa2C2mfoh0IvAiBdrQQV4ayYtvL-Ipn9i3oL0gHMcbBpBUI96DQWS1Kv4nx4gmUKzRbvVhh6xCG9zZJma0WDkEw1LgCbEMIKhYiHlTdt4FImO6k4NohnxcmrxIUjy1UAuQC9HURxoQPnUAm61ajExr8SpL4M70ejj02UJqJbu35auC-yPLel5dazSawMfaGBKs2kefUYpRn6j7TTgPcYON1dOp7CoMGRiNryghgme6-GXwnIQoX9NLDO5aRi2_5ZxnRYAy7xD1Dq7MgRTJ0ZCaakwaVyi5L9UqPdy0tPRMpg8Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5c00080542.mp4?token=GjU3nBscD34YQVOOWCafXqIh1n71vYiaLpFt4TqOFa2C2mfoh0IvAiBdrQQV4ayYtvL-Ipn9i3oL0gHMcbBpBUI96DQWS1Kv4nx4gmUKzRbvVhh6xCG9zZJma0WDkEw1LgCbEMIKhYiHlTdt4FImO6k4NohnxcmrxIUjy1UAuQC9HURxoQPnUAm61ajExr8SpL4M70ejj02UJqJbu35auC-yPLel5dazSawMfaGBKs2kefUYpRn6j7TTgPcYON1dOp7CoMGRiNryghgme6-GXwnIQoX9NLDO5aRi2_5ZxnRYAy7xD1Dq7MgRTJ0ZCaakwaVyi5L9UqPdy0tPRMpg8Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یک اخوند در تجمعات شبانه: دو شب پیش رهبری نیم ساعت در تجمع شبانه حضور داشتند.
@News_Hut</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/news_hut/72613" target="_blank">📅 09:58 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72611">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/a16936d012.mp4?token=V-Lcrc_l_t5DyIRToWESh4zy4ZUzuBSw6U0cSJ5hb8EFY_v2zmHPSwj-0x9dbTyp21VBl5yrDzcOoGumIthwgeqrO0sSHm38ec3YVyrpUfveigiE5qoLidRpylEP2pbkiuUx1svNw3876cfO1oN32F4TQyL92SuwwHMXHCYoLzNWONovXoJw0SFLUDu6FyAHbziF6XP2ijuPICQl0kEMT7J5YjdslbBOO_54Mp6LVSQM6CwKDpclWmvFPfpDHhP4yZsgGaZ-DnJ-wxt2wbxlMigBcvbdcu43yIE71HqaUWnuWfXxh3kHJFgKD_D6h7i-7APXBYCmaRHLQ9cswF8qtQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/a16936d012.mp4?token=V-Lcrc_l_t5DyIRToWESh4zy4ZUzuBSw6U0cSJ5hb8EFY_v2zmHPSwj-0x9dbTyp21VBl5yrDzcOoGumIthwgeqrO0sSHm38ec3YVyrpUfveigiE5qoLidRpylEP2pbkiuUx1svNw3876cfO1oN32F4TQyL92SuwwHMXHCYoLzNWONovXoJw0SFLUDu6FyAHbziF6XP2ijuPICQl0kEMT7J5YjdslbBOO_54Mp6LVSQM6CwKDpclWmvFPfpDHhP4yZsgGaZ-DnJ-wxt2wbxlMigBcvbdcu43yIE71HqaUWnuWfXxh3kHJFgKD_D6h7i-7APXBYCmaRHLQ9cswF8qtQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">به تازگی توی مملکت یه سری مهمونی میگیرن که توش با تم و استایل دهه هشتادی شرکت میکنن :))
@News_Hut</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/news_hut/72611" target="_blank">📅 09:31 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72610">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QMxEEPMdlwp-DVNy3wJ-xhWnRaThIRMB9wsmZ2wImyoJCmdxmUb0zin79b2QY7aRZyV1jxiQagNvu1juW052mxu_CDhnYR3_GeEYhfF5n_tJ5Dp1xvspJPM5diKehPItR9z2dSC1jHR93AmIG027jys-SPGWZa5Ifc3b-w0oR2vTcQ6RA5ochk6lf9__03J5hoJfuD0rbKkdjy6ktQHyIeCxsEZdigZSNN3zd9MwQLj6i1NqFYGMQ5WJ9B7QwaF05vQzimkVkJxOS-FUU7ejFIV01ua_nGfwLUptccuzenUeXbU7030WUpCKBd8oN1EHEaSwESJzNWWOK1AsOH0nlQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزارت خزانه‌داری ایالات متحده با اعمال تحریم‌های جدید علیه بخش‌های خودروسازی، ریلی، تولیدی و فولاد ایران، دامنه «عملیات طرد اقتصادی» (Operation Economic Outcast) را گسترش داد؛ بخش‌هایی که به گفته واشنگتن، با کاهش درآمدهای نفتی ایران در پی محاصره دریایی آمریکا، اهمیت فزاینده‌ای یافته‌اند.
وزارت خزانه‌داری مجوزهای جدیدی برای اعمال تحریم‌های بخشی علیه صنایع خودروسازی و ریلی ایران صادر کرد و شرکت‌های بزرگ خودروسازی از جمله «ایران‌خودرو»، «سایپا»، «ایران‌خودرو دیزل»، «پارس‌خودرو»، «زامیاد» و دو شرکت «نیرو موتور» را در فهرست تحریم‌ها قرار داد.
همچنین تأمین‌کنندگان خارجی در اندونزی، امارات متحده عربی، ترکیه و هنگ‌کنگ به اتهام تأمین قطعات خودرو برای تولیدکنندگان ایرانی و کمک به حفظ شبکه‌های تدارکاتی بین‌المللی آن‌ها، تحریم شدند.
@News_Hut</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/news_hut/72610" target="_blank">📅 09:03 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72609">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/news_hut/72609" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/news_hut/72609" target="_blank">📅 01:59 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72608">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZH4hgDzn0FFEsRp5sgmYHQDeIGSC6pFUxV7ohhZPpGe3x7HxQI0S8dO2wSbFgNYwtTZPgILazsxBcJxZaTFh8A8x3K95CrbHk_ZG-FZT3rNLBJsv-pveiaEL8kymHhWtKOa0WeH9COx4SIvR6zKBDIvh6C0Hv4gYl-oMgOc4n89X4bVDStKG_Yw5tt_CvtfI2x3ubPjNWPQLSW9S4nntCS5BTJXLOwtohdu4wV7ALYwHE1AQyof90_OagmL-_WgZ74miPJkvvVgSlNcMkTceCrr2lECR6b8Vh4ITBEsEHMghaZAusk1zmDjeDAXMiyZ-Wo7m5M7iP1DSTM2y8qSL8w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🦖
فقط یک بازی از میکس‌ت لوز شده؟
پولت برمی‌گرده!
میکس می‌بندی، هیجان بالا میره، اما یکی از انتخاب‌هات خراب می‌شه؟
با پیشنهاد ویژه
TrexBet
، در صورت رعایت شرایط، می‌تونی
۱۰۰٪ مبلغ شرطت رو پس بگیری
.
🦖
قوانین رو در سایت مطالعه کنید
🦖
🦖
🦖
🦖
🦖
بونوس صدرصدی اولین واریز
🦖
واریز آسان، برداشت سریع
🦖
سرعت بالا، طراحی حرفه ای و تجربه ای متفاوت
TREXBET — PLAY. PREDICT. WIN.
https://TrexBet.com
T.me/TrexBet_Ir</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/news_hut/72608" target="_blank">📅 01:59 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72607">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5821a90294.mp4?token=LWiyLR8eq8NxqIjPRFE-6XyYnGC4oF6PAh6PJb3-KZIlwkn2y5plEbz7-VVOI-1BdKt7By_4X_ofZ6oPDwSTKlfwsqarf-N-G5d9mGih9g75Qd2zaamJ5yHQ2GqncwJGoTMJyRfsGib5SjeQwPLSK0hk_LgrHOyMSRHaKAPSkr9kxHZASkfsroNyrntu73AJ8llHFE8FtLdCCEDtQ5bg_c_KgWCADNKagV-kgcdG_KWe9Ll7VFhtu0oO80XZWb9EIGMI-47vXgBlFe6jbEht9majk3bcnc16bS96SmvddqcmD3wq8h4FV7yXRn38rz2CTRriRMHa_3JbG2IFvlCVsQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5821a90294.mp4?token=LWiyLR8eq8NxqIjPRFE-6XyYnGC4oF6PAh6PJb3-KZIlwkn2y5plEbz7-VVOI-1BdKt7By_4X_ofZ6oPDwSTKlfwsqarf-N-G5d9mGih9g75Qd2zaamJ5yHQ2GqncwJGoTMJyRfsGib5SjeQwPLSK0hk_LgrHOyMSRHaKAPSkr9kxHZASkfsroNyrntu73AJ8llHFE8FtLdCCEDtQ5bg_c_KgWCADNKagV-kgcdG_KWe9Ll7VFhtu0oO80XZWb9EIGMI-47vXgBlFe6jbEht9majk3bcnc16bS96SmvddqcmD3wq8h4FV7yXRn38rz2CTRriRMHa_3JbG2IFvlCVsQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">#فوری
؛ترامپ درباره ایران:
یا کار بسیار درست و هوشمندانه‌ای انجام می‌دهند، یا عمرشان چندان طولانی نخواهد بود.
وقتی با آن‌ها توافق می‌کنید، بسیار محتمل است که به آن پایبند نمانند.
@News_Hut</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/news_hut/72607" target="_blank">📅 01:47 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72606">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dd837a9d25.mp4?token=fJyrifdKyOF6CkIm9UOKvQTuoxvbdMl4aVy7J2TuIyLTxAlEAFAIMaa8HfQ3VXRzeRKQz8hPDe6XcaKQui-Nz2ipUb3775pG2D6Gz2dz7GCfcB16Hi5Cg4hMPoR0JWKWED45TsxKE8hBoO7BeF10sgSOakbuHvieqCP_eB2QcAVgEYduo3c_YmJ18frpx5HwO31x0egK3jOp0Q_P4Ah0qwy4klnCs-f2OOAdxwcEpXvrOobX5BcrUprhbjEPM-IvrcTIbaaCG4jEASmrS9MqoVLL0m1Aj2egHzbXgz3gV2W1NHhBrZQtCtqPIPIWrPghzb7UDCZW3RqOOjridMl83w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dd837a9d25.mp4?token=fJyrifdKyOF6CkIm9UOKvQTuoxvbdMl4aVy7J2TuIyLTxAlEAFAIMaa8HfQ3VXRzeRKQz8hPDe6XcaKQui-Nz2ipUb3775pG2D6Gz2dz7GCfcB16Hi5Cg4hMPoR0JWKWED45TsxKE8hBoO7BeF10sgSOakbuHvieqCP_eB2QcAVgEYduo3c_YmJ18frpx5HwO31x0egK3jOp0Q_P4Ah0qwy4klnCs-f2OOAdxwcEpXvrOobX5BcrUprhbjEPM-IvrcTIbaaCG4jEASmrS9MqoVLL0m1Aj2egHzbXgz3gV2W1NHhBrZQtCtqPIPIWrPghzb7UDCZW3RqOOjridMl83w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ درباره ایران:
ایران در فوریه ۲۰۲۶، تنها سه تا چهار هفته با دستیابی به سلاح هسته‌ای فاصله داشت؛ شاید هم زودتر.
@News_Hut</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/news_hut/72606" target="_blank">📅 01:43 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72605">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/69424629e7.mp4?token=IKm7bckr6RDX0h37-q2Mxqy7o5c96SLNY1_2gtUYGzBIbz3kB4TuybSIrQ43oIaLcZyEHEzK7dPPMKaRSRULy4fuH1SMe0QPcCdojwXfZWi8cM9_AxuBYObZcydKYqukTn_B7rShDJfwVmApgIqIgTUP-Jn4mbOCsp2QC2ZKTNjwpHsviRH9QmvHgI1Ia4ET7e1Zi5Xs4IUPH6GBvPYJopYjvnAqEVWhVBy1seLAl3Z6kdofbFqiuVua1HDrTFvt60svZA1U3IyGfO3F6ClnSrziJeohUPeDJPv84iYRfSsmIdHvscpqwBCoQ04Hw6TNXJ6C1mmc4x_zs_AYChr5Tw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/69424629e7.mp4?token=IKm7bckr6RDX0h37-q2Mxqy7o5c96SLNY1_2gtUYGzBIbz3kB4TuybSIrQ43oIaLcZyEHEzK7dPPMKaRSRULy4fuH1SMe0QPcCdojwXfZWi8cM9_AxuBYObZcydKYqukTn_B7rShDJfwVmApgIqIgTUP-Jn4mbOCsp2QC2ZKTNjwpHsviRH9QmvHgI1Ia4ET7e1Zi5Xs4IUPH6GBvPYJopYjvnAqEVWhVBy1seLAl3Z6kdofbFqiuVua1HDrTFvt60svZA1U3IyGfO3F6ClnSrziJeohUPeDJPv84iYRfSsmIdHvscpqwBCoQ04Hw6TNXJ6C1mmc4x_zs_AYChr5Tw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ درباره ونزوئلا:
ونزوئلا تماماً تجهیزات روسی و چینی داشت. ما همه آن مزخرفات را از کار انداختیم؛ آن‌ها کار نمی‌کردند.
@News_Hut</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/news_hut/72605" target="_blank">📅 01:42 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72604">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7d2bdd7600.mp4?token=RMmNiniy2zq3iq22KXAkceokpHT8JoAR8mR6JjM9fbnEmYzd8Mek_-j7qNjS3XAVmLw3CkNyN5K6_STdv947q7Yhy-LwtqWUv4itp69_AnKIh2T5Cza15JjfLc8Eobd0HQzimBsBiMaviy6lBhZ3n9BHwbNBsM39RO-j6K888U2NHNAhH_2E8f50aY25QV2XdamaXmZNncf9tL2iWW8dlEfTC9r907n8oBqXVHwQz0MCR9fmto2EQVOjsyXQdSWGwdj86hAWzltHmGIqM8YNy2vJjYbroFTkf4PvcpooxjYEbW_ZuxRt0SmYT2EsLK5vDaZTypX-TzHLeklIwU7ADg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7d2bdd7600.mp4?token=RMmNiniy2zq3iq22KXAkceokpHT8JoAR8mR6JjM9fbnEmYzd8Mek_-j7qNjS3XAVmLw3CkNyN5K6_STdv947q7Yhy-LwtqWUv4itp69_AnKIh2T5Cza15JjfLc8Eobd0HQzimBsBiMaviy6lBhZ3n9BHwbNBsM39RO-j6K888U2NHNAhH_2E8f50aY25QV2XdamaXmZNncf9tL2iWW8dlEfTC9r907n8oBqXVHwQz0MCR9fmto2EQVOjsyXQdSWGwdj86hAWzltHmGIqM8YNy2vJjYbroFTkf4PvcpooxjYEbW_ZuxRt0SmYT2EsLK5vDaZTypX-TzHLeklIwU7ADg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ درباره ایران:
رؤسای جمهور [پیشین] ایران دیگر با ما نیستند، اما سعی داریم با فرد فعلی خوش‌رفتار باشیم.
بالاخره باید با کسی کنار بیاییم، مگر نه
😂
@News_Hut</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/news_hut/72604" target="_blank">📅 01:39 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72603">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">ترامپ درباره ایران: ایران آماده تسلیم شدن است. ما همین حالا خیلی راحت پیروز خواهیم شد.
@News_Hut</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/news_hut/72603" target="_blank">📅 01:37 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72601">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9371c09764.mp4?token=aDPD-q4MDGp39EFwRYzixqp1Ue6xd_5UqKgMeRerTDlWPWlCpxYtOjraqekODoCCYACu2mypqJWNFRmWYUxcyqGFEhlkfbDH7Fj-_gSOKWNVSxl3iWA7nPStxXYHaa_oFA780fIPYSn3f6LfaaepS7FTlkkMgZ9lsxwBeMt01cI0enhXh73rrzdaSJQHkd01QAaEHBid8WpF44ksDkU-eSsCfxnH4GUNdFK5waUlPaqfoilEvJq1sEGNmpwnrRjJm4E9qgURvwB0Pxri46_fmAfK94axWxsMvscNdQJryKFg1HLQj5ANdZKlYYy3bpIRLqaYeQIUI_57r2_LvprdIw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9371c09764.mp4?token=aDPD-q4MDGp39EFwRYzixqp1Ue6xd_5UqKgMeRerTDlWPWlCpxYtOjraqekODoCCYACu2mypqJWNFRmWYUxcyqGFEhlkfbDH7Fj-_gSOKWNVSxl3iWA7nPStxXYHaa_oFA780fIPYSn3f6LfaaepS7FTlkkMgZ9lsxwBeMt01cI0enhXh73rrzdaSJQHkd01QAaEHBid8WpF44ksDkU-eSsCfxnH4GUNdFK5waUlPaqfoilEvJq1sEGNmpwnrRjJm4E9qgURvwB0Pxri46_fmAfK94axWxsMvscNdQJryKFg1HLQj5ANdZKlYYy3bpIRLqaYeQIUI_57r2_LvprdIw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">#فوری
؛مامور های عربستان یه شخصی رو که قصد انجام عملیات انتحاری داشت در مسجدالحرام (خانه خدا)دستگیر کردن:
@News_Hut</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/news_hut/72601" target="_blank">📅 00:51 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72600">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c38d02b25b.mp4?token=Bo8YDbZoy41-SCQgQulDvSLwXdRR8KeC9vpd-uIbBXUnBy4fy244ihtFtP3qZUsfoHNxZy8u8BYqAlYQf5aBLG2HzCnGC1Nb4GiNLSvKjWZugcyDDueFWdTInQMCd8rj20BgoGMdWISO4cXZ73-TrD2uJAIo9h9cOF4nMh7_vcWx2jvxNTk2q6pAwsqsygn6nDTK9B3lECim8LDgdV0Ah4di7lhOuUByCjW1N53-5TTC4o8UK8RJDagULfNH4sm5FupdXTQVoZszdb-XLlQAnEEskNo7_ZjxWtmesg1NeT-OvS63pVt3HS_RJAfiSEMOu6mKfyG4RLMhzDFHzTVdZA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c38d02b25b.mp4?token=Bo8YDbZoy41-SCQgQulDvSLwXdRR8KeC9vpd-uIbBXUnBy4fy244ihtFtP3qZUsfoHNxZy8u8BYqAlYQf5aBLG2HzCnGC1Nb4GiNLSvKjWZugcyDDueFWdTInQMCd8rj20BgoGMdWISO4cXZ73-TrD2uJAIo9h9cOF4nMh7_vcWx2jvxNTk2q6pAwsqsygn6nDTK9B3lECim8LDgdV0Ah4di7lhOuUByCjW1N53-5TTC4o8UK8RJDagULfNH4sm5FupdXTQVoZszdb-XLlQAnEEskNo7_ZjxWtmesg1NeT-OvS63pVt3HS_RJAfiSEMOu6mKfyG4RLMhzDFHzTVdZA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سؤال: آیا ایران در حادثه «آر.ای.اف فیرفورد» (RAF Fairford) نقش داشت؟
ترامپ: بله، ظاهراً همین‌طور است.
@News_Hut</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/news_hut/72600" target="_blank">📅 00:15 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72599">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/j6kjPr5eJdS_CBCfRzK05TVu7MHP0iqJNpGB9wdZYygVF2ooJ4ymNW1GhSMI0nfEDvw_j6DAZ6Sbli3uppukUZAH6DZaPEx6Qytz4TZkcibNrK8JEsGX6b5JFXCmeP-Iz-5AkXB8tb8momudCsjBhuEnk3T-HD2z_ZxPt9xXWMEsfkqk3Sasbn3zKaT9-fjZfjhaer0mtqqWVjs2b1x_9F0POMnR5QFMGOK3i7l9wMRQEsbrfGxxSpnMPqhVUP4Xe8Oqb2d03YhS9jGf-tJz3BA-4IG5_qT2cWoSeVbYObiIFO8sHrUxH4NGKIjavklG9QGtZB3gg2pjZFDz5MRZTw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">به گزارش وال استریت ژورنال، ده‌ها نفتکش ایرانی و مرتبط با ایران در آب‌های آسیا سرگردان مانده‌اند، زیرا ایالات متحده فشار بر کشورها و شرکت‌هایی را که به کشتی‌های درگیر در تجارت نفت تحریم‌شده ایران خدمات می‌دهند، تشدید کرده است.
حدود ۲۰ نفتکش خالی ایرانی تنها در سریلانکا سرگردان هستند و برخی از خدمه با کمبود غذا، سوخت و آب شیرین مواجه هستند.
از زمان اعمال مجدد محاصره تنگه هرمز توسط ایالات متحده در ماه ژوئیه، کشتی‌های دیگری در نزدیکی مالزی، هند و چین سرگردان شده‌اند و از بازگشت بسیاری از کشتی‌ها به ایران جلوگیری کرده‌اند.
واشنگتن همچنین به سریلانکا فشار آورده است تا از تأمین کشتی‌های تحریم‌شده توسط شرکت‌های محلی جلوگیری کند و به آنها در مورد تحریم‌های ثانویه هشدار داده است. فشارهای مشابه و افزایش اقدامات تنبیهی در سایر نقاط آسیا، بنادر و شرکت‌های دریایی را به طور فزاینده‌ای نسبت به خدمات‌رسانی به کشتی‌های ایرانی بی‌میل کرده است.
@News_Hut</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/news_hut/72599" target="_blank">📅 23:51 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72598">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4bce71f4cf.mp4?token=VRdwNjB1UW8bW3VLs6FfQI4PCoHkGKBPGLNlHDIsbixNscsG6Iup45aS7l-9GwBCz5vZ9K_5pJbjei9FGhX2-eFyk0mDdVgJOIBsK9zz1hc6S5f7MD3RaYAlLVQm65Y9xqUd9uEHulYkCWSDkn80-Vv7-2fR5DsGAyP9t-jTBwsIFv2jJVz6v_7a4iuUwftF2OV0UvoAMCNsY7d2zCsTBNg5XFVjnAAdLNUtgeI3cIUJhtzz3pKW7ZNmwLPachnuH23CmtvK6rn0fLwp7JGul-n9080mHQaOmDtv5jElWh9oFJ7OY5LA1tCdjkRnUgRyz9qlvjEN1Vnu-fPHaTiztA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4bce71f4cf.mp4?token=VRdwNjB1UW8bW3VLs6FfQI4PCoHkGKBPGLNlHDIsbixNscsG6Iup45aS7l-9GwBCz5vZ9K_5pJbjei9FGhX2-eFyk0mDdVgJOIBsK9zz1hc6S5f7MD3RaYAlLVQm65Y9xqUd9uEHulYkCWSDkn80-Vv7-2fR5DsGAyP9t-jTBwsIFv2jJVz6v_7a4iuUwftF2OV0UvoAMCNsY7d2zCsTBNg5XFVjnAAdLNUtgeI3cIUJhtzz3pKW7ZNmwLPachnuH23CmtvK6rn0fLwp7JGul-n9080mHQaOmDtv5jElWh9oFJ7OY5LA1tCdjkRnUgRyz9qlvjEN1Vnu-fPHaTiztA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">با پیشرفت هوش‌مصنوعی، حضور و غیاب تو مدارس هم شکلش عوض شده و به این صورت با تشخیص چهره انجام میشه :
@News_Hut</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/news_hut/72598" target="_blank">📅 23:14 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72597">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/csxZ72E15I6p55sJR2GjptvANt0MWXl9ohfkMaAy7HDImMN7eza9GVTZUrR2q5a1KokkEzQf26cR-JXH0KTn5d_iSr8iI7MES6ahvBt8HbXF8ElXgQ0IMNEJXS33s_30NbKMiLfnMuYONhLcCVNsVHTumMyfy3Gul2KyOxG9kTV0tvmyB0rOkjesRU15M_Zm8ocn8tcc3WQGLH1rxop9c8d2ZazVGHx5dTNKh9HZkNi4n4Usvju4R_4iVwIy7a3LDsGiXvzuU-8JOLgNC2jyZ7IjZbTgsPQAEqGfLLdWJ7e8punlxE6fNUaOCcI4JMY94Ctn2mQaMLrF6Mj3QCbqGQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#فوری
؛پلیس بریتانیا اعلام کرد که یک تبعه ۲۷ ساله با تابعیت دوگانه بریتانیایی-ایرانی را در مرکز لندن به ظن «تدارک اقدامات تروریستی» بازداشت کرده است؛ اقدامی که با حادثه روز یکشنبه در نزدیکی یک پایگاه هوایی در انگلستان (که مورد استفاده ارتش ایالات متحده است) مرتبط دانسته می‌شود.
دو ملک در این منطقه مورد بازرسی قرار گرفتند.
مأموران مبارزه با تروریسم همچنین از مرد دیگری که تبعه ۲۶ ساله بریتانیاست، بازجویی کردند.
ویکی ایوانز، هماهنگ‌کننده ارشد ملی در بخش پلیس مبارزه با تروریسم، تحقیقات مربوط به پرونده «گلاسترشر» را «بسیار پیچیده» توصیف کرد و اظهار داشت که تیم‌های تخصصی در حال پیگیری «چندین خط تحقیقاتی» هستند.
@News_Hut</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/news_hut/72597" target="_blank">📅 22:30 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72595">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/m4YJ5oAAxMy_T20O0Xa8PVYicIh2kpQ9CbBPXuALGXkiAkpbYSsugY7QH0yEpLRJEZHditi0BDCQy5QZzLF5RvnkTTRoPpY5jGpJim2iJDODRZYg_qTaMeKi-dFZuah2IXPjxh2EcHJpHaJKSo-7mOYxQjA_t4WfIOvwFhXwRRBcEkTvrqO8CK8sQUbKaqNwy_Vb17Z0Z3n_HNFDJt-Hqa7rPdihlTS7N1r8PGVXV31XnIf8iv6PolaoEcVqhlXF_euE1i7EV8VmXNa-HB9a6M2W8taveXdQOLcOux3QxaJgbkV9jVI9ReJSbY0s4K8cdjJzYPYyWZqq-S7Dln-JZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b7b5d4066c.mp4?token=RJMqKhDJ8iZoGjxxAJ6DvAUVh-PuDWg4suqe4L5yb5rFzSzgt2lDRi0qbHX7M1hTlDgOpu-KUsiNrS8X616FHlE6gHJ5ILeb39c6oc0frX4dIbzG9WZfQC3pWnYzMMPoESnLyaQo-eZrNzCxCYHlL4g6bmU73W3NCYpmtVXaUzEFfqZeVMaM_leH5s-Ow_UQFEHM3mkoQr58Hg8lzVt_zhLwoSdIhUBi7jcX53y9edAPewQkaVWaWvN7_6H5by6h_k8uNhgghVJCCQoBqoJ8DNBAtfyw5GcNvUBc6hpBhpki27bfMmv1Msi6S_BpoLUweCe0oYNHCttrusqRRUiNPg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b7b5d4066c.mp4?token=RJMqKhDJ8iZoGjxxAJ6DvAUVh-PuDWg4suqe4L5yb5rFzSzgt2lDRi0qbHX7M1hTlDgOpu-KUsiNrS8X616FHlE6gHJ5ILeb39c6oc0frX4dIbzG9WZfQC3pWnYzMMPoESnLyaQo-eZrNzCxCYHlL4g6bmU73W3NCYpmtVXaUzEFfqZeVMaM_leH5s-Ow_UQFEHM3mkoQr58Hg8lzVt_zhLwoSdIhUBi7jcX53y9edAPewQkaVWaWvN7_6H5by6h_k8uNhgghVJCCQoBqoJ8DNBAtfyw5GcNvUBc6hpBhpki27bfMmv1Msi6S_BpoLUweCe0oYNHCttrusqRRUiNPg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">#فوووری
؛ترامپ در‌تروث پستی از اعتراضات دی‌ماه ایران منتشر کرد که مردم در آن شعار میدهند «امسال سال خونه سید علی سرنگونه»
@News_Hut</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/news_hut/72595" target="_blank">📅 21:51 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72594">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/elo8EQtPLW1A_SCPjLSRnS8baMA6BfJHA9uygjNrnFn6ATQPMAmmjdRQjqudCBJUDtGcfFUvXZ57-6fT_1rcJzXALPRQiMZ6LIWdeQ-3t0sgwrlX5eKoFXGplK9-dLJljYeUwwla3SCQpSDpygpNkDn_CKMH7Fd85M0IY-x9jdOXioT2CB9yvamZpWtHYXqJmsLTA_cWGd7HAZSVYNEeY7CYyXKMnGIvPY0zfzY6ken1CCyBhb8rvzHd3nQquaqEfaebaA0yFc9N8ZXciH38WO9p0pYJU-SI_2l2gRDfmqQnvt8DOqQjXJZI4sxLx3suvjFCJiqZSoLyuVLvRKT7XA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پرزیدنت ترامپ:
«گفتم برای از بین بردن تهدید هسته‌ای ایران ۴ تا ۶ هفته زمان لازم است، اما این کار را در یک شب انجام دادم. زمان باقی‌مانده برای اطمینان از این بود که این تهدید دوباره بازنگردد.»
@News_Hut</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/news_hut/72594" target="_blank">📅 21:36 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72593">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/210cf276f7.mp4?token=nCsHx0XkkyyXTwIIQzbBb77BhPSBagN-uLCCV6aMykyCR6VUf9cH_pcuqMQ4IXqWBKQhg60f2NTxNJP40z_CuLJLuPZosUP1jrCnxqefZlJMC_JKcStNJUuBRMB8p_NHgDVcJkev7B5E7YnS6X2C1kyBnrYz5v5ISI5l1ssE9HSamxdJuKdsIyxsp2Y_YgcNHj8_Az-5iDvhwFpxAglsvBCdaje6NRXKdKaWjnc79bYlh1S3UynsLUf9gzbYBDG4Q08HWT08U1uNbl0yPUcbPOOSeK2mimqW8gFuaDSAI3C4by7vZYe5unu8-wgW5lIEgPj-tpcTiTQwcJo-iGMuUA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/210cf276f7.mp4?token=nCsHx0XkkyyXTwIIQzbBb77BhPSBagN-uLCCV6aMykyCR6VUf9cH_pcuqMQ4IXqWBKQhg60f2NTxNJP40z_CuLJLuPZosUP1jrCnxqefZlJMC_JKcStNJUuBRMB8p_NHgDVcJkev7B5E7YnS6X2C1kyBnrYz5v5ISI5l1ssE9HSamxdJuKdsIyxsp2Y_YgcNHj8_Az-5iDvhwFpxAglsvBCdaje6NRXKdKaWjnc79bYlh1S3UynsLUf9gzbYBDG4Q08HWT08U1uNbl0yPUcbPOOSeK2mimqW8gFuaDSAI3C4by7vZYe5unu8-wgW5lIEgPj-tpcTiTQwcJo-iGMuUA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پیتر دوسی (از شبکه فاکس): آیا ممکن است این خلبان [در پرواز فلای‌دبی] توسط سپاه پاسداران در آنجا منصوب شده باشد، یا به طریقی دیگر افراطی شده و سپس تلاش کرده باشد هواپیما را سرنگون کند؟
ترامپ: بله، ممکن است همین‌طور بوده باشد.
@News_Hut</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/news_hut/72593" target="_blank">📅 20:54 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72592">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/31205a46fc.mp4?token=IpZ4vQNkopP_mcJ6UluK37toE3Zvh2O88DD1h6v7or_9ySY3tNZIQ8ZQgFO28dYcKQ2pJlr4W2FjGSOkRbkrEhw6tmMzS74MFJGtQFrioeKhCdAlmKg0mFir-uRmfEm4RvdO5uOPJgv0mhe7F8R4lz1d7Rg3MuhgWuotU-IxMmWZ-0VVXvNHd8UTaAOsO075EjG9zHbIwOlX3akZeFk-YAf2yzOW5lMizsd0XvHRD25AFnpZVX4BGseRKhvhV4dwSB_ikVHO5-jbLj7D6Kou_3h-LB2-cLwaJ_4YFtYYVjrQJMNREaFQgJP_rvRIk3-KzzL_UtlnDYtXCk0rwoZGOg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/31205a46fc.mp4?token=IpZ4vQNkopP_mcJ6UluK37toE3Zvh2O88DD1h6v7or_9ySY3tNZIQ8ZQgFO28dYcKQ2pJlr4W2FjGSOkRbkrEhw6tmMzS74MFJGtQFrioeKhCdAlmKg0mFir-uRmfEm4RvdO5uOPJgv0mhe7F8R4lz1d7Rg3MuhgWuotU-IxMmWZ-0VVXvNHd8UTaAOsO075EjG9zHbIwOlX3akZeFk-YAf2yzOW5lMizsd0XvHRD25AFnpZVX4BGseRKhvhV4dwSB_ikVHO5-jbLj7D6Kou_3h-LB2-cLwaJ_4YFtYYVjrQJMNREaFQgJP_rvRIk3-KzzL_UtlnDYtXCk0rwoZGOg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اظهارات ترامپ درباره احتمال دخالت ایران در حادثه هواپیمای فلای‌دبی:
بر اساس آنچه می‌شنوم، پاسخ را «بله» می‌دانم، اما در حال حاضر مشغول بررسی آن هستیم.
@News_Hut</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/news_hut/72592" target="_blank">📅 20:52 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72591">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9b0dca1ef0.mp4?token=iUcjoBpZqjGNq35lAJ9iS_EGkTKjM6C91L4zMnLxCCGhCkp9v_TPneSSpiek4oBwHO0GxgmiU_2a4VLUsSQFkpawNbBCVKynFuWmLPWG4VYl0cGd9Aj4rxvPt6hup0u72riKuMv6dv6f6v-sXvqibu-BKKiXOwITWq6Ph_eM4anGmLcps5EJMc6GQ5UR7hpnxxRDLKuuv4Pk53svVrmxlwpkYG_KkHHJMmTgRu1lMOcG40oQFYbxPRlyNWsJyc57HDvfCgVI8lrNtC-Ul6mmSmeIT2MQFJnjB_Y5yJGLUK9Alz3gDbRXYhZWcSHhZwMTMEkQHwLAJMfoUaUbyA1Z4g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9b0dca1ef0.mp4?token=iUcjoBpZqjGNq35lAJ9iS_EGkTKjM6C91L4zMnLxCCGhCkp9v_TPneSSpiek4oBwHO0GxgmiU_2a4VLUsSQFkpawNbBCVKynFuWmLPWG4VYl0cGd9Aj4rxvPt6hup0u72riKuMv6dv6f6v-sXvqibu-BKKiXOwITWq6Ph_eM4anGmLcps5EJMc6GQ5UR7hpnxxRDLKuuv4Pk53svVrmxlwpkYG_KkHHJMmTgRu1lMOcG40oQFYbxPRlyNWsJyc57HDvfCgVI8lrNtC-Ul6mmSmeIT2MQFJnjB_Y5yJGLUK9Alz3gDbRXYhZWcSHhZwMTMEkQHwLAJMfoUaUbyA1Z4g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">#مهم
:سؤال: در مورد نیروهای نیابتی ایران، مثل حزب‌الله، چطور؟
ترامپ: سرنوشت آن‌ها به سرنوشت ایران گره خورده است؛ هر مسیری که ایران طی کند، آن‌ها نیز همان مسیر را طی می‌کنند.
@News_Hut</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/news_hut/72591" target="_blank">📅 20:49 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72590">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">ترامپ درباره ایران:
به جرئت می‌گویم که صددرصد مردم — از جمله در سراسر جهان — با دستیابی ایران به سلاح هسته‌ای مخالف‌اند.
@News_Hut</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/news_hut/72590" target="_blank">📅 20:44 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72589">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">سؤال: اگر ایران پشت آن حمله به هواپیما باشد، آیا دست به تلافی خواهید زد؟ آیا آمریکا تلافی خواهد کرد؟
ترامپ: ضربه بسیار سختی به آن‌ها وارد خواهد شد؛ نگران نباشید.
@News_Hut</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/news_hut/72589" target="_blank">📅 20:43 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72588">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8061e95725.mp4?token=jp198AH2A4h9Dn-kuqN-gpJ6A9ChMS6TrKDeL__DGdU5wVTxC1Sddt5tonSyrmuGCBRiwrKa3iTbwX4nH63Fi2HOkJfhmI_YxgviBwGXswtVdVlWcsAd78qa3goLg3l1a3dc7YgT945BAYua0qMnA37odEgwX8mJXLwzsJj_SUjI_foOAOMvv8Isv83cvF1WM5l6WHl4L5N9D4fkE4wPmk8rgw4kkvUQw5CUweht2eNkciI5yWRzkQ6UQUJhCj8dXF_-pZkDEa7uADdsq51Hiotb2DuqTy_1ycohYi3R1pz_SWO_BicmNXK7pEI9meHwCdQgKcHlf44mYWQO3taezw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8061e95725.mp4?token=jp198AH2A4h9Dn-kuqN-gpJ6A9ChMS6TrKDeL__DGdU5wVTxC1Sddt5tonSyrmuGCBRiwrKa3iTbwX4nH63Fi2HOkJfhmI_YxgviBwGXswtVdVlWcsAd78qa3goLg3l1a3dc7YgT945BAYua0qMnA37odEgwX8mJXLwzsJj_SUjI_foOAOMvv8Isv83cvF1WM5l6WHl4L5N9D4fkE4wPmk8rgw4kkvUQw5CUweht2eNkciI5yWRzkQ6UQUJhCj8dXF_-pZkDEa7uADdsq51Hiotb2DuqTy_1ycohYi3R1pz_SWO_BicmNXK7pEI9meHwCdQgKcHlf44mYWQO3taezw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">#فوووری
؛رئیس‌جمهور ترامپ درباره ایران:
اکنون باید تصمیمی بگیرم: یا ایران توافق را امضا می‌کند، یا دیگر وجود نخواهد داشت.
@News_Hut</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/news_hut/72588" target="_blank">📅 20:28 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72587">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">ترامپ درباره ایران: «آن‌ها نمی‌توانند سلاح هسته‌ای داشته باشند — و نخواهند داشت.»
انها توافق کرده اند که سلاح هسته‌ای نداشته باشند.
@News_Hut</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/news_hut/72587" target="_blank">📅 20:24 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72586">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">خبرنگار: لارا ترامپ گفته است که جنگ با ایران ممکن است انتخابات میان‌دوره‌ای را برای شما به خطر بیندازد. آیا موافقید؟
ترامپ: ممکن است. [اما] باید کمک‌کننده باشد.
@News_Hut</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/news_hut/72586" target="_blank">📅 20:23 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72585">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/72ce76f49c.mp4?token=UYL44PwkMiEhOTP6ZC98F2-Mh_ONpiUtm7VMxGnZdJF89W-IkvtBABxm1EvBVollfDHn8XQZXbpxgbMktV-ABNtAGNIjTa8NlZBywG0IfMkzdS2TqQCMUcTztYmPCheipv9cOONPxLMeTanZfLW7Sqv9mCVXI_bxmi0YP3tVJphKG4tpvxSYkfpXQJSd_z9Y1pApCjsk-ixzZg7GP_qP3QX8--_gHcepZKA4eUkLSECSKYjWg6cnR0nJzjQsZ-GO0zux4ldDf6aqK0Y7tmYtslGRoj3Ml2RBMdPcwh2aAZF9J7L-Gbr1gyQv-XtguOqaRT6CV3iRNTZEwQe4zNnIDg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/72ce76f49c.mp4?token=UYL44PwkMiEhOTP6ZC98F2-Mh_ONpiUtm7VMxGnZdJF89W-IkvtBABxm1EvBVollfDHn8XQZXbpxgbMktV-ABNtAGNIjTa8NlZBywG0IfMkzdS2TqQCMUcTztYmPCheipv9cOONPxLMeTanZfLW7Sqv9mCVXI_bxmi0YP3tVJphKG4tpvxSYkfpXQJSd_z9Y1pApCjsk-ixzZg7GP_qP3QX8--_gHcepZKA4eUkLSECSKYjWg6cnR0nJzjQsZ-GO0zux4ldDf6aqK0Y7tmYtslGRoj3Ml2RBMdPcwh2aAZF9J7L-Gbr1gyQv-XtguOqaRT6CV3iRNTZEwQe4zNnIDg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">#فوری
؛ایالات متحده در حال اعزام گروه ضربت ناو هواپیمابار «یو‌اس‌اس تئودور روزولت» به خاورمیانه است.
تا پایان ماه نوامبر، سه ناو هواپیمابر و دو کشتی تهاجمی دوزیست در اطراف ایران مستقر خواهند شد.
@News_Hut
| NBC</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/news_hut/72585" target="_blank">📅 20:09 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72584">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a42198336a.mp4?token=KSOKOZbm4-pYH5SjopQXj4V8-8F-cPYSJvY77N7RgV_sMO9aiuq0cgiRQyWK3I7WWAxpgSmZvSFmObMbBluKwW1yVqYjwGeqSuwP9TiUNaddFrBNXf-JLupz1liBTTV3pTKnmuDVQPfCED7SCmBwthrMThJbjeUQvr6cqEpdoR0GwYQ_ye8N1Ids7HUgelAITjwyRUT_pyI7PwRMy5p5mvSr8fHykx7tHuPNVAJMtE2_D0sHmigMCPJmIhST2IEUYAo-_L5MGogzYoL3nId-8baLkuvUkeYNqA_tNq0lgxOvJB5T0moWy4HbvVlx8IypMAF7vZGLyy0ALF_kciDnVw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a42198336a.mp4?token=KSOKOZbm4-pYH5SjopQXj4V8-8F-cPYSJvY77N7RgV_sMO9aiuq0cgiRQyWK3I7WWAxpgSmZvSFmObMbBluKwW1yVqYjwGeqSuwP9TiUNaddFrBNXf-JLupz1liBTTV3pTKnmuDVQPfCED7SCmBwthrMThJbjeUQvr6cqEpdoR0GwYQ_ye8N1Ids7HUgelAITjwyRUT_pyI7PwRMy5p5mvSr8fHykx7tHuPNVAJMtE2_D0sHmigMCPJmIhST2IEUYAo-_L5MGogzYoL3nId-8baLkuvUkeYNqA_tNq0lgxOvJB5T0moWy4HbvVlx8IypMAF7vZGLyy0ALF_kciDnVw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">درگیری ثبت نامی های خودروی لاماری با شرکت وارد کننده، که ادعا می‌کند به دلیل محاصره دریایی چیزی وارد نکرده.
@News_Hut</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/news_hut/72584" target="_blank">📅 19:32 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72583">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f5610e80a6.mp4?token=Ax9Jpa0Dr0tYorv2guDvlkBHdAbFOOrvdIZS2crGkszJO6eCcY7wpvK1mtwFo9kKu-jHhbmhOKI9VggqF_NSTuLgfRJ2_QaiIeaetT0PkFvC0ltNMFxHPK90KwDmt3ansC9C3eY4UUXHWkW27OE8TDyHLr2IPhk-TD9YFupqyA4jZeYBiYEQP7NdP_0X480rmIHfa48eD45RJvLZ4OSfJP49A8GQWdQXIdBvgylYAwGKH1hrggUyUpskAaCEL9H6jlyJArtnSj83tHWQXYPGNP9Xz_eJH3712xqL2hbKFZE0O93StgWq0m3AP7ACGl2uD4tPlTVVyp0Dbzq3pW9EoQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f5610e80a6.mp4?token=Ax9Jpa0Dr0tYorv2guDvlkBHdAbFOOrvdIZS2crGkszJO6eCcY7wpvK1mtwFo9kKu-jHhbmhOKI9VggqF_NSTuLgfRJ2_QaiIeaetT0PkFvC0ltNMFxHPK90KwDmt3ansC9C3eY4UUXHWkW27OE8TDyHLr2IPhk-TD9YFupqyA4jZeYBiYEQP7NdP_0X480rmIHfa48eD45RJvLZ4OSfJP49A8GQWdQXIdBvgylYAwGKH1hrggUyUpskAaCEL9H6jlyJArtnSj83tHWQXYPGNP9Xz_eJH3712xqL2hbKFZE0O93StgWq0m3AP7ACGl2uD4tPlTVVyp0Dbzq3pW9EoQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شاهنشاه آریامهر:
«کلمه‌ی شاه در این‌کشور (ایران) معنای ویژه‌ای دارد و همه آن را می‌پذیرند. ممکن است اهالی روستایی دور‌افتاده در کشور درباره‌ی اتفاقات جهان چیزی ندانند، اما آنها معنی شاه را می‌دانند!»
@News_Hut</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/news_hut/72583" target="_blank">📅 19:00 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72582">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/news_hut/72582" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/news_hut/72582" target="_blank">📅 18:59 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72581">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/glg1xxhjKTCisCkclC6qZ-dc8IFqq0SuBupagzRw0cRl-KvkvpZ3P8lxqnjkJuS7HVmDlDKjET-z4zTP-OJ6d96m9syOpbevGdN_f6ysGl3WKNZ7bFvyipEFdORakxvFKK7kZkG3WeJabbKd3TqQZ5ZHeQ8LOa38e5Q5WYAkazw5PVGh9qgLCreKqow0ZmGTccGjkhzUqFsNg6RszBbOFM4aSoAlDWu6IXtAkcNeEwHUCTlRLMeNRf-FJtWLcvhPP4VAD4yYGf1wQrQufJ_wUpSXWhfxfV-p2UIE7x6B4klSU8qtl8Ov3xc5VNfNYdX6e7vG5b-3YV9Pv3-8pasxpg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🤩
نبرد هیجان انگیز پرتغال
🆚
دانمارک را در
TrexBet
پیش بینی کنید!
📉
نگاهی به آمار ۵ بازی اخیر دو تیم:
پرتغال: ۳ برد، ۱ تساوی، ۱ شکست و ۵ گل زده
دانمارک: ۲ برد، ۲ تساوی، ۱ شکست و ۱۰ گل زده
🦖
🦖
🦖
🦖
🦖
بونوس اولین واریز تا سقف ۱۰۰ یورو
🦖
بهترین ضرایب بین تمام سایت‌ها
🦖
واریز آسان و امن از طریق کارت به کارت
TREXBET — PLAY. PREDICT. WIN.
https://TrexBet.com
T.me/TrexBet_Ir</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/news_hut/72581" target="_blank">📅 18:59 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72580">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">#مهم
؛
یک
مقام آمریکایی:
ناو هواپیمابر «روزولت» و گروه ضربت همراه آن، سن‌دیگو را به مقصد خاورمیانه ترک کردند.
گروه عملیات آبی-خاکی «ماکین آیلند» نیز دوشنبه گذشته سن‌دیگو را به مقصد خاورمیانه ترک کرد.
حدود  ۲۲۰۰ تفنگدار دریایی در قالب این گروه آبی-خاکی به خاورمیانه اعزام می‌شوند.
تا پایان ماه نوامبر، سه ناو هواپیمابر و دو گروه عملیات آبی-خاکی در نزدیکی ایران مستقر خواهند شد.
با این تمرکز نیرو در خاورمیانه، فرماندهان گزینه‌های متعددی برای مواجهه با ایران در اختیار خواهند داشت.
@News_Hut</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/news_hut/72580" target="_blank">📅 18:19 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72579">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/k4357ZUIgNrCwj2Dq-f9xgHCNd-yY8Auw-up5di_iBJMwdCCerXom8Y6GqkS-7zp5WB5KWykGc38B-ZMn43CHQWR4i7NwMwTp5UUNbyvjJmmInaP_f8rMTsIMZQZeTRRzMhkVzXl7SSoHdJzhNoWtGw1J36TgN0Q_ZN1rovYwfd_A2Qh7Gmq-Q3FWKSiBdzP6L8vGajm-Nip5UbDNJNBPexLyvF7BTVNtw-HMhbJXILWRVzR64dfHnTdzehyoKeVTjEkG1KbOuDKtMjGiKy28hXtZqWERYdYlvx2gIBXETuwzwnV94FsRfijIpfgvFUkFQxNeIGXQCS33TzyiMJi5A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">امیرمحمد، خواننده آهنگ سنی نردن گوردوم، از بدن فوق جذاب و عضلانیش رونمایی کرد
@News_Hut</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/news_hut/72579" target="_blank">📅 17:32 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72578">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6f32d27e64.mp4?token=YztrLuOlSiQN_G4ffgxQdQzUJxSrn3yaYxpGSfjs9lPj7FhWYdbeSRYjQ196TZJuZ-o77AGJi6AxFODvq_fh4lt2FyVXnCr6l9gFclXh-wyIthkM1WOHHZxG-0AQxMpJACzGuatGxes2C8VUhiyKgbY33SsN-ybdEDeV2Ur1lGq58jqyBq7hWdtX5w9YiFWf1JT1FLfa4V4u0b-qjRcsB8auvjYB_nyNgXzxBF8NJPXQOT9snv4Qky4dq8sXFb0ksZqljYBb2lfTzmacFXIPxR5zV7whGweBv7hd-h7EUkAW0Au0QmDwI0vQcIj3MY_2iW0yM3fgtOUfX75MExTgDQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6f32d27e64.mp4?token=YztrLuOlSiQN_G4ffgxQdQzUJxSrn3yaYxpGSfjs9lPj7FhWYdbeSRYjQ196TZJuZ-o77AGJi6AxFODvq_fh4lt2FyVXnCr6l9gFclXh-wyIthkM1WOHHZxG-0AQxMpJACzGuatGxes2C8VUhiyKgbY33SsN-ybdEDeV2Ur1lGq58jqyBq7hWdtX5w9YiFWf1JT1FLfa4V4u0b-qjRcsB8auvjYB_nyNgXzxBF8NJPXQOT9snv4Qky4dq8sXFb0ksZqljYBb2lfTzmacFXIPxR5zV7whGweBv7hd-h7EUkAW0Au0QmDwI0vQcIj3MY_2iW0yM3fgtOUfX75MExTgDQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جزئیات حملات آمریکا به ایران از 28 فوریه تا 8 سپتامبر ( ۹ اسفند تا ۱۷ شهریور ) :
@News_Hut
| thecuriospark</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/news_hut/72578" target="_blank">📅 17:00 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72577">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4a8db6d91d.mp4?token=Apov-bzQRVaGir7GVh3aGkwhe9TRpbztD-06aQ3JCaU2IPrIPtKe5P-ql_aP1hXasI-WdQfIkPziM5TEeHqKqHJqThTEOrebLvGlybzyiD-kTKcVV68mNZFumVR4q4TvrQ_s3fxxqctR-tw8F4edFwA5hHRxWekWlAmAzNutdr4oYIqESiRaIQ5yymgwmiqSfANSxwwj9I3n8LDTTf0jqmiNhJhnKswW_0UJGrrB7OhvMb6jleQut8m4Mp8cLY3aAyAXk1a2f3SnkqdKy0WsiQw3kxrt1e4JJa_ii0GN506EzEWsTaeUvVn6uPEQy34z1hrBxftlAM3EmKu_SbcTUQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4a8db6d91d.mp4?token=Apov-bzQRVaGir7GVh3aGkwhe9TRpbztD-06aQ3JCaU2IPrIPtKe5P-ql_aP1hXasI-WdQfIkPziM5TEeHqKqHJqThTEOrebLvGlybzyiD-kTKcVV68mNZFumVR4q4TvrQ_s3fxxqctR-tw8F4edFwA5hHRxWekWlAmAzNutdr4oYIqESiRaIQ5yymgwmiqSfANSxwwj9I3n8LDTTf0jqmiNhJhnKswW_0UJGrrB7OhvMb6jleQut8m4Mp8cLY3aAyAXk1a2f3SnkqdKy0WsiQw3kxrt1e4JJa_ii0GN506EzEWsTaeUvVn6uPEQy34z1hrBxftlAM3EmKu_SbcTUQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدیو رقص این خانم ایرانی تو وان ترکیه وایرال شده و واکنش‌های مثبت و منفی زیادی رو در پی داشته:
@News_Hut</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/news_hut/72577" target="_blank">📅 16:33 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72576">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5a415ffdec.mp4?token=P5hMtvSht5nJnOXBlUVmZiz5k5H14m7FuagLzAFnDtW1zrmmvxIlsNdUKsSvzkANUmPbtft0BMEpKYLf8OEA3NwoISExHLM95y2WMPlzlr1yAfFx7YfqLYcSKYPN0gFvSemLGwSa59VsxM1Q1Rgca9KcqSHk3BOwiX6P7hFKHw9rMZ9trmNpYuDrO83LG84QBI1zdBhEN2-koQ_7lh9G4n4BUa2lQpcBoW4XS3f-L1-4YLLoHgpCDBMClw-rocW11qjWHi3oB8obPpWWG11zcCeBvL8PEPtZyLILkIHoXtYups9WnB9fMa_3M6e7LKdxk6BWKnE850XABJlRr0zgjw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5a415ffdec.mp4?token=P5hMtvSht5nJnOXBlUVmZiz5k5H14m7FuagLzAFnDtW1zrmmvxIlsNdUKsSvzkANUmPbtft0BMEpKYLf8OEA3NwoISExHLM95y2WMPlzlr1yAfFx7YfqLYcSKYPN0gFvSemLGwSa59VsxM1Q1Rgca9KcqSHk3BOwiX6P7hFKHw9rMZ9trmNpYuDrO83LG84QBI1zdBhEN2-koQ_7lh9G4n4BUa2lQpcBoW4XS3f-L1-4YLLoHgpCDBMClw-rocW11qjWHi3oB8obPpWWG11zcCeBvL8PEPtZyLILkIHoXtYups9WnB9fMa_3M6e7LKdxk6BWKnE850XABJlRr0zgjw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حساب اسرائیل به فارسی در پلتفرم ایکس:
حالا که بحث هواپیما گرم است، یادی کنیم از هواپیمای کیش.ایر که 31 سال پیش در مسیر تهران به کیش با 174 سرنشین ربوده شد.
زمانی که سوخت هواپیما تمام شد و در شرف سقوط بود، اسرائیل تنها کشوری بود که به هواپیما اجازه فرود داد و جان صدها بی‌گناه را نجات داد.
جمهوری اسلامی هرگز نتوانست پیوند بین دو ملت ایران و اسرائیل را از بین ببرد.
@News_Hut</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/news_hut/72576" target="_blank">📅 15:52 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72575">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">ترامپ اظهار داشت که ایران خواستار توافق است و درباره پیشنهاد آتش‌بس ایران که در آخر هفته رد شده بود، ترامپ گفت پیشنهاد ایران برای باز کردن تنگه هرمز کافی نبوده است.
@News_Hut
| Time</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/news_hut/72575" target="_blank">📅 15:32 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72574">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">سؤال: نتایج نظرسنجی‌های شما هرگز تا این حد پایین نبوده است.
ترامپ: این ارقام ساختگی هستند. من هر کسی را که امروز نامزد باشد، با اختلاف ۲۰ درصد شکست می‌دهم. نظرسنج‌ها فاسد هستند.
@News_Hut</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/news_hut/72574" target="_blank">📅 15:23 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72573">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">سؤال: اگر «گادی آیزنکوت» در انتخابات اسرائیل پیروز شود، آیا آمریکا می‌تواند بهتر از زمانِ «نتانیاهو» با او همکاری کند؟
ترامپ: خب، نمی‌دانم. حرف بدی درباره‌اش نشنیده‌ام... فکر می‌کنید او پیشتاز است؟
سؤال: او نامزد اصلی اپوزیسیون است.
ترامپ: خب، خیلی‌ها بارها «بی‌بی» را تمام‌شده دانسته‌اند، درست همان‌طور که بارها مرا تمام‌شده می‌دانستند. من بی‌بی را دست‌کم نمی‌گیرم.
@News_Hut
| Time</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/news_hut/72573" target="_blank">📅 15:22 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72572">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">سؤال: گزارش‌های متعددی وجود دارد مبنی بر اینکه پیش از ۷ اکتبر، به نتانیاهو درباره احتمال وقوع حمله هشدار داده شده بود.
ترامپ: امروز برای اولین بار این موضوع را شنیدم.
سؤال: گزارش‌ها حاکی از آن است که مصر و امارات به او هشدار داده بودند.
ترامپ: فکر نمی‌کنم؛ به نظرم اگر او خبر داشت، حتماً اقدامی در این باره انجام می‌داد.
@News_Hut
| Time</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/news_hut/72572" target="_blank">📅 15:20 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72571">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">ترامپ:
اگر من رئیس‌جمهور نبودم، عربستان سعودی الان وجود نداشت؛ اسرائیل هم همین‌طور. آن‌ها از روی کره زمین محو می‌شدند.
@News_Hut
| Time</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/news_hut/72571" target="_blank">📅 15:19 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72570">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">سوال: شما در ابتدا گفتید که جنگ با ایران حدود شش تا هشت هفته طول می‌کشد. اکنون وارد ماه هفتم شده‌ایم. می‌توانید توضیح دهید چرا این‌قدر طولانی شده است؟   ترامپ: فقط به این دلیل که می‌خواستم فراتر بروم. آن‌ها را از میان برداشتم. می‌توانستم همان‌جا متوقف شوم،…</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/news_hut/72570" target="_blank">📅 15:17 · 09 Mehr 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>

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
<img src="https://cdn4.telesco.pe/file/Gw25KyPZv88yv60EfisI_Cju4JAkyVEcxIG2jfX9ziq_Q0WxvUJhLUvuLt4de37kzDhK6hxSDnx67IurxE_rE-sGSRe6g4NoyQ9NiQrf-qtBxllpCWLCwcusaxKOkqkqjrdLqZC6VdS9hRcwWOLePGAoDLR9EEy487QA0BxoHhhJvUP6jpQMHWjEtvTeGGEkyWyXMpE9sy4SrVYml3D9YkGR-AQxIkTqcjtHp_H3aSbM4lQzmqerE4maELtamiCFR8LqbjX1uMoLgEwSjX-9Z5q_9Cx1LsPfkfOWBbM4y7hNfIualOh2rwBiMKjdopu3EA5FqLdN4atFelsb6XALLw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Persiana Soccer</h1>
<p>@persiana_Soccer • 👥 544K عضو</p>
<a href="https://t.me/persiana_Soccer" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 پرشیانا ساکر دریچه‌ای تازه از اخبار محرمانه و داغ فوتبال ایران و پوشش اخبار اختصاصی نقل و انتقالاتهماهنگی و رزرو تبلیغات:@adspersianaکانال دوم رسانه مردمی پرشیانا:@Persiana_Plussپیج اینستاگرام:Instagram.com/Persiana_Soccer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-19 15:05:25</div>
<hr>

<div class="tg-post" id="msg-29439">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KYMfRMUDst7tAj24tmJaRBNzgcW0QcRW7umnl8oBgic-2jFzDNBu0P6wjmySOQgucM2xNgMOAOdox9wmFI7e_UmhQtSJ190qijKxPfkSgAXBGzwP5qPp0IYYbu__c-He01NatGud6CxTeeaSuxKFaqNQK9Km2N0l7a9ONKb1yvYqajmToQyRCcGOO651EOt51elJh2xnYYVMVruaDVjlhkh82krhQSlqsVcAjEUJRSn7nBtEzSpyeZaPpRg67y4k5udKZugUZReiR9hx9ZW0eo34eJ36M_MApiH5lRyahthJrWMh0CoKEEHnBPAyCwIPd5Spor5e0YfshQbm0Gznhg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
👤
پرواز تماشایی برای گل شماره 979؛ گلزنی دیدنی کریس رونالدو 41 ساله در بازی امشب النصر
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 910 · <a href="https://t.me/persiana_Soccer/29439" target="_blank">📅 15:04 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29438">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EhwLBwyp3g-WZeOarBERAvK1FfiKXUzKWolhpmVtoXtGv9mbdHWzVTKMu6O_0wZxpERC06rh407xSkYn8jtNTE6eDwFSnfcktaVAS_D7E4vZQEIMY7FKCPfyydtjy0gIrihkHDDrrVg7GCFF6YNcMzH4_iRthTu36UkKX7CSQCymwFnflHCN_1r8ZZ8bThPabggMINBIUmO1h3kQYdltwDyiOcczoBFGwY3VHkKi8zFbetiAkQDYtOlKu3ESElYYtjDUuad8VHbR2I6g2Rd96ZgUsagHWFyaahMYjkwrv_C-sAXwDqh_QH61Otjqqm-r1WrWYxRM1zNMa9QQuO9Pgw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
مهدی‌تارتارسرمربی‌پرسپولیس:واقعا موندم چرا بازی برابر خیبر لغو شد. ما چند بار اعلام کردیم هیچ مشکلی برای این مسابقه نداریم اما سازمان لیگ به دلایل نامشخص تصمیم به لغو بازی ما گرفت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 8.78K · <a href="https://t.me/persiana_Soccer/29438" target="_blank">📅 14:47 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29437">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YY3nOYdD8elr5PtCnJmbUjJIcJi4OgfA2hJl_s5AhQ9SLXOjeO1qp2xBI5azvKG8JX8dFsBvJqlBZXjYv_SrFycw4e8qYDwxyqDxOAwcI-u8bzmdlZjsaoiI2Hbak5g6YO3efpE-Ertwequ4786D7X7c_pNqFV30xVzAPibp6Ek7O4VlIwDLUkYtEYCPTWK-IQQAQofJj3gdmcQbVVS_C4qqMGu6oUPr8M2hzr_SEAj9Hj39F1PsGcQLug2TgBUiMI1O2cuW-qi4_r3DJwqoKy11IsCHJzPVHv-jzE01jRowfwfTjJ3dOyI2Id_6X8iNKWH81tezG4KVAC3CJzjrvQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
تاییدشد؛ باشگاه‌پرسپولیس‌ اعلام‌کرد که هیچ گونه درخواستی برای به‌تعویق افتادن مسابقه با خیبر خرم آباد نداشته و این بازی روز یکشنبه برگزارمیشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/persiana_Soccer/29437" target="_blank">📅 14:39 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29436">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bBevE6cdLbUca4gOweEPBLqlhfJQuh15Oh8vQ9_JJtGwVkTWiSedLPJhXpTsikzC_qUXTnd70BjsfJnNyZtjumR3cqsmLTTpq514qsshEF5ykqBaD-A3hq7CBz7mOB7rnGZavFqxRbGor0cNgZfzN7C7LApRGdQwNxD7reV5ChE6m4ktuqKAwiMFNid1_Baz5FHqWFgwbhFABc0jVeTLSLCrdlranh2L5WSGGLYPrFc00dt1KlUbNxGjuIaEMoC1NE8GOYvJzeYCyfKR7WgkQvhTvX6g0Hnfhh6HiJDx6NtXDVDhHQOZxCTMxPWbgb0lMA1-1DmAGXLD3fhE5aYuqA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#تکمیلی؛علیرضامحمددستیار مهدی تارتار در پرسپولیس درروزهای‌گذشته‌با فرهان جعفری و محمد قربانی تماس‌های مفصلی داشته و از آن‌ها خواسته به تمام‌پیشنهادات خود پاسخ‌منفی بدهند تا بانک شهر در نیم فصل مقدمات جذب‌این دوبازیکن رو فراهم کنند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/persiana_Soccer/29436" target="_blank">📅 14:19 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29435">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/W3-Mcx5qGz1JFwKN7SwEKtONWqlQfNzF6DdldH5mvDhIx-pI5BInypr6RzHOHdSAmUIsmEdj9ReeJjLu5o1mkzquSYrWntPC5XF3qMRf8DeT2NFFDIefGFVaBDVVmOZHwNgSEdJWSg-Fx2_sVK0yPnoYAiqZgASW8hInhSe5OPJBGb9hSgoK7NN-QUaZB3Ck64XJvMKcL3atFrUnSOHFGS8DR0eTqum6rqTsEtzz_MMFbUS60biIE6_tY9t5ieJUhI2BOsf2Wv6AMZ7Tsak6SRnIw5Jqou7ZDWxLCX2z1XZzcAbU1z-gDr7VbQrpUYfaQqFyDPB4n8MciqnUkn4stw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇵🇹
🇵🇹
بعداز حمله‌شدید هواداران کریس رونالدو؛ دوست‌دختر ژائونوس پیج کریس رونالدو و جورجینا رو در اینستاگرام فالو کرد و برای او کامنت قلب قرمز گذاشت. دوست دختر نوس بعد از اون مصاحبه علیه CR7 توسط فن‌های رونالدو به قتل تهدید شده بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/persiana_Soccer/29435" target="_blank">📅 13:49 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29434">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/T71Bu0uanTHnb6nUvlkoKpebzVzAlrxbmsCOrvH6VLUIdGvBlYmd123LZGIVYDtSexrHRQhYGGwRiMMVVr6v5hPUiiK3OErXlev7hn3UEK683gNO_bF7d54EUcGjlZWqXhdIy_5X1r1JXkjiKnqd3-GazgtixRXYmzSWABpTE9EKZfGn1SOKOtKQpiG-urEVSldtHA-qsPJ9-v_8sOUhEnfxYyd5_vEJ7SiudyHVfVcnPjP7ZAc5SEHId3Sm3XtyQH4ss2C6Y0w5BlwVDTa-IXHtwBP05Sw5n0hFToDFg0hxuwgQXRLnhz0llrLAXZV9gWEVDXo4_r0ZZkn1rp6NhQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
بااعلام‌رسمی سازمان لیگ چهار دیدار ذوب آهن با سپاهان، پرسپولیس با خیبر، ملوان با خیبر و فجر سپاسی با آلومینیوم درهفته هفتم لیگ‌برتر به تعویق افتاد. این درحالیه‌که باشگاه پرسپولیس دقایقی قبل اعلام کرد هیچ مشکلی برای دیدار با خیبر ندارند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/persiana_Soccer/29434" target="_blank">📅 13:31 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29433">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZCaIqCh48VHqWvUVvccl2vi8yBXwfMEcRiB-DBJ5s_Xo8jfPnCK2n_q7y7xpxa74qZoPWjkQ7mfyoZOnB1sE-jAOE-eQR1vO7sNgF2En7ccMghpMFzbtz9NW9NcNaTYwjWQpYHgU227BDIGNq_C_FBR9lzYMXd7yOqBtmYdyTO8TB_6xNF51g-UOwJ3M5dOczr9Xh1gHZCg2qHjIt-rrpSehkyNFQzLKAzEP1ou7FUqeFX-DkcXo-HAy3rV1ZHCxBFoAmb06UsqkJB7HLYB9ybqFXLRb7CjYGm46Hb3IwVUUXePuHP37qiCy70uAVJ4FvGsPij6_xEDHFZFzTU2OSw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
تاییدشد؛ باشگاه‌پرسپولیس‌ اعلام‌کرد که هیچ گونه درخواستی برای به‌تعویق افتادن مسابقه با خیبر خرم آباد نداشته و این بازی روز یکشنبه برگزارمیشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 29.7K · <a href="https://t.me/persiana_Soccer/29433" target="_blank">📅 13:11 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29432">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fyvdxzAQsEHtKxWRctygaBScmDBY9DwQBn6tSw5d8gaw8eFrGleNePA3ELzj-8gt1L1ANxtzYTun7AQS7gpi--cpc22viJWqZ_YkypseUcuaN6DRWMBzdj6VO5qq8YyFJkg_FVXmefrAnoxN-G9t0O9EEXFNo1MADVcMICB2lGnm_aGR4RvC527hyDGhnWquxg9MNggPBBg1LJnXRdrJCN1ZAIseMaBpfKD6ekZ6EY-gLTKnLi1XmjIIGaGiDqd5agZHZdqjd3mW_Qy9THtOQbyiMZeW6mcR-8TSNPW0nrEmtmLz_oGMBtMHY4gBRAJzvIPwjZ_5dMnIR7_VYEY2iQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🍏
تقویت فوق العاده باتری آیفون در سری جدید آیفون 18 پرو و آیفون 18 پرومکس. قیمت آیفون 18پرو: 1.199 دلار حدود ۲۸۰ میلیون تومان آیفون 18پرومکس : 1.299 دلار حدود ۳۰۰ میلیون‌تومان.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 29.7K · <a href="https://t.me/persiana_Soccer/29432" target="_blank">📅 13:05 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29431">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SbStaM4I8DTk4R6NT2VapSQ3jXsL7m-_Ssp9RhyrQM_jP2cJ2qdOYoQTOEApH3w0BWKrOzq0O-DRHJIvFN_a53RSyojn4a8KFCpbPA5fiRKzok-o5JnXJ7sKTZlLl7YJKtN-X3XVwwsHVc5q-omJFX0c3pP4TZ44sChQki4UFf9xGu966ScLOgm-4uAwElPBo6vy8beASCa0Guxehjh6qRyCMKY2z0U8stepRC3FCQwzzV5Ky-SYOsZTeUuq8134rhrWn-8ho2_VSRFBywf3fvW-G_jFF5U3Ew1JeZ3QQlNvxQja7qlI0jqs1_gDRZQLkmI0O4pkeESYYlYE4Lv1Gw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
باشگاه پرسپولیس تا این لحظه هیچ درخواستی برای لغو دیدار مقابل خیبر خرم‌آباد ارائه نکرده‌اند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 32.7K · <a href="https://t.me/persiana_Soccer/29431" target="_blank">📅 12:45 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29430">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Y2Wn8pAYVx5QMW0EhL0bAMaYp2JAEUPN760cfXXDP9gkCli7dI9rwd4l7CP0DyEXHlSZfXhoJAqdRTs3BGTVTM1gm_HDdZn74UeXBcUZyIuM62qyfrNgeyJOihjXmaI8eyWW6DwTqcYYA6hPALk-8JgobYAH-ELkGlukUE_TfMZoathw9I6rZiu3vKbSaIsCJyqv96v7Jt4BIKNorvnM_099L_5Q9M-n7cWkJ5n1TBGPFNYSqtgpBz77QSb2M4fhywQjiZmGzzO4avIcte-gZSXntOX7epOUevVCPWhXeTNXDGGwJVCp1WmtuA8aazlscrdkZw5Miq26pFJKhsAZfA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇺
نتیجه کامل دیدار‌های امشب هفته نخست لیگ قهرمانان اروپا؛ از آتش‌بازی آبی‌اناری‌ها در نیوکمپ تا پیروزی ارزشمند آرسنال در ایتالیا وبرتری لیورپول و پاری‌سن ژرمن مقابل رقبای خود درگام‌اول رقابت‌ها.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 33K · <a href="https://t.me/persiana_Soccer/29430" target="_blank">📅 12:36 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29429">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f985df7eb6.mp4?token=UXPFW6MkA24Mprn81alQ0Ny4fYHqtcpSMhPm3VbtnOIhj3dsu9KuciUjNgQTdwwTAWj27BA7Iqu43RLMCSYRR-HWciTJp0O4YLN3kEKuQm1rh3a3kM_fIq22_mcQHo_kTxovWXUfgmpp_kBwSiHJJfA0PqsyEpW3r_Q6UW6_0bc5L10qVTTdosu7IVNukoJsFWl2_ILLaImCr12N8QPSLfFDhVO8blaOggPCY2QGxdAbiU0lUYfl685J3LOEBfjE6P64_aqV124cG9vYr6s_ZDlbWXI89p7AoAUpicSIRNzbs98ZnY-T43z0zaUqOr7zGH7ywSm1my6hyJ1ah6vrPQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f985df7eb6.mp4?token=UXPFW6MkA24Mprn81alQ0Ny4fYHqtcpSMhPm3VbtnOIhj3dsu9KuciUjNgQTdwwTAWj27BA7Iqu43RLMCSYRR-HWciTJp0O4YLN3kEKuQm1rh3a3kM_fIq22_mcQHo_kTxovWXUfgmpp_kBwSiHJJfA0PqsyEpW3r_Q6UW6_0bc5L10qVTTdosu7IVNukoJsFWl2_ILLaImCr12N8QPSLfFDhVO8blaOggPCY2QGxdAbiU0lUYfl685J3LOEBfjE6P64_aqV124cG9vYr6s_ZDlbWXI89p7AoAUpicSIRNzbs98ZnY-T43z0zaUqOr7zGH7ywSm1my6hyJ1ah6vrPQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇺
گل‌های سه دیدار فوق‌ جذاب امشب رقابت‌های چمپیونز لیگ؛ لیورپول با شاگردان سیمئونه، تک گل دیدار آرسنال و ناپولی و آتش‌بازی شاگردان انریکه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 33.6K · <a href="https://t.me/persiana_Soccer/29429" target="_blank">📅 12:20 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29427">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/cGfDGLk9EyNN5lhi5ewgHYznNaNiyAH1uZuRaGENizdGNznygA8ymyGU-_caOSlz-i_VuObKN11r9rod674jJ7PB5XYVHXGCd8vkIaazJ-JJMi1GtSBR3kRkf0AICEA52PUglxiHVMEiTRz6u8sg13Jq9JKP7PSgFpbwmkxL-BN-tRs9xf9YnWbDbHwjXr23X99Pxr_UecYEBpWgSUWcqRXARP0c9TVp-M0dUfeZuN75LJZB0TECpQaV7k146msEAx0Ot6xZyvkgAAoIkmMBxDbR_ggLeWV3bh6lAEN1cc6nNZEUPmNZOmaTMvasXL7sHhcW14kK8DGPBHxs5n5SOg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ssphVKeoT8rLREx9kW72C6EUygBEE2cdTk_0UBQBtmji01FPIu2OE5Bz-uJTxj_UaZ31Ax3J8htWMRvXILjeltFsajRjllLe-URx1V2XSaobfzAt-y-SGtaKMmIp94kSPEEoOcIrLZjxC-1Xv9ydCXfl1Jtn1M1tAt3HNTrg_4UXwukVJ7DVNLdipCvwnwreWqK6jLGIMot35jnVL6Zaxg1z6RnC7PZQPCwhH0O1c1uT_hTpZNkHu7olkJFdBUjeWBHEpy8P9Vfwu6oQKZSJwbB_zZcX69M5C3-tYWEoig3tkrI8AUTX1NAiHdcRfbyAPKcH_TB6GThu30MbOn9ImQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🟣
🇦🇷
پاس گل دیدنی لیونل مسی به کاسمیرو در بازی بامداد امروز اینترمیامی‌مقابل‌شیکاگو فایر در لیگ MLS؛ بازی با نتیجه یک بر یک به پایان رسید. این423امین‌پاس‌گل دوران حرفه‌ای لئو مسی بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 33.3K · <a href="https://t.me/persiana_Soccer/29427" target="_blank">📅 12:12 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29426">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b139c692a4.mp4?token=pR--xMYep2KMI54_NYF67L2qSPkS_sWefxM9GC9a7Z45kPZAfgXnMMTtWHKkEppJVJeLNFBKnQel9iRAdPp41qf7QM-cZllCUGxwvVkHak7w_igoD7V5d__uGyFlmQLiNGVq6XH6x8rVmC1tkb-HMbltNQeyaXmkQJJAlI-MHlAMAOIEMO66yBGb0aiyVSoDHZGAoq0kE8ATfhAA7nvEadFL8XRcOmRVmTKwcWJkRMBESvHwD_bwdKU4_rF_ZzqKyE9EugG34veRP7B6VaxBN59hmoqXQ3g6G9IzNo3xV39YSnsFnWgZtLGeMtMp9lxrld3dv0ulgf0I6IZQIV9-dWHAVYd8fVtz5grfJLNw7Him-YPC3Md5YRwla6g0zUrz7dfNdiaIfHKrYiqXJ3Z1NCf0XBzgGZQgXAKKjajjAsSYTRA7Mn2i7l7TZzXRDYr0tKuYoJjy_vhMS2A_ZjtnjY78DSHeF2IDsUwuF5D70Nlo9HU9hr1IcHDQrv-eMMu8j6kbB4hjt7jTfkG3foYn4sMhHtMqU-thmYgYeBaoYvh46apXQolnQDg36XWIFYUB9oxAKIlcUnJJolyCpZKBM6HelHpCptmCpN2h8hT3MEdDyb1XbtNBK0FFx88WrSklTXpzOBERLS6tQ8S7pMN-fX1wsfQufjzNFug7eP_mZYA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b139c692a4.mp4?token=pR--xMYep2KMI54_NYF67L2qSPkS_sWefxM9GC9a7Z45kPZAfgXnMMTtWHKkEppJVJeLNFBKnQel9iRAdPp41qf7QM-cZllCUGxwvVkHak7w_igoD7V5d__uGyFlmQLiNGVq6XH6x8rVmC1tkb-HMbltNQeyaXmkQJJAlI-MHlAMAOIEMO66yBGb0aiyVSoDHZGAoq0kE8ATfhAA7nvEadFL8XRcOmRVmTKwcWJkRMBESvHwD_bwdKU4_rF_ZzqKyE9EugG34veRP7B6VaxBN59hmoqXQ3g6G9IzNo3xV39YSnsFnWgZtLGeMtMp9lxrld3dv0ulgf0I6IZQIV9-dWHAVYd8fVtz5grfJLNw7Him-YPC3Md5YRwla6g0zUrz7dfNdiaIfHKrYiqXJ3Z1NCf0XBzgGZQgXAKKjajjAsSYTRA7Mn2i7l7TZzXRDYr0tKuYoJjy_vhMS2A_ZjtnjY78DSHeF2IDsUwuF5D70Nlo9HU9hr1IcHDQrv-eMMu8j6kbB4hjt7jTfkG3foYn4sMhHtMqU-thmYgYeBaoYvh46apXQolnQDg36XWIFYUB9oxAKIlcUnJJolyCpZKBM6HelHpCptmCpN2h8hT3MEdDyb1XbtNBK0FFx88WrSklTXpzOBERLS6tQ8S7pMN-fX1wsfQufjzNFug7eP_mZYA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
ویدیو جالب از حضور ریما رامین‌فر در جشنواره فیلم ونیز با تیپ و استایلی متفاوت و واکنش نقی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 33K · <a href="https://t.me/persiana_Soccer/29426" target="_blank">📅 12:11 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29425">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Fi870Y9iB4nuIm_G1W6kodqfwPgzBFwH1JR6COMv-YMu5f9OnrQ75N8G1mbeoO8XWRuV8Ksv0Sz5f4_xaK2Wx566cZwRieTV29liLvNMkspWrhQT_IEYmEfGX1Ai7zJeML2N_RgGH1X9vGCsOIS6vW7uFAWmPbDF4qXA0ltKZU_tozw4As0Y_Xlw0iL5C8lIujbxZc9V5D2PTkdhXZOVBOG0hPfhfCwOTXtb2gFEF3TMGq8rgb1HXJ1x__MoWK3VGaCwRQcRLX8UEXE9mh2Swwk0Iq3jlJ8rfD0gnM4l3kYfcNkNsFDDxlorQWwUAVoZgQYQHQ8Icfr0h0QDgylGEw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">▶️
بازی‌های‌جذاااااب
لیگ قهرمانان اروپا
رو با آپشن های تخصصی در
MelBet
پیشبینی کنید!
🆕
💵
امکان شارژ
کارت بکارت
و
هات ووچر
🎁
قرعه کشی و آفر های جذاب با جوایز ویژه
🌐
دانلود مستقیم اپلیکیشن اندروید
🤝
اسپانسر رسمی لالیگا
🇮🇷
پشتیبانی از زبان فارسی
✍️
حرفه ای،مطمئن و درکلاس جهانی پیشبینی کنید!
برای ورود بسایت فیلترشکن خود را خاموش کنید!
‌
🌐
Link
🔜
MelBet1.net
🌐
‌
Link
🔜
MelBet1.net</div>
<div class="tg-footer">👁️ 33K · <a href="https://t.me/persiana_Soccer/29425" target="_blank">📅 12:11 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29424">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/A74iCNTV-MAoh391GlnPrObsX4cFi-uy42hfprpbIXwfUYIB2lqOZs3Vv_J9nVMEWk1TBSirTNf81vs0xa43fDR49r_EvB2o72PyWcHoureKJFFK6c9gbRt825wIbw7eA8gEn3QQLjxmdPMxPE3UsRDc4_SA2pboukHtbSp_YfPhVGObnjnnXOtxCXFCEWGMzeHHYMdIHJZxUSliW11m3IlzCKxDSOjdCiZYg_wlTVgcpxqyuxGPZ2kShez6LJQnNOXsDBR3Ft_1VO4mU5g_9necNfj-aWzV762YBoYKZXk7MvnXrN_HUwZxnrZmnqAt0VnXhpe8rWT9vjftRtBVwg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
ترکیب احتمالی استقلال برای دیدار امروز با پیکان: حبیب‌فرعباسی، روزبه چشمی، آشورماتف، سامان فلاح، حسین گودرزی، سامان تورانیان، امیر محمد رزاقی نیا، اسماعیل قلی زاده، یاسر آسانی، حسین اسلامی و سحر خیزان؛ ساعت 19:00.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 36.6K · <a href="https://t.me/persiana_Soccer/29424" target="_blank">📅 11:45 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29422">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/p98d0E0GkTFWnh_NkiblGxMnDhCv50lLxmokBcDe2NgHwolHWmSJPjhz4dx2uHx1QfAz-6P5gX0fVJceEEWjpdTP9Sqzojm0h8xOKvH1m-zLLKw-hJ0fqIIl3E9gEsDYGobmJKvO_m1FgK6TXNVg1ankqUhSBjoBzyiCM8uQWW61_EGu_oMGj_tbP1ZRBA2cAWlz18WEjsz-fS0_0Zi2RxK1NrFPgJiWWRhXqxJM6kKWuTR-kqoX3PAcXwTNgEq5gvhGq6SYOM2ATkObJP0YR_0-yGwOh0ikWeU_aMF6H3IbIjyaPKqzOzCMNFOjE7favYK4uZR-O3bWrbNuPEGIww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/bIEymmlid3Xb1ukcY_Neh3QLuQVwAlPlQS8cU1pQQ4mtU2TBrT4_w_2lL34cPjGs3LP3XT5vf-MZ_e3YOsZjvTjkyW-r2Zc_zGY2p1jWFsUFhTC40QdWAhnzB2YdSAFFRqxIPwt921nGIE1b_mQXqOusHaYmv8kb5HQqF_eDVInyTZSJkzKg8AzXsOoi8eCFKlqH8Oh06-okzvYflFhl2FXnYmu5MadvtYenfIBP-nNK3-fBF5RHIur-w2SWq6akDCDYdLXy2oSpkB83eaSO3OOdFoUHEcFt2UK8G26rrjEGqrHbWhT-8BtC3I-umu5BmXEUOMa6hDOQ-3-KNDbIxA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">⚪️
🇹🇷
روزی‌ روزگاری آردا گولر به‌ این شکل با رونالدو وارد زمین میشد الان دیگه شده فوق ستاره رئال مادرید. رونالدو در مصاحبه اخیر خود گفته آردا پتانسیل این رو داره یه روزی توپ طلای فوتبال جهان رو از آن خود کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 37K · <a href="https://t.me/persiana_Soccer/29422" target="_blank">📅 11:27 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29421">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/e1mh3nqaD_h2mRyyA_Puz7zmvBCKSkyL6j68WYYMXCdT4tf081lwgyWxee0WZLqswMeU5T4b6u-PeWarULbwMWcD3jscfgmv22FG4IPo0MLM-Zv0v9-_lTWyMslO23dj0RZmO6e47ItzzamyZe9Iw-vGnX0fwToxjuoOZGa5PiqZ8E47yF6rQZhwp7bbT0jI3_Xvpz0mvHiJu6sOKOZAvZ8bwN-dS0j8QmpRQSi8YH0p256UnpEYoIvyKT9ECYZzvVEUn8HSTQqlrhu3lgexlwl0sXGgBj4gcWkMletUafCTKi5mgnFcoVkB7hDfvlOsVz_NS_PZvHBO8JQh8mxGTg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
ترکیب احتمالی استقلال برای دیدار امروز با پیکان:
حبیب‌فرعباسی، روزبه چشمی، آشورماتف، سامان فلاح، حسین گودرزی، سامان تورانیان، امیر محمد رزاقی نیا، اسماعیل قلی زاده، یاسر آسانی، حسین اسلامی و سحر خیزان؛ ساعت 19:00.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.6K · <a href="https://t.me/persiana_Soccer/29421" target="_blank">📅 10:39 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29420">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/05d0b23c5d.mp4?token=eQOrIzhnullDwrEXhrCOIE001Hpr6RH7ItS9ZLDA6XNECLT8KjaAvR-wxmBQGO0Qtq6BwoQ59xVlaCpxEN-dtjmbbKpf3wokACwhZRuTZIqQAD3WR7FRSmnhmTgnqgCDqqGdbEpRq3l5_8LW-GiVLkqeCkU3tXhYUHo0aodczuv37zKhOBzt2MT6OX3sA-9d5MohY5N4_bG9kZbaAsDF4IReLZYptXR66nUt-0eqMpwyKNaRrGVol_Pj4ZWu9TLJLAUf26-f8BbfT-5ZxQ-pyu8Mj6Q3o49zjZ7Ax-Mi23Pzt0zYZA5HbuE0uEUgUKmxnxN30pM4ryIKgmldMeopbTOpIKamrhBUzl3Y1pN15yo_auaNjk1xRjoH1DYyGQejl1EJiM4qt9a0EApmWK3SHVVU-nOWETwVQbTmD8z_ZIkPsYyfbhgIamgSVMrXvmOutUsTGnOFFUPF1dD9EbU0Ylz4bf4fGAaWUrOKkHjUjXYB3E_bUlidRazaWRblgp4QzDH_TWDRRVE24HtR8P6rJl9MRE7y652qZyh8CA6i6937nhdtuejGaUpxpA3RgNf9vBPS1SiB_bd48Q7UV6YN9gNW4J99UH7r1EljyK-GLf_R3qe0xJL1MFKeeJiKiwv1ZPqBhCAzP8QMGhU6KJ30Z8tERjzQ9b9Yjj86QPaHHKU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/05d0b23c5d.mp4?token=eQOrIzhnullDwrEXhrCOIE001Hpr6RH7ItS9ZLDA6XNECLT8KjaAvR-wxmBQGO0Qtq6BwoQ59xVlaCpxEN-dtjmbbKpf3wokACwhZRuTZIqQAD3WR7FRSmnhmTgnqgCDqqGdbEpRq3l5_8LW-GiVLkqeCkU3tXhYUHo0aodczuv37zKhOBzt2MT6OX3sA-9d5MohY5N4_bG9kZbaAsDF4IReLZYptXR66nUt-0eqMpwyKNaRrGVol_Pj4ZWu9TLJLAUf26-f8BbfT-5ZxQ-pyu8Mj6Q3o49zjZ7Ax-Mi23Pzt0zYZA5HbuE0uEUgUKmxnxN30pM4ryIKgmldMeopbTOpIKamrhBUzl3Y1pN15yo_auaNjk1xRjoH1DYyGQejl1EJiM4qt9a0EApmWK3SHVVU-nOWETwVQbTmD8z_ZIkPsYyfbhgIamgSVMrXvmOutUsTGnOFFUPF1dD9EbU0Ylz4bf4fGAaWUrOKkHjUjXYB3E_bUlidRazaWRblgp4QzDH_TWDRRVE24HtR8P6rJl9MRE7y652qZyh8CA6i6937nhdtuejGaUpxpA3RgNf9vBPS1SiB_bd48Q7UV6YN9gNW4J99UH7r1EljyK-GLf_R3qe0xJL1MFKeeJiKiwv1ZPqBhCAzP8QMGhU6KJ30Z8tERjzQ9b9Yjj86QPaHHKU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🍏
تقویت فوق العاده باتری آیفون در سری جدید آیفون 18 پرو و آیفون 18 پرومکس. قیمت آیفون 18پرو: 1.199 دلار حدود ۲۸۰ میلیون تومان آیفون 18پرومکس : 1.299 دلار حدود ۳۰۰ میلیون‌تومان.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.2K · <a href="https://t.me/persiana_Soccer/29420" target="_blank">📅 10:18 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29419">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/573430f5b6.mp4?token=dbjkSNAubcj4rLbnMCO5L8wptFyPdicr_4UE_4ng1_zukBfBKynKHZPqLrfKPLSMSzNzrwF58tyOd4yryALqop48EIRm9DYa1rloDOikXIHCkTuiwlXzvO0QvQYMsiQSF8Ls2UkdIHT71ZPsAMabFscZlBMnk_qdpni7TC1vFiFEuCK35EQFNLheD6h8sD8Ac0hSy9AM_OxHP1NrsmYrvmF4qMZoZz_rU41i9SQ_dl0MgdW-SMMpKj5nbKSvlmq_eH72hKUf-viBwIEQaNPs06UokTflCWzLhAl6UtLUlRocfZR46eExT9RLmhyMuh6mYzgYy96RoQOMLH5I3u3CCg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/573430f5b6.mp4?token=dbjkSNAubcj4rLbnMCO5L8wptFyPdicr_4UE_4ng1_zukBfBKynKHZPqLrfKPLSMSzNzrwF58tyOd4yryALqop48EIRm9DYa1rloDOikXIHCkTuiwlXzvO0QvQYMsiQSF8Ls2UkdIHT71ZPsAMabFscZlBMnk_qdpni7TC1vFiFEuCK35EQFNLheD6h8sD8Ac0hSy9AM_OxHP1NrsmYrvmF4qMZoZz_rU41i9SQ_dl0MgdW-SMMpKj5nbKSvlmq_eH72hKUf-viBwIEQaNPs06UokTflCWzLhAl6UtLUlRocfZR46eExT9RLmhyMuh6mYzgYy96RoQOMLH5I3u3CCg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
#فکت؛ برای اولین بار از فصل 2017/18 و بعد از 9 سال، ایران هیچ بازیکنی تو لیگ قهرمانان اروپا و پنج لیگ معتبر و جذاب فوتبال اروپا نداره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.3K · <a href="https://t.me/persiana_Soccer/29419" target="_blank">📅 10:10 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29418">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Goc3Xxzymz5AeTHhn9uYbiPy4WmKsyIlKjhz-PjvNuLfQhLDhMox6_EO7-WkOYu1Mr1iXg0MtlZha_JMTPkDkJ5swOzj65mYlkveoTTNqrLmcowooVmupQ3NBhBjoyNPJftsGnxZhxJlXnro7BwTbb0LPklE1MSpZfnZZUL1O8t7DwrkQXb4QeS89aerBrKgXBnCsLGz2xMhxjuqp-gu4HjbvgSiWboBZ63zY7Mb5ItKpX4GUsH7JRq7ijD8BDmLf0LCgNgDIZXyXSoRAotTalNLzoO9s09Eg7_vPKnyBNRnVbT__F2lQOIk8p48rLFToQjmF25eUP9_m7qNZbQ8kA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
باشگاه پرسپولیس تا این لحظه هیچ درخواستی برای لغو دیدار مقابل خیبر خرم‌آباد ارائه نکرده‌اند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.4K · <a href="https://t.me/persiana_Soccer/29418" target="_blank">📅 10:01 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29417">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/58d9326281.mp4?token=NLL5SCVvKUFw-_-76ddiWXcBOnBi5poLBx89IzrjRG-WFvT9hYJTjPl_Q2DUoT-wjkkOWbTiRVMgZu-FFK9MB03xoQqyN_Nlhnk7xZZVUND223JAxs8BfDZhtUws1yx-y25zjSkD3A-8CnMAar3mMFTKDqfwkAMnP5lsXrt9OniaXC0RAEO6kVwHayu5oeUTYYaG4NNNiaPWExFKsNyRM9FxV6R6VzGraradCN3JnOa9TZfoZ_mOrC4ohEEPqCuW-Ml0lzt0IOJ4qQlTHRKTpL-Wlmy-8gAO1b5gR8iVYE32qPVUOxTNu1Ln2aPOTzcFh2Kusdd1iH-YQJPj5HRGng" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/58d9326281.mp4?token=NLL5SCVvKUFw-_-76ddiWXcBOnBi5poLBx89IzrjRG-WFvT9hYJTjPl_Q2DUoT-wjkkOWbTiRVMgZu-FFK9MB03xoQqyN_Nlhnk7xZZVUND223JAxs8BfDZhtUws1yx-y25zjSkD3A-8CnMAar3mMFTKDqfwkAMnP5lsXrt9OniaXC0RAEO6kVwHayu5oeUTYYaG4NNNiaPWExFKsNyRM9FxV6R6VzGraradCN3JnOa9TZfoZ_mOrC4ohEEPqCuW-Ml0lzt0IOJ4qQlTHRKTpL-Wlmy-8gAO1b5gR8iVYE32qPVUOxTNu1Ln2aPOTzcFh2Kusdd1iH-YQJPj5HRGng" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🟣
🇦🇷
در شب گلزنی کاسمیرو و لوئیز سوارز برای اینترمیامی؛ این آتلانتایونایتد در لیگ MLS دو بر دو متوقف شد. لیونل‌مسی فوق‌ستاره میامی 422 امین پاس گل کل دوران حرفه‌ای خود را به ثبت رساند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.8K · <a href="https://t.me/persiana_Soccer/29417" target="_blank">📅 09:52 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29413">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lhWWOEWUl0wFlU1cHJ33TRZB9tN8FeCFRuDVYvDUxZFz5VBuyXNr2hqFg1gMaJZD8X8JU9vBHIaOQTWuPE-UGlg-l1e2J5VIhHfEyqBymKOLeV52sWjqe1GntwXDoSjcc4SZgt-h4at8QJzGwklOIqJBmf3aAt8_Kl69dKu5g9nOAIf6a0Pqok19Ax1b3QqgwgbO-qfeCKTrUBHLfWduVnI8qf_wwqYqyj1feuRB0pqEI_vIEjDn1Z_w38h2jEjLCx1tW1RG41And_dp7_tGssabpj3-_MramvCxY4K9YwS_i2foLdKHS3XIMPWa2czoEStJGLgyY1KO3FsHZpvXiQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
آیفون ۱۸ پرو رسماً ۱۸ شهریور معرفی میشود
‼️
اپل با انتشار دعوت‌نامه‌ای رسماً اعلام کرد که در تاریخ ۱۸ شهریور ساعت ۲۰:۳۰ شب به وقت ایران رویدادی برای معرفی محصولات جدید خود برگزار می‌کند. انتظار می‌رود در این رویداد علاوه‌بر آیفون ۱۸ پرو و ۱۸ پرو مکس، شاهد…</div>
<div class="tg-footer">👁️ 71K · <a href="https://t.me/persiana_Soccer/29413" target="_blank">📅 01:48 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29411">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mUu-SG__aIE-gZth5H5vhVU0TluQFP__O8qtmXKF9ujQSoSJOUF9XdjzkHdBw16FMZUtX6EVpDhpAjnSIAy5xbcrrHs3PQk9qPTxjaXKaH6B90wXPTlap6PfyaBp_yP4C8LX2xNhSixEDuiv6UeIKVTz91Ocng4flkyhv7a7kFaBhPHgT9VcKh0fve4VrGTJL5l5z3pck3l-s5M3JXCSoG-qZqT82ndM1oKUR2ao1wjW2jA2KoJqrvIBzQzRMyNzjK49xUScSuKBTuy5VfaFcGuxS-EKiA-LcCBYZht_nb4E2QB4iCpyP6IVyE-3x7ph-3NbG9s_ZQf8bwBVHdsp6A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
طبق‌شنیده‌های‌رسانه‌پرشیانا؛ شهاب زاهدی مورد توجه چندباشگاه‌لیگ‌برتری قرار گرفته و احتمال اینکه در نیم فصل به لیگ برتر بازگردد وجود دارد. به زودی اطلاعات دقیق‌تری در این باره خواهیم گفت. حتی شنیدیم ممکنه زاهدی در نیم فصل یاغی بشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 68.1K · <a href="https://t.me/persiana_Soccer/29411" target="_blank">📅 01:30 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29410">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1208f58f58.mp4?token=Iu0hNR6vg9kzMmEBcxfyln6nARfm92Y0pkiSUfn3iDcizoVrqiiL7y9n3rW5W4Kyw9VgFOfefsCpb8fTDDs3_vcDuCdQOdQDx7ZPBbUaCyJQqfFWObOqL9aK1QX8xDOwGshO82gMAKAKkMp9mljeQMa1QlQfVk2uZMrPyuh_krZd9T7kP7k4Rdtvf_UXTZD4xZX_dkhGi2pLOZDKcQO85X5gepuOPEuDccJZt2YfKt99AXQJ-kyMzDHjuz5ZurY9S_g02GuMC95n3yF9qXHv3CYgiubdvFPzwFPERiqBNz-pPRforO0Iu7tDQkFydrWXT15NHmeuNFdaS51plBU6MTaR4DZyawfDE_vUa55V3KCxBttCdCuJXP13in6tQsDv5oJU-198Dq_Lxxy2WSIMsp7nsuhePLAVRODLfU953ZeJHSIRNLQE8evT75azmMaEfcIo3RsV8Z4ofdCnlZQcuaAzFCwah-DvROfhogER3ulj5CYMR4Yt9griZcLJhKucnOYabht1O0yDm-QBAGGOOZOTWZs7wUtUe8U9ouOyOs1trOpR0-hJM1r-fayArrg8jczFd7zyNM_SDlkHcqcoHkp-I2zWUDF01vmcJFwHwheIo1wkhKURMpF9CgovP4VwQdCVUyG5fH8zzB1_xWeAI22UyzpQODuNf7eyPFKs0Ag" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1208f58f58.mp4?token=Iu0hNR6vg9kzMmEBcxfyln6nARfm92Y0pkiSUfn3iDcizoVrqiiL7y9n3rW5W4Kyw9VgFOfefsCpb8fTDDs3_vcDuCdQOdQDx7ZPBbUaCyJQqfFWObOqL9aK1QX8xDOwGshO82gMAKAKkMp9mljeQMa1QlQfVk2uZMrPyuh_krZd9T7kP7k4Rdtvf_UXTZD4xZX_dkhGi2pLOZDKcQO85X5gepuOPEuDccJZt2YfKt99AXQJ-kyMzDHjuz5ZurY9S_g02GuMC95n3yF9qXHv3CYgiubdvFPzwFPERiqBNz-pPRforO0Iu7tDQkFydrWXT15NHmeuNFdaS51plBU6MTaR4DZyawfDE_vUa55V3KCxBttCdCuJXP13in6tQsDv5oJU-198Dq_Lxxy2WSIMsp7nsuhePLAVRODLfU953ZeJHSIRNLQE8evT75azmMaEfcIo3RsV8Z4ofdCnlZQcuaAzFCwah-DvROfhogER3ulj5CYMR4Yt9griZcLJhKucnOYabht1O0yDm-QBAGGOOZOTWZs7wUtUe8U9ouOyOs1trOpR0-hJM1r-fayArrg8jczFd7zyNM_SDlkHcqcoHkp-I2zWUDF01vmcJFwHwheIo1wkhKURMpF9CgovP4VwQdCVUyG5fH8zzB1_xWeAI22UyzpQODuNf7eyPFKs0Ag" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
درمرحله‌سوم‌جام‌اتحادیه‌انگلیس؛شاگردان ژابی آلونسو درحالی دو برصفر از لیدز یونایتد عقب بودند در نهایت به پیروزی پرگل شش بر سه رسیدند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 84.3K · <a href="https://t.me/persiana_Soccer/29410" target="_blank">📅 01:17 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29409">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NGCWzH7L_xJyFpkNsFfazWxQHPa7VkzZ24heOIuwt8M3sAw6YqbKhu6qRJ2V9oVp0vJg_MWHC9YkhK0C9aMzBsP2HF83fDjjYsrLqQEwkmMMBnliiXM9Mj7x6TpH_z6BJAniNRwlkIKxEDpKjeT8cSxjZYQF2kLDPDv5bk-iwodkVHncLIDeshnJApdL527oRyw_LtSlig0spnZPMhmg8zgr5GDkSez2lCEcmdTqqcl5y-4aC65g0yyGBmWWveY6Wdz2FPl8ff0INzbOKP_QSe6w6X8SEfS0aTWjE-6hL6sjWygKkjxtrjnvWr1F15VGPIXgv1CTq3Ci_vK_kZ-8wA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
🇮🇷
#تکمیلی؛درباره محمد قربانی چون در لیست مهدی تارتار قرار داره باشگاه‌پرسپولیس در نیم فصل بار دیگر برای جذب او اقدام خواهد کرد. رقم تعیین شده برای‌ رضایت‌ نامه قربانی 1.2 میلیون دلاره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 86.6K · <a href="https://t.me/persiana_Soccer/29409" target="_blank">📅 01:03 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29407">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/t4ZKIsbwe1XKsWFg7jzO_X0XbLRNPtIe3xIO69bMaWAMCSB8DR9QajUDy0IOFK4Yi7EJRdqbR1PCARYUnUPtUR3NV6zRCLyuHrEjzV2CejSRRa1q2koPjYh61MNSfduqD4UODwzQVscownnFdU21JktVpZ3LuNcOy1IXCc3vKMSUrMrJf-mcBfnUVeAnMtAwHLk5pG5LATVW4M9kCYaorN8L_Ah5AnXeUrNc1AR6FcLH9ry5Zn2algkSUegEE3ajnXpaUUlLjdW3reQgLebXaKdPfzUrisiPyO1muu1nvFAkjqL0zdgnW3aNf93_6vgIoAb77-7KZNz55o_4i0Fwmg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌‌‌‌‌دیدارها‌ی‌‌‌‌‌امروز
؛جدال آبی‌ها با پیکان و نبرد یاران کمپانی باپدیده‌نروژی‌فصل گذشته چمپیونزلیگ
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 84.6K · <a href="https://t.me/persiana_Soccer/29407" target="_blank">📅 00:58 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29406">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jgJMa_nXMuYw1vUDGPH6EK6qZZ3jl4Yu67QizZaZ3_DwhWUnxzu9rejkblV7yu3GRnWiuf8cbdELkb4r7WxZs3115awxkT1_7_XC1GCQlCX0FimMwwnHBM90NqGW2Ac79u4CFqJOepKR-z0DL9P9L0vV7cKB264r-CT2AT3AX9_2kRFX112G6NApVWdp00cIPI1WbPQnef7MGDvJ0LABbg06hAETnI9LcRKEjIHetvb-uvkAY5zpqkAo7PlnIrHxk-mPDov8XqEjbUsGA7AP1S3_NVvVxZl8MD4GYFOKjD975YbO5ZxK6oKSGl0GkBKuMsX1vkbW64wTj-fKhokaYw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج‌‌‌‌‌دیدارهای‌‌‌‌دیروز؛
ازبردارزشمندلیورپولی‌ها در آنفیلد تا آتش‌بازی بارسلونا و پاری‌سن‌ژرمن مقابل رقبا
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 66.8K · <a href="https://t.me/persiana_Soccer/29406" target="_blank">📅 00:57 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29405">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MWPJMiQd8TszbfIPpxRtijPXHOcmvx3ABt2mmVH3Nt63eTd4juZBBCLxQzLH4rWF5kbmeuMTUHFRD_c174UNuxogUlaSXTLUR1AA-b-6dO5Sy4ViXxZkH1ysK6x1XC_z1VRNtkFhEjTZTBS3SACwB_txzR92jarMEdqdi6lfj8wP35lkNGrcqICueJfN8IupOKWg4rcAIOd8onvFLPINT8M8fMxRRmkC21asou3_u68E3d1cfTweQahYie1BbwjqsDsy5Kmb2Nis_z-0vobl_b7hjOlHawW5iyydmP9fi8ge6KaNMJujyZVd2AtpFTLXo2eZz7mcN8djM6id3DAbtQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
درمرحله‌سوم‌جام‌اتحادیه‌انگلیس؛
شاگردان ژابی آلونسو درحالی دو برصفر از لیدز یونایتد عقب بودند در نهایت به پیروزی پرگل شش بر سه رسیدند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.3K · <a href="https://t.me/persiana_Soccer/29405" target="_blank">📅 00:45 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29404">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">🇪🇺
نتیجه کامل دیدار‌های امشب هفته نخست لیگ قهرمانان اروپا؛ از آتش‌بازی آبی‌اناری‌ها در نیوکمپ تا پیروزی ارزشمند آرسنال در ایتالیا وبرتری لیورپول و پاری‌سن ژرمن مقابل رقبای خود درگام‌اول رقابت‌ها.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.8K · <a href="https://t.me/persiana_Soccer/29404" target="_blank">📅 00:40 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29403">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PdOzZ_tu4DrFt8nHj8-kxfNRh5qwajORmxfXIAIoDVkToiwP3SJGWeSOe_7nXVv_eARkTDtgl_SMSje6p_h74w99S_H2WV8m2oFGLC1Xk4tqdqw52SCUmsA-I9dKJsvO6CcH5L6ZIRmfDhJre43lQY2d0bL7V7PHmvHQlrHFDy6kFbRpPSACc859GRnmWkxRQrX3CMHprGFtb-G4_GrN3rzafvqgymF6peYHTdKb1gRcKh6dBAfjd7qNB6bVDNJ4T3x8OXg6tixFgrOX1KdSP6WaFZsPsqZ0Jo3hzZL0xqwF8IXVa670FVy3dvWdO4GWve5exaeucyPpneBNmxaKLw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇺
هفته اول لیگ قهرمانان اروپا؛ شماتیک ترکیب آرسنال و ناپولی و شماتیک‌ترکیب اتلتیکو و لیورپول؛ خولیان الوارز بالاخره در ترکیب اتلتیکو فیکس شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.5K · <a href="https://t.me/persiana_Soccer/29403" target="_blank">📅 00:34 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29402">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hllMlVLKMf-_x-FiByp_kQEgnkHRaWAXn4wzyDzX6C4nFp0W5-RnYcwL51FXBx4ovvlbD9GKEJAZOwaDEx8H-hybhGVcWlR-tBn2e92Eh-3x5K5s6bRsUcrcXo0BozOBkJRlj37JVK7B_wXmGPASXm4Hn0l0XLmcaVMIA4PeH7AA4uUMUvRIhvfoQ03QLHhut9gv8ydCYF0Pn1ujG4JVu9tPQjdUY4tfx7njIqcJUuUCWTCNTXaMVT-zwV04x7kjCVx_IZzobuVTvnQzCwCoqyfxm-5Tjy1eZjgSFLHTRtF7KGmTS8HLqIgSLgFWykDzWyuDv3McwG6gygkv1pHYvw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇪🇸
🇳🇴
#تکمیلی؛ باشگاه منچسترسیتی انگلیس برای‌فروش ارلینگ‌هالند ستاره‌نروژی 26 ساله خود در تابستان سال‌آینده 200 میلیون یورو میخواهد. از بین دوباشگاه بارسلونا و رئال مادرید هرکدوم این مبلغ رو پرداخت کنند بند فسخ هالند فعال خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50K · <a href="https://t.me/persiana_Soccer/29402" target="_blank">📅 00:08 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29401">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eZ398qbo-C1PneaLxriVTRaICgBggE1het8uYgAlh7c-Y_zNqZj6aVDb8HeXnk_4M_kisUS4fLE3-sn9m_6ZTXHE8_rgRFIoVzNsI0G5klpxv7-6xEr8HKO8EF7ozVAT5SXd63MG_uOWIOjEMOAV3SA6GWVIPpSOYm3h6Nagjc2F9qi8DKURyYf-MrK-fkJuJBPwtDn8MW9blmN7k-wN72CZY4MfQY_J68zT7UguJxJVpsShxyhcfMWt7HrCFmVScH7me9JwDm3tuGIk7N7mzjU2zfNTZk1zoumgN9Xroyxfn--m-2SVHpg6P3c4yhmhTmAhJ-Dxi1epv3RLr6lRHA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🇳🇴
طبق گفته اکثر رسانه‌ ها؛ این آخرین فصل حضور ارلینگ هالند در باشگاه منچسترسیتی و لیگ جزیره خواهد بود و در پایان فصل راهی یکی از دو باشگاه رئال مادرید یا بارسلونا خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.2K · <a href="https://t.me/persiana_Soccer/29401" target="_blank">📅 00:02 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29400">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/39a8082900.mp4?token=vOB7Z1uzXphqy3T5Hv4wHUorgVBjE0BVTUa0XoNhx-B_zHTOa8kXusXSIKRu6dDO8YdPQ_-5wwZ_4tCReGAxNS3nfGbT652ls8CpMFnqV6wn1d7TfgWPXNMhyVyfNEW9pENUkNGDlYTiJ_cupof_VehFCvBzDltn-84EkVoZudiLf6mIUN9mAo7q-k9Nj73uWr-YfKMrdzmbgrfrDq5LYF2bL7vx7ZnLViVnWRRZSpsONMgSNATlhjxek8Q-yAguMJkmhyfsMVdj8D_eWHqk10trLcjKhyStd-2MH95J2yqTeneZFgfRs2pD4ifmE3JZH-9Bdxw_Oi2Cq9Fdjw0gFQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/39a8082900.mp4?token=vOB7Z1uzXphqy3T5Hv4wHUorgVBjE0BVTUa0XoNhx-B_zHTOa8kXusXSIKRu6dDO8YdPQ_-5wwZ_4tCReGAxNS3nfGbT652ls8CpMFnqV6wn1d7TfgWPXNMhyVyfNEW9pENUkNGDlYTiJ_cupof_VehFCvBzDltn-84EkVoZudiLf6mIUN9mAo7q-k9Nj73uWr-YfKMrdzmbgrfrDq5LYF2bL7vx7ZnLViVnWRRZSpsONMgSNATlhjxek8Q-yAguMJkmhyfsMVdj8D_eWHqk10trLcjKhyStd-2MH95J2yqTeneZFgfRs2pD4ifmE3JZH-9Bdxw_Oi2Cq9Fdjw0gFQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
ماجرای‌ازدواج‌محمدپروین‌باآناهیتا درگاهی عمه دنیس اکرت مهاجم ملی پوش استاندارد لیژ از زبان داماد سابق علی پروین: پروین بشدت مخالف بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.5K · <a href="https://t.me/persiana_Soccer/29400" target="_blank">📅 23:40 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29399">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hjQiIH5mlgQYBMt0ScIgLWsDe13K6AO14VAIYrnvUYvuOLgyQaefFUs70O6zhSPbJVDVS9yK2-qXDIjl79_17mjAT_9pf-jY2_mdmYDR1gSrO4QMnfFBRdWHVddqoEi5FJaH6xywL3VotzL_FRILIVZ6FXd20oyrzgIRGE4K7BJrvWJtH5dHjg-zVFWWLbmlkJVOmTpbu0tJy5p5U8LXmtKcKDheJz3TxzFECKj4vNYzbPdxIu_WcMXJR6V7IWfhGyTJxjASyWjkjhBme0sW1A9K3gksWMI3hYrKDMfwCmw7kjqHHQHLG723OAXg7lmGIvkzIxwZEcIrtNEZkyUIbg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🤩
#فکت؛ رافینیا دیاز با گلزنی مقابل فاینورد تبدیل به اولین بازیکن تاریخ بارسلونا شد که در پنج بازی اول فصل برای این تیم گلزنی میکند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.8K · <a href="https://t.me/persiana_Soccer/29399" target="_blank">📅 23:27 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29398">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/O2rzAfCjsG5MTE7iVIuMbJBQhggtPW1O4RyFTp9NVl7Zr58PbzK-hF49wcMtBCYnGZcwG__b9zWaEWt0d6t8L3E0dSvCld8v_LwR_pfHgiWM2Qy0NUzjrkA05G6HXcIQTyrFJJAqGZwfyKfBGtO5FXsSjhLl0PyqagkIl4UeNZpkSIpRHVnPIMnvbJxaNa6GtrSKMKiZgGU22gckW2njvSU81d9l-VuAHN2oLj8LG8T8PlGG-Ex4pn_MQQuzBtuJxZIKmQp1I_yqF2nS1QuVlLgt2ADOCw-sCWmiGLdxl-Z05776fo7CdApMO3S6Iz5Zq6PvPK3E-urEghlqZBKn4Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
#تکمیلی؛ لژیونرهای ایرانی حاضر در اروپا:
‼️
علی‌رضا جهانبخش: اکسلسیور هلند؛ الهیار صیاد منش و علی قلی‌زاده: لخ پوزنان لهستان؛ محمدجواد حسین‌نژاد: ریوه آوه پرتغال؛ میلاد محمدی: ویتبسک بلاروس: نادر محمدی: دسته دو فوتبال روسیه
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.4K · <a href="https://t.me/persiana_Soccer/29398" target="_blank">📅 23:04 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29397">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TidER_c3xPHfKbffVsEegA7VQJWYiYwj7j6SV6nT7h2fz-ERFsyFV9FUyNVlVJOXkGvYOHgBoXzo5c42w3ll5NAZV6E1HerOf3qtiwndM2TX_C3iHBlsKU6059UV-OBqriVODjvpWzturYaMzwB1LF1Wwq-EvlR76cAgQfebfTvWFHvV8tCw3Zu9NcoSn578eLk_bPX-AWny1FU4Z9nNltWll3Uzp8xIwE2rhjH7JNEg-f-6NmOrpUAI-VX5orF21qKu_iYuHiGC_R4VQALCQKzyDKBLSCQUvbJXGX40rT5TLqMPfNRrFLnEgfw4IVYAY6G8NRXBbU6Bq3lOw-SPmA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
👤
نتایج درخشان و خیره کننده بارسلونا مدل هانسی فلیک در این فصل: 5 مسابقه، 5 پیروزی، 22 گل زده، 5 گل خورده، میانگین نمره 9.3 از فوتموب.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.1K · <a href="https://t.me/persiana_Soccer/29397" target="_blank">📅 22:47 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29396">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iGZIpEL-VDVj3Pq2vYWP9HJ1oqpWvJv4CHNdSr-4ysAIy9Oa63q9TIE8vtz4axHFOQW7aoMVs2Iyjar0mIc5t3G7kTUB-xe1dhHHhMGqqz7LhF5PPB_xYtgRY0PujYBRRitt7NONjpTlezPti67rfo1KU_NM0mWopxpbdmN3474bjxeS2r0z5WlV6NXj7xEzdSFi8kLjXqyn1U9cDJfY9bU3TtKnDsFOEZgZ0lGGzOGyPOZnDngtrY8E_iZn3pFrJpRggpm71merN2IKWZu8MUtc8jpothO4cpgqpPVoB9HGg2qsBdzfSLFzTrNqLnq1KfiY2ZmoBzYA73I93fkDZw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇺
🇪🇸
در هفته اول چمپونزلیگ؛ شاگردان هانسی فلیک درنیوکمپ آتش‌بازی راه انداختن و با نتیجه پر گل 5 بر 1 نماینده هلند رو شکست داد. 22 گل زده در 5 مسابقه؛ عملکرد استثتایی بارسای فلیک!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.3K · <a href="https://t.me/persiana_Soccer/29396" target="_blank">📅 22:34 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29395">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RHLyr7MHJbJ1qIQAujBe48Vjqbh--URTzYTL0xZUnvgPcvDNUf5ufP9xOMdvIX__7ORJvDC36knzndnP8e3vgnSPrZm-bCkcmtq_-FVhh-ZWB1BTBWkCX2cZCjIghEHOPiqyITmClNocEJeJiBwlueWdygwCpdPgJBWQkAeINLrp8-UO5Siaw8vs1EvnftqdV5wDgDpjaO31MaYWGasJwzfl1yGq9jITpBAU_HPgj-nz7dKpRYd7LnYSUgHAPw904hpxaRlEZWy_DD2hwkWO4onmVZ01cpeyGcbEatlJNExtPY00UqFxOZtE0dTg8fUw7wUHUi-i-nyuSFXPQGmnLA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇪🇸
کاشته تماشایی لامین یامال ستاره 19 ساله بارسا در بازی امشب آبی اناری‌ها مقابل فاینورد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61K · <a href="https://t.me/persiana_Soccer/29395" target="_blank">📅 22:12 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29394">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/adadb2bd3e.mp4?token=T7l72szkelI0BW_lmgAcvnGIl2K8hC3llM4Xnfyi97v1GelpWbM9c0ETlKeOBUX3biuhqraWAKTLSOekLN-DxveXoUpulqiA1CLzVyYNaABdaXplh8EpmqAxYwt68HEh2zI4xZDUzsphz19-Gec1V47vLaqHnI-Ks46ECYOlXtOVH7Dq0t1MJDk-pLs_9Zp3sCPkJ-R3irYR2BcXO2rvPYZga7-aof9dkK0P7bS0Bd9R4dotvrne_pg9gw0w-bQSxdXB7lQCIhc5jMr8khwymMMnW222CO5Q4t86bDph6uSuL-6qddgbOIs46a2Mb_8iYo4cXB68KmqXgwWLfOd50w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/adadb2bd3e.mp4?token=T7l72szkelI0BW_lmgAcvnGIl2K8hC3llM4Xnfyi97v1GelpWbM9c0ETlKeOBUX3biuhqraWAKTLSOekLN-DxveXoUpulqiA1CLzVyYNaABdaXplh8EpmqAxYwt68HEh2zI4xZDUzsphz19-Gec1V47vLaqHnI-Ks46ECYOlXtOVH7Dq0t1MJDk-pLs_9Zp3sCPkJ-R3irYR2BcXO2rvPYZga7-aof9dkK0P7bS0Bd9R4dotvrne_pg9gw0w-bQSxdXB7lQCIhc5jMr8khwymMMnW222CO5Q4t86bDph6uSuL-6qddgbOIs46a2Mb_8iYo4cXB68KmqXgwWLfOd50w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👤
👤
مقایسه‌عملکردکریس‌رونالدو
🆚
لیونل مسی به مناسبت قرارگرفتن لیونل مسی در لیست 30 نفر کاندیدای توپ طلا و غیبت عجیب کریس رونالدو!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.1K · <a href="https://t.me/persiana_Soccer/29394" target="_blank">📅 21:59 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29393">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/135ac654e4.mp4?token=fkDZ3p17jmBSMPE6-EKJ8PkQtVCl8dYNKK87XCIiXnEfUoOyRspnDuLv9IuFC3kiLDFQDfzLYb-aw-v5bfg-s1QaWhO1CrM8UJsIQN8NGbQQBKq56vsTXn40j8qLJ-DyvnpmKePOuq2tHF-JYVfLxLLUaMxvHb965Y-HCjja4lNCDlDMnsc-PlaNh7qQOfHF1NLyfl27_v-OdXIthGOKV_vxGkTSolVJqEVqrlFQhTX0frDnhCNUfsg6422xxGwafS1Bo4-Z0Vygbo3TBcpvhl9lTLTDUCbJpiF2VA8_ox_LToUMa1JrNa1oG_7hz3Lk6xtcF-BFcqflcmDvGqEKXA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/135ac654e4.mp4?token=fkDZ3p17jmBSMPE6-EKJ8PkQtVCl8dYNKK87XCIiXnEfUoOyRspnDuLv9IuFC3kiLDFQDfzLYb-aw-v5bfg-s1QaWhO1CrM8UJsIQN8NGbQQBKq56vsTXn40j8qLJ-DyvnpmKePOuq2tHF-JYVfLxLLUaMxvHb965Y-HCjja4lNCDlDMnsc-PlaNh7qQOfHF1NLyfl27_v-OdXIthGOKV_vxGkTSolVJqEVqrlFQhTX0frDnhCNUfsg6422xxGwafS1Bo4-Z0Vygbo3TBcpvhl9lTLTDUCbJpiF2VA8_ox_LToUMa1JrNa1oG_7hz3Lk6xtcF-BFcqflcmDvGqEKXA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇸
سوپرگل‌استثنایی کریم‌آدیمی ستاره 23 ساله تازه وارد بارسلونا در بازی امشب این تیم مقابل فاینورد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.1K · <a href="https://t.me/persiana_Soccer/29393" target="_blank">📅 21:56 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29392">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/K8GS55aZG-GnbfZbOHr_Ch7LvkkEs0c3gfs9rjrqv7srkdEuQu3-Zkj5rJa-XOcnSw8HkwJI5YzGrCmtLQhZRZmbsyvOLrubTFfAqfcwypH3EhtAgUi2Hpo3Mr5_7thaDQycAAXIaV7WmYX8Y9MgXBo_bDuG4hxi8xBhzRgBcVCjKsJXf1ADRGc5Sw18O5rSO_bpvRdWpHNMtlVB091JOi-mNNlKqoxjGfHg25tCiAZgfrwQHO6hldGK4hEKKWg9J75In7ZfnguidCUp3YAnvwyN_fqZPFfvQr9pIvRjA6cI1W1LHaMSZT5oBhJyeJpDzSpsBGVnYSWfkSSdE9Tnbg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇺
هفته اول لیگ قهرمانان اروپا؛
شماتیک ترکیب آرسنال و ناپولی و شماتیک‌ترکیب اتلتیکو و لیورپول؛ خولیان الوارز بالاخره در ترکیب اتلتیکو فیکس شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51K · <a href="https://t.me/persiana_Soccer/29392" target="_blank">📅 21:39 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29391">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3a9709bebc.mp4?token=BF3J8Tnw0hdHjDapINdzpT1va7Xis9NEiMJ04V_VcLMGDlZ03iB_S9JFlocSGHd50DDg_7N_d8bUCReNlflVPzt3doinSrJXbCK5c-D88IcOwG9Uhz2UDKWd57VEZVQQa6Q9uSfj5ItVjmvsTonipI_wETPj1TjoKz6Mc7a3dI5FJWMbjRKKeTCKjBx0VK-M0KjOS9PqlDjoV7fUMr4uodwsubThPlonZRuK8EH-P3BXQGt5by8qu2nGMf6mtQ4lGGfjBTfbRl4vigEkV5CjvcJPmENOJNvB0tQVxMcYcQn3DhDMRqF1N_dORqzUyUNWgcB96vlrPkZT0wC5bkTbrA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3a9709bebc.mp4?token=BF3J8Tnw0hdHjDapINdzpT1va7Xis9NEiMJ04V_VcLMGDlZ03iB_S9JFlocSGHd50DDg_7N_d8bUCReNlflVPzt3doinSrJXbCK5c-D88IcOwG9Uhz2UDKWd57VEZVQQa6Q9uSfj5ItVjmvsTonipI_wETPj1TjoKz6Mc7a3dI5FJWMbjRKKeTCKjBx0VK-M0KjOS9PqlDjoV7fUMr4uodwsubThPlonZRuK8EH-P3BXQGt5by8qu2nGMf6mtQ4lGGfjBTfbRl4vigEkV5CjvcJPmENOJNvB0tQVxMcYcQn3DhDMRqF1N_dORqzUyUNWgcB96vlrPkZT0wC5bkTbrA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
آرش فرزین دامادسابق علی‌پروین:
بعد از شش سال جدایی هنوزم لادن پروین رو دوست دارم! بت زدن ‌هام رو بازی‌های فوتبال باعث طلاقم شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52K · <a href="https://t.me/persiana_Soccer/29391" target="_blank">📅 21:10 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29390">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KymZFUbrAriaByXA6HRbB2yxl2fCCynpuMWCtp_CrHjaFwQ0glCANs3CsFxPdyfsiYm79X7voPa8l4O13jLvFqyvtCV3V-vsfC1FQWGEW2P0Rp6optd4RukkhfhPn6M_VsHeOPzmV2R4-KNShdrtoTNTkR3A5HovO2NRLnm4pMDfrpGeYBSzbnJuBkzDdCJNiPNvxpZzpeJF3Mf_F55a6gpv75EvlRN4daETf6jPmijkeMLhbNldqFCVHWWwi3hvRPI8w5GLVgJCNWy0FhpjVApuUeCP0_j_qwZo7Lnz_HfS6gAfmOReDP54iunSN8U7NBh7Hn5LHDzSq4tjkX-7Qg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇳🇴
پدر ارلینگ‌هالند ستاره‌نروژی منچسترسیتی: شاید روزی در آینده نچندان دور هالند رو در تیم رئال ببینیم. ممکن است اتفاقات هیجان انگیزی رخ بدهد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.4K · <a href="https://t.me/persiana_Soccer/29390" target="_blank">📅 20:53 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29389">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/448238a183.mp4?token=h1-qHpexxb8JLNBonNr579WJEIpt5LctTMGCa0wXe36hZhwVQhcaEsA1BWcv3ZGK3rBnLIRR20FzRv9MgCS0K1BTGG5MXHNE8vnmzJC997EOJwC3fSWL5QFgxY7biqXLsNF0QmyRE4rqlA51rPDba--rN6xYGmcqjThXn90WaFn0LcWxRHiRMj-J8AVoGER_0mxkEQVhzQ3SMpLiZL7skvMN6RjYEV3YImUx9bIlSXLd-sEQFq0OXux7lk8K61NhGds5u9s852Mr6an0vawzj1NcJiGszo8WyvwflKmWX3keH2u4yZ3htmEHgh6zOw_1nMXaqh-E70RlbGIE8SsSSA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/448238a183.mp4?token=h1-qHpexxb8JLNBonNr579WJEIpt5LctTMGCa0wXe36hZhwVQhcaEsA1BWcv3ZGK3rBnLIRR20FzRv9MgCS0K1BTGG5MXHNE8vnmzJC997EOJwC3fSWL5QFgxY7biqXLsNF0QmyRE4rqlA51rPDba--rN6xYGmcqjThXn90WaFn0LcWxRHiRMj-J8AVoGER_0mxkEQVhzQ3SMpLiZL7skvMN6RjYEV3YImUx9bIlSXLd-sEQFq0OXux7lk8K61NhGds5u9s852Mr6an0vawzj1NcJiGszo8WyvwflKmWX3keH2u4yZ3htmEHgh6zOw_1nMXaqh-E70RlbGIE8SsSSA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇺
هفته اول لیگ قهرمانان اروپا؛ شماتیک ترکیب بارسلونا برای دیدار مقابل فاینورد؛ ساعت 20:15
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.7K · <a href="https://t.me/persiana_Soccer/29389" target="_blank">📅 20:42 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29388">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">🔴
#تکمیلی؛ پیج معروف 433 سه پاس گل دیدنی نادر محمدی باپرتاب‌اوت دراین‌فصل رو پست‌کرده و میکل آرتتا روهم تگ خورده که این بازیکن رو بخر.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.9K · <a href="https://t.me/persiana_Soccer/29388" target="_blank">📅 20:34 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29387">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kWNQ9HmL8e0_w-vX-WyZOuWkyiLOHFQqDhzXdIsh0ceQ4-H44jr0l8zul8DuxXnW0w7e1tLZgegsCVpycd2pRQ-OuwxKt1V_KYx1pZZfzDCZtZmqL7mybHun8b2U9Y4ceNP50kaYie7r3E1wfsHdWFlzxdPHEH0ygYicEQZ0uHep2OtgQRoBpM65QyKTZF7mHXv-QCwml6Bres2mTUGIL1bIdt1i71j0djyGQIH45lh-Pt_KN89wVbW7c2INRGgSxWV1VeVVp75jLaPTlF_WOvpD9q052izVM0FOfPScd4Jg4NPX6p_2qbXpAEyhP4CQJsYbnndu6eG6sydbUP_JWg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
👤
طبق شنیده‌های رسانه پرشیانا؛ سردار آزمون فوق‌ستاره‌خط‌حمله شباب الاهلی برای جام ملت های آسیا 2027 به تیم ملی ایران باز خواهد گشت. بازی های جام ملت های آسیا دی ماه برگزار خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.6K · <a href="https://t.me/persiana_Soccer/29387" target="_blank">📅 20:11 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29386">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iNOzlHXe7-kuuXiVHKHKBo4KwDaRI_igiTIw-v_cfaS7nmo2kx2hAYhTViBL1EYlhMGNIFjfZcKYkAU1qxoqO2P8MRhIe449AnOiIy8MFi4kWX36QwfxlvPJNzwMWM-TWRjp4RyenZYj7KIT2jfSwKU194cKHnI_BoZyRVYInNCgiZAN3JhduhIaNcbALcBJMugTvGlWf1UQYg3Ho4puKNiF2PHYZ_qtJIUMLsJGUKAWmJ4ya4wYW5oders8og6xApHG89HfzbrbsJtgpPRIeA8wkewranEx2bNBjxdi1tNAkE7ELV-Pn1RlCY7QvibhDHlBF557EN7LPbK1VEiOvw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
اسماعیل کارتال سرمربی فنرباغچه در نشست خبری قبل از دیدار فردا با آاس رم: «آاس رم فعلی قدرتمند ترین و با کیفیت ترین ترکیب تاریخ این باشگاه است.»
حالا
ترکیب فصل ۲۰۱۵/۱۶
:
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52K · <a href="https://t.me/persiana_Soccer/29386" target="_blank">📅 19:52 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29385">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/shdZkfQSO-X8_QV5WzeEgonrOnc00qLl6Yge_ZXzCnT8bfLPceUs0HKjwcGFyQUzAP3sI0vTTPzga2uZRlEKIS2aeDkMEoSXlWYFyD86IP98oq18OmdufcxpYdolvfyP3t3DWhhR78eEt6xQSIN2CPgY7b9cwPi4iUaATFEOA0UyzqUp6fre4ZkZaysELhTgYn79-8GcWeCL4reT9w5J2KawvuLnXTNw0M7eeLwEIWWr1Fqr3nxGpuZtr7QcAnU8-0HdbFqDMHS9m7BIxzUWg0Rct4apK5kdB5IiUQ1HlB9IOGlPFaQwOYcnL4Yl7A-qQ0yLP3Q14kQ9j_l1j5lgVQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
بهترین‌بازیکنان لیگ برتر تاپایان هفته ششم از نگاه سایت متریکا؛ مدافع مغضوب کادر فنی آبی‌ها در رتبه سوم! علی علیپور بهترین بازیکن لیگ برتر.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.2K · <a href="https://t.me/persiana_Soccer/29385" target="_blank">📅 19:19 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29384">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VE5gid450XQa0la6GvStW0kYR_EwKen5paiRUNhBIuHhd0lOvt_4dt0APKAlxd2EjeoHSkGmbCBrnRNwQanIWBZ1xYJc6dEjCfxAVN-oeMhS4vQJr-RyyC7bTGvfCss5UWfheIY5uafS9yxDN9hLuemMfxahzJGarRQMh5N81NECjF1AdaFrWS7VeCjLgMQfIeu3YeS8XUzWZdGBd4llNukxt0LzgOxCrCRNQZrc2i63m-ZnZdAomwFt9PbqMrBXSn_dFrgUGmS5bxGAKOg3gFO78FgqSIgkhtwvVkYjpzOOxqYiopnXiNd8Fne3gYNo1vcGesdHIpGSo4aN7AIkZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇺
هفته اول لیگ قهرمانان اروپا؛
شماتیک ترکیب بارسلونا برای دیدار مقابل فاینورد؛ ساعت 20:15
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.6K · <a href="https://t.me/persiana_Soccer/29384" target="_blank">📅 19:03 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29383">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/s3hv0ywSTFqRLo99mNobN8dk9BXD1ztau3aFZz_tx_F312MZ8Xvhyb2gtpulKqCWF5oUYo3UBDG8e2zgUZhpFNOkU84ii8so5u2ecBiGiGh90tXBKta9xBm1Kf051-ZqDGL3ictaXf_lQUQ1U_82NBzlQR1zKuIszq78FHmbcJDmSfmUvBSOwegdz78jgCbtnXJOGZ27GzMcsXXXE7XGVJNcAcG1obwi5lmhKYYGMj8pDADhAM5XS2Vnr-hoHq8Rlp-DET9_5c7QXTAC9zYccRpYUGzhq-Gal571Xw5WYrgCbD2GR0mCyLw4cVglgIGI-QmZ_NNchq23tipjvDOoiA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
👤
فرصت‌های‌برگ‌ریزونی‌که‌بازیکنان رئال مادرید در بازی امشب و بازی مقابل بتیس از دست دادند تا اولین شکست کهکشانی‌ها در لالیگا رقم بخوره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.6K · <a href="https://t.me/persiana_Soccer/29383" target="_blank">📅 18:49 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29382">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/A2HvzsEPLIxH3rwvvB71puH1oS13WxpRqxN5LZzak9flp2nvlaSBXC8JHzT_qB6yg-ZIBvrL5OA9CWKLtUvrHB83B4kodzOQECM4GHnLOyMIhzr7j3vh2mDz479dczMupl1FNpl_3NTq7S7-EUcBZ55zf0QRkdB75JyUCSHoqVRHGY1g2YPa65l0qVKD1EKBN5kLvijw-N9p3anGuH67ilTLPYz2IeDPnF8rlDHUwAQo9zc_Cz0PTh7LMMRHgHdcXcaXDfyBJv7B6WAlIG1GAjd7I95RTte18QUfMhvqdHVLKcL7KyYvbweu0-Kwgd5eVVobdRzf-i3oJMAGaY2NlA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
با حضور لیونل مسی آرژانتینی؛ لیست 30 نفره نامزدهای توپ طلا مشخص شد، مراسم اهدای توپ طلای 2026 روز 4 آبان درلندن برگزار خواهد شد.
⚪️
Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.4K · <a href="https://t.me/persiana_Soccer/29382" target="_blank">📅 18:26 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29381">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nQfaJLwZr6kgVV9eQ1Iqv0JiY_fJBfw0m9A9tGbzyEBBRGbDSRHl1tBPvYegybFt8P3Es2B7rftPVELIz-O92DsQT0pWZw-q94BiIAd67bwiCG8UTdnpcLS8WEDeSWtXngTiAUu7WkMD4IjaOGaXCmBEOQRlj40xoulfI1aMTTMN53Q2p_RwrTX3iMcuXDgyzJOLY_af42W9TKQe1ozf_GlugKGXXVTKRrciDwCBo8D6pMQPOtWs_CEi93nEmXzU-IBxzWSuzCArrIY3jLuG80SDsuNwDuM6FfyvkQhoePa29N_nYD0dNG5uOoLqt-Y9zgQOg4r0ZOAA3Kk1PW20fw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👤
👤
لیونل مسی و کریس رونالدو آمادگی خود را برای حضور در مسابقه خدافظی کارلوس توز در تیم بوکاجونیورز اعلام‌کرده‌اند و بالاخره بعدِ سال‌ها این دو فوق ستاره در یک تیم همتیمی خواهند شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.9K · <a href="https://t.me/persiana_Soccer/29381" target="_blank">📅 18:26 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29380">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromBetegram</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/H_EFK078TluuDN0puVaD45-Y3bWcQClcdtASWFygn6nwRurYHqe2spLm4OEaxb3PxvpH2xjb7i4HMXIl4Z7M6aUOgSUW7Ug4d_zuCnxBrRwfSZ8Jq-GWGoEpVMrSpBE_o-KskHQO56q7hb82-J_V34wSv4GJHYunWPVGM5wEZShRW9TCfuqzFtEEYGvE--Sx4wlvMoE4IRaqJpgpxAlv1bBis04LKo1KH3D0wJ_QCT-LQcabINAcDA34uLUT5rSwaSRQBEGVriQLURx_ZCvX3F7JdE2hAktKqBmZt3Tw4KAijRJ739mBp6ESPHoNrFmO_xEsxTtNUuDPn6BTwJtVOg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 41.7K · <a href="https://t.me/persiana_Soccer/29380" target="_blank">📅 18:26 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29379">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SpHH5S6SvmbDI-SoXAS3CpiUnrDItfoEnqQsOAFTQx8_JzW3f1BZGUNKRrwTGd8s3SgwnEKOqbYwMw6Pbg3uCnCd5feRKDANr9KuXxlwhWQ5sVeiY2TY9ewNVPEot4LKZwddQ9hRZmqkTD4MKdz5H8OFPLnTiWFoCijFEt9mGUJJLTBBiNaT77X88gyih73oVoa70G1X1qowon-_ncL-XCES0iSkrc_0xecGODU3aaaKAV3Cf9L5QCMBLHQb7aRQxoRsS3_qbbrmXU7_Um0Es2q4MpMejFonW76qd_aeH-vBPEcwrss6LgSJci4gpADGMKA1_kuQ0fa3XI6e3VK50g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
بهترین‌بازیکنان لیگ برتر تاپایان هفته ششم از نگاه سایت متریکا؛
مدافع مغضوب کادر فنی آبی‌ها در رتبه سوم! علی علیپور بهترین بازیکن لیگ برتر.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.7K · <a href="https://t.me/persiana_Soccer/29379" target="_blank">📅 17:47 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29378">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dHbP_r6i2-i59g3FiTSjy4LA22LH3D3Vd-3nDKcSorBE_VrZlvWY2k40ghVG98_tkKMZF7Q48s9jMieowNJJ3Ynuyhg8sAblWAzw33IDOIlc9eXTAA_O762DD91LJBh-5N8MpYK2jjFgmdFZlsazZuQbZSkf9qCRt0Sxd4_Cakll6LAqvslbYIm5QULpvDPgbdnDUeqcrbRKSf-qoXB6hhQMX2QFr7y_j5aXs8HhuXRkEFBXunlkbyJBXg-5aaEQcA6Q4gjpgvpkBRu3RJcmx_2FaRMZUkJx5Rlb5NOMVOJr1bUJY3XMOup8OE6y70_wXbO0ObQrXLFYK_rbU93Hig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🍏
💵
قیمت‌های‌احتمالی‌آیفون 18 که قراره امشب حوالی ساعت20:30 بوقت‌ایران ازش رونمایی بشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.2K · <a href="https://t.me/persiana_Soccer/29378" target="_blank">📅 17:29 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29377">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EaCCu9F7l1kicBoy-qmvcZ1hjXUjjpN0TcWlqFxVDG1U5mkbqEi2-2LW_QARR8A1g_hXNleb8aJPtAaOI5bF5y-_mW9KiKzezlInDlrmZWATt3MxPmvEFtj1b6LM575u2Zil6dXEU8AgEo7RRh6Vvp2lzeUccagjkQaX_tP1m73q56fLL9sfDVBCwjZtoH9zHuSuSWLqeESJDvIxaGUjES3916aEkJZzySf6TRYoVbMdo2RZUc3fx55N050wtGpdDOFCBIP7GleLRuipvAVGmRSgxK0htnvcmTDSuoHFxs4ZOsOdJd3laSOkc7hPOOWMHGDfSVMn0ir-N0euFW32HQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
رکوردشکنی جالب پاریسی‌ها در تاریخ توپ طلا؛ نامزدهای نهایی کسب‌توپ‌طلای فصل گذشته فوتبال اعلام شدند و در اتفاقی جالب، پاری سن‌ ژرمن، فاتح لیگ قهرمانان با ده نامزد رکوردار شد. تا کنون هییچ باشگاهی در یک سال ده نامزد دراین‌مراسم نداشته.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.6K · <a href="https://t.me/persiana_Soccer/29377" target="_blank">📅 17:12 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29376">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pHg3cQjnbwa9t8qWQEXAAv5S6uuuChatlWO-1YpFMmV0gEVqDRkpHQsEBE9J484WDwF8sn959G0K_nFXx-GlsdWj1zF7VC5YHWe6xDjOF8UPiyYIxihjXHFYR8lUx42ZVbPTkbG0zZMXt3Rpia78Dl5yJHMMX3fVz5eqxuTx6GnM2RqIzJH1SRZv9bxzxF8ZBvMfPp_6ZnfhYuDfSSTbfsDRMkfPyLYupbL7dMb8KmJ6iuqYvdNpxPNv1ejRXu81hyF_VYkoUWITlMyw6-rhruCJiKl-RaAQX9ETbiVxNL5UbfhzPH8uwmXz70_HK02XJrwCATN_wYMwGQEeUSUNNg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
👤
فرصت‌های‌برگ‌ریزونی‌که‌بازیکنان رئال مادرید در بازی امشب و بازی مقابل بتیس از دست دادند تا اولین شکست کهکشانی‌ها در لالیگا رقم بخوره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.3K · <a href="https://t.me/persiana_Soccer/29376" target="_blank">📅 17:01 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29375">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jH9G88Q6QFQx62by5HAlzbzZ6f-V7nnW2X83jrPV0IC9Gy5IkKg1iwT3Jgj_hUq2ehx46YaVLJLM_Axmff6QHwfWp8RP6KXls9XFuCfpVoyjVM-ODjpWFoOQKUCvSgPyQKrYVDx2q72JOUlRFKEm7Q-Iylvjqgad4dUa8NYgq9A-IaK3nAWmeGcbtt3B-NayAxrWaI_qSj3ueSeup3Ap0mcD2Esam5kO26k6Aj5ythENkfUQLspZnZmuo1SKgtXZ-yUaXQyaJvz6ofIvZJxriK-rX8eORZF7TkVRa4xK0DIwvV43kvK2QMg3c0Y1qvLXw1cBL2TigS1OxD4K1qqkPA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#تکمیلی؛همانطورکه‌پیش‌تر هم گفتیم؛ بانک شهر بزودی تغییرات‌مدیریتی‌درباشگاه پرسپولیس رو انجام خواهدداد. باگزینه‌های مدنظرخودبرای مدیریت باشگاه پرسپولیس درحال‌انجام‌مذاکرات‌هستند و بعد از به جمع بندی نهایی تغییرات رو انجام خواهند داد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.7K · <a href="https://t.me/persiana_Soccer/29375" target="_blank">📅 16:36 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29374">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eWO2sOmJ6Ks9pD5Ru9pcRtXUQAfaW-uYNmbr1VKgemQOCCzzW3sx4zYJTuIfJc3XqLrwiV3hD0Q8Z8cMugjSdyylVCYKatGPbwIF7KSz0qhF_v9AT1Tj7zQtdgKfU6Z7_cseXfGBh15e-xAarmldAal88YMp1bv71-waCPyYk5-c3jCvAkrs5RY4OP2colZErVCSODKLXYop4PaonksvStAXEbGnpV7_YX8VUOzk-ertoaaUGHTgIsCzVdG82l-GnSaCNPA2UoMRq8bdXkh1gF-Ls32hOGvwDhnHvtfxWL-Kif2J8OVl-AsNZR6rDREfrE82hbbW6KD5hAoZzwjLvA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
#تکمیلی؛ برخلاف صحبت‌های امشب پیروز قربانی سرمربی تیم آلومینیوم؛ باشگاه استقلال مبلغ رضایت نامه محمد خلیفه و بهرام گودرزی دو بازیکن جوان‌آلومینیوم روبه‌حساب این باشگاه واریز کرده و بااین‌دوبازیکن قرارداد پنج ساله امضا کرده‌اند و نیم فصل به جمع آبی پوشان…</div>
<div class="tg-footer">👁️ 48.8K · <a href="https://t.me/persiana_Soccer/29374" target="_blank">📅 16:20 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29373">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pr5cUNJTdOtttT2aTGQOXcIzKa-wOpdpAaTVZqDEdiJ7BBQeWN719OHf_iQ1Y6XuLXXOyKr4b9ILEfoyaNCvL0yYI9FaIDRvdXBAMDCctJbn1SCcdgTaBmVB65QQ7s-nt7qCu8MIUQKowK1o06rO77qx1xrutAPWLLKm_7mmgdbTO0qlapCMqdRsP3CC6i1Xnemy0SUElevgMHavb-1rAzyw2CjbikHjKihKo41kUZ4yu3UQGSGCcBw4Dpm_swJcvQuemQ1Ya-sW6sqwueONxwYHRHzL2qzuIxwaEoC0tBLrg3KvMrSTuXNFEoNi_jx19AbyQjwUnyzfgr0MTo-Z2g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇹
خبرنگار معروف و محبوب شبکه DAZN ایتالیا که مسابقات جذاب سری‌آ پوشش میده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.3K · <a href="https://t.me/persiana_Soccer/29373" target="_blank">📅 15:57 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29372">
<div class="tg-post-header">📌 پیام #40</div>
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
<div class="tg-footer">👁️ 49.1K · <a href="https://t.me/persiana_Soccer/29372" target="_blank">📅 15:32 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29371">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/M0cgsiT0mEi-gwju4djgGa-HSgJ2YJJBCadWg1z6JmielxtDQDNufHKNuB-ofdWC5VY5a5bPXU90HCTGvvnhoHMGSU2BJa-UKopI_63ywN-3DxSGssuENt9D6VR9kSUPudHOxn6g8aosZtvAR3CteG1qcBGNRlOY5aMvDFh_WNwn1by3E4bJvN1ZuSp-dD7bYLhsvDx6UzpSRaTJ63gn1SGjhw17SM9DTfx9Zqb5-ZifNF1ImjQGgpLP6IhzzNJ0A1j2eYeTpvk_XWm_EGD0pt2ES5Di8Roj4zGIRxymg1xAIZOFqtRTfLjnlR2WHqq2amcHcuFCY5E6s60hk6jAfw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇦🇷
خوزه‌فلیکس‌دیاز:فلورنتینو پرز رئیس باشگاه رئال مادرید بعداز فروش نیکو پاز به کومو با رقم 60 میلیون یورو به‌اوقول‌داده در تابستان‌سال‌بعداو رو به رئال مادرید برگردونه تا برای کهکشانی ها بازی کنه.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.2K · <a href="https://t.me/persiana_Soccer/29371" target="_blank">📅 15:25 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29370">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/T0vNJi7DZ0d8GgAN4uDrUKV_znoOgKUu0DrJI-am5ObVwJvV4pnhyc0CLIYrTIneSllTlw8sMuaWNZHkKpGOkXhvezIJZRNgXkLGLiZTmss2_SBj2AkbbwkW_sYTSzguKPgc-fiNT5AHK8Ucs_HcNttBzPQHJyNQPTffAlOROm-JiElHlxdpxnUN4_xS1bi_1M6RpCtUBAELQuIyoH3g-nOJnPJTstEqI2gskvtq9HtO22G0sWXe48fw9dIrLuOcvSvf1SznBQH8y5UTC24P6GbHymodDCMfC-KKi91acmL22yub3FLUpyamJfQP-0iPcgi1mxLBvcMLwcHdEXqdFQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
با حضور لیونل مسی آرژانتینی؛ لیست 30 نفره نامزدهای توپ طلا مشخص شد، مراسم اهدای توپ طلای 2026 روز 4 آبان درلندن برگزار خواهد شد.
⚪️
Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.1K · <a href="https://t.me/persiana_Soccer/29370" target="_blank">📅 15:15 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29369">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gTLWtUK_Z53O0bzBxv3b6WWudHO4Qs3BG1YBn4yhtCUo-1F-12IiM36KTS05j-b7YoddX_xALlnqr6yPz-obL621xNZ8EaYsIwnwB4BZn-ffbBfH-eQFiPiSa9ODhmQxf_yrlPii0S65ovlOAgbBCzme9mooljMq58m8wD52qGQmoGU9MwwYVhe84rpjTKJlZC_0Xq0p2i9Ejvf1qyKYFY6JUN5V-E44z7lH81ZFPOWHKevOs70cHuIweK8vMyzhEUuOm8goZdWOIFYzrTd9QYHzlDWGQKgC781yRqGZZaGUXuZ2SLKgPsQGl4RdG9PpTvMqwR8_a4brmXQup9lLdQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
#تکمیلی؛صحبتهای‌پزشک.پرسپولیس درباره مصدومیت عجیب مهدی زارع درپایان تمرین امروز!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.6K · <a href="https://t.me/persiana_Soccer/29369" target="_blank">📅 14:59 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29368">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LizT6yOimIPqMIlu_ajZ-L-f8OOPXl6z4qfO9tjlcZkGVuj9_CukPivX10p5ZVSIxfIei1hmu5QegN1lanHIobOvlh5YOEp1F23T4K27C9BDW5KEtxWpfNSOoK9iK5ucSfq8MAmBKmMmmL5P9LlA-EZxOaPb919hZZgb7vK7GeFphjRdZcR_Ewhl_gaywsQJzifgIn-_boY52SPXij7f_DJ2icdVQD1dFyjYQzfjyJPEEFir4i6EMNH4PheMol-S_6dw_dD6fsCQWwIBmFnBVH4VVFt7ChbIY40lG9anBksqUjTegmjVaMFUCDET7X4SsKhF9lRkm7iSI7rtz_utFw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇦🇷
لیونل مسی آرژانتینی ساعاتی قبل با خرید 100% سهام‌باشگاه‌الدنسه‌مالک این باشگاه اسپانیایی تو دسته‌دوم لالیگا شد. چقد لوگوشون‌شبیه بارسائه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.1K · <a href="https://t.me/persiana_Soccer/29368" target="_blank">📅 14:44 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29367">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/I4A44-qUdOBgfqxzjV4AWn7fOS66u_XATEBoGj1gyJyKLmgn4p0leGQSj7L9IJROGN72AIPb4VV9hii5bMkbOm1bFi8AI9eOjXKMpn4r9nZNcOtl1nsCgwZY8mD-dQAeEOOAXf8yHfQhMPJFBJ8zgW6X9Ruix3WMUnKewVPFFQAiHrjzUtCvnbI1E2gT3WG9LQw7VeJbNyz0fGGVGhRZtE0aBEkxCD1Sz-h4OpNNcuJ_iJYetjjkhBR7F4eP5jhdtdSeoCUVI1RLVi8tdZgqupPgysW-A00BEUA-q_0llPZ_fY-ONYSD14hpUEamTBUTgIj8WhSCfUU3rta248z6jA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
ویس فحاشی برگ ریزون و باور نکردنی خداداد عزیزی به امید عالیشاه در پایان دیدار امشب؛ میگه منتظرم بیاد بیرون کارش دارم!
⚪️
@Persiana_Soccer – ویس فحاشی خداداد</div>
<div class="tg-footer">👁️ 51.5K · <a href="https://t.me/persiana_Soccer/29367" target="_blank">📅 14:13 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29366">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aXxWcxnPv3YdyShoGve4G7dUo5KdCReZ3on9a4d2AiO84VAM6kcJh3gZnmj2oZcjL2J_Km2rQlw160gGQYgwEVZ7tyCXnRHyluArcfJ9OHiiK9Hlggvqu3BJaqz7NLKkXX4nM15XY-UVxqbPHuzmGtPzklVe1ozxAxpWn9TwnGlprc8Hu4ett7V_dlNhQEuGmQZIO0iBexKAgPUBXZlCNYty0vdQyNN2X5U-VlZq0hSkEKw4Vwd4asGZ95vjp6prNKXVcp-5cbfNzOX1wOzMXSzWhn044CzPZivnxNZphYgyZCbpdMQw-9HW8ENS12Qut_r6Akg7fCwdZX3_ASBxew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
جام‌‌ملت‌‌های‌والیبال‌آسیا؛
تیم ملی والیبال ایران درسومین‌مسابقه خود درقهرمانی مردان آسیا 2026 بانتیجه‌سه‌بریک موفق به شکست چین شد. شاگردان پیاتزا بااین‌ پیروزی درجدول کلی‌مسابقات در جایگاه دوم قرار گرفتند و در مرحله یک چهارم نهایی رقابت ها به مصاف تیم ملی چین تایپه خواهند رفت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.7K · <a href="https://t.me/persiana_Soccer/29366" target="_blank">📅 13:44 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29365">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/765da8fbb9.mp4?token=mofjB3P5iJVz10L4Tc6a2snuVa_BdTXpvJCOKrS0l-FcX0WQ1N6L2IozHTRDvzZMVA2xC8CxAcMCidjmUscBRLZO1ed_VFAiIJczzjGsm6Uhz7bWS_-eBsM5bBiVEq4OTJDF_6UOWbN-iXm6G0GSHLCuK46Mlg9vauw8AyTXJ2CrlNkK9P-ahUSh1t2fk9mUDABqGyjJSvsqLi1hPVn1y9qbVIg10WdyUOxcbMvXfz-t5wmkVr_2-vi0ZjiKnRLAHr9Qc4we5j9i2Vx7oKrzw5gpg_OXokccSWs9KSH9w1wyE0XBkoChp_58sXpuFwxZLDGGpwPWdgBX9h3r6od0dLq2ibqPBS_MiF3AXnm7jYUmnS947s_6NNDXoIVNnB-y9xncVnzmYHqWDWfrYHh1aJDhKHi--71S5wCUL0HTeTs8h8jOcSWWbeVXNHZVVqZnn0LKhSVf9G40AcFURhww9diEx5abvNSDcBDQso08SgzCGnB5XJrImxQEsnoRqb-2vwX_zbNIfybgjOL7cKm3UySTRUcOpNxsyX7fkOktMGUq8rVzf3NKUYzR33EOB9iX68LYZXu1ZofP9awpO9QeVtMRuptGDHg_vBnYl8bsUxEvWcceFmQJ_uwUQgPIzpu3rv9J-RUhzYaPJOdZJCIrv5ypKz1iS9UAQZzgjBfu-1w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/765da8fbb9.mp4?token=mofjB3P5iJVz10L4Tc6a2snuVa_BdTXpvJCOKrS0l-FcX0WQ1N6L2IozHTRDvzZMVA2xC8CxAcMCidjmUscBRLZO1ed_VFAiIJczzjGsm6Uhz7bWS_-eBsM5bBiVEq4OTJDF_6UOWbN-iXm6G0GSHLCuK46Mlg9vauw8AyTXJ2CrlNkK9P-ahUSh1t2fk9mUDABqGyjJSvsqLi1hPVn1y9qbVIg10WdyUOxcbMvXfz-t5wmkVr_2-vi0ZjiKnRLAHr9Qc4we5j9i2Vx7oKrzw5gpg_OXokccSWs9KSH9w1wyE0XBkoChp_58sXpuFwxZLDGGpwPWdgBX9h3r6od0dLq2ibqPBS_MiF3AXnm7jYUmnS947s_6NNDXoIVNnB-y9xncVnzmYHqWDWfrYHh1aJDhKHi--71S5wCUL0HTeTs8h8jOcSWWbeVXNHZVVqZnn0LKhSVf9G40AcFURhww9diEx5abvNSDcBDQso08SgzCGnB5XJrImxQEsnoRqb-2vwX_zbNIfybgjOL7cKm3UySTRUcOpNxsyX7fkOktMGUq8rVzf3NKUYzR33EOB9iX68LYZXu1ZofP9awpO9QeVtMRuptGDHg_vBnYl8bsUxEvWcceFmQJ_uwUQgPIzpu3rv9J-RUhzYaPJOdZJCIrv5ypKz1iS9UAQZzgjBfu-1w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
آنالیز جذاب و دیدنی دیدار هفته اخیر آرسنال و چلسی؛ میکل آرتتا به‌این شکل تونست ژابی رو ببره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50K · <a href="https://t.me/persiana_Soccer/29365" target="_blank">📅 13:35 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29364">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ea3eaf66e2.mp4?token=iYvquS9p4WDE5chQK3gwSh13bmNNXq9t8_jLRcZ7FYm7elAtPt1N2hbfX3GGnAPYyQCKRMj4mbhxc5rLnyyrJSO7zI_GcrOnvEmEIIW9grxF0RigiZeY0BxervN7AyaF-UC80RoxXCC9Zx-9K_Fxob3jl2wpymf9SRfX75D0Xwy5EHtOFnO9meq1XFqHhJFOxWlrrBKm74cV6p_Wx89mVnYa-X56YDHFzfR9211IzkjOk6GYHdD7jjIEFwVWATcAjWh3SpYpKIo3o0u_H_dJQxOmFXWjw4PRXpmWsQKZQDVppJj7JEyU2SjABI8resOvJfHmPHPl46y3etlDfyQcZA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ea3eaf66e2.mp4?token=iYvquS9p4WDE5chQK3gwSh13bmNNXq9t8_jLRcZ7FYm7elAtPt1N2hbfX3GGnAPYyQCKRMj4mbhxc5rLnyyrJSO7zI_GcrOnvEmEIIW9grxF0RigiZeY0BxervN7AyaF-UC80RoxXCC9Zx-9K_Fxob3jl2wpymf9SRfX75D0Xwy5EHtOFnO9meq1XFqHhJFOxWlrrBKm74cV6p_Wx89mVnYa-X56YDHFzfR9211IzkjOk6GYHdD7jjIEFwVWATcAjWh3SpYpKIo3o0u_H_dJQxOmFXWjw4PRXpmWsQKZQDVppJj7JEyU2SjABI8resOvJfHmPHPl46y3etlDfyQcZA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔵
🔴
فاصله‌امتیازات دوتیم استقلال و پرسپولیس در تمام ادوار لیگ‌برتر به‌کمترین حالت خود در تاریخ 25 ساله برگزاری این مسابقات رسیده است؛ تا پایان هفته‌ششم لیگ بیست‌‌ششم استقلال تنهابایک امتیاز پیشه. نکته مهم این که در محاسبه امتیازات، کسر امتیازهای انضباطی اعمال نشده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.3K · <a href="https://t.me/persiana_Soccer/29364" target="_blank">📅 13:35 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29362">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1617cce66f.mp4?token=f4q4c4E1fRuYYFiX0ibs0cMi5JZa2zV9LQg4kY0xroZf1wnc_C8yro8ICNZHJVGguQ6iaTbJaoGpN56eV-1N_bWb6qiKnMS_L-seLO5EmuZb2f6Obo5xJInkJ_uqNZsPJyA6F4YVSMQ0e2CvmeowDimHIvMX8RjJ8lUU9pLL7U-DoVKMHMQ6L9Zo5jZy-MKQP_CWyX5aROF1kej2586XtPzGgS4FDkTcba484YAfCbGmP92IYtl2cqN9zl12DVxU4v-WqF8Ec83mUn3LDcEMsbe_MnxAdlZcN3LCh6wpVEoY9GtJ-YG6W4nQi9Xg1YnSVqUELml9lzugyb_qJMH8E2_usqTARb7NXKZMA0DkB9e1lFyyreOA8FdxYNLNyLIyZh-aPxPRuBdvfY5x1pHH57xRw61_hqXDmk8_cecFNtRLdwFQ3RyN2xlODmp6xoeR0MpW_uSyDrrq0KU_HQxyVaM_oifxtuJ0m-SvcsQ-q6EgfhtWsx52D_FW5wXa_Q3HBC6JIqqETiBfCVdNrQC3Ez3zBD-mq8zS3w8GY8etSFIzSZqluNdmdCKjhoFQcADNBtYVdrO-N_8cHdsCWpwfORD473TByGs2MGtS_UrJG0kChP17Xbng7qvVeHRnrXIsdZKc79OB-aZd7DE-KuXnZLfn8gTGj-vTFJrcJI5QFmU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1617cce66f.mp4?token=f4q4c4E1fRuYYFiX0ibs0cMi5JZa2zV9LQg4kY0xroZf1wnc_C8yro8ICNZHJVGguQ6iaTbJaoGpN56eV-1N_bWb6qiKnMS_L-seLO5EmuZb2f6Obo5xJInkJ_uqNZsPJyA6F4YVSMQ0e2CvmeowDimHIvMX8RjJ8lUU9pLL7U-DoVKMHMQ6L9Zo5jZy-MKQP_CWyX5aROF1kej2586XtPzGgS4FDkTcba484YAfCbGmP92IYtl2cqN9zl12DVxU4v-WqF8Ec83mUn3LDcEMsbe_MnxAdlZcN3LCh6wpVEoY9GtJ-YG6W4nQi9Xg1YnSVqUELml9lzugyb_qJMH8E2_usqTARb7NXKZMA0DkB9e1lFyyreOA8FdxYNLNyLIyZh-aPxPRuBdvfY5x1pHH57xRw61_hqXDmk8_cecFNtRLdwFQ3RyN2xlODmp6xoeR0MpW_uSyDrrq0KU_HQxyVaM_oifxtuJ0m-SvcsQ-q6EgfhtWsx52D_FW5wXa_Q3HBC6JIqqETiBfCVdNrQC3Ez3zBD-mq8zS3w8GY8etSFIzSZqluNdmdCKjhoFQcADNBtYVdrO-N_8cHdsCWpwfORD473TByGs2MGtS_UrJG0kChP17Xbng7qvVeHRnrXIsdZKc79OB-aZd7DE-KuXnZLfn8gTGj-vTFJrcJI5QFmU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
عملکرد 9 فوق ستاره‌ درفصل‌گذشته رقابت‌ها که در لیست 30 نفره کاندیدای توپ طلا قرار گرفته‌اند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.3K · <a href="https://t.me/persiana_Soccer/29362" target="_blank">📅 13:10 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29361">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/732028b756.mp4?token=C0Lo1T7GLjlpwF-NyiZQhM7tQrQmgGPTm62hUGARSz6rL3Kcva_yje_ykDq_AyqEv-gi2WVpDgHe2v0UlgMhDOCS_alVaMKcZR-FQhoLKfUs6Et0EGQB-02DNE-6DEFAFhaXnzBcFbP--EI4u8pdubg9dVOENLo_Lq0dndkYl0rk3KuwMYtfrTimywbzdv3qsKRM2UGpWUQVBtwt3cHjRI2RtSN_yMW5hRRTMg79Ha8UBZYFGqmdNeACzqzmv8wtwBmUKPGCFw9QOZ-O7-lVA48sIznnXxz77iI7-jhjzLfndHnD2OcrAFMIm2pqIMz36aDnaiwkKqoITVfPYLo4iQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/732028b756.mp4?token=C0Lo1T7GLjlpwF-NyiZQhM7tQrQmgGPTm62hUGARSz6rL3Kcva_yje_ykDq_AyqEv-gi2WVpDgHe2v0UlgMhDOCS_alVaMKcZR-FQhoLKfUs6Et0EGQB-02DNE-6DEFAFhaXnzBcFbP--EI4u8pdubg9dVOENLo_Lq0dndkYl0rk3KuwMYtfrTimywbzdv3qsKRM2UGpWUQVBtwt3cHjRI2RtSN_yMW5hRRTMg79Ha8UBZYFGqmdNeACzqzmv8wtwBmUKPGCFw9QOZ-O7-lVA48sIznnXxz77iI7-jhjzLfndHnD2OcrAFMIm2pqIMz36aDnaiwkKqoITVfPYLo4iQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📊
از پس‌فردا دیدارهای هفته هفتم لیگ‌برتر شروع میشه. تراکتور دراهواز به مصاف استقلال خوزستان خواهد رفت و آبی‌های پایتخت با پیکان بازی دارند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.7K · <a href="https://t.me/persiana_Soccer/29361" target="_blank">📅 12:45 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29360">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kvVbIw8kJvBWITnX7L6wG-AQZaYl03_rk5UfAvYLWZ9HB6S5bfvl4rDGZ0rnBYkKKNoNN3tagx5bfSLNRZVGWg_6N1A1m6nJMVPkqMiqtP0_NbgJZiE7_Ff7-68Hk2dCKnq5FBbMP28i-hB4nHawvO7U2oDa81z2crAhHN4pytkjZH5GNb7uvsujfnqRKxrBVsYSedURd89KPLtVbCJG9yGnw2WfZSh9KSc3fOkx2TEhA757fViOwg18X9CdUgi4GCge3iNoMDeq8WRB-qfwSAx1MQ6FTdfKoNov19nDKiA24_BLGss50748n6o7MwuYipg8ETTXOenQ_r-nBT5a4g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇧🇷
برسی عملکرد خیره کننده رافینیا دیاز ستاره برزیلی بارسا درفصل‌گذشته‌رقابت‌ها که یکی از بزرگ ترین غایبان لیست نهایی 30 نفره کاندید های جایزه توپ طلا در سال 2026 به شمار می‌آید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51K · <a href="https://t.me/persiana_Soccer/29360" target="_blank">📅 12:26 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29359">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WlfiCPXVFcU7nGJ3JQ-0ZwUjQY7hS5wOKC0H8ReE6Dxi3BE58DfENHkjtPsNolwu_sEydg5bXJrMnmhtJvZ9lW8LRdjY4DDT98PoC8a7i5WvTxel-DaXOpw3FIORPBm2bDlz7jmI9P595IKw6aFHTLobyhmZAD7pO4ofVbbc0Gs2CG55rNkXFsDyJ_7iIZgH9xxcibTnTY7U_dXualnrgL_hdNFgUXresQeck6dBOp0XUehgHHxNwdSZaTKSP_8NQBC1im0y4tuVbVQevWRR66HqC1er9OuF3cw6nFTmThQQ5mettTZGq2OIHgr3IQVksGsU80u3alvvaZAzCfFpyA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
با حضور لیونل مسی آرژانتینی؛ لیست 30 نفره نامزدهای توپ طلا مشخص شد، مراسم اهدای توپ طلای 2026 روز 4 آبان درلندن برگزار خواهد شد.
⚪️
Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.3K · <a href="https://t.me/persiana_Soccer/29359" target="_blank">📅 12:14 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29358">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hNR3JKvxPs77Q7iRgiiq0LDqM0EUZZvbOj6K_6V_ewbD2BIX1rsbrvbVkIaVr7GW3D3Alpr3VW_IFXRNOFOeFvEIBVgbfFXl4F3nyqQnmWwaZXMBzlQNLGJdLKtLW0gE0LSNE-eq_LSEd7FMGy9ymYHTueGCJmp4Ve8vsNSfpZMnaMSmad8uXFxSb6DLbSNmyeGAKpahpCaBxaiFUwmZOVBiSlzaNbuLql54lEyvQppdG55gNyG5Dar1hL_NVrgyxVFdCdJE1Ma2pmAh3xfqp7z8QkuI1SNN6Rebv-_N8SGFrO3jIRg2zK0iw4vA04Z3T2PgJ0Ww9UwgjbTuG1u10Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
دو سوپر گل دیدنی شهاب زاهدی در بازی امروز جوهر دارالتعظیم در حذفی؛ ضربه سرش رو ببینید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.1K · <a href="https://t.me/persiana_Soccer/29358" target="_blank">📅 11:40 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29357">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dXIoamewat60zwkwAxXrUtAUeH3m3FFQ3VSLWk_Iuh9Cku3I0v7Gu328u5kRzrdN8yNhoskmzT_whCqC3syx6pcz6A2XOd4CnKWZttlsH4dvZPuEt8NKdzTltbGwUQWcqtl6O4DCcP8qRxyIZ6_9hGEcCC7iaA1jMdRcpt_xWfEYN5g0XhC_vrIO1bcw39wfSSjPT1Q4nnpdUUL_qV19dgW3ZKcWWjBslCwM3zawXmM1erSwjD64J85Yr6B23aXgquClK8JZ9COugJzLSKiZD3msaGVFJHlb2I8J3-FFIW27Wx2kmM0Q88uSL6lTxE2BU4oorvk1TLWQPcr1R7ZuJw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇫🇷
رکورد خاص‌امباپه باگلزنی به اینتر؛ کیلیان امباپه در اولین بازی چمپیونزلیگ در دقایق ابتدایی به اینتر گل زد تا با رسیدن به آمار رائول افسانه‌ای، پنجمین گلزن برتر تاریخ لیگ قهرمانان اروپا شود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.4K · <a href="https://t.me/persiana_Soccer/29357" target="_blank">📅 11:22 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29356">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sW5YCfkW5h1qCS9mhC2SzGNbvKNBSzE5IKGlPuzZZSQW0gLKIGIvjHEhzeoPWiYSNuohp-wpaT05og7t2Hgex_tvSNHNlClP4oSDB8IFc2iFmImHpGJ0PvLMXy8UyaaKtRCVL-IIFMBH9mLjGYyUQLn9JzQ7KGrxcV2cE3d3u7xGIaGX4sQ8qAWuF3ENBEQSPcBs-STOyHk8bx7827EeyraNDL_gkAwMiNsFMObcyJod9Yvl2l-hqj_EJ1rJDE--DS8eUcWACCPu0Ooxdnxcq8WlUC_34ziIDsPqD9qL-z1IYjept9rWJ1fhpJ9-D8YZtBa0Icc2y3BJaxT9CBFc6w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇹
🇨🇴
با اعلام‌ رومانو؛
خامس‌ رودریگز فوق ستاره 34 ساله تیم ملی کلمبیا در آستانه عقد قرار دادی یک ساله به ارزش 650 هزار دلار با باشگاه آولینو در لیگ یک ایتالیا قرارگرفته است. شرایط‌جنگی کشور باعث شد که خامس از حضور در لیگ ایران پیشمون شود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.1K · <a href="https://t.me/persiana_Soccer/29356" target="_blank">📅 11:05 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29355">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VzJHWqOdQ2-SjTI-CYJR761jQq3VNI8O84EwvXnYH0-7hg2ObdLSkhG5CWb-n9rgF1KBMfFTFk6avIFaU_TRtBRvOZ9X8t9Nx68xkXoDWTPmaRte-w9n1DkL0veekBvKlJVPItJiOA-ES1Iv6hCWOAD3L9yuPVwWNDlfof0akQewSpX75XF366CjqiV0yaBf27UzmXmQchbogmiZlA0yYDAI9ZALPNBBpEa0kXYNh4iaCqz5KKmJZ1TLAyOjJBR093ngZucqxlr_SciXBToBn7qjcCjhPb95yQS8EpdjFmusle0B7_0JmG-ZWmJGZ4a6yZDoNUGuzLz1BSk6uXvzUQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
پوریا شهرآبادی مهاجم ۲۰ ساله پرسپولیس با دو گلی که این فصل به ثمر رساند به دومین گلزن جوان تاریخ این باشگاه با حداقل دو گل تبدیل شد. مهرداد اولادی با ۱۹ سال و ۶ ماه و یک روز، تنها بازیکنیه که پیش از ۲۰ سالگی به ۲ گل برای پرسپولیس رسیده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.5K · <a href="https://t.me/persiana_Soccer/29355" target="_blank">📅 10:44 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29354">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0b6f5a93d8.mp4?token=eyQUs5bMZb90vBUJ0Jjo9lQVyNyAHALcemL9ogtDDKr4KbU7hDI6TyRQST5rr6Pm3Hf4KDIPOhu6AZgGWFsy-Cz4CtqlescomrOl2gB06HBS9tPDYv7FgnDiuFzC5SqcubMCKqYibiWifrHSoy0Y3b3wtMRrjn2FATp8wV_8YIFO8TMUYqWxAo22YokvfBQYUnkqWOkSdALyQYjTlHzVAZFbd5wSYBaKMdnNQiEATKsacscWnghSn8UuAEoHAx1gmIvjL2_Uwfm4HRzIOj0w7WCUxBY7tE8dKYz_5l0pLS-90VrAGqQaNYqLfX80lJpVqYsngFI_flXZnGbERllOeg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0b6f5a93d8.mp4?token=eyQUs5bMZb90vBUJ0Jjo9lQVyNyAHALcemL9ogtDDKr4KbU7hDI6TyRQST5rr6Pm3Hf4KDIPOhu6AZgGWFsy-Cz4CtqlescomrOl2gB06HBS9tPDYv7FgnDiuFzC5SqcubMCKqYibiWifrHSoy0Y3b3wtMRrjn2FATp8wV_8YIFO8TMUYqWxAo22YokvfBQYUnkqWOkSdALyQYjTlHzVAZFbd5wSYBaKMdnNQiEATKsacscWnghSn8UuAEoHAx1gmIvjL2_Uwfm4HRzIOj0w7WCUxBY7tE8dKYz_5l0pLS-90VrAGqQaNYqLfX80lJpVqYsngFI_flXZnGbERllOeg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
حمایت تمام قد خوزه مورینیو از فده والورده؛
جایزه‌بهترین‌بازیکن زمین باید به‌کورتوا میرسید فک کنم اهداکننده‌جایزه گل والورده رو دید و بقیه بازی رو خوابید با این حال فده هم خوب بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.6K · <a href="https://t.me/persiana_Soccer/29354" target="_blank">📅 10:31 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29353">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JpMYyT-I0lVxZZIvT6R1DsDEqNA6ubfeeETRejL_8yesg4L5kK98fcDQz1tE-ykzcfrixd02k6FjzjUfCfnLqrO1kWVGeChSFtlrj4V0jbLRaAalhxv5A26c5I2RiEvdXwQ9DfNDONup0eKseOW3txSMsSBd9p9-jVh3Kop_bd8gO0J5BMBEwGhh2PZcfQjXFZsHVxBGg0Ua2jnyGkT-tvChVMQ9TqZ9el7y7x-B9Ih87ewEcn3sbbIjOGAiW-UqZ_g7zoLVzm85LPxhMAXE4VjJCEvQ7WKuZ1x0lkgP_XHkvbow2vW42jDvWu3nRSeiEQqwXs3olyowVsgckjx_Ow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛بعداز درخشش ادامه‌دار نادر محمدی در لیگ‌یک‌روسیه و لینک‌کردن او به آرسنال توسط رسانه 433؛ این‌بار نشریه سان گفته میکل آرتتا اگه قهرمانی UCL رو میخواد باید نادر محمدی رو در ژانویه جذب کنه! قطعا درهر بازی 3 4 پاس گل ثبت خواهد کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.1K · <a href="https://t.me/persiana_Soccer/29353" target="_blank">📅 09:49 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29352">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lBRn_lnFCyHF075zwmY3gXsZdB6bBIOqjhDsn1WzSoNEqqLibcStzItsH098gT7xOcj97eLjt999WXEf0FbgZal2lQtLqSjuEYUuDZAc2597F-08ECTZrVBkq-PXNURgW2VsuLm7oYxedY-EgSKj6-ubEdox35WIvV9Xg97TAftVgDg8fstSjwii8snVgLZkDsk-Krg4382XGQEoV9oLH95pEeHbWvL9B5kdpKSedw5uc4DMI72kPQBN59GpIEGRW2hsKajRWieK-c15GxP1eqZFq_MoBxTvG0y8quZd7P-qffVoyjEVfeywxYSoZKOa3vHQvy1K-bHvDgY7uc46jQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
👤
فرصت‌های‌برگ‌ریزونی‌که‌بازیکنان رئال مادرید در بازی امشب و بازی مقابل بتیس از دست دادند تا اولین شکست کهکشانی‌ها در لالیگا رقم بخوره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56K · <a href="https://t.me/persiana_Soccer/29352" target="_blank">📅 09:44 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29351">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NsC93Jtme6oJdGHXDbGMwLCvoRsC5qztU8d2Dy7r-0r6t1H3kzldMukflUgl-vcgxsfcZQ94Ppef6HSPK4dI8dnkExIzxpXmREfugclUcv48-rjq_mj6xG5XdvIiW3VhdKegUEPouIipzf0sZvm4m3B8VCSifcIyFU4IA0skGSO004Xhf6RYTemGYQ0YDb6xT-Z32YDhk9bn7gMiVIIholvDRkYStZ3IUN19P5bDaNOKpWJL2NN9Qcw6kMysDPqxskkYS6jBZWffx1_pAx8eb5scEKx7FBxGK8EleJzZcWz9ENBV9pHE4YnbeEYAulB9ZbWyHjeKqI8yo9_yM9dyNA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
تاکتیک‌ این‌روزهای کادر فنی اسپارتاک کوستروما درلیگ‌یک روسیه: نادر اوت پرتاب میکنه یکیتون بزنه توگل؛ نادر محمدی چهارمین پاس‌گل خود را با پرتاب اوت به ثبت رساند. چقدرم خوب میزنن تو گل!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.2K · <a href="https://t.me/persiana_Soccer/29351" target="_blank">📅 02:03 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29349">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JY_vawJTJO-mDKzEJ8auKbVpGGwLgKY-I9fgNq9HRvDAjH-RJ-zJAhdxVKhqz_hSFDI4LG3BGa7koqzDIjeTp7SHmgqiCqDFe2wpdzKVmX9VinVZpTpO5E1rorHM3Te8Ds0j4VwTj43U_2SV8cW2qeSVdljmWMiybCwD4bV6OfZTjEgj0hiYGlIe7TL85l8pK4o81Z1hkd4jkdjpIOCpdp0XA4kp4ni2MYDMXhGJ45JxUOgMHaH_FtgJmxKzR8DIIlDkmdZZfUXh_9nVf8ICwfqIDXF-IwgwGDCLG34CxymkvSJnYnWMaD3Xi_amYK4uwJ4pkQWjz-UeGhid9ifRmw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌‌‌‌ دیدارها‌ی‌‌‌‌ امروز
؛ ازجدال شاگردان فلیک با فاینورد تا تقابل لیورپول و اتلتیکو در چمپیونزلیگ!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.7K · <a href="https://t.me/persiana_Soccer/29349" target="_blank">📅 01:20 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29348">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eCVfR5L9HqSFsTt7Sm7Rp7ukFlKKgtqVKHKtI3JdSfOJRWPZv9NFKp_FKmxzS9QCpPAzup7phFuy2lDgRouTw0ehICZIC3F0HKG6cZwCnUMFg8VVXpNTWD-JVnrYpsBQGTxmuSQm85aLz0wXXPI6aLWKdkvXUU6baoVcT04b49nwKegHxuDQnCNjvlujtPqNMjHwTMKVvCXEYIAIUKFpNVoj7HUYSAfcVgHclTLypA-xvz6Mh02uF6J5xboI9axEFUDf4b57tKS7Au1gnxOpgAMJ2HiCwqnW7tVSCPUwPLTg8nm5jaRr90oJJlfSjfdb24P4Lz7jnwpj1uoKAOzzyg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج‌‌‌‌‌دیدارهای‌‌‌‌دیروز؛
شروع سه امتیازی رئالی‌ها در UCL و برد آبی‌های منچستر در شب دبل هالند
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.4K · <a href="https://t.me/persiana_Soccer/29348" target="_blank">📅 01:19 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29347">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Oxub4uQ44i1NAZGUE72bl2EsuRBNM6V5cGwVZp-ifl5l_N5G4wbgJdkNQ9E9HLNz-5G7fchGwMPA9WdV_zyCBfRZEWiYRFOdIPiWGN1ivOZV8wzb01C9WE6HDblr8S7A48ZKHBKLVWq-xEO59KuKYo5M7GtIVzZeRAVOzWO0g83lsEADLjNXe5Wn3CVQb4y6t-HznvAMDIRXfnlIS8DlbfzRLjJb8YrnLKE9GMvWFDJYIFLqfdPrJ0NYdBrYbyEdLmOIU6lAohW8LpWff-ttHsdZ30ajr7klH2fpiB14hZgklCAy3GEmNz02hbpNruoEgWmrMhTtJJWW0v4KoRTwSQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇺
در هفته اول لیگ قهرمانان اروپا؛ رئال مادرید با درخشش کیلیان امباپه دو بر یک از سد اینترمیلان گذشت. جالبه بدونید مجری شبکه اینتر که در تصویر میبینید گفته بود امشب‌چهاربرصفر رئال رو میبریم!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.6K · <a href="https://t.me/persiana_Soccer/29347" target="_blank">📅 01:04 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29345">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/NPM8gK1eami15peU_7b_nnDhYMHJBnEAb5ACFeR3TuZa85rAjFY_MmHY8Rh8LNwcru0B53JlLs5uWeIsqJ2sTQxJsTCLfjLH-TT_gngRJVY6Z3YYstQ3lSMOmobas4LaxppxPzGWmJtT23Hl3GzEJqrMjh0DbyC-C_6zqCvdXOS6aijYOgTMSUDDc1ZD8T9bgVrbeHx-f6m4ejdoDYXv1MdwuuB7TSonf7JAsS1Ugj1njEd1MzElogTT-Yow8a4Ln1uRxAKe8ToEjAAVClrP6uZI4zUFgQ7_vdW3sXKf5794Je7YosDT44UMHSF39s_NVS2F61_WTz3Mkt1-ZQ0t4Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/T3z2bBJ2dFPKCDQe9MZZalJk_UQu1dT5LUvrzFqhBCwH1CdbaijAk10txRLJWzVEhDm36y2ypfKsWu2Mk6DinDps4FWp9ZDTXqf8K3g3rTBvk0JW6s5KwuKSXqKgP_EjO5-sjFsFrwPlsuPsniXtgBmLy2tgMjFRBBUviozk36OPxGQq7k0CeW9JK7ckHuhjjvFzBRFT7v2LEaHCY4tePGUjk-tfFplJXOWbKqrGlsB2nMGE0-ktOwkJRi-ASkttBaqgo1mUc33E-cROFIl_oaekXgpwZmoajeUVaSQA-kKxvADCEOrK5bTvQooczIsnpAyUMA383AYpDSulGxUlhw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🔵
🏴󠁧󠁢󠁥󠁮󠁧󠁿
جک‌‌گریلیش‌ ستاره‌ سابق منچسترسیتی و فعلی اورتون در کنار پارتنرش؛ اون اوایلی که تازه اومده بود سیتی بیس چاری مست میکرد فوتبالش رو به چوخ داد الان باز بهتر شده!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.5K · <a href="https://t.me/persiana_Soccer/29345" target="_blank">📅 01:00 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29344">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/n7fCx35qcfdmSOKzYOnI_QWkBjtVDIOLGlx4vw2ultVs05ab7B3SzVVFfqYycS3hmArCqcghJuavgulXKbZJT10tPKxgYa1TUt6FxJU1UCLKk6_mdFov3QWGfEvABsCiQ-yf6Ep0T6Ez2SDy3D9OMTiAVuhK57HnjEyByIoEclqEEuD6AI6uZAFP9m-tjTbWdEBsHEwoDMttcxVM4nvWXTuZ70ijjFaqPnAUlfHL9Jim3E9CSPz8keTcnTGp25urEUsmXoIEuUWXSZ3AdDkOmHFZ8cRTHi9etg09WIFIPULN5DK5ei3u0ms33F39__7LsgxRFgYb7jcPtAn5JTaU2w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇺
در هفته اول لیگ قهرمانان اروپا؛ رئال مادرید با درخشش کیلیان امباپه دو بر یک از سد اینترمیلان گذشت. جالبه بدونید مجری شبکه اینتر که در تصویر میبینید گفته بود امشب‌چهاربرصفر رئال رو میبریم!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.9K · <a href="https://t.me/persiana_Soccer/29344" target="_blank">📅 00:37 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29343">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ftfTw0zaQYhmy2M3462JHkecRYsR1iig-eS-11pzar5b-B6ltZFiRFJcbGt2-E4zbOfmRScTLn-bmZdjsytDM_Sd8bOcuRWfgl10JdREDzCEH8k5AJqYNe0rzy4VGqStezYCd9nhMcqke6KWyWFRI95B2ToTUw7-m0PDOGTh9KToSQ8Rr8kUimD4z86LAfe-KugiaRsSZ8xYR6VCTuqq3ASc0zTzp_dlwneYVkVGb2cBpmwMvZ74dABD-CmQn9IXLS_oPQ4--4Al6ADtkrsZmNzdbMaUEt_5caHLUVpsh5eF67yvF1p3kVG2UJqLJ6muy45DS5qmGu_1L_hIidKmzg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇫🇷
رکورد خاص‌امباپه باگلزنی به اینتر؛ کیلیان امباپه در اولین بازی چمپیونزلیگ در دقایق ابتدایی به اینتر گل زد تا با رسیدن به آمار رائول افسانه‌ای، پنجمین گلزن برتر تاریخ لیگ قهرمانان اروپا شود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.5K · <a href="https://t.me/persiana_Soccer/29343" target="_blank">📅 00:28 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29342">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WEjA3xgH2yqY988EXv1kBomi5MBdkcWnarJYwSpL88c13aJkvZQXH_FZEMZDtEfL9OCBtP2_VO4P8le9gtgDGqrUnzZAjHbAvLosnHRvDaK80ghhK3jJI0YqjRVbXatoNTimewTDs6qJ-wABiT4C-sQ2K7l2rk6FT7V3Cp7whwG_mzrlOZIfWM7nqQ-zWVS_X8Kay3NHi8xBIqvjXXZsHxn-8wOrhTab3z3wxZFpgqKE9Quqd7WCrfAHWfgxnJNo5QmqFuMgmCi7FXwRJkZyr3HOqcecmVMBJ8E1z7-vf0PIvX7rR1tOiHmStqBM-cDX2K-Fu6cNeXJ5XGynKffHDQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
هفته‌اول‌چمپیونزلیگ؛شماتیک‌ترکیب رئال‌مادرید برای دیدار امشب مقابل اینترمیلان؛ ساعت 22:30
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.9K · <a href="https://t.me/persiana_Soccer/29342" target="_blank">📅 00:11 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29341">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/51b900e940.mp4?token=Hdkq9lsRIUUKdnq4MnYqdoAntg2Q-YmnAeuFLcfWCGQaFp8PP7sYLee7BNgppYn2esyFGgGeTRRS5_BJ0AqsSqTYyA-7ZeGPGIgXU8HfnPq3wLrrZ7egCJI1QWaHHK-L5AMZGs3EvSK13vVaiY11mYINpQPbapWLitmPDJgRx_QJQqRca3h7JaHdr7s084ig5_gVY27BRhh8-RUBxwyCOig3SDOKw0SBmU3gvS1dKdETE2Vr5aluYWFyjFSeboZnr0o0bS7SOaHf-h1li6fODBA81gusKdUYs5pBLRrVtmR4ansUK4ORyrBky6jUfsFuJisnWAxw8FgGXef7RuWrIQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/51b900e940.mp4?token=Hdkq9lsRIUUKdnq4MnYqdoAntg2Q-YmnAeuFLcfWCGQaFp8PP7sYLee7BNgppYn2esyFGgGeTRRS5_BJ0AqsSqTYyA-7ZeGPGIgXU8HfnPq3wLrrZ7egCJI1QWaHHK-L5AMZGs3EvSK13vVaiY11mYINpQPbapWLitmPDJgRx_QJQqRca3h7JaHdr7s084ig5_gVY27BRhh8-RUBxwyCOig3SDOKw0SBmU3gvS1dKdETE2Vr5aluYWFyjFSeboZnr0o0bS7SOaHf-h1li6fODBA81gusKdUYs5pBLRrVtmR4ansUK4ORyrBky6jUfsFuJisnWAxw8FgGXef7RuWrIQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
دو سوپر گل دیدنی شهاب زاهدی در بازی امروز جوهر دارالتعظیم در حذفی؛ ضربه سرش رو ببینید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.4K · <a href="https://t.me/persiana_Soccer/29341" target="_blank">📅 23:50 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29340">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/au5b6FzuayWnKEU1o6-CYt1wooFngoIktAajpvURLMrNWaP5C2n6LhhFXMp-xTyLxEKy7fwgc0sjl-3gIuwdz-7o0UMZakjWJOs5DBUlzd__PlGSmKgPIjLpdujez5i-emGv-pzhS7CW179y9vzx5ombE-vKTq1lMZz6JzDq6u_iaEAFsa-7rqPQL1traS4SqOEaLoRJQgPUu02m3fiCEtUM_I2jmRZcSzFj6_HtMQ9PGbeKitR0XEjrf32LCYEg1vlsjDtXtesPVCwxLYyH4ZeuPRqkU-rHK3bN7N1p7lDS1mXRQPbgXWCx0dVRz8UHTA_P_UpWYJ7SPajN2OGCQw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
وضعیت برگ ریزون بازیکنان السد و الجزیره در آستانه دیدار با استقلال و گل‌گهر؛ السد امشب چهار بر یک الغرافه رو شکست داد و الجزیره نیز سه بر یک تیم پر مهرهه و پرستاره شباب الاهلی رو برد. تمومی بازیکناشون آمادند. العین امارات هم حریف هفته اول تیم تراکتور در…</div>
<div class="tg-footer">👁️ 53.5K · <a href="https://t.me/persiana_Soccer/29340" target="_blank">📅 23:36 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29338">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">🚨
🔵
#فوری #تکمیلی #اختصاصی‌پرشیانا؛ مهدی تاج رئیس فدراسیون‌ فوتبال عصر امروز به مدیرعامل هلدینگ‌خلیج‌فارس قول‌ داده که روزچهارشنبه باشگاه استقلال روقهرمان فصل گذشته لیگ‌برتر معرفی کند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.8K · <a href="https://t.me/persiana_Soccer/29338" target="_blank">📅 23:03 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29337">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">🔴
👤
#تکمیلی؛صحبتهای‌پزشک.پرسپولیس درباره مصدومیت عجیب مهدی زارع درپایان تمرین امروز!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.1K · <a href="https://t.me/persiana_Soccer/29337" target="_blank">📅 22:53 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29335">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/UjuYv6SAy5ImMxyvZ-5Usc_Kblha_eUNSqkSbh12Nf6O3yL639foru-nhUtC1TWVh35Z-o9Wuy3yL0VYEzIb4VQt3fCHJ8s0tnqrZy1S3I0JWiwEsNPjYS1HlUFQ0pXOrNym7BkuoSMhsc0CFcWSqy8aej38ZAExitBYXSv0uOXWLyEu5vyng4S-mWBhRuM6aHTkYKhKtywLB3jjnDTkrn9gTWYBpR2Eanhq05Xd3n0hky-gB1rC_5Rew06UTvxauhqbTC3d_psBcL-b1_t8gJaxhq5gpyWO3qVTOPwhHnicT7MU6vS9Nen2DQ3CUil-aI7WvjDNyDjsm76IrbzAUQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/K348aqkE-IStx5tb18oR88U7u1n8LVYlccC664Q1xTkg8t-wNAB3OwEPaE0o2Jz2VKVN_8fSV3-q40M-jyfqA2yDN99u-zOK4ok3VPQXIGIP2TyX7ELBUah_QaP-XtYbPx73OuzLbQOFUNiPUyYBlRMdqCbM0WUORZkQY_DMYpGpVvNCWRKNnEBOvGJSm_VTXi72hu7RjZdg3jIp0HYILBB9-hqz7Imgo2IHAM97rwz3IhYHlmumAiLIIu4r2pNo8kkiX9kkZLn7OLa7qQXtWc01yo9s-Q4FLVGaO9O-YBykMcxLnlpdRm79CTIINYX-fOw8tdNapR4CC5yoGRo0lw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">‼️
زهرا گونیش ستاره تیم ملی والیبال ترکیه که بخاطر علاقه‌اش‌به‌کشورش پیشنهاد لژیونر شدن و حضور در رقابت‌های‌لیگ‌برترایتالیا رو رد کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.9K · <a href="https://t.me/persiana_Soccer/29335" target="_blank">📅 22:40 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29334">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0e83f3f081.mp4?token=XMCemHoZwVzon726L2-qJDh5DVDcTEcdKIqNwrFsilX7av4BAC8a-Te0jsgFNtk5uAe6GPO-JHMqs0KJixw6RuEsDWUl_WgimHqdPrVjznX2xkEwEauWeqG6Dow-1xGVOZTZgU5NBAu_m5K9vs6fTtIi_JuDEzb8wDOYbZnA4x98D7s0hGO9_vUmXHALNZ9QDIAASuKfBpUzNbHCscRTDWc85Z7hvYAC57OtR7FJ4STvt9PIYayYwrE-tlhMshQrBC2nxBNnfmaZkRhypi9QUNyJ3BYSI5WTRPtvn2BnNzZeNqTOdYcGemU-s7HGOJ2w8G0waewGtJLUZdDE4m9a8Du2P5Sr6iUfu7XTEIsH7mJaV9lV3R4mhNISLTzrjuiwEBMHWtpqRXj908KbpEbb_tSYvJKBKzZTGHwQbtTJs-0DZCwzLo7YOJv1ZNQbyFlthOYJIr6aKpMqeMTIvfBrJm8Wt2erkD3_GYf2qIo_ahfX834plnrYRzEtFgaFXD0_3WpnRdbb7rZXp3E5dAl_FlXhwTN0MrOV5okwxSnivOjYfDkvbJFENFtWOBrNJA3wcTjHhOeSCgYMqmTwVprPvXUT-Sb7m8JBe9flp2nrVovQ1JCELG1cMAUay38jZ19QN-PgEWCZjVI-hnZMEeVyQ6-yTUknL54A5abfdSVqWNg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0e83f3f081.mp4?token=XMCemHoZwVzon726L2-qJDh5DVDcTEcdKIqNwrFsilX7av4BAC8a-Te0jsgFNtk5uAe6GPO-JHMqs0KJixw6RuEsDWUl_WgimHqdPrVjznX2xkEwEauWeqG6Dow-1xGVOZTZgU5NBAu_m5K9vs6fTtIi_JuDEzb8wDOYbZnA4x98D7s0hGO9_vUmXHALNZ9QDIAASuKfBpUzNbHCscRTDWc85Z7hvYAC57OtR7FJ4STvt9PIYayYwrE-tlhMshQrBC2nxBNnfmaZkRhypi9QUNyJ3BYSI5WTRPtvn2BnNzZeNqTOdYcGemU-s7HGOJ2w8G0waewGtJLUZdDE4m9a8Du2P5Sr6iUfu7XTEIsH7mJaV9lV3R4mhNISLTzrjuiwEBMHWtpqRXj908KbpEbb_tSYvJKBKzZTGHwQbtTJs-0DZCwzLo7YOJv1ZNQbyFlthOYJIr6aKpMqeMTIvfBrJm8Wt2erkD3_GYf2qIo_ahfX834plnrYRzEtFgaFXD0_3WpnRdbb7rZXp3E5dAl_FlXhwTN0MrOV5okwxSnivOjYfDkvbJFENFtWOBrNJA3wcTjHhOeSCgYMqmTwVprPvXUT-Sb7m8JBe9flp2nrVovQ1JCELG1cMAUay38jZ19QN-PgEWCZjVI-hnZMEeVyQ6-yTUknL54A5abfdSVqWNg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🔴
#تکمیلی؛ مهدی زارع به دلیل مصدومیتی که امروز براش رخ داد2الی4هفته دور از میادین خواهد بود و دیدار با خیبر خرم آباد رو رسما از دست داد!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.9K · <a href="https://t.me/persiana_Soccer/29334" target="_blank">📅 22:25 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29333">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bZHnj6qAjuuXe5la9bAEHpgbUlmDbhicvoBRfV-tMHcB5kDkdj5jeno3WOXRSkKs33-xbZjdAq-U34Pm63c5N8KhVpN8TwkYs9iOvpv2sWcD-Wu3RfsPvfo5xAb8xeI740-piLSMLdGvBeN4IVOiAreASaCg8UwkJpOJ9Oe1Pd5D5OIl82c04Z2WP4lK8U8E0JE-3xTh-ZWHLQDzgFUzWlMJ4dk4McWbI_oyx8G8y8Z3DQmPSZPWTi_t6m5Lms1ZB5Ti5lX4IG27ULCSlcMK18JIFoylF6wkciucxHa8mUKBnEmpPMscnbJs270U4qZKEOJC5uZLfkyoHrsRfQXKMQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
ایننرمیلان هم امشب بااین ترکیب تهاجمی 352 به مصاف‌رئال‌مادریدمیره. مورینیو هم برای چندمین هفته پیاپی یان‌دیومانده خرید 140 میلیون یورویی کهکشانی هارو نیمکت نشین کرده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.7K · <a href="https://t.me/persiana_Soccer/29333" target="_blank">📅 22:18 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29332">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FMNQxTHDaO8yxmfAmLK8U61_AsQwnuuZr5EYy7d4B2_wP-0YUCp9NxFaJOycPujl12e_GeKb5M_eiq9G7X6L1iAbGA53WttM0_6zXQLJS2OSh1lUS-jxMVrm6i80rgmW9dKnkT0x_V3ySWI86-mUtwSS59YiPRWl2zHoZQszMlNoDBgwUy6gzboe2k9tvXJZ0pOeAq0HuTxIcYAWk_UtFrUegMvq-bakVO7lUMrCV5tcWeAVlznOpvNQalfpFvvg6nnC7Jj_A-omTD4XW9L2e30U-WmNquiXEeJ_U6VJTEClQbeOrqmDgFKpCeFn0pUKllPm_DX8Y9RLK1s1ebLRtw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
با حضور لیونل مسی آرژانتینی؛ لیست 30 نفره نامزدهای توپ طلا مشخص شد، مراسم اهدای توپ طلای 2026 روز 4 آبان درلندن برگزار خواهد شد.
⚪️
Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.4K · <a href="https://t.me/persiana_Soccer/29332" target="_blank">📅 22:12 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29331">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SPhI2rKjvqjYmq7j_Uov8z_uuWZECW4hvL9OZuNYTRpWROHhfQAAiFOPevGE__a3OY94wejavv9oGZnKE-L4QIaedrIhwJR-mOtHpirZoq-JS-QJchaxjmJ5U455m0torm-BPko8J8a504zlxC2IjRaVCA8PleUvmEBk27k_c2-yK96SaFUxFLsUvaYBeiQe-TVCpTy8PL9JHFifETdHMl3z46dVgSvAY9H2LxQsbjLsZ6oldOs27ss1lLUJYGk6dh6rsXswNnBUYmgjEAibldQF1_Kdd701t1cTTQExRprlolXn_pndAaJ4jNRHboT6pCQeZIynQT8VjFNZ92u-0g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇶
👤
عملکرد تیم دهوک عراق تحت هدایت یحیی گلمحمدی درفصل‌جدید لیگ برتر عراق: 6 مسابقه، 5 تساوی، 1 پیروزی، قرار گرفتن در رتبه هشتم جدول!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.2K · <a href="https://t.me/persiana_Soccer/29331" target="_blank">📅 21:57 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29330">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RY0W7verBp5ONMEYWRsPoMNfOZtYFFqk6TodM8648tUUANqx_fVpn0U5ruqAvRvWl9nfyKyibKZPFKwWaYInpNwrfP_svdpQMMV3FMrYcEsX_YCdM40V3WEoBmegLWgd88mIKgU0HIsvBHKl0qQjBj--D188jFK2Ejs7JLYvf-ELjpQagoPQFyljPMlG29ou-8G9N_nknbocFaYEFgILRic9rIwTl3fnYD810hofjjGEagfPEdkTyvHtv0ck4C3OW0nA-6siR5eIZEEJNv9RZ1mXgw-FodPZwUZTtiOErqTeyh2DcpYvrctQYsHx8FsfPkftxrZjeYVW1JUgJTb5vw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
هفته‌اول‌چمپیونزلیگ؛شماتیک‌ترکیب رئال‌مادرید برای دیدار امشب مقابل اینترمیلان؛ ساعت 22:30
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.8K · <a href="https://t.me/persiana_Soccer/29330" target="_blank">📅 21:45 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29329">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/felXiS7s2gB1SJNoO93C_Yogiet1QWuWJW-F-mppKTr08dVgFfLoUILMysk3XE8qX6Qq-rs8JuyfXXDdb3MKrApvqZKllTrmyPtgE1owN-UTGfOHEue3Lxt-xkmDogfnO1uFq6n39P5npBsBznnAxK4ti90cYX97NZVzuYImPmZF96zvUWLqm1obBvsqp0BQOViOYX1FNwIG8kHuCrXQ81N4hyqFlG9-dIEzQcf1chq4pcD929yuyqVOzcZ7ruhtN06BFkswaowVO3SE_acVEOY62Hi0BZbGCwJP4jPsQy2X4pk8lhvdoHrUuH2f5Pc1mNMI42Pq6x83euEIFRLhMQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
هفته‌اول‌چمپیونزلیگ
؛شماتیک‌ترکیب رئال‌مادرید برای دیدار امشب مقابل اینترمیلان؛ ساعت 22:30
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.9K · <a href="https://t.me/persiana_Soccer/29329" target="_blank">📅 21:18 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29328">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/939eacf7b5.mp4?token=hZg1qZ7HzloyWi62HAlocFOx-yEJmQ8bXWdeKS1VVEdI8-MnqO_x1o-3AG-Vy-815urV4Q-jkgvg6BZxtbI7F9pSLIEeMbp05mpW8Ts80I1X4fqt9M6KpVZUJ0w2P9xTqh61Xew_iwmPtE9HJq2UBzrnW0RK0bjdCfWOzwx4wXr3z6KMwlxTUrNVTvWVXnSXEoW5Kydm0gRz8bE6EVMA9b33EMDHPvfqhjvX8oABR3Ydis295k0mhIizqX3lHYyVUYtQL280YJdlt9ozuwDnQ_9m0mVYSkk2qGOPF9hqnaIkREjCPlrtcn3NWvb9rNQUbIP-Vq4T2sIvlRcwKW-uhA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/939eacf7b5.mp4?token=hZg1qZ7HzloyWi62HAlocFOx-yEJmQ8bXWdeKS1VVEdI8-MnqO_x1o-3AG-Vy-815urV4Q-jkgvg6BZxtbI7F9pSLIEeMbp05mpW8Ts80I1X4fqt9M6KpVZUJ0w2P9xTqh61Xew_iwmPtE9HJq2UBzrnW0RK0bjdCfWOzwx4wXr3z6KMwlxTUrNVTvWVXnSXEoW5Kydm0gRz8bE6EVMA9b33EMDHPvfqhjvX8oABR3Ydis295k0mhIizqX3lHYyVUYtQL280YJdlt9ozuwDnQ_9m0mVYSkk2qGOPF9hqnaIkREjCPlrtcn3NWvb9rNQUbIP-Vq4T2sIvlRcwKW-uhA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📊
به بهانه شروع فصل جدید چمپیونزلیگ؛ نگاهی بیندازیم به تموم قهرمانان این رقابت‌ها از گذشته تا کنون؛ رئال مادرید با اختلاف زیاد درصد جدول.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.2K · <a href="https://t.me/persiana_Soccer/29328" target="_blank">📅 21:01 · 17 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>

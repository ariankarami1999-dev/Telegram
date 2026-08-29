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
<img src="https://cdn4.telesco.pe/file/XETzMfOayefOqAtJhcquM30reFV5FAAe0IazcTHBgxiK8PVoh-N5VGtUWPaAec26L5m5SHIB7r4vss_NdaNOIB_j1hNX_D8VQhYpKx0NrsZYh5RViVdgPWuxTYtPEnW44z_-ycmh11DPfwH-WOAT9Uxg7Cj5M3YMkzshiISfv9YtQ5m4ZzfuDHylfXfh3bu4SelNxacmrn6fuFM56sR5739Z3n9qXCSPsFi3SUFHyUn-YdsbIxSaSlLDYnYqk_vCg2qQ2dsGPVjLBMJDD8jvDJJluim57R2zGa3XqVyhDESux6XNi9BrscDaknlUNVxLNAYTuXwkAuOAcvkuliDjng.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Persiana Soccer</h1>
<p>@persiana_Soccer • 👥 635K عضو</p>
<a href="https://t.me/persiana_Soccer" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 پرشیانا ساکر دریچه‌ای تازه از اخبار محرمانه و داغ فوتبال ایران و پوشش اخبار اختصاصی نقل و انتقالاتهماهنگی و رزرو تبلیغات:@adspersianaکانال دوم رسانه مردمی پرشیانا:@Persiana_Plussپیج اینستاگرام:Instagram.com/Persiana_Soccer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-07 07:44:06</div>
<hr>

<div class="tg-post" id="msg-28648">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NC7G-L6Ttqgkbq2HlTPnwmg72dU6OoAUIAly782BUDho4M533sH9V6QkWco-xqO79aNDFfwUC_rHuJGdKL1QzLpwmpO0KaJV_Z-_VEHeso9JxUWzb8Esg0GGeXmrJ1rZ5etGDC1Ay4gsD8lmMsMaWOdVKKkvNwEOwShDnma9f9Nq5KKqqJfFReCiVTeheXs4ableHfDNBk1I57JNdYKZ9kJFMLoQxci7dH4-749IV4r5lBKJBCQI1jKR6Z_GshaL7LhOKEKeLeVQ5s47LALqR5Ej_dxiduJBnDUfH9LX0_C2vEoAj6eGlr3XtqJcIFWGUvF6ZNJ3EXbOzmFd2Fw6jg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
شماتیک ترکیب احتمالی پرسپولیس برای دیدار امروز مقابل ملوان انزلی در هفته چهارم لیگ برتر.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/persiana_Soccer/28648" target="_blank">📅 01:45 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28646">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XRpMZGeSY_gyVj82YAT-dHRlWVY1wuUowtvfZyE6s8nt0rUQPYckadndr3jWO15_b1qno2H8AYklpRV7RUTFqp4y2HWdmSXFrvk9dGLXIaWdSQudYVYIqDk2B9t5b8J3yy3v8ivwKWYol88kBByUxkVHdLLSgs9LieVaVWpUD__ZCIJEt7c0U5tqRUvovLgvCZKW_xpcoI4p78jaVCjSutxayCm0EnUYFkuQAX_HdKs-OPscuu3ruKXJwj2qBYswksKMpLKKJYNMAR8CcOgeODDDdI7adL5f6QWrhnccsNTb0ChdWVVsETbhyhORJSXuViGTUVagAoV2S_W7syZtzQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌‌ دیدارها‌ی‌‌‌ امروز؛
مصاف پرسپولیس برابر انزلی‌چی‌ها و دوئل تاتنهام با شاگردان ماتیاس یایسله
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 31.4K · <a href="https://t.me/persiana_Soccer/28646" target="_blank">📅 00:47 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28645">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oEPzhq6OKBo3a3hi077DTiyN-1SEQOSloQdc1Y3wZ9gbBLmpJnWJ5reKBEjhuSttpVNIIaYuoum5D5l8UFfIxEjvtxj1Pe0iB5cEsrJrNUZAslPBC91WKE4-hCuk51_HtR7bH8D7-SANICi5FPD4SHsr23ZB04HSTJxytU1WkQyewmDRYeFFoO-lhpNxBl0imPpLFnQeprY6m0_MDWYt3M2Sf9To8OXcRKuCXhK5HDkVck2JVIu7-SpDnA3bywxkHbeuDeaRY8juRokkzE2ECfZUluqnZ62x1hZ_HhGq0s8m3jVjoXoRjZgNQgCkMb-TArLNFS3EKPWTYSvzL3idSA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج‌‌‌دیدارهای‌‌‌دیروز؛
ازتساوی‌بدون‌گل استقلال و فولاد تا برد پرگل‌بایرن‌مونیخ و من‌سیتی مقابل رقبا
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 30.8K · <a href="https://t.me/persiana_Soccer/28645" target="_blank">📅 00:47 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28644">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/D8liOPhALxuMaf2PMeC9ryAcqYVoSUlDAV0FH4UVc1XVRyA-_f85rogLHQBc-AyoSbWaC4Gz1h7h5thTB2qCHjoRxONOETRWsTYSxy360ihHsORRvNRWled47iYnTDqbBUe7FsZLjOOz7Os-pa-9AYP1s49tL8q10SYxVTaLeJCZvkBldKUpIVXldGkU0taKiBN_N8GDRHFrSYmmZWb1k-V-35J2bygn-VHVedFllyADdmDjHx4ljJFAqyt5WM7MxqA5NClama80pWgk-jTfDMyBjj18_BahbUzSw-_QvVbx2dWsI_G5HuZ74oF-dQpUXgPNHLMbMhv0W_BabIcCWQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
👤
تیم سپاهان در هفته چهارم لیگ برتر؛ با دبل دیدنی کسری طاهری 2 بر 0 از سد گل گلر گذشت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.5K · <a href="https://t.me/persiana_Soccer/28644" target="_blank">📅 23:53 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28642">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/nspNbG-okgTvOla7E99KeeJT3wdUAfLvki3H-m7APCJR6S6N5nZYxeO9oFTw6pg99_HkY0ghAhMxZP8fH8MW-Fpw1cXs_1l7i4-Y4jXErlTOK3hHZGO_HQoNg3WjznMOnswSFfOL1JlbkqitfUf4QqYYDl5oZ7kIrp7p6ZC2-X9iDZkI-25HrpPpaeSUH54Fw-XYXDolabgAlqaJs-VJcJ-N9xdlGrxEB6JPIFc953PP5dEQqH5CtM3QdFRAlBV_UYbPjNIPtrG7HXd3zGkUoO6KyfDUtBHhdp4jOxh8U_weQOKZjS4JCKt2cDeW3z-tjl57CpEKomF_IHn1rAgClA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vpNkTrXo6fgiP23D3QRewaYtwkwuEA9ADf1l1yfZ3bYaHltUzj1FZFvIxc1VZICS9gAIxgve_xZkRZTptECjxAbzUNOJ9-7oyMzRtTAv8x8H6aD-sMAUZjH4-wwR2mOLcCT4BZ4IbnDjCegYebCUZ1VNiYeJoKuiWjopID5eYrMNotKi0uursULuwXqA9d4CorzefNUq9isHKW79pifFz4Oc5iziKfW7xY7lacCZKvEFq29IJdAU4TqgTibLtntcUNpyIpW7QozkHsm_CkjuJplLqbqhPX096Ui2LgTXsQjcpPXftqGvjW85lXYN9Jm2itbF7YW28h1Gw61Rr_NFlA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">✅
هفته‌چهارم‌لیگ‌برتر؛ دشت یک امتیازی شاگردان سهراب بختیاری‌زاده در گرمای شدید اهواز؛ آبی‌ها بی تلفات به استقبال شهرآورد پایتخت رفتند.
🟠
فولاد خوزستان
0️⃣
-
0️⃣
استقلال
🔵
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.5K · <a href="https://t.me/persiana_Soccer/28642" target="_blank">📅 23:08 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28641">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aOIvlNmMLZJI5Pft4gO98ZbVNCtBgPc0nFQ-C7kZ_sgHKKDdzyh_gt05IYhnzBOJk_n79OmA9K847_NSCP7-33m80rjPMNHCezPhuF7mtkbtoF-OHzCDxz2cv_bWa2OiZZBH7JHRke7TNyzTlhEQsff4xhmGPQ7X4rcnPriN5ZQksw-CpPbiSP3mVdtxrXI1xvelUGakssA98YsjFYIBbeTxLtgGjyaYlUy65is3pcpdziS23qjHtJjx68OsHEL9AmBnl3OuUPm3oonRisq2rOg5Gk5FOB5_LwhzdFD6rwWH2gRvvvPSUimqm2LK9vnKoeq2DRxB9V5rALBLYdYv0A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
آمارنیمه‌اول دیدار امشب‌دوتیم‌استقلال
🆚
فولاد خوزستان در هفته چهارم رقابت های لیگ برتر.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.6K · <a href="https://t.me/persiana_Soccer/28641" target="_blank">📅 23:01 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28640">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8ffc6c7296.mp4?token=c0d9LRNUTrX2kka9F81UnlZQfPiTyNPGvO7smMbd3AFe_2xbviw5S2JoVrPgi4rosaPmb44dtg6q82E9KfjN07o1aqOOH__t8CzQkHJDq3gE93Gb0xxxmeplvmg4GLxJSt6KDerd-jkmylbhWWEfAXkqwvp2jpw6FRgJzmnjPfc2HkFjOQv6d1Sm3X6ONjVzffXcYxXCVQvqha-rJ8Ev1GE-I_0RF_wDUwvbAYwbseuDAhL11vDxoho64ggZHoieFZxPpqGFhw8Qt9Dozd6Dku658Mjc1nxGDk-uUSPrEgYaxOZ44ajfYeo0ElpdN7QEG1C285vPDof8hBl0guurFoQj3ssn-wYF9Ix3eVadT_KF6sb6TAb4picJh_AExXKdzruXq7jTUltfDLKMdBlm8nvK8HZQpXcl-2qYDHIJcKSdfVjDk2wkVF_qsbTAwE_xqo5Ty-U5dGP1OMXYXkumEemzCNf9Js-BxwoLbhP33O8yS_6fETK7VGT2H_GGDbLJOQimVRBZ5rKXrb2Xrzq6RxzkOxnriKs9yzQfktz3le1G2yIuvC_gLtHX1zpjGC3ujXKiYWQNxT3xa8J6Mdm6dkvs4EYIeZAY04RTcWqsiVN3uWb_YgKkIiBQ5ga4bADlk5rSkBqaEucOiPkdGNSNo1a5ryCr1UY5HvFPKrxFxc8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8ffc6c7296.mp4?token=c0d9LRNUTrX2kka9F81UnlZQfPiTyNPGvO7smMbd3AFe_2xbviw5S2JoVrPgi4rosaPmb44dtg6q82E9KfjN07o1aqOOH__t8CzQkHJDq3gE93Gb0xxxmeplvmg4GLxJSt6KDerd-jkmylbhWWEfAXkqwvp2jpw6FRgJzmnjPfc2HkFjOQv6d1Sm3X6ONjVzffXcYxXCVQvqha-rJ8Ev1GE-I_0RF_wDUwvbAYwbseuDAhL11vDxoho64ggZHoieFZxPpqGFhw8Qt9Dozd6Dku658Mjc1nxGDk-uUSPrEgYaxOZ44ajfYeo0ElpdN7QEG1C285vPDof8hBl0guurFoQj3ssn-wYF9Ix3eVadT_KF6sb6TAb4picJh_AExXKdzruXq7jTUltfDLKMdBlm8nvK8HZQpXcl-2qYDHIJcKSdfVjDk2wkVF_qsbTAwE_xqo5Ty-U5dGP1OMXYXkumEemzCNf9Js-BxwoLbhP33O8yS_6fETK7VGT2H_GGDbLJOQimVRBZ5rKXrb2Xrzq6RxzkOxnriKs9yzQfktz3le1G2yIuvC_gLtHX1zpjGC3ujXKiYWQNxT3xa8J6Mdm6dkvs4EYIeZAY04RTcWqsiVN3uWb_YgKkIiBQ5ga4bADlk5rSkBqaEucOiPkdGNSNo1a5ryCr1UY5HvFPKrxFxc8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👤
گلزنی رونالدو در بازی امشب النصر با التعاون؛
این 978امین‌گل CR7 در کل دوران حرفه‌ایش بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.7K · <a href="https://t.me/persiana_Soccer/28640" target="_blank">📅 22:47 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28639">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ge6eHv9hAVMJI58dmRt8KtSV_c-izZijGH2YWTtjredgK0ZPkZ43BIZ32V-LU-qcn8GkCC3t1zTsC12ABOuE3W0KWn3rhXFlj9PsIXNNZplce9-QTy_qUQ6yEnPsRA01BU6_xbRLOxTVYSaYW9auWa0K2tXRd2CE1Kd4mWcVVwvC2KgxlVeWQoyD_45DFrzCYnCjyXZg__gJkCWZy2SxrndDbWF7SIWPXYdVGMhJlKy7yriyY6Z2FQ4gAd00YL9Ff0XEtQFPAlIAlHWeYCbVv4C7Tjvd0NAeeOUdiBAqSVKwkfo-6zNc6rHkN19yBB7TJyZs6O__vdViPZap8fwZXA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
شماتیک‌ترکیب‌استقلال برای دیدار حساس امشب مقابل فولاد خوزستان؛ ساعت 21:00 از شبکه سه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.5K · <a href="https://t.me/persiana_Soccer/28639" target="_blank">📅 21:56 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28637">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QNuv91RMr_onBlCGXDgup8azDNsRbAugMZ22bVarseUBUjMEP1sB-1qriMCh4hpMQZei3w8DTxtTe6kv3ziA9mBLxaVKBlSH3ciKCjO4RJw-Kv8kNLYE-FOk79vdjEfpTXmeYM7P4EkoHjRQTQW0Apcgjif6dSChNqdRWrD_9-Z9rIr9MiJqgYMkrseFc2Zma1QzG8D1pfC3A3CNLHjoIJRtL3KSRdVVfQeDIATO6xQIWH8UX-XMFJraRoLdDekjM1P8XMGk6bHexLs_SLcfl_O4QXG7dOqskpJ_-u3XHgzDv-6p--kX1Iphk4AghHXwz50cdWFG5skyCrGU4yEGSQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
👤
تیم سپاهان در هفته چهارم لیگ برتر؛ با دبل دیدنی کسری طاهری 2 بر 0 از سد گل گلر گذشت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.6K · <a href="https://t.me/persiana_Soccer/28637" target="_blank">📅 21:49 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28636">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/17182aab77.mp4?token=iM_7S71Xrg-DtXGSgwmfw1SGwexaJjcsFHQmO0-UKGiN-OL2794y-2qCWXvmB0LImMf68IsF5qTwDXUgsD5tWeLrbRRNzMWjupgPRdy5ADWeVuP5KUGslDkEo-vYdtOPeC-XvTGsEXQRNX0kJqmp8DQCV8N88_fhMVXwUFwkXu8da8VBZuF4slepdm69IXQJLOLrb9qawgn4UfCOxgIMtG2QWYSwlUezFu-VPeMhK5ktwHTT20dnutijTJ6q_lJRvE1itqaVQeGOt9A7HdsB8qzImYZBrxHla_amkscfmn5-59yuHhveczT3T5CKAp4P4OjxhgZJ1vzes-Kllcab0w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/17182aab77.mp4?token=iM_7S71Xrg-DtXGSgwmfw1SGwexaJjcsFHQmO0-UKGiN-OL2794y-2qCWXvmB0LImMf68IsF5qTwDXUgsD5tWeLrbRRNzMWjupgPRdy5ADWeVuP5KUGslDkEo-vYdtOPeC-XvTGsEXQRNX0kJqmp8DQCV8N88_fhMVXwUFwkXu8da8VBZuF4slepdm69IXQJLOLrb9qawgn4UfCOxgIMtG2QWYSwlUezFu-VPeMhK5ktwHTT20dnutijTJ6q_lJRvE1itqaVQeGOt9A7HdsB8qzImYZBrxHla_amkscfmn5-59yuHhveczT3T5CKAp4P4OjxhgZJ1vzes-Kllcab0w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
هفته چهارم لیگ برتر؛ شماتیک ترکیب تراکتور برای دیدار مقابل چادرملو اردکان؛ ساعت 19:00
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.4K · <a href="https://t.me/persiana_Soccer/28636" target="_blank">📅 20:50 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28635">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/28930c27fc.mp4?token=ITD4VyunWZtCCZXlKw41IJ8O9PcPVr0aInRbMTzUXx84zw33EV6eLLlcErr6ThDYGv2z4cvpvi7Z5tnM42pUSZeqiI8Tf4TZOfNbnPiKE4GyEI1bcp5y-yYqjoQ-M21PVODFokVOEwvjnrZPhWWiyGq0QWNBEO2LczHA74F7CFptsUDv4XShPdnudQM0ndeZ1IQ_vXpjKXzgpKUrHJ1cK-lIUmGEVqYCQPxQJP7cihZNUoyj0YN6V4fRYANaEbMpO04XrvxqBBLRNKsqJDGS_KmZ8ZAQxcry-Y0n1zKBO5a-vArmLgMwhUbAw1FF5BY_4uFgcs9t6BqcYTLU416sjg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/28930c27fc.mp4?token=ITD4VyunWZtCCZXlKw41IJ8O9PcPVr0aInRbMTzUXx84zw33EV6eLLlcErr6ThDYGv2z4cvpvi7Z5tnM42pUSZeqiI8Tf4TZOfNbnPiKE4GyEI1bcp5y-yYqjoQ-M21PVODFokVOEwvjnrZPhWWiyGq0QWNBEO2LczHA74F7CFptsUDv4XShPdnudQM0ndeZ1IQ_vXpjKXzgpKUrHJ1cK-lIUmGEVqYCQPxQJP7cihZNUoyj0YN6V4fRYANaEbMpO04XrvxqBBLRNKsqJDGS_KmZ8ZAQxcry-Y0n1zKBO5a-vArmLgMwhUbAw1FF5BY_4uFgcs9t6BqcYTLU416sjg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🟡
👤
ستاره جدید نیومده گلزنی کرد؛ گل اول تیم سپاهان به گل‌گهر توسط کسری طاهری در دقیقه 6
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.1K · <a href="https://t.me/persiana_Soccer/28635" target="_blank">📅 20:40 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28634">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/L9Rbq_Nmd6JvZlb5-6abjJu-SS9hVW2AU4Rw4LLOtg7nSdJJoYZU9hTan7C5HteMHDfSzZxGj84rC5IXvSwDN7TQ_AN7yg7BxfSoqp-eBwZzC68apIEXY1NDlQEkFxe1Lj8X_-acILM2PQ1PJt4wBcaeMrQ9T3tMdli2z6MVESNG1R4f4R3MZFmzlV2I0g2O3nILgn7YYpsP3ZxnjtRAbzkE_4N5PB1wSoKuBd3eoDgSMrBPDkkfo6yH-6_R2lSM38L2Rg820QSuBbxkWR7OcFtJzWZJHuQdWrOHsgGXXB4kQTgWSx6KzFO5XZHwZEfuV0YlSSzYgAgAeq-A1rhNrg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هفته چهارم لیگ برتر؛ ترکیب دو تیم فولاد - استقلال برای دیدار امشب؛ ساعت 21:00
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.1K · <a href="https://t.me/persiana_Soccer/28634" target="_blank">📅 20:21 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28632">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/XoJ7HBQODNfoDTVzQW5Xk-RoNa-qV85-PYuMVY1GzbtJ5OBm5lAeQnq0y7KVrqEeoluwcO4YAU8v_Xoh8GIXA_bbv0p74vmOd3Xgc65R1VnToBo50OYmJusvsucsVM2H3nbd1jbgs_o4D9O4vMbU7bcgOuFaAurtaoHM4nlO1kpCnk17AYDY6GCjl6Lkv1WKsc5a4NJw2TCjTYTn34V3kS7Wxpz27QA2884i7Rk3MLfP41VWIX5mrZ-iZWnIlN8JvKq1ATYhNK9Ucp10qGmHTTtNhTvyCE_0htLpcXoVUvr_DmaONgebbMDfva1CjywZeUtUoVP8OfKKJwNJ1SIs9A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/bTdQm4M1s28nfxL-OwZjcNJVFTloU3FEZ007w4nSks9H2meCzI3FpeEnk1PU3-XEfk7d0VPQ3jDgboNRhI5SeRh_AsYmrOQCkZ-IfZs5FWibybWBiezhXtqIan29Y2JxuDKyzmS3AULzzaH9aFdzsg9F13FgnrGk1NweGsORa95meTd_9t32zIbO8i_9mLfpGGcu847P1cacmGWI4SHSE5qmPLAGKl0TLJKNwNFYQLXsnsOyySdiARRrijHMe4AgkamUtpxL8u9hYi0itSibJ9BkXKK4-2BuZLXoKdffKTM9BmeeFVJUvGX2b6dVsyMPF_vSMjek-B6tyNGOxLAWlg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">هفته چهارم لیگ برتر؛ ترکیب دو تیم فولاد - استقلال برای دیدار امشب؛ ساعت 21:00
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.4K · <a href="https://t.me/persiana_Soccer/28632" target="_blank">📅 20:18 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28631">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f8b6a569c2.mp4?token=YXdEYGovejt_2rGkuJlFpkvYpOarzqwekR3vbBigWE7UiYfqPprUS-PMNQ_OGBkZUYVed-zA5r0FAMw3eI8we1c_-bR86vvAktKPxvO4AXjSIZGJKWYsj_xTOvLC-LoSciuqIdMKCMEHaE6GYWqsYCo-TIJtwHOXQhwB_J2UGvgoUyS4w_RUNTjbopMgpav0DxAxs-ogi6wNzPIATfnG8iiKj9nv9Upo3cxHC6kowYpTCSXaIpw5JUoa84iHbQrtQz8v9vB2Jg14DBF-jjQs-7fsw0uVs4DBG9A4aBHaN_KWOcJuxxlThDQo6GCfR8wik-fLhPb7htdCYPHaZTvGCw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f8b6a569c2.mp4?token=YXdEYGovejt_2rGkuJlFpkvYpOarzqwekR3vbBigWE7UiYfqPprUS-PMNQ_OGBkZUYVed-zA5r0FAMw3eI8we1c_-bR86vvAktKPxvO4AXjSIZGJKWYsj_xTOvLC-LoSciuqIdMKCMEHaE6GYWqsYCo-TIJtwHOXQhwB_J2UGvgoUyS4w_RUNTjbopMgpav0DxAxs-ogi6wNzPIATfnG8iiKj9nv9Upo3cxHC6kowYpTCSXaIpw5JUoa84iHbQrtQz8v9vB2Jg14DBF-jjQs-7fsw0uVs4DBG9A4aBHaN_KWOcJuxxlThDQo6GCfR8wik-fLhPb7htdCYPHaZTvGCw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
هفته‌چهارم لیگ برتر؛ ترکیب سپاهان برای دیدار با گل گهر سیرجان؛ ساعت 19:30 از شبکه ورزش.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52K · <a href="https://t.me/persiana_Soccer/28631" target="_blank">📅 19:44 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28630">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b1bdc45bb6.mp4?token=GCeCOdxH27Adxr1ev-o_bIUaUVnrvnNLmWnNzAi9fZgKOMEW74oGWB-XDz8S4kwzCoIjRL-VLHSLcrHhjn6hQ_eJ8sSUwDaTnqQmLlAyZ0pSzqr21RaMxB9BwbZIn0O7pEZjU1WutNsOQCRAiFJeohzyuKah_YN0Cb4ntLJUvj9LHKpE6HF_n9O78rfE8y5bP1t89H_NEpQ2SHi9uNX0k-IXBZtjlfS-0Vqgd91J3vPjo0OrTvxrDCXQ6PKuROW8cBQdjnQXLAp6Dwu_i3MS2UX-16PWAaI5YXK-TwfI6knIhrLQ1twJ0TytJNBpRz5pHz3sjotBOr8S-1tzuXwpKQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b1bdc45bb6.mp4?token=GCeCOdxH27Adxr1ev-o_bIUaUVnrvnNLmWnNzAi9fZgKOMEW74oGWB-XDz8S4kwzCoIjRL-VLHSLcrHhjn6hQ_eJ8sSUwDaTnqQmLlAyZ0pSzqr21RaMxB9BwbZIn0O7pEZjU1WutNsOQCRAiFJeohzyuKah_YN0Cb4ntLJUvj9LHKpE6HF_n9O78rfE8y5bP1t89H_NEpQ2SHi9uNX0k-IXBZtjlfS-0Vqgd91J3vPjo0OrTvxrDCXQ6PKuROW8cBQdjnQXLAp6Dwu_i3MS2UX-16PWAaI5YXK-TwfI6knIhrLQ1twJ0TytJNBpRz5pHz3sjotBOr8S-1tzuXwpKQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🟡
👤
گلزنی احمد نوراللهی برای اتحاد کلبا در دیدار امشب مقابل اف سی یونایتد دبی در لیگ امارات
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.6K · <a href="https://t.me/persiana_Soccer/28630" target="_blank">📅 19:32 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28629">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/r9DnPFH3V0BA8W7nP6O67MfXrYfEWaKLb0hLDkdvQZUel4Im8PSLNJ86iBAvRnU3xOe8Bihbw3Yy_VMn2nCYmM_2cj6KXz_WNuOqOZsBHTYBFbIEHwgOjGWDi9wQtYmJG6Zz__MEhLMIbp7QquMU_UaQZEQxYaagrkiPBUKw1YRlZvc6tAq_fxneOHaVZCaDPHqRfWac_nVdcQR3AbdGPXtS0_BlW0gvfCEwbbFQF_hCd8FZNCilqd-vv1iWav0WOH_sljl2HF_M_nZuMO7L6wBwJ46mv_qWW9Ml985uONOnE9fYlVDMzTMyBFCicFcxfudHImNTuidHboGQ9IA8qQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
هفته‌چهارم لیگ برتر
؛ ترکیب سپاهان برای دیدار با گل گهر سیرجان؛ ساعت 19:30 از شبکه ورزش.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.3K · <a href="https://t.me/persiana_Soccer/28629" target="_blank">📅 18:47 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28628">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qbf-yZxvlQSgN1NZDrrFvKXRsBpZ4f04r8U44mLSWR-SFAndencETV5kQYejAp5zLApO-UClqn_VloFr0gYNj9w5Ha72jfz5UH3oHkS9IvMphUNWEGAgjzUayLT5yfrxZawr0T_2cR_lHTNrI5yPHq6rFqKoxBFQ93WelOe1HxDdOMnWSeZHynUsPNpx0xSBQIUdggAG91c7RrkHmRaJ_EFp-buJMc2XjhpHa1y_POrOTRdYG_rlNcb1Dy9WRUS2AC7gTeEFpdMDel_hq8ESzoquXrANKupNHRFeV78rDbJA-BYeUp8OhXw1mBeD_OlDns3HgM4HHK84foz1xeulNw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
هفته چهارم لیگ برتر؛
شماتیک ترکیب تراکتور برای دیدار مقابل چادرملو اردکان؛ ساعت 19:00
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.8K · <a href="https://t.me/persiana_Soccer/28628" target="_blank">📅 18:20 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28627">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CFUM0IeuWKLQljS1jOtZF_NfyHK26KukvFcN2uJFy8LxPJSncE8VQ1aX1OpGEflzUBWu5USvJ-zHq1ELckagY2PLv-TxUXxebgUzELFIzmnoB8SrjzQzE-3108_xeJaNOv7CS7e0A03HFUGSaXlqiBzmPzoTsj6lrXdClJ-6n8U663NxpB4NLMK5EJweCGNU5rn0rxkHfWvl_CaPuVCRtHUkZFprjVAxuo8RcZ812U08IiR7EJ_-1UEifCGOij2mV5SSuIDD1nAvXOQVEIIVFZTw7CM1uBGJ8S5kcjgWLZ2HH5vq27wwS1ehIXsvR2osTd4bEH_Lb3jAzzPb1Qbf5Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
لخ پوزنان لهستان با الهیار صیادمنش و علی قلی‌ زاده در لیگ اروپا مقابل تیم‌های مطرحی مثل لورکوزن، بنفیکا، ساندرلند و کریستال پالاس بازی میکنه. فرصت بزرگ برای الهیار صیادمنش که کریر فوتبالیش رو یه قدم ببره جلوتر.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.3K · <a href="https://t.me/persiana_Soccer/28627" target="_blank">📅 17:46 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28626">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aMpG_Q86bkNxwLOjylDgK9E1oqvzVyvmjEHR2_jrRx6b_wFOv64_sp3quoaVld7sgkkkUJMwevENVlvutfXQrDD_blCNCcBL_0gpIf0IaukeSOR1ldmuU06JeLtv1cDnXzLG2wN49b0sf9RhuIdYvcAEEBr89n2GK2Q5yTobzBtgKTQnFS9XQ9y2rKTcBHh2YkssF8Ew5PL3UlW7unjkkJ2L_gfk6KZ_CPcg68TGTZ7s0LS_iS262ksZ7nuaFccigXZOPslx4KK9KKNsxhmx51nvOcxPo5RdiKzhlAurF_CFioPEwgcnBA4OfciPAcTOEQy6WYrdWuVifINLww4x5g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
ترکیب احتمالی استقلال برای دیدار فردا مقابل فولاد خوزستان در هفته چهارم رقابت‌های لیگ برتر.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.7K · <a href="https://t.me/persiana_Soccer/28626" target="_blank">📅 17:15 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28625">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qUQHwH27NtaUyEzqfdQfknprlBQAeGcaITj-cXyRPLJ-VZA7pznOgD-Z-TowNRp1UkV9uz2kvslQ1GVDfgoqRYPi1XnPa25rcA-Gw0jNENHF_CjyvM413Sj9shGx_EsIHc71pq_X9MVsxYuIJ9NFhZGsPtY7IT8x9anIcqZWHk87gYmrU1J8Ox1CsgSqB37yUoQtPdq20xs2-sk9ZF8wxqEUL3XfM8Fj9A_r-MrW_JnwhhENa7y5WjsCa6spGbBG1O_GkLf7THv4cZfkYcrP55xPmpqu1ZQpNMzCZ_63nE9rQFS6gZ60mu73LTMjrDst6zliJM0B5nEeB0Aby1MaQQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
خبرنگارمعروف‌شبکه SPORT اسپانیا که معتقده که امسال بارسای هانسی فلیک قهرمان UCL میشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.3K · <a href="https://t.me/persiana_Soccer/28625" target="_blank">📅 16:55 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28624">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lXGuziSMPHgfqlL1yvyLT2APNf8mpVZTyeRbvpkq_50nYSyhhrb6l5G5k3ooen02aY1Wif0oEZMVh_UMkv5axWMynyh-idN7N53At2mo7BMHUGfUxEbQ1tYkHA_3QyMz6iwyTe6PZHS6WWI4DbnII44zTGpv5e-Hg0gJ16egGdhOyrgBGRZ8Ix61yPX0DGGrgO4Y7h8vz_Gm7y03wAin3AT21dFVbh7R0zzdniArb9ssJF7A9ZSrzbIbzPx0UnrcIIZZVKkxNNviKBVhvsddA6Jwn7OdzXPokzWXBBVFc8As8ClAGBe2VB5URd3HNVV0YCQKagxchT44nL4Y958v6Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
خبرنگاره از تارتار پرسید و گفت چرا اورونوف و سرگیف بازی‌نکردند؟ تارتار برگشت‌گفت به دلایل فنی بوده و حتما یچیزی‌ میدونستم‌که بهشون بازی ندادم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.8K · <a href="https://t.me/persiana_Soccer/28624" target="_blank">📅 16:38 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28622">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/sNKuQoc-FJ_jtmrtthFrWhtgqN75zO7usj1lu5NQFEFxga4PkfidEgfymBWanCM5qffzCIruiX7g_R2quJjiVqZWJwOqpsU-zYLXBnXh6cQW5G4EYi4mrT97FFNPmriHJoiNwv_c0P93l-qyJ32YYmvm_oGbwiRHeDo_cEpXoLF_z1KWKbqpK08sdk4i6kHHBQfX3jU84tdgANki07c9CTlY4Xl8T8tTg7_Zb5m2BgpFAyjc0mpUx7xfEk3Sj5JrOAD6ScubRKdLh5KAsyL5wm5BlwfuZOo7vSXCsTLMX4kEp6p4Z9zvBHgEJdjTrIFzwuk72ZtAanF00yfjcV6dQA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/OOWAqvzSAgNbw8Zy6rvUF67OtTPhVrhl67Hs6AuatlO-tIzwEqab0sFrtAFJOHEE7T4D5ccw0V6PSlfLr0AzOcfk9Gl01sHF95vnhmebfhgK9MedxAi2UxTcK5XB9LQNenjo59bvNrZ7GY47zIF0u9EWCEFfsre_gY3DaSo-mKqlLc-NGo2zpiqag500BwzDhwZ8Fd63Yg-_cUcGy1t2XnyH1Yy2KH4Pjpet0K4W0omaZaNAuXKsbtDyYwqW2T6lqTsSTeFxjqkQq-hZbwKc5GdlsffNF9Eg2ChIXy89v-oEBiNmH48fTBdcVrlLvhgnyc2fLR1qXkn56u0wSqNXbg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🟡
خبرنگارباشگاه‌الوصل:ازپیوستن‌مهدی طارمی به الوصل خوشحالم. او میتونه به خط حمله تیممون در این فصل کمک کنه. بزودی با او مصاحبه میکنم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.6K · <a href="https://t.me/persiana_Soccer/28622" target="_blank">📅 15:52 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28620">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AIcp9klOCRgKQ1ajAJl23bQuFe6dnvm5-NEbc4RzFcL2B0u4s6Aw2-5JdRMlt74P8Ajd73MMeGeg0_MmFsW3j2hn9t3lMH7f1UpBGnKWN2ZkwfWZSn5BuV_iRDQdR2t0edPCP6APv5RX3fGZam2qxITjHrQdEqDBYIgDH963VJ2-2oPbRoh6S-zRV7H4hlCQataYrei_yO9_zonQWpxM_jh9LC1YgVIiOUWvb0vEoAYowns8ZMkH88Tck8dm4yLt6ozJ5iEpe8-1gVHsU_Q1lFEwDdpTPV74uhuiSekcfcJWzT-RTJZu3kokZyqlsp5yWM3E6fnYf4e33haxLKpOhw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
عملکرد خیره کننده کیلیان امباپه، وینیسیوس جونیور و جود بلینگهام درکل دوران حرفه ایشون!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.6K · <a href="https://t.me/persiana_Soccer/28620" target="_blank">📅 15:07 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28619">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ObNOp8QjjtQF8vsobeo3zunoqnwQn4QsLZiJalVb29xkrwAqTeG1sYmHzw6ZDi4z51IkQ5BU4emMcqZyEPkaD3y_5RquTNedoSdilj5gMM4CZDHSHX9e1gWVD42y0ZLlfd5_Cg_Noivthzz2xGwir48zmfYI45uFdbMHGWEiVRHm5I1PoxkP9iK0Dakc8j_eDeyNh6ffipYP98hQ_3oc84Z9yxJZEnQ8A4wdh4g1qMdsDeFZl_1XvPvDzJ83demh1t1z9HAr07KIbiOX_blZKsagqJoJZvbWwFScIUrzZ96b-PhnynTpyEZANqW5dOo0M2Rd7mv4HVTH4CS8CqLUhQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
کامبک دیوانه‌وار تیم ساپینتو در مقدماتی لیگ اروپا؛ پافوس باهدایت‌ریکاردو ساپینتو شکست 2-0 دیدار رفت مقابل هایدوک اشپلیت را جبران کرد و با پیروزی 4-0 در مسابقه برگشت، به دور سوم مرحله مقدماتی رقابت‌های فصل‌آتی لیگ‌اروپا صعود کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.9K · <a href="https://t.me/persiana_Soccer/28619" target="_blank">📅 14:44 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28618">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/imGUMMlbN6nv76_yHnkVUDNMNUrAC46PkgaaTlAes_LpPPzy5JqYoOKTcZHTpTyX_GTETa3bW1_onueRfznJ7d6QtQjoaZHRGZJju-3xCy36gy0pjZfrz8djego265_8cFZn6pVK57hnlhDvEzveW7CIcnhPM8K5iiB-x_OcoCSlkieJiZnSqiqItY6b5AnodsfpQu2ZTXrDTz3ifO_KxGEMZQPN_Rfj7ojiugdbODKN6d9kPnv0COWUFb18sqzGo1MnF0y1uXBNqdXf1jgx-_Ehyqb-M24L6A-XmdSpvRfj0f8icaVpmh4VWummDdgnKvNG09u3tYDqRo5dwxIFLg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🔴
کادرپزشکی‌باشگاه پرسپولیس و استقلال در تلاش هستند که ابوالفضل جلالی و مهران احمدی به مسابقه شهرآوردپایتخت برسونند. 48 ساعت قبل از بازی مشخص خواهد شد به‌بازی‌رسیده‌اند یا که خیر.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.3K · <a href="https://t.me/persiana_Soccer/28618" target="_blank">📅 14:18 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28617">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Uc0WV8v-7L-oyY5EilsaTUKmCoh5CP-ymBkJu_FfMaDf6EJpBDZxJ0DttB5p-kub4fCilPNGo0MvM-iak-fQ3aYrTwG3hcfVmLiAlsrOoeMIm8oKtzhj1EpYs8VTvygGcclFjIPVWbheAoM6HzZ8-j6oOg0x4LQvFC-t5X2PNV7T2VpaJnJNcqbZLeVHDbeU5-SNNZqirLH04Rzz975XF_Rl27TwN7xPUJQCwq9xQLZSNxogx3W0c10vJbvE-0i5qpt7hVxUfI-iCBtFRTwUSJkS5ZxZuEKF_QGcpJxqPyDKbiK03FLn8ueEF3jTCtvmXe2hk7cpx-KaetoQ6wTyJA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
انتشار تیزر رسمی سریال کمدی «مرد سه‌ هزار چهره»؛ آغاز پخش از جمعه ۱۳ شهریور از شبکه سه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.7K · <a href="https://t.me/persiana_Soccer/28617" target="_blank">📅 13:59 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28616">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jFt7StSDpAmvYqQM-XZI6rFZu0b1f9Eg-F0zwX8n6F9zBvd0rGI5sQ39CNasX5-yq6eTRxofC2ZpCoa5ArF_rIK5Xdl3VEHBQk4KQHFFmed8bbH-dxk2bZa1-Hl0LwyE4x_qSLJLQspktXNoc9gq3kv_c5wxYf7qdJXwZ1-qNsXv8VUpMjiEL6Q_mviGjh_xddRPmKuKvpoVNtrVfOA7EBsRvjvCxbJnvOLnTJidMiEj3vFVwKHIFtW3JikQlBnjRvB5STCiW1eq5gKsxgbuAX8RuU7uzk-scmitePrIp-Of3y4yeWNwO3rPIPQtcctzip2tqy2-h7FEVjIVeG-CEw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
واکنش خولیان‌آلوارز به بیانیه اتلتیکو: حتی اگه بدون‌تیم هم بمونم در تمرینات اتلتیکو شرکت نمیکنم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.6K · <a href="https://t.me/persiana_Soccer/28616" target="_blank">📅 13:23 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28615">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dsyAsd-LXW4yic8kBWKk_-OxbQEAoFsnnzW26ofq4Z_yBR2cqXo2S6c64IcJKPPY4HiW7zYw9o9ceJeZV3qneJS95sDvvsd6TeljsazJVI4NWHYJgQLXK0_WupB59YIxtopQTplkZUtIkb6zld3-x4l_GS_WS6YYmQVqJ1gRsITa0Csfy0fBKPzIlXdz80LlYMnrfu1okeSVeC8DuhwayMRyiuWiY_Ue9eZ06iBxuk7XwYHvwfJJHkLOcJ99xc7ueeKxRkNntgHJm33ussxKPWN4FU5VCdkXVE1-JWdgcOKlmhg4ab58zXfPPXMZO4m07KBhqUydmAj1elniDGQNVQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
باشگاه‌تراکتوربدرخواست نکونام با عزیز گانیف هافبک دفاعی ملی پوش سابق البطائح امارات وارد مذاکره شده تا درصورت توافق نهایی با او قرار داد امضا کرد‌. گانیف در حال حاضر بازیکن آزاد بشمار می‌اید و مشکلی برای پیوستن به تراکتور ندارد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.9K · <a href="https://t.me/persiana_Soccer/28615" target="_blank">📅 12:41 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28614">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EphsBTT1EHlkhccU1etIT_Lnu88hmNXFlvJ7C4zYn-aUC9ncSVx-7Hrv5Yi0iBb_QIS8EsGdy8PR1bv0mLvI1VUrRUieaIl7ThaGIQ5_7elJ6spiHngnoI9hOJUVLkowc7bbHxz5HE4c5pX1ZmevwKASJQpsp6AykPzgSUlbb5BFb4t9nZJJBmMo9b1Ipo396xnVV_wkCqPCR7T8yH2nYK6h7eSkLzALfsXMTIq4WK65aqcncLbVVJDkTLb1QYP0EdZW2B0QTF08jHUfxLssRe2BV-fQDHuJgGPdmILyjxjR1hgTFuhOg05UCrudeaXS1IopY9dAEspstGNC7kO9bQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
بااعلام‌پیمان‌حدادی‌مدیرعامل پرسپولیس؛ پرونده نقل و انتقالات سرخپوشان در این پنجره بسته شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.6K · <a href="https://t.me/persiana_Soccer/28614" target="_blank">📅 12:25 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28613">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Gy-4EY3jP9kotbvJIDCTKtaBmHpH4IsY1rpdWIyaQQTRaxwwos94sP65h2tVhi4GXCYuV6yVq9mfDrrqE3x80IXAhBKRBHm_xXeCNt7dNrUWvuwX5bY0TjWfgaeAzb4M_VUr6pfBfO1yAU4HPAiqhvuE68ONmNkin_bsu4b_kn9d6oksntxuuILz23l6UCI13mRYWkXo577uEkgkkh62eSeu11TS7ZcHuc7J3yuEuwzEkOjpabOIxIJ-FZ-CyhK1GOAHGVraxsFmxwEFBjeS1eY9z2L3r4rHL98gshLb1-jup7kpqYFY5QWtF8PeMkqNfM6fNVTKb8mOxoMCSZroAQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📱
استوری دردناک محمد فرهنگ یکی از عکاسان زحمت‌کش فوتبال‌ایران: دلار شده 204 هزار تومان! الان من‌چطوری اعتراض‌کنم که بهم انگ وطن فروش نزنن و از کار هم بیکارم نکنن. خداوکیلی دیگه خسته شدیم از بس دویدیم و تهش هم هیچی نشد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.5K · <a href="https://t.me/persiana_Soccer/28613" target="_blank">📅 11:46 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28612">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vkaqGXWxPeW0vY_io69Jv5I6ehyUZbYmDc09kTZRNy8xD8T5oZWhs30U4bOwHaDvfOV5klfLJtbqofGDE-fdqt8rAcNHYNEuySd41GmZXRmbti0nUovU1n4C3tmbHZW_Hi02JwizvoIsMwzRXBPp73ChUZn-0Egb9lhXKWGcDpXpvu8Bip-wXVutp9Uf8fHGSfJhfCo_VflMKGQwAaEWiCAPAb0_8_KF_-Om1qOYVkJItG5qFILFgCqTt7uBEuFrxlpapOZHfxOw9HbRF-4eby2CTm2nuDwKOzJZ8yTppG3TL9RoFdjPdEwulnjpVcmcS_e9MeA7CaYD5Wg4R9dkyA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
👤
#اختصاصی‌پرشیانا #تکمیلی؛باتوجه به‌ سوالات‌زیادی‌که پرسیدین؛ بعداز پیگیری‌های دقیق از مدیربرنامه یاسر آسانی بااطمینان‌ کامل اعلام میکنیم که‌فسخ‌ قرارداد یاسر آسانی درسامانه فیفا ثبت نشده و تنها یک نوتیس برای باشگاه‌استقلال فرستاده بود و هیچ‌مشکلی برای همراهی…</div>
<div class="tg-footer">👁️ 57.5K · <a href="https://t.me/persiana_Soccer/28612" target="_blank">📅 11:20 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28611">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VPwacYorwErf0HZ9MNA57yMfUdjML-hhcVkqgmLhitIPHzXr0HqovPYlUlnt3z7KGJmJyZFLObQ7vlLmmbez7WmK5bnSCGVsVRYHbWjZ0xOZvrj5TA3dyC5kLQvCLdCHFkv1k8zIDLWRmRl3Njfy_aX-Acc7HJhFhFlm9GunuRdQE9Ch1hfguFLjMfnBzHS6DYWbyUZAbuJ-s5o_slPULgik0IyiGQ-Wb26dzqItUSmrbhljelej4Pyg2QtQ-Ka2AqZi2rCJiolsD6fnOASGUa415Wk3lw58haHirrMnXQtOk9dFaJDB0bdVHBNdQZg4KPOXyJCEUteHFZalavar8Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
وزیر ارتباطات: پرونده فیلترینگ باید در کشور بسته شود. بزودی‌بادستور رئیس جمهوری فیلترینگ فضای‌مجازی برداشته خواهدشد و تموم پلتفرم‌های فضای مجازی بدون فیلتر در دسترس خواهند بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.9K · <a href="https://t.me/persiana_Soccer/28611" target="_blank">📅 10:51 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28610">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UleeeumL2NYpGVdqJgFwxthVu6JNKw51Bp0nAnXG1HinZXyHhIGuxXzpIYNfe0XO7CRodnm0TJzlmgZ0vx_L-HheH4y0GTgtFKA976xqI9hX5kGqDTQ25fi_kCO5tdbJdPBC6V5a4ta-AQC6HifWJ_Nt7jSw0atum2g-AP5qED2Ekni4eE0yFQgLNek1FypO-hGCuuFYmkQ7xAgxCOzpP6a-abSJuPjZzVt-TsdzQhcd_CRc2A9yYUTXbNvpjPQtRcFwzQ8jcOQ5U-G8L1MwqLQB5f9DYCOwNUsrzky5rkn6tn7IeUP5pKfE4kacYG_BDU-Z5Rs2TVd3T9h6H6UNaA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
🇩🇪
‌اسپورت‌ امارات: باشگاه الوصل بعداز جذب مهدی طارمی و ریاض محرز در آستانه عقد قراردادی دوساله با مارکو رویس ستاره 37 ساله سابق‌ بورسیا دورتموند قرارگرفته و پیشنهادی دوساله به‌ارزش 10 میلیون یور به اسطوره دورتموندی ها داده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.8K · <a href="https://t.me/persiana_Soccer/28610" target="_blank">📅 10:51 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28609">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hdYOPgHxfFIscUwoQv88nZKKHoGR_8mLctRH5MsVVfn7FIBSTN18iBCmPO2XIv9l95MJ9rzlawD5vRFObjPHl0BQCPO9Hd7TqYial_a3yKgLrQAsFR0Bmj-O-2fCAe1aZTf2WZPzICsojPRhrcjCMu-cZPqs7HtDgp57Fmmz6Bf_zfB0BA4lk7tWDL57M5eqf4bItSLh4mvK0WJIdZ5aIjl26VSzyIF9PL8ssUE0hDrw9AEOkbvJ6TTU-nzZdqD6narwwflhuUVsRaSUXtGJ1s_sWZ5mEs8qz-n8wPtBtQNq6dKcHlgWXvLnx79jB17KnLC0xHkgylf4llmLgjfhPg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 54.6K · <a href="https://t.me/persiana_Soccer/28609" target="_blank">📅 10:51 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28608">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TvSf4gKi_eoraBFgre29KjR-VcIChXYKZ8-YTHJBYqQSbtBUvJATDu09pGZSmZU2k35oRJA_68BjBlfOD-McCHvW51Pkc2S-Uxa8-izWouYLUdkMn09lrnH8j2ajmQ1HdBl1a1lUn4DwBMZN4NbfW7YQZ3vT11nQ85xR9NK2dCDqxfgyWFjuaD8U7fVfdxFwtzsVAkl1eNv7Bgka36JKXV6hoOKl_Ek7ijZXxL9uO2CpS-ldoclQn4oA_y9vx6Gp-BVs7OdSWRsy2JelVee7rjjrYqxJi4mL8_UdxxW1nmMdOW0J2fRuXP1mr9Y1PL1ssfBCbBAgIx6RRySGvdBpzA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛ با اعلام باشگاه تاتنهام؛ عمر مرموش ستاره مصری منچسترسیتی با عقد قراردادی قرضی تا پایان فصل همراه با بند خرید دائمی به ارزش 50 میلیون‌یورو به‌این تیم پیوست و شاگرد دزربی شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.6K · <a href="https://t.me/persiana_Soccer/28608" target="_blank">📅 10:09 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28607">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pEmPxiHRVJeQgWSGNUfculGwP947fhrzPH6Hm3t2ETaqrBf3Y7bOSNz6dXA6WKe0rw-GWfUx5ETAypPAgVuZ6q197-D38ka5uc_NJhsfhvzy4GUD3pwth_HHcyXRfhE8wvJbPLPY7BjqbWtaFYb_v8h0S5mgjXv-R_BDYt5jN4c7FbUeiP6H5okjAjwFeonB3NCm0zNSLKfxAft4LYKUjyd2AU_E1_lCE8DOMwHB5_AAq3OWRE77lGdMLWbvQ3b3Eh8kVVkwLmm0lSIhpQNaA4S4AXohI_xu7EO6ZuxBNQAtyUgX7iLzzSffTJp8un9znr3VS_1fVfmqZOmy3R09ug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
واکنش خولیان‌آلوارز به بیانیه اتلتیکو: حتی اگه بدون‌تیم هم بمونم در تمرینات اتلتیکو شرکت نمیکنم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.8K · <a href="https://t.me/persiana_Soccer/28607" target="_blank">📅 09:52 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28606">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Dbu91yUyU0jImVR95R_LKqxKES27zIoi8jQTtYIH8-G1QW2JpwIlMk3y693bkBoBD8HEN_znXab7vBl1T5cD0TBmB9kGBFL9xyh_GW8_xRq9g-fRkaDJLYD-8GJctWIoEvSYRO3S090Vf7zLvnZ20UjmAiKwNHn6eifbE7Ye7szFtDM7choI6DSFIU5wpTkY3Wie9BZDepqfNyum3KKNvhOFv_iaGixQq95fe53e_z6CDyxReRVA6gIDVN-mXkUF-rLcOKnN4P6QawPlZbu-Pv9oqLb40Tk2FdMJm3vKUXNzWvddw21oUirAgJ9nM6bY3zVAA8OEI-RAmjQxg5fBhw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
دیشب گندوزی بازیکنی که قبلا مارسی بود در جریان بازی‌فنرباغچه و لیون‌حسابی رومخ هوادارای لیون رفت از زمان گرم کردن که فاک نشون میداد تا بعدازسوت‌پایان که اونجوری خوشحالی کرد و دیگه کار به دو سه پارت دعوای سفت و سخت رسید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54K · <a href="https://t.me/persiana_Soccer/28606" target="_blank">📅 09:30 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28604">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EljbNeLD04ElpE4LmwFdmEfCnd7KkK8exAaCLCEBSmKKbWSLLcIVLsy04KiBWWCVd3TCYeQJ0f8JcUWUJFTNsl2kgUHGEt14O38wzuE2BzpxKk0xi9qBXpNq5gBC8FGjWcmRetAv7rWH4jUQJmkw1wLicNZRO3Q1fpOSOLYoD8W7VMSVEvBoCERxIli7Z0kBjH8F3YGMOpTpfGEMI5xVN8BZVZ2lY7B030K6qFqDvZDSkV0QYiHe5XS58n8-H7Adv10QNArFWBKZhU6AhFR3OTTNJ2b_oQ6D4HqrKN-FP3iGLbmI5L1NV9_SQxsIeK7kD56EHw6dOm5nQpR8SJB6ng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه کامل مرحله گروهی لیگ قهرمانان اروپا در یک نگاه؛ چه بازی‌های جذابی قراره ببینیم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.7K · <a href="https://t.me/persiana_Soccer/28604" target="_blank">📅 09:17 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28603">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b440142175.mp4?token=PnnxD6MR7XlEzFbkbRLpO7ct3uXL-6AcOp65PKWOgQGCBDFm6_--kt8CPg7T_UwPrlGpEAnivkBijXBHc9zTGtHKoNPuPUduNj_B_xbyxE3C4KiN6f-AtT28_XyXaxCL0T99FCKY7TXOD-RhLkJaZkUf_m4zp_VR_2phL3wzWLET18Wtsq45fQlp3NPW7jreuNFnTpdppFQdyZ-ZTYZrZCJaiYfbXEHcXy3xJPsNP8474lkS5IejESolfiispAC1ZQLQQsLnhORMBAVkaxVFdhX18Tq1KGcS2U-wXUpxUDvDn6pC9hqRkejSwDrwMMoeiPLKMlznA8bFZkOXRc0HOw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b440142175.mp4?token=PnnxD6MR7XlEzFbkbRLpO7ct3uXL-6AcOp65PKWOgQGCBDFm6_--kt8CPg7T_UwPrlGpEAnivkBijXBHc9zTGtHKoNPuPUduNj_B_xbyxE3C4KiN6f-AtT28_XyXaxCL0T99FCKY7TXOD-RhLkJaZkUf_m4zp_VR_2phL3wzWLET18Wtsq45fQlp3NPW7jreuNFnTpdppFQdyZ-ZTYZrZCJaiYfbXEHcXy3xJPsNP8474lkS5IejESolfiispAC1ZQLQQsLnhORMBAVkaxVFdhX18Tq1KGcS2U-wXUpxUDvDn6pC9hqRkejSwDrwMMoeiPLKMlznA8bFZkOXRc0HOw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
پیش‌بینی جالب دیدارهای هفته‌چهارم رقابت‌های لیگ برتر؛ سیوش‌کنیدببینیم چندتاش درست در میاد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.5K · <a href="https://t.me/persiana_Soccer/28603" target="_blank">📅 09:01 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28602">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">🗓
🔴
🔴
#تقویم
؛
15 سال پیش درچنین روزی؛
شاگردان سر الکس فرگوسن در اولترافورد با نتیجه‌ تحقیر آمیز 8 بر 2 تیم آرسنال رو شکست‌ دادند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.7K · <a href="https://t.me/persiana_Soccer/28602" target="_blank">📅 08:24 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28601">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DFsfUsbBFOFRDqEPITtw0o0CPdVfr5YdUynV38Nq181w3nNoTmfj6x18LP5WLyxZv2LKPvh27wiv72CdZNRUSFGuub95A8Ake4d_SwsoFmxziICN12xoAZJYdVMuf9ytTyD15Z7zhFD94z1AUC9bOdOXCGSxOGjqES9r6tDlPHVCbcsHWJtJO_4DFp4t-uft6ZkfxX4ExVx2WVZsadcHGt2W1sNr-lW0iCo1cKe41y4hSnbKIXd6ypDxVv36XKYwBC3ukZ1iBwyRmMDy5MURyTXLzqWlKSFFBrzgKlx4qTFI6YiXTJ7SCdRcFSh2-k0BLsYqfHjLt5VEYnjNWYhM4w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌‌دیدارها‌ی‌‌‌امروز؛
جدال شاگردان سهراب با فولادی‌ها در هفته چهارم و دیدار افتتاحیه فصل جدید بوندسلیگا
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.3K · <a href="https://t.me/persiana_Soccer/28601" target="_blank">📅 01:50 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28600">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Nd86GrAJ8Z-ALkmk2HSVgI7_lk71s4XvWUM7EGnoEHtPyjNcA2wBU9XQv9Fcc9Mu0GIwqevcQcLz6gSproT3bIfuMxsRbDwc9qQK52C7AOs8MISHU-UMFMozKAKjLw20imPkCyHTLPUQbIDxLGi9BcGfgN2Mf5DZuY3kxRDyjIQ3EXp4gL0-R1X7dEvw9G2vYMiOBjHQ1pGxOWooHtJ0g353CtOHL1wQ7v-0rHs4Hi6Y8txruAdyDMxuLInKVj_1wfDWm44NNkZJQnJRoVS7Ahg_JXdQdyWbYrITEAwjYymhYbIivtez5TfiLDfwBWdpAStLaMn9Fopm7YRri2_Lkw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج‌‌ دیدارهای‌‌ دیروز؛
برد آبی‌اناری‌ها در اولین تجربه حضور رودری و صعود چلسی با گلزنی ولبک.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.3K · <a href="https://t.me/persiana_Soccer/28600" target="_blank">📅 01:48 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28599">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iNVy3ySlUSDVN0Z4otWabRpWUXJ-WFoaOEcfCVh2IRe6-24T7vvV82NEpJkDQ0i_yBgaBn1C5fWuAWAmg1flcFTJDqRBZwe4BL--ewQGGywTiZ-90ngwrOT7pdcx7rUNbrs8-u45yZmzUU3016WkoE817eTsm_rxhztybhZKifbZ_AimhYn34ugLoBkNXqGz8LYv6kpUQrULGBTJZUYLNV_c8KJbtx1stMTE1iHPPGrs87fC9PV0dAlQTmMzr1Wdi2kyqWbiM4JMy-G9XRSjCtfSAlgxPZ31iQzelpITPD7tNshaOcbQCfqdZnefobfFxaiJSt6-74LRoGYu7F-Gwg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
هفته‌دوم‌لالیگا|شماتیک‌ترکیب‌بارسلونابرای دیدار حساس امشب مقابل اتلتیک بیلبائو؛ ساعت 22:30
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.8K · <a href="https://t.me/persiana_Soccer/28599" target="_blank">📅 00:42 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28598">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lT0yZ1Nl0OYIbnRQQGmUh6cA-bIGHAothRCr05EodBVVwvbZLJhB6JzpK_15dHerpuDCxqPTNBKQAbxctSMnOIF2vb-ydYanLZOFOq_eU1feCrjVH5fqjm-qQcI_T8euiNuEiX0G94b0QHEmgKdn9UqllB1sT1VJM3bdTjl0QYB8ogATNlHIJm7jnpr4vfrKIx_wyb0n-bcFUBspUQikChh_MNyi0ZfOCZow8p8XmHuMQDKMElnYA_TkYNgSRMH85f8tb-xLGUiTWP0C1ib0BU_WbVjOk-cLgiwuRhDqMYE64cHNrnn8v7ITejtaFsZp4WIa6LiuWiApoGzrC-4mMw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
بیشترین گل زده و پاس گل از سال 2020 تا کنون؛
کیلیان‌امباپه‌وکوین‌دیبروینه در صدر جدول.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.2K · <a href="https://t.me/persiana_Soccer/28598" target="_blank">📅 00:31 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28597">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d099f34763.mp4?token=N9cQK7Sv_zITxiQTwXAuNcCYa7gR_y3gb-sFbTsRaQOIpkROybcusjWyUtPp99d-penChShUBZOXPZdTnk18u-qBCK1V1dCKqKW1MzWfPlhLwN3KV6kkHodVjO3CxMdQ197KxH2SnOyFk8b2VOZEefT6uZbHj2vV9CTHyfmYgKttNM72Z67PUnE17fhlE_S6ms1S1CWCI5pZ4mlpQHXC90WeJdfvKPrLFwHSuIUc37aFWSTZ8PVS1u14A5faK9hncDp_lgdkiI-sF8Qoh_nEAr2u5a32-OVg_rVZ3Tv9ButGXg30AUTcvQzezJjoKG4wgV7q_igPNEiR12t0grj4SQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d099f34763.mp4?token=N9cQK7Sv_zITxiQTwXAuNcCYa7gR_y3gb-sFbTsRaQOIpkROybcusjWyUtPp99d-penChShUBZOXPZdTnk18u-qBCK1V1dCKqKW1MzWfPlhLwN3KV6kkHodVjO3CxMdQ197KxH2SnOyFk8b2VOZEefT6uZbHj2vV9CTHyfmYgKttNM72Z67PUnE17fhlE_S6ms1S1CWCI5pZ4mlpQHXC90WeJdfvKPrLFwHSuIUc37aFWSTZ8PVS1u14A5faK9hncDp_lgdkiI-sF8Qoh_nEAr2u5a32-OVg_rVZ3Tv9ButGXg30AUTcvQzezJjoKG4wgV7q_igPNEiR12t0grj4SQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
انتشار تیزر رسمی سریال کمدی «مرد سه‌ هزار چهره»؛
آغاز پخش از جمعه ۱۳ شهریور از شبکه سه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.5K · <a href="https://t.me/persiana_Soccer/28597" target="_blank">📅 00:15 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28596">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Eu37aEFWmbH9JMZZnV7AxKe9Hevs6RnDdwFeziT-qa0NdLbGxj34gg6aUqzNSImt4MaYlk7P63ZXmjMcj052pB2xPKBQtai5QyRGxDNauwR8umjtpyCUNRny_lolEJPq1v8Gz8_ukydtlx7cXWMeFJMc2U4N6DS9brK6wFYpc04thrMjM2ISdgZFmvPI7INcz8JVnHgmy3F9-gNAceo2b5KisJtZqQmKOFy0zsGJTYSFxZy2aIhKo_BQfiLih9RB_UhJVzrh9y6-nZWmahjRWUjTa1PdBeEaZ1Fs7bccf0bJV4gpEKfKypfA9S4rfDhDPlc7bxXlxnbp8BJ7sF5oww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
ترکیب احتمالی استقلال برای دیدار فردا مقابل فولاد خوزستان در هفته چهارم رقابت‌های لیگ برتر.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.2K · <a href="https://t.me/persiana_Soccer/28596" target="_blank">📅 23:40 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28595">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kGHNePx2hGt8Nnbo_t81m4or_ut8T_bpOYAiJzPS004tPJWko_2epwIXFApdE_ZWCheKm3ALJyyjHQJwzJ6m0amwqFz-JcalMaGc6MLCJtfxnSuDZEnu1OO8SSyhqqpVV4RKmwRcG6w1UyAOnH9OJ9Hdam-dt-Mw7jxRPpgqM7VtJLMwkOWtATZqfbj07VFJY-pB6IE8aZTcq7t2vKFtNAt1xcsUYsf0hh7UvoLZcBDs6v0efMQ6fr7twvXxvIewKdd8N308PaNOmEb5hnWPC_xVY1PRuUFmCoAj84F_GH_VqLU1C-so8Ernh-LTCXC3f5986Ws7VOdBH_Wc1RO1nQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
گرانقیمت ترین بازیکنان آزاد ایرانی در ترانسفر مارکت که تا به این لحظه به تیمی قرارداد نبسته‌اند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.3K · <a href="https://t.me/persiana_Soccer/28595" target="_blank">📅 23:27 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28594">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ei_dfDtWFTQoG1BzI5rqsTJSZx0tIc6ODIx4flhXchh3L2ckN4UYUD6-Wzod5DHo-TmLJ6ap19E6b1_6a0fzaQD68AtX_SDW0XHQTYtC-k3Y6JXL4bEC7pneR9JT51AB24T-Rr0sqN6YqAbPoELa1trZ9YJYJ9gHZQBttFXPABiqJsEejlC9YLRQ6mdfTtLfw02zdu_7WrQHYKgZCZtSAEhaJSPs-Z4-hbft0A9kdKIkeM6jpGf-ncUEB-T02KfuiHKyujNRnxa4B0yoIfoc5VOt83FJiiVhaKHQqDKj8Rfph7KhBlakQioNVrUdacJdO6uZU8tPM7OpE9kgeHe9fg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
⚽️
🤩
بیانیه‌جدیدباشگاه اتلتیکومادرید: تحت هیچ‌شرایطی خولیان الوارز رو به بارسا نخواهیم داد. تنها تیمی‌که‌موافق‌هستیم آلوارز رو بفروشیم آرسناله و هیچ گونه مشکلی هم با این انتقال نداریم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.2K · <a href="https://t.me/persiana_Soccer/28594" target="_blank">📅 22:46 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28593">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WNfBcNgi8ot16dHHc9rNcp58ZZCYN8TmrqesQ00i9AFLEYmpL-tjQrcpr9gyHV9IRbRen2TEvBD7IfoczfW7eYQC3sCEpF2NQGEeW_1EtJlpY3xxQ5gux2Cy65M_uSQQxD67A6wSZzjc2K5unRc7hjEHU4xfeOTalk3qWfGRXwrlYmBlymBKFjAnWkqKEly9dOF_OogC-_Q6GR9nrfFYts2y7I4TvGweaw0yORV4cYG_ooGLQuGhAxaEN3eB5EitRSlmACbD8cT0B73zDRT6IGrNOCVkfmE51qMxfz4JUiYSFv8uNHJ-d98qD6-o7L_lMW_HkHETmyb3R8WRckJCog.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
بعدازجذب دنی ولبک؛ چلسی ساعتی قبل جردن هندرسون کاپیتان36ساله‌سابق لیورپول رو به خدمت گرفت. حالاجالبه‌بدونیدکه هدف ژابی آلونسو از خرید ولبک و هندرسون‌بحث‌فنی نیست فقط‌وفقط میخواد تجربه تیمش رو بالا ببره چیزی که توی تیم خیلی کم وجود داره و رختکن تیمش یه رهبر…</div>
<div class="tg-footer">👁️ 58.5K · <a href="https://t.me/persiana_Soccer/28593" target="_blank">📅 21:42 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28592">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AaK7XJc9B37CFj8iYfV8SgxdmPQIVGjlIkIT328-IKZUkXvyV3XL_5zOI69p9WoJxS1B8ULGiCpZgh23i_84aRwpIpap1uDCFC696DNYq2m1--0khwWVdyu4NvzJg9h4Js7KIPPqwawgyR_EhHmKGHCqyWWphvBSUPz0p43czzNj37IurdTWr4QzOnNKnVNp4cOB9s1JjHS3oYNm1g6UJ0y9baD_5OdMOqdm1JldTVWPSLarJZwxMxX9eZt5RaDJnOJxgAMlrTC6LZZsAJJkn744VAh_S8lYYQUsRa2syRU7FUUqJN940RziVoT3NGin2qaWYGCwqEDKLIP5zkNH4g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
مهدی تارتار به مدیریت‌تیم پرسپولیس گفته اگه پیشنهادی با رقم بالا برای فروش اورونوف به باشگاه ارسال‌شدمیتونن اورونوف رو بفروشند. حقیقت اینه تارتار اورونوف رو نمیخواد و میخواد فراریش بده.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 57.4K · <a href="https://t.me/persiana_Soccer/28592" target="_blank">📅 21:30 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28591">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QAO_g1mQqlNWUuuev_2CzY_1oSoZjhXt0bzcPwmhWun0eRelVHHgR6QMTxBcfM35Nk0pWqhkB_HOmWpxRhl-BsGkFCdT35IPukG9rYXxUCNfYYxHug-B7CrYNtb2KlYyJnlaBngX6pf9Xd2GRfkzQejWTod5LaT-kodN-KEX8bKdbbQrL-GcYR4gJjRKUn877XlEc52Ut3BWjnu-4fyPvn91oX7haDBTZa4FevEPLf-mJVG0VgtdqYEIiXz0g7QaHCKRcbJ2N5_gPQ-wCwacamzrro9mP5CrWop2M08m4sj9HCg1lrwLnCjyzJX99-AiDpmUI5VK5_e0dCwBhEYdBA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
هفته‌دوم‌لالیگا
|شماتیک‌ترکیب‌بارسلونابرای دیدار حساس امشب مقابل اتلتیک بیلبائو؛ ساعت 22:30
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.9K · <a href="https://t.me/persiana_Soccer/28591" target="_blank">📅 21:17 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28590">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FL5NnMcGEtl4wyRxerskxU-T_tqMpRqxkC4aKFsKHkOerr6ClUYlDEgXNa3D-f6FkD1oxbKeeSLxu6CBpS9n5tCiPmTqza9I-SEcoCTdkEPq4Qz-o79uY2jlK9gNGM8LjOvsm3JlN7iYwCQ-r8uQaGWhjefqiE793-VmW4rIPO4E8NMMNSfYh34rHosl8Tqi_yHpmGJGJURpiE5QO1DlMNlzK_2E6kO5yi48n4BZOX7zqDxmkjeDrGsEyZxBwWCyGHJfk43LEz_Jfub527vsakv5513wOAhBVlgcANUG5rL2Rb7t4O4aBwPj3ifmBIfq9eLZnFEChLV9JNQ_ytq7WQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
⚪️
آرسنال و رئال مادرید درمرحله گروهی لیگ قهرمانان اروپا بهم‌خوردند؛ آرسنال‌تنها تیمیه که رئال مادرید درتاریخUCLاون رو نبرده است. برنامه کامل بازی هارو در پایان مراسم قرعه کشی میزاریم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.6K · <a href="https://t.me/persiana_Soccer/28590" target="_blank">📅 21:09 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28589">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/016588e26c.mp4?token=R28b19Ks7nKkrlKv5ICr1n_inxWRarGZaO43sZCdgPrnrWCMlRnZTcUfbAOTeBEv_4KDPsCpVQ1VbgrsRGxT3tPRl3CFUrnzaCBFAHtq1tRcChd4ij9_KshomFMrafTHHZuC1GsEWkPpq_-9KxzduPPShs-CWNZ56vL_Rj98FtYpUHAu_ySLxrfRyIAaTdckuXhih5oQAtK2QMl46zcLZxae7Pc-ac3fuVeElyDRWZnDDjFkPZZ8E1vzBdbUmAYqFoLidley2uyTroh5vsh6e_Zh2MXAAcry7J5QEjZX6-7IpJI-CDEmBzA2KEv3wtIzKW5a-NTHvDb6my0iYEsTEA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/016588e26c.mp4?token=R28b19Ks7nKkrlKv5ICr1n_inxWRarGZaO43sZCdgPrnrWCMlRnZTcUfbAOTeBEv_4KDPsCpVQ1VbgrsRGxT3tPRl3CFUrnzaCBFAHtq1tRcChd4ij9_KshomFMrafTHHZuC1GsEWkPpq_-9KxzduPPShs-CWNZ56vL_Rj98FtYpUHAu_ySLxrfRyIAaTdckuXhih5oQAtK2QMl46zcLZxae7Pc-ac3fuVeElyDRWZnDDjFkPZZ8E1vzBdbUmAYqFoLidley2uyTroh5vsh6e_Zh2MXAAcry7J5QEjZX6-7IpJI-CDEmBzA2KEv3wtIzKW5a-NTHvDb6my0iYEsTEA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
درد و دل‌های علیرضا منصوریان سرمربی الطلبه عراق باخبرنگان‌عراقی بعداز دیدار این هفته این تیم در لیگ‌ برتر عراق که با پیروزی تیمش همراه شد: 8 ماهه که هیچ دستمزدی از الطلبه دریافت نکرده‌ام.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.7K · <a href="https://t.me/persiana_Soccer/28589" target="_blank">📅 20:43 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28588">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rMj9R4_MOg0-82wVqwpqH2Il4lrnIZawMAeluncVizrCnw1guvEfrqc2FzQAtRWf8yJKpDvi3nwm1heMUhUJ-_5LipQ8sYUIB93vop5DP3mn39LkJO_u7Vj8ALJkypptkHowHFsIat1wPozFn3GvHF_owlwG6jzLbs1WI_csB0HUF8RuB9HDvvMgwkyBYugQhgn4hyb3YHxO5x5J9CwxQBctDL93W7iT60O3dA-GiwFpa4uu1vDutK7hLiOcmnZIGNjdHqFhVhqee375XWGJkdN9qBPAK1io5BvkCk552NlRRGtfNPb3oGyY3qUxsdkjdBuK51rdwC7xIiXVw-xZyw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
⚪️
آرسنال و رئال مادرید درمرحله گروهی لیگ قهرمانان اروپا بهم‌خوردند؛ آرسنال‌تنها تیمیه که رئال مادرید درتاریخUCLاون رو نبرده است. برنامه کامل بازی هارو در پایان مراسم قرعه کشی میزاریم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.1K · <a href="https://t.me/persiana_Soccer/28588" target="_blank">📅 20:11 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28587">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RhQlZtyD2hbogfLmhzZIFFGc11LFeJf07BIQ9Age0YQTPck-gLrniz2GGxaLbkprTAaNfdsqYWxjbaHPksZZsUIfzb-oU7wdK5yEl3Fn5SIqtU2vKSjRYf1tAPSbRnizXkMpMZf5_pg6MBegmFB_EBTNzZwqFXsbTXVWUtF0j8uCEzk1soWBdhTKfMsDe5As_B3UQ-J0zaPMwU_IaH-WqWEcwgc98iZNSfhA6aEWYO1iRCaAGIb5doP3x382scNMfYtE5_qcVEIfo9SSc0vlMiqaJL2g9HjDm_NNgSO0ce9RAG2b-n8dOmCfXI6VxVp1rWnLYwU6WXqXjbk5k34Dpg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
سید بندی فصل جدید UCL مشخص شد؛ قرعه کشی مرحله‌گروهی‌هم امشب ساعت 20:30 برگزار میشه و مسابقات از اواخر هفته آینده شروع میشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56K · <a href="https://t.me/persiana_Soccer/28587" target="_blank">📅 20:07 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28586">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/t17sT3rTB7ZIVog8hW4DIbxktp8912iaPxuNUJhzJAePwWeyRUnxsFH4aL502YJzS5Rr0VeqFbPCCzqRkvOTDDUyS19RtcdqTIVzMPtmMyLSgewH8GEn2mOg_fYun72cBiZXzuD852gEjuA6MIXyOD_SJxr5mQvlrGJQ2fpDubBIWCwMW8Dc1XgAqCqfsnyz2_KNo2Mgerwryh3yJ2twepgYWHoAfuXgYJdHtCpvVdT6vlRuZ42rB2sIDixkT3ItfsqvFcKx-DjAcLMUe43ddcq2xhxe4qPe5vtFP9RU8L5GImeT0m8ikzuwxxj66XvgPu5bjzpC3Ky0vqVOFs9PlQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
بااعلام‌پیمان‌حدادی‌مدیرعامل پرسپولیس؛ پرونده نقل و انتقالات سرخپوشان در این پنجره بسته شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.7K · <a href="https://t.me/persiana_Soccer/28586" target="_blank">📅 19:44 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28585">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vl7eS-vj5aEBJJ4882MyHxp-_5EWmBMQqaNw67x-OPcg7IgB1X3CLGlTkStbojlicxaRaA-Q3yiU0pLlqwY28FHwn2S0OWlLrZtqNeFhoaEgyK_64d2s9GlaJgzykDAqQ28ktGh-rVKdlWq8WgzQkQJsG6PeoWofcNJydkheL1437XoLjRSNsy0_qxuwzAx5tCbW7AdwHIIbnhALyKRz0ZCqVj1p0tWFMmGhllXLsIdv49kHtojnCdpmxv8T9JT5zbDOSM9tVAZ28WHx-p11VWwYI9yeyfla1b0GKgnlpDLg0_aGksD3XRHdNamok-scNMZEpFUM4uSZMiNqgaIGUA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
گرانقیمت ترین بازیکنان آزاد ایرانی در ترانسفر مارکت که تا به این لحظه به تیمی قرارداد نبسته‌اند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.2K · <a href="https://t.me/persiana_Soccer/28585" target="_blank">📅 19:41 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28584">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tRMd_6mOa_Ajf_sjSg2oQCZitFNzcOKeuVeSHzKkrfgx5TDWxOuYLzr_luEq4hVWjC1mPVRqfVlnEZjDRe4InZtq1y-0G6thSfX_nKLD-W1BVtdIlGcNyr-3gSluwxckexcZpXT9AxiI6j9m9hbKsFhfScbyUQP_X9_ngidxaG95VhyWU5qp4bXfOUak65vT5ZZicu7c-smpftG4MCybasCd8sVPGRsZnFCBk2wjc7X1OKDJTkBQutizbqP1DuPs4PQs3VJxrX0A3wMvXXVVq8_8D8MQpST-4YwCBm889V6bGuB_x8hpfyHcwsIMnXwvE7TjWTZdFSlB8pK7S229rQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
طبق شنیده‌های رسانه پرشیانا؛ علیرضا بیرانوند دروازه‌بان‌تراکتور رایزنی‌های‌خود را با نهادهای ذیربط برای تمدید معافیت‌تحصیلی او به مدت دو سال دیگر آغاز کرده و پالس مثبت هم نشون دادند و به احتمال زیاد بیرانوند شهریوربه‌سربازی‌نخواهدرفت. سهرابیان نیز به همین…</div>
<div class="tg-footer">👁️ 58.2K · <a href="https://t.me/persiana_Soccer/28584" target="_blank">📅 18:37 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28583">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DHRWmqz9skzJMyJbtHSpI6JJmAhGLmyd6SMNxbXreFwb52T-GsZnl4DsilwAj6b-qewipNROUAq6i7-lkEP3NwBTehb7wz1MyrG5cRn2dTnURZzOgAvNylHISe6KqApwHzAbGuADNpIq_LK0qNCns0xSPJv4Rj35LSl_5edZN7KZ9uLLaetqtS2gevjuRZc8UIY6eGMmmAOXy1LJqIvNl_N1t7PPTziOGms4r3CeMolFJrzI5tpcXOVnJp-tc0Em9Q5vT9G_Hvnq4wpHIF_yAgciZDolytiptf2MKstEQRK855PlorZfCNDQyPBF2w9yWVEUyyhfjbD5tmpIaoLqOg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚪️
🇪🇬
با اعلام رومانو؛ عمر مرموش ستاره مصری 27 ساله منچستر سیتی با عقد قرار دادی چهار ساله به‌تیم‌تاتنهام پیوست‌. این یازدهمین ستاره من سیتی بود که بعد از جدایی پپ از سیتی جدا شده‌اند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.2K · <a href="https://t.me/persiana_Soccer/28583" target="_blank">📅 17:41 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28582">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OCbH53YF6jm1z5j2lK7E12i3byiuL0O_SC-mJPKzOIxdIGgcyge0vZJMie3DsKTCs4tzwL4nzPjuOZC9SprJNff4iYwUoJBj_rabxPflKub3jz3HNRh41J8AiCNzwZF4MbVNxnG-Me5Wl9IbYDweFyHvqsd0jnTKa7okbXpCMiAJYoAGNwjsPUsWcAWkKBud5WPEw1ZB3rVssijmI5bWz7tHoPVFPPukk3QXRz50vd70JaKDYAP-0jLsf8yFR2_ks57G8aC_daeX-rfNzO6HJgrnhIaYSr1Qsbb83vS1iKHTWoASAE2NPEsmLhkMHr7-qd-AxfVBZCyEWL9456OgDw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟢
#اختصاصی_پرشیانا #فوری؛ باشگاه آلومینیوم اراک رقم‌رضایت‌نامه مهدی‌مهدوی مدافع‌راست جوان خود را 300 هزار دلار اعلام کرد. باشگاه پرسپولیس طی روز های گذشته با ارسال نامه ای به این مدیران باشگاه خواستار جذب این مدافع راست شده بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58K · <a href="https://t.me/persiana_Soccer/28582" target="_blank">📅 17:29 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28581">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nCqr2pr8nv1cfotjnEf-T5dA3vXXAQa-pJD6jawr3i4k_n5jpPTAvEWOEbmrCMO3ULCdFYa1TORvT19awkosXP04Jh8HNWDUdhLkn6T2LUWyw_HJJcGeMOGAcWpDO23wZvomKa3hM4zEaMqEOp8gawLYUmOdPdd4lhLkY68snFLTStFR22GNq9e7ue2kFhBHDkctgNEgJk_kEj5xnBCydkAcNB4rtECeDgglp668ZEdWzp-08ny5BvjFrA1XYxNjh0dxOze54AzZGcaav2o_F5a9c6PCs9rwyoQwbbljGAk6jurh3EeCZv-ugZAXZuRI5nT5wMNYZcHUW0MjtAJ__w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
⚽️
🤩
#تکمیلی؛ همچون روز گذشته؛ خولیان آلوارز در تمرین امروز اتلتیکو مادرید شرکت نخواهد کرد. آلوارز میخواد سران اتلتیکو رو تحت فشار قرار بده تا با پیوستن او به بارسلونا موافقت کنند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.2K · <a href="https://t.me/persiana_Soccer/28581" target="_blank">📅 17:29 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28579">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oxjh65scSISmOW0iEgFjnkHJqNFqLpWkT1ua-fApMOe3lx-brCQ7FBQ-Dhwh-9Q2S90Ke1oWbonkTGAApE2rzqlZ6bBU8yL-4z1mtXI0liLYdJ_OxHYqVUZNwzBnr5HH1m0WX43pzcSdoUX7hr7xqkNKDO7hLB_Ob2EOhFEHyAKPaT8Af3aCIGOJQvLkHrnRgF-rzLCZteUVO2HyQAgHeviYCoiYedeIEHxJe9jqvW6sY49OIgw_g4rAiajMxCGRvtA23w2qXoqCos89y2PByubz6PEf3lIl_WpDEQOdhquxFXGH9zkHud_Y9gaqboOzaTYGR3Ismr_BdfL3uaHo0Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
🔵
تاییدشد؛ بااعلام باشگاه نساجی؛ کوروش اژدهاکش وینگر18ساله تیم پرسپولیس با قراردادی قرضی به این تیم پیوست. همچنین یعقوب براجعه مدافع راست جوان سرخ‌ ها نیز با قراردادی قرضی به‌همراه بند خرید قطعی به نساجی پیوست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.2K · <a href="https://t.me/persiana_Soccer/28579" target="_blank">📅 16:48 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28578">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NphChqMjt2amuA8PbrMiVAjQBqH_heb7Ktj6lD7KpAaRDv54CPhknQNG5TYzoCxv11W8CzSeeQvNcKfl8sYk581Boyh4qgBo-pTSE4rE6dewJjCfEJR9GfiQMynkZ-sHu3QrwUFjGCy37BVroTsbCMVpftNiR4gfoWNkNL9gdB95-U1DpmvmKV0jO_JmvOA_veYGPC-EVa7RYcmIl2Xwz-O5m1gKxciL3Iv-zd9ozOMOkADTLbh8_4Joj6PJH72VJHTGHz94mAmwM7driFzeENQjUi3OEbTJFjB9y3UZOIud8KjQgSfi8VrZZEhkxumW0u052qnnMnp7Rk1w6CvZTg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
وزیر ارتباطات:
پرونده فیلترینگ باید در کشور بسته شود. بزودی‌بادستور رئیس جمهوری فیلترینگ فضای‌مجازی برداشته خواهدشد و تموم پلتفرم‌های فضای مجازی بدون فیلتر در دسترس خواهند بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.7K · <a href="https://t.me/persiana_Soccer/28578" target="_blank">📅 15:57 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28576">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/drsIsigQoQKrOm1RZF4atiCsO4v3uA0w6IS0GYVLcXznxGPwGm5LK0KaLo-J9FlOsatQJootqgDUC8z3amigaDko5ZR9yYtv9Ndb9ulivL7E-kxinJFJMKfkM02r6C8zruvggOyXKW-A23wiB0G8WiMkGhS1lVZ8vG1lxg1F0gmFidAwc4O1mAiG9BJFZ5Vhbt3_2y8D1DhCBZ6oGLY8zX_atmyfy2QdKvqcL5rWIweth6IwJbMZgtzpHKFbZak7Ytgv7WOTclsD4gqk50GcZOrgrCWIw1uQSBKRKZDqE6E9l5yfWbWLcFKCPRrFjqa5aES9tfGs5UPGYqQoqxoqsA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📱
استوری اوستون اورونوف که گفته مصدومیت جدی نیست و مشکلی برای همراهی سرخ‌ها ندارد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.4K · <a href="https://t.me/persiana_Soccer/28576" target="_blank">📅 15:27 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28575">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/maA0Wq9Y9hn6llFBAI_CoE3OAgtB5y2ytIWaZAMfBZrLXPyWIuazbubU6iXHsxefYEp8eb0JYp1Fhi4Otzijmm1VcjgcUU7y0ZHpmLzgUnfUrdg_soK-jdIAGFEbkJaVreTZckb3cOz95jBXzz60LU7GX4hPiDMHpnHph8N_6N85i6WCTNnRMyAnVmH1kF58de3D7IXRTcd20JmltIOvnASHMtWUxXKE9GGDyeEzMl4Xztdt4S-E-JWRejCtaDIL3MDbdpR9BXsMEGH-lrWfKtAsjyAynAM3gCpzK0cFeQwwT3_ykJK5gDDBpXqxUZx_bZNO5PorUU7NqAB2htvWzw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
#فوری #تکمیلی #اختصاصی‌پرشیانا؛ مهدی تاج رئیس فدراسیون‌ فوتبال عصر امروز به مدیرعامل هلدینگ‌خلیج‌فارس قول‌ داده که روزچهارشنبه باشگاه استقلال روقهرمان فصل گذشته لیگ‌برتر معرفی کند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.3K · <a href="https://t.me/persiana_Soccer/28575" target="_blank">📅 15:18 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28574">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/22cb4cd7d4.mp4?token=GEp21H5mYyIFUCSyrRDdwxRsHlaEZxMTvvAqHb0cmRV2SgcB514HCUo6d5GnIVgLPxKfl5O5PW46gQ36nAXXVUttyVjNwqv2lqLPxi1S00eGQIATk1Qwh1YTvAFgsiRhaAYBTDJTnZEcezP4avpqtx3EUEOpfLP-Xgx9aUw8P59n1rETYs6gYTyPsVKHGjnEuljyOy7VXACQLctLSiCJZe_9_JV4cU5ydmaNjMz7IddnxJdtrSRRkjWITQt2ZIVf5adlJAM8daO2E7ew-GLVWNLRt-oKHHeC_Y_lVZCUq-sQAYtFqLELkFqC-FfDjsD6mfS1Y9EA1PWBtPJST-5U5Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/22cb4cd7d4.mp4?token=GEp21H5mYyIFUCSyrRDdwxRsHlaEZxMTvvAqHb0cmRV2SgcB514HCUo6d5GnIVgLPxKfl5O5PW46gQ36nAXXVUttyVjNwqv2lqLPxi1S00eGQIATk1Qwh1YTvAFgsiRhaAYBTDJTnZEcezP4avpqtx3EUEOpfLP-Xgx9aUw8P59n1rETYs6gYTyPsVKHGjnEuljyOy7VXACQLctLSiCJZe_9_JV4cU5ydmaNjMz7IddnxJdtrSRRkjWITQt2ZIVf5adlJAM8daO2E7ew-GLVWNLRt-oKHHeC_Y_lVZCUq-sQAYtFqLELkFqC-FfDjsD6mfS1Y9EA1PWBtPJST-5U5Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇸
👤
خبرنگار در پایان دیدار با سوسیداد:
امباپه میتونه به رکورد ۶۰ گل رونالدو در رئال مادرید تحت هدایت تو برسه؟⁣ ژوزه مورینیو: من چهل گل با جام قهرمانی رو به ۶۰ تا گل بدون جام ترجیح میدم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.7K · <a href="https://t.me/persiana_Soccer/28574" target="_blank">📅 14:46 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28573">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Z_CoCPq3qcFNT3dp_h3G_J7C4xaCTcJkr7VQF7BskYLybqTYB5r9DDiZnUwZ8aNqMmYClyhedWPd6op0JC_jyPT7bmg4pFsNhKOvqIRgPozSCQcb7hiHDMJ9J7BS2WJrI3RwqOFhJTYxFMozKhjczDB4I8Ca-Wa41hkbyG4yWaJb9WOLANFbGrEY2wE2uvhxJ38Bi1VISx0fFP7viYLniImQlI2a9M6NvqcxGE-DMIgCkmjY3kbqTUIoXgXOlyYk8OKMARK0k2afx76PKR-QtWnRLeinH6kvmOiqtBual5wc09IWGw_OVR5mAm2Ah2oyf904KjCdzpRrKPpoWXvKyQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
زنی باطرح‌شکایتی مدعی‌شد که توسط سرایدار منچستریونایتد در دهه ۸۰ میلادی مورد تجاوز قرار گرفته. این سرایدار در سال ۲۰۰۹ فوت شده و شاکی به تازگی شکایت خود را ارائه کرده. باشگاه منچستر با اعلام اینکه این موضوع ارتباطی به باشگاه ندارد و طی این ۴۰ سال اطلاعی از آن نداشته، بمنظور عدم مزاحمت این زن برای خانواده متوفی مبلغی را جهت جلب رضایت وی پرداخت کرد و پرونده بسته شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.1K · <a href="https://t.me/persiana_Soccer/28573" target="_blank">📅 14:12 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28572">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/f5cnszvXVp3NX9cvUCTDQkIndFeG4ug3MkeWfFpwj1F8NMmnjsYBq-tG2Dg2dlFw1BQeANTpN8EkpTDA0_Sc0Vqj_qGC1YAAZ89D_tiIWQw5dH_HpWgpgJDVdS36lglFLE3afvEi1GGsZDYSrwK1VGHUaLKwmDmzadWvCGO-9c-FeS0zpwjPcJevCJnFPDXf3Cq4E8fXtyTAP2JuY5nrs3nFIGtEXpakAqbe1cNFYiWjiAWUsdea099U3W1j4zO2lTAwWfi0qm7Bk0G8hmbdYrO2K2eM1WjjyGampxFjCXG4IjUytRnWTTX3lucR0xt9Qn97qcsPvKSLfXn0JV-T7w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
⚫️
از سری اتفاقاتی که فقط واسه تیمای ایرانی رخ میده: استقلال قراره تو هفته اول لیگ نخبگان تو ورزشگاه السد میزبان خود باشگاه السد باشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.2K · <a href="https://t.me/persiana_Soccer/28572" target="_blank">📅 13:33 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28570">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/kAJ_xGHhA9zSFBuUn_yOWrlh3PWqwyVWI2C7TE_llpF01XKOFVkGVJbk_iUc57DD3EQvetD9dWzF92gNt90FA_dW9VqZf5U-jx25d4GcpNSb_nwsoI_9YBIkrLtwv3rTxS6Hqn6ppBxiC6mWyQaGkAcIIc_V4D12UN2T2JZ2hkaHmMMlx0HzJlpGTDfyZVLIPeqJNExW3Wa_D1jJ_ykHjnfn0KQdYkYMe5EEgFBO934eT6xo5Ae70YcheA1D9UomxYVZyh1iR2joXsKxXDoxC8sRQ0BE27kLoSNaRyJkv1q54GnU_rN-6UJmwLeLo0QjbVoAglkidUic5oKfEMsR7w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/tYi6ShstwPc8cvVHIFZA4FXtcimwpz2zWMxYHqHHN3SSktkzUO9bnAYHQ83KvDeC9g9AjBNPHrAfoEBZ8MQoi9IjH_60WsY9k8wjRQSEov9ny0E9AvUwL-JIImV1Jt64CwyI8PBqaYksjEWq3V_dHq8pTs1eKEiB3DPgqzocYeK4lWaqcbtCnatgTCyinsSqmMDLawBCSR2kbPcCMW4jgGRNhYWZRrCitSqtibEekAwhzybN4aOI6tjkN7we2r3JC2jXzj7jURbO_QI_wv8GgnhPfeWmwG45uTOZSSZUlpov9pYgpGo1-x0Gb4FWFJepCMAv5ztE5q27EVgZFt3B9w.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">‼️
باشگاه میلان بعد انکونکو؛
ساموئل ریچی ستاره جوان خود را با قراردادی قرضی تا پایان فصل به کومو داد. ایجنت ریچی پارتنرشه که خبرنگار شبکه ایتالیایی DAZN نیز هست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.7K · <a href="https://t.me/persiana_Soccer/28570" target="_blank">📅 12:41 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28569">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rHO5dFzajwvTyISZkZoLKLPAiRyaK3_l_AdW_HfpC_1hQc7dWWbJk8v81nBaCEXEaGW5AvBoFi3kACxs52u56PNMLMwpOEYpRMK0KZLl6JXSviZrbfyZwb1haiymfZ5j8fFcQ71cQHexsgB8yl8deDbt7mg3l3ytZHLFvcaL-EQX-EI30GHJbCSkpvzQvBzzVU6R69RISfccFEzUhwQGUsKYqqVqkRakJL_eRhi7Wb0cHos-68PWxr6VyrfGkym_trsSnrsyPYBmD7fUrQE8v_C0hrtWqw0k8dpwdW2yAO-m-52ou1tRuYQh4wgxpdgLiu89jSSildduW7C8JnpeLw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
باتلاش‌پزشکان‌باشگاه‌ استقلال؛ روزبه چشمی و جلال الدین ماشاریپوف درلیست بازیکنان استقلال برای دیدار فردا مقابل مس شهر بابک قرار گرفتند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.2K · <a href="https://t.me/persiana_Soccer/28569" target="_blank">📅 12:28 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28568">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b570a2c1a4.mp4?token=dZrdApuHXX2VnsGGE_T067ZpXu45zMJRzmKKhmeUNAKvPlS1CSfEXwjZm6FRJIK-jyo-YdcV5iNX0KS_ebIlEYQ5EYj8QNyOCOqizBTCu1Au-DtF1SmzU0CwAUL-hZ_hoz0NCJ7PjyZP7_K2vLTPDhP7oK8-Kyu-B-CRjG-kxWCsx7n8nXZgMqlk7GxHlRDGztwmnBRVfbBwD0Oi002lz4L8ozeIZYX1nSdrvIc5ate5oM7spg9Blym-0r1eoyHEQodgF5bevzFfa6daLRPiWMQNh849XwQycLG0rpOK9XYaz1fOQTPXazl7NRrWfugqTK0QtoXdXKZDs5jz1ohIaZIEwE01-PtKLo6CcfEpBrFPxBFT_G5F38q2DN6fU9rMEwq6IMLZtZup3FZdPee_rYfuik_a3pCuvKyyAi-uVIR_E5XCr7Y-bM-8Pusto3wx8vhL87O8gjASmlNYSYQ-izsUibxuxumghTaCUTUlX1nacBNyD5-Z5DAx7m-ixi-P5mhAo1B09VleGOreOpY2-Bdx6kWPiyjcQ5KP3dexX23lBt_EYWQHTGWJ8SBUfoWS0jiY7Yn-rNnf3ov-HGU5Akb61fnhKEOoQPybOkUZ61-Yr80802vW3yF5ZNkO2Bht7EGJg_XxPo87lxNIK0t6jN6JizOj5InMd0q-pYWVVAA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b570a2c1a4.mp4?token=dZrdApuHXX2VnsGGE_T067ZpXu45zMJRzmKKhmeUNAKvPlS1CSfEXwjZm6FRJIK-jyo-YdcV5iNX0KS_ebIlEYQ5EYj8QNyOCOqizBTCu1Au-DtF1SmzU0CwAUL-hZ_hoz0NCJ7PjyZP7_K2vLTPDhP7oK8-Kyu-B-CRjG-kxWCsx7n8nXZgMqlk7GxHlRDGztwmnBRVfbBwD0Oi002lz4L8ozeIZYX1nSdrvIc5ate5oM7spg9Blym-0r1eoyHEQodgF5bevzFfa6daLRPiWMQNh849XwQycLG0rpOK9XYaz1fOQTPXazl7NRrWfugqTK0QtoXdXKZDs5jz1ohIaZIEwE01-PtKLo6CcfEpBrFPxBFT_G5F38q2DN6fU9rMEwq6IMLZtZup3FZdPee_rYfuik_a3pCuvKyyAi-uVIR_E5XCr7Y-bM-8Pusto3wx8vhL87O8gjASmlNYSYQ-izsUibxuxumghTaCUTUlX1nacBNyD5-Z5DAx7m-ixi-P5mhAo1B09VleGOreOpY2-Bdx6kWPiyjcQ5KP3dexX23lBt_EYWQHTGWJ8SBUfoWS0jiY7Yn-rNnf3ov-HGU5Akb61fnhKEOoQPybOkUZ61-Yr80802vW3yF5ZNkO2Bht7EGJg_XxPo87lxNIK0t6jN6JizOj5InMd0q-pYWVVAA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
دیشب گندوزی بازیکنی که قبلا مارسی بود در جریان بازی‌فنرباغچه و لیون‌حسابی رومخ هوادارای لیون رفت از زمان گرم کردن که فاک نشون میداد تا بعدازسوت‌پایان که اونجوری خوشحالی کرد و دیگه کار به دو سه پارت دعوای سفت و سخت رسید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.4K · <a href="https://t.me/persiana_Soccer/28568" target="_blank">📅 11:49 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28567">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nkGyIEhB9M_GXCza_qFcLOTBT9VAmPKRlPtO4lpoGsEhbIyUTw0nNvO9ypATiWKS1YowTQCFMZfxz6rpdrNub8-X2xVvDZFz_9ZAThpapeK7ywZeK8SpYODnTpVAAw-zWmMN1qettL-eDnX2zUadzcxON4Vj6sVoXMw-R7LTOKAplDiIHW-P0tuq9RoR1m8-n0UFn0hLZYH4o0xe9rUz1C_-pJeUhOk7vqzqZG-buqqK0xioqgeFTCdYWT7hSpnPK-Vx6eb7LCDt2PMhHR0kwXy_bnzHsSJ7K03osY8vvPFlaDtHBejcYLWa_-zvq7scD4MZSbmKTdPIwTftg-4Org.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛ خولیان آلوارز تمرین امروز اتلتیکو رو پیچونده و گفته دل درد دارم نمیتونم بیام تمرین اما یه‌کمپ‌دیگه‌رزرو کرده و انفرادی میخواد تمرین کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58K · <a href="https://t.me/persiana_Soccer/28567" target="_blank">📅 11:28 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28566">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GlCTcVSyfDQVqnvJuQKhn9hyu-CvUZU9xGGjEON_bSyY5b8ZaRjfcFNtgehZwbyw61PC_jABBg6uv9NhbrwXwIhRCU6uz1uOuzZknmwRM8r7wJhv2toanMTArcVzsycGlj1UfsiC2m8rvXC0I1EgDn4PVmjZzAZwiQ9XJgJ1SXXgFOoMElvdERXu4MaKk8N2TPxXspq5RuXKYsWd1Gnsg7TiW2_ye36T66kT_ombnqj5d7I-WZQ8fUiTKjKtnZgCs0rDa-M7hLiK54TACRaT_Y5kdb7hwar5tWjQAjLK9YjPejhkAoUAKfhj61FY2t2Fh4bFMYCbecHcomjlUCDNFQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🔴
#تکمیلی؛بردلی‌بارکولاستاره‌فرانسوی PSG در آستانه پیوستن به لیورپول قرار گرفته. توافقات شخصی بین او و باشگاه لیورپول انجام شده است. بارکولا گفته‌که‌نمیخوام PSG بمونم سران پاری‌سن ژرمن هم گفتن لیورپول 140 میلیون یورو بده بند فسخ قراردادت رو فعال میکنه. لیورپول…</div>
<div class="tg-footer">👁️ 57.6K · <a href="https://t.me/persiana_Soccer/28566" target="_blank">📅 11:28 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28564">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">🇪🇸
🤩
با اعلام رومانو؛ هکتور فورت ستاره جوان بارسا به دلیل زندگی در اسپانیا آفر دورتموند رو رد کرد و با عقد قراردادی به رئال سوسیداد پیوست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.6K · <a href="https://t.me/persiana_Soccer/28564" target="_blank">📅 10:40 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28563">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ed9d6f5b21.mp4?token=m42PRUH7zy22ztuaHpd1UBiHMzq85LYLRhsDmnzPtQ91NZVgQiU7_8gL8Ugyp93voCNbXxHuTzhziTIgquU_e-G03twNUJ92yaz8axu_EaBfnl5LVsw8yPBu22tGQYr56N22CkDdgB2coYdejSqpZAkgUXAVmDuvk1KiFUYyYmcZocVOj2QbnNFeca_rELSovcfwpz1xXMhGeqOGXCqXIOZk6McM9Us1WdhYY4H1abVFgm7e5F-0sez90i2hGD5Gt94wxiOGKXjSehudoWyfQQ_J5EwYX6nLqMruUl28eHoVE_VLtU4OIC9ilLdBGoZOul3WhAvAeBkqJVLSxywUUg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ed9d6f5b21.mp4?token=m42PRUH7zy22ztuaHpd1UBiHMzq85LYLRhsDmnzPtQ91NZVgQiU7_8gL8Ugyp93voCNbXxHuTzhziTIgquU_e-G03twNUJ92yaz8axu_EaBfnl5LVsw8yPBu22tGQYr56N22CkDdgB2coYdejSqpZAkgUXAVmDuvk1KiFUYyYmcZocVOj2QbnNFeca_rELSovcfwpz1xXMhGeqOGXCqXIOZk6McM9Us1WdhYY4H1abVFgm7e5F-0sez90i2hGD5Gt94wxiOGKXjSehudoWyfQQ_J5EwYX6nLqMruUl28eHoVE_VLtU4OIC9ilLdBGoZOul3WhAvAeBkqJVLSxywUUg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
چند حرکت فوق العاده خفن و البته ساده حین ورزش کردن برای درآوردن سیکس پک‌های شکمتون درکناریک‌رژیم درست به قطع کردن قند مصنوعی و مصرف کم روغن در برنامه غذاییتون.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.1K · <a href="https://t.me/persiana_Soccer/28563" target="_blank">📅 10:20 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28562">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">‼️
این تیکه‌های فان داداشمون به امیر قلعه نویی و مهدی طارمی مهاجم تیم ملی عالی بود حتما ببینید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.1K · <a href="https://t.me/persiana_Soccer/28562" target="_blank">📅 10:00 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28561">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/E9kyY65b5ehC9wjqi5A2GFCkhfQKK8yQdnfX6u8X76m69LQhyJYX5_gk0IXHpeKy_GvvFQ3LG2wZjtZ3zmaRPFfzhx6cvSrk9IoRRMvA5cuYrDoomSOXWq5-Q7re_VwjhugTsWeeD7hIetIc30keMqwWg5vMBs_3Q7vIRwJ37ae-E0NtXYFFZtbSrWioVZ5LDe-PcfAnn5YuhoHVC9WM3SBNpX3AnpgkckFRS4nfoNwIJSLgrIQ86wNNSFG9UA5k7Mh2urMnmA2jcJHWQcqlztV1mCslQTcFR5hnNc4nOPSnuphmWUvYGxggST7of5Sg5324PwjNCGluZ1WCrGM4mQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
شاگردان مورینیو در هفته دوم لالیگا با درخشش وهتریک امباپه چهار بر یک از سد سوسیداد گذشتند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.7K · <a href="https://t.me/persiana_Soccer/28561" target="_blank">📅 09:40 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28560">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/K50mB5I65sP-s8pz4RYSiwmYf0qsB3VsChvh7k7OcTvPzo8LEVabhAiQg3dbeTX8vZyTF-GWGCmnX5ch3cKCFZ6jL22Q3nIhtvfcyRNQDyIRcUPB8FQoX1SRLicPT3pv0TMUwS6ivSb4nuAqOnOLbJ3EM8XVrOSw-SJR1DPBTellGk-COsLWJiXxr7ggd4ajHNr9CLIIjNxDcs1Ey4ZGy8iAMRIv8KnPkB7m3yf0EVXzOEGgwDFjv1PWFKO9mNa1En3m84lrd1xC-F-KF8IbrNToMWB_qUMRPeYSyyYQsBoxKE0-Rl2A2U_J_jLF2M06TGmmLH6ZuTzGGpebhscBnw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛باشگاه‌تاتنهام‌امروز100 میلیون یورو به باشگاه‌منچسترسیتی‌پرداخت‌کرد و از ساوینیو ستاره 26 ساله برزیلی جدید خود رونمایی کرد؛ سیتیزن ها دراین پنجره 12 بازیکن خود رو فروختند که بیش از 400 میلیون‌یورو سودخالص کردند. الان هم میخواد حدود 140 میلیون به…</div>
<div class="tg-footer">👁️ 58K · <a href="https://t.me/persiana_Soccer/28560" target="_blank">📅 09:17 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28559">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/F5K4dER7a6N8375aQ8XUfe25SKzLWQuyYGNU3mhh9DDm2ViQ0mvSoN099fcNm-wTxjPGhGucbHpcDUOWisMKqbgn57A9NYytx02tOMeiIU8_Z28vnujgrDfb32mUobCDwDOQMQlRhFkfhwMqA2m0CR4lN6H2EJH-EqXwqTKshQwdGTbt915uBT3EU3Ir9TjRMfbkjduD3s-eYBMG5EFF8aF9DsLlupoPkHDjhFwRfHFubhqH5bVVn-8vGKzONWC8-d5WDZRh3EE8ld84gaKVkOruZHDZGCsDqbaJv19zpjc3H40mX1GvfDnTg8pN5YqG3CzfX9eQvRBTHZb5woQA0g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🗓
#تقویم
؛سال2021درچنین‌روزی؛
کریس رونالدو فوق ستاره پرتغالی سابق رئال مادرید و یوونتوس با عقد قراردادی دو ساله به منچستریونایتد بازگشت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.1K · <a href="https://t.me/persiana_Soccer/28559" target="_blank">📅 09:05 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28557">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QuHoxdN_kuwYKBguS10AetSJsktEXPuRDdGs2muPxnuVUbl7PFnSQTwsNK0OzwBG3UIAeeFvsSaNwDnu2OBfpLFUZz41qFqHTIaiX_zva7WWYfnvq3HmjgeH02SqWHh35sNpG9ajLKBdmuZWbsKkj7VYoK45a1GF7kGVpKFtcEP1Tn3isC-GGBy_Lxj2INzlLIKZ2ExsDlOfkGVOff3qSNOEE3Uj7ik1abtPtr6VpQPE8QvUMOw8_uCpCQo2GGTfZN-wI0XZaXhgjQ-3BNALX_Y5__xEd1kvV7pUlLPYpE6-p_GPc_JjXxQH9WjLkqer4hQEWUdND_CbRQ5dZDZ0ow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌‌دیدارها‌ی‌‌‌امروز؛
دوئل‌جذاب‌تیم‌های هانسی فلیک و ادین‌ترزیچ این‌بار درلالیگاواستادیوم نیوکمپ
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.6K · <a href="https://t.me/persiana_Soccer/28557" target="_blank">📅 01:57 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28556">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JRxfQnuteY5-uWwhOSw3f1BNn7V1dEKyDyeM-weY-2tQmR3tJDvBdnj-R9GLyVJBdfx3j55BrfNo0tnYeBUusNKmk5UoHQbFr3rk-D3H1NBvM1fQgAUXri3KHDKSxXOUUonprVH3rC8p4AQnCAE9nPEIB5r8mSxtrsFgdi2-0o7hxmGQAUviEseRVYWcz3kv9yQExcVJgQSz5Yqe4ki8TmEt8xePW5uABZBAROvXXL3ptdgp1NcnW_14-l08GcV3arQNGQQWORwVxw2rN-qxXO7uTp-cIT190cSsj5gBEMX5IOsXlr6WzHgQCNZuyseBpsxatZmiFcFP0fpLBxJFDQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج‌‌ دیدارهای‌‌ دیروز؛
از برد رئالی‌ها با هتریک امباپه تا صعود یاران کارتال به دور گروهی UCL
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.2K · <a href="https://t.me/persiana_Soccer/28556" target="_blank">📅 01:57 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28555">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/60b5eee892.mp4?token=Ff3QYkOFcsexCcHYX7vDvWEF0lhlBZHDlkJtpI_FMvSr3eog7lPhzQT0xD8JviFnKL6hYC5WhM532ou1HbQzQW6mAhtJjo3QptQZNNKcrmGpJgnhkT7co9U3RP8YcGKiIWcHxDBPp3FbjF6uLiHY1E4dq2L3b7MnFpYNoCJR083dDCb_LPTbn_Gm_J1UWT7bWlGaBKl0A8uY8ZX1EwOucwbtGiZ7Rlcy2PPpdkyen7QyFbHUWbfeQz4gqQHwSEGx30ve4w7A5VQF0hTNzbpSdip9Gzz9NigpkUL96CPLamL-J13Lypyqh-LQTFGQGtPhdKZnxBAbhdUEp07VIwhA7Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/60b5eee892.mp4?token=Ff3QYkOFcsexCcHYX7vDvWEF0lhlBZHDlkJtpI_FMvSr3eog7lPhzQT0xD8JviFnKL6hYC5WhM532ou1HbQzQW6mAhtJjo3QptQZNNKcrmGpJgnhkT7co9U3RP8YcGKiIWcHxDBPp3FbjF6uLiHY1E4dq2L3b7MnFpYNoCJR083dDCb_LPTbn_Gm_J1UWT7bWlGaBKl0A8uY8ZX1EwOucwbtGiZ7Rlcy2PPpdkyen7QyFbHUWbfeQz4gqQHwSEGx30ve4w7A5VQF0hTNzbpSdip9Gzz9NigpkUL96CPLamL-J13Lypyqh-LQTFGQGtPhdKZnxBAbhdUEp07VIwhA7Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
#هشدار
؛این‌ویدیوکوتاه‌از صحبت‌های مهم دکتر علی کرمی مدیرآزمایشگاه‌کنترل کیفیت مواد غذایی ببینید درباره مصرف آب معدنی برگاتون میریزه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.5K · <a href="https://t.me/persiana_Soccer/28555" target="_blank">📅 01:44 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28554">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FTa1trkLJcHuwN6mYV4PXAp9SOlyrGa1r1AVavCt4SuOXjvsOd8xJ2hQ75jVCok24WI2cmHRl5IlGsjGwu3mSeNF16H-i12AtsN2afZOs9EqyHjCazOpxNb942r0k3tG0h_jh-wwOf-lnwi6_WyAFS_sYS3QIOCt1vc5Bt2W4LwTBlOvXP-YKAIdus2d7Xrv05mMpo3Ix9jFbR9OIPUylC8fSK9IMkji5Q6kEh6AvsRrhqSg2V66OFkQPYOcxLyB4YCh08dLLdmjTwZ6VrscAIDyjkmYiSLTcXkRUfHbNs21zxrkIy2f6AtP-VGcl_gLTi_pE5UwNSUCbGp2GcRkVw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇹🇷
فنرباغچه‌امشب تو بازی‌برگشت‌پلی‌آف‌نهایی لیگ‌ قهرمانان اروپا در خارج از خانه لیون رو ۲-۱ شکست داد و با اسماعیل کارتال به چمپیونزلیگ صعود کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.8K · <a href="https://t.me/persiana_Soccer/28554" target="_blank">📅 01:18 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28553">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZdnMAn9RVbZfm_lAMu14Wmqs0mKxQ26Ss21zOrsDGHScvrqvPH7EhpdOl6OqPYk8GWx37ImV8ubJlWL_rIx1YDSIatRyQmYzUdtb5S4O-Iu4wnAXQLbvC3Htq_piQeC5pY3d02elhaXSrC97RMPihsMz--ApubpfSdcxINJWiC1SVNZVVooKEkT5-9BYl7Th9x9CIudXoBq-m8Sy0WtbW-aG3Mcn3bm0gzTeaLyaJyxEdviTTmqEPGsLDOO-7cpDYE3qc2Wl3fBxH86iJsmeqwQ1joWkb96saAWNPDInMukSPlkhDoQrX4DAnfvr7CWkIhaTNmHCD6RfbBuJsfbg1A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
🔴
#اختصاصی_پرشیانا #فوری؛ مدیریت دوباشگاه‌پرسپولیس و نساجی مازندران امروز بر سر پیوستن قرضی کوروش اژدها کش به جمع شاگردان مجتبی‌حسینی به توافق‌نهایی رسیدند و اژدهاکش با عقدقرار دادی یک‌ساله به نساجی  مازندران پیوست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.7K · <a href="https://t.me/persiana_Soccer/28553" target="_blank">📅 01:18 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28551">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/szNJhh0ZsrQJfBTgReEtyv_UxnLv_MArWr12uPWdVckRxvyfPRvPcWRAzwzicxVfcBXwXsBwJqH3HiWWHxXGWQ5T0IVR8dLorsJww83oh4ChoTEkIBr8Z5GEI0fGAbYtuoQfvlALFyyKv79pnR5sKtUfRGT938kDWFas6txiY9I7nzktqUAspAnNsgDr9fwqhTBSv3KfKEsGDWKZu3onQdopuYLXsIDn58j3wIf3reXJkxUiUAPSopk2_kFU_7-bjRXJYEoj9U4DLDNg-03UWdCN-nhZ7czNd6-wshefEyDMwyAPHojYhJnnbI6DdHcTYX0rhFSjwMu8zKSn9CteAw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇹🇷
فنرباغچه‌امشب تو بازی‌برگشت‌پلی‌آف‌نهایی لیگ‌ قهرمانان اروپا در خارج از خانه لیون رو ۲-۱ شکست داد و با اسماعیل کارتال به چمپیونزلیگ صعود کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.6K · <a href="https://t.me/persiana_Soccer/28551" target="_blank">📅 01:02 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28550">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DlnOBfhZVHSR_cJ4M8kyYHiwArR01VCxOAazScOuj_ZmCHYpisg6DcZlk7iml6C_SHY4a-v_C-XpuNIDwQMHRGmazLRvYBkhvJOS3kCehMmBsvjPcbOrdfkMdBC9PTFHl2f5hbpBD73WboGCWWMoqOG3mitjefwZDJ5KSR5ylCwh-aCO99Z0LCBnNCbEhso5sYNgZ2zQY2Ywn-VybgrKpoTubYvE0C2qpgvd_7D2Q7HG3ndXh7GYiLKw9hmuOJzPc_rGENiY-7O78AsZNiK5PUXH_gXAK9jhi5XkzVfNeaqVnsXVCvHXX4crXw4-7cYzJ4r3jblagmd7Z3KXI0PU5Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
شاگردان مورینیو در هفته دوم لالیگا با درخشش وهتریک امباپه چهار بر یک از سد سوسیداد گذشتند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.9K · <a href="https://t.me/persiana_Soccer/28550" target="_blank">📅 00:51 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28549">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LyndtkkRFcowi8cmwZpv7RBppZWQdOiDfTwQFg_QJOc_gvDKFPf5zWuvNU-oLZpWOG0wuuXrVhQuoJSxeyaKfm-D1aunprJZtyEPjQ8JSIcZJdnnHF5KTa2PvO7aBDZx8Qoq2Sh724lVpy7mYUjgGYtPwoxaYJMUUYvNBTpnEHpsLfRGIdI25wyytVlEh70OJdlt-_tPdjGFWJrkw_bkSz2NqWhVbtPSqceuOmpbe1jsvOsaupOjIOcHTlOxUiixOvV2W1UVL8diUPImzjziaUIyWoWtz6_7NbHJf9AcAl1_C6z9FSLkpk1Ur4DFR8vE8MnWOX9gpn3HEpPlQ-qc3w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
هفته‌دوم‌لالیگا|شماتیک ترکیب رئال مادرید برای دیدار امشب مقابل رئال سوسیداد؛ ساعت 22:30
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.8K · <a href="https://t.me/persiana_Soccer/28549" target="_blank">📅 00:29 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28548">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jDJlSG4BwigiJhHklpIPZR0lB7qAm7cPZipJwtzhzsAPvPfpNIkcD2cF5dbX8f_-hTbFL-bHQzJUL8GXKOHfY_lHRo3bxwbriCrlcqsU9MLaw6y9OSIYvU2bWKHwHQQT3286asKvOHkMeGv1UlYzSaNPj4jsfFNd0Cd6ZQHc09YxRZ_BuGeXvXPQN07h_Lisq_txIEtEhAp3SWljjRNO3N-8_-Dv0CHeix1CmmzOTsMCZALgAhyjfD5ywUYrASaKNFvgz5gZSOmIKSZG0nsEvrJK1TkiqCvEjkEKhHFKj81TaOexcyVugsXQ4JeiHIwc96hT0m_SEFWljzfu04KxQQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
راس ساعت 24:00 روزچهارشنبه پنجره نقل و انتقالات تابستونی لیگ‌برتر فوتبال‌ایران بسته خواهد شد. بعدش باشگاه‌ها درصورت جالی خالی در لیست خود میتونند که سه تا بازیکن آزاد رو جذب کنند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.2K · <a href="https://t.me/persiana_Soccer/28548" target="_blank">📅 00:07 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28547">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">‼️
ویدیویی‌دیگرازجشن‌فارغ‌التحصیلی دانجشویان رشته علوم ورزشی این بار دانشگاه آزاد تهران.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.7K · <a href="https://t.me/persiana_Soccer/28547" target="_blank">📅 00:00 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28546">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TdU7SAd0fck_5wdSGAZX3d1YXFGNK-L4JAkp7UgY0WGd-MoaT3fkv-DvMqFC1RC_VEc5j2kbhWv8tH3KVSdyS1YB5BRDoQFBow3xx4c4N7s_On_VhgBUQ3sSTNOpb8ZX6xFvntzhFLgW8FZvX6CqcLDCmUJGWCX5X7hgesRKJLHlkDlOpCjiPWermY_vP7QYslwBLZB-BtLwiOKmlN81Ah_ePit2B8dqR5FS2ltB_b-iEyvmUDvBsKmix5ol-2yEngRsUvFTOXWl7vW47uiaHwMDwbqkFziiJshZUANasuyBH-BMv6agN9YpVmG25cnS_WrkbqKJfRyhwkgpBx6MFA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌دیدارهای‌هفته‌چهارم رقابت های لیگ برتر؛ شش دیدار روز جمعه برگزار میشه، سه دیدار شنبه‌.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.2K · <a href="https://t.me/persiana_Soccer/28546" target="_blank">📅 23:41 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28545">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/b6F6xAb_stiJUbV-eCGqrnTLj6-Sk9itcRplupcmpkDxPz3jWhzHQ-j2wIt93zRSh1nByRizA0143i5HnOc0Nh8JlVwWmZ4m8Lox7y85ie3HrPEL6yQCA09MX3PP3ehZCSVkojmuxp_de7BcGHLRp-Me6ncmUQsk0FvZ4y80vml0t1H3dx_IwOqgW22myoWPnZiROZnP3YRD_tpqqwyo7_NB4kK5eJnpkX0CinVCpYKjbur3F45krl7V_msWaZipzEUh7oOIsIYNgRjqbIlCjxXv5XASDLUieba3OydNJe23Gm-ks3qhKMKhPVtXJAneZTFoFKa2b_PpD0g_DqCwSQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
طبق‌پیگیری‌های‌پرشیانا؛‌پاسخ‌فیفا به درخواست باشگاه استقلال برای‌جذب 3 بازیکن آزاد بعد از بسته شدن پنجره نقل و انتقالات تابستانی لیگ برتر منفی بوده و پنجره ابی‌ها درنیم‌فصل رسما بازخواهدشد و این باشگاه مجوز جذب بازیکنان مدنظرش رو داره.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 59.4K · <a href="https://t.me/persiana_Soccer/28545" target="_blank">📅 23:23 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28544">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">🗓
#تقویم
؛ 3 سال پیش درچنین‌روزی؛ لیونل مسی تو اولین بازیش درلیگ MLS این گلو به ثمر رسوند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.2K · <a href="https://t.me/persiana_Soccer/28544" target="_blank">📅 22:40 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28543">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/r6k-MM_a4UYy4rGq25vcVNTWluIZRu6UdKCuulG5Bj4wegMo6hR1gIGpbozjanFUXf39lh8USNGw6hsVKe0LkcbrAuOFEXE_5Oq7snK8r87hLsZ60eQi1KwYm_KNPQ_y0pnx_zn3511IfhvdrXJNCTOmiTk7TsM7E9Rdj6x-GRAkfLWP3jKqNhBFxsIwoxfYD5W4TvE-Uf4lIykrirEwuyRIWaUyWy2B6JANNdnwHSMKwfaJVXxb6rTgNlIg2qI_dmdWZQ057siB3AJAGOtf2vXJDpTrQFwTHRCiBSZMZtliuPhHT6GKVGw2nr7ZUvja-vC62v3Df9Giey-ijneSEg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🏴󠁧󠁢󠁥󠁮󠁧󠁿
#تکمیلی؛ اولی واتکینز ستاره آستون ویلا با عقد قراردادی سه ساله به الهلال پیوست. عربستانی ها برای این انتقال 60 میلیون یورو هزینه کردند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.3K · <a href="https://t.me/persiana_Soccer/28543" target="_blank">📅 22:27 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28542">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4ad00b2ad3.mp4?token=gFXxLxSap6-PzRBnwo8cy6L4NRAui_CwBHKcmBcrPInXLBoBMJtBPW8VcbSeKd-d4cphztAElFxChOB54GVph7yH5nqjXYtSP9gFJxUV-xDOH8tkIUbMkthJCVpJhdgDsUEAd5E3-W2ntezaqGzCzUWflzOBm4arbin6eH8N3RA3xHa44BlxClSPPuqqKfLvgegQhtcPQDOyelYWHLJfX0fFmsI4JhTyDPb-8C8eVxtqPlp3LahBU2uP_1K3sbBntvkLGTq5NpTSM148PydyHXnVG2T3RBfXJ-E53O8vjcL3T1VAFL0gqihai_Ri8J6eegw3TKwDo9gqadhxK4qD7Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4ad00b2ad3.mp4?token=gFXxLxSap6-PzRBnwo8cy6L4NRAui_CwBHKcmBcrPInXLBoBMJtBPW8VcbSeKd-d4cphztAElFxChOB54GVph7yH5nqjXYtSP9gFJxUV-xDOH8tkIUbMkthJCVpJhdgDsUEAd5E3-W2ntezaqGzCzUWflzOBm4arbin6eH8N3RA3xHa44BlxClSPPuqqKfLvgegQhtcPQDOyelYWHLJfX0fFmsI4JhTyDPb-8C8eVxtqPlp3LahBU2uP_1K3sbBntvkLGTq5NpTSM148PydyHXnVG2T3RBfXJ-E53O8vjcL3T1VAFL0gqihai_Ri8J6eegw3TKwDo9gqadhxK4qD7Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
رسانهTRTاسپورت: بعد از جذب لوکاکو، باشگاه فنرباغچه‌بدرخواست اسماعیل کارتال سرمربی ترکیه ای خود خواستارجذب رافائل لیائو شده و قصد داره با آفر سنگین او رو از منچستریونایتد هایجک کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.7K · <a href="https://t.me/persiana_Soccer/28542" target="_blank">📅 22:06 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28541">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hYVhZZTeUy2btHKLymDtK4C6NesSuxrwQElpYzaLaDC4crua_YYuamXq1zvwBjrhudSZiIsEdRu-P0D8tl3mNbNYoxHTyGLyymQrSDHdBxjcx6Ps_em50uhT86M5v20ncraBlcpCfvxEqe-Z1olmVt75Ic9lBZ0Onx110rY-fxhhIMqROPQRe7839fYazEvxB8uuMiJsUXisCtlvh3ptgQDP7UxGUkc9ZGh1P_o92dii-SLorCAZVhElOUrzSauIyCxp-SeXfhPaFwmkCNAnrRIUQjHnKgo-7QFBiSr1UfkX7XXSKPCN3V8IhAOD7QiDveAC0d1agqn1Ba1v7wGCDQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
آستون‌ویلا با پرداخت 65 میلیون یورو به چلسی نیکولاس جکسون ستاره‌سنگالی این‌تیم رو جذب کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.2K · <a href="https://t.me/persiana_Soccer/28541" target="_blank">📅 21:41 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28540">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MBthuF_Ue0z40uHNtDHCDOMRWO4RZc-ZsvOSfEEvBBijUBg9A_XFR37Gx7nLQ4TLg0WMRHWZvwVB5xbnOdbriBnCQW4ljLNGreCtdEwG3GP0Zzug1xkUSa5oH54Y0ONiL0D6xRK30tevRnJTLhKwD9KtJdWzLE9RVzU5AmC6U6So1fzxxTZpP4LM87YfZgcE4-IX8qwF-Uw-Ms-nHWDLaELGocOFi3dzYZ73wOYrt2IWLnzsdpkOpCwhkP95ilLDlJRj8h_RLOFsM5O4ELndSholSzTTK6hb5vSMZd0u9sMdtTkWb_fVbiODzdQA2zoRptJPvD_j8T0gFLDTPJyYZg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
هفته‌دوم‌لالیگا
|شماتیک ترکیب رئال مادرید برای دیدار امشب مقابل رئال سوسیداد؛ ساعت 22:30
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59K · <a href="https://t.me/persiana_Soccer/28540" target="_blank">📅 21:34 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28539">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UBJuvU866Gnyu3Kku5uU7deVucy_OuFshSC1cyBksRzCDZ-d-PHLERvlSFYqmIpvXgQ61_wbRVcnctopzFy3hV5k2B-R9HFkkyDCaelzYoyJ8Pgx1yDd8li2USZNRaDt5gnK-ynOePDgKYcGuZAPJZJPLAVX32VJ6_xpifILScQGe2boFIw0rRjZPWUAifjJtW8RAS6-TAuwXskTAfZdjGiSyp6i3dEFO_g9lhZWLjfKndV1zJJbJm1pS2pyfcloC_gIEOdMbIjd6tAJ2ZInRdE_qc7c_SvWaXiPx3nZtOND7lZxkNoJ0z2FBVRRZPtK3WfH5qzx5qDhf2VxAiTnRQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛مقایسه‌قیمت‌دیروز و امروز پلی‌استشن 5، آیفون 17 پرومکس و سامسونگ S26 اولترا
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.6K · <a href="https://t.me/persiana_Soccer/28539" target="_blank">📅 20:53 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28538">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QVt3bPJd_iCpoVUzXu22C_MQ1vI67wb-LqhLBTAvwa13deguahQHKaumWNpCLYt76Gch_SM3OXLqnD5ddckYjvcTx4b51NEzO9WmvXaxOuM7cQvlI2aRKXjTO_xVHPsId4UZEeAf1sUsPyQVw6tZx_vu0gN3pk4R3jq1m1ATi0jt9jtC8SBGFjxGhhoy2obVWbHdmEZ_lH8imlSzNFj9jqXkDLq-mFAbEiwPKuSVNGXx6uOZVeIQgeQEe9GuSbEjk8LSARpvPFi_SH18uK2mlma5e1Gfc1uSnjp55D48k8yZQs8e-xrtwEnvMnojHI7xbOE6nFLBrgaJplVwK-Tskg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛ خولیان آلوارز تمرین امروز اتلتیکو رو پیچونده و گفته دل درد دارم نمیتونم بیام تمرین اما یه‌کمپ‌دیگه‌رزرو کرده و انفرادی میخواد تمرین کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.1K · <a href="https://t.me/persiana_Soccer/28538" target="_blank">📅 20:43 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28537">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/03aba91807.mp4?token=UBvnAK0VKIOZlOdAq2EjFTMogNsi_yI_Pm25i5RrsXPxBrkMxD7BzGAuBByQFK5vaj_UC85Eu99usmaEIsRuBA7wPqLwUp28HwKCFR9uykDjGSgG1_6et-FPYHZ_v63w9oEDSKWV-HkSYCaZBfEMSfRVz9BBtVYqHHlxjYoy3_yNUcu-jt-rvtQZIfsO3wbWd6ZHyyEpWgdVIkufSNJ0036bQOX2MrKN7RREJ_n5BAnAOrcXqIXkwbIS-PakREc69BVxaOx13p4Et-69n2KTRrjNa6zotkU_I23DLeRkeYkSVHNRqr3EUcK1_vBBcnSHK3LsmSKMTfmTw4UaNAB8_w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/03aba91807.mp4?token=UBvnAK0VKIOZlOdAq2EjFTMogNsi_yI_Pm25i5RrsXPxBrkMxD7BzGAuBByQFK5vaj_UC85Eu99usmaEIsRuBA7wPqLwUp28HwKCFR9uykDjGSgG1_6et-FPYHZ_v63w9oEDSKWV-HkSYCaZBfEMSfRVz9BBtVYqHHlxjYoy3_yNUcu-jt-rvtQZIfsO3wbWd6ZHyyEpWgdVIkufSNJ0036bQOX2MrKN7RREJ_n5BAnAOrcXqIXkwbIS-PakREc69BVxaOx13p4Et-69n2KTRrjNa6zotkU_I23DLeRkeYkSVHNRqr3EUcK1_vBBcnSHK3LsmSKMTfmTw4UaNAB8_w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👤
ویدیویی از سیوهای حبیب فرعباسی دروازه‌بان بی ادعای استقلال در سه هفته ابتدایی لیگ برتر که سه کلین شیت برای آبی‌ها به ارمغان آورده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59K · <a href="https://t.me/persiana_Soccer/28537" target="_blank">📅 20:33 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28536">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8aeff973be.mp4?token=EQrfhi4T-_Kh9X0SVtI43dMxI89iPHY9iLO2976TwdEcCAWxQ9CgwvnKtUyTR5KVxladEBBER_cAZSKXxdP1OfKdTyCyTiz8OkoMpaweFK6JYAnYLGIPxaicQ4E73WTpbQLbbHvRb5WgNnZtsdBNr34WuxS8EGHUrTmVbcHUkZuXfPWBPBPA6R5AtOmtSAApIAJO_Gn9T0MkYjphTF2SHdjhsAQTj26DlBRgdl6Gml3aqyH-s8ntZi8MYrxcvmUrfxwkXBkydoPZ8BgiBrsD1dWehQxJQpWMc9eU3KnQjWVNg66UpiG3dMtjDJ4BOAiY19aSypK0rDc7PBPPXYHNRA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8aeff973be.mp4?token=EQrfhi4T-_Kh9X0SVtI43dMxI89iPHY9iLO2976TwdEcCAWxQ9CgwvnKtUyTR5KVxladEBBER_cAZSKXxdP1OfKdTyCyTiz8OkoMpaweFK6JYAnYLGIPxaicQ4E73WTpbQLbbHvRb5WgNnZtsdBNr34WuxS8EGHUrTmVbcHUkZuXfPWBPBPA6R5AtOmtSAApIAJO_Gn9T0MkYjphTF2SHdjhsAQTj26DlBRgdl6Gml3aqyH-s8ntZi8MYrxcvmUrfxwkXBkydoPZ8BgiBrsD1dWehQxJQpWMc9eU3KnQjWVNg66UpiG3dMtjDJ4BOAiY19aSypK0rDc7PBPPXYHNRA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
آیفون ۱۸ پرو رسماً ۱۸ شهریور معرفی میشود
‼️
اپل با انتشار دعوت‌نامه‌ای رسماً اعلام کرد که در تاریخ ۱۸ شهریور ساعت ۲۰:۳۰ شب به وقت ایران رویدادی برای معرفی محصولات جدید خود برگزار می‌کند. انتظار می‌رود در این رویداد علاوه‌بر آیفون ۱۸ پرو و ۱۸ پرو مکس، شاهد رونمایی از اولین آیفون تاشو با نام اولترا باشیم. اما احتمالاً خبری از مدل استاندارد آیفون ۱۸ تا بهار ۲۰۲۷ نخواهد بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.6K · <a href="https://t.me/persiana_Soccer/28536" target="_blank">📅 20:21 · 04 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>

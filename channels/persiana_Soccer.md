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
<img src="https://cdn4.telesco.pe/file/SgUfEcR3shLhuSwninn-34iOUl9mK5wKS_vUSoWP2bc_L2sa8XUuUN2fVWx4Tw1wylhm1s4xRWB1NrwpBSNubVYjyffUklrr9Uh62Gr2HX2Jz0Y4Xff2PT6pR4TJIizSSpV7HD3PsEIEiZkz2qfcIpFf-UZwlmI1xYjz-3RAIVD_paqDFWYxFzz1r9shUowHePLg4mYIHcSbhbnSXZo6AQhRjCVhRTMhs71g3ppbV6q5XHAPrUKRd9DW5J5_ts1t8FX7ycmHnTnk-hbkHJw7IaqIo7m270fgCHz2Syq-GrRout5zbrzgEKw2uNkBaVYIsDRGXuERh36N_s1bI2TYhw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Persiana Soccer</h1>
<p>@persiana_Soccer • 👥 633K عضو</p>
<a href="https://t.me/persiana_Soccer" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 پرشیانا ساکر دریچه‌ای تازه از اخبار محرمانه و داغ فوتبال ایران و پوشش اخبار اختصاصی نقل و انتقالاتهماهنگی و رزرو تبلیغات:@adspersianaکانال دوم رسانه مردمی پرشیانا:@Persiana_Plussپیج اینستاگرام:Instagram.com/Persiana_Soccer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-07 19:12:14</div>
<hr>

<div class="tg-post" id="msg-28677">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/h6uzsJ1SzPR1QcIzvJHRUHeS9s3EetlGwV838oqL0HE9Jyb1nFnRrCgKUu-CuSlGiObbICIZECZK7Ya_wJxvD0ZxS0KSUhKubvk100JGq30aHioRcvo4U1Y7YYhy7kSkIibi3zDPbLHrNWEs9EooCkGVgfmiSx5HzYU1DDfCv-3YlMDkmUZG3esKw0ar4bsDToz4WjNq-NnhBjd3EU6XOx92_5RladdxUqu9sOERXljkMCkTObIaCMu8ePxX6_KgsII5mVsc5UBsKstGf3nV9GR9KaVpuzBCBYCGm1jyLvZx6obP_pwhrfQUB-_Cm6vpO3lk2w-4WjHiq80h5pKAfg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
هفته‌چهارم‌لیگ‌برتر
؛ شماتیک ترکیب پرسپولیس برای دیدار مقابل ملوان؛ ساعت 19:15 از شبکه سه.
⚪️
Persiana_Soccer</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/persiana_Soccer/28677" target="_blank">📅 18:18 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28676">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e9cce8d93c.mp4?token=ge22Sf9gh14J0ltPSfBww2FKM2SGxCxlMM_a8ANvMTX9gG-AOmJDAIsHYS4qWQGr3FbRe5Rf9JK4-ow0rgdfd5vRJI0u9o7AAiejM9-se2TQctypnk6hYiCrTMXaIoTUVRvJuy-UPAVSPMXA2Jj3FZjNJ2XWIyZf5FjAokYsHqTCPBj8CYzU95sZ133gX_-WDeJSdOPUDnGMnVA-2UtlsLWe5rb6nkaCNL1cPEWDAnMUQk_sYF5Vn8odDdyuyzgfPfQ_KH8-SClzMIV-sfg3JrN6Bi9zmbipqH2bEORmoy980vS6VmvOxI2Z53ebNOLWn5IM999buKhoiMMqFihlyEYERASHmNE74Xb0JVOeCzNhisAGxSwUy_hs-DvvTwaBvwfQLVVuJUwknrMISoy87XUgEw5mDBD__qQflvkQTTnVjftWXarfuYhkNkvt_h-I8oYw9-l7vai31Xkm9DU8Jrl7MeDgNYeOnk97CqS8E8TjVRnvM-UhlhOFrcc7cjHRE2Zbs1svjTBbnF2Xzso2Jxu1mdt7vj7JhfUyCNrg2sl1GqLtPKeGqubtax9nN3MOXO3vzz9B628RlUX8Su_luFwhAp1XSEM8xLHluHWeSLjKgyc9It1TdgiVCC6i-_HzaB0_3-qWyQ8RsmddGnHgRdDmMISAt3atAjBOxrYtxgQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e9cce8d93c.mp4?token=ge22Sf9gh14J0ltPSfBww2FKM2SGxCxlMM_a8ANvMTX9gG-AOmJDAIsHYS4qWQGr3FbRe5Rf9JK4-ow0rgdfd5vRJI0u9o7AAiejM9-se2TQctypnk6hYiCrTMXaIoTUVRvJuy-UPAVSPMXA2Jj3FZjNJ2XWIyZf5FjAokYsHqTCPBj8CYzU95sZ133gX_-WDeJSdOPUDnGMnVA-2UtlsLWe5rb6nkaCNL1cPEWDAnMUQk_sYF5Vn8odDdyuyzgfPfQ_KH8-SClzMIV-sfg3JrN6Bi9zmbipqH2bEORmoy980vS6VmvOxI2Z53ebNOLWn5IM999buKhoiMMqFihlyEYERASHmNE74Xb0JVOeCzNhisAGxSwUy_hs-DvvTwaBvwfQLVVuJUwknrMISoy87XUgEw5mDBD__qQflvkQTTnVjftWXarfuYhkNkvt_h-I8oYw9-l7vai31Xkm9DU8Jrl7MeDgNYeOnk97CqS8E8TjVRnvM-UhlhOFrcc7cjHRE2Zbs1svjTBbnF2Xzso2Jxu1mdt7vj7JhfUyCNrg2sl1GqLtPKeGqubtax9nN3MOXO3vzz9B628RlUX8Su_luFwhAp1XSEM8xLHluHWeSLjKgyc9It1TdgiVCC6i-_HzaB0_3-qWyQ8RsmddGnHgRdDmMISAt3atAjBOxrYtxgQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
بجای‌مانده‌از دیدار روز گذشته فولاد و استقلال؛ دوئل علیرضاکوشکی و رامین رضاییان درکنار زمین.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/persiana_Soccer/28676" target="_blank">📅 18:08 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28675">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lHlDvNK0UDuqtR6g3Q2c77Y7rtBn43LJcpVb7I1CBIaD1kYSfeTERFUKZHwqTezu0YMc2mN1p4y5TvVhjbp0SnUZEEK0opEmP8JzBnrUPax1iB-fMFujUNH0zQcUFUQxV2ywOJoH0GXkvphdlLjL9stRf1Px4AgzQPzRURYjEMwTF_HtYgCbFxqCCSYToo03NfqfX0nJhpKTFrhlD61UkGETZPk6rRJIP-pMKkvQ89v8o8Plc2Q5YoBXLk5oLpoU8LzbFAW-kn9T81eA3ubKBgswghtSEbomryP6zbB3JN1YzmP1LXdPBlqfMx3Cof-_XlethZcOo8EDouPcYLL4PA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔹
دوخبرنگارمعروف و محبوب شبکه DAZN ایتالیا برای پوشش رقابت‌های فصل جدید سری‌آ
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/persiana_Soccer/28675" target="_blank">📅 17:51 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28674">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f7b03755e8.mp4?token=s8tDLlGmNbU47r7rbQdMsFubLb5psATFqTaIDHlbln7BgrKfUFJILasLNFgp-r5u3xqrMsQGs8ehyu_cf05-hcFRZYDVhNvEbN2rFgMNiUaIRjc5XQvffLhyatiNlBPOHUZQUQLqydIFdWDsbIzo0Jjd__2pH48Lc_2p2biCUaWWDID9iYgv4_t49oNOocF_1fenoB-aN8-jDEN3rb4hUpVqdkvB3MRk6pNm8XysNay7jiUfKYYmsUOlxcJ1nQSq12_tRZrKDRxhe27igLZHS2lrASzvp8YnTbL7MFQTDy4Fn9IxcfWcC_cvlF70IlvEydgklF_G32HEIet0KDFbXg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f7b03755e8.mp4?token=s8tDLlGmNbU47r7rbQdMsFubLb5psATFqTaIDHlbln7BgrKfUFJILasLNFgp-r5u3xqrMsQGs8ehyu_cf05-hcFRZYDVhNvEbN2rFgMNiUaIRjc5XQvffLhyatiNlBPOHUZQUQLqydIFdWDsbIzo0Jjd__2pH48Lc_2p2biCUaWWDID9iYgv4_t49oNOocF_1fenoB-aN8-jDEN3rb4hUpVqdkvB3MRk6pNm8XysNay7jiUfKYYmsUOlxcJ1nQSq12_tRZrKDRxhe27igLZHS2lrASzvp8YnTbL7MFQTDy4Fn9IxcfWcC_cvlF70IlvEydgklF_G32HEIet0KDFbXg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇸
👤
صحبت‌‌های‌خوزه‌مورینیو سرمربی جدید تیم رئال مادرید درخصوص جایزه ارزشمند توپ طلا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/persiana_Soccer/28674" target="_blank">📅 17:23 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28673">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mavqbls4e3vJT1k8j_rplps3T9OjzEIUX-jLsrV8V3ycRXD9VjoU3L7tpTpzHgsmv_gdS-dDREQQ6rU0yeBNpE-O27DZj0AtO5AYRxiSw2VtHRgRUfsJyI6zq-AapP2E4uMyj8B7GM4pu7w4TRjj4FsUF5c3Ia0SkbmRFzYofLka2sE__kudg2DMu-v7m9UskUG3FKj6CQHH1yvnWhjhgQ2_NemFVpGSOyNAxGLR9AJHX5xJvrvDae5FcboY3VD3JquTjzZUv1XxZdc1zibQKyWSqZYdJ7NaYMfJfsGUesgRL9L0x6FK6TFFbZtFfdp_9fNnJnjOgMdrNitkySEWVA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
به احتمال فراوان تیم پرسپولیس در بازی مهم امشب مقابل  ملوان با این ترکیب به میدان خواهد رفت،ستاره ازبک دور از ترکیب فیکس سرخ ها.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 31.6K · <a href="https://t.me/persiana_Soccer/28673" target="_blank">📅 16:27 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28672">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/873c1f0eb1.mp4?token=Wsn2_bnuEJl8sg2i4EV9x9BqVPiN6JNL-fSYxaWJuz8v3Wp2LVII9wJ3K_rX_q9xq_kfdEd918e8wZaSDLT_lxs2TwRZkAJQn-_gkOrw9sZfMaWpLRfu5WvPf2e3HhkChvIJYgWCmKfkX2Yh216yBSpfghKYqn-qrM9yp-OrELnGg5c9mT-GikkduxktMHw8hcw-O80TQ39zeSdWn1i_FNZPbWXKOQ_IeCANM9guAum1ppsagUdd4KDrWEVIVYtbhrqgoTS2Rmvx5fKF3ffwI-9NVVsQJa3AVj4DkIZgEVN870LepfwCZpe--OIiBNqS3z12knuNEKTF4zGDRLJPiA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/873c1f0eb1.mp4?token=Wsn2_bnuEJl8sg2i4EV9x9BqVPiN6JNL-fSYxaWJuz8v3Wp2LVII9wJ3K_rX_q9xq_kfdEd918e8wZaSDLT_lxs2TwRZkAJQn-_gkOrw9sZfMaWpLRfu5WvPf2e3HhkChvIJYgWCmKfkX2Yh216yBSpfghKYqn-qrM9yp-OrELnGg5c9mT-GikkduxktMHw8hcw-O80TQ39zeSdWn1i_FNZPbWXKOQ_IeCANM9guAum1ppsagUdd4KDrWEVIVYtbhrqgoTS2Rmvx5fKF3ffwI-9NVVsQJa3AVj4DkIZgEVN870LepfwCZpe--OIiBNqS3z12knuNEKTF4zGDRLJPiA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇹🇷
🇵🇹
باشگاه گالاتاسرای با پیشنهادی 50 میلیون یورویی درآستانه به‌خدمت‌گرفتن رافائل لیائو ستاره پرتغالی‌آث‌میلانه. لیائو ازمنچستریونایتد و الهلال نیز آفر مالی بالایی دریافت کرده بود اما به طرز عجیبی تصمیم گرفت راهی سوپرلیگ ترکیه شود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 33K · <a href="https://t.me/persiana_Soccer/28672" target="_blank">📅 16:11 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28671">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Jq-zt1RVJGBiy9M8N_VNfWEUfYTkpVqySqVrKrBs9MRYb1hBeLT-tCF9CXrUZsDv4UXXcuoCJnT1lzVnBNdJ3kGnMX7BEXfdjzHCizL-GjEWKnMVFszlTK5Y7tpRkZ-QGXoUQg4VBlBdlaDYd6IMscCUA92Dui1T2-E_VdAvNr1snvjfRflMejbleYT8Mt9HF92CFHfQFbe28kkdJ9QmTFS5lIy8pBczIKFKmCqkgis0m6CPRE5B3m7Z1kw3SE7YXNJ8IkET8edWReW-Qf1pBLFBAksYB6vXjSHw7QPwgSBB8N9EQAATJSm0P3GSWQs9WIo822rMVSDu5KyUThVRxA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
شماتیک ترکیب احتمالی پرسپولیس برای دیدار امروز مقابل ملوان انزلی در هفته چهارم لیگ برتر.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 37.9K · <a href="https://t.me/persiana_Soccer/28671" target="_blank">📅 15:20 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28670">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/26e418389c.mp4?token=QeCv3OOua9RLshwJ4qZqy6No7b4LMdBntECrd_-vJa3hZbwcJvjq2kqijtebEHosN6QE_i-Wmptvlw0ndMGd6y2MDOSSlIc2ekbXm7yqrnd6rUiS5rybtK_Bi61MiRiDEaVJCMEALjvZwpicQvsaDu0RVX4Nue0YNnf2W5NU3nRepF3mUKhErclfKTZJt07uD2UzpRUHOe-k6BRs19ID5zF4fDKgs8Zb5WT_jpzGLA-dzaMIKAXxXUNgd7ZRilkyZy6_52McVpz-MP9a4_3vdnfNd9ikMeRHgYJW4KaGQr8xU7HPdG-zyvhg1skZ3Yb2XCeVjjNS0p3P0pK4k5uTHg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/26e418389c.mp4?token=QeCv3OOua9RLshwJ4qZqy6No7b4LMdBntECrd_-vJa3hZbwcJvjq2kqijtebEHosN6QE_i-Wmptvlw0ndMGd6y2MDOSSlIc2ekbXm7yqrnd6rUiS5rybtK_Bi61MiRiDEaVJCMEALjvZwpicQvsaDu0RVX4Nue0YNnf2W5NU3nRepF3mUKhErclfKTZJt07uD2UzpRUHOe-k6BRs19ID5zF4fDKgs8Zb5WT_jpzGLA-dzaMIKAXxXUNgd7ZRilkyZy6_52McVpz-MP9a4_3vdnfNd9ikMeRHgYJW4KaGQr8xU7HPdG-zyvhg1skZ3Yb2XCeVjjNS0p3P0pK4k5uTHg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
رونالدو بعداینکه‌دیشب‌گل978دوران حرفه ایش رو زد یادش رفت خوشحالی گل معروفش رو انجام بده که مانه میاد یادش میندازه اونم انجام میده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.5K · <a href="https://t.me/persiana_Soccer/28670" target="_blank">📅 14:41 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28668">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/rqzjjsHhnnCzsstLwpRTVAMdRe5g2n7CA0g9bwOQ9lHzPBr7s5Y4VR1Tb5Dl__fzWFsqmVmNsKy8sJIHLYNOJqfzWrCiVD-CHE7kRhWSW3K7Pixsgx4P8_WaPFhUel-FF_G8uMUdimHRLI_deK8cE5NkRQkpo8JwmKynjJyblNjpXM1LrUp8f7oGw_sFZJWqXpIgbV_fJaIdnrREPsmg4k3Sl3FhUG_29zcChV2bE4de9UohpNSzZoyDL6JCk8rzf_SAEK-BtMohkS10mZlEjbUCjzeSsXZ8DMXTyb_Qnrdyjygs_2ll66osLWHlJRI_aEmoXTBzD-v8DtEsVRIvMA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/iCsQ8MHwbJrTt7XP1wLl59QAXOnRHL0NAm2Swc0Ggx5gO7jJb1uw9G_L24Mp2FnCSLp2iAKfCgxtI36S-hBMb6ujzJuRyT8bAPasrIaBlSh24JTOmHX8gDQKy2KT-WVsWyfTgopTQL91RWMF9TRUVwnXiJ7uvr2KlHmKnlI4kMHFRFlT_LkOkd1I2N9-ANPW7y-FbqusG08YRLoadE8QqodF9aMDZQONPA0nuHSgKfsu7F7dtcdnTd0RDGOE2OYVafwAw8ZY-Gw3ZKVsJxnyBRVNb5zZ1qnctiQMilmCNcHrHfWrom90DQabDf9_WuJefb4dIPJCigpwo4RAtYHnqQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📊
آمار نهایی دیدار دیشب دو تیم فولاد و استقلال درهفته چهارم لیگ برتر؛ بازی در حالی بدون گل به پایان رسید که آبی ها امید گل 1.4 ثبت کردند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.1K · <a href="https://t.me/persiana_Soccer/28668" target="_blank">📅 14:15 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28667">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/evpvrIKjbzyLCHI-IwIMBU5vgthZeBsxENf3qPUD3MobTPCK0x4A2SdrEDJosclhsflpYaGbRM6x6uj9nITOH2GF8wPI2Zrv4lrG5umuCKNd5FpcNy8Q-qtk5aJ6Rok98oQZUwdHEMaX4mTT9F-vIASAh1-2FgNUpy2-O_r2y1x1QgKiBvvCYEu3QxqzWyjVqaPJICulY3X4XCCMR1Wz6ysMtLqszK-00DnVWQvBGLndqcS6pJRJMEvawN03RqwsgLWxXxT8s2NN6Sq4vlVMLa9iOAlyle6yQuB1uCQNKOA6yx48nsYvlMZ8xyschRL--J0aOwp0apVfEOhn1ia3Kg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🔴
سید ابوالفضل جلالی، مهران احمدی و رستم آشورماتف سه‌بازیکن‌مصدوم سرخابی‌های پایتخت به دیدارحساس‌شهراوردپایتخت رسیدند. تقابل‌ بزرگ دو تیم استقلال
🆚
پرسپولیس یازده شهریورماه ساعت 19:30 در نقش جهان اصفهان برگزار میشود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.6K · <a href="https://t.me/persiana_Soccer/28667" target="_blank">📅 13:50 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28666">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d08aa642e2.mp4?token=L3b8NBNb8IYJWO8lzvXXhKmsUhCZdO3BG_faxyrH8Z8S0Ugu1UczHtpCRRhgf6OyS8YFfZLtyExfamnxO8mvddDLl2uzSrauB22XHFysHzFTb0z07f12072ZmUbPQR3KMai7mwcNeXKklNKs70XImlLPYuhQO1-qte8TVKD0MTdZRhoT-9O1JVoO3xAXgcAqwBSJcDaf7Sc_tBOTFtqx4SI-ybtVSANMpXOP0JIzymlNa7vfkZcOt68wuE7Ii1mWrH47pqwL0slSlDcLmudShkk-To1bbSMlpGHoryezaAqm7Nw4OiXoD9hnmNs62T1ObmktQ7b8fBVtvGdI3cb_Rg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d08aa642e2.mp4?token=L3b8NBNb8IYJWO8lzvXXhKmsUhCZdO3BG_faxyrH8Z8S0Ugu1UczHtpCRRhgf6OyS8YFfZLtyExfamnxO8mvddDLl2uzSrauB22XHFysHzFTb0z07f12072ZmUbPQR3KMai7mwcNeXKklNKs70XImlLPYuhQO1-qte8TVKD0MTdZRhoT-9O1JVoO3xAXgcAqwBSJcDaf7Sc_tBOTFtqx4SI-ybtVSANMpXOP0JIzymlNa7vfkZcOt68wuE7Ii1mWrH47pqwL0slSlDcLmudShkk-To1bbSMlpGHoryezaAqm7Nw4OiXoD9hnmNs62T1ObmktQ7b8fBVtvGdI3cb_Rg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
پوسترباشگاه‌لیگ‌دویی لگانس‌اسپانیا برای آلوارو مورتا مهاجم جدید این‌باشگاه؛ مورتا سابق درخشانی در تیم های رئال مادرید و یوونتوس در کارنامه داره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.3K · <a href="https://t.me/persiana_Soccer/28666" target="_blank">📅 13:41 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28665">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bTyK6QmftGFWt1HlbX2KlAszpzS1z7_VSD83NHI-oMCKGRBzjarBPjV4zlw6-h5pKo9IlfQBrWQytQyRtsTF3b09QWaLZRI9Y5cEHMUSI5RjWdXTw3z9-lTy44ZKWjiCB9pIdRXT2nOsjl3LROJrhGN-oduevkDIrnNu6M8j4pg75_1xDGPsZg_VIQ2FBWpks2-OYz2Wjb3bF2UcIrI2tIP6EW3jIh33IoF-jfWVSY0WpMQ5ptB53sKW_p2FgcbS2s_VhZ5ld7_djmhUBe588s7D8BDGLiVicZ_XTmTn72W_ErUuy35y1NuwmllehEbjfnNzPpGOfcyDnaDQuJczlQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
#فوری #تکمیلی #اختصاصی‌پرشیانا؛ مهدی تاج رئیس فدراسیون‌ فوتبال عصر امروز به مدیرعامل هلدینگ‌خلیج‌فارس قول‌ داده که روزچهارشنبه باشگاه استقلال روقهرمان فصل گذشته لیگ‌برتر معرفی کند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.4K · <a href="https://t.me/persiana_Soccer/28665" target="_blank">📅 13:12 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28664">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">🟡
👤
تیم سپاهان در هفته چهارم لیگ برتر؛ با دبل دیدنی کسری طاهری 2 بر 0 از سد گل گلر گذشت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.3K · <a href="https://t.me/persiana_Soccer/28664" target="_blank">📅 12:53 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28663">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fzVE0vahYMfuPgJqznV8oNFfPI6212gXTI-cZ-aXl2MWq9D08Yk1sZO2fGOaeiCV-18GnvGGexEGeniPunPd7zBsviFRbAYdivJxWmgvljKiz2T4eF_0ygTwGlCeulaW6u4GuIojneGEP49IhahJ7U4nn487bkay66i4cazknWogn5I8ae59v5P_WNsbuKNucClfSuAXpXzH61D5Q4O0-elaCWDdu47mduvBVgGoyuotDfBZDsi3FJ929KfF82dpMcdDb8CbpUKc-0yoOWnIHMz8P7yzkhQXlE5sqJQ_X9OeDCbCtCcc6yw_KqCVWqMqkuL9xcUS9zJJu36zXxbCZw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
پوسترباشگاه‌لیگ‌دویی لگانس‌اسپانیا برای آلوارو مورتا مهاجم جدید این‌باشگاه؛ مورتا سابق درخشانی در تیم های رئال مادرید و یوونتوس در کارنامه داره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.9K · <a href="https://t.me/persiana_Soccer/28663" target="_blank">📅 12:36 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28662">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/h5mdntFpKMTSl8fHes8r-T4lCPmHFhoiiGHIbbEC8FXCWMXhZIP_N46zlcOqFsxoc6J9RB2EQDYunRRTSVtYHVOCOdPZ8x_VgyVtdXDblnLH_oBfnfc0Xymv6RG3RX0jT5q6Awm3RDMc1xwZ1MXagcwQU92qw6gLJJAk46AxRoT6qtwZxFsi8gV0PoHvQxK-BMvBB2g3Gz88WgZvm5d0JcHf7NOlyNSOgmZYZYQ3nc53PQYHtWWYlMfcj5IyPnxjxfWbi6625yZt-zgh5SfqXj32kEAbtDsy89xhhrb4fJKdXZZG-FKeVXvlA3mi17O2i5LUdOaFEuNexnAPNyz-mw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
👤
#تکمیلی؛ شماره 9 الوصل به مهدی طارمی مهاجم جدیداین‌تیم رسید؛ طبق اخبار دریافتی رسانه پرشیانا مدیریت‌پرسپولیس بعد از اینکه متوجه شدند که طارمی دراروپا نمیمونه قصد داشتن برای جذب او مذاکره کنند که مهدی تارتار اعلام کرده بود که سن او بالاست و فعلا نیازی به…</div>
<div class="tg-footer">👁️ 46.5K · <a href="https://t.me/persiana_Soccer/28662" target="_blank">📅 12:07 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28661">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/K2IHbGsfYfgY42W2VzLGwldlRh-0BTCAq8cDAfCXJHDYuYAgLaJUZbOirk0MdI4qw9DK4v-rOSRTYyR7f2Wa5XWn-rto43pkl8k-Gwje2Y7g0oFBS9T4Qtwp2UkSz4FPkDamDILywaNPafyEOUkdd-HAyoPHldHZwAfAXq1QApvWPbAbEQeMTnuuFArjvVY5gqYmnBnfDurLh-VB_AfAzmEfQd2o2PR6eSYKFjkAenI33DGO8YZZbcNr8-Ky4w2vpm-s-CN2F_vI984PIj3ifOSDBtIOVPCiQbkiF31EiZcGx_GX35p0aJvKTOFjBrzzWwBhqs7pmEFuAIt7jNih8Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🔴
کادرپزشکی‌باشگاه پرسپولیس و استقلال در تلاش هستند که ابوالفضل جلالی و مهران احمدی به مسابقه شهرآوردپایتخت برسونند. 48 ساعت قبل از بازی مشخص خواهد شد به‌بازی‌رسیده‌اند یا که خیر.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.7K · <a href="https://t.me/persiana_Soccer/28661" target="_blank">📅 11:48 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28660">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bj7lAmyRxd35v_T8V9dAn7ugAmw2AIkH6jkImXKrv_tEfMkikgxUQfJ4EpjWiIiM9WG14IsrkxIsF6Muz_b08adtiC_2-ogNEMt0ZvpJQeQx4-RpqVirt32fS7wQwNSXgPVgXyQOAepTjtMHAd4L68_roUuUfap_TpVDv4kUtppw8ogZ4mpMCAGSdKusGJrvLb1Mo_YvzuDKZe2K6THzRIuWUvgy6JtGYJeDzFzgzfFRqn09vK63gPvw1HIbxzGHEs28i4nbpVJksC7imjIkdYigGfWX7H_E4i_adtd7tP8gzfKvm04ZzaG8o4lWEXERyOfX7xrqFQ3n-s2U7LT2Lw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
شهریه دانشگاه آزاد رسما اعلام شد
؛ پزشکی و داروسازی سالانه 137.5 میلیون تومان ناقابل.
⚪️
Persiana_Soccer</div>
<div class="tg-footer">👁️ 49K · <a href="https://t.me/persiana_Soccer/28660" target="_blank">📅 11:27 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28658">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/dhMfbwt7GHyHooPYANjybepy5mqeyMx66ErgLvnwJCqnEuLi3suVScWREX1Mzc_MYGdz8yNXSleogTudEjTMMj8LwKkXdCOda9puq1nghVszYnifW_CE_0gfDPbq_6OqC4ESNZqMu76nYmZPB-HkShpCMlqmO4rQp9lyoan3iCRHeQxGy6o888V_6jKOnJlQnKlFG6qyAiv2QaRUAeElyck1DCX6YZOhomR4Ho9vKQ37E-Uk5QycraB-sr-dvoeiWJW_87c2v_I5BeLq8FrOI-pRgPrm-R-52RcQej-BQIAtYL6Jpt5I8tha4jPdxP1JI6aneJTe_ctqF4uLEiew1g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/tSTTzgSWljDqPyMMbLnbcH2Kwv18fbZJ1TXD1NVYzNkWDBVYyTTWL4Okh8GN6SLr6kGtBV-36v-phx0BjCuqIh1L05H6jYzj-or6ko5HP92bF0h_wYamylx8oCJZ09_ZeXloUauiACLyyAaK-Qc79aHqqiaC3cSPEEXqhxQTNIAS0J2EadWJxBBwkWPM-1fcF6FrF4LOP8IouMVbvEbj0Krt0bFpmveLAnd4MxHdV_OlvGmAU8ATGWlB9LZ1IXXebWoaHcy4lviILtwlZ-MtuYlsbzEaGWbJLf5SnxiHzEHq7wIoG8T808VWJzNx3H3eTdBAAI1YWATcbIeV5rtM8A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
دوست دختر بلینگهام ستاره انگلیسی رئال مادرید و یکی از دلایل اوج گرفتن این ستاره در بازی‌های اخیر در مسابقات ملی و باشگاهی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.1K · <a href="https://t.me/persiana_Soccer/28658" target="_blank">📅 11:05 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28657">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kjDUbadaSD7pqeNBJVJwdrsjOKnjnq5i5LWN1xhHV2W1akAmwQ8HWgYWRSwMZhJ_XKBO7e9Dy_IulaA_KCGALIQCpOv_oplNTHvAUILfaQsHFuEk3nfVRkxRnl2l5AVtFHxZ6uG5JMZsa7K9zLyDYF4DSuU4igTMZdaL2c7ZOeJ0AiG99xHv6QvbQpIz-9OjYydcRezpUMMwJkQy-oE5Q-Swth5m-mf2lYvfIgYDFNbRj5DnZcUKBdFgoZXgFrwYqIXlIqFWEh5GH3mbz1pB9PFg-6t1KhtTee8QtECpJIFFOkyEbsC0CsiMDrk6xB87JbLKUICOBLoC4GvbHidDrg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
باشگاه گل گهر بابت استفاده باشگاه سپاهان از کسری‌طاهری خریدجدید‌طلایی پوشان شکایت کرد. باشگاه سپاهان هم میگه ما از فیفا استعلام داریم و فیفا گفته که کسری هیچ مشکلی برای بازی نداره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.8K · <a href="https://t.me/persiana_Soccer/28657" target="_blank">📅 10:50 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28656">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fa9fc8311f.mp4?token=aAjOg63VabBmlOqHS8kkpxL9NJg5pyGBt-GT9XJWkX4RoE7N-6iZZmANqZx5Owg-wycENwla8L__V720d9APXt5XOeo2zQM-V0237dyQXe3c8BDqbgANSLib-ZC8WQjAYL2sLhrUpu5Vr2HexwHiXzRq1GpgFmye6mKYszxlfRtDYGlXo0CRL4wsBI4qA-b96af0-nEumReSNwSE8ibExNWtTGWkm87MxfOK-rgXD5a-yzsbb9t2kXi_D6bQEv71vjSO_DVBfzKkAUArSNMKa2Ry5s3ZAV-OoiQElAvLo2yEcdCMzck6OIsrpAkljxT0NVjIQhpKIG4nLB2tUu8hkQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fa9fc8311f.mp4?token=aAjOg63VabBmlOqHS8kkpxL9NJg5pyGBt-GT9XJWkX4RoE7N-6iZZmANqZx5Owg-wycENwla8L__V720d9APXt5XOeo2zQM-V0237dyQXe3c8BDqbgANSLib-ZC8WQjAYL2sLhrUpu5Vr2HexwHiXzRq1GpgFmye6mKYszxlfRtDYGlXo0CRL4wsBI4qA-b96af0-nEumReSNwSE8ibExNWtTGWkm87MxfOK-rgXD5a-yzsbb9t2kXi_D6bQEv71vjSO_DVBfzKkAUArSNMKa2Ry5s3ZAV-OoiQElAvLo2yEcdCMzck6OIsrpAkljxT0NVjIQhpKIG4nLB2tUu8hkQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
سوپرسیوهای‌دیدنی‌حامدلک‌دربازی‌با استقلال؛
تقدیر رامین‌رضاییان از حامدلک در رختکن بعد بازی بااستقلال: حامد نمیبود این‌بازی رو 3-0 میباختیم.
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.5K · <a href="https://t.me/persiana_Soccer/28656" target="_blank">📅 10:40 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28655">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/de192f8f44.mp4?token=qPKy2jwsHif-6UEnmcLc_DBIs5-0SYqzn7xJanSUiR2yqPXxcLw2aIQNUIKzIf7_1-JTRVsdha-cQaWyuyS03u8FIM2sQwVn0p_4tEKDZVZuhxvvEmU_hPg0vgmF8XEITSLr6xfpINAQk3Fz6HB3xaILUvBPfUZeWf5AYcdCPs9VbWNqlr3qGXs-weGyEYO8Vq5Znm3ZjXbrEgkATbfSvzDGz_skAMc4d9sg2p7UnLA8xHAH9B6d_fLr-tctG8ZxSCZXAoXJoXEY-pEl3qpsIlk0zFVve9xA-aP_hzdmos5S7ObSM-LClnIhGR5c7Y5KZVV87eFomdwF11R6i253AJQuej2eq3A-2-YUI7d_8gZyIBmrjFJnXBD_WTgJC5djGB8DQCsU-r5BW15-aC2PENNRfoGVs6uy2UMnW4DaoCGlYIGZ_iHs9mZudcphlln3DIMTjmoQPgJ7wUjVmjnPLcGNQ9sr76Cu08bo5-tgfzLZBn60uOxsaczrHHiKmnpysTD9vgPy1sWWggWwCyaXbUm0oaR57NsUBBJBoXcS8OOnBmY5Aw8IenfKrFocbV-nqShSNaalBmd-0Q4QZw9sRo4gJkNdaI_KMjHNnKwyHoH6XjJvf31vC7gQZL-pfX_OXsmcTqf48uq5YU1bcZD4X5hMvEg67XTvBDJplaSNJjk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/de192f8f44.mp4?token=qPKy2jwsHif-6UEnmcLc_DBIs5-0SYqzn7xJanSUiR2yqPXxcLw2aIQNUIKzIf7_1-JTRVsdha-cQaWyuyS03u8FIM2sQwVn0p_4tEKDZVZuhxvvEmU_hPg0vgmF8XEITSLr6xfpINAQk3Fz6HB3xaILUvBPfUZeWf5AYcdCPs9VbWNqlr3qGXs-weGyEYO8Vq5Znm3ZjXbrEgkATbfSvzDGz_skAMc4d9sg2p7UnLA8xHAH9B6d_fLr-tctG8ZxSCZXAoXJoXEY-pEl3qpsIlk0zFVve9xA-aP_hzdmos5S7ObSM-LClnIhGR5c7Y5KZVV87eFomdwF11R6i253AJQuej2eq3A-2-YUI7d_8gZyIBmrjFJnXBD_WTgJC5djGB8DQCsU-r5BW15-aC2PENNRfoGVs6uy2UMnW4DaoCGlYIGZ_iHs9mZudcphlln3DIMTjmoQPgJ7wUjVmjnPLcGNQ9sr76Cu08bo5-tgfzLZBn60uOxsaczrHHiKmnpysTD9vgPy1sWWggWwCyaXbUm0oaR57NsUBBJBoXcS8OOnBmY5Aw8IenfKrFocbV-nqShSNaalBmd-0Q4QZw9sRo4gJkNdaI_KMjHNnKwyHoH6XjJvf31vC7gQZL-pfX_OXsmcTqf48uq5YU1bcZD4X5hMvEg67XTvBDJplaSNJjk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🟡
👤
کریس‌رونالدو با۱۰۴گل در ۱۱۰ بازی به بهترین گلزن تاریخ‌النصردرلیگ‌حرفه‌ای عربستان تبدیل شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.1K · <a href="https://t.me/persiana_Soccer/28655" target="_blank">📅 10:40 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28654">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/F1PN3BwWcwWwMtH0b7QhyH6f9QD_cgrJtO3jR05UyrobHFJKr6_6LM3pH7a9eF_4nNBsQFPBDxNAOA6n3zMZHl6nwp8hfysm-OLTSmooFoqilNG8k0Sb-mXzN0b67Q4rUVz3jdoyESE1uBaHYQIfd4BWyA0981tcyjBRnyNjPEcqqiMoXSESaPbwD3wqG6Pf9Mx0WuTE2BN67cIhOLSJielPU3DCi0-7LS24NuW5koUIWfOTjoQ-r-LWUgAHesJ3EGh8RRzw3S9ED-jtKvG-Q1FvMD8zm7II0-AO19Mbk00cRnqE4m_svbWZ9LvHN_OcQ26vdXwzB9vv-kynnlFecg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 45.6K · <a href="https://t.me/persiana_Soccer/28654" target="_blank">📅 10:40 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28653">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/41bc6c0a53.mp4?token=D7DlwMoqbo4BKZ-ITvQqzFcC7OJXIRs7Sg4oICtMP15ia4IgKWzz8mGQ-MTkofcwdM2Go88QSmiggPk8v7I31Eec4P_TSlORCIn-_k1S-BNF08lKWQRMDVySAx2--3i5XyK-MErWFq1Iv8EFxOFypG6bl1H5nKUSBLNVNw_iLvypDC-8eIJLmHxjl9KCVc_WikyJzAHuBguBXTXBSLCkRtqFWzmUijcztp_dqBL2qd94Xip2otf4weW1eNkwEIOPHIeLuLjPNhWuKL7R9c5Ssa96qzPXuDd1RvN9P8_Sw3NA2iS3igysdDrjquJkVibzG3puiIPgBcVu5sOXO0Fd1Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/41bc6c0a53.mp4?token=D7DlwMoqbo4BKZ-ITvQqzFcC7OJXIRs7Sg4oICtMP15ia4IgKWzz8mGQ-MTkofcwdM2Go88QSmiggPk8v7I31Eec4P_TSlORCIn-_k1S-BNF08lKWQRMDVySAx2--3i5XyK-MErWFq1Iv8EFxOFypG6bl1H5nKUSBLNVNw_iLvypDC-8eIJLmHxjl9KCVc_WikyJzAHuBguBXTXBSLCkRtqFWzmUijcztp_dqBL2qd94Xip2otf4weW1eNkwEIOPHIeLuLjPNhWuKL7R9c5Ssa96qzPXuDd1RvN9P8_Sw3NA2iS3igysdDrjquJkVibzG3puiIPgBcVu5sOXO0Fd1Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔵
🇵🇹
سوپرگل تماشایی روبن توس ستاره پرتغالی الهلال در بازی این هفته این تیم در لیگ عربستان؛ نوس این گل رو تقدیم دیگو زوتا فقید کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.9K · <a href="https://t.me/persiana_Soccer/28653" target="_blank">📅 10:22 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28652">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JeHUcSyCh-cPIphf5_geC8155R2IoVKbx7Pe_fztwo1-x73zrs-wiw3hgIktZn99MWJ2zCIvEM4IpF_SmH5zhL0GbVTzy6xvm5dNQSHpXP4nH3kkDkzi4akxgjeqxBHHYngm7x6AA2Q_wOexyqqI8Fh7E4VEYlSh3dqiVX_9b5SiZ_Z05m-8UAo7-zAlu3Ie2Sy-NClLo4TCHZmWTQV9JLzwOJEjH_tBDuoMzus_wWG6bHTUI_G_CbGU2s49u4E1uUu3yiml6KLhJq9IaD2BgAI66ACHBMPew-tziwi6Ic9yjo-Fmbky01xPD6-rNHsSiwklN1Ps_YlICAF_hhA64Q.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 46.3K · <a href="https://t.me/persiana_Soccer/28652" target="_blank">📅 09:59 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28651">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9f7ef945d2.mp4?token=YVgz_to4lSh2E2h6HpRn5Yqj1XE-0mhORZ73BjwyPd9AAVp26lerJl1qdfaRkDIyzIMLJQAKbqzF3oph8h4W-6O-REZ8ufiud6psSHauuN_4gZcskK5A3FYeH8IAnxi9OZXP9-J_i4FOy9R6X1YjYskOMwUlUmedUGSKdoPCeThHyiDigV9XrHFYBm10d9YmEDzUZH9SUUMzYjID-TrGZZe-wcuLHCQ0yc8-Is2OvGnfVVF8MXhkbaF5po4HtEYR9OlHvNzRoMyqvmddpg5Z8ZHy8oUE7z7axZzaBSUUDxqAkN_4zsFV86XsQ61KHxZzGDSxXCwxPGfctGLocDqikg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9f7ef945d2.mp4?token=YVgz_to4lSh2E2h6HpRn5Yqj1XE-0mhORZ73BjwyPd9AAVp26lerJl1qdfaRkDIyzIMLJQAKbqzF3oph8h4W-6O-REZ8ufiud6psSHauuN_4gZcskK5A3FYeH8IAnxi9OZXP9-J_i4FOy9R6X1YjYskOMwUlUmedUGSKdoPCeThHyiDigV9XrHFYBm10d9YmEDzUZH9SUUMzYjID-TrGZZe-wcuLHCQ0yc8-Is2OvGnfVVF8MXhkbaF5po4HtEYR9OlHvNzRoMyqvmddpg5Z8ZHy8oUE7z7axZzaBSUUDxqAkN_4zsFV86XsQ61KHxZzGDSxXCwxPGfctGLocDqikg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
شاهزاده الولید بن‌طلال‌مالک تیم الهلال در حال دوچرخه‌سواری‌درریاض‌درکنارجوانان‌عربستانی. او با بیش از ۱۹۰ میلیون یورو سه خرید بزرگ برای الهلال انجام داد. سامرویل؛ ۶۴ میلیون یورو؛ واتکینز؛ ۵۸ میلیون یورو؛ مارتینلی؛ ۶۰/۶۵ میلیون یورو.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.5K · <a href="https://t.me/persiana_Soccer/28651" target="_blank">📅 09:45 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28650">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hLjVvj9UUia33sgxvm6I1N7IBrok7MRlFK0oAZ_wJsNPquhnUwK_rboymaWDP6Xyh6xk6kFCod9KNzrXfNK-aCQ-bRJnCs5sfp819jf4g8Bf7uR2YwW9NAgaFXMjj013vm_Yzs-TlqNp3Ruw_VKjoKhKpMU1FmygORKSX3FMU8i2HafxtY6muZdU3Lbwn644xrv4ZgYI0p1LY749n2RCAkCrSuh9oArBSffu0GyoaOA2aV4iEMk3E56g5aYGmc3zg-9nSozpE0RPJS1HyqbFZqnyFxuE6lULI-e9sHC959SSotFx0FxqFgU1e3PBZGWoz19dYJhtdH-tJR233soWXw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
تارتار گفته به اورونوف بازی ندادم چون دیر به تمرینات اضافه شده درحالی‌ایری و محبی هم دیر به تمرینات اضافه شدن اما فیکس بازی کردند. واقعیت اینه تارتار هیییچ اعتقادی به اورونوف نداره و داره کاری میکنه اورونوف خودش فرار کنه بره.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 49.8K · <a href="https://t.me/persiana_Soccer/28650" target="_blank">📅 09:30 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28649">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6abfbbf23d.mp4?token=nqgikrizUOQ-J-0DJ6mQTpfmi8_25dlB87syblwhRyWKHwBs9nKyKeJ0U4iPY3FeBVpCPgYifIXE6Ls-gElZkYjUOMZzo5sGo9FqW9pSXSNG8h50aV2dEwF66AXooAE7XHgAXKEfOkmhbX6VUzsqCV5rSUBLFlYB-Pojwefn9Hbx9O0m5-YyZIISqAYAUkOvZ4m_bCxy1QuQqYIevfqYYz512gYjQbLiLXO0540jgDl1c0-B9rLmDN8hpSnvS0pcYxEWyiquXVRGy_ehWN67RChc1QCwLT9begVccRfg27tIHVyFdqfQOr30pRG3jQH0jzETt9fDufMXuw6bKDSsyg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6abfbbf23d.mp4?token=nqgikrizUOQ-J-0DJ6mQTpfmi8_25dlB87syblwhRyWKHwBs9nKyKeJ0U4iPY3FeBVpCPgYifIXE6Ls-gElZkYjUOMZzo5sGo9FqW9pSXSNG8h50aV2dEwF66AXooAE7XHgAXKEfOkmhbX6VUzsqCV5rSUBLFlYB-Pojwefn9Hbx9O0m5-YyZIISqAYAUkOvZ4m_bCxy1QuQqYIevfqYYz512gYjQbLiLXO0540jgDl1c0-B9rLmDN8hpSnvS0pcYxEWyiquXVRGy_ehWN67RChc1QCwLT9begVccRfg27tIHVyFdqfQOr30pRG3jQH0jzETt9fDufMXuw6bKDSsyg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
بجامانده از دیدار شب‌گذشته فولاد
🆚
استقلال؛ برخورد سرد رامین با یاسر آسانی و صالح حردانی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50K · <a href="https://t.me/persiana_Soccer/28649" target="_blank">📅 09:18 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28648">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NC7G-L6Ttqgkbq2HlTPnwmg72dU6OoAUIAly782BUDho4M533sH9V6QkWco-xqO79aNDFfwUC_rHuJGdKL1QzLpwmpO0KaJV_Z-_VEHeso9JxUWzb8Esg0GGeXmrJ1rZ5etGDC1Ay4gsD8lmMsMaWOdVKKkvNwEOwShDnma9f9Nq5KKqqJfFReCiVTeheXs4ableHfDNBk1I57JNdYKZ9kJFMLoQxci7dH4-749IV4r5lBKJBCQI1jKR6Z_GshaL7LhOKEKeLeVQ5s47LALqR5Ej_dxiduJBnDUfH9LX0_C2vEoAj6eGlr3XtqJcIFWGUvF6ZNJ3EXbOzmFd2Fw6jg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
شماتیک ترکیب احتمالی پرسپولیس برای دیدار امروز مقابل ملوان انزلی در هفته چهارم لیگ برتر.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.5K · <a href="https://t.me/persiana_Soccer/28648" target="_blank">📅 01:45 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28646">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XRpMZGeSY_gyVj82YAT-dHRlWVY1wuUowtvfZyE6s8nt0rUQPYckadndr3jWO15_b1qno2H8AYklpRV7RUTFqp4y2HWdmSXFrvk9dGLXIaWdSQudYVYIqDk2B9t5b8J3yy3v8ivwKWYol88kBByUxkVHdLLSgs9LieVaVWpUD__ZCIJEt7c0U5tqRUvovLgvCZKW_xpcoI4p78jaVCjSutxayCm0EnUYFkuQAX_HdKs-OPscuu3ruKXJwj2qBYswksKMpLKKJYNMAR8CcOgeODDDdI7adL5f6QWrhnccsNTb0ChdWVVsETbhyhORJSXuViGTUVagAoV2S_W7syZtzQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌‌ دیدارها‌ی‌‌‌ امروز؛
مصاف پرسپولیس برابر انزلی‌چی‌ها و دوئل تاتنهام با شاگردان ماتیاس یایسله
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.3K · <a href="https://t.me/persiana_Soccer/28646" target="_blank">📅 00:47 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28645">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oEPzhq6OKBo3a3hi077DTiyN-1SEQOSloQdc1Y3wZ9gbBLmpJnWJ5reKBEjhuSttpVNIIaYuoum5D5l8UFfIxEjvtxj1Pe0iB5cEsrJrNUZAslPBC91WKE4-hCuk51_HtR7bH8D7-SANICi5FPD4SHsr23ZB04HSTJxytU1WkQyewmDRYeFFoO-lhpNxBl0imPpLFnQeprY6m0_MDWYt3M2Sf9To8OXcRKuCXhK5HDkVck2JVIu7-SpDnA3bywxkHbeuDeaRY8juRokkzE2ECfZUluqnZ62x1hZ_HhGq0s8m3jVjoXoRjZgNQgCkMb-TArLNFS3EKPWTYSvzL3idSA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج‌‌‌دیدارهای‌‌‌دیروز؛
ازتساوی‌بدون‌گل استقلال و فولاد تا برد پرگل‌بایرن‌مونیخ و من‌سیتی مقابل رقبا
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.5K · <a href="https://t.me/persiana_Soccer/28645" target="_blank">📅 00:47 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28644">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/D8liOPhALxuMaf2PMeC9ryAcqYVoSUlDAV0FH4UVc1XVRyA-_f85rogLHQBc-AyoSbWaC4Gz1h7h5thTB2qCHjoRxONOETRWsTYSxy360ihHsORRvNRWled47iYnTDqbBUe7FsZLjOOz7Os-pa-9AYP1s49tL8q10SYxVTaLeJCZvkBldKUpIVXldGkU0taKiBN_N8GDRHFrSYmmZWb1k-V-35J2bygn-VHVedFllyADdmDjHx4ljJFAqyt5WM7MxqA5NClama80pWgk-jTfDMyBjj18_BahbUzSw-_QvVbx2dWsI_G5HuZ74oF-dQpUXgPNHLMbMhv0W_BabIcCWQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
👤
تیم سپاهان در هفته چهارم لیگ برتر؛ با دبل دیدنی کسری طاهری 2 بر 0 از سد گل گلر گذشت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58K · <a href="https://t.me/persiana_Soccer/28644" target="_blank">📅 23:53 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28642">
<div class="tg-post-header">📌 پیام #69</div>
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
<div class="tg-footer">👁️ 57.9K · <a href="https://t.me/persiana_Soccer/28642" target="_blank">📅 23:08 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28641">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aOIvlNmMLZJI5Pft4gO98ZbVNCtBgPc0nFQ-C7kZ_sgHKKDdzyh_gt05IYhnzBOJk_n79OmA9K847_NSCP7-33m80rjPMNHCezPhuF7mtkbtoF-OHzCDxz2cv_bWa2OiZZBH7JHRke7TNyzTlhEQsff4xhmGPQ7X4rcnPriN5ZQksw-CpPbiSP3mVdtxrXI1xvelUGakssA98YsjFYIBbeTxLtgGjyaYlUy65is3pcpdziS23qjHtJjx68OsHEL9AmBnl3OuUPm3oonRisq2rOg5Gk5FOB5_LwhzdFD6rwWH2gRvvvPSUimqm2LK9vnKoeq2DRxB9V5rALBLYdYv0A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
آمارنیمه‌اول دیدار امشب‌دوتیم‌استقلال
🆚
فولاد خوزستان در هفته چهارم رقابت های لیگ برتر.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.2K · <a href="https://t.me/persiana_Soccer/28641" target="_blank">📅 23:01 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28640">
<div class="tg-post-header">📌 پیام #67</div>
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
<div class="tg-footer">👁️ 57.7K · <a href="https://t.me/persiana_Soccer/28640" target="_blank">📅 22:47 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28639">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ge6eHv9hAVMJI58dmRt8KtSV_c-izZijGH2YWTtjredgK0ZPkZ43BIZ32V-LU-qcn8GkCC3t1zTsC12ABOuE3W0KWn3rhXFlj9PsIXNNZplce9-QTy_qUQ6yEnPsRA01BU6_xbRLOxTVYSaYW9auWa0K2tXRd2CE1Kd4mWcVVwvC2KgxlVeWQoyD_45DFrzCYnCjyXZg__gJkCWZy2SxrndDbWF7SIWPXYdVGMhJlKy7yriyY6Z2FQ4gAd00YL9Ff0XEtQFPAlIAlHWeYCbVv4C7Tjvd0NAeeOUdiBAqSVKwkfo-6zNc6rHkN19yBB7TJyZs6O__vdViPZap8fwZXA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
شماتیک‌ترکیب‌استقلال برای دیدار حساس امشب مقابل فولاد خوزستان؛ ساعت 21:00 از شبکه سه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.4K · <a href="https://t.me/persiana_Soccer/28639" target="_blank">📅 21:56 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28637">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QNuv91RMr_onBlCGXDgup8azDNsRbAugMZ22bVarseUBUjMEP1sB-1qriMCh4hpMQZei3w8DTxtTe6kv3ziA9mBLxaVKBlSH3ciKCjO4RJw-Kv8kNLYE-FOk79vdjEfpTXmeYM7P4EkoHjRQTQW0Apcgjif6dSChNqdRWrD_9-Z9rIr9MiJqgYMkrseFc2Zma1QzG8D1pfC3A3CNLHjoIJRtL3KSRdVVfQeDIATO6xQIWH8UX-XMFJraRoLdDekjM1P8XMGk6bHexLs_SLcfl_O4QXG7dOqskpJ_-u3XHgzDv-6p--kX1Iphk4AghHXwz50cdWFG5skyCrGU4yEGSQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
👤
تیم سپاهان در هفته چهارم لیگ برتر؛ با دبل دیدنی کسری طاهری 2 بر 0 از سد گل گلر گذشت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.7K · <a href="https://t.me/persiana_Soccer/28637" target="_blank">📅 21:49 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28636">
<div class="tg-post-header">📌 پیام #64</div>
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
<div class="tg-footer">👁️ 57.9K · <a href="https://t.me/persiana_Soccer/28636" target="_blank">📅 20:50 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28635">
<div class="tg-post-header">📌 پیام #63</div>
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
<div class="tg-footer">👁️ 59.1K · <a href="https://t.me/persiana_Soccer/28635" target="_blank">📅 20:40 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28634">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/L9Rbq_Nmd6JvZlb5-6abjJu-SS9hVW2AU4Rw4LLOtg7nSdJJoYZU9hTan7C5HteMHDfSzZxGj84rC5IXvSwDN7TQ_AN7yg7BxfSoqp-eBwZzC68apIEXY1NDlQEkFxe1Lj8X_-acILM2PQ1PJt4wBcaeMrQ9T3tMdli2z6MVESNG1R4f4R3MZFmzlV2I0g2O3nILgn7YYpsP3ZxnjtRAbzkE_4N5PB1wSoKuBd3eoDgSMrBPDkkfo6yH-6_R2lSM38L2Rg820QSuBbxkWR7OcFtJzWZJHuQdWrOHsgGXXB4kQTgWSx6KzFO5XZHwZEfuV0YlSSzYgAgAeq-A1rhNrg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هفته چهارم لیگ برتر؛ ترکیب دو تیم فولاد - استقلال برای دیدار امشب؛ ساعت 21:00
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.5K · <a href="https://t.me/persiana_Soccer/28634" target="_blank">📅 20:21 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28632">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/XoJ7HBQODNfoDTVzQW5Xk-RoNa-qV85-PYuMVY1GzbtJ5OBm5lAeQnq0y7KVrqEeoluwcO4YAU8v_Xoh8GIXA_bbv0p74vmOd3Xgc65R1VnToBo50OYmJusvsucsVM2H3nbd1jbgs_o4D9O4vMbU7bcgOuFaAurtaoHM4nlO1kpCnk17AYDY6GCjl6Lkv1WKsc5a4NJw2TCjTYTn34V3kS7Wxpz27QA2884i7Rk3MLfP41VWIX5mrZ-iZWnIlN8JvKq1ATYhNK9Ucp10qGmHTTtNhTvyCE_0htLpcXoVUvr_DmaONgebbMDfva1CjywZeUtUoVP8OfKKJwNJ1SIs9A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/bTdQm4M1s28nfxL-OwZjcNJVFTloU3FEZ007w4nSks9H2meCzI3FpeEnk1PU3-XEfk7d0VPQ3jDgboNRhI5SeRh_AsYmrOQCkZ-IfZs5FWibybWBiezhXtqIan29Y2JxuDKyzmS3AULzzaH9aFdzsg9F13FgnrGk1NweGsORa95meTd_9t32zIbO8i_9mLfpGGcu847P1cacmGWI4SHSE5qmPLAGKl0TLJKNwNFYQLXsnsOyySdiARRrijHMe4AgkamUtpxL8u9hYi0itSibJ9BkXKK4-2BuZLXoKdffKTM9BmeeFVJUvGX2b6dVsyMPF_vSMjek-B6tyNGOxLAWlg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">هفته چهارم لیگ برتر؛ ترکیب دو تیم فولاد - استقلال برای دیدار امشب؛ ساعت 21:00
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.9K · <a href="https://t.me/persiana_Soccer/28632" target="_blank">📅 20:18 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28631">
<div class="tg-post-header">📌 پیام #60</div>
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
<div class="tg-footer">👁️ 57.9K · <a href="https://t.me/persiana_Soccer/28631" target="_blank">📅 19:44 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28630">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b1bdc45bb6.mp4?token=Ldh91svvHWNkYhIgoE1v44Ru24WYa2AbyHIaANyCzxgD0bmE4Ow2TL1DYlZQ-f0wfEnFmatT8OKGVgmnGOh8qC9lRAwxWStpPyC6eNqaLc9ASkuh1glehub9txezMZpQV7Z7pZuVlZs_AnKrfZfq2snJvIgxdcb3pKl8JQqnF4UhYORYo-7-m5-A_cj-luuFG8zaNk41v_sKRZT-oCKwu2gQx4d9blSeF7h318DaXLjD72FgKbMOaIe6JHj_shdQyQMUSC7EJUsE8OLTC9Rmx2lUdXX4botqnz_wmYTWS53LwyGf7n_u_dq67BAh16D43jwuvn08gPxwv6JoCblZ-Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b1bdc45bb6.mp4?token=Ldh91svvHWNkYhIgoE1v44Ru24WYa2AbyHIaANyCzxgD0bmE4Ow2TL1DYlZQ-f0wfEnFmatT8OKGVgmnGOh8qC9lRAwxWStpPyC6eNqaLc9ASkuh1glehub9txezMZpQV7Z7pZuVlZs_AnKrfZfq2snJvIgxdcb3pKl8JQqnF4UhYORYo-7-m5-A_cj-luuFG8zaNk41v_sKRZT-oCKwu2gQx4d9blSeF7h318DaXLjD72FgKbMOaIe6JHj_shdQyQMUSC7EJUsE8OLTC9Rmx2lUdXX4botqnz_wmYTWS53LwyGf7n_u_dq67BAh16D43jwuvn08gPxwv6JoCblZ-Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🟡
👤
گلزنی احمد نوراللهی برای اتحاد کلبا در دیدار امشب مقابل اف سی یونایتد دبی در لیگ امارات
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.7K · <a href="https://t.me/persiana_Soccer/28630" target="_blank">📅 19:32 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28629">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hq6giDJPZE1JIRDKr-EG9XCGuNnM8PxRI3UCwgroi2LsllZvOX94TNY0thXy3_iDrsiR4HQfOdUW44EDosyr251GKfjHpyQWdPYtGaO8fSSFDL2lLfRjy8t03llywc2f1rtXeibcubTpItVwPzyB9sJJp2p-COMbRXeFJoA_zm3kOLicsmics9S8RwVlAwesurM5iHYYUXVa0eIZ5gH74nDdXmexGv_V05fx5WdNxYieU49O22sEy10npfuZGgVKNE09Xxd1ESCb1Bu1tQtPy2LATjKnnGcX2_wk2K5oQhBSEawPG_6bEMoKrLKJrMaFrDrHIdPIHrwXkTmVY0Ysvg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
هفته‌چهارم لیگ برتر
؛ ترکیب سپاهان برای دیدار با گل گهر سیرجان؛ ساعت 19:30 از شبکه ورزش.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.5K · <a href="https://t.me/persiana_Soccer/28629" target="_blank">📅 18:47 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28628">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NfvhOBhidE3IZkddPnA9xQ0ibhzpC8A6mOdn9b640VtBut9ogXdGompNqFupzCR4mjjSeXwMWDH-csMFYfbK6JNZzfdPbYqGKKrRKSE3LmprnzQcjJ1dkmmEQxtX9tKUD7idq6o42wk3XyhlZLUqrvYROGjZahINZY4EAxS6tIlmZZqqhc8aPgB8DqA7Pwl7VZK_A_gZ_VXdpexgv5FveeViW9coQ-pBobBHeJAqr7Sj21ictnSUFXh86Phn594J9NSiOa7VlHAJvtDIMMbyUgrTsZEN6PLg5JRl_bLBQi4zZ_OdVq7k7acISPNGdWnZtQylfdyeatqBSbQkieFQqw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
هفته چهارم لیگ برتر؛
شماتیک ترکیب تراکتور برای دیدار مقابل چادرملو اردکان؛ ساعت 19:00
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.8K · <a href="https://t.me/persiana_Soccer/28628" target="_blank">📅 18:20 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28627">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/unkVLk9OtyHpRn0_2m3dzHfT2HFmRplKZ-voztg3lbp1xH1X1prXHZRTR5U3oFg2QG2YRvhi8UUeQzUeHFephd_DgpN4vYVWQOiuEWlqvyIuxlXa7uXxhtVSjZvJQdPCAjNYa0_z1aGE62fqr8uI1ZnqmJ4b2CfyvCcFQNVxPAVkAVkrf1s-y7CmKXI10iEQ-xNHk1N3Josr5YWPRZj3cMSqDYA4xOWhrbuSkDoiGRCd6zlWeC2mhp1YKanuZKNtAQ-ss_AD4BkH8vH5f4uVMDQhz2qZL1ObiTilVjro2fjUrB2QFGxoE9-RcS6Vq2379GFdezyV4lnml_hYrbjPqg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
لخ پوزنان لهستان با الهیار صیادمنش و علی قلی‌ زاده در لیگ اروپا مقابل تیم‌های مطرحی مثل لورکوزن، بنفیکا، ساندرلند و کریستال پالاس بازی میکنه. فرصت بزرگ برای الهیار صیادمنش که کریر فوتبالیش رو یه قدم ببره جلوتر.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57K · <a href="https://t.me/persiana_Soccer/28627" target="_blank">📅 17:46 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28626">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eRB8k32AOpfHyTB1-HmRxH9WoPgRdOG9lLNtP6FEw_j4m1ECMfl4p_ZHe8WVOvAPLcipdfZdiuC7wT54pgyMZFVGKbox0uTYXvnHWM0Y3hQdI1JVFPzk9aprKTgvcUAjbtHjCLiN_xFtiSfzo_4X0uRKhe9PQr7nnNUTvBJZgXGRh9BJm7TSTE_7cQiz6dUA7UugaX-JZyPbewHD_-nm4agxlAwVqUnaWcJjhRfFlaar8BxI2SiTMhfTHD2BTt1mwIJ7hA1XvoJ7J1AfF2HMsPL9Acz_CXDSg-yjwhR9IB7oTVX69pwpPO19udLtzh8SHyQUVWN_Qskm2uNDFNUVMw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
ترکیب احتمالی استقلال برای دیدار فردا مقابل فولاد خوزستان در هفته چهارم رقابت‌های لیگ برتر.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.8K · <a href="https://t.me/persiana_Soccer/28626" target="_blank">📅 17:15 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28625">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BwxtVDDJ2uVBu532gaYRXbx_DqQIwaGZpPXO0-5KnfcNOmQr60NSNVnkrXym1XPK4-ZTCmtG7NCbtHw1sAwrGEGXTzJs1uqOE7-605Icef09rP54riF0LE1cZ5Rr7vaZTb6h5LrztO7cTSH_u5wbh1hjis332qJ5ImHND4uC-z-BzYXoWWzMnKe6z17Oku0bDd6cIWUgv95l3LbHStwOVTLVgMaGEWuA-IS75my-6F-lPdKMy92VjbY1tWzxnT-Jiu-gSveFrGLI4vqCr95gW3wh9-WwrnexIuBH_ag-ndfX0T8wV9IS0tgvmBQy4xkbCKs4M_DoYBr-2IW3XX1pZw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
خبرنگارمعروف‌شبکه SPORT اسپانیا که معتقده که امسال بارسای هانسی فلیک قهرمان UCL میشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.4K · <a href="https://t.me/persiana_Soccer/28625" target="_blank">📅 16:55 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28624">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IyNOp9iY9Nu1t1Qsk4GIFktFf7xbzQUTghmKJV0Ge3PZWeHbJlFNpcNdtdQRDBkuxhw_VRyCqYCRnQIwR6nn7hASJ_N1gGaWPfTIEzPws5UjOOo6_UbvVjIRdc0r5HjLAoTvz8h1fqcsUaeVnCwEqtzggFEOYMQaRtUng2BfMX0ugUN3yB7XwYipJioZH589VPr_qUFfW06CLY87dbvpVYBnCM0gypgx9_npIrPj0qzsGqE4HttFIQ9KEZHebtqJLt2AuQRBPknB--Gyctr5RMo-ZhLNR4NUQLQHoLsuUXzIS6NCPlMzyldfhcAAgpQRP1GvUxfbJJe6dVR0H9x6sw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
خبرنگاره از تارتار پرسید و گفت چرا اورونوف و سرگیف بازی‌نکردند؟ تارتار برگشت‌گفت به دلایل فنی بوده و حتما یچیزی‌ میدونستم‌که بهشون بازی ندادم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.6K · <a href="https://t.me/persiana_Soccer/28624" target="_blank">📅 16:38 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28622">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Z09kPpvXm8p6nsrJZBAAdLZs9Ge4tD8-njBCx8Aj_jY2GeEQ_Zj1w6zq1ZnX1PAawgkKIQ0Ays4K--6Ndmsh69FL5dJLWhQlrrhLIW8zdL6x6AhNFYwhopjUxCipIyQCDk1Qla-cb3_WZ1BS6ctJFyH_h__0ubuU5QLGeWXzCF-XZIuM_P_iYAdURf9Ub-5sE-gWSxNWqkGJF1H24nvH1QtFWNT_e-apkOaf0HdqjDS8_y9txhHL-jN-oAXd52xYcr2c0dXQT39rirbzVpcCkGF44EBMuoT_A6BZOuPmeo8O7_PmebAqH87P6kwoH3xEyx_ouHQmhaikSkknN9ZSXw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/CTMlTl9wGfP7-fJP0tv8BgJYPqkb4z4oG0z5zsLfoN50QmJGR1Tg-x3Pj9NjT-Q5wnunFuSN7GxxVWtAtDzRChjUmpMR0jnqMkY3Q-auH4iH7QpQeJZirl7V55w9J6XiFQ9q8iOudq1DCFw-KHfWY2TioJDqGRG-vsqgXSMCiunRvjN05f-K8ey_WF8mTcb8Eo3gx_DAIy18z163JBy37fSbrHy6_jYJ4raz7IbCqbZYaDachGYhrFjbdnWI_sxDi2ZhIhrJb96DrNvJNLs5QP8gjsUnll-DhBIUo8_SPoemtQrK3nd2o3iLVboGnqA9gj4jINKq8jQdRIEIac7jWQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🟡
خبرنگارباشگاه‌الوصل:ازپیوستن‌مهدی طارمی به الوصل خوشحالم. او میتونه به خط حمله تیممون در این فصل کمک کنه. بزودی با او مصاحبه میکنم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.9K · <a href="https://t.me/persiana_Soccer/28622" target="_blank">📅 15:52 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28620">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TL2Nvlfg1KvD38oacXWSXjWfHEQURLDWgBLnmqWjz3u-GQqRhkCvA3e1DpqMDR3KcYn6MZK0YfE1Ksi8DybZw9OQWKLi9jijIy1e5IaSKiPVcBQ-Cmpyo08tlVZjntQN1yyaWu8dEHDg3n4F7eeDaQGasJKaAGDP3bo1DxlPfQo-7BSvpYHCrpNyNtfk4FBBHIl7szKkF0NtXVBIFhcTZFZEgt9meqZg4QLzZLpPV4RAlemPYhHIipPBrIS-0jyCS44u3muopcoYL0pQypOAoXLTyWS5u2A6bvREsISWzJIMItRgEEyvOTJnz4ID5NCOhN5yY02n8rVTUWxsMZHheQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
عملکرد خیره کننده کیلیان امباپه، وینیسیوس جونیور و جود بلینگهام درکل دوران حرفه ایشون!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.7K · <a href="https://t.me/persiana_Soccer/28620" target="_blank">📅 15:07 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28619">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dojPIYoNJT2CeE6bYqdouNqze2povjY50BouFpXDSc11UOvIxf5YQBATvvNQLqD5BcRpfKMErM8tS9enA7GLNm3mXULzoxCe2VFNCX08yCm2P2kMObFyNEurLvzF9GGrw1lJbUdwpUF7u-Em4BfzpmtIu17guUqS6Mh7bLVpcYenBdQV5ohcNxj-NuHcIvTWBG2IacSsVTtob2jIuT4EEtwNWYkOEJyRi15owaA2p_9TlJr8bEmnQd_uqLbjzLqRSr1A1jJrcb1_l6gWsFW9QcCh1ZuY5nScg441iML3tyzxTPQ8lpyQxN7rzu8Oz2on5XiONyTcgj6a4bzbizPu8g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
کامبک دیوانه‌وار تیم ساپینتو در مقدماتی لیگ اروپا؛ پافوس باهدایت‌ریکاردو ساپینتو شکست 2-0 دیدار رفت مقابل هایدوک اشپلیت را جبران کرد و با پیروزی 4-0 در مسابقه برگشت، به دور سوم مرحله مقدماتی رقابت‌های فصل‌آتی لیگ‌اروپا صعود کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.9K · <a href="https://t.me/persiana_Soccer/28619" target="_blank">📅 14:44 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28618">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/B4q2d6LmfU9gsoJD7v6-lUE85e1G8H76v67o1FoK2Uaw4fi45x-Or64CKC4iEu3Y1B-zZa7bHr0QS7qgNntufmhCSPF1Etg_dVaZUbL3G_cnn8chGG5MXuwINHiFWoVF2qWtgPUf0ahUozlbats3CtJdejNlfULnk0gX4n4iSqb7H2hqV3GF0K771DOnRAI2cLvrZN7ib3E6ADXVCuaeDuT60TCQW9jxv4sWinHtoUwZpp56l9s2LewPkTDq3PkycMBFhHfhlckOxsYzCrSCriMCwpqcl74AHMyIT6CxxKknyj5DhG6jrMZVPmlXtfXSwbfG28H4TPRPkpU3oQRPvQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🔴
کادرپزشکی‌باشگاه پرسپولیس و استقلال در تلاش هستند که ابوالفضل جلالی و مهران احمدی به مسابقه شهرآوردپایتخت برسونند. 48 ساعت قبل از بازی مشخص خواهد شد به‌بازی‌رسیده‌اند یا که خیر.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58K · <a href="https://t.me/persiana_Soccer/28618" target="_blank">📅 14:18 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28617">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qItbLDqBjQkD3DnUf2P6iMJMRRA3aJge5gDI323CrZ3SLUjKH0sfMx9mtuSeDnF7bZOnzw8e7cqSpKH1iQFpc9jQEgVl-kqOnDCt8Gt5q4DpXzTSMwet3HaNwDz717FuBjwNVMfJswRJDn4i7IKyzEx_33ovBzfenMiOuCBrjLRn3AzeOteAOGJKRemb9sSyWNFa5W9Lc1ISNeKzh2F4OWPoCI1p-6Gy_tu8irvq1rJEgfS-HlpQx2aDtcQ4iH9AATepFGxnTVLIOUgZRIEMlA-0_WluuYury7N9bT-2gQCQm-OPoDIikb8X2vGDmU_XaQYDFd1bzgMi6DM-3IPjCg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
انتشار تیزر رسمی سریال کمدی «مرد سه‌ هزار چهره»؛ آغاز پخش از جمعه ۱۳ شهریور از شبکه سه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.3K · <a href="https://t.me/persiana_Soccer/28617" target="_blank">📅 13:59 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28616">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pGM-cETD8X35r_5-pIomHufEV3y5UMnI0GwLqBR5FLxtS9MXlEHujqDyeYN0IrrMZlgD6oSrnydOp971dc4k76ARQaD8asBYq0RENpZaDJrTySrITUSifjsbnhKh8R5QAB2s8fKBVX349pApEhMv98HWgzyrn9I1aJVoz_Jp9Gxw0oVikw2qsOSkw9N_cf3ONWnuyB2_uwz_7rF0H1gKGnxg-2xe0Mqqf_-UoYhdGmCoExJmSSPr5vRZoquwAI3kPYzkyXRkJZ8U6AHb0rvKhvFgKkWUAVszgznPWbmRdYFqxjXnMddPIEaFATdK3b0mN2swRDCdDuizxC9jhiPeNg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
واکنش خولیان‌آلوارز به بیانیه اتلتیکو: حتی اگه بدون‌تیم هم بمونم در تمرینات اتلتیکو شرکت نمیکنم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.1K · <a href="https://t.me/persiana_Soccer/28616" target="_blank">📅 13:23 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28615">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/k2mtUsWZ59RsWMxC3pZ50knB75Z_SiCO6RaQie_emXszsch3tgArLUhPAcU3sRA98HgDrLOIELYjuQOTXQIm53D5lJ0v6EzHsWfeLU6vBReDuLCW9maHGCn5HmxI6wEt76zUGxqKtvzRAXqN7OX6FQ1e9TIlxlVttDsLR60GHPXkJ18QnJKb0AUZjowOsGtHxiE8ezX3xFmiL22pUrOkwproS0JD6ovIFqU3mSdMj_dHnb_-bAyrE337OEvCnnYeyw0XbYBMia2ctHO02XKOtYko-wNLH6YbePXlHHlfHGOIejjRk1IdsgZQS295lOiGzVWwcVGQdA5dcz2tvdPfyw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
باشگاه‌تراکتوربدرخواست نکونام با عزیز گانیف هافبک دفاعی ملی پوش سابق البطائح امارات وارد مذاکره شده تا درصورت توافق نهایی با او قرار داد امضا کرد‌. گانیف در حال حاضر بازیکن آزاد بشمار می‌اید و مشکلی برای پیوستن به تراکتور ندارد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.3K · <a href="https://t.me/persiana_Soccer/28615" target="_blank">📅 12:41 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28614">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XbV2AGFsPKuqTtcftAxct4ZP_ZWzcvl7v3ZAyEAt87qWue6UIerCJtHoQ6llZyT-NYI5o7yypcqQ1xB2gCvRqEXKnuSuN3cvMRUJ_N95wBCp88YB1uba1BX3tcAvXQIhVZKkiIq5qh_WpOM67Dq9uE-lW6GPEOjmxPGiNSL80mzad-OnakinTLGBJlK_Y7c0IbEWa1LrSosg-T2Eag1CV6o11bqHJunULWUyuaC39NM_84S3clnTjBITuXhklfyj4U6VJT_7iPLLpiN5do3PhyIOLCWSF4zxjUOENB7CRWRrYuXIipfV447MbQjyhMIWp6s0z5uKXNy0ncmUjH-GmA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
بااعلام‌پیمان‌حدادی‌مدیرعامل پرسپولیس؛ پرونده نقل و انتقالات سرخپوشان در این پنجره بسته شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.6K · <a href="https://t.me/persiana_Soccer/28614" target="_blank">📅 12:25 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28613">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RvCCfWaki7DMGHoU_YGoTI-XNZsyeLoYcjnDZiAh9JG9wPTBWtl7imaOTFrGyCf-fDOowsGNTjTiZcCGQn65o5ItA0m3PgkXPFeg3YchD8XhX3nW9e8xGQzTO6tWLgtppgkzGqoTPEYGRqtd3jtFwsG7amlVRqpx6RkTVIcquRCFircoIovoKUNt8vtgIW5AnPQqj9kbPEO_SlJqIQ0TuS52LBe3lMCTPjyciHcJ8izorSa2Iq679XNOUXgh2jShrs6Js3rfIPlTU8hAjfAsqiru9esTeb3FE5_9iauQh88Eq8D0EQaR_fhYpOZwqPYYP-QNnqpMvfpn7Dgp2sZKCw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📱
استوری دردناک محمد فرهنگ یکی از عکاسان زحمت‌کش فوتبال‌ایران: دلار شده 204 هزار تومان! الان من‌چطوری اعتراض‌کنم که بهم انگ وطن فروش نزنن و از کار هم بیکارم نکنن. خداوکیلی دیگه خسته شدیم از بس دویدیم و تهش هم هیچی نشد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.7K · <a href="https://t.me/persiana_Soccer/28613" target="_blank">📅 11:46 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28612">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/G5ngFIT1yN-k7aE_GSfGz2gZ5PIbs1xMeACuDIMAcvNu7a_iP51gmW4yFPJhvWPze2Z05PFNu0nO0v7QfxR6pBWg0b8kkSc0Od6H7_Fq7OZToU9z1QDw3ppD4Ao-Wnh8rDnSS8Rk77lbNdknIxsYIxBdy1QUH9vN_pJ8Jt6A6Nm0A6LkQ9B92rHfru_ck8tB-JW9Gb_ryclHd2qQSH7fCtEaK00ZqE7-Fu140NmFkE0GOAWDHn_r9oSzWs8fmUQ8p6KS2ikzRDZJvoVHtMbf15FjHl4xehybtfOCzXPoumzDdmAwbEoIIpFc4ODWnU3P15M0wPnzRJSsVzpp9A-hKA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
👤
#اختصاصی‌پرشیانا #تکمیلی؛باتوجه به‌ سوالات‌زیادی‌که پرسیدین؛ بعداز پیگیری‌های دقیق از مدیربرنامه یاسر آسانی بااطمینان‌ کامل اعلام میکنیم که‌فسخ‌ قرارداد یاسر آسانی درسامانه فیفا ثبت نشده و تنها یک نوتیس برای باشگاه‌استقلال فرستاده بود و هیچ‌مشکلی برای همراهی…</div>
<div class="tg-footer">👁️ 59.1K · <a href="https://t.me/persiana_Soccer/28612" target="_blank">📅 11:20 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28611">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/B9mQ5woxu2ryvJTW3CLmyUKbo7z3n7Y1Hu1RZAQPQFPzYDFUn4Xw2WlFXFFdzhA4w7p8hvRG-hvWsNNPT3QGkzW68bp6MQNLhhokcTjJGOQPEpPOHCaMJmuj4R20_fUS5rzDAIjH5tm6GSSFPhWTcmJd4chg-vQaL9sfzdqJsLy1AKSFzedy6-4BCJ27-kywyNXQOs4SJ7cUZgg9H5HOHi6p7Ex5JRTGkQaTXoak02IkD7oohFjDaP-oUJ0oM3_DZ0O7EzvTdE7DofezPe5fF3jtmTxsXfl9EbnpkqqbgWkg6YeSG5_xtBYbd5AI061476lcsOs6DE5NTqBrEdDadQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
وزیر ارتباطات: پرونده فیلترینگ باید در کشور بسته شود. بزودی‌بادستور رئیس جمهوری فیلترینگ فضای‌مجازی برداشته خواهدشد و تموم پلتفرم‌های فضای مجازی بدون فیلتر در دسترس خواهند بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.6K · <a href="https://t.me/persiana_Soccer/28611" target="_blank">📅 10:51 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28610">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dCzPFN9o_xhDvpSGZ7pRtnEeLej6tnVfSUp6GNREf1U7WlK1bDNT_G7p2hlilPJXfIbaoRX_bpsv9haT20snNhSzCuiIPHDh08AtAwbpVtCrqdNPafFUIHkwIMyb5XIzjQWhoMGX-0PaGw9KqM1CGzWpD0Xy85koWg-GrrZpbOma4FnNNdmxO-CVjHuCT6RLlXEPs-UaFoarAeI7fTvHZsvY-WYGDSOlbvth5ENxf-JZTwGl8xVCIgVGnE-hhdyUsfnLAv56rzncb5_X5nkEkIn4dilmgk_7bGOAlaeFxSLf0qZMj7tYZa9kaDNWiYjgqcCfqEJ6JN3-5n9JymA7kg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
🇩🇪
‌اسپورت‌ امارات: باشگاه الوصل بعداز جذب مهدی طارمی و ریاض محرز در آستانه عقد قراردادی دوساله با مارکو رویس ستاره 37 ساله سابق‌ بورسیا دورتموند قرارگرفته و پیشنهادی دوساله به‌ارزش 10 میلیون یور به اسطوره دورتموندی ها داده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.3K · <a href="https://t.me/persiana_Soccer/28610" target="_blank">📅 10:51 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28608">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sdpWXpZzDJWf7rgsq1nJjHXy-U--fi_0BO0e54RAJT-9GCCkFVXb13kMRkEr8-x51JbmC0T5YFRts8nNvWf6GXojJD42L_YUy-jvADpySXxYgHTrbfv9wWAJLAXiZ5IFp9lPK2QWJWRzWIJydvFbHK5_uXWdDl-bQjOrB1_C7mQreGF241lfG2LZhmXTp0WAarQdDbS5n4DTCK-CgCzWRR1TmHPegiKV_alZZYoiVgSzu6Oc_vIIuDzw9Z0tQtQ6ZdlHhjr0jaM7JmryMbiEIxUt2inPDWByomKwfQxT5rKUFSXLKrPb4htW4glwHCK3LbD7hW7V4AYohDWzMFVP0w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛ با اعلام باشگاه تاتنهام؛ عمر مرموش ستاره مصری منچسترسیتی با عقد قراردادی قرضی تا پایان فصل همراه با بند خرید دائمی به ارزش 50 میلیون‌یورو به‌این تیم پیوست و شاگرد دزربی شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56K · <a href="https://t.me/persiana_Soccer/28608" target="_blank">📅 10:09 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28607">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NVvwo1SI1ZEch8VaEUyDCPuHwc2tYrDWTg64ewzRETxmLRB5LECsZNfePxjUEFLCdjfI4YyjpfXCGPO5j3LSgU2E3Up_Q9WuP8A23fYMGD4GKAGul1Vk630tpeBO4utQtcVH0SqdU-cCTqmegeY6GGt0iq_vQKgGuP025h1wKqHEO_P8eu51K16xbbE5PiHA5E7-mlYuB3p1KRnYj1UgIJ5UzdkZBCp_ss_xPRWY664eL1pkzcPhsw7se2JPWC464k3NMpvVV4NzwfnIDX8u7ELDFGZNW5-qm7eX9RjvmzYo1ojf7j91oIWZe-UjJAJetR6XHX3VIRrAMCDPDwXIUA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
واکنش خولیان‌آلوارز به بیانیه اتلتیکو: حتی اگه بدون‌تیم هم بمونم در تمرینات اتلتیکو شرکت نمیکنم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.1K · <a href="https://t.me/persiana_Soccer/28607" target="_blank">📅 09:52 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28606">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YWjKFcNv0tkJvF43t2ukbc_Z8B4zzOeRehS6UHMzoALGioOz0Ud8p8mplsYM_zo2VLjLvlQTwjN_-6nhjRs-G4oW2DeKHQTD2Hg8MPidSinw_0fWYgzqcUTYGcj0RsyQDaafkvM83GtxArd3kLVuhgk2HM3T8vPA4iZvjFfx0qY6AgOoedBCSg3v7rXWG_OcljYlqzkso9sMnQ84KBBgnnrKvswYVHYXcAyTPyU1KuNrLEz0bPVWS66S9nAhPTbPOUvQOVmhzCfexNO3iZkMbeeuu-xW8N3bq1VMYaMT2ewZ_eaOnZZDw-9So4PUF2vubk3YcYpcis9--uQrEIrXAA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
دیشب گندوزی بازیکنی که قبلا مارسی بود در جریان بازی‌فنرباغچه و لیون‌حسابی رومخ هوادارای لیون رفت از زمان گرم کردن که فاک نشون میداد تا بعدازسوت‌پایان که اونجوری خوشحالی کرد و دیگه کار به دو سه پارت دعوای سفت و سخت رسید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.3K · <a href="https://t.me/persiana_Soccer/28606" target="_blank">📅 09:30 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28604">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LFrnNN8YCgZtohB2bUqpqafUICRAakyJ2ce0pfOkggsbkNb4FsHOq657RlA-UGxjHixO3zxZJ5sFmvV9cZHRn7eZroVWUYE4UhhBmkAs7av89kYysecoL3qUVhijZ7riU7XQew9P8EhdXoZjF-VWOwzeJGf6UTieHqUVW45d-pE-5GrGH8g7WH_FByzwGMTlNGE2KHaukaoHW63HqTvdtNB6V7LAdQ0zR3YirbJs1MAOFhSZUzd15Ze5fpBvSoij8WfhJTM3kvJvaGKzL32GMVCdhA8Do8gggKoafL11qJaB1yqCO5XbeacnHzbgTFSaOznRfrkDV_s3_IdIYRf-qg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه کامل مرحله گروهی لیگ قهرمانان اروپا در یک نگاه؛ چه بازی‌های جذابی قراره ببینیم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.1K · <a href="https://t.me/persiana_Soccer/28604" target="_blank">📅 09:17 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28603">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b440142175.mp4?token=KLevnv_AKItCstJsHn-UmYtgTfjzZzDiuqmdVMvnytdRNrjpct15HmsWZXmbYZLz65okA_vvyKewWyOlDs9R5gVYhY90MiTc7MY_aJT2wTIyAMNQGNc3YlYSoYAmUCFwuwC2_jjwmWiIOS3YY-xrxIiqHE7btUnghgNoN2iZ5wj8tVYAVPyi87yTLUOQkcv-g4eqAefOg5Stvpr6EmVhE9dS5icE-i0aS3e6qDxRcpJS9V80-UPBjWl9fu4Wat1ghewTmaJIyjyl_YqLK9s0DvTF3jDo4ctvHqNcTAXHIxv9mXZ5uP0bnVlF9OjmSQb6_FVEJTezdrGknDKkmmVHHQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b440142175.mp4?token=KLevnv_AKItCstJsHn-UmYtgTfjzZzDiuqmdVMvnytdRNrjpct15HmsWZXmbYZLz65okA_vvyKewWyOlDs9R5gVYhY90MiTc7MY_aJT2wTIyAMNQGNc3YlYSoYAmUCFwuwC2_jjwmWiIOS3YY-xrxIiqHE7btUnghgNoN2iZ5wj8tVYAVPyi87yTLUOQkcv-g4eqAefOg5Stvpr6EmVhE9dS5icE-i0aS3e6qDxRcpJS9V80-UPBjWl9fu4Wat1ghewTmaJIyjyl_YqLK9s0DvTF3jDo4ctvHqNcTAXHIxv9mXZ5uP0bnVlF9OjmSQb6_FVEJTezdrGknDKkmmVHHQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
پیش‌بینی جالب دیدارهای هفته‌چهارم رقابت‌های لیگ برتر؛ سیوش‌کنیدببینیم چندتاش درست در میاد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.9K · <a href="https://t.me/persiana_Soccer/28603" target="_blank">📅 09:01 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28602">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">🗓
🔴
🔴
#تقویم
؛
15 سال پیش درچنین روزی؛
شاگردان سر الکس فرگوسن در اولترافورد با نتیجه‌ تحقیر آمیز 8 بر 2 تیم آرسنال رو شکست‌ دادند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.1K · <a href="https://t.me/persiana_Soccer/28602" target="_blank">📅 08:24 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28601">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rtdePduFb0gZ2TbT8lvQtQo20dGRxMlqSQhrlBbiFhBtsM_QMQagSfFCGs6qSBYWHKwysdskMuJMXzOOp3if-yNFEuGC0hmvVA0rpHQ66pdRJ3k7JJHSa7SVTFtkCGTLZXAfWBBeuG7TebcQldED2SD3Uo8Bp-gNzHCSPSutzxQXU64U1xSNxitqTQ6KiAuO_1HyBzI49hCtxz9DM9M9F9PuV06ZUd19LtsG03tHKZI_wYMLIZ7oLFZyPslFzZp6gBhvhOx8c2icZdOMQ5NhvTPfYYBMlfeMtWGhlgfOlk8WE_pvZ71yGY2DODbv9N-sBVzp3eXMh8M5vAcP0_awAw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌‌دیدارها‌ی‌‌‌امروز؛
جدال شاگردان سهراب با فولادی‌ها در هفته چهارم و دیدار افتتاحیه فصل جدید بوندسلیگا
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.5K · <a href="https://t.me/persiana_Soccer/28601" target="_blank">📅 01:50 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28600">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uJK1VO0M4QLnEYlLSVWSgJRN08FCj_F_o4CK-8LxbKmwbMXsroRJV1iKcuuZObmLwx6rroBrlDcmnm0wRynapgvm7v1dv8WqzFfodRbObBOJNQUrx-NvH-6ddqjKHDP9ZKcuvBb5aX7j3sd82EBokH9pWj3lzXoWaD4oQVYHDxzL5JxguHcglZ6vt0GYdnRPDoZsWy8dvpFUAy3UWl_Uu9nhX9bdgJPQMu9aciv83S8IlYEsjQ3u_xW9bBVp8PSob8x9CbF-kjmYuwKHzQKVGpzJsLW6LNtzoXD4-QpFrowRWxZq-aou899zdI1G7iae5Kk-lcWOQxnI5yTY5OE30A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج‌‌ دیدارهای‌‌ دیروز؛
برد آبی‌اناری‌ها در اولین تجربه حضور رودری و صعود چلسی با گلزنی ولبک.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.4K · <a href="https://t.me/persiana_Soccer/28600" target="_blank">📅 01:48 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28599">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TAt8lpfxED1PQvIrQgktopJfZ2a563jxeMfsZfSZ2rtxQy96GkJgCuWiIgAl4yAMT2dP4nuvR8WThLZOBguRZAzHsfKVfd5f1f3R35Md51G7PFtnh7GATgRJROytLDrGbk_GFpXImmUjNmYMNsyUSdHObRj-XsDE3hD8QmuD4YJRBMFocn3P_tFJOhrmw9aLECql7XGN53CuZE7yqQBXZU0UlwxdQBO1EJqL9zBgXADNTeMzZ7qM84OIS-Y0C1d_PXi0ZnsuTXMApPmqwfVAyzNk90jZpNAlWccStN4uT5wKDz8yPoQfpYjpj-zvRaC4nGXz9SK-C_P7HgUiXgW_Ew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
هفته‌دوم‌لالیگا|شماتیک‌ترکیب‌بارسلونابرای دیدار حساس امشب مقابل اتلتیک بیلبائو؛ ساعت 22:30
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.8K · <a href="https://t.me/persiana_Soccer/28599" target="_blank">📅 00:42 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28598">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TvtQNRqDlkRO_15IZJw6mwSCzhH4qJWpL2D7l8LyY85GE6Axrc2Tu81LJJK1N72kdEg4H7mPHWehPCGEKo9VemEU680HO_wWQOrtAc2Gx9DRMs_FNeGhIh1i-l5_UoImjtbUyJDGnNxYh4uq8ejENeZLKBCjqLHWvrMTdcSyYDc-H7ZsznBzg3TCbZQdReB-2ftvACCMytOCVAYlHOqGQK8g_rVFo61m0WvKwp7khOVZodIYUczp2Nb__xW6I8cfChPlDiuSPgNbj6cemAhZ2pX1bPBPZ6mHyDUrtP2hRKZip9OwnBk6E5fHdG_QDF8kJsus96MKo9v-M1Crz7c5Sg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
بیشترین گل زده و پاس گل از سال 2020 تا کنون؛
کیلیان‌امباپه‌وکوین‌دیبروینه در صدر جدول.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.2K · <a href="https://t.me/persiana_Soccer/28598" target="_blank">📅 00:31 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28597">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d099f34763.mp4?token=kZsBnLhpTvqO7jIwqb7hrFMiie0eq9DsxG7wKEANw5sjgLJ9RauWlW7QVoi0594RbisrDTTSEUYDxSVJu8JeBumOF-4-pa8npdX0fZi8liI5Cm96DjpnV8mFKJH6MEKeThAogIq4lRkDROGWjkYnWBMMUhYGtgCwitVwJpNE7P6JC34Qw-0JlXL24tUREtzAPRYQ1eOo7ZtrRiwTLO3EX8aTAApvt9BstNlzH9k0MbQHfkgZ5EII1TFPDY9zWvLXpmudPuvroDdG2wXj5pWvBme8onzJCE2D9wR9TWwjhuLJgT0dRvPH8TL5m2LZyYyvc_zn0_ICq6fvFBvPrkIkig" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d099f34763.mp4?token=kZsBnLhpTvqO7jIwqb7hrFMiie0eq9DsxG7wKEANw5sjgLJ9RauWlW7QVoi0594RbisrDTTSEUYDxSVJu8JeBumOF-4-pa8npdX0fZi8liI5Cm96DjpnV8mFKJH6MEKeThAogIq4lRkDROGWjkYnWBMMUhYGtgCwitVwJpNE7P6JC34Qw-0JlXL24tUREtzAPRYQ1eOo7ZtrRiwTLO3EX8aTAApvt9BstNlzH9k0MbQHfkgZ5EII1TFPDY9zWvLXpmudPuvroDdG2wXj5pWvBme8onzJCE2D9wR9TWwjhuLJgT0dRvPH8TL5m2LZyYyvc_zn0_ICq6fvFBvPrkIkig" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
انتشار تیزر رسمی سریال کمدی «مرد سه‌ هزار چهره»؛
آغاز پخش از جمعه ۱۳ شهریور از شبکه سه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.5K · <a href="https://t.me/persiana_Soccer/28597" target="_blank">📅 00:15 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28596">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qw8ayBhQ5Q93SPWN_dUd61Ko4EAPYg733pxq6qgK-Bil6W0FL9TRcBiPPC10Jg9tWIN_ZOIHIq3B7-Bb7JgWUfZ1MZQr13Sqm_j17Z0nKV0CP_pWjdj224JtDBB5CnfcLKwIWschoYthNr5o209lXymk5E-VSfdcop6FC3qS1N6ay6lm1eJmsE-lOA8CkLCcEcKK5_lasPHNGOQjTwb28A3RGX-luKNu8au5gwfCgaGqNxJpeRV8ALUVwvkfG92kpMeN6umho2JhFc_dHm5tWZeBsjVIJ5XGd8CmYk__sPQv5cZas81XRPONNCCxlAjVxcqF9bq2n0SpGXS92u9KXw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
ترکیب احتمالی استقلال برای دیدار فردا مقابل فولاد خوزستان در هفته چهارم رقابت‌های لیگ برتر.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.2K · <a href="https://t.me/persiana_Soccer/28596" target="_blank">📅 23:40 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28595">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/raDv6Ny_x_Nd00s4vu0icRqrgTjCat1AaFP8kJyLVIgcP-Ni8EzVIe7ZGhFgbeV-wSPpMsWMRBgjkyBJB5Cs9Rl28CteNts8rfcoO_r7josZk-JUDYhuto6QJcr969OwQYkwz8MuPLniifa_Yl_NPIuYTXHZhS_UyrrNXo7h8pFvmcmAH3dCTTo5tD4JMgRp5PKD6zw9m2BMCcFySRKPIp5-KG64zGHJuLHGnWUjOcTCT5DdZ4bVa8aI2-3m0vgb9ZFyY3XrvOwqsdNUqhygHJ5cOuPe8ivJJ2mY8qXGQBw_BmKp9WAnv40UuXt_L6pkA015Lz3K97FIu5JzfKfFgg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
گرانقیمت ترین بازیکنان آزاد ایرانی در ترانسفر مارکت که تا به این لحظه به تیمی قرارداد نبسته‌اند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.2K · <a href="https://t.me/persiana_Soccer/28595" target="_blank">📅 23:27 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28594">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DajILj-M0NjNiofVsA-99vcnroTI-ogZdXUaf5f3UO6hbohHJMQwk3YDU84LJjhBPbb1rIyylS9jCRy-WNKlDjR18u6UDJeHxS05--0c7UTQaEym56Mfu9hRDhe8ZWBzI_OqiV3Hl71CoKMCIfwTNilOVhBimKIYGzL0CpVt9CGoCsm7QSYq9Hlri7ohbOxTQpGae7mgMc6Mf3vMqOJRnDyWTJdZ8kRzfMEcFszUfYr5r-k7pRhfji9MvtQZ8VqzJ0VQJnNrdSwMAZ5ybM5BZoxEU_zuVl578WPewP0NTKlJHqGkAvx7LiJyCDr4sE8vtuis-b4CZkSekgwnT2cLsg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
⚽️
🤩
بیانیه‌جدیدباشگاه اتلتیکومادرید: تحت هیچ‌شرایطی خولیان الوارز رو به بارسا نخواهیم داد. تنها تیمی‌که‌موافق‌هستیم آلوارز رو بفروشیم آرسناله و هیچ گونه مشکلی هم با این انتقال نداریم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.1K · <a href="https://t.me/persiana_Soccer/28594" target="_blank">📅 22:46 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28593">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DN8cMaIIa5OMaBjdhJsipDq4vGSLsoknoJTZjEs5qePMcoyoVE20uvjRMKQAt9X9htzM6Vh0iXSUW840by5aA41n0kRE00-8-4afZ7glFCDHR6MNa9C7kHG9cPo89Rpua8XDFsjDvyiOR4TOnnSrRVt9y20Fv2TNI971WeKgPgJtzJw4f8aV0pAarp-2-En21rJFTifL709ATigpIb_D49XPP0u1MWSOAJGsadImr886fCXmqseoyQLPimkSgVwW3oDcopvpAZAWyvFaiCUbk7p1x1nUm_khNTwsS9w2mkax9MOd_nwKHl2F8UVKXkfHqO3DkDmzZf3R_dOerghOew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
بعدازجذب دنی ولبک؛ چلسی ساعتی قبل جردن هندرسون کاپیتان36ساله‌سابق لیورپول رو به خدمت گرفت. حالاجالبه‌بدونیدکه هدف ژابی آلونسو از خرید ولبک و هندرسون‌بحث‌فنی نیست فقط‌وفقط میخواد تجربه تیمش رو بالا ببره چیزی که توی تیم خیلی کم وجود داره و رختکن تیمش یه رهبر…</div>
<div class="tg-footer">👁️ 59.2K · <a href="https://t.me/persiana_Soccer/28593" target="_blank">📅 21:42 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28592">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DTc6qKJcGeX-4igF0oSM9Z4oQCZQGXOyuCKJfGvGxNjtAn8u1ORLU7s16ql0GfCK47zXqqU4mO_FVnscy_jy46KrrU6lr0kbLNcdvN4db4ouWrKr1uSw1IjlNtReBoassiZL57R1jKKt4zW-VJcgFTAuu3YCanQs3Vrv6h9NTObWZuy4RLc3aFTeZJXhfTiYzaRZA62X_Ixvr3wwy81uv4M9O1vyYvXg_u1Vz2cBSoL0E5bRSjBUqNCb_J0euUUDaONTPggyPLLqo7xOGoJL_l9gkLbBnkyuNGZnR59DIrBI-t-Pq_NFriMrEPTIyyAryK4aemcZEjC7GnzkgDxLoQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
مهدی تارتار به مدیریت‌تیم پرسپولیس گفته اگه پیشنهادی با رقم بالا برای فروش اورونوف به باشگاه ارسال‌شدمیتونن اورونوف رو بفروشند. حقیقت اینه تارتار اورونوف رو نمیخواد و میخواد فراریش بده.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 58.1K · <a href="https://t.me/persiana_Soccer/28592" target="_blank">📅 21:30 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28591">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NwkW5yTBoQTcN17M-rzTcqb9DBOzjK3Z-tma7XssNELTUbM20vfyg40rrOirON8A9HmcRwyW51VjJ4iqejmplBl4U_K-TcY0QVi0GvnmUJ9OtX02AxEzpWiE3iSp0DxD47DAq11OND9jifp8rvBsBKLr6slorUe1UymJ4dqPKAYtnBTT1JbI4RATDpyl7htfcy8ym7f9g3cip7KD25ouis_-EV90LlYh0d5bszLx8grZrR7jNAe0eHqkabz6gG09Uc-dKAaNbE_gqRZV6bD69vDFYk7zRhvQ1vPSM6VFq8Qlkw0XSZDCuFVkCapswVOaVV0JBnXr_h2ZpNagsTZDog.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
هفته‌دوم‌لالیگا
|شماتیک‌ترکیب‌بارسلونابرای دیدار حساس امشب مقابل اتلتیک بیلبائو؛ ساعت 22:30
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.6K · <a href="https://t.me/persiana_Soccer/28591" target="_blank">📅 21:17 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28590">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FL5NnMcGEtl4wyRxerskxU-T_tqMpRqxkC4aKFsKHkOerr6ClUYlDEgXNa3D-f6FkD1oxbKeeSLxu6CBpS9n5tCiPmTqza9I-SEcoCTdkEPq4Qz-o79uY2jlK9gNGM8LjOvsm3JlN7iYwCQ-r8uQaGWhjefqiE793-VmW4rIPO4E8NMMNSfYh34rHosl8Tqi_yHpmGJGJURpiE5QO1DlMNlzK_2E6kO5yi48n4BZOX7zqDxmkjeDrGsEyZxBwWCyGHJfk43LEz_Jfub527vsakv5513wOAhBVlgcANUG5rL2Rb7t4O4aBwPj3ifmBIfq9eLZnFEChLV9JNQ_ytq7WQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
⚪️
آرسنال و رئال مادرید درمرحله گروهی لیگ قهرمانان اروپا بهم‌خوردند؛ آرسنال‌تنها تیمیه که رئال مادرید درتاریخUCLاون رو نبرده است. برنامه کامل بازی هارو در پایان مراسم قرعه کشی میزاریم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.4K · <a href="https://t.me/persiana_Soccer/28590" target="_blank">📅 21:09 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28589">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/016588e26c.mp4?token=bg33soxx34Cw6-Kpk7SV9QXvC0nSXT4KiWYFWwUxPyWInMQzFX0q_kqzLgvmm8UZFE9fTisRL8WfHtKCIUYhgNitVYf7ZAYYq7_oeuWVn_QicEUDm2ek-DFz4dNkLp17d1lDGZUu6ghbQQpFmY7AJqGCUtJtk1h494uJEdo-vVkh8FzdvLYZTQ8PMFAZjMBSxd1O9ESKgwA6kajO1LG9o8ynIcGCnjgo_DbiBAl_9hOxdqK1j5ycUQ4XiMeEGzFAtwbKEIyYLZaT65I4a-vgTfUz7ZCCSRU7hvuIJ9WChr2sGVg1OYDDHtZAr6LkbkRKz1XmHk-3haTST25eq_6yrQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/016588e26c.mp4?token=bg33soxx34Cw6-Kpk7SV9QXvC0nSXT4KiWYFWwUxPyWInMQzFX0q_kqzLgvmm8UZFE9fTisRL8WfHtKCIUYhgNitVYf7ZAYYq7_oeuWVn_QicEUDm2ek-DFz4dNkLp17d1lDGZUu6ghbQQpFmY7AJqGCUtJtk1h494uJEdo-vVkh8FzdvLYZTQ8PMFAZjMBSxd1O9ESKgwA6kajO1LG9o8ynIcGCnjgo_DbiBAl_9hOxdqK1j5ycUQ4XiMeEGzFAtwbKEIyYLZaT65I4a-vgTfUz7ZCCSRU7hvuIJ9WChr2sGVg1OYDDHtZAr6LkbkRKz1XmHk-3haTST25eq_6yrQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
درد و دل‌های علیرضا منصوریان سرمربی الطلبه عراق باخبرنگان‌عراقی بعداز دیدار این هفته این تیم در لیگ‌ برتر عراق که با پیروزی تیمش همراه شد: 8 ماهه که هیچ دستمزدی از الطلبه دریافت نکرده‌ام.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.4K · <a href="https://t.me/persiana_Soccer/28589" target="_blank">📅 20:43 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28588">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NxYwnoVVDaj1Lxdrfi1v4hk4A5qa3gamxvTU8wHGnWiFLjHN3nj9acMZaBHoI_ZDOUDlEgTiU5lNFlBqyqG6SaAQN3erRMI7M90GxllFGqQ7vADyn3gzYzAtxO5-zLmD_LL4Zc_N_I-dfSninTjsvyQRstkt_NknrgoIKq-DbAX-2RGGUSwz0JYVCzduwQlBKenawb1kOEOKPEZIr8p47va_rWAGXhNu7UmXaxxUOgi815MA7JlmfTi02BqxKMk58_Z3i2ItgZV8EgGyQXWwftC4q_8in_JoOiLVhmBjE443-9l7zNWq_IJufgHdu3cUKLfZ9wTxtfJVyit5xAYiaA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
⚪️
آرسنال و رئال مادرید درمرحله گروهی لیگ قهرمانان اروپا بهم‌خوردند؛ آرسنال‌تنها تیمیه که رئال مادرید درتاریخUCLاون رو نبرده است. برنامه کامل بازی هارو در پایان مراسم قرعه کشی میزاریم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.8K · <a href="https://t.me/persiana_Soccer/28588" target="_blank">📅 20:11 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28587">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oEN0KkyjcJY5BkpVWrsnNnqa4jr9ymSqct2eLYRLPrQU9a8jl3UAJTldZH-YIynRs58ytIdpVVz1hFS6etsIf-4lDZBNZP9GG8Uwpfd8QDFw54AunrnOEhAoaVf1R_w7QH8XXEfdc63LnPi6iv0WmJJ-ttPrXQHdODsBQyHVYPqdHNkURBhGAwFbG5MJgJUhIAisR9eps00-BkCTBWI2G21JAGOdteyT5kJ48VDak-vQcEepQqQGaQEh4zrpvDhCVbzAAh7Z8JbYAw8wB7ZiedKQZ1x2_Zfa7daYWNJd-rgSvv3rzQ3D36qvGEhMPuFPUjKfyOpZtMbzfWIAUvJr6w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
سید بندی فصل جدید UCL مشخص شد؛ قرعه کشی مرحله‌گروهی‌هم امشب ساعت 20:30 برگزار میشه و مسابقات از اواخر هفته آینده شروع میشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.7K · <a href="https://t.me/persiana_Soccer/28587" target="_blank">📅 20:07 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28586">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/t17sT3rTB7ZIVog8hW4DIbxktp8912iaPxuNUJhzJAePwWeyRUnxsFH4aL502YJzS5Rr0VeqFbPCCzqRkvOTDDUyS19RtcdqTIVzMPtmMyLSgewH8GEn2mOg_fYun72cBiZXzuD852gEjuA6MIXyOD_SJxr5mQvlrGJQ2fpDubBIWCwMW8Dc1XgAqCqfsnyz2_KNo2Mgerwryh3yJ2twepgYWHoAfuXgYJdHtCpvVdT6vlRuZ42rB2sIDixkT3ItfsqvFcKx-DjAcLMUe43ddcq2xhxe4qPe5vtFP9RU8L5GImeT0m8ikzuwxxj66XvgPu5bjzpC3Ky0vqVOFs9PlQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
بااعلام‌پیمان‌حدادی‌مدیرعامل پرسپولیس؛ پرونده نقل و انتقالات سرخپوشان در این پنجره بسته شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.4K · <a href="https://t.me/persiana_Soccer/28586" target="_blank">📅 19:44 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28585">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gr7Eubjb-20gOLaWc1h_sh5vNSbPODk6cjr_uurvWkBzDmugjbBQp9-vu0QtQKJgABlK-ZgY6icW1q-RdqCSx3sOzeANqLRlMQ4kEejuLef3w_RKRwUCEbtDoDdYuuun8ydju4MoWz672COEypkmqr7iA7xXIyZqz9uAwvkyeXkEjlv8BsdmuJGlr9IaHLYbKAk1TTaPDo-Lo1jOQ7VSKS9qq3ffukg0sPMF-0hRt5nVbAl7TBEurcXxieGHEE4-F4VcxvlzjJKFk34yawxJYCvYOHaDGXORlz-xqEOUP9xeJ9VPNGyJ5z-5dwD-5Y71_3bshMd6TFIze1m002QXoA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
گرانقیمت ترین بازیکنان آزاد ایرانی در ترانسفر مارکت که تا به این لحظه به تیمی قرارداد نبسته‌اند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59K · <a href="https://t.me/persiana_Soccer/28585" target="_blank">📅 19:41 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28584">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/te5udyc3kl27C1omuGhZaERvs8IO0n5QIpgog__ujznaaEFu8N7FBIDhCA8_6GEovvZwB6LYuUnH3DMkD_VoCzNmpXKF59q0RIJFNtad9dd99E1fHzE7LThQkcv8mU83RtavRINulA-pOitWCib1jbcuxx-JxBSY7Hw7zRx89aZXoLpGaO272aN4qxzo57k-D8cf3Ncax2Z0DCt7jpq1F6Hn3SS2V3ft4xLXhySCebRiIVYmZD_6yL2s5bgwPVrwvY2WQ4wzs3W3nkz8BPOQl2-m6pXrnuGKcVBk_3NXzO8s7rcqdF7iSW6vDLSSc0u-i2BtdTN1wvXH0d29MtRFIQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
طبق شنیده‌های رسانه پرشیانا؛ علیرضا بیرانوند دروازه‌بان‌تراکتور رایزنی‌های‌خود را با نهادهای ذیربط برای تمدید معافیت‌تحصیلی او به مدت دو سال دیگر آغاز کرده و پالس مثبت هم نشون دادند و به احتمال زیاد بیرانوند شهریوربه‌سربازی‌نخواهدرفت. سهرابیان نیز به همین…</div>
<div class="tg-footer">👁️ 58.8K · <a href="https://t.me/persiana_Soccer/28584" target="_blank">📅 18:37 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28583">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mh-ccDiyP8H7R7ieL3PPP4kv7K6Dzz7FkQnL2VQIwyINIVWHykpN8jZNHocGFA-alotDC5K8fAbvCyZt96xf1gOPc6eEyKvxAMIlYrpHm3mOM5WacQJayITaSn9YCYWxYpiyPGDuEFzHZk-M3ta5EnBr--2iwjwN4ZuD5H71qVdYWAA-aulbahVG4KStojs9ya_P1obJgOkhwvK_moEXh5jQGQNV8fTlxcwUy25tYULbLCtlmfIYnhWBr_Ff4VJqhLBA1htFemG6lRDQetPFrMQZ5sn1vckykgKs9sbHeLzo2cD_dNqY_AzsJVTwOhc_0ro-dmyb4i0gzHwiinfxDA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚪️
🇪🇬
با اعلام رومانو؛ عمر مرموش ستاره مصری 27 ساله منچستر سیتی با عقد قرار دادی چهار ساله به‌تیم‌تاتنهام پیوست‌. این یازدهمین ستاره من سیتی بود که بعد از جدایی پپ از سیتی جدا شده‌اند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.8K · <a href="https://t.me/persiana_Soccer/28583" target="_blank">📅 17:41 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28582">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RYm0evF76QTW5TsIfrK1Gbd_EqaLej6MBh9cT0YcV7ULxc5OYp9cMCZ8CsqYLhUswMX-CzVZ6k1-cJ1MC3xDoY98HZvuZjbMNW2Z_RFO6LWJcHDGXcNupHZPhnm5JXchbB_LfBBE2Oyrvgu_kyXMZVVuvLjc_Wo6AGd9SRC913LeFPjMr4OA0_AecXMAdkCVil2Cz4kNfeMGPnEwdfCoAZzhkBxLI9142vPJq3PTF2Tr24h0M0WChAKsjNDRyNY0Sibl3bGtiEixvBo0SKIni4oIqwbb-hQJLZU40zy3XoprHGK5ERMcAZnu3KeheG_SccQnexSemUfH6H30yamrTA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟢
#اختصاصی_پرشیانا #فوری؛ باشگاه آلومینیوم اراک رقم‌رضایت‌نامه مهدی‌مهدوی مدافع‌راست جوان خود را 300 هزار دلار اعلام کرد. باشگاه پرسپولیس طی روز های گذشته با ارسال نامه ای به این مدیران باشگاه خواستار جذب این مدافع راست شده بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.7K · <a href="https://t.me/persiana_Soccer/28582" target="_blank">📅 17:29 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28581">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/i-4scHn4710mr63GGz0vLX0stuj-Sp-IK6lKIlBpXOBKU0bAlmaB1ql02rRQ6Pkq127TDNQ_u_DF5S4XLq-KLNzsYwBiqWaumzRkOFe3G1v4uUxqxy8FEOUcG168RxQ1sB4l181-2haic-eEcm7NimW7JbTm691jjO4_l3NAtG__LllT7toCyEK61hyCSJ4QvIjqeXhkPCrBhWK1gUJ1pLDIREgMDNAMtME39EbIERifEfVscrTcltZTiV-MV1Xr66zH1jrZZC8Bl6A2wGVWQhx4IXtyXxPST4YVeRtEqRsPcNkyhXsQ4kuUGGNU1GklmAV0QX9mXXZZDTeytSaplQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
⚽️
🤩
#تکمیلی؛ همچون روز گذشته؛ خولیان آلوارز در تمرین امروز اتلتیکو مادرید شرکت نخواهد کرد. آلوارز میخواد سران اتلتیکو رو تحت فشار قرار بده تا با پیوستن او به بارسلونا موافقت کنند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.8K · <a href="https://t.me/persiana_Soccer/28581" target="_blank">📅 17:29 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28579">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LlZtxD2RPMo-PHIuFL6wpxTKqFPlgpfyM94iqV9HegM6iF9hNm3fb1QpWp_Q7e_15br9C6TV8PFHGpzdPbuPiVc7NeHHgRzfs55AkU2wX_uDxa6YftfNzlXxmn57Ej_I_Oy4ZmlttneS9foLT5I9-Vr5QiORfAddrSdtibz5wDmJxbNFLwNLozQGlJ0kZR130j85grkbwnpD-kV7Sjm_pCtmK_PwL7_X10xPKn7CjmCNOnaT5aoYHQA0AiQOid08Zt0PWtsGaqZ4mqRd1eVofL0NRSEnNONLGOuauLiZEYH3suMqO0nV2cgWc_eRzJUBl7Ex9L32ABugeu5o4TrqZw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
🔵
تاییدشد؛ بااعلام باشگاه نساجی؛ کوروش اژدهاکش وینگر18ساله تیم پرسپولیس با قراردادی قرضی به این تیم پیوست. همچنین یعقوب براجعه مدافع راست جوان سرخ‌ ها نیز با قراردادی قرضی به‌همراه بند خرید قطعی به نساجی پیوست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.8K · <a href="https://t.me/persiana_Soccer/28579" target="_blank">📅 16:48 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28578">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bwrWAGUkyXDdU2mXrBO0-yrg3-AbzEpxEydMII4Mpxca5lfowvFoINNRIZZSeb3Vb6LdLa_wkKhbzCvdi8W_giVvyvsbWk-p5wnfylZN_iD0b_qT0I_kdGyShV3usG9DOck-V-DCS5cg4nBKm22ACCF6zi4Y0UhghdZ0chaCoN7Hz6QwGXrSaHP42hIROFFHNVFJ9rETRThP1mHnB4VV09zfQS6yLq3G3-SjmuiulaESr_ZNZc2fY-QQ5LLJOBcRJk-PDiiASWYXfx9MIlHhziUDftqiRJY_FOyLvJ9UETkVgfFoXnBczqXQfYTpMdLJO-trC_6LOZuTk7Mw-gC4iA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
وزیر ارتباطات:
پرونده فیلترینگ باید در کشور بسته شود. بزودی‌بادستور رئیس جمهوری فیلترینگ فضای‌مجازی برداشته خواهدشد و تموم پلتفرم‌های فضای مجازی بدون فیلتر در دسترس خواهند بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.4K · <a href="https://t.me/persiana_Soccer/28578" target="_blank">📅 15:57 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28576">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CBZ78PFCb2akvm_BeljxFLaJvfxKA5yrFFN46VmqlCkI2TkxWSSpnG7NAE4ztkrMWsGjcxqOFIGK2dyFWpdUAAMsxlx_pwY6rAiOG0Nkn1r5zlwhB14h20skmHSeSA2Oci2eP1Z_97VB_FKigSsgcQpsCwgmggPXvFt85mdfqBBJKiWU263ujaO2t29s4fB1NiaTVhMYgZ4Q3t0nuSFar7ccNksobBZsHH8zKziiS6VOp3DeZnCF83jX3fIPeP_TtWTUIp3r0LPKqAftWJlxfaDPKUGThPRz7jFyihtMFX12xhaajGTjZpUF9Q3MX2zR2B20GEL4eoxFFHbv4L7g2g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📱
استوری اوستون اورونوف که گفته مصدومیت جدی نیست و مشکلی برای همراهی سرخ‌ها ندارد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.9K · <a href="https://t.me/persiana_Soccer/28576" target="_blank">📅 15:27 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28575">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GAGSXhKiupMq3msO5yaE2yBiSWs4q7fAq2wd9lm7XzD3cjpyKDMGf6-Q_X38Zve7Mo0Org10mXZZdmI-PBShAxc9VHMKE-sPDZQx9KyxWeVQAuz44NaTQPBFS7CPi-4z2SnSHre6Rb920uPZSZLgRHBLZ87rF3RnZFRMnxYEGduyvIFlnehz5dl8xFN7X22z_4D23cCwbfZURgn_4HI2IFw0NsDTF4ew__KthFrbN_I2iai155iWduiC9uFyN6ROdxWWxa0QB6DLwTTI-LJIVTqapl99rFe-Yy0QYUAmtAfyC-3Cpis3yIfU_vb9opq_eNVFT1WZlh3mbxC1XqRpJA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
#فوری #تکمیلی #اختصاصی‌پرشیانا؛ مهدی تاج رئیس فدراسیون‌ فوتبال عصر امروز به مدیرعامل هلدینگ‌خلیج‌فارس قول‌ داده که روزچهارشنبه باشگاه استقلال روقهرمان فصل گذشته لیگ‌برتر معرفی کند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.8K · <a href="https://t.me/persiana_Soccer/28575" target="_blank">📅 15:18 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28574">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/22cb4cd7d4.mp4?token=AfkRqiARLtO28rRPbZMIeIYU90Cm0zn90O29i8SWd-QcfoRG3UorQO5mWubqYwSRsLL70qhEQrlIUIg_YfCS2uDdaqoBe-87-3-4QikpfpHFZJ9rbb5LVsgtgOCIxZw5SVY5QWtU7OEbP3drjlXRg3llHCbfjlXlJcHLgeLGCZRWswHrN95VJ85acgwXCKilJcEF6depMaTvKDflaPHFrEK0TXXMovRea0o8iUEgtd2r9_ovzzuuNHdVRCt9mMG_ztAUHUjLP44l7qnZEvGpVM-s2Lu8wJGQ0tv0nlpmj-FBVt1Zgz3gndPp9YqQjrZFY3YiFuTkklgLy3UcIYbAPQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/22cb4cd7d4.mp4?token=AfkRqiARLtO28rRPbZMIeIYU90Cm0zn90O29i8SWd-QcfoRG3UorQO5mWubqYwSRsLL70qhEQrlIUIg_YfCS2uDdaqoBe-87-3-4QikpfpHFZJ9rbb5LVsgtgOCIxZw5SVY5QWtU7OEbP3drjlXRg3llHCbfjlXlJcHLgeLGCZRWswHrN95VJ85acgwXCKilJcEF6depMaTvKDflaPHFrEK0TXXMovRea0o8iUEgtd2r9_ovzzuuNHdVRCt9mMG_ztAUHUjLP44l7qnZEvGpVM-s2Lu8wJGQ0tv0nlpmj-FBVt1Zgz3gndPp9YqQjrZFY3YiFuTkklgLy3UcIYbAPQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇸
👤
خبرنگار در پایان دیدار با سوسیداد:
امباپه میتونه به رکورد ۶۰ گل رونالدو در رئال مادرید تحت هدایت تو برسه؟⁣ ژوزه مورینیو: من چهل گل با جام قهرمانی رو به ۶۰ تا گل بدون جام ترجیح میدم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.1K · <a href="https://t.me/persiana_Soccer/28574" target="_blank">📅 14:46 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28573">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kPbMYlnJDfyWEXw1XHBQ8tctKmBmAiZ2msNnCdII7DgTEnLdxosk5I3og6PWZ27EQvJCbrWUorUWPqQvwEzra57tUalLLHJQjUigBOq-_uPQ1Kp6yx_liarGs9tsYg4Su_SB0v6Pi9JPPmZrIzUOeRFFRbEjZvCpQgugmNYGMTHP0U-GbM_Hu_CcL1ioSUokjYnAiZJL4EaRcTpaH9CNXvD3tKS7XNu504yniSmkLlo8pFsQyAYitMMTqcAtyx_N-aEoYLf5UVX8xCV8O8qYzHQ4dV4BQ1HgmjRPetEx4WNRjZZal_skhIeTP0Cfo0VE8t6piPuuF9S89BxAheJg4A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
زنی باطرح‌شکایتی مدعی‌شد که توسط سرایدار منچستریونایتد در دهه ۸۰ میلادی مورد تجاوز قرار گرفته. این سرایدار در سال ۲۰۰۹ فوت شده و شاکی به تازگی شکایت خود را ارائه کرده. باشگاه منچستر با اعلام اینکه این موضوع ارتباطی به باشگاه ندارد و طی این ۴۰ سال اطلاعی از آن نداشته، بمنظور عدم مزاحمت این زن برای خانواده متوفی مبلغی را جهت جلب رضایت وی پرداخت کرد و پرونده بسته شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.6K · <a href="https://t.me/persiana_Soccer/28573" target="_blank">📅 14:12 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28572">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ut9IOvp2iEE0Owa7Dxz6_03rsx4JpHK-anVpWo28f-NazABgwYEtybNJXKkS7HuUBsp3MiLD_Gi5jMZwhGfyec-v81W1HCmq24iGfsPhd6m0sF8Aw3XIbnCP37_NNB3R_zAZSnsEJVSC6dUQW7Gi5RC2EMnnJwecKFyTzDsEWtWH_KowvSLiiDaJv53qBt_67ULaaAbT2ckt1A4EK-Oi-HxiPCVW-gVmzbHhWZnCuEbE7_4h0Db5jRWa5NSPo2Rj3JYb4KIIsmxMmpdQ4oPVyJAO0JaOhMJFK7xH_tWpPjJEGUpyZ2Xv7zX44kUD6nDmKYKR2mJD0RjqN-841fGDwg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
⚫️
از سری اتفاقاتی که فقط واسه تیمای ایرانی رخ میده: استقلال قراره تو هفته اول لیگ نخبگان تو ورزشگاه السد میزبان خود باشگاه السد باشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.7K · <a href="https://t.me/persiana_Soccer/28572" target="_blank">📅 13:33 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28570">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/tRYYvzme9xg5iupNde5IHOVTZw8S4YvXLNJi1k5vXTsHSxErJ4Ocn2DWjLhFcZrLtdlJ4Fqx3I0Rft-YokoQB4MT9doWl0uRrXftP6fFR0TLLSPF6_05itI88zzix6OBakAvOm6YHJsHewTT6d3QH09xWc62E1BpJA-sMcBtKloYugviZO1vIGXfIRlIxTmbJ34GcHSAGF3YK5A_MeZBsrZYaYxJ29AaeR2-Mv6xzEWK14r9k5lnuQCRnKfB-Ld-VU8jM9NUELPFD-sT71lCsOh_JmWf948BSeqBam2TcuhRmI96b6klvmMLYQ9j3QQNnbkO2DT6s-dZWouIVYiTTA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qSOevcfTsQsz9ELM4JwOcg0VSCfgGYeNdca7avm6vCh0AWY4zMTuapx9gaSAAfJaFjAuVfAVvNiQ_HluoGiaFe-wa7UNCmGnwxMgk5Ah87yLUu-YDWZdjnMfBu-tl61vMWrR1djLkeIV3vl6VIPkY5c3yeD2Z2W7xfrc-bFdcrl4wYzCqG6BGQDxSvjmW7OfZjfU7KGewWyJQQLZfHSPvmDnL0v3THDwKpyVu_reKS5F2raSHTpUS7N61La25LB2D_QVr4vk_9rzeNhA_Jx7QBUTC2zX2xQrcyM1WTzTwmTdBP2pheshJe8enzpEZcdLU2SwiNtM4u7jw55282FgUw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">‼️
باشگاه میلان بعد انکونکو؛
ساموئل ریچی ستاره جوان خود را با قراردادی قرضی تا پایان فصل به کومو داد. ایجنت ریچی پارتنرشه که خبرنگار شبکه ایتالیایی DAZN نیز هست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.1K · <a href="https://t.me/persiana_Soccer/28570" target="_blank">📅 12:41 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28569">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rHO5dFzajwvTyISZkZoLKLPAiRyaK3_l_AdW_HfpC_1hQc7dWWbJk8v81nBaCEXEaGW5AvBoFi3kACxs52u56PNMLMwpOEYpRMK0KZLl6JXSviZrbfyZwb1haiymfZ5j8fFcQ71cQHexsgB8yl8deDbt7mg3l3ytZHLFvcaL-EQX-EI30GHJbCSkpvzQvBzzVU6R69RISfccFEzUhwQGUsKYqqVqkRakJL_eRhi7Wb0cHos-68PWxr6VyrfGkym_trsSnrsyPYBmD7fUrQE8v_C0hrtWqw0k8dpwdW2yAO-m-52ou1tRuYQh4wgxpdgLiu89jSSildduW7C8JnpeLw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
باتلاش‌پزشکان‌باشگاه‌ استقلال؛ روزبه چشمی و جلال الدین ماشاریپوف درلیست بازیکنان استقلال برای دیدار فردا مقابل مس شهر بابک قرار گرفتند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.6K · <a href="https://t.me/persiana_Soccer/28569" target="_blank">📅 12:28 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28568">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b570a2c1a4.mp4?token=bhvgevVE9RbCebdCL0eQ9ESGMDBfcVJbem91O55WS4MdVQVkZKfrD_ryg_21GIaR680pVVjUlSykGdp8Cmh5NVUoKQ6CqOtDJnXLQ3D0TZZehoLwPxg-yQQMuL5iMuaaTHVgvgJ_-wbQNsIQcyU9Aqe4PWr1PE1LnGDZ-Ykg2j9EvRSQMA-OiB13xZMh707NRdp537OgIagqfmwUZKAKIjWtG8zECYHIPwEudEUl_s9GoyB5M70wH6UeBLxmZ-WqVXG31NIOGD5ygKpDZK6_qHyl_ccP1OLJAXqjYVtfgWPbXFwKQm56-XQJuung_VKdCfJBQaKqGsjGja_us9VLk206mbBMo2hIo8JahD31mt4txupkBIJXGdp3kASMVHunzRTqC9ms-ljp-RNJeQaQrSyVhOmAPSe8oqQbIM-pUqlRFOBqAfiYLddk_4sB9TbhOcxoef-atfS0f0XQUtlGoWZAXY9kkBRNf76m0tIpJNr_dMawuPb9nm4N8GQ12GKlKWL-6VOJl1vdXajT5FdOnwBu3kpUY7dJrYPBfWMAsaTHKV3jrFZ01crVj0HrjHZo_keNRn8JqYV6sQbHUZe-LKG4rC9y36daFnrnpN0ngUD8mbL1AJ15djSyHgYek1AdlzVV-qkQqKG1u1gbxB5dWA7F0oSz1-4yx4JCDfdgHnM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b570a2c1a4.mp4?token=bhvgevVE9RbCebdCL0eQ9ESGMDBfcVJbem91O55WS4MdVQVkZKfrD_ryg_21GIaR680pVVjUlSykGdp8Cmh5NVUoKQ6CqOtDJnXLQ3D0TZZehoLwPxg-yQQMuL5iMuaaTHVgvgJ_-wbQNsIQcyU9Aqe4PWr1PE1LnGDZ-Ykg2j9EvRSQMA-OiB13xZMh707NRdp537OgIagqfmwUZKAKIjWtG8zECYHIPwEudEUl_s9GoyB5M70wH6UeBLxmZ-WqVXG31NIOGD5ygKpDZK6_qHyl_ccP1OLJAXqjYVtfgWPbXFwKQm56-XQJuung_VKdCfJBQaKqGsjGja_us9VLk206mbBMo2hIo8JahD31mt4txupkBIJXGdp3kASMVHunzRTqC9ms-ljp-RNJeQaQrSyVhOmAPSe8oqQbIM-pUqlRFOBqAfiYLddk_4sB9TbhOcxoef-atfS0f0XQUtlGoWZAXY9kkBRNf76m0tIpJNr_dMawuPb9nm4N8GQ12GKlKWL-6VOJl1vdXajT5FdOnwBu3kpUY7dJrYPBfWMAsaTHKV3jrFZ01crVj0HrjHZo_keNRn8JqYV6sQbHUZe-LKG4rC9y36daFnrnpN0ngUD8mbL1AJ15djSyHgYek1AdlzVV-qkQqKG1u1gbxB5dWA7F0oSz1-4yx4JCDfdgHnM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
دیشب گندوزی بازیکنی که قبلا مارسی بود در جریان بازی‌فنرباغچه و لیون‌حسابی رومخ هوادارای لیون رفت از زمان گرم کردن که فاک نشون میداد تا بعدازسوت‌پایان که اونجوری خوشحالی کرد و دیگه کار به دو سه پارت دعوای سفت و سخت رسید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.8K · <a href="https://t.me/persiana_Soccer/28568" target="_blank">📅 11:49 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28567">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/h3g_8Cogj0zqpR7SZdHwdczkyh5VPH6Ktu9p6CC5eXHqDIATlZ5zQ7-HzfqbFRJESKllvHNp4YcHGh56FFWnPbxYV3pxu2kcQQlvgD-o8Pv00-NHWR5Fpoguhkoyrfc4AFXT_e-glx5bbyLXY4-qRtv6GBM7f38U6B4ThZ-6-802K5vBj5CS0jO_1prDhTiq_eaK8aQHVgd0UCjOjVAs4JUQtUGSJ6kLsMGU8pb54mvK2MeGFelY6baPhBxSvbyI8DZj1lERa8cgsjWTZoYhEAN3l6JppHa7s-Mg0C0tA1OqO7mdlZL9deixun5mVtp3SUiX_PCjB3d4ZhwrXX58dw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛ خولیان آلوارز تمرین امروز اتلتیکو رو پیچونده و گفته دل درد دارم نمیتونم بیام تمرین اما یه‌کمپ‌دیگه‌رزرو کرده و انفرادی میخواد تمرین کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.3K · <a href="https://t.me/persiana_Soccer/28567" target="_blank">📅 11:28 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28566">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eYJ_3gkQTIr4QgiKXlpGnuSQuQO3C-MESKi2WUQFZRiMzNh8ENhSYaS9v8k54E4WLydBNe0QPD4j9DYQ5keseg3ENALIYNLC7tHf6tTAA8iDVfudYB8VLKJQwtFb3LGTK49mGCnyQqDNTY-a_3IzysqsDiduZ47IqUn8Pqv8iEyq1ImVGQN2QiM_GlfzVDFtDLswRGcNbAX-WkksadDhqwerehAWDmE_vF5HbJT-y69g1TtWkCqQ4rTwJJ2Tp7XzJ5bUOKuayE8_h9YJ5tv4iO8bQqj6fP5cLoHz4FQ6CX46q4LEKHCPy7e_I23s5FUBUdtIiEhy9ezv8dKBghPI_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🔴
#تکمیلی؛بردلی‌بارکولاستاره‌فرانسوی PSG در آستانه پیوستن به لیورپول قرار گرفته. توافقات شخصی بین او و باشگاه لیورپول انجام شده است. بارکولا گفته‌که‌نمیخوام PSG بمونم سران پاری‌سن ژرمن هم گفتن لیورپول 140 میلیون یورو بده بند فسخ قراردادت رو فعال میکنه. لیورپول…</div>
<div class="tg-footer">👁️ 58K · <a href="https://t.me/persiana_Soccer/28566" target="_blank">📅 11:28 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28564">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">🇪🇸
🤩
با اعلام رومانو؛ هکتور فورت ستاره جوان بارسا به دلیل زندگی در اسپانیا آفر دورتموند رو رد کرد و با عقد قراردادی به رئال سوسیداد پیوست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57K · <a href="https://t.me/persiana_Soccer/28564" target="_blank">📅 10:40 · 05 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>

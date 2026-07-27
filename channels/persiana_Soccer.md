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
<img src="https://cdn4.telesco.pe/file/jCc3YSp78ZdyqfgEwgwUqx3oysH0qgR4aqjTXuxjv9rC_VvuMzlbkvWOG964vD6lBWkWZ_fEoADPwcj9ke883BDTfjYYHVT9VQWGWUyF6wYfRJ9M9BIHkwVyEkkUCH3O-_4UWsfmgB8_N8132nxEw0llXMc-8fBmvt_NMYcSLUL8rA_1x1UnZC2NLZETScQJ_gC4G9bdLdwW7nB4BR4za8uWd9TSYGCvDGBeTcrW7iCGvdaA4pkdJYQRnPjaY4n66_acKQO69OWRaT5M-MlMJRGL7nbOgoSYU4feJ9lK_3mrMDpIS2EAWCGKOy0Pj1QooCk-aYb5WKHtRnH_FdMMDQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Persiana Soccer</h1>
<p>@persiana_Soccer • 👥 605K عضو</p>
<a href="https://t.me/persiana_Soccer" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 پرشیانا ساکر دریچه‌ای تازه از اخبار محرمانه و داغ فوتبال ایران و پوشش اخبار اختصاصی نقل و انتقالاتهماهنگی و رزرو تبلیغات:@ads_Persianaaکانال دوم رسانه مردمی پرشیانا:@Persiana_Plussپیج اینستاگرام:Instagram.com/Persiana_Soccer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-05 23:44:36</div>
<hr>

<div class="tg-post" id="msg-26645">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e09976f50c.mp4?token=SHfSWz2DXuC1JwXZXBB8U271-sj4Zt1_6QXNcaQWqJZ0WNMS9xEwjDLwcC-FnzgoWGWAjrexrJcj9tsDSOvrnh8t7D5qwT6QFSjyY7J6ZoYBUIRp6BDY_HzlK0KbI0_fh6igHTc8GsFkyZBOMrm-lGI6Ms4dnXpFGhiMFr6FP8itF3XzN8iYxzWkyrTX-EiDDkNmPGBFajEGRRH7mUBrL4egopZXcPsfz9O4VKLxYL8DdvzqpEKV8PQwjuPHaW7_uvwWtrueHhFS4hFM0gwHMMW5V1yyJn-cYNH6Rfpu85GYEtF3Nzy58EazCGUlza6Lk-AdYDSby-dzdSlJ6Obs8w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e09976f50c.mp4?token=SHfSWz2DXuC1JwXZXBB8U271-sj4Zt1_6QXNcaQWqJZ0WNMS9xEwjDLwcC-FnzgoWGWAjrexrJcj9tsDSOvrnh8t7D5qwT6QFSjyY7J6ZoYBUIRp6BDY_HzlK0KbI0_fh6igHTc8GsFkyZBOMrm-lGI6Ms4dnXpFGhiMFr6FP8itF3XzN8iYxzWkyrTX-EiDDkNmPGBFajEGRRH7mUBrL4egopZXcPsfz9O4VKLxYL8DdvzqpEKV8PQwjuPHaW7_uvwWtrueHhFS4hFM0gwHMMW5V1yyJn-cYNH6Rfpu85GYEtF3Nzy58EazCGUlza6Lk-AdYDSby-dzdSlJ6Obs8w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🟢
👤
طبق اخبار دریافتی رسانه پرشیانا؛ پس از کش‌وقوس های فراوان و مذاکرات با باشگاه های لیگ برتر؛ دقایقی قبل جواد نکونام با مدیران ایران خودرو برای عقد قرارداد یکساله با پیکان به توافق رسید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 8.08K · <a href="https://t.me/persiana_Soccer/26645" target="_blank">📅 23:37 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26644">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/D_KyClrn_Wej310DtgBg7bZAjOQKpLAk_DK2ySA_EbA3E0HRUPQHT1YPwNAefK7AHAW6kSMnonMP0Wiz9xod3-MJldtn6LLTuJs3N30CHxABKVczBaeLKWgfpWhlOz63TkubaddItHB1IoF5OWGo-mdgnTiEXAqqqfKa4lIxNbT4mMK56tfbgkOxTK2qKJc20-pcD8ZNgb0wYt-Mlzks5z2yp4Cc4rcx0_MCNLZa2n4n5gtf8TiCWpGYNoZS4pEj1qjQaCWlPsJgMvkHFOxJ3WFFI1O6teGk2wFG6RMCF4Mqq-ohe4GLDYKR1a09C9X_C1WapO7Gt1iGDOmZpc1UPQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔹
فرداشش‌مردادحوالی ساعت 16:00 قرعه کشی فصل جدید رقابت‌های لیگ برتر خلیج فارس انجام خواهد شد. مراسم از شبکه ورزش پخش میشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/persiana_Soccer/26644" target="_blank">📅 23:28 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26643">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QgJMqdMbuaW-x9ui-rKKWuBBk593yX71wXNn9MtDX34g6SNBrmDAzOI021smqjFGbnjjvWID3TSQ-CnmNoplj-F4FmE_ubYMI3J95LGgMj3loRjB1l0enuvjGYPfDAqbsWAdF8_-nM8ylfZiF4hVczHwKJMQddLWbgoQvGeslmy0dvK3zNxLyG80U-ilPO4V6lp-7EWLoVvHMnKTIaJ0AOMmWwttLBDQcpi6i9f5nfBRkpvHkV-4piLpGfNynDboEC2sPPgjTSI0Mv6dGpnjHO-DPs2ASiquS7ZTjMIQTwdnQMAIOjGEncGva-jY2tW3642rmY0ixeR3vt1A72RBFg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
یکی از مدیران باشگاه استقلال درباره آسانی:
🔵
با توجه به اینکه فسخ قرارداد آسانی در سازمان لیگ و فدراسیون‌فوتبال به‌ثبت نرسیده و باشگاه هم اسم آسانی را ازلیست‌تیم‌خارج نکرده‌ونیازی به ثبت دوباره (new registration) ندارد بالغو فسخش و توافق نهایی، طرفین به قرارداد…</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/persiana_Soccer/26643" target="_blank">📅 23:17 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26642">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pRxZYymahxCnNUXSNaPcZNGVYdmutff1R_xkaO2fmUBVVTTuJX4wX-04wSYk2slJD0q12Cr6Lu545g0MMDGcouaJQdtLytIjl9vB33ZycY4g8jT2gSjVLgoAAnjX05Fm4SfXrQfYYxMsxdYpYH4rBIrq65bFDouBB62fF7WSkRNrGw0uRa2L5okWNdpHR9dYVBHr7kXVsYeD-ehR6oxOSfk5bJUFuhT43HBWxE2SSC8FV3hl6qSgkA-v_CIySIltG6KlmtyqBFdCMsxn-PIb7Y6rmhlA11Ka53P_PyRX0Z8nzMfgjwiOIW01QIqJDnYpzu004cxOJNWTjk4wgzgVmg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
پرنسس لئونور شاهزاده اسپانیا امروز درحال شنا کردند که ناگهان با شش تا پسر شکار شد.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/persiana_Soccer/26642" target="_blank">📅 23:07 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26641">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dpM4_oONkl7285N16_CwukXXTawHwUu9XpOVrht_2JgOKhnEX2mH7mt9iytTZXocaF0NmxsCCkOvse3Mp3NlavHT2cxp-2_zEeR6rv1Jej7XL_rjxLzngGLFXK5nbhljIBkvEwY3WbNrk_qzkLC6Y1CEpPz0eEMtJvYzy7oEUBcon2Dw6UGeTMTkJDcL4ZTtLxQ0KNDxVTxifWfnfqnOneQ9k1jARMv5et47cpBZNoCzpXfMCHd5S2aH1i5q7UQZfpnyWTHVwi0QwRfqskXhboAbozXvqxSFF05iJfeKxhyfUD16WD86_65OWabLpzbolrMQu1Jy_uJRIbejTi4ULA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🇪🇸
خبرنگارشبکه‌باشگاه رئال‌مادرید: به احتمال فراوان فلورنتینو پرز بعد از جذب رودری برای جذب الساندرو باستونی مدافع اینترمیلان اقدام میکنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/persiana_Soccer/26641" target="_blank">📅 22:48 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26640">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Bh8ZrS03wW_OGY21Q6A_i_wfQlY-XMPwYyx4vJhAblzAg1QpnYJWErPrgfMjnfQfB3nwCxnAYqRtMHHT_uX9fvoJiMf1aDzz6CFQ8ARNupuM_xM_Dhy6MkWpJt5c6kUNwYlsaCHcpUTshz6tm-9Hhc9vVq2qEgubOxYcSKUVClNm7jlZXRzeqNRWTjQ0kPiu7MeZxUSIWlxNb-hv0KF2K3SdTcHqKzv0XIPvdjaOOvxDxfcpgh8UOPxNjKpiiFQxEqhtSNSPpSRIivNIDtBgbCVol5vVy_czqBwR1dvv3IOUCUeNlLg3NinRpyEWtwBrZhezlhzMutzDvqH8ZUrUuQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
#نقل‌وانتقالات|جیمز ترافورد دروازه‌بان 22 ساله انگلیسی برنلی باقراردادی‌بلندمدت به منچستر سیتی پیوست. احتمال جدایی ادرسون بالا گرفت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 32.1K · <a href="https://t.me/persiana_Soccer/26640" target="_blank">📅 22:29 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26639">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tWG7zQne2TXr6K8oPo3GgxVmQWTgIPKaO5hP1Xf2utPRL7FT6PMz8er-iroLvgQeQWS0dkt4XvBCHXCBarDrEGfWyijJFxvupS4RlRQOvJQxHKX6BZMdci7uKPkQFzb8nxRGCq8-nA-FxGMZRlbX8DUUsDydIYoKFLQg4vIGPbbo3shDqUpMDtjOE53BwOcwcmIfx-MUf_To4WuiwWk8_nA_dCnVEItgtx87iBdsls-xTgXebvqdSh0uGqtjuZ8SL8NdyPCW7H-jn9e_Kddfd56veyRwbmtaUsHJUUCxJRoBJ4qj0IhJoTQZqxF29LFbc-6GFlHfUZefiudmVABrYQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
🇮🇷
#تکمیلی #اختصاصی_پرشیانا؛ منصور عظیمی تا ساعات آینده راهی امارات خواهد شد تا رضایت نامه این بازیکن رو به الوحده پرداخت کنه. انتقال محمد قربانی به تراکتور نهایی شده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 35.6K · <a href="https://t.me/persiana_Soccer/26639" target="_blank">📅 22:12 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26638">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KWTjKH0ews5z3dQj7QMfhvoQP9Vf9BCoO3785wgvWzG0i2ggTGDBQ1GgGAps4kun1l_8uiEcDyQWKdZIMEEdoLzIJS1JMwLajEorKUaPG38L_-JNIa8Vc_4ArIQfOc5KBD0Be3XTo5_HdUwWuTB5KAGFL0zP1Q9NbuAOaGX03TvUeytXr5ua7ObKKWycU7gvtG-vgSRbR58X-QdyMn3RQZhimTjQUQ8exqjJtwM5u9DwUU-KUeaqGLa33m-t6J8gGXwYZinwsxmwepsI_H5FHGecWJRdUocAAgLkQkhzVDk3Rg06isjep_eMV67HOFh07JKvONFDyHh1XdrDvKopmQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🇪🇸
خبرنگارشبکه‌باشگاه رئال‌مادرید: به احتمال فراوان فلورنتینو پرز بعد از جذب رودری برای جذب الساندرو باستونی مدافع اینترمیلان اقدام میکنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.5K · <a href="https://t.me/persiana_Soccer/26638" target="_blank">📅 21:45 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26637">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PMIFOfH4Ummqqud_YBRfq0AiFDlGbA7RzWqA2MxFlK-5jDie6gokfT3VgxxLWFGyo-Hu3NZym_co3yKzoSEJa0ETLeAuEVThhCh25NpkYR85No9-v_-ycjQsmfP253qcJEtx4ytcgX9Yt-k9bfO1yM-Q09OyOH5bi7QZg2H8g0YEvMQm9Jh5dyOPO26990RzT9IGXfhokbC7rEiyZwLzkamh5HiMUr3pfcDvZxpuC6t29yJtfMbwTVLEHz9g3WZxUP9GcTeIEMWpavkOYTXUscTBmFJ8tahWrWHiYFyTyntQ0eqmIqfza2f-rMv-UE9aArM4TrCfIf_7V1tu_dQVVA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
رسانه‌های عربستانی: باشگاه الهلال عربستان در جدید ترین اقدام خود با پیشنهاد سه ساله سالانه به ارزش 65 میلیون یورو به دنبال جذب لوئیز دیازه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.2K · <a href="https://t.me/persiana_Soccer/26637" target="_blank">📅 21:30 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26636">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OhrSL4OT7akFezOOV20GpJWTOFYBa3Lsrd1PrtOOYNqTmqvksoxcreEoUPLp81lFkesoQnZiLxIpKyhv01unkIldYtRFIYi_CreErjDVgetEARo94OVb5QD2geOxAkBumhYxA7Gl-53_9xFNoDlYocnk0EJPznETJn-PtnKqXBZqxCxPJExXzNJ9XdN2E3BaWK_uQkzHWlwd-4MMGT44WLVVe2fMwdy6mUyP4UfONuNEPeX3uKrwCeiAq_oUVdaTBAaefzfzBtSOiKyMMkpCmxEg20Nym4QgH2QASvpvcMltuedn4p2mkee0WTjN2X9tRn1ngCWtC4yrEjRr6BIdyA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🔵
فلورین‌پلتنبرگ: ژابی‌آلونسو برای تقویت خط حمله باشگاه چلسی خواستار جذب دنی ولبک مهاجم انگلیسی 35 ساله سابق باشگاه آرسنال شده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.2K · <a href="https://t.me/persiana_Soccer/26636" target="_blank">📅 21:02 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26635">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/n_ku-_dxBuhLq5DvlllfNNeARH_2Ar_-CLfZnL97Cg5GZlRiL_fE7-m-yuVe_q6c6_5lT_9N2yx8x8WfYJCfRI4MF18scL3qu67wLKoRQ_W0cNvbfwsS7cJel7NjdeGKQb9ihTEQCIZxuXByTsaup5gjqfoDyW32DzAaPv1vFiqNlm0HhwFp7FHzrBI_ZCwWFKeozFXAcCSCeJeShGgODFA7jmXUNSILioBD3pCMr6JBPls63JBseMMzSVnI6F4pzm_jf14_EJpjne_7-l3X-CFMwX_S85VgSwXqk9yZZPaJIXdX0oa_MfgpcleydbNh4NHmP2L1oSIaP_QJTYY-vg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
آتزوری‌درحال‌شخصیت‌گرفتن؛بعدِانتخاب روبرتو مانچینی‌بعنوان‌سرمربی؛حالا پائولو مالدینی اسطوره میلانی‌ها بعنوان‌مدیرفنی تیم‌ملی‌ایتالیا انتخاب سد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.9K · <a href="https://t.me/persiana_Soccer/26635" target="_blank">📅 20:45 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26634">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KUvVEWFuLH8InWb6Nk7Dg2xLyqqBDz--E3jYsLff1HfDtilUdne6QfG6u2eNe0MvIYnVN0AsCOPDUQuPH_U31Tov8EZCbRRBA4nZ_jwI5d6B1y7y5AV4vST_HDNPatzTR_iya-cOlOEe1Y4tORUZKTLuZ1wDff8ck7cQu7QVY4A3jehfCVw0BjmUsQZaMCWImyXaLEQK_vCLdQqX9cQ0M9Va-jjKxENYws5day0rtGEAFzrtXsckq2FxaocMJG6ln52_qoEFiL-CIHTPxpjxItmVi8fiLjgh1WE9KyHlfeYWK6KQ3-Va7VBtU3w0hGS9FGopSPI9rlltqzmyrZUGOg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
باشگاه اتلتیکو دالاس که درسطح 2 آمریکاس و سال 2024 تاسیس‌شدامروز به عنوان نخستین قرار داد تاریخ‌باشگاهشون با چیچاریتوی مهاجم ۳۸ ساله سابق منچستر یونایتد و رئال مادرید امضا کردند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47K · <a href="https://t.me/persiana_Soccer/26634" target="_blank">📅 20:19 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26633">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ae0WFtqXEQH8ATlgGVZTyYg8kRXyVg5paG46yY98OBTM_EHUq8RILux8Ax5YlEqKzAREJjMeOYeUgjt4JL0A8FaTL462X3DxGSksW9TZvvJQlwdbkLyV1gvld7TLVqM699tSWDhXqcVXqty95LN4id0wfbaNknecUBqutuC92IvCpWq5IeGENJjR5-fG9vSijPhkrqA9bAe7KDyDvrJ4ECwfHYFD7mqp6zS7vK49eBav7jJ28AH54WK0fgGEsS5zIuTZqeCIgIVUnh2oXg2DT9Nl8cGXCgBFq8VT-YW_a137x5FxQDCk4bluc3SxLw1SvpTy61QN_PArXO_TsGXiBw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
میلاد کرمی دهن سرویس بلاگر محبوب ایلامی تواین‌وضعیت‌که‌میبینید داره شیر آلات تبلیغ میکنه.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 47.7K · <a href="https://t.me/persiana_Soccer/26633" target="_blank">📅 20:11 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26632">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uqNNqJ-WfZt15tf3MARfJENv6BbL7ToEJ-0b37mMfJBDjH4bnOf2gYa2v6mOZSevLf4M583BbdyGd2OMDRWETnh3AApbMX21txyUGVnRDR4E_TR8lO_nbqlb8UlEGYWpovF77s-QKLmDItgPKsG-gIaS1t_BNwTmXpuZLniZVN7p_SanQEmrh0QERglaWtsntvA5zQZH2KHZMUn42n0OQiz-Ny9L6MmLNF1Xa7IScHd5SiJtOQYj4iysrsTER6_CTGH9-UBWXb6FmZssVT32SDwsnO0yWvLC5W8HxqJNQA2fKPmvm9d1nVAvTVm-dny8o5-qVMxWHKz6IGp7S-4aFA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#تکمیلی؛ روزبه چشمی کاپیتان33ساله استقلال ظرف فردا یا نهایتا پس فردا با حضور در ساختمان باشگاه استقلال قراردادش رو تمدید خواهد کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.8K · <a href="https://t.me/persiana_Soccer/26632" target="_blank">📅 19:51 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26631">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/K2xnGxvkg2RWH4DocOJQ2TgifWu9ZTGlwfMPKX0MLVx6vQEYgP69OheG01D0Dd_0sDRNLY5qPIZ8gC_oIS7Z50SIT0Cs6k-P6cav9QsDtGFZ5SZ4YvEfF4L30yn37EhbgOeSlmaOl6_nlmwVLUrK_0IhCR4KnK24AC0F7Dwss4Tmp_BX7sf8Yrg3me1XSpLetb6zIzeX_srO0NaaHaITEleCKZXHBjx-LFBr-invMlxcoaEq_lYB1O1hDjwWIGRaBW5jjtUp_976JBwB47tpwyPuVZQKCgkMsIW1aXef983ApEuY_VxqWGmjrjKhCzhhlxEBtxuc7ome1zsLbV9Xog.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🔵
فلورین‌پلتنبرگ:
ژابی‌آلونسو برای تقویت خط حمله باشگاه چلسی خواستار جذب دنی ولبک مهاجم انگلیسی 35 ساله سابق باشگاه آرسنال شده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.8K · <a href="https://t.me/persiana_Soccer/26631" target="_blank">📅 19:44 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26630">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jHpDm9Vh3l7igt7JojxSRt1jGy_GiyotKYxuoxmljyEpsvDHyqosun_fDlJ2OzkEqEndEHVFcWcoxgMbuE7ZzM-oCRYV12LcFuq8DtlQRy6kDSyJqieVlUKRUOPpPwODu6gbnDPBxlqC4bQjwsNDqOYjGyALxBM43u0OKbYd9yOQW4ZTj8SEHJr6AFqGWiEUwniZpdYxQns_yOIkUuZVz2gUyoOQ7YlwwlCWuie1H0MM2m2Ozad6E3hROtY0uXRsVjkUNQZ6LgwTEFSLBc63yHEPumS7hkZEKhF1mW2vIZaii_nQpS3V3f8EPS5H8cj7n45TGpWp0J2wBAXKU-GPIA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
باشگاه چوروم اسپور برای جذب مامه تیام 150 هزار دلار به به باشگاه‌ایوپ‌اسپور پرداخت کرده بود و 750 هزاردلارهم به تیام برای 1.5 فصل؛ روی هم جذب این ستاره زیر یک میلیون دلار هزینه داشته.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.3K · <a href="https://t.me/persiana_Soccer/26630" target="_blank">📅 19:13 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26629">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Gc8CAtxEjgo1r2AVbxYEAfLgTPe9EMnl87sBBbFck7YhS0YI67j2bFqjhayrWvsdGrcMAsWiLYc9plw3G4L-cO2lXvk0aX_DckHEs1mKHC4ZzgM3aMKvlsIJYYdPg2LvatvOp720filq50knsRcoCS9p5wSTNjUJhtFTJnGDEVmeY7OTehQGDNoFEEutH0I3osjI-_gtwpaXps6qLoW63w76o_ISwuT2CIcTbi7QEUk4CCoaVv1LE5QLlog8AeyAz2d_8s5AG_qgVUeORi0hInXAInheVYBef5W4OEKGM4MiE4TTpeVmOA2sYZOMksLukaQi77f3Vx9Vvz9obulV2Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🔴
فرصت 24 ساعته نساجی به پرسپولیس! اگرپول ندهید دو بازیکن راهی استقلال میشوند!
‼️
علی تاجرنیا رئیس هیات مدیره باشگاه استقلال امروز ساعت 11:00 باشهاب زندی مدیرعامل باشگاه نساجی تماس میگیره و به او اعلام میکنه که حاضره رقم رضایت نامه کسری طاهری و دانیال ایری…</div>
<div class="tg-footer">👁️ 52.4K · <a href="https://t.me/persiana_Soccer/26629" target="_blank">📅 18:51 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26628">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vBQS1zVIj1VWgHvShiywc1gnpg-mvBDsF0pmSNneq1z3vNHOaQ6e90sORi90xWQRw1CGjYpLhsA2JYM9PNI67ZcOYApee5aR0wc4lKVQYC73gYIuex7fm2SM2W4Ey2KAxl7LfWD7FMWM3-mZhEitTrpuwbwALdkEIu5siLnjSvo8lfgKDqLEV_3GB4h86i3EeGt2JMixryIJq1V_8Z83FRQv93s_lfMABNAN-36cZ2yjk3G4cWoLgTMprtXEOhTio_UCvo-EtT8tlmL7G1cghFKgHUFAR0n1uxrbwiyplXLA_G8xg20n12MfBK9khi6vG0E0v_GSRSX5pAXfJ5FRHQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
#فوری؛ نشریه مارکا: الساندرو باستونی مدافع میانی اینتر میلان درآستانه عقدقراردادی چهار ساله با رئال مادرید قرار گرفته. توافقات شخصی صورت گرفته و باپرداخت50الی60 میلیون یورو بند فسخ باستونی 27 ساله توسط افعی‌ها فعال خواهد شد.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53K · <a href="https://t.me/persiana_Soccer/26628" target="_blank">📅 18:30 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26627">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2b902abcc5.mp4?token=ZF8BxrZo2qEdU1cKGq_e0KKpL6X7G8-Qk72OjfHw_rA7LsDAxnwSTlWQi68PEpy_ihfISlyyawlITK4sj9IvZ1axIa29RWeFE397_RVlsTKHT70x-MV_DDxi0krcbweMvhiFjPgK2GPoTWF_AENno1FTWGklpdHDL3aaBLLYVDvzcks5hILolf_kLx8TIsM4DzQfPF0piztcx9PceOKZbcfv1mEGt6I40o5VNyEaUf7Y8uPEg_Am3734Koaw4czcglzAWnsXcyQFjNPk-FRBFXka9h2vY7OnMYyIiGJtSK2FWvHX8p-ASTSw_797ugwo1VgH6vwpp9ce9O4u0dX3DA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2b902abcc5.mp4?token=ZF8BxrZo2qEdU1cKGq_e0KKpL6X7G8-Qk72OjfHw_rA7LsDAxnwSTlWQi68PEpy_ihfISlyyawlITK4sj9IvZ1axIa29RWeFE397_RVlsTKHT70x-MV_DDxi0krcbweMvhiFjPgK2GPoTWF_AENno1FTWGklpdHDL3aaBLLYVDvzcks5hILolf_kLx8TIsM4DzQfPF0piztcx9PceOKZbcfv1mEGt6I40o5VNyEaUf7Y8uPEg_Am3734Koaw4czcglzAWnsXcyQFjNPk-FRBFXka9h2vY7OnMYyIiGJtSK2FWvHX8p-ASTSw_797ugwo1VgH6vwpp9ce9O4u0dX3DA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
8 سیو دیدنی وزینیا گلر کیپ ورد در بازی مقابل آرژانتین؛ پبجش از 18 میلیون به 20 میلیون رسید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.2K · <a href="https://t.me/persiana_Soccer/26627" target="_blank">📅 18:17 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26626">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3df251c94b.mp4?token=toH9Bi8IN8zciw8Ru-kxLEfPKBB_V6EDi-PyXIhkG0MFhoQwt70aeUZTwimh7vpKtYr3KvAhgoqzMqRvcxAhOWMEE9GrM4s-GUaIgEmwD8kFwdN__9TIVYbcrvYSaU6K0XW90wtw8LrWB5Qa8O4Cdre7qgFqal74jdyrnLNoyLqHoEV5iHIFTLyMjvud4Bx9K-ZezGcqSXgTli9FEXuG3vPZpbX8HcpXlkpoZpNXk1jGnronxVIhxMHGeR2NMW7GCZ0_wXSZCZIsSs1SbM2som4NSGpJpCpo0Eac_d9XBi_J57js-fI7TTXGe9QHtdFc-7CG46CbXso50xNB6gRTX47G9pWWNXqL6TakbVXHx-eG0-_4dDozziqbiO-FqjwAQS-8BeReeFr2ESa_gpADlw7nBLUVbwPP_IaFBhq2ctVVmFsc0xeKAllPkjprJ0aKKiw_zcj88iUQVVARvPZk6jPa7LRiLfV6YXCqFbxDOFNYfIC5xqk9qmF2gEAM6FDy2rMDWIBgS1Km2b6BBbquByECbmu7RfxvxrLzJtsfbX0K-DetB0UBECgox01jpXquBj3Kc13I8qnNbkgMzvx-RB1iE4gtt3IA8TYFiRg1kuQtPFdB5udRXpOq5Fhdc8m2bII7kgAdJcMSpz9DVXwA8ms3YvYMM71e5KpjqAVGSHg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3df251c94b.mp4?token=toH9Bi8IN8zciw8Ru-kxLEfPKBB_V6EDi-PyXIhkG0MFhoQwt70aeUZTwimh7vpKtYr3KvAhgoqzMqRvcxAhOWMEE9GrM4s-GUaIgEmwD8kFwdN__9TIVYbcrvYSaU6K0XW90wtw8LrWB5Qa8O4Cdre7qgFqal74jdyrnLNoyLqHoEV5iHIFTLyMjvud4Bx9K-ZezGcqSXgTli9FEXuG3vPZpbX8HcpXlkpoZpNXk1jGnronxVIhxMHGeR2NMW7GCZ0_wXSZCZIsSs1SbM2som4NSGpJpCpo0Eac_d9XBi_J57js-fI7TTXGe9QHtdFc-7CG46CbXso50xNB6gRTX47G9pWWNXqL6TakbVXHx-eG0-_4dDozziqbiO-FqjwAQS-8BeReeFr2ESa_gpADlw7nBLUVbwPP_IaFBhq2ctVVmFsc0xeKAllPkjprJ0aKKiw_zcj88iUQVVARvPZk6jPa7LRiLfV6YXCqFbxDOFNYfIC5xqk9qmF2gEAM6FDy2rMDWIBgS1Km2b6BBbquByECbmu7RfxvxrLzJtsfbX0K-DetB0UBECgox01jpXquBj3Kc13I8qnNbkgMzvx-RB1iE4gtt3IA8TYFiRg1kuQtPFdB5udRXpOq5Fhdc8m2bII7kgAdJcMSpz9DVXwA8ms3YvYMM71e5KpjqAVGSHg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇹🇷
تیم ملی والیبال زنان ترکیه با برتری سه بر یک مقابل تیم ملی برزیل قهرمان لیگ ملت های والیبال زنان شدند. زهراگونیش‌بهترین‌بازیکن تورنمنت شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.4K · <a href="https://t.me/persiana_Soccer/26626" target="_blank">📅 18:17 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26625">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VF4IFcE0RDf5RVkJtVqrXVLV_vAkeZGJhd0GqtR90uqERC-2IjX_Av2ae7DNQBPp4vAgr8DRN5gHXELHvZf3KPcShZbKupQKc3y3tum7dbTcROLc8eKh90MmiFgSiJXiWoxqaRNb4eV0F2XkQtqXpj8PuooVx-1STJW4B0do6VEGvIORP-0Igcm6z-xoSFMh06pBfJF7G43sJ2xUdPvGXhDKIvt20GNRpcVfQIVyftEii7_wDQyUaLDegqVuCCNjYnu1F212TbGGjj4p3L77_M7YbqfvXLIUz_mx3_6z5mml5S4naK3ORcqE9KZKgf-6mssr1uK-b6baWvJiXyYSrg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🐉
میخوای به راحتی از فوتبال و باقی ورزش ها کسب درامد کنی؟!
⚠️
پس همین الان وارد کانال
Evil Bet
شو
چون بهت اموزش میده چطور دلاری پول دربیاری
❗️
💵
اینجا میتونی روزانه درامد داشته باشی و سرمایت چندبرابر کنی
👍
آدرس عضویت کانال vip:
https://t.me/+TmGWkUYH_8c0OWZk
https://t.me/+TmGWkUYH_8c0OWZk</div>
<div class="tg-footer">👁️ 51.6K · <a href="https://t.me/persiana_Soccer/26625" target="_blank">📅 18:17 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26624">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QWy_O59b_3K9xV7109V9nRTheDXV9d5KeH02TKceh_B4BnCpom5TUtHxPxAqy0YnSqD2wnmwOXTGIOLf9KDFAnU71MMk06yJcBsa4IiH1_RRi8RNlbtWmIGBWNUAW_nK5VQfsL9QbMOF2iqBgc-08_vayzme-k_sMWAkAOiCXb7AcV-0qVVf5C_HjGKElDTOMU9V_Gb0kE7COLB3bltpfR6vnc8ud0KdhjJ7G1x-befsfiTbJfB5pQTvjFzAI9UI4OZEoPVRLMR4rttMFg9srShB_OCOrPMf9HE4zwNzBcas1kWwQABV3390fU-7c2EDT7e3quUzqaAkiQcCev5Jow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🔵
#مهم؛ اینکه‌بعضی‌کانال‌ها میگن زندی مدیر عامل باشگاه نساجی‌پول‌پاشی کرده که با قیمت بالا تری دانیال‌ایری‌وکسری‌طاهری‌رو به پرسپولیس بده واقعاصحت‌نداره. زندی‌بارها تو جلسات با مدیرعامل پرسپولیس حاضر شد و گفت حتی حاضره با همون رقمی‌که طاهری رو از روس‌ها گرفت…</div>
<div class="tg-footer">👁️ 53K · <a href="https://t.me/persiana_Soccer/26624" target="_blank">📅 18:00 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26623">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mYRktDD5v9578o5e4KqpvG1zqb0WESRzLEkRO1z7gjaFrjiYMftqDONLhKwSLYvJepNTqNRSDP2x0iVYwB86_-P90lt3Ksj_p3qUABkAC0qOoFrVK8gtFY9LBN1LbdHgffPFcs4udCpDIWtm7e5XUEQ0K7f4Hum3VF1jH2BoBAkmDIUFrMgG7JCiYBFRbUA-2iHPMgx6Goe8qWxllL5SLxufSlf7NDLizaZfUxxwO50uO2Gep8KJ49QjnfGd7WbHH8JZLd0K3jLLLroAqG1IE14zKlpgQEYX9zwJSVqoWVtpVtbzXGnon-Jqj60RyrE5-T9rR3lPROp3wF0Sk3u5aA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
🇪🇸
🇧🇷
خوزه فلیکس دیاز: باشگاه رئال مادرید برای فروش وینیسیوس جونیور ستاره برزیلی خود رقمی بین 160 الی 200 میلیون یورو میخواهد.
‼️
آرسنال آمادس تاحقوق‌هفتگی بیش از 450 هزار پوند به وینی بده که در تاریخ این تیم بی‌سابقه‌ست!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.2K · <a href="https://t.me/persiana_Soccer/26623" target="_blank">📅 17:34 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26622">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ag9Zo2borfYRA5NtMqaRY9rWREmp4xKuuF8hcEOdPrsB5Y_6aIr80R1n8jrvRFdWoyUKMfvmF43edJpk0JThM2SdbUtgiAyPiKY93ZgSbTUQBiuDpKbzIPshtCDRA4kPwMEGmJmHr2VUugEM7qpp1fdbxMOrwhy7Zykcx-lSeaHd0SKoUuhOLecgF_CCTNThylW3n8Ycos95saHy2JAlGz9syCAOHlyTsVlCC__Bes77Ea8xVVMqyEoKVrtqI5H5Z3izD2jI5j55wKPsLt9XxiqpVQCtFX1XZ_IinG2uQ9bFu6sK2ZJbnqVQbGuxcLrYVaEiyZjk_m4ZReWImThoEw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
بااعلام فابریزیو رومانو و علی رغم شدید مایکل اولیسه به پیوستن به‌رئال‌مادرید؛ این ستاره فرانسوی این فصل هم دربایرن‌مونیخ موندنی شد اما تابستون سال بعد به احتمال زیاد این انتقال انجام میشود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.6K · <a href="https://t.me/persiana_Soccer/26622" target="_blank">📅 17:25 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26621">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YAPTjzae1IcCUl3Nj17IXKk25bvtUCb4w9MgUlleUSfk4Rin6cq_d7gR_yXKXHgWythCPL8xWaSbV9nSbnrIusQ2a05_0Rq0rJ4zXCcCd9gg1w03Vzwu93-W4Ehim1yg6AxCKqiDCpFnLpVZMvlGMwHzvvXh3v9Vx5O2CBCLjz16QobdcXLKjxcaQSI2QLTz_H_wS87qtBhphULIxtR6Ha8KuD3jDjLYHfuI6wYlqZ-fKTXoCYdGophxXJSkvww1YIdNBFrdM8_QJvbfjk_HbubaduTyCs_zNJZrbTF6kwmaDQ1k5Cs-ufvAUYjDDRS5bX3EajiakJhfO7EVifQNHA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🇵🇹
🇵🇹
فرناندو سانتوس‌سرمربی‌سابق تیم ملی پرتغال:
حقیقتا من هنوز از این‌که رونالدو رو در جام جهانی 2022نیمکت‌نشین‌کردم پشیمونم. ازاون زمان تاالان‌باکریس صحبت نکردم و رابطه‌خوبی نداشتیم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.9K · <a href="https://t.me/persiana_Soccer/26621" target="_blank">📅 17:15 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26619">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a1a0b40618.mp4?token=BgZS6jp4js50OrhJCXA5EfT4adUqi6LyhGbErTm_raRMZeJmdTBZRZ3GZGb7dheG0fGsUNeOTIEuG2QPsPVXFDVM87rqU5tDxzpwlLWJMbZW3oa71XqHtGaEZ1io_ZjTb5eyGPO4Skp0vUQRIOYjiq8vUoCgDjXd1vls4UyGx_NP-G8zA_P0NavF71xmzIKW9yrhZ_RlePuqTxI45YNJKx30QCCDedrfx_fd-KYFNeCz5RiTNG5E0rvYCcErvwcZkg7KDp3TifJbzsK599-_g4U0MGV09gypKQOnjszPN5xDe_gS4swdWb4RV8yZz7nTfkfWcytyZ7kvN0OFko69WA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a1a0b40618.mp4?token=BgZS6jp4js50OrhJCXA5EfT4adUqi6LyhGbErTm_raRMZeJmdTBZRZ3GZGb7dheG0fGsUNeOTIEuG2QPsPVXFDVM87rqU5tDxzpwlLWJMbZW3oa71XqHtGaEZ1io_ZjTb5eyGPO4Skp0vUQRIOYjiq8vUoCgDjXd1vls4UyGx_NP-G8zA_P0NavF71xmzIKW9yrhZ_RlePuqTxI45YNJKx30QCCDedrfx_fd-KYFNeCz5RiTNG5E0rvYCcErvwcZkg7KDp3TifJbzsK599-_g4U0MGV09gypKQOnjszPN5xDe_gS4swdWb4RV8yZz7nTfkfWcytyZ7kvN0OFko69WA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇸
تاتیانا دوس‌ دختر هکتور فورت ستاره جوان بارسلونا و حامی تیم ملی اسپانیا در جام‌ جهانی 2026؛ گفته چه آرژانتین چه انگلیس بیان فینال قطعا اسپانیایی‌ها توان‌شکست دادنش رو دارند.
⚪️
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 56.4K · <a href="https://t.me/persiana_Soccer/26619" target="_blank">📅 16:54 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26618">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bT1o0hkAGDlKcjGAjm4TJQcHCS9hR92cbuCECoJOJf1t7vhO8DnCh2Jm1CJap7ZLihllT3Jqdz_8kKtD-jcOo4my1pCjeUASuV7KpFALFnOE0h3f3n5BvecH6haxmv21yZtiI0qpaz8NIW2S0PXWgn6GEwkvepLobI2K-Su--upDXZalSn8OWSO2c4NlMLh2WKWRpwULNT7aZtZcnrhg1gjYG0wGq7DZZX86hKxDTDLEbfImZB5JfTOx9KIHnwaoXGy5eVu4hkF0lknYl8-2I5AQdYDqMx5BDSCMVcLOhdJP167qM35MJFS6liSET2PMrU0feRDBMXhk-ld_dvS6bQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
🇮🇷
#اختصاصی‌پرشیانا #فوری؛ محمد قربانی ستاره الوحده‌امارات‌امروزظهرجلسه‌ای یک ساعته با منصور عظیمی مشاورمحمدرضازنوزی و مسئول نقل و انتقالات تراکتور درهتل‌المپیک تهران داشته و برای عقدقرار داد به مدت سه‌فصل با تیم‌تراکتور به توافق کامل رسید. عظیمی به قربانی…</div>
<div class="tg-footer">👁️ 57K · <a href="https://t.me/persiana_Soccer/26618" target="_blank">📅 16:38 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26617">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ELZqOE0yPL-Q7UazML-x7kbIVwO8IT8n5Q_mUHkE3SHuBv_fOdE0Ag4ugzPZ-OCKPAjCR9zMh2Xr1NxRC4_RL7SR20v4eUV1Z8Tf2YE2yzkItCRC6wSfFscyPEk4ckHSCkWLAyKmm24KGgUHepEZx60V0jYHaQLNNS76itSHpsLQ4rfuDsz3Om3GY9NtXdf-Tfg39MpaMRnAe7nx-c22rhZF7dy8v5ROf7f57J_2w2ScC_tVT0E1yzLpIHdP7nB1TWbgG5kdaDhlO0cxxsugkBJKvYlbF7tFwkJld_tjWCjoeFKXLff9DjGZHxirdBpESu50e9mlbk39K98JKtWGqg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
🇮🇷
#اختصاصی‌پرشیانا #فوری؛ محمد قربانی ستاره الوحده‌امارات‌امروزظهرجلسه‌ای یک ساعته با منصور عظیمی مشاورمحمدرضازنوزی و مسئول نقل و انتقالات تراکتور درهتل‌المپیک تهران داشته و برای عقدقرار داد به مدت سه‌فصل با تیم‌تراکتور به توافق کامل رسید. عظیمی به قربانی…</div>
<div class="tg-footer">👁️ 55.7K · <a href="https://t.me/persiana_Soccer/26617" target="_blank">📅 16:27 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26616">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Jy_Rw3zqdlrZnL-HKlqGnGCle6Q57vrVuhJiUVLcfI2xXY_g5nrO2GDiF7ZDuSkfE3uBrPSjYLNmCy7Wj7YIxkHV6WWjD1J5omQ-vrRTSVq0NP6jwh2DJv2eekX4NTo_E3PsmQVfxx47BZU6u-YQmvo-lPuhHvv0OQpriXbfIv0zTDOGeevX3z6bTng3EtY80HZfufbqrHJXtzJedoly3gi3A7fPea_Nv5z-STEcA4EmJXQv3SNyjfTzymmrbbM09MQWPBj34rq0kQoLMRtHoj6rwx2jKJvt2FxCJALv9j4VFbqAnR9DUqEXx3o5-sa9lx23DNOff2X5zPXBl7byig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
🔵
طبق اخبار دریافتی رسانه پرشیانا؛ باشگاه پاختاکور ساعاتی‌قبل با مدیریت تراکتور برای جذب خامروبکوف‌به‌ارزش 800 هزار دلار به توافق رسید.
‼️
درحالیکه مدیریت تیم تراکتور با پرداخت رقم 2 میلیون دلار برای رضایت نامه محمد قربانی مخالفت کرده‌بودحالا بافروش خامروبکوف…</div>
<div class="tg-footer">👁️ 56.1K · <a href="https://t.me/persiana_Soccer/26616" target="_blank">📅 16:20 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26615">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nQeWceyNZCn6TFDTcmQ_45LuMR3rYS0sZJyhdbxPp-2Kw_jhISbNyfVAL15jl2ROwH2590Uz-opVBTV0YzFGOltVLgI9G6wKKHLfu0PtDIPRe07yBxJqWcw2B_kDab8-zf6F4Dsa-2Wr38Rz7pSFnhUHYuvY1HzmchneZcD592Hpl3qTftEA_w3gJRY5OSJyHmXb03YBRKHv4yBC5dZwUQUNEwP3QtoOAbkB-tS8Gf1EdxmIERtpPJsSMum-DiPZiSm9EKLRlJDzrfbjIHFa8qs4SLeyijd1v1ZUCTSTNSQcACImKenTZ6vs-uGTdQx1jWOMCjY9DKcHqb9iSFUqUg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
🔵
طبق اخبار دریافتی رسانه پرشیانا
؛ باشگاه پاختاکور ساعاتی‌قبل با مدیریت تراکتور برای جذب خامروبکوف‌به‌ارزش 800 هزار دلار به توافق رسید.
‼️
درحالیکه مدیریت تیم تراکتور با پرداخت رقم 2 میلیون دلار برای رضایت نامه محمد قربانی مخالفت کرده‌بودحالا بافروش خامروبکوف بزودی برای جذب ستاره 23 ساله باشگاه الوحده اقدام خواهد کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.3K · <a href="https://t.me/persiana_Soccer/26615" target="_blank">📅 16:09 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26614">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rxZdM5AI6NT8ajXt51d27zK6v0hal0RM_RK5pDwd7TLo4Nlmj8VknZPUGoCWHTTfcklcGu89csizb4ID-IYPvdG5foyLu3UOz5LojzI4npFPKIK8YJMIDqnOznHgYLZ_9LFNVE2-DUkIx7VpfQc6ztztFk3CCk7itZnPx0R_FmU3TEBphh6NEB2gSTeKWD8vsbv8ZRuOVkhyUD1n_JlcQeV8sfJH-LCP4mqbYkCTJZpOXR-yVa2CLj8gRCkFnat5hbeWfFmijVgDPQyI1JETvrW8SVpyvKMGUBhJFH9bYRSlouvFtMnoXwxt774_HTDjR90Qwx8C34muI2xVCjV9Iw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🔴
فرصت 24 ساعته نساجی به پرسپولیس! اگرپول ندهید دو بازیکن راهی استقلال میشوند!
‼️
علی تاجرنیا رئیس هیات مدیره باشگاه استقلال امروز ساعت 11:00 باشهاب زندی مدیرعامل باشگاه نساجی تماس میگیره و به او اعلام میکنه که حاضره رقم رضایت نامه کسری طاهری و دانیال ایری…</div>
<div class="tg-footer">👁️ 57.6K · <a href="https://t.me/persiana_Soccer/26614" target="_blank">📅 16:00 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26613">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GnFpSnt7Yt6yvOC2I3GBXOoQ0-P1vAqsmz2IfXcNChT8nFaz8CBCBVLkIbL-CMnKYi9AUo88F8p2iN9WxfK3Ig2NK4pjo-yXiuLMESLiUe7BdsBmDTrP3FGhCEdQCQDg5BJs5BHUqAPeAvZ7QFJ_RfVsl5-4_NTLXBwtUi9wcZZ7sXJFIiDWS2yyHIzDD_jkG82Is3-SKA5Wqap7PYK_G7XzGm25BgI3OEoRsG5gRuyJ2PvtEo9Xb9KiBGkna2mEyb0yFp83xvvmnnJb6osuGI9gdzog0QAzzMYdFb-NttTNOAxuQD2EhQoSE3tPvzMxmmJqKM6CsFr3Y34YnjH4zQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟢
👤
طبق اخبار دریافتی رسانه پرشیانا
؛ پس از کش‌وقوس های فراوان و مذاکرات با باشگاه های لیگ برتر؛ دقایقی قبل جواد نکونام با مدیران ایران خودرو برای عقد قرارداد یکساله با پیکان به توافق رسید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.8K · <a href="https://t.me/persiana_Soccer/26613" target="_blank">📅 15:33 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26612">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RaRqvlP4TcN78UJU5GRhvuRWdpqrFe97f35KJfSvma6T8NE_42L7w8TlwR2-PsCPX-IEgH5EzM6SIUinPfjbUEHhPz_DzUylGtvQrrLkNu24s4WZUIAq-92DrNLNCodgP_0JOnqBZDTf32dFA7thXLgY9d6wl9gm4ggVSkKgZUBOAZ5u6dRnFSA2duLumLoZrXGOBwXpwe0eYcDr4gC8nv_sOAgolw66lsNqnm3IPywzECzZlKgTHJ6D-uvq9zUmUsTRQn7t2uRriaL0KcRMV9tgHJ_khR6va_s5TadMbG11Sst2j5-8tzNNmJhdcP7KlLZC2kq7GdF0fdLfaPD9hQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
یان دیومانده ستاره جدید رئال مادرید بعد از پیوستن به این تیم این تصاویر رو منتشر کرد تا نشون بده از بچگی فن رئال و رونالدو بوده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.6K · <a href="https://t.me/persiana_Soccer/26612" target="_blank">📅 15:04 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26611">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aqb_H1IT3DBatBp5BLORg8vmlFSak_ZfGDfPQ9dY8eM9J4ZCmMSI_c8e90e92IUZgU9sywMr-_SANVwCb9H-vs8NsSoNcrv7SZDOPMK1mAcbFHmQhSJU5A8N_R6K7W9MS3rnREs2x1k9XgLSGd3wXbW4yQRxsNwVhKfb1lFtJOQG1_FFEJrNqdvfVCSkqDBaGfYs4fbdu0DpkuXxQoAQ_9_sfVMqy4q7406mB5LAzJq9pgPDp3jd7BoC77I09AK2hrDkunONfoCvEv5rCYD5dlccv3cSMXY6Bq8W6Xg5DZ3m-phbuY0FeEsLqmNwboTb7R4eAIvJOlMBJG5YnklBYQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
تایید خبر اختصاصی 14 روز پیش پرشیانا؛ با اعلام‌باشگاه‌پرسپولیس قرارداد محمد امین کاظمیان توافقی‌ فسخ‌شد. امین کاظمیان پارسال در شرایطی به پرسپولیس اومد که لقب فوق ستاره به او دادند.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.9K · <a href="https://t.me/persiana_Soccer/26611" target="_blank">📅 14:49 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26610">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HFxJ1eajt0knZUMbPd5xeIR2bCW_t77RBTTX6rSvHB9xAaagkGuQ3wFTPsjqJevz1yPkBUntbL6Lq3vAhGdP3w4f8kSIPaVeLFoU1geErsxFHTgGPyIho3qxnbXK1_VEAVb86DJtHFI3-H-I6UW_RZezFcEX8XtU-_Y8-E-aRlpFg0C5N_XJ8r4i2UsVzPrZIOQFUNKPM_UEdJdoVFk_uctBLxwXE_mwnGT3iAFafoSDASPwhRK4JpYiOX4TnoFTXhyJwSuVkDMvqkevdVLVWC8guhlHzqgPJenQNp9GmpkSJ4swBtiiQyvJKw13bjM7cPeGAOeiBM9clpCZKx6Qlw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🔴
فرصت 24 ساعته نساجی به پرسپولیس! اگرپول ندهید دو بازیکن راهی استقلال میشوند!
‼️
علی تاجرنیا رئیس هیات مدیره باشگاه استقلال امروز ساعت 11:00 باشهاب زندی مدیرعامل باشگاه نساجی تماس میگیره و به او اعلام میکنه که حاضره رقم رضایت نامه کسری طاهری و دانیال ایری…</div>
<div class="tg-footer">👁️ 60.3K · <a href="https://t.me/persiana_Soccer/26610" target="_blank">📅 14:39 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26609">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9b74811f44.mp4?token=THkwg1hjrKe2eM3vj33sx5wGH2viR2cJmHpQtJHaJF4YHeVrWtZCXBlJypHrffKdskwFprohqQgKlivDmTEzkh9qAcBK_VZb_c50hudDTDHFQ6oBHtAnS9qZbEDw7tFK-UPJsU-DgLFc2pRW7ViBvFwTOSZN0vjM6URyYD71oJh37x1d-0bdqipof3ooV12s8ZsxxaZEN9fjrei5KcLf7XuQUFhQZdZXmhVxN2G_QaLMagsNZCDJN-1bdTfawR-3O4iNsklRdcDCc8-2v-WVZ_F-Y5BxqoO_GV3f8js0hfTr7Iwqxz3AZZFdSsczXKwrFF1xFURLFzXmxg8F7Ef9Ng" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9b74811f44.mp4?token=THkwg1hjrKe2eM3vj33sx5wGH2viR2cJmHpQtJHaJF4YHeVrWtZCXBlJypHrffKdskwFprohqQgKlivDmTEzkh9qAcBK_VZb_c50hudDTDHFQ6oBHtAnS9qZbEDw7tFK-UPJsU-DgLFc2pRW7ViBvFwTOSZN0vjM6URyYD71oJh37x1d-0bdqipof3ooV12s8ZsxxaZEN9fjrei5KcLf7XuQUFhQZdZXmhVxN2G_QaLMagsNZCDJN-1bdTfawR-3O4iNsklRdcDCc8-2v-WVZ_F-Y5BxqoO_GV3f8js0hfTr7Iwqxz3AZZFdSsczXKwrFF1xFURLFzXmxg8F7Ef9Ng" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
پوستر باشگاه آث میلان برای روبن آموریم سر مربی جدید روسونری؛ قرارداد سه ساله امضا شد.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.8K · <a href="https://t.me/persiana_Soccer/26609" target="_blank">📅 14:26 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26608">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XFmGtJwmL8FMxKNoryd_fFrZL_RUIrVPyt-IUXQoo1Y4Lo55c_cEUWF9cI82aZoDaUko2BeU1PANEnJ_vCitIrZ5wWcZjFhJo5pei03prNlEDylY_WT7VXmVu45Opwb-Ggxn257RXTY72lGCB6TRMQcQR7SMk_waL0l1p9tfm2Dy_ilzxTvwCYXptnNrxT68T9jkltX5eI90es6wP-AJQ92nWkiS1xtZfjrOT-hGmZiLcFSgW3aBjdfNUXdHi4pep3XF_V57SSMzApsOPWNKgeFXGv1xOVh9yyB7BeI8NN2m1elqXFIehjx4FVBYW83-HL0d5LT-jjLpqcxAqjPZ0g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🔴
#اختصاصی‌پرشیانا #فوری؛ باشگاه نساجی دقایقی قبل رسما بر سررقم رضایت نامه دانیال ایری با باشگاه پرسپولیس به توافق نهایی رسید و به‌زودی رضایت‌نامه این‌بازیکن رو صادر خواهد کرد و باشگاه پرسپولیس پوستر ایری رو منتشر خواهد کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.8K · <a href="https://t.me/persiana_Soccer/26608" target="_blank">📅 14:11 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26607">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kzJPDO76Cuq3YdLFlOxzyhECHb1naH3RUIqwYxnbPM0cgzNWTGY9JFve5B22gQX9nGFYQ0IPGdDKhGHuf3r2CXikyWMkBkTRP-oHblKnMzwHieguh2E_NQpc7pk1lsWF1TN5cN2Ou8HDZPe3KHcxRSNZ2p-4KdqIDOaAgcUyR9Z-HPzaWsqUN0ylqw7AsGw7JLTea5iPQ7PCIIGC5meQHrlNokDlD_l_JBjJY0hzH4TySzyakCtyRANnfxo7Gufmwxc62y2U1MAyJCPvBlKRt5RMEfzZRqZ_ccw54gYT8BpEG6T_iv4QhQhw7Hxb9YYk6cc5nsUGqh-thGgK6tjPsA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
جایگاه لیگ‌ های آسیایی از نگاه Opta Power Rankings؛لیگ‌برتر جام خلیج فارس ایران در رتبه پنجم قاره آسیا و 61 ام جهان قرار گرفت.
⚪️
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 61.6K · <a href="https://t.me/persiana_Soccer/26607" target="_blank">📅 14:08 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26606">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cTe20JznA8nAluShSbLcx1da8_cTzH_Cz7-rzcPa92cNFZsqgAad3b3dagKa6CH58Jc44hfqKAyj8AxhnNJrGXHlBcd8k87P67Dez0gz4IqbLiVodudCTrh_XT3vR7t0JgXV0_xk9QH1SR86jYgypPurq-74e7cuiR8y_9fGa0Zk7x1s9tfpyhCBSK9sfSpRo6Tg4Qbe96Aw5Cj5x-PhRPd--Q6b68VnDbpuZHjk0hyFItTlZUgdl9gbCWAeq241r3vM8g6DngqIK8OiZUAqvY80ffafBR8kRGuoh6FrPSbjL0M1lCKige7zutfb-Szm5e8tlWxuBOcg_4cOkI-MXg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
طبق‌شنیده‌های‌پرشیانا؛ باشگاه نساجی مازندران با هومن ربیع زاده مدافع‌میانی 27 ساله‌تیم شمس‌آذر به توافق رسیده و این بازیکن‌جانشین دانیال ایری در این‌تیم خواهد شد. جالبه‌بدونید که ربیع زاده با اینکه مدافع آخره پارسال در لیگ برتر شش گل زده بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.1K · <a href="https://t.me/persiana_Soccer/26606" target="_blank">📅 13:42 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26605">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NfDnDj-psI8Hnk-805LcJnfRBacOtAHb8BOzbx0lwyJIO6W5H-ULblNtAE1FmK_TqC2vw_kf8_yHgy1P3UdOQ7iT8E6w9o8fJ-OSXASvkM7BZfEOCaN2OIdBM0p4Ndti8vaOzNrLjxEm67piu0ixoUTlH2WphtuAkNE9pw6fXyXSHETLYbLJaVtKsQBOb6-9EdUUhbP9mTyE_T65qIMB5_7HWY009GycYPZUP-jO0Qt1cSrsBpfYNJv4FuKLwJV1NYMkCPzRfiXoDaFg07oPJjG91FxZpJv8MakyhDLIK0NkiJYOVS-t3v2nfwIo5RX5o7048mT8EuAuQl1vgkSxLw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟢
🟠
فوتبال ایران فوق العاده‌ست
؛ داوود نوشی صوفیانی پری روز رفت باشگاه مس شهر بانک پیش پرداختی گرفت و رونمایی شد. دیشب پول رو پس داد و امروز با ذوب آهن اصفهان تمدید کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.8K · <a href="https://t.me/persiana_Soccer/26605" target="_blank">📅 13:36 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26604">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Vw9oyMGhzo9uC6w6LnxOUHwWvfKqNkk0q-k91FJJzxcisUj_zr6ucxP3eGSCaPJdRj5XMt7oQMsgSLztPXsdxbzk1YYqeLgMr7Fw_3ndMBq51hCyMwBHL_TlNyWt-vyXSI0_PArRmN5xPKT6Un40Did-bLhU10jyfB_FohGpcx7Yz3MnuFSM4b2PksAGsk0Hz0VjFmqM1yF4nJpdkbMlQTP-xMVtJNgsiZXUlUCh0eCl1v2xqC7OsSS6Xr8Y-STaLehoDrVFx6maD0fDAqeGSqz4CBDSmLb_zp0w8BNEjE9FYuGTngoUtG4SEn6DKX96FPUb4WLRe-tQUKX8c6mfAw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
طبق‌گفته وکیل‌ایتالیایی‌باشگاه استقلال؛ ظرف امروز و فردا دادگاه‌عالی‌ورزش CAS رای نهایی خود رادرباره پنجره‌آبی‌پوشان‌خواهدداد. یا پنجره رو بازی میکنه یا بسته میمونه تا نقل‌وانتقالات زمستون.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.3K · <a href="https://t.me/persiana_Soccer/26604" target="_blank">📅 13:20 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26603">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f0cb160c99.mp4?token=UEToYpVwq_K9GF-sSOOPUYoKpyarONKkHwOs238fKOKTj7T3mzNtZCPxun6zbvqgbxlPsVzMFhBOtPpyTyqgF02Bwf8bNsTX2-26oqf-sW2MmOYt2OStxiNZ_C6D8FcEZyYVreQcsEcM2kspAx8_FxarxWrRaYgtml6G7ZqHIV9TneSuem_bZavPAvpFcReM44JUQJ-R1l0aNaPWplh-zgr7yMjGyk4aqfUi2ZakYA5_OP-QqMCrQcdZeabijNxcJeIe93_ZzSghwfTGKNdpbKZPD26wz_OnQJzwS9M8G_zL7F67NieC4dUKbuAPXVjp01uceUtLGi9ZJEqWAdTzyQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f0cb160c99.mp4?token=UEToYpVwq_K9GF-sSOOPUYoKpyarONKkHwOs238fKOKTj7T3mzNtZCPxun6zbvqgbxlPsVzMFhBOtPpyTyqgF02Bwf8bNsTX2-26oqf-sW2MmOYt2OStxiNZ_C6D8FcEZyYVreQcsEcM2kspAx8_FxarxWrRaYgtml6G7ZqHIV9TneSuem_bZavPAvpFcReM44JUQJ-R1l0aNaPWplh-zgr7yMjGyk4aqfUi2ZakYA5_OP-QqMCrQcdZeabijNxcJeIe93_ZzSghwfTGKNdpbKZPD26wz_OnQJzwS9M8G_zL7F67NieC4dUKbuAPXVjp01uceUtLGi9ZJEqWAdTzyQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
علاقه بسیار شدید غزاله اکرمی بازیگر سینما و تلویزیون به مهاجم سابق استقلال: غلامرضا عنایتی ستاره سابق استقلال کراش دوران نوجوانی‌ام بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.7K · <a href="https://t.me/persiana_Soccer/26603" target="_blank">📅 12:58 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26602">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GlwjyIr8kXFlzB06CfGIyM8dk1f6s2QtWCXptW4sMqI_3ixbElh-M090X0sjHSNk-EWP7xhYCFZxkD6FLuDjgQPp2rOpjPWM1f33FW0hhTMvxKMoEkHcLgwatY8l7gYOXpRqQM1UGEezuhsBo76G__y7NaUrxI8elgvgNz46V2w6jixl9eQlbWNivSmA3JUPyEouvv9SLnR-qJILGg3zWJm6HoAstaEjQQ2xW5b9yqzZQmNkL0D9-nH2oAu9G5o3FWWWa9Bw5MZmxwrfZLT3qYdAKmkI2tTbrmF1uBC9HTidyWhSfP2NAxAOeAGbeapKLTkMQOKLOYyUQV4zsqKBPg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
ویدیویی‌خاطره‌ای‌انگیز ازسوپرگل‌های لئو مسی از روی ضربات ایستگاهی در دوران حضور در بارسا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.8K · <a href="https://t.me/persiana_Soccer/26602" target="_blank">📅 12:52 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26601">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/e81pFg6aR37d5J5zub50rUsiIbC3JP4zYZM1VumajLncKEFdVh7FZrLvF7IannxaiSyIviC6lh17lrINw1xw7mx5j0OMKcs-9LJFsw4I_OD6NUJQXx5Ip-zFrh-knQ0NjY_nm2dFzX3Eq2uEinCdguTxcNXFIkFCOt3kL-hGgnZuCmY7Wmacmmi5lClAQsWE8cvPkh2LZtJVgZsoL5LtnppEFhfeBq1GwGaKSqo5cRq-EnG8jY2bCTySOz9ZTS7oRJ5HwUCU_GYa7vm34vfebCfydVL1X1XH7bTnlTVM5MHGTShnB0Y0UhpSo0TKTvaDWTRxWMmHtEP7fwmXp4_WaQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
#اختصاصی‌پرشیانا #فوری؛باشگاه استقلال باردیگر به منیر الحدادی فوق‌ستاره سابق خود تماس گرفته و به او اطمینان خاطر داده که بهترین شرایط برای او و خانواده‌اش در تهران فراهم خواهند کرد و هیچ مشکلی برای او خانواده اش پیش نخواهد آمد‌. بایستی صبر کرد و دید منیر…</div>
<div class="tg-footer">👁️ 58.7K · <a href="https://t.me/persiana_Soccer/26601" target="_blank">📅 12:43 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26600">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NJppZEh1rAozBOVKZnGjSpeGk6jgK2hTWY_iQuU4Xy_1IzakLm6CY44YVOwNqRjNQD7HpXaGV6XMT5S5yaW3tZcL-aKm2Iy2ZfnLDMOE00W5xMiRXlaWAlN8ApfjQ61l2i_iEOfu1PQwzlmCmARYfCIo1bX1UfGu34_Qvv4RyiF3rQ00J-q9d64alkpfLXZVXMcuisHHU8m-z2WROdLRRmXXVda5bdPihd1z9ES5DGCj_bVILD-sToJHr3Ew4R4GuppwOnVCQQmKg5cJDEcxg7RAWYtCvzftXH7BMvIMLL_iJkMGGYV-iKQkST16JJhmjt-PWqZTwotAewaouhmFDA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
رئیس جمهور چک در اقدامی جالب و در حمایت ازتمام عکاسان به عکاسی مسابقات فرمول یک رفته.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.5K · <a href="https://t.me/persiana_Soccer/26600" target="_blank">📅 12:34 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26599">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/p1SgBE76THrRm-_ezmk0EKvetg9w9GzGpn1vfS87GJzyUJ1y921ok2weU367YfkWulZ4li8eHIJQjiqPsnat7YIN9HxSHtOx1PWKWNurzHcX-9uJwutKu8THPZFsYyHOJ0dlnOgphyL0cguDu5lo37ipwhBpsndb3Y299jihSXTXpOmyn1AS8fVtPjN7H_GLmkYhiCkfd0pJq9C2y1v59KKYg5ja8u382Yaf2jAW1c7iVLy7_eRJRULXCILtiEIWZhms8v434ITGMsWVK4pBR8yatzEJH1LZcHrzqSwONfe8v5CWSPb81WTmn9w7gQNLf5oKnGlLx0hPKp9mramhPQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
باشگاه پرسپولیس صبح امروز به درخواست مهدی تارتار؛ باارسال‌نامه‌ای رسمی به باشگاه تراکتور خواستار جذب صادق محرمی مدافع پرشورها شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.9K · <a href="https://t.me/persiana_Soccer/26599" target="_blank">📅 12:34 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26598">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DjzfZK0v0Rno8-1xMr5AFOwljZ4er7XT7q-QbCF0rgasbl3ejw1YFzlkIyTWgI7QXzhscZKYwRYiA0ZDfE3mEGEv--XDcNb3ddZGLCdsfYEqrHJyHpgs6jikAcAyDDevIBSLzb9Oih25Xis4AS6GEx4vUQqpnAeFuSXXsmxGT21NoWkv0XIhlqudk07ffe8xU8eJi5FcUmJi3DtnDCJcOObGX1Lqf0shxNUQb2d0RtVNuHEC7i1hfFljcXBin6jlhyaoeB7gX8Zh878CilKREQfS0hfMVORfe3dt-Wyjkvcje62pvOayvFsdIksj5tL2rOm6yMq9yQ5finKBwkm-Rw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
پیشبینی در سایت بین المللی ریتزوبت
1️⃣
2️⃣
3️⃣
4️⃣
1️⃣
2️⃣
3️⃣
1️⃣
2️⃣
3️⃣
4️⃣
⚡️
فرآیند ثبت نام ساده و آسان
⚡️
آپشن های متنوع با ضریب بالا
⚡️
امکان شارژ حساب با کارت بانکی
⚡️
شرطبندی بدون لیمیت روزانه
♠️
کازینو آنلاین شبانه روزی
⚡️
پشتیبانی از 61 زبان
🎰
بونوس 100% اولین واریز
⚽️
بونوس 100% ورزشی یکشنبه ها
📲
اپلیکیشن موبایل برای اندروید
🌐
http://ejh7qy8d.lol/L?tag=d_4828009m_69797c_&site=4828009&ad=69797
🌍
ریتزوبت؛ همراه شب‌های فراموش‌نشدنی ورزشی
⚡️
@Ritzobets_official</div>
<div class="tg-footer">👁️ 57.4K · <a href="https://t.me/persiana_Soccer/26598" target="_blank">📅 12:34 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26597">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ei4VHRDfuaOmDJ0hBO7Q9ylwxegue-VszCHCPb4R3H6cIBc0tW8yQB8bufcmDiBblo7MR5CXu0e99GEzp78SFcd5MDSMHa6yGCjNRXCiZFfpgSyd-r1txgv3QEiYik_KFJ7npzFjjMzMQkI-uajZKILBeHKjr4YET4Px624Bek5kN7sEHYiVSsTRuDJ8m1rIV3zZC4JDqMqgfrTnkgxnoB6D5Kj9LyKIbrFTVXlion9RKNfm0kgPuWBe2ARyfflcKfTDJ6ahJPVg4VIqQvIdlmw3HqN4lG7afRG62tTNz4Isu8BrnbQEv1eK6sLzTUy2HEkLTKzdR7IseRbK71bogA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
نشریه‌گاتزتامدعی‌شده که آندره‌آ پیرلو درگیر یک پرونده شرط‌بندی درروسیه‌شده و به احتمال فراوان فدراسیون فوتبال ایتالیا قید توافق با او رو میزنه و روبرتو مانچینی پرافتخار سرمربی آتزوزی میشود.
🔘
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59K · <a href="https://t.me/persiana_Soccer/26597" target="_blank">📅 12:06 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26596">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2a36a095cf.mp4?token=ekwEQI1klO8-YUu3z33sxJShXfLTXMy8MAhkU8MB9sB2XfAF5XQ1ZeF10bZ_lAF_ybh45Mwfx7i_jOI7252QIekpmlcKJxBgI_Z6nbEHRt-e1LHCwBFa_tB2yZDVglpyM2Ahig-rB_EdbbnbQkLGgYBx0noYyGzNPbucMDl3wIgazwGchk9xb3u858L7SLfpMtyiy4jMdDTSGTq5r1unJoUNQz-BtbrSvVxWd9S3x9_LP8j4f0gLSU1gaHqpy9pOnpQ1aLkJtEXhfH-qhr8VNyFLX3s1IFa_C4q4RnnWxmJAZf22FpSCduI5O9-2SuECLEC-T7_4ryk2Hl_FCX0GyA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2a36a095cf.mp4?token=ekwEQI1klO8-YUu3z33sxJShXfLTXMy8MAhkU8MB9sB2XfAF5XQ1ZeF10bZ_lAF_ybh45Mwfx7i_jOI7252QIekpmlcKJxBgI_Z6nbEHRt-e1LHCwBFa_tB2yZDVglpyM2Ahig-rB_EdbbnbQkLGgYBx0noYyGzNPbucMDl3wIgazwGchk9xb3u858L7SLfpMtyiy4jMdDTSGTq5r1unJoUNQz-BtbrSvVxWd9S3x9_LP8j4f0gLSU1gaHqpy9pOnpQ1aLkJtEXhfH-qhr8VNyFLX3s1IFa_C4q4RnnWxmJAZf22FpSCduI5O9-2SuECLEC-T7_4ryk2Hl_FCX0GyA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📹
ویدیویی از تمام‌کنندگی محشر لوئیز سوارز فوق ستاره سابق بارسا؛ یکی از بهترین مهاجم‌های تاریخ‌.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.5K · <a href="https://t.me/persiana_Soccer/26596" target="_blank">📅 11:44 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26595">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Kc0_e-jPDaBcQeI141Ouymn1WHF9azI9QxoBMqklQtxWwQIVesE4KrAVQsulA9_m8XzuI_fSrsEoIS1eHYmUaWhazKTSqRY7jTB_4ICVQg3N6A7QHTSiWUL7eNuEIhDIY6WBFpgv8fXCa27tak1fxdGGfMC3y1xKfWTXV0D9fcBmI76CGnLoQ6_N43Td1DZyC8lWiG6O2oQajl_qKBe4lXoh9u2fkhkOT2HW2mfzn-P3K_3qqQh6Qs32btsfjxZfJnNH4oPuLaxI4nntAc4rNRXrT0nMkqNozIKmobvELQzo-QvKBjnKq5p_Kn4XG-AjPqbv4a7XTAybqkQyBFP1Zw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
رودری اگه به رئال‌مادریدبپیونده؛ احوال‌پرسش با وینیسیوس جونیور در اولین جلسه تمرینی این تیم:
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 60.3K · <a href="https://t.me/persiana_Soccer/26595" target="_blank">📅 11:20 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26594">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vp0pojGe3F8074hzTW-xHen0BaltUP22NILNPX84XLzQw_PCUZLykDkjwuKrBVknXCwC4-GCdb1ppeU80ZgHNEEv0k51uNoKTCdbcUQ8AnQ4vY-jB3pg8y9jd_n_3NeOaq1FJuCKQdy83_MbG6zC0HbTaNC5DC1qMw1mMVAxBbtnKFuaF9O9s-a2EjfYJgjk4dGXxBPyiZOmS_CzioBEwpGPo4nY6AgMnpp0rHkmS9N6q6s0EERlbU2JR0dqNouTPX2Jiy55fbX3V4E7fnG2xiAw7FdSp5uwhBP3-QqobRkYqA5__jMA2zWs0FZu_h5uFNtpVp9ivA_3i3g9P7wshg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
باشگاه پرسپولیس صبح امروز به درخواست مهدی تارتار؛ باارسال‌نامه‌ای رسمی به باشگاه تراکتور خواستار جذب صادق محرمی مدافع پرشورها شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.9K · <a href="https://t.me/persiana_Soccer/26594" target="_blank">📅 10:59 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26593">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DFIr-_G1HKjyHabJnlc4DKmVb06eTyXGsb6RTH0roASYCxH_SI1fbwWAyMyDd5qKg4iMtu0_urEKcDTt8TCqewOuD1_3KfOsv-KmoP_kOXiNMwCAs7XIfoS3f3qJ3Pgz4ZOl_jTS-lmA12b523qHYcYNHSnoaMgeijF3hVKGVaBzO6MwjpbjEybn2F-ttwP99PivuRF7-ype91qU35lEDux7UjC6cvYXu684Wa3_rlfpq42LYPDHselWA8Sod-ydjfBYAKVyt_bMMGvrjaHnLkWXOPm_SroBmKKApo8CIgWCGSa075CiQlG-ihiK3rZXYqbO1i9-CoDDjMT0CICx3Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
#اختصاصی_پرشیانا #فوری؛ دقایقی قبل سیدمهدی رحمتی شخصا با محمدرضا اخباری دروازه بان فصل‌قبل سپاهان تماس گرفته و از او خواسته به گل گهر برود و قید حضور در تیم پرسپولیس رو بزند. قرار بود امشب محمدرضا اخباری پرسپولیسی شود ولی به احتمال زیاد راهی گل گهر سیرجان…</div>
<div class="tg-footer">👁️ 60.2K · <a href="https://t.me/persiana_Soccer/26593" target="_blank">📅 10:40 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26592">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Zw81YdWA31rXG5z4aRiF5S9gaRDbdirjpaDBKH7pstnqJXWmcjepjs2HuSID4Ojz7K6Dlxi9SRP9R6g-5GrGQBUHO5xt2h3LsEnYdE_JPw_sMIdDW__xWQlUK_NdwtOMfCmkp-r7AlT-d3KPVcO0IkjGkaSOlXvmGH0Henhc-LZevzEvqBvj2_mGc3ionUDfY3nDAkwoGjHUzj3eEok__xvInpGic0Rb0SZP8vI6GJzE3J7p5k2q9gioE8r1fwZs4fNDfbZJBSbAbj2sEqB3QvZuWf4UlgHpFaPwvZuHXy4wzB5lpK-hSdFCv5RG89pl_UvVmbK1wb33xkJOMqX6nA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
چیواله وکیل ایتالیایی‌باشگاه استقلال: روز دوشنبه یا سه‌شنبه هفته‌آینده دادگاه عالی ورزش رای نهایی‌خود را درباره پرونده‌باشگاه‌استقلال میدهد. ما مستندات رو کامل‌به‌فیفا و CAS ارائه‌کردیم و بسیار امیدوار هستیم که پنجره باشگاه استقلال باز شود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.6K · <a href="https://t.me/persiana_Soccer/26592" target="_blank">📅 10:37 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26591">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FLbHTg5pwNxGvTbPRQ2ev0HfxpCQjJLTdMqybaUxBrNnN51VXx0HzJ2lowHIeHrBkbvnAvsC-xjsXzKZ0-F91LklMYCbhB6nvsH1umr-AKLtv1XFdHCtBlMJ9lDnHU-BB_yzErPUIV5IivXCG3liybos4NpXtJr1al0drWBMTokRAfGctMWhddm0wfOuCX_6a67ZB7JjcaY4spAN9BWCjbDn3mh6KCORB1wGvBy8qKm0ZvKtqN3KUaHjd71wNxQxTXCzYW9g1omfBz1IhjyXbYNi_Y57EuHqHyLSCVKYbD0HRY_KmrDYfkNSQN7IfqBmK7cMwIdqAOFrcZ59NENWCA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇹
#نقل‌وانتقالات|باشگاه آث‌میلان با پرداخت 50 میلیون‌یورو به‌PSGگونزالو راموس مهاجم 25 ساله این تیم رو به خدمت گرفت. قرارداد ستاره پرتغالی باروسونری تا سال 2031 اعتبار خواهد داشت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.7K · <a href="https://t.me/persiana_Soccer/26591" target="_blank">📅 10:31 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26590">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BDSFUfpZcHBu6HdEDpywX1h89WHXj0UWjrpSj27xSLES8aoIFCw_1IMimXuv0EcMf4TYex6DBk_xmrTaEuYF0vs2LzOh9jTcf-Yn4qf37muXniZ0W6COuyMWgk3L08G_HL9ubfhxonQAHbFFLsU8YjW617A6uwGlPDh4UATTTH7Gso4JlOV2g3V-zfzZqG2fXQtdaZk6kNBROB9k5rkWnA8QINpEWd3vOlhaWKD2OL9sAy2r-5zCbRB7YHJUTULxNhyc6vgpdEq9T5Q-RGWmaEFX4TJiO8Mm6A3mKw2vXhF_MrSFVowcIu-lgoPWLgvYR5KH7XRcGPoGU7fRiwRAZg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
طبق‌پیگیری‌های‌پرشیاناازنزدیکان رضاییان؛ رامین رضاییان طی روزهای گذشته با پرداخت پنجاه هزار دلار به باشگاه استقلال بند فسخ قرار دادش رو فعال کرده و در حال حاضر بازیکن آزاد بشمار می‌آید و درصورتی که باشگاه استقلال او رو بخواهند باید قرار دادی جدید با این…</div>
<div class="tg-footer">👁️ 60.3K · <a href="https://t.me/persiana_Soccer/26590" target="_blank">📅 09:58 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26589">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/agfbPGNRWUCTvCwagcWcKeP62EnYU88-cIDr3vpjxQXFMgzGgsO-H0E7C1MFgXGg2tr4o5vRWKZuPl_u6dXdKKxjbbx5ZFYGu8HKnOi6B1dRIm1ykYCUMCRhIeUsjdtcJlx58879bf41TmGsm37J2Rb4u7NmMUPWFBlUpZlIjL-mOHxcsK07evTH-vwLuhFXCLGjmhsmeV5GlSUVu4_WKmw8mmKRyk_kfC2d2IXXixxuINJo9Gnuk40hf094IXUcVxBHk0WPBecjTekIP1WTWoHnv03pWbob_2IsjeNeF1XVgCbz6-0DvJYM7TXIGiejMU_E-AdJI1IIxPACkTJf_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
آرام جوینده در ادامه‌ مصاحبه‌اش گفته که سپهر حیدری تو روابط‌جنسی کم‌کاری کرده و اونجوری که من میخواستم هیچوقت نتونسته من رو ارضا کنه.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 59.8K · <a href="https://t.me/persiana_Soccer/26589" target="_blank">📅 09:49 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26588">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0c7b549a0c.mp4?token=bzmMf-kqPxF0eNFNrqaD9iLZW8j7GKJZT_hbDI6UAVXN_O3_1i1N7a8zefmL0ReaygBsN46JnlBmG9l1ezIYX9Ldv6pqR8ajedIex6VvPa3fS6eaa058o55Chmc4mA0L70i-LITu4BSnQwFP2eV6EBpShI7GwhFniq3SiLtoAWH6itCzFnI0J15fwO-4a0t5AW4w7TSkZzQ-xNyZvl6nGkxWDYzoPoTWPIDooHuIFHdIlG4n27jEXdLkMedUHp0bJ78-e64TKLSMTlkJ5KF3c3EhxaUZwhZK6YxV2tWm1Euy5FtS-ecwFBp64sLd0ZN6TwSBDZ2uaN9K1gZewom_Pw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0c7b549a0c.mp4?token=bzmMf-kqPxF0eNFNrqaD9iLZW8j7GKJZT_hbDI6UAVXN_O3_1i1N7a8zefmL0ReaygBsN46JnlBmG9l1ezIYX9Ldv6pqR8ajedIex6VvPa3fS6eaa058o55Chmc4mA0L70i-LITu4BSnQwFP2eV6EBpShI7GwhFniq3SiLtoAWH6itCzFnI0J15fwO-4a0t5AW4w7TSkZzQ-xNyZvl6nGkxWDYzoPoTWPIDooHuIFHdIlG4n27jEXdLkMedUHp0bJ78-e64TKLSMTlkJ5KF3c3EhxaUZwhZK6YxV2tWm1Euy5FtS-ecwFBp64sLd0ZN6TwSBDZ2uaN9K1gZewom_Pw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
🇪🇸
🇧🇷
خوزه فلیکس دیاز: باشگاه رئال مادرید برای فروش وینیسیوس جونیور ستاره برزیلی خود رقمی بین 160 الی 200 میلیون یورو میخواهد.
‼️
آرسنال آمادس تاحقوق‌هفتگی بیش از 450 هزار پوند به وینی بده که در تاریخ این تیم بی‌سابقه‌ست!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60K · <a href="https://t.me/persiana_Soccer/26588" target="_blank">📅 09:33 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26587">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fEvRindjG1uvSG_uvS476iRj-xZXbTXNBLU1Bo0i343mbD133YG1C2uKM60f5Xj295D0eB148_hqGhK3yjkQXuQwk05rpTcQRpUrMpMznwVh85bx7RoU8d-kUgWBECfndnoE6MhWADoBlfun5CdcvJysPdsBdeb5-yNuXAvFiXzIiPsPbiZYfYEM8_0iSxBphoeW6faUKwXAk3ekjyy_dc-aW9ZUDjJYXQDZWjeUKBHZ0Aksg_cHt05oookXBXf-8EZlSu75n47g8ns2jfxYtKpNslq5nzBcdv-XA-TUEWmr4dY3c_Ym4TPpCGmJBAiCVsvxE8ztC54sTK65K4bDUw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
مقایسه جالب عملکرد رامین رضاییان و یکی از مدعیان توپ طلا درکنار کین و دمبله در جام جهانی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.2K · <a href="https://t.me/persiana_Soccer/26587" target="_blank">📅 09:08 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26585">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/h61lDQl-Pzk231wpFM17JmxceGK9w7x8lFi-7Av9eDGLqGjcjc_19LYDz8gBcf1gET-oGR79aiojecrhEcK_biZGrGbi3I5F0VCtV21awCLBAcdY4YVi3k_e6A_0qsCM8A9-gOWbwgQgRjNuGsg97L-jcJ0J-yAU3AjXon5N3_XgT7rOSVzCdDD_cJZ1uBZy6JGhqLZ71jupuZSVlzqEnYS0DzDl9argA9RkTbtHpurw9lsLo1u7JryFPFLHL6dIrYvbwpGWMVtz_X5VSb9pULFxe5w88EnhJ0vNp-EgRsz0osIC7iKIOM4sfH13KDWQA34eVBDD8iD9-RiK_o4asw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ruuYMiCVoF5FpV5K2IqiHBxpD2KgTrEUWk1cVd8EboFBnW7voQnbe9toVgMllENUZdMFdvbjG1ObvkbULghGab3WVW1TmrPJ8CfxYrBR4StLSKutVUFi3ZlsvaPnjYDYTSSS8pjmL5IH-rmEBHQ-00PZLpNRQSSfK0LcdgEUyHoCa3lxECtt5YHDHYAeSNneiQcFMZEwnAqfrKPcdQy9d-v-n-UYwaUhH_cUN_MM0nsEHneiZAdduToUyrSx8uZIwn8Dm6DCwlnlA2-ScdvHZ5g3ZgYdI5aH9i9n8B7XmRg1lkHowonvsU4fSSfJ6HTUkfZgOwbHRO1ZgNzqf-FUvA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">‼️
آقای دیومانده بازیکن جدید رئال‌ مادرید هم مثل عثمان دمبله قبلا یه مصاحبه اسیدی کرده: الگوی من رونالدو عه؛ خبرنگار: مسی یا رونالدو؟ قطعا مسی!
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 61.7K · <a href="https://t.me/persiana_Soccer/26585" target="_blank">📅 08:55 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26584">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/K-vFg8GlLNNenkMFERvFHJP_gXROJPV1kazeTXy9No_VLY9AhQS8P5YBoJBJ0myDNoXjuK-saapejG-AxeG5MjHejL-SWsM7JMCQpi37edBwUCugbQa0btAMjk6slQdwXyCTm_IynSC5WlbTI6nHkgsCQdOpSFZlwDMNwWJCwWc8YI7HYKGWrFFCkXc-dWN_AZDEeCXxX02evPtyQgzcH0mlEWnS4H17TPPgwW4T_ANW370dkb5ye_fr0RGQfGdKToLUwJax456IydKOleeZ8xztUeWkPu4xRXIOXebF_i7BhNcvIC5HOLSs4DrPj7cpJh7FgDslxNcc99vfomybgg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🔴
#اختصاصی‌پرشیانا #فوری؛ باشگاه نساجی دقایقی قبل رسما بر سررقم رضایت نامه دانیال ایری با باشگاه پرسپولیس به توافق نهایی رسید و به‌زودی رضایت‌نامه این‌بازیکن رو صادر خواهد کرد و باشگاه پرسپولیس پوستر ایری رو منتشر خواهد کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 65K · <a href="https://t.me/persiana_Soccer/26584" target="_blank">📅 00:51 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26583">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gCSEYO8GQR_6IpV-0FbIvOQNghX3K1EvRjvgRClPa63meyh-edYBOQ-RJwk6ewwMqmo77U-7LmAxD0uz612QDn_2unHtSUvVSl8udMCOumStWIN3pLwzQHftS9CBEqphY-iUETNR8vcEoh2xGvCcCjO3bBs6XOtBWmGu_Al6sTJ-OpKTgmCyDvS-VMFt4Q-MuZfuo6n2WSFYiSgTUrJbAv6hyx-cW1jt0JxulCjgJMnkSknWNbzvcA-PZJhLiox5iqE797GqfKqu5iXJLcalUfZlWM3b8Rp6Bkx8Z3qLBRbuUd0EJJNHG6dVpD6qnDQMeZ-zXZXwJp1kqxqRveUCRg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇨🇮
با اعلام رومانو: یان دیومانده با عقد قرار دادی تا سال 2031 رسما به رئال مادرید پیوست و مدیریت این باشگاه بزودی از او رونمایی میکنند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.7K · <a href="https://t.me/persiana_Soccer/26583" target="_blank">📅 00:43 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26582">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SzC0mFQLkABSBIE6xxqXI79gbbgHEHg2TMsKBTL3OBg4ziRu2ZnnV_6S9vSQ9YrT6DX3wsbMkrTrmXp6Tnxtt7XASHu-8_e3Zx2qYlxjyThMzFAx6uZn-KgzhxwmjbOYY5Eyl9J_CouarTrEGUN7qvTobRmiQiGkjsjbWXquRHAsVTGmctdJNcfl8lTOtLGyKC-lj36IiVwT4KW5wudog6rN5_huCcqjkNMpDvDMDCMVssxHJSLYYKZAV5PV2fyyZu7QPhjD89KqZaDEdItjYrdHuanhmE4TK2BpuwOMxxKNLb5zHLovLJB6On_j3gTPozllRVS5pCdTc0QtsIx5hQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🇮🇹
اقدام ایرانی طور فدراسیون ایتالیا؛ از پپ گواردیولا، کارلو آنجلوتی و روبرتو مانچینی رسید به آندره‌آ پیرلو! پیرلو با عقدقراردادی‌تاپایان جام جهانی 2030 به‌عنوان سرمربی تیم ملی ایتالیا انتخاب شد. البته در صورت ناکامی در یورو برکنار خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64K · <a href="https://t.me/persiana_Soccer/26582" target="_blank">📅 00:39 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26581">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ns5z0o_17vh0VG9T-ZaZSkW3Dn80v3KcAJIDAtx415nqoZMJnbPYxwi4trIqMozdi21XVm3DDU2LOAmLGqaGzfaGf2iazYp3dLi31zKTYidiBbIytvaOZb0kETFux7Mb8Gc6RKQU3IuQ_xv5a2iv0oae47aV4iMZ24_H-qBkld-zE5CDfdm4BSbeyIw_TVpDV2nWvJWj1ARfrmLndzfRkZPQ2hCxmCDSVbbwFst-j8Gxro4XjMTwznKJvtLivNbW57KKnhoikgKXWuAMXwWx-H2n_50w7I-LHEP3VXqG4XnFS7mDZBbvV7wRPcCMU_24c7aeumYljookm5e-fKWqWA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج‌دیدارهای‌‌دیروز؛
برتری لک‌لک‌ها با درخشش سوبوسلای و برداقتصادی‌اینترمیامی با تک‌گل سوارز
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.5K · <a href="https://t.me/persiana_Soccer/26581" target="_blank">📅 00:39 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26579">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GKcluvr5Jhl-eBkEIlPh4aCyRlWt-g5k1Kb-1fO5nRfa2W25nWbr-KMquCROkM8px_w1JCiF-yMTWFiMJbG9aNEWldgEKXczHWP6mUch2mVr7VrKRqjS9RetBpePnaSJ2lJYHG1j1FkwOUWt8rTzmlGewF1-jtn4SpR7agQuGRUtejS8wxlv4mT_8_CmQqFZpMGfeFwhCMYsLRwXbb0e8mru83ze5twEwpdDcUFol9TJHgMHnku3LgFB11pXShqEZIFbrB6r-xe-wKpvPmJgpMKUxP02Rz95JVZbHz9NiyvUmAFZsD_FF1cew3FdPQoJYQmVJ1bOuE6CHetDhxbtiw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇨🇮
با اعلام رومانو: یان دیومانده با عقد قرار دادی تا سال 2031 رسما به رئال مادرید پیوست و مدیریت این باشگاه بزودی از او رونمایی میکنند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.4K · <a href="https://t.me/persiana_Soccer/26579" target="_blank">📅 00:17 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26578">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CtO98EC-RY-2Jv_jYX_8kwu0amid7-iyth3O_UYtMhQ0VsS-TuVicxl80INRAcksR4PFYaBj6O0Xr0t0n3P7dyr6i9Y0l2YvmfRSloJHHIXk5KdePCH-4k1DehgbDaa5nisQsWkGVCG_gz7SLFb8q7uVrwYp7_lhLYZRYukDujrcBs_zGvQRxiSsuzYmKKrCT1QqQlCMwU_PhGk4p4Kpgfl8oM0Xy2wYUk_b1ALxLda9_DBInzIOkvPEIzfSgrjaxLzqOytSjomMcPbNmGsJpoosDYCmLqqxAwjZJTHg5oA0yIwKDMBSaMHKt3ej6JSzb-rJ4zxq4jApU6zojCmBNw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#تکمیلی؛ پیروخبر ریپلای‌شده؛ رفقامون تو کانال میگن عثمان دمبله، کاکا، پائولو روسی‌ و بابی‌‌ چارلتون از قلم افتاده و این چهار نفر هم خلاصه موفق‌ به‌کسب‌ سه گانه‌ارزشمند گرفتن توپ طلا، قهرمانی رقابت های جام جهانی و لیگ قهرمانان اروپا نیز شده‌اند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64K · <a href="https://t.me/persiana_Soccer/26578" target="_blank">📅 00:02 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26576">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8d08e79ca3.mp4?token=p2Wwl9h07IG0Do8WdBGRWM1uvMmPIHvqgcUhsBePLHgk6xLgICKd9kQGVtiMF6solcLCIFy6_J3Ui1bdFdNQ_yM0o8Bj5oGVkpDc-LblmAPDoj-Bc1Y7exqmOkbvWzvaKqAgXBPMf5hxd3qUCghROOH9NwxfrPxjOkCAJhHPEAbXtafxlDH9cw4jY-2-z1fCo19H-nQn0yc7dZaCzXxYUncHbrLMzGX_2hEv43Bm3P6GXiHW6IFMukf65MYcMBWtrfm_z084OpaaOIPqvbQ7Pf5Jjs9riCPTnPslI-TCRvZl-Q1U3ImXdPwFCJ8RK2gVJFpbqx_xZgLn_y7jM-qJow" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8d08e79ca3.mp4?token=p2Wwl9h07IG0Do8WdBGRWM1uvMmPIHvqgcUhsBePLHgk6xLgICKd9kQGVtiMF6solcLCIFy6_J3Ui1bdFdNQ_yM0o8Bj5oGVkpDc-LblmAPDoj-Bc1Y7exqmOkbvWzvaKqAgXBPMf5hxd3qUCghROOH9NwxfrPxjOkCAJhHPEAbXtafxlDH9cw4jY-2-z1fCo19H-nQn0yc7dZaCzXxYUncHbrLMzGX_2hEv43Bm3P6GXiHW6IFMukf65MYcMBWtrfm_z084OpaaOIPqvbQ7Pf5Jjs9riCPTnPslI-TCRvZl-Q1U3ImXdPwFCJ8RK2gVJFpbqx_xZgLn_y7jM-qJow" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اگه نزنی ما احمد گوهری رو میاریم به جات!</div>
<div class="tg-footer">👁️ 64.6K · <a href="https://t.me/persiana_Soccer/26576" target="_blank">📅 23:39 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26575">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MScfjxFbLX_bRyWxK0PxhVitdzzR9PmAQnqJVHn2Pr2aS_HwzudP0I1C0LfPYblFCUEhY44n-eRltwIiz96uVr6HvCD6NfG4Dqifw57gL1p0750o85vusYrWi44HrXOTw0spD_pemRNLJejeUGEyOx0oscfhcP7jes3xKcROrm8Xc9cJUIsdbmFBARzUz_BO5aP-E_fj-4soSWH47c3cBscBQxXaRIEWug9pOBw7mi0iOl3W9PJfIoojxRl-ZwdszIG1BKd1lbrTMaq1ZrwtaaApE3-KT78hJD9y0HEVaUU6KzjYytvYb0gcrj-OWWcyGWnRnVLYvm6zf580rnizGg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#تکمیلی؛ حالا که تموم رسانه‌ها خبر از پیوستن اخباری به گلگهرمیدن لازمه بدونید قضیه چی بوده. مدیر عامل تیم پرسپولیس ساعت یک ظهر با اخباری تماس‌میگیره و میگه قرارداد رومیفرستیم امضا بزن اگه نزنی ما احمد گوهری رو میاریم به جات! اخباری هم میگه اوکیه امضا میزنم.…</div>
<div class="tg-footer">👁️ 65.3K · <a href="https://t.me/persiana_Soccer/26575" target="_blank">📅 23:20 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26573">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AhGWgpxz5NV7k2k37cDA9EiPVPGS3DDKr_fDmFnHjYkjDxKHm6tmeEyNdBmJz0C9LsMPu4NVD3QU7_VOUturrmsW1qH9hfBISGgXfDhk2nkeJb8N4HuZftTGFGX3T5Vm7kdA74zB5kNEvpVQSg4OT4k1IusBs86L0HZ-0BLA64Ee7TsT7TcBorVLpK_Jm-B1L3o2Mkc9tmh8jPDTMaVgnzeGlb3tNK0SxkBaFk1ZeZU_kcCoOyJF1Ndnfa-KQO4-zaZuDxFzAjQqf5QwLazIMGj5TyAK7bZwZBSpq3z_ww1ljq1RB0jZGrvZ9z46gsxkWuomw_R4Q0WJoaEeIM0ytw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
#اختصاصی_پرشیانا #فوری؛ دقایقی قبل سیدمهدی رحمتی شخصا با محمدرضا اخباری دروازه بان فصل‌قبل سپاهان تماس گرفته و از او خواسته به گل گهر برود و قید حضور در تیم پرسپولیس رو بزند. قرار بود امشب محمدرضا اخباری پرسپولیسی شود ولی به احتمال زیاد راهی گل گهر سیرجان…</div>
<div class="tg-footer">👁️ 66.1K · <a href="https://t.me/persiana_Soccer/26573" target="_blank">📅 22:47 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26572">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vD3QsRKbXU9hX2fwxpbJnHMJhYrVSDUL8zN5OUMosSdyJFTUYpoCqY2v3piWj6k9g0lIJq56mLIPuhL3fVOLt505BJnd5-e_nMCOOfQ_s-IGV1j6Npu44pEgcKUAHGybEBI09y3AHjgHUkIx7T5-oJRvULpoakGm9G1OIwOdnko4R6Yv2Dz5gj1CX0Hpyi9SHX2e32czduWwkMITQnMq2CPoYuMs28yvvV8NUjuFkTTHQvCfJzWIFikyHvwzIZ2pQ8ZsEo5jBhEU-Xc0c36NMrblU9ub9rx8c42p_oSGomUi-LQisVjpCsip2ItJBHHNf83oyHgm0Y4Arr89_Z4IYA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇨🇮
#تکمیلی؛ خب دیگه تمومه رومانو هم تایید کرد؛ یان دیومانده 19 ساله با قراردادی شش ساله به رئال‌مادرید پیوست. پرز قراره بزودی پول رو بزنه به حساب باشگاه لایپزیگ و این انتقال رسمی بشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 66.8K · <a href="https://t.me/persiana_Soccer/26572" target="_blank">📅 22:29 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26571">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GfGlrv-QLfiLLmNwKiq0SeHJQ_9rxL9P5fnRJF1r4CIPK8B0WhH4UjgvoRpT7XVm_NV1dofeUn8bTEpPSVyieYPsPCT4XOu_yEAiYpjq0o5hQBz9H4fSEDMXyuSMxjO3G0tEGrvABwZq-oCviGq40MclczTLgLNBXK-Qh8oeB7vd6GQ-BImf4TDFcPHAIG0e-NQdVpi2liOgviuu38tOGCR5J_cPaYlWU7GHhTkDRHEMvnNUdqzb1021ijzWXXMjcxwevbdeUtoO2oFo4cAWslvhgCWH49cW-s91mtc8KTShJYW3NPuJv6NOwFhn7fh_VKPJUOcEr3e7JGzU9THdPQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟢
مهدی عبدی مهاجم سابق تیم پرسپولیس که در فینال‌لیگ‌قهرمانان‌آسیا هم برای این تیم گل زده بود باعقد قراردادی یک ساله به خیبر خرم‌آباد پیوست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 66.2K · <a href="https://t.me/persiana_Soccer/26571" target="_blank">📅 22:06 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26570">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Tl4COL20YemuQcjou7pFadGX7za1j9LAk0CQjjeEjsUJ3gv87ix7n7PGLx9PXQDzWG3p27eYsmZxp_4ZP7msTgIov7GGqoYYmRrU0OtAJqJn_PWna3YImlcuhb_9d_n20yc4CZRH0RKZH38p0lAD4REY-iQKXvwZiIMTORug-2Lmzber_wQyWWv_5CSbp47pWpH0nbwUt5Z18oAGbAOAJ-uPvUxFu5xG4OwQa-BwtC6Q-sOp6xJd3iQXOfLH6yT4cpigJiKi3DfQD_8vdCL8J0kVszZ0tvTYuCKvrd2bf0iQ_s1PZ_Q2Eccux6dH8EdBBc29jFwr17gg-VYdAHvd0w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
هروقت فکر کردید بدشانسید یاد آرائوخو مدافع میانی بارسلونا بیفتید که بعداز گلی که به تیم بنفیکا زد اینجوری خوشحالی‌کرد و به خاطر خوشحالی‌اش مصدوم شد، گلش مردود شد و تیمش هم حذف شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 66.2K · <a href="https://t.me/persiana_Soccer/26570" target="_blank">📅 21:37 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26569">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uFcuqRRFjlVU6ZTHJ4ff5jMH3zxyimIMuoK9YuenRBaka3U88n28v7IvTLV9UtJTPW5R7EHT1MZ37erzqk_7rw_tlP8t-XQ-XBrmRcYXa9NNaVFFgsbT1-R4MAHZZfpOOjgqQg5fpZxdocSDZMv9LbaznsSwqoaAOxLsEdRIhCldamJVWLMwMufjnOG0QhkmLoMebZ91lu_XDA20pBpCwTNU_HVOVMaNlN0McKVfYTvz80rZqbfS_OiOiNS2pXl_oFHhWACTKdQvLIDcQjGBSQLN9Qfry1R7bY1WKG8GYe45fEBVBiD84qc_cRWsICOrKmm2vJIJF2h2AUz1HToJSg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
باشگاه‌استقلال به‌وعده‌اش‌عمل‌کرد و امروز پیش پرداختی توافق‌شده رو به یاسرآسانی پرداخت کرد و آسانی نیزتمایل خود را برای تمدیدقراردادش به مدت سه فصل دیگر اعلام کرد. بزودی بعد از انتخاب مدیر عامل کارهای تمدید قرارداد آسانی انجام میشود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 65.5K · <a href="https://t.me/persiana_Soccer/26569" target="_blank">📅 21:28 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26568">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rvDIbBQfrKcoTq64NECbVMi0T1Q8SrKDDGvdgk-8ChKUO-8e4iSQ4CtuSxqMXy1SSwgzIB2ylX17rIL5NBY_Ph0QGaA-NcZX9WurEdtaaS8Jtx2mv5WPU2NOPJSpBWAH8MIxfe1mYwAUkr2-rigBnKhQy51f4tlsUulkgE1_XU7LGHtZP_qAqJYCK0J2zn-_8plk5T9cd1lnofG0wKEm7l-z6vwqOt2-03d5Sz7COS2Rlq6qhofI9fZyybBbb8ZMHgsl-q6E3DpaNCLqMqNBMLbV96NkGAbCVwv9-ZMiyOH9CCvBL47DNtp10v1wnEWS8CEsuUoKO-fdqXQmvzlBwQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇧🇷
#تکمیلی؛ تلگراف: خبر مذاکره آرسنالی‌ها با وینیسیوس جونیور کذب محضه. این بازیکن بزودی قراردادش رو با رئال مادرید تمدید خواهد کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 65.4K · <a href="https://t.me/persiana_Soccer/26568" target="_blank">📅 21:12 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26567">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KRDBaxc-6Fw51qtihFjRPte2QpTOJMrmF4ye1GOXOXWtlBTXUPhVmbGuq1_QRJxXr-lFvdvgqwsjfX3ApG4vs8oOkfi_vlugyp2p1lakT9EpJ7PHDhtb3qsn-r3Ro6t_7iV_DEkfZ1CJ3r_f1SVRIKt1e5wPZymNGpNv3-RfDtBFrCFQE9J08M1kXOaO9-5dJQBcyAHSANOgadLBk9kQ3Jks1WpIB3kEegijwhMYOpsR7nZ_0KPsy75-wY0m7_SSf9DVkztLJSFwPo8fhAoCaP9sf5JKkM_sjZJk5h7KJtTCCaCBVCYNA6DV8SMnSe4QFKdaJsG1A3ZNQBBUViy3vg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
با اعلام رومانو؛
بایرن مونیخ بارا ساپوکو اندیه پدیده 18 ساله فوتبال سنگال رو با قراردادی 6 ساله به‌خدمت گرفت. پست این بازیکن هافبک میانیه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 65.4K · <a href="https://t.me/persiana_Soccer/26567" target="_blank">📅 21:00 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26566">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HPcJmrAiNmDLEzCMyZeP5KAWzFqOIRrTvrvEF_D0Xlt1s9M1AVB8FTXUY7c4jj74Dt9JLJXPNLcWfZsvS1WjGTnZ0o5O_sTuxifSkNIurp1reCBlBAGm4ixguyqF3sfmWgOFhaovgSbPfuO8MEZ5k82xt9UVxc9543YwhzjBV2G0NgjFabIYNNyave8FZcsbrgQcwoxZRG2zU6ApJNvJNLAClK0BsoPn4qhhh_BfYTdCkI4pZR28-lXxYip20Kmdyyj_Q8sPGnpi4Lkh2hfZ60M9JmM9Am6U0bmxGLhorWe__bsIt6XhQch2jwypJ0mwaMiVTc8nOewMw7htqzW8Bw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اگه میخواین بدونین کیفیت زندگی، اضطراب، فشار، چقدر روی زندگی‌تاثیرداره، باید بگم تام کروز و اکبر عبدی همسن‌بودن. تام‌کروزهمچنین بهترین تفریحات، بهترین بدن رو داره ولی متاسفانه‌اکبرعبدی‌فوت کرد.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 65.2K · <a href="https://t.me/persiana_Soccer/26566" target="_blank">📅 20:41 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26564">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Mc8e_Dp0E7u_UBb_-2cukwxUI0bAdGKdY_P31S8zx_uWH9pdoxsVCVPOioPfTnTjSLKMFFw8Tv1y89LnJYSn3bm97FjjCCqU7ZapRXhovMkEH7_MWQSY5-hJK75Zd1kQlLZ6_584mg7LqOH0ukY-Ya9Rst-WNn2fK9BYCdJyeK75wSmoHH9tJP9UQcUgRkyWhiR5OxdWbsxjmGSYNeARaoldCXDUgviaT10bXZXscgWEydUUmsdmdCNn2dlk19kIwFuWfrd6dnVEFDUArJkdfAmOpwxe3jB_tfrYSTKDu6nCc7KMFLH3x1y6M5GlR4oUlzjmkURfvcrSeNQIu6ynTg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
تاییدخبر اختصاصی20روزپیش رسانه پرشیانا
🔵
محمد خلیفه دروازه‌‌بان ملی‌پوش تیم آلومینیوم باعقدقراردادی به‌مدت پنج سال به استقلال پیوست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 66.1K · <a href="https://t.me/persiana_Soccer/26564" target="_blank">📅 20:06 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26563">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e2409944d0.mp4?token=Pj2QnYbnLpxDM2DoZZuV1nZPwNNftREm0Rkr1v9KRiQhs59ykVutAAWmmyAr4AFMcs1fCGaO1HMPMDxASf4gOK5q_8VqfaR2SBrFhYBtlN-VpmsQK1hdG_3LCTFBxGtajSEozR6dDpU26XMjhqqImKfm9jJqA-ZKDHvwnqhfkj4wQ0Cutd9YKy_Sgx0D2I7vMNSZtIVICL59CcRyUQNxrQYk45o7K5hv6YfcUetlBMht7ZkEAMN7g8MnKtW0d-Ia1FsZ5qXTjxQTgkbrNDlBs1ExkdeCWKM0mBWnOXWuqainZgsY7pombcqpUIENv_P2rFLkH_Z9B0Xp2zt6KoPoXw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e2409944d0.mp4?token=Pj2QnYbnLpxDM2DoZZuV1nZPwNNftREm0Rkr1v9KRiQhs59ykVutAAWmmyAr4AFMcs1fCGaO1HMPMDxASf4gOK5q_8VqfaR2SBrFhYBtlN-VpmsQK1hdG_3LCTFBxGtajSEozR6dDpU26XMjhqqImKfm9jJqA-ZKDHvwnqhfkj4wQ0Cutd9YKy_Sgx0D2I7vMNSZtIVICL59CcRyUQNxrQYk45o7K5hv6YfcUetlBMht7ZkEAMN7g8MnKtW0d-Ia1FsZ5qXTjxQTgkbrNDlBs1ExkdeCWKM0mBWnOXWuqainZgsY7pombcqpUIENv_P2rFLkH_Z9B0Xp2zt6KoPoXw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔵
🔴
#اختصاصی‌پرشیانا #فوری؛ باشگاه نساجی دقایقی قبل رسما بر سررقم رضایت نامه دانیال ایری با باشگاه پرسپولیس به توافق نهایی رسید و به‌زودی رضایت‌نامه این‌بازیکن رو صادر خواهد کرد و باشگاه پرسپولیس پوستر ایری رو منتشر خواهد کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 65.8K · <a href="https://t.me/persiana_Soccer/26563" target="_blank">📅 19:59 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26562">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LH3W01s1pTKlbSXGiubAF0C9hwyyNG_VgHIWJ9RxoDnfUvhIXbH6iqfhBVTrHLjesBun3-T3_E9rWqjPsPZJPZHDK2uOliFV_fQ-IuZAXLLAEU7EOi1IBVB79JZlobWfByqdBRykz7Wt-QAZEfy0aOb2-I--_Crr2W5MVcfOdkqTxq7PUKwo7mo95cDxKvNX13kuTizEj47GM-no4lqIXwV5sLzWGvupQHJ9AW5xlMwrboxGjqlVd-bqmiLYw3_-WakXuPRMWZFRwFyUjcb_tYOgb2SdAblpacFrDvx8Jl9qyRN-IMk9tam_LzodAVZN7v8bWyxS2KV-ZMw8MbW9Ug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
👤
#تکمیلی #اختصاصی_پرشیانا؛ طبق پیگیری‌ های رسانه پرشیانا؛ باشگاه استقلال پیش از شروع‌فصل‌جدیدقرارداد یاسر آسانی رورسما تا سال 2029 تمدید خواهدکرد. امروز توافقات حاصل شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 66.9K · <a href="https://t.me/persiana_Soccer/26562" target="_blank">📅 19:23 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26561">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/66921272ff.mp4?token=bwVo9PyPKFdJEDMCkW5NG9j0HbqUku2oYdcxh2qRRVGpXosiOgbTprmNsq-T5oG_BjVSNodaZl557krmnbpLK-K-OnhBAJVOZsVrN4_vkB-QW1s9-e1iy4SyzqLxuXpab2yZzuk1CZaEAZARW4qcUEKIwQ4gx0adlCczYfsBI9KUDiiawU9XqgVzT-5ctgqLxg3Ro59jqviIoggMO2Z5VUMMy2W77hFhyhkYSLksChitZpkc1tk26QCvYZHqxpdYDvEabkYwh-OoM68G2mTv_2sxKPQlVeu2xim5iezE0fQVY_dnmCoGWnvy0L42uo8yXWjEVH67Oem8axxK-zfhAA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/66921272ff.mp4?token=bwVo9PyPKFdJEDMCkW5NG9j0HbqUku2oYdcxh2qRRVGpXosiOgbTprmNsq-T5oG_BjVSNodaZl557krmnbpLK-K-OnhBAJVOZsVrN4_vkB-QW1s9-e1iy4SyzqLxuXpab2yZzuk1CZaEAZARW4qcUEKIwQ4gx0adlCczYfsBI9KUDiiawU9XqgVzT-5ctgqLxg3Ro59jqviIoggMO2Z5VUMMy2W77hFhyhkYSLksChitZpkc1tk26QCvYZHqxpdYDvEabkYwh-OoM68G2mTv_2sxKPQlVeu2xim5iezE0fQVY_dnmCoGWnvy0L42uo8yXWjEVH67Oem8axxK-zfhAA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📹
حضور جمعی‌ از بازیگران سینما و تلویزیون در مراسم خاکسپاری خدا بیامرز اکبر عبدی عزیز.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 66.1K · <a href="https://t.me/persiana_Soccer/26561" target="_blank">📅 18:50 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26560">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Zrj_3Gbm3Kl1Oh0IOhMLgO_YkPRUtujO_BoLLKCfx47EoXBQJOTaNWRyVsEY7mek-5DiRXZ38x4B6BDe0FbXdUbXLguyZrUPXgUD6IAM7mjJMvAzdz0SMZiSnWukt8gyfz4cistL6jE_65p77Z-ERZUtfje1EH3p3TFD-xHaZoPJEIeiEN0vXVG1xbyDe4nBdNZH840RaHLiQ-EvviOBwUAc3idSuePm6Zec6bQIwXvVdsInT47F0BGbkqpQ96jUxSd80Kq3kmFe2Lyd64gNEPl8JmhZV2WXDGD_t7SroBDE2kemUJ7H7ojhMAn92cUtF16YuP35-_Ye9kOrVTjN5A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
از دوس‌دختر لامین یامال پرسیدن‌چرا نامزدت رو بعد از پنج سال ترک کردی گفته فهمیدم لیاقتم بهتر از اونه و منم حق انتخاب دارم و انتخابم هم یاماله:)
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 65.2K · <a href="https://t.me/persiana_Soccer/26560" target="_blank">📅 18:35 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26559">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uR-S3aOZWlV3_JgqCRKkEOjZ4Lb_DKyXNwTuo_Be0wYE5XAb-dMejQcHlRY4c7pClCQgc4abp4jCwkA2zllLJzTbMeHXPmL5D8Uwwo-jQBvTSD4wRdxKMf0-_tt8UPLkPpx9-sPNgqGeZ1pxGChSmCVUI2Aq2ITFyv7GivWGWjQGAeV6mHegoD4HgibknL3A5LJQVHJPSqNgDbI24bKJ7IUn9zBzuM4QOtoEsDyll1k0YqAIst9-eKGgYnLpy4bG_IcusZ-I2WVxBi6QRJ1Nj8Xf9SU15BxDuvu7YSgpr3yPX8F13fgXYJXDcxQkWol2bK-SYUjdMheNfxTBE4ADTw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
مدیر ورزشی تیم لایپزیگ: در ازای فروش یان دیومانده به رئال‌مادرید 115 میلیون یورو از باشگاه اسپانیایی دریافت‌خواهیم کرد. توافقات بین طرفین انجام شده و به زودی این انتقال انجام میشود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 65.2K · <a href="https://t.me/persiana_Soccer/26559" target="_blank">📅 18:15 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26558">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Qtu14wo81pbI4maMy6b_jkXUW1wv1NYq6zm-MIgPgtszQZGxXWZRl2zSSnRKHnk9UsE3kAyEaN3HDn_RRBrKOismtWdz9IkDTFKvoXQBzUBfFg9_Z6sm3_NGXK2huMn8ubpUHJ7Ckaftmp7NuWcXekLF7-9BqJNeqEQ6rTUR0P-aLvlELY-fOdUMjkiTUO5FWPz0-EHu_qUSOTY3vJYbTI856YJJFaGWUSGgwf6Vdj0hXrVKSwefHRjTVjCzMsv0szN4HpXn_41_ri-UK9-nFglbDQPIIMzPvvLjfsMuUibTeTX-cTPVtgRwoAhpO3luY3Bsvbu6MpgeEHzFpZg5Vg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
👤
#اختصاصی‌پرشیانا #فوری؛طبق آخرین پیگیری‌ های رسانه پرشیانا؛ محمدرضا اخباری گلر 33 ساله سابق تراکتور و سپاهان تا ساعات آینده قرار داد ارسالی‌ باشگاه‌پرسپولیس روالکترونیکی‌ امضا خواهد کرد و رسما به جمع شاگردان تارتار اضافه میشود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 65.9K · <a href="https://t.me/persiana_Soccer/26558" target="_blank">📅 17:59 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26557">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Toz9r8YYIeZt4pAaUaISTEqoAAGhDxG1Uj5JNb5g9dC4CHigyKt3niVx6uzqFjkE1lwHSk9dWZFGtkSG7kfNo4lTeZHW3c9JtxrTLoXroj6IMAasRjJwLV6plQ5G-3guBPM0KjHqrOXUCL2BGeeox1NhHM3gdlEnALY20jNqu7gGIh7pytItbWdbk7uTI3BQnrAuUz_Wn65XMQRTlLPOKzJa6PJjlz_d-7HCHGb2pmWl_jdYj-n8-ARfGFGXL9fs9IUHHhPhyTEspVIHkf-jXUOrLrDnUU52OkNVHHUvdd7Hmi_-sNADskt0lC1XwieQayrvqP1b85CAT1AXtEo82Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
#اختصاصی‌پرشیانا #تکمیلی؛باشگاه گلگهر به‌‌درخواست‌ مهدی رحمتی خواستار جذب امیر رضا رفیعی دروازه‌بان جوان پرسپولیس شد. این احتمال وجود دارد که درصورت موافقت خودِ رفیعی، این بازیکن با پوریا لطیفی فر معاوضه شود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.5K · <a href="https://t.me/persiana_Soccer/26557" target="_blank">📅 17:55 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26556">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">📹
ویدیویی‌خاطره‌انگیز و دیدنی از عملکرد ریکاردو کاکا اسطوره‌فوتبال‌برزیل‌دردوران حضورش در میلان
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.5K · <a href="https://t.me/persiana_Soccer/26556" target="_blank">📅 17:46 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26555">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/g2iITsIFJDI5WxoxdBjQBNqAxzW4-DSvR0NFt2HCHzLQymtYzd0KMtnhp7tbnJ3DPu6PX0wO2yS6s8VoouimLN0OUMKBWsk8-KfDKX9SCOcanCzeB6CFP3BlwLF_J7f6h2C2ckMZJhIN8hRD0M2Dh6zV9PT3CGHfZCL_TtkYA-e7AD_aGFdspfUwAgHHzS2MNyT_Cd2G3YuflZe_LNbQuUHIrz350uT0Uf8Bm2E7U-jcxR691QlFABDB5eii_L2TaJ2kPbzwLfVv0LmzJi9OdmyoM8q69KwWRr8SqtdvSXYxjQodHnTbewwf-PIjdScdrcNPb5Br_yfOcRgS1Sllfg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
#تکمیلی؛ یاسر آسانی برای تمدید قراردادش به‌مدت سه فصل دیگر با مدیریت استقلال به توافق کامل رسید و بزودی رسما قراردادش تمدید میشود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.1K · <a href="https://t.me/persiana_Soccer/26555" target="_blank">📅 17:43 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26554">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/brz7NbomQ4BUw5hm5jSvpwNM0o4zoZBFakdM1L85JLxw-0PHJY0JKvgMXulTY8Ynhw_fkOK3NZpvdFDau28rg--9Qgfv5O43wf1QH4JGHZoALAnwsiKBE7D_vxIqwnGnjmgUotsrJzhcIizKdcyXEz2T1GzwEVXzl2FAFvl5GvybvhZ6d3APa1E2vpppPGB2jQXXO5CGyZWqay7YJ8GzvP3pWsPBolGIxoGPIB1eJIqDlEDlC6onn-XCxG-t9lv9xSl1flEo1HjIDXTXLnG7wJbtjlBYJonaT3YP6fPPkCX8GeQt-orjFsdMduGbzizEs9dEs2YAQR0czWaZ_AzG1w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
طبق‌اخباردریافتی‌پرشیانا؛ باشگاه استقلال برای تمدیدقرارداد روزبه‌ چشمی کاپیتان 32 ساله آبی‌ها به مدت دوفصل باایجنت او به توافق کامل رسید و بعد از بازگشت به ایران قراردادش رو تمدید خواهد کرد.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.5K · <a href="https://t.me/persiana_Soccer/26554" target="_blank">📅 17:43 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26552">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/738d729f53.mp4?token=bxNmpcmmqZ4x4DOJh_lgqVb6e_u5nDqbCNwe-dpBUsWtvGflNLVETB-1qxeF5tCpqFnLaJ_YzltfZeYlr67oLwMjeKbDaJV2efcspfVwWrIknjkIDFzmNZomdVOd5nsCGH9OcjSJB9DelCPzVgHwcMJXXCgzRJ90jps60nLqNlEJCTbue3ZFnrEIbfOkKqJFNwJvBYYojDme1epDDJ2pPwmqXVEB86oG86LAk8geXGkls-04hs5zT4KHmHB6INeiHpdXNCUxYpGobqNIAZr8uiEBHmNQUmIooy3LGDUisVqzzjp3n64I_ZQYUs4TXtojCixDM0pqdf4NTEd9JCZOGw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/738d729f53.mp4?token=bxNmpcmmqZ4x4DOJh_lgqVb6e_u5nDqbCNwe-dpBUsWtvGflNLVETB-1qxeF5tCpqFnLaJ_YzltfZeYlr67oLwMjeKbDaJV2efcspfVwWrIknjkIDFzmNZomdVOd5nsCGH9OcjSJB9DelCPzVgHwcMJXXCgzRJ90jps60nLqNlEJCTbue3ZFnrEIbfOkKqJFNwJvBYYojDme1epDDJ2pPwmqXVEB86oG86LAk8geXGkls-04hs5zT4KHmHB6INeiHpdXNCUxYpGobqNIAZr8uiEBHmNQUmIooy3LGDUisVqzzjp3n64I_ZQYUs4TXtojCixDM0pqdf4NTEd9JCZOGw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👤
👤
یادی‌کنیم‌از این‌صحبت‌های ارزشمند علی آقا دایی در گفتگو سال‌های اخیر با عادل فردوسی پور.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 65.2K · <a href="https://t.me/persiana_Soccer/26552" target="_blank">📅 17:26 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26551">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7014b2e92e.mp4?token=C-J_TT4u2ypdBwp_c5i5LOrc42X55pDaP2yXMlqimwZkUmULOTl2yLgTvle07dDHL71SUMasuk7tRNqCzT8SkljmjGMdGB5mSWBgRo3BrEgTANp0_l5DVUUEgTmykWKTo-Rll06sYh5kG6nvJhKtlmO7mHvctItGNo1UOZTnWImGB1YVRWjwkKbl3StAWbE4lf3SCYmxTrOVyPlReKwfWoDMj9_Xf7F-QcWWMqonC7uFLoL_r5gRZG7-_HH18hyhNQ5PaT1TXYfztCpkO_7D8Zzjq6SThyEqmJXrZUAOfwWCZAg1msqEKK-AwPAy_avfUDMi0RQfOk62LvvcSopQSA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7014b2e92e.mp4?token=C-J_TT4u2ypdBwp_c5i5LOrc42X55pDaP2yXMlqimwZkUmULOTl2yLgTvle07dDHL71SUMasuk7tRNqCzT8SkljmjGMdGB5mSWBgRo3BrEgTANp0_l5DVUUEgTmykWKTo-Rll06sYh5kG6nvJhKtlmO7mHvctItGNo1UOZTnWImGB1YVRWjwkKbl3StAWbE4lf3SCYmxTrOVyPlReKwfWoDMj9_Xf7F-QcWWMqonC7uFLoL_r5gRZG7-_HH18hyhNQ5PaT1TXYfztCpkO_7D8Zzjq6SThyEqmJXrZUAOfwWCZAg1msqEKK-AwPAy_avfUDMi0RQfOk62LvvcSopQSA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
عربستان‌میخوادبرای‌جام‌جهانی۲۰۳۴ ورزشگاهی حیرت انگیز درارتفاع ۳۵۰ متری بسازد. این ورزشگاه باظرفیت۴۶ هزارنفر برفراز یک آسمان‌خراش ساخته میشود. تماشاگران هنگام برگزاری بازیا می توانند در میان ابرها فوتبال‌تماشامیکنند و همزمان چشم‌اندازی وسیع و دیدنی‌از شهر را زیرپای خود خواهند داشت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 66.6K · <a href="https://t.me/persiana_Soccer/26551" target="_blank">📅 17:16 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26549">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QmjQsAq9m8fMEwzBL5SH7pydSXH4f-maIFXeoDJOTPQXzkoqgn4sbZR77hxrKA15Fj6iKlRJKosGrC8QS-2SCAV1YavbFIyfrERF_I3eDn8eGqa086adAghhfdiVf-Kn7bASF1ZxVE8_MwrO0W8zzR4XaYdGwGcOMKETqaaxtUEWWGKyVKhX57tgJXlnlRn4nA9VzaHuYJXKWhhME4WxjfRO9h3nmlT4_qOLB3Z0X7zTpjK435D-1lK6oG76sGH-51QyEX7Y1SnVxsh57PbzBMoDiRSY90S_nKghzMvWpoExDqrfjgLr_zps-bAorTf6xYwe3-k_2PJHqOTWguDM9g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
👤
#تکمیلی #اختصاصی_پرشیانا #فوری؛ محمدرضا اخباری گلرسابق‌سپاهان‌بعد از تماس مهدی تارتار دقایقی‌قبل موافقت خود را برای عقد قراردادی دو ساله با باشگاه پرسپولیس اعلام کرده و اگر اتفاق خاصی رخ ندهد اخباری بزودی پرسپولیسی میشود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 66K · <a href="https://t.me/persiana_Soccer/26549" target="_blank">📅 16:35 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26548">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a750ab04f2.mp4?token=lo0s1NsRCuw6KLjPREyqPhPycQgGkQNN0CVrJteVxU1D4c6k5bvU6WhczaJe5Cb9o7Ez0qy7WFB2QtKCPyHDpIuDQR7a3k9wO32EpLsM6QzYBaRMP-vj947NTsvh9_Q0lYtBmgERIH79TN44bLWKcvM7ozT_z4o_Bwi01ACllltT_4mT78Up_zTrss80kWOwV0thkwBRYE3QOXAxFBsG0wOvmKIw05ZKdebssy2gFMceqCsjxcZwurCRsXP17SJMOtmO9BOwuNOSZUx1C61BXbhccAGx51O69czQy4yUTsR4KUSNqDDfecuJDmydkgTJmPUbiwaUo5EEB7xjpK0xUTWBz0xh90TuwDlyDEf6pd0VAZWLGWNKvThGkU2FU55qoZz6m6oTXrX0aj1b4HDx53FxXIXWH7pSWaUDVLHUmi7rrzEzteYKy8XFBk80xjOKNQ_C4hlDubBO3mmuXTdm9ZDnCHk7xS0BuRU97T-9tegukILK11Di-oconOCoSNtt-U9_SK7bIObjzD3cuG4ttQ5rbtz3vFlRa8OJrW47sU-rEpcWvIqNqQeGLs6NK2gG0RR8UJIuHYMyU3X-gtliICRl8n6C4gkZe7d_UPNv-aIgN87jdqbU8YKaXKw6W4JTmrMnJcG21kLztivvNe3f7fTInuHg_BTpORonRsU9q0M" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a750ab04f2.mp4?token=lo0s1NsRCuw6KLjPREyqPhPycQgGkQNN0CVrJteVxU1D4c6k5bvU6WhczaJe5Cb9o7Ez0qy7WFB2QtKCPyHDpIuDQR7a3k9wO32EpLsM6QzYBaRMP-vj947NTsvh9_Q0lYtBmgERIH79TN44bLWKcvM7ozT_z4o_Bwi01ACllltT_4mT78Up_zTrss80kWOwV0thkwBRYE3QOXAxFBsG0wOvmKIw05ZKdebssy2gFMceqCsjxcZwurCRsXP17SJMOtmO9BOwuNOSZUx1C61BXbhccAGx51O69czQy4yUTsR4KUSNqDDfecuJDmydkgTJmPUbiwaUo5EEB7xjpK0xUTWBz0xh90TuwDlyDEf6pd0VAZWLGWNKvThGkU2FU55qoZz6m6oTXrX0aj1b4HDx53FxXIXWH7pSWaUDVLHUmi7rrzEzteYKy8XFBk80xjOKNQ_C4hlDubBO3mmuXTdm9ZDnCHk7xS0BuRU97T-9tegukILK11Di-oconOCoSNtt-U9_SK7bIObjzD3cuG4ttQ5rbtz3vFlRa8OJrW47sU-rEpcWvIqNqQeGLs6NK2gG0RR8UJIuHYMyU3X-gtliICRl8n6C4gkZe7d_UPNv-aIgN87jdqbU8YKaXKw6W4JTmrMnJcG21kLztivvNe3f7fTInuHg_BTpORonRsU9q0M" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇸
🇵🇹
دقیقا 17 سال پیش در جولای 2009 باشگاه رئال‌مادرید درورزشگاه برنابئو رونالدو رو به 80 هزار هوادار معرفی کرد و دوران طلایی رونالدو آغاز شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 66K · <a href="https://t.me/persiana_Soccer/26548" target="_blank">📅 15:59 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26547">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oJ28sw3NsEMmSnCOGaDKzhwwuYZHccGs-wpjruL8Lu5tAAHVVsmkbE0g5zOr1PPSf642U3uI3OL6pfd6o1tV1eGFsoWS47XHPl9h4ncKtWeW-DVN7RG-WKfSgL29nqiGyE5Q6n6Tic0DsdRcMKvV2MTRxWNT1rlFIWVE8eYPqG3FgYa88aIurxajlaQdb52ExdCpjmleMCJrm3CzTlZtOdnIAItOmr0wht5E9dKM8R03pvrj9ERLt4NuQvs2y38x5dCVaWEDtuDSYB3AMNUQaCkfDNAbeAAFC8N7iMv5w_8q9lmcqntMWR9I7AB3huu4foJ1L5JmKdOQ8o2YvNnDvA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
#تکمیلی؛ بعد از چند هفته بالاخره، سهراب بختیاری‌زاده‌سرمربی‌‌‌استقلال‌دیروز درخواست تمدید قرارداد دیدیه اندونگ هافبک گابنی فصل گذشته این تیم روداشته. باشگاه استقلال ازفیفااستعلام گرفته و درصورتیکه پاسخ فیفا مثبت‌باشد قرارداد اندونگ به مدت دو فصل با باشگاه…</div>
<div class="tg-footer">👁️ 66.7K · <a href="https://t.me/persiana_Soccer/26547" target="_blank">📅 15:53 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26546">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JbFkT3OjvQaxwe5w9G9Le9bq_GrcEXhGWgYZJlnfHVWkbAf4WJiGhq4mkXhb2Xi8SJjwNXCwIRheD56LyXRVKKlW-0BwIO9aiuUQhIxbSbK_Q1UrVHEMHeJRM3PXAllVar0fEyrwHRsYMfUjU4fj7mQY3Vxn_H71OwPH46_-JWvAmpoXMDIr2Ca97OzPMrQ7Z2PHbaIRbA930C3H5JbQCZccxEJA3LxqQaZJRzGQT25VzvpAeJDcrup2VwV3glaYGCA5DLgZHLkpHoxfDQYfY4ydw_jkEVOAd08envTVyXSI4kXTlIi5wzxdH9fdEY09jqmGVvBg1xj9bQVnBnqjNQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
‼️
🔴
👤
باشگاه پرسپولیس در دوپنجره قبلی بارها تلاش کرد تا مهدی طارمی رو جذب کنه و حتی به نماینده او گفته بود که در صورت موافقت طارمی رضایت‌نامه‌او پرداخت خواهند کرد اما طارمی پالس مثبت نشون‌نداد حالا باتوجه به‌اینکه در لیست مازاد قرار گرفته و ممکنه بزودی ار المپیاکوس…</div>
<div class="tg-footer">👁️ 66.5K · <a href="https://t.me/persiana_Soccer/26546" target="_blank">📅 15:38 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26545">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PR6EVfqeLya9UbukDoxnR1GknEQn5pL0Ck6bSVWO7upU8H71k-A-Iah6tt1Gk2SbaHiPxYd3AV1pIvS8NpLuvZg7gJzSfbugarK-wA2klQ9mEH-0gQ37Bmv4nzuxobyUApgwl2imbnf2WDBqK213odb47eLbEgKw-su8cscbGxtJg6NLgIxVoF4yDgiacQ2Fg5iE7EQLLnMP4pak8NQinHkHmLR1aMWbg6oC-xUOrrbYANjcKnjDzOeSzghkWRJROMIRilZXq0b4Q7_tKYtSWSRYmhLeGp-Pgdr2Rn890qaXV3WCQ7jR5N7WvwLh_y9103MpqTBLB6MSJne8El2Ikw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#اختصاصی_پرشیانا #فوری؛ دانیال ایری مدافع 22 ساله سابق دو باشگاه ذوب آهن و نساجی دقایقی قبل به‌شکل‌رسمی قرارداد داخلی خود را به مدت چهارسال باباشگاه پرسپولیس امضا کرد. پیمان حدادی به‌باشگاه نساجی قول‌داده فردا مبلغ رضایت نامه ایری رو به حساب قائمشهری ها…</div>
<div class="tg-footer">👁️ 66.9K · <a href="https://t.me/persiana_Soccer/26545" target="_blank">📅 15:23 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26544">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a35e208335.mp4?token=uoVElJly3BnyU-vbss0inwSTZJxwnFutTLbrs48ysXiTiZib-xzKH0gFJypnR-1wa_FML3Nf1fSvh0V3sImxCXuFkflpxnyZ0WA7PMlgLl0UtftH0J9UkV96pZxBAP4oqbIWVUpOYAcoie7uBpK8DFnyp3BbckpgCYtMWK7nCHtfEnxLDn7mglXNh8wTS4Bx00Y2QFZSde3MBbKnjYB5X3WrQpOGhd5uBl4KtBb9snDDHn3nN5kl5YYTY1bf76Gn165NxXvy1FcqTigloSAmQwb_0b71FYAttrffm2Xgoi0_cPWVwxxiZt-J82MUPA5Coy6CChshRk7UXmUStdgrMkYn_7lGiFPPRJjGrnc8_U8kRLC4yYl9WpZ_dsLWaFAZiyu1dwMEsOarN0nTtIw3fedHHepBkJJKO5iQ7QlUlKayO2mMDKQ6cFQZT9oi0CMJdY9vzNSFhOhwmfMXG52MR_fDFzmQyhO9qZ4AEDjkClNxXagl7coWhi4wKFHhQOHJNoMaZkCcaoar20SBBx7NBfddCnL2CBsJr4JG-h7HMq9_4KV5xsQagiX_3eB02_WDoZGf4CacA2HfuG7T5wLrD1JaQP9Wuxm6ozqPfAgIjmyYhzna2Kkx9MJN_VEpRKE8m1E2LvK2H3NUd_5XjsW1NqUGfV0d0dhWJYyMr15Ehmw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a35e208335.mp4?token=uoVElJly3BnyU-vbss0inwSTZJxwnFutTLbrs48ysXiTiZib-xzKH0gFJypnR-1wa_FML3Nf1fSvh0V3sImxCXuFkflpxnyZ0WA7PMlgLl0UtftH0J9UkV96pZxBAP4oqbIWVUpOYAcoie7uBpK8DFnyp3BbckpgCYtMWK7nCHtfEnxLDn7mglXNh8wTS4Bx00Y2QFZSde3MBbKnjYB5X3WrQpOGhd5uBl4KtBb9snDDHn3nN5kl5YYTY1bf76Gn165NxXvy1FcqTigloSAmQwb_0b71FYAttrffm2Xgoi0_cPWVwxxiZt-J82MUPA5Coy6CChshRk7UXmUStdgrMkYn_7lGiFPPRJjGrnc8_U8kRLC4yYl9WpZ_dsLWaFAZiyu1dwMEsOarN0nTtIw3fedHHepBkJJKO5iQ7QlUlKayO2mMDKQ6cFQZT9oi0CMJdY9vzNSFhOhwmfMXG52MR_fDFzmQyhO9qZ4AEDjkClNxXagl7coWhi4wKFHhQOHJNoMaZkCcaoar20SBBx7NBfddCnL2CBsJr4JG-h7HMq9_4KV5xsQagiX_3eB02_WDoZGf4CacA2HfuG7T5wLrD1JaQP9Wuxm6ozqPfAgIjmyYhzna2Kkx9MJN_VEpRKE8m1E2LvK2H3NUd_5XjsW1NqUGfV0d0dhWJYyMr15Ehmw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📹
اشک‌های زنده اکبر عبدی برای مردم ایران درباره شرایط اسفناک اقتصادی مملکتمون و گرونی‌ها.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 66.8K · <a href="https://t.me/persiana_Soccer/26544" target="_blank">📅 15:13 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26543">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KK7oqbBUTsk57I3NemXEmrS-wK1TS0pv7Zc3Au0InOfrPggzWjzkMGmDOeVRrq9B3IB_Qn-PhgUMw8UkpF_ZCS5tCl_dWCsYSG7huSRlt0kmmM233wpuM5vlW06R6uqMWQxPfEQFy5FOPOqiJf0r6g1eEbnpgDjBLou39wr8_vuvtfWMJ-vyHbRLTs9aTKdQCR4092H00PhGDKuHJ3IWYK_ckameSK2o6Vh0rChVrZM5K_sFU6Ti37Em_FhUEH7PH_E6qI74RHCg4uZ63wLPRgysU1oaRBJ7ov4O6EApdUSAnWyVdvMRjoeXdO3XUPGCd1HBTCYjLf9dMO2qKho8fg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
مدیر ورزشی تیم لایپزیگ: در ازای فروش یان دیومانده به رئال‌مادرید 115 میلیون یورو از باشگاه اسپانیایی دریافت‌خواهیم کرد. توافقات بین طرفین انجام شده و به زودی این انتقال انجام میشود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 66.2K · <a href="https://t.me/persiana_Soccer/26543" target="_blank">📅 14:55 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26542">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ca17hA4Hxs0tzfkygDcimilOS6yDoHYOTnUnp066cZ1Fs58O7pK7EEd1QYvkcXT-hlmGgUCBjSl71r8c-T5Dh7zQDg4Ayw1bpaPghgK1BOE7VrKXAPJLOl_DYLSGIdu8hYZkR8_51JP-QK8GKJuSFbkB-fpoWeDt3rIyOxq3QFXZCtTkESCRCunAP8gLuWEfC8aagtn7dxpRtEWFBq9JOWJAFLKjzPwayHKQcvq0EyvXXxq6PBoXl_2evgTvwLJSUcQXJaaIlAo0Vnm0oeWgqyll8MPbKz6xojPJtYgVRws08tkSn34XjxqQEojbVONftUajmI_fnqUes1TxIACCGw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
بااعلام فابریزیو رومانو و علی رغم شدید مایکل اولیسه به پیوستن به‌رئال‌مادرید؛ این ستاره فرانسوی این فصل هم دربایرن‌مونیخ موندنی شد اما تابستون سال بعد به احتمال زیاد این انتقال انجام میشود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 67.8K · <a href="https://t.me/persiana_Soccer/26542" target="_blank">📅 14:38 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26541">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MFCpRhBGoU7ctefxJv9gf9gSCRnQDG2zbMX_H7VC_0XvadjQRoqGqZ3EkLRgLYHMJTAqWn1kgFbFhEk4wxa07__KtCPM6r71cDI6uxVQ8LFOGOyTylQKFncvCsJjvYDzgruhjQxK0LoCVtUyzVx5PG1mAzgTprap4IavY95Es_5AIREyVYBgutuoutb1o1orNdyr8eotgJ6pFLqaD7PjGffKv3Sl0lQLOvGriA44H3BMAPD_kM5BnEhYrAcXu9oh7r2XdNRDJTcQKIU-F6ZprcLYVsS5IvJgkKIy19c6ktcMhosVADar4GSEtzF17Ijy90FuV-_qp75ZW5vUA4yLWQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
یاسر آسانی ستاره‌البانیایی‌تیم استقلال برای جلسه‌مهم با علی‌تاجرنیا رئیس هیات مدیره استقلال وارد ساختمان‌باشگاه‌شد. این جلسه مربوط به تمدید قرارداد این فوق ستاره آلبانیایی است و ممکن است همین امروز قرارداد آسانی سه ساله تمدید شود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 67.7K · <a href="https://t.me/persiana_Soccer/26541" target="_blank">📅 14:12 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26540">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WEqaywW85DW-QREnR2wfAoRsz_hnnB8d6Jd1wCeSekKjN_1HI9C80e2XRD1aF2STQdT_JcDEX22PiRYXErmOyElhGanb8W3uYW8hfokwqbw7t55fFE9mgIwfOgAl2qOh4Tt9w1nPD42IiTS0X4D44KLaFKfueN0CqOo30BcblyHoSapLfN4MtxBbRIYt6Cq2y4FuS2d5wjI6rSRb29a26e_8-RR3bxlRxnbphiU6bX9YmQTFUWQQ7Z2yOL6nn6LsetqYq7imnmkZ42X8neBHFyC2b_IcfYrn-hXv6D9WJTG4nU9WSGVDhH0yXS7MnZvIRlS4_7AldCJJfRf9TQFEzA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
طبق گفته رسانه‌های یونانی؛ مهدی طارمی مهاجم 34 ساله المپیاکوس در لیست مازاد این تیم قرار گرفته و باید تا میدون آزادی بدوعه برگرده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 68.7K · <a href="https://t.me/persiana_Soccer/26540" target="_blank">📅 13:14 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26539">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GbO1aRRU5hYzmjYuHcKh7bnNVkJMbdYBCaT9wiAEIPcHPWlmlX_glFdY1msr9rC2QLyB3pBWVKl6CcZJ121YpcApd3Gk_yj-uBhpTMtK1s8EP0TVI_prSArT1be9wn6zdJrww33p8qwy2YOu6nZbs8NKAMAdOVTUx_KGIr6TUYXbY53Zg34C5oWhNvXCB78MmMNv4xRnCKe8sGHBFUWgMxtmJ8ErGkk5nvFjbdS4Tbw__-4NLmgsCcrykRj_DeHrkouOCY3OBTYfL1V-hpiGkGSZqgMfWN50Vi_J07mIVFnSnAvtYDpMP0S5vTnj0VNkpnTk-3Lu1OnH5DU6MvpYtA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👤
مهدی طارمی: حالا که دیگه صعود نکردیم اصلا نباید سوار هواپیما بشیم و تا فرودگاه امام میدوییم.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 69.1K · <a href="https://t.me/persiana_Soccer/26539" target="_blank">📅 12:48 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26537">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7f40399edf.mp4?token=f0V4VP3EA2QMu3Ix8v60xUXG9pVKbmgGY_wXPOzH1MgrwPZrdQo7P2YaE_jKNbMOpage0gXpluoB-t0Mg7EHah3qntfTKtmsYWnbQoUWxVgVh37TZyjYLCdMxdWCT4Tnh2iCX9UzyyRsz0dd4iXBy-RBcdoMv8WhMyAtLjl705ZmBHEJdNPawK4dvM89uBg__6xagAd_13s3VAbZ0bwHvk6HdXU2TDaNXWHe3mkRErpkQAVdrsLVsJw_Hp-5oDr_8J1QpCSd_RaOaQBXtG3lx2RMyEhFkdF0ZDcoUY3aA5nfAQ2PgA0qlnsH5Rc36slFt90-n8RCJZ5QKKRtEal-CQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7f40399edf.mp4?token=f0V4VP3EA2QMu3Ix8v60xUXG9pVKbmgGY_wXPOzH1MgrwPZrdQo7P2YaE_jKNbMOpage0gXpluoB-t0Mg7EHah3qntfTKtmsYWnbQoUWxVgVh37TZyjYLCdMxdWCT4Tnh2iCX9UzyyRsz0dd4iXBy-RBcdoMv8WhMyAtLjl705ZmBHEJdNPawK4dvM89uBg__6xagAd_13s3VAbZ0bwHvk6HdXU2TDaNXWHe3mkRErpkQAVdrsLVsJw_Hp-5oDr_8J1QpCSd_RaOaQBXtG3lx2RMyEhFkdF0ZDcoUY3aA5nfAQ2PgA0qlnsH5Rc36slFt90-n8RCJZ5QKKRtEal-CQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚫️
فکر میکنی برگردون رونالدو جلو یوونتوس از برگردون تو بهتر بود؟ زلاتان ابراهیموویچ: اگه تو فاصله بیشتراز40متراز دروازه زده، آره بهتره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 68.5K · <a href="https://t.me/persiana_Soccer/26537" target="_blank">📅 12:35 · 04 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>

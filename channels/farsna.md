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
<img src="https://cdn4.telesco.pe/file/qnH6093dB_hs3kqc-xb5tae1zdvzf8ZwKfmLvvu3f1cuy2soWhVY4ETnxN8aUCZujewDMFkJsTdLhXRfJYzyANT0so94L6_czv7SBgI0EcioNjzUS79gFwyPBmXEF2qVGtd56_U53fsuOTlrE1rO9oBUL7n_QCiqxvKMIt1Q9ehHhPjnvBVm2RrakBpY7Fdt-8WjVw_Rx-q10o_Ns4aFH-bNugGMvms0FEo-KXQPNNjkZ1pjIKpIbrgkC0ImQ4cU_f8CHObHXL8k5Km3Q3Si-8RQsPGOjiqq2zsFR7-XiF8THE8CsSRtP_zImB6Uazf_FfeNiW2g1GjlrDWGednmiw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرگزاری فارس</h1>
<p>@farsna • 👥 1.83M عضو</p>
<a href="https://t.me/farsna" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 حقیقت روشن می‌شود‌‌تبلیغات@Farsnews_adsارتباط@FarsNewsفارس‌پلاس@Fars_Plus‌ورزش@SportFarsجهان@FarsNewsIntعکس@FarsImagesپیام‌رسان‌ها@Farsnaاینستاگرامinstagram.com/fars_newsتوییترtwitter.com/FarsNews_Agency</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-20 21:22:53</div>
<hr>

<div class="tg-post" id="msg-441221">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nMuXsCpn6h_XhbKoHNKpt2uCFwiQOe0Rj0666eIgTUsGffxeDMVcCtza4Wq-jaUqjB4PmTG75TyHa22nTtcRU-Baxrzx2HLiCBmMJNEl4TnxbKqLBUnaQWxaCe36rD0SeHwYQfOI8ILa3HwQZ3TG4DM3Pwiwv8fUillU4ESC5xCW0O1d2TEGQADtdg-zylbXce07hzhPKtE3cFcaeS0lGQ8sL8Fl15J7bo44UBqWIv8BAPesIKHHGBDrBp53MfN7QEMGpmPrnfpXcu5gqDgW13Vb1e_sn3d5WkwqeWokn7EhWAfrwoqHd2QudADQsfw3yaUlSm2ONGJrkhdRAzCAAQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ: اگر من نبودم، الان اسرائیل وجود نداشت.
@Farsna</div>
<div class="tg-footer">👁️ 994 · <a href="https://t.me/farsna/441221" target="_blank">📅 21:22 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441220">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ONphVNEBZomegJzNeq0xhBo9q6dyKPsP097SskrTXk41G__x5o478DPP5gWREa9p-OfWq9bAgqNFtD4VxRrmqCeswgU71MOIExopVvWVCyXmSu5Y4igRwbR_6Ufxrl986FWvX-WUVIUWY5IRuqIMpREsZSgWkMjO5ixVhhz0XKn0Dj1KPrSCPdP26YMEwXAsPwm_lFOXfYKxzFiD_3xq1C2KjfjcVik4qg527a8udoWvsEBgTqCgeqYgIJ72GmbPrifJvCDTe3_2htFXNynjOmiahS8EjCvayBSf2W9U-5vdjviAfIfVRWOLoqPLz0P8Cwkh6R9HUYdEH13BOY6Mdg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جنگ علیه ایران سود هواپیمایی‌ها را نصف کرد
🔹
انجمن بین‌المللی حمل‌ونقل هوایی: اختلال زنجیره تأمین، ۱۱ میلیارد دلار به شرکت‌های هواپیمایی خسارت زده و جنگ علیه ایران با افزایش ۷۰ درصدی نرخ سوخت، سود ۲۰۲۶ را از ۴۵ به ۲۳ میلیارد دلار کاهش داده است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 2.74K · <a href="https://t.me/farsna/441220" target="_blank">📅 21:13 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441213">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/h7tZu2weZNHv480f32OFISQCFFwN-e2XN7U0zHdDZBFpfVcQqrL-ZBqACNCHm2xXMzotk4fwXG2QbASvj3e9hdZJJv6JKQQij9btDCCtMgG2W7TmkvrkvPpza8JZFRclWd-J3JkqyHnKrxA63U-gg9Z6loHvbQv_Aa1LV6WlH4FkNOi-F5Wko4Q43BXABYmLj4T57b1IeKCFoZPxht4of8MZ1TXImqR-Ft58c2tnOMK5RbfcFw2KT21jmqztcJqTt2WaDvnJuU_z08Bc4Fw4L5kUQoRzOVCrwGzLd2hZdesXkhjwpZQ8MuaVm63BsUkg6nqBwNoMhNC2T4pClRUGBg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/s5r5FBqGxeOhmwTMuAa5kxEFyFNEuN2yWw74fqhM7c4-xhNJ-pY2v95_A5bxtgLlkliaCePFPW1TXfk_7Yc-a4PxSGMeODJ3LjUD8hY85HXyzqvTsEp_LH9m0o4baI0SU30GdTYpdEutVshdgxEJlTqg_W4bI3TCwwVmN5GUdDVg3ip637H5piegxTy2bCL-mkzihSLicGFECHaI2yWpMoy4HVg3af0ZaBsNaQfroenMHYRWARQUXd43eiP-mnmQCm9Euh6gSYz0rzqRV3EvYmycY6I1TmMeoyd-r3bJZTwsNkQz__WsN2-O6SUz_JTH2hx6Asi6oGSrG83feOJtLQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Srs4LyG1d_ZGpwEhMfBAabHYIYezucSbFjQD-lFrihDbYLqi-RZ1op84km55HZGNbSSRUJ4VTWv_LyY3bentAd3pJw48KGv5EnzVZWm3h41hahMYeSKsztz9CY_QuWJUKahXt9U9NAaOIG7euguTM_XS9A2ciXa4KXbrM5BpjTeDZMURet-0UspCfs9dAy-fD76K9tYVbJO6-MbPvKDbV4swGh7qTKIzdAgczIV9EVicyuOZuDUcWXAAnrHgVLCxoTe-b6mpZrTxZIY-XykJ66YYDkyrAHiHaJAildUS7W-ggfloqz62wlTztA_3bkHEKteQSPnn6YYHUvctgXNFLA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/NIGiOsnEfGKPTQO8h-5LA26xg09-ThCeNxIy-mh_6gQ1dTJCMTE2YHQ62uro7fA8OdfSq4LL7bgUSv1Ijpxix2CLLxu79XXI_37p1o_xmrIOkyeSJYq5bvKkh3OFfXzAC5yrFvYeTeY6_a8YM5rd9TztYRTQ9VT1Tc0HKXzIgyYwOqkbP3MH8cFIO47FpYwyOpBEnbV0fiHZ7YfLUd_jktXU0rE66tjOpIz5g2K1-Hff_wTWPNyyv9pxzCRUERRGSUwQShvInhuDr2kDQbdZbBDD4hF-ufT3gIQIn2gyfJ_CcQLpOUEUMKLma0ilOVnJL7J3tm872KtZZtKyVQ0j8A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Bf1lVRvODw_5AY19oE8yaS1a2L36EKHh33BhB8yWXeAEuDldv2GJKrMHSaSYIHAjrBpwCzpEFMJf3467I02BE6Z8iRc1eM7G6ZtzxC8ymeWLvzuJwQSvcBcNfPioBCYDgXqmCS1JomFI6w6LrkLmVRK33VRrK_C4IUwSgB7TdPkNi1VQI6ODeGWaAev2sjTrVk4KidDvuXzWUY06TyJ-5nSnFqjFMWmGPvnEstdhbPyNlS6_pKS-BX4BapKlpQ_jwpnAt-h60Lp_5ShBiBg7wqpAXdOOXvuWhJlgJc0UIrxbLiusjsd-B7PGmnkBw8AVjubfi-55LOyU9d13OuxPTA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/mWHzfPHyqSzL4yr-TR7tf3RE15JIo4Z5xB7gCbHTweQXS2ifJ81PYofhtkkczKz5l9bTKrUS0XYhqDr3I2uPiUWjOMKzyCGFoBmR8rAFSgVM8cIIJwCf3JvxcFWZP04OWo5dCf_2rM2NsICAH94CzUKMGD1KdhAvC_iF80t1otHdlv3xI1Y9FAvBGL_3W8I12rgvMIcKmOC7lN7OL5xfvuLv77ZvaR2857LlFF-BM2CoRlW8mhooHUpuD1LGWVUrDPI0CQVJHK38Inl2Ur0jygsZH0QgU0ngBLDkmghkZ1cmSg0h450Nq810YAHefXZnLZgXRe2GQnCPWfS_lHzIKA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/urLaJCPIAe440AFGVX70JD8DICoo_bWkho_QPyIvcrDRFo2S4rx-TFIlWZ7U9orrV1IQEeZ648OaJ9TxZ9b7KUtbpvtW-iPbK8tskIIJH_5o15vwzo6aSORGcCo9atX6i78JPsHjg3AJhri6Zkkojz7pj3h-696uBNKEN3RgZZvv4ZV2BtcWEbI7SbMO0h1mD_fPuCMpKRpMMn1qVFbxu8FMEAsJFxhnl-d_C1QTiZ5z2DzpM3cS2iUf4vpIqy7wZGpmvk8IPenXwFTt2hubgCAt9BXfTbb27U1yHF9z-_9RWbLM7Pu2tYQKCDho-3-hdsmc5eg_b3JrWr1eZrmlpQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
حضور رئیس شورای شهر تهران در خبرگزاری فارس
🔹
مهدی چمران صبح امروز ضمن بازدید از تحریریۀ خبرگزاری فارس، با مدیران این رسانه به گفت‌وگو پرداخت.
عکس:
صادق نیک‌گستر
@Farsna</div>
<div class="tg-footer">👁️ 5.1K · <a href="https://t.me/farsna/441213" target="_blank">📅 20:55 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441212">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">سیاست تکراری آمریکا و تحریم مجدد ایران
🔹
وزارت خزانه‌داری آمریکا چند فرد و نهاد ایرانی و چینی را به فهرست تحریم‌های خود علیه ایران افزود.
@Farsna</div>
<div class="tg-footer">👁️ 7.26K · <a href="https://t.me/farsna/441212" target="_blank">📅 20:34 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441211">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/e9I0gNginCMQmq6qkwdbVUmYlFzV6MqmCUPLrxJSNpltxW9EXE4_GGHXE1BnVuSnhqfTSFj5DFGz1rD4iIiaGwoB331hBnei4cIkc-tC359MzPdKWdPB4ek_tQ-33q4eDkU0Oq46cm7Xo80urcddvMdp_X6tvEwSLi1yg8GQGjp3wtvxgdU_ObX6nocjkbppHoiEdzKaiEc1z4-bFxbAoOQwn7rLloHP3kJl5g487BnInCvcSv0jC6x4mQcYv5CFZ8syNfuGO7AlMUyZ7veKokrdRcqu4mSM7oEifON8sEfexr_-94cjhtGlP_i_bZ_TXPsn6hSOjfZMlILEEcjlIQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
پزشکیان: تهدید به هدف‌قراردادن زیرساخت‌های حیاتی نه نمایش قدرت بلکه نشانهٔ استیصال در برابر ارادهٔ یک ملت است
🔹
ایران با تکیه بر دانش و توان متخصصان، وحدت ملی و همبستگی، در برابر هر فشار و تهدیدی استوار خواهد ماند.
@Farsna</div>
<div class="tg-footer">👁️ 8.61K · <a href="https://t.me/farsna/441211" target="_blank">📅 20:22 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441210">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">🎥
خبرنگار: آیا به حمله به نیروگاه‌ها و پل‌های ایران فکر می‌کنید؟
🔹
ترامپ: به تو نمی‌گویم، اما می‌توانم این کار را بکنم. @Farsna</div>
<div class="tg-footer">👁️ 8.89K · <a href="https://t.me/farsna/441210" target="_blank">📅 20:19 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441209">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">🔴
سخنگوی آتش‌نشانی تهران: ستون دود سیاه رنگ در جنوب تهران مربوط به آتش‌سوزی انباری در میدان قیام است
.
@Farsna</div>
<div class="tg-footer">👁️ 9.2K · <a href="https://t.me/farsna/441209" target="_blank">📅 20:11 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441208">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">🔴
حزب‌الله: یک خودروی نظامی ارتش اسرائیل در شهر القنطره هدف پهپادهای انتحاری قرار گرفت و در آتش سوخت.</div>
<div class="tg-footer">👁️ 8.89K · <a href="https://t.me/farsna/441208" target="_blank">📅 20:11 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441207">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">‌ آب شرب کوهستک و ۱۰ روستای اطراف تا فردا وصل می‌شود
🔹
مدیرعامل آبفای هرمزگان: عملیات اجرای خطوط لولهٔ جدید برای تأمین آب درحال انجام است و پیش‌بینی می‌شود آب شرب مردم شهر کوهستک و ۱۰ روستای اطراف تا فردا وصل شود.
🔸
بامداد امروز درپی حملهٔ دشمن آمریکایی به…</div>
<div class="tg-footer">👁️ 9.51K · <a href="https://t.me/farsna/441207" target="_blank">📅 20:02 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441206">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromرفاه خبر</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/l4bI8nr_QISTr9MJxGWBQoLtwGEuTEgf3kYQMJGMPF_5S1luFDOWoPeEqJm1HsOeT7nO2SLWE7SJh2NAimkZKiN9eFtSKu_aikMliHrSNs0o8ElGCuARl3ebhFUvTNtNtrHNRsNzHxnMg5Tgo-eCTJV28k2lxJHmW3ABKoV96esEJFblrXzVGQfhyqutyeWpKbnh3fjG61RW3n9q3ofXxn24JAqiFxdKH-8S9RnYulQY67h2W3btXkCvzB5kwzrlXasF-2zkeFbwPzPL8JoLRb2myAI-U4trSJYZB5sMpu82iSF-RUcKwo3ILhQtIXACSFdZCzui-plBuN5QTLIYEA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🌐
دستورالعمل پرداخت تسهیلات قرض‌الحسنه ازدواج و فرزندآوری ابلاغ شد
🔹
بانک مرکزی ج.ا.ا دستورالعمل اجرایی پرداخت تسهیلات قرض‌الحسنه ازدواج و فرزندآوری در سال ۱۴۰۵ را به شبکه بانکی کشور ابلاغ کرد.
🔹
بر این اساس، به هر یک از زوجین واجد شرایط، مبلغ ۳۰۰ میلیون تومان تسهیلات قرض‌الحسنه ازدواج پرداخت می‌شود. همچنین در صورت احراز شرایط سنی (زوج زیر ۲۵ سال و زوجه زیر ۲۳ سال)، مبلغ تسهیلات برای هر یک از زوجین به ۳۵۰ میلیون تومان افزایش می‌یابد.
🔹
تسهیلات ازدواج مشمولان ایثارگر نیز تا سقف ۶۰۰ میلیون تومان برای هر نفر و در صورت برخورداری از شرایط سنی مقرر، تا سقف ۷۰۰ میلیون تومان قابل پرداخت است.
🔹
تسهیلات قرض‌الحسنه فرزندآوری نیز برای فرزندانی که بیش از دو سال از تاریخ تولد آن‌ها نگذشته باشد، به شرح زیر پرداخت می‌شود:
▫️
فرزند اول: ۴۴ میلیون تومان
▫️
فرزند دوم: ۸۸ میلیون تومان
▫️
فرزند سوم: ۱۳۲ میلیون تومان
▫️
فرزند چهارم: ۱۶۵ میلیون تومان
▫️
فرزند پنجم و بیشتر: ۲۲۰ میلیون تومان
🔹
این تسهیلات بدون نیاز به سپرده‌گذاری و با ۶ ماه دوره تنفس برای شروع بازپرداخت اقساط پرداخت می‌شود.
🔹
متقاضیانی که پیش‌تر در سامانه مربوطه ثبت‌نام کرده‌اند، در اولویت دریافت تسهیلات قرار دارند.
@refahkhabar
‌ | بانک رفاه کارگران</div>
<div class="tg-footer">👁️ 8.24K · <a href="https://t.me/farsna/441206" target="_blank">📅 20:01 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441205">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromمشهدگیفت | محصولات متبرک و زیارتی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZhM2lxnC-ZNoS0UB9xtc6sBciuXqxy1GrjYiPHv0m655vsjHOFP6AckBp5--EYBWatpfbKwIhJtMqwHxsXlYqr09-Rskan4hzICxUpwmcIJNyfqxI-YQ1i1b_JJZswr5pEPbGoER7cp4fFpxDTHnpDXXpBFfQJ7f53zFSrWAGEpY70OYrPEhMEAnt4wH8Ei_ysnkAWhboyv5Lum7hKcuFqbOdI5mEDSaJAzthK4EfvpSu7y-xdafWYtlwj2MD_AOye1XC1zV5sfjUyiYJr6YbS2bHH8a5X_DjSK_Yak_icds6IFgDLCw04AF7h_7IBHRVORGlbZL1qawwtfj8uj3sQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چهارشنبه است،
روز زیارتی آقایم امام رضا (ع)
روزی که دلِ عشاق، بی‌اختیار راهی مشهد می‌شود
سنگ روضه منوره؛
قطعه‌ای از حرم مطهر رضوی، برای وقت‌هایی که میان تو و زیارت، فاصله‌هاست
✨
✔️
دارای شناسنامه اصالت متبرک
🎁
به همراه هدیه
‌
📌
بهای سنگ متبرک روضه منوره؛ قالب دایره 480.000 تومان و قالب مربع 380.000 تومان
‌
💬
ثبت سفارش و ارتباط مستقیم
@Mashhadgift_sup
🔗
برای دیدن سایر متبرکات به مشهدگیفت بپیوندید
👇🏻
https://t.me/mashhadgift_com</div>
<div class="tg-footer">👁️ 7.23K · <a href="https://t.me/farsna/441205" target="_blank">📅 19:59 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441204">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-footer">👁️ 6.58K · <a href="https://t.me/farsna/441204" target="_blank">📅 19:59 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441203">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">🔴
حادثهٔ دریایی در نزدیکی تنگهٔ هرمز
🔹
سازمان تجارت دریایی انگلیس: گزارشی از حادثه در ۲۰ مایلی شمال‌شرقی صحار عمان دریافت کرده‌ایم. موتورخانهٔ یک نفتکش ‌آتش گرفته و خدمه در حال تخلیه‌شدن هستند. @Farsna</div>
<div class="tg-footer">👁️ 7.92K · <a href="https://t.me/farsna/441203" target="_blank">📅 19:53 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441202">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/344d92cb3b.mp4?token=az3q5RojM_7ZyX6t9IwO7WKZ6dbmHHBN-SdB3t9GvxjANXQkk_n97De5kw8C33WGgUGUqepzARLq-ng7T8Frrm1fXT5oTRU7yIUMzQpCpmWpu3abELCOeqXhJP1wmrstL9uipbjUyOfrpu51gvbKdIc1bqiVKk90MQ7AFFkRoHIG7H_BdIaTcn2W9OQq64Jm8t0ErxMFYD30ruXpoxs6WI-R7119IlxIAEBOH_N4lNrIa9C4XWCXkWPnqZpAFL7l8NfqyieWbM1D2qJ5RyUwf6FA-esOWq960XhreuhmsNnn2oX2CkiYKVFtte2M0wptkQHXkTNRrGMTv5vXWfbSAQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/344d92cb3b.mp4?token=az3q5RojM_7ZyX6t9IwO7WKZ6dbmHHBN-SdB3t9GvxjANXQkk_n97De5kw8C33WGgUGUqepzARLq-ng7T8Frrm1fXT5oTRU7yIUMzQpCpmWpu3abELCOeqXhJP1wmrstL9uipbjUyOfrpu51gvbKdIc1bqiVKk90MQ7AFFkRoHIG7H_BdIaTcn2W9OQq64Jm8t0ErxMFYD30ruXpoxs6WI-R7119IlxIAEBOH_N4lNrIa9C4XWCXkWPnqZpAFL7l8NfqyieWbM1D2qJ5RyUwf6FA-esOWq960XhreuhmsNnn2oX2CkiYKVFtte2M0wptkQHXkTNRrGMTv5vXWfbSAQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ: ایران مدام ما را احمق جلوه می‌دهد
🔹
ایران مدام ما را احمق جلوه می‌دهد، چون با چند رئیس‌جمهور خیلی احمق سر و کار داشته است. خجالت می‌کشم بگویم چند آدم خیلی احمق اینجا نشسته بودند.  @Farsna</div>
<div class="tg-footer">👁️ 8.56K · <a href="https://t.me/farsna/441202" target="_blank">📅 19:50 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441201">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4d250ea597.mp4?token=FojrtapEeuatsXhvI_j-Cp6wOHzwGDY51FFe1OqYGMtAGyz7rujZ7oF4Haib9P3yoTpCtIzrDzRBdI5CoiLhIKp9dn7eZ3n7ax_qAeFWAAwnmRzZ1N6dfAJGwHTu15IBFnYodp8-3qKU_6K5qAH1WFoC-a4YEKK2YiXeijDw6Yjqcbqi0eBKGgMiBSqm2lx3QDrTmfcS2a68gLVxEkcZ_YJmfstXx1l-hjKuB8571Sz6GeDqRnff4b7iWYJJyK6AT6CtuWLXDozoYlkthiACZP9x20_-etH7JYy0qPQw2Fkx1QlTiGu275H7x1dE6cGyhMmSiGGz8aPUbkgrLw_lkA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4d250ea597.mp4?token=FojrtapEeuatsXhvI_j-Cp6wOHzwGDY51FFe1OqYGMtAGyz7rujZ7oF4Haib9P3yoTpCtIzrDzRBdI5CoiLhIKp9dn7eZ3n7ax_qAeFWAAwnmRzZ1N6dfAJGwHTu15IBFnYodp8-3qKU_6K5qAH1WFoC-a4YEKK2YiXeijDw6Yjqcbqi0eBKGgMiBSqm2lx3QDrTmfcS2a68gLVxEkcZ_YJmfstXx1l-hjKuB8571Sz6GeDqRnff4b7iWYJJyK6AT6CtuWLXDozoYlkthiACZP9x20_-etH7JYy0qPQw2Fkx1QlTiGu275H7x1dE6cGyhMmSiGGz8aPUbkgrLw_lkA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ: ایران باید توافق را امضا کند
🔹
رئیس‌جمهور آمریکا گفت که ایران بایستی توافق را امضا کند. او گفت که این توافق یک توافق «خوب و معنادار» است.
🔹
او همچنین افزود: «ما امروز دوباره به ایران ضربه خواهیم زد.»
🔹
رئیس‌جمهور آمریکا مدعی شد: «ما به حصول توافق نزدیک…</div>
<div class="tg-footer">👁️ 8.92K · <a href="https://t.me/farsna/441201" target="_blank">📅 19:44 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441200">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">🎥
پیراهن‌های ورزشی شهدای میناب که هیچ وقت پوشیده نشد
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.98K · <a href="https://t.me/farsna/441200" target="_blank">📅 19:36 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441199">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gRxcUWaAWCvO9jhS7nlNkCD-kVPY8PEJwHGAilyZaEJCcGEbRo7ERRJlfcjNcT98MXcriAxT5H6dGYtR6sfefsIFt3kujS-up8ycnmaLuLbxIRg3hK3zE5_s21Gq1l2ILGwM6EVgbu_E8Agx4K_oKus0KSBNkpPILs32FjMGON567-Pakp0zTrfGvnJKXicvpQT7_X0Rd8oNR0qI2kPnAf8-cgdSUt45e-GO9gBJqfhyYp1Il_kJ43J70gXdKDtc6iRDg9Jiv2JSYMF5nMtkcl5u1UNtzhdt3hRID03VPKMHiYZNojqDzqnp0dbtGm7vhOfG_4rihRLW2bfR-cbvtg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
کدام پایگاه‌ها صبح امروز هدف موشک‌های ایران قرار گرفت؟
@Farsna</div>
<div class="tg-footer">👁️ 8.95K · <a href="https://t.me/farsna/441199" target="_blank">📅 19:34 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441198">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BQ1DiOeI0opDSByyBMr_V4WDNIghUXjLPT_7N_ZiLklVPBtfV-SB7YP1EJCSJNz6VT7nmBcrR2Fh697_XmIe_68azu-7D5SF4eMTUaicefI4QvqvkltHzUqyYP7quK2KyS7cr5OZ9r-7elGZrKYd0dJ8tZ6CIl2FslFHdYRlEz9wp5UxSOElKdbP0PNztoCnpcMPqVZAL_ORSr-q_Hldb-4tImHcJSrgiEwPdsO_nfwOMg_lDt-5UMfEuu0NZWE4Rl-bwxaPEOr5bUwsIspWcMHhb-rjdkxsYyC5ZZcoaG_CjQR7blsgmPcbFLIFR0AaqlaQlyO4-aWg2YMq45dKmg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ: ایران باید توافق را امضا کند
🔹
رئیس‌جمهور آمریکا گفت که ایران بایستی توافق را امضا کند. او گفت که این توافق یک توافق «خوب و معنادار» است.
🔹
او همچنین افزود: «ما امروز دوباره به ایران ضربه خواهیم زد.»
🔹
رئیس‌جمهور آمریکا مدعی شد: «ما به حصول توافق نزدیک هستیم ولی ایران همچنان تعلل می‌کند.»
@FarsNewsInt</div>
<div class="tg-footer">👁️ 8.25K · <a href="https://t.me/farsna/441198" target="_blank">📅 19:32 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441196">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/K7dDTWydp2TayUSt8UZkYXPQ0fZCGye2_98YPywV8atyqoaeJvg8AJryE1KR3dv40e16DJ0Xu3OzpHO8OiL7OSqGEWJSfcFuG_OAIPhbsobYsT0OkkM0bBltaATgP5KZousupwUIAyprgOtOuXoMbtEfssQhTNKAKNzAbqrPU3lNbDpHJ1WoO849ZXfwPqkm3AVG5-Lx1-Ku4TP-EyM-nl77Xqu6jzRYXFylXAK8uOQQKgC_Q4mdwJqzGKyfTQ9GuYVKiOFHge7q24m9_YAWcLzslCOJvnlPfl6KWspThlAANHi9WJVr-j4mIjV-fsIVJlCiQMsrEN3d50eL14rDWw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حملهٔ نظامی، یکی از گزینه‌های روی میز ایران برای رفع محاصره
🔹
در کنار دیپلماسی و توافق سیاسی، گزینهٔ نظامی همچنان یکی از راه‌های مطرح برای پایان‌دادن به محاصرهٔ دریایی است؛ گزینه‌ای که به‌گفته تحلیلگران، نمونه‌های مشابه آن در باب‌المندب و خلیج‌فارس نشان داده حمله به ناوهای آمریکایی می‌تواند هزینه‌های سنگینی به واشنگتن تحمیل و آن را به عقب‌نشینی وادار کند.
🖼
اما در صورت انتخاب این مسیر، سناریوی حمله ایران برای شکستن محاصره چگونه خواهد بود؟
🔗
پاسخ را
اینجا
بخوانید
@Farsna</div>
<div class="tg-footer">👁️ 8.97K · <a href="https://t.me/farsna/441196" target="_blank">📅 19:22 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441194">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ucmTpWt9exGjLYoWsbKCLFhEo6wOrxSpNe6Wj7xRfMys-_PAs6BGIxmOBeTC3RTVjRcbutmFDInSRHPFyBB9D_NQBnJvmmSBaYJqOXhTbSfZVNAi8OBEWn2Q_XnqtrKLA2xff_xQXZlsPvC49EGCvVQtY9o5a_B_8OiD2WKfjhrjuh1pA-_6Nk3a_pDAb32mMUaiC8BOISZcHAKbtQtSq4MrbsuISMm62yMiP_IDkV9jhS3G4hvl9Jh9m9ExzGlLYEiKX40GOL_qOcVFvZdiBCEUMyMPoCxoCRJuSjdx8wpriFFxo-GnsV1-bnXE4R62P-FGTbMw5Bul95ci6fystA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کارت سفر در راه است
🔹
مدیرکل توسعه گردشگری داخلی وزارت گردشگری: تا هفتهٔ آینده کارت‌های سفر در اختیار مردم قرار می‌گیرد.
🔹
مردم از طریق این کارت می‌توانند هزینه‌های سفر خود را در درازمدت به‌صورت اقساطی پرداخت کنند.
🔹
اعتبار این کارت‌ها براساس سابقه بانکی…</div>
<div class="tg-footer">👁️ 8.64K · <a href="https://t.me/farsna/441194" target="_blank">📅 19:13 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441193">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/636c92e66e.mp4?token=AWVidr9zIvnAJP0y3hs7UzHwXUvGXYIjyV1ECjgufMEeQ8ME3UCZsrszF4YEk6XJh3QRVVudd71FvKRZYs9g6EEVxo5ZR-omm5vonRUTmMWerJSgCXq8aikqYnq4jizFw69bfuaILJk52S_xMMaN7w4LWSmjjrV8YCcRrqzAGSGm_UFgmAGr_bGGbwqedJqYqo1kS4XSmxsRQlCz0q4EImRiXtc7c-gS_0eXBtjhTC2QXelS1Uthd9PFE9htilLBs35p-DtaFNmipVG_SFewV-_TtDzpd7AINWUM8YvxdqaEMoBmhTIpSj8sNesbB2F0mEnTzyU4igKL3scnCL6IxQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/636c92e66e.mp4?token=AWVidr9zIvnAJP0y3hs7UzHwXUvGXYIjyV1ECjgufMEeQ8ME3UCZsrszF4YEk6XJh3QRVVudd71FvKRZYs9g6EEVxo5ZR-omm5vonRUTmMWerJSgCXq8aikqYnq4jizFw69bfuaILJk52S_xMMaN7w4LWSmjjrV8YCcRrqzAGSGm_UFgmAGr_bGGbwqedJqYqo1kS4XSmxsRQlCz0q4EImRiXtc7c-gS_0eXBtjhTC2QXelS1Uthd9PFE9htilLBs35p-DtaFNmipVG_SFewV-_TtDzpd7AINWUM8YvxdqaEMoBmhTIpSj8sNesbB2F0mEnTzyU4igKL3scnCL6IxQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
تصاویری جدید از جنایت آمریکا در مناطق مسکونی تهران
⚠️
حاوی تصاویر دلخراش
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.98K · <a href="https://t.me/farsna/441193" target="_blank">📅 19:05 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441187">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/gwfUzKi78_EOVyusdCbvbw4R7hA5G6wnl1_iPMUeNfChWP6xYcbMScH1h0JbzfBdaGZj7UOarGBWEQXmwY5p9uRllcNa9PmxWJCfs-3iBboaLCTUUceN7nz2WyQFD2OnahPsgtLbmFgms_xWaaowco_BOi7J9WB5X-CidxBPvt9vMWOc4YGLlKo8QMTw6w9tSNh_YycWHkTJYm5sCdhrKqw0m3zvwFqUzWZppXu34F6SAZWRzl2k-NdiOSAttk6sHHQEyZ0WNnIK_hJCJQzXpLXCE0x3u07-9l9aE6h_tQzeoLU0u0D604E7RhjaixW1smYKPHadM7kjrunxqaWOLA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/suYMhaUwXHbRrKcH7K6sEEp3F1tIS48TxxHR-J8nTOKm1LIj1_yHXQ4kpLDGgj5R1nrS3Df6rU2kXFgajw_Bq0VVN2NhUxLSLfIF8sQsQ5zCp4rqJ89lg994NxIFsyAvPxHMZe4izMEy4J4leG3UyzDl7kWgCkkObFtSh5sheufzMuDW5dbkpYo1Oq3W8QymQus8_17mMRJUSCa56GIBoe3UZ94MEh202CTaS1fBrV7PIoAlbzWZAgZY7k4r7fjJducbL_bdKyZPStr4CWzUx7R7fJfxuPLIUlqNwyg2wOQInQtX0aC9xHbCVOm5p6rG4d_jW1l0E741ERU7YyyoDQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/oUcAXjMBulNHof-JNs3ZQpx6LO5YGLdIztth0QweNSoSQbxbnQyQbjpXvTXR2XbOvGM1epX9F9Fi9qkOZNJYjM3cRHTT4Q0mc9-Fr_BOBO2MLbTqJEnTy3LQxQBsPS4EZvuHYURL2d3O5HK7R9bVH2x-KmJdyik8YEaqC2Ow-86kca9JggInV5d1IlJteC_kyvmz_VoQkmeIFu45RKVIqZ6n5W-PmlG1iK_yhPMPIj8TTu6UVpnG7zn2LFrIT6DxZxVImaUWCFm49u9jL0IhD4XXKgUdD5yptOLNAo46vqMKo_BUHwuNa1TTmT-qFZyayMbrF0I4c5F84duIo7Z7Yw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Yiuz_LcEHfzDYuc5XR_ySGX2Tfh670mBVODjCWQOSQ82eTWEvA_bGEE4QW8egUFMWKa-d1XAn6zQ5hHUfSgfw-nvr8bP-E0sodMgU9sbedngOgrRd3g2-S1lbm1l-oryiGW7HEGlcjKauQS3VWxuEyhmAsx4cgymFDiiqbhBGG4b5jJtHXFDcAe8vOaZ612A934tdXpNRQwPGHuSrdpVsYmQ-KLpPFDspU2-6yLL3WM-aa4mwkF-jdjCTNLW9izNcA2VtuMwYCPajcCksApqhG79WT70CMy2XE6TuJmueWnIJck5r9tjb79PNsEUjxZbz1ZSQtRx7Jr1cNs0WXSsVQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/CkFNO2LVK84Sg0Iu0E63W_0zVcFKGyFJj60fUGgx_pfb5iePFokMdisD188hkZqVKCFo8FPWVqUb5Y1-7Jrf8YTEjpbauYDQXI2IRHyIEWpXtX8E1e-4iP59jx79GK7xtxUz1ivti45-0Gx-5GvOjUgXjKHS-QvjFi_cWPAT6Z2tKHTyWY6hqe9UWbIU4AO_dyN3zL1APSFwEajQLxKOWtoy8yhzNRuOCLrD0PGwAJm1WotaTq4pOq-t6PRAAwnIX0tH06WbQGCxEUogdoEknegX8ACUXO4D_w4ZGSD-k7X2N7Eq-irneopL6-iPfCxGf-8ebqm6BxJLLYnIQzSmUg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/eiuSi6ncjFPnMsqBDSGRk6gtwcnLtcFwF6NUTHMyS-a8eA65qzJE87bF7D4Xn2hbJdivX9ff9JYIHDM0BGSIsRBe7_HmR6dgQx4IoWjkLmGr0yfsjSahxrxhbAShva8IRnoVIedut3_bs3o0VM99HMU_ZmlkDp05zsXaHw0lMM_u3e2_47QtZItQmUbAuLbyySEzDxJVnhxZhOV4uV6epMh8-6-JwU4HMRWRyGP9LIjL40ihSiWyuiMshBSKJdOqxqAXbfRSOZPPqaK8kI3Qv0jQ5xNVZeFcp1QIuLabORQfgEQ9xPcJO8fcYfU5bi_95cxcLw_7f6VeG84Mqn5OzQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
بازدید رئیس شورای شهر تهران از خبرگزاری فارس
عکس:
صادق نیک‌گستر
@Farsna</div>
<div class="tg-footer">👁️ 7.97K · <a href="https://t.me/farsna/441187" target="_blank">📅 19:04 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441186">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jHIeM6ArFagk4UW350j87JTlme8N39MYQYJYSQGvbRkzYQdrtaxLUe4EbC8AJ493wp-NiaNynj__irRUbNN_fNv2IQpUsN7K4x-UgnWcPf14LUGxOBIK4s2YG8pcCSOaRZydCF08BAlI50-4FmS--mIJ5ioc0xMoq-ESNSjCg3u1EtOOUGYmffaQixTZz43Qq1yzpsAF34bA9Mw99acNEj_9T0vL_4_k9YT4m3GioZEepwgdNsiqtYZZR1UTd3zmtco3HycT3v0WLezdZmP4GT4AOsnCp3rttvzOivxHZp78fc-z1ivRR5EGmOvYFSaNV2imNhK-QXPJDaEWLN5_BA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عضو کمیسیون امنیت ملی: طرح تنگهٔ هرمز آماده است
🔹
کوثری: همهٔ اقدامات و بررسی‌های لازم دربارهٔ تنگهٔ هرمز انجام شده و کمیسیون امنیت ملی مجلس نیز کارهای تخصصی مربوط به آن را به سرانجام رسانده است.
🔹
این طرح پس از آغاز به کار مجلس، در دستورکار قرار خواهد گرفت.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.93K · <a href="https://t.me/farsna/441186" target="_blank">📅 18:54 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441184">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0df9792bbe.mp4?token=oTTpgcyNOka6IO75imktQawtiiEp8nohUXlG5eMjYGh-9mp6Ynm3jLfHX4jNpKGYT5uYfgNZtzUu8i0fUjxh4Y7zFRnWhQmm3yD7umwGfhqXPBK_t5UxHeynv5NgW0N_3QbgV_jUTTuqiAUqhTz7TWq5iWbjAwCLavmpRTKH7y9ptyF_CefJwux-DJV89hKcN4xHA2HLnQcYz08nDrVkUME-k1q5ldXmQvblYhWRAsdYCXjWMp5rNr52imOp7Xb3TASnd28Xn2T9iCmIqWGqDf3lC0amvn-POMLLPNKZg2ezYn51aR4LIj2_3cTCQs-4r-kPDTtGPkS_AQ5SapTrbA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0df9792bbe.mp4?token=oTTpgcyNOka6IO75imktQawtiiEp8nohUXlG5eMjYGh-9mp6Ynm3jLfHX4jNpKGYT5uYfgNZtzUu8i0fUjxh4Y7zFRnWhQmm3yD7umwGfhqXPBK_t5UxHeynv5NgW0N_3QbgV_jUTTuqiAUqhTz7TWq5iWbjAwCLavmpRTKH7y9ptyF_CefJwux-DJV89hKcN4xHA2HLnQcYz08nDrVkUME-k1q5ldXmQvblYhWRAsdYCXjWMp5rNr52imOp7Xb3TASnd28Xn2T9iCmIqWGqDf3lC0amvn-POMLLPNKZg2ezYn51aR4LIj2_3cTCQs-4r-kPDTtGPkS_AQ5SapTrbA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
درگیری حریدی‌ها با پلیس اسرائیل در قدس اشغالی
🔹
صهیونیست‌های حریدی در پی اخباری مبنی بر دستگیری یک جوان حریدی که از خدمت نظامی فرار کرده بود، جاده‌ای را در محله رامات شلومو در قدس اشغالی مسدود کرده و با پلیس درگیر شدند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.53K · <a href="https://t.me/farsna/441184" target="_blank">📅 18:52 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441183">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">🔴
حزب‌الله: یک خودروی نظامی ارتش اسرائیل در شهر القنطره هدف پهپادهای انتحاری قرار گرفت و در آتش سوخت.</div>
<div class="tg-footer">👁️ 7.63K · <a href="https://t.me/farsna/441183" target="_blank">📅 18:48 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441182">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Iu5MY86x4pJTiYK4EgESgfxufEa16aqUwIXv-JzK1vK2DS7Hu2GyiHwlIqc8iv9gEKUzDfZklEUWX5WA5c6znMb-qm81Z5Ao_Hgq0nlCrTArgFwxLvgpgICNJ4oLV-tVaDG1Bhs_SKQqXatphOP8PZwkbF5jOF_dvOphiVfb1zv0-mirepuqRjd6Aa9Flv5iDOgAhc5MotYvsiCXZT7ZUtAbr1j2zT-hBNgZ5dg6SSN3zt-qVUQB2x-8XCzsl4ribtUbYHcWwZ6kpPCtzrMM5MiNHihNgRNYyBBTeYMnu1TK1st8kY4xc-90tD3coBljMbrrBJKNqytyBE3JlHlyEQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">طارمی: سیاست‌ ویزایی آمریکا باعث تنش در جام جهانی است
🔹
مهاجم تیم ملی ایران در مصاحبه با ESPN اظهار داشت: اقدامات دولت آمریکا در رد برخی درخواست‌های ویزا و جلوگیری از ورود یک داور سومالیایی، به وجههٔ این کشور آسیب‌زده و باعث ایجاد «تنش زیادی» در فضای جام جهانی ۲۰۲۶ شده است.
🔹
در ۳ جام جهانی قبلی که حضور داشتم، همیشه وقتی وارد کشور میزبان می‌شدیم، حس صمیمیت و جهانی بودن فوتبال را احساس می‌کردیم. اما متأسفانه اکنون چنین حسی ندارم.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.23K · <a href="https://t.me/farsna/441182" target="_blank">📅 18:43 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441179">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/s_KBjP3r20Y7D5xNOc_M9ICIfxduv9AtFYDK1P2LqgZwiR3yvYzamd-tPmy2EWybUMhBamVUYx8C0_0sL_4gGmiWZBoopW7KX0lfNxZogj2b6w1fAP2HHZgO0m1oYFfItJFQ29xyp4z87tRQq4LDm4TPcUCUj0uT4vE0-NAYkSBetZx5rTDIc2bamGWG7wlJVQdn5DmZl-klxxcvAXyNE2NlGT5-q820bjsK_wHavwJkFOU4soZsc7RKo-is9pwuNMLpPyJ-Jlys2DaGVTeXE1hv4V4EL8GUrkrPjveQfPr7LgI9JFyGAU2WIIFu0SPzZJobb1JzUqkqgixFdrkjDg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">۵ کشتی محاصرۀ آمریکا را شکستند
🔹
پایش هوش مصنوعی دریایی ویندوارد نشان می‌دهد که ۵ کشتی حامل گاز مایع که با ایران تجارت می‌کنند، محاصرۀ دریایی آمریکا را شکسته‌اند.
🔹
ترامپ ۳ ساعت پیش در تروث سوشال نوشت: «هیچ چیز از محاصره عبور نمی‌کند مگر اینکه ما بخواهیم. این یک دیوار فولادی است. ایران هیچ تجارتی ندارد.»
🔹
ویندوارد اما با تحلیل داده‌های ماهواره‌ای کپلر می‌گوید که ۴ کشتی محموله‌های خود را در هند و یک کشتی در پاکستان تخلیه کرده‌اند و صادرات ال‌پی‌جی ایران ادامه دارد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.35K · <a href="https://t.me/farsna/441179" target="_blank">📅 18:28 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441178">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/B0S7NIiMysvcOClfQ7AJJWe17wnsh3hk0fSLMcqbAtJ_RKxqZGHTAkyd4d721_mz_aFf4Xm515yOkHC_Ucwy6cWeso8rw36s1fh61Xqw-Xl2zlI67P5Gm37IpVTbZVWQFqkBc68DB49YzDtzH16355xllsbMyiyPNcU4B6dXViSrm0JfsCpSQjhOOgMBwdop_qGry8QgX38Plxmh3FUo6r6rC9ppLBUjyUYoK8aecgf7uzc3rIhcbe5TZ-gfzr36Yrd2rjyJ_pTzyI_o7vhgCbS0lL8Y4TEt_HBlanFA8wEhG5DKdB31auzrbuQw1YqCsTI9kbzIv1qguS6WBYWhWw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سخنگوی ارشد نیروهای مسلح: هر تهدید ترامپ را با تودهنی پاسخ داده‌ایم
🔹
به‌هیچ‌عنوان در مقابل نظام سلطهٔ جهانی و شیاطین عالم، به‌ویژه ترامپ و نتانیاهوی خبیث، کوتاه نخواهیم آمد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.44K · <a href="https://t.me/farsna/441178" target="_blank">📅 18:23 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441177">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">‌
🔴
ایران: آژانس به ابزار جنگ‌افروزان تبدیل‌ شده است
🔹
نمایندگی ایران در آژانس: چطور می‌توان به آژانس بین‌المللی انرژی اتمی اعتماد کرد، وقتی به ابزاری در دست جنگ‌افروزان تبدیل شده و چنان فلج و بی‌خاصیت شده که حتی نمی‌تواند یک نگرانی ساده را دربارهٔ گسترده‌ترین…</div>
<div class="tg-footer">👁️ 9.64K · <a href="https://t.me/farsna/441177" target="_blank">📅 18:22 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441176">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">تصویب قطعنامه ضدایرانی در آژانس اتمی
🔹
الجزیره: شورای حکام آژانس بین‌المللی انرژی اتمی قطعنامه‌ای را در مورد برنامه هسته‌ای ایران با ۲۱ رأی موافق، ۳ رأی مخالف و ۱۰ رأی ممتنع تصویب کرد.
🔹
گزارش‌ها حاکی است روسیه، چین و نیجر به این قطعنامه رأی مخالف داده‌اند.…</div>
<div class="tg-footer">👁️ 9.3K · <a href="https://t.me/farsna/441176" target="_blank">📅 18:20 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441175">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/njZONvoZThRC9EBfE_NBFm8TBx2-21qT2BK7Qc72Sxkw870T_vW1SvGZ0krI-l3_AJrrM4orJtLoZ6GnS_t9Zp9ts-whciKUSjvMbZ4ACkjBbwkjZbckjEp4tnE-U7koTVdW2ymoK9doSPi_PnqjhV9GVsKt0lbibupD7TyqUPt_-SaUGpp2p3W-dt4EHWd3Yqx9sHU77ikf1AE2v-QvAPY6hZnp4pQ412zL3Dy4ApnmQSRwOz9BgpFaRSE04phNI7wSTLk0apVQl8viAJK12nft_XQmF6ev2XvnTB4ro98qOqVQZdM5a2BJ_-u2L1iQruBxqY95Q2tLE1CqjDIWig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پرواز استانبول-رشت برقرار شد
🔹
نخستین پرواز مستقیم مسیر استانبول-رشت امروز در فرودگاه بین‌المللی سردار جنگل رشت به زمین نشست.
🔹
این پرواز از این پس به‌صورت هفتگی در مسیر رشت-استانبول و بالعکس انجام خواهد شد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.19K · <a href="https://t.me/farsna/441175" target="_blank">📅 18:15 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441174">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-text">تصویب قطعنامه ضدایرانی در آژانس اتمی
🔹
الجزیره: شورای حکام آژانس بین‌المللی انرژی اتمی قطعنامه‌ای را در مورد برنامه هسته‌ای ایران با ۲۱ رأی موافق، ۳ رأی مخالف و ۱۰ رأی ممتنع تصویب کرد.
🔹
گزارش‌ها حاکی است روسیه، چین و نیجر به این قطعنامه رأی مخالف داده‌اند.
@FarsNewsInt</div>
<div class="tg-footer">👁️ 7.88K · <a href="https://t.me/farsna/441174" target="_blank">📅 18:14 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441173">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/q3UuUBxejHRoud3Bu1ucu6bqBuPvYFW6ujZNtw2PqKQ62lwZopmmt3m7Rr-6EI-H_deSnT4CJPkYLBF7b0ZLbS_oyq9mV3jf-GMT2ZLKKYYJ_qIzapsNkG8FTeSUYVOV0wfDb8Rjx7phgmXqwBQQOOKX_0_ScOb_99nRerxB2jrJDStOYFPXFDuCqiBRx9alF6oLiwhT0wlY7LlhLqM5QgD1g3bJ-1s3c6L9AuKOSWdc6oKRf4nKf9SjfJ6u_LJ8tBlZ2TwjfiCTmdXUsoW7-hWlp_IXdKiqJySpWGGWLHZGbDaCvaHgvt3huBqE0jUUev0b_FhNMO5G3AjxF_rFVQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبر خوب پلیس برای متقاضیان گواهینامه
🔹
پلیس راهور اعلام کرد مدت اعتبار «برگۀ ثبت‌نام و قبولی مراحل آموزش و آزمون رانندگی» از ۲ سال به ۴ سال افزایش می‌یابد.
🔸
با این تغییر افراد در صورت طولانی‌شدن روند آموزش، تا ۴ سال نیاز به ثبت‌نام مجدد و پرداخت هزینه برای دریافت برگۀ جدید نخواهند داشت.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.94K · <a href="https://t.me/farsna/441173" target="_blank">📅 18:04 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441172">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">🎥
پدر و مادری که فرزندشان را در حملهٔ لامرد از دست دادند
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.23K · <a href="https://t.me/farsna/441172" target="_blank">📅 17:57 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441171">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Q5yWbJgv2QPoh46Prns7U-tYd7uhKAszOwGX9UO9CJbf2-IoK5HetRbr4vG5c6-udixJQIf7jOq5XxI_5ClTBwL6a1DcxIOBDQRmJRUXkMZKgqE0NbX6QMKPM3vuI0b7C9oxw8cSOOloStuvVOpqO_hXtbpjSSZ2VBqgjOScAAJFwwIq1aw06ksxAg-hKtYtQ8acBvsKEDptLRcqUfRCTMCF4GFOQoisGHtm_wGXJ5eiI8BRPZK-WZcR1v1HyWmbm9WmjOLV26qVIlAJd458QvFrAWRR8fn2sNTFEW45Yj-Oc3XFZ3Wuh_H1zLzQFSUwcQMwJHbcKPjYze_ctfYSxQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عبابافی نائین جهانی شد
🔹
عبای نائین به‌عنوان سیزدهمین پروندۀ ایران در حوزۀ نشان جغرافیایی، در سازمان جهانی مالکیت فکری ثبت شد.
🔹
عبابافی که بیشترین رواج آن در شهر محمدیۀ نائین است، قدمتی چندصدساله دارد و یکی از شاخص‌ترین دست‌بافته‌های سنتی ایران محسوب می‌شود.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.9K · <a href="https://t.me/farsna/441171" target="_blank">📅 17:46 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441170">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GmhOrgS1fV8myHE35JG09uDd-graguw6rgbkWfoG7e54wk9Tg3p0-26_oein4j14Erg8oX6FXmCvkjtMr5hWUXmq8CozxJQtxBjdJ4xdVdJiyuU4BuqVMvp93wY4xIifhCgRbFIz0DAOIrcZo-Hp6iQZo6EeKiCFGfCS5aFGYozmSe7WUFWDpQSKHbQ8S3pkMnNl01-qc8fwyxCPOYqbpwtOSgjwnICqYxSedh55TZBo_lWQPscQYENU3oUyF6UCILIlAimOk0i6ffvrKX_IxHI5HmG5lsnK1zd_XBPd_-XwI8wM5abbExmR9Op7kQlthXF1yclnGDi2mFSZv7CkfQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اعلام مقصران آلودگی هوا به کجا رسید
🔹
فلسفی، عضو کمیسیون کشاورزی، آب و منابع طبیعی مجلس می‌گوید سازمان حفاظت محیط‌زیست تاکنون هیچ گزارشی دربارۀ ترک‌فعل دستگاه‌های مسئول در اجرای قانون هوای پاک ارائه نکرده و بیشتر جنبۀ توصیفی و کلی دارند و عملکرد دستگاه‌های متخلف را مشخص نمی‌کنند.
🔹
به‌گفتۀ او، با گذشت ۹ سال از تصویب قانون هوای پاک، کمتر از ۱۵ درصد این قانون اجرایی شده است.
🔹
براساس قانون، سازمان حفاظت محیط‌زیست موظف است عملکرد ۱۷ دستگاه مسئول را رصد و موارد ترک‌فعل را به مراجع نظارتی اعلام کند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.38K · <a href="https://t.me/farsna/441170" target="_blank">📅 17:36 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441169">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6d26352c7b.mp4?token=FTkflXV5-L5vDgQYeMY80nHzLO25N5hSfhb-CU0Wmq_NYYJso6vD8A09PCijYKPtMXKNxX3r5FM1ksDsfGitkQakk1QYrU8lrzaYCA98TuHRQrALra6xqpwE6OKdmGNK6cr5mn1nhXUB4srVWSMnkDbatGxCLmMyTMWN3QNUE5sZyBgsDJFmej7HU9JdXtV61TLc2mZv5ZmTO4bQBA29BHIlW41NqIet3-gOj9zGc88k5Ricat3bZwEdGBdgyej0R8mJm5OmuFKwqTVPzf-RBMEpL3r3eq49G885wrh1Jntx_Y97WmgAIcX1uLkjmqtMDvmX2EX8Fr10_TubwaReAouYGi7-g7wbO44pcOVEFYryefbxNykKM0mOXxjIbJ4m3hQvjYC4XaDPVrAf0eTjxI9HZCtxEe6YdUHVs6xgm_iXYLsGgqSe5alyLPuG5T5htQfp0EyfugcLNH6QjQhVeZ-DU-Ht9POSHZpInxS7cK0nAZTPZjhLxZEK531kLnOC9LeuSMpWOCYLRClbILWfhyQiHfpvIdSgO5dJCJwgRW_8fWVPXsA5NMstvhwWhVpRY38oNBqcOhBWmTABpDUszNZ70x8brY-j8p5wnsl_HIRVUZG0UhO0sb6nHa6XU-ouM1-oHA7YJhhMmb8wrWkhY4dZi1Zbpu3pTjqkB06Pl7A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6d26352c7b.mp4?token=FTkflXV5-L5vDgQYeMY80nHzLO25N5hSfhb-CU0Wmq_NYYJso6vD8A09PCijYKPtMXKNxX3r5FM1ksDsfGitkQakk1QYrU8lrzaYCA98TuHRQrALra6xqpwE6OKdmGNK6cr5mn1nhXUB4srVWSMnkDbatGxCLmMyTMWN3QNUE5sZyBgsDJFmej7HU9JdXtV61TLc2mZv5ZmTO4bQBA29BHIlW41NqIet3-gOj9zGc88k5Ricat3bZwEdGBdgyej0R8mJm5OmuFKwqTVPzf-RBMEpL3r3eq49G885wrh1Jntx_Y97WmgAIcX1uLkjmqtMDvmX2EX8Fr10_TubwaReAouYGi7-g7wbO44pcOVEFYryefbxNykKM0mOXxjIbJ4m3hQvjYC4XaDPVrAf0eTjxI9HZCtxEe6YdUHVs6xgm_iXYLsGgqSe5alyLPuG5T5htQfp0EyfugcLNH6QjQhVeZ-DU-Ht9POSHZpInxS7cK0nAZTPZjhLxZEK531kLnOC9LeuSMpWOCYLRClbILWfhyQiHfpvIdSgO5dJCJwgRW_8fWVPXsA5NMstvhwWhVpRY38oNBqcOhBWmTABpDUszNZ70x8brY-j8p5wnsl_HIRVUZG0UhO0sb6nHa6XU-ouM1-oHA7YJhhMmb8wrWkhY4dZi1Zbpu3pTjqkB06Pl7A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
حملهٔ پهپادی حزب‌الله به مواضع نظامیان صهیونیست در ۲ شهرک الناقوره‌ ‌و القنطره در جنوب لبنان
@Farsna</div>
<div class="tg-footer">👁️ 9.42K · <a href="https://t.me/farsna/441169" target="_blank">📅 17:22 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441168">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YHz71K81YuRoa9_ahmBfkhyivMp0REn6maj3Uvx4ADUZHj-GeRU8E8GekTUFLLhCzwzdtUJg6pI1ZvAqOUIxs2c0srKnTN-sqEsw2pThalq5hporyT1I9VMHRwJWlEpX8WJYXWjfgrkRRa8GuNilOCT7j9Wa_z_Q4UNXqQ1RPT1SbpfGGG8fHYOI5e98WIUsORIkkV5yram-jNukfElJcwmzQTlwfvl4XMEf-6cGlq2DgOiDGSdSPcVqFMlzgy9JuwNXRg0dBySb9R_hHe29WNUhY7t3pN8w5m6YvXnh-iTvckKc1og6GJhAwNFxKqEfvZ1EreWAn9qfWe58Y1xXFw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بیش از ۲ هزار حاجی امروز وارد کشور می‌شوند
🔹
رئیس سازمان حج و زیارت اعلام کرد امروز بیش از ۲ هزار زائر ایرانی با ۹ پرواز از جده به فرودگاه‌های تهران، اصفهان، شیراز و گرگان منتقل می‌شوند.
🔹
هنوز بیش از ۱۰ هزار زائر ایرانی در عربستان حضور دارند و عملیات بازگشت آن‌ها همچنان ادامه دارد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/farsna/441168" target="_blank">📅 17:10 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441167">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kZfojin-8acRaFuds7TataHlXw-a9UKHomanK1GgzW-hrFabydMFORlzLy3THoYsy-JBYnFOvrrz136lsvz6JYZYReZJtAaJJDoi2KFXYha0qjWrChUJgVyBbBUQOqAhQNPYS1qaSD2FMpdS7cNkvzVJAkcd7xNGQDhP4c4DrcTYI2B27ei47oomq8J7IqjR2BeQJQYsFAoz5vqVuaXrXQiZHdlyFMwM_GjHtDO53H9vnmfq0QR1MENChcWJYVSNC7hfLdSAqevjmpb9voMpGzFYX1re42__FG-0LUfAP-DY7E6w-fnG_Z5Dk1TQgW6pBBsseQ9r27hhmOVy95C45w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">احتمال اصلاح مالیات کسب‌وکارها در بودجۀ ۱۴۰۵
🔹
رئیس ‌کل سازمان مالیاتی اعلام کرد با توجه به فشارهای اقتصادی ناشی از جنگ ۱۲ روزه و مشکلات ماه‌های اخیر، احتمال اعمال اصلاحات مالیاتی متناسب با شرایط جدید در بودجه ۱۴۰۵ وجود دارد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.9K · <a href="https://t.me/farsna/441167" target="_blank">📅 17:03 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441166">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c4b4ccd71c.mp4?token=Gsvqg9BRBAR2--p9RensZLDQn36e-O324SE_mF8z0g9cE9iVDo4Zt1Wr12PWFSPe3VCnNabk6ocBFjrZmSGT9otJ9vVhTyqzW7qqmJJ6lOr-2oC1_q69onoA-UUdpflwKpDmcUX01r81co0SkSI5BUXlq8oQlRK_rxJLC4IB3NHo5dKzXcI-QM0hztR_ltoLghC967fe2kuiVKrp4vHtQoPp3OKplxxRxOaO5AkJhHifhSURbs33Fy7Bb21mSVWwFVgq3U99fLNmkpTGpwZK63Jl1nBb-Ha-RDBGcxb0HS2kCpZnJPzj_xqrWNuB4gbl2FpgE-IOyciC9UJG4BWNUTzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c4b4ccd71c.mp4?token=Gsvqg9BRBAR2--p9RensZLDQn36e-O324SE_mF8z0g9cE9iVDo4Zt1Wr12PWFSPe3VCnNabk6ocBFjrZmSGT9otJ9vVhTyqzW7qqmJJ6lOr-2oC1_q69onoA-UUdpflwKpDmcUX01r81co0SkSI5BUXlq8oQlRK_rxJLC4IB3NHo5dKzXcI-QM0hztR_ltoLghC967fe2kuiVKrp4vHtQoPp3OKplxxRxOaO5AkJhHifhSURbs33Fy7Bb21mSVWwFVgq3U99fLNmkpTGpwZK63Jl1nBb-Ha-RDBGcxb0HS2kCpZnJPzj_xqrWNuB4gbl2FpgE-IOyciC9UJG4BWNUTzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
روایت حجاج از نگاه مسلمانان جهان پس از جنگ
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.75K · <a href="https://t.me/farsna/441166" target="_blank">📅 16:53 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441165">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rkwYy2AfQwa3zo4MDYJ1SGGrObe3zQbJYQRkzyjEApseEhFBLsbUaihPh4gDaj86N5xRtbHtS3bryUkJNshP3PD0nUA5rdVuFWp7Q5k-HYECEoe_d_qu1OrtV3o_85SHerntl6lyukfuSH4A56zzjy1rjI4VJ3A4kcOzjQZPR665mjh2WCzAqJGkbOFO3Tkf8xlIJeSciDs3-5O9FePHIa5r_Pg3ioSH3p9Cw5uqVl8mn_t5d2pfKwV0ZaFV-Gguk-xFvBIqlBBi6t63cvyBpOXkw6Rjj-MYx2r3OzUm7CSjoVVNLNHHKGWgjDPG2legvRHI0qJ9WWyp9gwCTnE-fQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">طلای جهانی در یک روز ۱۲۰ دلار ریزش کرد
🔹
قیمت جهانی هر اونس طلا در معاملات امروز با ریزش ۱۲۳ دلاری حدود ۳ درصد کاهش پیدا کرد و به ۴۱۳۴ دلار رسید.
@Farsna</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/farsna/441165" target="_blank">📅 16:49 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441164">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2d8867f73f.mp4?token=DiSRnuejqYBwdF3AaT6LYiXIeMTC2tWLabNr6g3VJu9dP8pQgJfdlUGtFdiCoDbE6YCeTbmGCuA-wqu8_YfArfgl1OkJHp3-fWXgAAgLXxAUjS2l2Dx2S7bw3c3Wjap5hdFKgOIOb57NCw-qEE3BOxdkcFHWqFP-uB3Ixh2wzkP3r2PC-pj3tFm0FgbaQ6u1cxbxadvB_utTRp8KnYakwKVAHEDhdEEmLzzYfR8qrkrWPSKooWnsRnPkF1n1TjyFplfThsQjH5MmXXtuNM9b53iCiNY13Ql2Y9v-nrfK7vxUlm3QEHoGL47Wp1FqXQdRjH97NzRj0GcxPJLfnTSbjw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2d8867f73f.mp4?token=DiSRnuejqYBwdF3AaT6LYiXIeMTC2tWLabNr6g3VJu9dP8pQgJfdlUGtFdiCoDbE6YCeTbmGCuA-wqu8_YfArfgl1OkJHp3-fWXgAAgLXxAUjS2l2Dx2S7bw3c3Wjap5hdFKgOIOb57NCw-qEE3BOxdkcFHWqFP-uB3Ixh2wzkP3r2PC-pj3tFm0FgbaQ6u1cxbxadvB_utTRp8KnYakwKVAHEDhdEEmLzzYfR8qrkrWPSKooWnsRnPkF1n1TjyFplfThsQjH5MmXXtuNM9b53iCiNY13Ql2Y9v-nrfK7vxUlm3QEHoGL47Wp1FqXQdRjH97NzRj0GcxPJLfnTSbjw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پایان کار گوشی‌قاپ‌ها و گردنبندقاپ‌های سریالی تهران
🔹
مأموران پایگاه دوم پلیس آگاهی تهران بزرگ در عملیاتی ضربتی، دو سارق حرفه‌ای به نام‌های «محسن» و «رامین» را در مخفیگاهشان در یکی از شهرستان‌های غرب تهران دستگیر کردند.
🔹
این متهمان در بازجویی‌های اولیه به ۲۰ فقره گوشی‌قاپی و گردن‌بندقاپی در نقاط مختلف پایتخت اعتراف کردند.
🔹
پلیس اعلام کرد برخورد با سارقان و مخلان امنیت با جدیت ادامه دارد و هیچ نقطه‌ای برای مجرمان امن نخواهد بود.
🔹
پیش‌تر نیز عامل سرقت مسلحانه از دو طلافروشی در میدان امام حسین(ع) و بلوار اندرزگو شناسایی و دستگیر شده بود.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/farsna/441164" target="_blank">📅 16:41 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441163">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس معارف</strong></div>
<div class="tg-text">دیدند راهبان صلیبی و اهل دیر
خیر کل آمده است به‌همراه کل خیر
🔹
شعرخوانی حبیبی کسبی برای عید مباهله
@FarsMaaref
💠</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/farsna/441163" target="_blank">📅 16:31 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441162">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e4625748c1.mp4?token=CmacFMgLvmy22bzndpACxbtQN4n36oXP78bklUOi6Ywn3LUSeptTNQvrVemDcNKRvm9rNouD602wJDofhz74E_5GU0bKPhtLGTKyWLLJd0uOoVfsL3xk4qqehmMMMjF2tRW_dLbisxmygHY8WcmRXoXSc06orUbb2fnZsdlr0W65P7mxrXEoG6SEru1_45w4zD6JY5fV5yVOZURJtknMqArESTKAKJ43bah5G-6smmWWR9kMutXo4ubovWNXllAhhbcJWOLxpTWUNJfL0l4K371Q9E9sGfCywzgCewG0Wy5ff9BAb0yys6oM-tiEG89ZETPxLxmydvlEecHDq-eFlQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e4625748c1.mp4?token=CmacFMgLvmy22bzndpACxbtQN4n36oXP78bklUOi6Ywn3LUSeptTNQvrVemDcNKRvm9rNouD602wJDofhz74E_5GU0bKPhtLGTKyWLLJd0uOoVfsL3xk4qqehmMMMjF2tRW_dLbisxmygHY8WcmRXoXSc06orUbb2fnZsdlr0W65P7mxrXEoG6SEru1_45w4zD6JY5fV5yVOZURJtknMqArESTKAKJ43bah5G-6smmWWR9kMutXo4ubovWNXllAhhbcJWOLxpTWUNJfL0l4K371Q9E9sGfCywzgCewG0Wy5ff9BAb0yys6oM-tiEG89ZETPxLxmydvlEecHDq-eFlQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔞
تصاویر لحظهٔ شلیک نظامی رژیم صهیونیستی به نوزاد ۷ ماههٔ فلسطینی در کرانهٔ باختری
⚠️
حاوی تصاویر دلخراش
@Farsna</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/farsna/441162" target="_blank">📅 16:26 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441161">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/01957eb299.mp4?token=GFju5wIZTPW76b8kSadUlAdBxQEJIT3ymqDnf1kFkMIal4KrL0Um70UDSqdA1PZoHwDJ3T1YZWjmv2lsosTfgJWhtzzQ3UysPQ_gS7IVDCk7tMd5NNSFW9O0QREessgGvFJVUzPZUU0eBaskaP04zqv9H9v468y5fdoGRWhs_VFLRpZ9EYPgv6rFBtIjOXxF-LMowbnT4vxqoRYwa_D5P0y1FiAdvsaD4Z_ZQ4egMqGUMyZjIuJwny15-vjIy9CfetNpn2F6Y8X6nhv1eUbDRxJsXT-CjX8hhMOISMbYDH-wzVCFR0EBgKs9oqS3QpSI9OkXCanHUP5fQmyrrPadjg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/01957eb299.mp4?token=GFju5wIZTPW76b8kSadUlAdBxQEJIT3ymqDnf1kFkMIal4KrL0Um70UDSqdA1PZoHwDJ3T1YZWjmv2lsosTfgJWhtzzQ3UysPQ_gS7IVDCk7tMd5NNSFW9O0QREessgGvFJVUzPZUU0eBaskaP04zqv9H9v468y5fdoGRWhs_VFLRpZ9EYPgv6rFBtIjOXxF-LMowbnT4vxqoRYwa_D5P0y1FiAdvsaD4Z_ZQ4egMqGUMyZjIuJwny15-vjIy9CfetNpn2F6Y8X6nhv1eUbDRxJsXT-CjX8hhMOISMbYDH-wzVCFR0EBgKs9oqS3QpSI9OkXCanHUP5fQmyrrPadjg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
فیلم دیده‌نشده از سلام نظامی شهدای دانش‌آموز میناب به رهبر شهید
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/farsna/441161" target="_blank">📅 16:23 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441160">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">🎥
پس از تجاوز دیشب دشمن آمریکایی، نیروهای مسلح کشورمان چه اهدافی را هدف قرار دادند؟  @Farsna</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/farsna/441160" target="_blank">📅 16:05 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441159">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/a74VSdhZBcDyK0bkduJdTJKlNzR8SH6mw-MV9hDo2BureZt1q_0s67yjAGqlHlIFFAWFKnM45s1_kcZVMuJFkKXoMKXX0KrrOzM-D7huRkMSFvHa_rrLHF2R-IK3zkqlZZZbAk2A0Cl1xbM9E6ia9b9TN5_TNTz-OZ1yevREccwfkBgdkWtr5jv-1SAzp-QRIDbBdd41dHOuCsA39Hz45KdwBjWH4giqrzKHt_qro7KTokQBv3gpKjrOo4VwDPbH-8Gu7-CsJUKacQUtwWqFEui2D7D2vuGAQDEgtRlMWmCQ0pQuRREzd8tKEa0FRQSSY_sCP-ivRXVjFlt4oTkG1w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بسته ماندن
تنگۀ هرمز کویت را به قرض لوله کشاند
🔹
براساس گزارش بلومبرگ، کویت برای صادرات نفتی خود کاملا به تنگۀ هرمز وابسته است. این مسئله باعث شده این کشور میادین نفتی خود را در حداقل سطح ممکن فعال نگه دارد تا بتواند از آسیب به چاه‌های نفت جلوگیری کند و بتواند نیاز داخلی به سوخت را تأمین نماید.
🔹
مدیر مؤسسه نفت کویت می‌گوید مذاکراتی را با عربستان و امارات آغاز کرده تا سیستم‌های خطوط لوله این دو کشور را به گونه‌ای گسترش دهند که قادر به انتقال نفت صادراتی کویت نیز باشد.
🔹
این در حالی‌است که به اذعان او «ایستگاه‌های پمپاژ و تأسیسات صادراتی، آسیب‌پذیرترین حلقه در زیرساخت خطوط لوله هستند؛ شما دیدید که ایران چگونه هر دو تأسیسات سعودی و اماراتی را هدف قرار داد.»
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/farsna/441159" target="_blank">📅 15:59 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441157">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GXeQUY92SezRHWYJ0q8qT3smUd6fY_VyMWGOw27Ks_LZ7Hu5SkWkovaYzteey2X5GDaK2VO3zEX_EoazezFg3TNUw_aD8hJnZ4VXgqUc144iOk5BJmvEd0zyB5qIKPv_PVbZG4zb3M0Ub_rt9jpXbJbZKXbkM4z0hayc5eocNDRCmEYEDkJ-f1MJv-lY0Oe6HWeI5R6sJMUris0D9kL7-5QMkFAqq6z8Kk7f-Q3c4-YaZSn8tZxaVzLA-vp_qWQQ2WRjU7asMY-MSz6Xisz6QG2fIyUnVBHettnPVFp41PN7ovopY6IHXQWmBcCVdHOotop8onE95JP35OmMRfFHuA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">صادق زیباکلام بازداشت شد
🔹
صادق زیباکلام صبح امروز با دستور قضایی بازداشت شد. پیش‌تر دادستانی تهران از تشدید قرار نظارت قضایی او به‌دلیل نقض ممنوعیت هرگونه فعالیت رسانه‌ای و تولید محتوا در شبکه‌های اجتماعی خبر داده بود.
🔹
براساس اعلام مراجع قضایی، زیباکلام با وجود این محدودیت‌ها در یک مصاحبۀ رسانه‌ای اظهاراتی مطرح کرد که به اعلام جرم جدید علیه او و تشدید قرار نظارت قضایی منجر شد.
🔹
پروندۀ او هم‌اکنون در دادسرای فرهنگ و رسانه در حال رسیدگی است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/farsna/441157" target="_blank">📅 15:55 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441156">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dc5c819659.mp4?token=Z86RWz9c2D_d03AVsgV4eY8HIMWggyCigluHBTwvv0lz0byo6janrRKD8ZrB4vWsVVDDA6RTvjjs1ayaY_G6cLcNnVweHWnE0YArX1_6tFDyq5mBu5J6LRICLaYYsRc8dmafG_l1Z-SPTuLAQ-IEoXdXQhNyGjMw5Bf6W9xNOqADUtwxDCwQYKpoEbhskjiLCJMtmcK2fzf5ZzwObA5914y70Qh4bhDIVvt9kKYm9EqzEUUE_MjqJ7Kj4UaPUuW9LgUzLEINN0yLIB7pGAUs4dEBQn2MTkuBglkFSeiXFyVzTWhOYWSTTJpAly1NjUFlfeNdlC4rrdqML0HxDH4vDw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dc5c819659.mp4?token=Z86RWz9c2D_d03AVsgV4eY8HIMWggyCigluHBTwvv0lz0byo6janrRKD8ZrB4vWsVVDDA6RTvjjs1ayaY_G6cLcNnVweHWnE0YArX1_6tFDyq5mBu5J6LRICLaYYsRc8dmafG_l1Z-SPTuLAQ-IEoXdXQhNyGjMw5Bf6W9xNOqADUtwxDCwQYKpoEbhskjiLCJMtmcK2fzf5ZzwObA5914y70Qh4bhDIVvt9kKYm9EqzEUUE_MjqJ7Kj4UaPUuW9LgUzLEINN0yLIB7pGAUs4dEBQn2MTkuBglkFSeiXFyVzTWhOYWSTTJpAly1NjUFlfeNdlC4rrdqML0HxDH4vDw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
هشتگ ۱۶۸# تیم ملی ایران در جام جهانی خبرساز شد
@Farsna -
Link</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/farsna/441156" target="_blank">📅 15:53 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441155">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tnHUfDAzprHVgeDYAksd91517bi4YN6rCLrmbQiSuQfEze7qcHz6kzyI5AzjchOVIy7dNlX4JAiglMtPt548ScM_XNgvOMO3z8A1RYszjukQnBEC1NoXABWhwhbxFBLTgw03_Ta9sSKHY0bOexyIwEldUxRydQBJxXsBu2JIRnWFFJNji3xD942J_nZHPAggfvyWSFbgQhjg-VTVbsBwxjKK2E69JkYsxiYFctUiqmLRpbbKM9jS19DrVg3EUucaQXdT-m7QBVfe-oteMQl472cpaqEtyeQWpgWE66ZGCJw6cIwhuazBS-BvjLfVwSXwkCjm4kLP4pRAut_4yoZE-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پزشکیان: مدیری که تصور کند برای حل مسائل تنها یک راه‌حل وجود دارد، در واقع شکست را پذیرفته است
🔹
بنده شکست را نخواهم پذیرفت و معتقدیم برای عبور از چالش‌های کشور راه‌های متعدد و ظرفیت‌های فراوانی وجود دارد و دانشگاهیان و نخبگان می‌توانند در شناسایی و به‌کارگیری…</div>
<div class="tg-footer">👁️ 9.55K · <a href="https://t.me/farsna/441155" target="_blank">📅 15:51 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441147">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ue5u8V0MGjqacDmZ-ZqrLmb6J-HBNFgg5oUgOG951PZuqab1-1JodnOgcs5M71lw0sSZwfLEF5c_9b2KUyDHy0nJIl0CjIu7uU3KE8yRWvzDbNe4ZB_nJ0ovMS9l26-QNyHit46WEaz18pSZRky9tmfusb5DHE8N_QxF5ZrsGZvo2SeiwGg2Br-_UlumIu2vUCFjFe1ehawZANmCRZpSgEWtgzhfMyzqWRIb_n6mCTzMawSsAfhjzjhA90PABXph1BCcG8fswlNawwi-FvgSHXjS3eRbE3vhA8bCzRua--JYgtxRBjAFAr85JBpFEC7xRnQZkW4cCjV6_KFZAbtmvg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پزشکیان: مدیری که تصور کند برای حل مسائل تنها یک راه‌حل وجود دارد، در واقع شکست را پذیرفته است
🔹
بنده شکست را نخواهم پذیرفت و معتقدیم برای عبور از چالش‌های کشور راه‌های متعدد و ظرفیت‌های فراوانی وجود دارد و دانشگاهیان و نخبگان می‌توانند در شناسایی و به‌کارگیری این راهکارها نقش مؤثری ایفا کنند.
@Farsna</div>
<div class="tg-footer">👁️ 9.96K · <a href="https://t.me/farsna/441147" target="_blank">📅 15:40 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441146">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ckbJ5KLnrq_JUSsEmk8gfhXF31eESIFE-qNISyAg46qxStMc5V-87YAgUYZg740Jvt56SuhIbUQFTCOPQS053be_UUQxB11CU-m9dy8mSbKa3yftQ2bWSr3zLLGt2Y4CmggNNMAJva1OaqJyx6T9B2FjiWQhTs0Dlpt0C42KGHw1nMSiogENLqM1-Nb3jzYM0HUUedJj31pd_PPZteobE86_1jH-DD-Dv96dWnEeMMCnPSB0iDuHYxvg4ursRx-OHdex8pApBfMFOPnW7DMVSVrJ3A9D8FN4s5j9nEwCCPZhxFNAMlri_uMphDWkteVgRhV75PLertebqnXcKWWueA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اعلام محدودیت‌های ترافیکی جاده‌های شمال
پنجشنبه ۲۱ خرداد:
🔹
کامیون‌ها و کامیونت‌ها (به‌جز حاملان مواد سوختی و فاسدشدنی) از ساعت ۸ تا ۲۴ در محور هراز ممنوع‌التردد هستند.
🔹
در صورت سنگینی ترافیک، محدودیت یک‌طرفه مقطعی در محور کندوان با صلاحدید پلیس راه اعمال خواهد شد.
روز جمعه ۲۲ خرداد:
🔸
از ساعت ۱۴ ورود خودروها از آزادراه تهران–شمال به سمت چالوس ممنوع می‌شود.
🔸
از ساعت ۱۵ مسیر پل زنگوله به سمت چالوس مسدود خواهد شد.
🔸
از ساعت ۱۶ مسیر مرزن‌آباد به سمت تهران یک‌طرفه می‌شود.
🔸
این محدودیت‌ها تا ساعت ۲۴ ادامه دارد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.92K · <a href="https://t.me/farsna/441146" target="_blank">📅 15:36 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441145">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/f0rI-ZU4lFXh-XpZ1O-AEN_kX4N03tqRoLnJAMH163-8YasXhw3dBAhsV8boeIWIjBodtq59WAnn7Yij1oWydc8NMbjpZp0QPkvNlbYuYA3cycGFp2k5i3O4KFteikrGLe4BNbOkeMBDJhrMTePHOhsNrl4hhkvxVxHgsOx-WhtweShHjfaTszE9dCfGONYb8ATaN3f4hkCvgsX1GkQf70Bw_MxiGL4U664cjdqFBmTcdMu5rXX8yFNydgo4b5JWXzz3wZI6SgFDwH9zPzZX9fD2MQtkzCPs_uAOXGjld4eYnkLR3cdINFks9zRWVOuJ_S30sNQXg1ZH9TyXQy3mmg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تلگرام رفع فیلتر می‌شود؟
🔹
درحالی‌که برخی رسانه‌ها از احتمال رفع فیلتر تلگرام خبر دادند، براساس اطلاعاتی که به فارس رسیده دیروز کمیتهٔ بازگشایی پلتفرم‌های فیلترشده جلسه‌ای برگزار نکرده‌اند و هیچ مصوبهٔ جدیدی در خصوص رفع فیلتر تلگرام تصویب نشده است.
🔸
هرگونه…</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/farsna/441145" target="_blank">📅 15:23 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441144">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Bf0RaT4UJYkD_pojqWJ4l0qA1g5zitymFMUbDwTTRXWya2XIW9RYxS3mmQD14zBgf_uMIvcXQ4jIGiDJNpeAO2f6d7t8RroSWGx5UEtT8MvCX7xm1NluTgSeXcSV7xTcBDfVE5cNUJxG6XMeatftL4aXXEUJku4ww2OaYVqgtfcqPncH8_5U2xKKeio0EnZHl0oDqD-eDHuYWuff1Q5KceKTRlfDB_Kejp4TIKYNG2Y-0c0s0CL233P3m4eiWKtVv33qTbGyfIPSFN4R2Tlb4ktiI6N99Zgh_d8FmDnnvv4DmzTuAgq91t-tMWWsN8kla9COzEZn9GivrS5mA-b26A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کشف ۱۶۳ هزار لیتر گازوئیل قاچاق در سواحل میناب
🔹
فرماندۀ پایگاه دریابانی میناب: ۳ مشک ماری حاوی ۱۶۳ هزار لیتر گازوئیل قاچاق در سواحل این شهرستان کشف شد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.88K · <a href="https://t.me/farsna/441144" target="_blank">📅 15:16 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441143">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Jm2Mtq9MuswkWx3rrNTE7SYR69YxYBdNq0PTg8zlCaOVlZ1tTyHQqpzdkFRX4jGfIWJWzEwb9qlK26jzjflpCrAOtyhxGI3Ky-N3wgfmjKTu-YplXPmEVw3gVxawrCLHsLo_Mx8kAA3Nr6mVnXGMiDAN7SpTwn_QszrydsAFgw38hnPPr-IrkXVSYIbW8MR3cB8gBgIFoAfjc0yU6vnX98YzXEfjo669jfc9_T3wynD482YV3qlXDc4sgMv4jpPinTJohCf8B3EzzTS3tAAz_RQs0roNwUvmyv6qaxN3RLFaqHq0mfmP37yF3ZaWJHp7SQcjEujZigUIrKscQpN4eA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">لیکود نامزدی نتانیاهو برای انتخابات آینده را اعلام کرد
🔹
حزب لیکود رژیم صهیونیستی اعلام کرد که نتانیاهو ریاست این حزب را برعهده خواهد داشت و در انتخابات پارلمانی آیندۀ رژیم نامزد خواهد شد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/farsna/441143" target="_blank">📅 15:13 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441142">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6ff7d0417a.mp4?token=SmEjXH6r2Mh-PJBp9TY7RWNCA7neYZJfPq0Oi-FbeZ1wCAZQcswxsakNEv-n5mI1J8m-XN23PqHzWptk-tdtTtvhMmBBTRBSj6MYmAdQIpzBkU7-HaGdUVfFcXsW-16t8AsNX3v5aQA8R0MpZnQEfzMlF03uIv1iBsG1hR5L5FxuCViiaiTL69nOOfnhBjc9eu3HAEB7OjaELQ2EI_Rty-iArHkt9S43s-Q9UqyzWbFj-9ygYaRwcIaprpF1zXmcEtbLIjuLJRB8lHxtREyGVwj89mGuqyed5bd1Xds5xVjv5-GXIq5ME0yJ-ClawmeMhYpPweL10DkkUX4ZK3Jmwg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6ff7d0417a.mp4?token=SmEjXH6r2Mh-PJBp9TY7RWNCA7neYZJfPq0Oi-FbeZ1wCAZQcswxsakNEv-n5mI1J8m-XN23PqHzWptk-tdtTtvhMmBBTRBSj6MYmAdQIpzBkU7-HaGdUVfFcXsW-16t8AsNX3v5aQA8R0MpZnQEfzMlF03uIv1iBsG1hR5L5FxuCViiaiTL69nOOfnhBjc9eu3HAEB7OjaELQ2EI_Rty-iArHkt9S43s-Q9UqyzWbFj-9ygYaRwcIaprpF1zXmcEtbLIjuLJRB8lHxtREyGVwj89mGuqyed5bd1Xds5xVjv5-GXIq5ME0yJ-ClawmeMhYpPweL10DkkUX4ZK3Jmwg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
آتش‌بازی ضدچینی تایوان با موشک‌های آمریکایی
🔹
تایوان برای اولین‌بار با سامانه‌های موشکی توپخانه‌ای هایمارس ساخت آمریکا شلیک واقعی انجام داد و حملات دقیق فرامنطقه‌ای را شبیه‌سازی کرد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/farsna/441142" target="_blank">📅 15:07 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441141">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">رویترز: هیئتی قطری امروز راهی تهران شد
🔹
خبرگزاری رویترز به‌نقل از منابع آگاه مدعی شده که هیئت مذاکره‌کنندهٔ قطری صبح امروز پس‌از رایزنی با آمریکا، راهی تهران شده است.
@Farsna</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/farsna/441141" target="_blank">📅 14:58 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441140">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c2c73674cb.mp4?token=TbZGMiKUS936SpRpydlVzjv4_FUhqS_7P-qIJGCMfUTP2yzx_ONZY-RrIJ9AL6nmUwwPiOseWv5sAIXu0SIbUvU9t3B1q8amtUzvd5Z7L6KRH_xMcCqpWSJreD71M2M2OeMEFLj4lwt7POrvTmy0Zo3Ms2Pm1rG645cMi2iaDun8TQfqbTejjg2VjFIHHALCJezK3QWFtxWM_HV1ZHTnu0Qd5ejqfHHQM8l_M7kkK5BU5eu2idMyCx_Jqf9xE9qIP9ECkYNbcc6OpmYF0mtrEa3CyGUx2foTYwtEQ3HKC6FsdRQbMqlEySP68iPrlFzbkvuWTwgMGkzBKRbl7SM1OQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c2c73674cb.mp4?token=TbZGMiKUS936SpRpydlVzjv4_FUhqS_7P-qIJGCMfUTP2yzx_ONZY-RrIJ9AL6nmUwwPiOseWv5sAIXu0SIbUvU9t3B1q8amtUzvd5Z7L6KRH_xMcCqpWSJreD71M2M2OeMEFLj4lwt7POrvTmy0Zo3Ms2Pm1rG645cMi2iaDun8TQfqbTejjg2VjFIHHALCJezK3QWFtxWM_HV1ZHTnu0Qd5ejqfHHQM8l_M7kkK5BU5eu2idMyCx_Jqf9xE9qIP9ECkYNbcc6OpmYF0mtrEa3CyGUx2foTYwtEQ3HKC6FsdRQbMqlEySP68iPrlFzbkvuWTwgMGkzBKRbl7SM1OQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
پالایشگاه بزرگ روسیه هدف قرار گرفت
🔹
پالایشگاه نفت در استان سامارا پس از حملۀ پهپادی اوکراین دچار آتش‌سوزی شد. این پالایشگاه یکی از بزرگترین تأسیسات صنعت نفت در منطقه و بخشی از شرکت دولتی روس‌نفت است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/farsna/441140" target="_blank">📅 14:53 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441139">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ba9232e26f.mp4?token=EtrMEmtESnQN2b8u1WcBLMYU4DUZIdxdrYvP2QA2EM0YWBKplyhGe4HhqoU5Kvq53owOodnI7Cvp3_3iE-XociV1BiTe2elbUZAuGZOGlbXv9ORmc4KtM-jJbuarvGIOXaQTgDC0fU3YF6JjGyUAlnWLYKbRGORF7wMMTijEP5mkZVSvlhwLmLKAPJ-OWsXLysnBBqCWf39LI4Y-fKzgeS5UyC7JGIdUO6C8lBulR6q4ddXCdTik8PAd1n_Er0TaHo3mc9YMCuf5_P3a-14O9jp1tq3ccvWf_iY7E26RMFM0anmvBF20f8-ocu4XHfQ2z3y1lUVzMa8l_wWrjglnww" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ba9232e26f.mp4?token=EtrMEmtESnQN2b8u1WcBLMYU4DUZIdxdrYvP2QA2EM0YWBKplyhGe4HhqoU5Kvq53owOodnI7Cvp3_3iE-XociV1BiTe2elbUZAuGZOGlbXv9ORmc4KtM-jJbuarvGIOXaQTgDC0fU3YF6JjGyUAlnWLYKbRGORF7wMMTijEP5mkZVSvlhwLmLKAPJ-OWsXLysnBBqCWf39LI4Y-fKzgeS5UyC7JGIdUO6C8lBulR6q4ddXCdTik8PAd1n_Er0TaHo3mc9YMCuf5_P3a-14O9jp1tq3ccvWf_iY7E26RMFM0anmvBF20f8-ocu4XHfQ2z3y1lUVzMa8l_wWrjglnww" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‌ آب شرب کوهستک و ۱۰ روستای اطراف تا فردا وصل می‌شود
🔹
مدیرعامل آبفای هرمزگان: عملیات اجرای خطوط لولهٔ جدید برای تأمین آب درحال انجام است و پیش‌بینی می‌شود آب شرب مردم شهر کوهستک و ۱۰ روستای اطراف تا فردا وصل شود.
🔸
بامداد امروز درپی حملهٔ دشمن آمریکایی به…</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/farsna/441139" target="_blank">📅 14:51 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441138">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/p-NPbq5Uib4k3OOOj_IF-1R7ePjNkfiNai57oO6UebgJ4Js2f0FXJsgjk8UcxLjqOmM9XvJhA1qlRBdcYNhWPebCcQjk-4ZSDs0gNlkmTmhTLH7MH5KQyJTh2JAkKDclBh5_vR7gpEWnjdqEkwc2_RvAnT2CHk1ALWpMsbs5bbY-CTsRTQU7TVeGQsk90HhrgHJkTbVuYqFjWDU-0l7l-eqC5u8QxSZTi25cfwHd9AHA2g0K1eF-Rextri7T53r-bYshyHDzFSn8yXs4mEdGSPiuYTiMVQgURto8RoNser6l1OVmau7SrhvI-h53ue9eznD_vx32i5oxiEhMG4owbw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اردوغان: حملات اسرائیل به سوریه و لبنان تهدیدی برای ترکیه است
.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/farsna/441138" target="_blank">📅 14:48 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441137">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RwfeMFgBGtJf5l_x1C5ZdOgHUG2FfmDcq-Y3Fq35gQvaqaltqwhroQKcbQMWNQ8YS_zYDirL-BcSfDJpokOZqxMh5JKMv_wVwrU42VAXU9YC_v558f3c2anuEN6d9ILAMDrFzggFrkyEJGh-ThdLc4lA2zMXLfFjrEM76FTCgpV6T8beuGZpjaoMqbIVneuWBBiV_e_Z0jabXfLy-AqZwIL-R8hp6GPvDdzso5isjc1-_oz8No61pxbBpzqNy24a0NB98fXIA08Qd-4jc48-9LWuV9eQ5ftYaUDEnavUsRRFbvxEUhPqjD0AU4ecrg7ea12-39eDlCLgZa15LOD8ZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تحولی مهم در منطقه آزاد ارس
جایگاه گمرک نوردوز به اداره‌کل ارتقا پیدا کرد
در پی پیگیری‌های مستمر استاندار آذربایجان شرقی، نماینده مردم مرند و جلفا در مجلس شورای اسلامی و مدیرعامل سازمان منطقه آزاد ارس، جایگاه گمرک نوردوز به عنوان تنها مرز زمینی ایران با ارمنستان، به سطح «اداره‌کل» ارتقا یافت.
مرز نوردوز که در محدوده منطقه آزاد ارس قرار دارد، یکی از مهم‌ترین گذرگاه‌های تجاری کشور در مسیر ارتباطی ایران با حوزه قفقاز و اوراسیا محسوب می‌شود و ارتقای جایگاه گمرک آن می‌تواند نقش مهمی در تسهیل تجارت، افزایش ظرفیت ترانزیت و توسعه مبادلات اقتصادی با کشورهای همسایه ایفا کند.
با ارتقای جایگاه گمرک نوردوز به اداره‌کل، اختیارات مدیریتی و عملیاتی این گمرک افزایش یافته و بسیاری از فرآیندهای اداری و تصمیم‌گیری که پیش از این نیازمند ارجاع به سطوح بالاتر بود، در همین مرز قابل انجام خواهد بود. این موضوع موجب تسریع در تشریفات گمرکی، کاهش زمان توقف کامیون‌ها و تسهیل صادرات و واردات از این مسیر خواهد شد.
ارتقای ساختاری گمرک نوردوز زمینه تقویت زیرساخت‌های گمرکی و توسعه تجهیزات و لجستیک در این مرز مهم را فراهم می‌کند.</div>
<div class="tg-footer">👁️ 9.64K · <a href="https://t.me/farsna/441137" target="_blank">📅 14:44 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441136">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YgJGYk09RY-ZDKnGvVMP77BbR_9l2TV80otdCmjkoqPIxulC51WTBEcnNsJ5ZDs09kNd7dJPfsntJ3-QKNIo2UuhlFjGWUbRUrcBO7J-Ybtuwu3G8h0K1F7S72pJywE19Q-2W-FxBwGIVJpCtb5mkc7SGR_S1iKDQgAshGcJa5T44-bQdBCd5FQj1o-3inXpDP30sLO4J7li2caUorG_aW_yK8KPtILhgBF-l2Oe62e6RLNFEsMD4FthD4RpH3W_2wSHJZaLl59ogHLKvtdaqCVcPhKvApjvCZYAgLfX9ZuHGYnz6nrptDNjOO62ri1u-oxiE02Z2FMR2sQuE5NJoQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">۵ گیگ اینترنت هدیه بدون قرعه‌کشی منتظرته!
🎁
با پیش‌بینی بازی‌های جام جهانی در اپلیکیشن «همراه من»، ۵ گیگ اینترنت رایگان هدیه بگیر؛ به همین راحتی.
اما این فقط شروع بازیه…
با ادامه پیش‌بینی مسابقه‌ها می‌تونی شانس بردن میلیاردها جایزه هیجان‌انگیز دیگه رو هم داشته باشی.
🏆
زمین بازی در «همراه من» منتظر توئه!
⚽️
👇
https://www.mci.ir/-4S0XAJB</div>
<div class="tg-footer">👁️ 9.34K · <a href="https://t.me/farsna/441136" target="_blank">📅 14:43 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441135">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-footer">👁️ 9.15K · <a href="https://t.me/farsna/441135" target="_blank">📅 14:43 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441134">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/40024382dd.mp4?token=S_COGhWFGuC8fPT1CV2zVo8O7dpPH87cSjfsABbaxG8y5cZxsh6Td8ZXlbFvgQxI-Z9cSNs7BcNJXgvHF0kYmw35uYgyoUWqx5KFrHwSlJrmSTVPSy-vsCuAcOacMLfpOTEd1cVFTNpAPGA6PceNym40QcPY1D2d0ZL0FHqEiJW_a_hCBxSmYeDT1jtfDC--lBGg2HV4VmR_XFm8phpnmaRxCYOfBAHqe9c9TCSQfVcD6FDiOk7fFaVHndKLrBHzkBs2i1ieZyED5VhlfQQnEEP7f9KXBiChpAKIfK0Ie0C7xc4iNS9f4GrUASYbMJ3T8G2Mcbh34Yszj0nO7BAoojzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/40024382dd.mp4?token=S_COGhWFGuC8fPT1CV2zVo8O7dpPH87cSjfsABbaxG8y5cZxsh6Td8ZXlbFvgQxI-Z9cSNs7BcNJXgvHF0kYmw35uYgyoUWqx5KFrHwSlJrmSTVPSy-vsCuAcOacMLfpOTEd1cVFTNpAPGA6PceNym40QcPY1D2d0ZL0FHqEiJW_a_hCBxSmYeDT1jtfDC--lBGg2HV4VmR_XFm8phpnmaRxCYOfBAHqe9c9TCSQfVcD6FDiOk7fFaVHndKLrBHzkBs2i1ieZyED5VhlfQQnEEP7f9KXBiChpAKIfK0Ie0C7xc4iNS9f4GrUASYbMJ3T8G2Mcbh34Yszj0nO7BAoojzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
تصاویر شلیک موشک‌های سوخت جامد و مایع دوربرد قدر و عماد و خیبرشکن به‌سمت اهداف آمریکایی در منطقه  @Farsna</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/farsna/441134" target="_blank">📅 14:40 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441133">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">‌
🔴
قالیباف: جنگ‌های تحمیلی اول، دوم و سوم به جهان نشان داد که مسیر فتح و پیروزی از دل ایستادگی و شهادت می‌گذرد. @Farsna</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/farsna/441133" target="_blank">📅 14:37 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441131">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">‌
🔴
قالیباف: با وجود شهادت فرماندهان و دانشمندان در جنگ ۱۲ روزه، نه حرکت علم و دانش در کشور متوقف شد و نه توان دفاعی و بازدارندگی ایران کاهش یافت.
🔸
فرماندهان شهید و دانشمندان کشور با سال‌ها مجاهدت و ایستادگی، نام خود را در حافظۀ تاریخی ملت ایران ماندگار…</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/farsna/441131" target="_blank">📅 14:27 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441130">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">🔴
قالیباف: جمهوری اسلامی ایران به هرگونه تجاوز با قاطعیت و بدون درنگ پاسخ می‌دهد.  @Farsna</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/farsna/441130" target="_blank">📅 14:24 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441129">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">🔴
قالیباف: جمهوری اسلامی ایران به هرگونه تجاوز با قاطعیت و بدون درنگ پاسخ می‌دهد.
@Farsna</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/farsna/441129" target="_blank">📅 14:23 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441128">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2ad86abac7.mp4?token=vOg5B_luQMRmu3A3-auXhHOdWoNW950DXDqpq9C5zypEMCuXVOtQBdgXGV6WdZ-_x3FYRdRKx_OyyiJakyWOB1_h61DhAz0EF-ws5td5sIDRxINz5qBclfeCGEr6eYRwYfsN7bThKtgaOL41MkDGqZEoCK6BdljKDa9W76lr-ZE1t1MD8jPPqTrNyQMnDOj4vLHu1bONVpLKhbnoXtD5HxbKPyAFSzxAFxrLsrlf6midWpyRRQKP0Z6S4Awyf_inAX1duiQOLtI_KokLdHT_JgSLwmUG1rhxhGHXtl_RCLwSxKgoPw0TtN45O-enxM65y8mmNOB4fVZzQAryaKhi7g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2ad86abac7.mp4?token=vOg5B_luQMRmu3A3-auXhHOdWoNW950DXDqpq9C5zypEMCuXVOtQBdgXGV6WdZ-_x3FYRdRKx_OyyiJakyWOB1_h61DhAz0EF-ws5td5sIDRxINz5qBclfeCGEr6eYRwYfsN7bThKtgaOL41MkDGqZEoCK6BdljKDa9W76lr-ZE1t1MD8jPPqTrNyQMnDOj4vLHu1bONVpLKhbnoXtD5HxbKPyAFSzxAFxrLsrlf6midWpyRRQKP0Z6S4Awyf_inAX1duiQOLtI_KokLdHT_JgSLwmUG1rhxhGHXtl_RCLwSxKgoPw0TtN45O-enxM65y8mmNOB4fVZzQAryaKhi7g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
عضو کمیسیون امنیت ملی مجلس: بررسی‌های ایران مبنی بر همکاری اردن با متجاوزان به کشور ما، تنبیه اردن را درپی داشت
🔹
این رویه شامل کشورهای هم‌دست خواهد شد. @Farsna</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/farsna/441128" target="_blank">📅 14:23 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441127">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">🎥
خسارت دشمن آمریکایی به تاسیسات آب‌رسانی سیریک
🔹
مدیرعامل شرکت آب‌وفاضلاب هرمزگان: زيرساخت‌هاى توزيع آب‌شرب شامل ۲ مخزن بتنى به حجم ۵۰۰ و ۲۰۰۰ متر مكعب با تأسيسات مكانيكى مربوطه مربوط به شهر كوهستك و ۱۰ روستاى بخش بمانى با جمعيت ۲۰ هزار نفری در پی حملات دشمن…</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/farsna/441127" target="_blank">📅 14:18 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441126">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DoP2gfh_TRBsuLckTbJrRsN3F2Wv9afzIYGAfrnScWvDvmE7ns_WL9QgfR8YUyLdn5ctUy1qjhHkw2AXNxxomCcGJmAcAOjdmocFF6bchX8gc1D6kbsEjOMezLSpHKKtbhNA_4-YVIMWqmpnSeLhmp95Oz9vVVOaHgBt2ED-G_AjlU6yd1OylixeYSoqYhrPxvsCcYf70H5DFoSw-BrvEagOxnZFfthNDaiWgncvvWyTLxrbYWiWP6VXVZuyJKY9KVsW1oDA-sLNXWd-h__DFUPX6rSc_cuRFgHNptztmbWX59sXkFo19QNYXN6rAWL70TmkM1VUw-BuD8MIQFArJw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎥
تصاویر ماهواره‌ای از انهدام آشیانه و انبار پایگاه‌ هوایی رامات دیوید بر اثر حملات موشکی شب گذشته ایران  @Farsna</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/farsna/441126" target="_blank">📅 14:10 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441125">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1117278651.mp4?token=In4IOJTWBhQGH0vF3M0D0TD9oFyVgCr9EPhPfFgibykPhWZHsyaDecPq8vLPRVaasSV1kiQIaJD_lR0YRZxM70OofdChfu1mPeI3Om1HdHFFxGYZpOQrrNKlYrzltoCwy6tU6kY9QEXBz6b8Pz4CViPn_OtjR99KlLsCtwqL5DM9ftP5w8mZR_TsZRermPObT6j9DCDXcVXi2gohSOERXUpKRIQVI-gKQeC8IzZMyCuscklk13FizztfZznZ1i04uTUi-a9g5P-Nl1-BQMSMv0gEWI37iKCNXjrRSW0sotwL0DTCK9ry8fTY7DQrnomFUD9R57lDtwlXf6PnKbmAVw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1117278651.mp4?token=In4IOJTWBhQGH0vF3M0D0TD9oFyVgCr9EPhPfFgibykPhWZHsyaDecPq8vLPRVaasSV1kiQIaJD_lR0YRZxM70OofdChfu1mPeI3Om1HdHFFxGYZpOQrrNKlYrzltoCwy6tU6kY9QEXBz6b8Pz4CViPn_OtjR99KlLsCtwqL5DM9ftP5w8mZR_TsZRermPObT6j9DCDXcVXi2gohSOERXUpKRIQVI-gKQeC8IzZMyCuscklk13FizztfZznZ1i04uTUi-a9g5P-Nl1-BQMSMv0gEWI37iKCNXjrRSW0sotwL0DTCK9ry8fTY7DQrnomFUD9R57lDtwlXf6PnKbmAVw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سخنگوی حزب اصلاح‌طلبِ ندای ایرانیان: ایستادگی نیروهای مسلح در ماجرای لبنان هوشمندانه بود.  @Farsna</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/farsna/441125" target="_blank">📅 14:05 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441124">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">️انهدام یک پهپاد متخاصم در آسمان خوزستان
🔹
یک فروند پهپاد متخاصم توسط شبکهٔ یکپارچهٔ پدافندی ایران صبح امروز در محدودهٔ روستای چال بلوطک شهرستان اندیکای خوزستان منهدم شد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/farsna/441124" target="_blank">📅 14:05 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441123">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e9de031baa.mp4?token=QGCwv9M_pkj6YIHiwT2ujs3r1iOZK1RIQKwkMrgyn5VTmy6rRtEXHCidZgA3E-yjTgemcGrBr6As0N67eWyShQXeOJIWwZQGD_07SOS8sY-xAIb8QT-fiLUOeu6CKf0oMUH9ynA6Tv32hgIX4OedV8zyBgevArNTyN7eafsAAZ1hbOiUwvg_4gETktg9iLG9SeBqYYx9SNa1bkMDtNzsy3c3TzKMnrAKT3tE7Gu-lS448r2RyW-H2CROSJjFoIU9sFsuwIWdoKd2zG39xkrM1f147F3e_GwOtSJJ1VCC7mbkbhF1Nr94skRd03eWqQMULfmCSp1fCfcT9Mifr5QrxA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e9de031baa.mp4?token=QGCwv9M_pkj6YIHiwT2ujs3r1iOZK1RIQKwkMrgyn5VTmy6rRtEXHCidZgA3E-yjTgemcGrBr6As0N67eWyShQXeOJIWwZQGD_07SOS8sY-xAIb8QT-fiLUOeu6CKf0oMUH9ynA6Tv32hgIX4OedV8zyBgevArNTyN7eafsAAZ1hbOiUwvg_4gETktg9iLG9SeBqYYx9SNa1bkMDtNzsy3c3TzKMnrAKT3tE7Gu-lS448r2RyW-H2CROSJjFoIU9sFsuwIWdoKd2zG39xkrM1f147F3e_GwOtSJJ1VCC7mbkbhF1Nr94skRd03eWqQMULfmCSp1fCfcT9Mifr5QrxA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
پزشکیان: هدایت‌های رهبر انقلاب پشتوانۀ اصلی مدیریت بحران‌های کشور است
🔹
دشمن که از مواجهۀ نظامی با ایران ناامید شده، تمام برنامه‌ریزی خود را بر ایجاد تفرقه و دامن زدن به اختلافات داخلی متمرکز کرده است.  @Farsna</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/farsna/441123" target="_blank">📅 13:39 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441122">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c6361ab1ac.mp4?token=K2l2cY62DsjW6iApYN8RYLwTtSHCQOPXzkUjbYhRvBqa7hnEVnbRqimEgjtstXeV07jScyPhtD6SqjFYToc8te9GlLRIkEgWHaG8Rq7uhDeOq5HU0YY7pVqFll-H43_JQ83nx1O_aageyiSTDUAg43OY0uOzifqvmTnl4dxYmNDe7_qTLDh3goUC9UsaAbRlVuEalklwPLWnPr_raZFqgyVSfBCp4AK4xkW5s9IkHCQt8AHPZH062BwfcTSN3HiCdWITh-rz0cnf52DDXeze2Ugdq2_kLiwGmL4bpi2OpxTxKCcpLbDyzjLF2bY2KvTjB84S1BBBzjJ4gWXW9qfusw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c6361ab1ac.mp4?token=K2l2cY62DsjW6iApYN8RYLwTtSHCQOPXzkUjbYhRvBqa7hnEVnbRqimEgjtstXeV07jScyPhtD6SqjFYToc8te9GlLRIkEgWHaG8Rq7uhDeOq5HU0YY7pVqFll-H43_JQ83nx1O_aageyiSTDUAg43OY0uOzifqvmTnl4dxYmNDe7_qTLDh3goUC9UsaAbRlVuEalklwPLWnPr_raZFqgyVSfBCp4AK4xkW5s9IkHCQt8AHPZH062BwfcTSN3HiCdWITh-rz0cnf52DDXeze2Ugdq2_kLiwGmL4bpi2OpxTxKCcpLbDyzjLF2bY2KvTjB84S1BBBzjJ4gWXW9qfusw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
عضو کمیسیون امنیت ملی مجلس: بررسی‌های ایران مبنی بر همکاری اردن با متجاوزان به کشور ما، تنبیه اردن را درپی داشت
🔹
این رویه شامل کشورهای هم‌دست خواهد شد.
@Farsna</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/farsna/441122" target="_blank">📅 13:36 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441121">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a594dfda42.mp4?token=oRrBJaIrz3DgbtM661TJgtGV2Rixp4gc3o8qhwufFYAzQJGATbQthKO4z7s0WUpYsgTy3XNwcHNyTnLcZcJBtm3LcvjrqcYwAEDqZUdDU9JIf_GLMObrhILzTjJN8fs9Ng1gKd1eIvMzibSluv70P19QBr1qoeYZev05nQkwqk4Ihj9Gi-Smq6W7uAg3e97wF1FbTK0-26lXFJy9AuXKsfnT9ObWPhzVpsg6v9IcT-IcRh7t1AzG9mxjOiaKzBV_svtKlvxpf47pNX1eAhPA9c_VWkZ2yTj3adQ2-AkjpTfwRnI0NUeuhc3XNU6bUfgQkkx4zU_aJVIyiXBtNfUiVA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a594dfda42.mp4?token=oRrBJaIrz3DgbtM661TJgtGV2Rixp4gc3o8qhwufFYAzQJGATbQthKO4z7s0WUpYsgTy3XNwcHNyTnLcZcJBtm3LcvjrqcYwAEDqZUdDU9JIf_GLMObrhILzTjJN8fs9Ng1gKd1eIvMzibSluv70P19QBr1qoeYZev05nQkwqk4Ihj9Gi-Smq6W7uAg3e97wF1FbTK0-26lXFJy9AuXKsfnT9ObWPhzVpsg6v9IcT-IcRh7t1AzG9mxjOiaKzBV_svtKlvxpf47pNX1eAhPA9c_VWkZ2yTj3adQ2-AkjpTfwRnI0NUeuhc3XNU6bUfgQkkx4zU_aJVIyiXBtNfUiVA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
پزشکیان: امکان ندارد دشمن یک کشور را با هواپیما و بمباران وادار به تسلیم کند
🔹
غزه با آن کوچکی را ۳ سال است که نتوانسته‌اند وادار به تسلیم کنند. ایران ما را هم قادر نخواهند بود و قطعا تسلیم نخواهیم شد.  @Farsna</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/farsna/441121" target="_blank">📅 13:35 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441117">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bba0f34ba3.mp4?token=j2jUCW32xenfPfbBbNMkyd_JNDWQPt5sKhpTz27lNGmCKGXZuVxsTpRFayKPyDRe83hFh3psim-BknTDuwmvmdR6fwmH1OR_SyVKxv8OAFSBS-vl-SkyGvrePOwmocXkmbTY7mHhDSVzi68Qqybn1RB5nWwRTMSJ8XUQX3-JCuiLT2hr8UX8XTjuXK8_9vzvtLHJ7t6IzsZsG6uAPBqywIonK2ZII9GHaIDpLv6pbR_8g6Czt7iV2kkR9ZPbj8_ESFnNufTS36HTJg1VMw0T1W-4nnAYbstiAEPEwFViJHXd6HFOEnH2bN1_XEOtzFWvyuaZyEiO2d0LRF6Ox017uA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bba0f34ba3.mp4?token=j2jUCW32xenfPfbBbNMkyd_JNDWQPt5sKhpTz27lNGmCKGXZuVxsTpRFayKPyDRe83hFh3psim-BknTDuwmvmdR6fwmH1OR_SyVKxv8OAFSBS-vl-SkyGvrePOwmocXkmbTY7mHhDSVzi68Qqybn1RB5nWwRTMSJ8XUQX3-JCuiLT2hr8UX8XTjuXK8_9vzvtLHJ7t6IzsZsG6uAPBqywIonK2ZII9GHaIDpLv6pbR_8g6Czt7iV2kkR9ZPbj8_ESFnNufTS36HTJg1VMw0T1W-4nnAYbstiAEPEwFViJHXd6HFOEnH2bN1_XEOtzFWvyuaZyEiO2d0LRF6Ox017uA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
معترضان ضدمهاجرت در ایرلند شمالی خانه‌ها و خودروها را به‌آتش کشیدند
🔹
پس‌از انتشار تصاویر حملهٔ یک پناهجوی سودانی با چاقو به یک فرد دیگر، اعتراضات خشونت‌آمیز ضدمهاجرتی در مرکز ایرلند شمالی شعله‌ور شد.
🔹
صدها معترض که بسیاری از آن‌ها نقاب بر صورت داشتند، در چند نقطه از پایتخت ایرلند شمالی که بخشی از بریتانیاست، تجمع کردند و در جریان آشوب‌ها یک اتوبوس، چند خودرو و یک ساختمان به‌آتش کشیده شد و ساکنان آن مجبور به تخلیه شدند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/farsna/441117" target="_blank">📅 13:28 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441116">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0411677642.mp4?token=IuIyhbjQW3-Ii_GTZlevvodP8J9ZB9Ll0dBANByIdPMt5Rvkn0wC147g58kMKQYi9xj6NitEgZq3jFWnqrGYiHZ3ve-EOmSzqakSiJ1jnl0OrhwgJAlhW9C3ehwIUNhLMpjRSd9lpuFanr0kErUJG6q4Svv4rlaLw6hNPoAA5m0ELlhH6ikPE486yPDGd97E_o9XsS6l7wsGUwnjlYeL0QttLNQio4H9HEIC4IwZucWef5tG0r2kn9RIJBJZghcN0cjOHAKgIeqXqCnPldS9HwCaBzrHq4n-M3nPGwMbSwus7_HDrJmXX6pQ2UjUBywEbJDUe7UBMy0OcGCSsIZbbA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0411677642.mp4?token=IuIyhbjQW3-Ii_GTZlevvodP8J9ZB9Ll0dBANByIdPMt5Rvkn0wC147g58kMKQYi9xj6NitEgZq3jFWnqrGYiHZ3ve-EOmSzqakSiJ1jnl0OrhwgJAlhW9C3ehwIUNhLMpjRSd9lpuFanr0kErUJG6q4Svv4rlaLw6hNPoAA5m0ELlhH6ikPE486yPDGd97E_o9XsS6l7wsGUwnjlYeL0QttLNQio4H9HEIC4IwZucWef5tG0r2kn9RIJBJZghcN0cjOHAKgIeqXqCnPldS9HwCaBzrHq4n-M3nPGwMbSwus7_HDrJmXX6pQ2UjUBywEbJDUe7UBMy0OcGCSsIZbbA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
پزشکیان: باید از حالت نه جنگ نه صلح خارج شویم
🔹
دشمن باید خواب این را ببیند که ما در برابر تجاوز آن‌ها کوتاه بیاییم.
🔹
وضعیت نه جنگ نه صلح برای کشور خوب نیست و باید این وضعیت را از بین ببریم.  @Farsna</div>
<div class="tg-footer">👁️ 9.7K · <a href="https://t.me/farsna/441116" target="_blank">📅 13:26 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441115">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3aba412f0f.mp4?token=gQctVdp1nYTbhQCzMp5tCcx_mxC4MkmWnrngd1F2UeK3w79MWMTqrG8xlwlQxxFYFphhmZRtc9shmEETEPGytvNOqvk5wuON2XN6Cif8AgEBDb5T6uVT-Q957LwrmoyepoKHrqByYPKNXCxeUb3w98YuSju_TVvGi9N-0LQWeg2ZVa8fD3T9auTxUm5fgIPenBfcZNlZDotSts7Zkn7ljnE-CbfMc-n9pc7EmxL8oHTVEeihl02joqyPA1lkHdnAzL_dRCLIUWK6B90jL4iNyVf0DVxtIxT2WbfM1FiHTFG4tbhUX1E0KF5l7rbUSjZSI7py9zryZx49mpowXMiNsw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3aba412f0f.mp4?token=gQctVdp1nYTbhQCzMp5tCcx_mxC4MkmWnrngd1F2UeK3w79MWMTqrG8xlwlQxxFYFphhmZRtc9shmEETEPGytvNOqvk5wuON2XN6Cif8AgEBDb5T6uVT-Q957LwrmoyepoKHrqByYPKNXCxeUb3w98YuSju_TVvGi9N-0LQWeg2ZVa8fD3T9auTxUm5fgIPenBfcZNlZDotSts7Zkn7ljnE-CbfMc-n9pc7EmxL8oHTVEeihl02joqyPA1lkHdnAzL_dRCLIUWK6B90jL4iNyVf0DVxtIxT2WbfM1FiHTFG4tbhUX1E0KF5l7rbUSjZSI7py9zryZx49mpowXMiNsw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
پزشکیان: باید از حالت نه جنگ نه صلح خارج شویم
🔹
دشمن باید خواب این را ببیند که ما در برابر تجاوز آن‌ها کوتاه بیاییم.
🔹
وضعیت نه جنگ نه صلح برای کشور خوب نیست و باید این وضعیت را از بین ببریم.
@Farsna</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/farsna/441115" target="_blank">📅 13:16 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441114">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MHbOa7Ke7Py77FXiofdpMWSzlc0ZH8C_7zsCtXiWsStx-FOMfwGYf0wi3jc784I8VUsH_SXm2hYdrW9pnDS0CFOmmNLTHScHRuLDeFe3xhRmfLuaVSdN6vWXiQGYMPmpIw7TA2CotYKGBp23QF7xxsybRtWKU6-kwnBB0ntQpcoi7_I09EHcIuh-GVmW4fQSZiMuMRIK7vz4Xmz2eh6sTMEw5HcWCF2s7f2DhlV88CWSUApVnuwwIg2Q5o2rUSKgBqRQ53tlEsf7XJeVuL1sRg8yzGyappInoMI7EkNoeNDk4HKhlSkmq2adpNjQ6kiPzkQfpkO7NCocrCPyEM2dKw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
حادثهٔ دریایی در نزدیکی تنگهٔ هرمز
🔹
سازمان تجارت دریایی انگلیس: گزارشی از حادثه در ۲۰ مایلی شمال‌شرقی صحار عمان دریافت کرده‌ایم. موتورخانهٔ یک نفتکش ‌آتش گرفته و خدمه در حال تخلیه‌شدن هستند.
@Farsna</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/farsna/441114" target="_blank">📅 13:14 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441113">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس هنر</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/b7Rl2_W4uISLpe3TLHwrYkdLiOG3LWNgspcuUBfmlMQwLvT7T16Y7INp16GQZCgfT1zQ84Y5Ylpl8oMIehvCXGmw0kxlNAM7iwn6XrUAOYQBi9Zb_RS9C-BSlQELqR2x9c_YQ-n0ixM7VnbGeLjivaMWchxjqH6O73ocrZTtjM8W-ZLbKvwD-mdxXadPgF8w5Ki-EepjP6GYzz5frhByouts38HMS5RrQNMKQZut0aR8S_vGAFjr0VppBiMY5euoylvpJ_pcRHC0I9FTQnVg8HSgjs2yEpu1sFtxqihHhNKnTCtII7A8KrQXShAK9utGUNiyxLsO8ub9sXr_kiHyGg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">«از سرگذشت» محرم امسال پخش نمی‌شود
🔹
نجفی سولاری، تهیه‌کنندهٔ برنامهٔ «از سرگذشت» در گفت‌وگو با فارس گفت که فصل جدیدی از این برنامه ساخته نشده و امسال تنها گلچینی از فصل‌های پیشین از تلویزیون پخش خواهد شد.
🔸
«از سرگذشت» با اجرای علی‌اکبر قلیچ، جزو برنامه‌های مناسبتی و گفت‌وگومحور است که محرم پارسال فصل سوم آن از شبکهٔ نسیم پخش شد و با سوژه‌هایی متنوع مثل شهدای جنگ تحمیلی ۱۲ روزه، توانست نظر مخاطبان تلویزیون را به خود جلب کند.
@Farsnart
-
Link</div>
<div class="tg-footer">👁️ 9.87K · <a href="https://t.me/farsna/441113" target="_blank">📅 13:07 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441112">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">🔴
منابع عراقی از آتش‌سوزی گسترده در مرکز اربیل و شنیده‌شدن صدای انفجار در نزدیکی پایگاه آمریکا در اربیل خبر دادند.
@Farsna</div>
<div class="tg-footer">👁️ 9.84K · <a href="https://t.me/farsna/441112" target="_blank">📅 13:05 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441111">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/95e6704a05.mp4?token=uWJ_OpN5m2l81FJuvuOrZYknrdxih32M6x-BblbV0s7H8eA3cE_d9Myswqj2Z6nC0Z7Ft4o-zvLbv_ZklsWhZyRI74paE42D7S_cCLJy38BL0ZMk3_zlcc3e_nYRSsOMf0bVq0Px5DVDqkTTYw0bKsFbGYi8zT3ePQTnvjLH5s-Qhpw4hkj8xvetDJ-dL8d-6iGuG39iyXIZ1mNHr9U0UErMo5BdJRQqSGeIIEQH3xHRvz6yi6bkL-nxXngBiZSZZVK-fYbQzoYrbopiqcblOiGWzBAnf3EywiilViGOocilyHMQvLvhTY_YPryBPjwSZ1p1qow5WVGyyG2h163o0g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/95e6704a05.mp4?token=uWJ_OpN5m2l81FJuvuOrZYknrdxih32M6x-BblbV0s7H8eA3cE_d9Myswqj2Z6nC0Z7Ft4o-zvLbv_ZklsWhZyRI74paE42D7S_cCLJy38BL0ZMk3_zlcc3e_nYRSsOMf0bVq0Px5DVDqkTTYw0bKsFbGYi8zT3ePQTnvjLH5s-Qhpw4hkj8xvetDJ-dL8d-6iGuG39iyXIZ1mNHr9U0UErMo5BdJRQqSGeIIEQH3xHRvz6yi6bkL-nxXngBiZSZZVK-fYbQzoYrbopiqcblOiGWzBAnf3EywiilViGOocilyHMQvLvhTY_YPryBPjwSZ1p1qow5WVGyyG2h163o0g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
عبدالکریمی: جریان روشن‌فکری همواره در پی تعمیق شکاف حاکمیت و ملت بوده
🔹
عضو هیئت علمی دانشگاه: روشن‌فکران ما امروز از غرب‌زدگی به غرب‌پرستی رسیده‌اند. این جریان در یکی از مبتذل‌ترین دوران تاریخی خود قرار دارد.
@Farsna</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/farsna/441111" target="_blank">📅 13:03 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441110">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromShahr Bank | بانک شهر(N@vid)</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MxS0dIV57f1KraP76tXI1fWlvzUT_sbPgbWVqVg7fWdfXDTYHrsWvk7fZmgEu_OjJkCgRABJx6ASyrmyMyIyLtrnp3lAh8dfZKjtNIq06-YEV8GKzO_unP6sb23P8JHCzrlExPQv4T01SbvlZDng0DCNKIszd1vRLhMicOgeFZUUQac9pXoaZgT_UT0ZBcmXuASUrc-s_3tW4oo47utOOa7pT7JGbzWjdgfV_i12A_3W0O37oaa5pts0ySx8rlzRMGZNjmxPVWkgR-iUp-lHutqMUfH0_vXye0eU9NP5jZ-GVAGyfJZYSE2hVNgzrGKWPFxcJM3wVdF9p2UUpHe4gA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
رِد بانک؛ با ارائه مجموعه‌ای جامع از سرویس‌های بانکی، سرمایه‌گذاری و هواداری فوتبال، تجربه‌ای متفاوت و یکپارچه را برای کاربران سراسر کشور فراهم آورده است.
🟢
در قالب طرح «رِدبانکی شو»، کاربران جدید پس از دانلود اپلیکیشن(دریافت از آدرس:
https://red-bank.ir/download
) انجام احراز هویت و افتتاح حساب، مبلغ ۱۰۰ هزار تومان هدیه افتتاح حساب دریافت می‌کنند.
🟡
همچنین هر کاربر می‌تواند با دعوت از دوستان خود از طریق لینک اختصاصی، به ازای هر افتتاح حساب موفق، ۱۰۰ هزار تومان پاداش دریافت کند.
مشروح خبر را
اینجا
بخوانید.</div>
<div class="tg-footer">👁️ 7.69K · <a href="https://t.me/farsna/441110" target="_blank">📅 12:59 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441107">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromگروه مالی فیروزه | Firouzeh</strong></div>
<div class="tg-text">💎
شمارش معکوس IPO فیروزه آغاز شد
شمارش معکوس برای عرضه اولیه
#وفیروزه
آغاز شد! در این ویدئو با رامین ربیعی، مدیرعامل گروه مالی فیروزه درباره چشم‌انداز این عرضه و شرایطی که فیروزه در آن عرضه اولیه می‌شود، گفت‌وگو کردیم.
00:40 - دو دهه اخیر فیروزه درخشان و سخت بود!
01:11 - تاب‌آوری و استقامت فیروزه ادامه‌دار است...
01:50 - ارزش‌گذاری فیروزه چگونه بود؟
02:17 - دارایی‌های ارزشمند هلدینگ فیروزه
04:00 - داشته‌های پنهان و ارزشمند گروه مالی فیروزه
03:58 - رکورد مشارکت در وفیروزه شکسته خواهد شد؟
🛒
شرکت در عرضه اولیه
«وفیروزه»
در تمام کارگزاری‌ها با ثبت سفارش خرید از طریق سامانه معاملات برخط امکان‌پذیر است.
💎
گروه مالی فیروزه
سرمایه‌گذاری، برای همه مردم ایران
🔜
+982179672000
💎
@firouzeh</div>
<div class="tg-footer">👁️ 7.81K · <a href="https://t.me/farsna/441107" target="_blank">📅 12:52 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441106">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-footer">👁️ 9.6K · <a href="https://t.me/farsna/441106" target="_blank">📅 12:52 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441105">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Jk-TumZ2Z8W5FZ6A4mvjryIsugsU8muffV4Fa9P27sX_kgjOI45KkJ6CE4M_ftnexDJvmGfXgxPM3LlzolVBMv80gABrHnhlFH43swA8weKvef7aPSnvEgyzJLo0qHbnEOLnAUCdQIwCJ_IBhraKuF-_BengTyUUmBGNogdiXpQ3o-Xi8je99UPtBo-Uth--RHBknJGpfWa7mBh0YTM9-N9BwI8pr6XqH5rYqV9q5nPuzfTfbDr_M9m9eL-QtHILIGikB8rPujNMtdrHKxKJ8TxhQmE1oBpqhu-XeFQEzGPK1HpuEJMNxLkVP7C8icpl7elQjMowDbamLBX6hr7Srw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بورس رکورد جدید زد
🔹
شاخص کل بورس در دقایق ابتدایی معاملات امروز با رسیدن به ۴ میلیون و ۶۰۲ هزار واحد رکورد تاریخی جدیدی را ثبت کرد. @Farsna</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/farsna/441105" target="_blank">📅 12:34 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441104">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/85f13cb69a.mp4?token=lozXPAIZzeNpVm40Io9uMm1GftcR2RqhlMEGEJ5sEDL1rdBy65w_R4LPVqEoblXnMouIvwU39IsCnCM7uQY_i-9jo5Eh7AKw_JxUz9jUZ2FDTdH7XXyhSW_2MXDEMSqNgucKAug2HIPUCIcz0kvFtHODZhvpTlsXwGPcTT-hLuEzelVGoV3-dcHrF7tgzjd73fU7nhLfmwGPst_qbnycm_EvZoHkNcjLjmSQ-iVg_cUL2FTffI5j7nwzLKkA9AyFlcRAsFqT9yYVcUpdGoie_bCk5IGCNE7Xvy2S2o3zRBnr8lYtFGEk25uxrDbEXWno3OgBHoaUBY3ZUK9tFS-wwQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/85f13cb69a.mp4?token=lozXPAIZzeNpVm40Io9uMm1GftcR2RqhlMEGEJ5sEDL1rdBy65w_R4LPVqEoblXnMouIvwU39IsCnCM7uQY_i-9jo5Eh7AKw_JxUz9jUZ2FDTdH7XXyhSW_2MXDEMSqNgucKAug2HIPUCIcz0kvFtHODZhvpTlsXwGPcTT-hLuEzelVGoV3-dcHrF7tgzjd73fU7nhLfmwGPst_qbnycm_EvZoHkNcjLjmSQ-iVg_cUL2FTffI5j7nwzLKkA9AyFlcRAsFqT9yYVcUpdGoie_bCk5IGCNE7Xvy2S2o3zRBnr8lYtFGEk25uxrDbEXWno3OgBHoaUBY3ZUK9tFS-wwQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
شعرخوانی سید حمیدرضا برقعی در جشن مباهلهٔ آستان مقدس مسجد جمکران
@Farsna</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/farsna/441104" target="_blank">📅 12:10 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441103">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">🔴
انتصاب اعضای جدید هیئت‌مدیرۀ مرکز خدمات حوزه‌های علمیه با حکم رهبر انقلاب
🔹
حضرت آیت‌الله سیّدمجتبی خامنه‌ای، طی حکمی اعضای جدید هیئت مدیرۀ مرکز خدمات حوزه‌های علمیه را برای مدت پنج سال منصوب کردند.
🔹
بر این اساس، حجج اسلام حسین رحیمیان، محمد جعفری گیلانی، محی‌الدین مکارم شیرازی، قدمعلی اسحاقیان، محمدمهدی حقانی و محمدحسین احسانی، به‌همراه نماینده مرکز مدیریت حوزه علمیه قم، نماینده حوزه علمیه خراسان و رئیس جامعة المصطفی العالمیه، به‌عنوان اعضای جدید هیئت مدیره مرکز خدمات حوزه‌های علمیه منصوب شدند.
🔹
جلسه تودیع و معارفه اعضای جدید هیئت مدیره مرکز خدمات حوزه‌های علمیه در روزهای ابتدایی خردادماه جاری با حضور حجت‌الاسلام والمسلمین محمدیان معاون ارتباطات حوزوی دفتر مقام معظم رهبری، دکتر ایروانی معاون نظارت و حسابرسی دفتر مقام معظم رهبری، اعضای سابق و اعضای جدید هیئت مدیره مرکز خدمات حوزه علمیه برگزار شد.
🔹
در این جلسه ضمن تشکر از اعضای سابق و رئیس مرکز، براساس نتیجه رأی‌گیری از اعضای جدید، حجت‌الاسلام والمسلمین حسین رحیمیان مجدداً به عنوان رئیس هیئت مدیره مرکز خدمات حوزه‌های علمیه انتخاب شد.
@Farsna</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/farsna/441103" target="_blank">📅 11:58 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441102">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SLsILYsPxtvQ9LNHO4LnM13oBdiKUosP_3Ei0EAy4Ee9WPbW88uKFa4hF60x96ZrHukg50cQWl-dSfn2-bZ-BVHaVJ9tV2U_HhAtKHG5i96iOUMyEaw6c8z-4ElyM_0gUnKdMwtHLYKjbAjVeP4bpgcF7KMDY8Nzom7DXZ-EUxjU68hQNSDav-jOXpLcP5FX6QtKbPI_MdBNfyu6F1kA2utYDy0T44kof6857mXDzd54XWRA-wsFxWqKu-yGupB6uar9tIC82n6UXHwfK7Yk_qrPAE91dwMij9AM6duemOVJNU0pUb1r3NAuhv7eStMR8EOY5W32nvjHIt2lS7KRug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عراق در سوگ آیت‌الله فیاض ۳ روز عزای عمومی اعلام کرد
🔹
در پی درگذشت مرجع تشیع آیت‌الله شیخ محمد اسحاق فیاض در عراق، دولت این کشور، سه روز عزای عمومی اعلام کرد.
🔹
در پی این ضایعه، «نزار آمیدی» رئیس‌جمهور و علی الزیدی نخست‌وزیر عراق  با صدور پیامهایی جداگانه،…</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/farsna/441102" target="_blank">📅 11:53 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441101">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iYnJY8OSGoPKDy8d-eW1408mlI6Ux37fFFVB_WBXNfJ2-6NKuxRmuUgTlUG8dojt6xeXLITnj5M5S30W-7C085otlGDHJdW2W7ASIPyoOLVGr36_eDNHiCBL3kys3mPxcDDZt4822l1vHh6SgXUWbcURTBEcoscbBQnetVuHNJDcVfjVxgCyFbyMF0elO3UARAMtSMsb9yAA9sbK16S4EnosqM8ixbOPYbwMcuhbSjXayrch_aIPKJ_cBbRRk4U9Zo9BogKESbNe7wrRHdT1eZRJ_T3n3OmUo0lClwsAmYWJzwB8cZF_gl4DzhPSVNS-g1n4LvJx-Sdm_B9RoYH7jg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">واگذاری فجر جم و پارسیان متوقف شد
🔹
هیئت وزیران با واگذاری پالایشگاه‌های فجر جم و پارسیان مخالفت کرد؛ دو مجموعه‌ای که در مجموع بیش از ۲۰۰ میلیون مترمکعب گاز در روز فرآورش می‌کنند و سهم مهمی در تأمین انرژی کشور دارند.
🔹
فجر جم حدود ۲۷ درصد و پارسیان بیش از ۱۰ درصد گاز کشور را تأمین می‌کنند؛ موضوعی که به‌دلیل اهمیت راهبردی این پالایشگاه‌ها در امنیت انرژی، واگذاری آن‌ها را متوقف کرد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/farsna/441101" target="_blank">📅 11:47 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441100">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1a85b1410e.mp4?token=DDvuCEa8vgqqFEOcEwmW5X6mPYQzg0Nou7R83Rr2zVBrVkn_xOtmSxjUTR_Jyg6aopFdcy7tW9V4GibqyOYkZ8367Vj63wyJvOZKYyACa63Wm23m_kjtIcTrI7m8KPPuGCs2V1wqA4WGTGhjR0DBX1oylXOFpuqZw8r0_IqjjrjLh5VbNWVeEuyM7uiaUz7WadHqyO0ux3vAzaXztYPkx9hFoUM4FjGzPKSSUIgkQSBOagP6SfZv7Jq5Fu1j4YSxPa-RNHZS6aFf3e18fXpYCkCDLNvAq7IMs2CmaLgYz2qNEdM136r3hrPHxLxlCT7X0vUAPgiCI4I3JnNA8QXEFA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1a85b1410e.mp4?token=DDvuCEa8vgqqFEOcEwmW5X6mPYQzg0Nou7R83Rr2zVBrVkn_xOtmSxjUTR_Jyg6aopFdcy7tW9V4GibqyOYkZ8367Vj63wyJvOZKYyACa63Wm23m_kjtIcTrI7m8KPPuGCs2V1wqA4WGTGhjR0DBX1oylXOFpuqZw8r0_IqjjrjLh5VbNWVeEuyM7uiaUz7WadHqyO0ux3vAzaXztYPkx9hFoUM4FjGzPKSSUIgkQSBOagP6SfZv7Jq5Fu1j4YSxPa-RNHZS6aFf3e18fXpYCkCDLNvAq7IMs2CmaLgYz2qNEdM136r3hrPHxLxlCT7X0vUAPgiCI4I3JnNA8QXEFA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
سپاه پاسداران: یک فروند پهپاد MQ9 دشمن رهگیری و منهدم شد
🔹
در جریان درگیری‌های هوایی جاری در تنگۀ‌هرمز یک فروند پهپاد MQ9 که از آسمان شمال خلیج‌فارس قصد نزدیک شدن و مداخله در صحنۀ نبرد را داشت، در آسمان شهرستان جم استان بوشهر مورد اصابت آتش رزمندگان قهرمان…</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/farsna/441100" target="_blank">📅 11:41 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441098">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/iARFisp2zF2i6v9lJE-Y32rmR4Hig4As3kYpz6QR4dc9uDO1wAUZd1lA7epgT3klhg7UD4DRxOTVwQlYOWQ2Eao5MSp_nhIy49NEnRZRbbbMQXszBckR1FjxbjaEtdOEnjwlgaJoX4ncJSGLZ5qc3DcIAHKybcvo89HjRQg_WtFR_kEZiIq8OKRS8_01usSR5kFhKDFOuGwrKuFxSOBL-Q4Tsk5YPN_FAjiUzFOA8Cp-2P750C5Q6Pz_f9s-aPdahOnpVL4zlPloZfYDJcuAoYD2TRB4YjIGqpHN1_jaAZTGcgqKCSXJCVaoHLo6W_rgC-SNj54ZK19VVnomeZ3YzQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Ia9n264r1xSc1PsUNKY-Sas237ZMlx5S-1MtdxHoZCPQj0rC37NG3pyyJWPkpHrwEHTK7bNkyJ4j2LutCjgStEuWCt4wBpm0cYGq3k9j6zYl9hssSdmaXg_T0XPQHPhhigFFYd1svtO5fro2FVaUk5R-wfgHznRrdVjZdHCYSgdz-RQ6B9QmswlNtt0D3jM22XzkAFOXM9onSbQal_NBoeQcM8mWBibYKWMWu1e6VHWAbbk1ruu4loYnrGsgyFwZAgEeqPZxwwLJ5uHMLQc2EhWK1o87k_oDlNxzHYZ5f60R7jFIBAos6farQWVp_GBEYIOGJ5t5_CSktHrBwc2ytA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">نمایندگان ایران در فوتبال آسیا مشخص شدند
🔹
کنفدراسیون فوتبال آسیا به‌صورت رسمی جدول تیم‌های صعودکننده به لیگ نخبگان و قهرمانان فصل بعد را منتشر کرد.
🔹
نمایندگان ایران در لیگ نخبگان استقلال و تراکتور و در لیگ قهرمانان گل‌گهر سیرجان اعلام شده است.
@Farsna</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/farsna/441098" target="_blank">📅 11:36 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441096">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/SFnwUZS2lueo3KRLgslndOdZEZ6O3G45AmvgngvjPp2yijapAZCY3bsC-Pj5o4dARV0i6eM8SWJJdcnqKUeBHpINc3IH2vwr89o9Z-psCipF4TZyLjlMCOzQPGzClI7LmsTbe3RZwn8j-697294FXQgoRNIjvlEhwYbjXnWGXQFZtMoqQyCHufwfQQqhcPFGurnik_NbuU6WNnU7Wbb38yIXcU4UbwIRgZ-ggUzGLiz2ZdgYdpHMbUvvdDF3VWMpCyM9lNaVBSWs1BcF6iyuoYxUk36tUGauuTDdXVeSZJcMXUl-e1r2etUFVcDBexptpZuh-ObQTItG0PRX4VYjjA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/TwlX3YNL4My78wVVHdbbxS79PBfe_8O1_f-UIa3zbiXuPMYijhRV4AYogTADX6opIZw2Hf7rgHQE6sR_-eS1hBbYRA1NgpPapi3KLqpzB-yRP3eQLsbmUJOD6VcWlpOjUknUkCdXjCLVUBzuDqbssWygvlnVzK3JGV_cKiBANgtb__dm3rFwawpFjFN5PRB7ovh2Z8pS_6uQf9yWxPgNXoG1nr_FfBRcBiSJa6rSZSLQZzYXK0PrzenMX5utiqqV_t_UaqW29NZxMuVviaNkf3rmpdATIMOQiAXEy8XhSMXbSf7dyjyga2aUX6TE0d2ENqfBXMFhwt41o_EKtTVrTg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">هلیکوپتر آپاچی آمریکایی مایه تمسخر ترامپ شد
🔹
در پی گزارش سرنگونی یک هلیکوپتر آپاچی آمریکایی در نزدیکی تنگه هرمز، کاربران خارجی یک سوال اساسی پرسیدند و آن این که هلیکوپتر آمریکایی هزاران کیلومتر دورتر از مرزهای آمریکا چه کار می کند؟
🔹
بسیاری از کاربران با اشاره به ریتوئیت پست ترامپ درباره سرنگونی هلیکوپتر ارتش آمریکا در نزدیکی تنگه هرمز در صفحه رسمی کاخ سفید این سوال را مطرح کردند که اصلا چرا باید ارتش آمریکا در نزدیکی مرزهای ایران که هزاران کیلومتر دورتر از مرزهای ایالات متحده است،‌ حضور داشته باشد؟
🔗
اظهارات کاربران در این باره را
اینجا
بخوانید.
@FarsNewsInt</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/farsna/441096" target="_blank">📅 11:20 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441095">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a856502fd2.mp4?token=SxoTUlTs2Gs74QQAuKt3WfcIgoFb2D3_TX9JVLc9rxyG4klPC8JHUx3Uh4ulvMLThFmJITvPDTOYS-OwII_njtHtau_5-VSLuHFXjazCGGdnu6Sg0D66s8ZmNZxkLvbE-T8AG-yFikvWONYzEJF38v6WCYJTBLLlkRhPsNRzuXZhT94yP8PNx5CKrhNderIooyvTOy7c-gP0SfxZdcNr28Mlc65JY1GOhIrCpZ-puH_T_mN1sp1LY4YRj57ZkjRtjB5oqnYG3-oA3I6YcxdUOsTRfxZSzTSYglqOxwHjrdSVRQ2ZRQnTOjs3Wn6iXsgjnYpdocuAuLGGOSc-rWOZiQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a856502fd2.mp4?token=SxoTUlTs2Gs74QQAuKt3WfcIgoFb2D3_TX9JVLc9rxyG4klPC8JHUx3Uh4ulvMLThFmJITvPDTOYS-OwII_njtHtau_5-VSLuHFXjazCGGdnu6Sg0D66s8ZmNZxkLvbE-T8AG-yFikvWONYzEJF38v6WCYJTBLLlkRhPsNRzuXZhT94yP8PNx5CKrhNderIooyvTOy7c-gP0SfxZdcNr28Mlc65JY1GOhIrCpZ-puH_T_mN1sp1LY4YRj57ZkjRtjB5oqnYG3-oA3I6YcxdUOsTRfxZSzTSYglqOxwHjrdSVRQ2ZRQnTOjs3Wn6iXsgjnYpdocuAuLGGOSc-rWOZiQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
ترخیص ۵۱ اتوبوس ضدآلایندگی از گمرک هرمزگان
🔹
رئیس‌ دادگستری هرمزگان: با پیگیری دستگاه قضایی، ۵۱ دستگاه اتوبوس ۱۸ متری مجهز به سامانه‌های ضدآلایندگی از گمرک ترخیص و به ناوگان حمل‌ونقل شهری کشور اضافه شد.
🔹
این اتوبوس‌ها با هدف کاهش آلودگی هوا و روان‌سازی ترافیک شهری وارد چرخۀ خدمت می‌شوند و ظرفیت جابه‌جایی مسافر در هر دستگاه معادل یک واگن قطار شهری است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/farsna/441095" target="_blank">📅 11:07 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441094">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">احتمال شنیدن صدای انفجار در جنوب اصفهان
🔹
سپاه اصفهان: به‌دلیل انجام انفجارهای کنترل‌شده تا ساعت ۱۴ امروز، احتمال شنیدن صدای این انفجارها در صفه، بهارستان و اطراف آن وجود دارد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/farsna/441094" target="_blank">📅 10:46 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441093">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/35603f2115.mp4?token=dxEnDbEAiZJaJkH5rEqyUWVf6WL4RwsLcxLvTAQqkSQun_dKdvCc3AoZATeECwEnRQfdskUk5NRxsQLhHkxGhybL12KI1tDHktnXNhtu5fEzVdzTHh15QQ0rWoWI9J2EFRMrAkpQDPWjro05JXOQqKIvwuhgd1kXYVJbDgYOcN3d9vtqaeRKi9s0WlpIxM__wJj7Vv19-8Ba6xLpfylhZfgZOdV-95WmYAi124JZhofLqUFhwgXxqLdvhfH3IEyuQHB7wUwh3reiry1grio76OT2S1-e1DMZD50SNRnCv-O0wIWSEUI8By4RGqrtYWyTaKavXXcyksZx1Jo7YOE6KA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/35603f2115.mp4?token=dxEnDbEAiZJaJkH5rEqyUWVf6WL4RwsLcxLvTAQqkSQun_dKdvCc3AoZATeECwEnRQfdskUk5NRxsQLhHkxGhybL12KI1tDHktnXNhtu5fEzVdzTHh15QQ0rWoWI9J2EFRMrAkpQDPWjro05JXOQqKIvwuhgd1kXYVJbDgYOcN3d9vtqaeRKi9s0WlpIxM__wJj7Vv19-8Ba6xLpfylhZfgZOdV-95WmYAi124JZhofLqUFhwgXxqLdvhfH3IEyuQHB7wUwh3reiry1grio76OT2S1-e1DMZD50SNRnCv-O0wIWSEUI8By4RGqrtYWyTaKavXXcyksZx1Jo7YOE6KA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
شنیده‌شدن صدای انفجار در بندرعباس
🔹
دقایقی پیش صدای چندین انفجار شدید در بندرعباس شنیده شد. هنوز محل دقیق این انفجارها مشخص نیست.
🔹
همچنین ساعتی پیش، دو مخزن آب در بخش بمانی سیریک هدف قرار گرفت و تخریب شد.
🔸
در ساعات گذشته پدافند در مناطقی از بندرعباس و…</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/farsna/441093" target="_blank">📅 10:31 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441092">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">توقیف اموال ۴۷ خائن به وطن در خراسان‌شمالی
🔹
رئیس‌کل دادگستری خراسان‌شمالی: تاکنون اموال ۴۷ خائن به وطن و افراد تأثیرگذار در شبکهٔ کمک به‌نفع دشمن، در خراسان‌شمالی شناسایی و توقیف شده است.
🔹
۴ نفر از متهمان مقیم آلمان، ۶ نفر مقیم انگلیس، ۲ نفر مقیم فرانسه، ۱۰ نفر مقیم ترکیه، ۵ نفر مقیم آمریکا، ۲ نفر مقیم کانادا، ۲ نفر مقیم ایتالیا، ۲ نفر مقیم استرالیا، ۲ نفر مقیم عمان و مابقی مقیم دانمارک، اسپانیا، قطر، امارات، چین، اسکاتلند، قبرس، یونان، نیوزیلند و کشورهای دیگر هستند که دستور‌های لازم در راستای توقیف اموال آن‌ها صادر شده است.
@Farsna</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/farsna/441092" target="_blank">📅 10:22 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441091">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iCcGxpDN316qA8qqcs3ylFNP4LCxv4LQFnOeUpjZaANjzlBhPHb8Rll9GaOwhLAr9fYupbl2H7WfoUk6d2t7FhojYNT6IjiOygSAlubEbW7W0jmIUpJERLDt5e9KH1JmavBqosGexRUl3FsJC_mfCXMb2Nnjhh1dG5BegC-pbmlbzK76J7CsVhEtcH2Wavgq3nETwevJvw8_tFmCTWDDpGXMTUieEuai2j3jqcAm2Upv2UHLqn3RIwx1Fcb-VThtGEswb41fsdcuWMMAXXYaS0n9IYR6hjeng-aR9xAv6khtnc2PrxJVmWdM60EzpGz_VbfeRLjWliL_UfpdAhU28A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
اولین سالگرد شهادت شهید نصیرباغبان فرمانده اطلاعات نیروی قدس سپاه
🔹
پنجشنبه ۲۱ خرداد ساعت ۱۷ الی ۱۹ حرم حضرت عبدالعظیم (ع)
@Farsna</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/farsna/441091" target="_blank">📅 10:20 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441090">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">تماس‌های خانگی رایگان شد
🔹
شرکت مخابرات همزمان با افزایش ۴۵ درصدی آبونمان تلفن ثابت، اعلام کرد مکالمات درون‌شهری و بین‌شهری به‌صورت ثابت به ثابت برای مشترکان خانگی از ابتدای خرداد رایگان محاسبه می‌شود.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/farsna/441090" target="_blank">📅 10:14 · 20 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>

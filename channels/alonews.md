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
<img src="https://cdn4.telesco.pe/file/DsB9mXv2uxm7MXJix9mM3JYaF3XzXK9WTS-GEBCgnWS0ERPfaGtOVEzCjbI9jbtvhu6NgeDMeAgQlE6jY_Mw2Ie5In8m9FqGBBSeTjCw7BeqlOrRplUwk4MnuOTrHoVngFWoxg6i23Fs--qzSZd0W9OVPtocva41eShDEyV0PYgSmVeRLLSBKcIZAQTfiN4pxbUmlDmCfIn4qCJFEkffW7_A3LV2Sx7jrQ4-2A_MGHehSgui5ypdFXdLVn-Qf7cEa9rlqErSb7EU2wE2-tAlOEt_cZJnZf8MvCIGSLODyEqzyB12Y4XScwSdh-PxruPsrpNEb2znPNt4Ddk7TkkfQw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 اخبار جنگ الونیوز AloNews</h1>
<p>@alonews • 👥 971K عضو</p>
<a href="https://t.me/alonews" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 با الونیوز از اخبار جنگ و وقایع در چند ثانیه مطلع باش!اخبار جنگ بدون سانسور در الونیوز👌جهت رزرو تبلیغات👇https://t.me/ads_alonewsپشتیبانی کانال🕵️https://t.me/AloNews?directمالک کانال🎩@AloNewsBotX:https://x.com/AloNewsBot</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-06 17:05:27</div>
<hr>

<div class="tg-post" id="msg-144249">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XDJohzhIOi-U-OHyvvkLMYjGT-a7hNnW-ut1F48eM_TcUMAdHuGD0j--DbTemv1GvQqRY3dWHiyQ3lHpaFMaz2Xr7vTclea2-BnWTzO53LqGiCBNvnOab3GEwKVuQ9DizCfK1XUvL-BaFzlIET6z7BBwewvt7tEpsNgpBm9fnXmS6xzAEEWLzmHiQIO_H_0hC4aO_0JdVfLS-ejwoxblgrIMm7onlFJGVP9jHLZbjz6wzIE83xM5PqG0FE2l85muRnPofX5rB0fmpsL1aCOfk1Q0yWxq5jMAsUyYnMa7mAaa6OQUTzrWikqTAEDAkOrydYFMQYAdvG1MqizAaVawMg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
رویترز: کره جنوبی از تلاش‌های ترامپ برای ازسرگیری مذاکرات با کره شمالی حمایت می‌کند، اما خواستار خلع سلاح هسته‌ای، آمادگی امنیتی بالا و نقش محوری در مذاکرات است.
🔴
سئول همچنین قصد دارد همکاری با واشنگتن در زمینه سرمایه‌گذاری، اطلاعات و کنترل عملیاتی زمان جنگ را تعمیق کند و همزمان برای مقابله با تهدیدات هسته‌ای و موشکی کره شمالی، رزمایش‌های مشترکی با آمریکا و ژاپن برگزار کند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 7.18K · <a href="https://t.me/alonews/144249" target="_blank">📅 16:50 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144248">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/c129d7d8d9.mp4?token=VIvlJa6HrKO0s2hF173MQM4gbJw_06fPuSC4ChfpTHZCbxPG5UB0Y8kkq8trhybdokf8R7GhjD2vbgMJqEPGEYMDC7HW79qFYBqIm2-PbURh312G7GO5oXyRfHzVIauC1LOXlLqKp0nvXZaS4b-O9VRYqPSfpc44PcxcO_0Ktpt9K3ND8GTqsMnocamiXs4BxzSV5jjW8Kqwj4nA97mynKEQU7x4UDnxcrzneZinQiuWdW4s6GnBtOUH_aa2iWEFDeZOU3frr2CZVxl0CaXGRXc8ePnTHgOugFq_8NVPWVkJDDHoZo5dF34dK3dAcLp225YajvRmCR9iUB-sOvhMfA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/c129d7d8d9.mp4?token=VIvlJa6HrKO0s2hF173MQM4gbJw_06fPuSC4ChfpTHZCbxPG5UB0Y8kkq8trhybdokf8R7GhjD2vbgMJqEPGEYMDC7HW79qFYBqIm2-PbURh312G7GO5oXyRfHzVIauC1LOXlLqKp0nvXZaS4b-O9VRYqPSfpc44PcxcO_0Ktpt9K3ND8GTqsMnocamiXs4BxzSV5jjW8Kqwj4nA97mynKEQU7x4UDnxcrzneZinQiuWdW4s6GnBtOUH_aa2iWEFDeZOU3frr2CZVxl0CaXGRXc8ePnTHgOugFq_8NVPWVkJDDHoZo5dF34dK3dAcLp225YajvRmCR9iUB-sOvhMfA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
تو یکی از خیابون‌های ساری، یه خانمی داشت خیابون رو برعکس میرفت!
🔴
وقتی مردم بهش اعتراض کردن که داری خلاف میای، طلبکار شد و گفت من دارم درست میام، شماها اشتباه میکنین.
✅
@AloNews</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/alonews/144248" target="_blank">📅 16:40 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144247">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">به جای روزی دو ساعت خبر خوندن، پنج دقیقه کانال ماهان رو بخون هر خبری درمورد تورم و گرونی هست اول اینجا میزاره
https://t.me/+6PPyWURHtW5jN2M0</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/alonews/144247" target="_blank">📅 16:38 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144246">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">‏
👈
عباس عراقچی:
همه کشورها موظف‌اند از اجرای تحریم‌های یک‌جانبه آمریکا خودداری کنند و تحریم‌های اقتصادی آمریکا علیه ایران کاملاً غیرقانونی و فاقد هرگونه توجیه هستند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/alonews/144246" target="_blank">📅 16:27 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144244">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/S3QRLX9BMLYVZ17UT_-FRCw-2ZEvmjZNCP-QLCB8ZlzLBnUdxaikyaQ5Ladnz5i84e14OvlQDR15K9Hw4V66muym4rxhidVmK6A-Vk1_MGtaHVcsAZwx2jcCcAzloFgKysiLomXnIN_sI-V_BnWyc0yzezSDjVxt1I1L9wArcvTVGTE8Ks-IS8FIwRfVNJIy39EmG3ex-0Qdku1t5wGY0yYM-nORmbyJq-FHlEw7TMrWWAySxWPJP8-Q--ZBI5en-qLo0lDfCqSUV9DzDvJR1BBsKcC54TEkVAKAlnRpOBtXIiAqF47p_TFugtWPeKgVEVHH_GeCRo0nvsKDKWHONw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
پست جدید ترامپ:
دیگر خبری از پسر خوب نیست!
✅
@AloNews</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/alonews/144244" target="_blank">📅 16:12 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144243">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Hs8jonNZMa2WOE3R3cMYgRq2pNzP12X7RqSNrpSV-8Lx7AUXNZr_PKOH-xHEQ71wUTIfPvVVqC-iOpM5TsM-UvA1_u77aaGoRcpt7yMB_w_CbmV5jA3arnzxEPKEyo6Wf--sLr0Dmce8ZoxJlM3a-w_ka_j-Em6cteAYNnk12hKAg-D85nSe4BTEvPoTxnDHiVHZm3e4PUbrxla8WmMryoX2OG8i5Bi6lMM8NiXyl-bTu_dSt5zJzaJ-yZiwdW0KSIH4y_UJVUJ8VNIffzcc2otJW_6vPnaZ2WnMeFF3ewQjpOBEXlS3lnA_-uixqkOEHSub4dWBh4r5F4b1CK7d-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
👈
تصاویر ماهواره‌ای نشان می‌دهد که یک فروند دیگر از بمب‌افکن‌های روسی Tu-95MS در اثر حملهٔ پهپادی اوکراین به پایگاه هوایی انگلس-۲ آسیب دیده است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/alonews/144243" target="_blank">📅 16:04 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144242">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JLGsFs5vnKFGjlqeZ6KgkviQI5qXwQfPRCpk-mLeKvdBHEejRvg8mkXT2UmQJxoZzEBXXXsU2rqV9Y-ywHGWx3ArNm6UnOLDbB4R1qTqlbothJaSn70iYO9eP-7pgn9M9H23x2DXDGfCVsAvRku8IYHr68s5Hhefp11PTfr-8bqmgaNFIXq2aOnRdZY_FRFwgsYfYrDJV0r6Oh3CsdOe1EAARau2FhsQBRZOvXMkYtr7jli7-25yAczTNa0NY_QAjCe6zV48L1HMhFBxcqy3E15mCN2iRTHF-aVxhzdC9c_lZYWwjdwtITiVnRdUMTwJEUmd-4zogv2nF5sYcyoK8Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
عربستان برای دومین بار در یک ماه نفت سنگین به چین فروخت
🔴
به گزارش بلومبرگ، عربستان سعودی برای دومین بار در ماه جاری، محموله‌هایی از گریدهای سنگین نفت خام خود را به پالایشگاه‌های چینی فروخته است.
🔴
این فروش نشان‌دهنده ادامه تقاضای پالایشگاه‌های چین برای نفت سنگین عربستان در بازار آسیاست.
✅
@AloNews</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/alonews/144242" target="_blank">📅 15:57 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144240">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KASkGtLuTZgVOMn7e5845WO9lrOzov8Y22gFeQMUPIuAqJWqmSHwn9xY6V0SgcmxircJyBkb418g0krL1uWJs16kTj003ZW_PlQbKVDQ2UXsP8q73K7_my9MWAZ0k10dzdg9UJvDYalu4HvuM9gACJXc-r_ayYiGUGendVbzOriqcxcdlY-3hGyBYWZvo9hEdXKWDkIkASutE3YuP6I6wa4p8ZJPxpNH8ALm6ynKsDaJvife71-0Symlu2nPRkBGTyyaR3a0IzYUxvKvBvgTGFSu7U1kMG5XBukiYS4gQX2ExtY5ol07KfIqZLMJ5vw-Jxz2SwiOyGOjMe22NwSBcQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
توهین علم‌الهدی به مردم:
اگر آمریکا بخواهد یک لشکر راه بیندازد، از همین بی‌بند و بارها و افراد بی‌توجه به دین راه می‌اندازد
#مفتخور
#بشکه
✅
@AloNews</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/alonews/144240" target="_blank">📅 15:45 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144238">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/bUuCVwCYe00rGKnc1cr6XiH01PMNFPrizsgnko1yytRUfJIw_KJsQzA6QnoXJESm0XweFkK-wdnQDLkqxMHqukJ5p9m7vKQJqDJwu1z7UUN_rtsTig2d8Q8R7yxEHMYGxvkitCKBg41VB4i3yslkVbuCTFpgbGidnUSkSceByE8jLWsL80qrNRSR0hz5HBKiqDu7QsCjvRgqj0fU9Poj2fTxeL7DCpKNpgh19xEMN-ran74RLbRqOyDDoXyrJ9PFO0dDOoUK5l9QpUqe829z50fRTQD61xQLyKPsZ533y8hxrUq9zV_hFD6iwPbAP1b_8TyshLoukfLfkqsq-ELiZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Gv-wXxE2VY-tNI8vK7PMbzPm-hGLiUU9s4Hty0db4SMuvqPNTaeu9fA6cLFEGNMKkA2WH0-SzMZlLnVIlrswj7ehDyYu4nxh1WFIxFOGFQ4HNb-5jwCZaIu1ba89_8JVDkHSpnID63ZmSTJh4zFtS6vdICPXsapWX3ggGy03z8MqrEN8gbOECEt2aVt4bU4dGpYYxyO6zNAV9ozaTFOZO2MRdiNKuRbPy54ZIK_cW6CCL-liY8iuGGzlOI1EqPyMaGNIkPMsp3VBpvJu21HduSmSxOn1VorQfsWvnSzC_iY0KMK2diroTtwPz3hI7RiEpWfWGK9FMOCAY_HgQO3rOg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
تجمع اقلیت بیکار و الاف در اعتراض به وضعیت حجاب زنان در مشهد
🔴
پ.ن: تجربه ثابت کرده زشت‌ها به خوشگل‌ها حسودی میکنن
✅
@AloNews</div>
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/alonews/144238" target="_blank">📅 15:41 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144236">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lYTd1hUvv7UDHvMwDT0mhr6V3LAZbb180kxJYhcBgE5tS9vwrumaDWF4hOCotarNnWigEeTEpX2BMLkW7bp2fDw9OCCdiEC-ipkz8EAolujdIjvbWnBf4gODFNJCuaLXpNzB8GcbklHuRDTuvPNf1Df4MekueFNd2UR5tqc9BWfVKZcchiRmtNTdosXgtHLxvy_PQTwTII3Pb2D5G5i-ExAeGh9ww49vkHlnzwNQnLbiI-H6CQCb1yfUoaO85zbYsvHI1h4PA4XVuzgytq9H9zHmDTmDu1IDp-x-V2jWSKkjjRfd3F4_OBAZjh1aJqRf4F2ofqa2VeynxplopxVzBg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
شاهکار یکی از دانش آموزان
✅
@AloNews</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/alonews/144236" target="_blank">📅 15:39 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144235">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">👈
نتایج امتحانات نهایی تیر و مرداد ماه اعلام شد.
🔴
از طریق سایت زیر میتونین نتایج ریدمان خودتون رو ببینین:   https://my.sanjesh.org/
✅
@AloNews</div>
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/alonews/144235" target="_blank">📅 15:33 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144234">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ohn4HITbRqQ90gc5juETocUw676jzW9vH2YEgnUmC8_ZtSeQx6FtefeWRcPfZvOG4tC1AAeNtODDFHhE1tSNcXEE1A6RK2qsmGtruzj0oRXt3SmODlcOcZMs3wOAg33J_A16A-Oe8200watlDsaxD_edKrNG1Cqwq1YFPNpP5hxlP9BdTWtvFT1DJpUg3zShCN2qD0R3B7JyZQDpg5_ZycrGBUYXjNzB0zbkFESJMHnoytf8PkVy6Z5ylawp48CF-CE_B2LPCepJMBA11qfZ1AUedSUhceOgn8mw2uuUeallsSJYhgUiwxroSdsexARxiByBObVFP5-zlw-fjvromg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">😐
😐
😐
😐
😐
😐
😐
😐
✅
@AloNews</div>
<div class="tg-footer">👁️ 30.6K · <a href="https://t.me/alonews/144234" target="_blank">📅 15:28 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144233">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FYihsPTTxqwK-n9gywIiZgzVnE-P6jYmBfxd4tMvd0PXOEXjUu1m53rad7ctLdzwy0B4Zv6zZ3DQRqlsAsUc-hACfIpVZ260i9nZSVXSgDlEwqs84jjTqKmwCCVFgDrCidrdIRYP0XO4NbpdUFX-VVq33xZn8hlEa776NQj89L0BabRtgHXNZA6jFQSLPCQv-S7J0ClQdqKUbR3I3cXDTIatv4ON6ZcY2c40LurathIQaJcug7zV-wwgcEM6GrLqHdbZLfTV1eKdjfGoGdt7QAi1JbZRPrtct6PYQjsrZJHRhV2DoWxrFFFCGuIpLHbKy8GglUG6XRu1SCXhnhuJYQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
شاهکار یکی از دانش آموزا
😐
✅
@AloNews</div>
<div class="tg-footer">👁️ 30.7K · <a href="https://t.me/alonews/144233" target="_blank">📅 15:26 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144232">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">👈
نتایج امتحانات نهایی تیر و مرداد ماه اعلام شد.
🔴
از طریق سایت زیر میتونین نتایج ریدمان خودتون رو ببینین:   https://my.sanjesh.org/
✅
@AloNews</div>
<div class="tg-footer">👁️ 30.6K · <a href="https://t.me/alonews/144232" target="_blank">📅 15:23 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144231">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">👈
نتایج امتحانات نهایی تیر و مرداد ماه اعلام شد.
🔴
از طریق سایت زیر میتونین نتایج ریدمان خودتون رو ببینین
:
https://my.sanjesh.org/
✅
@AloNews</div>
<div class="tg-footer">👁️ 30.7K · <a href="https://t.me/alonews/144231" target="_blank">📅 15:22 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144230">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/t1XSb_BQaIXKjxHwx6b7iSlfbK-sMs1AVGSaFltkDAeY38zz3hqZtIrXD56to069c8hIETDHV3Z6zBc_DPCzApMY2Qd-Em5cwyeoZUMid44M3Khee4ZfAVycjkHGIhLDX12ur7ULh5nHQCk6blT4BmYltKEpAZfs3tIppMbECLAErG4Sm684HjC4v2wkZ3MLnXmfJO99TzSTBEbcEZZ8gdnmrbTiNB2yPwagyr52j7Ouqzl4SwI5FBCL2SR2Ljb5Fm0ZCG-OGCNyxTqHxnECO2SOVxRxXWqETzMVcgZyEXiYflnfkZCgpUIccrAofwYVXzHN5BuAtt0lnDJRiFkq6Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
اقبالی، از نزدیکان جلیلی:
باید حکم زندان برای بی حجاب‌ها بدیم تا درس عبرتی برای زنان بی بند و بار باشه
✅
@AloNews</div>
<div class="tg-footer">👁️ 31.7K · <a href="https://t.me/alonews/144230" target="_blank">📅 15:18 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144229">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">👈
حمید رسایی: حجاب از نان واجبتره، چون مردها حتی با مو هم تحریک و به فساد کشیده میشن
✅
@AloNews</div>
<div class="tg-footer">👁️ 29.6K · <a href="https://t.me/alonews/144229" target="_blank">📅 15:17 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144228">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ckkDtyiiTt0o0KT9foGby9heldA5tLE-pGC5B6_ODsnF-lIOMKCIJ02lMhPESPySdGpbotE4oUDr4QPnOfL1M_aw9oor-X4JVmlaoV6jqMF16FTonIdUQ_s20AZusWYmu06sUyBjSF3Tk0Vx_1RDRwK62jqnVOiMC8hCMT8s4Cn1lcYj2GzGeEN4KT8BKAXYeaWFBNt32lqQCdvpklQlnnJUI3Q1miUKbtMSchxhYxlj9Na5chOLTSH09VODAx6a4ntbk6IlW7c22a95Rgj7q8Tx9MQz1TDNvR0x0dkRCd9bwp3vMxyj_eFZSdsYRPN1Rx373LMstZ9gcrste_nAvQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
حمید رسایی:
حجاب از نان واجبتره، چون مردها حتی با مو هم تحریک و به فساد کشیده میشن
✅
@AloNews</div>
<div class="tg-footer">👁️ 31.7K · <a href="https://t.me/alonews/144228" target="_blank">📅 15:14 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144227">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SfjvjN-znWhdOebN61J4DcBopVRfDkNTWbtk1S984Xw-bvWWYcjWd0J6c-I28vNFl50dwCoYf-cWoNQ0wXo2KlqHP_NAel6C64hSSHWMVJ2cBRwJGGdFQhXtP29FonthBkhq8Xnk9e0U-PcnDvMzaxRmSmlUp2-gpUGndteNcuVyswwB8mySk8bIFOnEMzNW-aR7zLSLVN4_YZGAi0svPpp62p2FduGrr19FY9BoNoJnE6bnsI1bnhjRj6EBUkt0ea30eRk4r8TtBmMSDUCROkZzpzvugFuF3LUhZlOwsjELiZVpycW_BIlcgMhyFfWXXRxNQygemBFTm7DMDQeDAA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
تمسخر طرفداران پهلوی توسط علی کریمی
✅
@AloNews</div>
<div class="tg-footer">👁️ 31.7K · <a href="https://t.me/alonews/144227" target="_blank">📅 15:08 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144226">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4cadbbc54a.mp4?token=uY4ebh5eIzgxeNrK5icIsQRzEqLbRGS6FFii8i-kGGpnQ33bxgTIAr3q3TgBTJq5zFJ3EPJfdEDTiNnJpmtG2qVvXeaVCysRxZqj5WNTiAtICfhoTkgNhWlYnuHwMz4H4VCRbEorQKxMNzlgODUkineLcYDbJoyny4s7QFK-aFz6UQv1ggbQ7yGNzAVb0HQKWKdz4e3Wt6PpHB5wPcNrAW51QuNpUqPtWx3JXkBnKvds7NZdPLoIxGeuVutSXQaeP1VI0rpwsSrbi6_ZmPMv2xUrP605lfV2eUdbJUMfY2p1G4XHYIR6X9i3zfuL0FpOcQ9WZeEUtOuDLL4ZDuiA3A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4cadbbc54a.mp4?token=uY4ebh5eIzgxeNrK5icIsQRzEqLbRGS6FFii8i-kGGpnQ33bxgTIAr3q3TgBTJq5zFJ3EPJfdEDTiNnJpmtG2qVvXeaVCysRxZqj5WNTiAtICfhoTkgNhWlYnuHwMz4H4VCRbEorQKxMNzlgODUkineLcYDbJoyny4s7QFK-aFz6UQv1ggbQ7yGNzAVb0HQKWKdz4e3Wt6PpHB5wPcNrAW51QuNpUqPtWx3JXkBnKvds7NZdPLoIxGeuVutSXQaeP1VI0rpwsSrbi6_ZmPMv2xUrP605lfV2eUdbJUMfY2p1G4XHYIR6X9i3zfuL0FpOcQ9WZeEUtOuDLL4ZDuiA3A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
نتانیاهو: ما اسلام را ویران نکردیم، من قصد ویران کردن اسلام را ندارم.
✅
@AloNews</div>
<div class="tg-footer">👁️ 32.7K · <a href="https://t.me/alonews/144226" target="_blank">📅 15:00 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144224">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lH1adrjdUFwG_D9D-8PGjqu4WX8FJawA3RiRjSGl3dgK5k3kO4Yi-I-lAfvw9U_fWOVFYWXI7u2ErxvOkHAEpH4O2nlMOz6evYW3aP3wAnaZNtD53W34baI0NHlxJQ-k-5Sq4ISOGJdzK8XmPKe8xue1f4sRMabso49QuIiF2CK3u5u6ClLL1a-TbOqCnIm_0KUfjmO9YKSoN3Rfme06Xf0bwcdqgmy9Ovaoz_nCuEO0WCJjxOi36dZ0T6yNjrGMYJi6Hc1EDP4uu-0cgy0TjSANCUMO2IObZBfD3AkLyDtwkDCKROH7eww7ruxF3jH_p5gz16WZh_5jsgDbiEVl7g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
وضعیت نزولی ذخایر نفت چین
✅
@AloNews</div>
<div class="tg-footer">👁️ 33.7K · <a href="https://t.me/alonews/144224" target="_blank">📅 14:56 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144223">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">👈
آکسیوس: هدف ایالات متحده این است که تا اواسط سپتامبر، عرض کانال اصلی را افزایش دهد تا حداقل ۵۰ کشتی در هر شب بتوانند از آن عبور کنند، و هدف بلندمدت، بازگرداندن ۶۰ تا ۷۰ درصد از حجم صادرات نفت قبل از جنگ است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 37.8K · <a href="https://t.me/alonews/144223" target="_blank">📅 14:32 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144222">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">👈
آکسیوس: تعداد کشتی های عبوری از تنگه هرمز، به ۲۰ تا ۳۰ تانکر در هر شب افزایش یافته است و این کشتی‌ها ۹ تا ۱۰ میلیون بشکه نفت حمل می‌کنند، که تقریباً نیمی از حجم صادرات نفت قبل از جنگ است.
🔴
امارات متحده عربی، بحرین و کویت به مسیر صادراتی تحت حمایت ایالات متحده پیوسته‌اند؛ انتظار می‌رود عربستان سعودی نیز به این گروه بپیوندد و قطر ممکن است به زودی تانکر‌های گاز مایع (LNG) را به این مسیر اعزام کند.
🔴
ایران به سمت کشتی‌ها شلیک کرده است، اما دقت این شلیک‌ها "محدود" بوده است، به طوری که تنها حدود ۲ درصد از کشتی‌هایی که ماه گذشته از این تنگه عبور کرده‌اند، مورد اصابت قرار گرفته‌اند.
﻿
✅
@AloNews</div>
<div class="tg-footer">👁️ 37.8K · <a href="https://t.me/alonews/144222" target="_blank">📅 14:32 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144221">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">👈
رویترز: کشور‌های حوزه خلیج فارس در حال تسریع میلیارد‌ها دلار سرمایه‌گذاری در بنادر، خطوط لوله و راه‌آهن هستند تا وابستگی خود به تنگه هرمز را کاهش دهند
✅
@AloNews</div>
<div class="tg-footer">👁️ 39.8K · <a href="https://t.me/alonews/144221" target="_blank">📅 14:15 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144220">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">👈
واکنش جدید چین به جنگ اقتصادی آمریکا علیه ایران: با تحریم‌های یکجانبه مخالفیم/ گفت‌وگو و مذاکره تنها راه حل مسائل است
✅
@AloNews</div>
<div class="tg-footer">👁️ 39.8K · <a href="https://t.me/alonews/144220" target="_blank">📅 14:09 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144219">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lv908IflmBclKTWQqID8RoN-dzLRG-eOTu4bJOKlz3rjQnu5BDeF7j8UrVGXkKaMt7QGGF2Xs3KF0MMI-rBTi0wFsq3Dg3LgDbOffzpUbyM8QgE3BtmitkkzsxfSlKFrrY7MR-1K5mZUuqNKA3w9w12OXHqQStIjCaRUt-CvrWGdrijkK2aArzYLDMNmFHT7ptnbGvXdwyodLjmyKFXe71iIr03Jiub7xo06Pyq_iFqfmR90rOjmBOhfdxChNVlqFblkFDQCBxgdE4TmFYCO580DsB9cFAJ5wyDrO9Wz1F-As0c36bmS0E9O226-0SckpZhForn9u7kP9zv9mbM-6A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
آکسیوس به نقل از منابع:
ایران اخیراً علاقه جدیدی به مذاکرات نشان داده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 40.9K · <a href="https://t.me/alonews/144219" target="_blank">📅 14:02 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144218">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">👈
خبرنگار الجزیره: ایران از هرمز به‌عنوان «بمب هسته‌ای جغرافیایی» استفاده می‌کند
🔴
با فعال کردن و استفاده از این اهرم هیچ گزینه‌ای جز در نظر گرفتن آن وجود ندارد
✅
@AloNews</div>
<div class="tg-footer">👁️ 41.9K · <a href="https://t.me/alonews/144218" target="_blank">📅 13:47 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144217">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">👈
ترامپ به اکسیوس: تنگه هرمز باز است، آمریکا در نبرد هرمز دست بالا را دارد و پاسخ ایران بسیار متواضعانه است.
🔴
ایرانی‌ها نمی‌خواهند ما دوباره به آنها حمله کنیم و این اصل مطلب است
✅
@AloNews</div>
<div class="tg-footer">👁️ 40.9K · <a href="https://t.me/alonews/144217" target="_blank">📅 13:45 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144216">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">👈
امام جمعه قم: هر گوشی تلفن همراه یک سنگر است که ممکن است زمینه نفوذ دشمن را فراهم کند
✅
@AloNews</div>
<div class="tg-footer">👁️ 40.8K · <a href="https://t.me/alonews/144216" target="_blank">📅 13:40 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144215">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FL9DUqHXTpGHhxxBnRGzEr-_vMU56a-H7OZYeRxH1EtW9vc2rHUTtHUpnp7qsqR770XZEHMqyeoxp6RUWukXCV0kPVcpC5d9BRw9Oxi_itoeXeHKEpgQRlcKcMBF5nMK4AGwOqReqLtfFEJH9lYt7x0bYlWEsfB2qOsh3kub2gxFJYCGuUIbuavsaqHp2Jt-tUFA4kum1FMlqCyy8SxZ6gr0XdXWcEBcYWLwpKtc5WcauR2O0fsch_v-_MDvymriMs5xbN3RtbzjMOTB9kSRG-JuGU0uJxvf0N_6q-DpEVfSkRYMJ8DMzfUS5uXm4crGy46uH2tjkVOW_goiJBW9Qw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
واکنش معاون عراقچی به ادعای مالکیت ترامپ بر تنگه هرمز: اسکیزوفرنی نوعی اختلال روان پریشی پیچیده و حاد است که با اختلال در تفکر و درک تحریف شده از واقعیت متبلور می‌شود.
🔴
شایع‌ترین علامت آن نیز توهم و هذیان است.
🔴
روانشناسان توصیه می کنند چنین بیمارانی باید به‌صورت ۲۴ ساعته تحت نظر باشند و درمان شوند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 42.9K · <a href="https://t.me/alonews/144215" target="_blank">📅 13:35 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144214">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">👈
سخنگوی کرملین ، پسکوف: فعلاً برنامه‌ای برای گفت‌وگوی پوتین و ترامپ وجود ندارد
✅
@AloNews</div>
<div class="tg-footer">👁️ 39.8K · <a href="https://t.me/alonews/144214" target="_blank">📅 13:30 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144213">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">👈
الجزیره: تلاش‌های دیپلماتیک با سفر مقام‌های منطقه‌ای به تهران شدت گرفته است
✅
@AloNews</div>
<div class="tg-footer">👁️ 41.9K · <a href="https://t.me/alonews/144213" target="_blank">📅 13:21 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144212">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/odwO0YMSiBVnzdYmKgBHmu77dgnIXoV1SVBXuQlH2P9lXanu2azY6oydtT32BSnlzliFgNenuVe7dZOts1S3AEVEczipZqkKIFrPjKRv7CNIXQIWfLVNNet3uAOwWYJ7AZDweXz5FN9HCqff-RsePGxGo0pU6E-H09x_4sfnf3tmdqb62eQqmCBQ1MVvDTN7zADZE4ReeO4PKzrIL6wT7MWlfChYwMUuslZAJiTAn5NKPSZXL4X_9LriaRi9eDeLUSfwcmOpXOMRskhZIsFGwjnP3T6pf3yFKoC_zpMD_NctqzrR91T-AMc5TjCbk5f3kzgWcitjOPa5KPr4wzvAlA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
آکسیوس: آمریکا در نبرد تنگه هرمز، دست بالاتر رو در اختیار داره
✅
@AloNews</div>
<div class="tg-footer">👁️ 43.9K · <a href="https://t.me/alonews/144212" target="_blank">📅 13:15 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144211">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bJT4Klhm-5rOB7iwC1ILGtvgZxgCExHYQhEeTBZ4MFgBC1Bf8qrH9pZRllDECBxuvXSnutEq8KcvRuYIMur03JKwrALazvQuo-vmR2ZJWOC1KReWIJSypD57ZlnEGUu5bGAABlhFxvphKy6BdK9pLgStl6utmK6LH8ZVtqYbQ7IZokBhvq5lRtZ_JBE_ZCFwZo_xy3RkwY1PLrQKh4E6FpRf7c-hWVVJmxztxC82ThL-JkKZ8Txp_kDoR0A410kQrvTAqdUedp0soGv89ngU2vRr-_Xwh1lRiSQSNXP9rrHnq0ZqdE7yksdG4zldLCPbMFRJmfG9WEdPytYv498Wog.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
پفک ۱۱۵ هزار تومانی!!
🔴
یه زمانی با همین پول میشد ۳تا پیکان خرید
✅
@AloNews</div>
<div class="tg-footer">👁️ 43.9K · <a href="https://t.me/alonews/144211" target="_blank">📅 13:10 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144210">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dc46ec0bdd.mp4?token=ZiF2RrstXlmY0_X9NA-QqqaCGLICh9IpajOs--1mmr-I_uunqjqO4X58BX_AtD1jPWa6wZIbRxi0a4aYO-aJgvvdsgoKsZHW0ev-zWqUA4J3wF2zo4MZaUa41W9VGRpuFjJxSqGUdaFLBWV9U70g11fyT3acRSgDcWXkUQpG6AhCaoGQp1V5mSlj8EshoQ9ISzXySSy5CoRVSk4LB8XnBYh-EspGYBuUnv-FsZM-L1kJ5BtW7tNny1UkSlGrblno3lnXabUOVAeMUEHypHMIX8anb8q01FIP0SBDuctDgQZn6gAe4d5OFJhcy1T4Ogz7eWUb3cLMivumd_t90jAqCg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dc46ec0bdd.mp4?token=ZiF2RrstXlmY0_X9NA-QqqaCGLICh9IpajOs--1mmr-I_uunqjqO4X58BX_AtD1jPWa6wZIbRxi0a4aYO-aJgvvdsgoKsZHW0ev-zWqUA4J3wF2zo4MZaUa41W9VGRpuFjJxSqGUdaFLBWV9U70g11fyT3acRSgDcWXkUQpG6AhCaoGQp1V5mSlj8EshoQ9ISzXySSy5CoRVSk4LB8XnBYh-EspGYBuUnv-FsZM-L1kJ5BtW7tNny1UkSlGrblno3lnXabUOVAeMUEHypHMIX8anb8q01FIP0SBDuctDgQZn6gAe4d5OFJhcy1T4Ogz7eWUb3cLMivumd_t90jAqCg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
کلیپ را که می‌بینید فکر می‌کنید افتتاحیه پالایشگاه است، آخرش متوجه می‌شوید که افتتاح پمپ بنزین در اطراف شهر یاسوج با ۴ عدد نازل است.
🔴
با حضور استاندار و سایر مقامات استان
✅
@AloNews</div>
<div class="tg-footer">👁️ 40.8K · <a href="https://t.me/alonews/144210" target="_blank">📅 13:06 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144209">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">👈
مدیر اکتشافات شرکت ملی نفت: هم‌اکنون یک چاه در منطقهٔ «دهنو» استان فارس در حال حفاری است و امیدواریم در این منطقه نیز به کشف جدیدی دست پیدا کنیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 40.8K · <a href="https://t.me/alonews/144209" target="_blank">📅 12:57 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144208">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OBqa6zSmQKKspjyuyoCQPq10v5mHid8hXsQRb46drDJUhbky4EEOmfBEbkR8ra3g_wN5pM33zNmW4t81KvzdT1kr4Ihc9M6XhB9-mjsErhXPMUuHP3DUqFjbz7Bd0XaooeWJM1kpk3GqE91EXVapFTWQv78c3HCTzdD8R4HkdlckY8wb7X6NbbN4JXIShJBRHKPLDPFUii4o5ThIGJ5ea12waJhkMoh1AOmJ0Q2Dt40E0J8oInlvsJYGx7eI2dKzn59IVd7Tf-3HPnPNPbXc5Mzt0-CMAvhNZ766y-sgjvk093lAFzM6RxA2E_kwY0nENzCxeFd3wDFAUdvWaoCxlg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
قالیباف در پاسخ به فرمانده سنتکام، توئیت ۳۱ تیر خود را مجددا بازنشر کرد
🔴
در منطقه‌ای که ما نفت نفروشیم کسی نفت نخواهد فروخت
✅
@AloNews</div>
<div class="tg-footer">👁️ 44.3K · <a href="https://t.me/alonews/144208" target="_blank">📅 12:45 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144207">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/e_BDGU7tgDhe82qj1xT7OOKhSscRn2CApRHuP3-7adVCvFlcEXDdo1bZBlBnbOpDgcVMu8dtBs0higLeZqFJoKBY_7p9tmsjTy5f5LTGqiOYkDGGUlqjUex3esHjPnlG4PBmGVQBBJDWGs3OKjuljbZ-GJssoc6gad6DwnHs2mbmUDE29eLyu8GC_VV0kzDZstb-68mTw1wxke3tlk37YP8SXBARl_9gq57dVQYz1EdjveaiQhYU5svWuS4YT2e4Lf7aP9kyFfQF1B1KMVhqqkVdYofOXssmYlARJ8ykOPGBTkynzEG8jC1-MAGSwNq5NGDjK3Q5t4ctNmkTj-K7Vg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
دبیر: شرایط فعلی بخاطر خباثت دشمن هست و اگه کسی بیاد خیابون برای اعتراض سرباز دشمنه
✅
@AloNews</div>
<div class="tg-footer">👁️ 42.9K · <a href="https://t.me/alonews/144207" target="_blank">📅 12:30 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144206">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">👈
معاون وزیر نفت: در جنگ ۴۰ روزه، بارگیری نفت در جزیره خارگ نه‌تنها متوقف نشد، بلکه بیش از ۱۰ درصد افزایش یافت
✅
@AloNews</div>
<div class="tg-footer">👁️ 40.8K · <a href="https://t.me/alonews/144206" target="_blank">📅 12:24 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144205">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">👈
بلومبرگ:قطر، وضعیت "قوه قاهره" را بر روی صادرات گاز مایع به مدت یک ماه دیگر تمدید کرد. این اقدام در حالی انجام می‌شود که اختلالات در تردد دریایی در تنگه هرمز همچنان ادامه دارد و بازگشت جریان انرژی از خلیج فارس به سطح طبیعی خود را دشوارتر می‌کند
✅
@AloNews</div>
<div class="tg-footer">👁️ 42.9K · <a href="https://t.me/alonews/144205" target="_blank">📅 12:20 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144204">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">👈
کوثری، عضو کمیسیون امنیت ملی: هرگونه توافق با عمان مشروط به رفع محاصره دریایی است؛ در غیر این صورت تنگه هرمز بسته می‌ماند و ایران آماده اقدامات تهاجمی در هر نقطه‌ای خواهد بود.
✅
@AloNews</div>
<div class="tg-footer">👁️ 43.9K · <a href="https://t.me/alonews/144204" target="_blank">📅 12:17 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144203">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">👈
رسانه‌ عبری: تل‌آویو شکست طرح مناطق آزمایشی در جنوب لبنان را به واشنگتن اطلاع داده است
🔴
وب‌سایت خبری اسرائیلی والا نوشت: اسرائیل از طریق کانال‌های امنیتی به آمریکا اطلاع داده است که طرح ایجاد مناطق حائل/ممنوعه پروازی در جنوب لبنان شکست خورده است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 42.9K · <a href="https://t.me/alonews/144203" target="_blank">📅 12:16 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144202">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">👈
زلزله ۳.۲ ریشتری شمال سمنان را لرزاند
✅
@AloNews</div>
<div class="tg-footer">👁️ 42.9K · <a href="https://t.me/alonews/144202" target="_blank">📅 12:09 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144201">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">👈
وزیر خزانه‌داری آمریکا: در حالی که ایران هیچ نفتی صادر نمی‌کند ما طی دو هفته گذشته ۱۳۰ میلیون بشکه نفت از طریق تنگه هرمز منتقل کردیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 42.9K · <a href="https://t.me/alonews/144201" target="_blank">📅 12:05 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144200">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e0c2e88b27.mp4?token=AaLRNd1-nL2aLb8U45pIlR_0-yZTdMPZ09busmcDnps99FDWWYW8bjs7arJet2mGsQyZMgYLwvhmvxu2xXEWfXaNkCDdIFkLIOdY7E3ZNZs9NnlodXGOkjcorxI_4chQ4EZ9SdmOGw472jzLrX34bLiIe5sLCcOdzc7M4UpOvq5H4itd3q-oH2YNe2M1vmMbIKMpVu3msRwtYS2ul2PkcvLrjXv5QjytMYR6M26wrp9Jg5V2oaxRqByXcsPHaGrOtie8YFwfsIe6Tjfvl71XAOPi9jEXDg9P8QmtVquW2TNXdVG2eH6kOQ5BeOU5TGjZfDjjaKxRyUi12JXSomLAFoi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e0c2e88b27.mp4?token=AaLRNd1-nL2aLb8U45pIlR_0-yZTdMPZ09busmcDnps99FDWWYW8bjs7arJet2mGsQyZMgYLwvhmvxu2xXEWfXaNkCDdIFkLIOdY7E3ZNZs9NnlodXGOkjcorxI_4chQ4EZ9SdmOGw472jzLrX34bLiIe5sLCcOdzc7M4UpOvq5H4itd3q-oH2YNe2M1vmMbIKMpVu3msRwtYS2ul2PkcvLrjXv5QjytMYR6M26wrp9Jg5V2oaxRqByXcsPHaGrOtie8YFwfsIe6Tjfvl71XAOPi9jEXDg9P8QmtVquW2TNXdVG2eH6kOQ5BeOU5TGjZfDjjaKxRyUi12JXSomLAFoi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
کوثری، عضو کمیسیون امنیت ملی: هرگونه توافق با عمان مشروط به رفع محاصره دریایی است؛ در غیر این صورت تنگه هرمز بسته می‌ماند و ایران آماده اقدامات تهاجمی در هر نقطه‌ای خواهد بود.
✅
@AloNews</div>
<div class="tg-footer">👁️ 42.9K · <a href="https://t.me/alonews/144200" target="_blank">📅 12:00 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144199">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bc92d5b228.mp4?token=VAR-EFjxnRTs7w2-8lMcnfxtdsNyhoWgXHhBwAQFZYSytHIxWUDWwrLGonOSZ50nFAQAJZfe1Y4Y3dfSGhc4aK5U7yKepd4qqEM-pZFxYafCN1EQcUE_7j_wmZ7B52PjUlwdG5FjhGuz5twgtjITkgLQpdU6DvOGAHlbdXy1laNnbUzPFaRwBloMmRJKJ64Janh2jlHbuX_k66NsTJJS1YsKSGjEdU7rOl2Q_5w_XMD1sg_YCYZT5tlyglvSf_eqSfC22S2sn6aEGa1R4l9s7d20ca0WCV3zf0eQGET1DkNK8kqk0PddJKIGxfJQxo-n7imFGmEpNo8MbTjKJbAjNpPXQsQt6gLaNcAMR9GKZfMmN0xKg9kJ45J10NA5l7yT-oHQNFraM3TpjRUMGU4uBzezWSZgH747PMRvccS7tDwn-DQLSEUb2klK-dXAbgNOMlMLO0Qrlrek28tgpjYHUEAjj7IobAPDuoFp6j5zPWtd4YTeZ2_PynC_QqcT_ZoD35GlXrTjS87uMFNVC-DGPtYSpdvPovpAb5riAqn7gp4RbXnmuAXrcevJaQYXD01rccwh8mZI1AaWXGMD5RNaa3sQ2YX63_W3wemyUfTQ-tZdhr-9UkwMiuKWzC5q33aUUsDQ47QTuwCw2t4gUDEamVBfAj4ouHJiW9p2DZOd9js" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bc92d5b228.mp4?token=VAR-EFjxnRTs7w2-8lMcnfxtdsNyhoWgXHhBwAQFZYSytHIxWUDWwrLGonOSZ50nFAQAJZfe1Y4Y3dfSGhc4aK5U7yKepd4qqEM-pZFxYafCN1EQcUE_7j_wmZ7B52PjUlwdG5FjhGuz5twgtjITkgLQpdU6DvOGAHlbdXy1laNnbUzPFaRwBloMmRJKJ64Janh2jlHbuX_k66NsTJJS1YsKSGjEdU7rOl2Q_5w_XMD1sg_YCYZT5tlyglvSf_eqSfC22S2sn6aEGa1R4l9s7d20ca0WCV3zf0eQGET1DkNK8kqk0PddJKIGxfJQxo-n7imFGmEpNo8MbTjKJbAjNpPXQsQt6gLaNcAMR9GKZfMmN0xKg9kJ45J10NA5l7yT-oHQNFraM3TpjRUMGU4uBzezWSZgH747PMRvccS7tDwn-DQLSEUb2klK-dXAbgNOMlMLO0Qrlrek28tgpjYHUEAjj7IobAPDuoFp6j5zPWtd4YTeZ2_PynC_QqcT_ZoD35GlXrTjS87uMFNVC-DGPtYSpdvPovpAb5riAqn7gp4RbXnmuAXrcevJaQYXD01rccwh8mZI1AaWXGMD5RNaa3sQ2YX63_W3wemyUfTQ-tZdhr-9UkwMiuKWzC5q33aUUsDQ47QTuwCw2t4gUDEamVBfAj4ouHJiW9p2DZOd9js" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
تریلی رب چپ کرده و مردم با پا رفتن توی رب‌ها و دارن اینجوری کیسه کیسه رب جمع میکنن :
✅
@AloNews</div>
<div class="tg-footer">👁️ 42.8K · <a href="https://t.me/alonews/144199" target="_blank">📅 11:54 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144198">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hSeoNk25UFaeqlkW3ZSnxWG7JG66onXA_diszhnlAdlIEJ_obQyPAI8DVxFJ-UZ-iLV9QjpQRPVC9XMdaUvVueEGAkypIjX1i276BnkJGB7Qbosnz__az_d1-81jWD2KA9YZ2YjZijQOSkUjzu6qiuhvTK2CV67n4ews2Hq77GM1qF550TtNpsWFviPzWxVZrOQiRZi7TxvaJqjWTijQ34JOCaKXZ--3-mRY2S5L-v9vJYMgev95tx04QCzzQ9l6DCOdoZwcLiiGYfGw9jNXmZmCzXhpCzpu8Jm2iyZRqn_-CDa4mXoakvyuyaXslNFM2RMWn8xJfXCZ61otAJi1kQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
نبویان:
اگه اعتراض کنید زیر پا لهتون میکنیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 41.8K · <a href="https://t.me/alonews/144198" target="_blank">📅 11:44 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144197">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">🔴
طلا به زودی گرمی 30 میلیون
‼️
🔴
سکه  به زودی 250 میلیون
‼️
🔴
دلار به زودی 210 هزار تومان
‼️
🤍
اگه میخوای بدونی کی وقت خرید طلاست
کی وقت فروشش، تو این کانال بهت میگن
@Tala v dolar
👈</div>
<div class="tg-footer">👁️ 41.8K · <a href="https://t.me/alonews/144197" target="_blank">📅 11:44 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144196">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SZlIUfBK2OOke7IQ-inCjatLz6ixFZeTQ27WBk-eUjYMY9LYInNWl0eue-g-OeLB5VxjsQ94SdL84EM23Jb5gEeTHACfstgpvt5TZcRAlMWWd5ooD3oUu97ELbOWwE36Vwd7m_KVsK76gf464nyd3S-ygWqsCnp0JNTpbZihbECZ-RHsB3K4dtMGjQDprZ9ewdh0VzfcY-P_kvpICYdOQMT78jwZn7RZX59YZP5zMEkmDpuJPkrQNoncliEm71Ut1NQb7gsqwJcUXVck_JDUIqS3Ki4DmAOrYqosUhRzmQ6-XdyvmgmCkho8J8LfGxo5nO-UpdIqK-5lRGEvfYpp5Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
خلاصه وضعیت LNG در جهان
🔴
در سمت عرضه آمریکا، کانادا و روسیه تا حد خوبی کسری عرضه را جبران کردند از اون طرف در آسیا تقاضای چین کاهش داشته است
✅
@AloNews</div>
<div class="tg-footer">👁️ 42.9K · <a href="https://t.me/alonews/144196" target="_blank">📅 11:39 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144195">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">👈
داده‌های شرکت کپلر نشان می‌دهد روز پنجشنبه تنها ۵ کشتی باری از تنگه هرمز عبور کرده‌اند؛ در حالی که میانگین تردد روزانه در ۱۰ روز اخیر ۱۵ کشتی بوده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 41.9K · <a href="https://t.me/alonews/144195" target="_blank">📅 11:35 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144194">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9e4b9a3684.mp4?token=s4iUqBb5xtkNnyTFEpft0-FxVM5jkAUwYBoVQ6hG_TENkWULInJVPSDn-_XZNE9IShMThfBK7IEwZpvNPYeqRVjMbFAS2Jkjbe7i7i_3NixdHiYZ0A3xrtpEaUdyMP-eJ8DhjQQ_r2r8Kh53nTNIYPTPU7nPc-bO46G_udhzZzhhMdyNAbiiv_wCN0ukQvfx3gTdvxHnVW2CO1WwmTUuvA5k8m_s0eSqIjjK_CjSkjW1IHz-sSTRw0MZgxPMnRvBAZx3RW9ZCzBqjWKhyAaANosZ5hN4tRtcBdcw-1wIJ0WIr_tNNI_s9muXERupwLZtfUJIGPPoQPelnJYks40w9Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9e4b9a3684.mp4?token=s4iUqBb5xtkNnyTFEpft0-FxVM5jkAUwYBoVQ6hG_TENkWULInJVPSDn-_XZNE9IShMThfBK7IEwZpvNPYeqRVjMbFAS2Jkjbe7i7i_3NixdHiYZ0A3xrtpEaUdyMP-eJ8DhjQQ_r2r8Kh53nTNIYPTPU7nPc-bO46G_udhzZzhhMdyNAbiiv_wCN0ukQvfx3gTdvxHnVW2CO1WwmTUuvA5k8m_s0eSqIjjK_CjSkjW1IHz-sSTRw0MZgxPMnRvBAZx3RW9ZCzBqjWKhyAaANosZ5hN4tRtcBdcw-1wIJ0WIr_tNNI_s9muXERupwLZtfUJIGPPoQPelnJYks40w9Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
رپ خوانی یک مداح مفتخور و بیسواد و نمایش آیفون ۱۷ خودش
✅
@AloNews</div>
<div class="tg-footer">👁️ 43.9K · <a href="https://t.me/alonews/144194" target="_blank">📅 11:31 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144193">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">👈
رویترز: جنگ ایران پس از شش ماه به بن‌بستی پرهزینه رسیده و احتمال دارد تهران با الگویی شبیه حوثی‌ها، حملات دوره‌ای و مذاکرات مقطعی را برای فرسایشی‌کردن درگیری دنبال کند.
🔴
کشورهای خلیج فارس نیز فشار اقتصادی و دیپلماتیک را به جنگ دوباره ترجیح می‌دهند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 41.8K · <a href="https://t.me/alonews/144193" target="_blank">📅 11:30 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144192">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/63c3458609.mp4?token=REF47agmdolvR1tOVxML1Yh0p5AXDT6iyoCcvBIdgpoTWfD5v8JoJLmFDHSGf8VbcSkwRpTHMo9SDU-S2IYAzsgmEOcstvYGKxY92N6pGk4AxiLQgKpvDQlEGGm5r4l9IdBBj66rOrPrgJwHAaBw7UnrZbJrU-1e2btlf9jE-d-hwoDhV2oxJB2mBKczPNtGB3mtGlr6k5wu4zhLpZZPj-fWtFCt3Il_CQKpWmcJoq4RkmZtjl_30cvbnwZg1Ms4K6r7COKDSP_xA-g4HLqlWx-Hzho5riHWtVNYNeUYuyCqFYCQYttl80SR22GmW-lrDRTbYjKKUHOeHtVjUXyBRQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/63c3458609.mp4?token=REF47agmdolvR1tOVxML1Yh0p5AXDT6iyoCcvBIdgpoTWfD5v8JoJLmFDHSGf8VbcSkwRpTHMo9SDU-S2IYAzsgmEOcstvYGKxY92N6pGk4AxiLQgKpvDQlEGGm5r4l9IdBBj66rOrPrgJwHAaBw7UnrZbJrU-1e2btlf9jE-d-hwoDhV2oxJB2mBKczPNtGB3mtGlr6k5wu4zhLpZZPj-fWtFCt3Il_CQKpWmcJoq4RkmZtjl_30cvbnwZg1Ms4K6r7COKDSP_xA-g4HLqlWx-Hzho5riHWtVNYNeUYuyCqFYCQYttl80SR22GmW-lrDRTbYjKKUHOeHtVjUXyBRQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
صحبت های «جعفر قائم پناه» معاون اجرایی پزشکیان؛ که حسابی تندروها رو عصبانی کرده: اگه من بودم و میدونستم رهبر رو میزنن قطعا غنی سازی رو تعطیل میکردم.
✅
@AloNews</div>
<div class="tg-footer">👁️ 42.9K · <a href="https://t.me/alonews/144192" target="_blank">📅 11:25 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144191">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b0bbae2e77.mp4?token=kc3cB87LNI7ZpF7LtXwIXzd4p6OQ51USP8S7V-D2rL5syApWnYp_wWSyk1m3c8j5YVX-KVDCA45praL1873BjoRrY-IofeXA65q-84pfsx8_4VSECjQ97tuRCZl7feAGBzlWMaE2HnaTa5513vqmHUHqVg92zZELpONWveGDaeZ2YbptrOZNQP-A1rNF5l57CdkkN8ml4K3EcggTRhnsaAZ4enPedo9qgwxY4OvdSQWU5lI-nJk4piYfcgkTvDYRvdt0xLTnascz-Uh5PL_BAEADg_aWEwHGr2KeoWUhR1NtgKPFwaUDT0BhByA3wNwQWpiyNCqds4zE1DxKrmeVCA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b0bbae2e77.mp4?token=kc3cB87LNI7ZpF7LtXwIXzd4p6OQ51USP8S7V-D2rL5syApWnYp_wWSyk1m3c8j5YVX-KVDCA45praL1873BjoRrY-IofeXA65q-84pfsx8_4VSECjQ97tuRCZl7feAGBzlWMaE2HnaTa5513vqmHUHqVg92zZELpONWveGDaeZ2YbptrOZNQP-A1rNF5l57CdkkN8ml4K3EcggTRhnsaAZ4enPedo9qgwxY4OvdSQWU5lI-nJk4piYfcgkTvDYRvdt0xLTnascz-Uh5PL_BAEADg_aWEwHGr2KeoWUhR1NtgKPFwaUDT0BhByA3wNwQWpiyNCqds4zE1DxKrmeVCA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏
👈
صف های عجیب چند کیلومتری بنزین در روسیه!
✅
@AloNews</div>
<div class="tg-footer">👁️ 43.9K · <a href="https://t.me/alonews/144191" target="_blank">📅 11:13 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144190">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">👈
ویدئویی وحشتناک از حبس یک خانواده در میان سیل عظیم نپال
✅
@AloNews</div>
<div class="tg-footer">👁️ 44.9K · <a href="https://t.me/alonews/144190" target="_blank">📅 11:05 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144189">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">👈
روسیه: اسرائیل باید به ماجراجویی‌ نظامی در سوریه پایان دهد
✅
@AloNews</div>
<div class="tg-footer">👁️ 43.9K · <a href="https://t.me/alonews/144189" target="_blank">📅 11:00 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144188">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cSBdZzNuWz-Kp7C_ToGWBYrSs-FoHwEeGgQkoE7urYAWbFCAmH75uoaPvn6BxlO_x8uWiUhkCZd74TnMj4V5HsuZBo2gXQeA4CvWPV3lir4ENZ_Qh-eCzOkHmBKQyK1Lfa3-W1iYLxGyui9uXmu88clqUEkTtnWtilvrV_dcFC7DFe3K4qvoiW8uFQoJWfWoY9b0uuZaPc53XuB2R6uLSzctE0WQ9UEQWqTXON1POBVI8ykUJRdKYGxvREBqtsRIvOFQ8wk5N9PMTUhsbBhKmeoylXzZbxK1Y2sU5PUro5DiUf_WI9KgJ9yluXN_apixn5q975kPw79XajzBlcwBCw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
پادشاه نروژ، هارالد پنجم و مسن‌ترین صاحب تاج و تخت سلطنت در اروپا در ۸۹ سالگی درگذشت
✅
@AloNews</div>
<div class="tg-footer">👁️ 47K · <a href="https://t.me/alonews/144188" target="_blank">📅 10:45 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144187">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">👈
رویترز: با وجود ادامه تشدید تنش‌ها در رابطه با ایران، نفت به سمت ثبت زیان هفتگی پیش می‌رود که نشان می‌دهد بازارها همچنان محتاطانه با خطرات تشدید تنش برخورد می‌کنند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 46K · <a href="https://t.me/alonews/144187" target="_blank">📅 10:41 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144186">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/51590b7113.mp4?token=qEaGce6opR0BP8Y4aY6LA3UI9Wowcz-1Y1m7osUk9Vu-g6VXMBSDW1hdW1dfxwQi6T8dnJvX-8yWQcjqUGcu0oly8gnyDoQUoPUBFUrNWYOhzuI6vNeuB0BGIfDSZ5UEEOvJDD_j12_7DR7bWTFNWtEmqLbUAphCN46I0I2-xifU1n37mF0mmH7CB4uqd07SOqxMQCkzCRaTbvOBlsNSt8pz3ANwmOeQkZ67_DbZjQBjfPiU4kcAOxpX5v0cIh9t-t8JYqa7OTf7VrlJrtlvjXtrvS_0p0UZbudCj7DbPpBdkeykUjpJ0VjzoaQzjxrfCWlX2HKaTR5HNShNKepySw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/51590b7113.mp4?token=qEaGce6opR0BP8Y4aY6LA3UI9Wowcz-1Y1m7osUk9Vu-g6VXMBSDW1hdW1dfxwQi6T8dnJvX-8yWQcjqUGcu0oly8gnyDoQUoPUBFUrNWYOhzuI6vNeuB0BGIfDSZ5UEEOvJDD_j12_7DR7bWTFNWtEmqLbUAphCN46I0I2-xifU1n37mF0mmH7CB4uqd07SOqxMQCkzCRaTbvOBlsNSt8pz3ANwmOeQkZ67_DbZjQBjfPiU4kcAOxpX5v0cIh9t-t8JYqa7OTf7VrlJrtlvjXtrvS_0p0UZbudCj7DbPpBdkeykUjpJ0VjzoaQzjxrfCWlX2HKaTR5HNShNKepySw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
بندر رجایی در سکوت
کامل...
✅
@AloNews</div>
<div class="tg-footer">👁️ 48K · <a href="https://t.me/alonews/144186" target="_blank">📅 10:35 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144185">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YJeUu_DpL_7u2W-Yk6h5NU4MmtjWr0v0vZxRZ3Y_mkBXu32cMQN0RKoOTU_n22_Ds6RrKjNGYFpgKV3JpAwwVrweqcFQcXQ23yuw5ZGDhv3HOi6Auect7AVqA850CuR7VW3CjxvlUZ5BwdrhPOb8ay6wRvuqkJbsvg8BcMMg3R4YayJqxvbT0fn447oHltISdxdRMLxkJwUiQMeZoPb29kxOX9TCXVjqiwmmKR5yHA1r3ch3dPT6eLIKsft-VMazbbzKAo_ysJae1yZqvYq9EFdPSsS2VOpoWRIFP2u3QMeH_CqMK17Qwf--Y9Iv9mh4pTuRkWog98LadRXGPWIkIg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
نفت پس گمانه‌زنی ها مبنی بر کذب بودن ادعای وال استریت ژورنال با کاهش ۲.۵ دلاری وارد کانال ۸۷ دلار شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 45K · <a href="https://t.me/alonews/144185" target="_blank">📅 10:26 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144184">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tyYXp9BOjH5EM4kM7YZcJZzKtS5NlxFTBnRyus6c6nBNHA1897h3SzK_8x7UENAdy-_J5uHxQuJgWqx6hjZnFhP1bn4uzRdBYdZFw1cUG2wRjT0smP8QagyebxVUPzy4q44RcQgJayMji1uB1cJ3m4a5HClF0s2tdodDaSXerhVLylLhnsylktxy2z7ETuVHXIjllYSiuUGJbZ1-sMge8Be2CM1cpctxDctS3hzBSa4zIk4ksdUn4nGShd9Hit2-tFO8ah9-hjxJWwORt2xUGOQNNYfwtFs2xSATkKMyXPHyaCty31zA8g1DNBwrfur3v4uBLKmWdmSt5wA-D8OUWQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
عراقچی: آمریکا باید یک واقعیت ساده را درک کند؛ فشار نتیجه نمی‌دهد
🔴
وزیر امور خارجه کشورمان پس از سفر دیروز نخست وزیر قطر به تهران: با نخست‌وزیر و وزیر امور خارجه قطر، گفت‌وگوهای سازنده و مبتکرانه‌ای در تهران داشتیم.
🔴
بازگرداندن دیپلماسی به مسیر خود ناممکن نیست. این امر به درک یک واقعیت ساده از سوی آمریکا بستگی دارد: فشار نتیجه نمی‌دهد. آمریکا باید اعتماد ایجاد کند، با احترام سخن بگوید، حقوق ما را تصدیق کند و به تعهدات خود پایبند باشد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 49K · <a href="https://t.me/alonews/144184" target="_blank">📅 10:18 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144183">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">👈
لاوروف: بریتانیا منفی‌ترین نقش را در درگیری اوکراین دارد
✅
@AloNews</div>
<div class="tg-footer">👁️ 43.9K · <a href="https://t.me/alonews/144183" target="_blank">📅 10:12 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144182">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jKYkf1UIv1ar3AogG56MjgdFiGu_XXd2c45nReMs3sJ5i9pqeRuPUP8M6w9uqIa4x6bGLXKTWyHireBuVzqezvyWQQkEmzRQ4iyThpvrc_HR_GFQx1xknLJHW1MT1i85875IStfU0KnyrKUZDUhH-ZVcU_BuuJ9A7kMvzmID1DZL5xIxpJWQOP-S-g2KcGI_GDfdnOU52EW0sStzBUf_Zx9LsMUWB8PKp_PvoTnUsbnim2g8UDaJOGaEm2r79BUna1itAK_S6wxwIGUL2cTFLPBRFXUb3HUmiDfTYOyW-uTgfA50COrgZhxjmuTdWtvKRypRS5lBjJRMszqFaXsA8Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
👈
الجزیره: ایران و قطر درباره ایجاد کریدور موقت کشتیرانی در تنگه هرمز، پاکسازی مین‌های دریایی و کاهش تنش‌های منطقه‌ای رایزنی کردند؛ هم‌زمان تلاش‌ها برای ازسرگیری مذاکرات تهران و واشنگتن ادامه دارد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 46K · <a href="https://t.me/alonews/144182" target="_blank">📅 10:04 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144181">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">👈
مقام ارشد وزارت خزانه‌داری آمریکا: تلاش ترامپ برای تحت فشار قرار دادن مسئولان مالی اعضای گروه (جی۲۰) برای قطع شریان‌های اقتصادی ایران
🔴
ترامپ تصمیم دارد تا مسئولان مالی گروه ۲۰ را ترغیب کند تا هفته آینده بر سر گام‌هایی برای تقویت رشد اقتصادی، کاهش عدم تعادل‌های جهانی و رویارویی با چالش‌های بدهی‌های دولتی به توافق برسند
✅
@AloNews</div>
<div class="tg-footer">👁️ 43.7K · <a href="https://t.me/alonews/144181" target="_blank">📅 09:59 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144180">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/860c4887d1.mp4?token=oioaYr1mluLsiP7Vwmlxz5eXjYplNpHVNzMX2aDsnNswkFOWaanFsqSTpd6NQnah6FJNxCz7rSrgHO8EThcJRz9Qu8vSLRnp6oT8FoIwOIyeUg-PpThJBwiyfEYfmv76YyLBxw9hlNgdsGTvstZQLvuliq3esGOpaiMGZfutENxrztREWLYWmDjBgFNV80J_45cOfmzyHsITSuWMNh0I5v6KDTGsLHSqtIyZ9QO97lqa8rNAjwMGK1YF-qlLrckBckxDL7uE1Rf24umJ4X_AInbvJ_DtiTKIAXjY4H9371L5qhA7HRSoUULQOuGZxSZ1pwuRxkDQ2wGexmcHSG5SRg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/860c4887d1.mp4?token=oioaYr1mluLsiP7Vwmlxz5eXjYplNpHVNzMX2aDsnNswkFOWaanFsqSTpd6NQnah6FJNxCz7rSrgHO8EThcJRz9Qu8vSLRnp6oT8FoIwOIyeUg-PpThJBwiyfEYfmv76YyLBxw9hlNgdsGTvstZQLvuliq3esGOpaiMGZfutENxrztREWLYWmDjBgFNV80J_45cOfmzyHsITSuWMNh0I5v6KDTGsLHSqtIyZ9QO97lqa8rNAjwMGK1YF-qlLrckBckxDL7uE1Rf24umJ4X_AInbvJ_DtiTKIAXjY4H9371L5qhA7HRSoUULQOuGZxSZ1pwuRxkDQ2wGexmcHSG5SRg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
تصاویر ماهواره‌ای از سیل عظیم نپال که نشان می‌دهد آن منطقه کاملا تخریب شده
✅
@AloNews</div>
<div class="tg-footer">👁️ 45.2K · <a href="https://t.me/alonews/144180" target="_blank">📅 09:57 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144179">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Oa7nkbGkJYdOYGR42_MW6Z_Or_RCx9Q4L1shpjX8h4twaJ_mulH25H5m3zsdXNxETkmS9p1hwCEAPl6xfbUaPMjwS3mJXJ3gLF86IIMOIwCqw_HPtvR2rf-AG-2KdxDNGVTZLGJyxdzBGeH7zKFNJxyyXby0zafOWIHHe_cWIumcwU5aqxjrGekrnsOEQSkr5SdGWOdj-UK8TcD5fNvk46LGg5BVp3wjnaMEcVGAhIINBCADGOtgkSQuJdTHLEbwVIxUx67ZhZBvwRa_E1jmJWZ36UfVCt_cwvWf-b1JGZVVD975wWqJs4hMcycZHbN67F9ZVnx7ve9Zwh_BKJ-nrQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ترامپ بار دیگر مدعی شد که
تنگه
هرمز اکنون بخشی از قلمرو جدید آمریکا محسوب می‌شود.
✅
@AloNews</div>
<div class="tg-footer">👁️ 44.9K · <a href="https://t.me/alonews/144179" target="_blank">📅 09:53 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144178">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eAWiApnhqSILj63vayT66MntEXlDXXgP8OUa-o0UqFO3MJ11pEQEPvvUJI7AgT90QUKx_w0vVCmeFHlVoj7uvRtN1fE61D5DhtjCVMUoi9jobk7Pq_1Dhc4doz9_chVLy2-70fQnZbIYZiLZZjAyKjMYbSgJQMU1cbBmtbpBqNCaTGdwMB_73_u-lbbH0r3Mb9cE1-5oJlMNUNhp19HyhaTvlUrI5Zfp3D-vAANReHC_JdFQTzozyBbMjobGnnB1nyRAukCsKc6wD_lMaQt582WY9jVfyUplGM0gocedEu3ir0lXyxXCE9t1AF9noG4CznoW0ldQ6bYTnqrkfxMW_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
اسکات بسنت، وزیر خزانه‌داری ایالات متحده
:
محاصره و عملیات طرد اقتصادی، اقتصاد رو به زوال ایران را ویران خواهد کرد.
🔴
ایالات متحده در ۱۴ روز گذشته، ۱۳۰ میلیون بشکه را هدایت کرده است.
🔴
ایران: ۰
✅
@AloNews</div>
<div class="tg-footer">👁️ 43.6K · <a href="https://t.me/alonews/144178" target="_blank">📅 09:50 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144177">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">👈
دریادار
برد کوپر
، فرمانده فرماندهی مرکزی آمریکا (CENTCOM)، مدعی شد که نیروهای آمریکایی عبور
۱۵۰۰ کشتی تجاری
و
۷۵۰ میلیون بشکه نفت خام
از تنگه هرمز را تسهیل کرده‌اند، در حالی که
به ایران اجازه صادرات هیچ مقدار نفت خامی داده نشده است.
🔴
دریادار کوپر همچنین مدعی شد که
هیچ کشتی ایرانی بدون اجازه CENTCOM وارد یا از بنادر ایران خارج نشده است
و کشتی‌ها تنها به دلایل
بشردوستانه
اجازه تردد پیدا می‌کنند.
🔴
او همچنین مدعی شد که از زمان آغاز
محاصره دریایی بنادر ایران توسط نیروی دریایی آمریکا
، حدود
۷۵ کشتی تغییر مسیر داده‌اند
و
۳ کشتی نیز از کار انداخته شده‌اند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 44.1K · <a href="https://t.me/alonews/144177" target="_blank">📅 09:46 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144176">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">👈
رئیس سازمان سنجش اعلام کرد: نتایج اولیه کنکور احتمالاً ۲۶ یا ۲۷ شهریور منتشر می‌شود. داوطلبان پس از اعلام نتایج تا ۵ مهر فرصت انتخاب رشته خواهند داشت
✅
@AloNews</div>
<div class="tg-footer">👁️ 43.2K · <a href="https://t.me/alonews/144176" target="_blank">📅 09:42 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144175">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">👈
بلومبرگ: ونزوئلا به‌طور جدی در حال بررسی خروج از اوپک، سازمان کشورهای صادرکننده نفت، است؛ سازمانی که بیش از ۶۰ سال پیش در تأسیس آن نقش داشت.
🔴
موضوع خروج ونزوئلا در جریان گفت‌وگوها با مقام‌های آمریکایی مطرح شده، هرچند هنوز تصمیم نهایی در این‌باره گرفته نشده است.
🔴
خروج ونزوئلا می‌تواند پرسش‌های بیشتری دربارۀ انسجام اوپک و توانایی این سازمان برای تأثیرگذاری بر قیمت جهانی نفت ایجاد کند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 45.1K · <a href="https://t.me/alonews/144175" target="_blank">📅 09:35 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144174">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">👈
روغن ۲۵۸٪ گران شد!
🔴
طبق گزارش مرکز آمار ایران، قیمت روغن و چربی‌ها در مرداد ۱۴۰۵ نسبت به مرداد سال گذشته «۲۵۸.۲ درصد افزایش»داشته است. در همین مدت، تورم خوراکی‌ها، آشامیدنی‌ها و دخانیات به «۱۲۸.۱ درصد» رسیده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 46K · <a href="https://t.me/alonews/144174" target="_blank">📅 09:26 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144173">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UIXUBpIbbrzqOxMSNVjFLSbmzHAhiBi97_tFcK0wwEtdCocRB6oMDNumBtZebT5p0Y6p-_BFvT2VJefC0OCMr56ZWsYUYjIGpZqmb-t2SuCbrzRYExgoCvL0rlfT9uOcr9TfUngNvafCy426K_ikqpBWGuHkhN5SiuMzVzOZQe62SsJJYVVFdzd3SkGNKwv-p79hLASwVsb0CZi581g7ed2J3RhbDe3xblmnhkV2b1zsX_5AH65WrzfPOwGcXbo904Xxanio5aLI1ESCAGXO6dEqL2D0kFSYa4ax8cl84axiYx4wRcRO7J-Zs5aqL6coDDoPdxAXlTyWDXbbxdSyig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
👈
پلیس نپال: شمار قربانیان سیل اخیر در این کشور به ۴۶۹ کشته افزایش یافت و جستجو برای یافتن مفقودان همچنان ادامه دارد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 47.4K · <a href="https://t.me/alonews/144173" target="_blank">📅 09:03 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144172">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">👈
وال استریت ژورنال: آمریکا از روسیه خواست روابط اقتصادی و امنیتی خود را با ایران متوقف کند
✅
@AloNews</div>
<div class="tg-footer">👁️ 46.3K · <a href="https://t.me/alonews/144172" target="_blank">📅 08:56 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144171">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">👈
رسانه‌های آمریکا: رئیس سیا از روسیه خواسته اطلاعاتی را با ایران به اشتراک نگذارد
✅
@AloNews</div>
<div class="tg-footer">👁️ 46.9K · <a href="https://t.me/alonews/144171" target="_blank">📅 08:52 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144170">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">👈
سازمان عملیات تجارت دریایی انگلیس تأیید کرد نفتکش «السلام ۲» متعلق به کویت، شامگاه پریشب در ساعت ۲۱:۵۰ به وقت جهانی مورد اصابت قرار گرفته است.
🔴
پیش از این، عصر همان روز نفتکش یونانی «مترو ونیزی» هدف حمله قرار گرفته بود.
🔴
توالی این حوادث طی روزهای اخیر، نگرانی‌ ها دربارۀ افزایش خطرات امنیتی برای تردد نفتکش‌ها و حمل‌ و نقل دریایی در منطقه را تشدید کرده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 48.6K · <a href="https://t.me/alonews/144170" target="_blank">📅 08:48 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144169">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rVWaoenwkEUtD4w-RC97z4McC-M6WpwDrvHPc6HNhYRYS0PD47GJPbYc0HwMUwTmgDoUQ3WSn3NlwUYlH_ACE58Y94-mzZgGYmBvS7Zt-EnG6n-T11cwdndAyy2egVXW-wJ9YrsGwhr_u6DH3-pvJY8jUp46cH_2eDv1vEvdHfSp4GqrESqpgsLZGreasBylLKwKaiDjT0m6sXbjsqPnMKv343FNCLrqneKViWs8rmLeOZJ7OWOg7UPii6p8rNLJTJpDuxCB863k5xGCE4KZAbkZaDg-m_LCbXPOuI3gv6x9pboEPilyepu7lHRNEm0rPQPBsf5T6alt1BVPYjCCOg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
واکنش نخست‌وزیر کانادا به تغییر نام دریاچه اونتاریو به «دریاچه آمریکا» توسط ترامپ
🔴
نام دریاچه اونتاریو از واژه وندات «اونتاریو» گرفته شده است که به‌درستی به معنای «دریاچه زیباست، دریاچه بزرگ است» است.
🔴
این نام بیش از ۴۰۰ سال قدمت دارد و پیش از کنفدراسیون کانادا و اعلامیه استقلال ایالات متحده آمریکا وجود داشته است
🔴
ما می‌دانیم که آمریکا در حال تغییر است. روابط تجاری‌شان، سیاست‌های خارجی‌شان، بناهای ملی‌شان، نام‌های آب‌هایشان.
🔴
کانادایی‌ها همچنین می‌دانند که این نام در واقعیت، دریاچه اونتاریو است - آن زمان، اکنون و همیشه
✅
@AloNews</div>
<div class="tg-footer">👁️ 47.7K · <a href="https://t.me/alonews/144169" target="_blank">📅 08:44 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144168">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rm_7tdjq1liaAKRpHQmyEyC3MixPg0UpjudSCsj1pK_DyiChBdRAeQCiYT_XO9Cxxgh3RYqq5iiuFe7b_tStY1j9uY085xnV36FWLb9HPs4H8JAiTL_0ghaZup4fVZDul6Rula_YEzSN6JSrYKJ51-_r-qIhsnYZRHeOk4b6cNW1IcsI_N56tnkWBWXnZoP58wOeyIAgQwpWplDlopCE5ytQl-cjBesKCG3aor24e94F5Efom2x6I8T6D24YBsewrfXzSmgUKbt6Ag8BdWn9zROEfPzH0ZyFrKr6fMT2jtQ1bqI8WGt8I1H-AoBEQWmXFkD046LPDkkO6jhcpnXCtA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
خشم شدید ترامپ از شبکه فاکس‌نیوز به خاطر پخش گزارشی درباره ایران
🔴
دونالد ترامپ در تروث سوشال:
جاناتان هانت از فاکس‌نیوز گزارش بسیار نادرستی درباره ایرانِ شکست‌خورده منتشر کرد.
🔴
من نمی‌خواهم دیداری داشته باشم؛ آنها هستند که می‌خواهند دیدار کنند. در واقع، برای توافق التماس می‌کنند.
🔴
برت بایر باید، برای یک‌بار هم که
شده، زیردستان بی‌کفایت خود را سر و سامان بدهد!
✅
@AloNews</div>
<div class="tg-footer">👁️ 53.2K · <a href="https://t.me/alonews/144168" target="_blank">📅 08:40 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144167">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jVE1uIRKQRp3FSFg4K9G3_2ZeHd5mvInm7wvSKaN2CfTfQ_rtALrAz4pbCNRZc34IR-NOsuUR4eamAS-C3nDyphbEZCl0JW1XhEY5JBz9vj_bpp-wCRp98l3zHc8XU93F3ysklvhUAPeTfDyuRcAeqNycFlYNcV4SCc2DlOpfJP_N0Z0_GXMbpuVsMGaV6j_8EyQaLfEP6dgU7Qb3JXOucRQ9QfAzs-4UJngb3P77hcGU2iq4d4a4bOSae1UQiqmkBpOh3vhtMkbVinDaae6LdVYG8VFjMgMDE1pKuZYXYeRSR_5r3T75Aa7d2tQ1VLNmJ0A77VMXqsAzCLu6r5EDQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
توییت جدید ترامپ: ایران کشوری رو به فروپاشی است
✅
@AloNews</div>
<div class="tg-footer">👁️ 53.8K · <a href="https://t.me/alonews/144167" target="_blank">📅 08:34 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144166">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/M6eVDvX_-GXqDHRD38iPuqkRUqhVYVO_JftMk6HI3cONN3Hi00Egxjrgoj9eofHXLRckp6nQkoeKyxm_qQRRbT4klU_42bXC6FyZ6_d1CM9GfFwM4LkhIiBq0gI3WVtbjtLkm6WqA_YYx-7wQPy71LIuDWJBZF4r795HfJ7gPEnFDS7MAzAaYaPBfD3i2QJYFxXu1-Qu1WVlbRI20As4Eq48L3vl4D_BHweScpuUATKludQc-r9iNm4oI04E23ScBopz6PykRVgbHNzfjNJH3cnQgko0XGmuGJv0aTzRLiW_ikzaCyyzdbFkbHF0tL0EVRAJ9iFsjYfX1CAcQ6br8A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ترامپ، فهرستی از رتبه‌بندی روسای جمهور آمریکا را منتشر کرد و خود را به عنوان "بزرگترین" در این فهرست قرار داد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 67.2K · <a href="https://t.me/alonews/144166" target="_blank">📅 01:23 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144165">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/W5m4GNZUiuA1h1qMxyStMKiiHQGfkVm4LFk69Q5h0a3AFImy_-6xnwXSVg4A8cta3iT7hCBKhadwL_D-_YAzJF_orGF65W7BngmSy_perhOG7wlbS7H3K6UpjvBtaop7eCilXui0JE8S-qt5JMTsygx1Nb7zRk8ZUP-ICPanwGZjzkl7zVF26M27qEV7oBcLNCkaTUQwd1WRzLn0T0l3b_wPEsaWMv50eSz-Usc8EZurPFsJNZCGf8zivkkxGM1SzVcbKH2iZ1XGV3ksyxotIuH0kAE4zbRn0Zb21GaG3lPr-h8BXNCIyxY2sBu0niXWGuQhmRyeu4x5qIsh-9iFgg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
برای اولین بار تور افغانستان گردی برای مردم ایران موجود کردن تو مملکت
🔴
قیمت تور ۷ روزه‌ هم ناقابل ۵۰ میلیون تومنه.
✅
@AloNews</div>
<div class="tg-footer">👁️ 67.4K · <a href="https://t.me/alonews/144165" target="_blank">📅 01:03 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144164">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JinEhrZlJraX3ewM3eIWNIUoITKW9pkjAIOzDDh8QsbdmnNDXh3j1pRxyDD5DxCM8R0TQhxFkJZLs0ke3g1SgLYjcVmdETZwnPB6jA2ihAtBv_Wbl96V5rDSAYsrZCsJx87Q3vGh4Psw9UQIHz7s4g5IFLpYwY0PM902ASyLXxAG1p-i47mEfI6wI7XdoWOqQeOilN16yKB4qN4ttY9vXaNHo87u3_VfU6f46aKbdTEQij72mkHSl5sJFrqZD2KcHn8M8TAH0oW8TYyIh-gttBdkiGZ8U3_zTOoYRzL6PYAVCEy9D6ub3mxM-UIezBB0Imlpuq8y8aQ9_-Yhd0E4DA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
امیراحمد کاظمی؛ کارشناس اقتصاد:
اثر واقعی محاصره دریایی آمریکا هنوز شروع نشده. گندم؛ ذرت؛ سویا؛ برنج؛ شکر؛ شیرخشک و کلی کالای حجیم دیگه در مقیاس موردنیاز ایران عملاً به حمل دریایی وابسته‌ان.
دریا که قفل بشه؛ فقط کشتی‌ها متوقف نمیشن؛ بلکه زنجیره تأمین قفل میشه. اول کرایه و بیمه میره بالا؛ بعد واردات کند میشه؛ بعد موجودی انبارها آب میره و در نهایت قیمت‌ها میتونن منفجر بشن.
اگر محاصره طول بکشه داستان از «اختلال واردات» میتونه به «بحران عرضه» تبدیل بشه. آخر مهر آغاز موج بشدت گسترده گرونی کالا هاست.
✅
@AloNews</div>
<div class="tg-footer">👁️ 68.6K · <a href="https://t.me/alonews/144164" target="_blank">📅 00:47 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144163">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qNWsvAg93_yx6uQZLWuqO7dFFXg2D6sy6zZPH2Uud4y0pIdQ-A2TRKBjXzobe3wgpzLF7BoCczK5Gz_Bynmk8kTR0HvT6F31FfH24kc8uy8PiR0KIPJo2sXMKMD428501eo6uqeAvTEdZNL_hUIyJtFlyOVs712lIywBLkSvpQTLRlEScgg4Z90rm2km5o5rh6SOnwZM0bUKDxjcCKcGdEhyMFyikH9CqIk4P9phOG-djmnVJx97ZnE3S4acsq1YP_p5QwBbWfv5ik5AeRd4-Rbjr_IP8YCOff4jOCzSya5eYe6XdZGCrruMudP2dZnBrkZ9LNczwl-foE_I2KJFmg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
فیلد مارشال: جنوب لبنان خط قرمز ماست
✅
@AloNews</div>
<div class="tg-footer">👁️ 66.6K · <a href="https://t.me/alonews/144163" target="_blank">📅 00:37 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144162">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">👈
تریلر کامل GTA VI منتشر شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 67.1K · <a href="https://t.me/alonews/144162" target="_blank">📅 00:23 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144161">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">به جای روزی دو ساعت خبر خوندن، پنج دقیقه کانال ماهان رو بخون هر خبری درمورد تورم و گرونی هست اول اینجا میزاره
https://t.me/+6PPyWURHtW5jN2M0</div>
<div class="tg-footer">👁️ 64.3K · <a href="https://t.me/alonews/144161" target="_blank">📅 00:22 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144160">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/390cb79159.mp4?token=In6hkYtvvO_F9tY4_Z3lRaKnVeljuhtc09wD1WxDGNosjErABLguux31THBT_QmoecE16dNK4Nqs4405TMXuM0XTIt353E6IblzJreH7zF2aX74VStEthmRJ7zT7aEOGyU6CHCApYydPGkX4e-q-9zHSrsGGyy7plSEGpH9inzTxlx7E1-bXUPRRYphc-1pH37nT3x1mm6gY9DEZNC-c2iLdoNHEIcGzdh9vysG61NbAjQ03KPLaXTs3Z9fqFEvQEUivJQe_LIYU_Cztw4RUju5MeDOAsqNmBm_X0bmwz80bhbzqY8PFwNRyYuX-C5Jkb7CpvgixjDPC_U_NzSrRNg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/390cb79159.mp4?token=In6hkYtvvO_F9tY4_Z3lRaKnVeljuhtc09wD1WxDGNosjErABLguux31THBT_QmoecE16dNK4Nqs4405TMXuM0XTIt353E6IblzJreH7zF2aX74VStEthmRJ7zT7aEOGyU6CHCApYydPGkX4e-q-9zHSrsGGyy7plSEGpH9inzTxlx7E1-bXUPRRYphc-1pH37nT3x1mm6gY9DEZNC-c2iLdoNHEIcGzdh9vysG61NbAjQ03KPLaXTs3Z9fqFEvQEUivJQe_LIYU_Cztw4RUju5MeDOAsqNmBm_X0bmwz80bhbzqY8PFwNRyYuX-C5Jkb7CpvgixjDPC_U_NzSrRNg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
وزیر نیرو : هر کسی میخواد برقش قطع نشه میتونه از بورس برق با قیمت آزاد خریداری کنه
✅
@AloNews</div>
<div class="tg-footer">👁️ 69.2K · <a href="https://t.me/alonews/144160" target="_blank">📅 00:05 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144159">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">👈
کویت و پاکستان توافق‌نامه همکاری دفاعی و نظامی امضا کردند
🔴
این توافق‌نامه بر تبادل تجربیات و ارتقای آمادگی نیروهای مسلح دو کشور تمرکز دارد
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.8K · <a href="https://t.me/alonews/144159" target="_blank">📅 23:50 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144158">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">👈
فیلد مارشال محسن رضایی: ایران فهرستی از شروط خود را برای انتقال به آمریکایی‌ها آماده کرده
🔴
ایران در حال حاضر یک مسیر موقت و مشخص برای عبور کشتی‌ها در وسط تنگه را مجاز دانسته است، به شرطی که آینده تردد در آن منوط به تفاهمنامه با واشنگتن باشد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 65.7K · <a href="https://t.me/alonews/144158" target="_blank">📅 23:37 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144157">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4699eef4cb.mp4?token=DM1WbSLd3uVypf7zD7RuimHMC1ud2W3nULhxeUtQO5xb4ZjZjd87PvYSjSisFGbiwM_OoVsv4go95iSho7vzXUUuJez4mI-rlNf7UZtsG_FtMpekgv9DR9GJpewVroekAcR0M6yOlvla0pfl7ZwNXxDZCoaufeXQ_wp0sH5ip1mE_4s3pHdHNzMsMU5580Bj3GR9OxTmSlTlaQ_DpxCgxjkMoG2Brq6KDOLeF_qSxAHDnipo1IUzmCSRk2XozK8yKK2O27X5ssV_B9JDYirkHQP18QA5AbE8QfcRlGFifmVOVIbUPcOQOCKKrNnyt8NKpk2hPTzVMzlX_f0vp7pkVQZ4qS9EE9lPSL88nwar6byP1vEKSCwDqBGQvSuHBxaZsArMHJ-mnHDhwnULJXN4bEe9LGvuMJjcC_XLlC8kQeqKbqZFlYT04UhEKnP4gSlxCfZB17jZzYUEwRQfGKEoGnePNUO2Sl8kNaAtwG0MNONKnB0SS5OFQ81DL0PdYwThOXoiADZXGOFvNT87b8-a_MvByVDyvtsoUuk0b34LClnfjowlPuZM7xJBKX-j3YVLGImNDPv8p75YxtdER8VRJkiBCFDtfdgVMcXAirB0HFfyU4loas6IBvWwqPn0pP3koWoEqcAFqCWwJtvt_l4PwXtWOcnYdrEPdaaWMRFQS1U" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4699eef4cb.mp4?token=DM1WbSLd3uVypf7zD7RuimHMC1ud2W3nULhxeUtQO5xb4ZjZjd87PvYSjSisFGbiwM_OoVsv4go95iSho7vzXUUuJez4mI-rlNf7UZtsG_FtMpekgv9DR9GJpewVroekAcR0M6yOlvla0pfl7ZwNXxDZCoaufeXQ_wp0sH5ip1mE_4s3pHdHNzMsMU5580Bj3GR9OxTmSlTlaQ_DpxCgxjkMoG2Brq6KDOLeF_qSxAHDnipo1IUzmCSRk2XozK8yKK2O27X5ssV_B9JDYirkHQP18QA5AbE8QfcRlGFifmVOVIbUPcOQOCKKrNnyt8NKpk2hPTzVMzlX_f0vp7pkVQZ4qS9EE9lPSL88nwar6byP1vEKSCwDqBGQvSuHBxaZsArMHJ-mnHDhwnULJXN4bEe9LGvuMJjcC_XLlC8kQeqKbqZFlYT04UhEKnP4gSlxCfZB17jZzYUEwRQfGKEoGnePNUO2Sl8kNaAtwG0MNONKnB0SS5OFQ81DL0PdYwThOXoiADZXGOFvNT87b8-a_MvByVDyvtsoUuk0b34LClnfjowlPuZM7xJBKX-j3YVLGImNDPv8p75YxtdER8VRJkiBCFDtfdgVMcXAirB0HFfyU4loas6IBvWwqPn0pP3koWoEqcAFqCWwJtvt_l4PwXtWOcnYdrEPdaaWMRFQS1U" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
پزشکیان: چیزی که در تفاهم‌نامه نوشتیم و امضا کردیم به نظر من سند افتخار جمهوری اسلامی است
‏
🔴
بارها گفتم همه عزیزان شورای امنیت از این تفاهم‌نامه با قدرت دفاع کردند
✅
@AloNews</div>
<div class="tg-footer">👁️ 65.2K · <a href="https://t.me/alonews/144157" target="_blank">📅 23:21 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144156">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KAcEvIkkyFz1O-abwnfO3IaueX3LfcaYBQotxXlruOehQf_Dm-LNHoTUDmRtHypMwiUWyGSVN9p3WgdpP2fodfYB0jguD5cC9CUNS9XvaqCc8d6i4UQhq-H3ajKIGBEbBzEf3M_pdBwhLuaEv2eelX1r_aLt8cx4XNZZp62EZPOBG_nWoYvalTzDPylgVtNQY1XFl7awE7xP1t2yyGnLnFs7KcssWDZ1XJogcgwK4ilhK7_-9QaCd8sxmdu6RjvB2kh57vZoKDbix90qdQ_a7bvqrWgSN9mERaPenWEWf4hJyPlsSasmdt5VIFuW2QshgU-1oUE6DYnPLxnwy4d_6Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ترامپ در Truth Social: خبر فوق‌العاده! شرکت Micron، یکی از داغ‌ترین شرکت‌های جهان، به‌تازگی از یک سرمایه‌گذاری عظیم ۱۰ میلیارد دلاری برای ساخت آزمایشگاه‌های تحقیقاتی جدید، همین‌جا در آمریکا، خبر داده است.
🔴
این شرکت کمک می‌کند آمریکا در هوش مصنوعی و رایانش پیشرفته همچنان در خط مقدم مطلق باقی بماند!
🇺🇸
🔴
به‌دلیل سیاست‌های عالی ما، شرکت‌ها در حال سرمایه‌گذاری تریلیون‌ها دلار هستند.
🔴
من کاملاً روشن کرده‌ام که آمریکا راه را به‌سوی یک عصر طلایی جدید در علم رهبری خواهد کرد. نتایج خودشان گویای همه‌چیز هستند: در دوران دولت من، شرکت‌ها تریلیون‌ها دلار سرمایه‌گذاری می‌کنند، چون می‌دانند آمریکا بهترین مکان جهان برای ساختن، اختراع کردن و رشد کردن است.
🔴
ما در حال تقویت اقتصادمان هستیم و خیلی بزرگ پیروز می‌شویم!
🔴
عصر طلایی آمریکا همین حالا اینجاست. MAGA!
🇺🇸
🇺🇸
🇺🇸
✅
@AloNews</div>
<div class="tg-footer">👁️ 61.7K · <a href="https://t.me/alonews/144156" target="_blank">📅 23:17 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144155">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dpQxUaJVErCfEIDMWXpt9eICt6JU-akFmzlYzLCC7DUp-eWSwLaX775GXJIfaZj_5ef1laL1hImLHJDfphsEeGrertgdCf_bFicu5TFKfCxOt7SLBcdHBeV9zl8v-J0z87Gmt-2TyuogQdWB2A9jhUpxVDd5nUQ-1HCgti4th9OkpuDriBxkPpI51r--4uUf85IDnNJpFOC-0T0cnmeDKz_QMDofZqIB3gTqABJt5ULlZL19ld4RSz4TQAMh9QYSYBjFCSqY6E_pQwsf56qpP1sPm5mvScZi28RHDI-2DcPRplnrRtM84VmVyrgb37lPYwVg_P7oRhGadwUFrS1FvQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ر
ئیس کمیسیون امنیت ملی: تنها مسیر نجات آمریکا، بازگشت به تفاهم‌نامه است
✅
@AloNews</div>
<div class="tg-footer">👁️ 60.4K · <a href="https://t.me/alonews/144155" target="_blank">📅 23:14 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144154">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">👈
محسن رضایی: اگر محاصره ادامه پیدا کند، ما منافع اقتصادی آمریکا را صد در صد و با شدت و قدرت هدف قرار خواهیم داد
✅
@AloNews</div>
<div class="tg-footer">👁️ 61.1K · <a href="https://t.me/alonews/144154" target="_blank">📅 23:10 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144153">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">👈
فیلد مارشال محسن رضایی: ضاحیه و بیروت خط قرمز جمهوری اسلامی هستن و اگه اسرائیل این مناطق لبنان رو بزنه بهش حمله میکنیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 60.5K · <a href="https://t.me/alonews/144153" target="_blank">📅 23:06 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144152">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">👈
وال استریت ژورنال : ترامپ منتظر نتایج تاثیر جنگ اقتصادی علیه ایران است. ترامپ دیگر اهمیتی برای یادداشت تفاهم با ایران قائل نیست
✅
@AloNews</div>
<div class="tg-footer">👁️ 59.5K · <a href="https://t.me/alonews/144152" target="_blank">📅 23:06 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144151">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">👈
فیلد مارشال محسن رضایی: ضاحیه و بیروت خط قرمز جمهوری اسلامی هستن و اگه اسرائیل این مناطق لبنان رو بزنه بهش حمله میکنیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 59.3K · <a href="https://t.me/alonews/144151" target="_blank">📅 23:02 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144150">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">👈
گفت‌وگوی وزرای خارجه مصر و روسیه درباره پیشنهاد مشترک ایران و عمان برای ایجاد یک کریدور موقت دریایی در تنگه هرمز
✅
@AloNews</div>
<div class="tg-footer">👁️ 59.8K · <a href="https://t.me/alonews/144150" target="_blank">📅 22:46 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144149">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">👈
فیلد مارشال محسن رضایی: ایران ۸۰ میلیون بشکه نفت در دوره آتش‌بس صادر کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 59.7K · <a href="https://t.me/alonews/144149" target="_blank">📅 22:40 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144148">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">👈
این وسط کافه بابک زنجانی پلمپ شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 58.7K · <a href="https://t.me/alonews/144148" target="_blank">📅 22:26 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144147">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c42582d38c.mp4?token=kHjhxJDBSkA9OLhi_AX6YusoIkycgVtiaH94zTlkuobqpZroM9N_7l22Fcx6dSINFeiaGeFVoqGXd7UzlOMt5jm1_iCd2lBP5PkbciNMptVa_eP0MewN_l66uTG7ONBd4ekSJ3kYPHFhnlpms6RSIl0O0uHPR3Dt3kbVKHEYz_souqGjv6JNulQBvtwx6t7gogjAlUwrC7PvCMe_6IXgU7T6wOVAZq56Y4mKdrwVkHSUWYluzbO5_UKuboezqNHCjgn2Esvcrquhx-Z8TTFmJAQPbMedSes8obBHe08sZXHRjsb3qZztg2o7MuqwbIu7TecrzFQg1MixffBBIE_gS4o-7ms5lCvxzPuYMVgw-QXW5y1su0tdLXa6nPyyuiZ_drLW-E1wH09WsYS6CKJhGUd49WoposZ63rWcBx0bP-HRclG0w6t8-yfHboQFX-cdDFjV4Vyh-9BM8-i0w3MJwIeWnrmjjho94f1bGZrvxKD4m0032sCPkWj1bw2hIbapCbCc1F6xeRE-xadHEQCNlhBazGli-B3MALxEBJc-YvNwHWGxkGwTSzM0K44OGjtHAcdz0uNs_yLqrTVslcZzfnmHAWy-N0CmGSxRcYvXQbXb-3751SNr6PeOOY8iPmVJgzbPb0fBKjZIlFy7Kp8wqAPXpD0JE-TZdf2GwJykjx8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c42582d38c.mp4?token=kHjhxJDBSkA9OLhi_AX6YusoIkycgVtiaH94zTlkuobqpZroM9N_7l22Fcx6dSINFeiaGeFVoqGXd7UzlOMt5jm1_iCd2lBP5PkbciNMptVa_eP0MewN_l66uTG7ONBd4ekSJ3kYPHFhnlpms6RSIl0O0uHPR3Dt3kbVKHEYz_souqGjv6JNulQBvtwx6t7gogjAlUwrC7PvCMe_6IXgU7T6wOVAZq56Y4mKdrwVkHSUWYluzbO5_UKuboezqNHCjgn2Esvcrquhx-Z8TTFmJAQPbMedSes8obBHe08sZXHRjsb3qZztg2o7MuqwbIu7TecrzFQg1MixffBBIE_gS4o-7ms5lCvxzPuYMVgw-QXW5y1su0tdLXa6nPyyuiZ_drLW-E1wH09WsYS6CKJhGUd49WoposZ63rWcBx0bP-HRclG0w6t8-yfHboQFX-cdDFjV4Vyh-9BM8-i0w3MJwIeWnrmjjho94f1bGZrvxKD4m0032sCPkWj1bw2hIbapCbCc1F6xeRE-xadHEQCNlhBazGli-B3MALxEBJc-YvNwHWGxkGwTSzM0K44OGjtHAcdz0uNs_yLqrTVslcZzfnmHAWy-N0CmGSxRcYvXQbXb-3751SNr6PeOOY8iPmVJgzbPb0fBKjZIlFy7Kp8wqAPXpD0JE-TZdf2GwJykjx8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
نفتالی بنت، نخست‌وزیر سابق اسرائیل:
دخترم ابیگیل، زمانی که افکار عمومی علیه ما شروع به تغییر کرده بود، در شهری در کرواسی بود.
🔴
او در صف بستنی ایستاده بود. فروشنده بستنی را برایش آماده کرده بود، اما بعد از او پرسید: "از اسرائیل هستی؟"
🔴
دخترم گفت: "بله."
🔴
فروشنده بستنی را برداشت، گفت: "اسرائیل؟ نه" و آن را دور انداخت.
🔴
دخترم به او نگاه کرد و گفت: "Fu*k you." من واقعاً به او افتخار می‌کنم. خیلی زیاد
✅
@AloNews</div>
<div class="tg-footer">👁️ 58.1K · <a href="https://t.me/alonews/144147" target="_blank">📅 22:22 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144146">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">👈
عراقچی: کشورهای منطقه نباید اجازه استفاده آمریکا از خاک خود علیه ایران را بدهند
✅
@AloNews</div>
<div class="tg-footer">👁️ 54K · <a href="https://t.me/alonews/144146" target="_blank">📅 22:20 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144145">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/359a9e5dcb.mp4?token=umK4wGs-JNJD-YeiwETw5bpDeFtVPd7nVBv-4ksypMhHZKz4_c9KJhsIjnnLGE4aN8EvUOjvbPWETKnYX6jT_4djz1ByksW2VNIFp2IOfCKh8pbosjsca8gJXDrARFGg1PJt28DJ2dWZEGpxjl0a_05ecFF9VhjpPh9QT0gOOUapJ4uT6QvsphpVp8P5Y_qF9WjnQutiZdbqbD_wI7mDQTXkXWkiR4C8qh1NqomjGitZ-3koFOngmENGBlYcMbKPaL-AGmNadlKVBDIja5Azrv3G5WOxqqbEI7TOYDqyeo5a_SIddqQnYSJxvbXiqcnCELM3sHB0g_vOgN6y8sfwgg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/359a9e5dcb.mp4?token=umK4wGs-JNJD-YeiwETw5bpDeFtVPd7nVBv-4ksypMhHZKz4_c9KJhsIjnnLGE4aN8EvUOjvbPWETKnYX6jT_4djz1ByksW2VNIFp2IOfCKh8pbosjsca8gJXDrARFGg1PJt28DJ2dWZEGpxjl0a_05ecFF9VhjpPh9QT0gOOUapJ4uT6QvsphpVp8P5Y_qF9WjnQutiZdbqbD_wI7mDQTXkXWkiR4C8qh1NqomjGitZ-3koFOngmENGBlYcMbKPaL-AGmNadlKVBDIja5Azrv3G5WOxqqbEI7TOYDqyeo5a_SIddqQnYSJxvbXiqcnCELM3sHB0g_vOgN6y8sfwgg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
سلاح ضد پهپاد جدید اوکراین برای مقابله با کوادهای FPV
🔴
این گجت جیبی یک پرتابگر تور است که تا ۲۵ متر برد دارد
✅
@AloNews</div>
<div class="tg-footer">👁️ 56.4K · <a href="https://t.me/alonews/144145" target="_blank">📅 22:08 · 05 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
